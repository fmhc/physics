# TAKT-DYNAMIK-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 47, Finn-Auftrag "Zellen umklappen")

- Karte KARTE.md bindend (TD0 bis TD4 unveraendert). Plan PLAN.md, eingefroren 2026-10-05 08:47:32 CEST.
- Alle Zahlen sind synthetische Gitterrechnungen auf der .69 (Python 3.12.3, numpy 2.4.4, scipy 1.18.0, 1 Thread), keine
  Messdaten.
- **Kennzeichen:** [E] hier gerechnet, [M] Mathematik (vorab ableitbar), [P] Projektdatei, [F] Festlegung im Plan,
  [H] Hypothese oder Lesart.
- **Begriffe:**
  - Arm a: feste Zerlegung. Arm b: Delaunay-gesteuerte 2-3/3-2-Zuege im gedehnten Netz, Zugzeit per Bisektion. Arm c:
    gleich viele Zufallszuege gleicher Typen zu denselben Zeiten.
  - Lesart R (Hauptlesart): Laengen und Raten der Kanten stetig, neue Kante aus der flachen Doppelpyramide
    (Cayley-Menger, linearisiert), wegfallende Kante gestrichen, dann Projektion auf die neue Zwangsflaeche. Lesart P
    (Nebenarm): Impulse statt Raten. Lesart H: Operatoren auf den ungedehnten Lagen (PLAN 4).
  - "Mode": die Kasteneigenmode mit dem groessten Energieanteil der idealen TT-Welle (Wellenlaenge = Kastenlaenge).
  - H0 = Energie bei t = 0; "Drift Ende" = (H(10 T) - H0) / H0; "Drift Max" = max_t |H - H0| / H0.
  - gd = im gedehnten Netz gemessen, hg = auf den ungedehnten Lagen (Hintergrund).
  - VD2 = V_D (TAKT-UMKLAPP-1) als 2 x 2 x 2-Superzelle.

## 1. Zeiten und Laeufe

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 08:19:29 CEST. Code kopiert 08:27:36 CEST; td.py neu bis 08:43 (letzter Zusatz: Abbruch bei wachsender Mode).
  - Rauchtests 06:40:06 bis 06:47:11 UTC (r1 rc = 1: A_red indefinit, Anlass fuer 1_E in der Zwangsflaeche; alle
    weiteren rc = 0; PLAN 11). Plantext ab 08:42:50 CEST.
  - Eingefroren 2026-10-05 08:47:32 CEST: PLAN.md.eingefroren-20261005-084732 (sha256 728ad544...), code/td.py
    (fbc02c48...), code/kette.sh (a22520d5...); tu.py, tg.py, tg_auswertung.py, tp.py, uk.py, ew.py, mn.py unveraendert
    (6c5c3a95..., ec48a258..., 88cbd2ce..., 419d7da6..., f52df743..., fa7b6417..., b36984d3...). Auf der .69 dieselben
    Summen (EINGEFROREN-SHA256-69.txt, 06:47:37 UTC).
  - Laufketten 06:47:37 bis 07:12:04 UTC auf cpu8, cpu9, cpu10; alle 45 Aufrufe (44 Laeufe) rc = 0; der laengste Abschnitt 500,7 s
    (s3, A = 1e-2, b, Lesart P, Abschnitt 1, danach Abschnitt 2 mit 65,9 s); alle anderen Laeufe in einem Abschnitt.
  - Auswertung, Bild, Tabellen (nachtrag/abschluss-cpu8.sh) 07:12:14 bis 07:12:21 UTC, rc = 0; lauf-69/PRUEFSUMMEN.txt
    lokal 0 Abweichungen.
  - Nachtraege (beschreibend, nach dem Einfrieren): nt-dehnung 06:53:03 bis 06:53:42 UTC (cpu8, zwischen zwei
    Kettenlaeufen), nt-bild 07:14:12 bis 07:14:15 UTC (cpu8), beide rc = 0.
  - Text ab 09:15:15 CEST. Abschluss siehe Dateiende.
