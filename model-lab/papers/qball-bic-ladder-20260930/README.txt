CURRENT ACCEPTED WORKING DRAFT: v0.45, 4 October 2026
Author: Finn Malte Hinrichsen, Hamburg, Germany.
Local working manuscript, not submitted or publicly released.

The three reproducibility locators are included in main.tex, PDF and HTML.
Completed .69 document QA: 53 PDF pages, 1157 MathML elements, all 17 figures
loaded; no overflow, missing anchors, raw-math spans or browser errors.
The HTML path repair preserves 79 distinct paths / 99 occurrences and passes
the eight bound regression cases. Displayed authorship is correct; PDF Author
metadata is not populated. Existing PDF was reused from three completed TeX
passes; the successful HTML/QA retry took 45.193 s wall / 9.145 s CPU.
Root visually inspected the title pages and changed PDF inventory page 49.
Independent export/result review completed. Earlier failed/incomplete attempts
remain recorded; no scientific claim, formula, tolerance or figure changed.
Evidence: coordination/resonance-20260930/wall-correlated-20261003/
paper-inventory-v45/ROOT-ACCEPTANCE.txt and html-path-fix-v3/completed/.

HISTORICAL STAGING AND PREVIOUS-VERSION RECORD BELOW.
Statements of pending v0.45 build/promotion below describe earlier stages
and are superseded by the current acceptance above.

Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls
Working manuscript v0.45, 4 October 2026 — staged sources; build and document QA pending
Author: Finn Malte Hinrichsen, Hamburg, Germany (explicit user instruction).
No institutional affiliation asserted. No submission or public release performed.

Source v0.44, 3 October 2026 evening: APPENDIX-DRIVING.tex now
states the separate vanishing-tail requirement for additional open channels
and the limitation of a leading-order source-overlap zero. This paragraph
is included in the v0.44 PDF/HTML and independently reviewed. No coupled-pilot
result is added as a physics finding.

Source v0.45, 4 October 2026: reproducibility inventory now explicitly
locates the Gauss finite-correlation comparison, exterior-domain sensitivity
and signed lag-kernel diagnostic. The earlier failed finite-correlation row
is retained unchanged. This is a source-only staging revision; no v0.45
PDF/HTML, document QA, promotion or new physics result is claimed.

