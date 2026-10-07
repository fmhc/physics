# QBALL-MONOPOL-1: Agenten-Vorhersagen (vor dem Lesen jedes Rauchlauf-Ergebnisses)

- Code-Agent, geschrieben ab 2026-10-04 08:04:27 CEST (date). Der Rauchlauf rauch1 war um diese Zeit gestartet; seine
  Ausgabe habe ich erst nach dem Schreiben dieser Datei gelesen.
- Grundlage: Schreibtisch [M] und die Freie-Ball-Familie aus QBALL-LADUNG-1 (fam-e0.json [P]).
  - Monopolkosten im Ball ~ (1/2) int f^2/r^2 d^3x = 2 pi int f^2 dr, also ~ 15 bis 20 bei Q ~ 200.
  - Topfgewinn hoechstens V0 pi^(3/2) f(0)^2 ~ 6 V0, am Monopol durch f ~ r^0,366 kleiner.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Fuer V0 <= 2 und Q >= 150 gibt es keine Bindung gegen E_frei (QM2 nicht eingetroffen) | 70 % |
| A2 | V0 = 0: Der Ball am Monopol wandert entlang +z vom Monopol weg (z_c waechst oder Ball am Kastenrand); E_mono > E_frei an allen Q | 80 % |
| A3 | QM0 eingetroffen, Abweichung auf dem Hauptgitter <= 3e-4 relativ | 85 % |
| A4 | Fuer jedes V0 waechst E_mono(Q) - E_frei(Q) mit Q (bester Start), ueber das Raster monoton | 60 % |
| A5 | QM4: Verhaeltnis D(0)/D(pi/2) beim kleinsten Q (V0 = 2) in [1,8; 2,2] | 30 % |
| A6 | J_z + Q/2 = 0 bis auf <= 1e-9 relativ in allen Zustaenden (Codeprobe, vorab ableitbar) | 97 % |
| A7 | Topf ohne Monopol bindet bei V0 = 2 und Q = 200 um mehr als 5 (E_frei - E_topf > 5) | 75 % |
