# ERGEBNIS HUELLEN-QUADRUPOL (Runde 20)

- Code-Agent. Eigener Code: code/quadrupol.py (l als Parameter 0, 1, 2; K1; Probe), code/auswertung_quadrupol.py
  (Wertung), code/pruef.py (Syntax). Unveraendert importiert: code/stille3.py (Code 1), code/beutel.py,
  code/huellen_leiter.py (Runde 18), code/auswertung.py (Runde 18, Hilfsfunktionen). code/dipol.py und
  code/auswertung_dipol.py liegen nur als Vorlage im Ordner (nicht auf die .69 kopiert, nicht ausgefuehrt).
- Start 2026-10-02 17:08:14 CEST. Plan geschrieben ab 17:20:06, eingefroren 17:23:30
  (PLAN.md.eingefroren-20261002-172330), vor dem ersten .69-Lauf (15:23:38 UTC = 17:23:38 CEST). Kein Nachtrag; der
  Code ist seit dem Einfrieren unveraendert (sha256 beim Einfrieren = Endstand). Bericht ab 17:47:30 CEST (date).
  Uhrzeiten der .69 in UTC (CEST = UTC + 2).
- Explorativ (v3). Alles modellintern (M2, linear, klassisch), keine Messdaten. Deutungen sind Hypothesen [H].
- Wie weit gekommen: das ganze Kartenfenster omega^2 = 1,40 bis 0,80 (R = 1,77 bis 19,41), alle 72 Zeilen und 71 Paare
  auf beiden Gitterstufen, Spurzeit zusammen 19,5 min.

## 1 Ergebnis zuerst

1. **Die Huelle traegt auch stille Quadrupol-Stellen (Q1 eingetroffen).**
   - 15 stille l = 2-Stellen in E1 auf 4 chi-Kurven: k = 0: 6, k = 1: 5, k = 2: 3, k = 3: 1.
   - Beide Stufen gleich (omega^2 <= 2,9e-9, rho <= 4,1e-9). Der Rechteck-Umlauf ist an allen 15 Stellen auf beiden
     Stufen aufgeloest und gleich dem Zellen-Umlauf. Laengs jeder Kurve wechselt der Umlauf.
   - Unter R = 2,88 (omega^2 > 1,20) gibt es noch keine l = 2-Kurve in E1.
2. **Abstand fast fest, aber gut 5 % groesser als bei l = 0 (Q2 nicht eingetroffen).**
   - k = 0: Mittel 2,566, CV 5,3 %, q = 1,057. k = 1: Mittel 2,322, CV 4,7 %, q = 1,060.
   - Die Streuung haelt die Grenze (< 10 %), der Abstand nicht (+-5 % um l = 0).
   - Nur beobachtet: Der Ueberschuss faellt mit R (k = 0 paarweise 14 % auf 1,8 %; bei l = 1 4,3 % auf 0,5 %).
3. **Versatz im Mittel 0,655 (Q3 eingetroffen, knapp ueber 0,6).**
   - Kreismittel ueber die 15 Stellen, arithmetisch 0,650. Je Kurve 0,80 / 0,63 / 0,47 / 0,42, Spanne 0,38 bis 0,89.
   - Gleich definiert fuer l = 1: 0,328 (je Kurve 0,43 / 0,33 / 0,26 / 0,19 / 0,16).
   - Nur beobachtet [H]: Der l = 2-Versatz ist fast genau doppelt so gross wie der l = 1-Versatz (gepoolt 2,00, je Kurve
     k = 0 bis 2: 1,8 bis 1,9).
4. **Bedeutung nach Karte: keine der beiden vorab festgelegten Bedeutungen ist ausgeloest.**
   - Q1 und Q3 treffen ein, Q2 nicht. Damit gilt "Eine Sprossenregel fuer alle l, R_n,l ~ (n + l/2 + konst) pi/k_innen
     [H]" nicht.
   - "Trifft Q3 nicht ein: Der Versatz hat eine andere Ursache" gilt ebenfalls nicht, weil Q3 eintrifft.
5. **K1 bestanden (Q0 eingetroffen); Grenzen.**
   - Die 6 bekannten Stellen (3 mit l = 0, 3 mit l = 1) findet derselbe Code auf beiden Stufen bitgleich zu den
     Vorlaeufern wieder. Gegen die Stufe-1-Referenz sind das 0 (Stufe 1) und <= 1,04e-8 (Stufe 2). Der Rechteck-Umlauf
     ist ueberall aufgeloest und gleich der Referenz.
   - Probe l = 2: Ein Start bei 4 hp verschiebt die Nullstellen um <= 2,9e-10.
   - Grenzen: nur R <= 19,4. Q2 stuetzt sich auf zwei Kurven (5 und 4 Abstaende). Linear, klassisch, M2, keine
     Zeitbereichspruefung.

## 2 Vorhersagen Q0 bis Q3

