# Runde 9, Karte ROT-1: Wirbel mit gefuelltem Kern und Waende der relativen Phase (2D-Querschnitt, N = 2)

Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3), keine formale Bestaetigung.
Beginn 2026-09-30 07:45:40 CEST (date, erster Befehl). PLAN begonnen 07:57:31 CEST (date), Vorab-Tabelle vor jeder
Rechnung (es gibt noch keinen Code und keine Ausgabe). Finn 07:47: "ja, starte ROT-1 und ROT-2 auch".

Belegstufen im Ergebnis: **[Hand]** Herleitung, **[num]** numerisch einfach, **[num+K]** numerisch mit Kontrolle (zweite
Gitterstufe, zweites Verfahren oder exakte Symmetrieprobe), **[H]** Hypothese, **[L?]** Literatur aus dem Gedaechtnis.

Gelesen vor dem Plan: KANDIDAT.md (0 bis 6), RUNDE-08/gf-bic/ERGEBNIS.md (0, 1), RUNDE-07/ERGEBNISSE-R7-A.md (RING),
RUNDE-07/ring/PLAN.md und ring.py (Numerik, Profiltabelle lauf-69/ausgabe/profile_bericht.txt), RUNDE-09.md,
RUNDE-09/PAPIER-ROT3.md (Arbeitsfeld W1, Stand 07:57; Pseudospin-Form des Kopplungsterms, Wandtypen).

## 1. Gleichungen (selbst nachgeprueft)

- L = sum_a (|d_t psi_a|^2 - |grad psi_a|^2) - U(S) + g Re[(psi_1^* psi_2)^2], J = 1, U = S - S^2 + S^3/2.
- Variation nach psi_1^*: g Re[(psi_1^* psi_2)^2] = (g/2)(psi_1^{*2} psi_2^2 + c.c.), Ableitung g psi_1^* psi_2^2. Also
  d_t^2 psi_a - lap psi_a + U'(S) psi_a - g psi_a^* psi_b^2 = 0, U' = 1 - 2 S + 1,5 S^2 (wie KANDIDAT 2.2) [Hand].
- Energie E = int sum_a (|psi_a,t|^2 + |grad psi_a|^2) + U(S) - g Re[(psi_1^* psi_2)^2]; Ladung
  Q_a = int 2 Im(psi_a conj(psi_a,t)) (Konvention ring.py, Q = 2 omega N fuer e^{-i omega t}); J_z = sum_a int
  -2 Re(conj(psi_a,t) d_theta psi_a).
- g = 0: U(2), Q_1 und Q_2 einzeln erhalten, getrennte Frequenzen omega_1, omega_2 erlaubt.
- g != 0: nur Q = Q_1 + Q_2 erhalten; dQ_1/dt = -2 g int f_1^2 f_2^2 sin 2(chi_2 - chi_1) (KANDIDAT 4.2).
- Symmetrie psi_2 -> i psi_2 kehrt g um (exakt). Mit psi_1 = f e^{i theta}, psi_2 = h ist die Drehung um alpha dasselbe
  wie psi_2 -> e^{i alpha} psi_2 (globale Phase). Also: Lauf bei -g ohne Saat = Lauf bei +g um 90 Grad gedreht. Das
  Gitter ist unter 90 Grad exakt symmetrisch: Probe auf Rundungsniveau (K4).

### 1.1 Ansatz Frage 1 (g = 0)

- psi_1 = f(r) e^{i theta - i omega_1 t}, psi_2 = h(r) e^{-i omega_2 t}. Bei g = 0 haengt nur S = f^2 + h^2 an der
  Dynamik, das Problem ist exakt achsensymmetrisch.