- **Laeufe** (Aufruf `kleintest.sh <Spur> <Name>-<Abschnitt> code/td.py lauf --netz <Netz> --A <A> --arm <Arm>
  [--lesart P] [--h 0.25] --budget 500 [--ereignisse <b-Lauf>] --out lauf/<Name>.json`; Zeiten aus den Logzeilen von
  kleintest.sh, UTC; Laufzeit = laufzeit der Rechnung):

  | Lauf (Netz, A, Arm) | Spur | Start | Ende | Laufzeit | rc |
  |---|---|---|---|---|---|
  | s1 1e-3 a / b | cpu8 | 06:47:37 | 06:48:06 | 3,5 / 23,9 s | 0 / 0 |
  | s4 1e-3 a / b | cpu8 | 06:48:06 | 06:48:15 | 3,0 / 4,5 s | 0 / 0 |
  | s1 1e-3 c / s4 1e-3 c | cpu8 | 06:48:15 | 06:48:42 | 22,1 / 3,0 s | 0 / 0 |
  | s1 1e-2 a / b / c | cpu8 | 06:48:42 | 06:53:39 | 3,1 / 194,9 / 95,4 s | 0 / 0 / 0 |
  | VD2 1e-3 a / b, 1e-2 a / b | cpu8 | 06:53:39 | 06:53:50 | 0,8 / 1,1 / 0,8 / 1,2 s | 0 |
  | s1 1e-3 b-P / a-h025 / b-h025 | cpu8 | 06:53:50 | 06:54:51 | 22,2 / 5,7 / 31,3 s | 0 |
  | s1 1e-2 b-P | cpu8 | 06:54:52 | 07:00:51 | 358,3 s | 0 |
  | s2 1e-3 a / b / c | cpu9 | 06:47:37 | 06:49:37 | 4,4 / 72,3 / 40,4 s | 0 |
  | s2 1e-2 a / b / c | cpu9 | 06:49:37 | 06:57:03 | 4,1 / 264,2 / 175,0 s | 0 |
  | s4 1e-2 a / b / c | cpu9 | 06:57:03 | 07:01:19 | 3,0 / 160,5 / 89,4 s | 0 |
  | s2 1e-3 b-P / a-h025 / b-h025 | cpu9 | 07:01:19 | 07:04:19 | 86,6 / 7,2 / 83,8 s | 0 |
  | s2 1e-2 b-P | cpu9 | 07:04:19 | 07:12:04 | 463,5 s | 0 |
  | s3 1e-3 a / b / c | cpu10 | 06:47:37 | 06:48:51 | 3,4 / 44,7 / 23,0 s | 0 |
  | s3 1e-2 a / b / c | cpu10 | 06:48:51 | 06:55:09 | 3,0 / 257,9 / 114,5 s | 0 |
  | s3 1e-3 b-P, s4 1e-3 b-P | cpu10 | 06:55:09 | 06:56:15 | 60,2 / 4,4 s | 0 |
  | s3, s4 1e-3 a-h025 / b-h025 | cpu10 | 06:56:15 | 06:57:30 | 5,2 / 52,4 / 5,3 / 8,1 s | 0 |
  | s3 1e-2 b-P (2 Abschnitte) | cpu10 | 06:57:30 | 07:06:59 | 500,7 + 65,9 s | 0 / 0 |
  | s4 1e-2 b-P | cpu10 | 07:06:59 | 07:11:02 | 242,1 s | 0 |
  | auswertung / bild / tabellen | cpu8 | 07:12:14 | 07:12:20 | 1,0 s / 4 s / <1 s | 0 |

## 2. Ergebnis zuerst

1. **Delaunay-gesteuertes Umklappen bleibt waehrend der Welle stabil, Zufallszuege nicht [E].** In keinem der 22
   b-Laeufe (Lesarten R und P, beide dt, alle Netze) entstand eine wachsende Mode. Gleich viele Zufallszuege zu denselben
   Zeiten erzeugten in allen 7 Faellen mit Zuegen 2 bis 15 wachsende Moden (omega^2 -5,80 bis -5,92 in s1 und s3 bei A = 1e-3); die
   Rechnung lief nach 2,4 bis 8,4 Perioden ueber (Abbruch bei 1e6-facher Amplitude). Das war aus HT2/HT3 erwartbar
   (TD2 nach Wortlaut eingetroffen, nach Plan verfehlt, weil Saat 4 bei A = 1e-3 gar keinen Zug hatte).
2. **Die Energie ist ueber Zuege nicht erhalten (TD1 verfehlt) [E].** Ein Zug aendert H im Mittel um 0,2 bis 0,46 %
   von H0 (hoechstens 2,2 %). Ueber 10 Perioden verliert die Welle in Lesart R 2,4 bis 12,7 % (A = 1e-3) bzw. 10,5 bis
   34,6 % (A = 1e-2); in Lesart P gewinnt sie 15 bis 20 % bzw. 32 bis 80 %. Arm a: hoechstens 2e-8. Die Zeitbehandlung
   ist nicht die Ursache: Halbes dt aendert die Drift um hoechstens 0,15 Prozentpunkte. Die potentielle (Regge-)Energie
   ist beim 2-3-Zug exakt stetig (<= 8e-13 H0, vorab abgeleitet [M]); der Sprung sitzt in der Bewegungsenergie. Deren Mass A0 gibt
   jedem Tetraeder unabhaengig von seiner Groesse dasselbe Gewicht, darum gibt es dort keine solche Stetigkeit [M];
   dass das die ganze Ursache ist, ist nicht getrennt gerechnet [H].
3. **TD0 haelt beim 2-3-Zug exakt, beim 3-2-Zug nur bis auf den Fehlwinkel der Welle (TD0 verfehlt) [E, M].** Im
   gedehnten Netz sind duales Mass und P-Sprung beim 2-3-Zug <= 2e-13 (relativ). Beim 3-2-Zug sind sie von der Ordnung
   der Kruemmung, die die Welle an der wegfallenden Kante traegt: Median 0,9e-6 bis 3e-6 (A = 1e-3) bzw. 1,2e-5 bis 2,1e-5 (A = 1e-2), einzelne
   Ausreisser an fast flachen gedehnten Tetraedern bis 6e3. Das war im Plan vorab so erwartet (PLAN 7).
4. **Die Zuege streuen und verschieben die Welle, linear in A (TD3 verfehlt) [E].** Nach 10 Perioden weicht die
   TT-Amplitude in Arm b um 0 bis 17,5 % (Mittel 5,1 %) von Arm a ab bei A = 1e-3, um 24 bis 54 % (Mittel 39 %) bei
   A = 1e-2; Phasenverschiebung bis 0,47 bzw. 1,26 rad. Exponent 0,89, also etwa wie A, nicht wie A^1,5 (vorab erwartet:
   Zahl der Zuege ~ A, Wirkung je Zug von A unabhaengig).
5. **Die Zerlegung kehrt nicht ganz zurueck (TD4 verfehlt) [E].** Nach vollen Perioden sind bei A = 1e-3 98,9 bis
   100 % der Ausgangsflaechen da (Saat 2: 98,91 %), bei A = 1e-2 nur 89 bis 95 %. Bei A = 1e-2 hatten 43 bis 85
   Delaunay-Ereignisse je Lauf keinen ausfuehrbaren Zug. VD2: kein einziger Zug (kleinster Randabstand 0,22), alle Arme gleich.

