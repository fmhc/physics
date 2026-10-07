# QCA-BCC-RUECK-1: Plan des Code-Agenten (Runde 38/39)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 09:24:34 CEST (date). Gelesen ab 09:24: KARTE.md,
  qca-gegenlesen/GEGENLESEN.md (ganz), qca-diamant-4 (PLAN.md, ERGEBNIS.md, code/qca_diamant.py), qca-dirac-t-1
  (PLAN.md, ERGEBNIS.md, code/qca_dirac.py, bild.py), qca-tetra-1 (ERGEBNIS.md, PLAN.md Abschnitt 0), v3-README,
  kleintest.sh auf der .69.
- Vor dem Plan gesehen (offengelegt): Mit jq die Gewichte S+/S- der Treffer in qca-dirac-t-1/lauf-69/haupt_B*.json
  gelesen. Form N, K4: 10 von 12 nichttrivialen Treffern mit Gewicht genau (4, 4), K5: 1 von 9. Das hat R3 (Abschnitt
  3) angeregt.
- Literatur ab 09:29 (1 Abruf), Code bis 09:41:35 CEST (scp, date), Rauchlauf 1 ab 07:41:39 UTC, Plantext ab
  09:43:25 CEST (date). Der Schreibtisch R1 bis R5 stand vor Rauchlauf 1 in den Grundzuegen; aufgeschrieben ist er
  erst hier. Was die Rauchlaeufe zeigten, steht in Abschnitt 7.
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde39-qca-rueck/ (code/, rauch/, lauf/), Start nur ueber
  kleintest.sh, Spuren cpu5 und p4000b, hoechstens zwei Laeufe zugleich, je ssh-Aufruf ein Starteraufruf. Reine
  CPU-Rechnung (numpy, scipy, matplotlib).
