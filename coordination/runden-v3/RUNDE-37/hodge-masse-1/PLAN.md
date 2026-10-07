# HODGE-MASSE-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Start 2026-10-05 09:25:54 CEST (date). Plantext ab 09:53:21 CEST (date), vor jeder Hauptrechnung. Zeitbox 150 min,
  also bis 11:55:54 CEST.
- Bindend: KARTE.md (HM0 bis HM4, Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] vorab ableitbar (eigene Mathematik), [E] gerechnet, [P] Projektdatei, [L] Literatur/Gedaechtnis,
  [F] Festlegung, [H] Hypothese oder Lesart. Alles synthetische Gitterrechnung, keine Messdaten.
- Code (code/): unveraendert kopiert ew.py, tp.py, tti.py, nachtrag_kinetik.py (TT-ISO-1), tg.py (TT-GLAS-1),
  dn.py (DEFEKT-NETZ-1), td.py, tu.py, uk.py, mn.py, tg_auswertung.py (TAKT-DYNAMIK-1); sha256 wie in den
  Herkunftsordnern (ew fa7b6417, tp 419d7da6, tti 6d6b6f7b, tg ec48a258, dn 0cd5d13e, td fbc02c48). Neu: hm.py
  (Spektren, HM0, HM1), hm_td.py (Umklapp-Aufbau mit anderer Bewegungsenergie), hm_aw.py (Auswertung, Bild).
- Zusatz der Leitung 09:4x (Codex-Gegenblick, sechs Vorbehalte): eingearbeitet in 0.4, 2, 6 und 7, vor dem Einfrieren.

## 0. Erste Schreibtischaufgabe: Was tun R1 und R2? Ist eine davon horizontal?

### 0.1 Was der Code tut [Codelesung]

- Modell (ew.py, tg.py): Kantenwerte a, H = 1/2 p^+ A p + 1/2 a^+ B a. A ist die Hamilton-Form (inverse Masse), B die
  Regge-Steifigkeit, M die Eckverschiebung (B M = 0), c die skalare Regel je Ecke (c^+ M = 0).
- S = orthonormales Komplement von Bild[M, c] (euklidisch, QR/SVD).
- **R1** (ew.spektrum_punkt, tg.punkt, tti A1R1/A2R1, TAKT-DYNAMIK-1): A_red = S^+ A S, B_red = S^+ B S,
  omega^2 = eig(A_red B_red). Also a und p beide in Bild S.
- **R2** (nachtrag_kinetik, tti A3R2, TT-GLAS-2 (c)): A_red = (S^+ A^-1 S)^-1 = (S^+ K S)^-1, also die Lagrange-Form
  K = A^-1 auf Bild S eingeschraenkt.
- TAKT-DYNAMIK-1 (Bloch-k = 0, Kasten): S = Komplement von Bild[M ohne Translationen, c ohne eine Spalte, 1_E], sonst R1.

### 0.2 Ableitung [M]

- **Eichanteil.** Die Verschiebungsregel M^+ p = 0 ist erster Klasse (IMPULS-NETZ-1 4.1). Ihr Loesungsraum ist der
  Annullator von Bild M und braucht keine Metrik. R1 legt p in Bild S, also in diesen Annullator.
  - Ohne skalare Regel ist R1 damit genau die symplektische Reduktion. Mit K = A^-1 gilt
    (S^+ A S)^-1 = S^+ K S - S^+ K Q (Q^+ K Q)^-1 Q^+ K S (Schur-Komplement, Q Basis von Bild M). Das ist der
    Stationaerwert von K(v + g) ueber g in Bild M, also die horizontale Form der Karte, sofern Q^+ K Q regulaer ist.
  - Unabhaengig von der Eichflaeche: Fuer jede andere Flaeche W = S + M X gilt W^+ S = 1 und W^+ B W = S^+ B S
    (B M = 0). Die omega^2 sind dieselben.
