# QCA-DIRAC-T-1: Plan des Code-Agenten (Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 08:04:01 CEST (date). Gelesen ab 08:04: KARTE.md,
  qca-diamant-4 (PLAN.md, ERGEBNIS.md, KARTE.md, code/), qca-tetra-1 (PLAN.md, ERGEBNIS.md), RUNDE-38.md (Ernte
  QCA-DIAMANT-4), v3-README, kleintest.sh; Quelle S. 5 bis 6 (lokale PDF-Kopie, ab 08:20).
- Code ab 08:27, Rauchlauf 1 um 06:31 UTC (08:31 CEST), Plantext ab 08:35:50 CEST (date). Der Schreibtisch (Abschnitt 3)
  stand vor Rauchlauf 1 fest; aufgeschrieben ist er erst hier. Was die Rauchlaeufe zeigten, steht in Abschnitt 7.
- Rechnungen nur auf der .69 in /home/fmh/fmhc-physics-remote/runde38-qca-dirac/ (code/, rauch/, lauf/), Start nur
  ueber kleintest.sh, Spuren cpu5 und p4000b, hoechstens zwei Laeufe zugleich. Reine CPU-Rechnung (numpy, scipy,
  matplotlib).
- **Kennzeichen:**
  - [S] an der Quelle gelesen: D'Ariano/Perinotti, PRA 90, 062106 (2014), arXiv:1306.1934v2. Lokale Kopie
    qca-tetra-1/quelle/, S. 5 bis 6 als Bild gelesen; kein Netzabruf (0 von 2).
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher
  - [M] eigene Mathematik (Schreibtisch)
  - [F] Festlegung dieses Plans (die Karte laesst es offen)
  - [H] Hypothese; [R] im Rauchlauf gesehen (vor dem Einfrieren)
- Vorhersagen QM-D0 bis QM-D3, Wahrscheinlichkeiten und die Schwelle 1e-3 (Kruemmung) stehen unveraendert auf der Karte.
  Hier stehen Modell, Messvorschrift und Urteilsregeln.

## 0. Quelle [S] und Uebernommenes

- **Dirac-Automat, Eq. (35) und (36), S. 5 bis 6:** "In this section we find the only two automata that can be
  obtained by locally coupling Weyl automata." Ansatz Ã'_k = ((x F̃_k, y B), (z C, t D̃_k)), "Locality of the coupling
  requires the off-diagonal blocks B and C to be independent of k". Ergebnis Eq. (36):
  Ẽ^±_k = ((n Ã^±_k, i m I), (i m I, n Ã^{±†}_k)) mit n² + m² = 1.
  - Die Masse ist also ein Vor-Ort-Term (k-unabhaengig), die Kopplung verbindet Ã mit Ã^†.
- **Eq. (37):** ω^{E±}_k = arccos[√(1 − m²)(c_x c_y c_z ∓ s_x s_y s_z)], c_i = cos(k_i/√3), s_i = sin(k_i/√3).
  - Folge [M]: bei k = 0 die Eigenphasen ±arccos(n) = ±arcsin(m), je zweifach; Luecke 2 arcsin(m) (= 2m nur in erster
    Ordnung). Kruemmung: cos ω = n d_k, d_k = 1 − k²/6 + O(k³), also ∂²ω/∂k² = n/(3m) in jeder Richtung; der k³-Term
    ist ungerade und faellt in der symmetrischen Differenz heraus.
- **Eq. (38):** Ẽ = I d^E − i γ⁰ γ^± · a^E + i m γ⁰ mit d^E = n d^A, a^E = n a^A (beschreibend).
- Weyl-Automaten Eq. (24), L_2-Kovarianz mit {I, iσ_x, iσ_y, iσ_z}, Eq. (5) und (19): Lesung aus QCA-TETRA-1.
- Aus QCA-DIAMANT-4 (ERGEBNIS.md, Teil B):
  - T-kovariante 4-Zustands-Automaten auf BCC: "Muenze mal Tetraederverschiebung" W(k) = C·S_+(k),
    S_+(k) = Σ_a e^{ik·h_a}|p_a⟩⟨p_a| in der monomialen Basis von 2+2' = Ind χ (Stabilisator C_3), C im Kommutanten.
  - Auf 2 und 2' je ein isotroper Weyl-Kegel mit v = 1/3 (Spurformel), Chiralitaeten entgegengesetzt.
  - Code-Grundlage: Gruppen T/2T, kovarianter Unterraum, exakte Defektformel, Einordnung (qca_diamant.py).

