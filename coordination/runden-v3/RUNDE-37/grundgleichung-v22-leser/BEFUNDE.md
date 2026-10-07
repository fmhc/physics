Urteil: weitergabefaehig nach den A-Befunden. 3 A-, 7 B-, 11 C-Befunde. Neue Rechnungen in 2.3, 3.1, 4 und 5 halten von Hand; zu stark bzw. nicht gedeckt sind der Torus-Schluss fuer "K = 0 als Gesetz", "Lesart R bevorzugt" und "beiden gerechneten Eckenregeln" im "Einfach gesagt".

# Leser der letzten Schicht: GRUNDGLEICHUNG-SKIZZE Fassung 2.2

- Gelesenes Dokument: coordination/runden-v3/RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.2.md
- Abgleich: RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.1.md, RUNDE-37/grundgleichung-v21-leser/BEFUNDE.md
- Start: 2026-10-05 12:15:43 (gemessen mit date)
- Ende: 2026-10-05 12:37:06 (gemessen mit date; Dauer 21 min 23 s = 12:37:06 - 12:15:43). sha256 von Fassung 2.2 beim Ende unveraendert.
- Leser: frischer, unabhaengiger Leser (Claude), keine Rechnerrechnung, Rechenwege von Hand im Text
- sha256 von Fassung 2.2 beim Lesebeginn: f81999a189c456b99a9bea7da70749f0f427b4577d83fb58eaa5df073566547d (232 Zeilen)
- Keine BRIEF-Datei mit Pfad und sha256 genannt; Grundlage ist der Auftrag der Leitung in der Nachricht, woertlich befolgt.

## 0. Lesestand

- Bis 12:16:17 (date): Fassung 2.2 vollstaendig (Zeilen 1 bis 232), BEFUNDE des zweiten Lesers vollstaendig (368 Zeilen), diff 2.1 gegen 2.2 vollstaendig.
- Danach: Quellen fuer Projektzahlen (Liste unten in den Selbstanzeigen).

## A-Befunde (falsch oder zu stark, muss geaendert werden)

Anforderungen an den Wortlaut; formulieren muss der Autor.

### A1 "K = 0 als eigenes Gesetz": Torus-Schluss ueber eine Aequivalenz, die nur asymptotisch flach gilt (Abschnitt 4, Zeile 157)

- Zitat: "Mit Regularitaet und asymptotisch flachem Rand ist das nach SKALAR-SEKTOR-L die ART in maximaler Scheibung [P, S dort]. Der Erhalt von K = 0 gibt dann dieselbe Lapse-Gleichung, also greift das Torus-Argument auch dort [M, mit SKALAR-SEKTOR-L]."
- Begruendung [P, SKALAR-SEKTOR-L/DOSSIER.md]:
  - Das "dann" stuetzt die Torus-Aussage auf die Gleichheit mit der ART, die die Quelle nur fuer asymptotisch flache Raeume gibt. Der Torus hat keinen solchen Rand. Die Quelle sagt zum anderen Fall: "Kosmologisch (K != 0) wirkt lambda, und die Theorien trennen sich" (Zeile 64 bis 66) und "Belastbar ist nur die Aussage fuer asymptotisch flache, isotrope Kontinuumsfaelle" (Zeile 255 f.).
  - Die Horava-Ecke alpha = beta = 0 ist nach derselben Quelle erst mit der CMC-Bedingung K = K(T) lebensfaehig (Zeile 46 bis 53, 113 bis 116); K = 0 folgt dort nur bei asymptotisch flachem Rand. Auf dem geschlossenen Torus ist die Ecke also der CMC- bzw. York-Fall, nicht "K = 0 als Gesetz".
  - Die Folgerung selbst laesst sich fuer das woertliche Gesetz K = 0 (tr pi = 0) ohne Rand begruenden [M, meine Rechnung, ungegengelesen]:
    - Bei alpha = beta = 0 ist die Bewegungsenergie (1/sqrt g)[pi:pi - (lambda/(3 lambda - 1)) (tr pi)^2]. Herleitung: pi^ij = sqrt g (K^ij - lambda g^ij K), tr pi = sqrt g (1 - 3 lambda) K, K:K - lambda K^2 = pi:pi/g + lambda (tr pi)^2/(g (1 - 3 lambda)).
    - Gegen die ART (lambda = 1, Koeffizient 1/2) bleibt c (tr pi)^2/sqrt g mit c = 1/2 - lambda/(3 lambda - 1) = (lambda - 1)/(2 (3 lambda - 1)).
    - {tr pi(x), Integral N c (tr pi)^2/sqrt g} hat in jedem Glied einen Faktor tr pi und verschwindet auf tr pi = 0. Ein Multiplikator mu zu tr pi = 0 faellt ebenfalls heraus, weil {tr pi(x), tr pi(y)} = 0 (tr pi erzeugt Weyl-Skalierungen und ist unter ihnen invariant).
    - Also gibt der Erhalt von tr pi = 0 die Lapse-Gleichung der ART, und die Hamilton-Bedingung ist auf tr pi = 0 dieselbe. Torus-Argument und T^3-Satz greifen damit ohne Bezug auf einen Rand.
    - Offen bleibt die Nullmode von mu auf dem Torus: Am flachen Hintergrund verlangt der Erhalt von H nur Laplace mu = 0 (aus delta(sqrt g R) = sqrt g ((1/2) mu R - 2 Laplace mu) bei delta g = mu g), also ist mu = konstant erlaubt.
