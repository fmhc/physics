# TORSION-STEIF-1: Ist die Torsion auf einem flachen Kuhn-Gitter algebraisch festgelegt, und was messen Baender auf den Linien gegen Baender zwischen den Zellen? (Runde 45, Finns Weiche "Baender", beide Zweige)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 04:16:30 CEST (date), vor jeder Rechnung.
- **Finn (05.10., gegen 04:15):** zu den Baendern mit markierter Seite "Teste beides" (auf den Linien und zwischen den Zellen).
- **Herkunft:** Kartenvorschlag aus REGGE-TORSION-L (RUNDE-37/regge-torsion-l/DOSSIER.md, Abschnitt 5). Rechnung, Vorhersagen TS1 und TS2, Bedeutung und Ableitbarkeitsprobe von dort sind **bindend und woertlich**; die Wahrscheinlichkeiten setzt die Leitung. Zusaetze der Leitung sind markiert.
- Kennzeichen: [M], [E], [S], [L], [P], [H].

## Rechnung (woertlich aus dem Dossier)

- Gl. (47) um h = 1 entwickeln: flache Geometrie, alle Simplexrahmen gleich ausgerichtet, Holonomie h_e = exp(X_e) je inneres Dreieck.
- Ln h_B nach Baker-Campbell-Hausdorff bis zur zweiten Ordnung; die Mittelung ueber die m_B Startsimplizes gibt Paargewichte, die vom zyklischen Abstand abhaengen [M, vorab].
- Daraus den Hesse-Block Q (X gegen X, 3 Zahlen je Dreieck) und den gemischten Block M (Kantenvektor gegen X) bilden; der Kanten-Kanten-Block ist bei h = 1 null.
- Bloch-Zerlegung auf dem periodischen 3D-Kuhn-Gitter (6 Tetraeder und 12 Dreiecke je Wuerfel, also Q(k) als 36 x 36). Code-Basis REGGE-4D-1, 3D-Kontrolle Abschn. 3.3 [P].
- Eigenwerte von Q(k) auf einem k-Gitter, dazu die volle Matrix [[0, M], [M^T, Q]] gegen die Eichbahnen (SO(3) je Tetraeder, Verschiebung je Ecke).

## Zusaetze der Leitung (Finns zweiter Zweig, beschreibend)

- **Arm "Baender auf den Linien":** Ein gerahmtes Band entlang der Kanten wird um eine Gelenkkante mit Fehlwinkel delta herumgefuehrt (gekruemmte Probe, z. B. ein Kegel-Defekt).
  - Messgroesse: Drehung des Rahmens.
  - Kontrolle [vorab ableitbar]: Drehung = delta. Das zeigt, dass Baender auf Linien die Kruemmung messen.
- **Arm "Rahmenenergie":** Bekommen die Rahmen je Zelle eine eigene Gradientenenergie (wie das Guertel-Feld), wird die Torsion dann ausbreitungsfaehig, also vom Cosserat- bzw. Poincare-Typ?
  - Messgroesse: Spektrum der Torsionsmoden mit und ohne Zusatzenergie.
  - Beschreibend, nur wenn die Zeitbox reicht.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TS0 | [Zusatz Leitung] Kontrolle: Arm "Linien" gibt Rahmendrehung = Fehlwinkel auf 1e-8; ohne Torsion reproduziert der Code die Eichnullmoden (Verschiebung je Ecke) | 85 % |
| TS1 | [H] Q(k) hat fuer k != 0 mindestens eine Nullmode; die Torsion ist auf dem Gitter dann nicht algebraisch festgelegt (woertlich) | 45 % |
| TS2 | [H] Die volle Matrix hat ausser den Eichbahnen keine Nullmoden (woertlich) | 55 % |

**Bedeutung (woertlich, dazu Zusatz):**
- **TS1 verfehlt:** Regime A gilt auf dem Netz. Torsion ist dann ein Spindichte-Platz ohne eigene Dynamik, und Finns Guertel-Feld waere keine Einstein-Cartan-Torsion. Danach erst die Skizze der Spin-Torsion-Kopplung.
- **TS1 trifft ein:** Die Torsion ist auf dem Netz unbestimmt. Vor jeder Spin-Kopplung ist dann zu klaeren, ob das ein Artefakt der Mittelung bzw. des Logarithmus ist.
- **[Zusatz Leitung] Fuer Finn:**
  - Baender auf den Linien messen die Kruemmung (TS0).
  - Baender zwischen den Zellen tragen Torsion. Ob sie dann eigene Dynamik haben, entscheiden TS1 und TS2.

## Ableitbarkeitsprobe (woertlich, gekuerzt)

- **Vorab ableitbar:**
  - Im Kontinuum ist die Zusammenhangsgleichung bei nicht entarteter Triade eindeutig loesbar [L].
  - Die Paargewichte der Startpunkt-Mittelung sind ableitbar [M].
  - Auf der Zwangsflaeche gibt es keine Rest-Eichung; jede X-Nullmode waere echt [M].
- **Nicht ableitbar:** ob Q(k) bei endlichem k Nullmoden hat (Mittelung, Gitterdoppler).
- **Literatur zuerst:** Christiansen/Hu/Lin 2023 (2312.11709) koennte den linearen Fall schon enthalten. Vor dem Rechnen den Volltext lesen (ein Abruf).
- **Grenze:** 3D-Gravitation hat keine lokalen Freiheitsgrade [L]. Gefragt ist nur, ob die Torsion festgelegt ist.

## Rahmen

- Code-Agent; ein bis zwei Abrufe per WebFetch erlaubt (2312.11709, ggf. 2610.00593 aus regge-torsion-l/quellen lokal).
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu11.
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 90 min.
