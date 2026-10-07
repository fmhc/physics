# INDUZIERT-WILSON-2D: Plan (Code-Agent, Runde 40)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 11:32:47 CEST (date). Zeitbox 120 min, also bis
  13:32 CEST.
- Ablauf (date, CEST; .69-Zeiten in UTC): Schreibtisch W4 ab 11:36, drei Abrufe 11:40:06 bis 11:40:11, Code ab
  11:42:45, Rauchlaeufe ab 09:46:05 UTC, Agenten-Vorhersagen 11:47:21, Plantext ab 11:49:26.
- **Grundlage:** KARTE.md (W0 bis W4, Wahrscheinlichkeiten und Bedeutung unveraendert); INDUZIERT-DIRAC-2D (KARTE,
  PLAN, ERGEBNIS, code eingefroren 20261004-102358, lauf-69/auswertung.json); INDUZIERT-DICHTE-2D-GROB (ERGEBNIS).
- **Kennzeichen:** [M] eigene Mathematik, [S] an der Quelle gelesen (Kopie in quellen/), [L] Literatur aus dem
  Gedaechtnis, [L?] unsicher, [F] Festlegung dieses Plans, [K] Kartenpunkt, [H] Hypothese, [E] hier gerechnet.

## 1. Schreibtisch W4 (vor jeder Rechnung)

Frage der Karte: Gilt abs det'(d + delta) = det'Delta_0 det'Delta_2 mit Delta_2 isospektral zu Delta_0, und folgt
c_KD = -4 in der Normierung der Karte? Normierung: Skalar Gamma_B = +1/2 log det'Delta_0 gibt c = 1; Fermion
Gamma_F = -log abs det' (Grassmann); ein Dirac-Fermion gibt +1.

### 1.1 Hodge-Zerlegung in 2D [M]

- d + delta ist auf Omega^0 + Omega^1 + Omega^2 selbstadjungiert (Hodge-Skalarprodukt), und (d + delta)^2 = Delta_0 +
  Delta_1 + Delta_2 (blockdiagonal).
- zeta-reguliert gilt log abs det'(d + delta) = 1/2 log det'(d + delta)^2 = 1/2 (log det'Delta_0 + log det'Delta_1 +
  log det'Delta_2). Die zeta-Funktionen einer direkten Summe addieren sich; einen multiplikativen Anomalieterm gibt es
  dabei nicht.
- Das Nicht-null-Spektrum von Delta_1 zerfaellt in exakte und koexakte Formen:
  - d bildet Eigenfunktionen von Delta_0 mit lambda != 0 injektiv auf exakte Eigenformen ab (Delta_1 d phi = d Delta_0 phi).
  - delta bildet Eigenformen von Delta_2 mit lambda != 0 injektiv auf koexakte Eigenformen ab.
  - Also log det'Delta_1 = log det'Delta_0 + log det'Delta_2, fuer jede Metrik.
- Die harmonischen Formen (1 + 2 + 1 auf dem Torus) sind genau die Nullmoden und fallen in allen Faktoren heraus.
- **Ergebnis:** abs det'(d + delta) = det'Delta_0 det'Delta_2. Das gilt auch diskret (DEC, Kontrolle K1 des
  Vorgaengers auf 1e-11).

### 1.2 Isospektralitaet [M]

- In 2D ist der Hodge-Stern * : Omega^0 -> Omega^2 eine Isometrie mit Delta_2 * = * Delta_0. Fuer jede Metrik g gilt
  also det'Delta_2(g) = det'Delta_0(g).
- Explizit fuer g = e^(2 sigma) delta: Delta_0 = -e^(-2 sigma) d^2. Auf dem Koeffizienten h von h dx^dy wirkt
  Delta_2 = -d^2 e^(-2 sigma) = e^(2 sigma) Delta_0 e^(-2 sigma). Beide sind aehnlich und haben dieselbe Diagonale des
  Waermeleitungskerns.
- Damit log abs det'(d + delta) = 2 log det'Delta_0 und Gamma_KD = -2 log det'Delta_0 = -4 Gamma_B.

### 1.3 Normierung und Vorzeichen [M]

- Gamma_B = +1/2 log det'Delta_0 gibt c = 1 (Polyakov: Gamma_B'' = P k^2 A, P = -1/(24 pi)).
- Gamma_KD = -4 Gamma_B, also **c_KD = -4**. Der Flaechenfaktor der Nullmode (log A_g) wird mit -4 multipliziert;
  er ist fuer sigma = s cos(k.x) unabhaengig von k und betrifft nur a, nicht c.
