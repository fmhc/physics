
## 5 Kontrollen

### K1 (bewiesene M1-Stelle, chi-Kopplung aus; Variante K1E1 von Code 1)

- Dieselbe Kette wie die Suche: Zeilen omega^2 = 0,78 bis 0,82 (ganze E1-Zeile, 201 Punkte), Rang, Unterzeilen,
  zwei Halbierungen, dann Newton und Rechteck aus Code 1 (unveraendert).
- In jeder Zeile genau eine Nullstelle der geschlossenen Bedingung; s dort wie in Runde 17 (Stufe 2: -0,0708 bei 0,78,
  -0,0271 bei 0,79, +0,0071 bei 0,80, +0,0300 bei 0,81, +0,0449 bei 0,82). Genau ein Vorzeichenwechsel, Zellen-Umlauf -1.

| Stufe | Lage aus Halbierung (omega^2 / rho) | Lage nach Newton | Abstand zur bewiesenen Stelle | Rechteck-Umlauf | groesster Sprung | Randpunkte | sigma2/sigma1 |
|---|---|---|---|---|---|---|---|
| 1 (hp 0,01) | 0,79767681 / 1,74461753 | 0,7976767750 / 1,7446175408 | 2,3e-7 / 4,6e-7 | -1 aufgeloest | 0,170 rad | 64 | 1,2e-13 |
| 2 (hp 0,005) | 0,79767683 / 1,74461754 | 0,7976767864 / 1,7446175446 | 2,1e-7 / 4,6e-7 | -1 aufgeloest | 0,170 rad | 64 | 1,4e-13 |

- **K1 bestanden** (1e-4, Umlauf -1 aufgeloest, beide Stufen, Zellen-Umlauf -1). Die Newton-Lagen stimmen mit Runde 17
  (0,797676775 / 1,744617541) auf 1e-9 ueberein.

### Die 15 bekannten Stellen (L1), beide Stufen

- Zuordnung (PLAN 5): auf jeder Stufe genau ein eigener Kandidat je bekannter Stelle; der Zellen-Umlauf hatte schon
  vor dem Rechteck das Vorzeichen der Tabelle. Newton (Code 1) startet an der eigenen Lage, nicht an der Tabelle.