- Anforderung:
  - "dann" und "[M, mit SKALAR-SEKTOR-L]" nicht als Begruendung fuer den Torus stehen lassen. Fuer das woertliche Gesetz K = 0 eine randfreie Begruendung angeben (z. B. die obige) oder [H] setzen.
  - Getrennt sagen: Die Horava-Ecke selbst ist auf geschlossenen Raeumen nach SKALAR-SEKTOR-L der CMC-Fall K = K(T); dort wirkt lambda, und die Gleichheit mit der ART ist nicht belegt.
  - Die Nullmoden (konstantes N, Multiplikator der Spurbedingung) als offen nennen (passt zu Abschnitt 9 Punkt 3).

### A2 "Lesart R nach UEBERGABE-KONFLUENZ-1 bevorzugt" ist einseitig gegen die Quelle (Abschnitt 6 "Reihenfolge", Abschnitt 9 Punkt 5)

- Zitate:
  - "Lesart R ist in der Geometrie reihenfolgefest (bis 1,6e-13), Lesart P traegt im Impuls eine Spur (bis 1,3e-5), auch bei disjunkten Zuegen. Eckenfelder werden bei 2-3- und 3-2-Zuegen gar nicht uebergeben [M]."
  - "Uebergaberegel beim Umklappen (Lesart R nach UEBERGABE-KONFLUENZ-1 bevorzugt), Kaskaden-Reihenfolge."
- Begruendung [P, UEBERGABE-KONFLUENZ-1/ERGEBNIS.md Abschnitte 5 und 6.2]:
  - Die Quelle waegt ab. R ist reihenfolgefest und umkehrbar, "verliert aber Energie (TAKT-DYNAMIK-1: -2,4 bis -12,7 % ueber 10 Perioden)". P gewinnt Energie (+15 bis +20 %) und hat eine kleine Spur.
  - Beim geladenen Skalar: "Lesart R skaliert pi_v mit *0'_v / *0_v ... Das erzeugt Ladung und verletzt Gauss nach dem Zug"; "Fuer die Forderung 'Gauss nach dem Zug ohne Ladung' ist P beim Skalar die passende Wahl."
  - Negativliste der Quelle: "'Lesart P ist falsch' oder 'R ist richtig'" darf nicht gesagt werden.
  - 2.2 nennt in Abschnitt 6 selbst Energie und "Gauss nach dem Zug erhalten, ohne Ladung zu erzeugen" als Bedingungen. R verfehlt nach der Quelle beide.
  - "gar nicht uebergeben" stimmt nur fuer phi und fuer Lesart P. In Lesart R ist dphi/dt stetig, also wird pi_v = Z_t *0_v phidot* mit *0'_v/*0_v umskaliert (diagonale Uebergabe). Ergaenzung [M, Leser]: Auch im neutralen Arm aendert das die globale U(1)-Ladung des Q-Balls (proportional zu Summe_v Im(phi_v pi_v)) an jeder Ecke, deren *0 sich aendert.
  - Gueltigkeitsbereich fehlt: nur Form A (A1, A2; Form B "nicht startbar"), nur 2-3-Startzuege, statische Paarprobe, linear um flach, N = 128, Licht nicht gerechnet (Quelle Abschnitt 5 "Grenzen").
  - Die Bevorzugung steht in der Abschaetzung der Leitung (RUNDE-49.md Zeile 49), nicht in der Bedeutung der Quelle.