- Gegenprobe Dirac: D^2 = nabla* nabla + R/4 (Lichnerowicz). Waermeleitungskoeffizient a_1 = (1/4 pi) tr(R/6 - E):
  Skalar +R/(24 pi), Spinor (Rang 2, E = -R/4) 2 (R/6 - R/4)/(4 pi) = -R/(24 pi). D ist konform kovariant
  (D_(e^(2 sigma) g) = e^(-3 sigma/2) D e^(sigma/2)). Gamma_D = -1/2 log det'D^2 hat deshalb dieselbe lokale Variation
  wie Gamma_B: c = +1, wie im Vorgaenger festgelegt.

### 1.4 Warum nicht c = +2 [M]

- Die naive Summe der Waermeleitungskoeffizienten gibt "2 Dirac-Fermionen":
  - Delta_1 = nabla* nabla + Ric mit Ric = (R/2) g, also tr E = -R und a_1(Delta_1) = (1/4 pi)(-R + R/3) =
    -4 R/(24 pi).
  - Summe a_1(Delta_0) + a_1(Delta_1) + a_1(Delta_2) = (1 - 4 + 1) R/(24 pi) = -2 R/(24 pi). Mit
    Gamma_KD = -1/2 log det'Delta_gesamt ergaebe das c = +2.
- Die Formel delta log det'A = -2 Integral delta sigma a_1(A) gilt aber nur fuer Operatoren mit delta A = -2 delta sigma A
  (oder -2 A delta sigma).
  - Delta_0 und Delta_2 erfuellen das.
  - Delta_1 nicht: Delta_1 = d e^(-2 sigma) delta_flach + delta_flach e^(-2 sigma) d; die Variation steht innen.
- Die exakte Zerlegung 1.1 ersetzt die Formel. Delta_1 traegt effektiv wie 2 Delta_0 bei (+2 R/(24 pi) statt
  -4 R/(24 pi)). Die Waermeleitungssumme +2 ist deshalb kein Gegenargument.

### 1.5 Literatur (3 gezielte Abrufe, 11:40:06 bis 11:40:11 CEST; Kopien in quellen/ mit Textfassung und sha256)

- **[S] Catterall, Laiho, Unmuth-Yockey, arXiv:1810.10626** (quellen/catterall-1810.10626.txt):
  - Z. 128 bis 130: "In flat, four dimensional space-time continuum Kähler-Dirac fermions are equivalent to four
    copies of Dirac fermions, but they differ in the presence of curvature."
  - Z. 303 bis 306: "Eq. (11) is valid in any metric in contrast to the usual Dirac equation. Nevertheless, it is
    guaranteed that in the limit of small curvature Eq. (11) is equivalent to four copies of the Dirac equation."
  - Z. 704 bis 707: Bilinear-Glied "associated with an anomalous breaking of the U (1) symmetry on manifolds with
    non-zero Euler number".
  - Bedeutung: KD = Dirac-Kopien gilt nur flach. Der Text ist 4D; eine 2D-Spuranomalie steht dort nicht.
- **[S] Kausch, hep-th/0003029** (quellen/kausch-hep-th-0003029.txt):
  - Z. 145 bis 152: "where η and ξ are conjugate fermion fields of dimensions 1 and 0, respectively. ... The stress
    tensor for this system has central charge c = −2".
  - Abstract Z. 21 bis 24: "a free two-component fermion field of spin one ... has central charge c = −2".
  - Bedeutung: Ein Paar Grassmann-Felder mit Gewichten (1, 0), also ein "verdrehtes" Dirac-Fermion, hat c = -2.
- **Ginsparg, hep-th/9108028:** abgerufen fuer die bc-Formel c = 1 - 3(2 lambda - 1)^2. In der Textfassung habe ich
  sie nicht gefunden (Formelsatz). Nicht verwendet.
