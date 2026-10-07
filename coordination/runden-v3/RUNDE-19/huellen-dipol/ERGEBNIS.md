# ERGEBNIS HUELLEN-DIPOL (Runde 19)

- Code-Agent. Eigener Code: code/dipol.py (l = 1, Kette, D4), code/auswertung_dipol.py (Wertung, Bilder). Unveraendert
  importiert: code/stille3.py (Code 1), code/beutel.py, code/huellen_leiter.py (HUELLEN-LEITER), code/auswertung.py
  (Runde-18-Auswertung, nur Hilfsfunktionen).
- Start 2026-10-02 15:41:30 CEST. Plan eingefroren 15:57:15 (PLAN.md.eingefroren-20261002-155715), vor dem ersten
  .69-Lauf (13:57:20 UTC = 15:57:20 CEST). Kein Nachtrag. Bericht: Geruest ab 16:08:50, Ergebnisteile ab 16:15:59 CEST
  (date, jeweils letzte Messung vor dem Schreiben). Uhrzeiten der .69 in UTC (CEST = UTC + 2).
- Explorativ (v3). Alles modellintern (M2, linear, klassisch), keine Messdaten. Deutungen sind Hypothesen [H].

## 1 Ergebnis zuerst

1. **Die Huelle traegt auch Dipol-Leitern (D1 und D2 eingetroffen).**
   - Im Kartenfenster omega^2 = 1,40 bis 0,80 (Huellenradius R = 1,8 bis 19,4) liegen 19 stille Dipol-Stellen (l = 1)
     auf 5 chi-Kurven (k = 0 bis 4).
   - Alle 19 sind auf beiden Gitterstufen gleich (omega^2 auf <= 1,1e-8, rho auf <= 6,0e-9) und haben dort denselben
     Zellen-Umlauf +-1. An allen 19 ist zusaetzlich der aufgeloeste Rechteck-Umlauf auf beiden Stufen gerechnet; er
     stimmt ueberall mit dem Zellen-Umlauf ueberein. Laengs jeder Kurve wechselt der Umlauf von Stelle zu Stelle.
   - Auf den Kurven k = 0, 1, 2 folgen die Stellen in fast festem Abstand in R: 2,49 / 2,26 / 2,37 im Mittel,
     Variationskoeffizient 3,6 / 3,7 / 3,9 %.
   - Vorab festgelegte Bedeutung (Karte): **Die Huelle traegt auch Dipol-Leitern. Der Mechanismus ist nicht an l = 0
     gebunden [H].**
2. **Gleiche Sprossenregel wie bei l = 0 (D3 eingetroffen).**
   - Je Kurve ist der mittlere Abstand bei l = 1 nur 1,7 bis 2,9 % groesser als bei l = 0 auf der Kurve gleichen
     Rangs im selben R-Bereich (q = 1,017; 1,027; 1,029; Grenze +-15 %).
   - Nach der Karte prueft D3, ob die Sprossenregel (halbe Innenwellenlaenge) fuer beide l dieselbe ist; im Fenster
     ist sie es [H].
   - Nicht vorhergesagt, nur beobachtet: Auf der Wandkurve k = 0 liegen die l = 1-Stellen bei um 0,9 bis 1,1
     groesserem R als die l = 0-Stellen (0,34 bis 0,47 Abstaende). Die chi-Kurven entstehen bei l = 1 etwa 1,6 bis 2,1
     in R spaeter.
3. **K1 bestanden (D0 eingetroffen).**
   - Die bewiesene M1-Dipolstelle (BEWEIS-2, Satz T2) ist die einzige K1-Stelle.
   - Getroffen auf 3,3e-8 (Stufe 1) bzw. 5,0e-9 (Stufe 2), Rechteck-Umlauf -1 aufgeloest auf beiden Stufen.
   - Selbsttest: Mit l = 0 rechnen die neuen Kanalfunktionen bitgleich wie Code 1.
4. **D4 offen.**
   - Die Verfolgung der M1-Dipolstelle beim Einschalten der chi-Kopplung (lam = 0 bis 1, wie STILLE-ZWEIFELD) brach
     bei lam = 0,20 ab: Das Profil-Newton scheiterte, auch mit 8 Teilschritten.
   - Bis lam = 0,15 blieb der verfolgte Punkt in E2 (rho >= 1,55 > sqrt2) und war schon ab lam = 0,05 keine stille
     Stelle mehr: T = 1,8e-14 bei lam = 0, dann 0,036; 0,20; 0,92.
   - Nach der Plan-Regel heisst ein Abbruch vor lam = 1 "offen". Der Abbruch liegt an der Profilfortsetzung, nicht an
     der Messgroesse.
5. **Grenzen:**
   - Das Fenster reicht nur bis R = 19,4; je Kurve gibt es 7, 5, 4, 2 und 1 Stellen. D2 und D3 stuetzen sich auf die
     Kurven k = 0 bis 2 (6, 4 und 3 Abstaende).
   - Linear, klassisch, Modell M2, ein Drehimpuls; keine Zeitbereichspruefung der Dipol-Stellen.

## 2 Vorhersagen D0 bis D4

