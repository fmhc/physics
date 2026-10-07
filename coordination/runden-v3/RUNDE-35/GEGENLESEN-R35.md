Urteil: Mathematik richtig, Deutung mit Auflagen: 27 Befunde (2 hoch, 9 mittel, 16 niedrig), abgeschlossen 22:36:38 CEST

# GEGENLESEN-R35: frischer Gegenleser der Schreibtischnotizen R34/R35

- Gegenleser: Anthropic Opus, frischer Agent ohne Vorkontext
- Beginn (per date): 2026-10-03 22:09:09 CEST
- Auftrag: Brief der Leitung im Agentenauftrag (keine BRIEF-Datei genannt)
- Arbeitsweise: nur lesen; Rechnungen im Kopf, Rechenweg im Text; keine Laeufe auf der .69

## 1. Gelesene Dateien

- RUNDE-34/tetra-konzept/STRINGS-PEITSCHE.md (ganz, 68 Zeilen)
- RUNDE-35/SCHREIBTISCH-QBALL-EIS-LAPSE.md (ganz, 63 Zeilen)
- RUNDE-35/tensor-eis-0/KARTE.md (ganz; geprueft wurde der Abschnitt "Schreibtisch", Z. 15-39)
- RUNDE-35.md: nur Z. 97-122 (TENSOR-EIS-1 vorbereitet), 124-169 (Ernte PEITSCHE-1), 171-225 (Ernte NETZ-C-1),
  236-269 (Ernte TENSOR-EIS-0), 271-288 (AEQ-0)
- ERGEBNIS.md von peitsche-1, netz-c-1, tensor-eis-0 (ganz)
- Fuer die im Auftrag genannten Formeln und Zitate zusaetzlich nur die Schreibtischteile der Karten: peitsche-1/KARTE.md
  Z. 14-60, netz-c-1/KARTE.md Z. 18-48 und 88-102, string-1/KARTE.md Z. 1-40 (keine Ergebnisse von string-1)
- Quelle Yan u. a. (PDF der Leitung): Textauszug S. 1-4 und Seite 3 als Bild (Fig. 2, Gl. 17)
- Nicht geoeffnet: alle Sperrdateien des Auftrags, kein Pruefer-Parallelordner, keine Datendateien

## 2. Befundtabelle

Zaehlung: 2 hoch, 9 mittel, 16 niedrig (Stand dieser Tabelle; Erlaeuterungen in Abschnitt 3). Vorschlaege sind
Anforderungen, keine Ersatztexte.

### 2a. hoch und mittel

