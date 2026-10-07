# DYON-STATISTIK-L: Dossier (Literaturkarte, Runde 39)

- Feldforscher fuer die Leitung claude-primary. Start 2026-10-04 11:06:02 CEST, Dossier geschrieben ab 11:27:44 CEST
  (alle Zeiten per date). Arbeitsstand, Abrufprotokoll und Erwartungen vor jedem Abruf: ARBEITSFELD.md (gleicher Ordner).
- 7 von 10 Abrufen verbraucht (curl, lokale Kopien in quellen/), keine Websuche, keine Rechnung, lokal kein Interpreter.
- **Kennzeichen:**
  - [S] an der Quelle selbst gelesen (lokale Kopie, pdftotext und grep; Seitenzahl der PDF-Fassung)
  - [S-P] im Projekt schon an der Quelle gelesen, hier nicht erneut abgerufen
  - [P] Projektdatei; [E] Projekt-Rechnung (synthetisch)
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher
  - [ES] eigener Schluss; [H] Hypothese

## 0. Kurzfazit

- Das Dyon (1,1) aus bosonischer Ladung und bosonischem Monopol ist ein Fermion mit halbzahligem Feld-Drehimpuls [S].
- Ohne Zeitumkehr ist "Fermion = Dyon" gegen "Fermion = reine Ladung" nur eine Benennung; ein Elektron *ist*
  topologisch ein (1,1)-Dyon in anderer Benennung [S]. "Kein Elektron, weil magnetisch geladen" traegt daher nicht.
- Physikalisch trennt die Kopplung an das Licht: Das Dyon hat bei theta = 0 immer alpha >= 1, im Quanten-Eis >= 1,45
  gegen <= 0,2 fuer die einfache Ladung [ES aus S]. Als schwach gekoppeltes "Elektron" taugt es nicht.
- Ein elektronartiges Fermion verlangt dann ein fermionisches Pfeilende, H1 [ES]; gebaut ist das im Levin/Wen-Modell
  mit gedrehten Strings [S]. Das Spin-Eis liegt nahe dem Eis-Grenzfall in E_b M_b (H2) [S]; ob Finns Netz den Twist
  tragen kann, prueft TWIST-PYRO-1.
- Groesste Abweichung vom Projektstand: Wang/Senthil nennen die Eisdefekte *magnetisch*; das Woerterbuch von
  LADUNG-MONOPOL-L ist in dieser Spalte zu berichtigen [S].

## 1. Ergebnis zuerst

1. **Ja, das Dyon (1,1) aus bosonischer Ladung und bosonischem Monopol ist ein Fermion; das steht jetzt an der Quelle**
   [S]:
   - Ning/Zou/Cheng 2020, S. 6: "(-1)^(qe qm) = 1, so the dyon is bosonic", also Fermion bei ungeradem qe qm. S. 14:
     "the fermion (1, 1)" in einer Theorie "with bosonic electric charge".
   - Wang/Senthil 2016, S. 7: Zwei Teilchen, die sich gegenseitig als Monopol sehen, binden zu einem Fermion; der
     Drehimpuls des Feldes ist "quantized to be 1/2". Dort ausgefuehrt nur fuer theta = pi, nicht woertlich fuer E_b M_b.
2. **Ohne Zeitumkehr ist "Dyon gegen reine Ladung" keine Phasenfrage** [S]:
   - Wang/Senthil, S. 3: "If this symmetry were absent then it is possible to go smoothly between any two of these
     phases." Fussnote 3, S. 6: Was elektrisch und was magnetisch heisst, "is a matter of convention".
   - Ning/Zou/Cheng, S. 14, schreiben einen geeichten Isolator aus *Elektronen* selbst um, als "(1, 1) dyon in a U(1)
     gauge theory with bosonic electric charge".
   - Topologisch (Statistik, Symmetrie) ist das Dyon also ein Elektron in anderer Benennung. Die Lesart der Leitung
     "Dyon ist Fermion, aber kein Elektron" ist **so nicht haltbar**.
3. **Haltbar wird sie ueber die Kopplung an das Licht** [ES aus S]:
   - Dirac: alpha_e mal alpha_m = 1/4. Das (1,1)-Dyon hat bei theta = 0 alpha_e + 1/(4 alpha_e) >= 1. Damit ist es bei
     *keiner* Kopplung das am schwaechsten gekoppelte Teilchen.
   - Im Quanten-Spin-Eis (Pace u. a. 2021, S. 4):
     - Spinon: alpha <= 0,2, ueblich 0,1 [S]
     - Dyon: alpha >= 1,45, ueblich 2,6 [ES, aus diesen Werten und Dirac]
   - Ein elektronartiges Fermion (schwach gekoppelt) verlangt, dass das schwach gekoppelte Stringende *selbst* ein
     Fermion ist. Das ist H1, im Levin/Wen-Modell "Quantum ether" (2006) mit gedrehten Stringoperatoren [S].
4. **Natuerliche Phase des Quanten-Spin-Eises auf Pyrochlor** (Wang/Senthil, S. 19) [S]:
   - E_b M_b im Spin-Eis-Grenzfall (gMFT), sonst der topologische Mott-Isolator (E_fT M_f)_theta.
   - E_f M_b, E_b M_f und E_bT M_f gelten fuer Kramers-Spins auf dem nicht-bipartiten Pyrochlor als "unlikely".
   - Wichtig: Wang/Senthil nennen die Eisdefekte *magnetisch* (S. 2). Die Pfeilquelle ist dort M, H1 waere dort bei
     theta = 0 "M_f" (E_b M_f oder E_bT M_f, beide "unlikely").
5. **Spin 1/2:** Beim Dyon kommen Statistik und halber Drehimpuls aus derselben e-m-Paarung (Wang/Senthil S. 7 [S];
   LADUNG-MONOPOL-1/2 [E]). Beim Stringend-Fermion kommt der Spin erst aus der emergenten Dirac-Struktur: 4 Sorten,
   gleiche Geschwindigkeit nur abgestimmt (Levin/Wen 2006, S. 9) [S]. Eine Gitter-Doppelgruppe fuer Dyonen habe ich
   an keiner Quelle gelesen.
