# ARBEITSFELD DREIECK-PUMPE-L (feldforscher, eine Arbeitsdatei, vor jedem Schritt neu lesen)

- Start feldforscher: 2026-10-04 18:12:19 CEST (date). Zeitbox 75 min.
- Gestrichenes bleibt stehen und wird ~~so~~ markiert. Offene Rueckfragen stehen unten und wandern mit.
- Kennzeichen wie KARTE.md: [S] (mit Zeile), [S Abstract], [P], [L], [L?], [M], [ES], [H].

## 0. Gelesene Projektdateien (18:12 bis 18:13, date-Rahmen oben)

- KARTE.md ganz.
- AGENTS.md Z. 127-138 (Dimensionsvergleich).
- RUNDE-34/eis-1/ERGEBNIS.md ganz: Pyrochlor-Stabnetz isostatisch, 12 L^2 Eigenspannungen auf geraden <110>-Linien,
  ebenso viele Nullmoden; Sun/Souslov/Mao/Lubensky 2012 dort nur [L?, nicht nachgelesen].
- RUNDE-37/tetraeder-l/DOSSIER.md Z. 80-125: Lubensky u. a. 2015 Indexsatz [S Abstract], Pyrochlor z = 6 = 2d,
  Stenull/Kane/Lubensky 2016 "Weyl lines in their bulk phonon spectra" [S Abstract].
- RUNDE-37/kopplung-tetra-1/ERGEBNIS.md: RUM-Ebenen = Tensor-Eis-Ebenen; Wegner 2007 [S]; Hammonds u. a. 1996;
  Gamma: 6 RUM (3 Translationen, 3 gegenlaeufige Drehungen); Ring-Holonomie kostet nach Relaxation nichts.
- RUNDE-23/kugelschale-1/ERGEBNIS.md: Dreieckskugel -> Ikosaeder, 12 Fuenfer-Ecken; Lidmar/Mirny/Nelson 2003 [L?].
- RUNDE-37/atem-netz-1/KARTE.md (nur gelesen): atmende Punkte, Huellkopplung = XY-Antiferromagnet; AN4 Pumpen.
- RUNDE-42/SCHALTER-UND-ATMEN.md B2: "Einen Umlauf gibt es nur mit einem eigenen Wert je Kante."

## 1. Schreibtischpruefung (eigene, vor jedem Abruf; Kopfrechnung, keine lokale Rechnung) [M]

Geschrieben zwischen 18:13:17 und 18:21:27 (beide per date), vor F1. ~~Notiert ab 18:15~~ (geschaetzte Zeit,
gestrichen; Selbstanzeige).

- **SP1 (wichtigster Fehler, Abschnitt 1, letzter Unterpunkt):** "Die Kante bekommt einen eigenen Wert, den Faltwinkel ...
  genau so ein eigener Kantenwert fehlte B2 und GLUONEN-L." Das stimmt im Sinn von B2 nicht.
  - Der Faltwinkel ist die relative Drehung der beiden starren Dreiecke, also eine Funktion von O_i^-1 O_j (O = Lage des
    Dreiecks). Das ist reine Eichung wie GLUONEN-L V2; das Ringprodukt um jede Ecke ist identisch 1 (Schliessbedingung des
    Netzes).
  - "Folgt nicht aus den Ecken" gilt nur fuer die zwei geteilten Ecken; aus den Lagen der vier Ecken folgt er
    (Spitzenabstand sqrt(3) sin(theta/2)).
  - Einen echten Umlauf (Holonomie ungleich 1) um eine Ecke gibt es nur als Winkeldefizit, und das legen die
    Kantenlaengen fest (Regge), nicht die Faltwinkel. Gleichseitig: gequantelt in 60-Grad-Stufen (Disklination);
    ungleich grosse Dreiecke: stufenlos. Der "eigene Kantenwert mit Umlauf" ist also die Kantenlaenge, nicht der
    Faltwinkel [M, ES].
- **SP2 (Abschnitt 2, letzter Unterpunkt):** "starr werden sie erst mit geschlossenen Schalen" ist fuer "jede Ecke in
  zwei" falsch. Geschlossene Schalen aus eckenteilenden Dreiecken sind wackelig: V = 3F/2, E = 3F, also 3V - E - 6 =
  1,5 F - 6 innere Freiheitsgrade; Kuboktaeder (F = 8): 6, Ikosidodekaeder (F = 20): 24 [M]. Die symmetrische Drehung
  des Kuboktaeders ist Fullers "Jitterbug" [L]. Starr (generisch) werden geschlossene Schalen erst, wenn sich die
  Dreiecke Kanten teilen (Triangulation, E = 3V - 6; Gluck 1975 [L?]).
  - Allgemein [M]: Ein starres Dreieck hat in D Dimensionen 3D - 3 Freiheitsgrade (2D: 3, 3D: 6). Liegt jede Ecke in n
    Dreiecken, kostet das je Dreieck 3 D (n - 1)/n Bedingungen. Ausgleich bei n = D: 2D n = 2 (Kagome), 3D n = 3, 4D
    n = 4. Fuer D-Simplexe stimmt die Karte: n = 2 in jeder Dimension.
- **SP3 (Abschnitt 1, Tetraeder-Schritt):** Wechsel des Bindungsmodells. Schritte 1 und 2: Binden = Ecken fallen
  zusammen (Kugelgelenk). Der Tetraeder-Schritt: Spitzen im Abstand 1 PU "binden" = neuer Stab (Punkte mit Durchmesser
  1 PU beruehren sich). Im reinen Zusammenfall-Modell entsteht aus zwei Dreiecken kein Tetraeder (dritte Bindung legt
  sie aufeinander, wie die Karte selbst sagt). Zwei Modelle = zwei Regime; die Karte muss sagen, welches Finn meint [M].
- **SP4 (Abschnitt 1, nur Wortwahl):** theta in sqrt(3) sin(theta/2) ist der Innen-Diederwinkel (180 Grad = flach).
  arccos(1/3) = 70,53 Grad ist der Diederwinkel des Tetraeders, richtig. Im Origami-Sprachgebrauch heisst
  "Faltwinkel" die Abweichung von flach, hier 109,47 Grad [M]. Rechnung: d = 1 heisst sin^2(theta/2) = 1/3, cos theta =
  1 - 2/3 = 1/3. Stimmt.
- **SP5 (Abschnitt 1, Zaehlung):** 12 - 3 - 2 = 7, minus 6 = 1: stimmt [M]. Die zweite Bindung zaehlt nur 2, weil beide
  Dreiecke dieselbe Kantenlaenge haben. Bei ungleich grossen Dreiecken ist die zweite Eckbindung ohne Dehnung
  unmoeglich: Ungleiche gleichseitige Dreiecke koennen sich nur Ecken teilen, keine Kanten (Frage 3) [M].
- **SP6 (fehlendes 2D-Gegenstueck zu Abschnitt 1):** In 2D: 6 - 2 = 4, minus 3 = 1. Schon eine geteilte Ecke ist ein
  Scharnier (eine relative Drehung). Zwei geteilte Ecken: 6 - 2 - 1 - 3 = 0, starr, mit zwei diskreten Lagen (Raute
  oder aufeinander). Der Faltwinkel ist in 2D diskret (0 oder 180 Grad), erst in 3D stufenlos [M].
