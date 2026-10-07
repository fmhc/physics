# LAMBDA-1: Plan (Code-Agent, Runde 36, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 00:17:02 CEST, Plantext ab 00:43:01 CEST (date).
  Zeitbox 120 min, also bis 02:17 CEST.
- **Grundlage:** KARTE.md (L0 bis L4; Vorhersagen, Wahrscheinlichkeiten und Schwellen unveraendert uebernommen),
  RUNDE-36/tensor-eis-n/ (PLAN.md, ERGEBNIS.md, code/tn.py, code/tn_auswertung.py).
- **Code:** code/lam.py ist eine Kopie von tn.py (eingefroren 20261004-000130, sha256 4952a92e...). Geaendert ist nur, dass
  der Koeffizient c des Spurglieds frei waehlbar ist (in tn.py schon als Argument `lam` von `hesse` angelegt); ergaenzt
  sind die c-Abtastung, die Zwangsflaechen-Dynamik, die Modenzerlegung, der volle statische KKT mit A(c), die exakte
  Pruefung je c und das Ortsraum-Spektrum je c. code/lam_auswertung.py ist neu (Helfer aus tn_auswertung.py).
- **Kennzeichen:**
  - [S] an der Quelle gelesen (mit Angabe);
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher;
  - [H] Hypothese;
  - [M] Mathematik, hier vorab hergeleitet;
  - [F] eigene Festlegung, wo die Karte offen ist.
- **Quellen, gelesen 00:35 bis 00:42 CEST** (5 von 6 erlaubten Abrufen, export.arxiv.org/api und arxiv.org/abs; die
  Wiedergabe lief ueber das WebFetch-Werkzeug):
  - Horava, "Quantum Gravity at a Lifshitz Point", arXiv:0901.3775 [S, Abstract]. Der Abstract nennt lambda nicht.
  - Charmousis, Niz, Padilla, Saffin, "Strong coupling in Horava gravity", arXiv:0905.2579 [S, erster Satz des Abstracts]:
    "two different strong coupling problems, extending all the way into the deep infra-red".
  - Blas, Pujolas, Sibiryakov, "On the Extra Mode and Inconsistency of Horava Gravity", arXiv:0906.3046, JHEP 0910:029
    [S, Abstract]: "We uncover the additional scalar degree of freedom arising from the explicit breaking of the general
    covariance"; "At linear level the mode is manifest only around spatially inhomogeneous and time-dependent
    backgrounds"; "the mode develops very fast exponential instabilities at short distances"; die "projectable"
    Fassung sei "a certain limit of the ghost condensate model".
  - Bogdanos, Saridakis, "Perturbative instabilities in Horava gravity", arXiv:0907.1636, CQG 27:075005 [S, Abstract]:
    "plagued by ghost-like scalar instabilities in the range of parameters which would render it power-counting
    renormalizable".
  - Die Dispersionsformel des Skalarmodus und die lambda-Bereiche (Geist bzw. Instabilitaet) stehen in keinem der
    Abstracts. Sie bleiben [L].
- Alle Rechnungen sind synthetische Gitterrechnungen, keine Messdaten. Einheiten J = g = 1.

## 1. Zuordnung c <-> lambda (geprueft)

- **Code:** In tn.py ist A = J (1 - lam t t^T), t = (1,1,1,0,0,0) in der Frobenius-Orthonormalbasis. Damit gilt
  1/2 E.A.E = (J/2) [E^ij E^ij - lam (E^ii)^2]. Der Kartenparameter c ist also genau `lam`; Vorzeichen und Normierung
  sind die des Impulsbilds pi^ij pi_ij - c pi^2 mit E^ij <-> pi^ij (kanonisch konjugiert zu a_ij, Gl. 12).
- **Gu/Wen:** Gl. 32 lautet H = (J/2) [(E^ij)^2 - (1/2) (E^ii)^2] + (g/2) a_ij R^ij [S, zitiert nach TENSOR-EIS-N
  PLAN 1.3; dort an der PDF gelesen, hier nicht erneut]. TENSOR-EIS-N K3 hat die Code-Matrix gegen Gu/Wens k-Raum-Matrix
  S. 19 auf 1,3e-15 bestaetigt: Der Diagonalblock X_J = (1/4) [[1, -1, -1], ...] ergibt A = 1 - (1/2) (Einsen)
  [S + E]. **Gu/Wens Wert ist c = 1/2.**