6. **Kartenvorschlag TWIST-PYRO-1** (Abschnitt 8): Laesst sich der Levin/Wen-Twist auf Finns Netz uebertragen? Teil A
   auf dem Diamantnetz (bipartit, das ist das Spin-Eis-Gitter), Teil B auf den Pyrochlor-Kanten (nicht bipartit,
   FLUSS-1). Teil B kann scheitern und ist nicht vorab abgeleitet.

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

1. **V9, gegen die Lesart der Leitung: Ein Elektron ist topologisch dasselbe wie das (1,1)-Dyon** [S].
   - Ning/Zou/Cheng, S. 14: "we first apply a T transformation so that the electric charge is bosonic. In other
     words, we may view the fermionic topological insulator as the result of 'ungauging' the (1, 1) dyon in a U(1) gauge
     theory with bosonic electric charge."
   - Dieselben Autoren, S. 3: "In defining automorphisms we ignore energetics such as gaps of the particles."
   - Folge: "Dyon kein Elektron" kann nur ueber Energetik und Kopplung begruendet werden, nicht ueber "es traegt
     magnetische Ladung" (Abschnitt 7.2).
2. **V1, gegen das Woerterbuch von LADUNG-MONOPOL-L: Bei Wang/Senthil sind die Eisdefekte magnetische Monopole** [S].
   - S. 2: "Defect configurations in the spin ice manifold such as a '3-in 1-out' tetrahedron ... are then identified
     with magnetic monopoles"; im Quanten-Eis "Magnetic monopoles (the defect tetrahedra) are now gapped quasiparticle
     excitations". S. 14: "the magnetic flux loops are very easy to picture".
   - Grund: ihre Konvention "the magnetic charge is time reversal odd" (Fussnote 3, S. 6); S^z ist T-ungerade.
   - Pace u. a. (Fussnote 17, S. 5) benennen dieselbe Anregung umgekehrt: "the spinon is called an electric charge".
   - Berichtigung: In LADUNG-MONOPOL-L/DOSSIER.md, Abschnitt 5, Zeile "Quelle des Kantenfeldes", ist "E in
     Wang/Senthil" falsch. Richtig ist M in Wang/Senthil, E bei HFB und Pace.
3. **V2, gegen den Rahmen der Karte (H1 gegen H2 als zwei Phasen)** [S]:
   - Wang/Senthil, S. 3: "the distinction between these phases is entirely a consequence of the unbroken time reversal
     symmetry. If this symmetry were absent then it is possible to go smoothly between any two of these phases."
   - Ning/Zou/Cheng, S. 6: Ohne orientierungsumkehrende Symmetrie "M will always be taken as a boson, because this can
     be achieved by smoothly tuning theta to be 0".
4. **V7 und V6: Die Obergrenze der deconfined Phase liegt bei alpha ~ 0,2, nicht beim selbstdualen 1/2** [S].
   - Pace u. a., S. 4: "alpha_c ~ 0.2 ... has been argued to be the limit of stability of the deconfined phase in
     general"; "0 <= alpha <= 0.2"; Tabelle I: alpha_QSI = 1/10.
   - Erwartet hatte ich 0,08 und eine offene Obergrenze (Wilson-Wert oder 1/2).
   - Folge: Im Quanten-Spin-Eis sind die Rollen fest. Das Spinon ist schwach gekoppelt, alles mit magnetischer Ladung
     stark (alpha_m >= 1,25). Das stuetzt die *Schlussfolgerung* der Leitung, mit anderer Begruendung.
5. **V3 (Wang/Senthil) und V8 (Ning/Zou/Cheng): Der Dyon-Satz steht nicht dort, wo erwartet** [S].
   - Wang/Senthil zitieren Goldhaber nicht und schreiben den Satz fuer E_b M_b nicht aus. Die Regel steht dort nur fuer
     die Dyonen bei theta = pi (S. 7).
   - Woertlich steht sie bei Ning/Zou/Cheng (S. 6 und 14).
6. **V4 und V5, neu: Pyrochlor-Phasen und Einordnung von Levin/Wen 2003** [S].
   - Wang/Senthil, S. 19: E_b M_b sei "justified only deep in the spin ice limit". Fuer Kramers-Spins auf nicht-bipartiten
     Gittern seien "fermionic monopoles or non-Kramers fermionic electric charges" unnatuerlich.
   - Wang/Senthil, S. 19, zur Quelle von STRINGENDE-1: "Ref. [37] constructed a rotor model in which one of the emergent
     particles is a fermion. This can be viewed as either a construction of Ef Mb or of Eb Mf depending on how time
     reversal is implemented". [37] = Levin/Wen, PRB 67, 245316 (2003).

## 3. Erwartungen mit Ausgang