- Stationaer bei festen Q_1, Q_2: Minimum von E_Q = Q_1^2/(4 N_1) + Q_2^2/(4 N_2) + G_1 + G_2 + V (N_a = int f_a^2,
  G_1 = int f'^2 + f^2/r^2, G_2 = int h'^2, V = int U(S)); die Euler-Lagrange-Gleichungen sind die stationaeren
  Gleichungen mit omega_a = Q_a/(2 N_a) [Hand]. J = Q_1 (nur psi_1 windet).
- Loeser: radialer Gradientenfluss, halbimplizit (Laplace implizit, Rest explizit), Zellmittengitter h = 0,04 bis
  R = 48. Kontrollen: Q_2 = 0 gegen die Schiess-Tabelle der RING-Karte (m = 1 bei omega^2 0,625: Q 110,174, E 100,728);
  Q_1 = 0 gegen m = 0; Virial in 2D: V = sum_a omega_a^2 N_a [Hand, Derrick]; dE/dQ_a = omega_a (Differenzen).
- Vergleichsobjekte bei gleichem Q und gleichem J = Q_1:
  - getrennt: einkomponentiger Wirbel mit Q_1 plus gewoehnlicher Ball mit Q_2 (E_v1(Q_1) + E_b(Q_2); unterhalb der
    Existenz des Balls zaehlt E = Q_2 als zerstreute Ladung)
  - bei gleichem Q: einkomponentiger Wirbel (J = Q) und Ball ohne Windung (J = 0)

### 1.2 Ansatz Frage 2 (g != 0) [Hand, Schreibtisch]

- Mit n_x + i n_y = 2 psi_1^* psi_2, n_z = |psi_1|^2 - |psi_2|^2, |n| = S ist Re[(psi_1^* psi_2)^2] = (n_x^2 - n_y^2)/4
  (so auch ROT-3 W1.1). Leichte Achse n_x bei g > 0, n_y bei g < 0.
- Beim Wirbel mit gefuelltem Kern windet Delta = arg psi_2 - arg psi_1 um den Kern einmal (-2 pi). Das Potential
  cos 2 Delta hat zwei Mulden je Umlauf: zwei pi-Waende je Wirbel (ROT-3 W1.2).
- Wandbreite, zwei Grenzwege auf der Pseudospin-Kugel bei festem S (Steifigkeit S/4 fuer den Einheitsvektor):
  - ueber den Aequator (Sine-Gordon-Knick der relativen Phase): n_e/S = tanh(k s), k = sqrt(2 |g| S)
  - ueber den Pol (Ising-artig, die schwaechere Komponente geht fast durch null): n_e/S = tanh(k s), k = sqrt(|g| S);
    das ist die Formel der Leitung 1/sqrt(|g| J S)
  - Spannung pro Laenge: sqrt(2|g|) S^{3/2} (Aequator) bzw. sqrt(|g|) S^{3/2} (Pol). Der Pol-Weg ist billiger.
- Zahlen mit S ~ 1: |g| = 0,2: 1/k = 1,6 (Aequator) bzw. 2,2 (Pol); |g| = 0,5: 1,0 bzw. 1,4.
- Getrennte Frequenzen bei g != 0 heissen ein starr drehendes Muster: omega_1 - omega_2 = Omega (ROT-3 W1.4). Die
  Musterdrehung misst arg P(t), P = int psi_1^* psi_2 e^{i theta} w(r) dA; d arg P/dt = omega_1 - omega_2.
- Vergleich: Pendelfrequenz der relativen Phase nu_0 ~ 0,13 bis 0,22 (GF-BIC 2.4, 3D). Omega << nu_0: Waende koennen
  sich bilden und mitdrehen oder einrasten; Omega >> nu_0: die Anisotropie mittelt sich weg.

### 1.3 Ansatz zwei Wirbel (Frage 2, Kraft)

- Grosser gemischter Ball bei festem Q (Radius ~ 12), psi_1-Wirbel bei A = (-d/2, 0), psi_2-Wirbel bei B = (+d/2, 0).
  Delta windet -2 pi um A und +2 pi um B: die Waende koennen A und B verbinden (Einschluss-Analogon [H]) oder zum Rand
  laufen.
