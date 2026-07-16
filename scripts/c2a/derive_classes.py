"""C2a — machine derivation of flavour weights + symmetry factors for ALL five
diagram classes, non-singlet (1,2,1,2) external assignment.

This script DERIVES (not fits) the per-class combinatorics from the Tr-ln
expansion and verifies:
  1. the BOX necklace flavour anchor (-2,+2,+2) [lineage cross-check];
  2. that a single UNIFIED evaluator reproduces the validated box() amplitude
     of skyrme_sign2 / startup_regression EXACTLY (normalization anchor);
  3. the per-class zero-momentum A0 coefficients and the P4 integrand-level
     cancellation Sum_class A0_class(p) = 0 pointwise in p (Rider #4a).

Framework (derivation/diagram_classes.md sec.1):
  W = -Tr ln(1 + S dM),  dM = m[ i g5 th - th^2/2 - i g5 th^3/6 + th^4/24 + ...],
  th = tau.pi (f=1 units).  The n-th term is (-1)^n/n Tr[(S dM)^n].
  4-pion part: partitions of 4 into n vertices (each vertex size = # legs):
    BOX (1,1,1,1) n=4 ; TRIANGLE (2,1,1) n=3 ; BUBBLE (2,2) n=2 ;
    SUNSET (3,1) n=2 ; CONTACT (4) n=1.

Vertex data:  size -> (Dirac matrix, scalar constant m*d_j)
    1 : (g5 , i*m )        # V1 = i m g5 th
    2 : (1  , -m/2 )       # V2 = -(m/2) th^2
    3 : (g5 , -i*m/6 )     # V3 = -(i m/6) g5 th^3
    4 : (1  , m/24 )       # V4 = (m/24) th^4
A vertex of size s carries s external legs; its Dirac factor is g5 (odd size)
or 1 (even size) because (tau.pi) ~ 1_Dirac, and g5 th^odd keeps one g5.

Physical amplitude for external legs {(k_i, a_i)} (distinct, ordered):
  A_phys = sum over ordered compositions of the class,
             (-1)^n/n * prod_v scalar(v) *
             sum over leg->slot assignments Re{ Tr_D[S G S G ...] * Tr_f[tau...] }
The loop-order tau string = legs in (vertex order, slot order); the same order
routes momenta (each vertex injects the sum of its legs' momenta).

Box-code (lineage) units:  A_code = A_phys / (-2 m^4).  This common factor is
irrelevant to the A0=0 test; it is fixed so the BOX reproduces skyrme_sign2's
box() (see verification 2). Derivation committed BEFORE the class MC is coded.
"""
import numpy as np
from itertools import permutations
from scripts.common.euclidean_gamma import g, g5

GM = [g[1], g[2], g[3], g[4]]
G5 = g5.astype(complex)
I4 = np.eye(4, dtype=complex)
# SU(2) flavour (Pauli), tau^1,tau^2,tau^3
tau = [np.array([[0, 1], [1, 0]], dtype=complex),
       np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]


def trf(flav_seq):
    """Flavour trace Tr_f[tau^{a1} tau^{a2} ...], flavours are 1-based -> index-1."""
    M = np.eye(2, dtype=complex)
    for a in flav_seq:
        M = M @ tau[a - 1]
    return np.trace(M).real


# ---- vertex table (Dirac matrix, scalar constant) keyed by vertex size ----
VDIRAC = {1: G5, 2: I4, 3: G5, 4: I4}
VSCALAR = {1: 1j, 2: -0.5, 3: -1j / 6.0, 4: 1.0 / 24.0}   # d_j (the m is separate)


CLASSES = {
    'BOX':      [(1, 1, 1, 1)],
    'TRIANGLE': [(2, 1, 1), (1, 2, 1), (1, 1, 2)],
    'BUBBLE':   [(2, 2)],
    'SUNSET':   [(3, 1), (1, 3)],
    'CONTACT':  [(4,)],
}