- **Skalare Regel (zweiter Klasse).** Richtig behandelt (Dirac) gehoert zu c^+ a = 0 die Folgeregel
  d/dt (c^+ a) = c^+ A p = 0.
  - Reduzierter Raum: Lagen in ker c^+ modulo Bild M; Impulse in Pi_RH = Komplement von Bild[M, A C] (C Basis von
    Bild c).
  - Formel: **RH**: A_red = S^+ (A - A C (C^+ A C)^-1 C^+ A) S. Lagrange-Form: K_red(q) = Stationaerwert von K(S q + g)
    ueber g in Bild M; c wirkt dabei holonom.
  - R1 verlangt statt dessen c^+ p = 0. Gleichwertig: R1 bildet den Stationaerwert von K auch ueber die
    euklidischen c-Richtungen, behandelt die Regel in der Bewegungsenergie also wie eine Eichung.
  - R1 = RH genau dann, wenn A Bild c in Bild[M, c] abbildet. Der Spur-Eichdefekt aus TT-ISO-1 (A c_v nicht in Bild M,
    0,9) spricht dagegen, entscheidet es aber nicht [P].
  - Die c-Behandlung von R1 haengt an der euklidischen Gleichsetzung des Kovektors c^+ mit dem Vektor c. In einer
    anderen Metrik G der Kanten wird daraus p senkrecht auf G^-1 c.
- **R2.** K auf Bild S ohne Stationaerwert ueber die Eichung. Die c-Regel ist holonom und richtig behandelt; der
  Eichanteil haengt an der Flaeche (nicht horizontal).

### 0.3 Antwort vorab (Frage 1, erster Teil) [M]

- **R1 ist in der Eichung horizontal (symplektisch), in der skalaren Regel nicht** (falsche Folgeregel c^+ p = 0
  statt c^+ A p = 0).
- **R2 ist in der skalaren Regel richtig, in der Eichung nicht horizontal.**
- Keine der beiden ist RH.
- Folge nach Karte (Abschnitt "Erste Schreibtischaufgabe"): Der Eichteil von HM1 ist fuer R1 schon entschieden (R1 ist
  in der Eichung flaechenunabhaengig). Er wird nur als Kontrolle gerechnet: "ohne c", R1 auf Sigma_E gegen
  RH-Lagrange auf Sigma_G1, alle omega^2, erwartet Rundung.
- Was R1 von RH trennt, ist die c-Behandlung; das rechnen HM1 (Definition G, 2) und der Reduktionsvergleich (3).

### 0.4 Vorbehalte (Codex-Gegenblick, Leitung 09:4x) und eigene Rauchbefunde

1. **Vertikale Positivitaet:** min_g K(v + g) setzt Q^+ K Q > 0 voraus.
   - Die DeWitt-Form mit lambda = 1 ist auf der laengs gerichteten Eichung langwellig entartet:
     G(sym(k x k^)) = |h|^2 - (tr h)^2 = 0 [M].
   - Fuer A2L (Lagrange-Summe von DeWitt-Formen) ist die Lagrange-Route deshalb bei kleinem k schlecht gestellt.
   - Darum: **RH ist die symplektische Route** (Impulse senkrecht auf Bild[M, A C]). Die Lagrange-Route laeuft als
     Variante A2LRHL und als Gegenprobe.
   - Gemessen wird je Netz an den TT-Richtungen (|k| klein): Q^+ K Q (Zahl negativer Eigenwerte, kleinster relativer
     Betrag) fuer A1, A2, A2L, dazu C^+ A C (Dirac-Bedingung). Netze ohne vertikale Positivitaet werden gemeldet.
2. **Horizontal ist nicht die einzige zulaessige Eichfixierung.** Geprueft wird, ob die physikalischen Frequenzen bei
   symplektischer Behandlung von der Eichflaeche unabhaengig sind (Satz, [M]) und ob R1 das erfuellt. Nicht behauptet
   wird, nur RH sei richtig.
3. **"Unprojiziert 0 %"** (TT-GLAS-2 (e)) zeigt keine isotropen physikalischen Moden, denn unprojiziert sind
   Eichmoden enthalten.
4. **HM4 < 1e-4** belegt keinen exakt erhaltenden Taktschritt. Getrennt ausgewiesen werden der Sprung der
   Bewegungsenergie (Massenform) und die Regularitaet von A_red nach dem Zug.
5. **Endliches Tor:** Die Urteile sind Schwellen; keines verlangt exakt verschwindende Anisotropie.
6. **Rang 4:** Summe *1 l l^T = Vol I (Rang 2) erzwingt keine Rang-4-Isotropie (Gegenbeispiel: Achsen mit Gewicht 1).
   Die Kette in 6 benutzt statt dessen die tensorielle Rekonstruktion je Tetraeder (Phi_t^-1), also die affine
   Patch-Identitaet von HM0.
