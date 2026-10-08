# Scientific claims register

Status: 2026-10-08. Read alongside [RESULTS.md](RESULTS.md). IDs below refer to its eight findings. This is an evidence map, not independent verification: the reports and implementations are mostly AI-authored, and no entry establishes agreement with experimental data or a new fundamental theory. Links identify archived derivations, implementations and plans; they do **not** mean that every linked script runs from a fresh checkout. Missing raw arrays and host-dependent imports remain reproducibility gaps; see [AUSSCHLUESSE.md](AUSSCHLUESSE.md).

**Error categories:** implementation residuals test equations as implemented; approximation errors compare models; discretization and finite-volume errors concern the numerical regulator; sampling errors concern Monte Carlo estimates; experimental uncertainty concerns measured data. These categories cannot substitute for one another. No experimental uncertainty is assessed here. A small same-grid model discrepancy is not a small total physical error.

**Rejection criteria below are prospective review requirements**, written after the archived results. They are not retroactive preregistration, numerical acceptance thresholds, or evidence that new runs have passed. Before a follow-up run, freeze its parameters, estimator, tolerance, resources and treatment of failures in a new plan. Existing plans remain unchanged.

## C1 — Linear light propagation on a static V background

- **Supported scope:** In the specified linear, static, isotropic construction, DEC light carries the expected GR far-field index. The index follows from the chosen coupling and lattice identities; recovering it checks the implementation.
- **Derivation / code:** [Report, especially sections 2 and 8](coordination/runden-v3/RUNDE-37/licht-ablenkung-v/ERGEBNIS.md); [la.py](coordination/runden-v3/RUNDE-37/licht-ablenkung-v/code/la.py) assembles the observable, [zf.py](coordination/runden-v3/RUNDE-37/licht-ablenkung-v/code/zf.py) summarizes it. Archived run was exploratory despite the presence of a card file.
- **Evidence / error:** Deflection/target rises 0.969 → 0.985 → 0.990 with L = 16, 24, 32. This is box-size dependence at fixed lattice spacing, not a controlled continuum extrapolation. Near-source dependence on the Hodge-weight prescription is a model/discretization ambiguity, not statistical noise.
- **Next rejection test:** Reject a proposed continuum interpretation if separately controlled box and spacing studies do not approach a common observable, or if alternative admissible weight prescriptions retain different long-distance limits. An algebraically imposed index cannot count as a distinctive prediction even if reproduced exactly.

## C2 — Static second-order PPN beta

- **Supported scope:** Particular finite-box static Regge calculations are compatible with beta = 1 within reported lattice-gauge sensitivity. This neither proves general Regge convergence nor tests full dynamical or strong-field GR.
- **Derivation / code:** [Report, equations in section 2](coordination/runden-v3/RUNDE-37/beta-netz-v/ERGEBNIS.md); [bn.py](coordination/runden-v3/RUNDE-37/beta-netz-v/code/bn.py), [bn_auswertung.py](coordination/runden-v3/RUNDE-37/beta-netz-v/code/bn_auswertung.py). The report's literature-based convergence expectation is conditional and its cited recollections are marked unchecked.
- **Evidence / error:** Nonlinear/perturbative agreement at L = 6, 12 is an implementation cross-check. L = 16, 24, 32 and radial fits explore finite-volume/far-field behavior; changing the gauge-residual treatment yields beta ≈ 0.95 ± 0.05. This is not an experimental or purely statistical confidence interval. Gamma = 1 is imposed by the isotropic first-order construction.
- **Next rejection test:** With a frozen observable and gauge prescription, reject the claimed GR limit if lattice-equation residuals or beta discrepancies persist under independent spacing and volume control. Convergence of a solver alone does not satisfy this test.

## C3 — Compact U(1) on the tent network

