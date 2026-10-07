# DIM-BEUTEL-2 Plan-Nachtrag 3 (NACHTRAEGLICH, waehrend der Hauptlaeufe)

- Geschrieben ab 2026-10-02 11:20 CEST (date vor dem Schreiben: 11:19:54).
- Gesehen hatte ich:
  - F1 bis k = 76; die beste Form bei k = 74 hat R_bag = 136, liegt also ueber R_self/2 = 128 und damit ausserhalb des
    Beutelbereichs;
  - F2 bis k = 48 und die Form A bei k = 50. Bm bei k = 50 rechnet seit ueber 250 s.
- Er aendert nichts an Modell, Formen, Loeser-Einstellungen, Stufenlisten, Wertung, E1 bis E4 und Bedeutung.

## Nur Zeitplan

- Anlass: Bm konvergiert bei Vicsek oben sehr langsam. Eine F2-Stufe kann dann fast einen ganzen Aufruf brauchen.
  Ohne Parallelrechnung erreicht F2 vermutlich k = 54 nicht. Dann fehlen die drei vollen Perioden ab k = 18.
- Laut Plan 5 haben die obersten F2-Stufen Vorrang vor den Kontrollen.
- **Aenderung:** Ab sofort wartet ein weiterer F2-Aufruf auf die Spur cpu (gleicher Code, Tag vic8, gleiche
  Einstellungen) mit klist = 54, 56, 58, 60. Er bekommt die Spur, sobald der laufende F1-Aufruf endet, und kann
  dabei vor F1-Aufruf 3 und der F1-Kontrolle drankommen.
- cpu2 rechnet weiter aufsteigend (k = 50, 52, ...). Doppelt gerechnete Stufen sind wegen der frischen Starts
  bitgleich; es gilt der letzte Stufen-Datensatz. Sie werden im Ergebnis genannt.
