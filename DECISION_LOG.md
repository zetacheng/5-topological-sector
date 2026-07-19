# Decision Log

This log is append-only. Corrections and reversals must be recorded as new entries that reference the earlier decision.

## 2026-07-15 — Separate the five papers into five repositories

### Decision

Maintain each of the five papers in its own repository. This repository is reserved for Paper 5 only.

### Reason

Separate repositories establish clear scientific scope, provenance, gates, review, and paper ownership.

### Evidence

The approved five-repository mapping supplied during infrastructure initialization.

### Consequences

Material from another paper repository must not be merged here. Cross-paper dependencies must be referenced explicitly and imported only with PI approval.

### Supersedes

None.

### Related gate

None; infrastructure decision.

### Related branch and files

`main`; repository governance files.


## 2026-07-15 — Record exact negative Paper 5 quartic coefficient as supported

### Decision

Record the migrated result `kappa_U=-17/(1152 pi^2)` as reproducibly supported, pending independent reviewer and PI acceptance.

### Reason

Five-class, exact, numerical, and PV records agree.

### Evidence

Commits `4a0de1e`, `cba89de`; gates P5-C2A-01 through 04.

### Consequences

Paper 5 must use the negative coefficient.

### Supersedes

Any former positive coefficient.

### Related gate

P5-C2A-03/04

### Related branch and files

Migration branch; `derivations/c2a/`, `results/c2a/`.

## 2026-07-15 — Record positive Skyrme claim as failed

### Decision

Preserve the historical positive quartic claim in the ledger with `FAILED` status and retire stabilization arguments requiring it.

### Reason

The exact coefficient is negative.

### Evidence

P5-C2A-03/04.

### Consequences

New stabilization requires a separate gate.

### Supersedes

Former positive-Skyrme route.

### Related gate

P5-SK-STAB-01

### Related branch and files

Migration branch; `CLAIMS.md`.

## 2026-07-15 — Record healthy-positive one-loop Berry-Maxwell sign as failed

### Decision

Preserve the historical inherited healthy-positive sign claim in the ledger with `FAILED` status at the tested order.

### Reason

Its migrated source coefficient is negative.

### Evidence

Accepted C2a result and PV confirmation.

### Consequences

No positive claim without a new mechanism.

### Supersedes

Former one-loop positive sign entry.

### Related gate

P5-BERRY-01

### Related branch and files

Migration branch; `CLAIMS.md`.

## 2026-07-15 — Reassign vector, Fierz, omega, and C6 authority to Paper 3

### Decision

Treat U(3) Fierz, omega, RPA/vector, C6, and vector stabilization verdicts as Paper 3-owned.

### Reason

They are vector-sector results in a mixed repository.

### Evidence

Inventory commits `0ba85e5` through `d80431b`.

### Consequences

Only separable `c_GW` evidence migrates.

### Supersedes

Mixed legacy ownership.

### Related gate

P5-GW-01

### Related branch and files

Inventory; `zetacheng/3-vector-sector`.

## 2026-07-15 — Treat Paper 4 consequences as downstream dependencies

### Decision

Paper 5 owns the coefficient and direct sign consequences, not dark-energy/interface/cosmological conclusions.

### Reason

Those subjects belong to Paper 4.

### Evidence

Inventory of Paper 4 branches.

### Consequences

Paper 4 artifacts remain excluded.

### Supersedes

Mixed legacy ownership.

### Related gate

P5-C2A-03/04

### Related branch and files

Inventory; `zetacheng/4-dark-energy-cosmology`.

## 2026-07-15 — Retain kappa-c2a as archive, not future authority

### Decision

Preserve the legacy repository unchanged as a mixed archive; future Paper 5 work occurs here.

### Reason

The legacy repository mixes paper ownership.

### Evidence

Full inventory.

### Consequences

No history merge; use file-level SHAs.

### Supersedes

Use of the legacy repo for active Paper 5 work.

### Related gate

None; migration governance.

### Related branch and files

Migration branch; `archive/LEGACY_KAPPA_C2A.md`.

## 2026-07-16 — Accept C2a and Goldstone-Wilczek review verdict

### Decision

Accept the independent C2a and Goldstone-Wilczek review verdict and promote P5-CL-001, P5-CL-002, P5-CL-003, and P5-CL-007 to `VERIFIED`.

### Reason

Independent clean-environment reproduction and mutation-tested symbolic regression satisfy the repository `VERIFIED` standard.

### Evidence

- `reviews/claude/2026-07-16-c2a.md`
- Branch `fix/audit-2026-07-16`
- 15/15 tests
- Unchanged raw artifacts

### Consequences

- The four claims may be cited as verified in Paper 5.
- Omega claims may not be cited as verified.
- P5-OMEGA-01 remains the next scope-separated migration item.

### Supersedes

None.

### Related gate

- P5-C2A-01
- P5-C2A-02
- P5-C2A-03
- P5-C2A-04
- P5-GW-01

### Related branch and files

`fix/audit-2026-07-16`; `CLAIMS.md`, `GATES.md`, and `reviews/claude/2026-07-16-c2a.md`.

## 2026-07-16 — Retract minimal-pair zero V/A Fierz entry

### Decision

Retract this note's Fierz entry that the minimal chiral pair gives identically zero vector and axial couplings, and retract the single-coupling economy postulate erected on it.

### Reason

