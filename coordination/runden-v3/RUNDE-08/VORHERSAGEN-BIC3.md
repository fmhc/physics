# Vorhersagen fuer Karte BIC-3 (Runde 8): weitere Nullstellen der Atmungsbreite nach der Phasenregel

- **Beginn: 2026-09-30 05:59:42 CEST (date).** Schreibbeginn dieser Datei: 06:08:28 CEST (date). Ende: letzte Zeile.
- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung. Reine Handrechnung; kein python, kein python3, kein awk.
- **Blindheit (per ls geprueft, 05:59:53):**
  - Unter RUNDE-07/bic2/lauf-*/ und auf der .69 (/home/fmh/fmhc-physics-remote/runde7-bic2/) liegen zu beta = 0,55 und 0,60
    nur die Ordner der bekannten Stellen: b055-0673, -0726, -0830/-0831 und b060-0710, -0759, -0856, dazu kurve-055
    (ab 0,6655) und kurve-060 (ab 0,7033).
  - Unter 0,665 (beta = 0,55) bzw. 0,703 (beta = 0,60) ist nichts gerechnet, und zu beta = 0,35 gibt es nichts.
  - Keine Ergebnisdatei geoeffnet ausser RUNDE-07.md, Abschnitt BIC-2 (zur Eichung freigegeben).
- Eichdaten: alle Stellen aus RUNDE-07.md, BIC-2 (Stand 05:37:56), dazu meine Datei
  RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md. Re rho der n = 1-Stellen bei beta = 0,55 und 0,60 ist dort nicht verfeinert;
  ich setze 1,77269 bzw. 1,79579 aus den groben Werten (Steigung ~0,37, abgel.).

## 1. Verfahren (Hand)

**Phasengroesse.**
- Statt Phi = q R_tw nehme ich Psi = k_c R_tw. Dabei ist R_tw = 1/(2 sqrt(beta) epsilon), epsilon = omega^2 - omega_min^2.
- k_c ist die Wellenzahl der ausbreitungsfaehigen Mode im homogenen gekoppelten Inneren bei der Duennwanddichte
  S_c = 1/(2 beta):
  - k_c^2 = omega^2 + rho^2 - dp_c + sqrt(4 omega^2 rho^2 + sp_c^2)
  - dp_c = 1 + 1/(4 beta), sp_c = 1/(2 beta)
- Grund: Bei beta = 0,5 laufen die Schritte von Phi/pi auf etwa 1,03 zu, also nicht auf 1. Der Grenzwert passt zu
  q/k_c = 1,035 (Hand, bei n = 5). Mit Psi naehern sich die Schritte 1 von unten.

**Psi/pi an den bekannten Stellen (Hand, rho* aus RUNDE-07.md):**

| beta | n = 1 | n = 2 | n = 3 | n = 4 | n = 5 |
|---|---|---|---|---|---|
| 0,40 | 1,7139 | 2,6764 | 3,6673 | - | - |
| 0,45 | 1,7537 | 2,7008 | 3,6862 | - | - |
| 0,50 | 1,7916 | 2,7224 | 3,7014 | 4,6911 | 5,6852 |
| 0,55 | 1,8279 | 2,7425 | 3,7141 | ? | ? |
| 0,60 | 1,8632 | 2,7618 | 3,7264 | ? | ? |

- **Schritte:**
  - 1 -> 2: 0,9625 / 0,9471 / 0,9308 / 0,9146 / 0,8986, linear in beta (-0,016 je 0,05)
  - 2 -> 3: 0,9909 / 0,9854 / 0,9790 / 0,9716 / 0,9646 (-0,007 je 0,05)
  - beta = 0,5 weiter: 3 -> 4 0,9897, 4 -> 5 0,9941
  - Die Luecke zu 1 schrumpft mit n (0,069 / 0,021 / 0,010 / 0,006 bei beta = 0,5).
- **Probe des Verfahrens an bekannten Stellen:**
  - Die fuenfte Stelle bei beta = 0,5 aus den ersten vier: Schritt 0,9938 erwartet, 0,9941 gefunden.
  - Psi_3/pi bei beta = 0,55 aus beta = 0,40 bis 0,50: 3,7139 erwartet, 3,7141 gefunden.
  - c_3 = Re rho - omega bei beta = 0,60 aus beta = 0,40 bis 0,55: 0,8817 erwartet, 0,8818 gefunden.
