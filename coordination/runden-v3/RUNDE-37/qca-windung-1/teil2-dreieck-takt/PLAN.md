# DREIECK-TAKT-1 mit QCA-WINDUNG-2: Plan des Code-Agenten (Runde 41, Teil 2)

- Code-Agent fuer die Leitung claude-primary; derselbe Agent wie QCA-WINDUNG-1. Start 2026-10-04 16:33:41 CEST (date).
  Gelesen: KARTE-2-DREIECK-TAKT.md (ganz); eigener Teil 1 (Code windung.py, ERGEBNIS.md).
- Ordner: lokal RUNDE-37/qca-windung-1/teil2-dreieck-takt/, auf der .69 /home/fmh/fmhc-physics-remote/runde41-qca-windung/
  teil2/ (code/, rauch/, lauf/). Teil-1-Dateien bleiben unveraendert.

## 0. Literatur: Erwartungen vor den Abrufen (geschrieben ab 16:39:14 CEST, vor Abruf 1)

- F1 Higashikawa/Nakagawa/Ueda, arXiv:1806.06868v2 (Volltext): Erwartung [L?]: Ihr 3D-Modell mit W3 ungleich 0 ist
  **nicht endlichreichweitig** im Sinn eines festen Takts aus Teilverschiebungen. Entweder ist U_F die Zeitentwicklung
  einer stetigen Treibung (dann quasilokal) oder der Floquet-Hamiltonian ist nichtlokal (saegezahnartig). Vermutung [M,
  vorab]: Fuer jede stetige Treibung mit lokalem H(t) ist U_F ueber t -> U(t) homotop zur Eins, also W3 = 0. Ein
  W3-Beispiel braucht daher Schritte, die selbst keine lokale Hamilton-Zeitentwicklung sind.
- F2 Kitagawa/Berg/Rudner/Demler, PRB 82, 235114 (2010), arXiv:1010.6126 (Volltext oder Abstract): Erwartung [L?]:
  Wabengitter, Sprung zyklisch laengs der drei Bindungsrichtungen; bei vollstaendigem Uebertrag ist U_F = 1 im Volumen
  (Chern 0), am Rand laeuft eine einseitige Welle; die Umkehr der Reihenfolge kehrt sie um. Bei Teiluebertrag
  Chern-Baender.
- F3 (Reserve) Kitagawa/Rudner/Berg/Demler, PRA 82, 033429 (2010), arXiv:1003.1729: 2D-Quantenlauf mit Chern-Baendern.
- **F1 gelesen (16:40, quellen/higashikawa-nakagawa-ueda-1806.06868v2.pdf, sha256 8e79373a...a33908, S. 1 bis 3 als
  Bild) [S]:**
  - Gitter Eq. (1): L_C = {(m1, m2, m3/2)}, Teilgitter L_ev, L_od in der dritten Richtung.
  - Eq. (2): spinselektive Thouless-Pumpen U_j^+- = Sum [(P_j^+-) c^dag_{x+-e_j} c_x + (P_j^-+) c^dag_x c_x],
    "P_j^+- := (sigma_0 +- sigma_j)/2". Eq. (3): U_{h,3}^+- verschiebt "by a half lattice site in the x3 direction".
  - Eq. (4), (5): U_F^wh = U_1^- U_{h,3}^- U_2^- U_{h,3}^+ U_1^+ U_{h,3}^- U_2^+ U_{h,3}^+, V^wh(k) = U(k) + U^H(k)
    (direkte Summe), "U^H(k) := U(k1, k2, k3 - 2pi), U_j^+-(k) := P_j^+- e^{-ik} + P_j^-+ and U_{h,3}^+-(k) := U_3(k/2)".
  - "A straightforward calculation shows that U(k) stays a constant value -sigma_0 if k belongs to the boundary of the
    Brillouin zone T^3 := [-pi, pi]^3". Eq. (6): "W := -1/(24 pi^2) Int ... Tr[R_i R_j R_k] = 1", R_i = U^dag d_i U.
    Also W = -W3(Karte).
  - "Here we focus on U(k) as a Floquet operator of lower Floquet bands"; die Abgeschlossenheit des Unterraums kommt aus
    "generalized adiabaticity ... or some fine-tuning of a driving protocol".
  - **Erwartung F1: teils.** Das Modell ist endlichreichweitig (nur spinselektive Teilverschiebungen), aber W = 1 gilt fuer
    den 2x2-Block U(k) auf [-pi, pi]^3, also fuer die "unteren Floquet-Baender". Meine Lesart [M, im Plan zu pruefen]:
    Auf dem feinen Gitter (Lagenabstand 1/2, alle Lagen gleich) ist U ein 2-Band-Automat mit k3 in (-2pi, 2pi]; ueber
    die ganze Zone ist W3 = W3(U) + W3(U^H) = 0, nur die Haelfte k3 in [-pi, pi] traegt 1. Der Partner sitzt im
    oberen Block U^H.
