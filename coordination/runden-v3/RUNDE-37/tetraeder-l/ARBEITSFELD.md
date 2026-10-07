# ARBEITSFELD TETRAEDER-L (eine Arbeitsdatei, vor jedem Schritt neu lesen)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-04 14:53:07 CEST (date). Zeitbox 90 min.
- Regeln: keine Websuche; hoechstens 14 Abrufe (arXiv abs/pdf/API), lokale Kopie in quellen/; lokal kein
  python/awk/perl; Versiegeltes nie oeffnen; nur in RUNDE-37/tetraeder-l/ schreiben; Zeiten per date.
- Kennzeichen: [S] an der Quelle gelesen (Zeile/Abschnitt), [S Abstract], [P] Projektdatei, [L] Gedaechtnis,
  [L?] unsicher, [ES] eigener Schluss, [H] Hypothese.
- Gestrichenes wird ~~durchgestrichen~~, nicht geloescht. Offene Rueckfragen stehen unten und wandern mit.

## 0. Vorarbeit gelesen (Datei angelegt zwischen 14:53:57 und 14:58:41, date; geschaetzte Zeit gestrichen)

- KARTE.md vollstaendig (E1 bis E8, Fragen 1 bis 5).
- RUNDE-34/TETRAEDER-ANALYSE.md vollstaendig: fast alles [L]; tragende Punkte fuer diese Karte:
  - Abschn. 2: T_d = S4 (24), T = A4 (12), 2T (24, 24-Zelle), McKay 2T <-> E6 [L]; 70,53 Grad, Luecke 7,36 Grad.
  - Abschn. 3.1 Spin-Eis (Castelnovo/Moessner/Sondhi 2008, Hermele/Fisher/Balents 2004) [L].
  - Abschn. 3.2 Fraktonen (Pretko 2017) [L].
  - Abschn. 3.3 A4 (Ma/Rajasekaran 2001, Altarelli/Feruglio 2005; theta_13 2012) [L].
  - Abschn. 3.4 B = 3 Skyrmion tetraedrisch (Braaten/Townsend/Carson 1990) [L?] -> Drehungs-/Spin-Teil liegt bei
    GUERTEL-1, hier nur am Rand.
  - Abschn. 3.5 Frank 1952, Frank-Kasper, Quasikristalle [L].
- RUNDE-37.md Ernte PONZANO-1: 6j asymptotisch = Ponzano-Regge (Regge-Wirkung in der Phase), Biedenharn-Elliott =
  Pachner 2-3 exakt, Flachheit aus Interferenz. EPRL-Literaturkarte geparkt. -> nur einordnen.
- RUNDE-37.md Ernte CDT-HORAVA-L (zusaetzlich gefunden, relevant fuer E5): lambda in CDT nicht bei Einstein (2D < 1,
  2+1 ~0,03 bis 0,49); Budd/Loll: CDT-Zeit als vorab festgelegter Lapse [P, dort S]. 15 Abrufe dort schon verbraucht.
- TENSOR-EIS-PYRO-1: Eichung an den Mitten mit Laengen (B1) -> zwei unabhaengige fcc-Regge-Kopien (Auf-Kanten mit
  Eichung an Ab-Mitten und umgekehrt); je Kopie 2 Gravitonen, Newton 1/r; Massen auf Auf- und Ab-Mitten spueren sich
  nicht [P, E]. Ausweg [H]: Werte nur auf einer Tetraedersorte.
- TWIST-SPIN-1: Fadenend-Fermion spinlos (T, nicht 2T); halber Spin braucht >= 2 Zustaende je Knoten [P].
- WELTMODELL-REVIEW-1 Abschn. 3 bis 5: K-A hat Ruhesystem (Collins u. a.), doppelte Gravitonen, spinloses Fermion,
  kein Standardmodell; L7 "doppelte Gravitonen" ableitbar (eine Tetraedersorte); L11 Generationen "ausser
  Reichweite" [P].
- RUNDE-41.md Warteschlange K-AM: Tetraeder als Raumscheiben eines Regge-Gitters, Punkte-ergeben-Striche als Strings,
  Flip-Flop Auf/Ab je Takt, Hoechstgeschwindigkeit = Flip-Flop-Takt; FLIPFLOP-ZWEIWELTEN-1, EIN-TAKT-1, DUNKEL-FLIP-L
  in der Warteschlange [P].
- WOLFRAM-SCAN-L K2: Pachner 1-4 und 2-3 als Hypergraph-Regeln; Erwartung "zerknittert bzw. verzweigt" [L?] dort.
- pool.jsonl: keine A4-Flavor- und keine Pachner-Idee; TETRA-nahe Ideen A3 STRICH-DEFIZIT, A4 ZUFALLSNETZ-1 (Delaunay!),
  A5 600-ZELLE, A7 HELIX-DREH, H4 TETRA-RAHMEN-1, H11 QCA-TETRA, SCHERWEICH-KETTE [P].

## 1. Projektsuche (grep) vor jedem Abruf (zwischen 14:53:57 und 15:01:07, date; Versiegeltes, KS-1 und Geheimnisse ausgeschlossen)