- **SP7 (Abschnitt 3):** Defizite stimmen: n = 5: 12 x 60 = 720; n = 4: 6 x 120 = 720; n = 3: 4 x 180 = 720; n = 7:
  -60 [M]. Aber: Das gilt fuer kantenteilende Netze (Triangulationen). Im eckenteilenden Netz (Kagome, Pyrochlor) liegt
  jede Ecke in genau zwei Dreiecken; dort sitzt die Kruemmung in den Loechern: Sechseck flach (60+60+120+120 = 360),
  Fuenfeck: Ikosidodekaeder (30 Ecken x 24 Grad = 720), Viereck: Kuboktaeder (12 x 60 = 720), Siebeneck: Sattel [M].
- **SP8 (Abschnitt 4, Dimension):** Kagome: gleichfoermige Gegendrehung (oben +alpha, unten -alpha) ist ein exakter
  endlicher Mechanismus, Gitter schrumpft isotrop um cos alpha [M]. Vom geraden Kagome aus ist das zweite Ordnung,
  im verdrehten erste Ordnung (daher Kompressionsmodul null erst im verdrehten).
  - 3D [M]: Bei geteilter Ecke mit Inversion (gerades Si-O-Si) wird jeder Mitte-Mitte-Vektor d = 2u zu (R_A + R_B) u.
    Verformung F = (R_A + R_B)/2. Isotrop (F = lambda Q) verlangt sym(R) = lambda I fuer eine Drehung; in 3D hat jede
    Drehung eine feste Achse, also lambda = 1. **Finns Netz kann nicht gleichfoermig isotrop atmen**: Die
    Gegendrehung um eine Achse n gibt F = cos phi (I - n n^T) + n n^T, also Schrumpfen nur quer zur Achse
    (tetragonal, Volumen cos^2 phi). In 2D (R + R^T = 2 cos alpha I) und 4D (isokline Drehung) geht es.
  - Thermisch, ueber drei Achsen gemittelt, ist das Schrumpfen im Mittel isotrop [M]. "Cristobalit schrumpft beim
    Erwaermen" bleibt [L], nicht geprueft (Gegensweep-Kandidat).
- **SP9 (Abschnitt 5c):** "Ungleiche Kantenlaengen ... die Ecken bekommen Winkeldefizite" gilt nur generisch und nur im
  kantenteilenden Netz. Eine ebene Triangulation mit ungleichen Dreiecken ist flach (Defizit 0). Zufaellige Laengen:
  in einer freien Haut Kruemmung (Beulen, KUGELSCHALE-1), in der Ebene eingesperrt Frustration/Spannung. Im
  eckenteilenden Netz bleiben ungleich grosse Dreiecke flach ("Breathing Kagome": grosse und kleine Dreiecke im
  Wechsel) [M].
- **SP10 (Abschnitt 5a, Vermutung zum Pruefen):** Breathing Kagome aus gleichseitigen Dreiecken zweier Groessen ist
  C3-symmetrisch. Eine topologische Polarisation R_T (ein Gittervektor) muesste C3-invariant sein, also null. Ungleiche
  Groesse allein polarisiert dann nicht; dafuer muss die Dreiecksform die C3-Symmetrie brechen [ES, zu pruefen an
  Kane/Lubensky].

## 2. Projekt-grep (18:13:05 bis 18:13:17 Zaehlung, danach Zeilen; Ausschluesse: vertraege-20260925, *ks-1*,
##    *KS-1*, ks-1-dk-lauf(e), *VERSIEGELT*, T8-SOLL-*, .git, dieser Ordner)

- Treffer (Dateien, nur .md/.txt): Kagome 22, Guest 7, Hutchinson 2, Lubensky 17, Rocklin 0, Thouless 17, Pumpe 149,
  Origami 3, Janus 3, Kapsid 11, Regge 227.
- **Guest/Hutchinson:** nur RUNDE-42.md Z. 573 (diese Karte) und fremde Treffer (Schenk/Guest Miura 2013 in
  parallel-pruefungen-20260910/.../miura/; Hutchinson in einem Quantenkaskadenlaser-Zitat). Kein Guest-Hutchinson im
  Projekt.
- **Rocklin:** 0. Transformierbare Polarisation ist im Projekt nicht gelesen.
- **Kane/Lubensky 2014 (arXiv:1308.0554):** im Projekt als Motivation, "Primaerabstract gelesen"
  (fourier-round3-20260927/EDGE-VORAB.md Z. 3; dort eine selbst gebaute Kette mit Randnullmode, a/b-Tausch schiebt sie
  auf die andere Seite); auch resonance-20260930/concept-review-tus/TETRAEDER-ARXIV-20261001.txt A3 und
  fourier-round2-20260927/ANALOGIE-IDEATION.md Z. 83. **Keine lokale Kopie des Abstracts gefunden** -> F1 darf ihn holen.
- **Lubensky u. a. 2015:** lokal in RUNDE-37/tetraeder-l/quellen/F11-api-regime-packung.xml (Abstract gelesen 18:14):
  "modifications to the periodic kagome lattice can eliminate all but trivial translational zero modes and create
  topologically distinct classes" [P, dort S Abstract]. Sagt nichts zu Guest-Hutchinson -> E1 bleibt offen.
- **Kagome:** EIS-1 (Linien-Eigenspannungen [L?]), FLUSS-1 (Kagome-Eis), LADUNG-MONOPOL-2 (Kagome-Sechsecke),
  KOPPLUNG-TETRA-1 (Sechserring), GLUONEN-L (Biexzitonen-Kagome, Wabengitter : Kagome = Diamant : Pyrochlor).
- **Thouless/Pumpe:** ideen-20260916/ANALOGIE-SPIELTISCH.md Z. 105 (Thouless-Pumpe allgemein); QWEN-ROH: "Pumpe" dort
  kein Invariant; QCA-WINDUNG-1 (spinselektive Thouless-Pumpen, Quantenwalk); RUNDE-42/SCHALTER-UND-ATMEN.md D4
  ("Gleichtakt allein pumpt nichts", Purcell; Shapere/Wilczek; tetra-ticks-Spielzeug); ATEM-NETZ-1 AN4. **Keine
  mechanische Thouless-Pumpe in Maxwell-Gittern im Projekt.**
- **Origami/Kapsid:** parallel-pruefungen-20260910/natur-mechanismen/NATUR-ABGLEICH.md Z. 18-24: Wei u. a.
  (arXiv:2310.18790, PNAS 2024): DNA-Origami-Experimente plus Modell fuer ein T = 3-Kapsid aus 60 Bausteinen;
  ungleiche Bindungsaffinitaeten beguenstigen Dimer-/Pentamer-Zwischenstufen [P]. RUNDE-27/quellen/2512.11562.txt
  (Meiri/Efrati, kumulative geometrische Frustration) zitiert Berengut u. a. 2020 (selbstbegrenzende Polymerisation von
  DNA-Origami mit Dehnungsaufbau), Videbaek u. a. 2024 (selbstschliessende Strukturen), Hagan/Grason RMP 2021 [P,
  nur Literaturliste]. RUNDE-05/06 Bio 46 "Kapsid" = Ring aus Q-Baellen, kein Dreiecksbezug.
