# UEBERLEITUNG-KH-1: Plan (Code-Agent fuer die Leitung claude-primary)

- Karte KARTE.md gelesen, UL0 bis UL4 und ihre Bedeutung bleiben unveraendert und bindend.
- Start des Agenten 2026-10-05 13:16:28 CEST (date). Plantext ab 13:37:02 CEST (date), vor jedem Rauchtest und vor jeder
  Rechnung dieser Karte.
- Kennzeichen: [M] Mathematik (Schreibtisch), [P] Projektbefund, [L] Gedaechtnis-Literatur, [H] Hypothese, [F] Festlegung
  dieses Plans, [E] wird gerechnet.
- Synthetisch, linearisiert um flach; keine Messdaten, keine Messdatenbestaetigung.

## 0. Projektsuche (Arbeitsweise Punkt 1)

- grep in runden-v3/RUNDE-*.md nach "Kuhn" (mit den Pflicht-Ausschluessen): 24 Zeilen in RUNDE-36, -37, -38, -44, -49.
  Davon enthaelt nur RUNDE-49.md Z. 120 zugleich "A2L", "RH", "R1" bzw. "Lund": die Startzeile dieser Karte.
- Was es auf dem Kuhn-Gitter schon gibt [P]:
  - REGGE-4D-1: euklidische 4D-Hesse, (1/4) k^2 (P2 - 2 P0s), tote Hyperdiagonale (Thales).
  - REGGE-WELLE-1: echte Zeit ueber k_tau = i omega; v -> 1, zwei laufende Moden, Dispersion = hyperkubisch.
  - REGIME-K-1: Pipeline-Kontrolle KW (Kuhn mit Treppen-Zeltzuegen, rk.py) = REGGE-4D-1; Hoehe tau = 1,5 wirkt
    langwellig nur ueber die Metrik (B1).
  - REGGE-RAND-1 / NEWTON-NACHRECHNUNG: 3D-Kuhn-Eckenoperator = 8 mal (-7-Punkt-Laplace).
  - GLEICHER-KEGEL-1, INDUZIERT-1, schiefes Kuhn-Netz: Skalar-/Graviton-Dispersion, nicht Regime H.
- Regime H (A1, A2, A2L mit R1, RH, R2) ist auf dem Kuhn-Netz nicht gerechnet. Die Kartenzeile stimmt.

## 1. Gitter, Variablen, Normierung

### 1.1 4D-Seite [F]

- 4D-Kuhn-Gitter = rk.baue('KW', tau = h) aus REGIME-K-1 (unveraenderte Kopie rk.py, pt.py): raeumlich das 3D-Kuhn-Netz
  (Wuerfel in 6 Tetraeder, Kantenvektoren d in {0,1}^3 ohne 0, 7 Kanten je Ecke), zeitlich Treppen-Zeltzuege mit Hub h
  (Zeltstangenhoehe), Zeitkoordinate der Ecken h n_t. Das ist das 4D-Kuhn-Gitter von REGGE-4D-1 mit Metrik
  diag(1, 1, 1, h^2) in Gitterkoordinaten (REGIME-K-1: KW = REGGE-4D-1). 15 Kanten je Ecke: 7 raeumliche d und 8
  zeitartige (d, 1), d in {0,1}^3; (0, 1) ist die Zeltstange, (111, 1) die tote Hyperdiagonale (Thales gilt fuer jede
  Diagonalmetrik [M], also fuer jedes h).
- Hesse H_rk = Hesse von S = Summe A eps nach den Kantenlaengen (rk: Hloc = -M, TT negativ). Euklidische Wirkung
  S_E = -Summe A eps = -(1/2) Int sqrt(g) R; also H_E = -H_rk (TT positiv). Variablen a = delta l / l wie im 3D-Code:
  H_a = diag(l) H_rk diag(l).
- Bloch-Form in Basispunkt-Konvention von rk (Phase der Kante = Zelle ihrer kanonischen Startecke), aber analytisch in
  k_t aufgebaut: H_a(k_s, w) = Summe_m C_m(k_s) z^m, z = exp(i w h), m in {-1, 0, 1}, w = euklidische Frequenz
  (physikalisch, Zeit T = h n_t). Kontrolle: gleich rk.Gitter.H bei reellem k (Abschnitt 6).
