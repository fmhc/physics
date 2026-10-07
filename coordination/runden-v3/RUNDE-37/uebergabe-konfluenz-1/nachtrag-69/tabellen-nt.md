# UEBERGABE-KONFLUENZ-1: Tabellen aus auswertung-nt.json (synthetisch, keine Messdaten)

## Urteile (mechanisch, PLAN 7)

| Nr | nach Plan | nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|
| UK0 | nicht entscheidbar | nicht entscheidbar | D_faelle = 0; D_max_delta = -; faelle = 11; gleiche_endzerlegung = 11; teil_disjunkt = -; teil_kombinatorik = true |
| UK1 | verfehlt | verfehlt | median_T = 2.32e-17; median_K = -; max_T = 6.81e-17; max_K = -; n_T = 11; n_K = 0 |
| UK2 | nicht entscheidbar | eingetroffen | n_plan = 0; n_wortlaut = 10; median_steigung_plan = -; median_steigung_wortlaut = 1.04 |
| UK3 | nicht entscheidbar | eingetroffen | median_R = 2.32e-17; median_P = 0; verhaeltnis = - |
| UK4 | nicht entscheidbar | nicht entscheidbar | grund = Form B (A2L) nicht startbar; n_A_neg_A2L = [28, 28, 28, 31, 31, 33, 33, 33, 28, 28, 28] |

## Zuege und Kombinatorik je Art

| Art | Faelle | gleiche Endzerlegung | Status XY/YX | Zugzahl XY/YX | Typ X/Y | Verschiebung / l (Median) |
|---|---|---|---|---|---|---|
| D | 0 | 0 | {} | {} | {} | - |
| T | 11 | 11 | {"ok/ok": 11} | {"4/2": 5, "3/3": 5, "2/4": 1} | {"23/23": 11} | 0.022 |
| K | 0 | 0 | {} | {} | {} | - |

## Geometrie: Delta je Sektor (relativ), Median [Min, Max] ueber Faelle

| Art | Form | Lesart | n | Delta_q | Delta_p | Delta_H_geo | Zeitumkehr q (XY) | Zeitumkehr p (XY) | Zwangsrest XY (Summe) |
|---|---|---|---|---|---|---|---|---|---|
| T | A1 | R | 11 | 3.37e-15 [2.9e-15, 2.26e-14] | 7.34e-15 [6.08e-15, 1.63e-13] | 7.88e-16 [1.12e-16, 3.19e-15] | 3.79e-15 [3.29e-15, 4.51e-15] | 8.45e-15 [6.41e-15, 9.67e-15] | 0.0425 [0.0174, 0.0809] |
| T | A1 | P | 11 | 3.37e-15 [2.9e-15, 2.26e-14] | 3.62e-07 [1.31e-08, 3.68e-06] | 3.27e-09 [3.09e-10, 5.85e-08] | 3.79e-15 [3.29e-15, 4.51e-15] | 3.96e-15 [3.3e-15, 4.53e-15] | 0.0425 [0.0174, 0.0809] |
| T | A2 | R | 11 | 3.29e-15 [2.98e-15, 3.01e-14] | 8.4e-15 [5.74e-15, 1.5e-13] | 8.18e-16 [1.19e-16, 3.97e-15] | 3.82e-15 [3.12e-15, 4.73e-15] | 9.12e-15 [7.01e-15, 1.31e-14] | 0.0623 [0.0419, 0.0932] |
| T | A2 | P | 11 | 3.29e-15 [2.98e-15, 3.01e-14] | 5.33e-07 [1.26e-08, 1.68e-06] | 6.62e-09 [1.58e-10, 1.49e-07] | 3.82e-15 [3.12e-15, 4.73e-15] | 3.95e-15 [3.15e-15, 4.66e-15] | 0.0623 [0.0419, 0.0932] |

## Skalar: Delta je Sektor, Median [Min, Max] ueber Faelle

| Art | Lesart | Amplitude | n | Delta_phi rel | Delta_pi rel | Delta_phi abs | Delta_pi abs | Zeitumkehr phi / pi (XY, max) | Delta_H_phi (max) |
|---|---|---|---|---|---|---|---|---|---|
| T | R | 0.001 | 11 | 0 [0, 0] | 2.32e-17 [5.21e-18, 6.81e-17] | 0 [0, 0] | 2.48e-19 [5.59e-20, 7.51e-19] | 0 / 6.38e-17 | 0 |
| T | R | 0.01 | 11 | 0 [0, 0] | 2.4e-17 [0, 7.21e-17] | 0 [0, 0] | 2.6e-18 [0, 7.95e-18] | 0 / 5.06e-17 | 0 |
| T | P | 0.001 | 11 | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 / 0 | 0 |
| T | P | 0.01 | 11 | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 / 0 | 0 |

