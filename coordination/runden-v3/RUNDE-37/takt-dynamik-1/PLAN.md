# TAKT-DYNAMIK-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 47, Finn-Auftrag "Zellen umklappen")

- Start 2026-10-05 08:19:29 CEST (date). Plantext ab 08:42:50 CEST (date), vor jeder Hauptrechnung. Zeitbox 150 min,
  also bis 10:49:29 CEST.
- Grundlage: KARTE.md (TD0 bis TD4, Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] vorab ableitbar (eigene Mathematik), [E] hier gerechnet, [P] Projektdatei, [F] eigene Festlegung,
  [H] Hypothese oder Lesart. Alles ist synthetische Gitterrechnung, keine Messdaten.
- Code: code/td.py (neu). Unveraendert kopiert und importiert: tu.py (TAKT-UMKLAPP-1, sha256 6c5c3a95...), tg.py
  (ec48a258...), tg_auswertung.py (88cbd2ce...), tp.py (419d7da6...), uk.py (f52df743...), ew.py (fa7b6417...), mn.py
  (b36984d3...), alle aus takt-umklapp-1/code. Die Originale sind unveraendert.
- Gewichte nur umkreisbasiert (Takt P = 8 d0^T *1 d0 aus HT0); P1 wird nirgends benutzt.

## 1. Modell und Bewegungsgleichung [F]

- **Netz im Kasten.** Periodische Netze als Kasten mit Bloch-k = 0 (alle Felder periodisch im Kasten). Hintergrund = die
  ungedehnten Lagen (flach). Glas: tg.zufallsnetz(128, s), s = 1 bis 4 (TT-GLAS-1). V_D: tu.reparatur auf tg.netz_V()
  (12 2-3-Zuege je Zelle, TAKT-UMKLAPP-1), dann 2 x 2 x 2-Superzelle (VD2: 80 Ecken, 640 Kanten).
- **Variablen.** Kantenwerte a_e = delta l / l (E Kanten) und Impulse; Hamilton-Netz wie TT-GLAS-1 (EINE-WELT-LOCH-1,
  R1): B = sum_t l D_t l (Regge), A = sum_t A0_t mit A0 = (n_e . n_f)^2 - 1/2 je Tetraeder (J = 1), beide aus tg.ops bei
  k = 0 (reell).
- **Zwangsflaeche.** S = orthonormales Komplement von Bild[M, c, 1_E] (QR, Rang geprueft): M = Eckverschiebungen ohne
  die 3 Translationen, c = -B W (skalare Regel je Ecke) ohne die Konstante, 1_E = gleichmaessige Streckung.
  - Grund fuer 1_E [M, E]: Bei k = 0 ist B 1_E = 0, also hat c nur Rang V - 1, und die gleichmaessige Streckung
    (Kastenvolumen) bleibt in Bild[M, c]-Komplement. Auf ihr ist A0 negativ (regulaeres Tetraeder: 1^T A0 1 = 12 - 18
    < 0), A_red wird indefinit. Rauchtest r1 brach genau daran ab. Bei k != 0 (TT-GLAS-1) entfernt c diese Richtung
    selbst. Entfernen von 1_E heisst: Kastenvolumen fest.
  - Reduziert: x = S^T a, A_red = S^T A S, B_red = S^T B S; H = 1/2 y^T A_red y + 1/2 x^T B_red x;
    dx/dt = A_red y, dy/dt = -B_red x; omega^2 = Eigenwerte von A_red B_red (wie tg.punkt).
  - B_red hat 5 Nullmoden (gleichmaessige spurfreie Dehnungen; flach, nicht Eichung im festen Kasten) [M].
- **Integrator.** Stoermer-Verlet (Kick-Drift-Kick), symplektisch, fester Schritt dt = T / N_T mit
  N_T = ceil(T omega_max / h), omega_max^2 = groesster Eigenwert von A_red B_red des Ausgangsnetzes, T = 2 pi / omega der
  Mode. Hauptlaeufe h = 0,5, Konvergenz in dt mit h = 0,25 (dt halb). Rauchtest Saat 1: omega_max = 27,0,
  omega = 2,49, N_T = 136; Rauchsaat 901: N_T = 188; VD2: N_T = 39.
  - Nach jedem Zug wird omega_max neu gerechnet und omega_max dt ausgewiesen (Verlet stabil fuer < 2).
