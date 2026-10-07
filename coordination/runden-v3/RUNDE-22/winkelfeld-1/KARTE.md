# WINKELFELD-1: Ist Winkelspannung eine Feldgroesse mit Fernwirkung? 2D-Netz, beulendes Blatt, 3D-Tetraedernetz (Runde 22)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 20:30:13 CEST (date), vor jeder Rechnung. Gerechnet von der Leitung (Finn 20:28: "mach weiter, rechne beide tests parallel").
- Herkunft:
  - Finns Fragen 20:22 ("koennen gekoppelte tetraeder in 3d koppeln ueber winkelspannung als feldgroesse?", "wie spannt
    sich der stoff")
  - TETRA-KLUMPEN, TETRA-KOPPLUNG (R17)
  - Erwartung G1 der Literaturkarte GEOMETRIE-STAND (laeuft parallel)
- Ableitbarkeitspruefung: In R16/R17 wurden Klumpen mit Eigendehnung (Q-A, Q-B) und LJ-Frustration gerechnet, aber keine
  reinen Winkelquellen (Fehlwinkel an einer Ecke bzw. Kante) und kein beulendes Blatt. Die Ausgaenge sind aus vorhandenen
  Dateien nicht ablesbar.
- Explorativ (v3), Hypothesen [H]. Laeufe je <= 10 min auf der .69 (kleintest.sh, CPU-Spuren).

## Modell

- Federnetz, alle Federn k = 1, Energie 1/2 Sum (|x_i - x_j| - L_ij)^2, freier Rand, Minimierung mit L-BFGS (Gradient per
  torch-Autograd).
- **Winkelquelle der Staerke s an einer Ecke v (2D):** Die sechs Randkanten des Sechsecks um v (jeweils v gegenueber)
  bekommen die Ruhelaenge 2 sin(theta/2) mit theta = (360 Grad - s)/6. Die Speichen bleiben 1.
  - s > 0 ist ein Fehlwinkel, wie eine Fuenfer-Ecke (s = 60: theta = 50 Grad).
  - s < 0 ist ein Ueberschuss, wie eine Siebener-Ecke.
- **Winkelquelle an einer Kante (a, b) in 3D:** Im Kuhn-Tetraedernetz des Wuerfels (6 Tetraeder je Zelle) bekommt in jedem
  Tetraeder, das (a, b) enthaelt, die gegenueberliegende Kante die Ruhelaenge (1 - eps) mal ihre Ausgangslaenge. Das
  verkleinert die Diederwinkel um (a, b); es ist ein Fehlwinkel an einer Kante, ein "Regge-Scharnier".
- **Beulendes Blatt:** dasselbe 2D-Netz mit 3D-Koordinaten und Biegeenergie kappa Sum (1 - n_1 . n_2) ueber benachbarte
  Dreiecke, kappa = 0,01, mit kleiner Anfangsauslenkung aus der Ebene.

## Arme

- **F1 (flach, eine Quelle +60):** Energie E(R) fuer Scheibenradius R = 6, 9, 12, 15, 18, 24; Exponent a aus E ~ R^a
  (Fit ueber R >= 9).
- **F2 (flach, neutrales Paar +60/-60 im Abstand 2):** E(R) fuer dieselben R.
- **F3 (flach, zwei +60 im Abstand d, R = 24):** E_int(d) = E(beide) - E(a) - E(b) + E(keine) fuer d = 2 bis 12.
- **B1 (beulend, eine Quelle +60):** E(R) wie F1.
- **D3 (3D, Kantenquelle eps = 0,05):**
  - Eigenenergie E(L) fuer Wuerfelkante L = 8, 10, 12, 14.
  - Zwei Quellen entlang einer Gitterachse: E_int(d) fuer d = 2 bis 6 bei L = 16.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| W0 | F1: E ~ R^a mit a zwischen 1,7 und 2,3 (topologische Winkelladung, Fernwirkung) | 80 % |
| W1 | F2: E(R) waechst langsamer als R^0,5 (neutrales Paar: hoechstens logarithmisch) | 75 % |
| W2 | F3: \|E_int(d)\| faellt mit d nicht ab, sondern waechst oder bleibt gleich gross (Fernwirkung gleichnamiger Winkelladungen in der flachen Ebene) | 65 % |
| W3 | B1: Exponent a < 1 fuer R >= 12; das Beulen schirmt die Winkelspannung ab ("der Stoff spannt sich zur Kruemmung") | 70 % |
| W4 | D3: E(L) aendert sich von L = 12 auf 14 um < 5 % (endliche Eigenenergie). \|E_int(d)\| faellt mit Exponent >= 2,5 (kurzreichweitig wie ein Punktdefekt) | 60 % |

**Bedeutung (vorab):**
- W0, W1 und W4 treffen ein: Eine Winkelquelle an einer Ecke ist in 2D eine echte Feldladung mit Fernwirkung. Eine
  einzelne Kantenquelle in 3D wirkt dagegen nur wie ein Punktdefekt.
  - Gekoppelte Tetraeder koppeln also ueber Winkelspannung als Feld nur dann weitreichend, wenn die Fehlwinkel zu Linien
    zusammenhaengen [H, im Modell].
- W3 trifft ein: Der Stoff loest Winkelspannung durch Kruemmung (Beulen). Das ist das 2D-Bild von "Winkeldefekt erzeugt
  Kruemmung" [H].
- W4 trifft nicht ein (Fernwirkung in 3D): Auch einzelne Kantenquellen tragen ein weitreichendes Winkelfeld.

## Rahmen

- Code der Leitung: RUNDE-22/winkelfeld-1/code/winkelfeld.py.
- Plan mit Code-Details vor dem ersten echten Lauf einfrieren (PLAN.md.eingefroren-*); ein Rauchlauf ist vorher erlaubt.

## Nachtrag vor den echten Laeufen (Leitung, 2026-10-02 20:40:58 CEST): Rauchlauf-Befund und geaenderte Quelle

- **Befund im Rauchlauf (ohne Wertung):** Die Sechseck-Randkanten-Quelle der Karte ist **netto neutral**.
  - Diskreter Gauss-Bonnet: Aendert man nur innere Ruhelaengen und laesst den Rand unveraendert, bleibt die Summe der
    Fehlwinkel im Inneren null. +60 an v wird durch -20 an jedem der sechs Nachbarn und +10 an jeder der sechs
    aeusseren Ecken genau ausgeglichen.
  - Gesehen: E(R = 6) = 0,0434, E(R = 9) = 0,0436, also fast konstant. Diese Quelle heisst jetzt Arm **N1** (nur
    berichtet, nicht blind).
- **Neue geladene Quelle fuer F1, F2, F3, B1:** Kegel-Ruhemetrik um eine Gitterecke (Code kegel_delta).
  - Die Abwicklung theta -> theta (1 - s/360) ergibt Ruhelaengen per Kosinussatz.
  - Netto-Winkelladung s am Apex; der Ausgleich sitzt im verkuerzten Randumfang. Das ist der Kegel bzw. die
    Fuenfer-Ecke im Kontinuum.
  - Gesehen im Rauchlauf: F1 E(6) = 0,447, E(9) = 1,009 (Verhaeltnis 2,26, also R^2); B1 E(6) = 0,053.
  - Selbstanzeige: W0 und W3 sind dadurch nicht mehr ganz blind; R = 6 und 9 sind bekannt. Gewertet wird wie festgelegt.
- **F2 und F3 mit s = 15 statt 60:** Die Quellen werden als Ruhelaengen-Aenderungen ueberlagert, und das ist nur im
  linearen Bereich sinnvoll. Grund vor jedem echten F2/F3-Lauf. F2: +15/-15 im Abstand 2; F3: zwei +15.
- **Auswertung:**
  - W0: Exponent aus log E gegen log R ueber R = 9 bis 24 (F1).
  - W1: Exponent ueber R = 9 bis 24 (F2) < 0,5.
  - W2: \|E_int(12)\| >= 0,5 \|E_int(2)\| (F3).
  - W3: Exponent ueber R = 12 bis 24 (B1) < 1.
  - W4:
    - E(14)/E(12) - 1 < 5 % (D3a)
    - Exponent von \|E_int\| gegen d ueber d = 3 bis 6 (D3b) >= 2,5; d = 2 nur berichtet, weil sich dort veraenderte
      Kanten ueberlappen koennen (Zaehler im Code)
- **D3 unveraendert.** Die 3D-Kantenquelle ist ebenfalls netto neutral, eine endliche Eigendehnung. Eine geladene
  3D-Disklinationslinie ist hier nicht gebaut. W4 prueft also den neutralen 3D-Fall.
