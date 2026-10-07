# CHIRAL-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu lesen; Gestrichenes bleibt stehen)

- Feldforscher fuer die Leitung claude-primary. Start 2026-10-04 14:20:02 CEST (date). Zeitbox 60 min, also bis
  etwa 15:20 CEST.
- Abrufbudget: 12 (arXiv abs/pdf, lokale Kopie in quellen/). Keine Websuche. Lokal kein python/awk/perl.
- Kennzeichen: [S] an der Quelle selbst gelesen; [P] Projektdatei, dort als [S] gefuehrt, von mir nicht an der
  Primaerquelle geprueft; [L] Gedaechtnis; [L?] unsicher; [ES] eigener Schluss; [H] Hypothese.

## 0. Gelesen vor dem Abruf (Projekt)

- KARTE.md (E1 bis E5).
- weltmodell-review-1/REVIEW.md Abschn. 3 bis 5, L6: "Chirale Fermionen, nichtabelsche Eichgruppe | Literatur |
  Forschungsstand, nicht im Projekt | nein | sehr hoch: ohne sie passt kein Kandidat". Rangliste Punkt 4: "Kann K-A
  oder K-B das Standardmodell auch nur im Prinzip tragen (Nielsen/Ninomiya; Spiegel-Fermionen mit Wechselwirkung
  abgeschaltet [L])?"
- RUNDE-40/WEICHE-STAND-v5.md: Fermionen-Zeile (A): QCA-BCC 8 Zustaende, Verdoppler an H, P, P'; Masse nur mit
  Inversion; Fadenende algebraisch Fermion; Zufallsnetz: ein Kegel plus raues Band.
- Fermion-Ergebnisse:
  - QCA-BCC-RUECK-1: mit 8 Zustaenden Weyl-Kegel isotrop, "an H, P und P' sitzen je vier weitere Kegel (Verdoppler)".
  - QCA-DIRAC-T-1: Masse mit Inversion, Konstruktion aus zwei entgegengesetzten Weyl-Automaten (A, A^dagger) mit
    Massenkopplung, also vektorartig [ES aus Eq. (36)-Form].
  - SPIN-ZUFALLSNETZ-1: ein sauberer Kegel langwellig, Doppler als inkohaerentes Band, rho(0) gross.
  - TWIST-SPIN-1: Fadenend-Fermion spinlos; halber Spin braucht >= 2 Zustaende je Knoten.
  - INDUZIERT-WILSON-2D: Wilson-Glied raeumt das Band, Antwort haengt am Wilson-Parameter.
  - SPIN-KAUSAL-L (Dossier): Spin 1/2 auf Kausalmengen nur mit Zusatzstruktur (Sverdlov, Noldus, Gudder); kein
    lokaler Tangentialraum (Surya 2019); Zufallsgitter: Doppler gespalten (Griffin/Kieu 1992: mit Eichfeld zurueck;
    Kieu u. a. 1994; Cohen 2006) [P, dort S Abstract]. **Damit ist E5 schon im Projekt beantwortet; kein Abruf.**

## 1. Projekt-grep (Karte: chiral, Nielsen, Ninomiya, Ginsparg, Spiegel, mirror, SU(2), nichtabelsch)

- Erwartung vor dem grep: wenige Treffer; Nielsen/Ninomiya nur als [L]-Erwaehnung; keine gelesene Primaerquelle zu
  chiralen Gitterfermionen im Projekt.
- Ergebnis (zwischen den date-Messungen 14:20:32 und 14:24:25): **bestaetigt.** Projekttexte: RUNDE-39.md Z. 312 "[ES/H] ... Haendigkeit insgesamt
  verschwinden (Nielsen/Ninomiya sinngemaess)"; RUNDE-40.md Z. 205 (LICHT-GLEICH-L: "Chadha/Nielsen nicht gelesen").
  Keine Projektdatei zu Ginsparg-Wilson, Domain-Wall-Fermionen, Spiegel-Fermionen, SMG. "Domain wall"-Treffer sind
  BEC/Solitonen (fachfremd). RUNDE-06/M-THEORIE-CALABI-YAU.md Z. 196: "Chirale Fermionen verlangen konische
  Singularitaeten (Acharya, Witten 2001, hep-th/0109152 [S])" [P] = Weg ueber Extra-Dimension/Geometrie.
- **Ueberraschung im Bestand (lokale Kopie, kein Abruf):** Levin/Wen, "Quantum ether: photons and electrons from a
  rotor model", hep-th/0507118v2, lokale Kopie RUNDE-37/twist-pyro-1/quellen/arxiv-hep-th-0507118.txt, Schluss
  Z. 1417-1444 [S, selbst gelesen]:
  - Z. 1421-1424: "This model is part of a much more general construction [5] that can produce gauge bosons with any
    gauge group. In particular, one should be able to construct a model that gives rise to SU (3) gauge bosons and
    massless Dirac fermions - that is, QCD."
  - Z. 1433-1444: "But can we actually construct a string-condensed local bosonic model that produces the entire
    standard model? We are close, but not quite there. In terms of elementary particles we can produce photons,
    gluons, leptons and quarks, but we do not know how to produce neutrinos or SU (2) gauge bosons. The problem with
    the neutrinos and the SU (2) gauge bosons is the famous chiral-fermion problem. [19] Neutrinos are chiral
    fermions and the SU (2) gauge bosons couple chirally to other fermions. At the moment, we do not know how to
    obtain chiral fermions and chiral gauge theories from any local lattice model, much less a local bosonic model."
    [19] = M. Luescher, hep-th/0102028 (2001) (Z. 1476).
  - Z. 1385-1389: "when bosonic models contain emergent non-Abelian gauge bosons, the models can produce electrons
    with a finite mass ... without fine tuning any parameters. [13]"
  - Folge: E3 erster Teil (nichtabelsch ja, chiral nein) ist Stand 2005/2007 an der Quelle belegt; offen ist nur,
    was seit 2007 dazukam (Wen 2013 SO(10), Wang/Wen 2018/2020, SMG). Das bestimmt die Abrufe.
