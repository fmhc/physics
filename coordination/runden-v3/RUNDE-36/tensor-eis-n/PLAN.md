# TENSOR-EIS-N: Plan (Code-Agent, Runde 36, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-03 23:24:33 CEST; Plantext ab 23:55:41 CEST (date).
  Zeitbox 150 min, also bis 01:54 CEST.
- Grundlage: KARTE.md (Vorhersagen N0 bis N4, Schwellen unveraendert uebernommen).
- Quelle: Gu, Z.-C.; Wen, X.-G.: "Emergence of helicity +-2 modes (gravitons) from qubit models", arXiv:0907.1203v3
  (4 Apr 2010), PDF per WebFetch geholt und seitenweise gelesen (S. 1-3, 9-24).
- Kennzeichen: [S] an der Quelle gelesen (Seite, Gleichung), [L] Literatur aus dem Gedaechtnis, [L?] unsicher,
  [H] Hypothese, [M] Mathematik (vorab ableitbar, Abschnitt 3), [F] eigene Festlegung.
- Alle Rechnungen sind synthetische Gitterrechnungen, keine Messdaten.

## 1. Rekonstruktion aus der Quelle

### 1.1 Freiheitsgrade [S]

- Symmetrisches Tensorfeld a_ij und konjugiertes E^ij, [a_ij(y), E^mn(x)] = (i/2)(delta_im delta_jn + delta_jm delta_in)
  delta(x - y) (Gl. 12, S. 10). Gu/Wen nennen sie auf dem Gitter theta_ab und phi^ab = 2 pi L^ab / n_G (S. 13, 18).
- Gitterplaetze (S. 12): a_xx, a_yy, a_zz, E^xx, E^yy, E^zz auf den Knoten; a_xy, E^xy auf i + (x + y)/2, entsprechend
  yz und zx (Plakettenmitten). Das ist dieselbe Staffelung wie TENSOR-EIS-0.
- Gu/Wens Gittervariablen tragen Vorzeichen (-1)^i; die tiefen Moden liegen bei k = (pi, pi, pi) (S. 17, 20, Gl. 55
  und 62). [F1] Ich rechne in den unversetzten Feldern (k = q + (pi, pi, pi)). Ableitungen sind Differenzen naechster
  Nachbarn, Fourier-Symbol i K_a mit K_a = 2 sin(q_a/2); Gu/Wens c_a = cos(k_a/2) ist dann -K_a/2. Die Gleichwertigkeit
  wird in Kontrolle K3 numerisch geprueft (Matrizen von S. 19).

### 1.2 Zwangsbedingungen, Eichungen, Masse [S]

- Vektorbedingung d_i E^ij = 0 (Gl. 13); auf dem Gitter Q(i, i + a) auf den Links (S. 13).
- Skalarbedingung R^ii = 0 (Gl. 21), also (delta_ij d^2 - d_i d_j) a_ij = 0 (Gl. 22); auf dem Gitter eta(i) auf den
  Knoten (S. 13).
- R^ij = eps^imk eps^jln d_m d_l a_nk (Gl. 16), mit d_i R^ij = 0 (Gl. 19).
- Eichungen: a_ij -> a_ij + d_i f_j + d_j f_i (Gl. 15, erzeugt von Gl. 13) und
  E^ij -> E^ij - (delta_ij d^2 - d_i d_j) f_0 (Gl. 23, erzeugt von Gl. 21).
- **Masse:** "Violation of this constraint at one point corresponds to a scalar charge which can be interpreted as a
  point mass" (S. 11, nach Gl. 22); zwei Massen R^ii(x) = m1 delta(x - x1) + m2 delta(x - x2) (Gl. 31). Auf dem Gitter
  ist das der Skalardefekt |m, i> mit S(j) = exp(2 pi i m / n_G) am Knoten i (Gl. 67, 68, S. 21).

### 1.3 Energien [S]