Gewertet nach PLAN Abschnitt 8 auf dem ganzen Fenster: Zeilen 0 bis 71, Paare 0 bis 70, omega^2 = 1,40 bis 0,80, beide
Stufen vollstaendig.

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| Q0 | K1 bestanden (90 %) | **eingetroffen** | 6 von 6 Stellen auf beiden Stufen: auf Kurve k im Paar i gefunden, Newton-Lage auf Stufe 1 bitgleich zur Referenz (Abstand 0), auf Stufe 2 <= 1,04e-8 (omega^2) bzw. <= 6,0e-9 (rho) gegen die Stufe-1-Referenz (bitgleich die Stufe-2-Lagen der Vorlaeufer). Rechteck-Umlauf aufgeloest im ersten Versuch und gleich dem Referenz-Umlauf, Zellen-Umlauf ebenso (Tabelle in Abschnitt 5) |
| Q1 | Mindestens 5 stille Quadrupol-Stellen in E1 (75 %) | **eingetroffen** | N = 15 im Fenster 0,80 bis 1,40. Alle auf beiden Stufen, keine nur auf einer Stufe, keine mit Merker |
| Q2 | Abstand in R je Kurve fast fest (Streuung < 10 %) und innerhalb +-5 % des l = 0-Abstands (60 %) | **nicht eingetroffen** | Kurven mit >= 4 Stellen: k = 0 (6 Stellen): Mittel 2,566, CV 0,053 (erfuellt), l = 0-Vergleich 2,428 (5 Abstaende), q = 1,057 (verfehlt). k = 1 (5 Stellen): 2,322, CV 0,047 (erfuellt), l = 0 2,190 (5), q = 1,060 (verfehlt) |
| Q3 | Versatz v im Mittel zwischen 0,6 und 1,0 (50 %) | **eingetroffen** | Kreismittel 0,6546 ueber 15 Stellen (Laenge des Mittelvektors 0,553), arithmetisch 0,6505, kleinstes v 0,381, groesstes 0,890. Keine Stelle am Rand der l = 0-Liste (kein Randfall nach PLAN 6) |

- Q3: Gewertet ist das Kreismittel (PLAN 6). Das arithmetische Mittel ergibt denselben Ausgang. Kein Wert liegt naeher
  als 0,11 am Umbruch 0/1.
  - Je Kurve: k = 0: 0,804; k = 1: 0,634; k = 2: 0,465; k = 3: 0,415.
  - Die inneren Kurven k = 2 und 3 liegen einzeln unter 0,6. Das gepoolte Mittel tragen k = 0 und 1 (11 der 15 Stellen).
- Bedeutung: siehe Abschnitt 1, Punkt 4.

## 3 Liste aller Quadrupol-Stellen (15)

- Sortiert nach fallendem omega^2. Lage aus Unterzeilen und Halbierung (Stufe 1); Differenzen Stufe 2 minus Stufe 1.
  R = Huellenradius (chi = 1/2), Stufe 1.
- Rechteck: aufgeloester Rechteck-Umlauf (Newton und Rechteck von Code 1 ab der eigenen Lage, Halbbreite 1e-3), alle im
  ersten Versuch. Knoten: Vorzeichenwechsel der c-Komponente von Y_c auf (0, r_m] an beiden Klammerenden, nur berichtet.
  v: Versatz nach PLAN 6 (Abschnitt 4).

| Nr | k | omega^2 | rho | R | d omega^2 (1e-9) | d rho (1e-9) | d R (1e-6) | Zellen-Umlauf St1 / St2 | Knoten | Rechteck St1 / St2 (aufgeloest) | groesster Sprung St1 / St2 (rad) | gezaehlt | v |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1,0236993 | 1,25175243 | 4,798 | 2,86 | 3,14 | 0,53 | -1 / -1 | 0 / 0 | -1 / -1 | 0,321 / 0,321 | ja | 0,624 |
| 2 | 0 | 0,91519592 | 1,14526134 | 7,593 | 1,15 | 1,32 | 0,15 | 1 / 1 | 0 / 0 | 1 / 1 | 0,393 / 0,393 | ja | 0,749 |
| 3 | 1 | 0,87715379 | 1,37901568 | 9,498 | 2,1 | 3,52 | 0,19 | -1 / -1 | 0 / 0 | -1 / -1 | 0,395 / 0,395 | ja | 0,482 |
| 4 | 0 | 0,86697594 | 1,10288927 | 10,18 | 0,71 | 0,85 | 0,31 | -1 / -1 | 0 / 0 | -1 / -1 | 0,345 / 0,345 | ja | 0,811 |
| 5 | 1 | 0,84585163 | 1,32273553 | 11,968 | 1,29 | 2,39 | 0,32 | 1 / 1 | 0 / 0 | 1 / 1 | 0,389 / 0,389 | ja | 0,584 |
| 6 | 0 | 0,83897984 | 1,0804278 | 12,694 | 0,52 | 0,65 | 0,17 | 1 / 1 | 0 / 0 | 1 / 1 | 0,397 / 0,397 | ja | 0,848 |
| 7 | 2 | 0,83879001 | 1,40275346 | 12,715 | 1,8 | 3,98 | 0,17 | 1 / 1 | 2 / 2 | 1 / 1 | 0,396 / 0,396 | ja | 0,381 |
| 8 | 1 | 0,82627312 | 1,28705021 | 14,301 | 0,93 | 1,65 | 0,21 | -1 / -1 | 0 / 0 | -1 / -1 | 0,396 / 0,396 | ja | 0,651 |
| 9 | 0 | 0,8205289 | 1,0665439 | 15,172 | 0,41 | 0,54 | 0,19 | -1 / -1 | 0 / 0 | -1 / -1 | 0,389 / 0,389 | ja | 0,872 |
| 10 | 2 | 0,81993055 | 1,35292669 | 15,268 | 1,19 | 3,39 | -0,04 | -1 / -1 | 2 / 2 | -1 / -1 | 0,33 / 0,33 | ja | 0,474 |
| 11 | 1 | 0,81260401 | 1,26337251 | 16,565 | 0,73 | 1,22 | 0,06 | 1 / 1 | 0 / 0 | 1 / 1 | 0,376 / 0,376 | ja | 0,7 |
| 12 | 0 | 0,80740366 | 1,05711639 | 17,63 | 0,34 | 0,47 | 0,26 | 1 / 1 | 0 / 0 | 1 / 1 | 0,376 / 0,376 | ja | 0,89 |
| 13 | 2 | 0,80717448 | 1,31621042 | 17,68 | 0,88 | 2,51 | 0,06 | 1 / 1 | 2 / 2 | 1 / 1 | 0,398 / 0,398 | ja | 0,54 |
| 14 | 3 | 0,80330068 | 1,37293427 | 18,573 | 1,08 | 4,1 | -0,15 | 1 / 1 | 2 / 2 | 1 / 1 | 0,396 / 0,396 | ja | 0,415 |
| 15 | 1 | 0,80242766 | 1,24679658 | 18,787 | 0,6 | 0,95 | 0,2 | -1 / -1 | 0 / 0 | -1 / -1 | 0,36 / 0,36 | ja | 0,737 |