- Weitere lokale Kopien mit Bezug: Wang/Senthil 1505.03520 (Spin-Eis-U(1), zitiert Forster/Nielsen/Ninomiya 1980
  "dynamical stability of local gauge symmetry"), Anber/Donoghue 1305.0011 (zitiert Chadha/Nielsen 1983, Nielsen/
  Ninomiya NPB 141 (1978) zur emergenten Lorentz-Invarianz, nicht zur Verdopplung). Nicht weiter verfolgt.

## 2. Abrufprotokoll (je Abruf: Erwartung vorher, Ausgang danach)

Erwartungen fuer Block 1, geschrieben nach 14:20:32 und vor dem Abruf um 14:24:25 (date-Grenzen; urspruenglich stand hier geschaetzt "14:25", berichtigt):

| Abruf | Quelle | Erwartung (ein Satz, vorher) |
|---|---|---|
| F1 | Kaplan, "Chiral symmetry and lattice fermions", arXiv:0912.2560 (PDF) | Nennt NN mit den Annahmen lokal, hermitesch/translationsinvariant, Ladung erhalten, bilinear; Domain-Wall und Overlap als Ausweg mit exakter chiraler Gittersymmetrie; chirale Eichtheorien: abelsch (Luescher) gebaut, nichtabelsch offen |
| F2 | Wang/You, "Symmetric Mass Generation", arXiv:2204.14271 (PDF) | SMG als Weg, Spiegel-Fermionen ohne Symmetriebruch zu entfernen; braucht anomaliefreien Inhalt (16 Weyl je Generation); Gitter-Belege in 1+1 und 3+1 nur numerisch fuer Spielmodelle, nicht fuer das volle SM |
| F3 | Golterman/Shamir, "Propagator zeros and lattice chiral gauge theories", arXiv:2311.12790 (abs) | Einwand: SMG erzeugt Propagator-Nullstellen, die Spiegelseite koppelt weiter ans Eichfeld, Ziel-Theorie nicht erreicht |
| F4 | Wang/Wen, "A non-perturbative definition of the standard models", arXiv:1809.11171 (abs) | Behauptet eine Gitterdefinition des SM mit 16 Weyl-Fermionen je Generation und Spiegelsektor, der durch Wechselwirkung (SMG) entfernt wird; numerisch nicht gezeigt |

Abgerufen 14:24:25-14:24:27 (curl, lokale Kopien quellen/, pdftotext). Ausgang:

- **F1 Kaplan 0912.2560v2 (18.01.2012), Abschn. 3.1 und 4.3: bestaetigt, mit Formverschiebung.** pdftotext Z.
  1294-1309: NN als Satz ueber eine Fermion-*Wirkung* S = Int Psi D(p) Psi (bilinear, impulsdiagonal also
  translationsinvariant), die nicht alle vier Bedingungen zugleich erfuellen kann: "1. D(p) is a periodic, analytic
  function of p; 2. D(p) ∝ γ p for a|p| << 1; 3. D(p) invertible everywhere except p = 0; 4. {Γ, D(p)} = 0"; (1) =
  Lokalitaet, (2)+(3) = ein Dirac-Fermion im Kontinuum, (4) = chirale Symmetrie. Z. 1323-1327 (tiefere Begruendung):
  "any symmetry that is exact on the lattice will be exact in the continuum limit, while any symmetry anomalous in
  the continuum limit must be broken explicitly on the lattice." SLAC-Ableitung verletzt (1), Folge: Ward-Identitaet
  der QED, Vertex unendlich am Zonenrand (Z. 1310-1314). Z. 2324-2334 (Zeilen 2322-2334): "there is currently no practical way to
  regulate general nonabelian chiral gauge theories on the lattice ... Thus we lack of a nonperturbative regulator
  for the Standard Model". Domain-Wall und Overlap: "a way to represent any global chiral symmetry without fine
  tuning" (Z. 2322-2323). **Korrektur an E1:** Hermitezitaet steht nicht in Kaplans Liste (euklidisch); die
  belastbare Form ist die Anomalie-Aussage, nicht die Hamilton-Form.
