Urteil: Zwei Papiere statt einem dicken. Kein eigenes Papier aus den Anhaengen A und B. Der Schnitt zwischen I und II wird erst nach ZZZ-ABGLEICH endgueltig. Auflagen PS-1 bis PS-8 (Abschnitt 5).
- I: M1-Kern, gekuerzt, kommt zuerst.
- II: M2-Huellenleitern, erst nach formalem v3-Test und Reproduktion durch ein zweites Haus.

# Paper-Schnitt: Was steht im Q-Ball-Manuskript, was fehlt, ein Papier oder mehrere?

- Pruefer: frischer Pruefer, Haus Anthropic (Claude), Auftrag der Leitung claude-primary auf Finns Frage
- Beginn: 2026-10-02 20:07:07 CEST, Ende des Berichts: 2026-10-02 20:20:18 CEST (beides per date gemessen). Dauer gut 13 min, Zeitbox 45 min. Danach kam nur noch der Abschnitt "Quote" in 5 hinzu; letzte Messung davor 20:20:53 CEST.
- Gegenstand: model-lab/papers/qball-bic-ladder-20260930/
  - laut Auftrag v0.25
  - tatsaechlich Draft 0.37 vom 02.10.2026, siehe 1.0
- Arbeitsweise: nur lesen; geschrieben wird nur diese Datei. Git nur lesend (diff, status, log, ls-tree), mit GIT_OPTIONAL_LOCKS=0.
- Nicht geoeffnet: RUNDE-22/codex-blick/ und RUNDE-22/zzz-abgleich/ (moegliche Parallelpruefung bzw. Abgleich), gesperrte Pfade laut Auftrag.

## 1. Ergaenzungen im Papier

### 1.0 Vorbefund: Versionsstand

- **Das Papier steht nicht auf v0.25, sondern auf Draft 0.37.**
  - main.tex Z. 13 und paper.txt Z. 6: "2 October 2026 --- Draft 0.37" (Stand 06:38).
  - README.txt (Z. 2, Stand 00:44) nennt noch v0.25.
  - v0.26 bis v0.37 stehen nur in den Stage-Ordnern unter coordination/resonance-20260930/ (je ROOT-ABNAHME.txt bzw. STAGE-REVIEW.txt), nicht in der README.
  - Umfang laut paper-stage-v37/PDF-INFO.txt: 49 PDF-Seiten. v0.1 hatte 12 Seiten (PEERBUS-RESULT.txt), v0.25 hatte 38 (README Z. 397-399).
- **`git diff --stat` unterschaetzt die Ergaenzungen.**
  - Die Statistik zeigt 10 Dateien mit +2397/-722 Zeilen. Davon sind die getrackten Abschnittsdateien nur kosmetisch geaendert: `\rm` wird zu `\mathrm` (COUNTERPULSE, EXTERIOR-FORMATION, LITERATURE, MODE-FIGURES, SOURCE-SHAPING).
  - Der Inhalt steckt in **8 ungetrackten neuen Abschnittsdateien** (git status `??`), die in `--stat` nicht erscheinen.
  - Der HEAD-Stand f726adb (02.10. 00:07) enthaelt main.tex mit "Draft 0.23".

### 1a. Seit dem letzten Git-Stand (HEAD = Draft 0.23, jetzt Draft 0.37)

| Abschnitt (Ort im Papier) | Was neu ist | Evidenzstufe | Version laut Stage-Notizen |
|---|---|---|---|
| sections/PHASE-DIFFUSION.tex (Anhang A) | Vorgeschriebene Wiener-Phasendrift der Treiberquelle: Korrelation e^{-D\|t-s\|}, Mittel der Quellenarbeit; ein Vergleich bei endlicher Kohaerenz | analytische Identitaet; numerisch (README Z. 386-394: 96 Checks, Reviews durch Nicht-Autor); Quelle vorgeschrieben, kein Rauschmodell | v0.24 |
| sections/FINITE-CORRELATION.tex (Anhang A) | OU-korrelierte Momentanfrequenz C(u), Grenzfall kleiner Korrelationszeit, Identitaet des rotierenden Mittels, Pulsvergleich, Aussenraum-Sensitivitaet, Kern mit Vorzeichen ueber Quellzeit-Abstaende | analytisch plus numerisch. **Die numerische Akzeptanz des urspruenglichen Feldlaufs ist gescheitert, ein OU-Mittel wurde nicht akzeptiert** (README Z. 396-399; NUMERICAL-METHOD-CONTROLS Z. 2-4) | v0.25 bis v0.29 |
| sections/NUMERICAL-METHOD-CONTROLS.tex (nach der Provenienz) | RK4-Endschrittdefekt als Mechanismus in Kontrollen mit konstanter Quelle; das Scheitern wird offen benannt | Methodenkontrolle, keine Physikaussage | ab v0.26 (v26 STAGE-REVIEW: "one appendix input before Contributions") |
| sections/SELF-GRAVITY-SCOPE.tex (Anhang B) | Instantane Klein-Gordon-Poisson-Schliessung: Kandidaten der ersten zwei Leiterlabels bleiben bei je zwei schwachen Kopplungen bestehen, omega^2 sinkt | explorativ numerisch, 4 Punkte, ausdruecklich bedingt (Poisson-Residuum, Matching offen) | vermutlich v0.29 (mtime 03:09; v29 ROOT-ABNAHME nennt "gravity model reviews") |
| sections/ANGULAR-SECOND-ORDER.tex (Anhang B) | Zweite Variation fuer ellipsoidale Y20-Deformation: Rueckwirkung auf den Ladungstransport im Kern, Energie bis O(eps^2) kompensiert, lokaler Zeitverschiebungstest mit zwei Observablen, 2 Figuren | numerisch (Endpunkt), Review durch Nicht-Autor; laut eigenem Text keine Bildung und keine Stabilitaet | v0.30 bis v0.32 |
| sections/FINITE-ELLIPSOIDAL-RESPONSE.tex (Anhang B) | Endliche Ellipsoide eps = ±0.02 und ±0.04 bei gleichem Q und E bis T = 32; Phasenrotation und kinetische Luecke bei fester Ladung; 3 Figuren | numerisch plus Algebra bei fester Ladung; "Einzelsignale haben keine eigene zertifizierte Fehlerhuelle" (v34 ROOT-ABNAHME) | v0.34, v0.35 |
| APPENDIX-DRIVING.tex, APPENDIX-FORMATION.tex, main.tex Z. 369-375 und 393-398 | **Umbau:** Umwelt-, Treiber- und Bildungsteile wandern aus dem Hauptteil in Anhang A und B. Neue Brueckensaetze, u. a. "None establishes formation ... do not supply additional evidence for the certified BIC backgrounds" | redaktionell, keine neue Aussage (v33 ROOT-ABNAHME) | v0.33 |
| main.tex, Provenienztabelle | 4 neue Zeilen: Phasendiffusion, rotierendes Mittel und endliche Korrelation, endliche Ellipsoide, Phasen- und Profildiagnosen | Herkunftsnachweis | v0.24 bis v0.35 |
| 5 getrackte Abschnitte, style.css, fonts/ | Matheschrift und `\mathrm` | nur Darstellung (v37 ROOT-ABNAHME: "Keine Zahlen ... geaendert") | v0.36, v0.37 |
| README.txt | Belege fuer v0.24 und v0.25; **zu v0.26 bis v0.37 nichts** | Dokumentationsluecke | bis v0.25 |

