# Gate Registry

Allowed statuses: `PROPOSED`, `SPECIFIED`, `RUNNING`, `PASS`, `FAIL`, `INCONCLUSIVE`, `SUSPENDED`, `RETIRED`.
## P5-C2A-01 — Full diagram-set and chiral-completeness gate

Status: PASS

### Scientific question

Does the complete non-singlet amplitude include all five classes and cancel at zero momentum pointwise?

### Scope

SU(2) non-singlet box, triangle, bubble, sunset, and contact.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Legacy commits `168d890334e67a4bbfca4dea5b84e8036a44acfa` and `2f9758dcf105c10dcd53a420d95ef4f9bd505765`.

### Analytic anchors

Box weights `(-2,+2,+2)`, symmetry sums `(16,48,16,32,16)`, and pointwise `A0=0`.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

All five classes are present; analytic and matrix densities agree and cancel to machine precision.

### Reviewer verdict

Legacy accepted record: PASS. Destination migration review pending.

### Independent reviewer verdict

PASS — independently reproduced by Claude on 2026-07-16.

### PI acceptance

ACCEPTED — 2026-07-16.

### Claim-promotion status

COMPLETED for the associated accepted claim or claims.

### Consequences

Incomplete box-only and positive-coefficient routes cannot be used.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`derivations/c2a/diagram_classes.md`; `scripts/c2a/derive_classes.py`; `results/c2a/raw/p4_gate_output.txt`.

### Migration provenance

Legacy commits `168d890334e67a4bbfca4dea5b84e8036a44acfa` and `2f9758dcf105c10dcd53a420d95ef4f9bd505765`.

### Date opened

2026-07-11 (legacy record).

### Date closed

2026-07-11 (legacy record).
## P5-C2A-02 — Production coefficient scan

Status: PASS

### Scientific question

Is the coefficient stable across mass, momentum plateau, routing, seeds, and evaluators?

### Scope

Five masses, three seeds, three momentum fractions, and four kinematic configurations.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Source commits `6167438acbfb16f6d723775fffe67bc40f1fe67c`, `6210279f22693da6f7f4406509203ad8d495aa88`, `f225fe880f1874d4522e61db160551ec468dbe8a`.

### Analytic anchors

Constant-included fit and Ward normalization `kappa_U=m^4 kappa_raw`.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

The aggregate gives `kappa_U approximately -0.00149` across the controlled scan.

### Reviewer verdict

Legacy accepted record: PASS. Destination migration review pending.

### Independent reviewer verdict

PASS — independently reproduced by Claude on 2026-07-16.

### PI acceptance

ACCEPTED — 2026-07-16.

### Claim-promotion status

COMPLETED for the associated accepted claim or claims.

### Consequences

Proceed to exact/PV gates; reject positive-sign interpretations.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`scripts/c2a/production_scan.py`; `scripts/c2a/aggregate.py`; `results/c2a/raw/scan_data.csv`.

### Migration provenance

Source commits `6167438acbfb16f6d723775fffe67bc40f1fe67c`, `6210279f22693da6f7f4406509203ad8d495aa88`, `f225fe880f1874d4522e61db160551ec468dbe8a`.

### Date opened

2026-07-12 (legacy record).

### Date closed

2026-07-12 (legacy record).
## P5-C2A-03 — Exact closed-form derivation

Status: PASS

### Scientific question

What is the exact finite-cutoff coefficient and controlled small-`m/Lambda` limit?

### Scope

All five classes in a sharp Euclidean four-ball.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Source commit `4a0de1e2d6875f0ac27907395b3fc28b6bd7ce25`, finalized at `cba89de41183d08c587af5187edfbc8de659df9f`.

### Analytic anchors

Exact radial integrals; cancellation of `m^2` and `m^4` corrections; positive denominator.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

`kappa_U(m,Lambda)=Lambda^4(-17 Lambda^6-85 Lambda^4 m^2-170 Lambda^2 m^4-90 m^6)/(1152 pi^2 (Lambda^2+m^2)^5)` and limit `-17/(1152 pi^2)`.

### Reviewer verdict

Legacy definitive check: PASS. Destination migration review pending.

### Independent reviewer verdict