- **F2 Wang/You 2204.14271v1 (29.04.2022): teils bestaetigt, teils verletzt.** Fluss-Text Z. 207-219: NN "states
  that it is not possible to gap the fermion doubler in a non-interacting local lattice model without breaking the
  chiral symmetry"; Ausweg Wechselwirkung (Eichten/Preskill 1986); "early attempts ... were not successful, either
  because certain anomalies were not carefully cancelled or because the appropriate gapping interaction has not been
  found"; Wen 2013 fuer Spin(10); "More recent numerical works have successfully shown that the SMG indeed provides
  a feasible solution to regularize chiral fermions [102-105]". Die Belege [102-105]: Kikukawa (Overlap-Mass,
  formal), Kikukawa 2019 (2D abelsch, "Why is the mission impossible?"), Catterall 2021 (gestaffelte Felder, PRD 104,
  014503), Zeng/Zhu/Wang/You 2022 (1+1D, DMRG) (Z. 3893-3905). Tabelle II (Z. 1213ff): in 3+1D nur so(4)
  Higgs-Yukawa (RHMC) und su(4) psi^4 (RHMC, FBMC), also vektorartige Spielmodelle. SM Z. 3246-3300: lokale und
  globale Anomalien verschwinden fuer 15Nf- und 16Nf-SM, "such that the SMG is possible in either cases" (notwendige
  Bedingung, kein Bau). Schluss Z. 3574-3579: "Hopefully combing the ideas ... already gives the ample insights to
  fully solve ... chiral Standard Model problems." **Verstoss gegen meine Erwartung:** SM-Anomaliefreiheit macht SMG
  auch fuer 15 Weyl je Generation zulaessig (nicht nur 16); mit erhaltenem U(1)_{B-L} "only works for the 16Nf -SM" (Fluss-Text Z. 3300-3303).
- **F3 Golterman/Shamir 2311.12790 (v1 21.11.2023, v2 13.02.2024), Abstract: bestaetigt und verschaerft.** "in an
  SMG phase, the poles in the mirror fermion propagators are replaced by zeros ... they act as coupled ghost states
  ... propagator zeros generate the same anomaly as propagator poles. Thus, gauge invariance will always be
  maintained in an SMG phase, in fact, even if the target chiral gauge theory is anomalous, but unitarity of the
  gauge theory is lost."
- **F4 Wang/Wen 1809.11171 (v1 28.09.2018, v3 03.04.2020), Abstract: verletzt (staerker als erwartet).** "we
  propose that Spin(10) chiral fermion theories with Weyl fermions in 16-dimensional spinor representations can be
  defined on a 3+1D lattice, and subsequently dynamically gauged ... As a result, the Standard Models from the
  16n-chiral fermion SO(10) Grand Unification can be defined non-perturbatively via a 3+1D local lattice model of
  bosons or qubits." Also: **dieselbe Gruppe (Wen), die 2005/07 "we do not know how ... much less a local bosonic
  model" schrieb, schlaegt 2018 genau ein lokales Bosonen-/Qubit-Gitter fuer das SM vor**, begruendet ueber
  Kobordismus-Klassifikation und die Existenz symmetrischer gapper Raender ("we propose"; kein Bau, keine Rechnung im
  Abstract).

Erwartungen fuer Block 2, geschrieben nach 14:25:31 und vor dem Abruf um 14:26:14 (date-Grenzen; urspruenglich geschaetzt "14:27", berichtigt):

| Abruf | Quelle | Erwartung (ein Satz, vorher) |
|---|---|---|
| F5 | Catterall, "Chiral lattice fermions from staggered fields", arXiv:2010.02290 (abs) | Reduzierte gestaffelte (Kaehler-Dirac-)Felder plus Vier-Fermion-Wechselwirkung entfernen die Spiegel; nur fuer bestimmte Fermionzahlen (Vielfache von 8 bzw. 16 Majorana), Eichung ungeprueft |
| F6 | Kaplan/Sen, "Weyl fermions on a finite lattice", arXiv:2312.04501 (abs) | Weyl-Fermion als Randzustand eines endlichen Gitters mit Extra-Dimension; Spiegel auf dem anderen Rand durch Eichfeld-Lokalisierung/Wechselwirkung abgekoppelt; Status: Vorschlag, nichtabelsch offen |
| F7 | arXiv-API, letzte 24 Monate (ab 2024-10): Titel/Abstract "chiral gauge theor*" AND lattice | 5 bis 20 Treffer, keiner mit numerisch gebauter nichtabelscher chiraler Gittereichtheorie in 3+1D; Streit SMG weiter offen |
| F8 | arXiv-API, alle Jahre: "causal set" AND (gauge OR chiral OR fermion OR Dirac) | wenige Treffer; Eichfelder hoechstens abelsch/skizziert; nichts zu chiralen Fermionen |

Abgerufen 14:26:14-14:26:36. **Zaehlung:** F5, F6 je 1; F7 und F8 zuerst per http mit 0 Byte (2 Abrufe ohne Inhalt,
mitgezaehlt), dann per https erneut (F7b, F8b, HTTP 200). Stand **10 von 12**. Ausgang:

- **F5 Catterall 2010.02290v4 (v1 05.10.2020, v4 15.06.2021), Abstract: bestaetigt.** "a proposal for constructing a
  lattice theory that we argue may be capable of yielding free Weyl fermions in the continuum limit. The model employs
  reduced staggered fermions and uses site parity dependent Yukawa interactions of Fidkowski-Kitaev type to gap a
  subset of the lattice fermions without breaking symmetries ... tied to the cancellation of certain discrete
  anomalies ... strong constraints on the number of lattice fermions ... numerical results for the model in two
  dimensions". Freie Weyl-Fermionen, keine Eichung, Numerik nur 2D.
