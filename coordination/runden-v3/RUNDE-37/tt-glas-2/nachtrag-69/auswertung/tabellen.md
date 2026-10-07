# TT-GLAS-2: Tabellen (mechanisch aus auswertung.json; Punkt als Dezimalzeichen)

## Laeufe (aus den kleintest-Logs, UTC)

| Lauf | Spur | Start | Ende | Dauer s | rc |
|---|---|---|---|---|---|
| tg2-nt512-a | p4000a | 05:51:57 | 06:02:34 | 637 | 0 |
| tg2-nt512-b | p4000a | 06:02:34 | 06:13:21 | 647 | 0 |

## Stabilitaet je Netz (Aufgabe 1)

| N | Saat | Klassen | vollst. | wachsend | Null bei Gamma | Null sonst | min omega^2 (ohne Gamma) | bei m | min omega^2 / s | A_red pd (ohne Gamma) | B_red neg max | Geraet | Laufzeit s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Zerlegung je Netz (Aufgabe 2; Spannen in Prozent)

| N | Saat | (a) voll | (b) affin, nur Masse | (c) Ersatzmasse, Relaxation | (d) Kontrolle zu c | (e) unprojiziert | Anteil c/(b+c) | (a) regulaer | (c) gueltig | (c) neg. omega^2 max | Projektionsanteil max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 512 | 5 | 9.05 | 9.05 | 3.00 | 3.00 | 0.00 | 0.249 | ja | ja | 1 | 0.469 |
| 512 | 6 | 8.92 | 8.92 | 5.83 | 5.83 | 0.00 | 0.395 | ja | ja | 0 | 0.483 |
| 512 | 7 | unvollstaendig (ridx [0, 1, 2, 3, 4, 5]) | | | | | | | | | |
| 512 | 8 | 7.30 | 7.30 | 3.18 | 3.18 | 0.00 | 0.304 | ja | ja | 0 | 0.473 |
| 512 | 9 | 10.41 | 10.41 | 4.56 | 4.56 | 0.00 | 0.304 | ja | ja | 0 | 0.485 |
| 512 | 10 | unvollstaendig (ridx [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) | | | | | | | | | |

## Mittel je N (Spanne, Aufspaltung, Doppelbrechungsanteil; Mittel +- SD, Prozent bzw. Anteil)

| N | Variante | Netze | Spanne % | Aufspaltung max % | Richtungsspanne % | Doppelbrechungsanteil | omega^2/k^2 Mittel |
|---|---|---|---|---|---|---|---|
| 512 | a | 4 | 8.92 +- 1.27 | 7.98 +- 1.01 | 2.52 +- 0.62 | 0.898 +- 0.077 | 4.8584 |
| 512 | b | 4 | 8.92 +- 1.27 | 7.98 +- 1.01 | 2.52 +- 0.62 | 0.898 +- 0.077 | 4.8585 |
| 512 | c | 4 | 4.14 +- 1.32 | 3.46 +- 1.09 | 1.73 +- 0.87 | 0.838 +- 0.061 | 0.12124 |
| 512 | d | 4 | 4.14 +- 1.32 | 3.46 +- 1.09 | 1.73 +- 0.87 | 0.838 +- 0.061 | 0.12125 |
| 512 | e | 4 | 0.00 +- 0.00 | 0.00 +- 0.00 | 0.00 +- 0.00 | 0.753 +- 0.17 | 0.14856 |

## Urteile

- TG2-0: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-1: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-2: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-3: nach Plan nicht entscheidbar (weniger als 4 Netze); nach Kartenwortlaut nicht entscheidbar (weniger als 4 Netze)
