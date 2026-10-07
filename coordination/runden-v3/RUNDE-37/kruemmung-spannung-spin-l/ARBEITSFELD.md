# ARBEITSFELD KRUEMMUNG-SPANNUNG-SPIN-L (feldforscher fuer claude-primary)

- Start 2026-10-05 10:37:27 CEST (date). Arbeitsfeld ab 10:44:10 CEST (date).
- Karte KARTE.md gelesen (unveraendert, KS1 bis KS5 bindend). Projektdateien gelesen: TORSION-STEIF-1/ERGEBNIS.md,
  WELTKRISTALL-L/DOSSIER.md, GUERTEL-FINN-NETZ-1/ERGEBNIS.md (Kopf, Ergebnis zuerst), GEN-04-SPIN-HALB.md,
  RUNDE-44 (Ernte REGGE-TORSION-L), RUNDE-22 Z. 390-424, SOC-RAUM-L/DOSSIER.md (Kopf, grep).
- Kennzeichen: [S] Quelle gelesen (Stelle), [S Abstract], [L] Gedaechtnis, [P] Projekt, [M] Mathematik, [ES] Schreibtisch,
  [H] Hypothese. Gestrichenes bleibt stehen (~~so~~).
- Budget: hoechstens 20 Abrufe, Zeitbox 90 min ab 10:37:27, also bis 12:07:27 (Rechnung aus der Startzeit, keine
  Schaetzung einer Endzeit der Arbeit).

## 0. Projektfunde vor jedem Abruf (lokal, keine Abrufe)

- P1 CDT-Geon-Hinweis 2025 ist im Projekt schon bestimmt: RUNDE-22/geometrie-stand/ARBEITSFELD.md Z. 144-150:
  arXiv 2504.11047 und 2510.21248 (Maas/Plaetzer/Pressler 2025, Autoren dort [L?]); Kruemmungskorrelatoren in 4D-CDT
  "consistent with a massive state", "at most a hint", Masse haengt an der Expansionsphase; kein Spin bestimmt
  [P, dort S Abstract].
- P2 Bowick/Giomi 2009 (0812.3064) und Bowick/Nelson/Travesset 2000 (cond-mat/9911379) liegen als Volltext lokal:
  RUNDE-22/geometrie-stand/hilfs/. Dazu Carlip gr-qc/9503024 (2+1-Gravitation), Katanaev cond-mat/0407469
  (Defekttheorie), Kleman/Friedel 0704.3055. Lesen ohne Abrufzaehlung, als "lokal gelesen" kennzeichnen.
- P3 SOC-RAUM-L (RUNDE-48) kennt schon: Dickman u. a. 2000 / Vespignani-Zapperi 1998 (SOC = absorbierender Zustand mit
  verstecktem Parameter), Tewari u. a. 1999 (Schaum, T1-Lawinen nur nass), Bonachela/Munoz 2009, Lin u. a. 2014.
  Kruemmung/Fehlwinkel als umverteilte Sandhaufen-Groesse kommt dort NICHT vor (grep "kruemmung|gauss|fehlwinkel":
  nur Z. 50, 133, 192, 194, 375, alle anderer Inhalt).
- P4 REGGE-TORSION-L Abruf A3 (04.10.): arXiv-Suche torsion AND (Regge OR simplicial OR spinfoam), 118 Treffer, keine
  Arbeit mit Fermionen + Torsion auf Simplexen (24-Monats-Fenster damit schon einmal abgedeckt) [P].
- P5 Seung/Nelson-Beulen im Projekt nur [L?] (RUNDE-22 ERGEBNIS Z. 135-136, 217; RUNDE-23 kugelschale-1 gamma ~ 154).
- P6 Projekt-grep (zwischen 10:37:27 und 10:44:10 nach date-Grenzen; Zeitpunkt selbst nicht gemessen; alle *.md, Ausschluesse wie vorgeschrieben): Friedman/Sorkin, spinorial, Giulini (Geon-Bezug),
  Aneziris, Hendriks, Duston/topspin: keine Treffer zum Geon-Thema. Geon-Spin ist im Projekt nicht gelesen.

## 1. Abrufprotokoll (Erwartung VOR dem Abruf, Ausgang danach)

- **Erwartung vor Abruf 1** (WebFetch arXiv-API id_list, 5 Abstracts; date beim Eintragen 10:44:37):
  - gr-qc/9609064 = Dowker/Sorkin, "A spin-statistics theorem for certain topological geons": Spin-Statistik gilt fuer
    eine Klasse von Geonen in einer Summe ueber Geschichten MIT Topologieaenderung (Paarerzeugung).
  - 2504.11047 = Maas u. a. 2025, Geon-Hinweis aus Kruemmungskorrelatoren in 4D-CDT, "at most a hint", kein Spin.
  - 2510.21248 = Folgearbeit, Abhaengigkeit von der kosmologischen Zeit, kein Spin.
  - 0712.4393 = Kostelecky/Russell/Tasson 2008: Schranken auf HINTERGRUND-Torsion (Komponenten bis ~1e-31 GeV) aus
    Lorentz-Verletzungs-Schranken; Einstein-Cartan im Abstract nicht genannt.
  - 0910.2574 = Giulini, "Matter from Space": Uebersicht Wheeler-Geonen, Friedman/Sorkin, spinorielle Mannigfaltigkeiten.