- **Lokale Quellen, die Abrufe ersparen (alle [S] lesbar):**
  - RUNDE-17/quellen-frustration/hilfs/p2-2609.26627.txt (Jones/Mughal/Schoenhoefer/Glotzer 2026, Tetraeder im
    Zylinder): Z. 28-35 "Tetrahelical arrangements appear within dodecagonal quasicrystalline phases of hard tetrahedra
    [23] ... while the densest known bulk packings are crystalline arrangements based on face-sharing tetrahedral dimers
    [25]"; [23] = Haji-Akbari u. a., Nature 462, 773 (2009); [25] = Chen/Engel/Glotzer, DCG 44, 253 (2010); [22] Wang
    u. a. JACS 145, 17902 (2023): Gold-Nanotetraeder zu Quasikristallen (Experiment!). -> E1 qualitativ [S]; Zahl 0,856
    dort nicht genannt.
  - RUNDE-17/.../p10-2305.07786.txt (Schoenhoefer/Sun/Mao/Glotzer, PRL 131, 258201 (2023)) S. 2: "hard tetrahedra
    famously form quasicrystals [19, 20] ... instead of the putative densest packing structure with a unit cell comprised
    of four tetrahedra arranged in a double-dimer structure"; "densest packings ... cannot serve as indicators to predict
    self-assembly". S. 3: 600 harte Tetraeder auf der 3-Sphaere -> 600-Zelle mit Leerstellen (rho max 0,96); S. 4: die
    Umgebungen des flachen Quasikristalls gleichen denen der defekten 600-Zelle ("Formen aus Formen": Kruemmung
    wegnehmen sagt die flache Ordnung vorher). -> E1, E6, Frage 4 [S].
  - RUNDE-22/dunkel-zeit/quellen/CDT-review-raw.txt (Ambjoern/Goerlich/Jurkiewicz/Loll 2012, arXiv:1203.3591):
    S. 58 Pachner-Zuege "minimal set of local topology-preserving changes ... which are ergodic"; S. 58-59 in CDT "not
    directly applicable ... do not respect the sliced structure"; S. 83 EDT: "crumpled phase", "branched-polymer",
    Uebergang erster Ordnung (Fussn. 19); S. 118 D_S = 4,02 +- 0,1 (gross) und 1,80 +- 0,25 (klein); S. 118-119
    "crinkled phase" der EDT mit D_S 1,7 +- 0,2 und Hinweis "a truly isotropic model which belongs to the same
    universality class as CDT"; S. 19 (d,1)- und (1,d)-Simplizes; Gl. (47) "each spacelike tetrahedron is shared by a
    pair of a (4,1)- and a (1,4)-simplex". -> E5 [S], K-AM (Auf/Ab in der Zeit!) [S].
  - RUNDE-22/geometrie-stand/hilfs/loll-1905.08669.txt (Loll 2019): EDT-Hoffnung auf kontinuierlichen Uebergang "has
    not been realized" (S. 8-9); zitiert Coumbe/Laiho 2015 (EDT mit Massterm) und Rindlisbacher/de Forcrand 2015.
  - RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt (Surya 2019, Living Rev.): Programm "geometric reconstruction"
    (Dimensionsschaetzer, Benincasa-Dowker-Wirkung), 15+ Arbeiten aufgezaehlt (S. 3-4). -> E7 zweiter Teil verletzt?
  - RUNDE-37/dyon-statistik-l/quellen/arxiv-2009.04499.txt (Pace/Morampudi/Moessner/Laumann 2020): Ergaenzung
    "diamond lattice (the premedial lattice of the pyrochlore lattice)"; E = +-S^z je nach A- oder B-Platz; Eisregel =
    div E = 0. -> E8 Pyrochlor/Diamant [S].
  - RUNDE-35.md Z. 97-120: Yan/Benton/Jaubert/Shannon PRL 124, 127203 (2020), arXiv:1902.10934 [P, dort S]: Rang-2-U(1)
    auf dem ATMENDEN Pyrochlor (A- und B-Tetraeder verschieden), DM-Kopplung nur auf A; Vektorladung. -> Auf/Ab-Asymmetrie
    in der Literatur, Bezug zu TENSOR-EIS-PYRO-1 Ausweg "eine Tetraedersorte".
  - RUNDE-37/ponzano-1: keine Quellen-Kopien (Literatur aus Gedaechtnis dort); nicht neu recherchieren.
- **Nicht lokal vorhanden:** Tetraedergleichung (nur KARTE/RUNDE-41), Quanten-Tetraeder (Barbieri, Baez/Barrett),
  A4-Flavor (nur [L] in TETRAEDER-ANALYSE; in qca-*-PLAN.md ist "A4" die Drehgruppe, nicht Flavor), cut-and-project/E8
  (nur Sadler/Fang/Kovacs/Irwin 2013 zur Tetrahelix, RUNDE-17 p1), persistente Homologie (keine Quelle), Zufallsgraph-
  Geometrie (Bianconi u. a.: keine Quelle), Maxwell-Gitter/Starre-Einheiten-Moden (keine Quelle).
- **Projektrechnungen mit Bezug:** EIS-1 (RUNDE-34), TENSOR-EIS-PYRO-1, TWIST-PYRO-1, TWIST-SPIN-1, KITAEV-DIAMANT-1,
  QBALL-PYRO-1, PONZANO-1, REGGE-*-Karten, KAUSAL-1, CDT-HORAVA-L (15 Abrufe), WOLFRAM-SCAN-L K2.

## 1b. Eigene Mathematik am Schreibtisch [M], vor den Abrufen

- Sternoktaeder: T1 = Ecken (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1) ist {x+y+z >= -1, x-y-z >= -1, -x+y-z >= -1,
  -x-y+z >= -1}; T2 = -T1. Schnitt = alle acht Ungleichungen +-x+-y+-z <= 1 = Oktaeder |x|+|y|+|z| <= 1; konvexe Huelle
  = Wuerfel [-1,1]^3. Kantenmitten von T1 = (+-1,0,0),(0,+-1,0),(0,0,+-1) = dieselben Oktaederecken. Also:
  **Rektifizierung von Auf = Schnitt von Auf und Ab** [M].
- 2T = 24 Hurwitz-Einheiten +-1, +-i, +-j, +-k, (+-1+-i+-j+-k)/2 (8 + 16 = 24, alle Norm 1) = Ecken der 24-Zelle [M].
- Diederwinkel arccos(1/3) = 70,5288 Grad; 360 - 5 x 70,5288 = 7,356 Grad [M].

## 2. Abrufplan mit Vorhersage je Abruf (vor dem jeweiligen Abruf geschrieben, zwischen 14:58:41 und 15:01:07, date)

