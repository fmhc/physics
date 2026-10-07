# ARBEITSFELD FARB-EIS-R3-L (feldforscher fuer claude-primary, Runde 43)

- Start (date): 2026-10-04 19:14:50 CEST. Zeitbox 35 min, also Ende spaetestens 19:49:50 CEST.
- Karte gelesen (KARTE.md, 32 Zeilen). Vorarbeit gelesen: gluonen-l/DOSSIER.md Abschn. 5.3, 5.5, K2, 12-14 (sed).
- Abrufbudget: 4 gezielte arXiv-Abrufe. Verbraucht: 0.
- Kennzeichen: [S] mit Zeile, [S Abstract], [P], [L], [L?], [M], [ES], [H].

## Offene Rueckfragen (wandern mit)

- R3 (aus GLUONEN-L): Rishonzahl im SU(3)-Quantenlink bei Brower/Chandrasekharan/Wiese, 1 oder N? -> Frage 1.

## A1 Erwartung (geschrieben 19:17:42 CEST, vor dem Abruf)

- Quelle: Brower/Chandrasekharan/Wiese, hep-th/9704106, Volltext-PDF von arxiv.org.
- Karten-Erwartung E1 (Leitung): feste Rishonzahl je Kantenende, im kleinsten Raum 1 [L?].
- Meine Erwartung vor dem Abruf [L?, aus Gedaechtnis]: Die Rishonzahl ist je **Kante** (Summe beider Enden) erhalten,
  nicht je Ende. Fuer U(N) ist jede Rishonzahl erlaubt; fuer SU(N) wird die U(1) durch det U gebrochen, und det U ist
  nur im Sektor mit **N Rishons je Kante** ungleich null. Also waehlen die Autoren fuer SU(3) Rishonzahl 3 (C(6,3) = 20
  Zustaende je Kante), nicht 1. Wenn das zutrifft, ist E1 im Teil "1" verletzt, und das farbige Pfeil-Eis mit einem
  Rishon je Ecke ist kein SU(3)-, sondern ein U(3)-artiges Modell mit eingefrorenen U(1)-Ladungen.
- Was mich ueberraschen wuerde: eine ausdrueckliche Wahl "ein Rishon je Kante" fuer SU(N), oder gar keine Festlegung.

## A1 Ausgang (Abruf 19:17:57, gelesen bis 19:18:14; Text quellen/A1-bcw-9704106.txt, arXiv v1 vom 14.04.1997, 27 S.)

