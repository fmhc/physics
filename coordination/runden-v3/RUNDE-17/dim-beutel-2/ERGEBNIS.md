# DIM-BEUTEL-2 Ergebnis (Runde 17, gewertete Wiederholung, explorativ nach v3)

- Code-Agent. Entwurf geschrieben ab 11:49:50 CEST (date), Endfassung ab 12:00:10 (date), nach der Schlussauswertung.
- Zeitbox: 10:50:22 bis 12:20.
- Grundlagen:
  - KARTE.md (verbindlich, unveraendert).
  - PLAN.md.eingefroren-20261002-110453, eingefroren vor jedem Aufruf auf der .69.
  - Nachtrag 1 (eingefroren 11:07:55): nach Rauchtest und d_s-Lauf, vor den Hauptlaeufen. Er legt maxcor 20 und
    6 Stufen je Periode fuer F2 fest.
  - Nachtraege 2 bis 7 (11:12:35, 11:20:15, 11:29:31, 11:31:38, 11:36:10, 11:49:43) sind NACHTRAEGLICH. Sie
    aendern nur den Zeitplan, dazu kommt Code-Version 3b (Formzustaende, Nachtrag 4). Physik, Formen,
    Loeser-Einstellungen und Wertung sind unveraendert.
- Gewertet wird die Schlussauswertung aus/auswertung/ (code/auswertung2.py, .69 Spur cpu, 11:58:45 bis 11:58:52).
- Alles ist modellintern, ohne Messdaten. Hypothesen sind mit [H] markiert, Literatur aus dem Gedaechtnis mit [L?].

## 1. Ergebnis zuerst

1. **E1 ist eingetroffen: Beim Sierpinski-Dreieck ist p_per = 0,583 +- 0,018.**
   - Das ist das Mittel von 14 Ein-Perioden-Sekanten (k = 34 bis 72, 3,17 Perioden, Q = 220 bis 9,1e4,
     Beutelradius 8 bis 74).
   - 13 der 14 Sekanten liegen zwischen 0,575 und 0,587. Ein Ausreisser liegt bei 0,643 (Periode k 56 -> 68).
2. **E3 ist eingetroffen: Beim Vicsek-Fraktal ist p_per = 0,550 +- 0,019.**
   - Das ist das Mittel von 13 Sekanten (k = 18 bis 54, genau 3 Perioden, Q = 85 bis 6,2e5, Beutelradius 8 bis 164).
   - Der Wert liegt unter der Grenze 0,569, also naeher an p_s = 0,543 als an p_H = 0,594.
   - 11 der 13 Sekanten liegen zwischen 0,538 und 0,557. Ausreisser: 0,607 (Periode 38 -> 50) und 0,569 (42 -> 54).
3. **E2 ist eingetroffen: d_s des Vicsek-Graphen, direkt gemessen, ist 1,184.**
   - Gemessen per Laplace-Zaehlung bei g = 8. Je Spektralperiode (Faktor 15) waechst die Eigenwertzahl meist exakt um
     den Faktor 5. Die Irrfahrt gibt 1,188 bis 1,193.
   - Das Soll bleibt 2 ln5/ln15 = 1,1886, denn die Abweichung 0,005 ist kleiner als 0,03.
4. **E4 ist eingetroffen: p_per liegt bei beiden Fraktalen nahe d_s/(d_s + 1).**
   - Abweichung F1: +0,006; F2: +0,007; erlaubt sind je 0,02.
   - Alle drei Ausreisser zeigen nach oben (Richtung p_H) und haben dieselbe Ursache: Die selbstaehnliche Loesung war
     gefunden, verfehlte aber knapp das Konvergenzkriterium.
     - F1, k = 68: E = 2,9999 x E(56).
     - F2, k = 50 und 54: E = 5,09 bzw. 4,999 x E eine Periode tiefer.
     - Der Identitaetsrest lag bei 1,4e-6 bis 3,5e-6, das Kriterium verlangt <= 1e-6. Diese Loesungen zaehlten
       deshalb nicht.
5. **Bedeutung (laut Karte):** E1 und E3 sind eingetroffen.
   - Der Beutelexponent misst die spektrale Dimension, also wie sich Wellen und Diffusion ausbreiten, nicht die
     Raumfuellung. Er taugt damit als Dimensionsmesser fuer Graphen ohne vorgegebene Dimension.
   - Einschraenkungen:
     - Er taugt nur als Sekante ueber volle selbstaehnliche Perioden. Der lokale Exponent p_loc = omega Q/E
       schwankt auf den Fraktalen zwischen 0,37 und 0,80.
     - Das Ergebnis ist zum grossen Teil schon durch die Selbstaehnlichkeit vorgegeben (Abschnitt 5, Grenzen).

