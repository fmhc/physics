# KAUSAL-1: Wie sieht ein zufaelliges Raumzeit-Netz ohne Ruhesystem aus? (Runde 37)

- Leitung claude-primary, rechnet selbst. Karte und Vorhersagen geschrieben ab 2026-10-04 02:45:43 CEST (date), vor jeder
  Rechnung.
- **Anlass:**
  - Finn ~02:40: "Ok weiter entwickeln". RUNDE-37/RAUMZEIT-NETZ.md, Lesart Kausalmenge.
  - ZUFALLS-REIBUNG-1: Ein raeumlich zufaelliges Netz zeichnet ein Ruhesystem aus.
  - Frage: Was kostet ein zufaelliges Netz in Raum UND Zeit, das keines auszeichnet?
- Kennzeichen: [M] Mathematik (Herleitung der Leitung), [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Modell:**
  - N Punkte gleichverteilt in einem kausalen Diamanten der 1+1-Raumzeit, in Lichtkegelkoordinaten (u, v) in [0,1]^2.
  - x liegt vor y genau dann, wenn u_x < u_y und v_x < v_y.
  - Ein Link ist ein Paar x vor y ohne Punkt dazwischen, also der "Strich" des Netzes.
- **Erwartung [M]:**
  - Relationen: Zwei Punkte sind mit Wahrscheinlichkeit 1/2 kausal verbunden.
  - Links: <L> = N (N - 1) int_0^1 int_0^1 (1 - a)(1 - b)(1 - a b)^(N - 2) da db. Fuer grosses N folgt
    <L>/N = ln N + gamma_E - 2 = ln N - 1,4228. Die Zahl der Striche je Punkt waechst also ohne Grenze.
  - Richtungen: Fuer einen Punkt fern vom Rand haben die zukuenftigen Links die Dichte N e^(-N A) dA d eta, mit Flaeche
    A = du dv und Rapiditaet eta = (1/2) ln(dv/du). Das ist gleichverteilt in eta, im Mittel genau 1 Link je
    Rapiditaetseinheit.
    - Das Netz bevorzugt also keine Geschwindigkeit: Links zeigen gleich oft in jede "Bewegungsrichtung".
    - Der Preis: Fast lichtartige Links gibt es in allen Rapiditaeten, und ihre Zahl waechst mit dem Netz. Das Netz ist
      nicht lokal.
- **Bezug [L]:**
  - Bombelli, Henson und Sorkin zeigen: Eine Poisson-Streuung in Minkowski zeichnet kein Bezugssystem aus.
  - Lokal begrenzte Nachbarschaft und Lorentz-Invarianz vertragen sich nicht.

## Test (Leitung, .69, Spur p4000a als CPU-Lauf)

- **Laeufe:** N = 2000, 4000, 8000, 16000, je 4 Saaten.
- **Links:** Punkte nach u sortieren. Ein zukuenftiger Kandidat y von x ist genau dann ein Link, wenn sein v kleiner ist
  als jedes v der Kandidaten davor (laufendes Minimum) [M]. Aufwand O(N^2), ohne Matrixprodukt.
- **Messgroessen:**
  - Anteil kausal verbundener Paare.
  - L/N je Saat.
  - Fuer Punkte im Zentrum (u, v in [0,4; 0,6]): Histogramm der Rapiditaet eta ihrer zukuenftigen Links (Klassen 0,25)
    und Dichte je Rapiditaetseinheit.
  - Zum Vergleich: exakter Wert des Doppelintegrals fuer <L>/N (beschreibend).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K0 | Kontrolle: Anteil kausal verbundener Paare 0,500 +- 0,01 fuer alle N | 95 % |
| K1 | L/N (Mittel der 4 Saaten) = ln N - 1,423 innerhalb 0,1 fuer jedes N | 75 % |
| K2 | Zentrum, N = 16000: Dichte der zukuenftigen Links je Rapiditaetseinheit 1,00 +- 0,05 in jeder 0,5-Klasse fuer abs(eta) <= 2 | 70 % |
| K3 | L/N waechst von N = 2000 bis 16000 um ln 8 = 2,08 +- 0,1 | 75 % |

**Bedeutung (vorab):**
- K1 bis K3 treffen ein: Ein Raumzeit-Netz ohne Ruhesystem hat keine festen Nachbarn. Jeder Punkt ist mit ~ln N
  anderen verbunden, gleich verteilt ueber alle Geschwindigkeiten.
- Fuer Finns Bild mit festen Tetraeder-Nachbarn heisst das: Entweder gibt es ein (sehr gut verstecktes) Ruhesystem, oder
  das Netz ist nicht lokal [L/H].
- Alles ist vorab ableitbar [M]. Der Test prueft die Herleitung der Leitung und zeigt die Zahlen fuer Finn.

## Rahmen

- Leitung rechnet selbst. Nur auf der .69 ueber kleintest.sh; je Lauf <= 10 min.
- Schwellen aendern sich nach dem Code nicht.
