# KRUEMMUNGS-SANDHAUFEN-2D-2: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 49)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 12:04:14 CEST. Codekopie 12:10:55, Erweiterung ksh2.py bis 12:13:51, Plantext 12:14:31 bis
    12:16:51 CEST.
  - Rauchtests R1 bis R10 10:16:57 bis 10:22:50 UTC (gelesen: rc, Laufzeiten, Schluessel, Durchsatz fuer N_max).
  - **Eingefroren 12:23:30 CEST:** PLAN.md.eingefroren-20261005-122330 (sha256 34cdd988...), code/ksh2.py (16089955...),
    code/kette-cpu.sh (cccd4fda...), code/kette-cpu7.sh (f38c6c1e...). Liste EINGEFROREN-SHA256.txt. Alle sieben
    Lauf-JSON und urteile.json tragen ksh2.py 16089955...
  - Hauptlaeufe 10:23:46 bis 10:38:24 UTC, AUS 10:38:24 bis 10:38:48 UTC, alle rc = 0, keine Wiederholung.
    **Erste Sicht auf Werte 12:39:09 CEST.** Text ab 12:43:12 CEST, Textstand 12:47:34 CEST (date).
- Synthetische, kombinatorische Modellrechnung (Python 3.12.3, numpy 2.4.4, scipy 1.18.0, je 1 CPU-Kern der .69,
  ubuntu-auto), keine Messdatenbestaetigung.
- **Kennzeichen:** [E] gerechnet, [M] Mathematik, [P] Projektdatei (2D-1), [L] Literatur aus dem Gedaechtnis,
  [ES] eigener Schluss, [H] Hypothese, [N] Nachtrag nach Sicht (nur beschreibend, kein Urteil).
- **Begriffe:** s = Kipp-Flips je Lawine; s_c2 = <s^2>/<s> (Abschneiden); r = Wahrscheinlichkeit eines Zusatz-Antriebs
  nach jedem Kipp-Flip; Alter = Antriebsschritte seit Einschwingbeginn / N; W1 = gemeinsames Altersfenster aller Faelle
  einer Gruppe, W2 = dessen spaetere Haelfte (Drift-Probe); P2D = Planregel "Potenzgesetz ueber 2 Dekaden" (a bis e).

## 1. Zeiten und Laeufe

Arbeitsordner /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-2/, alle Laeufe ueber
/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh (1 Thread, RuntimeMaxSec 600). Nur Kugel, Arm Z.

| Lauf | Spur | Aufruf (ksh2.py lauf ..., bzw. aus2) | Start bis Ende (UTC) | Dienstlaufzeit | rc |
|---|---|---|---|---|---|
| R1 / R3 | cpu | N = 16000 / 32000, r = 0,01, Budget 100 s, Saat 91 / 93 (code-r1) | 10:16:57 bis 10:20:18 | je 1 min 41 s | 0 |
| R2 | cpu7 | N = 24000, r = 0,01, Budget 100 s, Saat 92 | 10:19:16 bis 10:20:57 | 1 min 41 s | 0 |
| R4 bis R9 | cpu7 | Kleinfaelle wie L6, L7, L5, L2, L3, L4 (Budget 10 bis 20 s) | 10:20:57 bis 10:22:24 | 10 bis 20 s | 0 |
| R10 | cpu | aus2 ueber R1, R4 bis R9 | 10:22:28 bis 10:22:50 | 21,7 s | 0 |
| L1 | cpu | N = 16000, r = 0,01, Budget 520, Saat 21 | 10:23:47 bis 10:32:23 | 8 min 36 s | 0 |
| L2 | cpu7 | N = 8000, r = 0,01, Budget 300, Saat 22 | 10:23:46 bis 10:28:47 | 5 min 1 s | 0 |
| L3 | cpu7 | N = 8000, r = 0,003, Budget 300, Saat 23 | 10:28:47 bis 10:33:17 | 4 min 30 s | 0 |
| L4 | cpu | N = 8000, r = 0,03, Budget 300, Saat 24 | 10:32:23 bis 10:37:24 | 5 min 1 s | 0 |
| L5 | cpu7 | N = 2000, r = 0,01, Budget 90, Saat 25 | 10:33:17 bis 10:34:48 | 1 min 30 s | 0 |
| L6 | cpu7 | N = 2000, r = 0, Budget 90, Saat 26 (KS0) | 10:34:48 bis 10:36:18 | 1 min 30 s | 0 |
| L7 | cpu | N = 2000, r = 0, Budget 60, Saat 11 (K-ID) | 10:37:24 bis 10:38:24 | 1 min 0 s | 0 |
| AUS | cpu | aus2 (Urteile, Drift-Probe, K-ID, Bilder) | 10:38:24 bis 10:38:48 | 23,1 s | 0 |

- Zahl der Laeufe: 9 Rauchlaeufe + 1 Rauch-Auswertung, 7 Hauptlaeufe + AUS = 18 kleintest-Aufrufe. Keine Abweichung
  von der Laufliste, kein Lauf wiederholt, keiner nach der Schlusszeit.
- **N_max = 16000:** Nach der Planregel (Durchsatz x 0,8) war keines von 16000, 24000, 32000 "machbar"
  (16000 knapp: 216 s statt hoechstens 208 s fuers Einschwingen); dann gilt das Kartenminimum 16000. Tatsaechlich
  brauchte L1 fuer das volle Einschwingen (160 000 Schritte) 169,7 s und erreichte 300 000 Messschritte.
