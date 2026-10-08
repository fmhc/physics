# Results: what is computed, with limits

Status 2026-10-08. This page lists the findings of this notebook that we consider robust enough to state, each with
method, number, limits and the source file. Everything here is a **synthetic model computation**: no finding is a
confirmation by measured data, none is peer-reviewed, and most text and code was written by AI systems under human
direction ([BETEILIGTE.md](BETEILIGTE.md)). The source files are in German.

"Error" means the uncertainty stated in the source (jackknife or standard error of the mean unless noted). Several runs
were exploratory, without a pre-registered plan; this is noted per item. Small lattices throughout; no continuum or
infinite-volume limit has been taken anywhere.

The model architecture (Regge gravity + discrete exterior calculus Maxwell + scalar field on one simplicial complex) is
known from the literature, e.g. McDonald and Miller 2010. What is our own are the computations on the specific filled
tetrahedral network "V" and its time-extended "tent" version.

## Findings

### 1. Light deflection and Shapiro delay on V match the linearised GR far field

- **Claim:** For a static point source on V, light propagated with discrete Maxwell (DEC) on the deformed network gets
  the full GR refractive index, n - 1 = -2 Phi, with lapse and spatial lengths each contributing one half.
- **Method:** Linear static solution on periodic L^3 cells (L = 16, 24, 32), Hodge stars rebuilt from the solved edge
  lengths, eikonal deflection and time delay summed along lattice columns.
- **Numbers:** n - 1 within 0.1 % of -2 Phi per shell for r = 3 to 20 l_P (L = 32). Ratio of length part to lapse part
  0.999 to 1.001 (GR: 1). Total deflection / target 0.969, 0.985, 0.990 for L = 16, 24, 32; the remainder shrinks with L
  and is attributed to the torus approximation of the target.
- **Limits:** Linear in the mass. The far-field value follows in advance from lattice identities (stated in the source),
  so this tests that the implementation carries it, not an independent prediction. Below about 1.5 l_P the result
  depends on how the weights follow the geometry (ratios 0.68 to 3.9). Exploratory run without a frozen plan.
- **Source:** [licht-ablenkung-v/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/licht-ablenkung-v/ERGEBNIS.md)

### 2. Second-order PPN beta on V is compatible with 1

- **Claim:** The fully nonlinear static Regge solution on V reproduces the second-order lapse of GR in the far field.
- **Method:** Quasi-Newton solution with exact dihedral angles (L = 6, 12; agrees with second-order perturbation theory
  to 4e-6), perturbation theory on L = 16, 24, 32, shell-wise comparison with Einstein's value, extrapolated in volume.
- **Numbers:** beta(r) = 0.91 at r = 4.5 l_P rising to 1.00 at r = 10.5 to 11.5 l_P; extrapolated beta = 1.00 to 1.02
  depending on the fit form. Including the gauge residual of the lattice equations: beta = 0.95 +- 0.05.
  gamma = 1 is an identity of the isotropic gauge (deviation 2.5e-16), not a result.
- **Limits:** Static, single point source, periodic boxes. Near the source beta is far below 1 (0.58 at 2.6 l_P). The
  second-order spatial term (delta) could not be determined. Regge calculus is known to converge to GR, so agreement is
  expected in principle. Exploratory run.
- **Source:** [beta-netz-v/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/beta-netz-v/ERGEBNIS.md)

### 3. Compact U(1) on the tent network: massless, isotropic photon and a phase transition

- **Claim:** Quantised (Monte Carlo) compact U(1) gauge theory on the time-extended network V has a Coulomb phase with a
  massless photon moving at speed 1 in all tested directions, and a confining phase.
- **Method:** Euclidean heat-bath plus overrelaxation, weighted Wilson action normalised to Maxwell (identity holds to
  1e-15); cubic lattice L = 6, 8 as control.
