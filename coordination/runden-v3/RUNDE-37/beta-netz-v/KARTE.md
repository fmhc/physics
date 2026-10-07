# BETA-NETZ-V: Stimmt die Schwerkraft auf Finns Netz V auch in zweiter Ordnung der Masse (beta = 1)? (Runde 50, Versuch ohne Karte, Karte nachgearbeitet)

- Leitung claude-primary. Versuch gestartet vor 17:04:39 (Protokoll RUNDE-50.md) ohne Karte (Finn, 05.10. 15:38:
  "einfach machen und ausprobieren").
- Diese Karte ist nachgearbeitet ab 2026-10-05 17:05:57 CEST (date), auf Finns Wunsch ("Arbeite ggf die Karten dafuer
  nach"). Zu dieser Zeit war der Ordner leer. Die Erwartungen unten stehen also vor dem Ergebnis, aber nach dem Start.
- **Frage:** GR-Pruefliste Nr. 12 (Perihel). In isotropen Koordinaten gilt g_00 = -(1 - 2U + 2 beta U^2 + ...) mit
  beta = 1. Die Periheldrehung haengt an (2 + 2 gamma - beta)/3.
- **Herkunft [P]:** MATERIE-NETZ-1 (lineare Statik auf V, gamma = 1), REGGE-ZEIT-1 (Kuhn), licht-ablenkung-v (Takt und
  Laengen je zur Haelfte), RUNDE-49/GR-PRUEFLISTE-v2.md, RUNDE-50/GRUNDGLEICHUNG-v3.md.
- **Ableitbarkeit:**
  - [L, ungeprueft] Im Kontinuum geht Regge in Einstein ueber (Wong 1971, Barrett/Williams). Das Fernfeld sollte dann
    beta = 1 geben.
  - Echt gerechnet auf V sind nur das Gitter, die Eckenregel R1 fuer den Takt und die nichtlineare Loesung.

## Erwartungen der Leitung (vor dem Ergebnis, nach dem Start)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| B1 | Kontrolle: gamma = 1 auf 1 % im Fernfeld | 90 % |
| B2 | beta = 1 auf 5 % im Fernfeld (ab etwa 4 Gitterlaengen) | 60 % |
| B3 | Die nichtlineare Loesung konvergiert bis U ~ 0,1 bei r >= 2 Gitterlaengen | 70 % |

## Rahmen

- Wie im Auftrag an den Agenten (RUNDE-50.md): Spuren cpu8 bis cpu10 ueber kleintest.sh, je Lauf hoechstens 10 min,
  keine Urteile, kein Leser. Synthetisch, keine Messdaten.
