# ARBEITSFELD CSP-STRING-L (feldforscher)

- Beginn (date): 2026-10-04 11:06:12 CEST. Zeitbox 45 min, also Ende spaetestens 11:51.
- Dieser Abschnitt geschrieben ab 2026-10-04 11:08:19 CEST (date), vor jedem Abruf.
- Kennzeichen: [S] an der Quelle selbst gelesen (mit Seite/Zeile), [Sa] nur Abstract selbst gelesen, [L] Gedaechtnis,
  [L?] unsicher, [ES] eigener Schluss, [H] Hypothese. Fundstellen nur aus [S]/[Sa].
- Abrufzaehler: 0 von 10. Lokale Projektdateien zaehlen nicht als Abruf.

## 0. Gelesen vor dem ersten Abruf (nur intern)

- KARTE.md ganz (E1-E4 der Leitung).
- RUNDE-11/cemz-mess/CEMZ-MESS.md ganz. Fuer diese Karte tragend:
  - Kontinuierlicher Spin dort nur eine Zeile: "nur Empfindlichkeit, keine Schranke (24.09.-Bericht, Kundu/Schuster/Toro [Pa])".
  - Regime I/I'/II/III; V1: CEMZ-Zeitmaschine (Anh. G) nur D > 4; Fn. 23 "infinite tower ... clear in D = 4".
- art-grenzen-20260921/WARUM-SPIN-2.md: Glied 7 (Z. 248-286), Glied 10 (Z. 396-447), Rangliste (Z. 450-483),
  Nachtrag 24.09. (Z. 534-541, CSP als "vierter Ausweg", Z. 538), Berichtigungen 30.09. (Z. 611-773; Z. 764: CSP-Route
  "hier nicht neu bewertet"), Nachtrag 01.10. (Z. 813-925: CEMZ und Caron-Huot u. a. in D = 4 nur bedingt).
- literatur-20260924/GLIEDER-7-10-MESSBAR-20260924.md per grep (Z. 146-172, 301-335, 366-374, 521-523):
  CSP-Stand im Projekt = Schuster/Toro 2013 [S, Suchebene], Kundu/Schuster/Toro 2503.03817 [Pa] (linearisiert,
  spinlose Materie, O(rho_g/omega), Empfindlichkeit 1e-14 eV LVK / 1e-24 eV PTA, keine Schranke), Reilly/Schuster/Toro
  2505.01500 [Pa]. **Nicht im Projekt:** irgendetwas zu CSP in der Stringtheorie (grep "string" in diesem Zusammenhang leer).
- RUNDE-38.md Z. 219 (Scout-Tageslauf: S6 neu), RUNDE-39.md Z. 30-36 und 432 (Start dieser Karte).
- RUNDE-23/bildung-3d/PLAN.md Z. 111: **Falschtreffer** des Projekt-greps ("scipy CubicSpline" enthaelt "cSp"). Kein
  CSP-Inhalt. -> Gegensweep-Notiz G0.
- Pool: S6 CSP-STRING-L hat als Elter "S3 STRING-EINDEUTIG-L" (arXiv 2610.02124, Eindeutigkeit von String-Amplituden),
  noch "idee". Projektnetz: HAGEDORN-1/2 (Q-Ball-Ringe als Strings, Glied 7), TENSOR-EIS-N (N-Typ zieht wie -1/(8 pi r) an,
  nur Helizitaet 2 mit positiver Energie auf der Zwangsflaeche).

## 1. Eigene Vorab-Erwartungen (zusaetzlich zu E1-E4 der Karte; 11:08, vor jedem Abruf)

Grundhypothese [H0] (Regel 1): "Strings ohne CSP" und "CSP aus Strings" sind zwei Regime, nicht ein Widerspruch.
Vermuteter Moderator: **Stringspannung** (endliche Spannung alpha' > 0 gegen tensionsloser Grenzfall alpha' -> unendlich)
und **Spektrumsdefinition** (On-shell-Fock-Raum mit Virasoro-/GSO-Bedingungen gegen gelockerte Bedingungen).
Gedaechtnis [L?]: Font/Quevedo/Theisen 2013 (arXiv:1302.4771) "keine CSP in perturbativen Strings"; Mourad 2004/05
und Savvidy 2003: CSP-artige Zustaende in tensionslosen Strings. Das ist ungeprueft.

- E5 (2610.00745 selbst): Methode Lichtkegel- oder kovariante Quantisierung; Ergebnis "kein masseloser Zustand mit
  nichtverschwindendem Casimir W^2 = -rho^2"; Einschraenkung "perturbativ, flacher Hintergrund, endliche Spannung"; die
  Arbeit zitiert Font/Quevedo/Theisen 2013 als Vorlaeufer und erweitert auf Superstrings bzw. alle konsistenten
  Hintergruende. Wenn die Arbeit **nicht** FQT zitiert oder FQT widerspricht: Verstoss.
- E6 (Vorlaeufer): Das Ergebnis "perturbative Strings enthalten keine CSP" ist **nicht neu** (FQT 2013); neu ist hoechstens
  Superstring/GSO oder Beweisstrenge.
