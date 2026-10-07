# DYON-STATISTIK-L: Arbeitsfeld (feldforscher, Runde 39)

- Feldforscher fuer die Leitung claude-primary. Start 2026-10-04 11:06:02 CEST (date); Datei angelegt 11:11:16 CEST.
- Eine Datei fuer alle Zwischenstaende (Feld-Regel 5). Gestrichenes bleibt als ~~gestrichen~~ stehen.
- Kennzeichen: [S] an der Quelle selbst gelesen (lokale Kopie, grep/sed), [S-P] im Projekt schon an der Quelle gelesen
  (nicht neu abgerufen), [P] Projektdatei, [L] Gedaechtnis, [L?] unsicher, [ES] eigener Schluss, [H] Hypothese.
- Budget: hoechstens 10 Abrufe, Zeitbox 50 min (bis etwa 11:56 CEST).

## 0. Gelesen vor dem ersten Abruf (Projekt) [P]

- KARTE.md (E1 bis E5, Leitung 11:02:56).
- ladung-monopol-l/DOSSIER.md und ARBEITSFELD.md: schon an der Quelle gelesen (nicht erneut abrufen):
  - Goldhaber 1976 (Abstract, APS und INSPIRE): "may bear net half-integer spin, but the wave function of two such
    clusters must be symmetric under their interchange"; Relativbewegung "implies the usual connection between spin and
    statistics" [S-P].
  - Wang/Senthil PRX 6, 011034 (2016), APS-Volltext, aber vom Werkzeug nur bis Abschn. IV gesehen: Tabelle I (sieben
    Familien), III.B "E and M cannot simultaneously be fermionic" (strikt 3D bosonisch), III.A "most fundamental emergent
    particles to be dyons", II: (E_fT M_f)_theta mit Dyonen (+-1/2, +-1); Pyrochlor-Satz nur [S?] (Zusammenfassung) [S-P].
  - HFB 2004, CMS 2008, BSS 2012, MKF 2013, Levin/Wen 2005 RMP, DeGrand/Toussaint, Jackiw/Rebbi, Hasenfratz/'t Hooft:
    nur Abstracts [S-P].
- SPIN1.md (30.09.): Weg B, J = q/2, PDG 2025 Rev. 94 (94.3) [S-P]; Bai/Lu/Orlofsky [S-P].
- STRINGENDE-1: eps = e x m Fermion, Minus aus dem e-m-Kreuzanteil; 2-pi-Drehung von eps gibt -1 (Umlauf), Zweilagen
  +1; Levin/Wen 2003 Volltext [S-P]: Paar-Erzeugungsoperator auftauchender Fermionen nie lokal.
- LADUNG-MONOPOL-1/2 [P, E]: spinloses Teilchen q am Gitter-Monopol: Dublett (q = 1), Triplett (q = 2), Kommutator
  s = (-1)^q, auf Pyrochlor-Kanten G4 (Spin-1/2-artig). Austauschstatistik nicht gerechnet.
- UEBERLEITUNGEN-EMERGENZ.md Ue2: "Elektronen die Enden offener Faeden"; P4 Spin 1/2 offen.
- grep "dyon" (runden-v3, *.md): nur die schon genannten Dateien plus RUNDE-38.md Z. 43 und RUNDE-39.md (Plan). Keine
  Treffer zu Kravec, McGreevy, Thorngren, Burnell, "all-fermion" ausserhalb LADUNG-MONOPOL-L.

## 1. Schreibtisch-Notizen (vor jedem Abruf, 11:11 bis 11:14)

- **N1 [ES/L] Dyon-Statistik-Regel.** Teilchen (n, m) (elektrisch, magnetisch, ganzzahlig) hat bei theta = 0 die Statistik
  theta_e^n theta_m^m (-1)^(n m). E_b M_b: Fermion genau bei n, m beide ungerade; E_f M_b: n ungerade, m gerade; E_b M_f:
  m ungerade, n gerade; E_f M_f: alle ausser (gerade, gerade) -> "all-fermion".
- **N2 [ES] Ohne Symmetrie sind E_b M_b, E_b M_f, E_f M_b nur Umbenennungen.**
  - theta -> theta + 2 pi (Witten-Effekt, T-Schritt) bildet (n, m) auf Ladung n + m ab: aus E_b M_b wird E_b M_f
    (der neutrale Monopol ist dann (-1, 1), ein Fermion; das ist MKFs "statistical Witten effect").
  - Elektrisch-magnetische Dualitaet S tauscht E_b M_f gegen E_f M_b.
  - SL(2,Z) permutiert die drei Restklassen (1,0), (0,1), (1,1) mod 2 transitiv. Ohne Zeitumkehr ist theta frei, also
    sind die drei Faelle *eine* Phase; nur E_f M_f ist anders (und strikt 3D unmoeglich, E4).
  - Folge fuer die Karte: H1 (Fermion = reine Ladung, E_f) gegen H2 (Fermion = Dyon, E_b M_b) ist *ohne Symmetrie und
    ohne Angabe der Kopplung* kein Phasenunterschied, sondern eine Wahl, welches Teilchen "elektrisch" heisst.
  - Was dann physikalisch bleibt: (a) die Kopplung tau = theta/2pi + i 2pi/e^2 (welches Teilchen ist schwach
    gekoppelt?), (b) Symmetrien (Zeitumkehr pinnt theta, Gitterdrehungen), (c) die mikroskopische Festlegung "Quelle der
    Pfeile = elektrisch".
