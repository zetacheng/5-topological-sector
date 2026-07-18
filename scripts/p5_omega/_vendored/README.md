# Vendored runtime compatibility

Scientific owner: `zetacheng/3-vector-sector`. Destination use is runtime
compatibility for P5-OMEGA-01 only; this is not a Paper 5-owned derivation and
does not transfer scientific ownership.

Source: Paper 3 `main` at `0cb95fe7052a675708999d44f66084e446a3d0bf`,
`scripts/omega_dynamization.py` (whole-file SHA-256
`ca49145c931b42b9a456905beda71f42301d0200b8f08f6b63a79480c589cde4`).
`pit.py` contains only `PiT_single`, copied verbatim in computational content.
The legacy gate used the same named dependency. The Paper 3 `c6_gate.py`
Walecka sign assertion is deliberately not copied: its accepted result is an
upstream input, not runtime numerical functionality.

Upstream accepted scope: the Fierz, omega-health, and repulsive-kernel gates.
Paper 5 uses their accepted kernel only to test continuum stabilization.