- Bestaetigt: Rishonzahl ist je **Kante** erhalten (Gl. 4.4, Z. 676-686: "commute with the rishon number operator ...
  on each individual link ... superselection sectors of fixed rishon number for each link ... equivalent to working in
  a given irreducible representation of SU(2N)") [S].
- Bestaetigt: QCD-Wahl ist N Rishons je Kante: det U nur bei "exactly N = N fermionic rishons on each link" ungleich
  null (Z. 708-712, Gl. 4.6-4.7); "(2N)!/(N!)^2-dimensional representation of SU(2N) is the smallest with a
  non-vanishing determinant ... For QCD ... 20-dimensional Hilbert spaces associated with each link" (Z. 440-444) [S].
- Bestaetigt: Fundamentale Darstellung (= 1 Rishon, 2N Zustaende): "the operator that represents detU ... turns out
  to be zero. Hence, in that case even the Hamiltonian of eq.(2.20) has a U(N) gauge invariance" (Z. 434-438) [S].
- **Verstoss 1 (gegen meine Erwartung "SU(3) verlangt 3"):** Z. 462-467: U(1) auch brechbar "by antisymmetrized
  combinations of various paths connecting two lattice points ... one can construct SU(N) invariant quantum link
  Hamiltonians even with the fundamental representation of SU(2N), but with more complicated interactions. In the
  15-dimensional representation of SU(6) one can construct a more complicated plaquette action that leads to an SU(3)
  invariant theory, even without the link determinant term." -> Rishonzahl 1 ist fuer SU(3) **nicht ausgeschlossen**,
  aber nur mit nichtlokalen, antisymmetrisierten Mehrwegtermen, die BCW nicht ausschreiben [S].
- **Verstoss 2 (unerwartet):** "Baryon" steht schon bei BCW: det U "shifts an entire rishon-baryon — a color neutral
  combination of N rishons — along the link" (Z. 749-751, Bild 2 Z. 168-170); "For odd N this object would hence be a
  fermion" (Z. 1097-1100). Das ist ein Baryon am **Kantenende** (N Rishons einer Kante), nicht unser Knoten-Baryon
  (drei Rishons aus drei Kanten an einem Tetraeder) [S, ES].
- Folgerung [M, aus S Z. 434-438 und Gl. 4.4]: Mit 1 Rishon je Kante und nur Ring-/Plakettentermen ist das Modell
  U(3)-invariant; die U(1)-Ladung je Tetraeder (k - 2) ist erhalten. Jede k-Verteilung ist ein eigener Sektor.
- E1 (Karte): **verletzt** in zwei Punkten: Rishonzahl ist je Kante (nicht je Kantenende) fest; BCW waehlen fuer SU(3)
  N = 3 (20 Zustaende), nicht 1.

## Schreibtisch [M] nach A1 (nicht gegengelesen, keine Rechnung ausgefuehrt)

- Rishonzahl 1, k je Tetraeder in {0, 3}. Leere Tetraeder (E) sind nie benachbart (Kantenrishon sitzt an einem Ende).
  Baryon-Tetraeder (B) geben genau einen Rishon ab ("Aus-Grad 1"); alle B-E-Kanten zeigen in B. Im B-B-Teilgraphen hat
  jeder Knoten Aus-Grad 1 -> jede Komponente hat gleich viele Kanten wie Knoten (ein Kreis), 2 Orientierungen je
  Komponente (Kreis links oder rechts herum).
- Also: Zustaende = Summe ueber gueltige E von 2^c(E). c(E) <= N_B/6 = N_tet/9 (kleinster Kreis im Diamant: 6).
- Zweite Lesart: jede Konfiguration = Zerlegung der Diamant-Kanten in "Klauen" K_{1,3} (drei Kanten an einem Knoten)
  = Ueberdeckung der Pyrochlor-Plaetze durch Dreiecks-Trimere (Flaechen der Tetraeder), je Tetraeder hoechstens eines.
  Graphentheoretisch: Orientierung mit Eingangsgrad = 0 mod 3 (Claw-Decomposition) [M; Bezug Barat/Thomassen [L?]].
- Sechsring-Zug haelt E fest und dreht nur Komponenten, deren Kreis ein Sechsring ist -> jede Zusammenhangskomponente
  hat hoechstens 2^(N_tet/9) Zustaende; bei N_tet = 54 hoechstens 64.
- Folge fuer das K2-Band "groesste Komponente > 50 %": nur moeglich bei hoechstens 128 Zustaenden insgesamt, also
  ln(Zahl)/54 <= ln(128)/54 = 0,090 < 0,10. "Extensiv und zusammenhaengend" ist bei N_tet = 54 ausgeschlossen
  -> Zusammenhangsband vorab ableitbar, sobald das Entropieband besteht [M].

## Projekt-grep (19:19:58 bis 19:20:48, Ausschluesse wie vorgeschrieben)

- "claw decomposition", "rishon-baryon": 0 Treffer. "trimer": viele Treffer, aber andere Bedeutung (Wirbel-Trimer
  Eto/Nitta, E_trimer-Energien, Interatomare Potentiale p12-2204.09563) [P]. "null oder drei rein"/FARB-EIS-1 nur in
  GLUONEN-L und Leitungs-Arbeitsfeld [P].

## A2 Erwartung (geschrieben 19:21:05 CEST, vor dem Abruf)

- Quelle: arXiv-API, eine kombinierte Suche: (trimer UND (pyrochlore ODER diamond ODER "gauge theory" ODER baryon ODER
  "quantum link")) ODER "claw decomposition(s)" ODER (rishon UND baryon). max 80 Treffer.
- Karten-Erwartung E2: "null oder drei rein" = Baryon-Gesetz starker Kopplung bzw. SU(3)-Dimer/Trimer-Modelle [L?].
- Meine Erwartung: (a) Quanten-Trimer-Modelle vor allem auf Kagome/Dreieck (SU(3)-Trimer-RVB, Z3-Topologie,
  Rydberg), kein Pyrochlor-/Diamant-Treffer; (b) das Baryon-Gesetz der starken Kopplung (Monomer-Dimer-Polymer, n_M +
  Summe n_D = 3 je Platz, Baryon-Schleifen) erscheint in dieser Suche nicht in Trimer-Sprache; (c) Graphentheorie:
  Claw-Decompositions von 4-regulaeren bzw. 5-kantenzusammenhaengenden Graphen mit Bezug zu Tuttes 3-Fluss-Vermutung
  und Mod-3-Orientierungen; (d) rishon UND baryon: wenige Treffer (SO(3)/SU(3)-Quantenlink in 1D).
- Ueberraschung waere: Trimer-/Klauen-Ueberdeckung des Diamant- oder Pyrochlor-Gitters mit Entropie, oder ein
  SU(3)-Quantenlink auf Diamant/Pyrochlor.

## A2 Ausgang (Abruf 19:21:35; 21 Treffer insgesamt; quellen/A2-api-trimer-claw-rishonbaryon.xml)

- (c) **Verstoss 3 (Teil):** Claw-Decomposition ist bekannt, aber ihre Existenz folgt **nicht** aus der Teilbarkeit:
  "In 2006 Barat and Thomassen conjectured that every planar 4-edge-connected 4-regular simple graph of size divisible
  by three admits a claw-decomposition. Later, Lai (2007) disproved this conjecture ... smallest one contains 24
  vertices"; Hasanvand gibt 18 Knoten und eine Familie planarer 4-zusammenhaengender Gegenbeispiele; positiv: "every
  5-edge-connected graph of size divisible by three admits a claw-decomposition if it is essentially 6-edge-connected or
  planar" (Hasanvand 2022, arXiv:2205.09063) [S Abstract]. Diamant-Torus ist 4-regulaer, nur 4-kantenzusammenhaengend,
  nicht planar -> keiner der Saetze greift; Existenz je Haufen offen [ES].
- (a) bestaetigt: Quanten-Trimer in 2D: Giudice/Surace/Pichler/Giudici 2022 (tRVB, "Trimers are defined as two
  adjacent edges on a graph", Z3-Topologie, Anschluss an Z3-Gittereichtheorie, Rydberg) [S Abstract]; Zhang/Mao/Kim/
  Moessner 2024 (triangulares Trimer-Modell, U(1)xU(1)-Eichtheorie) [S Abstract]; Propp 2022/24 (Trimer-Ueberdeckungen
  des Dreiecksgitters, "twenty mostly open problems") [S Abstract]; Akutsu/Akutsu 2001 (Trimer-Monomer, Dreiecksgitter
  = Diamant-(111)-Oberflaeche, 3-Zustands-Vertexmodell) [S Abstract].
- Unerwartet (klein): Pyrochlor-Material mit Dreiecks-Trimeren: CsW2O6, "each of W 5d electrons are confined in
  regular-triangle W3 trimers ... charge order satisfying the Anderson condition in a nontrivial way" (Okamoto u. a.
  2020, Nat. Commun. 11, 3144; arXiv:2006.11053) [S Abstract]; Uebersicht Okamoto 2024 (arXiv:2406.13981) [S Abstract].
  Ob dort alle Plaetze in Trimeren sitzen (perfekte Ueberdeckung), steht nicht im Abstract [L?].
- (b) bestaetigt: Baryon-Gesetz der starken Kopplung erscheint nicht. (d): "rishon UND baryon" nur Preonen-Rishons
  (Zenczykowski 2011, 2018) -> Rauschen.
- Lokal (ohne Abruf) aus GLUONEN-L F10: Cataldi/Calajo/Silvi/Montangero/Halimeh 2025/26 (arXiv:2505.04704, PRL 136,
  170401): "encoding gauge superselection sectors into static SU(2) background charges ... a fragmented phase that is
  nonthermal but delocalized" [S Abstract, lokal]. Passt zur Folgerung, dass die k-Verteilung als statische
  U(1)-Hintergrundladung wirkt [ES].

## A3 Erwartung (geschrieben 19:23:51 CEST, vor dem Abruf)

- Quelle: arXiv-API, Zeitfenster 24 Monate (submittedDate 2024-10-04 bis 2026-10-04): (trimer UND (pyrochlore ODER
  diamond ODER "spin ice" ODER gauge ODER "three-dimensional")) ODER ("quantum link" UND (baryon ODER fragmentation
  ODER rishon(s))) ODER (claw UND decomposition). Zweck: Regel 7 fuer E3 (Negativaussage "nicht bekannt").
- Erwartung: (a) Trimer: 2D-Arbeiten (Kagome, Dreieck, Rydberg), hoechstens eine 3D-Arbeit, keine Zaehlung auf
  Diamant/Pyrochlor; (b) Quantenlink: einige Arbeiten zu Fragmentierung in U(1)- und SU(2)-Quantenlinks (1D/2D),
  vielleicht SU(3) in 1D/2D mit Rishons; kein SU(3)-Rishon-1-Modell in 3D; (c) Claw: 0 bis 2 Graphentheorie-Treffer.
- Ueberraschung waere: SU(3)-Quantenlink oder Trimer-/Klauenmodell auf Diamant/Pyrochlor, oder eine Zaehlung.

## A3 Ausgang (Abruf 19:24:12; 19 Treffer, viel Rauschen durch "claw"/"decomposition"; quellen/A3-api-24m-trimer-qlink-claw.xml)

- (a) bestaetigt: keine Trimer-/Klauenzaehlung auf Diamant/Pyrochlor in 24 Monaten. 3D-"Trimer" nur als Spin-Trimer-
  Magnet (Gomilsek u. a. 2026, arXiv:2605.06752) -> andere Bedeutung [S Abstract].
- (c) bestaetigt: keine neue Claw-Decomposition-Arbeit zu Gittern.
- (b) **Verstoss 4 (Richtung: staerker als erwartet):** Fragmentierung ist fuer U(1)-Quantenlinks inzwischen ein
  allgemeiner Satz: "any exact U(1) higher-form symmetry ... presents a fundamental obstruction to ergodicity under
  unitary dynamics in lattice systems with local interactions and finite on-site Hilbert space dimension. Focusing on
  the two-dimensional case ... necessarily exhibit Hilbert space fragmentation ... Krylov sectors whose number scales
  exponentially with system size ... including quantum link models" (Sohal/Verresen, arXiv:2511.21815, PRL 137, 060401
  (2026)) [S Abstract]. 3D: "3D U(1) quantum dimer models ... (also generically called quantum link models) with
  staggered charged static matter ... geometric fragmentation ... number of fragments is exponential in the linear
  system size" (Steinegger/Banerjee/Huffman/Rammelmueller, arXiv:2508.03802, PRD 112, 114512 (2025)) [S Abstract].
  Rishons 2026 nur U(1) ("virtual rishon", Rogerson u. a., arXiv:2603.05151) [S Abstract].