- Statisch: 2D-Gradientenfluss bei festem Gesamt-Q mit gemeinsamer Frequenz, Wirbel durch einen abstossenden Fleck
  (Pinning, Hoehe 2, Radius 0,6) festgehalten; E(d) bei g = 0; 0,2; 0,5 fuer d = 2, 4, 6, 8. Mass fuer Einschluss:
  Steigung von E_g(d) - E_0(d) gegen 2 x Wandspannung. Wandzahl auf einem Kreis um beide Wirbel: 0 = Waende verbinden
  A und B, 4 = Waende laufen zum Rand.

## 2. Numerik 2D (wie ring.py, zweikomponentig)

- Periodische Box [-L, L)^2, L = 38,4, Randschicht Breite 8 (sigma0 = 1, Daempfung von psi_t), Laplace spektral,
  Velocity-Verlet, float64/complex128 auf CUDA. Stufen: grob dx 0,3 / dt 0,05; fein dx 0,2 / dt 0,025.
- g wird in dyng linear ueber t = 0 bis 50 eingeschaltet (Rampe); die Arbeit der Rampe steht in der Energiebilanz.
- Saat wie RING-T (Stoerfaktor l = 1..6, eps = 0,01 bei r_s), in psi_1 mit Phase 2,4 l, in psi_2 mit Phase 1,1 l.
- Messung je 1,0: Q_1, Q_2, E, J (Box), Verlustraten der Randschicht (Bilanz), Fenster um den S^2-Schwerpunkt (Q_a, J,
  A_l(S) fuer l = 1..6, A_2 von S_1 und S_2, Kopplungsenergie, P fuer die Musterdrehung, Abstand der Schwerpunkte von
  S_1 und S_2). Je 5: Klumpen (Teilung), psi_1-Wirbel am Zentrum, Kreise r = 1,5 ... 6,5 fuer Waende (Windung von Delta,
  Flachanteil F90 von n_e, Zahl der Vorzeichenwechsel mit Hysterese, Steilheit r k_eff, S und Minderheitsanteil an der
  Wand). Bilder (S_1, S_2, Delta, n_z/S) zu vier Zeiten je Lauf als PNG auf der .69.
- Flachanteil F90 (Anteil des Kreises mit |n_e| >= 0,9 max): gleichmaessige Windung 0,287; scharfe Waende gegen 1.
  Steilheit r k_eff: gleichmaessig 1; Waende r k.

## 3. Laeufe

| Aufruf | Inhalt | T |
|---|---|---|
| radial | Familien Q = 93,86 / 110,17 / 138,76 / 199,35 (einkomponentig omega^2 0,65 / 0,625 / 0,60 / 0,575) mit q_2 = Q_2/Q = 0; 0,1; 0,25; 0,4; dazu Vergleichsobjekte v1(Q_1), Ball(Q_2), Ball(Q); dE/dQ-Probe | - |
| dyn0 | g = 0, Saat 0,01: Q = 110,17 mit q_2 = 0 (Kontrolle gegen RING-T), 0,1; 0,25; 0,4; Q = 93,86 mit q_2 = 0; 0,25; Q = 138,76 mit q_2 = 0; 0,25; einkomponentiger Wirbel mit Q_1 = 0,75 x 110,17 (gleiches J) | 1500 |
| dyn0 fein | L3: Q = 110,17 mit q_2 = 0 und 0,25 | 600 |
| dyng | Q = 199,35, q_2 = 0,25: g = 0; +0,2; -0,2; +0,5; -0,5 mit Saat; +0,5 und -0,5 ohne Saat (K4); Q = 110,17, q_2 = 0,25: g = +0,2 und +0,5 mit Saat | 1000 |
| dyng fein | L3: Q = 199,35, q_2 = 0,25, g = +0,5 mit Saat | 400 |
| paar | statisch, g = 0; 0,2; 0,5; d = 2, 4, 6, 8; dazu g = -0,5 bei d = 6 mit psi_2 -> i psi_2 (K4) | - |

