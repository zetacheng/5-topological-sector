"""C2a startup regression (MANDATORY, before anything new).

Reproduces the pilot P3 numbers with the CONSTANT-INCLUDED fit (NMC=4e5, seed 11)
to confirm the environment matches before any new diagram classes are added.

The pilot P2 finding: the box-only amplitude has A0 = box(k=0) != 0 (the box is a
chirally incomplete set), and the old fit basis {L^2,L^4,L^6} lacked a constant,
so A0 leaked into the L^4 coefficient and diverged as 1/e^4. The fix used here is
the constant-included basis {1, L^2, L^4, L^6}: the L^0 coefficient absorbs A0 and
the L^4 coefficient (-> kappa_raw) is clean.

Targets (m, e): A0, kappa_raw
    0.30, 0.10:  -0.07973, -0.235
    0.30, 0.05:  -0.07973, -0.280
    0.15, 0.05:  -0.14327, -5.561

NOTE: this measures the NON-SINGLET SU(2) orientation/Skyrme coefficient
(pion-direction legs, alternating flavour), for which exact Goldstone-ness makes
A0_total = 0 an exact requirement once the full diagram set is included. It does
NOT measure the anomalous U(1)_A singlet (eta) sector.
"""
import numpy as np
from itertools import permutations
from scripts.common.euclidean_gamma import g, g5

G5 = g5.astype(complex); GM = [g[1], g[2], g[3], g[4]]
rng = np.random.default_rng(11)
NMC = 400_000; CH = 100_000; VOL = np.pi**2/2          # NMC = 4e5, seed 11
pts = rng.normal(size=(NMC, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
P = pts*(rng.uniform(size=NMC)**0.25)[:, None]


def Sb(Pc, k, m):
    q = Pc + k; q2 = np.einsum('ni,ni->n', q, q)
    sl = (q[:, 0, None, None]*GM[0] + q[:, 1, None, None]*GM[1]
          + q[:, 2, None, None]*GM[2] + q[:, 3, None, None]*GM[3])
    return (-1j*sl + m*np.eye(4))/(q2 + m*m)[:, None, None]


def box(kk, m):
    """Box class: 4x V1 (i m gamma5 theta) legs; old flavour weights (-2,+2,+2)."""
    orders = [((0, 1, 2, 3), -2.0), ((0, 1, 3, 2), 2.0), ((0, 2, 1, 3), 2.0)]
    tot = 0.0
    for od, fl in orders:
        k1, k2, k3, k4 = [kk[i] for i in od]; acc = 0.0
        for s in range(0, NMC, CH):
            Pc = P[s:s+CH]
            S1 = Sb(Pc, np.zeros(4), m); S2 = Sb(Pc, k1, m)
            S3 = Sb(Pc, k1+k2, m); S4 = Sb(Pc, k1+k2+k3, m)
            M = np.einsum('ab,nbc,cd,nde,ef,nfg,gh,nha->n',
                          G5, S2, G5, S3, G5, S4, G5, S1, optimize=True)
            acc += np.sum(M.real)
        tot += fl*(-1.0)*(acc/NMC)*VOL/(2*np.pi)**4
    return tot


def op_vertex(kk, which):
    tot = 0.0
    for perm in permutations(range(4)):
        l = [kk[i] for i in perm]; fl = [0, 1, 0, 1]; f = [fl[i] for i in perm]
        if which == 'O1' and f[0] == f[1] and f[2] == f[3]:
            tot += (l[0] @ l[1])*(l[2] @ l[3])
        if which == 'O2' and f[0] == f[1] and f[2] == f[3]:
            tot += (l[0] @ l[2])*(l[1] @ l[3])
    return tot


def a4_const(cfg, m, lams=(0.4, 0.55, 0.7, 0.85, 1.0)):
    """Constant-included fit: returns (A0 = L^0 coeff, A4 = L^4 coeff)."""
    vals = [box([lam*k for k in cfg], m) for lam in lams]
    L = np.array(lams); X = np.vstack([L**0, L**2, L**4, L**6]).T
    c, _, _, _ = np.linalg.lstsq(X, np.array(vals), rcond=None)
    return c[0], c[2]


def kappa_raw(m, e):
    cfgA = [np.array([e, 0, 0, 0]), np.array([0, e, 0, 0]),
            np.array([-e, 0, 0, 0]), np.array([0, -e, 0, 0])]
    cfgB = [np.array([e, 0, 0, 0]), np.array([0.7*e, 0.71*e, 0, 0]),
            np.array([-e, 0, 0, 0]), np.array([-0.7*e, -0.71*e, 0, 0])]
    A0A, A4A = a4_const(cfgA, m); _, A4B = a4_const(cfgB, m)
    Mx = np.array([[op_vertex(cfgA, 'O1'), op_vertex(cfgA, 'O2')],
                   [op_vertex(cfgB, 'O1'), op_vertex(cfgB, 'O2')]])
    c1, c2 = np.linalg.solve(Mx, np.array([A4A, A4B]))
    return A0A, (c1 - c2)/2


if __name__ == "__main__":
    targets = [(0.30, 0.10, -0.07973, -0.235),
               (0.30, 0.05, -0.07973, -0.280),
               (0.15, 0.05, -0.14327, -5.561)]
    print("C2a STARTUP REGRESSION (constant-included fit, NMC=4e5, seed 11)")
    ok = True
    for m, e, tA0, tk in targets:
        A0, kap = kappa_raw(m, e)
        pa = abs(A0 - tA0) < 5e-5; pk = abs(kap - tk) < 5e-4
        ok = ok and pa and pk
        print(f"  m={m}, e={e}:  A0={A0:+.5f} (P3 {tA0:+.5f}) {'OK' if pa else 'XX'} | "
              f"kappa_raw={kap:+.3f} (P3 {tk:+.3f}) {'OK' if pk else 'XX'}")
    print(f"STARTUP REGRESSION: {'PASS' if ok else 'FAIL'}")
    raise SystemExit(0 if ok else 1)
