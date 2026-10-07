# V1-AUFHEBUNG-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Start 2026-10-05 10:25:35 CEST (date). Plantext ab 10:41:29 CEST (date), vor jeder Hauptrechnung. Zeitbox 120 min,
  also bis 12:25:35 CEST; danach kein neuer Lauf.
- Grundlage: KARTE.md (VA0 bis VA3; Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Code kopiert 10:35:28 CEST nach code/ (ew, tp, pn, mn, inz, nachtrag_iso, tg, dz, gs, nachtrag_umkreis,
  nachtrag_v_j1, nachtrag_v_kl, nachtrag_ikosaeder, dk aus glas-strahlung-1/code; nachtrag_quelle aus impuls-netz-1/code;
  smi, nachtrag_vorzeichen, tti aus skalar-misch-1/code; gemeinsame Dateien in allen drei Ordnern sha256-gleich).
  Originale unveraendert.
- Werkzeug: **code/va.py (neu)**. Unveraendert importiert: ew.py (fa7b6417...; Netz V, Operatoren B, A, M, c),
  pn.py (c8034e40...; J_ISO, A_J, tet_ableitungen, eckvolumen, richtungen, Konstanten), mn.py (b36984d3...; W_of), tp.py.
  code/referenz.json: jq-Auszug (nur gelesen, nichts gerechnet) der Vergleichswerte aus GLAS-STRAHLUNG-1 (V, J_iso und
  J = 1, je Lage; NVKL) und SKALAR-MISCH-1 (Kurve dTT = 0: 18 Punkte mit x = log10(Kegel, Sechseck) und TT_0; exakter
  Punkt; J_iso).
- Kennzeichen: [M] eigene Mathematik (vorab), [E] gerechnet, [P] Projektdatei, [L] Lehrbuch/Gedaechtnis ohne Abruf,
  [ES] eigener Schluss, [H] Hypothese, [F] Festlegung. Alles synthetische Gitterrechnung, keine Messdaten.

## 1. Rechenweg (unabhaengig von gs.py) [F]

- Netz V aus ew.baue('V') (E = 68 Kanten, nV = 10 Ecken, 58 Tetraeder, V = 0,25), Operatoren aus ew.ops (nicht ueber
  tg.netz_V/tg.ops/dz wie gs.py). Reduktion R1 mit numpy: S = Komplement von Bild [M, c] (SVD, Rang 40 geprueft),
  A_red = S^H A S = L L^H, Moden X = L U aus den zwei weichsten Eigenwerten von L^H B_red L.
- Bewegungsgewichte je Tetraeder-Art ueber pn.A_J (Arten finn_auf, finn_ab, kegel_T1, kegel_T2, sechs_T1, sechs_T2).
- Spannungsquelle mit eigener Q-Abbildung: Q_e = Summe_{Tetraeder, p -> e} 0,5 l_p X^T dK_p X (P1, pn.tet_ableitungen),
  sigma_e(T) = Q_e : (T - tr T 1) e^(i k.m_e) fuer 6 Basistensoren; Kontrolle KP1: Summe sigma_e n_e n_e^T = -V T.
- Impuls: fJ = -A_red^-1 S^H A P_M sigma (J' = -M^H sigma, IMPULS-NETZ-1 [P]).
- **Volle Kugel** (10 x 20 Gauss-Legendre-Richtungen, 200 Stueck), ohne den k -> -k-Trick von gs.py; die
  Spiegelsymmetrie wird damit mitgeprueft (VA0).
- Gemeinsam mit gs.py bleiben nur die Modell-Definitionen (Netz, Gewichte, P1-Form, Takt W) und die Definition der
  24 Lagen; Reduktion, Quelle, V1, Kraefte und Auswertung sind neu geschrieben.

## 2. V1-Quelle: Formel, Vorzeichen, Normierung (selbst nachvollzogen)

- **Kontinuum [M, L]:** Erhaltung mit c0 als Umrechnung Energie/Masse: d_t eps + c0^2 d_i pi_i = 0, d_t pi_i + d_j T_ij = 0.
  Fuer T_ij = S_ij e^(i(k.x - omega t)) folgt pi = (k.S)/omega und **eps = c0^2 (k.S.k)/omega^2 = c0^2 k^2 (n.S.n)/omega^2**.
  Auf der Massenschale der Mode j (omega = c_j k): **eps_j = (c0/c_j)^2 (n.S.n)**. Vorzeichen positiv (gleiches
  Vorzeichen wie n.S.n); die Rechnung ist linear, die Zeitkonvention e^(-i omega t) gegen cos aendert nichts.
- **Je Superzelle (Zelle, V = 0,25):** integrierte Spannung V S (KP1), integrierte Energie V eps_j, baryzentrisch auf die
  Ecken verteilt: m_v = V eps_j (V_v/V) e^(i k.x_v). V1-Einheitsquelle m_u = (V_v/V) e^(i k.x_v) (Summe 1 bei k = 0).
- **Kopplung auf dem Netz [P, nachvollzogen]:** skalare Regel kappa' c^H a = m (kappa' = kappa_g/2, PUMPE-NETZ-1).
  R1: a = S x + a_c, a_c = c (c^H c)^-1 m/kappa'. Die Potentialenergie (kappa_g/2) a^H B a gibt auf x die Kraft
  -kappa_g S^H B a_c, also **f_V1 = -(kappa_g/kappa') S^H B c (c^H c)^-1 m**.
- **Amplitude je Mode und Richtung:**
  **A_j(n; S) = X_j^H (f_S + f_J)(S) + (c0/c_j)^2 V (n.S.n) X_j^H f_V1(m_u)**,
  f_S = -S^H sigma (Kraft der Spannung, -dE_Materie/da), f_J wie oben.
- **Vorzeichen gegen die ART [L, M]:**
  - Spannung: dE_Materie = Summe sigma_e a_e mit Summe sigma n n^T = -V T entspricht H_int = -(1/2) Int h_ij T^ij
    (Probe von Hand: Dehnung in x um eps aendert die Gradientenenergie um -eps V T_xx).
  - Energie: Linearisierte Hamilton-Regel d_i d_j h_ij - Laplace h = 16 pi G rho; fuer rho > 0 ist der konforme Anteil
    positiv (h_ij = 2 Phi delta_ij, Phi_k = 4 pi G rho_k/k^2 > 0). Auf dem Netz ist c = -B W und P = W^H c > 0
    (Takt-Steifigkeit, G_N), also W^H a_c = P (c^H c)^-1 m/kappa'. **Kontrolle KV1:** Re(m_u^H W^H a_c) > 0 an allen k
    (positive Energie verlaengert die Kanten wie in der ART).
  - Impuls: J' = -M^H sigma ist die Gitter-Impulsbilanz (Vorzeichen in IMPULS-NETZ-1 hergeleitet und gegengelesen [P]).
- **Normierung:** kappa' = kappa_g/2 und die G_N-Formel (8 V/nV)/(lambda_min(P)/k^2) sind [P] (PUMPE-NETZ-1,
  MATERIE-NETZ-1); G_N/G wird zweimal gerechnet (Eigenwert, direkte Antwort m^H P^-1 m). c0 als Umrechnung ist eine
  Festlegung [F] (wie GLAS-STRAHLUNG-1 PLAN 1.4). Beschreibend: Skalierung lambda von V1, bei der der Gang null wird
  (lambda = 1 heisst: Normierung passt fuer volle Aufhebung).
- **Leistung [M, wie GLAS-STRAHLUNG-1 PLAN 1.4, nachvollzogen]:** Goldene Regel bei linearer Dispersion. Mit
  Modenmasse kappa_g und X^H A_red^-1 X = 1 gilt |g_j|^2 ~ c_j^2, Zustandsdichte k_j^2/c_j, also
  P/P_E = Summe_n w Summe_j (|A_j|^2/om2_j)(c0/c_j) / Summe_n w V Lambda_n[S]:S^*/k^2 (volle Kugel),
  c0^2 = Raumwinkelmittel von om2/k^2 ueber beide Zweige, **G = (P/P_E)/(G_N/G)**. Normierungsprobe: nur TT-Anteil
  der Quelle muss 1 + O(1e-6) geben (IMPULS-NETZ-1: TT-Kopplung 1 + 1,5e-6 [P]).

## 3. Kreisbahnen, Lagen, Kanaele [F]

- S = (u + i w)(u + i w)^T zur Bahnnormale m (u = m x (0,3; 0,5; 0,7) normiert, w = m x u), gleichfoermig mit
  Bloch-Phase an den Kantenmitten (Grenzfall k -> 0 einer kompakten Bahn), wie GLAS-STRAHLUNG-1/IMPULS-NETZ-1.
- **24 Lagen wie GLAS-STRAHLUNG-1** ([001], [111], [110], (1,2,3); 8 Normalen Saat 31; 12 Normalen Saat 47).
- Kanaele je Richtung: TT = Lambda_n[S], L = P S nn + nn S P, nn-Teil = Rest (fuer spurfreies S gleich
  (n.S.n)(nn - P/2)), V1. Groessen je Lage: TT, TTL, S (= S+J), SV1 (= V1+S+J, Hauptgroesse), ohneJ_S, ohneJ_SV1;
  beschreibend SV1 mit doppeltem V1 (fuer lambda).
- **Lagenabhaengigkeit** := Spanne max - min von G ueber die 24 Lagen (Kartenkopf: "0,999985 bis 1,000003");
  dazu Standardabweichung (ddof 1) und Gang b aus G = a - b Summe m_i^4 (Kleinste Quadrate).
- Diagnose je Richtung: Einheitsquelle N = nn - P/2 (nn-Teil mit n.N.n = 1): Leistungsanteil des Rests
  |A_nn + A_V1|^2 gegen |A_nn|^2 (Raumwinkelmittel) und bestes lambda fuer diese Quelle.

## 4. Gewichtspunkte und kl [F]

| Name | Gewichte (finn_auf, finn_ab, kegel_T1, kegel_T2, sechs_T1, sechs_T2) | Herkunft |
|---|---|---|
| J_iso | 1; 1; 10^-1,0453267 (0,090089); dto.; 10^-0,0010098 (0,997677); dto. | pn.J_ISO (TT-ISO-1) |
| F1_exakt | 1; 1; 0,02140518247407106; dto.; 1,1409989418009825; dto. | SKALAR-MISCH-1 N1, exakter TT-Punkt (TT_0 3,7e-11) |
| J1 | 1; 1; 1; 1; 1; 1 | Kontrolle |
| K-2.0 bis K-0.3 (18 Punkte) | 1; 1; 10^x0; 10^x0; 10^x1; 10^x1, x0 = -2,0 bis -0,3 in 0,1-Schritten, x1 von der Kurve | SKALAR-MISCH-1 suche-F1.json kurve_dTT0 ("E-Masse = T2-Masse") |

- kl (= k l_P): Hauptpunkte J_iso, F1_exakt, J1 bei **0,0025; 0,005; 0,01; 0,02**; Kurve (18 + exakter Punkt) bei
  **0,005; 0,01; 0,02**. Quadraturprobe 12 x 24 an J_iso und F1_exakt bei kl = 0,01.
- TT-Spanne fuer VA3: **TT_0 aus SKALAR-MISCH-1** (langwellig extrapoliert, [P], in referenz.json); beschreibend die
  eigene Tempo-Spanne om2/k^2 (max/min - 1 ueber 200 Richtungen und beide Zweige) je kl.

## 5. Kette pruefen (vor dem Einfrieren): was ist ableitbar?

- **K1 [L]:** In der linearisierten ART koppelt eine erhaltene Quelle nur ueber ihren TT-Anteil an die Strahlung
  (Eichinvarianz, k_mu T^mu nu = 0). Das gilt im Kontinuum.
- **K2 [M, vorab ableitbar]:** Auf V mit kubisch symmetrischen Gewichten (alle Punkte hier) ist G(m) **exakt linear in
  Summe m_i^4**: G ist eine quadratische Form in S(m), S quadratisch in m, also ein gerades Polynom vom Grad 4 in m; unter
  der kubischen Drehgruppe gibt es in Grad 4 nur (Summe m_i^2)^2 = 1 und Summe m_i^4. Damit ist die Lagenabhaengigkeit
  vollstaendig durch den Gang b bestimmt, und **Spanne(24 Lagen) = (2/3) abs(b) exakt** (die Lagen enthalten
  Summe m^4 = 1 und 1/3, den ganzen Bereich). Ein Rest anderer Winkelform ist ausgeschlossen. Probe: Fitrest.
- **K3 [M]:** Fuer spurfreies S tragen nn-Teil und V1 beide den Faktor n.S.n; sie gehen nur ueber die Summe
  C_j(n) = A_nn,j(n) + A_V1,j(n) je Richtung ein. "Aufhebung" heisst abs(C) << abs(A_nn); der Rest-Gang entsteht aus
  der Interferenz von C mit dem TT-Anteil.
- **K4, Netzquelle erhalten? Nur teilweise ableitbar:**
  - Impuls: gittergenau erhalten (J' = -M^H sigma) [P]. Bei E = T2 (dTT = 0) verschwindet damit die Laengs-Kopplung
    (IMPULS-NETZ-1: 2,6e-11 bei J_iso; mit J = 1 kehrt das L-Leck zurueck, GLAS-STRAHLUNG-1 4.7 [P]). Fuer die Punkte
    der Kurve dTT = 0 erwarte ich deshalb ein kleines L-Leck [ES], nicht abgeleitet (Rest Q != 0).
  - Energie: V1 kommt aus der **Kontinuums**-Erhaltung, nicht aus einer Gitter-Bilanz; die skalare Regel ist zweiter
    Klasse (TT-ISO-1, GAMMA-NETZ-L, IMPULS-NETZ-1 4.3 [P]). Es gibt auf dem Netz also keine Eichsymmetrie (Zeit-
    Umparametrisierung), die "Quelle erhalten" in "Nicht-TT-Teile entkoppeln exakt" uebersetzt. **Der Schritt der Karte
    "Mit V1, Spannung und J ist die Quelle auf dem Netz vollstaendig, also strahlt nur TT" ist nicht ableitbar.** Ein
    Rest bei k -> 0 ist moeglich; seine Groesse ist offen.
  - **"Der Rest folgt der TT-Spanne" ist nicht ableitbar, und es gibt ein Gegenargument [P, ES]:** Der nn-Kanal allein
    verschwindet am exakt TT-isotropen Punkt nicht (SKALAR-MISCH-1: Gang 0,003944 gegen 0,004077 bei J_iso, nur -3 %).
    Skizze [H]: Im Kontinuum entsteht das nn-Leck aus der Projektion (1 - P_c) mit der euklidischen Kanten-Metrik; deren
    Viererform Summe_e n_e n_e n_e n_e ist kubisch anisotrop und gibt genau die Winkelform Lambda_n[diag(n_i^2)]
    (kappa in SKALAR-MISCH-1), unabhaengig von der E/T2-Aufspaltung der Bewegungsenergie. Der V1-Kanal laeuft ueber
    c^H B (ebenfalls Kanten-Metrik). Wenn beide Lecks aus derselben Gitter-Anisotropie stammen, haengt ihr Rest vor
    allem von ihr und der Dynamik ab, nicht von der TT-Spanne. Das ist eine Skizze, keine Ableitung.
  - Die Kopplungen sind langwellig konstant (PUMPE-NETZ-1, Exponent ~0 [P]), und der Lagengang bei J_iso ist
    k-konvergiert (NVKL: Spanne 1,80e-5 bis 1,87e-5 fuer kl 0,005 bis 0,02 [P]). Ich erwarte je Gewichtspunkt einen
    k -> 0-Wert plus O((kl)^2) [ES]; Extrapolation b_0 = (4 b(0,005) - b(0,01))/3.
- **K5, Kontrollen mit vorab bekanntem Ausgang:**
  - VA0 rechnet eine Zahl nach, die in GLAS-STRAHLUNG-1 schon steht (Lauf GV). Bei richtigem Code ist der Ausgang
    vorab erwartet; VA0 prueft die Umsetzung, nicht die Physik. Keine Messung.
  - **VA2 ist vorab bekannt [P]:** GLAS-STRAHLUNG-1 Nachtrag NVJ1 (V, J = 1, V1+S+J, kl = 0,01): G = 0,998608 bis
    1,003323, Spanne 4,7e-3 > 1e-3. VA2 ist nur eine Code-Kontrolle mit unabhaengigem Rechenweg. Keine Messung.
- **Nicht ableitbar (gemessen wird):** die Groesse des Rests am exakten Punkt (VA1), sein Gang entlang der Kurve (VA3),
  lambda und der Restanteil der nn-Leistung je Gewichtspunkt.

## 6. Urteilsregeln (mechanisch in va.py aus; Werte bei 10 x 20 Richtungen)

- **VA0** (Kontrolle: V, J_iso, V1+S+J gibt 0,999985 bis 1,000003 auf 2e-6 fuer dieselben Bahnen), kl = 0,01:
  - Kartenwortlaut: abs(min - 0,999985) <= 2e-6 und abs(max - 1,000003) <= 2e-6 ueber die 24 Lagen.
  - Plan: je Lage abs(G_neu - G_GLAS) <= 2e-6 (G_GLAS aus aus-69/auswertung.json, GS0.V_voll, P_P1_SV1_J).
- **VA1** ([ES-Kette] am exakt isotropen Punkt ist mit V1 die Lagenabhaengigkeit unter 1e-6), Punkt F1_exakt:
  - Kartenwortlaut: Spanne(24 Lagen, V1+S+J, kl = 0,01) < 1e-6.
  - Plan: Wortlaut erfuellt **und** k -> 0-Spanne (2/3) abs(b_0) < 1e-6 mit b_0 = (4 b(0,005) - b(0,01))/3.
  - Nicht entscheidbar, wenn die Spanne bei 12 x 24 Richtungen um mehr als 5e-7 von 10 x 20 abweicht.
- **VA2** (Kontrolle: mit J = 1 und V1 bleibt die Lagenabhaengigkeit ueber 1e-3), Punkt J1:
  - Kartenwortlaut: Spanne(kl = 0,01) > 1e-3. Plan: Spanne > 1e-3 bei kl = 0,005, 0,01 und 0,02.
- **VA3** ([H] entlang der Kurve "E-Masse = T2-Masse" waechst der Rest mit V1 ungefaehr proportional zur TT-Spanne,
  Korrelation >= 0,9 auf >= 5 Punkten): 18 Kurvenpunkte + F1_exakt (19 Punkte), Rest = Spanne(V1+S+J, kl = 0,01),
  TT-Spanne = TT_0 [P]:
  - Kartenwortlaut: Pearson-Korrelation r(TT_0, Rest) >= 0,9.
  - Plan: Wortlaut **und** Pearson der Logarithmen >= 0,9 **und** Steigung log Rest gegen log TT_0 zwischen 0,5 und 1,5
    ("ungefaehr proportional"; die lineare Korrelation allein wird von den drei groessten TT-Werten bestimmt).
  - Nicht entscheidbar bei weniger als 5 gueltigen Punkten (Cholesky).
- Bedeutung der Ausgaenge: wie auf der Karte; nichts daran geaendert.

## 7. Kontrollen (beschreibend, in va.py)

- KP1 affin <= 1e-12 absolut; KF = M^H B, KR = c^H M <= 1e-12 relativ; KJ (M^H P_M sigma = M^H sigma) <= 1e-10;
  Rang [M, c] = 40 an allen k; Cholesky aller A_red.
- KV1 Vorzeichen (Abschnitt 2): Re(m_u^H W^H a_c) k^2 > 0 an allen k.
- G_N/G auf 1e-4 bei 1 (zwei Wege); nur-TT-Anteil auf 1e-5 bei 1; Gang-Fitrest <= 1e-9 (K2).
- Luecke om2_3/om2_2 >> 1. Quadratur 12 x 24 gegen 10 x 20.
- Konsistenz: F1_exakt aus Haupt- und Kurvenlauf gleich; VA2-Werte je Lage gegen GLAS NVJ1 (beschreibend).

## 8. Agenten-Erwartungen (vorab; kein Kartenurteil)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| A1 | VA0 nach Plan und Wortlaut eingetroffen | 90 % |
| A2 | VA2 eingetroffen (vorab bekannt, K5) | 95 % |
| A3 | VA1 nach Wortlaut eingetroffen (Rest am exakten Punkt < 1e-6) | 20 % |
| A4 | Rest am exakten Punkt innerhalb Faktor 2 des J_iso-Rests (1,8e-5) | 55 % |
| A5 | VA3 nach Wortlaut eingetroffen | 35 % |
| A6 | VA3 nach Plan eingetroffen | 15 % |
| A7 | lambda (Gang null) bei J_iso innerhalb 2 % bei 1 | 70 % |
| A8 | KV1 positiv an allen k | 90 % |

## 9. Laeufe (.69, kleintest.sh; Arbeitsordner /home/fmh/fmhc-physics-remote/v1-aufhebung-1/)

- Rauchtests (vor dem Einfrieren, 4 x 6 Richtungen, gelesen nur rc, Laufzeiten, Schluessel): r1 (cpu, haupt, 3 kl,
  1,2 s), r2 (cpu7, kurve, kl 0,01, 1,5 s), r3 (cpu, aus auf r1/r2, 2,1 s); alle rc = 0.
- Eingefrorener Code per scp in einen neuen Ordner, dann mv nach code/ (nie in place).
- **Laufliste:**

| Lauf | Spur | Aufruf (code/va.py ...) | Schaetzung |
|---|---|---|---|
| H1 | cpu | netz --punkte haupt --kl 0.0025,0.005,0.01,0.02 --out lauf/haupt.json | 15 s |
| K1 | cpu7 | netz --punkte kurve --kl 0.005,0.01,0.02 --out lauf/kurve.json | 60 s |
| Q1 | cpu | netz --punkte haupt --nur J_iso,F1_exakt --kl 0.01 --nt 12 --nphi 24 --out lauf/quad.json | 10 s |
| AUS | cpu | aus --haupt lauf/haupt.json --kurve lauf/kurve.json --quad lauf/quad.json --ref code/referenz.json --out aus/urteile.json --bild aus/bild-v1-aufhebung.png | 5 s |

- Je Lauf hoechstens 600 s (RuntimeMaxSec). Bricht ein Lauf ab, wird er einmal auf p4000a wiederholt (gekennzeichnet).
- Urteile nur aus AUS (eingefrorener Code). Schlusszeit: kein neuer Lauf nach 12:10 CEST.
