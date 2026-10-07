# GLUONEN-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu lesen)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-04 17:01:23 CEST (date). Zeitbox 90 min, also Abgabe
  spaetestens um die Marke Start + 90 min (wird per date geprueft, nicht vorab eingetragen).
- Gestrichenes bleibt stehen (~~so~~). Offene Rueckfragen stehen in Abschn. 9 und wandern mit.
- Kennzeichen wie in der Karte: [S] an der Quelle gelesen (Zeile der lokalen Textkopie), [S Abstract], [P] Projektdatei,
  [L] Gedaechtnis, [L?] unsicher, [M] eigene Mathematik, [ES] eigener Schluss, [H] Hypothese.

## 0. Gelesen vor dem Projekt-grep (17:01:23 bis 17:01:41)

- KARTE.md (E1 bis E6 der Leitung, Fragen 1 bis 4).
- RUNDE-42/FARBE-SCHREIBTISCH.md: Biege-Triplett T2 hat U(3) harmonisch; x y z bricht anharmonisch auf T_d; Ecken-
  Kopplung C3v spaltet T2 -> A1 + E (harmonisch); Folge: lokal erhaltene SU(3) waere der Eichweg, kein kleiner Test.
- RUNDE-42.md ab 16:39 (Farbfrage Finn, Haken: Farbe lokal geeicht braucht Verbindungsgroessen; eps_ijk als
  Spatprodukt spiegelungsungerade [H]; Pati-Salam-Bild 1 + 3 [H]; KOPPLUNG-TETRA-1 gestartet 16:50:40).
- CHIRAL-L DOSSIER: Levin/Wen hep-th/0507118 lokal (RUNDE-37/twist-pyro-1/quellen/) Z. 1417-1444: "gauge bosons with
  any gauge group", "photons, gluons, leptons and quarks"; K-A braucht nichtabelsche String-Netz-Marken statt Pfeilen;
  nichtabelsch chiral in 3+1D offen.
- TETRAEDER-L DOSSIER: 2T = 24 Hurwitz-Einheiten [M]; K-A-Fadenenden spinlos (T, nicht 2T; TWIST-SPIN-1) [P];
  Kanten gehoeren genau einem Tetraeder, Ecken genau einem Auf- und einem Ab-Tetraeder [M]; R4 Kanten gegen Ecken.
- KOPPLUNG-TETRA-1 KARTE: KT3 (Eichprobe, 20 %): Energie entlang RUM nur von Ring-Holonomie abhaengig? Laeuft.

## 1. Erwartungen (aus der Karte, vor jedem Abruf festgelegt von der Leitung; gelten als E1-E6)

Siehe KARTE.md. Eigene Abruf-Erwartungen F1 ff. folgen in Abschn. 2, je vor dem Abruf mit date-Grenze.

## 1b. Projekt-grep (vor jedem Abruf; 17:01:41 bis 17:08:18)

- Muster (grep -r -i, ohne *VERSIEGELT*, T8-SOLL-*, vertraege-20260925, ks-1-dk-lauf(e), KS-1-Pfade, Geheimnis-Muster):
  gluon, nichtabel, non-abelian, quantenlink/quantum link, string-netz/string-net, quantendoppel/quantum double,
  1080er, petcher, weingarten, bhanot, rebbi, rishon, D-Theorie, zohar, wilson-schleife, flaechengesetz, einschluss,
  confinement, SU(3), Kitaev, Creutz.
- **Ergebnis: Keine Rechnung im Projekt mit nichtabelscher Eichgruppe.** Kein Treffer zu Quantenlinks, Quantendoppel,
  1080er-Gruppe, Petcher/Weingarten, Bhanot/Rebbi (nur Jackiw/Rebbi 1976 "spin from isospin", RUNDE-12/quark1 [P]).
  "Rishon" nur als Harari/Shupe-Preonen (faden-einordnung-20260909.md), nicht als Quantenlink-Rishon.