| Abruf | Ziel | Vorhersage (ein Satz) |
|---|---|---|
| F1 | arXiv-API id_list gr-qc/9707010, gr-qc/9903060, 1102.5439 (E4) | Baez/Barrett: Hilbertraum mit Basis aus Flaechen plus einer weiteren Quantenzahl in 3D, nur Flaechen in 4D; Bianchi/Haggard: Volumen des Quanten-Tetraeders diskret; Barbieri: Quanten-Tetraeder aus Spin-Netzen, Winkel nicht vertauschbar |
| F2 | arXiv-API Suche "tetrahedron equation", neueste zuerst (E3) | viele math-ph/nlin-Arbeiten 2024-2026 zu Loesungen (3D-R-Matrizen, Cluster-Algebren); keine 3+1-Teilchenphysik; Zamolodchikovs Saiten-Motiv hoechstens in Abstracts erwaehnt |
| F3 | (nach F2) Volltext oder Abstract mit der physikalischen Lesart (E3) | Zamolodchikov 1980/81: faktorisierte Streuung gerader Strings in 2+1 D; Baxter 1983 bewies Zamolodchikovs Loesung; Gitter-Lesart 3D |
| F4 | arXiv-API id_list 1706.08749, 2311.09282, hep-ph/0610165 (E2) | Feruglio: Yukawas als Modulformen, Gamma_3 = A4, wenige Parameter; Ding/King: Uebersichtsartikel ohne Bestaetigung; Altarelli/Feruglio/Lin: A4 aus Orbifold-Fixpunkten (Tetraeder) |
| F5 | arXiv-API Suche modular + A4 + neutrino, neueste zuerst (E2, 24 Monate) | viele Modelle 2024-2026; Vergleiche mit JUNO 2025 und DESI-Massengrenze; Vorhersagen fuer delta_CP, Summe m_nu, m_bb; keine Bestaetigung |
| F6 | arXiv-API Suche "dynamical triangulations", neueste zuerst (E5, 24 Monate) | CDT aktiv (Loll, Ambjoern, Goerlich/Nemeth, Clemente/D'Elia); EDT mit Massterm aktiv (Laiho u. a.) mit Anspruch auf 4D-Phase; also "EDT scheitert" nicht mehr Konsens |
| F7 | arXiv-API Suche Tetraeder-Packung/Quasikristall (E1) | Haji-Akbari 2009, Chen/Engel/Glotzer 2010 mit 4000/4671 = 0,856347, Kallus/Elser/Gravel, Torquato/Jiao |
| F8 | arXiv-API Suche Quasikristall + E8 + Tetraeder (Irwin u. a.) (E6) | Arbeiten der Quantum Gravity Research auf arXiv, Zeitschriften hoechstens Tagungsbaende oder MDPI |
| F9 | arXiv-API Suche emergente Geometrie aus Zufallsgraphen / Simplizialkomplexen (E7b) | Bianconi/Rahmede (Network Geometry with Flavor), Trugenberger (kombinatorische QG), Kelly u. a. 2019: mehrere Gruppen, also mehr als Einzelarbeiten |
| F10 | arXiv-API Suche persistente Homologie + kosmisches Netz / amorph (E7a) | etablierte Reihe (Pranav u. a. 2017, Hiraoka u. a. 2016) und laufende Arbeiten 2024-2026 |
| F11 | arXiv-API id_list 1503.01324, 1711.11044 (Regime steif gegen Regel) | Lubensky u. a.: Maxwell-Gitter, Kagome und Pyrochlor, Nullmoden auf Linien bzw. Ebenen; Pretko/Radzihovsky: Elastizitaet dual zu symmetrischer Tensor-Eichtheorie, Disklinationen = Fraktonen |
| F12 | (nach F11) Volltext Lubensky u. a. (Pyrochlor-Ebenen) | Pyrochlor-Netz hat Nullmoden und Eigenspannungen auf Ebenen im k-Raum; also TENSOR-EIS-PYRO-1 TE1 "Ebenen" ableitbar |
| F13-F14 | Reserve fuer Verstoesse | - |

## 3. Abrufprotokoll (Zaehler x/14)

- F1 (1/14), 15:01:22-15:01:23, arXiv-API, quellen/F1-api-quantentetraeder.xml. (Erster Versuch 15:01:15 ueber http ohne
  Weiterleitung: leere Datei, kein Inhalt; nicht gezaehlt, hier vermerkt.) **Bestaetigt E4, eine Zeile:** Barbieri 1998
  (NPB 518, 714): Flaechen mit SU(2)-Darstellungen plus Schliessung; "due to an uncertainty relation, the 'geometry of the
  tetrahedron' exists only in the sense of 'mean geometry'"; Baez/Barrett 1999 (ATMP 3, 815): 3D-Basis = vier
  Flaechen plus eine Groesse, "e.g. the area of one of the parallelograms formed by midpoints of the tetrahedron's
  edges", in 4D nur die Flaechen; Bianchi/Haggard 2011 (PRL 107, 011301): Bohr-Sommerfeld-Volumenspektrum des
  Tetraeders gibt die Koernung der Schleifengravitation. [ES] Die Kantenmitten-Parallelogramme sind Schnitte des
  Oktaeders aus 1b, also des Schnitts von Auf und Ab; der Wechsel zwischen den drei Parallelogramm-Basen ist die
  6j-Umkopplung (PONZANO-1) [L].
- F2 (2/14), 15:01:37-15:01:38, arXiv-API, quellen/F2-api-tetraedergleichung.xml, 133 Treffer, 60 neueste gelesen
  (Titel; Abstracts mit string/scattering/circuit/3D). **Bestaetigt E3 im Kern:** Padmanabhan/Singh/Korepin 2025
  (arXiv:2510.23944) [S Abstract]: "The different forms of the tetrahedron equation appear when all possible ways to
  label the scattering process of infinitely long straight lines are considered in three dimensional spacetime";
  Loesungen in Fuelle (Quanten-Cluster-Algebren, Clifford, Majorana, Teichmueller-TQFT, M-Theorie-Branen); kein
  3+1-Teilchenmodell unter 60 Titeln. **Neu, nicht erwartet (aber kein Verstoss):**
  - Quantenschaltkreis-Lesart: "Toffoli gates solve the tetrahedron equations" (Sinha/Padmanabhan/Korepin 2024,
    arXiv:2405.16477) [S Abstract]: integrable Quantenschaltkreise aus 3-Qubit-Gattern.
  - Die bekannten 3D-integrablen Gitter sind gestapelte Eis-Schichten: "q-oscillator valued six-vertex model",
    "layer to layer transfer matrices" (Kuniba/Maruyama/Okado 2016, arXiv:1509.09018; Inoue/Kuniba/Terashima/Yagi 2025,
    arXiv:2505.08924, "quantized six-vertex model ... three-dimensional integrable lattice model") [S Abstract]. Das
    Sechs-Vertex-Modell ist das 2D-Eis (zwei rein, zwei raus) [L]. -> Bezug K-A (Pfeil-Eis) [ES].

## 4. Erwartungsverstoesse (getrennt gefuehrt)

(folgt)

## 5. Offene Rueckfragen (wandern mit)

- R1: Was genau meint Finn mit "Formen, die was bedeuten"? Arbeitsannahme: Umformungen, die eine Groesse erhalten
  (Volumen, Topologie, Symmetrie, Reihenfolge) oder eine Messgroesse liefern.
- F3-Vorhersage (vor dem Abruf, vor 15:02:36 date): Volltext arXiv:2510.23944 (6 Seiten) nennt Zamolodchikov 1980/81 als Ursprung
  (gerade Strings in 2+1), erklaert den Namen ueber vier Ebenen bzw. Weltflaechen, die einen Tetraeder bilden, und
  nennt keine 3+1-Anwendung.
- F3 (3/14), 15:02:36-15:02:37, arXiv-PDF 2510.23944v1 -> quellen/F3-2510.23944.txt (E-Mails entfernt, PDF geloescht).
  **Bestaetigt E3 und schaerft:** S. 1 "formulated in the early 80's by Zamolodchikov [4]. Early solutions were studied
  by Baxter [5] and Bazhanov [6] but were found insufficient for physical applications in spite of their ingenuity" [S].
  S. 2: "The main source ... is the scattering of three straight lines in two dimensional space. From a three
  dimensional spacetime perspective this process forms a tetrahedron or a 3-simplex"; Lesarten "vacua - cell or volume",
  "string - face", "particle - edge"; "In a given time slice, the vacua, string and particle correspond to the face,
  edge and vertex of the intersecting strings" [S]. Gl. (1) R_ijk R_ilm R_jlp R_kmp = R_kmp R_jlp R_ilm R_ijk.
  [M] Gl. (1) hat sechs Indizes und vier R: vier Strings haben C(4,2) = 6 Kreuzungspunkte ("Teilchen") und C(4,3) = 4
  Dreifachtreffen (Ereignisse) = 6 Kanten und 4 Ecken eines Tetraeders in der Raumzeit.
  [ES] Teilchen sind hier Kreuzungspunkte von Strings: "Striche ergeben Punkte", die Umkehrung von Finns Richtung. Der
  Name "Tetraeder" kommt aus der Raumzeit-Figur des Streuvorgangs, nicht aus Tetraeder-Bausteinen.
- F4-Vorhersage (vor dem Abruf, vor 15:03:11 date; ~~15:04~~ war geschaetzt): wie in Abschnitt 2 (Feruglio: Modulformen, Gamma_3 = A4; Ding/King: Uebersicht
  ohne Bestaetigung; Altarelli/Feruglio/Lin: A4 aus Orbifold-Fixpunkten).
- F4 (4/14), 15:03:11-15:03:20, arXiv-API, quellen/F4-api-a4-modular.xml. **Bestaetigt E2 teilweise, eine Zeile
  plus Nuance:** Feruglio 2017 (arXiv:1706.08749) [S Abstract]: Yukawas als Modulformen der Stufe N, Gruppe Gamma_N;
  "The most economical model predicts neutrino mass ratios, lepton mixing angles, Dirac and Majorana phases uniquely in
  terms of the modulus vacuum expectation value, with all the parameters except one within the experimentally allowed
  range" (das sparsamste Modell lag also schon 2017 in einer Groesse daneben). Ding/King 2023 (arXiv:2311.09282,
  Uebersicht 168 S.): "single modulus A_4 models", Fixpunkte, Top-down. Altarelli/Feruglio/Lin 2007 (NPB 775, 31):
  A4 aus einem 6D-Orbifold mit "four fixed points where 4 dimensional branes are located and the tetrahedral symmetry of
  A4 connects these branes ... a remnant of the 6D space-time symmetry" [S Abstract] -> Tetraeder in Extra-Dimensionen.
  Gamma_3 = A4 selbst nur [L] (nicht woertlich in diesen Abstracts).