- **F6 "Kaplan/Sen 2312.04501": Fehlabruf.** Die Nummer gehoert zu Lim u. a., "Graph Metanetworks ..." (fachfremd).
  Meine Gedaechtnis-Nummer war falsch [L-Fehler, Selbstanzeige]. Ersatz ohne Abruf: F7 enthaelt Kaplan/Sen 2024 und
  Kroth/Sen 2025 mit Abstract.
- **F7b arXiv-API 24 Monate (2024-10-04 bis 2026-10-04): 84 Treffer. Erwartung "Streit offen, keine nichtabelsche
  3+1-Gittertheorie" bestaetigt; Erwartung ueber die Art der Arbeit verletzt** (siehe Abschn. 3, V-Liste). Abstracts
  aus der API-Antwort selbst gelesen (lokale Kopie F7-api-chiral-24m.xml, Auszug F7-entries.txt):
  - Thorngren/Preskill/Fidkowski, 2601.04304 (07.01.2026): "Hamiltonian framework for constructing chiral gauge
    theories on the lattice based on symmetry disentanglers ... Using lattice rotor models, we realize this idea in
    1+1 and 3+1 spacetime dimensions for U(1) symmetries with mixed 't Hooft anomalies ... exactly solvable
    Hamiltonian lattice model of the (1+1)-dimensional '3450' chiral gauge theory, and we argue that a related
    construction applies to the U(1) hypercharge symmetry of the Standard Model fermions in 3+1 dimensions."
  - Lu/Seifnashri/Shao, 2604.06307 (07.04.2026; PRD 114, 034518 (2026)): "solvable Hamiltonian that realizes an
    exact lattice chiral U(1)_V x U(1)_A symmetry. Nielsen-Ninomiya-type no-go theorems are evaded by using lattice
    bosons rather than fermions. The continuum limit is a compact boson field theory with an axion-like coupling."
  - Baig/Chen/Cherman/Neuzil, 2607.09935 (10.07.2026), 2D: "bosonic lattice models can offer a lattice
    regularization of chiral fermions ... ultra-local action and an ultra-local symmetry ... The reconstructed lattice
    Dirac operator has no doublers, but is consistent with the Nielsen-Ninomiya theorem because it turns out to be
    non-local."
  - Seifnashri, 2601.14359 (20.01.2026): "exactly solvable abelian chiral lattice gauge theories in two spacetime
    dimensions" (34-50-Modell). Onoda, 2606.12358 (10.06.2026): 2D nichtabelsch ueber Bosonisierung, "Establishing
    the desired continuum limit remains an important open problem."
  - Golterman/Shamir, 2505.20436v3 (26.05.2025; v3 12.01.2026, "Matches published version"): "we formulate a
    generalized no-go theorem which establishes the conditions for the applicability of the Nielsen-Ninomiya theorem
    to this hamiltonian. If these conditions are satisfied, the massless fermion spectrum must be vector-like ...
    qualitative differences between four-dimensional and two-dimensional theories that limit the lessons that can be
    drawn from two-dimensional models ... a list of open questions". Dazu 2603.15985 (Lattice 2025, gleiche Aussage).
  - Araki/Fukaya/Onogi/Yamaguchi, 2608.29963 (30.08.2026): "first numerical examination of symmetric mass generation
    (SMG) for domain-wall fermions ... two-dimensional Euclidean lattice ... the local four-Fermi interaction
    selectively gaps the edge fermions on the mirror wall while leaving the physical wall intact."
  - Kaplan/Sen, 2412.02024 (02.12.2024): "Four-dimensional chiral gauge theory can be formulated as the boundary
    theory on a five-dimensional manifold in a manner that may be realized on a finite lattice ... universality
    being violated by inaccessible light modes in the five-dimensional bulk."
  - Kroth/Sen, 2506.04324 (04.06.2025): "Recent work has extended this idea to realize a single unpaired Weyl fermion
    in a finite lattice ... string defect embedded in (2n+2)-dimensional spacetime on a finite lattice for n=1".
    Dang/Karur/Sen, 2606.05306 (03.06.2026): Gradientenfluss-Vorschlag auf der Platte, umgesetzt fuer n = 1 (2D).
  - Lin/Zhang/Zhang, 2602.11935 (12.02.2026; PRA 113, 063303 (2026)): "In static lattice systems, the
    Nielsen-Ninomiya theorem enforces the pairing of Weyl points with opposite chiralities ... Periodic driving
    provides a viable route to circumvent this no-go constraint ... eight Weyl points emerge in the quasienergy
    spectrum ... whose net chirality can be precisely tuned."
  - Bakircioglu/Arnault/Arrighi, 2505.07900v3 (12.05.2025; v3 17.01.2026; "Last arXiv preprint before submission"):
    "We demonstrate the existence of FD issues in QCAs ... By applying a covering map on the Brillouin zone, we
    provide a flavor-staggering-only way of fixing FD that does not break the chiral symmetry of the massless scheme.
    We explain how this method coexists with the Nielsen-Ninomiya no-go theorem, and give an example of
    neutrino-like QCA showing that our model allows to put chiral fermions interacting via the weak interaction on a
    spacetime lattice, without running into any FD problem."
  - Kouroshnia/Moffat/Thompson, 2607.05485v5 (06.07.2026): nichtlokale Kontinuums-QFT: "no additional fermion
    species are introduced ... provided that the form factor is nonvanishing at every point ... distinguish this
    result from the standard Nielsen-Ninomiya theorem, which applies local lattice fermions on a compact Brillouin
    zone."
  - Liu, 2602.13948 (15.02.2026): NN-artige Saetze aus gruppenkohomologischen Anomalien in Quanten-Spinsystemen
    (Kapustin/Sopenko): "a fundamental algebraic incompatibility between anomaly data and the dimension of local
    Hilbert spaces."
  - Ma/Zhang, 2411.09886 (15.11.2024): "By abandoning Hermiticity, the non-Hermitian formulation circumvents the
    Nielsen-Ninomiya theorem while maintaining chiral symmetry".