- **L-Typ:** H = (J/2) C^i_j C^i_j + (g/2) R^ij R^ij (Gl. 27), C^i_j = eps^imn d_m (E^nj - (1/2) delta_nj E^ll) (Gl. 24).
  Dispersion der Helizitaet-2-Moden omega^2 = g J k^6 (Gl. 30). Aussage: "the force is repulsive between two masses
  with the same sign and decay as |x1 - x2|^-4" (S. 11, nach Gl. 31). Eine Herleitung steht nicht da.
- **N-Typ:** H = (J/2) [(E^ij)^2 - (1/2)(E^ii)^2] + (g/2) a_ij R^ij (Gl. 32). Der Term (34) ist unter (23) invariant,
  "provided that E^ij satisfy the constraint (13)"; a_ij R^ij ist unter (15) invariant bis auf eine totale Ableitung
  (S. 12). Bewegungsgleichungen (35): omega^2 = g J k^2 fuer die Helizitaet-2-Moden. Aussage: "the force between the two
  masses is proportional to m1 m2/r^2. Two masses with the same sign attract" (S. 12, nach Gl. 35). Ohne Herleitung.
  Mit a_00, a_0i als Multiplikatoren: "exactly the linearized Einstein action" (Gl. 37).
- **Gittermodell:** H = H_U + H_J + H_g (Gl. 60), H_U nach Gl. 39. Quadratisch entwickelt (S. 19, Gl. 62):
  zusaetzlich (U1/2)(d_i phi^ij)^2 + (U2/2)(R^ii)^2; Gu/Wen setzen U ~ J ~ g (S. 18).
- Gu/Wen selbst: Fuer das N-Gittermodell ist [H_U, H_J] != 0 und [H_U, H_g] != 0; "the omega ~ |k| dispersion ... is
  not a reliable result" (S. 19-21, Abschn. VII.E).
- **Auffaelligkeiten der Quelle [S]:**
  - In der Matrix auf S. 19 steht der Strafterm am phi-Block mit "2 U2", der am theta-Block mit "8 U1". Nach Gl. 39 und
    62 gehoert U1 zur Vektor- und U2 zur Skalarbedingung. Ich richte mich nach der Struktur (phi-Block = Vektorbedingung).
    K3 prueft beide Zuordnungen.
  - H'_J auf S. 18 laesst in der Druckfassung die (L^aa)^2-Glieder weg; die kompaktifizierte Fassung H_J (S. 18) und die
    Matrix auf S. 19 enthalten sie. Ich folge Gl. 32, 62 und S. 19.

### 1.4 Was die Quelle offen laesst, und meine Festlegungen

- [F2] Rechenweg der Kraft: **statischer stationaerer Wert von H unter exakten Zwangsbedingungen** (Gl. 13 fuer E,
  Gl. 31 fuer a), fuer E- und a-Teil. Der E-Teil traegt keine Quelle; sein stationaerer Wert ist 0 (homogen).
  Wechselwirkung U(r) = E(Paar) - E(Masse 1) - E(Masse 2), m1 = m2 = 1, g = J = 1.
- [F3] Torus: Auf dem periodischen Gitter ist die Summe von R^ii identisch null (totale Ableitung). Zwei gleiche Massen
  sind dort nur mit gleichfoermigem Neutralisierungshintergrund moeglich: q = 0 wird nicht geloest (pinv der
  Nullmatrix = 0), wie in TENSOR-EIS-0.
- [F4] Strafterme gehoeren zum Gittermodell (Gl. 60), nicht zur Statik der Karte; sie gehen in N2 (beschreibend) und N3
  (Dynamik) ein.
- [F5] N4 (Pyrochlor): Die Quelle hat keine Fassung auf anderen Gittern. Ein Tensor-Eichmodell auf dem Pyrochlor-Gitter
  waere eine eigene Modellbildung; dafuer reicht die Zeitbox nicht. N4 wird **nicht gerechnet** und als
  "nicht auswertbar" gemeldet. Erwartung dazu nur als [H] im Ergebnis.

## 2. Rechenweg (Code code/tn.py, Auswertung code/tn_auswertung.py)

