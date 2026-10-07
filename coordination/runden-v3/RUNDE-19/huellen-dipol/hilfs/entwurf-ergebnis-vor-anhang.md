# ERGEBNIS HUELLEN-DIPOL (Runde 19)

- Code-Agent. Eigener Code: code/dipol.py (l = 1, Kette, D4), code/auswertung_dipol.py (Wertung, Bilder). Unveraendert
  importiert: code/stille3.py (Code 1), code/beutel.py, code/huellen_leiter.py (HUELLEN-LEITER), code/auswertung.py
  (Runde-18-Auswertung, nur Hilfsfunktionen).
- Start 2026-10-02 15:41:30 CEST. Plan eingefroren 15:57:15 (PLAN.md.eingefroren-20261002-155715), vor dem ersten
  .69-Lauf (13:57:20 UTC = 15:57:20 CEST). Kein Nachtrag. Bericht ab 16:16 CEST (date). Uhrzeiten der .69 in UTC
  (CEST = UTC + 2).
- Explorativ (v3). Alles modellintern (M2, linear, klassisch), keine Messdaten. Deutungen sind Hypothesen [H].

## 1 Ergebnis zuerst

1. **Die Huelle traegt auch Dipol-Leitern (D1 und D2 eingetroffen).**
   - Im Kartenfenster omega^2 = 1,40 bis 0,80 (Huellenradius R = 1,8 bis 19,4) liegen 19 stille Dipol-Stellen (l = 1)
     auf 5 chi-Kurven (k = 0 bis 4).
   - Alle 19 sind auf beiden Gitterstufen gleich (omega^2 auf <= 1,1e-8, rho auf <= 6,0e-9) und haben dort denselben
     Zellen-Umlauf +-1. Laengs jeder Kurve wechselt der Umlauf von Stelle zu Stelle.
   - Auf den Kurven k = 0, 1, 2 folgen die Stellen in fast festem Abstand in R: 2,49 / 2,26 / 2,37 im Mittel,
     Variationskoeffizient 3,6 / 3,7 / 3,9 %.
   - Vorab festgelegte Bedeutung (Karte): **Die Huelle traegt auch Dipol-Leitern. Der Mechanismus ist nicht an l = 0
     gebunden [H].**
2. **Gleiche Sprossenregel wie bei l = 0 (D3 eingetroffen).**
   - Je Kurve ist der mittlere Abstand bei l = 1 nur 1,7 bis 2,9 % groesser als bei l = 0 auf der Kurve gleichen
     Rangs im selben R-Bereich (q = 1,017; 1,027; 1,029; Grenze +-15 %).
   - Nach der Karte prueft D3, ob die Sprossenregel (halbe Innenwellenlaenge) fuer beide l dieselbe ist; im Fenster
     ist sie es [H].
   - Nicht vorhergesagt, nur beobachtet: Auf der Wandkurve k = 0 liegen die l = 1-Stellen 0,9 bis 1,1 in R hinter
     den l = 0-Stellen (0,34 bis 0,47 Abstaende). Die chi-Kurven entstehen bei l = 1 etwa 1,6 bis 2,1 in R spaeter.
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
   - Das Fenster reicht nur bis R = 19,4; je Kurve gibt es 7, 5, 4, 2 und 1 Stellen.
   - D2 und D3 stuetzen sich auf die Kurven k = 0 bis 2 (6, 4 und 3 Abstaende).
   - Gezaehlt ist mit dem Zellen-Umlauf. Der aufgeloeste Rechteck-Umlauf ist an RECHTECK_ZAHL Stellen auf beiden
     Stufen gerechnet und stimmt dort ueberall mit dem Zellen-Umlauf ueberein.

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
  2,51 / 2,46 / 2,44 / 2,43 / 2,43); die Abstaende fallen langsam gegen einen festen Wert.

## 3 Liste aller Dipol-Stellen (19)

- Sortiert nach fallendem omega^2. Lage aus Unterzeilen und Halbierung (Stufe 1); Differenzen Stufe 2 minus Stufe 1.
  R = Huellenradius (chi = 1/2). Knoten: Zahl der Vorzeichenwechsel der c-Komponente von Y_c auf (0, r_m] an den
  beiden Klammerenden (Stufe 1, nur Gegenprobe).
- Rechteck: aufgeloester Rechteck-Umlauf (Newton und Rechteck von Code 1 ab der eigenen Lage) Stufe 1 / Stufe 2,
  "-" = nicht gerechnet. Stichprobe nach PLAN 7: Nr. 15 bis 19 (je Kurve die Stelle mit kleinstem omega^2).

| Nr | k | omega^2 | rho | R | d omega^2 (1e-9) | d rho (1e-9) | d R (1e-6) | Zellen-Umlauf St1 / St2 | Knoten | Rechteck St1 / St2 |
|---|---|---|---|---|---|---|---|---|---|---|
ANHANG_ZEILEN

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

- Die Abstaende beider l laufen im Fenster gleich: groesster Abstand direkt nach der Geburt der Kurve, dann langsamer
  Abfall; die Wandkurve k = 0 ist bei beiden l die gleichmaessigste.