- Treffer, gelesen (Zeilen):
  - RUNDE-10/alt1/ALT-1.md Z. 135-146, 409-412, 541: nichtabelsche Wirbel (Auzzi u. a. 2003; Eto/Hirono/Nitta/Yasui
    2014; colorful boojums), "Kleinste Aenderung: ein nichtabelsches Eichfeld; das ist keine kleine Aenderung" [P].
  - RUNDE-35/graviton-netz-l/DOSSIER.md Z. 13, 100-101: String-Netze geben Eichbosonen und Fermionen ("photons,
    electrons, gluons, and quarks"), keine Gravitonen [P, dort S Levin/Wen].
  - RUNDE-37/kitaev-diamant-1/ERGEBNIS.md Z. 20-40, 225-240: Ryu-2009-Modell auf dem Diamantgitter nachgerechnet:
    Majoranas im **statischen Z_2**-Eichfeld, Fluesse durch Sechserringe erhalten; "Das Eichfeld ist Z_2, es gibt kein
    Photon" [P]. STRINGENDE-1: Z_2, Levin/Wen-2003-Modell [P].
  - RUNDE-37/weltmodell-review-1/REVIEW.md Z. 72, 178, 288: L6 "keine nichtabelsche Eichgruppe" [P]. WILSON-2D dort ist
    ein Wilson-**Fermion** (Schwerkraft-Antwort), keine Wilson-Eichwirkung.
  - RUNDE-12/quark1/QUARK-1.md: U(3)-Ball ist (Q,0)-Multiplett, nie Farbsingulett [P]; FL-Beutel = "scalar gluon" [P].
  - RUNDE-41.md Z. 246-266 und CHIRAL-L: nichtabelsch chiral in 3+1D offen; K-A braucht String-Netz-Marken [P].
  - RUNDE-40: kein Treffer.
- KOPPLUNG-TETRA-1 (17:08): code/, lauf-69/, rauch-69/ leer; quellen/ mit Wegner 2007 (cond-mat/0703486, RUM in
  Tetraederkristallen) und einem 404-Fehlabruf. Die Eichprobe ist also noch nicht definiert (Code fehlt) [P].
- Lokal vorhandene Volltexte, die ich ohne Abruf lesen darf: Levin/Wen hep-th/0507118 (twist-pyro-1/quellen und
  dyon-statistik-l/quellen), Pace u. a. 2009.04499, Wang/Senthil 1505.03520, Kaplan 0912.2560, Ryu 0811.2036 (PDF).

## 1c. Schreibtisch vor dem ersten Abruf (17:08, [M], nicht gegengelesen)

- **Zuordnung im Netz [M]:** Jede Ecke gehoert genau zwei Tetraedern (TETRAEDER-L [M]) und ist damit genau eine Kante
  des Diamantgitters der Mitten. Gitter-Eichtheorie auf dem Diamantgitter: Materie je Platz = je Tetraeder, Verbindung
  je Kante = je gemeinsamer Ecke, Feldstaerke je kleinster Schleife = je Sechsring, Gauss-Gesetz je Platz = je Tetraeder
  (vier Kanten). Genau so ist Quanten-Spin-Eis gebaut (Spin auf der Pyrochlor-Ecke = elektrisches Feld auf der
  Diamantkante, Eisregel = Gauss-Gesetz) [L, Hermele/Fisher/Balents 2004; im Projekt als S Abstract].
- **Verdrehung starrer Tetraeder ist reine Eichung [M]:** Hat jedes Tetraeder eine Lage O_i in SO(3) und ist die
  Verdrehung R_ij = O_i^-1 O_j, dann ist das Produkt um jeden Ring O_1^-1 O_2 O_2^-1 O_3 ... O_6^-1 O_1 = 1. Die
  Holonomie ist identisch 1, die Feldstaerke null. Die Energie haengt dann von Platzvariablen ab (Sigma-Modell auf
  SO(3), Elastizitaet), nicht von Schleifen. Nichttriviale Holonomie gibt es nur
  (a) mit eigener Variablen je Ecke (unabhaengig von O_i, O_j), oder
  (b) mit Defekten: Ist die Lage eines Tetraeders nur bis auf seine Drehgruppe T bestimmt (Ecken nicht beschriftet),
      kann ein Umlauf in einem Element von T zurueckkommen. Das ist eine Disklination; ihr Wert liegt in T bzw. bei
      Spinoren in 2T. pi_1(SO(3)/T) = 2T (Ueberlagerung SU(2) -> SO(3)/T mit Faser 2T) [M; Mermin 1979 L].
- **Folge fuer KT3 [ES]:** Definiert KOPPLUNG-TETRA-1 die Verdrehung als O_i^-1 O_j, ist "gleiche Holonomie" immer
  erfuellt (= 1), und "eichartig" hiesse "Energie null fuer alle Verdrehungen", also nur auf den RUM-Flaechen. Der
  Ausgang waere vorab ableitbar (verfehlt abseits der RUM, trivial erfuellt auf den RUM). Rueckfrage an die Leitung
  (Abschn. 9, R1).

## 2. Abrufe: Erwartung vor Abruf, Ausgang

Erwartungen F1 bis F3 geschrieben ab 2026-10-04 17:09:03 CEST (date), vor dem ersten Abruf.

| Nr | Quelle | Erwartung (vor Abruf) | Ausgang |
|---|---|---|---|
| F1 | Wiese, arXiv:2107.09335 (Volltext; Review Quantenlinks/D-Theorie) | Linkvariable = Operator aus Generatoren einer groesseren Algebra (U(N): SU(2N)), endlicher Raum je Kante; Rishons = Fermionen an den Kantenenden, U = c_x c_y^+, Rishonzahl je Kante erhalten; Kontinuum ueber 4+1D-Coulomb-Phase und Dimensionsreduktion; Vorlaeufer Horn 1981, Orland/Rohrlich 1990; Quantensimulation Banerjee u. a. 2013 | **bestaetigt bis auf Rishons** (17:09:17 bis 17:10:51, 6 S. gelesen). Einbettungsalgebra U(N)/SU(N): SU(2N) mit 4N^2-1 Generatoren (Z. 593-600); SO(N): SO(2N); Sp(N): Sp(2N); SU(2) am einfachsten mit SO(5), 5- bzw. 4-dim. Raum je Kante, Beispiel auf dem **Wabengitter** (Z. 611-656). Vorlaeufer Horn 1981, Orland/Rohrlich 1990, dann Chandrasekharan/Wiese 1997 (Z. 100-102, Lit. 39-41). D-Theorie: "(3 + 1)-d QCD arises from a non-Abelian Coulomb phase of a (4 + 1)-d SU(3) quantum link model, with chiral quarks arising naturally as domain wall fermions" (Z. 37-40); 1/g^2 = L0/e^2, xi ~ exp(24 pi^2 L0 / (11 N e^2 c)) (Z. 790-802); "due to confinement in (3 + 1)-d, xi cannot remain infinite" (Z. 790). Extra-Dimension "just a few lattice spacings" (Z. 465-466, U(1)-Fall). U(1)-Quantenlink mit Spin 1/2 je Kante in 3+1D "plausible" Coulomb-Phase (Z. 447-449). Kalte Erdalkali-Atome fuer SU(N)-Links (Z. 840-843, Lit. 19 Banerjee u. a.). **"Rishon": 0 Treffer** -> bleibt [L] |
| F2 | Levin/Wen, cond-mat/0404617 (Volltext; String-Netz-Kondensation) | Marken je Kante, Verzweigungsregeln je Ecke (dreiwertig), F-Symbole mit Pentagon; exakt loesbares H = -Sum Q_v - Sum B_p; in 2+1D topologische (gappe) Phasen, Gitter-Eichtheorie mit Gruppe G als Spezialfall (Marken = Darstellungen); masselose Eichbosonen nur als Ausblick fuer 3+1D. Also: "nichtabelsche Eichfelder" in 2+1 heisst topologisch, nicht Gluonen (E2 teils verletzt) | **bestaetigt, mit Verstoss gegen E2 im 3+1D-Teil** (gelesen Fluss-Text F2-levin-wen-fluss.txt). "all deconfined gauge theories can be understood as string-net condensates where the strings are essentially electric flux lines" (Z. 163-165); Marken = Darstellungen, Gauss-Gesetz: E1 x E2 x E3 muss die triviale Darstellung enthalten; SU(2): Dreiecksungleichung (Z. 319-329). 2+1D: "all discrete gauge theories, and all doubled Chern-Simons theories" (Z. 410-412), topologisch und gappt. **3+1D steht schon in derselben Arbeit (Abschn. V), nicht erst bei Walker/Wang:** symmetrische Tensorkategorien, "gauge theories coupled to bosonic or fermionic charges" (Z. 1574-1578); auf dreiwertigen 3D-Gittern ist H "not exactly soluble ... B_p do not commute in general" (Z. 1591-1593), eine Zusatzbedingung (32) ist noetig (Z. 1654-1671); in 3D nur bosonische oder fermionische Teilchen ohne gegenseitige Statistik (Z. 1729-1732); Fermionen aus "twisted gauge theories" (Z. 1755-1780) |
| F3 | Kitaev, quant-ph/9707021 (Volltext; Quantendoppel) | beliebige endliche Gruppe G; je Kante C[G] mit Orientierung; Eckoperator A_v^g (Eichtransformation), Plakette B_p^h (Fluss); H = -Sum A_v - Sum B_p; Anregungen = (Konjugationsklasse, Darstellung des Zentralisators); nichtabelsch fuer nichtabelsches G; T oder 2T nicht namentlich | **bestaetigt.** "Let G be a finite (generally, nonabelian) group ... H = C[G] ... dimensionality N = abs(G)" (Z. 531-535); "the value of a spin can be interpreted as a G gauge field" (Z. 557); Teilchen (C, chi) (Z. 859-861); Universalitaet mit S5, "Unsolvability of the group seems to be important" (Z. 1735-1736). **Neu und wichtig fuer die Verdrehung:** "the vertex variables ... are a Higgs field ... an arbitrary Hamiltonian can be written in a gauge-invariant form if we introduce additional Higgs fields. Of course, it is a very simple observation. The real problem is to understand how the artificial gauge symmetry 'materialize'" (Z. 493-497). Die Eichsymmetrie muss im Hamiltonian nicht exakt sein, sie "materialisiert" bei grossen Abstaenden (Z. 417-440) |

Nachtrag lokal (ohne Abruf, 17:11): Levin/Wen hep-th/0507118 (twist-pyro-1/quellen) Z. 72-78: Ref. [5] (= PRB 71,
045110 = F2) "can realize gauge bosons with any gauge group. However ... did not provide an explicit example of the most
physically relevant case a model realizing gauge bosons and fermions in (3+1) dimensions"; Z. 1417-1420: "one should be
able to construct a model that gives rise to SU (3) gauge bosons and massless Dirac fermions - that is, QCD" [S]. Das
Photon dort kommt aus einem **Rotormodell** (unendlich-dimensional), nicht aus einem exakt loesbaren String-Netz.
**Verstoss (V-c):** "Gluonen aus String-Netzen" ist eine Moeglichkeitsbehauptung ohne Bau; das Projekt (RUNDE-35
graviton-netz-l DOSSIER Z. 100-101) zitiert es staerker.

Erwartungen F4 bis F6 geschrieben ab 2026-10-04 17:12:02 CEST (date), vor dem Abruf.

| Nr | Quelle | Erwartung (vor Abruf) | Ausgang |
|---|---|---|---|
| F4 | Alexandru/Bedaque/Lamm/Lawrence, arXiv:1906.11213 (Volltext; S(1080) fuer Quantenrechner) | S(1080) ist die groesste "kristallartige" Untergruppe von SU(3); mit Wilson-Wirkung Ausfrier-Uebergang bei beta_f ~ 3,5 bis 4 (SU(3)-Normierung), unter dem Skalenbereich beta ~ 6; mit veraenderter Wirkung (Zusatzterm) kleinere Gitterabstaende (~0,08 fm); zitiert Bhanot/Rebbi 1981 (SU(3)-Untergruppen) und Petcher/Weingarten 1980 (SU(2)) | **bestaetigt, mit zwei neuen Zahlen** (17:12:21; Autoren zusaetzlich Harmalkar, Warrington; 1906.11213v2). "largest 'crystal-like' discrete subgroup of SU(3), S(1080) ... only 11 qubits" (Z. 49-51); "freezing" bei beta_f, danach "differs drastically from the continuous group" (Z. 58-66); "particular problem for asymptotically-free theories" (Z. 66-67); beta_f waechst mit der Gruppengroesse (Z. 83-84); Z_N fuer N > 4 im Skalenbereich (Z. 85-86). **SU(2): "BT has beta_f = 2.24(8), BO and BI have beta_f = 3.26(8) and beta_f = 5.82(8) ... scaling regime beta >~ 2.2"** (Z. 86-93): die binaere Tetraedergruppe 2T friert genau am Beginn des Skalenbereichs ein. SU(3): fuenf kristallartige Untergruppen S(60), S(108), S(216), S(648), S(1080), alle beta_f < 6; S(1080) beta_f = 3.58(2) (Bhanot/Rebbi 1981) bzw. 3.935(5) (Z. 137-145); mit Zusatzterm beta_1 Re Tr U_p (Z. 165-170) bis a ~ 0,08 fm, Kontinuumswert "agrees with the full SU(3) results" (Z. 19-22, 410). Petcher/Weingarten 1980 = Lit. [23] (Z. 596-597) |
| F5 | Greensite, hep-lat/0301023 (Volltext; Confinement-Review) | Wilson 1974: Flaechengesetz bei starker Kopplung fuer jede kompakte Gruppe (auch U(1)); kein Uebergang zwischen stark und schwach fuer SU(2)/SU(3) in 4D (Creutz 1980, Glaettung); U(1) mit Uebergang und Coulomb-Phase; Zentrumssymmetrie; ueber SU(N>=5) mit Volumenuebergang wahrscheinlich nichts | **teils bestaetigt, Kernsatz nicht gefunden.** "computer simulations of QCD, initiated by Creutz [2] in 1980, ... persuaded most skeptics" (Z. 36-39); "there exists no derivation of quark confinement starting from first principles" (Z. 41-43); kompaktes QED4 schliesst bei starker Kopplung ein (Monopol-Coulomb-Gas, Z. 5262-5264); Potential konkav, linear als Grenzfall (Z. 1422-1436). **Den Satz "kein Uebergang fuer SU(2)/SU(3) bei T = 0" habe ich per grep (phase transition, crossover, all couplings, weak coupling) nicht gefunden** -> bleibt [L]. Ergaenzt durch F1 Z. 443-446 (U(1) in 4D: Coulomb-Phase, schwach erster Ordnung getrennt) und Z. 783-791 (nichtabelsch Coulomb-Phase erst in 4+1D) |
| F6 | arXiv-API, id_list: 1104.2632 (Walker/Wang), 1211.2242 (Banerjee u. a.), 1211.2241 (Zohar/Cirac/Reznik), hep-th/9704106 (Brower/Chandrasekharan/Wiese), hep-lat/9609042 (Chandrasekharan/Wiese), hep-th/9511201 (Bais/de Wild Propitius) | Walker/Wang: 3+1D-TQFT aus verzweigten Fusionskategorien, exakt loesbares Gittermodell; Banerjee: Erdalkali-Atome, U(N)/SU(N)-Quantenlinks, Rishons (fermionisch) im Abstract; Zohar: SU(2) Yang-Mills mit kalten Atomen (abgeschnittene Kogut-Susskind-Links); Brower: QCD als Quantenlinkmodell, 5. Dimension; Chandrasekharan/Wiese: Quantenlinks diskret, Eichsymmetrie exakt; Bais: diskrete Eichtheorien aus gebrochenen kontinuierlichen (Higgs SU(2) -> H) | **bestaetigt, mit Verschiebungen** (6 Eintraege). Brower/Chandrasekharan/Wiese: "A rishon representation in terms of fermionic constituents of the gluons is derived" und 5. euklidische Dimension, "extent resembles the inverse gauge coupling" -> **Rishons dort, nicht bei Banerjee** [S Abstract]. Chandrasekharan/Wiese 1997: "U(1) and SU(2) quantum link models are constructed explicitly"; 5. Dimension: "universality arguments suggest that dimensional reduction ... occurs" [S Abstract]. Banerjee u. a. 2013: Erdalkali-Atome, U(N)/SU(N) mit fermionischer Materie, chirale Symmetriebrechung [S Abstract]. **Zohar/Cirac/Reznik 2013: SU(2) Yang-Mills "in 1+1 dimensions", Eichinvarianz aus Drehimpulserhaltung**, keine Quantenlinks [S Abstract]. Walker/Wang 2011: Levin-Wen nach 3+1D ueber "unitary braided fusion categories", Punkte und Defektschleifen [S Abstract]. Bais/de Wild Propitius 1995: planare Eichtheorien, per Higgs auf endliches H gebrochen; Langstrecke = diskrete H-Eichtheorie mit Aharonov-Bohm, Alice-Fluss, Cheshire-Ladung [S Abstract] |

Erwartungen F7 bis F10 geschrieben ab 2026-10-04 17:14:21 CEST (date), vor dem Abruf.

| Nr | Quelle | Erwartung (vor Abruf) | Ausgang |
|---|---|---|---|
| F7 | arXiv-API, Abstract: "gauge theory" UND nematic UND (tetrahedral ODER "point group"), alle Jahre | Liu/Nissinen/Slager/Wu/Zaanen 2016/17 (PRX/PRE): Gitter-Eichtheorie mit **diskreter Punktgruppe G als Eichgruppe** auf den Kanten, gekoppelt an O(3)-Rotoren je Platz; die Eichung kodiert die Ununterscheidbarkeit der Orientierung (Tetraeder: T); Phasen nematisch, "vestigial chiral" fuer T; keine Gluonen | (folgt) |
| F8 | arXiv-API, Abstract: (pyrochlore ODER "diamond lattice") UND (non-Abelian ODER nonabelian ODER "SU(2) gauge" ODER "SU(3) gauge"), alle Jahre | wenige Treffer; Parton-Spinfluessigkeiten mit SU(2)-Eichstruktur (Mittelfeld), nichtabelsche topologische Ordnung in 3D als Einzelfaelle; kein Gittermodell mit Gluonen auf Pyrochlor/Diamant | (folgt) |
| F9 | arXiv-API, letzte 24 Monate: "SU(3)" UND ("discrete subgroup" ODER "finite subgroup" ODER "crystal-like") | Lamm-Gruppe u. a.: Gatter fuer Sigma(36x3), Sigma(72x3), Sigma(216x3), S(1080); Wirkungen gegen Ausfrieren; kein Anspruch, dass eine endliche Gruppe a -> 0 erreicht | (folgt) |
| F10 | arXiv-API, letzte 24 Monate: (non-Abelian ODER SU(2) ODER SU(3)) UND "lattice gauge" UND (quantum computer/processor, trapped-ion, superconducting, qudit, Rydberg, cold atoms) | Experimente nichtabelscher Gittereichtheorie auf digitalen Quantenrechnern (Ionen/Qudits, supraleitend), meist 1+1D oder wenige Plaketten in 2+1D; mit kalten Atomen nichtabelsch hoechstens Vorschlaege -> E6 ("kalte Atome naechster Laborbezug") teils verletzt | (folgt) |

Ausgang F7 bis F10 (gelesen 17:14:52 bis 17:17:59):

- **F7 bestaetigt** (2 Treffer): Liu/Nissinen/Slager/Wu/Zaanen, PRX 6, 041025 (2016), arXiv:1512.07822: "discrete
  non-Abelian gauge theory ... a family of lattice gauge models encapsulating nematic ordering of general three
  dimensional point group symmetries ... vestigial phase carrying no more than chiral order ... I, O and T symmetric
  matter" [S Abstract]. Liu/Greitemann/Pollet, PRE 97, 012706 (2018), arXiv:1706.01811: "non-Abelian gauge theory ...
  arbitrary point-group symmetry"; Nematisch-isotrop-Uebergang "generically first-order for all polyhedral symmetries"
  [S Abstract]. -> Die Tetraedergruppe als Kanten-Eichgruppe ist ein bekannter Bau, aber fuer Orientierungsordnung.
- **F8 bestaetigt** (7 Treffer, alle Jahre): kein Modell mit Gluonen auf Pyrochlor/Diamant. Ryu 2009 (Projekt) und
  Si/Yu 2007 (arXiv:0709.1302: Kitaev-Verallgemeinerung auf dem Diamantgitter, geschlossene Strings mit "abelian
  statistics in the gapped phase and non-abelian statistics in the gapless phase") [S Abstract]; 5d-Pyrochlor:
  Spin-Bahn-Kopplung wirkt als **statisches** SU(2)-Eichfeld fuer Elektronen (arXiv:2103.13672) [S Abstract].
- **F9 bestaetigt** (3 Treffer, 24 Monate; zwei fachfremd): Osorio Perez/Murairi/Gustafson/Lamm 2025, arXiv:2511.17437:
  Gattersatz fuer die 216-elementige Sigma(72x3) [S Abstract]. Kein Anspruch auf a -> 0.
- **F10 verletzt E6** (33 Treffer, 24 Monate): Die nichtabelschen Laborlaeufe sind digital. Ionen-Qudits: "the first
  quantum simulation of genuine non-abelian string-breaking dynamics in a pure SU(2) lattice gauge theory ... on a
  trapped-ion quantum computer" (arXiv:2605.05841); IBM 156 Qubits: SU(2) auf Dreiecksgitter 8x8 und 16x8,
  Adjungierten-Stringbruch (arXiv:2608.28752); SU(2) in 1+1D, 60 Plaetze, "weak-coupling regime" (arXiv:2602.18080);
  SU(2) und SU(3) thermisch in 1D auf Ionen (arXiv:2501.00579). Kalte Atome mit Rishons: weiter Vorschlag, "Gauge-symmetry
  breaking is inevitable in established rishon-based schemes for alkaline-earth-like atoms" (arXiv:2506.14747) [alle S
  Abstract]. Dazu (30.09.2026): "no efficient formulation suitable for simulations near the continuum limit is
  currently known for the non-Abelian case"; Dual-Formulierungen nichtabelsch zwingend nichtlokal (arXiv:2609.39780)
  [S Abstract].
- Lokal (ohne Abruf): Pace u. a. 2009.04499 Z. 656-658: E und A "act on the edge of the diamond lattice (the premedial
  lattice of the pyrochlore lattice)", Rotation um "hexagonal plaquette" [S]. Bestaetigt 1c (Ecke = Diamantkante).

