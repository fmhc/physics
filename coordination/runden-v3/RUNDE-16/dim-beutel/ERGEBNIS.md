# DIM-BEUTEL Ergebnis (Runde 16, explorativ nach v3)

- Code-Agent. Die Endfassung habe ich ab 10:46:04 CEST geschrieben (date); den Entwurf ab 10:37:02.
- Zeitbox: 09:48:35 bis 11:18.
- Grundlagen:
  - KARTE.md (verbindlich, unveraendert).
  - Plan PLAN.md.eingefroren-20261002-095901, eingefroren vor jedem Aufruf auf der .69.
  - Nachtrag 1 (eingefroren 10:02:32), vor jedem Lauf: Randbereich der Gitter und Konvergenzregel.
  - Nachtraege 2 bis 4 (10:07:57, 10:16:43, 10:21:50), NACHTRAEGLICH, waehrend der Laeufe: Hysterese auf dem Fraktal,
    frische Starts Z3/Z4, Loeser-Parameter maxcor, neu gerechnete Kette.
- Gewertet wird die Schlussauswertung (aus/auswertung/, .69 Spur cpu, 10:45:21 bis 10:45:28 CEST).
- Alles ist modellintern; es gibt keine Messdaten. Hypothesen sind mit [H] markiert, Literatur aus dem Gedaechtnis mit
  [L?].

## 1. Ergebnis zuerst

1. **Gitter: D1, D2 und D3 sind eingetroffen. Der Beutelexponent zaehlt dort die Dimension.**
   - Gemessen: p* = 0,5001 (Kette), 0,6669 (Quadratgitter), 0,7511 (kubisch).
   - Daraus folgt d = p/(1 - p) = 1,001 +- 0,001, 2,002 +- 0,002 und 3,02 +- 0,03.
   - Bedeutung nach der Vorab-Festlegung der Karte: 3/4 bzw. 4/3 ist die Unterschrift von "3 Raumdimensionen plus
     masseloser Inhalt".
   - Warum es 3 Dimensionen sind, leitet die Rechnung nicht her; die Dimension steckt im Graphen.
2. **Sierpinski: D4 ist in der Hauptwertung "offen".**
   - Der Fortsetzungsast bleibt in zu kleinen Beuteln haengen (metastabil). Frische Starts liegen dort um bis zu
     33 % tiefer.
   - Formal gibt der Ast p* = 0,822, aber nur mit 0,9 Dekaden Plateau. Unter einer Dekade schreibt die Regel
     "offen" vor.
   - Ohne diese Regel waere D4 auf dem Ast "nicht eingetroffen" (0,822 > 0,5951). Das waere aber ein Artefakt des
     haengenden Asts: Seine Sekante springt zwischen 0,597 (k 42 -> 54) und 0,822 (k 54 -> 66).
3. **Nachtrag, nicht gewertet: Frische, selbstaehnliche Starts (Z3) sprechen fuer d_s.**
   - Gemessen: E(6,708 Q) = (2,99 bis 3,10) x E(Q). Das gibt p = 0,575 / 0,594 / 0,577 / 0,576, Mittel 0,581, also
     d = 1,39.
   - Alle vier Perioden liegen naeher an d_s (0,5772) als an d_H (0,6131).
   - Die Kontrolle mit g = 9 gibt dieselben Energien (relativ <= 3e-13). Startknoten s2 gibt 0,588 und 0,582
     (k = 70 dort nicht konvergiert).
   - Das stuetzt [H] "der Beutelexponent misst die spektrale Dimension". Es ist aber keine gewertete Bestaetigung.
4. **d_s direkt gemessen, d_s = 1,3652:**
   - Eigenwert-Zaehlfunktion (g = 7): Je Faktor 5 in lambda steigt die Zahl der Eigenwerte exakt um den Faktor 3,
     ueber fuenf Perioden. Daraus folgt d_s/2 = ln3/ln5 = 0,682606.
   - Rueckkehrwahrscheinlichkeit der Irrfahrt von s1 (g = 10): d_s/2 = 0,6826 ab t = 625.
5. **D5 ist eingetroffen.**
   - Bei kleinem Q bildet sich kein Beutel. Dann gilt p -> 1 und E = sqrt(2) Q (freie Quanten).
   - Das Plateau (p innerhalb +-0,02) ist in 3D am kuerzesten: 2,62 Dekaden, gegen 3,24 (1D) und 3,72 (2D).
   - Vorbehalt: Die Laenge haengt an der gewaehlten Graphgroesse, bei der Kette auch am Konvergenzkriterium.