**Kern seit HEAD unveraendert:** Abstract, Beweisteil, Leiter, Duennwand und nichtlineare Obstruktion haben keine inhaltliche Aenderung (Diff von main.tex Z. 366-398 und 441-520). Alles Neue liegt in den Anhaengen A und B.

### 1b. Ueber die Versionen bis v0.37 (Quelle: README.txt Z. 52-404, PEERBUS-RESULT.txt, REVISION-MATRIX-FINAL.txt, Stage-Notizen)

| Version | Ergaenzung | Evidenzstufe |
|---|---|---|
| v0.1 (30.09.) | Drei Existenzfaelle: zwei radiale Moden und ein Dipol. 15 radiale Kandidaten mit getrennten Belegstufen, sequentielle Vorhersagen gegen MOD2, Duennwand kalibriert bzw. abgeleitet, quadratische Quelle, n1-Strahlungsevidenz | **Beweis** (rechnergestuetzt, Ball-Arithmetik, OpenAI/Anthropic-intern gegengelesen, keine zweite Intervall-Implementierung: main.tex Z. 44-47); numerisch; sequentielle Vorhersagen "reportedly author-blinded" (Abstract), also **vorab gewertet**, aber nicht nach v3; Duennwand teils **nachtraeglich** kalibriert |
| v0.2 bis v0.4 | Glockenbild; Fragen zu Umwelt und Bildung; Windungspruefung periodischer Dichteinseln; Vermittler-Vorbehalt; Energie-Ladungs-Identitaet mit Schranke gegen Verduennung | Ausblick; Schranke ist ein elementarer **Beweis** (README Z. 78-87) |
| v0.5, v0.6 | T2-Dipol: erzwungene zweite Harmonische, vier Ausgangsamplituden ungleich null; Quellstrom-Check mit festen Gewichten | numerisch, Eingang nur naeherungsweise |
| v0.7, v0.8 | Winkelidentitaeten fuer komplexe Dipolpolarisation; vollstaendige L0-Koeffizienten-Einschliessung > 0.000559 bei T2; H4_gamma-Regularitaet | **Beweis, bedingt** auf T2-, Span- und Einschliessungshypothesen |
| v0.9 | Projektionsidentitaet fuer lineare Quellen | analytisch (Beweis) |
| v0.10 | Primaerliteratur: Battye/Sutcliffe, Azatov et al., Evslin, Malomed, Soffer/Weinstein; Datenpaket geprueft; 2D-Probe und Probe mit zusaetzlichem neutralem Kanal | **Literatur**; Proben explorativ |
| v0.11 | Drei Farbfiguren; analytische Vorhersage fuer zwei Gegenpulse | Darstellung; analytisch |
| v0.12, v0.13 | Gegenpuls-Dynamik (linear, l = 1); R13-Vorzeichenwechsel und Windung fuer n6 bis n10 | numerisch |
| v0.14 bis v0.19 | Quellenformung, 2x2-Aktuatorvergleich, Phasenquadratur, Endpunktgroessen, Leistungsbilanz, phasenabhaengige Quellenarbeit | numerisch, feste Designs, Review durch Nicht-Autor. Die Rollen sind Codex-Agenten (README V0.13/V0.14: formation_next_calculation, ag-phy-coordination, formation_review). Zu v0.20 heisst es woertlich "internal OpenAI checks; no cross-house replication claimed" (README Z. 345-346) |
| v0.20 bis v0.23 | Winkel-Chirp l = 2 auf nichtstationaerem Hintergrund; Fourier-Diagnose im Aussenraum; Verstimmung und Spiegelung | numerisch explorativ |
| v0.24 bis v0.37 | siehe 1a | siehe 1a |

**Befund zu 1:** Seit etwa v0.13 kam kein neuer Kernsatz hinzu (Existenz, Leiter, Duennwand, Obstruktion).

- Gewachsen sind zwei Nebenlinien:
  - (A) lineare Antwort auf vorgeschriebene Treiber: Umwelt, Gegenpuls, Quellenformung, Phase, Rauschen.
  - (B) explorative Konzentration und Bildung.