## 2. Vorhersagen E1 bis E4

| Nr | Vorhersage | Ausgang | Zahlen |
|---|---|---|---|
| E1 | Sierpinski: p_per = 0,577 +- 0,015 (naeher an p_s als an p_H) | eingetroffen | p_per = 0,5828 +- 0,0176 (14 Sekanten, 3,17 Perioden); Abstand zu 0,577: 0,006 |
| E2 | Vicsek: d_s direkt 1,19 +- 0,03 | eingetroffen | d_s = 1,1840 (Zaehlung g = 8, 34 Sekanten, Spanne 1,151 bis 1,189); Irrfahrt 1,188 / 1,193 / 1,190 |
| E3 | Vicsek: p_per naeher an p_s (0,543) als an p_H (0,594) | eingetroffen | p_per = 0,5498 +- 0,0190 < Grenze 0,5687 (13 Sekanten, 3,0 Perioden) |
| E4 | beide: p_per innerhalb +- 0,02 um d_s/(d_s + 1) | eingetroffen | F1: 0,5828 - 0,5772 = +0,0056; F2: 0,5498 - 0,5431 = +0,0067 |

- p_per(k) = ln(E(Q_k+12)/E(Q_k))/ln P, mit P = 3 sqrt5 = 6,708 (F1) bzw. 5 sqrt15 = 19,365 (F2). Das Band ist +- eine
  Standardabweichung der Sekanten (PLAN 4).
- Bei p_per zaehlt je Stufe die tiefste Energie unter den konvergierten Formen A, Bm, Bp.

### F1 Sierpinski g = 10 (Mitte s1 = (256, 256))

- Sollwerte: d_s = 1,3652 (DIM-BEUTEL, direkt), d_H = 1,5850; p_s = 0,5772, p_H = 0,6131.
- p_per je Periode (Start-k):

| 34 | 36 | 38 | 40 | 42 | 44 | 46 | 48 | 50 | 52 | 54 | 56 | 58 | 60 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0,5799 | 0,5746 | 0,5746 | 0,5782 | 0,5769 | 0,5754 | 0,5764 | 0,5764 | 0,5841 | 0,5781 | 0,5790 | 0,6427 | 0,5764 | 0,5869 |

- Ergebnis: Mittel 0,5828, Standardabweichung 0,0176, Spanne 0,5746 bis 0,6427.
  - Nicht ueberlappende Perioden (ab k = 34, 46, 58): 0,5799 / 0,5764 / 0,5764.
  - Daraus d = p/(1 - p) = 1,397 (Soll d_s 1,365, d_H 1,585).
- Beutelbereich: k = 34 bis 72. Bei k = 74 und 78 ist R_bag = 136 bzw. 138, also groesser als R_self/2 = 128.

### F2 Vicsek g = 8 (Plusfassung, Mitte c = (3280, 3280))

- Sollwerte: d_s = 2 ln5/ln15 = 1,1886 (direkt 1,1840), d_H = ln5/ln3 = 1,4650; p_s = 0,5431, p_H = 0,5943.
- p_per je Periode (Start-k):

| 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 42 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0,5382 | 0,5394 | 0,5419 | 0,5412 | 0,5421 | 0,5569 | 0,5421 | 0,5428 | 0,5436 | 0,5427 | 0,6065 | 0,5413 | 0,5687 |

- Ergebnis: Mittel 0,5498, Standardabweichung 0,0190, Spanne 0,5382 bis 0,6065.
  - Nicht ueberlappende Perioden (ab k = 18, 30, 42): 0,5382 / 0,5421 / 0,5687.
  - Daraus d = p/(1 - p) = 1,221 (Soll d_s 1,189, d_H 1,465).
- Beutelbereich: k = 18 bis 54. Bei k = 14 und 16 ist R_bag = 5 < 8.
- **Periode (Schreibtisch, PLAN 1):**
  - Laenge x 3 gibt Knoten x 5. Der Widerstand waechst auf dem Baum wie die Laenge, also kleine Eigenwerte x 1/15.
  - Daraus folgt Q-Faktor 5 sqrt15 = 19,365 und Energie x 5, also p = ln5/ln(5 sqrt15) = d_s/(d_s + 1).
  - Die Zaehlung bestaetigt den Eigenwertfaktor 15 direkt: N(lambda)/N(lambda/15) = 5 exakt an den meisten Stellen.
