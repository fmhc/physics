# QBALL-PYRO-1: Eingefrorene Q-Baelle auf Finns Tetraedergitter? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 03:38:44 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Scout-Lauf 20261004T010216Z: arXiv 2606.15855 (DNLS auf dem Pyrochlor-Gitter, kompakte Zustaende aus der flachen
    Bande) [L?: nur Abstract gelesen]. Ideenpool S1.
  - Das Pyrochlor-Gitter besteht aus Tetraedern, die sich an den Ecken beruehren, also Finns Netz.
  - Bisher liefen unsere Q-Baelle auf Wuerfel- bzw. Dreiecksgittern (QBALL-GITTER-1, KEGEL-Q, DREIECK-LINSE-1).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Gitter:** Knoten auf den Kanten-Mittelpunkten des Diamantgitters; jeder Knoten hat 6 Nachbarn in zwei Tetraedern.
  - Graph-Laplace Delta = A - 6 I, A die Nachbarschaftsmatrix.
  - Spektrum von A [L]: zwei exakt flache Baender bei -2, zwei Baender mit Dispersion bis +6.
  - Also -Delta in [0, 8], die flachen Baender liegen am oberen Rand, bei -Delta = 8.
- **Kompakte Zustaende [M]:** Ein Sechserring (Hexagon) im Pyrochlor-Gitter traegt den Vektor v mit +-1 abwechselnd auf
  seinen 6 Knoten. Er ist Eigenvektor von A zu -2 (jeder Nachbarknoten ausserhalb sieht zwei entgegengesetzte Werte).
- **Nichtlinear [M]:** M1 auf dem Gitter mit Abstand h: Feldgleichung phi_tt = Delta phi/h^2 - U'(abs(phi)^2) phi,
  U(S) = S - S^2 + beta S^3, beta = 1/2.
  - Fuer f = a v gilt -Delta f = 8 f und abs(f)^2 = a^2 auf allen 6 Knoten. Also ist phi = a v e^(i omega t) eine exakte
    Loesung fuer jede Amplitude, mit omega^2 = 8/h^2 + U'(a^2).
  - Ein "Q-Ball", der genau auf einem Ring sitzt.
  - U'(S) = 1 - 2 S + 1,5 S^2 ist > 1 genau fuer S > 4/3. Fuer a^2 > 4/3 liegt omega^2 ueber dem ganzen Band
    (1 bis 1 + 8/h^2), fuer kleinere a^2 im Band.
- **Beweglichkeit [H]:** Flache Baender haben Gruppengeschwindigkeit 0. Ein Ringzustand sollte sich nicht verschieben
  lassen ("eingefroren").
- **Zum Vergleich:** Ein gewoehnlicher, kontinuumsnaher M1-Q-Ball (omega^2 = 0,7, mehrere Gitterabstaende breit) auf
  demselben Gitter.

## Test (Code-Agent)

- **Gitter:** periodisches Pyrochlor-Gitter, z. B. 6^3 bis 10^3 kubische Zellen (16 Knoten je Zelle); h frei
  (h = 1 fuer die Ringe, h = 0,5 fuer den Vergleichsball).
- **Linear:** Spektrum von A auf einem k-Gitter; flache Baender pruefen; Hexagon-Vektor als Eigenvektor pruefen.
- **Ring nichtlinear:**
  - Residuum der stationaeren Gleichung fuer a^2 = 0,5; 1; 1,5; 2; 3.
  - Zeitentwicklung (symplektisch, T = 100 bzw. 200) mit kleinem Rauschen; Leckanteil ausserhalb der 6 Knoten.
  - Lineare Stabilitaet (Bogoliubov-Eigenwerte um den Ring, kleiner Ausschnitt), soweit in <= 10 min machbar.
- **Beweglichkeit:** Ring mit Phasengradient (Impulsstoss) starten; Ladungsschwerpunkt ueber die Zeit.
- **Vergleichsball:** stationaerer M1-Q-Ball bei h = 0,5 auf dem Pyrochlor-Gitter, z. B. per Imaginaerzeit bzw. Newton.
  - Energie E und Ladung Q gegen den 3D-Kontinuumswert (Radiallöser, Tabelle RUNDE-02 bzw. REGEL-1).
  - Ein kleiner Stoss: Beweglichkeit gegen den Ring.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QP0 | [M] Zwei exakt flache Baender bei A = -2 (Abweichung <= 1e-12 ueber das k-Gitter); der Hexagon-Vektor ist Eigenvektor zu -2 (Residuum <= 1e-12) | 90 % |
| QP1 | [M] f = a v ist fuer alle fuenf Amplituden stationaere Loesung mit omega^2 = 8/h^2 + U'(a^2) (Residuum <= 1e-12); ohne Rauschen bleibt der Leckanteil ueber T = 100 <= 1e-10 | 85 % |
| QP2 | [H] Mit Rauschen (1e-6): Fuer a^2 > 4/3 (omega ueber dem Band) bleibt der Ring in mindestens einer der Amplituden 1,5; 2; 3 ueber T = 200 kompakt (Leck <= 1e-3). Fuer a^2 = 0,5 und 1 (im Band) zerlaeuft er (Leck >= 1e-2) | 45 % |
| QP3 | [H] Eingefroren: Ein Impulsstoss bis 10 % von omega verschiebt den Ladungsschwerpunkt eines stabilen Rings ueber T = 200 um weniger als einen halben Gitterabstand | 55 % |
| QP4 | Vergleichsball (h = 0,5, omega^2 = 0,7): E und Q weichen hoechstens 5 % vom 3D-Kontinuum ab, und er laesst sich durch einen Stoss verschieben (Schwerpunkt > 2 Gitterabstaende in T = 200) | 65 % |

**Bedeutung (vorab):**
- QP1 und QP3 treffen ein: Auf Finns Tetraedergitter gibt es neben den gewoehnlichen Q-Baellen exakte, gitterfeste
  Feldklumpen auf einzelnen Sechserringen. Ihre Frequenz liegt am oberen Bandrand, also bei Massen ~ 1/h, sehr schwer bei
  feinem Gitter.
  - Sie koennen sich nicht bewegen. Dann waeren sie als "eingefrorene Materie" ein Kennzeichen des Gitters selbst [H].
- QP2 verfehlt (alle Ringe zerlaufen): Die exakten Ringe sind instabil, also nur mathematisch interessant.
- QP4 trifft ein: Gewoehnliche Q-Baelle merken vom Tetraedergitter wenig.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