Gewertet nach PLAN Abschnitt 8 und 9 auf dem ganzen Fenster: Zeilen 0 bis 71, Paare 0 bis 70, omega^2 = 1,40 bis 0,80,
R = 1,77 bis 19,41, beide Stufen vollstaendig.

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| D0 | K1 bestanden, bewiesene M1-Dipolstelle auf 1e-6 (90 %) | **eingetroffen** | Stufe 1: Newton 0,7544960434 / 1,8263420627, Abstand zu BEWEIS-2 3,0e-8 / 3,3e-8; Stufe 2: 0,7544960184 / 1,8263420352, Abstand 4,6e-9 / 5,0e-9. Rechteck-Umlauf -1 aufgeloest auf beiden Stufen (groesster Sprung 0,325 rad, 68 Randpunkte), Zellen-Umlauf -1. Einzige K1-Stelle |
| D1 | In E1 stille Dipol-Stellen, mindestens 5 im Fenster (75 %) | **eingetroffen** | 19 Stellen im Fenster 0,80 bis 1,40, alle auf beiden Stufen, keine nur auf einer Stufe, keine mit Merker |
| D2 | Stellen auf chi-Kurven mit fast festem Abstand in R, Streuung < 15 % (60 %) | **eingetroffen** | Kurven mit >= 4 Stellen: k = 0 (7 Stellen): Mittel 2,489, CV 0,036; k = 1 (5): 2,262, CV 0,037; k = 2 (4): 2,366, CV 0,039 |
| D3 | Abstand innerhalb +-15 % des l = 0-Abstands bei gleichem R (50 %) | **eingetroffen** | q = Abstand l = 1 / l = 0 (gleicher Rang, Paarmitten im R-Bereich): k = 0: 2,489 / 2,448 = 1,017; k = 1: 2,262 / 2,203 = 1,027; k = 2: 2,366 / 2,300 = 1,029 |
| D4 | Die M1-Dipolstelle hat in M2 keinen Nachfolger mit nur einem offenen Kanal (75 %) | **offen** | Homotopie lam = 0 bis 1 (cpot 0,25, Stufe 1) brach bei lam = 0,20 ab (Profil-Newton gescheitert). Bis dahin nur E2: lam = 0: T = 1,8e-14; 0,05: T = 0,036; 0,10: 0,199; 0,15: 0,924 (Gauss-Newton dort nicht konvergiert). Kein Schritt in E1, kein E1-Versuch an der Klemme |

- Nach der Karte gilt damit die Bedeutung "D1 und D2 eingetroffen" (Abschnitt 1, Punkt 1), eingeschraenkt auf R <= 19,4.
- Zur Streuung (D2): Wie bei l = 0 ist der erste Abstand nach der Geburt einer Kurve der groesste (k = 0: 2,66, dann
  2,51 / 2,46 / 2,44 / 2,43 / 2,43); danach fallen die Abstaende langsam und flachen ab.

## 3 Liste aller Dipol-Stellen (19)

- Sortiert nach fallendem omega^2. Lage aus Unterzeilen und Halbierung (Stufe 1); Differenzen Stufe 2 minus Stufe 1.
  R = Huellenradius (chi = 1/2). Knoten: Zahl der Vorzeichenwechsel der c-Komponente von Y_c auf (0, r_m] an den
  beiden Klammerenden (Stufe 1, nur Gegenprobe).
- Rechteck: aufgeloester Rechteck-Umlauf (Newton und Rechteck von Code 1 ab der eigenen Lage) Stufe 1 / Stufe 2.
  Stichprobe nach PLAN 7: Nr. 15 bis 19 (je Kurve die Stelle mit kleinstem omega^2); die uebrigen 14 nach PLAN 7
  ("reicht die Zeit") ebenfalls.

| Nr | k | omega^2 | rho | R | d omega^2 (1e-9) | d rho (1e-9) | d R (1e-6) | Zellen-Umlauf St1 / St2 | Knoten | Rechteck St1 / St2 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1,07305911 | 1,20578177 | 4,085 | -10,39 | -5,98 | 1,16 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 2 | 0 | 0,93895155 | 1,12354106 | 6,745 | -2,64 | -1,25 | 0,34 | +1 / +1 | 0,0 | +1 / +1 aufgeloest |
| 3 | 1 | 0,88598265 | 1,34495564 | 8,976 | -1,34 | -1,59 | 0,5 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 4 | 0 | 0,88115621 | 1,09051434 | 9,254 | -1,08 | -0,34 | 0,17 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 5 | 1 | 0,85237881 | 1,2968371 | 11,351 | -0,53 | -0,64 | 0,45 | +1 / +1 | 0,0 | +1 / +1 aufgeloest |
| 6 | 0 | 0,84842071 | 1,07246073 | 11,717 | -0,53 | -0,04 | 0,29 | +1 / +1 | 0,0 | +1 / +1 aufgeloest |
| 7 | 2 | 0,84278249 | 1,37301725 | 12,281 | -0,2 | -0,08 | 0,2 | +1 / +1 | 2,2 | +1 / +1 aufgeloest |
| 8 | 1 | 0,83127536 | 1,2674133 | 13,622 | -0,21 | -0,23 | 0,24 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 9 | 0 | 0,82726837 | 1,06098252 | 14,161 | -0,27 | 0,1 | 0,28 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 10 | 2 | 0,82325701 | 1,32678174 | 14,745 | -0,00 | 0,2 | 0,11 | -1 / -1 | 2,2 | -1 / -1 aufgeloest |
| 11 | 3 | 0,81803176 | 1,39073742 | 15,584 | 0,24 | 1,08 | 0,11 | -1 / -1 | 2,2 | -1 / -1 aufgeloest |
| 12 | 1 | 0,81655947 | 1,24807569 | 15,839 | -0,06 | -0,05 | 0,29 | +1 / +1 | 0,0 | +1 / +1 aufgeloest |
| 13 | 0 | 0,81245674 | 1,05301021 | 16,593 | -0,14 | 0,16 | 0,38 | +1 / +1 | 0,0 | +1 / +1 aufgeloest |
| 14 | 2 | 0,80993867 | 1,29479774 | 17,094 | 0,08 | 0,3 | 0,38 | +1 / +1 | 2,2 | +1 / +1 aufgeloest |
| 15 | 1 | 0,80563459 | 1,23457054 | 18,024 | 0,02 | 0,04 | 0,4 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 16 | 3 | 0,80530422 | 1,34892895 | 18,1 | 0,24 | 1,07 | 0,13 | +1 / +1 | 2,2 | +1 / +1 aufgeloest |
| 17 | 4 | 0,80201832 | 1,40277741 | 18,889 | 0,43 | 1,84 | 0,22 | +1 / +1 | 2,2 | +1 / +1 aufgeloest |
| 18 | 0 | 0,80150043 | 1,04713972 | 19,02 | -0,07 | 0,2 | 0,18 | -1 / -1 | 0,0 | -1 / -1 aufgeloest |
| 19 | 2 | 0,80011893 | 1,27213868 | 19,378 | 0,12 | 0,33 | 0,27 | -1 / -1 | 2,2 | -1 / -1 aufgeloest |

