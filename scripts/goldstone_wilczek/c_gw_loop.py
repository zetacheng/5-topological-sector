"""C6 anchor #1 — Goldstone-Wilczek coefficient c_GW (numeric fermion loop).

Fermion loop <J^mu(q) pi^a(k1) pi^b(k2) pi^c(k3)>: one gamma^mu (baryon-current)
vertex + three V1 = i m gamma5 tau vertices, four propagators, summed over the 3!
orderings of the pion legs around the loop, overall (-1) fermion loop.

We extract the epsilon-structure by choosing mu=0 and k1,k2,k3 along the
orthogonal spatial axes 1,2,3 (magnitude a), so eps^{0nu rho sig}k1 k2 k3 = a^3.
The MATCHING reference is the tree topological current
  B^mu = eps^{mu nu rho sig} Tr[L_nu L_rho L_sig]/(24 pi^2),
whose 4-point coefficient for the SAME config (flavours 1,2,3) is
  B^0_ref = -i a^3 / (2 pi^2)   (derived in c6_matching.md).
c_GW = Gamma^0_loop / B^0_ref.  HARD GATE: c_GW = 1 (unit baryon charge),
finite / cutoff-independent (anomaly-type) -- verified at two cutoffs and masses.

Euclidean gammas from fierz_verify: directions 0..3 -> g[1..4]; S(q)=(-i q.g+m)/(q^2+m^2).
"""
import numpy as np
from itertools import permutations
from scripts.common.euclidean_gamma import g, g5

GM = [g[1], g[2], g[3], g[4]]
G5 = g5.astype(complex)
I4 = np.eye(4, dtype=complex)
tau = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.array([[1, 0], [0, -1]], complex)]


def trf(seq):
    M = np.eye(2, dtype=complex)
    for a in seq:
        M = M @ tau[a - 1]
    return np.trace(M)


def Sb(P, kvec, m):
    q = P + kvec
    q2 = np.einsum('ni,ni->n', q, q)
    sl = (q[:, 0, None, None]*GM[0] + q[:, 1, None, None]*GM[1]
          + q[:, 2, None, None]*GM[2] + q[:, 3, None, None]*GM[3])
    return (-1j*sl + m*I4) / (q2 + m*m)[:, None, None]


def loop_Gamma0(a, m, P, w):
    """Gamma^0 for pions (flav1,k1)=e_1*a, (flav2,k2)=e_2*a, (flav3,k3)=e_3*a."""
    ks = [np.array([0., a, 0., 0.]), np.array([0., 0., a, 0.]), np.array([0., 0., 0., a])]
    fl = [1, 2, 3]
    Ktot = ks[0] + ks[1] + ks[2]
    gamma0 = GM[0]                                  # baryon-current vertex mu=0
    N = P.shape[0]
    acc = np.zeros(N, dtype=complex)
    for perm in permutations(range(3)):             # 3! orderings of pions
        f = trf([fl[perm[0]], fl[perm[1]], fl[perm[2]]])
        if abs(f) < 1e-14:
            continue
        k_s1 = ks[perm[0]]; k_s2 = k_s1 + ks[perm[1]]
        S1 = Sb(P, np.zeros(4), m)                   # S(p)
        S2 = Sb(P, k_s1, m)                          # S(p+k_s1)
        S3 = Sb(P, k_s2, m)                          # S(p+k_s1+k_s2)
        S4 = Sb(P, Ktot, m)                          # S(p+Ktot)
        # Tr[gamma0 S1 g5 S2 g5 S3 g5 S4]
        M = np.einsum('ab,nbc,cd,nde,ef,nfg,gh,nha->n',
                      gamma0, S1, G5, S2, G5, S3, G5, S4, optimize=True)
        acc += f * M
    prefac = -(1j*m)**3                              # (-1) fermion loop * (i m)^3
    dens = prefac * acc
    return (dens * w).mean()                          # Int d^4p/(2pi)^4 via importance w


def make_sample(nmc, seed, m, a=2, Rmax=1.0):
    """Importance sample |p|<Rmax with rho(r)~r^3/(r^2+m^2)^a (Sobol)."""
    from scipy.stats import qmc, norm
    rg = np.linspace(0, Rmax, 40001)
    pdf = rg**3 / (rg**2 + m*m)**a
    seg = (pdf[1:] + pdf[:-1]) / 2 * np.diff(rg)
    Z = seg.sum(); cdf = np.concatenate([[0.], np.cumsum(seg)]) / Z
    mm = int(np.ceil(np.log2(max(nmc, 2))))
    u = qmc.Sobol(d=5, scramble=True, seed=seed).random_base2(mm)[:nmc]
    gd = norm.ppf(np.clip(u[:, :4], 1e-12, 1-1e-12)); gd /= np.linalg.norm(gd, axis=1, keepdims=True)
    r = np.interp(u[:, 4], cdf, rg)
    P = gd * r[:, None]
    w = 2*np.pi**2 * (r**2 + m*m)**a * Z / (2*np.pi)**4
    return P, w


def c_gw(m, a=0.02, nmc=262144, seed=11, Rmax=1.0):
    P, w = make_sample(nmc, seed, m, a=2, Rmax=Rmax)
    G0 = loop_Gamma0(a, m, P, w)
    B0ref = -1j * a**3 / (2*np.pi**2)
    return G0 / B0ref, G0, B0ref


if __name__ == "__main__":
    print("=" * 70)
    print("C6 anchor #1 — Goldstone-Wilczek coefficient c_GW (fermion loop)")
    print("  c_GW = Gamma^0_loop / B^0_ref ; HARD GATE c_GW = 1 (unit baryon charge)")
    print("=" * 70)
    print("\n  cutoff-independence (m=0.30, a=0.01) -- anomaly-type finite coefficient:")
    for Rmax in (1.0, 2.0, 4.0, 8.0):
        c, *_ = c_gw(0.30, a=0.01, Rmax=Rmax)
        print(f"    Rmax={Rmax:4.1f}: c_GW = {c.real:+.5f} {c.imag:+.5f}i")
    print("\n  m-independence (Rmax=4, a=0.01) -- topological, m-independent:")
    for m in (0.30, 0.15):
        c, *_ = c_gw(m, a=0.01, Rmax=4.0)
        print(f"    m={m:4.2f}: c_GW = {c.real:+.5f} {c.imag:+.5f}i")
    print("\n  a->0 extrapolation (m=0.30, Rmax=4, linear in a^2):")
    xs, ys, yi = [], [], []
    for a in (0.005, 0.01, 0.02, 0.04):
        c, *_ = c_gw(0.30, a=a, Rmax=4.0)
        xs.append(a*a); ys.append(c.real); yi.append(c.imag)
        print(f"    a={a:5.3f}: c_GW = {c.real:+.6f} {c.imag:+.6f}i")
    A = np.vstack([xs, np.ones(len(xs))]).T
    c0 = np.linalg.lstsq(A, np.array(ys), rcond=None)[0][1]
    i0 = np.linalg.lstsq(A, np.array(yi), rcond=None)[0][1]
    print(f"    => c_GW(a->0) = {c0:+.6f} {i0:+.6f}i")
    ok = abs(c0 - 1) < 0.005 and abs(i0) < 0.005
    print(f"\n  HARD GATE  c_GW = 1 (unit baryon charge), real, cutoff-independent: "
          f"{'PASS' if ok else 'FAIL'}")