- Koeffizienten in der Frobenius-Orthonormalbasis (xx, yy, zz, sqrt2 xy, sqrt2 yz, sqrt2 zx); dann ist die Paarung
  E^ij da_ij kanonisch und H = 1/2 E.A.E + 1/2 a.B.a.
- Operatoren je q aus ihren Definitionen (Epsilon-Kontraktion mit i K), nicht aus einer Modenzerlegung:
  - inc (Gl. 16), Skalarzeile c = tr inc (Gl. 22), Vektorbedingung Kv (Gl. 13), Eichgeneratoren G15 (Gl. 15) und
    G23 (Gl. 23), C-Operator (Gl. 24).
  - Hesse-Matrizen:
    - N-Typ: A = J (1 - lambda t t^T) mit lambda = 1/2 und t = Spurvektor, B = g inc.
    - L-Typ: A = J C^T C, B = g inc^T inc.
    - Strafterme: A + U_v Kv^T Kv, B + U_s c c^T.
- **Statik:**
  - Je q das KKT-System [[B, c], [c^T, 0]] per pinv (hermitian, rcond 1e-10) mit rechter Seite (0, 1).
  - kappa(q) = x^T B x ist der stationaere Wert je Einheitsquelle (1/2 kappa |rho|^2).
  - U(r) = (1/N) Sum_{q != 0} kappa(q) cos(q.r) per irfftn; Ausgabe Oktant 0 <= x, y, z <= 17.
  - Gegenweg (L = 64): kappa' = 1/(c^T B^+ c) per eigh-pinv.
  - **Minimumtest:** Eigenwerte von P_c B P_c (P_c = Projektor auf den Tangentialraum der Zwangsflaeche). Ein Minimum
    existiert, wenn keiner unter -1e-9 mal max|eig B| liegt; sonst ist der Wert ein Sattel.
- **Groessen:** L = 64 (mit Minimumtest), 128, 192, 256.
- **Torus-Korrektur:** U_inf(r) aus der exakten Loesung von U_L = a + b/L + c/L^3 mit L = 128, 192, 256 (Hauptwert);
  Unsicherheit = Abstand zur gleichen Anpassung mit L = 64, 128, 256 (wie TENSOR-EIS-0). Begruendung [M]: neutralisierter
  periodischer Green-Kern = Kern + const/L + r^2/(6 L^3) + O(L^-5).
- **Exponent:**
  - p = minus die Steigung der Ausgleichsgeraden von log|U_inf| gegen log r im Fenster 4 <= r <= 16.
  - Strahlen:
    - [100]: (n,0,0), n = 4..16
    - [110]: (n,n,0), n = 3..11
    - [111]: (n,n,n), n = 3..9
  - "Schale": eine gemeinsame Gerade durch alle Oktantvektoren mit 4 <= r <= 16.
  - Kraftexponent = p + 1.
- **Kraftrichtung:** Vorzeichen der Differenzen U_inf(r_{k+1}) - U_inf(r_k) laengs der drei Strahlen, 2 <= r <= 16.
  - Steigt U nach aussen (dU > 0), ist die Kraft anziehend.
  - Faellt U nach aussen (dU < 0), ist sie abstossend.
- **Stabilitaet** (BZ-Gitter L = 32, alle q != 0; q = 0 gesondert):
  - Eigenwerte von A_N und B_N ohne Strafterme (Definitheit).
  - Einschraenkung auf die Zwangsflaechen, die Eichung eingeschlossen: A auf ker Kv, B auf ker c.
  - Einschraenkung auf die eichfreien Zwangsflaechen: S_E = ker Kv ohne G23, S_a = ker c ohne Bild G15, je per SVD.
  - Gewichte der negativen Eigenvektoren: physikalisch, Eichung, Verletzung.
