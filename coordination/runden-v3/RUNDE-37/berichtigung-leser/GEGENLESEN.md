Urteil: veroeffentlichbar nach woertlicher Uebernahme von A1 bis A4 (4 A, 10 B, 11 C)


- Beginn: 2026-10-04 22:12:35 CEST (date)
- Zeitbox: 25 Minuten
- Ende der Pruefung: 2026-10-04 22:26:35 CEST (date, vor diesem Eintrag); Dauer 22:12:35 bis 22:26:35 = 14 min 0 s
- Gelesen: Gegenstand ganz; Journal (jq title/result/meaning); RUNDE-43.md Z. 117, 199-256, 300-345, 605-608 (Rest per grep); SAGNAC.md Z. 51-75; ROOT-CHECK, DIMENSION-REVIEW, ROOT-REVIEW-2003, ATEM-DYNAMIK-CHECK, PEER, PEER-ADDENDUM ganz; DREIPOL3-REVIEW Z. 120-165; EVOLUTION-FINDING ganz; BCW Z. 445-480; Marolf-Text Z. 126-131, 196-218; Hamilton/Lisle Z. 10-24, 585-602; FARB-EIS-Dossier, DIM-LEITER-, DREIPOL-2-, WEYL-LINEAR-2-ERGEBNIS und GAMMA-NETZ-L-Dossier in Ausschnitten; atem.py Z. 701-739; FLUSS-UND-ZITTERN.md per grep. Keine Datendateien, nichts Versiegeltes, kein KS-1.

## 1. Alte Wortlaute (woertlich?)

Journal (jq '.title, .result, .meaning' auf claude-runde-v3-43-20261004.json, gelesen 22:14):
- I-1 result-Zitat: woertlich vorhanden.
- I-2 result-Zitat "FARB-EIS-R3-L: SU(3) braucht drei Rishons je Kante." und meaning-Zitat "Kleber: Echtes SU(3) braucht drei Bausteine je Kante.": beide woertlich.
- I-3 meaning-Zitat: woertlich.
- I-4 result-Ausschnitt "2D-Dreifarben-Dreieck lokales Minimum": woertlich (Teilsatz).
- I-5 meaning-Ausschnitt: woertlich (Teilsatz).

RUNDE-43.md (626 Zeilen):
- DIM-LEITER-QBALL-1, Bedeutung (Z. 251-252): Alt-Zitat woertlich. Der vorangehende Satz derselben Bedeutung ("Unser Q-Ball pendelt sich nicht bei 3 bis 4 Dimensionen ein.") wird nicht zitiert; unkritisch.
- FARB-EIS-R3-L (Z. 331-332): Zitat sinngemaess woertlich; im Original stehen "Extensiv" und "zusammenhaengend" in eigenen Anfuehrungszeichen, und der Satz steht unter "Ableitbarkeit FARB-EIS-1 [M, Agent, nicht gegengelesen]", nicht unter "Bedeutung".
- ATEM-NETZ-1, Bedeutung (Z. 316-318): Alt-Zitat woertlich (erster Halbsatz von Z. 317-318).
- **ISO-ATEM-1, Bedeutung (Z. 275-276): Das Zitat "ohne Energie" steht NICHT in RUNDE-43.md** (grep: null Treffer in der Datei). Die Bedeutung lautet dort: "Finns Netz kann als Ganzes in alle Richtungen gleich atmen, ohne dass sich ein Tetraeder verbiegt, und zwar auf zwei Arten." Die Wendung "ohne Energie" steht in RUNDE-43/WEICHE-STAND-v7.md Z. 95, RUNDE-43/WEICHE-STAND-v8.md Z. 114 (dort schon mit "Im Modell starrer Tetraeder"), RUNDE-37/iso-atem-1/KARTE.md Z. 36 und ERGEBNIS.md Z. 60. Siehe A1.
- Protokollzeile 19:31:31 (Z. 319): Zitat woertlich (endet im Original mit ", wie bei Regge/CDT.").

## 2. Neue Wortlaute gegen die Grundlagen