- **Ausgang Abruf 1** (quellen/A1-arxiv-api-idlist.txt) [S Abstract, ueber WebFetch]:
  - Dowker/Sorkin: bestaetigt mit Praezisierung. "In a theory without topology change there is no obstruction to
    'anomalous' spin-statistics pairings for geons." Mit Topologieaenderung: "non-chiral abelian geons do satisfy a
    spin-statistics correlation if ... functional integral over metrics on a particular four-manifold", das "creates a
    pair of geons from R^3". Klasse = nicht-chirale abelsche Geonen; Prozess = PAARERZEUGUNG aus R^3, nicht ein
    Hosenbein (eine Raumschicht -> zwei). Kleine Abweichung zur Wortwahl in KS2, nicht zum Kern.
  - Maas/Plaetzer/Pressler 2504.11047: bestaetigt, inzwischen Phys. Lett. B 879 (2026) 140600. Gezeigt: Kruemmungs-
    Kruemmungs-Korrelatoren "consistent with a massive state ... over a certain distance window", "at most a hint".
    Geon hier = selbstgebundene GRAVITONEN (Wheeler-Typ), nicht topologischer Geon; Spin wird nicht bestimmt.
  - 2510.21248 heisst "Composite objects in quantum (super)gravity": Geonen brauchen zusammengesetzte Operatoren;
    "dependence on cosmological time". Bestaetigt.
  - KRT 2008: bestaetigt. "19 of the 24 independent torsion components down to levels of order 10^-31 GeV"; Einstein-
    Cartan im Abstract nicht genannt. Ob "Hintergrund"-Torsion gemeint ist, sagt der Abstract nicht woertlich.
  - Giulini "Matter from Space": bestaetigt (Uebersicht).
  - **Erwartungsverstoss (klein):** Der CDT-"Geon" ist ein Wheeler-Geon (Graviton-Bindungszustand), kein topologischer
    Friedman/Sorkin-Geon. Die zwei Geon-Begriffe nicht vermischen.
- **Erwartung vor Abruf 2** (curl Volltext Giulini 0910.2574, PDF -> pdftotext; date beim Eintragen 10:45:37):
  - Liste: Eine Primmannigfaltigkeit ist NICHT spinoriell genau dann, wenn sie ein Linsenraum L(p,q) oder S^1 x S^2 ist
    (Hendriks / Friedman-Witt); fast alle anderen Primfaktoren sind spinoriell [L].
  - Friedman/Sorkin 1980: Zustaende mit halbzahligem Drehimpuls sind ERLAUBT, wenn die 2-pi-Drehung nicht in der
    Einskomponente der (asymptotisch festen) Diffeomorphismen liegt; erzwungen werden sie nicht.
  - Quantentheorie noetig (Wellenfunktion auf dem Konfigurationsraum Riem/Diff_F); klassisch gibt es keinen Spin 1/2.
  - Statistik: ohne Topologieaenderung Spin-Statistik-Verletzung moeglich (Aneziris u. a. 1989; Sorkin/Surya).
- **Ausgang Abruf 2** (curl 10:45:41, quellen/A2-giulini-0910.2574.pdf/.txt, 37 S.) [S]:
  - **Liste bestaetigt** (S. 28, Z. 1341-1350 der txt): "those 3-manifolds ... which do not allow for spinorial states are
    connected sums of lens spaces and handles (S1 x S2) ... there are no other non-spinorial manifolds than the 'obvious'
    ones." Generisch: "the generic case is that spinorial states are allowed" (S. 27). Fussnote 17: Homotopie gegen
    Isotopie gegen Diffeotopie; Frage "now known for all 3 manifolds".
  - **Bedingung bestaetigt** (S. 27, Abb. 9/10): Drehung um 360 Grad des Halses (Diffeomorphismus auf dem Zylinder
    R x S^2); spinoriell, wenn er nicht in der Einskomponente der Diffeomorphismen liegt, die die Sphaere im Unendlichen
    festhalten. Allgemein (S. 24-25): Bedingungen S1 (Q nicht einfach zusammenhaengend) und S2 (360-Grad-Schleife in Q
    nicht zusammenziehbar).
  - Beispiele [S]: RP^3 = L(2,1) nicht spinoriell (starre Drehung macht die Verdrillung rueckgaengig, S. 28-29).
    S^3/D8* (Wuerfel, Gegenflaechen mit 90-Grad-Schraube verklebt, Abb. 11) IST spinoriell und chiral (S. 29-30).
    Starrer Rotor Q = SO(3) = RP^3: zwei Sektoren, ganz- und halbzahlig (S. 26). Skyrme: 360-Grad-Schleife nur bei
    ungerader Windungszahl nicht zusammenziehbar (S. 26, Ref. [21]).
  - **Erwartungsverstoss V-A2a (mittel):** "in [GR] spinorial states usually exist only in non-abelian sectors, i.e.
    sectors that correspond to higher-dimensional unitary irreducible representations of the fundamental group [23]"
    (S. 26). Bei S^3/D8* ist der spinorielle Sektor die 2-dimensionale Darstellung (S. 30). Erwartet hatte ich das
    einfache Vorzeichen wie beim starren Rotor (abelsch). Folge: Ein spinorieller Geon ist ein MEHRKOMPONENTIGER
    Zustand; "Wellenfunktion wechselt das Vorzeichen" gilt in einer hoeherdimensionalen Darstellung.
  - **Erwartungsverstoss V-A2b (klein bis mittel):** Giulini (S. 24): Die Behauptung, der Schritt SO(3) -> SU(2) sei
    rein quantenmechanisch, "the mathematical facts underlying ... 'spin 1/2 from gravity' disprove this": Die
    asymptotische Symmetriegruppe wird "for purely topological reasons" zur Doppelueberlagerung. Erwartet: "klassisch
    kein Spin 1/2". Korrigiert: Die Doppelueberlagerung ist klassisch-topologisch (Konfigurationsraum), halbzahlige
    Drehimpuls-ZUSTAENDE brauchen die Quantisierung (Wellenfunktion auf Q).
  - Statistik [S] (S. 32-34): RP^3 # RP^3, Abbildungsklassengruppe Z2 * Z2; 1-dimensionale Darstellungen zeigen "both
    statistics sectors exist"; 2-dimensionale mischen die Sektoren (Winkel tau). "indication against a classical
    'spin-statistics correlation' ... Such a connection can therefore only exist in certain sectors and the question
    ... how these sectors are selected [8, 9]" (= Dowker/Sorkin 1998, 2000). Bestaetigt.
  - Aneziris u. a. 1989 steht NICHT in Giulinis Literaturliste (grep). Zuschreibung in KS2 bleibt [L].