- Rechteck an allen 15 Stellen und beiden Stufen (30 Proben):
  - Rechteck-Umlauf = Zellen-Umlauf in 30 von 30. Echter Rangabfall: sigma2/sigma1 <= 1,4e-11.
  - 68 bis 78 Randpunkte. Newton-Lage gegen Halbierungslage <= 1,8e-7 (omega^2, Nr 4) bzw. <= 1,7e-7 (rho, Nr 15).
- Umlauf laengs der Kurven: k = 0: -1, +1, -1, +1, -1, +1; k = 1: -1, +1, -1, +1, -1; k = 2: +1, -1, +1.
- Knotenzahl der c-Komponente: 0, 0, 2, 2 fuer k = 0 bis 3, an jeder Stelle gleich an beiden Klammerenden. Das ist
  dasselbe Muster wie bei l = 0 und l = 1. Sie ist nirgends Bedingung.

## 4 Abstaende und Versatz fuer l = 0, 1, 2 je Kurve (gleich definiert)

- Lagen R (Stufe 1):
  - l = 0: Runde 18, ref/l0-stellen-r18.json = RUNDE-18 aus/laeufe/stellen.json, volle Stellenzahl.
  - l = 1: HUELLEN-DIPOL, ref/l1-stellen-r19.json.
  - l = 2: diese Suche.
- q = mittlerer Abstand / mittlerer l = 0-Abstand derselben Kurve k (Paarmitten im R-Bereich der Stellen). Versatz
  v = (R - R0_unten) / (folgender l = 0-Abstand), modulo 1. Fuer l = 0 ist v = 0 per Definition.
- Die l = 0-Zeilen zeigen nur die Lagen im Fenster R <= 19,41.

| k | l | Lagen R | Abstaende | Mittel (CV) | l = 0-Vergleich: Mittel (Zahl) | q | v je Stelle | v Kreismittel |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 3,21 5,76 8,21 10,64 13,06 15,48 17,90 | 2,551 2,452 2,431 2,422 2,418 2,415 | 2,448 (0,021) | - | - | 0 (Def.) | 0 |
| 0 | 1 | 4,09 6,75 9,25 11,72 14,16 16,59 19,02 | 2,660 2,509 2,463 2,443 2,433 2,426 | 2,489 (0,036) | 2,448 (6) | 1,017 | 0,344 0,403 0,430 0,445 0,454 0,461 0,466 | 0,429 |
| 0 | 2 | 4,80 7,59 10,18 12,69 15,17 17,63 | 2,795 2,587 2,513 2,478 2,458 | 2,566 (0,053) | 2,428 (5) | **1,057** | 0,624 0,749 0,811 0,848 0,872 0,890 | 0,804 |
| 1 | 0 | 5,92 8,40 10,68 12,89 15,06 17,21 19,35 | 2,481 2,280 2,208 2,173 2,152 2,139 | 2,239 (0,058) | - | - | 0 (Def.) | 0 |
| 1 | 1 | 8,98 11,35 13,62 15,84 18,02 | 2,376 2,270 2,217 2,186 | 2,262 (0,037) | 2,203 (4) | 1,027 | 0,253 0,305 0,338 0,362 0,380 | 0,328 |
| 1 | 2 | 9,50 11,97 14,30 16,57 18,79 | 2,470 2,334 2,264 2,222 | 2,322 (0,047) | 2,190 (5) | **1,060** | 0,482 0,584 0,651 0,700 0,737 | 0,634 |
| 2 | 0 | 9,25 11,81 14,19 16,47 18,71 | 2,562 2,373 2,286 2,237 | 2,365 (0,060) | - | - | 0 (Def.) | 0 |
| 2 | 1 | 12,28 14,75 17,09 19,38 | 2,464 2,349 2,284 | 2,366 (0,039) | 2,299 (3) | 1,029 | 0,198 0,245 0,278 0,303 | 0,256 |
| 2 | 2 | 12,72 15,27 17,68 | 2,553 2,411 | 2,482 (0,040) | 2,299 (3) | 1,080 (3 Stellen, nicht gewertet) | 0,381 0,474 0,540 | 0,465 |
| 3 | 0 | 12,56 15,16 17,60 | 2,600 2,435 | 2,518 (0,046) | - | - | 0 (Def.) | 0 |
| 3 | 1 | 15,58 18,10 | 2,516 | 2,516 | 2,435 (1) | 1,033 | 0,173 0,214 | 0,193 |
| 3 | 2 | 18,57 | - | - | - | - | 0,415 | 0,415 |
| 4 | 0 | 18,49 | - | - | - | - | 0 (Def.) | 0 |
| 4 | 1 | 18,89 | - | - | - | - | 0,159 | 0,159 |