- **Welle (stehende TT-Mode).** k1 = kleinster reziproker Kastenvektor (Glas: 2 pi / L in x, L = 128^(1/3) = 5,04;
  VD2: erster reziproker Vektor der Superzelle). Ideale TT-Welle a_e = n_e^T h+ n_e cos(k1 . m_e) (m_e Kantenmitte, h+
  wie tg/uk aus k x (0,3; 0,5; 0,7), Frobenius-Norm 1). Die Mode ist die Eigenmode von A_red B_red mit dem groessten
  Energieanteil dieser Welle.
  - Rauchtest: Anteil 0,29 (Saat 1), 0,44 (VD2). Die ideale Welle ist bei Wellenlaenge = Kastenlaenge (etwa 4
    Kantenlaengen, k l ~ 1,5) auf viele Moden verteilt; die Mode ist eine gemischte "TT-artige" Kastenmode. Das wird je
    Netz ausgewiesen und ist eine Grenze der Rechnung.
- **Anfang und Amplitude.** x(0) = 0, dx/dt(0) = omega alpha x_Mode: Bei t = 0 ist das Netz ungedehnt, also Delaunay.
  alpha so, dass der Betrag der TT-Lesung der Mode (4 Komponenten cos/sin x h+/hx, Abschnitt 6) gleich A ist. Das ist die
  Dehnungsamplitude im Sinne von UMKLAPP-1 (F = 1 + a h, |h| = 1). A = 1e-3 und 1e-2, je 10 Perioden.
- **Gedehntes Netz.** l_e(t) = l0_e (1 + a_e(t)), a = S x.

## 2. Energie [F]

- H(x, y) mit den Operatoren der aktuellen Zerlegung, gemessen an 200 Proben je Periode und unmittelbar vor und nach
  jedem Zug (gleicher Zeitpunkt; vor dem Zug alte, danach neue Operatoren). Sprung je Zug: Delta H, Delta V, Delta K,
  relativ zu H0 = H(0).
- Energiedrift: (H(10 T) - H0) / H0 ("Ende") und max_t |H(t) - H0| / H0 ("Maximum"). Die Spruenge an den Zuegen sind Teil
  der Drift.

## 3. Ereignissuche (Arm b) [F]

- Nach jedem Schritt fuer alle Flaechen mu_f aus den gedehnten Laengen: Die Doppelpyramide (Flaeche a b c, Spitzen d, e)
  wird aus ihren 9 Laengen eingebettet (intrinsisch, Cayley-Menger-Konstruktion), mu = (|e - C|^2 - R^2) / R^2 bezueglich
  der Umkugel von a b c d (wie uk.raender). Delaunay verletzt: mu < 0.
- Faellt mu einer nicht gesperrten Flaeche im Schritt unter 0: Bisektion in tau (60 Schritte) mit der geschlossenen Form
  eines Kick-Drift-Kick-Schritts der Laenge tau, x(tau) = x + tau A_red y - tau^2/2 A_red B_red x; die frueheste Flaeche
  zuerst; Zug am rechten Rand (mu knapp < 0); danach der Rest des Schritts mit den neuen Operatoren (Zeitgitter fest).
- Zugtyp in der gedehnten Einbettung: Trifft d-e das Dreieck (drei Volumina abde, bcde, cade gleiches Vorzeichen):
  2-3. Liegt d-e hinter genau einer Kante PQ und hat PQ Grad 3: 3-2 (tu.zug32_vorbereiten, neue Tetraeder PRde, QRde).
  Ausfuehrung auf den Hintergrundlagen nur, wenn dort alle neuen Volumina > 1e-10 des Mittels (tu.zug23_ok,
  tu.zug32_vorbereiten). Sonst "nicht ausgefuehrt", Flaeche gesperrt, bis ihr mu wieder > 0 ist.
- Nach einem Zug werden Flaechen mit mu < 0 (Rest der Linearisierung der neuen Kante, O(A^2)) gesperrt, bis mu > 0
  (gegen Flattern). Ausgewiesen als "nach Zug sofort verletzt".

## 4. Abbildung des Zustands ueber einen Zug [F, H]

- **Lesart H (Hintergrund).** Die Operatoren werden mit der neuen Zerlegung auf den ungedehnten Lagen gebaut; die
  Delaunay-Pruefung und TD0 laufen im gedehnten Netz. Grund: Das Modell ist linear um den flachen Hintergrund, und jede
  Zerlegung fester Lagen ist flach; Operatoren am gedehnten (gekruemmten) Netz waeren ein anderes, nichtlineares Modell.