- **Kennzeichen:**
  - [S] an der Quelle gelesen: D'Ariano, Erba, Perinotti, "Isotropic quantum walks on lattices and the Weyl
    equation", arXiv:1708.00826v2 (30. Nov. 2017), PRA 96, 062101 (2017). PDF (7 Seiten) als Bild gelesen, Kopie
    quelle/dariano-erba-perinotti-2017-arXiv-1708.00826.pdf (sha256 dc410794...7bb91c81). Dazu die Lesung der Quelle
    von 2014 (D'Ariano/Perinotti, PRA 90, 062106) aus qca-tetra-1 und qca-gegenlesen.
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher; [M] eigene Mathematik; [F] Festlegung dieses Plans;
    [H] Hypothese; [R] im Rauchlauf gesehen (vor dem Einfrieren).
- Die Vorhersagen QR0 bis QR2 und ihre Wahrscheinlichkeiten stehen unveraendert auf der Karte. Zahlenschwellen nennt
  die Karte nicht; die hier festgelegten sind mit [F] markiert.

## 0. Literatur [S]

- **Abrufe:** 1 von 3 (WebFetch auf arxiv.org/pdf/1708.00826). Das Werkzeug lieferte keinen Text, nur die abgelegte
  PDF; alle Fundstellen unten habe ich selbst auf den Seitenbildern gelesen.
- **Umfang der Klassifikation (S. 1, Abstract):** "We present a thorough classification of the isotropic quantum walks on
  lattices of dimension d = 1, 2, 3 with a coin system of dimension s = 2. For d = 3 there exist two isotropic walks,
  namely the Weyl quantum walks". S. 4: "From now on we will restrict to s = 2". Schluss (S. 7): "complete
  classification ... with coin dimension s = 2".
  - Folge: Zu s = 4 und s = 8 und zur Gruppe T mit mehr als zwei Zustaenden sagt die Arbeit nichts. QR1 und QR2 sind
    aus ihr **nicht vorab ableitbar**.
- **Rueckspruenge, woertlich:**
  - S. 2: "A = Σ_{h∈S} T_h ⊗ A_h, where S = S_+ ∪ S_−, S_− = S_+^{−1} is the set of inverses of S_+". Weiter: "Generally
    we will consider also self-transitions ... S ≡ S_+ ∪ S_− ∪ {e}. In the following, for each group G considered, we
    will assume A_h ≠ 0 for all h ∈ S_+ ∪ S_−, whereas in general we allow for the case A_e = 0."
  - S. 4, Abschn. V: "By definition the transition matrices are nonnull, hence |A_h| and |A_−h| must have orthogonal
    supports, and for s = 2 they must then be rank-one."
  - Die Arbeit verlangt also mehr als die Quelle von 2014 ("if A_gg' ≠ 0 then A_g'g ≠ 0"): alle acht Spruenge besetzt.
    Unter T ist beides dasselbe (R1).
- **Isotropie (S. 2, Definition 1):** "there exists a projective unitary representation U over C^s of L such that
  A_λ(h) = U_l A_h U_l^†", Λ transitiv auf jedem S_+^n. Dazu Eq. (2), S. 2: "[U_l, A_h] ≠ 0 ∀h ∈ S_+, ∀l ∈ L : l(h) ≠ h"
  ("two transition matrices associated to different generators must be distinct"); beschreibend geprueft.
- **Eq. (9), S. 3:** "modulo a uniform local unitary we can always assume Σ_h A_h = I_s": W → W(0)^† W. Die Normierung
  ist eine Eichung (Abschnitt 1, Punkt 5).
- **Ausschluss von Z_3 bei s = 2 (S. 5, vor Prop. 3):** "it follows that all the n_k must be mutually orthogonal and then
  |K| ≤ 4. The case K ≅ Z_3 is not consistent with Eqs. (17) and (18)." Fig. 1 (S. 6): "Body-centered cubic (BCC)
  lattice (c): the only possible isotropy group is U_L = {I, iσ_X, iσ_Y, iσ_Z}". Damit ist T bei s = 2 in der Arbeit
  selbst ausgeschlossen (wie QCA-TETRA-1, M1/M2).
- **Prop. 5c (S. 7):** d = 3, s = 2: A_e = 0 und die acht Matrizen mit η^± = (1 ± i)/4 (Weyl). Auf S. 6 steht
  α_+² = α_−² = 1/4, also ist das Sprunggewicht in S_+ und S_− gleich: J_+ = J_− = 1 (R5).
- **Was die Arbeit nicht enthaelt:** Kovarianz unter T fuer s > 2, Blockzerlegung, Muenze mal Verschiebung. Andere
  Arbeiten zu s = 4 oder s = 8 unter T kenne ich nicht [L?]; nicht weiter gesucht (Zeitbox).

## 1. Kartenpruefung und Festlegungen (vor dem Einfrieren offengelegt)

1. **Rueckspruung-Bedingung: Matrix oder Block (Kartenluecke, Festlegung) [M, F]:**
   - Woertlich (Quelle 2014, Karte) heisst die Bedingung: A_h ≠ 0 ⇒ A_−h ≠ 0 als Matrizen ("Matrix-Lesart").
   - Diese Lesart erfuellt schon eine direkte Summe zweier entkoppelter Automaten, von denen einer nur in S_+ und der
     andere nur in S_− springt. Beispiel mit 8 Zustaenden: (C_1 S_+) ⊕ (C_2 S_−) auf (2+2') ⊕ (2+2') (R2). Jedes
     Teilchen springt dann nur in eine Richtungsgruppe, also genau der Befund A4, den die Karte beheben will.
   - **Haupturteil mit der Block-Lesart:** Fuer jeden unzerlegbaren Teilautomaten (gemeinsamer invarianter Unterraum
     aller A_h; Bloecke aus dem Kommutanten der *-Algebra der A_h) gilt die Bedingung innerhalb des Blocks.
   - Die Matrix-Lesart (Kartenwortlaut) steht bei QR1 und QR2 als Vermerk. Bei s = 2 (QR0) fallen beide zusammen.
2. **Mindestnorm [F]:** "besetzt" heisst ||A_h||_F ≥ 1e−3 · max_h' ||A_h'||_F (im Block: Normen der komprimierten
   Q^†A_hQ, relativ zum groessten im Block). Begruendung:
   - Numerische Reste exakt verschwindender Spruenge liegen bei ≤ 3e−6 in der Norm (QCA-DIAMANT-4: Gewichtsrest
     ≤ 7,1e−12 vor der Nachpolitur), also mehr als zwei Groessenordnungen darunter.
   - Ein einseitiger Automat mit einer Beimischung ε der Gegenrichtung verletzt die Unitaritaet in der Frequenz 2h
     in erster Ordnung (Defekt ~ε²); bei ε = 1e−3 sind das ~1e−6, weit ueber der Trefferschwelle. Faellt die erste
     Ordnung weg, bleibt ~ε⁴ = 1e−12; das faengt Punkt 3 ab.
   - Die Varianten mit festem Anteil (Punkt 4) liegen bei Normverhaeltnissen ≥ 0,23, weit ueber 1e−3.
3. **Treffer und Gueltigkeit [F]:** Treffer heisst Defekt < 1e−10 (Karte, wie die Vorgaenger). Fuer die Urteile zaehlen
   nur **gueltige** Treffer: voller Unitaritaetsdefekt nach der Nachpolitur ≤ 1e−20, Kovarianz ≤ 1e−10, Rest der
   Nebenbedingungen ≤ 1e−9. Grund: Eine Beimischung ε ~ 1e−3 an einen einseitigen Automaten koennte bei Defekt ~ε⁴
   formal als Treffer zaehlen; eine echte Loesung poliert auf ≤ 1e−22 (QCA-DIRAC-T-1: ≤ 2,5e−22, meist ≤ 1e−28).
   Vermerk bei QR1: Zaehlung ohne die Schwelle 1e−20.
4. **Nebenbedingung als feste Anteile statt Strafterm [F]:** Variante "frei" (keine Bedingung, Einordnung danach)
   sowie r50, r20, r05 mit der zusaetzlichen Residuenzeile (1 − w)J_+ − wJ_− = 0, J_± = Σ_{h∈S±}||A_h||²_F,
   w = 0,5; 0,2; 0,05. In Form O zusaetzlich J_+ + J_− = s/2 (sonst erfuellt der reine Vor-Ort-Automat die Bedingung).
   Ein fester Anteil hat keine Randloesungen nahe einseitiger Automaten; die Variante frei deckt beliebige Anteile ab.
5. **Formen [F]:** N (acht BCC-Spruenge, wie Prop. 5c und QCA-DIAMANT-4 Teil B) und O (dazu Vor-Ort-Term A_0, "self-
   transitions", S. 2 der Arbeit von 2017). Haupturteil mit N oder O; Vermerk nur N. Die Variante W(0) = I (Eq. 9) rechne
   ich nicht: W → XW mit konstantem unitaerem X im Kommutanten von V erhaelt Kovarianz, Unitaritaet und alle Normen
   ||A_h||, also auch die Rueckspruung-Bedingung (Matrix-Lesart); Eq. (9) ist nur eine Eichung.
6. **Kegel [F, wie QCA-DIAMANT-4 und QCA-DIRAC-T-1]:** Kegel heisst Kegel bei k = 0: ein Cluster von W(0) (Phasenabstand
   < 1e−7), dessen erste Ordnung in allen 126 Richtungen aufspaltet (halbe Spreizung > 1e−6, exakt aus dW/dk) und
   echt koppelt (relativer Kommutator der Generatoren > 1e−2). Verdoppler (H, P, P') und Masse beschreibend.
7. **Isotropie [F]:** Fuer jeden Kegel v(k̂) = Spreizung/(2|k|) ueber 400 Fibonacci-Richtungen, Streuung =
   Standardabweichung/Mittel. "Isotrop" heisst: Streuung ≤ 1e−3 bei |k| = 1e−5 (erste Ordnung) und ≤ 1e−2 bei
   |k| = 0,05 (Aufgabe: "Richtungsstreuung der Geschwindigkeit bei abs(k) = 0,05").
   - Begruendung fuer 1e−2: Der Weyl-Automat der Quelle, den die Quelle isotrop nennt, hat bei 0,05 die Streuung
     2,8e−3 (QCA-TETRA-1); 1e−2 laesst ihn mit Faktor 3,5 Abstand zu.
   - Vermerk "streng": ≤ 1e−3 bei 0,05. Daran scheitert schon der Quellautomat.
8. **360 Grad = −1 [F]:** Am Treffer selbst: implementierende Unitaere fuer C2x und C2y eindeutig (kleinster
   Singulaerwert ≤ 1e−8, zweitkleinster ≥ 1e−4) und Kommutator K = −I (≤ 1e−8), "projektiv" wie QCA-DIAMANT-4. Dazu
   im isotropen Kegel-Cluster P V(C2x)² P = −P, P K P = −P, P V(C3)³ P = −P (≤ 1e−10, ueber die 2T-Lifts). Haupturteil
   verlangt beides; Vermerk nur ueber die Darstellung (der Gegenleser nennt diese Pruefung eine Wahl, keinen Befund).
9. **Nichttrivial [wie QCA-DIRAC-T-1]:** nicht trivial, wenn die W(k) nicht vertauschen (> 1e−8, sechs Paare), das
   relative Spektrum nicht konstant ist (> 1e−8, Gitter 12³) und das Sprunggewicht ≥ 1e−10 ist.
10. **Darstellungsliste vollstaendig [M]:**
    - **Dimension 4:** die fuenf Summen eindimensionaler Darstellungen von T (bis auf ⊗χ), 1+3 (Kontrolle 1'+3),
      2+2, 2+2' (Kontrolle 2+2''; 2+2'' = (2+2')⊗1'' ist in der Konjugation dieselbe Klasse). Gemischte Darstellungen
      von 2T (2^(n) plus zwei eindimensionale) rechne ich nicht: V(−1) = diag(−I_2, I_2) vertauscht mit allen A_h, der
      Automat zerfaellt in einen linearen und einen spinoriellen 2-Zustands-Automaten unter T, beide unmoeglich (M1, M2
      bzw. S2 mit r = 1, auch mit Vor-Ort-Term) [M].
    - **Dimension 8:** die fuenf Spinorklassen K1 bis K5 (wie QCA-DIRAC-T-1) gerechnet. Gemischte Klassen zerfallen
      ebenso in Summen von Automaten der Dimensionen (4, 4), (6, 2) oder (2, 6); die 2-dim Summanden sind unmoeglich,
      bei (4, 4) gilt die Block-Lesart je Summand, also das s = 4-Ergebnis. Rein lineare 8-dim Klassen (24 bis auf
      ⊗χ; 15 davon nur eindimensionale Summanden, nach D1 ohne Spruenge) rechne ich nicht: Sie koennen 360 Grad = −1
      nicht tragen und gehoeren zu keiner Vorhersage. Luecke offen benannt.
11. **Urteil nach Kartenwortlaut:** Kartenwortlaut = Matrix-Lesart (Punkt 1); steht bei QR1 und QR2 als Vermerk.
    Sonst weiche ich vom Wortlaut nicht ab.

## 2. Darstellungen und Gitter

- Wie QCA-DIRAC-T-1: t_a = (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1), h_a = t_a/√3, S = {±h_a}; T aus C2x und R3 mit
  2T-Lifts U(C2x) = −iσx, U(R3) = (I − i(σx + σy + σz))/2; 2^(n) = ω^{n q(g)} U(g).
- s = 2 (QR0): L_2 = {E, C2x, C2y, C2z} mit {I, iσx, iσy, iσz} (Quelle).
- s = 4: Liste aus Abschnitt 1, Punkt 10 (zehn Faelle). s = 8: K1 = 2+2+2+2, K2 = 2+2+2+2', K3 = 2+2+2+2'',
  K4 = 2+2+2'+2', K5 = 2+2+2'+2''.

## 3. Schreibtisch [M]

- **R1 (Reduktion unter T):** T besteht aus eigentlichen Drehungen, die das Tetraeder {t_a} erhalten, bildet also S_+
  auf S_+ ab und wirkt auf S_+ und S_− je transitiv. Kovarianz erhaelt die Frobenius-Norm: ||A_h|| = a_+ auf S_+,
  a_− auf S_−. Die Bedingung (Matrix-Lesart) heisst dann a_+ > 0 und a_− > 0; das ist zugleich "alle acht A_h ≠ 0"
  (Arbeit von 2017). Aus der Frequenz 0: 4(a_+² + a_−²) + ||A_0||² = s.
- **R2 (direkte Summe):** Fuer V = V_1 ⊕ V_2 und T-kovariante unitaere Automaten W_1 (nur S_+) und W_2 (nur S_−) ist
  W_1 ⊕ W_2 T-kovariant und unitaer und erfuellt die Matrix-Lesart, aber in keinem Block die Bedingung. Mit 2+2'
  (Ind χ, monomial) gibt es W_1 = C_1 S_+(k) und W_2 = C_2 S_−(k) (QCA-DIAMANT-4 Teil B; S_−(k) = Σ_a e^{−ik·h_a}|p_a⟩⟨p_a|
  mit derselben monomialen Basis, denn −h_a hat denselben Stabilisator C_3 wie h_a).
- **R3 (Konstruktion mit 8 Zustaenden):** W(k) = X·(C_1 S_+(k) ⊕ C_2 S_−(k)) auf V = Ind χ ⊕ Ind χ' (K4 = (2+2') ⊕
  (2+2'), K5 = (2+2') ⊕ (2+2'')), C_i im Kommutanten der Teile, X unitaer im Kommutanten von V.
  - Unitaer (Produkt von Unitaeren) und T-kovariant (jeder Faktor ist kovariant).
  - J_+ = J_− = 4 fuer jedes X. Mischt X die beiden Sektoren, ist der Automat (generisch) unzerlegbar und erfuellt die
    Block-Lesart: Ein Teilchen springt um h_a, die Muenze dreht es in den S_−-Sektor, dann kann es um −h_a zurueck.
  - Bei k = 0 vertauscht W(0) = X(C_1 ⊕ C_2) mit V; bei K4 ist der Kommutant M_2 ⊕ M_2, also generisch vier
    Zweifach-Cluster, jedes eine 2T-Irrep 2 oder 2'. Auf jedem ist die erste Ordnung c k·σ (Hom_T(3, End 2) ist
    eindimensional, QCA-GEGENLESEN 2.6), in erster Ordnung also isotrop; c ≠ 0 ist generisch. 360 Grad = −1, weil V
    spinoriell ist.
  - Folge: QR2 ist **bis auf die Isotropie bei |k| = 0,05 vorab ableitbar**. T erlaubt in zweiter Ordnung
    a k² I + b Q·σ (QCA-DIRAC-T-1 S5); der Term b Q·σ macht die Spreizung bei endlichem k richtungsabhaengig. Ob ein
    Automat bei 0,05 unter 1e−2 bleibt, ist offen und wird gerechnet.
