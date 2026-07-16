# C2a Results — pinning kappa_U (CHECKPOINT: table + band + gates)

**Target (stated in all outputs):** this is the NON-SINGLET SU(2) orientation /
Skyrme coefficient (pion-direction legs, alternating flavour `(1,2,1,2)`), for
which exact Goldstone-ness makes `A0_total = 0` an exact requirement. It does
**NOT** measure the anomalous `U(1)_A` singlet (eta) sector.

**Config confirmation.** All `k != 0` production points were evaluated through the
unified full-symmetric evaluator `skyrme_fast.py` (validated to machine precision
against the independent matrix evaluator `skyrme_full.py`). The lineage `box()`
is a **regression reference only** and is never mixed into production numbers.
Single routing prescription across all five classes. Fixed seeds, printed configs;
importance sampling `rho(r)~r^3/(r^2+m^2)^4` (Sobol QMC).

## 1. kappa_U(m) table (importance MC, seeds 11/23/47, N=16384)

| m/Λ | kappa_raw | kappa_U = m⁴·kappa_raw | band (kappa_U) | MC | plateau | overdet resid | \|A0\| | O1/O2 cond | L⁶/L⁴ |
|-----|-----------|------------------------|----------------|----|---------|---------------|--------|-----------|-------|
| 0.08 | −36.386 | **−0.001490** | 5e-6 | 0.023 | 0.231 | 5.8e-8 | 2.9e-8 | 4.12 | 0.034 |
| 0.12 | −7.190 | **−0.001491** | 5e-6 | 0.005 | 0.046 | 2.2e-8 | 2.9e-8 | 4.12 | 0.034 |
| 0.15 | −2.945 | **−0.001491** | 5e-6 | 0.002 | 0.019 | 1.5e-8 | 2.9e-8 | 4.12 | 0.034 |
| 0.20 | −0.932 | **−0.001491** | 5e-6 | 0.0004 | 0.006 | 1.2e-8 | 2.9e-8 | 4.12 | 0.034 |
| 0.30 | −0.184 | **−0.001487** | 5e-6 | 0.00001 | 0.001 | 6.6e-9 | 2.9e-8 | 4.12 | 0.034 |

`kappa_raw` scales as `1/m⁴` to the digit (ratios `(1.5)⁴=5.06`, `(1.25)⁴=2.44`
reproduced), so `kappa_U = m⁴ kappa_raw` is **m-independent**.

## 2. Log-law fit  kappa_U(m) = a ln(Λ/m) + b   (Λ=1)

- **a = 0.00000 ± 0.00000**  (slope consistent with zero)
- **b = −0.00149 ± 0.00001**
- χ²/dof = 0.225/3 = **0.075**  → log-law consistency (validity gate): **OK**
- residuals ~1e-6 (kappa_U units)

A flat `kappa_U` (a=0) means the O(p⁴) Skyrme coefficient is UV-finite — the
IR/UV logs of the individual diagram classes cancel in the full chiral set already
at the O(k⁴) coefficient level (Goldstone protection), consistent with the
constituent-quark Skyrme term being finite (Diakonov–Petrov / Ebert–Reinhardt).

## 3. Gates

- **P1 (Ward/m⁴ anchor):** the m⁴ factor `kappa_U = m⁴ kappa_raw` is exact
  (pilot: `m Pi_P(0) = -<psibar psi>`, ratio 1.0000000000). Anchor uncertainty ~0.
- **P4 (chiral completeness A0=0):** PASS — A0_total machine-zero, pointwise-exact
  (`p4_gate_output.txt`); confirmed at production (|A0| ≈ 3e-8, importance & QMC).
- **P6 (routing / regulator):** A0=0 under BOTH routings. kappa_raw asym=−2.9478,
  sym=−2.9335; difference resolved → routing (regulator) systematic on kappa_U =
  **7.2e-6** (0.5%). S_mono sits **141** below the window edge, so the routing
  systematic (0.005 on S) is IMMATERIAL to the verdict. (The decisive tool for a
  load-bearing verdict would be the overlap-lattice derivative expansion; the
  sharp-cutoff MC is a proxy and here the margin is ~150×.) `p6_routing_output.txt`.
