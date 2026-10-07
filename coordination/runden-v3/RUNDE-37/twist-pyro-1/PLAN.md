# TWIST-PYRO-1: Plan des Code-Agenten (Runde 40)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 11:34:08 CEST (date). Karte, DYON-STATISTIK-L/DOSSIER.md
  (Abschnitt 8), STRINGENDE-1 (Karte, Plan, Ergebnis, Code), KITAEV-DIAMANT-1/ERGEBNIS.md und
  RUNDE-34/tetra-konzept/ANALYSE.md gelesen ab 11:34:08; Quelle gelesen ab 11:40 (ungefaehr, zwischen zwei date-Stempeln
  11:34:08 und 11:49:02); Plantext ab 11:54:40 CEST (date).
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde40-twist-pyro/ ueber
  /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spur cpu6 (1 Thread, 4 GB, <= 10 min). Reine Ganzzahl-Rechnung.
- **Kennzeichen:** [S] an der Quelle gelesen; [M] eigene Mathematik (Schreibtisch); [F] Festlegung dieses Plans (die
  Karte laesst es offen); [H] Hypothese; [R] im Rauchlauf gesehen (vor dem Einfrieren); [Z] Zusatzvorgabe dieses Plans,
  nicht aus der Karte (getrennt markiert, eigene Urteile nach Kartenwortlaut).
- Vorhersagen TP0 bis TP3 und ihre Wahrscheinlichkeiten stehen unveraendert auf der Karte. Hier stehen Modell,
  Messvorschrift, Schreibtischprobe und Urteilsregeln.

## 0. Quelle [S]

- Lokale Kopie des Feldforschers, keine neuen Abrufe (0 von 3): M. Levin, X.-G. Wen, "Quantum ether: photons and
  electrons from a rotor model", Phys. Rev. B 73, 035122 (2006), arXiv:hep-th/0507118v2 (13 Feb 2007), 10 S.
  Kopie in quellen/ (PDF sha256 70d21155..., Text sha256 ae790faf...). Gelesen: Text vollstaendig (pdftotext-Fassung
  des Feldforschers), Seiten 5 und 6 zusaetzlich als Bild (Fig. 4 bis 6).
