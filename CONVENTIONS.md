# Convention Registry

No calculation may begin until every relevant convention is filled, reviewed, and locked. Conflicts must be recorded, not silently resolved.

| Convention | Locked definition | Source |
|---|---|---|
| Euclidean/Minkowski | Migrated C2a and GW loops are Euclidean. Minkowski continuation: NOT YET IMPORTED. | Migrated scripts |
| Metric signature | NOT YET IMPORTED for Paper 5 Minkowski calculations. | Mixed C6 static convention excluded |
| Gamma matrices | Hermitian Euclidean gamma matrices with `{gamma_mu,gamma_nu}=2 delta_mu_nu`. | Extracted gamma utility at `e4f65785` |
| Gamma5 | `gamma5=gamma1 gamma2 gamma3 gamma4`, Hermitian, `gamma5^2=1`; vertices use `i gamma5`. | C2a code |
| Fourier transform | Loop measure `d^4p/(2 pi)^4`. Full transform pair: NOT YET IMPORTED. | C2a derivation |
| Wick rotation | Calculations are Euclidean; general map NOT YET IMPORTED. | Source scope |
| Generator normalization | Pauli `tau^a`; `Tr(tau^a tau^b)=2 delta_ab`, `Tr(tau^a tau^b tau^c)=2i epsilon_abc`. | C2a/GW |
| Flavor basis | Non-singlet SU(2) pattern `(1,2,1,2)`. U(2)/U(3) basis: NOT YET IMPORTED. | C2a |
| Field dimensions | NOT YET IMPORTED. | — |
| Cutoff and lattice units | Sharp Euclidean four-ball `|p|<Lambda`; production `Lambda=1`; ratios use `m/Lambda`. | Exact/PV config |
| External momentum routing | Asymmetric cumulative production routing; symmetric P6 cross-check; `e=m/6,m/4,m/3`. | P6 and production scripts |
| Orientation-field normalization | `M=m exp(i gamma5 theta)`, `theta=tau.pi/f`; common `1/f^4` suppressed. | C2a derivation |
| Skyrme operator | `kappa_raw=(c1-c2)/2`, `kappa_U=m^4 kappa_raw`. Hedgehog commutator map: NOT YET IMPORTED. | Production/exact scripts |
| Topological current | `B^mu=epsilon Tr(L L L)/(24 pi^2)`; `B0_ref=-i a^3/(2 pi^2)`; `c_GW=1`. | P5-GW-01 |
| Sign of the action | `W=-Tr ln(partial-slash+M)`. | C2a derivation |
| Attractive/repulsive channels | NOT YET IMPORTED; Paper 3 vector conventions excluded. | — |
| Green functions | `S(q)=(-i q.gamma+m)/(q^2+m^2)`. Others: NOT YET IMPORTED. | Migrated scripts |
| Statistical errors | Three-seed standard error `std/sqrt(3)`; MC, half plateau spread, and basis residual stacked in quadrature. | Aggregate script |
