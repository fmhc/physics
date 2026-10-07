# QCA-DIAMANT-4: Plan des Code-Agenten (Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 06:48:09 CEST (date). Gelesen ab 06:48: KARTE.md,
  qca-tetra-1 (PLAN.md, ERGEBNIS.md, code/), RUNDE-38.md (Ernte QCA-TETRA-1), v3-README, kleintest.sh.
  Code ab 07:09:51, Plantext ab 07:14:18 CEST (date), vor dem ersten Rauchlauf.
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde38-qca-diamant/ (code/, rauch/, lauf/), Start nur
  ueber kleintest.sh, Spuren cpu5 und p4000b, hoechstens zwei Laeufe zugleich. Reine CPU-Rechnung (numpy, scipy,
  matplotlib).
- **Kennzeichen:**
  - [S] an der Quelle gelesen (D'Ariano/Perinotti, PRA 90, 062106 (2014), arXiv:1306.1934v2; Lesung in
    qca-tetra-1/PLAN.md Abschnitt 0, kein neuer Abruf)
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher
  - [M] eigene Mathematik (Schreibtisch, vor jeder Rechnung)
  - [F] Festlegung dieses Plans (die Karte laesst es offen)
  - [H] Hypothese; [R] im Rauchlauf gesehen (vor dem Einfrieren)
- Die Vorhersagen QD0 bis QD3 und ihre Wahrscheinlichkeiten stehen unveraendert auf der Karte; die Karte nennt keine
  Zahlenschwellen. Hier stehen Modell, Messvorschrift und Urteilsregeln.

## 0. Uebernommen aus QCA-TETRA-1

- Isotropie nach der Quelle (Eq. 5) [S]: Es gibt eine treue unitaere (projektive) Darstellung V einer Gruppe L von
  Graph-Automorphismen, transitiv auf den Richtungen, mit A_{l(h)} = V(l) A_h V(l)^† fuer alle l, h. Nur die
  Konjugationswirkung zaehlt; V und V ⊗ χ (χ eindimensional) geben dieselben Bedingungen [M].
- Eq. (19) [S]: "Ã_{k=0} commutes with the representation U ..., whence we can classify the automata by requiring
  identity (19)": Σ_h A_h = I. Fuer irreduzibles V folgt das bis auf eine Phase (Schur); fuer reduzibles V nicht [M].
- Defekt D = Σ_d ||Σ_{f−f'=d} A_{f'}^†A_f − δ_{d0} I||_F² (exakt, nach Parseval das Zonenmittel von ||W^†W − I||_F²),
  Suche mit Levenberg-Marquardt im kovarianten Unterraum, Treffer D < 1e−10. Code qca_tetra.py auf s Zustaende
  verallgemeinert (code/qca_diamant.py).
- Vektoren: t_a = (1,1,1), (1,−1,−1), (−1,1,−1), (−1,−1,1); Bindung e_a = t_a/√3 (Laenge 1); u = k/√3.
- Diamantnetz: A-Knoten bei x, Nachbarn (B) bei x + e_a. Gruppen am A-Knoten: L_2 = {E, C2x, C2y, C2z} und
  T (12 Drehungen); beide permutieren die vier Striche transitiv (L_2 einfach transitiv, T mit Stabilisator C_3).

## 1. Kartenpruefung (vor dem Einfrieren offengelegt)

1. **Zweite Fassung (Kartenfehler, berichtigt):**
   - Das Beispiel der Karte, "ein gleichzeitiger Sprung beider Untergitter", ist dieselbe Regel wie Fassung 1 [M]:
     U = ((0, X̂), (Ŷ, 0)) ist genau dann unitaer, wenn X̂(k) und Ŷ(k) unitaer sind, und U² = diag(X̂Ŷ, ŶX̂); das
     Spektrum von U ist ±√spec(X̂Ŷ). Der Zweischritt A → B → A mit unitaeren Halbschritten und der gleichzeitige
     Sprung haben also dieselben Loesungen und dieselben Kegel.
   - **Fassung 1 (Kartenwortlaut, wie QCA-TETRA-1 C-1):** Ŷ(k) = Σ_a e^{−ik·e_a} B_a (A → B laengs +e_a),
     X̂(k) = Σ_a e^{ik·e_a} C_a (B → A laengs −e_a), beide unitaer; B_a und C_a unabhaengig, Isotropie
     B_{ga} = V(g) B_a V(g)^†, C_{ga} = V(g) C_a V(g)^† mit demselben V auf beiden Untergittern.
   - **Fassung 2 (begruendete Alternative, Cayley-Graph-Fassung) [F]:** Das Diamantnetz ist der Cayley-Graph der Gruppe
     Z³ ⋊ Z_2 mit vier Involutionen s_a = (e_a, −1) [M]: (R, +)·s_a = (R + e_a, −), (R, −)·s_a = (R − e_a, +). Die
     Homogenitaet der Quelle (dieselben Uebergangsmatrizen an jedem Knoten) verlangt dann C_a = B_a: ein Schritt, in
     dem jeder Knoten beider Untergitter mit denselben vier Matrizen zu seinen Nachbarn springt. Das ist die
     woertliche Uebertragung der Quelle und zugleich die einfachste Lesart von "gleichzeitiger Sprung"; sie ist ein
     Spezialfall von Fassung 1 (X̂(k) = Ŷ(−k)) und prueft, ob Treffer die strengere Regel ueberleben.
   - **Urteil nach Kartenwortlaut:** Weil das Kartenbeispiel gleich Fassung 1 ist, ist das Urteil nach Kartenwortlaut
     das Urteil nur mit Fassung 1 (Vermerk bei QD1 und QD2).