## 4 Abstaende in R: Vergleich mit l = 0 je Kurve

- l = 0: Lagen je Kurve aus RUNDE-18-ERGEBNIS Abschnitt 4 (Stufe 1, zwei Nachkommastellen), gleicher Rang k.
  Vergleichsabstaende: die l = 0-Abstaende, deren Paarmitte im R-Bereich der l = 1-Stellen der Kurve liegt (PLAN 8).

| k | l = 1: Lagen R | l = 1: Abstaende | Mittel (CV) | l = 0: Lagen R im Bereich | l = 0: Vergleichsabstaende | Mittel | q = l1/l0 |
|---|---|---|---|---|---|---|---|
| 0 | 4,09 6,75 9,25 11,72 14,16 16,59 19,02 | 2,660 2,509 2,463 2,443 2,433 2,426 | 2,489 (0,036) | 3,21 5,76 8,21 10,64 13,06 15,48 17,90 | 2,55 2,45 2,43 2,42 2,42 2,42 | 2,448 | 1,017 |
| 1 | 8,98 11,35 13,62 15,84 18,02 | 2,376 2,270 2,217 2,186 | 2,262 (0,037) | 8,40 10,68 12,89 15,06 17,21 | 2,28 2,21 2,17 2,15 | 2,203 | 1,027 |
| 2 | 12,28 14,75 17,09 19,38 | 2,464 2,349 2,284 | 2,366 (0,039) | 11,81 14,19 16,47 18,71 | 2,38 2,28 2,24 | 2,300 | 1,029 |
| 3 | 15,58 18,10 | 2,516 | - | 15,16 17,60 | (2,44) | - | nicht gewertet (2 Stellen) |
| 4 | 18,89 | - | - | 18,49 | - | - | nicht gewertet (1 Stelle) |

- Die Abstaende beider l verhalten sich im Fenster gleich: groesster Abstand direkt nach der Geburt der Kurve, dann
  langsamer Abfall (Abbildung abb-abstand.png).
- **Lage gegeneinander (nur beobachtet):** Auf k = 0 liegen die l = 1-Stellen um 0,88; 0,99; 1,04; 1,08; 1,10; 1,11;
  1,12 oberhalb der jeweils naechstkleineren l = 0-Stelle (in R), das sind 0,34 bis 0,47 des folgenden l = 0-Abstands,
  mit R steigend.
  - Lesart [H, nicht gerechnet]: Die offene Teilwelle l hat im Inneren die Phase k_innen r - l pi/2. Fuer l = 1
    verschiebt das die Vorzeichenwechsel der Kopplung um eine halbe Sprosse. Gleicher Abstand bei verschobener Lage
    passt zu diesem Bild.
- **Geburt der Kurven** (erste Zeile mit k + 1 Nullstellen von m_bc, rho ~ 1,41): l = 1: k = 1 bei R = 6,71; 2: 10,36;
  3: 14,56; 4: 18,17 (Abstand 3,65 / 4,20 / 3,61). l = 0 (Runde 18): 4,7; 8,76; 12,47; 16,11. Lesart [H]: Die inneren
  chi-Zustaende l = 1 brauchen k R ~ 4,49; 7,73; ... (Nullstellen von j_1) statt n pi, also etwas mehr Platz.

## 5 Kontrollen, Grenzen, Selbstanzeigen, Laufzeiten, sha256

### K1 (bewiesene M1-Dipolstelle, Modell K1E1 von Code 1, l = 1)

- Dieselbe Kette wie die Suche: Zeilen omega^2 = 0,77; 0,76; 0,75; 0,74; 0,73 (ganze E1-Zeile, 201 Punkte), Rang,
  Unterzeilen, zwei Halbierungen, dann Newton und Rechteck von Code 1 (Abklingstart bei R_bg).
- In jeder Zeile genau eine Nullstelle der geschlossenen Bedingung (rho = 1,7987 bei 0,73 bis 1,8434 bei 0,77), s dort
  (Stufe 2): +0,0245 (0,77), +0,0108 (0,76), -0,0116 (0,75), -0,0494 (0,74), -0,1078 (0,73). Genau ein
  Vorzeichenwechsel, Zellen-Umlauf -1, Knotenzahl 0. Keine weitere K1-Stelle.
- Referenz BEWEIS-2: 0,75449601378 / 1,82634203018. Kartenwerte 0,7544960184 / 1,8263420673.

