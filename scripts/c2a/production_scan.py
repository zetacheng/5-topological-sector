"""C2a PRODUCTION SCAN — kappa_raw / kappa_U via the full five-class amplitude.

CONFIG CONFIRMATION (printed in every header): all k!=0 production points are
evaluated through the unified full-symmetric evaluator (skyrme_fast.py, validated
to machine precision against skyrme_full.py). The lineage box() is a REGRESSION
REFERENCE ONLY and is never mixed into production numbers.

Method (spec sec.3-5):
  * amplitude(lambda*cfg) fit in the constant-included basis {1,L^2,L^4,L^6};
    A0=L^0 (must be ~0 for the full set), A4=L^4 (Skyrme), A6=L^6 (contamination).
  * plateau: e in {m/6, m/4, m/3} (all <= m/3); kappa_raw(e) stable => plateau.
  * overdetermination: >=4 kinematic configs projecting O1,O2; least-squares
    solve D[c1,c2]=A4 with residual reported (basis systematic).
  * kappa_raw = (c1-c2)/2 ; kappa_U = m^4 * kappa_raw   (P1: H3 => m^4 factor).
Fixed seeds, printed configs. Second party re-verifies with a different evaluator.
"""
import sys
import numpy as np
from itertools import permutations
from scripts.c2a import skyrme_fast as FA

LAMBDAS = np.array([0.4, 0.55, 0.7, 0.85, 1.0])
EFRAC = {'m/6': 1/6, 'm/4': 1/4, 'm/3': 1/3}
# four kinematic configs: planar family cfg(e,theta), angles chosen for a
# well-conditioned O1/O2 design matrix (condition number printed).
ANGLES = {'A(90)': np.pi/2, 'B(45)': np.pi/4, 'C(30)': np.pi/6, 'D(120)': 2*np.pi/3}
SEEDS = (11, 23, 47)
FLAV = [1, 2, 1, 2]


def make_cfg(e, theta):
    k0 = np.array([e, 0.0, 0.0, 0.0])
    k1 = np.array([e*np.cos(theta), e*np.sin(theta), 0.0, 0.0])
    return [k0, k1, -k0, -k1]           # sum = 0


def op_vertex(cfg, which):
    """Tree kinematic structures O1,O2 for flavour pattern (1,2,1,2) (lineage)."""
    tot = 0.0
    fl = [0, 1, 0, 1]
    for perm in permutations(range(4)):
        l = [cfg[i] for i in perm]; f = [fl[i] for i in perm]
        if f[0] == f[1] and f[2] == f[3]:
            if which == 'O1':
                tot += (l[0] @ l[1]) * (l[2] @ l[3])
            else:
                tot += (l[0] @ l[2]) * (l[1] @ l[3])
    return tot


def fit_coeffs(vals):
    """Constant-included fit vals(lambda) ~ c0 + c2 L^2 + c4 L^4 + c6 L^6."""
    X = np.vstack([LAMBDAS**0, LAMBDAS**2, LAMBDAS**4, LAMBDAS**6]).T
    c, *_ = np.linalg.lstsq(X, np.asarray(vals), rcond=None)
    return c   # [c0(A0), c2(A2), c4(A4), c6(A6)]


def amp_lambda_scan(cfg, m, P, w):
    """Full five-class amplitude at each lambda*cfg (unified evaluator, per lambda)."""
    return np.array([FA.full_amplitude([lam*k for k in cfg], m, P, w=w) for lam in LAMBDAS])


def kappa_for_e(m, e, P, w):
    """One (m,e): per-config A0/A4/A6, overdetermined O1/O2 solve, kappa_raw."""
    A0s, A4s, A6s, D = [], [], [], []
    for name, th in ANGLES.items():
        cfg = make_cfg(e, th)
        vals = amp_lambda_scan(cfg, m, P, w)
        c = fit_coeffs(vals)
        A0s.append(c[0]); A4s.append(c[2]); A6s.append(c[3])
        D.append([op_vertex(cfg, 'O1'), op_vertex(cfg, 'O2')])
    D = np.array(D); A4 = np.array(A4s)
    sol, res, rank, sv = np.linalg.lstsq(D, A4, rcond=None)
    c1, c2 = sol
    kappa_raw = (c1 - c2) / 2
    resid = float(np.sqrt(res[0])) if res.size else float(
        np.linalg.norm(D @ sol - A4))
    cond = sv[0] / sv[-1]
    return {
        'kappa_raw': kappa_raw, 'A0': np.array(A0s), 'A4': A4, 'A6': np.array(A6s),
        'resid': resid, 'cond': cond, 'c1': c1, 'c2': c2,
    }


def scan_mass_seed(m, seed, nmc):
    """One (mass, seed): per-e kappa_raw + diagnostics. Emits CSV rows to stdout.

    CSV: DATA,m,seed,elabel,e,kappa_raw,A0max,resid,cond,A6A4
    """
    print(f"# C2a PRODUCTION  m={m} seed={seed} NMC={nmc}")
    print(f"# EVALUATOR: skyrme_fast unified full-symmetric (5 classes), ONE routing;")
    print(f"#           lineage box() is REGRESSION REFERENCE ONLY, not used here.")
    print(f"# NON-SINGLET (1,2,1,2); A0_total=0 exact (Goldstone). Not eta sector.")
    print(f"# lambdas={list(LAMBDAS)} angles(deg)="
          f"{ {k: round(np.degrees(v),1) for k,v in ANGLES.items()} }")
    print(f"# SAMPLER: importance rho(r)~r^3/(r^2+m^2)^4 (Sobol QMC), taming box variance")
    P, w = FA.make_sample_importance(nmc, seed=seed, m=m, a=4, qmc=True)
    for elabel, ef in EFRAC.items():
        e = ef * m
        info = kappa_for_e(m, e, P, w)
        A0max = float(np.max(np.abs(info['A0'])))
        A6A4 = float(np.max(np.abs(info['A6'])) / (np.max(np.abs(info['A4'])) + 1e-30))
        print(f"DATA,{m},{seed},{elabel},{e:.6f},{info['kappa_raw']:.8f},"
              f"{A0max:.3e},{info['resid']:.3e},{info['cond']:.4f},{A6A4:.5f}")


if __name__ == "__main__":
    m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.30
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    nmc = int(float(sys.argv[3])) if len(sys.argv) > 3 else 50_000
    scan_mass_seed(m, seed, nmc)