2. **C-2-Lesart nicht gerechnet [F]:** QCA-TETRA-1 rechnete zusaetzlich C-2 (nur der Zweischritt unitaer). Fuer s = 4
   enthaelt C-2 die Fassung 1, kann also nur Treffer hinzufuegen. QD1 ist schon mit Fassung 1 entschieden (Abschnitt
   3, D4), QD2 ebenso (D4: lineare Treffer mit Kegel in Fassung 1). Dazu die Kosten: C-2 brauchte mit s = 2 schon
   440 s fuer drei Faelle. Grenze: Eigene Treffer von C-2 jenseits von Fassung 1 bleiben ungeprueft.
3. **"Unzerlegbare" 4-dim Darstellungen gibt es nicht [M]:** Die irreduziblen Darstellungen haben die Dimensionen
   1, 1, 1, 3 (T = A_4), 1, 1, 1, 2, 2, 2, 3 (2T), 1, 1, 1, 1 (L_2 linear) und 2 (L_2 projektiv, Pauli). Jede 4-dim
   Darstellung ist also zerlegbar (endliche Gruppe, unitaer, Maschke). Die 4-dim irreduzible Spin-3/2-Darstellung
   (Γ_8 der Doppelgruppe von O bzw. T_d) zerfaellt auf 2T in 2' + 2'' [L] und ist in der Konjugation gleich 2 + 2';
   sie ist damit mitgerechnet. Uneigentliche Drehungen (T_d) rechne ich wie die Quelle nicht.
4. **"Kegel bei k = 0" fuer s = 4 [F]:** wie in QCA-TETRA-1 verallgemeinert (Abschnitt 5). Mehrfachpunkte mit linearen
   und flachen Zweigen zaehlen als Kegel; der Typ wird beschreibend mitgeschrieben.
5. **Eq. (19) [F]:** Fuer reduzibles V folgt W(0) = I nicht aus der Isotropie. Ich rechne jede Fassung in zwei
   Varianten: "frei" (nur Unitaritaet und Isotropie) und "w0" (zusaetzlich W(0) = I wie Eq. 19; im Diamant
   W(0) = X̂(0)Ŷ(0)). Treffer beider Varianten zaehlen; die Urteile nur mit "frei" stehen als Vermerk daneben.
6. **Teil B:** Die Karte beschreibt einen "Dirac-artigen Automaten (zwei Weyl-Anteile mit Massenkopplung)", QD3 fragt
   aber nach einem Kegel. Ein massiver Dirac-Automat hat keinen Kegel. Geurteilt wird nach dem Wortlaut von QD3
   (Kegel irgendwo in der Brillouin-Zone); Treffer ohne Kegel werden beschreibend gezaehlt. Gruppe nur T (Karte).
7. **QD2 ohne Treffer [F]:** Gibt es keinen QD1-Treffer, ist QD2 "nicht auswertbar" (Aussage ueber eine leere Menge).
8. **360 Grad [F]:** phasenfrei ueber den Kommutator K = U_x U_y U_x^† U_y^† der implementierenden Unitaeren der
   180-Grad-Drehungen (wie QCA-TETRA-1). Bei T ist das ausreichend: Die Spinorklasse von 2T schraenkt sich auf L_2 zur
   Pauli-Klasse ein (K = −I), die lineare zu K = +I [M, im Code an jeder Darstellung geprueft]. V(C3)³ ist in 4 Dim
   nicht phasenfrei; die C3-Implementierbarkeit wird beschreibend mitgeschrieben.

## 2. Darstellungsliste (4 Dimensionen) [M]

- Gleichwertigkeit: V und V ⊗ χ geben dieselbe Konjugation; aequivalente Darstellungen geben unitaer aequivalente
  Loesungen. Gerechnet wird je Klasse mindestens ein Vertreter, bei T einige Gleichwertigkeitskontrollen.
