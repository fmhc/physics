# SPIN-KAUSAL-L: Arbeitsfeld (Feldforscher, Runde 38)

- Feldforscher fuer die Leitung claude-primary. Start 2026-10-04 08:57:56 CEST (date), Zeitbox 60 min.
- Dieses Feld ist die einzige Arbeitsdatei (Regel 5). Gestrichenes bleibt mit ~~...~~ stehen.
- Kennzeichen: [S] an der Quelle selbst gelesen (lokal oder Volltext), [S Abstract] nur Abstract woertlich,
  [L] aus dem Gedaechtnis, [L?] unsicher, [ES] eigener Schluss, [H] Hypothese.
- Gelesen vor dem ersten Abruf (08:58 bis 09:04): KARTE.md, RUNDE-38/WEICHE-STAND-20261004.md,
  SCHACHBRETT-KAUSAL-1/ERGEBNIS.md, QCA-TETRA-1/ERGEBNIS.md, QCA-DIAMANT-4/ERGEBNIS.md,
  KAUSAL-4D-STABIL-L/DOSSIER.md Abschn. 9 (Methodenbefund) und dessen Abrufweg (WebFetch speichert PDF, dann
  pdftotext auf stdout).

## 0. Erwartungen der Karte (unveraendert uebernommen, vor jedem Abruf)

| Nr | Erwartung | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | 3+1-Fermionen auf Kausalmengen offen; Surya 2019 nennt es als offen [L?] | **teils eingetroffen**: offen ja, aber Surya nennt Fermionen nicht (V1) | Nomaan X 2023 "Fermions" [S]; Johnston 6.4 [S]; Surya Z. 7928-7931 [S]; A1/A6/A9/A11 |
| E2 | Johnston Kap. 6: 2D-Ansaetze, kein 4D-Dirac-Operator | **teils eingetroffen**: kein 4D-Operator, aber 6.4 allgemein-dimensional (V4) | Johnston S. 143-151 [S] |
| E3 | Neuere Vorschlaege nach 2015 (Rahmen/Clifford je Element, Quantenlaeufe) [L?] | **nicht eingetroffen** (nach Recherchestand nicht belegt): Ideen aelter (2008, 2013/15, 2015), nach 2015 nur FJ 2016 auf festem Gitter (V2) | A1, A6, A9, A11 |
| E4 | Ausweg: Spinor als Zusatzfeld mit lokaler Lorentz-Eichgruppe (Rahmen je Element) [ES] | **eingetroffen als Literaturweg** (Sverdlov), mit Hindernis BHS und Johnstons Kritik | Sverdlov [S]; Johnston 6.2 [S]; Surya Satz 2 [S] |
| E5 | Statistische Lorentz-Invarianz reicht, damit ein eingesetzter Spinor sich im Mittel richtig dreht [H] | **gespalten**: Einbettungsgewichte ja (trivial), Rahmen aus Streuung nein (BHS), kompakt ja | Surya Z. 1525-1600 [S]; S1 [ES] |

## 1. Eigene Vorueberlegung am Schreibtisch (vor dem ersten Abruf, 09:04) [ES, L]

- Unsere QCA-Befunde stuetzen sich auf drei Zutaten, die eine Kausalmenge nicht hat:
  1. Homogenitaet (Cayley-Graph, ueberall dieselbe Nachbarschaft)
  2. ein unitaerer Schritt zwischen festen Zeitschichten (globaler Takt)
  3. eine endliche Nachbarmenge S_+, auf der eine Drehgruppe wirkt
  - Kausalmenge: zufaellig, keine Schichten mit gleicher Elementzahl, in 3+1 unendlich viele Links je Element
    (Lorentz-Invarianz) [L].
- Zwei Wege, auf denen Spin trotzdem hineinkommen koennte:
  - (W1) **Gemittelte Kovarianz mit Einbettungsvektoren:** Gewichte wie sigma.(y-x) aus der Einbettung. Das Mittel ist
    dann automatisch kovariant (Streuung invariant, Faktoren kovariant). Das waere vorab ableitbar, wie SK1 in
    SCHACHBRETT-KAUSAL-1.
  - (W2) **Intrinsisch:** Aus der Ordnung allein gibt es nur Skalare (Zahlen, Volumina, Eigenzeiten).
    - Entlang einer Kette sind alle Elemente paarweise verknuepft. Deshalb ist die Gram-Matrix der Schritte
      Delta_i.Delta_j aus Eigenzeiten intrinsisch.
    - Paritaetsgerade Spuren von gamma-Produkten waeren damit intrinsisch, Weyl-Terme (epsilon) braeuchten eine
      Orientierung [ES, zu pruefen].