- **Versatz gepoolt:**
  - l = 0: 0 (Definition).
  - l = 1: Kreismittel 0,328 (arithmetisch 0,327, 19 Stellen, Laenge 0,818, Spanne 0,159 bis 0,466).
  - l = 2: Kreismittel 0,655 (arithmetisch 0,650, 15 Stellen, Laenge 0,553, Spanne 0,381 bis 0,890).
- Die l = 1-Werte von q (1,017; 1,027; 1,029) sind die von HUELLEN-DIPOL. Die l = 0-Lagen in voller Stellenzahl
  aendern daran in drei Stellen nichts.
- **Geburt der Kurven** (erste Zeile mit k + 1 Nullstellen von m_bc, rho ~ 1,41), in R:

  | Kurve | l = 0 (Runde 18) | l = 1 (HUELLEN-DIPOL) | l = 2 |
  |---|---|---|---|
  | k = 0 | ab Zeile 0 (R = 1,77) | ab Zeile 0 (R = 1,77) | Zeile 20, R = 2,88 |
  | k = 1 | 4,7 | 6,71 | 8,26 |
  | k = 2 | 8,76 | 10,36 | 12,47 |
  | k = 3 | 12,47 | 14,56 | 16,11 |
  | k = 4 | 16,11 | 18,17 | - |

  Die Zeilen 0 bis 19 (R = 1,77 bis 2,81) haben fuer l = 2 keine Nullstelle in E1.

**Nur beobachtet, nachtraeglich, nicht gewertet [H]:**

- **Abstand:** Paarweise gegen den l = 0-Abstand mit naechster Paarmitte betraegt der Ueberschuss auf k = 0:
  - l = 2: 1,140; 1,064; 1,038; 1,025; 1,018.
  - l = 1: 1,043; 1,023; 1,013; 1,009; 1,006; 1,005.
  - Bei l = 2 ist er etwa dreimal so gross wie bei l = 1 und faellt ebenso mit R. Das passt zum Verhaeltnis der
    Zentrifugalterme 6 : 2. Gerechnet ist das nicht.
  - Auf k = 1 ist der Ueberschuss paarweise 1,118; 1,074; 1,052; 1,039. Hier kommt hinzu, dass der gleichrangige
    l = 0-Partner ein anderer chi-Zustand ist (naechster Punkt). Gegen l = 0, Kurve k + 1 waere q = 0,982 (k = 1) bzw.
    0,986 (k = 2).
- **Versatz der Wandkurve k = 0:** Bei aehnlichem R ist v(l = 2) / v(l = 1) = 0,624 / 0,344 = 1,81 (R ~ 4 bis 5) und
  0,890 / 0,466 = 1,91 (R ~ 18 bis 19). v steigt fuer beide l mit R an.
  - Lesart [H]: Die Phase der Innenwelle j_l ~ sin(kr - l pi/2) verschiebt um l/2 Abstaende. Dazu kommt eine
    Korrektur, die mit R abnimmt (Nullstellen von j_2 liegen 0,83 bis 0,95 Abstaende hinter n pi).
- **Innere Kurven, Rangpartner k + 1:** Die l = 2-Stellen der Kurven k >= 1 liegen fast auf den l = 0-Stellen der
  naechsthoeheren Kurve k + 1.
  - Gleich definierter Versatz gegen l = 0, Kurve k + 1:
    - k = 1 gegen l = 0, k = 2: 0,097; 0,066; 0,051; 0,042; 0,036.
    - k = 2 gegen k = 3: 0,058; 0,043; 0,035.
    - k = 3 gegen k = 4: 0,032.
  - rho liegt dabei nur 0,006 bis 0,019 tiefer. Beispiel: Nr 8 bei R = 14,30 mit rho = 1,2871, l = 0, k = 2 bei
    R = 14,19 mit rho = 1,2998.
  - Auch die Geburt der l = 2-Kurve k faellt nahe an die der l = 0-Kurve k + 1 (k = 2 und 3 in derselben Zeile).
  - Lesart [H]: Der l = 2-chi-Zustand vom Rang k hat etwa so viele radiale Halbwellen wie der l = 0-Zustand vom Rang
    k + 1. Die Nullstellen von j_2 liegen nahe (n + 1) pi.
  - Der Vergleich "gleicher Rang" (Karte) paart fuer die inneren Kurven also verschiedene chi-Zustaende. Nur die
    Wandkurve k = 0 vergleicht Gleiches mit Gleichem.
  - Fuer eine Folgekarte waere ein Vergleich nach rho (gleiche chi-Energie) statt nach Rang naheliegend. Das ist eine
    nachtraegliche Beobachtung und keine Wertung.

## 5 Kontrollen, Grenzen, Selbstanzeigen, Laufzeiten, sha256

### K1 (Q0): bekannte Stellen mit demselben Code

- Kette je Stelle: Zeilen i und i+1, Paar i (HL.cmd_block), Punkt auf Kurve k, dann Newton und Rechteck
  (HL.cmd_umlauf). Modell M2, quadrupol.py mit ell=0 bzw. ell=1.
- Referenzen: ref/k1-referenz.json, per jq aus den Vorlaeuferdateien gezogen (Newton-Lagen Stufe 1). Abstand bei Stufe 2
  ebenfalls gegen die Stufe-1-Referenz.

