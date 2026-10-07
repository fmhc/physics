# Q-STERN-2: Stille Stelle unter schwacher Eigengravitation, volle Rechnung erster Ordnung (Runde 14)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 23:29:53 CEST (date), vor jeder
  Codezeile und jedem Lauf.
- Herkunft: RUNDE-13/q-stern (KARTE.md, ERGEBNIS.md, HERLEITUNG.md, qstern.py).
  - Dort: Cowling-Naeherung, alpha in {0,01; 0,03; 0,1} zu gross gewaehlt (Kompaktheit bis 0,59).
  - Ausgang ueberall unentschieden, weil die Lokalisierung kein Budget hatte.
  - Gemessen ohne Regelwert: alpha = 0,01 bei omega^2 ~ 0,7528, also -0,045, Kompaktheit am Ort ~0,103.
- Frage: Wohin wandert die stille Stelle l = 0, n = 1 (alpha = 0: omega^2 = 0,797677, rho = 1,744618) bei kleiner
  Kompaktheit, wenn die Schwingung auf das Newton-Potential zurueckwirkt (delta Phi)? Und wie gross ist der Unterschied zur
  Cowling-Naeherung?

## Modell (bindend; Herleitung durch den Agenten in HERLEITUNG.md, vor dem Code)

- Wirkung und Hintergrund wie Q-STERN (Newton-Grenzfall, L = (1 - 4 Phi)|d_t phi|^2 - |grad phi|^2 - (1 - 2 Phi) U),
  Phi'' + (2/r) Phi' = alpha rho_E, Phi(inf) = 0.
- **Neu:** Die Linearisierung enthaelt delta Phi = psi(r) cos(rho t), mit
  psi'' + (2/r) psi' = alpha delta rho_E(a, b), psi regulaer bei 0, psi(inf) = 0.
  - psi geht ueber die Faktoren in L in die Gleichungen fuer a und b ein. Dort steht psi immer mit dem Hintergrund f
    multipliziert und faellt deshalb mit f exponentiell ab; die Kanalasymptotik bleibt dieselbe. Der Agent prueft das
    in der Herleitung.
  - Ob delta rho_E alle Terme erster Ordnung enthaelt (Zeit- und Gradiententerme), legt die Herleitung fest.
- Zum Vergleich wird derselbe Code mit psi = 0 gerechnet (Cowling).

## Kompaktheitsziel statt freier Kopplung

- Zwei Kopplungen alpha_1, alpha_2, vor dem Einfrieren so gewaehlt, dass 2|Phi(0)| am Ort der Stelle etwa 0,01 bzw. 0,03
  ist.
  - Nach Q-STERN skaliert die Kompaktheit ungefaehr mit 10 alpha, also alpha ~ 0,001 und 0,003.
  - Der Agent misst das vorher und traegt die Werte in den Plan ein.

## Vorhersage (Leitung, vor jedem Lauf)

- Aus der in Q-STERN gemessenen Cowling-Steigung (Delta omega^2 ~ -4,5 alpha bei kleinem alpha):
  - alpha ~ 0,001: Lage ~0,7932
  - alpha ~ 0,003: Lage ~0,7842
- **V1 (Cowling):** Der Code mit psi = 0 trifft diese Lagen auf +-20 % der Verschiebung. ~75 %.
- **V2 (voll):** Mit delta Phi ist die Verschiebung ebenfalls negativ und betraegt das 0,3- bis 3-fache der
  Cowling-Verschiebung. ~65 %.
- **V3:** Stille Stelle in voller Rechnung bei beiden alpha gesehen (Umlauf -1). ~85 %.

## Kontrollen (bindend)

- K1: alpha = 0 gibt die bewiesene Stelle auf 1e-4, Umlauf -1 auf beiden Stufen.
- K2: Hintergrund auf zwei Gittern, omega, Q, E und Phi(0) auf 1e-6 relativ.
- K3: Aussenrand R und 1,5 R, Lage auf 1e-4.
- K4: Der neue Code mit psi = 0 reproduziert die Lage aus Q-STERN (qstern.py) bei alpha = 0,01 auf 1e-6 (0,75283 bzw.
  0,75281 nach Interpolation; Vergleich an denselben Zeilen).
- K5: Restpruefung der psi-Gleichung (Poisson) an der gefundenen Stelle, relativ < 1e-8.
- Verfehlt K1, K2 oder K4: nicht auswertbar.

## Regel (bindend, je alpha und je Rechnung voll/Cowling)

- **Gesehen:**
  - lokalisiertes, aufgeloestes Rechteck (groesster Phasensprung < 0,4 rad) mit Umlauf +-1 auf beiden Stufen, dazu ein
    Vorzeichenwechsel von s
  - Lage im Fenster 0,74 <= omega^2 <= 0,80, 1,65 <= rho <= 1,80
  - Stufen auf 1e-4 gleich, K3 bestanden
- **Nicht gesehen:** im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.

## Plan-Vorgabe (Lehre aus Q-STERN)

- Reihenfolge je alpha:
  1. Grobsuche des Vorzeichenwechsels auf dem Ast (Zeilen im Abstand hoechstens 0,005)
  2. **Lokalisierung mit kleinem Rechteck zuerst, mit eigenem Zeitbudget**
  3. danach Streifenpruefung im uebrigen Fenster, nur fuer "nicht gesehen" noetig
- Budget je Aufruf vorher mit einem Rauchtest messen. Kein Aufruf darf sein Budget mit dem Aufloesen schwellennaher
  Raender aufbrauchen, bevor die Lokalisierung gelaufen ist.

## Rahmen

Code-Agent. Nur .69 ueber kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4. Jeder Aufruf hoechstens 10 min. PLAN mit Herleitung
und gemessenem Budget vor dem ersten Lauf einfrieren. Zeitbox 90 min.