- **T (12 Elemente), 10 Faelle:**
  - linear, Summen eindimensionaler Darstellungen 1, 1', 1'' (bis auf ⊗χ fuenf Klassen): 1+1+1+1, 1+1+1+1',
    1+1+1+1'', 1+1+1'+1', 1+1+1'+1''
  - linear: 1+3 (= Permutationsdarstellung der vier Striche = 2 ⊗ 2 "Spinor x Spinor") und 1'+3 (gleichwertig,
    Kontrolle; 1''+3 ebenso)
  - projektiv (2T): 2+2 (= 2'+2' = 2''+2'' in der Konjugation), 2+2' (= 2'+2'' = Spin 3/2 auf 2T) und 2+2''
    (gleichwertig zu 2+2', Kontrolle)
- **L_2 (Klein-Vierergruppe), 8 Faelle:**
  - linear: Summen von vier Charakteren 1, χx, χy, χz; bis auf Verschiebung elf Klassen. Gerechnet: 1+1+1+1,
    1+1+1+x, 1+1+x+x (Traeger hoechstens zwei Charaktere; die y- und z-Faelle sind unter der 120-Grad-Drehung des
    Gitters gleich), 1+1+x+y, 1+1+y+z, 1+1+x+z (Traeger drei Charaktere, alle drei Klassen) und 1+x+y+z (regulaer)
  - projektiv: P+P (Pauli ⊕ Pauli); die verdrehte Gruppenalgebra ist M_2(C), es gibt nur diese Klasse.
- Teil A rechnet alle 18 Faelle, Teil B die 10 T-Faelle, Teil 0 (s = 2) BCC L2:Pauli, L2:1+chi_x, T:2 und die zwoelf
  2-dim Faelle von QCA-TETRA-1 auf dem Diamant (Fassung 1).

## 3. Schreibtisch [M] (vor jeder Rechnung)

- **D1 (M1/M3 fuer beliebiges s):** Wirkt eine 180-Grad-Drehung g durch Konjugation trivial, dann gilt
  A_{g h_1} = A_{h_1} =: A und A_{−g h_1} = A_{−h_1} =: B mit g h_1 = h_j ≠ h_1. Der Koeffizient von
  e^{ik·(h_1 − h_j)} in W^†W hat genau die Beitraege A^†A + B^†B (t_1 − t_j ist keine Summe zweier t), muss 0 sein,
  also A = B = 0 und mit der Transitivitaet alle A_h = 0. Widerspruch zu Σ A_h^†A_h = I. Das gilt fuer jedes s.
  - BCC: keine Loesung fuer T:1+1+1+1 bis T:1+1+1'+1'' (V_4 wirkt auf eindimensionalen Darstellungen von A_4
    trivial) und fuer L_2 mit hoechstens zwei Charakteren im Traeger.
  - Offen bleiben auf BCC: T:1+3, T:2+2, T:2+2' (und Kontrollen). Teil B ist damit die eigentliche Rechnung.
- **D2 (Fassung 1, Struktur):** Ŷ unitaer heisst, alle Fourier-Koeffizienten von Ŷ^†Ŷ − I und ŶŶ^† − I verschwinden.
  Die zwoelf Differenzen e_b − e_a sind verschieden, also B_b^†B_a = 0 und B_aB_b^† = 0 (a ≠ b), Σ_a B_a^†B_a = I.
  - Die Urbildraeume W_a = Bild(B_a^†) sind paarweise orthogonal, jedes B_a^†B_a ist der Projektor auf W_a, und
    ⊕ W_a = C^s.
  - Isotropie erhaelt den Rang, also rang B_a = r fuer alle a, 4r = s. Fuer s = 2 unmoeglich (M6), fuer s = 4 ist r = 1.
  - V(g) bildet W_a auf W_{ga} ab: V permutiert vier orthogonale Geraden wie die Striche. Nach dem
    Imprimitivitaetssatz ist V ≅ Ind_{Stab}(λ) (monomial).
  - T: Stab = C_3 (bzw. Z_6 in 2T). Ind(1) = 1+3, Ind(ω) = 1'+3, Ind(ω²) = 1''+3 (linear); Ind χ_1 = 2+2',
    Ind χ_3 = 2'+2'', Ind χ_5 = 2+2'' (Spinor; Frobenius mit den Eigenwerten e^{∓iπ/3} von V(C3) auf 2).
  - L_2: Stab trivial, V ≅ regulaere Darstellung 1+x+y+z (linear) oder verdreht regulaer P+P (projektiv).
  - **Folge:** Fassung 1 (und damit Fassung 2) hat Loesungen hoechstens fuer T:1+3, T:1'+3, T:2+2', T:2+2'',
    L2:1+x+y+z und L2:P+P. Keine Loesung fuer T:2+2, alle eindimensionalen Summen und die L_2-Klassen mit zwei oder
    drei Charakteren im Traeger.