- **Numbers:** Photon E/|k| = 1.01 +- 0.04 at beta = 2.0, equal for the <111> and <100> direction families within about
  5 %. Transition at beta_c = 1.45 +- 0.01 on V (L = 3, spread = hysteresis width); cubic control 0.998 to 1.006
  (literature value about 1.011, quoted from memory).
- **Limits:** The plain circumcentric Hodge stars of the tent network give a negative Maxwell band for every tested
  time step; the computation needed vertex weights found by a numerical search (3 of 484 triangle classes stay slightly
  negative). Only L = 2 and 3 on V. Order of the transition not established. String tension and Luescher term could not
  be measured (sigma = 2.0 +- 0.8 a^-2 only in one distance window, compatible with zero without r < 0.3 a). Search,
  multihit and re-analysis were decided during the run.
- **Source:** [quant-2/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/quant-2/ERGEBNIS.md)

### 4. SU(2) on the network: gradient-flow scales track the hypercubic lattice at two lattice spacings

- **Claim:** Dimensionless gradient-flow ratios of SU(2) Yang-Mills on the tent network agree with the hypercubic lattice
  at two temporal lattice spacings (N_t,c = 4 and 6) to a few per cent.
- **Method:** Wilson flow of the same weighted action (Luescher RK3), t0 and w0 at t^2 <E> = 0.3, flow time on the
  network converted with a free-field factor kappa = 0.0145; beta_c from Polyakov-loop susceptibility.
- **Numbers (network / hypercube, statistical errors only):**
  w0/sqrt(t0): 0.998 +- 0.007 (N_t,c = 4), 0.978 +- 0.009 (N_t,c = 6).
  T_c sqrt(t0): 0.973 +- 0.010 (N_t,c = 4), 1.010 +- 0.022 (N_t,c = 6).
  beta_c(network, N_t = 6) = 3.411 +- 0.014, realistic spread about 0.03.
- **Limits:** T_c sqrt(t0) depends steeply on the assignment of beta_c: +-0.03 in beta_c(network) moves it by +-12 %,
  so this agreement is a condition on beta_c rather than an independent test. Finite volume: L = 4 gives t0 31 +- 14 %
  higher than L = 6 at N_t = 18. At the alternative reference value c = 0.1125 the two lattices disagree (ratio 0.43).
  Two spacings only; the extrapolation in the source is descriptive. SU(2), not SU(3); no fermions.
- **Sources:** [quant-3/ERGEBNIS-S5.md](coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS-S5.md),
  [quant-3/ERGEBNIS-S6.md](coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS-S6.md)

### 5. Quantised Q-ball field: no small bound states; classical Q-balls are many-quantum objects

- **Claim:** In the quantised complex scalar (Q-ball) sector, states of 2 to 5 quanta are not bound; at stronger coupling
  the quanta repel. Classical Q-balls exist only for a large number of quanta.
- **Method:** Hybrid Monte Carlo on cubic lattices (L = 4, 8) and on V (L = 4), multi-particle correlators, free-field
  control at the same statistics.
- **Numbers:** Binding per particle at lambda = 0.25, L = 4: b_2 = 0.0010 +- 0.0007, free control 0.0007 +- 0.0010
  (indistinguishable). At lambda = 1: E(2) - 2 m_1 = +0.016 +- 0.003, E(3) - 3 m_1 = +0.051 +- 0.011 (repulsive).
  Classical Q-balls require lambda N >= 112 quanta (bound from lambda N >= 141.5).
- **Limits:** Small lattices and limited statistics; the interpretation "Q-balls are heavy multi-particle objects, not
  small particles" is a hypothesis drawn from these numbers. A coding error in a first version was found and those runs
  were discarded (documented). Exploratory run.
- **Source:** [quant-1/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/quant-1/ERGEBNIS.md)

### 6. A fixed-volume constraint stabilises the network dynamics in 3 of 4 test networks

- **Claim:** In the Hamiltonian dynamics of the network with topology-changing moves, a global volume constraint
  (unimodular-gravity style) removes the strongly growing mode that otherwise appears after moves.