- E7 (Gravitation und CSP): Es gibt keine publizierte, nichtlinear konsistente Kopplung eines CSP-Gravitons; nur
  linearisiert (Kundu/Schuster/Toro). Kubische Vertices CSP-CSP-Graviton sind offen oder durch No-go eingeschraenkt.
- E8 (CEMZ-Text, lokal): Im CEMZ-Volltext kommt "continuous spin" nicht vor (E3 der Karte).
- E9 (Projektbezug): Ein CSP-Graviton loest das CEMZ-Problem nicht automatisch: CEMZ verlangt eine Aenderung der
  **Dreieramplitude des Helizitaet-2-Gravitons**; ob ein CSP-Austausch (unendlich viele Helizitaeten, ein Teilchen) die
  Zeitvoreilung heilen kann, ist nicht untersucht. [H]

## 2. Lokale Vorpruefungen (kein Abruf; Eintrag 11:09:36, date)

- **L1 CEMZ-Volltext lokal** (art-grenzen-20260921/cemz-gegenpruefung-codex-quellen/1407.5597v1.txt, Codex-Kopie).
  Erwartung E8: "continuous spin" kommt nicht vor. Befund: **bestaetigt.** "continuous" genau einmal, Z. 358, im
  Koordinatensinn ("continuous in the vnew coordinates"); kein "infinite spin", kein "Wigner". [S, grep]
  -> E3 der Karte im Teil "CSP werden dort nicht behandelt" fuer v1 bestaetigt (spaetere Fassungen nicht geprueft).
- **L2 Scout-Datensatz lokal** (research-scout-claude-20260913/runs/20261004T043016Z-daily/candidates.json, Abstract aus
  der arXiv-OAI-Ernte). Erwartung E5/E6: Vorlaeufer Font/Quevedo/Theisen 2013. Befund: **bestaetigt, mit Namen:**
  - Titel "Absence of Continuous Spin Particles in Superstring Theory", Arwa Alabbasi, **Fernando Quevedo**
    (Mitautor von 1302.4771), erstellt 2026-09-30, aktualisiert 2026-10-02, hep-th/hep-ph, ohne Zeitschrift.
  - Abstract woertlich: "In this note we show that these particles are absent in perturbative super-string theories,
    generalising a result in arXiv:1302.4771 to the supersymmetric case. This stands out as a general low-energy
    prediction of all perturbative superstring constructions." [Sa, lokale Scout-Kopie]
  - Folge: E1 im Abstract bestaetigt; E6 bestaetigt (Kern nicht neu, neu ist der supersymmetrische Fall).
  - Neu fuer mich: die Autoren selbst nennen das eine **Niedrigenergie-Vorhersage** aller perturbativen
    Superstring-Konstruktionen. Das macht aus "getrennt" (E4) moeglicherweise "gegenseitig ausschliessend" -> pruefen.

## 3. Abrufprotokoll (Erwartung vor Abruf -> Befund)

- **Vorab A1 (11:09:36):** Volltext 2610.00745. Erwartung: (i) Argument wie FQT 2013 = endliche Entartung je
  Massenstufe -> nur endlichdimensionale Darstellungen der kleinen Gruppe ISO(D-2) -> Translationen wirken trivial ->
  nur Helizitaet; (ii) Superstring-Zusatz: GSO, Ramond-Sektor, Fermionen-CSP (Brink/Khan/Ramond/Xiong) ausgeschlossen;
  (iii) ausdrueckliche Grenzen: perturbativ, endliche Spannung, kompakte innere CFT; tensionsloser Grenzfall
  (Mourad/Savvidy) als bekannte Ausnahme erwaehnt; (iv) kein Wort zu CEMZ oder Gravitationskausalitaet.