Erwartungen F11, F12 geschrieben ab 2026-10-04 17:17:59 CEST (date), vor dem Abruf.

| Nr | Quelle | Erwartung (vor Abruf) | Ausgang |
|---|---|---|---|
| F11 | Liu u. a., arXiv:1512.07822 (Volltext, PRX 2016) | H = -J Sum_<ij> Tr(R_i^T U_ij R_j) - K Sum_Plakette Tr(U U U U), U_ij in G (Punktgruppe), R_i in O(3) bzw. SO(3) je Platz; die Eichung entfernt die Ununterscheidbarkeit der Orientierung; Phasen: isotrop, G-nematisch, vestigial chiral (fuer T, O, I); Defekte ueber Homotopie (pi_1 = Doppelgruppe) erwaehnt; kubisches Gitter | **bestaetigt** (17:18:24, 17 S., Fluss-Text). "O(3)/G lattice gauge theory ... O(3) triads R_i defined on sites and gauge fields U_ij in G defined on links" (Z. 389-390); beta H = -Sum Tr(R_i^T J U_ij R_j) - Sum K_C delta_C(U_Plakette) Tr U (Z. 395-398); Eichung R_i -> Lambda_i R_i, U_ij -> Lambda_i U_ij Lambda_j^T (Z. 404-409); erster Term "is nothing but a Higgs term [54] for the matter fields R_i" (Z. 418-419); Plaketten mit U != 1 "represent topological defects in the nematic" (Z. 429-431); Defekte ueber Homotopie von O(3)/G (Z. 439-441), Doppelgruppe nicht woertlich; grosses K, kleines J: "deconfining phase with topological gauge fluxes as excitations ... deconfinement seems unphysical dealing with 'molecular' matter" (Z. 307-312); "With deconfined gauge fields and disordered rotors ... (non-Abelian) topological excitations and topological order ... no identified analogues in thermal liquid crystal systems" (Z. 719-726); Fel 1995 zu Tetraeder-Nematen zitiert (Z. 1853) |
| F12 | arXiv-API, 24 Monate: emergent UND (non-Abelian gauge, SU(2)/SU(3) gauge, gluon, Yang-Mills) UND (spin, lattice model, string-net, spin liquid, bosonic) | Regel-7-Pruefung meiner Negativaussage: kein lokales bosonisches 3+1D-Modell mit masselosen nichtabelschen Eichbosonen gebaut; Treffer: Parton-Spinfluessigkeiten (SU(2) gappt/Higgs), 2+1D-Chern-Simons, emergente SU(2) an Punkten (Dirac-Spinfluessigkeit) | **im Kern bestaetigt, mit einem Verstoss** (50 Treffer, viel Rauschen durch "spin"/"gluon"). Kein Bau gefunden. Aber: **Chandrasekharan 2026 (arXiv:2602.22515)**: qubit-regularisierte Hamilton-Eichtheorien "naturally realize both confined and deconfined phases"; "we argue that second-order quantum phase transitions separating the confined and deconfined phases are likely to exist. Such critical points would provide a nonperturbative route to defining continuum limits ... potentially allowing Yang-Mills theory ... to emerge from finite-dimensional lattice constructions" [S Abstract] -> zweiter Kontinuumsweg neben der D-Theorie, ohne Zusatzdimension, begruendet, nicht gezeigt. Feuerpfeil u. a. 2026 (arXiv:2601.19980): SU(2)-Eichfeld in Parton-Theorien (2+1D) [S Abstract]. Wang/Yao 2025 (arXiv:2504.16694): Biexzitonen auf den Kanten eines Wabengitters bilden ein Kagome-Gitter, "governed by a genuine non-Abelian lattice gauge field" (statisch, Huepfen als Linkvariable) [S Abstract] |