- **I-1:** Bedingungen (dQ/domega < 0, E < Q, radial, keine Eigenwertzaehlung, keine nichtradialen Stoerungen, keine Zeitentwicklung, gleiche dimensionslose Festlegung) treu zu DIMENSION-REVIEW Z. 7-26 und 38-43. Zahlen stimmen mit ERGEBNIS-Tabelle Z. 57-67: Q_s(3) = 141,497, Q_s(12) = 2,60921e13. **Der Schlusssatz verwechselt aber zwei Groessen** (A2): Fensterrand-Werte sind fuer D = 7 bis 12 die Q_min (Tabelle: "2,47197e6 (Rand)" bis "9,36754e12 (Rand)", Erklaerung Z. 69), nicht die eben genannten Q_s; die Q_s liegen im Fenster (omega_s = 0,957729 bis 0,974048).
- **I-2:** "antisymmetrisierte Mehrwegterme" und "kein Satz" treu zu ROOT-CHECK 6 und BCW Z. 462-466. **Aber "mit einem Rishon ist das Modell U(3)" steht unbedingt da** (A3); BCW Z. 465-466 und PEER-ADDENDUM sagen ausdruecklich "even with the fundamental representation of SU(2N)", und das ist ein Rishon je Kante (Dossier Z. 66: "Fundamentale Darstellung (1 Rishon, 2N = 6 Zustaende)"; Dossier V1 Z. 35 nennt "Rishonzahl 1 ist fuer SU(3) ausgeschlossen" selbst "Teilweise verletzt"). RUNDE-43.md Z. 327 hatte noch "ohne Zusatzterme"; die Berichtigung streicht diese Einschraenkung.
- **I-3:** Vier Voraussetzungen treu zu ROOT-CHECK 5 und Marolf-Text (A4-marolf-1409.2509.txt Z. 126-131 Def. I; Z. 196-218 Herleitung und Satz: "universal coupling to energy, the same notion of time evolution, and a compatible definition of locality"). "weder ein Gegenbeweis noch ein Ausweg" verkuerzt ROOT-REVIEW-2003 Z. 57-58 ("weder Gegenbeweis noch hinreichender Ausweg"), siehe B2. "Nicht jeder physikalische Netzumbau muss eine reine Umbenennung sein" entspricht ROOT-REVIEW-2003 Z. 58-59 und PEER Z. 5; "physikalische" ist sprachlich schief (C1).
- **I-4:** Treu zu ROOT-CHECK 1 ("supports tested local energy landscape, not ... full stability"). "aus allen geprueften Richtungen" ist aber genau die Wendung, die der DREIPOL-2-Leser schon ersetzt hat (ERGEBNIS Z. 211: '"6 + 9 Richtungen" ersetzt durch "drei Klassen und 9 Zufallsstoerungen"'; Z. 291). Zwei der sechs Stoerungen (P1, P2) sind exakte Symmetrien (Z. 92-93), L3 (Sektor 63/57/60) kehrt nicht zurueck (Z. 94, ohne Urteil). Siehe B3.
- **I-5:** Treu zu ROOT-REVIEW-2003 Z. 42-44.
- **RUNDE-43.md DIM-LEITER:** Kriterienlesart und "keine Naturkonstante" treu zu DIMENSION-REVIEW Z. 14-15 und 38-43. Der erste Halbsatz "Die Drei ist die erste Dimension, in der ..." bleibt unberichtigt, siehe B1.
- **RUNDE-43.md FARB-EIS "Extensiv/zusammenhaengend":** Schwellen stimmen mit Dossier Z. 123 (groesste Komponente > 50 %; ln(Zahl)/54 gegen 0,10). "gilt nur fuer N = 54" ist aber enger als Codex ("finite N54 pair of particular thresholds") und als die Rechnung, siehe B4.
- **RUNDE-43.md ATEM-NETZ-1:** "vorgegebener Formzyklus", "ueberdaempfte Bewegung erster Ordnung", "keine Selbstordnung", "kein energieerhaltender Motor", "Arbeit vom vorgegebenen Antrieb" treu zu ATEM-DYNAMIK-CHECK Z. 6-12 und 19-25. **"Es dreht sich wie ein Schwimmer bei kleiner Reynoldszahl" steht in keiner Grundlage** (grep "reynolds|Purcell|Schwimmer" ueber latest-claude-20261004, breathing-trimer-20261004, atem-netz-1, RUNDE-43.md: nur die Berichtigung selbst), siehe B5. "feste Federn": Im Code (atem.py Z. 715-720) sind die Ruhelaengen zeitabhaengig, ell = (d_i + d_j)/2 mit d = 1 + EPS sin(...), siehe C2.
- **Trimer-Satz:** "energieerhaltend", "Gesamtdrehimpuls null", "Dreipunkt-Modell" stimmen mit EVOLUTION-FINDING Z. 16-29 und 37-40. Es fehlen die Grenzen derselben Datei (Z. 45-53), siehe B6.
- **ISO-ATEM-1:** Inhalt treu zu ROOT-CHECK 2 und ROOT-REVIEW-2003 Z. 61-62, aber das Zitat sitzt an der falschen Stelle (A1); "Modenkopplung" aus ROOT-CHECK Z. 35 fehlt in der Aufzaehlung (C3).