- **Horava [L]:** kinetischer Teil der Lagrangedichte (2/kappa^2) sqrt(h) N (K_ij K^ij - lambda K^2). Die Inverse der
  Superform X -> X - lambda tr(X) delta auf symmetrischen 3x3-Matrizen ist Y -> Y + (lambda/(1 - 3 lambda)) tr(Y) delta
  [M]. Im Impulsbild steht deshalb pi^ij pi_ij - (lambda/(3 lambda - 1)) pi^2. Also gilt **c = lambda/(3 lambda - 1),
  lambda = c/(3 c - 1)**, wie auf der Karte. Der Gesamtfaktor spielt keine Rolle, c ist ein Verhaeltnis.
- **Zuordnung der Karte bestaetigt.** Zusaetzlich [M]: (lambda - 1)/(3 lambda - 1) = 1 - 2c exakt.

  | c | 0,30 | 1/3 | 0,40 | 0,45 | 0,48 | 0,49 | 0,50 | 0,51 | 0,52 | 0,55 | 0,60 | 0,70 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | lambda | -3 | Pol | 2 | 1,2857 | 1,0909 | 1,0426 | 1 | 0,9623 | 0,9286 | 0,8462 | 0,75 | 0,6364 |
  | 1 - 2c | 0,4 | 1/3 | 0,2 | 0,1 | 0,04 | 0,02 | 0 | -0,02 | -0,04 | -0,1 | -0,2 | -0,4 |

  - c < 1/3 entspricht lambda < 0, c = 1/3 dem Pol lambda = unendlich. Die Kartenbereiche "lambda > 1 <-> 1/3 < c < 1/2"
    und "1/3 < lambda < 1 <-> c > 1/2" stimmen.
- **Warum genau 1/2 [M]:** Die Skalarbedingung erzeugt die Eichung Gl. 23, delta E^ij = (delta_ij d^2 - d_i d_j) f_0.
  Auf ker Kv (d_i E^ij = 0) gilt bis auf totale Ableitungen delta [E^ij E^ij - c (E^ii)^2] = 2 (1 - 2c) E^ii d^2 f_0. Das
  Spurglied ist also nur bei c = 1/2 eichinvariant. Das ist die Gitterfassung von "lambda = 1 <-> volle
  Diffeomorphismen-Invarianz" [L].

## 2. Schreibtisch [M] (vor jeder Rechnung)

Je q != 0 im k-Rahmen (n = K/|K|, K_a = 2 sin(q_a/2), wie TENSOR-EIS-N Abschnitt 3):

- Basis: TT (zwei Richtungen), V (zwei), T = (delta - n n)/sqrt2, L = n n; die Spur ist t = sqrt2 T + L.
- **A(c)** ist blockdiagonal in (TT | T, L | V):
  - TT: J;
  - (T, L): J [[1 - 2c, -sqrt2 c], [-sqrt2 c, 1 - c]], dazu U_v K^2 im L-L-Eintrag;
  - V: J plus Strafterm.
- **B:** TT g K^2; T: b = -g K^2 + 2 U_s K^4; L, V: 0.
- **Spektrum omega^2 = eig(A B):**
  - g J K^2 (zweimal, TT, unabhaengig von c);
  - **omega_s^2 = J (1 - 2c) b** (T-L-Block);
  - 0 (dreimal; fuer c != 1/2 halbeinfach, bei c = 1/2 vier Nullen mit Jordankette).
  - U_v tritt nicht auf.