- Anforderung:
  - "bevorzugt" durch die Abwaegung je Sektor ersetzen: Geometrie (R reihenfolgefest, aber Energieverlust) gegen Skalar (P erhaelt Ladung bzw. Gauss). Als Abschaetzung der Leitung kennzeichnen.
  - "gar nicht uebergeben" auf phi bzw. Lesart P beschraenken.
  - Gueltigkeitsbereich nennen und R, P in einem Halbsatz erklaeren.

### A3 "Einfach gesagt", Satz 2: "unter beiden gerechneten Eckenregeln" (Zeile 232); damit A5 des zweiten Lesers nur teilweise

- Zitat: "Stoerungen wuchsen dabei aber unter beiden gerechneten Eckenregeln."
- Begruendung:
  - Abschnitt 4 desselben Dokuments: "Mit B wachsen Moden unter R1 und unter RH, unter R2 eine Mode auf einem von vier Glasnetzen (drei Reduktionen gerechnet)." RUNDE-48.md Zeile 442: "A2LR2 waechst nur auf s2".
  - Gerechnet sind drei Eckenregeln, nicht zwei. Unter der dritten wuchs mit der Literaturtraegheit nur eine Mode auf einem Glasnetz. "beiden" ist eine falsche Zahl und verschweigt den fast sauberen Fall.
  - Die Anforderung A5 des zweiten Lesers verlangte genau diesen Zusatz ("unter R2 nur auf einem von vier Glasnetzen").
  - Falls R2 bewusst nicht zaehlt, weil es von der Eichflaeche abhaengt (RUNDE-48.md Zeile 295), muss das dastehen. Abschnitt 4 zaehlt R2 mit.
- Anforderung:
  - Zahl richtigstellen und R2 einordnen: gerechnet, mit B nur eine Mode auf einem Glasnetz; oder ausdruecklich als nicht stimmige Reduktion ausgenommen.
  - Abschnitt 0 ("A1 bis A5 in 2.2 eingearbeitet") bis dahin auf "A5 teilweise" setzen.

## B-Befunde (knapp)

- **B1 Statische Beispiele gibt es auf dem Modell-Torus nicht (Abschnitt 5; "Einfach gesagt" Satz 4).**
  - Zitate: "Vakuum um eine ruhende Masse ... schliesst nur ueber den Lapse-Term"; "Momentan ruhender Staub hat Kruemmung ohne Spannung"; "In einer ruhenden, unbewegten Lage halten sich Kruemmung, das Gefaelle im Gang der Uhren und die Spannung der Materie die Waage."
  - Beide Beispiele brauchen Daten mit K_ij = 0 und rho > 0 irgendwo. Hamilton-Bedingung: R = 16 pi G rho + 2 Lambda. Bei Lambda = 0, rho >= 0 ist R >= 0 und nicht ueberall 0; das schliesst der T^3-Satz aus Abschnitt 4 [L] aus. Bei Lambda > 0 erst recht (R >= 2 Lambda > 0).
  - Ausserdem gilt fuer jede statische Lage auf einem geschlossenen Raum (Lapse-Gleichung mit K = 0 integriert): Integral N (4 pi G (rho + S) - Lambda) = 0. Mit rho + S >= 0 geht das nur bei Lambda > 0.
  - Die Beispiele sind damit Bilder aus dem offenen, asymptotisch flachen Kontinuum bzw. oertliche Bilanzen, keine Zustaende des T^3-Modells aus Abschnitt 1. Abschnitt 4 und 5 widersprechen sich so ohne Hinweis.
  - Anforderung: Beispiele als oertlich bzw. asymptotisch flach kennzeichnen; einen Satz ergaenzen, dass es auf dem T^3 mit Lambda = 0 nach Abschnitt 4 keine statische oder momentan ruhende Lage mit Materie gibt; Satz 4 des "Einfach gesagt" entsprechend einschraenken.
- **B2 Vorzeichen des Lambda-Beitrags (Abschnitt 5, Zeile 169).**
  - Zitat: "... die Kraft auf die Kante pdot_e = -dH/dq_e also +eps_e/(16 pi G l_e). Dazu kommt der Lambda-Beitrag (Lambda/8 pi G) (dV/dl_e)/(2 l_e)."
  - Rechenweg: H_Lambda = (Lambda/8 pi G) Summe_t N_t V_t; bei N = 1 ist dH_Lambda/dq_e = (Lambda/8 pi G)(dV/dl_e)(dl_e/dq_e) = (Lambda/8 pi G)(dV/dl_e)/(2 l_e), weil dq = 2 l dl. Der Ausdruck ist also der Beitrag zu dH/dq_e. In der Kraft steht er mit Minus.
  - Der Satz folgt direkt auf die Kraft; in dieser naheliegenden Lesart ist das Vorzeichen falsch.
  - Anforderung: die Groesse benennen (Beitrag zu dH/dq_e) oder in der Kraft -(Lambda/8 pi G)(dV/dl_e)/(2 l_e) schreiben.