- **Hauptlesart R (Laengen und Raten stetig):**
  - gemeinsame Kanten: a und da/dt unveraendert;
  - 2-3, neue Kante d-e: a_de = j . a_9, da_de/dt = j . da_9/dt; j = Linearisierung der flachen Laenge |d - e| der
    Doppelpyramide nach ihren 9 Kanten am Hintergrund (Einbettung wie Abschnitt 3, komplexer Schritt);
  - 3-2, wegfallende Kante PQ: a_PQ und da_PQ/dt gestrichen;
  - Uebertragung: x' = S'^T a', dx'/dt = S'^T da'/dt (orthogonale Projektion auf die neue Zwangsflaeche),
    y' = A'_red^-1 dx'/dt.
- **Nebenarm Lesart P (Impulse):** p = S y; 2-3: p' = Null-Fortsetzung (kanonisch zu a' = J a, weil J^T Z = 1); 3-2:
  p' = J^T p mit J = flache Fortsetzung der Kante PQ aus der neuen Doppelpyramide (R d e; P, Q); y' = S'^T p'.
- **Schreibtischpruefung an einem Zug [M]** (J = flache Fortsetzung, Z = Null-Fortsetzung):
  1. S_T(l) = S_T'(l, f(l)) exakt, weil beide Zerlegungen dieselbe flache Doppelpyramide beschreiben. Am flachen
     Hintergrund (Fehlwinkel 0) folgt B_T = J^T B_T' J und B_T' J = Z B_T (die neue Kante hat Fehlwinkel 0, alle anderen
     behalten ihren).
  2. Daraus c'^T J a = c^T a (der Zwang bleibt erfuellt), J M = M' (Eichung geht in Eichung), J 1_E = 1_E'. Die
     Projektion entfernt beim 2-3-Zug nur Anteile in Bild[M', 1_E'] (Teil von ker B'). Also springt V beim 2-3-Zug nicht:
     Delta V = 0 exakt (Kontrolle im Lauf).
  3. 3-2-Zug: V(a) = V'(R a) + 1/2 delta^2 B_PQ,PQ mit delta = a_PQ - j . a_9 = (B a)_PQ / B_PQ,PQ (der nichtflache Anteil,
     also der Fehlwinkel der Welle an PQ). Dazu entfernt die Projektion einen Anteil entlang c'. V springt um O(delta^2).
  4. K: A = sum_t A0_t ist je Tetraeder ungewichtet; ein 2-3-Zug fuegt einen Tetraederbeitrag hinzu, ein 3-2-Zug nimmt
     einen weg. Es gibt keine Identitaet wie in 1., also springt K an jedem Zug, Groesse offen.
  - Kontrollen je Zug im Lauf: l_de (flach aus 9 Kanten) gegen l_de im neuen Netz (Hintergrund); Projektionsrest von a';
    Delta V bei 2-3; gedehnte neue Kante linear gegen nichtlinear flach.
- Ist A'_red nach einem Zug nicht positiv definit, wird mit LU weitergerechnet und das ausgewiesen.

## 5. Zufallsarm (c) [F]

- Zeiten und Typen der ausgefuehrten Zuege aus Arm b (Lesart R, gleiches Netz, gleiches A, gleiches h). An jeder Zeit ein
  zufaelliger zulaessiger Zug desselben Typs im aktuellen Netz: 2-3 gleichverteilt unter uk.kandidaten (konvex, alle
  neuen Volumina >= 1e-3 des mittleren Ausgangsvolumens, neue Kante), 3-2 unter tu.kandidaten32 (Grad 3, konvex, gleiche
  Schwelle). Saat default_rng([4543, N, s, -log10 A]). Abbildung Lesart R. Gibt es keinen zulaessigen Zug, wird er
  ausgelassen und gezaehlt.
- Abbruch, wenn |x| > 1e6 x |x_Mode| oder nicht endlich (wachsende Mode); Zeit ausgewiesen.

## 6. Messgroessen [F]