- **Janus:** keine Janus-Kolloide im Projekt (nur Namen).
- **Regge:** viel (REGGE-4D-1, GRAVITON-NETZ-L, REGGE-RAND-1, DREIECK-LINSE-1); RUNDE-16/stabil-6-8-12/KARTE.md Z. 44
  hat das Defizit 2 pi - N pi/3 schon.
- **Atmendes Pyrochlor:** TETRAEDER-L Frage 2 zitiert Yan u. a. 2020 (Rang-2-U(1) "auf dem atmenden Pyrochlor") [P].
  Das "Breathing"-Pyrochlor (abwechselnd grosse und kleine Tetraeder) ist also im Projekt schon als Name da.

## 3. Abrufprotokoll (Erwartung VOR Abruf, mit date)

Zaehlung: jeder curl-Aufruf ins Netz = ein Abruf (Grenze 10). Lokale Kopie je Abruf in quellen/.

- **F1, Erwartung geschrieben 18:21:27 (date) bis vor dem Abruf.** arXiv-API, Titelsuche (OR) nach drei Arbeiten:
  Kane/Lubensky "Topological boundary modes in isostatic lattices" (E2), Rocklin u. a. "Transformable topological
  mechanical metamaterials" (E3, E1 teilweise), Chen/Upadhyaya/Vitelli "Nonlinear conduction via solitons ..." (E6).
  Erwartung: (a) Kane/Lubensky: Polarisation aus der Geometrie, verformtes Kagome, Nullmoden an einem Rand bzw. an
  Domaenenwaenden. (b) Rocklin: eine weiche gleichfoermige Verformung ("Guest"- oder Guest-Hutchinson-Mode) schaltet
  die Polarisation um; Kantensteifigkeit aendert sich stark. (c) Chen u. a.: Soliton in der topologischen Kette traegt
  die Nullmode von einem Ende zum anderen; mechanischer Prototyp. Keine Aussage ueber Pumpen im Thouless-Sinn.
- **F1 ausgefuehrt 18:21:59 bis 18:22:00 (date): leer** (0 Byte; http ohne Weiterleitung). Zaehlt als Abruf 1
  (Selbstanzeige). Lokale Kopie F1-api-kane-rocklin-chen.xml (leer).
- **F2 = F1 wiederholt, https mit -L, 18:22:07 bis 18:22:08 (date):** HTTP 200, 3 Eintraege. Kopie
  quellen/F2-api-kane-rocklin-chen.xml (+ F2-header.txt).
  - (c) Chen/Upadhyaya/Vitelli, arXiv:1404.2263, PNAS 111, 13004 (2014): **bestaetigt** (E6). Z. 67: "the soft motion,
    initially localized at the edge, can in fact propagate unobstructed all the way to the opposite end"; "moving
    domain walls between distinct topological mechanical phases"; "transporting a mechanical state from one location to
    another" [S Abstract].
  - (a) Kane/Lubensky, arXiv:1308.0554, Nat. Phys. 10, 39 (2014): **teilweise.** Z. 45: Randmoden "localized at their
    boundary", "topological origin", "new topological bulk mechanical phases with distinct boundary modes", Modelle "in
    one and two dimensions". **Kagome und "Polarisation" stehen nicht im Abstract.** E2-Kern (Polarisation aus der
    Geometrie, ein Rand) damit nicht an der Quelle gelesen.
  - (b) Rocklin/Zhou/Sun/Mao, arXiv:**1510.06389** (nicht 1510.04970 wie erinnert), Nat. Commun. 8, 14201 (2017):
    **Verstoss (klein) gegen die Erwartung im Wortlaut.** Z. 16: "a uniform soft deformation of the whole structure, to
    allow metamaterials to be immediately and reversibly transformed between states with contrasting mechanical and
    acoustic properties"; "We discuss the general classification of all structures that exhibit such soft
    deformations"; "edge stiffness and speed of sound". Kein "Guest-Hutchinson", kein "Polarisation" im Abstract.
    "Klassifikation aller Strukturen, die solche weichen Verformungen zeigen" deutet an: nicht jedes Maxwell-Gitter hat
    sie -> E1 wackelt. Volltext noetig (F3).
- **F3, Erwartung geschrieben 18:22:47 (date), vor dem Abruf.** Volltext Rocklin u. a. 1510.06389v1 (PDF, pdftotext).
  Erwartung: (1) Begriff "Guest mode" bzw. "Guest-Hutchinson mode" mit Zitat Guest/Hutchinson 2003; die Aussage, dass
  periodische Maxwell-Gitter unter periodischen Randbedingungen mindestens d Eigenspannungen haben, aber eine weiche
  makroskopische Verformung **nicht immer** (nur eine Klasse; das waere Verstoss gegen E1 im Wortlaut). (2) Verformtes
  Kagome als Beispiel; die Guest-Mode dreht die Dreiecke gegeneinander und schaltet die topologische Polarisation R_T
  um (E3). (3) Keine zyklische Pumpe; hoechstens "reversibel". (4) Ein Wort zu 3D oder zu Pyrochlor eher nicht.
- **F3 ausgefuehrt 18:23:03 bis 18:23:04 (date):** PDF 7 Seiten, quellen/F3-rocklin-1510.06389v1.pdf, Text
  F3-rocklin-1510.06389v1.txt (pdftotext -layout, 556 Zeilen; Zeilennummern unten = dieser Text). Gelesen 18:23 bis
  18:24:26.
  - (1) **Verstoss gegen meine Zwischenerwartung, E1 haelt:** Z. 272-280 (Methods, rechte Spalte): "all lattices with
    <z> = 2d (Maxwell lattices) must have d(d - 1)/2 homogeneous deformations that are of zero energy. For 2D lattices
    ... Maxwell lattices have at least one such soft deformation (which we name the uniform soft twisting). These floppy
    modes have also been called 'Guest modes' [15, 16]." [15] = Guest/Hutchinson, J. Mech. Phys. Solids 51, 383 (2003);
    [16] = Lubensky u. a. 2015. Z. 252-258: "2D structures satisfying <z> = 2d must have at least one uniform soft
    twisting ... even with arbitrarily chosen shapes of triangles". Die "Klassifikation" des Abstracts meint die zwei
    Regime (Dilatation det > 0, Scherung det < 0), nicht welche Gitter die Mode haben.
    - Eigene Nachrechnung [M]: Einheitszelle n Ecken, nd Freiheitsgrade + d^2 (Verformung F), nd Staebe: d^2 Nullmoden,
      minus d Translationen, minus d(d-1)/2 Drehungen = d(d-1)/2. **3D: drei Guest-Moden** = die drei gegenlaeufigen
      Gamma-Drehungen von KOPPLUNG-TETRA-1 [P]. Passt.
  - (2) E3 **bestaetigt, genauer:** Abb. 1a (Z. 71-75): "Two types of triangles (red and blue) are connected by free
    hinges at their corners, forming a deformed kagome lattice"; "3 critical angles ... where sides of the triangles form
    straight lines ... and topological polarization RT ... changes". Z. 234-242: R_T "points to an edge that gains extra
    floppy edge modes"; Folge "0 -> (a2 - a1) -> a2 -> 0"; "stiff edges in the direction of -RT". Z. 216-230: Kantensteifigkeit
    steigt "by orders of magnitude as floppy modes leave the edge" (Rechnung, 60 x 60, konjugierte Gradienten; kein
    Experiment). Z. 202-206: "deformed" heisst Dreiecke anderer Form als im regulaeren Kagome, nicht gedehnt.
  - (3) Regulaeres verdrehtes Kagome (Ref. [18] = Sun u. a. 2012): Z. 124-131 "the uniform soft twisting is a pure
    dilation" (eps_xy = 0, eps_xx = eps_yy), "emergent conformal symmetry". Das bestaetigt Kartenabschnitt 4 fuer gleiche
    Dreiecke [S].
  - (4) **Finns Bild steht woertlich als Vorschlag drin:** Z. 279-286: "If tip-to-tip attraction between polygon
    (colloidal/nano) particles can be realized, an extended periodic 2D lattice may be self-assembled ... binding sites at
    the tips can serve as flexible hinges". 2015 also Vorschlag, nicht gebaut.
  - (5) Keine Pumpe, kein 3D; "reversibly transformed" (Abstract). RUMs "argued to be responsible for negative thermal
    expansion in some crystals [47, 48]" (~~Z. 289-295~~ Z. 288-293; [47] Hammonds u. a. 1996) [S]; Cristobalit selbst nicht genannt.
  - Karte 5(a) "alle weichen Moden an einen Rand" ist zu stark: Die Quelle sagt "extra floppy edge modes" an einer Seite,
    steife Kanten in Richtung -R_T [S Z. 234-242].