## 2. Vorhersagen D1 bis D5

- Wertung nach PLAN 4 und Nachtrag 1; die Hauptwertung laeuft auf dem Fortsetzungsast.
- p* ist die Sekante ueber die letzte volle Periode (Q-Faktor 6,708) bis K_v. h* ist das Mittel von h ueber dieselben
  13 Punkte.

| Nr | Vorhersage | Ausgang | Zahlen |
|---|---|---|---|
| D1 | Kette: p -> 0,50 +- 0,02, h -> 0,50 +- 0,03 | eingetroffen | p* = 0,50015, h* = 0,4982 (K_v = 56, Q = 7,2e3) |
| D2 | Quadrat: p -> 0,667 +- 0,02, h -> 0,333 +- 0,03 | eingetroffen | p* = 0,66687, h* = 0,3331 (K_v = 79, Q = 2,8e5) |
| D3 | kubisch: p -> 0,75 +- 0,02, h -> 0,25 +- 0,03 | eingetroffen | p* = 0,75114, h* = 0,2489 (K_v = 76, Q = 1,7e5) |
| D4 | Sierpinski: p naeher an 0,577 als an 0,613 | offen | Ast metastabil; formal p* = 0,822 (K_v = 66), Plateau 0,9 Dekaden < 1. Nachtrag Z3 (nicht gewertet): 0,575 / 0,594 / 0,577 / 0,576 |
| D5 | Abweichung bei kleinem Q; Plateau in 3D am kuerzesten | eingetroffen | L_pl = 3,24 (1D), 3,72 (2D), 2,62 (3D). Hoechste Abweichung unterhalb des Plateaus: 0,42 / 0,33 / 0,25 |

- Bei der Kette begrenzt das Konvergenzkriterium K_v, nicht die Graphgroesse: k = 57 hat einen Identitaetsrest von
  1,2e-6 > 1e-6.
- Gueltig ist dort Q = 569 bis 7,2e3. Zusammen mit dem Abwaertsast reicht das Plateau von Q = 4,2 bis 7,2e3.

### Je Graph: p, h, Dimension, Fehlerband, Plateau

| Graph | gueltig bis | p* | p* Periode davor | h* | d = p*/(1-p*) | d_h = 1/h* - 1 | Fehlerband d | Plateau (+-0,02 um p*) | Beutelradius im Plateau |
|---|---|---|---|---|---|---|---|---|---|
| G1 Kette 4096 | k 56, Q 7,2e3 | 0,50015 | 0,50047 | 0,4982 | 1,0006 | 1,007 | +-0,0013 | Q 4,2 bis 7,2e3 (3,24 Dek.) | R_vol 2,5 bis 149 |
| G2 Quadrat 256^2 | k 79, Q 2,8e5 | 0,66687 | 0,66712 | 0,3331 | 2,0018 | 2,002 | +-0,0023 | Q 53 bis 2,8e5 (3,72 Dek.) | R_vol 3,4 bis 74 |
| G3 kubisch 64^3 | k 76, Q 1,7e5 | 0,75114 | 0,75311 | 0,2489 | 3,018 | 3,018 | +-0,032 | Q 415 bis 1,7e5 (2,62 Dek.) | R_vol 3,6 bis 19,6 |
| G4 Sierpinski, Ast | k 66, Q 3,5e4 | 0,822 | 0,597 | 0,141 | (4,6) | (6,1) | nicht sinnvoll | Ein-Perioden-Sekante: Q 4,5e3 bis 3,5e4 (0,90 Dek.) | Graphradius 20 bis 30 |
| G4, Nachtrag Z3 | k 46 bis 76 | 0,575 bis 0,594 (Mittel 0,581) | - | - | 1,35 bis 1,47 (Mittel 1,39) | - | Spanne | 4 Perioden, Q 1,5e3 bis 1,7e5 | Graphradius 18 bis 112 |

- Das Fehlerband ist delta d = delta p/(1 - p*)^2, mit delta p = |p* - p*_vor| + Delta p der Groessenkontrolle
  (PLAN 4).
- h ist keine unabhaengige Messung. Am Minimum gilt exakt E = omega Q + E_chi, also p_loc = 1 - h (PLAN 1).
  d_h weicht nur ab, weil h* ein Mittel ist und p* eine Sekante.
