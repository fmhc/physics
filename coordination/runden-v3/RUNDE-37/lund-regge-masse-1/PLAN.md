# LUND-REGGE-MASSE-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Karte KARTE.md bindend; LR0 bis LR4 und ihre Bedeutung unveraendert. Start 2026-10-05 10:12:13 CEST (date).
  Plantext ab 10:38:47 CEST (date), nach den Rauchtests r1 bis r4 (nur Laufzeiten und Schluessel gelesen), vor jeder
  Hauptrechnung.
- Kennzeichen: [M] Mathematik (Schreibtisch, vorab), [P] Projektdatei mit Fundstelle, [E] hier gerechnet (erst im
  Ergebnis), [F] Festlegung dieses Plans, [H] Hypothese, [ES] eigener Schluss.
- **Code:** code/lrm.py (neu). Unveraendert kopiert und importiert: tp.py, ew.py, tti.py, nachtrag_kinetik.py
  (tt-iso-1/code), tg.py (tt-glas-1/code), dn.py (defekt-netz-1/code), inz.py, pn.py, mn.py, nachtrag_iso.py
  (impuls-netz-1/code), smi.py (skalar-misch-1/code), hm.py (hodge-masse-1/code; Hinweis der Leitung 10:2x).
  sha256 der Kopien gleich den Quellordnern (tp 419d7da6, ew fa7b6417, tg ec48a258, tti 6d6b6f7b, dn 0cd5d13e,
  inz e65a5cbf, pn c8034e40, mn b36984d3, nachtrag_iso 1c92cb23, smi 9459838b, hm 0ed5e2ce, nachtrag_kinetik fd0d17b9).

## 0. Zusaetze der Leitung (woertlich sinngemaess, mit Uhrzeit)

- **Zusatz der Leitung 10:1x** (aus CODEX-REVIEW-R48, HM-A1): lambda = 1 im Projekt; die DeWitt- bzw. Lund-Regge-Form
  ist dann indefinit (Spurrichtung), der Eichblock hat im Kontinuum laengs den Eigenwert 4(1 - lambda) k^2 = 0. Daher:
  (a) Spektrum der summierten Masse und des Eichblocks je Netz und k ausgeben; (b) vor der Hamilton-Form pruefen, ob die
  Legendre-Transformation (Invertierung) regulaer ist; (c) mit R1 reduzieren (Dirac, mit der skalaren Regel), nicht ueber
  ein Minimum; (d) ist die Masse nicht invertierbar, ist das ein Ergebnis: keine Pseudoinverse.
  Umsetzung: Abschnitte 1.4, 3, 5.
- **Hinweis der Leitung 10:2x** (HODGE-MASSE-1 fertig, nicht doppeln): R1 eichflaechenunabhaengig; RH zweite stimmige
  Reduktion; A2L (= diese Masse) mit RH TT exakt isotrop, aber wachsende Moden auf jedem Netz; stabil nur R1 mit A1/A2.
  Aufgabe bleibt: Lund-Regge mit R1, kl-Scan, Extrapolation, Stabilitaet an 511 k, Bahnlagen-Gang auf V. Kernfrage
  Stabilitaet: negative Richtungen der reduzierten Masse und wachsende Moden je Netz und k getrennt zaehlen; pruefen, ob
  die Instabilitaet die konforme bzw. Spur-Richtung der lambda = 1-Form ist; A2L-Bausteine aus hodge-masse-1/code nutzen,
  wenn sie zur Formel passen, Formel vorher vergleichen. Umsetzung: 1.3 (Vergleich K1), 5 (Zaehlung, Diagnose).

## 1. Die Masse als Formel

1. **Variablen** wie im Projektcode: a_e = dl_e/l_e (ew.py, Kopf). Kartenvariable q_e = d(l_e^2) = 2 l_e^2 a_e.
2. **Rekonstruktion je Tetraeder t** (6 Kanten, Kantenvektoren x_e): q_e = x_e^T dh_t x_e. Mit dh = Summe_s y_s B6_s
   (tp.B6, Frobenius-orthonormal) ist q = P_t y, P_t[e, s] = x_e^T B6_s x_e, also dh_t = R_t q mit R_t = P_t^-1.