## 3. Urteile

Mechanisch durch code/td.py auswertung (eingefroren 08:47:32 CEST), lauf-69/auswertung.json; Regeln PLAN 8.

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| TD0 | Kontrolle, vorab ableitbar: duales Mass der neuen/wegfallenden Kante bzw. Flaeche < 1e-10 relativ, P springt < 1e-10 relativ | 85 % | **verfehlt** | **verfehlt** | 1 994 Zuege in b-Laeufen (Lesart R): 2-3 hoechstens 2,1e-13; 3-2 Median 0,9e-6 bis 3e-6 (1e-3) bzw. 1,2e-5 bis 2,1e-5 (1e-2), Minimum 1,8e-9, Maximum 5,8e3 (s2, 1e-2) |
| TD1 | [H] Drift (b) < 2 x Drift (a) bei A = 1e-3 | 55 % | **verfehlt** | **verfehlt** | Ende-Drift b / a: s1 -0,0406 / 1,7e-8; s2 -0,127 / 2,1e-9; s3 -0,0245 / 1,9e-8; s4 1,7e-8 / 1,7e-8 (kein Zug). Max-Drift b / a: 0,041 / 5,3e-4; 0,128 / 2,7e-4; 0,031 / 5,6e-4; gleich |
| TD2 | [H] Drift (c) >= 10 x Drift (a) und wachsende Moden | 75 % | **verfehlt** | **eingetroffen** | Ende-Drift c / a: 9,6e16; 8,7e17; 6,0e16; 1 (s4, kein Zug); Median 7,8e16. Wachsende Moden 2 / 4 / 4 / 0. Plan verlangt jedes Netz: s4 hat keinen Zug |
| TD3 | [H] TT-Amplitudenverlust (b gegen a) bei 1e-3 < 1e-3 und Wachstum >= A^1,5 | 45 % | **nicht entscheidbar** | **verfehlt** | \|Amp_b / Amp_a - 1\|: 1e-3: 0,0084 / 0,175 / 0,019 / 0 (Mittel 0,051); 1e-2: 0,50 / 0,54 / 0,29 / 0,24 (Mittel 0,39); Exponent 0,89. Plan (modal): bei 1e-2 kehrte kein Lauf an einer vollen Periode zur Ausgangszerlegung zurueck |
| TD4 | Kontrolle, vorab ableitbar: nach vollen Perioden >= 99 % der Flaechen wie am Anfang | 85 % | **verfehlt** | **verfehlt** | Minimum ueber Perioden: 1e-3: s1 0,9936, s2 0,9891, s3 0,9926, s4 1; 1e-2: 0,892 / 0,895 / 0,905 / 0,952; VD2 1 |

- **Vorab ableitbar bzw. vorab erwartet (PLAN 7):**
  - TD0 fuer 3-2-Zuege verfehlt [M]: Die 10 gedehnten Laengen der 5 Ecken sind bei einer Welle nicht flach. Bestaetigt:
    Die 3-2-Werte wachsen mit A (Median etwa 1e-6 bei 1e-3, 1,2e-5 bis 2,1e-5 bei 1e-2).
  - TD3-Teil "mindestens wie A^1,5" nicht zu erwarten [M + P]. Bestaetigt: Exponent 0,89.
  - TD1 nach Wortlaut "vorab sehr unwahrscheinlich" (Delta K != 0 [M]). Bestaetigt.
  - Delta V = 0 beim 2-3-Zug [M]. Bestaetigt: hoechstens 7,7e-13 H0 in allen b-Laeufen.
  - VD2 ohne Zug [P, M]. Bestaetigt.
  - Neu und nicht ableitbar waren: die Groesse und das Vorzeichen der Energiespruenge (Lesart R verliert, P gewinnt), die
    Streuung, die Rueckkehr der Zerlegung, die Stabilitaet in Arm b auch bei A = 1e-2.
- **TD2 nach Plan verfehlt** allein wegen Saat 4: Ihr kleinster Randabstand (2,0e-3) liegt ueber dem, was die Mode bei
  A = 1e-3 erreicht; Arm b hatte 0 Zuege, also auch Arm c. In den drei Netzen mit Zuegen sind beide Teile erfuellt.
- **Agenten-Vorhersagen (PLAN 10, kein Urteil):** D1 (Delta V bei 2-3 <= 1e-10 H0 in allen Laeufen, 85 %): in den
  b-Laeufen eingetroffen (<= 7,7e-13); in den c-Laeufen nach H0 gemessen verfehlt, weil H dort explodiert (bezogen auf
  das jeweilige |H| <= 6e-11). D2 (mittlerer |Delta H| > 1e-6 H0, 70 %): eingetroffen (2e-3 bis 4,6e-3). D3 (2-3 < 1e-10
  und alle 3-2 > 1e-8, 65 %): verfehlt (3-2 Minimum 1,8e-9). D4 (Arm b ohne wachsende Mode, 70 %): eingetroffen.

## 4. Tabellen

- Quelle: lauf-69/auswertung.json, formatiert mit code/tabellen.py (nach dem Einfrieren, nur Darstellung) zu
  lauf-69/tabellen.md; Punkt als Dezimalzeichen. Saaten s1 bis s4 = Glas N = 128 (TT-GLAS-1).
- **Bilder:** lauf-69/bild-takt-dynamik.png (eingefrorenes td.py bild; logarithmisch, die explodierenden c-Laeufe
  ueberdecken die Amplitudenkurven) und nachtrag-69/bild-takt-dynamik-2.png (Nachtrag, nur Darstellung): Energie in % ueber
  t / T fuer die drei Arme (c bei +-60 % abgeschnitten, Abbruch senkrecht markiert), Zuege je Periode, TT-Lesung / A fuer
  Saat 2.