- **Method:** Implicit-midpoint integrator with a Lagrange multiplier, four disordered networks s1 to s4 (N = 128),
  amplitude 1e-3, 10 periods, with and without constraint; card and expectations written before the runs.
- **Numbers:** Without the constraint all four networks abort after 0.12 to 7.2 periods (metric no longer positive).
  With it, s1, s2, s3 run 10 periods with max |H - H0|/H0 = 2.8e-3, 1.05e-3, 7.2e-4; the strong mode (omega^2 about
  -1e7) does not survive any of the 133 moves in s1 to s3. Integrator check with fixed operators: energy kept to 1.3e-10
  over 10 periods.
- **Limits:** The constraint force is not small (30 to 88 % of the network force). s4 has an unstable episode and an
  unexplained drift of 2.9e-3. The control with a random single constraint used one random vector per network and was
  added after first results. Not the full model (mass matrix updated piecewise).
- **Source:** [volumen-g2-1/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/volumen-g2-1/ERGEBNIS.md)

### 7. Calibration of the dimension estimators: they underestimate at accessible sizes

- **Claim:** The Hausdorff and spectral dimension estimators used for the dynamical-network runs are biased low at the
  sizes we can simulate, so small-size dimension values from those runs are not interpretable.
- **Method:** Same estimators applied to ensembles with known answers: random quadrangulations (exact sampler,
  d_H = 4, d_s = 2) and 1+1D causal dynamical triangulations, N up to 1e5.
- **Numbers:** Quadrangulations: d_H from size scaling 3.38 (N = 1e3 to 1e5); compatible with 4 only with a large
  negative offset (chi^2/ndf = 1.2; d_H = 3 gives 20). Spectral dimension maximum 1.77 to 1.83 instead of 2. CDT: d_s =
  2.00, but d_H = 2.2 to 2.3, stable up to N = 64000; whether this is a lattice correction is undecided.
- **Limits:** Quadrangulations instead of triangulations (same universality class assumed). The CDT layer weight is our
  own derivation, not taken from the literature.
- **Source:** [ds-eichung-2d-1/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/ERGEBNIS.md)

### 8. Higgs-portal model: reduced energy and inertia reproduce tested static and linear dynamic observables

- **Claim:** In a classical model with two complex singlets coupled to a real Higgs amplitude (radial 3D, Higgs mass
  and vacuum value as inputs), a reduced Higgs energy ("Ecomp") and induced inertia reproduce the tested full-model
  profiles, forces, energy curvatures and low linear dynamic frequencies.
- **Method:** CUDA float64 evaluation of 24 archived stationary profiles (8 parameter groups, three grid/box levels),
  then new relaxations, Hessian eigenvalues and 63 linear dynamic spectral problems at one parameter point;
  pass criteria set in advance per step.
- **Numbers:** Profile error of the second-order Higgs response 0.64 to 0.71 % at the stronger coupling. Portal-force
  error of Ecomp 0.0097 to 0.0116 %. In 18 new relaxations the Ecomp matter profile deviates by at most 6.6e-5 %, the
  reconstructed Higgs profile by about 0.65 %. Full theory: no negative energy curvature in all 8 tested sectors
  (angular orders l = 0 to 3) after identified symmetry directions. Reduced models: radial eigenvalue errors at most
  0.0099 % (E3) and 0.00025 % (Ecomp). A further 36 matrices test angular orders l = 1, 2 against the full static
  Higgs response (Schur complement): at most 0.007295 % (E3) and 0.0003385 % (Ecomp) eigenvalue error, translation
  identified and other tested directions positive. Independent finite-angle energy differences check the angular
  derivation. Adding the induced Higgs inertia reduces the maximum Ecomp dynamic-frequency error from 0.01583 %
  to 0.000237 %; E3 with inertia reaches 0.007857 %. No resolved exponentially growing mode in tested l = 0, 1, 2
  sectors on three finite grids. Errors compare models at the same discretization, not statistical uncertainties.