def Sprop(qvec, m):
    """Euclidean propagator S(q) = (-i q_slash + m)/(q^2+m^2) as 4x4 (single q)."""
    ql = qvec[0] * GM[0] + qvec[1] * GM[1] + qvec[2] * GM[2] + qvec[3] * GM[3]
    q2 = float(qvec @ qvec)
    return (-1j * ql + m * I4) / (q2 + m * m)


def amp_phys_single_p(comps, klegs, alegs, m, p):
    """Physical amplitude density at ONE loop momentum p (4-vector), general k.

    klegs: list of 4 external momentum 4-vectors; alegs: list of 4 flavours.
    Returns Re part (a real scalar), summed over ordered comps and assignments.
    """
    total = 0.0
    for comp in comps:
        n = len(comp)
        prefac = ((-1.0) ** n / n) * np.prod([VSCALAR[s] for s in comp]) * (m ** n)
        # slot list: (vertex_index, dirac_matrix) flattened in vertex/slot order
        vslots = []          # slot -> vertex index
        for vi, s in enumerate(comp):
            vslots += [vi] * s
        for perm in permutations(range(4)):     # leg -> slot assignment
            # legs in slot order:
            slot_leg = list(perm)
            # per-vertex injected momentum (sum of that vertex's legs)
            inj = [np.zeros(4) for _ in comp]
            flav_loop = []
            # walk slots in order; group by vertex
            vertex_legs = [[] for _ in comp]
            for slot, leg in enumerate(slot_leg):
                vertex_legs[vslots[slot]].append(leg)
            for vi in range(n):
                for leg in vertex_legs[vi]:
                    inj[vi] = inj[vi] + klegs[leg]
                    flav_loop.append(alegs[leg])
            # Dirac trace Tr[ S(q1) G1 S(q2) G2 ... ]; q_i = p + sum_{j<i} inj[j]
            M = I4.copy()
            acc = np.zeros(4)
            for vi in range(n):
                q = p + acc
                M = M @ Sprop(q, m) @ VDIRAC[comp[vi]]
                acc = acc + inj[vi]
            trd = np.trace(M)
            total += (prefac * trd * trf(flav_loop)).real
    return total


def flavour_symmetry_report():
    """Print S_flavour = sum over comps & assignments of Tr_f, and the box anchor."""
    print("=" * 70)
    print("FLAVOUR-WEIGHT + SYMMETRY DERIVATION  (external legs a=(1,2,1,2))")
    print("=" * 70)
    a = [1, 2, 1, 2]
    # BOX necklace anchor: 3 reflection-rep necklaces fixing leg0
    print("\n[1] BOX necklace flavour anchor (fix leg0; 3 reflection reps):")
    reps = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
    for r in reps:
        w = trf([a[i] for i in r])
        print(f"    necklace {r} -> Tr_f = {w:+.1f}")
    print("    lineage anchor (-2,+2,+2):",
          [trf([a[i] for i in r]) for r in reps] == [-2, 2, 2])

    print("\n[2] S_flavour (sum over ordered comps x 24 assignments of Tr_f):")
    for name, comps in CLASSES.items():
        Sf = 0.0
        for comp in comps:
            vslots = []
            for vi, s in enumerate(comp):
                vslots += [vi] * s
            for perm in permutations(range(4)):
                flav_loop = [a[perm[slot]] for slot in range(4)]
                Sf += trf(flav_loop)
        print(f"    {name:9s} comps={comps}  S_flavour = {Sf:+.3f}")