- **A1 (Abruf 1/10, 11:09:53) arXiv:2610.00745v1, quellen/2610.00745.pdf (sha256
  95166197ca67b243e561932221b5d4b6ea7e3c185246ef6f548ad9dd2e6a5250), pdftotext quellen/2610.00745.txt (1059 Z.), ganz
  gelesen. Eintrag 11:11:44. [S]** Ausgang je Teil:
  - (i) **VERLETZT (Methode):** Kein Entartungsargument. Explizite Moden-Rechnung im Lichtkegel-NSR-Formalismus, d = 10:
    T^i = T_B^i + T_F^i annihiliert den masselosen NS-Vektor psi^j_{-1/2}|0> (Abschn. 4, Gl. 24-33ff., S. 6-8) und den
    Ramond-Grundzustand |A>_R (Abschn. 5, Gl. 43-47, S. 9-10); "Therefore Pi^i |A>_R = 0 ... the effective little group is
    again SO(8)" (S. 10). Kriterium (S. 4, Z. 195): CSP-Zustaende haben sum_i (Pi^i)^2 != 0; im Bezugssystem p^i = 0
    reicht T^i|psi> = 0 (S. 4, ~~Z. 213-215~~ Z. 220-221, Zeilen nachgeprueft 11:13).
  - (ii) **teils:** Erweiterung auf geschlossene Strings IIA/IIB (T_closed = T_L x 1 + 1 x T_R) und heterotisch
    E8 x E8, Spin(32)/Z2 inkl. innerer Stromalgebra J^a_{-1} (Abschn. 6, Gl. 48-56, S. 11-12). **GSO kommt im Text nicht
    vor** (grep); Fermion-CSP-Supermultipletts (Brink/Khan/Ramond/Xiong) nicht als eigener Fall behandelt; [20] wird nur
    fuer die Zerlegung von Pi^i (Gl. 6) zitiert.
  - (iii) **bestaetigt:** S. 3 (Z. 122-125): "CSPs are not present in all formulations of string theory so far (with the
    possible exception of tension-less strings). Therefore, modulo unknown potential non-perturbative effects, superstring
    theory universally predicts the absence of CSPs." S. 13 (Z. 939-945): "intrinsically perturbative ... We may
    speculate, however, that a fully non-perturbative formulation of M-theory could require continuous-spin degrees of
    freedom as well." Tensionslose Strings **ohne Zitat** (kein Mourad, kein Savvidy im Literaturverzeichnis).
  - (iv) **bestaetigt:** kein "causal", kein Camanho/Maldacena/CEMZ, kein "three-point" (grep, Z. 1-1059). Der einzige
    Turm-Bezug: Fn. 1, S. 3 (Z. 156-158): "In the massive case, the existence of an infinite tower of massive modes is
    another implication from string theory that fits with the efforts to make sense of UV completion of massive higher
    spin particles in which an infinite tower seems to be required for consistency (see for instance [21, 22])" mit
    [21] Duff/Pope/Stelle 1989, [22] Huang/Remmen 2022 (arXiv:2203.00696).
  - **Analysezyklus Z-1 (Verstoesse, die ich nicht erwartet hatte):**
    - **V-a (gross, gegen E4):** Die Autoren formulieren die Abwesenheit als **Falsifikationsbedingung**: "Any positive
      experimental signal of CSPs would directly falsify perturbative string theory" (S. 3, ~~Z. 129-130~~ Z. 128-129); "should particles
      carrying continuous spin be detected experimentally we would be able to rule out perturbative superstring
      constructions" (S. 3, ~~Z. 152-155~~ Z. 152-154). -> CSP-Zweig und String-Zweig sind laut Arbeit nicht bloss "getrennt", sondern im
      perturbativen Regime **gegenseitig ausschliessend**; die Verbindung ist eine Ausschlusskante, also eine Kopplung.
    - **V-b (mittel, gegen E4):** Dieselbe Oszillatoralgebra baut den masselosen Sektor (rho = 0) und den unendlichen
      massiven Turm: "The same creation and annihilation operators that build the massless states also generate the entire
      tower of massive string excitations" (S. 12, Z. 925-928). Im Stringbild sind "massiver Turm" (Glied 7, massive
      Fassung) und "kein CSP" (Glied 7, Wortlaut masselos) zwei Seiten einer Struktur.
    - **V-c (klein, innerer Widerspruch der Arbeit):** S. 4 (Z. 228-233): beide Beitraege verschwinden "separately" bzw.
      "independently"; S. 12 (Z. 928-929): "the explicit cancellation between bosonic and fermionic oscillator
      contributions ... is what fixes T^i = 0". Nach den eigenen Abschn. 4-5 ist es kein Aufheben, sondern getrenntes
      Verschwinden. [ES] Das schwaecht die Lesart "distinctly stringy property" (S. 12, ~~Z. 924~~ Z. 925).
    - **V-d (klein, Kalibrierung):** S. 12 (Z. 921-923): Strings erklaeren, "why such states are absent in nature, an
      experimental result that has no other fundamental explanation" (~~Z. 921-923~~ Z. 921-924). Eine Messgrenze wird nicht zitiert; das Projekt kennt
      fuer rho_g nur Empfindlichkeiten (24.09.-Bericht). -> "Abwesenheit in der Natur" ist dort Nichtnachweis, kein Befund.
    - **V-e (klein, Projektstand nachziehen):** Kundu/Schuster/Toro ist erschienen: Phys. Rev. D 113 (2026) 076017 (Ref.
      [10], S. 14); Reilly/Schuster/Toro PRD 113 (2026) 015028 ([11]); neu fuer das Projekt: Kundu/Russo/Schuster/Toro
      JHEP 11 (2025) 125 ([12]); Metsaev JHEP 03 (2026) 061 "on-shell cubic vertices for continuous-spin fields and
      integer-spin fields" ([16], arXiv:2510.05011); Basile/Bekaert/Figueroa/Skvortsov arXiv:2606.28245 ([18]).
    - **V-f (Selbstanzeige-relevant):** Danksagung S. 13 (Z. 953-955): "We counted with the assistance of Claude for
      checking our computations". Meine Lesung ist daher nicht voll hausfremd zur Pruefung der Autoren.
    - **[ES] Mechanismus (Regel 6):** Die Autoren selbst verorten den Kern in "forbidding an infinite spectrum of massless
      particles" (S. 12, Z. 922). T^i vertauscht mit der Massenstufe; auf dem masselosen Niveau (bei fester Impulsrichtung
      endlich viele Zustaende, 8_v + 8_s) koennen vertauschende hermitesche T^i, die SO(8) ineinander dreht, nur den
      Eigenwert 0 haben. Dann folgt rho = 0 schon kinematisch (Weinbergs Argument fuer endlich viele Freiheitsgrade).
      Die Moden-Rechnung ist so gesehen eine Konsistenzpruefung. Nicht an einer Quelle gelesen -> FQT 2013 pruefen (A2).
  - Korrigierte Erwartung (protokolliert): Das Ergebnis ist eine **Endlichkeitsaussage ueber den masselosen Sektor
    perturbativer Strings mit Spannung**; die Ausnahme liegt dort, wo dieser Sektor unendlich wird (tensionsloser
    Grenzfall, unendlich viele masselose hoehere Spins).

