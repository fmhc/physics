
## 2 Vorhersagen L1 bis L5

Gewertet nach PLAN Abschnitt 6 auf dem Bereich von PLAN-NACHTRAG-2 und -4: Paare 0 bis 109, Zeilen 0 bis 110,
omega^2 = 1,40 bis 0,763542 (R = 1,77 bis 38,95). Alle Zahlen gelten fuer beide Stufen (Stellen und Umlaeufe gleich).

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| L1 | Alle 15 bekannten Stellen wiedergefunden, Lage auf 1e-6 (90 %) | **eingetroffen** | 15 von 15 auf beiden Stufen: Zuordnung aus der eigenen Suche, Newton ab der eigenen Lage, Abstand zur Tabelle von Runde 17 hoechstens 7,9e-9 (Tabelle auf 8 Stellen gerundet), Rechteck-Umlauf aufgeloest (groesster Sprung 0,30 bis 0,40 rad, 64 bis 78 Randpunkte), Vorzeichen wie Runde 17, sigma2/sigma1 <= 8e-12 |
| L2 | Unter omega^2 = 0,819 mindestens 10 weitere Stellen (60 %) | **eingetroffen** | 72 neue Stellen mit omega^2 < 0,819 (bis 0,76406, Ende des gewerteten Bereichs) |
| L3 | Auf jeder der vier chi-Kurven werden die Stellen zur Schranke hin dichter (Abstaende in omega^2 nehmen ab) (70 %) | **eingetroffen** | Spearman(Delta omega^2, omega^2) = 1,0 auf k = 0, 1, 2, 3 (14, 15, 13, 11 Abstaende); Delta omega^2 faellt von 0,184 / 0,071 / 0,034 / 0,020 (oben) auf 0,0026 / 0,0021 / 0,0022 / 0,0023 (R ~ 37 bis 38) |
| L4 | Pro chi-Kurve Abstaende in R ungefaehr konstant, Streuung < 25 % (50 %) | **eingetroffen** | 8 Kurven mit >= 4 Stellen (k = 0 bis 7): CV = 0,015; 0,046; 0,056; 0,060; 0,041; 0,039; 0,034; 0,030. Mittlere Abstaende 2,43; 2,17; 2,22; 2,28; 2,30; 2,35; 2,41; 2,46 |
| L5 | Fuenfte oder weitere chi-Kurve mit Stellen bei kleinerem omega^2 (45 %) | **eingetroffen** | Kurven k = 4 bis 9 tragen Stellen (9, 8, 6, 5, 2, 1), erste bei omega^2 = 0,80363 (k = 4) |

- Nach der Karte gilt damit die Bedeutung "L2 bis L4 eingetroffen" (Abschnitt 1, Punkt 1), mit der Einschraenkung auf
  R <= 39.
- Zur Streuung (L4): Die Abstaende sind nicht zufaellig verteilt, sondern fallen auf den inneren Kurven langsam
  (k = 1: 2,48 -> 2,11; k = 3: 2,60 -> 2,16) und sind auf der Wandkurve k = 0 fast fest (2,55 -> 2,41). Die erste
  Stelle nach der Geburt einer Kurve hat jeweils den groessten Abstand.

## 3 Stellen

- **88 Stellen im gewerteten Bereich**, vollstaendige Liste in Anhang A (omega^2, rho, R und Umlauf, beide Stufen).
  - Jede ist ein Vorzeichenwechsel von s auf einer Kurve, auf beiden Stufen im selben Zeilenpaar gefunden, Zellen-Umlauf
    auf beiden Stufen gleich (+1: 44, -1: 44), ohne Merker. Keine Stelle nur auf einer Stufe, keine gepaarte Stelle mit
    Merker.
  - Lage beider Stufen: |d omega^2| <= 7,2e-9, |d rho| <= 6,0e-9, |d R| <= 1,0e-6.
  - Lage aus zwei Halbierungen nach den Unterzeilen: Klammer 1/32 des Zeilenabstands. Wo Newton nachgerechnet hat
    (L1, Stichprobe), lag die Halbierungslage auf <= 8,9e-7 in omega^2 (L1-10; sonst <= 1,6e-7) bzw. in der Stichprobe
    auf <= 2,1e-8 in omega^2 und <= 1,7e-7 in rho richtig.
  - "Groesster Phasensprung" gibt es nur beim Rechteck-Umlauf (L1, Stichprobe; Abschnitt 5). Der Zellen-Umlauf ist ein
    Vorzeichenprodukt (Plan 4), ohne Phasenrand.