- Die Sekanten je Periode fallen auf allen Gittern von oben gegen d/(d+1):
  - G1: 0,5085 / 0,5015 / 0,5005 / 0,5001;
  - G2: 0,6890 / 0,6712 / 0,6679 / 0,6671 / 0,6669;
  - G3: 0,7840 / 0,7595 / 0,7531 / 0,7511.
- Zusatz ohne Wertung: Der Fit p_loc = p_inf + a Q^(-1/(d+1)) ueber das Plateau gibt p_inf = 0,4993 / 0,6645 /
  0,7439, also d_inf = 0,997 / 1,981 / 2,905.
  - Der Fit schiesst leicht unter den Sollwert, weil die Annaeherung nicht rein ~1/R verlaeuft.
  - Die Abweichung vom Soll bleibt <= 0,006 in p.
- **Sierpinski, Nachtrag Z3** (frische Starts, Startform A, R0 = Q^0,4 um s1, g = 10):

| Periode (k) | E(k) | E(k+12) | Verhaeltnis | p | V_bag |
|---|---|---|---|---|---|
| 46 -> 58 | 178,263 | 532,930 | 2,990 | 0,5754 | 265 -> 895 |
| 52 -> 64 | 332,495 | 1030,82 | 3,100 | 0,5945 | 409 -> 1547 |
| 58 -> 70 | 532,930 | 1599,42 | 3,001 | 0,5774 | 895 -> 2701 |
| 64 -> 76 | 1030,82 | 3087,06 | 2,995 | 0,5763 | 1547 -> 4625 |
| 70 -> 82 | 1599,42 | 4904,83 | 3,067 | 0,5887 | 2701 -> 8999 (k = 82 nicht konvergiert, nicht verwendet) |

- Erwartung, wenn d_s zaehlt (selbstaehnlich): Energie x 3 und Volumen x 3 je Periode. Zaehlte d_H, waere das
  Energieverhaeltnis 6,708^0,6131 = 3,21.
- p_loc der frischen Loesungen schwankt mit halber Periode zwischen 0,57 und 0,68. Darum taugt h = 1 - p_loc an
  einzelnen Punkten hier nicht als Dimensionsschaetzer; die Sekante taugt.

## 3. Kontrollen

### 3.1 dE/dQ = omega (die eigentliche Kontrolle, weil p + h = 1 eine Identitaet ist)

- Identitaetsrest |E - omega Q - E_chi|/E auf gueltigen Punkten, hoechstens: 9,5e-7 (G1), 1,6e-7 (G2), 9,8e-8 (G3),
  4,9e-7 (G4-Ast).
- |p_fd - Mittel p_loc| je Intervall (Median / Hoechstwert):
  - G1: 1,5e-3 / 3,1e-3. Die Beutellaenge springt in ganzen Knoten; dadurch hat E(Q) Knicke, und p_loc zeigt einen
    Saegezahn zwischen 0,4995 und 0,5038.
  - G2: 2,1e-4 / 7,1e-4.
  - G3: 8,8e-5 / 1,2e-4.
  - G4-Ast: 2,1e-4 / 2,3. Der Hoechstwert stammt aus den Beutelspruengen.
- Spline-Integral von omega Q ueber ln Q gegen E(K_v) - E(k_s): relativ 2,9e-3 (G1), 5,1e-5 (G2), 1,5e-5 (G3),
  7,8e-2 (G4-Ast mit Spruengen).
- Bewertung: dE/dQ = omega gilt auf G2 und G3 auf <= 1e-3. Auf G1 und G4 stoeren die diskreten Formwechsel.

### 3.2 Graphgroesse (bestanden auf G1 bis G3)

- G1, Kette 4096 gegen 8192 (k 40 bis 56): bitgleich, Delta E = 0, sogar gleiche Iterationszahlen.
- G2, 256^2 gegen 192^2 (k 40 bis 73): |Delta E/E| <= 9,3e-14, |Delta p| <= 3,8e-7.
- G3, 64^3 gegen 48^3 (k 40 bis 64): |Delta E/E| <= 2,4e-14, |Delta p| <= 1,1e-7.
  - Am Rand wird die Gueltigkeit verletzt: 48^3 ab k = 65 (|1 - chi| = 1,4e-6), 64^3 ab k = 77 (1,7e-6). Das hat
    K_v = 76 festgelegt.
