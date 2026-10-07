# TT-GLAS-1: Plan (Code-Agent, Runde 45, Zweig Glas)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 04:18:23 CEST (date). Plantext ab 04:37:36 CEST (date),
  vor jeder Rechnung mit Werten. Zeitbox 120 min, also bis 06:18:23 CEST; kein neuer Lauf danach.
- Grundlage: KARTE.md (TG-G0 bis TG-G3; Wortlaut, Schwellen und Wahrscheinlichkeiten der Karte unveraendert).
- Kennzeichen: [M] Mathematik (vorab ableitbar), [E] hier gerechnet, [P] Projektdatei, [F] eigene Festlegung,
  [H] Hypothese, [L] Literatur aus dem Gedaechtnis. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Ableitbarkeitsprobe

- **Projektsuche** (grep, Ausschluesse wie vorgegeben): Regge-Kruemmung auf Poisson-Delaunay-Netzen gibt es nur im
  skalaren (konformen) Sektor: REGGE-SCHAUM-1 (RUNDE-36) [P]. Dort gibt der Schaum Newtons G auf 0,02 % wie das
  Kuhn-Gitter; der Tensor K/8 ist richtungsfrei (0,9995 bis 1,0009); Splitter (V_min 3e-5 bis 1e-4) kosten dort
  Genauigkeit der Winkelableitungen (Schlaefli bis 8e-8). TT-Moden auf Zufallsnetzen: keine Datei.
- **Rohdaten (jq 'keys'):** TT-ISO-1 lauf-69/kontrolle.json (hauptlauf_V_23, nachtrag_*, ohne_A1R1_13, steifigkeit_affin,
  symmetrie_*): nur regelmaessige Netze V, S, ohne. EINE-WELT-LOCH-1 lauf-69: nur V, S, ohne. STRICH-NETZ-1 lauf-69
  (eigen-1-fem, klein-2000, kontrolle): Zufallsnetze, aber nur skalare und Weyl-Felder. Es gibt keine Rohdaten, aus denen
  TG-G0 bis TG-G3 schon folgen.
- **Vorab ableitbar [M]:**
  - Poisson-Punkte sind statistisch isotrop; das Ensemble-Mittel jeder Richtungsgroesse ist richtungsfrei. TG-G2 ist nur
    Kontrolle (wie die Karte sagt).
  - Zentraler Grenzwertsatz: Ist die effektive (homogenisierte) TT-Antwort einer Superzelle eine Summe kurzreichweitig
    korrelierter Beitraege, streut ihr anisotroper Teil wie N^(-1/2). TG-G1 ist daher schwach informativ. Nicht
    ableitbar ist, ob Splitter (Beitraege ~ 1/V_t) so schwere Raender erzeugen, dass der Exponent abweicht [H].
- **Teilweise vorab, als Hypothese [P, H]:** TT-ISO-1 fand die Regge-Steifigkeit affiner TT-Wellen a^+ B a / k^2 auf drei
  verschiedenen Triangulierungen (V, S, ohne) gleich dem Volumen mal 1 (0,25 je Zelle, Spanne <= 2,5e-8). REGGE-SCHAUM-1
  fand die konforme Summenregel auch auf Zufallsschaum. Lesart [H]: Regge ist eine konsistente Diskretisierung; die
  fuehrende Steifigkeit einer glatten Welle ist fuer jede Triangulierung der Kontinuumswert. Dann ist die affine
  Steifigkeit auf jedem Netz isotrop, und jede Anisotropie sitzt in der effektiven Masse nach der Reduktion
  (nichtaffine Relaxation). Zusatz Z1 prueft das beschreibend bis N = 8000.
- **Folge fuer den Ersatz der Karte [M + H]:** Mit der Lagrange-Masse A3 ist die affine Masse einer TT-Welle auf jeder
  Triangulierung isotrop (TT-ISO-1 Abschnitt 6: Phi_t^-1 a_t = h, Masse = Summe V_t/V_F |h|^2) [M]. Mit der Hypothese
  oben waere der Rayleigh-Quotient affiner TT-Wellen bei kleinem k auf **jedem** Netz exakt isotrop: Der Ersatz waere
  vorab fast festgelegt und traegt keine Information ueber das Glas. Mit der Hamilton-Masse A1 braucht der Quotient A^-1
  auf der Zwangsflaeche, ist also nicht affin auswertbar.
- **Nicht ableitbar:** der Vorfaktor der Streuung (TG-G3), die Zahl masseloser TT-Moden auf Zufallsnetzen, ihre
  Stabilitaet, die Groesse der nichtaffinen Relaxation.

