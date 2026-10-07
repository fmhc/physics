# SCHWEBUNGSUHR-3: Pendeln oder Drift? Startphasen-Probe (Runde 23, Leitung)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 22:30:46 CEST (date), vor jedem Lauf.
- Herkunft: Gegenlesen von SCHWEBUNGSUHR-2 durch die Leitung (RUNDE-23.md, jq auf lauf-69/S*.json).
  - Bei D = 18 und 22 ist Q_1(t = 0) genau das Minimum der Zeitreihe, das Mittel liegt in der Mitte der Spanne, und die
    Fenstermittel sind vom Anfang bis zum Ende konstant.
  - Die Schreibtisch-Lesart [H]: ein AC-Josephson-Pendeln, dQ_1/dt = -K sin(phi_1 - phi_2), mit phi_1 - phi_2 =
    theta - |Delta omega| t.
  - Daraus folgt Q_1(t) - Q_1(0) = (K/|Delta omega|) [cos(theta) - cos(theta - |Delta omega| t)]:
    - theta = 0: Pendeln oberhalb des Starts (wie gemessen)
    - theta = pi: Pendeln unterhalb des Starts
    - theta = pi/2: Pendeln symmetrisch um den Start
  - Der "Gewinn des grossen Balls" im schwachen Bereich waere damit nur ein Versatz der Startphase.
- Ableitbarkeitspruefung: Die Rohdaten von SCHWEBUNGSUHR-2 enthalten nur theta = 0. Die Lage bei theta = pi und pi/2
  folgt nicht aus vorhandenen Dateien, nur aus dem Modell der Leitung. Das Modell ist die Hypothese, die hier geprueft wird.
- Explorativ (v3), M1 in 1D, Code unveraendert: RUNDE-23/schwebungsuhr/code/schwebung1d.py, Modus paar, Argument
  theta in Einheiten von pi.

## Laeufe (alle omega^2 = 0,60 / 0,65, dx 0,1, T = 3000, L = 900, wie SCHWEBUNGSUHR-2)

| Name | D | theta/pi | wofuer |
|---|---|---|---|
| P22 | 22 | 1 | J1, J2, J3, J5 |
| P18 | 18 | 1 | J2, J5 |
| H22 | 22 | 0,5 | J4 |
| P12 | 12 | 1 | J6 (starker Bereich) |

## Vorhersagen (vor jedem Lauf)

Bezeichnungen wie in SCHWEBUNGSUHR-2:
- roh_Q1 ist die Zeitreihe von Q_1 aus der Analyse des Skripts.
- Spanne = max - min von roh_Q1.
- Fenster A = [50; 447,3], Fenster E = [2602,7; 3000] (ladungen.anfang / ladungen.ende).
- r = (Delta omega_E - Delta omega_frei) / Delta omega_frei mit Delta omega_frei = 0,031633058913306 (dx 0,1).

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| J1 | P22: Q_1(0) ist praktisch das Maximum (max(roh_Q1) - Q_1(0) < 0,05 Spanne), und Q_1 in Fenster A und E liegt unter Q_1(0) | 80 % |
| J2 | P22 und P18: r < 0 | 75 % |
| J3 | P22: Spanne innerhalb +-25 % der Spanne bei theta = 0 (6,647e-4) | 70 % |
| J4 | H22: Mittel von roh_Q1 ueber [50; 3000] liegt innerhalb +-0,15 Spanne um Q_1(0) | 60 % |
| J5 | P22: Q_1 in Fenster A und E unterscheiden sich relativ um < 1e-5; P18: < 1e-4 | 75 % |
| J6 | P12: Q_1 in Fenster E liegt unter Q_1(0) (der grosse Ball verliert beim schnellen Anfangsfluss) | 55 % |

**Bedeutung (vorab):**
- J1 bis J5 treffen ein: Im schwachen Bereich ist der Takt-Versatz aus SCHWEBUNGSUHR-2 ein Josephson-Pendeln mit
  Startphasen-Versatz. Es gibt keine fortlaufende Drift und keinen Netto-Fluss vom kleinen zum grossen Ball [H, 1D].
  "Die Uhren laufen auseinander" gilt dann nur als Versatz, nicht als Gesetz.
- J1 oder J2 trifft nicht ein (der grosse Ball gewinnt auch bei theta = pi): Es gibt einen phasenunabhaengigen Fluss zum
  grossen Ball (reifungsartig). Die Josephson-Lesart der Leitung ist dann falsch.
- J6 entscheidet getrennt: Trifft J6 ein, setzt die Startphase auch die Richtung des einmaligen Anfangsflusses im starken
  Bereich. Trifft J6 nicht ein, gewinnt der grosse Ball dort unabhaengig von der Phase.

## Rahmen

- Leitung rechnet selbst auf der .69 (kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4), je Lauf ~90 s.
- Plan = diese Karte. Sie wird vor dem ersten Lauf als KARTE.md.eingefroren-<zeit> schreibgeschuetzt kopiert.
- Auswertung nur mit jq auf den Ergebnisdateien (lokal). Kein Hilfsskript.