- Taylor in w exakt aus den Laurent-Koeffizienten: d^j/dw^j bei 0 = Summe_m C_m (i m h)^j.

### 1.2 Abbildung der 4D-Kantenvariablen auf Kantenraten, Lapse und Shift [F, M]

- Euklidische ADM-Form ds^2 = N^2 dt^2 + g_ij (dx^i + N^i dt)(dx^j + N^j dt), t = Gitterzeit (Schritt 1), Hintergrund
  N = h, N^i = 0, g = 1. Fuer die zeitartige Kante (d, 1) von (x, t) nach (x + d, t + 1) gilt linear
  delta s = 2 h dN + 2 d . dN_vec + d^T dg d [M].
- Raeumlicher Anteil der zeitartigen Kante = Mittel der zwei Zeitschichten (zeitsymmetrisch, mit der Inversion
  (t, x) -> (-t, -x) des Kuhn-Gitters vertraeglich) [F]:
  delta s_(d,1)(x, t + 1/2) = sigma_d + (1/2) [delta s_d(x, t) + delta s_d(x, t + 1)].
- Zerlegung des Rests sigma_d in die affinen Teile und den Gitterrest:
  - sigma_0 = 2 h^2 n (Zeltstange; n = a_Stange = physikalische Lapse-Stoerung delta alpha),
  - sigma_(e_i) - sigma_0 = 2 h beta_i (beta = physikalischer Shift dx/dT),
  - sigma_d = sigma_0 + 2 h d . beta + L_d fuer |d| >= 2: vier Gitterreste L_110, L_101, L_011, L_111 (L_111 sitzt nur
    auf der toten Hyperdiagonale und faellt heraus).
- In a-Variablen und Bloch (Basispunkt, Kante (d,1) an der Zelle (x, t)):
  2 (h^2 + |d|^2) a_(d,1) = sigma_d + |d|^2 (1 + z) q_d, a_Stange = n, a_d (raeumlich) = q_d.
  Jacobi-Matrix J(w) = J(z = 1) + (z - 1) J_z; neue Variablen x = (q [7], n, beta [3], L [4]).
- Physikalische Form je Zeiteinheit und Raumzelle (Volumen 1): P(w; h) = -(1/h) J(w)^+ H_a(w) J(w),
  Taylor-Koeffizienten P_p (p = 0 bis 4) exakt.
- Gitterreste: Schur-Komplement der drei lebenden L in der Reihe (D = P_LL, D_0 muss regulaer sein; Reihe der Inversen
  bis Ordnung 4). Ergebnis S_p(h) auf x_K = (q, n, beta), 11 Variablen.
- Begruendung: Ohne zeitsymmetrisches Mittel aendert sich der beta-Wert um O(1) * qdot (einseitige Lage der Kante), und
  M_eff verschiebt sich um Shift-Shift-Terme [M]; mit dem Mittel unterscheiden sich zulaessige Varianten nur um
  O(h) im Shift, was fuer h -> 0 verschwindet [M, H]. Als Empfindlichkeitsprobe (beschreibend, nicht geurteilt) wird
  M_eff zusaetzlich mit dem einseitigen Anteil (z statt (1 + z)/2, obere Schicht) gerechnet.

### 1.3 M_eff, Steifigkeit, Lapse- und Shift-Bloecke [F]

- Euklidisch: S_E-Hesse = w^2 K + V (+ Lapse/Shift), echte Zeit w = i omega.
- Aus S_p(h): M_eff(h) = S_2[q,q] (omega^2-Teil, bei festem n und beta), V_eff(h) = S_0[q,q] (Steifigkeit),
  C(h) = S_0[q,n] (Lapse-Kopplung; Bedingung C^+ q = 0), X(h) = S_1[q,beta] (Shift-Kopplung), Dnn = S_0[n,n],
  Dbb = S_0[beta,beta]; dazu alle uebrigen Bloecke (S_1[q,q], S_1/S_2[q,n], S_p[n,beta], S_1/S_2[beta,beta], S_3, S_4).
