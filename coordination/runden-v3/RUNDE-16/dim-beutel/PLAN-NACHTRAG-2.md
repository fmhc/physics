# DIM-BEUTEL Plan-Nachtrag 2 (NACHTRAEGLICH, waehrend der Hauptlaeufe)

- Geschrieben ab 2026-10-02 10:07:36 CEST (date), NACH dem Start der Hauptlaeufe (10:05:40).
- Gesehen hatte ich zu diesem Zeitpunkt: Sierpinski g = 10, s1, Aufwaertsast k = 40 bis 49, dazu die Rauchtests.
- Er aendert nichts an Modell, Graphen, D1 bis D5 und Bedeutung. **Die eingefrorene Wertung (PLAN 4, Wertung auf dem
  Fortsetzungsast) bleibt die Hauptwertung.**

## Anlass

- Auf dem Sierpinski-Graphen waechst der Beutel beim Aufwaertsast nicht mit. Von k = 40 bis 49 bleibt V_bag bei
  139 bis 179 Knoten, und p_loc steigt von 0,67 auf 0,85.
- Schreibtisch: Bei Q = 2373 haette ein linear doppelt so grosser Bereich (Volumen x 3, lambda_1 / 5) etwa
  E ~ 130 + 134 = 264 statt 339. Der Ast steckt also sehr wahrscheinlich in einem metastabilen Zustand fest
  (Huelle haengt an den Engstellen des Fraktals: Wachstum in ein Nachbar-Teildreieck geht nur ueber einen
  Knoten).
- Folge: Der Fortsetzungsast misst auf G4 eine Hysterese-Kurve, nicht unbedingt das Minimum E(Q). Das Problem ist
  numerisch (Minimumsuche), nicht physikalisch.

## Zusatzrechnung (NACHTRAG)

- **Z1:** Sierpinski g = 10, s1, Abwaertsast von oben. Frische Startform A bei k = 87 (R0 = Q^0,4), dann
  Fortsetzung abwaerts bis k = 0. Dieser Ast bleibt eher bei zu grossen Beuteln haengen; der Aufwaertsast eher bei zu
  kleinen.
- **Z2 (nur falls Zeit):** dasselbe fuer das Quadratgitter 256^2 (k = 79 abwaerts) als Hysterese-Probe auf einem
  gewoehnlichen Gitter.

## Zusatzauswertung (NACHTRAG, ausdruecklich zweitrangig)

- **Einhuellende:** E_env(Q_k) = Minimum aller auf dem Hauptgraphen bei Q_k gefundenen Energien. Beitraege:
  Aufwaertsast, Abwaertsast ab k_s, Abwaertsast von oben und die frischen Starts.
- p*_env ist die Sekante ueber die letzte volle Periode der Einhuellenden. Gueltigkeit und Fehlerband werden wie in
  PLAN 4 bestimmt.
- D4 wird zusaetzlich auf der Einhuellenden ausgewiesen. Das Ergebnis traegt die Marke "Nachtrag-Wertung" und
  ersetzt die Hauptwertung nicht.
- Fuer G1 bis G3 wird die Einhuellende ebenso berichtet (Hysterese-Probe), soweit Abwaertsaeste von oben vorhanden
  sind.
- Jede Abweichung zwischen Ast und Einhuellender (> 1e-6 relativ) wird als Konkurrenzzustand gemeldet.