- **c = Re rho* - omega* an den Stellen** (Eichung; braucht man fuer rho):

| beta | n = 1 | n = 2 | n = 3 | n = 4 | n = 5 |
|---|---|---|---|---|---|
| 0,40 | 0,8265 | 0,8312 | 0,8231 | - | - |
| 0,45 | 0,8400 | 0,8486 | 0,8423 | - | - |
| 0,50 | 0,8515 | 0,8626 | 0,8580 | 0,8526 | 0,8481 |
| 0,55 | 0,8617 | 0,8742 | 0,8709 | ? | ? |
| 0,60 | 0,8709 | 0,8839 | 0,8818 | ? | ? |

**Rechenweg je Ziel:**
1. Ziel-Psi_n/pi aus den Schritttabellen hochrechnen.
2. c_n hochrechnen.
3. Setze rho = omega + c_n.
4. Loese k_c(omega^2) R_tw(omega^2) = Psi_n mit Newton-Schritten von Hand; dPsi/domega^2 ~ -Psi/epsilon + R dk_c/domega^2.
5. Die Fehlerbalken setzen sich zusammen aus Psi-Hochrechnung und c-Hochrechnung (je 1 sigma quadratisch addiert); die
   Tabelle nennt etwa 2 sigma.

**Umlaufzahl (Paritaetsregel, bic2-Konvention):** n ungerade -1, n gerade +1.
- Das stimmt an allen 16 aufgeloesten Umlaeufen aus RUNDE-07.md und der Nachricht der Leitung (beta = 0,40 bis 0,60).
- Der nicht aufgeloeste Umlauf bei beta = 0,5, n = 5 hat ebenfalls das passende Vorzeichen.

## 2. Vorhersagen

| Ziel | omega*^2 | Re rho* | Umlauf | Herleitung (Kurzform) |
|---|---|---|---|---|
| (a) beta = 0,55, n = 4 | **0,64564 +- 0,0003** | **1,6702 +- 0,002** | **+1** | Schritt 3 -> 4 = 0,9859 +- 0,003 (Mittel aus zwei Hochrechnungen: Lueckenverhaeltnis gegen beta = 0,5 in epsilon gibt 0,9852; schrumpfende beta-Steigung gibt 0,9866), Psi_4/pi = 4,7000; c_4 = 0,8667 +- 0,0015 (Versatz gegen beta = 0,5 waechst +0,0014 je n); Loesung bei epsilon = 0,10019, R_tw = 6,729, k_c = 2,1942 |
| (a) beta = 0,55, n = 5 | **0,62708 +- 0,0004** | **1,6551 +- 0,003** | **-1** | Schritt 4 -> 5 = 0,9919 +- 0,003, Psi_5/pi = 5,6919; c_5 = 0,8632 +- 0,002; epsilon = 0,0816, R_tw = 8,26, k_c = 2,1648 |
| (b) beta = 0,60, n = 4 | **0,68195 +- 0,0003** | **1,7048 +- 0,002** | **+1** | Schritt 3 -> 4 = 0,9823 +- 0,003, Psi_4/pi = 4,7087; c_4 = 0,8790 +- 0,0015; epsilon = 0,0986, R_tw = 6,544, k_c = 2,2601 |
| (b) beta = 0,60, n = 5 | **0,66386 +- 0,0004** | **1,6914 +- 0,003** | **-1** | Schritt 4 -> 5 = 0,9898 +- 0,003, Psi_5/pi = 5,6985; c_5 = 0,8766 +- 0,002; epsilon = 0,0805, R_tw = 8,01, k_c = 2,2333 |
| (c) beta = 0,35, n = 1 | **0,6218 +- 0,001** | **1,5993 +- 0,002** | **-1** | Psi_1/pi = 1,6721 +- 0,004 (Zuwachs je 0,05 in beta: 0,0398 / 0,0379 / 0,0363 / 0,0353, nach unten 0,0418); c_1 = 0,8107 +- 0,002; epsilon = 0,3361, R_tw = 2,514, k_c = 2,0890. Hier ist dPsi/domega^2 nur -12, daher der breitere Balken |
| (c) beta = 0,35, n = 2 | **0,47655 +- 0,0008** | **1,5010 +- 0,003** | **+1** | Psi_2/pi = 2,6495 +- 0,004 (Mittel aus direkter beta-Hochrechnung 2,6489 und n = 1 plus Schritt 0,978 = 2,6501); c_2 = 0,8107 +- 0,003; epsilon = 0,1908, R_tw = 4,429, k_c = 1,8795 |
| (c) beta = 0,35, n = 3 | **0,41651 +- 0,0006** | **1,4452 +- 0,003** | **-1** | Psi_3/pi = 3,6449 +- 0,005 (3,6443 bzw. 3,6455); c_3 = 0,7998 +- 0,003; epsilon = 0,1308, R_tw = 6,46, k_c = 1,7720 |
| (c) beta = 0,35, n = 4 | **0,38452 +- 0,0008** | **1,4079 +- 0,005** | **+1** | Schritt 3 -> 4 = 0,998 (Luecke 0,002, weil die Luecken mit fallendem beta schrumpfen), Psi_4/pi = 4,6435 +- 0,007; c_4 = 0,7878 +- 0,005 (zweifach hochgerechnet, groesster Einzelfehler); epsilon = 0,0988, R_tw = 8,554, k_c = 1,7054 |