| l | Stelle (Referenz) | k | Paar | Stufe | gefunden | Zellen-Umlauf | Newton omega^2 / rho | Abstand zur Referenz | Rechteck-Umlauf | groesster Sprung | Randpunkte | sigma2/sigma1 | bestanden |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Runde 18 Nr 1 (R17 Nr 15) | 0 | 24 | 1 | ja | -1 | 1,1586598791 / 1,1704152123 | 0 / 0 | -1 aufgeloest | 0,297 | 64 | 2,5e-13 | ja |
| 0 | Runde 18 Nr 1 (R17 Nr 15) | 0 | 24 | 2 | ja | -1 | 1,1586598863 / 1,1704152148 | 7,2e-9 / 2,5e-9 | -1 aufgeloest | 0,297 | 64 | 5,6e-15 | ja |
| 0 | Runde 18 Nr 5 (R17 Nr 11) | 1 | 50 | 1 | ja | -1 | 0,8970290558 / 1,3095535152 | 0 / 0 | -1 aufgeloest | 0,383 | 68 | 1,3e-12 | ja |
| 0 | Runde 18 Nr 5 (R17 Nr 11) | 1 | 50 | 2 | ja | -1 | 0,8970290585 / 1,3095535181 | 2,7e-9 / 2,8e-9 | -1 aufgeloest | 0,383 | 68 | 2,2e-12 | ja |
| 0 | Runde 18 Nr 9 (R17 Nr 7) | 2 | 56 | 1 | ja | +1 | 0,8474342576 / 1,3395604917 | 0 / 0 | +1 aufgeloest | 0,319 | 74 | 6,5e-13 | ja |
| 0 | Runde 18 Nr 9 (R17 Nr 7) | 2 | 56 | 2 | ja | +1 | 0,8474342596 / 1,3395604956 | 2,0e-9 / 3,9e-9 | +1 aufgeloest | 0,319 | 74 | 8,2e-12 | ja |
| 1 | HUELLEN-DIPOL Nr 1 | 0 | 32 | 1 | ja | -1 | 1,0730590671 / 1,2057817383 | 0 / 0 | -1 aufgeloest | 0,281 | 64 | 7,0e-14 | ja |
| 1 | HUELLEN-DIPOL Nr 1 | 0 | 32 | 2 | ja | -1 | 1,0730590567 / 1,2057817323 | 1,04e-8 / 6,0e-9 | -1 aufgeloest | 0,281 | 64 | 1,1e-13 | ja |
| 1 | HUELLEN-DIPOL Nr 5 | 1 | 55 | 1 | ja | +1 | 0,8523787403 / 1,2968369948 | 0 / 0 | +1 aufgeloest | 0,399 | 69 | 3,2e-12 | ja |
| 1 | HUELLEN-DIPOL Nr 5 | 1 | 55 | 2 | ja | +1 | 0,8523787398 / 1,2968369942 | 5,3e-10 / 6,3e-10 | +1 aufgeloest | 0,399 | 69 | 4,8e-12 | ja |
| 1 | HUELLEN-DIPOL Nr 14 | 2 | 66 | 1 | ja | +1 | 0,8099386623 / 1,2947977232 | 0 / 0 | +1 aufgeloest | 0,394 | 74 | 3,7e-12 | ja |
| 1 | HUELLEN-DIPOL Nr 14 | 2 | 66 | 2 | ja | +1 | 0,8099386624 / 1,2947977235 | 7,7e-11 / 3,0e-10 | +1 aufgeloest | 0,394 | 74 | 2,1e-12 | ja |

- Auf Stufe 1 sind nicht nur die Newton-Lagen, sondern auch die Zellenlagen bitgleich mit den Vorlaeuferdateien
  (Beispiel 0,8474342905935343 in Paar 56). quadrupol.py geht fuer l = 0 und l = 1 also genau den Rechenweg von
  Code 1 bzw. dipol.py.
- Die Stufe-2-Newton-Lagen sind bitgleich die Stufe-2-Werte der Vorlaeufer (Runde 18 aus/umlauf-L1-st2.json,
  HUELLEN-DIPOL aus/laeufe/umlauf-A-st2.json). Die Abstaende in der Tabelle sind gegen die Stufe-1-Referenz gemessen.
- Im Paar je Stelle gab es genau einen Punkt, ohne weg-Merker, mit steig != 0.

### Probe l = 2 (PLAN 4, nur berichtet)

| Zeile | omega^2 | R | Nullstellen von m_bc (Vorzeichen) | r0 = 4 hp statt 2 hp: max abs(d rho) / max rel. abs(d s) | Abklingstart am Gebietsrand statt n_start |
|---|---|---|---|---|---|
| 40 | 1,00 | 5,23 | 1 (-) | 2,9e-10 / 1,9e-7 | bitgleich (0 / 0) |
| 60 | 0,8321 | 13,52 | 3 (+-+) | 1,1e-13 / 1,5e-8 | bitgleich |
| 71 | 0,80 | 19,41 | 4 (+++-) | 5,8e-14 / 6,1e-9 | bitgleich |

- Zahl und Vorzeichenfolge der Nullstellen waren in allen Varianten gleich. Der Start r^3 und der k_2-Start sind damit
  fuer die Lagen unkritisch.
- Dass der Abklingstart bitgleich herausfaellt, deute ich so [H]: Die abklingenden Loesungen wachsen nach innen ueber
  viele Groessenordnungen. Nach der Normierung ist ihr Startort darum auf Maschinengenauigkeit vergessen.

### Zwei Gitterstufen und Merker

- Alle 72 Zeilen: auf beiden Stufen gleiche Zahl, gleiche Vorzeichenfolge und gleiche Lage (<= 9,9e-9) der Nullstellen
  von m_bc. Keine unsichere Nullstelle, kein Illinois-Fall, keine Abnahme der Nullstellenzahl zur Schranke hin.
- Alle 15 Stellen auf beiden Stufen im selben Zeilenpaar auf derselben Kurve. Lage auf 2,9e-9 (omega^2), 4,1e-9 (rho),
  5,3e-7 (R). Zellen-Umlauf 15 von 15 gleich. Keine Stelle nur auf einer Stufe, keine gepaarte Stelle mit Merker.
