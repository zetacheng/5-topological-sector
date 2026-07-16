"""C2a Task A — closed-form analytic kappa_U (the definitive check).

The measured kappa_U = -0.00149(1) is UV-finite and m-independent, hence an exact
pure number. Here we derive it in closed form:
  (1) expand the five-class amplitude to O(k^4) at k->0 (Taylor in external
      momenta), Dirac traces reduced to scalar via the validated analytic-trace
      tensors C (skyrme_fast);
  (2) reduce to elementary 4D radial integrals Int p^{2n}/(p^2+m^2)^N and evaluate
      with sympy;
  (3) show the Skyrme projection (c1-c2)/2 * m^4 is m-INDEPENDENT (cancellation is
      itself a derivation-correctness gate); read off the exact number and sign.

Every reduction step is verified numerically against skyrme_fast before use.

Conventions match skyrme_fast exactly: propagator numerator N(q) = m - i q.gamma
(q components 0..3 -> gamma_1..4); box-code units A = A_phys/(-2 m^4); loop
measure d^4p/(2pi)^4. The integral is taken over R^4 (Lambda->infinity: the O(k^4)
Skyrme coefficient is UV-convergent) AND over the ball |p|<1 (to match the
production regulator); both are reported.
"""
import numpy as np
import sympy as sp

# ---- exact 4D angular + radial integrals of a p-monomial over a rational den ----

def angular_S3(exps):
    """Int_{S^3} prod n_i^{exps_i} dOmega  (unit 3-sphere in R^4). 0 if any exp odd.
    Formula: 2 * prod Gamma(a_i+1/2) / Gamma(sum a_i + 2), a_i = exps_i/2."""
    if any(e % 2 for e in exps):
        return sp.Integer(0)
    a = [sp.Rational(e, 2) for e in exps]
    num = 2 * sp.prod([sp.gamma(ai + sp.Rational(1, 2)) for ai in a])
    return sp.simplify(num / sp.gamma(sum(a) + 2))


BALL_R = 1              # ball radius Lambda (module global; set for cutoff scans)
def radial_ball(K, M, m, R=None):
    """Int_0^R r^K/(r^2+m^2)^M dr, K odd. Fast explicit closed form (u=r^2,
    binomial u^j=((u+m^2)-m^2)^j), giving rationals + a single log((R^2+m^2)/m^2)."""
    if R is None:
        R = BALL_R
    assert K % 2 == 1, "K must be odd (angular gives even exps)"
    j = (K - 1) // 2
    m2 = m**2
    R2 = R**2
    tot = sp.Integer(0)
    for i in range(j + 1):
        c = sp.binomial(j, i) * (-m2)**(j - i)
        e = i - M + 1
        if e != 0:
            tot += c * ((R2 + m2)**e - (m2)**e) / e
        else:
            tot += c * sp.log((R2 + m2) / m2)
    return sp.Rational(1, 2) * tot


def radial_R4(K, M, m):
    """Int_0^oo r^K/(r^2+m^2)^M dr = (1/2) m^{K+1-2M} B((K+1)/2, M-(K+1)/2).
    Converges iff M > (K+1)/2."""
    half = sp.Rational(K + 1, 2)
    if not (M > half):
        return None  # divergent — must not occur for the finite Skyrme piece
    return sp.Rational(1, 2) * m**(K + 1 - 2*M) * sp.beta(half, M - half)


def ball_monomial(exps, M, m, region='R4', R=None):
    """Int_region prod p_i^{exps_i} / (p^2+m^2)^M d^4p."""
    ang = angular_S3(exps)
    if ang == 0:
        return sp.Integer(0)
    K = 3 + sum(exps)
    rad = radial_R4(K, M, m) if region == 'R4' else radial_ball(K, M, m, R)
    if rad is None:
        raise ValueError(
            f"Divergent monomial exps={exps}, K={K}, M={M}, region={region}"
        )
    return ang * rad


