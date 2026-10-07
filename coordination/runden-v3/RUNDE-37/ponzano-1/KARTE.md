# PONZANO-1: Steckt Regges Wirkung schon in Drehimpulsen auf Tetraederkanten? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 02:27:20 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - In Finns Netzbild sind Striche Laengen. Regges Wirkung (Flaeche bzw. Laenge mal Fehlwinkel) gibt Einsteins
    Schwerkraft (REGGE-RAND-1, REGGE-4D-1). Sie war bisher aber eingegeben, nicht hergeleitet.
  - Die Regel (REGEL.md, Abschnitt 8) heisst: Umbenennen ist frei.
  - Ponzano und Regge (1968) [L]: Belegt man die sechs Kanten eines Tetraeders mit Drehimpulsen j, hat das 6j-Symbol der
    Quantenmechanik fuer grosse j die Form (1/sqrt(12 pi V)) cos(sum_e (j_e + 1/2) theta_e + pi/4).
    - theta_e sind die Aussenwinkel und V das Volumen des Tetraeders mit den Kantenlaengen j_e + 1/2.
    - In der Phase steht Regges Wirkung. Bewiesen von Roberts 1999 [L].
  - Biedenharn-Elliott-Identitaet [L]: zwei Tetraeder = drei Tetraeder (Pachner-Zug 2-3) gilt exakt. Das ist die
    Umbenennungsfreiheit in 3D, als Identitaet der Drehimpulsalgebra.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- **Ehrlich vorab:** Die Hauptaussagen sind bekannte Mathematik [L], also vorab ableitbar. Die Karte ist eine
  Vorfuehrung fuer Finns Bild. Scheitern koennen nur die Zahlen der Umsetzung und der Hypothesenpunkt PO3.

## Schreibtisch (vor jeder Rechnung)

- **6j-Symbol** exakt ueber die Racah-Formel (ganze Zahlen bzw. Brueche, oder mpmath mit vielen Stellen).
  - Zulaessig sind Tripel mit Dreiecksungleichung und ganzzahliger Summe.
- **Form:** eine feste, unsymmetrische Tetraederform b_e (ganze Zahlen), j_e = lambda b_e mit lambda = 1 bis 200. Die
  Laengen fuer die Formel sind l_e = j_e + 1/2.
- **Nicht geometrische Wahl:** Spins, die die Dreiecksbedingungen erfuellen, aber zu keinem echten Tetraeder gehoeren
  (Cayley-Menger-Determinante negativ). Dort sollte das 6j-Symbol exponentiell klein werden (klassisch verbotener
  Bereich) [L].
- **Pachner-Zug 2-3:** Die Summe ueber die innere Kante x, sum_x (2x+1) {..}{..}{..}, ist gleich dem Produkt zweier 6j
  (Biedenharn-Elliott).
  - [H] Den Hauptbeitrag sollte die Summe dort sammeln, wo die drei Tetraeder flach um die innere Kante schliessen
    (Fehlwinkel 0). Das ist Regges Bewegungsgleichung, hier aus der Interferenz der Phasen.

## Test (Code-Agent)

- **PO0, Kontrollen:**
  - Orthogonalitaet sum_x (2x+1)(2f+1){a b x; c d f}{a b x; c d f'} = delta_ff'
  - Biedenharn-Elliott an 20 zufaelligen zulaessigen Spinsaetzen
  - Symmetrien des 6j-Symbols (24 Tetraedersymmetrien)
  - Vergleich mit einer unabhaengigen Bibliothek (z. B. sympy.physics.wigner.wigner_6j) fuer kleine j
- **PO1, Ponzano-Regge:**
  - Relativer Fehler e(lambda) = abs(6j - PR)/(1/sqrt(12 pi V)) fuer lambda = 5, 10, 20, 50, 100, 200, an zwei Formen.
  - Dazu die Phase: Lage der Nullstellen des 6j in einer Spinfolge gegen die Nullstellen des Kosinus.
- **PO2:** ln abs(6j) gegen lambda fuer eine nicht geometrische Wahl.
- **PO3:** Summand des 2-3-Zugs gegen x. Bestimmen:
  - Wo liegt sein Schwerpunkt bzw. die stationaere Phase?
  - Welcher Laenge der inneren Kante entspricht der flache Schluss der drei Tetraeder (aus der Geometrie der zwei
    Tetraeder)?

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PO0 | Orthogonalitaet, Biedenharn-Elliott und Symmetrien exakt (rational) bzw. auf 1e-30 (mpmath); Abgleich mit der Fremdbibliothek exakt | 90 % |
| PO1 | e(lambda) faellt wie 1/lambda (Steigung in log-log zwischen -1,3 und -0,7); bei lambda = 100 ist e < 0,02 an beiden Formen | 70 % |
| PO2 | Nicht geometrisch: ln abs(6j) sinkt linear in lambda (R^2 > 0,99 ueber lambda = 20 bis 200) | 70 % |
| PO3 | [H] Die Summe des 2-3-Zugs sammelt ihr Gewicht bei der flachen Laenge x*: Der gewichtete Schwerpunkt der Summanden (nach Betrag) liegt innerhalb +-10 % von x* bei lambda >= 50 | 45 % |

**Bedeutung (vorab):**
- PO1 trifft ein: In Finns Bild, Striche als Drehimpulse, steckt Regges Wirkung schon in der Quantenmechanik eines
  einzelnen Tetraeders. Einsteins Wirkung (in 3D) muss also nicht eingegeben werden; sie ist der klassische Grenzfall der
  Kopplung von Drehimpulsen [L].
- PO0 (Biedenharn-Elliott) zeigt die Regel "Umbenennen ist frei" in 3D exakt, als Identitaet.
- PO3 trifft ein: Die Bewegungsgleichung (flacher Schluss) folgt aus Interferenz. Bleibt sie aus, ist das 2-3-Gewicht
  nicht geometrisch lokalisiert, und die einfache Lesart gilt nur fuer die Phase, nicht fuer das Gewicht.
- Grenze: Das ist 3D-Schwerkraft ohne Wellen. In 4D gilt Aehnliches nur naeherungsweise (Spinschaum-Modelle) [L].

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