- **P0 (ohne Strafterme):** omega_s^2 = -(1 - 2c) g J K^2 = -((lambda - 1)/(3 lambda - 1)) g J K^2.
  - Das ist genau die Horava-IR-Formel der Karte [L] mit xi = g J (Gravitonmodus omega^2 = g J K^2, Gl. 35) und k -> K.
    Es gilt an jedem Gitter-q, nicht nur bei kleinem k.
  - **c < 1/2** (lambda > 1 oder lambda < 0): Wachstum an jedem q != 0 mit gamma(q) = |K| sqrt((1 - 2c) g J); das
    Maximum liegt an der Zonenecke K^2 = 12, also gamma_max = sqrt(12 (1 - 2c)).
  - **c > 1/2** (1/3 < lambda < 1): omega_s^2 > 0, kein Wachstum. Die Energie im T-Sektor, 1/2 J (1 - 2c) E_T^2 +
    1/2 b a_T^2, ist dann negativ definit: ein Geist.
- **P1 (Gu/Wen-Gittermodell, U_v = U_s = 1):** omega_s^2 = -((lambda - 1)/(3 lambda - 1)) (xi K^2 - eta K^4) mit
  eta = 2 U_s J. Der Strafterm (U_s/2)(R^ii)^2 wirkt wie ein R^2-Glied (z = 2) im Horava-Potential [L?].
  - **c < 1/2:** Wachstum nur bei K^2 < g/(2 U_s) = 1/2 (kleines k). Das Maximum liegt bei K^2 = 1/4; auf dem Gitter
    L = 32 ist das K^2 = 0,22910 (n = (2, 1, 1) und Lagen), also gamma_max = sqrt(0,124126 (1 - 2c)).
  - **c > 1/2:** Wachstum bei K^2 > 1/2, Maximum an der Zonenecke: gamma_max = sqrt(276 (2c - 1)). Der Geist trifft
    auf die positive Strafenergie 2 U_s K^4; das erklaert das Wachstum, das TENSOR-EIS-N bei 0,51 sah (2,35).
- **Zusammensetzung des schnellsten Modus (P0 und P1):**
  - a-Seite: a_L/a_T = -sqrt2 c/(1 - 2c), kein TT-Anteil. Der Anteil der Skalarbedingung (Masse) ist
    1/(1 + 2c^2/(1 - 2c)^2), unabhaengig von K und U.
  - E-Seite: nur E_T, also die Eichrichtung von Gl. 23; E_T = -b a_T/s_D. Kein Anteil an der Verletzung der
    Vektorbedingung.
  - Abstand von Z: f_off^2 = 1/(1 + 2c^2/(1 - 2c)^2 + |b|/(J |1 - 2c|)).
  - Fuer c -> 1/2 wird der Modus zur reinen Eichrichtung. Das ist das Gitterbild davon, dass Horavas Zusatzmodus bei
    lambda = 1 zur Eichfreiheit der Zeitumparametrisierung wird [L].
- **(b) Zwangsflaeche Z = ker c x ker Kv (ohne Quelle):**
  - Die orthogonal projizierte Bewegung hat M2 M1 = diag(g J K^2, g J K^2, 0) in der Basis (TT, TT, T). Fuer kein c und
    keine Strafe gibt es Wachstum; die Strafterme verschwinden auf Z.
  - Unter der freien Bewegung ist Z nur bei c = 1/2 invariant. Fuer c != 1/2 erzeugt E_T eine Verletzung der
    Skalarbedingung, d a_T/dt = J (1 - 2c) E_T.
  - Dirac (linear): Fuer c != 1/2 kommt die Folgebedingung E_T = 0 hinzu. Die Skalarbedingung wird zusammen mit E_T
    zweiter Klasse, die Eichung Gl. 23 entfaellt. Der invariante Unterraum V* = Z mit E_T = 0 hat die Dimension 7
    (c != 1/2) bzw. 8 (c = 1/2); Wachstum gibt es dort nicht.
  - Horava-Bild [L, gestuetzt durch S]: Projizierbar (keine lokale Hamilton-Bedingung) entspricht der freien Dynamik
    P0 mit Skalarmodus. Nicht projizierbar (lokale Bedingung) entspricht dem strengen Z: Um den flachen Hintergrund gibt
    es linear keinen Skalarmodus. Das passt zu Blas/Pujolas/Sibiryakov [S]: "At linear level the mode is manifest only
    around spatially inhomogeneous and time-dependent backgrounds".
  - **Energie auf Z:** A auf ker Kv = diag(J, J, J (1 - 2c)). Fuer c > 1/2 liegt eine negative Richtung (E_T) auf Z: Die
    Energie ist dort nach unten unbeschraenkt, waechst linear aber nicht. B auf ker c ist >= 0.