| Nr | Erwartung (Karte, vor jedem Abruf) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | Wang/Senthil, Abschn. V oder Tabelle: In E_b M_b ist das Dyon (1,1) ein Fermion; Faktor (-1)^(q m) | **in der Sache eingetroffen, Ort falsch** | Ning/Zou/Cheng, PRR 2, 043043 (2020), arXiv:1905.03276v3, S. 6: "(-1)^(qe qm) = 1, so the dyon is bosonic"; S. 3: "(e.g., a bosonic charge (1, 0) turns into a fermionic dyon (n, 1))" fuer ungerades n; S. 14: "the fermion (1, 1)" [S]. Wang/Senthil, arXiv:1505.03520v2, S. 7: Regel nur fuer theta = pi ("relative monopoles ... Fermi statistics of their bound state", Feld-Drehimpuls "quantized to be 1/2"); kein ausdruecklicher E_b M_b-Satz, keine Goldhaber-Zitation [S] |
| E2 | Goldhaber 1976: spinlose Ladung + spinloser Monopol, ungerades q m: halbzahliger Drehimpuls, Fermi-Statistik | **eingetroffen** (nicht neu abgerufen) | PRL 36, 1122, Abstract: "may bear net half-integer spin", "the wave function of two such clusters must be symmetric under their interchange" (in naiven Koordinaten), die Relativbewegung "implies the usual connection between spin and statistics" [S-P, LADUNG-MONOPOL-L A4; SPIN1.md E4] |
| E3 | Im Quanten-Spin-Eis keine langreichweitige Kraft zwischen Ladung und Monopol; Dyon = beide am selben Ort, ohne eigene Bindung; Stabilitaet modellabhaengig | **nicht an einer Quelle belegt; ein Teil falsch** | Keine Quelle zur Spinon-Monopol-Bindung gelesen. Pace u. a. erwarten nur "spinon-antispinon 'Rydberg' bound states" (S. 4) [S]. "Am selben Ort" ist auf dem Gitter falsch: Ladungen sitzen auf dem Diamantgitter, Monopole auf dem Dualgitter (Pace, Supplement: Photon "calculated on the dual lattice") [S]. "Ohne Zusatzkraft keine Bindung": LADUNG-MONOPOL-1/2 [E], Kato [ES] |
| E4 | "All-fermion electrodynamics" ist in einem strikt 3D-Bosonen-Gittermodell nicht moeglich (Wang/Potter/Senthil 2014; Kravec/McGreevy/Swingle 2015) | **eingetroffen** (ueber Zitat) | Wang/Senthil, S. 6: "in a strictly 3d spin/bosonic system (as opposed to systems that can only appear the boundary of a 4 + 1 dimensional system) ... E and M cannot simultaneously be fermionic", mit [24] Wang/Potter/Senthil, Science 343 (2014), und [36] Kravec/McGreevy/Swingle, PRD 92, 085024 (2015) [S]. Primaerquellen nicht gelesen |
| E5 | Halber Spin des Dyons aus dem Feld-Drehimpuls; auf dem Gitter projektive Darstellung der Punktgruppe | **teilweise** | Feld-Drehimpuls 1/2: Wang/Senthil S. 7 [S]; PDG 2025, Gl. (94.3) [S-P, SPIN1.md]. Gitter-Doppelgruppe: nur Projekt-Rechnung (LADUNG-MONOPOL-1: s = (-1)^q; LADUNG-MONOPOL-2: G4) [E]. In Ning/Zou/Cheng meint "rotation" nur die U(1)-Drehung (S. 6) [S]. grep "spin-statistics" in vier Volltexten: 0 Treffer |

## 4. Literaturstand (kurz)

- **Klassifikation mit Zeitumkehr** (Wang/Senthil, PRX 6, 011034, 2016; arXiv:1505.03520v2) [S]:
  - sieben Familien (Tabelle I, S. 3), Unterschied "entirely a consequence of the unbroken time reversal symmetry"
  - Regel fuer gebundene relative Monopole (S. 7)
  - Pyrochlor-Kandidaten E_b M_b und (E_fT M_f)_theta (S. 19)
  - Das Schwinger-Bosonen-Spinon ist ein "Kramers boson" (S. 7): Ein emergentes Boson mit halbzahliger innerer
    Darstellung ist erlaubt.
- **Symmetrie-Fraktionalisierung allgemein** (Ning/Zou/Cheng, PRR 2, 043043, 2020; arXiv:1905.03276v3) [S]:
  - Dyon-Statistik (-1)^(qe qm) (S. 6)
  - Ohne orientierungsumkehrende Symmetrie ist theta frei; die Statistik des neutralen Monopols ist dann nicht
    universell (S. 3, 6)
  - Elektron = (1,1)-Dyon nach T-Umbenennung (S. 14)
- **Quanten-Spin-Eis-Kopplung** (Pace/Morampudi/Moessner/Laumann, PRL 127, 117205, 2021; arXiv:2009.04499v2) [S]:
  - alpha_QSI = 1/10 am ueblichen Punkt, einstellbar von 0 bis ~0,2, dort Einschluss (S. 4)
  - Monopolladung aus Dirac "m = e/2 alpha" (Tabelle I)
  - Benennung Spinon = elektrisch (Fussnote 17)
- **Levin/Wen, "Quantum ether"** (PRB 73, 035122, 2006; arXiv:hep-th/0507118v2) [S]:
  - bosonisches Rotormodell auf dem kubischen Gitter, Fermionen sind Stringenden (S. 1)
  - ungedreht Bosonen (S. 4), gedreht Fermionen (Gl. 12, S. 7)
  - Photonen nur bei kleinem alpha (S. 3)
  - vier Sorten Dirac-Fermionen, c = c_e nur abgestimmt (S. 9)
  - Monopole kommen im Text nicht vor
- **Weitere Treffer, nur Abstract** [S]:
  - Zou/Wang/Senthil, PRB 97, 195126 (2018), arXiv:1710.00743: mit T und SO(3) 15 Phasen, 11 anomale
  - Li/Chen, PRB 95, 041106 (2017), arXiv:1607.02287: Dipol-Oktupol-Pyrochlor, zwei U(1)-Phasen
- **Aus dem Projekt** [S-P]: Goldhaber 1976; Jackiw/Rebbi und Hasenfratz/'t Hooft 1976; MKF 2013 (statistischer
  Witten-Effekt); HFB 2004 (Abstract); Levin/Wen 2003 (Volltext, STRINGENDE-1); PDG 2025, Rev. 94.

## 5. Regime und Moderatoren (Feld-Regel 1)