## 1. Kartenpruefung und Festlegungen (vor dem Einfrieren offengelegt)

1. **"2+2'+2+2' oder 2+2+2'+2'" (kleiner Kartenfehler):** Das ist dieselbe Darstellung; die Reihenfolge der Summanden
   ist gleichgueltig. Gerechnet als eine Klasse K4.
2. **QM-D0, "Luecke 2m (bzw. nach Quelle)" [F]:** geurteilt nach Quelle, 2 arcsin(m). Woertlich 2m stimmt nur in erster
   Ordnung: relativ (arcsin(m) − m)/m ≈ m²/6, bei m = 0,1 schon 1,7e−3. Die woertliche Lesung steht als Vermerk.
   Massen m = 0,1; 0,3; 0,6 [F], beide Automaten E^+ und E^−.
3. **QM-D1, Formen [F]:** Kartenwortlaut "alle Muenzen bzw. Sprungformen aus QCA-DIAMANT-4 Teil B" heisst: acht
   BCC-Spruenge ohne Vor-Ort-Term, Variante frei (Form N) und mit W(0) = I (Form N-w0). Haupturteil mit diesen beiden.
   Erweitert (Vermerk): Form O mit Vor-Ort-Term, wie im Dirac-Automaten der Quelle.
4. **QM-D2, "Luecke bei k = 0 (massiv)" [F]:**
   - Die Quasienergie ist nur bis auf eine globale Phase bestimmt. Ich messe die Luecke phasenfrei: Fuer jedes Cluster
     von W(0) (Eigenphasen naeher als 1e−7) den halben Kreisabstand zum naechsten anderen Cluster; "Luecke" ist das
     Minimum. Beim Quell-Dirac-Automaten ist das arcsin(m) = |ω(0)| der Quelle (Hinweis der Leitung: abs(ω(0)) > 1e−3).
   - Massiv heisst: nichttrivial, jedes Cluster bei k = 0 genau zweifach, jedes ohne lineare Aufspaltung ("quadratisch",
     Abschnitt 4), Luecke > 1e−3. Damit gibt es bei k = 0 keinen Kegel; die Baender haben dort Kanten der Form
     ω ≈ ω_c + κ k²/2, wie bei ω² = m² + v²k². Ein Kegel bei k = 0 (auch an einer Bandkante) zaehlt als masselos.
   - Spin 1/2 (360 Grad = −1), "Produkt der Darstellungsmatrizen": fuer jedes Cluster mit Projektor P gilt
     P V(C2x)² P = −P, P V(C3)³ P = −P und P K P = −P, K = V(C2x)V(C2y)V(C2x)^†V(C2y)^† (je ≤ 1e−10; V mit den
     2T-Lifts). Beschreibend dazu die implementierenden Unitaeren aus dem Treffer selbst (wie QCA-DIAMANT-4).
   - Kandidaten: Suchtreffer (Teil B, Formen N, O, P) und die Konstruktionen aus Abschnitt 3 (S3). "Es gibt einen
     Automaten" ist eine Existenzaussage; eine geprueft unitaere und kovariante Konstruktion genuegt. Vermerke: nur
     Suche; nur Suche ohne Inversionsbedingung.
5. **QM-D3, "Richtungsstreuung der Kruemmung" [F]:** je Cluster und je sortiertem Zweig κ(k̂) = 2D(h) − D(2h),
   D(h) = [ω(hk̂) + ω(−hk̂) − 2ω(0)]/h², h = 1e−4 (k-Einheiten, Gitterschritt |h_a| = 1), 400 Fibonacci-Richtungen.
   Richardson, weil die sortierten Zweige einen Fehler erster Ordnung in h haben koennen (Spinaufspaltung ∝ |k|³).
   Streuung = Standardabweichung / |Mittel|; isotrop, wenn das Maximum ueber alle Zweige und Cluster ≤ 1e−3 ist
   (Schwelle der Karte). QM-D3 ist wie QM-D2 eine Existenzaussage: eingetroffen, wenn ein QM-D2-Kandidat isotrop ist.
6. **Bedeutungsabsatz der Karte:** "QM-D2 verfehlt: Masse braucht einen Bruch der Tetraeder-Symmetrie". Am Schreibtisch
   (S3, S4) zeigt sich eine dritte Moeglichkeit: Masse ohne Bruch von T, aber mit einer zusaetzlichen Inversion
   (Paritaet) oder einer abgestimmten Muenze. Das berichte ich beschreibend.