| Stufe | Lage aus Halbierung | Lage nach Newton | Abstand zu BEWEIS-2 | Abstand zur Karte | Rechteck-Umlauf | groesster Sprung | Randpunkte | sigma2/sigma1 |
|---|---|---|---|---|---|---|---|---|
| 1 (hp 0,01) | 0,75449598 / 1,82634198 | 0,7544960434 / 1,8263420627 | 3,0e-8 / 3,3e-8 | 2,5e-8 / -4,6e-9 | -1 aufgeloest | 0,325 rad | 68 | 1,8e-13 |
| 2 (hp 0,005) | 0,75449596 / 1,82634195 | 0,7544960184 / 1,8263420352 | 4,6e-9 / 5,0e-9 | -4,2e-11 / -3,2e-8 | -1 aufgeloest | 0,325 rad | 68 | 7,6e-14 |

- **K1 bestanden** (Abschnitt 4 des Plans: 1e-6, Umlauf aufgeloest, gleich auf beiden Stufen). Der Abstand zur
  bewiesenen Stelle faellt von Stufe 1 auf Stufe 2 in omega^2 und rho je um den Faktor 6,5 (Diskretisierungsfehler,
  der mit der Gitterweite faellt).
- **Selbsttest l = 0** (beide K1-Laeufe, 5 Punkte bei omega^2 = 0,75): Ersatzfunktionen gegen Code 1 und HUELLEN-LEITER:
  max |Differenz| = 0 in m_ac, m_bc, m_ab, regulaerer und abklingender Basis; Knotenzahlen gleich. Die l-Fassung
  aendert also nur, was l(l + 1)/r^2, den Ursprungsstart und den Abklingstart betrifft.

### Triviale Moden

- Translation und Boost-Partner liegen bei rho = 0. Abgetastet wurde rho >= sqrt2 - w + 1e-4 >= 0,2311 (Suche) bzw.
  >= 0,1226 (K1). Kleinstes rho einer Stelle: 1,0471 (Nr. 18). Keine Stelle liegt in der Naehe von rho = 0.

### Rechteck-Umlauf gegen Zellen-Umlauf (PLAN 7), beide Stufen

- Je Kurve k = 0 bis 3 die Stelle mit kleinstem omega^2, dazu k = 4. Halbbreite 1e-3 an allen fuenf Stellen.

| Stelle (Nr) | k | omega^2 / rho (Newton, St1) | R | Newton - Halbierung (omega^2 / rho, St1) | Zellen-Umlauf St1 / St2 | Rechteck-Umlauf St1 / St2 | groesster Sprung | Randpunkte | sigma2/sigma1 St1 / St2 | d omega^2 Newton St1 - St2 |
|---|---|---|---|---|---|---|---|---|---|---|
| 18 | 0 | 0,8015004763 / 1,0471397458 | 19,02 | 4,6e-8 / 2,6e-8 | -1 / -1 | -1 / -1 aufgeloest | 0,328 | 82 | 7,2e-12 / 7,7e-12 | 6,5e-11 |
| 15 | 1 | 0,8056345934 / 1,2345705336 | 18,02 | -1,1e-9 / -2,7e-9 | -1 / -1 | -1 / -1 aufgeloest | 0,394 | 69 | 1,6e-11 / 7,0e-12 | -2,3e-11 |
| 19 | 2 | 0,8001188675 / 1,2721385303 | 19,38 | -6,0e-8 / -1,5e-7 | -1 / -1 | -1 / -1 aufgeloest | 0,400 | 71 | 6,0e-12 / 2,5e-11 | -1,2e-10 |
| 16 | 3 | 0,8053041379 / 1,3489286584 | 18,10 | -8,7e-8 / -2,9e-7 | +1 / +1 | +1 / +1 aufgeloest | 0,353 | 74 | 6,5e-12 / 1,7e-11 | -2,4e-10 |
| 17 | 4 | 0,8020183023 / 1,4027775011 | 18,89 | -1,9e-8 / 8,6e-8 | +1 / +1 | +1 / +1 aufgeloest | 0,366 | 74 | 3,3e-12 / 1,5e-12 | -4,3e-10 |

- **Zellen-Umlauf = Rechteck-Umlauf in 5 von 5 Proben auf beiden Stufen**, alle im ersten Versuch aufgeloest, echter
  Rangabfall (sigma2/sigma1 <= 2,5e-11). Damit gilt die Zaehlung mit dem Zellen-Umlauf.
- **Die uebrigen 14 Stellen** (PLAN 7, "reicht die Zeit"), beide Stufen, Halbbreite 1e-3: alle im ersten Versuch
  aufgeloest, Rechteck-Umlauf = Zellen-Umlauf in 14 von 14 (Einzelwerte in Abschnitt 3). Ueber alle 19 Stellen und beide
  Stufen: groesster Sprung 0,281 bis 0,400 rad, 64 bis 82 Randpunkte, sigma2/sigma1 <= 2,5e-11, Newton-Lage gegen
  Halbierungslage <= 2,1e-7 (omega^2) bzw. <= 5,6e-7 (rho).

### Zwei Gitterstufen

- Alle 72 Zeilen: auf beiden Stufen gleiche Zahl, gleiche Vorzeichenfolge und gleiche Lage (<= 1,1e-8) der Nullstellen
  von m_bc. Keine unsichere Nullstelle, kein Illinois-Fall, keine Abnahme der Nullstellenzahl zur Schranke hin.