- Zusatz, nicht gewertet: Ohne die drei Ausreisser waeren die Mittel 0,578 (F1) und 0,543 (F2).

### d_s-Direktmessung Vicsek (aus/ds/ds-vicsek.json)

- Die Zaehlung N(lambda) laeuft per Traegheitssatz: Gauss-Elimination auf dem Baum, ohne Auffuellung, exakt.
  - Pruefung bei g = 5 gegen die dichten Eigenwerte: Alle fuenf Pruefstellen stimmen ueberein (25, 116, 500, 1876,
    2001).
- Sekanten ueber eine Spektralperiode im Skalenbereich (N(lambda/15) >= 5, N(lambda) <= n/25):
  - g = 8: d_s = 1,1840 (34 Sekanten);
  - g = 7: 1,1826;
  - g = 5: 1,1764.
  - Typisch ist d_s/2 = 0,594316 = ln5/ln15 exakt. Einzelne Stellen liegen tiefer (bis 0,575), naemlich dort, wo eine
    Stufe der Treppe N(lambda) in das Fenster faellt.
- Irrfahrt (traege, vom Mittelpunkt, g = 7, bis t = 15^4):
  - Sekanten d_s = 0,978 (t = 1 -> 15), 1,188, 1,193, 1,190 (t = 3375 -> 50625);
  - Fit ueber t = 225 bis 50625: 1,154. Der Fit mittelt nicht ueber volle Perioden der log-periodischen Schwingung,
    die Sekanten tun das.

## 3. Kontrollen

### 3.1 dE/dQ = omega an jeder Stufe

- Von der besten Loesung aus wird nach Q e^(+-0,01) fortgesetzt; daraus p_fd = ln(E+/E-)/0,02.
- F1 (20 Stufen im Bereich):
  - |p_fd - p_loc| hat Median 1,2e-6 und Hoechstwert 1,4e-5;
  - alle +-Loesungen sind konvergiert, keine aendert V_bag;
  - **bestanden.**
- F2 (19 Stufen):
  - Median 1,1e-6, Hoechstwert 1,9e-6; keine +-Loesung aendert V_bag.
  - Bei k = 48 erfuellte eine der beiden +-Loesungen das Konvergenzkriterium nicht. Ihre Gradient- und
    Identitaetswerte habe ich nicht gespeichert; p_fd - p_loc ist dort 2,6e-7.
  - Nach PLAN 4 ist die Kontrolle damit formal **nicht bestanden**. In der Sache gilt dE/dQ = omega aber auf
    <= 2e-6.
- Ausserhalb des Bereichs: F1 k = 74 und 78 haben ebenfalls je eine nicht konvergierte +-Loesung.

### 3.2 Zwei Generationen (voller Graph der kleineren Generation gegen Teilgebiet der grossen; beide Startform A)

- **F1: g = 9 (voller Graph, 29526 Knoten) gegen g = 10.**
  - 12 Stufen k = 34 bis 78, groesste relative Abweichung 1,3e-11 (wo beide konvergiert sind). **Bestanden.**
  - Die Kontrolle prueft die Graphgroesse und das Teilgebiet zugleich.
  - Bei k = 74 ist A im Hauptlauf nicht konvergiert. Die Energie stimmt trotzdem auf 6e-13.
- **F2: g = 7 (voller Graph, 78125 Knoten) gegen g = 8.**
  - 6 Stufen: k = 14, 20, 26, 32, 38, 50 (k = 14 liegt ausserhalb des Bereichs).
  - Groesste relative Abweichung 1,9e-13. **Bestanden.**
  - R_bag reicht dabei bis 107; R_self der Kontrolle ist 1093.
  - k = 44 lief auf beiden Spuren in die ZEITGRENZE: A braucht dort auch im Hauptlauf 20003 Iterationen. k = 56 und
    62 entfielen (Nachtrag 7). Die Kontrolle deckt also 5 der 7 Kontrollstufen im Bereich ab.

### 3.3 Zwei Startformen

