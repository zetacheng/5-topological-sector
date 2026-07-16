# Paper 5 Migration

## Source

Repository: `zetacheng/kappa-c2a`

## Administrative metadata

- [x] source inventory
- [x] commit provenance
- [x] branch provenance
- [x] ownership classification

## Paper source

- [x] latest Paper 5 source imported
- [ ] figures imported
- [ ] bibliography imported

The audited legacy refs contain no clean authoritative Paper 5 paper source, figure set, or bibliography. The PI separately supplied `paper5_internal_dimension_v0_22.tex`, now imported under `paper/`; figures and bibliography remain unavailable.

## Scientific record

- [x] C2a derivations
- [x] exact closed form
- [x] PV/regulator check
- [x] scripts
- [x] tests
- [x] raw outputs
- [x] processed outputs
- [x] verdicts
- [x] Goldstone-Wilczek audit
- [x] claims ledger
- [x] decision log
- [x] gate registry
- [x] failed routes
- [x] archive references

## Cross-paper exclusions

- [x] Paper 3 files excluded
- [x] Paper 4 files excluded
- [x] Paper 1 files excluded

## Validation

- [x] source hashes recorded
- [x] migrated tests pass
- [x] Ruff passes
- [x] structure tests pass
- [x] no raw outputs edited
- [x] no claim remains marked VERIFIED before independent review

GNU Make was unavailable in the Windows migration environment. Each Make target's
underlying command was run directly: structure test, Ruff, pytest, and the combined
Ruff-plus-pytest check all passed. GitHub CI remains configured to run the same checks.

## Unresolved review items

- `legacy-kappa/topo-mass-radius` combines a Paper 5 topology question with Paper 3 omega inputs and Paper 1 dark-matter framing.
- `legacy-kappa/wrinkle-bound-excitation` combines Paper 4 interface and Paper 1 excitation/DM framing.
- Paper 5 v0.22 source is imported; its figures and bibliography remain unavailable.
- Destination independent Claude/PI review remains pending.

## Migration assessment

`PARTIAL — REVIEW REQUIRED`: the authoritative C2a and separable Goldstone–Wilczek records are migrated and reproducible, and the PI-supplied v0.22 paper source is imported; figures, bibliography, and ambiguous mixed-ownership classification remain open.

Scientific artifacts are migration-complete; formal claim acceptance and paper-source synchronization remain pending.
