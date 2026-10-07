# DIM-BEUTEL: Kann ein Beutel die Dimension messen? (Runde 16)

- Leitung: claude-primary. Karte, Schreibtischrechnung und Vorhersagen geschrieben ab 2026-10-02 09:47:42 CEST (date),
  vor jeder Rechnung.
- Anlass: Finn, 02.10.: "können wir daraus dimensionen ableiten? können wir daraus 3/4 bzw 4/3 flipping ableiten?"
- Ausgangspunkt BEUTEL-1 (M3): E ~ Q^p mit gemessenem p = 0,7503 bei freiem, masselosem Inhalt in einer Huelle.
- Explorativ (v3), Hypothesen [H], Literatur aus dem Gedaechtnis [L?].

## Schreibtisch der Leitung [ES]

- **Beutel in d Raumdimensionen** mit masselosem Inhalt (Dispersion omega ~ k^z, relativistisch z = 1):
  - Energie E = Q omega + B Vol, mit omega ~ R^(-z) und Vol ~ R^d.
  - Minimiert ueber R: E ~ Q^p mit p = d/(d + z), Huellenanteil h = B Vol / E = z/(d + z).
  - Bei z = 1: p = d/(d + 1), also 1/2, 2/3, 3/4 fuer d = 1, 2, 3, und h = 1/(d + 1).
  - Umgekehrt gilt Q ~ E^((d+1)/d), also **4/3 in 3D**. Das ist dieselbe Zahl wie beim Strahlungsgas: Bei masselosen
    Quanten in 3D ist E ~ S^(4/3) [L?].
  - **"3/4 und 4/3" sind also Kehrwerte desselben Gesetzes. Die 4 darin ist d + z = Raumdimensionen + 1, weil
    masselose Quanten omega ~ k haben (Lichtkegel).**
  - Mit Masse (Tropfen, wie M1/M2) gilt E ~ Q, also p = 1.
- **Auf einem Graphen** (Fraktal) mit Volumen ~ R^(d_H) und tiefstem Laplace-Eigenwert ~ R^(-d_w):
  - Es gilt d_w = 2 d_H/d_s [L?]; d_s ist die spektrale, d_H die Hausdorff-Dimension.
  - Fuer die Wellengleichung (omega^2 = Laplace-Eigenwert) ist omega ~ R^(-d_w/2).
  - Daraus folgt p = d_H/(d_H + d_w/2) = **d_s/(d_s + 1)**.
  - **Der Beutelexponent misst also die spektrale Dimension, nicht die Hausdorff-Dimension:** d_s = p/(1 - p) [H].
  - Gemessen in 3D (BEUTEL-1): p = 0,7503 ergibt d_s = 3,005; der Huellenanteil 0,2497 ergibt d = 1/h - 1 = 3,005.
- **Unterscheidungspunkt:** Sierpinski-Dreieck (Gasket) mit d_s = 2 ln3/ln5 = 1,3652 und d_H = ln3/ln2 = 1,5850 [L?].
  - Vorhersage p = 0,5772, falls d_s zaehlt.
  - Vorhersage p = 0,6131, falls d_H zaehlt.
  - Die Differenz ist 0,036.

## Rechnung

- Diskretes FLS-artiges Zweifeldmodell wie BEUTEL-1 M3, auf Graphen:
  - Energiefunktional: E = Q^2/(4 Sum phi_i^2) + Sum_<ij> [(phi_i - phi_j)^2 + (1/2)(chi_i - chi_j)^2]
    + Sum_i [(1/4)(chi_i^2 - 1)^2 + 2 chi_i^2 phi_i^2].
  - Das ist die Energie bei fester Ladung Q mit psi = phi e^{i omega t}, omega = Q/(2 Sum phi^2).
  - Minimum bei festem Q, z. B. per Gradientenfluss oder L-BFGS.
  - Randknoten: chi = 1 festhalten bzw. weit genug weg.
- **Graphen:**
  - G1: Kette (d = 1)
  - G2: Quadratgitter (d = 2)
  - G3: kubisches Gitter (d = 3)
  - G4: Sierpinski-Dreieck, Generation >= 7
  - Gitterabstand 1. Der Beutel muss gross gegen den Gitterabstand und klein gegen den Graphen sein; das ist zu pruefen
    und zu berichten.
- **Messung:**
  - E(Q) ueber mindestens eine Dekade in Q im Beutelbereich.
  - Lokaler Exponent p(Q) und Plateauwert, dazu Huellenanteil h(Q) und geschaetzte Dimension p/(1 - p) bzw. 1/h - 1.
  - Startknoten beim Sierpinski-Dreieck: eine Ecke hoher Generation im Inneren (Wahl begruenden, zweite Wahl als
    Kontrolle).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| D1 | Kette: p -> 0,50 +- 0,02, h -> 0,50 +- 0,03 | 85 % |
| D2 | Quadratgitter: p -> 0,667 +- 0,02, h -> 0,333 +- 0,03 | 80 % |
| D3 | Kubisches Gitter: p -> 0,75 +- 0,02, h -> 0,25 +- 0,03 (bestaetigt BEUTEL-1 diskret) | 75 % |
| D4 | Sierpinski-Dreieck: p liegt naeher an 0,577 (d_s) als an 0,613 (d_H) | 70 % |
| D5 | Ausserhalb des Beutelbereichs (kleines Q, Gitterskala) weicht p deutlich ab; der Plateaubereich ist in 3D am kuerzesten | 70 % |

**Bedeutung fuer Finns Frage (vorab):**
- Treffen D1 bis D3 ein, misst der Exponent die Dimension. 3/4 bzw. 4/3 sind dann die Unterschrift von "3
  Raumdimensionen + masseloser Inhalt".
- Trifft D4 ein, misst er die spektrale Dimension. Dann taugt er als Dimensionsmesser auch fuer Graphen ohne
  vorgegebene Dimension, also fuer entstehende Geometrie. Das ist ein moeglicher Baustein fuer "Dimension ableiten"
  [H], kein Beweis.
- Herleiten, warum es 3 Dimensionen sind, kann diese Rechnung nicht. Die Dimension steckt im Graphen.

## Rahmen

- Code-Agent, eigener Code (numpy/scipy, duenne Matrizen). Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und
  cpu2, je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 90 min.
