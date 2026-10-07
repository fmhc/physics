# ZELLE600-1, Nachtrag 120-Zelle: Erwartung vor der Rechnung

- **Auftrag:** Zusatz der Leitung (Nachricht 06:39, optional): 120-Zelle aus den Tetraedermitten bauen, Spektrum
  600 x 600 auf der .69, Vielfachheiten gegen 1, 4, 9, 16, ... und die Frage: Haengt das Wasserstoff-Muster an der
  Zahl der Kanten je Knoten?
- **Geschrieben ab 2026-10-05 06:40:03 CEST (date), vor jeder Rechnung zur 120-Zelle.** Karte, Z0 bis Z4 unveraendert.
- Kennzeichen: [M] eigene Schreibtischrechnung, nicht geprueft; [L] Literatur aus dem Gedaechtnis.

## Schreibtisch [M]

- **Bau:** Ecken = normierte Mitten der 600 Tetraeder, Kanten = Tetraederpaare mit gemeinsamem Dreieck.
  1200 Dreiecke liegen in je 2 Tetraedern, also 1200 Kanten und Grad 4.
  Kantenwinkel: cos theta = 1 - 1/(4 phi^4) = 0,96353, theta = 15,52 Grad, Sehne 1/(sqrt2 phi^2) = 0,2701.
- **Symmetrie:**
  - Gleiche Drehgruppe G = (2I x 2I)/{+-1} (Ordnung 7200), Stabilisator einer Ecke = Tetraedergruppe T (Ordnung 12).
  - Die Kugelfunktionen vom Grad k bilden fuer k <= 5 eine irreduzible G-Darstellung der Dimension (k+1)^2.
  - Wie oft sie in den 600 Funktionen vorkommt, zaehlen die T-invarianten Anteile:
    m_k = Summe_{l<=k} h_l mit h_l = 1, 0, 0, 1, 1, 0, 2, ... (Molien-Reihe von T).
    Also m_k = 1, 1, 1, 2, 3, 3 fuer k = 0 bis 5.
- **Folgen:**
  - k = 0, 1, 2 (m = 1): Die Kugelfunktionen sind exakt Eigenvektoren, lambda_A = 4 sin((k+1) theta) / ((k+1) sin theta).
    Laplace-Werte 0, 1/phi^4 = 0,14590, 1/phi^2 = 0,38197; Vielfachheiten 1, 4, 9.
  - k = 3, 4, 5 (m = 2, 3, 3): Es gibt je m Niveaus mit Vielfachheit 16, 25, 36. Die Eigenvektoren mischen die
    Kugelfunktion mit den weiteren Kopien. Das unterste Niveau jeder Art liegt nahe am Kontinuum
    4 (1 - sin((k+1) theta)/((k+1) sin theta)); die weiteren Kopien erwarte ich viel hoeher (Gittermoden).
  - k = 6: 49 zerfaellt unter G in 9 + 12 + 12 + 16 (V_3 auf 2I = 3' + 4). Ein 49-faches Niveau ist durch die
    Symmetrie nicht erzwungen.
  - Kontinuum: lambda_k / lambda_1 bei k = 2 genau phi^2 = 2,618 gegen 8/3 = 2,667 (-1,8 %). Bei k = 3 schaetze ich
    mit der zonalen Funktion etwa 4,8 gegen 5 (-4 %).

## Vorhersagen (vor der Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| N1 | Kontrolle [M, vorab ableitbar]: 600 Ecken auf S^3, 1200 Kanten, Grad 4, alle Kanten gleich lang (15,52 Grad) | 97 % |
| N2 | [M] Die sechs untersten Laplace-Niveaus haben die Vielfachheiten 1, 4, 9, 16, 25, 36 | 70 % |
| N3 | [M, vorab ableitbar] Laplace-Niveau 1 und 2 exakt 1/phi^4 = 0,14590 und 1/phi^2 = 0,38197 | 90 % |
| N4 | [M] Kein 49-faches Niveau. Die Kugelfunktionen vom Grad 6 verteilen sich auf Niveaus mit 9, 12, 12, 16 (oder einer Teilmenge davon) | 80 % |
| N5 | [M] lambda_k / lambda_1 fuer k = 2 und 3 liegt innerhalb von 10 % bei k(k+2)/3 (bei der 600-Zelle war k = 3 um -21,5 % daneben) | 80 % |
| N6 | [M] Ab k = 3 sind die untersten Niveaus nicht mehr exakt die Kugelfunktionen (Beimischung der zweiten Kopie), aber ueberwiegend: Anteil der Grad-k-Funktionen im untersten passenden Niveau ueber 90 % | 60 % |

## Antwort auf die Frage, vorab [M]

- Die exakten Entartungen haengen an der Symmetriegruppe H4, nicht an der Kantenzahl. Beide Zellen haben dieselbe
  Gruppe. Also gilt in beiden das exakte n^2 hoechstens bis n = 6.
- Die Kantenzahl (12 gegen 4, also feineres Netz mit 600 Ecken) entscheidet zweierlei:
  - wie gut die Abstaende dem Kontinuum k(k+2) folgen;
  - ob die Niveaus in der Wasserstoff-Reihenfolge bleiben.
- Bei der 600-Zelle bricht es nach n = 6 hart ab (120 = 91 + 29). Bei der 120-Zelle erwarte ich nach n = 6 einen
  aufgespaltenen Haufen nahe dem Kontinuum: ungefaehr Wasserstoff, aber nicht exakt.
- Alles ist Darstellungstheorie und vorab ableitbar, also keine Messung.
