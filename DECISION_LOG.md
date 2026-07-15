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


## 2026-07-15 — Accept exact negative Paper 5 quartic coefficient

### Decision

Accept the migrated result `kappa_U=-17/(1152 pi^2)`, subject to destination migration review.

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

## 2026-07-15 — Withdraw positive Skyrme claim

### Decision

Withdraw the positive quartic claim and retire stabilization arguments requiring it.

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

## 2026-07-15 — Withdraw healthy-positive one-loop Berry-Maxwell sign

### Decision

Record the inherited healthy-positive sign claim as failed at the tested order.

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
