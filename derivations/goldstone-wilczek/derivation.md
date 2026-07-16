# Goldstone–Wilczek Topological-Current Normalization

This note is a provenance-preserving extraction of **Step 1 — Goldstone-Wilczek matching** from legacy `derivation/c6_matching.md` at commit `0ba85e578d438f4f9abcb2a10c501e74acc0b190`.

Only the independently separable topological-current calculation is authoritative here. The legacy Step 2 onward—HS integration, `C6=-G_V/2`, Walecka bookkeeping, vector sign, and stabilization conclusions—is Paper 3-owned and deliberately omitted.

## Step 1 — Goldstone-Wilczek matching (anchor #1)

The fermion loop `<J^mu(q) pi^a pi^b pi^c>` with one `gamma^mu` (baryon-current)
vertex and three `V1 = i m gamma5 tau.pi` vertices induces the topological
current. Its leading (three-momentum) epsilon-structure matches the topological
baryon current

    B^mu = eps^{mu nu rho sig} Tr[L_nu L_rho L_sig] / (24 pi^2),   L_mu = U^dag d_mu U.

**Tree reference.** With `U=exp(i tau.pi)` (f=1, code convention), `L_mu = i tau^a
d_mu pi^a + O(pi^2)` and `Tr[tau^a tau^b tau^c] = 2 i eps_{abc}`, so
`Tr[L_nu L_rho L_sig] = 2 eps_{abc} d_nu pi^a d_rho pi^b d_sig pi^c` and

    B^mu = (1/12 pi^2) eps^{mu nu rho sig} eps_{abc} d_nu pi^a d_rho pi^b d_sig pi^c.

For the test configuration `mu=0`, pions `(flav 1,2,3)` with momenta along the
orthogonal axes `1,2,3` of magnitude `a`, the 4-point coefficient (three
functional derivatives, 3! equal assignments) is

    B^0_ref = (1/12 pi^2) * 3! * eps^{0123} eps_{123} (i a)^3 = - i a^3 / (2 pi^2).

**Loop side (numeric, `c_gw_loop.py`).** `Gamma^0 = -(i m)^3 Int d^4p/(2pi)^4
sum_{3! orderings} Tr_f[tau tau tau] Tr_D[gamma^0 S g5 S g5 S g5 S]`, Euclidean
`S(q)=(-i q.gamma + m)/(q^2+m^2)`. Define `c_GW = Gamma^0 / B^0_ref`.

RESULT (importance-QMC, a->0 and Rmax->inf extrapolations):
- cutoff scan m=0.30: c_GW = 0.980, 0.997, 0.9988, 0.9989 at Rmax=1,2,4,8
  (converged by Rmax=4: anomaly-type FINITE, cutoff-independent);
- m-independence: c_GW(0.30)=c_GW(0.15) to <0.1% (topological);
- a->0 extrapolation (Rmax=4): **c_GW = 0.9999 +- 0.0005**, imaginary part 0.

**HARD GATE PASSED: c_GW = 1 (unit baryon charge), real, cutoff-independent.**
The microscopic vector current matches the topological baryon current with unit
coefficient: `J^mu_top = B^mu`.