- Beide sind Codex-intern geprueft, ohne zweites Haus.
- Zusammen machen sie inzwischen rund die Haelfte des PDFs aus.
  - Lage im aktuellen paper.pdf, per pdftotext seitenweise gesucht: Anhang A beginnt auf S. 20, B auf S. 36, Provenienz C auf S. 45, Methodenkontrollen D auf S. 47, Literatur auf S. 48, insgesamt 49 Seiten.
  - A und B belegen damit die Seiten 20 bis 45, also 25 bis 26 von 49 Seiten. Gezaehlt: 45 - 20 = 25, dazu die geteilte Startseite.

## 2. Vorhandenes, das nicht im Papier steht

Das Papier enthaelt nichts zum Zweifeldmodell. Die Suche nach "Friedberg", "FLS", "two-field", "bag" und "shell" in main.tex und sections/*.tex ergab nur Formulierungen zu Niveauflaechen und Schalen (MODE-FIGURES Z. 28-30, NONLINEAR Z. 301). Alles Folgende gilt "im Modell" (RUNDE-20.md Z. 287: "Alles 'modell' (keine Messdaten)").

### 2a. Huellenstrang M2: Zweifeldmodell psi/chi, Modell BEUTEL-1 von Codex, Rechnungen durch Code-Agenten der Leitung (Haus Anthropic)

| Ergebnis | Fundstelle | Stufe | Anmerkung |
|---|---|---|---|
| 15 stille Stellen im Ein-Kanal-Fenster E1, Umlauf ±1 auf zwei Stufen; keine in E2 (mit Vorbehalt) | RUNDE-17.md Z. 324-352 | numerisch, Vorhersagen S1-S4 vor dem Plan; Plan nach der Karte eingefroren, Code nach dem Einfrieren geaendert (Selbstanzeige) | Ursprungsbefund |
| Blinder Nachbau mit Code 2 | RUNDE-17.md Z. 361-367, Z. 445 ff.; RUNDE-18.md Z. 73 | numerisch, laut RUNDE-18 "post hoc" | zweiter Code im selben Haus |
| **HUELLEN-UHR:** Zeitbereich, Code 3, 5 von 5 eingetroffen. BIC-Mode strahlt 3,7e-5 bzw. 5,3e-5 ab, die Kontrolle 2300- bis 35 000-mal mehr. Exponent eps^4 gegen eps^2. Ticks bei 2 pi/rho | RUNDE-18.md Z. 43-76 | **vorab gewertet**, mit Gegenprobe (verschobenes omega^2, generischer Stoss, Nullarm) und zwei Gittern | staerkster Einzelbeleg; nur l = 0 |
| 88 stille Stellen auf 10 chi-Kurven bis R = 39, Sprossenabstand etwa 2,2 bis 2,5 | RUNDE-18.md Z. 103-143, Z. 174 | numerisch, Ordnung **nachtraeglich** beschrieben | Rundungsgrenze chi < 1e-16 begrenzt die Zaehlung (Z. 182) |
| l = 1: 19 Stellen auf 5 Leitern; l = 2: 15 Stellen, Q2 knapp nicht eingetroffen (+5,7/+6,0 % statt <= 5 %) | RUNDE-19.md Z. 80-110 und Z. 178; RUNDE-20.md Z. 153-184 und Z. 262 | numerisch; Versatz zwischen den l **nachtraeglich** mit Kugel-Bessel-Phasen [H] | Paarung ueber l nur nach rho, nicht nach Rang (RUNDE-20.md Z. 281) |
| HUELLEN-LEITER-3: formal P1' nicht, P2' eingetroffen. Nachtraeglich lagen alle 8 Sprossen hoechstens 0,018 daneben | RUNDE-19.md Z. 147-172 | **nicht als vorab bestanden zitierfaehig** (Fremdstimme) | |
| **SPROSSEN-VORAB:** 12 von 12 neuen l = 0-Sprossen vorab getroffen. Alle Abweichungen negativ; k = 7 brauchte 79 % der Toleranz | RUNDE-20.md Z. 59-95 | **vorab gewertet**, Zeitfolge an Dateizeiten geprueft | Nachtrag 1: eine Sprosse war vorbekannt; Nebenlesart 7 von 7 |
| **SPROSSEN-L1L2:** 10 von 10 neuen l = 1/2-Sprossen vorab getroffen; P2 2,6-mal genauer als P_lin | RUNDE-21.md Z. 39-81 | **vorab gewertet** | Satz B: eine verworfene Wurzel bei R = 22,29 ist nachtraeglich eine echte Stelle |
| **LEITERFORMEL (Phasenregel):** LF0, LF1 (genau 80,0 %, ohne Puffer), LF3, LF4 eingetroffen; **LF2 nicht** (62,5 % statt >= 70 %) | RUNDE-21.md Z. 161-195 | vorab gewertet; **vorab festgelegte Bedeutung: "nicht als geschlossener Baustein fuer l = 0, 1, 2 bestaetigt"**. McMahon-Term und Radiusversatz kamen **nachtraeglich** [H] | Die Regel gilt gut auf eingespielten Leitern (Wandkurve bei R ~ 40 auf 0,07 bis 0,33 %), schlecht auf jungen Kurven (bis 20 %) |

**Gegenlesen zur Zaehlung der Sprossentests.**

- RUNDE-21.md Z. 76 sagt: "Die Sprossenregel ist fuer l = 0, 1, 2 **je zweimal** vorab bestanden (R20, R21)". Das trifft nicht zu. l = 0 wurde einmal geprueft (R20, 12 Sprossen), l = 1 und l = 2 je einmal (R21, 10 Sprossen zusammen).
- Richtig ist: **zwei** vorab gewertete Tests insgesamt. Der Auftrag der Leitung formuliert es korrekt.
- Folge fuer v3 Abschnitt 5: Je l liegt nur ein bestandener Test vor.

**Gegenlesen zu L2.** Die R20-Latten-Bilanz zaehlt fuer SPROSSEN-VORAB die "L4-Vorpruefung" als L2 (RUNDE-20.md Z. 270).

- Diese Vorpruefung eicht das Annahmekriterium positiv an bekannten Stellen. Ein Kontrollarm im Sinn von V3-ENTWURF Abschnitt 2 ist sie nicht ("Ist der Effekt groesser als in der Kontrolle (Permutation, Symmetrie, Kopplung aus)?").
- In beiden ERGEBNIS-Dateien finden sich keine Nullfenster und kein Permutationsarm.
  - Gesucht wurde mit grep -i nach "kontroll", "gegenprobe", "versetzt", "zufall" und "nullvorhersage": in beiden Dateien 0 Treffer.
  - Die Suche nach "L2" bzw. "L4" fand in sprossen-vorab nur die L4-Vorpruefung.
  - Die Pruefung lief nur per grep, ich habe nicht beide Dateien ganz gelesen.
- Mit einer Gegenprobe abgesichert ist nur HUELLEN-UHR.

### 2b. Literatur zum Huellenstrang (RUNDE-21/fls-stille/ERGEBNIS.md)

- **Nach Recherchestand nicht beschrieben:** stille, eingebettete Moden in FLS-artigen Q-Baellen.
  - Gesucht wurde auf arXiv nach "Q-ball x BIC": 0 Treffer ueber alle Jahre (ERGEBNIS Z. 170).
  - Formulierung dort: "nach Recherchestand nicht beschrieben", nicht "neu".
  - Nicht geprueft ist, ob M2 in genau dieser Form in der Literatur vorkommt (zusaetzliche psi-Masse, Sextik).
- **Bekannt und zu zitieren:**
  - lineares FLS-Problem mit drei Kanaelen: 2412.13885, Abschn. 3
  - Superradianz an FLS: 2503.04657
  - **Halbwellen-Periodizitaet der Streumaxima im Wandradius fuer duennwandige Einfeld-Sextik-Q-Baelle: 2510.27064** (Gl. 108-118, Abb. 3; Abstract: "peak spacing is simply the inverse of the Q-ball size")
  - Folge von Abstrahlungs-Dips bei phi^6-Oszillonen: 2004.01202, Abschn. 7.5 (ERGEBNIS Z. 20-31 und 116-130)
- **Berichtigungsbedarf im bestehenden Papier**, unabhaengig von jedem Schnitt:
  - LITERATURE.tex Z. 24-31 beschreibt Azatov2024 (= 2412.13885v1, bibliography.tex Z. 43-46) nur als Arbeit zur Einfeld-Sextik. Abschnitt 3 dort behandelt aber FLS-Q-Baelle.
  - 2510.27064 betrifft **dieselbe Sextik-Familie wie das Papier**. Sie ist die naechste Abgrenzung fuer die Duennwand-Phasenanpassung des Papiers (main.tex Abschn. "A thin-wall phase-matching description"), nicht nur fuer M2.
  - Die vorbereitete Karte ZZZ-ABGLEICH stellt genau diese Frage (RUNDE-22.md Z. 201-202). Ihr Ergebnis liegt nicht vor; den Ordner habe ich nicht geoeffnet.

### 2c. Bildung, Toechter, Drehimpuls (Einfeldmodell M1, **in 2D**, nicht 3D wie das Papier)

| Ergebnis | Fundstelle | Stufe |
|---|---|---|
| BILDUNG-1: Einzelne Klumpen laufen auf die Q-Ball-Familie zu (B0-B2 eingetroffen, B3 nicht: Arm iii behaelt 62,6 % der Ladung); "M1 ist in 2D fuer isolierte Klumpen bildungsfaehig (Stufe 5, im Modell) [H]" | RUNDE-22.md Z. 89-117 | vorab gewertet; nur ein Familienpunkt (Q = 66,6), symmetrisch, ohne Wellenbad |
| BILDUNG-2: C1 nicht eingetroffen (grosser duennwandiger Klumpen atmet bis T = 1000), C0 nicht (Drift aus dem Suchfenster), C3 eingetroffen, C4 nicht | RUNDE-22.md Z. 205-238 | vorab gewertet; Bad-Arm offen; Idee BILDUNG-LEITER **ungerechnet** [H] |
| KF-EICH: Der Klassifikator sagt bei exakten Baellen "auf"; "auf" heisst nur "Q passt zu omega" | RUNDE-21.md Z. 129-160, Z. 237 | Eichung |
| Bio 28b: Der gefuetterte Drehball (m = 1) zerfaellt in Toechter ohne Windung; 3 von 8 Stuecken "auf" und rund | RUNDE-22.md Z. 126-151 | vorab gewertet; D0 weitgehend vorab ableitbar |
| Bio 28c: Der Drehimpuls bleibt erhalten (8e-14); 52 bis 84 % gehen in die Bahnbewegung der Toechter | RUNDE-22.md Z. 160-188 | **nur beschreibend**: J1/J2 waren vorab aus den Bio-28b-Rohdaten ableitbar (Selbstanzeige der Leitung); kein Gittervergleich, L3 offen |

### 2d. Sonstiges

- **EW-BAELLE** (RUNDE-20.md Z. 102-139): reine Lektuere von 2609.19293. M2 ist kein Spielzeug dieser Klasse, es gibt keinen Beutel. Ein Ein-Kanal-Fenster existiert [H]. Stille Atmung elektroschwacher Baelle ist offen, schwer zu rechnen und geparkt. Keine eigene Rechnung, kein Papierstoff, hoechstens ein Satz im Ausblick.
- **Codex-Uhr mit Detektor** (RUNDE-22.md Z. 69-88): explorativ, Zweitauswertung nicht blind, laut Leitung nur Fussnote.

## 3. Papierkandidaten

Stufen: B = Beweis, N = numerisch, V = vorab gewertet, P = nachtraeglich, L = Literatur.

### Kandidat I: BIC im 3D-Sextik-Q-Ball (M1), der Kern des jetzigen Manuskripts

- **Kernaussage:** Im dreidimensionalen Sextik-Q-Ball heben sich im Ein-Kanal-Fenster Abstrahlungen exakt auf.
  - Drei solche eingebetteten linearen Moden sind rechnergestuetzt bewiesen: zwei radiale und ein Dipol.
  - 15 radiale Kandidaten bilden eine Folge mit fast gleichem Abstand in der inversen Verstimmung.
  - Nichtlinear speist die zweite Harmonische offene Kanaele. Daraus folgt eine bedingte Obstruktion.
- **Tragende Belege:**
  - Existenz: B per Ball-Arithmetik. Die Beweisbausteine sind haeuseruebergreifend gegengelesen, eine zweite Intervall-Implementierung gibt es nicht (main.tex Z. 44-47).
  - Folge n1 bis n15: N; fuer n6 bis n10 zeigen Vorzeichenwechsel und Windung (v0.13), A06 und A10 bleiben historisch.
  - Sequentielle Vorhersagen: "reportedly author-blinded" (Abstract). Sie liegen vor v3 und sind kein formaler Test.
  - Duennwand: teils kalibriert, also P.
  - L0-Koeffizient bei T2: B, bedingt auf die Hypothesen.
  - T2-Antwort: N.
- **Neuheitsstand:**
  - BIC in Q-Baellen: arXiv "Q-ball x BIC" ergab 0 Treffer (fls-stille ERGEBNIS Z. 170), also nach Recherchestand nicht beschrieben.
  - Bekannt sind der Radialoperator (Azatov 2412.13885), das Mechanismusprinzip (Friedrich/Wintgen) und das Duennwandbild. Das Papier beansprucht hier selbst keine Prioritaet (main.tex Z. 71-75).
  - **Neu zu pruefen:** Das Papier nennt als zentralen Beitrag "numerically tested spacing structure" (main.tex Z. 71-72). 2510.27064 zeigt fuer **dieselbe Sextik-Familie** Halbwellen-Periodizitaet der Streumaxima im Wandradius.
  - Ob das derselbe Mechanismus ist, klaert ZZZ-ABGLEICH (laeuft bzw. ist vorbereitet).
- **Was fehlt:**
  - Literatur: Azatov2024 als FLS-Arbeit richtigstellen; 2510.27064 und 2004.01202 abgrenzen.
  - Zweites Haus: mindestens eine Einschliessung unabhaengig nachrechnen, z. B. C0, im anderen Haus. Begruendung: v3 Abschnitt 5 verlangt fuer Aussagen nach aussen eine Reproduktion durch ein zweites Haus. Gegenlesen ist keine Reproduktion.
  - Formaler v3-Test: nur noetig, wenn die Abstandsregel als Gesetz behauptet wird. Wird die Folge wie jetzt beschreibend vertreten, reicht B plus N.
  - Oeffentliches Supplement mit Lizenz und Archiv-ID (README Z. 44-49).
  - README auf v0.37 nachziehen.
  - Anhang A und B kuerzen oder auslagern (siehe 4).
- **Abhaengigkeit:** keine. I kann allein stehen.

### Kandidat II: Stille Huellenleitern im FLS-artigen Zweifeldmodell (M2)

- **Kernaussage:** Im Zweifeldmodell mit chi-Huelle gibt es im Ein-Kanal-Fenster viele exakt stille lineare Moden (l = 0, 1, 2). Sie ordnen sich auf Leitern im Huellenradius, und neue Sprossen lassen sich vorab vorhersagen.
- **Tragende Belege:**
  - N mit Windungszahl auf zwei Stufen und drei Codes, alle im selben Haus.
  - V: HUELLEN-UHR, 5 von 5, mit Gegenprobe, nur l = 0.
  - V: zwei bestandene Sprossentests, 12 von 12 (l = 0) und 10 von 10 (l = 1, 2).
  - Die Phasenregel ist **nicht** als geschlossener Baustein bestaetigt (LF2 nicht eingetroffen). Die Korrekturen nach McMahon und mit Radiusversatz sind P [H].
- **Neuheitsstand:**
  - In der FLS-Literatur nach Recherchestand nicht beschrieben.
  - Bekannt: das Dreikanalproblem, Halbwellen-Periodizitaet in der Streuung (2510.27064), "more peaks" (2503.04657) und Oszillon-Dips (2004.01202).
  - Ungeprueft ist, ob M2 in genau dieser Form schon in der Literatur vorkommt.
  - Ein physikalischer Anker fehlt: Die elektroschwachen Baelle haben keinen Beutel (RUNDE-20.md Z. 117-118).
- **Was fehlt:**
  - **Formaler v3-Test mit echter Gegenprobe.** Das Nullfenster ist bisher nicht gemacht (vgl. 2a).
    - Anforderung: ein Kontrollarm, in dem das unveraenderte Annahmekriterium in Fenstern um einen halben Sprossenabstand versetzt **keine** Stelle annehmen darf.
    - Je l mindestens ein weiterer vorab gewerteter Satz neuer Sprossen, damit l = 0, 1, 2 je zweimal bestanden sind.
  - **Reproduktion durch ein zweites Haus.** Bisher stammen alle drei Codes von Code-Agenten der Leitung. Codex hat das Modell gebaut, die Stellen aber nicht nachgerechnet.
  - Gezielte Literaturpruefung der genauen M2-Form.
  - Optional eine Einschliessung fuer eine M2-Stelle, damit II den Beweisstandard von I erreicht.
  - Konvergenz jenseits von R = 40: Rundungsgrenze und Code-Reichweite (RUNDE-20.md Z. 92-94).
- **Abhaengigkeit:** II nutzt Mechanismus, Windungsnachweis und Kanalbild aus I. Am besten zitiert II den Kandidaten I als Preprint. Ohne I muss II den Mechanismus selbst herleiten.

### Kandidat III: Antwort auf vorgeschriebene Treiber (heute Anhang A, S. 20-36)

- **Kernaussage:** Auf festem Hintergrund entscheidet die adjungierte Ueberlappung einer lokalen Quelle, ob die stille Mode angeregt wird. Gegenpulse, Quellenformung und Phasenrauschen veraendern Projektion und Quellenarbeit.
- **Belege:**
  - Projektionsidentitaet und Gegenpuls-Vorhersage: analytisch.
  - Designvergleiche mit vier festen Designs: N, nur Codex-intern geprueft (Rollennamen in README V0.13-V0.20; Z. 345-346).
  - OU-Teil: **numerische Akzeptanz gescheitert** (NUMERICAL-METHOD-CONTROLS Z. 2-4).
- **Neuheitsstand:** Eine Literaturabgrenzung fuer Anhang A fehlt ganz. Lineare Antwort und kohaerente Gegenpulse sind Standardwerkzeuge, das L4-Risiko ist hoch. L5 ist nicht erfuellt: kein Aktuator, keine Hardware (SOURCE-SHAPING.tex Z. 24).
- **Was fehlt:** eine scharfe Aussage, Literatur, ein zweites Haus, ein formaler Test, Messbezug.
- **Abhaengigkeit:** voll von I. Fuer ein eigenes Papier zu duenn.

### Kandidat IV: Bildung und Relaxation (heute Anhang B, S. 36-45, dazu BILDUNG-1/-2, Bio 28b/c)

- **Kernaussage (derzeit nur moeglich):** Kleine isolierte Klumpen relaxieren auf die Q-Ball-Familie, das ist in 2D gezeigt. Grosse duennwandige Klumpen behalten eine langlebige Atmung.
- **Belege:**
  - gemischt 2D (Runden 21/22) und 3D (Anhang B)
  - mehrere vorab gewertete Vorhersagen nicht eingetroffen: B3, C0, C1, C4, J2
  - Bio 28c vorab ableitbar
  - Klein-Gordon-Poisson-Schliessung: 4 Punkte
- **Neuheitsstand:** Bildung durch Fragmentierung und nichtlineare Relaxation sind Literatur (KasuyaKawasaki2000 in APPENDIX-FORMATION.tex Z. 5; Ciurla2024 "investigate nonlinear relaxation", LITERATURE.tex Z. 38-39). Das L4-Risiko ist hoch.
- **Was fehlt:** eine Aussage, 3D, ein formaler Test, ein zweites Haus.
- **Moeglicher Haken fuer spaeter:** BILDUNG-LEITER fragt, ob die Relaxationszeit an stillen Stellen einen Gipfel hat [H, ungerechnet]. Faellt diese Pruefung vorab gewertet positiv aus, verbindet sie IV mit I und II.

### Kein Papierstoff

- EW-BAELLE: Lektuere, die Frage ist offen und schwer.
- Codex-Uhr mit Detektor.

## 4. Empfehlung samt Risiken

### 4.1 Empfehlung: zwei Papiere, geschnitten nach Modell und Evidenzstufe, nicht nach den Codex-Anhaengen

1. **Papier I (zuerst): M1-Kern, gekuerzt.**
   - Inhalt:
     - Hauptteil S. 1-20 mit Existenz, Folge, Vorhersagen, Duennwand, nichtlinearer Obstruktion und Schluss.
     - Provenienz.
     - Ein kurzer Anhang nur mit der Projektionsidentitaet (ENVIRONMENT-PROJECTION) und eventuell der analytischen Gegenpuls-Vorhersage.
   - Der Rest von Anhang A und Anhang B wandert in ein datiertes technisches Supplement oder einen Arbeitsbericht. Dieser wird archiviert, nicht eingereicht.
   - SELF-GRAVITY-SCOPE (4 Punkte, bedingt) streichen oder auf einen Ausblicksatz kuerzen.
   - Umfangsschaetzung aus den gemessenen Seitenlagen:
     - Hauptteil 20 Seiten, Provenienz C 2 Seiten (S. 45-46), Literatur 2 Seiten (S. 48-49): 20 + 2 + 2 = 24.
     - Dazu 1 bis 2 Seiten Kurzanhang.
     - Ergebnis: **rund 25 bis 26 statt 49 Seiten.** Das ist eine Schaetzung; der neue Satzspiegel ist nicht gebaut.
2. **Papier II (danach): stille Huellenleitern in M2.**
   - Erst nach einem formalen v3-Test, der die Auflagen aus 3/II erfuellt (Nullfenster, je l ein zweiter Satz), und nach einer Reproduktion durch ein zweites Haus.
   - II zitiert I fuer Mechanismus und Windungsnachweis.
   - Das Halbwellenprinzip wird 2510.27064 zugeschrieben. Neu ist dann nur die Existenz exakt stiller Leitern und ihre vorab gepruefte Vorhersagbarkeit.
3. **Kein eigenes Papier aus Anhang A oder B.**
   - Kandidat IV (Bildung) bleibt geparkt, bis zwei Bedingungen erfuellt sind:
     - eine scharfe, vorab gewertete Aussage, am ehesten BILDUNG-LEITER
     - ein Befund in 3D statt nur in 2D

### 4.2 Reihenfolge und was zuerst fertig werden kann

| Schritt | wer (Rolle) | Voraussetzung |
|---|---|---|
| 1. Ergebnis von ZZZ-ABGLEICH abwarten: Ist die Einfeld-Leiter derselbe Halbwellen-Mechanismus wie in 2510.27064? | laufende Karte | entscheidet, wie I seinen "spacing structure"-Beitrag formulieren darf |
| 2. Literatur in I berichtigen (Azatov als FLS-Arbeit, 2510.27064, 2004.01202), Anhaenge auslagern, README auf v0.37 nachziehen | Autor: Codex (pflegt das Papier); Pruefer liefern nur Anforderungen; frischer Leser eines anderen Hauses liest die letzte Schicht | Finns Ja zum Schnitt |
| 3. Eine Einschliessung von I im zweiten Haus nachrechnen, z. B. C0 | anderes Haus als das, das den Beweis gebaut hat | Reproduktion, kein formaler Test, darf daher parallel zu Schritt 4 laufen |
| 4. Formaler v3-Test fuer II (ein Vertrag, eine Seite, Gegenlesen durch ein anderes Haus) | Leitung | v3 Abschnitt 5: hoechstens ein formaler Test gleichzeitig |
| 5. II reproduzieren (anderes Haus, unabhaengiger Code) und schreiben | anderes Haus | Schritt 4 bestanden |

**Zuerst fertig werden kann I.** Der Kern ist seit v0.13 inhaltlich stabil (Abschnitt 1). Offen sind nur Literatur, Kuerzung, Zweit-Haus-Nachrechnung und Supplement.

### 4.3 Risiken in beide Richtungen

**Zu duenne Einzelpapiere (Salamitaktik):**

- A oder B als eigenes Papier haette keine scharfe Aussage.
  - L4-Risiko hoch, L5 nicht erfuellt.
  - Ein Teil (OU) hat die numerische Akzeptanz nicht bestanden.
  - Geprueft wurde nur in einem Haus.
  - Der gemeinsame Methodenteil wuerde doppelt verwertet.
- II allein wird duenn, wenn es nur "auch in M2 gibt es stille Stellen" sagt. Tragfaehig ist II erst mit Leitern, vorab bestandenen Vorhersagen, Zeitbereichstest und Abgrenzung. Den Sprossenabstand darf II nicht als neues Gesetz verkaufen, denn das Halbwellenprinzip ist Literatur.
- **Gegenfall 1:** Zeigt ZZZ-ABGLEICH, dass die M1-Leiter derselbe Mechanismus ist wie in 2510.27064, verlieren I ("spacing structure") und II (Leiterregel) dasselbe Stueck Neuheit.
  - Dann kann **ein** gemeinsames Papier "BIC in Q-Baellen: Beweise in M1, Leitern in M1 und M2" staerker sein als zwei geschwaechte.
  - Deshalb die Schnittentscheidung I/II erst nach ZZZ-ABGLEICH endgueltig machen.
- **Gegenfall 2:** Faellt der formale M2-Test durch, etwa weil das Nullfenster ebenfalls Stellen annimmt oder neue Sprossen verfehlt werden, schrumpft II auf "es gibt stille Stellen in M2". Das ist dann ein Abschnitt in I oder ein kurzer Brief, kein eigenes Papier.

**Ueberladenes Gesamtpapier:**

- Heute 49 Seiten, davon der Kern auf S. 1-20 und rund 25 Seiten Anhang A/B.
  - Das Abstract (main.tex Z. 16-42) erwaehnt die Anhaenge nicht. Leser sehen nicht, wozu sie da sind.
  - Die Anhaenge sind nur Codex-intern geprueft.
- Schwache Teile ziehen die Beweise mit herunter:
  - gescheiterte OU-Akzeptanz (NUMERICAL-METHOD-CONTROLS)
  - Klein-Gordon-Poisson mit nur 4 Punkten
  - Bildungsaussagen ohne Bildungsnachweis
- Die Evidenzstufen B, N und P vermischen sich. Die v3-Regel fuer Aussagen nach aussen (formaler Test, zweites Haus) laesst sich fuer 49 Seiten nicht erfuellen, fuer 25 Kernseiten schon eher.
- Hohe Pflegelast und Drift:
  - 37 Fassungsnummern zwischen dem 30.09. und dem 02.10. (v0.36 nur als privater Zwischenbau)
  - README seit v0.25 nicht nachgezogen
  - Die Leitung arbeitete in diesem Auftrag noch mit "v0.25".
- M2 als zusaetzlicher Abschnitt in I wuerde I so lange blockieren, bis M2 formal getestet und reproduziert ist.

**Uebergreifend "nur im Modell":**

- Keiner der Kandidaten hat Messbezug (L5). Fuer ein mathematisch-physikalisches Papier ist das zulaessig.
- Teilchen-, Hadronenbeutel-, Gravitations- und Uhr-Deutungen muessen ausserhalb bleiben. Das Papier sagt das heute schon: "no claim of ... a particle model, or an experimental realization" (Abstract).
- Die Bildungsbefunde sind 2D-Befunde und duerfen nicht als Stuetze fuer 3D-Bildung gelesen werden.

## 5. Offene Entscheidungen fuer Finn

1. **Schnitt:** Zwei Papiere (I M1-Kern, II M2-Huellenleitern) oder ein gemeinsames BIC-Papier?
   - Empfehlung: zwei.
   - Endgueltig erst nach ZZZ-ABGLEICH entscheiden (Gegenfall 1 in 4.3).
2. **Kuerzung von I:** Anhang A und B (bis auf die Projektionsidentitaet) in ein archiviertes technisches Supplement? SELF-GRAVITY-SCOPE streichen? Codex pflegt das Papier und braucht dafuer einen klaren Auftrag.
3. **Huellenstrang nach aussen:** ja oder nein. Bei ja:
   - formaler v3-Test mit Nullfenster und je l einem weiteren Satz
   - danach Reproduktion durch ein zweites Haus; welches Haus, entscheidet Finn
   - Der Strang ruht laut RUNDE-21.md Z. 80 und RUNDE-22.md Z. 7 bis zu dieser Entscheidung.
4. **Zweit-Haus-Nachrechnung einer Einschliessung von I** (z. B. C0): Haus und Budget. Ohne sie bleibt I nach v3 nur eine interne Fassung.
5. **Literaturberichtigung in I sofort beauftragen?**
   - Unabhaengig vom Schnitt: Azatov2024 als FLS-Arbeit, 2004.01202.
   - 2510.27064 erst nach ZZZ-ABGLEICH.
6. **Veroeffentlichungsweg:** Preprint ja oder nein, und wann; Supplement mit Lizenz und Archiv-ID (README Z. 44-49). Bisher ist nichts freigegeben (README Z. 4).

### Auflagen aus dieser Pruefung (Anforderungen, kein Wortlaut)

| Kennz. | Auflage |
|---|---|
| PS-1 | Versionsstand richtigstellen: Das Papier ist Draft 0.37 mit 49 Seiten, nicht v0.25. README auf v0.37 nachziehen; die Notizen zu v0.26 bis v0.37 liegen nur in den Stage-Ordnern |
| PS-2 | Fuer Ergaenzungen seit HEAD nicht `git diff --stat` allein nehmen. Die 8 neuen Abschnittsdateien sind ungetrackt und erscheinen dort nicht |
| PS-3 | LITERATURE.tex: Azatov2024 auch als FLS-Arbeit fuehren; 2004.01202 abgrenzen; 2510.27064 nach ZZZ-ABGLEICH abgrenzen, weil es den zentralen Beitrag "spacing structure" (main.tex Z. 71-72) beruehrt |
| PS-4 | Vor jeder Aussage nach aussen fuer I: eine Einschliessung im zweiten Haus reproduzieren |
| PS-5 | Fuer II: im formalen Test eine echte Gegenprobe (L2, z. B. Nullfenster um einen halben Sprossenabstand versetzt, gleiches Annahmekriterium); je l ein zweiter vorab gewerteter Satz; Reproduktion im zweiten Haus; genaue M2-Form in der Literatur pruefen |
| PS-6 | Phasenregel nie als Ergebnis fuehren, nur als "vorab nicht als geschlossener Baustein bestaetigt (LF2), Korrekturen nachtraeglich [H]" |
| PS-7 | RUNDE-21.md Z. 76 ("je zweimal") per neuem Eintrag berichtigen: zwei Tests insgesamt, je l einer |
| PS-8 | Bildung, Toechter und Drehimpuls nur als 2D-Befunde im Modell fuehren; Bio 28c nur beschreibend; nicht als Stuetze fuer 3D-Bildung im Papier |

### Quote der geprueften Angaben

Geprueft habe ich 9 Angaben aus dem Auftrag und aus den Rundenprotokollen der Leitung.

- **Bestaetigt (5):**
  - Papierdateien seit HEAD geaendert
  - zwei vorab bestandene Sprossentests
  - Berichtigungsbedarf zu Azatov2024 sowie fehlende Abgrenzung zu 2510.27064 und 2004.01202 (grep in LITERATURE.tex und bibliography.tex: 0 Treffer)
  - Toechter und Drehimpuls (Bio 28b/c)
  - EW-BAELLE als reine Lektuere
- **Mit Einschraenkung (2):**
  - Die Phasenregel ist kein bestandenes Ergebnis, denn LF2 traf nicht ein.
  - Die Bildung gilt nur in 2D und nur an einem Familienpunkt.
- **Falsch (2):**
  - "v0.25": Der Stand ist Draft 0.37.
  - RUNDE-21.md Z. 76: "je zweimal".

### Grenzen dieser Pruefung

- **Gelesen:**
  - im Papier: Abstract und Einleitung, der Diff seit HEAD, die neuen Abschnitte (Anfang und Ueberschriften), APPENDIX-*, SELF-GRAVITY-SCOPE, LITERATURE Z. 20-40 und das README ganz
  - Stage-Notizen v26 bis v37: nur die Anfaenge
  - RUNDE-17 bis -22: Ernten und Abschaetzungen; von den ERGEBNIS-Dateien nur fls-stille in Teilen und sprossen-vorab ueber die Ueberschriften
- **Nicht gelesen:** PROOF.tex, NONLINEAR.tex, MONOPOLE-BOUND.tex im Einzelnen und die uebrigen ERGEBNIS-Dateien ganz. Deren Zahlen stammen aus den Ernten der Leitung.
- **Literatur:** Die Angaben zur Literatur stammen aus fls-stille. Selbst geprueft habe ich nur das Papier (grep: 0 Treffer fuer 2510.27064 und 2004.01202; Azatov-Passage gelesen), nicht die Primaerquellen.
- **Nicht geoeffnet:** RUNDE-22/codex-blick/ und RUNDE-22/zzz-abgleich/. Aus RUNDE-22.md bin ich nur bis Z. 238 gelesen, nicht den Eintrag "ZZZ-ABGLEICH gestartet".
- **Git:** nur lesend (diff, status, log, ls-tree, mit GIT_OPTIONAL_LOCKS=0), wie im Auftrag ausdruecklich erlaubt.
  - Die festen Pruefregeln sagen "kein git"; der Auftrag geht nach seiner Widerspruchsregel vor.
  - pdftotext lief nur nach stdout.

## 6. Einfach gesagt

Unser Papier ist in drei Tagen von 12 auf 49 Seiten gewachsen. Der eigentliche Kern steht aber seit Tagen fest: drei bewiesene "stille Schwingungen" eines Q-Balls und ihre Leiter. Dazugekommen sind vor allem lange Anhaenge ueber das Anstossen und das Entstehen der Baelle, und die sind noch wackelig. Ausserhalb des Papiers liegt ein zweiter Fund: Auch ein Q-Ball mit Huelle hat viele stille Schwingungen auf Leitern, und wir haben 22 neue Sprossen vorher richtig angesagt. Mein Rat: zwei schlanke Papiere statt eines dicken, zuerst das Beweispapier und das Huellenpapier erst, wenn ein zweites Team nachgerechnet hat und ein sauberer Test bestanden ist. Aus den Anhaengen allein sollte man kein eigenes Papier machen, das waere zu duenn.
