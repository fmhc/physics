# TWIST-SPIN-1: Plan des Code-Agenten (Runde 41)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 13:14:01 CEST (date). Karte, TWIST-PYRO-1 (Karte, Plan,
  Ergebnis, Code, Quelle), STRINGENDE-1/ERGEBNIS.md, DYON-STATISTIK-L/DOSSIER.md und RUNDE-34/tetra-konzept/ANALYSE.md
  gelesen ab 13:14:01; Quelle vollstaendig gelesen vor 13:34:06; Code-Entwurf ab 13:39:03; Plantext ab 13:44:17 CEST
  (date).
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde41-twist-spin/ ueber kleintest.sh, Spur cpu6 (1 Thread,
  4 GB, <= 10 min). Reine Ganzzahl-Rechnung.
- **Kennzeichen:** [S] an der Quelle gelesen; [M] eigene Mathematik (Schreibtisch); [F] Festlegung dieses Plans; [H]
  Hypothese; [L] Literatur aus dem Gedaechtnis; [R] im Rauchlauf gesehen (vor dem Einfrieren); [Z] Zusatz dieses Plans,
  nicht aus der Karte (getrennt markiert, eigene Urteile).
- Vorhersagen TS0 bis TS3 und ihre Wahrscheinlichkeiten stehen unveraendert auf der Karte.

## 0. Quelle [S]

- Lokale Kopie (wie TWIST-PYRO-1, in quellen/): M. Levin, X.-G. Wen, "Quantum ether: photons and electrons from a rotor
  model", Phys. Rev. B 73, 035122 (2006), arXiv:hep-th/0507118v2. Text vollstaendig gelesen; grep nach "rotat", "spin",
  "framing". Keine weiteren Abrufe (0 von 3): Die Frage ist mathematisch; der Bezug zum Gürteltrick bleibt [L].
- Was die Quelle zu Drehungen und Spin sagt: **nichts ueber Gitterdrehungen.** Fundstellen:
  - S. 5: "To define W~(C), one must first choose a projection of the 3D lattice onto a 2D plane. Any projection will
    work"; "The choice of framing, C', is not unique". Die Projektion ist eine feste Zusatzstruktur.
  - S. 7: Vergleich mit "a standard tight binding model of spinless fermions, each site can be occupied by 0 or 1
    fermion. However, in our case the charge QI can be any integer". Die Quelle vergleicht ihre Fermionen mit
    *spinlosen* Gitterfermionen, ein Zustand je Knoten und Ladung.
  - S. 8: "The hopping operators t~IJ are completely characterized by the two algebraic relations (19),(20). Any
    collection of hardcore hopping operators that satisfy these relations will give rise to a Hamiltonian equivalent
    to (18)." (19) = Statistik, (20) = Fluss um Plaketten. Grundlage fuer Stufe F unten.
  - S. 9: Spin 1/2 im Kontinuum kommt aus der Bandstruktur: pi-Fluss von Hand (Gl. 24, 25), "the bands are doubly
    degenerate ... a total of 4 massless four component Dirac fermions"; c = c_e nur abgestimmt.

## 1. Schreibtisch und Ableitbarkeitsprobe (vor jeder Rechnung)

### 1.1 Wirkung einer Drehung [M]

- Vorzeichenalgebra wie TWIST-PYRO-1 (exakt): L+- -> X, (-1)^{L^z} -> Z; Huepfer h_l = X_l Z_{T(l)}, Schleifen
  B~_p = X_{E(p)} Z_{T(p)}, Lesart S. Eine Drehung g permutiert Kanten: P_g h_l P_g^-1 = X_{gl} Z_{g T(l)}, waehrend
  das Modell an gl den Huepfer X_{gl} Z_{T(gl)} hat. **Fehlmenge D_l(g) = g T(l) + T(gl)**, ebenso fuer Schleifen.
- Die Fehlmenge ist ein Z-Operator, kein Vorzeichen. Er ist genau dann ein "lokaler Eichfaktor" im Sinn der Karte
  (Vorzeichen je Kante, Faktor (-1)^{Q_I} = Z_{Stern(I)} je Knoten), wenn D ein Korand ist (Summe von Sternen).