| Nr | Datei:Zeile | Art | Schwere | Wortlaut (kurz) | Begruendung | Anforderung |
|---|---|---|---|---|---|---|
| B1 | RUNDE-35.md:212-213 | Ueberzeichnung | hoch | "Ein Stabnetz hat nie eine einzige 'Lichtgeschwindigkeit'. ... in jeder Richtung um >= 27 %, mit Doppelbrechung und Richtungsabhaengigkeit." | Gerechnet: vier Netze, eine Winkelfederstaerke k_theta = 0,1. Gegenbeispiel aus der eigenen Tabelle A1: fcc mit W1-Federn wird bei k_theta = 1/18 elastisch isotrop (Rechnung 3.1), dann gibt es in fuehrender Ordnung weder Doppelbrechung noch Richtungsabhaengigkeit. Die 27 % widersprechen auch der allgemeinen Schranke der eigenen Karte (isotrop nur > 2/sqrt 3, also > 15,5 %). Ergebnis -> Leitung: der Agentenhinweis "Querwellen koennen fast isotrop werden" (fcc-W2 4,2 % / 2,7 %) fehlt. Haltbar ist nur: nie eine Geschwindigkeit fuer alle drei Polarisationen (Satz, Abschnitt 4). | "nie" auf "nicht alle drei Polarisationen gleich schnell" begrenzen; 27 %, Doppelbrechung und Richtungsabhaengigkeit als Befund der vier Netze bei k_theta = 0,1 kennzeichnen; das isotrope fcc-Gegenbeispiel nennen oder nachrechnen lassen. |
| B2 | RUNDE-35.md:273-274 | Physik zu stark / Widerspruch | hoch | "Eine Erhaltungsregel mit Feldenergie (Pfeil- oder Tensor-Eis) ist Austausch mit Spin 1 oder Spin 2 in der 'elektrischen' Form: Gleiche Quellen stossen sich ab." | Lorentzkovarianter Spin-2-Austausch zwischen positiven Energien zieht an; so steht es auch in SCHREIBTISCH:16 ("geraden Spin (0 oder 2)") und in AEQ-0 selbst (Z. 287). Das Tensor-Eis ist eine raeumliche Rang-2-Eichtheorie mit positiv definiter Feldenergie, also maxwellartig im Vorzeichen, kein Graviton-Austausch an T_00. "Immer ab" hat Gegenfaelle (Abschnitt 3.2): ART (Erhaltungssatz und Zwangsbedingung, trotzdem Anziehung), Gummituch mit vorgegebenen Lasten, strukturierter Steifigkeitskern, Torus. | Satz auf "Gauss-Gesetz-Ensemble mit positiv definiter, ortsfester Feldenergie" eingrenzen; "Spin 2" dort streichen oder ausdruecklich vom Spin-2-Austausch an T_mu_nu trennen; den Widerspruch zu SCHREIBTISCH:16 aufloesen. |
| B3 | RUNDE-35.md:214-216 | Schluss traegt nicht | mittel | "Netzwellen scheiden als Licht in Finns Bild also aus." | Die Begruendung ist die netzspezifische Anisotropie aus B1. Robust sind nur: (a) eine zusaetzliche Laengswelle, isotrop c_l/c_q > 2/sqrt 3; (b) Isotropie nur mit Feinabstimmung; (c) Gitterdispersion ab Ordnung (ka)^2. Das ist das alte Problem der elastischen Aethertheorien (Cauchy, Green, MacCullagh, Kelvin) [L, Gedaechtnis des Gegenlesers]. | Den Ausschluss auf (a) bis (c) stuetzen und als [H] mit Bedingungen formulieren. |
| B4 | STRINGS-PEITSCHE.md:34-36 | Uebertragung falsch | mittel | "V(r) = sigma r + c - pi (d - 2)/(24 r) ... Das Zittern selbst erzeugt also wieder einen kleinen 1/r-Anteil." | Der Luescher-Term gehoert zu einer schwingenden Weltflaeche (Quanten-String zwischen statischen Quellen, Wilson-Schleife). In Finns klassischem d-dimensionalen Netz mit zwei festen Ladungen ist der String eine Linie; ihr Querzittern gibt den Ornstein-Zernike-Term ((d - 1)/2) ln r, keinen 1/r-Term. So steht es richtig in string-1/KARTE.md:31-32; R34 ist nicht berichtigt. | R34 mit Vermerk berichtigen oder auf STRING-1 verweisen; den Luescher-Term nur fuer den Quanten- bzw. Weltflaechenfall nennen. |
| B5 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:27-28 und 33 | Literatur falsch zugeordnet | mittel | "mit 'Pinch-Linien' statt Pinch-Punkten [L?: Yan/Benton/Jaubert/Shannon, PRL 2020]"; "Geprueft wuerden die Pinch-Linien" | An der Quelle (Fig. 1c, S. 3) ist das Kennzeichen der vierzaehlige Pinch-Punkt (4FPP) in [hk0]. Pinch-Linien gehoeren zu Benton/Jaubert/Yan/Shannon, Nat. Commun. 7, 11572 (2016), arXiv:1510.01007 (Ref. [29] der Quelle; Titel an der arXiv-Schnittstelle gelesen). RUNDE-35.md:109 und die Karte sind richtig, diese Datei nicht. | Berichtigungsvermerk in der Datei (neuer Vermerk statt Ueberschreiben). |
| B6 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:50-51 und 56-57 | fehlender Vorbehalt | mittel | "nur Lichtgeschwindigkeit veraenderlich (Einstein 1911) ... halb so gross"; "Wenn 'Licht' die Netzwelle ist und Massen die Netzgeschwindigkeit absenken, ist das Weg 2 (halbe Ablenkung)." | Halbe Ablenkung nur, wenn die Absenkung gleich der Uhrenverlangsamung ist (c = 1 + Phi). Eine isotrope Absenkung c = 1 + 2 Phi gibt die volle Ablenkung (Schwarzschild in isotropen Koordinaten, Brechzahlbild nach Eddington bzw. Dicke 1957 [L]). Im Netz entscheidet, wie die Ruheenergie der Fehlstellen von der Netzgeschwindigkeit abhaengt (Rechnung 3.3). | Die Bedingung nennen; "Weg 2" als einen von mehreren Faellen fuehren, nicht als Folge. |
| B8 | RUNDE-35.md:265-267 | Ueberzeichnung | mittel | "Ein Tensor-Eis auf Finns Gitter gibt keine Schwerkraft im einfachen Sinn." | Gerechnet wurde auf einem einfach-kubischen Gitter in Gaussscher Naeherung. Das ERGEBNIS nennt unter "Nicht abgedeckt" ausdruecklich Pyrochlor bzw. Finns Tetraeder und nichtgausssche Effekte; die Leitung laesst beides weg (Ergebnis -> Leitung). | "kubisches Gitter, Gausssche Phase" nennen; Finns Gitter als Erwartung [H]. |
| B9 | RUNDE-35.md:217-221 | fehlender Vorbehalt | mittel | "Fehlstellen werden relativistisch ... gamma bleibt begrenzt. Das ist das Gittermodell der Lorentz-Verletzung ..." | Gerechnet: 1D-Sine-Gordon-Kette, eine Antriebskraft F = 0,02. Im Endzustand gleicht die Abstrahlung die Leistung 2 pi F v aus, also haengt gamma_max von F ab (die Abstrahlung steigt mit gamma, also verschiebt ein anderes F das Gleichgewicht); das ist nicht geprueft. Ohne Antrieb bremst die Abstrahlung jeden diskreten Kink langsam ab. Keine 3D-Fehlstelle gerechnet; "das Gittermodell" statt "ein". | Kette, F und h nennen; F-Abhaengigkeit als offen kennzeichnen; h^(-0,56) nicht hochrechnen. |
| B10 | RUNDE-35.md:163 | unklar, fehlender Vorbehalt | mittel | "Drehende Q-Baelle bleiben unter halber Lichtgeschwindigkeit." | Gemessen ist der innere Energiefluss v_E im Ruhesystem (2D, M1, m = 1 bis 8, omega^2 = 0,52 bis 0,99), nicht die Geschwindigkeit des Balls; woertlich gelesen ist der Satz falsch, denn ein Q-Ball laesst sich auf jedes v < 1 boosten. Die strenge Schranke B1 ist 0,816; die Haelfte stuetzt nur die Kernnaeherung (Grenzwert 1/2 fuer omega -> 1) plus Rechenbereich. Das ERGEBNIS sagt es richtig ("Energie fliesst in ihm"). | "innerer Energiefluss im Ruhesystem" und den Bereich nennen. |
| B11 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:25-26; tensor-eis-0/KARTE.md:36 | fehlender Vorbehalt | mittel | Pretko 2017 "deutet deren Wechselwirkung als Gravitationsanalogon"; "Dynamik der Fraktonen ('Mach', Pretko 2017 [L?])" als moegliche Anziehung | An der Quelle (arXiv-Abstract 1702.07613): die Wechselwirkung ist "always attractive", aber "will generically be short-ranged"; ein Newton-Potenzgesetz nur "under certain conditions". Als Zutat fuer Fernanziehung ist das also nicht ohne Weiteres tauglich. | Kurzreichweite und Bedingung ergaenzen; Zitat als [S, nur Abstract] fuehren. |

### 2b. niedrig

