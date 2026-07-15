# C2a — symbolic derivation of the five diagram classes

**Target (state in all outputs):** this measures the NON-SINGLET SU(2)
orientation / Skyrme coefficient (pion-direction legs, alternating flavour). Exact
Goldstone-ness makes `A0_total = 0` an EXACT requirement once the full set is
included. It does NOT measure the anomalous U(1)_A singlet (eta) sector.

Status of this note: framework, vertex structure, zero-momentum Dirac reductions,
and the BOX + CONTACT prefactors are derived and machine-verified below. The
TRIANGLE/BUBBLE/SUNSET flavour weights + symmetry factors follow the same scheme
and are completed before the MC of those classes is coded (P4 is the machine test).

## 1. Framework

Integrate out the constituent fermion with mass term `M(x) = m exp(i γ5 θ)`,
`θ = τ·π/f`. The pion effective action is
`W = −Tr ln(∂̸+m+ΔM) = const − Tr ln(1 + S ΔM)`,
`S = (∂̸+m)^{-1}`, `ΔM = m(iγ5θ − θ²/2 − iγ5θ³/6 + θ⁴/24 + …)`.
Expanding `−Tr ln(1+SΔM) = Σ_n [(−1)^n/n] Tr[(SΔM)^n]`, the 4-π part collects all
vertex compositions with four external θ's on one fermion loop.

## 2. Vertices (Dirac ⊗ flavour) — rider-#2 identities MACHINE-VERIFIED

Using `(τ·π)² = π² 𝟙` (the ε-term `i ε_abc π_a π_b τ_c` vanishes, antisym×sym):

| vertex | expression | Dirac | flavour (external legs) | m |
|---|---|---|---|---|
| V1 | `i m γ5 θ` | γ5 | `τ·π`  (1 leg, triplet) | m¹ |
| V2 | `−(m/2) π²` | 𝟙 | `π²` = δ-pair (2 legs, **singlet**) | m¹ |
| V3 | `−(i m/6) γ5 π²(τ·π)` | γ5 | δ-pair + `τ` leg (3 legs) | m¹ |
| V4 | `+(m/24) (π²)²` | 𝟙 | two δ-pairs (4 legs, **singlet**) | m¹ |

Verified: `(τ·π)²=π²𝟙`, `(τ·π)³=π²(τ·π)`, `(τ·π)⁴=(π²)²𝟙`.

## 3. Diagram classes (leg partition of the 4 external π's; #props = #vertices)

| class | vertices | props | Dirac vertex seq | m-power |
|---|---|---|---|---|
| BOX | (V1,V1,V1,V1) | 4 | γ5,γ5,γ5,γ5 | m⁴ |
| TRIANGLE | (V1,V1,V2) | 3 | γ5,γ5,𝟙 | m³ |
| BUBBLE | (V2,V2) | 2 | 𝟙,𝟙 | m² |
| SUNSET | (V1,V3) | 2 | γ5,γ5 | m² |
| CONTACT | (V4) | 1 | 𝟙 | m¹ |

All classes with ≥2 propagators contribute at O(k⁴); omitting them is H2. Their
different m-powers are physical — the loop `∫d⁴p S^n ~ [mass]^{4−n}` compensates,
so every class's A0 ~ [mass]⁴ and they can cancel. (Hence the common `1/f⁴` and the
per-class `m^n` must both be kept; one may NOT pull out a uniform `m⁴`.)

## 4. Zero-external-momentum Dirac reductions — MACHINE-VERIFIED

At `k→0` all propagators equal `S(p)=(−ip̸+m)/(p²+m²)`; the Dirac trace collapses
(`γ5 S γ5 = (ip̸+m)/(p²+m²)`, so `γ5Sγ5·S = 1/(p²+m²)`):

| class | `Tr_Dirac` at k=0 | verified |
|---|---|---|
| BOX  `Tr[(γ5S)⁴]` | `4/(p²+m²)²` | ✓ (max err 2e-13) |
| TRIANGLE `Tr[γ5Sγ5S·𝟙S]` | `4m/(p²+m²)²` | ✓ |
| BUBBLE `Tr[S²]` | `4(m²−p²)/(p²+m²)²` | ✓ |
| SUNSET `Tr[(γ5S)²]` | `4/(p²+m²)` | ✓ |
| CONTACT `Tr[S]` | `4m/(p²+m²)` | ✓ |

## 5. Flavour weights