**(c) Gilt die Regel bei beta = 0,35? Ja, nach allen Kriterien, die ich pruefen kann (Hand):**
- **Duennwandgrenze:** Sie existiert, weil beta > 1/4; omega_min^2 = 0,2857.
- **Innenbarriere:** B = dp(S0) - c^2 > 0 an allen vier Stellen.
  - dp(S_c) = 1,714. In 3D liegt S0 ueber S_c (wie bei beta = 0,40: S0 = 1,38 gegen S_c = 1,25 bei omega^2 = 0,70).
  - c^2 = 0,62 bis 0,66, also B ~ 1,05 oder mehr.
  - Die Barrierengrenze, hochgerechnet aus 0,848 / 0,865 / 0,878 (beta = 0,40 / 0,45 / 0,50), liegt bei ~0,83. Das ist
    ueber der obersten Stelle 0,62.
- **Ein offener Kanal:** Re rho* < 1 + omega an allen vier Stellen (Abstand 1 - c = 0,19 bis 0,21), und c^2 < 1.
- **Stabilitaet:** Alle vier Stellen liegen weit unter der Q_min-Grenze (bei beta = 0,5: 0,927).
- **Geschlossener Kanal:**
  - Der Topf in der Wand ist bei beta = 0,35 tiefer: dp_min = 1 - 4/(9 beta) = -0,27 statt +0,11.
  - Er ist aber schmal (Wandbreite sqrt(beta) = 0,59). Nach meiner Abschaetzung bleibt es bei einem gebundenen
    Wandzustand, also bei einem Atmungsast.
  - Sollte kurve einen zweiten schmalen Ast zeigen, gilt die Vorhersage fuer den Ast mit c = Re rho - omega ~ 0,80.
- **Vorbehalt:** Die Regel ist nur fuer beta = 0,40 bis 0,60 geeicht. beta = 0,35 ist eine Stufe Hochrechnung nach unten.

## 3. Unterscheidungspunkte: was die Regel widerlegt

1. **Kein Vorzeichenwechsel** von s im Fenster "Vorhersage +- 3 Fehlerbalken" auf einem kurve-Raster <= 0,005, bei
   Kernwachstum < 1e8: Die Phasenregel ist fuer diesen Ast falsch.
2. **Vorzeichenwechsel vorhanden, aber ausserhalb des Fehlerbalkens:** Die Hochrechnung von Psi bzw. c ist falsch, die
   Regel qualitativ noch moeglich. Liegt die Stelle mehr als 3 Fehlerbalken daneben, ist die Regel als quantitatives
   Werkzeug widerlegt.
3. **Umlaufzahl mit falschem Vorzeichen** (aufgeloest, Rechteck enthaelt die Stelle): Die Paritaetsregel ist widerlegt.
4. **Zwei Vorzeichenwechsel dicht beieinander** (Paar statt Einzelstelle): Das Bild "eine reelle Funktion s mit
   einfachen Nullstellen" ist widerlegt.
5. **Nur fuer (c):** Zeigt kurve von 0,38 bis 0,64 keinen einzigen Vorzeichenwechsel, gilt die Regel unterhalb
   beta = 0,40 nicht. Die Innenbarriere waere dann nicht hinreichend.

## 4. Fertige Aufrufe (bic2.py, Form wie RUNDE-07/bic2/PLAN.md, Abschnitt 8)

