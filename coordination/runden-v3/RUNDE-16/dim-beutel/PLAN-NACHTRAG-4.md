# DIM-BEUTEL Plan-Nachtrag 4 (NACHTRAEGLICH, waehrend der Laeufe)

- Geschrieben ab 2026-10-02 10:21:18 CEST (date).
- Gesehen hatte ich:
  - Z3-Ergebnisse (frische Starts bei k = 46 bis 82);
  - den Sierpinski-Aufwaertsast bis k = 67 (k = 67 nicht konvergiert, Beutelsprung 601 -> 1007 Knoten);
  - eine Probe-Auswertung auf Teildaten (G3 K_v = 76, G4 K_v = 66).
- Er aendert nichts an Modell, Graphen, D1 bis D5, Bedeutung und Hauptwertung.

## 1. Kontrollen fuer Z3 statt fuer den haengenden Ast

- Die geplanten G4-Kontrollen (g = 9 und s2) waren als Fortsetzungsaeste angelegt. Die Aeste haengen auf dem Fraktal
  fest, also vergleichen sie Hysterese mit Hysterese.
- Ersatz: dieselben frischen Starts wie Z3 (Startform A, R0 = Q^0,4) bei k = 46, 58, 70.
  - auf g = 9 mit s1 (Groessenkontrolle);
  - auf g = 10 mit s2 (Startknoten-Kontrolle).
- Berichtet werden wie in Z3 die Verhaeltnisse E(k+12)/E(k) und daraus p.
- Die Fortsetzungsaeste g = 9 und s2 fallen weg. Den Abwaertsast von oben (Z1) und den Abwaertsast ab k_s fuer G4
  rechne ich nur, wenn Zeit bleibt.

## 2. Kette

- Mit maxcor 5 erreichte die Kette das Konvergenzkriterium (Nachtrag 1, N2) ab k = 54 nicht mehr.
- Der Aufwaertsast der Kette wird deshalb mit maxcor 20 neu gerechnet (Tag ket4096m20-auf), ebenso die
  Groessenkontrolle 8192 (ket8192m20-auf). Der maxcor-5-Versuch wurde abgebrochen und wird nicht gewertet.
- Der Abwaertsast der Kette (maxcor 5) bleibt; er wird nur fuer D5 (kleines Q) gebraucht.

## 3. Zeitbox

- Laeufe enden spaetestens um 10:58. Danach kommen Auswertung und Bericht.