- Normierung [M]: 3D-Code: B = Hesse von V = -Summe l eps = -(1/2) Int sqrt(h) R (EH-Normierung S = (1/2) Int sqrt(g) R).
  ADM: Bewegungsteil (1/2) G_L(eps_punkt), eps = Verzerrung (a = n^T eps n), G_L(X) = X:X - (trX)^2. Damit ist die
  erwartete Lund-Regge-Traegheit in derselben Normierung K_LR = Summe_t V_t Phi_t^-T G_L Phi_t^-1 = V_ref * K_A2L
  (K_A2L = hm.tet_geo 'Kt' assembliert, V_ref = 1/6 auf Kuhn, alle V_t = 1/6, also A2 = A1).

### 1.4 Grenzfall h -> 0 und Extrapolationsregel [F]

- h-Folge h_j = 2^-j, j = 0 bis 10 (1 bis 1/1024). Alle Bloecke S_p(h_j) exakt je h.
- Grenzwert Q0 jedes Blocks: kubisches Polynom in h durch die vier kleinsten h (j = 7 bis 10), Wert bei 0.
  Fehlerschaetzung e(Q) = ||Q0 - Q0'|| / ||Q0|| mit Q0' = quadratisch durch j = 8 bis 10.
  **Gueltige Fassung nach Rauchtest r3 (Abschnitt 9):** kubisch durch j = 0 bis 3 (h = 1, 1/2, 1/4, 1/8), Q0' quadratisch
  durch j = 1 bis 3.
- Nach dem Rauchtest darf nur aus technischer Konvergenz (Normen aufeinanderfolgender Differenzen, kein Vergleich mit
  A2L, keine Spektren) der Fitbereich verschoben werden; jede Aenderung wird hier vor dem Einfrieren vermerkt.
- Beschreibend: Ordnung der Konvergenz (Verhaeltnis aufeinanderfolgender Differenzen), S_3 und S_4 gegen 0.

## 2. 3D-Seite (Regime H) auf dem Kuhn-Netz [F]

- Netz: tg.modell(LV = I, pos = [0], G = 6 Kuhn-Tetraeder, O = Eckversaetze) (unveraenderte Kopien tg.py, hm.py, ew.py,
  tp.py, tti.py, dn.py, nachtrag_kinetik.py aus HODGE-MASSE-1). B (Regge), M_disp (Eckverschiebung), c (skalare Regel),
  A1 = A2, K_A2L aus hm.tet_geo; Paarungen ueber hm.punkt (unveraendert): A2LR1 (b), A2LRH (c), A1R1 (Referenz).
- Konvention: 4D-Groessen (Basispunkt rk) werden per Phasenmatrix in die tg-Konvention gebracht: beide auf
  Kantenmitte, F_tg = U^+ F_rk U, U = D_rk D_tg^-1 P (P Kantenzuordnung ueber +-d). Vektoren C ebenso (C_tg = U^+ C_rk).

## 3. Regeln aus dem Grenzfall und Paarungen [M, F]

### 3.1 Erwartete Struktur [M, H] (Schreibtisch, vor der Rechnung)