Bewertung F11-F12 (17:25:29): F11 bestaetigt -> Kernbefund V2 (Verdrehung = Higgs-Term, T-Fluss = Defekt).
F12: Regel 7 erfuellt; keine Negativaussage "unmoeglich" erlaubt; Chandrasekharan 2026 ist ein Erwartungsverstoss gegen
meine eigene Schreibtisch-Vermutung (V-g, siehe Abschn. 8 Gestrichenes). **Budget: 12 von 12 Abrufen verbraucht** (alle
mit Inhalt). Ab hier nur noch lokale Lesungen.

Bewertung F4-F6 (17:13:32): F4 bestaetigt E3 im Kern; neu ist die Zahl fuer 2T (beta_f = 2,24 am Rand des
SU(2)-Skalenbereichs) und dass S(1080) mit Zusatzterm den Skalenbereich doch erreicht (V-d: "friert ein" ist keine
Endstation). F5: Kernsatz von E5 an dieser Quelle nicht gefunden (V-e, schwach). F6: Rishons gehoeren zu
Brower/Chandrasekharan/Wiese 1997/99; Zohar u. a. ist 1+1D und ohne Quantenlinks (V-f, klein).

Berichtigung 17:30 (Zeilen per grep nachgeprueft): F1 "just a few lattice spacings" Z. 463 (nicht 465-466);
Gl. (3.9) SU(2N) Z. 598 (nicht 593-600); SU(2)-Spinor (jL, jR) = (1/2, 0) oder (0, 1/2) Z. 657 (nicht 646-653, so
auch in Abschn. 3); 4+1D-Coulomb-Phase Z. 783; "due to confinement in (3 + 1)-d" Z. 790; SU(2) = SO(3) = Sp(1) Z. 615.