3. **Form:** T = 1/2 Summe_t V_t G_lambda(dh_t', dh_t'), G_lambda(X, Y) = X:Y - lambda tr X tr Y, **lambda = 1**.
   - Fundstelle lambda: ew.py Z. 170 `A0 = (n_e.n_f)^2 - 0.5` = G_p(n n, n n) mit G_p(X, Y) = X:Y - 1/2 tr X tr Y; in 3D
     ist G_p^-1 = G_1 (X:Y - tr X tr Y) [M; REGGE-KINETIK-L 4.1]. Dasselbe G_1 steht in nachtrag_kinetik.py Z. 30
     (`Ginv = 1 - TR TR^T`) und hm.py Z. 34 (`GL`).
   - Summe ueber die Tetraeder (Bloch-Phasen wie tg.ops_BA): K_karte(k) = Summe_t D_t R_t^T V_t G_1 R_t D_t,
     D_t = diag(2 l_e^2) (Variablenwechsel q -> a).
   - **Rechnung mit K = hm.tet_geo `Kt`** (A2L von HODGE-MASSE-1 = A3 von TT-ISO-1/EINE-WELT-LOCH-1 mit J = 1):
     K_t = (V_t/V_ref) Phi_t^-T G_1 Phi_t^-1, Phi_t[e, s] = n_e^T B6_s n_e, V_ref = V_Kasten/T. Es gilt
     K_karte = 4 V_ref K [M] (dh = 2 eps, P_t = diag(l^2) Phi_t). **Kontrolle K1:** je Tetraeder auf <= 1e-12 relativ
     (lauf lr0, beide Wege unabhaengig gebaut). Ein globaler Faktor aendert keine Spanne, keine Traegheit und keinen
     Gang (Gn ist unter A -> A/c invariant [M]).
4. **Legendre (Zusatz 10:1x b, d):** je k Eigenwerte von K: n_neg, n_null (|ev| <= 1e-12 max), kleinster Betrag relativ.
   Nur bei n_null = 0 wird A S = K^-1 S gebildet (Loesung, keine volle Inverse, keine Pseudoinverse). Sonst wird der
   Punkt als "Legendre singulaer" gezaehlt und nicht weiter gerechnet. |ev|min/max < 1e-8 wird als "fast singulaer"
   gezaehlt. H = 1/2 p^+ A p + 1/2 a^+ B a.

## 2. Schreibtischaufgabe: Haelt die Kette? (vor dem Einfrieren) [M, mit P]

**Ergebnis: Die Kette haelt fuer R1 nicht. LR1 ist keine Kontrolle, sondern vorab ableitbar verfehlt.**

1. R1 gibt die reduzierte Geschwindigkeitsmetrik K_red = (S^+ A S)^-1 = S^+ Q S mit Q = K - K X (X^+ K X)^-1 X^+ K,
   X = [M, c] (REGGE-KINETIK-L 4.3; im Code als Kontrolle `R1_gleich_K_schur_ueber_M_und_c`). Langwellig gilt
   omega^2/k^2 = kappa(h) / Q_0(h) + O(k^2), kappa = statisch relaxierte Steifigkeit auf TT (affin isotrop, TT-ISO-1,
   TT-GLAS-2 [P]), Q_0(h) = lim Q(v_aff(h)) fuer k -> 0 (Stoerungsrechnung: Mischterme erster Ordnung sind gegenphasig
   und fallen heraus) [M].
2. **Glied LR0:** K(v_aff(h)) = V_Kasten G_1(h, h) auf jedem Netz, exakt (jedes Tetraeder rekonstruiert h) [M].
3. **Glied Eichung:** bei k = 0 gilt M^+ K v_aff(h) = Summe_t V_t G_1(eps_t(xi), h) = G_1(Summe_t V_t eps_t(xi), h) = 0
   fuer jede periodische Eckverschiebung xi, weil Summe_t V_t eps_t(xi) = Integral sym grad xi = 0 auf dem Torus [M].
   Die akustische Laengsrichtung ist bei lambda = 1 im Kontinuum K-null (Zusatz 10:1x), aber der gemeinsame Block mit c
   ist regulaer: Kontinuum [[1 - lambda, 2 lambda], [2 lambda, 2 - 4 lambda]] = [[0, 2], [2, -2]], det = -4 [M]. Ihre
   Beitraege zu Q_0 verschwinden wie k^2 [M].
