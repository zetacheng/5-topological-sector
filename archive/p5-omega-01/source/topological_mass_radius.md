# Topological mass/radius gate — first-principles mass and stable radius
of the candidate U(3) topological structure with the full nonlocal omega kernel.

**Scope.** Compute `E_tot[F] = E_2 + E_4 + E_omega` for a unit-winding embedded
SU(2) hedgehog and decide: (1) does a finite-size stable solution exist; (2) its
radius `R_star`; (3) its rest mass `M_topo`; (4) does it lie inside the
continuum/derivative-expansion window; (5) how it depends on `f, G/N, Lambda,
M_omega`, regulator. "DM structure" is provisional — this gate only asks whether a
stable massive topological object exists, not whether it is cosmological dark
matter. No cosmology, formation, abundance, SPARC, or paper edits here.

Accepted, non-reopened inputs: Goldstone–Wilczek `J^mu=B^mu` (`c_GW=1`); pinned
quartic `kappa_U=-17/(1152 pi^2)` (NEGATIVE, m- and Lambda-independent);
dynamical omega from the omega-dynamization branch with healthy gates
`Z_omega>0, M_omega^2>0, g_omegaB!=0, D_00(0,q)>0`, and the FULL static kernel
`D_00(0,q)=g0/(1+g0 Pi_V(q))`, `Pi_V(q)=q^2 N_mult Pi_T(q^2)`, NOT only the
heavy-vector contact.

---

## 0. Conventions and unit synchronization (Phase 0 gate)

**Regulator/units.** Everything is computed in the SAME Euclidean sharp 4-ball
`|p|<Lambda` used by the C2a `kappa_U` extraction and the omega loop, with the
cutoff `Lambda` the single fundamental scale. All lengths are reported as the
dimensionless product `R Lambda`; all energies as `E/Lambda`. Set `Lambda=1` in
code; restore via `M_phys = (M/Lambda) Lambda_phys`. `Nc=3`, `Nf=2`,
`N_mult = Nc Tr_f[Q_V^2] = 6` (the omega-branch multiplicity).

**Two-derivative constant f (computed here, same scheme).** `f` is NOT set to 1.
It is the pion-kinetic coefficient from the SAME fermion loop / same 4-ball
cutoff as `kappa_U` (the "axial-current/two-point machinery" — `skyrme_sign2.py`
computes the companion `Z_pi` anchor in exactly these units). In closed form
(chiral quark loop, 4-ball):

    f^2(m,Lambda) = 4 Nc m^2 Int_{|p|<Lambda} d^4p/(2pi)^4  1/(p^2+m^2)^2
                  = (Nc m^2/4pi^2) [ ln((Lambda^2+m^2)/m^2) - Lambda^2/(Lambda^2+m^2) ].

This is positive, `~ m^2 ln(Lambda/m)`, and is cross-checked numerically against
the `twopt`/`Z_pi` machinery. Because `f^2`, `kappa_U`, `Z_omega`, and the omega
kernel all come from one loop with one cutoff, the inputs ARE synchronized (no
mixing of regulators). If that cross-check failed we would stop with
`INPUT NORMALIZATIONS NOT SYNCHRONIZED`; it does not.

**Locked inputs (per m/Lambda):** `f^2(m)`, `kappa_U=-17/(1152 pi^2)`,
`Z_omega=N_mult Pi_T(0)`, `M_omega^2=1/(g0 Z_omega)`, `g0=G/N` (free, scanned),
`g_omegaB=c_GW/sqrt(Z_omega)`, `c_GW=1`.

---

## 1. Hedgehog, baryon density, energy pieces

**Ansatz** (embedded SU(2), lower U(1) block trivial):
`U = diag( exp[i F(r) x^·tau], 1 )`, `F(0)=pi`, `F(inf)=0`, unit winding.

**Baryon density** (`B^0 = -(1/2pi^2)(sin^2F/r^2)F'`):

    B = 4pi Int_0^inf r^2 B^0 dr = -(2/pi) Int_0^inf sin^2F F' dr = 1  (exactly, F: pi->0).

For the profile family `F_2(r;R)=2 arctan(R/r)` this evaluates in closed form to

    B^0_R(r) = (4/pi^2) R^3/(r^2+R^2)^3 ,   Int d^3x B^0_R = 1,
    B~(q) = (1+qR) e^{-qR}   (3D Fourier transform; B~(0)=1),

which is exactly the normalized profile used in the omega-dynamization static
energy — a built-in consistency anchor.