- **Vorab A2-A4 (11:14, vor den Abrufen):**
  - A2 Font/Quevedo/Theisen 2013, arXiv:1302.4771 (PDF). E10: "simple observation", bosonischer String im
    Lichtkegel, T^i auf alpha^i_{-1}|0>; Grenzwert massiver Darstellungen (m -> 0, Spin -> unendlich) erwaehnt;
    Mourad/Savvidy (tensionslos) zitiert. Wenn FQT ein Endlichkeits-/Entartungsargument nutzt: stuetzt [ES] aus Z-1.
  - A3 arXiv-API id_list (ein Abruf, sechs Abstracts):
    - 2406.17017 (Bellazzini/De Angelis/Romano): E11: On-shell-Dreipunktamplituden fuer CSP; Kopplung an Gravitonen
      nur eingeschraenkt (Aequivalenzprinzip oder rho -> 0). [L?]
    - 2510.05011 (Metsaev 2026): E12: kubische Vertices CSP-CSP-ganzzahliger Spin existieren in bestimmten Faellen;
      keine Aussage zur nichtlinearen Vollstaendigkeit.
    - 2606.28245 (Basile/Bekaert/Figueroa/Skvortsov): E13: Formalismus, keine Gravitations-No-go-Aussage.
    - hep-th/0504118 (Mourad): E14: CSP entstehen aus einem tensionslosen bzw. abgewandelten String.
    - 1505.01759 (Longo/Morinelli/Rehren): E15: Teilchen unendlichen Spins nicht in beschraenkten Gebieten
      lokalisierbar, nur in raumartigen Kegeln ("string-localized").
    - 1302.1577 (Schuster/Toro): E16: Helizitaetskorrespondenz oberhalb rho; CSP-Graviton-Matrixelement umgeht
      Weinberg-Witten.
  - A4 arXiv-API-Suche abs:"continuous spin", nach Datum, 24 Monate (Regel 7). E17: 20-40 Treffer; keine nichtlineare
    CSP-Gravitation; keine Arbeit mit CSP in Strings endlicher Spannung; hoechstens 1-2 zu tensionslosen Strings.
- **A2 (Abruf 2/10, 11:13:18) Font/Quevedo/Theisen 2013, arXiv:1302.4771v1, quellen/1302.4771.pdf (sha256
  c74db148fcc11d8f0b3319b4ac6e91eef600e8db124653ced1f5897df53e4300), 8 S., ganz gelesen. [S]** E10 **bestaetigt, mit
  zwei Zusaetzen, die tragen:**
  - Kernargument ist ein **Multiplett-Argument**, nicht die Rechnung: "particles of different masses and spin are in the
    same multiplet ... It is then clear that if the massive representations do not carry a continuous label the massless
    states should not carry it either" (S. 2). Die Rechnung T^i|j> = 0 nennen sie selbst "a consistency check" (S. 5).
  - **Die Superstring-Erweiterung steht schon dort als Behauptung:** "In the compactified theory there are also
    contributions from the internal CFT but they will not change the argument and result. The same is true for the
    extension to the fermionic string." (S. 6). -> 2610.00745 liefert dazu die ausgeschriebene Rechnung, keinen neuen Satz.
  - Tensionslos: "it has been suggested that CSR's could be realised in the zero tension limit of string theory in which
    the infinite tower of massive states collapses to zero mass (see for instance [9])" mit [9] = Savvidy, IJMPA 19 (2004)
    3171, hep-th/0310085; "even if true it does not correspond to the standard string constructions" (S. 3).
  - Feldtheorie-Seite schon 2013 genannt: [7] Yngvason 1970; Mund/Schroer/Yngvason 2004 "String localized quantum fields
    from Wigner representations" (S. 3, Ref. S. 6); Swampland-Einordnung: "if there exist interacting field theories for
    these states, they should belong to the swampland" (S. 3). 2610.00745 sagt dagegen, das Ergebnis "bypasses the
    swampland programme" (S. 3). -> Rahmung verschoben, Inhalt gleich.
  - "if these states are detected experimentally, all string theory constructions known so far would be ruled out" (S. 2)
    -> die Falsifikationslesung (V-a) ist nicht neu, sie steht schon 2013 da.