- **N3 [ES] Kopplungsargument gegen "Dyon = Elektron".** Dirac: q_e q_m = 2 pi -> alpha_e alpha_m = 1/4
  (alpha = q^2/4pi). Jedes Teilchen mit magnetischer Ladung m != 0 hat alpha_eff >= m^2/(4 alpha_e). Das (1,1)-Dyon bei
  theta = 0: alpha_eff = alpha_e + 1/(4 alpha_e) >= 1 (Minimum am selbstdualen Punkt alpha_e = 1/2). Ein Dyon ist also
  nie schwach an das Photon gekoppelt. Ein Elektron (alpha = 1/137) kann darum kein Dyon sein, solange es eine
  schwach gekoppelte Ladung gibt; das schwach gekoppelte Teilchen muesste selbst Fermion sein (E_f im schwachen
  Rahmen).
  - Moderator (Feld-Regel 1): alpha_e. Weit weg vom selbstdualen Punkt gibt es ein eindeutig "leichtestes gekoppeltes"
    Teilchen; am selbstdualen Punkt (alpha = 1/2) verschwindet der Unterschied.
  - Unterscheidungspunkt (Feld-Regel 2): Coulomb-Staerke zwischen zwei der leichtesten Fermionen (alpha_e gegen
    alpha_e + 1/(4 alpha_e)), und der Monopolfluss durch eine Huelle um das Fermion (0 gegen 2 pi/e).
  - ~~Fuer Quanten-Spin-Eis erinnere ich alpha_QSI ~ 0,08 (Pace/Morampudi/Moessner/Laumann 2021) [L?]; dann
    alpha_m ~ 3: das Dyon waere stark gekoppelt.~~ Gestrichen 11:31 nach A5: am ueblichen Punkt alpha_QSI = 1/10,
    einstellbar 0 bis 0,2 (Pace S. 4) [S]; damit alpha_m = 2,5 bzw. >= 1,25 (V6, V7).
- **N4 [ES/L?] Zeitumkehr im Spin-Eis.** S^z (das Eisfeld) ist T-ungerade. In der Standard-Elektrodynamik ist E T-gerade,
  B T-ungerade. Darum koennte Wang/Senthil die Spin-Eis-"Ladung" (Spinon) in ihrer Konvention als *magnetisch* fuehren.
  Zu pruefen am Volltext (Abschnitt zu Spin-Eis). Das ist eine Falle fuer die Lesart "E_b M_b": welches Teilchen ist dort E?
- **N5 [ES] Spin-Statistik-Analogon auf dem Gitter.** STRINGENDE-1 (2-pi-Umlauf von eps gibt -1) und LADUNG-MONOPOL-1/2
  (s = (-1)^q) sind dieselbe Regel: Die 2-pi-Drehung eines e-m-Verbunds traegt die gegenseitige Phase. Fuer das Dyon
  aus bosonischem E und M folgt halbzahliger Spin *und* Fermi-Statistik (Goldhaber), also kein Verstoss. Fuer ein E_f
  aus einem Gittermodell ist der Spin nicht automatisch halbzahlig [L?]; eine Literaturstelle fuer 3D kenne ich nicht
  sicher.
- **N6 [L] Levin/Wen "Quantum ether" (PRB 73, 035122, 2006, hep-th/0507118 [L?]):** bosonisches Rotormodell auf dem
  kubischen Gitter mit Photonen und masselosen Dirac-Fermionen. Das waere die direkte Literatur zu Ue2 und H1 (E_f).

## 2. Abrufprotokoll (Erwartung vor dem Abruf, Feld-Regel 3)