- Rangsprung nach Plan-Regel: 0.
- Der Code-Merker (mit Schwellenabstand, wie Runde 18/19) steht 8-mal je Stufe, immer an der juengsten Kurve in ihren
  ersten beiden Paaren: k = 0: Paare 20, 21; k = 1: 50, 51; k = 2: 58, 59; k = 3: 65, 66 (Luecke 0,0017 bis 0,017). Nach
  dem Plan zaehlt er nicht.
  - Nr 7 (k = 2) liegt im Geburtspaar 58 auf der markierten Kurve. Ihr Rechteck-Umlauf ist auf beiden Stufen
    aufgeloest und gleich dem Zellen-Umlauf.
  - Nr 6 (Paar 58) und Nr 11 (Paar 65) liegen in solchen Paaren auf anderen Kurven.

### Hintergrund

- Profile wie Runde 18/19 (dieselbe Zeilenliste, sha256 gleich der Dipol-Liste), 72 Zeilen auf beiden Stufen. Newton
  in <= 5 Iterationen je Zeile.
- Stufenvergleich (jq auf profile-info.json): abs(dQ/Q) <= 6,2e-11, abs(dE/E) <= 6,3e-11, R auf 3,5e-6 gleich, Rand
  abs(f(R_bg))/f(0) <= 6,8e-17. Bei 0,80: R = 19,41, chi(0) = 2,3e-9.

### Grenzen

- **Fenster:** nur omega^2 = 0,80 bis 1,40 (R <= 19,4), wie Karte. Wenige Stellen je Kurve; Q2 beruht auf zwei Kurven
  mit 5 und 4 Abstaenden.
- **Q3:** Q3 haengt am gepoolten Mittel ueber Kurven mit verschiedenem Versatz (0,42 bis 0,80 je Kurve, Laenge des
  Mittelvektors 0,55). Das Mittel haengt also davon ab, wie viele Stellen jede Kurve im Fenster beitraegt.
- **Gleicher Rang ist nicht gleicher chi-Zustand** (Abschnitt 4, nachtraegliche Beobachtung): Fuer die inneren
  Kurven vergleicht die Kartendefinition l = 2-Zustaende mit l = 0-Zustaenden anderer Knotenzahl.
- **Zaehlung** mit dem Zellen-Umlauf wie im Vorlaeufer. Der Rechteck-Umlauf ist an allen Funden auf beiden Stufen
  gerechnet und ueberall gleich.
- **Nicht aufloesbar:** Doppelwechsel innerhalb einer Unterzeile (1/8 Zeilenabstand) waeren nicht gesehen; der
  kleinste Abstand zweier Stellen einer Kurve ist 2,22 in R. Je 1e-4 an den Schwellen ist nicht abgetastet.
- **Reichweite:** linear, klassisch, Modell M2, ein Drehimpuls (l = 2, je m gleich). Keine Zeitbereichspruefung.

### Selbstanzeigen

- **Lokale Regel verletzt:** einmal awk (17:31 CEST, `awk 'NR%3==0'` in einer Pipe hinter grep, Ausgabe durch `head -0`
  verworfen, wirkungslos).
  - Sonst lokal nur jq, grep, sed, cut, tr, cp, diff, ls, mkdir, cat, head, tail, wc, sort, chmod, sha256sum, rsync,
    ssh, date. Dazu bash-Schleifen und Warteschleifen mit sleep.
  - Eine lokale Ueberwachung (tail -F mit grep auf aus/logs/kette.txt) habe ich am Ende selbst gestoppt.
  - Kein python und kein bc lokal.
- **Lesen ausserhalb der Freigabe:** In einer Sammelauflistung erschien die Ordnerliste von
  RUNDE-19/huellen-dipol/hilfs/ (nur Dateinamen). Keine Datei daraus geoeffnet. Nichts aus Sperrbereichen.
- **.69:**
  - Ausserhalb des eigenen Ordners nur `ls -la` auf kleintest.sh und auf den venv-Python (Dateieintrag, nicht der
    Inhalt). kleintest.sh nicht gelesen.
  - Angelegt habe ich nur /home/fmh/fmhc-physics-remote/runde20-huellen-quadrupol/.
  - sha256sum nur im eigenen Ordner. Keine Prozesse beendet.
- **Nachtraegliche Auswertung:** Die Beobachtungen in Abschnitt 4 (Rang k + 1, paarweise Verhaeltnisse) habe ich
  nach den Ergebnissen mit jq auf eigenen Ausgaben gerechnet (hilfs/l2-k-plus-1.json, hilfs/versatz.jq). Sie sind nicht
  gewertet und aendern keine Wertung.
- **Plan:** kein Nachtrag. Die Kette prueft K1 per jq vor dem ersten Block automatisch; dazwischen gab es keine
  Entscheidung von Hand.
- **Sonst:** Nichts in den Scratchpad geschrieben; die Ausgaben der Hintergrund-Befehle legt das Werkzeug selbst unter
  /tmp/claude-1000/.../tasks ab. Kein git, kein Peerbus, keine Unteragenten, keine Literatur.

### Laufzeiten (.69, kleintest.sh, Spur cpu6, nacheinander; Service runtime; UTC)