## 3. Rueckwaerts: fehlende Stellen

Titel, result und meaning vollstaendig gegen ROOT-CHECK, ROOT-REVIEW-2003, DIMENSION-REVIEW, ATEM-DYNAMIK-CHECK gelesen (dazu DREIPOL3-REVIEW Z. 120-165, weil ROOT-REVIEW-2003 Z. 26 darauf verweist):
- **Titel "im Zufallsnetz kein lineares Tempo-Glied mehr"**: zu stark nach ROOT-REVIEW-2003 Z. 32-33 ("<2sigma gegen null bedeutet Nullvertraeglichkeit, nicht Abwesenheit eines linearen Terms"). Das meaning sagt richtig "nicht mehr nachweisbar", der Titel nicht. WEYL-LINEAR-2/ERGEBNIS.md Z. 39: "0,001 liegt am Rand" des 95-%-Bereichs; Z. 52-54: Vorab-Bedeutung "kein lineares Glied" ist "nicht bewiesen". Siehe A4.
- **result "Entmischung in 3D ab 600 bis 650 (Nachtrag)"**: ROOT-REVIEW-2003 Z. 22-23 "beschreibt eine moegliche Entmischung"; DREIPOL3-REVIEW Z. 160-162 schlaegt vor: "mit einer Entmischungs-Verzweigung zwischen 600 und 650 ... vereinbar". Siehe B7.
- **Titel und meaning zu gamma** ("gamma = 1 folgt am Schreibtisch, wenn Masse-Energie und Takt in der Eckregel stecken"): ROOT-REVIEW-2003 Z. 52-53 verlangt Lapse, Quellenkopplung UND geklaerte Zwangsbedingungen; die dritte Bedingung fehlt. GAMMA-NETZ-L/DOSSIER.md Z. 56 (V3) nennt die Regeln selbst ein "Paar zweiter Klasse". Codex las um 20:03 noch kein Dossier. Siehe B8.
- **result "3D-Tropfen bei Q1 = 800 3,32 unter dem Mischball"**: ROOT-CHECK Z. 15-16: Arm nach den Hauptergebnissen, "not an untouched prior prediction"; DREIPOL-2/ERGEBNIS Z. 294: in 3D nur Fixpunkt des symmetrischen Flusses. Kein Stabilitaetsanspruch im Eintrag, aber ohne Kennzeichnung. Siehe C8.
- Geprueft und ohne Befund: VERSCHRAENK-DIM-1 (N-Abhaengigkeit D* ~ 0,53 ln N - 0,5 steht da, passt zu ROOT-CHECK Z. 54-55); ISO-ATEM-1-result ("zweite isotrope Atemform", kein "nur zwei"); ATEM-NETZ-1-result ("ordnen sich 2 + 2" = ROOT-CHECK Z. 42 "local 2+2"); GEMEINSAMES-NETZ-L-result (nur Literaturliste); DIM-AUSWAHL-L ("kein Einpendeln ... belegt"); Titel nennt beim Guertel keinen Spin 1/2.
- **RUNDE-43.md**, nicht im Abschnitt "Lesarten" erfasst, gleicher Codex-Grund (B10): Z. 223-224 (GEMEINSAMES-NETZ-L-Bedeutung "Fuer ein festes Netz mit eigener Uhr gibt es einen Beweis ... Einstein-Schwerkraft nein. Das gemeinsame Netz braucht entweder Geometrie als Netz selbst (mit Eichredundanz), Nichtlokalitaet oder Holografie."; ROOT-CHECK Z. 62-67); Z. 316-317 ("die grosse gemeinsame Eis-Ordnung braucht Rauschen und sehr viele Takte"; ROOT-CHECK Z. 43-44: "separate averaged diagnostic, not the same full dynamics"); Tabellenzeilen Z. 605 ("kleinste stabile Ladung") und Z. 608 ("echtes SU(3) braucht drei Rishons je Kante; ein Rishon gibt U(3)").

