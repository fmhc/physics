# DIM-BEUTEL-2 Plan-Nachtrag 7 (NACHTRAEGLICH, nur Zeitplan der F2-Kontrolle)

- Geschrieben ab 2026-10-02 11:49 CEST (date vor dem Schreiben: 11:49:27).
- Gesehen hatte ich: alle Hauptstufen F1 und F2, die Zwischenauswertung 2 (aus/auswertung-zwischen2/, nicht
  gewertet) und die F2-Kontrolle (g = 7, voller Graph) bis k = 32. Allein k = 32 brauchte dort 139 s.
- Er aendert nichts an Modell, Formen, Loeser-Einstellungen, Wertung, E1 bis E4 und Bedeutung.

## Aenderungen

- Laeufe enden laut Plan spaetestens 12:02. Ein zweiter Aufruf der F2-Kontrolle auf cpu2 wuerde nach etwa 11:55
  beginnen und bis etwa 12:05 laufen.
  - Deshalb habe ich die bash-Schleife der cpu2-Kette auf der .69 per PID beendet (nur die Schleife).
  - Der laufende Aufruf 1 der F2-Kontrolle laeuft unberuehrt zu Ende.
- **Neu auf cpu** (frei seit 11:47): ein Aufruf der F2-Kontrolle mit derselben Version 3, demselben Tag vic7v und
  denselben Einstellungen (g = 7, voller Graph, nur A, ohne Fortsetzung), klist = 50, 44.
  - Das sind die beiden oberen Kontrollstufen im F2-Beutelbereich. k = 56 und 62 liegen ausserhalb und entfallen
    (Plan 5: zuerst die oberen Stufen der Kontrollen).
  - Rechnen beide Spuren k = 44, gilt der letzte Stufen-Datensatz; das wird gemeldet.
- Die Schlussauswertung laeuft, sobald beide Aufrufe fertig sind, spaetestens um 12:02, mit dem bis dahin
  geschriebenen Stand.