- **Lineare Dynamik:**
  - da/dt = A E, dE/dt = -B a; omega^2 = Eigenwerte von A B (6x6; die 12x12-Matrix wuerde Jordan-Rundung ~eps^(1/4)
    erzeugen).
  - Parametersaetze, je J = g = 1:
    - N-Typ: P0 (ohne Strafterme); P1 U_v = U_s = 1 (Gu/Wen U ~ J ~ g); P2 0,1/0,1; P3 10/10; P4 100/100;
      P5 U_v = 1, U_s = 0,01; P6 U_v = 0,01, U_s = 1.
    - L-Typ: L0 (ohne Strafterme), L1 (1/1).
  - Physikalische Dynamik mit exakten Zwangsbedingungen: A, B eingeschraenkt auf S_E = S_a. Dass beide Raeume gleich
    sind, wird geprueft.
  - Beschreibend, ohne Urteil: lambda-Abtastung 0,40 / 0,45 / 0,49 / 0,50 / 0,51 / 0,55 / 0,60 (mit U = 1 und ohne);
    Linienschnitte [100], [110], [111]; Driftbeispiel per expm.
- **Exakte Pruefung** (Bruchrechnung, physikalische Komponenten mit Gram-Matrix W = diag(1,1,1,2,2,2)):
  - Ort: 12 zufaellige rationale K-Vektoren.
  - Rechnung: charakteristisches Polynom der omega^2-Matrix W^-1 A W^-1 B; Vielfachheit der Null; Sturm-Kette des
    Restpolynoms (Anzahl reeller bzw. positiver Wurzeln).
  - Jordanstruktur bei 0: Raenge von D^k fuer die 12x12-Bewegungsmatrix.
  - Saetze: P0, P1, P3, P5, L0, L1, lambda = 0,45 und 0,55.

## 3. Schreibtisch vorab [M] (vor jeder Rechnung hergeleitet)

Im k-Rahmen je q != 0 (K-Dach = K/|K|): TT (zwei transversal-spurfreie Richtungen), T = (delta - K-Dach K-Dach)/sqrt2,
L = K-Dach K-Dach, V (zwei gemischte). Dann gilt:

- inc hat die Eigenwerte +K^2 (TT, zweimal), -K^2 (T), 0 (L, V: Eichung Gl. 15). c ist proportional zu T:
  c.a = -sqrt2 K^2 a_T. Kv verschwindet auf TT und T; G23 ist proportional zu T (= -c).
- **N-Typ statisch:** a_T ist durch die Masse festgelegt, a_T = -rho/(sqrt2 K^2). Die Energie (g/2)(-K^2) a_T^2 =
  -g rho^2/(4 K^2) ist ein fester Wert. TT ist positiv (Minimum bei 0), die Eichung ist null.
  - kappa_N = -g/(2 K^2), also U_N(r) = -(g/2) m1 m2 G_Delta(r) -> -g m1 m2/(8 pi r).
  - Anziehend, Exponent 1, Kraft ~ m1 m2/r^2, wie Gu/Wen.
  - **Ein Minimum existiert** auf der (affinen) Zwangsflaeche; die negative Richtung T ist durch die Zwangsbedingung
    gebunden, nicht frei.
- **L-Typ statisch:** B_L = g inc^2, auf T also g K^4.
  - Daraus kappa_L = g K^4 a_T^2 / rho^2 = g/2, eine Konstante.
  - U_L(r) = (g/2)(delta_r0 - 1/N): Fuer r >= 1 gibt es **keine Wechselwirkung**, nur die Torus-Konstante -g/(2N);
    die Kraft ist null.
  - Im Kontinuum ebenso (Kontaktglied).
  - Gu/Wens r^-4 folgt aus Gl. 27 und 31 in statischer Rechnung nicht. Lesart [H]: Das Feld einer Masse
    (R^ij ~ d_i d_j (1/r), faellt wie r^-3) ist langreichweitig; die Kreuzenergie integriert sich aber zu einem
    Kontaktglied.
  - **Erwartung: N0 nicht eingetroffen** (keine Abstossung).