- **Rauchbefunde vor dem Plantext** (nur Code-Gegenproben, Laufzeiten und Startbarkeit gelesen, keine Spannen,
  Energien oder Urteile):
  - A0 = Phi GH Phi^T auf 1,6e-15; A2_t K_t = 1 je Tetraeder auf 1,3e-9 (Glas), 1e-15 (V, A15).
  - A1 aus A0 = tg-A (0); c^+ M = 5e-16.
  - R1 von A2L = K-Schur ueber Bild[M, c] (1,7e-14).
  - RH fuer A1: Hamilton gegen Lagrange 5,7e-14 (Glas), 1,2e-16 (V).
  - RH fuer A2L: Hamilton gegen Lagrange 4e-9 (Glas), 1,2e-8 (A15), aber **5,07 bzw. 0,84 auf V** ([100]).
    Lesart: vertikale Entartung (0.4 Punkt 1); wird gemessen.
  - **Umklapp-Kasten (k = 0, Glas s1): A_red positiv definit nur fuer A1R1 und A2R1.** A1RH: 9 negative Richtungen,
    A2RH: 5, A2LR1: 28, A2LRH: 46 (von m = 481). In td.py bricht ein Lauf dann ab.
  - Laufzeiten: V und A15 je unter 1 s, Glas N = 128 etwa 9 s je k-Punkt (bis 29 s mit Gegenproben), td A2R1 eine
    Periode 4,4 s (N_T = 183, omega_max = 38,0; die Mode hatte 4 Ereignisse), Messarm eine Periode 4,8 s.
  - Absturzprobe der Kette r10 bis r13 (07:57 bis 07:58 UTC): hm.py V voll, td A2R1 und Messarm je eine Periode, dann
    hm_aw.py auf diesen Probedaten (rauch/test). Gelesen nur Rueckgabewerte (alle 0) und Schluessel; kein Wert, keine
    Urteilszeile.

## 1. Bewegungsenergien (Formeln) [F]

- Je Tetraeder t: Phi_t[p, s] = n_p^T B6_s n_p, TR_s = tr B6_s, V_ref = V_Kasten / T (nur Skala, die Spanne haengt
  nicht davon ab).
  - **A1** (J = 1, Hamilton-additiv): A = Summe_t A0_t mit A0_t = Phi_t (1 - TR TR^T/2) Phi_t^T = (n.n)^2 - 1/2.
  - **A2** (Kartenformel, TT-ISO-1-A2): A = Summe_t (V_ref/V_t) A0_t (Hamilton-additiv).
  - **A2L** (Lagrange-additiv, = TT-ISO-1-A3 mit J = 1): K = Summe_t (V_t/V_ref) Phi_t^-T (1 - TR TR^T) Phi_t^-1,
    A = K^-1. DeWitt mit lambda = 1: G(h) = |h|^2 - (tr h)^2.
- **Je Tetraeder sind A2 und A2L invers** (A2_t K_t = 1) [M, im Rauchtest bestaetigt]. Global nicht: Die
  Lagrange-Form von A2 ist die Infimal-Faltung der Tetraederformen (die Kantenrate wird auf die Tetraeder verteilt).
  A2L ist die Summe [M].