- **Zusammen [M + S]:** Z_KD = det'Delta_0 det'Delta_2 = (det'Delta_0)^2. Das entspricht zwei (1,0)-Systemen (je
  Z = det'Delta_0, Gamma = -2 Gamma_B, c = -2), also c = -4. Das ist die topologische Verdrehung: Formen haben
  ganzzahligen Spin, der zweite Spinorindex dreht mit.
- Nicht gefunden: eine Quelle, die c = -4 fuer das 2D-Kaehler-Dirac-Feld woertlich nennt.

### 1.6 Gegen den Vorgaenger und gegen die Erwartung der Leitung

- Der Vorgaenger ([K1] in INDUZIERT-DIRAC-2D) hat dieselbe Herleitung. Ich finde keinen Fehler: Zerlegung,
  Isospektralitaet, Grassmann-Vorzeichen und Normierung (Skalar = 1) stimmen.
- Feinheiten ohne Folgen fuer c:
  - Nullmoden und Flaechenfaktor betreffen nur a (k-unabhaengig).
  - d - delta (Catterall) statt d + delta: d - delta ist antiselbstadjungiert, die Betraege der Eigenwerte sind
    dieselben.
  - Eine Kopplung "Spinor x flacher Geschmacksindex" waere eine andere Theorie (zwei Dirac-Fermionen, c = 2), nicht
    d + delta auf Formen.
- **Schranke:** Das ist eine Kontinuumsaussage. Auf dem DEC-Netz des Vorgaengers ist der Delta_2-Teil vom Artefakt
  der Leitwerte 1/w_e beherrscht (+48); messbar ist -4 dort nicht.
- **Urteil W4 (Schreibtisch, vor jeder Rechnung): eingetroffen.** Die KD-Beziehung gilt, und c_KD = -4 im Kontinuum in
  der Normierung der Karte. Meine Sicherheit etwa 95 %; die 75 % der Karte bleiben stehen.

## 2. Code [F]

- code/dirac2d.py, dichte2d_grob.py, zufall2d.py, grob_auswertung.py, dirac_auswertung.py: unveraendert aus
  INDUZIERT-DIRAC-2D (eingefroren 20261004-102358; sha256 gleich den dortigen Pruefsummen).
- **code/wilson2d.py (neu):**
  - Netz, Laengen, Skalar und (A) ueber Aufrufe der unveraenderten Funktionen (dg.grundpunkte,
    dg.periodisches_netz, dg.psi, dg.laengen_geo, dg.netz_pruefen, Netz.gamma, dc.dirac_matrix, dc.gamma_dirac),
    in derselben Reihenfolge wie im Vorgaenger.
  - Neu: D_W, Gamma_W, Modi dichte und kontrolle.
- **code/wilson_auswertung.py (neu):** Tor, Bitvergleich W0, Urteile, Ausgleich (Funktionen aus grob_auswertung.py und
  dirac_auswertung.py), Bild.

## 3. Wilson-Operator

### 3.1 Form [F, K1]

- **D_W = D_A + r eps (K x 1_2).**
  - D_A: Bauweise (A) des Vorgaengers (dc.dirac_matrix), reell antisymmetrisch, 2N x 2N.
  - K: Kotangens-Steifigkeit des Skalars aus denselben physikalischen Laengen (K_ij = -w_ij, K_ii = Summe_j w_ij),
    ungeerdet, je Spinorkomponente ("Gewichte von L wie beim Skalar").
  - eps = sqrt(A/N), der mittlere Netzabstand: r ist in Netzabstands-Einheiten gegeben.
- **Warum eps:** D_A skaliert mit der Laenge, K in 2D nicht. Mit eps ist E2 (eps = 2) exakt das skalierte E1-Netz bei
  gleichem r (D_W(E2) = 2 D_W(E1-Form)); die Skalengleichheit des Vorgaengers bleibt. Ohne eps haette E2 effektiv
  r/2. Fuer E1 (eps = 1) ist es woertlich D_A + r L.
- **Kontinuum [M]:** D_A ~ V_i D_g und K ~ V_i (-Delta_g) mit V_i ~ eps^2 (Zahl = Volumen). Also D_W ~ V (D_g +
  r eps (-Delta_g)): Wilson-Glied mit der lokalen physikalischen Gitterweite. Schwere Anteile (Masse ~ r/eps) geben in
  2D nur lokale Glieder (kosmologisches Glied in a, R^2/m^2 in d), kein k^2-Glied [L].
- **Normierung [K2]:** Auf dem Quadratnetz ist K das 5-Punkt-Laplace (Diagonalgewicht 0, Achsengewicht 1). Die Doppler
  bei (pi, 0) bekommen 4 r, der bei (pi, pi) 8 r. Karten-r = 1/2 entspricht dem ueblichen Wilson-Parameter 1.

### 3.2 Vorzeichen und Hermitezitaet [M]

- D_A ist antisymmetrisch (antihermitesch), r eps K symmetrisch und auf dem Grundnetz positiv semidefinit (Delaunay,
  w >= 0).
- Mit eps_s = 1 x i sigma_y (reell, eps_s^2 = -1) gilt eps_s gamma_a eps_s^-1 = -gamma_a, also
  eps_s D_W eps_s^-1 = D_W^T (Gegenstueck zur gamma5-Hermitezitaet). Die Singulaerwerte sind paarweise entartet
  (Kramers; Rauchlauf und K1).
- D_W ist nicht normal. Deshalb Singulaerwerte statt Eigenwerte, wie die Karte (D_W^dagger D_W) verlangt.
- Das Vorzeichen von r ist fuer abs det und die Singulaerwerte gleichgueltig: D_A - r eps K = -(D_A + r eps K)^T.

### 3.3 Gamma_W

- **Gamma_W = -1/2 log det'(D_W^T D_W) = -Summe_(i >= 3) log sigma_i(D_W)**, ohne die zwei kleinsten Singulaerwerte
  (ein Kramers-Paar). Fermion-Konvention wie im Vorgaenger; fuer r -> 0 waere es Gamma_A.

### 3.4 Nullmoden [M, E]

- **s = 0 (Grundnetz):** Aus x^T D_W x = r eps x^T K x = 0 folgt K x = 0, also x konstant. Auf dem flachen Netz ist
  Summe_j w_ij d_ij = 0, also D_A u = 0. Der Kern sind genau die zwei konstanten Spinoren, rechts und links.
  - Exakt (Cauchy-Binet fuer das (2N-2)-te Kompositum): prod' sigma = abs det M_(0) sqrt(det(V^T V) det(W^T W)).
    M_(0) ist D_W ohne die zwei Zeilen und Spalten von Knoten 0; V und W sind die rechten und linken Nullvektoren mit
    v(Knoten 0) = e_k.
- **s != 0:** Die zwei Nullmoden von D_A (bei ungeradem N geschuetzt) hebt das Wilson-Glied auf
  sigma_1 = sigma_2 ~ r eps s^2 k^2/8 an (Rauchlauf: 1e-4 bei k eps = 0,05, 1,6e-2 in E2-Einheiten bei 0,6). Sie
  bleiben vom Rest getrennt (sigma_3 ~ 2 pi/L).
  - Sie sind die Fortsetzung der Kontinuums-Nullmoden e^(-sigma/2) u (Torus, periodisch: fuer jedes sigma zwei) und
    verschwinden fuer s -> 0 und fuer eps -> 0.
  - Konsistent ist deshalb, bei jedem s genau die zwei kleinsten Singulaerwerte wegzulassen. prod_(i >= 3) sigma_i ist
    stetig in s, solange die Luecke zu sigma_3 besteht.
- **Rechnung bei s != 0:**
  - log prod' sigma = log abs det D_W - log(sigma_1 sigma_2), mit LU von D_W (COLAMD).
  - sigma_1, sigma_2 aus Block-Inversiteration (Breite 4, (D_W^T D_W)^-1 mit derselben LU, Start mit den konstanten
    Spinoren) und Rayleigh-Ritz (Singulaerwerte von D_W Q).
  - Abbruch, wenn sich log(sigma_1 sigma_2) um weniger als 1e-13 aendert (mindestens 3, hoechstens 60 Schritte).
- **Nicht gewaehlt:** antiperiodische Raender (ohne Nullmoden). Das waere eine andere Randbedingung als bei (A), und die
  Karte verlangt det'. Im Kontinuum betrifft die Nullmoden-Behandlung nur den k-unabhaengigen Teil a (Normierung
  Integral e^sigma ist unabhaengig von k).