Bewertung F1-F3 (17:10:51): F1, F3 bestaetigen -> je eine Zeile. Verstoesse: (V-a) E2: 3+1D-Verallgemeinerung steht in Levin/Wen 2004 selbst und ergibt dort nur Eichtheorien endlicher Gruppen (symmetrische Tensorkategorien), nicht masselose Gluonen; (V-b) Rishons nicht im Review. Kitaev Z. 493-497 stuetzt meinen Schreibtischpunkt 1c (Verdrehung O_i^-1 O_j = Higgs-Form, trivial).

## 3. Fragen 1-4: Notizen (ab 17:25:29)

- F1 Bauweisen: Tabelle in DOSSIER Abschn. 3 (Wilson/Kogut-Susskind, Quantenlink/D-Theorie, String-Netz, Quantendoppel,
  endliche Untergruppe, Punktgruppen-Eichtheorie). Je Kante / je Ecke / je Schleife / Kontinuum / Einschluss.
- F2 Finns Netz [M + S Pace]: Tetraeder = Platz (Gauss-Gesetz, Ladung, "Quark"), Ecke = Kante (Linkvariable, "Gluon"),
  Sechsring = Plakette. Jede Diamantkante liegt in 6 Sechsringen [M, von Hand gezaehlt: Ringe = geordnete Tripel
  (i,j,k) verschiedener Bindungsrichtungen, Weg +a_i -a_j +a_k -a_i +a_j -a_k; 12 Ringe je Platz, 6 je Kante].