- **D3 (Normalform):** Sei |a⟩ die monomiale Basis (V(g)|a⟩ = φ_a(g)|ga⟩). Zu jeder Loesung gibt es Unitaere T, T' im
  Kommutanten von V mit B_a = U_0 T|a⟩⟨a|T^† und C_a = U_1 T'|a⟩⟨a|T'^† (U_0 = Σ_a B_a, U_1 = Σ_a C_a, beide im
  Kommutanten). Beweis: |p_a⟩ := V(g_a)|p_1⟩ hat dieselben Phasen φ_a(g) wie |a⟩ (gleicher Stabilisatorcharakter, weil
  die Ind(λ) paarweise inaequivalent sind); T: |a⟩ ↦ |p_a⟩ ist unitaer und vertauscht mit V. Damit
  W(k) = X̂Ŷ ≅ C_2 S(−k) C_1 S(k), S(k) = diag(e^{−ik·e_a}), C_1, C_2 beliebige Unitaere im Kommutanten.
  Umgekehrt ist jede solche Wahl eine isotrope unitaere Loesung. Fassung 2: C_2 = C_1.
- **D4 (Kegel bei k = 0, erste Ordnung):** W(k) = W_0 (I − iH_1(k) + O(k²)) mit W_0 = C_2C_1,
  H_1 = K − C_1^†KC_1, K(k) = diag(k·e_a). Auf einem Eigenraum E von W_0 spalten die Eigenphasen linear nach den
  Eigenwerten von P_E H_1 P_E auf.
  - Kommutativer Kommutant (V multiplizitaetsfrei: T:1+3, T:2+2', L2:1+x+y+z): C_1 ist auf jeder isotypischen
    Komponente skalar. Ist E eine einzige Komponente, gilt P_E H_1 P_E = 0: keine lineare Aufspaltung.
  - **T:1+3, frei:** W_0 = diag(λ_1, λ_3 I_3), dreifache Entartung ohne lineare Aufspaltung, also generisch kein Kegel.
    **Mit W_0 = I:** H_1 = −(e^{iψ} − 1)K|s⟩⟨s| + h.c. (C_1 = I + (e^{iψ} − 1)|s⟩⟨s|, s = (1,1,1,1)/2,
    ⟨s|K|s⟩ = 0) hat die Eigenwerte ±(2|sin(ψ/2)|/√3)|k|, 0, 0: ein isotroper Kegel mit zwei in erster Ordnung flachen
    Zweigen. Beispiel: Grover-Lauf C = 2|s⟩⟨s| − I. V ist linear (Permutationsdarstellung), 360 Grad wirken als +1.
  - **T:2+2', frei:** zwei zweifache Entartungen (auf 2 und 2') ohne lineare Aufspaltung, kein Kegel. Mit W_0 = I:
    vierfacher Punkt mit Kopplung 2 ↔ 2'; ob Dirac- oder Rarita-Schwinger-artig, ist offen.
  - **L2:1+x+y+z:** frei W_0 generisch nicht entartet (kein Kegel bei 0); mit W_0 = I vierfacher Punkt, offen.
  - **L2:P+P (Kommutant M_2):** C_i = I ⊗ c_i. In der monomialen (Bell-)Basis ist K = (1/√3) Σ_j k_j σ_j ⊗ σ_j^T.
    Fuer einen Eigenvektor v von c_2c_1 (nicht entartet) ist E = C² ⊗ v und P_E H_1 P_E = Σ_j d_j k_j σ_j mit
    d = (r(v) − r(c_1 v))/√3, r_j(w) = ⟨w|σ_j^T|w⟩. Generisch sind alle d_j ≠ 0: **Weyl-Kegel bei k = 0**, im
    Allgemeinen anisotrop; der zweite Eigenvektor gibt −d, also den Partner mit entgegengesetzter Chiralitaet.
    Isotrop fuer r(v) ∝ (±1, ±1, ±1) und c_1 v ⊥ v: d = (2/3)(±1, ±1, ±1), Steigung 2/3 je Zweischritt (1/3 je
    Schritt). Die Darstellung ist projektiv, 360 Grad wirken als −1.
  - **Fassung 2, frei:** W_0 = C²; die Eigenvektoren von C² sind (generisch) Eigenvektoren von C, also d = 0 bei P+P und
    keine lineare Aufspaltung bei den kommutativen Faellen: generisch kein Kegel bei 0. Mit W_0 = I (C² = I) bleiben
    diskrete Loesungen, darunter der Grover-Lauf (T:1+3) mit Kegel und flachen Zweigen.
- **D5 (Teil B, Dimensionen):** A_{±h_1} muessen mit V(C3 um h_1) vertauschen; kovariante Dimension
  2 Σ_λ m_λ² (m_λ Vielfachheiten der Eigenwerte von V(C3)): 1+3 → 12, 2+2 → 16, 2+2' → 12 (komplex). Einen
  Ausschlussbeweis fuer diese drei habe ich nicht; Teil B wird gerechnet.