| Moderator | Regime A | Regime B | Beleg |
|---|---|---|---|
| Zeitumkehr (bzw. Spiegelung) | vorhanden: sieben Familien, theta = 0 oder pi gepinnt, Statistik von M universell | fehlt: alle Familien glatt verbunden; E/M ist Konvention | WS S. 3, Fussn. 3; NZC S. 6 [S] |
| T-Paritaet des Pfeilfeldes | T-ungerade (Spins): Pfeilquelle heisst bei WS M | T-gerade: Pfeilquelle heisst E | WS S. 2, Fussn. 3 [S]; Finns Pfeile: T-Wirkung nicht festgelegt [ES] |
| Kopplung der Pfeilquelle | alpha <= 0,2 (deconfined, QSI): Rollen schwach/stark fest, Dyon >= 1,45 | nahe selbstdual (alpha ~ 1/2): Unterschied "elektrisch/magnetisch" schwindet, Dyon bleibt >= 1 | Pace S. 4 [S]; LW S. 3 [S]; Dirac [ES] |
| Kernenergie der Monopole | natuerliche Gitterkerne: Einschluss ab alpha ~ 0,2, kein glatter Weg durch den selbstdualen Bereich | unterdrueckte Monopole: Coulomb-Phase reicht weiter, WS-Glattheit erreichbar | Pace S. 4 ("has been argued") [S]; Regime B nur [L], nicht geprueft |
| Abstand vom Spin-Eis-Grenzfall | nahe: E_b M_b (gMFT) | fern: (E_fT M_f)_theta moeglich | WS S. 19 [S] |
| Kramers oder nicht | Kramers, nicht bipartit: fermionische Monopole und nicht-Kramers-Fermion-Ladungen "unnatural" | Nicht-Kramers: das Argument greift so nicht | WS S. 14, 19 [S] |
| Stringoperator | ungedreht: Stringenden Bosonen | gedreht: Stringenden Fermionen | LW S. 4, S. 7 [S]; STRINGENDE-1 [E] |
| Gitter von Finns Netz | Diamant-Kanten (= Spin-Eis-Gitter, bipartit): Literatur gilt direkt | Pyrochlor-Kanten (FLUSS-1, nicht bipartit): alles [H] | LADUNG-MONOPOL-L Abschn. 5 [P]; Gegensweep G3 |

- **Feld-Regel 6 (Kopplung vor Bauteil) [ES]:** Die gemeinsame Groesse ist die Dirac-Paarung qe qm' - qm qe'. Aus ihr
  folgen das Minuszeichen der Statistik (NZC S. 6), der Feld-Drehimpuls 1/2 (WS S. 7) und die Kopplungsschranke
  alpha_e alpha_m = 1/4. Statistik, Spin und "Elektron oder nicht" sind drei Ablesungen derselben Groesse. Das
  Bauteil (Dyon oder Stringende) ist es nicht.

## 6. Unterscheidungspunkte (Feld-Regel 2)

| Erklaerungspaar | Wo sie messbar auseinanderlaufen | Zugang |
|---|---|---|
| H1 (Pfeilquelle selbst Fermion) gegen H2 (Fermion = Dyon), Benennung durch das Gitter festgelegt | (a) Statistik der elementaren Pfeilquelle: -1 gegen +1. (b) Kopplung des leichtesten Fermions an das Licht: H1 <= 0,2, H2 >= 1,45 im QSI-Bereich. (c) Monopolfluss durch eine Huelle um das Fermion: 0 gegen 2 pi/e | im Modell messbar: (a) Huepfalgebra wie LW Gl. 12 bzw. STRINGENDE-1; (b) Energie der Topologie-Sektoren wie bei Pace; (c) Zaehlen der Monopole |
| Leitungslesart "Dyon kein Elektron" gegen Gegenlesart "Dyon = Elektron in anderer Benennung" (NZC S. 14) | Nicht in Statistik oder Symmetrie: Dort sind beide gleich, empirisch nicht unterscheidbar. Nur in Energetik und Kopplung: Bei theta = 0 ist das Dyon mit alpha >= 1 nie das am schwaechsten gekoppelte Teilchen | Kopplungsmessung; im QSI-Bereich eindeutig fuer die Leitung |
| Wang/Senthil "ohne T glatt verbunden" gegen Pace "deconfined nur bis 0,2" | im selbstdualen Bereich alpha ~ 1/2: dort bei natuerlichen Kernen Einschluss, bei unterdrueckten Monopolen Coulomb | im QSI-Modell unzugaenglich (alpha <= 0,2 gemessen); nur in Modellen mit Monopol-Chemiepotential [L] |
| E_b M_b gegen (E_fT M_f)_theta im Quanten-Spin-Eis | Statistik und Kramers-Eigenschaft der reinen elektrischen Ladung (Boson gegen Kramers-Fermion); Oberflaechenzustaende | WS S. 7, 19 [S]; Materialfrage offen |

## 7. Projektbezug

### 7.1 Welche Phase hat ein Pfeil-Eis auf Finns Netz natuerlich?

- **Diamant-Lesart** (Pfeile auf den Kanten des Tetraederknoten-Netzes = Spins auf Pyrochlor-Ecken = Quanten-Spin-Eis):
  Nahe dem Spin-Eis-Grenzfall ist E_b M_b die gMFT-Phase. Dort sind Pfeilquelle und Monopol Bosonen, das Fermion ist
  das Dyon (H2) [S, WS S. 19; Benennung WS S. 2]. Fern davon (Kramers-Spins) ist der topologische Mott-Isolator der
  einzige weitere einfache Kandidat [S]. H1 hiesse in WS-Kuerzeln bei theta = 0 "M_f" (E_b M_f, E_bT M_f); beide gelten
  fuer Kramers-Spins als "unlikely" [S]. Im Mott-Isolator ist der reine Monopol (0, 2) zwar ein Fermion, die elementaren
  Anregungen mit q_m = 1 sind aber die Dyonen (+-1/2, +-1), und die sind Bosonen (WS Tabelle I) [S]. Ob ein Eisdefekt
  dort einem solchen Dyon entspricht, habe ich nicht gelesen [offen].