- **(c) Statik:** c steht nur in A (E-Teil), die Quelle nur im a-Teil (c.a = rho). Der E-Teil hat die rechte Seite 0,
  also E = 0.
  - Daraus folgt U(r) = -(g/2) m1 m2 G_Delta(r) -> -1/(8 pi r) und **G_eff(c) = 1/(8 pi) fuer jedes c**.
  - Der statische Wert ist auf Z fuer c <= 1/2 ein Minimum (bei 1/2 bis auf Eichung), fuer c > 1/2 ein Sattel in
    Richtung E_T.
  - Horava-Bild [L?]: lambda steht nur bei K_ij (Zeitableitungen); die statische Newton-Grenze haengt nicht von lambda
    ab.
- **Folge [M]:** L0 bis L4 sind alle vorab ableitbar. Erwartet ist "eingetroffen" fuer alle fuenf.
  - L1: Exponent exakt 0,5 in P0 und P1.
  - L2: Delta = 1 (P0) und 0,979 (P1).
  - L4: konstant und damit selbsterfuellend.
  - Die Rechnung prueft also Rekonstruktion, Schreibtisch und Numerik, keine offene Frage. Scheitern koennen nur Code und
    Herleitung.

## 3. Agenten-Vorhersagen (vorab, mit Zahl; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| A1 | P0: gamma_max = sqrt(12 (1 - 2c)) fuer c < 1/2, also 2,1909 / 2,0000 / 1,5492 / 1,0954 / 0,6928 / 0,4899; 0 fuer c >= 1/2. Ort: Zonenecke (q = -pi in allen drei Achsen); Anteil wachsender q 100 % (c < 1/2) bzw. 0 %. Abweichung <= 1e-10 relativ |
| A2 | P1: c < 1/2: sqrt(0,124126 (1 - 2c)) = 0,22282 / 0,20341 / 0,15756 / 0,11141 / 0,07046 / 0,04982 bei K^2 = 0,22910; c > 1/2: sqrt(276 (2c - 1)) = 2,3495 / 3,3227 / 5,2536 / 7,4297 / 10,507 an der Zonenecke; c = 1/2: 0 |
| A3 | Volles Spektrum gleich der Formel aus Abschnitt 2 (sortiert, relativ zu \|A\|\|B\|): <= 1e-10 fuer c != 1/2 in P0 bis P6, <= 1e-6 bei c = 1/2 (Jordan-Rundung) |
| A4 | Zusammensetzung: a-Seite Anteil Skalarbedingung 0,4706 / 0,3333 / 0,1111 / 0,02410 / 0,003460 / 0,000832 (c < 1/2) bzw. 0,000768 / 0,002950 / 0,01626 / 0,05263 / 0,1404 (c > 1/2, P1), auf 1e-8; Rest Eichung Gl. 15. E-Seite Eichrichtung Gl. 23 = 1 auf 1e-10; TT- und Vektoranteil < 1e-10; f_off >= 0,008 ueberall |
| A5 | Kleines k: gamma/\|K\| am kleinsten Gitter-q gleich sqrt(1 - 2c) (P0) bzw. sqrt((1 - 2c)(1 - 2 K^2)) mit K^2 = 0,038429, also Faktor 0,96080 (P1); auf dem [100]-Schnitt bei \|q\| = 1e-3 gleich sqrt(1 - 2c) auf 1e-6 (beide). Fuer c > 1/2 kein Wachstum bei kleinem k |
| A6 | Projektion (b): kein Wachstum; -Re(omega^2)/s <= 1e-12. Invarianzdefekt bei c = 1/2 <= 1e-14, sonst ungefaehr \|1 - 2c\|/max(1, \|1 - 3c\|) bei kleinem q. Dirac: Dimension 7 (c != 1/2), 8 (c = 1/2), einheitlich ueber q; kein Wachstum |
| A7 | Energie auf Z: negative A-Richtung an 100 % der q fuer c > 1/2, an 0 % fuer c <= 1/2; kleinster Wert J (1 - 2c), z. B. -0,4 bei c = 0,70; B auf ker c ohne negative Richtung |
| A8 | Statik: 8 pi G_eff in [0,997; 1,003]; Kernabweichung delta_c <= 1e-12 und max\|E\|/max\|kappa\| <= 1e-12 fuer alle c; Abweichung von -1/(8 pi r) ab r = 8 etwa 0,41 % (wie TENSOR-EIS-N); U_korr gegen TENSOR-EIS-N <= 1e-9 relativ |
| A9 | Exakt: charakteristisches Polynom x^3 (x - K^2)^2 (x - s) in allen 144 Faellen (12 c, P0/P1, 6 Punkte). Negative Wurzel: P0 an allen Punkten fuer c < 1/2, an keinem fuer c >= 1/2; P1 nach dem Vorzeichen von s = (1 - 2c)(2 K^4 - K^2). Keine nicht reellen Wurzeln |
| A10 | Ortsraum L = 6 bei c = 0,45 und 0,55 (P0, P1): sortierte Realteile gegen Fourier <= 1e-8 relativ zu max omega^2. Kleinstes omega^2: P0/0,45 = -1,2; P0/0,55 = 0; P1/0,45 = 0 (auf L = 6 gilt K^2 >= 1, also kein Wachstum); P1/0,55 = -27,6 |