- Raeumliche 4D-Eckverschiebung (exakt null bei jedem w): (q, n, beta) = (M_disp xi, 0, ~ w xi). Aus S(w) v = 0 folgt
  V_eff M_disp = 0 und X = -i M_eff M_disp Y: der Shift tritt als (qdot - M_disp beta') auf (ADM-Form).
- Zeitliche Eckverschiebung (q unberuehrt): (0, n = i w xi0, beta = grad xi0). Daraus C = M_eff M_disp (grad) bis auf
  Faktor, also M_eff^-1 C in Bild M_disp: die Lapse-Bedingung C^+ q = 0 ist erster Klasse ("Passbedingung").
- Folge: Ist die Grenzform ADM-artig (Lapse rein Multiplikator, Shift ADM, keine w^1-Kreisel-Terme in q, S_3 = S_4 = 0)
  und gilt die Passbedingung, dann ist die exakte Reduktion: q, p im Komplement von Bild[M_disp, C] (Eichfixierung
  M_disp^+ q = 0 und C^+ p = 0). Das ist R1 mit C an Stelle von c. RH (Dirac-Paar C^+ q, C^+ A p) ist dann entartet
  (C^+ A C = 0). Ist C parallel c, ist die Grenzfall-Reduktion woertlich R1 mit A = M_eff^-1.
- Scheitern moeglich: Lapse quadratisch (Dnn != 0), Kreiselterm, Shift nicht ADM, Passbedingung verletzt (dann
  Folgebedingung C^+ A p = 0, also RH-artig).

### 3.2 Regel-Kennzahlen (mechanisch, im Grenzwert, je k) [F]

- Skala sig_k = max_p ||S_p|| |k|^p (p = 0, 1, 2), Frobenius-Normen, tol_s = 1e-6.
- (R-L) Lapse rein Multiplikator: |S_0[n,n]|, |S_1[n,n]| |k|, |S_2[n,n]| |k|^2, ||S_1[q,n]|| |k|, ||S_2[q,n]|| |k|^2,
  ||S_p[n,beta]|| |k|^p (p = 0, 1, 2) alle <= tol_s sig_k.
- (R-K) kein Kreiselterm: ||S_1[q,q]|| |k| <= tol_s sig_k.
- (R-S) Shift ADM: Y = argmin ||X - M_eff M_disp Y||; Rest ||X - M_eff M_disp Y|| / ||X|| <= tol_s;
  ||S_0[beta,beta] - Y^+ M_disp^+ M_eff M_disp Y|| / ||S_0[beta,beta]|| <= tol_s; ||S_2[q,beta]|| |k|^2,
  ||S_1[beta,beta]|| |k|, ||S_2[beta,beta]|| |k|^2 <= tol_s sig_k.
- (R-H) hoehere Ordnungen: ||S_3|| |k|^3, ||S_4|| |k|^4 <= tol_s sig_k.
- (R-P) Passbedingung: ||(1 - P_Mdisp) M_eff^-1 C|| / ||M_eff^-1 C|| <= tol_s.
- (R-c) Lage von C gegen c: sin(C, c) (beschreibend; "C parallel c" wenn <= tol_s), Faktor kappa = c^+ C / c^+ c.
- (R-V) V_eff gegen B: ||V_eff - B|| / ||B|| (beschreibend).
- Dieselbe Passbedingung zusaetzlich fuer (M_eff, c), (K_LR, c) und (K_LR, C) (beschreibend; erklaert R1 gegen RH).
- "Grenzfall-Regeln ADM-artig" an einem k: (R-L), (R-K), (R-S), (R-H) erfuellt. Wird mit e(Q) (Extrapolation)
  verglichen: Kennzahl minus Fehlerschaetzung.

### 3.3 Paarungen auf dem Kuhn-Netz [F]

- (a) Hauptpaarung "M_eff mit den Grenzfall-Regeln": A = M_eff(0)^-1 (Hamilton), Potential B (3D-Regge, wie im
  Regime-H-Code), Regeln aus dem Grenzfall: wenn (R-P) erfuellt: S = Komplement von Bild[M_disp, C(0)], A_red = S^+ A S,
  B_red = S^+ B S (erster Klasse, R1-Bauart mit C); wenn (R-P) verletzt: RH-Bauart mit C (hm.rh_A mit C). Spektrum
  ueber hm.z_auswerten (1/omega^2 = Eigenwerte von L^-1 K_red L^-+, B_red = L L^+).
- (a') beschreibend: wie (a), aber Potential V_eff(0) statt B (volle Grenzform).
- (b) A2L mit R1 = hm.punkt 'A2LR1'. (c) A2L mit RH = hm.punkt 'A2LRH'.
- beschreibend: M_eff mit R1 (Code-c) und mit RH (Code-c); A1R1; die Variante (a) mit Q0' (Fehlerschaetzung).
- RH gilt an einem k als nicht definiert, wenn |c^+ A c| / (||A|| ||c||^2) <= 1e-10 (eine Ecke je Zelle: skalar).
- Wachsende Moden: n_neg aus hm.z_auswerten (negative Eigenwerte von Z). Ist B_red nicht positiv definit:
  Eigenwerte lambda von A_red B_red, wachsend wenn Re lambda < -1e-9 max|lambda| oder |Im lambda| > 1e-9 max|lambda|.

### 3.4 k-Raster [F]

- R13 = tti.richtungen13 (wie HODGE-MASSE-1, Kristalle). Betraege: |k| = 1e-3, 2e-3 (HODGE-MASSE-1) und kl = 0,005;
  0,01; 0,02; 0,05; 0,1; 0,2 mit l = mittlere Kantenlaenge des 3D-Kuhn-Netzes (wie LUND-REGGE-MASSE-1).
- BZ-Gitter L = 8: k = 2 pi m / 8, m in {0..7}^3 ohne 0 (511 k), wie LUND-REGGE-MASSE-1.
- TT-Spanne: je Richtung und Zweig w(kl) = w0 + w2 (kl)^2 + w4 (kl)^4 ueber kl = 0,005 bis 0,1 (fuenf Werte,
  lrm.fit_kl-Bauart), Spanne0 = max w0 / min w0 - 1 ueber 13 x 2; nur wenn alle Fitpunkte regulaer (hm: zwei positive,
  Luecke < 1e-2). Dazu beschreibend Spanne je Betrag.

## 4. UL0: Kontrolle gegen REGGE-WELLE-1 [F]

- h = 1, eigene Laurent-Form (1.1) in Kantenlaengen, festes Komplement Q0 der fuenf Nullvektoren bei k_t = 0
  (4D-Eckverschiebungen rk.G und Hyperdiagonale), F(omega) = Q0^+ (Summe_m C_m z^m) Q0, z = exp(-omega h) bei
  k_t = i omega. Nullstellen mit regge_welle.pep_wurzeln, aberth, windung (unveraenderte Kopie; Schluessel 2m, damit
  dort z' = exp(i k_t h / 2)), Bereich R = (0, 3|k|] x [-0,5|k|, 0,5|k|].
- 24 Richtungen regge_welle.richtungen(), |k| = 0,05. UL0 eingetroffen, wenn an allen 24: Windungszahl 2, genau zwei
  verfeinerte Nullstellen in R, beide v = Re omega / |k| in [0,9997; 0,9999]. Sonst nicht eingetroffen.
- Beschreibend: dieselbe Rechnung bei |k| = 0,2 und fuer h = 1/2, 1/4, 1/8 (Bereich in omega h skaliert).

## 5. Mechanische Auswerteregeln UL1 bis UL4 [F]

Alle k = Raster (3.4, 104 Punkte) und BZ-Gitter (511). "Fehler" = Extrapolations-Fehlerschaetzung (1.4).

- **UL1** (M_eff = A2L, relativ 1e-6): r(k) = ||M_eff(0) - K_LR|| / ||K_LR|| (tg-Konvention, Frobenius), e(k) =
  Fehlerschaetzung von M_eff. Eingetroffen, wenn max_k (r + e) < 1e-6; nicht eingetroffen, wenn max_k (r - e) >= 1e-6;
  sonst nicht entscheidbar. Beschreibend: bester skalarer Faktor kappa* (kleinste Quadrate ueber alle k) und r mit kappa*.
- **UL2** (a: isotrop und stabil): Voraussetzung: Grenzfall-Regeln an allen k ADM-artig (3.2) und M_eff(0) an allen k
  regulaer (Legendre). Sonst nicht entscheidbar.
  - Spanne0 von (a) mit Q0 und mit Q0'; delta = |Spanne0(Q0) - Spanne0(Q0')|.
  - Eingetroffen, wenn Spanne0 + delta < 1e-6 und an allen gerechneten k (Raster und BZ) keine wachsende Mode, weder mit
    Q0 noch mit Q0'.
  - Nicht eingetroffen, wenn Spanne0 - delta >= 1e-6 oder an einem k eine wachsende Mode mit Q0 und mit Q0'.
  - Sonst (oder Fitpunkte nicht regulaer) nicht entscheidbar.
- **UL3** (b: A2L mit R1 anisotrop > 1 %): Spanne0 von A2LR1. Eingetroffen, wenn > 0,01; nicht eingetroffen, wenn <= 0,01;
  nicht entscheidbar, wenn ein Fitpunkt nicht regulaer.
- **UL4** (c: A2L mit RH hat wachsende Moden): eingetroffen, wenn an einem gerechneten k (wo RH definiert) n_neg >= 1;
  nicht eingetroffen, wenn RH an allen k definiert und nirgends wachsend; sonst nicht entscheidbar.
- Kartenwortlaut: wie Plan; wo der Wortlaut weiter oder enger ist, wird es im Ergebnis getrennt genannt (z. B. UL2
  "an allen gerechneten k" = Raster und BZ-Gitter; UL1 "relativ" = Frobenius je k).

## 6. Kontrollen [F]

- K1 Laurent-Form bei reellem k gegen rk.Gitter.H (h = 1 und h = 1/8): max rel. Abweichung <= 1e-12.
- K2 Hermitezitaet C_-m = C_m^+ (<= 1e-12 rel.), 4D-Eichnullvektoren ||H G|| / (||H|| ||G||) <= 1e-12 (auch komplexes
  k_t), tote Hyperdiagonale (Zeile = 0).
- K3 Geometrie je h: rk.kontrollen (Fehlwinkel, Schlaefli, Volumen), Kuhn 3D: tg.modell-Pruefung, B M_disp = 0,
  c^+ M_disp = 0.
- K4 Reproduktion HODGE-MASSE-1 auf V mit den uebertragenen Kopien: hm.lauf_spanne('V') gegen hodge-masse-1/lauf-69/
  sp-V.json, alle acht 'spanne_alle' gleich auf <= 1e-10.
- K5 L-Block D_0 regulaer (kleinster Betrag relativ >= 1e-10) an allen k und h; M_eff hermitesch.
- K6 Symmetrie: Spektren von M_eff(0) und K_LR an k und an der Permutation (k2, k1, k3) (S3 des Kuhn-Netzes) gleich.
- K7 Empfindlichkeit der Abbildung (beschreibend): M_eff mit einseitigem Anteil gegen zeitsymmetrisch.

## 7. Agenten-Vorhersagen (vor jeder Rechnung; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | UL0 eingetroffen | 85 % |
| A2 | Grenzwert existiert (S_p(h) konvergiert, S_3, S_4 -> 0) und die Grenzfall-Regeln sind an allen k ADM-artig mit Passbedingung | 65 % |
| A3 | UL1 eingetroffen (M_eff = K_LR an allen k auf 1e-6) | 35 % |
| A4 | C parallel c (sin <= 1e-6) an allen k | 50 % |
| A5 | UL2 eingetroffen | 60 % |
| A6 | UL3 eingetroffen | 45 % |
| A7 | UL4 eingetroffen | 45 % |
| A8 | V_eff = B auf 1e-6 an allen k | 40 % |

## 8. Laeufe [F]

- Nur auf der .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu8, cpu9, cpu10, je <= 600 s,
  Arbeitsordner /home/fmh/fmhc-physics-remote/ueberleitung-kh-1/ (code/, rauch/, lauf/), Logs mit absolutem Pfad.
- Rauch (je <= 120 s, nach diesem Plantext): r1 technisch (K1 bis K3, K5, Konvergenznormen, Laufzeit), r2 UL0-Maschine an
  einer nicht geurteilten Stelle (nur Zahl der Wurzeln und Laufzeit). Keine Werte zu UL1 bis UL4 ansehen.
- Haupt: h1 Raster + K4 (cpu8), h2/h3 BZ-Gitter in zwei Teilen (cpu9, cpu10), u0 UL0 + Dispersion (cpu10), aw Auswertung
  (cpu8). Code: code/ukh.py (neu), alles andere unveraenderte Kopien.
- Einfrieren: PLAN.md und code/*.py per sha256 (EINGEFROREN-SHA256.txt, Kopien *.eingefroren-<datum>) vor dem ersten
  Hauptlauf; auf der .69 dieselben Summen.

## 9. Rauchtests und Aenderungen vor dem Einfrieren (Nachtrag ab 13:49:20 CEST, date)

- Alle auf cpu8, .69-Zeiten UTC, je unter 2 s Laufzeit.
- **r1** (11:45:14 bis 11:45:16 UTC, code-r1): K1 <= 5,6e-16; K2 hermitesch <= 3,2e-15, Eichnullvektoren bei komplexem
  k_t <= 3,4e-16, tote Zeile <= 3,2e-14; Fehlwinkel <= 4,1e-14 fuer alle elf h; tote Kante nur die Hyperdiagonale (alle h);
  3D-Kuhn-Modell E = 7, T = 6, V_box = 1, V_ref = 1/6, l = 1,28210; B M = 0 und c^+ M = 0 auf 5e-16. L-Block D_0 gut
  konditioniert (kleinster/groesster Betrag ~1). Konvergenznormen: aufeinanderfolgende Differenzen von S_2[q,q] und
  S_0[q,q] <= 1,1e-15 fuer grosse h (die Bloecke haengen nicht von h ab); zu kleinen h waechst nur Rundung (S_0[q,q] bis
  1,2e-10, C bis 1,2e-5 relativ bei kl = 0,01 und h = 1/1024).
- **r3** (11:46:45 bis 11:46:46 UTC, code-r3, neuer Modus rauch3): Normen aller Bloecke S_p(h) je h an zwei k. Gesehen:
  S_0[q,q], S_0[q,n], S_0[beta,beta], S_1[q,beta], S_2[q,q] unabhaengig von h; S_2[q,beta] ~ h, S_3[q,beta] ~ h^2,
  S_4[q,q] ~ h^2, S_4[q,beta] ~ h^3; alle Bloecke n-n, n-beta, S_1[q,n], S_2[q,n], S_1[q,q] null (<= 1e-12).
  Selbstauskunft: Damit habe ich vor dem Einfrieren die Struktur gesehen, die (R-L), (R-K) und (R-H) pruefen, dazu die
  Norm ||S_2[q,q]|| = 5,34 an einem k (ohne Vergleich mit K_LR). Werte zu UL1 bis UL4 (r, Spannen, wachsende Moden)
  habe ich nicht gesehen.
- **r2** (11:46:46 bis 11:46:47 UTC): UL0-Maschine bei |k| = 0,3 (x+, x-): je zwei Wurzeln in R, Windung 2 (nur Zahlen).
- **Codeprobe p-*** (11:47 bis 11:49 UTC, code-r4/r5, Schalter --probe: 2 Richtungen, 8 + 8 BZ-Punkte, UL0 bei |k| = 0,3,
  dann Auswertung): erst Absturz im beschreibenden UL0-Teil (aberth: singulaere Matrix bei h = 1/2); danach laeuft die
  Kette mit rc = 0. Werte der Probe nicht angesehen (nur rc, Laufzeit, Schluessel).
- **Aenderungen vor dem Einfrieren (keine Schwelle, keine Regel geaendert):**
  - Fitknoten (1.4): Weil alle Taylor-Bloecke bis p = 4 Polynome vom Grad <= 3 in h sind (r3) und Rundung zu kleinen h
    waechst (r1), liegt der kubische Fit jetzt auf j = 0 bis 3 (h = 1, 1/2, 1/4, 1/8), Q0' quadratisch auf j = 1 bis 3.
    Der kubische Fit ist dann fuer alle Bloecke exakt; e(Q) misst Rundung und eine etwaige Abweichung vom Polynomgrad.
  - Modus rauch3 und Schalter --probe (nur fuer Rauchtests).
  - Schutz gegen Abstuerze: aberth-Fehler -> unverfeinerte Kandidaten mit Merker 'aberth_fehler'; Inversen ueber
    inv_sicher (Pseudo-Inverse bei Singularitaet, sichtbar ueber Meff_min_rel); Fehler einer Paarung -> 'definiert'
    = False mit Text 'fehler' (zaehlt in UL4 als "nicht definiert", in UL2 als nicht entscheidbar).