- Bekannte Stellen: Nr. 1 bis 15 aus Runde 17 liegen in Anhang A mit ihrer alten Nummer (Spalte "bek.").
- **Neue Stelle im alten Fenster:** Nr. 13 in Anhang A, omega^2 = 0,82709373, rho = 1,29983132, k = 2, R = 14,19,
  Umlauf -1. STILLE-ZWEIFELD konnte sie nicht sehen: zwischen dessen Zeilen 0,81 und 0,83 wechselt s auf k = 2 zweimal
  (0,82709 und 0,81309). ZWEIFELD-NACHBAU rechnete erst ab 0,83.
- Ueber omega^2 = 1,1587 (R < 3,2) gibt es keine Stelle mehr; dort liegt nur die Wandkurve k = 0 in E1.

## 4 Kurven

- **Kriterium:** k = Rang der Nullstelle von m_bc in der Zeile, von unten gezaehlt (PLAN 4). Pruefungen im gewerteten
  Bereich: Die Zahl der Nullstellen nimmt zur Schranke hin nie ab; Zahl, Lage (auf 4,3e-10) und Vorzeichenfolge sind
  in allen 111 Zeilen auf beiden Stufen gleich; kein Rangsprung nach Plan-Regel; keine unsichere Nullstelle.
  - Knotenzahl der c-Komponente von Y_c auf (0, r_m] als Gegenprobe: monoton im Rang, aber nicht eindeutig (bei R = 39:
    0, 0, 2, 2, 4, 4, 4, 6, 6, 6 fuer k = 0 bis 9). Als Index ungeeignet; der letzte Knoten liegt offenbar oft jenseits
    r_m = r_half.
  - Zuordnung zu Runde 17: Kurven 1 bis 4 von ZWEIFELD-NACHBAU = k = 0 bis 3. k = 0 ist die Wandmode (rho 1,24 bei
    omega^2 = 1,40, faellt auf 1,027 bei R = 37), k >= 1 sind innere chi-Zustaende, die bei rho = sqrt2 entstehen und mit
    wachsendem R zum Boden des inneren chi-Topfs (m0 ~ 1,186 bei R = 39) absinken.
- **Geburt der Kurven** (erste Zeile mit k + 1 Nullstellen, rho ~ 1,41): k = 1 bei R = 4,7; 2: 8,76; 3: 12,47; 4: 16,11;
  5: 20,22; 6: 23,79; 7: 27,85; 8: 31,90; 9: 35,93. Abstand ~3,9 in R. Die erste Stelle folgt 0,1 bis 2,4 in R danach.

| k | Stellen | omega^2 oben .. unten | R oben .. unten | mittl. Abstand R | CV Abstand R | min / max Abstand R | Spearman (d omega^2, omega^2) | Umlauf wechselt |
|---|---|---|---|---|---|---|---|---|
| 0 | 15 | 1,15866 .. 0,765248 | 3,21 .. 37,18 | 2,427 | 0,015 | 2,410 / 2,551 | 1,0 | ja |
| 1 | 16 | 0,968506 .. 0,764059 | 5,92 .. 38,40 | 2,165 | 0,046 | 2,108 / 2,481 | 1,0 | ja |
| 2 | 14 | 0,881217 .. 0,764340 | 9,25 .. 38,11 | 2,220 | 0,056 | 2,127 / 2,562 | 1,0 | ja |
| 3 | 12 | 0,840150 .. 0,764820 | 12,56 .. 37,61 | 2,277 | 0,060 | 2,159 / 2,600 | 1,0 | ja |
| 4 | 9 | 0,803628 .. 0,765522 | 18,49 .. 36,92 | 2,303 | 0,041 | 2,206 / 2,478 | 1,0 | ja |
| 5 | 8 | 0,791932 .. 0,764195 | 21,82 .. 38,26 | 2,349 | 0,039 | 2,248 / 2,508 | 1,0 | ja |
| 6 | 6 | 0,783372 .. 0,765243 | 25,13 .. 37,19 | 2,411 | 0,034 | 2,322 / 2,530 | 1,0 | ja |
| 7 | 5 | 0,776836 .. 0,764180 | 28,45 .. 38,27 | 2,455 | 0,030 | 2,379 / 2,548 | 1,0 | ja |
| 8 | 2 | 0,768383 .. 0,765622 | 34,33 .. 36,82 | 2,492 | - | 2,492 | - | ja |
| 9 | 1 | 0,764781 | 37,65 | - | - | - | - | - |

