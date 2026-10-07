# UEBERLEITUNG-V-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 49)

- Karte KARTE.md gelesen; UV0 bis UV4, Wahrscheinlichkeiten und Bedeutung bleiben unveraendert und bindend. Die vorab
  festgelegte Behandlung statischer Richtungen (Schur-Komplement, keine stille Pseudo-Inverse) ist bindend.
- Start des Agenten 2026-10-05 14:08:24 CEST (date). Plantext ab 14:22:46 CEST (date), vor jedem Rauchtest und vor jeder
  Rechnung dieser Karte. Zeitbox 150 min ab Start.
- Gelesen (nur lesend): ueberleitung-kh-1/ (KARTE, PLAN.md.eingefroren-20261005-135022, ERGEBNIS, code/ukh.py,
  nachtrag_ukh.py, nachtrag_konv.py, nachtrag_aw.py); regime-k-2/ (KARTE, PLAN.md.eingefroren-20261005-130842, ERGEBNIS,
  code/rk2.py, code/rk.py); hodge-masse-1/code/hm.py, tg.py, dn.py (netz_ew); lund-regge-masse-1/PLAN.md.eingefroren
  (Abschnitte 1 bis 7) und code/lrm.py (k-Gitter, Schwelle wachsend); tt-iso-1/code/tp.py (AV), tti.py (richtungen13).
  ERGEBNIS-Dateien von HODGE-MASSE-1, LUND-REGGE-MASSE-1 und TT-ISO-1 nur ueber die Zitate in den obigen Dateien.
- Kennzeichen: [M] Mathematik (Schreibtisch), [P] Projektbefund, [F] Festlegung dieses Plans, [H] Hypothese, [E] wird
  gerechnet. Synthetisch, linearisiert um flach; keine Messdaten, keine Messdatenbestaetigung.

## 1. Gitter [F]

- **V mal Zeit:** wie REGIME-K-2, Arm V-A: Raumnetz V = ew.geometrie('V') ueber rk2.netz_raum (10 Untergitter, 68 Kanten,
  58 Tetraeder je fcc-Zelle, Gittervektoren tp.AV), Zeltstangen-Treppe rk.Gitter mit Hubfolge A (Untergitter 0 bis 9,
  Hoehen j/10, Ordnung rk2.ord_rang). Einziger Unterschied zu REGIME-K-2: Zeltstangenhoehe tau = h statt 1. Je Zelle 146
  Kanten: 68 raeumliche, 10 Zeltstangen (b, b, (0,0,0,1)), 68 Diagonalen (b1, b2, (d, dt)) mit dt = +-1 (bei V-A dt = -1).
  Die Geometrie bei tau = h ist das Bild der bei tau = 1 unter diag(1, 1, 1, h) [M], wie beim Kuhn-Gitter in UEBERLEITUNG-KH-1.
- **Kuhn (Kontrolle UV0):** rk.baue('KW', tau = h) wie UEBERLEITUNG-KH-1.
- h-Folge H7 = 1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64.

## 2. Variablen und Abbildung J [F, M]

- a-Variablen a = dl/l wie im Projektcode. Euklidische ADM-Form: Fuer eine zeitartige Kante mit 4D-Vektor (dx, dT) gilt
  linear d(s) = 2 dT^2 n + 2 dT dx . beta + dx^T dg dx (n = Lapse-, beta = Shift-Stoerung).
- **Raeumliche Kanten (Schichtkanten):** Bei gestaffelten Hoehen (V-A: j/10) sind sie um dT = h (hb_b2 - hb_b1) geneigt.
  Fassung B (Haupt, **Aenderung ab 14:35:13 CEST (date), nach Abbruch von Rauchtest r1-v an einer Zusicherung, die die Neigung
  zeigte; keine Werte gesehen**): ADM-Zerlegung wie an den Diagonalen, d(s) = 2 dT^2 n + 2 dT dx . beta + 2 |dx|^2 q_e,
  also q_e = raeumlicher Metrikanteil. Fassung A (urspruenglicher Plantext, q_e = a_e; Schema "lsa", beschreibend, nur
  Raster): Beide haben denselben Grenzwert h -> 0 (Unterschied O(h) n, O(h) beta [M]), nur die h-Abhaengigkeit (UV1) kann
  sich unterscheiden. Auf Kuhn sind die Schichtkanten nicht geneigt, beide Fassungen gleich.