- **F2 gelesen (16:42, quellen/kitagawa-berg-rudner-demler-1010.6126.pdf, sha256 35702546...c21c5781, S. 1, 2, 6 bis 10
  als Bild) [S]: Erwartung bestaetigt.**
  - Eq. (9): "H(k) = - Sum_i J_i(t) (cos(b_i . k) sigma_x + sin(b_i . k) sigma_y)", "b1 = (-1/2, sqrt3/2),
    b2 = (-1/2, -sqrt3/2) and b3 = (1, 0)"; Protokoll S. 6: "1. J1 = lambda J; J2, J3 = J for nT < t <= nT + T/3",
    2. J2 = lambda J, 3. J3 = lambda J. Eq. (10): "e^{-iTH_eff} = e^{-iH3T/3} e^{-iH2T/3} e^{-iH1T/3}".
  - S. 7: "We find C+- = +-1 for 1 < lambda < lambda_c, where lambda_c ~ 3.3"; "For lambda > lambda_c, the Chern
    numbers of both bands become zero"; Fig. 6: "Here we choose JT = pi/16, and lambda = 1, 3, 3.3, 4"; "At lambda = 4,
    the Chern numbers associated with each of the bands are zero, yet the nanoribbon clearly still supports chiral edge
    states".
  - S. 8 (Grenzfall J -> 0, lambda J (T/3) = pi/2): "a particle starting at any site in the bulk comes back to the
    starting site after two complete driving periods. On the other hand, a particle which starts at the upper (lower)
    edge on sublattice B (A) propagates unidirectionally along the edge to the left (right)."
  - Zur Umkehr der Reihenfolge sagt die Quelle nichts; das wird gerechnet.
- F3 nicht abgerufen (2 von 3 Abrufen).

## 1. Schreibtisch [M] (vor jeder Rechnung; zuerst pruefen, dann rechnen)

- **T1 (Leitung, geprueft):** W3(AB) = W3(A) + W3(B) fuer Abbildungen T^3 -> U(N) (Standard, Ausmultiplizieren von
  (AB)^-1 d(AB); die Mischterme sind exakt). Eine Teilverschiebung I - P + exp(i k.f) P mit festem P haengt nur von
  k.f ab, faktorisiert also ueber S^1 und hat W3 = 0; eine feste Muenze ebenso. Jedes Produkt daraus hat W3 = 0, in
  jeder Reihenfolge. **Richtig, mit einer Voraussetzung:** Jeder Faktor muss selbst eine Abbildung auf demselben Torus
  sein (periodisch). Higashikawa u. a. verletzen genau das: U_h3(k3) = U_3(k3/2) hat Periode 4 pi.
- **T2 (staerker, eigene Herleitung, Saetze aus dem Gedaechtnis [L]):** Jede endlichreichweitige translationsinvariante
  Unitaere in 3D (Laurent-Polynom U(z), z_j = exp(i k_j), beliebige Zahl innerer Zustaende) hat W3 = 0.
  - U ist ueber dem Ring R = C[z1^+-1, z2^+-1, z3^+-1] invertierbar (U^-1 = U^dag ist wieder ein Laurent-Polynom),
    det U ist ein Monom c z^m.
  - K-Theorie [L]: K_1(R) = R^* (Bass/Heller/Swan fuer regulaere Ringe; K_0 von Laurent-Ringen ueber einem Koerper ist
    Z, Swan), also SK_1(R) = 0: U + I_m = diag(det U, 1, ...) E mit E ein Produkt elementarer Matrizen E_ij(p) ueber R.
  - E_ij(t p), t von 0 nach 1, ist eine Homotopie durch invertierbare Laurent-Matrizen von I nach E; W3 ist auf
    GL(N, C) homotopieinvariant. Also W3(U) = W3(det U) = 0.
  - Das ist das K_1-Gegenstueck zu "endlichreichweitige Projektoren haben Chern-Zahl 0" (Dubail/Read 2015; Chen u. a.
    2014) [L]. Folgerung: Kein lokaler Takt in 3D (endliche Reichweite, ein Bravais-Gitter, Translationsinvarianz)
    traegt Netto-Haendigkeit; der Floquet-Weg braucht quasilokale Schwaenze oder einen ausgesonderten Unterraum.
  - **Folge fuer die Karte:** DT1 kann nach T2 fuer endlichreichweitige Automaten nicht eintreten; die Rechnung prueft
    T2 (Suche, Literaturnachbau) und kann es widerlegen.