- Laufzeiten der Runde: kurve mit 11 bis 15 Profilen 210 bis 470 s, exakt 200 bis 450 s, also je unter 10 min.
- --abstand ist so gesetzt, dass die untere Grenze omega_min^2 + abstand unter der tiefsten Zielstelle liegt:
  - beta = 0,55: 0,5455 + 0,07 = 0,6155
  - beta = 0,60: 0,5833 + 0,07 = 0,6533
  - beta = 0,35: 0,2857 + 0,09 = 0,3757
- --drho ist nur ein Keim (Steigung Re rho gegen omega^2 bei beta = 0,5: 0,40 bei n = 1, 0,85 bei n = 2, ~1 bei n >= 3).

**(a) beta = 0,55**

    kurve --geraet cpu --pot poly --beta 0.55 --xmin 0.615 --xmax 0.665 --dx 0.005 --abstand 0.07 --h 0.02 --out aus-kurve-055-tief
    exakt --geraet cpu --beta 0.55 --x0 0.64564 --rho0 1.67022 --drho 1.0 --h 0.01 --out aus-exakt-b055-0646
    exakt --geraet cpu --beta 0.55 --x0 0.62708 --rho0 1.65508 --drho 1.0 --h 0.01 --out aus-exakt-b055-0627

**(b) beta = 0,60**

    kurve --geraet cpu --pot poly --beta 0.60 --xmin 0.655 --xmax 0.700 --dx 0.005 --abstand 0.07 --h 0.02 --out aus-kurve-060-tief
    exakt --geraet cpu --beta 0.60 --x0 0.68195 --rho0 1.70480 --drho 1.0 --h 0.01 --out aus-exakt-b060-0682
    exakt --geraet cpu --beta 0.60 --x0 0.66386 --rho0 1.69138 --drho 1.0 --h 0.01 --out aus-exakt-b060-0664

**(c) beta = 0,35** (kurve in zwei Teilen, damit jeder Aufruf unter 10 min bleibt)

    kurve --geraet cpu --pot poly --beta 0.35 --xmin 0.38 --xmax 0.50 --dx 0.01 --abstand 0.09 --h 0.02 --out aus-kurve-035-tief
    kurve --geraet cpu --pot poly --beta 0.35 --xmin 0.58 --xmax 0.66 --dx 0.01 --abstand 0.09 --h 0.02 --out aus-kurve-035-oben
    exakt --geraet cpu --beta 0.35 --x0 0.6218 --rho0 1.5993 --drho 0.45 --h 0.01 --out aus-exakt-b035-0622
    exakt --geraet cpu --beta 0.35 --x0 0.47655 --rho0 1.5010 --drho 0.85 --h 0.01 --out aus-exakt-b035-0477
    exakt --geraet cpu --beta 0.35 --x0 0.41651 --rho0 1.4452 --drho 1.0 --h 0.01 --out aus-exakt-b035-0417
    exakt --geraet cpu --beta 0.35 --x0 0.38452 --rho0 1.4079 --drho 1.0 --h 0.01 --out aus-exakt-b035-0385

- Hinweis zu exakt: Das erste grosse Rechteck liegt um x0. Liegt die Stelle mehr als 5e-4 daneben, gibt es 0
  (Lehre aus Runde 7). Massgeblich sind die neu gelegten Rechtecke.
- Bei (c) n = 1 (Balken +-0,001) sollte man x0 erst nach kurve setzen, sonst liegt die Stelle womoeglich ausserhalb des
  ersten Rechtecks.

## 5. Einfach gesagt

Wir haben aus den bisher gefundenen Stellen, an denen der atmende Q-Ball keine Welle abstrahlt, eine Regel abgelesen: Die
Welle im Inneren muss eine bestimmte Zahl halber Schwingungen zwischen Mitte und Rand unterbringen. Mit dieser Regel
haben wir acht neue Stellen vorausgesagt, fuer drei Kraftgesetze, die noch niemand gerechnet hat, samt Fehlerbalken und
Drehsinn. Liegen die gerechneten Stellen innerhalb der Balken, ist die Regel ein echtes Werkzeug. Fehlen sie oder liegen
sie weit daneben, war sie nur eine gute Beschreibung der alten Zahlen.


**Ende: 2026-09-30 06:09:41 CEST (date, nach dem Schreiben gemessen).** Dauer 10 min, Budget 30 min.