- **R4 (4 Zustaende):**
  - Moegliche Darstellungen: Nach D1 (QCA-DIAMANT-4; die Frequenz h_i − h_j hat keinen Vor-Ort-Beitrag, gilt also auch in
    Form O) scheiden die eindimensionalen Summen aus, nach S2 (QCA-DIRAC-T-1, mit und ohne Vor-Ort-Term) 2+2, nach
    Abschnitt 1, Punkt 10 die gemischten. Es bleiben 1+3 und 2+2' (und Gleichwertige), beide monomial (Ind χ von C_3).
  - Sektortrennung ausgeschlossen: Π_+ := Σ_a P_a^†P_a (P_a = A_{h_a}, M_a = A_{−h_a}) vertauscht mit V, ist also bei
    2+2' gleich x P_2 + y P_2'. Fall Π_+ = P_2 (S_+ wirkt nur auf 2, S_− nur auf 2'):
    - Frequenz h_i − h_j: P_j^†P_i + M_i^†M_j = 0, die Summanden liegen in End(2) bzw. End(2'), also beide 0.
    - Dann haben die vier P_a paarweise orthogonale Bilder und Σ P_a^†P_a = P_2 (Rang 2): Rang 1,
      P_a = α|u_a⟩⟨v_a| mit Orthonormalbasis u_a von C^4 und v_a ∈ 2 (Eigenvektor von V(C3 um h_a), also
      |⟨v_a|v_b⟩|² = 1/3). Ebenso M_a = β|u'_a⟩⟨v'_a| mit v'_a ∈ 2'.
    - Frequenz h_a + h_b: Die Terme M_b^†P_a + M_a^†P_b (Hom(2, 2')) muessen verschwinden; |v'_b⟩⟨v_a| und |v'_a⟩⟨v_b|
      sind linear unabhaengig, also ⟨u'_b|u_a⟩ = 0 fuer a ≠ b; Frequenz 2h_a gibt ⟨u'_a|u_a⟩ = 0.
    - Acht orthonormale Vektoren in C^4 gibt es nicht: Widerspruch (sofern α, β ≠ 0). Ebenso Π_+ = P_2', und bei 1+3
      Π_+ = P_1 oder P_3 (v'_a sind dann die Tetraederrichtungen in 3, paarweise unabhaengig).
  - Offen bleibt der Fall mit gebrochenen Anteilen (0 < x < 1 oder 0 < y < 1). Den beweise ich nicht; er wird gesucht.
    QR1 ist **nicht vorab ableitbar**.
- **R5 (Kontrolle s = 2):** Nach Prop. 5c der Arbeit von 2017 gibt es unter L_2 mit s = 2 nur die Weyl-Automaten, mit
  α_+² = α_−² = 1/4, also J_+ = J_− = 1. Vorab ableitbar: r50 und frei finden Weyl-Automaten (QR0), r20 findet nichts.
- **Folge fuer die Vorhersagen:** QR0 vorab ableitbar (Literatur). QR2 vorab ableitbar bis auf die Isotropie bei 0,05
  (R3). QR1 offen.

## 4. Rechenweg

- **Suche (code/qca_rueck.py):** kovarianter Unterraum (Gruppenmittel ueber T bzw. L_2), Orthonormalbasis E_j,
  A = Σ x_j E_j; Residuen je Bahn der Differenzen unter T × {±1} (gewichtet, wie QCA-DIRAC-T-1) plus Nebenbedingungen
  (Abschnitt 1, Punkt 4); eigenes Levenberg-Marquardt (hoechstens maxit Iterationen, Abbruch bei D < 1e−30 oder
  Stillstand); Startwerte komplex gaussisch, ||x||² = s. Treffer: D < 1e−10; Nachpolitur (30 Gauss-Newton-Schritte) fuer
  1e−28 < D < 1e−10; Gueltigkeit Abschnitt 1, Punkt 3.
- **Codepruefung je Lauf:** Bahn-Defekt gegen vollen Defekt (≤ 1e−10 relativ), J_+ aus der Gram-Matrix gegen direkt
  (≤ 1e−10), Jacobi-Matrix gegen Differenzenquotient (≤ 1e−4), darunter ein Fall mit beiden Nebenbedingungen.
- **Einordnung je Treffer:**
  - Rueckspruenge: Normen der acht A_h, J_+, J_−, J_0, Matrix-Lesart; Bloecke aus dem Kommutanten (Nullraum von
    X A_h − A_h X und X A_h^† − A_h^† X, Schwelle 1e−8 im Singulaerwert), Eigenraeume eines zufaelligen hermiteschen
    Kommutantenelements, Invarianz geprueft; Block-Lesart je Block (Abschnitt 1, Punkt 1 und 2).
  - Klasse (trivial, massiv, Kegel bei 0, sonst), Kegel-Cluster mit Geschwindigkeit, Chiralitaet, Isotropie bei 1e−5
    und 0,05, Spin je Cluster; am Treffer C2x, C2y, C3 und Inversion; H, P, P'; Homogenitaet Eq. (2) (beschreibend).
  - s = 2: Spektralvergleich mit Eq. (29) bzw. Prop. 5c, |cos(Δφ/2)| gegen |c_x c_y c_z ∓ s_x s_y s_z| an 50
    Zufalls-k, Abweichung ≤ 1e−8 heisst "Weyl".
  - Voll eingeordnet werden die ersten 30 nichttrivialen Treffer je Fall; die Urteile zaehlen nur voll eingeordnete.
- **Teil 0:** QR0-Suche (L2:Pauli, Form N, frei, r50, r20), Weyl-Automaten der Quelle als Referenz (Rueckspruenge,
  Isotropie), Konstruktionen R3: K4 gemischt (drei zufaellige X), K4 direkte Summe (X = I, Gegenprobe zur
  Block-Lesart), K5 gemischt (zwei X).
- **Bilder (code/bild.py):** lauf-69/treffer_je_fall.png (Treffer je Darstellung, Form und Variante nach Kategorie,
  kleinster Defekt), lauf-69/omega_treffer.png (Eigenphasen ω(k) laengs Γ–H–N–Γ–P–H fuer Quelle, Konstruktionen und
  je Darstellung den besten Treffer).

## 5. Urteilsregeln (mechanisch in code/auswertung.py)

- **Moegliche Urteile:** "eingetroffen", "nicht eingetroffen", "nicht auswertbar".
- **Vorbedingungen fuer alle:** alle Laeufe Modus haupt; T 12 Elemente ohne Konsistenzfehler, 2T 24, Kern ±I,
  Spinor-SO(3)-Abweichung, U(C2x)² + I und U(R3)³ + I je ≤ 1e−12; jede Darstellung unitaer und projektiv geschlossen
  (≤ 1e−12), Kommutator −I bei projektiven, +I bei linearen; Codepruefung (Abschnitt 4); Projektoren idempotent
  (≤ 1e−10); alle Faelle vorhanden (Teil 0: drei Varianten; Teil 4: zehn Darstellungen × N, O × frei, r50, r20, r05;
  Teil 8: K1 bis K5 × N, O × frei, r50, r20). Sonst alle drei "nicht auswertbar". Laeufe mit rc ≠ 0 liefern keine Datei
  und fehlen dann.
- **QR0:** eingetroffen genau dann, wenn L2:Pauli, Form N, Variante r50 mindestens einen gueltigen nichttrivialen
  Treffer hat, der die Block-Lesart erfuellt, einen Kegel bei 0 hat und spektral Weyl ist (≤ 1e−8). Vermerk: Variante
  frei.
- **QR1:** nicht auswertbar, wenn QR0 nicht eingetroffen ist (Suchkontrolle). Eingetroffen genau dann, wenn es in Teil 4
  (alle zehn Darstellungen, Formen N und O, alle vier Varianten) keinen gueltigen nichttrivialen Treffer gibt, der die
  Block-Lesart erfuellt und einen Kegel bei 0 hat. Vermerke: Matrix-Lesart (Kartenwortlaut); nur Form N; ohne
  Gueltigkeitsschwelle 1e−20; Zahl der Rueckspruung-Treffer ohne Kegel.
- **QR2:** nicht auswertbar, wenn QR0 nicht eingetroffen ist. Eingetroffen genau dann, wenn es in Teil 8 mindestens
  einen gueltigen, nichttrivialen, voll eingeordneten Treffer gibt, der die Block-Lesart erfuellt, einen isotropen
  Kegel bei 0 mit Spin −1 im Cluster hat (Abschnitt 1, Punkte 6 bis 8) und am Treffer "projektiv" wirkt. Vermerke:
  Matrix-Lesart; Isotropie streng (1e−3 bei 0,05); nur Form N; 360 Grad nur ueber die Darstellung; Konstruktionen aus
  Teil 0 (zaehlen nicht fuer das Haupturteil, weil die Karte nach der Suche fragt).
- **Beschreibend:** Treffer und Kategorien je Fall, Defektminima, Geschwindigkeiten, Isotropie, Massen, Verdoppler,
  Homogenitaet, Gleichwertigkeit (1'+3 gegen 1+3, 2+2'' gegen 2+2', K3 gegen K2).
- **Grenze:** Eine Suche ist kein Beweis. Ein "eingetroffen" bei QR1 stuetzt sich auf Suche plus R4 (Teilbeweis).

## 6. Laufplan

- Hauptlaeufe (je ein ssh-Aufruf, Starts und Aufteilung nach Rauchlauf 2, Abschnitt 7):
  - H-0 (cpu5): Teil 0, 40 Starts je Variante.
  - H-4N (p4000b): Teil 4, Form N, alle vier Varianten, 40 Starts je Fall.
  - H-4O (cpu5): Teil 4, Form O, alle vier Varianten, 40 Starts je Fall.
  - H-8 (Teil 8): Aufteilung und Starts siehe Abschnitt 7, maxit 600.
  - danach ueber den Starter: auswertung.py und bild.py (alle Laeufe).
- Faellt ein Lauf aus (rc ≠ 0 oder Zeitabbruch), sind die betroffenen Urteile "nicht auswertbar"; ein zweiter Versuch
  nur bei einem Fehler ausserhalb des Codes, offengelegt.

## 7. Rauchlaeufe [R] (vor dem Einfrieren, offengelegt; Text ab 09:50 CEST)

- **Rauch 1** (07:41:39 bis 07:42:21 UTC, beide rc = 0):
  - Teil 0 (6 Starts, 9,9 s): L2:Pauli frei und r50 je 2 Treffer, alle Weyl (Spektralabweichung ≤ 5,6e−16),
    J_+ = J_− = 1, v = 0,577350, Isotropie bei 0,05 2,82e−3; r20 ohne Treffer (kleinster Defekt 0,165), wie R5.
    Weyl-Referenz A^± exakt unitaer, Block-Lesart erfuellt. Konstruktionen: K4 gemischt (3) und K5 gemischt (2)
    unzerlegbar (Kommutant 1), Kategorie "Rueck + Kegel, isotrop, projektiv"; K4 direkte Summe "Rueck nur Matrix"
    (Kommutant 2, Wirkung mehrdeutig), wie R2.
  - Teil 4 (3 Starts, 35,8 s): frei nur einseitige oder triviale Treffer; r50, r20, r05 ohne Treffer. Kleinste
    Defekte N: r50 0,00153 (2+2', 2+2'') und 4/45 (1+3); r20 0,00846 (1'+3, 2+2'); r05 1,16e−4; O deutlich groesser.
- **Rauch 2** (07:43:20 bis 07:46:11 UTC, rc = 0):
  - Teil 4, nur 1+3 und 2+2', Form N, r50/r20/r05 mit 25 Starts (15,3 s): dieselben Minima (0,0015294 bei 2+2' r50;
    0,0084581 bei r20 fuer beide; 1,1607e−4 bei r05 fuer beide; 1+3 r50 4/45).
  - Teil 8 (2 Starts, 171 s): K4 N frei ein unzerlegbarer Rueck-Treffer mit vier Weyl-Kegeln (v 0,337 und 0,484,
    Streuung bei 0,05 2,4e−4 bis 1,3e−3), projektiv; K4 N r50 ein Rueck-Treffer mit sehr langsamen Kegeln
    (v 0,0066 bis 0,010, Streuung bei 0,05 0,10 bis 0,38); K4 N r20 und K5 N r20 ohne Treffer (0,0234); K5 N r50 bis
    5,0e−7 (langsame Konvergenz, wie in QCA-DIRAC-T-1); K1, K2, K3 ohne Rueck-Treffer; Form O nur trivial oder
    einseitig. Zeiten je Start: N 1,4 bis 4,3 s, O 2 bis 7 s.
- **Rauch 3** (07:48 UTC): auswertung.py auf den Rauchdateien, rc = 0, Urteile "nicht auswertbar" (Modus rauch);
  Diagnose ohne Vorbedingungen QR0, QR1, QR2 je "eingetroffen". bild.py auf p4000b wartete beim Einfrieren noch auf
  die Spur (Lock belegt durch einen fremden Lauf); Ergebnis steht im ERGEBNIS.
- **Aenderungen nach den Rauchlaeufen (vor dem Einfrieren):**
  - auswertung.py: Urteile werden auch bei verletzten Vorbedingungen gerechnet und als Diagnose abgelegt (die
    offiziellen Urteile bleiben dann "nicht auswertbar"); Vermerk "alle Kegel des Automaten isotrop" bei QR2 ergaenzt
    (beschreibend, aendert keine Regel).
  - Keine Schwelle und keine Urteilsregel geaendert. maxit fuer Teil 8 Form N auf 600 (K5 konvergiert langsam),
    Form O bleibt 300 (Zeit).
- **Wirkung auf die Vorhersagen:** Alle drei Ausgaenge habe ich vor dem Einfrieren gesehen: QR0 und QR2 waren am
  Schreibtisch ableitbar (R5, R3), QR1 ist in den Rauchlaeufen ohne Gegenbeispiel. Offen fuer die Hauptlaeufe sind die
  Zahlen (Treffer je Fall, Geschwindigkeiten, Isotropie) und ob mehr Starts doch einen 4-Zustands-Rueck-Treffer finden.
- **Hauptlaeufe (festgelegt nach Rauch 2):**
  - cpu5: H-0 (Teil 0, 40 Starts je Variante), H-4O (Teil 4, Form O, alle Varianten, 40 Starts), H-8Na (Teil 8,
    Form N, frei und r50, 12 Starts, maxit 600), H-8Nb (Teil 8, Form N, r20, 12 Starts, maxit 600)
  - p4000b: H-4N (Teil 4, Form N, alle Varianten, 40 Starts), H-8Oa (Teil 8, Form O, frei, 12 Starts), H-8Ob (Teil 8,
    Form O, r50 und r20, 12 Starts)
  - Ist p4000b durch fremde Laeufe belegt, laufen die Auftraege dort spaeter oder nacheinander auf cpu5; Inhalt und
    Saat bleiben gleich.

## 8. Einfrieren

- Eingefroren: Zeit und Pruefsummen in EINGEFROREN-SHA256.txt und im Dateinamen PLAN.md.eingefroren-*. Danach keine
  Aenderung an Plan und Urteilsregeln; Code nur bei echten Fehlern, offengelegt.