- **Zeltstangen:** n_b = a der Zeltstange an Untergitter b (10 bei V); das ist die Lapse-Stoerung.
- **Diagonalen** (Partner = raeumliche Kante mit denselben (b1, b2, d)): raeumlicher Anteil zeitsymmetrisch wie
  UEBERLEITUNG-KH-1: 2 s a = sigma + (1/2)(1 + z^dt) 2 |dx|^2 q_e, z = exp(i w h), s = Quadrat der 4D-Laenge. Rest
  sigma = Lapse-Anteil + Shift-Anteil + Gitterrest.
- **Lapse und Shift an Diagonalen und geneigten Schichtkanten:** an jeder Ecke die Zeltstange, die von der Ecke zur Zeit
  der anderen Ecke hin reicht (dT > 0: Startecke Schicht 0, Endecke Schicht dt - 1; sonst Startecke -1, Endecke dt),
  mit Bloch-Faktor z^Schicht und raeumlicher Phase der Endecke; bei V-A-Diagonalen beide Schicht -1), mit Gewichten (w1, w2) fuer
  Start- und Endecke: Lapse 2 dT^2 (w1 n_b1 + w2 n_b2), Shift 2 dT dx . (w1 beta_b1 + w2 beta_b2).
- **Gitterreste L:** Unterraum des sigma-Raums der lebenden Diagonalen (tote Kanten = Nullzeilen der lokalen Hesse,
  rk2.tote_idx, werden ausgenommen), komplementaer zum Bild der Shift-Abbildung B_s (bei z = 1). Parametrisiert durch eine
  Orthonormalbasis; das Schur-Komplement haengt nur vom Unterraum ab [M].
- **Zwei Schemata:**
  - "achse" (nur Kuhn, = UEBERLEITUNG-KH-1 woertlich): (w1, w2) = (1, 0) (Basispunkt), L = Spann der lebenden
    Nicht-Achsen-Diagonalen (110, 101, 011); Shift aus den drei Achsen-Diagonalen.
  - "ls" (Hauptschema fuer V; auf Kuhn beschreibend): (w1, w2) = (1/2, 1/2) (Mittelpunkt, zeitlich ausgerichtete
    Zeltstangen), L = orthogonales Komplement von Bild B_s in der Metrik der Groessen sigma_e / (2 |dx_e|^2) (h-unabhaengig,
    gleich a im Grenzfall). Das ist der Kleinste-Quadrate-Shift (Shift = bestangepasstes Vektorfeld an den Ecken).
  - "ls2" (V, beschreibend, nur Raster): wie "ls", aber L orthogonal in der Metrik von sigma selbst (andere Gewichte
    der Diagonalen, also ein anderer Unterraum L). Vor dem ersten Rauchtest statt eines Schemas "start" (w1, w2) = (1, 0)
    gewaehlt: Bei V-A ist das Untergitter 9 nie Startecke einer Diagonale, B_s haette dann Rang 27 statt 30 [M].
- Begruendung [M]: M_eff (omega^2-Block bei festem n, beta) haengt nur vom Unterraum L ab; die Zahl der Nullrichtungen von
  M_eff modulo Eichung ist unter ADM-Form schemaunabhaengig (Kern der horizontalen Masse M_perp = Kern M_eff + Bild M_disp).
  Diese Unabhaengigkeit wird mit M_perp (Abschnitt 4) und den Schemata "ls2" (V) bzw. "ls" (Kuhn) beschreibend geprueft.
- Bedingung je k: Rang B_s = 3 NV (V: 30), J(z = 1) regulaer auf den lebenden Kanten; sonst ist das Schema an diesem k
  nicht definiert (Meldung, kein Ersatz).