| Nr | Zeit (date) | Ziel | Erwartung vor Abruf | Ausgang | Verstoss? |
|---|---|---|---|---|---|
| A1 | 11:12:11 (curl) | arXiv:1505.03520v2, PDF, 25 S., lokal quellen/arxiv-1505.03520.pdf, Text per pdftotext | Titel "Time-reversal symmetric U(1) quantum spin liquids" (Wang/Senthil). Ausdruecklicher Satz: gebundener Zustand aus bosonischem E und bosonischem M ist Fermion (mit Goldhaber/Jackiw-Rebbi-Zitat). Ohne T: E_b M_f ueber theta -> theta + 2 pi gleich E_b M_b; E_f M_b dual. Spin-Eis-Abschnitt: S^z T-ungerade, Spinon dort "magnetisch" benannt; Pyrochlor E_b M_b oder (E_fT M_f)_theta | Nummer und Titel richtig. Siehe Abschnitt 3, V1 bis V5: Satz fuer das (1,1)-Dyon in E_b M_b fehlt, die Regel steht nur fuer theta = pi; "ohne T alle sieben glatt verbunden" steht woertlich; Spin-Eis-Defekte heissen dort *magnetische* Monopole; Pyrochlor-Satz bestaetigt | **ja** (V1, V2, V3; V4/V5 neu) |
| A2 | 11:12:11 (curl) | arXiv:hep-th/0507118, Abstract, lokal quellen/arxiv-hep-th-0507118-abs.html | Levin/Wen, "Quantum ether: photons and electrons from a rotor model": rein bosonisches Rotormodell, kubisches 3D-Gitter, Photonen und masselose Dirac-Fermionen; "string-net condensation"; kein Wort zu Dyonen | bestaetigt (eine Zeile): "a purely bosonic model -- a rotor model on the 3D cubic lattice -- whose low energy excitations behave like massless U(1) gauge bosons and massless Dirac fermions"; "quantum ether ... gives rise to both photons and electrons"; keine Dyonen [S] | nein |
| A3 | 11:16:45 (curl) | arXiv-API, Titelabfrage "fine structure constant" AND "spin ice" (gezielt auf eine bekannte Arbeit, kein Suchersatz fuer Unbekanntes); lokal quellen/arxiv-api-fine-structure-spin-ice.xml | Pace/Morampudi/Moessner/Laumann, PRL 127, 117205 (2021) [L?]: emergente Feinstrukturkonstante des Quanten-Spin-Eises alpha ~ 0,08, also gross gegen 1/137; definiert fuer die Spinonen (HFB-"elektrisch"); Monopole entsprechend stark gekoppelt (alpha_m ~ 3), vielleicht nicht im Abstract | Treffer arXiv:2009.04499v2, PRL 127, 117205 (2021), DOI stimmt. Abstract: "alpha_QSI is more than an order of magnitude greater than alpha_QED ~ 1/137"; "can be tuned all the way from zero up to what is believed to be the strongest possible coupling beyond which QED confines"; "experiments ... should expect ... strong interactions" [S]. Zahl 0,08 und Zuordnung zu Spinon oder Monopol nicht im Abstract | **teilweise** (V6: alpha ist ein Stellknopf, kein fester Wert; Obergrenze unbekannt) |
| A4 | 11:16:45 (curl) | arXiv:hep-th/0507118v2, PDF 10 S., lokal quellen/arxiv-hep-th-0507118.pdf | Die Fermionen sind Enden offener (elektrischer) Strings, also reine U(1)-Ladungen (E_f im HFB-Rahmen), Fermi-Statistik ueber besondere Stringoperatoren wie Levin/Wen 2003; Dirac-Struktur aus pi-Fluss-artigem Huepfen; Lorentz-Invarianz nur bei kleinen Energien; zur T-Wirkung und zu Dyonen nichts; Spin 1/2 nur als emergente Dirac-Struktur | bestaetigt (Einzelheiten Abschnitt 3, A4): Fermionen = Stringenden = Ladungen ("twisted string operator", Gl. 12); pi-Fluss je verdoppelter Plakette, 4 Sorten vierkomponentiger Dirac-Fermionen; c != c_e, Lorentz nur durch Abstimmen von t; "monopol" kommt im Text nicht vor; Photon nur bei kleinem alpha | nein (kleiner Zusatz: alpha-Satz) |
| A5 | 11:18:03 bis 11:18:05 (curl) | arXiv:2009.04499v2, PDF 11 S., lokal quellen/arxiv-2009.04499.pdf | alpha_QSI ~ 0,08 bis 0,1 am ueblichen Arbeitspunkt; alpha bezieht sich auf die Spinonen (Quellen des S^z-Feldes); die "staerkste moegliche Kopplung" ist der Einschluss-Uebergang der kompakten U(1)-Gittertheorie (Wilson ~ 0,08 oder selbstdual 1/2, ich weiss es nicht, 50:50); Monopolkopplung 1/(4 alpha) eher nicht ausgeschrieben | Tabelle I (S. 4): alpha_QSI = 1/10 bei mu = zeta = 0; alpha = e^2/hbar c fuer die Spinonen ("which are the electric charges of the theory", S. 2); Monopolladung "from Dirac quantization, m = e/2 alpha" (Tabelle I). Obergrenze: "alpha_c ~ 0.2 at which pure lattice QED on the cubic lattice is known to confine", "argued to be the limit of stability of the deconfined phase in general [5-7]"; "0 <= alpha <= 0.2" (S. 4). Weder 0,08 noch 1/2 | **teilweise** (V7: Obergrenze 0,2, nicht 0,08 und nicht 1/2) |
| A6 | 11:21:15 bis 11:21:16 (curl) | arXiv-API, Titelabfrage ti:"symmetry enriched" AND ti:U(1) (gezielt auf zwei bekannte Arbeiten zur Symmetrie-Fraktionalisierung in U(1)-Fluessigkeiten); lokal quellen/arxiv-api-symmetry-enriched-u1.xml | Treffer Zou/Wang/Senthil, PRB 97, 195126 (2018) und Ning/Zou/Cheng (PRR 2020) [L?]; Abstracts: Klassifikation symmetrie-angereicherter U(1)-Fluessigkeiten (SO(3), Zeitumkehr), manche Kombinationen anomal; zur Spin-Statistik unter Gitterdrehungen steht im Abstract vermutlich nichts | bestaetigt (eine Zeile): 10 Treffer, darunter arXiv:1710.00743 (ZWS, PRB 97, 195126: mit T und SO(3) "15 distinct such quantum spin liquids", "11 other anomalous states") und arXiv:1905.03276 (Ning/Zou/Cheng, PRR 2, 043043: Daten rho, nu, p, n; zwei Anomalie-Stufen, "deconfinement anomaly"); dazu arXiv:1607.02287 (Li/Chen, Dipol-Oktupol-Pyrochlor) und arXiv:1904.11550 (Hsin/Turzillo). Spin-Statistik unter Gitterdrehungen in keinem Abstract [S]. Volltexte nicht geholt (Zeit) | nein |