- **P7 (analytic slope):** independent DETERMINISTIC QMC evaluator reproduces
  kappa_U=−0.00149. Slopes a1(O1)=−6e-6, a2(O2)=+2e-6, aK(Skyrme)=−4e-6 — every
  O(p⁴) coefficient is m-independent (a≈0). Zero log slope ⟺ the constituent-quark
  Skyrme term is UV-finite (Diakonov–Petrov / Ebert–Reinhardt); the finite value b
  is scheme(cutoff)-dependent, as the pre-registration anticipated. `p7_slope_output.txt`.
- **overdetermination:** O1/O2 design cond 4.12, residual ~1e-8 (two structures
  fully capture the O(k⁴) amplitude).
- **plateau (H1):** kappa_raw stable across e∈{m/6,m/4,m/3}; L⁶/L⁴ ≈ 0.034 (inside
  the derivative-expansion radius, resolving H1).
- **H2 / H3 (root causes):** H2 (missing seagulls) resolved — full class set shifts
  kappa_raw from box-only −0.235 to −0.19 at m=0.30 and, crucially, makes A0=0 so
  the old 1/e⁴ leakage (the 9× spread) is gone. H3 resolved by P1 (m⁴ factor).

## 4. Error budget (stacked, kappa_U at operating point m=0.15)

| source | on kappa_U |
|--------|-----------|
| MC statistical (seeds 11/23/47) | 1.0e-6 |
| plateau spread (H1) | 4.8e-6 |
| overdetermination residual (basis) | ~2e-8 |
| routing/regulator (P6) | 7.2e-6 |
| m⁴ Ward anchor (P1) | ~0 |
| **stacked (quadrature)** | **8.7e-6** |

**kappa_U = −0.00149 ± 0.000009**  (m-independent; operating value = plateau value).

## 5. Kill-criterion arithmetic (pre-registered, verbatim)

> If the pinned kappa_U places `S_mono = 640 · kappa_U (N=3)` outside `[140, 550]`,
> THE DARK-ENERGY CHAIN TERMINATES. Inside the window: proceed to C2b.
> No post-hoc window adjustment.

- `S_mono = 640 · (−0.00149 ± 0.000009) = −0.95 ± 0.006`
- window `[140, 550]`  →  **inside: NO** (S_mono is ~150× below the lower edge, and
  of the wrong sign; the lower edge is 141 units away, dwarfing every systematic).

### Verdict line (verbatim from the pre-registered kill criterion)

> If the pinned kappa_U places S_mono = 640·kappa_U outside [140, 550], THE
> DARK-ENERGY CHAIN TERMINATES.

`S_mono = −0.95 ∉ [140, 550]`: the criterion, as pre-registered by the
dark-energy paper, is **not met by this measurement**. The consequent termination
verdict is recorded and owned by that paper (`paper4_dark_energy_v6_3.tex`, Sec.
"The pre-registered verdict"), not by this repository.

The result is doubly decisive: the magnitude is ~150× too small AND the sign is
negative (the pilot P5 note: a negative kappa_U breaks the induced-Maxwell
construction). This measurement is the input on which the companion paper
retracted its v5.6–5.8 viability-gate claims, and on which this paper retracted its
own positive-kappa entries (S2-1, Gate 3); cross-paper consequences are recorded
in the owning papers.

### Scope / robustness caveat
This is the continuum sharp-cutoff MC proxy (skyrme_sign2 lineage). Every gate
(P1,P4,P6,P7, log-law, overdetermination, plateau) passed, two independent
evaluators (matrix `skyrme_full`, analytic-trace `skyrme_fast`) and two
integrators (pseudo-random MC, deterministic Sobol QMC) agree, and the verdict
holds by ~150× — far outside any residual regulator systematic. Per P6, the
formally decisive tool would be the overlap-lattice derivative expansion, but the
margin here makes the criterion mismatch robust; the companion paper owns the
consequent termination verdict.