4. **Glied skalare Regel (hier bricht die Kette):** c_v = -B w_v. Bei k = 0 ist c_v^+ K v_aff(h) = -w_v^+ B p mit dem
   Impulsmuster p = K v_aff(h) einer gleichmaessigen Verzerrungsrate. p ist kein vertraegliches Laengenmuster, B p ist
   im allgemeinen nicht null; nur die Summe ueber alle Ecken verschwindet (Summe w_v = 2 x globale Skalierung, Nullmode
   von B bei k = 0). Die **optischen** Regelrichtungen (nV - 1 je Zelle) koppeln also mit O(1) an die gleichmaessige
   TT-Rate, und die Dirac-Partnerbedingung c^+ p = 0 zieht diese Kopplung von Q ab [M].
   - Ecksymmetrie: c_v^+ K v_aff(h) ist ein unter der Lagengruppe von v invariantes lineares Funktional von h.
     T_d- und T_h-Lagen (C-Lagen in V, S; 2a in A15): nur tr h, also null fuer TT. D3d-Lagen (Pyrochlor- und H-Lagen in
     V und S, Achse n_v in <111>): alpha n_v^T h n_v + beta tr h, ungleich null fuer T_2g-artige, null fuer E_g-artige h
     (n^T h n = (2/3)(+-h_xy +- h_yz +- h_zx)). D2d-Lagen (A15, 6c, Achse e_a): alpha h_aa + beta tr h, ungleich null fuer
     E_g-artige, null fuer T_2g-artige h [M].
   - Folge: Q_0(h) = V_Kasten |h|^2 + Delta(h), Delta != 0 in genau einer kubischen Klasse (T_2g in V und S, E_g in A15).
     Die TT-Geschwindigkeit ist dann richtungsabhaengig, ausser Delta = 0 zufaellig. Die Groesse von Delta ist nicht
     ableitbar.
5. **Pruefbare Vorhersagen des Mechanismus (vorab, [M]):**
   - P1: V und S, [100]: ein TT-Zweig (E_g, h ~ e_yy - e_zz) liegt genau auf dem unprojizierten affinen Wert w_aff (Code:
     `affin_unproj`), der andere (T_2g, h ~ e_yz) nicht.
   - P2: A15, [100]: der T_2g-Zweig liegt auf w_aff, der E_g-Zweig nicht.
   - P3: [111] auf V, S, A15: beide Zweige entartet (dreizaehlige Achse).
   - P4: Glas: kein Zweig ist durch Symmetrie geschuetzt.
6. **Schon vorhandene Projektzahlen [P], die das stuetzen (Altdaten-Abfrage):**
   - EINE-WELT-LOCH-1, Nachtrag (nachtrag-69/kinetik.json, A3-R1 = diese Masse mit R1): V [100] omega^2/k^2 = 0,0052083
     (= 1/192 genau, der affine Wert in V_Finn-Normierung) und 0,0057584; [111] 0,0055750 doppelt. S [100] 0,0052083 und
     0,0052470. Auf dem 511-k-Gitter: V 142 von 511 k mit Wachstum (kleinstes omega^2 -0,77), S 28 (-0,16).
   - HODGE-MASSE-1 4.2: A2LR1 (= diese Masse mit R1) Spanne V 10,56 %, S 0,743 %, A15 4,69 %; Glas 34,7 % (28 wachsend),
     76,4 % (31), nicht regulaer (33), 950 % (28). A2LRH (Regel nur auf den Lagen, ohne den Abzug aus Punkt 4): TT
     isotrop bis 1e-7 (S, A15). Genau der Unterschied R1 gegen RH ist das Glied aus Punkt 4.
   - Diese Zahlen sind Reproduktionen, keine neuen Messungen. Neu sind: kl-Abhaengigkeit, (kl)^2-Koeffizient,
     Stabilitaet von A15 und Glas, Zaehlung je k, Spurdiagnose, Bahnlagen-Gang.
