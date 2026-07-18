# Regeneration comparison

The destination-adapted solver was run in the recorded Windows `.venv`.
Comparison against immutable legacy CSVs used the same grids and deterministic
formulae:

| File | Maximum absolute difference | Acceptance tolerance |
|---|---:|---:|
| `topo_scan.csv` | `2.22e-16` | `1e-12` |
| `topo_ER_curve.csv` | `8.88e-16` | `1e-12` |
| `topo_profile_F2.csv` | `4.44e-16` | `1e-12` |

The source's q-grid convergence anchor at `nq=1500,3000,6000` gives the same
displayed `E_omega=0.05945`; the finer `nq=6000` value is used as the
convergence check. Integrated comparisons therefore use `1e-12` only for the
deterministic archived regeneration and use looser, source-supported tolerances
for the independent coordinate/direct-quadrature crosscheck.
