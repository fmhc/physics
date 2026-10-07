# DIM-BEUTEL-2 Plan-Nachtrag 5 (NACHTRAEGLICH, nur Zeitplan)

- Geschrieben ab 2026-10-02 11:31 CEST (date vor dem Schreiben: 11:31:4x, siehe Freeze-Stempel).
- Gesehen hatte ich zusaetzlich zu Nachtrag 4: F2 k = 50, Aufruf 3 (Version 3). Bp lief in die ZEITGRENZE
  (129 s nach Bm); Aufruf 4 (Version 3) rechnet k = 50 wieder von vorn und wird absehbar nicht fertig.
- Er aendert nichts an Modell, Formen, Loeser-Einstellungen, Stufenlisten, Wertung, E1 bis E4 und Bedeutung.
- **Neu auf cpu2:** zwei Aufrufe Version 3b nur fuer k = 50 (Tag vic8). Sie warten auf die Spur und konkurrieren
  nach Aufruf 4 mit der F2-Kontrolle um die Spur.
  - Laut Plan 5 haben F2-Hauptstufen Vorrang vor Kontrollen.
  - k = 50 und k = 52 werden fuer den zusammenhaengenden Beutelbereich bis k = 54 gebraucht.