PASS — independently reproduced by Claude on 2026-07-16.

### PI acceptance

ACCEPTED — 2026-07-16.

### Claim-promotion status

COMPLETED for the associated accepted claim or claims.

### Consequences

The controlled quartic coefficient is exactly negative.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`derivations/c2a/exact_kappa_derivation.md`; `scripts/c2a/derive_kappa_closed.py`; `results/c2a/raw/closed_form_output.txt`.

### Migration provenance

Source commit `4a0de1e2d6875f0ac27907395b3fc28b6bd7ce25`, finalized at `cba89de41183d08c587af5187edfbc8de659df9f`.

### Date opened

2026-07-13 (legacy record).

### Date closed

2026-07-13 (legacy record).

## P5-OMEGA-01 — Scope-separated omega-channel health gate

Status: PROPOSED

### Scientific question

Do the four omega health gates survive scope-separated re-derivation?

### Scope

Paper 5-facing checks of `Z_omega`, `M_omega^2`, `g_omegaB`, and `D_00`, together with the upstream Fierz pinning `G_omega=-G/N`. Paper 1 dark-matter framing and Paper 3 vector-sector authority are excluded.

### Locked assumptions

None locked. PI scope separation and applicable conventions are required before specification.

### Inputs

Paper 5 v0.23 and the scope-separated companion records in `zetacheng/3-vector-sector` as cross-repository references only. No omega production artifacts are imported into this repository.

### Cross-repository caveats

The four health gates hold for any `g0 > 0` and are coupling-independent. The below-threshold pole requires `g0 > 1/(4 m_f^2 Z_omega) ~ 10.6`; the artifact value `g0 = 20` is representative, not derived from `G/N`. At that coupling, `m_omega ~ 1.4 m_f`, not `m_f << m_omega << Lambda`.

### Analytic anchors

The separable `c_GW=1` result at P5-GW-01 is the only supported upstream anchor in this repository; it does not establish the omega health claims.

### Regression anchors

None registered.

### Kill criterion

The continuum nonlocal radius scan must give `R_star >> a` with `E''(R_star) > 0`; a cutoff-scale minimum is a lattice lump, not continuum topological matter.

### Required computations

Scope-separated re-derivation of the Fierz pinning, induced kinetic coefficient, mass, topological-current coupling, static kernel, and full nonlocal radius scan.

### Required deliverables

Committed derivation notes, locked conventions, scripts, tests, regression anchors, immutable outputs, provenance, and an independent review verdict.

### Result

Not run in this repository.

### Reviewer verdict

PENDING

### Consequences

P5-CL-009 through P5-CL-013 remain `PROPOSED` in this repository. The companion paper owns the omega existence, health, and repulsive-kernel claims; Paper 5 retains the topological-stabilization question and its continuum-radius kill criterion.

### Repository branch

Future `gate/p5-omega-01` branch after PI scope approval.

### Relevant files

`paper/paper5_internal_dimension_v0_23.tex`; `CLAIMS.md`; `MIGRATION.md`.

### Migration provenance

Scope-separated companion migration in `zetacheng/3-vector-sector`: P3-FIERZ-01, P3-VEC-O1/O2/O3, and P3-OMEGA-01. Paper 5 retains references only.

### Date opened

2026-07-16

### Date closed

Open.
## P5-C2A-04 — Regulator and PV sign confirmation

Status: PASS

### Scientific question

Does the negative sign survive a second chirally consistent regulator?

### Scope

Common PV form factor at `M_PV=2,4,8` plus exact cutoff comparison.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Source commit `cba89de41183d08c587af5187edfbc8de659df9f`.

### Analytic anchors

PV preserves pointwise `A0=0`; all PV coefficients are negative and approach the sharp result.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

Negative sign confirmed; exact controlled value remains `-17/(1152 pi^2)`.

### Reviewer verdict

Legacy Task B: PASS. Destination migration review pending.

### Independent reviewer verdict

PASS — independently reproduced by Claude on 2026-07-16.

### PI acceptance

ACCEPTED — 2026-07-16.

### Claim-promotion status

COMPLETED for the associated accepted claim or claims.

### Consequences