- F5-Vorhersage (vor dem Abruf, vor 15:03:36 date; ~~15:04~~ geschaetzt): viele modulare A4-Modelle 2024-2026; einige vergleichen mit JUNO (2025) und der
  DESI-Massensumme; Vorhersagen fuer delta_CP, Summe m_nu, m_bb; keine Bestaetigung; Verstoss waere eine
  "bestaetigt"-Aussage oder ein Abstract, das A4-Modelle insgesamt fuer ausgeschlossen erklaert.
- F5 (5/14), 15:03:36-15:03:45, arXiv-API, quellen/F5-api-a4-front.xml: nur 3 Treffer (2005, 2020, 2022). **Suchfehler,
  kein Befund:** "abs:A4" trifft "$A_4$" in Abstracts offenbar nicht. Gezaehlt.
- F6-Vorhersage (vor dem Abruf, vor 15:04:01 date; ~~15:05~~ geschaetzt): Suche modular + neutrino + (JUNO oder DESI), neueste zuerst: 10 bis 40 Arbeiten
  2024-2026, die modulare Modelle (A4, S4, A5) an JUNO-2025-Werten bzw. der DESI-Massengrenze pruefen; einzelne Modelle
  ausgeschlossen, keines bestaetigt; normale Ordnung bevorzugt.
- F6 (6/14), 15:04:01-15:04:32, arXiv-API, quellen/F6-api-modular-juno-desi.xml, 10 Treffer (9 aus 2025-2026).
  **E2 im Kern bestaetigt (aktiv, keine Bestaetigung), mit zwei Verstoessen gegen die Gewichtung:**
  - JUNO hat sin^2 theta_12 schon hochpraezise bestimmt und "already constrains part of these predictions"; offen sind
    vor allem Korrelationen sin^2 theta_23 - delta_CP, die DUNE und Hyper-K auf > 3 sigma pruefen koennen
    (Dutta/Goswami/Kashav/Patel, JHEP 08 (2026) 118, arXiv:2601.18397) [S Abstract].
  - Bei minimalen Fixpunkt-Modellen (zwei rechtshaendige Neutrinos, drei Fixpunkte) "the only viable possibilities are
    based on modular S_4' and A_5 symmetry" (Shang/Lu/Ding/King 2026, arXiv:2601.09598) [S Abstract]: A4 ist an der
    Front nicht bevorzugt. TM1 ("the first column of the tri-bimaximal mixing matrix is preserved") lebt weiter.
  - Gamma_3 = A4 woertlich: "the Gamma_3 \cong A_4 modular group" (Kumar/Dutta/Das 2025, arXiv:2512.22020) [S Abstract].
  - DESI kommt in keinem der 10 Abstracts vor (nur JUNO) [S]; Massensummen-Bezug also nicht gefunden.