- L4 (r = 0,03): Einschwingen zeitbegrenzt (66 460 von 80 000 Schritten), Messung 96 000 Schritte (Budget).

## 2. Ergebnis zuerst

1. **Die Kontrollen halten [E].** KS0 ist eingetroffen: Mit neuer Saat gibt N = 2000, r = 0 s_c2 = 722 statt 830
   (-13 %, Grenze 15 %). Der Lauf mit Saat 11 (K-ID) gibt die Lawinenfolge aus 2D-1 ueber 136 126 Schritte bitgleich
   wieder. Alle Lawinen enden von selbst, alle Strukturpruefungen sind fehlerfrei.
2. **Das Abschneiden waechst mit N, aber nicht nachweislich mit D >= 0,3 (KS1 nach Plan nicht entscheidbar, nach
   Wortlaut nicht eingetroffen) [E].** Bei r = 0,01 ist s_c2 = 1 339 / 2 117 / 2 384 fuer N = 2000 / 8000 / 16000,
   D = 0,285 [0,166; 0,398]. Die Drift-Probe gibt in beiden Altersfenstern dasselbe D (0,280 und 0,283). Das Wachstum
   wird langsamer: lokal 0,33 von 2000 nach 8000, 0,17 von 8000 nach 16000 [N].
3. **Die Antriebsrate bleibt ein versteckter Regler (KS2 nach Plan nicht entscheidbar, nach Wortlaut nicht
   eingetroffen) [E].** Bei N = 8000 ist s_c2(0,01) / s_c2(0,003) = 1,58 [1,37; 1,86]. Mit r = 0,03 springt s_c2 auf
   13 050, das 6,2-Fache. Gegen r = 0 aus 2D-1 [P] (989) aendert schon r = 0,003 s_c2 um das 1,35-Fache [N].
4. **Die Gradverteilung ist fest bei je einem Drittel (KS3 eingetroffen) [E].** In allen sechs Kugelfaellen
   (N = 2000 bis 16000, r = 0 bis 0,03) gilt rho5 / rho6 / rho7 = 0,334 bis 0,337 / 0,332 bis 0,333 / 0,330 bis 0,334,
   in beiden Messhaelften gleich. Der Zustand ist schon beim ersten Zeitreihenpunkt erreicht (1000 Antriebsschritte
   nach der Anfangsrelaxation, bei N = 16000 Alter 0,06) [N].
   [M, nach Sicht]: Im stabilen Zustand gibt es nur die Grade 5, 6 und 7, und rho5 - rho7 = 12/N. KS3 prueft also nur
   eine freie Zahl, rho6.
5. **Kein sauberes Potenzgesetz beim groessten N (KS4 nicht eingetroffen) [E].** Bei N = 16000 sieht P(s) ueber etwa
   drei Dekaden potenzgesetzartig aus: tau = 1,363, s_c = 1 703, M1 schlaegt die gestreckte Exponentialfunktion um
   dAIC 7 281. Es scheitert aber an der Fitguete 0,174 > 0,15 (zweite Haelfte 0,182), wie 2D-1 bei N = 8000 (0,167).

## 3. Urteile

Mechanisch durch code/ksh2.py aus2 (eingefroren 12:23:30 CEST), aus-69/urteile.json; Regeln PLAN 4 bis 8. "Nach Plan"
= Intervallregel und Drift-Probe (Hauptschaetzer, W1, W2 muessen uebereinstimmen). "Nach Kartenwortlaut" =
Punktschaetzer der ganzen Messung.

