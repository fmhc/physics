# GEMEINSAMES-NETZ-L: Arbeitsfeld (feldforscher, Runde 42)

- Start 2026-10-04 18:54:24 CEST (date). Zeitbox 75 min, also Abgabe spaetestens 20:09:24 CEST.
- Arbeitsdatei nach Feld-Regel 5: alles hier, vor jedem Schritt neu gelesen. Gestrichenes bleibt mit ~~ stehen.
- Abrufe: hoechstens 10 (jeder arXiv-API-Aufruf = 1). Keine Websuche. Kopien in quellen/.
- Kennzeichen: [S] (mit Zeile), [S Abstract], [P], [L], [L?], [M], [ES], [H].

## 0. Gelesen vor dem ersten Abruf (Projektstand, [P])

- KARTE.md (ganz), RUNDE-42/GEMEINSAMES-NETZ-v1.md (L1 bis L9), RUNDE-42/KOMPONENTEN-KURZ.md, RUNDE-40/WEICHE-STAND-v5.md,
  RUNDE-37/gluonen-l/DOSSIER.md (ganz), RUNDE-37/takt-rand-4d-1/ERGEBNIS.md (ganz), RUNDE-37/tetraeder-l/DOSSIER.md
  (Z. 1-140), RUNDE-35/graviton-netz-l/DOSSIER.md (ganz), RUNDE-37/chiral-l/DOSSIER.md (Z. 1-60).
- Projekt-grep (mit Ausschluss der versiegelten Pfade):
  - "graphity|konopka|markopoulou": nur Einordnungen vom 09.09. (graphen-brief-20260909.md Z. 5: "Quantum Graphity
    (Konopka/Markopoulou/Smolin 2006)"; faden-einordnung-20260909.md Z. 42: Bilson-Thompson/Markopoulou/Smolin 2007,
    "geschuetzte Teilsysteme ... Diese Stabilitaet erschwert zugleich Wechselwirkungen"). Keine Karte, keine Quelle
    gelesen [P].
  - "weinberg-witten": nur Dateien vom 06.-13.09. und GRAVITON-NETZ-L (Carlip 2012 sekundaer [S dort]).
  - "nielsen-ninomiya": CHIRAL-L mit lokalen Volltexten (Kaplan 0912.2560, Thorngren/Preskill/Fidkowski 2601.04304,
    Wang/You 2204.14271) -> E6 ohne neuen Abruf pruefbar.
  - "collins|chadha|bednik": LICHT-GLEICH-L hat die Tempo-Literatur (L2) [P].
  - "marolf|rubakov|dvali|shaposhnikov|brane|bilson|helon|volovik": Branen nur als Dark Dimension und Randall/Sundrum
    (Negativseite, DUNKEL-FLIP-L); Domain-Wall-Lokalisierung von Eichfeldern und Schwerkraft auf **derselben** Wand
    (Rubakov/Shaposhnikov, Dvali/Shifman) nirgends. Marolf, Volovik, Bilson-Thompson-Bandgraphen: keine Karte.

## 1. Abrufplan (vorab, kann sich aendern)

| Abruf | Inhalt | wofuer |
|---|---|---|
| A1 | arXiv-API-Suche: Quantum Graphity, braided ribbon (Bilson-Thompson), alle Jahre, nach Datum | E1, Frage 1, Finns "Baender mit markierter Seite" |
| A2 | arXiv-API-Suche: (C)DT mit Materie (Titel) | E4, L1 |
| A3 | arXiv-API id_list: Domain-Wall-Welt (Rubakov-Review, Dvali/Shifman, Randall/Sundrum II, Dubovsky/Rubakov), D-Theorie voll (Brower u. a. 2004), Grabowska/Kaplan | Frage 3 |
| A4 | arXiv-API: Weinberg-Witten, Marolf "kinematic nonlocality", Witten "Symmetry and emergence" | E5, Frage 2 (L3) |
| A5 | arXiv-API, 24 Monate: emergente Gravitonen auf Gittern mit Materie | E2, Regel 7, GRAVITON-NETZ-L Q4 |
| A6-A10 | Volltexte nach Befund (Verstoesse zuerst) | |

## 2. Erwartungen und Abrufe (Erwartung immer mit date-Zeit VOR dem Abruf)

### A1 (Erwartung geschrieben 2026-10-04 18:58:03 CEST, vor dem Abruf)

- Abruf: arXiv-API, search_query = ti:graphity OR abs:"quantum graphity" OR abs:"braided ribbon" OR (abs:braid AND
  abs:preon), nach Datum absteigend, max 60.
- **E1 (Karte):** Quantum Graphity (Konopka/Markopoulou/Severini 2008): Graph mit dynamischen Kanten kuehlt zu einem
  niedrigdimensionalen, regelmaessigen Netz; Materie als Defekte; Lorentz-Invarianz und Lokalitaet offen [L].
- **A1-a (eigene):** Hamma u. a. (Bose-Hubbard auf veraenderlichem Graphen, um 2010): Materie huepft auf dem Graphen und
  formt ihn; Lichtgeschwindigkeit aus Lieb-Robinson-Schranken; keine Einstein-Gleichungen.
- **A1-b (eigene):** Bilson-Thompson/Markopoulou/Smolin (2006/07): Zoepfe aus drei Baendern in gerahmten Spin-Netzen
  tragen die Ladungen der ersten Generation (Verdrillung = Ladung); offen: Dynamik, Wechselwirkung, Masse,
  Propagation (erst 4-wertig, Wan), Schwerkraft-Kopplung.
- **A1-c (Regel 7):** Letzte 24 Monate hoechstens eine Handvoll Arbeiten; keine zeigt Materie, Eichfeld und
  Schwerkraft zugleich.
- **Ausgang A1 (18:58:24):** Antwort "Rate exceeded." (14 Byte, 0 Eintraege). Zaehlt als Abruf 1 von 10, ohne Inhalt
  (Selbstanzeige). Erwartungen E1, A1-a bis A1-c bleiben ungeprueft. Wiederholung erst nach lokaler Arbeit (Pause).

### L-lokal (ohne Abruf): E6, E3 und D-Theorie aus lokalen Kopien frueherer Karten

