# Q-STERN-2b: Gravitationsgesetz fuer die zweite stille Stelle (l = 0, n = 2) (Runde 15)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-02 01:22:22 CEST (date), vor jedem Lauf.
- Herkunft: RUNDE-14/q-stern2 (Q-STERN-2).
  - Fuer die erste Stelle (n = 1) ist die Verschiebung unter schwacher Eigengravitation ~ -0,47 x Kompaktheit
    2|Phi(0)| am Ort (Kompaktheit 0,01 und 0,03).
  - Die Rueckwirkung delta Phi aendert sie um ~2 %.
- Frage: Gilt dasselbe Gesetz fuer die zweite bewiesene Stelle l = 0, n = 2 (omega^2 = 0,6851289044582160933,
  rho = 1,690356597328143; BEWEIS-2, T1)?

## Methode

- Code qstern2.py aus RUNDE-14/q-stern2, unveraendert in der Physik. Erlaubt sind nur Aufrufparameter, also Fenster und
  Zeilen; braucht es eine Codeaenderung, dann neuer Name und Diff.
- Kopplungen alpha so gewaehlt, dass 2|Phi(0)| am Ort der n = 2-Stelle etwa 0,01 bzw. 0,03 ist. Vor dem Einfrieren
  messen.
- Je Kopplung voll (mit psi) und Cowling (psi = 0). Lokalisierung zuerst, wie in Q-STERN-2.

## Kontrollen (bindend)

- K1: alpha = 0 gibt die n = 2-Stelle auf 1e-4, Umlauf auf beiden Stufen wie bei alpha = 0 berichtet.
- K2: Hintergrund auf zwei Gittern auf 1e-6 relativ.
- K3: Aussenrand R gegen 1,5 R, Lage auf 1e-4.
- K5 nur berichten, mit dem in Q-STERN-2 gesehenen Rauschniveau als Vergleich; keine Bedingung.
- Verfehlt K1 oder K2: nicht auswertbar.

## Regel (bindend, je Kopplung und Rechnung)

- **Gesehen:**
  - lokalisiertes, aufgeloestes Rechteck (< 0,4 rad) mit Umlauf +-1 auf beiden Stufen, dazu ein Vorzeichenwechsel von s
  - Lage im Fenster 0,60 <= omega^2 <= 0,70, 1,60 <= rho <= 1,75
  - Stufen auf 1e-4 gleich, K3 bestanden
- **Nicht gesehen:** im Fenster kein Vorzeichenwechsel auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.

## Vorhersage (Leitung, vor jedem Lauf)

- V1: in voller Rechnung bei beiden Kompaktheiten gesehen. ~85 %.
- V2: Verschiebungskoeffizient k = Delta omega^2 / Kompaktheit (volle Rechnung) in [-0,71; -0,24], also -0,47 +- 50 %.
  ~60 %.
- V3: voll : Cowling (Verschiebung in omega^2) in [0,9; 1,1]. ~80 %.

## Rahmen

Code-Agent (Fortsetzung des Q-STERN-2-Agenten). Nur .69 ueber kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4, jeder Aufruf
hoechstens 10 min. PLAN-Abschnitt vor dem ersten Lauf einfrieren. Zeitbox 60 min.