- **F1:**
  - Die beste Form im Bereich war 10-mal A, 7-mal Bp und 3-mal Bm.
  - Die Formen unterscheiden sich um bis zu 28 %; die Energielandschaft hat viele Nebentaeler.
  - p_per nur aus A (wo A gueltig ist): 0,5762. Der Unterschied zu 0,5828 ist 0,007 <= 0,01, also **robust**.
- **F2:**
  - Die beste Form war 13-mal Bp, 6-mal A und nie Bm. Bm (kleiner Startradius) liegt bis zu 89 % hoeher und
    konvergiert oben oft nicht (maxiter 30000).
  - p_per nur aus A: 0,5454. Der Unterschied ist 0,004, also **robust**.

### 3.4 Beutelradius gegen Zelle und Graph

| | Zelle | R_bag im Bereich | R_bag/Zelle | R_self | R_bag/R_self | Wandkanten |
|---|---|---|---|---|---|---|
| F1 | 1 (Dreieckskante) | 8 bis 96 | 8 bis 96 | 256 | 0,03 bis 0,38 | 8 bis 32 |
| F2 | 1 (Gitterzelle) | 8 bis 242 | 8 bis 242 | 3280 | 0,002 bis 0,074 | meist 4 (volle Kopie), bis 12 |

- R_bag ist der groesste Graphabstand eines Beutelknotens (chi < 1/2) vom Mittelpunkt.
- Die Spannen sind die Extremwerte im Bereich, nicht Anfang und Ende. Am Bereichsrand ist R_bag = 8 und 74 (F1)
  bzw. 8 und 164 (F2).
- Der Beutel waechst in Spruengen, entlang der Teilkopien des Fraktals (F2 zum Beispiel V = 49, 149, 249, 749, 1249, 3749,
  6244 Knoten).

## 4. Abbildungen (aus/auswertung/)

- **abb1-p.png:** p_loc (Punkte), p_fd (Kreuze) und p_per (Quadrate, an der Periodenmitte) gegen Q, je Fraktal.
  Linien: p_s (gruen), p_H (rot) und das Mittel von p_per (gestrichelt).
- **abb2-profile.png:**
  - oben: phi/max (Punkte) und chi (Striche) gegen den Graphabstand, je vier Stufen;
  - unten: Lagebild des Beutels auf dem Fraktal (F1 k = 70, F2 k = 54); Farbe phi/max, grau chi > 1/2.
- **abb3-ds.png:** Zaehlfunktion N(lambda) fuer Vicsek g = 5, 7, 8 und Rueckkehrwahrscheinlichkeit P(t), je mit
  Steigung ln5/ln15.
- **abb4-E.png:** E/Q^p_s gegen Q fuer alle Formen und das Minimum. Die Schwingung ist log-periodisch; die gepunkteten
  Linien begrenzen den Beutelbereich.
- Tabellen: stufen-F1.csv, stufen-F2.csv; alle Zahlen in auswertung.json.

## 5. Grenzen, Selbstanzeigen, Laufzeiten, sha256

### Grenzen

- **Modellintern:** Die Aussagen gelten nur fuer das M3-Funktional auf diesen Graphen (Kantengewicht 1). "Minimum"
  heisst lokales Minimum aus L-BFGS-B; das globale Minimum ist unbekannt. Die drei Startformen landen oft in
  verschiedenen Taelern (bis 28 % bzw. 89 % Unterschied).
- **Selbstaehnlichkeit [H]:** Auf exakt selbstaehnlichen Graphen gibt jede selbstaehnliche Familie lokaler Minima bis
  auf Wandversatz genau p = ln M/ln P.
  - M ist der Massenfaktor (3 bzw. 5), P = M sqrt(T) mit dem Eigenwertfaktor T (5 bzw. 15).
  - Die Rechnung prueft also vor allem dreierlei: Die Minimierung trifft solche Familien; die Q-Periode kommt aus
    der Eigenwertskalierung (d_w); Wand und Gitter stoeren nicht.
  - Dass dabei d_s statt d_H herauskommt, folgt aus der Wellengleichung (omega^2 = Eigenwert). Es ist keine
    unabhaengige Entdeckung.
- **Konvergenzkriterium:** Bei grossen Beuteln verfehlten selbstaehnliche Loesungen das Kriterium knapp
  (Identitaetsrest 1,4e-6 bis 3,5e-6). Das gab die drei Ausreisser, alle nach oben. Die Regel blieb unveraendert.