7. **Ableitbarkeit je Vorhersage (vorab):**
   - LR0: vorab ableitbar [M] (Identitaet), Kontrolle.
   - LR1: vorab ableitbar verfehlt [M, P]; erwartet V ~ 0,106, S ~ 0,0074, A15 ~ 0,047 (Reproduktion).
   - LR4: vorab verfehlt nach [P] (EINE-WELT-LOCH-1: V 142, S 28 von 511 k); die Rechnung reproduziert mit neuem Code.
   - LR3: nicht streng ableitbar (anderes kl), nach [P] (HODGE-MASSE-1 bei kleinem k) sehr wahrscheinlich verfehlt.
   - LR2: nicht ableitbar. [H] Erwartung nach SKALAR-MISCH-1 (Gang und dTT bewegen sich gemeinsam, Verhaeltnis ~0,2;
     hier dTT ~ 10 %): |Gang| ~ 0,02, also verfehlt. Ungeprueft, die Masse liegt nicht in der J-Familie.
   - Spurdiagnose: Jede negative Richtung der lambda = 1-Form hat K-gewichteten Spuranteil > 1/3, denn
     K(v, v) = Summe_t w_t (|eps_t|^2 - (tr eps_t)^2) < 0 verlangt Summe w (tr eps)^2 > Summe w |eps|^2 [M]. "Spur-
     dominiert" ist also vorab ableitbar; offen ist, ob es die oertlichen konformen Richtungen (Span w_v) sind.

## 3. Reduktion R1 (wie im Projektcode) und Pruefungen

- S = orthonormales Komplement von Bild[M, c] (hm.zerlege, wie tg.punkt/ew.spektrum_punkt Z. 316 f.; bei Rangverlust
  SVD mit Schwelle 1e-9). A_red = S^+ A S, B_red = S^+ B S.
- omega^2: masselose Moden ueber Z = L^-1 A_red^-1 L^-+ (B_red = L L^+), hm.z_auswerten: zwei betragsgroesste
  Eigenwerte, "ok" = beide positiv und Luecke |ev_3|/|ev_2| < 1e-2. Alle omega^2 ueber L^+ A_red L (hermitesch,
  Sylvester); ist B_red nicht positiv definit (Gamma), allgemeine Eigenwerte von A_red B_red.
- Wachsend: Re omega^2 < -1e-9 s oder |Im omega^2| > 1e-9 s (s = max |omega^2|). Negative Richtung: Eigenwert
  < -1e-10 max. [M]: Bei positiv definitem B_red ist die Zahl wachsender Moden gleich der Zahl negativer Richtungen von
  A_red. Beide werden trotzdem getrennt gezaehlt (Hinweis 10:2x).
- Pruefungen an [100] und [111], kl = 0,01, je Netz: B M und c^+ M relativ (<= 1e-12; massenunabhaengig, gelten fuer
  jede Masse); K (A S) - S (<= 1e-8); R1 = K-Schur ueber [M, c] (Eigenwerte <= 1e-8 relativ).
- Ausgabe Zusatz 10:1x a: je Punkt Spektrum-Kennzahlen von K, Eichblock Q^+ K Q (Q Basis Bild M) und gemeinsamer Block
  [Q C]^+ K [Q C]; volle Eigenwertlisten von K und Q^+ K Q an [100] und [111] bei kl = 0,01 und am Kasten (k = 0).

## 4. Netze, kl, Richtungen, Extrapolation

- Netze: V, S (= C15; dn.netz_ew), A15 (dn.baue('A15', 'delaunay'), wie HODGE-MASSE-1), Glas N = 128 Saaten 1 bis 4
  (tg.zufallsnetz). Bau ueber hm.netz und tg.modell.
- **kl:** l = mittlere Kantenlaenge des Netzes [F]; kl = 0,005; 0,01; 0,02; 0,05; 0,1; 0,2. (IMPULS-NETZ-1 misst kl mit
  l_P = sqrt(2)/4; nur der Gang in 6 nutzt diese Konvention.)
