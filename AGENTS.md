# Agent Rules

These rules apply to all future human-assisted and AI-assisted work in this repository.

## Required reading

Before making changes, read `PROGRESS.md`, `GATES.md`, `DECISION_LOG.md`, `CLAIMS.md`, `HANDOFF.md`, and `CONVENTIONS.md`.

## Role separation

- **ChatGPT:** conceptual discussion, physical interpretation, analytic derivation planning, gate design, calculation specifications, assumptions, and competing interpretations. ChatGPT does not certify numerical results.
- **Codex:** maintenance, symbolic and numerical implementation, tests, regression anchors, reproducibility, results, and disciplined branches and commits. Codex must not promote a result into a paper claim without review.
- **Claude:** independent reviewer/discriminator, gate verdicts, overclaim detection, and paper updates only after acceptance.
- **User / Principal Investigator:** owns the physical programme; approves assumptions, gates, and scope changes; accepts or rejects verdicts; authorizes paper updates.

## Mandatory rules

1. Never reopen a closed gate unless a concrete inconsistency is documented.
2. Never silently change conventions.
3. Commit a derivation note before production code.
4. Tests and regression anchors are mandatory.
5. Never edit raw outputs manually.
6. Processed results must identify the script and raw input used.
7. Do not update `.tex` paper files before reviewer acceptance.
8. Preserve failed results.
9. Explicitly distinguish the original model, a model extension, a phenomenological EFT, and a numerical proxy.
10. Every result must identify its regulator, cutoff, normalization, seeds, and operating point.
11. One branch corresponds to one scientific gate or one paper-edit task.

The standard gate workflow is PI approval, ChatGPT specification, committed derivation note, Codex implementation and artifacts, Claude review and verdict, then PI acceptance or rejection. Paper changes follow only after acceptance.
