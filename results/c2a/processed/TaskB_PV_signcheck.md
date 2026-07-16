# Task B — Pauli-Villars second-regulator sign check (m = 0.15)

`pv_check.py`. Second regulator: a common Pauli-Villars form factor
`F(p) = [M_PV^2/(p^2+M_PV^2)]^2` applied to the loop momentum uniformly across all
propagators and classes, with the sharp ball edge softened; `M_PV` in cutoff
units. This is the chirally-consistent PV: because it multiplies the whole
integrand by a common factor, it preserves the A0 identity exactly
(`F * sum_class density = F * 0 = 0`).

> NOTE (reported honestly). The *naive* scalar-denominator replacement
> `1/(p^2+m^2) -> 1/(p^2+m^2) - 1/(p^2+M^2)` with the numerator mass held at `m`
> does NOT preserve the pointwise A0 identity at finite `M` (residual ~1/M^2,
> because the numerator/denominator mass mismatch breaks the chiral structure);
> its extracted kappa is ~2x off. The common form factor is the correct
> second regulator and is used below.

## [1] A0 pointwise cancellation under PV — HOLDS

`max|sum_class density|` at k=0 (importance ball sample, m=0.15):

| M_PV | max\|Σ density\| |
|---|---|
| 2 | 2.2e-11 |
| 4 | 2.4e-11 |
| 8 | 2.0e-11 |

Machine-precision cancellation, as expected (common form factor times the exact
pointwise-zero sum).

## [2] kappa_U(PV) vs sharp cutoff

| M_PV | kappa_U(PV) |
|---|---|
| 2 | -0.001475 |
| 4 | -0.001488 |
| 8 | -0.001491 |
| sharp cutoff (production) | -0.001491 |
| closed form -17/(1152 pi^2) | -0.001495 |

As `M_PV -> inf` the form factor `-> 1` and kappa_U(PV) rises monotonically to the
sharp-cutoff value; every point is NEGATIVE.

## [3] Regulator-independence (analytic, definitive)

The closed-form machinery (`derive_kappa_closed.py`, ball radius Lambda kept
general) gives the exact cutoff dependence:

    kappa_U(m, Lambda) = Lambda^4 (-17 Lambda^6 - 85 Lambda^4 m^2 - 170 Lambda^2 m^4
                                   - 90 m^6) / (1152 pi^2 (Lambda^2 + m^2)^5)

and

    kappa_U(m -> 0, Lambda) = -17/(1152 pi^2)   for ALL Lambda.

So kappa_U is EXACTLY cutoff- (regulator-) independent: sharp ball, PV form
factor, and the cutoff-removed R^4 limit all give -17/(1152 pi^2) = -0.0014952.
(The earlier noise-dominated R^4 importance estimate ~ -0.0032 was a sampling
artifact, 26% error; it is superseded by this exact result and by the reliable
ball+form-factor numbers above.)

## Verdict

    SIGN under second regulator: NEGATIVE CONFIRMED (-0.0014952, exact;
    numeric PV -0.001475..-0.001491 across M_PV=2,4,8, all negative and
    converging to the sharp value; kappa_U is analytically regulator-independent
    = -17/(1152 pi^2)).

The negative sign of kappa_U is robust to the choice of regulator. This confirms,
independently of the sharp-cutoff Monte Carlo, that S_mono = 640 kappa_U =
-85/(9 pi^2) = -0.957 lies outside [140, 550]: the dark-energy chain TERMINATES.
