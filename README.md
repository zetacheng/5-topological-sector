# 5-topological-sector

Paper 5 — **Topological Sector of the Lattice Fermion Condensate**

Core scientific responsibility: CP1/Hopf structure, Skyrme coefficient, WZW level, baryon topology, U(3), and topological quantization.

This repository contains one paper only. Historical scientific progress will be imported separately.

## Current status

`INFRASTRUCTURE INITIALIZED`

## Role separation

- **ChatGPT:** conceptual discussion, physical interpretation, analytic derivation planning, gate design, calculation specifications, and identification of assumptions and competing interpretations. ChatGPT does not certify numerical results.
- **Codex:** repository maintenance, symbolic and numerical implementation, tests, regression anchors, reproducibility, result files, and branch and commit discipline. Codex must not promote a result into a paper claim without review.
- **Claude:** independent reviewer/discriminator; reviews derivations and results, gives gate verdicts, identifies overclaims, and updates the paper only after results are accepted.
- **User / Principal Investigator:** owns the physical programme, approves assumptions, gates, and scope changes, accepts or rejects final verdicts, and decides when paper text may be updated.

## Directory guide

- `paper/`: paper source and figures after approved import.
- `derivations/`: preregistered analytic derivation notes.
- `scripts/`: reproducible symbolic and numerical implementations.
- `tests/`: repository, regression, and scientific tests.
- `results/`: immutable raw outputs and provenance-linked processed artifacts.
- `reviews/`: independent ChatGPT and Claude review records.
- `docs/`: workflow, result schema, and branching policy.
- `archive/`: preserved retired routes and historical material.

## Standard gate workflow

1. The PI approves the question, assumptions, scope, and gate.
2. ChatGPT prepares the derivation plan and calculation specification.
3. A derivation note is committed before production code.
4. Codex implements the calculation, tests, anchors, and reproducible artifacts on one gate branch.
5. Claude independently reviews the derivation and result and records a verdict.
6. The PI accepts or rejects the verdict. Only accepted results may affect paper text.

## Reproducibility commands

```text
make check
make test
make lint
make structure
```

## Warning

No result is accepted merely because code runs. A result requires analytic and regression anchors, tests, stored outputs, complete provenance, and independent review.