- **Teilgebiet:** Gerechnet wurde auf dem Teilgebiet Rcut um den Mittelpunkt, aussen festes Vakuum. Der
  Randlagentest (<= 1e-10) und die Generationenkontrolle auf dem vollen Graphen (F1 1,3e-11) zeigen keinen Einfluss.
- **p_loc** ist auf Fraktalen kein Dimensionsschaetzer. Es schwankt mit der Beutelform zwischen 0,37 und 0,80.
- **F2:** Der Bereich umfasst genau die geforderten 3 Perioden. Das gelang nur mit den Nachtraegen 3 bis 6 (Zeitplan,
  Version 3b).

### Selbstanzeigen

1. **Rauchtest-Start:** Der erste lokale Start scheiterte. Der Logordner wurde im Hintergrundjob angelegt und war beim
   zweiten Befehl noch nicht da (Wettlauf). Ich habe 10 s spaeter neu gestartet; kein .69-Aufruf war betroffen.
2. **auswertung2.py:**
   - Das Dateimuster der Profile habe ich vor der ersten Auswertung um den Tag ergaenzt.
   - Nach Zwischenauswertung 2 habe ich in abb1 den p-Bereich von 0,45 bis 0,75 auf 0,30 bis 0,95 erweitert, damit
     alle p_loc-Punkte sichtbar sind. Das betrifft nur die Abbildung.
3. **Nachtraege 2 bis 7 sind nachtraeglich.** Jeder nennt, was ich gesehen hatte. Die Zwischenauswertungen
   (aus/auswertung-zwischen/, aus/auswertung-zwischen2/) habe ich vor den Nachtraegen 4 bis 7 gesehen; sie sind nicht
   gewertet.
4. **Code-Version 3b mitten in der F2-Folge (Nachtrag 4):** Sie speichert und laedt nur Formzustaende.
   - Die Stufen k = 50 und 52 stammen aus Version 3b, alle anderen aus Version 3.
   - Fuer k = 50 lief auf cpu die Formreihenfolge Bp, A, Bm (Nachtrag 6). Der Stufendatensatz k = 50 stammt von cpu2:
     A und Bm dort gerechnet, Bp aus dem cpu-Formzustand geladen.
5. **Beendete Prozesse (jeweils keine laufende Rechnung):**
   - die lokale Warteschleife "F2 von oben" (Nachtrag 4);
   - die wartenden Aufrufe 2 und 3 der cpu-Kette 3b (Nachtrag 6). Das Beenden der lokalen ssh beendete die
     Gegenseite nicht. Deshalb habe ich auf der .69 bash-Schleife, kleintest und flock per PID beendet.
   - die bash-Schleife der cpu2-Kette auf der .69 (Nachtrag 7). Der laufende Kontrollaufruf lief weiter.
6. **Verschwendete Rechenzeit:**
   - Version 3 rechnete k = 50 dreimal bis zur ZEITGRENZE (cpu2, Aufrufe 2 bis 4).
   - Bm bei k = 50 lief insgesamt viermal, mit jeweils derselben Energie 2537,876607 (deterministisch).
7. Im Kopf von Nachtrag 5 steht "11:31:4x". Die Zeit vor dem Schreiben war 11:31:38.
8. **F2-Kontrolle:** k = 44 lief auf beiden Spuren und wurde auf keiner fertig. k = 50 lief nur auf cpu. Es gibt
   keine doppelten Stufendatensaetze, weder in der Kontrolle noch in den Hauptlaeufen.
9. **+-Fortsetzung:** Gradient und Identitaetsrest der +-Loesungen speichert der Code nicht, nur das Flag pm_konv.
   Darum kann ich bei F2 k = 48 nicht sagen, wie knapp das Kriterium verfehlt wurde.
10. Den Entwurf dieses Berichts habe ich vor der Schlussauswertung aus Zwischenauswertung 2 geschrieben. Die
    Hauptdaten F1 und F2 waren da schon vollstaendig. Die Zahlen habe ich gegen die Schlussauswertung geprueft.
11. py_compile auf der .69 hat code/__pycache__/ angelegt (nur auf der .69).

### Laufzeiten (.69, kleintest.sh, CEST; alle rc = 0)

