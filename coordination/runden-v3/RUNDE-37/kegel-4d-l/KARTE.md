# KEGEL-4D-L: Bezouts Satz und Keplers Optik der Kegelschnitte (Kreis, Ellipse, Parabel, Hyperbel) als Quelle fuer 4D-Ideen in Finns Programm (Runde 46, Finn-Auftrag, Ideation mit Literatur)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 06:06:11 CEST (date), vor jedem Abruf.
- **Finn (05.10., vor 06:05:35), woertlich:** "Bezouts Theorem und Keplers optics zu conic sections / circle, ellipse, parabola, hyperbola, nutze das für 4d ideen"
- **Projektsuche (alle Dateitypen):**
  - Bezout, Kegelschnitt, Paralipomena, Kustaanheimo, Runge-Lenz: 0 Treffer.
  - Fock nur in anderem Sinn (Fock-Raum).
  - Die 600-Zelle kommt nur als gekruemmte Schliessung der Tetraederpackung vor (7,36 Grad Luecke, RUNDE-17, -27, -34) [P].
  - Hopf-Abbildung: 4 Treffer (Q-Ball-Hopf) [P].
- Kennzeichen: [S], [S Abstract], [L], [L?], [M], [ES], [H], [P].

## Saatideen der Leitung (vorab, je mit Kennzeichen)

- **S1 [M, vorab gerechnet]: Keplers Stetigkeit ist ein Lorentz-Schub.**
  - Die Ebene t = a + v x schneidet den Lichtkegel t^2 = x^2 + y^2 in (1 - v^2) x^2 - 2 a v x + y^2 = a^2.
  - Fuer v < 1 ist das eine Ellipse mit Exzentrizitaet e = v, fuer v = 1 eine Parabel, fuer v > 1 eine Hyperbel.
  - Keplers Folge Kreis -> Ellipse -> Parabel -> Hyperbel ist also der Lichtkegel, von immer schneller bewegten Ebenen geschnitten. Die Parabel ist der Lichtschnitt.
  - In 4D: Der Lichtkegel t^2 = x^2 + y^2 + z^2, geschnitten mit Hyperebenen, gibt Rotationsellipsoide, Paraboloide und Hyperboloide.
- **S2 [L]: Fock 1935.** Die gebundenen Wasserstoffzustaende sind freie Bewegung auf der 3-Sphaere S^3 im 4D-Impulsraum (stereographisch); die Entartung n^2 kommt aus SO(4); dahinter steht der Runge-Lenz-Vektor. Gebunden heisst SO(4) (Ellipsen), ungebunden SO(3,1) (Hyperbeln). Bezug: Finns -13,6 eV-Frage.
- **S3 [L]: Kustaanheimo/Stiefel 1965.**
  - Das 3D-Kepler-Problem ist ein 4D-Oszillator mit einer U(1)-Bedingung, ueber die Hopf-Abbildung R^4 -> R^3.
  - In 2D bildet die Quadrierung z -> z^2 (Levi-Civita) zentrierte Oszillator-Ellipsen auf Kepler-Ellipsen mit Brennpunkt im Ursprung ab (Bohlin/Arnold-Dualitaet).
  - Die "verborgene" vierte Richtung ist eine Phase; Bezug zur inneren Phase des Q-Balls? [H]
- **S4 [L]: Bezout.**
  - Zwei Kegelschnitte schneiden sich in hoechstens 4 Punkten; n Quadriken in P^n in 2^n Punkten.
  - Alhazens Spiegelproblem fuehrt auf eine Gleichung 4. Grades.
  - Gravitationslinsen: n Punktmassen geben hoechstens 5n - 5 Bilder (Rhie, Khavinson/Neumann 2006 [L?]). Zaehlgrenzen aus dem Grad der Linsengleichung.
- **S5 [H]: Die 600-Zelle als Finns 4D-Tetraeder-Netz auf S^3** (120 Ecken, 600 regulaere Tetraeder).
  - Nach Fock wuerde ihr Laplace-Spektrum die Wasserstoff-Entartungen 1, 4, 9, 16, 25, ... zeigen, solange die H4-Symmetrie die SO(4)-Multipletts nicht spaltet.
  - Ableitbarkeitsprobe: Welche SO(4)-Harmonischen bleiben unter H4 irreduzibel? Das ist Gruppentheorie (vorab ableitbar, Literatur). Die Reihenfolge der Eigenwerte und die erste Spaltung sind klein rechenbar.

## Auftrag (feldforscher)

1. **S1 bis S5 an der Literatur pruefen:**
   - Kepler 1604 (Paralipomena: Brennpunkt, Stetigkeitsprinzip) [Sekundaerquelle reicht]
   - Fock 1935 bzw. Bander/Itzykson 1966
   - Kustaanheimo/Stiefel 1965
   - Bezout und Linsenbildzahl
   - 600-Zelle bzw. H4-Darstellungen und Laplace-Spektrum der 600-Zelle (gibt es das schon?)
2. **4D-Ideen fuer Finns Programm:** 4 bis 6 Ideen. Je: Idee, Bezug (Netz, Takt, Q-Ball, Licht, Wasserstoff/Unschaerfe), Ableitbarkeitsprobe, kleiner Test (hoechstens 10 min), Datenbezug falls vorhanden. Beispiele (nicht bindend):
   - Lichtkegel des Netzes geschnitten mit bewegten Ebenen: Abweichung der Kegelschnitte durch das kubische Muster
   - 4D-Takt als Folge von Schnitten
   - Wasserstoff auf der 600-Zelle
   - KS bzw. Hopf und die Q-Ball-Phase
   - Bezout-Zaehlung von Gleichgewichten bzw. Bildern
3. **Hoechstens ein Kartenvorschlag,** ausgearbeitet mit Vorhersagen, die scheitern koennen.

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| KB1 | Kontrolle [M, vorab gerechnet]: Kegelschnitt-Exzentrizitaet = Geschwindigkeit der schneidenden Ebene (e = v); Gegenlesen bestaetigt | 95 % |
| KB2 | [L?] Kepler fuehrte 1604 den Begriff "Brennpunkt" und das Stetigkeitsprinzip ein (Parabel als Ellipse mit einem Brennpunkt im Unendlichen) | 80 % |
| KB3 | [L?] Das Laplace-Spektrum der 600-Zelle zeigt fuer die untersten Niveaus die Entartungen 1, 4, 9, 16 (Literatur oder Gruppentheorie) | 55 % |
| KB4 | [L?] Die Bildzahl von n Punktlinsen ist hoechstens 5n - 5 (Rhie-Vermutung, bewiesen Khavinson/Neumann 2006) | 75 % |

**Bedeutung (vorab):**
- **KB1:** Keplers Stetigkeit ist geometrisch dasselbe wie relativistische Bewegung; die Parabel ist "Licht". Das ist eine anschauliche Bruecke fuer Finn, keine neue Physik.
- **KB3:** Ein 4D-Tetraeder-Netz (600-Zelle) traegt das Wasserstoff-Muster von selbst bis zu einer Grenze. Ein kleiner Test lohnt nur, wenn das nicht schon in der Literatur steht.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 8 Abrufe (arXiv-API, INSPIRE-API, arxiv.org per WebFetch, freie Verlagsseiten), keine Websuche.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/kegel-4d-l/.
