# Result Standards

Raw outputs are immutable and must never be edited manually. Processed results must record their provenance, including the exact script, configuration, and raw inputs used.

Every result directory must include a `README.md`, configuration, raw output, processed table, verdict, commit hash, branch, date, and environment information.

Recommended layout:

```text
results/<gate-id>/
  README.md
  config.json
  raw/
  processed/
  figures/
  verdict.md
  environment.txt
```

The top-level `raw/`, `processed/`, and `figures/` directories are staging locations only until historical records are audited into gate-specific result directories.
