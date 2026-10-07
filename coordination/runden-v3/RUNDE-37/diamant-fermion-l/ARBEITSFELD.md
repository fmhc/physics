# DIAMANT-FERMION-L: Arbeitsfeld (feldforscher fuer claude-primary)

- Start 2026-10-04 22:32:11 CEST (date). Zeitbox 60 min, also bis etwa 23:32 CEST.
- Dieses Feld wird vor jedem Schritt neu gelesen. Gestrichenes bleibt stehen (~~so~~), offene Rueckfragen wandern mit.
- Kennzeichen: [S Z.] Quelle mit Zeile der lokalen Kopie, [S Abstract], [S-lokal] lokale Kopie eines frueheren
  Agenten, selbst gelesen, [P] Projektdatei, [L] Gedaechtnis, [M] Mathematik von Hand (ungeprueft), [ES], [H].

## 0. Gelesen vor dem ersten Abruf (lokal, 22:32 bis 22:42)

- KARTE.md (bindend; DF1 bis DF3 unveraendert).
- licht-finn-netz-1/ERGEBNIS.md ganz (Abschnitte 1, 3, 4 genau), PLAN.md (Zeile W-D), code/licht_netz.py Z. 1-58,
  153-166 (weyl_matrix: Bindung i -> j mit 0,5 i (sigma.n) e^{ik.d}; D_BOND = (a/4) t_a, t_a = (1,1,1), (1,-1,-1),
  (-1,1,-1), (-1,-1,1); a = 2 sqrt2 PU, b = sqrt6/2 PU).
- weyl-linear-1/ERGEBNIS.md ganz (Umrechnung l = hbar c / (2 abs(lambda1) E_QG,1), Phase gegen Gruppe).
- strang-anker-l/DOSSIER.md ganz (Anker; JLM nur Abstract, "order unity"; 9,6e20 GeV ist Photon-Schranke).
- Lokale Quelle vorhanden: RUNDE-34/grb-221009a/quellen/jlm-hep-ph-0209264.txt (JLM PRD 2003, Volltext). Sie ist
  aelter als die Crab-Synchrotron-Arbeit (dort Ref. [60], Z. 2201).

## 1. Schreibtisch vor jedem Abruf [M, von Hand, nicht numerisch geprueft]

### 1.1 W-D langwellig

- H = [[0, M], [M^dag, 0]] (Untergitter A, B), M(k) = (i/2) sum_a (sigma.n_a) e^{ik.d_a} = (i/2) sigma.V(k),
  V(k) = sum_a n_a e^{ik.d_a}, d_a = b n_a.
- Momente des Tetraedersterns: sum n_a = 0; sum n_a^i n_a^j = (4/3) delta_ij; sum n_a^i n_a^j n_a^l =
  (4/(3 sqrt3)) abs(eps_ijl) (nur alle drei Indizes verschieden). Das dritte Moment ist ungleich null, weil der
  Knoten kein Inversionszentrum ist.
- Daraus M = c [sigma.k + i eps sigma.q + O(k^3)], c = -2b/3, eps = b/sqrt3, q = (k_y k_z, k_z k_x, k_x k_y).
- Also H = c [tau_x (x) sigma.k - eps tau_y (x) sigma.q] + ... (tau auf den Untergittern).
- M M^dag = k^2 + eps^2 q^2 - 2 eps sigma.(q x k) -> E = abs(c) k [1 -+ eps abs(q^(n) x n) k + ...].
  a1 = +-(b/sqrt3) abs(q^(n) x n): 110 -> +-sqrt2/4 = +-0,3536; 100 und 111 -> 0. abs(c) = 2b/3 = 0,8165.
  Trifft ERGEBNIS Abschnitt 3 (Tempo 0,8165; a1 +-0,3536) [P].

### 1.2 Was spaltet, sind keine Helizitaeten

- Bei eps = 0 sind die zwei Zustaende mit E = +abs(c)k: R = (tau_x = +1, Helizitaet +) und L = (tau_x = -1,
  Helizitaet -). gamma5 = tau_x (vertauscht mit tau_x sigma.k).
- Die Stoerung tau_y sigma.q hat in R und L den Erwartungswert 0 (tau_y antikommutiert mit tau_x). Sie koppelt R mit
  L ueber die Querkomponente abs(q x k^). Die aufgespaltenen Zustaende sind (R +- e^{i phi} L)/sqrt2: Helizitaet
  im Mittel 0, Spin quer zu k (laengs +-(q x k)), Chiralitaet gemischt.
- Feldtheoretisch: tau_y sigma_i = -i gamma^i (mit beta = tau_z), also Term ~ psibar sigma^{0i} psi (d_j d_l)
  abs(eps_ijl): Tensor-Typ der Dimension 5 (SME-Familie H^(5)?), nicht der Myers-Pospelov-Typ
  psibar (n.gamma)(eta1 + eta2 gamma5)(n.d)^2 psi. [M; Zuordnung zur SME-Familie [L], offen.]
- Folge fuer DF3: Die Schranken der Literatur sind fuer helizitaetsabhaengige (CPT-ungerade) Terme formuliert. Fuer
  W-D gilt in jeder generischen Richtung: ein Zweig superluminal, einer subluminal, gleich gross. Uebertragbarkeit
  ist [ES] und zu pruefen.