- **Farbiges Pfeil-Eis [M, aus F6-Abstract (Rishons) und F1 (Gauss-Gesetz, SU(2N)) abgeleitet, nicht an der Quelle
  geprueft]:** Kleinster Quantenlink je Ecke = ein Rishon (Fermion mit Farbindex) am Auf- oder am Ab-Ende der Ecke, also
  2N Zustaende (SU(3): 6 = Pfeilrichtung x 3 Farben). k = Zahl der Rishons an den Ecken eines Tetraeders.
  - U(1) (Pfeil-Eis, Spin 1/2 je Ecke): k = 2 genau ("zwei rein, zwei raus").
  - SU(2) (SO(5)-Spinor, F1 Z. 646-653): k gerade, k in {0, 2, 4}, Singulett-Vielfachheit 1, 1, 2.
  - SU(3), Rishonzahl 1: k = 0 mod 3, also k in {0, 3}; k = 3 ist der eps_abc-Knoten (Baryon-Knoten): drei Ecken
    tragen Farbe, eine nicht ("3 + 1").
  - Klassischer Schatten [M]: Fuer Marken {1, 3, 3quer} ist "enthaelt ein Singulett" gleich "Trialitaet = 0 mod 3",
    also eine Z_3-Eisregel (Zentrum von SU(3)); das Nichtabelsche steckt nur in Vielfachheiten und Amplituden.
  - Pauling-Schaetzungen [M]: U(1) ln(3/2) = 0,405 je Tetraeder; SU(2) gewichtet ln(9/4) = 0,811; SU(3) minimal
    ln(5/4) = 0,223. (Wabengitter, SU(3) minimal: Pauling negativ, also wohl starr.)
  - Ringterm Tr(U U U U U U) laesst jedes k_x unveraendert [M] -> Sektoren nach {k_x}.
