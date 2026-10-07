# DIM-BEUTEL Plan-Nachtrag 3 (NACHTRAEGLICH, waehrend der Laeufe)

- Geschrieben ab 2026-10-02 10:16:29 CEST (date).
- Gesehen hatte ich: Sierpinski s1, Aufwaertsast bis k = 65; kubisch bis k = 70; Rauchtests.
- Er aendert nichts an Modell, Graphen, D1 bis D5, Bedeutung und Hauptwertung (PLAN 4, Fortsetzungsast).

## Anlass

- Der Sierpinski-Aufwaertsast faellt immer weiter zurueck. Von k = 40 bis 65 waechst V_bag nur von 139 auf 601.
  Selbstaehnlich waeren x 3 je Periode, also etwa 1250 bei k = 64. p_loc steigt bis 0,91.
- Die Ein-Perioden-Sekante schwankt deshalb stark: k 47 -> 59 gibt 0,580, k 53 -> 65 gibt 0,812.

## Loeser (Ausfuehrungsdetail, schon umgesetzt ab 10:14)

- Ab den Fortsetzungsaufrufen gilt maxcor = 5 statt 20. Grund: L-BFGS-B kostet je Iteration ~ maxcor^2 x n, und die
  Laufzeit reichte nicht.
- Version dimbeutel2.py rechnet einen ZEITGRENZE-Punkt beim Fortsetzen neu (wie in Nachtrag 1, N3 vorgesehen).
- Physik, Funktional und Toleranzen sind unveraendert.

## Zusatzrechnung Z3 (fuer die Einhuellende aus Nachtrag 2)

- Frische Starts mit Startform A (Kugel R0 = Q^0,4 um s1) auf g = 10 bei k = 46, 52, 58, 64, 70, 76, 82.
  Das sind halbe Perioden. R0 waechst je Periode um 2,14, fast wie die Selbstaehnlichkeit (2).
- Sie gehen in die Einhuellende ein wie alle frischen Starts. Die Hauptwertung bleibt unberuehrt.
- Zusatzgroesse (nur berichtet): das Verhaeltnis E(k+12)/E(k) dieser frischen Starts. Selbstaehnlich (d_s) waere es
  3, mit p = ln 3/ln(3 sqrt 5) = 0,5772.