## 3. Bloecke, Grenzfall, UV1 [F]

- H_a(k_s, w) = Summe_m C_m z^m in a-Variablen (rk2.Laurent, unveraendert; C_m in Kantenlaengen, dann diag(l) C diag(l)),
  J(w) = Summe_m J^(m) z^m. P(w) = -(1/h) J(w)^+ H_a(w) J(w), Taylor-Koeffizienten P_p exakt (p = 0, 1, 2; Abschnitt 9:
  p bis 4 an wenigen k). Schur ueber L als Reihe (D_0 = P_0[L, L] muss regulaer sein). Ergebnis S_p(h) auf
  (q, n, beta): V 68 + 10 + 30.
- Benennung: M_eff = S_2[q,q], V_eff = S_0[q,q], C = S_0[q,n] (Lapse-Kopplung), X = S_1[q,beta] (Shift-Kopplung),
  D_bb = S_0[beta,beta], Kreisel G = S_1[q,q].
- **UV1-Kennzahl:** je Block Q in {M_eff, V_eff, C, X} und je k: d(Q, k) = max_h in H7 ||Q(h) - Q(1)||_F / ||Q(1)||_F.
  Dazu beschreibend die uebrigen Bloecke (n-n, n-beta, beta-beta, Kreisel, S_1[q,n], S_2[q,n], S_2[q,beta]) als Normen
  je h.
