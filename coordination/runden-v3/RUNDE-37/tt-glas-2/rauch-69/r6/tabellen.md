# TT-GLAS-2: Tabellen (mechanisch aus auswertung.json; Punkt als Dezimalzeichen)

## Laeufe (aus den kleintest-Logs, UTC)

| Lauf | Spur | Start | Ende | Dauer s | rc |
|---|---|---|---|---|---|
| tg2-bz128-s1 | cpu6 | 05:21:20 | 05:24:01 | 161 | 0 |
| tg2-bz128-s2 | cpu6 | 05:24:01 | 05:26:46 | 165 | 0 |
| tg2-bz128-s3 | cpu6 | 05:26:46 | 05:29:37 | 171 | 0 |
| tg2-bz128-s4 | cpu6 | 05:29:37 | 05:32:10 | 153 | 0 |
| tg2-bz128-s5 | cpu6 | 05:32:10 | 05:34:55 | 165 | 0 |
| tg2-bz128-s6 | cpu6 | 05:34:55 | 05:37:29 | 154 | 0 |
| tg2-bz128-s7 | cpu6 | 05:37:29 | 05:39:59 | 150 | 0 |
| tg2-bz128-s8 | cpu6 | 05:39:59 |  | - | None |
| tg2-bz256-s1 | p4000a | 05:21:17 | 05:23:51 | 154 | 0 |
| tg2-bz256-s10 | p4000b | 05:29:20 | 05:32:19 | 179 | 0 |
| tg2-bz256-s11 | p4000b | 05:32:19 | 05:34:55 | 156 | 0 |
| tg2-bz256-s12 | p4000b | 05:34:55 | 05:37:32 | 157 | 0 |
| tg2-bz256-s2 | p4000a | 05:23:51 | 05:26:29 | 158 | 0 |
| tg2-bz256-s3 | p4000a | 05:26:29 | 05:29:03 | 154 | 0 |
| tg2-bz256-s4 | p4000a | 05:29:03 | 05:32:14 | 191 | 0 |
| tg2-bz256-s5 | p4000a | 05:32:14 | 05:35:05 | 171 | 0 |
| tg2-bz256-s6 | p4000a | 05:35:05 | 05:37:59 | 174 | 0 |
| tg2-bz256-s7 | p4000b | 05:21:18 | 05:23:52 | 154 | 0 |
| tg2-bz256-s8 | p4000b | 05:23:52 | 05:26:28 | 156 | 0 |
| tg2-bz256-s9 | p4000b | 05:26:28 | 05:29:20 | 172 | 0 |
| tg2-dk256-A | p4000a | 05:37:59 |  | - | None |
| tg2-dk256-B | p4000b | 05:37:32 |  | - | None |

## Stabilitaet je Netz (Aufgabe 1)

| N | Saat | Klassen | vollst. | wachsend | Null bei Gamma | Null sonst | min omega^2 (ohne Gamma) | bei m | min omega^2 / s | A_red pd (ohne Gamma) | B_red neg max | Geraet | Laufzeit s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 128 | 1 | 112 | ja | 0 | [6] | 0 | 0.2008 | [1, 0, 0] | 0.000275 | ja | 0 | cpu | 158 |
| 128 | 2 | 112 | ja | 0 | [6] | 0 | 0.2004 | [0, 1, 0] | 0.000124 | ja | 0 | cpu | 161 |
| 128 | 3 | 112 | ja | 0 | [6] | 0 | 0.1841 | [1, 0, 0] | 0.000306 | ja | 0 | cpu | 165 |
| 128 | 4 | 112 | ja | 0 | [6] | 0 | 0.2005 | [0, 1, 0] | 0.000339 | ja | 0 | cpu | 150 |
| 128 | 5 | 112 | ja | 0 | [6] | 0 | 0.1991 | [0, 1, 0] | 9.29e-05 | ja | 0 | cpu | 161 |
| 128 | 6 | 112 | ja | 0 | [6] | 0 | 0.203 | [0, 0, 1] | 0.000373 | ja | 0 | cpu | 150 |
| 128 | 7 | 112 | ja | 0 | [6] | 0 | 0.2055 | [0, 1, 0] | 0.000459 | ja | 0 | cpu | 147 |
| 256 | 1 | 112 | ja | 0 | [6] | 0 | 0.1282 | [0, 0, 1] | 0.000175 | ja | 0 | cuda | 151 |
| 256 | 2 | 112 | ja | 0 | [6] | 0 | 0.1305 | [0, 0, 1] | 1.51e-05 | ja | 0 | cuda | 154 |
| 256 | 3 | 112 | ja | 0 | [6] | 0 | 0.1288 | [1, 0, 0] | 6.5e-05 | ja | 0 | cuda | 151 |
| 256 | 4 | 112 | ja | 0 | [6] | 0 | 0.126 | [0, 0, 1] | 8.85e-05 | ja | 0 | cuda | 187 |
| 256 | 5 | 112 | ja | 0 | [6] | 0 | 0.1231 | [1, 0, 0] | 7.61e-05 | ja | 0 | cuda | 168 |
| 256 | 6 | 112 | ja | 0 | [6] | 0 | 0.1272 | [0, 1, 0] | 9.22e-05 | ja | 0 | cuda | 171 |
| 256 | 7 | 112 | ja | 0 | [6] | 0 | 0.1272 | [0, 1, 0] | 2.8e-05 | ja | 0 | cuda | 150 |
| 256 | 8 | 112 | ja | 0 | [6] | 0 | 0.1239 | [0, 1, 0] | 6.71e-05 | ja | 0 | cuda | 153 |
| 256 | 9 | 112 | ja | 0 | [6] | 0 | 0.1244 | [0, 1, 0] | 0.00011 | ja | 0 | cuda | 168 |
| 256 | 10 | 112 | ja | 0 | [6] | 0 | 0.1237 | [0, 1, 0] | 0.000182 | ja | 0 | cuda | 175 |
| 256 | 11 | 112 | ja | 0 | [6] | 0 | 0.1258 | [0, 0, 1] | 0.000133 | ja | 0 | cuda | 153 |
| 256 | 12 | 112 | ja | 0 | [6] | 0 | 0.1313 | [0, 0, 1] | 0.000303 | ja | 0 | cuda | 154 |