## 4. Messvorschriften

### 4.1 Freie Dynamik (a)

- **Saetze [F1]:**
  - P0: U_v = U_s = 0, reine Form Gl. 32 mit c;
  - P1: U_v = U_s = 1, Gu/Wens U ~ J ~ g, wie die TENSOR-EIS-N-Abtastung "mit U = 1", in der 0,51 wuchs;
  - P2 bis P6 wie TENSOR-EIS-N, nur fuer L0 bei c = 1/2, sonst beschreibend.
- **Gitter [F7]:** BZ mit L = 32, alle 32 767 q != 0, q_a = 2 pi n/32 mit n = -16 .. 15 (die Zonenecke -pi ist dabei).
- **Je q:** omega^2 = eig(A(c) B), 6x6, wie TENSOR-EIS-N.
  - Wachstumstest je Eigenwert: -Re(omega^2) > tau s oder abs(Im(omega^2)) > tau s, mit tau = 1e-6 und
    s = ||A||_2 ||B||_2 (unveraendert aus TENSOR-EIS-N).
  - Polynomiales Wachstum zaehlt nicht [F8 = TENSOR-EIS-N F7].
- **Wachstumsrate:** gamma = abs(Im sqrt(omega^2)) (Hauptzweig) fuer Eigenwerte, die den Test bestehen, sonst 0.
  - Das ist der groesste positive Realteil der Eigenwerte der Bewegungsmatrix D = [[0, A], [-B, 0]].
  - gamma(q) = Maximum ueber die Eigenwerte, gamma_max(c) = Maximum ueber q.
- **Lage:** q* = argmax (erstes nach Index), K^2(q*), Anteil der q mit Wachstum.
- **Zusammensetzung an q*:**
  - Eigenvektor a von A B zum Eigenwert mit groesstem gamma; E = -B a/s_D mit s_D = sqrt(-omega^2) (Hauptzweig);
    z = (a, E).
  - Orthogonalprojektoren in der Frobenius-Orthonormalbasis:
    - a-Seite: Skalarbedingung (Richtung c), Eichung Gl. 15 (Bild G15), Helizitaet 2 (S_a = TT);
    - E-Seite: Eichrichtung Gl. 23 (G23), Verletzung der Vektorbedingung (Bild Kv^T), Helizitaet 2 (S_E).
  - Anteile je Seite (je Seite normiert) und gesamt (euklidisch in (a, E), J = g = 1). f_off = sqrt(Anteil Skalar +
    Anteil Vektor) des Gesamtvektors, also der Abstand von z zu Z relativ zu |z|.