| Nr | Datei:Zeile | Art | Schwere | Wortlaut (kurz) | Begruendung | Anforderung |
|---|---|---|---|---|---|---|
| B12 | RUNDE-35.md:160-161 | Messgroessen vermischt | niedrig | "kommen c beliebig nahe (0,9985 gemessen)" | 0,9985 ist die Nullstellen-Schnelle bei R0/10, also die Mustergroesse, die laut eigenem Befund der Wand vorauslaeuft (+0,36 % ueber Duennwand bei R = 8). Passend waere der Energiefluss 0,99983 (d = 2, R0 = 80) bzw. 0,9999998 (d = 3). "beliebig nahe" ist Hochrechnung: 1 - v = 2,75e-3 / 7,0e-4 / 1,7e-4 fuer R0 = 20/40/80, also etwa R0^-2. Gerechnet wurden nur Waende, keine Strings. | Energieflusszahl nennen, Hochrechnung kennzeichnen, "Waende" statt "ausgedehnte Objekte". |
| B13 | RUNDE-35.md:130, 131, 138-139, 142-143 | Bereich verkuerzt | niedrig | "-0,27 % bis -1,03 %"; "in der Wand hoechstens 0,99983"; "In d = 2 bleibt kein Klumpen"; "Maximum von 0,39 bis 0,40" | Spanne nur der drei gewerteten Laeufe (alle fuenf: bis -2,62 %); 0,99983 nur d = 2, R0 = 80 (d = 3: 0,9999998); Nachlauf nur R0 = 20; Ringmaximum 0,39 bis 0,40 nur fuer m >= 3 (m = 1: 0,353, m = 2: 0,384). "Oszillon ... reelles Gegenstueck eines Q-Balls": Oszillonen sind nicht ladungsgeschuetzt, die Frequenz driftet 1,217 -> 1,299. | Laufbereich anhaengen; beim Oszillon "langlebig, nicht stabil" vermerken. |
| B14 | RUNDE-35.md:145-147 | fehlender Vorbehalt | niedrig | "Im fast leeren Kern ist v_E = 2 omega x/(omega^2 + 1 + 2 x^2)" | Naeherung (f ~ r^m, U ~ f^2), genau nur fuer omega -> 1. Bei omega^2 = 0,52 gibt sie 0,414, gemessen 0,365 bis 0,393. Lage des Maximums laut Formel r = m sqrt(2/(1 + omega^2)), also m bis 1,15 m; gemessen m bis 1,45 m. Die B3-Erklaerung (monoton in omega) bleibt richtig. | "naeherungsweise, genau fuer omega -> 1" ergaenzen. |
| B15 | RUNDE-35.md:158 | falsche Begruendung | niedrig | "Kartenzahl 0,814 berichtigt auf 0,8151 (Leitung: Rundung)" | 0,99/1,49 = 0,66443, Wurzel 0,81513; gerundet 0,815. 0,814 ist ein Rechenversehen, keine Rundung. | Als Versehen kennzeichnen. |
| B16 | RUNDE-35.md:188-189 (aus ERGEBNIS uebernommen) | kleiner Rechenfehler | niedrig | "der Kink ist 9 % schmaler" | gamma aus der Steigung ist 9,0 % groesser (3,220/2,953 = 1,090); die Breite ist dann 1/1,090 = 0,917, also 8,3 % schmaler. | "9 % steiler" oder "8 % schmaler". |
| B17 | RUNDE-35.md:116-119 | ueberholte Hypothese, schiefer Vergleich | niedrig | "richtungsabhaengig (wie bei Dipolen)"; "koennten sich in manchen Richtungen anziehen" | Dipol-Dipol geht wie (1 - 3 cos^2)/r^3 und wechselt das Vorzeichen; hier (7/8 + cos^2/8)/r ohne Vorzeichenwechsel. Die Vermutung ist durch Schreibtisch und T1 widerlegt, im Abschnitt aber nicht als ueberholt markiert. | Rueckverweis auf Z. 168 und 251. |
| B18 | RUNDE-35.md:111-112 | unklar | niedrig | "Rang-2-Phase fuer D_A < 0 zwischen etwa 1e-3 und 5e-2 J_A. Darunter ein Uebergang erster Ordnung" | Fig. 2 (als Bild gelesen): die Zahlen sind Temperaturen T/J_A. Die obere Grenze ist ein Crossover (gestrichelt, gesteuert vom Betrag von D_A durch T) und haengt von D_A ab, rund 5e-2 erst bei D_A = -0,15; die untere ist die Linie erster Ordnung zur q = W-Ordnung, rund 1e-3. | "T/J_A" und "Crossover, abhaengig von D_A" ergaenzen. |
| B19 | RUNDE-35.md:252 | fehlende Kennzeichnung | niedrig | "Steigung 0,03989 gegen 1/(8 pi) = 0,03979" | Das ist der endlichkeitskorrigierte Wert; roh bei L = 64: 0,028 -> 0,023 (T3 woertlich nicht eingetroffen). | "(korrigiert)" anfuegen. |
| B20 | RUNDE-35.md:283 | Zahl zu scharf | niedrig | "Gemessen ist eta < ~1e-15 [L: MICROSCOPE ...]" | Endergebnis an der Quelle (arXiv:2209.15487, PRL 129, 121102): eta(Ti, Pt) = (-1,5 +- 2,3 stat +- 1,5 syst)e-15, also rund 2,7e-15 bei 1 sigma. Fuer den Schluss (15 % gegen 1e-15) ohne Folgen. | "Genauigkeit einige 1e-15" mit Quelle. |
| B21 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:13 | zu allgemein | niedrig | "Eine Gauss-Regel ist eine Vektor-Kopplung (Spin 1)." | Rang-2-Gauss-Regeln (TENSOR-EIS-0) und die Hamilton-Zwangsbedingung der ART sind auch Gauss-Regeln. | "Gauss-Regel fuer ein Pfeilfeld mit skalarer Ladung". |
| B22 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:29 | Ueberzeichnung | niedrig | "Das ist genau Finns Tetraedergitter mit Tensor- statt Pfeil-Einheiten." | Bei Yan u. a. sitzen Heisenberg-Spins (Vektoren) mit DM-Kopplung nur auf A-Tetraedern, das Gitter ist atmend (A ungleich B); das Tensorfeld wird aus den Spins gebildet. | "genau" streichen, Unterschiede nennen. |
| B23 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:40 (vgl. RUNDE-35.md:285) | Vorzeichenkonvention | niedrig | "Das Integral der Spur T^mu_mu ist dann -E." | -E gilt fuer Signatur (-,+,+,+), bei (+,-,-,-) +E; AEQ-0 nennt die Quelle "genau E". | Signatur angeben. |
| B24 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:18-19 | unklare Formulierung | niedrig | "schneller als der Ladungsgewinn ~ Q" | Gemeint ist der Bindungsgewinn (m - omega_0) Q gegenueber freien Teilchen. | Wort ersetzen. |
| B25 | SCHREIBTISCH-QBALL-EIS-LAPSE.md:62-63 | Ueberzeichnung | niedrig | "Abweichungen sind nur moeglich, wo die Spin-2-Kette bricht (Glieder 10 und 7)." | "nur" setzt voraus, dass die Kette alle Annahmen enthaelt (etwa auch Masselosigkeit, minimale Kopplung, vgl. B7); das ist nicht gezeigt. | Als [H] bzw. "nach unserer Kette" kennzeichnen. |
| B26 | STRINGS-PEITSCHE.md:52-53 | fehlender Vorbehalt | niedrig | "bei einem relativistischen String ist die 'Peitschenspitze' genau Lichtgeschwindigkeit" | Gilt fuer den unendlich duennen Nambu-Goto-String. Bei Feld-Strings oder Waenden endlicher Dicke wird die Spitze geglaettet, der Energiefluss bleibt unter 1 (PEITSCHE-1: 0,99983 bzw. 0,9999998). | "im Nambu-Goto-Grenzfall" ergaenzen. |
| B27 | tensor-eis-0/KARTE.md:30-31 | unklar | niedrig | "Skalarladung ... d_i d_j E_ij = rho ... G(r) = -r/(8 pi)" | Nicht gesagt, ob E hier spurfrei ist. -r/(8 pi) gilt fuer symmetrisches E mit Spur (6 Freiheitsgrade); spurfrei wird der Kern 3/(2 q^4) (ERGEBNIS: U5/U6 = 1,5). | Annahme nennen. |