- F7-Vorhersage (vor dem Abruf, vor 15:04:57 date; ~~15:06~~ geschaetzt): Suche "dynamical triangulations", neueste zuerst: CDT aktiv (Loll, Ambjoern,
  Goerlich/Nemeth, Clemente/D'Elia), EDT mit Massterm aktiv (Laiho, Dai, Bassler u. a.) mit Anspruch auf eine 4D-Phase;
  "EDT scheitert" waere dann kein Konsens mehr.
- F7 (7/14), 15:04:57-15:04:59, arXiv-API, quellen/F7-api-dt-front.xml, 441 Treffer, 60 neueste (2021-2026) gelesen
  (Titel; 9 Abstracts). **ERWARTUNGSVERSTOSS zu E5 (zweiter Teil):**
  - Dai/Freeman/Laiho/Schiffer/Unmuth-Yockey 2024/25 (arXiv:2408.08963) [S Abstract]: "Euclidean dynamical
    triangulations (EDT) ... the emergent de Sitter geometries of our simulations ... agreement with de Sitter is
    good"; laufende kosmologische Konstante, Vorhersage "deviations from LambdaCDM at the O(10^-3) level".
  - Asaduzzaman/Catterall, PRD 107, 074505 (2023), arXiv:2207.12642 [S Abstract]: EDT mit lokalem Massterm beta:
    "a line of first order phase transitions with a latent heat that decreases as kappa -> infinity"; D_H -> 4 entlang
    der kritischen Linie, D_s = 3/2 im Kleinen; "a degree of universality".
  - Budd/Lionni-Anschluss 2025 (arXiv:2507.01604) [S Abstract]: 3D-DT mit Baum-Dekoration hat eine neue
    "triple-tree phase" neben "the familiar crumpled and branched polymer phases".
  - ~~Loll 2026~~ Ambjoern/Loll 2026 (Autoren nachgeprueft; arXiv:2604.05641) [S Abstract]: CDT "compatible with those of a de Sitter space", "a spectral dimension
    near 2". Ambjoern/Gizbert-Studnicki/Goerlich/Nemeth PRD 110, 126006 (2024): UV-Fixpunkt "data precision does not
    yet provide a proof".
  - Korrektur der Erwartung: "euklidisch scheitert" gilt nur fuer reine EDT (nur Einstein-Hilbert-Kopplungen):
    zerknuellt/verzweigt, erster Ordnung [S: AGJL 2012 S. 83; Loll 2019 S. 8-9]. Mit Massterm (Moderator!) ist EDT eine
    aktive Gegenposition mit eigenem de-Sitter-Anspruch. Urteil: nicht "gescheitert", sondern "ohne gesicherten
    Kontinuumslimes, umstritten" (Regel 7).
  - Nebenfund fuer E7: van der Duin/Loll/Schiffer/Silva 2025 (arXiv:2510.05693) [S Abstract]: Betti-Zahlen
    vergroeberter DT-Geschichten als Funktion der Vergroeberungsskala (topologische Datenanalyse an Quantenraumzeit).
- F8-Vorhersage (vor dem Abruf, vor 15:05:51 date; ~~15:08~~ geschaetzt): Suche "Pachner moves", neueste zuerst: DT/CDT-Algorithmen, Spinschaum-
  Invarianz (Ponzano-Regge, Turaev-Viro), Tensornetze; dazu kanonische simpliziale Gravitation (Dittrich/Hoehn), in der
  ein Zeitschritt ein Pachner-Zug ist; keine Arbeit, die Pachner-Zuege als deterministische Wachstumsregel mit
  3+1-Ergebnis zeigt.
- F8 (8/14), 15:05:51-15:05:56, arXiv-API, quellen/F8-api-pachner.xml, 83 Treffer, alle Titel, 10 Abstracts.
  **Vorhersage eingetroffen (Dittrich/Hoehn gefunden); fuer die Karte der wichtigste Fund (in E5 nicht vorgesehen):**
  - Dittrich/Hoehn, "Canonical simplicial gravity" (arXiv:1108.1974, CQG 2012) [S Abstract]: "A discrete
    forward/backward evolution is realized by gluing/removing single simplices step by step ... and amounts to Pachner
    moves in the triangulated hypersurfaces ... the hypersurfaces evolve in a discrete 'multi-fingered' time through the
    full Regge solution"; Pachner-Zuege "generically change the number of variables, but can be implemented as canonical
    transformations".
  - Hoehn, "Canonical linearized Regge Calculus: counting lattice gravitons with Pachner moves" (arXiv:1411.5672)
    [S Abstract]: 4D linear um flach: "the 1-4 move generates four 'lapse and shift' variables ...; the 2-3 move
    generates a 'graviton'; the 3-2 move removes one 'graviton' and produces the only non-trivial equation of motion;
    and the 4-1 move removes four 'lapse and shift' variables".
  - Dittrich/Kaminski/Steinhaus, CQG 31, 245009 (2014), arXiv:1404.5288 [S Abstract]: 4D-Regge-Wirkung invariant unter
    5-1 und 4-2, aber "a local invariant path integral measure does not exist for the 4D linearized Regge theory".
    Borissova/Dittrich, JHEP 09 (2023) 069 [S Abstract]: lokales invariantes Mass fuer 3D-lorentzsches Regge,
    "obstructions in defining such a measure in 4D". -> passt zu PONZANO-1 (3D exakt, 4D nur naeherungsweise) [P].
  - Wachstumsregeln: Klales/Cianci/Needell/Meyer/Love, PRE 82, 046705 (2010) [S Abstract]: Gittergas auf 2D-
    Triangulierung, Geometrie per Pachner-Zug geaendert, Dreieckszahl waechst wie (Zeitschritte)^(1/3). Finkel 2006
    (hep-th/0601163): stochastische Graphen mit Pachner-aehnlichen Zuegen.
  - Teilchen als Zoepfe in Spin-Netzen, die per Pachner-Zug evolvieren (Smolin/Wan, NPB 796, 331 (2008); Bilson-
    Thompson-Modell in arXiv:2106.01332) [S Abstract]: "the braids ... commute with the evolution algebra generated by
    the local Pachner moves" -> ohne nichtlokale Zuege keine Wechselwirkung.
- F9-Vorhersage (vor dem Abruf, vor 15:06:34 date; ~~15:09~~ geschaetzt): Suche Quasikristall + E8 bzw. Irwin + Tetraeder: Arbeiten von Fang, Irwin,
  Sadler, Kovacs, Amaral u. a. auf arXiv; Zeitschriften hoechstens Tagungsbaende, MDPI oder Acta Phys. Pol. A; kein
  PRL/PRB; Verstoss waere ein Eintrag in einer etablierten Physik- oder Kristallographie-Zeitschrift.
- F9 (9/14), 15:06:34-15:06:35, arXiv-API, quellen/F9-api-e8-quasikristall.xml, 4 Treffer. **Bestaetigt E6, eine
  Zeile:** Baake/Gaehler 1998 (Aperiodic 97, World Scientific) [S Abstract]: "The 4D quasicrystal of Elser and Sloane,
  obtained from the root lattice E8 by the cut-and-project method"; Fang/Irwin (arXiv:1511.07786v4, Kommentar "Paper no
  longer used - updated", ohne journal_ref): 3D-Schnitte des Elser-Sloane-Quasikristalls "contain only regular
  tetrahedra"; Amaral/Clawson/Irwin 2023 (arXiv:2306.01964, ohne journal_ref): quasikristalline Spinschaeume auf EPRL-
  Basis, 600-Zelle. Grenze: fehlender journal_ref beweist keine fehlende Veroeffentlichung. Nebenbefund: Gorham/
  Laughlin (arXiv:1905.12165) zurueckgezogen ("incorrect assertion ... via the E8 lattice").
- F10-Vorhersage (vor dem Abruf, vor 15:06:52 date; ~~15:10~~ geschaetzt): kombinierte Suche persistente Homologie (kosmisches Netz, amorph, Glas) ODER
  emergente Geometrie (Zufallsgraphen, Simplizialkomplexe, Netzgeometrie): viele Arbeiten zur persistenten Homologie
  (etabliert, laufend 2024-2026); fuer emergente Geometrie mehrere Gruppen (Bianconi/Rahmede, Trugenberger, Kelly u. a.).
- F10 (10/14), 15:06:52-15:06:53, arXiv-API, quellen/F10-api-ph-emergent.xml, 27 Treffer. **E7 erster Teil bestaetigt,
  zweiter Teil gespalten:**
  - Persistente Homologie etabliert und aktiv: Glaeser und amorphe Festkoerper (2017-2025, u. a. arXiv:2407.17707,
    2507.05484), kosmisches Netz; neu: drei Arbeiten April 2026 bestimmen die Neutrinomasse aus der Topologie des
    kosmischen Netzes, z. B. arXiv:2604.02300 [S Abstract]: Unsicherheit 0,05 eV (gesamtes Materiefeld, Simulation).
  - Zufallsnetze: wenige Gruppen. Bianconi/Rahmede (arXiv:1607.05710) [S Abstract]: "an hyperbolic network geometry
    emerges spontaneously from models of growing simplicial complexes that are purely combinatorial" (Simplizes =
    "nodes, links, triangles, tetrahedra"); Bianconi (arXiv:1711.06290): "gluing different copies of an arbitrary
    regular polytope". -> Wachsen durch Ankleben von Tetraedern gibt hyperbolische, nicht flache 3D-Geometrie.
  - Kausalmengen: kein Einzelfall, sondern ein Programm "geometric reconstruction" (Surya 2019, lokal, S. 3-4) [S].
    -> E7 zweiter Teil fuer Kausalmengen VERLETZT, fuer Zufallsgraphen eingetroffen.