## 2. Darstellungsliste (8 Dimensionen) [M]

- Spinor-Irreps von 2T: 2, 2' = 2 ⊗ 1', 2'' = 2 ⊗ 1''. In der Konjugation zaehlt nur V bis auf ⊗χ; ⊗1' vertauscht
  zyklisch 2 → 2' → 2'' → 2. Komplexe Konjugation tauscht 2' und 2'' (Loesungen gehen in Loesungen ueber, k → −k).
- 8-dim Spinordarstellungen (n_2, n_2', n_2'') mit Summe 4, bis auf zyklische Verschiebung fuenf Klassen:
  - K1 = 2+2+2+2 (4,0,0)
  - K2 = 2+2+2+2' (3,1,0)
  - K3 = 2+2+2+2'' (3,0,1), Gleichwertigkeitskontrolle zu K2 (komplexe Konjugation)
  - K4 = 2+2+2'+2' (2,2,0)
  - K5 = 2+2+2'+2'' (2,1,1)
- Gemischte Summen (linear plus Spinor) sind keine projektiven Darstellungen von T. Als Darstellungen von 2T gelesen,
  erzwingt V(−1) = diag(I, −I) Blockdiagonalitaet: Das sind direkte Summen eines linearen und eines Spinor-Automaten
  mit je 4 Zustaenden, schon in QCA-DIAMANT-4 gerechnet; nicht gerechnet. Rein lineare 8-dim Summen sind kein Spin 1/2;
  nicht gerechnet.
- Teil A: T:2+2 (s = 4); Suchkontrolle T:2+2' (s = 4); Quelle: L2 mit Pauli ⊕ Pauli (s = 4).

## 3. Schreibtisch [M] (vor Rauchlauf 1)

- **S1 (Massenterm, Schur):**
  - Ein Massenterm ist eine k-unabhaengige (Vor-Ort-)Kopplung zwischen zwei Sektoren. T-Invarianz verlangt V M = M V,
    also nach Schur eine Abbildung zwischen aequivalenten Irreps. Zwischen 2 und 2' gibt es keine (QCA-DIAMANT-4).
  - Mit 8 Zustaenden enthaelt jede Spinorzerlegung eine Irrep mindestens zweimal (vier Summanden, drei Sorten). In allen
    fuenf Klassen ist ein Schur-Massenterm erlaubt.
  - Ob die beiden gleichen Irreps Weyl-Kegel entgegengesetzter Chiralitaet tragen, entscheidet der Automat. Beispiel:
    K4 als (2+2')_{S+} ⊕ (2+2')_{S−}: auf beiden 2-Kopien Kegel mit entgegengesetzter Chiralitaet, Kopplung erlaubt.
- **S2 (Satz: keine Spruenge bei r Kopien derselben Spinor-Irrep):**
  - V = U ⊗ I_r (U Spinor-Irrep 2, r beliebig). Mit den 8 BCC-Spruengen und wahlweise einem Vor-Ort-Term I ⊗ γ hat
    kein T-kovarianter unitaerer Automat Spruenge ≠ 0.
  - Beweis: Der Stabilisator C_3 von h_1 erzwingt A_{±h_i} = I ⊗ α^± + (n_i·σ) ⊗ β^± (n_i = t_i/√3,
    α^±, β^± ∈ M_r). Die Fourier-Koeffizienten von W^†W und WW^† zu d = h_i − h_j, 2h_i und h_i + h_j enthalten keinen
    Vor-Ort-Beitrag. Mit n_i·n_j = −1/3 und der linearen Unabhaengigkeit von I, n_i·σ, n_j·σ, (n_i × n_j)·σ folgen:
    - (E1) α^{+†}α^+ + α^{−†}α^− = (1/3)(β^{+†}β^+ + β^{−†}β^−)
    - (E2) α^{+†}β^+ + β^{−†}α^− = 0
    - (E4) β^{+†}β^+ = β^{−†}β^− =: P
    - (F1) α^{−†}α^+ = −β^{−†}β^+
    - (F2) α^{−†}β^+ + β^{−†}α^+ = 0
    - (G1) β^{−†}β^+ ist antihermitesch
    - dazu die WW^†-Fassungen, darunter β^+β^{+†} = β^−β^{−†}
  - Fall P invertierbar: Polarzerlegung und Eichung mit I ⊗ T (links, im Kommutanten) geben β^+ = p > 0 und β^− = v p.
    Dabei ist v unitaer und antihermitesch (v² = −I), und v vertauscht mit p (aus der WW^†-Fassung von E4). E2 und F2
    ergeben α^+ und α^− vertauschen mit v.
  - Aus F1 folgt X² = I fuer X = p^{−1/2}α^+p^{−1/2}. E1 wird zu Tr(p(Y^†Y + YY^†)) = (2/3) Tr p mit der Involution
    Y = p^{1/2}Xp^{−1/2}.
  - Fuer jede Involution gilt Y^†Y + YY^† ≥ 2I: in 2×2-Bloecken mit Spur 0 ist das (2|a|² + |b|² + |c|²)I ≥ 2|a² + bc|·I
    = 2I. Also 2 Tr p ≤ (2/3) Tr p, Widerspruch.
  - Fall P singulaer: Alle Spruenge verschwinden auf C² ⊗ ker P (aus E1 und E4), dort wirkt nur I ⊗ γ, konstant. Die
    Unitaritaet trennt dann einen Automaten auf C² ⊗ supp P ab, mit derselben Struktur und invertierbarem P.
    Widerspruch wie oben; P = 0 heisst keine Spruenge.
  - Folge: T:2+2 mit 4 Zustaenden hat keinen nichttrivialen Automaten, weder mit noch ohne Vor-Ort-Term (mit ihm nur
    W = I ⊗ γ konstant). Ebenso K1 = 2+2+2+2 mit 8 Zustaenden. QCA-TETRA-1 M2 (T:2, s = 2) ist der Fall r = 1. Die
    Defektminima 4/45 (T:2+2) und 2/45 (T:2) aus QCA-DIAMANT-4 und QCA-TETRA-1 passen dazu.
- **S3 (Konstruktion massiver T-kovarianter Automaten, K4):**
  - **(a) Quellform:** A(k) = C·S_+(k) (4 Zustaende, 2+2', QCA-DIAMANT-4) und
    E(k) = ((n A(k), i m I), (i m I, n A(k)^†)) wie Eq. (36), V = (2+2') ⊕ (2+2').
    - E ist unitaer (A A^† = I) und T-kovariant: A und A^† sind kovariant, i m I vertauscht mit V ⊕ V. V ist eine
      Spinordarstellung.
    - Da A und A^† vertauschen, zerfaellt E in 2×2-Bloecke ((n e^{iθ}, i m), (i m, n e^{−iθ})); also cos ω = n cos θ,
      e^{iθ} die Eigenwerte von A(k).
    - C = e^{iα}P_2 + e^{iβ}P_2'. Bei k = 0: θ = α auf 2, β auf 2'. Nahe k = 0 gilt θ = α ± |k|/3 + O(k²).
    - Fuer α ∈ {0, π}: cos ω = ±n cos(|k|/3 + O(k²)) haengt von θ² = k²/9 + O(|k|³) ab. Also keine lineare Aufspaltung,
      Luecke arcsin(m) und Kruemmung n/(9m), in jeder Richtung gleich. Anisotropie und Spinaufspaltung erst ab O(|k|³).
    - Fuer α ∉ {0, π} bleibt ein linearer Term ∝ n sin α: Kramers-Weyl-Kegel an der Bandkante.
    - Wahl C = P_2 − P_2' (α = 0, β = π): beide Sektoren massiv (Eigenphasen ±arcsin m und π ± arcsin m), isotrop,
      Spin 1/2. Das ist vorab ein Beispiel fuer QM-D2 und QM-D3. Gerechnet und geprueft wird es in Teil 0 (Konstruktion
      "a_spiegel"); "a_allgemein" ist dieselbe Form mit zufaelligem α, β.
  - **(b) Muenze mal Verschiebung ohne Vor-Ort-Term:** W(k) = (N ⊗ C)·diag(S_+(k), S_−(k)), N = ((n, i m), (i m, n)) auf
    den Kopien, C = P_2 − P_2'. Bei k = 0 sind die Eigenvektoren von N ausgeglichen (|a| = |b|), die linearen Terme
    ±(1/3)k·σ der beiden Kopien heben sich auf: massiv. Ueber die Isotropie sage ich vorab nichts (S5).
- **S4 (Wann ist eine Kante quadratisch?):**
  - Bei k = 0 vertauscht W(0) mit V, die Cluster sind 2T-Multipletts; fuer Spinor-V sind sie mindestens zweifach.
  - Auf einer zweidimensionalen Irrep ist die erste Ordnung zwingend c k·σ (Hom_T(3, End 2) eindimensional). T verbietet
    c ≠ 0 nicht. Unter T allein ist also jede Kante bei k = 0 generisch ein Kramers-Weyl-Kegel; c = 0 ist eine
    Bedingung der Kodimension 1 je Cluster [M; generisch: H].
  - Eine Inversion Π (unitaer, ΠV = VΠ, Π W(k) Π^† = W(−k)) erzwingt c = 0: Auf dem Cluster wirkt Π skalar, und
    Π H(k) Π = −H(k). Beide Konstruktionen aus S3 (C = P_2 − P_2') haben eine solche Inversion: (a) mit
    Γ = σ_x ⊗ C, (b) mit Γ = σ_x ⊗ I (Kopientausch).
  - Folge [H]: Suchtreffer der Form O (nur T) sind generisch Kegel bei 0. Mit Inversion (Form P) sind die Kanten
    quadratisch.
- **S5 (zweite Ordnung):** Auf einer 2-dim Spinor-Irrep erlaubt T neben a k² I einen Term b Q·σ mit
  Q = (k_y k_z, k_z k_x, k_x k_y). Q transformiert unter T wie ein Vektor und ist gerade unter k → −k; auch die Inversion
  verbietet ihn also nicht. Er spaltet die Kante in zweiter Ordnung richtungsabhaengig. In (a) ist b = 0 (Spektrum ueber
  θ²). Fuer (b) und generische Treffer der Form P erwarte ich b ≠ 0, also anisotrope Kruemmung [H].
- **Folge fuer die Vorhersagen:**
  - **QM-D0:** vorab ableitbar eingetroffen (Eq. 37 [S], Ableitung oben). Geprueft werden Nachbau und Messcode.
  - **QM-D1:** vorab ableitbar eingetroffen (S2). Die Suche (≥ 200 Starts je Form) kann den Beweis widerlegen.
  - **QM-D2 und QM-D3:** vorab ableitbar eingetroffen durch die Konstruktion (a) mit C = P_2 − P_2', wenn ihr Nachbau die
    Pruefungen besteht. Offen und gerechnet: ob die Suche (ohne Konstruktion) massive Treffer findet und wie
    verbreitet Masse und Isotropie unter T allein, unter T mit Inversion und ohne Vor-Ort-Term sind.

## 4. Rechenweg

- **Gitter, Gruppen, Darstellungen:** wie QCA-DIAMANT-4 (t_a, u = k/√3, T aus C2x und R3 mit 2T-Lifts U(C2x) = −iσ_x,
  U(R3) = (I − i(σ_x + σ_y + σ_z))/2). V = ⊕ ω^{n q(g)} U(g) je Summand 2^{(n)}. Pruefungen je Lauf: T mit 12 Elementen,
  2T mit 24, Kern ±I, U(C2x)² = −I, U(R3)³ = −I, jede Darstellung unitaer und projektiv geschlossen, Kommutator −I.
- **Formen (Slots):**
  - N: 8 Spruenge (S_+ und S_−), wie QCA-DIAMANT-4 Teil B
  - O: N plus Vor-Ort-Term A_0, wie Eq. (35) der Quelle
  - P: O plus Inversion: Π A_h Π^† = A_{−h}, Π A_0 Π^† = A_0, mit Π = Kopientausch der doppelten Irreps (K4: beide
    Paare; K5: das 2-Paar, Identitaet auf 2' und 2''). Nur K4 und K5.
  - Teil A zusaetzlich N-w0 (Σ A_h = I).
- **Suche:** kovarianter Unterraum (Gruppenmittel, bei P ueber T × {1, Π}), Orthonormalbasis E_j, A = Σ x_j E_j.
  - Residuen: Koeffizienten R_d von W^†W − I fuer je eine Differenz d je Bahn unter T × {±1}, gewichtet mit
    √(Bahnlaenge). Fuer kovariante A ist das genau der volle Defekt (||R_gd|| = ||R_d||, R_{−d} = R_d^†).
  - Codepruefung in jedem Lauf: gegen alle Differenzen (Unit aus QCA-DIAMANT-4), relativ ≤ 1e−10; Jacobi-Matrix gegen
    Differenzenquotient ≤ 1e−4.
  - Loeser: eigenes Levenberg-Marquardt (Normalgleichungen, Marquardt-Skalierung), hoechstens 300 Iterationen, Abbruch
    bei D < 1e−30 oder Stillstand (relativ < 1e−9 ueber 40 Iterationen ab Iteration 61). Startwerte komplex gaussisch,
    ||x||² = s.
  - Nachpolitur: Treffer mit 1e−28 < D < 1e−10 mit 30 Gauss-Newton-Schritten. Treffer: D < 1e−10. Gueltig fuer die
    Urteile nur mit vollem Defekt D_voll < 1e−10 und Kovarianzabweichung ≤ 1e−10.
  - Saat 39·10000 + Teilcode (Rauch 3900·10000 + ...).
- **Einordnung je Treffer** (W(k) = Σ_f e^{iu·f} A_f, u = k/√3, f ganzzahlige t-Vektoren oder 0, wie QCA-DIAMANT-4):
  - trivial: Sprunggewicht Σ_{h≠0}||A_h||² < 1e−10 (nur Vor-Ort-Term), oder vertauschende W(k) (≤ 1e−8, sechs
    Zufallspaare), oder konstantes relatives Spektrum (Spannweite < 1e−8, Gitter 12³)
  - Cluster von W(0) aus der Schur-Zerlegung (Phasenabstand < 1e−7)
  - erste Ordnung exakt: G_j = Q^† W(0)^† ∂W/∂k_j Q / i, halbe Spreizung der Eigenwerte von Σ n_j G_j ueber 126
    Richtungen. "linear", wenn das Minimum > 1e−6 ist; "quadratisch", wenn das Maximum ≤ 1e−6 ist; sonst "gemischt".
    Dazu Kommutatorwert und Chiralitaet det(tr(G_i σ_j)/2) wie QCA-DIAMANT-4.
  - Klassen: trivial; massiv (Abschnitt 1.4); "Kegel bei 0" (ein Cluster linear); sonst
  - Kruemmung (Abschnitt 1.5) fuer quadratische Cluster; Spin-1/2-Pruefung je Cluster (Abschnitt 1.4)
  - am Treffer (beschreibend): implementierende Unitaere fuer C2x, C2y, C3 und fuer die Inversion h → −h (Nullraum,
    kleinster Singulaerwert ≤ 1e−8)
  - Verdoppler (beschreibend): Cluster und lineare Aufspaltung an H, P, P' (T-invariante Punkte)
- **Teil 0:**
  - Quell-Dirac E^± (Eq. 24 und 36), m = 0,1; 0,3; 0,6: Unitaritaet (Koeffizienten, Gitter 16³), L_2-Kovarianz,
    Einordnung, Soll-Kruemmung n/(3m), Lesepruefung Eq. (37) an 50 Zufalls-k (beschreibend)
  - Suchkontrolle T:2+2' (s = 4, Form N, 40 Starts): QCA-DIAMANT-4 mit dem neuen Loeser wiederfinden
  - Konstruktionen (S3) bei denselben drei m: a_spiegel, a_allgemein (zufaelliges α, β), b_muenze_verschiebung;
    Unitaritaet, T-Kovarianz, Einordnung
- **Bilder:**
  - lauf-69/treffer_je_zerlegung.png: Treffer je Zerlegung und Form nach Klassen, kleinster Defekt; Teil A und
    Suchkontrolle
  - lauf-69/omega_hochsymmetrie.png: Eigenphasen laengs Γ–H–N–Γ–P–H fuer Quelle, Konstruktionen und je einen Treffer
    je Fall (bevorzugt massiv); Cluster bei Γ schwarz, kleinster Abstand rot (Luecke)
- **Code:** code/qca_dirac.py (Rechnung), code/auswertung.py (Urteile), code/bild.py (Bilder).

## 5. Urteilsregeln (mechanisch in code/auswertung.py)

- **Moegliche Urteile:** "eingetroffen", "nicht eingetroffen", "nicht auswertbar".
- **Vorbedingungen fuer alle:**
  - alle Laeufe rc = 0 und Modus haupt
  - Gruppenpruefungen (Abschnitt 4) ≤ 1e−12; jede Darstellung unitaer, projektiv geschlossen, K = −I, V(C2x)² = −I,
    V(R3)³ = −I (≤ 1e−12)
  - Codepruefung (Defekt ≤ 1e−10 relativ, Jacobi ≤ 1e−4); Projektoren idempotent (≤ 1e−10)
  - alle Faelle vorhanden: Teil 0, Teil A (N, N-w0, O), Teil B (N und O je K1 bis K5, P fuer K4 und K5)
  - Sonst alle Urteile "nicht auswertbar".
- **QM-D0:** eingetroffen genau dann, wenn fuer E^+ und E^− bei allen drei m gilt:
  - (i) Unitaritaet ≤ 1e−12 (Koeffizienten und Gitter)
  - (ii) genau zwei Cluster bei k = 0, je zweifach, bei −arcsin(m) und +arcsin(m) (≤ 1e−12)
  - (iii) beide quadratisch
  - (iv) Kruemmungsstreuung ≤ 1e−3 in allen Zweigen
  - (v) |κ| weicht von n/(3m) relativ ≤ 1e−3 ab
  - Vermerk: woertlich 2m.
- **Suchkontrolle** (Vorbedingung fuer QM-D1 und fuer die Such-Vermerke von QM-D2): T:2+2' Form N hat mindestens
  einen gueltigen Treffer der Klasse "Kegel bei 0".
- **QM-D1:** nicht auswertbar ohne Suchkontrolle. Eingetroffen genau dann, wenn die Formen N und N-w0 je mindestens
  200 Starts haben und keinen gueltigen nichttrivialen Treffer. Vermerk: Form O (erweitert).
- **QM-D2:** eingetroffen genau dann, wenn mindestens ein Kandidat massiv ist und Spin 1/2 in allen Clustern traegt.
  - Kandidaten: gueltige nichttriviale Suchtreffer aus Teil B oder Konstruktionen aus Teil 0 mit Unitaritaet und
    T-Kovarianz ≤ 1e−12.
  - Vermerke: nur Suche; nur Suche in den Formen N und O (ohne Inversionsbedingung).
- **QM-D3:** nicht auswertbar, wenn QM-D2 nicht eingetroffen ist. Eingetroffen genau dann, wenn mindestens ein
  QM-D2-Kandidat isotrop ist (Streuung ≤ 1e−3 in allen Zweigen aller Cluster). Vermerk: nur Suchtreffer.
- **Beschreibend, ohne Urteil:** Zahlen je Fall und Klasse, Defektminima, Kegelgeschwindigkeiten, Kruemmungen,
  Inversion am Treffer, Verdoppler, Gleichwertigkeit K2 gegen K3, Lesepruefung Eq. (37).
- Grenze: Eine Suche mit 40 Starts je Fall ist kein Beweis. Die Nullbefunde fuer K1 und T:2+2 stuetzt S2.

## 6. Laufplan

- Rauchlaeufe vor dem Einfrieren (Abschnitt 7). Die Laufzeiten bestimmen die Aufteilung; je Starteraufruf < 600 s.
- Haupt, Starts: Teil 0 Suchkontrolle 40; Teil A 200 je Form; Teil B 40 je Fall. Je ein ssh-Aufruf je Starteraufruf,
  hoechstens zwei zugleich. Hochrechnung aus Rauch 2 (Sekunden je Start: N 1,5 bis 2,8; O K1 8,2, O K2/K3 3,3,
  O K4/K5 1,5 bis 2,2; P 1,4 bis 2,3):
  - cpu5: H-BN (Form N, K1 bis K5, etwa 430 s), dann H-BO2 (Form O, K2 und K3, etwa 270 s), dann H-A (Teil A)
  - p4000b: H-BO1 (Form O, K1, etwa 330 s), dann H-BOP (Formen O und P, K4 und K5, etwa 300 s), dann H-0 (Teil 0)
  - danach ueber den Starter bild.py und auswertung.py (alle Laeufe)
- Faellt ein Lauf aus (rc ≠ 0 oder Zeitabbruch), sind die betroffenen Urteile "nicht auswertbar". Einen zweiten Versuch
  gibt es nur bei einem Fehler ausserhalb des Codes, und er wird offengelegt.

## 7. Rauchlaeufe [R] (vor dem Einfrieren, offengelegt; Text ab 08:39:00 CEST)

- **Rauch 1** (06:31 UTC, beide rc = 0; Teil 0 13,9 s, Teil B Form O K1 und K4 mit 3 Starts 36,5 s):
  - Quell-Dirac E^± bei m = 0,1; 0,3; 0,6: Unitaritaet exakt (Koeffizienten 0, Gitter ≤ 1,2e−15), L_2-Kovarianz 0.
    Bei Γ zwei Zweifach-Cluster bei ±arcsin(m), beide quadratisch. Kruemmung n/(3m) bis 1,7e−7 relativ, Streuung
    ≤ 7,7e−8, Spin 1/2. Lesepruefung Eq. (37): E^+ passt zu c c c − s s s, E^− zu c c c + s s s (≤ 4,4e−16), mit
    meiner Konvention e^{+ik·h} (Eq. 16).
  - Konstruktion a_spiegel (C = P_2 − P_2'):
    - massiv, Luecke arcsin(m), Kruemmung ±n/(9m) (1,1055; 0,35331; 0,14815), Streuung ≤ 4,7e−7
    - Spin 1/2, Inversion am Treffer vorhanden
    - Verdoppler: an H quadratisch, an P und P' Vierfach-Kegel (bei ±π/2)
  - a_allgemein (zufaelliges α, β): alle vier Cluster linear (0,15 bis 0,33), also Kegel bei 0.
  - b_muenze_verschiebung: massiv, aber anisotrop (Streuung 4,3e−3 bei m = 0,1; 0,062 bei 0,3; 0,32 bei 0,6); die
    beiden Zweige eines Clusters haben verschiedene Kruemmung.
  - Suchkontrolle T:2+2': 7 von 10 Treffern, alle Kegel bei 0 mit v = 0,33333 (QCA-DIAMANT-4 wiedergefunden).
  - Teil B, Form O: K4 ein Treffer mit vier linearen Clustern (0,33 und 0,14). K1 zwei Treffer, die als "massiv"
    eingeordnet wurden. Sie sind aber reine Vor-Ort-Automaten (Sprunggewicht 1,2e−15, W konstant), ein Fehler meiner
    Trivialitaetsregel und kein Befund.
- **Aenderung nach Rauch 1 (vor dem Einfrieren):** Trivialitaet um "Sprunggewicht < 1e−10" ergaenzt (Abschnitt 4). Die
  Regel wird dadurch strenger; Konstruktionen und echte Treffer haben Sprunggewichte der Groessenordnung 1.
- **Rauch 2** (06:34 bis 06:35 UTC, rc = 0; 3 Starts je Fall; Form N 37,3 s, Formen O und P 72,4 s):
  - Form N: K4 ein Treffer, Kegel bei 0 (vier lineare Cluster, je 1/3). K1, K2, K3, K5 ohne Treffer (kleinster Defekt
    8/45, 0,0889, 0,0889, 5,0e−7).
  - Form O: K1 zwei triviale (Vor-Ort-Term), K2, K3, K4 je ein Treffer mit Kegel bei 0, K5 ohne Treffer (2/45).
  - Form P: K4 ein massiver Treffer, anisotrop (Streuung 0,41), mit Inversion, dazu ein trivialer; K5 ein trivialer.
- **Rauch 3** (06:35 bis 06:38 UTC, rc = 0): Teil A mit 20 Starts je Form: N 0 Treffer (4/45), N-w0 0 Treffer
  (0,0974, wie QCA-DIAMANT-4), O 8 Treffer, alle trivial (nur Vor-Ort-Term, wie S2). Teil 0 mit Endcode; bild.py und
  auswertung.py ueber den Starter (Urteile "nicht auswertbar", weil Modus rauch).
- **Wirkung auf die Vorhersagen:**
  - QM-D0 bis QM-D3 waren am Schreibtisch ableitbar (Abschnitt 3); die Rauchlaeufe bestaetigen S2 bis S4 und den
    Nachbau. Ich habe die Ausgaenge damit vor dem Einfrieren gesehen.
  - Offen fuer die Hauptlaeufe sind nur die beschreibenden Zahlen: wie oft die Suche Kegel, Masse und Isotropie findet.
    Die Vermerke "nur Suche" haengen daran.
  - Keine Schwelle und keine Urteilsregel nach einem Rauchlauf geaendert, ausser der Trivialitaetsregel oben (strenger).

## 8. Einfrieren

- Eingefroren: Zeit und Pruefsummen in EINGEFROREN-SHA256.txt und im Dateinamen PLAN.md.eingefroren-*. Danach keine
  Aenderung an Plan und Urteilsregeln; Code nur bei echten Fehlern, offengelegt.