## 3. Erwartungsverstoesse (laufend)

### A1 Wang/Senthil, arXiv:1505.03520v2 (gelesen 11:12 bis 11:15, Zeilennummern = pdftotext ohne -layout)

- **V1 (stark, gegen LADUNG-MONOPOL-L Woerterbuch und gegen die Karte):** Wang/Senthil nennen die Spin-Eis-Defekte
  *magnetische* Monopole und die Eis-Schleifen *magnetische* Feldlinien [S]:
  - Einleitung (S. 2): "The loops can be viewed as 'magnetic' field lines of an artificial magnetic field. Defect
    configurations in the spin ice manifold such as a '3-in 1-out' tetrahedron ... correspond to end points of the loops
    and are then identified with magnetic monopoles"; im Quanten-Eis "Magnetic monopoles (the defect tetrahedra) are now
    gapped quasiparticle excitations where these field lines end."
  - Abschn. X (S. 14): "In the specific context of quantum spin ice the magnetic flux loops are very easy to picture."
  - Grund: ihre Konvention "magnetic charge is time reversal odd" (Fussnote 3, S. 6) und S^z ist T-ungerade.
  - Folge: In Wang/Senthil-Kuerzeln ist die Quelle der Pfeile **M**, nicht E. Das Woerterbuch in
    LADUNG-MONOPOL-L (Zeile "Quelle des Kantenfeldes ... E in Wang/Senthil") ist in dieser Spalte falsch. HFB
    ("electric") und Wang/Senthil ("magnetic") benennen dieselbe Anregung entgegengesetzt; Inhalt ist die T-Paritaet.
  - Korrektur der Erwartung: N4 war richtig; die Lesart "E_b M_b: Spinon = E" ist umzudrehen (Spinon = M, der
    HFB-"Monopol" = E). Fuer das Dyon (1,1) aendert das nichts (es enthaelt beide).
- **V2 (stark, gegen den Rahmen der Karte H1 gegen H2):** Wortlaut S. 3, vor Tabelle I: "We emphasize that the
  distinction between these phases is entirely a consequence of the unbroken time reversal symmetry. If this symmetry
  were absent then it is possible to go smoothly between any two of these phases." Dazu Fussnote 3: "Strictly speaking
  what we call electric and what we call magnetic is a matter of convention: the U(1) gauge theory is self-dual so that
  we can interchange the definition of E and M." [S]
  - Folge: Ohne Zeitumkehr (und ohne Angabe der Kopplung) sind "Fermion = reine Ladung" und "Fermion = Dyon" keine
    verschiedenen Phasen. N2 bestaetigt, sogar staerker (alle sieben, nicht nur drei).
- **V3 (teilweise, gegen E1):** Ein Satz "in E_b M_b ist das (1,1)-Dyon ein Fermion" steht nicht im Text (grep "dyon",
  "bound state", "Eb Mb", "Goldhaber": kein Treffer dieser Art; Goldhaber wird nicht zitiert). Die Regel steht aber
  ausdruecklich fuer theta = pi, Abschn. V (S. 7): "these two dyons see each other as relative monopoles. This leads to
  the Fermi statistics of their bound state. The Kramers degeneracy can be simply understood by first calculating the
  angular momentum of the U(1) gauge field. It is readily seen that this is quantized to be 1/2." Ebenso fuer den reinen
  Monopol (0, 2): "These are also relative monopoles and hence their bound state is a fermion." [S]
  - Korrektur: E1 in der Sache (Regel "relative Monopole binden zu einem Fermion, Feld-Drehimpuls 1/2") an der Quelle
    belegt; fuer das konkrete (1,1) in E_b M_b bleibt es [ES] (gleiche Regel, Dirac-Paarung 1).
