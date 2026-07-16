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