- **Erwartung vor Abruf 3** (WebFetch INSPIRE-API, Friedman/Sorkin 1980 und Aneziris u. a. 1989; date 10:47):
  - FS 1980 (PRL 44, 1100): Abstract sagt, dass in Quantengravitation Zustaende mit halbzahligem Drehimpuls fuer
    bestimmte raeumliche Topologien moeglich sind; reine Gravitation, keine Spinorfelder.
  - Aneziris u. a. 1989 (Int. J. Mod. Phys. A 4): Geonen koennen ohne Topologieaenderung die Spin-Statistik verletzen.
- **Ausgang Abruf 3** (quellen/A3-inspire-fs1980-aneziris1989.txt) [S Abstract, Aneziris-Abstracts gekuerzt]:
  - FS 1980 bestaetigt: "For a certain class of three-manifolds, the angular momentum of an asymptotically flat quantum
    gravitational field can have half-integral values." -> "kann", nicht "muss"; Quantenfeld noetig.
  - Aneziris u. a. 1989 bestaetigt in der Sache: IJMPA 4, 5459: "quantum state of two identical geons may not be an
    eigenstate of the geon exchange operator"; MPLA 4, 331: "three-dimensional geons may be neither bosons nor
    fermions (nor paraparticles)". Wortlaut "Spin-Statistik-Verletzung" steht im gekuerzten Text nicht; Dowker/Sorkin
    (Abruf 1) sagen es fuer die Theorie ohne Topologieaenderung ausdruecklich.
  - Kein Verstoss.
