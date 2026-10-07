# Vorhersagen fuer Karte SP-1 (Runde 8): Nullstellen der Breite fuer l = 1 und l = 2 bei beta = 0,5

- **Beginn: 2026-09-30 06:35:35 CEST (date).** Schreibbeginn dieser Datei: 06:41:45 CEST (date). Ende: letzte Zeile.
- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung. Reine Handrechnung; kein python, kein python3, kein awk.
- **Blindheit (per ls geprueft, 06:35:39):**
  - Lokal (RUNDE-07/bic2/lauf-*/, RUNDE-08/) gibt es nur aus-pole-l1 (Aufruf V6, laut meinem Vorschlag bei 0,72 bis 0,78).
  - Auf der .69 (runde7-bic2/) liegen aus-pole-l1, aus-pole-l1-0750 und aus-pole-l1-0755.
  - Keiner dieser Ordner liegt nach Namen unter 0,72, keiner betrifft l = 2. Ich habe keinen geoeffnet.
- Eichung:
  - l = 1-Werte der Leitung (Gamma 1,70e-3 / 2,49e-4 / 2,04e-5 / 2,33e-7 bei 0,72 / 0,74 / 0,75 / 0,755)
  - l = 0-Stellen aus RUNDE-07.md, BIC-2
  - Pole aus RUNDE-06.md: l = 1 Re rho = 1,7635198 (0,70), 1,87598 (0,80), 1,9138667 (0,84), 1,6481991 (0,60);
    l = 2 Re rho = 1,6786834 (0,60); l = 0-Pole
- bic2.py exakt rechnet nur l = 0 (grep: `a.l` nur im pole-Zweig). Umlaufzahlen fuer l > 0 sind daher erst nach einer
  Code-Erweiterung messbar. Die Lagen prueft `pole --l`.

## 1. Die Regel fuer l > 0 (Hand, [H])

1. **Phase an der Wand.**
   - Psi = k_c R_tw wie in VORHERSAGEN-BIC3.md: R_tw = 0,707107/(omega^2 - 0,5).
   - k_c^2 = omega^2 + rho^2 - 1,5 + sqrt(4 omega^2 rho^2 + 1), mit rho = Re rho des l-Pols.
   - Die regulaere l-Welle traegt den Versatz der Riccati-Bessel-Funktion:
     - phi_l = Psi - l pi/2 + delta_l(Psi)
     - delta_1 = arctan(1/Psi)
     - delta_2 = arctan(3 Psi/(Psi^2 - 3))
2. **Nullstellen** liegen bei phi_l/pi = n + theta'(epsilon) + Dtheta_l.
   - theta'(epsilon) ist der l = 0-Versatz. Er passt auf alle fuenf beta = 0,5-Stellen:
     - Fit theta' = 0,675 + 1,4 epsilon^2
     - gemessen 0,7916 / 0,7224 / 0,7014 / 0,6911 / 0,6852
   - Dtheta_l ist der zusaetzliche Wandversatz der l-Welle.
3. **Eichung an der l = 1-Stelle.**
   - Aus den vier Gamma-Werten der Leitung folgt die Nullstelle bei 0,7556 (Hand: signierte Wurzel mit quadratischem Fit
     ergibt 0,7557; das Verhaeltnis der zwei innersten Punkte ergibt 0,7556).
   - Re rho_1(0,7556) = 1,826 +- 0,002 (Interpolation zwischen 0,70 und 0,80, dazu die Kruemmung aus 0,84).
   - Damit ist Psi/pi = 2,1438 und phi_1/pi = 1,6907. Gegen die l = 0-Familie (n = 1: 1,7916) folgt
     **Dtheta_1 = -0,102** an der Wand R_w = R_tw + 0,65 = 3,416.
4. **Wie Dtheta mit dem Radius faellt (Annahme).**
   - Dtheta_l(R_w) = -0,102 (l(l+1)/2) [0,5 (3,416/R_w)^2 + 0,5 (3,416/R_w)]
   - Das ist das Mittel aus 1/R^2-Skalierung (Zentrifugalterm) und 1/R-Skalierung. Der Unterschied beider geht in den
     Fehlerbalken ein.
5. **Re rho des l-Asts (Zentrifugalmodell).**
   - c_l^2 = c_0^2 + l(l+1)/R_w^2, mit c = Re rho - omega und R_w = R_tw + 0,65.
   - Das Wandstueck 0,65 ist geeicht aus l = 1 bei 0,70 (0,72) und bei 0,80 (0,54).
   - Proben bei 0,60: l = 1 gibt Modell 1,6452 gegen gemessen 1,6482; l = 2 gibt Modell 1,6830 gegen 1,6787.
   - c_0 kommt geglaettet aus den l = 0-Polen (0,851 bis 0,861). Die Wellen von Re rho um die Nullstellen herum sind
     +-0,004, deshalb der Balken +-0,005.