- Hinderniskandidat: Bombelli/Henson/Sorkin, "Discreteness without symmetry breaking" [L]. Keine Lorentz-aequivariante
  Zuordnung einer Richtung bzw. eines Rahmens zu Elementen einer Streuung. Grund: keine invariante
  Wahrscheinlichkeit auf der Hyperbel.
  - Folge fuer E4/E5 [ES]: Rahmen je Element koennen nicht aus der Streuung gewaehlt werden, ohne die statistische
    Lorentz-Invarianz zu brechen. Sie muessten Eichfreiheitsgrade sein, mit nicht kompakter Gruppe SO(3,1).
  - Moderator-Kandidat (Regel 1): kompakte Gruppe (euklidisch, SO(4) bzw. Raumdrehungen) gegen nicht kompakte
    (Lorentz).
- Literatur, die ich aus dem Gedaechtnis erwarte [L?]:
  - Sverdlov 2008, "Spinor fields in causal set theory"
  - Jacobson 1984, Spinor-Kettenpfadintegral in 3+1 (Nullschritte mit sigma-Projektoren)
  - Finster, kausale Fermionsysteme (Spinraeume primaer, Kausalstruktur abgeleitet)
  - Kaehler-Dirac-Fermionen auf dynamischen Triangulierungen (Catterall u. a. 2018): Formen statt Spinoren, kein
    Rahmen noetig
  - Christ/Friedberg/Lee 1982, Zufallsgitter
  - Meyer 1996: skalare QCA trivial, innerer Raum erzwungen
  - Friedman/Sorkin 1980: Spin 1/2 aus Topologie (Geonen)

## 2. Abrufprotokoll (Vorhersage vor Abruf; Verstoesse voll, Bestaetigungen eine Zeile)