## 3. Erlaeuterungen zu den Befunden

### 3.1 Zu B1: fcc mit Winkelfedern wird elastisch isotrop (Rechnung aus Tabelle A1 von NETZ-C-1)

- fcc ist ein Bravais-Gitter (keine innere Relaxation). Die elastischen Konstanten sind deshalb genau linear in den
  Federkonstanten, also linear in k_theta bei k = 1.
- Aus Tabelle A1 (Geschwindigkeiten quadriert, rho c^2 in Einheiten von rho):
  - C44: [100]-Querwelle 0,7071^2 = 0,5 (Z) und 1,0488^2 = 1,1 (W1). Steigung 6 je Einheit k_theta.
  - (C11 - C12)/2: [110]-Querwelle mit Polarisation [1-10], 0,5^2 = 0,25 (Z) und 1,1402^2 = 1,3 (W1). Steigung 10,5.
  - C11: [100]-Laengswelle, 1,0^2 = 1,0 (Z) und 1,5492^2 = 2,4 (W1). Steigung 14.
  - C12 aus der [110]-Laengswelle W1: (C11 + C12 + 2 C44)/2 = 1,4832^2 = 2,2, also C12 = 4,4 - 2,4 - 2,2 = -0,2.
  - Unabhaengige Probe mit [111], W1: (C11 + 2 C12 + 4 C44)/3 = (2,4 - 0,4 + 4,4)/3 = 2,133 = 1,4606^2 und
    (C11 - C12 + C44)/3 = 3,7/3 = 1,233 = 1,1106^2. Beides passt zur Tabelle.
- Zener-Verhaeltnis A = C44/((C11 - C12)/2) = (0,5 + 6 k_theta)/(0,25 + 10,5 k_theta): A = 2 bei k_theta = 0,
  A = 1,1/1,3 = 0,846 bei k_theta = 0,1.
  - A = 1 bei 0,5 + 6 k = 0,25 + 10,5 k, also k_theta = 0,25/4,5 = 1/18 = 0,056.
- Dort gilt: C44 = 0,833, C11 = 1 + 14/18 = 1,778, C12 = 0,111.
  - Born-Stabilitaet erfuellt: C11 > Betrag C12; C11 + 2 C12 = 2,0 > 0; C44 > 0.
  - Das Medium ist elastisch isotrop: c_quer = sqrt 0,833 = 0,913 in allen Richtungen und fuer beide Polarisationen
    (keine Doppelbrechung), c_laengs = sqrt 1,778 = 1,333 in allen Richtungen.
  - c_l/c_q = 1,46. Die Mindestspanne 1,27 wird hier nicht unterschritten, aber "Doppelbrechung und
    Richtungsabhaengigkeit" verschwinden in fuehrender Ordnung. Uebrig bleibt Anisotropie erst ab Ordnung (ka)^2.
- Die 27 % sind ausserdem keine allgemeine Schranke: Die eigene Karte (netz-c-1/KARTE.md:27) nennt fuer isotrope
  stabile Medien nur c_l/c_q > 2/sqrt 3 = 1,155; ein Netz nahe Kompressionsmodul 0 kaeme dem nahe.
- Nebenbei unklar in RUNDE-35.md:176-177: "fcc" meint dort fcc-Z, "Pyrochlor" und "Diamant" aber die W1-Fassungen.

### 3.2 Zu B2: Probe der Aussage "Gleiche Quellen stossen sich in einer Erhaltungsregel-Theorie immer ab"

- **Warum sie im Eis-Fall stimmt:** F = (1/2) E.M.E mit linearer Nebenbedingung B E = rho und positiv definitem M.
  Das Minimum ist F(rho) = (1/2) rho.(B M^-1 B^T)^-1.rho, also positiv definit in rho. Bei ortsfester, isotroper
  Steifigkeit ist der Ortsraumkern positiv und faellt mit r (1/(4 pi r), Vektor (7/8 delta + 1/8 r r)/(4 pi r)).
  Dann stossen sich gleiche Quellen ab. Das ist ein Satz, aber nur unter diesen Bedingungen.
- **Gegenfaelle:**
  1. ART: Die Quelle ist erhalten (d_mu T^mu nu = 0) und die Hamilton-Zwangsbedingung ist eine Gauss-artige
     Gleichung fuer die Energiedichte. Trotzdem ziehen sich gleiche Massen an, weil die Feldenergie nicht positiv
     definit ist (konformer Modus mit negativem Vorzeichen) [L]. Genau das ist die gesuchte Zutat.
  2. Elastizitaet mit vorgegebenen Lasten (Gummituch): Gesamtpotential Pi = U_el - W = -(1/2) f.u. Der
     Wechselwirkungsterm ist -f1.G(r).f2 < 0 fuer gleiche Lasten; gleiche Lasten ziehen sich an. Das Vorzeichen haengt
     also daran, ob die Quellen Zwangsbedingungen sind (Eis) oder Arbeit leisten (Lasten). Fuer Finns Satz
     "Kraefte in den Staeben" ist diese Unterscheidung wesentlich.
  3. Positiv definiter, aber q-abhaengiger Kern (Steifigkeit mit Struktur, etwa ein Maximum bei endlichem q): G(q) > 0
     fuer alle q erzwingt nicht G(r) > 0 fuer alle r; der Kern kann im Ortsraum das Vorzeichen wechseln.
  4. Endlicher Torus: TENSOR-EIS-0, L = 32, 44 von 189 Abstaenden mit Scheinanziehung.
- **Zum Wort "Spin 2":** Bei Lorentz-kovariantem Austausch ziehen gerade Spins gleiche Quellen an
  [L: Feynman, Lectures on Gravitation; Zee, QFT in a Nutshell]. Das Tensor-Eis ist eine raeumliche Rang-2-Theorie mit
  positiv definiter "elektrischer" Energie, also im Vorzeichen maxwellartig. Es als "Austausch mit Spin 2" zu fuehren,
  verwischt genau den Unterschied, auf den AEQ-0 hinaus will.

### 3.3 Zu B6: Halbe oder volle Ablenkung in einem Netz mit veraenderlicher Wellengeschwindigkeit

