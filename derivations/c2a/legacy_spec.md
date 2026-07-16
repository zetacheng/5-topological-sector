# C2a — Resume specification (provenance record)

> This file is the verbatim resume prompt + pre-registered specification for the
> C2a computation (pinning `kappa_U`, the dark-energy chain's foundation).
> Committed so provenance lives with the code. Do not edit the specification
> sections retroactively; append notes in `derivation/diagram_classes.md` and the
> results CSVs instead.

---

## Claude Code Resume Prompt — C2a continuation

You are resuming an in-progress computation in the repository
zetacheng/kappa-c2a (public). Work on branch `c2a`. Do NOT recreate
anything that already exists there.

### State of the branch (all independently verified by a second party)
- Lineage files: skyrme_sign2.py, fierz_verify.py (algebra verified).
- startup_regression.py: constant-included fit reproduces the pilot
  P3 numbers exactly (verified on two machines).
- derivation/diagram_classes.md: framework locked -- vertex identities
  ((tau.pi)^2 = pi^2 * identity, etc.), BOX flavour anchor (-2,+2,+2)
  from the SU(2) trace, all five zero-momentum Dirac reductions
  (machine-checked), CONTACT prefactor A0_contact =
  -(4 m^2/3) Int d4p/(2pi)^4 1/(p^2+m^2) (independently re-derived and
  confirmed), and the per-class skeleton table:
    BOX      (V1,V1,V1,V1): 4 props, g5.S.g5.S.g5.S.g5.S
    TRIANGLE (V1,V1,V2):    3 props, g5.S.g5.S.1.S
    BUBBLE   (V2,V2):       2 props, 1.S.1.S
    SUNSET   (V1,V3):       2 props, g5.S.g5.S
    CONTACT  (V4):          1 prop (closed tadpole), k-independent.

### Your first actions (in order)
1. Clone/attach the repo, check out `c2a`, run startup_regression.py
   and confirm STARTUP REGRESSION: PASS before anything else.
2. Commit THIS ENTIRE PROMPT (the specification below included) into
   the repo as docs/C2a_spec.md, so provenance lives with the code.
3. Resume at the exact point the previous session stopped:
   (a) finish the flavour weights + symmetry factors for
       TRIANGLE / BUBBLE / SUNSET for the non-singlet (1,2,1,2)
       external assignment, appending to derivation/diagram_classes.md
       and committing the derivation BEFORE coding the MC;
   (b) semi-analytic A0 pre-check;
   (c) full momentum-routed MC per class;
   (d) the P4 gate, checkpointing there BEFORE the production scan.

### Rider #4 (sharpens P4/P6 -- apply it)
At k=0 there are no external momenta, hence NO routing ambiguity --
all propagators carry the same loop momentum. Consequences:
(a) attempt the A0 cancellation at the INTEGRAND level (pointwise in
p, before integration): with correct weights the sum of the five
classes' zero-momentum integrands should vanish identically, which is
regulator-independent and stronger than the integrated 3-sigma test;
(b) if A0 fails at k=0 it is combinatorics/weights, NOT a routing
artifact -- P6's routing test applies to the k!=0 fit points only.

### Standing discipline
Checkpoint at P4 with the per-class A0 table printed regardless of
pass/fail; if any gate fails, stop and report -- never emit kappa_U
numbers past a failed gate. A second party clones the public repo and
independently reruns your scripts at every checkpoint: every claimed
number must be reproducible from the committed code alone (fixed
seeds, printed configs).

---

# C2a Specification — Pinning kappa_U (the dark-energy chain's foundation)

Pre-registered 2026-07-10, before execution. Reviewed spec: Claude +
ChatGPT round complete.

## Target clarification (MAGI round 2)
This computation measures the NON-SINGLET SU(2) orientation/Skyrme
coefficient (pion-direction legs, alternating-flavor pattern), for
which exact Goldstone-ness makes A0_total = 0 an exact requirement.
It does NOT measure the anomalous U(1)_A singlet (eta) sector, where
the anomaly legitimately generates a potential and A0 != 0. State
this in all outputs.

## Objective
Determine the dimensionless Skyrme coefficient kappa_U of the chiral
field to a stated error band, resolving the current 9x normalization
spread (0.054 vs 0.49 across mass points).

## Pre-registered kill criterion (verbatim, print with results)
If the pinned kappa_U places S_mono = 20 x 32 N kappa_U outside
[140, 550] (i.e., beta outside ~[7, 28], allowing the factor-2
geometric-constant mush around the required S = 276), THE DARK-ENERGY
CHAIN TERMINATES. Inside the window: proceed to C2b. No post-hoc
window adjustment.

## Root-cause hypotheses for the 9x spread (to be discriminated)
H1 Kinematic contamination: e = 0.18 with m = 0.15 puts k/m > 1 --
   outside the derivative-expansion radius; k^4 fit contaminated by
   all higher orders.
H2 Missing seagull/contact diagrams of the exponential vertex.
H3 Vertex normalization convention (the m^4 factor).

## Method

### 1. Vertex set (from m e^{i gamma5 theta} expanded)
   V1 = i m gamma5 theta         (1-point)
   V2 = -(m/2) theta^2           (2-point, scalar)
   V3 = -(i m/6) gamma5 theta^3  (3-point)
   V4 = +(m/24) theta^4          (4-point)
Diagram classes for the 4-theta amplitude at O(k^4), with symmetry
factors to be derived and printed:
   BOX      (V1,V1,V1,V1)  -- the only class in the old script
   TRIANGLE (V1,V1,V2)
   BUBBLE   (V2,V2)
   SUNSET   (V1,V3)
   CONTACT  (V4)           -- verify analytically it is k-independent
All classes with >=2 propagators contribute at O(k^4); their omission
is H2. Flavor weights per class from the U(2) trace structure,
derived symbolically and cross-checked against the old box weights
(-2,+2,+2).

### 2. Normalization anchor (Ward identity) -- resolves H3
Axial Ward identity: at zero momentum the 1-point gamma5 vertex
normalization is tied to the condensate, Gamma_5(0) ~ m <psibar psi>
/ f_pi^2-structure (PCAC). Concretely: verify numerically that the
2-point function of V1 at q -> 0 reproduces the chiral relation
Pi_P(0) = <psibar psi>/m within MC error, thereby FIXING whether the
physical kappa_U carries the m^4 factor. This check is mandatory and
reported before any kappa value.

### 3. Kinematics -- resolves H1
   e <= m/3 for every mass point; at least three e values per mass
   (e.g. m/6, m/4, m/3) demonstrating a PLATEAU of the extracted
   O(k^4) coefficients (plateau = variation < MC error). Fit in
   lambda with basis {lambda^2, lambda^4, lambda^6}; report the
   lambda^6 coefficient as a contamination diagnostic.

### 4. Operator basis and overdetermination
   At least four kinematic configurations projecting the two quartic
   structures (O1, O2): the 2x2 solve becomes an overdetermined
   least-squares; the residual is a systematic-error estimate,
   reported.

### 5. Mass scan and extrapolation
   m/Lambda in {0.08, 0.12, 0.15, 0.20, 0.30}. Fit
   kappa_U(m) = a ln(Lambda/m) + b (the scheme-expected law).
   The operating-point value and the coefficient a are both reported;
   consistency of the log law across the scan is itself a validity
   gate (failure => scheme contamination unresolved => report
   inconclusive, do NOT force a number).

### 6. Error budget (reported as a stacked band)
   MC statistical (multiple seeds: 11, 23, 47) + plateau spread (H1
   residual) + overdetermination residual (basis systematic) + m^4
   anchor uncertainty (from the Ward-identity check's MC error).

### 7. Deliverables
   kappa_U(m) table with total band; the gate arithmetic
   S_mono = 640 kappa_U (N=3) vs [140, 550]; verdict line printed
   verbatim from the kill criterion; all code + CSV committed
   (new repo or Paper 5 campaign repo, branch c2a).

## PILOT RESULTS (2026-07-10, in-session — regression targets)
P1 Ward anchor VERIFIED exactly: m Pi_P(0) = -<psibar psi> (ratio
   1.0000000000 at m = 0.15, 0.30). H3 settled: kappa_U = m^4 kappa_raw.
P2 LEAKAGE MECHANISM FOUND: box-only amplitude has A0 = box(k=0) != 0
   (chirally incomplete set); the old fit basis {l^2,l^4,l^6} lacked a
   constant, so A0 leaked into the l^4 coefficient, diverging as 1/e^4
   (measured: kappa_raw 60 -> 637 -> 10191 for e = 0.18/0.10/0.05 at
   m=0.3, exact 2^4 steps). The July-8 magnitude AND sign are
   leakage-dominated artifacts; even the log-growth mimicked the
   expected law (A0 itself grows toward the chiral limit).
P3 Constant-included fit (NMC=4e5, seed 11) — regression targets:
     m=0.30, e=0.10:  A0 = -0.07973,  kappa_raw = -0.235
     m=0.30, e=0.05:  A0 = -0.07973,  kappa_raw = -0.280
     m=0.15, e=0.05:  A0 = -0.14327,  kappa_raw = -5.561
   => plateau-level kappa_U ~ -0.002..-0.003: one-loop-natural
   magnitude, NEGATIVE sign. If this survives the seagulls, the kill
   criterion FIRES (S ~ 1.6, overshoot) and the negative sign breaks
   the induced-Maxwell construction. NOT final: box-only is provably
   incomplete (P2).
P4 NEW MANDATORY GATE — chiral completeness: with ALL diagram classes
   (box+triangle+bubble+sunset+contact) the k=0 amplitude must cancel:
   |A0_total| < 3x MC error. This is the machine test that the diagram
   set and flavor weights are right. Report A0 per class.
P6 REGULATOR GATE (MAGI round 2): the sharp momentum cutoff is not
   shift-invariant and can itself leave a spurious contact residual.
   If A0 cancellation fails, FIRST run a momentum-routing test (same
   routing prescription enforced across all diagram classes; vary the
   routing and check A0 stability) and a symmetry-preserving
   subtraction, before concluding the diagram set is wrong. The
   sharp-cutoff MC is a PROXY; the decisive version, if the verdict
   is load-bearing, is the overlap-lattice derivative expansion.
   Repeat the A0 cancellation and ONE representative k^4 point under
   a second prescription (e.g., Pauli-Villars-like subtraction or
   dimensional-style symmetric routing) as cross-validation.
P7 ANALYTIC-SLOPE GATE (MAGI round 2): derive symbolically the
   analytic one-loop derivative-expansion (heat-kernel) coefficient
   of the Skyrme term for the constituent fermion loop, cross-checked
   against at least one literature convention (e.g., Ebert-Reinhardt
   or Diakonov-Petrov). The fitted log slope a in
   kappa_U(m) = a ln(Lambda/m) + b must agree with it within the
   total error band; the constant b may be scheme-dependent. Failure
   => normalization or combinatorics unresolved => report
   inconclusive.
P5 STATUS FREEZE: Paper 4 v5.6-5.8 monopole-gate claims and Paper 5's
   kappa-sign entry are SUSPENDED pending this computation. No
   submission of either until the verdict line prints.

## Execution estimate
Continuum sharp-cutoff MC proxy (skyrme_sign2 lineage): ~5 diagram
classes x 5 masses x 3 e-values x ~6 lambda points; box-class cost
~1 min/point => full run a few hours CPU. Suitable for Claude Code;
core verification runs feasible in-session.

## Explicitly out of scope (no concept expansion)
C2b (twisted-loop chi_top), C2c (f normalization), C2e (homogeneous-DE
LIV checklist: theta-dot, DE perturbations, sound speed, early-universe
evolution), DESI forward-fit protocol (registered separately: kill via
full w(z) forward-fit, not CPL w_0 sign).

---

## Branch note (this session)

The verified state was pushed to `origin/c2a`. This session's designated
working branch is `claude/c2a-kappa-u-skyrme-35v1ap`, fast-forwarded from
`origin/c2a` (a linear descendant of the initial commit) so the full verified
lineage is preserved and continuation work is pushed to the designated branch.
