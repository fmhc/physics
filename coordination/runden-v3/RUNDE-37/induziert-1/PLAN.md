# INDUZIERT-1: Plan (Code-Agent, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 05:22:30 CEST (date). Code ab 05:46:52 CEST, Plantext ab
  05:51:57 CEST (date).
- Vor diesem Plantext gerechnet: nichts zu dieser Karte. Parallel zum Schreiben lief der Rauchlauf "kontrolle-r1"
  (nur Kontrollen, Abschnitt 7); was er zeigt, steht in Abschnitt 11.
- Grundlage: KARTE.md (Schreibtisch, Test, IN0 bis IN5 mit Schwellen unveraendert uebernommen), Kette aus
  RUNDE-36/regge-4d-1/code/regge4d.py (unveraendert kopiert, sha256 2708f33b...; benutzt werden B0, Projektoren,
  Eichbasis, Richtungsliste).
- **Kennzeichen:** [M] eigene Mathematik; [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [F] Festlegung dieses
  Plans (von der Karte offen gelassen); [K] Kartenberichtigung; [H] Hypothese.

## 1. Modell [M]

- Kuhn-Netz in n = 2, 3, 4 Dimensionen wie REGGE-4D-1: n! Simplizes je Wuerfel, Kanten (x, d) mit d aus den
  2^n - 1 nicht leeren 0/1-Vektoren (Reihenfolge wie regge4d.py), Variablen s = l^2 je Kante.
- **Feld:** phi auf den Knoten, P1 je Simplex. Mit G_ab = (s_0a + s_0b - s_ab)/2 (a, b = 1..n) gilt
  V = sqrt(det G)/n!, grad lambda_a . grad lambda_b = (G^-1)_ab fuer a, b >= 1, und lambda_0 = 1 - sum lambda_a.
  - Kompakt: Gam = P^T G^-1 P mit P = [-1 | I] (n x (n+1)).
  - Lokale Matrix K_sigma = V Gam + (m^2 V/(n+1)) I (konzentrierte Massenmatrix, Karte).
  - K = Summe der K_sigma; Gamma(s) = 1/2 log det K (Karte).
- **Massenterm [F1]:** Die Masse sitzt geometrisch in der konzentrierten Massenmatrix (V_sigma/(n+1) je Ecke), haengt
  also von s ab wie sqrt(g) m^2 phi^2. Begruendung: Nur so ist die Masse ein kovarianter Regulator. Ein fester Term
  m^2 phi^2 waere eine zweite, nicht geometrische Kopplung. Im flachen Netz ist die Massenmatrix 1 je Knoten.
- **Masselos in 2D (Teil A):** Nullmode entfernt, Gamma = 1/2 log det' K. G = K^+, also G(q = 0) = 0. Weil die
  Konstante fuer jedes s im Kern liegt, gelten die Formeln von Abschnitt 2 exakt mit K^+.

## 2. Ableitungen und Blasensumme [M]

- **Lokale Ableitungen, analytisch [F2]:** G ist linear in s, G = sum_e s_e E_e. Damit:
  - dV/ds_e = (V/2) tr(G^-1 E_e)
  - d2V/ds_e ds_f = (V/4) tr(G^-1 E_e) tr(G^-1 E_f) - (V/2) tr(G^-1 E_e G^-1 E_f)
  - d(G^-1) = -G^-1 E_e G^-1; d2(G^-1) = G^-1 E_e G^-1 E_f G^-1 + (e <-> f)
  - Produktregel fuer K_sigma = V Gam + (m^2 V/(n+1)) I.
  - Begruendung: exakt und billig. Gegenprobe mit zwei weiteren Wegen (Abschnitt 7, K5): komplexer Schritt fuer dK
    (h = 1e-20) und fuer d2K als komplexer Schritt der analytischen dK, unabhaengig davon zentrale Differenz
    komplexer Schritte (h = 1e-4).
- **Hesse-Matrix, exakt:** dGamma/ds_a = 1/2 Tr(G K_a) und
  d2Gamma/ds_a ds_b = 1/2 Tr(G K_ab) - 1/2 Tr(G K_a G K_b), G = K^-1 (K^+ masselos), weil dG = -G dK G.
- **Fourier [M]:**
  - Translationsinvariant: G_ij = int_q G(q) e^{iq.(x_i - x_j)} mit G(q) = 1/K(q).
  - Fusspunkt-Konvention: Pi_dd'(k) = sum_R Hess_{(0,d),(R,d')} e^{ik.R}. Fuer reelles
    delta s_(x,d) = Re(u_d e^{ik.x}) gilt delta s^T Hess delta s = (N/2) u^+ Pi(k) u (k nicht gleich -k).
  - Vertexfunktion V_d(p, p') = sum_ij e^{-ip.x_i} (K_(0,d))_ij e^{ip'.x_j}. Damit
    Tr(G K_a G K_b) = int_p int_p' G(p) V_a(p,p') G(p') V_b(p',p), und die R-Summe erzwingt p' = p + k.
  - Ergebnis: **Pi_dd'(k) = 1/2 int_q G(q) W_dd'(q;k) - 1/2 int_q G(q) G(q+k) V_d(q,q+k) V_d'(q,q+k)^***.
    - V_d'(q+k, q) = V_d'(q, q+k)^*, weil K_(0,d') reell symmetrisch ist. Pi ist also hermitesch.
    - Vorzeichen: Der Tadpole-Teil (zweite Ableitung von K) kommt mit +, die Blase mit - (aus dG = -G dK G).
- **Phasen aus den Fusspunkten:** Simplextyp t mit Ecken v_0..v_n, lokale Kante e = (a, b) mit Richtung
  d = v_b - v_a und Fusspunkt v_a. Das Simplex mit e am Ursprung liegt bei x = -v_a.
  - V_d(q, q+k) = sum_Delta c_dDelta(k) e^{-iq.Delta}, Delta = v_c - v_c' (31 Werte in 4D).
  - c_dDelta(k) = sum_{t, e in d} sum_{v_c - v_c' = Delta} (dK_e)_cc' e^{ik.(v_c' - v_a)}.
  - W_dd'(q;k) = sum_{t, e in d, f in d'} e^{ik.(v_a' - v_a)} sum_cc' (d2K_ef)_cc' e^{-iq.(v_c - v_c')}.
- **Gitterintegrale:** g(R) = int_q G(q) e^{-iqR}, b(R) = int_q G(q) G(q+k) e^{-iqR}. Damit
  - Pi(k) = 1/2 sum_Delta w_dd'Delta(k) g(Delta) - 1/2 c(k) B(k) c(k)^+, B_{Delta,Delta'} = b(Delta - Delta').
  - Tadpole-Vektor dGamma/ds_d = 1/2 sum_Delta c_dDelta(0) g(Delta).
  - g und b per FFT auf dem L_q^n-Gitter (Riemann-Summe). Auf dem Torus L = L_q mit k auf dem Gitter ist das exakt.
    G(q+k) dann per Verschieben des Gitters, sonst aus dem verschobenen Symbol.
- **Mittelpunkts-Konvention** (fuer die Kette aus REGGE-4D-1): Pi^mid_dd' = e^{-ik.d/2} Pi_dd' e^{ik.d'/2}. Wegen der
  Inversionssymmetrie ist Pi^mid reell und gerade in k (geprueft).
- **Symbol [M, IN0]:** Im flachen Kuhn-Simplex (Orthoschema) ist grad lambda_i . grad lambda_j nur fuer
  aufeinanderfolgende Ecken ungleich null, und deren Differenz ist ein Achsenvektor. Jede Achsenkante traegt in der
  Summe ueber die Wuerfel das Gewicht sum_j C(n-1,j) j!(n-1-j)!/n! = 1. Also K(q) = sum_mu 4 sin^2(q_mu/2) + m^2;
  die Diagonalen tragen flach das Gewicht null. Fuer die Gitterintegrale wird das separable Symbol nur benutzt, wenn
  es auf dem Gitter auf <= 1e-12 mit dem allgemeinen (FFT des Stencils) uebereinstimmt; sonst das allgemeine.

## 3. Teil A (2D, Polyakov-Kontrolle)

- **Netz:** 2D-Kuhn = Quadrate mit (1,1)-Diagonale, rechtwinklig-gleichschenklige Dreiecke, Torus L x L, masselos,
  Nullmode entfernt. Flaeche A = L^2 = N.
- **Konforme Mode [F3]:** Ecken-Skalierung s_ij(eps) = s_ij exp(eps (sigma_i + sigma_j)), sigma = cos(k.x). Das ist
  l_ij = l_ij exp(eps (sigma_i + sigma_j)/2), also delta l/l = (sigma_i + sigma_j)/2 (Karte) in erster Ordnung.
  - Die Karte legt nur die erste Ordnung fest. Ich nehme die Ecken-Skalierung, weil sie wie e^{2 sigma} im Kontinuum
    eine Gruppe ist; konstantes sigma ist exakt eine globale Streckung. Polyakovs Formel gilt fuer diese Familie
    [L Polyakov 1981].
  - d2Gamma/d eps^2 = (N/2) u^+ Pi(k) u + sum_x,d dGamma/ds_d s_d (sigma_x + sigma_{x+d})^2 mit
    u_d = s_d (1 + e^{ik.d}); der zweite Term ist N sum_d dGamma/ds_d s_d (1 + cos k.d).
- **Messgroesse (Karte):** c_A(k) = (d2Gamma/d eps^2)/(k^2 A); Polyakov: -1/(24 pi) = -0,0132629.
- **Flaechenglied [K1, Kartenberichtigung]:** Die Karte erwartet "plus ein globales Flaechenglied O(1/A)". Dieses Glied
  (1/2) log(A_sigma/A) gehoert zu det' des Laplace-Operators M^-1 K (mit Massenmatrix), nicht zu det' K.
  - Exakt gilt [M]: det'(M^-1 K) = det'(K) A/(N det M).
  - In 1/2 log det' K steht also kein Flaechenglied. Waere das Gitter genau Polyakov fuer det'(M^-1 K), so haette
    det' K statt des Flaechenglieds den lokalen Term (1/2) sum_x log m_x.
  - Fuer N = L^2 und n = 1 waere das Flaechenglied fast doppelt so gross wie der Polyakov-Term. Es muss also behandelt
    werden: In P gibt es dieses Glied nicht. In D (unten) faellt es exakt heraus.
  - Urteil nach Kartenwortlaut: dieselbe Groesse c_P. Die Karte schreibt Gamma = 1/2 log det K vor, und ein
    Flaechenglied ist darin nicht abzuziehen.
- **Varianten (beschreibend, nicht geurteilt):**
  - l-linear: l_ij = l_ij (1 + eps (sigma_i + sigma_j)/2), also halber Tadpole-Term.
  - s-linear: kein Tadpole-Term (reine Hesse-Form in s).
  - D: Gamma_D = 1/2 log det'(M^-1 K). Verglichen wird Gamma_D - 1/2 log A mit Polyakov ohne Flaechenglied, also
    c_D = c_P - (1/2) (sum_x log m_x)''/(k^2 A); die Massenmatrix kommt aus den Dreiecksflaechen (Heron).
- **Gitter und Fenster [F4]:** L = 256, 512, 1024; k = 2 pi n/L in den Richtungen (1,0) (Urteil), (1,1) und (1,-1)
  (beschreibend); n = 1, 2, 4, ..., 64 (L >= 512) bzw. bis 16 (L = 256), abs(k) <= 0,8.
  - Fenster 2 pi/L << k << 1: n >= 8 und abs(k) <= 0,1.
  - Kleinstes ausgewertetes k im Fenster: L = 1024, n = 8, abs(k) = 0,0491.
- **Teil A2 (beschreibend, [F], vor dem Einfrieren ergaenzt):** universeller Anteil ueber die 4phi-Harmonische.
  - Im Kontinuum gilt [M]: 1/2 log det' -> -(1/(96 pi)) int sqrt(g) R (1/Delta) R. Quadratisch in h (Basis wie B0)
    ist das K_Pol = -(1/(48 pi)) k^2 t t^T mit t_a = <1 - n n, X_a>, in 2D also -(1/(48 pi)) k^2 P0s.
  - Alle polynomialen k^2-Terme haben in der Richtung phi von k nur die Moden 0 und 2. Dazu gehoeren lokale
    Gitterterme, Gegenterme und ihre Lage, Konventionen, Fortsetzungen zweiter Ordnung und die Massenmatrix.
  - Eine 4phi-Mode bei O(k^2) kann also nur aus dem nicht-analytischen Polyakov-Anteil kommen [M].
  - Rechnung: K_2 = B0^T (Pi^mid(k) - Pi(0)) B0/k^2 auf dem Torus L = 512 und 1024, fuer alle Gittervektoren n mit
    4 <= abs(n) <= 12 (Halbebene).
  - Fit je Eintrag mit den Moden 0, 2, 4 und k^2 mal den Moden 0, 2, 4, 6. Kennzahl
    lambda = <gemessene 4phi-Koeffizienten, Polyakov>/<Polyakov, Polyakov>; Polyakov heisst lambda = 1.
  - Nicht geurteilt. Prueft die Normierung der Kette gegen eine unabhaengige, universelle Zahl, auch wenn lokale
    Terme c_P beherrschen.
- **Beschreibend:** Steifigkeit der zwei Knotenverschiebungs-Moden u_d = sin(k.d/2) d.xi (Mittelpunktskonvention), roh
  und mit Gegenterm. In 2D ist B0 eine 3 x 3-Matrix und invertierbar; der Metrik-Teil ist also ganz Pi(0) (Abschnitt
  5), in symmetrischer Lage.

## 4. Teil B (4D): Rechnung

- Pi(k) in s und in Fusspunkt-Konvention aus Abschnitt 2, auf einem L_q^4-Gitter.
- **[F5] Massen:** m^2 = 0,01 und 0,04 (Karte, Urteil); m^2 = 0,0025 nur beschreibend, falls Zeit bleibt.
- **[F6] q-Gitter:** L_q = 64 (Haupt) und 48 (Konvergenz), dazu 32 nur beschreibend. Fehlerabschaetzung [M]: Die
  Riemann-Summe einer periodischen, in einem Streifen der Breite ~m analytischen Funktion hat einen Fehler
  ~ e^{-m L_q}. Er trifft nur den Infrarotteil, und der ist ~ m^4/(16 pi^2) klein.
- **[F7] k-Punkte:** k = 0 sowie die 8 Richtungen aus REGGE-4D-1 ((1,0,0,0), (1,1,0,0), (1,-1,0,0), (1,1,1,0),
  (1,1,1,1), (1,1,-1,-1), (1,1,1,-1), (1,2,3,4), normiert), jeweils mit abs(k) = 0,025; 0,05; 0,1; 0,2; 0,4.
  0,025 ist nur beschreibend.
- **Zusaetzlich [F8]:** zweite Variation des Gesamtvolumens V''(k) aus denselben Simplex-Ableitungen, Tadpole-Vektor
  dGamma/ds, Volumen-Gradient. Die 3D-Fassung (n = 3, L_q = 128, Kontinuum c0s/c2 = -1) rechne ich nur beschreibend.

## 5. Gegenterm und Kette

- **Sachlage [M]:** Im Gitter haengt die Vakuumenergie je Zelle von der Zellform ab (Karte). Pi(0) ist O(1), die
  erwartete Einstein-Steifigkeit dagegen klein: im Kontinuum c2 ~ Lambda^2/(384 pi^2) ~ 3e-3 bei Lambda ~ pi [L, H].
  Alles, was Pi(0) mit Ortsfaktoren der Ordnung (k.d)^2 multipliziert, verschiebt c2 deshalb in fuehrender Ordnung.
  Ich erwarte daher, dass die Lage und der Umfang des Gegenterms die Zahlen stark mitbestimmen. Das wird offen
  gezeigt (Varianten unten).
- **[F9] Umfang: nur der Metrik-Teil.**
  - CT = Pi0 B0 (B0^T Pi0 B0)^-1 B0^T Pi0 mit Pi0 = Pi(0) (15 x 15, reell). Dann gilt (Pi0 - CT) B0 = 0: Konstante
    Metriken kosten bei k = 0 nichts (wie bei Regge), die 5 Gittermoden behalten ihre k = 0-Steifigkeit.
  - Begruendung: Zieht man Pi(0) ganz ab, werden alle 15 Moden bei k -> 0 weich. Fuenf zusaetzliche masselose Felder
    sind keine Metrik-Theorie mehr, und das Schur-Komplement wird zu O(k^2)/O(k^2), richtungsabhaengig und nicht
    analytisch.
  - "Ganz" wird beschreibend mitgerechnet (Variante G).
- **[K2, Kartenberichtigung] Lage:** Die Karte sagt "vor Ort (Kanten mit demselben Fusspunkt, also k-unabhaengig)".
  - Ein reiner Fusspunkt-Gegenterm bricht die Inversionssymmetrie des Kuhn-Netzes: Die Inversion bildet Kantenpaare
    mit gemeinsamem Anfang auf Paare mit gemeinsamem Ende ab.
  - In der Mittelpunkts-Konvention der Kette hat er die Form CT_dd' e^{ik.(d'-d)/2}. Er bringt also einen ungeraden,
    rein imaginaeren O(k)-Anteil in eine sonst reelle, gerade Form. Mit voller Subtraktion waere die Form bei O(k)
    indefinit.
  - Berichtigung: je zur Haelfte am gemeinsamen Anfangs- und am gemeinsamen Endpunkt ("vor Ort" an den Ecken). Das
    ergibt in der Mittelpunkts-Konvention CT_dd' cos(k.(d'-d)/2). Diese Fassung ist lokal, k-unabhaengig je
    Ecke und inversionssymmetrisch.
  - Urteil nach Kartenwortlaut: mit der reinen Fusspunkt-Lage (Variante R2), ebenfalls mit Metrik-Teil.