| Nr | Vorhersage (Karte, woertlich) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] und Vorbehalte |
|---|---|---|---|---|---|
| KS0 | Kontrolle [P]: Mit denselben Einstellungen gibt die Kugel bei N = 2000 das s_c2 aus KRUEMMUNGS-SANDHAUFEN-2D-1 auf 15 % wieder | 85 % | **eingetroffen** | **eingetroffen** | s_c2 = 721,7 [642,3; 828,4] (Saat 26) gegen 830,1 (2D-1, Saat 11); Q = 0,869, also -13,1 %. Gleiche Einstellungen, neue Dynamik-Saat (PLAN 2). Vorbehalt: Die 15 % liegen in der Groesse des 95-%-Intervalls von s_c2 |
| KS1 | [H] Auf der Kugel waechst s_c2 bei r = 0,01 mit N wie N^D, D >= 0,3 (N = 2000, 8000 und das groesste in 10 min machbare N, mindestens 16000) | 50 % | **nicht entscheidbar** | **nicht eingetroffen** | N = 2000 / 8000 / 16000: s_c2 = 1 339,4 / 2 117,1 / 2 383,7, streng steigend. D = 0,285 [0,166; 0,398] (Hauptschaetzer), 0,280 [0,164; 0,384] (W1, Alter 10 bis 28,75), 0,283 [0,144; 0,450] (W2, Alter 19,4 bis 28,75). Alle drei "nicht entscheidbar", also keine Drift-Wirkung. Zweitschaetzer D(M1) = 0,258 |
| KS2 | [H] Bei N = 8000 aendert sich s_c2 zwischen r = 0,003 und r = 0,01 um weniger als den Faktor 1,5 (Grenzwert fuer kleine Rate) | 50 % | **nicht entscheidbar** | **nicht eingetroffen** | Q = s_c2(0,01) / s_c2(0,003) = 2 117,1 / 1 339,9 = 1,580 [1,371; 1,858]; W1 1,565 [1,355; 1,823]; W2 1,726 [1,402; 2,152]. Alle Punktschaetzer ueber 1,5, alle Intervalle schneiden 1,5 |
| KS3 | [H] Im stationaeren Zustand liegt der Anteil der Grade 5, 6 und 7 auf der Kugel je zwischen 0,25 und 0,40, fuer alle gerechneten N | 60 % | **eingetroffen** | **eingetroffen** | Sechs Kugelfaelle L1 bis L6: rho5 0,3344 bis 0,3367, rho6 0,3319 bis 0,3333, rho7 0,3303 bis 0,3337; zweite Messhaelfte jeweils um weniger als 0,001 anders. [M, nach Sicht]: nur rho6 ist frei (Abschnitt 4.4) |
| KS4 | [H] Beim groessten N folgt P(s) auf der Kugel ueber mindestens 2 Dekaden einem Potenzgesetz (Fitguete <= 0,15 und Potenzgesetz vor gestreckter Exponentialfunktion um dAIC > 10) | 35 % | **nicht eingetroffen** | **nicht eingetroffen** | N = 16000, r = 0,01: P2D "nein" nur wegen (c): Fitguete 0,174 (24 Bins) > 0,15; zweite Haelfte ebenso (0,182). Erfuellt: dAIC(M3 - M1) = +7 281, dAIC(M2 - M1) = +382 427, s_c = 1 702,5 >= 200, 10 270 Lawinen mit s >= 200, kein Abbruch. tau = 1,363 [1,359; 1,366]. Eichung (BTW) aus 2D-1 [P] |

- **K-ID (Code-Kontrolle, PLAN 1):** identisch. s, T, A und Status gleich ueber 136 126 Messschritte; Anfangsrelaxation,
  Einschwingschritte (20 000), Netz (Saat 3000, Kantenzahl) und alle Zeitreihenzeilen (136 Messung, 20 Einschwingen,
  ohne die neue Spalte) gleich. Die Neuberechnung der Vorlage aus ihren Rohdaten gibt s_c2 = 830,0858, gleich dem
  veroeffentlichten Wert.
- **Bedeutung nach Karte (vorab festgelegt):**
  - "KS1, KS2 und KS4 treffen ein": **nicht ausgeloest.**
  - "KS1 verfehlt: Die breiten Lawinen waren ein Effekt endlicher Groesse": **nach Wortlaut ausgeloest, nach Plan
    offen.** Der Satz ist zu stark. s_c2 waechst in allen drei Schaetzern mit N; die untere 95-%-Grenze von D liegt bei
    0,14 bis 0,17, also ueber null.
  - "KS2 verfehlt: Der Zustand haengt an der Antriebsrate ...": **nach Wortlaut ausgeloest, nach Plan offen.**
    Beschreibend gestuetzt durch r = 0,03 (das 6,2-Fache). Einschraenkung: An r haengt die Lawinenstatistik, die
    Gradverteilung haengt nicht an r (KS3).
  - "Nur 2D und nur Kombinatorik: keine Folge fuer Lambda oder Schwerewellen": gilt.

## 4. Tabellen

### 4.1 Faelle (aus-69/urteile.json; P2D-Bedingungen PLAN 4)

| Fall | Mess-schritte | Lawinen s >= 1 | Anteil s = 0 | <s> | s_max | Abbruch | tau M1 [95 %] | s_c M1 | s_c2 [95 %] | dAIC M2-M1 | dAIC M3-M1 | (c) (Bins) | n(s >= 200) | P2D (verletzt) | Drift z | Einschwingen | Alter Ende |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L6 N2000 r0 (KS0) | 213 068 | 175 772 | 0,175 | 30,57 | 7 243 | 0 | 1,326 [1,317; 1,335] | 580,9 | 721,7 [642,3; 828,4] | 180 856 | -263 | 0,160 (19) | 5 198 | nein (a, c) | 0,06 | 20 000 | 116,5 |
| L5 N2000 r0,01 | 164 604 | 135 913 | 0,174 | 40,53 | 16 230 | 0 | 1,347 [1,340; 1,352] | 1 022,8 | 1 339,4 [1 144,9; 1 569,3] | 175 331 | +1 632 | 0,178 (22) | 4 904 | nein (c) | 1,60 | 20 000 | 92,3 |
| L2 N8000 r0,01 | 292 499 | 241 490 | 0,174 | 50,23 | 21 276 | 0 | 1,366 [1,360; 1,370] | 1 623,5 | 2 117,1 [1 880,2; 2 349,5] | 367 350 | +6 916 | 0,181 (24) | 9 915 | nein (c) | 0,94 | 80 000 | 46,6 |
| L1 N16000 r0,01 | 300 000 | 247 749 | 0,174 | 52,26 | 42 523 | 0 | 1,363 [1,359; 1,366] | 1 702,5 | 2 383,7 [2 021,6; 2 834,2] | 382 427 | +7 281 | 0,174 (24) | 10 270 | nein (c) | 0,02 | 160 000 | 28,75 |
| L1, zweite Haelfte | 150 000 | 123 770 | 0,175 | 52,31 | 36 781 | 0 | 1,363 [1,358; 1,368] | 1 702,4 | 2 393,6 [1 971,3; 2 776,6] | 191 338 | +3 613 | 0,182 (24) | 5 167 | nein (c) | 0,08 | - | 28,75 |
| L3 N8000 r0,003 | 300 000 | 247 602 | 0,175 | 39,19 | 16 621 | 0 | 1,351 [1,346; 1,354] | 990,7 | 1 339,9 [1 203,2; 1 476,0] | 315 107 | +2 281 | 0,170 (21) | 8 674 | nein (c) | 0,91 | 80 000 | 47,5 |
| L4 N8000 r0,03 | 96 000 | 79 280 | 0,174 | 153,03 | 79 482 | 0 | 1,396 [1,393; 1,399] | 13 147,6 | 13 050,5 [10 716,1; 14 907,9] | 216 372 | +9 927 | 0,253 (32) | 4 729 | nein (c) | 0,79 | 66 460 (zeitbegrenzt) | 20,3 |