## 4. Zahlen und Zeilenangaben

- Journal "erschien um 22:01": recorded_at 2026-10-04T20:01:45 UTC = 22:01:45 CEST. Stimmt.
- Codex-Dateien "seit 19:34": mtime DIMENSION-REVIEW und PEER 19:34, ROOT-CHECK und PEER-ADDENDUM 19:35. Plausibel.
- 141,5 und 2,6e13: Q_s(3) = 141,497; Q_s(12) = 2,60921e13 (ERGEBNIS-Tabelle). Stimmt.
- "12 bis 24": Faktoren 12,05 bis 23,51 (ERGEBNIS Z. 80). Nachgerechnet: 141,497 x 12 = 1697,96, Rest 7,28/141,5 = 0,05, also 1705,24/141,497 = 12,05; 1,10962 x 23,5 = 26,076, Rest 0,016/1,11 = 0,01, also 23,51. Stimmt.
- 3,32 (DREIPOL-2): 1923,30784 - 1919,98575 = 3,32209 (ROOT-CHECK Z. 12-13). Stimmt.
- N = 54, Entropie > 0,10, groesster Teil > 50 %: Dossier Z. 28 und 123. Stimmt. Kontrolle: 2^(54/9) = 2^6 = 64; ln 128 = 7 x 0,693 = 4,852; 4,852/54 = 0,090 < 0,10.
- ROOT-CHECK "Z. 125-252" fuer Marolf: so in ROOT-CHECK Z. 58-59; Def. I steht in A4-marolf-1409.2509.txt Z. 126, Def. II Z. 168, Satz Z. 216-218. Stimmt.
- BCW "Z. 450-478": stimmt mit ROOT-CHECK Z. 81; die tragende Stelle ist Z. 462-468 (grep: "antisymmetrized combinations" Z. 463, "fundamental representation of SU(2N)" Z. 466, "15-dimensional" Z. 467).
- Hamilton/Lisle "Abstract Z. 15-22": Der Kerr-Satz beginnt in Z. 14 ("We show that the river model works also for rotating (Kerr-Newman)"), "no azimuthal swirl" Z. 17, twist Z. 18-19. Genauer Z. 14-23 (C4). "Z. 589-599": stimmt genau ("But the river has a surprising twist" bis "gradients in the twist of the river").
- SAGNAC.md 4.3: alter Wortlaut Z. 68-71, woertlich bis auf die Anfuehrungszeichen um Drall (Original doppelt, C5).
- Protokollzeile 19:31:31 = RUNDE-43.md Z. 319. Stimmt.

## A-Befunde

**A1 (ISO-ATEM-1: Zitat an falscher Stelle).** "ohne Energie" steht nicht in RUNDE-43.md (null Treffer); die Bedeutung dort (Z. 275-276) lautet anders. Ersatz fuer den Punkt "ISO-ATEM-1, Bedeutung":