- **F4, Erwartung geschrieben 18:24:56 (date), vor dem Abruf.** arXiv-API, Relevanz, alle Jahre: (ti:pump OR
  ti:pumping) AND abs:topological AND (abs:mechanical OR abs:elastic OR abs:phononic OR abs:metamaterial), bis 20
  Treffer. Erwartung (E4): Rosa/Pal/Arruda/Ruzzene 2019 "Edge states and topological pumping in spatially modulated
  elastic lattices" (raeumliche Modulation, Randzustand wandert ueber die Kette), dazu zeitliches Pumpen in
  magneto- oder elektromechanischen Wellenleitern (Grinberg u. a. 2020, Xia u. a. 2021). Alle mit modulierten Federn
  oder Massen in Gittern mit Luecke bei endlicher Frequenz, **keines** mit der Guest-Mode eines Maxwell-Gitters als
  Pumpparameter. Falls doch eines mit Maxwell-/Kagome-Gitter und Nullmoden pumpt: Verstoss, voll lesen.
- **F4 ausgefuehrt 18:25:13 (date, Start und Ende in derselben Sekunde):** 61 Treffer, die ersten 20 in
  quellen/F4-api-mech-pumping.xml. Gelesen bis 18:25:52.
  - E4 **bestaetigt** (mit anderer Quelle als erinnert): Xia, Riva, Rosa, Cazzulani, Erturk, Braghin, Ruzzene,
    arXiv:2006.07348, PRL 126, 095501 (2021): "a smooth temporal variation of the modulation phase drives the transfer
    of edge states from one boundary of the waveguide to the other" (Experiment, Aluminiumbalken mit Piezo-Flecken)
    [S Abstract]. Grinberg u. a., arXiv:1905.02778: "the first temporal topological pump that produces on-demand, robust
    transport of mechanical energy using a 1D magneto-mechanical metamaterial" [S Abstract]. Rosa u. a. 2019 nicht unter
    den ersten 20; nicht gebraucht.
  - **Verstoss V-F4a (Faltwinkel als Pumpparameter gibt es):** Li, Kevrekidis, Mao, Yang, arXiv:2401.09668 (Jan. 2024),
    "Topological pumping in origami metamaterials": "topological pumping in origami metamaterials with spatial
    modulation by tuning the rotation angles"; Pumpen von Wellen "from one topological edge state to another" ueber
    gekoppelte Origami-Ketten als synthetische Dimension; Nichtlinearitaet lokalisiert wie "discrete breathers" [S
    Abstract]. Einordnung: raeumliche Modulation von Winkeln, Wellen bei endlicher Frequenz, kein zeitliches Atmen,
    keine Nullmoden. Erwartung korrigiert: Winkel (Origami) koennen Pumpparameter sein, aber bisher nur als Muster im
    Raum (Theorie/Rechnung).
  - **Verstoss V-F4b (gepumpt wird ein Soliton, und es braucht Reibung):** Juergensen, ..., Rechtsman, arXiv:2502.14046
    (Feb. 2025), "Quantized dynamical pumping via dissipation in a mechanical Thouless pump": gekoppelte Pendel
    (Frenkel-Kontorova), "quantized non-adiabatic Thouless pumping using topological kink solitons"; "the pump is
    non-adiabatic and dissipation is necessary"; Quantisierung "cannot be described by the Chern number"; Experiment mit
    Defekt [S Abstract]. Erwartung korrigiert: Die naechste mechanische Pumpe zu Finns Bild transportiert eine
    Verformungsfront (Kink) je Zyklus um einen festen Schritt; das verbindet E4 mit E6 (Chen u. a. 2014: Soliton =
    wandernde Domaenenwand). Voller Zyklus: siehe Abschnitt 4 (V2).
  - Keiner der 20 Treffer nutzt die Guest-Mode eines Maxwell-Gitters zum Pumpen (Titel und Abstracts der mechanischen
    Treffer gelesen: 2401.09668, 1905.02778, 2006.07348, 2502.14046; ~~uebrige nach Titel nicht mechanisch oder
    Quanten~~ berichtigt 18:26: auch 2303.04111, 2005.14066, 2402.09958, 1911.02567 per Abstract gelesen: modulierte
    Steifigkeit, Resonatoren oder Phason, Wellen bei endlicher Frequenz. grep ueber die ganze Datei nach maxwell,
    kagome, floppy, zero mode, guest, isostatic: keine Treffer ausser origami).
- **F5, Erwartung geschrieben 18:26:27 (date), vor dem Abruf (Regel 7, 24 Monate).** arXiv-API, submittedDate
  2024-10-04 bis 2026-10-04: (abs:Maxwell OR abs:isostatic OR abs:kagome OR abs:floppy OR abs:"Guest mode" OR
  abs:"soft twisting") AND (abs:pump OR abs:pumping OR abs:Thouless). Erwartung: wenige Treffer (0 bis 8), meist
  Kagome-Elektronik/Photonik ("pump" als Laser-Pumpen); **keine** Arbeit, die Nullmoden eines Maxwell-Gitters ueber
  einen Zyklus der Guest-Mode pumpt. Dann lautet das Urteil zu "Pumpen durch gleichmaessiges Atmen": nach
  Recherchestand nicht belegt (nicht "widerlegt").