### 1.3 Pruefung der Schreibtischaussage der Leitung (sigma.q unter O verboten)

- Gruppentheorie richtig fuer einen 2x2-Operator: In O ist sigma ~ T1 (axial oder polar ist in O gleich, O hat nur
  eigentliche Drehungen), q ~ T2, T1 x T2 = A2 + E + T1 + T2: keine Invariante. Explizit C4z: k -> (-k_y, k_x, k_z),
  q -> (q_y, -q_x, -q_z), sigma -> (-sigma_y, sigma_x, sigma_z), sigma.q -> -sigma.q.
- Fuer W-D falsch: Der Term steht im Kanal tau_y. Die Elemente von O ohne T (4_1-Schraube, zweizaehlige Achsen
  laengs 110) tauschen die Untergitter: V = tau_x (x) U(R), tau_y -> -tau_y. Zusammen mit sigma.q -> -sigma.q ist
  tau_y sigma.q invariant (A2 x A2 = A1). Im Lagegeeichten Bloch-Bild gibt die Translation nur eine gemeinsame Phase.
- W-D hat die 4_1-Schrauben schon: T_ij = (i/2) sigma.n_ij haengt nur von der Bindungsrichtung ab, also ist jede
  eigentliche Gitterdrehung (mit Spin-Drehung U(R)) Symmetrie, auch mit Untergittertausch. Raumgruppe der
  eigentlichen Drehungen F4_1 3 2, Punktgruppe O.
- Uneigentliche Elemente: Inversion (Bindungsmitte) und Spiegel bilden H auf -H ab; mit dem Untergitter-Operator
  Gamma = tau_z sind P Gamma und M Gamma Symmetrien. Auch sie lassen tau_y sigma.q stehen (geprueft fuer P Gamma ~ tau_y
  und einen Spiegel x <-> y mit axialem Spin).
- Zeitumkehr Theta = i sigma_y K: tau_y sigma.q gerade. Untergitter-Chiralitaet: erlaubt (antikommutiert mit tau_z).
- T_d-Teil der Aussage: Mit axialem sigma ist sigma.q unter T_d A2 (Spiegel x <-> y: q -> (q_y, q_x, q_z),
  sigma -> -(sigma_y, sigma_x, sigma_z)), also verboten. "Unter T_d erlaubt" gilt nur, wenn sigma wie ein polarer
  Vektor transformiert, oder im Kanal tau_y mit M Gamma. Unter T erlaubt: richtig.
- **Urteil [M]:** Die Aussage stimmt fuer einen Ein-Untergitter-Operator (2x2) und ist fuer Finns Diamant-Operator
  falsch. Die Drehung um 90 Grad (als 4_1-Schraube) verbietet die Spaltung nicht; W-D hat sie bereits.
- Ursache [ES, Feldregel 6]: das dritte Moment sum w_v v v v des Sprungsterns (Knoten ohne Inversionszentrum).

### 1.4 Gegenterm ohne Symmetriebruch (Verbesserung) [M]

- A -> B-Vektoren in Einheiten a/4: ungerade Koordinaten, Summe = 3 mod 4. Schale 1: 4 Vektoren (1,1,1)-Typ,
  Produkt v_x v_y v_z = +1. Schale 3 (Laenge sqrt11): 12 Vektoren (+-1, +-1, +-3)-Typ, alle mit Produkt -3.
- Sprung T_v = (i/2) w_s sigma.v (unnormiert). Zweites Moment: Schale 1: 4 delta, Schale 3: 44 delta. Drittes Moment
  (Koeffizient von abs(eps)): Schale 1: +4, Schale 3: -36.
- sigma.q-Term ~ 4 w1 - 36 w3 = 0 fuer w3 = w1/9. sigma.k-Term ~ 4 w1 + 44 w3 = (80/9) w1, bleibt.
- Alle Symmetrien aus 1.3 bleiben (T_ij haengt nur vom Bindungsvektor ab). Die naechste Spaltung kaeme aus dem
  fuenften Moment (Kanal tau_y, Ordnung k^4 in M): relative Spaltung ~ k^3, also Dimension 7.
- Das ist eine feste Zahl auf Baumniveau (Naik-/Symanzik-artig), keine Symmetrie. In einer wechselwirkenden Theorie
  waere der Koeffizient abzustimmen, weil kein Symmetriegrund ihn festhaelt [ES].
- Offen: Tempo-Isotropie bleibt (Rang-2-Tensor kubisch). Nullstellen des verbesserten Operators: nicht geprueft.

### 1.5 Doppler von W-D: Knotenlinien [M] (unerwartet; nicht in der Karte)

- det M = (i/2)^2 det(sigma.V) = (1/4) V.V (komplex-bilinear). Nullstellen: V.V = 0, also Re V senkrecht Im V und
  abs(Re V) = abs(Im V). Zwei reelle Bedingungen in 3D: generisch Linien.
- Ebene k_x = 2 pi/a, k = (2 pi/a)(1, u, v), alpha = (pi/2)(u+v), beta = (pi/2)(u-v):
  V = (2/sqrt3) (i (cos alpha + cos beta), sin beta - sin alpha, -(sin alpha + sin beta)). Re V senkrecht Im V auf der
  ganzen Ebene. Nullbedingung: 2 sin^2 alpha + 2 sin^2 beta = (cos alpha + cos beta)^2.