### 4.1 Energiedrift (relativ zu H0), Lesart R, h = 0,5 [E]

| Netz | A | Ende a | Ende b | Ende c | Max a | Max b | Max c | Max b / Max a |
|---|---|---|---|---|---|---|---|---|
| s1 | 1e-3 | 1.67e-08 | -0.0406 | 1.6e+09 (Abbruch 8,4 T) | 0.000534 | 0.0411 | 1.6e+09 | 76.9 |
| s2 | 1e-3 | 2.11e-09 | -0.127 | -1.82e+09 (4,7 T) | 0.000268 | 0.128 | 1.95e+09 | 478 |
| s3 | 1e-3 | 1.91e-08 | -0.0245 | 1.15e+09 (3,4 T) | 0.000558 | 0.0315 | 1.15e+09 | 56.4 |
| s4 | 1e-3 | 1.67e-08 | 1.67e-08 (0 Zuege) | 1.67e-08 (0 Zuege) | 0.000534 | 0.000534 | 0.000534 | 1 |
| s1 | 1e-2 | 1.67e-08 | -0.105 | 1.09e+10 (2,8 T) | 0.000534 | 0.123 | 1.09e+10 | 231 |
| s2 | 1e-2 | 2.11e-09 | -0.346 | 3.24e+09 (4,2 T) | 0.000268 | 0.346 | 3.24e+09 | 1290 |
| s3 | 1e-2 | 1.91e-08 | -0.271 | 4.22e+10 (2,4 T) | 0.000558 | 0.271 | 4.44e+10 | 486 |
| s4 | 1e-2 | 1.67e-08 | -0.213 | 1.35e+10 (3,6 T) | 0.000534 | 0.214 | 1.35e+10 | 400 |
| VD2 | 1e-3 / 1e-2 | 3.03e-05 | 3.03e-05 (0 Zuege) | - | 0.00653 | 0.00653 | - | 1 |

- "Max a" ist die Verlet-Schwankung (omega dt)^2 / 4 (s1: omega dt = 0,046), kein Trend. Arm c: Ende = letzte Probe vor
  dem Abbruch (Zeit in Perioden T).
- **Nebenarme [E]:**

| Netz | A | Lesart P: Ende-Drift (Zuege) | Lesart R, h = 0,25: Ende-Drift (Zuege) | Lesart R, h = 0,5 (Vergleich) | Arm a, h = 0,25 |
|---|---|---|---|---|---|
| s1 | 1e-3 | +0.148 (30) | -0.0408 (31) | -0.0406 (31) | 2.6e-10 |
| s2 | 1e-3 | +0.180 (144) | -0.127 (113) | -0.127 (113) | 3.3e-11 |
| s3 | 1e-3 | +0.202 (93) | -0.0230 (67) | -0.0245 (65) | 3.0e-10 |
| s4 | 1e-3 | 1.67e-08 (0) | 2.6e-10 (0) | 1.67e-08 (0) | 2.6e-10 |
| s1 | 1e-2 | +0.493 (658) | - | -0.105 (351) | - |
| s2 | 1e-2 | +0.798 (858) | - | -0.346 (479) | - |
| s3 | 1e-2 | +0.646 (1038) | - | -0.271 (470) | - |
| s4 | 1e-2 | +0.324 (453) | - | -0.213 (294) | - |

### 4.2 Zuege je Periode und Energiespruenge je Zug (Lesart R, h = 0,5) [E]

| Netz | A | Arm | Zuege (2-3 / 3-2) | nicht ausgef. | je Periode | Summe Delta H | mittel \|Delta H\| | max \|Delta H\| | 2-3: max \|Delta V\| / mittel Delta K | 3-2: mittel Delta V / mittel Delta K | omega_max dt (max) | sofort verletzt (max) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| s1 | 1e-3 | b | 31 (15 / 16) | 0 | 3.1 | -0.0406 | 0.00461 | 0.0149 | 5.4e-14 / +0.0034 | -7.7e-05 / -0.00565 | 1.52 | 6 |
| s2 | 1e-3 | b | 113 (54 / 59) | 0 | 11.3 | -0.127 | 0.00326 | 0.0150 | 2.5e-14 / +0.00223 | -0.00017 / -0.00403 | 0.50 | 4 |
| s3 | 1e-3 | b | 65 (31 / 34) | 2 | 6.5 | -0.0244 | 0.00265 | 0.00881 | 5.9e-14 / -4.1e-05 | -9.4e-05 / -0.00059 | 1.01 | 10 |
| s4 | 1e-3 | b | 0 | 0 | 0 | - | - | - | - | - | - | - |
| s1 | 1e-2 | b | 351 (174 / 177) | 85 | 35.1 | -0.105 | 0.0023 | 0.0171 | 3.6e-13 / +0.00179 | -0.00011 / -0.00224 | 1.58 | 133 |
| s2 | 1e-2 | b | 479 (232 / 247) | 43 | 47.9 | -0.346 | 0.00197 | 0.0182 | 1.1e-13 / +0.00116 | -0.00018 / -0.00231 | 0.51 | 111 |
| s3 | 1e-2 | b | 470 (226 / 244) | 61 | 47.0 | -0.271 | 0.00198 | 0.0132 | 3.7e-13 / +0.00123 | -0.00015 / -0.00211 | 1.04 | 78 |
| s4 | 1e-2 | b | 294 (145 / 149) | 44 | 29.4 | -0.213 | 0.0025 | 0.0220 | 7.7e-13 / +0.00166 | -0.00015 / -0.0029 | 0.86 | 54 |
| s1 / s2 / s3 | 1e-3 | c | 28 / 55 / 30 | 0 | 3.3 / 11.8 / 8.8 | (explodiert) | - | - | - | - | 0.54 / 0.50 / 0.50 | 0 |
| s1 / s2 / s3 / s4 | 1e-2 | c | 140 / 257 / 162 / 134 | 0 | 50 / 61 / 69 / 37 | (explodiert) | - | - | - | - | 0.56 / 0.57 / 0.76 / 0.64 | 0 |