- **N-Typ Definitheit:** A_N = J (1 - (1/2) t t^T) hat die Eigenwerte 1 (fuenfmal) und -1/2 (Spur delta/sqrt3 =
  (sqrt2 T + L)/sqrt3, Gewicht 2/3 Eichung G23, 1/3 Verletzung von Gl. 13, 0 physikalisch). B_N: -K^2 auf T (reine
  Verletzung von Gl. 21).
  - Auf ker Kv (TT + T): A = diag(J, J, 0), positiv semidefinit, die 0 ist die Eichrichtung.
  - Auf ker c (TT + L + V): B = diag(gK^2, gK^2, 0, 0, 0).
  - Auf der eichfreien Zwangsflaeche (TT): A = J, B = g K^2.
  - **Erwartung N2 eingetroffen.**
- **q = 0 (homogene Torusmoden):** Hier sind alle Bedingungen trivial erfuellt und es gibt keine Eichrichtung.
  - E^ij = e delta_ij ist eine physikalische negative Richtung, Energie -(3J/4) e^2 je Knoten; B = 0.
  - [F6] Fuer N2 gilt das unendliche Gitter (q != 0). Die Torus-Nullmode wird im Vermerk gemeldet. Unter einer Lesung,
    die sie einschliesst, waere der Klammerteil von N2 verfehlt.
- **Mit Straftermen:** Der (T, L)-Block von A ist [[0, -J/sqrt2], [-J/sqrt2, J/2 + U_v K^2]], det = -J^2/2 < 0 fuer
  jedes q und jedes U_v.
  - Die negative Richtung bleibt also; der Vektor-Strafterm hebt sie nie.
  - B auf T: b = -g K^2 + 2 U_s K^4 < 0 fuer K^2 < g/(2 U_s).
  - Im Gittermodell ist die Energie damit nicht nach unten beschraenkt; die negativen Richtungen bleiben ausserhalb der
    eichfreien Zwangsflaeche.
- **Dynamik:**
  - omega^2 = eig(A B): TT g J K^2 (N, Gl. 35) bzw. g J K^6 (L, Gl. 30).
  - (T, L)-Block der N-Form: A B = [[0, 0], [-J b/sqrt2, 0]], nilpotent, weil A_TT = J (1 - 2 lambda) = 0 genau bei
    lambda = 1/2.
  - V-Block: 0.
  - **Keine exponentiell wachsenden Moden**, fuer jedes U_v und U_s.
  - Polynomiales Wachstum: Jordankette E_L -> a_T -> E_T -> a_L, Laenge 4 in der 12x12-Bewegungsmatrix. Die
    Skalarbedingung c.a waechst linear, wenn die Vektorbedingung verletzt ist (E_L != 0); E_T (Eichung 23) und a_L
    (Eichung 15) wachsen mit.
  - L-Typ: groesste Kettenlaenge 2; c.a bleibt erhalten.
  - **Erwartung N3 nicht eingetroffen.**
  - Bei lambda != 1/2 gilt omega^2 = J (1 - 2 lambda) b auf T.
    - lambda < 1/2 waechst exponentiell bei kleinem K.
    - lambda > 1/2 waechst exponentiell dort, wo b > 0.

## 4. Agenten-Vorhersagen (vorab, mit Zahl; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| A1 | L-Typ: abs(U_inf) < 1e-12 fuer alle 2 <= r <= 16; roh U_L(r != 0) = -1/(2 L^3) auf 1e-12 relativ; c-Koeffizient der Anpassung -0,5 |
| A2 | N-Typ: U_inf(r) * 8 pi r = -1 auf 2 % fuer r >= 4 und auf 0,5 % fuer r >= 8 |
| A3 | N-Typ: Exponenten 1,00 +- 0,02 auf allen drei Strahlen und der Schale |
| A4 | Je q != 0 genau ein negativer Eigenwert von A_N (-0,5) und einer von B_N (-K^2); Gewichte: A-negativ 0 / 2/3 / 1/3 (phys / Eichung / Verletzung), B-negativ 0 / 0 / 1 |
| A5 | Auf der eichfreien Zwangsflaeche: A = J (beide Eigenwerte), B/K^2 = 1 (min und max); physikalische Dynamik omega^2/K^2 = 1 |
| A6 | Exakt: Charakteristisches Polynom x^4 (x - g J K^2)^2 (N, alle U), x^4 (x - g J K^6)^2 (L); Jordan bei 0: 4 (N, b != 0), 2 (L) |
| A7 | lambda-Abtastung: exponentielles Wachstum fuer alle lambda != 0,50 (mit U = 1), keines bei 0,50 |
| A8 | K3: urspruenglich "4 eig(X Y) = eig(A B) auf 1e-10 relativ; vertauschte Zuordnung weicht ab". Nach rauch3 als nicht pruefbar erkannt (eig(A B) haengt nicht von U ab; Jordan-Rundung ~1e-7). Ersetzt durch: direkter Matrixvergleich trifft bei s = (1, 1, 1) und strukturgleicher Zuordnung auf <= 1e-12 relativ, die vertauschte Zuordnung weicht um O(1) ab (in rauch4 schon gesehen, s. Abschnitt 8) |
| A9 | q = 0: eig A_N = {-0,5; 1 (fuenfmal)}, eig B_N = 0 (sechsmal) |