- **T3:** Fuer jede stetige Treibung mit stetigem H(t, k) ist U_F ueber t -> U(t) homotop zur Eins, also W3 = 0.
  W3 ungleich 0 braucht Schritte, die keine lokale Hamilton-Zeitentwicklung sind (Teilverschiebungen, wie in 1D der
  Shift), oder einen Unterraum.
- **T4 (Higashikawa u. a., Lesart):** Auf dem feinen Gitter (Lagenabstand 1/2, alle Lagen gleich; u = (k1, k2, q3),
  q3 = k3/2) ist Eq. (5) ein Produkt aus Teilverschiebungen in den Variablen u, also endlichreichweitig mit
  W3 = 0 ueber den ganzen Torus (T1 und T2). Die Quelle integriert ueber k3 in [-pi, pi], also q3 in [-pi/2, pi/2]
  (halbe Zone); dort ist W = 1 behauptet (W = -W3 der Karte). Erwartung: W3(halbe Zone) = -1, W3(andere Haelfte) = +1;
  der Partner-Weyl-Punkt liegt bei k3 = 2 pi (q3 = pi), im oberen Block U^H.

## 2. Rechnungen [F]

- **P3 (3D, windung.py aus Teil 1 unveraendert):**
  - Produkte: je N = 2, 3, 4 zwoelf Zufallsprodukte aus 4 Muenzen (Haar) und 4 Teilverschiebungen (zufaelliger
    Projektor vom Rang 1 bis N-1, zufaellige Richtung aus 13 Gitterrichtungen, Vorzeichen zufaellig), dazu jeweils die
    umgekehrte Reihenfolge. Exaktes Produkt als Laurent-Polynom (Faltung).
  - Pyrochlor-Dreieckstakt (Finns Bild in 3D): 4 Teilgitter (Ecken eines Tetraeders, FCC), Takt je Dreieck: auf jeder
    der 4 Flaechen (gleich orientiert als Rand des Simplex [0123]) die drei Kanten nacheinander als Teiluebertrag
    exp(-i theta (Sprung + h.c.)), erst die Auf-, dann die Ab-Tetraeder (Ab-Bindung a-b mit Zellversatz a_a - a_b),
    24 Schritte; theta = pi/2, pi/3, 0,4; Drehsinn vorwaerts und umgekehrt.
  - Additivitaet: Grad-1-Abbildung K-S1 aus Teil 1 (quasilokal, W3 = -1) mal Zufallsprodukt R, beide Reihenfolgen.
  - Higashikawa: Eq. (5) als Produkt auf dem feinen Torus; W3 ganzer Torus; Randwert der Halbbox (U = -sigma_0?);
    W3 der Halbbox (q3 in [-pi/2, pi/2)) und der anderen Haelfte, Rechteckregel N = 16, 32, 48, 64; Weyl-Punkte auf
    dem ganzen Torus (Suche aus Teil 1); Kegel bei k = 0 (Isotropie in k-Koordinaten bei |k| = 1e-4, 0,05, 0,2).
  - **Gitter:** fuer Laurent-Polynome zusaetzlich N_exakt = 6 M + 1 (M = groesste Frequenz je Richtung); dort ist die
    Rechteckregel exakt bis auf Rundung [M].
- **LM (3D, Test von T2):** allgemeine endlichreichweitige Unitaere mit Traeger F15 (0, +-e_j, vier Raumdiagonalen
  beidseitig), N = 2 (40 Starts) und N = 3 (30 Starts; je ein Lauf): Levenberg-Marquardt (scipy, MINPACK) auf alle Koeffizienten von
  U^dag U - I mit analytischer Jacobi-Matrix, Zufallsstart; Treffer D < 1e-20; W3 bei N = 16, 24, 32, 48 und N_exakt = 7.
  Diese Treffer sind im Allgemeinen kein offensichtliches Produkt.