- Loesungen: W-Punkte (u, v) = (1/2, 0), (0, 1/2) usw.; dazu u = v = 0,392 (tan(alpha/2) = 1/sqrt2). Probe mit
  V.V = (1/3)[4 sum z_a^2 - (sum z_a)^2], z_a = e^{ik.d_a}: bei u = v = 0,392 ist 4 sum z^2 = -1,77 und
  (sum z)^2 = -1,78 (Rundung).
- Also: geschlossene Nullstellen-Schleife um X in der Ebene k_x = 2 pi/a durch die vier W-Punkte. Bei X selbst
  keine Nullstelle (LHS 0 < RHS 4).
- Folge: W-D ist nicht "nur ein Dirac-Kegel bei Gamma". Es hat Nullmoden auf Linien am Zonenrand
  (abs(k) ~ 2,2 bis 2,6 pro PU). LICHT-FINN-NETZ-1 rechnete nur k <= 0,6 pro PU und konnte sie nicht sehen.
- [H] Bezug: WEYL-LINEAR-1 nennt ein "raues Band bei E ~ 0" auf Zufallsnetzen. Ob das dieselbe Ursache hat, ist offen.
- **Berichtigung (23:00:34, beim Gegenlesen des Dossiers):** ~~"am Zonenrand (abs(k) ~ 2,2 bis 2,6 pro PU)"~~ ist
  ungenau. Die Schleife liegt in der Ebene k_x = 2 pi/a ausserhalb der Quadratflaeche und beruehrt sie nur in den
  W-Ecken (abs(k) = 2,48). Zurueckgefaltet mit G = (1,1,1) 2 pi/a (V(k+G) = -i V(k), Nullstellen bleiben) liegt
  (1; 0,392; 0,392) bei (0; -0,608; -0,608) 2 pi/a, abs(k) = 1,91 pro PU, im Zoneninneren
  (Summe der Betraege 1,216 <= 1,5). Also Knotenlinien durch W, die auch durchs Innere laufen.
- Zusatz (23:00:34): Die Ursache "Knoten ohne Inversionszentrum" allein reicht nicht; FKM hat dieselben Knoten.
  Es braucht zusaetzlich einen unter Bindungsinversion ungeraden Sprung (sigma.n). Im Dossier so formuliert.

## 2. Abrufe (hoechstens 8; Erwartung mit date vor jedem Abruf)

### A1 (Erwartung 22:43:57 CEST): arXiv-API id_list, Gitterfermionen (11 IDs aus dem Gedaechtnis)

