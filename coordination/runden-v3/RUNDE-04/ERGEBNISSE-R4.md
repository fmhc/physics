# Runde 4 (v3): Ergebnisse der gerechneten Tests

Verfasser: Auswerte-Agent (Anthropic, Opus 5.5) im Auftrag der Leitung claude-primary. Explorativ, keine formale
Bestaetigung. Die Abschaetzung (weiter, parken, verwerfen) entscheidet die Leitung; die Vorschlaege unten sind Vorschlaege.

- **Beginn:** 2026-09-30 02:27:59 CEST (gemessen mit date)
- **Ende:** 2026-09-30 02:47:08 CEST (gemessen mit date, nach dem Schreiben des Inhalts)

**Quellen:**

- Vorhersagen vorab: wellen/PLAN.md, chemie-bio/PLAN.md
- Berichte: wellen/lauf-69/ausgabe/*_bericht.txt (russell, monster, stokes, surfen, brandung) und
  chemie-bio/lauf-69/ausgabe/*_bericht.txt (profil, katalyse, kette, chromatographie, neuron, wunde, nerv, artbildung)
- Ablauf: beide lauf-69/LAUF.log
- Code (wellen.py, chemie_bio.py im jeweiligen lauf-69/) nur gelesen, um Pruefkriterien und Definitionen nachzuschlagen.

**Regeln dieser Auswertung:** Alle Zahlen stammen aus den Berichten. "Fein" heisst dx 0,05 / dt 0,025; wo ein Bericht
grob und fein zeigt, steht fein. Was ein Bericht nicht enthaelt, steht als "nicht im Bericht". Keine Deutung ueber das
Gerechnete hinaus; wo etwas fragwuerdig ist, steht es als Frage.

## Kurzbild

- 12 Tests:
  - 2 getroffen: Kette, Artbildung
  - 6 teilweise: Russell, Monster, Surfen, Katalyse, Neuron, Wunde
  - 4 verfehlt: Stokes, Brandung, Chromatographie, Nervenfaser
- L3 laut Bericht in 10 von 12 bestanden; nicht bestanden bei Russell und Nervenfaser. Gegenprobe (L2) gerissen bei
  Russell (nach dem Codekriterium) und Nervenfaser (d = 40).
- Numerisch fragwuerdig trotz bestandenem L3:
  - Brandung: eine Ladungsbilanz mit negativem Seeanteil
  - Chromatographie: bis 52,6 % Ladungsverlust, 14 von 36 Durchlaufzeiten fehlen
  - Katalyse und Kette: der L3-Effekt misst nicht den Kartenbefund
- Offene Frage mit Gewicht: Stokes skaliert linear statt quadratisch in a; ein Starteffekt ist nicht ausgeschlossen (B1).
- Lauf: beide Ketten laut LAUF.log auf spur=p4000b (Quadro P4000), alle Aufrufe rc = 0, laengster Aufruf 2 min 32 s
  (artbildung). Die Uhrzeiten in Logs und Berichten sind UTC.

**Legende der Latten-Woerter:**

- L1 (kann scheitern): ja, oder teils (Teile vorab ableitbar, laut CB-PLAN Abschnitt 6)
- L2 (Gegenprobe) und L3 (Aufloesung): bestanden oder gerissen, laut Bericht
- L4 (schon bekannt) und L5 (Messbezug): aus dem jeweiligen PLAN uebernommen. Die Literatur dort stammt aus dem
  Gedaechtnis und ist nicht nachgelesen; die Berichte pruefen L4 und L5 nicht.

## 1. Je Test

### 1.1 Russell (Wellen 1)

- **Vorhersage (PLAN 4.1):**
  - Einzelball "abgestrahlt unter 1e-5".
  - Gleichphasig v = 0,1: "Die Baelle verschmelzen ... Bis t_m sind 3 bis 9 Prozent der Energie abgestrahlt."
  - Gleichphasig 0,3 und 0,5: "laufen durcheinander hindurch ... Abgestrahlt 1e-4 bis 1e-2, bei 0,5 weniger als bei 0,3."
  - Gegenphasig: "verschmelzen nie. Abgestrahlt unter 1e-3 bei v = 0,1, 1e-3 bis 1e-2 bei 0,3 und 0,5."
  - Hypothese H (Anteil haengt von v ab): "erwartet ja".
- **Ergebnis (abgestrahlter Energieanteil, fein):**

  | v | gleichphasig | gegenphasig | einzeln (Kontrolle) |
  |---|---|---|---|
  | 0,1 | 6,798e-02 (X bei t_m 5,53; v danach 0,0140; "getrennt") | 2,221e-07 | 2,081e-07 |
  | 0,3 | 6,614e-02 (v danach 0,2345; S_max-Verhaeltnis 0,7840) | 4,915e-05 | 1,145e-07 |
  | 0,5 | 3,597e-02 (v danach 0,4721; S_max-Verhaeltnis 0,7655) | 5,770e-05 | 5,800e-08 |

  - Grob gleichphasig: 6,797e-02 / 6,621e-02 / 3,583e-02. K0 (Profil gegen Anker) 1,2e-10, bestanden.
- **Getroffen?** Teilweise.
  - Getroffen: Einzelball unter 1e-5; gleichphasig v = 0,1 im Band 3 bis 9 %; gegenphasig v = 0,1 unter 1e-3; H;
    Reihenfolge "bei 0,5 weniger als bei 0,3".
  - Verfehlt: gleichphasig 0,3 und 0,5 liegen ueber dem Band 1e-4 bis 1e-2; gegenphasig 0,3 und 0,5 liegen unter dem
    Band 1e-3 bis 1e-2.
  - Verschmelzen bei v = 0,1: laut Bericht "getrennt" (X = 5,53 bei der Codeschwelle |X| < 5, siehe C7).
- **L3 laut Bericht:** nicht bestanden (kleinster Effekt 2,221e-07, groesste Aenderung grob/fein 1,376e-04). L2 ebenfalls
  nicht bestanden (Einzelball bis 2,081e-07 gegen kleinsten Stoss 2,221e-07); siehe A3.
- **Latten:** L1 ja · L2 gerissen · L3 gerissen · L4 weitgehend · L5 mittelbar
- **Vorschlag: parken.** Die gleichphasige Abstrahlung ist grob/fein stabil (6,797e-02 gegen 6,798e-02), aber laut PLAN
  weitgehend bekannt, und L2/L3 scheitern formal am gegenphasigen v = 0,1-Stoss, der sich nicht vom Einzelball
  unterscheidet.

### 1.2 Monsterwelle (Wellen 2)

- **Vorhersage (PLAN 4.2):**
  - S0 = 0,8: Verhaeltnis "bei M + 2 und M + 3 sd zwischen 0,5 und 2"; "S_max/S0 unter 1,02; keine Ueberschreitung von
    4 S0".
  - S0 = 0,3: 4-S0-Ueberschreitungen "seltener als nach Rice (Verhaeltnis unter 1)"; "S_max/S0 hoechstens 4,3".
  - S0 = 0,1: "Verhaeltnis ueber 3 im Spaetfenster", "Persistenz ueber 0,8"; Q-Baelle mit "S in der Mitte 0,45 bis 0,55".
  - Hypothese H der Karte: "in keiner der beiden Dichten bestaetigt". Erhaltung: Drift von E und Q "unter 1e-5".
- **Ergebnis (Fenster 50-150 / 150-300):**
  - S0 = 0,8 (Referenz Rice): M+2sd 1,01 / 0,966; M+3sd 1,04 / 0,954; S_max/S0 1,005 / 1,005; bei 4 S0 keine
    Ueberschreitung. M+4sd 1,69 / 0,862; M+5sd 4,43 (6 gegen 0,968) / 0,257.
  - S0 = 0,3 (Referenz Rayleigh, weil V >= M^2): 4 S0 0,0404 / 0,116; 2 M 1,45 / 1,6; M+2sd 1,15 / 1,54;
    S_max/S0 4,468 / 4,592; Persistenz 0,299 / 0,295.
  - S0 = 0,1 (Referenz Rice / Rayleigh): 4 S0 1,32 / 1,77; Persistenz 0,828 / 0,844; S_max/S0 8,918 / 9,849.
  - Erhaltung (fein): dE 2,5e-06 / 8,0e-06 / 3,4e-10 (S0 = 0,1 / 0,3 / 0,8); dQ hoechstens 7,8e-16.
  - L2 bestanden (0,966 und 0,954).
- **Getroffen?** Teilweise.
  - Getroffen: stabile Kontrolle; S0 = 0,3 leichter Schwanz bei 4 S0; S0 = 0,1 Persistenz ueber 0,8; Erhaltung; H nach der
    vorab festgelegten Lesart nicht bestaetigt.
  - Verfehlt: S0 = 0,1 Verhaeltnis 1,77 statt ueber 3; S0 = 0,3 S_max/S0 4,468 und 4,592 statt hoechstens 4,3;
    S0 = 0,1 S_max/S0 9,849, also S_max nahe 0,98, ueber der vorhergesagten Mittendichte 0,45 bis 0,55.
  - Saettigungszeiten, omega und Profile der Klumpen: nicht im Bericht.
- **L3 laut Bericht:** bestanden (S0 = 0,1: log-Verhaeltnis 0,569, Aenderung 8,6e-05; S0 = 0,3: -2,154, Aenderung 0,0534).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 weitgehend · L5 mittelbar
- **Vorschlag: verwerfen.** Die Kartenhypothese (kurzlebige Spitzen haeufiger als Zufall) ist nach der vorab
  festgelegten Lesart bei beiden Dichten nicht gestuetzt (0,3: 4-S0-Spitzen seltener; 0,1: haeufiger, aber langlebig),
  der Rest ist laut PLAN bekannte Q-Ball-Bildung.

### 1.3 Stokes-Drift (Wellen 3)

- **Vorhersage (PLAN 4.3):**
  - "Der Ball driftet in Laufrichtung der Welle, dX ~ a^2: dX(0,02)/dX(0,01) und dX(0,04)/dX(0,02) je 4 +- 0,8."
  - "dX(0,04) etwa 0,01 bis 1." Die Drift je Periode "waechst mit der Zeit (Beschleunigung)".
  - Vorzeichen: "Ich erwarte + (etwa 70 Prozent)."
  - Stehend mit Bauch und ohne Welle: "|dX| unter 1e-9". Links gegen rechts: "auf 1e-6". Knoten: "|dX| unter einem
    Zehntel des laufenden Werts". "Ladungsaenderung des Balls unter 1e-3."
- **Ergebnis (fein):**
  - laufend a = 0,01 / 0,02 / 0,04: dX 1,4368 / 2,9168 / 6,0083; Verhaeltnisse 2,030 und 2,060 (Bericht:
    L1_skalierung_a2 nicht bestanden).
  - Drift je Periode 1,818e-02 / 3,691e-02 / 7,603e-02; v_anfang 4,101e-03 / 8,319e-03 / 1,707e-02; Beschleunigung
    2,470e-08 / 8,170e-08 / 5,469e-07; dQ_Fenster -1,9e-05 / -9,0e-05 / -2,4e-04.
  - nach links a = 0,04: dX -6,0083; Summe rechts plus links -4,97e-14.
  - stehend mit Bauch: dX -1,095e-06 (grob 3,615e-05); ohne Welle: 6,6e-11 (grob 2,1e-09); stehend mit Knoten: 0,14708.
  - dQ_Fenster stehend: 1,2e-03 (Bauch) und 1,4e-03 (Knoten).
  - L2 und Spiegelprobe bestanden.
- **Getroffen?** Verfehlt (Kernvorhersage).
  - Verfehlt: dX waechst etwa linear mit a statt mit a^2; dX(0,04) = 6,0 liegt ueber 0,01 bis 1; die Beschleunigung ist
    klein, v_anfang waechst ebenfalls etwa linear mit a.
  - Getroffen: Vorzeichen +, Spiegelprobe, Knoten unter einem Zehntel (0,147 gegen 6,008).
  - Knapp verfehlt: Bauch 1,1e-06 statt unter 1e-9; Ladungsaenderung stehend 1,2e-03 und 1,4e-03 statt unter 1e-3.
- **L3 laut Bericht:** bestanden (dX(0,04) fein 6,0083, grob 6,0101).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 teilweise · L5 keiner
- **Vorschlag: weiter, zuerst klaeren.** Die a^2-Vorhersage ist bei bestandenem L3 klar verfehlt, aber vor jeder Deutung
  ist offen, ob die zu a proportionale Anfangsgeschwindigkeit aus dem Startzustand stammt (B1).

### 1.4 Surfen (Wellen 12)

- **Vorhersage (PLAN 4.4):**
  - "Kein Mitnehmen bei allen A." Der Ball wird "zuerst zum Paket hin gezogen (X_min < 0)".
  - "Endgeschwindigkeit klein und positiv ...: unter 3e-3 bei A = 0,1 und unter 1e-2 bei A = 0,2. Fuer A <= 0,1 skaliert
    sie mit A^2 (Verhaeltnisse etwa 4)."
  - "Energiegewinn unter 1 Prozent." Bei A = 0,2: "S_max der Welle allein steigt ueber A^2 = 0,04".
  - Gegenprobe: "|v| unter 1e-6, Energiegewinn unter 1e-5".
- **Ergebnis (fein), A = 0,025 / 0,05 / 0,1 / 0,2:**
  - mitgenommen: bei keinem A
  - v_ende 2,385e-04 / 9,450e-04 / 4,003e-03 / 1,123e-02; Verhaeltnisse 3,962 und 4,236
  - X_min -0,011 / -0,040 / -0,179 / -1,093; X_max 0,037 / 0,139 / 0,537 / 0,696
  - Energiegewinn relativ -1,98e-05 / -4,48e-05 / 4,89e-05 / 2,02e-03; dQ relativ bis -6,9e-03 (A = 0,2)
  - S_max des Balls waehrend des Durchgangs bei A = 0,2 zwischen 0,4718 und 1,4700 des Anfangswerts
  - S_max der Welle allein 6,250e-04 / 2,500e-03 / 1,559e-02 / 2,127e-01
  - ohne Welle: v -7,9e-20, Energiegewinn -9,14e-09; L2 bestanden
- **Getroffen?** Teilweise, Kern getroffen.
  - Getroffen: kein Mitnehmen, X_min < 0, A^2-Skalierung, Energiegewinn unter 1 %, Selbstfokussierung bei A = 0,2,
    Gegenprobe.
  - Verfehlt: v_ende 4,003e-03 ueber 3e-3 (A = 0,1) und 1,123e-02 ueber 1e-2 (A = 0,2).
- **L3 laut Bericht:** bestanden (A = 0,1: 4,003e-03 fein, 4,008e-03 grob; A = 0,2: 1,1230e-02 fein, 1,1271e-02 grob).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 vermutlich · L5 keiner
- **Vorschlag: parken.** Im Ein-Feld-Modell ist die Karte nur als freies Paket rechenbar, dort gibt es kein Mitnehmen und
  keinen Messbezug; die urspruengliche Form (Welle auf einem Medium) braucht laut PLAN Abschnitt 1 ein zweites Feld.

### 1.5 Brandung (Wellen 13)

- **Vorhersage (PLAN 4.5):**
  - "Ueberwiegend 'aufgenommen': Zerfall ja in mindestens 9 der 12 Laeufe." "Nahe gegenphasig bei v = 0,1 ist
    'zurueckgeworfen' moeglich".
  - "Nie 'durchgereicht' (Anteil hinter dem See unter 0,1)."
  - "Verformung vor dem Kontakt unter 1e-3".
  - "Die linke Wand wandert um 0,5 bis 1,7 zum Ball hin (x_wand sinkt)".
  - Gegenproben: See allein "Wand wandert hoechstens 0,5, Seeladung aendert sich hoechstens um 1e-3"; Ball allein
    "Verformung vor x = 10 unter 1e-3".
- **Ergebnis:**
  - Ausgang: 9 von 12 "zerbrochen oder teilweise aufgenommen"; 3 von 12 "durchgereicht" (v = 0,3 / Phase 0,5;
    v = 0,5 / Phase 0,5; v = 0,5 / Phase 1,0); kein Lauf "aufgenommen" oder "zurueckgeworfen".
  - Anteil im See 0,057 bis 0,504, einmal -2,441 (v = 0,5 / Phase 0,5). Anteil hinter dem See ueber 0,1 in 7 von 12
    Laeufen, hoechstens 3,406. S_max vorn am Ende 0,006 bis 0,195 des Anfangswerts.
  - Verformung vor Kontakt: S 2,4e-03 bis 1,7e-02, Breite 7,5e-02 bis 1,3e-01.
  - Wandverschiebung -1,30 bis +5,60; 6 von 12 im Band -0,5 bis -1,7; 4 positiv (+0,90; +0,95; +1,30; +5,60).
  - See allein: Wand 0,000, Q_See -9,1e-09. Ball allein: Verformung 8,3e-04. Beide Gegenproben bestanden.
- **Getroffen?** Verfehlt.
  - Verfehlt: kein Lauf "aufgenommen", drei "durchgereicht" (vorhergesagt: nie); Verformung vor Kontakt 2,4e-03 bis
    1,7e-02 statt unter 1e-3; Wandverschiebung nur in 6 von 12 Laeufen im Band.
  - Getroffen: beide Gegenproben; vorn bleibt in keinem Lauf mehr als 0,195 des Anfangs-S_max.
- **L3 laut Bericht:** bestanden (Ausgang grob = fein in allen Laeufen, Anteile aendern sich hoechstens um 0,056; der Code
  vergleicht dabei nur die Anteile vor und See).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 teilweise · L5 mittelbar
- **Vorschlag: weiter, zuerst klaeren.** Die Vorhersage ist bei bestandenem L3 und bestandenen Gegenproben klar verfehlt,
  aber die Bilanz des Laufs v = 0,5 / Phase 0,5 ist ohne eine Messung der rechten Wand bzw. der Seeladung je Seite nicht
  lesbar (C1).

### 1.6 Katalyse (Chemie 8)

- **Vorhersage (PLAN 4.1):**
  - "dphi = pi, ohne: keine Verschmelzung bei irgendeinem v".
  - dphi = 3pi/4, ohne: "offen"; Hypothese "Verschmelzung hoechstens in einem mittleren v-Fenster".
  - bruecke: "Bei kleinem v (<= 0,2) entsteht mindestens ein Klumpen mit etwa 2 Q0. Dieselbe Verschmelzung zeigt aber
    schon nur_AC: C wirkt als Reaktionspartner, nicht als Katalysator."
  - sperre bei 3pi/4: "weniger Verschmelzung als ohne".
  - Codeprobe: bei dphi = pi muessen bruecke und sperre gleich sein.
- **Ergebnis (Muster grob = fein; groesster Klumpen in Q0, fein):**
  - pi: ohne ........ (0,93 bei v <= 0,2; 0,00 ab v = 0,4); bruecke ..x..... (v = 0,15: 1,52); sperre ..x..... (alle
    Werte gleich bruecke); nur_AC ........ (hoechstens 1,30)
  - 3pi/4: ohne ........ (hoechstens 1,01); bruecke .x...... (v = 0,1: 1,53); sperre ........ (hoechstens 1,47);
    nur_AC ........ (hoechstens 1,32)
  - bruecke bei v <= 0,2: 1,18 / 1,46 / 1,52 / 1,49 (pi) und 1,45 / 1,53 / 1,46 / 1,37 (3pi/4)
- **Getroffen?** Teilweise.
  - Getroffen: pi ohne verschmilzt nie (Symmetriesatz, vorab ableitbar); Codeprobe bruecke = sperre.
  - Verfehlt: kein Klumpen mit etwa 2 Q0 (hoechstens 1,53); nur_AC verschmilzt bei keinem v, "Dieselbe Verschmelzung
    zeigt aber schon nur_AC" trifft nicht zu.
  - Nicht entscheidbar: "sperre weniger als ohne" (beide ohne Verschmelzung).
  - 3pi/4 ohne (offen vorhergesagt): keine Verschmelzung bei irgendeinem v.
- **L3 laut Bericht:** bestanden (Effekt 0,9887, Aenderung 2,8e-03, Klassen 64 von 64 gleich); zur Effektgroesse siehe C4.
- **Latten:** L1 teils · L2 bestanden · L3 bestanden · L4 teilweise · L5 keiner
- **Vorschlag: weiter, zuerst klaeren.** Der in PLAN Abschnitt 5 genannte Fall "bruecke verschmilzt, nur_AC nicht" ist
  eingetreten, aber nur an je einem v-Punkt mit 1,52 bzw. 1,53 Q0 knapp ueber der Schwelle 1,5 Q0; ein feineres v-Raster
  und eine Schwellenvariation muessten zeigen, ob er traegt.

### 1.7 Kettenreaktion (Chemie 16)

- **Vorhersage (PLAN 4.2):**
  - "Die Front erlischt; Reichweite 0, hoechstens 1."
  - "Bei d_in = 16 verschmelzen zuend und kalt fast gleichzeitig (etwa 170, Faktor 2), also ohne Front."
  - "Bei d_in = 24 verschmilzt in kalt nichts, in zuend nur Paar 0."
  - Fallzeiten (Handrechnung): "19 / 171 / 510 / 1520 fuer d = 8 / 16 / 20 / 24".
- **Ergebnis (Fusionszeiten der Paare 0 bis 4):**
  - Zuendpaar allein: 13
  - d_in = 16: Einzelpaar 167; zuend [13, None, 163, 163, 165]; kalt [165, 162, 162, 162, 165]
  - d_in = 20: Einzelpaar 507; zuend [13, 461, None, 494, 500]; kalt [500, 493, 493, 493, 500]
  - d_in = 24: Einzelpaar None; zuend [13, None, None, None, None]; kalt alle None
  - gezuendet (t_zuend < 0,8 t_kalt): bei keinem Paar; Reichweite 0 bei allen d_in
- **Getroffen?** Getroffen.
  - Reichweite 0; d_in = 16 fast gleichzeitig; d_in = 24 wie vorhergesagt.
  - Einzelpaare 167 / 507 / None nahe der Handrechnung 171 / 510 / 1520 (Zuendpaar 13 gegen 19).
  - Nicht vorhergesagt: In zuend verschmilzt Paar 1 (d_in = 16) bzw. Paar 2 (d_in = 20) bis T = 600 gar nicht.
- **L3 laut Bericht:** bestanden (Effekt 438, Aenderung 1,0, Fusion 50 von 50 gleich); zur Effektgroesse siehe C5.
- **Latten:** L1 teils · L2 bestanden · L3 bestanden · L4 wahrscheinlich · L5 keiner
- **Vorschlag: verwerfen.** Die Kartenhypothese (laufende Front) tritt bei keinem der drei Abstaende ein, das Ergebnis war
  aus den Fallzeiten vorab ableitbar, und es gibt keinen Messbezug.

### 1.8 Chromatographie (Chemie 20)

- **Vorhersage (PLAN 4.3):**
  - "Der grosse Ball (omega^2 = 0,6) braucht laenger."
  - Trennung t(0,6) - t(0,8): "etwa +1 / +5 / +11 Zeiteinheiten bei eps = 0,01 / 0,02 / 0,03"; Streuung je Seed
    "+-1 / +-2 / +-3".
  - "Ordnung 0,6 > 0,7 > 0,8: bei eps = 0,03 in mindestens 3 von 4 Seeds".
  - Mittlere Verzoegerung "bei eps = 0,02: etwa 3,7 / 2,7 / 1,9 Prozent".
  - Reflexion bei eps = 0,03 "in 1 bis 2 Seeds" (omega^2 = 0,6). "Ladungsverlust unter 1e-3."
  - Gegenprobe glatt: "Spannweite unter 0,1".
- **Ergebnis:**
  - glatt: 266,691 / 266,685 / 266,676, Spannweite 0,0153
  - eps = 0,01: Trennung im Mittel -2,83, Spannweite 11,0; Ordnung in 0 von 4 Seeds; Verzoegerung 2,9 / 8,1 / 4,0 %
  - eps = 0,02: Trennung im Mittel -3,66, Spannweite 13,07; Ordnung in 0 von 4; Verzoegerung 12,8 / 10,5 / 12,2 %;
    4 von 12 Durchlaufzeiten None
  - eps = 0,03: Trennung im Mittel None; Ordnung in 0 von 4; Verzoegerung 14,0 / None / 13,2 %; 10 von 12
    Durchlaufzeiten None
  - reflektiert: 0 in allen Laeufen; Ladungsverlust im Fenster hoechstens 5,26e-01 (laut Code relativ,
    1 - Q_Ende/Q_Anfang)
  - Gegenprobe bestanden
- **Getroffen?** Verfehlt.
  - Verfehlt: Trennung negativ statt positiv; Ordnung bei keinem eps in irgendeinem Seed; Verzoegerung bei eps = 0,02
    10,5 bis 12,8 % statt 1,9 bis 3,7 %; keine Reflexion, aber 14 von 36 Durchlaufzeiten fehlen; Ladungsverlust bis
    52,6 % statt unter 1e-3.
  - Getroffen: nur die glatte Gegenprobe.
- **L3 laut Bericht:** bestanden (Effekt 3,656, Aenderung 0,479); gilt nur fuer die Laeufe mit Durchlaufzeit (C2).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 teilweise · L5 mittelbar
- **Vorschlag: parken.** Die Vorhersage ist klar verfehlt, aber mit bis zu 52,6 % Ladungsverlust und 14 von 36 fehlenden
  Durchlaufzeiten traegt die Messgroesse Durchlaufzeit nicht; zuerst Aufbau und Potentialstaerke klaeren.

### 1.9 Neuron (Bio 13)

- **Vorhersage (PLAN 4.4):**
  - "Kein Sprung. Kleine Stoesse: Spitze ~ |eps|, Spitze/|eps| auf 20 Prozent konstant fuer |eps| <= 0,1. Darueber wird
    die Antwort unterlinear und glatt."
  - "Abgestrahlte Ladung etwa ~ eps^2, bei eps = 1 einige Prozent."
  - "Keine Spaltung, kein Zerfall: ... auch ein Ball mit 25 Prozent der Ladung (amplitude -0,5) entspannt sich zu einem
    breiten Ball mit omega^2 etwa 0,98."
- **Ergebnis:**
  - dehnung, |eps| <= 0,1: Spitze/|eps| 1,161 bis 1,273. Fuer |eps| > 0,1: +eps 1,099 bis 1,336; -eps 1,324 / 1,373 /
    1,467 / 1,559 / 1,681 (eps = -0,2 bis -1,0). Klumpenzahl 1 in allen dehnung-Laeufen.
  - Q abgestrahlt (relativ), dehnung +eps: 6,35e-05 bei 0,1, 1,10e-01 bei 1,0. Dehnung -eps: negativ ab -0,1, bis
    -2,44e-03.
  - amplitude: Spitze/|eps| zwischen 1,938 (-0,5) und 4,967 (+0,1). amplitude -0,3: Q abgestrahlt 1,01e-01, omega^2 am
    Ende 0,9366. amplitude -0,5: Klumpen 0, Q abgestrahlt 6,19e-01, omega^2 am Ende 0,9962.
  - Spruenge: 1 (amplitude -0,3 nach -0,5: Klumpenzahl 1 nach 0; Spitze/|eps| 2,922 nach 1,938).
- **Getroffen?** Teilweise.
  - Getroffen: linearer Bereich (1,161 bis 1,273, innerhalb 20 %); dehnung-Reihe ohne Sprung.
  - Verfehlt: ueber |eps| = 0,1 nicht unterlinear (bei -eps steigt Spitze/|eps| bis 1,681); abgestrahlte Ladung
    6,35e-05 bei eps = 0,1 und 1,10e-01 bei eps = 1,0 (eps^2 erwartete den Faktor 100) und damit 11 % statt "einige
    Prozent"; amplitude -0,5 mit Klumpenzahl 0 und 62 % abgestrahlter Ladung statt "kein Zerfall"; omega^2 0,9962 statt
    etwa 0,98.
- **L3 laut Bericht:** bestanden (Effekt 1,681, Aenderung 9,7e-04, Klumpenzahl 25 von 25 gleich).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 wahrscheinlich · L5 keiner
- **Vorschlag: parken.** Die einzige Sprungmeldung ist ein Wechsel der Klumpenzahl an der Schwelle S > 0,01 beim
  schwaechsten Ball, fuer den PLAN Abschnitt 5 zuerst eine Variation der Klumpenschwelle verlangt; ein Messbezug fehlt.

### 1.10 Wundheilung (Bio 27)

- **Vorhersage (PLAN 4.5):**
  - "Heilzeit der Schiefe: einige zehn Zeiteinheiten ..., mit dem Schaden wachsend."
  - "Heilzeit der Form: oft nicht erreicht".
  - "Abgestrahlte Ladung: unter 1 Prozent bei 10 Prozent Schnitt, einige Prozent bei 50 Prozent."
  - "Neues omega^2 bei 0,7: etwa 0,743 / 0,81 / 0,91 ..., falls kaum Ladung abgestrahlt wird"; bei 0,55 "etwa 0,575 /
    0,636 / 0,797".
  - Gegenproben: symmetrisch "Die Schiefe bleibt auf Rundungsniveau"; null "Formfehler nur auf Gitterniveau (etwa
    1e-4)".
- **Ergebnis (Schnitt 10 / 25 / 50 %):**
  - Heilzeit der Schiefe: 28 / 23 / 22 (omega^2 = 0,7) und 50 / 29 / 21 (0,55)
  - Heilzeit der Form: None in allen Faellen ausser 0,55 mit 10 % (118) und 0,55 symmetrisch (400,0)
  - Q abgestrahlt (relativ): 5,92e-02 / 1,80e-01 / 6,81e-01 (0,7) und 4,30e-02 / 1,07e-01 / 3,43e-01 (0,55); symmetrisch
    3,52e-01 (0,7) und 1,99e-01 (0,55)
  - omega^2 am Ende (aus Q): 0,7668 / 0,8671 / 0,9906 (0,7) und 0,5880 / 0,6813 / 0,9054 (0,55)
  - symmetrisch: |Schiefe|max 5,4e-17 bzw. 6,2e-17; null: Formfehler am Ende 8,0e-05 bzw. 4,9e-05
- **Getroffen?** Teilweise.
  - Getroffen: Die Schiefe heilt in einigen zehn Zeiteinheiten; die Form heilt meist nicht; beide Gegenproben.
  - Verfehlt: Die Heilzeit der Schiefe faellt mit dem Schaden, statt zu wachsen. Abgestrahlte Ladung 5,9 % bzw. 4,3 % bei
    10 % Schnitt (statt unter 1 %) und 68 % bzw. 34 % bei 50 % (statt einige Prozent). omega^2 am Ende liegt ueber den
    vorhergesagten Werten, deren Bedingung "kaum Ladung abgestrahlt" nicht erfuellt ist.
- **L3 laut Bericht:** bestanden (alle 12 Vergleiche ok, z. B. Heilzeit 30 grob gegen 28 fein bei 0,7 / 10 %).
- **Latten:** L1 ja · L2 bestanden · L3 bestanden · L4 wahrscheinlich · L5 keiner
- **Vorschlag: parken.** Numerik und Gegenproben sind sauber, aber laut PLAN ist das wahrscheinlich bekannte Relaxation
  ohne Messbezug; die beiden klaren Abweichungen stehen unter B6.

### 1.11 Nervenfaser (Bio 41)

- **Vorhersage (PLAN 4.6):**
  - stoss: "Tempo je Glied: etwa 0,5 / 0,4 / 0,33 / 0,25 fuer d = 9 / 12 / 15 / 40, also stets schneller als v = 0,2."
    "Daempfung je Glied: mindestens 0,9 fuer d >= 12". "Bei d = 40 wird der Stoss trotzdem weitergeleitet, nur
    ballistisch".
  - atem: "Keine Weiterleitung bei allen d: Ball 1 bleibt unter 10 Prozent von Ball 0."
  - Gegenproben: ruhe (Signal 0) und d = 40 (keine Atem-Weiterleitung).
- **Ergebnis:**
  - stoss, Tempo je Glied: d = 9 [1,0; 0,45; 0,45; None; 0,14]; d = 12 [0,52; 0,40; 0,46; 0,14; None]; d = 15 [0,30;
    0,38; 0,54; 0,28; 0,44]; d = 40 keine Ankunft ausser Ball 0, Weiterleitung False
  - stoss, Daempfung je Glied: d = 12 [5,811; 0,709; 0,347; 0,429; 0,755]; d = 15 [0,923; 0,632; 0,762; 2,808; 0,411]
  - stoss, Amplitude von Ball 0: 0,181 / 0,196 / 1,289 / 3,973 (d = 9 / 12 / 15 / 40); groesste Amplitude der anderen
    Baelle 1,127 (d = 9), 1,1365 (d = 12), 1,606 (d = 15)
  - atem: Weiterleitung True bei allen vier d; Ball 1 zu Ball 0: 0,6 / 0,423 / 0,355 / 0,167
  - Ausdehnung der ruhenden Kette bis T: 147,88 / 61,07 / 21,79 / 0,00
- **Getroffen?** Verfehlt.
  - atem wird bei allen d weitergeleitet (Ball 1 bei 16,7 bis 60 % von Ball 0), auch in der Gegenprobe d = 40.
  - Daempfung je Glied bei d >= 12: nur ein Wert zwischen 0,9 und 1 (0,923), dazu Werte ueber 1 (5,811; 2,808).
  - Der Stoss wird bei d = 40 nicht weitergeleitet (vorhergesagt: ballistisch weitergeleitet).
  - Tempo je Glied liegt teils im vorhergesagten Bereich, aber mit fehlenden und ungeordneten Ankunftszeiten.
- **L3 laut Bericht:** NICHT bestanden (stoss: kuerzeste Laufzeit 9,0 gegen Aenderung einer Ankunftszeit 14,0; atem:
  0,0722 gegen 1,07e-04).
- **Latten:** L1 ja · L2 gerissen · L3 gerissen · L4 teilweise · L5 mittelbar
- **Vorschlag: parken.** Die Messung traegt nicht (L3 und Gegenprobe d = 40 gerissen, Amplituden ueber 1, Bezugskette
  dehnt sich um bis zu 148 aus); vor einer Wiederholung Aufbau und Messgroesse klaeren.

### 1.12 Artbildung (Bio 18, Zufallskarte)

- **Vorhersage (PLAN 4.7):**
  - 3D m = 0: "Q(omega) ist U-foermig". "Einziger Knick: Q_min innen, grob bei omega^2 = 0,8 bis 0,93 und Q_min etwa 40 bis
    150". "E = Q wird bei kleinerem omega^2 als Q_min gekreuzt".
  - 2D m = 0: "keine Verzweigung"; Q faellt "auf etwa 11,7 bis 11,9 bei 0,99".
  - 2D m = 1, 2: "ebenfalls monoton"; Q bei 0,99 "etwa 48 bzw. 89"; ungueltig "nahe der duennen Wand (etwa
    omega^2 < 0,52)".
  - "Artgrenzen: keine."
  - Numerik: "Virialrest unter 1e-4"; Probe dE = omega dQ "im Median unter 1e-3, nahe der duennen Wand bis etwa 1e-2".
- **Ergebnis:**
  - 3D m = 0: 49 von 49 gueltig; Q_min 111,91 bei omega^2 = 0,93 (innen); einziger Vorzeichenwechsel von dQ bei 0,93;
    E = Q bei 0,846; Q 2,17e+06 bei 0,51 und 200,8 bei 0,99
  - 2D m = 0: 49 von 49 gueltig; kein Vorzeichenwechsel; Q(0,99) = 11,823
  - 2D m = 1: 35 von 49 gueltig (0,65 bis 0,99); kein Vorzeichenwechsel; Q(0,99) = 48,65
  - 2D m = 2: 41 von 49 gueltig (0,56 bis 0,99; 0,57, 0,59 und 0,60 ungueltig); kein Vorzeichenwechsel;
    Q(0,99) = 90,40
  - Artgrenzen: keine (alle drei Paare leer)
  - Virialrest der gueltigen Zeilen hoechstens 6,2e-09; dE-Probe Median 1,4e-04 bis 5,9e-04, Maximum 4,1e-04 bis 5,9e-03
- **Getroffen?** Getroffen. Einzige Abweichung: Der ungueltige Bereich reicht bei m = 1 bis 0,64 und bei m = 2 bis 0,60
  statt nur bis etwa 0,52.
- **L3 laut Bericht:** bestanden (kleinste relative Q-Variation 0,929 gegen Aenderung h/2h 5,7e-06; Gueltigkeit 196 von
  196 gleich).
- **Latten:** L1 teils · L2 bestanden · L3 bestanden · L4 weitgehend · L5 keiner
- **Vorschlag: verwerfen (als Karte).** Es gibt keine Artgrenze, alle Kernvorhersagen sind wie vorab abgeleitet getroffen,
  laut PLAN weitgehend Literatur und ohne Messbezug; die Q(omega)-Tabellen bleiben in artbildung.json als Nachschlagewerte.

## 2. Auffaelligkeiten

### A. Kontrollen oder L3 gerissen

- **A1 Nervenfaser, L3 und Gegenprobe d = 40.**
  - L3 nicht bestanden: Eine Ankunftszeit aendert sich zwischen grob und fein um 14,0; die kuerzeste Laufzeit je Glied
    ist 9,0.
  - Die Gegenprobe "d = 40, keine Atem-Weiterleitung" reisst: Ball 1 erreicht 0,167 der Amplitude von Ball 0,
    Ankunftszeiten 3 / 64 / 146 / 300.
  - PLAN begruendet die Vorhersage mit einer Kopplung ueber die Schwaenze ~ e^{-kappa d}. Ob das Signal bei d = 40 auf
    anderem Weg ankommt (etwa als Strahlung von Ball 0), zeigt der Bericht nicht.
- **A2 Nervenfaser, Messgroesse.**
  - Die stoss-Amplitude ist laut Code (chemie_bio.py, test_nerv) die Zeitableitung der Schwerpunktsdifferenz zu ruhe,
    also eine Geschwindigkeit.
  - Sie erreicht 1,127 (d = 9), 1,1365 (d = 12), 1,606 (d = 15) und 3,973 (d = 40, Ball 0). Bei c = 1 (CB-PLAN
    Abschnitt 1) kann kein Ball so laufen.
  - Ball 0 startet mit v = 0,2 und zeigt 0,181 bzw. 0,196 (d = 9, 12), aber 1,289 bzw. 3,973 (d = 15, 40).
  - Weiter: atem-Tempo 3,0 im ersten Glied bei d = 12 (Ankunft 3 und 7), also schneller als c = 1. Ungeordnete
    Ankunftszeiten: d = 9 stoss Ball 4 bei 44 vor Ball 3 bei 50; d = 12 stoss Ball 5 bei 158 vor Ball 4 bei 165.
    Daempfung je Glied ueber 1: 7,537; 5,811; 4,219; 2,808; 1,222.
  - Die ruhende Bezugskette dehnt sich bis T um 147,88 (d = 9) und 61,07 (d = 12) aus.
  - Tempo und Daempfung je Glied sind damit nicht belastbar.
- **A3 Russell, L2 und L3.**
  - Beide scheitern am gegenphasigen Stoss v = 0,1 (2,221e-07), der auf Hoehe des Einzelballs liegt (bis 2,081e-07).
  - Der Code prueft fuer L2 "kleinster Stoss >= 5 x groesster Einzelball" (wellen.py Z. 376). PLAN 4.1 nennt als Scheitern
    dagegen "alle Stoesse weniger als das Fuenffache des Einzelballs". Diese Bedingung ist nicht erfuellt: Fuenf von
    sechs Stoessen liegen bei 4,9e-05 bis 6,8e-02.
  - Fuer L3 stimmen PLAN und Code ueberein (kleinster Effekt gegen groesste Aenderung). Die groesste Aenderung stammt aus
    gleichphasig v = 0,5 (3,583e-02 grob, 3,597e-02 fein).
  - Welche Lesart fuer L2 gilt, entscheidet die Leitung.

### B. Klare Widersprueche zur Vorhersage

- **B1 Stokes: Drift linear statt quadratisch in a.**
  - Verhaeltnisse 2,030 und 2,060 statt 4 +- 0,8. v_anfang waechst ebenfalls etwa linear (4,101e-03 / 8,319e-03 /
    1,707e-02); die Beschleunigung ist klein (hoechstens 5,469e-07).
  - Schon im Rauchtest (T = 12; seine Zahlen gelten laut PLAN nicht) steht v_anfang bei 4,125e-03 / 8,326e-03 / 1,694e-02.
  - Beim Surfen, dessen Paket bei x = -60 startet, skaliert v_ende dagegen mit A^2 (3,962 und 4,236).
  - Frage an die Leitung, keine Deutung: Stammt der zu a proportionale Anteil aus dem Startzustand, in dem die Welle bei
    t = 0 schon auf dem Ball liegt (PLAN 6: "Die Welle ist gleich zu Beginn ueberall da")?
- **B2 Brandung:** 0 von 12 "aufgenommen" (vorhergesagt: ueberwiegend aufgenommen), 3 von 12 "durchgereicht"
  (vorhergesagt: nie). Die Wandverschiebung ist in 4 Laeufen positiv (+0,90 bis +5,60) statt -0,5 bis -1,7.
- **B3 Chromatographie:** Trennung negativ (-2,83 und -3,66) statt +1 und +5; die Ordnung 0,6 > 0,7 > 0,8 tritt in keinem
  Seed auf; die Verzoegerung bei eps = 0,02 liegt bei 10,5 bis 12,8 % statt 1,9 bis 3,7 %.
- **B4 Katalyse:** nur_AC verschmilzt bei keinem v; "Dieselbe Verschmelzung zeigt aber schon nur_AC" trifft nicht zu.
  Kein Klumpen erreicht etwa 2 Q0 (hoechstens 1,53).
- **B5 Nervenfaser:** umgekehrt zur Vorhersage: atem wird bei allen d weitergeleitet, stoss bei d = 40 nicht.
- **B6 Wundheilung:** Die Heilzeit der Schiefe sinkt mit dem Schaden (28 / 23 / 22 und 50 / 29 / 21), statt zu steigen.
  Die abgestrahlte Ladung liegt bei 4,3 bis 68 % statt unter 1 % bis einige Prozent.
- **B7 Neuron:** Bei negativem eps steigt Spitze/|eps| oberhalb 0,1 bis 1,681, statt unterlinear zu werden; die
  abgestrahlte Ladung ist bei eps = +1 11 %.
- **B8 Monster:** S0 = 0,1: Verhaeltnis 1,77 statt ueber 3; S_max/S0 9,849 (S_max nahe 0,98) statt Mittendichte 0,45 bis
  0,55. S0 = 0,3: S_max/S0 4,468 und 4,592 statt hoechstens 4,3.
- **B9 Russell:** gleichphasig 0,3 und 0,5 staerker (6,614e-02; 3,597e-02), gegenphasig 0,3 und 0,5 schwaecher
  (4,915e-05; 5,770e-05) als die vorhergesagten Baender.

### C. Bilanzen und Messgroessen, numerisch fragwuerdig

- **C1 Brandung, v = 0,5 / Phase 0,5.**
  - Anteile: vor 0,010, See -2,441, hinter 3,406 (Summe 0,975).
  - Laut Code (wellen.py Z. 826-828) ist der Seeanteil die Aenderung der Seeladung geteilt durch Q_Ball und der Anteil
    hinter dem See die Ladung dort geteilt durch Q_Ball. Der See hat also das 2,441-Fache einer Ballladung verloren;
    hinter ihm liegt das 3,4-Fache.
  - Der Wert -2,441 gleicht zahlenmaessig Q_Ball = 2,441 (PLAN 4). Ob das Zufall ist, klaert der Bericht nicht.
  - Gemessen wird nur die linke Wand (-0,65 in diesem Lauf). Ob der See als Ganzes wandert oder Ladung abgibt, steht
    nicht im Bericht. Aehnlich v = 0,5 / Phase 1,0: linke Wand +5,60, hinter 0,871.
- **C2 Chromatographie.**
  - Ladungsverlust im Fenster bis 52,6 % (chemie_bio.py Z. 569: 1 - Q_Ende/Q_Anfang) statt unter 1e-3.
  - 14 von 36 Durchlaufzeiten fehlen, obwohl kein Lauf als "reflektiert" gilt (Code: reflektiert heisst nur, dass der
    Ball am Ende links der Zone steht). Wo diese Baelle stehen: nicht im Bericht (chromatographie.json fuehrt x_end).
  - Die Trennung zaehlt nur Seeds mit allen drei Zeiten: Bei eps = 0,02 stuetzt sie sich auf die Seeds 2 und 3, bei
    eps = 0,03 auf keinen. Die Spannweite (11,0; 13,07) ist groesser als der Betrag des Mittels (2,83; 3,66).
  - L3 und Gegenprobe gelten formal nur fuer diese Teilmenge; die mittleren Verzoegerungen mitteln nur ueber Laeufe mit
    Durchlaufzeit.
- **C3 Brandung, Verformung vor Kontakt.**
  - S 2,4e-03 bis 1,7e-02 und Breite 7,5e-02 bis 1,3e-01, gegen die Kontrolle Ball allein (S 3,8e-04 bis 8,3e-04,
    Breite 6,3e-03 bis 1,3e-02).
  - Gemessen wird "vor dem Strand" bei x < 16 (PLAN 4.5); PLAN nennt den Seeschwanz nur fuer x < 13 kleiner als 1e-4.
  - Im Rauchtest (T = 12, gilt nicht) weicht nur die Breite ab (8,9e-03 bis 5,3e-02 gegen 2,0e-04 bis 5,2e-04), S nicht.
    Ob der Seeschwanz die Zahlen traegt, zeigt der Bericht nicht.
  - Die End-Spalten der Kontrollzeilen "Ball allein" sind nicht auswertbar: Die Anteile summieren sich zu 1, 0,037 und 0;
    v_vor ist -0,458 / -0,053 / -0,073.
- **C4 Katalyse, L3-Effekt.**
  - Der Effekt 0,9887 (chemie_bio.py Z. 377: groesstes |q1(bruecke) - q1(ohne)|) passt zur Zeile 3pi/4, v = 0,4
    (bruecke 0,99, ohne 0,00). Dort ist keiner der Laeufe verschmolzen.
  - q1(ohne) = 0,00 heisst: Im Fenster |x| < 75 liegt kein Klumpen mit S > 0,05.
  - Der Effekt misst also nicht die Verschmelzung. Tragfaehig ist die Klassengleichheit 64 von 64.
- **C5 Kette, L3-Effekt.**
  - Der Effekt 438 entsteht, weil der Code fehlende Fusionen als T = 600 zaehlt (chemie_bio.py Z. 494): Paar 1 bei
    d_in = 16 verschmilzt in zuend nicht, in kalt bei 162.
  - Das ist eine Verzoegerung, kein Zeitgewinn einer Front; PLAN 4.2 nennt L3 ohne Front "gegenstandslos".
  - Dasselbe Ausbleiben zeigt Paar 2 bei d_in = 20 (kalt 493).
- **C6 Neuron, Sprung und Vorzeichen.**
  - Der gemeldete Sprung ist der Wechsel der Klumpenzahl von 1 nach 0 (Schwelle S > 0,01) bei amplitude -0,3 nach -0,5;
    Spitze/|eps| aendert sich dabei nur von 2,922 auf 1,938. PLAN Abschnitt 5: "zuerst die Klumpenschwelle variieren".
  - Bei dehnung mit negativem eps ist "Q abgestrahlt" negativ (bis -2,44e-03), die Fensterladung am Ende also groesser
    als am Anfang. Der Bericht erklaert das nicht.
- **C7 Schwellen knapp getroffen.**
  - Katalyse: Beide "x" liegen mit 1,52 und 1,53 Q0 knapp ueber 1,5; die Nachbarn 1,46 und 1,49 bzw. 1,45 und 1,46 knapp
    darunter.
  - Russell: gleichphasig v = 0,1 liegt mit X = 5,53 knapp ueber der Codeschwelle |X| < 5 fuer "verschmolzen"
    (wellen.py Z. 386) und heisst deshalb "getrennt"; v danach 0,0140.

### D. Kleinere Punkte

- **D1 Monster, Kontrolle S0 = 0,8, Fruehfenster:** M+4sd 1,69 (180 gegen 106) und M+5sd 4,43 (6 gegen 0,968). Nicht Teil
  des L2-Kriteriums, kleine Zahlen; im Spaetfenster 0,862 und 0,257. Wo V >= M^2 gilt (S0 = 0,3; S0 = 0,1 spaet), ist die
  Referenz Rayleigh mit gleichem Mittel, ohne angepasste Varianz (PLAN 4.2).
- **D2 Stokes, Gegenprobe:** L2 besteht, weil der Code relativ zum Effekt prueft (wellen.py Z. 622). Die absolute
  Vorhersage "unter 1e-9" verfehlen Bauch (fein -1,095e-06, grob 3,615e-05) und ohne Welle grob (2,1e-09).
- **D3 Surfen:** Der Energiegewinn ist bei A = 0,025 und 0,05 negativ (-1,98e-05; -4,48e-05), obwohl v_ende > 0; klein
  gegen die 1-%-Schranke.
- **D4 Wundheilung:** Heilzeit der Form 400,0 = T bei 0,55 symmetrisch; "dauerhaft" gilt dort nur am letzten Messpunkt.
- **D5 Artbildung:** Die Gueltigkeitsgrenze bei m = 2 ist ausgefranst (0,56 und 0,58 gueltig; 0,57, 0,59 und 0,60
  ungueltig). Die ungueltigen Zeilen haben Virialrest 0,26 bis 0,39.
- **D6 Rechenort:** Beide Ketten liefen laut LAUF.log auf spur=p4000b; beide PLAN-Dateien nennen p4000a (CB-PLAN:
  "p4000b nur, wenn sie es freigibt"). Ob die Freigabe vorlag, steht nicht in den gelesenen Dateien.

## 3. Zusammenfassungstabelle

| Test | Kernergebnis (fein) | Treffer | L1 | L2 | L3 | L4 | L5 | Vorschlag |
|---|---|---|---|---|---|---|---|---|
| Russell | gleichphasig 3,6 bis 6,8 % abgestrahlt, gegenphasig hoechstens 5,8e-05 | teilweise | ja | gerissen | gerissen | weitgehend | mittelbar | parken |
| Monster | S0 = 0,1: 4-S0-Verhaeltnis 1,77, Persistenz 0,84; S0 = 0,3: 0,116 | teilweise | ja | bestanden | bestanden | weitgehend | mittelbar | verwerfen |
| Stokes | dX ~ a (2,03; 2,06 statt 4), dX(0,04) = 6,0 | verfehlt | ja | bestanden | bestanden | teilweise | keiner | weiter (klaeren) |
| Surfen | kein Mitnehmen; v_ende ~ A^2 (3,96; 4,24) | teilweise | ja | bestanden | bestanden | vermutlich | keiner | parken |
| Brandung | 0 von 12 aufgenommen, 3 von 12 durchgereicht | verfehlt | ja | bestanden | bestanden | teilweise | mittelbar | weiter (klaeren) |
| Katalyse | bruecke verschmilzt an je einem v (1,52 / 1,53 Q0), nur_AC nie | teilweise | teils | bestanden | bestanden | teilweise | keiner | weiter (klaeren) |
| Kette | Reichweite 0 bei d_in = 16, 20, 24 | getroffen | teils | bestanden | bestanden | wahrscheinlich | keiner | verwerfen |
| Chromatographie | Trennung -2,8 / -3,7; 14 von 36 ohne Zeit; Verlust bis 52,6 % | verfehlt | ja | bestanden | bestanden | teilweise | mittelbar | parken |
| Neuron | dehnung glatt; ein Klumpenzahl-Sprung bei amplitude -0,5 | teilweise | ja | bestanden | bestanden | wahrscheinlich | keiner | parken |
| Wunde | Schiefe heilt in 21 bis 50; 4,3 bis 68 % Ladung abgestrahlt | teilweise | ja | bestanden | bestanden | wahrscheinlich | keiner | parken |
| Nervenfaser | atem ueberall weitergeleitet, stoss bei d = 40 nicht; Amplituden ueber 1 | verfehlt | ja | gerissen | gerissen | teilweise | mittelbar | parken |
| Artbildung | 3D Q_min 111,9 bei 0,93; 2D monoton; keine Artgrenze | getroffen | teils | bestanden | bestanden | weitgehend | keiner | verwerfen |

## 4. Einfach gesagt

Wir haben zwoelf kleine Computerversuche mit unseren Feldklumpen, den Q-Baellen, ausgewertet und jedes Ergebnis mit der
Vorhersage verglichen, die vor dem Rechnen aufgeschrieben wurde. Zwei Versuche kamen wie erwartet heraus, sechs teilweise
und vier klar anders; zum Beispiel schiebt eine Welle den Ball nicht mit dem Quadrat ihrer Hoehe, sondern etwa im gleichen
Verhaeltnis wie die Hoehe. Bei einigen Versuchen ist die Messung selbst verdaechtig: In der Ballkette zeigt der Rechner
Geschwindigkeiten ueber der Lichtgeschwindigkeit, und auf der rauen Strecke verlieren manche Baelle bis zur Haelfte ihrer
Ladung, sodass die gemessenen Zeiten wenig aussagen. Diese Stellen muessen zuerst geprueft werden, bevor jemand daraus
etwas ueber Physik schliesst; welche Karten weiterlaufen, entscheidet die Leitung.