- **E6 (Karte), lokal geprueft 18:59 (kein Abruf):** **eingetroffen, unvollstaendig.** Kaplan 0912.2560 Z. 1325-1327:
  "any symmetry that is exact on the lattice will be exact in the continuum limit, while any symmetry anomalous in the
  continuum limit must be broken explicitly on the lattice"; Z. 2325-2327: "there is currently no practical way to
  regulate general nonabelian chiral gauge theories on the lattice" [S, lokal chiral-l/quellen]. TPF 2601.04304 Z.
  90-92: "lattice models with strictly local interactions and strictly on-site symmetries generically produce fermions
  in vector-like pairs"; Z. 94-95: "chiral fermions in D spacetime dimensions arise as boundary modes of a gapped system
  in D+1 dimensions"; Z. 229-230: "a complete Hamiltonian realization of the full Standard Model has not yet been
  achieved" [S]. Unvollstaendig: Auswege sind auch nicht-on-site-Symmetrie (Disentangler), SMG auf der Platte, Floquet
  (CHIRAL-L [P]). Eine Zeile, weiter.
- **E3 (Karte), lokal geprueft (kein Abruf):** **eingetroffen.** Gluonen nicht gebaut: GLUONEN-L V1 [P]. Schwerkraft:
  0 Treffer fuer "gravit" in beiden Levin/Wen-Volltexten (cond-mat/0404617 in gluonen-l/quellen, hep-th/0507118 in
  twist-pyro-1/quellen) [S, Negativbefund per grep]. Eine Zeile, weiter.
