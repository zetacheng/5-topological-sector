# P5-OMEGA-01 provenance

Owning gate: `P5-OMEGA-01`. Legacy source: `zetacheng/kappa-c2a` at pinned
commit `6a20b05e0899a878fde214c44cf77a8610d7516f` (not a moving branch).

## Source and immutable raw inventory

The three `.txt` files are byte-identical Git blobs. The three CSVs are
content-identical but were normalized from legacy CRLF to LF in the
destination Git blob. Their worktree representation may be CRLF under the
local checkout policy; the checks below are Git-object bytes.

| Source path | Destination path | Legacy blob SHA-256 | Destination blob SHA-256 | Identity |
|---|---|---|---|---|
| `results/topo_verdict.txt` | `raw/topo_verdict.txt` | `abe439134428395eeba883c9e0b278e8da2224de5e7d214b2fcd00c565e56dae` | `abe439134428395eeba883c9e0b278e8da2224de5e7d214b2fcd00c565e56dae` | byte-identical |
| `results/topo_output.txt` | `raw/topo_output.txt` | `46464138a941059948485f58c52f6686d902e5dad3ad31b511fc36fd3e5530fb` | `46464138a941059948485f58c52f6686d902e5dad3ad31b511fc36fd3e5530fb` | byte-identical |
| `results/topo_crosscheck_output.txt` | `raw/topo_crosscheck_output.txt` | `dcbec9d415dd06a836a0d8b2adcadcbcb74bab844349eac318c986097535ad38` | `dcbec9d415dd06a836a0d8b2adcadcbcb74bab844349eac318c986097535ad38` | byte-identical |
| `results/topo_scan.csv` | `raw/topo_scan.csv` | `1739047563decdd05cca7b5c9cc1f0120b664ef2a8622f90f429510ba6f0977e` | `990b1bf08deeb2afabea281aa8da5efcfe394dd3eb6aa7668764c26e33b03d40` | CRLF-to-LF normalized; content-identical |
| `results/topo_ER_curve.csv` | `raw/topo_ER_curve.csv` | `b8acf26d455607e5b28e30431942c23658eca27841aa64352f326db2430ee08a` | `f0dafbaf337ecab17eca97af944cc1170ee6017d4f20f14e8344e8221d996eb0` | CRLF-to-LF normalized; content-identical |
| `results/topo_profile_F2.csv` | `raw/topo_profile_F2.csv` | `453e298b1168181c63e7c0a0a3fd45770057bf3812b19e30a71026402e465779` | `b8e1407a60e1df86bd427ed1066fd04c5256956759ed343a7115383830c7fea3` | CRLF-to-LF normalized; content-identical |

For the CSV rows, SHA-256 after CRLF-to-LF normalization is respectively
`990b1bf08deeb2afabea281aa8da5efcfe394dd3eb6aa7668764c26e33b03d40`,
`f0dafbaf337ecab17eca97af944cc1170ee6017d4f20f14e8344e8221d996eb0`, and
`b8e1407a60e1df86bd427ed1066fd04c5256956759ed343a7115383830c7fea3` for
both source and destination.

Exact reproduction commands: `python -m scripts.p5_omega.topological_mass_radius`
and `python -m scripts.p5_omega.topo_crosscheck`. Generated output goes only
to `regen/`, never to `raw/`.

Regeneration comparison uses parsed CSV values, not raw byte equality; see
`processed/regeneration_comparison.md`. It is therefore not platform-dependent.

Inputs use 4-ball cutoff units with `Lambda=1`, `Nc=3`, `Nf=2`,
`N_mult=6`, `c_GW=1`, `kappa_U=-17/(1152 pi^2)`, finite EFT momentum band,
the `eft` regulator, and F1/F2/F3 profile families. Recorded operating point:
`m=0.20`, `g0=20`; scan includes the source-defined ranges. Headline archived
verdict: `MASS/RADIUS GATE FAILS: MINIMUM IS A CUTOFF-SCALE LATTICE LUMP.`

The adapted runtime is documented in `archive/p5-omega-01/ADAPTATION_DIFF.md`.
Its only Paper 3 compatibility dependency is `PiT_single`; ownership remains
with Paper 3. Reviewer record: `reviews/claude/2026-07-16-p5-omega-01.md`.