- **Pyrochlor-Kanten-Lesart** (FLUSS-1, LADUNG-MONOPOL-2): Keine gelesene Quelle behandelt dieses Gitter. Uebertragung
  ist [H] (Gegensweep G3, LADUNG-MONOPOL-L O1).
- **Mit einfachen Pfeilen** (ungedrehte Stringoperatoren) sind Stringenden Bosonen (LW S. 4 [S]; Pauli-Algebra [ES]).
  H1 braucht eine besondere Bauweise: den LW-Twist bzw. die Knotenstruktur aus STRINGENDE-1. Ohne sie liegt das Netz,
  falls es eine Coulomb-Phase hat, im H2-Regime [ES].
- **Der Weg zu H1 steht schon im Projekt** [S]: Levin/Wen 2003 (STRINGENDE-1) ist nach WS S. 19 "either a construction of
  Ef Mb or of Eb Mf depending on how time reversal is implemented".

### 7.2 Taugt das Dyon als "Elektron"? Beide Lesarten

- **Lesart A (Leitung): "Fermion, aber kein Elektron".**
  - Gestuetzt [ES aus S]: Im Quanten-Spin-Eis koppelt das Dyon mindestens 7,25-mal, am ueblichen Punkt 26-mal staerker
    an das Licht als das Spinon (Verhaeltnis 1 + 1/(4 alpha_e^2); alpha aus Pace S. 4).
  - Das reale Elektron hat alpha = 1/137. Ein Fermion mit alpha >= 1 ist nicht elektronartig.
  - Allgemein [ES]: Bei theta = 0 ist das (1,1)-Dyon bei keiner Kopplung das am schwaechsten gekoppelte Teilchen.
- **Lesart B (Gegenlesart): "Das Dyon ist ein Elektron in anderer Benennung".**
  - Gestuetzt [S]: WS Fussnote 3 (E/M Konvention); WS S. 3 (ohne T glatt verbunden); NZC S. 14 (Elektron-Isolator als
    (1,1)-Dyon einer Theorie mit bosonischer Ladung).
  - Statistik, Symmetriedarstellung und halbzahliger Drehimpuls des Dyons sind die eines Elektrons.
- **Urteil [ES]:**
  - Die Begruendung der Leitung ("es traegt magnetische Ladung") ist keine invariante Begruendung. Magnetische Ladung
    ist relativ zur Wahl, welches Teilchen elektrisch heisst.
  - Invariant ist: *Ist das am schwaechsten an das Licht gekoppelte Teilchen ein Fermion?* Im Regime A (deconfined,
    natuerliche Kerne, QSI) ist das bei E_b M_b nicht so. Dann ist das Dyon ein stark gekoppeltes Fermion und kein
    elektronartiges.
  - Fuer ein elektronartiges Fermion braucht es die Phase, in der die schwach gekoppelte Pfeilquelle selbst Fermion ist:
    "E_f" in der HFB/Pace-Benennung, "M_f" in der WS-Benennung fuer T-ungerade Pfeile, Levin/Wen 2006 im Gitter.
  - Rueckfrage R2: Welche Bedeutung hat "Elektron" in Ue2?
- **Vorschlag fuer den Ue2-Ueberleitungssatz [ES]:** "Elektronen die Enden offener Faeden" gilt nur fuer *gedrehte*
  Faeden. Mit einfachen Pfeilen sind die Fermionen Dyonen und koppeln stark an das Licht.

### 7.3 Spin 1/2 unter Drehungen

- **H2 (Dyon):** Statistik und halbzahliger Drehimpuls kommen gemeinsam, aus der Paarung (WS S. 7 [S]; Goldhaber [S-P]).
  Auf dem Gitter zeigt das die Projekt-Rechnung (LADUNG-MONOPOL-1: s = (-1)^q; LADUNG-MONOPOL-2: G4) [E]. Eine
  Literaturstelle zur Punktgruppe habe ich nicht gelesen.
- **H1 (Stringende):** Die Statistik kommt aus dem Twist (LW Gl. 12 [S]). Spin 1/2 kommt erst aus der emergenten
  Dirac-Struktur (pi-Fluss, vier Sorten, c = c_e nur abgestimmt; LW S. 9 [S]).
- **Verletzbarkeit:** Fuer innere Symmetrien ist Spin-Statistik bekannt verletzbar: "Clearly E is a Kramers boson"
  (WS S. 7) [S]. Fuer Gitterdrehungen habe ich keine Quelle gelesen. Ich erwarte dasselbe, weil diskrete Drehungen wie
  innere Symmetrien wirken [L?].
- **Folge [ES]:** Fuer P4 ist H2 der Weg mit Spin 1/2 "gratis", fuer "Elektron" (schwache Kopplung) H1. Kein Weg liefert
  im Projekt beides zugleich, ausser einer Phase mit schwach gekoppelter fermionischer Pfeilquelle *und* emergenter
  Lorentz-Symmetrie [H].

### 7.4 Berichtigungen fuer andere Projektdateien (nur benannt, nicht geaendert)

- LADUNG-MONOPOL-L/DOSSIER.md, Abschn. 5, Zeile "Quelle des Kantenfeldes": "E in Wang/Senthil" ist zu ersetzen durch "M
  in Wang/Senthil (Defekt = magnetischer Monopol, S. 2; T-ungerade, Fussn. 3)" [S].
- LADUNG-MONOPOL-L, Zeile "Dyon ... bei E_b M_b ein Fermion [ES aus Goldhaber S]": jetzt [S] (NZC S. 6 und 14).
- LADUNG-MONOPOL-L, Regime-Tabelle "E_b M_b: reine Ladung Boson, Dyon Fermion gegen E_f M_b": gilt nur mit
  Zeitumkehr oder bei festgelegter Kopplung (V2, V9).

## 8. Vorschlag: Rechenkarte TWIST-PYRO-1