- **Frage 3, lokal (kein Abruf), wichtig:** Wiese 2107.09335 Z. 782-835 [S, lokal gluonen-l/quellen/F1]:
  - Z. 783-784: "in (4 + 1)-d non-Abelian SU(N) gauge fields can exist in a Coulomb phase with massless gauge bosons".
  - Z. 790-791: endliche Ausdehnung L0, "Assuming that xi >> L0, the theory undergoes dimensional reduction from 4 + 1 to
    4 dimensions"; xi ~ exp(24 pi^2 L0 / (11 N e^2 c)) (Gl. 3.17).
  - Z. 803-805: "It is very natural to incorporate Shamir's variant [74] of Kaplan's domain wall fermions [75] in this
    (4 + 1)-d setup, which can be regularized in the D-theory framework with SU(N) quantum links [65]".
  - Z. 827: "At finite extent L0, the domain wall fermions have a residual mass mu = 2M exp(-M L0)".
  - Z. 829-831: "For a sufficiently large domain wall mass M > [24 pi^2 / ((11N - 2N_f) e^2 c), Layout gelesen [M]], the
    theory reaches the chiral limit together with the continuum limit".
  - Brower/Chandrasekharan/Wiese hep-th/9704106 (Abstract, lokale API-Kopie gluonen-l/quellen/F6-api-batch.xml Z. 150):
    "formulated with a fifth Euclidean dimension, whose extent resembles the inverse gauge coupling ... The inclusion of
    quarks is natural in Shamir's variant of Kaplan's fermion method, which does not require fine-tuning to approach
    the chiral limit" [S Abstract].
  - **[ES] Kopplung vor Bauteil (Regel 6):** Haendigkeit (Restmasse ~ exp(-M L0)) und Kleber-Kontinuum (xi ~
    exp(+c L0/e^2)) sind **zwei Exponentiale derselben Plattendicke L0**; die Bedingung "chiral und Kontinuum zugleich"
    ist ein Verhaeltnis der beiden Raten (mu xi -> 0), also eine Bedingung an M e^2, nicht an ein Bauteil.
  - **[ES] Grenze:** Das ist QCD, also **vektorartig**: Dasselbe Gluonfeld koppelt an beide Waende (links oben, rechts
    unten), zusammen ein Dirac-Quark mit exakter chiraler Symmetrie. Die Haendigkeit des Standardmodells (nur
    Linkshaender spueren die schwache Kraft) verlangt, dass das Eichfeld die Waende unterscheidet. Das ist der offene
    Teil (Kaplan Z. 2325-2327; CHIRAL-L: Kaplan/Sen 2024, Dang/Karur/Sen 2026 "Gauge field flow for chiral gauge theories
    on a slab" [P, dort S Abstract]).
  - **Erwartungsverstoss-Kandidat (gegen GEMEINSAMES-NETZ-v1, Beobachtung [ES]):** Die "zwei unabhaengigen Straenge" sind
    in der Literatur seit 1997 **ein** Strang (Brower/Chandrasekharan/Wiese). Neu waere am Projekt nur die Floquet-Fassung
    und Finns Geometrie, nicht die Verbindung.

### A2 = Wiederholung A1 (Erwartung geschrieben 2026-10-04 18:59:44 CEST, vor dem Abruf)

- Gleiche Abfrage wie A1, gleiche Erwartungen E1, A1-a, A1-b, A1-c (unveraendert, da A1 ohne Inhalt).
- **Ausgang A2 (19:00:22):** wieder "Rate exceeded." (0 Eintraege). Abruf 2 von 10, ohne Inhalt (Selbstanzeige).
  Folgerung: Die API ist vermutlich durch parallele Agenten derselben Adresse gedrosselt. Plan geaendert: naechster
  Versuch als id_list-Stapel mit dem hoechsten Wert (Saetze fuer Frage 2); scheitert er, Ausweich auf arxiv.org/abs.

- **Lokal, kein Abruf (19:01): Satz zu L8.** Surya 2019 (Living Rev. Rel., lokal RUNDE-22/geometrie-stand/hilfs/
  surya-1903.11544.txt): Z. 128-132 "it does not violate Lorentz invariance as shown in an elegant theorem by Bombelli et
  al (2009) ... The combination of discreteness and Lorentz invariance moreover gives rise to an inherent and
  characteristic non-locality"; Z. 1401 "the valency of the graph C is infinite"; Z. 1579-1584 "Theorem 2 In dimensions
  n > 1 there exists no equivariant measurable map D : C(M^d, rho_c) -> H" [S]. [ES] Damit ist L8 kein offenes
  Bauproblem, sondern die Weiche selbst als Satz: endliche Valenz (lokal) heisst Vorzugssystem; ohne Vorzugssystem
  unendliche Valenz. Die Richtung "endliche Valenz -> Vorzugssystem" steht nicht woertlich da, folgt aber, weil eine
  endliche Nachbarmenge eine Richtung auszeichnen wuerde [ES, nicht an der Quelle geprueft].

### A3 (Erwartung geschrieben 2026-10-04 19:01:19 CEST, vor dem Abruf)

- Abruf: arXiv-API id_list = 1409.2509, 1710.01791, cond-mat/0302460, gr-qc/0403053, gr-qc/0605006, hep-th/0603022,
  0801.0861 (Saetze fuer Frage 2 plus zwei Graphity/Band-Arbeiten als Ersatz fuer A1).
- **A3-a (E5-Umfeld):** Marolf 1409.2509: Emergente Gravitation aus einer lokalen, nicht gravitativen Theorie verlangt
  kinematische Nichtlokalitaet, weil der Hamilton-Operator der Gravitation ein Randterm ist.
- **A3-b:** Witten 1710.01791: Eichsymmetrie kann emergent sein; Weinberg-Witten verbietet ein emergentes Graviton in
  einer Lorentz-invarianten Theorie mit erhaltenem Energie-Impuls-Tensor; Ausweg: emergente Raumzeit (Holografie).
- **A3-c (L4/L1):** Levin/Wen cond-mat/0302460: In lokalen bosonischen Modellen treten Fermionen nur zusammen mit
  Eichfeldern auf (Stringenden).
- **A3-d (L2):** Collins u. a. gr-qc/0403053: Lorentz-verletzender Regler gibt per Schleifen O(1)-Abweichungen der
  Grenzgeschwindigkeiten, ohne Feinabstimmung nicht klein. (Bekannt aus LICHT-GLEICH-L [P]; nur Bestaetigung.)
- **A3-e (L8):** Bombelli/Henson/Sorkin gr-qc/0605006: wie Surya oben.
- **A3-f (E1):** Konopka/Markopoulou/Severini 0801.0861: wie E1.
- **A3-g (A1-b):** Bilson-Thompson/Markopoulou/Smolin hep-th/0603022: wie A1-b.
- **Ausgang A3 (19:02:36, 7 Eintraege, quellen/A3-api-saetze.xml):**
  - **A3-a Marolf 1409.2509: VERLETZT (Hauptverstoss bisher).** Erwartet war die Weinberg-Witten-Logik mit dem Ausweg
    "keine volle Lorentz-Invarianz" (E5). Abstract Z. 87: "arguments forbidding non-linear dynamical gravity from
    appearing in the low energy effective description of field theories with local kinematics, even for those with
    instantaneous long-range interactions ... gravitational theories with universal coupling to energy -- an
    intrinsically non-linear phenomenon -- are characterized by Hamiltonians that are pure boundary terms on shell. In
    order for this to be the low energy effective description of a field theory with local kinematics, all bulk
    dynamics must be frozen ... The result applies to theories defined either on a lattice or in the continuum, and
    requires neither Lorentz-invariance nor translation-invariance" [S Abstract]. **Korrigierte Erwartung:** Der Ausweg
    "Ruhesystem" (Finns Netz A) hilft gegen Weinberg-Witten, nicht gegen Marolf. Verboten ist nichtlineare, universell an
    die Energie koppelnde Schwerkraft aus lokaler Kinematik; lineare Spin-2-Moden (Gu/Wen, Regge-Wellen) nicht. -> Volltext
    noetig (Annahmen "local kinematics", Status der linearen Moden, Auswege). Voller Analysezyklus.
  - **A3-b Witten 1710.01791:** Abstract nennt Weinberg-Witten nicht ("gauge symmetries may be emergent"); weder
    bestaetigt noch verletzt. Eine Zeile.
  - **A3-c Levin/Wen cond-mat/0302460: eingetroffen.** "fermions always come in pairs and their creation operator always
    has a string-like structure ... the fermions always couple to a nontrivial gauge field ... exactly soluble examples
    ... in 2 and 3 dimensions" [S Abstract; "We argue", kein strenger Satz].
  - **A3-d Collins u. a. gr-qc/0403053: eingetroffen.** "Lorentz violation at the percent level, some 20 orders of
    magnitude higher than earlier estimates, unless the bare parameters of the theory are unnaturally strongly
    fine-tuned" [S Abstract].
  - **A3-e Bombelli/Henson/Sorkin gr-qc/0605006: eingetroffen, und mein [ES] oben ist jetzt [S Abstract]:** "there is no
    way to associate a finite-valency graph to a sprinkling consistently with Lorentz invariance".
  - **A3-f Konopka/Markopoulou/Severini 0801.0861: teils verletzt (E1).** "background independent model for emergent
    locality, spatial geometry and matter ... evidence that the model also has a low-energy phase in which the graph ...
    appears to be ordered, low-dimensional and local ... thermodynamically stable under local perturbations. The model
    can also give rise to an emergent U(1) gauge theory in the ground state by the string-net condensation mechanism of
    Levin and Wen" [S Abstract]. Lokalitaet ist nicht "offen", sondern mit Evidenz behauptet; Licht (U(1)) kommt dazu,
    auf demselben Graphen. Schwerkraft-Dynamik und Lorentz-Invarianz: im Abstract nicht.
  - **A3-g Bilson-Thompson/Markopoulou/Smolin hep-th/0603022: teils verletzt (A1-b).** "local excitations that can be
    mapped to the first generation fermions ... propagate coherently as they can be shown to be noiseless subsystems
    ... braiding of graphs ... ribbon graphs embedded in a three-dimensional manifold ... dynamics is given by local
    moves ... matter appears to be already included in the microscopic kinematics and dynamics" [S Abstract].
    Propagation ist behauptet, nicht offen. Offen laut Abstract: Wechselwirkung, Masse, Eichbosonen, Spin.
    [ES] Finns "Kanten = Baender mit markierter Seite" sind Bandgraphen; dort traegt die Verdrillung die Ladung (Helon-
    Modell, Bilson-Thompson 2005 [L]), im Projekt die Rahmung den Spin 1/2 (TWIST-PYRO-1 [P]). Zwei Lesarten derselben
    Struktur.

### A4 (Erwartung geschrieben 2026-10-04 19:03:49 CEST, vor dem Abruf)

- Abruf: Volltext Marolf, arXiv:1409.2509 (PDF), pdftotext.
- **A4-a:** "Local kinematics" heisst Tensorprodukt-Hilbertraum bzw. lokale Operatoralgebra (Gitter erlaubt).
- **A4-b:** Lineare Gravitonen (Gu/Wen, Xu) sind ausdruecklich nicht ausgeschlossen; verboten ist erst die
  nichtlineare, universelle Kopplung (Gauss-Gesetz fuer Energie).
- **A4-c:** Als Auswege nennt der Text AdS/CFT (Rand-Theorie, eine Dimension weniger) und Eichredundanz bzw.
  Zwangsbedingungen, nicht Lorentz-Verletzung.
- **A4-d:** Weinberg-Witten wird als verwandt, aber schwaecher (Lorentz-Annahme) eingeordnet.
- **Ausgang A4 (19:03:57, 6 S., quellen/A4-marolf-1409.2509.txt; Zeilen = Zeilen dieser Textdatei):**
  - **A4-a eingetroffen, praezisiert.** Definition II, Z. 168-171: "a theory will be said to be kinematically local iff
    the commutator of two gauge-invariant local Heisenberg-picture operators (with at least one bosonic) vanishes when
    evaluated at different spatial locations at a common time"; Z. 174-176: bulk simultaneity "a background structure
    independent of dynamical fields"; Z. 186-188: "H(t) may be arbitrarily non-local in space. In particular,
    instantaneous long-range interactions are allowed" [S]. [ES] Finns Netz (A) mit aeusserer Uhr erfuellt genau diese
    Annahmen.
  - **A4-b eingetroffen.** Z. 91-92: "our arguments place no constraints on the emergence of strictly linear spin-2
    degrees of freedom"; Z. 281-283: "Thus the linearized theory is free to appear in an effective description as found
    in [15, 16, 19, 20]" (= Xu 2006 zweimal, Gu/Wen 2012, Xu/Horava 2010) [S].
  - **A4-c teils.** Auswege Z. 246-248: "the consequences of our theorem can be avoided by introducing a priori kinematic
    non-localities violating our assumptions. The gauge/gravity dualities of string theory are examples" [S]. Eichredundanz
    als Ausweg steht nicht da; Lorentz-Verletzung ausdruecklich nicht (Fussnote 2, Z. 99-101: "Lorentz-violating theories
    that couple universally to energy may be constructed in analogy with Horava-Lifshitz gravity"). Horava-Lifshitz
    selbst koppelt nicht universell an Energie (Z. 162-164), wird aber von der Impuls-Fassung erfasst (Z. 280-281) [S].
  - **A4-d eingetroffen.** Z. 54-56, 65: Weinberg-Witten "already excludes the emergence of gravity from local
    Poincare-invariant field theories ... one might attempt to evade the theorem by working on a lattice as in e.g. [9,
    15, 16, 19, 20]" [S].
  - **Satz (Z. 218-220):** "Consider any limit where the effective description of a local theory is a gravitational
    theory with universal coupling to energy, the same notion of time evolution, and a compatible definition of
    locality. In this limit all local observables away from the boundary become independent of time." [S]
  - **Annahme "compatible notions of locality" (Z. 203-207):** die Schwerkraft-Beschreibung und die lokale Theorie
    teilen, was Rand und was Inneres ist. Faellt sie, ist das die geforderte Nichtlokalitaet (Z. 249-252) [S].
  - **[ES] Zwei Regime (Regel 1):** "Gu/Wen: Quantengravitation wenigstens linear" gegen "Weinberg-Witten/Marolf:
    emergente Schwerkraft verboten" widersprechen sich nicht. Moderator: **linear gegen nichtlinear**, genauer: ob das
    Schwerefeld die gesamte Energie einschliesslich seiner eigenen als Randfluss traegt (Gauss-Gesetz fuer Energie).
  - **[ES] Folge fuer L3:** Finns festes Netz (A) darf lineare Spin-2-Wellen tragen (wie gerechnet), aber keine
    nichtlineare, universell an die Energie koppelnde Schwerkraft, solange seine Kinematik lokal ist und Rand/Inneres
    mit der Schwerkraft-Beschreibung teilt. L3 ist damit in seiner nichtlinearen Form ein **Satz** (mit Annahmen), nicht
    offen. Offen bleiben die Auswege: (i) die Kantenlaengen sind selbst die Schwerkraft mit ihren Zwangsbedingungen
    (Regge, CDT; dann "eingesetzt", GRAVITON-NETZ-L Regime A [P]), (ii) Nichtlokalitaet (Kausalmenge, Weiche B),
    (iii) Holografie (Schwerkraft eine Dimension hoeher als die lokale Theorie).
  - **[ES] Spannung zur Platte (Frage 3):** In der D-Theorie lebt die lokale Theorie in der Platte und unsere Welt am
    Rand; in Marolfs Ausweg (Holografie) lebt die lokale Theorie am Rand und die Schwerkraft im Inneren. Dieselbe
    Zusatzrichtung kann nicht beides zugleich sein, ohne die Annahme "kompatible Lokalitaet" zu brechen [H].

### A5 (Erwartung geschrieben 2026-10-04 19:05:01 CEST, vor dem Abruf)

- Abruf: arXiv-API, 24 Monate (submittedDate 2024-10-04 bis 2026-10-04) AND (abs:"emergent graviton" OR abs:"emergent
  gravitons" OR (abs:"emergent gravity" AND abs:lattice) OR (abs:graviton AND abs:qubit)), nach Datum, max 60.
- **E2 (Karte) mit Regel 7:** Emergente Gravitonen aus Gittermodellen (Spin 2), Probleme bei Lorentz-Invarianz und
  Materiekopplung [L].
- **A5-a:** 10 bis 40 Treffer; die meisten sind Festkoerper-"Gravitonen" (chirale Gravitonmoden im fraktionalen
  Quanten-Hall-Effekt, Fraktonen, Rang-2-U(1)), also Spin-2-Moden in 2+1 bzw. ohne Energiekopplung.
- **A5-b:** Keine Arbeit zeigt auf einem lokalen Gitter nichtlineare, universell an die Energie koppelnde Schwerkraft;
  hoechstens eine behauptet einen Ausweg aus Weinberg-Witten/Marolf.
- **A5-c:** Keine Arbeit hat Gravitonen und Eichbosonen und Fermionen aus **einem** Gittermodell.
- **Ausgang A5 (19:05:11, 11 Eintraege, quellen/A5-api-graviton-24m.xml):**
  - **A5-a verletzt (Methode):** Kein einziger Treffer mit "emergent graviton(s)" oder "emergent gravity" plus "lattice";
    die 11 Treffer kommen alle aus dem Zweig graviton AND qubit (Gravitations-Verschraenkung, Streuung, Simulation).
    Moegliche Ursache: Phrasensuche zu eng (Festkoerperarbeiten schreiben "chiral graviton", "fracton") [ES]. Das ist ein
    Befund ueber meine Abfrage, nicht ueber die Literatur (Selbstanzeige).
  - **A5-b/A5-c:** in dieser Abfrage nichts dafuer und nichts dagegen. Naechster Treffer am Thema: Nunez u. a.
    2511.04358, "Gauge and diffeomorphism invariance from quantum information principles": Streuamplituden, kein Gitter
    [S Abstract]. Urteil nach Regel 7: "nach Recherchestand nicht belegt" (kein "widerlegt"). Fuer L3 traegt ohnehin
    Marolfs Satz (A4), nicht das Fehlen von Arbeiten.

### A6 (Erwartung geschrieben 2026-10-04 19:05:42 CEST, vor dem Abruf)

- Abruf: arXiv-API, (abs:"causal dynamical triangulations" AND (ti:scalar OR ti:matter OR ti:gauge OR ti:"Yang-Mills"
  OR ti:field OR ti:fields)) OR (abs:"dynamical triangulations" AND (ti:fermion OR ti:fermions)), nach Datum, max 60.
- **E4 (Karte):** CDT mit Materie: Materie veraendert die Phasenstruktur kaum; Fermionen schwierig [L?].
- **A6-a (eigene):** Ambjorn u. a. (um 2021): Ein Skalarfeld mit springenden Randbedingungen veraendert die Topologie
  bzw. die Phase ("matter-driven") -> E4 waere dann teils verletzt.
- **A6-b:** Eichfelder auf CDT nur in 2D (kompaktes U(1)); in 4D-CDT keine Eichfelder.
- **A6-c:** Fermionen nur auf euklidischen DT (Kaehler-Dirac, Catterall/Laiho u. a.), nicht auf CDT.
- **A6-d:** Keine Arbeit mit Skalar, Eichfeld und Fermion zugleich auf einer dynamischen Triangulierung in 4D.
- **Ausgang A6 (19:05:52, 22 Eintraege, quellen/A6-api-cdt-materie.xml):**
  - **E4 verletzt in 2D, in 4D nicht geprueft.** Ambjorn u. a. 1201.1590: 2D-CDT mit d masselosen Skalaren hat eine
    "c=1 barrier"; "For d>1 the effective average geometry is no longer toroidal but 'semiclassical' and spherical with
    Hausdorff dimension d_H = 3" [S Abstract]. 1412.3434: der "blob" (d = 4) hat D_S = 2 [S Abstract]. Materie
    veraendert die Geometrie also stark, sobald genug davon da ist (Moderator: Materiemenge c bzw. d) [ES].
    "Matter-driven change of spacetime topology" (Ambjorn u. a. um 2021, A6-a) kam in dieser Abfrage nicht vor; A6-a
    bleibt [L?].
  - **A6-b verletzt:** 4D-Eichfelder auf CDT gibt es: 2411.12668 "4D SU(N) gauge theories coupled to gravity in the
    Causal Dynamical Triangulations (CDT) approach ... topology emerges on thermalized triangulations only in the
    so-called C-phase of CDT" [S Abstract], aber "over fixed triangulations", also ohne Rueckwirkung auf die Geometrie.
    2D mit Rueckwirkung: U(1), SU(2) (2010.15714, 2112.03157) [S Abstract].
  - **A6-c eingetroffen:** Fermionen nur auf euklidischen DT: Kaehler-Dirac "in the quenched approximation where the
    geometry is allowed to fluctuate but there is no back-reaction", vierfache Entartung wie bei gestaffelten Fermionen
    (1810.10626); Majorana in 2D-EDT (2212.07412) [S Abstract]. Auf CDT keine.
  - **A6-d eingetroffen:** 2112.03157: Eichfelder auf CDT "as a step towards studying, ultimately, systems of gravity
    coupled with bosonic and fermionic matter" [S Abstract]. Das Gesamtsystem ist erklaertes Fernziel.
  - **Nicht vorgesehen:** Sakharov auf Triangulierungen, 2505.07102 (2025): "free massive scalar field theory in
    two-dimensional Lorentzian spacetime, an effective gravitational action emerges ... The generalization to higher
    dimensions and other models is also discussed, but the details are left for future work" [S Abstract]. Passt zum
    Projektstrang INDUZIERT (2D Polyakov) [P]; Bezug im Gegensweep pruefen.

### A7 (Erwartung geschrieben 2026-10-04 19:07:34 CEST, vor dem Abruf)

- Abruf: arXiv-API id_list = hep-ph/0104152, hep-th/9612128, hep-th/9906064, hep-th/0105243, hep-lat/0309182,
  1511.03649, hep-th/0007220.
- **A7-a Rubakov-Review:** Fermionen sitzen als chirale Nullmoden auf einer Domaenenwand (Jackiw-Rebbi,
  Rubakov/Shaposhnikov); Eichfelder auf der Wand festzuhalten ist das Problem; Schwerkraft haelt die Verzerrung (RS2).
- **A7-b Dvali/Shifman:** Eichfelder bleiben auf einer Wand, wenn das Innere (Bulk) einschliesst (confining).
- **A7-c Randall/Sundrum II:** 4D-Newton auf einer Brane trotz unendlicher 5. Dimension (AdS5-Verzerrung).
- **A7-d Dubovsky/Rubakov:** Problem der Ladungsuniversalitaet fuer festgehaltene Eichfelder.
- **A7-e Brower u. a. 2004:** D-Theorie voll: Quantenspins und Quantenlinks, QCD mit Domain-Wall-Quarks.
- **A7-f Grabowska/Kaplan:** chirale Eichtheorie auf einer 5D-Platte, Eichfeld per Gradientenfluss in die Platte
  verlaengert; Spiegelfermionen koppeln nur an ein glattes Feld; Vorschlag, nicht gezeigt.
- **A7-g Boulanger/Damour/Gualtieri/Henneaux:** Mehrere masselose Spin-2-Felder koennen nicht konsistent
  miteinander wechselwirken; es bleiben getrennte Welten (Bezug: Finns Netz traegt in Bauweise B1 zwei Welten ohne
  gegenseitige Anziehung [P]).
- **Ausgang A7 (19:07:45, 7 Eintraege, quellen/A7-api-platte-wand.xml):**
  - **A7-a Rubakov hep-ph/0104152: im Abstract nur der Rahmen** ("ordinary matter (with possible exceptions of gravitons
    ...) is trapped to a three-dimensional submanifold --- brane"; "extra dimensions may be large, and even infinite")
    [S Abstract]. Domain-Wall-Fermionen und Eichfeld-Problem stehen nicht im Abstract; nicht weiter abgerufen.
  - **A7-b Dvali/Shifman: eingetroffen, praezisiert:** "massless gauge bosons localized on the wall ... outside the wall
    the theory is in the non-Abelian confining phase, while inside the wall it is in the Abelian Coulomb phase" [S
    Abstract]. Festgehalten wird ein **abelsches** Feld (Licht), kein Kleber.
  - **A7-c Randall/Sundrum II: eingetroffen.** "a single 3-brane embedded in five dimensions ... even without a gap in the
    Kaluza-Klein spectrum, four-dimensional Newtonian and general relativistic gravity is reproduced" [S Abstract].
  - **A7-d Dubovsky/Rubakov: eingetroffen und verschaerft (Verstoss gegen meine stille Annahme "Wand-Welt traegt alles"):**
    "in the non-Abelian case the gauge fields inside the brane are never four-dimensional and their self-interaction is
    strong at all distances of interest. Hence this mechanism does not work for d>2 ... At d=1, however, the bulk gauge
    fields are strongly coupled in the non-Abelian case"; Ladungsuniversalitaet im Dvali/Shifman-Typ "enforced by the
    presence of 'confining strings'" [S Abstract].
  - **A7-e Brower u. a. 2004: eingetroffen.** "classical gauge fields are replaced by quantum links ... provided the
    (d+1)-dimensional D-theory is massless. When the extent of the extra Euclidean dimension becomes small in units of the
    correlation length, an ordinary d-dimensional quantum field theory emerges by dimensional reduction" [S Abstract].
  - **A7-f Grabowska/Kaplan: eingetroffen, mit Zusatz (nicht vorgesehen, wichtig fuer L9):** "gauge fields that reside
    on one d-dimensional surface and are extended into the bulk via gradient flow ... mirror fermions couple to the gauge
    fields via a form factor that becomes exponentially soft ... A physical realization of this construction would imply
    the existence of mirror fermions in the standard model that are invisible except for interactions induced by vacuum
    topology, and which could gravitate differently than conventional matter" [S Abstract].
  - **A7-g Boulanger/Damour/Gualtieri/Henneaux: eingetroffen, und als Satz staerker als erwartet:** "there is no
    consistent (ghost-free) coupling, with at most two derivatives of the fields, that can mix the various 'gravitons'
    ... The only possible deformations are given by a sum of individual Einstein-Hilbert actions. The impossibility of
    cross-couplings subsists in the presence of scalar matter"; "in any spacetime dimension >=3" [S Abstract].
    [ES] Finns Netz in Bauweise B1 (zwei Welten, 4 statt 2 Helizitaet-2-Moden, WEICHE-STAND-v5 [P]): Bleiben beide
    masselos, verbietet der Satz (im Lorentz-invarianten Grenzfall, hoechstens zwei Ableitungen) jede Kreuzkopplung. Die
    "zwei Welten ohne gegenseitige Anziehung" sind dann kein Gitterfehler, sondern die einzige konsistente Lesart.
  - **[ES] Zwei Regime der Platte (Regel 1):** (i) endliche Platte, Inneres in der Coulomb-Phase, Dimensionsreduktion
    (D-Theorie): nichtabelscher Kleber und vektorartige Haendigkeit ja, Schwerkraft nicht enthalten; (ii) unendliches
    Inneres mit Festhalten auf der Wand (Branenwelt): Schwerkraft (RS2), Fermionen (Domain-Wall) und Licht (Dvali/
    Shifman) ja, nichtabelscher Kleber nein (Dubovsky/Rubakov). Moderatoren: Ausdehnung der Zusatzrichtung (L0 << xi
    gegen unendlich) und Phase des Inneren (Coulomb gegen einschliessend). Kein Regime traegt alle vier.
- **Berichtigung 19:09 zu "Zwei Regime der Platte" oben:** "nichtabelscher Kleber nein" ist zu stark. Gelesen ist nur:
  Dvali/Shifman halten ein abelsches Feld fest; der branen-induzierte Mechanismus scheitert nichtabelsch fuer d > 2 und
  ist bei d = 1 stark gekoppelt (Dubovsky/Rubakov). Richtig: "nichtabelscher Kleber auf der Wand nicht gezeigt".
- **Projektbezug (lokal, 19:09):** TENSOR-EIS-PYRO-1/ERGEBNIS.md Z. 35-41 [P]: Bauweise B1 "zerfaellt exakt in zwei
  unabhaengige Kopien"; Z. 74: "Massen auf einer Auf- und einer Ab-Mitte haben exakt keine Wechselwirkung"; Z. 194-195
  [H]: "Eine Kopplung, die die Kopien bindet; sie muss eichinvariant und damit von Kruemmungsordnung sein, also bleiben
  beide Zweige masselos." [ES] Gegen BDGH: mit hoechstens zwei Ableitungen ist eine solche Bindung zweier masseloser
  Zweige unmoeglich; Kruemmungsordnung (vier Ableitungen) liegt ausserhalb des Satzes, bringt aber in der Regel Geister
  [L]. Kandidat fuer Frage 4.

### A8 (Erwartung geschrieben 2026-10-04 19:09:38 CEST, vor dem Abruf) = Wiederholung der Abfrage A1

- Gleiche Abfrage wie A1 (Graphity, Bandzoepfe, alle Jahre, nach Datum, max 60).
- Erwartungen jetzt angepasst an A3: E1 und A1-b sind teils schon beantwortet (A3-f, A3-g). Neu erwartet:
  - **A8-a:** Folgearbeiten nennen Probleme der Graphity-Tiefphase (zu viele Dreiecke bzw. falsche Dimension,
    Abhaengigkeit von Feinabstimmung der Kopplungen).
  - **A8-b:** Bandzopf-Programm: 4-wertige Bandnetze (Wan, Hackett, He), Erhaltungsgroessen der Zoepfe; Wechselwirkung
    und Masse bleiben offen; keine Arbeit nach 2015.
  - **A8-c (Regel 7):** In den letzten 24 Monaten hoechstens 2 Arbeiten zu Graphity; keine mit Schwerkraft-Dynamik.
- **Ausgang A8 (19:09:52, 40 Eintraege, quellen/A8-api-graphity-baender.xml):**
  - **A8-a eingetroffen, und damit E1 VERLETZT:** Die Tiefphase ist nicht von selbst ein regelmaessiges Netz.
    1506.07588 (2015): "the model as originally presented favours a graph composed of small disjoint subgraphs. Such a
    disconnected space is a poor representation of our universe. A new term ... hypervalence term ... causes a connected
    lattice-like graph to be favoured" [S Abstract]. 1808.05632 (2018): "the simple Hamiltonians used in Quantum
    Graphity models are highly degenerate, having multiple ground states that are not lattices ... We then propose a
    Hamiltonian that has a rectangular lattice as a ground state ... the defects from the perfect lattice seem to behave
    like particles of quantized mass that attract one another" [S Abstract]. 1804.10793 (2018): "in the continuous limit
    (N -> infinity) the complete graph reduces to the set of disconnected points" [S Abstract].
    **Korrigierte Erwartung:** Das regelmaessige Netz muss in die Schrittregel hineingebaut werden (Zusatzterme,
    massgeschneiderter Hamilton-Operator). Passt zu TETRAEDER-L [ES dort]: "K-A setzt sein Netz ein" [P].
  - **A8-b teils verletzt:** Bandzopf-Review 1109.0080 (2011): "the tetravalent scheme has naturally substantiated a rich,
    dynamical theory of interactions and propagation of braids, which is ruled by topological conservation laws" [S
    Abstract]; 0811.2161: "an infinite number of species of conserved quantities" [S Abstract]. Arbeiten nach 2015 gibt es
    (2004.11140, 2501.03260). 2501.03260 (2025): "Braids correspond to chirality, and twists, to charges. We note that this
    model captures only the SU(3)_c x U(1)_em sector of the standard model" [S Abstract]. Mein [ES]-Vermerk zu A3-g
    ("Verdrillung = Ladung") ist damit [S Abstract].
  - **A8-c eingetroffen:** In den letzten 24 Monaten keine Graphity-Arbeit in dieser Abfrage (juengste 1901.00446,
    2019); Bandzoepfe: nur 2501.03260 (Darstellungstheorie, keine Dynamik) [S API]. Urteil "nach Recherchestand ruht
    das Programm", nicht "gescheitert".
  - **[ES] Zwei Regime der Haendigkeit (Regel 1):** (i) Haendigkeit als Spektraleigenschaft (Weyl-Kegel, Dispersion):
    Nielsen-Ninomiya bzw. Anomalie-Satz greift, Ausweg Platte; (ii) Haendigkeit als topologisches Etikett (Zopf-
    Chiralitaet, Helon-Modell): kein Bandspektrum, kein NN, aber auch keine Weyl-Dynamik gezeigt. Unterscheidungspunkt:
    ob das chirale Objekt eine Weyl-Dispersion hat und nur linkshaendig an die schwache Kraft koppelt.

### A9 (Erwartung geschrieben 2026-10-04 19:10:43 CEST, vor dem Abruf)

- Abruf: arXiv-API, (submittedDate 2024-10-04 bis 2026-10-04 AND (abs:"Weinberg-Witten" OR (abs:"emergent gravity" AND
  (abs:"no-go" OR abs:nonlocal OR abs:"non-local" OR abs:nonlocality)) OR abs:"multi-graviton" OR abs:"multiple
  gravitons")) OR (abs:"causal dynamical triangulations" AND abs:scalar AND (abs:"four-dimensional" OR abs:"four
  dimensions")), nach Datum, max 60.
- Zweck: Regel 7 vor den negativen Urteilen zu L3 (Marolf, BDGH) und E4 in 4D.
- **A9-a:** 0 bis 10 Treffer im 24-Monats-Teil; keiner zeigt nichtlineare, universell koppelnde Schwerkraft aus lokaler
  Gitterkinematik; keiner hebt BDGH auf (hoechstens Bigravity-Varianten mit einer massiven Mode).
- **A9-b (E4, 4D):** Ambjorn u. a. zeigen, dass ein Skalarfeld mit Sprung-Randbedingung die 4D-CDT-Geometrie bzw.
  Topologie aendert; sonst ist die Rueckwirkung in 4D klein.
- **Ausgang A9 (19:10:54, 10 Eintraege, quellen/A9-api-regel7-cdt4d.xml):**
  - **A9-a teils verletzt:** Es gibt einen neuen Anspruch, Weinberg-Witten zu umgehen: 2602.11806 (Essay, Feb. 2026),
    "the effective action of a non-gravitating quantum field theory in the ultraviolet (UV) develops an Einstein-Hilbert
    term in the infrared ... the RG flow of boundary conditions ... 'unfreezing' the metric ... also provides the
    mechanism to evade the Weinberg-Witten no-go theorem" [S Abstract]. Das ist der holografische Ausweg (Marolf Z.
    246-248), kein lokales Gitter. Mehrfach-Gravitonen: 2501.16442 (Jan. 2025) "ghost free massive gravity and their
    multi-graviton extensions ... arising from a higher dimensional theory of gravity, upon discretising the extra
    dimension ... important information related to the extra dimension is missing ... improved deconstruction procedure
    that maintains the free lapse" [S Abstract]. Mit Massen ist Mehrfach-Gravitation konsistent; BDGH betrifft nur
    masselose Kreuzkopplung. Kein Treffer zeigt nichtlineare Schwerkraft aus lokaler Gitterkinematik.
    **Regel-7-Urteil:** "per Satz mit Annahmen ausgeschlossen (Marolf 2014); Gegenbeispiel nach Recherchestand (24
    Monate, arXiv) nicht gefunden".
  - **[ES] nicht vorgesehen, Bezug Frage 3:** Eine Platte aus Lagen von Finns Netz mit je eigenen Kantenlaengen waere
    "dekonstruierte" Zusatzdimension: je Lage ein Graviton, gekoppelt zu Mehrfach-Gravitation (eine masselose Mode plus
    massiver Turm). Nach 2501.16442 fehlt dabei ohne freie Lapse die Hamilton-Zwangsbedingung der Zusatzrichtung [H].
  - **A9-b nicht geprueft:** Der 4D-Teil fand nur die 2D-Arbeiten (1201.1590, 1412.3434) wieder. E4 in 4D bleibt [L?].

### Gegensweep-Pruefungen lokal (19:11 bis 19:12, kein Abruf)

- **G-a "Marolf ist im Projekt unbekannt":** geprueft (grep ueber coordination, model-lab): Treffer nur in Rohtexten
  fremder Quellen (Literaturlisten), in keiner Analyse-Datei; WARUM-SPIN-2.md und GF-S0-KLAERUNG ohne Marolf -> neu [P].
- **G-b "Graphity-Probleme sind neu":** geprueft: **falsch.** RUNDE-22/geometrie-stand/ERGEBNIS.md Z. 89 "EV5 - Quantum
  Graphity braucht Zusatzterme", Z. 808-811 mit 0801.0861, 1008.1340, 1506.07588, 1808.05632 [P]. Der E1-Verstoss ist
  also ein Verstoss gegen die Kartenerwartung, nicht neues Wissen fuers Projekt.
- **G-c "2505.07102 ist neu":** geprueft: **falsch.** Schon in INDUZIERT-G-L (quellen/raasakka-2505.07102.txt) und
  RUNDE-22 [P]. Vermerk unter A6 ist damit erledigt.
- **G-d "BDGH (Mehrfach-Gravitonen) ist neu":** geprueft: im Projekt nur Bekaert/Boulanger/Sundell 2012 (hoehere Spins,
  WARUM-SPIN-2.md Z. 266) [P]; BDGH 2001 und die Folge fuer die zwei Kopien von TENSOR-EIS-PYRO-1 nirgends -> neu.

### A10 (Erwartung geschrieben 2026-10-04 19:12:22 CEST, vor dem Abruf; letzter Abruf)

- Abruf: arXiv-API, ti:"matter-driven" OR ti:"matter driven" OR (abs:"causal dynamical triangulations" AND
  ti:"scalar fields") OR (abs:"causal dynamical triangulations" AND abs:"scalar field" AND abs:"phase diagram"), nach
  Datum, max 40.
- **A10-a (E4, 4D):** Ambjorn u. a. (um 2021): Ein Skalarfeld mit nichttrivialen (springenden) Randbedingungen in 4D-CDT
  mit Torus-Raum aendert die Topologie bzw. treibt einen Phasenuebergang ("matter-driven"); ohne Sprung kaum Wirkung.
- **Ausgang A10 (19:12:36, 14 Eintraege, quellen/A10-api-cdt4d-materie.xml; 10 von 14 fachfremd, "matter driven"):**
  - **A10-a eingetroffen, damit E4 auch in 4D verletzt:** Ambjorn u. a., 2103.00198 "Matter-driven change of spacetime
    topology": "The matter fields are multi-component scalar fields taking values in a torus with circumference delta
    in each spatial direction ... Changing delta, we observe a phase transition caused by the scalar field ... the phase
    transition can change the topology to a simply connected one" [S Abstract]. Moderator: Zielraum bzw. Randbedingung
    des Skalars (delta), in 2D die Materiemenge (d > 1).
- **Abrufbilanz:** 10 von 10 verbraucht (A1, A2 ohne Inhalt; A3 bis A10 mit Inhalt). Keine Websuche.

### Nachtraege ohne Abruf (19:14)

- Marolf veroeffentlicht: DOI 10.1103/PhysRevLett.114.031104 (A3-XML, Eintrag 1409.2509) [S API].
- L5 kein Satz: D'Ariano/Perinotti 1306.1934 (lokal chiral-l/quellen) Z. 4-6: "the Dirac equation in three
  space-dimensions emerges from the large-scale dynamics of the minimal nontrivial quantum cellular automaton satisfying
  unitarity, locality, homogeneity, and discrete isotropy. The Dirac equation is recovered for small wave-vector and
  inertial mass" [S]. Ein unitaerer, lokaler Automat mit Masse existiert; L5 ist eine Projektluecke (Umklappen zwischen
  Schrittsaetzen), kein No-go.

### Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | geprueft? | Ergebnis |
|---|---|---|---|
| G-a | Marolf ist im Projekt unbekannt | ja (grep) | stimmt, nur in fremden Literaturlisten |
| G-b | Graphity-Probleme sind neu | ja (grep) | **falsch**: RUNDE-22 EV5 kennt sie |
| G-c | Raasakka 2505.07102 ist neu | ja (grep) | **falsch**: INDUZIERT-G-L |
| G-d | BDGH ist neu | ja (grep) | stimmt |
| G-e | Marolfs Annahme "lokale Kinematik" trifft auf Finns Netz zu | teils ([ES]) | trifft zu, wenn die Kantenlaengen physikalische lokale Groessen mit aeusserer Uhr sind (Weiche A); nicht, wenn sie Eichredundanz tragen (Regge mit Zwangsbedingungen, Weiche C). Welche Lesart Finn meint, ist offen (Rueckfrage) |
| G-f | BDGH gilt auf Finns Netz | nein | Satz setzt Lorentz-invarianten Pauli-Fierz-Grenzfall und hoechstens zwei Ableitungen voraus; das Netz hat ein Ruhesystem. Gilt nur fuer den langwelligen Grenzfall [ES] |
| G-g | Die 4+1-Coulomb-Phase der SU(N)-Quantenlinks existiert | nein | nur Wiese Z. 783-784 (Behauptung im Review) [S]; keine Numerik gelesen |
| G-h | Weinberg-Witten im Wortlaut | nein | nur sekundaer (Marolf Z. 54-56; Carlip ueber GRAVITON-NETZ-L [P]) |
| G-i | D-Theorie-Haendigkeit = SM-Haendigkeit | ja (Wiese Z. 803-831, Kaplan Z. 2325-2327) | nein, vektorartig |