## 5. Kontrollen

- K1, Operatoridentitaeten je q (L = 32), jeweils <= 1e-12 relativ:
  - d_i R^ij = 0;
  - inc G15 = 0 und c G15 = 0;
  - Kv G23 = 0 ([S, V] = 0, S. 14);
  - C G23 = 0;
  - c = -G23;
  - inc symmetrisch.
- K2, Ortsraum L = 6 (Stencils per np.roll, Lagen geprueft):
  - statisches U fuer N und L gegen den Fourierweg, <= 1e-10;
  - Spektrum A B fuer P0 und P1 gegen die Vereinigung der Fourier-Spektren, <= 1e-6 relativ.
- K3, Gu/Wen-Matrix S. 19, bei k = q + (pi, pi, pi):
  - **entscheidend (nach rauch3 ergaenzt, s. Abschnitt 8):** direkter Matrixvergleich A = 2 D^-1 X D^-1 und
    B = 2 D Y D mit D = diag(1, 1, 1, sqrt2 s_xy, sqrt2 s_yz, sqrt2 s_zx), s = +-1 (alle acht Vorzeichen probiert),
    U_v = 0,7, U_s = 1,3, 200 zufaellige q, beide Zuordnungen der Strafterme. Schwelle: <= 1e-12 relativ zur
    Matrixgroesse fuer die strukturgleiche Zuordnung;
  - nur berichtet: 4 eig(X Y) gegen eig(A B). Dieser Vergleich haengt nicht von U_v, U_s ab und ist durch
    Jordan-Rundung auf etwa 1e-7 begrenzt;
  - Signaturen von A gegen X und von B gegen Y.
- K4, Dispersion: physikalische omega^2/K^2 (N) gegen Gl. 35, und die exakte Charakteristik (L) gegen Gl. 30.
- K5:
  - Statik: kappa gegen kappa' (L = 64);
  - Zwangsresiduum c.x - 1 fuer q != 0;
  - Spiegel- und Vertauschungssymmetrie von G.
- K6: Groessenreihe, Abstand der beiden Torus-Anpassungen.

## 6. Urteilsregeln (mechanisch in code/tn_auswertung.py)

- **N0** (L-Typ: Abstossung, Kraftexponent 4 +- 0,4, nach Torus-Korrektur):
  - **Eingetroffen** genau dann, wenn alle drei Bedingungen gelten:
    1. U_inf > 0 fuer alle Oktantvektoren mit 2 <= r <= 16;
    2. U_inf faellt laengs aller drei Strahlen fuer 2 <= r <= 16 (Kraft abstossend);
    3. der Kraftexponent p + 1 liegt in [3,6; 4,4] auf allen drei Strahlen und der Schale.
  - Ist max abs(U_inf) ueber 2 <= r <= 16 kleiner als 1e-12 (g m^2), heisst der Befund "keine Wechselwirkung"; dann
    **nicht eingetroffen**, Exponent nicht definiert.
  - Gilt N0 als Pruefung der Fassung aus Abschnitt 1.4 [F2].