- Alle 19 Stellen auf beiden Stufen im selben Zeilenpaar auf derselben Kurve, Lage auf 1,04e-8 (omega^2), 6,0e-9 (rho),
  1,2e-6 (R); Zellen-Umlauf 19 von 19 gleich. Keine Stelle nur auf einer Stufe, keine gepaarte Stelle mit Merker.
- Merker: Rangsprung nach Plan-Regel 0.
  - Der Code-Merker (mit Schwellenabstand, Runde-18-Nachtrag 1) steht 9-mal je Stufe, immer an der juengsten Kurve in
    ihren ersten Paaren (k = 1: Paare 46, 47; k = 2: 54 bis 56; k = 3: 62, 63; k = 4: 69, 70; Luecke 0,0016 bis 0,022).
    Er zaehlt nach dem Plan nicht.
  - Zwei Stellen liegen in solchen Paaren: Nr. 11 (k = 3, Paar 63) und Nr. 17 (k = 4, Paar 70). Beide haben auf beiden
    Stufen den aufgeloesten Rechteck-Umlauf gleich dem Zellen-Umlauf.
  - In Paar 54 (Geburtszeile von k = 2, Luecke 0,0016) sind auf beiden Stufen zwei Unterzeilen (t = 4/8, 5/8) der
    Kurve k = 2 verworfen; dort gibt es keinen Wechsel.
- Knotenzahl der c-Komponente als Gegenprobe: 0, 0, 2, 2, 2 fuer k = 0 bis 4, an jeder Stelle gleich an beiden
  Klammerenden. Monoton im Rang, aber nicht eindeutig (wie bei l = 0); als Index ungeeignet, der Rang reicht.

### Hintergrund

- Profile wie Runde 18 (gleiche Zeilen ab 1,40, letzte Zeile 0,80): Stufe 1 und 2 in 2,1 s bzw. 3,4 s, Newton in 1 bis
  5 Iterationen je Zeile, alle 72 Zeilen auf beiden Stufen.
- Stufenvergleich der Profile (jq auf profile-info.json, .69): |dQ/Q| <= 6,2e-11, |dE/E| <= 6,3e-11, Huellenradius R
  auf 3,5e-6 gleich, Rand |f(R_bg)|/f(0) <= 6,8e-17. Bei 0,80: R = 19,41, chi(0) = 2,3e-9 (Rundung unkritisch; Runde-18-Grenze R ~ 39).

### D4 (Homotopie, PLAN 9, nur Stufe 1)

- Verfahren nach PLAN 9: Modell(lam, cpot = 0,25), Start an der K1-Newton-Lage (Stufe 1), festes Gebiet R_bg = 106,3
  (N = 10630, hp = 0,01), Abgleich r_m = 3,44. Rundungsschutz (Kopplung 0, wo |chi| < 1e-12) war nie aktiv (chi(0) >=
  0,82).

| lam | Bereich | omega^2 | rho | T = abs(G) | G (Zeilen a, b, c) | Gauss-Newton | r_half | chi(0) | Sekunden |
|---|---|---|---|---|---|---|---|---|---|
| 0 | E2 | 0,7544960 | 1,8263421 | 1,8e-14 | 1,6e-14; 8,9e-15; 0 | 1 Schritt | 3,45 | 1,000 | 7,1 |
| 0,05 | E2 | 0,7172760 | 1,7842567 | 0,0356 | 0,0143; -0,0016; 0,0325 | 9, Ende ohne Abstieg | 4,93 | 0,945 | 40,4 |
| 0,10 | E2 | 0,7162044 | 1,7894623 | 0,199 | 0,0769; 0,0104; 0,1835 | 7 | 6,50 | 0,883 | 33,3 |
| 0,15 | E2 | 0,7204025 | 1,5506470 | 0,924 | -0,0009; -0,9240; -0,0013 | 25 (Hoechstzahl, letzter Schritt 0,01) | 8,71 | 0,818 | 76,4 |
| 0,20 | - | - | - | - | - | Profil bei omega^2 = 0,72040 gescheitert (8 Teilschritte) | - | - | - |

- Der Fortsetzungsaufruf (gleiches Verfahren, ab dem gespeicherten Zustand bei lam = 0,15) scheiterte an derselben
  Stelle. Ausgang nach PLAN 9: **offen**.
- Was die Spur trotzdem zeigt [H]: Schon bei lam = 0,05 ist der Punkt keine stille Stelle mehr (T = 0,036 gegen
  1,8e-14 bei lam = 0), und T waechst mit lam. In E1 kam die Spur bis lam = 0,15 nicht (rho >= 1,55). Ob ein E1-
  Nachfolger bei groesserem lam entsteht, ist offen.
- Schreibtisch-Abschaetzung (nicht gerechnet): Bei cpot = 0,25 steigt die Duennwand-Grenze des Q-Balls mit lam (etwa
  0,66 bei lam = 0,2; 0,706 bei 0,3; 0,727 bei 0,4). Eine Spur bei omega^2 ~ 0,72 verliesse deshalb um lam ~ 0,35 ohnehin
  den Existenzbereich. Fuer eine Folgerunde: Profilfortsetzung in lam mit Halbierung und Praediktor, Klemme an der
  Duennwand-Grenze.

### Grenzen

- **Fenster:** nur omega^2 = 0,80 bis 1,40 (R <= 19,4), wie Karte. Wenige Stellen je Kurve; D2 und D3 beruhen auf drei
  Kurven mit 6, 4 und 3 Abstaenden.
