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

The audited legacy refs contain no clean authoritative Paper 5 paper source, figure set, or bibliography. The PI separately supplied `paper5_internal_dimension_v0_23.tex`, now imported under `paper/` alongside v0.22; figures and bibliography remain unavailable.

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
- [x] no claim was promoted before independent review and PI acceptance

GNU Make was unavailable in the Windows migration environment. Each Make target's
underlying command was run directly: structure test, Ruff, pytest, and the combined
Ruff-plus-pytest check all passed. GitHub CI remains configured to run the same checks.

## Unresolved review items

- The legacy `topo-mass-radius` route combined Paper 5 topology with Paper 3 omega inputs and Paper 1 dark-matter framing. Its omega quantities and Fierz pinning have since been scope-separated into `zetacheng/3-vector-sector`; Paper 5 retains cross-repository references only under P5-OMEGA-01.
- `legacy-kappa/wrinkle-bound-excitation` combines Paper 4 interface and Paper 1 excitation/DM framing.
- Paper 5 v0.23 source is imported alongside v0.22; its figures and bibliography remain unavailable.
- Independent Claude review and PI acceptance are complete for the authoritative C2a and separable Goldstone-Wilczek records.

## Migration assessment

`SCIENTIFIC RECORD MIGRATION COMPLETE — ANCILLARY PAPER ASSETS AND MIXED-OWNERSHIP ROUTES REMAIN OPEN.`

- Authoritative C2a scientific record: complete.
- Separable Goldstone-Wilczek record: complete.
- Independent review: complete.
- PI acceptance: complete.
- Latest Paper 5 v0.23 source: present.
- Figures and bibliography: pending.
- Mixed-ownership `topo-mass-radius` and `wrinkle-bound-excitation`: intentionally not imported and still require separate ownership review.