| Lauf | Start | Ende | Dauer | rc |
|---|---|---|---|---|
| q20-pruef (py_compile) | 15:23:38 | 15:23:38 | 0,1 s | 0 |
| q20-liste | 15:23:38 | 15:23:39 | 0,4 s | 0 |
| q20-prof-st1 / -st2 | 15:23:39 / 15:23:41 | 15:23:41 / 15:23:45 | 2,2 / 3,4 s | 0 |
| q20-k1-l0-st1 / q20-k1-l1-st1 | 15:23:45 / 15:24:18 | 15:24:18 / 15:24:57 | 33,2 / 38,8 s | 0 |
| q20-k1-l0-st2 / q20-k1-l1-st2 | 15:24:57 / 15:26:04 | 15:26:04 / 15:27:18 | 66,7 / 74,3 s | 0 |
| q20-probe | 15:27:18 | 15:27:45 | 26,9 s | 0 |
| q20-b1-0-71 (Stufe 1, Zeilen 0 bis 71) | 15:27:45 | 15:31:30 | 224,5 s | 0 |
| q20-b2-0-40 / q20-b2-40-71 (Stufe 2) | 15:31:30 / 15:34:17 | 15:34:17 / 15:38:39 | 166,9 / 262,6 s | 0 |
| q20-b1-0-71-w, -b2-0-40-w, -b2-40-71-w (Fortsetzung, nichts zu tun) | 15:38:39 | 15:38:41 | je 0,4 s | 0 |
| q20-stellen (Auswertung) | 15:38:41 | 15:38:41 | 0,6 s | 0 |
| q20-uA1 / q20-uA2 (Rechteck an allen Funden) | 15:38:41 / 15:40:12 | 15:40:12 / 15:43:11 | 90,6 / 178,5 s | 0 |
| q20-final | 15:43:11 | 15:43:11 | 0,5 s | 0 |

- Zusammen 1171 s (19,5 min) Spurzeit auf cpu6, jeder Aufruf unter der 600-s-Grenze (laengster 262,6 s).

### sha256

Code (lokal = .69, verglichen; seit dem Einfrieren unveraendert):

```
de6b6a080d655de641be0080df96fca5d132baa9216f1135d126e3d8acdd2a23  code/quadrupol.py
dc5d0ab49781e8ff2ff22f3a1f13ec4c5831684d63ed4d77b0090417ada5dd6c  code/auswertung_quadrupol.py
f7fc36210a5166c5fa6a08e114395452d9ca2660f1ac11d5b3357fbe9d879238  code/pruef.py
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py (Code 1, unveraendert)
68c0a1fb9195550e4d93384304ba506c78e3239fbe9cd8a95e5571fa4e6bc45b  code/huellen_leiter.py (Runde 18, unveraendert)
f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py (unveraendert)
782058b1443b17a09f84a7f1e1888c593d2382dc8bab0bd2986372ca3308dac2  code/auswertung.py (Runde 18, unveraendert)
0094476d6b88a37bbbd96d411f823ab335ef78ba13c710b7f5cab81774dc0b54  code/dipol.py (Vorlage, nicht ausgefuehrt)
0b82b817dac9f4b81e44f1aea911aa353aec22e168aad80b262927146be289c4  code/auswertung_dipol.py (Vorlage, nicht ausgefuehrt)
```

Plan:

```
8d67ecb6fff4e900bed2757b4fe38af727110fac20433adde673818a606616fc  PLAN.md.eingefroren-20261002-172330 (PLAN.md gleich)
```

Referenzdaten (ref/, Kopien der Vorlaeuferdateien bzw. per jq daraus):

```
7f78dfe807ab6c0902e556887b95a778876dfa8708b6fd8c38c30c9cab7d3cf6  ref/k1-referenz.json
5ce185ec655577131d6eca73cb4e8006aab6294ca4ad91840360caaf0a6ab202  ref/l0-stellen-r18.json (= RUNDE-18 aus/laeufe/stellen.json)
7cacd6a11d77cbdaf5d34291912efadedec717023222c3f76f1851b2cadb00cf  ref/l1-stellen-r19.json (= RUNDE-19 huellen-dipol aus/laeufe/stellen.json)
3167308ed44194f852460d094bd29579b9f56c28f3b1e523901f9ebf1712e13a  ref/zeilen-r19.json (= aus/zeilen.json dieser Runde)
```

Ausgaben (lokal = Spiegel von /home/fmh/fmhc-physics-remote/runde20-huellen-quadrupol/aus/ ohne *.npz; Stichproben
verglichen):