### Kalibrierung (Zwischenstand)

- (a) gemessen: nur Simulationen und Rechnungen der Literatur (CDT/EDT-Monte-Carlo, Graphity-Numerik); ueber Finns Netz
  nichts Neues gemessen; Naturgrenzen (LLR, Pulsare) nur [L].
- (b) verdichtet: Zwei-Regime-Tabellen; "Gauss-Gesetz fuer Energie" als gemeinsame Groesse fuer L3; "L0 setzt beide
  Exponentiale" fuer Frage 3; Satz-Landkarte L1-L9.
- (c) Warnzeichen: Meine Sicherheit "L3 ist ein Satz" stieg stark durch **eine** Arbeit (Marolf), waehrend die Frage in
  linear/nichtlinear, lokal/eichredundant, masselos/massiv zerfiel. Der Satz haengt an "compatible notions of
  locality" und "same notion of time evolution".

### Berichtigungen nach Rueckwaertsdurchgang (Zeilen per grep geprueft)

- Wiese: "chiral limit together with the continuum limit" steht in Z. 833, nicht 829-831 -> richtig Z. 829-833.
  Coulomb-Phase Z. 783-784, Dimensionsreduktion Z. 790-791, Domain-Wall Z. 803-805, Restmasse Z. 827 (bestaetigt).
