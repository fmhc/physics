# Draft section: thin-wall phase-matching description of the breathing-mode ladder

<!--
Draft by the theory agent of claude-primary (Anthropic, Opus), for the second paper on the BIC ladder.
Started 2026-09-30 10:24:13 CEST (date). End time at the bottom of the file.
Sources: RUNDE-09/MODELL-DUENNWAND.md (M.1-M.7), RUNDE-09/VORHERSAGEN-MOD2.md, RUNDE-08/VORHERSAGEN-SP1.md,
RUNDE-09/sd1/VORHERSAGEN-SD1.md; outcomes as recorded in RUNDE-09.md (FORMEL-1/2/3 and MOD-2 outcome, SP-1, SD-1,
MESS-1); resonance-20260930/novelty-audit/PAPER-LEITER-EINARBEITUNG.txt (evidence rules).
Literature marks: [checked] = the quoted passage was read in the local text extraction of the PDF in
coordination/resonance-20260930/papers/; [to verify] = not yet checked against the primary text.
Wording of the whole paper is decided by the coordinating author (Codex, ag-phy-coordination).
-->

**Status of this section.**
- The thin-wall picture is a *description with calibrated constants*, not a parameter-free theory.
- Two ingredients are derived: the geometry (thin-wall radius, interior wavenumber, bare wall state) and the structure
  of the condition (period $\pi$ in a phase, alternating sign of the coupling).
- Two ingredients are fitted to computed zeros: a wall phase $\theta(\epsilon)$ and a level shift of the wall state.
- All statements refer to the linearized radial problem. Nothing in this section concerns nonlinear stability.

## 5.1 Setting

- We consider $U(S)=S-S^2+\beta S^3$ with $S=|\phi|^2$ and unit mass, and a Q-ball $\phi=f(r)e^{i\omega t}$.
- Perturbations are $\delta\phi=e^{i\omega t}\,(u\,e^{i\rho t}+v^{*}e^{-i\rho t})$.
- For angular momentum $l$ the reduced radial functions $U=ru$, $V=rv$ obey

$$
U''=\Big[d_p(r)+\tfrac{l(l+1)}{r^2}-(\omega+\rho)^2\Big]U+s_p(r)\,V,\qquad
V''=s_p(r)\,U+\Big[d_p(r)+\tfrac{l(l+1)}{r^2}-(\omega-\rho)^2\Big]V,
$$

  with

