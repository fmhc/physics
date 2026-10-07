# IMPULS-NETZ-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 46)

- Start 2026-10-05 07:14:26 CEST (date). Plantext ab 07:32:34 CEST (date), vor jeder Rechnung. Zeitbox 150 min, also
  bis 09:44:26 CEST; danach kein neuer Lauf.
- Grundlage: KARTE.md (IN0 bis IN3; Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Werkzeug: code/pn.py, ew.py, tp.py, mn.py, nachtrag_iso.py unveraendert aus PUMPE-NETZ-1 kopiert (sha256 c8034e40...,
  fa7b6417..., 419d7da6..., b36984d3..., 1c92cb23...). Neu: code/inz.py (importiert diese fuenf unveraendert).
- Kennzeichen: [M] eigene Mathematik (vorab), [E] gerechnet, [P] Projektdatei, [ES] eigener Schluss, [F] Festlegung,
  [H] Hypothese, [L?] Literatur ohne Abruf, [S] Quelle abgerufen. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Teil 1: Formulierung der Impulskopplung (Schreibtisch, vor jeder Rechnung)

### 1.1 Welche Netzgroesse ist die Impulsregel? [M, Codelesung ew.py]

- Bezeichnungen wie ew.py/pn.py: Kantenwerte a (a_e = delta l/l), Impulse p, H_0 = (1/(2 kappa_g)) p^H A p +
  (kappa_g/2) a^H B a. M (E x 3 nV): Eckverschiebung xi -> Kantendehnung, (M xi)_e = n_e.(xi_s2 e^(i k.T_e) - xi_s)/l_e.
  c (E x nV): skalare Regel (c^H a = Summe l eps je Ecke). Bekannt [P, gerechnet in PUMPE-NETZ-1]: B M = 0 (Regge ist
  bei Eckverschiebung im Flachen invariant), c^H M = 0 (KR: 1,6e-15), Rang [M, c] = 40.
- **Die Impuls- bzw. Verschiebungsregel ist M^H p = 0** (3 Komponenten je Ecke). Sie erzeugt die Eckverschiebung:
  {a, xi^H M^H p} = M xi. Ihr Multiplikator ist der Shift nu (Eckgeschwindigkeit). In R1 steckt sie schon im Code: p wird
  auf das Komplement von Bild [M, c] projiziert (pn.py Z. 259 bis 263), a ebenso (dort ist M^H a = 0 die Eichwahl).
- **Sie ist erster Klasse** [M]: d/dt (M^H p) = -kappa_g M^H B a = 0, weil B M = 0. Sie vertauscht mit dem skalaren Paar:
  {c^H a, xi^H M^H p} = c^H M xi = 0, und c^H p, M^H p sind beide Impulse. Anders als die skalare Regel (zweiter Klasse,
  TT-ISO-1, GAMMA-NETZ-L [P]) ist die Verschiebungsregel also eine echte Eichregel.
- Kontinuum [L, ADM]: Das ist die linearisierte Impulsbedingung -2 d_j pi_ij + (Materieterm) = 0, Multiplikator N_i.

### 1.2 Wie koppelt die Impulsdichte der Materie daran? [M]

- **Regel mit Quelle: M^H p = J.** J (3 nV je k) ist der Materie-Impuls je Ecke, mit denselben P1-Gewichten wie die
  Spannung: J_v = Int psi_v T^(0i) d^3x (psi_v: P1-Hutfunktion der Ecke v; fuer glatte Stroeme J_v = V_v j(x_v), V_v =
  Eckvolumen wie pn.eckvolumen).
- Hamilton-Funktion: H = H_0 + sigma^H a + mu^H (m - kappa' c^H a) - nu^H J + nu^H M^H p (+ Eichwahl M^H a = 0). Der
  Term -nu^H J ist die Kopplung Shift mal Impulsdichte (ADM: N_i H^i_Materie). **Keine neue Konstante:** Die
  Normierung von J ist dadurch festgelegt, dass M^H p + (Materie-Erzeuger) die Gesamtverschiebung erzeugt.
- **Widerspruchsfreiheit (Erhaltung der Regel):** d/dt (M^H p - J) = -M^H sigma - J'. Die Regel bleibt genau dann
  erhalten, wenn **J' = -M^H sigma** (Gitter-Impulsbilanz: Aenderung des Impulses an der Ecke = minus Nettokraft der
  Spannung auf die Ecke; M^H sigma ist die P1-Divergenz Int psi_v d_j T^(ij)). Fuer eine vorgegebene Quelle legt das J
  bis auf eine Konstante fest. Fuer sigma(t) = sigma_0 cos(omega t): J(t) = -M^H sigma_0 sin(omega t)/omega.
  Gleichwertig [M]: Die Wirkung ist unter zeitabhaengiger Eckverschiebung (a -> a + M xi, nu -> nu + xi') genau dann
  invariant, wenn J' = -M^H sigma; sonst aendert sie sich um -Int (M^H sigma + J')^H xi dt.
- Vertraeglich mit dem skalaren Paar [M]: p_J := M (M^H M)^-1 J liegt in Bild M, also gilt c^H p_J = 0 von selbst;
  c^H a ist unter Eckverschiebungen invariant. A_red (Cholesky) bleibt unveraendert; J ist eine lineare Quelle, es gibt
  keine neue Mode und keine neue Instabilitaet.
- **Grenze [ES]:** Fuer eine vorgegebene Quelle (wie hier) ist J durch die Bilanz definiert. Fuer ein dynamisches
  Materiefeld auf dem Gitter (phi an den Ecken, P1) ist die gemeinsame Eckverschiebung keine exakte Symmetrie der
  Materie-Energie; ein lokal aus (phi, phi') gebildetes J erfuellt die Bilanz dann nur bis auf Gitterfehler. Nicht
  gerechnet.

### 1.3 R1-Reduktion mit Impulsquelle [M]

- a = S x + a_c (wie pn.py), **p = S y + p_J**, S = Orthonormalbasis des Komplements von Bild [M, c] (= ker M^H und ker c^H).
  Symplektisch: p^H da = y^H dx (p_J steht senkrecht auf S und auf a_c). Reduzierte Hamilton-Funktion:
  H_red = (1/(2 kappa_g)) (S y + p_J)^H A (S y + p_J) + (kappa_g/2) x^H B_red x - x^H f_red (+ V1 wie pn.py).
- Bewegung: x' = (A_red y + S^H A p_J)/kappa_g, y' = -kappa_g B_red x + f_red. Eliminiert:
  x'' + A_red B_red x = A_red f_eff/kappa_g mit **f_eff = f_red + A_red^-1 S^H A p_J'**, p_J' = -P_M sigma
  (P_M = M (M^H M)^-1 M^H). Fuer sigma_0 cos(omega t) ist der Zusatz in Phase mit der Spannungskraft und unabhaengig
  von omega: **f_SJ = -[S^H + A_red^-1 S^H A P_M] sigma_0**.
- Modenkopplung (pn.py-Konvention X = L U): g_j = X_j^H f_eff = -e_j^H sigma_0 + (V1-Teil wie pn.py) mit
  **e_j = S X_j + P_M A S A_red^-1 X_j = (1 - P_c) A p_j**, p_j = S A_red^-1 X_j (Impulsrichtung der Mode).
- **Lesart [M]:**
  - Ohne J koppelt die Spannung an die R1-Modenform S X_j = TT + M xi_j. Der Eichanteil M xi_j entsteht, weil die
    R1-Wahl (senkrecht zu Bild M im euklidischen Kantenmass) eine Laengsbeimischung abzieht; er koppelt an M^H sigma
    (= Divergenz). Das ist das Leck aus PUMPE-NETZ-1 4.4. Folge: **Ohne J haengt die Kopplung von der Eichwahl ab**
    (andere Eichung M^H G a = 0 mit positivem G: anderer Eichanteil, andere Zahl).
  - Mit J koppelt die Spannung an die ungeprojizierte Geschwindigkeit (1 - P_c) A p_j der Mode. p_j liegt in ker M^H
    und ker c^H und haengt nicht von der Eichwahl der Lage ab. **Mit J ist die Kopplung eichunabhaengig.** Herleitung fuer
    die Eichung M^H G a = 0: a = T x_G mit T = (1 - P_M^G) S, P_M^G = M (M^H G M)^-1 M^H G; dann p^H da = y^H dx_G -
    J^H K dx_G mit K = (M^H G M)^-1 M^H G S. Der Zusatzterm hebt den Unterschied -K^H M^H sigma der Kraft genau auf.
  - Kontinuum [M]: Die Bewegungsenergie je Tetraeder in ew.py ist eine DeWitt-Form, A0_ef = (n_e.n_f)^2 - 1/2 =
    G(n_e n_e, n_f n_f) mit G(X, Y) = X:Y - (1/2) tr X tr Y (ew.py Z. 170). Im Kontinuum bildet G einen TT-Impuls auf eine
    TT-Geschwindigkeit ab; dann ist e_j rein TT, und nur T^TT koppelt (Einstein). Auf dem Gitter haengt es davon ab, ob
    A p_j Laengs- oder Eichanteile hat. **Nicht vorab ableitbar; das misst die Rechnung (IN2).**
- **Energie-Kanal (V1) [M]:** Die Kraft f_V1 = -(kappa_g/kappa') B c (c^H c)^-1 m haengt nicht von J ab. Die skalare
  Regel bleibt zweiter Klasse; ihr Leck (Amplitude 2,7 bis 3,0 % in PUMPE-NETZ-1) wird durch die Impulskopplung nicht
  behoben. Mit J aendert sich nur die Interferenz von V1 mit dem Spannungskanal. Darum berichte ich S+J und V1+S+J getrennt.

### 1.4 Mitfuehrung (Gravitomagnetismus) [M]

- Stationaere Quelle mit Impuls J (z. B. rotierend; transversal, M^H sigma = -J' = 0): Ruhelage aus dH/dy = 0:
  y = -A_red^-1 S^H A p_J, x = 0. Energie **H_min(J) = (1/(2 kappa_g)) p_J^H [A - A S A_red^-1 S^H A] p_J**
  (Schur-Komplement). Sie ist eichunabhaengig (nur Impulse). Stationaritaet: A p/kappa_g = M lambda + c eta, Shift
  nu = -lambda, also H_min = -(1/2) J^H nu (Identitaet, Kontrolle KGM).
- **Einstein-Bezug (vorab im Kontinuum, keine Messung) [M]:** ADM linear, Maximalslicing, transversaler Shift:
  gamma'_ij = 32 pi G (pi_ij - delta_ij pi/2) + d_i N_j + d_j N_i, d_j pi_ij = -j_i/2. Stationaer: pi_ij =
  -(d_i N_j + d_j N_i)/(32 pi G), Laplace N = 16 pi G j^T, also N_i = -4 G Int j_i/r (wie g_0i in harmonischer Eichung
  [L]). Energie H_GM = Int abs(grad N)^2/(32 pi G) = **8 pi G abs(j^T(k))^2/k^2** je Volumen (c = 1). Fuer zwei
  Punktstroeme 4 G (m1 v1).(m2 v2)/r, passend zum -4 G m1 m2 v1.v2/r-Anteil der EIH-Lagrange-Funktion [L?].
- Einheiten [F, wie PUMPE-NETZ-1 PLAN 1.3]: c := c_0 (TT-Tempo, J_iso 0,323734 [P]). Zeit tau = c_0 t, Impuls in
  tau-Einheiten = c_0 mal Impuls in ew-Einheiten, Energie unveraendert. Je Zelle (Bloch, J_v = V_v e e^(i k.p_v),
  Summe V_v = V_Zelle): **H_GM,E = 8 pi G c_0^2 V_Zelle abs(e_T)^2/k^2.**
- Messgroesse r(n, e) = H_min(J_e) k^2/(8 pi G c_0^2 V_Zelle) fuer Einheitsvektoren e senkrecht zu n (2 x 2-Block je
  Richtung, Eigenwerte und Mittel). Einstein: r = 1.
  - Rotierende Quelle (Fernfeld, Dipolstrom j(k) ~ L x k): R_rot(L) = Summe_n w_n abs(L x n)^2 r(n, e_L)/Summe_n w_n
    abs(L x n)^2 = Verhaeltnis der gravitomagnetischen Selbstenergie Gitter/Einstein. L = [001], [111], (1,2,3).
  - Gleichfoermig bewegte Quelle: R_mov(v) mit Gewicht abs(v_T)^2, v_T = (1 - n n) v. v = [001], [111], (1,2,3).
  - Laengsanteil (beschreibend): k^T Q k gegen 2 pi G c_0^2 V_Zelle/k^2. Das ist der Kontinuumswert unter der
    Bedingung (d_i d_j - delta_ij Lap) pi_ij = 0, die GAMMA-NETZ-L [P] als Gegenstueck von c^H p = 0 nennt [ES];
    eichabhaengig, kein Urteil.
- Ohne J ist H_min = 0: keine Mitfuehrung (PUMPE-NETZ-1 5. [P]).

## 2. Ableitbarkeitsprobe (vor jeder Rechnung)

- **IN0 vorab ableitbar [M]:** Ohne J ist der Rechenweg in inz.py derselbe wie in pn.py (gleiche Operatoren, gleiche
  Interpolation). Die Kontrolle prueft nur die Kopie und meine Erweiterung, sie misst nichts Neues. Erwartet: G_rad/G_N
  ohne J = 1,18440509 / 0,90877497 / 0,97696465 (h1.json [P]) auf Rundungsfehler.
- **IN1 vorab ableitbar [M]:** Abschnitt 1.1 bis 1.3 folgt aus B M = 0 und c^H M = 0 (beides bekannt [P]). Die Rechnung
  prueft nur diese Identitaeten bei k != 0 und die Eichunabhaengigkeit am Code (Abschnitt 4, KE). **Das ist keine
  Messung.** Die Eichabhaengigkeit ohne J (KE ohne J) ist dagegen der Groesse nach nicht vorab bekannt.
- **IN2 nicht ableitbar:** Ob (1 - P_c) A p_j auf dem Gitter langwellig reine TT ist (Abschnitt 1.3), und wie gross der
  V1-Rest nach der Interferenz ist.
- **IN3 nicht ableitbar:** Ob das Schur-Komplement von A im Vektor-Sektor dasselbe Verhaeltnis zum TT-Sektor hat wie
  DeWitt im Kontinuum. Gemessen wird das Verhaeltnis r; der Einstein-Wert 1 ist [M], keine Messung.
- **Symmetrie:** Ich verwende keine Symmetrieaussage fuer ein Urteil. Wo ich eine nenne, ist sie bei k != 0 am Code
  geprueft (benannte Richtungen [100], [111] usw. der Isotropie-Tabelle, kl 0,01 und 0,1).

## 3. Quelle und Rechenweg [F]

- Netz V (ew.baue('V')), Paarung A1R1, J_iso (primaer) und J = 1 (beschreibend), alles wie PUMPE-NETZ-1 PLAN 2 und 3.
- Quelle wie PUMPE-NETZ-1: zwei gegenphasige phi-Klumpen, w = d = 0,8 l_P, Achsen [001], [111], (1,2,3); Spannung
  T[phi] cos(omega t) mit P1-Gewichten; V1-Energie aus der Kontinuums-Erhaltung (unveraendert).
- **Neu:** J aus der Gitter-Bilanz J' = -M^H sigma (Abschnitt 1.2); Zusatzkraft A_red^-1 S^H A (-P_M sigma_0) je J-Variante.
  Kanaele: S, V1, V1+S (wie pn.py), **S+J, V1+S+J** (neu).
- Leistung per Goldener Regel auf der Massenschale (pn.py unveraendert); statische bzw. quasistatische Kopplung an die
  zwei weichen Moden von B_red: ohne J A-unabhaengig (wie pn.py), mit J A-abhaengig (je J-Variante).
- Richtungen 10 x 20 (Gauss-Legendre x gleichmaessig), kl-Gitter 28 Werte 0,005 bis 1,0, Auswertung bei
  kl in {0,01; 0,02; 0,05; 0,1; 0,15; 0,2; 0,3; 0,5; 0,8} wie pn.py.

## 4. Messgroessen und Kontrollen

- **G_rad/G_N je Achse** (kl = 0,01, J_iso, dynamisch): ohne J (V1+S; IN0), mit J (V1+S+J; IN2), dazu S+J und S allein;
  quasistatisch S+J (J_iso, J = 1). G_N/G aus KN wie pn.py.
- **Kreisbahnen** (Nachtrag ND von PUMPE-NETZ-1, jetzt geplant): kompakte spurfreie Quelle S = (u + i w)(u + i w)^T,
  Bahnnormale m = [001], [111], [110], (1,2,3) und 8 Zufallsnormalen (Saat 31), kl = 0,01, 10 x 20 Richtungen:
  G_rad/G ohne und mit J (statisch; mit J quasistatisch J_iso und J = 1; dynamisch J_iso).
- **Isotropie** (wie Nachtrag NI): gleichfoermige Spannung mit Wellenvektor k, 10 benannte Richtungen (kl 0,01 und 0,1)
  und 6 x 12 Richtungen (kl 0,01): R(+), R(x), C_L1, C_L2, C_nn, C_Ptr ohne und mit J (J_iso).
- **Mitfuehrung:** r(n, e), R_rot, R_mov, isotropes Mittel R_iso (Abschnitt 1.4) bei kl in {0,01; 0,02; 0,05; 0,1; 0,2},
  10 x 20 Richtungen, J_iso (primaer) und J = 1 (c_0 = 0,349212 quadratisch gemittelt, nur naeherungsweise).
- **Kontrollen:**
  - Wie PUMPE-NETZ-1: KP1, KR (Rang 40, c^H M), KN (G_N/G), KD (dynamisch S gegen statisch S), KM. KA, KT, KG sind in
    PUMPE-NETZ-1 mit denselben Operatoren gerechnet [P] und werden nicht wiederholt; IN0 prueft den gemeinsamen Rechenweg.
  - KND: Kreisbahnen und kompakte phi-Quellen ohne J (statisch) gegen Nachtrag ND von PUMPE-NETZ-1 (1,0344 / 0,9925 /
    1,0030 / 1,0030; phi 1,1622 / 0,9118 / 0,9671 [P]).
  - **KF (erste Klasse):** max abs(M^H B)/(abs(M) abs(B)) <= 1e-10 an allen k des Hauptlaufs.
  - **KJ:** M^H p_J = M^H sigma (also M^H P_M sigma = M^H sigma), Rest relativ <= 1e-10; c^H p_J <= 1e-10 relativ.
  - **KE (Eichprobe):** gleichfoermige Spannungen h+, hx, L1, L2, nn an 10 benannten Richtungen, kl 0,01 und 0,1, J_iso,
    zwei Eichungen M^H G a = 0 mit G = diag(Zufall in [0,25; 4]) (Saat 41 und 43) gegen R1. Ohne J: Unterschied
    (beschreibend). Mit J: Kraft und Kopplung gleich, <= 1e-8 (Teil von IN1). Masse: Kraft relativ zu ihrer Norm;
    Kopplung abs(C_G - C_R1)/C_E geteilt durch max(C_R1/C_E, 1), also relativ zur Einstein-Skala (C_nn ist auf [100]
    null, ein reiner Quotient waere dort Rauschen).
  - **KGM:** H_min = -(1/2) J^H nu, relativ <= 1e-8; S^H A p_stat = 0 relativ <= 1e-10.
  - **KDJ:** dynamisch P_SJ/P_E gegen quasistatisch C_SJ/C_E (J_iso) bei kl = 0,01; erwartet gleich (wie KD) [M].
  - **KK:** r(n, e) bei kl 0,01 gegen 0,02 (Konvergenz in k, Exponent von H_min k^2 nahe 0).

## 5. Urteilsregeln (mechanisch in inz.py urteil)

- **IN0** (Kontrolle: ohne J reproduziert der Code PUMPE-NETZ-1, G_rad/G_N = 1,18 / 0,91 / 0,98 auf 1 %):
  - Nach Plan: abs(G/G_ref - 1) <= 0,01 fuer alle drei Achsen, G = P(V1+S)/P_E/(G_N/G) ohne J, kl = 0,01, J_iso;
    G_ref = 1,1844050923687857 / 0,9087749678217026 / 0,9769646539098713 (h1.json, PN2 det).
  - Nach Kartenwortlaut: dasselbe gegen 1,18 / 0,91 / 0,98.
- **IN1** ([H] es gibt eine widerspruchsfreie Impulskopplung):
  - Nach Plan eingetroffen, wenn Abschnitt 1 eine Kopplung angibt und am Code gilt: Rang [M, c] = 40 an allen k, KR
    (c^H M) <= 1e-10, KF <= 1e-10, KJ <= 1e-10, Cholesky von A_red an allen k (beide J), KE mit J <= 1e-8. Sonst nicht
    eingetroffen. Kartenwortlaut: dieselbe Regel. Vorab ableitbar (Abschnitt 2).
- **IN2** ([H] mit Impulskopplung G_rad/G_N fuer alle drei Achsen innerhalb 1e-2 bei 1):
  - Nach Plan: abs(G_rad,dyn(V1+S+J)/G_N - 1) <= 0,01 fuer alle drei Achsen (kl = 0,01, J_iso).
  - Nach Kartenwortlaut: dieselbe Regel (die Kartenzahlen 1,18 / 0,91 / 0,98 sind die dynamischen V1+S-Werte).
  - Beschreibend daneben: S+J allein, quasistatisch, J = 1, Kreisbahnen.
- **IN3** ([H] die Mitfuehrung hat den Einstein-Koeffizienten auf 10 %):
  - Nach Plan: R_rot fuer L = [001], [111], (1,2,3) und R_mov fuer v = [001], [111], (1,2,3) bei kl = 0,01, J_iso, alle
    sechs in [0,9; 1,1].
  - Nach Kartenwortlaut ("den Einstein-Koeffizienten"): isotropes Mittel R_iso (Winkel und beide Querrichtungen) in
    [0,9; 1,1].
- Bricht J_iso ab (Cholesky), urteilt J = 1 (gekennzeichnet). Fehlt beides: nicht entscheidbar.
- Bedeutung der Ausgaenge: wie auf der Karte; nichts daran geaendert.

## 6. Agenten-Erwartungen (vorab; kein Kartenurteil)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| Z1 | KF, KJ, KGM, KE mit J auf <= 1e-10 bzw. 1e-8 | 90 % |
| Z2 | KE ohne J: Eichung G aendert C_L oder G_rad bei mindestens einer Richtung um mehr als 10 % relativ | 75 % |
| Z3 | S+J: abs(G_rad/G_N - 1) <= 0,05 fuer alle drei Achsen (Leck mindestens dreimal kleiner) | 50 % |
| Z4 | R_iso in [0,5; 2] | 70 % |

## 7. Laeufe (.69, kleintest.sh, Spuren cpu5 und cpu6, 1 Thread, <= 600 s)

- Arbeitsordner /home/fmh/fmhc-physics-remote/impuls-netz-1/; Code nach dem Einfrieren in code/ (per scp in eine neue
  Datei, dann mv; nie in place).
- **Rauchtests** (vor dem Einfrieren, nur Rueckgabewert, Laufzeit, Speicher und JSON-Schluessel gelesen, keine Werte):
  r1 (cpu6) inz.py lauf --rauch; r2 (cpu5) inz.py zusatz --rauch.
- **Laufliste:**

| Lauf | Spur | Aufruf | Schaetzung |
|---|---|---|---|
| H1 | cpu6 | inz.py lauf --out lauf/h1.json (10 x 20, 28 kl, beide J; IN0, IN2, KF, KJ, KD, KDJ) | 3 bis 6 min |
| Z1 | cpu5 | inz.py zusatz --out lauf/zusatz.json (Isotropie, KE, Kreisbahnen, Mitfuehrung) | 1 bis 4 min |
| UR | cpu5 | inz.py urteil --h1 lauf/h1.json --zusatz lauf/zusatz.json --out lauf/urteile.json | < 10 s |
| BI | cpu5 | inz.py bild --h1 lauf/h1.json --zusatz lauf/zusatz.json --bild lauf/bild-impuls-netz.png --out lauf/bild.json | < 10 s |
| H2 | cpu6 | inz.py lauf --nt 12 --nphi 24 --out lauf/h2.json (Quadratur, beschreibend; nur wenn H1 < 5 min) | 4 bis 8 min |

- Bricht H1 an der Laufzeit ab: einmal mit --nt 8 --nphi 16 (gekennzeichnet). Urteile nur aus H1 (bzw. diesem Ersatz)
  und Z1.
