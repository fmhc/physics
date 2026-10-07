# PHASE-3D: Ergebnis (Code-Agent, Runde 26, Fast Lane, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 04:35:02 CEST (date).
- Rauchlaeufe (nur Code-Test, beta = 0,6, frei gewaehlte omega^2 und rho; keine Sprosse der Karte): .69, 02:48:22 bis
  02:57:50 UTC. Drei feststeckende Rauch-Einheiten habe ich beendet (PLAN.md Abschnitt 8 sagt faelschlich zwei;
  Selbstanzeige 3).
- **Eingefroren 05:00:06 CEST:** Plan, Code, Konfigurationen, Sprossendateien und Startskripte, vor jedem echten Lauf.
  Dateien: PLAN.md.eingefroren-20261003-050006, code/*.eingefroren-20261003-050006 und
  code/lauf-eingefroren-20261003-050006/.
- **Kette** (5 x profile, 2 x phase, 2 x auswertung): .69, 03:00:11 bis 03:02:42 UTC. Alle rc = 0 ausser phase bei
  beta = 1/2 (rc = 1, Abweichung 1).
- **Nachlauf** (Abweichung 1): 03:02:54 bis 03:02:57 UTC, phase und auswertung bei beta = 1/2 mit code/phase_3d_nach.py,
  beide rc = 0. Er liefert nur die Neben- und Zusatzform bei beta = 1/2; die Urteile sind bitgleich.
- Urteile in lauf-69/auswertung-b05.json (P3D-1, P3D-2) und lauf-69/auswertung-b1.json (P3D-3); mit jq zusammengefasst
  in lauf-69/urteile.json.
- Geschrieben ab 05:05:24 CEST (date); Ende in der letzten Zeile.
- Markierungen: [A] Festlegung des Code-Agenten (im Plan vor den Laeufen), [H] Deutung/Hypothese. Alles gilt im
  linearen, radialen Zweikanalmodell (M1, l = 0): numerische Evidenz im Modell, keine Messung.

## Ergebnis zuerst

1. **Mit k_in(rho_z) sagt die ebene Wandphase die 3D-Lagen nicht voraus.** Delta_n liegt fest neben null:
   - beta = 1/2: -0,238 (n = 1) bis -0,283 (n = 15)
   - beta = 1: -0,103 bis -0,075
   - P3D-1, P3D-2 und P3D-3 sind **nicht eingetroffen**.
2. **Der Versatz strebt gegen einen festen Wert.** Der lineare Ausgleich gibt b = -0,290 (beta = 1/2, n = 8 bis 15) und
   b = -0,124 (beta = 1). Die Reste sind hoechstens 3e-4 bzw. 1,1e-3.
   - abs(Delta_n) waechst, wenn eps faellt (Spearman -1).
   - Das ist der dritte Fall der Karte.
3. **Ursache [H], vorab berechnet (PLAN.md Abschnitt 7):** Die Innenwellenzahl im 3D-Ball ist nicht k_in(rho_z).
   - Das 3D-Plateau liegt bei S_top = S_c + eps, die Sprosse bei omega_n und rho_n = rho_z + c eps.
   - k verschiebt sich um O(eps), mal R ~ 1/eps gibt das eine Phase der Ordnung 1.
   - Vorab geschaetzt (mit c bei n ~ 10 bzw. k = 1): Haupt- minus Zusatzform etwa -0,27 (beta = 1/2) und -0,12 bis
     -0,13 (beta = 1).
   - Gemessen: -0,278 bei n = 10 und -0,131 bei k = 1. Die Grenzwerte b = -0,290 und -0,124 liegen etwas daneben, weil c
     mit fallendem eps noch waechst.
4. **Mit der lokalen Innenwellenzahl passt die ebene Wandphase [H].** Die Zusatzform nimmt k(omega_n^2, rho_n, S0) und
   phi(rho_z); sie stand vorab im Plan und wird nur berichtet.
   - beta = 1/2 (n = 2, 6 bis 10): Delta = -0,0050 bis -0,0011, Achsenabschnitt +0,0016
   - beta = 1: Delta = +0,028 bis +0,049, Achsenabschnitt +0,012
5. **Numerik:**
   - R ist auf drei Wegen bestimmt: eigenes RK4 mit zwei Schritten, bic2-Profil aus RUNDE-13, DOP853. Die Wege stimmen
     auf hoechstens 3,1e-9 ueberein; Delta ist damit auf unter 1e-8 genau.
   - Die gedruckte Rundung der omega^2 wirkt hoechstens 1,5e-3 (n = 11).
   - Die ganze Zahl n' ist bei beta = 1/2 fuer alle 15 Sprossen n + 1.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 4 (lauf-69/urteile.json). K-Profil hat jede Sprosse bestanden.

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| P3D-1 | beta = 1/2: abs(Delta_n) < 0,03 fuer n = 13 bis 15 | 55 % | **nicht eingetroffen**: Delta = -0,2828 / -0,2833 / -0,2834 |
| P3D-2 | beta = 1/2: linearer Ausgleich ueber n = 8 bis 15 mit abs(b) < 0,02, und abs(Delta_n) faellt mit eps | 50 % | **nicht eingetroffen**: b = -0,2904 (a = +0,240, Rest <= 2,8e-4); abs(Delta_n) steigt mit fallendem eps (Monotonie-Bedingung nicht erfuellt, Spearman -1) |
| P3D-3 | beta = 1: linearer Ausgleich ueber die acht Sprossen mit abs(b) < 0,03 | 45 % | **nicht eingetroffen**: b = -0,1241 (a = +0,716, Rest <= 1,1e-3) |

- **Auslegungen [A]**, vor den Laeufen festgelegt:
  - Ausgleich ungewichtet, eps = omega^2 - omega_min^2.
  - "faellt mit eps" streng: abs(Delta_(n+1)) < abs(Delta_n).
  - Abwicklung um die Sprosse mit kleinstem eps; sie war nirgends noetig.
- Kein Urteil haengt an einer Auslegung. Jedes abs(b) liegt mehr als viermal ueber der Grenze, und jedes abs(Delta)
  bei n = 13 bis 15 mehr als neunmal.
- Eigene Vorhersage des Code-Agenten (PLAN.md Abschnitt 7, vor den Laeufen): P3D-1 10 %, P3D-2 10 %, P3D-3 15 %,
  Versatz der Hauptform gegen die Zusatzform etwa -0,27 bzw. -0,12 bis -0,13. Zusatzform mit abs(b) < 0,05 in beiden
  beta: 50 %; das ist eingetreten (+0,002 und +0,012; nur Bericht).

**Bedeutung (nach Karte):** Dritter Fall:
- "abs(Delta_n) strebt gegen einen festen anderen Wert: Es gibt einen Konventions- oder Kruemmungsversatz. Beschreiben,
  nicht nachtraeglich einrechnen."
- Beschreibung [H]:
  - Ein Konventionsversatz ist es nach meiner Lesart nicht. Halbhoehe S_c/2 und die Phase phi sind dieselben wie in 1D,
    wo die Formel auf 0,005 % traf.
  - Ein Kruemmungsversatz im engeren Sinn ist es auch nicht. Kruemmungskorrekturen der Wandphase sind O(1/R) und
    verschwinden fuer eps -> 0.
  - Der Versatz kommt aus der Innenwellenzahl. Im 3D-Ball sitzt das Innere bei S_top = S_c + eps, und die Sprosse liegt
    bei omega_n und rho_n.
  - Die Abweichung k_lok - k_in(rho_z) ist O(eps). Ueber den Radius R ~ 1/(2 sqrt(beta) eps) summiert sie sich zu einer
    festen Phase: 0,29 pi bei beta = 1/2 und 0,12 pi bei beta = 1.
  - Wird k_lok genommen (Zusatzform), verschwindet der Versatz bei beta = 1/2 bis auf 0,005. Bei beta = 1 bleibt ein
    Rest +0,012 bis +0,05 mit Steigung 0,53.
- Nicht eingerechnet: Die Urteile bleiben "nicht eingetroffen". Die Zusatzform war vorab als Bericht festgelegt; sie
  ersetzt die Formel der Karte nicht.
- Folge fuer das Papier [H]: theta_inf = 1/2 - phi/pi (0,6871 bzw. 0,7804) ist mit k_in(rho_z) nicht die Phase der
  3D-Leiter. Ob theta und c im Grenzfall eichfrei werden, haengt an c_inf = lim (rho_n - rho_z)/eps und an
  R - R_tw (Kontrollen). Beide liefert die ebene Rechnung allein nicht.

## Sprossentabellen

- Spalten:
  - Delta: Hauptform, k_in(rho_z) und phi(rho_z)
  - Neben: k_in und phi der ebenen Wand bei rho_n (omega_min)
  - Zusatz: k(omega_n^2, rho_n, S0) und phi(rho_z)
- R ist die Hauptrechnung (rk4:0.005). R_tw = 1/(2 sqrt(beta) eps). n' = ceil(x - 1/2).
- dDelta/d(omega^2) = k_in dR/d(omega^2)/pi (zentrale Differenz +-1e-6).

**beta = 1/2** (lauf-69/auswertung-b05.json; Neben und Zusatz aus auswertung-b05-nach.json, Abweichung 1):

| n | omega^2 | eps | R | R - R_tw | n' | Delta | Neben | Zusatz | dDelta/d(omega^2) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,797676787 | 0,297677 | 2,366333 | -0,0091 | 2 | -0,23837 | nicht definiert (*) | +0,06746 | -6 |
| 2 | 0,685128904 | 0,185129 | 3,973378 | +0,1538 | 3 | -0,25452 | +0,25140 | -0,00111 | -13 |
| 3 | 0,631450 | 0,131450 | 5,593029 | +0,2137 | 4 | -0,26295 | - | - | -26 |
| 4 | 0,601421 | 0,101421 | 7,217759 | +0,2458 | 5 | -0,26826 | - | - | -43 |
| 5 | 0,582417 | 0,082417 | 8,845427 | +0,2658 | 6 | -0,27178 | - | - | -64 |
| 6 | 0,569360 | 0,069360 | 10,474282 | +0,2795 | 7 | -0,27458 | +0,09122 | -0,00499 | -91 |
| 7 | 0,559848241 | 0,059848 | 12,104566 | +0,2896 | 8 | -0,27650 | +0,08114 | -0,00412 | -122 |
| 8 | 0,552619111 | 0,052619 | 13,735413 | +0,2972 | 9 | -0,27807 | +0,07354 | -0,00355 | -157 |
| 9 | 0,546939897 | 0,046940 | 15,367297 | +0,3032 | 10 | -0,27901 | +0,06798 | -0,00280 | -197 |
| 10 | 0,542364420 | 0,042364 | 16,999110 | +0,3081 | 11 | -0,27999 | +0,06333 | -0,00242 | -242 |
| 11 | 0,53860 | 0,038600 | 18,630883 | +0,3121 | 12 | -0,28100 | - | - | -291 |
| 12 | 0,535449 | 0,035449 | 20,262564 | +0,3154 | 13 | -0,28206 | - | - | -345 |
| 13 | 0,532772 | 0,032772 | 21,894811 | +0,3183 | 14 | -0,28278 | - | - | -404 |
| 14 | 0,530470 | 0,030470 | 23,527369 | +0,3207 | 15 | -0,28331 | - | - | -467 |
| 15 | 0,528469 | 0,028469 | 25,160632 | +0,3229 | 16 | -0,28340 | - | - | -535 |

- (*) rho_1 = 1,7446 > 1 + omega_min = 1,7071. Die ebene Wand bei omega_min ist dort aussen in beiden Kanaelen offen.
- "-": rho_n nicht bekannt (Karte: "wo rho_n bekannt ist").
- Lokale Wellenzahl bei n = 10: k_lok = 1,974623 gegen k_in(rho_z) = 1,923325, Differenz 0,0513. Der
  Schreibtischwert im Plan war ebenfalls 0,0513.

**beta = 1** (lauf-69/auswertung-b1.json; id = k aus RUNDE-24, eps aufsteigend):

| k | omega^2 | eps | R | R - R_tw | n' | Delta | Neben | Zusatz | dDelta/d(omega^2) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,780879289 | 0,030879 | 16,598747 | +0,4067 | 13 | -0,10289 | +0,13604 | +0,02814 | -403 |
| 2 | 0,783570852 | 0,033571 | 15,292516 | +0,3986 | 12 | -0,10054 | +0,14340 | +0,02982 | -341 |
| 3 | 0,786770768 | 0,036771 | 13,986872 | +0,3891 | 11 | -0,09774 | +0,15221 | +0,03182 | -285 |
| 4 | 0,790636736 | 0,040637 | 12,681743 | +0,3776 | 10 | -0,09455 | +0,16274 | +0,03407 | -234 |
| 5 | 0,795397215 | 0,045397 | 11,377316 | +0,3634 | 9 | -0,09082 | +0,17564 | +0,03667 | -188 |
| 6 | 0,801396906 | 0,051397 | 10,073720 | +0,3455 | 8 | -0,08646 | +0,19180 | +0,03974 | -147 |
| 7 | 0,809178539 | 0,059179 | 8,771142 | +0,3221 | 7 | -0,08132 | +0,21266 | +0,04360 | -111 |
| 8 | 0,819644217 | 0,069644 | 7,469635 | +0,2903 | 6 | -0,07537 | +0,24063 | +0,04898 | -81 |

- n' = 13 bis 6. Mit der Zaehlung [H] aus RUNDE-24 (n = 12 bis 5) ist das wieder n' = n + 1, wie bei beta = 1/2 [H].

**Ausgleiche (Bericht, ohne Regel; a = Steigung, b = Achsenabschnitt):**

| Menge | Form | a | b | Rest max |
|---|---|---|---|---|
| beta = 1/2, n = 6 bis 10 | Haupt | +0,200 | -0,2885 | 1,2e-4 |
| beta = 1/2, n = 11 bis 15 | Haupt | +0,244 | -0,2906 | 2,5e-4 |
| beta = 1/2, n = 6 bis 15 | Haupt | +0,223 | -0,2898 | 3,7e-4 |
| beta = 1/2, n = 6 bis 10 | Neben | +1,033 | +0,0195 | 2,4e-4 |
| beta = 1/2, n = 6 bis 10 | Zusatz | -0,096 | +0,0016 | 1,3e-4 |
| beta = 1, k = 1 bis 4 | Haupt | +0,856 | -0,1293 | 7,1e-5 |
| beta = 1, k = 1 bis 8 | Neben | +2,698 | +0,0530 | 2,3e-4 |
| beta = 1, k = 1 bis 8 | Zusatz | +0,534 | +0,0121 | 4,3e-4 |

- Die Nebenform hat bei beta = 1/2 abs(b) = 0,0195, knapp unter 0,02. Sie ist nur berichtet; ihre Phase phi(rho_n)
  streut je nach Tiefe um 4e-4 bis 2e-3 rad (beta = 1/2) bzw. 6e-3 bis 1,2e-2 rad (beta = 1), siehe Kontrollen.
- Die Ausgleiche sind nachtraeglich gelesen; der Achsenabschnitt ist keine Messung des Grenzwerts.

## Kontrollen

- **K-Profil** (Regel, je Sprosse): bestanden bei allen 23 Sprossen.
  - Aufloesung der Bisektion <= 1,5e-12
  - abs(R(rk4:0.01) - R(rk4:0.005)) <= 3,1e-9 (beta = 1/2) bzw. 1,4e-10 (beta = 1); Grenze 1e-5
  - abs(R(bic2:0.01) - R(rk4:0.005)) <= 3,1e-9; Grenze 1e-5
- **Berichtet:**
  - DOP853 rtol 1e-12 gegen die Hauptrechnung: <= 2,0e-10 (beta = 1/2, n = 3 bis 15) bzw. 6,7e-12 (beta = 1); rtol
    1e-10 <= 2,1e-9.
  - DOP853 fehlt bei n = 1 und 2 (Abweichung 2).
  - bic2:0.01 gegen rk4:0.01 <= 6,5e-13. Beide sind RK4 mit h = 0,01 in u = t - f; das prueft den Code, nicht die
    Diskretisierung.
- **Phase:**
  - Die Hauptform nimmt k_in und phi unveraendert aus PHASE-WAND (sha256 der Kopien geprueft in start.sh).
  - Die Nachrechnung bei rho_z gibt d_phi = 0 und d_k = 0 (gleicher Code, gleiche Tiefe), bei beta = 1/2 (Nachlauf) und
    bei beta = 1. Die Streuung ueber d >= 16 sqrt(beta) ist 8,9e-8 bzw. 5,6e-8.
  - phi(rho_n) (Nebenform) streut ueber die Tiefen 16, 20, 24 sqrt(beta):
    - beta = 1/2: 3,6e-4 bis 1,9e-3 rad (n = 2, 6 bis 10)
    - beta = 1: 5,7e-3 bis 1,2e-2 rad
    - Grund [H]: Die wachsende e2-Mode speist e1 ueber den Wandschwanz.
    - Im Delta sind das hoechstens 6e-4 bzw. 4e-3.
  - k_lok(omega_min, rho_z, S_c) - k_in(rho_z) <= 2,2e-16.
- **3D-Plateau:**
  - S0 - S_c - eps = -1,1e-3 (n = 15) bis -0,25 (n = 1) bei beta = 1/2, und -2,4e-3 bis -1,2e-2 bei beta = 1. Das ist
    O(eps^2); die Entwicklung von S_top gibt -3 beta eps^2 (nachtraeglich gerechnet, nicht im Plan).
  - Das Plateau liegt also bei S_c + eps, wie im Plan angenommen.
- **R - R_tw:**
  - beta = 1/2: steigt von +0,280 (n = 6) auf +0,323 (n = 15)
  - beta = 1: von +0,290 (k = 8) auf +0,407 (k = 1)
  - Nicht konvergiert erkennbar; ein Grenzwert ist nicht bestimmt.
- **Lagefehler der Eingaben:** dDelta/d(omega^2) betraegt hoechstens 535 (n = 15).
  - Gedruckte Rundung: 5e-7 bei 6 Stellen gibt <= 2,7e-4; n = 11 (5 Stellen, 5e-6) gibt 1,5e-3.
  - R13-Interpolation (wenige 1e-6) gibt etwa 7e-4 bei 3e-6; R24 (<= 3,7e-7) gibt <= 1,5e-4.
  - Selbst ein Lagefehler von 2e-5 gaebe nur 0,011, gegen einen Versatz von 0,29.
- **Unveraendert seit dem Einfrieren (sha256, lokal = .69, am Ende geprueft):**
  - PLAN.md = PLAN.md.eingefroren-20261003-050006: 2223f0d6c6b3803f844553fc6c62a9d557baad3fc0a39aa002baa07668350831
  - phase_3d.py fcd7a98a..., kette.sh 8f98074e..., start.sh 6dcf5422..., alle Konfigurationen und Sprossendateien wie in
    PLAN.md Abschnitt 10
  - phase_wand.py (c9add782...) und bic2_3d_praez.py (ba86ae6a...) unveraendert
- **Ausgaben:**
  - urteile.json b615a29c2fb545a09ea3dd1214ba98d04c70c44ca82cf50efa315b93ce4e03f4
  - auswertung-b05.json c61faed3a6619d34a1fa3f4c3c9c9ea538f09a204014d5d0fd6ae7dd60fddc7c
  - auswertung-b1.json f85e0038e62e61621829817cb642a076c016eb297fd6c9ca479744f85bb3095a
  - auswertung-b05-nach.json 1f4936eb0cead4dbed6a9a2bea7cdc2f497847f7f64085c2ad15dbcb0c7c6edb
  - phase_3d_nach.py 5019eda0da7ae3d3ed768a7944681df82d0dee09e05254efff32cd83cf4f720d
- **Laufzeiten** (.69, Unit-Laufzeit): profile 100 bis 150 s je Spur (bic2 14 bis 27 s je Profil, RK4 0,1 bis 0,7 s,
  DOP853 0,8 bis 2,3 s); phase 1 s bzw. 4 s; auswertung je < 1 s. Keine Wartezeit auf Spur-Sperren.

## Latten (v3)

- **L1 (kann scheitern): ja.**
  - Drei Vorhersagen mit Zahlengrenzen standen in der Karte vor jeder Rechnung. Die Regeln waren vor dem ersten echten
    Lauf eingefroren.
  - Alle drei sind gescheitert, also konnten sie scheitern.
  - Die Rauchlaeufe liefen bei beta = 0,6 ohne Sprossen; sie verrieten keine Lage.
  - Meine eigene Gegenvorhersage (Versatz etwa -0,27 bzw. -0,12 bis -0,13) stand vorher im Plan. Sie haette mit
    einem Hauptform-Ausgang nahe 0 ebenso scheitern koennen.
- **L2 (Gegenprobe): ja, mit Grenzen.**
  - R auf drei Wegen: RK4 mit zwei Schritten, bic2 aus RUNDE-13 und DOP853 (ausser n = 1, 2).
  - Phase und k_in aus PHASE-WAND, dort mit zwei Integratoren geprueft.
  - Die Zusatzform ist eine Rechnung, keine zweite Methode.
  - Es fehlen ein anderes Haus und eine direkte Rechnung der 3D-Wandphase.
- **L3 (Numerik): ja.** Delta ist numerisch auf < 1e-8 bestimmt. Die Eingabelagen begrenzen es auf <= 1,5e-3. Beides
  liegt um Groessenordnungen unter dem Versatz 0,29 und unter den Grenzen 0,02 bis 0,03.
- **L4 (schon bekannt): teilweise.**
  - Phasenanschluss mit Wandphase und lokaler Wellenzahl (WKB, Bohr-Sommerfeld) ist Lehrbuchstoff.
  - Dass das Innere eines duennwandigen 3D-Q-Balls bei S_top statt S_c liegt, ist Standard der Q-Ball-Literatur.
  - Neu im Projekt: Die Groesse des Versatzes ist hier gemessen, und ebene Phase plus lokale Wellenzahl treffen die
    3D-Lagen bei beta = 1/2 auf 0,005 [H].
  - Literatur nicht gesucht.
- **L5 (Messbezug): nein.** Modellinterne Aussage: linear, radial, l = 0, M1.

## Selbstanzeigen

1. **Abweichung 1 (Nachlauf):**
   - Der eingefrorene phase-Lauf bei beta = 1/2 brach bei rho_1 = 1,7446 ab (rc = 1): aussen beide Kanaele offen. Ich
     hatte nicht geprueft, ob alle rho_n im ebenen Fenster liegen.
   - Die eingefrorene Auswertung lief mit der Teildatei (nur rho_z). Neben- und Zusatzform fehlten dort bei beta = 1/2;
     die Hauptform und die Urteile waren nicht betroffen.
   - Nachlauf um 03:02:54 UTC, mit offener Begruendung: phase_3d_nach.py, eine neue Datei mit zwei markierten
     Aenderungen. phase vermerkt rho ausserhalb des Fensters; auswertung rechnet die Zusatzform ueberall, wo rho_n
     bekannt ist.
   - Urteile (jq-Gleichheit), Delta, R und K-Profil aller Zeilen sind gleich.
   - Bei beta = 1 rechnet die eingefrorene Fassung alle acht Sprossen in beiden Formen.
2. **Abweichung 2:**
   - DOP853 lieferte bei n = 1 und 2 kein R ("Halbhoehe auf einer Klammerbahn nicht erreicht").
   - Ursache: Dort ist u0 > 1e-3, der Umschaltpunkt wird nie erreicht, und der erste Abschnitt meldet R nicht.
   - Das ist ein Fehler in einer Berichtsprobe; keine Regel haengt daran. n = 1 und 2 sind durch RK4 (zwei Schritte) und
     bic2 geprueft.
3. **Rauchlaeufe und Codeaenderungen vor dem Einfrieren** (PLAN.md Abschnitt 8):
   - DOP853-Toleranz in zwei Abschnitten, enge Startklammer, einstellbare Phasentiefe, Protokoll je Bahn
   - Drei feststeckende Rauch-Einheiten (r26p3-rauch-prof, -rauch2-prof, -rauch3-prof) habe ich per systemctl --user
     stop mit vollem Einheitennamen beendet. Der eingefrorene Plan nennt zwei; das ist ein Zaehlfehler dort, nicht
     berichtigt.
4. **Zusatzform** ist meine Ergaenzung, nicht in der Karte.
   - Sie stand vor den Laeufen im eingefrorenen Plan, nur als Bericht.
   - Sie hat kein Urteil veraendert. In "Ergebnis zuerst" steht sie trotzdem als vierter Punkt, weil sie den Versatz
     erklaert [H].
5. **Vorwissen:**
   - Die rho_n (RUNDE-13, RUNDE-24) kannte ich vor dem Plan; die Schreibtischschaetzung nutzt sie.
   - R_halb und S0 aus RUNDE-13 habe ich vor den Laeufen nicht gelesen.
6. **Python auf der .69 ausserhalb der Spur:** Einmal `python --version` per ssh (02:45 UTC), kein Lauf.
7. **Lokal:**
   - kein Interpreter
   - bash, ssh, scp, rsync, jq, sha256sum, date, cp, mkdir, chmod, ls, grep, cat, cut, tail, head, cmp, paste
   - sed in einem Befehl (vier Aufrufe), um rauch5.sh und k-auswertung5-b06.json aus den Rauch-3-Dateien abzuleiten,
     und einmal fuer den Zeitstempel der letzten Zeile dieser Datei
   - eine Warteschleife (until ssh ...; sleep)
   - Hilfsdateien nur im Scratchpad (Hash-Liste, zwei jq-Auszuege)
8. **Sonst:**
   - kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Dienste, Timer oder Hooks
   - nur die Spuren cpu, cpu2, cpu3, cpu4 und cpu6; jeder Aufruf unter 3 min
   - auf der .69 nichts in place ueberschrieben (phase_3d.py vor dem Einfrieren per .neu und mv)
   - Zielwerte und Lagen nur in Dateien
   - Dateien nur in RUNDE-26/phase-3d/ und runde26-phase-3d/

## Einfach gesagt

Ein Q-Ball ist wie ein Tropfen, in dem eine Welle zwischen Mitte und Rand hin und her laeuft; bei bestimmten Groessen
strahlt sie gar nichts ab. In der flachen, eindimensionalen Version konnten wir diese Groessen allein daraus vorhersagen,
wie eine einzelne Wand die Welle zurueckwirft. Im dreidimensionalen Ball klappt das mit der Wellenlaenge der flachen
Wand nicht: Die Vorhersage liegt immer um gut ein Viertel einer halben Wellenlaenge daneben (in der zweiten
Modellvariante um etwa ein Achtel), und der Fehler wird bei groesseren Baellen nicht kleiner. Der Grund ist, dass sich die Wellenlaenge im Inneren eines 3D-Balls ein klein wenig
aendert, und dieser kleine Unterschied summiert sich ueber den grossen Radius zu einem festen Versatz. Nimmt man die
Wellenlaenge des echten Inneren, trifft die Wandregel auf wenige Tausendstel; das war aber eine Zusatzrechnung, die nur
berichtet und nicht gewertet wird, und alles gilt nur im Rechenmodell.

---
Letzte Aenderung dieser Datei: 2026-10-03 05:09:34 CEST (date). Zeitbox 90 min ab 04:35:02 eingehalten.
