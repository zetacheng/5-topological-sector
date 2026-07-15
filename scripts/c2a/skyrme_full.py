"""C2a — full five-class momentum-routed Monte-Carlo (vectorised).

Implements the unified full-symmetric evaluator of derivation/diagram_classes.md
sec.6 for ALL five diagram classes (BOX, TRIANGLE, BUBBLE, SUNSET, CONTACT), with
ONE routing prescription enforced across every class (P6-ready). Amplitudes are
returned in box-code units A_code = A_phys/(-2 m^4), matching the lineage box().

Target: NON-SINGLET SU(2) orientation/Skyrme coefficient, external legs a=(1,2,1,2).
Goldstone-ness => A0_total = 0 is EXACT (sec.6.3, pointwise). This measures NOT
the anomalous U(1)_A singlet (eta) sector.

Reproducibility: fixed seeds, printed configs; a second party reruns from the
committed code alone.
"""
import numpy as np
from itertools import permutations
from scripts.common.euclidean_gamma import g, g5

GM = [g[1], g[2], g[3], g[4]]
G5 = g5.astype(complex)
I4 = np.eye(4, dtype=complex)
tau = [np.array([[0, 1], [1, 0]], dtype=complex),
       np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]

VDIRAC = {1: G5, 2: I4, 3: G5, 4: I4}
VSCALAR = {1: 1j, 2: -0.5, 3: -1j / 6.0, 4: 1.0 / 24.0}
CLASSES = {
    'BOX':      [(1, 1, 1, 1)],
    'TRIANGLE': [(2, 1, 1), (1, 2, 1), (1, 1, 2)],
    'BUBBLE':   [(2, 2)],
    'SUNSET':   [(3, 1), (1, 3)],
    'CONTACT':  [(4,)],
}
VOL = np.pi**2 / 2
MEAS = VOL / (2 * np.pi) ** 4


def trf(flav_seq):
    M = np.eye(2, dtype=complex)
    for a in flav_seq:
        M = M @ tau[a - 1]
    return np.trace(M).real