- **Kleines k:** gamma am kleinsten Gitter-q (2 pi/32, 0, 0), geteilt durch |K|; ebenso auf dem [100]-Schnitt bei
  |q| = 1e-3.
- **Vergleich mit Horava:**
  1. volles Spektrum gegen die Formel aus Abschnitt 2 (sortiert, relativ zu s) fuer alle c, P0 bis P6, auf dem Gitter und
     auf den Schnitten [100] und [111];
  2. gamma_max gegen die Horava-IR-Kurve sqrt(12 max(0, (lambda - 1)/(3 lambda - 1))) (P0, xi = g J) und gegen die Kurve
     mit z = 2-Glied (P1);
  3. Koeffizient bei kleinem k, gamma/|K|, gegen sqrt(max(0, (lambda - 1)/(3 lambda - 1))).

### 4.2 Zwangsflaeche (b) [F5]

- Z = {a in ker c} x {E in ker Kv}, ohne Quelle. Orthonormalbasen Z_a (6x5) und Z_E (6x3) per SVD.
- **Hauptmass (wie im Auftrag):** orthogonale Projektion der Bewegung auf Z.
  - M1 = Z_a^T A Z_E, M2 = Z_E^T B Z_a; omega^2 = eig(M2 M1) (3x3) und eig(M1 M2) (5x5).
  - Derselbe Wachstumstest mit s = ||M1|| ||M2||; gamma_Z(c) ist das Maximum.
  - Je c fuer P0 und P1 gerechnet (die Strafterme fallen auf Z heraus, das wird so geprueft).
- **Beschreibend:**
  - Eigenwerte der 8x8-Matrix [[0, M1], [-M2, 0]], max Re/||D||;
  - Invarianzdefekt ||(1 - P_Z) D P_Z|| / ||D||;
  - Energie auf Z: Eigenwerte von Z_E^T A Z_E und Z_a^T B Z_a.
- **Gegenprobe Dirac:**
  - groesster unter D invarianter Unterraum V* in Z, iteriert Q <- Q ker((1 - Q Q^T) D Q), SVD-Toleranz 1e-9 ||D||;
  - Bewegung auf V*: Wachstum, wenn ein Eigenwert von (Q^T D Q)^2 einen Realteil > tau ||D||^2 oder einen Imaginaerteil
    > tau ||D||^2 hat; Rate = max Re eig(Q^T D Q); die Dimension von V* wird gemeldet.
- **Gegenprobe TT:** A und B eingeschraenkt auf S_E (die "physikalische Dynamik" von TENSOR-EIS-N).

### 4.3 Statik (c) [F2]

- Wie TENSOR-EIS-N [F2]: statischer stationaerer Wert unter exakten Bedingungen.
  - Kern kappa(q) aus dem 7x7-KKT (a-Teil), U(r) per irfftn.
  - L = 64 (mit Minimumtest), 128, 192, 256; nur N-Typ.
- **Torus-Korrektur** unveraendert: U_L = a + b/L + c/L^3 exakt an L = 128, 192, 256; zum Vergleich an 64, 128, 256
  (Unsicherheit).
- **G_eff:** Ausgleich U_inf(r) = -G_eff/r (g = m1 = m2 = 1) nach kleinsten Quadraten ueber alle Oktantpunkte mit
  8 <= r <= 16.
- **c-Abhaengigkeit:**
  - Das statische Problem mit vollem H_c (E- und a-Teil, A(c), Bedingungen Kv E = 0 und c.a = 1) als ein 16x16-KKT je q.
  - Gerechnet auf dem L = 32-Halbgitter (17 407 q) und an 20 000 Zufalls-q.
  - Gemessen: delta_c = max abs(kappa_c - kappa)/max abs(kappa) und max abs(E)/max abs(kappa).
  - Weil c nicht eingeht [M], gilt G_eff(c) := G_eff (derselbe Kern), sofern delta_c <= 1e-10.

### 4.4 Exponent (L1) und Asymmetrie (L2)

- **L1 [F3]:** p ist die Steigung der Ausgleichsgeraden von ln gamma_max(c) gegen ln(1/2 - c) an c = 0,45, 0,48 und 0,49.
  Das sind die Listenwerte "aus c = 0,45 bis 0,49".
