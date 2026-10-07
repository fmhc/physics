# PUMPE-NETZ-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 46)

- Start 2026-10-05 06:02:29 CEST (date). Plantext ab 06:19:19 CEST (date), vor jeder Rechnung. Zeitbox 150 min, also
  bis 08:32:29 CEST; danach kein neuer Lauf.
- Grundlage: KARTE.md (PN0 bis PN2; Wortlaut, Schwellen, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Werkzeug: code/ew.py, code/tp.py unveraendert aus EINE-WELT-LOCH-1 (sha256 fa7b6417..., 419d7da6...), code/mn.py
  unveraendert aus MATERIE-NETZ-1 (b36984d3...; benutzt werden nur W_of, LP, VCELL). Neu: code/pn.py.
- Kennzeichen: [M] eigene Mathematik (vorab), [E] gerechnet, [P] Projektdatei, [ES] eigener Schluss, [F] Festlegung,
  [H] Hypothese, [L?] Literaturzahl ohne Abruf. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Ableitbarkeitsprobe (vor jeder Rechnung)

### 1.1 Normierung: ein G fuer Takt, Raum und TT [M]

- Regge: Summe_e l_e eps_e entspricht (1/2) Int sqrt(h) R. Mit -S_Regge = (1/2) a^T B a (ew.py) ist das ADM-Potential
  -(1/(16 pi G)) Int sqrt(h) R = (1/(8 pi G)) (1/2) a^T B a. Also **kappa_g = 1/(8 pi G)**; aus dem Ecktakt (GAMMA-NETZ-L)
  **kappa' = kappa_g/2 = 1/(16 pi G)** in V1.
- Newton aus MATERIE-NETZ-1 [P]: weiche Richtung von P = -W^H B W ist 0,2 k^2 (Eigenvektor (1,...,1)/sqrt10), also
  mu(k) = -(kappa_g/kappa'^2) m_Zelle/(2 k^2) (kubische Einheiten). Kontinuum: Phi(k) = -4 pi G_N m_Zelle/(V_Zelle k^2).
  Mit V_Zelle = 1/4 und kappa_g/kappa'^2 = 32 pi G folgt **G_N = G** (kein Zufall: u^H P u = 2 k^2 ist genau die
  Einstein-Hilbert-Steifigkeit der konformen Mode h = 4 phi delta, nachgerechnet).
- TT [P, TT-ISO-1 Abschnitt 5]: affine TT-Welle a_e = n_e^T h n_e (also delta g = 2 h) hat a^H B a = (1/4) k^2 abs(h)^2 je
  Zelle. (kappa_g/2)(1/4) k^2 abs(h)^2 = (1/(64 pi G)) k^2 abs(2h)^2 V_Zelle: **dieselbe Konstante G** wie Einstein-Hilbert.
- Materie mit Hodge-Gewichten [M]: Ich nehme die P1-Form (lineare Elemente je Tetraeder, Gewichte = 3D-Kotangens-Formel
  aus den 6 Kantenlaengen): E_t = (1/2) V_t g_t^-1 : (d phi)(d phi). Je Tetraeder gilt exakt delta E_t = -(1/2) V_t T_t : delta g_t
  mit T = (grad phi)(grad phi) - (1/2) abs(grad phi)^2 1. Die Kantenkraft sigma_e = d E/d a_e ist also genau die
  Einstein-Kopplung -(1/2) T : delta g, eingeschraenkt auf stueckweise flache Metriken. Fuer gleichfoermiges T:
  Summe_e sigma_e n_e n_e^T = -V_Zelle T.
- **Folge [M]:** In der Kontinuumsgrenze ist G_rad/G_N = (1/(8 pi kappa_g))/(kappa_g/(32 pi kappa'^2)) = (2 kappa'/kappa_g)^2
  = gamma^2, in V1 also 1. **PN2 ist damit in der Kontinuumsgrenze vorab ableitbar, aber nur, wenn die innere
  Relaxation des Netzes (nicht-affine Moden bei kleinem k) weder die TT-Steifigkeit noch die Kopplung der Spannung an die
  TT-Mode umnormiert.** Bei kleinem k sind beide Korrekturen von derselben Ordnung k^2 wie die Steifigkeit selbst (die
  affinen Verzerrungen sind bei k = 0 Nullmoden, innere Moden sind steif, die Kopplung ist O(k)). Das ist nicht vorab
  ableitbar; das misst die Rechnung. Ebenso die Gitterabweichung bei endlichem k l.
- **PN1 [M]:** Mit erhaltener Quelle (Abschnitt 3.3) ist die Spannung S = -(omega^2/2) I (I = Energie-Quadrupol). Bei
  endlichem G_rad und linearer Dispersion folgt P ~ omega^2 abs(S)^2 ~ omega^6 abs(I)^2 vorab. Gemessen werden nur die
  Abweichungen durch Gitterdispersion, Relaxation bei endlichem k und Quellgroesse.

### 1.2 K1 und PN0: Kopplung von V1 an TT [M]

- In V1 steht die Quelle nur in der skalaren Regel (kappa' c^H a = m). In R1 ist a = S x + a_c mit a_c = c (c^H c)^-1 m/kappa'
  (S orthogonal zu Bild [M, c]). Die TT-Moden werden nur ueber die Kraft -kappa_g S^H B a_c angetrieben.
- Symmetrie: Fuer k laengs [100] (Kleine Gruppe C4v) und [111] (C3v) ist eine Skalarquelle A1, die TT-Zweige B1/B2 bzw. E.
  Dort ist die Kopplung exakt null, sofern die Quelle selbst die Symmetrie hat. Fuer allgemeine Richtungen bricht das Gitter
  die Drehsymmetrie um k.
- Ordnung: Ist die relaxierte Regge-Hesse-Form bei O(k^2) isotrop (Einstein-Hilbert), koppelt Skalar an TT erst bei O(k^4);
  die Amplitude relativ zur Spannungskopplung ist dann O((k l)^2) (Karte). Bekannt sind nur die TT-TT-Steifigkeit (isotrop
  auf 2,5e-8 [P]) und die konforme Steifigkeit (isotrop auf 1e-7 [P]), **nicht der Kreuzblock Skalar-TT**. Ebenso offen:
  ob die statische V1-Antwort, eine reine Eck-Skalierung W mu (MATERIE-NETZ-1, exakt [P]), auf dem Gitter TT-Anteil hat.
  Damit ist PN0 der Richtung nach (Kontinuum: null) vorab ableitbar, die Gitterordnung nicht.

### 1.3 Bezug: linearisierte Einstein-Theorie (vorab, keine Messung) [M, L]

- c = 1-Einheiten: Zeiteinheit so, dass die TT-Geschwindigkeit bei kleinem k c_0 = 1 ist (die Bewegungsenergie in ew.py ist
  frei normiert; Verhaeltnisse P_Gitter/P_E haengen davon nicht ab).
- Quelle T_ij(x, t) = s_ij(x) cos(omega t), S~(k) = Int s e^(-i k.x) d^3x. Fernfeld h_ij^TT = (4 G/r) Lambda_n[S~(omega n)].
- Leistung: P_E(omega) = (G omega^2/(4 pi)) Int dOmega_n Lambda_n[S~(k n)] : S~(k n)^*, k = omega/c_0.
  Kompakt: P_E = (2 G omega^2/5) abs(S^TF)^2 = (G/10) omega^6 abs(I^TF)^2 (Quadrupolformel, zeitgemittelt).
- Fernfeld-Amplitude (Winkelmittel): r h_rms = 4 sqrt(G P)/omega.
- Statische TT-Kopplung je k: C_E(k) = 4 Lambda_n[S~(k)] : S~(k)^*/k^2 (aus der affinen Steifigkeit 1/4 je Zelle).

### 1.4 Beschreibender Teil, vorab [M, ES]

- **Bewegte Quelle:** In V1 und mit S koppelt keine Materie-Impulsdichte an die Impulsbedingung M^H p = 0 (deren
  Multiplikator waere der Shift). Eine gleichfoermig bewegte Quelle wirkt also nur ueber ihre Energie (V1, O(v^0), mit
  der Zeitabhaengigkeit der Lage) und ihre Spannungen rho v v (S, O(v^2)). Mitfuehrung (Gravitomagnetismus, O(v)) fehlt
  strukturell. Vorab ableitbar; keine Rechnung dafuer geplant, nur wenn Zeit bleibt eine beschreibende.
- **Pumpen:** Mit additiven Quellen ist die Antwort linear; parametrische Verstaerkung braucht eine Modulation von B oder A
  (multiplikativ, zweite Ordnung in der Quelle). Abschaetzung als Mathieu-Rate, keine Rechnung geplant.

## 2. Formulierung: lineare Antwort im Frequenzbereich [F, M]

- Netz V (ew.baue('V')), R1 wie ew.py: S(k) = orthonormales Komplement von Bild [M, c] (Rang 40 erwartet, geprueft).
  A_red = S^H A S, B_red = S^H B S. Bewegungsgewichte J je Tetraeder-Art (A = Summe_t J_t A0_t):
  - **J_iso** (primaer fuer die Dynamik): TT-ISO-1-Bestwahl symmetrisch [P]: finn_auf = finn_ab = 1,
    kegel = 10^-1,0453267 (0,0901), sechs = 10^-0,0010098 (0,9977). Dort ist c_TT isotrop auf 1e-5 [P].
  - **J = 1** (ew.py unveraendert, beschreibend).
- Hamilton (G = 1): H = (1/(2 kappa_g)) p^H A p + (kappa_g/2) a^H B a + sigma(t)^H a + mu^H (m(t) - kappa' c^H a)
  + Eichung, Zwang c^H p = 0, M^H a = M^H p = 0 (Paar zweiter Klasse wie ew.py).
  - Daraus: a = S x + a_c, a_c = c (c^H c)^-1 m/kappa'; x' = A_red y/kappa_g; y' = -kappa_g B_red x + f_red mit
    f_red = S^H f, **f_V1 = -(kappa_g/kappa') B c (c^H c)^-1 m = -2 B c (c^H c)^-1 m**, **f_S = -sigma**.
  - Statischer Grenzfall = KKT-System von MATERIE-NETZ-1 (nachgerechnet [M]).
- Moden: A_red = L L^H (Cholesky), D = L^H B_red L = U Omega^2 U^H. TT = die zwei kleinsten Omega^2 (Kontrolle:
  TT-Anteil ueber ew.tensor_fit und tp.tt_anteil an 3 Richtungen). Modenkopplung g_j = (L U_j)^H f_red.
- **Leistung (Goldene Regel, unendliches Volumen):**
  P(omega) = (pi/(4 kappa_g)) (V_Zelle/(2 pi)^3) Summe_j Int dOmega_n (k_j^2/v_j) abs(g_j(k_j n))^2,
  k_j auf der Massenschale Omega_j(k_j n) = omega, v_j = dOmega_j/dk radial. Nachgerechnet [M]: fuer ein Netz mit affiner
  Einstein-Kopplung ergibt das genau P_E (1.3).
- **Statische TT-Kopplung** (unabhaengig von A und J): C(k) = Summe der zwei weichen Eigenrichtungen v_j von B_red:
  abs(v_j^H f_red)^2/lambda_j. Verhaeltnis G_rad,stat/G = Int C dOmega/Int C_E dOmega.
- Bloch-Konvention wie ew.py/mn.py: a_e(R) = a_e(k) e^(i k.R) (R = Zelle der kanonischen Kante), f(k) = Summe_R f(R) e^(-i k.R).
- Numerik: Richtungen Gauss-Legendre in cos(theta) (10) x gleichmaessig in phi (20) = 200. Radial kl in 28 Werten
  geometrisch von 0,005 bis 1,0 (l = l_P = sqrt2/4 kubisch); Massenschale und Kopplungen durch Interpolation in log-log je
  Richtung und Zweig. Auswertung bei kl in {0,01; 0,02; 0,05; 0,1; 0,15; 0,2; 0,3; 0,5; 0,8} mit omega = c_0 kl/l_P.

## 3. Quelle

### 3.1 phi-Quadrupol (zwei gegenphasige Klumpen) [F]

- phi(x) = g(x - x_c - d e) - g(x - x_c + d e), g = exp(-abs(x)^2/(2 w^2)), w = d = 0,8 l_P, Mitte x_c = Ecke P0 (Zelle 0).
  Zwei Klumpen entgegengesetzten Vorzeichens; zwischen ihnen zeigt grad phi laengs e.
- phi schwingt als cos(Omega t); die Spannung schwingt mit omega = 2 Omega. Quellterm: T_ij(x, t) = T[phi]_ij(x) cos(omega t)
  (der Vorfaktor 1/2 aus cos^2 faellt in allen Verhaeltnissen heraus).
- Achsen e: [001] (primaer), [111], allgemein (1, 2, 3)/sqrt14.
- phi an den Ecken, P1 je Tetraeder; Kasten aller Zellen mit Abstand <= 3,2 (kubisch) von x_c.

### 3.2 Spannungskopplung S (Hodge) [F, M]

- Je Tetraeder K_t = V_t D^T g_t^-1 D (Gram-Matrix g aus den 6 Kantenlaengen, Ecke 0 als Ursprung). dK_t/dl_p je Kante p
  durch komplexen Schritt (h = 1e-20). sigma_e(R) = Summe ueber Tetraeder an der Kante: l_p (1/2) phi_t^T (dK_t/dl_p) phi_t.
- Kontinuum-Spannung derselben Quelle fuer den Bezug: S~(k) = Summe_t V_t T_t e^(-i k.x_t) (x_t Schwerpunkt).

### 3.3 Energieanteil fuer V1 (Erhaltung) [F, M]

- Erhaltung in c = 1: d_t^2 eps = d_i d_j T_ij, also eps~(k) = (k_i k_j/omega^2) S~_ij(k) (auf der Schale: n n : S~).
- Eckenergie: m_v(k) = (V_v/V_Zelle) e^(i k.p_v) eps~(k) (V_v: Eckvolumen = 1/4 jedes anliegenden Tetraeders, wie mn.py;
  p_v Lage der Ecke in der Zelle). Monopol und Dipol sind null; m ist eine reine Quadrupol-Verteilung der Eckenergie.
- Energie-Quadrupol: I = -2 S(0)/omega^2. "Feste Amplitude" (Karte) heisst also S(0) ~ omega^2.

## 4. Messgroessen und Kontrollen

- Je kl und Achse: P_V1, P_S, P_V1+S (kohaerente Summe der Kraefte), P_E; Verhaeltnisse P/P_E, P_V1/P_S;
  Amplitudenverhaeltnis A_R = sqrt(P_V1/P_S); r h_rms; statisch C_V1/C_E, C_S/C_E; fuer J_iso (primaer) und J = 1.
- **Kontrollen:**
  - KP1: Summe_t E_t fuer gleichfoermiges grad phi = (1/2) abs(G)^2 V_Zelle; Summe_e sigma_e n_e n_e^T = -V_Zelle T (relativ <= 1e-10).
  - KR: Rang [M, c] = 40 an allen k; c^H M = 0.
  - KN: weiche Richtung von P bei kl = 0,01: lambda/k^2 = 0,2 (also G_N/G = 1) an allen 200 Richtungen.
  - KA: affine TT-Steifigkeit a^H B a/k^2 = 0,25 (abs(h) = 1) an [100], [110], [111].
  - KT: TT-Anteil der zwei gewaehlten Moden >= 0,99 bei kl = 0,01 an [100], [110], [111]; Omega^2/k^2 gegen TT-ISO-1
    (J_iso 0,10480; J = 1: 0,11889 / 0,12643 in [100]).
  - KG: P_E aus der Winkelformel gegen die kompakte Formel (2 G omega^2/5) abs(S(0)^TF)^2 bei kl = 0,01 (prueft Quadratur
    und Lambda; Rest nur durch die Quellgroesse, O((k R)^2)). Die Goldene Regel selbst ist am Schreibtisch gegen P_E
    nachgerechnet (Abschnitt 2), nicht numerisch.
  - KD: dynamisch (P_S/P_E, J_iso und J = 1) gegen statisch (Int C_S/Int C_E) bei kl = 0,01. Erwartet [M]: gleich, weil die
    Massenschalen-Kopplung bei kleinem k nur die statische TT-Kopplung mal Zustandsdichte ist (Abschnitt 2).
  - KS: V1-Einheitskopplung (eps~ = 1) an TT in [100], [110], [111] gegen Median, Min, Max ueber die 200 Richtungen bei
    kl = 0,01 (Symmetrie 1.2: in [100] und [111] erwartet nahe null). Die Einheitskopplung haengt nicht von der Quelle ab.
  - KQ: Winkelquadratur 10 x 20 gegen 14 x 28 (Lauf H2): Tabellenwerte gleich auf <= 1e-3 relativ.
  - KM: Massenschale monoton und innerhalb des kl-Gitters (Zaehler nicht_monoton_oder_aussen = 0 fuer kl <= 0,5).

## 5. Urteilsregeln (mechanisch in pn.py auswertung)

**PN0** (Kontrolle; V1 allein: TT-Abstrahlung unter 1e-3 der Spannungskopplung bzw. skaliert wie (k l)^2):
- Nach Plan (Amplitude, wie K1): eingetroffen, wenn fuer alle drei Achsen (J_iso) A_R(kl) <= 1e-3 fuer alle kl <= 0,1
  **oder** der Exponent p aus dem log-log-Fit von A_R ueber kl in {0,01; 0,02; 0,05; 0,1} >= 1,8 ist.
- Nach Kartenwortlaut (Leistung): wie Plan mit P_V1/P_S statt A_R (Schwelle 1e-3, Exponent der Leistung >= 1,8).
- K1 (Karte) ist dasselbe wie PN0 nach Plan.

**PN1** ([H] mit S strahlt das Netz TT ab, Leistung folgt omega^6 bei fester Amplitude auf 20 % fuer kl < 0,3):
- Nach Plan: fuer alle drei Achsen (J_iso) (a) P_V1+S(kl = 0,01) >= 0,1 P_E und (b) Q(kl) = [P_V1+S/(omega^6 abs(I)^2)](kl)
  / [dasselbe bei kl = 0,01] liegt fuer alle kl in {0,02; ...; 0,2} in [0,8; 1,2] (kl < 0,3 streng; 0,3 beschreibend).
- Nach Kartenwortlaut: P_V1+S/P_quad in [0,8; 1,2] fuer alle kl in {0,01; ...; 0,2}, P_quad = (G/10) omega^6 abs(I^TF)^2
  (reine Quadrupolformel, absolut).

**PN2** ([H] Kopplung der Abstrahlung passt zur statischen Newton-Kopplung, Verhaeltnis wie Einstein auf 10 %):
- G_N/G aus KN (Mittel ueber Richtungen).
- Nach Plan: G_rad/G = P_V1+S/P_E bei kl = 0,01 (J_iso); eingetroffen, wenn (G_rad/G)/(G_N/G) in [0,9; 1,1] fuer alle drei Achsen.
- Nach Kartenwortlaut ("Kopplung"): G_rad,stat/G = Int C_S dOmega/Int C_E dOmega bei kl = 0,01 (ohne J); gleiche Schwelle.
- Bedeutung der Ausgaenge: wie auf der Karte; nichts daran geaendert.
- Bricht der J_iso-Lauf ab, urteilt J = 1 (gekennzeichnet; P_E dann mit Winkelmittel von 1/c_j, nur naeherungsweise).
  Fehlt beides: nicht entscheidbar.

## 6. Agenten-Erwartungen (vorab; kein Kartenurteil)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| Z1 | KP1, KR, KN, KA auf <= 1e-8 | 85 % |
| Z2 | V1-Amplitude an TT bei kl = 0,01 unter 1e-3 der S-Amplitude (alle Achsen) | 65 % |
| Z3 | G_rad,stat/G bei kl = 0,01 in [0,9; 1,1] | 55 % |
| Z4 | P_V1+S/P_E bei kl = 0,3 weicht um mehr als 10 % von kl = 0,01 ab | 40 % |

## 7. Laeufe (.69, kleintest.sh, Spur cpu6, 1 Thread, <= 600 s)

- p4000a/p4000b waren um 04:15 UTC belegt (QBALL-DOPPELSPALT-1); die Rechnung ist numpy (kleine dichte Matrizen) und
  laeuft auf cpu6.
- **Rauchtests** (vor dem Einfrieren, nur Rueckgabewert, Laufzeit, Speicher und JSON-Schluessel gelesen, keine Werte):
  - r1 04:26:02 bis 04:26:15 UTC (cpu6, --rauch: 4 x 6 Richtungen, 6 kl), rc = 0, 12,0 s, 104 MB; Quelle 3,0 s, k-Schleife 3,0 s.
  - r2 04:27:13 bis 04:27:27 UTC (cpu6, --rauch, neue Optionen --nt --nphi --w --d), rc = 0, 12,9 s.
- **Laufliste** (Arbeitsordner /home/fmh/fmhc-physics-remote/pumpe-netz-1/, Code aus code/ nach dem Einfrieren):

| Lauf | Spur | Aufruf | Schaetzung |
|---|---|---|---|
| H1 | cpu6 | pn.py lauf --out lauf/h1.json (10 x 20 Richtungen, w = d = 0,8 l_P; primaer, Urteile) | 1 bis 3 min |
| H2 | cpu6 | pn.py lauf --nt 14 --nphi 28 --out lauf/h2.json (KQ) | 2 bis 5 min |
| H3 | cpu6 | pn.py lauf --w 1.6 --d 1.6 --out lauf/h3.json (groessere Quelle, beschreibend: Formfaktor) | 1 bis 3 min |
| BI | cpu6 | pn.py bild --ein lauf/h1.json --bild lauf/bild-pumpe-netz.png --out lauf/bild.json | < 10 s |

- Bricht H1 an der Laufzeit ab: einmal mit --nt 8 --nphi 16 (gekennzeichnet). Urteile nur aus H1 (bzw. diesem Ersatz).