- **V4 (neu, Pyrochlor):** Abschn. XIV.A (S. 19): "Existing theoretical work[11] assumed that the simplest phase in the
  Eb Mb family is the prime candidate ... However this is justified only deep in the spin ice limit[5]". Fuer
  Kramers-Spins auf dem nicht-bipartiten Pyrochlor sei es "quite unnatural - at the level of parton mean field theory -
  to have fermionic monopoles or non-Kramers fermionic electric charges. This is already enough to render unlikely the
  Ef Mb , Eb Mf and EbT Mf phases." Ergebnis: "beside the Eb Mb state described by gMFT, the topological Mott insulator
  (EfT Mf)theta is the only state that has a simple mean field description on the pyrochlore lattice with Kramers
  spins!" Vorbehalt der Autoren: "only suggestive". [S]
  - Abschn. IX (S. 14): Wortlaut "this does not rule out the Ef Mb state, but does make it less natural in nonbipartite Kramers
    spin systems" [S].
- **V5 (neu, Levin/Wen 2003 = STRINGENDE-1-Quelle):** S. 19: "Ref. [37] constructed a rotor model in which one of the
  emergent particles is a fermion. This can be viewed as either a construction of Ef Mb or of Eb Mf depending on how
  time reversal is implemented on the microscopic rotor degrees of freedom." [37] = Levin/Wen, PRB 67, 245316 (2003)
  [S]. Folge: Ob das Stringend-Fermion "Ladung" oder "Monopol" ist, entscheidet die T-Wirkung, nicht das Modell.
- Bestaetigt (eine Zeile je): E_b M_b ist "the one constructed in most of the existing microscopic models[3, 5-9]"
  ([5] = HFB 2004) und "the state accessed by the gauge mean field theory of Ref.[11]" (Savary/Balents 2012) [S, S. 7];
  E4: "in a strictly 3d spin/bosonic system ... E and M cannot simultaneously be fermionic" mit [24] = Wang/Potter/
  Senthil, Science 343 (2014), [36] = Kravec/McGreevy/Swingle, PRD 92, 085024 (2015) [S, S. 6 und Literaturliste].
- Tabelle I am Volltext [S]: (E_fT M_f)_theta: elementare Dyonen (+-1/2, +-1) sind **Bosonen**; reine Ladung (1,0) und
  reiner Monopol (0,2) sind Fermionen, beide als Verbund zweier Dyonen.

### A3/A5 Pace/Morampudi/Moessner/Laumann 2021 (gelesen 11:18 bis 11:21)

- **V6 (gegen meine N3-Zahl):** alpha_QSI ist kein fester Wert, sondern ein Stellknopf: "tunable ranging from exactly zero
  at the RK point all the way to 0.1 at mu = -0.5"; "0.06 at zeta = -0.15 and increases to 0.2 at zeta = 1"; am
  ueblichen Punkt (mu = zeta = 0) 1/10 (Tabelle I, S. 4) [S]. Meine Erinnerung 0,08 ist durch 0,1 zu ersetzen.
- **V7 (gegen meine 50:50-Erwartung zur Obergrenze):** Die deconfined Phase reicht nach den Autoren nur bis
  alpha_c ~ 0,2 ("argued to be the limit of stability of the deconfined phase in general [5-7]", [5] = Cardy 1980),
  also weit unter dem selbstdualen Wert 1/2 [S, S. 4].
  - Folge [ES, mit Dirac m = e/(2 alpha) aus Tabelle I und PDG (94.2) S-P]: alpha_m = 1/(4 alpha_e) >= 1,25 in der ganzen
    deconfined Phase; am ueblichen Punkt alpha_m = 2,5. Das (1,1)-Dyon (theta = 0) hat alpha_e + alpha_m >= 1,45, am
    ueblichen Punkt 2,6. Das Spinon hat <= 0,2.
  - Der selbstduale Punkt (alpha = 1/2), an dem "elektrisch" und "magnetisch" gleich stark waeren, liegt ausserhalb der
    deconfined Phase. Innerhalb gibt es immer eine schwach und eine stark gekoppelte Sorte.
- **Benennung [S]:** Pace u. a., Fussnote [17] (S. 5): "we adopt the language used by the gauge theory literature where the
  spinon is called an electric charge. Our electric charge is referred to as a magnetic monopole in the classical spin
  ice literature and a spinon in the quantum spin liquid literature. Our magnetic monopole is also sometimes referred
  to as a vison". Damit drei Konventionen: CMS/BSS und Wang/Senthil (Defekt = magnetisch), HFB und Pace (Defekt =
  elektrisch).
- Bestaetigt (eine Zeile): Spinonen und Monopole leben auf Diamantgitter bzw. dessen Dualgitter (Supplement, Gl. 13 ff.,
  "photon dispersion is calculated on the dual lattice") [S]; Pace erwartet "spinon-antispinon 'Rydberg' bound states"
  (S. 4), ueber Spinon-Monopol-Bindung steht nichts.

### A4 Levin/Wen 2006, "Quantum ether" (gelesen 11:17 bis 11:18)

- Bestaetigt [S]: "The fermions correspond to endpoints of the strings that is, defects in the string liquid where a
  string ends in empty space" (S. 1); im "twisted rotor model" gilt die fermionische Huepfalgebra (Gl. 12): "We conclude
  that in the twisted rotor model the charged particles are fermions" (S. 7). Im ungedrehten Modell: "We conclude that
  the charged particles are bosons."