- **Supported scope:** Small-lattice Monte Carlo data support a Coulomb-like regime and a transition for a particular searched set of vertex weights. Photon isotropy is tested only in the sampled direction families; no exact masslessness or all-direction isotropy theorem follows.
- **Derivation / code:** [Report](coordination/runden-v3/RUNDE-37/quant-2/ERGEBNIS.md); [qu2.py](coordination/runden-v3/RUNDE-37/quant-2/code/qu2.py) implements the simulation, [gw.py](coordination/runden-v3/RUNDE-37/quant-2/code/gw.py) evaluates weighted Maxwell bands, [gwp.py](coordination/runden-v3/RUNDE-37/quant-2/code/gwp.py) checks the selected weights. Weight search and some analysis choices were adaptive.
- **Evidence / error:** V uses L = 2, 3 only. E/|k| = 1.01 ± 0.04 is a finite-lattice estimate; beta_c = 1.45 ± 0.01 uses hysteresis width, not a confidence interval. Plain circumcentric weights yield negative bands at tested time steps. Searched weights leave three negative triangle classes but positive physical quadratic eigenvalues at tested momenta. Neither sampled positivity nor constant-field normalization proves positivity at every momentum, reflection positivity, uniqueness, or a continuum limit. The chain identity d1 d0 = 0 and quadratic-action positivity are distinct checks.
- **Next rejection test:** A resolved negative physical eigenvalue at an independently chosen momentum rejects global quadratic positivity for the fixed weight set. Persistent directional dispersion after controlled long-wavelength/refinement tests rejects the corresponding isotropy claim. Freeze the weights before holdout testing; a new search creates a new model requiring new holdouts.

## C4 — SU(2) flow-scale comparisons

- **Supported scope:** Two scale assignments at c = 0.3 give some close network/hypercube ratios. This is not demonstrated universality, a continuum determination, SU(3), or a hadron calculation.
- **Derivation / code:** [S5 report](coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS-S5.md), [S6 report](coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS-S6.md); [su2flow.py](coordination/runden-v3/RUNDE-37/quant-3/code/su2flow.py), [su2flow_s6.py](coordination/runden-v3/RUNDE-37/quant-3/code/su2flow_s6.py), [zusammen_s6.py](coordination/runden-v3/RUNDE-37/quant-3/code/zusammen_s6.py). [S6 plan](coordination/runden-v3/RUNDE-37/quant-3/VORAB-S6.md) distinguishes original sections from later amendments.
- **Evidence / error:** Nt,c = 4, 6; a two-point extrapolation has no degrees of freedom to test its assumed form. Statistical error bars exclude beta_c uncertainty, normalization uncertainty and finite volume. A ±0.03 beta_c shift moves one ratio by about ±12%; L = 4 versus 6 changes t0 by 31 ± 14%. The c = 0.1125 ratio ≈ 0.43 already contradicts an unqualified claim that both discretizations agree at accessible scales.
- **Next rejection test:** Freeze scale setting independently of the desired agreement. Reject universality for the tested formulation if controlled continuum/volume extrapolations of preregistered observables remain incompatible across geometries and reference scales. Add spacing levels sufficient to test the fit form; merely extending a two-point line is not verification.

## C5 — Quantised Q-ball sector: unresolved small binding

- **Supported scope:** No convincing binding of 2–5 quanta was resolved in the tested parameter/volume window; stronger-coupling examples show repulsion. This does not exclude weaker binding, other couplings or larger volumes. Classical large-charge branches are not proof that all possible Q-balls require the quoted charge threshold.
- **Derivation / code:** [Report](coordination/runden-v3/RUNDE-37/quant-1/ERGEBNIS.md); corrected [q1.py](coordination/runden-v3/RUNDE-37/quant-1/code/q1.py) and revised estimator [q1a.py](coordination/runden-v3/RUNDE-37/quant-1/code/q1a.py). The archived first-version coding failure remains part of the record.
- **Evidence / error:** Cubic L = 4, 8 and V L = 4; free-field controls and sampling errors constrain detection sensitivity. The near-zero binding estimate is comparable to the free-control bias/uncertainty. No continuum or infinite-volume binding analysis is established.
- **Next rejection test:** A negative E(N) − N m1 that survives independent estimator, fit-window, volume and spacing controls would refute the restricted no-binding interpretation at those parameters. Failure to resolve it only sets a sensitivity-dependent bound; it does not prove exact absence.

## C6 — Fixed-volume stabilization in three test networks

- **Supported scope:** The specified constrained integrator completes ten periods in s1–s3 while the unconstrained controls fail; s4 remains problematic. The global constraint is an added dynamical assumption, not a derived physical law.
- **Derivation / code:** [Report](coordination/runden-v3/RUNDE-37/volumen-g2-1/ERGEBNIS.md), [original card](coordination/runden-v3/RUNDE-37/volumen-g2-1/KARTE.md); [vg2.py](coordination/runden-v3/RUNDE-37/volumen-g2-1/code/vg2.py), [vg2b.py](coordination/runden-v3/RUNDE-37/volumen-g2-1/code/vg2b.py). The random-constraint comparison was added after initial results.
- **Evidence / error:** Four N = 128 networks, one small-amplitude regime, ten periods. Fixed-operator energy residual ≲1.3e−10 checks that integrator; moving operators and topology changes have separate drift and jump errors. Large constraint forces and s4's unresolved drift prevent a general stability conclusion. No size, long-time or continuum stability limit is established.
- **Next rejection test:** Independent network seeds, smaller time steps and longer durations must retain the claimed improvement under frozen criteria. A surviving strong growing mode or nonconvergent unexplained energy drift rejects general stabilization; s4 already prevents a universal four-network success claim.