- Alle Kugelfaelle: 100 % der Lawinen enden stabil (Status 0), kein Abbruch, kein blockierter Versuch (0), keine
  instabile Ecke am Ende. KH0-artige Pruefungen [E]: 1 792 637 Schritte ohne Verletzung (Summe q = 12, Grad >= 3,
  Kantenzahl, Doppelkante), 919 volle Strukturpruefungen fehlerfrei.
- Anfangsrelaxation: s = 2 232 (N = 2000) bis 25 060 (N = 16000) Flips, immer stabil beendet.
- Zusatzantriebe (ganzer Fall): 36 241 (r = 0,003), 60 468 / 150 084 / 188 785 (r = 0,01; N = 2000 / 8000 / 16000),
  599 927 (r = 0,03).
- Die Intervalle der Faelle stammen aus dem Bootstrap der Vorlage (analyse_fall); die Fensterwerte in 4.3 aus eigenen
  unabhaengigen Ziehungen. Daher weichen die Intervalle des Hauptschaetzers dort leicht ab (z. B. L2 [1 899; 2 372]).

### 4.2 s_c2 je N und r (Hauptschaetzer, 95 %)

| r | N = 2000 | N = 8000 | N = 16000 |
|---|---|---|---|
| 0 (2D-1, Saat 11) [P] | 830,1 [729,1; 978,2] | 988,9 [863,3; 1 120,8] | - |
| 0 (2D-2, Saat 26, KS0) | 721,7 [642,3; 828,4] | - | - |
| 0,003 | - | 1 339,9 [1 203,2; 1 476,0] | - |
| 0,01 | 1 339,4 [1 144,9; 1 569,3] | 2 117,1 [1 880,2; 2 349,5] | 2 383,7 [2 021,6; 2 834,2] |
| 0,03 | - | 13 050,5 [10 716,1; 14 907,9] (Einschwingen zeitbegrenzt) | - |

- [N, Kopfrechnung] Quotienten bei N = 8000: r 0,003 / 0 = 1,35; 0,01 / 0,003 = 1,58; 0,03 / 0,01 = 6,16; 0,01 / 0 = 2,14.
  Der Zuwachs gegen r = 0 ist 351 bei r = 0,003 und 1 128 bei r = 0,01, also etwa proportional zu r (Faktor 3,2 bei
  Faktor 3,3 in r). Linear fortgesetzt (Steigung etwa 1,2 * 10^5) waere die Verschiebung gegen r = 0 erst unter
  r ~ 0,001 kleiner als etwa 12 %. Das stuetzt sich auf r = 0 aus einem anderen Lauf (2D-1, andere Saat).
- [N] Lokale Steigungen: r = 0,01: 0,33 (2000 -> 8000) und 0,17 (8000 -> 16000). r = 0 [P]: 0,13 (2D-1) bzw. 0,23
  (mit dem KS0-Wert) von 2000 nach 8000. Der Zusatzantrieb verstaerkt also auch die N-Abhaengigkeit.

### 4.3 Drift-Probe (Pflicht, PLAN 6)

KS1 (r = 0,01), D je Schaetzer:

| Schaetzer | Alter | Lawinen N = 2000 / 8000 / 16000 | s_c2 N = 2000 / 8000 / 16000 [95 %] | D [95 %] | D [68 %] | Urteil |
|---|---|---|---|---|---|---|
| Haupt | ganze Messung (Ende 92,3 / 46,6 / 28,75) | 135 913 / 241 490 / 247 749 | 1 339,4 / 2 117,1 / 2 383,7 | 0,285 [0,166; 0,398] | [0,216; 0,342] | nicht entscheidbar |
| W1 | 10 bis 28,75 | 31 003 / 123 837 / 247 749 | 1 330,7 [1 083; 1 563] / 1 961,6 [1 709; 2 291] / 2 383,7 [2 098; 2 784] | 0,280 [0,164; 0,384] | [0,230; 0,334] | nicht entscheidbar |
| W2 | 19,38 bis 28,75 | 15 454 / 61 776 / 123 770 | 1 361,8 [1 015; 1 713] / 2 220,7 [1 791; 2 643] / 2 393,6 [2 022; 2 860] | 0,283 [0,144; 0,450] | [0,193; 0,381] | nicht entscheidbar |

KS2 (N = 8000), Quotient s_c2(r = 0,01) / s_c2(r = 0,003):