- Lagen je Kurve (R der Stellen, Stufe 1; omega^2 in Anhang A):
  - k = 0: 3,21 5,76 8,21 10,64 13,06 15,48 17,90 20,31 22,72 25,13 27,54 29,95 32,37 34,77 37,18
  - k = 1: 5,92 8,40 10,68 12,89 15,06 17,21 19,35 21,48 23,61 25,73 27,84 29,96 32,07 34,18 36,29 38,40
  - k = 2: 9,25 11,81 14,19 16,47 18,71 20,91 23,10 25,27 27,42 29,57 31,71 33,85 35,98 38,11
  - k = 3: 12,56 15,16 17,60 19,94 22,23 24,49 26,71 28,92 31,11 33,29 35,45 37,61
  - k = 4: 18,49 20,97 23,36 25,70 27,99 30,25 32,49 34,71 36,92
  - k = 5: 21,82 24,32 26,75 29,12 31,44 33,74 36,01 38,26
  - k = 6: 25,13 27,66 30,12 32,51 34,87 37,19
  - k = 7: 28,45 31,00 33,47 35,89 38,27
  - k = 8: 34,33 36,82; k = 9: 37,65
- **Abbildungen** (aus/, Stufe 2 fuer die Kurven, Stellen aus der Zaehlung):
  - abb-stellen.png: "Stellen in (omega^2, rho) mit den chi-Kurven". Links der ganze gewertete Bereich, rechts der
    Duennwand-Ausschnitt 0,76 bis 0,83. Punkte: Nullstellen von m_bc je Zeile, Farbe = k (mod 10). Dreiecke: Stellen
    (auf: Umlauf +1, ab: -1). Sterne: die 15 Stellen aus Runde 17.
  - abb-abstand.png: "Abstand gegen R". Links Delta R benachbarter Stellen je Kurve gegen R (Mitte des Paares), rechts
    Delta omega^2 gegen omega^2 (logarithmisch).
  - Ablesbar: Delta R liegt fuer alle Kurven zwischen 2,1 und 2,6 und laeuft zu einem kurvenabhaengigen festen Wert
    (k = 0 ~ 2,41, innere Kurven von oben gegen ~ 2,1). Delta omega^2 faellt ueber zwei Groessenordnungen.
- **Schreibtisch-Abschaetzung [H]** (nicht gerechnet, nur Einsetzen): Im Balleinneren (g = 0, S = S0 mit
  U_S(S0) = omega^2) hat der a-b-Block eine schwingende Mode mit
  k_innen^2 = -[(Va - Ea + Va - Eb)/2 - sqrt(((Ea - Eb)/2)^2 + gs^2)], Va = omega^2 + S0 (3 S0 - 2), gs = S0 (3 S0 - 2),
  Ea = (w + rho)^2, Eb = (w - rho)^2.
  - Wandmode, letzte Stelle (omega^2 = 0,76525, rho = 1,02705, S0 = 1,2033): pi / k_innen = 2,368; gemessen 2,410.
  - k = 1, letzte Stelle (0,76406; 1,18834; S0 = 1,2025): 2,065; gemessen 2,108.
  - Kurvengeburten: Zahl der inneren chi-Zustaende ~ R sqrt(2 - m0^2) / pi, also eine neue Kurve je
    pi / sqrt(2 - 1,405) = 4,07 in R; gemessen ~ 3,9.
  - Lesart [H]: Die Kopplung der chi-Mode an die offene Welle sitzt in der Wand; dort hat die regulaere offene Welle die
    Phase k_innen R + konst. Jedes Mal, wenn diese Phase um pi waechst, wechselt die Kopplung ihr Vorzeichen und die
    Stelle ist still. Das ist die Mechanismus-Aussage der Karte; die 2 % Abweichung sind nicht untersucht.