## 2. Wahl: volles Hamilton-Netz, kein Ersatz [F]

- **Entscheidung:** Ich uebertrage das Hamilton-Netz von EINE-WELT-LOCH-1 woertlich auf periodische
  Poisson-Delaunay-Netze und rechne die Moden exakt (dicht), wie ew.py. Gruende: (1) Der Ersatz ist nach Abschnitt 1
  weitgehend vorab festgelegt. (2) Nur das volle Modell kann die zwei masselosen TT-Moden zaehlen und die Stabilitaet
  pruefen (die Punkte, die die Karte "den wichtigeren Befund" nennt).
- **Preis:** Die dichte Rechnung kostet ~E^3 je k-Punkt (E ~ 7,8 N Kanten). Rauchzeiten je k-Punkt (1 Thread, .69):
  N = 64: 0,3 s; N = 128: 2 s; N = 256: 15 s. N = 512 waere ~120 s je Punkt, also ~35 min je Netz: nicht in Laeufen zu
  hoechstens 10 min und nicht in der Zeitbox.
  - **Abweichung von der Karte [F]:** N-Leiter 32, 64, 128, 256 statt "etwa 500 bis 8000". Der Exponent wird damit unter
    der Kartenspanne gemessen; TG-G3 (N ~ 8000) ist nur extrapoliert.
- **Uebertragung [F], Code code/tg.py:**
  - Netz: N Punkte gleichverteilt im Wuerfel [0, L)^3, L = N^(1/3) (Dichte 1, Abstand ~1), Saat
    np.random.default_rng([4537, N, saat]); periodische Delaunay-Triangulierung ueber 27 Kopien mit Saum 4 (wie
    strich-netz-1/spinnetz.zufallsnetz); behalten wird je Tetraeder die Kopie mit Schwerpunkt im Grundwuerfel.
  - Kanten, Ecken und Tetraeder in Bloch-Form wie ew.py (Kantenschluessel: Anfangsecke, Endecke, Kastenversatz).
  - B = Summe_t l D_t l (Regge, D = d theta/d l je Tetraeder, komplexer Schritt nach den Eckkoordinaten und C^+, wie
    ew.zelle_D, vektorisiert); Eichung = Eckverschiebung M; skalare Regel je Ecke c_v = -B w_v (Gewicht l_e, g = 1);
    Bewegungsenergie je Tetraeder A0 = (n_e . n_f)^2 - 1/2 mit J = 1 fuer alle Tetraeder; Zwangsflaeche
    S = orthonormales Komplement von Bild[M, c] (QR, bei Rangverlust SVD); omega^2 = Eigenwerte von
    (S^+ A S)(S^+ B S) (Hauptlauf-Paarung A1R1). Rechenweg: Cholesky A_red = L L^+, Eigenwerte der hermiteschen
    L^+ B_red L (gleiche Eigenwerte); ist A_red nicht positiv definit, allgemeine Eigenwerte von A_red B_red.
  - Eichung: Auf dem Zufallsnetz liegt jede Ecke in vielen Tetraedern; nach dem Argument von EINE-WELT-LOCH-1 (PLAN 1.3)
    faellt B1 dann mit der Eck-Eichung zusammen [M]. Ich nehme direkt die Eck-Eichung.
- **k-Wahl [F]:** Der periodische Kasten ist eine Superzelle; in Bloch-Form ist jedes k erlaubt (die Kasten-k = 2 pi m/L
  sind der Sonderfall Phase 1). Ich messe den langwelligen Grenzfall der periodisch fortgesetzten Probe:
  |k| = 1e-2 in 13 Richtungen, dazu |k| = 2e-2 in [100], [110], [111] fuer die Linearitaet. 2e-2 << 2 pi/L
  (>= 0,99 fuer N <= 256).
  - 1e-2 statt 1e-3 wie in ew.py, weil Splitter die Skala s = max omega^2 stark erhoehen koennen (D ~ l^2/V_t,
    REGGE-SCHAUM-1). Bei 1e-2 liegt omega^2 der TT-Moden ~1e-5 und bleibt weit ueber der numerischen Toleranz 1e-12 s.
    Die Dispersion ist O(k^2 l^2) ~ 1e-4 relativ; in V ist sie nach EINE-WELT-LOCH-1 (Linearitaet 8,5e-8 zwischen 1e-3
    und 2e-3) bei 1e-2 ~ 3e-6 relativ [Kopfrechnung].