### 1.2 Satz K (Vertauschungsgraph) [M]

- K_lm = [m in T(l)] + [l in T(m)] (Vorzeichen h_l h_m = (-1)^K h_m h_l; nur fuer Kanten mit gemeinsamem Knoten
  ungleich 0).
- Jede unitaere Abbildung, die jedes h_l auf ein Vielfaches von h_{gl} abbildet, erhaelt K. Umgekehrt: Ist K
  g-invariant, dann ist C_{gl,gm} = [gm in D_l] symmetrisch, und U'_g = V_g P_g mit der lokalen Phase
  V_g = (-1)^{Sum C n n} (CZ-artig, nur Beinpaare am selben Knoten) bildet jedes h_l exakt auf h_{gl} ab. Twisted
  Schleifen gehen dann auf +-B~_{gp}, weil beide mit allen Huepfern vertauschen.
- **Seitensatz:** Nach TWIST-PYRO-1 1.3 ist K_lm = 1 genau dann, wenn l und m (projiziert) auf derselben Seite der
  Geraden durch den Knoten in Richtung delta_h liegen. Die Seite eines Beins d ist sign(cross(delta_h, M d)) =
  sign(nu . d) mit **nu = 4 M_0 + 5 M_1** (delta_h = (5, -4)). Werte: nu(P1) = (80, 67, 100), nu(P2) = (74, -40, -25),
  nu(P3) = (121, -20, -25). K haengt also nur von der Ebene senkrecht zu nu ab.

### 1.3 Folgen fuer Stufe K (vorab, vollstaendig) [M]

- **Diamant, T am Knoten** (Beine d1 = (1,1,1), d2 = (1,-1,-1), d3 = (-1,1,-1), d4 = (-1,-1,1)):
  - nu . d = (247, -87, -113, -47) fuer P1: Teilung {d1} | {d2, d3, d4}. Invariant nur unter C3 um [111]:
    **K-Untergruppe {e, a, aa}** (a = C3 um [111]).
  - P2: (9, 139, -89, -59), P3: (76, 166, -116, -126): Teilung {d1, d2} | {d3, d4}. Invariant unter allen drei C2 um
    die Wuerfelachsen: **K-Untergruppe V4 = {e, C2x, C2y, C2z}**.
  - Allgemein: Eine T-invariante Zweifaerbung der vier Beine waere einfarbig; das geht mit einer Ebene nicht, weil
    Summe d = 0. **Fuer keine generische Projektion wirkt ganz T auf Stufe K.**
- **Pyrochlor-Kanten, T am Tetraederzentrum:** Die Teilung an Plaetzen der Klasse i (Mittelpunkt einer Bindung d_i)
  haengt an den Rangfolgen der v_j = nu . d_j. Invariant sind nur e und die C2, die die Rangfolge umkehrt:
  **P1: {e, C2y}, P2: {e, C2z}, P3: {e, C2y}.**
- **Kubisch (LW-Nachbau), O am Knoten:** Teilung nach dem Oktanten von nu. P1: Oktant (+,+,+), **K-Untergruppe D3 um
  [111]** (6 Elemente); P2, P3: Oktant (+,-,-), **D3 um [1,-1,-1]**. Keine Vierteldrehung C4 wirkt auf Stufe K. Damit
  ist schon LWs eigenes kubisches Modell mit fester Projektion nicht voll O-symmetrisch.
- **Pyrochlor, D3 am Platz:** nicht von Hand hergeleitet (Rechnung).
- Offen bleibt auf Stufe K nur das Schleifenvorzeichen sigma auf den K-Untergruppen (nicht hergeleitet).

### 1.4 Stufe W (Kartenwortlaut) [M]

- Innerhalb einer Seite gilt T(l) = Beine derselben Seite mit kleinerem Winkel zu delta_h (TWIST-PYRO-1 1.3). Eine
  C3 (P1, drei Beine auf einer Seite) oder C2x (P2, P3, tauscht d1 und d2 auf derselben Seite) aendert diese
  Winkelfolge. Dann enthaelt D_l an einem Knoten genau ein Bein; das ist kein Korand (ein Stern hat alle Beine).
