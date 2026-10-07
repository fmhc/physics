# B-BALL-2b: Laeuft die stille Stelle im letzten Viertel (t = 0,75 bis 1) stetig? (Runde 13)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 20:02:46 CEST (date), vor jedem Lauf
  dieser Karte.
- Herkunft: B-BALL-2 (ERGEBNIS-KARTE2.md), Ausgang "Kontinuitaet traegt" fuer t = 0,25, 0,5 und 0,75.
  - Lagen omega*^2 = 0,79768 / 0,83077 / 0,85882 / 0,87652 / 0,92561 fuer t = 0 / 0,25 / 0,5 / 0,75 / 1.
  - Der letzte Schritt ist mit 0,049 deutlich groesser als die anderen (0,018 bis 0,033). Ob die Stelle dort stetig
    laeuft, ist offen.

## Test

- Code bball2.py, unveraendert. Mischpotential U_t wie in Karte 2, t = 0,9.
- Mindestens 17 Zeilen in omega^2 von 0,8765 bis 0,9256 (Abstand hoechstens 0,003), feine rho-Abtastung bzw. direkte
  Nullstellensuche, zwei Stufen h = 0,02 und 0,01, Umlaufrechtecke wie in Karte 2.

## Vorhersage (Leitung, vor dem Lauf)

- Quadratische Interpolation durch t = 0,5 / 0,75 / 1: omega*^2(0,9) = 0,9022 +- 0,012, rho*(0,9) = 1,8252 +- 0,008.
- Gefunden (Kontinuitaet im letzten Viertel): ~85 %.
- Umlauf -1: ~90 %, falls gefunden.

## Regel (bindend)

- **Gefunden:** Aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen und ein Vorzeichenwechsel von s, mit der Lage in
  0,8765 <= omega^2 <= 0,9256 und 1,810 <= rho <= 1,838. Die Lagen beider Stufen stimmen auf 1e-4 ueberein.
  - Dann gilt "Kontinuitaet im letzten Viertel traegt".
  - Die quadratische Vorhersage wird getrennt gewertet: getroffen, wenn die Lage im Band +-0,012 bzw. +-0,008 liegt.
- **Nicht gefunden:** Im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
  Dann haengen Sextik- und Log-Stelle nicht nachweislich stetig zusammen.
- **Unentschieden:** alles andere.

## Rahmen

Code-Agent (Fortsetzung). Nur .69 ueber kleintest.sh, Spuren cpu3 und cpu4, jeder Aufruf hoechstens 10 min. Kurzer
PLAN-Abschnitt "Karte 2b" vor dem ersten Lauf einfrieren. Zeitbox 25 min.