- **Folge fuer die Vorhersagen:**
  - **QD0:** vorab ableitbar eingetroffen (QCA-TETRA-1 und M6). Geprueft wird der neue, auf s verallgemeinerte Code.
  - **QD1:** vorab ableitbar eingetroffen (D3, D4: Fassung 1, L2:P+P, Variante frei, generisch Weyl-Kegel bei 0).
  - **QD2:** vorab ableitbar nicht eingetroffen, wenn die Variante w0 mitzaehlt (D4: T:1+3 mit W(0) = I, Kegel bei 0
    mit linearer Darstellung). Nur mit "frei" waere QD2 eingetroffen (nur L2:P+P hat dann Kegel bei 0). Das
    Haupturteil haengt also an Festlegung 1.5; beide stehen im Ergebnis.
  - **QD3:** offen. Das ist die eigentliche Rechnung.
  - Pruefbar sind ausserdem: D2 (Nullbefunde fuer die nicht monomialen Faelle), D4 (Kegeltypen, Geschwindigkeiten),
    die offenen Vierfachpunkte (T:2+2', L2 regulaer, P+P mit W(0) = I) und Verdoppler.

## 4. Rechenweg

- **Suche:** je Fall Orthonormalbasis des kovarianten Unterraums (Gruppenmittel), Parameter komplex, Startwerte komplex
  gaussisch, je Block normiert auf Σ||·||_F² = s. scipy least_squares, method "lm", analytische Jacobi-Matrix,
  Toleranzen 1e−15, max_nfev 400. Residuen: exakte Koeffizienten von Ŷ^†Ŷ − I (Fassung 1 auch X̂^†X̂ − I; Fassung 2 nur
  Ŷ, weil X̂(k) = Ŷ(−k)); BCC W^†W − I; Variante w0 zusaetzlich X̂(0)Ŷ(0) − I bzw. Σ_h A_h − I. Treffer: Gesamtdefekt
  D < 1e−10.
- **Starts:** Haupt 100 je Fall in Teil 0 und Teil B, 40 je Fall in Teil A (Teil A ist am Schreibtisch entschieden,
  D2 bis D4; Zeitbox); Rauch 10 (rauch2_A1w0: 5); Saat 38·10000 + 1000 (BCC) / 2000 (Fassung 1) / 3000
  (Fassung 2) + 100 (w0) + Fallnummer; Rauch mit Saatbasis 3800. Die Starts sind keine Schwelle.
- **Nachpolitur (Diagnose, nach Rauchlauf 1 eingefuehrt):** Treffer mit 1e−26 < D < 1e−10 werden mit 30
  Gauss-Newton-Schritten (lstsq) nachpoliert; D_poliert wird mitgeschrieben, die Einordnung nutzt die polierten
  Parameter, wenn D kleiner wurde. Das Treffermerkmal D < 1e−10 bleibt das der Suche.
- **Einordnung jedes Treffers** (s-Zustaende, W = Schritt auf BCC bzw. Zweischritt X̂Ŷ auf dem Diamant):
  - trivial: Spannweite der sortierten Eigenphasenluecken auf dem Gitter 12³ < 1e−8 (relatives Spektrum konstant)
    **oder** (nach Rauchlauf 1 ergaenzt, Abschnitt 7) alle W(k) vertauschen: max ||[W(u), W(u')]||_max < 1e−8 ueber
    sechs feste Zufallspaare. Dann ist der Automat eine direkte Summe von Ein-Zustands-Verschiebungen.
  - Cluster bei k = 0: Eigenwerte von W(0) mit Phasenabstand < 1e−7 (Gruppen mit m ≥ 2).
  - **Kegel bei k = 0:** fuer einen Cluster (Mitte φ_c, Groesse m) die m Eigenphasen nahe φ_c bei k = εn,
    ε = 1e−5, 126 Richtungen (26 Gitter, 100 Fibonacci); Spreizung sp(ε) = max − min. Kegeltest bestanden, wenn
    sp(ε)/(2ε) > 1e−3 in allen Richtungen und sp(2ε)/sp(ε) in [1,9; 2,1] (wie QCA-TETRA-1 mit
    sp = 2 arcsin β fuer s = 2). **Dazu (nach Rauchlauf 1 ergaenzt, Abschnitt 7): echte Kopplung in erster
    Ordnung.** G_j = Q^†(W(0)^†W(εe_j) − I)Q/(−iε), ε = 1e−4, Q Orthonormalbasis des Clusterraums; Kegel nur, wenn
    max ||[G_i, G_j]||_max / max ||G_i||²_max > 1e−2. Sonst kreuzen nur entkoppelte Zweige (etwa vier geradeaus
    laufende Zustaende), das ist kein Kegel. Die Regel vor Rauchlauf 1 (nur Kegeltest, nur Spektrums-Trivialitaet)
    steht als Vermerk bei jedem Urteil. Beschreibend: Zahl der in erster Ordnung flachen Zweige (|Steigung| < 1e−3
    nach Abzug des Mittels), Geschwindigkeiten, Chiralitaet det(tr(G_i σ_j)/2) bei Zweifach-Clustern, bei BCC das
    Gewicht der Spruenge in S_+ und S_−.
  - Klassen: "Kegel bei 0", "Entartung bei 0 ohne Kegel", "keine Entartung bei 0", "trivial".
  - Isotropie (beschreibend): v(k̂) = sp/(2|k|) ueber 400 Fibonacci-Richtungen bei |k| = 1e−5 und 0,05;
    Standardabweichung und Spannweite relativ zum Mittel. Diamant: W ist ein Zweischritt, je Schritt halbe Werte.
  - **360 Grad:** implementierende Unitaere fuer C2x, C2y und eine C3 (um (1,1,1)) aus dem Treffer selbst
    (Nullraum von U A_h − A_{gh} U ueber alle Bloecke). "projektiv": C2x und C2y eindeutig (kleinster Singulaerwert
    ≤ 1e−8, zweitkleinster ≥ 1e−4) und ||K + I||_max ≤ 1e−8; "linear": eindeutig und ||K − I||_max ≤ 1e−8; sonst
    "mehrdeutig".
  - **Verdoppler und Linien (beschreibend, je Fall die ersten drei nichttrivialen Treffer):** kleinste
    Eigenphasenluecke auf dem Gitter 16³, lokale Minima (bis 16) plus Hochsymmetriepunkte (Diamant: X, W, L, K;
    BCC: H, N, P, −P) als Starts fuer Nelder-Mead; Entartung, wenn Luecke < 1e−6; Aequivalenz modulo reziprokem
    Gitter; Kegeltest dort mit ε = 1e−4 (sonst gleiche Schwellen, einschliesslich Kommutatortest). Ein Punkt ohne
    Kegel mit flachen Richtungen deutet auf Knotenlinien.
- **Bilder:** treffer_teilA.png, treffer_teilB_0.png (Treffer je Darstellung nach Klassen, kleinster Defekt);
  omega_teilA.png, omega_teilB.png (Eigenphasen von W(k) laengs Γ–X–W–L–Γ–K bzw. Γ–H–N–Γ–P–H fuer je einen
  Treffer je Fall, bevorzugt mit Kegel bei 0).
- **Code:** code/qca_diamant.py (Rechnung), code/auswertung.py (Urteile), code/bild.py (Bilder).

## 5. Urteilsregeln (mechanisch in code/auswertung.py)

- **Moegliche Urteile:** "eingetroffen", "nicht eingetroffen", "nicht auswertbar".
- **Vorbedingungen fuer alle:** alle Laeufe rc = 0 und Modus haupt; T mit 12 Elementen ohne Konsistenzfehler, 2T mit
  24, Kern ±I, Spinor-SO(3)-Abweichung ≤ 1e−12, V(C3)³ = −I (≤ 1e−12), L_2 mit 4, Wirkung auf die Richtungen als
  Permutation; jede Darstellung projektiv geschlossen und unitaer (≤ 1e−12), Kommutator −I genau bei "projektiv",
  +I bei "linear"; Projektor des kovarianten Raums idempotent (≤ 1e−10); Defekt-Codepruefung (Gitter gegen exakt,
  Diamant auch X̂Ŷ gegen Koeffizientenform) ≤ 1e−10; alle Faelle vorhanden (Teil 0: 15, Teil A: 4 × 18,
  Teil B: 2 × 10). Sonst alle Urteile "nicht auswertbar".
- **QD0:** eingetroffen genau dann, wenn (i) BCC s = 2, L2:Pauli mindestens einen Treffer mit Kegel bei 0 hat und
  (ii) Diamant s = 2, Fassung 1, in allen zwoelf Darstellungen keinen Treffer hat. Vermerk: BCC L2:1+chi_x und T:2.
- **QD1:** nicht auswertbar, wenn die Positivkontrolle QD0 (i) fehlt. Eingetroffen genau dann, wenn in Teil A
  (Fassung 1 oder 2, Variante frei oder w0, irgendeine Darstellung) mindestens ein nichttrivialer Treffer einen Kegel
  bei 0 hat (Kegeltest und Kommutatortest). Vermerke: dasselbe nur mit Fassung 1 (= Urteil nach Kartenwortlaut);
  dasselbe nach der Regel vor Rauchlauf 1.
- **QD2:** nicht auswertbar, wenn QD1 nicht eingetroffen ist. Eingetroffen genau dann, wenn jeder QD1-Treffer die
  Wirkung "projektiv" hat. Vermerke: nur Variante frei; nur Fassung 1 (Kartenwortlaut); nach der Regel vor
  Rauchlauf 1; Zaehlung projektiv, linear, mehrdeutig je Fall.
- **QD3:** nicht auswertbar, wenn QD0 (i) fehlt. Eingetroffen genau dann, wenn in Teil B (Variante frei oder w0)
  mindestens ein nichttrivialer Treffer einen Kegel bei 0 hat oder die Entartungssuche bei einem der untersuchten
  Treffer (die ersten drei nichttrivialen je Fall) einen Kegelpunkt findet. Vermerk: nach der Regel vor Rauchlauf 1.
- **Beschreibend, ohne Urteil:** Dimensionen, Defektminima, Kegeltypen, Geschwindigkeiten, Isotropie, Verdoppler,
  C3-Implementierbarkeit, Gleichwertigkeitskontrollen (1'+3 gegen 1+3, 2+2'' gegen 2+2', drei L_2-Klassen mit drei
  Charakteren).
- Grenze: Eine Suche mit 100 Starts ist kein Beweis. Die Nullbefunde in Teil A stuetzt D2; in Teil B stuetzt nur D1
  die eindimensionalen Faelle.

## 6. Laufplan

- Rauch (10 Starts) vor dem Einfrieren: Teil 0, Teil A (vier Laeufe oder weniger), Teil B, Bild, Auswertung; Zeiten
  bestimmen die Aufteilung der Hauptlaeufe (je Starteraufruf < 600 s).
- Haupt (Teil 0 und B 100 Starts je Fall, Teil A 40), je ein Starteraufruf, Laufzeiten aus Rauchlauf 1
  hochgerechnet (alle < 600 s):
  - cpu5: H-Ba (Teil B frei: fuenf eindimensionale Faelle, T:2+2, T:1+3), H-Bc (Teil B frei: T:2+2''), H-A1f
    (Fassung 1 frei), H-A2f (Fassung 2 frei), H-A2w (Fassung 2 w0), H-0 (Teil 0)
  - p4000b: H-Bb (Teil B frei: T:1'+3, T:2+2'), H-Bw (Teil B w0, alle), H-A1w (Fassung 1 w0)
  - danach ueber den Starter: bild.py (alle Laeufe) und auswertung.py (alle Laeufe; die Teil-B-frei-Laeufe werden
    zusammengefuehrt).
  - Spuren cpu5 und p4000b, hoechstens zwei zugleich, jeder Lauf mit eigenem ssh-Aufruf.
- Faellt ein Lauf aus (rc ≠ 0 oder Zeitabbruch), sind die betroffenen Urteile "nicht auswertbar"; ein zweiter Versuch
  nur bei einem Fehler ausserhalb des Codes, offengelegt.

## 7. Rauchlaeufe [R] (vor dem Einfrieren, offengelegt; Text ab 07:31:35 CEST)

- **Rauch 1** (10 Starts je Fall; 05:17 bis 05:22 UTC, alle rc = 0): Teil 0 7,2 s; A1 frei 61,8 s; A1 w0 116,1 s;
  A2 frei und A2 w0 je etwa 59 s; B frei 94,4 s; B w0 44,8 s.
  - Teil 0: BCC L2:Pauli 2 Treffer, beide mit Kegel bei 0 (v = 0,57735, Verdoppler an H, P, P'); L2:1+chi_x und T:2
    ohne Treffer (0,400 bzw. 2/45); Diamant s = 2 in allen zwoelf Faellen ohne Treffer (12/7 bzw. 4/3, das Doppelte
    der QCA-TETRA-1-Minima, weil hier Ŷ und X̂ zaehlen).
  - Teil A, wie D2 bis D4: Treffer nur fuer T:1+3, T:1'+3, T:2+2', T:2+2'', L2:1+x+y+z und L2:P+P, in beiden
    Fassungen. Frei: Kegel bei 0 nur in Fassung 1 bei L2:P+P (10 von 10, zwei Weyl-Kegel, anisotrop, v 0,18 bis
    1,04 je Zweischritt, projektiv, C3 nicht implementierbar); T:1+3 dreifach mit quadratischer Aufspaltung (Verhaeltnis
    4); T:2+2' zweifach ohne lineare Aufspaltung; L2 regulaer ohne Entartung bei 0; Fassung 2 frei nirgends Kegel.
    w0: Kegel bei 0 in beiden Fassungen fuer alle sechs Faelle mit Loesungen; T:1+3 vierfach mit zwei flachen
    Zweigen, exakt isotrop, linear (Grover-Typ, wie D4).
  - **Teil B:** Treffer fuer T:1+3, T:1'+3, T:2+2', T:2+2'' (frei und w0), keine fuer T:2+2 (kleinster Defekt
    4/45 frei) und die eindimensionalen Summen (12/7).
    - Frei: T:2+2' mit zwei Weyl-Kegeln bei 0, v = 1/3, isotrop, projektiv, C3 implementierbar; T:1+3 mit
      Dreifachpunkt, v 0,50 bis 0,577, linear. Defekt der Treffer nur ~1e−21 (Suche bei 400 Auswertungen).
    - w0: alle Treffer sind (fast) reine Verschiebungen: Gewicht ganz in S_+ oder ganz in S_−, Eigenphasen
      k·h_a (gerade Linien im Bild), Zweige (−1, 1/3, 1/3, 1/3) bei k ∥ (1,1,1).
- **Befund und Regelaenderung nach Rauch 1 (vor dem Einfrieren):**
  - Die Kegelregel aus Abschnitt 4 (erste Fassung) zaehlte das Kreuzen entkoppelter, geradeaus laufender Zustaende
    als Kegel und die reine Verschiebung als nichttrivial. Mit ihr waere QD3 schon durch die w0-Verschiebungen
    eingetroffen. Das ist ein Fehler meiner Definition fuer s = 4, kein Befund.
  - Ergaenzt (beide Ergaenzungen machen die Regel strenger): Trivialitaet auch bei vertauschenden W(k); Kegel nur mit
    nicht vertauschenden Generatoren erster Ordnung (Abschnitt 4). Die Urteile nach der alten Regel stehen als
    Vermerk daneben. Keine Zahlenschwelle der Karte gibt es; 1e−8 und 1e−2 sind neu und mit Rauch 2 geeicht: echte
    Kegel haben Kommutatorwerte 0,4 bis 2,2, die w0-Verschiebungen 3e−6 bis 1e−5.
  - Nachpolitur eingefuehrt (Abschnitt 4), weil Teil-B-Treffer bei ~1e−21 stehen blieben.
  - Weiter ergaenzt: Chiralitaet, Gewicht S_+/S_−, Zusammenfuehren aufgeteilter Laeufe in auswertung.py und bild.py.
- **Rauch 2** (05:27 bis 05:30 UTC, rc = 0; B frei 96,6 s, B w0 46,1 s, A1 w0 mit 5 Starts 65,3 s):
  - Nachpolitur: alle B-frei-Treffer gehen von ~1e−21 auf 1e−30 bis 4e−30, sind also echte Loesungen.
  - B frei: alle Treffer sind "Muenze mal Verschiebung" (Gewicht ganz in S_+ oder S_−, W(k) = C·S_±(k) bis auf
    Konjugation) mit echter Kopplung (Kommutatorwert 0,9 bis 2,1); T:2+2' zwei isotrope Weyl-Kegel mit v = 1/3,
    C3 implementierbar, projektiv; Verdoppler an H, P, P' (Kegelpunkte).
  - B w0: alle Treffer jetzt "Entartung bei 0 ohne Kegel" (Kommutatorwert ~4e−6).
  - A1 w0: alle Kegel bleiben Kegel (Kommutatorwert 0,4 bis 1,9).
- **Rauch 3** (05:30 UTC, rc = 0): Teil 0 mit Endcode (Chiralitaet des BCC-Weyl-Kegels 0,19245 = (1/√3)³), bild.py und
  auswertung.py liefen ueber den Starter (Urteile "nicht auswertbar", weil Modus rauch).
- **Rauch 4** (05:32 bis 05:33 UTC, rc = 0): Fallauswahl per Index (--faelle idx:...; Namen mit Apostroph lassen
  sich ueber ssh schlecht uebergeben), Zusammenfuehren aufgeteilter Teil-B-Laeufe in auswertung.py und bild.py.
- **Wirkung auf die Vorhersagen:**
  - QD0, QD1 und QD2 sind wie am Schreibtisch ableitbar (Abschnitt 3); die Rauchlaeufe bestaetigen D2 bis D4.
  - **QD3 ist im Rauchlauf gesehen [R]:** Teil B frei hat T-kovariante Treffer mit echten Kegeln. Schreibtisch
    nachtraeglich [M, nach dem Rauchlauf]: Fuer monomiales V (Ind λ von C_3) ist W(k) = C·diag(e^{ik·h_a}) mit C im
    Kommutanten unitaer und T-kovariant (Beweis wie D3, nur ein Halbschritt). Auf der isotypischen Komponente 2 ist
    die erste Ordnung die Kompression des Vektoroperators diag(k·h_a), unter T zwingend c·k·σ: ein isotroper
    Weyl-Kegel, sobald c ≠ 0. Die Rechnung zeigt c = 1/3. Anders als auf dem Diamant hebt sich hier nichts weg, weil
    es keinen Rueckschritt gibt.
  - Hauptlaeufe aendern daran voraussichtlich nichts; sie liefern Zahlen, Kontrollen und Bilder.

## 8. Einfrieren

- Eingefroren 2026-10-04 07:33:24 CEST (date): PLAN.md.eingefroren-20261004-073324, Code mit derselben Endung,
  Pruefsummen in EINGEFROREN-SHA256.txt. Danach keine Aenderung an Plan und Urteilsregeln; Code nur bei echten
  Fehlern, offengelegt.