- **A3 (Abruf 3/10, 11:13:23: leere Antwort ueber http, 0 Byte, sha256 e3b0c442...; Abruf 4/10, 11:13:30 ueber https)
  arXiv-API id_list, quellen/abs-batch-A3.xml (sha256 423032e106030aeb3b538ff771d5a6d55091dfeec9051dc24e025ac82b776068),
  6 Abstracts. [Sa]**
  - 1302.1577 Schuster/Toro: E16 **bestaetigt** (eine Zeile): Helizitaetskorrespondenz oberhalb rho; "a candidate
    CSP-graviton matrix element, which shows that the Weinberg-Witten theorem does not apply to CSPs"; "known long-range
    forces might be mediated by CSPs with very small rho".
  - 1505.01759 Longo/Morinelli/Rehren (CMP 345 (2016) 587): E15 **bestaetigt und schaerfer:** "local fields generating them
    from the vacuum state cannot exist"; "the subspace of states localized in any double cone is trivial"; "In an
    interacting theory, if the vacuum vector is cyclic for a double cone local algebra, then the theory does not contain
    infinite spin representations"; unter Bisognano-Wichmann; Gegenbeispiel ohne diese Eigenschaft "with continuous particle
    degeneracy". -> **Zweiter, stringfreier Weg zu "kein CSP": Lokalitaet.** (Regel 6, siehe Z-2)
  - hep-th/0504118 Mourad 2005: E14 **teils verletzt:** nicht "tensionsloser Grenzfall des ueblichen Strings", sondern eine
    eigene "conformally invariant string action", verallgemeinert aus einer CSP-Punktteilchenwirkung; BRST-quantisiert;
    "the vacuum carries a continuous spin representation ... the spectrum is ghost-free". Ob diese Wirkung tensionslos
    ist, steht im Abstract nicht ([L?] ja). 2610.00745 zitiert Mourad nicht.
  - 2406.17017 Bellazzini/De Angelis/Romano (v3, JHEP 05 (2025) 166 laut 2610.00745 Ref. [17]): E11 **teils:**
    Dreipunktamplituden "uniquely determined by matching their high-energy limit to that of definite-helicity (ordinary)
    massless particles"; Kopplung an Gravitation und Elektromagnetismus nur "in a loose version of S-matrix principles".
  - 2510.05011 Metsaev (v2 19.08.2026; JHEP 03 (2026) 061 laut Ref. [16]): E12 **teils verletzt:** "All parity-even cubic
    vertices for self-interacting continuous-spin fields ... are obtained. Cross-interactions of continuous-spin fields and
    integer-spin fields are also derived"; "manifestly Lorentz invariant formal cubic action involving at least one
    continuous-spin field turns out to be divergent"; Abhilfe durch modifizierte Wirkung. Kubische Ebene also gebaut, mit
    Divergenzproblem; nichtlinear darueber nichts.
  - 2606.28245 Basile/Bekaert/Figueroa/Skvortsov (v1 26.06.2026): E13 **bestaetigt (Formalismus), mit Zusatz:** "CSP
    amplitudes can be understood as the infinite-spin limit of amplitudes of massive particles".
- **A4 (Abruf 5/10, 11:14:23) arXiv-API-Suche abs/ti "continuous spin" ODER abs "infinite spin", 80 Treffer, nach Datum,
  reicht bis 2024-09-18, quellen/search-A4.xml (sha256 186a885f789b7dfb28308f62950331e00245aab49c26453a34702abf225bbe1f).
  [Sa fuer die unten genannten Abstracts]** Viel Fremdtreffer (Spinmodelle, n-Koerper "infinite spin", Kerr). E17:
  - **bestaetigt:** keine Arbeit mit nichtlinearer CSP-Gravitation im Titel; keine Arbeit ausser 2610.00745 zu CSP in
    Strings endlicher Spannung. Metsaev 2505.02817: kubische Vertices CSP-ganzzahliger Spin "complete for the dimensions of
    space-time greater than four" (also nicht fuer D = 4 vollstaendig).
  - **VERLETZT (gross) -> Z-2:** Zwei Gravitations-Bootstrap-Arbeiten 2026 finden neben dem String eine zweite Ecke mit
    unendlich vielen Spins **bei einer Masse**, und der String wird erst durch eine Endlichkeitsannahme ausgewaehlt:
    - Berman/Caron-Huot/Chandra/Elvang/Herderschee/Lin/Morales, arXiv:2607.14230v1: erlaubter Bereich "a non-convex domain
      with two sharp corners: one being the closed superstring Virasoro--Shapiro amplitude, the other an infinite spin tower
      amplitude exchanging states of every spin at the same mass ... requiring a finite number of states near the first
      mass level leaves only the Virasoro--Shapiro amplitude."
    - Huang/Wan/Wang/Zhou, arXiv:2610.02124v1 (= Pool S3, Elter dieser Karte): "Virasoro--Shapiro amplitude, together with
      infinite-spin alternatives, in supergravity"; "Finite-spin support at the lowest massive pole is therefore an
      additional assumption required to select the Virasoro--Shapiro amplitude".
    - dazu Shao/Vichi arXiv:2607.27300v2: "infinite-spin-tower (IST) amplitudes"; "graviton pole imposes unitarity
      constraints on UV spectrum".
  - **VERLETZT (mittel, Projektstand):** Reilly/Russo/Schuster/Toro arXiv:2505.15890v2: Photon als CSP, 21-cm-Uebergang,
    Abweichung "proportional rho^2 alpha^2/omega^2", "suggesting experimental constraints rho <~ 1 meV". Das Projekt
    (24.09.) kannte fuer das Photon nur einen Beispielwert. Es ist eine vorgeschlagene Grenze (Wortlaut "suggesting"),
    keine Datenanpassung; fuer das Graviton weiter nur Empfindlichkeiten.
  - Namensfallen: "infinite spin" = klassischer Grenzfall grosser Drehimpulse (Das/Mandal/Sarkar 2506.23974, Kerr-Arbeiten),
    n-Koerper-Kollisionen; "string" = stringlokalisiertes Feld (Mund/Schroer/Yngvason) gegen Stringtheorie.

