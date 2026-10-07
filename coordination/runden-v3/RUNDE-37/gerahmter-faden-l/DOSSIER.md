# GERAHMTER-FADEN-L: Dossier (feldforscher fuer die Leitung claude-primary, Runde 50, Schritt b)

## 1. Kopf

- **Frage (KARTE.md, bindend):** Was braucht ein bosonisches 3D-Gittermodell, damit die Enden seiner Faeden Fermionen
  mit echtem Spin 1/2 sind (2-pi-Drehung -1 UND Austausch -1)? Liefert ein Drehrahmen je Knoten (SU(2)- bzw.
  SO(3)-Rotor) die Rahmung der Faeden? Ziel: Bauanleitung fuer Finns Tetraedernetz.
- **Zeiten (alle per date):** Start 2026-10-05 18:27:32 CEST. Arbeitsfeld ab 18:36:08. Abrufe 18:36:45 bis 18:52:57.
  Gegensweep 18:52 bis 18:55. Dossier ab 18:57:32. Endzeit siehe letzte Zeile.
- **Abrufe: 15 von 15.** 5 arXiv-API (davon 2 Sammelabrufe mit 14 bzw. 5 Abstracts, 3 Suchen), 6 Volltexte per curl
  (LW 2005, Thorngren 2014, Bednorz 2018, Wan/Wang/Wen 2022, Chen/Kapustin 2018, Freedman u. a. 2011; Abruf 2/3 und
  8/9 je zwei PDFs, einzeln gezaehlt), 1 INSPIRE-API, 3 WebSearch. Abruf 1 hatte einen leeren http-Vorversuch
  (Weiterleitung), mitgezaehlt. Ohne Abrufzaehlung lokal gelesen: Levin/Wen 2006 und Ning/Zou/Cheng 2020 (Projektkopien)
  sowie Projektdateien.
- **Art:** nur Literatur und Schreibtisch. Keine Rechnung, keine Messdaten. Literatur ist keine Messdatenbestaetigung.
- **Kennzeichen:** [S] an der Quelle gelesen (Fundstelle), [S Abstract] nur Abstract, [W] nur Kurztext eines
  Suchwerkzeugs (nicht gelesen), [L] Gedaechtnis, [P] Projektbefund, [M] Mathematik am Schreibtisch (nicht maschinell
  geprueft), [ES] eigener Schluss, [H] Hypothese.
- **Arbeitsfeld** mit allen Erwartungen vor jedem Abruf, Ausgaengen, Gegensweep und Rueckfragen: ARBEITSFELD.md.
  **Quellenkopien:** quellen/ (PDF, Fluss-Text, API-Antworten). Zeilenangaben "Fluss-Z." beziehen sich auf die
  *-fluss.txt-Dateien dort.

## 2. Kurzfazit (Ergebnis zuerst)

1. **Kontinuum:** 2-pi-Vorzeichen und Austauschvorzeichen eines Fadenendes sind eine Zahl, die Verschlingung des Fadens
   mit seiner Rahmung (Thorngren 2014, S. 4-5 [S]); Z2-Fermion: da = w2, Spin-Darstellung (WWW 2022 [S]).
2. **Gitter, Moderator "feste Rahmung?":** Projektion (LW), Verzweigung, feste Spinstruktur (Chen/Kapustin [S]) sind
   feste Rahmungen; mit ihnen gibt es Fermionen ohne Spin (TWIST-SPIN-1 [P]; Creutz [S Abstract] "no such constraint").
   Erzwungen wird der Zusammenhang erst ohne feste Rahmung bzw. bei Lorentz-Invarianz im Grenzfall [ES].
3. **Ein geordnetes Drehrahmen-Feld ist selbst eine feste Rahmung** [M, Skizze]; im Projekt ist es zudem innere SO(3) [P].
4. **Bauanleitung (Abschn. 9) [H]:** Faden und Rahmentransport auf denselben Link, "Fluss = Hebungsvorzeichen des
   Rahmens" (WWW Anhang C [S]); Rahmen an den Raum verriegeln; Faden traegt seine Rahmung; sie setzt auch den Twist.
5. **GF2 nach Recherchestand nicht belegt;** Nahtreffer Bednorz 2018, Freedman u. a. 2011. **[ES]** Die Z2-Wirbellinien
   des Rahmens sind nicht die Faeden, sondern die pi-Flusslinien der Fermionen.

## 3. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet (vor dem Abruf) | Gefunden | Quelle |
|---|---|---|---|
| V1 | "All-fermion"-Elektrodynamik bzw. FcFl ist in jedem strikt 3D-bosonischen Gitter verboten (DYON-STATISTIK-L E4) | Zwei Regime: fuer verzweigungsunabhaengige (BIB) Systeme ist die w2 w3-Ordnung nichttrivial, fuer generische, verzweigungsabhaengige (GLB) "belong to the same phase" wie ein Produktzustand. Verzweigung ~ Rahmen "may be related", "trivializes any Stiefel-Whitney classes" (Vermutung der Autoren) | Wan/Wang/Wen 2022, S. 2-3, Fussnote 1 [S] |
| V2 | LW 2005 fuehrt im 3D-Teil gerahmte Faeden ein | Keine Rahmung, sondern eine Konvention JE KNOTEN: "orientation conventions for each vertex ... 'left turns' and 'right turns' ... (such an orientation convention can be obtained by projecting ...)". Die Projektion ist nur ein Weg | LW 2005, S. 11 [S] |
| V3 | (Karte, GF3) Ein Drehrahmen-Feld liefert die Rahmung der Faeden und damit Spin 1/2 | Ein gleichfoermig geordneter Rahmen ist selbst eine feste Rahmung: Punktgruppe wirkt als Konjugation, kein Bindungswinkel aendert sich, kein Vorzeichen. Und das Projekt-Rahmenfeld ist eine innere SO(3) | [M, Skizze]; [P] |
| V4 | Kein bosonisches Modell mit Spin-1/2-Fadenenden und Drehsymmetrie gefunden | Bednorz 2018: "Fermi-Dirac spin 1/2 operators can be emergent in a fully commuting field theory ... rotation symmetry remains preserved". Aber: Kontinuum, Faden = SU(2)-Wilson-Linie mit Spin-1/2-Indizes an den Enden, Statistik per Vorzeichen gewaehlt ("the - sign is to get antisymmetric fermions, with + we get bosons") | Bednorz 2018 [S] |
| V5 | Freedman u. a.: nur Band-Permutationsgruppe | Das Feld rahmt die Faeden selbst: Urbild eines Punktes von S^2 = Boegen zwischen Igeln, zurueckgezogener Tangentialvektor = Rahmung, "a set of ribbons connecting the hedgehogs". Nach einem Austausch "the ribbon on the left has a twist in it. So we rotate that particle by -2 pi" | Freedman u. a. 2011, Fluss-Z. 1740-1800 [S] |
| V6 | Thorngren: allgemeine 4d-Theorie, Linien brauchen Rahmung | Staerker und enger: Spin- UND Austauschvorzeichen aus derselben Verschlingungszahl; Kontext aber anomale Randphasen bosonischer SPT; die "fermionic strings" sind das anomale Element | Thorngren 2014, S. 1-5 [S] |
| V7 (Werkzeug) | arXiv-API-Phrasensuche deckt 24 Monate ab | Eine Suche 0 Treffer (Syntax), eine 4, eine 170 verrauscht. Urteile im 24-Monats-Fenster nur "nach Recherchestand" | Abrufe 4, 5, 12 |

