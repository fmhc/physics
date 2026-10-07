# SCHWERE-MASSE-V: Wiegt die Bindungsenergie eines Q-Balls auf Finns Netz V so viel wie seine uebrige Energie? (Runde 50, Versuch ohne Karte, Karte nachgearbeitet)

- Leitung claude-primary. Versuch gestartet vor 16:51:51 (Protokoll RUNDE-50.md) ohne Karte (Finn, 05.10. 15:38: "einfach
  machen und ausprobieren"). Diese Karte ist nachgearbeitet ab 2026-10-05 17:05:57 CEST (date), auf Finns Wunsch ("Arbeite
  ggf die Karten dafuer nach"). Zu dieser Zeit lag im Ordner keine Ergebnisdatei (nur code/ und lauf-69/, nicht gelesen).
  Die Erwartungen unten sind deshalb vor dem Ergebnis geschrieben, aber nach dem Start.
- **Frage:** GR-Pruefliste Nr. 9. Ist die schwere (aktive) Masse eines gebundenen Q-Balls, gelesen aus dem Fernfeld des Takts,
  gleich seiner Gesamtenergie, unabhaengig vom Anteil der Bindungsenergie? Messdaten: MICROSCOPE prueft das
  Aequivalenzprinzip auf etwa 1e-15 [L].
- **Herkunft [P]:** MATERIE-NETZ-1 (Quelle mit V1-Kanal, Takt mit Einsteins Vorzeichen, Q-Ball als Materie);
  RUNDE-49/GR-PRUEFLISTE-v2.md Nr. 9; RUNDE-50/GRUNDGLEICHUNG-v3.md.
- **Ableitbarkeit [M]:** Koppelt die Quelle nur an die Energiedichte, ist M_schwer = E schon durch den Aufbau. Koppelt sie an
  rho + 3p (Tolman), gilt M_schwer = E nur, wenn die Spannungsspur im Gleichgewicht verschwindet (von Laue, Virialsatz);
  auf dem Gitter erwartet man einen Rest, der mit der Groesse R faellt.

## Erwartungen der Leitung (vor dem Ergebnis, nach dem Start)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| SM1 | M_schwer / E = 1 auf 1e-3 fuer alle gerechneten Q-Baelle, unabhaengig vom Bindungsanteil | 70 % |
| SM2 | Das Integral der Spannungsspur ist auf dem Gitter nicht exakt null; der Rest faellt mit R wie (a/R)^p, p >= 2 | 60 % |

## Rahmen

- Wie im Auftrag an den Agenten (RUNDE-50.md): Spuren cpu2 bis cpu4 ueber kleintest.sh, je Lauf hoechstens 10 min,
  keine Urteile, kein Leser. Synthetisch, keine Messdaten.