### Analysezyklus Z-2 (11:16): eine gemeinsame Groesse hinter "kein CSP" und "nur der String"

- Regel 6: Zu "kein CSP" fuehren mindestens drei Wege: (1) Oszillatoralgebra perturbativer Strings (FQT 2013 S. 2, 5-6;
  2610.00745 Abschn. 4-6) [S]; (2) Lokalitaet in beschraenkten Gebieten (Longo/Morinelli/Rehren: Vakuum zyklisch fuer
  Doppelkegel-Algebren -> keine unendlichen Spins) [Sa]; (3) Wigner/Weinberg: kein beobachteter kontinuierlicher
  Freiheitsgrad, endlich viele Zustaende je Impuls (FQT S. 2 "something that has not been observed in nature") [S].
  -> Der String ist nicht "die Ursache", sondern ein Fall einer gemeinsamen Voraussetzung. **[H] Gemeinsame Groesse:
  Zahl der Zustaende je Massenstufe und Impuls (endlich gegen unendlich).** 2610.00745 sagt es selbst: "forbidding an
  infinite spectrum of massless particles" (S. 12, Z. 922).
- Dieselbe Groesse entscheidet im Gravitations-Bootstrap zwischen String und "infinite spin tower" (2607.14230,
  2610.02124, Abstracts [Sa]): Endlich viele Zustaende an der ersten Massenstufe -> nur Virasoro-Shapiro.
- **Korrigierte Erwartung zu E4 (protokolliert, [H]):** Der CSP-Zweig ist vom String-Zweig nicht getrennt, sondern mit ihm
  ueber eine gemeinsame Annahme gekoppelt: "endlich viele Zustaende je Massenstufe". Haelt sie, sind CSP und die
  Einmassen-Turm-Ecke beide ausgeschlossen und der String bleibt; faellt sie, oeffnen sich beide. Zu pruefen: (a) ob
  2607.14230 die Turm-Ecke selbst mit CSP oder unendlicher Entartung verbindet; (b) ob der tensionslose Fall (Mourad,
  Savvidy) genau dort liegt.
- **Vorab A5-A7 (11:16):**
  - A5 arXiv-API id_list hep-th/0410009, hep-th/0310085, 2203.00696. E18: Mourad 2004 verbindet CSP mit tensionslosen
    Strings; Savvidy 2004: tensionsloser String enthaelt unendlich viele masselose Spins bzw. unendlichdimensionale
    Darstellungen; Huang/Remmen 2022: UV-vollstaendige Gravitationsamplituden brauchen einen unendlichen Turm.
  - A6 2607.14230 Volltext (PDF), nur per grep gelesen: E19: kein Wort zu "continuous spin"; die Turm-Ecke wird als
    unendliche Entartung bei einer Masse beschrieben und nicht als physikalischer Kandidat verworfen, sondern nur durch die
    Endlichkeitsannahme.
  - A7 2406.17017 Volltext (PDF), nur per grep "gravit": E20: Unter strengen S-Matrix-Regeln keine konsistente
    CSP-Graviton-Kopplung mit Aequivalenzprinzip; nur mit gelockerter Analytizitaet oder Faktorisierung.
- **A5 (Abruf 6/10, 11:16:10) arXiv-API id_list, quellen/abs-batch-A5.xml (sha256
  eb43a477b784b098fa134124a3ade63368874995b4b5a4404b412605297a5dc8). [Sa]** E18 **bestaetigt, und ein Verstoss:**
  - Mourad, hep-th/0410009v3 "Continuous spin and tensionless strings": Punktteilchenwirkung -> CSP; "The string
    generalisation of the action is identical to the tensionless extrinsic curvature action proposed by Savvidy"; BRST:
    "critical dimension of 28". -> Mourads CSP-String ist tensionslos (damit E14 nachtraeglich: tensionslos ja).
  - Huang/Remmen, 2203.00696v2, PRD 106, L021902 (2022) (= Ref. [22] von 2610.00745): UV-vollstaendige
    Vier-Graviton-Amplituden ohne String; "The spectrum invariantly exhibits accumulation points in the form of infinite
    towers of states on each mass pole". -> wieder: nicht-stringige Vervollstaendigung = unendlich viele Zustaende je Pol.
  - **VERLETZT (gross):** Savvidy, hep-th/0310085v2, IJMPA 19 (2004) 3171 (FQT-Ref. [9]): tensionsloser String mit
    Umfangswirkung, D = 13, "All particles are massless"; "The ground state is infinitely degenerated and contains massless
    gauge fields of arbitrary large integer spin"; "The excitation levels realize CSR representations of little group E(11)
    with an infinite number of helicities"; Vermutung: alle Anregungsstufen sind physikalische Nullzustaende; "in this model
    there is no gravity" (Tensorfeld zweiter Stufe ohne besondere Rolle). -> Im einzigen String-Regime mit CSP ist (a) der
    Grundzustand unendlich entartet, (b) Glied 7 im Wortlaut verletzt (masselose Spins beliebiger Hoehe), (c) kein
    ausgezeichnetes Spin-2-Feld mehr. Erwartet hatte ich nur (b).