| Nr (R17) | omega^2 St1 (Newton) | rho St1 | Abstand zur Tabelle St1 (omega^2 / rho) | Abstand St2 | Umlauf St1 / St2 | groesster Sprung St1 / St2 | Randpunkte | sigma2/sigma1 St1 / St2 | Zellen-Umlauf |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,8186494777 | 1,0518798683 | 2,3e-9 / 1,7e-9 | 1,8e-9 / 1,2e-9 | +1 / +1 | 0,396 / 0,396 | 78 / 78 | 6,4e-12 / 3,1e-12 | +1 / +1 |
| 2 | 0,8205792437 | 1,3620025724 | 3,7e-9 / 2,4e-9 | 5,3e-9 / 7,1e-9 | -1 / -1 | 0,328 / 0,328 | 76 / 76 | 4,5e-12 / 2,2e-12 | -1 / -1 |
| 3 | 0,8212349922 | 1,2341124543 | 2,2e-9 / 4,3e-9 | 3,1e-9 / 5,2e-9 | +1 / +1 | 0,371 / 0,371 | 68 / 68 | 2,7e-12 / 1,6e-12 | +1 / +1 |
| 4 | 0,8357865012 | 1,0593113530 | 1,2e-9 / 3,0e-9 | 1,9e-9 / 3,6e-9 | -1 / -1 | 0,352 / 0,352 | 76 / 76 | 3,6e-12 / 7,4e-13 | -1 / -1 |
| 5 | 0,8372894678 | 1,2490386607 | 2,2e-9 / 7,4e-10 | 1,0e-9 / 1,9e-9 | -1 / -1 | 0,399 / 0,399 | 69 / 69 | 4,8e-12 / 6,0e-12 | -1 / -1 |
| 6 | 0,8401501090 | 1,4094402225 | 1,0e-9 / 2,5e-9 | 1,6e-9 / 6,5e-9 | +1 / +1 | 0,382 / 0,382 | 68 / 68 | 1,8e-13 / 4,9e-12 | +1 / +1 |
| 7 | 0,8474342576 | 1,3395604917 | 2,4e-9 / 1,7e-9 | 3,6e-10 / 5,6e-9 | +1 / +1 | 0,319 / 0,319 | 74 / 74 | 6,5e-13 / 8,2e-12 | +1 / +1 |
| 8 | 0,8603807407 | 1,2717418511 | 7,4e-10 / 1,1e-9 | 2,4e-9 / 2,8e-9 | +1 / +1 | 0,350 / 0,350 | 68 / 68 | 4,2e-12 / 6,2e-13 | +1 / +1 |
| 9 | 0,8608598134 | 1,0697635134 | 3,4e-9 / 3,4e-9 | 4,3e-9 / 4,0e-9 | +1 / +1 | 0,398 / 0,398 | 75 / 75 | 1,9e-12 / 9,2e-13 | +1 / +1 |
| 10 | 0,8812165141 | 1,3980434274 | 4,1e-9 / 2,6e-9 | 7,9e-9 / 2,4e-9 | -1 / -1 | 0,398 / 0,398 | 67 / 67 | 2,7e-12 / 2,9e-12 | -1 / -1 |
| 11 | 0,8970290558 | 1,3095535152 | 4,2e-9 / 4,8e-9 | 1,5e-9 / 1,9e-9 | -1 / -1 | 0,383 / 0,383 | 68 / 68 | 1,3e-12 / 2,2e-12 | -1 / -1 |
| 12 | 0,9009691084 | 1,0855395993 | 1,6e-9 / 6,9e-10 | 2,6e-10 / 9,8e-11 | -1 / -1 | 0,344 / 0,344 | 68 / 68 | 5,4e-13 / 5,0e-13 | -1 / -1 |
| 13 | 0,9685058155 | 1,3789199258 | 4,5e-9 / 4,2e-9 | 1,7e-9 / 9,6e-10 | +1 / +1 | 0,373 / 0,373 | 68 / 68 | 1,6e-13 / 1,1e-12 | +1 / +1 |
| 14 | 0,9751475178 | 1,1122313994 | 2,2e-9 / 5,6e-10 | 2,5e-10 / 5,8e-10 | +1 / +1 | 0,326 / 0,326 | 64 / 64 | 1,9e-13 / 4,5e-13 | +1 / +1 |
| 15 | 1,1586598791 | 1,1704152123 | 9,3e-10 / 2,3e-9 | 6,3e-9 / 4,8e-9 | -1 / -1 | 0,297 / 0,297 | 64 / 64 | 2,5e-13 / 5,6e-15 | -1 / -1 |

- Alle Umlaeufe im ersten Versuch aufgeloest (Halbbreite 1e-3, bei Nr. 6 8,6e-4 wegen der Schwelle; adaptive
  Verfeinerung auf 64 bis 78 Randpunkte).

### Stichprobe Rechteck-Umlauf gegen Zellen-Umlauf (PLAN 4), beide Stufen

- Je Kurve k = 0 bis 3 die Stelle mit kleinstem omega^2, dazu k = 4 und k = 8 (Reihenfolge des Plans; k = 12 gibt es
  im gewerteten Bereich nicht). Alle am unteren Ende des Bereichs (R = 36,8 bis 38,4), wo die Stellen am dichtesten
  liegen. Halbbreite des Rechtecks 2,4e-4 bis 2,6e-4 (halber Zeilenabstand).

