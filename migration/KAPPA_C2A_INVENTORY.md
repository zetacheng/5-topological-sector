# Legacy kappa-c2a Inventory for Paper 5

Date: 2026-07-15

## Scope and method

Source repository: `zetacheng/kappa-c2a`  
Destination repository: `zetacheng/5-topological-sector`  
Destination branch: `sync/kappa-c2a-paper5-migration`

The legacy remote was fetched read-only with branches, tags, and pruning. No legacy history is merged. The legacy repository has no tags. Classification is file-level because the main feature chain mixes Paper 3 and Paper 5. Duplicate inherited files on downstream branches are classified once at their authoritative source ref; branch-exclusive artifacts are listed separately.

Allowed classifications: `PAPER5_AUTHORITATIVE`, `PAPER5_SUPPORTING`, `PAPER3_OWNED`, `PAPER4_OWNED`, `CROSS_PAPER_REFERENCE_ONLY`, `AMBIGUOUS_REQUIRES_REVIEW`, `OBSOLETE_OR_SUPERSEDED`.

## Source refs inspected

- `legacy-kappa/main` at `0f153e84574781230ca9a42aa9993bf7092f9262`
- `legacy-kappa/c2a` at `82b272940976166b547d4a7b6899c895d610e814`
- `legacy-kappa/claude/c2a-kappa-u-skyrme-35v1ap` at `cba89de41183d08c587af5187edfbc8de659df9f`
- `legacy-kappa/c6-gate` at `9515bd6d9d9d4a1a2a66290b97c8ec0ebcf2b71b`
- `legacy-kappa/omega-gate` at `0a58e2c96387b9b0f9c253f6c20ec2833de222ff`
- `legacy-kappa/u3-fierz-gate` at `08d8504949c28825c551f7c201f4f4e50636fcac`
- `legacy-kappa/omega-dynamization` at `d80431b8b01ce1aa5b5a77b8ea66990085503ce8`
- `legacy-kappa/topo-mass-radius` at `6a20b05e0899a878fde214c44cf77a8610d7516f`
- `legacy-kappa/de-interface-wrinkle` at `5ee543c9c7c37082c1053f438aa10a4a65ee7234`
- `legacy-kappa/driven-interface-wrinkle` at `2a80c9db07654c51978891f6bac4a9518ea8a6dd`
- `legacy-kappa/wrinkle-bound-excitation` at `17c187df09966e2a89bb73489d5cdd121ade3f21`
- `legacy-kappa/sea-interface-phase-conversion` at `1cd94b5dde72745006b3fec67b40b227fd8eaacb`
- Tags: none.

## Commit classification