6. **Umlaufzahl:**
   - Entlang eines l-Asts wechselt sie ab; das legt die Regel fest.
   - Das absolute Vorzeichen setze ich wie bei l = 0 (n ungerade -1). Die Riccati-Bessel-Normierung x^(l+1) am Ursprung
     und sin(x - l pi/2) aussen haben dasselbe Vorzeichen.
   - Das gilt nur, wenn eine W-Abbildung fuer l > 0 gleich gebaut wird.

## 2. Vorhersagen

### (a) l = 1, die naechsten zwei Stellen unter 0,7556

| Ziel | omega*^2 | Re rho* | Umlauf | Herleitung |
|---|---|---|---|---|
| l = 1, n = 2 | **0,6620 +- 0,0023** | **1,7196 +- 0,005** | **+1** (Wechsel sicher; absolut unter der Konventionsannahme) | Dtheta_1 = -0,056 +- 0,015 (R_w = 5,01), theta' = 0,7224, also phi_1/pi = 2,6664 und Psi/pi = 3,1343; c_1 = 0,9060 aus c_0 = 0,861; Loesung bei epsilon = 0,162, R_tw = 4,365, k_c = 2,2563 |
| l = 1, n = 3 | **0,6178 +- 0,0013** | **1,6656 +- 0,005** | **-1** | Dtheta_1 = -0,037 +- 0,015 (R_w = 6,65), theta' = 0,7014, also phi_1/pi = 3,6644 und Psi/pi = 4,1400; c_1 = 0,8796 aus c_0 = 0,8535; epsilon = 0,1178, R_tw = 6,003, k_c = 2,1667 |

- **Probe [H]:**
  - Die l = 1-Stellen liegen jeweils zwischen zwei l = 0-Stellen: 0,7977 > **0,7556** > 0,6851 > **0,6620** > 0,6314 >
    **0,6178** > 0,6014.
  - Mit Gamma_env ~ 3,7e-3 gibt das sin^2-Modell bei 0,70 das Maximum (gemessen 3,66e-3, Runde 6). Bei 0,60 (zwischen
    n = 3 und n = 4) liegt es nahe der Einhuellenden (gemessen 4,97e-3).
  - Zur Nullstelle hin faellt die Einhuellende, weil der l = 1-Zustand nahe der Kante liegt (c_1 -> 1). Das Modell
    ueberschaetzt Gamma bei 0,72 bis 0,75 um das 1,3- bis 2,5-Fache; die Lage betrifft das nicht.

### (b) l = 2, die obersten drei Stellen

- **Fenster:**
  - Nach dem Zentrifugalmodell erreicht der l = 2-Ast die Kante Re rho = 1 + omega (c_2 = 1) bei omega^2 ~ 0,670 +- 0,01.
  - Darueber gibt es keinen l = 2-Atmungspol mit nur einem offenen Kanal. Das passt zu Runde 6: bei 0,7 kein l = 2-Pol
    im Kasten, bei 0,6 der schmale Pol 1,6787 - 2,91e-3 i.
- **Die Stelle m = 1 laege ausserhalb.** An der Fenstergrenze ist phi_2/pi schon 2,26; m = 1 braucht ~1,53. Die oberste
  Stelle im Fenster ist daher **m = 2**.
- **Zusatzversatz der l = 2-Welle:**
  - -pi (statt -pi/2) plus delta_2 = arctan(3 Psi/(Psi^2 - 3)) (0,088 pi bei Psi = 10,8)
  - dazu Dtheta_2 = 3 Dtheta_1 am selben Wandradius (Zentrifugalterm 6 statt 2)
  - Das Modell fuer rho liegt bei 0,60 um 0,0043 zu hoch; ich ziehe 0,004 von c_2 ab.

| Ziel | omega*^2 | Re rho* | Umlauf | Herleitung |
|---|---|---|---|---|
| l = 2, m = 2 | **0,6505 +- 0,005** | **1,777 +- 0,008** | **+1** | Dtheta_2 = -0,162 +- 0,07, theta'(0,152) = 0,7065, Ziel phi_2/pi = 2,544; bei 0,652 gerechnet 2,5247, Steigung -18 je Einheit omega^2. Am unsichersten: c_2 = 0,971, geschlossener Abfall kappa = 0,24, Zustand kaum noch an die Wand gebunden |
| l = 2, m = 3 | **0,6094 +- 0,003** | **1,696 +- 0,006** | **-1** | Dtheta_2 = -0,109 +- 0,05, theta' = 0,6917, Ziel 3,5830; bei 0,60937 gerechnet 3,5838 (c_2 = 0,9151, Psi = 14,189, delta_2/pi = 0,0673) |
| l = 2, m = 4 | **0,5865 +- 0,0015** | **1,655 +- 0,006** | **+1** | Dtheta_2 = -0,083 +- 0,04, theta' = 0,6856, Ziel 4,6029; bei 0,587 gerechnet 4,5778, Steigung -55, also 0,58655 (c_2 = 0,8895, Psi = 17,35) |