def make_sample(nmc, seed):
    """Uniform sample in the unit 4-ball (same construction as the lineage)."""
    rng = np.random.default_rng(seed)
    pts = rng.normal(size=(nmc, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    return pts * (rng.uniform(size=nmc) ** 0.25)[:, None]


def Sb(P, kvec, m):
    """Vectorised propagator S(p+k) over sample P (N,4). Returns (N,4,4)."""
    q = P + kvec
    q2 = np.einsum('ni,ni->n', q, q)
    sl = (q[:, 0, None, None] * GM[0] + q[:, 1, None, None] * GM[1]
          + q[:, 2, None, None] * GM[2] + q[:, 3, None, None] * GM[3])
    return (-1j * sl + m * I4) / (q2 + m * m)[:, None, None]


def _terms(comps):
    """Pre-enumerate (comp, vertex_legs, flav_perm_order) for a class.

    Groups leg->slot assignments that share the SAME routing (vertex_legs as a
    tuple of frozensets is NOT enough — routing depends only on which legs sit on
    which vertex, i.e. the partition, but the Dirac chain is identical for all
    assignments of a comp with the same per-vertex leg SET). We therefore group by
    (comp index, per-vertex leg tuple sorted) and sum Tr_f over slot orderings.
    """
    out = []
    for ci, comp in enumerate(comps):
        n = len(comp)
        vslots = []
        for vi, s in enumerate(comp):
            vslots += [vi] * s
        groups = {}   # key: tuple(sorted legs per vertex) -> accumulated Tr_f
        for perm in permutations(range(4)):
            vertex_legs = [[] for _ in comp]
            flav_loop = []
            for slot, leg in enumerate(perm):
                vertex_legs[vslots[slot]].append(leg)
                flav_loop.append([1, 2, 1, 2][leg])
            key = (ci, tuple(tuple(sorted(vl)) for vl in vertex_legs))
            groups.setdefault(key, {'vertex_legs': [sorted(vl) for vl in vertex_legs],
                                    'comp': comp, 'trf': 0.0})
            groups[key]['trf'] += trf(flav_loop)
        for gk, gv in groups.items():
            if abs(gv['trf']) > 1e-12:
                out.append(gv)
    return out


def amplitude(name, cfg, m, P, return_density=False):
    """Amplitude of a class for external config cfg (4 momenta), flavours (1,2,1,2).

    cfg: list of four 4-vectors k_i (must sum to zero). Returns box-code units.
    If return_density, returns the per-point density array (for pointwise A0 checks).
    """
    conv = -2.0 * m**4
    N = P.shape[0]
    dens = np.zeros(N)
    for gv in _terms(CLASSES[name]):
        comp = gv['comp']; n = len(comp)
        prefac = ((-1.0) ** n / n) * np.prod([VSCALAR[s] for s in comp]) * (m ** n)
        # routing: injected momentum per vertex = sum of its legs' cfg momenta
        inj = [sum((cfg[leg] for leg in vl), np.zeros(4)) for vl in gv['vertex_legs']]
        # build Dirac chain S(q1) G1 S(q2) G2 ... ; q_i = p + sum_{j<i} inj_j
        acc = np.zeros(4)
        M = None
        for vi in range(n):
            Ti = np.einsum('nab,bc->nac', Sb(P, acc, m), VDIRAC[comp[vi]], optimize=True)
            M = Ti if M is None else np.einsum('nab,nbc->nac', M, Ti, optimize=True)
            acc = acc + inj[vi]
        trd = np.einsum('naa->n', M)
        dens += (prefac * gv['trf'] * trd).real
    dens = dens / conv
    if return_density:
        return dens
    return dens.mean() * MEAS


def a0_gate(m, seeds=(11, 23, 47), nmc=400_000, verbose=True):
    """P4 gate: per-class A0 at k=0 with MC error over seeds; A0_total must vanish.

    Because Sum_class density(p) = 0 POINTWISE (sec.6.3), A0_total is zero to
    machine precision sample-by-sample, not merely within 3 sigma.
    """
    zero = [np.zeros(4)] * 4
    per_class = {c: [] for c in CLASSES}
    totals = []
    pointwise_max = 0.0
    for seed in seeds:
        P = make_sample(nmc, seed)
        dens_sum = np.zeros(nmc)
        for c in CLASSES:
            d = amplitude(c, zero, m, P, return_density=True)
            per_class[c].append(d.mean() * MEAS)
            dens_sum += d
        totals.append(dens_sum.mean() * MEAS)
        pointwise_max = max(pointwise_max, np.max(np.abs(dens_sum)))
    if verbose:
        print(f"\n{'='*64}")
        print(f"P4 GATE — chiral-completeness A0 cancellation  [m={m}]")
        print(f"  NON-SINGLET (1,2,1,2); Goldstone => A0_total=0 EXACT. Not the eta sector.")
        print(f"  NMC={nmc}, seeds={seeds}")
        print(f"{'='*64}")
        print(f"  {'class':10s} {'A0 (box-code units, mean +- sd over seeds)':s}")
        for c in CLASSES:
            arr = np.array(per_class[c])
            print(f"  {c:10s} {arr.mean():+.6f} +- {arr.std():.6f}")
        tarr = np.array(totals)
        # MC error scale from the box class (representative single-class error)
        boxarr = np.array(per_class['BOX'])
        box_err = boxarr.std() if len(boxarr) > 1 else abs(boxarr[0])
        print(f"  {'-'*50}")
        print(f"  {'A0_TOTAL':10s} {tarr.mean():+.3e} +- {tarr.std():.3e}")
        print(f"  pointwise max|Sum_class density| = {pointwise_max:.3e}  "
              f"(exact cancellation => ~machine eps)")
        thr = 3 * box_err
        passed = abs(tarr.mean()) < max(thr, 1e-9)
        print(f"  3 x (single-class MC error) threshold = {thr:.3e}")
        print(f"  P4 VERDICT: {'PASS' if passed else 'FAIL'}  "
              f"(|A0_total| {'<' if passed else '>='} threshold)")
    return per_class, totals, pointwise_max


if __name__ == "__main__":
    import sys
    m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.30
    nmc = int(float(sys.argv[2])) if len(sys.argv) > 2 else 400_000
    a0_gate(m, nmc=nmc)