- **D3-Vergleich:** l = 0-Lagen nur mit zwei Nachkommastellen aus dem Runde-18-Bericht; Rundung 0,005 je Lage, auf die
  Mittel <= 0,0034 (0,15 %). Die Abschrift (hilfs/l0-kurven.json) ist fuer k = 0 bis 3 mit sed/diff gegen den
  Berichtstext geprueft und gleich. Gleicher Rang heisst nicht gleicher chi-Zustand: Die Kurve k der l = 1-Leiter ist
  ein l = 1-Zustand, die Kurve k der l = 0-Leiter ein l = 0-Zustand. Der im Plan nur "falls Zeit" genannte Vergleich mit
  der l = 0-Kurve naechsten rhos ist nicht gemacht.
- **Zaehlung mit Zellen-Umlauf** (wie Runde 18). Der Rechteck-Umlauf ist an allen 19 Stellen auf beiden Stufen
  gerechnet und ueberall gleich; die Zaehlung haengt damit nicht an dieser Abkuerzung.
- **Doppelwechsel innerhalb einer Unterzeile** (1/8 Zeilenabstand) waeren nicht gesehen; kleinster Abstand zweier
  Stellen einer Kurve 2,19 in R.
- **Schwellen:** je 1e-4 an rho = sqrt2 - w und an rho = sqrt2 nicht abgetastet (wie Runde 18).
- **Ursprungsstart l = 1:** Reihe bis r^4 bei r0 = 2 hp. Der K1-Abstand (3e-8 auf Stufe 1, 5e-9 auf Stufe 2) und die
  Stufengleichheit der Stellen (1e-8) zeigen, dass der Startfehler die Lagen nicht merklich verschiebt.
- **Reichweite:** linear, klassisch, Modell M2, ein Drehimpuls (l = 1, je m gleich). Keine Zeitbereichspruefung der
  Dipol-Stellen.

### Selbstanzeigen

- **Lesen ausserhalb der Freigabe:**
  - BEWEIS-2.md ganz gelesen (frei war es nur fuer die Lage der Dipolstelle und die Kanalkonvention l = 1). Benutzt habe
    ich nur diese Angaben: Satz T2 (Lage, Kasten), das Kanalsystem mit 2/r^2, A, B = O(r^2), J_0, und den Satz, dass
    die Translationsmode bei rho = 0 liegt.
  - Ordnerlisten, nur Namen: RUNDE-10/beweis2/ (dazu Zeilenzahl von BEWEIS-2.md) und RUNDE-18/huellen-leiter/ (zeigte
    auch aus/ und hilfs/; nicht geoeffnet). Nichts aus Sperrbereichen. kleintest.sh nicht gelesen.
- **.69:** einmal `nproc; uptime` (Lastanzeige, keine Rechnung). Nur der eigene Ordner angelegt und gelistet. Die
  Ausgaben der Laeufe kamen per ssh in den lokalen Ordner aus/logs/. Der erste Aufruf (py_compile, 13:57:20 UTC) ist dort
  nicht gespeichert; seine Ausgabe (4-mal "py_compile ok", rc 0, 0,1 s) steht nur in der Sitzung.
- **Lokal ausserhalb der Befehlsliste:** chmod (Einfrieren), wc -l (Zaehlen), sleep in Warteschleifen, bash-Schleifen,
  eine lokale Ueberwachung (tail -F mit grep auf aus/logs/kette.txt), die ich am Ende selbst gestoppt habe. Kein python,
  awk oder bc lokal.
- **Laufzeitersatz statt Kopie:** dipol.py ersetzt beim Import HL.werte_k, S3.regulaer und S3.abklingend durch die
  l-Fassungen, im D4-Lauf zusaetzlich S3.Pot durch eine Unterklasse mit dem Rundungsschutz aus PLAN 9. Die importierten
  Dateien selbst sind unveraendert (sha256 wie Runde 18).
- **Code nach dem Einfrieren geaendert**, Verfahren gleich:
  - code/dipol.py 5a9e50ac... (V0 bis V2: Syntax, Liste, K1, Profile, Bloecke) wurde zu 0094476d... (ab V3: Rechtecke,
    D4). Geaendert ist nur der D4-Teil: Fehlerfang je Schritt (Abbruch mit Grund statt Programmende), Schritt als
    eigene Funktion, Ausgabe n_schnitt. Die Aenderung lag vor dem ersten D4-Lauf.
  - code/auswertung_dipol.py nach dem Einfrieren geschrieben (setzt PLAN 5 bis 9 um), seit dem ersten Lauf
    unveraendert.
- **D4-Fortsetzung:** Der Aufruf r19-d4-w stand vorab in der Kette (fuer die 600-s-Grenze). Nach dem Abbruch
  wiederholte er denselben Schritt mit demselben Verfahren und scheiterte gleich. Danach keine weitere D4-Rechnung.
- Nichts in den Scratchpad geschrieben; die Ausgaben der Hintergrund-Befehle legt das Werkzeug selbst unter
  /tmp/claude-1000/.../tasks ab. Kein git, kein Peerbus, keine Unteragenten, keine Literatur.

### Laufzeiten (.69, kleintest.sh, Spur cpu6, nacheinander; Service runtime; UTC)