## 4. Abgleich GF1 bis GF3 (beschreibend, Erwartungen der Karte unveraendert)

| Nr | Erwartung (Karte) | Wahrsch. | Befund | Tragende Fundstelle |
|---|---|---|---|---|
| GF1 | [L] Neuere Arbeiten (2018-2026) zeigen: echter Spin 1/2 verlangt Kopplung an die Geometrie ueber w2 bzw. eine Rahmung der Faeden | 65 % | **eingetroffen, mit Regime-Einschraenkung.** Kontinuum/TQFT: ja, und Spin und Statistik sind dort dieselbe Groesse. Gitter: mit fester Rahmung gibt es Fermionen ohne Spin; die Kopplung ist dort nicht erzwungen | Thorngren 2014 S. 4-5 [S] (2014, aelter als das Fenster); WWW 2022 S. 2-3 und Anhang C [S]; Chen/Kapustin 2018 [S]; Creutz 2014 [S Abstract] |
| GF2 | [L] Mindestens eine Arbeit konstruiert ein Gittermodell, in dem ein lokaler Rahmen bzw. SU(2)-Rotor je Knoten den Fadenenden Spin 1/2 gibt, ohne Spinoren von Hand | 40 % | **nicht eingetroffen (nach Recherchestand).** Zwei Websuchen und zwei API-Suchen (eine im 24-Monats-Fenster). Nahtreffer: Bednorz 2018 (Kontinuum; Spinor-Index am Ende strukturell eingebaut; Statistik gewaehlt), WWW Anhang C (Kopplungsgesetz, aber Rahmen = Raumzeit-Hintergrund), Freedman u. a. (Feld rahmt Faeden; Kontext freie Fermionen) | Abrufe 5, 6, 7, 13, 15 |
| GF3 | [H] Fuer Finns Netz folgt eine konkrete, als Rechenkarte pruefbare Bauanleitung (Kopplung Drehrahmen <-> LW-Twist) | 55 % | **teilweise eingetroffen.** Eine Bauanleitung laesst sich aus vier Quellen zusammensetzen (Abschn. 9), sie ist aber [H]. Zwei Teile sind schon am Schreibtisch entschieden (geordneter Rahmen hilft nicht; richtungsartige Knotenkonvention traegt keinen Spin, Skizze). Offen und rechenbar: Vertraeglichkeit knotenweiser Konventionen und ob Spin- und Austauschvorzeichen aus einer Regel kommen | Abschn. 9, 10 |

## 5. Kernaussagen mit Quellenstufe (Literaturstand)

**K1 Rahmung = Spinstruktur; Spin und Statistik aus einer Zahl** (Thorngren 2014, S. 4-5 [S]):
- "we should think of a as a spin structure. Then it is well-known (see eg. [10]) that a spin structure is the same as
  an assignment of +-1 to framed curves which flips signs when the framing is rotated by 2 pi." ([10] = Scorpan 2005 [L].)