- E3 nach Regel 7: "Zaehlung und Zusammenhang auf Diamant/Pyrochlor nicht allgemein bekannt" -> nach Recherchestand
  (A2 ohne Zeitfenster, A3 mit 24 Monaten, GLUONEN-L F8/F10/F12) **nicht gefunden**; der Zusammenhang ist aber
  durch die U(1)-Erhaltung (A1) und allgemeine Fragmentierungssaetze (A3) weitgehend vorgezeichnet [ES].

## A4 Erwartung (geschrieben 19:24:53 CEST, vor dem Abruf) -- zugleich Gegensweep-Pruefung

- Quelle: de Forcrand/Fromm, "Nuclear physics from lattice QCD at strong coupling", arXiv:0907.1915 (Volltext-PDF).
  Gegensweep-Punkt: Das "Baryon-Gesetz der starken Kopplung" (Karte E2) habe ich nur aus dem Gedaechtnis.
- Erwartung [L?]: Bei starker Kopplung (beta = 0, gestaffelte Fermionen) gilt je Platz die Grassmann-Bedingung
  n_M(x) + Summe der Dimer-Besetzungen = N_c = 3, ausser der Platz liegt auf einer orientierten, selbstvermeidenden
  Baryon-Schleife. Das ist eine Saettigung auf 3 (Mesonen-Dimere, Quarks), nicht "null oder drei rein" fuer Rishons.
  E2-Teil "Baryon-Gesetz" waere dann nur Analogie.