## C7 — Dimension-estimator calibration

- **Supported scope:** Finite-size calibration exposes substantial, ensemble-dependent bias. Quadrangulation estimates are low; CDT Hausdorff estimates near 2.2–2.3 are above the expected 2, with the distance convention/lattice-correction interpretation unresolved. This is not a measured spacetime dimension.
- **Derivation / code:** [Report and its explicit CDT weight assumption](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/ERGEBNIS.md); [dseich.py](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/code/dseich.py), [cdtexakt.py](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/code/cdtexakt.py), [analyse.py](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/code/analyse.py); [card](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/KARTE.md).
- **Evidence / error:** Sizes reach 10^5 for quadrangulations and 64000 for CDT. Sampling/fit uncertainty is much smaller than some estimator and offset dependence. Size studies exist, but do not settle the limiting estimator value or validate extrapolation to the project's higher-dimensional networks.
- **Next rejection test:** Reject a proposed dimension estimator/fit as calibrated for the target size range if it fails independent known-ensemble controls with matched metric and finite-size treatment. Do not reinterpret that failure as new dimensional physics.

## C8 — Classical Higgs-portal reduction

- **Supported scope:** Reduced energy and inertia approximate specified full classical radial-3D model observables. Higgs parameters are inputs; no electroweak symmetry-breaking derivation, quantum stability, full nonlinear stability or calculation on V is supplied.
- **Derivation / code:** [Response](coordination/higgs-response-20261008/ERGEBNIS.md), [force](coordination/higgs-force-20261008/ERGEBNIS.md), [minima](coordination/higgs-minima-20261008/ERGEBNIS.md), [full modes](coordination/higgs-modes-20261008/ERGEBNIS.md), [reduced modes](coordination/higgs-reduced-modes-20261008/ERGEBNIS.md), [angular derivation](coordination/higgs-angular-modes-20261008/ERGEBNIS.md), [linear dynamics](coordination/higgs-dynamics-20261008/ERGEBNIS.md). Each packet contains its run.py and PLAN.md; the final implementation is [run.py](coordination/higgs-dynamics-20261008/run.py) with [models.py](coordination/higgs-dynamics-20261008/models.py).
- **Evidence / error:** Earlier response/force tests cover eight parameter groups; new relaxations and mode tests use one parameter point with three grid/box settings. The maximum ≈0.000237% dynamic-frequency discrepancy is a same-discretization approximation error. Residual checks and some grid/box comparisons are present; no continuum physical accuracy, general parameter-domain guarantee, or experimental precision follows. A radial 3D background plus tested angular sectors is not a full nonlinear 3D evolution.
- **Next rejection test:** Retain the existing [dynamic plan](coordination/higgs-dynamics-20261008/PLAN.md) and [reconstruction amendment](coordination/higgs-dynamics-20261008/AMENDMENT.md). New parameter/finite-amplitude tests need new frozen criteria. Failure of a reduced model's promised observable tolerance rejects that approximation in the tested regime; instability in an untested sector would invalidate a broader stability claim. Neither outcome determines whether nature uses this model.

## Reading the archive

| Archive term | Meaning here |
|---|---|
| V / Zeltnetz | Specific filled tetrahedral spatial network / its time-extended tent construction; distinguish the two. |
| Finn-Ecke / Finn-Kante | Project vertex/edge labels and length convention, not independently established physical objects or scales. |
| Takt | Lapse or local time-rate variable in the stated model. |
| Hebehoehen | Vertex lifting weights used in weighted dual geometry; model inputs, not measured particle properties. |
| Umklappen / Zug | A specified local topology-changing move; details depend on the experiment. |
| KARTE / VORAB / PLAN | Task card or run plan. Read timestamps and amendments: file existence alone does not establish preregistration. |
| ERGEBNIS / lauf-69 | Result report / archived run-output directory named after an original compute host. |

**Priority rule after the reviews:** First make one V calculation portable and independently checkable, and test the Maxwell construction's positivity and refinement behavior. A distinctive anisotropy/dispersion signal remains a *candidate question*: it becomes a physical prediction only after specifying the physical scale, regulator interpretation, comparison model and observational test. Additional digits in C8 cannot discharge C1–C7's missing foundational tests. External human review remains outstanding.
