# UMKLAPP-FOLGE-1: Heizt eine Folge von Umklappzuegen das Netz auf, wenn die Traegheit aus der 4D-Wirkung kommt? (Runde 50, schlanke Karte nach dem Codex-Gegenblick)

- Leitung claude-primary, geschrieben ab 2026-10-05 18:31:02 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - UMKLAPP-4D-1: Mit M_eff ist der Sprung je Einzelzug 60- bis 1e7-mal kleiner als unter Form A2 und faellt wie mu.
  - Codex-Gegenblick (Bus 6136add5): Im P-Arm sind alle 56 Spruenge positiv; wiederholte Umbauten koennten heizen.
    Entscheidender Test: kumulativer Energiefehler einer Umbaufolge gegen eine Referenz ohne Umbau.
  - TAKT-DYNAMIK-1: Dynamik mit Umklappen unter Form A (R verliert 2,4 bis 12,7 %, P gewinnt 15 bis 20 % ueber 10 Perioden).
- **Ableitbarkeit:** [M] Sind alle Einzelspruenge positiv und unabhaengig, waechst der kumulative Fehler linear mit der
  Zahl der Zuege. Nicht ableitbar sind Groesse und Vorzeichen in einer echten Folge (Korrelationen, Rueckzuege).

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| UF1 | Mit M_eff und P bleibt die Energiedrift einer Welle ueber 10 Perioden mit Umklappen unter 1e-4 relativ (gegen dieselbe Welle ohne Umklappen) | 50 % |
| UF2 | Im P-Arm waechst die Energie monoton mit der Zahl der Zuege (Heizen) | 55 % |
| UF3 | Der R-Arm driftet weniger als der P-Arm | 50 % |

## Rahmen

- Code-Agent (Folgeauftrag an den UMKLAPP-4D-1-Agenten), ohne Einfrieren und Leser (Finn: einfach machen).
- TAKT-DYNAMIK-1-Aufbau (Glas, Welle, Umklappen in der Zeitentwicklung), Traegheit M_eff wie UMKLAPP-4D-1, Arme P und R,
  Referenz ohne Umklappen.
- Spuren cpu2 bis cpu4 ueber kleintest.sh, je Lauf hoechstens 10 min; df vor jedem Lauf.
- Synthetisch, keine Messdaten.