- Richtungen: Kristalle die 13 von TT-ISO-1 (tti.richtungen13), Glas die 13 Wuerfelachsen (tg.richtungen13w).
- **Spanne(kl)** = max/min - 1 der 26 Werte omega^2/k^2 (13 Richtungen x 2 TT-Zweige), nur aus Punkten mit ok; Zahl der
  ok-Punkte wird mitgegeben.
- **Extrapolation [F]:** je Richtung und Zweig (aufsteigend sortiert) w(kl) = w0 + w2 (kl)^2 + w4 (kl)^4, kleinste
  Quadrate ueber kl = 0,005 bis 0,1 (5 Punkte); Spanne0 = max w0 / min w0 - 1. (kl)^2-Koeffizient: dieselbe Anpassung
  fuer Spanne(kl) (s0, s2, s4) und je Zweig w2/w0 (Bereich).
- Zum Vergleich an denselben Punkten die impulsseitige Paarung A1R1 (J = 1, tg-A).
- Dazu je Punkt: TT-Anteil (tensor_fit) an [100], [110], [111] bei kl = 0,01; affine Ritz-Werte unprojiziert und auf S
  projiziert (P1 bis P3).

## 5. Stabilitaet

- Kristalle: 511 k (L = 8 des jeweiligen reziproken Gitters, ohne Gamma; fuer V und S dieselben k wie TT-ISO-1), dazu
  Gamma beschreibend.
- **Glas [F, Zeitbox]:** 4^3-Gitter der Superzelle, 36 k-Klassen (k und -k zusammen) einschliesslich Gamma, je Saat
  ein Lauf. Grund: ein Glas-Punkt kostet ~7 s (Rauchtest r4); 6^3 (112 Klassen, TT-GLAS-2) braucht ~13 min je Saat.
- Je k getrennt: K (n_neg, n_null, Betrag-min), Eichblock Q^+ K Q (n_neg, min, Betrag-min), gemeinsamer Block,
  Legendre regulaer ja/nein, negative Richtungen von A_red, wachsende Moden, B_red negativ, A1R1 (Kontrolle: n_neg,
  wachsend).
- **Spurdiagnose (Hinweis 10:2x):** fuer jede Eigenrichtung y von A_red die Geschwindigkeit v = A S y; je Tetraeder
  eps_t = Phi_t^-1 u_t; Spuranteil f = Summe w_t |tr eps_t|^2/3 / Summe w_t |eps_t|^2 (rein konform 1, gleichverteilt
  ~1/6); Weyl-Anteil = euklidischer Anteil von v in Span{w_v} (oertliche Umskalierungen, tg.ops Wh). Mittel ueber die
  negativen gegen die positiven Richtungen.

## 6. Bahnlagen-Gang auf V (wie IMPULS-NETZ-1, ohne V1)

- Aufbau wie smi.tabelle (SKALAR-MISCH-1) bzw. inz.kreisbahnen: ew.baue('V'), Spannung Q = ni.Q_map, 200 Richtungen
  pn.richtungen(10, 20), kl = 0,01 mit l_P, 12 Kreisbahnen smi.bahnen() (Saat 31), Impulskopplung J, ohne V1.
- Masse: K aus nachtrag_kinetik.zell_matrizen (Teil 3, V_Finn-Normierung; Faktor ohne Einfluss), A = K^-1 je Richtung,
  dann wie smi.auswerten (A_red, S^+ A P_M sigma). Gang = -b aus G = a + b Summe m_i^4 (smi.gang_fit), G aus
  smi.G_exakt.
- Kontrollen: J_iso reproduziert smi.G_P (<= 1e-8); J = 1 reproduziert IMPULS-NETZ-1 5.2 ([001] 1,00327, [111] 0,99837,
  [110] 0,99960 auf 1e-5).
- Ist A_red an einer der 200 Richtungen nicht positiv definit, ist der Gang nicht definiert (dann Bericht, kein Ersatz).
- Beschreibend: Gang bei k -> 0 (tau_stat, Lagrange ueber |k| = 0,01 bis 0,04 wie smi.gang_null).

## 7. Urteilsregeln (mechanisch)