- **F8b arXiv-API Kausalmengen, alle Jahre: 25 Treffer; "chiral" in 0 Abstracts. Erwartung zu chiralen Fermionen
  bestaetigt; zu Eichfeldern verletzt:** Sverdlov 0807.2066 (2008): "Lagrangian of a charged scalar field coupled to a
  SU(n) Yang-Mills field ... in terms of holonomies between pairs of points, causal relations, and volumes or
  timelike distances"; Sverdlov/Bombelli 0905.1506 (2009): "we treat in detail the case of scalar fields, Yang-Mills
  gauge fields and the gravitational field". Nichtabelsche Eichfelder sind also als Vorschlag da (Holonomie je
  Punktpaar), nicht als Rechnung. Fermion-Treffer = die aus SPIN-KAUSAL-L bekannten (Sverdlov, Noldus, Gudder).

Erwartungen fuer Block 3 (letzte zwei Abrufe), geschrieben nach 14:28:51 und vor dem Abruf um 14:29:30 (date-Grenzen; urspruenglich geschaetzt "14:30", berichtigt):

| Abruf | Quelle | Erwartung (ein Satz, vorher) |
|---|---|---|
| F11 | Bakircioglu/Arnault/Arrighi 2505.07900v3 (PDF) | Die "Reparatur" deutet die Doppler als physikalische Geschmaecker um (wie gestaffelte Fermionen); die Netto-Chiralitaet aller Kegel bleibt null; das "neutrino-like" Beispiel ist chiral nur je Geschmack, nicht insgesamt, und das ist die Art, wie es mit NN koexistiert |
| F12 | Thorngren/Preskill/Fidkowski 2601.04304 (PDF) | 3+1 nur abelsch (U(1) mit gemischter Anomalie); nichtabelsche chirale Eichung (SU(2)) ausdruecklich offen; Rotoren mit unendlich-dimensionalem lokalem Raum; Disentangler existiert genau bei Anomaliefreiheit |

Abgerufen 14:29:30-14:29:31 (HTTP 200, pdftotext). **Stand 12 von 12, Budget erschoepft.** Ausgang:

- **F11 Bakircioglu/Arnault/Arrighi 2505.07900v3: Erwartung im Kern bestaetigt, Begruendung anders.** Abschn. 6.2
  (pdftotext Z. 2086-2240): Sie zitieren NN 1981 woertlich ("the appearance of equally many right- and left-handed
  species ... is an unavoidable consequence of a lattice theory under some mild assumptions", Z. 2093-2096) und
  NN: "The most important consequence of our no-go theorem is that the weak interaction cannot be put on the
  lattice" (Z. 2116-2117). Ihr "Neutrino" (Z. 2141-2252): Der Zustandsraum enthaelt weiter psi_R und psi_L fuer zwei
  Geschmaecker (Gl. 6.9); gewaehlt werden g_R = 0, psi_R(n = 0) = 0 und der zweite Geschmack unbesetzt (Gl.
  6.11-6.12). "thanks to our lattice structure allowing for two flavors (even if one of them ... is actually not
  populated), red right-handed neutrinos do not appear, i.e., we bypass Nielsen-Ninomiya's theorem - in its very
  original form" (Z. 2248-2251). Fussnote 17 (Z. 2122-2125): ob die chirale Symmetrie am Geschmacks-Staffeln liegt
  oder an einer Besonderheit ihres Schemas, sei offen. Ein-Teilchen-Bild, keine Anomalie, kein Dirac-See.
  **[ES]:** Das ist ein vektorartiger Zustandsraum mit abgekoppeltem rechtshaendigen Zuschauer, kein Netto-chirales
  Spektrum; NN wird nicht umgangen, sondern die Frage wird durch Anfangsbedingung und g_R = 0 vermieden. Bestaetigt
  zugleich: Ihre (3+1)D-QED-QCA (Ref. [8]) **hat** Verdopplung (Z. 71, 1186) wie unsere QCA-TETRA/BCC-Befunde.
- **F12 Thorngren/Preskill/Fidkowski 2601.04304v2 (12.06.2026): bestaetigt, mit einer Ergaenzung.** Z. 90-92:
  "lattice models with strictly local interactions and strictly on-site symmetries generically produce fermions in
  vector-like pairs [NN81]". Z. 101-106: Overlap "does not provide an explicitly local Hamiltonian". Z. 113-115: SMG
  "requires understanding the strongly-coupled mirror fermion sector". Z. 127-128: "there are obstructions to
  gauging symmetries on the lattice that have no analogue in the continuum ... anomaly cancellation in quantum field
  theory does not, in general, guarantee the existence of a corresponding lattice construction". Z. 163-166: 3450 in
  1+1D, "tensor-product Hilbert space, albeit with infinite-dimensional rotor degrees of freedom". Z. 170-191: in
  3+1D "complicated by our inability to find exactly solvable Hamiltonians ... we combine our construction with the
  domain wall fermion framework ... D+1-dimensional slab hosting a free-fermion G-SPT ... This anomaly matching
  plausibly allows ... to be gapped out together". Z. 230-232: "While a complete Hamiltonian realization of the full
  Standard Model has not yet been achieved". "non-abelian": 0 Treffer im ganzen Text. **Ergaenzung zur Erwartung:**
  auch dieser neueste Hamilton-Weg braucht in 3+1D eine Extra-Dimension endlicher Dicke (Platte).

