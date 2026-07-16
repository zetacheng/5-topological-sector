"""C2a aggregation: read production_scan per-(m,seed) outputs, build kappa_U(m)
with the stacked error band, fit the log law kappa_U(m)=a ln(Lambda/m)+b, and
print the kill-criterion arithmetic. NO verdict prose here -- table + band only
(checkpoint output). Second party re-derives from the committed CSV + this code.
"""
import sys, glob, os
import numpy as np

MASSES = [0.08, 0.12, 0.15, 0.20, 0.30]
SEEDS = [11, 23, 47]
EFRAC = {'m/6': 1/6, 'm/4': 1/4, 'm/3': 1/3}
LAMBDA = 1.0


def load(scandir):
    """rows[(m,seed,elabel)] = dict(kappa_raw,A0max,resid,cond,A6A4)."""
    rows = {}
    # Path 1: committed CSV (results/scan_data.csv) -- header row, no DATA prefix.
    if os.path.isfile(scandir) and scandir.endswith(".csv"):
        for line in open(scandir):
            if line.startswith("m,seed") or not line.strip():
                continue
            m, seed, el, e, kr, a0, res, cond, a6 = line.strip().split(",")
            rows[(float(m), int(seed), el)] = dict(
                e=float(e), kappa_raw=float(kr), A0max=float(a0),
                resid=float(res), cond=float(cond), A6A4=float(a6))
        return rows
    # Path 2: raw per-(m,seed) scan .out files (DATA, prefix).
    for f in glob.glob(os.path.join(scandir, "*.out")):
        for line in open(f):
            if not line.startswith("DATA,"):
                continue
            _, m, seed, el, e, kr, a0, res, cond, a6 = line.strip().split(",")
            rows[(float(m), int(seed), el)] = dict(
                e=float(e), kappa_raw=float(kr), A0max=float(a0),
                resid=float(res), cond=float(cond), A6A4=float(a6))
    return rows


def build(rows):
    out = {}
    for m in MASSES:
        # kappa_raw[e][seed]
        per_e_seed = {el: [rows[(m, s, el)]['kappa_raw'] for s in SEEDS
                           if (m, s, el) in rows] for el in EFRAC}
        if any(len(v) < len(SEEDS) for v in per_e_seed.values()):
            continue
        e_means = {el: np.mean(per_e_seed[el]) for el in EFRAC}
        e_mcerr = {el: np.std(per_e_seed[el], ddof=1) / np.sqrt(len(SEEDS)) for el in EFRAC}
        kappa_raw = np.mean(list(e_means.values()))          # plateau central
        mc_err = np.sqrt(np.mean([e_mcerr[el]**2 for el in EFRAC]))
        plateau_spread = max(e_means.values()) - min(e_means.values())
        resid = np.mean([rows[(m, SEEDS[0], el)]['resid'] for el in EFRAC])
        A0max = np.max([rows[(m, s, el)]['A0max'] for s in SEEDS for el in EFRAC])
        cond = rows[(m, SEEDS[0], 'm/3')]['cond']
        A6A4 = np.mean([rows[(m, SEEDS[0], el)]['A6A4'] for el in EFRAC])
        # stacked band (added in quadrature): MC, plateau(H1), overdet(basis)
        band = np.sqrt(mc_err**2 + (plateau_spread/2)**2 + resid**2)
        out[m] = dict(kappa_raw=kappa_raw, mc_err=mc_err, plateau_spread=plateau_spread,
                      resid=resid, band_raw=band, kappa_U=m**4 * kappa_raw,
                      band_U=m**4 * band, A0max=A0max, cond=cond, A6A4=A6A4,
                      e_means=e_means)
    return out


def logfit(out):
    ms = np.array(sorted(out))
    y = np.array([out[m]['kappa_U'] for m in ms])
    w = np.array([1/max(out[m]['band_U'], 1e-9)**2 for m in ms])
    X = np.vstack([np.log(LAMBDA/ms), np.ones_like(ms)]).T
    W = np.diag(w)
    beta = np.linalg.solve(X.T@W@X, X.T@W@y)          # [a, b]
    resid = y - X@beta
    cov = np.linalg.inv(X.T@W@X)
    aerr, berr = np.sqrt(np.diag(cov))
    chi2 = float(resid@W@resid)
    dof = len(ms) - 2
    return dict(a=beta[0], b=beta[1], aerr=aerr, berr=berr, chi2=chi2, dof=dof,
                resid=resid, ms=ms, y=y)


def report(scandir):
    rows = load(scandir)
    out = build(rows)
    print("=" * 78)
    print("C2a PRODUCTION AGGREGATE — kappa_U(m) table + stacked band (CHECKPOINT)")
    print("  evaluator: skyrme_fast unified full-symmetric (lineage box NOT mixed in)")
    print("=" * 78)
    print(f"{'m':>6} {'kappa_raw':>11} {'kappaU':>12} {'bandU':>11} "
          f"{'MC':>9} {'plat':>9} {'resid':>9} {'|A0|':>8} {'cond':>6} {'L6/L4':>7}")
    for m in sorted(out):
        d = out[m]
        print(f"{m:6.2f} {d['kappa_raw']:+11.5f} {d['kappa_U']:+12.6f} "
              f"{d['band_U']:11.6f} {d['mc_err']:9.5f} {d['plateau_spread']:9.5f} "
              f"{d['resid']:9.2e} {d['A0max']:8.1e} {d['cond']:6.2f} {d['A6A4']:7.3f}")
    if len(out) >= 3:
        lf = logfit(out)
        print("\n  LOG-LAW FIT  kappa_U(m) = a ln(Lambda/m) + b   (Lambda=1)")
        print(f"    a = {lf['a']:+.5f} +- {lf['aerr']:.5f}")
        print(f"    b = {lf['b']:+.5f} +- {lf['berr']:.5f}")
        print(f"    chi2/dof = {lf['chi2']:.3f}/{lf['dof']} = {lf['chi2']/max(lf['dof'],1):.3f}")
        print(f"    fit residuals (kappaU - fit): {np.array2string(lf['resid'], precision=5)}")
        good = lf['chi2'] / max(lf['dof'], 1) < 5.0
        print(f"    log-law consistency (validity gate): "
              f"{'OK' if good else 'FAIL -> INCONCLUSIVE'}")
        # operating-point kappa_U (use m=0.15 as representative operating point)
        mop = 0.15
        kop = out[mop]['kappa_U'] if mop in out else lf['a']*np.log(1/mop)+lf['b']
        bandop = out[mop]['band_U'] if mop in out else abs(lf['a'])*0.1
        print(f"\n  OPERATING POINT m={mop}: kappa_U = {kop:+.5f} +- {bandop:.5f}")
        # kill-criterion arithmetic (N=3): S_mono = 640 * kappa_U
        for label, kv, bv in [('operating m=0.15', kop, bandop)]:
            S = 640.0 * kv; Sband = 640.0 * bv
            print(f"\n  KILL-CRITERION ARITHMETIC ({label}):")
            print(f"    S_mono = 640 * kappa_U = {S:+.2f} +- {Sband:.2f}")
            print(f"    window [140, 550]; inside: {140 <= S <= 550}")
    return out


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else "results/c2a/raw/scan_data.csv"
    report(d)