**Frage:** Laesst sich der Levin/Wen-Twist (gedrehte Stringoperatoren, Fermionen als Stringenden) auf Finns Netz
uebertragen? Teil A auf dem Diamantnetz (bipartit, Quanten-Spin-Eis-Gitter), Teil B auf den Pyrochlor-Kanten (nicht
bipartit, FLUSS-1).

- **Modell:**
  - Pfeile als Spin 1/2 auf den Kanten, periodische Zellen (Diamant 2 x 2 x 2 und 3 x 3 x 3 kubische Zellen; Pyrochlor
    1 x 1 x 1 und 2 x 2 x 2)
  - Ladung Q_I = rein - raus je Knoten (orientierte Kanten statt LW-Staffelung (-1)^I)
  - Stringoperator W(C) = Produkt der sigma^+/sigma^- entlang C
  - gedreht: W~(C) = W(C) mal Produkt von sigma^z ueber die Kanten, die die Rahmung C' kreuzen (LW Gl. 8, Projektion
    auf eine Ebene, drei Projektionsrichtungen)
- **Messgroessen (exakt, ganzzahlig, wie STRINGENDE-1):**
  - T1: Vertauschen alle gedrehten kleinsten Schleifenoperatoren paarweise und mit allen Q_I? (Diamant: Sechsecke;
    Pyrochlor-Kanten: Dreiecke und Sechsecke)
  - T2: Vorzeichen der Huepfalgebra nach LW Gl. (12) fuer alle geordneten Kantentripel an einem Knoten (Diamant 24,
    Pyrochlor-Kanten 120)
  - T3, Kontrolle: ungedreht, Vorzeichen +1
  - T4, Kontrolle: kubisches Gitter mit LW-Projektion (Nachbau der Quelle), Vorzeichen -1
- **Vorhersagen (Vorschlag, vor jeder Rechnung einzufrieren):**

| Nr | Vorhersage | ableitbar? | Wahrsch. |
|---|---|---|---|
| TP0 | T3 +1 und T4 -1 in allen Tripeln; T1 auf dem kubischen Gitter erfuellt | ja (Pauli-Algebra; Quelle) | 90 % |
| TP1 | Teil A (Diamant): T1 erfuellt fuer mindestens eine Projektion, T2 = -1 an allen Knoten | teilweise (bipartit wie kubisch; Grad 4 statt 6 nicht hergeleitet) | 65 % |
| TP2 | Teil B (Pyrochlor-Kanten): T1 erfuellt fuer mindestens eine Projektion | nein | 40 % |
| TP3 | falls TP2: T2 = -1 an allen Knoten und unabhaengig von der Projektionsrichtung | nein | 50 % |

- **Ableitbarkeitsprobe (vor dem Vorschlag gemacht):**
  - T3 ist vorab ableitbar: Ungedrehte Huepfer bestehen aus vertauschenden Pauli-Faktoren auf verschiedenen Kanten. Das
    prueft nur den Code.
  - T4 ist vorab ableitbar (Quelle, LW S. 7). Das prueft den Nachbau.
  - T1 auf Pyrochlor-Kanten habe ich nicht hergeleitet. LW zeigen die Vertraeglichkeit fuer das bipartite kubische
    Gitter ("Any projection will work", S. 5) und nutzen die Staffelung (-1)^I (Gl. 1). Finns Pyrochlor-Netz hat
    Dreiecke. Ob die Kreuzungszahlen um ein Dreieck vertraeglich sind, ist offen. Hier kann die Karte scheitern.
  - Projekt-grep: STRINGENDE-1 (Z_2, Torus-Code, LW-2003-Spin-3/2-Modell), KITAEV-DIAMANT-1 (Z_2, Majoranas auf Diamant)
    [P]. Ein U(1)-Twist auf Diamant- oder Pyrochlor-Kanten wurde nicht gerechnet.
  - Die geplante LICHT-ELEKTRON-TETRA-1 (Ue2, RUNDE-38.md Z. 43) liegt nahe. TWIST-PYRO-1 waere deren algebraischer
    Vorlauf und fuegt das nicht-bipartite Netz hinzu.
- **Laufzeit:** ganzzahlige Pauli-Algebra auf wenigen tausend Kanten; STRINGENDE-1 brauchte 12 s. Kleintest-Spur
  (cpu/p4000), deutlich unter 10 min.
- **Bedeutung (vorab):**
  - TP2 scheitert: Der einfache LW-Twist traegt auf den Pyrochlor-Kanten nicht. H1 braucht dort eine andere
    Knotenbauweise, sonst bleibt das Netz im H2-Regime (Fermionen nur als stark gekoppelte Dyonen).
  - TP1 und TP2 bestehen: H1 ist algebraisch baubar. Ob die Phase deconfined ist und wie gross alpha ist, bleibt offen.
- **Verworfen: DYON-PAAR-1** (zwei Gitter-Verbunde aus LADUNG-MONOPOL-1 vertauschen, Berry-Phase -1). Das Ergebnis ist
  vorab ableitbar (Goldhaber [S-P], WS S. 7, NZC S. 6 [S]) und prueft nur Code und Adiabatik.

## 9. Gegensweep-Befunde (Feld-Regel 4)

