# FRUST-3D: Was kostet die 7,36-Grad-Luecke? Fuenf Knicklicht-Tetraeder um eine Kante (Runde 27)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 05:15:08 CEST (date), vor jeder Rechnung.
- Herkunft: Finn ~05:12 "Check die Geometrie Sachen aus x dimensionalen Sachen"; RUNDE-27/GEOMETRIE-XD.md, Test 1.
- **Schreibtisch [M]:**
  - Eine pentagonale Bipyramide aus 16 gleichen Staeben (7 Ecken: Achse A-B, Ring r_0 bis r_4; Staebe: Achse 1, Speichen
    10, Ring 5) ist ein Haufen aus 5 Tetraedern um die Kante AB.
  - Mit Ring und Speichen der Laenge 1 muesste die Achse 2 sqrt(1 - 1/(4 sin^2 36 Grad)) = 1,0515 lang sein. Das ist der
    Fehlpass der 7,36-Grad-Luecke.
  - Als Stabwerk mit Gelenken: 3V - 6 = 15 < 16 Staebe, also ein ueberzaehliger Stab und genau eine Eigenspannung.
- Projekt-grep (fuenfte Probe): RUNDE-17/quellen-frustration (Literatur, 5 Tetraeder lassen 7,36 Grad) [S].
  - Ein Stabmodell des Fehlpasses ist im Projekt nicht gerechnet.

## Test (Code-Agent)

- **Stabmodell wie TETRA-STAB/TETRA-KETTE** (RUNDE-26/tetra-kette/code/tetra_kette.py, gebuendelt): von Natur aus gerade
  Staebe, B = 1, L = 1, Ks = 25600 (Knicklicht), N Segmente, keine Torsion.
- **Zwei Lagerungen:**
  - (G) Gelenke: Die Verbinder halten nur die Lage, Staebe frei drehbar, keine Einspannung.
  - (E) Einspannung: Die Verbinder halten die Richtungen der geraden Kanten wie im regulaeren Fall; die Verbinder sind frei
    drehbar als starre Koerper.
- **Bezug:**
  - Alle Ruhelaengen 1, Einspannrichtungen aus der "Wunschgeometrie" (regulaere Tetraeder je Paar).
  - Der Fehlpass wird vom Gleichgewicht verteilt.
- **Gemessen:**
  - Axialkraft je Stabart (Achse, Speichen, Ring)
  - Biegemomente an den Ecken
  - Durchbiegung (Stich) je Stab
  - gespeicherte Energie und Anteile Dehnung/Biegung
  - Endabstaende: Achse, Ringradius
- Kontrolle: Derselbe Code mit 4 Tetraedern um eine Kante (Luecke 77,9 Grad, also offen und ohne Zwang) und ein einzelnes
  Tetraeder sind spannungsfrei.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| F0 | Kontrolle: 1 Tetraeder und 4 um eine Kante (offen) spannungsfrei, |F| L und |tau| < 1e-8 | 90 % |
| F1 | (G) Gelenke: Die Achse steht unter Zug, Speichen und Ring unter Druck (Vorzeichenmuster der einen Eigenspannung) | 55 % |
| F2 | (G) Gelenke mit Knicklicht-Steifigkeit: Mindestens eine gedrueckte Stabart knickt aus (Stich > 1 % der Stablaenge), weil 5 % Fehlpass weit ueber der Euler-Last liegen | 65 % |
| F3 | (E) Einspannung: Die gespeicherte Energie liegt hoeher als bei (G); ueber 80 % davon ist Biegung | 55 % |

**Bedeutung (vorab):**
- F1 bis F3 treffen ein: Die 3D-Frustration gleicher Tetraeder wird in Staben nicht als Dehnung, sondern als Biegung und
  Ausknicken aufgenommen, mit Zug in der Achse [H].
  - Ein Raum aus Knicklicht-Tetraedern waere an jeder Fuenfer-Kante sichtbar verbogen.
- F1 trifft nicht ein: Das Vorzeichenmuster ist anders. Beschreiben, mit dem Eigenspannungsvektor.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min). Die Spur setzt seit heute 1 Thread
  fuer BLAS.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt (z. B. 4 Tetraeder), offenlegen.
- Zeitbox 75 min.