## Zerlegung je Netz (Aufgabe 2; Spannen in Prozent)

| N | Saat | (a) voll | (b) affin, nur Masse | (c) Ersatzmasse, Relaxation | (d) Kontrolle zu c | (e) unprojiziert | Anteil c/(b+c) | (a) regulaer | (c) gueltig | (c) neg. omega^2 max | Projektionsanteil max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 256 | 1 | 12.31 | 12.31 | 5.23 | 5.23 | 0.00 | 0.298 | ja | ja | 0 | 0.503 |
| 256 | 2 | 10.67 | 10.67 | 5.98 | 5.98 | 0.00 | 0.359 | ja | ja | 1 | 0.532 |
| 256 | 3 | 11.91 | 11.91 | 3.46 | 3.46 | 0.00 | 0.225 | ja | ja | 1 | 0.486 |
| 256 | 7 | 6.91 | 6.91 | 7.72 | 7.72 | 0.00 | 0.528 | ja | ja | 2 | 0.492 |
| 256 | 8 | 12.84 | 12.84 | 6.09 | 6.09 | 0.00 | 0.322 | ja | ja | 0 | 0.485 |
| 256 | 9 | 11.54 | 11.54 | 5.09 | 5.09 | 0.00 | 0.306 | ja | ja | 0 | 0.492 |
| 256 | 10 | 12.29 | 12.29 | 7.19 | 7.19 | 0.00 | 0.369 | ja | ja | 0 | 0.487 |
| 256 | 11 | 14.56 | 14.56 | 6.65 | 6.65 | 0.00 | 0.313 | ja | ja | 0 | 0.487 |

## Mittel je N (Spanne, Aufspaltung, Doppelbrechungsanteil; Mittel +- SD, Prozent bzw. Anteil)

| N | Variante | Netze | Spanne % | Aufspaltung max % | Richtungsspanne % | Doppelbrechungsanteil | omega^2/k^2 Mittel |
|---|---|---|---|---|---|---|---|
| 256 | a | 8 | 11.63 +- 2.21 | 10.44 +- 2.65 | 3.79 +- 0.86 | 0.885 +- 0.087 | 4.8964 |
| 256 | b | 8 | 11.63 +- 2.21 | 10.44 +- 2.65 | 3.79 +- 0.86 | 0.885 +- 0.086 | 4.8964 |
| 256 | c | 8 | 5.93 +- 1.34 | 5.23 +- 1.72 | 1.99 +- 0.69 | 0.867 +- 0.13 | 0.1201 |
| 256 | d | 8 | 5.93 +- 1.34 | 5.23 +- 1.72 | 1.99 +- 0.69 | 0.867 +- 0.13 | 0.1201 |
| 256 | e | 8 | 0.00 +- 0.00 | 0.00 +- 0.00 | 0.00 +- 0.00 | 0.87 +- 0.095 | 0.14794 |

## Urteile

- TG2-0: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-1: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-2: nach Plan nicht entscheidbar; nach Kartenwortlaut verfehlt
- TG2-3: nach Plan nicht entscheidbar (weniger als 4 Netze); nach Kartenwortlaut nicht entscheidbar (weniger als 4 Netze)