| Nr | Selbstverstaendlich angenommen | geprueft? | Befund |
|---|---|---|---|
| G1 | "Elektron" in Ue2 meint ein schwach gekoppeltes Fermion | nein (Definitionsfrage) | Rueckfrage R2; ohne diese Festlegung ist H1/H2 ohne T eine Namensfrage (V2, V9) |
| G2 | Pace' alpha und meine Dirac-Rechnung benutzen dieselben Einheiten | **ja** (Pace Tabelle I, S. 4) | ja: alpha = e^2/hbar c, Coulomb e^2/r, "m = e/2 alpha", also alpha_m = 1/(4 alpha) [S + ES] |
| G3 | Quanten-Spin-Eis-Aussagen gelten fuer "Finns Netz" | **teilweise** (Projektdateien) | Das Projekt hat zwei Lesarten: Diamant-Kanten (KITAEV-DIAMANT-1, Ue2-Plan; = Spin-Eis-Gitter, Literatur gilt) und Pyrochlor-Kanten (FLUSS-1, LADUNG-MONOPOL-2; Literatur nur [H]). Karte TWIST-PYRO-1 traegt beide Teile |
| G4 | "alpha_c ~ 0,2 allgemein" ist gemessen | **ja** (Wortlaut S. 4) | nein: "has been argued" (Cardy 1980); gemessen nur das QSI-Modell bei zeta ~ 1. Gegenregime mit unterdrueckten Monopolen nur [L] |
| G5 | Finns Pfeile sind T-ungerade wie Spins | nein | nicht festgelegt; davon haengt nur das Etikett E/M ab, nicht die Kopplungsaussage |
| G6 | Das Dyon ist ein gebundenes Teilchen | ja (Projekt) | nicht von selbst: LADUNG-MONOPOL-1/2 ohne Topf keine Bindung [E]. Die Statistik des (1,1)-Sektors gilt trotzdem (Goldhaber: "two such clusters") |
| G7 | Theta spielt fuer die Statistikregel keine Rolle | Schreibtisch | ja: Die Paarung qe qm' - qm qe' haengt nicht von theta ab; theta verschiebt nur die Ladungen (NZC Abb. 2, S. 3) [S + ES] |

## 10. Kalibrierung

- **(a) Gemessen:** nichts in dieser Karte. Pace u. a. haben alpha_QSI im Modell numerisch bestimmt (ED, Topologie-
  Sektoren), also Modellrechnung, keine Materialmessung. LADUNG-MONOPOL-1/2 und STRINGENDE-1 sind synthetisch.
- **(b) Verdichtet:**
  - die invariante Frage "ist das schwaechst gekoppelte Teilchen ein Fermion?" (D1)
  - die Schranke alpha_11 >= 1 und die QSI-Zahlen (D2)
  - die Zwei-Regime-Aufloesung WS gegen Pace (D3, Regime B nur [L])
  - die Spin-Statistik-Asymmetrie H1/H2 (D4)
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Finns Netz liegt im H2-Regime". Gestuetzt nur auf die Spin-Eis-Literatur (anderes Gitter, falls Pyrochlor-Kanten
    gemeint sind) und auf "einfache Pfeile sind bosonisch". Keine Rechnung zum Quanten-Pfeil-Eis auf Finns Netz
    existiert (LADUNG-MONOPOL-L O1).
  - **Warnzeichen:** Meine Sicherheit, dass "das Dyon kein Elektron" ist, stieg mit Pace, waehrend die Frage zerfiel:
    topologisch (V9) falsch, energetisch (V7) richtig, und das Energetische haengt an einer argumentierten, nicht
    bewiesenen Stabilitaetsgrenze (G4).

## 11. Offene Fragen und Rueckfragen

- **R1 (aus LADUNG-MONOPOL-L, weiter offen):** Meint H2 den Monopol des konjugierten Feldes (nur der gibt
  Feld-Drehimpuls mit einer Pfeilquelle)? Nach diesem Dossier ja.
- **R2 (neu, an die Leitung):** Was heisst "Elektron" in Ue2?
  - "schwach gekoppeltes Fermion mit Einheitsladung": dann ist das Dyon keines, H1 ist noetig.
  - "Fermion mit U(1)-Ladung und Spin 1/2": dann ist H1 gegen H2 ohne Zeitumkehr eine Benennungsfrage.
- **R3 (neu, an die Leitung):** Welche Lesart von "Finns Netz" gilt fuer Ue2: Diamant-Kanten (= Quanten-Spin-Eis) oder
  Pyrochlor-Kanten (FLUSS-1)? Davon haengt ab, ob die QSI-Literatur direkt gilt.
- **O1:** Hat das Quanten-Pfeil-Eis auf Pyrochlor-Kanten eine deconfined Phase, und wie gross ist alpha dort?
  Methode wie Pace (Topologie-Sektoren plus Photongeschwindigkeit) [H].
- **O2:** Gitter-Doppelgruppe des Dyons an einer Literaturstelle (Kandidaten nur aus dem Gedaechtnis: symmetrie-
  angereicherte U(1)-Fluessigkeiten mit Raumgruppe) [L?].
- **O3:** Ist die Grenze alpha_c ~ 0,2 mit unterdrueckten Monopolen aufhebbar (Regime B)? [L], nicht geprueft.
- **O4:** Im topologischen Mott-Isolator ist die reine Ladung ein Kramers-Fermion (WS Tabelle I). Ist sie dort schwach
  gekoppelt und damit elektronartiger als jedes Dyon? Dazu nichts gelesen [H].

## 12. Quellenliste mit Abrufstand

Alle Abrufe am 2026-10-04 per curl; lokale Kopien in quellen/. Zeiten: date-Stempel um den Abruf.