- **L2 [F4]:** Delta = abs(gamma(0,55) - gamma(0,45)) / max(gamma(0,55), gamma(0,45)); Delta := 0, wenn beide null sind.
  - Bezug auf die groessere Rate ist die strengste der drei Lesarten.
  - Gemeldet werden auch die Lesarten mit Bezug auf die kleinere Rate und auf den Mittelwert.

## 5. Urteilsregeln (mechanisch in code/lam_auswertung.py)

- **L0 eingetroffen** genau dann, wenn beide Bedingungen gelten:
  1. Bei c = 0,50 besteht kein Eigenwert an keinem q den Wachstumstest, in P0 bis P6 und in der TT-Dynamik; der Rest
     max(-Re omega^2, abs(Im omega^2))/s ist also < 1e-6.
  2. Ueber alle Oktantpunkte mit 8 <= r <= 16 gilt max abs(U_inf 8 pi r + 1) <= 0,01.
  - Sonst nicht eingetroffen.
- **L1:** Je Satz S in {P0, P1} erfuellt genau dann, wenn
  - Wachstum (gamma_max > 0) bei c = 0,40, 0,45, 0,48 und 0,49 vorliegt und
  - p in [0,35; 0,65] liegt.
  - **Eingetroffen**, wenn in P0 und in P1 erfuellt [F1]; sonst nicht eingetroffen, mit Vermerk, falls nur in einem.
- **L2:** Je Satz erfuellt, wenn Delta > 0,20. Eingetroffen, wenn in beiden [F1].
- **L3:** Eingetroffen genau dann, wenn beide Bedingungen gelten:
  1. Die Projektion (b) zeigt fuer kein c und kein q Wachstum, in P0 und P1.
  2. Jeder schnellste freie Wachstumsmodus (P0, P1, jedes c mit Wachstum) hat f_off > 1e-6 [F5].
  - **Nicht auswertbar**, wenn die Dirac-Gegenprobe beim Wachstum anders entscheidet als (1) oder die TT-Dynamik Wachstum
    zeigt, (1) aber nicht.
  - Gibt es gar kein freies Wachstum, ist (2) leer (Vermerk).
- **L4:**
  - Gegenprobe zuerst: delta_c <= 1e-10 und max abs(E)/max abs(kappa) <= 1e-10 fuer alle c; sonst **nicht auswertbar**.
  - **Eingetroffen** genau dann, wenn alle drei Bedingungen gelten:
    1. U_inf < 0 an allen Oktantpunkten mit 2 <= r <= 16 und steigend laengs [100], [110], [111] (anziehend); das gilt
       dann fuer jedes c;
    2. G_eff(c) > 0 und der groesste Sprung zwischen benachbarten c der Liste <= 10 % von G_eff [F6: "stetig" auf
       einer diskreten Liste];
    3. abs(8 pi G_eff(1/2) - 1) <= 0,01 [F6: Toleranz wie L0].
  - Vermerk: vorab ableitbar.

## 6. Laeufe auf der .69 (kleintest.sh, Spuren cpu und cpu6, hoechstens zwei zugleich)

| Lauf | Spur | Aufruf (im Ordner runde36-lambda) | erwartet |
|---|---|---|---|
| S1 | cpu | code/lam.py statik --L 64 --mitmin --L 128 --L 192 --out lauf/statik-64-128-192.json --npz lauf/statik-64-128-192.npz | ~ 90 s |
| S2 | cpu6 | code/lam.py statik --L 256 --chunk 2 --out lauf/statik-256.json --npz lauf/statik-256.npz | ~ 170 s |
| SC | cpu | code/lam.py scan --L 32 --out lauf/scan.json | nach rauch |
| KO | cpu6 | code/lam.py kontrolle --out lauf/kontrolle.json | ~ 60 s |
| AW | cpu | code/lam_auswertung.py --lauf lauf --out lauf/auswertung.json | ~ 20 s |