- Push-off-Formel: exp(i pi int_{gamma-hat} a) = (-1)^{link(gamma, gamma')} exp(i pi int_gamma a).
- "a 2 pi rotation of the quasiparticle gives a minus sign by increasing the linking number by one."
- "The framing also causes fermionic braiding statistics ... creating a particle-antiparticle pair, braiding them, and
  then annihilating ... the framing always points into the page. This forces link(gamma, gamma') = 1, so the braiding
  phase is -1."
- S. 5-6: w2 ist Poincare-dual zu X_w2, "a magnetic surface operator defined so that any wavefunction changes by
  (-1)^F around a loop linking X_w2" (im 3D-Raum: Linien).
- [ES] LWs gedrehter Fadenoperator W~(C) = W(C) (-1)^{sum n_ci} mit "framing C' ... a curve drawn next to C" (LW 2006,
  lokal [S]) ist genau diese Push-off-Formel; "into the page" ist LWs Projektion.

**K2 Fermionische Ladung = dynamische Spinstruktur; Gitterform des Kopplungsgesetzes** (Wan/Wang/Wen 2022 [S]):
- Anhang C: "for a twisted Z2-gauge theory satisfying da = w2, the corresponding Z2 gauge charge is a fermion. This is
  because da = w2 implies that under a combined Z2-gauge and SO(inf) spacetime rotation transformation, the Z2 gauge
  charge transforms as Z2 x|_{w2} SO(inf)."
- Linkpaare (a_ij in Z2, gamma_ij in SO), Verknuepfung (a1, g1)(a2, g2) = (a1 + a2 + w2(g1, g2), g1 g2); "For a nearly
  flat connection ... on a triangle (ijk)": w2(gamma_ij, gamma_jk) = a_ik - a_ij - a_jk, "which is w2 = da". "the Z2
  gauge charge carries a half-integer spin, and is a fermion using the spin-statistics theorem."
- Fluss-Z. 2784-2786: "the emergent dynamical Spin structure of the Z2 gauge theory and emergent dynamical Spin^c
  structure of the all-fermion U(1) gauge theory".
- Einschraenkung [S]: gamma ist dort der Raumzeit-Rahmen (Hintergrund), und es heisst "nearly flat" (Zulaessigkeit).

**K3 Feste Rahmung auf dem Gitter; Verzweigung als Rahmung** (Chen/Kapustin 2018; WWW 2022 [S]):
- Chen/Kapustin S. ~3, Fig. 2: "To define bosonic hopping operators U_f, we need to choose a framing for each edge of the
  dual lattice, i.e. a small shift of each dual edge along some orthogonal direction"; Kreuzungen in der Projektion
  bestimmen die Z-Faktoren, wie bei LW. "The framing for gauge constraints is opposite to the framing used to define
  hopping operators."
- Triangulierung: "we choose a branching structure ... an orientation on each edge such that there is no oriented loop on
  any triangle"; Fermion (Majorana-Paar) je Tetraeder; "E is a spin structure (i.e. a 2-chain such that dE = w2)";
  w2 = "all edges of the triangulation, together with the (02) edge for all '+' tetrahedra and the (13) edge for all '-'
  tetrahedra"; "our bosonization map depends on the choice of a spin structure E" (Abstract: "depends explicitly on the
  choice of a spin structure of the spatial manifold").
- WWW S. 2-3: "We conjecture that the independence of the branch structure of spacetime complex for lattice models
  implies the independence of frame structure of spacetime manifold in the continuum limit." Fussnote 1: Verzweigung
  "may be related to the frame structure on a smooth manifold that trivializes any Stiefel-Whitney classes".

**K4 Anomalie-Grenze** (FHH 2022 [S Abstract]; WWW [S]; Thorngren [S]):
- FcBl = "ordinary fermionic toric code"; FcFl "can only exist at the boundary of a non-trivial 4+1d invertible bosonic
  phase", "same gravitational anomaly as all-fermion quantum electrodynamics", Wirkung (1/2) int w2 w3.
- Thorngren (Einleitung, Fluss-Z. 46-50): Anomalie w2 w3 "can be cancelled by introducing neutral fermions, but
  remains if we introduce charged fermions."
- WWW S. 3: fuer GLB-Systeme gehoert die w2 w3-Ordnung zur trivialen Phase. [ES] Das Verbot "FcFl bzw. all-fermion-QED
  im strikt 3D-bosonischen Gitter" gilt also im BIB-Regime; fuer verzweigungsabhaengige Gitter ist es nach dieser
  Aussage kein Phasenhindernis. Ein explizites GLB-Gittermodell dafuer habe ich nicht gesehen.

**K5 Auf dem Gitter ist Spin-Statistik frei** ([S Abstract] bzw. [S]):
- Creutz 2014: "for particles hopping on a lattice, there is no such constraint. If a lattice model yields a relativistic
  field theory in a continuum limit, this constraint must 'emerge'"; spinlose Gitterfermionen -> Dirac (Graphen,
  staggered).
- Ning/Zou/Cheng 2020 (lokale Projektkopie [S]): mit innerer SO(3) sind (E_b^{1/2} M_b^trn) und (E_f^{1/2} M_b^trn)
  realisierbar; sie "can emerge only if the microscopic lattice system has a half-odd-integer spin in each unit cell. The
  converse is also true"; E_b^{1/2} M_b^{1/2} ist anomal; Minimalgruppe Z2 x Z2 der pi-Drehungen genuegt.
- Cheng/Wang [S Abstract]: Fuer das kristalline Aequivalenzprinzip "it is necessary to change the central extension
  structure of the symmetry group by the Z2 fermion parity" (spinlos <-> Spin 1/2 vertauscht). Thorngren/Else
  [S Abstract]: Raumgruppe wie innere Symmetrie.
- Bednorz 2018 [S]: Statistik per Vorzeichen im Tauschterm gewaehlt und energetisch stabilisiert ("The antisymmetric
  state has then lower energy (in the first order) than the symmetric and so it is stable"); "We failed to present a
  Lorentz invariant model".

**K6 Rahmen aus dem Feld; Austausch braucht Verdrillung** (Freedman u. a. 2011 [S], Balachandran u. a. 1993
[S Abstract]):
- Freedman: S^2-Feld, Urbild-Boegen zwischen Igeln, Rahmung aus dem zurueckgezogenen Tangentialvektor; Baender "can
  break and reconnect"; Austausch hinterlaesst eine Verdrillung, die durch -2 pi Drehung eines Igels aufgehoben wird;
  Doppelverdrillung per "lasso" loesbar (Guerteltrick). Abstract: T^r_2n mit "even part" (Paritaet der Verdrillungen
  plus Paritaet der Permutation gerade). Kontext: Teo/Kane-Defekte freier Fermionen.
- Balachandran u. a.: Spin-Statistik-Beweise "for spinning particles ... require neither relativity nor field theory.
  They do, however, assume certain continuity conditions involving the existence of antiparticles."

**K7 3D-Stringnetze** (LW 2003 [S Abstract], LW 2005 [S]):
- LW 2003: "fermions always come in pairs ... creation operator always has a string-like structure"; "fermions always
  couple to a nontrivial gauge field".
- LW 2005 S. 11-12: Knotenkonvention links/rechts; Zusatzbedingung (32), weil "Small closed curves ... can (in a sense)
  intersect exactly once"; Fermionen aus der verdrehten Eichtheorie (33): "all the quasiparticles corresponding to 'odd'
  representations i are fermionic"; nur Eichtheorien und verdrehte Eichtheorien. Spin unter Drehungen kommt nicht vor;
  im 2D-Teil nur "By the spin-statistics theorem they are closely connected to the quasiparticle spins".
- Lan/Wen 2019 [S Abstract]: Punktteilchen = Darstellungen von G_f = Z2^f x|_{e2} G_b.

## 6. Regime und Moderatoren (Regel 1)

| Paar | Moderator | Regime 1 | Regime 2 | Beleg |
|---|---|---|---|---|
| Spinloses Fermion (TWIST-SPIN-1) gegen Spin-1/2-Fermion (TQFT) | Haengt die Fadenregel von einer festen Rahmung ab (Projektion, Verzweigung, feste Spinstruktur, geordneter Rahmen)? | fest (GLB-artig): Fermion ohne Spin unter den rahmungserhaltenden Drehungen | frei (BIB-artig, rahmenunabhaengig): Spin = Statistik (eine Verschlingungszahl) | [P], [S] Thorngren, WWW, Chen/Kapustin; Verbindung [ES] |
| Anomalie FcFl/all-fermion verboten gegen erlaubt | dieselbe Verzweigungsabhaengigkeit | BIB: verboten (Rand von w2 w3) | GLB: kein Phasenhindernis | WWW S. 3 [S]; Schluss [ES] |
| Spin aus innerem Index gegen Spin aus Rahmung | Traegt das Ende einen eigenen SU(2)-Index (Rotor-Halbsektor, Isospin) oder nur die Z2-Ladung? | innerer Index: Spin und Statistik unabhaengig (Kramers-Boson, E_b^{1/2}, Bednorz-Vorzeichen) | Rahmung: beide aus einer Zahl | Ning/Zou/Cheng [S], Bednorz [S], Thorngren [S] |
| Spin aus Bandstruktur gegen Spin am Ende | Energieskala (Gitter gegen Grenzfall) | Gitter: Punktgruppe darf trivial wirken (Creutz) | Grenzfall: Lorentz-Spinor, kombiniert mit Geschmacksdrehung | Creutz [S Abstract]; LW 2006 S. 9 [P] |
| Rahmen geordnet gegen Rahmen frei/textuiert | Zustand des Rahmenfelds am Fadenende | geordnet: wirkt wie feste Rahmung, spinlos | frei (Quantenrotor, symmetrisch) oder Ende = Defekt des Rahmens: Spin moeglich | [M, Skizze]; Freedman [S]; Jackiw/Rebbi [P] |

## 7. Unterscheidungspunkte (Regel 2)

| Nr | Erklaerungspaar | Wo sie messbar auseinanderlaufen | zugaenglich? |
|---|---|---|---|
| U1 | feste gegen freie Rahmung | Einzelnes Fadenende, oertliche 2-pi-Drehung der Rahmung am Ende relativ zur Umgebung: +1 gegen -1; bzw. PSG-Invariante (C2)^2 am Einzelende, wenn die Punktgruppe die Rahmung mitdreht | Modell ja (Rechenkarte M3, M4); Natur nein |
| U2 | innerer Index gegen Rahmung | Ein Ende mit Spin 1/2 OHNE Twist: beim inneren Index ein Boson (moeglich), bei reiner Rahmung im rahmenunabhaengigen Regime unmoeglich (Statistik und Spin sind eine Zahl) [ES] | Modell ja (Folgekarte GERAHMTER-FADEN-2) |
| U3 | Bandstruktur-Spin gegen Fadenend-Spin | Punktgruppen-Klasse am Gitter (trivial moeglich) gegen Lorentz-Spin im Grenzfall | Modell ja (TWIST-SPIN-1 Stufe F zeigt trivial); Natur nein |
| U4 | BIB gegen GLB | Laesst sich FcFl in einem 3+1D-Gitter mit fester Verzweigung realisieren? | nur theoretisch; kein Modell bekannt [ES] |

## 8. Was im Projekt schon steht und was neu ist

- **Schon im Projekt [P]:**
  - Spin aus Isospin, Ladung + Monopol, FR (Jackiw/Rebbi in QUARK-1 [S]; VIERTE-KOORDINATE-L VK3 "Spin erst mit
    Kopplung an Raumdrehungen"; GEN-04 H1, H2, H4, H10; SPIN-HOPF-L fuer Hopfionen).
  - TWIST-PYRO-1 (Twist traegt, Lesart S), TWIST-SPIN-1 (spinlos; >= 2 Zustaende je Knoten noetig; Guerteltrick braucht
    stetige Rahmungswechsel), DYON-STATISTIK-L (Wang/Senthil, Kramers-Boson, all-fermion verboten).
  - RUNDE-46 L4 [Codex]: "Spin- und Austauschpfad muessen dieselbe Phasenregel benutzen."
  - IDEEN-SPIN-ZEIT I1 (kurzer Lift, Vorzeichen kippt nur bei 180 Grad), I2 (Ringschwellen), I3 (Phasenterm noetig);
    Z2-SCHUTZ-2/GPU-Z2-1 (endliche Barriere, Z2-Wirbelring am Sattel).
- **Neu fuers Projekt (Literatur, nicht neu fuer die Welt):** Thorngrens Push-off (K1); WWW: Regime BIB/GLB, Verzweigung
  ~ Rahmung (Vermutung), Kopplungsgesetz Anhang C (K2-K4); LWs Knotenkonvention (K7); Chen/Kapustins Gitter-w2 und
  Spinstruktur E auf Triangulierungen (K3); FHH FcFl-Anomalie; Bednorz; Freedman u. a. (Feld rahmt Faeden); Creutz;
  Cheng/Wang; Balachandran u. a.
- **Neu, Schreibtisch [ES/M, ungeprueft]:**
  - Antwort auf die geparkte Frage aus IDEEN-SPIN-ZEIT: Die Z2-Wirbellinien des Drehrahmens (Hebungsvorzeichen -1 um
    einen Ring) sind unter da = w2 die pi-Flusslinien der Fermionen (X_w2 bei Thorngren), nicht die LW-Faeden.
  - Ein geordneter, ans Gitter gekoppelter Rahmen ist eine spontan feste Rahmung: Punktgruppe als Konjugation, kein
    Vorzeichen (V3).
  - Eine richtungsartige Knotenkonvention (nur n_i in S^2, wie LWs Projektion) kann kein wegunabhaengiges 2-pi-Vorzeichen
    tragen, weil pi_1(S^2) = 0 und eine Drehung um n_i selbst n_i festhaelt (Gegensweep G5).
  - Mit Kopplungsgesetz: Eine oertliche 2-pi-Drehung des Rahmens am Knoten i, bei der die Bindungen an i einzeln durch
    180 Grad gehen, wirkt auf die Fadenvariablen wie das Gauss-Produkt A_i, also -1 auf einem Ende bei i.

## 9. Bauanleitung fuer Finns Netz [H, zusammengesetzt; nichts davon gerechnet]

- **B0 Entscheidung vorab (Rueckfrage R1/R2):** Was heisst "echter Spin 1/2"? (a) PSG-Klasse 2T am Einzelende unter der
  Punktgruppe (wie TWIST-SPIN-1) oder (b) -1 unter oertlicher 2-pi-Rahmendrehung. (b) ist schwaecher; (a) braucht B4.
- **B1 Rahmen je Knoten:** Einheitsquaternion q_i (Hebung von R_i), Bindung gamma_ij = R_i^T R_j, kurzer Lift s_ij
  (Realteil > 0; IDEEN-SPIN-ZEIT I1). Vorhanden in Z2-SCHUTZ/GPU-Z2-1 [P].
- **B2 Fadenvariable auf demselben Link:** Z2 (oder U(1)-Pfeil wie im Eis) a_ij. LW-Fadenoperatoren wie TWIST-PYRO-1.
- **B3 Kopplungsgesetz (WWW Anhang C [S]):** Fluss von a durch jede kleinste Schleife = Hebungsvorzeichen des Rahmens um
  diese Schleife (Diamant: Sechsecke; gefuelltes Netz: Dreiecke). Gleichwertig [ES]: U_ij = (-1)^{a_ij} s_ij ist eine
  flache SU(2)-Verbindung. Im Hamiltonian: Flussterm -sum_p w2_q(p) B_p statt -sum_p B_p.
- **B4 Verriegelung an den Raum:** Im Projekt ist die Rahmen-SO(3) bisher innere Symmetrie [P]. Fuer physikalischen Spin
  muss eine Gitterdrehung auf die Rahmen wirken (nicht nur auf die Knotenorte), und ein Energieterm muss die
  Rahmenachsen an die Bindungsrichtungen der Tetraeder binden (Gegenstueck zu Jackiw/Rebbi: Isospin an Raum gekoppelt
  [P]). Achtung [M, Skizze]: Im gleichfoermigen verriegelten Zustand bleibt als Symmetrie nur die Konjugation
  q -> g~ q g~^-1 uebrig, und die traegt kein Vorzeichen; deshalb ist B7 noetig.
- **B5 Der Faden traegt seine Rahmung:** Der Fadenoperator enthaelt die Hebungsbuchhaltung des Rahmens entlang des
  Fadens (Z2-Anteil des Produkts der (a, gamma)-Paare). Ohne B5 sieht das Ende nur Wirbel, nicht seine eigene Drehung.
- **B6 Dieselbe Rahmung setzt das Twist-Vorzeichen:** LW 2005 erlaubt eine Konvention je Knoten [S]. Nach G5 reicht eine
  richtungsartige Konvention (n_i) nicht; sie muss von der vollen Rahmung bzw. vom Hebungsvorzeichen abhaengen. Nur
  dann kommen Spin und Statistik aus einer Regel (Codex-Bedingung L4).
- **B7 Ende frei oder als Defekt:** Ist der Rahmen gleichfoermig geordnet, bleibt das Ende spinlos (V3). Noetig ist
  entweder ein quantenhafter, symmetrischer Rahmen (Rotor mit Halbsektor am Ende, "spin from isospin") oder ein Ende,
  das ein Defekt des Rahmens ist (Freedman: Faeden = Urbild-Boegen zwischen Igeln).
- **B8 Zulaessigkeit:** "nearly flat" (WWW) heisst: keine Bindung bei 180 Grad; fuer Dreiecke keine ueber 120 Grad
  (I2). Sonst mischen die Sektoren; dann gilt nur der endliche Energieschutz aus Z2-SCHUTZ-2/GPU-Z2-1.
- **B9 Anomalie-Grenze:** Die magnetische Seite (Flussschleifen bzw. Monopole) muss bosonisch bleiben (FcBl), solange das
  Modell rahmenunabhaengig sein soll (BIB). Eine feste Rahmung wuerde das Verbot aufheben, aber zugleich den Spin (B6).

## 10. Vorschlag Rechenkarte GERAHMTER-FADEN-1 (Entwurf, vor jeder Rechnung)

- **Frage:** Kommen auf Finns Diamantnetz das 2-pi-Vorzeichen am Fadenende und das Austauschvorzeichen aus derselben
  Regel, wenn die Fadenoperatoren mit dem Rahmenfeld statt mit einer festen Projektion gerahmt werden?
- **Modell (exakt, GF(2)/Z4 wie TWIST-PYRO-1/-SPIN-1; Rahmen als klassischer Hintergrund):**
  - Netz: Diamant n = 2, 3 (Code TWIST-PYRO-1/-SPIN-1); Pyrochlor-Kanten optional.
  - Rahmenklassen: R0 gleichfoermig (q_i = 1); R1 glatt zufaellig mit groesstem Bindungswinkel theta_max in
    {15, 30, 45, 60} Grad; R2 Kern um 360 Grad verdreht (kleine Kugel wie Z2-SCHUTZ).
  - Varianten: A feste Projektion (Kontrolle); B LW Lesart S mit knotenweiser Richtung n_i = q_i z q_i^-1; C wie A plus
    Kopplungsgesetz B3 und Hebungsbuchhaltung B5.
- **Messgroessen:**
  - M1 Vertraeglichkeit: Zahl antivertauschender Paare (Schleife, Schleife) und (Huepfer, Schleife) in B bei R1 je theta_max.
  - M2 Austausch: T-Kreuzungs-Vorzeichen in allen Tripeln (A, B, C).
  - M3 Spin: Vorzeichen eines Zustands mit einem Ende am Knoten i unter einer oertlichen 2-pi-Drehung von q_i (K Schritte,
    drei Achsen, darunter die Achse n_i), relativ zum Zustand ohne Ende. B: Produkt der Konventionswechsel-Unitaeren;
    C: Vorzeichen aus Hebungsbuchhaltung und Flussanpassung.
  - M4 Punktgruppe: PSG-Invariante (C2)^2 am Einzelende unter T, Rahmen per Konjugation (R0) mitgedreht.
- **Erwartungen:**

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| GFR0 | Kontrolle: A gibt TWIST-PYRO-1/-SPIN-1 bitgleich wieder (0 antivertauschende Paare, -1 in allen Tripeln, (C2)^2 = +1) | vorab [P] | 90 % |
| GFR1 | [H] B ist bei R1 mit theta_max <= 30 Grad vertraeglich (0 Paare), bei 60 Grad nicht (> 0 Paare) | offen | 45 % |
| GFR2 | [H] B liefert in M3 kein achsenunabhaengiges -1 (ueberall +1 oder achsenabhaengig) | Skizze G5, scheiterfaehig | 70 % |
| GFR3 | C liefert in M3 -1 mit Ende und +1 ohne, fuer alle drei Achsen; M2 in C gleich A | Skizze [M] | 75 % |
| GFR4 | M4 bei R0: (C2)^2 = +1 in A, B und C (geordneter Rahmen = feste Rahmung) | Skizze [M] | 70 % |

- **Vorab ableitbar (Pflicht: Schreibtischrechnung je Leiter vor dem Bau):** GFR0 ganz [P]. GFR3: c-Zahl-Faktoren
  aendern die Huepfalgebra nicht (also M2 gleich A); das Vorzeichen in M3 folgt aus "jede Bindung an i kippt ihren
  kurzen Lift einmal" (Skizze). GFR4: Konjugation erhaelt alle Bindungswinkel (Skizze). Echt offen und in beide
  Richtungen scheiterfaehig: GFR1 (Jordan-Argument aus TWIST-PYRO-1 gilt nur fuer eine globale Projektion) und GFR2 (die
  Skizze G5 kann an Wandknoten mit eigenem Vorzeichen scheitern).
- **Bedeutung (vorab):** GFR2 und GFR3 treffen ein -> Spin kommt nur aus der Hebungsbuchhaltung, die Statistik aus dem
  Twist; zwei getrennte Regeln, Codex-Bedingung L4 nicht erfuellt; Folgekarte GERAHMTER-FADEN-2 (Quantenrotor j <= 1/2
  je Knoten, Huepfer transportieren den Rahmen; Frage U2). GFR2 scheitert (B gibt achsenunabhaengig -1 genau mit Ende)
  -> knotenweise LW-Rahmung traegt selbst Spin; Bauanleitung verkuerzt sich auf B1, B2, B6, B4.
- **Kontrollen:** ohne Ende; Achse = n_i (B muss +1 geben); 4-pi-Drehung (+1 in allen Varianten); Gegenprobe G1 aus
  TWIST-PYRO-1 (falsche Rahmungsrichtung muss anschlagen).
- **Aufwand:** klein, exakt, Kleintest-Spur der .69. Projekt-grep vor dem Bau (Hebung, Lift, w2, Rahmung, Konvention)
  durch die Leitung, mit den Pflicht-Ausschluessen. Synthetisch, keine Messdaten.

## 11. Gegensweep (Regel 4): "Was war so selbstverstaendlich, dass ich es nicht geprueft habe?"

- **G1 "Im Projekt dreht eine Raumdrehung den Rahmen mit."** Geprueft, durchgefallen [P]: GUERTEL-FINN-NETZ-1/PLAN.md
  Z. 42 "Innere Symmetrie: SO(3)"; Z2-SCHUTZ-1/PLAN.md Z. 30; Z2-SCHUTZ-1/KARTE.md Z. 10. -> B4 ist Pflicht.
- **G3 "Ein Rahmenfeld gibt dem Ende Spin."** Am Schreibtisch durchgefallen fuer den geordneten Rahmen [M, Skizze] -> B7.
- **G4 "Die 24-Monats-Suche deckt das Feld ab."** Mit Abruf 15 geprueft: Abdeckung duenn (API-Phrasensuche 0/4/170
  verrauscht). Urteile im Fenster nur "nach Recherchestand".
- **G5 "Eine Knotenkonvention aus einer Richtung reicht."** Am Schreibtisch durchgefallen [M, Skizze] -> B6, GFR2.
- **G2 "LWs Modell ist anomaliefrei."** Nur indirekt [P] (DYON-STATISTIK-L E4); gilt im BIB-Regime (V1).
- **Nicht geprueft:** G6 Goldstein/Turner-Formel fuer w2 (Chen/Kapustin [2]); Scorpan 2005 als Beleg fuer K1; Read/
  Chakraborty 1989 (bosonische Spinonen mit Spin 1/2) [L]; ob WWWs Vermutung auf dem dreiecksfreien Diamant gilt.

## 12. Kalibrierung

- **(a) Gemessen:** nichts. Zu Spin und Statistik emergenter Fadenend-Fermionen gibt es hier keine Messung; alle Quellen
  sind Theorie. Projektbefunde (TWIST-PYRO-1/-SPIN-1, Z2-SCHUTZ-2) sind synthetisch.
- **(b) Nuetzlich verdichtet:** "Spin und Statistik = eine Verschlingungszahl der Rahmung" (Thorngren); "fermionische
  Ladung = dynamische Spinstruktur, da = w2" (WWW); "feste Rahmung erlaubt spinlose Fermionen" (TWIST-SPIN-1 mit
  Chen/Kapustin, Creutz); Regel 6: Alle Wege zu Spin 1/2 (Rahmung, Isospin-Verriegelung, Ladung+Monopol, FR, Band)
  setzen dieselbe Groesse um, die Gleichsetzung "2-pi-Drehung = (-1)^F" (Erweiterungsklasse e2 = w2; Lan/Wen G_f,
  WWW Z2 x|_{w2} SO) [ES].
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** geordneter Rahmen = feste Rahmung (V3); G5 (Richtung reicht nicht);
  "GLB erlaubt FcFl" (Schluss aus einem Abstract-Satz plus S. 3); die Gitter-Skizze "oertliche 2-pi-Drehung = A_i".
- **Warnzeichen:** Meine Sicherheit, dass "Rahmung = Spin = Statistik" die Antwort ist, stieg stark, gestuetzt auf zwei
  Seiten Thorngren und einen Anhang von WWW. Zugleich hat sich die Frage in fuenf Regime aufgespalten (Abschn. 6), und
  auf dem Gitter erzwingt keine gefundene Bauweise den Zusammenhang. Das grobe Bild ist also nur im Kontinuum sicher.

## 13. Offene Fragen

1. R1/R2 (Leitung): Massstab fuer "echter Spin" (PSG 2T oder oertliche Rahmendrehung)? Ist Finns Tetraederlage selbst
   der Rahmen (starr) oder kommt ein eigenes Rahmenfeld dazu?
2. Gibt es eine Gitterregel fuer den Push-off mit einer Rahmung aus Knotenrahmen (nicht Projektion)? In den gelesenen
   Quellen (LW 2005/2006, Chen/Kapustin) stehen nur Projektionen.
3. Gilt WWWs "Verzweigung ~ Rahmung" auf dem dreiecksfreien Diamant, und laesst sich FcFl in einem GLB-Gitter bauen?
4. Wird der Spin-Statistik-Zusammenhang bei quantenhaften Rahmen erzwungen, wenn die Huepfer den Rahmen transportieren
   (Balachandran: Stetigkeit und Antiteilchen)? Folgekarte GERAHMTER-FADEN-2.
5. Datennaehe: In Quanten-Spin-Eis-Materialien tragen die Gitterplaetze Kramers-Dubletts (zwei Zustaende je Platz) [L];
   ob deren Spinonen eine projektive Punktgruppenklasse tragen, habe ich nicht gesucht.

## 14. Negativliste (darf nach dem Befund NICHT gesagt werden)

- "Ein Drehrahmen-Feld gibt den Fadenenden automatisch Spin 1/2." Geordnet wirkt es als feste Rahmung; im Projekt ist es
  eine innere SO(3).
- "Auf dem Gitter ist Spin-Statistik erzwungen." Creutz, Kramers-Boson, Bednorz' Vorzeichenwahl sprechen dagegen.
- "Die Z2-Wirbellinien des Rahmens sind die LW-Faeden." Nach da = w2 sind sie pi-Flusslinien fuer die Fermionen [ES].
- "WWW haben bewiesen, dass Verzweigung gleich Rahmung ist." Es ist eine Vermutung ("We conjecture", "may be related").
- "All-fermion-Elektrodynamik ist auf jedem 3D-Gitter unmoeglich." Belegt fuer das BIB-Regime; fuer GLB-Systeme ist die
  w2 w3-Ordnung trivial [S], die Folgerung ist [ES].
- "Bednorz hat ein Gittermodell mit emergenten Spin-1/2-Fermionen." Kontinuum; Statistik gewaehlt; kein Lorentz-Modell.
- "Freedman u. a. zeigen Spin-Statistik fuer bosonische Igel." Kontext freie Fermionen mit Majorana-Nullmoden.
- "Thorngren zeigt Spin 1/2 fuer Gitterfermionen." Kontinuum, anomale Randphasen.
- "GF2 ist widerlegt." Nur: nach Recherchestand nicht belegt.
- "Eine Projektion je Knoten traegt Spin 1/2." Schreibtisch G5 sagt nein; nicht gerechnet.
- "Die Bauanleitung ist gerechnet" oder "Spin 1/2 ist im Netz gezeigt." Nichts gerechnet.
- Die Zenodo-Schrift "The Vortex Framework" (2026) als Beleg: nicht gelesen, ohne Begutachtung, nur Werkzeug-Text.

## 15. Selbstanzeigen

1. **awk lokal benutzt** (18:57, Zeilenfilter in einer Seitenpruefung; Ausgabe nicht verwendet). Verstoss gegen die
   Regel "Lokal kein python, awk oder perl". Sonst lokal nur curl, pdftotext, pdfinfo, file, grep, sed, tr, fold, cut,
   uniq, wc, ls, mkdir, cat, jq (lesend), date, printf.
2. **Seitenzahlen aus "file"** zuerst falsch notiert (6 bzw. 19 S.); im ARBEITSFELD Abschn. 5 berichtigt (pdfinfo).
3. **Abrufzaehlung:** Abruf 1 umfasst einen leeren http-Vorversuch; Abrufe 2/3 und 8/9 waren je zwei curl in einem
   Befehl, einzeln gezaehlt; Abruf 4 lieferte 0 Treffer (Syntax) und ist gezaehlt.
4. **Nicht gelesen:** LW 2003 Volltext, Lan/Wen II Volltext, Wen 2017 Volltext, Gaiotto/Kapustin 2015, Scorpan 2005,
   Goldstein/Turner. Die Seitenangabe "S. ~3/~5" bei Chen/Kapustin ist aus dem Fliesstext geschaetzt.
5. **Thorngren 2014** liegt vor dem 24-Monats-Fenster; GF1 nennt "etwa 2018 bis 2026". Die tragenden neueren Stellen
   sind WWW 2022 und Chen/Kapustin 2018.
6. Schreibzugriffe nur in diesem Kartenordner (ARBEITSFELD.md, DOSSIER.md, quellen/). Nichts Versiegeltes geoeffnet;
   jedes grep ueber Projektordner mit den Pflicht-Ausschluessen (Einzeldatei-greps in Kartenordnern ohne Siegel).

## 16. Quellenliste

**Abgerufen (quellen/, Abrufnummer):**
- Levin, M.; Wen, X.-G. (2003): Fermions, strings, and gauge fields in lattice spin models. PRB 67, 245316.
  https://arxiv.org/abs/cond-mat/0302460 [S Abstract] Abruf 1.
- Levin, M. A.; Wen, X.-G. (2005): String-net condensation: A physical mechanism for topological phases. PRB 71, 045110.
  https://arxiv.org/abs/cond-mat/0404617 [S] S. 11-12; 2D-Teil Fluss-Z. 1460-1466. Abrufe 1, 2.
- Thorngren, R. (2014): Framed Wilson operators, fermionic strings, and gravitational anomaly in 4d. arXiv v2
  2014-11-09, ohne Zeitschriftenangabe im arXiv-Eintrag.
  https://arxiv.org/abs/1404.4385 [S] S. 1-6. Abrufe 1, 3.
- Fidkowski, L.; Haah, J.; Hastings, M. B. (2022): Gravitational anomaly of 3+1 dimensional Z2 toric code with fermionic
  charges and fermionic loop self-statistics. PRB 106, 165135. https://arxiv.org/abs/2110.14654 [S Abstract] Abruf 1.
- Fidkowski, L.; Haah, J.; Hastings, M. B. (2020): An exactly solvable model for a 4+1D beyond-cohomology SPT phase.
  PRB 101, 155124. https://arxiv.org/abs/1912.05565 [S Abstract] Abruf 1.
- Chen, Y.-A.; Kapustin, A. (2019): Bosonization in three spatial dimensions and a 2-form gauge theory. PRB 100, 245127.
  https://arxiv.org/abs/1807.07081 [S] Fig. 2, Abschn. Triangulierung. Abrufe 1, 10.
- Lan, T.; Wen, X.-G. (2019): A classification of 3+1D bosonic topological orders (II). PRX 9, 021005. https://arxiv.org/abs/1801.08530
  [S Abstract] Abruf 1.
- Chen, Y.-A.; Hsin, P.-S. (2023): Exactly solvable lattice Hamiltonians and gravitational anomalies. SciPost Phys. 14, 089.
  https://arxiv.org/abs/2110.14644 [S Abstract] Abruf 1.
- Thorngren, R.; Else, D. V. (2018): Gauging spatial symmetries and the classification of topological crystalline phases.
  PRX 8, 011040. https://arxiv.org/abs/1612.00846 [S Abstract] Abruf 1.
- Cheng, M.; Wang, C. (2022): Rotation symmetry-protected topological phases of fermions. PRB 105, 195154.
  https://arxiv.org/abs/1810.12308 [S Abstract] Abruf 1.
- Freedman, M.; Hastings, M. B.; Nayak, C.; Qi, X.-L.; Walker, K.; Wang, Z. (2011): Projective ribbon permutation
  statistics. PRB 83, 115132. https://arxiv.org/abs/1005.0583 [S] Fluss-Z. 280-290, 575-590, 1740-1810. Abrufe 1, 14.
- Hsin, P.-S.; Lam, H. T.; Seiberg, N. (2019): Comments on one-form global symmetries ... SciPost Phys. 6, 039.
  https://arxiv.org/abs/1812.04716 [S Abstract] Abruf 1 (nicht verwendet).
- Seiberg, N.; Witten, E. (2016): Gapped boundary phases of topological insulators via weak coupling.
  https://arxiv.org/abs/1602.04251 [S Abstract] Abruf 1.
- Kapustin, A.; Thorngren, R. (2017): Fermionic SPT phases in higher dimensions and bosonization. JHEP 10 (2017) 080.
  https://arxiv.org/abs/1701.08264 [S Abstract] Abruf 1.
- Zhou, S.-T.; Cheng, M.; Rakovszky, T.; von Keyserlingk, C.; Ellison, T. D. (2025): Finite-temperature quantum
  topological order in three dimensions. https://arxiv.org/abs/2503.02928 [S Abstract] Abruf 5.
- Bednorz, A. (2018): Local bosonization of massive fermions in three spatial dimensions with rotation invariance.
  PRD 98, 036012. https://arxiv.org/abs/1804.11160 [S] S. 1-2, Tauschterm, Stabilitaet. Abrufe 7, 8.
- Wen, X.-G. (2017): Exactly soluble local bosonic cocycle models, statistical transmutation, and simplest
  time-reversal symmetric topological orders in 3+1D. PRB 95, 205142. https://arxiv.org/abs/1612.01418 [S Abstract]
  Abruf 7.
- Wan, Z.; Wang, J.; Wen, X.-G. (2022): 3+1d boundaries with gravitational anomaly of 4+1d invertible topological order
  for branch-independent bosonic systems. PRB 106, 045127. https://arxiv.org/abs/2112.12148 [S] S. 2-3, Fussnote 1,
  Fluss-Z. 1900-1915, 2748-2792, Anhang C (Fluss-Z. 3905-3985). Abrufe 7, 9.
- Zhang, Z.-F.; Wang, Q.-R.; Ye, P. (2023): Continuum field theory of 3D topological orders with emergent fermions and
  braiding statistics. PRR 5, 043111. https://arxiv.org/abs/2307.09983 [S Abstract] Abruf 7.
- Creutz, M. (2014): Emergent spin. Ann. Phys. https://arxiv.org/abs/1308.3672 [S Abstract] Abruf 7.
- Balachandran, A. P.; Daughton, A.; Gu, Z. C.; Marmo, G.; Sorkin, R. D.; Srivastava, A. M. (1993): Spin-statistics
  theorems without relativity or field theory. IJMPA 8, 2993-3044. INSPIRE-API [S Abstract] Abruf 11.
- Nur Werkzeug-Kurztext [W], nicht gelesen: Gaiotto/Kapustin (2015) https://arxiv.org/abs/1505.05856;
  "Fermionic Gaussian PEPS in 3+1d" https://arxiv.org/abs/2304.06744; Zenodo https://zenodo.org/records/18575279;
  Z2-Gittereichtheorien https://arxiv.org/abs/1708.08507, https://arxiv.org/abs/2011.01500,
  https://arxiv.org/abs/1908.10453, https://arxiv.org/abs/2408.14295; https://arxiv.org/abs/2508.02370. Abrufe 6, 13, 15.

**Lokal gelesen (kein Abruf):**
- Levin, M.; Wen, X.-G. (2006): Quantum ether: photons and electrons from a rotor model. PRB 73, 035122.
  https://arxiv.org/abs/hep-th/0507118 [S] Fluss-Z. 555-600, 850-870 (Kopie twist-pyro-1/quellen/).
- Ning, S.-Q.; Zou, L.; Cheng, M. (2020): Fractionalization and anomalies in symmetry-enriched U(1) gauge theories.
  PRR 2, 043043. https://arxiv.org/abs/1905.03276 [S] Z. 1500-1520, 1748-1775, 3194-3218, 3384-3392 (Kopie
  dyon-statistik-l/quellen/).
- Projekt [P]: TWIST-PYRO-1, TWIST-SPIN-1, KRUEMMUNG-SPANNUNG-SPIN-L, DYON-STATISTIK-L, IDEEN-SPIN-ZEIT, Z2-SCHUTZ-1/-2,
  GPU-Z2-1, GUERTEL-FINN-NETZ-1 (PLAN Z. 42), GEN-04-SPIN-HALB, RUNDE-46/LUECKEN-ABGLEICH (L4), RUNDE-49 (VK3),
  QUARK-1.

**Nur Gedaechtnis [L]:** Scorpan 2005; Goldstein/Turner (w2 auf Triangulierungen); Read/Chakraborty 1989; Kramers-
Dubletts in Spin-Eis-Materialien.

## 17. Einfach gesagt

Ein Teilchen am Ende eines Fadens wird zum Elektron-artigen Teilchen mit halbem Spin, wenn der Faden wie ein Band eine
"Seite" hat und das Teilchen dieses Band beim Drehen mitverdreht; dann kommen das Minuszeichen beim Drehen und das beim
Vertauschen aus derselben Verdrehung. Auf Finns Netz klappt das bisher nicht, weil die Bandseite von aussen fest
vorgegeben ist (wie eine feste Blickrichtung), und ein einfach geordnetes Rahmenfeld wuerde genau dasselbe tun. Die
Literatur liefert die Zutaten (Rahmen und Faden auf derselben Kante koppeln, Rahmen an den Raum binden, das Fadenende den
Rahmen mitnehmen lassen); ob sie auf Finns Netz zusammenpassen, muss eine kleine exakte Rechnung zeigen.

---
Endzeit (date, beim Schreiben dieser Zeile): 2026-10-05 19:02:50 CEST. Abrufe 15 von 15. Zeitbox (bis 19:57:32) eingehalten.