- Spruenge relativ zu H0. "je Periode" bei c bis zum Abbruch. "nicht ausgef." = Delaunay-Ereignis ohne ausfuehrbaren Zug
  (keine Kante vom Grad 3, oder auf den ungedehnten Lagen ungueltig; s1 bei 1e-2: 81 von 85 vom Typ 3-2); die Flaeche
  bleibt gesperrt, bis ihr mu wieder > 0 ist.
  "sofort verletzt" = Flaechen mit mu < 0 direkt nach einem Zug (Linearisierungsrest der neuen Kante, gesperrt).
- Arm a ohne Zuege verletzt die Mode zeitweise 1 / 7 / 8 / 0 Flaechen (A = 1e-3) bzw. 32 / 35 / 44 / 16 (A = 1e-2) von
  1 700 bis 1 746; UK1 (affin) liesse 1,2 A F, also ~2 bzw. ~21 erwarten [P]. Die Mode hat Kantendehnungen bis 0,89 bis
  1,51 A (Effektivwert 0,29 bis 0,41 A; Nachtrag nachtrag-69/dehnung.json).
- Bei A = 1e-3 klappt anfangs oft dasselbe Flaechenpaar hin und zurueck (s1: Flaeche 1-102-91, Randabstand 6,1e-4);
  spaeter kommen weitere Flaechen dazu (Bild 2, Mitte).

### 4.3 Sprung von P und dualem Mass am Zug (relativ zu max \|*1\|, max \|*2\|, max P_vv des Ausgangsnetzes) [E]

| Netz | A | Typ | n | gd: *1 der Kante | gd: *2 der Flaeche | gd: max \|Delta P\| | hg: max \|Delta P\| | hg: Median \|Delta P\| |
|---|---|---|---|---|---|---|---|---|
| s1 | 1e-3 | 2-3 | 15 | 4.2e-15 | 5.5e-17 | 1.4e-14 | 1.1e-05 | 2.8e-06 |
| s1 | 1e-3 | 3-2 | 16 | 9.9e-06 | 1.2e-05 | 5.7e-05 | 1.1e-05 | 3.6e-06 |
| s2 | 1e-3 | 2-3 | 54 | 9.9e-16 | 1.2e-16 | 5.7e-15 | 2.0e-05 | 2.2e-07 |
| s2 | 1e-3 | 3-2 | 59 | 1.4e-05 | 6.8e-05 | 7.1e-05 | 2.0e-05 | 2.2e-07 |
| s3 | 1e-3 | 2-3 | 31 | 1.7e-16 | 1.6e-16 | 2.8e-15 | 1.1e-04 | 5.0e-07 |
| s3 | 1e-3 | 3-2 | 34 | 7.4e-06 | 1.8e-05 | 1.0e-04 | 1.5e-04 | 5.0e-07 |
| s1 | 1e-2 | 2-3 | 174 | 4.1e-14 | 3.0e-16 | 2.1e-13 | 0.14 | 8.7e-05 |
| s1 | 1e-2 | 3-2 | 174 | 6.8 | 0.0024 | 7.2 | 0.016 | 8.0e-05 |
| s2 | 1e-2 | 2-3 | 232 | 9.5e-16 | 3.2e-15 | 1.1e-13 | 0.28 | 3.8e-05 |
| s2 | 1e-2 | 3-2 | 242 | 1.3e+03 | 0.0035 | 5.8e+03 | 0.025 | 3.5e-05 |
| s3 | 1e-2 | 2-3 | 226 | 1.6e-14 | 1.1e-16 | 6.7e-14 | 0.051 | 8.6e-05 |
| s3 | 1e-2 | 3-2 | 236 | 1.1e+02 | 5.7e-04 | 1.7e+02 | 0.019 | 6.0e-05 |
| s4 | 1e-2 | 2-3 | 145 | 1.9e-14 | 1.9e-16 | 1.3e-13 | 0.051 | 6.8e-05 |
| s4 | 1e-2 | 3-2 | 145 | 2.5e-04 | 8.2e-04 | 2.5e-03 | 0.0095 | 5.6e-05 |
| c, alle Netze | 1e-3 / 1e-2 | 2-3 und 3-2 | 11 bis 88 je Typ | 0,006 bis 4,6 | 0,005 bis 0,36 | 0,005 bis 16,6 | 0,005 bis 9,2 | 4e-4 bis 0,04 |

- 3-2-Zuege in b (gd, *1 der wegfallenden Kante): Median 3,0e-6 / 1,1e-6 / 8,6e-7 (s1 / s2 / s3, A = 1e-3), 2,1e-5 /
  1,2e-5 / 1,7e-5 / 1,4e-5 (A = 1e-2); 90-%-Wert <= 2,2e-4; ueber 1e-2 nur 1 / 2 / 1 / 0 Zuege je Lauf bei A = 1e-2.
- hg ist der Sprung, den die Dynamik in Lesart H sieht: Am Hintergrund ist der umgeklappte Bereich nicht kugelig, der
  Sprung ist von der Ordnung des Randabstands (Median 2e-7 bis 9e-5).

### 4.4 Amplitude, Phase, Streuung (letzte Periode [9 T, 10 T]) [E]

