# Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls

**Finn Hinrichsen — preprint version 0.53, 30 October 2026** (released 31 October 2026). Not peer reviewed. Release
[`qball-bic-v0.53`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.53). This is the current version;
versions 0.52 and 0.51 remain unchanged in [`../qball-bic-ladder-v0.52/`](../qball-bic-ladder-v0.52/README.md) and
[`../qball-bic-ladder-v0.51/`](../qball-bic-ladder-v0.51/README.md).

*Kurz auf Deutsch:* Preprint zu lokalisierten linearen Moden eines Q-Balls (komplexes Skalarfeld, sextisches Potential,
drei Raumdimensionen). Neu in 0.53: die erwartete Leiter als ausdrückliche Vermutung mit den fehlenden Beweisbausteinen,
ein Teil „Limitations and open problems“, eine numerische Auswertung der Ladungssteigung dQ/dω an den drei bewiesenen
Hintergründen, eine Matching-Rechnung, die die Indizes 5 und 11–14 auf aufgelöste numerische Windungen hebt, das
Begleitarchiv Revision 3 und eine kürzere Widmung. Kein Zertifikat, Lemma oder Einschluss ist geändert. Drei
Existenzaussagen sind computergestützt mit Intervallarithmetik eingeschlossen; alles Übrige ist numerische Evidenz oder
bedingte Aussage. Nicht begutachtet, keine Messdaten. Text und Daten CC BY 4.0, Code MIT.

![Figure 1 of the preprint: a Q-ball, the balance of terms, open and closed channels, and the ladder of radiation zeros](qball-overview.png)

*Figure 1 (overview, unchanged from 0.52).* (a) Density profiles of stored backgrounds and the thin-wall formula;
(b) Coleman's mechanical picture; (c) the two sidebands of an excitation, one open (can radiate) and one closed; (d) at
C0 the open-channel tail cancels (stored numerical reconstruction, not a pointwise enclosure); (e) locations of the
l = 0 sequence through n = 18 and of C2 by the evidence classes of preprint 0.52: computer-assisted proofs for C0, C1
and C2, numerical candidates for n = 3–18. Panel (e) still shows n = 5 and 11–14 with weaker evidence; their updated
classes are in Table 2 of the paper, and their location changes are below the plotting resolution. The grey width
curve and the phase inset are schematic.

## Files

| File | Content |
|---|---|
| [`paper.pdf`](paper.pdf), [`paper.html`](paper.html) | main paper (28 pages) |
| [`supplement.pdf`](supplement.pdf), [`supplement.html`](supplement.html) | supplement, 43 pages (dependency audit, exploratory driving/formation material, numerical controls, charge slope in S7, archive structure and figure provenance) |
| `main.tex`, `supplement.tex`, `sections/*.tex`, `*.pdf` figures, `*.png` | TeX sources and figures used by the PDF/HTML build |
| [`qball-overview.pdf`](qball-overview.pdf), [`.png`](qball-overview.png), [`.svg`](qball-overview.svg) | Figure 1 (unchanged from 0.52); plotting script, receipt and inputs in [`../qball-bic-ladder-v0.52/fig-overview/`](../qball-bic-ladder-v0.52/fig-overview/README.md) |
| [`archive-r3/`](archive-r3/README.md) | description and manifest of the companion archive revision 3 (release asset) |
| `style.css`, `fonts/` | HTML style and the bundled, unmodified DejaVu Math TeX Gyre font; the font keeps its own licence (`fonts/DejaVu-COPYRIGHT.txt`, `fonts/FONT-PROVENANCE.txt`) and is not covered by CC BY 4.0 |
| [`CITATION.cff`](CITATION.cff) | citation metadata |
| [`LICENSE`](LICENSE), [`LICENSE-CODE`](LICENSE-CODE) | CC BY 4.0 (text, figures, data, certificates); MIT (code) |