| Nr | Quelle | URL | Abruf (CEST) | gelesen |
|---|---|---|---|---|
| A1 | C. Wang, T. Senthil (2016), "Time-reversal symmetric U(1) quantum spin liquids", Phys. Rev. X 6, 011034; arXiv:1505.03520v2 | https://arxiv.org/pdf/1505.03520 | 11:12:11 | Volltext (25 S.), per grep und sed: S. 2-3, 6-8, 14, 19, Literaturliste |
| A2 | M. Levin, X.-G. Wen (2006), "Quantum ether: photons and electrons from a rotor model", Phys. Rev. B 73, 035122; arXiv:hep-th/0507118 | https://arxiv.org/abs/hep-th/0507118 | 11:12:11 | Abstract |
| A3 | arXiv-API, Titelabfrage zu A5 | http://export.arxiv.org/api/query?search_query=ti:"fine structure constant" AND ti:"spin ice" | 11:16:45 | Metadaten und Abstract von A5 |
| A4 | wie A2, Volltext (10 S.) | https://arxiv.org/pdf/hep-th/0507118 | 11:16:45 | S. 1, 3-5, 7, 9 |
| A5 | S. D. Pace, S. C. Morampudi, R. Moessner, C. R. Laumann (2021), "The Emergent Fine Structure Constant of Quantum Spin Ice Is Large", Phys. Rev. Lett. 127, 117205; arXiv:2009.04499v2 | https://arxiv.org/pdf/2009.04499 | 11:18:03 bis 11:18:05 | Volltext (11 S.): S. 1-5, Supplement (Dualgitter) |
| A6 | arXiv-API, Titelabfrage ti:"symmetry enriched" AND ti:U(1) | http://export.arxiv.org/api/query?search_query=ti:"symmetry enriched" AND ti:U(1) | 11:21:15 bis 11:21:16 | 10 Abstracts, darunter L. Zou, C. Wang, T. Senthil (2018), PRB 97, 195126, arXiv:1710.00743; Y.-D. Li, G. Chen (2017), PRB 95, 041106, arXiv:1607.02287; P.-S. Hsin, A. Turzillo (2020), JHEP 09, 022, arXiv:1904.11550 |
| A7 | S.-Q. Ning, L. Zou, M. Cheng (2020), "Fractionalization and Anomalies in Symmetry-Enriched U(1) Gauge Theories", Phys. Rev. Research 2, 043043; arXiv:1905.03276v3 | https://arxiv.org/pdf/1905.03276 | 11:25:22 bis 11:25:23 | Volltext (31 S.) per grep: S. 3, 4, 6, 14 |

- **Nur ueber Zitat in A1, nicht gelesen:** C. Wang, A. C. Potter, T. Senthil, "Classification of Interacting
  Electronic Topological Insulators in Three Dimensions", Science 343, 6171 (2014) (so im Zitat [24]; Seitenzahl nicht
  geprueft);
  S. M. Kravec, J. McGreevy, B. Swingle, Phys. Rev. D 92, 085024 (2015) [36]; L. Savary, L. Balents, PRL 108, 037202
  (2012) [11]; J. L. Cardy, Nucl. Phys. B 170, 369 (1980) (Zitat [5] in A5).
- **Im Projekt schon an der Quelle gelesen [S-P], nicht erneut abgerufen:** A. S. Goldhaber, PRL 36, 1122 (1976),
  Abstract; M. Hermele, M. P. A. Fisher, L. Balents, PRB 69, 064404 (2004), Abstract; M. Levin, X.-G. Wen, PRB 67,
  245316 (2003), Volltext; M. A. Metlitski, C. L. Kane, M. P. A. Fisher, PRB 88, 035131 (2013), Abstract; PDG 2025,
  Rev. 94.
- **Projektdateien [P]:** RUNDE-37: ladung-monopol-l/DOSSIER.md und ARBEITSFELD.md, stringende-1/ERGEBNIS.md,
  ladung-monopol-1/ERGEBNIS.md, ladung-monopol-2/ERGEBNIS.md, UEBERLEITUNGEN-EMERGENZ.md (Ue2),
  kitaev-diamant-1/ERGEBNIS.md (Kopf); RUNDE-09/spin1/SPIN1.md; RUNDE-38.md Z. 43; RUNDE-39.md Z. 29.

## 13. Selbstanzeigen

1. **Zwei Abrufe waren arXiv-API-Titelabfragen** (A3, A6). Ich habe sie als gezielte Abrufe bekannter Arbeiten
   gezaehlt, nicht als Suche. A6 lieferte zehn Treffer; gelesen habe ich vier Abstracts.
2. **Seitenzahlen** stammen aus pdftotext je Seite (PDF-Fassung arXiv), nicht aus der Zeitschriftenfassung.
3. **Volltexte nur per grep und Ausschnitt gelesen**, nicht vollstaendig. Ein Satz zum Dyon in E_b M_b bei Wang/Senthil
   kann in nicht gelesenen Teilen stehen. grep nach "dyon", "bound state", "Goldhaber", "Eb Mb" fand keinen solchen Satz.
4. **Matrixkonvention bei NZC S. 3:** Die Klammer "(1, 0) turns into ... (n, 1)" passt nicht eindeutig zur dort
   abgedruckten T-Matrix. Ich stuetze E1 auf S. 6 ((-1)^(qe qm)) und S. 14.
5. **Regime B (unterdrueckte Monopole) ist Gedaechtnis [L]**, nicht geprueft.
6. **Zeitbox:** Start 11:06:02; Dossier ab 11:27:44 CEST. Keine Peerbus-Nachricht, kein Journaleintrag, kein Commit,
   keine Aenderung an anderen Projektdateien (Berichtigungen nur benannt, Abschnitt 7.4).

## Einfach gesagt

Wenn man eine elektrische Ladung und einen magnetischen Pol zusammensteckt, verhaelt sich das Paar wie ein Elektron:
Es ist ein Fermion und hat einen halben Spin. Das steht jetzt woertlich in zwei Fachartikeln. Allerdings ist es nur eine
Frage der Benennung, welches Teilchen man "elektrisch" nennt; ein Fachartikel beschreibt echte Elektronen sogar
ausdruecklich als so ein Paar. Was wirklich zaehlt, ist, wie stark ein Teilchen mit dem Licht zusammenwirkt: Im
Quanten-Eis koppelt das Paar mindestens siebenmal staerker an das Licht als die einfache Ladung, ein echtes Elektron
dagegen sehr schwach. Fuer ein Elektron wie in unserer Welt muesste deshalb schon das einfache Ende eines Pfeilfadens
ein Fermion sein, und dafuer braucht Finns Netz eine besondere "verdrehte" Bauweise; ob es die geben kann, soll die
kleine Rechnung TWIST-PYRO-1 pruefen.