| Netz | A | Mode: omega / Anteil der TT-Welle | Amp a / A | Amp b / Amp a - 1 | Phase b - a (rad) | modal (b): Anteil TT / Null / Rest (Periode) | Flaechen wie Anfang b (min) | Ausgangszerlegung an vollen Perioden |
|---|---|---|---|---|---|---|---|---|
| s1 | 1e-3 | 2.493 / 0.289 | 1.0002 | +0.0084 | +0.015 | 0.99722 / 0.0004 / 0.0024 (1) | 0.99362 | 1 von 10 |
| s2 | 1e-3 | 2.627 / 0.297 | 1.0001 | -0.175 | +0.469 | - | 0.98906 | 0 von 10 |
| s3 | 1e-3 | 2.324 / 0.214 | 1.0002 | -0.0191 | +0.269 | 0.98495 / 0.0028 / 0.0123 (2) | 0.99255 | 2 von 10 |
| s4 | 1e-3 | 2.242 / 0.534 | 1.0002 | 0 | 0 | 1 / 1e-30 / 0 (10) | 1 | 10 von 10 |
| s1 | 1e-2 | 2.493 / 0.289 | 1.0002 | -0.500 | -0.344 | - | 0.89211 | 0 von 10 |
| s2 | 1e-2 | 2.627 / 0.297 | 1.0001 | -0.536 | +1.26 | - | 0.89459 | 0 von 10 |
| s3 | 1e-2 | 2.324 / 0.214 | 1.0002 | -0.290 | +0.975 | - | 0.90550 | 0 von 10 |
| s4 | 1e-2 | 2.242 / 0.534 | 1.0002 | -0.242 | +0.866 | - | 0.95235 | 0 von 10 |
| VD2 | 1e-3 / 1e-2 | 1.788 / 0.443 | 1.0027 | 0 | 0 | 1 (10) | 1 | 10 von 10 |

- Lesart P (Nebenarm), Amp b / Amp a - 1: +0,0036 / -0,126 / -0,038 / 0 (A = 1e-3), -0,30 / -0,32 / -0,54 / -0,12
  (A = 1e-2). Lesart R mit h = 0,25: +0,0086 / -0,175 / -0,017 / 0 (A = 1e-3).
- Arm c: Amplitude nicht auswertbar (Abbruch vor 10 T).
- "Anteil der TT-Welle" = Energieanteil der idealen TT-Welle in der gewaehlten Mode: Die Kastenwelle (Wellenlaenge
  5,04, etwa 4 Kantenlaengen) ist im Glas auf viele Moden verteilt.

### 4.5 Wachsende Moden [E]

| Arm | Laeufe | wachsende Moden (max nach einem Zug) | A_red nicht pd | Abbruch (t / T) |
|---|---|---|---|---|
| a | 10 (h = 0,5) + 4 (h = 0,25) | 0 | - | - |
| b, Lesart R | 10 (h = 0,5) + 4 (h = 0,25) | 0 | 0 | - |
| b, Lesart P | 8 | 0 | 0 | - |
| c, A = 1e-3 | s1 / s2 / s3 / s4 | 2 / 4 / 4 / 0 (kein Zug) | 0 | 8,4 / 4,7 / 3,4 / - |
| c, A = 1e-2 | s1 / s2 / s3 / s4 | 15 / 12 / 15 / 11 | 0 | 2,8 / 4,2 / 2,4 / 3,6 |

- Arm c: Die erste wachsende Mode trat nach dem 14. (s1) bzw. 2. (s3) Zufallszug auf (A = 1e-3); omega^2 der wachsenden
  Moden -5,80 bis -5,92 in beiden Netzen (Ursache des fast gleichen Werts nicht untersucht [H]). omega_max dt blieb
  <= 0,76, also ist das Wachstum keine Verlet-Instabilitaet.
- Arm b: omega_max dt stieg nach einzelnen Zuegen bis 1,58 (s1; ein Zug erzeugt auf den ungedehnten Lagen einen flachen
  Tetraeder), blieb unter der Verlet-Grenze 2; die Laeufe mit halbem dt bestaetigen die Drift.

### 4.6 Kontrollen [E]

- Zwangsflaeche: S^T M und S^T c <= 1,3e-15 (relativ); B_red hat in allen 5 Netzen 5 Nullmoden (vorab erwartet: gleichmaessige spurfreie
  Dehnungen [M]); A_red im Ausgangsnetz positiv definit (mit 1_E).
- Flache Laenge der neuen Kante aus 9 Kanten = Abstand im Netz (Hintergrund) auf 1e-16; gedehnte neue Kante linear gegen
  nichtlinear flach: <= 7e-4 (A = 1e-3), <= 2,2 % (A = 1e-2); Projektionsrest (Eichanteil, Maximum je Lauf) 3,8 bis 9,5 % von a.
- Arm a: Drift 2e-9 bis 2e-8 (h = 0,5), 3e-11 bis 3e-10 (h = 0,25); nach vollen Perioden Ausgangszerlegung.

## 5. Bedeutung fuer Finns Mechanismus "Zellen umklappen" [H]