| Schaetzer | Alter | s_c2(0,01) [95 %] | s_c2(0,003) [95 %] | Q [95 %] | Urteil |
|---|---|---|---|---|---|
| Haupt | ganze Messung | 2 117,1 [1 899,4; 2 372,4] | 1 339,9 [1 209,0; 1 489,6] | 1,580 [1,371; 1,858] | nicht entscheidbar |
| W1 | 10 bis 46,56 | 2 117,1 [1 904,3; 2 359,5] | 1 352,9 [1 213,1; 1 471,1] | 1,565 [1,355; 1,823] | nicht entscheidbar |
| W2 | 28,28 bis 46,56 | 2 254,3 [1 917,1; 2 642,8] | 1 306,1 [1 115,0; 1 516,3] | 1,726 [1,402; 2,152] | nicht entscheidbar |

Viertel der Messung je Fall (<s> hier ueber alle Schritte, auch s = 0):

| Fall | s_c2 je Viertel | <s> je Viertel | Alter am Viertelende | Planflag Drift (z) |
|---|---|---|---|---|
| L6 N2000 r0 | 654 / 741 / 799 / 692 | 24,5 / 25,9 / 25,0 / 25,5 | 36,6 / 63,3 / 89,9 / 116,5 | nein (0,06) |
| L5 N2000 r0,01 | 1 302 / 1 785 / 1 147 / 1 095 | 34,7 / 34,6 / 32,6 / 32,1 | 30,6 / 51,2 / 71,7 / 92,3 | nein (1,60) |
| L2 N8000 r0,01 | 1 651 / 2 260 / 2 021 / 2 474 | 38,2 / 42,8 / 41,1 / 43,8 | 19,1 / 28,3 / 37,4 / 46,6 | nein (0,94) |
| L1 N16000 r0,01 | 2 885 / 1 808 / 2 135 / 2 653 | 45,3 / 41,0 / 43,2 / 43,1 | 14,7 / 19,4 / 24,1 / 28,8 | nein (0,02) |
| L3 N8000 r0,003 | 1 204 / 1 583 / 1 143 / 1 406 | 31,2 / 34,4 / 31,7 / 32,1 | 19,4 / 28,8 / 38,1 / 47,5 | nein (0,91) |
| L4 N8000 r0,03 | 12 089 / 14 565 / 10 925 / 14 207 | 125,0 / 136,6 / 112,4 / 131,5 | 11,3 / 14,3 / 17,3 / 20,3 | nein (0,79) |

- Kein Fall zeigt einen gerichteten Trend wie die Scheibe in 2D-1 (79 -> 40). Die Viertel schwanken um bis zu
  +-25 %, ohne Richtung; das passt zum schweren Schwanz von P(s). Die Drift-Probe hat kein Urteil veraendert.

### 4.4 Gradverteilung im stationaeren Zustand (Mittel ueber die Zeitreihe der Messung, alle 1000 Schritte)

| Fall | rho5 | rho6 | rho7 | rho4, rho8, Rest | 2 rho5 + rho7 | rho5 + 2 rho7 | zweite Haelfte rho5 / rho6 / rho7 | Zeilen | KS3 je Fall |
|---|---|---|---|---|---|---|---|---|---|
| L6 N2000 r0 | 0,3367 | 0,3326 | 0,3307 | 0 | 1,004 | 0,998 | 0,3368 / 0,3325 / 0,3308 | 213 | eingetroffen |
| L5 N2000 r0,01 | 0,3363 | 0,3333 | 0,3303 | 0 | 1,003 | 0,997 | 0,3367 / 0,3326 / 0,3307 | 164 | eingetroffen |
| L2 N8000 r0,01 | 0,3347 | 0,3321 | 0,3332 | 0 | 1,003 | 1,001 | 0,3347 / 0,3322 / 0,3332 | 292 | eingetroffen |
| L1 N16000 r0,01 | 0,3344 | 0,3319 | 0,3337 | 0 | 1,003 | 1,002 | 0,3344 / 0,3320 / 0,3336 | 300 | eingetroffen |
| L3 N8000 r0,003 | 0,3346 | 0,3322 | 0,3331 | 0 | 1,002 | 1,001 | 0,3348 / 0,3318 / 0,3333 | 300 | eingetroffen |
| L4 N8000 r0,03 | 0,3346 | 0,3322 | 0,3331 | 0 | 1,002 | 1,001 | 0,3349 / 0,3317 / 0,3334 | 96 | eingetroffen |

- [M, nach Sicht] Die Zeitreihe wird nach dem Ende einer Lawine gelesen. Dann ist keine Ecke instabil, es gibt also
  nur die Grade 5, 6 und 7 (rho4 = rho8 = 0 bestaetigt das), und rho5 + rho6 + rho7 = 1. Auf der Kugel gilt ausserdem
  Summe q = 12, also rho5 - rho7 = 12/N (gemessen: 0,0060 bei N = 2000, 0,0007 bei N = 16000). Frei ist nur rho6.
  Die drei Bedingungen der Karte sind also eine Bedingung an rho6; das stand weder in der Karte noch im Plan.