- F11-Vorhersage (vor dem Abruf, vor 15:07:19 date; ~~15:11~~ geschaetzt): id_list 1503.01324 (Lubensky u. a., Maxwell-Gitter: Kagome/Pyrochlor,
  Nullmoden auf Linien bzw. Ebenen), 1711.11044 (Pretko/Radzihovsky: Elastizitaet dual zu symmetrischer
  Tensor-Eichtheorie, Disklinationen = Fraktonen), 1001.0586 (Chen/Engel/Glotzer: Dimer-Packung 4000/4671 = 0,856347).
- F11 (11/14), 15:07:19, arXiv-API, quellen/F11-api-regime-packung.xml, 3 Treffer.
  - Chen/Engel/Glotzer, DCG 44, 253 (2010) [S Abstract]: "densest known packing of regular tetrahedra with density phi =
    4000/4671 = 0.856347 ... unit cell of four tetrahedra forming two triangular dipyramids (dimer clusters)". Mit
    Jones u. a. 2026 (lokal, Z. 32-34: "densest known bulk packings ... face-sharing tetrahedral dimers [25]") gilt der
    Rekord 2026 noch. **E1 vollstaendig bestaetigt.**
  - Lubensky/Kane/Mao/Souslov/Sun 2015 (arXiv:1503.01324) [S Abstract]: Indexsatz "N_0 - N_S = dN - N_B", Grenze
    z_c ~ 2d; Kagome als Beispiel. [M] Pyrochlor: z = 6 = 2d (jeder Platz in zwei Tetraedern mit je drei Nachbarn), also
    ein Maxwell-Gitter; die Calladine-Zaehlung 0 von TENSOR-EIS-PYRO-1 (A) ist genau dieser Satz. Pyrochlor selbst steht
    nicht im Abstract.
  - **ERWARTUNGSVERSTOSS gegen TETRAEDER-ANALYSE Abschn. 4 (Regime "steif" gegen "Regel"):** Pretko/Radzihovsky,
    PRL 120, 195301 (2018), arXiv:1711.11044 [S Abstract]: "elasticity theory of a two-dimensional quantum crystal is
    dual to a fracton tensor gauge theory ... disclinations and dislocations corresponding to fractons and dipoles ...
    The transverse and longitudinal phonons of crystals map onto the two gapless gauge modes". Steifigkeit und
    Tensor-Regel sind also (in 2D) zwei Schreibweisen derselben Theorie, kein Gegensatz von Mechanismen. Korrigierte
    Erwartung [ES]: Der Moderator ist nicht "steif oder Regel", sondern (i) Netzdimension (Kette schirmt ab, Volumen
    nicht; Projekt: TETRA-KETTE gegen WINKELFELD-1 2D E ~ R^2), (ii) Defektart (isotrope Dilatation koppelt in erster
    Ordnung nicht, Disklination stark), (iii) ob die Ladungen beweglich sind (Fraktonen sind es nicht).
- F12-Vorhersage (vor dem Abruf, vor 15:08:09 date; ~~15:12~~ geschaetzt): id_list 1606.00301 (Stenull/Kane/Lubensky: verallgemeinertes Pyrochlor als
  3D-Maxwell-Gitter, Weyl-Linien von Nullmoden), 0710.5515 (Castelnovo/Moessner/Sondhi: Monopole mit Coulomb-Kraft),
  cond-mat/0305401 (Hermele/Fisher/Balents: emergentes Photon), 1702.07613 (Pretko: Fraktonen-Gravitation, Mach),
  0912.4531 (Henley: Coulomb-Phase, Pinch-Punkte). Alle sollten TETRAEDER-ANALYSE 3.1/3.2 bestaetigen.
- F12 (12/14), 15:08:09-15:08:12, arXiv-API, quellen/F12-api-eis-frakton.xml, 5 Treffer. **Bestaetigt TETRAEDER-
  ANALYSE 3.1 und 3.2 im Wortlaut, mit einem Verstoss:**
  - Hermele/Fisher/Balents, PRB 69, 064404 (2004) [S Abstract]: Pyrochlor, U(1)-Spinfluessigkeit, Spinonen mit
    "electric" Ladung, Monopol, "a gapless 'photon' ... linearly dispersing". Castelnovo/Moessner/Sondhi, Nature 451, 42
    (2008) [S Abstract]: Monopole in Spin-Eis, Fluessig-Gas-Uebergang der Monopole. Henley, Annu. Rev. CMP (2010)
    [S Abstract]: Zwangsbedingung = divergenzfreier Fluss; "defects ... behave as effective charges with Coulomb
    interactions"; Pinch-Punkte. Stenull/Kane/Lubensky, PRL 117, 068001 (2016) [S Abstract]: verallgemeinerte
    Pyrochlor-Gitter mit topologischen Randzustaenden und "Weyl lines in their bulk phonon spectra" -> Finns Netz als
    3D-Maxwell-Gitter ist Literatur (Bezug EIS-1, TENSOR-EIS-PYRO-1 A).
  - **VERSTOSS gegen TETRAEDER-ANALYSE 4.2 ("Tensor-Regel = aussichtsreichster Weg zu Kraeften"):** Pretko, PRD 96,
    024051 (2017) [S Abstract]: Fraktonen plus emergentes Graviton; die Anziehung folgt aus Schwerpunkterhaltung, ist
    stets anziehend, aber "This force will generically be short-ranged, but we discuss how the power-law behavior of
    Newtonian gravity can arise under certain conditions". Korrigierte Erwartung [ES]: Eine Tensor-Regel gibt
    gravitonartige Moden, aber nicht von selbst eine Newton-Fernkraft; das 1/r in TENSOR-EIS-PYRO-1 stammt aus der
    Regge-Bauweise B1 (Laengen an Mitten), nicht aus dem Fraktonen-Mechanismus.
- F13-Vorhersage (vor dem Abruf, vor 15:09:04 date; ~~15:13~~ geschaetzt): Volltext Hoehn 2014 (arXiv:1411.5672): bestaetigt die Zaehlung je Pachner-Zug
  (1-4: vier Lapse/Shift, 2-3: ein Graviton, 3-2: Bewegungsgleichung, 4-1: entfernt); reine 1-4/4-1-Folgen tragen
  keine Gravitonen; Gitter-Beispiel oder "tent moves" fuer regelmaessige Netze; keine Aussage zu zwei Sublagen.