| Source commit | Legacy ref | Scientific subject | Classification | Reason |
|---|---|---|---|---|
| `e4f65785f408ab7e8645c181f692f08503ff718f` | `legacy-kappa/main ancestry` | Lineage imports: Skyrme and Fierz utilities | `CROSS_PAPER_REFERENCE_ONLY` | Mixed commit; Paper 5 Skyrme lineage is supporting, Fierz material is not Paper 5 authority. |
| `037bfd9ec9baf176861052c358e0007bceebe64d` | `legacy-kappa/main ancestry` | Startup regression | `PAPER5_SUPPORTING` | Paper 5 C2a environment regression. |
| `cc7384cd1d276b7ac371e029a50c6dd08fbdfe1f` | `legacy-kappa/main ancestry` | Legacy initial README | `OBSOLETE_OR_SUPERSEDED` | Superseded repository-level metadata. |
| `82b272940976166b547d4a7b6899c895d610e814` | `legacy-kappa/c2a` | C2a derivation framework | `PAPER5_AUTHORITATIVE` | Non-singlet orientation derivative expansion. |
| `eb7908ad3fd4c7519cf1f1be6b71ace5b1565528` | `legacy-kappa/main ancestry` | C2a preregistered specification | `PAPER5_SUPPORTING` | Gate specification and provenance. |
| `168d890334e67a4bbfca4dea5b84e8036a44acfa` | `legacy-kappa/main ancestry` | Five-class weights and symmetry factors | `PAPER5_AUTHORITATIVE` | Core C2a derivation and anchors. |
| `2f9758dcf105c10dcd53a420d95ef4f9bd505765` | `legacy-kappa/main ancestry` | Five-class evaluator and A0 gate | `PAPER5_AUTHORITATIVE` | Chiral-completeness checkpoint. |
| `7d83c667b23c81ca83f2a8255fa69fc9330abd51` | `legacy-kappa/main ancestry` | Legacy ignore rules | `OBSOLETE_OR_SUPERSEDED` | Destination has its own ignore policy. |
| `6167438acbfb16f6d723775fffe67bc40f1fe67c` | `legacy-kappa/main ancestry` | Production C2a scan machinery | `PAPER5_AUTHORITATIVE` | Independent evaluator and production scan. |
| `6210279f22693da6f7f4406509203ad8d495aa88` | `legacy-kappa/main ancestry` | C2a result checkpoint | `PAPER5_AUTHORITATIVE` | Committed C2a tables, gates, and outputs. |
| `f225fe880f1874d4522e61db160551ec468dbe8a` | `legacy-kappa/main ancestry` | Aggregate-table reproduction | `PAPER5_AUTHORITATIVE` | Reproduces committed scan table. |
| `4a0de1e2d6875f0ac27907395b3fc28b6bd7ce25` | `legacy-kappa/main ancestry` | Exact closed-form kappa | `PAPER5_AUTHORITATIVE` | Exact finite-cutoff expression and continuum value. |
| `cba89de41183d08c587af5187edfbc8de659df9f` | `legacy-kappa/claude/c2a-kappa-u-skyrme-35v1ap` | PV sign check | `PAPER5_AUTHORITATIVE` | Independent regulator/sign confirmation. |
| `0ba85e578d438f4f9abcb2a10c501e74acc0b190` | `legacy-kappa/c6-gate` | GW plus C6 matching | `CROSS_PAPER_REFERENCE_ONLY` | Mixed commit: separable c_GW evidence is Paper 5; C6/HS/vector conclusion is Paper 3. |
| `9515bd6d9d9d4a1a2a66290b97c8ec0ebcf2b71b` | `legacy-kappa/c6-gate` | C6 vector verdict | `PAPER3_OWNED` | C6=-G_V/2 and stabilization verdict belong to Paper 3. |
| `c81ebccab734f5ddbe35d3548639977beeb67dd5` | `legacy-kappa/omega-gate` | Omega O1 | `PAPER3_OWNED` | Standalone vector-sector result. |
| `0d57a16cbcb3a4c6738f479e44c021bbf0686220` | `legacy-kappa/omega-gate` | Omega O2 | `PAPER3_OWNED` | RPA/vector interaction result. |
| `0a58e2c96387b9b0f9c253f6c20ec2833de222ff` | `legacy-kappa/omega-gate` | Omega O3 and verdict | `PAPER3_OWNED` | Omega-sector conclusion. |
| `c02d1ff0cbb0a8d721e62da95865307153a31643` | `legacy-kappa/u3-fierz-gate` | U(3) Fierz derivation | `PAPER3_OWNED` | Vector/Fierz ownership. |
| `08d8504949c28825c551f7c201f4f4e50636fcac` | `legacy-kappa/u3-fierz-gate` | U(3) Fierz gate | `PAPER3_OWNED` | G_omega=-G/N result. |
| `73e6effe03e59b2b5a09e2950580676ac64506ed` | `legacy-kappa/omega-dynamization` | Omega dynamization derivation | `PAPER3_OWNED` | Vector pole and static kernel. |
| `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | `legacy-kappa/omega-dynamization` | Omega dynamization artifacts | `PAPER3_OWNED` | Vector production evidence. |
| `0f153e84574781230ca9a42aa9993bf7092f9262` | `legacy-kappa/main` | Mixed feature-chain merge | `OBSOLETE_OR_SUPERSEDED` | Not merged; file-level source commits are used. |
| `b3e5068b94056ec2f731a15d87c11ec46bcdd508` | `legacy-kappa/topo-mass-radius` | Topological mass/radius derivation | `AMBIGUOUS_REQUIRES_REVIEW` | Paper 5 question, but tightly couples Paper 3 omega inputs and Paper 1 DM framing. |
| `6a20b05e0899a878fde214c44cf77a8610d7516f` | `legacy-kappa/topo-mass-radius` | Topological mass/radius results | `AMBIGUOUS_REQUIRES_REVIEW` | Mixed ownership; not migrated pending PI/reviewer split. |
| `e642882128b98990a12dd79cdde9374a849dfb71` | `legacy-kappa/de-interface-wrinkle` | DE-interface wrinkle derivation | `PAPER4_OWNED` | Dark-energy/interface work. |
| `30ed7576a31a30c63960e0d97922c8a7264c9afc` | `legacy-kappa/de-interface-wrinkle` | DE-interface correction | `PAPER4_OWNED` | Dark-energy/interface work. |
| `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | `legacy-kappa/de-interface-wrinkle` | DE-interface artifacts | `PAPER4_OWNED` | Dark-energy/interface work. |
| `a27e5708777076ca6ba67fe58cb1f2bdaf34969c` | `legacy-kappa/driven-interface-wrinkle` | Driven interface derivation | `PAPER4_OWNED` | Dark-energy/interface EFT. |
| `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | `legacy-kappa/driven-interface-wrinkle` | Driven interface artifacts | `PAPER4_OWNED` | Dark-energy/interface EFT. |
| `91ffd7d15890579f2f4c0982a5dc296146b8787e` | `legacy-kappa/wrinkle-bound-excitation` | Wrinkle-bound derivation | `AMBIGUOUS_REQUIRES_REVIEW` | Mixed Paper 4 interface and Paper 1 DM/excitation framing. |
| `17c187df09966e2a89bb73489d5cdd121ade3f21` | `legacy-kappa/wrinkle-bound-excitation` | Wrinkle-bound artifacts | `AMBIGUOUS_REQUIRES_REVIEW` | Mixed ownership; excluded. |
| `96cd1c4a41bec61138b4f9801b861157982c1d96` | `legacy-kappa/sea-interface-phase-conversion` | Sea-interface derivation | `PAPER4_OWNED` | Dark-energy/interface and black-hole consequences. |
| `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | `legacy-kappa/sea-interface-phase-conversion` | Sea-interface artifacts | `PAPER4_OWNED` | Dark-energy/interface production work. |