- **Pruefung K1:** Formel gegen dichte Singulaerwerte (N = 151, s = 0 und +-0,5, r = 1, 1/2 und 2): <= 2,3e-13 [E].

## 4. Netze, Saaten, Messgroesse (wie INDUZIERT-DIRAC-2D)

- Torus, sigma = s cos(k.x), Punkte nach physikalischer Flaeche, Neuvernetzung je Verformung (Delaunay in Koordinaten),
  physikalische Laengen (geo), S = 0,5, Richtungen 0 und 90 Grad.
- **E1:** N = 16 001, A = N (eps = 1), n = 1, 2, 4, 6 (k eps = 0,050 / 0,099 / 0,199 / 0,298), Saaten ab 0.
- **E2:** N = 16 001, A = 64 004 (eps = 2), n = 2, 4, 8, 12 (k eps = 0,099 / 0,199 / 0,397 / 0,596), Saaten ab 1000.
- D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2, y = D/A; y_eps = y A/N, x = (k eps)^2.
- **Ausgleich (unveraendert):** y_eps = a + c x + d x^2 gemeinsam ueber E1 und E2. GLS auf den 8 Zellmitteln mit
  freier Kovarianz je Datensatz, Birge-Faktor, Modellprobe chi^2 bei 5 FG. c_eff = c/P, SE = SE_U(c)/abs(P).
