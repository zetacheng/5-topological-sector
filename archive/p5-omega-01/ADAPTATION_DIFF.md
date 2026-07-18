# P5-OMEGA-01 adaptation diff

Source: `zetacheng/kappa-c2a@6a20b05e0899a878fde214c44cf77a8610d7516f`.

## `topological_mass_radius.py`

- Removed legacy `sys.path` manipulation and imported `PiT_single` through
  the package-relative `._vendored.pit` module.
- Removed the legacy import-time `walecka_regression()` assertion. That is an
  accepted Paper 3 sign anchor, recorded as an upstream input rather than
  duplicated as a Paper 5 derivation.
- Replaced the legacy `results/` output location with
  `results/p5-omega-01/regen/`, created only when `main()` runs. Immutable
  raw evidence is never opened for writing.
- Replaced `os.path.join` output construction with `pathlib.Path`.

No formula, grid, constant, regulator, profile family, operating point, or
numerical method was changed.

## `topo_crosscheck.py`

- Removed legacy `sys.path` manipulation.
- Replaced the legacy Paper 3 import with package-relative
  `._vendored.pit.PiT_single`.

No scientific computation was changed.