- **Was die Rechnung traegt [E]:**
  1. Delaunay als Auswahlregel haelt das Netz auch dynamisch stabil: Waehrend eine Welle laeuft und das Netz 31 bis 479 (Lesart P bis 1 038)
     Mal umklappt, waechst keine Mode; dieselbe Zahl zufaelliger Zuege zerstoert die Rechnung in wenigen Perioden. Das ist
     TU1 (TAKT-UMKLAPP-1) jetzt im laufenden Betrieb [P, E].
  2. Die potentielle Energie (Regge-Kruemmung) ist beim 2-3-Zug exakt stetig, weil die neue Kante flach fortgesetzt wird;
     das ist Mathematik [M] und hier auf 1e-12 bestaetigt.
  3. Die Bewegungsenergie springt an jedem Zug, im Mittel um 0,2 bis 0,5 % von H0; das passt zum Anteil der
     umgeklappten Zellen an der ganzen Welle (5 von 850 bis 873 Tetraedern) [H]. Das Modell gibt jedem Tetraeder
     dasselbe Gewicht A0, egal wie gross er ist;
     ein 2-3-Zug fuegt einen Tetraeder hinzu, ein 3-2-Zug nimmt einen weg.
  4. Wie die Energie ueber den Zug weitergegeben wird, legt das Modell nicht fest: Mit stetigen Raten (Lesart R) verliert
     die Welle Energie, mit stetigen Impulsen (Lesart P) gewinnt sie. Beides sind Festlegungen, keine Physik des Netzes.
- **Bedeutung nach Karte (vorab festgelegt):**
  - "TD1 und TD3 treffen ein ..." nicht ausgeloest.
  - "TD1 verfehlt: Die Zuege brauchen eine bessere Zeitbehandlung (exakte Zugzeiten), oder sie tragen Energie. Das waere
    ein Hinweis auf einen versteckten Freiheitsgrad." **Ausgeloest.** Die Zugzeiten sind hier exakt (Bisektion auf
    dt / 2^60, dt-Halbierung aendert die Drift um <= 0,15 Prozentpunkte). Es bleibt "sie tragen Energie". Lesart: Der
    versteckte Freiheitsgrad ist die Zahl der Zellen bzw. ihr Gewicht in der Bewegungsenergie; beim 3-2-Zug kommt der
    Fehlwinkel auf der wegfallenden Kante hinzu (kleiner Beitrag, Delta V ~ 1e-4 H0) [H].
  - "TD3 verfehlt, also starke Streuung: Die Zuege daempfen bzw. zerstreuen Wellen. Das waere eine moegliche messbare
    Signatur (Daempfung oder Dispersion von Schwerewellen) und waere gegen Daten zu pruefen [H]." **Nach Wortlaut
    ausgeloest** (Plan: nicht entscheidbar). Einschraenkung: Vorzeichen und Groesse haengen hier an der Lesart (R daempft,
    P verstaerkt), und die Wirkung waechst wie A (Zahl der Zuege ~ A). Fuer eine Signatur muesste die Weitergabe der
    Energie am Zug erst festgelegt sein [H].
- **Lesart fuer Finns "Zellen umklappen" [H]:**
  - Mechanismus: Delaunay waehlt, welche Zelle umklappt; damit bleibt der Takt positiv und das Netz stabil, auch mitten
    in einer Welle. Das ist ein brauchbarer Taktschritt.
  - Was fehlt: eine Regel, die die Energie am Zug erhaelt. Zwei Kandidaten (nicht gerechnet): eine nach Volumen
    gewichtete Bewegungsenergie (DeWitt-Mass mal Zellvolumen, dann traegt ein fast flacher neuer Tetraeder fast nichts
    bei), oder eine Abbildung, die H am Zug festhaelt und nur die Richtung im Zustandsraum waehlt.
  - Folge fuer die Groessenordnung: Die Zuege kommen nur an Flaechen mit Randabstand unter der Dehnung vor. Bei einer
    echten Schwerewelle (Dehnung ~1e-21) waeren es entsprechend weniger Zuege je Periode und Zelle; ob es sie im Netz
    gibt, haengt an der Dichte fast entarteter Flaechen [H].
- Grenzen: N = 128, Wellenlaenge = Kastenlaenge (k l ~ 1,5), gemischte Mode (Anteil der TT-Welle 0,21 bis 0,53),
  lineare Dynamik mit Operatoren am ungedehnten Netz (Lesart H), bei A = 1e-2 viele nicht ausfuehrbare Zuege.

## 6. Selbstanzeigen

1. **Zwangsflaeche mit 1_E (Abweichung vom TT-GLAS-1-Modell):** Bei Bloch-k = 0 war A_red mit [M, c] allein indefinit
   (Rauchtest r1). Ich habe die gleichmaessige Streckung zusaetzlich entfernt (Kastenvolumen fest), vor dem Einfrieren
   und im Plan begruendet. Andere Wege (kleines Bloch-k, groesserer Kasten) sind nicht gerechnet.
2. **Die "TT-Mode" ist gemischt:** Bei N = 128 und Wellenlaenge = Kastenlaenge traegt die beste Mode nur 21 bis 53 % der
   idealen TT-Welle. "TT-Amplitude" ist die Tensor-Lesung dieser Mode. Ein reiner TT-Test braeuchte groessere Kaesten.
3. **Lesart H und nicht ausfuehrbare Zuege:** Bei A = 1e-2 waren 43 bis 85 Delaunay-Ereignisse je Lauf auf den
   ungedehnten Lagen nicht ausfuehrbar, und bis zu 133 Flaechen waren nach Zuegen gesperrt. Arm b ist bei A = 1e-2 also
   nicht voll Delaunay-gesteuert; das traegt zur Drift der Zerlegung (TD4) bei.
4. **Rauchtests verrieten Zahlen:** Ereigniszahlen (r1b: 2 in einer Periode, r2b: 214 in 3,5 Perioden, r4h: 64, VD2: 0)
   und Mode-Anteile (0,29, 0,44) vor dem Einfrieren gelesen (PLAN 11).
5. **Zwischenstaende gelesen:** Nach dem Einfrieren habe ich Werte einzelner Laeufe gelesen, waehrend andere noch
   liefen (s1 b A = 1e-3 um 08:48, die c-Laeufe A = 1e-3 um 08:49, b-Laeufe A = 1e-2 ab 08:52 CEST). Keine Regel
   geaendert.