External non-singlet assignment (matching the lineage box): legs `(0,1,2,3)`
carry `(τ¹,τ²,τ¹,τ²)`. Flavour weight of a loop ordering = `Tr_f[` product of the
leg τ's in loop order `]`, with V2/V4/V3 δ-pairs enforcing same-flavour partners.

**BOX (anchor) — MACHINE-VERIFIED:** the three inequivalent necklaces give
`Tr_f[τ¹τ²τ¹τ²]=−2`, `Tr_f[τ¹τ²τ²τ¹]=+2`, `Tr_f[τ¹τ¹τ²τ²]=+2` — exactly the
lineage `(−2,+2,+2)`. Uses `Tr[τ^aτ^bτ^cτ^d]=2(δ_abδ_cd−δ_acδ_bd+δ_adδ_bc)`.

**CONTACT — k-independent, derived:** a single vertex routes NET zero external
momentum through the one propagator, so `A0_contact` is the only contribution and
it is `k`-independent (contributes to A0 only, never O(k⁴)). Flavour/leg factor:
`(1/24)·δ⁴(π²)²` gives `(1/24)·8·Σ_{3 pairings}δδ = (1/3)·1` for `(1,2,1,2)`.
With the Tr-ln coefficient `(−1)^1/1` and `m·Tr[S]`:
`A0_contact = −(4m²/3)∫ d̃⁴p /(p²+m²)`  (`d̃⁴p ≡ VOL/(2π)⁴` MC measure).

## 6. Flavour weights + symmetry factors — ALL classes, MACHINE-VERIFIED

All results below are produced and checked by `derive_classes.py` (fixed seeds,
output archived in `derive_classes_output.txt`). The external legs are the four
DISTINCT non-singlet pions `a=(1,2,1,2)` on legs `(0,1,2,3)`.

### 6.1 The unified rule (removes the δ-pair ambiguity)

Because the four external pions are DISTINCT fields, every vertex's legs are
external and distinguishable: a size-`s` vertex contributes the ORDERED SU(2)
string `τ^{a}τ^{b}…` (`s` factors), **not** a `π²`-type δ-pair. Concretely, the
`4`-π part of `[(−1)^n/n] Tr[(SΔM)^n]` is, for external legs `{(k_i,a_i)}`,

```
A_phys = Σ_{ordered comps of the class} (−1)^n/n · Π_v (m·d_{s_v}) ·
             Σ_{leg→slot assignments σ∈S4} Re{ Tr_D[S Γ S Γ …] · Tr_f[τ-string] }
```

with vertex data `(size → Dirac Γ, constant d)`:
`1→(γ5, i)`, `2→(𝟙, −1/2)`, `3→(γ5, −i/6)`, `4→(𝟙, +1/24)`.
The loop-order τ-string and the momentum routing are BOTH read in
(vertex order, slot order); the `1/n` exactly compensates the `n` cyclic copies
of each composition. Taking the real part supplies the reflected necklace.

**Anchor 1 (lineage box weights).** For the box, the three reflection-rep
necklaces give `Tr_f = (−2,+2,+2)` — reproduced exactly (see §5).

**Anchor 2 (normalization).** The unified full-symmetric BOX reproduces the
validated lineage `box()` **as an integral**: at `k=0` they agree pointwise
(reflection exact); at `k≠0` they differ pointwise by a piece antisymmetric
under the symmetric-ball measure, so the integrals agree —
`(unified − lineage) = −7e−5 ± 1.4e−4` (consistent with 0). Box-code units are
`A_code = A_phys/(−2m⁴)`; this common factor is irrelevant to the `A0=0` test.

### 6.2 Flavour sums and symmetry factors (derived)

`S_flavour ≡ Σ_{ordered comps}Σ_{σ∈S4} Tr_f[τ-string]`. Since at `k=0` the Dirac
trace is identical across comps/assignments, it factors out and `S_flavour`
carries all of the flavour+multiplicity information:

| class | comps (ordered) | #comps | `S_flavour` | vertex-const Π·(−1)^n/n |
|---|---|---|---|---|
| BOX | (1,1,1,1) | 1 | **16** | `(1/4)(i)⁴ = +1/4` |
| TRIANGLE | (2,1,1),(1,2,1),(1,1,2) | 3 | **48** | `(−1/3)(−½)(i)(i) = −1/6` |
| BUBBLE | (2,2) | 1 | **16** | `(+1/2)(−½)² = +1/8` |
| SUNSET | (3,1),(1,3) | 2 | **32** | `(+1/2)(i)(−i/6) = +1/12` |
| CONTACT | (4) | 1 | **16** | `(−1)(1/24) = −1/24` |