- **A6 (Abruf 7/10, 11:16:16) Berman u. a., arXiv:2607.14230v1, quellen/2607.14230.pdf (sha256
  d7a89495b6a061cba2ec00182d93a9706a88a8874c91e0aad81c9714c335efa5), 52 S., per grep und Z. 262-292, 1254-1300 gelesen.
  [S]** E19 **bestaetigt:** kein "continuous spin"/"CSP" im Text (grep). IST "exchanges states of every spin J = 0, 2,
  4, ... at the same mass m" (S. 4, Gl. 1.7); "Requiring that only finitely many spins appear at the mass gap removes all
  IST amplitudes ... once only finitely many spins are allowed at the gap, [the spectrum] is forced to be the discrete
  tower of the closed string" (S. 5); IST = Virasoro-Shapiro "with all zeta_k formally replaced by 1" (S. 24, Gl. 5.14-5.15).
  Die Endlichkeit ist dort **Annahme**, nicht Ergebnis.
- **A7 (Abruf 8/10, 11:16:24) Bellazzini/De Angelis/Romano, arXiv:2406.17017v3 (JHEP 05 (2025) 166),
  quellen/2406.17017.pdf (sha256 130de128cf0ca19dcfba94444e9319e2d712aa0bc583628afe83478704dfb51c), 39 S., per grep und
  Z. 625-655, 1550-1560, 1855-1902 gelesen. [S]** E20 **bestaetigt, schaerfer als erwartet (Verstoss gegen E2/E7 in der
  Staerke):**
  - S. 12 (Z. 635-642), Folgen der "mass-splitting selection rule": "1. No on-shell coupling of CSP to (massless)
    gravitons is possible. Similarly, CSPs cannot be coupled on-shell to photons. 2. CSPs have no on-shell three-point
    self-interactions, e.g. no CSP-like gravitons nor non-abelian (massless) gauge theory can be recovered, on-shell, in
    the high-energy limit. 3. ... the CSP can't reduce to an on-shell graviton in the UV limit."
  - S. 31 (Z. 1860-1863): "3-CSPs on-shell amplitudes vanish, as do CSP-particle-antiparticle amplitudes and
    2-CSPs-1-graviton amplitudes" (unter ihren Annahmen: Poincare, Kleingruppen-Kovarianz, Analytizitaet, gutes
    Hochenergieverhalten).
  - Mit gelockerter Faktorisierung (massives Graviton, dann M -> 0): "CSPs coupled to gravity manifestly violate the
    equivalence principle at large distances ... different helicities fall differently ... consistent with General
    Relativity predictions at short distances" und Zeitverzoegerung "always remains positive, and even finite" (S. 26,
    ~~Z. 1554-1557~~ Z. 1554-1558, nachgeprueft ~~11:26~~ 11:24:00 laut date); S. 32: "violate the equivalence principle at distances larger than the spin scale, while preserving
    causality at all scales".
  - Fn. 29 (S. 31): "the SU(2) little group of massive particles contracts to CSPs ISO(2) for m -> 0 and j -> infinity with
    mj held fixed".
  - **Regel 1, offener Widerspruch:** Metsaev 2510.05011 [Sa] "All parity-even cubic vertices for self-interacting
    continuous-spin fields ... are obtained" gegen BDR "CSPs have no on-shell three-point self-interactions". Vermutete
    Moderatoren: Funktionenraum (Funktionen der Bispinoren mit Analytizitaet gegen Distributionen bzw.
    Vektor-Superraum), gleiche oder verschiedene Spinskalen rho der drei Beine, Lichtkegel- gegen komplexe Kinematik.
    Nicht aufgeloest (Metsaev nur Abstract).
- Werkzeugnotiz (~~11:19~~ 11:17:59, date; geschaetzte Zeit berichtigt): In einem Befehl stand die Zeichenfolge "awk2=0 head -0" (Tippfehler). Das ist eine
  Variablenzuweisung vor head, kein awk-Aufruf; die Zeile lieferte nichts. Kein python, awk oder perl verwendet.

## 4. Gegensweep (Eintrag nach A7; Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- G0 Projekt-grep der Leitung: Treffer in RUNDE-23/bildung-3d/PLAN.md ist **Falschtreffer** ("CubicSpline"). **Geprueft**
  (Z. 111).
- G1 "String" heisst Stringtheorie. **Geprueft: nicht immer.** CSP-Felder sind in der Feldtheorie "string-localized"
  (FQT Ref. [7]: Mund/Schroer/Yngvason 2004 [S, Ref.-Liste]; Longo/Morinelli/Rehren: nur in raumartigen Kegeln
  lokalisierbar [Sa]). Ebenso "infinite spin" = klassischer Drehimpulsgrenzfall (A4).