- **Limits:** The second-order response was planned after the first-order one failed at stronger coupling (documented).
  A first dynamic run stopped on a reconstruction-residual check near the translation zero mode; a numerically stable
  equivalent reconstruction passed unchanged tolerances, retaining 28 completed spectra and computing the remaining 35.
  One parameter point for relaxations and modes; the earlier curvature tests are static, while the new spectral test
  concerns linear dynamics only. No direct nonlinear time integration or quantum-stability test;
  computed on radial grids, not on V. This is a classical model with Higgs parameters put in by hand, not a derivation
  of the Higgs mechanism.
- **Sources:** [higgs-response](coordination/higgs-response-20261008/ERGEBNIS.md),
  [higgs-force](coordination/higgs-force-20261008/ERGEBNIS.md),
  [higgs-minima](coordination/higgs-minima-20261008/ERGEBNIS.md),
  [higgs-modes](coordination/higgs-modes-20261008/ERGEBNIS.md),
  [higgs-reduced-modes](coordination/higgs-reduced-modes-20261008/ERGEBNIS.md),
  [higgs-angular-modes](coordination/higgs-angular-modes-20261008/ERGEBNIS.md),
  [higgs-dynamics](coordination/higgs-dynamics-20261008/ERGEBNIS.md); background:
  [inventory of earlier portal runs](coordination/higgs-bestandsaufnahme-20261007/BESTAND.md)

## Negative results

- **Unmodified Q-balls are not hadrons.** They are bosonic; a spinning Q-ball changes its angular momentum by its whole
  charge (J = m Q, steps of hundreds to thousands). No Regge line: in 2D the shape ratio R2 = 2.375 at Q = 1000
  (hadrons 1.98) and drifts towards the rigid rotor with Q; in 4D the two-plane test gives K = 1.36 to 1.53 (Regge: 1).
  [qball-hadron-1/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/qball-hadron-1/ERGEBNIS.md)
- **No small bound states in the quantised Q-ball sector** (finding 5 above).
- **No generation mechanism from flux patterns.** Without spin-orbit coupling none of the 64 Z2 flux patterns of the
  cubic cell has isolated Dirac nodes; with spin-orbit coupling three nodes appear only at the isotropic point, and the
  three masses are freely tunable (no prediction). The same check found that two of eight AI-generated scripts crash
  and three insert their result by hand.
  [antigravity-nachbau-1/ERGEBNIS.md](coordination/runden-v3/RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md)
- **Braid (preon) models do not fit into V as dual subgraphs.** In a strict simplicial complex two tetrahedra share at
  most one triangle, so the four-valent braid (two nodes sharing three edges) cannot occur; the original authors state
  the same. Relaxing the rule yields only the trivial braid. Desk proof, not independently checked.
  [zopf-simplizial-l/ERGEBNIS.md](coordination/runden-v3/RUNDE-51/zopf-simplizial-l/ERGEBNIS.md)
- **No measurable string tension** in compact U(1) on V at the accessible sizes (finding 3).
- **Flow scales disagree at the second reference value** c = 0.1125 (finding 4).
- **Vortex triples and pairs do not form a robust Y string**; they are screened or bound as a bag.
  [y1](coordination/runden-v3/RUNDE-10/y1/ERGEBNIS.md), [y2](coordination/runden-v3/RUNDE-11/y2/ERGEBNIS.md)
- **Formation of bound Higgs-portal objects from broad initial packets failed** the pre-set criteria (runs B22/B23,
  summarised in [BESTAND.md](coordination/higgs-bestandsaufnahme-20261007/BESTAND.md)); stationary existence is not
  spontaneous formation.

## Not shown

No derivation of particle masses, of SU(3), of the weak interaction, of the Higgs mechanism or of three generations; no
spin-1/2 dynamics; no quantitative prediction tested against measured data. The per-area status table in the
[README](README.md) gives a subjective maturity estimate for each area.