- Frage 3 (Drehung und stille Stellen) nur, wenn Zeit bleibt; die stillen Stellen der beta_eff-Leiter sind 3D-Werte
  und gelten fuer den 2D-Querschnitt nicht unmittelbar.

## 4. Vorab-Erwartung (2026-09-30, vor jeder Rechnung; Zeit der Datei siehe Kopf)

| Nr. | Frage | Erwartung | p |
|---|---|---|---|
| V1 | Existenz g = 0 | Der Fluss konvergiert fuer alle q_2 in {0,1; 0,25; 0,4} bei allen vier Q zu einem gefuellten Wirbel: h maximal bei r = 0, f ringfoermig, Residuum < 1e-8 | 0,85 |
| V2 | Frequenzen | omega_2 < omega_1 (der Kern ist tiefer gebunden); Omega = omega_1 - omega_2 zwischen 0,01 und 0,08 bei Q = 110, q_2 = 0,25 | 0,75 / 0,5 |
| V3 | Energie, Bindung | E_fc(Q_1, Q_2) < E_v1(Q_1) + E_b(Q_2) in allen Faellen (der gefuellte Kern ist gebunden); bei Q = 110, q_2 = 0,25: E_fc = 96 +- 3, Bindung 8 +- 4 | 0,8 / 0,5 |
| V4 | Energie, Reihenfolge | E_b(Q) < E_fc(Q_1, Q_2) < E_v1(Q) bei gleichem Q, in allen Faellen | 0,9 |
| V5 | Kontrolle | q_2 = 0: omega^2 und E wie die RING-Tabelle auf 1e-3; Virialrest < 1e-4 | 0,9 |
| V6 | Dynamik g = 0 | Einkomponentig bei Q = 110,17: Teilung mit l = 2, gamma 0,055 bis 0,075 (RING-T 0,0641) | 0,85 |
| V7 | Dynamik g = 0 | Gefuellter Wirbel bei Q = 110,17, q_2 = 0,25 lebt laenger als der einkomponentige gleicher Ladung: kleinere Rate der staerksten Mode oder keine Teilung bis 1500 | 0,6 |
| V8 | Dynamik g = 0 | Er lebt auch laenger als der einkomponentige Wirbel mit gleichem J (Q_1 = 82,6) | 0,7 |
| V9 | Zerfallsart | Wo der gefuellte Wirbel zerfaellt: der Kern rutscht heraus (l = 1, Abstand der Schwerpunkte waechst zuerst) statt l = 2-Teilung | 0,4 |
| V10 | Waende | Bei \|g\| = 0,5 (Q = 199) entstehen nach der Rampe zwei Waende: F90 >= 0,6 und r k_eff >= 2 auf den Kreisen mit beiden Komponenten, genau 2 Vorzeichenwechsel | 0,65 |
| V11 | Waende | Bei \|g\| = 0,2 ebenso, aber breiter (F90 kleiner als bei 0,5) | 0,5 |
| V12 | Breite | gemessenes k zwischen 0,7 sqrt(\|g\| S) und 1,3 sqrt(2 \|g\| S) | 0,55 |
| V13 | Wandtyp | Ising-artig: die schwaechere Komponente faellt an der Wand auf unter die Haelfte ihres Kreismittels | 0,5 |
| V14 | Drehung | Das Muster dreht mit d arg P/dt = omega_1 - omega_2 (auf 30 %), gleicher Sinn wie die Windung; kein Einrasten auf Omega = 0 bis T | 0,6 |
| V15 | Schicksal g != 0 | bis T = 1000 bei Q = 199: zerfaellt frueher als bei g = 0 (Teilung, Kernaustritt oder psi_2-Wirbel dringt ein) 0,45; bleibt gebunden mit drehenden Waenden 0,4; rastet ein 0,15 | - |
| V16 | Symmetrie | g <-> -g ohne Saat: Dichten nach 90-Grad-Drehung gleich auf <= 1e-9 | 0,95 |
| V17 | Paar | bei g = 0,5 verbinden die Waende A und B (0 Vorzeichenwechsel auf dem Kreis um beide) fuer d = 4 bis 8 | 0,65 |
| V18 | Paar | E_g(d) - E_0(d) steigt linear mit d, Steigung zwischen 1,4 sqrt(\|g\|) S^{3/2} und 2,6 sqrt(2\|g\|) S^{3/2}: also Einschluss-artig (Kraft konstant, faellt nicht ab) | 0,55 |
| V19 | Paar | E_0(d) (g = 0) aendert sich zwischen d = 4 und 8 um weniger als ein Drittel der Wandarbeit bei g = 0,5 | 0,7 |
| V20 | Kontrollen | Ladungs- und Energiebilanz mit Randverlust auf <= 1e-3 relativ; L3 gleicher Ausgang, Raten auf 20 % | 0,75 |

