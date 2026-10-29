# Abbildungen zum Stand 29.10.2026 / Figures, status 29 Oct 2026

Alle Abbildungen zeigen nur gespeicherte Ergebnisse; für diese Abbildungen wurde weder ein Fit noch eine neue Rechnung
gemacht. Synthetische Modellrechnungen (G1–G4 Gitterrechnungen, die Q-Ball-Leiter ein Kontinuumsmodell), keine
Messdaten, nicht begutachtet. Die zugrunde liegenden internen
Ergebnisdateien und Rohdaten sind hier nicht mit veröffentlicht; die geplotteten Werte stehen unten.
All figures show stored results only; no fit and no new computation was made for them. Synthetic model calculations
(G1–G4 lattice simulations, the Q-ball ladder a continuum model), no measured data, not peer reviewed. The underlying internal result files and raw data are not published here; the
plotted values are listed below.

Belegart der Gluon-Abbildungen / evidence class of the gluon figures: [R] Euclidean Monte Carlo simulation of pure
SU(3) gauge theory (quenched, Wilson action) on the lattice BCC-r\* × Z. Error bars: statistical (block jackknife);
after cross-reading, rather lower bounds.

## G1 — Flow scale and lattice spacing (`fig-gluon-g1-skala.png`, `.svg`)

![G1](fig-gluon-g1-skala.png)

Gradient-flow scale t₀/a² (a) and the lattice spacing a derived from it (b) versus β, for two discretisations of the
energy density (clover blue, plaquette orange). β = 6.0 on a 4³×16 box (22 configurations), β = 6.5–6.8 on 5³×8 (50
configurations each); a = √t₀ / √(t₀/a²) with √t₀ = 0.1669 fm (Lüscher; convention r₀ = 0.5 fm, a setting [W]); the
0.66 % reference error is not included. Clover and plaquette differ by a factor 1.3–2.7 in t₀, so there is no
definition-independent scale yet; at β = 7.0 the flow does not reach t₀ inside the box. β = 6.8 (open symbols) sits at
the volume limit and is descriptive only; a volume check on 8³×12 at β = 6.8 is unresolved (hot- and cold-start chains
disagree).

Plotted values (clover t₀/a²): 0.2446(4) / 0.3008(18) / 0.3531(30) / 0.5006(115) / 0.756(38) at β = 6.0 / 6.5 / 6.6 /
6.7 / 6.8; a(t₀) = 0.337 / 0.304 / 0.281 / 0.236 / 0.192 fm. Plaquette t₀/a²: 0.0895 / 0.122 / 0.150 / 0.260 / 0.570.

## G2 — Control ratio K = √t₀/w₀ (`fig-gluon-g2-k.png`, `.svg`)

![G2](fig-gluon-g2-k.png)

Ratio of two differently defined flow scales (measured on the same ensembles) versus β, clover and plaquette, with the quenched SU(3) continuum value 0.9796
from cubic lattices (Asakawa et al., arXiv:1503.06516, Tab. II) and the pre-registered ±10 % gate (grey). Same ensembles
as G1. For the clover definition K drops from +20.3 % (β = 6.0) to +7.7 % (6.7) and +4.7 % (6.8); the plaquette
definition gives −7.3 / −22.8 / −7.7 % (6.6 / 6.7 / 6.8) and is not smooth. The gate is passed only for the clover
definition; at β = 6.8 the small box pushes K in the same direction, so that point is descriptive only.

Plotted values: clover 1.1784(2) / 1.1616(10) / 1.1329(22) / 1.0545(64) / 1.0256(83); plaquette 1.1351(3) / 1.0778(30)
/ 0.908(16) / 0.756(6) / 0.904(6) at β = 6.0 / 6.5 / 6.6 / 6.7 / 6.8.

## G3 — Topological susceptibility (`fig-gluon-g3-chi.png`, `.svg`)

![G3](fig-gluon-g3-chi.png)

t₀²χ_t (raw clover charge at flow time t₀) versus a²/t₀, with the cubic-lattice continuum value 6.67(7)×10⁻⁴
(Cè et al., arXiv:1506.06052, Eq. (5.4)) as dashed line. β = 6.0 (4³×16, 100 configurations), 6.5 / 6.6 (5³×8, 50
each), 6.7 on 5³×8 (50) and 7³×10 (64); the diamond is 7³×10 at t_p (√(8t) = 2.5a), shifted by +0.04 for legibility.
**There is no continuum band:** no continuum fit is stored, and the points are not linear in a². At a²/t₀ ≈ 2 the value
is still 37–47 % low; the charge is not integer-valued and keeps growing with flow time (G4). The open symbol
(β = 6.7, 5³×8) was selected after looking at the data and is descriptive only. a is the cube edge; the undetermined
anisotropy of the lattice (+3 to +15 %) is not in the error budget.

Plotted values (×10⁻⁴): 0.395(48) / 0.746(130) / 1.10(22) / 3.76(54) [5³×8] / 3.56(55) [7³×10, t₀] / 4.23(72)
[7³×10, t_p] at a²/t₀ = 4.09 / 3.32 / 2.83 / 2.00 / 2.05 / 2.05.

## G4 — Flow-time dependence of t₀²χ_t (`fig-gluon-g4-flussverlauf.png`, `.svg`)

![G4](fig-gluon-g4-flussverlauf.png)

t₀²χ_t as a function of flow time, plotted against the smoothing radius √(8t)/a; lines are the mean curve (no errors
stored there), points with error bars at t₀, t_p and 2t₀. β = 6.7 on 7³×10 (64 configurations) and β = 6.6 on 5³×8
(50). Grey: pre-registered plateau window √(8t) = 2.50–2.85a. In the continuum the curve would be flat; here it keeps
rising inside the window, d ln⟨Q²⟩/d ln t = 0.38(9) (gate ≤ 0.2: not met, borderline; about 1.7σ under an AR(1)-based
error-inflation estimate, a longer-block reanalysis remains pending). At β = 6.7 the two boxes give the same χ (ratios 0.95–1.06 ± 0.22); that the deficit comes from the coarse
lattice rather than the box is only an indication and, without a cubic-lattice comparison, not specific to BCC.

## Q-ball ladder (`fig-qball-ladder.png`, `.svg`)

![Q-ball ladder](fig-qball-ladder.png)

Figure from preprint 0.51 ([paper folder](../../model-lab/papers/qball-bic-ladder-v0.51/README.md)): archived radial
locations through n = 15 and their inverse detunings 1/(ω² − 1/2). Filled symbols mark the two radial existence
enclosures C0/C1; open symbols are numerical candidates, not certified. The plot keeps its original fifteen-point
dataset including an earlier rounded index-15 estimate; the paper's ladder table records the later 15–18 calculation.
No fit or extrapolation. Licence of all figures in this folder: CC BY 4.0.