## 2b. Projektdaten im Gegensweep (kein Abruf; lokale Kopie DP 2014 aus qca-tetra-1/quelle/, pdftotext nach quellen/)

- QCA-TETRA-1 ERGEBNIS Z. 166-172 (Tabelle QT3): Kegelpunkte des Weyl-Automaten A^+: Gamma W = +I, P W = -I, H W = -I,
  P' W = +I (A^-: Gamma +I, P +I, H -I, P' -I). **Also liegen nicht alle Doppler bei derselben Quasienergie:** zwei
  Kegel bei Quasienergie 0, zwei bei pi.
- DP 2014 Gl. (27)-(29) [S, lokale Kopie Z. 560-609]: a_x = s_x c_y c_z ± c_x s_y s_z, a_y = c_x s_y c_z ∓ s_x c_y s_z,
  a_z = c_x c_y s_z ± s_x s_y c_z, d = c_x c_y c_z ∓ s_x s_y s_z, alpha_y = ∓sigma_y, c_i = cos(k_i/√3).
- **[M, eigene Algebra, nicht gegengelesen]:** A^+ = R_z(c) R_y(-b) R_x(a) mit R_j(t) = exp(-i sigma_j t), a = k_x/√3,
  b = k_y/√3, c = k_z/√3 (= Transponierte von R_x(a) R_y(b) R_z(c); passt zum TETRA-1-Vermerk "stimmt nur fuer W^T").
  Urbilder von +I im Wuerfel [0, 2pi)^3: vier mit a, b, c in {0, pi} (gerade Zahl von pi; alle ≡ Gamma) und vier in
  {pi/2, 3pi/2} (darunter (pi/2, pi/2, 3pi/2) = P'). Probe gegen die TETRA-1-Tabelle: M(pi/2, pi/2, pi/2) = -I (P),
  M(0, 0, pi) = -I (H), M(pi/2, pi/2, 3pi/2) = +I (P') - stimmt. Linearisiert: Jacobi-Matrix bei Gamma diag(1, -1, 1),
  Determinante -1; bei P' diag(1, 1, 1), Determinante +1 (erste Rechnung im Kopf mit R_x R_y R_z gab +1/-1, gleiche
  relative Lage; vor 14:36:37 fuer die exakte DP-Form korrigiert). Der Wuerfel ueberdeckt die Zone vierfach; Abbildungsgrad
  4 x (-1 + 1)/4 = 0. **Folge:** Gamma
  und P' haben entgegengesetzte Chiralitaet bei Quasienergie 0; der DP-Automat ist bei niedriger Quasienergie
  vektorartig, die Floquet-Umgehung (Lin/Zhang/Zhang 2026) ist in ihm nicht verwirklicht.
- Inversion (k -> -k mit festem Unitaer) erzwingt Abbildungsgrad bzw. W3 = 0 (Grad der Antipodenabbildung auf T^3 ist
  -1) [M]. Die reine Drehgruppe T erzwingt das nicht. QCA-BCC-RUECK-1 Z. 206-207: "Die Chiralitaeten der vier Kegel
  heben sich auf (Summe ≤ 2,9e−5)" - gemessen ueber die vier Kegel bei k = 0, ohne Trennung nach Quasienergie (aus der
  Zusammenfassung nicht ersichtlich [ES]).

## 3. Notizen je Erwartung (geschrieben vor der date-Messung 14:36:37; zuerst geschaetzt "14:38", berichtigt)

- **E1 (NN-Inhalt): eingetroffen, Form korrigiert.** Kaplan: vier Bedingungen an eine bilineare Wirkung (lokal,
  richtiger Kontinuumslimes, keine weiteren Nullstellen, {Gamma, D} = 0). Tiefer: Anomalie-Satz (exakte
  Gittersymmetrie bleibt exakt; anomale muss explizit gebrochen sein). TPF 2026: "strictly local interactions and
  strictly on-site symmetries". Liu 2026: Unvertraeglichkeit von Anomaliedaten und Dimension der lokalen
  Hilbertraeume. Die Pruefliste der Annahmen ist also: lokal, on-site, frei (bilinear), statisch (zeitunabhaengig),
  hermitesch, endliche lokale Dimension. Translationsinvarianz ist fuer die Anomalie-Form nicht noetig [ES aus
  Kaplan Z. 1323-1327].
