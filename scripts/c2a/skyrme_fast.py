"""C2a — analytic-trace evaluator (fast, and an INDEPENDENT cross-check).

Same physics as skyrme_full.py (unified full-symmetric five-class evaluator,
one routing prescription), but the Dirac trace of each propagator chain is
reduced to a precomputed CONSTANT tensor contracted with momentum vectors,
instead of N-vectorised 4x4 matrix chains. This is ~100x faster and, being a
structurally DIFFERENT evaluator, serves as the second-evaluator cross-check
required at every checkpoint.

Trace reduction.  A propagator numerator is N(q) = m*1 - i*(q.gamma).  For a
chain Tr[N(q1)G1 N(q2)G2 ... N(qn)Gn], write each factor as
    N(q).G = m*(G) + sum_mu (-i q_mu)*(gamma_mu . G)
so, with a 5-valued index s per vertex (s=0 -> the 'm' term B0=G ; s=mu ->
B_mu = gamma_mu . G, weight -i q_mu),
    Tr[...] = sum_{s1..sn} C[s1..sn] * prod_i W_i(s_i),
    C[s1..sn] = Tr[ B_{s1}^{(1)} B_{s2}^{(2)} ... B_{sn}^{(n)} ]   (constant),
    W_i = ( m, -i q_i1, -i q_i2, -i q_i3, -i q_i4 ).
C is precomputed once per composition; the per-point work is one tensor
contraction over the N-sample.  q components 0..3 map to gamma_1..gamma_4,
matching skyrme_full's Sb.
"""
import numpy as np
from itertools import permutations
from scripts.common.euclidean_gamma import g, g5

GM = [g[1], g[2], g[3], g[4]]        # gamma_1..gamma_4
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


def _Ctensor(comp):
    """Precompute C[s1..sn] = Tr[ B_{s1}^{(1)} ... B_{sn}^{(n)} ] for a comp."""
    n = len(comp)
    Bs = []
    for s in comp:
        G = VDIRAC[s]
        Bs.append([G] + [GM[mu] @ G for mu in range(4)])   # index 0..4
    C = np.zeros((5,) * n, dtype=complex)
    for idx in np.ndindex(*([5] * n)):
        M = I4
        for i in range(n):
            M = M @ Bs[i][idx[i]]
        C[idx] = np.trace(M)
    return C


def _groups(comps):
    """(comp, Ctensor, vertex_legs, Tr_f) grouped by routing (per-vertex leg set)."""
    out = []
    for comp in comps:
        C = _Ctensor(comp)
        vslots = []
        for vi, s in enumerate(comp):
            vslots += [vi] * s
        groups = {}
        for perm in permutations(range(4)):
            vertex_legs = [[] for _ in comp]
            flav_loop = []
            for slot, leg in enumerate(perm):
                vertex_legs[vslots[slot]].append(leg)
                flav_loop.append([1, 2, 1, 2][leg])
            key = tuple(tuple(sorted(vl)) for vl in vertex_legs)
            g_ = groups.setdefault(key, {'vertex_legs': [sorted(vl) for vl in vertex_legs],
                                         'comp': comp, 'C': C, 'trf': 0.0})
            g_['trf'] += trf(flav_loop)
        for gv in groups.values():
            if abs(gv['trf']) > 1e-12:
                out.append(gv)
    return out


_GCACHE = {}
def groups_for(name):
    if name not in _GCACHE:
        _GCACHE[name] = _groups(CLASSES[name])
    return _GCACHE[name]