- **N1** (N-Typ: stationaere statische Wechselwirkung anziehend, Potential ~ 1/r, Exponent 1 +- 0,1):
  - **Eingetroffen** genau dann, wenn alle drei Bedingungen gelten:
    1. U_inf < 0 fuer alle Oktantvektoren mit 2 <= r <= 16;
    2. U_inf steigt laengs aller drei Strahlen (Kraft anziehend);
    3. p in [0,9; 1,1] auf allen drei Strahlen und der Schale.
  - Zusaetzlich gemeldet:
    - ob ein Minimum existiert (Minimumtest L = 64) und welcher stationaere Wert vorliegt;
    - Abstand zu -1/(8 pi r);
    - Unsicherheit der Torus-Anpassung.
- **N2** (N-Typ: quadratische Form indefinit, negative Richtungen ausserhalb der eichfreien Zwangsflaeche), auf dem
  BZ-Gitter L = 32, q != 0, ohne Strafterme:
  - (i) **Indefinit:** fuer mindestens ein q hat A_N oder B_N einen Eigenwert < -1e-9 mal max abs(eig).
  - (ii) **Aussen:** die Einschraenkungen von A_N auf ker Kv und von B_N auf ker c sowie auf die eichfreien Raeume S_E,
    S_a sind fuer alle q positiv semidefinit (Minimum >= -1e-9 relativ).
  - Eingetroffen genau dann, wenn (i) und (ii) gelten.
  - Gilt (i), aber (ii) nicht, ist N2 **nicht eingetroffen**; dann hat das Netz physikalisch negative Richtungen
    (Vermerk).
  - q = 0 gesondert [F6]; Strafterm-Saetze beschreibend.
- **N3** (lineare Gitterdynamik hat wachsende Moden):
  - "Wachsend" heisst **exponentiell** [F7]. Kriterium: fuer ein q != 0 gilt -Re(omega^2) > 1e-6 |A| |B| oder
    abs(Im(omega^2)) > 1e-6 |A| |B|.
  - Begruendung der Schwelle: Ein Jordanblock der Groesse 2 in A B erzeugt Rundungswerte der Ordnung 1e-8 relativ.
  - Geprueft wird in P0 bis P6 und in der physikalischen Dynamik.
  - Bestaetigung exakt: In mindestens einem rationalen Punkt hat das charakteristische Polynom (P0, P1, P3, P5) eine
    Wurzel, die nicht reell und nicht >= 0 ist.
  - Eingetroffen, wenn Gleitkomma und exakte Pruefung uebereinstimmend Wachstum zeigen. Nicht eingetroffen, wenn beide
    keines zeigen. Widersprechen sie sich: **nicht auswertbar**.
  - Polynomiales (saekulares) Wachstum aus Jordanbloecken bei omega = 0 zaehlt nicht [F7]. Es tritt auch in stabilen
    Eichtheorien auf (Eichdrift, z. B. Maxwell in Zeiteichung [L]). Es wird mit Ort (Eichung, Verletzung) gemeldet.
- **N4:** nicht gerechnet [F5], also **nicht auswertbar**.
- Die lambda-Abtastung, die Strafterm-Saetze fuer N2 und das Driftbeispiel sind beschreibend und tragen kein Urteil.

## 7. Laeufe auf der .69 (kleintest.sh, Spuren cpu und cpu6, hoechstens zwei zugleich)

| Lauf | Spur | Aufruf | Erwartete Dauer |
|---|---|---|---|
| S1 | cpu | tn.py statik --L 64 --mitmin --out lauf/statik-64.json --npz lauf/statik-64.npz | ~ 20 s |
| S2 | cpu | tn.py statik --L 128 --L 192 --out lauf/statik-128-192.json --npz lauf/statik-128-192.npz | ~ 200 s |
| S3 | cpu6 | tn.py statik --L 256 --chunk 2 --out lauf/statik-256.json --npz lauf/statik-256.npz | ~ 350 s |
| SP | cpu6 | tn.py spektrum --L 32 --out lauf/spektrum.json | ~ 60 s |
| KO | cpu | tn.py kontrolle --out lauf/kontrolle.json | ~ 60 s |
| AW | cpu | tn_auswertung.py --lauf lauf --out lauf/auswertung.json | ~ 20 s |