- G2 2610.00745 ist die geltende Fassung. **Geprueft:** /pdf/ liefert die neueste Fassung, Stempel "v1 30 Sep 2026"
  (Z. 13); keine v2 zum Abrufzeitpunkt.
- G3 Ein CSP-Graviton (Kundu/Schuster/Toro) vertraegt sich mit dem On-shell-No-go von BDR. **Nicht selbstverstaendlich**
  (BDR S. 12: "no CSP-like gravitons ... on-shell"). -> wird mit A9 geprueft.
- G4 Die Modenrechnung von 2610.00745 stimmt. **Nicht geprueft** (keine Nachrechnung in der Zeitbox). Gemildert durch
  [ES] Endlichkeitsargument und FQT S. 5 ("consistency check").
- G5 "Abwesenheit in der Natur" ist gemessen. **Geprueft: nein** (Photon nur vorgeschlagene Grenze rho <~ 1 meV,
  2505.15890 [Sa]; Graviton nur Empfindlichkeit).
- **Vorab A9 (vor dem Abruf):** Kundu/Schuster/Toro 2503.03817 (PDF, per grep). E21: nur linearisiert; nichtlineare
  Selbstkopplung als offen benannt; BDR 2406.17017 zitiert mit dem Argument, dass Feldtheorie mit Stroemen das
  On-shell-No-go umgeht (Nicht-Analytizitaet oder Off-shell).
- **A9 (Abruf 9/10, 11:18:17) Kundu/Schuster/Toro, arXiv:2503.03817v2 (13 May 2026; laut 2610.00745 Ref. [10] PRD 113
  (2026) 076017), quellen/2503.03817.pdf (sha256 a2d7a61b943098d38797c62b7c63d703a07c794c0a30ba7473a520708c2ee591), per
  grep, txt Z. 35-58 und 822-837 gelesen. [S]** E21 **teils verletzt:**
  - bestaetigt: "limited to leading order in Newton's gravitational constant, G_N" (Einleitung, Z. 52-58); "To compute a
    realistic waveform in sources, including non-linear effects, a more complete theory of interacting CSP's is required,
    which is presently a pressing direction of ongoing work" (Schluss, Z. 834-837).
  - verletzt: BDR [10] wird nicht als No-go behandelt, sondern als "a complementary path to building up interacting
    theories with non-zero rho" (Z. 35-37). Eine Antwort auf "no CSP-like gravitons ... on-shell" (BDR S. 12) steht dort
    nicht (grep "on-shell" nur im Sinn von Ebene-Wellen-Loesungen, Z. 54-56).
  - Glied-7-Lesart der Autoren: "an important gap in the above arguments: they assume that massless particles carry
    Lorentz-invariant helicity, which is not required by Lorentz-covariance of the theory" (Z. 42-45).
  - Nebenbefund: FQT 2013 ist erschienen als Fortsch. Phys. 62 (2014) 975 (KST Ref. [26], Z. 1184-1187).
- Abrufe: 9 von 10 (davon einer leer). Reserve 1 nicht genutzt. Hashes aller Kopien: quellen/SHA256SUMS.txt.
- **Gegensweep-Ergebnis G3 (geprueft mit A9):** Die CSP-Graviton-Route ist linear und hat fuer die Selbstkopplung (Glied 9)
  ein publiziertes On-shell-No-go gegen sich (BDR), auf das die CSP-Gravitationsarbeit nicht eingeht. Das war mir vor A7
  nicht bewusst; im Projekt stand nur "nur linearisiert".

## 5. Abschluss (Eintrag ab 11:24:20, date)

- Bezeichner A1-A9 sind Arbeitsnamen. Massgeblich ist die Zaehlung "Abruf n/10": A3 hatte zwei Versuche (Abruf 3 leer,
  Abruf 4), deshalb gibt es kein A8. Insgesamt 9 von 10 Abrufen.
- DOSSIER.md geschrieben ab 11:20:12 (date) und danach in beide Richtungen gegen die Quelltexte gegengelesen. Dabei
  berichtigt: Kurzfazit auf 10 Zeilen gekuerzt; Voraussetzungen der zwei Bootstrap-Arbeiten ergaenzt (maximale
  Supersymmetrie, Paritaetsbedingung, Baumniveau bzw. dispersive Annahmen); "keine der Arbeiten behandelt Kausalitaet"
  eingeschraenkt auf 2610.00745 und FQT (BDR rechnen Zeitverzoegerungen fuer CSP-Sonden); BDR-Zeilenangaben.
- Offene Rueckfragen wandern mit: DOSSIER.md Abschn. "Offene Fragen" 1-6. Am wichtigsten: Gilt das On-shell-No-go (BDR) auch
  gegen die lineare CSP-Graviton-Kopplung (KST)?
- Nicht gemacht: kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Aenderung ausserhalb des Kartenordners,
  keine Sperrpfade geoeffnet (Abrufe nur arXiv; lokal nur KARTE, CEMZ-MESS, WARUM-SPIN-2, GLIEDER-7-10-MESSBAR, RUNDE-36/37/38/39,
  RUNDE-23 PLAN, Pool, Scout-Lauf 20261004T043016Z-daily, CEMZ-Codex-Kopie).
- Ende (date, beim Schreiben dieser Zeile gemessen): 2026-10-04 11:24:35 CEST