- **Richtungen [F]:** die 13 Wuerfelachsen [100], [010], [001], [110], [1-10], [101], [10-1], [011], [01-1], [111],
  [11-1], [1-11], [-111]. Sie decken die Halbkugel ab (omega^2(k) = omega^2(-k)); das Zufallsnetz hat keine Symmetrie,
  die einen Sektor reichen liesse. Beide TT-Polarisationen = die zwei untersten positiven masselosen Moden.
- **Saaten:** je N die Saaten 1 bis 12 (48 Netze). Rauchnetze hatten die Saaten 901 bis 903 und gehen nicht ein.

## 3. Klassen und Kennzahlen (mechanisch in tg.py und tg_auswertung.py)

- Je k-Punkt mit s = max |omega^2| und tau = 1e-12 s:
  - wachsend: Re omega^2 < -tau oder |Im omega^2| > tau;
  - masselos: nicht wachsend und |omega^2| <= 30 eps^2 (eps = |k|);
  - Luecke: nicht wachsend und omega^2 >= 100 eps^2;
  - unklar: alles andere.
  - (Abweichung von ew.py [F]: dort 1e-9 s, 1e3 eps^2, 1e-4 s und 2e3 eps^2. Die s-relativen Schwellen versagen bei
    grossem s durch Splitter; die eps-Schwellen sind an das groessere eps angepasst.)
- **TT-Anteil:** an [100], [110], [111] bei |k| = 1e-2 fuer die zwei untersten masselosen Moden, Tensor-Fit mit
  Eichspalten wie ew.tensor_fit, tp.tt_anteil.
- **Regulaeres Netz:** an allen 16 Punkten genau 2 masselose Moden, beide positiv (> tau), keine wachsende oder unklare
  Mode; an den drei TT-Richtungen TT-Anteil >= 0,99 fuer beide und linear
  (|omega^2(2e-2)/(4 omega^2(1e-2)) - 1| <= 0,01).
- **Spanne je Netz:** max/min - 1 ueber die 26 Werte omega^2/k^2 (13 Richtungen x 2 Zweige, |k| = 1e-2). Sie enthaelt die
  Aufspaltung der zwei Polarisationen (wie TT-ISO-1).
- **Richtungsabweichung je Netz:** wbar_d = Mittel der zwei Zweige in Richtung d; delta_d = wbar_d / Mittel_d(wbar) - 1.

## 4. Urteilsregeln (nur regulaere Netze)

- **TG-G0 (Kontrolle):** derselbe Code (tg.py, gleiche Klassen, gleiche 13 Richtungen, |k| = 1e-2) auf Finns gefuelltem
  Netz V (Geometrie aus ew.geometrie, J = 1, A1R1). Spanne s_V wie oben.
  - Nach Plan: eingetroffen genau dann, wenn |s_V / 0,06338809562866454 - 1| <= 1e-3 (TT-ISO-1,
    lauf-69/gitter-V-A1R1.json, spanne_J1; dort 13 Sektor-Richtungen x 2 |k|, Extremwerte in [100]).
  - Nach Kartenwortlaut ("6,34 % auf 1e-3 relativ"): |s_V / 0,0634 - 1| <= 1e-3.
  - Der Halbsatz "bzw. der Rayleigh-Quotient die TT-ISO-1-Werte" betrifft den Ersatz und entfaellt. Beschreibend: affine
    Steifigkeit von V (TT-ISO-1: 0,25 je Zelle = Volumen x 1).
- **TG-G1 (Exponent):** nur N mit mindestens 2 regulaeren Netzen; mindestens 3 solche N, sonst "nicht entscheidbar".
  - Nach Plan: Kleinste-Quadrate-Gerade ln(Spanne je Netz) gegen ln N ueber alle regulaeren Netze; eingetroffen genau
    dann, wenn p in [-0,65; -0,35].
  - Nach Kartenwortlaut ("Die Spanne je Netz faellt mit N wie N^p"): Gerade durch ln(mittlere Spanne je N) gegen ln N;
    gleiche Schwelle.
  - Beschreibend: Bootstrap ueber Netze je N (2000 Ziehungen, Saat 17), 68- und 95-%-Bereich.
- **TG-G2 (Mittel ueber Saaten richtungsfrei):** je N mit mindestens 3 regulaeren Netzen: z_d = Mittel(delta_d) /
  Standardfehler(delta_d) ueber Netze, 13 Richtungen.
  - Nach Plan: eingetroffen genau dann, wenn fuer jedes dieser N hoechstens 2 der 13 |z_d| > 2 sind und kein |z_d| > 3,5
    (bei 13 Tests mit 2 Standardfehlern waere "alle innerhalb" auch bei exakter Isotropie in ~45 % der Faelle verfehlt).
  - Nach Kartenwortlaut ("innerhalb von 2 Standardfehlern"): alle |z_d| <= 2 fuer jedes N.
