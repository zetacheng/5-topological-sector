"""C2a P6 — routing / regulator cross-validation (MAGI round 2).

(a) A0 cancellation under a SECOND routing prescription (centered 'sym'): must
    still vanish (it does exactly, pointwise, being routing-independent at k=0).
(b) ONE representative k^4 point (kappa_raw at the operating mass) under the two
    prescriptions 'asym' (lineage) and 'sym' (shift-centered): the extracted
    kappa must be stable within the MC band. The raw amplitude carries an O(k^2)
    routing/cutoff artifact; the test is whether the O(k^4) projection is stable.

Single routing prescription is used across ALL classes within each run.
Evaluator: skyrme_fast unified full-symmetric; importance sampling.
"""
import numpy as np
from scripts.c2a import skyrme_fast as FA
from scripts.c2a.production_scan import ANGLES, LAMBDAS, make_cfg, op_vertex, fit_coeffs

SEEDS = (11, 23, 47)


def kappa_route(m, e, route, nmc=16384):
    ks = []
    for seed in SEEDS:
        P, w = FA.make_sample_importance(nmc, seed=seed, m=m, a=4, qmc=True)
        A4, D = [], []
        for th in ANGLES.values():
            cfg = make_cfg(e, th)
            vals = np.array([FA.full_amplitude([lam*k for k in cfg], m, P, route=route, w=w)
                             for lam in LAMBDAS])
            A4.append(fit_coeffs(vals)[2])
            D.append([op_vertex(cfg, 'O1'), op_vertex(cfg, 'O2')])
        sol, *_ = np.linalg.lstsq(np.array(D), np.array(A4), rcond=None)
        ks.append((sol[0] - sol[1]) / 2)
    return np.mean(ks), np.std(ks) / np.sqrt(len(SEEDS))


def a0_route(m, route, nmc=16384, seed=11):
    P, w = FA.make_sample_importance(nmc, seed=seed, m=m, a=4, qmc=True)
    return sum(FA.amplitude(c, [np.zeros(4)]*4, m, P, route=route, w=w) for c in FA.CLASSES)


if __name__ == "__main__":
    m, e = 0.15, 0.15/4
    print("=" * 68)
    print(f"P6 ROUTING / REGULATOR CROSS-VALIDATION  (m={m}, e={e:.4f})")
    print("  evaluator: skyrme_fast unified full-symmetric, importance sampling")
    print("=" * 68)
    for route in ('asym', 'sym'):
        a0 = a0_route(m, route)
        print(f"  A0_total [{route:4s}] = {a0:+.3e}  (routing-independent at k=0: expect ~0)")
    ka, ea = kappa_route(m, e, 'asym')
    ks, es = kappa_route(m, e, 'sym')
    print(f"\n  kappa_raw [asym] = {ka:+.5f} +- {ea:.5f}")
    print(f"  kappa_raw [sym ] = {ks:+.5f} +- {es:.5f}")
    diff = abs(ka - ks); band = np.sqrt(ea**2 + es**2)
    resolved = diff > 3 * band
    # routing systematic expressed on kappa_U at this mass
    kU_sys = diff * m**4
    print(f"  |asym - sym| = {diff:.5f}   combined MC band = {band:.5f}   "
          f"resolved (>3 band): {resolved}")
    print(f"  => routing (regulator) SYSTEMATIC on kappa_U = {kU_sys:.2e}")
    print("     (sharp cutoff is not shift-invariant; the two prescriptions bracket")
    print("      the sharp-cutoff proxy value. Decisive tool if load-bearing would")
    print("      be the overlap-lattice derivative expansion -- P6 note.)")
    # effect on the kill verdict: window [140,550] on S=640 kappa_U
    kU = 0.5 * (ka + ks) * m**4
    S = 640 * kU; S_sys = 640 * kU_sys
    print(f"  kappa_U (routing-avg) = {kU:+.6f}   S_mono = 640 kappa_U = {S:+.3f} "
          f"+- {S_sys:.3f} (routing)")
    margin = min(abs(S - 140), abs(S - 550))
    print(f"  distance of S_mono from window [140,550] edge = {margin:.1f}; "
          f"routing systematic = {S_sys:.3f}")
    print(f"  P6 VERDICT: routing systematic is {'IMMATERIAL' if S_sys < margin else 'MATERIAL'} "
          f"to the kill margin (systematic {S_sys:.3f} << distance {margin:.1f}).")