- **H2 (2D, Kitagawa u. a. 2010, Eq. 9, 10):** Protokolle "voll" (J -> 0, lambda J T/3 = pi/2; reiner Dreieckstakt,
  endlichreichweitig), "lam3" (JT = 3 pi/16, lambda = 3), "lam4" (lambda = 4), "lam1" (lambda = 1, Nachbaukontrolle:
  statisch, lueckenlos); je Reihenfolge 1-2-3 (b1 bei 120 Grad, b2 bei 240 Grad, b3 bei 0 Grad: gegen den Uhrzeigersinn)
  und 3-2-1. Volumen: zwei Quasienergie-Luecken (groesste Bogen ohne Eigenphase, Gitter 162^2), Chern-Zahlen beider
  Baender (Fukui/Hatsugai/Suzuki). Streifen: Zickzack-Rand, W = 40 Zellen, 1200 k-Werte; Randfluss je Luecke: Zahl der
  Eigenphasen-Durchgaenge durch die Luckenmitte, nach Rand (Gewicht im oberen bzw. unteren Viertel > 0,6) und Richtung
  (Vorzeichen von d eps/dk, eps = -phi/T), Zuordnung ueber Eigenvektor-Ueberlapp benachbarter k.

## 3. Lehre aus Teil 1: Vorbedingungen ohne Rauschfehler [F, vor dem Einfrieren]

- Keine relative Schwelle auf Groessen, die verschwinden koennen. Absolute Schwellen weit ueber dem Rundungsniveau:
  Unitaritaet <= 1e-8; Randwert Higashikawa <= 1e-10; "W3 = 0" heisst |W3| <= 1e-8 bei N_exakt (exakte Quadratur;
  Rundung ~1e-14); "ganzzahlig" heisst |W3 - round(W3)| < 0,05 (Karte).
- Vorbedingungen fuer alle Urteile: alle Laeufe Modus haupt, rc = 0; Unitaritaet aller 3D-Automaten <= 1e-8; Nachbau
  Kitagawa: lam1 ist bei Quasienergie 0 lueckenlos (kleinster Abstand einer Eigenphase zu 0 < 1e-6; die Dirac-Punkte
  liegen bei Nk = 162 auf dem Gitter); lam3 hat Luecken bei 0 und pi (kleinster Abstand > 1e-3). Keine weitere.

## 4. Urteilsregeln (mechanisch in code/auswertung2.py)

- **DT0:** eingetroffen genau dann, wenn (a) alle Zufallsprodukte (beide Reihenfolgen) und alle Dreieckstakte (beide
  Drehsinne) |W3| <= 1e-8 bei N_exakt haben **und** (b) lam3 vorwaerts: beide Chern-Zahlen eindeutig mit |C_rund| >= 1
  und |C - C_rund| < 0,05, und in mindestens einer Luecke einseitiger Randfluss (N_oben ungleich 0, N_unten = -N_oben,
  N_bulk = 0). Sonst nicht eingetroffen. Vermerk: Additivitaet (|W3(S1 R) + 1| < 0,05, |W3(R S1) + 1| < 0,05).
- **DT1:** eingetroffen genau dann, wenn ein endlichreichweitiger 3D-Automat auf seinem eigenen Brillouin-Torus
  ganzzahlig |round(W3)| >= 1 hat: Zufallsprodukte, Dreieckstakte, LM-Treffer, Higashikawa auf dem ganzen feinen Torus.
  Nicht eingetroffen, wenn alle |W3| < 0,05. Sonst nicht auswertbar. Vermerk (zaehlt nicht): Higashikawa-Halbzone (der
  2x2-Block der unteren Floquet-Baender; kein endlichreichweitiger Automat auf eigenem Torus, T4).
- **DT2:** nicht auswertbar, wenn DT1 nicht eingetroffen ist (Karte: "Wenn DT1"). Sonst: tiefster Kegel bei
  Quasienergie 0 ungepaart (Netto-Chiralitaet der Luecke bei 0 ungleich 0) und isotrop: (max - min)/Mittel der
  Kegelgeschwindigkeit <= 0,10 bei |k| = 0,05. Vermerk: dieselben Groessen fuer den Higashikawa-Halbzonenblock.
- **DT3:** eingetroffen genau dann, wenn der reine Dreieckstakt ("voll") in beiden Reihenfolgen in jeder der beiden
  Luecken einseitigen Randfluss hat (N_oben ungleich 0, N_unten = -N_oben, N_bulk = 0) und die Umkehr das Vorzeichen
  dreht (N_oben(umgekehrt) = -N_oben(vorwaerts) in jeder Luecke). Nicht eingetroffen sonst. Vermerke: lam3, lam4.