- Fundstellen (Seite der arXiv-PDF):
  - S. 2, Gl. (1): Rotoren auf den Kanten des kubischen Gitters, Q_I = (-1)^I Sum_{legs of I} L^z_i,
    B_p = L+_1 L-_2 L+_3 L-_4; "The 'legs of I' are the six links that are attached to the vertex I".
  - S. 4, Gl. (5): ungedreht L+_i L-_j L+_k = L+_k L-_j L+_i "for any i, j, k incident to some vertex I"; "this is the
    bosonic hopping operator algebra".
  - S. 5, Gl. (7): [Q_I, W(C)] = [W(C'), W(C)] = 0 fuer geschlossene C.
  - S. 5, Gl. (8): W~(C) = (L+_{i1} L-_{i2} ...)(-1)^{Sum_{legs of C} n^c_i L^z_i}; "n^c_i is the number of times that the
    link i crosses the curve C', where C' is some 'framing' of C"; "To define W~(C), one must first choose a projection
    of the 3D lattice onto a 2D plane. Any projection will work"; "One can check directly that both of the equalities
    in (7) hold for the twisted string W~"; die Phase haengt ab von "rotors on the links incident to vertices I_k along
    the curve C".
  - S. 5, Gl. (9) und Fig. 5: Plakette in der xz-Ebene, Rahmung "shifting it up and to the left"; Drehfaktor auf den
    Kanten 1, 4, 5, 6, 7, 8, 9, 10 (die beiden Plakettenkanten oben und links und sechs Beine).
  - S. 6, Gl. (10), (11) und Fig. 6: Huepfer L~_i = W~(i) mit Rahmung "just down and to the right of the link i";
    "we pick a hopping term which commutes with B~_p"; "One can check that L~_i does in fact commute with B~_p".
  - S. 7, Gl. (12): L~+_i L~-_j L~+_k = (-1) L~+_k L~-_j L~+_i "for any i, j, k incident to some vertex I";
    "the fermionic hopping algebra".
- Nachbau von Fig. 5 [M]: Mit der Projektion (x, y, z) -> (x + 0,4 y, z + 0,3 y) (y nach rechts oben) und der
  Rahmung = Plakettenrand, um (-eps, +eps) verschoben, kreuzen genau die Kanten 1, 4, 5, 6, 7, 8, 9, 10 die Rahmung
  (oben, links, +y-Bein unten links, -y-Bein oben rechts, vier Beine oben links). Das trifft die Abbildung. Nachbau von
  Fig. 6 / Gl. (11) [M]: Rahmung um (+eps, -eps): x-Kante -> zwei Beine am rechten Ende (-z, -y), z-Kante -> zwei
  Beine am unteren Ende (+x, +y). Das trifft Gl. (11) in der Zahl und Lage der Faktoren.

## 1. Kartenpruefung und Schreibtischprobe (vor jeder Rechnung)

### 1.1 Spin 1/2 oder Rotor (Berichtigung der Messgroesse T1)

- Die Karte nennt die Pfeile "Spin 1/2". Fuer Spin 1/2 gilt sigma+ sigma- != sigma- sigma+. Zwei *ungedrehte*
  Schleifen mit einer gemeinsamen Kante vertauschen dann schon nicht (das Quanten-Spin-Eis ist nicht exakt loesbar) [M].
  "Vertauschen" kann fuer Spin 1/2 also nicht die Frage von T1 sein.
- LW rechnen mit Rotoren: L+- = e^{+-i theta} vertauschen untereinander, (-1)^{L^z} antivertauscht mit L+- derselben
  Kante [S, Gl. 1 und 8]. Fuer diese Algebra ist das Vertauschungsvorzeichen zweier Monome exakt die symplektische Form
  ueber GF(2), mit L+- -> X und (-1)^{L^z} -> Z [M]. Fuer Spin 1/2 gilt dasselbe Vorzeichen fuer alle Paare ohne
  gemeinsame Huepfkante, insbesondere fuer alle Tripel von T2 (drei verschiedene Kanten) [M].
- **Festlegung [F]:** T1 = "das Drehvorzeichen s(A,B) = |E(A) n Z(B)| + |Z(A) n E(B)| mod 2 ist fuer alle Paare 0". Fuer
  Rotoren heisst das: A und B vertauschen. Fuer Spin 1/2 heisst es: Der gedrehte Kommutator ist gleich dem ungedrehten
  (bis auf eine unitaere Z-Kette) [M]. Dazu T1a: jede Schleife aendert kein Q_I.

### 1.2 Ladung ohne Staffelung

- Q_I = rein - raus (orientierte Kanten). Eine geschlossene Schleife mit L+ auf Kanten in Laufrichtung und L- gegen die
  Laufrichtung aendert kein Q_I, auf jedem Graphen, bipartit oder nicht [M]. Der Drehfaktor ist eine Funktion der L^z und
  vertauscht mit allen Q_I. **T1a ist vorab ableitbar**; die Rechnung prueft nur Code und Kantenzuordnung.
- LW brauchen (-1)^I nur, um auf dem bipartiten Gitter eine Orientierung zu haben (alle Kanten von gerade nach
  ungerade) [M].

### 1.3 T2 ist fuer jede generische Projektion vorab ableitbar [M]

- Huepfer an einem Knoten I: L~_a = X_a Z_{T(a)}, T(a) = Beine von a, die die verschobene Kante a' = a + delta_h
  kreuzen. Fuer zwei Kanten a, b an I kann b die Rahmung a' nur nahe I kreuzen (zwei Strecken mit gemeinsamem Endpunkt).
- Misst man Winkel phi ab der Richtung von delta_h, dann kreuzt b die Rahmung a' genau dann, wenn phi_b dasselbe
  Vorzeichen hat wie phi_a und |phi_b| < |phi_a|. Damit ist s(a, b) = 1 genau dann, wenn a und b auf derselben Seite der
  Geraden durch I in Richtung delta_h liegen.
- Der Antivertauschungsgraph an jedem Knoten ist also eine disjunkte Vereinigung zweier Cliquen. Jedes Tripel hat dann
  1 oder 3 antivertauschende Paare, und das Vorzeichen nach Gl. (12) ist (-1)^{s_ij + s_ik + s_jk} = -1. Das gilt fuer
  jeden Grad (4 beim Diamant, 6 kubisch und Pyrochlor) und jede Projektion, solange keine Kante an I parallel zu
  delta_h projiziert wird und keine zwei Kanten an I in dieselbe Richtung fallen.
- Ungedreht (T3) sind alle Z leer: +1 [M].
- Folge: **T2 = -1 und T3 = +1 sind vorab ableitbar**, in beiden Lesarten von 1.4, auf allen drei Netzen, fuer alle
  generischen Projektionen. Der TP3-Teil "unabhaengig von der Projektionsrichtung" ist damit ebenfalls vorab ableitbar.

### 1.4 T1 haengt an der Lesart von Gl. (8); zwei Lesarten [M]

- Gl. (8) zaehlt "the number of times that the link i crosses the curve C'" ueber die Beine von C. Offen ist, ob die
  ganze projizierte Kante zaehlt oder nur ihr Stueck am Knoten von C:
  - **Lesart S (Stummel):** Nur Kreuzungen nahe dem Knoten von C, an dem die Kante Bein ist. Das entspricht Fig. 5
    (Beine als kurze Stummel um die Plakette) und der Aussage, die Phase haenge an den Rotoren "on the links incident to
    vertices I_k along the curve C".
  - **Lesart V (volle Kante):** Jede Kreuzung der ganzen projizierten Beinstrecke mit C' zaehlt.
- **Jordan-Argument:** Zwei geschlossene Kurven der Ebene kreuzen sich gerade oft. Fuer zwei Schleifen A, B mit
  Rahmungen A' = A + delta, B' = B + delta folgt daraus:
  - Lesart S: s(A,B) ist die Paritaet aller Kreuzungen fern von Knoten, gezaehlt einmal als (B-Kante mit A') und einmal
    als (A-Kante mit B'). Jede ferne Kreuzung zweier projizierter Kanten zaehlt also zweimal, s(A,B) = 0. **Lesart S:
    T1b gilt fuer jedes Netz und jede generische Projektion.**
  - Lesart V: s(A,B) ist die Zahl der fernen Kreuzungen, bei denen genau eine der beiden Kanten die andere Schleife
    beruehrt ("gemischte ferne Kreuzungen"), mod 2. Sie haengt nicht von delta ab.
- **Gegenbeispiel Lesart V auf dem kubischen Gitter (LW-Projektion):** p = xz-Plakette (0..1, y = 0, 0..1); r' =
  yz-Plakette (x = 1, y = -1..0, z = 0..1), gemeinsame Kante (1,0,0)-(1,0,1). Die hintere z-Kante von r'
  ((1,-1,0)-(1,-1,1)) liegt projiziert bei x = 0,6 und kreuzt die untere Kante von p. Die untere Kante von p beruehrt r'
  (Knoten (1,0,0)), die z-Kante beruehrt p nicht. Von Hand: E(r') n T(p) = {Kante 6 aus Fig. 5}, E(p) n T_V(r') = leer
  (untere und obere Kante kreuzen r' + delta je zweimal), also s = 1: **in Lesart V antivertauschen p und r'.** In
  Lesart S zaehlt die ferne Kreuzung nicht, die untere Kante von p liegt in T_S(r'), s = 1 + 1 = 0.
  - Fuer jede generische Projektion ueberlappen projiziert zwei Plaketten aus x- und y-Richtung an einer z-Kante; ich
    erwarte deshalb in Lesart V fuer jede Projektion des kubischen Gitters antivertauschende Paare [M, nicht fuer alle
    Projektionen ausgerechnet].
- **Huepfer gegen Schleifen [S: LW verlangen es, S. 6]:** Mit delta_h = -delta_p (LW: Plakette "up and to the left",
  Huepfer "down and to the right") gehen die Kreuzungen von a mit p + delta_p durch Verschiebung eins zu eins in die
  Kreuzungen der p-Kanten mit a + delta_h ueber. Lesart S: s(a, p) = 0 fuer jedes Netz [M]. Lesart V: kann an fernen
  Kreuzungen scheitern.

### 1.5 Ableitbarkeitsprobe zu den Vorhersagen (ausdruecklich)

| Nr | Karte: "vorab ableitbar?" | Schreibtisch (dieser Plan) |
|---|---|---|
| TP0 | ja | Lesart S: ja, eingetroffen erwartet. Lesart V: T1 auf dem kubischen Gitter scheitert erwartbar (Gegenbeispiel 1.4) |
| TP1 | teilweise | **Lesart S: ja, vollstaendig.** Bipartit und Grad 4 spielen keine Rolle: T1a aus der Orientierung (1.2), T2 aus der Zwei-Cliquen-Struktur fuer jeden Grad (1.3), T1b aus dem Jordan-Argument (1.4). Lesart V: nicht hergeleitet |
| TP2 | nein | **Lesart S: ja**, aus 1.2 und 1.4; nicht-bipartit und Dreiecke spielen keine Rolle. Lesart V: nicht hergeleitet, Scheitern erwartet (ferne Kreuzungen an Tetraedern, die projiziert konvexe Vierecke sind) [H] |
| TP3 | nein | ja, in beiden Lesarten (1.3), sofern TP2 eintrifft |

- Was die Rechnung dann noch pruefen kann: den Code, den Nachbau von Fig. 5/6, die Generizitaet der drei Projektionen und
  die beiden Schreibtisch-Argumente selbst (eine einzige antivertauschende Paarung in Lesart S wuerde 1.4 widerlegen).
  Neu ist nur der Lesart-V-Teil.
- **Hauptlesart [F]: Lesart S.** Gruende: (1) nur sie macht LWs eigene Aussagen "Any projection will work" und "(7)
  holds" wahr (Gegenbeispiel 1.4 fuer V); (2) Fig. 5 zeichnet die Beine als Stummel; (3) die Quelle spricht von Rotoren
  "on the links incident to vertices along the curve". Lesart V wird vollstaendig mitgerechnet und mit eigenen Urteilen
  berichtet. Selbstanzeige: Diese Wahl fiel in Kenntnis der Schreibtisch-Erwartung (S besteht, V scheitert an TP0).

## 2. Netze, Orientierung, Schleifen [F]

- **Kubisch (T4):** Knoten Z^3 mod L, L = 3 und 4. Kanten v -> v + e_a (orientiert in +a). Kleinste Schleifen: 3 L^3
  Plaketten v, v+e_a, v+e_a+e_b, v+e_b.
- **Diamant ("durch"):** Einheiten a/4, kubische Zelle Kantenlaenge 4, n x n x n Zellen, n = 2 und 3 (64 bzw. 216
  Knoten). A = {x, y, z gerade, x+y+z = 0 mod 4}, B = A + (1,1,1). Kanten A -> A + d, d in {(1,1,1), (1,-1,-1),
  (-1,1,-1), (-1,-1,1)}, orientiert A -> B. Kleinste Schleifen: alle einfachen 6-Kreise (Tiefensuche in der
  Ueberlagerung, nur zusammenziehbare), erwartet 16 n^3.
- **Pyrochlor-Kanten ("entlang"):** Einheiten a/8, Zelle Kantenlaenge 8, n = 1 und 2 (16 bzw. 128 Knoten). Knoten =
  Mittelpunkte der Diamantkanten A + d (A: alle Koordinaten = 0 mod 4, Summe = 0 mod 8). Kanten = die 6 Kanten jedes
  Tetraeders (um A- und B-Zentren). Orientierung: von s nach t, wenn die erste von 0 verschiedene Komponente von t - s
  (kuerzestes Bild) positiv ist. Kleinste Schleifen: 4 Dreiecke je Tetraeder (erwartet 32 n^3) und alle einfachen
  zusammenziehbaren 6-Kreise (erwartet 16 n^3, die Kagome-Sechsecke).
- Doppelte Schleifen werden ueber ihre Kantenmenge auf dem Torus entfernt. Jede Schleife muss auf dem Torus einfach sein
  (Zaehler "nicht einfach" = 0).
- Huepfer: eine je Kante des Torus. T2: an jedem Knoten alle geordneten Tripel verschiedener Kanten (Diamant 24,
  kubisch und Pyrochlor 120 je Knoten).

## 3. Projektion und Rahmung [F]

- Parallelprojektion pi(r) = S * M r mit ganzzahligem M (2 x 3), S = 2^30. Drei Projektionen fuer alle Netze
  (Fassung nach dem Rauchlauf, Abschnitt 7; Auswahlregel dort nur Generizitaet):
  - P1 "LW-artig, nahe y": M = [[20, 8, 0], [0, 7, 20]], Blickrichtung (-8, 20, -7). Das ist die LW-Projektion fuer
    T4 (y nach rechts oben, kurz: (0,4; 0,35)). Erste Fassung [[10, 4, 0], [0, 3, 10]] war fuer den Diamant nicht
    generisch.
  - P2 "nahe [111]": M = [[11, -10, 0], [6, 0, -5]], Blickrichtung (10, 11, 12) (unveraendert).
  - P3 "schraeg": M = [[9, -5, 0], [17, 0, -5]], Blickrichtung (5, 9, 17). Erste Fassung [[5, -2, 0], [9, 0, -2]]
    (Blickrichtung (2, 5, 9)) war fuer den Diamant nicht generisch.
  - Zwei Matrizen mit demselben Kern geben bis auf eine lineare Abbildung der Ebene dasselbe Bild; Kreuzungen bleiben
    erhalten [M].
- Rahmung jeder Schleife: das projizierte Polygon, verschoben um delta_p = (-5, +4) ("links oben", wie Fig. 5).
  Rahmung jedes Huepfers: die projizierte Kante, verschoben um delta_h = -delta_p = (+5, -4) ("rechts unten", wie
  Fig. 6). |delta| / Kantenlaenge ~ 1e-9.
- Beine einer Kurve: alle Kanten mit einem Endpunkt auf der Kurve (die Kurvenkanten eingeschlossen), in der
  Ueberlagerung gerechnet, dann auf den Torus abgebildet (Z-Mengen per XOR; Zaehler fuer Torus-Zusammenfall).
- Kreuzung: exakter Schnitt zweier Strecken (ganzzahlige Kreuzprodukte). Parameter t entlang der Beinstrecke:
  - nah (zaehlt in S und V): t < 1e-5 an einem Endpunkt, der Knoten der Kurve ist
  - fern (zaehlt nur in V): 1e-3 < t < 1 - 1e-3
  - sonst "unklar" (Zaehler)
- Entartungen (Zaehler, muessen 0 sein): Schnitt genau in einem Streckenendpunkt; kollineare Ueberlappung; an einem
  Knoten zwei Kanten projiziert in dieselbe Richtung; eine Kante parallel zu delta.

## 4. Rechenweg (exakt) [M]

- Operatoren als Bitmengen (X = Huepfkanten, Z = Drehmenge); Paulioperatoren i^k X^x Z^z wie in STRINGENDE-1 fuer die
  Produkte. Keine Gleitkommazahl.
- T1a: je Schleife der Ladungsvektor Delta Q (ganzzahlig) aus Laufrichtung und Orientierung; muss 0 sein.
- T1b: s(A,B) fuer alle Paare der gedrehten kleinsten Schleifen (Lesart S und V).
- T2: je Knoten und geordnetem Tripel (i, j, k): V1 = Phase von L~_i L~_j L~_k gegen L~_k L~_j L~_i (Paulimultiplikation),
  V3 = (-1)^{s_ij + s_ik + s_jk}. V1 = V3 in allen Faellen, sonst "inkonsistent".
- T3: dasselbe ungedreht (Z leer).
- T4: T2 auf dem kubischen Gitter mit P1.
- [Z] Z3: s(a, p) fuer alle Paare (Huepfer, gedrehte Schleife). LW verlangen [L~_i, B~_p] = 0 (S. 6). Ohne diese
  Bedingung waere T2 = -1 nach 1.3 fuer jede Projektion schon gesetzt und saehe nichts.
- [Z] Gegenprobe G1 (Empfindlichkeit von Z3): dieselben Huepfer mit gleichsinniger Rahmung delta_h = +delta_p.
  Erwartung auf dem kubischen Gitter mit P1 [M, von Hand: untere x-Kante von p gegen p]: mindestens ein
  antivertauschendes Paar (Huepfer, Plakette), in Lesart S.
- Kontrastprobe ohne eigene Erwartung im Urteil: Lesart V selbst (zeigt, dass T1b auch "antivertauscht" melden kann).

## 5. Laeufe [F]

- Rauch: kubisch L = 3, Diamant n = 2, Pyrochlor n = 1; alle drei Projektionen; beide Lesarten.
- Haupt: kubisch L = 3, 4; Diamant n = 2, 3; Pyrochlor n = 1, 2; alle drei Projektionen; beide Lesarten.
- Ausgabe je (Netz, Groesse, Projektion, Lesart): Zahlen der Schleifen, Paare, antivertauschenden Paare, T2-/T3-
  Vorzeichen, Inkonsistenzen, Entartungen, unklare Kreuzungen, Torus-Zusammenfaelle, Z3 und G1, und die ersten fuenf
  antivertauschenden Paare als Beispiele.

## 6. Urteilsregeln (mechanisch in code/auswertung.py)

- Moegliche Urteile: "eingetroffen", "nicht eingetroffen", "nicht auswertbar", bei TP3 zusaetzlich "entfaellt"
  (Bedingung TP2 nicht erfuellt).
- Bausteine je (Netz, Groesse, Projektion, Lesart):
  - generisch: Entartungen = 0 und unklare Kreuzungen = 0
  - T1 ok: T1a (Delta Q = 0 fuer alle Schleifen, alle Schleifen einfach) und T1b (0 antivertauschende Paare)
  - T2 ok: alle V1 = -1 und 0 Inkonsistenzen; T3 ok: alle V1 = +1 und 0 Inkonsistenzen
  - Z3 ok: 0 antivertauschende Paare (Huepfer, Schleife)
  - Inkonsistenz V1/V3 irgendwo im betroffenen Teil oder nicht generisch -> "nicht auswertbar"
- **Nach Plan** (je Lesart; Hauptlesart S):
  - TP0: eingetroffen genau dann, wenn T3 ok fuer alle Netze, Groessen und Projektionen, und auf dem kubischen Gitter mit
    P1 fuer L = 3 und 4: T2 ok (T4), T1 ok, Z3 ok. "nicht auswertbar", wenn kubisch-P1 nicht generisch ist, eine
    Inkonsistenz auftritt oder G1 (kubisch, P1, L = 4, Lesart S) kein antivertauschendes Paar zeigt.
  - TP1: "nicht auswertbar", wenn TP0 (gleiche Lesart) nicht eingetroffen ist. Sonst eingetroffen genau dann, wenn es
    eine Projektion gibt, fuer die beim Diamant n = 2 und 3 generisch sind und T1 ok, T2 ok und Z3 ok gelten. Ist keine
    Projektion generisch: "nicht auswertbar".
  - TP2: Sperre wie TP1. Eingetroffen genau dann, wenn es eine Projektion gibt, fuer die beim Pyrochlor n = 1 und 2
    generisch sind und T1 ok gilt.
  - TP3: "entfaellt", wenn TP2 (gleiche Regelart und Lesart) nicht eingetroffen ist. Sonst eingetroffen genau dann, wenn
    beim Pyrochlor fuer alle drei Projektionen und n = 1, 2 T2 ok und Z3 ok gelten; eine nicht generische Projektion
    macht TP3 "nicht auswertbar".
- **Nach Kartenwortlaut** (je Lesart): ohne Z3, ohne G1-Sperre und ohne Kontrollsperre durch TP0:
  - TP0: T3 ok ueberall, T2 ok kubisch-P1 (L = 3, 4), T1 ok kubisch-P1 (L = 3, 4).
  - TP1: es gibt eine Projektion mit T1 ok und T2 ok beim Diamant (n = 2 und 3).
  - TP2: es gibt eine Projektion mit T1 ok beim Pyrochlor (n = 1 und 2).
  - TP3: "entfaellt", wenn TP2 (Wortlaut, gleiche Lesart) nicht eingetroffen; sonst T2 ok beim Pyrochlor fuer alle drei
    Projektionen und n = 1, 2.
  - Nicht generisch oder inkonsistent: "nicht auswertbar" wie oben.
- Schreibtisch-Erwartung (Abschnitt 1, vor jeder Rechnung): Plan-S und Wortlaut-S: TP0 bis TP3 eingetroffen. Plan-V:
  TP0 nicht eingetroffen, TP1 und TP2 nicht auswertbar, TP3 entfaellt. Wortlaut-V: TP0 nicht eingetroffen; TP1, TP2
  nicht hergeleitet (Scheitern erwartet [H]).
- Wirkung des Rauchlaufs: keine. Er prueft nur, ob der Code laeuft. Was er zeigt, steht in Abschnitt 7.

## 7. Rauchlauf [R]

- **Laeufe** (.69, kleintest.sh, Spur cpu6; Zeiten aus den Starter-Zeilen, UTC + 2 h = CEST; alle rc = 0, je < 1 s
  Rechenzeit; kubisch L = 3, Diamant n = 2, Pyrochlor n = 1):
  - rauch 11:59:56 bis 11:59:57 und Auswertung 12:00:02: erste Fassung (P1 = [[10,4,0],[0,3,10]], P3 = [[5,-2,0],[9,0,-2]]).
  - rauch2 12:00:45 bis 12:00:46: dieselbe Fassung, dazu Beispielliste der unklaren Kreuzungen (nur Diagnose; die
    Liste gibt t als Gleitkomma-Text aus, kein Urteil haengt daran).
  - rauch3 12:03:03 bis 12:03:04 und Auswertung: P1 = [[20,8,0],[0,7,20]], P3 = [[7,-3,0],[13,0,-3]].
  - kandidaten 12:03:53 bis 12:03:54 (code/kandidaten.py): fuenf P3-Kandidaten, nur Entartungs- und Unklar-Zaehler.
    Regel vorab im Skript: der erste generische Kandidat der Liste. Ergebnis: (5, 9, 17) generisch auf allen drei
    Netzen; (3, 8, 14), (2, 9, 13), (7, 4, 15) je 128 unklare Kreuzungen beim Diamant; (6, 11, 19) generisch.
  - rauch4 12:04:06 bis 12:04:07 und Auswertung: endgueltige Fassung (Abschnitt 3). Ausgaben in rauch-69/.
- **Codeaenderungen vor dem Einfrieren:**
  - auswertung.py: Groessenliste umschaltbar (Argument "rauch" nur fuer den Codetest; der Hauptlauf ruft ohne es auf).
  - twist_pyro.py: Diagnoseliste unklarer Kreuzungen; P1 und P3 ersetzt.
  - Grund fuer P1/P3: Beim Diamant lagen im ersten Rauchlauf je 128 Kreuzungen im unklaren Band. Ursache (Diagnose):
    exakte Projektionszufaelle. Beispiel P1 alt: Knoten (0,0,0) liegt projiziert genau auf der Kante (2,-2,0)-(1,-3,1)
    desselben Sechsecks; (-2,2,0) = 6/7 (-1,-1,1) + 2/7 (-4,10,-3). Das ist keine generische Projektion; die Plan-Regel
    haette diese Projektionen ohnehin ausgeschlossen. Keine Schwelle, keine Urteilsregel und keine Vorhersage wurde
    geaendert.
- **Gesehen, offengelegt (rauch4, endgueltige Fassung):**
  - Zaehlungen wie erwartet: kubisch 81 Plaketten; Diamant 128 Sechsecke; Pyrochlor 32 Dreiecke und 16 Sechsecke.
    T1a-Fehler 0, nicht einfache Schleifen 0, Mehrfachkanten 0, Torus-Zusammenfaelle 0, Entartungen 0, unklare
    Kreuzungen 0 in allen neun (Netz, Projektion)-Paaren.
  - T3: +1 in allen Tripeln (3240, 1536, 1920). T2: -1 in allen Tripeln, in beiden Lesarten, alle Projektionen.
  - Lesart S: 0 antivertauschende Schleifenpaare, 0 antivertauschende (Huepfer, Schleife)-Paare, ueberall.
    G1 (gleichsinnige Huepferrahmung): 972 (kubisch), 1152 bis 1536 (Diamant), 512 (Pyrochlor) antivertauschende Paare.
  - Lesart V: antivertauschende Schleifenpaare 216 (kubisch, jede Projektion), 384 bis 640 (Diamant), 48 bis 64
    (Pyrochlor: Dreieck-Sechseck und Sechseck-Sechseck, kein Dreieck-Dreieck); Huepfer-Schleife 108, 256 bis 320,
    48 bis 72.
  - Huepfer haben nie ferne Kreuzungen (0 in allen Faellen), wie in 1.3 hergeleitet.
  - Rauch-Auswertung mit den kleinsten Groessen: Plan-S und Wortlaut-S TP0 bis TP3 eingetroffen; Plan-V TP0 nicht
    eingetroffen, TP1/TP2 nicht auswertbar, TP3 entfaellt; Wortlaut-V TP0 bis TP2 nicht eingetroffen, TP3 entfaellt.
    Alles wie die Schreibtisch-Erwartung in Abschnitt 6.
- **Folge:** Der Rauchlauf aendert weder Vorhersagen, Schwellen noch Urteilsregeln. Plan und Code werden in dieser
  Fassung eingefroren.
- **Selbstanzeige bis zum Einfrieren:** Lokal ausser der erlaubten Liste nur Anzeige- und Dateibefehle: wc, pdfinfo,
  head, tr, ls, cat. Kein Interpreter lokal; auf der .69 nur mkdir, mv, ls, cat, grep, tail, sha256sum ausserhalb des
  Starters.