- **F5 ausgefuehrt 18:26:40 (date):** 38 Treffer, alle in quellen/F5-api-maxwell-pump-24m.xml. **Bestaetigt.** Treffer
  sind Maxwell-Gleichungen/Maxwell-Bloch, elektronische Kagome-Stoffe, BKT ("Thouless"), Laser-"pump". Kein Treffer
  zu Pumpen mit Nullmoden oder Guest-Mode. Einziger Maxwell-Zaehlungs-Treffer: arXiv:2607.18995 ("extending Maxwell's
  rigidity count to dynamic, non-equilibrium processes", granulare Kontinua), keine Pumpe [S Abstract].
  Urteil (Regel 7): "Pumpen eines Maxwell-Gitters durch gleichmaessiges Atmen (Guest-Mode)" = nach Recherchestand
  nicht belegt (F4 alle Jahre, F5 24 Monate).
- **F6, Erwartung geschrieben 18:26:53 (date), vor dem Abruf.** arXiv-API, Relevanz: (ti:kagome AND (abs:colloidal OR
  abs:colloids OR abs:Janus OR abs:patchy)) OR (abs:"DNA origami" AND abs:triangular AND (abs:shell OR abs:shells OR
  abs:icosahedral OR abs:capsid OR abs:tubules)). Erwartung (E5): Kolloid-Kagome aus dreiklebigen (Triblock-)Janus-Kugeln
  (Chen/Bae/Granick 2011; Mao/Chen/Granick 2013 "Entropy favours open colloidal lattices": Kagome durch die Entropie der
  weichen Drehmoden stabilisiert); Simulationen von Patchy-Teilchen (Romano/Sciortino). DNA-Origami-Dreiecke binden
  **ueber Kanten** mit Fasenwinkeln (Hayakawa u. a. 2022 Roehrchen; Videbaek u. a. 2024), Ikosaederschalen
  (Sigl u. a. 2021) vermutlich nicht auf arXiv. Dreiecke, die nur an den **Spitzen** binden (Rocklins Vorschlag), eher
  nicht gebaut.
- **F6 ausgefuehrt 18:27:08 (date):** 10 Treffer, quellen/F6-api-selbstbau.xml. Gelesen bis 18:29:28.
  - DNA-Origami **bestaetigt** (Kantenbindung mit Winkelvorgabe): Hayakawa, Videbaek, Hall, Fang, Sigl, Feigl, Dietz,
    Fraden, Hagan, Grason, Rogers, arXiv:2203.01421, PNAS 119, e2207902119 (2022): "triangular subunits using DNA origami
    that have specific, valence-limited interactions and designed binding angles"; "geometrically programming the
    dihedral angles between neighboring subunits"; Roehrchenbreite "prescribed through the dihedral angles"; aber
    "a distribution in the width and the chirality" [S Abstract]. Wei u. a. 2024 (arXiv:2310.18790): Dreiecke -> T = 3
    Ikosaederkapside aus 60 Einheiten, ungleiche Bindungen -> Dimer- oder Pentamer-Wege [S Abstract; P]. Sigl 2021
    selbst nicht gefunden (nicht gesucht).
  - **Verstoss V-F6a (klein, Kruemmung aus Fuenfer-/Siebener-Ecken wird gebaut):** Price, Hayakawa, Videbaek, Saha,
    Tyukodi, Hagan, Fraden, Grason, Rogers, arXiv:2506.16403 (Juni 2025): Kirigami-Abbildung ebener Kachelungen auf
    gekruemmte Kristalle "via the arrangement of disclination defects"; Toroide, helikale und schlangenfoermige
    Roehrchen "from DNA origami subunits", aus Dreiecks-Untereinheiten; "geometric specificity of angular folds" noetig
    gegen Fehlbau [S Abstract]. Das ist Kartenabschnitt 3 (n Dreiecke je Ecke = Kruemmung) als Bauplan im Experiment;
    erwartet hatte ich nur Schalen und Roehrchen.
  - **Verstoss V-F6b (Kolloid-Kagome ist schwer):** Mallory/Cacciuto, arXiv:1902.05583 (2019, Simulation): Kagome aus
    Triblock-Janus-Kolloiden ist eine "elusive structure"; metastabile Aggregate; Aktivierung (Eigenantrieb) verbessert
    die Bildung "significantly" [S Abstract]. Chen/Bae/Granick 2011 und Mao/Chen/Granick 2013 nicht unter den Treffern
    (vermutlich nicht auf arXiv) -> bleiben [L]. Erwartung korrigiert: Eckenbindung bildet Kagome nur muehsam;
    Kantenbindung mit Winkelvorgabe baut verlaesslich Schalen und Roehrchen.
  - Huang u. a., arXiv:2511.06630 (Nov. 2025): Au-Bipyramiden per DNA zu rhomboedrischen Kristallen mit Kagome-Ebenen
    [S Abstract]; kein Dreiecks-Eckenbau.
  - Dreiecke, die nur an den Spitzen binden: **nicht gefunden** (eine Abfrage). Bleibt Rocklins Vorschlag (F3 Z. 278-286).
- **Zwischenbefund Gegensweep vorgezogen (18:29, nach F6, ohne Abruf) [ES, L?]:** SP8 sagt "Finns Netz kann nicht
  gleichfoermig isotrop atmen". Bewiesen ist das nur fuer die gleichfoermige Gegendrehung der primitiven Zelle (Gamma).
  Kippmuster groesserer Zellen (X-Punkt-RUM) sind nicht abgedeckt. Aus dem Gedaechtnis [L?]: Das kubische P2_13-Modell
  von beta-Cristobalit (Tetraeder gedreht um die vier verschiedenen <111>-Achsen) ist kubisch und dichter als das
  ideale Fd-3m. Zweite Ordnung [M]: Mittel von (I - n n^T) ueber die vier <111> = (2/3) I, also isotrop. **SP8 wird
  eingeschraenkt:** in 3D kein isotropes Atmen mit der Gamma-Mode; mit vier Untergittern vermutlich doch [H].
  -> Rechenkartenkandidat.
- **F7, Erwartung geschrieben 18:29:28 (date), vor dem Abruf.** arXiv-API, Relevanz: (ti:breathing AND (ti:kagome OR
  ti:pyrochlore) AND (abs:mechanical OR abs:acoustic OR abs:phononic OR abs:elastic OR abs:Maxwell)) OR
  (abs:"topological polarization" AND (abs:disorder OR abs:disordered OR abs:random OR abs:jammed OR abs:amorphous)).
  Erwartung (Frage 3): Breathing Kagome in Akustik/Mechanik als Higher-Order-TI mit Eckzustaenden (Ni u. a. 2019, Xue u.
  a. 2019), Resonator- oder Federnetze bei endlicher Frequenz, **nicht** als Zentralkraft-Maxwell-Rahmen; keine Arbeit
  mit "Polarisation R_T des Breathing Kagome" (nach SP10 ist sie null). Fuer Unordnung: Sussman/Stenull/Lubensky 2016
  "Topological boundary modes in jammed matter" (Polarisation auch in ungeordneten Netzen moeglich); evtl.
  Quasikristalle (Zhou/Zhang/Mao).
- **F7 ausgefuehrt 18:29:54 (date):** 28 Treffer, quellen/F7-api-breathing-unordnung.xml. Gelesen bis 18:30:36.
  - **Bestaetigt (Breathing Kagome mechanisch = Federmassen bei endlicher Frequenz):** Wakao, Yoshida, Araki, Mizoguchi,
    Hatsugai, arXiv:1909.02828, PRB 101, 094107 (2020): "higher-order topological phases in a spring-mass model with a
    breathing kagome structure"; Eckzustaende bei festem Rand; Z3-Berry-Phase 2 pi/3; Experiment nur vorgeschlagen
    ("can be detected experimentally through a forced vibration") [S Abstract]. Keine Arbeit zu R_T im Breathing Kagome.
  - **Anker 3D, ungleich grosse Tetraeder gibt es als Kristalle:** LiGa(1-x)In(x)Cr4O8: "a network of size-alternating
    spin-3/2 Cr3+ tetrahedra known as a 'breathing' pyrochlore lattice" (Tanaka u. a., arXiv:2301.05064, JPSJ 87, 073710)
    [S Abstract]; Ba3Tm2Zn5O11, "F-43m breathing pyrochlore crystal structure", Einkristalle gezuechtet (Yadav u. a.,
    arXiv:2407.00222, PRMaterials 8, 123401 (2024)) [S Abstract]. Dort ist die Physik Magnetismus, nicht Mechanik.
  - **Unordnung, bestaetigt:** Zhou/Zhang/Mao, arXiv:1809.09188, PRX 9, 021054 (2019): Penrose- und "disordered
    parallelogram tilings" bekommen topologische Rand-Nullmoden; Polarisation mit Richtungen, die periodisch "not
    allowed" sind [S Abstract]. Charara, McInerney, Sun, Mao, Gonella, arXiv:2204.13615: polarisierte Maxwell-Gitter
    "focus these zero modes to one of their boundaries in a manner that is protected against disorder"; 3D-gedruckte
    Kagome-Doppelschicht, Laser-Vibrometrie (endliche Frequenz) [S Abstract]. Damit ist Kartenabschnitt 5(a) "alle
    weichen Moden an einen Rand" im Wortlaut gedeckt (meine Einschraenkung nach F3 gilt nur fuer Rocklins Wortlaut).
  - **Verstoss V-F7 (gegen Kartenhypothese 5d, aus F3 + Zaehlung):** "Zufaellige Groessen: ... das gleichmaessige
    Atmen zerfaellt vermutlich in Flecken [H]." Gegenbefund: Rocklin Z. 252-258: Maxwell-Gitter haben die gleichfoermige
    weiche Verformung "even with arbitrarily chosen shapes of triangles" [S]. Die Zaehlung d(d-1)/2 gilt fuer jede
    periodische Superzelle, also auch fuer ein Zufallsnetz mit periodischem Rand [M]. Ein Stueck davon behaelt die
    Verformung (ein Mechanismus bleibt ein Mechanismus, wenn man Bindungen weglaesst) [M]. **Die globale Atem-Mode
    ueberlebt Unordnung**; lokal drehen die Dreiecke dann ungleich (nicht affin), und die Mode ist im Allgemeinen keine
    reine Dilatation mehr (Dilatation gegen Scherung nach det eps, Rocklin Z. 108-131) [S, M]. Nicht gefunden: eine
    Messung dazu in Zufallsnetzen.
  - Sussman/Stenull/Lubensky 2016 (jammed matter) nicht unter den Treffern (Phrase vermutlich nicht im Abstract).
- **F8, Erwartung geschrieben 18:30:36 (date), vor dem Abruf (Gegensweep-Pruefung).** arXiv-API, Relevanz:
  abs:cristobalite AND (abs:"rigid unit" OR abs:"thermal expansion" OR abs:tetragonal OR abs:P2_13 OR abs:"negative
  thermal"). Erwartung: Dove-Gruppe/Verwandte: beta-Cristobalit als dynamisch ungeordneter Mittelwert gekippter
  Domaenen (RUM); alpha-Cristobalit tetragonal; Waermeausdehnung von beta-Cristobalit klein oder leicht negativ (Karte
  sagt "schrumpft beim Erwaermen" [L], ich erwarte: das gilt nicht allgemein, alpha dehnt sich stark aus). P2_13 nur
  vielleicht erwaehnt.
- **F8 ausgefuehrt 18:30:58 (date):** nur 3 Treffer, quellen/F8-api-cristobalit.xml. Gelesen bis 18:31:27.
  - **Gegen die Karte (Abschnitt 4, [L] "Cristobalit schrumpft beim Erwaermen"), mit meiner Erwartung:** BeF2 in der
    alpha-Cristobalit-Struktur (Rechnung, arXiv:2209.10087, RSC Adv. 12, 26588 (2022)): "we do not find any negative
    thermal expansion"; "giant" Volumenausdehnung ~175e-6/K bei 300 K, besonders entlang c; Ursache grosse
    Grueneisen-Parameter weicher Moden [S Abstract]. Rickwardt/Nielaba/Mueser/Binder (cond-mat/0010315) rechnen die
    Waermeausdehnung von beta-Cristobalit und beta-Quarz, Vorzeichen nicht im Abstract [S Abstract].
  - Urteil: "Cristobalit schrumpft beim Erwaermen" ist nach Recherchestand **nicht belegt** (kein "widerlegt": eine
    Abfrage, Klassiker der Dove-Gruppe nicht auf arXiv). Zwei-Regime-Lesart [ES, L]: gekippte Phase (alpha, statische
    Drehung) dehnt sich beim Erwaermen aus, weil die Kippung zurueckgeht; nur in der ungekippten Phase (beta, dynamische
    Drehung) ziehen thermische Drehungen das Netz zusammen (Spannungseffekt, NTE). Moderator: Temperatur relativ zum
    alpha-beta-Uebergang. Rocklin ~~Z. 289-295~~ Z. 288-293 stuetzt nur "RUMs ... argued to be responsible for negative thermal
    expansion in some crystals" [S].
  - P2_13 kommt nicht vor; der Gegensweep-Zwischenbefund bleibt [L?].
- **F9, Erwartung geschrieben 18:31:27 (date), vor dem Abruf.** arXiv-API, Relevanz: abs:jitterbug OR (abs:patchy AND
  abs:valence AND (abs:"empty liquid" OR abs:"empty liquids" OR abs:gel OR abs:gels)). Erwartung: (a) Jitterbug: 0 bis 3
  Treffer, eher Mathematik; falls einer: Kuboktaeder aus 8 eckverbundenen Dreiecken dreht sich zum Ikosaeder und
  Oktaeder (Fuller). (b) Patchy-Kolloide (E5, dritter Teil [H]): Bianchi u. a. 2006 "empty liquids": Bei kleiner
  Valenz (2 bis 3 Bindungen je Teilchen) schrumpft das Gas-Fluessig-Gebiet, Netzwerke/Gele bei kleiner Dichte statt
  Kristall. Eckenbindende Dreiecke haben Valenz 3, also Gel-Regime.
- **F9 ausgefuehrt 18:31:46 bis 18:31:47 (date):** 13 Treffer, quellen/F9-api-jitterbug-patchy.xml. Gelesen bis 18:32:31.
  - (b) **bestaetigt** (E5 dritter Teil, Substanz): Ruzicka, Zaccarelli, ..., Sciortino, arXiv:1007.2111, Nat. Mater. 10,
    56 (2011): "the phase diagram of patchy colloids can be significantly altered by limiting the particle coordination
    number (that is, valence)"; "first observation of empty liquids and equilibrium gels in a complex colloidal clay"
    [S Abstract]. Smallenburg/Sciortino, arXiv:1307.1842: "for patchy colloids with limited valence ... the disordered
    liquid phase is stable all the way down to the zero-temperature limit" [S Abstract]. Neves u. a., arXiv:2504.02474
    (April 2025): Steifigkeit in Gelen begrenzter Valenz setzt mit der Perkolation von Teilchen mit mindestens drei
    Bindungen ein; "a robust minimum average valence, below which the gel is never rigid" [S Abstract].
    Einordnung [ES]: Dort uebertragen die Bindungen Drehmoment (Patch-Bindungen sind winkelsteif); bei Finns
    Kugelgelenken nicht. Moderator: Biegesteifigkeit am Gelenk.
  - (a) **Verstoss V-F9 (Jitterbug ist gebaut und taucht in Nanoclustern auf):** Mogi u. a., arXiv:2509.09613 (Sept.
    2025): Roboter MOFU, "Jitterbug geometric transformation mechanism that enables smooth diameter changes from
    approximately 210 mm to 280 mm with a single actuator" [S Abstract]. Khajehpasha u. a., arXiv:2601.10434 (Jan. 2026,
    Rechnung mit ML-Potential): Gold-Nanocluster Au55 bis Au561, Uebergaenge Kuboktaeder -> Ikosaeder als
    "soft-mode-driven jitterbug-type ... motions" [S Abstract]. Sadler u. a., arXiv:1302.1174: nennt "Buckminster
    Fuller's 'jitterbug transformation'" [S Abstract]. Erwartung war "0 bis 3, eher Mathematik"; tatsaechlich ein
    gebautes Atemgeraet mit einem Motor und eine Atomcluster-Anwendung.
  - Jitterbug-Zahlen [M] (Kantenlaenge a, starr): Umkugelradius Kuboktaeder a, Ikosaeder 0,951 a, Oktaeder a/sqrt(2) =
    0,707 a; Volumen 2,357 a^3, 2,182 a^3, 0,471 a^3; Verhaeltnis Kuboktaeder/Oktaeder genau 5. MOFU nutzt 280/210 =
    1,33 von hoechstens 1,41 im Durchmesser.
- **F10, Erwartung geschrieben 18:32:31 (date), vor dem Abruf (letzter Abruf; Ankersuche fuer Frage 1).** arXiv-API,
  Relevanz: (abs:triangular OR abs:triangles) AND (abs:"tip-to-tip" OR abs:"vertex-to-vertex" OR abs:"corner-to-corner"
  OR abs:"corner-sharing" OR abs:"vertex-sharing") AND (abs:assembly OR abs:self-assembly OR abs:colloidal OR abs:origami
  OR abs:metamaterial OR abs:kirigami). Erwartung: wenige Treffer; Bowtie-Antennen aus Nanoprismen (Spitze an Spitze,
  Spalt statt Bindung), vielleicht Kirigami-Rotationsmetamaterial aus Dreiecken (gelenkig an den Ecken verbunden,
  auxetisch). Eckenbindender Selbstbau aus Dreiecken: hoechstens ein Treffer.
- **F10 ausgefuehrt 18:32:53 (date):** 2 Treffer, quellen/F10-api-ecken-selbstbau.xml. **Im Rahmen der Erwartung (ein
  Treffer), inhaltlich wichtig:**
  - Ferrar, Bedi, Zhou, Zhu, ..., arXiv:1802.02949, Soft Matter 14, 3902 (2018): duenne gleichseitige Dreiecksprismen
    (Kante 120 um) an einer Luft-Wasser-Grenzflaeche binden kapillar "in either a tip-to-tip or tip-to-midpoint edge
    configurations"; bei T/L = 1/5 bindet die Spitze "to any position along the other triangle's edge"; "Prisms of all
    T/L ratios self-assemble into space-spanning open networks"; Ziel Kagome nur als Ausblick [S Abstract]. Das ist
    Finns Frage 1 als Experiment in 2D, mit einem dritten Bindungsmodus (Spitze an Kantenmitte).
  - Wilson, Kumar, Sherrington, Thorpe, arXiv:1303.5898, PRB 87, 214108 (2013): Modell der experimentell hergestellten
    glasartigen Silica-Doppelschicht; die Einzelschicht "can be now thought of as a two dimensional network of corner
    sharing triangles", daraus Tetraeder [S Abstract]. Material-Anker fuer ein ungeordnetes eckenteilendes Dreiecksnetz.
- **Abrufbudget erschoepft: 10 von 10 (F1 leer, F2 bis F10).** Keine weiteren Abrufe.
- Projektdatei statt Abruf (18:35): Kusner/Kusner/Lagarias/Shlosman, arXiv:1611.10297v3, lokal
  RUNDE-17/quellen-frustration/hilfs/p8-1611.10297.txt Z. 1801-1823: Fullers Jitterbug ist "a jointed framework motion"
  vom Kuboktaeder zum Ikosaeder; "the joint distances remain constant during the motion, so that they can be rigid
  bars" [P, dort S]. Projekt-grep 18:35:15 nach P2_13, I-42d, Jitterbug, Kuboktaeder: nur dieser Treffer und
  Kuboktaeder als Nachbarschaft in LIFE-FCC-1/LIFE-DIAMANT-1; keine Karte zum isotropen Atmen. Eine Unter-grep in
  RUNDE-37 lief ohne die Ausschluesse T8-SOLL-* und *KS-1* (Dateien); Namenspruefung 18:35:55: solche Dateien gibt es
  dort nicht (Selbstanzeige, klein).

## 4. Erwartungsverstoesse (getrennt; wichtigste zuerst; Stand 18:36)

- **V1 (aus F3 + Zaehlung, gegen Kartenhypothese 5d):** Die globale Atem-Mode ueberlebt beliebige Dreiecksformen und
  damit Unordnung (d(d-1)/2 je periodischer Superzelle; "even with arbitrarily chosen shapes of triangles"). Sie ist
  dann meist keine reine Dilatation. 3D: drei solche Moden.
  - Voller Zyklus: Die Zaehlung (meine und Rocklins) braucht nur "Maxwell" und Periodizitaet. Einschraenkung: Bei
    besonderer Geometrie (gerade Linien) kommen Eigenspannungen und Volumen-Nullmoden dazu (Rocklin ~~Z. 244-250~~ Z. 219-226 [berichtigt, vor 18:37:55 (date)], EIS-1
    [P]); die Untergrenze bleibt. Folge fuer Frage 2: In 2D gibt es genau einen gleichfoermigen Freiheitsgrad, also
    keine Schleife und kein Pumpen allein durch gleichfoermiges Atmen; in 3D drei, also Schleifen moeglich [M]. Ob
    eine Schleife etwas traegt: nicht belegt (F4, F5).
- **V2 (F4, 2025):** Die mechanische Thouless-Pumpe, die Finns Bild am naechsten kommt, pumpt Kink-Solitonen,
  nicht-adiabatisch und nur mit Reibung; die Quantisierung ist keine Chern-Zahl (Juergensen u. a. 2025).
  - Voller Zyklus: Das verbindet E4 (Randzustand wandert, Xia u. a. 2021) und E6 (Kink in der Gelenkkette, Chen u. a.
    2014). Gemeinsame Groesse [ES, Regel 6]: Nicht das Bauteil (Pendel, Gelenkkette, Piezo-Balken), sondern eine
    **raeumlich laufende Phase** der Modulation (Wanderwelle) traegt; gleichphasiges Atmen hat keine. Drei Wege zu
    "Pumpen" (Randzustand, Kink, Fluidvolumen) haben dieselbe Bedingung: ein Zyklus mit Flaeche im Parameterraum.
- **V3 (F9, 2025/2026):** Der Jitterbug ist als Atem-Roboter gebaut (ein Motor, 210 -> 280 mm) und taucht als weiche
  Mode in Gold-Nanoclustern auf (Rechnung). Endliches 3D-Gegenstueck zu Finns Bild: 8 eckverbundene Dreiecke, Volumen
  Faktor 5 bei festen Kanten [M]. Erwartet hatte ich nur Mathematik.
- **V4 (F4, 2024):** Winkel einer Origami-Kette als Pumpparameter (raeumliche Modulation, synthetische Dimension) ist
  vorgeschlagen; kein zeitliches Atmen.
- **V5 (F6, 2025):** Kruemmung durch gezielt gesetzte Disklinationen (Fuenfer-/Siebener-Ecken) ist bei
  DNA-Origami-Dreiecken ein Bauprinzip (Toroide, Helices).
- **V6 (F6, 2019):** Kolloid-Kagome aus Janus-Kugeln ist "elusive"; Aktivitaet hilft. Eckenbindung ordnet schlecht.
- **V7 (F8, gegen Karte [L]):** "Cristobalit schrumpft beim Erwaermen" nicht belegt; die alpha-Cristobalit-Struktur
  (BeF2, Rechnung) dehnt sich riesig aus. Zwei Regime: statische Kippung (alpha) gegen dynamische (beta).
- **V8 (F3, nur meine Zwischenerwartung):** Ich hatte nach dem Abstract erwartet, dass nicht jedes Maxwell-Gitter eine
  Guest-Mode hat. Falsch: alle haben d(d-1)/2.
- Kein Verstoss, aber wichtig: F10 Ferrar u. a. 2018 (Spitze an Spitze und Spitze an Kantenmitte, offene Netze).

## 5. Offene Rueckfragen (wandern mit)

- R1 (an Finn): "An den Ecken binden" = Ecken fallen zusammen (Gelenk, Kagome/Pyrochlor) oder beruehren sich im Abstand
  1 PU (neuer Stab, Kontaktnetz)? Die Karte nutzt beides (SP3).
- R2 (an Finn): Was soll gepumpt werden: Fluessigkeit (Hubvolumen), eine Verformung (Kink) oder ein Randzustand?
- R3 (an Finn): "Ungleich gross" = zwei Groessen im Wechsel (Breathing) oder zufaellig?
- R4 (an Finn/Leitung): Darf eine Ecke mehr als zwei Partner haben? Ab n = 3 je Ecke ist ein Dreiecksnetz in 3D
  ausgeglichen; mit Kantenteilung entstehen starre Schalen.
- R5 (Leitung): ISO-ATEM-1 (Rechenkarte im Dossier) gegen ATEM-NETZ-1 abstimmen: gleiche Einheit, gleiche Tetraeder.
- R6 (offen, Literatur): Ist das P2_13-Modell von beta-Cristobalit mit exakt starren regulaeren Tetraedern erreichbar?
  Nicht gelesen (Budget erschoepft).

## 6. Gegensweep (18:36, Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- **G1 "Binden an der Ecke" ist ein Kugelgelenk.** Geprueft (F10, Ferrar u. a. 2018): Echte Spitzenbindung ist ein
  Kapillarkontakt; daneben bindet die Spitze an die Kantenmitte oder an jede Stelle der Kante. Ein dritter
  Bindungsmodus, den Karte und ich nicht hatten. Ergebnis: Regime-Liste Ecke-Ecke / Ecke-Kante / Kante-Kante.
- **G2 "Gleichmaessig" heisst gleich in jeder primitiven Zelle.** Nicht durch Abruf geprueft (Budget). Folge: SP8
  ("Finns Netz kann nicht isotrop atmen") gilt nur fuer die Gamma-Mode. Vier-Untergitter-Kippung (P2_13 [L?]) ist
  offen -> Rechenkarte ISO-ATEM-1.
- **G3 "Cristobalit schrumpft beim Erwaermen" (Karte [L]).** Geprueft (F8): nicht belegt, Gegenbeispiel fuer die
  gekippte Phase. Zwei Regime.
- **G4 "Gelenke sind frei".** Geprueft (F3 ~~Z. 268-277~~ Z. 271-278 [berichtigt, vor 18:37:55 (date)]): Endliche Gelenksteifigkeit bestimmt Kantensteifigkeit und
  Schallgeschwindigkeit der weichen Moden; F9 (Neves u. a. 2025): Steifigkeit von Gelen haengt an Bindungen mit
  Drehmoment. Moderator Gelenksteifigkeit.
- **G5 "Pumpen" heisst Thouless.** Nicht geprueft; Finn kann eine Fluessigkeitspumpe meinen (R2). Antwort fuer beide
  Lesarten im Dossier.
- **G6 "Die Maxwell-Zaehlung gilt fuer Finns Netz".** Geprueft (F3 ~~Z. 244-250~~ Z. 219-226 [berichtigt, vor 18:37:55 (date)] und EIS-1 [P]): Finns regulaeres Netz ist
  gerade die besondere Geometrie mit geraden Linien; dort kommen Eigenspannungen und Linien- bzw. Ebenen-Nullmoden dazu.
  Untergrenzen bleiben.

## 7. Kalibrierung (18:36)

- (a) gemessen: die Experimente aus F2 bis F10 (siehe Dossier-Ankertabelle); alles andere ist Rechnung oder Theorie.
- (b) verdichtet: Zaehlungen [M] (n = D je Ecke; 1,5 F - 6 bei eckenteilenden Schalen; d(d-1)/2 Guest-Moden), Faltwinkel
  = reine Eichung [M], Gamma-Mode in 3D tetragonal [M], Jitterbug-Zahlen [M].
- (c) Gewissheit ohne neue Evidenz: "3D kann nicht isotrop atmen" wuchs am Schreibtisch und musste im Gegensweep
  eingeschraenkt werden (Warnzeichen). "Breathing Kagome hat R_T = 0" [ES] und "eine Schleife der drei 3D-Guest-Moden
  koennte pumpen" [H] sind nicht belegt.

## 8. Abschluss (Eintraege nach dem Dossier)

- DOSSIER.md geschrieben ab 18:38:56 (date); Rueckwaertsdurchgang danach: drei Praezisierungen (Ergebnis 1a,
  Einfach gesagt, Endlage Oktaeder [L]) und eine weitere Zeilenberichtigung (Rocklin ~~Z. 289-295~~ Z. 288-293).
- **Selbstanzeige Regelverstoss:** vor 18:45:23 (date) einmal awk fuer eine Zeilenlaengenprobe des Dossiers benutzt
  (verboten). Keine Physikrechnung; nichts daraus geaendert.
- Zeitbox: Start 18:12:19; Abschlusszeit steht unten, per date gemessen.
- Abgeschlossen: 2026-10-04 18:45:59 CEST (date).