- Ueberraschung waere: eine Formulierung als "null oder drei Quarklinien je Platz" oder ein reines Eichfeld-Gesetz.

## A4 Ausgang (Abruf 19:25:10; quellen/A4-dff-0907.1915.txt, 4 S.)

- **bestaetigt** (eine Zeile): "Because each site hosts Nc = 3 Grassmann fields chi and 3 fields chibar, a triality
  constraint arises: each site is attached to exactly 3 dimers, or is traversed by a baryon loop. Thus, baryon loops
  are self-avoiding" (Z. 76-87); Dimere n = 0..3 je Kante (Z. 95-99) [S]. -> Saettigung auf 3 bzw. Baryon-Schleife,
  nicht "null oder drei rein"; gemeinsam ist nur die Trialitaet [ES].

## Gegensweep (19:25-19:27)

- G1 (geprueft, A4): Baryon-Gesetz der starken Kopplung -> bestaetigt, nur Analogie.
- G2 (geprueft, lokal in A1): Erhaelt der Ringterm jedes k? BCW schreiben die Plakette als Produkt von "color neutral
  glueballs formed by two rishons located at the same corner of a plaquette" (Z. 746-748): jeder Faktor verschiebt
  einen Rishon zwischen zwei Kantenenden am selben Platz -> k je Platz erhalten [S, M].
- G3 (nicht geprueft): Ob die Zeitschriftenfassung (Phys. Rev. D, 1999) von arXiv v1 abweicht, insbesondere Z. 462-468.
- G4 (nicht geprueft): Kleinster Kreis im Diamant = 6 [L]; auf dem 3x3x3-Torus (N_tet = 54) sind Windungskreise
  ebenfalls 6 lang [M]. Traegt die Schranke c(E) <= N_tet/9.
- G5 (nicht geprueft): Pauling-Schaetzung (5/4)^N_tet fuer die Gesamtzahl; nur die Obergrenze je k-Muster ist [M].

## Abschluss

- DOSSIER.md geschrieben ab 19:27:00, Wortlaut-Korrektur ab 19:29 (Sicherung DOSSIER.md.bak-vor-korrektur), Ende 2026-10-04 19:30:44 CEST (date).
- Abrufe 4 von 4. Offene Rueckfrage R3: erledigt (DOSSIER Abschn. 4). Neue offene Fragen F1 bis F5 im DOSSIER Abschn. 9.