- IDs [L]: 0712.1201 (Creutz), 0712.4401 (Borici), 0801.3361 und 0804.1145 (Bedaque/Buchoff/Tiburzi/Walker-Loud),
  0907.1371 und 0907.3774 (Kimura/Misumi), 0907.2825 (Capitani/Weber/Wittig), cond-mat/0607699 (Fu/Kane/Mele),
  1111.6483 (Young u. a.), 1306.1934 (D'Ariano/Perinotti).
- **Erwartung:** Creutz/Borici: zwei Nullstellen (minimale Verdopplung), chiral. Bedaque 0801: brechen hyperkubische
  Symmetrie und C bzw. T, brauchen Gegenterme. Bedaque 0804: auf dem Hyperdiamant keine minimal verdoppelte Aktion
  mit voller Symmetrie. Kimura/Misumi: Hyperdiamant-Fermionen mit diskreter Symmetrie, Abstimmung noetig.
  Capitani: drei Gegenterme (Dimension 3 und 4). FKM: Dirac-Punkte an den drei X-Punkten (anisotrop).
  Young: nichtsymmorphe Dirac-Punkte bei X. D'Ariano: Weyl-Automat auf dem BCC-Gitter. Ein bis zwei IDs falsch.
- Abruf 22:44:08 CEST, curl, quellen/A1-api-idlist-gitterfermionen.xml (10 IDs, nicht 11; alle 10 richtig;
  Titel der beiden Kimura/Misumi-Arbeiten gegenueber meinem Gedaechtnis vertauscht).
- **Ausgang (22:44:39):**
  - Bestaetigt (je eine Zeile): Creutz 0712.1201 "two species", "exact chiral symmetry" [S Abstract]. Borici 0712.4401
    Parameter fest, nur Masse frei [S Abstract]. Bedaque 0801.3361: "parity and time-reversal, are explicitly
    broken", "radiatively generate relevant and marginal operators", "fine-tuning of several parameters", "unavoidable
    for actions displaying minimal fermion doubling" (mit Annahmen) [S Abstract]. Capitani 0907.2825: Viererimpuls
    mit "linearly divergent piece" [S Abstract]. Young 1111.6483: "Dirac points at the three symmetry related X
    points", geschuetzt durch "crystallographic symmetries" [S Abstract]. D'Ariano 1306.1934: "Lorentz covariance is
    distorted in the ultra-relativistic limit" [S Abstract].
  - **Verstoss V-a (mittel):** Kimura/Misumi 0907.1371: Bedingungen fuer "Lorentz-covariant excitations from poles";
    "the non-nearest-site hoppings are essential for the correct excitations" [S Abstract]. Erwartet hatte ich nur
    "Abstimmung noetig". Das ist dieselbe Richtung wie mein Schreibtisch 1.4 (Gegenterm aus der dritten Schale).
    Korrektur der Erwartung: Auf Hyperdiamant ist "naechste Nachbarn allein" schon als unzureichend fuer
    Lorentz-Kovarianz benannt.
  - **Verstoss V-b (mittel, Zwei-Regime):** Bedaque 0804.1145: Aktionen "with enough symmetries to exclude fine
    tuning; however, they produce multiple doublings. The limit where the actions exhibit minimal doubling does not
    possess the requisite symmetry." [S Abstract]. Erwartet war nur die zweite Haelfte. Die erste passt zu meinem
    Befund 1.5 (W-D hat volle Symmetrie und Knotenlinien). Zwei Regime: symmetrisch + mehrfach verdoppelt gegen
    minimal verdoppelt + abgestimmt. Moderator: Symmetriegruppe der Aktion.
  - Kimura/Misumi 0907.3774: "BBTW fermions in higher even dimensions inevitably yield unphysical degrees of freedom";
    Creutz-Fermionen "lose the high discrete symmetry" [S Abstract]. Bestaetigt.
  - FKM cond-mat/0607699: Abstract nennt die X-Punkte nicht. Lage der Dirac-Punkte nur ueber Young [S Abstract]
    und [L].

### A2 (Erwartung 22:45:02 CEST): arXiv-API id_list, Elektronen-Schranken (5 IDs aus dem Gedaechtnis)

- IDs [L]: astro-ph/0212190 (JLM, Nature 2003), 0707.2673 (Maccione/Liberati/Celotti/Kirk 2007), 0906.0681
  (Liberati/Maccione 2009), 1304.5795 (Liberati 2013), 1308.4973 (Kostelecky/Mewes 2013, Fermionen beliebiger
  Dimension).
- **Erwartung:** JLM: Crab-Synchrotron gibt abs(eta) < ~7e-8 fuer Elektronen, Konvention
  E^2 = p^2 + m^2 + eta p^3/M_Pl, helizitaetsabhaengig. Maccione 2007: volle Crab-Spektrumanpassung, abs(eta_+-)
  um 1e-5 bis 1e-7. Liberati 2013: Zusammenfassung ~1e-7 fuer QED Dimension 5. Kostelecky/Mewes: Klassifikation mit
  spinabhaengigen Koeffizienten der Dimension 5 (Typ H oder b/d), ohne Zahlen im Abstract.
- Abruf 22:45:12 CEST, quellen/A2-api-idlist-elektronen.xml, 5 von 5 IDs richtig.
- **Ausgang (22:45:26):**
  - Maccione u. a. 0707.2673: O(E/M)-Verletzung in QED (EFT), volle Crab-Spektrumrechnung, "constraints of order
    10^{-5} at 95% confidence level on the lepton Lorentz Violation parameters" [S Abstract]. Im erwarteten Band
    (oberes Ende). Eine Zeile.
  - JLM astro-ph/0212190: Schranke auf eine Verletzung "that produces a maximum electron speed less than the speed of
    light", aus "100 MeV synchrotron radiation from the Crab nebula", "factor of 40 million" besser [S Abstract].
    Die Zahl 7e-8 steht nicht im Abstract; sie bleibt [L].
  - **Verstoss V-c (klein, Regime):** Die beiden Crab-Zahlen sind verschiedene Regime: JLM nur die subluminale
    Richtung (maximale Elektronengeschwindigkeit), Maccione eine Gesamtanpassung mit ~1e-5. Ich hatte sie als eine
    Zahl erwartet. Moderator: Annahmen ueber Population/Helizitaet und Vollspektrum gegen Grenzfrequenz.
  - Liberati 2013, Liberati/Maccione 2009, Kostelecky/Mewes 2013: Abstracts ohne Zahlen; Kostelecky/Mewes klassifiziert
    "all Lorentz- and CPT-violating and invariant terms ... of arbitrary mass dimension" [S Abstract]. Die Zuordnung
    meines Terms (R3) bleibt offen.

### A3 (Erwartung 22:45:39 CEST): arXiv-API-Suche, Elektronen-Lorentz-Verletzung, neueste zuerst (Regel 7)

- Suche: abs "Lorentz" UND abs "electron" UND (abs "Crab" ODER abs "LHAASO"), sortiert nach Einreichung, 40 Eintraege.
- **Erwartung:** Seit 2021 Arbeiten mit den PeV-Photonen des Crab (LHAASO): superluminale Elektronen ueber
  Vakuum-Cherenkov, Skala E_LV,e einige 1e24 bis 1e26 GeV fuer das lineare Glied, also abs(eta) ~ 1e-6 bis 1e-7.
  Keine Arbeit der letzten 24 Monate, die die Crab-Schranke aufweicht oder ein Signal meldet.
- Abruf 22:45:49 CEST, quellen/A3-api-elektronen-LV-neueste.xml, 39 Eintraege (2002 bis 2025-10).
- **Ausgang (22:46:44):**
  - Li/Ma 2204.02956 (PLB 829 (2022) 137034, Zitat in 2505.06121): Vakuum-Cherenkov-Freiheit der IC-Elektronen hinter
    den 1,1-PeV-Photonen verbessert lineare Elektronen-Schranken "by 10^4 times" [S Abstract]; Zahl nicht im Abstract.
  - 2210.14817: "the 1.12 PeV high-energy photon from Crab Nebula corresponds to a 2.3 PeV high-energy electron"
    (SSC-Modell der LHAASO) [S Abstract]. Das ist die Zahl fuer meine Umrechnung.
  - Stecker 1306.6095: Crab-Flare 2010, Elektronen "up to ~5.1 PeV", superluminal delta_e <= ~5e-21; subluminal
    abs(delta_e) <= ~8e-17 aus dem Crab-Gammaspektrum [S Abstract]. delta_e = Geschwindigkeitsueberschuss (c = 1).
  - JLM u. a. astro-ph/0309681 (PRL 2004): "LV parameters for positrons and electrons are different", "electron
    helicity decay" [S Abstract]. Bestaetigt die Helizitaets-Konvention der Literatur.
  - **Verstoss V-d (mittel, innerhalb 24 Monate):** 2505.06121 (Mai 2025, Fassung Okt. 2025): Cherenkov-Schranken
    seien in EFT-artigen Ansaetzen berechtigt, aber "naturally evaded in models of space-time foam" (D-Branen); dort
    strahlen Elektronen "despite moving faster than photons" nicht [S Abstract]. Erwartet hatte ich keine Aufweichung.
    Zwei Regime: EFT-Dispersion mit Standard-Dynamik (Schwellenanalyse gilt) gegen stochastisches Medium
    (Prozess unterdrueckt). Moderator: ob die Verletzung als lokale Dispersion mit ueblichen Matrixelementen auftritt.
    Fuer ein festes Netz mit Bloch-Dispersion gilt das erste Regime [ES].
  - Keine Arbeit der letzten 24 Monate meldet ein Elektronen-Signal (in diesen 39 Treffern) [S Abstract, Titel].

### A4 (Erwartung 22:46:58 CEST): arXiv-API-Suche, Hyperdiamant / minimal verdoppelt / Diamant-Gitterfermionen, neueste zuerst (Regel 7 fuer DF1, DF2)

- Suche: abs hyperdiamond ODER abs "minimally doubled" ODER (abs "diamond lattice" UND abs "lattice fermion"), 40.
- **Erwartung:** In den letzten 24 Monaten einige Gitter-QCD-Arbeiten zu Karsten-Wilczek- bzw. Borici-Creutz-
  Fermionen (Gegenterme, Abstimmung, Mesonen), keine mit einem isotropen Diamant-Operator ohne Abstimmung. Hyperdiamant
  selten nach 2012.
- Abruf 22:47:10 CEST, quellen/A4-api-hyperdiamant-minimal-neueste.xml, 40 Eintraege (viele fachfremd: Minimalflaechen,
  Spieltheorie). Kein Hyperdiamant-Treffer nach 2013.
- **Ausgang (22:47:36):**
  - Bestaetigt: Borsanyi/Capitani u. a. 2502.07354: "breaking of the hypercubic symmetry, which requires the inclusion
    and tuning of new counterterms", "tree-level spatial Naik improvement", "non-perturbative tuning" [S Abstract].
    Vig u. a. 2401.07651 ebenso [S Abstract]. Shukre u. a. 2508.09690 (PRD 112, 114501): Symanzik-Wirkung "up to
    dimension-5, including the divergent dimension-3" [S Abstract].
  - **Verstoss V-e (klein, Regime):** Misumi 2512.22609 (PRD 113, 074521 (2026)): Hamilton-Formulierung minimal
    verdoppelter Fermionen in 3+1 D (Dirac und Weyl), Knotenstruktur, Symmetriemuster; eine Deformation, die "all the
    symmetries" erhaelt, erzeugt oberhalb eines kritischen Werts weitere Weyl-Knoten; das Einzel-Weyl-Regime
    verlangt "generically requires 'moderate' parameter tuning" [S Abstract]. Erwartet hatte ich nur Lagrange-
    Gitter-QCD-Arbeiten. Neu ist die Unterscheidung: Abstimmung auf ein offenes Gebiet (Phase) gegen Abstimmung auf
    einen Punkt (Isotropie-Gegenterm). Der sigma.q-Koeffizient von W-D gehoert zur zweiten Art [ES]: Jeder Wert ungleich
    null gibt ein lineares Glied.
  - In den letzten 24 Monaten kein Diamant- oder Hyperdiamant-Operator mit isotropem Kegel ohne Abstimmung (in diesen
    40 Treffern). Fuer DF1 heisst das: nach Recherchestand nicht belegt, nicht widerlegt.

### A5 (Erwartung 22:47:50 CEST): Volltext Bedaque/Buchoff/Tiburzi/Walker-Loud 0804.1145 (PDF)

- **Erwartung:** Kurzarbeit (PRD Brief Report). Ausgang Graphen -> Diamant -> Hyperdiamant; Spruenge laengs der fuenf
  Bindungsvektoren mit Gamma-Matrizen (4D-Gegenstueck von W-D). Die symmetrische Aktion hat mehr als zwei Nullstellen
  (vielleicht Linien oder Flaechen), der minimal verdoppelte Grenzfall (Creutz) bricht die Permutationssymmetrie S5.
  Zum 3D-Diamant hoechstens ein Satz (Nullstellen auf Linien beim skalaren Sprung).
- Abruf 22:47:59 CEST, quellen/A5-Bedaque-hyperdiamond-0804.1145v1.pdf (4 S.), .txt (-layout) und .raw.txt
  (Lesereihenfolge; Zeilen unten beziehen sich auf .raw.txt).
- **Ausgang (22:49:27):**
  - Bestaetigt: Gl. (7) ist das 4D-Gegenstueck von W-D: Zweikomponenten-Spinoren auf L- und R-Knoten, naechste
    Nachbarn "with equal probability in all five directions", Sprungmatrix sigma.e_alpha bzw. sigmabar.e_alpha
    [S Z. 156-185]. Symmetrie nur A5, nicht S5 [S Z. 186-190, 321-325].
  - Bestaetigt: "it has, in addition to the pole at p_mu = 0 ... several others poles at finite p_mu, e.g.
    p1 = -p2 = -p3 = p4 = cos^-1(-2/3)" [S Z. 334-337]. Das 4D-Gegenstueck hat also Doppler bei endlichem Impuls,
    wie mein Befund 1.5 fuer W-D (dort als Linien) [M].
  - Bestaetigt: Borici-Creutz: e_alpha nur fuer B = 1/sqrt5, C = 1 symmetrisch; die Zusatzterme sind
    "non-nearest neighbor interactions" und "break the Z5 symmetry" [S Z. 380-404]. Z5 erzwingen gibt "additional
    poles, and a Lorentz non-symmetric continuum limit" [S Z. 488-492]; "mutilated fermions" auch bei Celmaster 1982
    und Drouffe/Moriarty 1983 [S Z. 449-452, 517-519]. Schluss: "Z5 symmetry on a hyperdiamond appears
    incommensurate with minimal doubling" [S Z. 493-496].
  - **Verstoss V-f (gross, Regime):** Die Arbeit fragt nur nach Operatoren der Dimension 3 und 4 ("only two chirally
    symmetric relevant operators ... Both ... identically vanish because the five basis vectors sum to zero"
    [S Z. 326-334]; Einleitung Z. 35-40). Operatoren der Dimension 5 kommen nicht vor. Ich hatte erwartet, dass die
    Gitterliteratur die Spaltung zweiter Ordnung mitbehandelt. Sie tut es nicht, weil dort a -> 0 geht und
    Dimension 5 verschwindet. Fuer ein Netz mit fester Masche l ist genau Dimension 5 beobachtbar.
    Zwei Regime: Gitter als Regulator (a -> 0, Kriterium "keine Operatoren der Dimension 3 und 4") gegen
    physikalisches Netz (l fest, Kriterium "keine Operatoren der Dimension 5 mit Spinstruktur"). Moderator: ob die
    Masche gegen null geht. Folge: DF2 ist in der Literatur fuer Dimension 3/4 belegt; fuer die Spaltung (Dimension 5)
    sagt sie nichts.
  - [ES/M] Das Simplex der fuenf e_alpha hat wie der Tetraederstern ein drittes Moment ungleich null (kein
    Inversionszentrum). Ein sigma.q-artiger Term der Dimension 5 ist daher auch in Gl. (7) zu erwarten; nicht
    gerechnet.

### A6 (Erwartung 22:49:45 CEST): Volltext Kimura/Misumi 0907.1371 (PDF), gezielt "Lorentz", "non-nearest"

- **Erwartung:** Die Bedingung fuer "Lorentz-covariant excitations" betrifft nur die fuehrende Ordnung (Rang-2-Tensor
  der Sprungvektoren proportional zu delta, also isotroper Kegel bzw. richtige Gamma-Struktur). Nicht-naechste
  Spruenge braucht man, weil der verformte Hyperdiamant (Creutz) sonst einen schiefen Kegel hat. Keine Aussage zu
  Dimension 5.
- Abruf 22:49:54 CEST, quellen/A6-KimuraMisumi-0907.1371v3.pdf (22 S.), .raw.txt (Zeilen unten).
- **Ausgang (22:51:36):**
  - **Verstoss V-g (gross):** Die Bedingung betrifft nicht den Rang-2-Tensor, sondern die Zerlegung in "Vektor-" und
    "Axialvektor-Funktionen". Mit nur naechsten Spruengen erscheinen in den Koeffizienten nur e^{ip} oder e^{-ip};
    man braucht "both of L -> R and R -> L", und der Operator hat die Form D(p) = sum i gamma_mu F_mu(p) +
    sum gamma_mu gamma5 G_mu(p) mit unabhaengigen reellen F, G [S Z. 463-489]. "the operator including both of
    i gamma-terms and gamma gamma5-terms yields unphysical fermion doublers in general" [S Z. ~495-497]; das
    Nielsen-Ninomiya-Abzaehlen greift dann nicht ("based on Poincare-Hopf theorem for either ... not for both")
    [S Z. 484-489]. Abhilfe "non-nearest-site (but nearest-unit-cell) hoppings", die aber "lower the discrete
    symmetry"; daraus eine "no-go property": genug Symmetrie und physikalische minimale Verdopplung schliessen sich in
    dieser Feldanordnung aus [S Z. 503-522, 1102-1110].
  - **Uebersetzung auf W-D [M]:** M = (i/2) sigma.V, V = X + iY. Hermitescher Teil -(1/2) sigma.Y (Y ~ k, "Vektor"),
    antihermitescher Teil (i/2) sigma.X (X = sum n_a cos(k.d_a) ~ q, "Axialvektor"). Der sigma.q-Term IST die
    G-Funktion von Kimura/Misumi. Dieselbe Groesse X erzeugt (a) die lineare Spaltung bei kleinem k
    (Spaltung ~ abs(X x Y)) und (b) die Knotenlinien: Ohne X waeren Nullstellen Y = 0 (drei Bedingungen, Punkte,
    Nielsen-Ninomiya zaehlt); mit X sind es zwei Bedingungen (Linien). Gemeinsame Kopplungsgroesse (Feldregel 6).
  - **Folgerung [M]:** Ein spinentarteter Operator (nur Vektor-Teil, H = tau_x sigma.F) hat in keiner Ordnung eine
    Spinspaltung (H^2 = F^2). Auf dem Diamant verlangt das im Zellen-Eichbild T_{d1+R} = T_{d1-R}^dag, also Spruenge
    laengs d_b und 2 d_1 - d_b: eine Bindung d_1 ist ausgezeichnet, die Tetraedersymmetrie ist gebrochen
    (Creutz-Mechanismus). Begruendung: Kein A -> B-Vektor hat ein A -> B-Negativ (Summe der Koordinaten 3 mod 4 gegen
    1 mod 4), weil die Knoten keine Inversionszentren sind.
  - Erwartung korrigiert: Die Hyperdiamant-Literatur benennt genau die W-D-Struktur (Vektor plus Axialvektor aus
    einseitigen Spruengen) als Ursache unphysikalischer Doppler, nicht als Dimension-5-Spaltung.
- **Konvention JLM (lokal, ohne Abruf):** E^2 = p^2 + m_a^2 + eta_a p^n / M^(n-2), M ~ M_P = 1,22e19 GeV
  [S-lokal jlm-hep-ph-0209264.txt Z. 103, 167]. Cherenkov-Linie eta = m^2/(2 p_max^3) ~ 1,5e-3 fuer 100-TeV-
  Elektronen [S-lokal Z. 655]; nachgerechnet [M]: 2,61e-7 GeV^2 x 1,22e19 GeV / (2 x 1e15 GeV^3) = 1,6e-3.

### A7 (Erwartung 22:53:03 CEST): Volltext Fu/Kane/Mele cond-mat/0607699 (PDF), nur das Diamant-Modell

- **Erwartung:** Gl. (1) H = t sum c^dag c + i (8 lambda_SO / a^2) sum c^dag s.(d1 x d2) c (naechste Nachbarn
  skalar, uebernaechste mit Spin-Bahn). Nur mit t: Entartung laengs Linien (X-W). Mit lambda_SO: 3D-Dirac-Punkte an
  den drei X-Punkten; eine Bindungsverzerrung delta t oeffnet die Luecke (STI/WTI). Kegel an X anisotrop (nicht
  explizit gesagt).
- Abruf 22:53:26 CEST, quellen/A7-FuKaneMele-cond-mat-0607699v2.pdf (4 S.), .raw.txt.
- **Ausgang (22:53:58):**
  - Bestaetigt: Gl. (4) wie erwartet; "Due to inversion symmetry, each band is doubly degenerate"; "3D Dirac points at
    the three inequivalent X points"; Luecke durch Bindungsmodulation delta t_p [S Z. 450-472].
  - **Verstoss V-h (gross):** Ich hatte FKM nur als anisotropes Gegenbeispiel erwartet. Gl. (5): H_eff^z =
    t a sigma^y q_z + 4 lambda_SO a sigma^z (s_x q_x - s_y q_y) + m_z sigma^x [S Z. 474-477]. Daraus [M]:
    H^2 = t^2 a^2 q_z^2 + 16 lambda^2 a^2 (q_x^2 + q_y^2) + m^2 (die Kreuzterme heben sich, s_x s_y + s_y s_x = 0);
    der Kegel ist isotrop genau fuer t = 4 lambda_SO (eine Abstimmung). Und: wegen Inversion plus Zeitumkehr ist jedes
    Band an jedem k zweifach entartet [S Z. 466-467], also gibt es keine Spinspaltung in irgendeiner Ordnung.
    Korrektur: Der Weg ohne Spaltung auf dem Diamant ist nicht die 4_1-Schraube, sondern P T (Kramers an jedem k).
    Preis: drei Dirac-Kegel an X (sechs Weyl-Knoten), Isotropie nur abgestimmt.
  - [M] Warum W-D das nicht hat: Dort antikommutiert die Inversion mit H (sigma.n ist ungerade), also antikommutiert
    auch P T; es paart E mit -E statt E mit E. Moderator der beiden Regime: Paritaet des Naechste-Nachbarn-Sprungs
    unter Bindungsmitten-Inversion. Gerade (FKM): Dirac an X, entartet, mehrere Kegel. Ungerade (W-D): Dirac bei Gamma,
    gespalten, Knotenlinien.
- Berichtigung A6 (22:53:58, nach grep): Die Zeilen sind D(p) und "independent real functions" Z. 485-493,
  Poincare-Hopf Z. 496, "unphysical fermion doublers in general" Z. 500-501, nicht-naechste Spruenge Z. 503-506,
  "lower the discrete symmetry" und no-go Z. 513-522. Die Angaben "Z. ~495-497" und "Z. 463-489" oben sind
  ~~ungenau~~ durch diese ersetzt.

- Berichtigung A7 (22:58:37, nach grep): "Due to inversion symmetry, each band is doubly degenerate" steht in
  Z. 468, die drei X-Punkte in Z. 468-469. Die Angabe ~~[S Z. 466-467]~~ oben ist durch Z. 468-469 ersetzt. Ebenso
  steht das Bedaque-Abstract in der .raw.txt in Z. 8-15 (nicht 11-13); im Dossier berichtigt.

## 5. Gegensweep (22:58, vor dem Dossier-Schluss)

- G1 "spaltet die Helizitaeten": geprueft [M], Querspin (1.2).
- G2 "W-D hat nur den Kegel bei Gamma": geprueft [M] (1.5), Gattung durch A5/A6 gestuetzt.
- G3 "Gitterliteratur meint Dimension 5": geprueft [S] A5, nein (V-f).
- G4 "FKM ist anisotrop": geprueft [S + M] A7, isotrop bei t = 4 lambda_SO, spinentartet (V-h).
- G5 "Helizitaets-Schranken gelten fuer W-D": teilweise [ES].
- G6 "Finns Knoten = Diamant-Knoten": nicht geprueft; Skizze: sigma.n auf Pyrochlor-Knoten (Inversionszentren) ist
  unter Inversion ungerade, gerade k-Terme verschwinden, H(0) = 0 fuer 8 Baender [M, Skizze].
- G7 "gleiche Grenzgeschwindigkeit Elektron und Licht": nicht geprueft; [P] 0,8165 gegen 2,8284 (Code-Einheiten).
- G8 "4D-Euklid uebertraegt sich auf 3D-Hamilton": teilweise (Misumi 2512.22609 [S Abstract]).

## 4. Umrechnung DF3 [M, von Hand]

- W-D als Elektron, superluminaler Zweig: E = hbar c k (1 + a1 k l) (Phasenkoeffizient) -> E^2 = p^2 + 2 a1 l p^3
  (c = hbar = 1). Mit JLM: eta = 2 a1 l M, also l = eta l_P / (2 a1) mit l_P = hbar c / M = 1,616e-35 m.
- a1 = 0,3536 (110; l = Tetraederkante): 2 a1 = 0,7071.
- Cherenkov-Schwelle p_th^3 = m^2 M / (2 eta) [JLM-Konvention]; keine Abstrahlung bis p heisst eta < m^2 M/(2 p^3),
  also l < hbar c m^2 / (4 a1 p^3).
  - p = 2,3 PeV (LHAASO-SSC, 2210.14817): eta < 3,18e12 / (2 x 1,217e19) = 1,31e-7; l < 1,31e-7 x 1,616e-35 /
    0,7071 = 3,0e-42 m = 1,9e-7 l_P.
  - p = 5,1 PeV (Crab-Flare, Stecker): eta < 1,20e-8; l < 2,7e-43 m = 1,7e-8 l_P. Probe ueber Steckers
    delta_e <= 5e-21: delta = 2 a1 k l -> l <= 5e-21 x 1,973e-16 GeV m / (0,7071 x 5,1e6 GeV) = 2,7e-43 m. Gleich.
- Subluminaler Zweig (gleich gross, entgegengesetzt): Maccione u. a. abs(eta) ~ 1e-5 (95 %): l < 2,3e-40 m =
  1,4e-5 l_P. JLM Nature 7e-8 [L]: l < 1e-7 l_P.
- In jeder Lesart l << l_P. Bedingung: Bindungsrichtung beliebig ausser 100/111; bei kreisenden Elektronen
  durchlaeuft k alle Richtungen einer Ebene [ES].

## 3. Offene Rueckfragen (wandern mit)

- R1: Nullstellen-Schleifen von W-D numerisch bestaetigen (Leitung, Code; nicht mein Mandat). -> Kartenvorschlag
  DIAMANT-NULLSTELLEN-1 im Dossier 7.1.
- R2: Hat der verbesserte Operator (w3 = w1/9) weniger oder mehr Nullstellen? Offen (Dossier 7.6 Nr. 2).
- R3: SME-Zuordnung des Terms psibar sigma^{0i} psi d_j d_l abs(eps_ijl). Offen (Dossier 7.6 Nr. 4).
- R4 (neu): FKM auf Finns Netz; t = 4 lambda_SO aus Symmetrie? Offen (Dossier 7.6 Nr. 6).
- R5 (neu): sigma.n auf den Pyrochlor-Knoten (G6). Offen.
- Zusatz 23:01:12: Gewicht der dritten Schale in normierten Richtungen (wie W-D) ist sqrt(11/3)/9 = 0,213; die
  1/9 gilt fuer unnormierte Sprungvektoren in Einheiten a/4 [M].

## 6. Abschluss

- Dossier geschrieben ab 22:55:43 CEST, gegengelesen und berichtigt bis 23:01:12 CEST (date). 7 von 8 Abrufen
  verbraucht. Kein Journal, kein Peerbus, kein Commit.
