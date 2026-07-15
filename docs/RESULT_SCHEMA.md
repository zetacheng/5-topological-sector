# Result Schema

Raw outputs are immutable. Never edit, normalize, or replace raw data manually. Corrections require a new recorded run.

Processed results must identify the exact producing script, configuration, and raw inputs. Every result directory must record:

- `README.md` describing the question and artifact inventory;
- configuration, normally `config.json`;
- raw output;
- processed table;
- reviewer-facing verdict;
- exact commit hash;
- branch;
- run date;
- environment information;
- regulator, cutoff, normalization, seeds, and operating point when applicable.

Recommended future directory:

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

Checksums are recommended for immutable raw artifacts. A processed artifact must be reproducible from its recorded raw inputs and script at the recorded commit.
