# DIM-BEUTEL-2 Plan-Nachtrag 1 (nach Rauchtest und d_s-Lauf, VOR den Hauptlaeufen F1/F2)

- Geschrieben ab 2026-10-02 11:07:30 CEST (date). Nachtraeglich zum eingefrorenen Plan (11:04:53).
- Gesehen hatte ich:
  - die Rauchtests R2 und R3 (aus/rauch/, nicht gewertet);
  - den d_s-Lauf (aus/ds/, laut Plan gewertet; d_s/2 je Spektralperiode meist exakt ln5/ln15).
- Er aendert nichts an Graphen, Formen, Wertung, E1 bis E4 und Bedeutung. Er legt nur fest, was der Plan nach dem
  Rauchtest offen liess.

## Rauchtest (nicht gewertet)

- R1: Vicsek-Graphbau g = 5, 7, 8 im d_s-Lauf: 5^g Knoten, 5^g - 1 Kanten, zusammenhaengend. Die Baum-Zaehlung
  stimmt bei g = 5 an allen fuenf Pruefstellen mit den dichten Eigenwerten ueberein.
- R2: Sierpinski g = 10, k = 46, A auf dem Teilgebiet (nach einer Rcut-Erweiterung 2869 Knoten) gibt E = 178,2632151.
  Das ist Z3 aus DIM-BEUTEL (178,26321514805, voller Graph). Laufzeit 0,3 s.
- R3: Vicsek g = 8, k = 36, A: maxcor 20 und 10 geben dieselbe Energie, Laufzeit 0,4 bzw. 0,3 s. Die Stufe mit
  Fortsetzung brauchte 0,9 s.

## Festlegungen

- **Loeser fuer alle gewerteten Folgen:** L-BFGS-B, Jacobi-Skalierung, gtol 1e-7, ftol 1e-15, maxiter 30000,
  **maxcor 20** (wie DIM-BEUTEL), eps = 0,01 fuer die Fortsetzung. Keine Aenderung waehrend einer Folge.
- **F2 bekommt 6 Stufen je Periode** (Regel aus PLAN 5: Stufe k = 36 deutlich unter 40 s):
  - Hauptlauf k = 14, 16, ..., 64 (26 Stufen);
  - Kontrolle g = 7, voller Graph, nur A, k = 14, 20, ..., 62 (9 Stufen).
- F1 bleibt wie im Plan: Haupt k = 34, 36, ..., 78; Kontrolle g = 9, k = 34, 38, ..., 78.
- Reihenfolge: cpu2 rechnet F2 Haupt, dann F2 Kontrolle; cpu rechnet F1 Haupt, dann F1 Kontrolle.