- G4 (Nachtrag Z4): g = 9 gegen g = 10 bei k = 46, 58, 70 gibt relativ <= 3e-13. Die Perioden-p sind gleich (0,5754
  und 0,5774).

### 3.3 Startform (bestanden auf G1 bis G3, nicht auf G4)

- G2 und G3 (k = 30, 50, 70) und G1 (k = 30, 50): Startform A (Kugel) und B (Gauss-Klumpen mit chi = 1 ueberall)
  enden auf der Astenergie.
  - Abweichung <= 6e-14 (G2, G3) bzw. <= 4e-12 (G1).
  - Bei G1, k = 50, erreichte A das Kriterium nicht (Gradient 3e-5), traf aber dieselbe Energie.
  - G1, k = 70: Es gibt keinen Ast zum Vergleich (K_v = 56). Frisch A und B konvergierten dort nicht (20000 bzw. 6226
    Iterationen).
- G4, k = 50: A liegt 1,4 % und B 8,3 % ueber dem Ast. Bei k = 46, 52, 58 und 64 liegt Z3 um 21,7 / 1,4 / 22,3 /
  33,5 % unter dem Ast.
  - Das sind Konkurrenzzustaende in beide Richtungen; die Energielandschaft des Fraktals hat viele Nebentaeler.
  - Bei k = 30 liegt B 10 % unter A; dort gibt es keinen Ast.
- G4, Abwaertsast von oben (Z1, Nachtrag 2):
  - Der Beutel bleibt von k = 87 bis 81 bei 13859 Knoten stehen, zu gross. p_loc faellt von 0,59 auf 0,36.
  - Die Punkte sind ueberwiegend nicht konvergiert (Identitaetsrest > 1e-6). Bei k = 82 liegt der Ast 16 % ueber Z3.
- Startknoten s2 (Z4): E(46) liegt 2 % unter s1. Die Perioden geben p = 0,588 und 0,582; der Punkt k = 70 ist nicht
  konvergiert.

### 3.4 d_s-Direktmessung auf dem Sierpinski-Graphen

- **Spektrum g = 7** (3282 Knoten, alle Eigenwerte, dicht):
  - N(0,3) = 243, N(0,06) = 81, dann 27, 9, 3 und 1, also exakt Faktor 3 je Faktor 5 in lambda.
  - Daraus folgt d_s/2 = 0,6826062 = ln3/ln5 ueber fuenf Perioden.
  - Ohne die Nullmode zaehlt man 0,688 bis 0,861 (Endlichkeit).
- **Irrfahrt** (traege, g = 10, von s1): d_s/2 = 0,7449, 0,6979, 0,6841, 0,6829, 0,6827 und 0,6826 fuer die
  Zeitschritte t -> 5t von t = 1 bis 3125. Fit ueber t = 25 bis 15625: 0,6811.
- **Irrfahrt von s2:** 0,636, 0,651 und 0,706 fuer t = 125 bis 3125 (Fit 0,675). Die lokale Struktur ist noch nicht
  ausgemittelt, weil s2 ein Knoten niedriger Generation ist.
- **Ergebnis:** d_s = 1,3652. Der Literaturwert [L?] ist damit numerisch bestaetigt.
  - d_H = ln3/ln2 steckt in der Konstruktion; der Code prueft die Knotenzahl (3^(g+1) + 3)/2.
  - d_w = 2 d_H/d_s habe ich nicht getrennt gemessen.

### 3.5 Literatur (arXiv-API)

- Nur eine Abfrage gelang ("spectral dimension" AND Sierpinski AND gasket, 10:05:53). Die zweite brach ab
  (HTTP 000). Ihre Wiederholung bekam HTTP 429 (10:12:49); danach habe ich laut Regel abgebrochen.
- **arXiv:1207.3298** [L, Abstract]: Bei Erstpassage-Groessen auf Fraktalen haengt das Skalengesetz an Hausdorff- und
  spektraler Dimension. Es zeigt kleine log-periodische Oszillationen, numerisch bestaetigt fuer das
  Sierpinski-Dreieck. Das passt zu den log-periodischen Schwankungen hier.
- **arXiv:2211.02827:** lokale spektrale Dimension des Sierpinski-Dreiecks (das Abstract nennt keine Zahl).
- d_s = 2 ln3/ln5, d_w = ln5/ln2 und d_w = 2 d_H/d_s stehen in keinem gelesenen Abstract. Sie bleiben [L?];
  d_s ist hier aber direkt gemessen.

