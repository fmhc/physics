# Tetraederketten – Schnitte und Schnittpunkte

## Exakte Zählregel für generische Schnitte

Für eine face-sharing Tetraederkette und eine Ebene, die keine Knoten exakt trifft:

`P = T3 + 2*T4 + 2*C`

- `P`: eindeutige Schnittpunkte der Ebene mit den Kanten
- `T3`: Zahl geschnittener Tetraeder mit dreieckigem Schnitt
- `T4`: Zahl geschnittener Tetraeder mit viereckigem Schnitt
- `C`: Zahl getrennter Schnittinseln

Begründung: lokale Schnittpolygone liefern 3 bzw. 4 Punkte; jede gemeinsame geschnittene Innenfläche benachbarter Tetraeder identifiziert zwei davon. Bei S=T3+T4 geschnittenen Tetraedern und C Komponenten gibt es S-C solche Nachbarschaften.

## Zusammenfassung

| Modell   |   Tetraeder |   Kanten |   P_min |   P_median |   P_mittel |   P_max |   Wahrscheinlichkeit_mehrere_Schnittinseln |   Anzahl_diskreter_P_Zustaende |
|:---------|------------:|---------:|--------:|-----------:|-----------:|--------:|-------------------------------------------:|-------------------------------:|
| 11+1     |           9 |       30 |       6 |         10 |    10.2044 |      16 |                                    0.00099 |                              9 |
| 19+1     |          17 |       54 |       6 |         10 |    12.6335 |      28 |                                    0.01217 |                             16 |

## Repräsentative Schnitte

| Modell   | Schnitt     |   P |   T3 |   T4 |   Komponenten_C |   geschnittene_Tetraeder |         nx |         ny |         nz |
|:---------|:------------|----:|-----:|-----:|----------------:|-------------------------:|-----------:|-----------:|-----------:|
| 11+1     | minimal     |   6 |    2 |    1 |               1 |                        3 |  0.543613  |  0.835654  |  0.0785347 |
| 11+1     | maximal     |  16 |    4 |    5 |               1 |                        9 | -0.0978267 | -0.184077  | -0.978032  |
| 11+1     | zwei Inseln |  14 |    6 |    2 |               2 |                        8 |  0.53641   | -0.57594   | -0.616893  |
| 19+1     | minimal     |   6 |    2 |    1 |               1 |                        3 |  0.995264  |  0.0590074 | -0.0772477 |
| 19+1     | maximal     |  28 |    8 |    9 |               1 |                       17 | -0.370387  |  0.583021  |  0.723118  |
| 19+1     | zwei Inseln |  24 |   12 |    4 |               2 |                       16 |  0.374415  | -0.41621   |  0.828603  |

## Tick-Definition

Ein geometrischer Vertex-Tick tritt auf, wenn die rotierende Schnittebene einen Knoten passiert. Nicht jeder Vertex-Tick ändert P. Die Tabellen `slice_tick_events.csv` unterscheiden daher Identitäts-Ticks von echten Anzahl-Ticks (`Delta_P != 0`).