- **Kartenwortlaut:** DT0 bis DT3 wie oben. Lesart DT1: "endlichreichweitiger 3D-Automat" heisst: die ganze
  Floquet-Unitaere ist auf ihrem Torus ein Laurent-Polynom. Die Halbzone von Higashikawa u. a. ist das nicht; ich
  nenne sie getrennt.

## 5. Rauchlauf, Sichtregel, Laufplan

- Rauchlaeufe (Modus rauch): P3 klein (W3 der Produkte, Takte, Higashikawa sichtbar: Kontrollen bzw. Literatur), H2
  (Chern-Zahlen sichtbar, Randfluss nicht geschrieben), LM klein (Trefferzahl und Zeit, W3 nicht geschrieben).
- Hauptlaeufe: H-P3 (p4000b), H-H2 und H-LM (p4000a), danach auswertung2.py.

## 6. Rauchlaeufe [R] und Aenderungen vor dem Einfrieren

- Rauch P3a (14:50 UTC): Abbruch, windung.py aus Teil 1 hat kein fib_dirs -> eigene Funktion in teil2.py.
- Rauch P3b (14:52 UTC, rc = 0): Produkte |W3| <= 8e-15 bei N_exakt; Dreieckstakt (theta = pi/3, beide Drehsinne)
  ~1e-16 (N_exakt = 7, das Produkt hat nur Frequenzen bis 1); Additivitaet S1 R und R S1 = -1,000000. **Higashikawa
  falsch gelesen:** Kegel bei k = 0 quadratisch, Rand +sigma_0. Ursache: Ich hatte U_j^+- = P_j^+- e^{-ik} + P_j^-+
  gelesen; Eq. (2) (Spin +- springt um +-e_j) und die Entwicklung "U_j^+-(k) ~ sigma_0 -+ i P_j^+- k" (S. 2) verlangen
  e^{-+ik}. Berichtigt; dazu Nachbaupruefung an der Quellformel cos eps = 2 cos^2(k1/2) cos^2(k2/2) cos^2(k3/2) - 1.
- Rauch P3c (14:54 UTC, rc = 0), berichtigtes Modell: Formelabweichung 5,6e-16; Rand der Halbbox = -sigma_0 (6,7e-16);
  W3(Halbbox) = -0,99999994 (N = 64), also W = -W3 = +1 wie in der Quelle; andere Haelfte +1,0; ganzer feiner Torus
  ~2e-16; Kegel bei k = 0 isotrop mit v = 1,0000 (Spannweite 3,4e-5 bei |k| = 0,05); U(k3 = 2 pi) = sigma_0 (zweite
  Entartung bei Quasienergie 0 in der anderen Haelfte). Das habe ich vor dem Einfrieren gesehen (Literaturkontrolle;
  der ganze Torus zaehlt zu DT1, Selbstanzeige).
- Rauch H2a (14:50 UTC, rc = 0, JT = pi/16 wie Fig. 6): lam4 hatte Chern +-1 statt 0, und die Quasienergien erreichen
  pi gar nicht (Summe der Schrittnormen <= 3 pi/8 bei lambda = 4), also kann die Luecke bei pi nicht schliessen. Der
  Text nennt fuer die Chern-Rechnung "J/omega = 3/32", also JT = 3 pi/16. -> JT = 3 pi/16 [F]; die Angabe "JT = pi/16"
  in Fig. 6 passt dazu nicht (offen, Selbstanzeige). Ausserdem war die Lueckensuche gitterempfindlich (Scheinluecken
  ~0,02 aus der Abtastung): Gitter 162 (Dirac-Punkte auf dem Gitter) und Vorbedingungen ueber den kleinsten Abstand der
  Eigenphasen zu 0 bzw. pi; Randfluss mit 1200 k-Werten und der Regel "Vorzeichenwechsel, und einer der beiden Werte
  liegt in der halben Luecke" (dort gibt es nur Randzustaende).
- Rauch LM a (14:51 UTC): 4 Treffer von 4, aber 27 s je Start mit Differenzen-Jacobi -> analytische Jacobi-Matrix.
- Keine Urteilsregel und keine Vorhersage nach einem Rauchergebnis geaendert; Randfluss und LM-W3 im Rauchlauf nicht
  geschrieben.
