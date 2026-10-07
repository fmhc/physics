# QBALL-MONOPOL-1: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 07:49:10 CEST. Agenten-Vorhersagen ab 08:04:27 CEST, Plantext ab 08:13:11 CEST.
  - Rauchlaeufe 06:03:55 bis 06:15:19 UTC (rauch1 bis rauch6, PLAN Abschnitt 8).
  - Eingefroren 08:15:41 CEST: PLAN.md.eingefroren-20261004-081541, Code-Kopien *.eingefroren-20261004-081541,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe (UTC):
    - haupt (Gitter H) 06:15:47 bis 06:17:44
    - grob (Gitter G) 06:17:44 bis 06:18:07
    - fein-v2 (Gitter F) 06:18:42 bis 06:20:31
    - qmax (Bisektion, H) 06:20:31 bis 06:21:07
    - fein-v1 06:21:07 bis 06:24:34, fein-v05 06:24:34 bis 06:27:31, fein-v0 06:27:31 bis 06:32:33
    - auswertung 06:32:43 bis 06:32:46; Nachtrag nachtrag_winkel.py 06:32:46 (beschreibend, nach dem Hauptlauf geschrieben)
  - Text ab 08:21:17 CEST. Alle Laeufe auf Spur p4000a ueber kleintest.sh, nacheinander.
- **Code:** Nach dem Einfrieren unveraendert. Die sha256 von qmonopol.py (8288398...) und auswertung.py (ae5c540...)
  sind lokal, eingefroren und auf der .69 gleich; haupt.json traegt dieselbe Skript-Pruefsumme.
- **Rechenart:** klassische Feldrechnung (Relaxation bei fester Ladung) auf der .69, numpy/scipy auf der CPU der Spur
  p4000a. Keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [E] hier gerechnet, [R] im Rauchlauf gesehen, [F] Festlegung im Plan,
  [S] an der Quelle gelesen (nur ueber Dossier und SPIN1.md), [L] Literatur aus dem Gedaechtnis, [L?] unsicher,
  [H] Hypothese.

## 1. Ergebnis zuerst

1. **Ja, mit dem tiefsten Topf (V0 = 2) haftet der Q-Ball am Monopol [E].**
   - Die Bindung gegen den freien Ball ist etwa 1 Energieeinheit: 0,92 / 1,01 / 1,00 / 0,90 bei Q = 150 / 200 / 300 /
     500. Das sind 0,6 bis 0,2 % von E.
   - Beide Starts landen im selben Zustand, und er ist ein lokales Minimum (kleinster Hesse-Eigenwert > 0).
   - Mit V0 = 0,5 und 1 haftet nichts: Der Ball wandert an allen Q ab. Der Topf allein (ohne Monopol) wuerde ihn dort
     um 2,4 bis 6,6 binden.
2. **Der Ball umhuellt den Monopol nicht, er sitzt auf ihm [E].**
   - Der Ladungsschwerpunkt liegt 0,43 bis 1,05 ueber dem Halbdichteradius, der Monopol also am unteren Rand des Balls.
   - Die Nulllinie (Dirac-String als Wirbelfaden) zeigt vom Ball weg nach unten und laeuft nicht durch ihn.
   - Die Winkelform ist darum weit weg von der Mode 1 + cos theta: D(0)/D(pi/2) = 16 bis 250 statt 2.
   - Nur dicht am Monopol gilt die Mode: lokaler Exponent 0,365 bis 0,387 (Soll 0,366), Winkelverhaeltnis 2,02 bis 2,03
     in der innersten Zelle.
3. **Die Bindung endet nach Kartenkriterium bei Q_max ~ 838 (V0 = 2), aber nicht absolut [E].**
   - Unter 1e-3 relativ faellt die Bindung zwischen Q = 836 und 841 (Bisektion, Gitter H).
   - Absolut bleibt sie bis Q = 2000 positiv: 0,62 (Q = 1000) und 0,28 (Q = 2000) auf dem feinsten Gitter, sinkend.
   - Die Verlaengerung (Richardson-Werte, linear in Q bzw. in log Q) ergibt eine Abloesung erst bei Q ~ 2700 bis 3200 [H].
   - Der Grund ist nicht ein teurer Faden im Ball (D5): Der direkte Monopolterm bleibt bei 1,9 bis 2,3.