- Wichtiger Zusatz [S, S. 3]: "When alpha >> 1, the quantum fluctuations are so large that the gauge theory is in the
  confining phase ... The gauge bosons (such as photons) can exist at low energies only in the deconfined phase when
  alpha is small." alpha bezieht sich dort auf die Stringend-Ladungen.
- Dirac-Struktur [S, S. 9]: pi-Fluss je "doubled" Plakette; Ergebnis "QED with four species of massless Dirac
  fermions"; "the speed of light ... and the speed of the massless Dirac fermion ... are not the same ... we can tune the
  value of t to make c = c_e"; "the emergent electrons are massless" (Problem genannt).
- "monopol" kommt im Text nicht vor [S, grep].
- Folge [ES]: Im Levin/Wen-Weg ist das Elektron ein *schwach gekoppeltes* fermionisches Stringende (H1). Spin 1/2 kommt
  dort nicht aus dem Gitter, sondern aus der emergenten Dirac-Struktur, und nur mit Abstimmung (c = c_e) als Lorentz-
  Spin. Beim Dyon (H2) kommen Statistik und halbzahliger Drehimpuls gemeinsam aus der e-m-Paarung (Wang/Senthil Abschn.
  V [S]; LADUNG-MONOPOL-1/2 [E]).

### Zwischenstand Erwartungen (11:22)

- E1 teilweise: Regel an der Quelle (WS Abschn. V, relative Monopole -> Fermion, Feld-Drehimpuls 1/2); Satz fuer (1,1) in
  E_b M_b nicht im Text.
- E2 eingetroffen [S-P] (Goldhaber-Abstract, nicht neu abgerufen).
- E3 nicht an einer Quelle belegt; Projekt-Rechnung LM-1/2 [E] und Kato [ES] stuetzen "keine Bindung ohne Zusatzkraft";
  "am selben Ort" ist auf dem Gitter falsch (Diamant gegen Dualgitter) [S Pace, Supplement].
- E4 eingetroffen (WS-Wortlaut mit [24], [36]; Primaerquellen nicht gelesen).
- E5 teilweise (Feld-Drehimpuls 1/2 an der Quelle WS Abschn. V; Gitter-Doppelgruppe nur Projekt-Rechnung).
- grep "spin-statistics" in allen drei Volltexten: 0 Treffer [S]. Spin-Statistik-Verletzung fuer eine *innere*
  Symmetrie steht aber bei WS S. 7: CP^1-Spinon z ist Kramers-Dublett, "Clearly E is a Kramers boson" (E_bT M_b) [S].

## 3b. Schreibtisch nach den Abrufen (D1 bis D5, 11:22 bis 11:26)

- **D1 [ES] Invariante Fassung von H1 gegen H2.** Sei P das am schwaechsten gekoppelte Teilchen (kleinstes
  alpha = |n + m tau|^2-Groesse). Elektronartig heisst: P ist ein Fermion. Bei theta = 0 gilt fuer das (1,1)-Dyon
  alpha_11 = alpha_e + 1/(4 alpha_e) >= 1 > min(alpha_e, 1/(4 alpha_e)), denn das Minimum ist <= 1/2. Das Dyon ist also
  *bei keiner Kopplung* das am schwaechsten gekoppelte Teilchen. Elektronartig ist nur: E_f M_b mit alpha_e < 1/2 oder
  dual E_b M_f mit alpha_e > 1/2.
- **D2 [ES] QSI-Zahlen.** Pace [S]: Spinon alpha in [0; 0,2], ueblich 0,1. Dirac: Monopol 1/(4 alpha) in [1,25; unendl.),
  ueblich 2,5. Dyon (1,1): >= 1,45, ueblich 2,6. Verhaeltnis alpha_11/alpha_e = 1 + 1/(4 alpha_e^2): mindestens 7,25
  (an der Grenze 0,2), am ueblichen Punkt 26, bei alpha_e = 0,06 etwa 70.
- **D3 [ES/L] Zwei Regime zur Spannung WS gegen Pace.** WS: ohne T sind alle sieben Phasen glatt verbunden. Pace (nach
  Cardy): deconfined nur bis alpha ~ 0,2. Beides stimmt, wenn der Moderator die Kernenergie der Monopole ist: mit
  "natuerlichen" Gitterkernen endet die Coulomb-Phase vor dem selbstdualen Bereich, die Rollen schwach/stark sind dann
  fest (Regime A, QSI, Levin/Wen); mit unterdrueckten Monopolen (Monopol-Chemiepotential) reicht die Coulomb-Phase in
  den selbstdualen Bereich [L, nicht geprueft], dann ist H1 gegen H2 ohne T nur Umbenennung (Regime B, WS).