- **B3 rho + S gegen T^3-Satz: Logik ordnen (Abschnitt 4; Abschnitt 0 "sonst nicht generisch").**
  - Mit Lambda = 0 und rho >= 0 (beim Q-Ball: U >= 0) schliesst der T^3-Satz maximale Daten mit Materie ganz aus, gleich welches Vorzeichen rho + S hat. "Dann gilt nur 'nicht generisch'" ist dort ueberholt. Bei Lambda > 0 gibt es auf T^3 mit rho >= 0 gar keine maximalen Daten (R >= 2 Lambda > 0).
  - Das Vorzeichen von rho + S zaehlt fuer Lambda < 0, fuer U < 0 und fuer die York-Alternative: -Laplace N + W N = d tau/dt hat bei d tau/dt > 0 eine positive Loesung, wenn der kleinste Eigenwert von -Laplace + W positiv ist; W >= 0 (nicht ueberall 0) ist dafuer hinreichend, W < 0 irgendwo macht es zur Pruefaufgabe [L].
  - Die Aussagen sind nicht falsch, sondern schwaecher als moeglich; die Pruefpunkte in Abschnitt 8 (Nr. 6) und 9 (Nr. 4) zielen dadurch auf den falschen Fall.
  - Anforderung: Bedingungen ordnen (Lambda-Vorzeichen, rho >= 0, rho + S >= 0) und den Pruefpunkt rho + S an CMC und Lambda < 0 binden.