| Aufruf | Spur | Lauf (Lock erhalten bis Ende) | Service-Laufzeit | Inhalt |
|---|---|---|---|---|
| d_s Vicsek | cpu | 11:05:12 bis 11:05:57 | 45 s | Zaehlung g = 5, 7, 8; Irrfahrt g = 7 |
| Rauchtests R2, R3 (3 Aufrufe) | cpu2 | 11:05:22 bis 11:05:27 | 1,5 / 1,9 / 1,6 s | nicht gewertet |
| F1 Haupt 1 | cpu | 11:07:55 bis 11:14:32 | 6 min 36 s | k = 34 bis 72 |
| F1 Haupt 2 | cpu | 11:14:32 bis 11:21:43 | 7 min 11 s | k = 74 bis 78 |
| F2 Haupt 1 | cpu2 | 11:07:55 bis 11:12:24 | 4 min 29 s | k = 14 bis 44 |
| F2 Haupt 2 | cpu2 | 11:12:24 bis 11:21:25 | 9 min 1 s | k = 46, 48; k = 50 ZEITGRENZE |
| Zwischenauswertung 1 | cpu2 | 11:21:25 bis 11:21:32 | 7 s | nicht gewertet |
| F2 k = 54 (Nachtrag 3) | cpu | 11:21:43 bis 11:26:19 | 4 min 36 s | k = 54 |
| F1 Haupt 3 | cpu | 11:26:19 bis 11:26:20 | 0,8 s | nichts mehr offen |
| F1 Kontrolle 1 | cpu | 11:26:20 bis 11:30:11 | 3 min 52 s | g = 9, k = 34 bis 66 |
| F2 Haupt 3 | cpu2 | 11:21:32 bis 11:30:33 | 9 min 1 s | k = 50 ZEITGRENZE |
| F2 3b (Nachtrag 4) | cpu | 11:30:11 bis 11:34:45 | 4 min 34 s | k = 52 |
| F1 Kontrolle 2 | cpu | 11:34:45 bis 11:38:03 | 3 min 17 s | g = 9, k = 70 bis 78 |
| F2 Haupt 4 | cpu2 | 11:30:33 bis 11:39:33 | 9 min 1 s | k = 50 ZEITGRENZE |
| F2 3b k = 50, Bp zuerst (Nachtrag 6) | cpu | 11:38:03 bis 11:47:03 | 9 min 1 s | Bp fertig, Bm ZEITGRENZE |
| F2 3b k = 50 (Nachtrag 5) | cpu2 | 11:39:33 bis 11:46:30 | 6 min 56 s | k = 50 fertig |
| Zwischenauswertung 2 | cpu | 11:47:03 bis 11:47:11 | 7 s | nicht gewertet |
| F2 3b k = 50, Aufruf 2 | cpu | 11:47:11 bis 11:47:12 | 1 s | nichts mehr offen |
| F2 Kontrolle 1 | cpu2 | 11:46:30 bis 11:55:30 | 9 min 0 s | g = 7, k = 14 bis 38; k = 44 ZEITGRENZE |
| F2 Kontrolle oben (Nachtrag 7) | cpu | 11:49:45 bis 11:58:45 | 9 min 1 s | g = 7, k = 50; k = 44 ZEITGRENZE |
| F2 3b k = 50, cpu2 Aufruf 2 | cpu2 | 11:55:30 bis 11:55:31 | unter 1 s | nichts mehr offen |
| Schlussauswertung | cpu | 11:58:45 bis 11:58:52 | 7,0 s | gewertet (aus/auswertung/) |

- Alle Rechenlaeufe endeten um 11:58:45, vor der Plangrenze 12:02.

- Die Zeiten "Lock erhalten" sind aus den Logs abgeleitet (Ende minus Service-Laufzeit, bzw. Ende des Vorgaengers).
  Die Logs liegen in aus/logs/.
- Die Formzustaende und Profile liegen in aus/haupt/ (vom .69-Stand kopiert).

### sha256