- **Grenzwert (fuer alle weiteren Schritte):** Q0 = kubische Interpolation durch h = 1, 1/2, 1/4, 1/8, ausgewertet bei
  h = 0 (Endfassung von UEBERLEITUNG-KH-1). Q0' = quadratisch durch 1/2, 1/4, 1/8; Q0'' = kubisch durch 1/8, 1/16, 1/32,
  1/64. Fehlerschaetzung e(Q) = max(||Q0 - Q0'||, ||Q0 - Q0''||) / ||Q0||. Diese Fitwahl wird nach dem Rauchtest nicht
  geaendert.

## 4. M_eff, statische Richtungen, UV2 [F]

- Je k (Grenzwert Q0, tg-Konvention, Abschnitt 6): Eigenwerte von M_eff (hermitesch symmetrisiert). Null, wenn
  |lambda| <= tol_null max|lambda|, tol_null = max(1e-10, 100 e(M_eff)). n_u = Zahl der Nullrichtungen.
- Lage: Anteil der Nullrichtungen in Bild M_disp (Eich-Ueberlapp n_ug, Abstand <= 1e-8), Kopplungen
  ||u^+ C|| / ||C||, ||u^+ c|| / ||c||, ||u^+ X|| / ||X||, ||u^+ G|| / max(||G||, 1e-300), u^+ B u (Kondition).
- **Schemafreie Kontrolle M_perp:** weiterer Schur ueber beta (Reihe) ergibt S'_p auf (q, n); M_perp = S'_2[q,q].
  n_u_perp = (Zahl der Nullwerte von M_perp, gleiche Toleranz) - Rang M_disp. Beschreibend, geht in kein Urteil ein.
- Dazu je k: Zahl negativer Eigenwerte von M_eff, kleinster Nicht-Null-Betrag relativ.

## 5. Regime H mit M_eff, R1 und statischen Richtungen [F, bindend nach Karte]

Je k, mit Q0 (Urteil) und Q0' (Robustheit), im 3D-Netz V (tg.modell ueber hm.netz('V'), B Regge, M = M_disp, c = Code-Regel):

1. Statische Richtungen u = Kern von M_eff ohne Eichanteil (Abschnitt 4); W = orthonormales Komplement (Eigenvektoren zu
   Nicht-Null-Werten).
2. **Bindende Behandlung:** Gleichung der statischen Richtungen = ihre Zeile des Potentials B:
   u^+ B (W p + u s) = 0, also s = -(u^+ B u)^-1 u^+ B W p. Eingesetzt (Schur-Komplement im Potential):
   B_p = W^+ B W - W^+ B u (u^+ B u)^-1 u^+ B W, c_p = W^+ c - W^+ B u (u^+ B u)^-1 u^+ c (ebenso C_p), M_dp = W^+ M_disp,
   M_p = W^+ M_eff W (regulaer nach Konstruktion), A_p = M_p^-1.
   - u^+ B u muss regulaer sein (Kondition <= 1e10); n_ug muss 0 sein. Sonst: Reduktion an diesem k **nicht definiert**,
     Meldung, keine Pseudo-Inverse.
   - Ist n_u = 0, entfaellt Schritt 2 (W = Einheit).
3. **R1** (wie hm.zerlege): S = orthonormales Komplement von Bild[M_dp, c_p]; A_red = S^+ A_p S, B_red = S^+ B_p S.
4. Spektrum: ist B_red positiv definit (Cholesky L), omega^2 = Eigenwerte von L^+ A_red L (hermitesch) und die TT-Zweige
   ueber hm.z_auswerten (zwei groesste 1/omega^2, ok = beide positiv und Luecke < 1e-2; bei dim_red = 2 Luecke = 0).
   Sonst allgemeine Eigenwerte von A_red B_red.
5. **Wachsend** (Schwelle wie LUND-REGGE-MASSE-1 und UEBERLEITUNG-KH-1): s = max|omega^2|; wachsend, wenn
   Re omega^2 < -1e-9 s oder |Im omega^2| > 1e-9 s.
- Paarungen: **(a) Hauptpaarung** = Schritte 1 bis 5 mit Code-c (woertlich "R1"). (a_C) beschreibend: dasselbe mit C_p
  statt c_p. (a_V) beschreibend: Potential V_eff statt B. (a_s) beschreibend: Schema "ls2" (nur Raster).
- Beschreibend je k: dim_red, Passbedingung ohne Inverse (c_p in Bild(M_p M_dp), Rest relativ), sin(C, c) (Unterraumwinkel
  der Spalten) und kleinste-Quadrate-Faktor C = c kappa, ||V_eff - B|| / ||B||, TT-Anteil der zwei Moden (tg.tensor_fit,
  tp.tt_anteil) an [100], [110], [111] bei kl = 0,01.
- Der Kreiselterm G = S_1[q,q] kommt in Regime H nicht vor; seine Groesse wird nur berichtet (Abschnitt 9).

## 6. Konvention, k-Raster, BZ-Rand [F]

- 4D-Groessen in die tg-Konvention: q_tg = U^+ q_rk, U[i_rk, e_tg] = 1 bei gleicher Orientierung, exp(i k . R_d) bei
  umgekehrter (tg-Start = rk-Ende in Zelle d) [M]; F_tg = U^+ F_rk U, C_tg = U^+ C_rk, X_tg = U^+ X_rk. Kontrolle:
  U^+ M_disp(rk) = M (tg) auf <= 1e-12.
- **Raster V** (wie HODGE-MASSE-1 und LUND-REGGE-MASSE-1): 13 Richtungen tti.richtungen13 x kl = 0,005; 0,01; 0,02; 0,05;
  0,1; 0,2 mit l = mittlere Kantenlaenge von V (tg), dazu abs(k) = 1e-3 und 2e-3 (HODGE-MASSE-1); 104 k.
- **BZ V** wie LUND-REGGE-MASSE-1: k = (m/8) BVc, BVc = 2 pi inv(AV)^T, m in {0..7}^3 ohne 0 (511 k).
  **BZ-Rand ("Komponenten pi")** = die Punkte mit einer reduzierten Komponente k . a_j = pi (m_j = 4): 169 k; darunter X,
  L, W des fcc-Gitters. Zusaetzlich ausdruecklich K = 2 pi (3/4, 3/4, 0) und U = 2 pi (1, 1/4, 1/4) (Rand, nicht im
  Gitter). Gamma nicht (wie LUND-REGGE-MASSE-1). Auf Kuhn ist m_j = 4 genau k_i = pi.
- **Kuhn:** dieselben 13 Richtungen und kl mit l = 1,28210 (mittlere Kantenlaenge des 3D-Kuhn-Netzes), abs(k) = 1e-3,
  2e-3; BZ k = 2 pi m / 8 (511 k).

## 7. Spanne [F]

- Je Richtung und TT-Zweig (aufsteigend) w(kl) = w0 + w2 kl^2 + w4 kl^4, kleinste Quadrate ueber kl = 0,005 bis 0,1;
  Spanne0 = max w0 / min w0 - 1 ueber 13 x 2; nur wenn alle Fitpunkte ok (Reduktion definiert, zwei positive masselose
  Moden mit Luecke). Beschreibend Spanne je kl und auf den HODGE-MASSE-1-Punkten.

## 8. UV0 auf Kuhn [F]

- Schema "achse", sonst identischer Code. r(k) = ||M_eff - K_LR|| / ||K_LR|| (tg, Frobenius; K_LR = V_ref K_A2L wie
  UEBERLEITUNG-KH-1) an allen 615 Kuhn-k.
- Statische Raumdiagonale: n_u = 1 und Anteil der Kante 111 an u >= 0,999; zwei Moden: dim_red = 2; beides an den k, an
  denen UEBERLEITUNG-KH-1 reduzieren konnte (78 kl-Rasterpunkte und die 342 BZ-k ohne Komponente pi).
- Spanne0 der Hauptpaarung (a) auf Kuhn.

## 9. Regeln und hoehere Ordnungen (beschreibend) [F]

- Wie UEBERLEITUNG-KH-1 PLAN 3.2: (R-L) Lapse reiner Multiplikator (Bloecke n-n, n-beta, w^1/w^2 q-n), (R-K) Kreisel
  ||G|| |k| relativ, (R-S) X in Bild(M_eff M_disp) und D_bb = Y^+ M_disp^+ M_eff M_disp Y, Skala sig_k = max_p ||S_p|| |k|^p.
- Lauf "hoeher": p bis 4 an 4 V-k ([100] kl = 0,05 und 0,2; [321] kl = 0,1; ein BZ-Punkt) je h: Normen aller Bloecke
  S_3, S_4 (gehen sie mit h gegen 0?).

## 10. Mechanische Auswerteregeln UV0 bis UV4 [F]

- **UV0:** eingetroffen, wenn (i) alle 615 r in [0,745; 0,775) (Kartenzahlen 0,75 bis 0,77 als auf zwei Stellen gerundete
  Werte gelesen; UEBERLEITUNG-KH-1 selbst: 0,7489 bis 0,7660), (ii) an allen 420 Reduktions-k (78 + 342) n_u = 1,
  Anteil 111 >= 0,999, dim_red = 2, keine Reduktion undefiniert, (iii) Spanne0 (a) < 1e-8 mit allen Fitpunkten ok. Sonst
  nicht eingetroffen. Beschreibend die woertliche Lesart r in [0,75; 0,77].
- **UV1:** eingetroffen, wenn max ueber die vier Bloecke und alle V-k (Raster + BZ + K, U) von d(Q, k) <= 1e-10; sonst
  nicht eingetroffen. Nicht entscheidbar, wenn das Schema "ls" an einem k nicht definiert ist (dort fehlt d).
- **UV2:** eingetroffen, wenn an allen V-k (Raster + BZ + K, U) n_u >= 1 (mit Q0); nicht eingetroffen, wenn an einem k
  n_u = 0 und kleinster/groesster Betrag >= 100 tol_null; sonst nicht entscheidbar.
- **UV3:** Spanne0 der Hauptpaarung (a) mit Q0 und mit Q0'; delta = |Spanne0(Q0) - Spanne0(Q0')|. Eingetroffen, wenn alle
  Fitpunkte ok und Spanne0 + delta < 1e-6; nicht eingetroffen, wenn alle Fitpunkte ok und Spanne0 - delta >= 1e-6; sonst
  nicht entscheidbar.
