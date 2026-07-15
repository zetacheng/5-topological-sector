# Task A — closed-form analytic kappa_U (definitive check)

Derivation in `derive_kappa_closed.py` (sympy). The five-class amplitude is
Taylor-expanded to O(k^4) at k->0; Dirac traces reduced to scalar via the
validated analytic-trace tensors C (skyrme_fast); reduced to elementary 4D
radial integrals `Int_0^1 r^K/(r^2+m^2)^M dr` (sharp ball Lambda=1, matching the
production regulator) and evaluated exactly. Every reduction step was verified
numerically against the existing evaluators before use:

- monomial ball integrals vs MC: rel <= 1e-3 (self-check);
- the symbolic O(k^4) integrand vs a finite-difference of skyrme_fast's density,
  per class at a fixed p: BOX/TRIANGLE/SUNSET all match to <1% (finite-difference
  limited).

## Result (exact, ball Lambda=1)

    kappa_U(m) = -(90 m^6 + 170 m^4 + 85 m^2 + 17) / (1152 pi^2 (m^2+1)^5)

Per-class A4 (config theta=90): BUBBLE = CONTACT = 0; the Skyrme coefficient comes
entirely from BOX + TRIANGLE + SUNSET.

## m-independence (the correctness gate) — shown explicitly

Small-m expansion:

    kappa_U(m) = -17/(1152 pi^2)  +  (5/72 pi^2) m^6  +  ...

The m^2 and m^4 terms CANCEL exactly (numerator coefficients -85 = -17*5 and
-170 = -17*10 match the (m^2+1)^5 expansion 5, 10). The residual is O(m^6): a
finite-cutoff (m^2/Lambda^2) artifact, which the production scan also exhibits
(both show the same weak decrease in magnitude with m). d(kappa_U)/dm =
5 m^5 (3 m^2 + 4) / (48 pi^2 (m^2+1)^6) -> 0 as m/Lambda -> 0.

## The exact number and sign

    kappa_U = -17 / (1152 pi^2)  =  -(17/36) * 1/(32 pi^2)  =  -0.00149519

- rational multiple of 1/pi^2: **-17/1152** (equivalently -17/36 in units of 1/32pi^2);
- **SIGN: NEGATIVE**, read off analytically (all numerator coefficients negative,
  denominator positive-definite).

## Agreement with production

| m | closed-form kappa_U | production | deviation |
|---|---|---|---|
| 0.08 | -0.0014952 | -0.0014900 | 0.35% |
| 0.12 | -0.0014952 | -0.0014910 | 0.28% |
| 0.15 | -0.0014951 | -0.0014910 | 0.28% |
| 0.20 | -0.0014948 | -0.0014910 | 0.26% |
| 0.30 | -0.0014915 | -0.0014870 | 0.30% |

Deviation 0.26-0.35% < the stacked band (0.6%). The closed form is the EXACT
ball-Lambda=1 value; the production importance-QMC (N=16384) approaches it. The
measured kappa_U is thus confirmed to be an exact pure number.

## Cutoff (Lambda) independence — exact

Keeping the ball radius Lambda general (`derive_kappa_closed.py`, `BALL_R`):

    kappa_U(m, Lambda) = Lambda^4 (-17 Lambda^6 - 85 Lambda^4 m^2 - 170 Lambda^2 m^4
                                   - 90 m^6) / (1152 pi^2 (Lambda^2 + m^2)^5)

    kappa_U(m -> 0, Lambda) = -17/(1152 pi^2)   for ALL Lambda.

So the pure number is not only m-independent but exactly Lambda- (cutoff-)
independent: sharp ball at any radius, and the R^4 (cutoff-removed) limit, all
give -17/(1152 pi^2). This underwrites the Task B regulator-independence result.

## Kill-criterion arithmetic (exact)

    S_mono = 640 * kappa_U = 640 * (-17/(1152 pi^2)) = -85/(9 pi^2) = -0.9570

Outside [140, 550], negative. The dark-energy-chain TERMINATE verdict is confirmed
in closed form, independent of Monte Carlo.