- Verdrehung: reine Eichung (1c); T-Fluss = Disklination; O(3)/T_d-Eichtheorie = Higgs-Term + Defektterm (F11).
  Finns Tetraeder sind regulaer (T_d mit Spiegeln); fuer die Tetraeder-"Materie" waere G = T_d (24 Elemente, = S4),
  T (12) nur fuer chirale Bausteine [M].
- Reicht SO(3)/T/2T? SO(3): 3 Eichbosonen, reelles Triplett (Quark = Antiquark) [M]; T, 2T: diskret, topologisch;
  2T als SU(2)-Ersatz grenzwertig (beta_f 2,24 gegen 2,2, F4); nichts Tetraedrisches naehert SU(3) (alle fuenf
  kristallartigen SU(3)-Untergruppen beta_f < 6, F4).
- F3 Einschluss/Kontinuum: siehe DOSSIER Tabelle; Kern: Bei starker Kopplung schliessen alle kompakten Gruppen ein
  (auch U(1)), getrennt wird bei schwacher Kopplung.

## 4. Regime und Moderatoren (17:25)

| Scheinbarer Widerspruch | Moderator | Regime A | Regime B |
|---|---|---|---|
| "String-Netze geben Gluonen" gegen "exakt loesbare 3+1D-String-Netze sind Eichtheorien endlicher Gruppen" | Markenmenge (endlich gegen alle Darstellungen von SU(3)) und Phase (deconfined gegen eingeschlossen) | endlich: topologisch, gappt (F2) | SU(3): ~~keine deconfined Phase in 3+1D~~ keine Coulomb-Phase in 3+1D (berichtigt 17:38); Gluonen nur kurzreichweitig (F1 Z. 783-791) [ES] |
| "Endliche Untergruppe ersetzt SU(3)" gegen "friert ein" | beta gegen beta_f; Wirkung; Gruppengroesse | beta < beta_f: SU(N)-artig | beta > beta_f: diskrete Theorie (F4) |
| "Quantenlinks geben Licht" gegen "SU(N)-Quantenlinks schliessen ein" | abelsch/nichtabelsch; Raumdimension | U(1) 3+1D: Coulomb-Phase (F1 Z. 443-449) | SU(N): Coulomb erst in 4+1D (F1 Z. 783-791) |
| "Verdrehung = Kleber" gegen "Verdrehung = Higgs" | eigene Variable je Kante? Defektkosten K gegen Ausrichtung J | O_i^-1 O_j: reine Eichung/Higgs [M; F3; F11] | grosses K, kleines J: deconfined T-Fluss, topologisch (F11) |
| Leitung: stark gegen schwach | Kopplung | stark: alle Gruppen Flaechengesetz (F5 Z. 5262; F1 Z. 443) | schwach: U(1) Licht, endlich eingefroren, SU(N) asymptotisch frei |

Kopplung vor Bauteil (Regel 6) [ES]: Wilson-Links, Quantenlinks mit 5. Dimension, String-Netze, Partonen, qubit-
regularisierte kritische Punkte: fuenf Wege. Gemeinsame Groesse: die effektive Kopplung am Gitterabstand und ihr Fluss
(beta; L0/e^2 in der D-Theorie, F1 Z. 790-802; Abstand zu beta_f; Naehe zum kritischen Punkt). Der Baustein (Gruppe,
Marke) entscheidet nur, ob dieser Fluss existiert.

## 5. Unterscheidungspunkte (17:25)