- **D4 [ES] Asymmetrie Spin gegen Statistik.** H2 (Dyon): Fermi-Statistik und halbzahliger Drehimpuls kommen gemeinsam
  aus derselben e-m-Paarung (WS Abschn. V [S]; LADUNG-MONOPOL-1/2 [E]: s = (-1)^q, G4). H1 (Stringende, Levin/Wen
  2006): Statistik aus dem Twist der Stringoperatoren, Spin 1/2 erst aus der emergenten Dirac-Struktur (pi-Fluss, 4
  Sorten, Lorentz nur abgestimmt) [S]. Fuer P4 (Spin 1/2) ist H2 der "billigere" Weg, fuer "Elektron" (schwache
  Kopplung) H1.
- **D5 [ES] Kartenidee TWIST-PYRO-1.** Levin/Wen 2006 definieren den Twist ueber eine 2D-Projektion und Rahmung,
  W~(C) = (L+ L- ...)(-1)^(Sum n_i^c L^z_i) (Gl. 8), auf dem *bipartiten* kubischen Gitter mit Q_I = (-1)^I Sum L^z
  (Gl. 1) [S]. Finns Netz ist nicht bipartit (Dreiecke) und traegt Pfeile (Spin 1/2) statt Rotoren. Ob die gedrehten
  Plakettenoperatoren dort vertauschen und die Huepfalgebra -1 gibt, ist offen: Das ist pruefbar, kann scheitern und ist
  nicht vorab abgeleitet.

## 3c. Gegensweep (Feld-Regel 4, 11:26)

| Nr | Selbstverstaendlich angenommen | geprueft? | Befund |
|---|---|---|---|
| G1 | Das Wort "Elektron" in Ue2 meint ein schwach gekoppeltes Fermion | nein (Definition) | Rueckfrage R2; ohne diese Festlegung ist H1/H2 ohne T eine Namensfrage (V2) |
| G2 | Pace' alpha und meine Dirac-Rechnung benutzen dieselben Einheiten | **ja** (Tabelle I, S. 4) | ja: alpha = e^2/hbar c, Coulomb e^2/r, m = e/(2 alpha), also alpha_m = 1/(4 alpha) [S + ES] |
| G3 | Aussagen ueber Quanten-Spin-Eis (Spins auf Pyrochlor-*Ecken*, 2 rein/2 raus) gelten fuer Finns Netz (Pfeile auf Pyrochlor-*Kanten*, 3 rein/3 raus) | nein | offen, wie LADUNG-MONOPOL-L G6; alle QSI-Zahlen sind fuer Finns Netz [H] |
| G4 | "alpha_c ~ 0,2 allgemein" ist eine Messung | **ja** (Wortlaut) | nein: "has been argued" (S. 4), gestuetzt auf Cardy 1980; gemessen ist nur das QSI-Modell (zeta ~ 1). Gegenregime mit unterdrueckten Monopolen nur [L] |
| G5 | Die Spin-Eis-T-Konvention (Pfeile T-ungerade) gilt fuer Finns Pfeile | nein | Finns Pfeile haben keine festgelegte T-Wirkung; ohne T ist E/M ohnehin Konvention (V2) |
| G6 | Das Dyon ist ein Teilchen (gebunden) | ja (Projekt) | nein, nicht von selbst: LADUNG-MONOPOL-1/2 ohne Topf keine Bindung [E]; die Statistik des (1,1)-Sektors gilt trotzdem (Goldhaber: zwei "clusters") |
| G7 | Fuer die Statistikregel spielt theta keine Rolle | Schreibtisch | ja, die Paarung n m' - m n' haengt nicht von theta ab; theta verschiebt nur Ladungen (Witten-Effekt) [ES] |

## 4. Offene Rueckfragen (wandern mit)

- R1 (aus LADUNG-MONOPOL-L, weiter offen): "Monopol" in H2 = Defekt des konjugierten Feldes, nicht FLUSS-1-Defekt.
- R2 (neu, an die Leitung): Soll "Elektron" in Ue2 heissen "schwach gekoppeltes Fermion mit Einheitsladung" (dann
  zaehlt N3) oder nur "irgendein Fermion mit U(1)-Ladung" (dann ist N2 massgeblich und H1/H2 Namensfrage)?

## 5. Gestrichen


## 3d. Abruf A7 (Nachtrag im Abrufprotokoll-Format)

| Nr | Zeit (date) | Ziel | Erwartung vor Abruf | Ausgang | Verstoss? |
|---|---|---|---|---|---|
| A7 | vor 11:26 | arXiv:1905.03276, PDF (Ning/Zou/Cheng, Volltext; Nummer aus A6) | Regel fuer die Symmetrie-Fraktionalisierung eines Dyons: Phase von (q_e, q_m) = q_e-Anteil mal q_m-Anteil mal ein Zusatz aus der gegenseitigen e-m-Paarung; fuer Drehungen (bzw. 2-pi-Drehung) ein Faktor (-1)^(q_e q_m), d. h. Spin-Statistik fuer das Dyon; Gitterdrehungen eher nur ueber "kristallines Aequivalenzprinzip" erwaehnt | | |

### Ausgang A7 (11:25:22 bis 11:25:23 curl; gelesen bis 11:27), arXiv:1905.03276v3, 31 S., lokal quellen/arxiv-1905.03276.pdf