The zero was a `gamma5`-without-the-`i` convention slip. The chirally invariant pair gives `|c_V| = |c_A| = 1/2`.

### Evidence

`paper/paper5_internal_dimension_v0_23.tex`, Sec. “Gates and next actions,” Fierz arithmetic; `zetacheng/3-vector-sector` P3-FIERZ-01 and `results/u3-fierz/`; independent reviewer confirmation against the standard Fierz table.

### Consequences

Cross-channel ratios are Fierz-inherited. Any programme statement resting on vanishing V/A content or the economy postulate requires re-examination; those statements are owned by companion papers and are flagged, not amended here.

### Supersedes

The v0.19 Fierz entry.

### Related gate

P3-FIERZ-01 (companion repository); P5-OMEGA-01 (Paper 5 topological-stabilization scope).

### Related branch and files

`paper/v0.23`; `paper/paper5_internal_dimension_v0_23.tex`, `CLAIMS.md`, `GATES.md`, and `MIGRATION.md`.

## 2026-07-18 — Migrate and close P5-OMEGA-01 as failed

### Decision

Migrate P5-OMEGA-01 from pinned legacy SHA `6a20b05e0899a878fde214c44cf77a8610d7516f`, preserve immutable evidence, land the reviewer transcript, close the stabilization gate as `FAIL`, and move precisely scoped P5-CL-008 to `FAILED`.

### Reason

The full nonlocal omega mass/radius gate had already run and failed; the owning repository required a durable, scope-separated record.

### Evidence

`results/p5-omega-01/`; `derivations/p5-omega-01/`; `reviews/claude/2026-07-16-p5-omega-01.md`; programme synchronization record `0-programme/reviews/PROG-SYNC-01.md`.

### Consequences

No omega health result is retracted and no claim is promoted to `VERIFIED`. A cutoff-scale lattice baryon remains untested. Paper 5 v0.24 text synchronization remains pending; Paper 3 needs a one-sentence downstream-status update; Paper 1’s unmerged governance branch must withdraw the failed route as a live continuum direction.

### Supersedes

Only the v0.22/v0.23 phrase “continuum-radius gate open”; not the verified Paper 3 omega-health results.

### Related gate

P5-OMEGA-01.

### Related branch and files

`gate/p5-omega-01-verdict`; `GATES.md`, `CLAIMS.md`, `HANDOFF.md`, and the migrated record.

## 2026-07-18 — Disclose the P5-CL-008 narrowing

### Decision

Restate P5-CL-008 from “A stable continuum topological matter solution exists” to “Within the tested one-loop EFT with the verified negative quartic coefficient and endogenous nonlocal omega kernel, a stable continuum (B=1) topological soliton exists,” concurrent with marking it `FAILED`.

### Reason

The original claim was broader than the gate tested. The gate fails the continuum-within-EFT proposition specifically; the scoped wording makes the claim text and its `FAILED` status agree without implying that the full theory has no baryon.

### Evidence

`reviews/claude/2026-07-16-p5-omega-01.md`, especially its Scope paragraph.

### Consequences

This is a narrowing, recorded so it is not mistaken for a silent softening of a failed claim. The reviewer accepted it on that basis. The accepted claim wording is unchanged by this entry.

### Supersedes

The prior broader wording of P5-CL-008 only.

### Related gate

P5-OMEGA-01.

### Related branch and files

`gate/p5-omega-01-verdict`; `CLAIMS.md` and `reviews/claude/2026-07-16-p5-omega-01.md`.

## 2026-07-18 — Import Paper 5 v0.24 synchronizing the failed continuum gate

### Decision

Import `paper/paper5_internal_dimension_v0_24.tex` alongside v0.22 and v0.23. The v0.24 source replaces the v0.23 description of the continuum-radius gate as *open* with a run-and-failed statement in all six places: the two abstract mentions, the in-body decisive-gate paragraph (cutoff-scale collapse, `M_omega R_star = 0.87`, `q_core/Lambda ~ 0.63`, structural collapse), the two Gate-3 (Skyrme/WZW) re-scope clauses, and a v0.24 changelog note in the status block recording `P5-OMEGA-01` `FAILED` and `P5-CL-008` `FAILED`.

### Reason

`P5-OMEGA-01` is `FAILED` and merged, with `P5-CL-008` marked `FAILED`. The paper prose still described the continuum-radius gate as open, contradicting the ledger. v0.24 makes the paper text consistent with the recorded verdict, the synchronization that `PROG-SYNC-01` and the `P5-CL-008` decision-log entry anticipated.

### Evidence

`0-programme/reviews/PROG-SYNC-01.md`; `reviews/claude/2026-07-16-p5-omega-01.md`; the merged `P5-OMEGA-01` gate record and the `P5-CL-008` `FAILED` row in `CLAIMS.md`.

### Consequences

Documentation only; no script, test, result, or number changed. Earlier versions (v0.22, v0.23) are retained unchanged as the historical record.

### Supersedes

The v0.23 paper text's description of the continuum-radius gate as open. No claim status is altered by this entry.

### Related gate

P5-OMEGA-01; P5-CL-008.

### Related branch and files

`paper/v0.24`; `paper/paper5_internal_dimension_v0_24.tex`, `PROGRESS.md`, `CLAIMS.md`, `HANDOFF.md`, `DECISION_LOG.md`.