- **UV4:** eingetroffen, wenn (a) an allen V-k (Raster 104, BZ 511, K, U) definiert ist und weder mit Q0 noch mit Q0'
  eine wachsende Mode hat; nicht eingetroffen, wenn an einem k (a) mit Q0 und mit Q0' wachsend ist; sonst nicht
  entscheidbar. Getrennt berichtet: BZ-Rand (169 + K, U), uebrige BZ, Raster.
- **Kartenwortlaut:** UV1 bis UV4 wie Plan (UV4 "an allen gerechneten k einschliesslich BZ-Rand" = alle 617 V-k). UV0
  nach Wortlaut zusaetzlich mit der woertlichen Lesart r in [0,75; 0,77]; weichen beide ab, steht dort "unklar".

## 11. Kontrollen [F]

- K1 Laurent-Form gegen rk.Gitter.H bei reellem k (V und Kuhn, h = 1 und 1/64), <= 1e-12 relativ.
- K2 4D-Eichnullvektoren bei komplexem k_t (rk.Gitter.G bzw. rk2.G_batch): ||H G|| / (||H|| ||G||) <= 1e-12.
- K3 rk.Gitter.kontrollen je h fuer V und Kuhn (Fehlwinkel, Schlaefli, Volumen, tote Kanten).
- K4 Zuordnung rk/tg: U^+ M_disp(rk) = M(tg) <= 1e-12; V_eff gegen B (beschreibend).
- K5 L-Block D_0 regulaer (kleinster/groesster Betrag >= 1e-10), Rang B_s = 3 NV, J(z = 1) regulaer, an allen k und h.
- K6 M_eff hermitesch (relativ <= 1e-10).