def a0_table(m, nmc=400_000, seed=11):
    """Semi-analytic A0 per class in box-code units, plus integrand-level cancellation.

    Uses the SAME unit ball MC sample as the lineage (radius 1, VOL=pi^2/2).
    A0 is evaluated at k=0 (all external momenta zero).
    """
    rng = np.random.default_rng(seed)
    VOL = np.pi**2 / 2
    pts = rng.normal(size=(nmc, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    P = pts * (rng.uniform(size=nmc) ** 0.25)[:, None]
    zero = [np.zeros(4)] * 4
    a = [1, 2, 1, 2]
    meas = VOL / (2 * np.pi) ** 4
    print("\n" + "=" * 70)
    print(f"[3] PER-CLASS A0 (k=0) in box-code units  [m={m}, NMC={nmc}, seed={seed}]")
    print("    (box-code unit = A_phys / (-2 m^4); common factor, irrelevant to A0=0)")
    print("=" * 70)
    # Evaluate class A0 density per sampled p, average -> integral estimate.
    conv = -2.0 * m**4
    per_class = {}
    dens_sum = np.zeros(min(nmc, 4000))   # store first points for integrand check
    NP = dens_sum.shape[0]
    a0_tot = 0.0
    for name, comps in CLASSES.items():
        s = 0.0
        dv = np.zeros(NP)
        for idx in range(nmc):
            val = amp_phys_single_p(comps, zero, a, m, P[idx]) / conv
            s += val
            if idx < NP:
                dv[idx] = val
        a0 = s / nmc * meas
        per_class[name] = a0
        dens_sum[:] += dv
        a0_tot += a0
        print(f"    A0[{name:9s}] = {a0:+.6f}")
    print(f"    {'-'*40}")
    print(f"    A0[TOTAL]     = {a0_tot:+.6f}")
    # integrand-level (Rider #4a): mean |sum density| vs mean |box density|
    box_dens = np.zeros(NP)
    for idx in range(NP):
        box_dens[idx] = amp_phys_single_p(CLASSES['BOX'], zero, a, m, P[idx]) / conv
    rel = np.mean(np.abs(dens_sum)) / (np.mean(np.abs(box_dens)) + 1e-30)
    print(f"    integrand-level |sum|/|box| (first {NP} pts) = {rel:.3e} "
          f"(Rider #4a: ~0 if weights exact)")
    return per_class, a0_tot


def _box_lineage_point(cfg, m, p):
    """Lineage box() contribution at ONE p (replicates skyrme_sign2.box exactly)."""
    orders = [((0, 1, 2, 3), -2.0), ((0, 1, 3, 2), 2.0), ((0, 2, 1, 3), 2.0)]
    tot = 0.0
    for od, fl in orders:
        k1, k2, k3, k4 = [cfg[i] for i in od]
        S1 = Sprop(p, m); S2 = Sprop(p + k1, m)
        S3 = Sprop(p + k1 + k2, m); S4 = Sprop(p + k1 + k2 + k3, m)
        M = G5 @ S2 @ G5 @ S3 @ G5 @ S4 @ G5 @ S1
        tot += fl * (-1.0) * np.trace(M).real
    return tot


def verify_box_reproduction(m=0.30, nsmp=20000, seed=999):
    """Normalization anchor: the unified full-symmetric BOX must reproduce the
    lineage box() INTEGRAL within MC error.

    The unified evaluator is the Bose-symmetric 1PI vertex (all 24 leg->slot
    assignments, factor 1/n). The lineage box() uses 3 reflection-rep necklaces
    with an overall (-1). At k=0 they agree pointwise (reflection exact); at
    k!=0 they differ pointwise by a piece ANTISYMMETRIC under the symmetric ball
    measure, so they agree as integrals. We therefore compare integrals, not
    pointwise values, and report the difference with its MC error.
    """
    rng = np.random.default_rng(seed)
    pts = rng.normal(size=(nsmp, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    P = pts * (rng.uniform(size=nsmp) ** 0.25)[:, None]
    e = 0.10
    cfg = [np.array([e, 0, 0, 0]), np.array([0, e, 0, 0]),
           np.array([-e, 0, 0, 0]), np.array([0, -e, 0, 0])]
    a = [1, 2, 1, 2]
    conv = -2.0 * m**4
    VOL = np.pi**2 / 2; meas = VOL / (2 * np.pi) ** 4
    us = np.empty(nsmp); ls = np.empty(nsmp)
    for idx in range(nsmp):
        us[idx] = amp_phys_single_p(CLASSES['BOX'], cfg, a, m, P[idx]) / conv
        ls[idx] = _box_lineage_point(cfg, m, P[idx])
    ui = us.mean() * meas; li = ls.mean() * meas
    di = (us - ls).mean() * meas; de = (us - ls).std() / np.sqrt(nsmp) * meas
    print("\n" + "=" * 70)
    print("[0] NORMALIZATION ANCHOR: unified full-symmetric BOX vs lineage box()")
    print("=" * 70)
    print(f"    unified BOX integral ({nsmp} pts) = {ui:+.6f}")
    print(f"    lineage box() integral            = {li:+.6f}")
    ok = abs(di) < 3 * de
    print(f"    (unified - lineage) integral = {di:+.3e} +- {de:.3e}  "
          f"-> consistent with 0: {ok}")
    return ok


def analytic_density(name, x, m):
    """Closed-form k=0 physical A0 density g(p) (x=p^2), from the DERIVED weights.
    S_flavour = {BOX:16, TRI:48, BUB:16, SUN:32, CON:16}."""
    D = x + m * m
    if name == 'BOX':
        return 16.0 * m**4 / D**2
    if name == 'TRIANGLE':
        return -32.0 * m**4 / D**2
    if name == 'BUBBLE':
        return 8.0 * m**2 * (m * m - x) / D**2
    if name == 'SUNSET':
        return (32.0 / 3.0) * m**2 / D
    if name == 'CONTACT':
        return -(8.0 / 3.0) * m**2 / D
    raise KeyError(name)


def verify_analytic_vs_numeric(m=0.30, npts=200, seed=7):
    """Per-point: unified matrix evaluator (physical) vs closed-form density."""
    rng = np.random.default_rng(seed)
    pts = rng.normal(size=(npts, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    P = pts * (rng.uniform(size=npts) ** 0.25)[:, None]
    a = [1, 2, 1, 2]; zero = [np.zeros(4)] * 4
    print("\n" + "=" * 70)
    print("[4] ANALYTIC vs NUMERIC k=0 density, and POINTWISE cancellation (Rider #4a)")
    print("=" * 70)
    maxerr = {}; sum_dens = np.zeros(npts)
    for name in CLASSES:
        e = 0.0
        for i in range(npts):
            x = float(P[i] @ P[i])
            num = amp_phys_single_p(CLASSES[name], zero, a, m, P[i])  # physical
            ana = analytic_density(name, x, m)
            e = max(e, abs(num - ana))
            sum_dens[i] += num
        maxerr[name] = e
        print(f"    {name:9s}: max|numeric-analytic| = {e:.2e}")
    print(f"    {'-'*50}")
    print(f"    POINTWISE Sum_class density: max|.| = {np.max(np.abs(sum_dens)):.2e}"
          f"   (Rider #4a: 0 => weights exact, regulator-independent)")
    return max(maxerr.values()) < 1e-10, np.max(np.abs(sum_dens))


if __name__ == "__main__":
    flavour_symmetry_report()
    ok_box = verify_box_reproduction(0.30)
    ok_ana, pw = verify_analytic_vs_numeric(0.30)
    per_class, a0_tot = a0_table(0.30, nmc=4000, seed=11)
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  box-reproduction anchor (unified==lineage) : {'PASS' if ok_box else 'FAIL'}")
    print(f"  analytic==numeric density                  : {'PASS' if ok_ana else 'FAIL'}")
    print(f"  Rider #4a pointwise cancellation max|.|    : {pw:.2e}  "
          f"{'PASS' if pw < 1e-10 else 'FAIL'}")
