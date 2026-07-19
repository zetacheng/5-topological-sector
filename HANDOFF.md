# Current Handoff

## Current task

The `P5-OMEGA-01` gate record is merged as `FAILED`, and Paper 5 v0.24 synchronizes the paper text with that verdict (`PROG-SYNC-01`, Paper 5 side).

## Status separation

- Calculation and reproduction: complete.
- Migration: complete including the PI-supplied Paper 5 v0.23 source alongside v0.22; figures and bibliography remain unavailable.
- Independent scientific review: complete.
- PI acceptance: complete.
- Merge readiness: accepted gates are ready for merge.

## Next scientific item

The Paper 5 side of the `PROG-SYNC-01` synchronization is complete: v0.24 is imported, and the paper text now states the `P5-OMEGA-01` continuum-radius gate as run-and-failed, consistent with `P5-CL-008` `FAILED`. The remaining programme edits are outside this repository:

1. Paper 3 minimal tense/status update.
2. Paper 1 governance-branch correction before merge.
3. Programme register synchronization after the owning-repository merges.

## Scientific question

Does the migration faithfully establish C2a and `c_GW=1` without importing Paper 3, Paper 4, or Paper 1 authority?

## Locked inputs

Inventory source SHAs; exact/PV state `cba89de41183d08c587af5187edfbc8de659df9f`; separable GW commit `0ba85e578d438f4f9abcb2a10c501e74acc0b190`.

## Do not reopen

P5-C2A-01/02/03/04 or P5-GW-01 unless a concrete inconsistency is documented; the failed positive claim; cross-paper ownership decisions.

## Required next input

Paper 5 figures and bibliography; PI scope approval and ownership decision for `legacy-kappa/topo-mass-radius` and `legacy-kappa/wrinkle-bound-excitation`.

## Expected Codex output

A reviewable migration PR with reproducible scripts, tests, immutable outputs, ledgers, and exclusions.

## Questions for ChatGPT

Can the mixed topological mass/radius record be separated from Paper 3 omega assumptions? Which CP1/Hopf/WZW/U(2)/U(3) gate is next?

## Questions for Claude

Verify the exact coefficient, PV sign, GW normalization, ambiguous classifications, and overclaim boundaries.

## Role separation

ChatGPT plans; Codex implements and preserves provenance; Claude reviews; the PI accepts verdicts and authorizes paper updates.