> - **ISO-ATEM-1, Bedeutung (Z. 275-276):**
>   - Alt: "Finns Netz kann als Ganzes in alle Richtungen gleich atmen, ohne dass sich ein Tetraeder verbiegt, und zwar auf zwei Arten."
>   - Neu: Das gilt im Modell starrer Tetraeder. Null Verformungsenergie heisst weder null Bewegungsenergie noch eine kostenlose Uhr. Dafuer fehlen Traegheit, Rueckstellkraft, Antrieb, Daempfung und Modenkopplung. "Auf zwei Arten" heisst: zwei gefundene Scharen; dass es nur diese zwei gibt, zeigen die Zufallsstarts nicht (ROOT-CHECK.txt 2).
>   - Die Wendung "ohne Energie" steht in RUNDE-43/WEICHE-STAND-v7.md Z. 95 und RUNDE-37/iso-atem-1/ERGEBNIS.md Z. 60; dort gilt dieselbe Ergaenzung.

**A2 (I-1: Schlusssatz verwechselt Q_min und Q_s).** Die genannten 141,5 und 2,6e13 sind Q_s, die Schwellen mit E = Q. Sie liegen im Fenster (omega_s = 0,957729 bis 0,974048 fuer D = 7 bis 12). Fensterrand-Werte sind dort die Q_min (ERGEBNIS-Tabelle "(Rand)", Z. 69; DIMENSION-REVIEW Z. 50-53, 68-69). Ersatz fuer den letzten Satz von I-1:

> Fuer D = 7 bis 12 hat Q(omega) im Fenster kein inneres Minimum; die kleinste Ladung der Familie ist dort ein Fensterrand-Wert bei omega^2 = 0,9999. Die genannten Schwellen mit E < Q liegen dagegen im Fenster.

**A3 (I-2: neue unbedingte Aussage "mit einem Rishon ist das Modell U(3)").** BCW Z. 465-466: "one can construct SU(N) invariant quantum link Hamiltonians even with the fundamental representation of SU(2N), but with more complicated interactions". Die Fundamentaldarstellung ist ein Rishon je Kante (Dossier Z. 66: "1 Rishon, 2N = 6 Zustaende"; Zaehlung C(6,1) = 6, C(6,2) = 15, C(6,3) = 20, passt zu den "20 Zustaenden" bei drei Rishons in RUNDE-43.md Z. 325). Codex nennt das ausdruecklich (ROOT-CHECK Z. 84; PEER-ADDENDUM "sogar in fundamentaler SU(2N)"). RUNDE-43.md Z. 327 hatte noch "ohne Zusatzterme". Ersatz fuer den Neuen Wortlaut von I-2:

> FARB-EIS-R3-L: In der einfachen Einzelkanten-Determinanten-Bauweise von Brower/Chandrasekharan/Wiese braucht SU(3) drei Rishons je Kante; mit einem Rishon und ohne Zusatzterme ist das Modell U(3). BCW nennen ausdruecklich antisymmetrisierte Kombinationen mehrerer Wege zwischen zwei Gitterpunkten, die das zusaetzliche U(1) brechen, und zwar schon in der Fundamentaldarstellung von SU(2N), also mit einem Rishon je Kante, dann mit verwickelteren Wechselwirkungen. Es ist also kein Satz, dass jede SU(3)-Physik drei Bausteine je Kante braucht.

**A4 (Rueckwaerts: Titel zu WEYL-LINEAR-2 fehlt).** Die Berichtigung erklaert "Alle uebrigen Aussagen des Eintrags bleiben unberuehrt" und bestaetigt damit den Titelsatz, den Codex ausdruecklich beanstandet (ROOT-REVIEW-2003 Z. 32-33). Ersatz: neue Zeile in Teil I:

> | I-6 | title: "im Zufallsnetz kein lineares Tempo-Glied mehr" | im Zufallsnetz ist kein lineares Tempo-Glied mehr nachweisbar; der Wert ist mit null vertraeglich, ein Glied der Groesse 0,001 liegt am Rand des 95-%-Bereichs (-0,0011 bis +0,0009). | ROOT-REVIEW-2003.txt 2; RUNDE-37/weyl-linear-2/ERGEBNIS.md Z. 39 und 52-54 |

Folge: In "Was Finn erfaehrt" die Zahl "Drei Saetze" anpassen.