## 4. Abbildungen

Alle Abbildungen liegen in aus/auswertung/ (Schlussauswertung).

- **abb1-p.png:** p(Q) je Graph.
  - Punkte: p_loc = omega Q/E auf dem Ast; x = nicht gueltig. Orange: Sekante ueber eine Periode. Gruen:
    Groessenkontrolle.
  - Soll-Linien: d/(d+1) mit Band +-0,02; bei G4 0,5772 (d_s) und 0,6131 (d_H).
  - G4 zusaetzlich: Sekante der Einhuellenden (gestrichelt; nahe 0,577 ueberall dort, wo Z3-Paare liegen) und der
    Abwaertsast von oben.
- **abb2-profile.png:** phi/max und chi fuer k = 40, 52, 64 und 76.
  - Gitter: Schnitt durch die Mitte. Die chi-Wand ist etwa 2 bis 3 Gitterabstaende breit; chi ist innen praktisch 0.
  - Bei G1 gibt es nur k = 40 und 52, weil der Kettenlauf vor k = 64 endete; bei G4 nur bis k = 64.
  - Sierpinski: alle Knoten gegen den Graphabstand.
- **abb3-hysterese-volumen.png:**
  - links: Abstand der Aeste zur Einhuellenden;
  - rechts: V_bag(Q). Auf G4 sieht man die Stufen des haengenden Asts.
- **abb4-ds.png:**
  - links: Rueckkehrwahrscheinlichkeit P(t) mit der Steigung -ln3/ln5;
  - rechts: Zaehlfunktion N(lambda), g = 7, mit Stufen in Faktor-5-Abstaenden.
- **Tabellen:** punkte-G1.csv bis punkte-G4.csv (Ast mit Gueltigkeitsspalte) und auswertung.json (alle Zahlen).

## 5. Grenzen, Selbstanzeigen, Laufzeiten, sha256

### Grenzen

- Alles ist modellintern. Die Aussagen gelten nur fuer das diskrete M3-Funktional der Karte auf diesen Graphen
  (Kantengewicht 1, offener Rand).
- "Minimum" heisst lokales Minimum aus L-BFGS-B. Es gab keine Zeitentwicklung und keine Stabilitaetsanalyse.
- **Gitter:**
  - Die chi-Wand ist nur etwa 2 bis 3 Gitterabstaende breit (abb2).
  - In der Kette springt die Beutellaenge in ganzen Knoten; p_loc zeigt deshalb einen Saegezahn.
  - Die Annaeherung an d/(d+1) erfolgt von oben, je Periode um einige 1e-3 (3D).
- **Sierpinski:**
  - Der Fortsetzungsast ist metastabil. Er waechst nur in Spruengen: V_bag 139 -> 179 -> 301 -> 449 -> 521 -> 601
    -> 1007. Bei k = 67 faellt E von 2069 auf 1474, obwohl Q steigt.
  - Auch Z3 ist kein bewiesenes globales Minimum, sondern eine selbstaehnliche Familie lokaler Minima.
  - Ihr Energieverhaeltnis ~3 folgt schon aus der Selbstaehnlichkeit (Laenge x 2, Volumen x 3, lambda / 5) [H].
    Z3 prueft also vor allem, dass die Minimierung diese Familie trifft und dass Wand und Gitter sie nicht stoeren.
    Die Kombination ln3/ln(3 sqrt5) = d_s/(d_s + 1) ist dabei vorgegeben.
- **Kette:** K_v ist durch das Konvergenzkriterium begrenzt (k = 57, Q = 8,4e3). maxcor 20 reicht dort nur knapp.
- **D5:** Die Plateaulaengen haengen an den gewaehlten Graphgroessen (64^3 gegen 256^2 und 4096) und, bei der Kette,
  an der Konvergenz. "In 3D am kuerzesten" gilt nur fuer diese Wahl.

### Selbstanzeigen

1. **Planfehler:**
   - Die Randdefinition fuer Gitter (L1-Abstand) war falsch. Ich habe sie in Nachtrag 1 vor jedem Lauf berichtigt.
   - Der Plan nennt r = 1,17213; richtig ist (3 sqrt5)^(1/12) = 1,17188. Der Code rechnet mit der Formel.