- **Folge:** Stufe W scheitert beim Diamant fuer alle drei Projektionen schon an einem Element. Fuer Pyrochlor-T
  erwartet [H].

### 1.5 Stufe F (schwach, Teilchenzahl erhalten) [M mit S. 8]

- In der Quelle bestimmen (19) Statistik und (20) Fluss das Huepfproblem. Alle Seitenteilungen geben T2 = -1
  (TWIST-PYRO-1). Also ist das gedrehte Modell im Sektor fester Teilchenzahl (hardcore) genau dann gleichwertig, wenn
  der **Fermionfluss Phi_p** jeder kleinsten Schleife g-invariant ist: Phi_{gp} = Phi_p.
- Messvorschrift Phi_p: Ein Fermion am Startknoten v0, Partner fern, Sektor B~_q = +1 fuer alle q. O = Produkt der
  Huepfer um p = i^m X_{E(p)} Z_S; S + T(p) = Summe der Sterne einer Knotenmenge V' (kleinere Wahl);
  Phi_p = i^m (-1)^{[v0 in V']}. Umgekehrte Umlaufrichtung: zusaetzlich (-1)^{|E(p) n T(p)|} (aus B~^dagger). Alle
  Startknoten und beide Richtungen muessen gleich sein.
- **Handrechnung (Fig. 5, kubisch, P1; Gl. 11 wie in TWIST-PYRO-1 nachgebaut):** xz-Plakette A = (0,0,0),
  B = (1,0,0), C = (1,0,1), D = (0,0,1), Umlauf A->B->C->D. O = h_AD h_DC h_BC h_AB = +X_{dp} Z_S mit
  S = {AB, BC, A+y, C-y, B+x, B+y, B-z, B-y}; S + T(p) = Stern(B) + Stern(D); V' = {B, D}; Start A: **Phi = +1**;
  Start B: O_B = -O_A, (-1)(-1) = +1. Diese Werte stehen fest im Code (fig5_probe).
- Phi fuer Diamant- und Pyrochlor-Schleifen ist **nicht hergeleitet**. Stufe F ist der eigentlich offene Teil.
- [Z] Frustrationsprobe: Phi setzt voraus, dass es den Sektor "alle B~ = +1" gibt. Ich pruefe das orientierte Produkt
  der B~ ueber geschlossene Zellflaechen (Wuerfel, Adamantan-Kaefige, Tetraeder, Kuboktaeder-Stumpf-Tetraeder) im
  Ladung-0-Sektor; jedes Vorzeichen muss +1 sein.

### 1.6 TS2 vorab [M]

- (a) **Paarerzeuger zeigen im bosonischen Modell nie 2T:** Wirkt eine Gruppe exakt (Stufe K), bildet jede Relation
  (U'_a)^3, (U'_b)^2, (U'_b U'_a)^3 jedes h_l und jedes Z_l auf sich ab, ist also ein Skalar. Auf jedem
  Paarerzeuger ist das Pruefvorzeichen dann +1. Das gilt auch im PSG-Bild: Paarerzeuger (Teilchen plus Gegenteilchen)
  tragen lambda mal lambda* = +1.
- (b) **Ein Fermion am festen Knoten traegt keine projektive Klasse:** Je Knoten und Ladung gibt es einen Zustand
  (Quelle S. 7). Eine eindimensionale projektive Darstellung ist ein Korand. Fuer T ist die Invariante
  I = lambda3^2 / (lambda1^2 lambda2^3) (lambda1 = (C3)^3, lambda2 = (C2)^2, lambda3 = (C2 C3)^3); eindimensional ist
  I = 1. Bei reellen Eichfaktoren (+-1) ist I = lambda2 = eta_b(I0)^2 = +1. Fuer O ist die Invariante (C4)^4, fuer
  D3 gibt es keine (H^2(D3, U(1)) = 0: Spin 1/2 ist dort projektiv nicht von ganzzahlig unterscheidbar).
- (c) Einzelwerte (C3)^3 usw. haengen von der Normierung ab (A -> -A kippt (C3)^3). Ich normiere eta_g(I0) = +1 am
  Fixknoten bzw. am Bezugsknoten (1,1,1) beim Pyrochlor-T.
- **Folge:** Beim Diamant (T am Knoten) ist TS2 in jeder Stufe "nicht eingetroffen", sobald TS1 in dieser Stufe
  traegt; sonst "entfaellt". Nur beim Pyrochlor-T am Tetraederzentrum (kein Knoten fest) ist die Klasse nicht
  hergeleitet; reell ist sie dort (C2)^2 an einem beliebigen Knoten.

### 1.7 Die Vermutung der Leitung (Verdrillung -> Spin-Statistik) [M, gegen die Leitung]

- Der Guerteltrick [L: Finkelstein und Rubinstein 1968, aus dem Gedaechtnis] braucht eine stetige Schar von Rahmungen,
  die lokal ineinander ueberfuehrt werden. Auf dem Gitter aendert sich K, sobald nu eine Ebene senkrecht zu einem
  Bein ueberquert (Satz K). Dort gibt es keine lokale Unitaere, die Huepfer auf Huepfer abbildet.
- Eine nichttriviale T-Klasse braucht mindestens zwei Zustaende am festen Punkt; ein Fadenende am Knoten hat einen.
- **Vorhersage:** Spin-Statistik folgt auf Finns Netz nicht aus der Verdrehung allein. Halber Spin unter
  Gitterdrehungen braucht mehr Zustaende je Knoten (oder entsteht wie bei LW erst in der Bandstruktur).

### 1.8 Ableitbarkeitstabelle

| Nr | Karte | Schreibtisch (dieser Plan) | Rest fuer die Rechnung |
|---|---|---|---|
| TS0 | ungedreht echt, alle +1 | ja: D = 0, K = 0, U'_g = P_g, Phi = +1, Relationen Identitaet [M] | nur Kontrolle (Code) |
| TS1 | Diamant: Drehungen mit Eichfaktoren symmetrisch | Plan (Stufe K): **nein**, K-Untergruppen 1.3; Wortlaut (Stufe W): **nein** 1.4 | sigma auf den Untergruppen; Stufe F offen [Z] |
| TS2 | falls TS1: projektiv | Plan, Wortlaut: **entfaellt**; schwach: **nein** am Knoten 1.6 | PSG-Kontrolle, falls Stufe F traegt |
| TS3 | Pyrochlor wie Diamant | Plan: TS1 nein (1.3), TS2 entfaellt -> **gleich, also eingetroffen**; Wortlaut erwartet ebenso [H] | Stufe F und PSG beim Pyrochlor offen |

- Was die Rechnung noch pruefen kann: die beiden Saetze (eine einzige Abweichung von 1.3 widerlegt den Seitensatz),
  den Code, die Handrechnung 1.5, und neu: Stufe F (Fermionfluss), die Frustrationsprobe und beim Pyrochlor-T die
  PSG-Klasse.

## 2. Netze, Gruppen [F]

- Netze und Schleifen aus TWIST-PYRO-1 (eingefrorener Code, unveraendert importiert): Diamant n = 2, 3 (Sechsecke);
  Pyrochlor-Kanten n = 1, 2 (Dreiecke, Sechsecke); kubisch L = 3, 4 (Plaketten). Projektionen P1, P2, P3, Lesart S
  (Hauptlesart von TWIST-PYRO-1; Lesart V wird nicht gerechnet, sie verletzt schon LWs Aussage).
- Gruppen als ganzzahlige Matrizen um ein Zentrum c: g(s) = c + R(s - c) mod Periode.
  - **Diamant: T um den Knoten (0,0,0)**, Erzeuger a = C3 um [111] ((x,y,z) -> (z,x,y)), b = C2 um z;
    Relationen (C3)^3 = aaa, (C2)^2 = bb, (C2 C3)^3 = ababab (Buchstaben in Zeitfolge, erst a).
  - **Pyrochlor: T um das Tetraederzentrum (0,0,0)** (gleiche Gruppe wie beim Diamant, damit "dasselbe" vergleichbar
    ist; kein Knoten bleibt fest). Zusaetzlich D3 um den Platz (1,1,1) (a, b = C2 um [1,-1,0]; Relationen aaa, bb,
    abab, denn in D3 hat C2 C3 die Ordnung 2: Kartenberichtigung, (C2 C3)^3 passt dort nicht). D3 nur berichtet.
  - **Kubisch: O um (0,0,0)**, a = C3 um [111], c = C4 um z; Relationen aaa, cccc, acac.
- Ungedreht (alle T leer) wird auf allen Netzen mitgerechnet (TS0).

## 3. Rechenweg (exakt) [M]

- Je Netz, Groesse, Projektion und Gruppenelement g:
  - **Stufe W:** Fehlmengen D aller Huepfer und Schleifen; Zahl der D, die kein Korand sind (Breitensuche-Loeser
    delta y = D). Stufe W traegt fuer g, wenn alle D Koraender sind.
  - **Stufe K:** Zahl der Paare (l, m) am selben Knoten mit K_{gl,gm} ungleich K_lm. Bei 0: Clifford-Abbildung
    X_l -> X_{gl} Z_{D_l}, Z_l -> Z_{gl}; Pruefung U'(h_l) = h_{gl} (exakt) und Schleifenvorzeichen sigma_p:
    U'(B~_p) = sigma B~_{gp} (gleicher Umlauf) bzw. sigma (B~_{gp})^dagger mit Faktor (-1)^{|E n T|}. Stufe K traegt
    fuer g, wenn K-Abweichungen 0, alle Huepfer exakt und alle sigma = +1.
  - **Stufe F:** Phi_p fuer alle Schleifen (1.5); Zahl der p mit Phi_{gp} ungleich Phi_p. Stufe F traegt fuer g, wenn 0
    Abweichungen, 0 Inkonsistenzen, alle Korandloesungen vorhanden.
- **Relationen (Stufe K):** Sind alle Buchstaben einer Relation K-symmetrisch, wird die zusammengesetzte Abbildung auf
  allen X_l, Z_l geprueft (Identitaet?) und auf dem Paarerzeuger h_{l0} am Fixknoten ausgewertet.
- **PSG (Stufe F, nur wenn alle g der Gruppe Stufe F tragen):** Eichfeld x mit Summe x um p = [Phi_p = -1]
  (GF(2)-Elimination); Eichfaktoren eta_g aus delta y = x + x o g^-1, bei Bedarf mit einer der 8 Torus-Holonomien;
  Normierung eta_g(I0) = +1; Relationswerte an allen Knoten (muessen konstant sein), Wert am Bezugsknoten, Paarerzeuger
  lambda(I0) lambda(J), Invariante ((C2)^2 fuer T, (C4)^4 fuer O).
- **Frustrationsprobe [Z]:** Zellflaechen ueber Zentren und Abstand (kubisch Wuerfel, Diamant Adamantan-Kaefige um
  A + (2,2,2), Pyrochlor Tetraeder um A und A + (2,2,2) sowie Stumpf-Tetraeder um A + (4,4,4)); Flaeche muss
  geschlossen und orientierbar sein; Vorzeichen des orientierten Produkts im Ladung-0-Sektor.
- Generik: Entartungs- und Unklar-Zaehler aus twist_pyro.drehung muessen 0 sein (wie TWIST-PYRO-1).

## 4. Urteilsregeln (mechanisch in code/auswertung_spin.py)

- Moegliche Urteile: "eingetroffen", "nicht eingetroffen", "nicht auswertbar", "entfaellt" (Bedingung "falls TS1"
  nicht erfuellt).
- **Sperren:** nicht generisch (Zaehler ungleich 0), fehlende Schleifenbilder, unklare Umlaufrichtung, Phi-
  Inkonsistenz oder Matrix-Relation ungleich Identitaet im betroffenen Teil -> "nicht auswertbar".
- **Nach Plan (Haupturteil):**
  - TS0: eingetroffen genau dann, wenn ungedreht auf allen Faellen und Groessen alle g Stufe K tragen, alle
    berechenbaren Relationsautomorphismen Identitaet sind, alle Paarerzeuger-Vorzeichen +1 und alle PSG-Invarianten
    +1 (bzw. keine) sind.
  - TS1: eingetroffen genau dann, wenn es eine Projektion gibt, fuer die beim Diamant (n = 2 und 3) alle 12 Elemente
    von T Stufe K tragen.
  - TS2: entfaellt, wenn TS1 (Plan) nicht eingetroffen. Sonst eingetroffen genau dann, wenn fuer diese Projektion ein
    Paarerzeuger-Vorzeichen (Stufe K) gleich -1 ist.
  - TS3: wie TS1 und TS2 fuer Pyrochlor-T (n = 1 und 2); eingetroffen genau dann, wenn beide Urteile gleich den
    Diamant-Urteilen sind.
- **Nach Kartenwortlaut:** wie Plan, aber Stufe W statt K ("lokale Eichfaktoren: Vorzeichen je Kante bzw. Knoten").
  TS2 (falls TS1): eingetroffen, wenn ein Pruefvorzeichen auf einem Paarerzeuger -1 ist (PSG-Werte, falls vorhanden,
  sonst Stufe K).
- **[Z] schwach (Stufe F):** TS1-schwach: es gibt eine Projektion, fuer die beim Diamant (n = 2, 3) alle g Stufe F
  tragen und die Frustrationsprobe nur +1 zeigt (sonst "nicht auswertbar"). TS2-schwach (falls TS1-schwach):
  eingetroffen genau dann, wenn die PSG-Invariante -1 ist. TS3-schwach: Pyrochlor-T gleich Diamant in beiden.
- **Schreibtisch-Abgleich (beschreibend, kein Urteil):** K-Untergruppen je Projektion gegen 1.3; Fig.-5-Probe gegen
  1.5; Gegenprobe Stufe F (Fluss einer Schleife umgedreht muss Abweichungen erzeugen).
- Schreibtisch-Erwartung (vor jeder Rechnung): Plan TS0 eingetroffen, TS1 nicht eingetroffen, TS2 entfaellt, TS3
  eingetroffen. Wortlaut gleich. Schwach: offen (Stufe F nicht hergeleitet).

## 5. Kontrollen [F]

- Ungedreht (TS0) auf allen Netzen; kubischer LW-Nachbau mit Vierteldrehungen (Gruppe O): erwartet Stufe K nur D3
  (1.3), C4 nicht; Stufe F offen, Fig.-5-Probe Phi = +1.
- Gegenprobe Stufe F: Fluss der Schleife 0 umgedreht; fuer mindestens ein g ungleich e muss die Zahl der Abweichungen
  > 0 sein.
- Stufe K kann scheitern: Die K-Abweichungen ungleich 0 sind fuer die meisten g vorab erwartet.

## 6. Laeufe [F]

- Rauch: Diamant n = 2, Pyrochlor n = 1 (T und D3), kubisch L = 3; alle Projektionen; ungedreht.
- Haupt: Diamant n = 2, 3; Pyrochlor n = 1, 2 (T und D3); kubisch L = 3, 4. Danach Auswertung.
- Wirkung des Rauchlaufs: keine auf Vorhersagen, Schwellen oder Urteilsregeln; er prueft, ob der Code laeuft.
  Was er zeigt, steht in Abschnitt 7.

## 7. Rauchlauf [R]

- Text ab 2026-10-04 13:50:03 CEST (date), vor dem Einfrieren.
- **Laeufe** (.69, kleintest.sh, Spur cpu6; Zeiten aus den Starter-Zeilen, UTC + 2 h; alle rc = 0, je unter 2 s;
  Diamant n = 2, Pyrochlor n = 1, kubisch L = 3):
  - rauch 13:47:01 bis 13:47:03, Auswertung 13:47:08: erste Fassung.
  - rauch2 13:48:39 bis 13:48:41 und Auswertung: mit Diagnosezaehlern (unten).
  - rauch3 13:49:43 bis 13:49:45 und Auswertung: mit vollstaendiger Kaefigliste. Ausgaben in rauch-69/.
- **Codeaenderungen vor dem Einfrieren (keine an Vorhersagen, Schwellen oder Urteilsregeln):**
  1. fermionfluss: Diagnosezaehler (phase_minus, start_in_V, E_T_ungerade, auswertungen) und eine Vorzeichen-Option
     fuer die neue beschreibende **Gegenprobe "Kante 0"** (Huepfer auf Kante 0 mit -1: genau die Schleifen mit
     Kante 0 muessen kippen); auswertung_spin.py zeigt sie im Abgleich. Grund: Im ersten Rauchlauf war Phi ueberall
     +1; ich wollte sehen, ob die Konsistenzpruefung leer laeuft.
  2. Kaefigliste vervollstaendigt: Diamant auch die Kaefige um A + (3,3,3) (= B + (2,2,2)), Pyrochlor auch die
     Stumpf-Tetraeder um A + (6,6,6). Grund: Zaehlprobe; jedes Sechseck gehoert zu zwei Zellen, also 8 Zellen je
     kubischer Zelle, im ersten Lauf waren es 4.
- **Gesehen, offengelegt (rauch3):**
  - K-Untergruppen in allen neun Paaren (Diamant, Pyrochlor-T, kubisch; P1 bis P3) genau wie 1.3. Auf diesen
    Untergruppen sind alle Schleifenvorzeichen sigma = +1 (Stufe K traegt genau auf der K-Untergruppe).
  - **Fermionfluss Phi = +1 auf allen Schleifen** aller Netze und Projektionen (128 Sechsecke; 32 Dreiecke und 16
    Sechsecke; 81 Plaketten), 0 Inkonsistenzen. Die Konsistenzpruefung ist nicht leer: Die -1 aus der Phase und die -1
    aus "Start in V'" kommen gleich oft vor (z. B. Diamant P2: je 1024 von 1536 Auswertungen) und heben sich in jeder
    Auswertung auf. |E n T| ist ueberall gerade; der Umkehrfaktor wurde also nie gebraucht. Gegenprobe Kante 0: genau
    die Schleifen mit Kante 0 kippen (6 bzw. 4).
  - Damit traegt Stufe F fuer alle Elemente (Fluss gleichfoermig). Das war am Schreibtisch offen (1.5) und ist jetzt
    vor dem Einfrieren gesehen. Vertraeglich mit der Quelle S. 8, Gl. (20): Huepferprodukt um eine Doppelplakette =
    Fluss "up to some signs having to do with orientation conventions"; in diesen Konventionen kommt kein Zusatzzeichen.
  - Fig.-5-Probe wie die Handrechnung (Phi = +1, V' = {(1,0,0), (0,0,1)}).
  - Frustrationsprobe: alle geschlossenen Zellen +1 (Diamant 64, kubisch 27, Pyrochlor 8 Tetraeder). Pyrochlor n = 1:
    8 Stumpf-Tetraeder "nicht geschlossen" (der Torus mit 16 Knoten ist fuer diese Zelle zu klein).
  - PSG: Holonomie-Maske 0 genuegt; alle Relationswerte +1 an allen Knoten; Invarianten +1.
  - Rauch-Urteile (kleinste Groessen): Plan TS0 eingetroffen, TS1 nicht eingetroffen, TS2 entfaellt, TS3 eingetroffen;
    Wortlaut ebenso; schwach: TS0, TS1 eingetroffen, TS2 nicht eingetroffen, TS3 nicht auswertbar (wegen der
    Pyrochlor-n = 1-Zellen).
- **Folge:** Keine Aenderung an Vorhersagen, Schwellen oder Urteilsregeln. Insbesondere lockere ich die
  Frustrationsregel nicht, obwohl ich jetzt weiss, dass sie TS3-schwach voraussichtlich "nicht auswertbar" macht
  (Selbstanzeige). Plan und Code werden in dieser Fassung eingefroren.
- **Selbstanzeige bis zum Einfrieren:** Lokal ausser der erlaubten Liste nur Datei- und Anzeigebefehle (ls, cat, head,
  tail, wc). Kein Interpreter lokal; auf der .69 ausserhalb des Starters nur mkdir, mv, ls, tail, sed (Anzeige des
  Starters), sha256sum. Code lokal mit sed geaendert (neue Datei .neu, dann mv); auf der .69 per scp nach .neu, dann mv.