- Getrennt fuer B (Skalar), W1 (r = 1), W05 (r = 1/2); gepaart je Saat W05 - W1, W1 - B, W05 - B.
- (A) wird nur auf der ersten Saat jedes Blocks gerechnet (Bitvergleich W0), aus Zeitgruenden [F, K4].

## 5. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| W0 | Kontrolle: Skalar und (A) ohne Wilson auf denselben Saaten bitgleich mit INDUZIERT-DIRAC-2D | 85 % |
| W1 | [H] Wilson r = 1: c_eff im Band [0,7; 1,3] mit SE <= 0,3 | 40 % |
| W2 | [H] Streuung je Saat des Wilson-Fermions hoechstens doppelt so gross wie die des Skalars | 55 % |
| W3 | [H] r = 1/2 und r = 1 stimmen innerhalb 2 SE ueberein | 55 % |
| W4 | Schreibtisch: Die KD-Beziehung gilt, und c_KD = -4 in der Normierung der Karte (Kontinuum) | 75 % |

## 6. Urteilsregeln (mechanisch durch code/wilson_auswertung.py nach lauf-69/auswertung.json)

- **Tor [F]:**
  - Netz: wie im Vorgaenger (eingefrorene Pruefungen aus -GROB, Grundnetz Delaunay, Skalar-LU mit U_ii > 0 und
    perm_r = perm_c, Newton-Residuum <= 1e-12).
  - W (je r): Grundnetz endlich, Nullvektor-Residuen rechts und links <= 1e-8 (relativ). Bildnetze endlich, letzte
    Aenderung von log(sigma_1 sigma_2) <= 1e-10, Luecke sigma_2/sigma_3 <= 0,5.
  - Faellt Tor Netz oder Tor W fuer ein r, sind die Teile mit diesem r nicht auswertbar.
- **Vorbedingungen je Ausgleich:** mindestens 16 Saaten je Datensatz; Modellprobe p >= 0,01.
- **W0:** Bitvergleich gegen INDUZIERT-DIRAC-2D lauf/ (gleiches N, A und Saat).
  - Skalar auf allen Netzen: Gamma(0), Gamma(+S), Gamma(-S), D, y. (A) dieselben Groessen auf den A-Saaten.
  - Eingetroffen: alle Werte gleich (==), keine Zeile fehlt. Nicht eingetroffen: ein Wert verschieden. Sonst nicht
    auswertbar.
- **W1 (Bandregel wie im Vorgaenger):** Band [0,7; 1,3]; die halbe Breite 0,3 ist zugleich die SE-Schwelle der Karte.
  - Eingetroffen: c_eff(W1) im Band und SE <= 0,3.
  - Nicht eingetroffen: Abstand zum Band > 2 SE.
  - Sonst nicht auswertbar. Kartenwortlaut: Punktwert im Band und SE <= 0,3.
- **W2 [K5]:**
  - Q = sqrt(Summe_Zellen var_W1 / Summe_Zellen var_B). var ist die Varianz von y_eps ueber die Saaten je Zelle
    (ddof 1), ueber 8 Zellen (E1 und E2) summiert. SE(Q) per Delete-one-Jackknife ueber alle Saaten.
  - Eingetroffen: Q <= 2 und SE(Q) <= 0,5. Nicht eingetroffen: Q - 2 > 2 SE(Q). Sonst nicht auswertbar.
  - Kartenwortlaut: Q <= 2. Mitberichtet: Q fuer r = 1/2, Verhaeltnis je Zelle, Verhaeltnis der SE(c_eff) W1/B.