| Stelle (Anhang A) | k | omega^2 / rho (Newton, St1) | R | Zellen-Umlauf St1 / St2 | Rechteck-Umlauf St1 / St2 | groesster Sprung | Randpunkte | sigma2/sigma1 St1 / St2 | d omega^2 St1-St2 |
|---|---|---|---|---|---|---|---|---|---|
| 81 | 0 | 0,76524823 / 1,02705186 | 37,18 | -1 / -1 | -1 / -1 aufgeloest | 0,386 | 84 | 7,1e-12 / 2,4e-11 | 1,7e-10 |
| 88 | 1 | 0,76405899 / 1,18834089 | 38,40 | -1 / -1 | -1 / -1 aufgeloest | 0,390 | 74 | 6,1e-11 / 1,1e-10 | 2,7e-10 |
| 85 | 2 | 0,76433960 / 1,19755340 | 38,11 | +1 / +1 | +1 / +1 aufgeloest | 0,396 | 66 | 5,3e-11 / 4,2e-11 | 2,8e-10 |
| 83 | 3 | 0,76482001 / 1,21326353 | 37,61 | -1 / -1 | -1 / -1 aufgeloest | 0,363 | 68 | 3,3e-11 / 2,2e-11 | 3,1e-10 |
| 80 | 4 | 0,76552152 / 1,23604220 | 36,92 | +1 / +1 | +1 / +1 aufgeloest | 0,352 | 72 | 7,5e-11 / 7,0e-11 | 3,5e-10 |
| 79 | 8 | 0,76562187 / 1,36666740 | 36,82 | +1 / +1 | +1 / +1 aufgeloest | 0,392 | 79 | 5,0e-11 / 3,2e-11 | 6,2e-10 |

- **Zellen-Umlauf = Rechteck-Umlauf in 6 von 6 Proben auf beiden Stufen, dazu in 15 von 15 L1-Stellen.** Damit gilt die
  Zaehlung mit dem Zellen-Umlauf (PLAN 4) ohne Vorbehalt. Echter Rangabfall an allen Proben (sigma2/sigma1 <= 1,1e-10).

### Zwei Gitterstufen

- Alle 88 Stellen auf beiden Stufen im selben Zeilenpaar auf derselben Kurve, Lage auf 7,2e-9 (omega^2), 6,0e-9 (rho),
  1,0e-6 (R); Zellen-Umlauf in 88 von 88 gleich. Keine Stelle nur auf einer Stufe.
- Zeilen: in allen 111 gewerteten Zeilen gleiche Zahl, gleiche Lage (<= 4,3e-10) und gleiche Vorzeichenfolge der
  Nullstellen von m_bc.
- Ausserhalb (nicht gewertet): Die Zeilen 255 bis 259 (R ~ 111 bis 113) haben auf beiden Stufen dieselbe Zahl und Lage
  der Nullstellen, aber verschiedene Vorzeichenfolgen; das passt zur Rundungsdiagnose von Nachtrag 4.

### Hintergrund (Konvergenz vor der Suche)

- Alle 263 Zeilen (omega^2 1,40 bis 0,74) auf beiden Stufen (hp 0,01 mit bis 19 900 Gitterpunkten; hp 0,005 mit bis
  39 800): |dQ/Q| <= 6,2e-11, |dE/E| <= 6,3e-11 zwischen den Stufen, Huellenradius R auf 3,5e-6 gleich, Rand
  |f(R_bg)|/f(0) <= 3,4e-17. Kein Profil ueber der Schwelle 1e-6.
- **Die Profile sind bis omega^2 = 0,74 (R = 114,2, Q = 1,26e7) sauber.** Die Grenze der Wertung (R = 39) kommt nicht vom
  Hintergrund, sondern von der Messgroesse (Rundungs-chi im Inneren, Nachtrag 4).
- Kosten: Bei R ~ 110 kostet ein Profil 11 bis 26 s; beide Profillaeufe erreichten die 600-s-Grenze und wurden mit
  derselben Fortsetzung ab dem letzten gespeicherten Profil fortgesetzt.