2. **Versionsabfrage:** Neben py_compile habe ich auf der .69 einmal `python -c "import scipy, numpy, matplotlib"`
   ausserhalb von kleintest.sh aufgerufen (unter 1 s, keine Rechnung).
3. **Rauchtest:** Beim ersten Aufruf war ein Logpfad falsch (cwd). Fuer die Spur cpu2 lief dadurch zunaechst nichts;
   ich habe den Aufruf wiederholt.
4. **Loeser waehrend der Laeufe umgestellt (Nachtrag 3):**
   - maxcor 20 -> 5, weil die Laufzeit nicht reichte.
   - G3 hat k <= 69 mit maxcor 20 und k >= 70 mit maxcor 5; der G4-Ast entsprechend k <= 64 und k >= 65.
   - Funktional und Kriterien blieben gleich.
5. **Kette:**
   - Der maxcor-5-Versuch erfuellte das Kriterium ab k = 54 nicht. Ich habe ihn per kill (PID) abgebrochen; er wird
     nicht gewertet (aus/haupt/punkte-ket4096-auf.jsonl).
   - Neu gerechnet mit maxcor 20 (ket4096m20-auf). Diesen Lauf habe ich nach k = 59 ebenfalls per PID beendet, weil
     k = 57 schon ungueltig war.
6. **Laufreihen umgeplant:**
   - Fuenfmal habe ich lokale Laufreihen-Skripte (bash) per kill -9 beendet, ohne laufende Rechnungen zu
     unterbrechen.
   - Einen auf der .69 noch wartenden Aufruf (flock, ohne Rechnung) habe ich per PID beendet. Kein pkill -f.
7. **Weggefallen:** die G4-Fortsetzungsaeste g = 9 und s2 (ersetzt durch Z4), der G4-Abwaertsast unter k = 40 und Z2
   (Quadrat von oben).
   - Die G4-Startformkontrolle hat deshalb nur bei k = 50 einen Ast zum Vergleich.
   - Frisch A bei k = 80 lief in die Zeitgrenze.
8. **auswertung.py:**
   - Nach der Probe-Auswertung habe ich Z3/Z4 und den Kettenpfad ergaenzt.
   - In der ersten Schlussauswertung (10:44:39) stand ein falscher Vergleichswert fuer d_H: 0,5772 statt
     p = d_H/(d_H + 1) = 0,6131. Er betraf nur das JSON-Feld D4 und die Linie in abb1.
   - Ich habe den Wert berichtigt und um 10:45:21 neu ausgewertet; gewertet wird diese Fassung. D4 ist ohnehin
     "offen", und den Nachtrag-Vergleich habe ich mit 0,5951 gefuehrt.
9. **Probe-Auswertungen** auf Teildaten (auswertung-zwischen/, auswertung-fastfinal/) liefen ueber kleintest.sh und
   sind nicht gewertet.

### Laufzeiten (.69, kleintest.sh, CEST; alle rc = 0)

| Aufruf | Spur | Start | Ende | Laufzeit |
|---|---|---|---|---|
| Rauchtests (5 Aufrufe, aus/rauch/) | cpu, cpu2 | 10:02:46 | 10:04:27 | 9 bis 35 s |
| kub64-auf (maxcor 20) | cpu | 10:05:46 | 10:14:20 | 8 min 34 s |
| sie10s1-auf (maxcor 20) | cpu2 | 10:05:47 | 10:14:33 | 8 min 46 s |
| kub64-auf-2 (weiter, maxcor 5) | cpu | 10:14:22 | 10:16:41 | 2 min 18 s |
| sie10s1-auf-2 (weiter) | cpu2 | 10:14:33 | 10:20:40 | 6 min 7 s |
| ket4096-auf (maxcor 5, abgebrochen) | cpu | 10:16:45 | 10:18:02 | 1 min 17 s |
| frisch Z3 | cpu | 10:16:47 | 10:20:25 | 2 min 23 s |
| ket4096-ab | cpu | 10:18:02 | 10:20:35 | 10 s |
| ket4096m20-auf (beendet nach k = 59) | cpu | 10:18:10 | 10:23:12 | 2 min 37 s |
| qu256-ab | cpu | 10:20:35 | 10:25:37 | 2 min 24 s |
| qu256-auf | cpu2 | 10:20:41 | 10:26:25 | 5 min 40 s |
| ds | cpu2 | 10:26:26 | 10:26:59 | 33 s |
| ket8192m20-auf | cpu | 10:23:17 | 10:28:25 | 2 min 48 s |
| kub64-ab | cpu | 10:25:40 | 10:34:28 | 6 min 3 s |
| frisch sie10s1 (Startformen) | cpu2 | 10:26:59 | 10:36:00 | 9 min 1 s |
| qu192-auf | cpu | 10:29:33 | 10:36:31 | 2 min 3 s |
| Z4 g9 / Z4 s2 | cpu2 | 10:36:03 | 10:38:40 | 16 s / 2 min 17 s |
| kub48-auf | cpu | 10:34:28 | 10:38:40 | 2 min 9 s |
| frisch qu256 / kub64 / ket4096 | cpu | 10:36:32 | 10:44:13 | 1 min 3 s / 1 min 23 s / 3 min 6 s |
| sie10s1-oben (Z1) | cpu2 | 10:38:40 | 10:44:38 | 5 min 58 s |
| Schlussauswertung | cpu | 10:45:21 | 10:45:28 | 7 s |