- **W3 [K6]:**
  - Delta = c_eff(W05) - c_eff(W1). SE(Delta) aus dem gepaarten Ausgleich der Differenz W05 - W1 je Saat (gleiches
    Modell).
  - Eingetroffen: abs Delta <= 2 SE(Delta) und SE(Delta) <= 0,3. Nicht eingetroffen: abs Delta > 2 SE(Delta). Sonst
    nicht auswertbar. Vorbedingungen fuer W1, W05 und die Differenz.
  - Kartenwortlaut: abs Delta <= 2 sqrt(SE_W1^2 + SE_W05^2) (ungepaart).
- **W4:** Schreibtisch (Abschnitt 1), vor jeder Rechnung: eingetroffen.
- **Bedeutung:** wie auf der Karte vorab festgelegt (W1 und W2 treffen ein / W1 verfehlt mit c_eff > 1,3 / W4 haelt).

## 7. Kontrollen

- **K1:** Gamma_W-Formel gegen dichte Singulaerwerte (N = 151, s = 0 und +-0,5; r = 1, 1/2, 2).
- **K2:** Spektrum nahe null bei s = 0: kleinste Singulaerwerte von D_W fuer r = 0 (= (A)), 1/2 und 1 bei N = 4 001
  und 16 001, gegen das Kontinuum eines Dirac-Fermions (2 pi abs(m)/L, je Impuls zweifach). Frage der Karte: Ist das
  Band angehoben?
- **W0** als Urteil (Bitvergleich).
- **Tor-Kennzahlen:** Luecke sigma_2/sigma_3, Iterationen, groesstes sigma_2, kleinstes sigma_3.

## 8. Beschreibend (kein Urteil)

- je Operator (B, W1, W05 und die gepaarten Differenzen): nur E1, nur E2, mit k^6, a je Datensatz, Fenster
  k eps <= 0,40, nur k^2 im Fenster, Jackknife-SE
- c_eff(k) je Zelle; Saatstreuung, Versatz- und Restanteil
- Bild lauf-69/bild-ck-gegen-k2.png: c_eff(k) gegen (k eps)^2 fuer Skalar, W1, W05 und die Differenz W05 - W1
- nach dem Rauchlauf festgelegt (Abschnitt 11): Ausgleich fuer W1 + 4 B und W05 + 4 B (Kontinuum: 1 + 4 = 5),
  Streuungsverhaeltnis von W1 + 4 B und W05 - W1, Kontrollvariable c_eff(W) = c_eff(W + 4 B) - 4 c_eff(B) mit dem
  Skalar aus allen 96 + 96 Saaten des Vorgaengers (SE ohne Korrelation der beiden Teile)

## 9. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Einheit von r:** Die Karte schreibt D_W = D_A + r L ohne Einheit. Festgelegt: r in Netzabstands-Einheiten
  (Faktor eps, Abschnitt 3.1). Fuer E1 ist das woertlich die Karte.
- **[K2] Normierung:** Karten-r = 1/2 entspricht auf dem Quadratnetz dem ueblichen Wilson-Parameter 1.
- **[K3] Saaten:** dieselben Saaten und Netze wie INDUZIERT-DIRAC-2D (ab 0 bzw. 1000, N = 16 001). Wegen der Zeitbox
  nur ein Teil der dortigen 96 + 96 Saaten (Abschnitt 12).
- **[K4] (A)** nur auf der ersten Saat jedes Blocks; W0 ist also fuer (A) ein Teilvergleich.
- **[K5] W2 "Streuung je Saat":** wie die "Saatstreuung" des Vorgaengers (Standardabweichung von y_eps je Zelle ueber
  Saaten), hier ueber 8 Zellen gepoolt; die SE-Regel ist meine Festlegung.
- **[K6] W3 "innerhalb 2 SE":** im Plan die SE der gepaarten Differenz (beide r auf denselben Netzen); ungepaart als
  Kartenwortlaut.
- **[K7] r bei W2:** Die Karte nennt bei W1 r = 1, bei W2 kein r. Geurteilt mit r = 1; r = 1/2 mitberichtet.

## 10. Agenten-Vorhersagen