```
c95eeb9299671ae7d43c85406dc0b641d677240963bdef8282241ca80896a1a9  aus/laeufe/z-st1-*.json (verkettet, Namensfolge, 72 Dateien)
154838b64272779688c900b52438ff888cfd070507104ade2f1e69aab90df039  aus/laeufe/paar-st1-*.json (verkettet, 71 Dateien)
a36658709491335b6ca0e05be4b37885be8ff63703beedba269208a457c01fb9  aus/laeufe/z-st2-*.json (verkettet, 72 Dateien)
a056925fb4cc323974466cc93508356f767a5529c119ccc1e9b57aa43576aabb  aus/laeufe/paar-st2-*.json (verkettet, 71 Dateien)
3167308ed44194f852460d094bd29579b9f56c28f3b1e523901f9ebf1712e13a  aus/zeilen.json
35521477795feaa443a4a56ee79aa5a8fa7909117d5c62f37a36c65c03f502a4  aus/laeufe/auswertung.json
918e189eba4bcc5d7192d7e9c48ba43a08175f9c2cf49d5413cfe8d0a1e7702f  aus/laeufe/auswertung-final.json
44a79034e33adb36f03773edb92e1a81996d81baace1131807be6639b9698708  aus/laeufe/stellen.json
9a64552b15c8574fd5dc3a2a946fc9a0eb6f98d69fa226958b215cfcd41f6e82  aus/laeufe/k1-l0-st1.json
415238e8675ed3a1ba6a478639ec18712939a94d7a59fdb6c325f6c71518d28b  aus/laeufe/k1-l0-st2.json
b659fcce148dda9553359864ee55bb82de63086fabc608e5b502aa46193c88d8  aus/laeufe/k1-l1-st1.json
2d0de9d1fdab09d46db0979b8c2daa79c81fd598d3bc7d784865bcb33f5472a8  aus/laeufe/k1-l1-st2.json
573164680afc66bbf2cb6934ce991ec6e81f6deca75688c059747129a10580c7  aus/k1-l0/*.json + aus/k1-l1/*.json (verkettet, 60 Dateien)
6103e495142ff8855eabee570a0712d85311edc5fe7364f8bc358a7784e66c0e  aus/laeufe/probe-l2-st1.json
db0f13cddb19973c5cfb63c0ffe7972f916393e950b1a49464315cf5b16058d8  aus/laeufe/umlauf-punkte-alle-st1.json
0646866f53eb5983d50e7eabaf5584ce92f0ea6e273e59bd730f71328c0265c5  aus/laeufe/umlauf-punkte-alle-st2.json
dbd262cfcf07b35898164cdb8af3bbd29d6a619679f74727cd885dfd6127cc52  aus/laeufe/umlauf-alle-st1.json
af81c75e088544ddf267e2fd0b9c3ed29f7b1d40b3bcbee2841b15cf1d971fdc  aus/laeufe/umlauf-alle-st2.json
5515c14a8753080ad8b5301a67b752fa9b0a6b9dd13c031923d65ba640b4a8d7  aus/prof-st1/profile-info.json
2552e987de732cf1a12a6f4b6ffeeb55eceebb097a41417c28bbc5ec4f385ae7  aus/prof-st2/profile-info.json
```

Hilfsdateien (hilfs/):
- Kette kette.sh, Laufzeiten laufzeiten.sh.
- jq-Formatierer: versatz.jq (Schreibtischprobe vor dem Einfrieren; nachtraeglich auch fuer Rang k + 1), k1tab.jq,
  kurventab.jq (eine Zeile vor dem ersten Gebrauch per sed berichtigt), stellentab.jq, l0fenster.jq, paarweise.jq
  (nachtraeglich).
- Zwischenstaende: k1-tabelle*.md, stellen-tabelle*.md, laufzeiten-tabelle.md, v-je-nr.txt, l2-k-plus-1.json.

```
ee49e0b00e0bc6664599f9d452dad28ce2b99f0f2a71c745b322495ead9e17ef  hilfs/kette.sh
6d5d00eb23ea80dbf773a3cef0e7a98f9af9b6ebd1cc2e21dad0e931f6898525  hilfs/laufzeiten.sh
971fc9f31e16365ea14536d8d9d37e71a4be7d330326646c3ce56624c64786d0  hilfs/versatz.jq
3aec730bc8eb7a1dde8d5cac35b750cbc0e46325af8d661d9b88461960432a69  hilfs/k1tab.jq
4837f10b0399870cf4ffa460e1e4a3aeca39a83d1a79c3e9310e1331a8a08fbf  hilfs/kurventab.jq
703044d331bcc50a050d9e11da66e9830e035799ad63367f706de4e47cf66ef0  hilfs/stellentab.jq
cdb7df9050132549a5d785084ddf68f23899bc04247ce8795fc9349ed9b9fb49  hilfs/l0fenster.jq
7c43bd1f13a4d3163ae1004a4609935789232aa7dd9db472ccc6e7c0af2e0c28  hilfs/paarweise.jq
a502638bc90cacb3463efc57d096a617d00435c1d901999584630030e9beec3b  hilfs/l2-k-plus-1.json
2e756c5b2974090053b9b1f2588de2f22d66c3405b2126a60ceee896a7760282  hilfs/k1-tabelle.md
4eb53f42a36c14e9e681c6ca7d2b9ee5b152204188d48e2f5ed045a9e393dac3  hilfs/k1-tabelle-komma.md
0ebee9c5f9fd7568d91de12690537ec4d099bbb5e363e5d797f2d1469b0cbd37  hilfs/stellen-tabelle.md
49a15f1bf047151346a316120b0fac926ed7febcc4a69bd7608322b5c220db07  hilfs/stellen-tabelle-v.md
d0482d95aefc875423657eb8e983481808b7dbf15de08d473e79e877bd0d1e59  hilfs/laufzeiten-tabelle.md
3195f4c552a9ceda8be25436bafeae1c5f71b76fb225ebb64580891a136d7e17  hilfs/v-je-nr.txt
```

## 6 Einfach gesagt

Ein Q-Ball mit Huelle kann nicht nur atmen (groesser und kleiner werden) und kippen, sondern sich auch abwechselnd zur
Zigarre langziehen und zum Pfannkuchen plattdruecken; das ist eine Quadrupol-Schwingung. Wir haben gesucht, bei welchen
Ballgroessen diese Schwingung "still" ist, also keine Wellen nach aussen abgibt, und bei Baellen bis zum Radius 19
genau 15 solche Stellen gefunden, mit zwei verschieden feinen Rechengittern gleich. Sie liegen wieder auf Leitern mit
fast gleichen Sprossenabstaenden, nur sind die Abstaende hier rund 6 Prozent groesser als beim Atmen, mehr als
vorhergesagt. Gegenueber den Sprossen der Atmung sind sie um etwa zwei Drittel eines Abstands verschoben, ungefaehr
doppelt so weit wie beim Kippen; das passt zur Idee, dass die Verschiebung mit der Schwingungsform waechst. Weil eine
der drei Vorhersagen daneben lag, gilt die vorab formulierte Sprossenregel fuer alle Schwingungsformen nicht als
bestaetigt.