- **Lage gegeneinander (nur beobachtet):** Auf k = 0 liegen die l = 1-Stellen um 0,88; 0,99; 1,04; 1,08; 1,10; 1,11;
  1,12 hinter der jeweils naechstkleineren l = 0-Stelle, also 0,34 bis 0,47 der folgenden l = 0-Abstaende, mit R steigend. Lesart [H, nicht
  gerechnet]: Die offene Teilwelle l hat im Inneren die Phase k_innen r - l pi/2; fuer l = 1 verschiebt das die
  Vorzeichenwechsel der Kopplung um eine halbe Sprosse. Gleicher Abstand, verschobene Lage passt zu diesem Bild.
- **Geburt der Kurven** (erste Zeile mit k + 1 Nullstellen von m_bc, rho ~ 1,41): l = 1: k = 1 bei R = 6,71; 2: 10,36;
  3: 14,56; 4: 18,17 (Abstand 3,65 / 4,20 / 3,61). l = 0 (Runde 18): 4,70; 8,76; 12,47; 16,11. Lesart [H]: Die inneren
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
  bewiesenen Stelle faellt von Stufe 1 auf Stufe 2 um den Faktor 6,5 bzw. 6,5 (Gitterfehler, nicht Verfahrensfehler).
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
  Rangabfall (sigma2/sigma1 <= 2,5e-11). Damit gilt die Zaehlung mit dem Zellen-Umlauf. RECHTECK_WEITERE

### Zwei Gitterstufen

- Alle 72 Zeilen: auf beiden Stufen gleiche Zahl, gleiche Vorzeichenfolge und gleiche Lage (<= 1,1e-8) der Nullstellen
  von m_bc. Keine unsichere Nullstelle, kein Illinois-Fall, keine Abnahme der Nullstellenzahl zur Schranke hin.
- Alle 19 Stellen auf beiden Stufen im selben Zeilenpaar auf derselben Kurve, Lage auf 1,04e-8 (omega^2), 6,0e-9 (rho),
  1,2e-6 (R); Zellen-Umlauf 19 von 19 gleich. Keine Stelle nur auf einer Stufe, keine gepaarte Stelle mit Merker.
- Merker: Rangsprung nach Plan-Regel 0. Der Code-Merker (mit Schwellenabstand, Runde-18-Nachtrag 1) steht 9-mal je
  Stufe an neu entstehenden Kurven; er zaehlt nach dem Plan nicht. In Paar 54 (Geburtszeile von k = 2, Luecke 0,0016)
  sind auf beiden Stufen zwei Unterzeilen (t = 4/8, 5/8) der Kurve k = 2 verworfen; dort gibt es keinen Wechsel.
- Knotenzahl der c-Komponente als Gegenprobe: 0, 0, 2, 2, 2 fuer k = 0 bis 4, an jeder Stelle gleich an beiden
  Klammerenden. Monoton im Rang, aber nicht eindeutig (wie bei l = 0); als Index ungeeignet, der Rang reicht.

### Hintergrund

- Profile wie Runde 18 (gleiche Zeilen ab 1,40, letzte Zeile 0,80): Stufe 1 und 2 in 2,1 s bzw. 3,4 s, Newton in 1 bis
  4 Iterationen je Zeile. Bei 0,80: R = 19,41, chi(0) = 2,3e-9 (Rundung unkritisch; Runde-18-Grenze R ~ 39).

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
  Mittel <= 0,003 (0,1 %). Gleicher Rang heisst nicht gleicher chi-Zustand: Die Kurve k der l = 1-Leiter ist ein
  l = 1-Zustand, die Kurve k der l = 0-Leiter ein l = 0-Zustand.
- **Zaehlung mit Zellen-Umlauf** (wie Runde 18). Rechteck-Umlauf an RECHTECK_ZAHL Stellen gerechnet, ueberall gleich.
- **Doppelwechsel innerhalb einer Unterzeile** (1/8 Zeilenabstand) waeren nicht gesehen; kleinster Abstand zweier
  Stellen einer Kurve 2,19 in R.
- **Schwellen:** je 1e-4 an rho = sqrt2 - w und an rho = sqrt2 nicht abgetastet (wie Runde 18).
- **Ursprungsstart l = 1:** Reihe bis r^4 bei r0 = 2 hp. Der K1-Abstand (3e-8 auf Stufe 1, 5e-9 auf Stufe 2) und die
  Stufengleichheit der Stellen (1e-8) zeigen, dass der Startfehler die Lagen nicht merklich verschiebt.
- **Reichweite:** linear, klassisch, Modell M2, ein Drehimpuls (l = 1, je m gleich). Keine Zeitbereichspruefung der
  Dipol-Stellen.

### Selbstanzeigen

SELBSTANZEIGEN

### Laufzeiten (.69, kleintest.sh, Spur cpu6, nacheinander; Service runtime; UTC)

LAUFZEITEN

### sha256

SHA256

## 6 Einfach gesagt

EINFACH