4. **Drehimpuls: J_z = -Q/2 in jedem Zustand, auf 1e-15 [E, vorab M].** Das ist eine Identitaet des Ansatzes, also eine
   Codeprobe. Ueber Spin oder Statistik des Verbunds sagt die klassische Rechnung nichts.
5. **Kontrollen halten:**
   - QM0 trifft die Radialtabelle auf 7e-6.
   - Ohne Topf (QM1) liegt der Monopolball nie unter der gitterreinen Referenz. Nach Kartenwortlaut (1D-Referenz)
     liegt er bei Q >= 500 knapp darunter; das ist das Translationsartefakt des Polargitters.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/auswertung.py auf Gitter H; Werte in lauf-69/auswertung.json. Die Felder
"vermerk" sind per jq nachgetragen (und das Feld urteil_kartenwortlaut von QM1 in den Vermerk verschoben); die
unveraenderte Maschinenfassung ist lauf-69/auswertung.maschine.json (sha256 aa036a0..., wie in PRUEFSUMMEN.txt der .69).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| QM0 | Kontrolle: ohne Monopol und Topf kugeliger Ball, E auf 1e-3 gegen die Radialtabelle (Q = 473,413, E = 428,641) | 85 % | **eingetroffen** | eingetroffen | E = 428,63796, Abweichung -7,1e-6; z_c = 2e-10; D(0)/D(pi/2) = 1 + 6e-10. G: -3,3e-5, F: -5,7e-7 |
| QM1 | Kontrolle: V0 = 0, alle Q: E_mono >= E_frei (Kato) | 90 % | **eingetroffen** (gegen E_ref, 6 von 6) | **nicht eingetroffen** auf H: Q = 500 / 1000 / 2000 liegen 0,010 / 0,054 / 0,149 unter E_frei (2e-5 bis 9e-5 relativ). Auf F an allen Q darueber | E_mono - E_ref = +0,065 bis +0,220; alle 12 Faelle abgewandert |
| QM2 | [H] mit Topf (ein V0 > 0) Bindung E_mono < E_frei - 1e-3 E_frei | 65 % | **eingetroffen** | eingetroffen | V0 = 2: 6,1e-3 / 5,2e-3 / 3,6e-3 / 2,0e-3 bei Q = 150 / 200 / 300 / 500. V0 = 0,5 und 1: keine (<= 1,0e-4, abgewandert) |
| QM3 | [H] fuer ein V0 endet die Bindung bei Q_max im Bereich bis 2000 | 45 % | **eingetroffen** | eingetroffen, mit Vermerk | V0 = 2: Q_max(Raster) = 500, Bisektion 836 bis 841. Vermerk: Absolut bleibt die Bindung positiv (Q = 1000 / 2000: 0,67 / 0,40 auf H, 0,62 / 0,28 auf F); die Bindung endet an der Relativschwelle |
| QM4 | bei kleinem Q Winkelform der Mode: D(0)/D(pi/2) = 2 auf 10 % | 60 % | **nicht eingetroffen** | nicht eingetroffen (punktweise am Dichtemaximum r = 0,93: 3,10; nur dicht am Monopol im Band, gerechnet bis r = 0,125: 2,02 bis 2,15, vorab ableitbar) | Q = 150, einziger haftender Zustand V0 = 2: 16,3 |