- **E2 (Auswege, Stand SM): eingetroffen; Feld lebendiger als erwartet.** Overlap/GW und Domain-Wall: globale
  chirale Symmetrie ja; nichtabelsche chirale Eichtheorie "no practical way" (Kaplan 2012). SMG: Kernstreit
  (Golterman/Shamir 2023-2026: Nullstellen = Geister, Unitaritaet verloren; verallgemeinertes No-go, falls
  Bedingungen gelten). 2025-2026: Hamilton-/Bosonen-Wege (TPF, Seifnashri, Lu/Seifnashri/Shao, Baig u. a., Onoda),
  exakt nur in 1+1D; in 3+1D nur abelsch (U(1)_Y) und mit Platte (TPF), oder als Vorschlag (Wang/Wen SO(10)). Volles
  SM: von niemandem gebaut; TPF Z. 230-231 sagt das ausdruecklich.
- **E3 (bosonische Netze): teils verletzt.** Nichtabelsch: Levin/Wen "any gauge group", SU(3) "should be able to"
  [S]. Chiral: 2005/07 "much less a local bosonic model" [S], 2018 Wang/Wen "via a 3+1D local lattice model of
  bosons or qubits" (Vorschlag) [S Abstract], 2026 Bosonen als *Werkzeug* gegen NN (Lu/Seifnashri/Shao, Baig u. a.)
  [S Abstract]. Die Richtung hat sich umgekehrt: bosonisch ist nicht mehr die schwerere, sondern die bevorzugte
  Ausgangslage. Gezeigt (exakt, gerechnet) aber nur 1+1D.
- **E4 (Kausalmengen): eingetroffen fuer chiral (0 Treffer), verletzt fuer nichtabelsch** (Sverdlov 2008, SU(n) ueber
  Holonomien je Punktpaar; Sverdlov/Bombelli 2009). Spinoren: SPIN-KAUSAL-L [P].
- **E5 (Zufallsgitter): ohne Abruf aus SPIN-KAUSAL-L [P, dort S Abstract]: gespalten** (Griffin/Kieu 1992 mit Eichfeld
  zurueck; Kieu u. a. 1994; Cohen 2006). Dazu Projekt: SPIN-ZUFALLSNETZ-1 (raues Band statt Kegel) [P].

## 4. Regime und Unterscheidungspunkte

- **Moderatoren (Regel 1), je mit Quelle:**
  - M1 Ort der Symmetrie: on-site (NN gilt) gegen not-on-site (GW/Overlap; TPF; Lu u. a.) [S].
  - M2 Kopplung: frei (NN-Satz bilinear) gegen stark (SMG); Golterman/Shamir: auch stark vektorartig, *wenn* ihre
    Bedingungen gelten [S Abstract]. Das ist das Regime-Paar schwach/stark der Leitung.
  - M3 Dimension: 1+1D (exakte Loesungen: 3450, 34-50, DMRG-SMG, DWF-SMG 2026, Onoda) gegen 3+1D (nur Vorschlaege);
    Golterman/Shamir 2025: zweidimensionale Lehren begrenzt uebertragbar [S Abstract].
  - M4 Lokalitaet: lokal (NN) gegen nichtlokal (SLAC: Ward-Identitaet bricht [S Kaplan]; Baig u. a.: rekonstruierter
    Operator nichtlokal, Eichung trotzdem moeglich, 2D [S Abstract]; Kouroshnia u. a.: Kontinuum [S Abstract]). Das
    ist das Regime-Paar lokal/nichtlokal der Leitung.
  - M5 Zeit: statisch gegen periodisch getrieben/QCA (Lin/Zhang/Zhang 2026: ungepaarte Weyl-Punkte [S Abstract]).
  - M6 abelsch gegen nichtabelsch; M7 Hintergrund- gegen dynamisches Eichfeld (Dang u. a. 2026 nur Hintergrund);
    M8 hermitesch gegen nicht hermitesch (Ma/Zhang 2024).
- **Kopplungsgroesse (Regel 6) [ES]:** Sechs Wege zu Chiralitaet ohne Doppler (Symmetrie nicht on-site,
  Extra-Dimension, starke Kopplung, Nichtlokalitaet, periodischer Antrieb, keine Hermitezitaet). Gemeinsame Groesse:
  **wo die 't-Hooft-Anomalie sitzt** (im Volumen einer Extra-Dimension, in einer nicht-on-site Symmetrie, in
  nichtlokalen Operatoren, in der Quasienergie-Windung, oder durch stark gekoppelte Spiegel aufgehoben). Liu 2026 und
  TPF Z. 127-128 sagen dasselbe von der Gitterseite. Kandidatenvergleich deshalb nach "wo kann die Anomalie sitzen",
  nicht nach Fermion-Bauteil.
- **Unterscheidungspunkte (Regel 2):**
  - SMG gegen Golterman/Shamir: 4D mit dynamischem Eichfeld; Vorzeichen des Ein-Schleifen-Beitrags zur
    Beta-Funktion (Nullstelle gegen Pol) und Unitaritaet; in 2D abelsch: negativer Beitrag zum Photon-Massenquadrat
    [S Abstract 2311.12790]. 2D zugaenglich, 4D bisher von niemandem gerechnet [ES].
  - Floquet/QCA gegen statisch: Netto-Chiralitaet je Quasienergie-Sektor (Windungszahl W3 von U(k)). Fuer den
    DP-Automaten [M]: 0. Fuer Projekt-Automaten ohne Inversion offen; klein pruefbar.
  - Nichtlokal (K-B) gegen lokal: Zeigt ein nichtlokaler Dirac-Operator auf einer Kausalmenge Doppler, und haelt die
    Ward-Identitaet mit Eichfeld? Unzugaenglich, weil es keinen 3+1-Dirac-Operator auf Kausalmengen gibt [P].
  - Wang/Wen-Vorschlag gegen Golterman/Shamir-No-go: ein 3+1D-SMG-Modell mit 16 Weyl-Fermionen und dynamischer
    Eichung; Messgroesse: masselose Spektren beider Chiralitaeten nach dem Einschalten. Praktisch unzugaenglich
    (Vorzeichenproblem, Kaplan Z. 2340-2342) [ES].

