Geometric mode triplets and symmetry-compatible interactions
English translation of the German working draft v0.6a — 1 October 2026

BASIS
Frozen source-v0.6a.html copied before translation from
model-lab/papers/su3-geometric-triplets-20260930/paper.html.
SHA256: eb04ab2fa4c6f329db550c3dbe3b15f9ce32fb0347918654fba46429989c51c0.
INPUTS.sha256 binds the German manuscript, its figure, the complete received
Anthropic review (including its v0.6a follow-up), and saved figure data.
SOURCE-SHA256SUMS.txt is the unchanged source manifest accompanying the
German manuscript, not a newly regenerated audit of every upstream file.

TRANSLATION BOUNDARY
Codex (OpenAI) translated the complete German v0.6a into English HTML and
LaTeX. Scientific claims, numbers, limitations and literature-reading scopes
come from that source. The added translation provenance and document links
are editorial additions. No fresh literature search or proof audit is claimed.
The received Anthropic review is a project-internal review across AI providers,
not journal refereeing. Its new v0.6a checks were limited as documented there.
The separately proposed Schur/leakage supplement and newer BIC-ladder findings
are not imported into this translation. No new scientific claim or run.

The previous v0.5 delivery remains unchanged in the parent directory. This
v0.6a directory is the revised English reading version, not an overwrite
of the German original or the separately owned -en review directory.

REVIEW RESPONSE
W1–W5 and K1–K17: follow the revised German v0.6a, including the static
six-direction sum versus the noninvariant independent-neighbour network,
prescribed shell control model, new outline/conclusion, corrected rounding,
model notation and explicit literature roles. Optional unverified symmetry
claims have not been added by the translator.
K11: explicitly name the triplet as the object treated in isolation.
E2: criterion/acceptance criterion, parameter settings/runs and Computation;
avoid internal gate/arm terminology and host names in the paper narrative.
E3: numbered LaTeX sections/subsections, labels and linked references,
thebibliography/cite and equation references; PDF bookmarks.
E4: larger figure text, legends below axes, distinct population/energy labels,
neutral titles. Render from the unchanged saved FIGURE-DATA.json only.
E5: source version, translation by Codex (OpenAI), path and hash in the
document provenance. No invented human author list or review claim.
v0.6a N1/N2: retain the corrected boundary term -u(8)^2/16, the contractible
unrestricted configuration space, and the separate fixed-charge reduction
caveat. Do not turn the latter into evidence for spin one-half.

FIGURE
The input JSON is byte-identical to shell-detuning/RESULT.json, SHA256
7ce6dbf45326981a52d86708f4b3bc551a34ca115dcba5bfcc90c44c056f1b37.
plot-english.py redraws stored scan points, mode-population samples and the
three stored spatial-energy samples. No solver, fit or new physical data.
transfer-detuning-source.svg preserves the German figure; the English SVG,
PDF and PNG contain translated labels and the revised layout.

EXECUTION
All rendering and document QA on ubuntu-auto (.69), CPU core 11, nice 19,
after checking load and memory. Existing private TeX/Pandoc/Poppler tools
and the existing Python environment were used. No local interpreter, test,
compiler or browser start, no CUDA physics, installation, service or hook.
build-remote.sh records the remote build procedure with no-shell-escape.
Remote workspace:
/home/fmh/fmhc-physics-remote/paper-english-v05-20260930/v0.6a/

STATUS
Complete English HTML, LaTeX, 12-page A4 PDF and browser PDF.
Automated document QA on .69 checks all eight tables, all precise decimal
values, fifteen equations and the original bibliography links. HTML has
no horizontal overflow, missing figure or browser error. LaTeX has 31
resolved labels and 17 PDF bookmarks, with no overfull boxes, missing
characters, duplicate targets or unresolved references in the final log.
All twelve PDF pages, the HTML opening and its figure were visually read.
The title break was adjusted to avoid splitting 'interactions'.
An additional OpenAI context independently read the complete source and
both translations; REVIEW-TRANSLATION-V06A.txt records its bounded verdict.
The final wording uses 'cube graphs' (not the broader 'cubic graphs') and
'particle number'. This is a translation review, not a new physics audit.

One inherited wording issue is recorded separately: section 6.1 calls the
construction an action while equation (11) displays the Lagrangian. It was
preserved in translation, not silently changed or treated as a new result.
All source/translation/build boundaries remain in the accompanying notes.