| Lauf | Zweck | Start | Ende | Dauer | rc |
|---|---|---|---|---|---|
| r19-pruef | py_compile (V0) | 13:57:20 | 13:57:20 | 0,1 s | 0 |
| r19-liste | Zeilenliste (72 Zeilen) | 13:57:36 | 13:57:36 | 0,4 s | 0 |
| r19-k1-st1 | K1 Stufe 1 mit Selbsttest | 13:57:36 | 13:58:13 | 36,3 s | 0 |
| r19-prof-st1 | Profile Stufe 1 | 13:58:13 | 13:58:15 | 2,1 s | 0 |
| r19-k1-st2 | K1 Stufe 2 mit Selbsttest | 13:58:15 | 13:59:26 | 71,1 s | 0 |
| r19-prof-st2 | Profile Stufe 2 | 13:59:26 | 13:59:30 | 3,4 s | 0 |
| r19-b1-0-71 | Block Stufe 1, Zeilen 0 bis 71 | 13:59:58 | 14:04:40 | 281,8 s | 0 |
| r19-b2-0-40 | Block Stufe 2, Zeilen 0 bis 40 | 14:04:40 | 14:08:45 | 245,5 s | 0 |
| r19-b2-40-71 | Block Stufe 2, Zeilen 40 bis 71 | 14:08:45 | 14:13:21 | 275,7 s | 0 |
| r19-b1-0-71-w, r19-b2-0-40-w, r19-b2-40-71-w | Fortsetzung, nichts zu tun | 14:13:21 | 14:13:25 | 0,5 / 3,2 / 0,5 s | 0 |
| r19-pruef2 | py_compile (V3) | 14:13:33 | 14:13:33 | 0,1 s | 0 |
| r19-stellen | Auswertung | 14:13:33 | 14:13:37 | 4,1 s | 0 |
| r19-uP1 / r19-uP2 | Rechteck-Stichprobe Stufe 1 / 2 | 14:13:37 / 14:14:16 | 14:14:16 / 14:15:31 | 39,1 / 74,4 s | 0 |
| r19-d4 | D4-Homotopie | 14:15:31 | 14:18:11 | 159,8 s | 0 (Abbruch im Verfahren bei lam = 0,20) |
| r19-d4-w | D4-Fortsetzung | 14:18:11 | 14:18:12 | 1,4 s | 0 (gleicher Abbruch) |
| r19-final | Endauswertung | 14:18:12 | 14:18:13 | 0,6 s | 0 |
| r19-bild | Abbildungen | 14:18:13 | 14:18:15 | 1,9 s | 0 |
| r19-uA1 / r19-uA2 | Rechteck uebrige 14 Stellen, Stufe 1 / 2 | 14:18:15 / 14:19:37 | 14:19:37 / 14:22:14 | 81,7 / 157,1 s | 0 |
| r19-final2 | Endauswertung mit allen Rechtecken | 14:22:14 | 14:22:14 | 0,5 s | 0 |

- Zusammen 1441 s (24 min) Spurzeit auf cpu6, jeder Aufruf unter der 600-s-Grenze (laengster 281,8 s).
- Abbildungen (aus/, Stufe 2 fuer die Kurven):
  - abb-stellen.png: Nullstellen von m_bc in (omega^2, rho), Farbe = Kurve k; Stellen als Dreiecke (auf: +1, ab: -1).
  - abb-abstand.png: Abstand Delta R gegen R (Paarmitte) je Kurve, l = 1 (Kreise) und l = 0 aus Runde 18 (Kreuze).
    Ablesbar: Die l = 1-Kurven laufen wie die l = 0-Kurven, etwas nach rechts versetzt.

### sha256

Code (lokal = .69, verglichen):

```
0094476d6b88a37bbbd96d411f823ab335ef78ba13c710b7f5cab81774dc0b54  code/dipol.py (Endfassung, ab V3)
5a9e50ac590f4d9c792cf84e4850b22b89057c67bea96ce7fd5b41ff65cda085  code/dipol.py (Fassung V0 bis V2)
0b82b817dac9f4b81e44f1aea911aa353aec22e168aad80b262927146be289c4  code/auswertung_dipol.py
782058b1443b17a09f84a7f1e1888c593d2382dc8bab0bd2986372ca3308dac2  code/auswertung.py (Runde 18, unveraendert)
68c0a1fb9195550e4d93384304ba506c78e3239fbe9cd8a95e5571fa4e6bc45b  code/huellen_leiter.py (Runde 18, unveraendert)
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py (Code 1, unveraendert)
f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py (unveraendert)
f7fc36210a5166c5fa6a08e114395452d9ca2660f1ac11d5b3357fbe9d879238  code/pruef.py
```

Plan:

```
da41f500616ddd9f607bd0016d040e7a7c890207e2dedf2910f42bdf576cb92b  PLAN.md.eingefroren-20261002-155715 (PLAN.md gleich)
```

Ausgaben (lokal = Spiegel von /home/fmh/fmhc-physics-remote/runde19-huellen-dipol/aus/ ohne *.npz; verglichen):