- Marolf: Satz Z. 218-219 (nicht 218-220); lineare Theorie Z. 281-282 (nicht 281-283); Ausweg Z. 246-248 (bestaetigt);
  "requisite non-locality" Z. 113-115 und "This constitutes a certain non-locality" Z. 236 ersetzen den Verweis
  "Z. 249-252" unter A4 (dort steht die Einbettung in ein Einteilchen-System, nicht die geforderte Nichtlokalitaet).
- Erledigt durch A10: "A6-a bleibt [L?]" (A6) und "A9-b nicht geprueft" (A9); E4 in 4D ist jetzt [S Abstract] verletzt.
- Erledigt durch G-c: "Bezug im Gegensweep pruefen" (A6, 2505.07102 ist Projektwissen).
- Abrufplan Abschn. 1 nicht eingehalten: tatsaechlich A1/A2 gedrosselt, A3 Saetze, A4 Marolf-Volltext, A5 Gravitonen 24
  Monate, A6 CDT/DT mit Materie, A7 Platte/Wand/BDGH, A8 Graphity/Zoepfe, A9 Regel 7, A10 4D-CDT-Materie.

### Abgabe

- DOSSIER.md geschrieben ab 19:16:03, Rueckwaertsdurchgang bis 19:22:57 CEST (date). Berichtigt dort: Kaplan Z. 2324-2326
  (statt 2325-2327), TPF Z. 230-231 (statt 229-230), Autorennamen aus XML, absolute Aussagen an Annahmen gebunden.
- Selbstanzeige: 19:20 Sicherungskopie des Dossiers versehentlich im Session-Scratchpad (gemeinsam mit der Leitung)
  abgelegt und um 19:20:18 wieder entfernt.
