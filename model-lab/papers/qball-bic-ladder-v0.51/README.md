# Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls

**Finn Hinrichsen — preprint version 0.51, 29 October 2026.** Not peer reviewed. Release
[`qball-bic-v0.51`](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51).

> **Superseded by preprint 0.52** (same results, plus a dedication, a non-technical overview and an overview figure):
> [`../qball-bic-ladder-v0.52/`](../qball-bic-ladder-v0.52/README.md). Apart from this note, the folder is kept unchanged as the 0.51 record.

*Kurz auf Deutsch:* Preprint zu lokalisierten linearen Moden eines Q-Balls (komplexes Skalarfeld, sextisches Potential,
drei Raumdimensionen). Drei Existenzaussagen sind computergestützt mit Intervallarithmetik eingeschlossen; alles Übrige
ist numerische Evidenz oder bedingte Aussage. Nicht begutachtet, keine Messdaten. Text und Daten CC BY 4.0, Code MIT.

## Files

| File | Content |
|---|---|
| [`paper.pdf`](paper.pdf), [`paper.html`](paper.html) | main paper (21 pages) |
| [`supplement.pdf`](supplement.pdf), [`supplement.html`](supplement.html) | supplement, 40 pages (dependency audit, exploratory driving/formation material, numerical controls) |
| `main.tex`, `supplement.tex`, `sections/*.tex`, `*.pdf` figures, `*.png` | TeX sources and figures used by the PDF/HTML build |
| `style.css`, `fonts/` | HTML style and the bundled, unmodified DejaVu Math TeX Gyre font; the font keeps its own licence (`fonts/DejaVu-COPYRIGHT.txt`, `fonts/FONT-PROVENANCE.txt`) and is not covered by CC BY 4.0 |
| [`CITATION.cff`](CITATION.cff) | citation metadata |
| [`LICENSE`](LICENSE), [`LICENSE-CODE`](LICENSE-CODE) | CC BY 4.0 (text, figures, data, certificates); MIT (code) |
| [`archive-r2/`](archive-r2/) | manifest and description of the companion archive; the archive itself is a release asset |

## What the paper claims, and what it does not

* **Computer-assisted existence (C0, C1, C2).** Three localized linear modes (two radial, l = 0; one dipole, l = 1) of
  the linearized two-channel equations are enclosed on the infinite radial domain: interval (ball-arithmetic) interior
  enclosures plus analytic exterior estimates. Trust assumptions: correctness of the proof code and of the ball-arithmetic
  library. The three primary certificate runs were repeated for this revision with unchanged code; receipts agree
  except for four timing fields, all step records are byte-identical. This is a reproduction of the same implementation,
  **not** an independent interval implementation.
* **Numerical sequence.** Further radial locations up to continuation index 18 are numerical candidates with the
  evidence classes listed in the paper's ladder table; they are not certified. The index is a continuation label, not a
  certified node count.
* **Thin-wall interpretation.** An independently computed planar transmission zero gives an unfitted spacing candidate.
  Identifying it with a radial limiting spacing remains open; an absolute-location test of the finite-order
  approximation failed and is reported.
* **Nonlinear statement (conditional).** A second-harmonic analysis separates one monopole outgoing coefficient from
  zero under explicitly audited exact-mode and enclosure hypotheses. It obstructs a specified uniformly localized smooth
  continuation for linked dipole polarizations with p·p ≠ 0; circular polarization needs a separate quadrupole
  certificate. No lifetime or stability theorem; the charge slope dQ/dω at the certified backgrounds is not evaluated.
* **Literature position.** The paper delimits its results against the literature it cites and makes no global
  priority claim.
* No measured data are involved. The Supplement's driving, formation and response material is exploratory.

## Companion archive (release asset)

`qball-bic-v0.51-archive-r2.zip` (about 37 MB; 494 payload files plus `MANIFEST.sha256`, 495 files in total, under `archive/`) contains proof code, exact inputs, receipts
and step protocols of C0/C1/C2 with rerun instructions, a separate interval check (G11), ladder and planar-wall records,
mode-figure data, render receipts of the exploratory figures and the hash-closed record chain of the nonlinear
coefficient bound. Only the linear certificates are offered as a rerun; everything else is a record or a hash binding,
as listed in the archive's coverage table. Historical records were lexically cleaned (machine names, user paths, names
of individual AI agents replaced by neutral labels) with a complete historical-to-present hash map (`CLEAN-MAP.tsv`);
numbers were not changed. SHA-256 of the ZIP and of its `MANIFEST.sha256` are in [`archive-r2/README.md`](archive-r2/README.md).

## Changes against the internal staging build of 28 October 2026

Release edits only: author line, date and version line, data-availability statement (release identifier and
licences), the new section "Use of AI tools" in place of a placeholder, and two archive sentences in the Supplement.
No result, number, lemma or figure changed. The PDF/HTML were rebuilt with the same toolchain and the same document
checks (two checks that required staging markers were inverted into release-marker checks).

## Use of AI tools

Text, code, computations and internal reviews were produced with extensive use of Claude (Anthropic) and Codex (OpenAI)
under the author's direction; see the corresponding section of the paper.

## Licence and citation

Text, figures, data and certificates: [CC BY 4.0](LICENSE). Code (in the companion archive): [MIT](LICENSE-CODE).
Please cite: Finn Hinrichsen, *Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls*,
preprint version 0.51 (2026), https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51.

The earlier working versions remain in [`../qball-bic-ladder-20260930/`](../qball-bic-ladder-20260930/) as history.
