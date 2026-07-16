# C2a — Non-singlet Orientation-Sector Derivative Expansion

## Scientific question

What is the complete one-loop quartic/Skyrme coefficient of the non-singlet SU(2) orientation field after all chirally required diagram classes are included?

## Locked scope and assumptions

- Non-singlet SU(2) orientation sector only; not the anomalous U(1)_A singlet.
- Fermion mass field (M(x)=m\exp(i\gamma_5\theta)).
- Euclidean sharp four-ball cutoff for the exact finite-cutoff expression and production comparison.
- All five vertex partitions: box, triangle, bubble, sunset, and contact.
- The Ward normalization supplies the (m^4) operator-normalization anchor.
- The source conventions and unresolved convention imports are recorded in `CONVENTIONS.md`.

## Authoritative result

The legacy record establishes

```text
kappa_U(m, Lambda) =
Lambda^4 (-17 Lambda^6 - 85 Lambda^4 m^2 - 170 Lambda^2 m^4 - 90 m^6)
------------------------------------------------------------------------
                1152 pi^2 (Lambda^2 + m^2)^5
```

and therefore

```text
lim_(m/Lambda -> 0) kappa_U = -17/(1152 pi^2).
```

The negative sign is confirmed by the exact expression, two independent evaluators, the production scan, and the common-form-factor PV comparison.

## Required anchors

- five-class flavor weights and symmetry factors;
- pointwise (A_0=0) cancellation;
- startup regression targets;
- Ward (m^4) normalization;
- matrix and analytic-trace evaluator agreement;
- exact/numerical agreement;
- regulator/PV negative-sign persistence;
- committed aggregate-table reproduction.

## Provenance

- Source repository: `zetacheng/kappa-c2a`.
- Derivation framework: `2f9758dcf105c10dcd53a420d95ef4f9bd505765`.
- Production checkpoint: `6210279f22693da6f7f4406509203ad8d495aa88`.
- Exact derivation: `4a0de1e2d6875f0ac27907395b3fc28b6bd7ce25`.
- Final exact/PV branch state: `cba89de41183d08c587af5187edfbc8de659df9f`.

`diagram_classes.md`, `legacy_spec.md`, and `exact_kappa_derivation.md` are byte-for-byte copies of the identified legacy blobs. Paper 4 kill-chain commentary present in historical files is retained as provenance only and does not make Paper 5 the owner of those downstream conclusions.

## Implementations

The exact scripts are in `scripts/c2a/`. Reproduction commands and stored artifact provenance are in `results/c2a/README.md`.

## Known failure modes

The source record identifies incomplete diagram sets, constant-term leakage into the quartic fit, momentum outside the derivative-expansion radius, broken chiral structure in naive PV denominator replacement, and sampling noise in an earlier R4 estimate.

## Preregistered verdicts

The complete record accepts the exact negative coefficient and rejects the former positive-coefficient route. Passing code alone is insufficient; the stored anchors and independent review remain part of the verdict.