- [N] Bild bild-grad-zeitreihe.png: Alle drei Anteile liegen schon beim ersten Zeitreihenpunkt des Einschwingens
  (nach 1000 Antriebsschritten; Alter 0,06 bei N = 16000, 0,5 bei N = 2000) bei etwa 0,33. Sie bleiben dort bis zum
  Ende, mit Schwankungen von etwa +-0,02 bei N = 2000 und weniger bei grossem N. Einen Punkt direkt nach der
  Relaxation gibt es nicht. Das Drittel entsteht also schnell (Relaxation und erste Antriebsschritte), nicht langsam durch
  den Antrieb.
- [ES, Kopfrechnung aus 2D-1] Die grobe Verzweigungszahl 2 rho5 + rho7 ist gleich 1 + rho5 - rho6. Bei je einem
  Drittel ist sie genau 1: Jeder Kipp-Flip aendert drei weitere Ecken um einen Grad, und jede ist mit
  Wahrscheinlichkeit 1/3 an der passenden Kante des Bandes {5, 6, 7}.

### 4.5 Fits (beschreibend; M1 auf s >= 2, dazu Dauer T und Flaeche A)

| Fall | tau (s) | beta (M3) | tau_T | <T> | T_max | tau_A | <A> | A_max |
|---|---|---|---|---|---|---|---|---|
| L6 N2000 r0 | 1,326 | 0,231 | 1,123 | 14,1 | 618 | 1,320 | 17,0 | 1 059 |
| L5 N2000 r0,01 | 1,347 | 0,228 | 1,168 | 15,4 | 797 | 1,378 | 21,6 | 1 561 |
| L2 N8000 r0,01 | 1,366 | 0,226 | 1,207 | 16,7 | 889 | 1,427 | 26,1 | 3 713 |
| L1 N16000 r0,01 | 1,363 | 0,225 | 1,204 | 16,9 | 1 277 | 1,428 | 27,4 | 7 119 |
| L3 N8000 r0,003 | 1,351 | 0,228 | 1,170 | 15,3 | 750 | 1,382 | 20,6 | 2 366 |
| L4 N8000 r0,03 | 1,396 | 0,218 | 1,316 | 23,5 | 1 870 | 1,478 | 67,7 | 7 388 |

- [N] Fitguete (c) bei N = 16000, Bins mit mindestens 100 Lawinen bis s_c/2 = 851: Bei s = 2 liegen die Daten um
  10^-0,174 unter M1, von s = 5 bis 30 um bis zu 10^+0,10 darueber, von s = 200 bis 630 um 10^-0,13 bis 10^-0,17
  darunter. Die Abweichung ist also eine Kruemmung von log P(s), kein Rauschen. Auch ohne s = 2 laege (c) bei 0,172.
- Die Methode schaetzte das BTW-tau in 2D-1 mit 1,07 statt 1,2 bis 1,3 [P, L]; die tau-Werte sind darum nicht als
  Modellexponent zu lesen.

### 4.6 Abbildungen (aus-69/)

- bild-Ps-kugel-r0.01.png: P(s) fuer N = 2000 / 8000 / 16000 bei r = 0,01 mit M1-Fit. Die drei Kurven liegen bis
  s ~ 2 000 aufeinander; danach endet N = 2000 zuerst, N = 16000 reicht bis s ~ 4 * 10^4. Der Schwanz liegt ueber den
  M1-Kurven.
- bild-Ps-kugel-N8000-rate.png: r = 0,003 / 0,01 / 0,03 bei N = 8000. Gleich bis s ~ 300, dann wandert das Abschneiden
  mit r. r = 0,03 reicht bis s ~ 8 * 10^4, mit einem Buckel am Ende.
- bild-Ps-ks0.png: 2D-1 (Saat 11) gegen 2D-2 (Saat 26), N = 2000, r = 0. Deckungsgleich bis s ~ 3 000; Unterschiede nur
  in den letzten Bins (Einzelereignisse).
- bild-grad-zeitreihe.png: rho5, rho6, rho7 gegen das Alter fuer alle sechs Faelle, mit dem KS3-Band.
- bild-sc2-N.png: s_c2 gegen N bei r = 0,01 fuer Hauptschaetzer, W1 und W2, mit Ausgleichsgeraden.

## 5. Bedeutung [H, ES]

- **Fuer Finns Regel ("Kruemmung wird umverteilt"):**
  - Auf der geschlossenen Kugel gibt die Regel Lawinen, die immer von selbst enden und ueber etwa drei Dekaden breit
    verteilt sind. Das Abschneiden waechst mit N, aber langsam (D ~ 0,28, lokal fallend). Ein sauberes Potenzgesetz
    nach Plan gibt es weder bei 8000 (2D-1) noch bei 16000. Belastbar ist hoechstens "quasi-kritisch" [H].
  - Die Lawinengroesse haengt deutlich an der Antriebsrate. Schon r = 0,003 vergroessert s_c2 gegen r = 0 um etwa
    ein Drittel [N]. Nach dem SOC-RAUM-L-Kriterium [P] ist das eine versteckte Abstimmung. Fuer eine SOC-Aussage
    braeuchte es eine N-Reihe bei r = 0. Die vorhandenen r = 0-Werte (2D-1 und KS0) wachsen von 2000 nach 8000 nur mit
    D ~ 0,13 bis 0,23 [N].
  - Die Gradverteilung ist dagegen robust: je ein Drittel Grad 5, 6, 7, gleich fuer alle N und r. [H] Ein Drittel je
    Grad ist die Verteilung groesster Entropie auf {5, 6, 7} mit Mittel 6. Genau dort ist die grobe Verzweigungszahl
    3 * 1/3 = 1. Dann waere "Verzweigung 1" eine Abzaehl-Eigenschaft der Regel (Bandbreite 3, drei weitere Ecken je
    Flip), keine dynamische Selbstorganisation. Dazu passt, dass das Drittel schon beim ersten Zeitreihenpunkt
    erreicht ist.
  - [H] Pruefvorschlag: dieselbe Regel mit breiterem stabilen Band, z. B. Grad 4 bis 8. Dort gaebe die groesste
    Entropie 1/5 je Grad und die grobe Verzweigung 3/5. Werden die Lawinen dann klein, ist die Abzaehl-Erklaerung
    gestuetzt.