- Licht als Netzwelle mit c(x) = 1 + dc(x); Brechzahl n = 1 - dc. Die ART gibt n = 1 - 2 Phi (volle Ablenkung),
  Einstein 1911 n = 1 - Phi (halbe Ablenkung).
- Massive Fehlstelle mit Ruheenergie E0(x) und H = sqrt(p^2 c^2 + E0^2). Langsam: H = E0 + p^2 c^2/(2 E0), also
  Beschleunigung a = -c^2 grad ln E0 = -grad Phi.
- Mit E0 ~ c^alpha folgt Phi = alpha dc, also n = 1 - Phi/alpha. Ablenkung relativ zur ART: 1/(2 alpha).
  - alpha = 1 (E0 proportional zu c): halbe Ablenkung. Beispiel: Sine-Gordon-Kink, E0 = 8 sqrt(kappa V0), wenn die
    Netzgeschwindigkeit ueber die Federsteifigkeit kappa absinkt.
  - alpha = 1/2: volle Ablenkung.
  - alpha = 2 (E0 = m c^2 mit festem m): ein Viertel.
  - alpha = 0 (c sinkt ueber die Massendichte, E0 bleibt): Licht wird abgelenkt, Fehlstellen fallen nicht.
- Folgerung fuer die Anforderung: "Weg 2" stimmt fuer den einfachsten Fall (Steifigkeit, Kink), ist aber keine
  allgemeine Folge von "Massen senken die Netzgeschwindigkeit". Die Aussage zu gamma_PPN = 1 in Z. 58-59 ist richtig.
- Rechnung des Gegenlesers [M], einfache Teilchennaeherung; kein Projektergebnis.

### 3.4 Zu B4: Luescher-Term oder Ornstein-Zernike-Logarithmus

- Der Luescher-Term -pi (d - 2)/(24 r) entsteht aus den Querschwingungen einer zweidimensionalen Weltflaeche (String
  der Laenge r, lange Zeit T), also fuer das Potential zwischen statischen Quellen in einer Quantentheorie oder fuer
  Wilson-Schleifen [L].
- In Finns klassischem Netz (STRING-1: d-dimensionales Gitter ohne Zeitrichtung, zwei feste Ladungen) ist der String
  eine Linie. Die Summe ueber ihre Querauslenkungen gibt e^(-r/xi) r^(-(d-1)/2), also F/T = r/xi + ((d - 1)/2) ln r.
  Der Zusatz waechst logarithmisch und ist kein 1/r-Anteil.
- string-1/KARTE.md:31-32 hat das richtig. R34 bleibt ohne Vermerk falsch, und eine Leserin von R34 erwartet in
  STRING-1 den falschen Zusatz.

### 3.5 Zu B7: Probe der Aussage "nur Spin 2 gibt volle Lichtablenkung mit Aequivalenzprinzip"

- Unter den ueblichen Annahmen stimmt sie in erster Ordnung: lorentzinvariante Feldtheorie ohne Vorzugssystem,
  ein masseloser Vermittler, universelle Kopplung. Dann gilt: Skalar an der Spur keine Ablenkung, Spin 1 Abstossung,
  Spin 2 an T_mu_nu volle Ablenkung [L].
- Gegenfaelle, wenn eine Annahme faellt [L, Gedaechtnis des Gegenlesers]:
     gamma = 1 erreichen; sie scheitern an den Vorzugssystem-Parametern, nicht an der Ablenkung.
  2. Massiver Spin 2 (Fierz-Pauli): bei gleichem Newton-Potential nur 3/4 der Ablenkung (van Dam-Veltman-Zakharov).
     "Spin 2" allein reicht also nicht, er muss masselos sein (oder abgeschirmt).
  3. Spin 2 plus schwach gekoppelter Skalar (Brans-Dicke): gamma = (1 + omega)/(2 + omega), mit grossem omega
     innerhalb der Cassini-Grenze. "nur" schliesst Beimischungen nicht aus.
- "aus unseren eigenen Bausteinen nachvollzogen": Gezeigt ist, dass Skalar (AEQ-Haken 1 und 2) und Pfeil-
  bzw. Tensor-Eis (Abstossung) scheitern. Dass Spin 2 an T_mu_nu die einzige Loesung ist, ist [L] (Weinberg, Deser,
  Feynman), nicht nachgerechnet.

### 3.6 Zu B9 und B10: kurze Begruendungen

- B9: Ohne Reibung ist der Endzustand ein Gleichgewicht aus zugefuehrter Leistung 2 pi F v (v nahe 1) und
  Gitterabstrahlung, die mit kleinerer verkuerzter Breite steil waechst. Steigt die Abstrahlung mit gamma, liegt das
  Gleichgewicht bei staerkerem F bei groesserem gamma, bei schwaecherem F tiefer; ohne Antrieb bremst ein diskreter
  Kink langsam ab. gamma_max = 1,78 / 2,61 / 3,86 gilt also nur fuer F = 0,02; die Abhaengigkeit von F ist nicht
  gerechnet. Fuer eine Hochrechnung auf Planck-Gitter (Glied 10) fehlt damit die zweite Groesse. (Berichtigung im
  eigenen Text: eine erste Fassung dieser Zeile hatte die Richtung der F-Abhaengigkeit verkehrt.)
- B10: Das Modell ist lorentzinvariant; ein geboosteter drehender Q-Ball hat im Laborsystem einen Energiefluss, der
  mit der Fluggeschwindigkeit gegen 1 geht. Die Aussage "unter halber Lichtgeschwindigkeit" betrifft nur den inneren Energiefluss im
  Ruhesystem.

## 4. Ausdruecklich geprueft und fuer richtig befunden

Alle Rechnungen im Kopf; Rechenweg jeweils kurz.

### 4a. Strings, Peitsche, drehende Q-Baelle

- **Kraftgesetz nach Netzdimension** (STRINGS-PEITSCHE.md:13-17): Gauss im d-dimensionalen Netz, Fluss durch eine
  Kugelschale ~ r^(d-1), also Feld ~ r^(1-d). Potential d = 1: ~ r; d = 2: ~ ln r; d = 3: ~ 1/r. Kraft konstant,
  ~ 1/r, ~ 1/r^2. Richtig. Der Zaehlfall (Z. 20-22) stimmt auch: In der Eis-Kette ist der Fluss bei gegebenen Ladungen
  eindeutig, die Entropie haengt nicht von r ab.
- **String-Bruch** (Z. 31-32): sigma r_c = 2 mu, also r_c = 2 mu/sigma; mit der Konstanten c genauer (2 mu - c)/sigma.
  Das "~" deckt das.