## Candidate file classification

| Legacy path | Legacy ref | Source commit | Scientific subject | Classification | Destination path | Inclusion or exclusion reason |
|---|---|---|---|---|---|---|
| `derivation/diagram_classes.md` | `legacy-kappa/main` | `2f9758dcf105c10dcd53a420d95ef4f9bd505765` | Five-class non-singlet derivative expansion | `PAPER5_AUTHORITATIVE` | `derivations/c2a/diagram_classes.md` | Copy byte-for-byte. |
| `docs/C2a_spec.md` | `legacy-kappa/main` | `eb7908ad3fd4c7519cf1f1be6b71ace5b1565528` | Preregistered C2a gate specification | `PAPER5_SUPPORTING` | `derivations/c2a/legacy_spec.md` | Copy byte-for-byte. |
| `derive_classes.py` | `legacy-kappa/main` | `168d890334e67a4bbfca4dea5b84e8036a44acfa` | Flavor weights and symmetry factors | `PAPER5_AUTHORITATIVE` | `scripts/c2a/derive_classes.py` | Copy byte-for-byte. |
| `derive_classes_output.txt` | `legacy-kappa/main` | `168d890334e67a4bbfca4dea5b84e8036a44acfa` | Per-class symbolic anchors | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/derive_classes_output.txt` | Copy byte-for-byte. |
| `p4_gate.py` | `legacy-kappa/main` | `2f9758dcf105c10dcd53a420d95ef4f9bd505765` | Pointwise A0 cancellation gate | `PAPER5_AUTHORITATIVE` | `scripts/c2a/p4_gate.py` | Copy with package-relative import transformation. |
| `p4_gate_output.txt` | `legacy-kappa/main` | `2f9758dcf105c10dcd53a420d95ef4f9bd505765` | A0 gate output | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/p4_gate_output.txt` | Copy byte-for-byte. |
| `skyrme_full.py` | `legacy-kappa/main` | `2f9758dcf105c10dcd53a420d95ef4f9bd505765` | Independent matrix evaluator | `PAPER5_AUTHORITATIVE` | `scripts/c2a/skyrme_full.py` | Copy with local gamma-module import transformation. |
| `skyrme_fast.py` | `legacy-kappa/main` | `6167438acbfb16f6d723775fffe67bc40f1fe67c` | Independent analytic-trace evaluator | `PAPER5_AUTHORITATIVE` | `scripts/c2a/skyrme_fast.py` | Copy byte-for-byte. |
| `production_scan.py` | `legacy-kappa/main` | `6167438acbfb16f6d723775fffe67bc40f1fe67c` | Production coefficient scan | `PAPER5_AUTHORITATIVE` | `scripts/c2a/production_scan.py` | Copy with package-relative import transformation. |
| `p6_check.py` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | Routing/regulator check | `PAPER5_AUTHORITATIVE` | `scripts/c2a/p6_check.py` | Copy with package-relative imports. |
| `p7_slope.py` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | Slope anchor | `PAPER5_AUTHORITATIVE` | `scripts/c2a/p7_slope.py` | Copy with package-relative imports. |
| `aggregate.py` | `legacy-kappa/main` | `f225fe880f1874d4522e61db160551ec468dbe8a` | Aggregate-table reproduction | `PAPER5_AUTHORITATIVE` | `scripts/c2a/aggregate.py` | Path-only transformation for destination result data. |
| `derive_kappa_closed.py` | `legacy-kappa/main` | `cba89de41183d08c587af5187edfbc8de659df9f` | Exact finite-cutoff coefficient | `PAPER5_AUTHORITATIVE` | `scripts/c2a/derive_kappa_closed.py` | Copy with package-relative imports. |
| `pv_check.py` | `legacy-kappa/main` | `cba89de41183d08c587af5187edfbc8de659df9f` | PV regulator/sign check | `PAPER5_AUTHORITATIVE` | `scripts/c2a/pv_check.py` | Copy with package-relative imports. |
| `startup_regression.py` | `legacy-kappa/main` | `037bfd9ec9baf176861052c358e0007bceebe64d` | Legacy startup anchors | `PAPER5_SUPPORTING` | `scripts/c2a/startup_regression.py` | Copy with local gamma-module import transformation. |
| `skyrme_sign2.py` | `legacy-kappa/main` | `e4f65785f408ab7e8645c181f692f08503ff718f` | Box-only lineage evaluator | `PAPER5_SUPPORTING` | `scripts/c2a/skyrme_sign2.py` | Copy with local gamma-module import transformation; explicitly non-authoritative lineage. |
| `fierz_verify.py` | `legacy-kappa/main` | `e4f65785f408ab7e8645c181f692f08503ff718f` | Gamma utilities plus Fierz analysis | `CROSS_PAPER_REFERENCE_ONLY` | — | Not copied as-is; only Euclidean gamma definitions are extracted into a Paper 5 utility. |
| `results/RESULTS_C2a.md` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | C2a verdict and error budget | `PAPER5_AUTHORITATIVE` | `results/c2a/processed/RESULTS_C2a.md` | Copy byte-for-byte; Paper 4 consequences remain historical context, not Paper 5 authority. |
| `results/TaskA_closed_form.md` | `legacy-kappa/main` | `cba89de41183d08c587af5187edfbc8de659df9f` | Exact closed-form derivation record | `PAPER5_AUTHORITATIVE` | `derivations/c2a/exact_kappa_derivation.md` | Copy byte-for-byte. |
| `results/TaskB_PV_signcheck.md` | `legacy-kappa/main` | `cba89de41183d08c587af5187edfbc8de659df9f` | PV sign record | `PAPER5_AUTHORITATIVE` | `results/c2a/processed/TaskB_PV_signcheck.md` | Copy byte-for-byte. |
| `results/scan_data.csv` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | Production scan table | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/scan_data.csv` | Copy byte-for-byte. |
| `results/aggregate_output.txt` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | Committed aggregate table | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/aggregate_output.txt` | Copy byte-for-byte. |
| `results/p6_routing_output.txt` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | Routing output | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/p6_routing_output.txt` | Copy byte-for-byte. |
| `results/p7_slope_output.txt` | `legacy-kappa/main` | `6210279f22693da6f7f4406509203ad8d495aa88` | Slope output | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/p7_slope_output.txt` | Copy byte-for-byte. |
| `results/closed_form_output.txt` | `legacy-kappa/main` | `4a0de1e2d6875f0ac27907395b3fc28b6bd7ce25` | Exact coefficient output | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/closed_form_output.txt` | Copy byte-for-byte. |
| `results/lambda_scan_output.txt` | `legacy-kappa/main` | `cba89de41183d08c587af5187edfbc8de659df9f` | Cutoff scan | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/lambda_scan_output.txt` | Copy byte-for-byte. |
| `results/pv_signcheck_output.txt` | `legacy-kappa/main` | `cba89de41183d08c587af5187edfbc8de659df9f` | PV output | `PAPER5_AUTHORITATIVE` | `results/c2a/raw/pv_signcheck_output.txt` | Copy byte-for-byte. |
| `derivation/c6_matching.md` | `legacy-kappa/main` | `0ba85e578d438f4f9abcb2a10c501e74acc0b190` | GW normalization plus Paper 3 C6 matching | `PAPER5_SUPPORTING` | `derivations/goldstone-wilczek/derivation.md` | Transform: extract only GW Step 1; omit signature-dependent static-energy bookkeeping, C6, HS, Walecka, and vector verdict. |
| `scripts/c_gw_loop.py` | `legacy-kappa/main` | `0ba85e578d438f4f9abcb2a10c501e74acc0b190` | Goldstone-Wilczek loop normalization | `PAPER5_AUTHORITATIVE` | `scripts/goldstone_wilczek/c_gw_loop.py` | Transform only gamma import to Paper 5 utility; physics logic unchanged. |
| `results/c_gw_output.txt` | `legacy-kappa/main` | `0ba85e578d438f4f9abcb2a10c501e74acc0b190` | GW cutoff/mass/extrapolation output | `PAPER5_AUTHORITATIVE` | `results/goldstone-wilczek/raw/c_gw_output.txt` | Copy byte-for-byte. |
| `scripts/c6_gate.py` | `legacy-kappa/main` | `0ba85e578d438f4f9abcb2a10c501e74acc0b190` | C6/HS bookkeeping | `PAPER3_OWNED` | — | Excluded. |
| `results/c6_bookkeeping_output.txt` | `legacy-kappa/main` | `0ba85e578d438f4f9abcb2a10c501e74acc0b190` | C6 bookkeeping output | `PAPER3_OWNED` | — | Excluded. |
| `results/c6_verdict.txt` | `legacy-kappa/main` | `9515bd6d9d9d4a1a2a66290b97c8ec0ebcf2b71b` | Paper 3 C6 sign verdict | `PAPER3_OWNED` | — | Excluded. |
| `derivation/omega_gates.md` | `legacy-kappa/main` | `0a58e2c96387b9b0f9c253f6c20ec2833de222ff` | Omega gates | `PAPER3_OWNED` | — | Excluded. |
| `scripts/omega_gates.py` | `legacy-kappa/main` | `0a58e2c96387b9b0f9c253f6c20ec2833de222ff` | Omega gate implementation | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_O1_output.txt` | `legacy-kappa/main` | `c81ebccab734f5ddbe35d3548639977beeb67dd5` | Omega O1 | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_O2_output.txt` | `legacy-kappa/main` | `0d57a16cbcb3a4c6738f479e44c021bbf0686220` | Omega O2 | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_O3_output.txt` | `legacy-kappa/main` | `0a58e2c96387b9b0f9c253f6c20ec2833de222ff` | Omega O3 | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_verdict.txt` | `legacy-kappa/main` | `0a58e2c96387b9b0f9c253f6c20ec2833de222ff` | Omega verdict | `PAPER3_OWNED` | — | Excluded. |
| `derivation/u3_fierz.md` | `legacy-kappa/main` | `c02d1ff0cbb0a8d721e62da95865307153a31643` | U(3) Fierz derivation | `PAPER3_OWNED` | — | Excluded. |
| `scripts/u3_fierz_gate.py` | `legacy-kappa/main` | `08d8504949c28825c551f7c201f4f4e50636fcac` | U(3) Fierz implementation | `PAPER3_OWNED` | — | Excluded. |
| `results/u3_fierz_output.txt` | `legacy-kappa/main` | `08d8504949c28825c551f7c201f4f4e50636fcac` | U(3) Fierz output | `PAPER3_OWNED` | — | Excluded. |
| `results/u3_fierz_verdict.txt` | `legacy-kappa/main` | `08d8504949c28825c551f7c201f4f4e50636fcac` | U(3) Fierz verdict | `PAPER3_OWNED` | — | Excluded. |
| `derivation/omega_dynamization.md` | `legacy-kappa/main` | `73e6effe03e59b2b5a09e2950580676ac64506ed` | Omega dynamization | `PAPER3_OWNED` | — | Excluded. |
| `scripts/omega_dynamization.py` | `legacy-kappa/main` | `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | Omega dynamization code | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_dyn_D00.csv` | `legacy-kappa/main` | `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | Omega propagator data | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_dyn_Zomega.csv` | `legacy-kappa/main` | `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | Omega residue data | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_dyn_energy.csv` | `legacy-kappa/main` | `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | Omega energy data | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_dyn_output.txt` | `legacy-kappa/main` | `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | Omega output | `PAPER3_OWNED` | — | Excluded. |
| `results/omega_dyn_verdict.txt` | `legacy-kappa/main` | `d80431b8b01ce1aa5b5a77b8ea66990085503ce8` | Omega verdict | `PAPER3_OWNED` | — | Excluded. |
| `README.md` | `legacy-kappa/main` | `037bfd9ec9baf176861052c358e0007bceebe64d` | Mixed legacy repository overview | `OBSOLETE_OR_SUPERSEDED` | — | Destination README governs Paper 5. |
| `.gitignore` | `legacy-kappa/main` | `7d83c667b23c81ca83f2a8255fa69fc9330abd51` | Legacy ignore policy | `OBSOLETE_OR_SUPERSEDED` | — | Destination policy retained. |
| `derivation/topological_mass_radius.md` | `legacy-kappa/topo-mass-radius` | `b3e5068b94056ec2f731a15d87c11ec46bcdd508` | Topological-object construction with omega/DM coupling | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `scripts/topological_mass_radius.py` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology/omega solver | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `scripts/topo_crosscheck.py` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology/omega cross-check | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `results/topo_ER_curve.csv` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology energy data | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `results/topo_crosscheck_output.txt` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology cross-check | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `results/topo_output.txt` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology raw output | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `results/topo_profile_F2.csv` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology profile | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `results/topo_scan.csv` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology scan | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `results/topo_verdict.txt` | `legacy-kappa/topo-mass-radius` | `6a20b05e0899a878fde214c44cf77a8610d7516f` | Mixed topology/DM verdict | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded pending a clean split of Paper 5 topology from Paper 3 omega and Paper 1 DM framing. |
| `derivation/de_interface_wrinkle.md` | `legacy-kappa/de-interface-wrinkle` | `30ed7576a31a30c63960e0d97922c8a7264c9afc` | de interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `scripts/de_interface_wrinkle.py` | `legacy-kappa/de-interface-wrinkle` | `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | de interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/dewrinkle_kernel.csv` | `legacy-kappa/de-interface-wrinkle` | `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | de interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/dewrinkle_output.txt` | `legacy-kappa/de-interface-wrinkle` | `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | de interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/dewrinkle_sigma.csv` | `legacy-kappa/de-interface-wrinkle` | `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | de interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/dewrinkle_verdict.txt` | `legacy-kappa/de-interface-wrinkle` | `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | de interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `derivation/driven_interface_wrinkle.md` | `legacy-kappa/driven-interface-wrinkle` | `a27e5708777076ca6ba67fe58cb1f2bdaf34969c` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `scripts/driven_interface_wrinkle.py` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `scripts/driven_wrinkle_2d.py` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_2d_output.txt` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_dispersion.csv` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_output.txt` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_phase_diagram.csv` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_profile.csv` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_verdict.txt` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `results/driven_wrinkle_2d_field.csv` | `legacy-kappa/driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | driven interface wrinkle | `PAPER4_OWNED` | — | Excluded. |
| `derivation/sea_interface_phase_conversion.md` | `legacy-kappa/sea-interface-phase-conversion` | `96cd1c4a41bec61138b4f9801b861157982c1d96` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `scripts/sea_bh_core.py` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `scripts/sea_interface.py` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `results/sea_bh_core.csv` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `results/sea_bh_output.txt` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `results/sea_interface_output.txt` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `results/sea_interface_verdict.txt` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `results/sea_reverse_transition.csv` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `results/sea_wall_profile.csv` | `legacy-kappa/sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | sea interface phase conversion | `PAPER4_OWNED` | — | Excluded. |
| `derivation/wrinkle_bound_excitation.md` | `legacy-kappa/wrinkle-bound-excitation` | `91ffd7d15890579f2f4c0982a5dc296146b8787e` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |
| `scripts/wrinkle_bound_excitation.py` | `legacy-kappa/wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |
| `results/wrinkle_bound_eigen.csv` | `legacy-kappa/wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |
| `results/wrinkle_bound_output.txt` | `legacy-kappa/wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |
| `results/wrinkle_bound_profile.csv` | `legacy-kappa/wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |
| `results/wrinkle_bound_verdict.txt` | `legacy-kappa/wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |
| `results/wrinkle_threshold.csv` | `legacy-kappa/wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | wrinkle bound excitation | `AMBIGUOUS_REQUIRES_REVIEW` | — | Excluded. |

## Ownership summary

- Paper 5 authoritative: the C2a five-class derivation, exact coefficient, regulator checks, production tables, and the independently separable Goldstone-Wilczek loop/output.
- Paper 5 supporting: preregistration, startup/lineage checks, and the GW subsection extracted from the mixed C6 note.
- Paper 3 owned: U(3) Fierz, omega gates/dynamization, vector/RPA results, C6 matching, and the sign/stabilization verdict based on `G_V`.
- Paper 4 owned: dark-energy/interface, phase-conversion, and cosmological/black-hole consequences.
- Ambiguous: the topological mass/radius and wrinkle-bound branches because they combine Paper 5 questions with Paper 3 or Paper 1 assumptions and framing.
- Obsolete/superseded: legacy repository metadata, ignore policy, and the mixed merge commit as a migration source.

## Import lock

Only rows with a Paper 5 classification and an explicit destination may be imported in this migration. Ambiguous rows remain excluded until PI and independent reviewer classification. Paper 3/4/1 artifacts are referenced by SHA only and are not copied into Paper 5 production directories.