- **Fuer die 3D-Fassung (SOC-UMKLAPP-1) [H]:**
  - Vor einem Bau lohnt die Schreibtischrechnung "Zahl der von einem Zug betroffenen Elemente mal Wahrscheinlichkeit an
    der Bandkante". In 2D ergibt sie 3 * 1/3 = 1. In 3D haengt sie an der Bandbreite der Kantengrade und an der Zahl
    der Kanten, die ein 2-3- oder 3-2-Zug aendert. Dazu kommt die Frustration aus 2D-1 (kein Kantengrad mit
    Fehlwinkel null).
  - Die Antriebsrate muss gegen null gehen. In 2D aendert schon r = 0,003 die Statistik messbar.
  - Die geschlossene Flaeche ohne Senke bleibt der interessantere Fall (2D-1).
- **Nicht betroffen:** Lambda, Schwerewellen, Finns 3D-Netz. Das ist eine kombinatorische 2D-Vorstufe.

## 6. Selbstanzeigen und Negativliste

### 6.1 Selbstanzeigen

1. **Geschaetzte Uhrzeit im eingefrorenen Plan:** Der Kopf von PLAN.md nennt "Vorlage gelesen bis ~12:10". Diese Zeit
   ist geschaetzt, nicht per date gemessen. Das verstoesst gegen die Zeitregel; sie steht auch in der eingefrorenen
   Kopie. Ausserdem nennt PLAN 11 fuer den Start der cpu7-Rauchkette 10:19:18 UTC. Das ist die date-Ausgabe meiner
   Pruefung 2 s nach dem Start; laut Log startete R2 um 10:19:16.
2. **Dateien unter /tmp/claude-1000:** Das Werkzeug hat Ausgabedateien unter /tmp/claude-1000/.../tasks/ angelegt:
   b3mn55flx (haengender ssh-Startbefehl der Rauchketten), bq61k1w4c (Warteschleife), Monitore behquq7l3, ble66k4eo,
   bikxppm56. Inhalt: nur Kettenzeilen (rc, Zeiten) und eine Fehlermeldung zur Umleitung.
3. **Startfehler der Rauchketten:** In einem ssh-Aufruf lief mkdir im Hintergrundteil, waehrend die zweite Umleitung
   den Ordner schon brauchte. Die cpu7-Rauchkette startete darum erst 2 min 19 s spaeter von Hand; der erste
   ssh-Aufruf hing im Hintergrund, bis die cpu-Kette fertig war. Kein Einfluss auf Laeufe oder Werte.
4. **Lock-Probe:** Vor dem ersten Lauf habe ich mit `flock -n` geprueft, ob die Spuren cpu und cpu7 frei sind. Dabei
   wurde jeder Lock kurz gehalten, ausserhalb von kleintest.sh.
5. **Indirekte Sicht im Rauchtest (geplant):** Die Durchsatzzahlen aus R1 bis R3 (Schritte je Sekunde) haengen ueber
   <s> mittelbar an der Lawinenstatistik. Sie wurden fuer N_max gelesen, wie in PLAN 11 angekuendigt.
6. **Aenderungen nach dem Rauchtest:** bild_sc2_N klemmt negative Fehlerbalken (vor dem Einfrieren, in PLAN 11).
   Die diff-Datei habe ich 6 s nach dem Schreiben der Einfrierliste neu erzeugt (vermerkt in EINGEFROREN-SHA256.txt;
   Dokumentation, kein Laufcode).
7. **Werkzeuge:** Lokal kein python, awk, perl oder bc. Code- und Planbearbeitung mit Edit, Write und sed; Rechnungen
   im Text sind Kopfrechnung. jq nur lesend, lokal und auf der .69. Auf der .69 kein python ausserhalb von
   kleintest.sh, kein awk.
8. **Planschwaechen, nach Sicht nicht korrigiert:**
   - (a) KS3 prueft nur eine freie Zahl (rho6, Abschnitt 4.4); das Band 0,25 bis 0,40 war damit sehr weit.
   - (b) Die KS0-Toleranz von 15 % liegt in der Groesse des 95-%-Intervalls von s_c2; der neue Wert liegt bei -13 %.
   - (c) Die Intervallregeln fuer KS1 und KS2 machten "nicht entscheidbar" bei ~250 000 Lawinen mit schwerem Schwanz
     wahrscheinlich; mehr N- oder Saat-Wiederholungen haetten die Intervalle verengt.
   - (d) L4 (r = 0,03) hatte ein zeitbegrenztes Einschwingen und nur 96 000 Messschritte; er dient nur der
     Beschreibung und KS3.
   - (e) KS1 laeuft wie in der Karte bei r = 0,01. Der Rateneffekt (KS2) steckt damit auch in der N-Reihe.
   - Die Urteile bleiben mechanisch.