- **Luescher-Term als Formel** (Z. 35): -pi (d - 2)/(24 r), d Raumzeit-Dimensionen, d = 4 gibt pi/12. Formel und Zitat
  richtig; nur die Uebertragung ist falsch (B4).
- **STRING-1-Schreibtisch** (string-1/KARTE.md:19-35):
  - Poisson-Summe: Sum_m exp(-(K_V/2)(x - 2 pi m)^2) ist proportional zu Sum_n exp(-n^2/(2 K_V) + i n x). Das
    Theta-Integral erzwingt div n = 0, eine Einfuegung exp(i(theta_A - theta_B)) erzwingt die Ladungen. Flussenergie
    n^2/(2 K_V) = (K/2) n^2, also K_V = 1/K. Richtig.
  - Spinwellen: eta = 1/(2 pi K_V) = K/(2 pi). 3D geordnet: <cos> ~ exp(G(r)/K_V) mit G = 1/(4 pi r), also
    F/T = c - 1/(4 pi K_V,R r), und wegen K_V,R <= K_V gilt C >= K/(4 pi). Richtig.
  - Uebergaenge: 1/0,75 = 1,33 und 1/0,333 = 3,0. Die Villain-Werte passen zu meinem Gedaechtnis
    (2D-BKT bei etwa 0,752, 3D bei etwa 0,3331) [L, Gegenleser].
  - Ornstein-Zernike: e^(-r/xi) r^(-(d-1)/2), also (d - 1)/2 ln r; d = 2: 1/2, d = 3: 1. Richtig.
  - Paarfugazitaet: 1 + 2 e^(-mu/T) cos theta = exp(2 e^(-mu/T) cos theta) in erster Ordnung, also h = 2 e^(-mu/T).
    Richtig.
- **Duennwand-Kollaps** (peitsche-1/KARTE.md:16-22):
  - V = (phi^2 - 1)^2/4: sigma = Integral sqrt(2V) dphi = (1/sqrt 2)(2 - 2/3) = 2 sqrt 2/3 = 0,9428; m^2 = V''(1) = 2.
  - Energie d = 2: 2 pi sigma R gamma = 2 pi sigma R0, also gamma = R0/R, v = sqrt(1 - (R/R0)^2). d = 3:
    gamma = (R0/R)^2, v = sqrt(1 - (R/R0)^4). Werte d = 2: sqrt 0,75 = 0,8660, sqrt(15/16) = 0,9682,
    sqrt 0,99 = 0,9950. d = 3: 0,9682, sqrt(255/256) = 0,9980, sqrt(1 - 1e-4) = 0,99995. Alle wie in Tabelle 3.1.
  - t_c d = 2: R0 arcsin 1 = (pi/2) R0, bei R0 = 80 also 125,664. d = 3: Integral dx/sqrt(1 - x^4) von 0 bis 1 =
    (1/4) B(1/4, 1/2) = Gamma(1/4)^2/(4 sqrt(2 pi)) = 13,1450/10,0265 = 1,31103 (Gamma(1/4) = 3,62561). Mal 40: 52,441; mal 20: 26,221.
  - Anfangsenergie 2 pi 0,9428 80 = 473,9, wie im ERGEBNIS.
  - Musterschwelle: Ueberschuss c/R^2 gegen 1 - v_duenn = R^2/(2 R0^2), gleich bei R^4 = 2 c R0^2, also
    R = (2c)^(1/4) sqrt R0; c = 0,2 gibt 0,80. 0,8 sqrt 80 = 7,2; 0,8 sqrt 40 = 5,1; 0,8 sqrt 20 = 3,6. Richtig.