| Nr | Karte | nach Plan eingetroffen, wenn |
|---|---|---|
| LR0 | Masse bei gleichmaessiger Rate = Kontinuumswert (1e-12), V, S, A15, Glas | lr0: LR0_fehler_max <= 1e-12 auf allen 7 Netzen |
| LR1 | Spanne0 auf V, S, A15 ohne Abstimmung < 1e-6 | auf allen drei: alle Fit-Punkte ok und Spanne0 < 1e-6 |
| LR2 | Gang auf V < 1e-3 | A_red an allen 200 Richtungen pd und abs(Gang) < 1e-3 (kl = 0,01) |
| LR3 | Glas N = 128, kl = 0,05: Spanne <= 1/2 der Spanne mit J = 1 | alle 4 Saaten an allen 13 Richtungen ok und Mittel(LR) <= 0,5 Mittel(A1R1) |
| LR4 | V und S an allen 511 k stabil | V und S: 0 k Legendre-singulaer, 0 k mit wachsender Mode |

- Nach Kartenwortlaut: wie Plan; ist der Gang nicht definiert, heisst LR2 nach Wortlaut "verfehlt" (er faellt nicht unter
  1e-3) und nach Plan "nicht entscheidbar".

## 8. Laufliste (Spuren cpu5, cpu6; je Lauf <= 600 s; Laufzeiten aus den Rauchtests)

| Kette | Lauf | Aufruf (code/lrm.py ...) | erwartet |
|---|---|---|---|
| cpu5 | lr0 | lr0 | < 1 min |
| cpu5 | spV, spS, spA15 | spanne --netz V / S / A15 | je < 1 min |
| cpu5 | stV, stS, stA15 | stabil --netz V / S / A15 | je ~1 min |
| cpu5 | gang | gang | ~1 bis 2 min |
| cpu5 | spG1a/b, stG1, spG3a/b, stG3 | spanne --netz glas-sX --teil 0/1; stabil --netz glas-sX | je ~4,5 bis 5 min |
| cpu6 | spG2a/b, stG2, spG4a/b, stG4 | wie oben, Saaten 2 und 4 | je ~4,5 bis 5 min |
| cpu5 (nach beiden) | zuG1..4, bild | zusammen (Glas-Teile); bild (alle 7 Spannen) | < 1 min |

- Laufketten code/kette-cpu5.sh, code/kette-cpu6.sh, code/kette-ende.sh. Arbeitsordner
  /home/fmh/fmhc-physics-remote/lund-regge-masse-1/ (code/, lauf/, rauch/). Logs mit absolutem Pfad.
- Reihenfolge nach Karte: LR0 und V zuerst, dann S, A15, Glas; der Gang (LR2) laeuft frueh, weil er nur ~1 min braucht.

## 9. Rauchtests vor dem Einfrieren

- r1 bis r4 (cpu5, 08:29:47 bis 08:38:38 UTC, rc = 0, 20 bis 75 s): Modus rauch, Ausgabe nur Schluessel und
  Laufzeiten; Codeprobe "Zusammenfuehrung der Teillaeufe gleich Gesamtlauf" (V) = wahr. Gelesen: Laufzeiten
  (Glas-Punkt 7,3 s voll, 6,5 s Stabilitaet), Schluessel, Rueckgabewerte. Zwischen r1 und r4 geaendert: hermitesche
  omega^2 (Sylvester) statt allgemeiner Eigenwerte, A S statt voller Inverse, K [Q C] einmal, Teillaeufe und
  Zusammenfuehrung, Glas-Gitter 4^3.

## 10. Festlegungen und Grenzen [F]

- Spanne aus |k| = kl/l mit l = mittlere Kantenlaenge; TT-ISO-1 und HODGE-MASSE-1 messen bei |k| = 1e-3 (kubisch), das
  Glas bei 1e-2. Vergleich mit dortigen Zahlen nur ueber den kleinsten kl-Wert bzw. die Extrapolation.
- Glas-Stabilitaet nur 4^3 (36 Klassen), nicht 6^3.
- Keine Abstimmung, keine Gewichte: die Masse ist parameterfrei (bis auf einen globalen Faktor).
- Synthetisch, keine Messdatenbestaetigung.