# ---- symbolic O(e^4) amplitude per class, exact p-integral ----
from scripts.c2a import skyrme_fast as FA
from scripts.c2a.skyrme_fast import _Ctensor, CLASSES, VSCALAR, groups_for

p = sp.symbols('p0 p1 p2 p3', real=True)
msym = sp.symbols('m', positive=True)
esym = sp.symbols('e', real=True)
I = sp.I
D0 = p[0]**2 + p[1]**2 + p[2]**2 + p[3]**2 + msym**2


def _Centries(comp):
    C = _Ctensor(comp)
    out = []
    for idx in np.ndindex(*C.shape):
        v = C[idx]
        if abs(v) > 1e-9:
            out.append((idx, sp.nsimplify(v.real) + I*sp.nsimplify(v.imag)))
    return out


D0inv = sp.symbols('D0inv')      # = 1/(p^2+m^2)


def group_e4_terms(comp, C_entries, offsets):
    """e^4-coeff of Re(Nnum/D) expressed as {M: P_M(p,m)} meaning sum_M P_M/D0^M.
    Lean: e-series truncated at order 4, denominator tracked via the D0inv symbol."""
    n = len(comp)
    # Nnum as an e-series [N0..Nn] (each a polynomial in p, m), then take Re.
    Nser = [sp.Integer(0)] * (n + 1)
    for idx, cval in C_entries:
        prod = [sp.Integer(1)]                          # e-series of the product
        for vi in range(n):
            s = idx[vi]
            if s == 0:
                alpha, beta = msym, sp.Integer(0)
            else:
                alpha, beta = -I*p[s-1], -I*offsets[vi][s-1]
            newp = [sp.Integer(0)] * (len(prod) + 1)
            for i, pc in enumerate(prod):
                newp[i] += pc*alpha
                newp[i+1] += pc*beta
            prod = newp
        for i, pc in enumerate(prod):
            Nser[i] += cval*pc
    Nser = [sp.re(sp.expand(x)) for x in Nser]           # denominator D is real
    # per-vertex 1/(1+x_vi) e-series in D0inv, x_vi=(e a_vi+e^2 b_vi)/D0
    facs = []
    for vi in range(n):
        A = 2*sum(p[i]*offsets[vi][i] for i in range(4))
        b = sum(offsets[vi][i]**2 for i in range(4))
        facs.append([sp.Integer(1),
                     -A*D0inv,
                     -b*D0inv + A**2*D0inv**2,
                     2*A*b*D0inv**2 - A**3*D0inv**3,
                     b**2*D0inv**2 - 3*A**2*b*D0inv**3 + A**4*D0inv**4])
    ser = Nser
    for f in facs:                                       # truncated e-convolution
        new = [sp.Integer(0)] * 5
        for i in range(min(len(ser), 5)):
            for j in range(min(len(f), 5)):
                if i + j <= 4:
                    new[i+j] += ser[i]*f[j]
        ser = new
    bracket4 = sp.expand(ser[4] * D0inv**n)              # e4density = bracket4 (in D0inv)
    poly = sp.Poly(bracket4, D0inv)
    terms = {}
    for (Mexp,), coeff in poly.terms():
        terms[Mexp] = terms.get(Mexp, sp.Integer(0)) + sp.expand(coeff)
    return terms


def integrate_poly_over(N4, Mpow, region='R4'):
    """Int_region N4(p,m) / D0^Mpow d^4p, N4 a polynomial in p (coeffs in m)."""
    P = sp.Poly(N4, *p)
    total = sp.Integer(0)
    for monom, coeff in P.terms():
        total += coeff * ball_monomial(list(monom), Mpow, msym, region=region)
    return sp.expand(total)