- Energiedrift (Ende, Maximum); Delta H, Delta V, Delta K je Zug, getrennt nach 2-3 und 3-2.
- Zuege je Periode (ausgefuehrt; 2-3 / 3-2; nicht ausgefuehrt).
- **TD0 (im gedehnten Netz):** am Ereignis Laengen l0 (1 + a) der Region (5 Ecken), neue Kante nichtlinear flach aus
  der gedehnten Doppelpyramide. Je Tetraeder intrinsisch eingebettet, Hodge-Teile wie tu.hodge (umkreisbasiert,
  vorzeichenbehaftet). Gemessen: *1 der neuen bzw. wegfallenden Kante, *2 der wegfallenden (2-3) bzw. neuen (3-2)
  Flaeche, max |Delta *1| der Region, max |Delta P| mit P = 8 d0^T *1 d0; relativ zu max |*1|, max |*2| und max P_vv des
  Ausgangsnetzes. Dieselben Groessen im Hintergrund (das ist der Sprung, den die Dynamik in Lesart H sieht).
- **TT-Amplitude und Phase:** TT-Leser = kleinste Quadrate der Kantenwerte an n^T H n (cos, sin)(k1 . m) nach Abzug der
  Eichrichtungen; Komponenten (cos, sin) x (h+, hx), projiziert auf die TT-Richtung der Mode. Amplitude und Phase aus
  alpha sin(omega t) + beta cos(omega t) ueber die letzte Periode [9 T, 10 T]. Gegen Arm (a): |Amp_b / Amp_a - 1| und
  phi_b - phi_a.
- **Anteil in anderen Moden:** an vollen Perioden, an denen die Zerlegung gleich der Ausgangszerlegung ist,
  Modalenergien bezueglich des Ausgangsnetzes: Anteil TT-Mode, Nullmoden, Rest (letzte solche Periode).
- **Wachsende Moden:** nach jedem Zug und an vollen Perioden Eigenwerte von A_red B_red: wachsend = omega^2 < -1e-12
  max |omega^2| oder komplex (wie tg.klassen); A_red pd; omega_max dt.
- **Zerlegung an vollen Perioden:** Anteil der Ausgangsflaechen, die vorhanden sind.

## 7. Ableitbarkeitsprobe (vor dem Einfrieren)

- **TD0 [M]:** Beim 2-3-Zug bekommt die neue Kante die flache Laenge der Doppelpyramide; die 5 Ecken liegen am Ereignis
  auf einer Kugel, also sind *1 der neuen Kante, *2 der wegfallenden Flaeche und alle Delta *1 bis auf den
  Bisektionsrest null (Karte). **Beim 3-2-Zug gilt das nicht exakt:** Die 10 gedehnten Laengen der 5 Ecken sind bei einer
  Welle nicht flach (Fehlwinkel an PQ von der Ordnung A); die Kugelbedingung gilt nur fuer die Doppelpyramide der
  Ereignisflaeche (9 Laengen, ohne die Kante d-e). *1 von PQ und *2 der neuen Flaeche sind dann von der Ordnung delta,
  nicht 1e-10. TD0 nach Wortlaut ist vorab nur fuer 2-3-Zuege zu erwarten; fuer 3-2-Zuege ist das Verfehlen vorab zu
  erwarten [M], die Groesse ist offen und wird gemessen.
- **TD1:** Delta V(2-3) = 0 [M, 4.2]. Delta K != 0 und Delta V(3-2) != 0 im Allgemeinen [M, 4.3, 4.4], also springt H an
  jedem Zug. Arm (a) hat mit Verlet keinen Trend, nur eine Schwankung O((omega dt)^2) [M]; bei Start mit x(0) = 0 und
  Ende bei t = 10 T ist die Ende-Drift (a) nahe Rundung. TD1 ist damit nicht vorab entschieden, aber nur zu halten, wenn
  sich die Spruenge ueber 10 Perioden fast genau aufheben [H]; nach Wortlaut (Ende-Drift) vorab sehr unwahrscheinlich.
- **TD3:** Die Abbildung ist linear im Zustand; die relative Wirkung eines Zugs haengt nicht von A ab. Die Zahl der Zuege
  waechst wie A (UK1 [P]). Also waechst die Streuung wie A (Exponent nahe 1), nicht wie A^1,5 [M + P]. Der Teil
  "mindestens wie A^1,5" ist vorab nicht zu erwarten; Teil 1 (< 1e-3 bei A = 1e-3) ist offen.