The positive-sign claim fails independently of the production regulator.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`scripts/c2a/pv_check.py`; `results/c2a/processed/TaskB_PV_signcheck.md`.

### Migration provenance

Source commit `cba89de41183d08c587af5187edfbc8de659df9f`.

### Date opened

2026-07-13 (legacy record).

### Date closed

2026-07-13 (legacy record).
## P5-GW-01 — Goldstone–Wilczek normalization

Status: PASS

### Scientific question

Does the fermion-loop topological current match the baryon current with unit coefficient?

### Scope

Only the separable topological-current loop; C6/vector conclusions are excluded.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Source commit `0ba85e578d438f4f9abcb2a10c501e74acc0b190`.

### Analytic anchors

`B^mu=epsilon Tr(L L L)/(24 pi^2)` and `B0_ref=-i a^3/(2 pi^2)`.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

`c_GW(a->0)=0.999885`, accepted as `c_GW=1`.

### Reviewer verdict

Legacy hard gate: PASS. Destination migration review pending.

### Independent reviewer verdict

PASS — independently reproduced by Claude on 2026-07-16.

### PI acceptance

ACCEPTED — 2026-07-16.

### Claim-promotion status

COMPLETED for the associated accepted claim or claims.

### Consequences

Paper 5 may use unit topological-current normalization; no Paper 3 vector conclusion follows.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`derivations/goldstone-wilczek/`; `scripts/goldstone_wilczek/`; `results/goldstone-wilczek/`.

### Migration provenance

Source commit `0ba85e578d438f4f9abcb2a10c501e74acc0b190`.

### Date opened

2026-07-13 (legacy record).

### Date closed

2026-07-13 (legacy record).
## P5-SK-STAB-01 — Former positive-Skyrme stabilization route

Status: RETIRED

### Scientific question

Can the historical minimal route rely on a positive quartic coefficient?

### Scope

Only the route whose defining premise is `kappa_U>0`.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Closed P5-C2A-03 and P5-C2A-04; source commits `4a0de1e`, `cba89de`.

### Analytic anchors

Exact negative coefficient and PV sign.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

The positive premise is false; the route is retired.

### Reviewer verdict

Legacy C2a record withdraws the positive route. Destination review pending.

### Consequences

Any stabilization proposal requires distinct higher-order or nonperturbative physics and a new gate.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`results/c2a/verdict.md`; `CLAIMS.md`; `DECISION_LOG.md`.

### Migration provenance

Closed P5-C2A-03 and P5-C2A-04; source commits `4a0de1e`, `cba89de`.

### Date opened

2026-07-13 (retired by exact record).

### Date closed

2026-07-13 (retired by exact record).
## P5-BERRY-01 — One-loop induced Berry-Maxwell sign

Status: FAIL

### Scientific question

Does this one-loop sector supply the formerly claimed healthy positive coefficient?

### Scope

Only the direct sign consequence at the tested order; no higher-order mechanism.

### Locked assumptions

Only assumptions recorded in the cited migrated derivation/configuration; Paper 3/4/1 assumptions are excluded.

### Inputs

Source `6210279f22693da6f7f4406509203ad8d495aa88` plus exact/PV confirmation.

### Analytic anchors

Exact and PV-confirmed negative coefficient.

### Regression anchors

Corresponding tests under `tests/c2a/` or `tests/goldstone_wilczek/`.

### Kill criterion

Failure of a cited identity, tolerance, sign, or provenance check.

### Required computations

Reproduce the cited scripts and regression tests from the recorded configuration.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, and test.

### Result

The former healthy-positive sign claim fails at the tested order.

### Reviewer verdict

Legacy Paper 5 consequence recorded in the C2a result. Destination review pending.

### Consequences

A positive term requires a separately specified and reviewed mechanism.

### Repository branch

`sync/kappa-c2a-paper5-migration`

### Relevant files

`results/c2a/processed/RESULTS_C2a.md`; `CLAIMS.md`; `DECISION_LOG.md`.

### Migration provenance

Source `6210279f22693da6f7f4406509203ad8d495aa88` plus exact/PV confirmation.

### Date opened

2026-07-13 (legacy record).

### Date closed

2026-07-13 (legacy record).
