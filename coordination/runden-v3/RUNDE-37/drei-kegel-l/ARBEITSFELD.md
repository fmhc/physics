# DREI-KEGEL-L: Arbeitsfeld (feldforscher)

- Start 2026-10-05 00:43:55 CEST (date). Karte gelesen 00:44, Vorlagen gelesen bis 00:52.
- Gelesen (nur lesen): diamant-fermion-l/DOSSIER.md, diamant-nullstellen-1/ERGEBNIS.md, tetraeder-l/DOSSIER.md
  (Z. 55-90, 215-240), spin-zufallsnetz-1/ERGEBNIS.md (Z. 1-60), lokale FKM-Kopie
  diamant-fermion-l/quellen/A7-FuKaneMele-cond-mat-0607699v2.raw.txt Z. 440-500 (kein Abruf).
- Kennzeichen: [S Z.] Quelle, Zeile; [S Abstract]; [S-lokal]; [P] Projektdatei; [L] Gedaechtnis; [M] von Hand;
  [ES] eigener Schluss; [H] Hypothese.
- Gestrichenes bleibt stehen (~~...~~), offene Rueckfragen stehen in Abschnitt 4.

## 0. Ausgangslage aus den Vorlagen

- FKM Gl. (4)/(5) [S-lokal Z. 455-476]: H = t sum c_i^+ c_j + i (8 lambda/a^2) sum c_i^+ s.(d1 x d2) c_j;
  Dirac-Punkte an X^r = 2 pi r^/a; H_eff^z = t a sigma^y q_z + 4 lambda a sigma^z (s_x q_x - s_y q_y) + m_z sigma^x;
  m_z = sum_p delta t_p sgn[d_p . z^]; "sigma^i ... sublattice, s^i ... spin"; H^x, H^y "with x, y and z permuted in
  q_i and s_i, but not sigma^i"; "delta t_p = 0 is thus a multicritical point separating 8 ... phases".
- DIAMANT-NULLSTELLEN-1 [P, E]: Nullstellen nur an den drei X, Tempo 2,8284 isotrop, a2 laengs -1/12, quer -1/3
  (Spannweite 89 %), Spinspaltung 1e-14.

## 1. Schreibtisch [M] (vor allen Abrufen, 00:52 bis 00:54)

Konventionen: Ursprung auf einem A-Atom. A = fcc-Gitter R, B = R + tau, tau = (a/4)(1,1,1). Lage-Eichung
|alpha,k> = sum_R e^{ik.(R+r_alpha)} |R+r_alpha>. Drehung g um den Ursprung: g|alpha,k> = |alpha, g k>.
Rueckfaltung: |alpha, k - G> = e^{-iG.r_alpha} |alpha,k>. G = (2 pi/a)(0,0,2) ist reziproker Gittervektor (alle
Indizes gerade). e^{-iG.tau} = e^{-i pi} = -1, e^{-iG.0} = 1.

1.1 **Stern von X:** drei Arme X_x, X_y, X_z (X und -X gleich modulo G). Stabilisator von X_z in T (= A4) ist
    V4 = {E, C2x, C2y, C2z}; C3[111]: (x,y,z) -> (z,x,y) bildet X_x -> X_y -> X_z exakt ab (ohne G, ohne Phase).
1.2 **Vorzeichen von V4 an X_z:**
    - C2x: X_z -> -X_z = X_z - G. A: +1. B: e^{-iG.tau} = -1. Ebenso C2y. C2z haelt X_z fest: A +1, B +1.
    - Also traegt A an X_z den trivialen Charakter von V4, B den Charakter chi_z = (C2x, C2y, C2z) -> (-1, -1, +1).
    - Gleich fuer X_x, X_y mit zyklisch vertauschten Vorzeichen.
