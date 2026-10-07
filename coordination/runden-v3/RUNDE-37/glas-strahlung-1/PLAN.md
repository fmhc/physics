# GLAS-STRAHLUNG-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48, Glas-Zweig)

- Start 2026-10-05 09:03:22 CEST (date). Plantext ab 09:23:55 CEST (date), vor jeder Hauptrechnung. Zeitbox 150 min,
  also bis 11:33:22 CEST; danach kein neuer Lauf.
- Grundlage: KARTE.md (GS0 bis GS3; Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Werkzeug: code/gs.py (neu). Unveraendert kopiert und importiert: tg.py (TT-GLAS-1, ec48a258...), dz.py (TT-GLAS-2),
  ew.py (fa7b6417...), tp.py (419d7da6...), pn.py, mn.py, inz.py, nachtrag_iso.py, nachtrag_umkreis.py (IMPULS-NETZ-1);
  dk.py nur kopiert. Benutzt werden: tg.zufallsnetz, tg.modell, tg.ops, tg.netz_V; dz.basis, dz.reduziert, dz.assemble;
  pn.richtungen, pn.ACHSEN, pn.DMAT, pn.J_ISO, Konstanten; die Formel von nachtrag_umkreis.K_umkreis (gebuendelt
  nachgebaut in gs.K_umk, ebenso pn.K_aus_laengen in gs.K_p1).
- Rauchtests vor dem Plantext und vor dem Einfrieren (07:23 bis 07:26 UTC, Rauchsaaten 901, 902, grobes Richtungsgitter
  2 x 4): gelesen nur Rueckgabewerte, Laufzeiten, Speicher und Schluessel (Abschnitt 8).
- Kennzeichen: [M] eigene Mathematik (vorab), [E] gerechnet, [P] Projektdatei, [ES] eigener Schluss, [F] Festlegung,
  [H] Hypothese, [L?] Literatur ohne Abruf. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Uebertragung des IMPULS-NETZ-1-Aufbaus auf eine Glas-Superzelle [F, M]

### 1.1 Netze, Gewichte, Bloch-Randbedingungen

- Glas = periodisches 3D-Poisson-Delaunay-Netz mit N Punkten (Dichte 1) im Wuerfel L = N^(1/3), genau wie TT-GLAS-1/2
  (tg.zufallsnetz mit SAAT_BASIS 4537: Saat s gibt dieselben Netze wie dort). Die Superzelle ist die Elementarzelle
  eines Kristalls mit Gittervektoren L e_i; Bloch-k ist frei, Felder in der Bildzelle R tragen e^(i k.R).
- Modell wie TT-GLAS (R1, Regge-Steifigkeit B, Eckverschiebung M, skalare Regel c = -B W, Bewegungsenergie
  (n_e.n_f)^2 - 1/2 je Tetraeder mit **J = 1**, "Bewegungsgewichte wie TT-GLAS"). Auf V (Kontrolle) J_iso je
  Tetraeder-Art (pn.J_ISO) wie IMPULS-NETZ-1.
- Materie (Hauptarm): **P1-Gewichte** je Tetraeder (pn.K_aus_laengen, 3D-Kotangens), Spannung sigma_e = l_e dE/dl_e,
  Impuls J aus der Gitter-Bilanz J' = -M^H sigma (IMPULS-NETZ-1, Teil 1), Kraft mit J: f = -S^H sigma - A_red^-1 S^H A
  P_M sigma. V1-Energie in der skalaren Regel aus der Kontinuums-Erhaltung (wie pn.py). Eckvolumina baryzentrisch.
- Nebenarm (beschreibend, ohne Urteil): umkreisbasierte Gewichte *1 (nachtrag_umkreis.K_umkreis) statt P1, sonst alles
  gleich (Takt-konsistenter Fall, TAKT-UMKLAPP-1 HT0: P = 8 d0^H *1 d0 [P]).

### 1.2 Wellenzahl und Richtungen

- Bloch-k = kabs n. **Glas: kabs = 0,01** (Punktabstand 1; wie TT-GLAS EPS1, dort wegen der Splitter-Skala gewaehlt);
  das entspricht k l_P' = 0,012 mit l_P' = l_P 40^(1/3) = 1,209 (gleiche Eckdichte wie V). **V: kabs = 0,01/l_P**
  (kl = 0,01 wie IMPULS-NETZ-1). Die kleinste Gitter-Wellenzahl der Superzelle ist 2 pi/L = 1,25 (N = 128) bis 0,79
  (N = 512), also kabs << 2 pi/L: die Rechnung ist langwellig.
- Richtungen: Gauss-Legendre nt x nphi wie pn.richtungen; gerechnet wird nur die obere Halbkugel. **Glas: 6 x 12
  (36 Richtungen je Netz)**, V: 10 x 20 (100 Richtungen; wie IMPULS-NETZ-1).
- k -> -k [M]: Alle Operatoren sind reell bis auf Bloch-Phasen; bei -k sind B, A, M, c, Moden und Kraefte konjugiert.
  Fuer eine reelle Quelle (phi) ist die untere Halbkugel gleich der oberen; fuer die komplexe Kreisbahn-Quelle S gilt
  |A_j(-n; S)|^2 = |A_j(n; S^*)|^2. Die Auswertung setzt die untere Halbkugel so zusammen.

### 1.3 Quellen und Quellgroesse gegen Zellgroesse

- **Kreisbahnen (Hauptgroesse):** kompakte spurfreie Quelle S = (u + i w)(u + i w)^T zur Bahnnormale m (u = m x
  (0,3; 0,5; 0,7) normiert, w = m x u), wie IMPULS-NETZ-1. Umgesetzt als gleichfoermige Spannung S in jeder Zelle mit
  Bloch-Phase e^(i k.m_e): sigma_e = Q_e : (S - tr S 1), Q_e = Summe_{t, p -> e} 0,5 l_p X_t^T dK_p X_t (wie
  nachtrag_iso.Q_map; Bloch-Amplitude der integrierten Spannung je Superzelle = V S). Das ist der Grenzfall k -> 0 einer
  kompakten Quelle; er mittelt ueber die ganze Superzelle. Gerechnet wird mit 6 Basistensoren; jede Bahnlage ist eine
  Linearkombination (Auswertung).
- **phi-Quadrupol (drei Quellachsen [001], [111], (1,2,3)):** zwei gegenphasige Gauss-Klumpen um x_c = pos[0], w = d =
  0,8 l_P', Abschneideradius 3,2 x 40^(1/3) = 10,94 (V: w = d = 0,8 l_P, 3,2 wie pn.quelle). Summiert wird ueber alle
  Bilder der Superzelle, deren Tetraeder-Schwerpunkt im Radius liegt: Die Quelle sitzt einmal im unendlichen periodischen
  Glas, ihre Bloch-Komponente ist sigma(k) = Summe_R e^(-i k.R) sigma(R) (wie pn.quelle). Sie ist groesser als die
  Superzelle N = 128 (Durchmesser ~10 gegen L = 5); das ist bei dieser Bauweise erlaubt.
- **Vorab [M, ES]: Der phi-Quadrupol ist gittergross.** Er sieht eine feste Zahl von Tetraedern um pos[0], unabhaengig
  von N. Seine Abweichung von Einstein ist eine lokale Eigenschaft der Umgebung und faellt mit N nicht; berichtet wird
  sie nur beschreibend (Mittel und Streuung ueber Saaten). Die Fragen GS1 bis GS3 betreffen die Kreisbahnen.

### 1.4 Messgroesse: Goldene Regel bei linearer Dispersion [M]

- Je Richtung n und TT-Mode j (zwei weichste Moden von L^H B_red L, X = L U wie inz.py): Kopplung g_j = X_j^H f,
  om2_j, Tempo c_j = sqrt(om2_j)/kabs.
- pn.py rechnet die Leistung mit der Goldenen Regel auf der Massenschale (28 kl-Werte, Interpolation). Bei kleinem k
  (lineare Dispersion, k-unabhaengige Kopplungskonstante) ist das gleichwertig zu [M]:
  P/P_E = Summe_n w_n Summe_j (|A_j|^2/om2_j) (c0/c_j) / Summe_n w_n C_E(n),
  A_j = g_j(S + J) + (c0/c_j)^2 (n.S~.n) g_j(V1-Einheitskraft), C_E = Lambda_n[S~]:S~^*/(V k^2).
  - (c0/c_j)^2 im V1-Term ist das pn.py-eps auf der Massenschale; der Faktor c0/c_j ist 1/(Gruppengeschwindigkeit) der
    Mode gegen c0 im Einstein-Bezug.
  - Normierung: Der Bezug C_E = 4 Lambda[S~]/k^2 in inz.py gilt fuer V_Zelle = 1/4; allgemein ist er
    Lambda[S~]:S~^*/(V k^2) [M, aus der affinen TT-Steifigkeit a^H B a = V k^2 abs(h)^2].
- **c0** := Wurzel aus dem Raumwinkelmittel von om2_j/k^2 ueber beide Zweige [F] (inz.py: einfaches Mittel ueber die
  Richtungen; fuer J_iso gleich auf 1e-5). Auf dem Glas sind die Tempi je Netz anisotrop (TT-GLAS: Spanne 15 % bei
  N = 128 [P]); dann hat P/P_E einen kleinen Jensen-Anteil von etwa 3/8 Var(om2/(c0 k)^2) [M], geschaetzt 6e-4
  (N = 128) bis 1,5e-4 (N = 512) [Kopfrechnung]. Er gehoert zur Abstrahlung (langsame Richtungen strahlen mehr).
- **G_N/G** = (8 V/nV)/(Raumwinkelmittel von lambda_min(P)/k^2), P = -W^H B W (Verallgemeinerung von 0,2/lambda: 0,2 =
  8 x 0,25/10). Dazu beschreibend die direkte Newton-Antwort m^H P^-1 m 8 V k^2/abs(Summe m)^2.
- **G_rad/G_N = (P/P_E)/(G_N/G)** fuer V1+S+J (Hauptgroesse). Beschreibend: Kopplungsmass K (ohne c0/c_j, V1 mit
  eps = 1), ohne J, nur S, Nebenarm umkreisbasiert.

### 1.5 Bahnlagen (fest vor der Rechnung) [F]

- 24 Bahnnormalen: [001], [111], [110], (1,2,3); 8 Zufallsnormalen mit Saat 31 (die 12 Lagen von IMPULS-NETZ-1);
  12 weitere Zufallsnormalen mit Saat 47 (numpy default_rng, normal(size = (12, 3)), normiert). Alle Urteile ueber
  alle 24.

### 1.6 Kanaele [F]

- Je Richtung n wird S zerlegt: TT = Lambda_n[S], L = P S nn + nn S P (laengs-quer), nn-Teil = S - TT - L (fuer
  spurfreies S gleich (n.S.n)(nn - P/2)). V1 = Energiekanal (Kraft (c0/c_j)^2 V (n.S.n) g_j(V1)).
- Kanalanteile als Zuwaechse in fester Reihenfolge (Interferenz im jeweiligen Zuwachs):
  d_TT = G(TT) - 1, d_L = G(TT + L) - G(TT), d_nn = G(S) - G(TT + L), d_V1 = G(S + V1) - G(S); Summe = G - 1.
  Gleicher Nenner (Einstein, nur TT) und gleiches G_N fuer alle.

## 2. Kontrolle GS0 auf Netz V [F]

- Derselbe Code (gs.py netz --N 0): V aus tg.netz_V (allgemeine Form, wie TG-G0 in TT-GLAS-1), J_iso, phi-Quadrupol
  w = d = 0,8 l_P, kl = 0,01, 10 x 20 Richtungen, V1+S+J. Soll: IMPULS-NETZ-1 h1.json dyn_V1SJ = 1,0296610138 /
  1,0040051253 / 0,9674684346 [P].
- **Vorab [M]:** Unterschiede zu inz.py sind nur die Auswertung bei festem k (statt Massenschale mit Interpolation) und
  je Mode statt Zweigmittel; fuer J_iso (Tempi isotrop auf 1e-5) und kl = 0,01 erwarte ich Abweichungen <= 1e-4.
  GS0 prueft also die Umsetzung (P1-Buendelung, Q, Quellbilder, J-Kraft, V1-Kraft, Normierung C_E, G_N), keine Physik.
- Beschreibend: Kreisbahnen S+J auf V gegen IMPULS-NETZ-1 (0,99850 / 1,00122 / 1,00054 / 1,00054 [P]); V mit 6 x 12
  Richtungen (Quadratur des Glas-Gitters).

## 3. Netze, Saaten, Laeufe [F]

- N = 128: Saaten 1 bis 8; N = 256: Saaten 1 bis 8; N = 512: Saaten 1 bis 6 (Karte: mindestens 4). Je Netz alle 36
  Richtungen; ein Netz zaehlt nur vollstaendig.
- Beschreibende Zusatzlaeufe (kein Urteil): N = 128, Saat 1 mit 8 x 16 Richtungen (Quadratur) und mit kabs = 0,02
  (Grenzfall k -> 0).
- Reihenfolge nach Zeitbox: zuerst GS0 und N = 128 (CPU), gleichzeitig N = 256 und dann N = 512 (GPU).

## 4. Ableitbarkeitsprobe und Verkettung (vor jeder Rechnung)

- **GS0 vorab ableitbar [M]** (Abschnitt 2): gleiche Physik, andere Auswertung; keine Messung.
- **G_N = G auf dem Glas vorab ableitbar [M, verkettet]:** P = 8 d0^H *1 d0 (HT0, auch auf Glasnetzen [P]). Der
  umkreisbasierte Laplace hat auf Delaunay-Netzen lineare Praezision: Summe_{e an v} *1_e (x_u - x_v) = Summe |*e| e^ = 0
  (geschlossene Voronoi-Zelle), und Summe_e *1_e e e^T = V 1 (Divergenzsatz je Voronoi-Zelle; die Tangentialteile heben
  sich paarweise weg). Dann loest das affine Feld die Takt-Gleichung exakt, der O(k)-Rest verschwindet, und
  lambda_min(P) = 8 V k^2/nV (1 + O(k^2)). Also G_N/G = 1 + O(k^2) auf jedem Glasnetz [M]; KN ist nur Kontrolle.
  (Je Tetraeder gilt Summe *1 e e^T = V_t 1 nicht: Ecktetraeder gibt Nebendiagonale 1/24 [M, von Hand]; erst die
  Summe ueber die Voronoi-Zelle ist exakt.)
- **TT-Steifigkeit affin exakt [P]:** TT-GLAS-1 Z1 (affine Regge-Steifigkeit = V k^2 auf <= 1e-5) und TT-GLAS-2
  (Relaxation traegt <= 1e-5). Die Steifigkeit liefert also keinen isotropen Rest. Ob die Kopplung der TT-Quelle an die
  projizierte Welle exakt ist, ist nicht abgeleitet; auf V war sie 1 + 1,5e-6 [P].
- **GS1 (Kette, [H] mit [M]-Teilen):** Eine Superzelle ist eine Summe aus ~6,8 N weitgehend unabhaengigen Tetraedern;
  jede richtungsabhaengige Groesse einer Probe (Tempo, Lecks) hat Schwankungen ~N^-1/2 (Zentraler Grenzwertsatz bei
  kurzreichweitiger Korrelation). TT-GLAS bestaetigt das fuer die TT-Spanne (-0,47 bis -0,56 [P]). Die Lagenabhaengigkeit
  von G entsteht linear aus diesen Schwankungen (Kreuzterm Einstein-Amplitude x Leck, Tempo-Faktor c0/c_j), also
  erwartet p ~ -0,5; quadratische Terme (abs(Leck)^2) fielen wie N^-1. Beides erfuellt p <= -0,4. **GS1 ist damit
  wahrscheinlich, aber nicht abgeleitet:** offen ist, ob die Lecks kurzreichweitig sind, und die Anpassung ueber einen
  Faktor 4 in N mit 6 bis 8 Netzen je N hat eine Unsicherheit von etwa +-0,15 [Kopfrechnung].
- **GS3 (Kette, [M] plus [H]):** In einem isotropen Medium kann eine skalare Quelle (V1, Energie) keine Helizitaet-2-Mode
  anregen (Drehung um n). Im statistisch isotropen Ensemble ist daher der Mittelwert der V1-Amplitude E[dA_V1] = 0 [M,
  bis auf die Wuerfelsymmetrie des periodischen Kastens, TT-GLAS-1 Abschnitt 7]. Der Kreuzterm Einstein-TT x V1 mittelt
  sich ueber alle Bahnlagen exakt weg (<S_ab S_cd^*> isotrop, TT_n[nn] = 0 [M]); mit 24 Lagen naeherungsweise. Es bleibt
  E abs(dA_V1)^2 ~ Varianz ~ N^-1 [H, CLT]. **Erwartung aus der Kette: Der V1-Rest faellt wie ~N^-1; GS3 sollte
  verfehlt werden**, ausser es gibt einen Mechanismus ausserhalb dieser Kette (Kasteneffekt, langreichweitige
  Korrelation). Das ist eine Vorhersage, keine Messung; gerechnet wird trotzdem.
- **GS2 nicht ableitbar:** Der Mittelwert enthaelt N^-1-Terme (Jensen-Anteil der Tempi, abs(Leck)^2) und moeglicherweise
  eine isotrope Umnormierung der TT-Kopplung, deren Groesse unbekannt ist.
- **phi-Quadrupol:** lokale Groesse (1.3), faellt mit N nicht [M]; kein Urteil.

## 5. Urteilsregeln (mechanisch in gs.py aus)

- Hauptgroesse je Netz und Bahnlage: G = P_P1_SV1_J (V1+S+J, P1, Goldene Regel, durch G_N/G).
- **GS0** (Kontrolle: Code gibt auf V 1,030 / 1,004 / 0,967 auf 1e-3 wieder):
  - Plan: abs(G_phi - G_ref) <= 1e-3 fuer alle drei Achsen (G_ref aus h1.json, Abschnitt 2).
  - Kartenwortlaut: abs(G_phi - 1,030 / 1,004 / 0,967) <= 1e-3.
- **GS1** ([H] Streuung ueber die Bahnlagen faellt mindestens wie N^-0,4, Anpassung N = 128 bis 512):
  - Streuung je Netz = Standardabweichung (ddof 1) von G ueber die 24 Lagen.
  - Plan: Gerade ln(Streuung) gegen ln N ueber alle vollstaendigen Netze, Steigung p <= -0,4.
  - Kartenwortlaut: Gerade durch die drei Mittelwerte der Streuung je N, Steigung <= -0,4.
  - Nicht entscheidbar, wenn ein N weniger als 2 vollstaendige Netze hat. Bootstrap (Netze je N, 2000, Saat 2026) nur
    beschreibend.
- **GS2** ([H] Mittelwert ueber Lagen und Saaten bei N = 512 innerhalb 1e-3 bei 1): abs(Mittel - 1) <= 1e-3 (Plan und
  Wortlaut). Nicht entscheidbar bei weniger als 2 Netzen N = 512.
- **GS3** ([H] V1 traegt einen isotropen Rest, der mit N nicht faellt; Mittelwert-Abweichung bei N = 128 und 512 gleich
  auf 30 %):
  - Kartenwortlaut: D_N = Mittel(G) - 1; D_128 und D_512 gleiches Vorzeichen, abs(D_512/D_128 - 1) <= 0,3, und der
    V1-Zuwachs traegt bei beiden N mindestens die Haelfte: abs(d_V1,N) >= 0,5 abs(D_N).
  - Plan: mittlerer V1-Zuwachs d_V1 (ueber Lagen und Saaten) bei N = 128 und 512 gleiches Vorzeichen,
    abs(d_V1,512/d_V1,128 - 1) <= 0,3 und abs(d_V1,512) > 2 Standardfehler (ueber die Netze).
  - Nicht entscheidbar, wenn N = 128 oder N = 512 weniger als 2 vollstaendige Netze hat.
- Bedeutung der Ausgaenge: wie auf der Karte; nichts daran geaendert.

## 6. Auswertung und Bild (gs.py aus, auf der .69)

- Je Netz: G je Lage (alle Groessen aus 1.4 und 1.6), Mittel, Streuung, Min, Max; G_N/G (zwei Wege), Tempo-Spanne,
  Kontrollen. Je N: Mittel ueber Lagen und Saaten, Streuung der Netzmittel, mittlere Lagenstreuung, Kanalzuwaechse
  (P1 und umkreisbasiert), phi-Quadrupol je Achse (Mittel und Streuung ueber Saaten). Exponenten: Hauptgroesse,
  dazu beschreibend K, S+J, nur TT, umkreisbasiert, Tempo-Spanne.
- Bild: links G_rad/G_N ueber die 24 Bahnlagen fuer jedes N (alle Netze) mit V und dem Doppelpulsar-Band; Mitte
  Streuung gegen N doppellogarithmisch mit Gerade und N^-0,4; rechts Kanalzuwaechse gegen N.
- Kontrollen: KP1 (Summe sigma n n^T = -V T, P1 und umkreisbasiert) <= 1e-10 relativ; KF (M^H B) und KR (c^H M) am
  ersten k je Netz <= 1e-10; KJ (M^H P_M sigma = M^H sigma) <= 1e-8; Cholesky und voller Rang an allen k; Luecke
  om2_3/om2_2 >> 1; KN G_N/G = 1 auf 1e-3 (vorab, Abschnitt 4).

## 7. Agenten-Erwartungen (vorab; kein Kartenurteil)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| A1 | GS0 auf <= 1e-4 | 80 % |
| A2 | KN: G_N/G auf dem Glas in [0,999; 1,001] je Netz | 85 % |
| A3 | Steigung der Lagenstreuung zwischen -0,7 und -0,3 | 65 % |
| A4 | mittlerer V1-Zuwachs bei N = 512 kleiner als halb so gross wie bei N = 128 (Betrag) | 60 % |

## 8. Laeufe (.69, kleintest.sh, Spuren p4000a, p4000b, cpu, cpu7; je Lauf <= 600 s)

- Arbeitsordner /home/fmh/fmhc-physics-remote/glas-strahlung-1/; eingefrorener Code nach code/ (per scp in einen neuen
  Ordner, dann mv; nie in place).
- **Rauchtests** (vor dem Einfrieren, gelesen nur rc, Laufzeiten, Speicher, Schluessel): r1 V (cpu, 0,7 s), r2 N = 128
  zwei Rauchsaaten (cpu, 7 s je Netz, 1,6 s je k), r3 N = 512 (p4000a, 8,7 s je k, GPU 0,70 GB, RAM 1,1 GB), r4 N = 256
  (p4000b, 1,4 s je k, GPU 0,19 GB), r5 und r6 Auswertung (3 s); alle rc = 0.
- **Laufliste:**

| Lauf | Spur | Aufruf (code/gs.py ...) | Schaetzung |
|---|---|---|---|
| GV | cpu | netz --N 0 --nt 10 --nphi 20 --out lauf/v.json (GS0) | 10 s |
| GV6 | cpu | netz --N 0 --out lauf/kontrolle/v-6x12.json (beschreibend) | 5 s |
| C128a | cpu | netz --N 128 --saaten 1,2,3,4 --out lauf/gs | 4 x 60 s |
| C128b | cpu7 | netz --N 128 --saaten 5,6,7,8 --out lauf/gs | 4 x 60 s |
| Q128 | cpu | netz --N 128 --saaten 1 --nt 8 --nphi 16 --out lauf/kontrolle/q8x16 (beschreibend) | 110 s |
| K128 | cpu7 | netz --N 128 --saaten 1 --kabs 0.02 --out lauf/kontrolle/k002 (beschreibend) | 60 s |
| A256 | p4000a | netz --N 256 --saaten 1,2,3,4 --out lauf/gs | 4 x 52 s |
| B256 | p4000b | netz --N 256 --saaten 5,6,7,8 --out lauf/gs | 4 x 52 s |
| A512-1, -3, -5 | p4000a | netz --N 512 --saaten s --out lauf/gs (je ein Netz je Lauf) | je 320 s, GPU 0,7 GB |
| B512-2, -4, -6 | p4000b | netz --N 512 --saaten s --out lauf/gs | je 320 s |
| AUS | cpu | aus --v lauf/v.json --ein lauf/gs-N*.json --out aus/auswertung.json --bild aus/bild-glas-strahlung.png | 5 s |
| AUSK | cpu | aus --v lauf/kontrolle/v-6x12.json --ein lauf/kontrolle/*.json --out aus/kontrolle.json (beschreibend) | 5 s |

- Frist im Skript 540 s (keine neue Richtung danach; ein Netz ohne alle 36 Richtungen zaehlt nicht). Bricht ein Lauf
  (Speicher, Laufzeit) ab, wird er einmal mit demselben eingefrorenen Code auf der anderen GPU-Spur wiederholt
  (gekennzeichnet). Schlusszeit der Laufketten: kein neuer Lauf nach 11:05 CEST.
- Urteile nur aus AUS (eingefrorener Code, alle vollstaendigen Netze der Laufliste).
