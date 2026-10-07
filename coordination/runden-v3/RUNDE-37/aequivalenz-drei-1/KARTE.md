# AEQUIVALENZ-DREI-1: Sind schwere, fallende und traege Masse eines Q-Balls auf Finns Netz dieselbe, aus einer einzigen Wirkung? (Runde 50, schlanke Karte nach dem Codex-Gegenblick)

- Leitung claude-primary, geschrieben ab 2026-10-05 19:14:43 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - Codex-Gegenblick (Bus 6136add5): Ein unabhaengiger Aequivalenztest muss Quellwirkung, freien Fall und
    Traegheitsantwort aus derselben Wirkung vergleichen.
  - SCHWERE-MASSE-V: M_schwer = E durch den Aufbau; mit metrischer Kopplung Virialrest S/E ~ 0,1 (a/R)^2.
  - NETZ-GPU (qball-fall-v): zwei Baelle mit 8,6 % und 2,1 % Bindung fallen auf 0,15 % gleich; bei h = 1 haftet der Ball
    am Gitter (24 bis 27 % des Wegs), bei h = 0,8 nicht.
- **Ableitbarkeit:**
  - [M] Bei metrischer Kopplung folgen aktive, passive und traege Masse im Kontinuum aus derselben Wirkung (von Laue,
    Virialsatz).
  - Nicht ableitbar: die Gitterreste je Masse und ihre Abhaengigkeit von der Bindung bei endlicher Aufloesung.

## Messgroessen (alle mit der GPU-Engine netzgpu, metrische Kopplung mit Spannungsterm)

- M_aktiv: 1/r-Anteil des Takts im Fernfeld des ruhenden Q-Balls.
- M_passiv: Fallbeschleunigung in einem vorgegebenen schwachen Takt-Gefaelle, geteilt durch das Gefaelle.
- M_traege: Impuls je Geschwindigkeit eines langsam bewegten (geboosteten) Q-Balls, p/v.
- Je mindestens drei Baelle mit verschiedener Bindung (2 bis 10 %), Gitterabstand h = 0,8 und 0,6.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| AQ1 | M_passiv / M_traege = 1 auf 1e-3 fuer alle Baelle (h = 0,8) | 65 % |
| AQ2 | M_aktiv / M_traege = 1 auf 1e-3 fuer alle Baelle (h = 0,8) | 40 % |
| AQ3 | Die Abweichungen faellen von h = 0,8 auf h = 0,6 um mindestens den Faktor 1,5 (Gittereffekt) | 60 % |
| AQ4 | Keine Abhaengigkeit des Quotienten M_passiv/M_traege vom Bindungsanteil groesser als 5e-4 | 55 % |

## Rahmen

- Code-Agent ohne Einfrieren und Leser (Finn: einfach machen); Engine-Code aus coordination/runden-v3/netz-gpu/code
  bzw. auf der .69 /home/fmh/fmhc-physics-remote/netz-gpu/code (nur kopieren oder als Bibliothek nutzen, nicht aendern).
- GPU-Spuren p4000a und p4000b ueber kleintest.sh, je Lauf hoechstens 10 min; df vor jedem Lauf.
- Synthetisch, keine Messdaten.