- **TD2:** Wachsende Moden nach Zufallszuegen sind aus HT2/HT3 erwartbar [P] (TAKT-UMKLAPP-1: 10 von 12 Z-Netzen bei
  a = 1e-3 stabil, bei 1 bis 6 Zuegen; hier sind es mehr Zuege). Das Drift-Verhaeltnis ist offen.
- **TD4 [M]:** Bei t = n T ist x in Arm (a) exakt 0 (Sinus-Start), das Netz also ungedehnt und Delaunay = Ausgangszerlegung.
  In Arm (b) bleibt ein Rest aus Streuung und Phasenverschiebung; Abweichungen nur an Flaechen, deren Randabstand mu0
  unter der Restdehnung liegt. Dazu kommen "gesperrte" Flaechen. Kontrolle, Groesse der Restdehnung offen.
- **Zahl der Zuege [P, M]:** nach UK1 grob vorhersagbar (Karte). Rauchtest r1 (Saat 1, A = 1e-3, 1 Periode) zeigte 2
  Ereignisse (Selbstanzeige).
- **V_D [P, M]:** kleinster Randabstand 0,22 (TAKT-UMKLAPP-1) bei Dehnungen <= 1e-2: kein Zug zu erwarten. Rauchtest r3
  (VD2, A = 1e-2): 0 Ereignisse. VD2 ist damit Kontrolle der Ereignissuche (keine falschen Ereignisse); Arm (c) entfaellt
  dort, wenn Arm (b) keinen Zug hat (gleiche Zahl = 0, also identisch mit Arm (a)).

## 8. Urteilsregeln (mechanisch, code/td.py auswertung)

- **TD0** (alle ausgefuehrten Zuege der b-Laeufe in Lesart R): Wortlaut = Plan: max ueber Zuege von (*1 der
  neuen/wegfallenden Kante, *2 der Flaeche, max |Delta P|), relativ, im gedehnten Netz < 1e-10. Getrennt ausgewiesen:
  2-3 und 3-2.
- **TD1** (Glas s1 bis s4, A = 1e-3, h = 0,5): Wortlaut: |Ende-Drift (b)| < 2 |Ende-Drift (a)| in jedem Netz. Plan:
  Maximum-Drift (b) < 2 x Maximum-Drift (a) in jedem Netz.
- **TD2** (Glas s1 bis s4, A = 1e-3): Wortlaut: Median ueber Netze von |Ende-Drift (c)| / |Ende-Drift (a)| >= 10 und
  wachsende Moden in mindestens einem Netz. Plan: Maximum-Drift (c) / Maximum-Drift (a) >= 10 in jedem Netz und wachsende
  Moden in jedem Netz (nach einem Zug oder am Ende).
- **TD3** (Glas s1 bis s4): Wortlaut: Mittel ueber Netze von |Amp_b / Amp_a - 1| bei A = 1e-3 < 1e-3 und
  log10(Mittel bei 1e-2 / Mittel bei 1e-3) >= 1,5. Plan: dasselbe mit dem modalen Anteil ausserhalb der TT-Mode
  (1 - Anteil_TT, letzte volle Periode mit Ausgangszerlegung).
- **TD4** (alle fertigen b-Laeufe, Lesart R, h = 0,5): Wortlaut = Plan: an jeder vollen Periode >= 99 % der
  Ausgangsflaechen vorhanden.
- Fehlen Laeufe, werden die vorhandenen gewertet und die Zahl vermerkt; fehlt eine Seite ganz: "nicht entscheidbar".

## 9. Laeufe auf der .69 (kleintest.sh, Spuren cpu8, cpu9, cpu10, je 1 Thread, <= 600 s je Aufruf)

- Arbeitsordner /home/fmh/fmhc-physics-remote/takt-dynamik-1/ (code/ eingefroren, lauf/). Laufketten code/kette-cpu8.sh,
  code/kette-cpu9.sh, code/kette-cpu10.sh, einmalig per ssh gestartet (kein Dienst, kein Timer). Jeder Lauf hat ein
  Wanduhr-Budget von 500 s je Aufruf; ist er nicht fertig, schreibt er einen Zwischenstand (.zustand.npz/.json) und wird
  sofort neu aufgerufen (hoechstens 4 Abschnitte). Schlusszeit: nach 10:20 CEST (08:20 UTC) startet kein neuer Lauf.