## 12. Ausweichstellen (Meldepflicht)

- Keine Pseudo-Inverse. Nicht definierte Stellen (B_s Rangverlust, D_0 singulaer, u^+ B u singulaer, statische Richtung
  mit Eichanteil, M_p singulaer) werden je k gezaehlt und gemeldet und zaehlen in UV2 bis UV4 nach Abschnitt 10.
- Der allgemeine Eigenwertweg bei nicht positiv definitem B_red ist kein Ausweichen, sondern Teil der Regel 5.4; er wird
  gezaehlt.

## 13. Agenten-Vorhersagen (vor jeder Rechnung; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | UV0 eingetroffen | 80 % |
| A2 | UV1 eingetroffen (Rundung bei h = 1/64 bleibt unter 1e-10) | 50 % |
| A3 | UV2 eingetroffen (V hat keine Thales-Kante wie die Wuerfeldiagonale, aber Kombinationen sind moeglich) | 40 % |
| A4 | UV3 eingetroffen | 50 % |
| A5 | UV4 eingetroffen | 30 % |
| A6 | n_u_perp = n_u an allen V-k (Schemaunabhaengigkeit) | 70 % |

## 14. Laeufe [F]

- Nur auf der .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu2, cpu3, cpu4, je <= 600 s,
  Arbeitsordner /home/fmh/fmhc-physics-remote/ueberleitung-v-1/ (code/, rauch/, lauf/), Logs mit absolutem Pfad.
- Code: code/uv.py (neu). Unveraendert kopiert: rk.py, pt.py, rk2.py, ew.py, tp.py (regime-k-2/code, eingefroren);
  tg.py, hm.py, tti.py, dn.py, nachtrag_kinetik.py (hodge-masse-1/code).
- Hauptlaeufe: kw (Kuhn: Raster + BZ, Schemata achse und ls) und v-raster (V Raster, Schemata ls und ls2) auf cpu2;
  v-bz0 (BZ m-Index 0 bis 255) auf cpu3; v-bz1 (256 bis 510, dazu K, U) auf cpu4; hoeher (cpu2); auswertung (cpu2).
- Rauchtests (je <= 120 s, nach diesem Plantext): r1 technisch (K1 bis K5, Laufzeit je k, Schluessel; keine
  h-Differenzen, keine Spektren, keine Nullzaehlung); r2 Codeprobe der Kette an 2 bis 4 k mit Auswertung (nur rc, Laufzeit,
  Schluessel; Werte nicht ansehen).