## 5. Kontrollen

- K1 g = 0, q_2 = 0 gegen die bekannte einkomponentige Grenze: Profiltabelle (radial) und Teilung bei Q = 110,17 (RING-T:
  t = 75, gamma 0,0641, l = 2).
- K2 Bilanz: Q_1, Q_2 (g = 0), Q (g != 0), J und E gegen das, was die Randschicht schluckt, plus Rampenarbeit.
- K3 zwei Gitterstufen (grob gegen fein) fuer einen dyn0- und einen dyng-Lauf.
- K4 exakte Symmetrie g <-> -g (psi_2 -> i psi_2, 90-Grad-Drehung); im paar: E(-0,5, i psi_2) = E(+0,5).
- K5 radial: Virial, dE/dQ_a = omega_a, Residuum.

## 6. Kostenplan (Schaetzung, nicht gemessen)

- Grundlage ring.py auf der P4000: 5,9 bis 7 ns je Gitterpunkt und Schritt fuer ein Feld. Zwei Felder und Kopplung:
  etwa 14 ns; Messung je 20 Schritte etwa +25 %.
- dyn0 grob: 9 Laeufe x 256^2 x 30 000 Schritte: etwa 4 bis 5 min, bei geteilter Karte bis 8 min; notfalls in zwei
  Aufrufe geteilt (--laeufe).
- dyn0 fein: 2 x 384^2 x 24 000: etwa 2 min. dyng grob: 9 x 256^2 x 20 000: etwa 4 min. dyng fein: 1 x 384^2 x 16 000:
  unter 1 min. radial: unter 1 min. paar: 13 Konfigurationen x 4000 Iterationen: etwa 2 min.
- Zusammen etwa 15 bis 20 min Rechenzeit in 6 bis 8 Aufrufen, je unter 10 min; Spuren p4000a und p4000b (p4000b nur ohne
  WM-1-MB). Warten hinter KOLL-1 moeglich.
- Speicher: groesster Stapel 9 x 2 x 256^2 complex128 = 19 MB je Feld, etwa 20 Felder: unter 0,5 GB; frei auf den P4000
  etwa 1,3 GB (Ollama belegt den Rest).

## 7. Was welches Ergebnis bedeuten wuerde

- V3/V7 ja: Der zweite Kanal stabilisiert den Wirbel, indem er das Loch fuellt; das ist ein zusammengesetztes Objekt
  (Ring mit Kern), energetisch gebunden. Nein: der Kern ist nur Ballast.
- V10 bis V14 ja: Bei g != 0 wird der gefuellte Wirbel ein Rotor mit zwei Waenden; die Drehung des Musters ist die
  Frequenzdifferenz. Das waere die "oszillierende" Form der Frage Finns [H].