$$
d_p=\big(S\,U'(S)\big)'=1-4S+9\beta S^2,\qquad s_p=S\,U''(S)=-2S+6\beta S^2 .
$$

- For $1-\omega<\mathrm{Re}\,\rho<1+\omega$ the channel $U$ is open with $q^2=(\omega+\rho)^2-1$, and $V$ is closed with
  $\kappa^2=1-(\omega-\rho)^2$.
- An embedded (radiationless) mode is a real pair $(\rho,\omega^2)$ at which a regular solution has no radiating
  component in $U$ and no growing component in $V$.
- For real $\rho$ all coefficients are real. The condition amounts to two real equations in two real unknowns, so such
  points are generically isolated along a one-parameter family of balls.

## 5.2 Thin-wall background

- $U(S)/S$ is minimal at $S_c=1/(2\beta)$, which defines the thin-wall threshold $\omega_c^2=1-1/(4\beta)$ and the
  detuning $\epsilon=\omega^2-\omega_c^2$.
- Balancing wall tension against the pressure difference gives the thin-wall radius and profile in $d$ dimensions:

$$
R_{\rm tw}=\frac{d-1}{4\sqrt\beta\,\epsilon}\quad\Big(d=3:\ R_{\rm tw}=\frac{1}{2\sqrt\beta\,\epsilon}\Big),\qquad
S(r)\simeq\frac{S_c}{1+e^{(r-R_{\rm tw})/\sqrt\beta}} .
$$

- To leading order $R_{\rm tw}$ coincides with Eq. (46) of Kovtun, Nugaev and Shkerin (2018) for the same sextic family
  [checked], whose thin-wall treatment goes back to Coleman (1985).
- At $\beta=1/2$, $\omega^2=0.6$ one finds $R_{\rm tw}=7.07$; the charge radius of the computed profile is 7.41.

## 5.3 Three zones

**Interior** ($r<R_{\rm tw}-O(\sqrt\beta)$).
- With $S\simeq S_c$ the two channels mix into one propagating and one evanescent mode:

$$
k_c^2=\omega^2+\rho^2-d_c+\sqrt{4\omega^2\rho^2+s_c^2},\qquad
\kappa_c^2=d_c-\omega^2-\rho^2+\sqrt{4\omega^2\rho^2+s_c^2},
$$

  with $d_c=1+1/(4\beta)$ and $s_c=1/(2\beta)$.
- These are the interior solutions of Kovtun et al. (their Eqs. 51-53, spherical Bessel functions $j_{l+1/2}$ and
  $i_{l+1/2}$) [checked].
- Regularity at $r=0$ selects a standing wave $\propto \hat\jmath_l(k_c r)$ (Riccati-Bessel function) in the
  propagating mode.
- The standing wave is predominantly open-channel-like: $V/U\approx-0.16$ at the first zero of $\beta=1/2$. The closed
  channel is classically forbidden in the interior ($d_c>(\omega-\rho)^2$).

**Wall** ($|r-R_{\rm tw}|=O(\sqrt\beta)$).
- With $x=r-R_{\rm tw}$ the closed-channel potential of the planar wall is a Rosen-Morse II well:

$$
d_p(x)=1+\frac{1}{8\beta}-\frac{\tanh(\alpha x)}{8\beta}-\frac{9}{16\beta}\,\mathrm{sech}^2(\alpha x),\qquad
\alpha=\frac{1}{2\sqrt\beta}.
$$

- Its ground state is known in closed form (verified by substitution of
  $\psi_0=\cosh^{-A/\alpha}(\alpha x)\,e^{-Bx/A}$):

$$
E_w=1+\frac{1}{8\beta}-A^2-\frac{B^2}{A^2},\qquad A=\tfrac12\Big(-\alpha+\sqrt{\alpha^2+\tfrac{9}{4\beta}}\Big),\qquad
B=-\frac{1}{16\beta}.
$$

- For $0.35\le\beta\le0.60$ this well binds exactly one state; at $\beta=1/2$, $c_w\equiv\sqrt{E_w}=0.7993$.
- This is the "trapped" state of the Feshbach picture. Switching off the channel coupling in the full radial problem
  indeed continues the breathing pole into a bound state of the closed channel.
- The coupling $s_p=S(6\beta S-2)$ changes sign inside the wall at $S=1/(3\beta)$. That fixes the internal structure of
  the source, not the existence of zeros.

**Exterior.** $U\propto\sin(qr+\delta)$, $V\propto e^{-\kappa r}$.

## 5.4 Phase-matching condition

- To leading order in $\sqrt\beta/R_{\rm tw}$ the wall problem is planar and independent of $R_{\rm tw}$.
- The radius enters the matching in only two ways:
  - through the phase $\Psi\equiv k_cR_{\rm tw}$ with which the regular standing wave arrives at the wall
  - through an overall factor of the evanescent interior component, which is absorbed into its free amplitude
- The three exterior conditions are therefore linear in $(a\sin\Psi,\ a\cos\Psi,\ b)$ with $R$-independent
  coefficients.
- Eliminating the amplitudes leaves, besides the resonance condition $\rho\simeq\omega+c$, a condition that is periodic
  in $\Psi$ with period $\pi$ (since $a\to-a$ gives the same solution):

$$
\boxed{\;k_c(\omega_n^*,\rho_n^*)\,R_{\rm tw}(\omega_n^*)=\pi\,\big[n+\theta(\epsilon_n)\big],\qquad
\mathrm{Re}\,\rho_n^*=\omega_n^*+c(\epsilon_n)\;}
$$

- Equivalently, in Feshbach form, the coupling of the wall state to the open continuum behaves as

$$
g(\omega)\;\propto\;|F_w|\,\sin\!\big(\Psi(\omega)-\pi\theta\big),
$$

  where $F_w$ is the $R$-independent form factor of the wall source $s_pV_w$.
- Radiation cancels whenever the wall sits at a particular phase of the interior standing wave.
- For $l>0$ the regular wave carries the Riccati-Bessel offset, and the condition applies to
  $\Psi-l\pi/2+\delta_l(\Psi)$ with $\delta_1=\arctan(1/\Psi)$ and $\delta_2=\arctan\!\big(3\Psi/(\Psi^2-3)\big)$.

**Derived versus calibrated.**
- Derived: $R_{\rm tw}$, $k_c$, the bare wall state $c_w$, the period $\pi$, and the sign structure of $g$.
- Calibrated:
  - the wall phase $\theta(\epsilon)$, written as $\theta_\infty+\theta_1\epsilon(+\theta_2\epsilon^2)$; a term linear in
    $\epsilon\propto1/R$ is the natural curvature correction
  - the dressed wall-state energy $c(\epsilon)$, which contains a level shift $\delta c$ caused by the channel coupling
- At $\beta=1/2$ a fit to $n=5,7,8,9$ gives $\theta=0.6576+0.3341\,\epsilon$ (residuals $\le6\times10^{-5}$), and
  $c=\mathrm{Re}\,\rho^*-\omega^*$ decreases toward $c_\infty\approx0.80$-$0.82$.
- Deriving $\theta$ and $\delta c$ requires the planar two-channel wall problem *with* coupling, which has not been
  solved.

## 5.5 Consequences

1. **Alternating winding numbers.**
   - Near the wall state the two real components of the test map behave as $c_0(\rho-\rho_c)$ and
     $s(\omega)\propto g(\omega)$.
   - The sign of the Jacobian therefore follows $\mathrm{d}s/\mathrm{d}\omega^2$, which alternates between consecutive
     zeros of $\sin(\Psi-\pi\theta)$.
   - Consequence: consecutive zeros carry opposite winding numbers, $(-1)^n$ in our convention. This holds wherever the
     winding has been resolved, for $l=0$, for $l=1,2$, and on the counter-rotating branches of the two-component ball.
2. **Curvature of the width.**
   - From $\Gamma\simeq\Gamma_{\rm env}\sin^2(\Psi-\pi\theta)$,

$$
\Gamma\simeq C_n\,(\omega^2-\omega_n^{*2})^2,\qquad
C_n=\Gamma_{\rm env}\Big(\frac{\mathrm{d}\Psi}{\mathrm{d}\omega^2}\Big)^2\propto(n+\theta)^4 .
$$

   - At $\beta=1/2$ the measured $C_n$ (1.08, 8.8, 35.6 at $n=1,2,3$; about 750, 1210, 1830 at $n=7,8,9$) correspond to
     $\Gamma_{\rm env}\approx5.9\times10^{-3}$ for $n=3$ to $9$ (and $4\times10^{-3}$ at $n=1$).
   - So one envelope accounts for a variation of $C_n$ over three orders of magnitude.
3. **Accumulation and limiting step.**
   - Since $\Psi\propto k_c/\epsilon$, the zeros accumulate at the thin-wall threshold as $\epsilon_n\simeq k_c/[2\sqrt\beta\,\pi\,(n+\theta)]$, i.e.

$$
\frac{1}{\omega_n^{*2}-\omega_c^2}\simeq b_\infty\,(n+\theta_{\rm eff}),\qquad b_\infty=\frac{2\sqrt\beta\,\pi}{k_\infty},
$$

     with $k_\infty$ evaluated at $\omega_c$ and $\rho_\infty=\omega_c+c_\infty$.
   - At $\beta=1/2$ the bare wall state gives $b_\infty=2.334$. The calibrated level shift gives 2.298.
   - The measured steps approach $\approx2.305$. Within the model this corresponds to $c_\infty\approx0.82$, i.e. a level
     shift $\delta c\approx0.02$ above the bare value.
   - Finite data do not establish a limit theorem; the "$1/n$ accumulation" is an asymptotic statement of the model with
     numerical support.
4. **Absence without an interior barrier.**
   - The mechanism needs a closed-channel state bound *at the wall*, i.e. an interior that is classically forbidden for
     the closed channel, $d_p(S_0)>(\omega-\rho)^2$.
   - This fails in $d=1$ over the computed range and for the logarithmic potential $U=\ln(1+S)$, where
     $d_p=(1+S)^{-2}<1$. In neither case were zeros seen.
   - It also fails for the Petrov droplet model of MESS-1, where no ladder was found (a prediction made before that
     computation).
   - A thin-wall limit (a minimum of $U/S$) forces a sign change of $U''$ inside the wall. Plateau, wall well and
     barrier therefore appear together.
5. **Higher angular momentum.**
   - With the Riccati-Bessel offset and a centrifugal shift of the wall state, blind predictions for $l=1,2$ located 4 of
     5 zeros within their stated bars. The fifth, at the edge of the $l=2$ window, was allowed to fail by a rule stated
     in advance.
   - All 5 winding numbers were correct.
   - All measured positions lie below the predictions (by $-0.0007$ to $-0.0066$), so the ansatz for the $l$-dependent
     wall phase is biased.
6. **Second ladder and two-component balls.**
   - For the counter-rotating mode of a second field component the closed-channel state is the rotation mode $\propto f$.
     It fills the ball rather than sitting at the wall.
   - The source is then a filled sphere, and its form factor vanishes near the zeros of $j_1(k_aR)$.
   - For $l=1$ the Lommel overlap of two $j_1$ functions vanishes near $k_aR\simeq m\pi$, half a step below.
   - In the two-component ball at $g=0.2$ the $l=1$ counter-rotating branch has seven resolved zeros with alternating
     winding. Three blind predictions of their positions were hit (offsets $-2.3$ to $-2.6\times10^{-3}$, bars $\pm4\times10^{-3}$).
   - The same prediction's model of the existence window and of $\mathrm{Re}\,\nu^*$ (an interior level shift $\approx1.5gS$)
     was refuted: the branch extends to $\omega^2\approx0.674$, not 0.54.
   - The co-rotating partner (the spin-dipole mode proper) is bound at all 19 computed points.

## 5.6 Tests of the description

| test | basis | outcome |
|---|---|---|
| fit, $\beta=1/2$, $n=5$-9 | $\theta_\infty,\theta_1$ from $n=5,7,8,9$ | residuals $\le6\times10^{-5}$ in $\theta$; with 3 constants per $\beta$ fitted at $n=2$-4, all 7 unfitted zeros with $n\ge5$ within $4\times10^{-5}$ in $\omega^2$; $n=1$ off by $1$-$4\times10^{-3}$ |
| MOD-2, $\beta=1/2$, $n=10$-15 | frozen predictions from $n\le9$ only | $n=11$-15 within stated bars ($\pm2.5$-$5\times10^{-5}$); **constant offset $-1.9$ to $-2.0\times10^{-5}$** (model high); measured positions are width minima from three-point grids (signed square root), without winding test |
| SP-1, $l=1,2$ | frozen predictions | 4/5 positions, 5/5 winding numbers; systematic negative offset |
| SD-1, two components, $l=1$ | frozen predictions | ladder part (positions, alternation, step) hit; existence window and frequency refuted |

- The two blind arms that predicted $n=11$-15 (MOD-2 and the empirical ladder formula) were evaluated on the same
  target computations. They are not independent replications, and the formula arm was updated sequentially.
- The constant offset of MOD-2 is most simply absorbed by a shift of $c$ by $\approx10^{-3}$ or an equivalent change of
  $\theta$; the data do not distinguish the two.

## 5.7 Relation to known mechanisms

- **Nonradiating sources.**
  - That a localized oscillating source does not radiate when its Fourier component on the radiation shell vanishes is
    classical. Schott (1933) discussed radiationless motions of a charged spherical shell at $kR=n\pi$; see also Bohm
    and Weinstein (1948) [to verify].
  - The phase condition above is a dynamical realization of this condition for the wall source of a Q-ball, with the
    wall phase replacing the bare $kR=n\pi$.
- **Friedrich-Wintgen.**
  - Friedrich and Wintgen "suggested that BICs may appear from the destructive interference of two resonances coupled to
    a single radiation channel". Yu and Lu (2025) proved existence in the original three-equation system; their
    reduced model imposes two real conditions $N(s,\lambda)=D(s,\lambda)=0$ [checked].
  - The present case involves one wall state, not two interfering resonances. The cancellation is between two paths of
    the same state (direct emission from the wall and emission via the interior standing wave). The counting (two real
    conditions) is the same.
- **Topological charge.**
  - Zhen et al. (2014): a BIC is where both far-field components vanish; they "carry conserved and quantized
    topological charges", and "annihilation of BICs is only possible when charges of opposite signs are present"
    [checked].
  - Here the test map $W=L(y_a)+iL(y_b)$ plays the role of $c_x+ic_y$ on the plane $(\mathrm{Re}\,\rho,\omega^2)$. The
    ladder is a chain of alternating charges.
  - Under smooth deformations ($\beta$, dimension, coupling $g$) zeros can therefore only disappear in pairs or at the
    boundary of the domain.
- **Q-ball perturbation theory.**
  - The interior solution is that of Kovtun et al. (2018) [checked]; their matching treats bound modes, ours the
    embedded case with an outgoing condition.
  - Feshbach-type quasinormal modes of Q-balls in 1+1 dimensions: Evslin et al. (2026) [checked, abstract].
  - Near-field and single-frequency quasinormal modes: Ciurla et al. (2024) [cited via our literature report; to verify].

## 5.8 Figure proposal (Fig. 3: three zones)

- **Panel (a):** background $S(r)=f^2$ at $\beta=1/2$ for the first zero ($\omega^2=0.797677$) and for $n=5$
  ($\omega^2=0.582417$), with $R_{\rm tw}$ marked and the logistic thin-wall profile overlaid.
  - Data: `bic2.py` routine `profil()` at the stated $\omega^2$, or Codex's R44 profile files
    (`resonance-20260930/feshbach-20260930/profile-arm-*.npz`).
- **Panel (b):** $d_p(r)$ and $s_p(r)$ with the Rosen-Morse approximation of the wall well, and the energy lines
  $(\omega\pm\rho)^2$.
- **Panel (c):** the radiationless eigenfunction $U(r)$, $V(r)$ at the same points.
  - The standing wave inside, the wall-bound $V$ and the vanishing outgoing $U$ should be visible.
  - Data: not stored. The `exakt.json` files keep poles, amplitudes and tables, but no eigenfunction arrays (keys
    checked). One short run of `bic2.py` (routines `direkt_m`/`eigen` at the pole) is needed.
  - For $n=1$ the certified solution data of the computer-assisted proof can serve as a cross-check.
- Colour the three zones; mark the sign change of $s_p$ at $S=1/(3\beta)$.

## 5.9 What the model does not explain

1. The values of the wall phase $\theta(\epsilon)$ and of the level shift $\delta c$. Both are fitted; the planar
   two-channel wall problem with coupling is not solved.
2. The constant offset of about $-2\times10^{-5}$ in the blind predictions for $n=11$-15, and whether it resides in
   $\theta$ or in $c$.
3. The thick-wall zeros ($n=1$, and $n=2$ to a lesser extent): errors of $10^{-3}$ in $\omega^2$ at $n=1$.
4. The size of the $l$-dependent wall phase: the $l>0$ predictions are biased low.
5. The existence window and the frequency of the counter-rotating $l=1$ branch in the two-component ball: the
   interior-level model was refuted. The wall minimum of $U'(S)$ in that channel, which the model ignored, is a likely
   reason.
6. Whether every width minimum is an exact zero. Exactness is established only by winding tests at the resolved points
   and by the computer-assisted proof for $n=1$. The zeros at $n\ge7$ are width minima.
7. Whether the ladder is infinite. The model predicts accumulation at $\omega_c^2$, but no theorem is available.
8. Anything nonlinear. Second-order sources at $\omega\pm2\rho$ are open, and the leakage observed at $n=1$ scales with
   the fourth power of the amplitude. The model says nothing about lifetimes or stability.
9. Transfer to experiments. Systems without a wall-bound closed-channel state (e.g. the Petrov droplets examined) are
   not expected to show the ladder.

<!-- End: see next line (date measured after writing). -->

<!-- End: 2026-09-30 10:27:31 CEST (date, measured after writing). -->