- **Schranke B1:** v_E = 2 omega x f^2/(omega^2 f^2 + f'^2 + x^2 f^2 + U) mit x = m/r. Mit f'^2 >= 0 und
  U >= omega_min^2 f^2 folgt v_E <= 2 omega x/(omega^2 + omega_min^2 + x^2); Maximum bei x^2 = omega^2 + omega_min^2,
  Wert omega/sqrt(omega^2 + omega_min^2). M1: U/S = 1 - S + S^2/2 = 1/2 + (1 - S)^2/2 >= 1/2. Bei omega^2 = 0,99:
  sqrt(0,99/1,49) = sqrt 0,66443 = 0,8151. 0,4981/0,8151 = 0,611, also 61 %. Richtig.
- **Kernformel** (RUNDE-35.md:145-147): f ~ r^m gibt f' = x f; U = f^2. Nenner f^2(omega^2 + 1 + 2 x^2). Maximum von
  x/(a + 2 x^2) bei x^2 = a/2, Wert 2 omega sqrt(a/2)/(2a) = omega/sqrt(2a) = omega/sqrt(2(1 + omega^2)).
  omega^2 = 0,99: 0,99499/1,99499 = 0,4987. Richtig (Vorbehalt B14). Steigt mit omega, weil omega^2/(1 + omega^2)
  steigt; Grenzwert 1/2.
- **Ringschaetzung:** f' = 0, U/f^2 = omega^2 - x^2: Nenner 2 omega^2 f^2, also v_E = m/(r omega). Richtig als
  grobe Schaetzung; Abweichung laut ERGEBNIS hoechstens 2,5 %.
- **Zahlenabgleich PEITSCHE-1 Leitung gegen ERGEBNIS:** 0,8660/0,9685/0,9985 gegen 0,8660/0,9682/0,9950; Schwellen
  7,3/5,2/3,7 und 12,1/7,7; 1,025 und 0,9994 bei R = 2; 1,1e-5; 1 % und 1,30; 0,365 bis 0,498; 61 %; 2,5 %;
  Energiefehler 9,4e-9 (bis t_c); 7e-16; Selbstanzeigen. Alles richtig uebernommen (Ausnahmen B12 bis B16).

### 4b. Stabnetze, Tensor-Eis, LAPSE und AEQ

- **fcc-Elastizitaet** (netz-c-1/KARTE.md:18-25): Zentralfedern, Gitterkonstante a: C11 = 2k/a, C12 = C44 = k/a.
  In c0 = sqrt(C44/rho): [100] sqrt 2 / 1 / 1; [110] sqrt(5/2) = 1,581, 1, sqrt(1/2) = 0,707; [111] sqrt(8/3) = 1,633,
  sqrt(2/3) = 0,816. Mit Kante 1 (a = sqrt 2, rho = 4/a^3) sind das 1,0 / 0,7071 / 1,118 / 0,5 / 1,1547 / 0,5774 wie in
  Tabelle A1. Richtig.
- **c_l/c_q >= 2/sqrt 3** (KARTE:27): isotrop c_l^2/c_q^2 = (lambda + 2 mu)/mu; K = lambda + 2 mu/3 > 0 gibt
  lambda > -2 mu/3, also Verhaeltnis^2 > 4/3. Richtig (streng >).
- **Satz hinter "nie eine einzige Geschwindigkeit"** (gilt allgemein, auch anisotrop): Waere C_ijkl n_j n_l = A delta_ik
  fuer alle n, dann ist der in (j, l) symmetrische Teil A delta_ik delta_jl. Verjuengen i = k, j = l gibt C_ijij = 9A;
  verjuengen j = i, l = k gibt (C_iikk + C_ijij)/2 = 3A, also C_iikk = -3A. Fuer reine Dehnung ist die Energie
  (1/2) C_iikk eps^2 < 0: negativer Kompressionsmodul. Ein stabiles Netz hat also nie eine Geschwindigkeit fuer alle drei
  Polarisationen. Das ist der haltbare Kern von B1.
- **Diamant-Z 0,4714:** Bindung 1, a = 4/sqrt 3, Volumen je Atom a^3/8 = 1,5396, rho = 0,6495. Dehnung eps: zwei
  Bindungen je Atom, Energiedichte eps^2/1,5396 = 0,6495 eps^2 = (9/2) K eps^2, also K = 0,14434. c = sqrt(K/rho) =
  sqrt(2/9) = 0,4714. Richtig.
- **Keating-Probe** (ERGEBNIS NETZ-C-1): alpha = 1/3, beta = 0,1333, a = 2,3094: (alpha + 3 beta)/a = 0,7333/2,3094 =
  0,3175; 4 alpha beta/(a (alpha + beta)) = 0,17778/1,0777 = 0,1650. Mit rho = 0,6495 und den Tabellenwerten
  (0,6992^2 und 0,5040^2) gleich. Die Formelschreibweise weicht vom ueblichen /(4a) ab, ist aber in sich stimmig.
- **Maxwell-Zaehlung:** fcc 3 - 6 = -3, Pyrochlor 12 - 12 = 0, Diamant 6 - 4 = 2, srs 12 - 6 = 6. Richtig.
- **Kink-Kette:** Leistungsbilanz 2 pi F v = 8 gamma eta v^2 gibt gamma v = pi F/(4 eta); q = pi 0,00382/0,04 = 0,300;
  v_soll = 10/sqrt 101 = 0,99504. Ohne Reibung p = 8 gamma v = 2 pi F t, also gamma = sqrt(1 + (pi F t/4)^2); F = 0,02,
  t = 828: pi 0,02 828/4 = 13,0. Abgestrahlte Leistung 2 pi 0,02 0,7775 = 0,0977. Gruppengeschwindigkeit
  sin(kh)/(h omega) < 1, weil sin(kh) <= 2 sin(kh/2) und omega > (2/h) sin(kh/2). Faktor je Halbierung
  2,614/1,781 = 1,468 und 3,861/2,614 = 1,477; log2 1,47 = 0,556. Alles richtig.
- **Zahlenabgleich NETZ-C-1:** 403 Richtungen, 1,41/1,32/1,27/1,49, [110]-Doppelbrechung, 1365 Nullpunkte, srs-Nullast,
  5 bis 9 %, 0,4714, 0,1 % und 0,25 %, 0,968 gegen 0,995, 3,22 gegen 2,95, 1,78/2,61/3,86 und 13/26/52, 0,03 %,
  3,5e-8, 0/0/2/6, 2,7e-9/2,3e-8, dt^4, dt = 0,0125, Selbstanzeigen. Richtig uebernommen (Ausnahme B16). Herrmann u. a.
  2009 mit Delta c/c ~ 1e-17 passt [L, Gegenleser].
- **Tensor-Kern** (tensor-eis-0/KARTE.md:21-29), mit s = q.rho, Q = q^2, R = rho^2, M = -(q rho^T + rho q^T)
  + (s/2Q) q q^T + (s/2) Eins:
  - Spur: -2s + s/2 + 3s/2 = 0. Gauss: q.M = -Q rho - s q + s q/2 + s q/2 = -Q rho, also i q.E = rho. Orthogonal zu
    jedem symmetrischen T mit T q = 0 und Spur 0. Richtig.
  - Spur(M^2) = 2s^2 + 2QR + s^2/4 + 3s^2/4 - 2s^2 - 2s^2 + s^2/2 = 2QR - s^2/2; |E|^2 = (2/q^2)(rho^2 - (q_dach.rho)^2/4).
  - Fourier: FT[1/q^4] = -r/(8 pi), FT[q_i q_j/q^4] = d_i d_j r/(8 pi) = (delta - r r)/(8 pi r).
    G = delta/(4 pi r) - (delta - r r)/(32 pi r) = (7/8 delta + 1/8 r r)/(4 pi r). Richtig.
  - U = 2K p.G.p > 0, da G positiv definit (Eigenwerte 7/8 und 1); Verhaeltnis 1/(7/8) = 8/7 = 1,1429; antiparallel
    -U. Richtig.
  - Skalar (6 Freiheitsgrade): |E|^2 = rho^2/q^4, U = K rho1 rho2 (-r/(8 pi)); ungleich Steigung 1/(8 pi) = 0,03979.
  - Torus: Winkelmittel von 1 - q_z^2/4 ist 11/12; -(2/(4 pi))(11/12) 2,8373 = -0,41394; durch 64: -0,00647.
    r^2-Term: Laplace(a r^2) = 6a = xi/(4 pi L), also a = xi/(24 pi L). Alles richtig.
- **Quelle Yan u. a., Gl. 17** (Bild S. 3): transversaler, spurfreier Projektor, Spur 2. Passt zur Aussage des Agenten.
- **LAPSE und AEQ:**
  - von Laue: Integral T_ij = 0 fuer ruhende abgeschlossene Koerper; Spur bei (-,+,+,+) gleich -E (B23).
  - Aequivalenzprinzip: E = N E0, Kraft -E0 grad N, Traegheit E0, Beschleunigung -grad N. Richtig und, wie vermerkt,
    vorab ableitbar.
  - Skalar: -K Laplace chi = s, F_min = -(1/2) s G s < 0. Richtig.
  - Integral |phi|^2 = Q/(2 omega) (Q = 2 omega Integral f^2). 200/1,4898 = 134,25; /157,295 = 0,8535 (mit den
    gerundeten Eingaben; 0,854 liegt in der Rundung von omega). Grenzwert 1/(2 omega_min^2) = 1 bei omega_min^2 = 1/2.
    Spanne 0,854 bis 1,0, also etwa 15 %. Richtig.
  - Coulomb-Selbstenergie ~ Q^2/R mit R ~ Q^(1/3): ~ Q^(5/3). Richtig.
  - Tabellenzeilen Nordstroem (keine Ablenkung) und Einstein 1911 (halbe, 0,83 Bogensekunden) passen zum Gedaechtnis
    [L]; Cassini (2,1 +- 2,3)e-5 passt (Bertotti/Iess/Tortora 2003) [L, Gegenleser].

## 5. Literaturpruefung an der Quelle

### 5a. An der Quelle gelesen [S] (je Zitat, was gelesen wurde)

| Zitat | Gelesen | Ergebnis |
|---|---|---|
| Yan/Benton/Jaubert/Shannon, PRL 124, 127203 (2020), arXiv:1902.10934 | PDF der Leitung: Text S. 1-4 (pdftotext), S. 3 als Bild | Gl. 6, 14, 18 (J_A = J_B = 1, D_A = -0,01, D_B = 0), Fig. 1c 4FPP in [hk0], 1b zweizaehlig in [0kl], Fig. 1d Monte Carlo bei T = 2,5e-3 J_A, Gl. 17, Fig. 2 (T/J_A gegen D_A/J_A) wie in RUNDE-35.md:99-112 bzw. KARTE angegeben (Unschaerfe B18). Keine Pinch-Linien als Kennzeichen (B5). Ref. [29] = Benton u. a., Nat. Commun. 7, 11572 (2016); Ref. [30] = Pretko, PRD 96, 024051 (2017). |
| Benton/Jaubert/Yan/Shannon, "A spin liquid with pinch-line singularities on the pyrochlore lattice" | arXiv-Schnittstelle (Titelsuche "pinch-line"): arXiv:1510.01007, Nat. Commun. 7, 11572 (2016) | Das ist die Pinch-Linien-Arbeit (B5). |
| Pretko, "Emergent gravity of fractons: Mach's principle revisited", PRD 96, 024051 (2017) | arXiv:1702.07613, Abstract | Jahr, Titel und Deutung als Gravitationsanalogon richtig; "always attractive", aber "generically short-ranged"; Newton-Potenzgesetz nur "under certain conditions" (B11). |
| Sadoune/Liu/Yan/Jaubert/Shannon/Pollet, PRR 7, 033061 (2025) | arXiv:2402.10658, Abstract | "smectic liquid crystal", "thermal order-by-disorder": die Zusammenfassung in RUNDE-35.md:113-114 ist richtig. |
| MICROSCOPE, Touboul u. a., PRL 129, 121102 (2022) | arXiv:2209.15487, Abstract | eta(Ti, Pt) = (-1,5 +- 2,3 stat +- 1,5 syst)e-15 (B20). |
| Pace/Morampudi/Moessner/Laumann, PRL 127, 117205 (2021) (Quelle fuer "~0,08") | arXiv:2009.04499, Titel und Abstract | Abstract: Eis-Feinstrukturkonstante "more than an order of magnitude greater" als 1/137, also ueber etwa 0,07; die Zahl 0,08 steht nicht im Abstract. Die Kennzeichnung [L?] in SCHREIBTISCH:22 ist angemessen. |
| Goriely/McMillen 2002 | arXiv-Titelsuche "cracking whip" ohne Treffer | Nicht an der Quelle geprueft. |

### 5b. Aus dem Gedaechtnis des Gegenlesers beurteilt [L, nicht an der Quelle]

- Plausibel und nach meinem Gedaechtnis richtig zugeordnet (Bandangaben ohne Gewaehr):
  - Goriely/McMillen, PRL 88, 244301 (2002), Ueberschall der Spitze. Die Leitung fuehrt es zu Recht als [L?].
  - Turok, Nucl. Phys. B 242, 520 (1984), Cusps generisch; Vilenkin/Shellard (Buch 1994); Damour/Vilenkin,
    PRL 85, 3761 (2000).
  - Luescher/Symanzik/Weisz, Nucl. Phys. B 173, 365 (1980); haeufiger zitiert wird zusaetzlich Luescher, Nucl. Phys.
    B 180, 317 (1981).
  - Bali u. a. (SESAM), "Observation of string breaking in QCD", PRD 71, 114513 (2005). Das [L?] der Leitung kann
    hier entfallen.
  - Frank, Proc. Phys. Soc. A 62, 131 (1949), Lorentz-Verkuerzung von Versetzungen; McLaughlin/Scott, PRA 18, 1652
    (1978).
  - Barcelo/Liberati/Visser, "Analogue Gravity", Living Rev. Relativ. (2005, Neufassung 2011); Keating, Phys. Rev.
    145, 637 (1966).
  - Lee/Stein-Schabes/Watkins/Widrow, "Gauged Q balls", PRD 39, 1665 (1989); Hermele/Fisher/Balents, PRB 69, 064404
    (2004).
  - Friedberg/Lee/Pang, PRD 35, 3640 und 3658 (1987); Bertotti/Iess/Tortora, Nature 425, 374 (2003).
  - Villain: 2D-BKT bei etwa 0,752, 3D bei etwa 0,3331; Gleiser, PRD 49, 2978 (1994); Gleiser/Sornborger, PRE 62,
    1368 (2000).
- Ergaenzungen, die die Leitung pruefen sollte, bevor sie sie nutzt:
  - Fuer "Doppelbrechung" ist die schaerfste Grenze astrophysikalisch (Polarimetrie, Kostelecky/Mewes, um 1e-32 fuer
    die doppelbrechenden Koeffizienten), viel schaerfer als 1e-17.
  - Elastische Aethertheorien (Cauchy, Green, MacCullagh, Kelvin) zu B3.
  - vDVZ zu B7.

## 6. Ende

- Ende (per date, vor dem letzten Eintrag gemessen): 2026-10-03 22:36:38 CEST. Dauer 27 min 29 s
  (22:09:09 bis 22:36:38), Zeitbox 60 min eingehalten.
- Keine Laeufe auf der .69, keine lokalen Interpreter, keine Rechnung auf dem Rechner. Werkzeuge: Lesen, grep, sed -n,
  pdftotext nach stdout, date, wc, ls, cut; sieben WebFetch-Abrufe an genau benannten Quellen (Pretko-Abstract
  zweimal; Abschnitt 5a).
- Geschrieben nur diese Datei.
- Urteil: Die Schreibtischmathematik traegt (alle im Auftrag genannten Formeln nachgerechnet und richtig). Die
  Zahlen der drei ERGEBNIS-Dateien sind bis auf Kleinigkeiten richtig uebernommen. Zu stark sind vor allem die
  Bedeutungsabsaetze und die absoluten Saetze (B1, B2, B3, B7) sowie eine Literaturzuordnung (B5).