## Faelle (Lesart R und P, Formen A1 / A2; Skalar-Amplitude 1e-3)

| Saat | Art | X / Y | Typ X/Y | Zuege XY | Zuege YX | gleich | A1 R: Dq / Dp | A1 P: Dq / Dp | A2 R: Dq / Dp | A2 P: Dq / Dp | A2L startbar (neg.) | Skalar R / P: max(Dphi, Dpi) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | T | 548 / 843 | 23/23 | 23-23-23-32 | 23-23 | True | 3.11e-15 / 7.44e-15 | 3.11e-15 / 1.31e-08 | 3.09e-15 / 5.74e-15 | 3.09e-15 / 5.66e-08 | False (28) | 1.5e-17 / 0 |
| 1 | T | 1248 / 1250 | 23/23 | 23-23-23 | 23-23-23 | True | 3.43e-15 / 7.16e-15 | 3.43e-15 / 6.12e-07 | 3.34e-15 / 7.12e-15 | 3.34e-15 / 4.22e-07 | False (28) | 2.06e-17 / 0 |
| 1 | T | 11 / 20 | 23/23 | 23-23-23 | 23-23-23 | True | 3.14e-15 / 6.79e-15 | 3.14e-15 / 2.74e-07 | 2.98e-15 / 6.35e-15 | 2.98e-15 / 9.18e-08 | False (28) | 3e-17 / 0 |
| 2 | T | 955 / 1538 | 23/23 | 23-23 | 23-23-23-32 | True | 2.26e-14 / 1.63e-13 | 2.26e-14 / 7.08e-07 | 3.01e-14 / 5.08e-14 | 3.01e-14 / 1.68e-06 | False (31) | 6.81e-17 / 0 |
| 2 | T | 141 / 1090 | 23/23 | 23-23-23 | 23-23-23 | True | 5.1e-15 / 2.72e-14 | 5.1e-15 / 1.35e-06 | 3.92e-15 / 1.5e-13 | 3.92e-15 / 6.54e-07 | False (31) | 2.78e-17 / 0 |
| 3 | T | 537 / 557 | 23/23 | 23-23-23-32 | 23-23 | True | 3.42e-15 / 7.34e-15 | 3.42e-15 / 3.68e-06 | 3.25e-15 / 1.43e-14 | 3.25e-15 / 8.06e-07 | False (33) | 1.01e-17 / 0 |
| 3 | T | 587 / 648 | 23/23 | 23-23-23-32 | 23-23 | True | 2.9e-15 / 6.26e-15 | 2.9e-15 / 5.57e-08 | 3.29e-15 / 8.18e-15 | 3.29e-15 / 3.86e-08 | False (33) | 2.32e-17 / 0 |
| 3 | T | 207 / 1555 | 23/23 | 23-23-23 | 23-23-23 | True | 3.16e-15 / 7.06e-15 | 3.16e-15 / 3.93e-08 | 3.14e-15 / 9.58e-15 | 3.14e-15 / 5.33e-07 | False (33) | 5.21e-18 / 0 |
| 4 | T | 287 / 288 | 23/23 | 23-23-23-32 | 23-23 | True | 3.49e-15 / 1.41e-14 | 3.49e-15 / 3.62e-07 | 3.55e-15 / 8.4e-15 | 3.55e-15 / 6.02e-07 | False (28) | 3.64e-17 / 0 |
| 4 | T | 1235 / 1283 | 23/23 | 23-23-23-32 | 23-23 | True | 3.14e-15 / 6.08e-15 | 3.14e-15 / 3.71e-08 | 3.17e-15 / 6.46e-15 | 3.17e-15 / 1.26e-08 | False (28) | 1.15e-17 / 0 |
| 4 | T | 436 / 1519 | 23/23 | 23-23-23 | 23-23-23 | True | 3.37e-15 / 8.09e-15 | 3.37e-15 / 7.28e-07 | 3.31e-15 / 9.81e-15 | 3.31e-15 / 7.75e-07 | False (28) | 4.71e-17 / 0 |