- **Varianten (alle mit derselben Kette):**
  - P (Plan): Pi^mid(k) - CT cos(k.(d'-d)/2)
  - R2 (Kartenwortlaut): Pi^mid(k) - CT e^{ik.(d'-d)/2}
  - R1 (Taylor-Lesart "Pi(k) - Pi(0)" in der Kettenkonvention, kein lokaler Gitterterm): Pi^mid(k) - CT
  - G (ganz): Pi^mid(k) - Pi0 cos(k.(d'-d)/2)
  - L (Laengen statt Quadrate): Pi^l = J Pi^mid J + 2 diag(dGamma/ds), J = diag(2 l), B0^l = J^-1 B0, CT^l aus Pi^l(0),
    symmetrisch gelegt. Ohne volle Subtraktion haengt der Metrik-Teil von der Variablenwahl ab [M].
  - U (roh, ohne Gegenterm)
- **Kette (wie REGGE-4D-1, komplex-hermitesch erweitert):**
  - h als 10-Vektor (Frobenius-Orthonormalbasis), delta s_d = d^T h d (B0, Mittelpunkts-Konvention).
  - Schur-Komplement ueber das orthogonale Komplement C von range(B0) (5-dim), Pseudoinverse (Eigenwerte unter
    1e-8 max verworfen). Mit dem Metrik-Teil wirkt das Schur-Komplement erst in O(k^4); bei R2 und G nicht.
  - Projektoren P2, P1, P0s, P0w; c2 = Re tr(P2 K)/(5 k^2), c0s = s^T K s/k^2, r = c0s/c2, Spin-2-Eigenwerte.
  - Direkte Form B0^T Pi_sub B0 wird mitberichtet.
- **[F10] Eichsteifigkeit (IN4):** Eichmoden u_d = sin(k.d/2) d.xi (4 Stueck, Mittelpunkts-Konvention). Spin-2-Moden
  B0 Q2 (Q2 Orthonormalbasis von range P2). Beide im vollen 15-dim Kantenraum, ohne Schur.
  - Steifigkeit je Einheit Kantenlaengen-Aenderung: verallgemeinerte Eigenwerte von (U^+ Pi_sub U, U^+ W U) mit
    W = diag(1/(4 s_d)), weil abs(delta l)^2 = sum abs(delta s_d)^2/(4 s_d).
  - kappa2 = Mittel der 5 Spin-2-Werte. Kennzahl: max abs(kappa_eich)/kappa2.
  - Beschreibend auch je Einheit delta s.
- **[F11] Volumen (IN5):** Metrik-Komponenten A = B0^T Pi0 B0 und Vm = B0^T V''(0) B0 (10 x 10). alpha nach kleinsten
  Quadraten, Kennzahl ||A - alpha Vm||_F/||A||_F. Beschreibend: Schur-Fassung und die vollen 15 x 15.

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| IN0 | Kontrollen 4D: P1-Symbol des flachen Kuhn-Netzes = sum_mu 4 sin^2(q_mu/2) auf <= 1e-12; Pi(k) hermitesch auf <= 1e-9 (relativ) | 70 % |
| IN1 | Teil A (2D): Steifigkeit der konformen Mode pro Flaeche und k^2 = -1/(24 pi) auf 3 % beim kleinsten ausgewerteten k im Fenster m << k << 1 | 55 % |
| IN2 | Teil B: Die induzierte Spin-2-Steifigkeit c2 ist positiv, mit demselben Vorzeichen wie in REGGE-4D-1 | 60 % |
| IN3 | [H] Teil B: Nach dem Gegenterm gilt c0s/c2 = -2 auf 10 % (k -> 0), also Einsteins 1/2 aus Materie | 25 % |
| IN4 | [H] Teil B: Nach dem Gegenterm sind die vier Knotenverschiebungs-Moden weich: Steifigkeit <= 5 % der Spin-2-Steifigkeit bei abs(k) = 0,2 (je Einheit Kantenlaengen-Aenderung) | 25 % |
| IN5 | [H] Teil B: Pi(0) weicht in Metrik-Komponenten um mehr als 10 % (relative Frobenius-Norm) von einem Vielfachen der zweiten Variation des 4-Volumens ab | 70 % |

- **Gemeinsames Tor [F12]:** Die Torus-Gegenprobe (Abschnitt 7, K1 bis K4) muss bestehen: relative Abweichung
  Blasensumme gegen direkte zweite Differenz von 1/2 log det <= 1e-5 in allen Faellen, ebenso der Tadpole-Vektor gegen
  erste Differenzen. Sonst sind IN1 bis IN5 "nicht auswertbar" (Kette falsch).
- **IN0 eingetroffen**, wenn beide Teile gelten:
  - (a) max abs(K(q) - sum 4 sin^2(q_mu/2)) <= 1e-12 auf 64 Zufalls-q, n = 4, masselos, aus den lokalen Matrizen
    (Karte).
  - (b) max ueber alle gerechneten 4D-k (alle Massen und Gitter) von max abs(Pi - Pi^+)/max abs(Pi) <= 1e-9
    (Fusspunkt-Konvention, roh).
- **IN1 eingetroffen**, wenn abs(c_P/(-1/(24 pi)) - 1) <= 0,03 bei L = 1024, n = 8, Richtung (1,0) [F3, F4].
- **IN2 eingetroffen**, wenn c2 > 0 (Schur, Variante P) fuer alle 8 Richtungen, abs(k) in {0,05; 0,1; 0,2} und
  m^2 in {0,01; 0,04}. "Dasselbe Vorzeichen wie REGGE-4D-1" heisst c2 > 0 in der Konvention H = Hess(euklidische
  Wirkung), wie dort.
- **IN3 eingetroffen**, wenn abs(r/(-2) - 1) <= 0,10 (Schur, P) fuer alle 8 Richtungen bei abs(k) = 0,05 (kleinster
  Leiterwert der Kette, [F7]) und beiden Massen.
- **IN4 eingetroffen**, wenn bei abs(k) = 0,2 fuer alle 8 Richtungen und beide Massen gilt: kappa2 > 0 und
  max abs(kappa_eich) <= 0,05 kappa2 (P, je Einheit delta l, [F10]).
- **IN5 eingetroffen**, wenn die Kennzahl aus [F11] fuer beide Massen > 0,10 ist.
- **Gitterkonvergenz [F13]:** IN2 bis IN5 werden auf L_q = 64 und 48 ausgewertet. Unterscheiden sich die Urteile, ist
  die Nummer "nicht auswertbar".
- **Urteil nach Kartenwortlaut:** IN2 bis IN4 zusaetzlich mit R2 (reine Fusspunkt-Lage) berichtet; IN1 nach
  Kartenwortlaut ist c_P (Abschnitt 3).
- Urteile mechanisch durch code/induziert_auswertung.py nach lauf-69/auswertung.json.

- **Leitungszusatz (Nachricht der Leitung waehrend des Plantexts, vor dem Einfrieren; beschreibend, nicht
  geurteilt):** Richtungsabhaengigkeit von c2 und c0s/c2 im kleinsten k (abs(k) = 0,025 und 0,05), getrennt nach
  Achse (1,0,0,0), Flaechendiagonale (1,1,0,0) und (1,-1,0,0), Raumdiagonale (1,1,1,0) und Hyperdiagonale (1,1,1,1).
  Dazu die Streuung ueber alle 8 Richtungen (Spanne/abs(Mittel) und Standardabweichung/abs(Mittel)), je Variante und
  Masse. Vergleich: REGGE-4D-1 bei eingegebener Regge-Wirkung. Plan, Schwellen und Urteile bleiben davon unberuehrt.

## 7. Kontrollen

- **K1 bis K4, Torus-Gegenprobe (Tor):** Blasensumme auf dem Torus (exakt) gegen direkt per slogdet gerechnetes
  1/2 log det K. Zweite Differenz entlang reeller ebener Wellen delta s = Re(u e^{ik.x}) mit Zufalls-u (je 2), Schritt
  1e-2 und Richardson.
  - 2D L = 16 masselos (det'), k = 2 pi (1,0)/16 und 2 pi (3,2)/16
  - 2D L = 16, m^2 = 0,04
  - 3D L = 6, m^2 = 0,04
  - 4D L = 5, m^2 = 0,04 und masselos (det'), k = 2 pi (1,0,0,0)/5 und 2 pi (1,2,0,1)/5 bzw. (2,1,1,0)/5
  - Dazu die konforme Mode (Ecken-Skalierung) in 2D L = 16 direkt gegen die Formel aus Abschnitt 3 und der
    Tadpole-Vektor gegen erste Differenzen.
- **K5:** lokale Ableitungen analytisch gegen komplexen Schritt bzw. zentrale Differenz komplexer Schritte (n = 2, 3,
  4, alle Typen, leicht verzerrte Simplizes, m^2 = 0,04).
- **K6:** Symbol (IN0 a), dazu die Stencil-Gewichte der Diagonalkanten.
- **K7:** Imaginaerteil von Pi^mid (soll Rundungsrauschen sein), Hermitezitaet, Gitterkonvergenz 32/48/64, Schur gegen
  direkt.

## 8. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde37-induziert/, nur ueber kleintest.sh, Spuren cpu3 und cpu4, hoechstens
  zwei zugleich.
- **Rauch** (vor dem Einfrieren):
  - kontrolle (vollstaendig)
  - teilA rauch (L = 64, 128)
  - teilB rauch (n = 4, L_q = 16, 3 Richtungen, abs(k) = 0,05 und 0,2)
  - Probe der Auswertung auf den Rauchdaten
- **Haupt:**
  - kontrolle; teilA
  - teilB n = 4 mit m^2 = 0,01 und 0,04 bei L_q = 64 und 48
  - beschreibend: n = 4 L_q = 32; n = 3 L_q = 128; m^2 = 0,0025
  - danach auswertung
- Jeder Lauf deutlich unter 10 min (geschaetzt 1 bis 4 min).
- **Abbruch:** Besteht die Torus-Gegenprobe nach zwei ernsthaften Versuchen nicht, ist Teil B "nicht gerechnet".
  Code nach dem Einfrieren nur bei echten Fehlern aendern, offengelegt.

## 9. Agenten-Vorhersagen (vor jeder Rechnung zur Karte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | IN0 eingetroffen (Symbol exakt [M]; Hermitezitaet strukturell) | 95 % |
| A2 | Torus-Gegenprobe besteht auf <= 1e-7 | 80 % |
| A3 | IN1 nicht eingetroffen. Der Gitter-Regulator ist nicht kovariant; lokale Terme (d sigma)^2 mit gitterabhaengigem Koeffizienten addieren sich zu Polyakov [M, H]. Dazu hat das 2D-Kuhn-Netz eine anisotrope Vakuumspannung (dGamma/ds_(1,0) = (2/pi - 1)/4 ~ -0,091 [M]). Sie macht die Antwort von der Fortsetzung zweiter Ordnung und von der Richtung abhaengig | 70 % |
| A4 | c_P haengt deutlich von der Richtung ab: Spanne ueber (1,0), (1,1), (1,-1) > 10 % | 75 % |
| A5 | IN2 eingetroffen (c2 > 0 in P) | 55 % |
| A6 | IN3 nicht eingetroffen | 85 % |
| A7 | IN4 nicht eingetroffen: Das Gitter bricht die Umbenennung bei O(k^2) mit Koeffizienten derselben Ordnung wie c2 | 85 % |
| A8 | IN5 eingetroffen: Entlang der Spur ist Pi(0) negativ (Gamma ~ log der Skala), das Volumen positiv; Proportionalitaet scheitert schon am Vorzeichenmuster [M] | 95 % |
| A9 | Die Varianten P, R1, R2, G, L unterscheiden sich in r bei abs(k) = 0,05 um mehr als 20 % | 75 % |
| A10 | c2 haengt schwach von der Masse ab (m^2 0,01 gegen 0,04: < 10 %) | 60 % |

## 10. Rechenaufwand (gemessen im Rauchlauf)

- teilB n = 4, L_q = 64: Gitter 2,1 s, 7 k-Punkte 6,7 s, also rund 1 s je k-Punkt. Ein Hauptlauf mit 41 k-Punkten
  braucht rund 45 s. kontrolle 34 s, teilA (L = 64, 128) unter 1 s.

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- Abschnitte 1 bis 9 sind nach den Rauchlaeufen in Schwellen, Urteilsregeln und Festlegungen [F1] bis [F13]
  unveraendert. Ergaenzt wurden vor dem Einfrieren nur der Leitungszusatz (beschreibend) und Teil A2 (beschreibend).
- **kontrolle-r1** (03:51:54 bis 03:52:28, cpu3, rc = 0):
  - Ableitungen analytisch gegen komplexen Schritt <= 7,8e-16, gegen zentrale Differenz komplexer Schritte <= 3,5e-8.
  - Symbol <= 5,3e-15; Stencil-Gewicht der Diagonalkanten 0,0 (n = 2, 3, 4).
  - Torus-Gegenprobe: <= 4,5e-8 (2D), <= 5,7e-7 (3D), aber bis 6,8e-6 in 4D. Die Richardson-Schaetzung zeigte, dass
    das der Abbruchfehler O(eps^4) der zweiten Differenz mit eps = 1e-2 war.
  - **Code geaendert:** Schritt 1e-2 -> 2,5e-3 (Torus-Gegenprobe, konforme Mode, Massenterm). Die Schwelle 1e-5 blieb.
- **kontrolle-r2** (03:55:01 bis 03:55:36, cpu3, rc = 0): Torus-Gegenprobe <= 2,5e-8 in allen Faellen, auch fuer die
  konforme Mode (2D, L = 16) und den Tadpole-Vektor (<= 1e-9). Das Tor ist damit vor dem Einfrieren sichtbar
  bestanden.
- **teilA rauch** (03:55:00 bis 03:55:01, cpu3) und **Probe p1** der Auswertung (03:55:48 bis 03:55:53, cpu3):
  - L = 64 und 128, Richtung (1,0), kleinstes k = 0,049 (L = 128): c_P = +0,1249, c_D = -0,0416, c_s = +0,1703,
    l-linear +0,1476. Polyakov waere -0,0133.
  - (1,1): c_P = +0,079; (1,-1): c_P = +0,170. l-linear ist in allen drei Richtungen 0,1475 bis 0,1476.
  - Der Tadpole-Anteil c_P - c_s = -0,045 (Achse) passt zur Schreibtischrechnung von A3.
  - **IN1 ist damit vor dem Einfrieren als "nicht eingetroffen" absehbar** (Faktor ~ -9 statt 1). A3 und A4 sind
    ebenfalls absehbar.
  - IN0 (a) und die Hermitezitaet sind in der Probe erfuellt (5,3e-15; 3e-16).
- **Teil A2 rauch** (04:00:26 bis 04:00:27, cpu3; Probe p2 04:00:39 bis 04:00:50, cpu4), L = 128,
  abs(k) = 0,20 bis 0,59: lambda = 0,998, Rest 0,4 %.
  - Die 4phi-Harmonische trifft Polyakovs -1/(48 pi) also schon auf dem groben Gitter.
  - Danach habe ich Teil A2 nicht mehr geaendert (Schalen, Fit-Modell, Gitter L = 512 und 1024 standen vorher im
    Code).
- **teilB rauch:** n = 4 mit m^2 = 0,04 bei L_q = 16 und 64 (3 Richtungen, abs(k) = 0,05 und 0,2, Zeitmessung),
  dazu m^2 = 0,01/0,04 bei L_q = 16 und 12 fuer eine Codeprobe der Urteilslogik ("probe16", L_q 16/12 statt 64/48).
  - Gesehen habe ich nur Laufzeiten, rc und das Durchlaufen der Auswertung.
  - **Die 4D-Zahlen (c2, r, Eichsteifigkeit, IN5) und die Probe-Urteile zu IN2 bis IN5 habe ich vor dem Einfrieren
    nicht angesehen.**