6. **Nachtraege nicht eingefroren:** code/tabellen.py, code/nachtrag_dehnung.py, code/nachtrag_bild.py und
   nachtrag/abschluss-cpu8.sh nach dem Einfrieren geschrieben (Darstellung bzw. beschreibend; td.py dabei unveraendert,
   Summe auf der .69 geprueft). nt-dehnung lief auf cpu8 zwischen zwei Kettenlaeufen (flock, keine Doppelbelegung).
7. **Regelverstoss Scratchpad:** Drei lokale Wartebefehle liefen als Hintergrundaufgaben; das Werkzeug legte ihre
   Ausgaben (nur Status- und Ereignislisten der ssh-Abfragen) unter /tmp/claude-1000/.../tasks/ ab. Das verletzt "Nie
   nach /tmp/claude-1000/...". Danach habe ich nur noch auf der .69 gewartet.
8. **TD2 nach Plan** scheitert nur an Saat 4 ohne Zug; die eingefrorene Regel "in jedem Netz" hatte keine Ausnahme fuer
   Netze ohne Zug.
9. **TD3 nach Plan nicht entscheidbar:** Die modale Streuung setzt die Ausgangszerlegung an einer vollen Periode voraus;
   bei A = 1e-2 trat sie nie ein, bei A = 1e-3 nur in s1 (Periode 1), s3 (Periode 2) und s4.
10. **D1 nach H0 bemessen:** In den c-Laeufen ist Delta V bei 2-3-Zuegen relativ zum jeweiligen |H| <= 6e-11, aber nach
    H0 gemessen gross, weil H explodiert.
11. **Arm c Drift:** Die Zahlen 1e9 bis 4e10 sind Momentaufnahmen vor dem Abbruch (verschiedene Zeiten), kein
    vergleichbarer Drift-Wert.
12. **TD0-Maxima bei 3-2** kommen von 1 bis 2 Zuegen je Lauf bei A = 1e-2 mit fast flachen gedehnten Tetraedern; das
    Urteil haengt nicht daran (auch die Mediane liegen ueber 1e-10).
13. **Bild aus dem eingefrorenen Code** ist schwer lesbar (logarithmische Achsen, explodierende c-Laeufe); das lesbare
    Bild ist ein Nachtrag (nachtrag-69/bild-takt-dynamik-2.png).
14. **Lokal** kein python, awk oder perl; jq lokal nur zum Lesen von lauf-69/*.json (Auszuege, Mediane). Kein Journal,
    kein Peerbus, kein Commit.

## 7. Einfach gesagt

Wir haben eine Schwerewelle durch ein Netz aus kleinen Tetraedern laufen lassen und erlaubt, dass Zellen umklappen, wenn
die Welle das Netz zu stark verzerrt. Klappen die Zellen nach der Delaunay-Regel um, bleibt das Netz stabil; klappen
gleich viele Zellen zufaellig um, wachsen Stoerungen von selbst an, und die Rechnung explodiert nach wenigen
Schwingungen. Aber bei jedem Umklappen aendert sich die Energie der Welle um etwa zwei bis fuenf Promille, weil im Modell
jede Zelle gleich viel "Traegheit" hat, egal wie gross sie ist; je nach Rechenvorschrift verliert oder gewinnt die Welle
dadurch ueber zehn Schwingungen zwischen einigen Prozent und mehr als der Haelfte. Umklappen ist damit ein stabiler, aber kein
verlustfreier Taktschritt; dafuer braucht das Modell noch eine Regel, wie die Energie beim Umklappen weitergegeben wird.
Alles sind Rechnungen an kleinen Modellnetzen, keine Messungen.

## 8. Dateien

- KARTE.md (unveraendert), PLAN.md und PLAN.md.eingefroren-20261005-084732, EINGEFROREN-SHA256.txt (lokal),
  EINGEFROREN-SHA256-69.txt (auf der .69 erzeugt, Kopie).
- code/: td.py (neu; mit .eingefroren-20261005-084732), kette.sh (mit .eingefroren-...); unveraendert kopiert: tu.py,
  tg.py, tg_auswertung.py, tp.py, uk.py, ew.py, mn.py; Nachtraege: tabellen.py, nachtrag_dehnung.py, nachtrag_bild.py;
  td.py.vorfix (Zwischenstand vor den ersten Korrekturen, nicht benutzt).
- lauf-69/: td-<Netz>-A<A>-<Arm>[-P][-h025].json (48 Laeufe), Logs je Abschnitt, kette-cpu8/9/10.out, auswertung.json,
  tabellen.md, bild-takt-dynamik.png, PRUEFSUMMEN.txt (auf der .69 erzeugt, lokal 0 Abweichungen).
- nachtrag-69/: dehnung.json, bild-takt-dynamik-2.png, Logs, abschluss-cpu8.sh, PRUEFSUMMEN.txt.
- rauch-69/: Rauchlogs, rauch-kette.sh, r1.json, r3-vd2.json, r7.json (nur Schluessel).
- Auf der .69: /home/fmh/fmhc-physics-remote/takt-dynamik-1/ (code/, lauf/, nachtrag/, rauch/, code-rauch1/).

Abschluss der Datei 2026-10-05 09:21:05 CEST (date). Zeitbox 150 min ab 08:19:29 CEST (bis 10:49:29) eingehalten; kein Lauf mehr aktiv (letzter Lauf nt-bild 07:14:15 UTC). Kein frischer Gegenleser; Zahlen rueckwaerts gegen lauf-69/tabellen.md und auswertung.json geprueft (dabei acht Stellen berichtigt). Journal, Peerbus und Commit uebernimmt die Leitung.
