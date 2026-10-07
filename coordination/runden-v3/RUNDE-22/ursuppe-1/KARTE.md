# URSUPPE-1: Welche Dimension entsteht aus einer Graph-Suppe, und welche Regel braucht es dafuer? (Runde 22)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 20:30:13 CEST (date), vor jeder Rechnung. Gerechnet von der Leitung (Finn 20:28: "mach weiter, rechne beide tests parallel").
- Herkunft:
  - Finns Frage 20:24 ("1+2+3+4+xD teilchen die eine ursuppe bilden und daraus logik ueber geometrie entsteht?")
  - Arbeitsmodell v2.3 (§10, §11 Dimension; Variante B ohne Dynamik)
  - DIM-BEUTEL (spektrale Dimension als Messgroesse)
  - Erwartung G3 der Literaturkarte GEOMETRIE-STAND
- Ableitbarkeitspruefung: Graph-Dynamiken wurden im Projekt nicht gerechnet. DIM-BEUTEL mass feste Gitter und Fraktale.
- Explorativ (v3), Hypothesen [H]. Laeufe je <= 10 min auf der .69 (kleintest.sh, CPU-Spuren).

## Modell

- N = 600 Knoten. Start ist ein zufaelliger z-regulaerer Graph (z = 6 und z = 12; feste Saat, je zwei Saaten).
- Gradgleiche Doppelkanten-Tausche (a-b, c-d) -> (a-c, b-d), Metropolis bei sinkender Temperatur. Die Zahl der Tausche
  legt der Plan fest.
- Energien:
  - **E0** = 0: Kontrolle, bleibt zufaellig.
  - **E_tri** = - Sum_e t_e: moeglichst viele Dreiecke.
  - **E_man** = Sum_e (t_e - 2)^2: Flaechenregel, jede Kante in genau zwei Dreiecken.
  - Dabei ist t_e die Zahl der Dreiecke an Kante e.
- **Messgroessen:**
  - spektrale Dimension d_s(t) = 2 t Sum lambda e^(-lambda t) / Sum e^(-lambda t) aus den Laplace-Eigenwerten
  - das Plateau: das Fenster [t, 4t] vor der Endlichkeitszeit (P(t) > 2/N) mit der kleinsten relativen Schwankung;
    "Plateau", wenn die Schwankung < 20 % ist
  - Zusammenhangskomponenten, Clusterkoeffizient, Anteil der Kanten mit t_e = 2
- **K0 (Messgeraet):**
  - Dreiecksgitter auf dem Torus (25 x 25): Plateau mit d_s in 1,6 bis 2,4.
  - Zufallsgraph z = 6: kein Plateau unter 20 %, oder ein Plateau ueber 4.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| U0 | E0 (z = 6 und 12): kein Plateau mit d_s <= 4 (Zufallssuppe ohne endliche Dimension) | 85 % |
| U1 | E_tri: Die Suppe klumpt (mehr als eine Komponente oder Clusterkoeffizient > 0,5); kein Plateau mit d_s in 1,5 bis 3,5 | 65 % |
| U2 | E_man, z = 6: mindestens 80 % der Kanten mit t_e = 2, und Plateau mit d_s in 1,6 bis 2,4 (Flaeche) | 40 % |
| U3 | E_man, z = 12: weniger als 50 % der Kanten mit t_e = 2 (z = 12 vertraegt sich schlecht mit einer Flaeche) | 55 % |

**Bedeutung (vorab):**
- U0 und U1 treffen ein: Eine Suppe ohne lokale Konsistenzregel ergibt keinen Raum. Sie ist entweder unendlichdimensional
  (Zufall) oder klumpt (Dreiecke maximieren).
- U2 trifft ein: Eine lokale Flaechenregel (jede Kante in genau zwei Dreiecken) laesst eine Dimension von etwa 2 entstehen
  [H]. Entsprechend braucht eine 3D-Welt eine Regel fuer Tetraeder (jedes Dreieck in genau zwei Tetraedern); das waere
  der naechste Schritt.
- U2 trifft nicht ein: Die Flaechenregel allein reicht nicht, oder die Abkuehlung bleibt haengen; Grund beschreiben.

## Rahmen

- Code der Leitung: RUNDE-22/ursuppe-1/code/ursuppe.py.
- Plan mit Zahl der Tausche, Temperaturplan und Saaten vor dem ersten echten Lauf einfrieren; ein Rauchlauf ist vorher
  erlaubt.

## Plan der echten Laeufe (Leitung, 2026-10-02 20:40:58 CEST; vor den Laeufen eingefroren)

- **Rauchlaeufe (vor dem Einfrieren):**
  - Der Zufallsgraph-Erzeuger (Paarung mit Verwerfen) scheiterte.
  - Ersetzt durch den Zirkulanten-Ring C_N(1..z/2), gemischt mit 100 N gueltigen Tauschen (Standardverfahren).
  - K0-Gitter (25 x 25 Torus): Plateau d_s = 2,04, Schwankung 3,2 %. K0 bestanden.
  - Zufall z = 6: kein Plateau (None).
  - man, z = 6, nur 20 000 Tausche: Anteil t_e = 2 = 0,097, kein Plateau.
  - Diese drei sind gesehen.
- **Echte Laeufe:** N = 600; Saaten 1 und 2; T0 = 2, T1 = 0,02 (geometrisch).
  - z = 6: 2 000 000 Tausche; z = 12: 1 000 000 Tausche.
  - Arten: zufall (= E0), tri, man; dazu K0-Gitter erneut.
- **Endlichkeitsgrenze:** P(t) > 2 c/N mit c = Zahl der Komponenten. Gilt fuer mehrere Komponenten, steht so im Code.
- U0 wertet "kein Plateau mit d_s <= 4": Plateau None oder Schwankung >= 20 % oder d_s > 4.
