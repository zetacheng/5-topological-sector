# C2a Results

This directory contains the immutable legacy evidence for the complete non-singlet five-class orientation-sector calculation.

## Reproduction commands

Run from the repository root with the project development dependencies installed:

```text
python -m scripts.c2a.derive_classes
python -m scripts.c2a.p4_gate
python -m scripts.c2a.aggregate results/c2a/raw/scan_data.csv
python -m scripts.c2a.derive_kappa_closed ball
python -m scripts.c2a.pv_check
```

The full P4 and PV commands are computationally substantial. The pytest regression suite exercises the same anchors with reduced deterministic samples where appropriate. The committed raw outputs remain the comparison targets.

## Required reproductions

- exact coefficient and finite-cutoff expression;
- negative sign;
- pointwise (A_0=0);
- aggregate table from `scan_data.csv`;
- PV comparison.

## Directory contract

- `config/`: migrated run parameters.
- `raw/`: immutable byte-for-byte legacy output and data blobs.
- `processed/`: byte-for-byte legacy result narratives.
- `figures/`: reserved; the legacy record contained no C2a figures.
- `verdict.md`: Paper 5-scoped verdict.
- `PROVENANCE.md`: source-to-destination ledger.
- `environment.txt`: migration/reproduction environment; the exact legacy environment was not recorded.