- **TG-G3 (N ~ 8000):**
  - Nach Plan: Extrapolation der Plan-Geraden aus TG-G1 auf N = 8000. "eingetroffen (extrapoliert)", wenn der Wert
    < 1 % ist, sonst "verfehlt (extrapoliert)". Ist TG-G1 nicht entscheidbar, ist TG-G3 es auch nicht.
  - Nach Kartenwortlaut: "nicht entscheidbar", weil kein Netz mit N ~ 8000 im vollen Modell gerechnet wird.
- **Zaehlung (Bedeutungssatz der Karte):** Zahl der Netze, die an allen 16 Punkten genau zwei masselose TT-Moden haben
  (regulaer), dazu je Netz die Gruende fuer "nicht regulaer". Sind nicht alle Netze regulaer, steht das im Bericht vor
  den Urteilen.
- Bricht ein Lauf ab oder fehlt ein Netz, gehen nur vorhandene vollstaendige Netze ein; fehlt die Kontrolle, ist TG-G0
  "nicht entscheidbar".

## 5. Agenten-Vorhersagen (vorab; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Alle vollstaendigen Zufallsnetze sind regulaer (genau 2 masselose TT-Moden, nichts waechst) | 60 % |
| A2 | Mittleres omega^2/k^2 bei N = 256 weicht um mehr als 10 % vom V-Wert (~0,12) ab | 70 % |
| A3 | Mittlere Spanne bei N = 256 zwischen 1 % und 10 % | 50 % |
| A4 | Zusatz Z1: affine Steifigkeit auf jedem Zufallsnetz 1 auf 1e-3 (Spanne < 1e-3) | 75 % |

## 6. Laeufe auf der .69 (kleintest.sh, Spuren cpu3 und cpu4, je 1 Thread, <= 600 s)

- Einmalige Laufketten code/kette-cpu3.sh und code/kette-cpu4.sh, Schlusszeit 03:45:00 UTC (05:45 CEST); jeder Lauf
  ueber kleintest.sh; gestartet von der Laptop-Shell per ssh im Vordergrund der Sitzung (kein Dienst, kein nohup).
  - cpu3: Kontrolle V; N = 32 (Saaten 1-12); N = 64 (1-12); N = 128 (1-6); N = 256 (Saaten 1, 3, ..., 11, je ein Lauf).
  - cpu4: Zusatz Z1 affin (N = 256, 2000, 8000, je Saaten 1, 2); N = 128 (7-12); N = 256 (Saaten 2, 4, ..., 12).
  - Danach tg_auswertung.py --lauf lauf --out lauf/auswertung.json (cpu3).
- **Laufzeitschaetzung** (aus den Rauchzeiten): N = 32 ~1 s, 64 ~5 s, 128 ~35 s, 256 ~250 s je Netz; Kette cpu3
  ~1 900 s, cpu4 ~1 900 s, also ~32 min Wand.
- **Zusatz Z1 (beschreibend):** affine Steifigkeit K = a^+ B a / (k^2 V_Kasten) fuer a_e = n_e^T h n_e e^{i k . m_e},
  h = die zwei TT-Polarisationen (Frobenius-Norm 1, wie tti.py), 13 Richtungen, |k| = 1e-2. Auf V entspricht 0,25 je
  Zelle dem Wert 1.

## 7. Rauchlaeufe vor dem Einfrieren (.69 in UTC)

- r1 (02:30 UTC): Kontrolle und N = 64, Saat 1, mit --rauch (nur Schluessel, Zeiten). r2 (02:31 bis 02:33): N = 128,
  Saat 1, und N = 256, Saat 1, Richtungen 0 und 1, mit --rauch.
- Danach Aenderung ohne Kenntnis von Werten: eps 1e-3 -> 1e-2 und die Klassenschwellen (Abschnitt 3), aus der Ueberlegung
  zu Splittern.
- r3 (02:35 bis 02:37): ganze Kette klein ohne --rauch (Kontrolle, N = 32 und 64 mit Saaten 901-903, N = 128 mit 901-902,
  affin N = 512 und 8000 mit Saat 901, Auswertung zweimal). Gelesen nur Rueckgabewerte, Laufzeiten, Speicher und
  JSON-Schluessel; die Werte nicht.