Die lokalen Kopien und die .69 stimmen ueberein (geprueft fuer Code, auswertung.json und stufen-vic8.jsonl).

    8815c7ca3ee78af36e85d07c664f30986b0aa8b38aa6ee90bb690d930c5bce54  PLAN.md.eingefroren-20261002-110453
    62cebf69c043705e2e1657848a22d38cff532691d8949455ec359b7ab281a24b  PLAN-NACHTRAG-1.md.eingefroren-20261002-110755
    d2957c6d69dc247371726fe4daae26598e1f899a7ebbce4c01bdbb3ba1a0d38a  PLAN-NACHTRAG-2.md.eingefroren-20261002-111235
    4ed34a8202c5ca59d7accbfc5f85b3260966eefe051e6cf7927744f11a5a25d1  PLAN-NACHTRAG-3.md.eingefroren-20261002-112015
    8d566ba09fadce688bba76cd5bfad31ea56201cb6e00d4de08c5e6c3f94e2e0b  PLAN-NACHTRAG-4.md.eingefroren-20261002-112931
    3e0694538c4b5c5f1afaa418ef114a98cb6620b547ac415123b45a4e3074ad6f  PLAN-NACHTRAG-5.md.eingefroren-20261002-113138
    c9356e5a0e3e98348162474d595112dc0a88585693e4a53193867bcca02f1db8  PLAN-NACHTRAG-6.md.eingefroren-20261002-113610
    329951073d75417c03709682453701df985fe9808dd20d547e525ed872aa49a1  PLAN-NACHTRAG-7.md.eingefroren-20261002-114943
    cb1c840c1a8d099c5f5f4f56d0d1699e8d45f344614996f0696fbd9217b70e45  code/dimbeutel3.py   (alle Aufrufe ausser 3b)
    0eb94851680e39b5642b0c582ee7dcfe72cf112545b88ea2b81cd41e4bbbb2b6  code/dimbeutel3b.py  (F2 k = 50, 52)
    d368c3a1838e29e012a38a4dc8c76e5d86201157107c21e872d80be76875ed9c  code/auswertung2.py  (Schlussauswertung)
    1b06d3f057d1fd14a72145e0cdd1e5c1903572616737a8774a28f3bfd05def92  aus/auswertung/auswertung.json
    9ab5843cae3db5a72dd55bfc015386a7d82e0de9a151009a925474f36c96bfd9  aus/auswertung/abb1-p.png
    ec9f2ceb834d9d4af39005a9c9a2ddb6a5397db8bbf8ef13e195aa94e2ae3631  aus/auswertung/abb2-profile.png
    8a6b842e259d5aa4070f7e22d72fc9106651f55e2bfa8341a925dd6f55f662cc  aus/auswertung/abb3-ds.png
    e2fad9e3103bf2988232af983cdc72ca46e2cf0d7879bb8aacfc1d771f5eefe6  aus/auswertung/abb4-E.png
    066861a2b91c67ae38e3c073246320cefb333e4e18627fdf9008e1065f08bb05  aus/auswertung/stufen-F1.csv
    dbffc97dd54c50b509fd5c1837731137cb8f251f7d484843a3b1328b5095ffe0  aus/auswertung/stufen-F2.csv
    c05d85882fec339328f6de40d82f43490813a7399be3c7c254a5de1a783782bf  aus/haupt/stufen-sie10.jsonl
    3aa4a2036456e414d4521c456d548148aa8af571ca392292fd3ca44df116db7d  aus/haupt/stufen-vic8.jsonl
    d3c89016239c25492eceec8fa9033b663bcf790b8b51237bd6bed21d8085bf04  aus/kontrolle/stufen-sie9v.jsonl
    d340dc8e60928f6bb7e0706211aae6f50dce0e615991f7906cbb92c904e06707  aus/kontrolle/stufen-vic7v.jsonl
    a53867e53b97e1a95aab773666c31f3223889068365c43b76985c6870d046851  aus/ds/ds-vicsek.json

- Die vollstaendige Liste steht auch in hilfs/sha256-final.txt.

## 6. Einfach gesagt

Wir haben ausgerechnet, wie viel Energie ein "Beutel" braucht, der eine bestimmte Menge Wellen auf zwei Fraktalen
einsperrt: dem Sierpinski-Dreieck und dem Vicsek-Kreuz. Die Frage war, ob das Wachstum dieser Energie die
"geometrische" Dimension zeigt, also wie viel Platz das Fraktal fuellt, oder die "spektrale", also wie sich Wellen
darauf ausbreiten. Auf beiden Fraktalen kam die spektrale heraus: 0,583 statt 0,577 beim Dreieck und 0,550 statt
0,543 beim Kreuz; die geometrischen Werte waeren 0,613 und 0,594 gewesen. Man muss dafuer aber ueber eine ganze
"Selbstaehnlichkeits-Stufe" mitteln, denn dazwischen schwankt der Wert stark. Der Beutel ist also ein Messgeraet
dafuer, wie sich Wellen auf einem Netz ausbreiten, nicht dafuer, wie gross es aussieht.
