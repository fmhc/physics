Englische Fassung des SU(3)-Arbeitsentwurfs v0.5
=============================================

Fertig: vollständige englische Übersetzung in HTML und LaTeX, englisch
beschriftete Grafik und zwei PDF-Fassungen. Wissenschaftliche Aussagen sind
unverändert auf die deutsche Basis v0.5 begrenzt. Kein neuer Physiklauf.

Öffnen:
- paper.pdf: LaTeX-Satz, 10 A4-Seiten, primäre PDF-Lesefassung.
- paper.html: englische HTML-Fassung mit transfer-detuning.svg.
- paper-html.pdf: separat aus HTML gedruckte Fassung.
- main.tex und transfer-detuning.pdf: editierbare LaTeX-Quelle und Vektorgrafik.

Basis/Dateibesitz:
Koordinationsauftrag in coordination/status-audit-20260930/AN-PD1-PAPER.txt.
Eigener Ordner -en-codex; deutscher Originalordner und alter -en-Ordner wurden
nicht bearbeitet. source-v0.5.html und transfer-detuning-source.svg sind die
vor Arbeitsbeginn gesicherten Originale. BASIS-SHA256SUMS.txt hält die damals
beobachteten Originalpfade/Hashes fest; INPUTS.sha256 bindet die eigenen Kopien.
SOURCE-SHA256SUMS.txt ist die unveränderte Quellenliste des deutschen Autors,
mit Pfaden relativ zur Projektwurzel. Sie ist kein neuer Auditnachweis.

Übersetzungsgrenzen:
Publikationsfassung offen. Ausführlicher H1-Titel hat Vorrang. Dezimalpunkte
statt Dezimalkommas; keine stillen neuen Beweise. Die Manuskriptfassung folgt
v0.5, nicht späteren separaten Außenraum-/Normalformnotizen. HTML und LaTeX
wurden getrennt übersetzt und auf Sinntreue geprüft; Wortlaut nicht identisch.
Details: REVIEW-TRANSLATION.txt, REVIEW-INDEPENDENT.txt sowie die beiden
TRANSLATION-NOTES-Dateien. REVIEW-INDEPENDENT enthält seinen Prüfsnapshot;
danach erfolgten die dort empfohlenen Sprach- und technische Satzkorrekturen.

Rechenort/Prüfung:
Nur Darstellung und Dokumentprüfung auf ubuntu-auto (.69), CPU11, nice19,
OPENBLAS_NUM_THREADS=1 / OMP_NUM_THREADS=1 für Plot/Browser-QA. Keine CUDA-
Physik, keine Simulation, kein Fit, keine erneute Eigenwertrechnung. Last vorab
geprüft (12 logische CPUs, ca. sechs laufende Physikprozesse, ca. 19 GiB verfügbar).
Keine fremden Jobs, Dienste oder GPU-Zustände verändert. Kein Git/Hook/Dienst.

Remote-Arbeitsordner:
/home/fmh/fmhc-physics-remote/paper-english-v05-20260930/
Da pdflatex dort nicht installiert war, wurden vorhandene lokale TeX-Live-
Dateien, pdftex, Pandoc und Poppler samt benötigten Bibliotheken ausschließlich
nach tools/ im Remote-Arbeitsordner kopiert. Keine Systeminstallation.
pdfTeX 1.40.25, TeX Live 2023/Debian; Pandoc 3.1.3. Compiler mit
-no-shell-escape. Keine lokalen Interpreter-, Compiler- oder Teststarts.

Wiederherstellung mit vorhandenem TeX Live auf einem erlaubten QA-Rechner:
  pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
Die Ausgabe main.pdf entspricht der Lesefassung paper.pdf.
Benötigt übliche Pakete einschließlich lmodern, amsmath, amssymb, graphicx,
booktabs, tabularx, microtype, geometry und hyperref. Vollständige Präambel in main.tex.

plot-english.py liest ausschließlich FIGURE-DATA.json und zeichnet die schon
berechneten Werte wie plot-source.py, mit englischen Labels und PDF-Ausgabe.
Es ruft keine Physikfunktionen auf. Grafikdaten stammen unverändert aus
coordination/resonance-20260930/shell-detuning/RESULT.json.

QA-Nachweise:
qa/DOCUMENT-QA.json: Quellstruktur, Tabellenwerte, genaue Dezimalzahlen, Links,
Browserdarstellung. qa/TEX-QA.json: LaTeX-Tabellenwerte/Dezimalzahlen, 15 Tags,
Compilerlog und Hashes. qa/PDF-INFO.txt und PDF-FONTS.txt: PDF-Eigenschaften.
qa/latex-final.log: abschließender Compilerlauf. PNG-Dateien: Remote-Sichtproben.
Frühe technische Fehlversuche sind als alte QA-Logs erhalten; maßgeblich sind
DOCUMENT-QA.json, TEX-QA.json und latex-final.log. Kein Physikzertifikat.

ARTIFACT-SHA256SUMS.txt bindet die fertigen auszuliefernden Dateien.