9. **Nachtraege nach Sicht** (alle [N], beschreibend, kein Urteil): Quotienten und lokale Steigungen (4.2), die
   Bindungen rho5 + rho6 + rho7 = 1 und rho5 - rho7 = 12/N (4.4), das Drittel direkt nach der Relaxation (Bild), das
   Muster der Fitguete-Abweichung (4.5), die Entropie-Hypothese und der Pruefvorschlag (5). Kein Lauf nach der Sicht.
10. **Literatur aus dem Gedaechtnis [L]:** BTW-tau 1,2 bis 1,3 (aus 2D-1 uebernommen), ungeprueft.
11. Kein Lesen von ~/.secrets, ~/.openclaw/workspace/secrets oder ~/.codex/auth.json; nichts Versiegeltes geoeffnet; kein
    grep oder find ueber Projektordner (nur ueber eigene Dateien). Geschrieben nur im Kartenordner und in
    /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-2/. KARTE.md und der Ordner der Vorlage sind unveraendert;
    die Vorlage auf der .69 wurde nur gelesen (aus2 --ref). Zeiten per date, Laufzeiten aus den kleintest-Logzeilen.

### 6.2 Negativliste (darf nach dem Befund NICHT gesagt werden)

- "Finns Regel ist selbstorganisiert kritisch" bzw. "SOC gezeigt": nicht gezeigt. KS1 und KS2 sind nach Plan offen
  und nach Wortlaut nicht eingetroffen, KS4 ist nicht eingetroffen.
- "Die breiten Lawinen sind nur ein Endlichkeitseffekt": ebenfalls nicht gezeigt; s_c2 waechst mit N.
- "D = 0,285 ist der Skalenexponent": drei N unter einer Dekade, lokale Steigung fallend.
- "Es gibt einen Grenzwert fuer kleine Rate": nicht gezeigt; Faktor 1,58 zwischen r = 0,003 und 0,01.
- "Die Gradverteilung ordnet sich durch den Antrieb langsam selbst zu je 1/3": Das Drittel steht schon beim ersten
  Zeitreihenpunkt (1000 Antriebsschritte nach der Relaxation), und
  KS3 prueft nur rho6.
- "Verzweigungszahl 1 ist bewiesen" oder "erklaert Kritikalitaet": grobe Mittelfeld-Kopfrechnung, die
  Entropie-Erklaerung ist eine Hypothese.
- "tau = 1,36 ist der Modellexponent": Methodenverzerrung (BTW 1,07) und Fitguete verfehlt.
- "Die Kugel hat ein Potenzgesetz ueber 2 Dekaden": nach Plan nein (Fitguete 0,174).
- "KS0 bestaetigt die Messung": KS0 ist eine Wiederholbarkeitskontrolle innerhalb von 13 %, keine Messdatenpruefung.
- Jede Aussage zu Lambda, Schwerewellen oder Finns 3D-Netz.

## 7. Einfach gesagt

Wir haben das Dreiecksnetz auf der Kugel noch einmal gerechnet, jetzt bis 16 000 Ecken, und dabei auch geaendert, wie
oft waehrend einer Lawine nachgeschubst wird. Die Lawinen werden mit groesserem Netz zwar groesser, aber langsamer als
vorhergesagt, und ob das Wachstum reicht, koennen unsere Daten nicht sicher entscheiden. Wie gross die Lawinen werden,
haengt deutlich davon ab, wie oft man nachschubst; das ist ein versteckter Regler, und ein echtes "selbstorganisiert
kritisches" System sollte keinen brauchen. Sehr fest ist dagegen die Zusammensetzung des Netzes: Immer hat je ein
Drittel der Ecken 5, 6 oder 7 Nachbarn, und das folgt vermutlich schon aus einfachem Abzaehlen. Ein sauberes
Potenzgesetz, das Kennzeichen echter Kritikalitaet, haben wir auch diesmal nicht gefunden.

## 8. Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-122330, EINGEFROREN-SHA256.txt.
- code/: ksh-vorlage-2d-1.py (unveraenderte Kopie der Vorlage, f2c3627a...), ksh2.py
  (+ ksh2.py.eingefroren-20261005-122330), ksh2-gegen-vorlage.diff, kette-cpu.sh, kette-cpu7.sh, rauch-kette.sh.
- jq/tabelle.jq: Leseauszug (vor der Sicht angelegt, nur Formatierung).
- aus-69/: urteile.json (mechanische Urteile, Faelle, Drift-Probe, K-ID), fuenf PNG.
- lauf-69/: L1.json bis L7.json (ohne Rohdaten), Logs L1 bis L7 und AUS, Kettenausgaben, code.sha256, PRUEFSUMMEN.txt
  (sha256 aller Lauf-JSON, npz, aus-Dateien und des Codes auf der .69).
- rauch-69/: Logs und Kettenausgaben der Rauchtests (ohne Werte).
- Rohdaten (npz je Fall: s, T, A, Status je Schritt) nur auf der .69 unter lauf/ und rauch/.
- Ins Forschungsjournal habe ich nicht geschrieben (Schreibrecht nur im Kartenordner); das macht die Leitung.