Notiert 11:47:21 CEST (date) in AGENT-VORHERSAGEN-ENTWURF.txt, vor jedem y- oder c_eff-Wert eines Wilson-Laufs. Gesehen
waren da schon K1, K2 bei N = 4 001 und die Logzeilen der Rauchsaat 902 (Abschnitt 11).

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| C1 | Tor (Netz, W1, W05) besteht in allen Hauptlaeufen | 85 % |
| C2 | W0: Skalar auf allen Netzen und (A) auf den A-Saaten bitgleich | 95 % |
| C3 | c_eff(W1) Punktwert in [0,7; 1,3] | 60 % |
| C4 | Streuungsverhaeltnis Q(W1) <= 2 (Punktwert) | 55 % |
| C5 | abs(c_eff(W05) - c_eff(W1)) <= 2 SE (gepaart) | 60 % |
| C6 | abs d_eff(W05) > abs d_eff(W1) (schwere Doppler: k^4-Glied ~ 1/r^2) | 60 % |
| C7 | Skalar auf den Saaten dieses Laufs: c_eff(B) Punktwert in [0,6; 1,4] | 70 % |

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC; Rauchsaaten >= 902)

Alle mit der Codefassung dieses Plans (wilson2d.py unveraendert seit dem ersten Start; wilson_auswertung.py einmal vor
der Probe berichtigt, siehe unten).

- **kontrolle** (09:46:05 bis 09:46:20, cpu, rc 0):
  - K1: Formel gegen dichte Singulaerwerte <= 2,3e-13 (N = 151; s = 0, +0,5, -0,5, +0,5; r = 1, 1/2, 2). Bei s = 0
    zwei Singulaerwerte <= 2e-15, danach ein Kramers-Paar bei 0,42 bis 0,57. Bei s = +-0,5 ein Kramers-Paar bei 0,008
    bis 0,010, der Rest ab 0,42.
  - K2 bei N = 4 001 (Saat 993, s = 0): r = 0 (= (A)) zeigt das Band des Vorgaengers (0,00058, 0,00123, 0,00204, ...).
    Mit r = 1 und r = 1/2 liegen die kleinsten von null verschiedenen Singulaerwerte bei 0,0971 bis 0,1010
    (Kontinuum 0,0993, achtfach) und 0,138 bis 0,139 (Kontinuum 0,1405). **Das Band ist angehoben.**
- **dichte-r902-e1** (09:46:07 bis 09:48:14, cpu7, rc 0): E1, Saaten 902 (mit A) und 903. 74,2 s bzw. 52,0 s je Saat.
  sigma_1 = sigma_2 (Kramers) von 1,0e-4 (k eps = 0,05) bis 3,0e-3 (0,3) fuer r = 1; sigma_3 = 0,050 bis 0,060;
  3 bis 9 Iterationen. Nullvektor-Residuen am Grundnetz <= 2,4e-17.
- **dichte-r902-e2** (09:47:14 bis 09:48:47, cpu, rc 0): E2, Saaten 902 und 903 (ohne A), 46,9 s je Saat. Groesste
  Luecke sigma_2/sigma_3 = 0,016/0,117 = 0,14 (n = 12, r = 1).
- **kontrolle-k2-16001** (09:49:23 bis 09:50:46, cpu, rc 0): K2 bei N = 16 001 (Saat 994): r = 0 Band bei 7e-5,
  3,2e-4, 5,1e-4; r = 1: 0,0492 bis 0,0501, r = 1/2: 0,0492 bis 0,0500 (Kontinuum 0,04967, achtfach), danach 0,0696
  bzw. 0,0695 (Kontinuum 0,0703).
- **dichte-r904-e1** (09:49:21 bis 09:53:14, cpu7, rc 0) und **dichte-r905-e2** (09:50:58 bis 09:53:39, cpu, rc 0):
  weitere Rauchsaaten (E1 904 bis 907 mit A auf 904; E2 905 bis 907 mit A auf 905), nur fuer die Probe der Auswertung
  und den Bitvergleich gegen die Rauchdateien des Vorgaengers. 69 bis 77 s je Saat mit A, 44 bis 54 s ohne.
- **Probe der Auswertung** (auswertung-probe, -probe2, -probe3: 09:53:44 bis 09:56:23, cpu, alle rc 0):
  - Probe-Ordner rauch/probe (Kopien meiner Rauchdateien), Vergleich gegen Kopien der Rauchdateien des Vorgaengers
    (rauch/probe-ref: dichte-r903, dichte-r905-e1, dichte-r905-e2 und dessen lauf/auswertung.json).
  - Codepfad, Tor, Bitvergleich und Bild laufen. Bitvergleich: Skalar 165 von 165 (E1) und 99 von 99 (E2) Werten
    gleich, (A) 33 von 33 (E1, Saat 904) und 33 von 33 (E2, Saat 905). W0 dort "nicht auswertbar", weil die
    Saaten 902 und 903 beim Vorgaenger fehlen (so gewollt).
  - Tor bestanden; Luecke sigma_2/sigma_3 hoechstens 0,14; hoechstens 9 Iterationen.
  - Jackknife bei 5 Saaten nicht moeglich (Kovarianz singulaer); bei >= 16 Saaten wie im Vorgaenger.