- Einfrieren: PLAN.md und code/*.py per sha256 (EINGEFROREN-SHA256.txt, Kopien *.eingefroren-<datum>) vor dem ersten
  Hauptlauf; auf der .69 dieselben Summen.

## 15. Rauchtests und Aenderungen vor dem Einfrieren (Nachtrag ab 14:37:47 CEST, date)

- Alle ueber kleintest.sh, .69-Zeiten UTC (CEST = UTC + 2).
- **r1** (12:32:46 UTC, cpu2 KW, cpu3 V): KW rc 0 (0,5 s). V brach an einer Zusicherung ab: |dx|^2 der Diagonale ungleich
  l^2 der Partner-Schichtkante, weil die Schichtkanten bei gestaffelten Hoehen geneigt sind. Folge: Fassung B (Abschnitt 2,
  q = raeumlicher Metrikanteil) als Haupt, Fassung A als Schema "lsa" (beschreibend). Gesehen nur der Traceback.
- **r1b** (12:35:21 UTC) und **r1c** (12:36:28 UTC, nach Fix): rc 0, V 14 s. Gelesen nur Technik: K1 <= 5,6e-16 (KW) bzw.
  3,8e-16 (V); K2 <= 2,3e-15 bzw. 8,6e-17; Fehlwinkel <= 3,6e-15 (KW) bzw. 1,7e-14 (V, alle h); tote Kante KW nur die
  Hyperdiagonale, V keine; V: NE 146, 68 Diagonalen mit dt = -1; D_0 kleinster/groesster Betrag 2e-4 bis 3e-3 (ls, lsa),
  2e-5 bis 1e-4 (ls2), KW 0,62 bis 1; Rang B_s = 30 (V) bzw. 3 (KW) an 6 Proben-k; J regulaer (kleinster rel. Singulaerwert
  >= 3e-4); Laufzeit ~0,54 s je k, Schema und 7 h. K4 war in r1b 0,57 (V): Fehler in der Kontrollfunktion M_disp_rk
  (4D-Laenge statt raeumlicher Laenge der geneigten Kante), behoben; r1c: K4 1,5e-16. Die Reduktion nutzt M aus tg.ops
  und war nicht betroffen.
- **r2** Codeprobe (12:36:28 bis 12:36:55 UTC, cpu2, code/probe.sh): kw, vraster, vbz Teil 0 und 1 mit --probe (2 bis 3
  k), hoeher, auswertung: alle rc 0. Gelesen nur rc, Laufzeiten und Schluessel der Auswertung; keine Werte.
- **Aenderungen vor dem Einfrieren** (ohne Kenntnis von Werten zu UV0 bis UV4):
  1. Fassung B der Schichtkanten (Abschnitt 2); Schema "lsa" = Fassung A (beschreibend, Raster).
  2. Schema "ls2" statt "start" (Abschnitt 2, Rangverlust [M]).
  3. Fix der Kontrollfunktion M_disp_rk (K4).
  4. Spannenfunktion robust gegen fehlende Punkte (nur fuer die Codeprobe noetig).
  5. Zusatzregel (strenger): Ist an einem V-k tol_null > 1e-6 (Extrapolationsfehler von M_eff > 1e-8), koennen UV2, UV3
     und UV4 nicht "eingetroffen" sein (dann nicht entscheidbar), "nicht eingetroffen" bleibt moeglich.
  6. TT-Zweige (Abschnitt 5.4): gleichwertig zu hm.z_auswerten direkt aus den omega^2 (zwei betragskleinste; Luecke
     |omega^2_2| / |omega^2_3|; ok = beide positiv und Luecke < 1e-2), ohne A_red zu invertieren. Eine zwischenzeitliche
     Zusatzbedingung "ok nur ohne wachsende Mode" wurde vor dem Einfrieren wieder gestrichen, damit UV3 nicht an UV4 haengt
     (wie UEBERLEITUNG-KH-1 und HODGE-MASSE-1).