- **Erwartung vor Abruf 4** (WebSearch "spinorial topological geon triangulation Regge spin network causal set half-integer
  spin"; date 10:47:24): keine Arbeit, die einen spinoriellen Geon auf einem Simplex-Netz konkret baut oder numerisch
  zeigt. Am naechsten liegen erwartet: Duston "topspin networks" (LQG mit Topologie ueber verzweigte Ueberlagerungen),
  Bilson-Thompson/Markopoulou/Smolin (Zoepfe in Bandnetzen, Spin nicht hergeleitet). KS3 eher verfehlt.
- **Ausgang Abruf 4** (WebSearch): nur allgemeine Treffer (Regge-Einfuehrung 1904.01966, Spin-Netze gr-qc/0512144,
  SO(4)-Darstellungen gr-qc/0402050, 0901.1074, CDT-Wikipedia, 1204.5394 ohne Titel). Keiner zu spinoriellen Geonen auf
  Netzen. Erwartung nicht verletzt, aber die Suche war zu breit (WebSearch liefert nichts Gezieltes) -> arXiv-API.
- **Erwartung vor Abruf 5** (WebFetch arXiv-API: abs:geon AND (triangulation OR lattice OR Regge OR simplicial OR
  "spin network" OR "causal set"), alle Jahre, nach Datum): 5 bis 15 Treffer; Maas u. a. 2025/26 dabei; Wheeler-Geonen
  auf Gittern; kein spinorieller (Friedman/Sorkin-)Geon auf einem Netz. date beim Eintragen 10:47:48.
- **Ausgang Abruf 5** (arXiv-API, totalResults 4) [S Abstract, ueber WebFetch]: 2510.21248 und 2504.11047 (Maas u. a.),
  quant-ph/9706018 (Hadley 1997: Teilchen als 4-Geon mit geschlossenen zeitartigen Kurven), gr-qc/9512025 (Cooperstock
  u. a. 1995: kugelfoermiger Gravitations-Geon unmoeglich). Kein spinorieller Geon auf einem Netz. Erwartung bestaetigt.
- **Erwartung vor Abruf 6** (WebFetch arXiv-API: (abs:spinorial AND (triangulation OR lattice OR simplicial OR "spin
  network" OR "causal set" OR discrete)) OR ti:topspin; date beim Eintragen 10:48:10): Treffer zu Duston
  "topspin networks" (LQG, Topologie in Spin-Netzen); spinoriell + Gitter eher Skyrme-Gitter; kein Regge-Geon.
- **Ausgang Abruf 6** (arXiv-API, totalResults 53; "spinorial" wird breit benutzt) [S Abstract, ueber WebFetch]:
  - Einschlaegig nur LQG-Topologie: Duston 2011 (1111.1252) "topspin networks, a proposal which allows topological
    information" in Spin-Netzen; Duston 2013 (1308.2934) Fundamentalgruppe einer Raumschicht aus einem Topspin-Netz;
    Villani 2021 (2106.14188) "topology can actually change due to the action of the Hamiltonian" (Topspin-Formalismus).
  - Kein Abstract leitet halbzahligen Spin aus der Topologie eines Netzes her. Erwartung bestaetigt (Duston ja, kein
    Regge-Geon). Neu fuer mich: Topologieaenderung im Topspin-Formalismus (Villani 2021) -> Ansatz fuer die "weitere
    Zugart", die die Karte fuer Topologieaenderung verlangt [S Abstract].
  - Randnotiz: 2607.25684 (Kura 2026) Landau-Niveaus auf der Wuerfeloberflaeche, ungerade Monopolladung braucht
    spinorielle Darstellungen von 2O. Nicht Geon; nur Beispiel "Monopol -> spinoriell" (vgl. GEN-04 H2) [S Abstract].
- **Erwartung vor Abruf 7** (WebSearch "sandpile self-organized criticality curvature deficit angle triangulation
  disclination"; date 10:49:00): keine Sandhaufenregel mit Fehlwinkel als Korn. Naechste Treffer: Schaum-T1-Lawinen
  (topologische Ladung 6 - n), Knitterlaerm (crackling noise beim Zerknuellen), evtl. kombinatorischer Ricci-Fluss.
- **Ausgang Abruf 7** (WebSearch): Grundlagen zu Sandhaufen (2009.08160), "Self-organized criticality and the lattice
  topology" (adap-org/9601002: Gittertopologie aendert die Exponenten in 2D nicht), 2608.13500 "Symmetry Emergence in
  Self-Organized Criticality", Akkretionsscheiben (astro-ph/0009424). Keine Regel mit Kruemmung als Korn. Erwartung
  bestaetigt; WebSearch zu breit -> arXiv-API.
- **Erwartung vor Abruf 8** (WebFetch arXiv-API: (abs:sandpile OR abs:"self-organized criticality") AND (abs:curvature
  OR abs:triangulation OR abs:disclination OR abs:"topological charge" OR abs:Ricci OR abs:"deficit angle"), alle
  Jahre; date 10:49:20): 10 bis 40 Treffer, ueberwiegend Netzwerk-Kruemmung (Ollivier/Forman) und Sandhaufen auf
  gekruemmten Graphen; kein Fehlwinkel als umverteilte Groesse bei dynamischen Triangulierungen oder Membranen.
- **Ausgang Abruf 8** (arXiv-API, totalResults 10) [S Abstract, ueber WebFetch]:
  - Dantas 2021 (2105.11958): Sandhaufen-Dynamik auf eingefrorenen dreiwertigen Spin-Netzen, SOC in den Lawinen,
    "slowly expanding, 2-dimensional dual (triangulated) space" (Linie Ansari/Smolin, im Projekt [P SOC-RAUM-L]).
    Umverteilt werden Spin-Labels (also Laengen im Dualraum), nicht Fehlwinkel.
  - Vacaru 2010 (1010.2021): "nonholonomic Ricci flow diffusion can be with self-organized critical behavior"
    (Kontinuum, Finsler; keine Fehlwinkel, kein Netz).
  - Vallarino 2026 (2604.13890): Forman-Ricci-Kruemmung eines Wirtschaftsgraphen als Zustandsgroesse; unter einer
    Schwelle Potenzgesetz der Kaskaden. Graph-Kruemmung mit Schwelle, aber keine Raumgeometrie.
  - Kalinin 2026 (2607.25878): Sandhaufen-Relaxation und Monge-Ampere, "normalized curvature measures converge"
    (Mathematik, tropisch).
  - Rest nicht einschlaegig. **Keine Regel mit Fehlwinkel als umverteiltem Korn bei dynamischen Triangulierungen
    oder Membranen.** Erwartung bestaetigt. Kleiner Verstoss: Es gibt "Kruemmung mit Schwelle -> Kaskaden" auf Graphen
    (Vallarino) und "Ricci-Fluss mit SOC" (Vacaru); die Kombination Kruemmung + SOC ist also nicht leer.
- **Erwartung vor Abruf 9** (curl Volltext KRT 2008, arXiv 0712.4393; date 10:50:14): KRT schreiben, dass in der
  Einstein-Cartan-Theorie die Torsion nicht propagiert und ausserhalb von Materie verschwindet; ihre Schranken gelten
  fuer eine Hintergrund-Torsion (konstant im Labor), wie sie Theorien mit propagierender Torsion liefern koennten.
  Benutzt: Torsionspendel mit polarisierten Elektronen (Heckel u. a.), Komagnetometer.
- **Ausgang Abruf 9** (curl 10:50:26, quellen/A9-krt-0712.4393.pdf/.txt, 4 S.) [S]:
  - S. 1: "In many models, the torsion has spin density as its source. Some scenarios allow torsion waves to propagate";
    "sources of spin density strong enough to produce torsion effects are difficult to identify or create. Typical
    limits on torsion in the literature involve dynamical properties, being obtained from searches for spin-spin
    interactions or for torsion-mass effects [4]."
  - S. 1: Voraussetzung: "a theory predicting a nonzero torsion field in the vicinity of the Earth"; Naeherung "torsion
    background as constant"; S. 2: "Our analysis and results apply to most torsion theories predicting nonzero
    laboratory effects. Teleparallel models are exceptions"; Quelle der Torsion Sonne (S), Erde (E) oder ausserhalb
    ("galactic or cosmological scales").
  - Experimente: Dual-Maser (Neutron) [14] und "spin-polarized torsion pendulum [15]" = Heckel u. a., PRL 97, 021603
    (2006) (nicht 2008). Schranken z. B. |A_X| < 2,1e-31 GeV ~~(Tabelle I, Gl. 7)~~ -> berichtigt 11:07: Gl. (6), bei streng minimaler Kopplung (Gegenlesen am txt).
  - **Einstein-Cartan wird NICHT genannt** (grep "cartan": nur "Riemann-Cartan"). KS4 Teil 2 ist also ein Schluss aus
    KRTs Voraussetzung (Hintergrund-Torsion im Labor), nicht ihre Aussage. Erwartung im Kern bestaetigt, aber "EC
    algebraisch" steht dort nicht; Quelle dafuer fehlt noch.
  - Lokal gelesen (kein Abruf), Katanaev 2005 (cond-mat/0407469, RUNDE-22 hilfs) Abschn. 5, Gl. (18), (22), (26) [S]:
    allgemeine 8-Parameter-Lagrangedichte quadratisch in Torsion und Kruemmung; die Forderungen "nur Versetzungen",
    "nur Disklinationen", "keine Defekte" lassen L = -kappa R~(e) + 2 gamma R^A_ij R^A ij uebrig: Hilbert-Einstein fuer
    das Dreibein plus Quadrat des antisymmetrischen Ricci-Teils. Die T^2-Terme mit (22) sind genau Hilbert-Einstein
    (teleparallel). Eigene Dynamik bekommt die Verbindung erst ueber den Kruemmungs-Quadrat-Term gamma.
- **Erwartung vor Abruf 10** (WebSearch 24-Monats-Fenster: "Einstein-Cartan four-fermion contact interaction torsion
  constraints 2025"; date 10:51:09): Arbeiten 2024-2026 zur Einstein-Cartan-Vierfermion-Wechselwirkung (z. B.
  Shaposhnikov u. a.), mit dem Befund: minimal gekoppelt ~ G, unmessbar klein; mit grossen nicht-minimalen Kopplungen
  (Holst/Immirzi) groesser, dann Collider-/Astro-Schranken. Keine Arbeit, die reine EC im Labor ausschliesst.
- **Ausgang Abruf 10** (WebSearch; nur Trefferliste und Kurztext des Suchwerkzeugs, nichts an der Quelle gelesen):
  2509.08848 (2025; laut Suchtext: EC mit Fermionen erzeugt nicht-renormierbare Vierfermion-Terme, "catastrophic
  quartic divergences"), 2604.21535 (2026, Fermion-Dichte und Inflation), 1607.01128, 1211.4359 und 1404.5195
  (Torsion + Extradimensionen + LHC), 1102.5667, 1405.0397, 0811.1932. Keine Labor-Arbeit gegen reine EC sichtbar.
  Erwartung im Kern bestaetigt (keine Labor-Widerlegung reiner EC), Einzelheiten [L/Suchtext], nicht [S].
- **Erwartung vor Abruf 11** (WebFetch arXiv-API id_list 2509.08848, 2604.21535, 2106.14188, 1111.1252, 1105.3456;
  date 10:51:46):
  - 2509.08848 / 2604.21535: EC mit Fermionen -> Vierfermion-Kontaktterm; mindestens einer sagt woertlich, dass die
    Torsion algebraisch (nicht dynamisch) ist.
  - 2106.14188 (Villani): Topologieaenderung durch den Hamiltonoperator im Topspin-Formalismus; kein Spin 1/2.
  - 1111.1252 (Duston): Topologie in Spin-Netzen ueber verzweigte Ueberlagerungen; kein Spin 1/2 aus Topologie.
  - 1105.3456 (Gravity Probe B, Gegensweep "Kruemmung -> Richtung"): geodaetische Praezession ~ -6602 +- 18 mas/Jahr
    gegen GR -6606; Frame-Dragging ~ -37 +- 7 gegen -39.
- **Ausgang Abruf 11** (WebFetch; das Werkzeug gab trotz Auftrag nur den ERSTEN Satz jedes Abstracts) [S Abstract,
  nur erster Satz]:
  - 1105.3456: Everitt u. a., PRL 106, 221101 (2011), "testing ... the geodetic and frame-dragging effects, by means of
    cryogenic gyroscopes in Earth orbit". Zahlen NICHT gelesen -> bleiben [L].
  - 2106.14188: Villani, "Including topology change in Loop Quantum Gravity with topspin network formalism ...", CQG
    (accepted): "in order to include in the theory the possibility of changes in the topology of spacetime".
  - 1111.1252: Duston, CQG 29 (2012) 205015, "topspin networks ... allows topological information to be encoded in
    spin networks".
  - 2604.21535: Alexander, Chen, Liu, Marciano, Sasaki, Su 2026, Inflation aus Fermionen (nur erster Satz).
  - 2509.08848: Chishtie 2025, "Theoretical and experimental assessment of Einstein-Cartan theory: A comparative
    analysis within the USMEG-EFT framework", Can. J. Phys. 104 (2026) 1-14 (nur erster Satz).
  - Erwartung zu "EC algebraisch woertlich" NICHT pruefbar (Abstracts abgeschnitten). Kein inhaltlicher Verstoss;
    Werkzeugverlust. Lehre: id_list ueber WebFetch nur mit Satz-Suchauftrag, nicht "complete abstract".
- **Erwartung vor Abruf 12** (WebFetch arXiv-API, 24-Monats-Fenster 2024-10-05 bis 2026-10-05: abs:geon OR abs:geons
  OR (abs:"spin-statistics" AND abs:topology); date beim Eintragen 10:52:33): 3 bis 10 Treffer; Maas u. a.
  (2x), Wheeler-/Boson-Sterne-Geonen; KEINE neue Arbeit zu Spin-Statistik topologischer Geonen. Stand 2024-2026 = Stand
  Dowker/Sorkin.
- **Ausgang Abruf 12** (arXiv-API, 24 Monate, totalResults 8) [S Abstract, ein Satz je Eintrag, ueber WebFetch]:
  - Tsirulev 2026 (2608.03942) "Charged topological geons with a self-gravitating scalar field" (Ladung aus Topologie,
    klassisch); Spadafora 2024 (2412.02755) BTZ-Geon, Inneres mit anderer Topologie; Bhattacharya 2024 (2410.13993)
    verborgene Topologie mit Quantendetektoren; Maas u. a. (2x); Rest fachfremd (Majorana-Ketten, Dirac-Kondensate
    um Kerr mit halbzahliger azimutaler Quantenzahl).
  - **Keine neue Arbeit zu Spin oder Statistik topologischer Geonen im Fenster.** Erwartung bestaetigt. Stand
    2024-2026 nach Recherchestand = Dowker/Sorkin 1998/2000.
- **Erwartung vor Abruf 13** (WebFetch arXiv-API, 24 Monate: ("half-integer" OR "spin 1/2" OR "spin-1/2" OR fermion OR
  fermions OR spinor) AND (Regge OR "dynamical triangulations" OR "causal set" OR "spin foam" OR "group field theory")
  AND (topology OR torsion OR curvature); date 10:52:50): 5 bis 20 Treffer, Fermionen auf CDT/Kausalmengen/Spin-
  schaum als EINGESETZTE Materie; keine Arbeit, die Spin 1/2 aus Kruemmung oder Topologie eines Netzes herleitet.
- **Ausgang Abruf 13** (arXiv-API, 24 Monate, totalResults 2) [S Abstract, ein Satz, ueber WebFetch]:
  - Migdal 2026 (2602.21129) "Geometric QCD II": Fermionen auf einer QCD-Weltflaeche (keine Raumzeit-Geometrie).
  - Dutta 2024 (2412.20478) "Properties of black hole exterior fermions in spinfoam": "For a locally pinched negative
    curvature, fermions accumulate in the black hole exterior region". Fermionen sind dort eingesetzte Materie; die
    Kruemmung verteilt sie nur [ES nach dem Zitat; das Werkzeug schrieb "DERIVED", das ist nach dem Zitat falsch].
  - Erwartung zur Trefferzahl verfehlt (2 statt 5-20; dreifaches UND zu eng), inhaltlich bestaetigt: keine Arbeit
    leitet Spin 1/2 aus Kruemmung oder Topologie eines Netzes her (24 Monate, nach Recherchestand).
- Lokal (kein Abruf): Bowick/Giomi 2009 und Carlip 1995 fuer Beulen bzw. Punktteilchen als Kegel; siehe Abschnitt 2.

## 2. Lokal gelesen (kein Abruf), fuer Frage 4

- Bowick/Giomi 2009 (0812.3064, RUNDE-22 hilfs) [S]:
  - S. 20 (txt Z. 1052-1062): Auf starrer Unterlage ordnen sich Defekte so, dass sie die Gausskruemmung abschirmen;
    "if the geometry of the substrate is allowed to change (for instance by lowering the bending rigidity) the system
    eventually enters a regime where the substrate itself changes shape ... The latter is the fundamental mechanism
    behind the buckling of crystalline membranes [69]" ([69] = Seung/Nelson, PRA 38, 1005 (1988)).
  - S. 21, Gl. (54), (55): F_el = (Y/2) Int Int G_2L [eta - K][eta - K]; "Coulomb energy of a multi-component plasma of
    charge density eta in a background of charge density -K"; Defekte "attracted to regions of like-sign Gaussian
    curvature".
  - S. 22: Holonomie "a vector parallel transported around a closed loop ... rotates by an angle delta = Int K";
    auf dem Dreiecksnetz k(v) = (pi/3)(6 - c(v)). Die Quelle eta - K ist die Differenz aus vorhandener Kruemmung und
    der durch die Disklination erzeugten.
  - Die Beulradius-Zahlen (Seung/Nelson) stehen im txt nicht (grep "127", "154" nur Gleichungsnummern) -> [L].
- Carlip gr-qc/9503024 (lokal): Punktteilchen-Fehlwinkel 8 pi G m dort nicht gefunden (grep deficit/conical) -> [L].
- Katanaev 2005 (lokal): siehe Ausgang Abruf 9.
- **Erwartung vor Abruf 14** (WebFetch arXiv-API id_list gr-qc/0606062, hep-th/0103093, mit Satz-Suchauftrag; date
  10:54:18): Trautman 2006 "Einstein-Cartan theory" und Shapiro 2002 "Physical aspects of the space-time torsion"
  sagen im Abstract, dass die Torsion in EC algebraisch an die Spindichte gebunden ist bzw. sich nicht ausbreitet
  (Kontaktwechselwirkung). Falls die IDs nicht stimmen: Fehlanzeige.
- **Ausgang Abruf 14** (arXiv-API, Satz-Suchauftrag) [S Abstract, ueber WebFetch]:
  - Shapiro 2002 (hep-th/0103093, Phys. Rept. 357, 113): "we review the upper bounds for the background torsion";
    "the propagating torsion may be consistent with the principles of quantum theory only in the case when the torsion
    mass is much greater than the mass of the heaviest fermion coupled to torsion."
  - Trautman 2006 (gr-qc/0606062, Encycl. Math. Phys. 2, 189-195): ECT erlaubt Torsion "relating torsion to the density
    of intrinsic angular momentum"; Vorschlag 1922 von Cartan. "algebraisch" steht im Abstract nicht.
  - **Erwartungsverstoss (mittel), V-A14:** Ich erwartete nur "EC algebraisch". Gefunden dazu eine harte Bedingung fuer
    AUSBREITENDE Torsion: quantenkonsistent nur, wenn die Torsionsmasse viel groesser ist als die Masse des schwersten
    angekoppelten Fermions (Shapiro). Ausbreitende Torsion ist also nicht frei waehlbar; fuer Finns Netz hiesse das: eine
    Rahmen-/Guertel-Energie, die Torsion ausbreiten laesst, muesste eine sehr schwere Mode geben [ES].
- **Erwartung vor Abruf 15** (curl Volltext Trautman gr-qc/0606062; date 10:54:41): Im Text steht, dass die
  Torsionsgleichung algebraisch ist (Torsion = Spindichte mal Konstante), die Torsion ausserhalb der Materie
  verschwindet und sich nicht ausbreitet; Abweichungen von GR erst bei Dichten ~ 1e54 g/cm^3 (fuer Elektronen) bzw.
  ~ 1e47 (Neutronen) [L].
- **Ausgang Abruf 15** (curl 10:54:53, quellen/A15-trautman-gr-qc-0606062.pdf/.txt, 7 S.) [S]:
  - Gl. (24) Cartan-Gleichung Q + Spuren = 8 pi s, algebraisch in der Torsion Q; Gl. (25) aufgeloest
    Q = 8 pi (s + ...). Direkt danach: "Therefore, torsion vanishes in the absence of spin ... there is no difference
    between the Einstein and Einstein-Cartan theories in empty space. Since practically all tests of relativistic gravity
    are based on ... Einstein's equations in empty space, ... the latter is as viable as the former."
  - Gl. (30)-(31): Torsion eliminierbar, T_eff = T + s^2; "a spin-spin contact interaction, reminiscent of the one
    appearing in the Fermi theory"; "whenever terms quadratic in spin can be neglected - in particular in the linear
    approximation - ECT is equivalent to GRT". "Cartan-Radius" eines Nukleons ~ 1e-26 cm.
  - Abschnitt "Spinning fluid and the generalized Mathisson-Papapetrou equation of motion": dP_mu/ds =
    (Q^rho_mu nu P_rho - (1/2) R_rho sigma mu nu S^rho sigma) u^nu. Kruemmung uebt eine Kraft auf Spin aus; sie
    erzeugt keinen.
  - Summary: "the effects of spin and torsion can be significant only at densities of matter that are very high, but
    nevertheless much smaller than the Planck density".
  - Erwartung bestaetigt (algebraisch, verschwindet ohne Spin, im Vakuum gleich GR). Die Dichtezahlen 1e54/1e47 g/cm^3
    stehen dort nicht; statt dessen Cartan-Radius 1e-26 cm. Kein Verstoss.
- **Erwartung vor Abruf 16** (WebFetch arXiv-API, Satz-Suchauftrag: abs:"cosmic string" AND abs:"deficit angle" AND
  abs:tension; date 10:55:17): Mehrere Abstracts sagen, dass eine gerade Kosmische Saite mit Spannung mu einen
  Kegel mit Fehlwinkel 8 pi G mu erzeugt (Vilenkin 1981). Damit ist "Spannung = Kruemmung" fuer Linien woertlich GR.
- **Ausgang Abruf 16** (arXiv-API, totalResults 7) [S Abstract, ein Satz, ueber WebFetch]:
  - Griffiths 2002 (gr-qc/0204085): "The deficit angle (the tension) of the string decreases through the gravitational
    wave" -> Fehlwinkel und Spannung werden gleichgesetzt.
  - Niedermann 2015 (1412.2750): "If the tension exceeds a critical value, the deficit angle becomes larger than 2pi".
  - Die Formel 8 pi G mu steht in keinem der 7 Abstracts -> bleibt [L] (Vilenkin 1981). Erwartung in der Sache
    bestaetigt (Fehlwinkel = Spannung), in der Formel nicht pruefbar. Kleiner Verstoss: kein Abstract nennt die Zahl.
- **Erwartung vor Abruf 17** (WebFetch arXiv-API, Satz-Suchauftrag: abs:"spin structure" AND (triangulation OR
  triangulated OR simplicial) AND combinatorial; date 10:55:42): Budney (2013/2018) "Combinatorial spin structures on
  triangulated manifolds": Spinstruktur als Z_2-Beschriftung auf dem dualen Geruest mit einer Bedingung je
  Kodimension-2-Simplex; damit ist "Z_2-Vorzeichen je Verbindung" (RT-Dossier [L]) an der Quelle pruefbar.
- **Ausgang Abruf 17** (arXiv-API, totalResults 6) [S Abstract, ueber WebFetch]:
  - Benedetti/Petronio 2013 (1304.3884) "Spin structures on 3-manifolds via arbitrary triangulations": "Any spin
    structure s on M can be encoded by extra combinatorial structures on T."
  - Novak/Runkel 2014 (1402.2839, 2D): "A spin structure is encoded by assigning to each triangle a preferred edge, and
    to each edge an orientation and a sign, subject to certain admissibility conditions."
  - Tata 2020 (2008.10170): Spin- und Pin-Strukturen kombinatorisch ueber ein Rahmenfeld nahe dem dualen 1-Geruest.
  - Novak/Runkel 2015 (1506.07547) "Spin from defects in two-dimensional quantum field theory".
  - Erwartung in der Sache bestaetigt (Vorzeichen je Kante mit Zulaessigkeitsbedingungen, in 2D woertlich; in 3D
    "extra combinatorial structures"). Kleiner Verstoss: Budney taucht nicht auf; die 3D-Kodierung kenne ich nur aus
    dem Abstract-Satz, nicht im Einzelnen.
- **Erwartung vor Abruf 18** (WebFetch arXiv-API, Satz-Suchauftrag: abs:foam AND (abs:"topological charge" OR
  abs:curvature) AND (abs:avalanche OR abs:avalanches OR abs:T1 OR abs:rearrangement OR abs:rearrangements); date
  10:56:08): Schaum-Arbeiten nennen 6 - n als topologische Ladung und T1 als ihre Umverteilung; Lawinen ja, aber
  ausgeloest durch Scherspannung; niemand nennt es "Kruemmungs-Sandhaufen". KS5 bleibt nach Wortlaut verfehlt.
- **Ausgang Abruf 18** (arXiv-API, totalResults 1) [S Abstract, ein Satz]: nur Modes/Kamien 2008 (0810.5724)
  "Spherical Foams in Flat Space" (T2-Umordnung am symmetrischen Tetraeder-Blaeschen; keine Lawinen).
  - **Erwartungsverstoss (klein), V-A18:** Ich erwartete Schaum-Arbeiten, die 6 - n als topologische Ladung mit
    T1-Lawinen verbinden. Die Abfrage fand keine. Die Gleichsetzung "T1 = Kantenflip der dualen Triangulierung,
    6 - n = Kruemmungsladung" bleibt mein Schluss [M/ES] (mit Bowick/Giomi S. 22: k(v) = (pi/3)(6 - c(v)) [S]);
    Lawinen im 2D-Schaum nur ueber Tewari u. a. 1999 [P SOC-RAUM-L].
- **Erwartung vor Abruf 19** (curl Volltext Gravity Probe B, arXiv 1105.3456; date 10:56:36; Gegensweep G1
  "Kruemmung -> Richtung ist gemessen"): geodaetische Drift -6601,8 +- 18,3 mas/Jahr gegen GR -6606,1;
  Frame-Dragging -37,2 +- 7,2 gegen -39,2 [L].
- **Ausgang Abruf 19** (curl 10:56:46, quellen/A19-gpb-1105.3456.pdf/.txt, 5 S.) [S]: Abstract (PDF): "geodetic drift
  rate of -6,601.8 +- 18.3 mas/yr and a frame-dragging drift rate of -37.2 +- 7.2 mas/yr, to be compared with the GR
  predictions of -6,606.1 mas/yr and -39.2 mas/yr". Einleitung: "a geodetic drift in the orbit plane due to motion
  through the space-time curved by the Earth's mass"; "matches the curvature precession ... given by W. de Sitter in
  1916". Erwartung exakt bestaetigt. -> "Kruemmung dreht Richtung" ist auf ~0,3 % gemessen.
- Abruf 20 nicht benutzt (Reserve).

## 3. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe? (ab 10:59:46)

- G1 "Kruemmung -> Richtung ist gemessene Physik": GEPRUEFT (Abruf 19, GP-B). Bestanden.
- G2 "Spannung einer Linie = Fehlwinkel" (Kosmische Saite): GEPRUEFT (Abruf 16). In der Sache bestanden
  ("deficit angle (the tension)"), die Zahl 8 pi G mu nicht an der Quelle.
- G3 "Der CDT-Geon ist ein Geon im Sinne von Friedman/Sorkin": GEPRUEFT (Abruf 1). DURCHGEFALLEN: Wheeler-Geon
  (selbstgebundene Gravitonen), Topologie in CDT fest (RUNDE-22 [P] "feste Schichttopologie").
- G4 "KRT nennen Einstein-Cartan": GEPRUEFT (Abruf 9). DURCHGEFALLEN: nicht genannt; Schluss auf EC ist meiner.
- G5 "Pachner-Zuege erhalten die Topologie" (Karte [M]): NICHT an der Quelle geprueft [L Pachner 1991].
- G6 "Jede orientierbare 3-Mannigfaltigkeit traegt eine Spinstruktur" (Karte [M]): nicht an der Quelle; kombinatorische
  Kodierung auf Triangulierungen gibt es (Abruf 17), das stuetzt die Umsetzbarkeit, nicht den Satz.
- G7 "Die 4 freien Rahmendrehungen koennten eine Z_2-Schleife tragen": am Schreibtisch GEPRUEFT [M]: Es sind lineare
  Nullmoden, ihr Raum ist R^4 je Zelle, zusammenziehbar -> keine Z_2. Eine Z_2 gibt es nur ueber die kompakte Gruppe
  SO(3); fuer N Rahmen ist pi_1(SO(3)^N) = (Z_2)^N, also sind Z_2-Schleifen fuer Rahmen-Netze billig und vorab
  ableitbar. Offen ist nur, welche Energie sie schuetzt und was den Sektor waehlt.
- G8 "Ein Henkel im Netz koennte Spin 1/2 tragen": an der Quelle GEPRUEFT (Giulini S. 28): S^1 x S^2 und Linsenraeume
  (auch RP^3) sind NICHT spinoriell.
- G9 "Kruemmungs-Sandhaufen auf geschlossener Flaeche": NICHT geprueft. [ES]: Gauss-Bonnet erhaelt die Summe der
  Kruemmungsladungen -> ohne Senke ein Sandhaufen mit fester Energie (absorbierender Uebergang statt SOC; Dickman u. a.
  [P SOC-RAUM-L]).
- G10 "Ein Spinor sieht einen 4-pi-Kegel (Fehlwinkel -2 pi) als Vorzeichen -1": [M] aus der SU(2)-Hebung
  exp(-i alpha sigma/2) bei alpha = -2 pi; nicht an einer Quelle geprueft.

## 4. Berichtigungen (Regel 5: nichts still geloescht; eingetragen 11:00:22)

Ich habe in diesem Feld und in zwei Quellendateien Zeitangaben geschaetzt statt gemessen und sie danach per sed durch
date-Werte ersetzt. Die urspruenglichen Wortlaute, hier als gestrichen erhalten:
- Erwartung 1: ~~"date davor 10:45:0x, siehe unten"~~ -> "date beim Eintragen 10:44:37".
- Erwartung 2: ~~"date beim Eintragen siehe Ausgang"~~ -> "10:45:37".
- Erwartung 5: ~~"date 10:47:5x siehe naechste Zeile"~~ -> "10:47:48".
- Erwartung 6: ~~"date beim Eintragen siehe oben, 10:4x"~~ -> "10:48:10".
- Erwartung 12: ~~"date beim Eintragen siehe Zeile davor"~~ -> "10:52:33".
- P6: ~~"(10:4x, ..."~~ -> date-Grenzen 10:37:27 bis 10:44:10.
- quellen/A1: ~~"vor 10:46"~~ -> "vor 10:45:25"; quellen/A3: ~~"vor 10:47:3x"~~ -> "vor 10:47:16".

## 5. Zwischenstand vor dem Dossier (11:00:22)

- Abrufe: 19 von 20 (Abruf 20 Reserve, nicht benutzt).
- KS1 eingetroffen (FS-Abstract + Giulini S. 27); KS2 im Kern eingetroffen, Klammer "Hosenbein" nicht belegt
  (Paarerzeugung aus R^3) -> streng: teilweise; KS3 nicht eingetroffen (nach Recherchestand); KS4 eingetroffen
  (Trautman Gl. 24/25 + KRT-Voraussetzung, der Schluss auf EC ist meiner); KS5 nicht eingetroffen (nach Recherchestand).
- Offene Rueckfragen, die mitwandern:
  - R1: Welche Energie hatte GUERTEL-FINN-NETZ-1 genau (SO(3)- oder SU(2)-empfindlich)? Fuer den Kartenvorschlag Z2-NETZ-1
    noetig; nicht gelesen (PLAN.md dort).
  - R2: Dowker/Sorkin-Volltext: Ist der Paarerzeugungs-4-Mannigfaltigkeit ein "Hosenbein"? Nicht gelesen.
  - R3: Seung/Nelson-Beulradius-Zahlen (127, 154) weiter [L].

## 6. Gegenlesen des Dossiers am Text (ab 11:07:15)

- KRT: |A_X| < 2,1e-31 GeV steht in Gl. (6) und gilt "If torsion is strictly minimally coupled" (txt Z. 250-262);
  Abruf-9-Zeile oben berichtigt. Dazu KRT S. 3: "a torsion magnitude of 10^-27 GeV is roughly comparable to that of the
  metric laplacian on the surface of the Earth".
- Bowick/Giomi: Seitenkoepfe im txt (Z. 1038 = S. 20, Z. 1094 = S. 21, Z. 1154 = S. 22): Beulen S. 20, Gl. (54)/(55)
  S. 21, Holonomie und k(v) S. 22. Stimmt mit dem Dossier.
- Quellenliste: Zeitschriftangaben von Bowick/Giomi (Band, Seite) und Katanaev waren aus dem Gedaechtnis -> als [L]
  markiert. "Kamien" (Modes) und "u. a." (Niedermann) waren nicht gelesen -> entfernt bzw. "weitere Autoren nicht
  gelesen".
- GUERTEL-Energie: PLAN Z. 18 ("haengt nur von q_a . q_b ab"), Z. 24 (Formel im ebenen Fall), Z. 36 ("2(1 - cos
  omega)") -> Dossier-Zitat auf Z. 18, 24, 36 praezisiert.

## 7. Abschluss

- DOSSIER.md geschrieben ab 11:02:15, gegengelesen ab 11:07:15 (Abschnitt 6), Ende 11:10:01 CEST (date).
- Abrufe 19 von 20. Keine Rechnung, kein python/awk/perl, Schreiben nur in diesem Kartenordner.