- Vor AW wird TENSOR-EIS-N lauf-69/auswertung.json als lauf/tensor-eis-n-auswertung.json daneben gelegt (nur Vergleich).
- Laeufe einzeln starten, jeweils mit `cd ... && bash kleintest.sh ...` in einem eigenen ssh-Aufruf im Hintergrund;
  Rueckgabe und Log pruefen.

## 7. Festlegungen [F] (wo die Karte offen ist)

- F1: "Freie Gitterdynamik" bedeutet P0 und P1; fuer L1 und L2 muessen beide erfuellt sein.
- F2: Statik wie TENSOR-EIS-N F2; c-Unabhaengigkeit gegengeprueft; G_eff per Ausgleich ueber 8 <= r <= 16.
- F3: L1 aus c = 0,45 / 0,48 / 0,49, Exponent der Rate gamma_max (die Rate an ihrem Ort in der Zone).
- F4: Asymmetriemass mit Bezug auf die groessere Rate.
- F5: Zwangsflaeche: Hauptmass ist die orthogonale Projektion (wie im Auftrag); Gegenproben Dirac und TT; Schwelle fuer
  "neben Z" ist f_off > 1e-6.
- F6: L4: "stetig" heisst Sprung <= 10 %; "gleich 1/(8 pi)" heisst auf 1 %.
- F7: Gitter L = 32 fuer alle Abtastungen, wie TENSOR-EIS-N.
- F8: Exponentielles Wachstum nach dem tau-Test von TENSOR-EIS-N; polynomiales Wachstum zaehlt nicht.

## 8. Rauchlaeufe (vor dem Einfrieren; offengelegt)

Code hochgeladen 22:46:42 UTC (sha256 lam.py 65dac72d..., lam_auswertung.py 3a6522e1...), danach unveraendert. Alle
Rauchlaeufe auf der .69 ueber kleintest.sh, Zeiten UTC, alle rc = 0.

| Lauf | Spur | Zeit | Inhalt | gesehen |
|---|---|---|---|---|
| rauch1 | cpu | 22:46:53 | statik L = 16 (mitmin), 24 | nur Log (0,4 s) |
| rauch1b | cpu | 22:47:02 | statik L = 32 | nur Log (0,4 s) |
| rauch2 | cpu6 | 22:46:54 bis 22:46:58 | scan L = 8 (Ldirac 8, Lstat 8, nzufall 200) | Log (3,8 s); per jq nur Codepruefungen: kontr_Z (Kv Z_E 5,6e-16, c Z_a 2,7e-15), Summen der Zerlegungsanteile (1 auf 2e-16), Dirac "einheitlich" (alle true), Schluessel, kein NaN/Infinity |
| rauch3 | cpu6 | 22:47:13 bis 22:47:42 | scan L = 16 (Ldirac 16, Lstat 16, nzufall 2000) | nur Log (28,8 s) |
| rauch4 | cpu | 22:47:14 bis 22:47:28 | kontrolle Lort 4, nexakt 2 | nur Log (13,9 s) |
| rauch5 | cpu | 22:48:07 bis 22:48:09 | statik L = 34/36/40 (Oktant 18 fuer den Auswertungstest) | nur Log |
| rauch6 | cpu | 22:48:14 bis 22:48:17 | lam_auswertung.py auf den Rauchdaten (Lkorr 34/36/40, scan L = 8) | nur rc und Laufzeit (2,8 s); Urteilszeile per grep unterdrueckt; auswertung.json und Bilder nicht geoeffnet |

- **Nebenbei gesehen (rauch2):** An der Zahl der Zerlegungseintraege war erkennbar, dass P1 auf dem L = 8-Gitter fuer
  c < 1/2 kein Wachstum hat (5 statt 6 Eintraege). Das folgt aus Abschnitt 2: Auf L = 8 ist K^2 >= 0,586 > 1/2. Auf
  L = 32 ist K^2_min = 0,038.
- **Zeit:** Aus rauch3 (L = 16: 28,8 s) folgen fuer L = 32 etwa 4 min fuer SC, unter der 600-s-Grenze. Deshalb bleibt
  SC ein Lauf.
- Nach den Rauchlaeufen wurden keine Schwelle, keine Urteilsregel und kein Code geaendert.