| Nr | Zeit (date) | Ziel | Vorhersage (vor Abruf) | Ausgang | Verstoss? |
|---|---|---|---|---|---|
| L1 | 09:04-09:05 | lokal: Surya 1903.11544 (Projekttext), grep fermion/spinor/Dirac/spin | Fermionen hoechstens in einem Satz als offen genannt; kein Dirac-Operator | **Keine einzige Erwaehnung** von fermion, spinor oder Dirac (4 Treffer, alle Ising-Spins, Z. 8982-8990). Staerker: Z. 7928-7931 "the only class of matter fields that we know how to study, since at present no well defined representation of non-trivial tensorial fields on causal sets is known"; Z. 7314-7322 kein lokaler Tangentialraum, weil die Valenz unendlich ist | **ja (V1)** |
| A1 | 09:06-09:07 (date-Fenster 09:05:52 bis 09:07:49) | arXiv-API: (abs "causal set" ODER "causal sets") UND (fermion, fermions, fermionic, spinor, spinors, Dirac), neueste zuerst, 50 | Unter 15 Treffer. Darunter Sverdlov 2008 (Spinorfelder), Jones/Yazdi 2026, vielleicht Finsters kausale Fermionsysteme als Fehltreffer. In 24 Monaten keine 3+1-Bauweise | 15 Treffer (totalResults 15). Einschlaegig: Sverdlov 0808.2956 (2008) "Spinor fields in Causal Set Theory"; **Noldus 1305.0443v3 (2013) "Free Fermions on causal sets"** ("We construct a Dirac theory on causal sets; [...] the causet must be regarded as emergent in an appropriate sense too"); **Gudder 1507.01281 (2015)** ("A discrete, free Dirac operator is introduced"); Nomaan X 2306.04800 (2023) "Quantum Field Theory On Causal Sets" (Uebersicht); Jones/Yazdi 2602.16782 (2026); Knuth 1212.2332 (Schachbrett aus Einflussnetz); Earle 1102.1200 ("3 + 1" Dirac, Mastergleichung). Rest fachfremd (Ng, Bianconi, Wieland, Krugly, Sverdlov 1201.5850). In 24 Monaten (ab 2024-10) nur Jones/Yazdi | **teils (V2):** zwei Bauweisen, die ich nicht kannte (Noldus, Gudder); Finster nicht unter den Treffern. Nur Titel und von der Zusammenfassung zitierte Saetze, deshalb A4 woertlich |
| A2 | 09:07:57-09:08:42 (date-Fenster, parallel zu A3, A4) | arXiv 0808.2956 (Sverdlov 2008), PDF; der Zusammenfasser konnte das PDF nicht lesen, es wurde lokal gespeichert, pdftotext auf stdout | Rahmen bzw. Vektorfeld (oder Gamma-Matrizen) je Element als Zusatzfeld; die Spinorstruktur kommt nicht aus der Ordnung; Lorentz-Invarianz nur ueber Mittel oder Bezugswahl; nur Wirkung, keine Rechnung | Eingetroffen. Vierbeine aus **Holonomien** (Zusatzfelder auf der Kausalmenge), Spinor = "leftover degrees of freedom of holonomies plus additional scalar fields"; nur Lagrangedichten, keine Numerik (Notiz A2) | nein |
| A3 | 09:07:57-09:08:42 | arXiv 1305.0443v3 (Noldus 2013, v3 Jan. 2015), PDF lokal, pdftotext | Dirac-Theorie nur mit Zusatzstruktur (Einbettung, Rahmen oder Mannigfaltigkeit "emergent"); kein intrinsischer 4D-Operator aus der Ordnung allein; keine Numerik | Eingetroffen. Clifford-wertige "generating structure" K auf dem Linkgeruest (K K* + K* K = 2·1⊗I); **"not enough information is present in the causal set itself to find a unique solution [...] the dimension is put in by hand"**; Beispiele nur 2-Element-Menge und "Diamant" (Notiz A3) | nein, aber der Satz zur Dimension traegt mehr (siehe V3) |
| A4 | 09:07:57-09:08:42 | arXiv-API id_list, Abstracts woertlich: 2306.04800, 1507.01281, 1102.1200, 1212.2332, 1810.10626 (Catterall u. a., Kaehler-Dirac auf DT, ID aus dem Gedaechtnis) | Nomaan X nennt Fermionen als offen oder gar nicht; Gudder auf eigener gitterartiger Kausalmenge (nicht gestreut); Earle und Knuth ohne Streuung; Catterall: Kaehler-Dirac auf euklidischen DT, kein Spin-Geruest noetig | Teils lesbar: Die Zusammenfassung gab die Abstracts **nicht vollstaendig** wieder ("[continuing ...]"). Woertlich erhalten: Catterall/Laiho/Unmuth-Yockey, PRD 98, 114503 (2018): "natural extension of staggered fermions to random geometries without requring vielbeins and spin connections" (ID und Titel stimmen). Gudder 2015: "the basic structural element is a covariant causal set". Nomaan X 2023: "a broad overview of a construction of a theory for matter on fixed causal set backgrounds". Earle: "derivation of the Dirac equation in '3+1' dimensions [...] master equation approach" | nein, soweit lesbar; Nomaan X offen -> A5 |
| L3 | 09:09:30-09:12 | lokal: Johnston 2010, Doktorarbeit (PDF heute schon von anderer Karte abgerufen, tool-results/webfetch-1791088294035-p4nk6j.pdf, 172 S.), pdftotext S. 140-155 | wie E2: 2D-Skizzen, kein 4D-Dirac-Operator | **Teils verletzt (V4):** 6.4 "Square root of the propagator" ist **dimensionsunabhaengig** formuliert (R_0^2 = -rho Phi ⊗ I, Groesse von I je Dimension), nur ohne Loesung. Johnston wuenscht ausdruecklich, dass die Wurzel die Groesse des Spinraums **erzwingt**. Sverdlov wird zitiert und kritisiert (Notiz L3) | ja (V4) |
| A5 | 09:12:20-09:14:41 (date-Fenster, parallel zu A6, A7) | arXiv 2306.04800 (Nomaan X 2023, Uebersicht QFT auf Kausalmengen), PDF lokal, pdftotext, grep | Nennt Fermionen bzw. Spinoren in einem Satz als offen oder "future work", ohne Bauweise; zitiert Johnston, nicht Sverdlov/Noldus | Eingetroffen. Abschnitt "Fermions": erst brauche man "the retarted Green function analogue on the causal set"; die Antivertauschung sei leicht; Johnstons zwei Vorschlaege; "the square root of a matrix (if it exists) is not unique in general and therefore we may need further constraints". Schluss: Fermionen als kuenftige Richtung (Notiz A5) | nein |
| A6 | 09:12:20-09:14:41 | arXiv-API: (abs "causal set(s)") UND ("spin structure", tetrad, vierbein, "quantum walk(s)", Clifford, "vector field", "gauge field", electromagnetic), neueste zuerst, 40 | Wenige Treffer; in 24 Monaten hoechstens Vektor- bzw. Eichfeld-Vorschlaege, keine Spinor- oder Rahmen-Bauweise, kein Quantenlauf auf Kausalmengen | Eingetroffen. totalResults 4, alle Sverdlov (2008 x2, 2009 mit Bombelli, 2018 "Electromagnetic Lagrangian on a causal set that resides on edges rather than points"). Keiner ab 2024 | nein |
| A7 | 09:12:20-09:14:41 | arXiv-API: ti:checkerboard, neueste zuerst, 40 | Foster/Jacobson (2016/17) "Spin on a 4D Feynman checkerboard" vorhanden [L?]; sonst 1+1 (Skopenkov/Ustinov u. a.); kein 3+1-Schachbrett auf Kausalmengen | **Fehlgriff der Abfrage:** totalResults 244, die neuesten 40 (2024-04 bis 2026-09) sind fachfremd (Festkoerper, Bildverarbeitung, Kopulas). Kein Feynman-Schachbrett darunter. Prueft nichts | Methode (Abfrage zu breit) |
| A8 | 09:14:41-09:16 | arXiv-API: (ti:checkerboard ODER ti:checkers) UND abs:Feynman, neueste zuerst, 30 | Foster/Jacobson "Spin on a 4D Feynman checkerboard" (2016/17) erscheint; 4D-Schachbrett mit Spin nur auf festem Gitter bzw. mit Zusatzannahmen; keine Kausalmengen-Fassung in 24 Monaten | totalResults 10: Skopenkov/Ustinov-Reihe "Feynman checkers" (2020-2024, 1+1, auch "lattice quantum field theory with real time"), Earle 2010, Hanna 2006, Smith 1995 ("HyperDiamond", 4D, Phaenomenologie-Modell). **Foster/Jacobson nicht darunter.** In 24 Monaten nur Ozhegov/Skopenkov/Ustinov 2407.03258 (1+1) | **ja (V5):** mein Gedaechtnistitel nicht gefunden; moegliche Luecke: Abfrage verlangt "Feynman" im Abstract -> A9 |
| A9 | 09:16-09:19 (vor date 09:19:31) | arXiv-API: (ti:checkerboard UND au:Jacobson) ODER (abs:causet UND (fermion(s), spinor(s), Dirac)), neueste zuerst, 30 | Foster/Jacobson erscheint (Spin auf 4D-Gitter-Schachbrett); die causet-Abfrage bringt hoechstens Noldus erneut, keine neue 3+1-Bauweise | Eingetroffen. totalResults 4: **Foster/Jacobson 1610.01142 (2016) "Spin on a 4D Feynman Checkerboard"**, Gudder 1507.01281 und 1403.5338, Noldus 1305.0443. Gudder-Abstract jetzt vollstaendig: "covariant causal set (c-causet)", Wachstumsmodell, "the structure of a four-dimensional discrete manifold emerges", Dirac-Operator auf dieser Struktur (Notiz A9) | nein (V5 aufgeloest: Titel stimmt, Abfrage A8 war zu eng) |
| A10 | 09:19:31-09:19:54 | arXiv 1610.01142 (Foster/Jacobson 2016), PDF lokal, pdftotext: Abstract pruefen, grep causal set/random/lattice/isotrop/doubl | Kausalmengen hoechstens als Ausblick; Gitter fest; Isotropie nur im Kontinuumsgrenzfall; nichts zu Zufallsnetzen; keine Verdopplung, weil der Schritt nur vorwaerts laeuft bzw. nicht unitaer ist | Eingetroffen, mit einem Zusatz, der mehr traegt (V6). **Tetraedrische Nullschritte** (n_i an den Tetraederecken), Schrittgeschwindigkeit 3c. Keine Verdopplung: "the lack of a local action is our proposed explanation". Nicht unitaer: Norm halbiert sich je Schritt. Verweis auf [11]: unitaere BCC-Regel mit Weyl-Grenzfall ("unitarity and locality were shown there to imply the Weyl equation"). Fuer die Dirac-Masse **BCC**: Gegen-Chiralitaet springt in die Gegenrichtung. Kausalmengen: kein Treffer (Notiz A10) | **ja (V6)** |
| A11 | 09:20-09:21 | arXiv-API: abs "causal set(s)", neueste zuerst, 60, nur Titel (Gegensweep: entgehen mir Arbeiten ohne meine Stichworte?) | Keine Arbeit mit Spin, Spinor oder Fermion im Titel ausser Jones/Yazdi; Themen: SJ-Zustand, Verschraenkung, Dynamik, Phaenomenologie, d'Alembert-Operatoren | Eingetroffen. totalResults 403; die Phrasensuche greift lose (viele ML-Arbeiten zu "causal"). Kausalmengen-Physik 2025-04 bis 2026-09, etwa 22 Titel: Propagatoren 1+1 (Hinrichsen, Kastrati x2), Spektraldichte (Jones), Entropie (Jones/Yazdi), Kruemmung (Barton), Einbettung (Madsen "On the Uniqueness of Embeddings of Causal Sets"), Rekonstruktion (Hu, Braun x2), Dynamik (Zalel, Srivastava, Gutzeit, Ferguson), Eichhorn x2, Boguna, Adamson, Surya, Bevilacqua, Teruel, George. **Kein Titel zu Spin, Spinor oder Fermion** | nein |
| A12 | 09:21-09:22 | arXiv-API: abs "random lattice" UND (fermion(s), doubling, Dirac, Weyl), neueste zuerst, 30 (fuer L4 der Rechenkarte) | Wenige Treffer, Kern in den 1980ern (Christ/Friedberg/Lee, nicht auf arXiv). Aussage, dass Zufallsgitter die Verdopplung nicht einfach beseitigt bzw. Doppler als Stoermoden zurueckkehren [L?] | Eingetroffen, aber gespalten: Griffin/Kieu 1992-93 (Doppler "revived" mit Eichfeld), Kieu/Markham/Paranavitane 1994 (je nach Zufallsgitter-Art), Cohen 2006 (spontane chirale Brechung schon frei), Hatsugai/Wen/Kohmoto 1996 (2D, E = 0 ohne Verdopplung). Woertlich in A13 | teils (V7: Regimespaltung statt einer Aussage) |
| A13 | 09:22-09:23 | arXiv-API id_list hep-lat/9211022, hep-lat/9412048, hep-lat/0602021, Abstracts woertlich | wie A12 | Eingetroffen, Wortlaut in Notiz A13 | nein |
| L2 | 09:05-09:06 (date 09:05:52 waehrenddessen, vor A1) | lokal: Scout-Cache (OAI-PMH, research-scout-claude-20260913/http-cache), Datensaetze mit "causal set" und spinor/fermion/Dirac | 0 bis 2 Treffer, keiner mit 3+1-Spinoren | 1 Treffer: Jones/Yazdi, arXiv:2602.16782 (Fassung 2026-09-29), Spektralentropie bosonisch **und fermionisch**, Kausalmengen-Beispiel nur 1+1. **Fenster des Caches nur 2026-08-31 bis 2026-10-02**, also kein 24-Monats-Test | nein |

