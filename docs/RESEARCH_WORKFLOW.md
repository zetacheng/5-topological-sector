# Research Workflow

## Roles

- **ChatGPT:** conceptual discussion, physical interpretation, analytic derivation planning, gate design, calculation specifications, assumptions, and competing interpretations. ChatGPT does not certify numerical results.
- **Codex:** repository maintenance, symbolic and numerical implementation, tests, regression anchors, reproducibility, result files, and branch and commit discipline. Codex must not promote a result into a paper claim without review.
- **Claude:** independent reviewer/discriminator; reviews derivations and results, issues gate verdicts, identifies overclaims, and updates the paper only after results are accepted.
- **User / Principal Investigator:** owns the physical programme; approves assumptions, gates, and scope changes; accepts or rejects final verdicts; decides when paper text may be updated.

## Standard gate workflow

1. The PI approves the scientific question, scope, assumptions, anchors, kill criterion, and required deliverables.
2. ChatGPT prepares a calculation specification and identifies competing interpretations.
3. The derivation note is completed and committed before production code.
4. Codex implements on a single gate branch and records tests, anchors, configuration, environment, raw outputs, processed artifacts, and provenance.
5. Claude performs an independent review and records `PASS`, `FAIL`, or another permitted gate verdict with limitations and overclaim checks.
6. The PI accepts or rejects the verdict and authorizes any claim-ledger or paper update.

Code execution alone is not evidence of gate passage. Failed and inconclusive routes remain preserved.
