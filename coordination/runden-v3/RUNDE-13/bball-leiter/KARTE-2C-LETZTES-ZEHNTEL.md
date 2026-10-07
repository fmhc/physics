# B-BALL-2c: Eine wandernde Nullstelle oder zwei verschiedene? Das letzte Zehntel t = 0,9 bis 1 (Runde 13)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 20:15:53 CEST (date), vor jedem Lauf
  dieser Karte.
- Herkunft: B-BALL-2b (ERGEBNIS-KARTE2.md).
  - Nach der Regel "nicht gefunden": Bei t = 0,9 liegt im Fenster 0,8765 bis 0,9256 kein Vorzeichenwechsel.
  - **Meine Fensterwahl hat Monotonie vorausgesetzt, und die gilt nicht** (Selbstanzeige der Leitung).
  - Der nachtraegliche Lauf fand die Stelle bei t = 0,9 unterhalb des Fensters: omega*^2 = 0,86787, rho* = 1,79602,
    Umlauf -1. Bis 0,9706 gibt es keine zweite.
  - Bei t = 1 liegt die Stelle bei 0,92561.
- Frage: Wandert eine einzige Nullstelle zwischen t = 0,9 und 1 rasch von 0,868 nach 0,926, oder entsteht dazwischen ein
  neues Nullstellenpaar (Falte) und die Log-Stelle ist eine andere?

## Test

- bball2.py unveraendert, t in {0,925; 0,95; 0,975}.
- Weites Fenster 0,82 <= omega^2 <= 0,97, Zeilenabstand hoechstens 0,005 (mindestens 31 Zeilen je t), zwei Stufen
  h = 0,02 und 0,01, Umlaufrechtecke wie bisher. Gezaehlt wird die Zahl der Vorzeichenwechsel von s im ganzen Fenster.

## Regel (bindend)

- **Eine wandernde Nullstelle:** Fuer jedes der drei t gibt es im weiten Fenster genau einen Vorzeichenwechsel von s, mit
  aufgeloestem Rechteck und Umlauf -1 auf beiden Stufen, und alle anderen Rechtecke haben aufgeloest Umlauf 0. Die Lagen
  steigen mit t und liegen zwischen 0,8679 und 0,9256.
- **Falte (zwei verschiedene Stellen):** Fuer mindestens ein t gibt es drei oder mehr Vorzeichenwechsel (ein Paar mit
  Umlauf +1 und -1 dazu), auf beiden Stufen aufgeloest. Oder der eine Wechsel springt nicht monoton.
- **Unentschieden:** alles andere, auch kein Wechsel bei einem t.

## Vorhersage (Leitung, vor dem Lauf)

- Eine wandernde Nullstelle: ~60 %. Grund: Bei t = 0,9 und t = 1 gibt es im gerechneten Bereich je genau einen Wechsel
  von + nach - mit gleichem Umlauf.
- Falte: ~30 %. Grund: Bei t = 0,9 naehert sich s am oberen Rand der Null (-4,8e-4 bis -1,07e-3, zum Rand hin kleiner).
- Falls eine wandernde Nullstelle: Lage bei t = 0,95 zwischen 0,88 und 0,91 (~60 %).

## Rahmen

Code-Agent (Fortsetzung). Nur .69 ueber kleintest.sh, Spuren cpu3 und cpu4. PLAN-Abschnitt "Karte 2c" vor dem ersten
Lauf einfrieren. Zeitbox 30 min.