- Startzeiten schliessen die Wartezeit am Spur-Lock ein. "Laufzeit" ist die Service-Laufzeit.
- Die Logs liegen in aus/logs/. Die Zustandsdateien (zustand-*.npz) liegen nur auf der .69 unter
  /home/fmh/fmhc-physics-remote/runde16-dim-beutel/aus/.

### sha256

Plan und Nachtraege:

    f81e389fb50fc731cc628d8f5a58db13bcf015760f4e8963712e4ce7836f5131  PLAN.md.eingefroren-20261002-095901
    d2118792d06c1e2a4adbf53e0d521223797d11c8aec0c52ddfa43fff7fb7075f  PLAN-NACHTRAG-1.md.eingefroren-20261002-100232
    c92e7fe73f6084a245996f2ae79402fddb82b093779368a2706a9fe67cc4881a  PLAN-NACHTRAG-2.md.eingefroren-20261002-100757
    9cc4bbdd7ee1c40e00d0cb21b3c721349f3fe29ec2508e0d59b7d759e7e7e598  PLAN-NACHTRAG-3.md.eingefroren-20261002-101643
    38e97c13616a4f4541a28eccacb8cf855f70de2115761fc3f1b9908a7d6ea5ed  PLAN-NACHTRAG-4.md.eingefroren-20261002-102150

Code (lokal und auf der .69 gleich):

    8d9e3659fc33997bbc0936008c88ccd133ac5a137bc01b4775e250df7c957b3e  code/dimbeutel.py    (Rauchtest, kub64-auf, sie10s1-auf)
    44f228abc9db91a73c17638e925dbc258aa174aa4fe6e62cd1c9145e933c15f6  code/dimbeutel2.py   (alle Aufrufe ab 10:14)
    04ea620270552fcda8937b6e3fe650c80b3ad464fea6b10bb578223d3d21d9bf  code/auswertung.py   (Schlussauswertung 10:45:21)