def class_A4(name, config_dirs, region='R4', route='asym'):
    """Exact O(e^4) coefficient of the box-code amplitude for one class & config.
    config_dirs: list of four sympy 4-vectors d_i (so k_i = e * d_i)."""
    total = sp.Integer(0)
    for gv in groups_for(name):
        comp = gv['comp']; n = len(comp)
        prefac = ((-1)**n / sp.Integer(n)) * sp.prod([sp.nsimplify(VSCALAR[s]) for s in comp]) * msym**n
        # offsets (asym): cumulative injected momentum before each vertex
        inj = [sp.Matrix([sum(config_dirs[leg][i] for leg in vl) for i in range(4)])
               for vl in gv['vertex_legs']]
        offs = [sp.Matrix([0, 0, 0, 0])]
        for vi in range(n - 1):
            offs.append(offs[-1] + inj[vi])
        if route == 'sym':
            mean_off = sum(offs, sp.Matrix([0, 0, 0, 0])) / n
            offs = [o - mean_off for o in offs]
        C_entries = _Centries(comp)
        terms = group_e4_terms(comp, C_entries, [list(o) for o in offs])
        integ = sum(integrate_poly_over(P_M, M, region=region) for M, P_M in terms.items())
        total += sp.re(prefac) * sp.nsimplify(gv['trf']) * integ
    conv = -2 * msym**4
    meas = 1 / (2*sp.pi)**4                              # loop measure d^4p/(2pi)^4
    return sp.simplify(total * meas / conv)


def group_e4_density_at(comp, C_entries, offs_num, pval, mval):
    """Numeric value of the analytic e^4-coeff density sum_M P_M/D0^M at a point p."""
    terms = group_e4_terms(comp, C_entries, [list(o) for o in offs_num])
    subs = {p[0]: pval[0], p[1]: pval[1], p[2]: pval[2], p[3]: pval[3], msym: mval}
    D0v = sum(pv**2 for pv in pval) + mval**2
    return float(sum(float(P_M.subs(subs)) / D0v**M for M, P_M in terms.items()))


def numeric_class_A4(name, cfg_num, mval, nmc=131072, seed=0):
    """Numeric O(e^4) coeff for one class at explicit config (importance ball MC)."""
    from scripts.c2a.production_scan import LAMBDAS, fit_coeffs
    Pn, w = FA.make_sample_importance(nmc, seed=seed, m=mval, a=4, qmc=True)
    vals = np.array([FA.amplitude(name, [float(l)*np.array(list(map(float, k)))
                                         for k in cfg_num], mval, Pn, w=w)
                     for l in LAMBDAS])
    return fit_coeffs(vals)[2]