## B-Befunde

- **B1 (DIM-Bedeutung, erster Halbsatz bleibt stehen).** "Die Drei ist die erste Dimension, in der kleine Klumpen zerfallen koennen" wird nicht berichtigt. Codex: keine Auswahl von drei Dimensionen (ROOT-CHECK Z. 52-53), kein ausgezeichnetes Fenster bei D3/4 (DIMENSION-REVIEW Z. 12-13). Zudem haengt "erste" am Vorzeichen von E - Q in D = 2 am oberen Rand: E/Q = 0,9999999974, Abstand 1 - 0,9999999974 = 2,6e-9, ohne eigene Fehlerkontrolle (DIMENSION-REVIEW Z. 56-58). Vorschlag: "Dass D = 3 die erste solche Dimension ist, haengt an der gemeinsamen Festlegung und am Vorzeichen von E - Q in D = 2 nahe omega -> 1, das nicht eigens kontrolliert ist; eine ausgezeichnete Dimension folgt daraus nicht."
- **B2 (I-3, "kein Ausweg").** Codex schreibt "weder Gegenbeweis noch hinreichender Ausweg" (ROOT-REVIEW-2003 Z. 57-58) und "does not verify an escape" (ROOT-CHECK Z. 65-66). "noch ein Ausweg" klingt nach Urteil. Vorschlag: "allein weder ein Gegenbeweis noch ein hinreichender Ausweg". Auch in "Was Finn erfaehrt": "kein hinreichender Ausweg fuer sich".
- **B3 (I-4, "aus allen geprueften Richtungen").** Der DREIPOL-2-Leser hat genau diese Wendung ersetzt (ERGEBNIS Z. 211, Endfassung Z. 291: "in drei nichttrivialen Stoerungsklassen und 9 [Zufallsstoerungen]"); P1/P2 sind exakte Symmetrien, L3 kehrt nicht zurueck (anderer Ladungssektor). Vorschlag: "kehrt es in drei nichttrivialen Stoerungsklassen und 9 Zufallsstoerungen zurueck (Stichprobe)".
- **B4 (FARB-EIS, "gilt nur fuer N = 54").** Codex: "finite N54 pair of particular thresholds" = nur dort gezeigt, nicht nur dort gueltig. Gegenfall aus der Dossierrechnung selbst: Die Komponentenschranke 2^(N_tet/9) gibt hoechstens ln 2/9 = 0,693/9 = 0,077 Entropie je Tetraeder, also ist eine solche Komponente selbst extensiv; den Ausschluss macht die Schwelle 0,10 > 0,077. Mit denselben Schwellen gaelte er (falls die Schranke allgemein haelt, [M, nicht gegengelesen]) fuer jedes N_tet ab 31: 0,077 + 0,693/N < 0,10 heisst 0,693/N < 0,023, also N > 30,1. Vorschlag: "ist nur fuer N = 54 mit den zwei gewaehlten Schwellen gezeigt und haengt an der Schwelle 0,10; eine Komponente mit 2^(N/9) Zustaenden waere selbst extensiv."
- **B5 (ATEM-NETZ-1, "Schwimmer bei kleiner Reynoldszahl").** Steht in keiner Grundlage (grep, Abschnitt 2); eigene Analogie der Leitung ohne Kennzeichnung. Sie ueberkorrigiert ausserdem: Im Code (atem.py Z. 714-724) sind alle Kraefte paarweise zentral, und xdot = g F mit gleichem g. Damit gilt Summe x_i x xdot_i = g Summe x_i x F_i = 0, dieselbe Bedingung wie Drehimpuls null bei gleichen Massen. Die Drehung je Takt ((pi/2) eps^2, RUNDE-43.md Z. 305-306) ist die geometrische Phase der Formschleife, wie bei der Katze; Codex selbst: "A vanishing net torque does not force the best-fit orientation to remain fixed" (ATEM-DYNAMIK-CHECK Z. 24-25). Falsch am alten Satz war das Bild eines traegen, energieerhaltenden Koerpers, nicht die Geometrie. Vorschlag: statt des Schwimmer-Satzes Codex' Wortlaut (ATEM-DYNAMIK-CHECK Z. 11-12) "geometrische Umorientierung unter einem vorgegebenen Formzyklus"; die Katze darf als geometrischer Vergleich bleiben, wenn "ueberdaempft und angetrieben, nicht traege" dabeisteht (das ist meine Lesart, nicht Codex').
- **B6 (Trimer-Satz ohne Grenzen).** EVOLUTION-FINDING nennt selbst: kleine Winkel (-0,00038 rad bei epsilon 0,01; -0,0015 rad bei 0,02; Z. 17-22), Form nicht exakt geschlossen, keine periodische Bahn, kein starrer Rotor (Z. 45-50), Bindung im Paarpotential vorgegeben, nur 2D (Z. 51-53), keine unabhaengige Replikation (Z. 13-14). Vorschlag anhaengen: "(endlicher Befund mit kleinen Winkeln; Form nicht exakt geschlossen, keine periodische Bahn, 2D, nicht unabhaengig nachgerechnet)".
- **B7 (Rueckwaerts, Entmischung 600 bis 650).** Vorschlag als neue Zeile: result "Entmischung in 3D ab 600 bis 650 (Nachtrag)" -> "beschreibende Abtastung, vereinbar mit einer Entmischungs-Verzweigung zwischen 600 und 650 in 3D (Nachtrag); Ordnung und Schwelle offen" (ROOT-REVIEW-2003 Z. 22-25; DREIPOL3-REVIEW Z. 159-162).
- **B8 (Rueckwaerts, gamma).** Titel und meaning nennen zwei von drei Codex-Bedingungen (ROOT-REVIEW-2003 Z. 52-53). Vorschlag: "... wenn Masse-Energie und Takt in der Eckregel stecken und die Zwangsbedingungen geklaert sind (die Regeln sind bisher ein Paar zweiter Klasse, GAMMA-NETZ-L V3)".
- **B9 (I-1, Stabilitaet).** Fehlt: E < Q prueft nicht alle Mehrball- und Spaltkanaele (DIMENSION-REVIEW Z. 24-26). Ein Halbsatz genuegt.
- **B10 (RUNDE-43.md unvollstaendig).** Die in Abschnitt 3 genannten Stellen Z. 223-224, 316-317, 605, 608 fehlen im Abschnitt "Lesarten"; mindestens 605 und 608 wiederholen woertlich die berichtigten Aussagen.