- Auch die l = 2-Stellen verzahnen sich mit l = 0 und l = 1. Das ist jedoch schwaecher gefordert, weil Dtheta_2 gross
  und unsicher ist.

### (c) Was die Regel fuer l > 0 widerlegt

1. **l = 1:**
   - Fehlt auf einem Raster <= 0,003 im Fenster Vorhersage +- 3 Balken ein V-foermiger Einbruch mit Gamma_min < 1e-6,
     dann ist die Uebertragung auf l = 1 widerlegt.
   - Dasselbe gilt fuer eine Stelle ausserhalb des Intervalls zwischen den benachbarten l = 0-Stellen (0,6314 bis 0,6851
     bzw. 0,6014 bis 0,6314). Das waere ein Bruch des Halbwellenversatzes -pi/2.
2. **Abstand statt Lage:** Der Abstand der l = 1-Stellen n = 2 und n = 3 in Psi/pi muss 1,006 +- 0,03 sein (Hand:
   4,1400 - 3,1343). Ein Abstand unter 0,9 oder ueber 1,1 widerlegt das Phasenbild, auch wenn die Lagen im Balken liegen.
3. **l = 2:**
   - Gibt es oberhalb von 0,68 einen schmalen l = 2-Atmungspol unter 1 + omega, ist das Zentrifugalmodell widerlegt.
   - Fehlen m = 3 und m = 4, ist die Regel fuer l = 2 widerlegt. m = 2 allein nicht: nahe der Kante darf sie versagen.
   - Liegen m = 3 und m = 4 um etwa eine halbe Stufe verschoben (z. B. 0,63 und 0,597), dann ist der Bessel-Versatz
     -l pi/2 + delta_l falsch.
4. **Re rho:** Weicht Re rho an einer gefundenen Stelle um mehr als 0,015 vom Modell ab, ist das Zentrifugalmodell fuer
   c_l widerlegt. Die Nullstellenregel betrifft das nicht.
5. **Umlauf** (erst nach einer exakt-Erweiterung fuer l > 0): Zwei benachbarte Stellen desselben l-Asts mit gleichem
   Vorzeichen widerlegen die Abwechslung.

## 3. Fertige Aufrufe (bic2.py pole, je hoechstens 10 min; fuenf Werte je Aufruf, zwei Stufen)

    pole --geraet cpu --l 1 --omega2 0.656,0.659,0.662,0.665,0.668 --h 0.02,0.01 --bereich resonanz --out aus-pole-l1-066
    pole --geraet cpu --l 1 --omega2 0.614,0.616,0.618,0.620,0.622 --h 0.02,0.01 --bereich resonanz --out aus-pole-l1-062
    pole --geraet cpu --l 2 --omega2 0.642,0.646,0.650,0.654,0.658 --h 0.02,0.01 --bereich resonanz --out aus-pole-l2-065
    pole --geraet cpu --l 2 --omega2 0.604,0.607,0.610,0.613,0.616 --h 0.02,0.01 --bereich resonanz --out aus-pole-l2-061
    pole --geraet cpu --l 2 --omega2 0.583,0.585,0.587,0.589,0.591 --h 0.02,0.01 --bereich resonanz --out aus-pole-l2-059
    pole --geraet cpu --l 2 --omega2 0.66,0.67,0.68,0.69 --h 0.02,0.01 --bereich resonanz --out aus-pole-l2-kante

- Auswertung: Gamma gegen omega^2; signierte Wurzel linear durch null gibt die Lage.
- Der letzte Aufruf prueft das Fenster: Der Pol verlaesst den Kasten zwischen 0,67 und 0,68.
- Liegen die Rasterpunkte zu grob fuer die Balken, nachfeinern. Bei l = 2, m = 2 (+-0,005) koennte das Raster die Stelle
  verfehlen; dann zuerst 0,640 bis 0,660 im Abstand 0,004.

## 4. Einfach gesagt

Der Q-Ball kann nicht nur gleichmaessig atmen, sondern auch zur Seite schwappen (l = 1) oder sich zur Zigarre verformen
(l = 2). Fuer diese Schwingungen sagt unsere Regel ebenfalls Stellen ohne Abstrahlung voraus. Sie liegen aber um eine
halbe bzw. ganze Welle verschoben, weil die auslaufende Welle einen anderen Drehimpuls traegt. Fuer l = 1 erwarten wir die
naechsten Stellen bei 0,662 und 0,618, jeweils zwischen zwei Stellen der Atmung. Fuer l = 2 gibt es wegen der Kante nur
Stellen unterhalb von etwa 0,67, und die unsicherste davon liegt ganz oben.


**Ende: 2026-09-30 06:42:48 CEST (date, nach dem Schreiben gemessen).** Dauer 7 min 13 s, Budget 30 min.