The companion archive (proof code, certificates, selected records) is the release asset
`qball-bic-v0.53-archive-r3.zip` of release
[`qball-bic-v0.53`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.53) (SHA-256
`6980a82552063b05fccbfb9e71117d3ecd75d20f6a195dafc3269844e7878fb1`); description and checksums in
[`archive-r3/README.md`](archive-r3/README.md). Revision 2 remains the asset of release
[`qball-bic-v0.51`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51).

## Changes against preprint 0.52

* **Conjecture 1** (Section 6): the radial ladder and its limiting spacing stated explicitly, with quantifiers and the
  three missing proof ingredients. The word "classical" in the abstract.
* **Limitations and open problems** (part of Section 8): open nonlinear questions (circular polarization, radial
  second-harmonic coefficients, no lifetime), background stability and the computational trust base (one implementation,
  one interval library, no proof assistant; the analytic lemmas were examined only in internal, AI-assisted reviews).
* **Charge slope** (Supplement S7): numerical evaluation of dQ/dω at C0, C1 and C2; all three lie on the branch
  dQ/dω < 0, well below the minimum of Q(ω) at ω² ≈ 0.9272, with virial, cubic-NLS-limit and independent shooting
  controls. Under the hypotheses of the radial slope criterion, which are not independently verified, this bears only
  on a purely growing l = 0 instability; it is numerical, not an enclosure.
* **Matching calculation** (Section 5): boundary condition and outer-radius insensitivity of the matching map, and a
  calculation with a prespecified acceptance rule that raises indices 5 and 11–14 of Table 2 to resolved numerical
  windings.
* **Data availability** for archive revision 3, including the correction of the earlier sentence that no beta = 1
  records were included; a shorter dedication; a sentence on an external assessment in "Use of AI tools"; version line
  and revision note.
* No certificate, lemma, certified enclosure or figure image changed. Section, table and figure numbers are those of 0.52.

## What the paper claims, and what it does not

* **Computer-assisted existence (C0, C1, C2).** Three localized linear modes (two radial, l = 0; one dipole, l = 1) of
  the linearized two-channel equations are enclosed on the infinite radial domain: interval (ball-arithmetic) interior
  enclosures plus analytic exterior estimates. Trust assumptions: correctness of the proof code, of the ball-arithmetic
  library and of the analytic lemmas. For preprint 0.51 the three primary certificate runs were repeated with unchanged
  code; this is a reproduction of the same implementation, **not** an independent interval implementation.
* **Numerical sequence.** Further radial locations up to continuation index 18 are numerical candidates with the
  evidence classes listed in the paper's ladder table; they are not certified.
* **Thin-wall interpretation.** An independently computed planar transmission zero gives an unfitted spacing candidate.
  Identifying it with a radial limiting spacing remains open (Conjecture 1); an absolute-location test of the
  finite-order approximation failed and is reported.
* **Nonlinear statement (conditional).** A second-harmonic analysis separates one monopole outgoing coefficient from
  zero under explicitly audited exact-mode and enclosure hypotheses. It obstructs a specified uniformly localized smooth
  continuation for linked dipole polarizations with p·p ≠ 0; circular polarization needs a separate quadrupole
  certificate. No lifetime or stability theorem.
* No measured data are involved. The Supplement's driving, formation and response material is exploratory.

## Use of AI tools

Text, code, computations and internal reviews were produced with extensive use of Claude (Anthropic) and Codex (OpenAI)
under the author's direction. Gemini (Google) was used for an external assessment of preprint 0.52; its comments were
checked and prompted parts of this revision. See the corresponding section of the paper.

## Licence and citation

Text, figures, data and certificates: [CC BY 4.0](LICENSE). Code (proof code in the companion archive): [MIT](LICENSE-CODE).
Please cite: Finn Hinrichsen, *Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls*,
preprint version 0.53 (2026), https://github.com/fmhc/physics/releases/tag/qball-bic-v0.53.