```
af8c32f310e656f847b775f4cf13828be146ea560030385e2bfcdd78c51ef2fd  aus/laeufe/z-st1-*.json (verkettet, Namensfolge, 72 Dateien)
1956b380a828fa6d8fb809b160389287cd3acd012c6357853b9e9229cbd56e52  aus/laeufe/paar-st1-*.json (verkettet, 71 Dateien)
ee7a675178b57dc4f790fdffdeba78925c6890ad0e7f8ede89074654d5456ee0  aus/laeufe/z-st2-*.json (verkettet, 72 Dateien)
9a99f5f5d151294ac95260139b4c79797fe7d26f25d6415a4d6cf6a8fad4b0c2  aus/laeufe/paar-st2-*.json (verkettet, 71 Dateien)
3167308ed44194f852460d094bd29579b9f56c28f3b1e523901f9ebf1712e13a  aus/zeilen.json
70c2513ac8162112306706349a6e5005d5a5b0d55b26b1045bde97b2f5d9e7a2  aus/k1-st1.json
fbf0c17c75299461d541913235a8b9bd91f732fd8d360701769d3314f2a0556f  aus/k1-st2.json
68be3c497adcdef7abbaa90bfbc2060337fc2a06b0c85c7ea5169a0a29768943  aus/laeufe/auswertung.json
20cf3aec5bedac189cf4023ca5b2787542de29964eda91bf023444fcc8d50628  aus/laeufe/auswertung-final.json
7cacd6a11d77cbdaf5d34291912efadedec717023222c3f76f1851b2cadb00cf  aus/laeufe/stellen.json
9bb9f4afb9c72854050ead6fc11798cce1df6147259dbc7ce9c86457a190893b  aus/laeufe/umlauf-P-st1.json
9b269dff7f0bf9639b2ab8d5f79bc8c2e8eb8374dda097184a17a0ac7098eb64  aus/laeufe/umlauf-P-st2.json
adba5291ee4130160fc2a57ccfd9ec4c61f2a6c6961e2c9859de43cc92ff6160  aus/laeufe/umlauf-A-st1.json
dbc01e9d4c158ae46d77bd31c59aa3096928fb7164b90b7cc9f8c083fdf85750  aus/laeufe/umlauf-A-st2.json
6983b94a284eb36f9b432274de075f6fb2f98dc2fced57718be16515a13d7f05  aus/laeufe/d4-st1.json
6a28e0ca72163f524af4e6c2f749d96c5356efcc1ab316d6d22041a1c602719c  aus/laeufe/l0-kurven.json (= hilfs/l0-kurven.json)
710e4d38e8841d1d8fb450f7ab3910b4ef5ed8a0faec4ed53e67ce4ed6d09a56  aus/abb-stellen.png
e5de45b70cce2253293b0fd023723926cb80c43609ba3e4c1e401d581c89d37c  aus/abb-abstand.png
09f8bceb0bb89029d41ba4f7a83aeb5cc2b39edfdfde587aa5aeb13e4f72d7ec  aus/prof-st1/profile-info.json (nur .69)
10417907b7ab387269172dbde947958bf50967455c64c10127bd4200e04752b2  aus/prof-st2/profile-info.json (nur .69)
```

Hilfsdateien (hilfs/): Aufrufe k.sh, kette-v1.sh bis kette-v3.sh, laufzeiten.sh; Tabellen anhang.jq, anhang2.jq,
kurven.jq; l = 0-Daten l0-kurven.json mit Abschriftpruefung l0-pruef-quelle.txt / l0-pruef-json.txt; Zwischenstaende
anhang-zeilen.md, anhang-zeilen2.md, entwurf-ergebnis-vor-anhang.md, p1.txt, p5.txt (Textbausteine, nicht benutzt).

```
f92fdeb354715794e6c2d3c92bef4f7df77f97bc93844a7a55d4648fd506e6a6  hilfs/k.sh
85bf572cbef652866b739cdf269921ffd8929767c689fe137c481d98888162cc  hilfs/kette-v1.sh
5f078c4cdf1a01bc051cee105dc1f532e451ebacd13cace3a11f6eb03ea1a279  hilfs/kette-v2.sh
68dc3273ff2d954970f5d8024369c03aa0682f29522d30c5e7d2b4c111f7c549  hilfs/kette-v3.sh
877ff19fe33182114ad8c310b944c2efcb65a46fd51a95bcde2957251aecf189  hilfs/laufzeiten.sh
6e5753a794293c8e48061d605f314c6055a17a767f9ddde0eb21000b8122fe56  hilfs/anhang.jq
9375015bd4eac518d3724066e863f3a63439103f670464d60e78aba5c5ddee72  hilfs/anhang2.jq
ea001052ef7addbfda16ad2aebf966f8779e70951cc6cf8ad0692036d764bf34  hilfs/kurven.jq
6a28e0ca72163f524af4e6c2f749d96c5356efcc1ab316d6d22041a1c602719c  hilfs/l0-kurven.json
42aa0bfe426233876fbb8a0155fcabcffe504332fb687e6531937a89f665361f  hilfs/l0-pruef-quelle.txt (= l0-pruef-json.txt)
305c6cdf81731aa74cc4dec3514135e25dd7e2c06d319224208188c29cd4e560  hilfs/anhang-zeilen2.md
```

## 6 Einfach gesagt

Ein Q-Ball mit Huelle kann nicht nur "atmen" (gleichmaessig groesser und kleiner werden), sondern auch hin und her
kippen; das ist eine Dipol-Schwingung. Wir haben gesucht, bei welchen Ballgroessen diese Kippschwingung "still" ist, also
keine Wellen nach aussen abgibt, und bei Baellen bis zum Radius 19 genau 19 solche Stellen gefunden, mit zwei
verschieden feinen Rechengittern gleich. Sie liegen wie bei der Atmung auf Leitern mit fast gleichen Sprossenabstaenden,
und diese Abstaende sind nur 2 bis 3 Prozent groesser als bei der Atmung. Das passt zu demselben einfachen Bild: Die
Kopplung an die nach aussen laufende Welle wechselt jedes Mal das Vorzeichen, wenn im Ballinneren eine halbe Wellenlaenge
mehr Platz hat. Ob die bewiesene Kippschwingung des einfacheren Modells ohne Huelle einen stillen Nachfolger im
Huellenmodell hat, bleibt offen, weil diese Rechnung unterwegs abbrach.
