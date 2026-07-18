# P5-OMEGA-01 provenance

Owning gate: `P5-OMEGA-01`. Legacy source: `zetacheng/kappa-c2a` at pinned
commit `6a20b05e0899a878fde214c44cf77a8610d7516f` (not a moving branch).

## Source and immutable raw inventory

| Source path | Destination path | SHA-256 source | SHA-256 destination | Equality |
|---|---|---|---|---|
| `results/topo_verdict.txt` | `raw/topo_verdict.txt` | `abe439134428395eeba883c9e0b278e8da2224de5e7d214b2fcd00c565e56dae` | `abe439134428395eeba883c9e0b278e8da2224de5e7d214b2fcd00c565e56dae` | yes |
| `results/topo_output.txt` | `raw/topo_output.txt` | `46464138a941059948485f58c52f6686d902e5dad3ad31b511fc36fd3e5530fb` | `46464138a941059948485f58c52f6686d902e5dad3ad31b511fc36fd3e5530fb` | yes |
| `results/topo_crosscheck_output.txt` | `raw/topo_crosscheck_output.txt` | `dcbec9d415dd06a836a0d8b2adcadcbcb74bab844349eac318c986097535ad38` | `dcbec9d415dd06a836a0d8b2adcadcbcb74bab844349eac318c986097535ad38` | yes |
| `results/topo_scan.csv` | `raw/topo_scan.csv` | `1739047563decdd05cca7b5c9cc1f0120b664ef2a8622f90f429510ba6f0977e` | `1739047563decdd05cca7b5c9cc1f0120b664ef2a8622f90f429510ba6f0977e` | yes |
| `results/topo_ER_curve.csv` | `raw/topo_ER_curve.csv` | `b8acf26d455607e5b28e30431942c23658eca27841aa64352f326db2430ee08a` | `b8acf26d455607e5b28e30431942c23658eca27841aa64352f326db2430ee08a` | yes |
| `results/topo_profile_F2.csv` | `raw/topo_profile_F2.csv` | `453e298b1168181c63e7c0a0a3fd45770057bf3812b19e30a71026402e465779` | `453e298b1168181c63e7c0a0a3fd45770057bf3812b19e30a71026402e465779` | yes |

Exact reproduction commands: `python -m scripts.p5_omega.topological_mass_radius`
and `python -m scripts.p5_omega.topo_crosscheck`. Generated output goes only
to `regen/`, never to `raw/`.

Inputs use 4-ball cutoff units with `Lambda=1`, `Nc=3`, `Nf=2`,
`N_mult=6`, `c_GW=1`, `kappa_U=-17/(1152 pi^2)`, finite EFT momentum band,
the `eft` regulator, and F1/F2/F3 profile families. Recorded operating point:
`m=0.20`, `g0=20`; scan includes the source-defined ranges. Headline archived
verdict: `MASS/RADIUS GATE FAILS: MINIMUM IS A CUTOFF-SCALE LATTICE LUMP.`

The adapted runtime is documented in `archive/p5-omega-01/ADAPTATION_DIFF.md`.
Its only Paper 3 compatibility dependency is `PiT_single`; ownership remains
with Paper 3. Reviewer record: `reviews/claude/2026-07-16-p5-omega-01.md`.