Ergebnisse:

    aa1de2ba4c32f278935970446306a37ee0aa38972956e592e200dd39e34e93bc  aus/auswertung/auswertung.json
    738abb4af363b4ef2a0f783c23fee88166b6a9bee7d2c0d8e247e23cf327cbf2  aus/auswertung/abb1-p.png
    9f1c7ab6296772eb0ae5c6943cf00dcc8e2da6da28eb84c6e7f908628f94ad1a  aus/auswertung/abb2-profile.png
    06b75bd268ddcf0f0ff69f85ad1ec2cdfa7c25f22c01962240a4927a5a85557a  aus/auswertung/abb3-hysterese-volumen.png
    ca6be7bfe4534e356479d9c92087d1a6f86b0b517d143cd60307ccad2ad12132  aus/auswertung/abb4-ds.png
    d66b713018c98be80e065cda3e8bc8c27da4db65f06734742efba7e0c547517e  aus/auswertung/punkte-G1.csv
    0b275d5aa8077b273faa7c56445a63224e6bae1cc9b9678c064a1a30d6fde3ce  aus/auswertung/punkte-G2.csv
    b58b846aad92bc049970894a0722348790cc59e9065cf8500a2604c5339a28c4  aus/auswertung/punkte-G3.csv
    05a81b78f243e96cb4638e481b2bc0a8d1ab64b781e943b039293573a2522d56  aus/auswertung/punkte-G4.csv
    04f0fc9767447e78084f13bfd6cfdd4c1fe37e5ac40204b659a6678d25bd4742  aus/haupt/punkte-ket4096m20-auf.jsonl
    33ea7f6b6eef5a957948e9b86ed2f255edbb4209c213bc3b992b4d8af23a4530  aus/haupt/punkte-ket4096-ab.jsonl
    9e81a77624b9cafb6e8c1482f4e44c4116fa18e8c747ea899f215e47b9db990c  aus/haupt/punkte-qu256-auf.jsonl
    67cffac55d6bec360419af74a758f4be86e062ecbf6f77fbe3421483870557c6  aus/haupt/punkte-qu256-ab.jsonl
    3314208194d22c260cbb27024a5bdf15579f29a4085d474f271ea283e71d7274  aus/haupt/punkte-kub64-auf.jsonl
    9da196b360772306d3eb699682109329463c06948476dbf0ffc7735a3cc09422  aus/haupt/punkte-kub64-ab.jsonl
    daa132c83f4ed04c6dc503ff5202c1ad52bf16251ab8f4aa6b3e91678a28f13f  aus/haupt/punkte-sie10s1-auf.jsonl
    de2d80d9467cf4341c46df63b7bcf5ea7c1de90ce3e109facc54654480cfe1e1  aus/haupt/punkte-sie10s1-oben.jsonl
    adcf3accd2ba53b56327a7ca94b66861da068a544c8ee00cc54710471bec4577  aus/kontrolle/punkte-ket8192m20-auf.jsonl
    faab702f1fa5811bf9148ccf159f2accff5a2a994f0397f7320526dcf95739cd  aus/kontrolle/punkte-qu192-auf.jsonl
    97d8657107e43e768ff2f9bed477bd28ee2acc1c9b44661e8b6b557c90ed2ad4  aus/kontrolle/punkte-kub48-auf.jsonl
    b67c8a8e63c76c851f2a1bad19a7d5a1f2e7575dfa480319b6ef8b110bf9d803  aus/frisch/frisch-sie10s1-z3.jsonl
    a33dbeffe5b3e6d81e74e7d8bf95bebf35f23732ac38bd60f48b5e5f2b0c7b3b  aus/frisch/frisch-sie9s1-z4.jsonl
    7162408d0c365f2a3f4c06c3e83cd9b9ebe1639ffc23e2ba2dda2e379b9e99a6  aus/frisch/frisch-sie10s2-z4.jsonl
    51bd340cfd183666d9142fc7d0223bbd1a359d748ce690f700d24f7478cab240  aus/frisch/frisch-sie10s1.jsonl
    9f0708f05e31256131213a76fbf0f7a9e11e0ed77ef8980893663ddac6fa63e2  aus/frisch/frisch-qu256.jsonl
    6f40213421efdf5efa0d530b650e3b3bee9171f4bc804b66100ce23b92b8b168  aus/frisch/frisch-kub64.jsonl
    30d3eb1e1aca78f5b4617efa9ef015537da586e0719769b885d38de2a49467a3  aus/frisch/frisch-ket4096.jsonl
    4ed00baba7d8d30100b073fa4281d0e72fe6555153bd982e0a8020a5e7da25d2  aus/ds/ds.json

## 6. Einfach gesagt

Wir haben ausgerechnet, wie viel Energie ein "Beutel" braucht, der eine bestimmte Menge masseloser Wellen einsperrt.
Das haben wir auf einer Linie, einer Flaeche, einem Wuerfelgitter und einem Fraktal (dem Sierpinski-Dreieck) gemacht.
Auf den drei gewoehnlichen Gittern waechst die Energie genau mit der erwarteten Potenz 1/2, 2/3 und 3/4. Aus dieser
Potenz kann man die Dimension zurueckrechnen; die 3/4 (bzw. 4/3) ist die Handschrift von drei Raumrichtungen plus
masselosem Inhalt. Auf dem Fraktal blieb unser Standardverfahren in zu kleinen Beuteln haengen, deshalb ist die
Hauptwertung dort offen. Frisch gestartete Rechnungen zeigen aber die Potenz 0,58: Das passt zur "spektralen"
Dimension 1,37, nicht zur "geometrischen" 1,58. Warum unsere Welt drei Dimensionen hat, erklaert die Rechnung nicht,
denn die Dimension steckt schon im Gitter.
