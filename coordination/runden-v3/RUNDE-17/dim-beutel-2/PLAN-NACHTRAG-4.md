# DIM-BEUTEL-2 Plan-Nachtrag 4 (NACHTRAEGLICH, waehrend der Hauptlaeufe)

- Geschrieben ab 2026-10-02 11:29 CEST (date vor dem Schreiben: 11:29:05).
- Gesehen hatte ich:
  - F1 Haupt komplett (k = 34 bis 78), die Zwischenauswertung (aus/auswertung-zwischen/, nicht gewertet) und die
    F1-Kontrolle bis k = 62;
  - F2 bis k = 48, dazu k = 54 (Spur cpu, Nachtrag 3).
  - Bei F2 k = 50 brauchte Bm in Aufruf 2 ueber 379 s (dann ZEITGRENZE) und in Aufruf 3 genau 30000 Iterationen
    (399,5 s, nicht konvergiert).
- Er aendert nichts an Modell, Formen, Loeser-Einstellungen, Stufenlisten, Wertung, E1 bis E4 und Bedeutung.

## 1. Code-Version 3b (nur Ablauf)

- Anlass: Eine Stufe mit langsamer Form passt womoeglich nicht in einen Aufruf (540 s). Mit Version 3 wird sie dann
  in jedem Aufruf von vorn gerechnet und nie fertig.
- **dimbeutel3b.py** = dimbeutel3.py plus Formzustand:
  - Jede fertig gerechnete Form einer Stufe wird gespeichert (formzustand-<tag>-k<k>-<form>.npz: Loesung, Rcut,
    Datensatz).
  - Ein spaeterer Aufruf laedt fertige Formen, statt sie neu zu rechnen. Die Form wird im Datensatz mit
    aus_zustand = true markiert.
  - Physik, Startformen, Loeser-Einstellungen und die +-Fortsetzung sind unveraendert.
  - Eine geladene Form ist bitgleich mit einer neu gerechneten, denn frische Starts sind deterministisch.
- Version 3 laeuft auf cpu2 unveraendert weiter (Kette aus Nachtrag 1). Version 3b laeuft nur auf cpu.

## 2. Zeitplan

- Die wartende Kette "F2 von oben" (Nachtrag 2, k = 64 abwaerts, Version 3) habe ich per PID beendet. Sie hatte noch
  nichts gestartet; auf der .69 lief nichts von ihr. Grund: k = 64 waere mit Version 3 nie fertig geworden.
- **Neu auf cpu** (wartet auf die Spur, Version 3b, Tag vic8, gleiche Einstellungen): klist = 52, 56, 58, 50; bis zu
  drei Aufrufe.
- Ziel ist der zusammenhaengende Beutelbereich ab k = 18 bis mindestens k = 54 (drei volle Perioden).
- Die F2-Kontrolle (g = 7) bleibt am Ende der cpu2-Kette. Die F1-Kontrolle laeuft auf cpu zu Ende. Ihre oberen Stufen
  (74, 78) liegen ausserhalb des F1-Beutelbereichs.
