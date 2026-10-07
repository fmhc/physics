# DIM-BEUTEL-2 Plan-Nachtrag 6 (NACHTRAEGLICH, nur Zeitplan)

- Geschrieben ab 2026-10-02 11:36 CEST (date vor dem Schreiben: 11:35:58).
- Gesehen hatte ich zusaetzlich: F2 k = 52 ist fertig (Version 3b auf cpu, 273 s). Damit fehlt fuer den
  zusammenhaengenden Bereich k = 18 bis 54 nur noch k = 50.
- Er aendert nichts an Modell, Formen, Loeser-Einstellungen, Stufenlisten, Wertung, E1 bis E4 und Bedeutung.

## Aenderungen

- Die wartenden Aufrufe 2 und 3 der cpu-Kette 3b (klist 52, 56, 58, 50) habe ich beendet. Lokal per PID, auf der
  .69 per PID: bash-Schleife, kleintest und flock. Sie warteten nur auf die Spur, keine Rechnung lief.
  - Grund: Sie haetten zuerst k = 56 gerechnet. Das ist fuer drei Perioden nicht noetig.
- **Neu auf cpu:** ein Aufruf Version 3b nur fuer k = 50 mit der Formreihenfolge Bp, A, Bm (zweiter Aufruf, falls
  noetig).
  - Die Reihenfolge der Formen aendert keine Zahl: Jede Form startet frisch, gewertet wird das Minimum der
    konvergierten Formen.
  - So rechnet cpu Bp, waehrend cpu2 (Kette 3b-k50, Reihenfolge A, Bm, Bp) A und Bm rechnet. Fertige Formen werden
    ueber die Formzustaende geteilt.
- Die F2-Kontrolle (g = 7) bleibt auf cpu2; die F1-Kontrolle laeuft auf cpu zu Ende.