READ
paper.pdf — primary numbered LaTeX reading version.
paper.html — browser version with local MathML/figures.
main.tex + sections/*.tex — editable manuscript sources.

SCOPE
Three concrete linear existence enclosures; fifteen reported radial candidate
locations with different evidence levels; sequential predictions and a calibrated
thin-wall description; nonlinear source expansion, prior n=1 radiation evidence,
and a numerical T2 dipole second-harmonic response with explicit input limits.
No infinite-ladder theorem, no linear/nonlinear stability or particle-identification claim.
No new physics/ODE calculation performed to assemble this manuscript.
The nonlinear algebra check referenced in the paper is separately documented.

REVIEW
MANUSCRIPT-REVIEW.txt: separate OpenAI context reviewed the assembled content;
its literature subsection is that reviewer's own work, so not independently
reviewed by that same context. The coordinator read all supplied sections.
Two wording recommendations were adopted: particular instead of isolated parameter
values, and bare closed-channel wall state rather than solved coupled wall state.
Existence proof components separately carry OpenAI/Anthropic internal reviews.
These are not external journal refereeing and not a second interval implementation.

BUILD AND QA
Current v0.44 build: /home/fmh/fmhc-physics-remote/paper-bic-v44-20261003/.
Build and document QA passed on .69 CPU11 nice19, one thread:
52 pages, 1157 MathML elements, all 17 images loaded, no overflow,
missing anchors, raw math fallback or browser errors. Build used 21.31
CPU-s and 23.50 wall-s. Root visually checked the changed PDF page 37.
Acceptance: wall-correlated-20261003/paper-channel-v44/ROOT-ABNAHME.txt
under coordination/resonance-20260930/. INPUTS.sha256 records the immutable
build inputs; this README status update follows the build and is not one
of those frozen inputs. The staged README preserves that earlier status.
Source stage and BUILD-PLAN.txt: coordination/resonance-20260930/
wall-correlated-20261003/paper-channel-v44/.
Existing figures are copied without regeneration. The legacy MathML QA
baseline was recovered byte-identically from paper-v38-literature/build/;
its hash matches the inherited source manifest. No physics run is included.

Previous v0.43 build: /home/fmh/fmhc-physics-remote/paper-bic-v43-20261003/.
Root document QA passed on ubuntu-auto (.69), CPU11 nice19, one thread:
52 pages, 1157 MathML elements, 17 loaded images, no overflow, unresolved
references, missing anchors, raw math fallback or browser errors.
Build used 20.45 CPU-s; literature PDF page visually checked separately.
Acceptance: coordination/resonance-20260930/literature-novelty-20261003/ROOT-ABNAHME.txt.
No local interpreter/compiler/browser starts or new physics calculation.
Previous v0.42 build: /home/fmh/fmhc-physics-remote/paper-bic-v42-20261003/.
Root v0.42 document QA passed; the records below describe earlier versions.
Previous acceptance record: coordination/resonance-20260930/
paper-v42-beta1/ROOT-ABNAHME.txt.
That record reports 1152 MathML elements and 17 loaded figures, with no
overflow, unresolved references, missing anchors or browser errors.
The manuscript is 52 pages; document QA is not scientific acceptance.
The v0.39 addition describes a separate radial M1 relaxation study. Two
individual Gaussian starts pass its charge--frequency diagnostic, but
the predeclared combined formation criterion was not met. No exact
stationarity, nonspherical stability or capture from unbound radiation
is inferred. The source review is a document review, not a trajectory
reproduction. New M2 time-domain results are not inserted into this M1 paper.
The v0.26--v0.37 additions were not recorded in this README as they occurred.
Their source/build records remain in the separate stages; no retrospective
claim of a newly performed review or build is made by this status correction.
PS-3 literature corrections are incorporated in this draft: the FLS part of
Azatov et al., the established interior dispersion of Zhang/Zhou/Zhu, and
real-field oscillon decay minima. They do not extend the existence claims.
Eight section files remain outside Git tracking; their inventory and hashes
are in coordination/resonance-20260930/paper-v38-literature/UNTRACKED-SECTIONS.sha256.
Git inclusion belongs to the coordinated snapshot, not this README correction.
Historical v0.17: 30 pages, 699 MathML elements, eight loaded figures; Root QA passed.
pdfTeX uses -no-shell-escape. Document QA checks author, resolved references,
no overfull boxes, loaded HTML figure, MathML, anchor targets, browser errors.
DOCUMENT-QA.json and build-3.log record the actual result; paper-v10/
BUILD-OBSERVATION.txt distinguishes the initial line-wrap assertion failure
from the successful second document check. The final rebuild then incorporated
the last text and method-citation changes; BUILD-REVIEW-ROOT.txt records acceptance.
plot.py uses figure-data.json only; reported numbers, no new fit, no invented errors.

BEFORE SUBMISSION
A complete draft is not a submission-ready research package. Provide a durable
public supplementary archive, code/data license and environment instructions;
reconcile all figure/source versions; finish full external scientific review and
publication decision. Stronger operator-theoretic, nonlinear and infinite-ladder
claims would require new results, not an editorial change. Authorship is now fixed
by Finn's instruction, but submission has not been authorized by this task.

REVISION 0.2 (30 September 2026)
Added a limited bell-mode analogy, an explicit distinction between spatial tails
and interaction range, and environmental/formation questions. The original action
contains no electromagnetic coupling: no CMB interaction rate is inferred.
Condensate fragmentation literature is an adjacent mechanism, not evidence of
formation in this model or a universal wavelength ratio. The existing n=1
nonlinear evidence is distinguished from the unevaluated additional cases.
Numerical claims, certificate values and figure data are unchanged.
Updated PDF: 14 pages. Remote assembly paper-bic-v02-20260930; final TeX pass
and document-qa.py passed (253 MathML elements, no missing anchors or errors).
The initially missing TeX/Pandoc search paths were corrected only for the build
commands; no system configuration, wrapper or service was installed.
Supporting editorial review: function-implementation/ENTWURF-GLOCKEN-UMWELT.txt
and MODELCODE-REVIEW.txt. Kasuya/Kawasaki v3 was read at the original text,
model equations and fragmentation discussion; no parameter imported from it.

REVISION 0.3 (30 September 2026)
Added two reviewed outlook cautions: a high-density periodic region must be
checked for closed paths winding around the box before calling it an isolated
island; a mediator's nonlocal static response differs from temporal memory.
These are proposed diagnostics and model-extension caveats, not new paper
results. No BIC claim, certificate, numerical coefficient or figure changed.
Independent text review: coordination/resonance-20260930/formation-nonlinear-3d/
PAPER-V03-EDITORIAL-REVIEW.txt. Assembly and QA on .69 CPU passed: 14 pages,
253 MathML elements, no missing anchors, browser errors or overfull boxes.

REVISION 0.4 (30 September 2026)
Added an elementary energy-charge identity and global rest-density bound to
the formation outlook. For closed data with E<|Q|, persistence is energetically
biased and cannot alone establish localized stationary Q-ball formation.
No simulation numbers, BIC assertions, certificate values or figures changed.
Independent algebra/text review: coordination/resonance-20260930/paper-v04/REVIEW.txt.
Remote PDF/HTML build and QA passed:14pages,263MathML, no missing anchors,
browser errors or overfull boxes. The first Pandoc invocation lacked the
final /data path; fixed only in that build command, no system configuration.

REVISION 0.5 (1 October 2026)
Integrated the separately reviewed T2 forced second-harmonic calculation:
four nonzero numerical outgoing amplitudes on the prescribed comparisons,
with a power table in the common radial L2 normalization. This is an
approximate-input result, not a transfer of the exact linear certificate
or a lifetime measurement. Abstract, nonlinear section, outlook, conclusion
and provenance now agree. The exact-input/exterior error transfer remains
open; T1 response remains unevaluated. No new simulation during assembly.
Review: coordination/resonance-20260930/paper-v05/REVIEW.txt; its remaining
wave-number sign-convention wording was replaced by the neutral statement
that both physical sidebands transport positive energy with the specified
outgoing conditions. Old source snapshots are in paper-v05/before/.
PDF/HTML build and QA on .69 CPU11 passed:15pages,279MathML expressions,
no missing anchors, overfull boxes or browser errors; figure loaded.
Private library/font/data paths were set only in build-command environment;
no system configuration, installation, service or wrapper was added.

REVISION 0.6 (1 October 2026)
Added the separately reviewed fixed-weight source-current check for T2,
without refitting its boundary coefficients. Empirical volume/current
residuals are distinguished from energy-power coefficients and certified
error bounds. Outlook updated; exact input/exterior transfer remains open.
Bell/environment/formation passages rechecked for consistency.
Review: coordination/resonance-20260930/paper-v06/REVIEW.txt.
Build and browser QA .69 CPU11: 15pages,289MathML, no missing anchors,
overflow, unresolved references or browser errors. No new simulation during
paper assembly; separate Green diagnostic provenance remains unchanged.
Initial pdftotext PATH lookup failed after successful TeX/Pandoc generation;
retried using existing private binary. No system install/configuration.

REVISION 0.7 (1 October 2026)
Added exact angular identities for complex dipole polarization and a
conditional continuation obstruction. Circular polarization removes the
oscillatory monopole source but not the full quadrupole source. An exact
radial quadrupole nonzero certificate would cover all nonzero polarizations
in that one linked radial eigenspace; the certificate remains open.
The uniformly localized C2 continuation class and allowed detunings are
explicit. No numerical table, existence certificate or figure was changed.
Independent insert and integrated-diff reviews are in paper-v07/.
Build/QA on .69 CPU11 passed:16pages,314MathML, no missing anchors,
figure load errors, overfull boxes or browser errors. Root checked the
PDF first-page preview and new extracted text before updating canonical
PDF/HTML/text together. No physics simulation or public submission.

REVISION 0.8 (1 October 2026)
Added the complete conditional L0 second-harmonic coefficient enclosure at
T2: shared error <0.001023269269845280, fixed comparison modulus
>0.001582591541472706, resulting exact-mode coefficient bound
>0.000559322271627427 under the inherited T2/span/enclosure hypotheses.
The stronger channel is the negative physical sideband. Jost normalization
is explicit; the old approximate unit-L2 power table is not recertified.
A separately reviewed ODE/origin argument establishes background and
tangent membership in H4_gamma with gamma=1/10. The excluded nonlinear
families still require C2 dependence in that fixed weighted space.
Circular polarization, exact L2 response, lifetime and instability remain
open. No new physics simulation during assembly. Bell/environment/formation
passages retain their limited scope. Text and final regularity reviews:
coordination/resonance-20260930/paper-v08/INTEGRATED-REVIEW*.txt.
PDF/HTML QA on .69 CPU11 passed:16pages,327MathML,no missing anchors,
no overfull boxes or browser errors. Root inspected new PDF page12.
Source binding, tool hashes, logs and generated artifacts are in paper-v08/stage.

REVISION 0.9 (1 October 2026)
Added a reviewed conditional linear source-projection identity derived from
this model's time equation. An initially projection-free homogeneous packet
cannot populate the localized mode on the fixed background; a prescribed
local physical source can have a nonzero adjoint overlap. The doubled source
obeys conjugation pairing. Positive modal norm is not global passivity or
an environmental energy/cosmological maintenance claim. Other results unchanged.
Evidence: paper-v08/PENCIL-NORM-UMWELT and independent review; final English
ENVIRONMENT-PROJECTION-DRAFT and review; paper-v09/STAGE-REVIEW and BUILD-REVIEW-ROOT.
Built on .69:17PDFpages,359MathML elements, no unresolved anchors/overfull
boxes/browser errors. Root visually checked new PDFpage14. v0.8Stage retained.

REVISION 0.10 (1 October 2026)
Primary literature added for model provenance (Battye/Sutcliffe), established
radial equations (Azatov et al.), small-amplitude paired modes (Evslin et al.),
embedded-soliton accumulation (Malomed et al.) and nonlinear FGR context
(Soffer/Weinstein), with differences in models and theorem scope explicit.
Candidate table/figure values now use the audited data package with C0/C1
certificate updates. A06 unconverged and A10 untested status remain visible.
Inherited exact-mode, Jost-span, normalization and exterior hypotheses are
listed explicitly. New prescribed-pulse overlap and finite detuning bound
are conditional linear excitation statements, not formation or longevity.
Exploratory 2D and additional-neutral-channel probes have narrower evidence
status than the interval existence certificates; Born cancellations are not
coupled BIC proofs. Historical source reading and final rereading are
separated in PROOF-SOURCES-ADDENDUM.txt. No physics job during paper assembly.
First document build:20pages,442MathML, document QA passed after whitespace
normalization in one expected-text check. Root viewed the updated figure.
Final text and method-citation reviews are complete. Final rebuild and document
QA passed on .69 CPU11:20pages,442MathML,no missing anchors, browser errors,
overflow or overfull boxes. Root inspected rendered PDF pages13,14,17,
including the inherited hypotheses, coefficient bound and pulse/channel text.
Source and build-input hashes were rechecked. This is a working manuscript,
not an external scientific acceptance or a public submission.

REVISION 0.11 (1 October 2026)
Three added color figures: spherical C0 amplitude cutaway; T2 dipole3D
isosurfaces and phase sections at three linear phases; C0 parameter-space
residual loops with phase winding and an offsetcontrol. These use stored
numerical radial solutions with exact spherical harmonics/time factors,
not a new nonlinear3D simulation. Display reconstructions are not certified
pointwise eigenfunction arrays. Figure hashes/data audit and renderreviews:
coordination/resonance-20260930/paper-v11-figures/.
Added independently reviewed analytic two-pulse prediction for canceling
one previously driven linear modal projection, retaining source pairing and
labphase condition. No performed de-excitation experiment/PDEtest; no claim
that all modes/radiation or the charged background become stationary.
Current build /home/fmh/fmhc-physics-remote/paper-bic-v11-20261001/ on .69CPU11.
DocumentQA23pages,465MathML,4figures, no unresolved references/overfullboxes/
missinganchors/browsererrors. Finalacceptance BUILD-REVIEW-ROOT.txt.

v0.12: finite-time counterpulse dynamics, 1 October 2026
Added the reviewed fixed-background linear radial l=1 four-arm/two-grid
counterpulse experiment and its stored-data figure. Target projection and
remaining field norm are separated; neither is presented as energy removal
or nonlinear shutdown. The analytic detuning family remains distinct from
the executed zero-detuning test. Global mode-defect convergence is not claimed.
Numerical inputs, reviews and receipts:
coordination/resonance-20260930/counterpulse-dynamics-20261001/.
This document build introduces no new physics run. Previous v0.11 is saved
in paper-v12-counterpulse/canonical-v11-before/.

V0.13 UPDATE (1 October 2026)
R13 adds numerical sign-change/resolved-winding evidence for n6..10; table,
figure and prediction discussion now use the same new source records.
Historical A06/A10 remain labelled as historical. No new existence certificate,
independent code replication, or validated interpolation error asserted.
Current integrity checks: INPUTS.sha256, ARTIFACTS.sha256,
INPUT-RECHECK-v13.txt, ARTIFACT-RECHECK-v13.txt and SOURCE-R13.sha256.
Older named review/hash files remain historical, not current artifact manifests.
Text author formation_next_calculation, final nonauthor reader ag-phy-coordination;
new R13 input independently checked by formation_review. Review/build records:
coordination/resonance-20260930/paper-r13-review/.
Canonical v0.12 backup: same directory, canonical-v12-before/.

V0.14 UPDATE (1 October 2026)
Added bounded spatiotemporal source-shaping comparison after COUNTERPULSE-TEST,
with five-row table and stored-data figure. Both temporal waveform and spatial
support change; equal Bsrc is not equal work/energy. The stronger selected
projection and lower nonzero remaining field do not establish exact cancellation.
Global eigenmode residual nonconvergence remains explicit. Existing proof
claims/certificates unchanged. Source: SOURCE-SHAPING.sha256 and
coordination/resonance-20260930/source-shaping-20261001/.
Current build is /home/fmh/fmhc-physics-remote/paper-bic-v14-20261001/, .69CPU11.
Current manifests INPUTS.sha256/ARTIFACTS.sha256, checks *RECHECK-v14.txt;
older versioned checks refer only to historical builds. Text author
formation_next_calculation, nonauthor text reader ag-phy-coordination,
result reader formation_review. Canonical v0.13 saved before promotion in
source-shaping-20261001/canonical-v13-before/. No external publication.

V0.15 STAGED UPDATE (1 October 2026; awaiting Root build/review)
Added fixed2x2 actuator comparison after the original source-shaping figure:
four-row fine-grid table and seventh figure factorial-comparison.pdf.
Browser asset for the seventh figure is PNG; the existing six SVGs remain.
Two spatial PAIRS crossed with two temporal PAIRS, normalized after their
component sum. B/T0 maximizes the measured single-pulse projection diagnostic;
B/T1 minimizes both measured pair field norms among these four designs.
No universal additive space/time effects, energy-efficiency claim or new
phase-error finding. Old two-source limitations remain as historical scope.
New source/review: source-shaping-20261001/factorial/RESULT.json and
RESULT-REVIEW.txt. Stage CHANGE-NOTE.txt and STAGE-SHA256SUMS.txt bind files.
Only main version/source row, SOURCE-SHAPING section and this README changed.
Other proof sections copied unchanged. This note is not a build acceptance.

V0.15 BUILD COMPLETED
The planned v0.15 build above has now completed on ubuntu-auto, CPU11 nice19.
27 pages, 595 MathML elements, seven loaded figures; browser/text QA passed.
Root inspected PDF pages22–24. Initial HTML conversion failure and corrected
QA are retained in factorial/paper-stage/BUILD-OBSERVATION.txt; no physics rerun.
Current build /home/fmh/fmhc-physics-remote/paper-bic-v15-20261001/.
Current INPUTS.sha256/ARTIFACTS.sha256 and v15 checks supersede earlier
version-specific integrity checks. SOURCE-FACTORIAL.sha256 binds the new data.
Canonical v0.14 preserved in factorial/canonical-v14-before/.

V0.16 STAGED UPDATE (1 October 2026; Root review/build pending)
Added constant second-pulse phase reconstruction from two real quadratures,
with direct pi/4 implementation control, selected signed phase offsets and
uniform CONSTANT-phase RMS over allfour designs. Eighth figure phase-response
has PDF+PNG; original sixSVG and factorialPNG remain unchanged.
RMS is not mean norm, time average or dynamic noise. Equal source budget
is not equal target preparation: A/T1 starts with weaker mode excitation,
so its lower uniform RMS is not universal superiority for storage/erasure.
No energy/work interpretation, global eigenmode residual limitation retained.
Data/review: phase-quadrature RESULT/RESULT-REVIEW and analysis/figure/SUMMARY.
No new physics calculation or rendering for this textstage. Canonical files
unchanged. Root owns final text/build/QA/promotion; this is not acceptance.

V0.17 STAGED UPDATE (1 October 2026; Root review/build pending)
Added reviewed stored-profile attribution of the second-component boundary
mode defect, without changing the original operator or reference fields.
Added endpoint-only H2/Q2/E2 definitions and four-design single/pair table.
B/T0 lowers the rotating generator while raising the laboratory coefficient;
B/T1 lowers both. These are not measured work or full nonlinear labenergy.
All16 stored states on two grids were used, no PDE rerun. Source-L2 budget
is equal across designs of the same pulse count; a pair uses twice single.
Eight existing figures unchanged, no ninth figure. Theorems and literature
unchanged. No build/test performed by the text author. See CHANGE-NOTE.txt
and SOURCE-ENDPOINT.sha256 for new evidence/provenance.

V0.18 PRIVATE TEXT STAGE (1 October 2026; Root review/build pending)
Adds independently time-integrated PH/JQ/XQ/PEsrc/PEx balances for the same
four designs, single/pair, two grids. Prior endpoint-only limitation is scoped
to that earlier analysis; no historical result is deleted. A new table gives
net second-pulse source works from integrated pair-minus-single totals.
B/T1 second pulse is negative in both work conventions; B/T0 has negative
rotating-generator work but positive laboratory source-work coefficient.
E2 includes exchange and remains a coefficient of the frozen linear ansatz.
No actuator efficiency, full nonlinear energy or shutdown claim. No new plot:
all eight existing figures unchanged. Theorem/literature sections unchanged.
New source: power-balance/RESULT.json ff6ea6c8... and independent
RESULT-REVIEW.txt 0b1e691b...; complete hashes in SOURCE-POWER.sha256.
Build script targets v18 and document QA checks the new work paragraph/table.
No test, interpreter or build was executed by the author.

Root v0.18 build validation: 32 PDF pages, 733 MathML elements, eight loaded
figures, no overflow, missing anchors, browser errors, undefined references or
Overfull boxes. PDF pages27–28 inspected visually. Three LaTeX passes, Pandoc
and browser QA on .69 CPU11 nice19; build19.51CPU-s/20.78wall-s, Exit0.
POWER text review5ae842bb; result review0b1e691b. New Table9 distinguishes
second-pulse source work from rotating-generator work and background exchange.
Actual build INPUTS excludes README/status and provenance-only documents;
author's initial broader manifest is retained in private stage. No release.

V0.19: phase-dependent source work, actual fixed four-design measurement.
New paragraph and phase-work figure display measured real-linear coefficient
curves, direct45degree controls, nominal sign intervals and positive uniform
constant-phase means. Sourcework-only T3 after both sourcewindows, sameh/dt.
Root and nonauthor scientific text/code reviews; bound sources in
SOURCE-PHASE-WORK.sha256. Exact nominal polynomial isolation is not a PDE
error certificate or experimental tolerance; fixed amplitude/normalization.
New figure generated once on .69CPU11nice19 in2.12CPU-s, no new PDE.
Earlier statements about endpoint-only diagnostics retain historical scope.

Root v0.19 validation: 33 PDF pages, 755 MathML elements, nine loaded
figures; no overflow, missing anchors, browser errors, undefined references
or Overfull boxes. PDF pages28–29 visually inspected, including Figure9.
Three LaTeX passes, Pandoc and browser QA on .69 CPU11 nice19;
20.14 CPU-s / 24.30 wall-s, Exit0. Input checks passed before and after.
Independent integration review INTEGRATED-REVIEW.txt hash2fe073d6.
README/status documents are excluded from the actual build-input manifest.
No public release and no new field simulation in this document build.

V0.20 private stage: one fixed angular tangent on a time-dependent inward
chirp background, explicitly distinct from the stationary BIC. Reviewed
finite-time numerical diagnostic, not a full 3D stability/formation claim.
New Figure10 reconstructs signed linear density variations from bound
snapshots. Canonical promotion waits for actual figure/build validation.

Root v0.20 validation:34PDFpages,791MathML,10loadedfigures; nooverflow,
missinganchors,browsererrors,undefinedreferences orOverfullboxes.
Firstbuildfailed ononeOverfull inline(h,dt)list; unnumbered display fixed
layout only. FailedR1logs retained. R2 Exit0,19.55CPU/20.88wall on.69CPU11
nice19; R1used18.63CPU. PDF30/31visuallychecked,Fig10hasnoylabeloverlap.
Actual build manifests checked before/after and aftercanonicalpromotion.
FigureR1layoutissue retained, correctedR2measured4.78CPUtotalforbothrenders.
No publicrelease, no newtheorem, no newPDEinthisbuild. Data/figure/code/text
reviews are internal OpenAI checks; no cross-house replication claimed.

V0.21: independently reviewed fixed exterior Fourier diagnosis added, p32.
Nine stored snapshots;89–94% outward-oriented spectral WINDOW energy, not
escaped original total energy. Significant filter-source term prevents a
free-scattering/remnant-binding claim. No new PDE. Diagnostic0.33CPU seconds.
Document build R1 passed; layout-only R2 flushes Fig10 before new paragraph.
R2:35pages,822MathML,10loadedimages,nooverflow/missinganchors/browsererrors,
noOverfull/undefinedreferences. Root visually checked PDF32. Build R1/R2
19.97/18.62CPU seconds on.69CPU11nice19; bounded document work only.
Evidence: angular-chirp-l2/exterior-analysis/paper-stage/ and RESULT-REVIEW.txt.
Canonical v20 backed up in exterior-analysis/canonical-v20-before/.
No submission/publicrelease, no new theorem or independent physical replication.

V0.22: prescribed temporal phase drift comparison added PDF30.
One delta=.1 at same source-L2 budget raises uniform-in-initial-phase
mean laboratory source work by about10.2%; both means remain positive.
No noise/thermal/efficiency or nonlinear claim; independent data review.
36pages,841MathML,10loadedimages,nooverflow/missinganchors/browsererrors,
noOverfull/undefinedreferences. Root visual PDF30 checked: all new text and
limitations contiguous/readable. R1PASS20.09CPU; layout-onlyR2PASS19.12CPU.
All document work on.69CPU11nice19; physical detuning run7.53CPU separately.
Evidence phase-work/detuning/paper-stage/, SOURCE-DETUNING.txt and results.
Priorcanonicalv21 retained detuning/canonical-v21-before/. No publicrelease.

V0.23: fixed mirror detuning and exact finite-grid parameter tangent.
Same nominal source/operator; old+.1 result reused, no first-pulse replay.
Positive local direction agrees with the finite mirror pair. Positive even
component and small nonzero diagnostic residual exclude an exact-linear
interpretation of these numerical values. Kernel interpretation reviewed
algebraically; no isolated rotation cause, thermal/noise or efficiency claim.
Physical run12.56CPU on.69CPU11nice19,97gates; independent nonauthor review.
Document build/QA passed, separate from physical time. No publicrelease.
Root v0.23:37PDFpages,862MathML,10loadedimages,zerooverflow/missinganchors/
browsererrors/Overfull/undefinedreferences. VisualPDF30 checked: all new
text/table/limits on same page, no clipping. Build19.65CPU/20.97wall on.69.
Inputs rehashed before/after build and before promotion. Priorv22 backedup
in detuning/directional/canonical-v22-before/. README completion receipt is
postbuild metadata; original bound build-input README retained in stage.

Root v0.24 completion,2October2026: PHASE-DIFFUSION-1 source-work mean
and reviewed Wiener/Cauchy interpretation integrated. 38PDFpages,
885MathML objects,10loadedimages,no overflow/missinganchors/browsererrors,
no Overfull/undefined references. Root visually inspected new text PDF31.
One .69CPU11nice19 build19.78CPU/21.08wall,Exit0. New physics run separate:
14.37CPU,96checks,independent code/result/text reviews. Source norm fixed;
no auxiliary-endpoint/efficiency/thermal/stability inference. Canonical
README completion metadata postdates the hash-bound build input README.
Build evidence: source-shaping-20261001/phase-diffusion/paper-stage/.

Root v0.25 completion, 2 October 2026: reviewed rotating-mean identity
and descriptive values added; finite-correlation theory and failed numerical
acceptance reported separately, without an accepted OU mean. 38 PDF pages,
908 MathML elements, 10 loaded images, no overflow, missing anchors or browser
errors. Build exit 0, 19.80 CPU seconds, 21.13 wall seconds on .69 CPU11 nice19.
Visual inspection of PDF pages 31/32 recorded in private stage. Input and
artifact manifests checked again before promotion; v24 files retained under
finite-correlation/canonical-v24-before/. This completion receipt is postbuild
metadata; the original hash-bound README remains in paper-stage/.

V0.38, 2 October 2026: literature scope and documentary corrections.
Primary-text reading and a separate integration review are in
coordination/resonance-20260930/paper-v38-literature/.
The interior wavenumber is explicitly attributed to established work;
phase matching remains calibrated. Oscillon radiation minima are distinct
from exact linear enclosures. Steps from the rounded table are now
2.3043, 2.3053, 2.3068; no new eigenvalue or precision claim.
Build on .69 CPU11 nice19:21.41 CPU-s,24.91 wall-s,Exit0,49pages,
1118MathML,17loadedfigures; Root visually checked PDF3/4/10.
No new physics in this build, no manuscript cut, no public submission.
Git additions and independent second-house C0 reproduction remain open.

v0.40 addition: independently confirmed numerical planar-wall transmission zero
rho=1.52414976213 and unfitted wall-based spacing candidate b=2.31000162857.
Separate mesh/boundary refinements; empirical, not certified, error estimates.
The radial limiting identification and finite-curvature phase function remain open.
One zero found does not prove uniqueness; planar scattering is not an L2 BIC.
Stage/review/build record: coordination/resonance-20260930/paper-v40-planar-wall/.

v0.41 — 3 October 2026
Section 8.2 adds the reviewed exploratory M1 two-dimensional lattice
comparison: h^4/h^8 minimum-width trends and square/triangular angular
channels, with explicit amplitude-decay convention and numerical limits.
Koshelev et al. 2018 supplies the optical analogy, not a Q-ball theorem.
No physical lattice, three-dimensional persistence or nonlinear stability
claim is made. The separate unresolved M2 transport diagnosis is not
imported into this M1 manuscript.
Stage, independent review, source bindings and successful document QA:
coordination/resonance-20260930/paper-v41-grid-robustness/.
Build host ubuntu-auto (.69), CPU11 nice19; 51 PDF pages, 1138 MathML
nodes, 17 loaded figures. Root inspected the new passage on PDF page20.
Remote build: /home/fmh/fmhc-physics-remote/paper-bic-v41-20261003/.

v0.42 — 3 October 2026
Adds a local known-target replication of the planar transmission zero
for U(S)=S-S^2+S^3 (beta=1): rho about 1.77345307180, with spacing
candidate b about 2.618613482. Independent Numerov implementation;
mesh and domain sensitivities are empirical, not certified error bounds.
No blind-search, uniqueness or radial-ladder-limit claim is made.
Evidence: coordination/resonance-20260930/planar-wall-beta1-20261003/.
Text and rendering correction reviewed separately; document build/QA
and page inspection must pass before this staged version is promoted.
Dossier: coordination/resonance-20260930/paper-v42-beta1/.
Document QA and visual inspection now passed on .69: 52 pages,
1152 MathML nodes, 17 loaded figures, no overflow or missing anchors.
Root inspected the new result paragraph on PDF page11.
Remote: /home/fmh/fmhc-physics-remote/paper-bic-v42-20261003/.

v0.43 — 3 October 2026 — staged, build and document QA pending
Added five primary-source comparisons: Flach et al. on discrete-breather
and optical-soliton total reflection; Watabe et al. on spinor-domain-wall
scattering; Heeck et al. for the established leading thin-wall radius;
Inagaki and Murakami for leading second-harmonic radiation zeros.
The nonlinear comparison explicitly distinguishes the leading harmonic
cancellation from vanishing of the complete finite-amplitude radiation.
No priority, universal Krein-signature requirement, new BIC result,
or new physics computation is claimed. Existing numerical results,
figures, certificates and historical revision blocks are unchanged.
Dossier: coordination/resonance-20260930/literature-novelty-20261003/.
Source reviews: ROOT-REVIEW.txt, CHANNEL-REVIEW.txt, INSERT-REVIEW.txt.
BEFORE.sha256 in stage/ binds the four canonical v0.42 input text files.
Only staged main.tex, sections/LITERATURE.tex, sections/bibliography.tex,
and README.txt were prepared; canonical publication files remain unchanged.
Remote target: /home/fmh/fmhc-physics-remote/paper-bic-v43-20261003/.
No v0.43 PDF/HTML, browser check or document-QA acceptance is asserted here.

V0.43 ROOT ACCEPTANCE (3 October 2026; supersedes staged status above)
The reviewed source insertions are now built and promoted with PDF/HTML/text.
The page containing the new channel and nonlinear-harmonic comparisons was
visually checked. The complete unchanged document-QA suite plus new source
checks passed. Previous v0.42 files are backed up in the review folder.

V0.44 ROOT ACCEPTANCE (3 October 2026; recorded in this history 4 October)
The additional-channel scope paragraph was independently reviewed and the
v0.44 document built once on .69 CPU11 nice19 under the existing cpu2 lock.
The Root acceptance receipt records Exit 0, 21.31 CPU seconds and 23.50 wall
seconds; 52 PDF pages, 1157 MathML elements and 17 loaded images, with no
reported overflow, missing anchors, browser errors, undefined references
or raw-math fallbacks. Root visually inspected the changed paragraph on
PDF page 37. The sources and PDF/HTML/text were promoted after binding
checks; previous canonical artifacts were retained in canonical-before/.
No new physics result or public release was made. This paragraph records
existing acceptance evidence, not a new build or independent reproduction.
Evidence: coordination/resonance-20260930/wall-correlated-20261003/
paper-channel-v44/ROOT-ABNAHME.txt and build/DOCUMENT-QA.json,
build/BUILD-TIME.txt. The original frozen build README remains unchanged.

V0.45 — 4 October 2026 — STAGED, NOT YET ACCEPTED
Only the date/version and three explicit reproducibility table locators
change in main.tex; no scientific result, tolerance, formula or figure is
changed. README metadata distinguishes the accepted v0.44 from this pending
source revision and adds the missing v0.44 historical acceptance entry.
The original failed finite-correlation inventory row remains verbatim.
Independent text review and .69 document build/QA are still required.
Stage: coordination/resonance-20260930/wall-correlated-20261003/
paper-inventory-v45/. BEFORE.sha256 binds the canonical input text files;
EVIDENCE.sha256 binds the specifically named results/reviews and v0.44
acceptance receipts. No canonical manuscript file is changed by this stage.

V0.45 ROOT ACCEPTANCE — historical status correction, 5 October 2026
The pending status above is superseded by the existing acceptance of
4 October 2026 17:07:10 CEST. On 5 October, all five canonical files
(main.tex, README.txt, paper.pdf, paper.html, paper.txt) were checked
against paper-inventory-v45/CANONICAL-AFTER.sha256 and matched before
this append-only README correction. The existing acceptance records
53 pages, 1157 MathML elements and 17 images; document gates and the
8-case export corpus passed. Title and changed inventory page were
visually inspected then; no new full-document visual inspection is
claimed. The bell/environment/formation scope statements remain in
the accepted source and exported text. No new build, physics run or
publication is performed by this correction. The old acceptance manifest
remains historical; this README now has a new hash.
Evidence: coordination/resonance-20260930/wall-correlated-20261003/
paper-inventory-v45/ROOT-ACCEPTANCE.txt and CANONICAL-AFTER.sha256.