1.3 **A4 ohne Spin (Charaktertafel, Klassen E, 3C2, 4C3, 4C3^2):**
    | | E | 3C2 | 4C3 | 4C3^2 |
    |---|---|---|---|---|
    | 1 | 1 | 1 | 1 | 1 |
    | 1' | 1 | 1 | w | w^2 |
    | 1'' | 1 | 1 | w^2 | w |
    | 3 | 3 | -1 | 0 | 0 |
    | chi_A (A an den drei X) | 3 | 3 | 0 | 0 |
    | chi_B (B an den drei X) | 3 | -1 | 0 | 0 |
    - chi_A: n(1) = n(1') = n(1'') = (3 + 9)/12 = 1, n(3) = (9 - 9)/12 = 0. Also **A: 1 + 1' + 1''**.
    - chi_B = chi_3. Also **B: 3** (in der Ma-Rajasekaran-Basis: V4 diagonal, C3 zyklisch).
    - Mit Ursprung auf B tauschen die Rollen (A: 3, B: 1+1'+1''). Allgemein entscheidet (r_alpha - c)_z mod a/2 ueber
      das Vorzeichen: 0 -> 1+1'+1'', a/4 -> 3. Leere T_d-Lagen (8b) verhalten sich wie A bzw. B.
    - Unter T_d: A -> A1 + E, B -> T2 (sigma_d [x<->y] haelt tau und B_z fest: +1; S4z gibt -1).
1.4 **Mit Spin (2T = SL(2,3), 24 Elemente; Klassen 1, -1, 6 x (+-i,+-j,+-k), p, p^2, -p, -p^2 mit
    p = (1+i+j+k)/2, je 4):**
    | | 1 | -1 | 6 i | 4 p | 4 p^2 | 4 (-p) | 4 (-p^2) |
    |---|---|---|---|---|---|---|---|
    | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
    | 1' | 1 | 1 | 1 | w | w^2 | w | w^2 |
    | 1'' | 1 | 1 | 1 | w^2 | w | w^2 | w |
    | 3 | 3 | 3 | -1 | 0 | 0 | 0 | 0 |
    | 2 | 2 | -2 | 0 | 1 | -1 | -1 | 1 |
    | 2' | 2 | -2 | 0 | w | -w^2 | -w | w^2 |
    | 2'' | 2 | -2 | 0 | w^2 | -w | -w^2 | w |
    - Proben: Summe der Dimensionsquadrate 24; <2,2> = (4+4+16)/24 = 1; <2,2'> = (8 + 8(w+w^2))/24 = 0.
    - chi_orb = chi_A + chi_B = (6, 6, 2, 0, 0, 0, 0); chi_12 = chi_orb x chi_2 = (12, -12, 0, 0, 0, 0, 0).
    - n(2) = n(2') = n(2'') = (24 + 24)/24 = 2. Also **12 = 2 (2 + 2' + 2'')**. Kein 3 und kein 1, 1', 1''
      moeglich: In spinorielle Zustaende (-1 wirkt als -1) passen nur 2, 2', 2''.
    - 2 x 3 = (6, -6, 0, 0, 0, 0, 0) = 2 + 2' + 2'' = 2 x (1 + 1' + 1''). **Mit Spin verschwindet der Unterschied**
      zwischen "Triplett" und "1 + 1' + 1''" in der Doppelgruppe.
    - Je Chiralitaet (2 Zustaende je X): Ind von Q8 (2-dim Spinor) nach 2T = 2 + 2' + 2'' (Frobenius).
1.5 **Zweites A4 ("Translations-A4"):** fcc-Translationen modulo einfach-kubisch (Z2 x Z2: 0, (a/2)(0,1,1),
    (a/2)(1,0,1), (a/2)(1,1,0)) wirken auf die X-Zustaende mit e^{-iX_r.t}: t = (a/2)(0,1,1) gibt (X_x, X_y, X_z) ->
    (+1, -1, -1), fuer A und B gleich. Mit C3 zusammen: (Z2 x Z2) x| Z3 = A4, die drei X sind das **Triplett 3** fuer
    jede Untergitter- und Spinkomponente. Mit Spin (Ordnung-3-Lift von C3, Spin -> 1' + 1''): 12 = 4 x 3.
    - [ES] Das ist strukturgleich mit der Taste-Gruppe gestaffelter Fermionen (Translationen als Taste-Operatoren)
      und vermutlich mit dem Orbifold-A4 bei Altarelli/Feruglio/Lin (Halbperioden-Translationen x| Z3) [L, zu pruefen].
1.6 **Volle Raumgruppe:** Ist der 4-dim Raum an X ein irreduzibler kleiner Doppelgruppen-Darstellungsraum, dann sind
    die 12 Zustaende eine einzige irreduzible Darstellung (Stern mit 3 Armen, induziert) [L: Bradley/Cracknell;
    Vierfach-Entartung an X in Fd-3m: Young u. a. 2012, zu pruefen].
1.7 **Massen:** m_r = sum_p delta t_p sgn(d_p . r^). Die vier Vorzeichenspalten sind die drei nichttrivialen
    Charaktere von Z2 x Z2 (Hadamard): m_x = d1 + d2 - d3 - d4, m_y = d1 - d2 + d3 - d4, m_z = d1 - d2 - d3 + d4.
    - Vier Bindungen unter T_d: A1 + T2; der A1-Teil (sum delta t_p) faellt heraus. **(m_x, m_y, m_z) ist T2, also 3
      unter A4.**
    - delta t_p = d_p . v (relative Untergitter-Verschiebung u ~ v, optisches Phonon): m_r = a v_r [M].
    - Beispiele: nur Bindung 1 moduliert: m = delta (1,1,1), drei gleiche Betraege. delta t = (d, d, 0, 0):
      m = (2d, 0, 0), ein Kegel massiv, zwei masselos.
1.8 **Abgleich mit dem Ma-Rajasekaran-Massenterm [M, Quelle noch nicht gelesen]:**
    - Gitter: sum_r m_r A_r^+ B_r mit A in 1+1'+1'', B in 3, m in 3. Das ist die Invariante
      l^c(1,1',1'') x L(3) x Phi(3) mit **gleichen** Kopplungen h1 = h2 = h3 (DFT-Zerlegung von A_r).
    - Translationsinvarianz erhaelt die Kristallimpulse modulo G, also V4_t: jede translationsinvariante quadratische
      Stoerung ist im Kegelindex r diagonal. Mischung zwischen Kegeln braucht Translationsbruch bei Wellenvektor X.
    - [ES] Folge: Zwei translationsinvariante Sektoren haben dieselbe Kegelbasis, die Mischungsmatrix waere eine
      Permutation. PMNS/CKM verlangten Periodenverdopplung (Superzelle sc statt fcc).
1.9 **Wo spinorielle und orbitale Lesart auseinanderlaufen:** Die Chiralitaet an X_z ist proportional zu
    sigma^y s_z (aus alpha_x alpha_y alpha_z), mischt also A und B. "Untergitter" ist nicht "Haendigkeit". Die
    Zuordnung B -> 3, A -> 1+1'+1'' entspricht daher nicht L -> 3, l^c -> 1+1'+1'' im Sinne der Chiralitaet.
    Emergenter Spin an X_z: (sigma^x s_y, sigma^x s_x, -s_z) bis auf Normierung, nicht der Gitterspin s.

## 2. Abrufe (Erwartung vor Abruf, Ausgang danach)

(folgt)

## 3. Erwartungsverstoesse (laufend)

| Nr | Erwartet | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| K-1 gross | Karte: "Unter A4 spaltet die reine Vertauschung ... in 1 + 1' + 1'', weil die Klein-Vierergruppe die Achsen festhaelt" | V4 haelt die Punkte X fest, wirkt aber auf B-Zustaende mit Vorzeichen (Rueckfaltung, e^{-iG.tau} = -1): B ist 3, A ist 1+1'+1''; welches Untergitter, haengt vom Drehzentrum ab | 1.2, 1.3 [M] | "Punkt fest" heisst nicht "Zustand fest" |
| K-2 gross | DK2: "sofern der Spin nichts aendert" | Der Spin aendert alles: in 2T gibt es kein spinorielles 3; 12 = 2(2+2'+2''); 2 x 3 = 2 x (1+1'+1'') | 1.4 [M] | Frage "1+1'+1'' oder 3" ist mit Spin nur nach Abspalten eines Spins definiert, und das ist nicht eindeutig (1.9) |
| K-3 mittel | Karte nennt ein A4 | Es gibt mindestens zwei: Punktgruppen-A4 (Lage-Symmetrie) und Translations-A4 (fcc/sc x| C3); unter dem zweiten sind die drei Kegel ein Triplett | 1.5 [M] | Welches A4 "Flavour" ist, ist eine Wahl |

## 4. Offene Rueckfragen (wandern mit)

- R1: Ist der 4-dim Raum an X in Fd-3m (Doppelgruppe, mit T) irreduzibel? (Young u. a. 2012)
- R2: Wie entsteht das Orbifold-A4 bei Altarelli/Feruglio/Lin? Halbperioden-Translationen?
- R3: Ma-Rajasekaran: Zuordnung und Massenmatrix im Wortlaut.
- R4: Literatur Doppler/Tastes/Valleys als Generationen (DK1).

### F1 (arXiv-API: Doppler/Taste/Kaehler-Dirac UND Generationen/Familien)

- Erwartung, notiert 2026-10-05 00:55:28 CEST (date), vor dem Abruf: Es gibt einige Vorschlaege (Kaehler-Dirac/gestaffelte Tastes als Generationen, z. B. Catterall u. a. 2018 bis 2026; aeltere Montvay-/Spiegel-Arbeiten), dazu viele Arbeiten, in denen Taste ausdruecklich NICHT Flavour ist (Taste-Brechung, Rooting). Kein anerkanntes Modell. Ein Treffer, der drei Generationen aus einer Gittersymmetrie ableitet, waere ein Verstoss.
- Abruf 00:55:33 (curl, 80 Eintraege, Kopie quellen/F1-api-doppler-generationen-20261005-005533.xml). Suche verrauscht
  ("taste" trifft Lebensmittel und Musik).
- **Ausgang: bestaetigt (eine Zeile je Fund).**
  - Schmelzer, I. (2002), hep-th/0209167: "Fermion doubling is used here as a tool to obtain the necessary number of
    steps of freedom. The correspondence extends to important structural properties (families, colors, flavor pairs,
    electromagnetic charge)"; "The extension to gauge fields is the major open problem" [S Abstract]. Vorschlag, Aussenseiter.
  - Jourjine, A. N. (2010), 1005.3593: "Classical massive DK spinors are shown to be equivalent to four generations of
    Dirac spinors with equal mass ... Quantization breaks U(2,2) to U(2)xU(2), lifts mass spectrum degeneracy" [S Abstract].
    Vier, nicht drei; Gleichmassigkeit klassisch, Aufspaltung erst durch Quantisierung.
  - Roadmap Part II (2023), 2312.12799: Pruefpunkte "evade familiar fermion doubling problems" und "explain the existence
    of three generations"; das Modell "has yet to cross" den Generationen-Punkt [S Abstract].
  - Gestaffelte Literatur behandelt Taste als Artefakt: "fourth-root trick that produces one taste per flavor" und
    O(a^2)-Taste-Brechung (Lee-Sharpe-Lagrangian) [S Abstract, Eintrag Z. 1168 der Kopie]; Rooting-Streit (Kommentar zu
    Creutz, Z. 1334) [S Abstract].
  - Kein Treffer leitet drei Generationen aus einer Gittersymmetrie ab. Catterall (Kaehler-Dirac) taucht nicht auf;
    vermutlich Umlaut-Schreibweise. Offen fuer F2.

### F2 (arXiv-API: Catterall/Volovik/Zubkov UND Generationen; "three generations" UND Gitter-Doppler/Valleys)

- Erwartung, notiert 2026-10-05 00:56:39 CEST (date): Catterall u. a. (2016 bis 2026) behaupten, reduzierte Kaehler-Dirac-Felder liefern Generationen (eher 4 bzw. 2 als 3) und brauchen Symmetric Mass Generation; Volovik/Zubkov leiten Familien aus mehrfachen Fermi-Punkten ab. Kein Ansatz liefert 3 aus der Gittersymmetrie mit Hierarchie. Verstoss waere: ein Gittermodell mit drei Kegeln an X (oder M/L) ausdruecklich als drei Generationen.
- Abruf 00:56:45 (curl, 60 Eintraege, quellen/F2-api-catterall-volovik-generationen-*.xml). au:Zubkov trifft auch
  Mathematiker; der zweite Zweig ("three generations" UND Gitter UND Doppler/Valleys) liefert nichts Eigenes.
- **Ausgang: teilweise verletzt (mittel).**
  - Catterall, S. (2021), 2010.02290, PRD 104, 014503: reduzierte gestaffelte Felder, Fidkowski-Kitaev-Yukawa, "gap a
    subset of the lattice fermions without breaking symmetries"; Anomalien "place strong constraints on the number of
    lattice fermions" [S Abstract].
  - Catterall, S. (2023), 2209.03828, PRD 107, 014501: "theories of two staggered fields yield eight Dirac or sixteen
    Majorana fermions in the continuum limit", passend zur Fermionenzahl, die Randfermionen 4+1-dim. topologischer
    Supraleiter gappt [S Abstract].
  - Catterall, S.; Pradhan, A. (2025), 2501.10862: Shifts (Translationen) gestaffelter Hamilton-Fermionen "are related to
    continuum axial transformations"; aus den Shifts "conserved, quantized charges that generate continuous symmetries";
    't-Hooft-Anomalien [S Abstract].
  - Volovik/Zubkov (2014), 1402.5700, NPB 881, 514: emergente Weyl-Spinoren am Fermi-Punkt, emergente Eich- und
    Gravitationsfelder; nichts zu drei Generationen [S Abstract]. Volovik (2003), hep-ph/0310006: Familiengruppe SU(4)_F
    mit vierter Generation als Dunkle Materie, gesetzt, nicht abgeleitet [S Abstract].
  - **Verstoss gegen meine Erwartung:** Ich erwartete "Tastes = Generationen" bei Catterall. In den Abstracts dienen die
    Taste-Freiheitsgrade dazu, die 16 Weyl-Komponenten EINER Generation (bzw. die anomaliefreie Zahl) zu stellen, nicht
    drei Generationen. Dasselbe Muster: Schmelzer (Doppler fuer "families, colors, flavor pairs") und TETRAEDER-L
    (Zopfmodell: drei Baender = eine Generation) [P].
  - **Korrigierte Erwartung:** In der Literatur werden Gitter-Vielfachheiten haeufiger als innere Komponenten einer
    Generation gelesen als als Generationenzahl. Translationen als Taste-/Axialsymmetrie stuetzt 1.5 [S Abstract
    2501.10862].

### F3 (Young u. a. 2012, arXiv:1111.6483, PDF)

- Erwartung, notiert 2026-10-05 00:57:18 CEST (date): Der Text sagt, dass in Raumgruppe 227 (Fd-3m) mit Spin-Bahn-Kopplung am X-Punkt nur vierdimensionale doppelwertige Darstellungen existieren (jedes Band an X vierfach entartet) und dass dies den Dirac-Punkt durch Kristallsymmetrie schuetzt. Verstoss waere: zwei 2-dim Darstellungen, die erst Zeitumkehr zu vier verklebt, oder mehrere 4-dim Darstellungen.
- Abruf 00:57:22 (curl, PDF 6 S., quellen/F3-Young-1111.6483-20261005-005722.pdf, Text F3-Young-1111.6483.raw.txt).
- **Ausgang: bestaetigt, mit einer Zusatzangabe.** Fd-3m "exhibits FDIRs R_Gamma at Gamma and R_X at X"; "R_X is a
  projective representation of G_X ... point group operations in G_X are those of the group D4h"; "The Dirac point at X
  in the FKM model is also spanned by states belonging to R_X" [S Z. 96-107]. Bildtext: "four dimensional projective
  representation of the little group at X which contains a four-fold rotation accompanied by a sub-lattice exchange
  operation" [S Z. 351-354]. "Gapped phase obtained by breaking the fourfold rotation symmetry" [S Z. 360-361].
  - Das Wort "only" (nur 4-dim Darstellungen an X) steht nicht da; es genuegt aber, dass der Dirac-Raum an X eine
    irreduzible 4-dim Darstellung ist. Damit sind die 12 Zustaende unter der vollen Raumgruppe eine irreduzible
    12-dim Darstellung (Induktion ueber den Stern, [L] Bradley/Cracknell). R1 erledigt.
  - Zusatz fuer K-3: Die kleine Gruppe an X enthaelt die Schraube mit Untergittertausch. Unter ihr mischen A und B an X;
    die Punktgruppen-Zerlegung A -> 1+1'+1'', B -> 3 ist also keine Zerlegung unter der vollen Gruppe.

### F4 (Ma/Rajasekaran 2001, arXiv:hep-ph/0106291, PDF)

- Erwartung, notiert 2026-10-05 00:57:50 CEST (date): Lepton-Dubletts L_i als 3, rechtshaendige geladene Leptonen l^c_i als 1, 1prime, 1primeprime, drei Higgs-Dubletts Phi_i als 3; geladene Leptonen ueber drei freie Kopplungen h1, h2, h3; mit <Phi> = (v,v,v) wird die Massenmatrix U_omega x diag(h1,h2,h3) x sqrt3 v; die Hierarchie steckt in den h_i, nicht in A4. Verstoss waere: andere Zuordnung oder Massen aus der Ausrichtung der VEVs.
- Abruf 00:57:56 (curl, PDF 11 S., quellen/F4-MaRajasekaran-hep-ph-0106291-20261005-005756.pdf, Text *.raw.txt).
- **Ausgang: bestaetigt.** "(nu_i, l_i)_L ~ (3, 1)", "l1R ~ (1, 1)", "l2R ~ (1', 1)", "l3R ~ (1'', 1)", "N_iR ~ (3, 0)",
  "Phi_i ... ~ (3, 0)" [S Gl. (9)-(14)]; M_l mit Zeilen (h1 v_i, h2 w^{..} v_i, h3 w^{..} v_i) [S Gl. (18)]; "If v1 = v2 =
  v3 = v, then M_l is easily diagonalized" mit U_L = (1/sqrt3)[[1,1,1],[1,w,w^2],[1,w^2,w]], Massen sqrt3 h_i v [S Gl. (19)].
  Charaktertafel wie meine (chi(3) = 3, 0, 0, -1) [S Tab. 1]. 3 x 3 = 1 + 1' + 1'' + 3 + 3 [S Gl. (1)-(4)].
  - Zusatz (stuetzt 1.8): Quarks mit derselben Zuordnung geben Massenmatrizen, die "diagonal just as that of the charged
    leptons" sind; Mischung nur aus "violation of v1 = v2 = v3", "the final effect is negligible"; fuer die richtige
    CKM-Matrix "all quarks are trivial under A4" [S Abschnitt Quark Sector, Z. 884-900].
  - [M] Gitter gegen MR: Die Gitter-Massenmatrix ist Gl. (18) mit h1 = h2 = h3 und (v1, v2, v3) = (m_x, m_y, m_z);
    M M^+ = 3 h^2 diag(abs(v_r)^2). MR legen die Hierarchie in h_i bei ausgerichtetem VEV, das Gitter kann sie nur in
    den VEV-Komponenten (Bindungsmodulation) tragen.

### F5 (Altarelli/Feruglio/Lin 2007, arXiv:hep-ph/0610165, PDF)

- Erwartung, notiert 2026-10-05 00:58:29 CEST (date): A4 entsteht als Rest der Raumzeit-Symmetrie eines Orbifolds T2/Z2 mit vier Fixpunkten: Z2 x Z2 aus Translationen um halbe Perioden, Z3 aus einer Drehung des speziellen (hexagonalen) Torus; Felder an den Fixpunkten tragen 1 + 3. Verstoss waere: A4 nicht aus Translationen x| Drehung, oder Leptonen nicht als 3 aus Fixpunkt-Vertauschung.
- Abruf 00:58:35 (curl, PDF 16 S., quellen/F5-AltarelliFeruglioLin-hep-ph-0610165-20261005-005835.pdf, Text *.raw.txt).
- **Ausgang: bestaetigt.** "a discrete subgroup of rotations and translations in the extra space is left unbroken. This
  group can be generated by two transformations: S : z -> z + 1/2, T : z -> omega z" [S Gl. (3)]; "S and T induce even
  permutations of the four fixed points ... thus generating the group A4" [S Gl. (4)]; "A4, together with 4D translations
  and 4D proper Lorentz transformations, can be seen as the subgroup of the space-time symmetry in six dimensions that
  survives compactification" [S S. 3]; Brane-Felder a = (a1, ..., a4) an den vier Fixpunkten [S Gl. (17)].
  - [ES] Fourier-dual zu 1.5: Bei AFL vertauschen Halbperioden-Translationen vier Orte (1 + 3); auf dem Diamant geben
    fcc/sc-Translationen vier Impulse Gamma, X_x, X_y, X_z Charaktere (Gamma = 1, die drei X = 3). Gleiche Gruppe, gleicher
    Mechanismus (Translation x| Drehung), einmal im Orts-, einmal im Impulsraum.

### F6 (arXiv-API, nach Datum absteigend: Doppler/Valleys/Taste/Dirac-Punkte UND Generationen/Flavour-Symmetrie/A_4/tetraedrisch; Regel-7-Pruefung)

- Erwartung, notiert 2026-10-05 00:59:50 CEST (date): In den neuesten 50 Treffern (2024 bis 2026) kein Vorschlag, der drei Standardmodell-Generationen aus Gitter-Dopplern oder Valleys ableitet; Treffer eher Festkoerper (Valley-Flavour, Moire) und Gitter-QCD (Taste-Brechung). Verstoss waere: eine neue Arbeit "doublers/valleys as generations" oder "A4 from crystal symmetry" fuer Teilchenfamilien.
- Abruf 00:59:57 (curl, 32 Eintraege gesamt, nach Einreichdatum absteigend, quellen/F6-api-neueste-doppler-flavour-*.xml).
- **Ausgang: bestaetigt, mit einem Zusatzfund.** Juengste Treffer (2025-2026) sind Festkoerper ("flavor" = Spin/Valley in
  rhomboedrischem Graphen, Valley-Hall) und die Roadmap Part II; kein Vorschlag "Doppler/Valleys als Generationen" und
  kein "A4 aus Kristallsymmetrie" fuer Teilchenfamilien. Regel 7: fuer ein anerkanntes Modell "nach Recherchestand nicht
  belegt".
  - Zusatz: Giordano, M. (2023), 2303.03109, PRD 107, 114509: "spontaneous breaking of vector flavor symmetry on the lattice
    is impossible in gauge theories with a positive functional-integral measure ... any order parameter vanishes in the
    symmetric limit of fermions of equal masses"; gilt fuer "staggered, minimally doubled and Ginsparg-Wilson fermions"
    [S Abstract]. [ES] Fuer die Gegensweep-Frage: Gleiche Kegel bekommen ihre Hierarchie nicht spontan aus einer
    vektorartigen Eichdynamik; ob der Satz auf die diskrete Kegel-Symmetrie passt, ist offen.
  - Lampe, B. (2014), 1405.6604: drei Generationen aus Austauschkopplungen "obeying a tetrahedral symmetry"; "The observed
    hierarchy ... is attributed to a natural hierarchy in the microscopic couplings" [S Abstract]. Keine Doppler.
  - Creutz, M. (2007), 0708.1295: "the exact chiral symmetry of staggered fermions is a flavored symmetry among the four
    'tastes'"; Rooting "forbids the appearance of the correct 't Hooft vertex" [S Abstract].
- **Abrufe: 6 von 6 verbraucht.** Projekt-grep 01:01 (mit allen Ausschluessen) nach Dimension-6/IceCube: c^(6) fuer
  Photonen in KUBISCH-ANKER-L [P]; nichts zu generationsabhaengiger Neutrino-Dispersion.

## 5. Gegensweep (01:02): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Das Vorzeichen -1 von C2x auf B an X_z ist physikalisch, nicht Eichartefakt | ja [M] | B an X_z ist ein 1-dim invarianter Unterraum, der Eigenwert haengt nicht an der Phasenwahl. Er haengt am Drehzentrum: C2x um B = C2x um A mal Translation (a/2)(0,1,1), die auf X_z mit e^{-i pi} = -1 wirkt. Dann tauschen A und B die Rollen. Konsistent mit 1.3 |
| G2 | Zeitumkehr spielt fuer die Zerlegung keine Rolle | ja [M] | Theta|A,X_r> = |A,X_r> (reell), also bildet Theta 1' auf 1'' ab; mit Spin 2' auf 2''. Folge: Bei exakter C3 und Zeitumkehr spalten die drei Kegel hoechstens 1 + 2 (zwei bleiben entartet). Drei verschiedene Massen brauchen C3-Bruch |
| G3 | Ausser den drei X gibt es keine weiteren Kegel | ja, ueber [P/E] DIAMANT-NULLSTELLEN-1 | nur X (45 von 45 Treffern) |
| G4 | Ein Gitterfeld = eine Teilchenart (drei Kegel = e, mu, tau) | nein | Grundannahme der Karte; FKM-Kegel sind Dirac (vektorartig), die schwache Kopplung ist chiral |
| G5 | Finns Knoten tragen A4 als Lagesymmetrie | nein | Auf Diamant-Knoten (T_d) ja; auf Pyrochlor-Knoten (Tetraederecken, D3d) nicht. Offen (vgl. DIAMANT-FERMION-L G6) |
| G6 | Spin gehoert dazu | teilweise | TETRAEDER-L: Fadenenden spinlos [P]. Ein spinloses FKM gibt es nicht (ohne lambda Knotenlinien X-W [P]); fuer spinlose Zustaende gilt die orbitale Zerlegung 1.3 |

## 6. Berichtigungen und Abschluss

- Berichtigung (01:06, nach grep an der lokalen FKM-Kopie): In Abschnitt 0 steht "[S-lokal Z. 455-476]". Genauer: Dirac-Punkte
  an X Z. 468-469, Massenformel m_z Z. 479, "multicritical point" Z. 486-488, "At X_r, delta = sgn[m_r]" Z. 506. Im
  DOSSIER sind die genauen Zeilen eingetragen; Abschnitt 0 bleibt unveraendert stehen.
- Erwartungsverstoesse: Die laufende Tabelle (Abschnitt 3: K-1 bis K-3) ist im DOSSIER Abschnitt 2a um K-4 (Catterall:
  eine Generation statt drei), K-5 (Massen-Triplett, MR mit h1 = h2 = h3, keine Mischung), K-6 (Young: kein "nur") und
  K-7 (Giordano) ergaenzt.
- Rueckfragen R1 bis R4: alle bearbeitet (R1 F3, R2 F5, R3 F4, R4 F1/F2/F6). Neu offen: DOSSIER 7.3, Punkte 1 bis 5.
- DOSSIER.md geschrieben ab 01:02:55; Wortlaut-Berichtigungen 01:06 ("vertauschen mit"; Zeilenangaben FKM; Bedingung
  "sofern beide Lepton-Sektoren ... auf demselben Netz").
- Ende: 2026-10-05 01:06:45 CEST (date).