- **V8 (E1 an der Quelle eingetroffen, aber bei Ning/Zou/Cheng, nicht bei Wang/Senthil):**
  - S. 6: "Suppose that the matter is generated by a particular dyon (qe, qm) ... We will further assume that
    (-1)^(qe qm) = 1, so the dyon is bosonic." Das ist die Regel (-1)^(q m) fuer bosonisches E und M woertlich [S].
  - S. 3: "the T^n transformation changes the statistics of particles for odd n (e.g., a bosonic charge (1, 0) turns
    into a fermionic dyon (n, 1))" [S]. (Die Matrixkonvention fuer T ist dort nicht eindeutig zu der Klammer; die
    Aussage "(n,1) bei ungeradem n fermionisch" ist eindeutig.)
- **V9 (stark, gegen die Lesart der Leitung "Dyon ist kein Elektron"):** S. 14, Abschn. "Fermionic insulators": Ein
  geeichter fermionischer Isolator (fermionische Eichladungen, also "Elektronen") wird umgeschrieben: "we first apply a
  T transformation so that the electric charge is bosonic. In other words, we may view the fermionic topological
  insulator as the result of 'ungauging' the (1, 1) dyon in a U(1) gauge theory with bosonic electric charge";
  "we assume that the fermion (1, 1) transforms linearly" [S].
  - Folge: Auf der Ebene der universellen Daten (Statistik, Symmetriedarstellung) *ist* ein Elektron dasselbe wie das
    (1,1)-Dyon einer Theorie mit bosonischer Ladung; nur die Benennung aendert sich. NZC sagen dazu ausdruecklich (S. 3):
    "In defining automorphisms we ignore energetics such as gaps of the particles." [S]
  - Korrektur meiner Lage: Die Leitungslesart ist als *topologische* Aussage falsch; haltbar ist sie nur ueber Energetik
    und Kopplung (D1, D2), also im Regime A (D3).
- **Bestaetigt (eine Zeile):** S. 6: "In the absence of any orientation-reversing symmetry, M will always be taken as a
  boson, because this can be achieved by smoothly tuning theta to be 0. On the other hand, in the presence of a
  orientation-reversing symmetry ... the statistics of M is a robust universal feature" [S]; S. 3: "If theta = 2 pi N
  with N even (odd), the elementary charge-neutral monopole is bosonic (fermionic)" [S]. Deckt V2 und N2.
- Nicht gefunden: Gitter-Drehungen oder Spin-Statistik (Z. 829 "rotation" meint die U(1)-Drehung R_theta) [S, grep].
- Abrufzaehler: 7 von 10 (A1 bis A7). Keine weiteren Abrufe geplant (Zeitbox).

### Zwischenstand Erwartungen (11:27, nach A7)

- E1 **eingetroffen** in der Sache und im Wortlaut (NZC S. 6, (-1)^(qe qm); S. 3 und S. 14 "fermionic dyon"/"the fermion
  (1,1)"); bei Wang/Senthil nur die Regel fuer theta = pi (V3).
- E2 eingetroffen [S-P]. E3 nicht an einer Quelle belegt. E4 eingetroffen (ueber WS-Zitat). E5 teilweise.

## 4b. Offene Rueckfragen (Stand Abgabe; wandern ins Dossier, Abschnitt 11)

- R1 (alt): "Monopol" in H2 = Defekt des konjugierten Feldes; nach diesem Stand ja.
- R2 (neu): Bedeutung von "Elektron" in Ue2 (schwach gekoppelt oder nur Fermion mit Ladung).
- R3 (neu, aus Gegensweep G3): Welche Lesart von "Finns Netz" gilt fuer Ue2, Diamant-Kanten (= Quanten-Spin-Eis) oder
  Pyrochlor-Kanten (FLUSS-1)?

## 5b. Gestrichen (Nachtrag)

- ~~"Dyon bei E_b M_b ist Fermion" nur [ES aus Goldhaber]~~ (LADUNG-MONOPOL-L): jetzt [S], NZC S. 6 und 14.
- ~~Woerterbuch LADUNG-MONOPOL-L: "Quelle des Kantenfeldes = E in Wang/Senthil"~~: bei Wang/Senthil M (S. 2, Fussn. 3).
- ~~N3-Zahl 0,08~~: 0,1 (siehe Abschnitt 1, N3).

## 6. Abgabe

- DOSSIER.md geschrieben ab 11:27:44 CEST; Rueckwaertslesung der Zahlen und Seitenzahlen 11:29 bis 11:31 (Seiten per
  pdftotext je Seite geprueft; NZC grep "spin-statistics": 0 Treffer); Berichtigungen: Science-Zitat (Seitenzahl nicht
  geprueft), Kennzeichen [S]/[ES] bei den Dyon-Zahlen, "M_f" nur bei theta = 0 (Mott-Isolator: elementare Dyonen
  bosonisch).
- Keine Peerbus-Nachricht, kein Commit, kein Journaleintrag, keine Aenderung an Dateien ausserhalb des Kartenordners.