**Two-derivative energy** `E_2 = (f^2/4) Int d^3x Tr(d_iU^dag d_iU)`. Hedgehog
`Tr(d_iU^dag d_iU) = 2(F'^2 + 2 sin^2F/r^2)`, so

    E_2 = 2pi f^2 Int_0^inf (r^2 F'^2 + 2 sin^2F) dr .   [scales as R: E_2 = 2pi f^2 i2(R), i2 ~ R]

**Quartic (Skyrme) energy.** The C2a quartic operator projects onto the
Skyrme (commutator) structure; on the hedgehog its coefficient multiplies the
standard integral

    E_4 = kappa_U * 2pi Int_0^inf sin^2F (2F'^2 + sin^2F/r^2) dr .  [scales as 1/R]

With `kappa_U<0`, `E_4<0` — the quartic is DESTABILIZING (drives collapse). The
absolute operator normalization carries an O(1) convention factor `kc` (the map
from the C2a box-code O1/O2 projection to `Tr([L_i,L_j]^2)`); we take the natural
`kc=1` (matching `omega_gates.ER_assembly`'s `|B|~|kappa_U|`), and verify every
conclusion is unchanged over `kc in [0.5,5]` (Phase 7 sensitivity). Because the
sign is fixed (`E_4<0`) the collapse is `kc`-robust.

**Omega energy (full nonlocal kernel).**

    E_omega = (g_omegaB^2/2) Int d^3q/(2pi)^3 |B~(q)|^2 D_00(0,q)
            = (c_GW^2/2)(1/2pi^2) Int_0^{qmax} q^2 (1+qR)^2 e^{-2qR} D_00(0,q) dq,
    D_00(0,q) = g0/(1 + g0 Pi_V(q)),  Pi_V(q)=q^2 N_mult Pi_T(q^2) >= 0.

`E_omega>0` for every profile (`D_00>0`). Crucially `D_00` is an EFT object valid
for `q<Lambda` only; the omega cannot mediate repulsion at distances below `1/Lambda`.

**Dimensions/scaling (Derrick).** Under `F(r)->F(r/L)`:
`E_2->L E_2`, `E_4->L^{-1} E_4`, and in the heavy/local omega limit
`E_omega->L^{-3} E_omega^loc`. So the naive scale energy is

    E(L) = A L - |B|/L + C/L^3 ,  A=2pi f^2 i2u>0, |B|=|kappa_U|2pi i4u>0,
    C = (g_omegaB^2/2M_omega^2) Int(B^0)^2 > 0   (heavy/local ONLY).

`E(L)` has a Derrick minimum at `L_*^2=(-|B|+sqrt(|B|^2+12AC))/(2A)>0` — **but only
if the omega really contributes `C/L^3`.** That requires `M_omega L_* >> 1` (soliton
much larger than the omega Compton wavelength). The full-kernel computation tests
whether that regime is actually reached.

---

## 2. Variational equations and two methods

**Method A (trial families):** minimize `E_tot(R)` for
`F_1=2 arctan(R^2/r^2)`, `F_2=2 arctan(R/r)`, `F_3=2 (arctan(R/r))^p`. Pilot +
regression anchor; report family spread.

**Method B (full variational):** discretize `F(r)` on a radial grid and minimize
the complete nonlocal functional (no one-parameter restriction) by (i) direct
finite-difference minimization / gradient relaxation of the Euler–Lagrange system,
cross-checked by (ii) an independent coordinate-space omega implementation. The
EL equation for the local pieces is

    d/dr[ 2 f^2 r^2 F' + 2 kappa_U (... quartic ...) ] = (source terms) + omega back-reaction,

with the omega contribution nonlocal (its variation feeds back through `B^0` and
`D_00`). Convergence of both implementations to the same `(R_star, M_topo)` within
the stated band is required.

---

## 3. Full nonlocal omega kernel (Phase 3)

Do NOT assume `E_omega ~ 1/R^3` except as a regression limit. Checks: (1)
`E_omega>0` per profile; (2) convergence in `qmax`/grid; (3) coordinate- vs
momentum-space agreement; (4) heavy-vector limit reproduces
`(g_omegaB^2/2M_omega^2)Int(B^0)^2`; (5) light/screened regime handled with the
full kernel. Report `M_omega R_star`. Classification: `>>1` local-6th valid;
`~1` full kernel essential; `<<1` long-range regime.

**Central kernel fact.** For `R Lambda <~ 1`, `B~(q)=(1+qR)e^{-qR} ~ 1` across the
whole EFT band `q<Lambda`, so `E_omega -> (1/4pi^2) Int_0^Lambda q^2 D_00 dq =
const`: the omega repulsion **saturates** at small R instead of growing as
`1/R^3`. It therefore cannot provide the divergent short-distance barrier the
`C/R^3` limit assumes.

---

## 4. Stability (Phase 4)

A candidate passes only if `dE/dF|_{F_*}=0` and `delta^2E[F_*]>0` for ALL tested
radial modes (not just the scale mode), excluding collective zero modes: at
minimum the scale/radius Hessian and the first several radial fluctuation
eigenvalues, plus profile-deformation sensitivity. Require
`lambda_min^fluct > 0`.

## 5. Continuum/cutoff validity (Phase 5)

Report `R_star Lambda, R_star/a, m_dyn R_star, M_omega R_star`.
- Continuum PASS: `R_star Lambda >= 10` and `q_core/Lambda <= 0.2`, stable under >=2
  regulators.
- Marginal: `3 <= R_star Lambda < 10`.
- Cutoff artifact: `R_star Lambda < 3` OR the minimum tracks the cutoff under
  regulator variation. Thresholds are pre-registered and not relaxed after the fact.

## 6. Mass (Phase 6)

`M_topo = E_tot[F_*] - E_vacuum` (vacuum = trivial `U=1`, `E=0`). Report
`M_2, M_4, M_omega` separately and `M_topo=M_2+M_4+M_omega`; require `M_topo>0`
(do not call it negative merely because `E_4<0`). Report `M_topo/Lambda,
M_topo/m_dyn, M_topo R_star`; if `Lambda_phys` is unfixed, give only the
dimensionless value and the scaling `M_phys=(M/Lambda)Lambda_phys`.

## 7. Parameter scan (Phase 7)

Scan `m_dyn/Lambda in {0.10,0.15,0.20,0.30}` and a range of `g0=G/N`. For each
report `R_star Lambda, M_topo/Lambda, M_omega R_star, lambda_min^fluct`. Separate
sign-robust / representative / parameter-dependent conclusions; determine whether
stable continuum solutions exist for all `g0>0`, only above a critical `g0`, in a
window, or not at all; report any `g0,crit`.

## 8. Regressions (Phase 8)

- **Omega off** (`g_omegaB=0`): negative-`kappa_U` must collapse (no finite-R
  minimum). Expected: `E_2+E_4=AR-|B|/R` decreases monotonically to `R->0`.
- **Quartic off** (`kappa_U=0`): expect positive `E_2` + omega; with the LOCAL
  omega, `E_2+C/R^3` has a Derrick minimum.
- **Local omega limit** (`D_00->1/M_omega^2`): reproduce `E(R)=AR-|B|/R+C/R^3`;
  compare its minimum to the full-kernel result — the discrepancy measures the
  invalidity of the local approximation when `M_omega R_star <~ 1`.
- **Sign-flip** (`D_00->-D_00`): must destabilize (code-sign anchor only).

---

## Pre-registered expectation (from the input-synchronized scales)

All energy scales (`f^2 ~ m^2 ln`, `kappa_U` pure number, `Z_omega ~ ln`, `M_omega`)
are set by the single cutoff `Lambda` — there is NO hierarchy, so the soliton size
is `R_star Lambda ~ O(1)`, not `>=10`. Concretely (m=0.20): the heavy/local limit
gives a Derrick minimum at `R_star Lambda ~ 1.6` with `M_omega R_star ~ 0.9 < 1`,
i.e. the local `C/R^3` approximation is already INVALID; the full nonlocal kernel,
whose repulsion saturates below `R Lambda ~ 1`, does not stabilize a continuum
soliton and the negative-`kappa_U` collapse proceeds to the cutoff. Both the
`R_star Lambda < 3` condition and the "minimum tracks the cutoff under regulator
variation" condition are met.

**Expected verdict:** `MASS/RADIUS GATE FAILS: MINIMUM IS A CUTOFF-SCALE LATTICE
LUMP` — a stable finite-radius CONTINUUM object is NOT established; any minimum
sits at the cutoff scale and its existence is regulator-sensitive. This is a
sign-robust negative result for the continuum dark-structure claim and supersedes
the earlier `E(R)=AR-|B|/R+C/R^3` heavy-vector assembly, which implicitly assumed
`M_omega R_star >> 1`.

The pre-registered verdict lines are those in the task; exactly one is printed by
the solver from the measured `(R_star Lambda, lambda_min, M_topo)`.