## C-Befunde

- **C1 (I-3):** "Nicht jeder physikalische Netzumbau muss eine reine Umbenennung sein" ist schief, weil ein physikalischer Umbau per Definition keine Umbenennung ist. PEER Z. 5: "Nicht jeder Netzumbau muss reine Umbenennung sein."
- **C2 (ATEM-NETZ-1):** "feste Federn" liest sich wie feste Ruhelaengen; im Code sind sie zeitabhaengig (atem.py Z. 715 und 720). Besser: "staendige, auch ziehende Federn mit vorgegebenen, zeitabhaengigen Ruhelaengen" (ATEM-DYNAMIK-CHECK Z. 7 und 16).
- **C3 (ISO-ATEM-1):** "heisst nicht null Bewegungsenergie und keine kostenlose Uhr" besser "heisst weder ... noch ..."; "Modenkopplung" fehlt (ROOT-CHECK Z. 35). In A1 schon eingearbeitet.
- **C4 (II-1):** "also eine Lorentz-Transformation" besser wie die Quelle: "also eine Lorentz-Struktur aus sechs Zahlen (Geschwindigkeit und Drehung)" (H/L Z. 18-19). Zeilenangabe Abstract besser Z. 14-23.
- **C5 (II-1):** Im Original steht "Drall" in doppelten Anfuehrungszeichen (SAGNAC.md Z. 69); Fundstelle Z. 68-71 angeben.
- **C6 (FARB-EIS):** Der Satz "Extensiv und zusammenhaengend ..." steht in RUNDE-43.md unter "Ableitbarkeit FARB-EIS-1 [M, Agent, nicht gegengelesen]", nicht unter "Bedeutung"; diesen Status mitnennen.
- **C7 (I-3):** "Energie als Randfluss" um "universell" ergaenzen (Marolf Def. I, Z. 126-131: "universal coupling to energy"; ROOT-CHECK Z. 60).
- **C8 (Rueckwaerts, DREIPOL-2):** "3D-Tropfen bei Q1 = 800 3,32 unter dem Mischball" als Nachtrag N1 nach Sicht und als Fixpunkt des symmetrischen Flusses kennzeichnen (ROOT-CHECK Z. 15-16, 22; ERGEBNIS Z. 120, 294).
- **C9 (WEYL-LINEAR-2, ausserhalb der Berichtigung):** Der Journalwert "+0,00005 +- 0,0005" ist der Ansatz-A-Wert (ERGEBNIS Z. 117); das WM1-Urteil steht auf Ansatz B, -0,00023 +- 0,00063 (Z. 47). Der 95-%-Bereich in Z. 39 (-0,0011 bis +0,0009, Mitte -0,0001) passt nicht zu symmetrisch +0,00005 +- 1,96 x 0,0005 (1,96 x 0,0005 = 0,00098, also -0,00093 bis +0,00103); vielleicht Bootstrap-Perzentile, nicht geprueft.
- **C10 (Titel gegen meaning, ausserhalb der Codex-Hinweise):** Titel "auf Finns Tetraeder-Netz", meaning "auf Finns Diamant-Netz"; nicht geprueft, welches stimmt.
- **C11 ("Was Finn erfaehrt"):** Nach A4 sind es vier Saetze; Marolf-Zeile nach B2 ("kein hinreichender Ausweg").

