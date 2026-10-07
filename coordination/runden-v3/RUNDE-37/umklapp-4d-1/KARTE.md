# UMKLAPP-4D-1: Wird der Energiesprung der Geometrie beim Umklappen kleiner, wenn die Traegheit aus der 4D-Wirkung kommt? (Runde 50, Versuch ohne Karte, Karte nachgearbeitet)

- Leitung claude-primary. Versuch gestartet vor 17:04:39 (Protokoll RUNDE-50.md) ohne Karte (Finn, 05.10. 15:38:
  "einfach machen und ausprobieren").
- Diese Karte ist nachgearbeitet ab 2026-10-05 17:05:57 CEST (date), auf Finns Wunsch ("Arbeite ggf die Karten dafuer
  nach"). Zu dieser Zeit war der Ordner leer. Die Erwartungen unten stehen also vor dem Ergebnis, aber nach dem Start.
- **Frage:** Grundgleichung v3, Abschnitt 6, Punkt 2. Unter Form A2 ist der Geometriesprung beim 2-3-Zug 5e5- bis 2e6-mal
  groesser als der Skalarsprung und schrumpft nicht mit dem Ueberschuss mu (KANON-TRANSFER-1). Bleibt das, wenn die
  Traegheit M_eff aus der 4D-Zeltwirkung in der stetigen Grenze stammt (UEBERLEITUNG-V-1/-2)?
- **Herkunft [P]:** KANON-TRANSFER-1, UEBERGABE-KONFLUENZ-1 (gespeicherte Faelle, Glas N = 128), UEBERLEITUNG-V-1/-2
  (M_eff), RUNDE-50/GRUNDGLEICHUNG-v3.md.
- **Ableitbarkeit:**
  - [M] Eine Kante kommt beim 2-3-Zug neu hinzu; fuer sie braucht es eine Regel (Laenge stetig, Rate frei waehlbar).
  - [H] Haengt M_eff an der Kosphaerizitaet stetig von der Lage ab, sollte der Sprung mit mu fallen.

## Erwartungen der Leitung (vor dem Ergebnis, nach dem Start)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| U1 | Mit M_eff faellt der Geometriesprung mit mu (Exponent >= 1 zwischen mu = -1e-3 und -1e-4) | 45 % |
| U2 | Bei mu = -1e-4 ist der Sprung mit M_eff mindestens 10-mal kleiner als mit Form A2 | 45 % |
| U3 | M_eff auf dem Glas macht Schwierigkeiten (mehr negative Richtungen als Ecken oder schlechte Kondition) | 50 % |

## Rahmen

- Wie im Auftrag an den Agenten (RUNDE-50.md): Spuren cpu5 und cpu6 ueber kleintest.sh, je Lauf hoechstens 10 min,
  keine Urteile, kein Leser. Synthetisch, keine Messdaten.