- Endliche Gruppe gegen SU(N): oberhalb beta_f (Plakette springt, Hysterese; F4 Z. 118-121: "agree very well until
  they abruptly diverge"). Fuer 2T gegen SU(2) liegt der Punkt am Beginn des Skalenbereichs -> K1.
- Verdrehung als Eichfeld gegen Higgs: Holonomie um den Sechsring (identisch 1 gegen schwankend); Energie nur von
  Holonomie abhaengig. Mit O_i^-1 O_j nicht unterscheidbar (R1).
- String-Netz-SU(3) gegen eingeschlossenes SU(3): bei Abstaenden groesser 1/Lambda nicht unterscheidbar (beide
  Flaechengesetz); nur bei kurzen Abstaenden (asymptotische Freiheit) [ES].
- D-Theorie gegen kritischer Punkt (Chandrasekharan 2026): Ordnung des Uebergangs zwischen eingeschlossen und deconfined
  in 3+1D (zweiter gegen erster Ordnung) [S Abstract]; mit kleinen Tests nicht zugaenglich.
- 2+1D gegen 3+1D bei Quantendoppeln: Statistik von Punktteilchen (nichtabelsch nur in 2+1D; F2 Z. 1729-1732).

## 6. Gegensweep (17:25): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Einschluss bei starker Kopplung ist nichtabelsch | ja (F5 Z. 5262-5264; F1 Z. 443-446) | nein, auch kompaktes U(1) |
| G2 | Gluonen brauchen eine kontinuierliche Gruppe | ja (F4) | praktisch nein: S(1080) mit Zusatzterm trifft SU(3) bis a ~ 0,08 fm; streng a -> 0 nicht |
| G3 | Ecke = Diamantkante, Plakette = Sechsring | ja (Pace Z. 656-658 [S]; Zaehlung [M]) | ja; 6 Sechsringe je Kante |
| G4 | Die Verdrehung ist ueberhaupt eine Verbindung | ja ([M]; F3 Z. 493-497; F11 Z. 418-419) | nur reine Eichung (Higgs-Term) |
| G5 | Ein klassischer 3D-Test spricht fuer 3+1D | nein, [ES] | 3D-klassisch = (2+1)D-Quantenphysik; fuer Finns 3+1D braucht es Diamant x Zeit (4D) -> in K1 eingebaut |
| G6 | Finn meint mit "Gluonen" SU(3) mit 8 Gluonen | nein | Rueckfrage R2 |
| G7 | Levin/Wen haben Gluonen gebaut | ja (lokal hep-th/0507118 Z. 72-78, 1417-1420) | nein, Behauptung |
| G8 | Niemand hat 3+1D nichtabelsche Eichbosonen emergent gebaut (Regel 7) | ja (F12) | kein Bau gefunden; Chandrasekharan 2026 begruendet einen Weg |
| G9 | Finns Netz hat 2T | ja (TWIST-SPIN-1 ueber TETRAEDER-L [P]) | nein: Fadenenden spinlos, T; 2T erst mit Spinoren |

## 7. Kartenvorschlaege: Ableitbarkeitsprobe (17:25)

- K1 ZWEI-T-AUSFRIER-1 (2T gegen SU(2) auf Diamant x Zeit; Verhaeltnis r = beta_f(2T) / beta_peak(SU(2))):
  Hyperkubus r ~ 1,02 (F4) -> Vorzeichen von r - 1 auf Finns Gitter nicht ableitbar; vorher Mittelfeld-Schaetzung am
  Schreibtisch (Flyvbjerg 1984 [S Zitat in F4]); liegt sie weit weg von 1, wird der Test ableitbar und entfaellt.
- K2 FARB-EIS-1 (Zaehlung und Ergodizitaet der Gauss-Gesetz-Zustaende fuer U(1), SU(2), SU(3) minimal auf periodischen
  Diamant-Haufen): Pauling ableitbar, exakte Entropie und Zerfall in Sektoren unter dem Sechsring-Zug nicht; keine
  Quelle (F8). Notwendige Bedingung fuer resonierenden Farbkleber, kein Gluonennachweis.
- Verworfen: PUNKTGRUPPE-DIAMANT (O(3)/T_d auf Finns Netz): Phasen generisch, Uebergang generisch erster Ordnung (F7),
  Finns geordnetes Netz liegt tief in der Higgs-Phase -> ueberwiegend ableitbar. S(1080) auf Finns Netz: Abstand
  beta_f/6 ~ 0,6 auf dem Hyperkubus -> Ausgang ableitbar (scheitert ohne Zusatzterm). EICHPROBE-RING (Disklination im
  Federnetz): E ~ R^2 wie im Kristall [L], weitgehend ableitbar; nur als Hinweis an KOPPLUNG-TETRA-1 (R1).

## 8. Gestrichenes

- ~~[ES, 17:10] "Ein SU(3)-Quantenlinkmodell direkt auf Finns 3D-Netz (3+1D) hat ohne 5. Dimension keine
  Kontinuumsgrenze."~~ Gestrichen 17:25: zu stark. F1 sagt nur, dass nichtabelsch in 3+1D eingeschlossen wird und die
  D-Theorie die 5. Dimension nutzt; Chandrasekharan 2026 (F12) begruendet einen Weg ueber kritische Punkte endlicher
  Gittermodelle. Neu: "nach Recherchestand offen; zwei Vorschlaege (D-Theorie, kritischer Punkt)".
- ~~[ES, 17:08] "Mechanik kann keine Eichfelder tragen."~~ Gestrichen 17:25 (nie in eine Datei uebernommen, nur als
  Gedanke vermerkt): Elastizitaet ist in 2D dual zu einer Tensor-Eichtheorie (Pretko/Radzihovsky, TETRAEDER-L V1 [P]).
  Richtig ist nur: Die **Verdrehung als Verbindung** ist reine Eichung [M]; der Dualitaetsweg ist abelsch, und fuer
  nichtabelsche Gruppen sind Dual-Formulierungen in einer Klasse zwingend nichtlokal (arXiv:2609.39780 [S Abstract]).
- ~~[ES, 17:25] "Fuer SU(N) gibt es in 3+1D keine deconfined Phase."~~ Berichtigt 17:38 im Rueckwaertsdurchgang: F1
  traegt nur "keine masselose Coulomb-Phase" (Coulomb-Phase erst in 4+1D, Z. 783-790); Chandrasekharan 2026 nennt
  deconfined Phasen qubit-regularisierter Modelle (Art aus dem Abstract nicht erkennbar).
- ~~DOSSIER-Entwurf: "Zohar u. a. ... ohne Quantenlinks"~~ (17:38): steht nicht im Abstract, gestrichen.
- ~~DOSSIER-Entwurf: "Ein T-Eichfeld gibt es nur ueber Disklinationen"~~ (17:38): zu stark (Quantendoppel D(T) setzt T
  direkt auf die Kanten); ersetzt durch "Als T-Eichfeld beschreibt sie Disklinationen".
- ~~DOSSIER-Entwurf: "etwa 3000 Links"~~ (17:38): nachgerechnet 972 (Diamant L = 3, L_t = 6) bzw. 1024 (4^4).

## 10. Abschluss

- DOSSIER.md geschrieben ab 17:30:39, Rueckwaertsdurchgang (Zeilennummern per grep, zu starke Stellen) bis 17:38.
- Abgabe 2026-10-04 17:39:07 CEST (date). Offene Rueckfragen R1 bis R3 stehen in Abschn. 9 und im DOSSIER Abschn. 13.

## 9. Offene Rueckfragen (wandern mit)

- R1 (17:08, an die Leitung, fuer KOPPLUNG-TETRA-1): Wie ist die Verdrehung in der Eichprobe KT3 definiert? Als
  O_i^-1 O_j ist die Ring-Holonomie identisch 1 [M]; dann ist KT3 vorab ableitbar. Pruefbar wird KT3 nur mit einer
  eigenen Variablen je Ecke oder mit einer Disklination im Ring (Holonomie in T).
- R2 (17:25, an Finn ueber die Leitung): Meint "Gluonen" die acht SU(3)-Gluonen der starken Kraft, oder jeden
  nichtabelschen Kleber (auch SU(2) oder eine diskrete Gruppe)? Davon haengt ab, ob 2T (K1) ueberhaupt zaehlt.
- R3 (17:25, offen, Literatur): Wahl der Rishonzahl im SU(3)-Quantenlink (1 oder N) bei Brower/Chandrasekharan/Wiese;
  nur Abstract gelesen. Fuer K2 vor dem Bau im Volltext pruefen.