- F13 (13/14), 15:09:04, arXiv-PDF 1411.5672v2 -> quellen/F13-1411.5672.txt (E-Mails entfernt, PDF geloescht).
  **Vorhersage eingetroffen, mit Schaerfung fuer K-AM:**
  - S. 5 (Abschn. 3) [S]: "1-4 Pachner move: introduces 1 new vertex ... and 4 new boundary edges ... neither produces
    curvature (deficit angles) nor a Regge equation of motion"; "2-3 ... produces curvature through a single new deficit
    angle"; "3-2 ... produces one Regge equation of motion and three deficit angles"; "4-1 ... removes 1 old vertex ...
    four Regge equations of motion and six deficit angles"; 1-4 und 2-3 "canonical refining (or lattice growing)", 3-2
    und 4-1 "canonical coarse graining (or lattice shrinking)".
  - Abschn. 9, Satz 9.1 [S]: Zahl der Konfigurations-"Gravitonen" auf einer geschlossenen triangulierten Hyperflaeche
    E - 4V + 10 (4V - 10 unabhaengige Eckverschiebungs-Erzeuger).
  - Abschn. 12 [S]: in zweiter Ordnung brechen die Eichsymmetrien; "a hypersurface deformation algebra cannot exist in
    full 4D Regge Calculus".
  - [M] Ableitbarkeit TENSOR-EIS-PYRO-1: Eine B1-Kopie hat je primitiver Zelle V = 1 Eckplatz und E = 6 Kanten (die
    sechs Kanten eines Tetraeders), also E - 4V = 2 = zwei Gravitonen je Kopie; beide Kopien 4. Die Zaehlung war vorab
    aus der Literatur ableitbar (TE2-Zahl dort ohnehin [M]).
  - ~~[ES, aus S] CDT-Sandwich als Zugfolge: (4,1) auf einen Raum-Tetraeder kleben = 1-4-Zug, (3,2) = 2-3, (2,3) = 3-2,
    (1,4) = 4-1 (die (1,4) ist "time-reversal" der (4,1), AGJL S. 19). Ein reiner Auf/Ab-Takt aus (4,1) und (1,4), also
    1-4 und 4-1, erzeugt nach Hoehn keine Kruemmung, nur Lapse/Shift und Bewegungsgleichungen; Gravitonen kommen erst
    mit den 2-3-Zuegen, also den (3,2)-Simplizes.~~
    **Gestrichen vor 15:15:16 (date; ~~15:16~~ geschaetzt) (eigene Pruefung [M]):** Der Zugtyp haengt nicht am Simplex-Typ, sondern daran, wie viele seiner
    Tetraeder beim Kleben schon in der Hyperflaeche liegen (Hoehn S. 6 "in order of increasing number of identified
    tau"). Eine zweite (4,1) mit demselben Spitzenpunkt teilt schon die (3,1)-Seitenflaeche der ersten und ist dann ein
    2-3-Zug, kein 1-4. Haltbar bleibt nur: 1-4 und 4-1 (Punkt entsteht, Punkt vergeht) tragen allein keine Kruemmung
    [S S. 6]; jede Zugfolge zu einer Hyperflaeche mit E Kanten und V Ecken enthaelt mindestens E - 4V + 10 Zuege 2-3
    [S Satz 9.1, S. 17], und diese tragen die Gravitonen. Seitenzahlen = PDF-Seiten der lokalen Textkopie.
- F14-Vorhersage (vor dem Abruf, vor 15:10:23 date, ~~15:15~~ geschaetzt; Gegensweep-Pruefung): id_list 1203.1669 (Daya Bay 2012: theta_13 ungleich 0
  mit > 5 sigma, sin^2 2 theta_13 ~ 0,09), hep-ph/0202074 (Harrison/Perkins/Scott: tribimaximale Mischung mit
  U_e3 = 0), hep-ph/0106291 (Ma/Rajasekaran: A4 fuer Neutrinos). Erwartung: alles wie TETRAEDER-ANALYSE 3.3 und E2.
- F14 (14/14), 15:10:23-15:10:24, arXiv-API, quellen/F14-api-tbm-theta13.xml, 3 Treffer (Gegensweep-Pruefung).
  - Daya Bay, PRL 108, 171803 (2012) [S Abstract]: "a non-zero value for the neutrino mixing angle theta_13 with a
    significance of 5.2 standard deviations"; sin^2 2theta_13 = 0,092 +- 0,016 (stat) +- 0,005 (syst). Bestaetigt.
  - Harrison/Perkins/Scott, PLB 530, 167 (2002) [S Abstract]: Begriff "tri-bimaximal" (bimaximal nu_mu-nu_tau,
    trimaximal nu_e). U_e3 = 0 steht nicht im Abstract [L/M].
  - Ma/Rajasekaran, PRD 64, 113012 (2001) [S Abstract]: A4 = "the symmetry of the tetrahedron", Darstellungen 1, 1',
    1'', 3; Ziel: "a nearly degenerate neutrino mass matrix". **Verstoss gegen TETRAEDER-ANALYSE 3.3 (Chronologie):**
    Das A4-Papier (Juni 2001) ist aelter als der Begriff "tri-bimaximal" (Februar 2002); es "erklaerte" TBM nicht.
    Die Verbindung A4 -> TBM ist Altarelli/Feruglio 2005 [L, nicht abgerufen].
- **Abrufe erschoepft (14/14) um 15:10:24.** Ab hier nur lokale Lektuere und Schreibtisch.

## 4. Erwartungsverstoesse (getrennt, wichtigste zuerst; geschrieben vor 15:13:48 date; ~~Stand 15:12~~ geschaetzt)

1. **Regime "steif" gegen "Regel" ist kein Gegensatz** (gegen TETRAEDER-ANALYSE Abschn. 4.1/4.2): Elastizitaet eines
   2D-Quantenkristalls ist dual zu einer Fraktonen-Tensor-Eichtheorie (Pretko/Radzihovsky 2018) [S Abstract]. F11.
2. **Fraktonen-Anziehung "generically short-ranged"** (gegen TETRAEDER-ANALYSE 4.2 "aussichtsreichster Weg zu
   Kraeften"): Pretko 2017 [S Abstract]. F12.
3. **E5 zweiter Teil:** EDT mit Massterm ist aktive Gegenposition mit de-Sitter-Anspruch (Dai/Laiho u. a. 2024/25;
   Asaduzzaman/Catterall 2023) [S Abstract]; Hinweis schon in AGJL 2012 S. 118-119 ("crinkled") [S lokal]. F7.
4. **E7 zweiter Teil fuer Kausalmengen:** Programm "geometric reconstruction" (Surya 2019) [S lokal].
5. **E2 Gewichtung:** A4 an der Front nicht bevorzugt (minimale Fixpunktmodelle: nur S4' und A5 tragfaehig, Shang/Lu/
   Ding/King 2026); JUNO hat schon eingeschraenkt (Dutta u. a. 2026) [S Abstract]. F6.
6. **TETRAEDER-ANALYSE 3.3 Chronologie:** Ma/Rajasekaran 2001 vor "tri-bimaximal" 2002 [S Abstract]. F14.
- Nicht Verstoss, aber in keiner Erwartung vorgesehen (Neues): kanonische Regge-Zeitentwicklung durch Pachner-Zuege
  mit Graviton-Zaehlung (Dittrich/Hoehn 2012; Hoehn 2014) [S]; Tetraedergleichung = gestapelte Eis-Schichten und
  integrable Quantenschaltkreise [S Abstract]; A4 aus Orbifold-Fixpunkten [S Abstract]; Bianconi: Ankleben von
  Tetraedern gibt hyperbolische Geometrie [S Abstract]; TDA an DT (Loll u. a. 2025) und persistente Homologie ->
  Neutrinomasse (2026) [S Abstract]; Gold-Nanotetraeder bilden im Experiment Quasikristalle (Wang u. a. 2023, nur als
  Literaturzitat in Jones u. a. 2026 gelesen) [S Zitat].

## 5. Gegensweep (Was war so selbstverstaendlich, dass ich es nicht geprueft habe?) (geschrieben vor 15:13:48 date; ~~15:13~~ geschaetzt)

| Nr | Selbstverstaendlichkeit | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | "TBM ist seit theta_13 != 0 ausgeschlossen" | ja (F14, F6) | theta_13 != 0 mit 5,2 sigma [S]; exakte TBM hat U_e3 = 0 [L/M]; TM1 (erste TBM-Spalte) lebt [S] |
| G2 | "A4 erklaerte TBM von Anfang an" (TETRAEDER-ANALYSE 3.3) | ja (F14) | falsch in der Chronologie: A4 2001 vor TBM 2002 [S] |
| G3 | "Auf/Ab" ist in Pyrochlor und in CDT dasselbe | ja (lokal + M) | nein: Pyrochlor-Auf/Ab = raeumliche Inversion durch einen Eckplatz [M]; CDT-(1,4) = "time-reversal" der (4,1) [S AGJL S. 19]. K-AM vermischt beide |
| G4 | "Tetraedergleichung handelt von Tetraeder-Bausteinen" | ja (F3) | nein: Name aus der Raumzeit-Figur des Streuvorgangs [S] |
| G5 | "fehlender journal_ref = nicht begutachtet" (E6) | nein | Grenze vermerkt |
| G6 | "0,856 ist noch Rekord" | ja (lokal + F11) | Jones u. a. 2026 nennt die Dimer-Packung weiter "densest known" [S] |
| G7 | "Starre Netze schirmen ab" | ja (F11 + Projekt) | nur in Ketten; 2D-Volumen: Kegelquelle E ~ R^2 (WINKELFELD-1) [P]; Dualitaet [S] |
| G8 | "McKay 2T <-> E6" | nein | bleibt [L] (lokale Treffer nur Autorennamen) |
| G9 | "Kantenwerte koennen Auf und Ab koppeln" | ja [M] | nein: im Pyrochlor gehoert jede Kante genau einem Tetraeder, jede Ecke genau einem Auf und einem Ab |

## 6. Seitenzahlen berichtigt (vor 15:15:16 date, ~~15:16~~ geschaetzt; per Formfeed-Zaehlung in den lokalen Textkopien, PDF-Seiten)

- AGJL 2012: Pachner ergodisch S. 58; in CDT nicht direkt anwendbar S. 59; ~~S. 83~~ zerknuellt/verzweigt S. 84;
  ~~S. 118~~ D_S 4,02/1,80 S. 117; "crinkled" S. 119; (d,1)/(1,d) S. 19; Gl. (47) S. 26.
- Schoenhoefer u. a. 2023: "hard tetrahedra famously form quasicrystals" ~~S. 2~~ S. 1; 600-Zelle mit Leerstellen,
  rho 0,96 ~~S. 3~~ S. 2; Quasikristall-Umgebungen als Defekte ~~S. 4~~ S. 4 (bleibt).
- Jones u. a. 2026: Z. 29-34, S. 1. Loll 2019: S. 9. Surya 2019: S. 3. Pace u. a. 2020: S. 8 (Anhang).
- Hoehn 2014: Zuege S. 6; Satz 9.1 S. 17; Diskussion S. 26. Padmanabhan u. a. 2025: S. 1-2.

## 7. Schreibtisch nach den Abrufen (vor 15:15:16 date, ~~15:17~~ geschaetzt) [M, ES]

- [M] Pyrochlor: jede Ecke gehoert genau einem Auf- und einem Ab-Tetraeder, jede Kante genau einem Tetraeder. Werte auf
  Kanten koennen Auf und Ab deshalb nie direkt koppeln (TENSOR-EIS-PYRO-1 B1: zwei Welten), Werte auf Ecken koppeln sie
  immer (Spin-Eis: ein Spin-Umklappen erzeugt ein Paar auf einem Auf- und einem Ab-Tetraeder; Pace u. a.: E = +-S je
  nach A- oder B-Platz [S]).
- [M] B1-Kopie je primitiver Zelle: V = 1 (Ab-Mitte), E = 6 (Kanten des einen Auf-Tetraeders); E - 4V = 2 = zwei
  Gravitonen je Kopie. Hoehns Zaehlung ist die Literatur zu TE2 "4 statt 2".
- [M] Pyrochlor je primitiver Zelle: 4 Ecken, 12 Kanten, 2 Tetraeder, 2 Stumpf-Tetraeder; Volumenprobe 2 a^3/(6 sqrt2)
  + 2 (23 sqrt2/12) a^3 = 4 sqrt2 a^3 = (2 sqrt2 a)^3 / 4. Die Stumpf-Tetraeder sind die Loecher; wer sie mit
  Diagonalen trianguliert, verbindet Ecken verschiedener Tetraeder und koppelt so Auf und Ab [ES].
- [ES] Wachstum nur durch 1-4-artiges Ankleben von Tetraedern an Flaechen gibt "gestapelte" Komplexe mit baumartigem
  Dual (verzweigtes Polymer, AGJL S. 84 Fussn. 20: "A branched polymer is a tree graph") bzw. hyperbolische Netze
  (Bianconi/Rahmede [S Abstract]). Fuer WOLFRAM-SCAN-L K2 (Pachner-Familie) ist der negative Ausgang damit weitgehend
  ableitbar, sofern die Regel nur 1-4 nutzt; offen nur mit 2-3/3-2.
- Kalibrierungs-Warnzeichen: Meine Sicherheit fuer "K-AM hat eine Heimat in der kanonischen Regge-Rechnung" stieg mit
  einer Volltextquelle und zwei Abstracts schnell, waehrend "Flip-Flop" sich in drei Lesarten aufspaltete (raeumliche
  Inversion, Zeitumkehr (4,1)/(1,4), Zugpaar 1-4/4-1). Die gestrichene Zuordnung oben ist ein Beispiel.
## 8. Zeitfehler (Selbstanzeige, vor 15:15:46 date)
- Ich hatte Vorhersage- und Abschnittszeiten von Hand eingetragen (15:04 bis 15:17), die bis zu 3 Minuten NACH dem
  gemessenen Abrufbeginn lagen, also geschaetzt bzw. in der Zukunft. Alle durch date-Grenzen ersetzt, die alten Werte
  durchgestrichen stehen gelassen. Die Reihenfolge Vorhersage -> Abruf ist davon nicht beruehrt: Jede Vorhersage wurde im
  selben Befehl vor dem date-Aufruf und dem curl angehaengt.

## 9. Abgabe

- DOSSIER.md abgegeben 2026-10-04 15:24:04 CEST (date). Gegenlesen vorwaerts und rueckwaerts durch mich selbst (kein frischer Leser): Autorennamen von 2604.05641, 1711.06290, 2106.01332 berichtigt; "acht" lokale Volltexte zu "sechs" berichtigt; Zopfmodell aus der Generationen-Liste genommen (drei Baender = eine Generation); Seitenangabe Tetrahelix S. 2 und 3.
