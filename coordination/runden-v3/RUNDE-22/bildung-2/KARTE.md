# BILDUNG-2: Woran scheiterten die KF-5-Tropfen: Groesse, Wellenbad oder Verschmelzen? (Runde 22, Fast Lane)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 19:30:12 CEST (date), vor jedem Lauf.
- Herkunft:
  - BILDUNG-1 (R22): Einzelne Gauss-Klumpen bei omega^2 = 0,60 (Q = 66,6) laufen in 50 bis 200 Einheiten auf die
    Familie. M1 ist in 2D fuer isolierte Klumpen bildungsfaehig [H].
  - KF-5 (R6, R20): Tropfen mit Q ~ 1300 bis 2100 im Wellenbad verschmolzen und waren nie "auf".
  - Drei Kandidaten fuer den Unterschied: Groesse (duennwandig), Wellenbad, Verschmelzen.
- Ableitbarkeitspruefung: Keiner der drei Arme ist im Projekt gerechnet; die Ausgaenge sind aus vorhandenen Dateien nicht
  ablesbar.
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min (Abschnitte mit Zwischenspeicher erlaubt).

## Test

- Aufbau, Integrator, Klassifikator und Box wie BILDUNG-1 (RUNDE-22/bildung-1/bildung1.py), unveraendert importiert.
  Beide Gitter. Klassifikation zu T = 100, 250, 500, 1000.
- **Arm A (Groesse):** ein Klumpen vom Typ (i) gegen den Familienball bei omega^2 = 0,52 (duennwandig, grosses Q). Box
  gegebenenfalls groesser; im Plan festlegen.
- **Arm B (Wellenbad):** Klumpen (i) bei omega^2 = 0,60 plus ein zufaelliges Wellenbad (feste Saat). Die Ladung des Bads
  in der Box betraegt 20 % von Q_F, raeumlich gleichmaessig; die Erzeugung legt der Plan fest.
  - **K-Arm B0:** ein exakter Familienball im selben Bad. Er muss "auf" bleiben, sonst ist der Klassifikator im Bad
    nicht brauchbar.
- **Arm C (Verschmelzen):** zwei Klumpen (i) bei omega^2 = 0,60, Mittenabstand 3 R_F, gleichphasig, ruhend. Gebietszahl
  wie in Bio 28 weiter (Maske aus Runde 5/21 bzw. der Klassifikator-Maske; im Plan festlegen).

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| C0 | K-Arm B0: exakter Ball im Bad bleibt bis T = 1000 "auf" | 60 % |
| C1 | Arm A: "auf" und rund bei T = 500, beide Gitter | 55 % |
| C2 | Arm B: "auf" und rund bei T = 500, beide Gitter (nur wertbar, wenn C0 eintrifft) | 50 % |
| C3 | Arm C: Die Klumpen verschmelzen (Gebietszahl 1), bevor einer von ihnen "auf" ist | 55 % |
| C4 | Arm C: Das verschmolzene Gebilde ist bei T = 1000 "auf" und rund | 35 % |

**Bedeutung (vorab):**
- C1 und C2 treffen ein, C4 nicht: Groesse und Bad hindern die Bildung nicht; das "nie auf" in KF-5 lag am Verschmelzen
  [H].
- C1 trifft nicht ein: Grosse, duennwandige Klumpen erreichen die Familie langsamer oder gar nicht.
- C2 trifft nicht ein (bei C0): Das Wellenbad hindert die Bildung.
- C0 trifft nicht ein: Der Klassifikator taugt im Bad nicht; Arm B bleibt offen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (bei Belegung p4000b), je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 90 min.
