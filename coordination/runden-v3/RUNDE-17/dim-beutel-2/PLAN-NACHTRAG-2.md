# DIM-BEUTEL-2 Plan-Nachtrag 2 (NACHTRAEGLICH, waehrend der Hauptlaeufe)

- Geschrieben ab 2026-10-02 11:12 CEST (date vor dem Schreiben: 11:12:18). Hauptlaeufe laufen seit 11:07:55.
- Gesehen hatte ich zu diesem Zeitpunkt:
  - F1: Stufen k = 34 bis 70 (Logzeilen);
  - F2: Stufen k = 14 bis 42 und die Form A bei k = 44. Sie lief 103 s und 20003 Iterationen und erfuellt das
    Konvergenzkriterium nicht (Gradient 2e-5 > 1e-5).
- Er aendert nichts an Modell, Graphen, Formen, Loeser-Einstellungen, Stufenlisten, Wertung, E1 bis E4 und
  Bedeutung.

## Nur Zeitplan (Lauf-Reihenfolge)

- Anlass: Die oberen F2-Stufen werden teuer (grosse Beutel, kleine Eigenwerte). Die vier geplanten F2-Aufrufe auf
  cpu2 reichen womoeglich nicht bis k = 64.
- **Aenderung:** Ist die Kette auf cpu fertig (F1 Haupt und F1 Kontrolle), rechnet cpu zusaetzlich F2-Hauptstufen
  von oben nach unten. Dabei gelten derselbe Code, derselbe Tag vic8 und dieselben Einstellungen, mit
  klist = 64, 62, 60, 58, 56, 54, 52, 50.
- Das aendert keine Zahl: Frische Starts haengen nicht von der Reihenfolge oder der Spur ab. Jede Stufe startet
  neu aus A, Bm und Bp.
- Rechnen beide Spuren dieselbe Stufe, gilt der zuletzt geschriebene Stufen-Datensatz (Auswertung). Doppelte
  Stufen werden im Ergebnis genannt.
- F2-Kontrolle (g = 7) bleibt am Ende der cpu2-Kette.