- **Lesarten von "A2" fuer die Urteile:**
  - nach Kartenwortlaut: A2 = Kartenformel; dahin zeigen die Vergleichszahlen (A2R1 5,92 %).
  - nach Plan: A2 = A2L. Nur fuer diese Form gelten die Begruendungen der Karte zu HM0 ("jedes Tetraeder hat dasselbe
    g-Punkt") und zu HM4 ("2 bzw. 3 Tetraeder zerlegen die Bipyramide verschieden").
  - Beide werden gerechnet und gemeldet.

## 2. Reduktionen und Eichflaechen [F]

- Varianten je k (hm.punkt): A1R1, A1RH, A2R1, A2RH, A2LR1, A2LRH (symplektisch), A2LRHL (Lagrange-Route),
  A2LR2 (= A3R2).
- **Zwei Eichflaechen fuer HM1** (auf V):
  - Sigma_E = ker M^+ in ker c^+ (Code).
  - Sigma_G1 = ker(M^+ G1) in ker c^+, G1 = diag(U(0,25; 4)) je Kante mit Saat 41, wie die Eichprobe in IMPULS-NETZ-1
    (inz.py); Vertreter W = S - M (M^+ G M)^-1 M^+ G S.
  - Beschreibend Sigma_G2 (Saat 43).
- **Auf Sigma_G** gerechnet (alle generalisierten Eigenwerte basisfrei):
  - RH symplektisch: Impulse Pi = Komplement Bild[M, A C], gepaart mit W, K_q = Gm (T^+ A T)^-1 Gm^+, Gm = W^+ T.
  - RH Lagrange: Schur von K auf W ueber Bild M.
  - R1-G (Definition G, das R1-Rezept in der G-Metrik, in der Sigma_G orthogonal ist): Impulse senkrecht auf
    Bild[M, G^-1 c], gepaart mit W.
  - R1-P (Definition P, woertlich): orthonormale Basis von Sigma_G, a und p darauf eingeschraenkt.
  - R2: K auf W.
  - Ohne c (nur Eichung): R1 auf Sigma_E gegen RH-Lagrange auf Sigma_G1, alle omega^2 (A1).

## 3. Netze, k, Messgroessen [F]

- **Netze:**
  - V, S (ew-Netze ueber dn.netz_ew; S = C15 nach DEFEKT-NETZ-1).
  - A15 (dn.baue Delaunay).
  - Glas N = 128, Saaten 1 bis 4 (tg.zufallsnetz).
- **Kristalle:** 13 Richtungen tti.richtungen13 (Keil), |k| = 1e-3 und 2e-3; Spanne = max/min - 1 ueber 52 Werte
  omega^2/k^2 (wie TT-ISO-1).
- **Glas:** 13 Richtungen tg.richtungen13w (Halbkugel), |k| = 1e-2; Spanne ueber 26 Werte (wie TT-GLAS-1/2).
  |k| = 2e-2 nur an [100], [110], [111] (Linearitaet).
- **Masselose Moden:** die zwei betragsgroessten Eigenwerte von Z = L^-1 K_red L^-+ (B_red = L L^+).
  - "ok": beide positiv, Luecke |ev3|/|ev2| < 1e-2.
  - Eine Spanne gilt nur, wenn an allen Punkten ok.
  - Dazu TT-Anteil an [100], [110], [111] (tensor_fit), Zahl negativer Richtungen und, beschreibend, der Ritz-Wert auf
    den projizierten affinen TT-Wellen (wie TT-GLAS-2 (b)).
- **Beschreibend:** affine Steifigkeit (tg.affin), vertikale Positivitaet (0.4 Punkt 1).
- **HM0:** gleichmaessige Verzerrungsrate v_e = n_e^T h n_e bei k = 0, 6 Basistensoren und 3 zufaellige symmetrische h
  (Saat 7).
  - Fehler = |K_disk(v) - (V_Kasten/V_ref) G(h)| / ((V_Kasten/V_ref) |h|^2), Maximum ueber die 9 h.
  - A2L: v^T K(0) v. A2: v^T A2(0)^-1 v.
- **Zwei Abweichungen von der Karte (Rauchbefund):**
  - Je Glasnetz zwei Laeufe (Richtungen 0 bis 6 und 7 bis 12), zusammengefuehrt in hm_aw.py.
  - Fuer die Spanne zaehlt nur |k| = 1e-2 (wie TT-GLAS-1/2).

## 4. Umklapp-Aufbau (Frage 3) [F]

- td.py unveraendert. hm_td.py ersetzt nur die Bewegungsenergie A (A2, A2L, V_ref = V_Kasten/T der Ausgangszerlegung,
  fest ueber alle Zuege) und wahlweise die Reduktion (RH mit C = [c, 1_E]).
- Gleich: Netze glas-N128-s1 bis s4, A = 1e-3, Arm b (Delaunay-Zuege), Lesart R (Laengen und Raten stetig, Projektion
  auf die neue Zwangsflaeche, y' = A'_red^-1 xd'), h = 0,5, 10 Perioden, Budget 500 s je Abschnitt, hoechstens 4
  Abschnitte.
- **Startbar** (Rauchbefund 0.4) sind nur A1R1 und A2R1, weil A_red sonst nicht positiv definit ist.
  - Hauptarm (Wortlaut): **A2R1**, Saaten 1 bis 4, Arm b, und Arm a (feste Zerlegung, Verlet-Bezug).
  - Plan-Lesart A2L: im Kasten nicht startbar (A2LR1 28, A2LRH 46 negative Richtungen in s1). Ist das in allen vier
    Netzen so, ist HM4 nach Plan "nicht entscheidbar" (gezaehlt im Lauf).
- **Messarm (beschreibend, kein Urteil):** auf der unveraenderten A1R1-Bahn (Saaten 1 bis 3, Arm b; zugleich Kontrolle
  gegen TAKT-DYNAMIK-1). An jedem Zug die reduzierte Bewegungsenergie 1/2 xd^T A_red^-1 xd vor und nach dem Zug fuer
  A1, A2, A2L x R1, RH.
  - Bezug je Form: ihr Wert am Start (x = 0, alles kinetisch).
  - Das trennt die Stetigkeit der Massenform von der Dynamik (Vorbehalt 4).
- **Messgroessen:**
  - dH, dK, dV je ausgefuehrtem Zug relativ zu H0, getrennt nach 2-3 und 3-2; Mittel und Maximum des Betrags je Lauf.
  - Drift Ende und Maximum.
  - A_red positiv definit nach jedem Zug (eig_nach), omega_max dt.

## 5. Kontrolle HM0 und weitere Kontrollen

- HM0 wie 3.
- Reproduktion (Kontrolle des Codes, geht in kein HM-Urteil ein; Schwelle 1e-4 relativ):
  - V: A1R1 6,3388 %, A2R1 5,924 %, A2LR2 3,182 %. S: 2,685 %, 6,408 %, 0,303 %. A15: A1R1 0,934 %.
  - Glas s1 bis s4: A1R1 10,93 / 11,38 / 23,70 / 12,46 %, A2LR2 8,19 / 7,18 / 8,01 / 8,54 % (TT-GLAS-2, gerundet,
    also Schwelle 0,01 Prozentpunkte).
  - Messarm s1: 31 Zuege, Ende-Drift -0,0406 (TAKT-DYNAMIK-1).
- Code-Gegenproben je Lauf: siehe Rauchbefunde (0.4), RH Hamilton gegen Lagrange fuer A1 und A2.

## 6. Bausteine verketten (vor dem Einfrieren)

- **HM0:**
  - A2L: Identitaet [M]. Gleiche Rate je Tetraeder gibt Summe_t (V_t/V_ref) G(h) = (V_Kasten/V_ref) G(h), weil die
    Tetraeder den Kasten fuellen. Vorab ableitbar, also eine Kontrolle und keine Messung.
  - A2 (Kartenformel): vorab ableitbar verfehlt [M]. Die Infimal-Faltung verteilt die Kantenrate auf die
    Tetraeder; der Wert weicht deshalb vom Kontinuumswert ab, die Groesse ist offen.
- **HM1:**
  - RH-Teil: Flaechenunabhaengigkeit der symplektischen Reduktion ist ein Satz [M, L]; vorab ableitbar, als Kontrolle
    der Umsetzung gerechnet (zwei verschiedene Formeln).
  - R1-Teil nach Plan (Definition G): R1 ist in der Eichung kanonisch. Eine Flaechenabhaengigkeit kommt nur ueber
    c -> G^-1 c; sie verschwindet, wenn A c in Bild[M, c, G^-1 c] liegt. Ihre Groesse ist nicht ableitbar.
  - R1-Teil nach Wortlaut (Definition P): Die Impulse verletzen M^+ p = 0, also ist eine Abhaengigkeit generisch zu
    erwarten; die Groesse ist offen.
- **HM2/HM3 mit A2L und RH (Kette [H, nicht bewiesen]):**
  1. Patch-Identitaet von HM0.
  2. Fuer periodisches xi ist Summe_t V_t sym(grad xi)_t = 0 (diskreter Divergenzsatz). Damit ist eine gleichmaessige
     Rate K-orthogonal zu allen periodischen Eichmoden.
  3. Fuer die langen Eichmoden gilt G(h_TT, sym(k x xi)) = 0, weil TT senkrecht auf k steht.
  4. Ein linearer Verzerrungsanteil ist Eichung (quadratisches xi). Also B a_aff = O(k^2) und c^+ a_aff = O(k^2).
  5. Die affine Steifigkeit ist isotrop (TT-ISO-1 2,5e-8, TT-GLAS-2 1,7e-5 [P]).
  - Folge: omega^2/k^2 ist in fuehrender Ordnung isotrop, Spanne O(k^2), **sofern das reduzierte Problem regulaer
    ist**.
  - Vorbehalt 1 (vertikale Entartung bei lambda = 1) und die Rauchbefunde (A2LRH im Kasten indefinit) koennen genau das
    verhindern: zusaetzliche weiche oder negative Moden, dann "nicht ok".
  - Fuer A2 (Kartenformel) gibt es keine solche Kette.
  - Erwartung des Agenten (kein Urteil): HM2 nach Plan 50 %, nach Wortlaut 15 %.
- **HM4:** Fuer gleichmaessige Rate auf der Bipyramide erhaelt A2L den Sprung exakt (Patch-Identitaet). Die Mode hat
  aber k l ~ 1,5, die Rate aendert sich ueber eine Bipyramide um O(1). Ableitbar ist nichts; erwartet wird ein
  kleinerer, aber nicht verschwindender Sprung [H]. Fuer A2 (Kartenformel) gibt es keine Identitaet.

## 7. Urteilsregeln (mechanisch in hm_aw.py)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| HM0 | A2L: Fehler (3) <= 1e-12 auf V, S, A15 und Glas s1 bis s4 -> eingetroffen | dasselbe mit A2 (Kartenformel) |
| HM1 | V, A1, 26 k x 2 Zweige: (i) max rel. Abstand RH(Sigma_E, Dirac-Formel) gegen RH(Sigma_G1, symplektisch gepaart) <= 1e-10 und (ii) max rel. Abstand R1(Sigma_E) gegen R1-G(Sigma_G1) > 1e-4 -> eingetroffen; sonst verfehlt; nicht alle Punkte ok -> nicht entscheidbar | (i) wie Plan, (ii) mit R1-P |
| HM2 | Spanne(V, A2LRH, 52 Werte) < 1e-3 und alle Punkte ok -> eingetroffen; ok nicht ueberall -> nicht entscheidbar | Spanne(V, A2RH) < 1e-3 (sonst wie Plan) |
| HM3 | Mittel ueber s1 bis s4 der Spanne(Glas, A2LRH) <= 0,5 x Mittel der Spanne(Glas, A1R1), beide hier gerechnet -> eingetroffen; ein Netz nicht ok -> nicht entscheidbar | Mittel Spanne(Glas, A2RH) <= 7,65 % (= 15,3 % / 2) |
| HM4 | A2L im Aufbau (R1): Mittel von abs(dH)/H0 ueber die 2-3-Zuege < 1e-4 in jedem Lauf mit 2-3-Zug -> eingetroffen; Lauf nicht startbar (A_red indefinit) -> nicht entscheidbar | A2 (Kartenformel), R1: jeder ausgefuehrte 2-3-Zug in den b-Laeufen s1 bis s4 mit abs(dH)/H0 < 1e-4 -> eingetroffen; kein 2-3-Zug -> nicht entscheidbar |

- Fehlen Laeufe, werden die vorhandenen gewertet und vermerkt; fehlt eine Seite ganz: nicht entscheidbar.
- Beschreibend (kein Urteil): A1RH, A2LR1, A2LRHL, Ritz-Spannen, Sigma_G2, Messarm, vertikale Positivitaet.

## 8. Laufliste (.69, kleintest.sh, Spuren cpu8, cpu9, cpu10, sonst cpu3, cpu4; je Lauf <= 600 s)

| Lauf | Spur | Aufruf (im Ordner /home/fmh/fmhc-physics-remote/hodge-masse-1) | Schaetzung |
|---|---|---|---|
| sp-V, sp-S, sp-A15 | cpu8 | code/hm.py spanne --netz V/S/A15 --out lauf/sp-<netz>.json | je < 30 s |
| sp-glas-s1a/b ... s4a/b | cpu8, cpu9, cpu10, cpu3 | code/hm.py spanne --netz glas-s<i> --ridx 0-6 bzw. 7-12 --out lauf/sp-glas-s<i>-a/b.json | 100 bis 200 s |
| td-A2R1-s<i>-b, -a | cpu9, cpu10, cpu4 | code/hm_td.py lauf --kin A2 --red R1 --netz glas-N128-s<i> --A 1e-3 --arm b/a --budget 500 --out lauf/td-A2R1-s<i>-b/a.json | 30 s bis 8 min |
| td-A2LR1-s<i>-b | cpu4 | wie oben mit --kin A2L (Startbarkeit; Abbruch erwartet) | < 10 s |
| td-mess-s<i>-b (i = 1, 2, 3) | cpu3, cpu4 | code/hm_td.py lauf --kin A1 --red R1 --messformen ... --arm b | 1 bis 5 min |
| aw | cpu8 | code/hm_aw.py --ordner lauf --out lauf/auswertung.json (Urteile, Tabellen, Bild) | < 30 s |

- Laufketten code/kette-<spur>.sh, einmalig per ssh gestartet, kein Dienst. Nicht fertige td-Laeufe werden mit ihrem
  Zwischenstand fortgesetzt (hoechstens 4 Abschnitte). Schlusszeit: nach 11:25 CEST (09:25 UTC) startet kein neuer
  Lauf.
- Laufstand per ssh-Abfrage, keine lokalen Hintergrundaufgaben.

## Nachtrag nach dem Einfrieren: Zusatz der Leitung 10:1x (woertlich aufgenommen 2026-10-05 10:13:34 CEST, date)

- Dieser Abschnitt steht nicht in PLAN.md.eingefroren-20261005-095835 und aendert keine Urteilsregel.
- Wortlaut der Leitung:

> Zusatz der Leitung 10:1x: Befund aus REGGE-KINETIK-L (RUNDE-37/regge-kinetik-l/DOSSIER.md; Literatur, ohne frischen Leser). Deine Vorhersagen und Bedeutungen aenderst du nicht. Bitte so einordnen:
>
> 1. **Standardform der Literatur:** die Lund-Regge-Supermetrik, Summe_tau V(tau) [dh:dh - (tr dh)^2] (Hartle/Miller/Williams 1997, Gl. 3.5 und 3.13). Sie ist volumengewichtet und wirkt auf die **Geschwindigkeiten** (Lagrange-Seite).
>    - Unser Code (TT-ISO-1, IMPULS-NETZ-1) legt die DeWitt-Form je Tetraeder auf die **Impulse** (Hamilton-Term, J = inverse Masse).
>    - Je Tetraeder ist das die Umkehrung, ueber geteilte Kanten summiert aber nicht dasselbe.
> 2. **Antwort auf die Rueckfrage des Literaturagenten:** "A2" in deiner Karte meint die volumengewichtete Fassung aus TT-ISO-1, also die **impulsseitige**. HM0 ("gleichmaessige Verzerrung = Kontinuumswert") gilt exakt nur fuer die geschwindigkeitsseitige Lund-Regge-Form.
>    - Verfehlt A2 auf der Impulsseite HM0, ist das kein Codefehler. Urteile dann nach Kartenwortlaut und vermerke es so.
> 3. **R1 ist laut Schreibtischrechnung des Agenten am Code** (nicht gegengelesen) schon die korrekte Dirac-Reduktion: das Skalarpaar (c^H q, c^H p) plus der Quotient nach Eckverschiebungen. Die Frequenzen haengen dann nicht von der Eichflaeche ab, solange B M = 0 und c^H M = 0 gelten.
>    - Fuehre HM1 dann als Identitaetsprobe. Bestaetigt sich das, ist die TT-GLAS-2-"Projektionsanisotropie" kein Reduktionsartefakt; das waere dann ein Befund gegen meinen Verdacht.
> 4. **Wenn es in der Zeitbox ohne Verzug geht:** Rechne einen beschreibenden Zusatzarm mit der geschwindigkeitsseitigen Lund-Regge-Masse.
>    - Dazu gehoert die Legendre-Transformation der ueber Tetraeder summierten Form, nicht die je Tetraeder invertierte.
>    - Messe die TT-Spanne gegen kl auf V und Glas N = 128 und, falls moeglich, den Energiesprung je 2-3-Zug.
>    - Nach Feinberg/Friedberg/Lee/Ren 1984 (Abstract) und Christiansen 2011 (statischer linearisierter Regge-Operator mit L2-Masse) waeren dort langwellig nur Korrekturen der Ordnung (kl)^2 zu erwarten [H].
>    - Geht es nicht, schreib einen Satz dazu. Dann starte ich eine eigene Karte LUND-REGGE-MASSE-1.
> 5. Nimm diesen Zusatz woertlich als "Zusatz der Leitung 10:1x" in PLAN.md bzw. als datierten Nachtrag auf.

- Nachtrag der Leitung 10:1x zu Punkt 4 (woertlich):

> Rechne den Lund-Regge-Zusatzarm bitte NICHT. Ich starte dafuer jetzt eine eigene Karte, LUND-REGGE-MASSE-1, auf den Spuren cpu5 und cpu6. Punkte 1 bis 3 gelten weiter: A2 ist impulsseitig, HM0 entsprechend einordnen, HM1 als Identitaetsprobe fuehren. Deine Aufgabe bleibt sonst unveraendert.

- Umsetzung (Agent):
  - Punkt 4 nicht gerechnet. Anmerkung: A2L dieses Plans (Abschnitt 1) ist nach meiner Lesung bereits die
    geschwindigkeitsseitige Lund-Regge-Form, Legendre-transformiert nach der Summe (A = K^-1). Sie ist mit R1, R2 und
    RH bei kleinem k gerechnet; es gibt keinen kl-Scan.
  - Punkt 3: beschreibender Nachtrag nt2 (code/nachtrag_r1_identitaet.py): R1 mit demselben Paar auf Sigma_G1,
    kanonisch gepaart, gegen Sigma_E; daneben R2.

## Nachtrag nach dem Einfrieren: zweiter Zusatz der Leitung 10:1x (CODEX-REVIEW-R48), woertlich aufgenommen

- Aufgenommen nach dem Lauf des Diagnose-Nachtrags nt3 (siehe unten). Aendert keine Urteilsregel.
- Wortlaut der Leitung:

> Zusatz der Leitung 10:1x: Befund des unabhaengigen Pruefers CODEX-REVIEW-R48 (RUNDE-37/codex-review-r48/REVIEW.md, Punkte HM-A1, HM-A6 und HM-B0). Deine Vorhersagen bleiben unveraendert; bitte vor HM1 bis HM3 beachten:
>
> 1. **HM-A1:** Die Bewegungsenergie im Projekt entspricht laut drei Projektdateien lambda = 1 (den Code hat der Pruefer nicht gelesen). Dann hat der vertikale Eichblock C = R^T A R im Kontinuum in Laengsrichtung den Eigenwert 4(1 - lambda) k^2 = 0. Die Reduktion "Minimum ueber Eichrichtungen" ist bei langen Wellen also nicht sauber definiert.
>    - Gib vor HM1 bis HM3 das Spektrum von C je Netz und k aus.
>    - Hat C dort eine Null- oder negative Richtung, reduziere auf der Impulsseite bzw. zusammen mit der skalaren Regel (R1, Dirac). Kennzeichne die horizontale Reduktion dann als dort nicht definiert, statt Zahlen zu erzwingen.
> 2. **HM-A2:** Der A_h-Teil von HM1 ist vorab ableitbar, weil die Steifigkeit die Eichrichtungen exakt annulliert (B M = 0). Fuehre ihn als Kontrolle.
> 3. **HM-A6 und HM-B0:**
>    - In TAKT-DYNAMIK-1 gab es 31 bis 113 Zuege in 10 Perioden. 1e-4 je Zug laesst also bis ~1,1 % Drift zu.
>    - Ausserdem gilt r_R r_P >= 1: Uebergabe der Raten und Uebergabe der Impulse koennen nicht beide Energie verlieren. Lege die Lesart vorab fest.
>    - Schreib ausdruecklich hin, dass in A2 die Masse proportional zum Zellvolumen ist und nicht die inverse Masse.
>    - Den Satz "energieerhaltender Taktschritt" nicht aus HM4 folgern; berichte nur den gemessenen Sprung und die Drift.
> 4. Ist dein Plan schon eingefroren: Punkt 1 als Diagnose-Nachtrag (beschreibend), Punkte 2 und 3 in die Bedeutung. Nimm das woertlich als "Zusatz der Leitung 10:1x" auf.

- Umsetzung (Agent):
  - Punkt 1: Diagnose-Nachtrag nt3 (code/nachtrag_c_spektrum.py, beschreibend). Spektrum von C = Q^H K Q fuer A1, A2
    und A2L auf V, S, A15 und Glas s1 an [100], [110], [111] bei drei |k|.
  - Die Lesart der Zuege stand vor dem Einfrieren fest: R (Abschnitt 4).
  - RH ist in diesem Plan schon impulsseitig definiert (0.4 Punkt 1); die Lagrange-Route A2LRHL ist nur Gegenprobe.