- **Rauschen (angesehen, Selbstanzeige):**
  - Q(W1) = 4,04 und Q(W05) = 4,11 auf 6 + 5 Rauchsaaten. In E1: Rest 0,0040 gegen 0,00098 und Versatz 0,0117
    gegen 0,0029 (W1 gegen Skalar).
  - Die Kombination W1 + 4 B streut nur 0,10-mal so stark wie der Skalar, W05 - W1 nur 0,18-mal.
  - Lesart [M, H]: Fuer r -> unendlich ist D_W ~ r eps K x 1, also Gamma_W -> -2 log det'K = -4 Gamma_B + konst. Die
    schweren Anteile schwanken wie -4 Skalare.
  - c_eff-Werte habe ich nicht angesehen, weder in der Probe noch im Probe-Bild.
- **Folgen fuer den Plan (vor dem Einfrieren, nicht nach c_eff):**
  - Urteilsregeln W0 bis W3 unveraendert (Text ab 11:49:26, vor der ersten Probe um 11:53).
  - Beschreibend dazu (Abschnitt 8): Ausgleich fuer W1 + 4 B und W05 + 4 B, Streuung von W1 + 4 B und W05 - W1, und die
    Kontrollvariable c_eff(W) = c_eff(W + 4 B) - 4 c_eff(B; 96 + 96 Saaten des Vorgaengers).
  - Erwartung: SE(c_eff(W1)) etwa 4 x SE(Skalar), also 0,5 bis 0,7 bei etwa 64 + 64 Saaten. W1 wird damit
    wahrscheinlich "nicht auswertbar" (SE > 0,3), W2 wahrscheinlich "nicht eingetroffen" (Q ~ 4). Die gepaarte
    Differenz fuer W3 ist dagegen scharf (SE etwa 0,03). Die Karte und C1 bis C7 bleiben unveraendert.
- **Codeaenderungen vor dem Einfrieren:** wilson2d.py ist seit dem ersten Rauchlauf unveraendert. wilson_auswertung.py:
  W0-Logik berichtigt (fehlende Vergleichszeile gibt "nicht auswertbar" statt "nicht eingetroffen", wie in
  Abschnitt 6), dazu die beschreibenden Kombinationen und die Kontrollvariable.

## 12. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde40-induziert-wilson/ (code/, rauch/, lauf/), nur ueber kleintest.sh.
- **Bloecke [F]:** je 8 Saaten, die erste mit (A). Gemessen 69 bis 77 s mit A und 44 bis 54 s ohne, also etwa 450 s
  je Block (Grenze 600 s).
- **cpu:** E1 in Bloecken e1-s0, e1-s8, e1-s16, ... (Saaten 0 bis hoechstens 95).
- **cpu7:** E2 in Bloecken e2-s1000, e2-s1008, ... (Saaten 1000 bis hoechstens 1095).
- Je Spur eine lokale Schleife: ein ssh-Aufruf je Block, nacheinander. Hoechstens zwei ssh-Verbindungen zugleich.
- **Uhrregel [F]:** Ein Block wird nur gestartet, wenn date vor 12:55:00 CEST zeigt. Die Entscheidung haengt nur an der
  Uhr, nicht an Werten. Waehrend der Laeufe sehe ich nur Logzeilen (Singulaerwerte, Zeiten), keine y-Werte.
- **Abbruch:** Jeder Block schreibt nach jeder Saat. Endet ein Block vorzeitig (600 s), wird mit den fertigen Saaten
  geurteilt (offengelegt). Unter 16 Saaten je Datensatz sind W1 bis W3 nicht auswertbar.
- **Danach:** Pruefsummen auf der .69, dann wilson_auswertung.py auswerten lauf lauf/auswertung.json
  /home/fmh/fmhc-physics-remote/runde39-induziert-dirac/lauf (Vorgaenger nur gelesen).