- **Lesarten:**
  - Plan und Kartenwortlaut unterscheiden sich nur bei QM1. Ursache ist das Translationsartefakt des Polargitters: Es
    ist auf F viermal kleiner, und dort haelt auch der Kartenwortlaut.
  - QM3 ist nach der Bindungsdefinition der Karte (aus QM2) eingetroffen. Die Bedeutungszeile der Karte ("Grosse
    Q-Baelle loesen sich, weil die Nulllinie teurer wird") trifft nicht zu (Abschnitt 8).

**Agenten-Vorhersagen** (AGENTEN-VORHERSAGEN.md, 08:04:27 CEST, vor dem Lesen jedes Rauchlaufs)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (70 %) | keine Bindung fuer V0 <= 2, Q >= 150 | **nicht eingetroffen**: V0 = 2 bindet bei Q = 150 bis 500 |
| A2 (80 %) | V0 = 0: Ball wandert ab, E_mono > E_frei an allen Q | **nicht eingetroffen**: Abwandern ja (12 von 12), aber E_mono < E_frei (1D) bei Q = 500, 1000, 2000 (Artefakt) |
| A3 (85 %) | QM0 eingetroffen, <= 3e-4 | **eingetroffen**: -7,1e-6 |
| A4 (60 %) | E_mono - E_frei steigt mit Q, monoton je V0 | **nicht eingetroffen**: bei V0 = 2 erst fallend (150 -> 200), dann steigend; bei V0 = 0 fallend (Artefakt) |
| A5 (30 %) | QM4-Verhaeltnis in [1,8; 2,2] | **nicht eingetroffen**: 16,3 |
| A6 (97 %) | J_z + Q/2 = 0 auf <= 1e-9 relativ | **eingetroffen**: <= 7e-16 relativ |
| A7 (75 %) | Topf ohne Monopol bindet bei V0 = 2, Q = 200 um mehr als 5 | **eingetroffen**: 12,24 |

## 3. Tabellen [E]

### 3.1 Gitter H: bester Zustand je (V0, Q)

- E_frei: freier Ball (1D, gleiches r-Gitter). B_frei = E_frei - E_mono. B_topf = E_topf - E_mono.
- dz = z_c - R_halb: Abstand des Ladungsschwerpunkts vom Halbdichteradius des freien Balls.
- lambda_min: kleinster Hesse-Eigenwert (Metrik 2w).

| V0 | Q | E_frei | E_mono | B_frei | B_frei/E_frei | B_topf | Status | dz | D(0)/D(pi/2) | lambda_min |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 150 | 149,2896 | 148,3722 | **0,9175** | **6,1e-3** | -10,14 | konvergiert | 0,43 | 16,3 | 0,084 |
| 2 | 200 | 194,2935 | 193,2866 | **1,0069** | **5,2e-3** | -11,23 | konvergiert | 0,45 | 22,4 | 0,068 |
| 2 | 300 | 281,6505 | 280,6471 | **1,0034** | **3,6e-3** | -12,30 | konvergiert | 0,50 | 35,1 | 0,050 |
| 2 | 500 | 450,8467 | 449,9507 | **0,8960** | **2,0e-3** | -13,00 | konvergiert | 0,64 | 60,3 | 0,033 |
| 2 | 1000 | 859,5749 | 858,9099 | 0,6650 | 7,7e-4 | -13,31 | konvergiert | 0,78 | 122 | 0,018 |
| 2 | 2000 | 1652,5195 | 1652,1193 | 0,4002 | 2,4e-4 | -13,40 | konvergiert | 1,05 | 250 | 0,0098 |
| 1 | 150 bis 2000 | | | -0,012 bis 0,167 | <= 1,1e-4 | | abgewandert (12/12) | | | |
| 0,5 | 150 bis 2000 | | | -0,022 bis 0,165 | <= 1,0e-4 | | abgewandert (12/12) | | | |
| 0 | 150 bis 2000 | | | -0,032 bis 0,149 | <= 9e-5 | | abgewandert (12/12) | | | |

- Bei V0 = 2 geben Start A und B denselben Zustand: E gleich auf <= 6e-11, z_c auf <= 8e-6.
- Bei V0 <= 1 wandern beide Starts ab (z_c > R_halb + 4 nach 11 bis 24 Schritten). Die kleinen Werte von B_frei dort
  liegen im Bereich des Translationsartefakts (3.4).
- **Topf allein** (E_frei - E_topf), zum Vergleich:
  - V0 = 0,5: 2,36 / 2,72 / 3,02 / 3,19 / 3,21 / 3,16
  - V0 = 1: 5,01 / 5,68 / 6,26 / 6,58 / 6,62 / 6,53
  - V0 = 2: 11,05 / 12,24 / 13,30 / 13,89 / 13,98 / 13,80
  - jeweils Q = 150 / 200 / 300 / 500 / 1000 / 2000
  - Der Monopol nimmt also bei V0 = 2 rund 10 bis 13,4 dieser Topfbindung wieder weg; am Monopol bleibt etwa 1 uebrig.

### 3.2 Energieanteile der haftenden Zustaende (V0 = 2, Gitter H)

| Q | omega^2 | e_kin = omega^2 N | e_rad | e_pol | e_az (Monopol direkt) | e_pot | e_topf | Anteil r < 3 | <cos theta> |
|---|---|---|---|---|---|---|---|---|---|
| 150 | 0,828 | 68,26 | 12,75 | 8,91 | 1,88 | 60,60 | -4,03 | 0,37 | 0,65 |
| 200 | 0,789 | 88,81 | 15,92 | 11,71 | 2,03 | 79,07 | -4,24 | 0,30 | 0,69 |
| 300 | 0,743 | 129,26 | 20,82 | 16,55 | 2,14 | 116,18 | -4,30 | 0,21 | 0,72 |
| 500 | 0,697 | 208,65 | 28,37 | 24,63 | 2,22 | 190,27 | -4,19 | 0,13 | 0,76 |
| 1000 | 0,649 | 402,93 | 42,53 | 40,63 | 2,29 | 374,42 | -3,89 | 0,06 | 0,80 |
| 2000 | 0,615 | 784,02 | 63,66 | 65,45 | 2,33 | 740,13 | -3,47 | 0,03 | 0,82 |

- Der direkte Monopolterm e_az waechst nur von 1,9 auf 2,3. Ein Faden durch den Ball (D5: Kosten ~ phi_0^2 R) kommt
  nicht vor.
- Der Topfgewinn e_topf faellt ab Q = 300 von -4,3 auf -3,5, weil der Ball weiter vom Monopol wegrueckt (dz 0,5 -> 1,05).

### 3.3 Gitterverdopplung der Bindung B_frei (V0 = 2)

| Q | G (h = 0,1; N_t = 32) | H (0,05; 64) | F (0,025; 128) | Verhaeltnis (G-H)/(H-F) | Richardson (F + (F-H)/3) | relativ (Richardson) |
|---|---|---|---|---|---|---|
| 150 | 0,9310 | 0,9175 | 0,9144 | 4,4 | 0,913 | 6,1e-3 |
| 200 | 1,0273 | 1,0069 | 1,0022 | 4,3 | 1,001 | 5,1e-3 |
| 300 | 1,0400 | 1,0034 | 0,9947 | 4,2 | 0,992 | 3,5e-3 |
| 500 | 0,9708 | 0,8960 | 0,8780 | 4,2 | 0,872 | 1,9e-3 |
| 1000 | 0,8572 | 0,6650 | 0,6189 | 4,2 | 0,604 | 7,0e-4 |
| 2000 | 0,8936 | 0,4002 | 0,2850 | 4,3 | 0,247 | 1,5e-4 |

- Zweite Ordnung (Verhaeltnis ~4). Die Gebunden-Urteile (> 1e-3 relativ) sind auf H, F und Richardson gleich: gebunden
  bis Q = 500, nicht bei 1000 und 2000.
- Auf G liegt Q = 1000 knapp unter der Schwelle (9,97e-4); G ist nicht das Urteilsgitter.
- Bei grossem Q ist die Gitterabhaengigkeit gross (G -> H: 0,49 bei Q = 2000). Das ist das Translationsartefakt am
  verschobenen Ball (3.4). Die absolute Bindung bei Q = 2000 ist darum nur auf etwa 0,05 sicher.

**Gitter F bei V0 <= 1** (bester Start je Q; B_frei = E_frei - E_mono, negativ heisst ueber dem freien Ball)

| V0 | Q = 150 | 200 | 300 | 500 | 1000 | 2000 | Status |
|---|---|---|---|---|---|---|---|
| 1 | -0,033 | -0,032 | -0,035 | -0,047 | -0,074 | -0,117 | abgewandert (12/12) |
| 0,5 | -0,046 | -0,043 | -0,047 | -0,055 | -0,087 | -0,140 | abgewandert (12/12) |
| 0 | -0,059 | -0,057 | -0,077 | -0,070 | -0,092 | -0,129 | abgewandert (12/12) |

- Auf F liegt jeder abgewanderte Zustand ueber dem freien Ball, auch bei grossem Q. Auf H lag er dort knapp darunter
  (3.1, 3.4).
- Das bestaetigt, dass die kleinen negativen Werte auf H vom Translationsartefakt kommen: Es ist auf F etwa viermal
  kleiner.

### 3.4 Kontrolle ohne Topf (QM1) und Translationsartefakt (Gitter H)

| Q | E_frei (1D) | freier Ball verschoben (2D, am Stopp) | E_ref | E_mono(V0 = 0), bester Start | E_mono - E_ref | E_mono - E_frei |
|---|---|---|---|---|---|---|
| 150 | 149,2896 | 149,2575 | 149,2575 | 149,3220 | +0,0645 | +0,0324 |
| 200 | 194,2935 | 194,2504 | 194,2504 | 194,3164 | +0,0660 | +0,0230 |
| 300 | 281,6505 | 281,5871 | 281,5871 | 281,6675 | +0,0804 | +0,0171 |
| 500 | 450,8467 | 450,7510 | 450,7510 | 450,8366 | +0,0856 | **-0,0102** |
| 1000 | 859,5749 | 859,3819 | 859,3819 | 859,5212 | +0,1393 | **-0,0536** |
| 2000 | 1652,5195 | 1652,1503 | 1652,1503 | 1652,3701 | +0,2197 | **-0,1494** |

- Ein freier Ball, der auf dem Polargitter nach aussen rutscht, wird kuenstlich billiger. Am Stopp sind das
  -0,032 bis -0,369 (H), -0,108 bis -1,549 (G) und -0,008 bis -0,089 (F).
- Der Monopolball liegt am selben Ort stets darueber (Kato auf demselben Gitter).
- Gegen den 1D-Wert liegt er bei Q >= 500 darunter. Das ist Kartenwortlaut "nicht eingetroffen".

### 3.5 Q_max nach Kartenkriterium (V0 = 2, Gitter H, beschreibend)

| Q | B_frei/E_frei | B_frei | Start | z_c |
|---|---|---|---|---|
| 707,1 | 1,27e-3 | 0,789 | A | 4,87 |
| 771,1 | 1,13e-3 | 0,759 | A | 5,05 |
| 805,2 | 1,06e-3 | 0,744 | B | 5,14 |
| 822,9 | 1,03e-3 | 0,736 | A | 5,18 |
| 831,8 | 1,01e-3 | 0,732 | A | 5,20 |
| **836,4** | **1,004e-3** | 0,730 | A | 5,21 |
| **840,9** | **0,996e-3** | 0,728 | A | 5,23 |

- Q_max liegt in [836,4; 840,9]. Auf Gitter F laege es nach 3.3 etwas tiefer (F bindet bei Q = 1000 um 0,046 weniger
  als H) [H, nicht gerechnet].
- Die absolute Bindung ist dort noch 0,73. Das Ende ist eines der Relativschwelle: E waechst wie Q, die Bindung kaum.

## 4. Kontrollen [E]

- **Winkeldiskretisierung:** kleinster Eigenwert 0,49900 / 0,49975 / 0,499937 / 0,499984 bei N_t = 16 / 32 / 64 / 128
  (Soll 1/2, zweite Ordnung). Naechste: 3,4995 und 8,497 bei N_t = 128 (Soll 3,5 und 8,5). Ohne Monopol 0, 2, 6.
- **Radialer Loeser gegen qladung2:** Q = 473,413 gibt 428,6268 / 428,63796 / 428,64075 (h = 0,1 / 0,05 / 0,025).
  Richardson 428,6417, qladung2 428,64169.
- **QM0 auf drei Gittern:** E_2D = E_1D auf alle Stellen (H: 428,637955); z_c <= 2e-10; D(0)/D(pi/2) = 1 + 6e-10.
  - G: -3,3e-5 gegen die Tabelle, F: -5,7e-7.
- **Starts:** A und B geben bei allen sechs haftenden Zustaenden dieselbe Energie (<= 6e-11) und denselben Ort
  (z_c <= 8e-6).
- **Minimum:** Bei allen haftenden Zustaenden sind die vier Hesse-Eigenwerte nahe sigma = -0,2 positiv. Der kleinste
  faellt mit Q von 0,084 auf 0,0098; das ist vermutlich das Gleiten entlang z [H].
- **Monopolverhalten an r -> 0:**
  - Lokale Exponenten in der ersten theta-Zelle 0,375 bis 0,387, im Kugelmittel der ersten Zellen 0,368 / 0,365.
    Soll (sqrt3 - 1)/2 = 0,366.
  - Die Abweichung der Zellwerte um 1 bis 5 % ist Diskretisierung nahe dem nicht glatten Punkt r = 0.
  - Nachtrag (code/nachtrag_winkel.py, nach dem Hauptlauf, nicht im Plan): punktweises f^2(theta = 0)/f^2(pi/2) in
    der innersten Zelle 2,024 bis 2,029 fuer alle sechs haftenden Zustaende (Mode: 2).
- **Drehimpuls:**
  - J_z + Q/2 <= 1,3e-12 absolut (<= 7e-16 relativ) in allen 48 Faellen.
  - Aufteilung bei Q = 200, V0 = 2: Materie -31,47, Kreuzanteil -68,53, weil der Ball auf der +z-Seite sitzt
    (<cos theta> = 0,69).
- **Ladung:** 2 omega N = Q exakt (eingebaut).
- **Rand:** Ladungsanteil in r > 30 <= 2,7e-9 in allen Faellen.

## 5. Kartenberichtigungen (vor dem Einfrieren offengelegt) und was daraus wurde

- **K1 (Q-Raster):** 150 statt 50/100. Der kleinste Wert liegt ueber Q_s ~ 142, darum kann Zerfliessen keine
  Scheinbindung machen. Bei V0 = 2 haftet schon Q = 150.
- **K2 (QM1-Referenz):** Mit Gitterreferenz eingetroffen, nach Kartenwortlaut nicht (Q >= 500). Der Unterschied ist
  genau das vorab in rauch2 gesehene Translationsartefakt.
- **K3 (QM4-Messgroesse):**
  - Strahlintegriert: 16,3 bei Q = 150.
  - Punktweise am Radius der groessten Kugelmittel-Dichte (r = 0,93): 3,10.
  - Dicht am Monopol ist es 2, wie vorab abgeleitet (Nachtrag, beschreibend):
    - 2,024 bis 2,029 bei r = 0,025; 2,07 bis 2,09 bei r = 0,075; 2,12 bis 2,15 bei r = 0,125
    - bei r = 1 schon 3,1 bis 3,5, bei r = 2 5,6 bis 6,4
  - In keiner nicht trivialen Lesart trifft QM4 ein.
- **K4 (Drehimpuls):** J_z = -Q/2 identisch (4.).
- **K5 (Relaxationsart):** LM-Newton, monoton fallend; bei V0 = 2 konvergiert in 6 bis 18 Schritten.

## 6. Latten (v3)

- **L1 (kann scheitern):** ja.
  - Keine Bindung (mein A1) war moeglich und wahrscheinlich; ebenso eine Bindung ueber das ganze Raster (QM3 falsch).
  - QM4 ist gescheitert, ebenso meine A1, A2, A4, A5.
  - QM1 und die Drehimpulszeile waren vorab ableitbar (Kato bzw. Identitaet). QM0 prueft den Code.
- **L2 (Gegenprobe):**
  - zwei Starts
  - drei Gitter
  - Wu-Yang-Gleichheit (Schreibtisch)
  - Winkeleigenwerte gegen Monopol-Kugelfunktionen
  - 1D gegen qladung2
  - symmetrischer QM0-Start
  - Hesse-Eigenwerte
  - Translationsartefakt als eigene Kontrollrechnung
- **L3 (Numerik):**
  - Newton-Dekrement < 1e-12 E; Gitterfehler zweiter Ordnung.
  - Bei Q >= 1000 bestimmt das Translationsartefakt die absolute Bindung auf etwa 0,05 (F), die Gebunden-Urteile
    aendert es nicht.
- **L4 (schon bekannt):**
  - Haftung eines Q-Balls an Monopolen ueber ein Portal: Bai/Lu/Orlofsky 2022, dort mit globaler Ladung und
    kugelsymmetrischem Ansatz [S, ueber Dossier und SPIN1.md].
  - Monopol-Kugelfunktionen [L Wu/Yang 1976]; Kato [L]; J = Q/2 im Projekt seit SPIN1.md B-V3 [P].
  - Ein geeichter Q-Ball am Monopol hatte im Projekt 0 Metadatentreffer (SPIN1.md E11) [P]. Die "sitzende" Form neben
    dem Monopol kenne ich aus der Literatur nicht [L?]; nicht gesucht.
- **L5 (Messbezug):** keiner.
  - Synthetische Rechnung mit eingesetztem Monopol, eingesetztem Topf und Hintergrundfeld-Naeherung.
  - Monopole sind nicht beobachtet ("no confirmed observations", PDG 2025 [S, ueber SPIN1.md E10c]).

## 7. Selbstanzeigen

1. **Vorwissen vor dem Einfrieren:** rauch1 zeigte die Bindung bei Q = 200, V0 = 2 (1,0; z_c = 2,8; Winkelverhaeltnis
   22). QM2 und QM4 waren damit vor dem Hauptlauf absehbar (PLAN Abschnitt 8).
2. **Regeln nach Rauchlaeufen festgelegt** (vor dem Einfrieren, offengelegt):
   - symmetrischer QM0-Start
   - Abwanderungs-Stopp
   - Gitterreferenz fuer QM1
   - Die QM1-Referenz habe ich gewaehlt, *nachdem* rauch2 eine Verletzung gegen die 1D-Referenz zeigte. Sie ist
     lockerer als der Kartenwortlaut. Darum steht das Urteil nach Kartenwortlaut ("nicht eingetroffen") gleichrangig
     daneben.
   - Schwellen blieben unveraendert.
3. **Abgewandert heisst nicht bewiesen ungebunden.** Bei V0 = 0,5 und 1 koennte ein sehr flaches lokales Minimum
   vom Translationsartefakt (Gefaelle ~0,01 je Laengeneinheit) ueberdeckt sein.
   - Seine Bindung laege aber unter 1e-4 relativ, also weit unter der Schwelle.
   - Ein Lauf mit festgehaltenem Schwerpunkt fehlt.
4. **Eigenwerte nur auf H.** Gitter F lief ohne Minimum-Pruefung; die Zustaende stimmen aber in E und z_c mit H
   ueberein.
5. **Q_max-Bisektion nur auf H.** Der Wert 838 ist gitterabhaengig (3.5).
6. **GPU ungenutzt:** Die Rechnung lief als CPU-scipy in der Spur p4000a, wie im Auftrag vorgegeben. Die Projektregel
   "auf CUDA" ist fuer diese Karte nicht erfuellt.
7. **Lokal:**
   - kein python, awk oder perl
   - benutzt: jq, sed, grep, sha256sum, date, ssh und scp, dazu cp, mv, mkdir, ls, cat, head, tail und wc
   - auf der .69 ausserhalb des Starters nur Dateibefehle (mkdir, mv, ls, grep, jq, sha256sum) und ein ls auf das
     venv, um matplotlib zu finden; kein Interpreterstart
8. **Ein Startertest scheiterte** (rauch5, Bildcode bei nur einem Q). Das ist vor dem Einfrieren behoben (rauch6).
9. **Nachtrag nach dem Hauptlauf:** code/nachtrag_winkel.py habe ich nach den Urteilen geschrieben und gestartet (eigener
   Start ueber kleintest.sh). Es ist beschreibend, aendert kein Urteil und steht nicht im eingefrorenen Plan.
10. **Bild bild-bindung.png:** Die rechte y-Beschriftung ist oben angeschnitten; die Zahlen stehen in 3.1 und 3.3.
11. **Zeitbox:** Start 07:49:10, Abgabe ab 08:34:14 CEST (innerhalb von 120 min).

## 8. Bedeutung

- **Gegen die vorab festgelegte Bedeutung der Karte:**
  - "QM2 trifft ein: Q-Baelle koennen mit Zusatzkraft an Monopolen haften." Ja, aber nur mit genug Zusatzkraft:
    V0 = 2 haftet, V0 = 1 nicht. Die Bindung ist klein (etwa 1, gegen 12 bis 14 Topfbindung ohne Monopol).
  - "Der Verbund traegt J = Q/2 + Z und ist bei ungeradem Q ein Fermion mit grossem Spin." Klassisch gilt J_z = -Q/2
    exakt. Die Quantenaussage (Spektrum, Statistik) prueft diese Rechnung nicht.
  - "QM3 trifft ein: Es gibt eine groesste haftende Ladung. Grosse Q-Baelle loesen sich, weil die Nulllinie mit der
    Groesse teurer wird." Nur zur Haelfte:
    - Nach Kartenkriterium endet die Bindung bei Q ~ 838.
    - Der Ball loest sich aber bis Q = 2000 nicht, und die Nulllinie laeuft nicht durch ihn. Der Ball weicht dem Faden
      aus, indem er sich neben den Monopol setzt.
    - Die absolute Bindung sinkt trotzdem langsam; eine echte Abloesung liegt verlaengert bei Q ~ 2700 bis 3200 [H].
- **Neu fuer das Projekt [E]:**
  - die sitzende, stark asymmetrische Form
  - die Topfschwelle zwischen V0 = 1 und 2
  - die Groesse der Bindung
  - Q_max nach Kartenkriterium
- **Nicht gezeigt:**
  - Statistik
  - ein Monopol im Pfeil-Eis
  - Coulomb-Selbstenergie (vernachlaessigt; QBALL-LADUNG-1: ~ e^2)
  - Stabilitaet gegen nicht axialsymmetrische Stoerungen (der Ansatz erlaubt sie nicht)

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-081541, EINGEFROREN-SHA256.txt, AGENTEN-VORHERSAGEN.md, KARTE.md
- code/:
  - qmonopol.py: Gitter, Funktional, LM-Newton, Eigenwerte, Kennzahlen, Modi rauch und lauf
  - auswertung.py: Urteile und Bilder
  - nachtrag_winkel.py: beschreibender Nachtrag nach dem Hauptlauf (sha256 45a5ed6...), nicht eingefroren
  - je mit Kopie *.eingefroren-20261004-081541
- lauf-69/:
  - haupt.json/.log (H), grob.json/.log (G)
  - fein-v2, fein-v1, fein-v05, fein-v0 (.json/.log, F)
  - qmax.json/.log
  - auswertung.json (mit Vermerken), auswertung.maschine.json, auswertung.log
  - nachtrag-winkel.json/.log (beschreibender Nachtrag)
  - bild-bindung.png, bild-winkel.png, bild-profil.png
  - PRUEFSUMMEN.txt
  - haupt.npz (10,8 MB, sha256 f940292...) bleibt auf der .69 (Felder fuer Bilder und Nachtrag)
- rauch-69/: rauch1 bis rauch3 (.json/.log), t4/ (rauch4 bis rauch6: Testauswertung und Bilder)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-qball-monopol/ (code/, rauch/, lauf/)

## 10. Einfach gesagt

Ein Q-Ball ist ein Klumpen aus vielen gleichen Feldteilchen; hier traegt er die Ladungszahl Q. Am Computer bleibt so ein
Ball an einem magnetischen Pol nur haengen, wenn dort zusaetzlich eine kraeftige Klebemulde sitzt (die staerkste der vier
geprueften). Dann setzt er sich wie ein Tropfen auf den Pol, statt ihn zu umhuellen. Die Haftung ist schwach, etwa ein
halbes Prozent seiner Energie; ab etwa Q = 840 faellt sie unter die vorher festgelegte Schwelle, verschwindet aber bis
Q = 2000 nicht ganz. Der Drehimpuls ist immer genau die halbe Ladungszahl, doch das folgt schon aus der Rechnung auf dem
Papier, und ob sich so ein Verbund wie ein Elektron verhaelt, kann diese Rechnung ohne Quantenteil nicht zeigen; alles ist
Rechnung, keine Messung.