def make_sample(nmc, seed):
    rng = np.random.default_rng(seed)
    pts = rng.normal(size=(nmc, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    return pts * (rng.uniform(size=nmc) ** 0.25)[:, None]


def make_sample_importance(nmc, seed=0, m=0.15, a=4, qmc=True):
    """Importance sample in the unit 4-ball with radial pdf rho(r) ~ r^3/(r^2+m^2)^a.

    The five-class integrand is sharply peaked at |p|~m (up to 1/(p^2+m^2)^4 for the
    box); uniform-ball MC then has variance ~1/m^12 and is useless for small m.
    Sampling r from rho with a=4 makes the box integrand*weight ~ const, taming the
    variance. Direction uniform on S^3. Returns (P, w) where the estimator is
    amplitude = mean(density * w). qmc=True uses a Sobol (low-discrepancy) draw.
    """
    from scipy.stats import norm
    rgrid = np.linspace(0.0, 1.0, 40001)
    pdfu = rgrid**3 / (rgrid**2 + m*m)**a
    seg = (pdfu[1:] + pdfu[:-1]) / 2 * np.diff(rgrid)
    Z = seg.sum()
    cdf = np.concatenate([[0.0], np.cumsum(seg)]) / Z
    if qmc:
        from scipy.stats import qmc as _qmc
        mm = int(np.ceil(np.log2(max(nmc, 2))))
        u = _qmc.Sobol(d=5, scramble=True, seed=seed).random_base2(mm)[:nmc]
        gdir = norm.ppf(np.clip(u[:, :4], 1e-12, 1 - 1e-12))
        ur = u[:, 4]
    else:
        rng = np.random.default_rng(seed)
        gdir = rng.normal(size=(nmc, 4)); ur = rng.uniform(size=nmc)
    gdir /= np.linalg.norm(gdir, axis=1, keepdims=True)
    r = np.interp(ur, cdf, rgrid)
    P = gdir * r[:, None]
    w = 2 * np.pi**2 * (r**2 + m*m)**a * Z / (2 * np.pi)**4   # per-point weight
    return P, w


def make_sample_qmc(nmc, seed=0):
    """Deterministic quasi-MC uniform sample in the unit 4-ball (Sobol).

    A structurally DIFFERENT integrator from pseudo-random MC (low-discrepancy,
    no statistical noise) -- used for the P6/P7 cross-checks. Direction from a
    4D Gaussian via the normal inverse-CDF, radius via u^{1/4}; all 5 coordinates
    drawn from one Sobol sequence so the whole ball is covered quasi-uniformly.
    """
    from scipy.stats import qmc, norm
    m = int(np.ceil(np.log2(max(nmc, 2))))
    u = qmc.Sobol(d=5, scramble=True, seed=seed).random_base2(m)[:nmc]
    g = norm.ppf(np.clip(u[:, :4], 1e-12, 1 - 1e-12))
    g /= np.linalg.norm(g, axis=1, keepdims=True)
    r = u[:, 4] ** 0.25
    return g * r[:, None]


def _Wmat(q, m):
    """W = (m, -i q1, -i q2, -i q3, -i q4) as (N,5) complex."""
    N = q.shape[0]
    W = np.empty((N, 5), dtype=complex)
    W[:, 0] = m
    W[:, 1:5] = -1j * q
    return W


def amplitude(name, cfg, m, P, return_density=False, route='asym', w=None):
    """Box-code-unit amplitude of a class for external cfg (4 momenta summing to 0).

    route='asym' (default): q_i = p + sum_{j<i} inj_j  (lineage prescription).
    route='sym'          : centered routing q_i = p + offset_i - mean_i(offset_i),
                           a shift-symmetric second prescription for the P6 gate.
    The SAME route is used for every class (single prescription across classes).
    w: per-point importance weights (from make_sample_importance); None => uniform
       ball, estimator dens.mean()*MEAS.
    """
    conv = -2.0 * m**4
    N = P.shape[0]
    dens = np.zeros(N)
    for gv in groups_for(name):
        comp = gv['comp']; n = len(comp)
        prefac = ((-1.0) ** n / n) * np.prod([VSCALAR[s] for s in comp]) * (m ** n)
        inj = [sum((cfg[leg] for leg in vl), np.zeros(4)) for vl in gv['vertex_legs']]
        offsets = [np.zeros(4)]
        for vi in range(n - 1):
            offsets.append(offsets[-1] + inj[vi])
        if route == 'sym':
            mean_off = sum(offsets) / n
            offsets = [o - mean_off for o in offsets]
        elif route != 'asym':
            raise ValueError(route)
        Ws = []
        denom = np.ones(N)
        for vi in range(n):
            q = P + offsets[vi]
            Ws.append(_Wmat(q, m))
            denom = denom * (np.einsum('ni,ni->n', q, q) + m * m)
        # contract C[s1..sn] with W_i over the sample
        R = np.tensordot(Ws[0], gv['C'], axes=([1], [0]))      # (N, 5,..[n-1])
        for vi in range(1, n):
            R = np.einsum('na,na...->n...', Ws[vi], R, optimize=True)
        trace = R                                              # (N,) complex
        dens += (prefac * gv['trf'] * trace / denom).real
    dens = dens / conv
    if return_density:
        return dens
    return (dens * w).mean() if w is not None else dens.mean() * MEAS


def full_amplitude(cfg, m, P, return_density=False, route='asym', w=None):
    """Sum over all five classes (box-code units)."""
    N = P.shape[0]
    if return_density:
        d = np.zeros(N)
        for c in CLASSES:
            d += amplitude(c, cfg, m, P, return_density=True, route=route)
        return d
    return sum(amplitude(c, cfg, m, P, route=route, w=w) for c in CLASSES)


def _comp_table():
    """Group all classes' groups by composition; batch groups sharing a C tensor.

    Returns list of (comp, C, prefac, groups) where groups is a list of
    (vertex_legs, trf). Cached.
    """
    if _comp_table._c is None:
        table = {}
        for name in CLASSES:
            for gv in groups_for(name):
                comp = gv['comp']
                key = comp
                if key not in table:
                    prefac = ((-1.0) ** len(comp) / len(comp)) \
                        * np.prod([VSCALAR[s] for s in comp]) * 1.0   # m^n applied later
                    table[key] = {'comp': comp, 'C': gv['C'], 'prefac0': prefac,
                                  'groups': []}
                table[key]['groups'].append((gv['vertex_legs'], gv['trf']))
        _comp_table._c = list(table.values())
    return _comp_table._c
_comp_table._c = None


def full_amplitude_batch(cfgs, m, P, max_elems=8_000_000):
    """Sum-over-five-classes amplitude for a BATCH of B external configs.

    Batches BOTH over the B configs AND over the groups sharing each composition's
    trace tensor C, so the whole five-class evaluation is a handful of large
    contractions. N-chunk size is chosen per composition to bound the intermediate
    (M*chunk*5^(n-1) <= max_elems). Identical result to looping full_amplitude
    (validated to 1e-15). Returns array (B,) in box-code units.
    """
    conv = -2.0 * m**4
    B = len(cfgs)
    N = P.shape[0]
    out = np.zeros(B)
    cfg_arr = np.array([[np.asarray(k, float) for k in cfg] for cfg in cfgs])  # (B,4,4)
    for entry in _comp_table():
        comp = entry['comp']; n = len(comp)
        C = entry['C']
        prefac = entry['prefac0'] * (m ** n)
        groups = entry['groups']; G = len(groups)
        chunk = max(500, int(max_elems / (B * G * max(1, 5 ** (n - 1)))))
        # injected momentum per (config b, group j, vertex vi): (B,G,n,4)
        inj = np.zeros((B, G, n, 4))
        for j, (vlegs, tf) in enumerate(groups):
            for vi, vl in enumerate(vlegs):
                if vl:
                    inj[:, j, vi, :] = cfg_arr[:, vl, :].sum(axis=1)
        trfvec = np.array([tf for (_, tf) in groups])          # (G,)
        M = B * G
        injflat = inj.reshape(M, n, 4)
        wgt = (prefac * np.tile(trfvec, B)).astype(complex)      # (M,) index b*G+j
        accM = np.zeros(M)
        for s in range(0, N, chunk):
            Pc = P[s:s + chunk]; nc = Pc.shape[0]
            denom = np.ones((M, nc))
            accm = np.zeros((M, 4))
            Ws = []
            for vi in range(n):
                q = Pc[None, :, :] + accm[:, None, :]            # (M,nc,4)
                W = np.empty((M, nc, 5), dtype=complex)
                W[..., 0] = m
                W[..., 1:5] = -1j * q
                Ws.append(W)
                denom = denom * (np.einsum('mni,mni->mn', q, q) + m * m)
                accm = accm + injflat[:, vi, :]
            R = np.tensordot(Ws[0], C, axes=([2], [0]))          # (M,nc,5^(n-1))
            for vi in range(1, n):
                R = np.einsum('mna,mna...->mn...', Ws[vi], R, optimize=True)
            contrib = (wgt[:, None] * R / denom).real            # (M,nc)
            accM += contrib.sum(axis=1)
        out += accM.reshape(B, G).sum(axis=1)
    return out / conv / N * MEAS

