# TT-GLAS-2: Tabellen (mechanisch aus auswertung.json; Punkt als Dezimalzeichen)

## Stabilitaet je Netz (Aufgabe 1)

| N | Saat | Klassen | vollst. | wachsend | Null bei Gamma | Null sonst | min omega^2 (ohne Gamma) | bei m | min omega^2 / s | A_red pd (ohne Gamma) | B_red neg max | Geraet | Laufzeit s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 128 | 1 | 112 | ja | 0 | [6] | 0 | 0.2008 | [1, 0, 0] | 0.000275 | ja | 0 | cpu | 158 |
| 128 | 2 | 112 | ja | 0 | [6] | 0 | 0.2004 | [0, 1, 0] | 0.000124 | ja | 0 | cpu | 161 |
| 256 | 1 | 112 | ja | 0 | [6] | 0 | 0.1282 | [0, 0, 1] | 0.000175 | ja | 0 | cuda | 151 |
| 256 | 2 | 112 | ja | 0 | [6] | 0 | 0.1305 | [0, 0, 1] | 1.51e-05 | ja | 0 | cuda | 154 |
| 256 | 7 | 112 | ja | 0 | [6] | 0 | 0.1272 | [0, 1, 0] | 2.8e-05 | ja | 0 | cuda | 150 |
| 256 | 8 | 112 | ja | 0 | [6] | 0 | 0.1239 | [0, 1, 0] | 6.71e-05 | ja | 0 | cuda | 153 |

## Zerlegung je Netz (Aufgabe 2; Spannen in Prozent)

| N | Saat | (a) voll | (b) affin, nur Masse | (c) Ersatzmasse, Relaxation | (d) Kontrolle zu c | (e) unprojiziert | Anteil c/(b+c) | (a) regulaer | (c) gueltig | (c) neg. omega^2 max | Projektionsanteil max |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Mittel je N (Spanne, Aufspaltung, Doppelbrechungsanteil; Mittel +- SD, Prozent bzw. Anteil)

| N | Variante | Netze | Spanne % | Aufspaltung max % | Richtungsspanne % | Doppelbrechungsanteil | omega^2/k^2 Mittel |
|---|---|---|---|---|---|---|---|

## Urteile

- TG2-0: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-1: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-2: nach Plan nicht entscheidbar; nach Kartenwortlaut nicht entscheidbar
- TG2-3: nach Plan nicht entscheidbar (weniger als 4 Netze); nach Kartenwortlaut nicht entscheidbar (weniger als 4 Netze)