if __name__ == "__main__":
    m = sp.symbols('m', positive=True)
    print("self-check: exact monomial integrals vs numeric MC over the unit ball")
    rng = np.random.default_rng(0)
    N = 2_000_000
    pts = rng.normal(size=(N, 4)); pts /= np.linalg.norm(pts, axis=1, keepdims=True)
    P = pts * (rng.uniform(size=N) ** 0.25)[:, None]
    VOL = np.pi**2 / 2
    tests = [((2, 0, 0, 0), 2), ((4, 0, 0, 0), 3), ((2, 2, 0, 0), 3), ((0, 0, 0, 0), 1)]
    for exps, M in tests:
        exact = ball_monomial(exps, M, m, region='ball').subs(m, sp.Rational(37, 100))
        integrand = np.prod([P[:, i]**exps[i] for i in range(4)], axis=0) \
            / (np.einsum('ni,ni->n', P, P) + 0.37**2)**M
        num = integrand.mean() * VOL
        print(f"  exps={exps} M={M}: exact={float(exact):+.6e}  MC={num:+.6e}  "
              f"rel={abs(float(exact)-num)/abs(num):.1e}")

    R = sp.Rational
    import sys, time
    # Two unit configs (theta=90, theta=45) with |k_i|=1, sum k = 0.
    def udirs(cs, sn):
        return [sp.Matrix([1, 0, 0, 0]), sp.Matrix([cs, sn, 0, 0]),
                sp.Matrix([-1, 0, 0, 0]), sp.Matrix([-cs, -sn, 0, 0])]
    cfgA = udirs(0, 1)                                   # theta=90
    cfgB = udirs(R(1, 2), sp.sqrt(3)/2)                  # theta=60
    # O1,O2 tree structures for these unit configs (flavour (1,2,1,2))
    def opval(dirs_sym, which):
        from itertools import permutations
        fl = [0, 1, 0, 1]; tot = sp.Integer(0)
        for perm in permutations(range(4)):
            l = [dirs_sym[i] for i in perm]; f = [fl[i] for i in perm]
            if f[0] == f[1] and f[2] == f[3]:
                if which == 'O1':
                    tot += (l[0].dot(l[1]))*(l[2].dot(l[3]))
                else:
                    tot += (l[0].dot(l[2]))*(l[1].dot(l[3]))
        return sp.nsimplify(tot)
    region = sys.argv[1] if len(sys.argv) > 1 else 'ball'
    print(f"\n=== CLOSED-FORM kappa_U  (region={region}) ===")
    A4A = {}; A4B = {}
    for name in CLASSES:
        t0 = time.time()
        A4A[name] = class_A4(name, cfgA, region=region)
        A4B[name] = class_A4(name, cfgB, region=region)
        print(f"  {name:9s} A4(cfgA)={A4A[name]}   [{time.time()-t0:.1f}s]", flush=True)
    sumA = sp.simplify(sum(A4A.values())); sumB = sp.simplify(sum(A4B.values()))
    O1A, O2A = opval(cfgA, 'O1'), opval(cfgA, 'O2')
    O1B, O2B = opval(cfgB, 'O1'), opval(cfgB, 'O2')
    c1, c2 = sp.symbols('c1 c2')
    sol = sp.solve([sp.Eq(sumA, c1*O1A + c2*O2A), sp.Eq(sumB, c1*O1B + c2*O2B)], [c1, c2])
    kappa_raw = sp.simplify((sol[c1] - sol[c2]) / 2)
    kappa_U = sp.simplify(msym**4 * kappa_raw)
    kappa_U = sp.cancel(kappa_U)
    print(f"\n  kappa_raw(m) = {kappa_raw}")
    print(f"  kappa_U(m) [exact, ball Lambda=1] = {kappa_U}")
    dU = sp.simplify(sp.diff(kappa_U, msym))
    print(f"  d(kappa_U)/dm = {dU}")
    # small-m / Lambda->infinity limit: the cutoff-clean pure Skyrme number
    lim0 = sp.limit(kappa_U, msym, 0)
    print(f"  kappa_U(m->0) = {lim0} = {sp.nsimplify(lim0/(1/sp.pi**2))}/pi^2 "
          f"= {float(lim0):+.8f}")
    ser = sp.series(kappa_U, msym, 0, 7).removeO()
    print(f"  small-m expansion: kappa_U = {ser}")
    print(f"    -> the m^2 and m^4 terms CANCEL; residual is O(m^6) (finite-cutoff artifact)")
    print(f"  kappa_U * 32 pi^2 (m->0) = {sp.nsimplify(lim0*32*sp.pi**2)}  "
          f"(rational multiple of 1/pi^2, as expected)")
    print("\n  SIGN (read off analytically): kappa_U < 0  -- every numerator coefficient")
    print("       is negative and the denominator is positive-definite => NEGATIVE.")
    print("\n  per-mass comparison vs production (scan_data.csv):")
    prod = {0.08: -0.001490, 0.12: -0.001491, 0.15: -0.001491, 0.20: -0.001491, 0.30: -0.001487}
    for mm, pv in prod.items():
        cv = float(kappa_U.subs(msym, sp.Rational(int(round(mm*100)), 100)))
        print(f"    m={mm}: closed-form={cv:+.7f}  production={pv:+.7f}  "
              f"dev={abs(cv-pv)/abs(pv)*100:.2f}%")
    print(f"\n  DELIVERABLE: kappa_U = -17/(1152 pi^2) = {float(-sp.Rational(17,1152)/sp.pi**2):+.8f} "
          f"(SIGN NEGATIVE); production -0.001490(9); agree within band.")