(`S_flavour = #comps · W₂₄` with `W₂₄ = Σ_{σ∈S4} Tr_f = 16` for `a=(1,2,1,2)`.)

### 6.3 Closed-form zero-momentum A0 densities (physical units)

Combining the vertex constants, the `m^n`, `S_flavour`, and the §4 Dirac
reductions gives the per-class `A0` integrand `g(p)` (`x≡p²`, `D≡p²+m²`),
each independently checked against the 4×4 matrix trace (max err `≤5e−15`):

| class | `g(p)` |
|---|---|
| BOX | `+16 m⁴ / D²` |
| TRIANGLE | `−32 m⁴ / D²` |
| BUBBLE | `+8 m²(m²−p²) / D²` |
| SUNSET | `+(32/3) m² / D` |
| CONTACT | `−(8/3) m² / D` |

**Pointwise cancellation (Rider #4a, P4 pre-check):**
`Σ g(p) = [−8m⁴ − 8m²x]/D² + 8m²/D = −8m²D/D² + 8m²/D = 0` — **exactly**,
for all `p`, regulator-independently. Numerically `max|Σ g| = 6.7e−15`.

### 6.4 Correction to the §5 CONTACT prefactor

The §5 draft used the `(π²)²` δ-pair structure and obtained flavour factor
`1/3`, i.e. `A0_contact = −(4m²/3)∫d̃⁴p/D`. That undercounts by **2×**: the four
external legs are distinct, so the correct object is the full ordered trace
`W₂₄ = 16` (not the 3-pairing δ-sum `= 8`). The corrected value is

```
A0_contact = −(8m²/3) ∫ d̃⁴p /(p²+m²)          (2× the §5 draft)
```

This is not cosmetic: with the §5 value the five classes do **not** cancel
(residual `−0.036` in box-code units at `m=0.3`); with the corrected value
`A0[TOTAL]=0` exactly. The P4 pre-check thus did its job — it caught a real
combinatorial error in the diagram set. The same distinct-leg rule was applied
uniformly to V2 in TRIANGLE/BUBBLE and V3 in SUNSET (ordered τ-strings, not
δ-pairs), which is why those cancel too.

### 6.5 Per-class A0 in box-code units (m=0.30, cross-check)

`A_code = A_phys/(−2m⁴)`; analytic values reproduced by MC:
`BOX −0.0805, TRIANGLE +0.1611, BUBBLE +0.1375, SUNSET −0.2907,
CONTACT +0.0727 → TOTAL = 0.0000`.

### 6.6 Status → P4 checkpoint (PASSED)
Derivation complete and machine-verified. The full momentum-routed MC
(`skyrme_full.py`, vectorised, one routing prescription across all classes,
P6-ready) reproduces the per-point evaluator EXACTLY at `k=0` and `k≠0`, and
reproduces the lineage `box()` integral.

**P4 GATE — PASS (all masses).** `p4_gate.py`, seeds (11,23,47),
NMC 4e5/2e5 (archived in `p4_gate_output.txt`):

| m | A0_total (box-code units) | pointwise max\|Σ density\| | verdict |
|---|---|---|---|
| 0.30 | −4.26e−17 ± 6.5e−20 | 1.45e−12 | PASS |
| 0.15 | −9.87e−17 ± 1.0e−18 | 1.41e−11 | PASS |
| 0.08 | −1.39e−16 ± 1.5e−19 | 1.49e−10 | PASS |

`A0_total` is machine-zero (not merely `<3σ`) because `Σ_class g(p)=0`
pointwise; the diagram set and flavour weights are correct. Per-class `A0` is
nonzero and reproducible (e.g. m=0.30: BOX −0.0797 [= pilot P3 box-only A0
−0.07973], TRIANGLE +0.1593, BUBBLE +0.1384, SUNSET −0.2908, CONTACT +0.0727).

**Checkpoint reached — BEFORE the production `kappa_U` scan.** Per standing
discipline, no `kappa_U` numbers are emitted until the checkpoint is reviewed.
Next (post-checkpoint): the `k≠0` `kappa_raw` k⁴-fit with the full class set,
the plateau/overdetermination/mass-scan protocol (spec §3–6), the P6 routing
cross-validation and P7 analytic-slope gate, then the kill-criterion arithmetic.