- Zeiten geschaetzt aus rauch2 (L = 32: 0,71 s fuer 17 408 q-Punkte, beide Typen). Faellt S3 an der 600-s-Grenze,
  wird L = 256 durch L = 224 ersetzt und die Anpassung (128, 192, 224) genommen. Das ist vorab festgelegt.

## 8. Rauchlaeufe (vor dem Einfrieren; offengelegt)

- rauch1 (cpu, 21:50:50 UTC): Abbruch beim Import (Bruch-Hilfsfunktion F mit zwei Argumenten), ohne Rechnung.
- rauch2 (cpu, 21:51:00 bis 21:51:04 UTC). Gesehen habe ich:
  - Zeiten;
  - Zwangsresiduen um 1e-15;
  - Minimumtest L = 16: keine negativen Tangentialeigenwerte fuer N und L;
  - kappa gegen kappa' 3e-15;
  - Symmetrien;
  - G(0) = -0,1193 bzw. -0,1228 (N, L = 16 bzw. 32) und 0,49988 bzw. 0,49998 (L). Das passt zu kappa_L = 1/2 konstant
    (Abschnitt 3);
  - Operatorkontrollen K1 bei L = 8 (<= 7e-15, Raenge 3, physikalische Raeume von E- und a-Seite gleich);
  - Ortsraumbau L = 4;
  - exakte Pruefung an einem Punkt (P1: alle omega^2 reell, nicht negativ).
- Keine U(r)-Werte bei r != 0, keine Exponenten, keine Urteile.
- **rauch3** (Kette mit kleinen Groessen, alle rc = 0):
  - Laeufe: statik L = 34 (cpu, 21:57:57 UTC); L = 36/40 (cpu, bis 21:58:01); kontrolle (cpu, 21:58:01 bis 21:58:24);
    statik L = 48 (cpu6, 21:58:44 bis 21:58:46); spektrum L = 8 (cpu6, bis 21:58:47); Auswertung mit Lkorr 36/40/48
    (cpu, 21:58:54 bis 21:58:57).
  - **Fehlstart:** Der erste Startbefehl stand mit `cd ... && ... &` als Ganzes im Hintergrund. Die cpu6-Kette lief deshalb
    zunaechst im Heimatordner mit leerem Starterpfad an und brach ohne Rechnung ab (keine Dateien). Ich habe sie danach
    im richtigen Ordner gestartet.
  - Von rauch3 habe ich nur Rueckgabewerte, Fehlermeldungen und Dateinamen gelesen. Ausgabe der Auswertung, Urteile und
    Bilder blieben ungelesen.
  - Ausnahme: die Kontrollen K2 und K3 per jq:
    - Ortsraum gegen Fourier statisch 1,5e-16 (N) und 2,7e-15 (L);
    - Spektrum P0 4,9e-8 und P1 1,2e-6 absolut bei max omega^2 = 12;
    - Signaturen A/X (5, 0, 1), B/Y (2, 3, 1);
    - 4 eig(X Y) gegen eig(A B): 1,1e-7 (ohne Strafterme) und 2,4e-6 (mit). Die vertauschte Zuordnung lag gleich nah.
  - Daraus folgte: Der Eigenwertvergleich unterscheidet die Strafterm-Zuordnung nicht. Ich habe den direkten
    Matrixvergleich ergaenzt (K3, A8). Das ist eine Kontrolle, keine Urteilsschwelle.
- **rauch4** (cpu, 22:00:23 bis 22:00:46 UTC, nur kontrolle, neuer Code). Gelesen habe ich nur den Matrixvergleich:
  - strukturgleich, s = (1, 1, 1): A 1,3e-15, B 4,3e-14 (Matrixeintraege bis ~10^2);
  - vertauscht: 2,4 bzw. 38.
- Keine Schwelle und keine Urteilsregel wurde nach einem Rauchlauf geaendert.