- Name td-<netz>-A<A>-<arm>[-P][-h025].json. Reihenfolge nach Karte: zuerst A = 1e-3 mit (a) und (b), dann (c), dann
  A = 1e-2, dann Nebenarm P und dt-Konvergenz.
  - cpu8: s1 a, b (1e-3); s4 a, b (1e-3); s1 c, s4 c (1e-3); s1 a, b, c (1e-2); VD2 a, b (1e-3, 1e-2); s1 b-P (1e-3);
    s1 a, b h025 (1e-3); s1 b-P (1e-2).
  - cpu9: s2 a, b (1e-3); s2 c (1e-3); s2 a, b, c (1e-2); s4 a, b, c (1e-2); s2 b-P (1e-3); s2 a, b h025; s2 b-P (1e-2).
  - cpu10: s3 a, b (1e-3); s3 c (1e-3); s3 a, b, c (1e-2); s3 b-P, s4 b-P (1e-3); s3, s4 a, b h025; s3, s4 b-P (1e-2).
- Schaetzung aus den Rauchtests: A = 1e-3 je Lauf 5 bis 45 s; A = 1e-2 Arm a ~4 s, Arme b und c ~0,5 s je Zug
  (Neuaufbau der Operatoren), offen; VD2 ~1 s.
- Danach auf cpu8: auswertung (lauf/auswertung.json) und bild (lauf/bild-takt-dynamik.png), dann Pruefsummen.

## 10. Agenten-Vorhersagen (vorab; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| D1 | Delta V bei 2-3-Zuegen <= 1e-10 H0 in allen Laeufen (Kontrolle 4.2) | 85 % |
| D2 | Der Energiesprung je Zug ist im Mittel ueber Zuege vom Betrag > 1e-6 H0 (K-Sprung) | 70 % |
| D3 | TD0 im gedehnten Netz: 2-3-Zuege < 1e-10, 3-2-Zuege > 1e-8 | 65 % |
| D4 | Arm (b) bleibt in allen 4 Glasnetzen ohne wachsende Mode (A = 1e-3 und 1e-2) | 70 % |

## 11. Rauchtests vor diesem Plantext (.69 in UTC)

- r1 (06:40:06, cpu8): Abbruch "A_red nicht positiv definit" (siehe 1.). r1b (06:40:54 bis 06:40:57, cpu8, --rauch,
  Saat 1, A = 1e-3, Arm b, 1 Periode): rc = 0. Gelesen: Schluessel, N_T, dt, omega_max, omega und Anteil der Mode,
  Bauzeit, Zahl der Ereignisse (2).
- Rauchkette (06:41:35 bis 06:45:17, Rauchsaat 901 und VD2), alle rc = 0: r2b (A = 1e-2, b, 110 s Budget, nicht
  fertig: 650 von 1880 Schritten, 214 Ereignisse, also ~0,5 s je Zug), r2c (A = 1e-2, c, 162 Zuege in 110 s), r3 (VD2,
  A = 1e-2, b, --rauch, 1,1 s), r5a (A = 1e-2, a, 3,7 s), r4p (A = 1e-3, b, Lesart P, 42,6 s), r4h und r4h2 (A = 1e-3,
  b, h = 0,25: Abschnitt und Fortsetzung, 15 + 38,5 s, 64 Ereignisse). r2c2 (06:46, Fortsetzung von Arm c mit
  Zufallszustand), r6aw (auswertung) und r6bild (bild) auf dem Rauchordner (06:46:20 bis 06:46:43), rc = 0.
  Nach dem letzten Code-Zusatz (Abbruch bei wachsender Mode, kennzahlen ohne Amplitude bei Abbruch) r7 (06:47:07 bis
  06:47:11, eingefrorener Stand, A = 1e-3, a, --rauch) rc = 0.
- Gelesen: Rueckgabewerte, Laufzeiten, Abschnitte, N_T, Zahl der Ereignisse (r1b: 2 in einer Periode; r2b: 214 in 3,5
  Perioden; r4h: 64 in 10 Perioden; VD2: 0), Mode-Anteil (Saat 1: 0,29; VD2: 0,44), Schluessel der Urteile; keine
  Energien, Amplituden, Spruenge oder Urteile.
- Regeln (Abschnitte 1 bis 8) nach den Rauchtests nur in 1. (Zwangsflaeche mit 1_E, nach r1) geaendert.