- **B4 Weg ueber Z_s: Tempo-Unterschied fehlt (3.1).**
  - Zitat: "Kommt die 8 ueber Z_s allein in den Skalar, aendert sich die Compton-Wellenzahl ..."
  - Rechenweg: omega^2 = N0^2 (Z_s k^2 + U'(0))/Z_t. Weg Z_s (N0 = 1, Z_s = 8, Z_t = 1): omega^2 = 8 k^2 + U'(0), k_C^2 = U'(0)/8. Weg Z_t (N0 = 1, Z_s = 1, Z_t = 1/8): omega^2 = 8 k^2 + 8 U'(0); das ist im Skalar genau die N0-Setzung (Z_s = Z_t = 1, N0^2 = 8). In beiden Wegen ist Z_s/Z_t = 8, also laeuft der Skalar in beiden mit Tempo Wurzel 8, das Licht mit 1.
  - Anforderung: den Tempo-Unterschied fuer beide Wege nennen; der Unterschied zwischen den Wegen ist nur die Compton-Laenge.
- **B5 Zeichen S und K mehrfach belegt (2.3, 3.2, 4).**
  - S ist Shift-Operator (2.3), S = |phi|^2 (3.2), Spannungsspur in rho + S (4) und Netzname S (2.3, 4). In Abschnitt 4 steht "rho + S = 4 |phidot|^2 - 2 U" direkt neben U = U(S) mit S = |phi|^2.
  - K ist Spur der aeusseren Kruemmung (4), K_t die lambda = 1-Form (2.2), "negative Richtungen von K" (4) und "Regime K" (2.3).
  - Anforderung: eigene Zeichen; mindestens in Abschnitt 4 "S = g^ij T_ij" ausschreiben.
- **B6 Abschnitt 0: "stabil ist bisher nur eine Paarung, keine Reduktion".**
  - "nur eine" liest sich als Zahl; ohne wachsende Moden sind zwei Paarungen (A1R1, A2R1). "stabil" heisst dort "ohne wachsende Moden in den gerechneten Spektren"; die Positivitaet auf der Eichung fehlt (Abschnitt 4).
  - Anforderung: an die Paarung binden, beide nennen, Vorbehalt in einem Halbsatz.
- **B7 KRUEMMUNGS-SANDHAUFEN-2D-1: Evidenzart fehlt (Abschnitt 5).**
  - "breite Lawinen" und "Potenzgesetz knapp verfehlt" stimmen (ERGEBNIS Abschnitt 2 Punkt 3: Fitguete 0,167 > 0,15 bei N = 8000).
  - "Verzweigung ~1" ist dort ein Nachtrag nach Sicht [N, ES] im Endzustand; die Negativliste nennt die Verzweigungszahl 1 eine "Mittelfeld-Kopfrechnung". Die Karte ist ohne frischen Leser geerntet.
  - Anforderung: "grobe Schaetzung im Endzustand, Nachtrag nach Sicht" o. ae. kennzeichnen.

## C-Befunde (knapp)

- **C1 (2.3, Zeile 82):** "Die Stabilitaet stimmt mit der von B nur in linearer Ordnung um p = 0 ueberein." Das "nur" behauptet eine Abweichung darueber. Gezeigt ist die Gleichheit in linearer Ordnung; verschiedene Zwangsflaechen heissen noch nicht verschiedene Stabilitaet. Besser: "ist nur in linearer Ordnung als gleich gezeigt".
- **C2 (4, Zeile 154):** "... wenn es sich von Scheibe zu Scheibe aendert, also wenn sich das Volumen aendert." Mit dV/dt = -tau Integral N sqrt g (CMC, Vorzeichen nach Konvention) gilt: Volumen aendert sich genau bei tau ungleich 0. Fuer eine Zeit muss tau aber monoton sein. Im geschlossenen S^3-Staubuniversum geht tau am Umkehrpunkt durch 0 (dV/dt = 0) und bleibt eine Zeit [L]. Auf T^3 mit Lambda = 0 und rho >= 0 gibt es nach dem T^3-Satz keinen solchen Punkt; dort stimmt der Satz. Einschub "auf dem T^3" genuegt.
- **C3 (5, Zeilen 172 f.):** "schliesst nur ueber den Lapse-Term": bei Lambda ungleich 0 auch ueber den Lambda-Term, den Zeile 171 selbst aufzaehlt. "Mit Bewegung kommen der Bewegungsanteil (quadratisch in p) und pdot selbst hinzu": bei s ungleich 0 auch der Shiftterm (linear in p, ueber die q-Abhaengigkeit von S).
- **C4 (5, Zeile 170):** "von derselben Ordnung wie der Fehlwinkel, sobald N ungleich ist" gilt, wo die Gleichungen N an die Kruemmung binden (statisch, Newton-Fall). Bei frei gewaehltem N haengt die Groesse von der Wahl ab. Besser "im Newton-Fall".
- **C5 (3.1, Zeile 117):** "richtungsgleich auf jedem periodischen Delaunay-Netz": Fuer Licht braucht es *1_e > 0 (3.2). In Gleichstaenden (DANZER-TT-1: 41 bis 42 % der Tetraeder) haben Kanten bzw. Flaechen Duale der Groesse 0. "strikt Delaunay" bzw. "*1 > 0" dazuschreiben.
- **C6 (6):** "Lesart R" und "Lesart P" sind in 2.2 nicht erklaert (Quelle: R = Laengen und Raten stetig, Projektion auf die neue Zwangsflaeche; P = Impulse stetig, Null-Fortsetzung). "[S Treffer]" ist kein erklaertes Kennzeichen (Zeile 11).
- **C7 (0):** Bei "Codex zu Fassung 2 ... Punkte 3 und 4 teilweise; offen sind ..." gehoeren alle genannten Reste zu Punkt 4; was an Punkt 3 offen ist, steht nicht da (nach 2.2 nur noch Satz 2 des "Einfach gesagt", A3 hier). "B- und C-Befunde soweit unten vermerkt": 2.2 hat keine Vermerke mehr, alle "(Leser ...)"-Hinweise sind gestrichen. Mein Abgleich: B1 bis B14 und C1 bis C9 des zweiten Lesers sind aufgenommen; aus B11 wurde A1 hier, aus C2 der Rest B2 hier.
- **C8 (2.3 (i), DANZER-TT-1):** "die Zerlegung ist dort zu 41 % Zufall". Die Quelle sagt: 41 bis 42 % der Tetraeder haben weitere Ecken auf der Umkugel (80/192 = 0,417; 336/816 = 0,412; 1424/3456 = 0,412, von Hand), der Zitter waehlt dort die Zerlegung, und die Spanne haengt daran (gleiche Ecken: 1/1 9,0 gegen 13,1 %, 3/2 1,2 gegen 2,6 %). Die Spanne bleibt gross (3/2: 2,6 % gegen A15 0,934 %, DT3 nicht eingetroffen). Gerechnet ist A1R1. So fassen.
- **C9 (2.3, Zeile 87):** "Auf Glas waechst es an jedem k": in der Quelle "an jedem gerechneten k" (52 Glaspunkte, LR3).
- **C10 ("Einfach gesagt" Satz 4):** Der Lambda-Term fehlt in der Aufzaehlung, Abschnitt 5 nennt ihn. Bei der Einschraenkung nach B1 mit erledigen.
- **C11 (0):** "'Kruemmung = Spannung' gilt in dieser Form nur statisch und bei gleichem N": als "nur wenn" richtig. Auf dem Modell-Torus mit Materie sind beide Bedingungen zusammen aber nur bei 4 pi G (rho + S) = Lambda ueberall moeglich (statische Lapse-Gleichung mit konstantem N), siehe B1. Kein Aenderungszwang.

## Projektzahlen gegen Quellen (neue Verweise)

| Stelle | Dokument | Quelle | Ergebnis |
|---|---|---|---|
| 2.3 (i) | DANZER-TT-1: 12,2 / 6,2 / 2,6 % | ERGEBNIS Zeile 60 f.: Saatmittel 12,2 % (8 Saaten), 6,2 % (8), 2,6 % (4) | stimmt |
| 2.3 (i) | "zu 41 % Zufall" | Zeile 248 f.: 41 bis 42 % der Tetraeder in Gleichstaenden | Zahl gerundet, Lesart C8 |
| 2.3 (i) | "Grund nicht gezeigt" | RUNDE-49.md Zeile 62: "Ikosaeder-Ordnung als Grund" nicht gezeigt | stimmt |
| 6 | 32 von 32 gleich | ERGEBNIS 2 Punkt 1 und UK0: 32 nach Plan, 42 mit Nachtrag | stimmt |
| 6 | R bis 1,6e-13 | ERGEBNIS 2 Punkt 2: Delta_q <= 3,0e-14, Delta_p <= 1,6e-13 (A1, A2) | stimmt (nur Form A, A2 hier) |
| 6 | P bis 1,3e-5, auch disjunkt | ERGEBNIS 2 Punkt 3: Maximum 1,3e-5; disjunkt bis 2,8e-7 | stimmt; "bis 1,3e-5" ist das Gesamtmaximum |
| 6 | Eckenfelder "gar nicht uebergeben" | ERGEBNIS 5 Punkt 1: in R wird pi_v mit *0'/*0 skaliert | nur fuer phi bzw. P (A2 hier) |
| 6, 9 | "Offen: Kaskaden, Licht"; "R bevorzugt" | ERGEBNIS 2 Punkt 5, 5 Punkt 3; Negativliste 6.2 | offen stimmt; "bevorzugt" nicht (A2 hier) |
| 5 | Kugel breite Lawinen | ERGEBNIS 2 Punkt 3: Kugel breiter (s_c2 358 / 830 / 989) | stimmt |
| 5 | Potenzgesetz knapp verfehlt | KH2: Fitguete 0,167 > 0,15 bei N = 8000 | stimmt |
| 5 | Verzweigung ~1 | 2 Punkt 3 und 4.6: grobe Verzweigungszahl 1,01 [N] | Zahl stimmt, Kennzeichen fehlt (B7) |
| 2.3 | 142 / 28 / 12 von 511 k, kl 0,94 / 2,17 / 2,02 | LUND-REGGE-MASSE-1 Zeile 62 f., Tab. Zeilen 172 bis 174 | stimmt |
| 4 | Spuranteil 0,334 bis 0,337; Glas 28 bis 33 von 29 bis 34 | LUND-REGGE-MASSE-1 Zeilen 67 f., 204 | stimmt |
| 4 | K = 0 als Gesetz, Horava-Ecke | SKALAR-SEKTOR-L Zeilen 19 bis 24, 64 bis 66, 113 bis 116, 255 f. | asymptotisch flach stimmt; Torus-Schluss nicht gedeckt (A1 hier) |

- Nullkegel von Hand: h = a I + h_TF, h:h - (tr h)^2 = |h_TF|^2 + 3 a^2 - 9 a^2 = 0 gibt |h_TF|^2 = 6 a^2; Spuranteil 3 a^2/(3 a^2 + 6 a^2) = 1/3. Passt zu 0,334 bis 0,337.

## Tabelle: A1 bis A5 des zweiten Lesers

| Befund | Stand | Begruendung (Restpunkte hier) |
|---|---|---|
| A1 Spurbindung als erledigt gemeldet | umgesetzt | Abschnitt 0 "als Kette benannt, am Code offen", 2.2 "Am Code nicht bestaetigt", Abschnitt 8 Nr. 3. Je Leser steht der Stand da. Rest: C7 |
| A2 "R1 stabil, RH nicht" | umgesetzt | Abschnitt 4 bindet Stabilitaet an die Paarung, nennt B unter R1 und RH instabil, R2 mit einer Mode auf einem Glasnetz, drei Reduktionen, fehlende Positivitaet auf der Eichung. Rest: B6 (Wortlaut in Abschnitt 0) |
| A3 York-Zeit ohne Bedingung | umgesetzt | Bedingung (tau aendert sich, Volumen aendert sich), ruhender Torus ohne York-Zeit, Wechsel des Hintergrunds, Existenz als [L] mit Voraussetzungen. Rest: C2 |
| A4 "Folge" in Abschnitt 5 | umgesetzt | statischer Fall abgegrenzt, Lambda-Term genannt, Bewegungsterme genannt, Hamilton-Bedingung getrennt, Staub "momentan ruhend, nicht statisch", Uhren-Satz als [L]. Neu: B1 (Beispiele auf dem Modell-Torus unmoeglich), B2 (Vorzeichen Lambda), C3, C4 |
| A5 "Einfach gesagt" | teilweise | "bisher", "in unseren Rechnungen", kein "genau dann", Satz 5 als Kandidat mit Bedingung; B9, B14 und "ruhend = statisch" erledigt. Offen: "beiden gerechneten Eckenregeln" (A3 hier), R2 fehlt |

- Zusaetzlich zu den A-Befunden des zweiten Lesers: dessen B11 ist von "offen" zu einer [M]-Aussage geschaerft worden, die die Quelle nicht deckt (A1 hier).

## Von Hand geprueft und haltbar (Auftrag B)

- **2.3:** H_N(aN) = a H_N(N) aus M(aN) = M(N)/a; ohne Shift- und Gaussterm richtig, Euler und Grad 0 ebenso. Legendre mit Shift: (1/2) pᵀ M^-1 p + pᵀ S s. Mit zellweise verschiedenen S_t bleibt (1/2) bᵀ M^-1 b - (1/2) Summe_t sᵀ S_tᵀ M_t S_t s/N_t mit b = Summe_t M_t S_t s/N_t; bei S_t = S hebt sich das weg, sonst nicht, also quadratisch in s. Zwei-Zellen-Formel p^2 N1 N2/(2 (m1 N2 + m2 N1)). Nichtlokale Form mit festem M(1): bei N = c beide (1/2) c pᵀ M(1)^-1 p. Gemischte Form: Elimination von P_t gibt Summe_t vᵀ R_tᵀ G_t R_t v/(2 N_t).
- **3.1:** Zeiteinheit und Licht wie im Dokument; die Flaechen-Identitaet Summe_f *2_f |f|^2 n_f n_fᵀ = Vol I habe ich unabhaengig nachgerechnet (Gauss je Tetraeder um den Umkreismittelpunkt; c_f - c_t parallel zu n_f, g_f - c_f in der Flaeche; Flaechenterme heben sich periodisch weg; Rest Summe_f |f| |f*| n_f n_fᵀ). Rest: B4, C5.
- **4:** rho + S = 4 |phidot|^2 - 2 U mit T_mn = 2 Re(d_m phi* d_n phi) + g_mn L: rho = |phidot|^2 + |grad phi|^2 + U, S = 3 |phidot|^2 - |grad phi|^2 - 3 U, Summe 4 |phidot|^2 - 2 U. Q-Ball-Schwanz: (4 omega^2 - 2 m^2) f^2 < 0 genau bei omega^2 < m^2/2; mit U = m^2 |phi|^2 ist m die Masse (omega^2 = k^2 + m^2). Integral-Argument, T^3-Folgerung [L] und York-Bedingung haltbar (Reste B3, C2). "Gleiche Lapse-Gleichung" fuer woertliches K = 0 haltbar, Begruendung nicht (A1).
- **5:** dH/dq_e = -eps_e/(16 pi G l_e), Kraft +eps_e/(16 pi G l_e); gewichteter Schlaefli-Term mit N_ref. Staub: momentan ruhend nicht statisch (im Staub verlangt das hydrostatische Gleichgewicht d_i N = 0 [L], die Lapse-Gleichung aber Laplace N = 4 pi G N rho > 0 bei Lambda = 0). Reste B1, B2, C3, C4.

## Urteil

**An Finn weitergabefaehig: ja nach den A-Befunden.**

- Die neuen Rechnungen in 2.3, 3.1, 4 und 5 halten von Hand. Die Projektzahlen der drei neuen Verweise stimmen mit den Quellen.
- Die drei A-Befunde betreffen eine Begruendung und zwei Quellen- bzw. Zaehlstellen, keine Rechnung:
  - Torus-Schluss fuer "K = 0 als Gesetz" ueber die nur asymptotisch flache Gleichheit (A1)
  - "Lesart R bevorzugt" gegen die Abwaegung und Negativliste der Quelle (A2)
  - "beiden gerechneten Eckenregeln" im "Einfach gesagt" (A3)
- B1 (statische Beispiele auf dem Modell-Torus unmoeglich) und B2 (Vorzeichen Lambda) sollten mit den A-Befunden erledigt werden. Ein Neubau ist nicht noetig.
- Abschnitt 0 und "Einfach gesagt" sind sonst nicht staerker als der Text; Ausnahmen A3, B6, B1.

## Selbstanzeigen

- **Werkzeuge:** date, ls, wc, sha256sum, diff, grep, sed -n, cut (alle lesend) und Read. Geschrieben nur diese Datei (Write, Edit); der Ordner entstand beim ersten Write. Kein Interpreter, kein awk, kein ssh, kein git, kein Peerbus, kein Journal, keine Unteragenten. Ein grep scheiterte an einer ugrep-Grenze (keine Ausgabe), danach einfacher wiederholt.
- **grep-Ausschluesse:** Alle greps liefen auf einzelne benannte Dateien (Fassung 2.2, RUNDE-48.md, die genannten ERGEBNIS- bzw. DOSSIER-Dateien), keiner ueber einen Projektordner. Die Pflicht-Ausschluesse waren deshalb nicht noetig.
- **Ordnernamen:** `ls -la` auf RUNDE-37 (erste 50 Zeilen) zeigte Namen anderer Karten- und Leserordner, u. a. grundgleichung-v2-leser und mehrere gemeinsames-netz-*-leser. Geoeffnet habe ich nur die im Auftrag genannten Dateien. Einen parallelen Pruefer kenne ich nicht.
- **Lesetiefe:**
  - Fassung 2.2 und die BEFUNDE des zweiten Lesers vollstaendig; Fassung 2.1 nur ueber das diff (gezielt die geaenderten Stellen).
  - RUNDE-49.md vollstaendig (68 Zeilen; darin auch die Zeilen zu diesem Auftrag und eine Frage Finns). RUNDE-48.md nur per grep und Zeilen 291 bis 310.
  - SKALAR-SEKTOR-L nur per grep und Zeilen 44 bis 70, 108 bis 122. UEBERGABE-KONFLUENZ-1, DANZER-TT-1, KRUEMMUNGS-SANDHAUFEN-2D-1 abschnittsweise (Kopf, Ergebnis, Bedeutung, Negativliste, grep). LUND-REGGE-MASSE-1 nur per grep.
- **Nicht selbst geprueft:**
  - HODGE-MASSE-1 steht nicht in meiner Quellenliste: "1 bis 88 negative Richtungen", "A1RH 9, A2RH 5, A2LR1 28, A2LRH 46 von 481" und die HM0-Zahlen kenne ich nur ueber den zweiten Leser bzw. RUNDE-48.md ("28 bis 46").
  - Jacobson/Pulakkat selbst nicht gelesen. Meine Rechnung in A1 setzt die uebliche Form N sqrt g (K:K - lambda K^2 + R) ohne a_i-Terme voraus [L].
  - Code (Spurbindung, Lesarten R und P).
- **Literatur aus dem Gedaechtnis [L], an keiner Quelle geprueft:** Schoen/Yau, Gromov/Lawson; Eigenwert- bzw. Maximumprinzip-Kriterium fuer die CMC-Lapse; geschlossenes Staubuniversum mit Umkehrpunkt; hydrostatisches Gleichgewicht; Weyl-Skalierung von R in 3D; Form der Horava-Wirkung.
- **Eigene Rechnungen [M], ungegengelesen:** Klammer in A1, Ladungsaenderung unter Lesart R (A2), B1, B2, B4, C2, C8, Flaechen-Identitaet und rho + S (Abschnitt "Von Hand geprueft").
- **Einordnung:** B2 (Vorzeichen Lambda) und B1 (statische Beispiele) koennten auch als A gelten. Ich habe B gewaehlt, weil B2 in der Lesart "Beitrag zu dH/dq_e" richtig ist und B1 eine fehlende Bedingung ist, keine falsche Aussage.
- **Zeiten:** Alle Uhrzeiten stammen aus date: Start 12:15:43, Lesestand 12:16:17, vor den A-Befunden 12:31:34, Quellenabgleich 12:35:27, Ende im Kopf.