## 5. Gegensweep (Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- G1 "Unsere QCA-Doppler sind gewoehnliche NN-Paare bei gleicher Energie." **Geprueft** (Projektdaten + DP 2014 lokal,
  Abschn. 2b): Die Kegel liegen bei zwei Quasienergien (0 und pi). Fuer den DP-Automaten bilden Gamma und P' bei
  Quasienergie 0 ein Paar entgegengesetzter Chiralitaet [M] - die Selbstverstaendlichkeit haelt hier, aber nur durch
  Rechnung, nicht aus dem Satz; fuer die 8-Zustands-Treffer ohne Inversion ist sie offen.
- G2 "Bosonisch ist schwerer als fermionisch" (Levin/Wen 2005). **Geprueft** (F7 Abstracts): 2026 umgekehrt; Bosonen
  sind der Hebel gegen NN (Lu u. a., Baig u. a.), aber exakt nur in 1+1D bzw. ohne Fermionen.
- G3 "Ein Weltmodell muss das SM als Gittertheorie nichtperturbativ definieren." Nicht geprueft an Quellen. Kaplan
  Z. 2333-2334: "we think perturbation theory suffices for understanding the Standard Model in the real world" [S].
  **[ES]:** Fuer ein Netz als *Fundament* (K-A, K-M) reicht Stoerungstheorie nicht: das SM muss aus dem Netz als
  Grenzfall folgen; die Frage ist dort echt. Fuer K-B ebenso, solange Fermionen auf der Kausalmenge leben sollen.
- G4 "Die Doppler muessen weg." Nicht geprueft: Sie koennten physikalische Spiegel-Teilchen bei hoher Masse sein.
  [ES/L]: Bei derselben SU(2) x U(1) bekaemen sie Masse nur aus der elektroschwachen Brechung, also hoechstens
  TeV-Skala; das waere eine vierte, gespiegelte Generation [L]. Nur die SMG-Variante (symmetrisch, hohe Skala) bleibt.
- G5 "Pfeil-Eis (Spin 1/2 je Kante) und Rotoren sind gleich gut." Nicht geprueft. TPF brauchen unendlich-dimensionale
  Rotoren [S Z. 165]; Liu 2026 bindet NN-artige Saetze an die Dimension der lokalen Hilbertraeume [S Abstract]. Ob
  Finns endliche Pfeile reichen, ist offen [H].

## 6. Offene Rueckfragen (wandern mit)

- R1: Gilt Nielsen/Ninomiya fuer QCA (diskrete Zeit, unitaer) genauso wie fuer Hamiltonians? (Projekt hat QCA)
  **Teilantwort (vor 14:36:37):** Nein, nicht in derselben Form: Floquet erlaubt ungepaarte Weyl-Punkte je Quasienergie-
  Sektor (Lin/Zhang/Zhang 2026 [S Abstract]); die Summe ueber alle Sektoren bleibt 0 [L?]. Fuer den DP-Automaten
  ist die Netto-Chiralitaet bei Quasienergie 0 trotzdem 0 [M]. Offen fuer die 8-Zustands-Automaten.
- R2: Wo steht Kaplans eigene neuere Arbeit (Kaplan 2024, "Kap24" bei TPF) genau? Nicht gelesen (Nummer unbekannt,
  F6 war ein Fehlabruf).
- R3: Ist Golterman/Shamirs verallgemeinertes No-go auf Wang/Wen und TPF anwendbar? Nur Abstracts gelesen.

## 7. Rohdatenprobe zum Kartenvorschlag (jq, nur gelesen)

- qca-bcc-rueck-1/lauf-69/haupt_8Na.json: Schluessel "spruenge", "A", "chiral_det", "kegel_cluster", "spezialpunkte"
  vorhanden. Bei Gamma je Treffer vier Zweifach-Kegel mit "phase" und "chiral_det"; erster nichttrivialer Eintrag:
  Phasen 0,551 / -0,234 / 1,613 / -3,117, Vorzeichen + / + / - / -. An H, P, P' nur "phase", "m", "typ",
  "lin_min/max" (keine Chiralitaet). Folge: Die Netto-Chiralitaet je Quasienergie-Luecke ist aus den gespeicherten
  Daten nicht ablesbar; die Karte braucht Rechnung (Kegel in der ganzen Zone oder W3-Integral).
- Floquet-Version von NN [M, Skizze]: alle Luecken tragen dieselbe Netto-Chiralitaet = W3; statisch 0.

## 8. Abgabe

- Stand 14:44:58 (date): DOSSIER.md geschrieben ab 14:38:40, Rueckwaertsdurchgang mit Zeilen- und Wortlautkorrekturen (Selbstanzeige 6 im
  Dossier). Offene Rueckfragen R1 (Teilantwort), R2, R3 wandern ins Dossier (O1 bis O5).