- V17/V18 ja: lineares Potential zwischen einem psi_1- und einem psi_2-Wirbel durch zwei pi-Waende, ein
  Einschluss-Analogon im Sinn der Vortex-Molekuele [L?]. Kein Anspruch auf QCD-Einschluss oder Quarks.

## 8. Nachtrag 2026-09-30 08:22:33 CEST (date), vor den Ergebnissen der .69-Laeufe

- **Vorschau offengelegt:** Der lokale Rauchtest radial (08:07:50 bis 08:07:56, CPU, 300 Iterationen, nur Q = 110,17) hat
  schon Zahlen geliefert: omega_1^2 0,648, omega_2^2 0,476 (Omega 0,115), E_fc 98,17, Bindung 5,97 bei q_2 = 0,25;
  K1 und K5 auf 1e-6. Die Vorab-Tabelle (Abschnitt 4) stand vorher fest (Kopie PLAN.md.eingefroren-20260930-0758) und
  bleibt unveraendert. Die .69-Laeufe sind die Messung.
- **Aenderungen am Code vor den Messlaeufen** (Rauchtests 08:07 bis 08:21):
  - Wirbelsuche: Umlauf durch die acht Nachbarn statt Plakette. Die Plakette verliert einen Wirbel, der genau auf einem
    Gitterpunkt oder einer Gitterlinie sitzt (Rauchtest 08:09). Zahlen dort sind Blockzahlen, keine Wirbelzahlen.
  - Kreise: zusaetzlich Windung von psi_1 und psi_2 einzeln (W1, W2).
  - paar (statisch): der abstossende Fleck hielt die Wirbel nicht (Windung um A nach dem Fluss 0). Ersatz: Phasenklammer
    auf dem Ring 0,5 < |x - A| < 2 (Phase von psi_1 = arg(x - A) + c, Amplitude frei), ebenso psi_2 um B; Q_1 = Q_2 = Q/2
    einzeln fest. Abstaende d = 5; 6,5; 8; 9,5 (d >= 5, damit sich die Ringe nicht beruehren); K4 bei d = 6,5.
    Bei g = 0 kann psi_1 den Bereich um A raeumen (U(2), keine Kopplung): E_0(d) ist dort eine Textur ohne Waende.
  - **neu paardyn:** dasselbe Paar ohne Zwang zeitlich entwickelt (g = 0; 0,2; 0,5; d = 3, 5, 7, 9; T = 250; g von
    Anfang an). Eine Kraft F zwischen den Wirbeln wird (Magnus) zu einer Drehung des Paars mit
    Omega = F/(pi rho_a d), rho_a = 2 omega S_a = omega S_0 [Hand, Magnus-Kraft 2 pi rho v je Wirbel, nicht nachgelesen].
    Konstante Kraft (Einschluss): Omega d konstant; Kraft ~ 1/d: Omega d^2 konstant.
- **Vorab zu paardyn** (neu, vor jedem paardyn-Lauf):

| Nr. | Erwartung | p |
|---|---|---|
| V21 | g = 0,5: das Paar dreht; Omega d ist ueber d = 5, 7, 9 konstant auf +-30 % (Einschluss-artig), Omega d^2 nicht | 0,45 |
| V22 | g = 0,5: F = pi rho_a Omega d liegt zwischen 0,5 und 1,5 x 2 sigma_Pol (2 sigma_Pol = 2 sqrt(g) S_0^{3/2}) | 0,4 |
| V23 | g = 0: \|Omega\| < 0,3 x \|Omega(g = 0,5)\| beim gleichen d | 0,6 |
| V24 | g = 0,5, d = 3: die Wirbel laufen bis T zusammen (d < 1,5, gemischter Wirbel) | 0,35 |
| V25 | g = 0,2: \|Omega\| kleiner als bei 0,5, Verhaeltnis 0,6 +- 0,2 (sqrt(g)-Skalierung der Wandspannung) | 0,4 |