## Urteil

**Veroeffentlichbar nach woertlicher Uebernahme von A1 bis A4.** Die alten Wortlaute des Journals stimmen, die Grundlagen sind ueberwiegend treu wiedergegeben, die Zahlen stimmen. Es gibt aber drei Stellen, an denen die Berichtigung selbst falsch oder irrefuehrend ist: A1 (Zitat nicht in der Quelle), A2 (Q_min mit Q_s verwechselt) und A3 (neue unbedingte U(3)-Aussage gegen BCW Z. 465-466). Dazu kommt A4: Ein von Codex ausdruecklich beanstandeter Titelsatz bliebe mit dem Vermerk "unberuehrt" bestaetigt. B1 und B5 empfehle ich dringend: Ohne B1 bleibt die Sonderstellung der Drei stehen, und B5 ueberkorrigiert ohne Quelle. Formuliert die Leitung statt der Ersatztexte eigene, braucht diese Schicht einen frischen Leser.

## Nicht geprueft

- Bus-Nachrichten 19855775 und 5537c5bb und die Zeit 16:14 (kein Peerbus erlaubt).
- Marolf-PDF nicht geoeffnet, nur die gespeicherte Textfassung A4-marolf-1409.2509.txt (Z. 126-131 und 196-218 gelesen; Def. II Z. 168 ff. nur per grep).
- BCW Z. 434-444 und 705-718 (Determinante braucht drei Rishons) nicht gelesen; "braucht" in der Einzelkanten-Bauweise uebernommen aus RUNDE-43.md und ROOT-CHECK ("stated SU3 choice").
- Ob Hamilton/Lisles "kein Wirbel" an ihrer Wahl des Bezugsrahmens (Doran-Form) haengt; nur Abstract und Z. 585-602 gelesen.
- Die Gravity-Probe-B-Zahlen (aus SAGNAC.md, [L]).
- Keine Datendateien und kein auswertung.json geoeffnet; die E/Q-Werte zu D = 2 stammen aus DIMENSION-REVIEW.
- ATEM-NETZ-1/ERGEBNIS.md und ISO-ATEM-1/ERGEBNIS.md nur per grep, nicht ganz gelesen; GUERTEL-Berichte nicht gelesen (I-5 nur gegen ROOT-REVIEW-2003 geprueft).
- DREIPOL-2: welche drei Stoerungsklassen gemeint sind (B3), nur aus ERGEBNIS Z. 88-94 erschlossen.