## 3. Notizen je Abruf

### L1 Surya 2019 (lokal, [S], Zeilennummern der Projektdatei)

- Z. 7928-7931, Abschn. 5 "Matter on a continuum-like causal set", woertlich: "The simplest matter field is the free
  scalar field on a causal set in Md . As we noted in the previous Section, this is the only class of matter fields
  that we know how to study, since at present no well defined representation of non-trivial tensorial fields on causal
  sets is known."
- Z. 7314-7322, woertlich: "unlike a regular lattice, a simple construction of a locally defined tangent space from the
  set of links or next to nearest neighbours to e is not possible, since the valency of the graph is infinite. This
  means in particular that derivative operators cannot also be simply defined. [...] the best way forward is to look
  for scalar quantities, rather than more general tensorial ones".
- Z. 1525-1600 (Abschn. Lorentz-Invarianz):
  - Euklidischer Fall: Eine Richtung je Element ist konsistent waehlbar, weil S^1 kompakt ist. Woertlich: "it is
    possible to assign a consistent direction for a given realisation [...] and hence break Euclidean symmetry".
    Das Ensemble bleibt im Mittel invariant ("Christ et al (1982) [...] the random discretisation preserves the
    Euclidean group").
  - Lorentz-Fall: "Theorem 2 In dimensions n > 1 there exists no equivariant measurable map D : C(Md , rho_c) -> H".
    Grund: Die Hyperbel ist nicht kompakt (Bombelli et al 2009).
- Schlussabschnitt (Z. 9242-9250): Als die zwei wichtigsten offenen Fragen nennt Surya Lambda-Modelle und eine
  Quantendynamik, nicht Fermionen.
- Bedeutung [ES]:
  - E1 ist in der Sache gestuetzt, aber anders als erwartet: Surya nennt Fermionen nicht als offen. Sie sagt, dass
    schon Vektor- und Tensorfelder fehlen.
  - Das Hindernis liegt also vor dem Spin: beim Tangentialraum bzw. bei Richtungen. Das deckt sich mit W2.
  - Der Moderator "kompakt gegen nicht kompakt" steht als Satz in der Quelle (Theorem 2 gegen den euklidischen Fall).

### A2 Sverdlov 2008, arXiv:0808.2956v1 [S, pdftotext]

- Abstract: "The goal of this paper is to define fermionic fields on causal set. This is done by the use of holonomies to
  define vierbines, and then defining spinor fields by taking advantage of the leftover degrees of freedom of holonomies
  plus additional scalar fields. Grassmann nature is being enforced by allowing measure to take both positive and
  negative values [...]".
- Einleitung: "vector fields are redefined in terms of holonomies"; vierbeine werden durch "a set of four vector fields
  that are no longer assumed to be orthogonal to each other" ersetzt.
- Diskussion (Abschn. 4): "fermions can be interpreted as local frame defined by non-orthonormal vector fields";
  "a vierbine is precisely what tells us what direction is the one with respect to which spin might be up or down".
- Zahlen- oder Simulationsbefunde: keine gefunden (grep numeric/simulat nur ein Satz ueber die Wichtigkeit von
  Numerik, Z. 1320).
- [ES]: Das ist genau E4 (Rahmen je Element als Zusatzfeld). Der Rahmen kommt nicht aus der Ordnung, sondern aus
  eingesetzten Holonomien.

### A3 Noldus 2013, arXiv:1305.0443v3 [S, pdftotext]

- Einleitung: "in case of Fermi fields on causal sets; this problem has defied anybody up till now. [...] the concepts
  of vierbein and Clifford bundle are mandatory for the continuum description. Given the complete absence of such
  concepts for causal set theory, the best one may hope for is the existence of an object which has no counterpart in
  the continuum".
- S. 2: "One notices that not enough information is present in the causal set itself to find a unique solution in this
  way; the problem being that too many expressions can fit these equations and that the dimension is put in by hand."
- Dann: Kausalmenge "emergent from a spinor perspective": K in Cl_R(p,q) ⊗ R^(n×n) mit Traeger auf Diagonale und
  Links, "strongly generates I if and only if KK* + K*K = 2 1 ⊗ I".
- Rechnung nur fuer die 2-Element-Kausalmenge und den "Diamanten" (letzter Abschnitt), in 2-dim Darstellung.

### L3 Johnston 2010, Doktorarbeit, Kap. 6 [S, pdftotext, selbst gelesen]

- 6.2: "One approach to this has been considered by Sverdlov (2008c). [...] The resulting expressions, however, are
  very complicated and it is not clear in what way the Lorentz-transformation properties of a spinor are included."
  Und: "we do not necessarily want a model for spinors on a causal set, but rather a model for spin-half particles.
  [...] This is clearly a formidable task."
- Fussnote 2: "since spinors cannot be defined for an arbitrary Lorentzian manifold, it may be over-optimistic to try to
  define them for an arbitrary causal set."
- 6.3: "Generalising the model to 3+1 dimensions was attempted by Feynman but not published (Schweber, 1986) and has
  been attempted by subsequent authors (including Jacobson and Schulman (1984); Jacobson (1984) and others)."
- 6.4: Gleichung (6.19) R_m^2 = -rho K_R ⊗ I; "The size of the identity matrix I corresponds to the size of the
  'spin-space' [...] (e.g. for the 4-spinor theory in d = 4, I would be a 4 × 4 matrix). Ideally, we would like the
  size of this spin-space to be determined by the act of taking the square root of KR, i.e. we'd like it to only work
  for I of a particular size." Schluss: "The square roots of a matrix (if they exist) are in general not unique. [...]
  This remains a task for future work."

### Schreibtisch S1 (09:12, nach L3 und A3) [ES, eigene Algebra, nicht gegengelesen]

- Frage: Erzwingt Johnstons Wurzelbedingung eine Spinraumgroesse s?
- Ansatz: R_0 retardiert (Traeger auf Diagonale und Relationen), Bloecke: D_x auf der Diagonale (s x s), M_xy
  auf Relationen.
- Diagonale: (R_0^2)_xx = D_x^2, und (-rho K_R)_xx = 0. Also ist D_x nilpotent.
- Link (x,y): Zwischen x und y liegt kein Element. Deshalb gilt (R_0^2)_xy = D_x M_xy + M_xy D_y. Das soll
  -rho K_xy I_s ungleich 0 sein.
- **Folgerung 1:** D_x ist ungleich 0 und nilpotent. Daraus folgt s >= 2. Ein skalarer Wurzelansatz (s = 1) ist auf
  jeder Kausalmenge unmoeglich, sobald K auf Links nicht verschwindet.
- **Folgerung 2:** s = 2 geht trivial: R_0 = 1 ⊗ E12 + c L ⊗ E21 mit c = -rho a.
  - Probe: E12^2 = E21^2 = 0, E12 E21 + E21 E12 = I_2. Also R_0^2 = c L ⊗ I_2 = -rho Phi ⊗ I_2 (masselos).
  - Das ist die "Reduktion auf erste Ordnung" wie [[0,1],[box,0]] im Kontinuum, kein Spinor.
  - **Die Wurzelbedingung erzwingt also eine Verdopplung, aber keinen Spin.** Das passt zu Noldus ("too many
    expressions can fit").
- **Folgerung 3 (3+1):** Ein spinorielles D_x waere ein nilpotentes 2x2, etwa sigma.m mit komplexem Nullvektor m. Das
  ist eine Flagge je Element.
  - Die Bahn der Nilpotenten unter SL(2,C) ist nicht kompakt.
  - Eine aequivariante Wahl aus der Streuung waere ein Gegenstueck zu Theorem 2 (BHS) und damit unmoeglich [ES, nicht
    bewiesen].
  - In 1+1 gibt es nur zwei Lichtrichtungen (R, L), beide unter Boosts fest. Deshalb geht SCHACHBRETT-KAUSAL-1 ohne
    Rahmen.
  - Unterscheidungspunkt nach Dimension: 1+1 (endlich viele, feste Nullrichtungen) gegen 2+1 und 3+1 (S^1 bzw. S^2
    unter SL(2,R) bzw. SL(2,C), ohne invariantes Wahrscheinlichkeitsmass) [ES].

### A5 Nomaan X 2023, arXiv:2306.04800v1 [S, pdftotext]

- Abschnitt "Fermions": "To discuss QFT for fermions, we need a way to first obtain the retarted Green function
  analogue on the causal set and then use an appropriate PJ operator in order to get a unique set of modes. The latter
  issue is resolved easily by replacing the bosonic PJ operator [...] with a fermionic version based on an
  anti-commutator". Dann Johnstons zwei Vorschlaege. Zum Schluss: "However, the square root of a matrix (if it exists)
  is not unique in general and therefore we may need further constraints."
- Zu Feldlagrangedichten (Sverdlov-Linie, Ref. [30]): "amenable to gauge fields and spinors, it is a top-down approach
  [...] somewhat complicated".
- Schluss: "we would like to apply this construction to more realistic theories - interacting theories and theories
  involving fermions."

### A9/A10 Foster/Jacobson 2016, arXiv:1610.01142v1 [S, pdftotext]

- Abstract woertlich wie im Abrufprotokoll (Weyl auf "time-diagonal, hypercubic spacetime lattice with null faces";
  Rechtshaender: Projektor auf den Spin in Schrittrichtung; Pfadamplitude i^(±T) 3^(-B/2) 2^(-N); "Fermion doubling
  does not occur").
- pdftotext-Zeile 107: "The four spatial unit vectors n_i point to the vertices of a tetrahedron". Schrittgeschwindigkeit 3c
  (Courant marginal).
- Verdopplung: "the lack of a local action is our proposed explanation for how the fermion doubling is evaded".
- Schluss: "Although the underlying lattice is not Lorentz invariant, that symmetry is recovered by the propagator in
  the continuum limit." Dirac-Masse: "we enlarged the lattice to a bcc one, so that opposite chirality spinors with the
  same spin could step in opposite directions." "Lorentzian lattice schemes ensuring 4D Lorentz symmetry in the
  continuum limit of an interacting theory are not known."
- Nicht unitaer: "the discrete propagator is not unitarity [sic]". Verweis [11]: "one can write a unitary discrete
  evolution rule on a body centered cubic lattice whose continuum limit is the Weyl equation. (Interestingly, unitarity
  and locality were shown there to imply the Weyl equation.)"
- [ES] Bezug zu unseren Rechnungen:
  - Der FJ-Schritt (1/2) Sum_a e^(ik.h_a) P(n_a) ist die Einschraenkung von QCA-DIAMANT-4 Teil B (Muenze mal
    Tetraederverschiebung, 4 Zustaende) auf den Spinorteil 2. Dort gilt <a|P_2|a> = 1/2 und
    |<a|P_2|b>|^2 = 1/12 = (1/4)(1/3), passend zu FJs 3^(-1/2) je Knick.
  - Unser v = 1/3 ist FJs "step speed 3c".
  - Unsere 4-Zustands-Regel waere damit eine unitaere Erweiterung des FJ-Schachbretts. Die Algebra ist eigene und
    nicht gegengelesen.

### A13 Zufallsgitter-Fermionen [S Abstract, arXiv-API]

- Griffin/Kieu 1992 (hep-lat/9211022): "the doublers suppressed in the free field case are revived for random lattices
  in the continuum limit unless gauge interactions are implemented in a non--invariant way" (2D, abelsches
  Hintergrundfeld).
- Kieu/Markham/Paranavitane 1994 (hep-lat/9412048): "While the fermion doubling is confirmed on one kind of lattices,
  there is positive evidence that it may be absent for the other [...] arbitrary randomness by itself is shown to be not
  a sufficient condition to remove the fermion doublers."
- Cohen 2006 (hep-lat/0602021): "the random lattice does so by spontaneous chiral symmetry breaking even in the free
  theory" (4D, gequenchte QCD).
- Hatsugai/Wen/Kohmoto 1996 (cond-mat/9603169): Titel "Random Lattice Fermions at E=0 without Doubling". Nur Titel,
  Auszug durch das Werkzeug.

### L2 Scout-Cache (lokal)

- Jones/Yazdi 2026, arXiv:2602.16782, "Spectral Spacetime Entropy for Quasifree Theories" [S Abstract, lokal]:
  "for both bosonic and fermionic field theories"; "a calculation in a causal set in 1+1 dimensions".
  - Fermionisch ist dort nur der Formalismus (quasifreie Zustaende). Ob das Kausalmengen-Beispiel fermionisch ist,
    sagt der Abstract nicht.
- Selbstanzeige: Beim Zaehlen habe ich um 09:05 versehentlich eine Dateiliste nach /tmp/claude-1000/scout-cs-list.txt
  geschrieben (6,5 KB, nur Cache-Dateinamen). Um 09:05:52 geloescht (ls bestaetigt). Verstoss gegen die
  Scratchpad-Regel.

## 4. Erwartungsverstoesse (laufend, Reihenfolge nach Gewicht wie im DOSSIER)

- V3 (S1, aus L3 + A3): Die Wurzel erzwingt s >= 2 (nilpotentes Kontaktglied), aber keinen Spin; s = 2 trivial.
- V6 (A10): Foster/Jacobson 2016, tetraedrisches 3+1-Schachbrett mit Spin, ohne Doppler, nicht unitaer, BCC fuer die
  Masse. Nach meiner Algebra Einschraenkung von QCA-DIAMANT-4 Teil B.
- V1 (L1): Surya nennt Fermionen nicht; das Hindernis liegt frueher (Tensorfelder, Tangentialraum).
- V2 (A1): Vorschlaege aelter als erwartet (Sverdlov 2008, Noldus 2013/15, Gudder 2015).
- V7 (A12/A13): Verdopplung auf Zufallsgittern regimeabhaengig.
- V4 (L3): Johnston 6.4 allgemein-dimensional.
- V5 (A8, Methode): zu enge Abfrage haette FJ verneint.
- Korrigierte Erwartungen (protokolliert):
  - E1: "Surya nennt es als offen" -> "Surya nennt Tensorfelder als nicht wohldefiniert; Fermionen offen laut Nomaan X".
  - E3: "neuere" -> "aeltere Vorschlaege, nach 2015 nur auf festem Gitter".

## 5. Offene Rueckfragen (wandern mit)

- R1: ~~Ist die Projektsuche der Leitung vollstaendig?~~ Erledigt im Gegensweep G1: fuer Kausalmengen-Fermionen ja; aber
  RUNDE-22/geometrie-stand/ERGEBNIS.md Z. 61/790 kannte schon Kaehler-Dirac auf zufaelliger Geometrie [L?].
- R2 (offen, an die Leitung): FJ Gl. (11) gegen QCA-DIAMANT-4 Teil B pruefen (unitaere Erweiterung?).
- R3 (offen): Christ/Friedberg/Lee 1982 und Griffin/Kieu am Volltext lesen, bevor SPIN-ZUFALLSNETZ-1 startet (L4).
- R4 (offen): Gilt das BHS-Muster fuer Null-Flaggen streng (S1 Folgerung 3)? Frischer Leser fuer S1 und D2/D3.

## 6. Gegensweep (Regel 4)

- G1 geprueft: Projekt-Vorarbeit (siehe R1).
- G2 geprueft: andere Schreibweisen (causet, causets: A9) und Titelliste der 60 neuesten "causal set"-Abstracts (A11):
  nichts zu Spin. Ungeprueft: "partial order", "poset", "discrete spacetime".
- G3 teils geprueft: Spin 1/2 ohne Spinorfeld (Kaehler-Dirac, nur Abstract). Kaehler-Dirac auf Kausalmengen: keine
  Abfrage, [H].
- G4 geprueft: FJ-Titel aus dem Gedaechtnis richtig; Inhalt traegt mehr (V6).
- G5 nicht bewiesen: BHS fuer Null-Flaggen (Argument: kein invariantes Wahrscheinlichkeitsmass auf S^2 unter
  SL(2,C)) [ES].
- G6 geprueft: Die wiederverwendete Johnston-PDF ist die Doktorarbeit (pdfinfo 172 S., Titel).

## 7. Zaehler

- WebFetch: 13 von 15 (A1 bis A13). Websuche: keine. Lokal kein python und kein perl.
- Selbstanzeige awk: Um 09:28 rief ich in einer Befehlszeile versehentlich "awk 2>/dev/null; true" ohne Programm auf.
  Das startete awk ohne Programm; die Ausgabe war unterdrueckt, Wirkung keine. Trotzdem ein Verstoss gegen
  "lokal kein awk".
- Selbstanzeige Scratchpad: siehe Notiz L2 (09:05, geloescht 09:05:52).
- Dossier geschrieben ab 09:24:59 (date).
