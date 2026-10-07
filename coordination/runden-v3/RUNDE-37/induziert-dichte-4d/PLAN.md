# INDUZIERT-DICHTE-4D: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 08:15:57 CEST (date). Code ab 08:33, Plantext ab
  08:52 CEST (date).
- **Vor diesem Plantext gerechnet:** Rauchlaeufe r1 bis r6 (Abschnitt 11): Laufzeit, Speicher, Netzpruefung,
  Einbettbarkeit und eine blinde Rauschprobe (nur Streuungen, keine Mittelwerte der Messgroesse). Werte der
  Messgroesse (Mittel oder Vorzeichen) habe ich vor dem Einfrieren nicht gesehen.
- **Grundlage:**
  - KARTE.md: IV0 bis IV3 mit Schwellen unveraendert uebernommen (Abschnitt 5).
  - INDUZIERT-1: code/induziert.py unveraendert kopiert (sha256 b3867eac...). Benutzt: gram_E und lokal_K_batch
    (P1 aus der Simplex-Gram-Matrix, Kontrolle K4).
  - INDUZIERT-DICHTE-2D: Verteilungsfunktions-Abbildung, feste Punktzahl, Neuvernetzung, S-Schema, Fit
    y = a + c k^2 je Saat, Urteilslogik (code/dichte2d.py, code/dichte_auswertung.py), hier fuer 4D neu geschrieben
    in code/dichte4d.py und code/auswertung4d.py.
  - INDUZIERT-ZUFALL-2D: log det' mit geerdetem Knoten 0, duenne LU (gleiche splu-Optionen).
- **Kennzeichen:** [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [F] Festlegung dieses
  Plans (von der Karte offen gelassen), [K] Kartenpunkt (vor dem Einfrieren offengelegt), [H] Hypothese,
  [E] hier gerechnet (Rauchlauf).

## 1. Geometrie und Kopplung (gemeinsame Zufallszahlen)

- **Torus [F, K5]:** [0, L1) x [0, Lq)^3 in Koordinaten mit L1 = 24, Lq = 6,5, V = 6591. Metrik g = e^(2 sigma) delta,
  sigma = s cos(k x1), k = 2 pi n/L1 laengs der langen Achse, n = 1 und 2 (abs(k) = 0,262 und 0,524).
- **Zwei Dichten bei festem Volumen [F]:** N = 6591 (rho = 1, Hauptdichte) und N = 3296 (rho = 0,5). Mittlerer
  Koordinatenabstand h0 = (V/N)^(1/4) = 1,000 bzw. 1,189; abs(k) h0 = 0,26 und 0,52 bzw. 0,31 und 0,62.
- **Grundpunkte:** N gleichverteilte Punkte, Saat numpy default_rng([20261004, 4, N, saat]).
- **Abbildung psi_s [M]:** wie INDUZIERT-DICHTE-2D, aber mit Dichte e^(4 sigma):
  - Phase phi = k x1 mod 2 pi; gesucht phi' mit Phi_s(phi') = phi,
    Phi_s(t) = (1/I0(4s)) int_0^t e^(4 s cos u) du = t + sum_m 2 I_m(4s)/(m I0(4s)) sin(m t) (30 Glieder).
  - Newton (Schritt auf 0,5 begrenzt) bis abs(Schritt) < 1e-14; x1' = x1 + (phi' - phi)/k, Querkoordinaten fest.
  - Die Bildpunkte sind exakt unabhaengig mit Koordinatendichte e^(4 sigma)/I0(4s) verteilt, also gleichverteilt im
    physikalischen Volumen V_g = V I0(4s). Jede Differenz in s ist damit erwartungstreu.
- **Punktzahl [K4]:** N bleibt fest (Binomialprozess), wie in 2D; sonst keine gemeinsamen Zufallszahlen.

## 2. Netz und Pruefungen

- **Netz [Karte]:** Delaunay der Punkte in Koordinaten (Qhull, scipy-Vorgaben) mit periodischem Saum:
  - Kopien aus den 80 Nachbarzellen nur, wenn sie hoechstens W0 = 2,5 lokale mittlere Abstaende vor dem
    Grundbereich liegen. Lokaler Abstand h(x) = h0 e^(-sigma(x)) I0(4s)^(1/4), so dass auch duenne Bereiche
    genug Saum haben.
  - Behalten werden die Simplizes mit Schwerpunkt im Grundbereich (genau ein Bild je Torus-Simplex, kanonisch);
    Ecken modulo N, Eckkoordinaten unverfaltet (Kantenvektoren direkt), Orientierung positiv.
- **Pruefung je Netz (Tor a):**
  - alle 5 Ecken verschieden, alle N Knoten benutzt, Orientierung > 0
  - Summe der Koordinatenvolumina = V auf 1e-9
  - jede Tetraeder-Facette in genau zwei Simplizes; Euler-Charakteristik V - E + F - T + S = 0
  - Teilsimplizes mit Periodenversatz gezaehlt (Versatz der Ecken relativ, Werte -1..1), so dass auch Kanten
    laenger als Lq/2 richtig gezaehlt werden
  - Saum: Die Umkugel jedes behaltenen Simplex liegt im Saum (Marge > 0, Saum am Kugelmittelpunkt mit
    e^(-abs(s) k R) abgeschwaecht). Dann liegt kein fehlender Punkt in einer Umkugel; mit Facettenpaarung und
    Volumen ist das Netz vollstaendig und Delaunay.
- **Kontrolle K2:** gleiche Simplexmenge mit Saum 2,5 und 4,0 (Grundnetz und Bildnetze bei +-S) und leere Umkugeln
  per kd-Baum (kein Punkt innerhalb R (1 - 1e-9)).

## 3. Laengenregeln und P1-Steifigkeit [K1]

- **P1 [Karte]:** K_T = V P^T G^-1 P aus der Gram-Matrix G der 10 Kantenlaengenquadrate, V = sqrt(det G)/24 (Code
  wie induziert.lokal_K_batch, m^2 = 0); Kontrolle K4: gleich auf <= 1e-9 relativ.
- **Geodaetische Laengen (geo) [M]:** log l = log abs(d) + sigma(m) + [b + a^2 - (abs(d)^2 abs(grad sigma)^2 - a^2)]/24
  mit a = d.grad sigma(m), b = (d.grad)^2 sigma(m), m Kantenmitte (4D-Fassung der 2D-Formel; Kontrolle K3 gegen
  numerisch minimierte Weglaenge).
- **Befund im Rauchlauf [E]: geodaetische Laengen sind in 4D fuer Splitter nicht einbettbar.**
  - Splitter: Simplizes mit kleinem Volumen bei normalen Seitenflaechen. Im Grundnetz gilt fuer
    eps = V/V_regulaer etwa P(eps < x) = 5 x^2 (r3, r4: 47 bzw. 89 Simplizes unter 0,01, kleinstes eps 9e-4).
  - Die P1-Steifigkeit eines Splitters waechst wie 1/eps. Schon kleine, nicht konforme Laengenaenderungen machen
    G indefinit.
  - Gemessen (nicht einbettbar, von 9e4 bis 1,7e5 Simplizes): festes Netz 1 bis 8 bei s = 0,001 bis 0,01;
    200 bis 850 bei s = 0,25 (abs(k) h0 = 0,26 bis 0,52); Bildnetze aehnlich; bei S = 0,5 und abs(k) h0 = 0,63 bis
    0,94 rund 2 bis 4 %.
  - Damit ist die Kartenregel "Kantenlaengen physikalisch" bei jedem brauchbaren S nicht fuer alle Simplizes
    definiert.
- **Berichtigung [K1]:**
  - **Urteil mit der Schwerpunktregel (sp):** alle zehn Kanten eines Simplex mit e^(sigma(c_T)) am
    Koordinatenschwerpunkt c_T skaliert. Der Simplex ist aehnlich zum Koordinatensimplex, also immer einbettbar.
    Es gilt K_T = e^(2 sigma(c_T)) K_T^koord: die Standard-FEM-Diskretisierung von -div(sqrt(g) g^-1 grad) =
    -div(e^(2 sigma) grad) mit stueckweise konstantem Koeffizienten [M]. Physikalisch bis auf die Aenderung von
    sigma innerhalb eines Simplex.
  - **Kartenwortlaut mit geo+:** geodaetische Laengen; nur die nicht einbettbaren Simplizes erhalten die
    Schwerpunktregel (Zahl je Netz protokolliert). Auf denselben Netzen und mit denselben Urteilsregeln gerechnet
    und mitberichtet.
  - Bei s = 0 stimmen beide Regeln ueberein (Koordinatenlaengen); Gamma(0) ist fuer beide gleich.

## 4. Materie und log det'

- Gamma = 1/2 log det' K, det' K = N det K_(0) (Knoten 0 geerdet), wie INDUZIERT-ZUFALL-2D.
- splu mit MMD_AT_PLUS_A, SymmetricMode, diag_pivot_thresh 0, ohne Equilibrierung; Summe log U_ii (math.fsum).
- Je LU: U_ii > 0, perm_r = perm_c, alle Simplizes einbettbar (lu_ok). Zeilensumme von K protokolliert.
- Kontrolle K4: LU gegen dichte slogdet(K + 1 1^T/N) und Eigenwerte, N = 1500, s = 0 und +-S, beide Regeln.
- Fill-in gemessen (r1, r2, isotrop): nnz(LU) 2,1e6 / 1,2e7 / 4,5e7 bei N = 2000 / 5000 / 10000, LU 0,5 / 5,9 / 40 s.
  Auf dem gestreckten Torus N = 3296: 0,6 s je LU (r6). Exakte LU genuegt, keine stochastische Naeherung.

## 5. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IV0 | Kontrolle: Die Variante "festes Netz" gibt eine positive konforme Steifigkeit (Vorzeichen wie INDUZIERT-1) | 70 % |
| IV1 | [H] Mit Streuung nach Volumen und Neuvernetzung ist die konforme Steifigkeit negativ (Einstein-Vorzeichen), Steigung + 2 SE < 0 | 50 % |
| IV2 | [H] Ihr Betrag waechst mit der Dichte etwa wie rho^(1/2): Exponent zwischen zwei Dichten 0,5 +- 0,2 | 35 % |
| IV3 | Kein Volumenterm: k^0-Glied innerhalb 3 SE mit null vertraeglich | 60 % |

## 6. Messgroesse und Urteilsregeln (mechanisch durch code/auswertung4d.py nach lauf-69/auswertung.json)

- **Differenzenschema [F, K5]:** je Saat, n und Variante y = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/(S^2 V), S = 0,25.
  - Dichte-Variante: Gamma(+-S) jeweils auf dem eigenen Delaunay-Netz der Bildpunkte psi_(+-S)(z).
  - Festes Netz: dasselbe Grundnetz (Delaunay von z), nur die Laengen bei +-S. Gleiches S-Schema wie die
    Dichte-Variante (vergleichbar; Richardson mit kleinem h waere fuer geo+ an fast entarteten Splittern singulaer).
  - Gamma(0) ist das Grundnetz mit Koordinatenlaengen, gleich fuer beide Varianten und Regeln.
- **Fit [Karte, wie 2D]:** je Saat y(n) = a + c k_n^2 ueber n = 1, 2 (zwei Punkte, exakt bestimmt). Saatmittel und
  SE = Std(je Saat, ddof 1)/sqrt(M). c ist die konforme Steifigkeit je Volumen und k^2, a das k^0-Glied.
- **Globales Glied [M, K2]:** Bei fester Punktzahl waechst das physikalische Volumen auf V I0(4S). K ist in 4D homogen
  vom Grad 2 in den Laengen, also gilt exakt Gamma(lambda l) = Gamma(l) + (N - 1) log lambda. Daraus folgt in y das
  k-unabhaengige Glied dy = (N - 1) log I0(4S)/(2 S^2 V) = 1,887 rho (N - 1)/N bei S = 0,25. Berichtigtes k^0-Glied:
  a_korr = a - dy. Auf dem festen Netz gibt es kein solches Glied (dort ist Gamma bei konstantem sigma exakt linear).
- **Tor:**
  - (a) Je Saat: alle Netze gueltig (Abschnitt 2), alle LU ok (beide Regeln), Newton-Residuum <= 1e-12. Saaten mit
    einem Fehler werden ausgeschlossen und gezaehlt [F]. Sind es mehr als 5 % einer Dichte oder bleiben weniger als
    8 Saaten, sind die Urteile dieser Dichte "nicht auswertbar".
  - (b) Kontrollen fuer das Urteil (Regel sp): K1 Residuum <= 1e-12 und alle Momenten-z-Werte <= 4; K2 gleich und
    leere Umkugeln und gueltig; K4 <= 1e-9 relativ, P1 gegen INDUZIERT-1 <= 1e-9.
  - (c) Fuer den Kartenwortlaut (geo+) zusaetzlich K3: Laengenformel gegen numerische Geodaete <= 1e-3 relativ.
- **IV0 [F: Rauschregel]:** festes Netz, N = 6591, Regel sp: eingetroffen, wenn c - 2 SE > 0; nicht eingetroffen, wenn
  c + 2 SE < 0; sonst nicht auswertbar. Mitberichtet: geo+ und N = 3296 mit derselben Regel.
- **IV1 [Karte: Schwelle; F: Rauschregel fuer "nicht eingetroffen"]:** Dichte-Variante, N = 6591, Regel sp:
  eingetroffen, wenn c + 2 SE < 0; nicht eingetroffen, wenn c - 2 SE > 0; sonst nicht auswertbar.
  - Kartenwortlaut zweiwertig mitberichtet: eingetroffen genau dann, wenn c + 2 SE < 0, sonst nicht eingetroffen.
  - Mitberichtet: geo+, N = 3296, noetige Saatzahl fuer abs(c) = 2 SE.
- **IV2 [Karte: Band; F: Rauschregel]:** p = ln(c_6591/c_3296)/ln 2,
  SE(p) = sqrt((SE_6591/c_6591)^2 + (SE_3296/c_3296)^2)/ln 2, Regel sp.
  - Nicht auswertbar, wenn eines der beiden c nicht mehr als 2 SE von 0 liegt.
  - Nicht eingetroffen, wenn beide getrennt sind und verschiedenes Vorzeichen haben.
  - Eingetroffen, wenn p in [0,3; 0,7] und SE(p) <= 0,2 (SE hoechstens die Bandhalbbreite, wie ID1 in 2D).
  - Nicht eingetroffen, wenn der Abstand von p zum Band > 2 SE(p); sonst nicht auswertbar.
  - Mitberichtet: geo+ und dieselbe Groesse fuer das feste Netz (beschreibend).
- **IV3 [Karte: 3 SE; K2: Berichtigung]:** Regel sp, N = 6591: eingetroffen, wenn abs(a_korr) <= 3 SE(a), sonst nicht
  eingetroffen. Kartenwortlaut (roh, a ohne Abzug) mit derselben Regel mitberichtet; er ist durch dy vorab
  entschieden (Abschnitt 10).

## 7. Kontrollen

- K1 (psi), K2 (Saum, leere Umkugeln), K3 (Geodaete), K4 (LU, P1), wie oben.
- **K5 (beschreibend):** Kippen gegen s ohne LU (s = 1e-4 bis S, n = 1 und 2): neue 4-Simplizes gegenueber s = 0 und
  nicht einbettbare Simplizes mit geodaetischen Laengen (Bildnetz und festes Netz).
- **K6 (beschreibend):** Gamma(s) eines Bildnetzes und des festen Netzes (Regel sp) auf feinem s-Gitter, N = 1500:
  Spruenge an Kippstellen. [M] In 4D ist die P1-Steifigkeit beim Kippen nicht stetig (anders als der Kotangens-
  Laplace in 2D); Beispiel Doppelpyramide in 3D: Energie 0,866 gegen 3,464 fuer die beiden Delaunay-Zerlegungen
  derselben fuenf Punkte auf einer Kugel.
- **Laufend:** Netz-, LU- und Newton-Pruefungen in jedem Netz (Tor a); Zahl ersetzter Simplizes (geo+), Anteil neuer
  Simplizes, Saum-Marge.

## 8. Laeufe

- .69, /home/fmh/fmhc-physics-remote/runde38-induziert-4d/ (code/, rauch/, lauf/), nur ueber kleintest.sh, Spuren cpu3
  und cpu4, je Spur nacheinander, je ssh-Aufruf ein Starter. Jeder Lauf schreibt nach jeder Saat.
- Hauptlaeufe (alle mit Dichte-Variante und festem Netz auf demselben Grundnetz, beide Regeln, S = 0,25, n = 1, 2):
  - **cpu3:** kontrolle-a (N = 6591; K1, K2, K3, K4), dann dichte N = 6591 mit je 2 Saaten je Start:
    Saaten 0 bis 15 (8 Starts).
  - **cpu4:** kontrolle-b (N = 3296; K2, K5, K6), dann dichte N = 3296 mit je 4 Saaten je Start: Saaten 0 bis 11
    (3 Starts); danach dichte N = 6591 mit je 2 Saaten je Start ab Saat 100 (100 bis 109, 5 Starts), soweit die
    Zeitbox reicht (letzter Start spaetestens 10:05 CEST).
  - Ausgabe lauf/kontrolle-a.json, lauf/kontrolle-b.json, lauf/dichte-N<N>-s<saat0>.json.
- **Laufzeit (gemessen, r5 und r6):** N = 6591: 22 s Qhull, 3,5 s je LU, 42 s je Bildnetz, 243 s je Saat (mit festem
  Netz); N = 3296: 13 s Qhull, 0,65 s je LU, 20 s je Bildnetz, etwa 110 s je Saat bei einem S. Speicher <= 0,8 GB.
- **Saatzahl [F, K7]:** aus der Laufzeit (Zeitbox) bestimmt; die Hauptdichte N = 6591 traegt IV0, IV1 und IV3 und
  bekommt den groessten Teil (bis 26 Saaten), N = 3296 nur fuer IV2 (12 Saaten). Erwartete Genauigkeit aus der
  blinden Rauschprobe (Abschnitt 11, je zwei Saaten, grob): Std(y) je Saat 0,004 bis 0,05, also SE(c) etwa 0,02 bis
  0,05 bei N = 6591 und etwa 0,02 bei N = 3296. Die Werte von c sind unbekannt; "nicht auswertbar" ist ein
  moeglicher Ausgang.
- **Abbruch:** Nicht fertige Saaten fehlen; geurteilt wird mit den fertigen (offengelegt), Mindestzahl 8 je Dichte.
- Danach: auswertung4d.py lauf lauf/auswertung.json.

## 9. Agenten-Vorhersagen (nach den Rauchlaeufen, vor den Hauptlaeufen; ohne Kenntnis der Messwerte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor besteht (hoechstens 5 % Saaten ausgeschlossen) | 85 % |
| A2 | IV3 berichtigt eingetroffen: abs(a_korr) <= 3 SE | 55 % |
| A3 | Die Regeln sp und geo+ geben dasselbe Vorzeichen von c in beiden Varianten | 70 % |
| A4 | IV1 eingetroffen | 40 % |
| A5 | IV0 eingetroffen | 60 % |
| A6 | IV2 nicht auswertbar (Rauschen) | 50 % |

## 10. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Laengenregel:** Abschnitt 3. Geodaetische Laengen sind fuer Splitter nicht einbettbar; Urteil mit der
  Schwerpunktregel, Kartenwortlaut mit geo+ (Ersatz nur der nicht einbettbaren Simplizes) auf denselben Netzen.
- **[K2] Volumenterm:** Bei fester Punktzahl enthaelt das k^0-Glied exakt dy = (N - 1) log I0(4S)/(2 S^2 V)
  (1,887 bei rho = 1, S = 0,25), allein aus der Homogenitaet von K. Es ist kein Merkmal der induzierten Wirkung,
  sondern der Konvention "N fest, Gesamtvolumen waechst". Nach Kartenwortlaut ist IV3 deshalb vorab entschieden
  ("nicht eingetroffen", vorab ableitbar). Berichtigt wird a_korr = a - dy geurteilt: Gleichwertig ist das
  Festhalten des physikalischen Gesamtvolumens (sigma minus 1/4 log I0(4S)), also "Zahl = Volumen" exakt.
- **[K3] IV2 und Homogenitaet [M]:** Weil K homogen vom Grad 2 ist, gilt exakt c(rho, k) = rho^(1/2) c_1(k rho^(-1/4))
  (c_1 bei Dichte 1). Der Exponent 0,5 folgt damit fuer jedes lokale k^2-Glied, sobald c im Fenster nicht von k
  abhaengt. IV2 prueft also, ob die Steifigkeit im Fenster ein reines k^2-Glied ist, nicht Sakharov im engeren Sinn.
  Das gilt fuer beide Varianten. Geurteilt wird nach Kartenwortlaut.
- **[K4] Feste Punktzahl statt Poisson:** wie INDUZIERT-DICHTE-2D (gemeinsame Zufallszahlen).
- **[K5] S, Torusform und Fenster:**
  - S = 0,25 statt 0,5: Bei S = 0,5 waren 2 bis 4 % der Simplizes nicht einbettbar (r1, r2). Die Koordinatendichte
    schwankt mit e^(8S) (55-fach bei 0,5, 7,4-fach bei 0,25); der Querschnitt im duennen Bereich hat bei 0,25 noch
    etwa 6,5/1,36 = 4,8 lokale Abstaende (rho = 1).
  - Gestreckter Torus mit k laengs der langen Achse: Ein isotroper Torus mit N = 6591 haette L = 9 und
    abs(k) h0 >= 0,7; das ist kein Langwellenbereich. Die Querrichtungen sind kurz (6,5); Endlichkeitseffekte dort
    sind nicht gemessen [H: klein gegen die UV-dominierten lokalen Glieder].
  - Fenster n = 1, 2 (abs(k) h0 = 0,26 bis 0,62); n = 3 waere 0,79 bzw. 0,93.
  - [M, H] Nichtlinearitaet in S: Fuer eine reine Einstein-Wirkung mit dichtegebundenem Abschneiden gaebe das
    S-Schema D(S)/Gamma''(0) = (I1(2S)/S) I0(4S)^(-1/2) = 0,92 bei S = 0,25 (0,75 bei S = 0,5). Das aendert weder das
    Vorzeichen (IV0, IV1) noch den Exponenten (IV2, gleicher Faktor bei beiden Dichten).
- **[K6] Delaunay in Koordinaten:** Kartenwortlaut, wie 2D. Bis zur ersten Ordnung in abs(grad sigma) l ist das
  physikalische Delaunay-Netz dasselbe (die Abweichung der Metrik ist dann eine Moebius-Abbildung, die leere
  Kugeln erhaelt) [M].
- **[K7] Saaten und Rauschen:** Die Saatzahl folgt aus der Laufzeit (Abschnitt 11), nicht aus Werten der
  Messgroesse. Die blinde Rauschprobe gab nur Standardabweichungen.
- Kartenfehler, die ein Urteil nach Kartenwortlaut veraendern: [K1] (Regel nicht ueberall definiert) und [K2]
  (IV3 vorab entschieden). Beide Lesarten werden berichtet.

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC; Rauchsaaten >= 900)

- **netztest-r1** (06:35:25 bis 06:36:52, cpu3, rc 0), isotrop N = 2000 und 5000 (Dichte 1), S = 0,5, n = 1:
  - Grundnetze gueltig: 31,6 bzw. 31,7 Simplizes je Knoten, mittlerer Grad 37,6, Euler 0, Facetten gepaart,
    Saum-Marge 0,75 bzw. 0,61, groesster Umkugelradius 1,33 bzw. 1,37.
  - Qhull 6,9 s (19 000 Punkte) und 13,0 s (32 000 Punkte). LU MMD 0,5 s und 5,9 s, COLAMD 1,0 und 12,9 s.
  - Bildnetze bei S = 0,5 (abs(k) h0 = 0,94 bzw. 0,75): ungueltig (Saum-Marge negativ, Kante > L/2) und 2 393 bis
    4 208 Simplizes mit geodaetischen Laengen nicht einbettbar (2,6 bis 3,8 %).
- **netztest-r2** (06:35:27 bis 06:37:22, cpu4, rc 0), isotrop N = 10 000: Qhull 21 s (50 000 Punkte), LU 40 s,
  nnz(LU) 4,5e7, 1,4 GB; Bildnetze bei S = 0,5: 6 075 bzw. 6 153 nicht einbettbar (1,9 %).
- **einbettung-r3** (06:40:11 bis 06:46:34, cpu3, rc 0), Torus 32 x 4,5^3, N = 2916, n = 1 und 2: Splitter im
  Grundnetz und nicht einbettbare Simplizes gegen s (Abschnitt 3). Neue Simplizes gegenueber s = 0: 1 % bei
  s = 0,001, 9 % bei 0,01, 36 % bei 0,05, 66 % bei 0,15, 82 % bei 0,3, fast gleich fuer beide k.
- **einbettung-r4** (06:40:13 bis 06:46:26, cpu4, rc 0), Torus 24 x 6^3, N = 5184: ebenso; bei s = 0,25 und n = 1
  (abs(k) h0 = 0,26) 205/226 (fest) und 332/276 (Bild) nicht einbettbar, bei n = 2 825/849 und 1 129/1 143.
- **rausch-r5** (ab 06:47:04, cpu3), N = 6591, Saaten 950 bis 952, S = 0,25, n = 1, 2, blind: nur Laufzeiten und
  Streuungen gespeichert. Saat 950 in 243 s; Bildnetze gueltig, alle LU ok; geo+ ersetzt 367 bis 1 349 Simplizes je
  Bildnetz (0,2 bis 0,6 %), 253 bis 1 017 im festen Netz.
- **rausch-r6** (ab 06:47:07, cpu4), N = 3296, Saaten 950 bis 953, S = 0,125 und 0,25, blind. Nach zwei Saaten
  (Standardabweichung aus je zwei Werten, also grob):
  - Dichte-Variante, Regel sp: Std(y) 0,015 (n = 1) und 0,0018 (n = 2) bei S = 0,25; 0,018 und 0,0059 bei
    S = 0,125.
  - Festes Netz, Regel sp: Std(y) 3,5e-5 und 9,5e-5.
  - Regel geo+: Dichte 0,015 und 0,0085; festes Netz 0,005 und 0,009 (S = 0,25), also im festen Netz rund
    100-mal mehr als sp (fast entartete Splitter).
  - Daraus: Std von c je Saat etwa 0,07 (N = 3296); S = 0,25 rauscht weniger als 0,125.
  - rausch-r5 nach zwei Saaten (N = 6591, S = 0,25): Dichte sp 0,0039 (n = 1) und 0,047 (n = 2); festes Netz sp
    6e-6 und 2,1e-4; geo+ Dichte 0,0092 und 0,071, festes Netz 0,0013 und 0,015. Die Streuung schwankt stark
    zwischen k und Dichten (je ein Freiheitsgrad).
- **Codeprobe p1** (06:55:03 bis 07:00:16, cpu3 und cpu4): Dichte-Variante nicht blind auf kleinem Torus
  12 x 4,4^3 (N = 1022 und 511, Saaten 990 und 991), Kontrolle mit allen Teilen, Auswertung. Nur auf Fehler,
  Rueckgabewert und Struktur geprueft; Messwerte und Urteile der Probe nicht gelesen.
  - probe-a, probe-b rc 0. Kontrollprobe: K1 Residuum 8,9e-16, z <= 1,13; K2 gleiche Simplexmengen und leere
    Umkugeln, im duennen Probetorus aber Saum-Marge -0,26 bei n = 2, +S (das Tor ist dort zu streng, die Menge war
    gleich der mit Saum 4,0); K3 8,1e-5; K4 <= 3,2e-12 absolut, P1 gegen INDUZIERT-1 3,7e-16; K5 ohne Fehler.
  - Auswertung rc 0; dabei je eine Saat am Saumtor ausgeschlossen, so dass die Analysepfade leer blieben.
  - Deshalb Testkopie rauch/probe2 mit per jq auf 1 gesetzter Saum-Marge (nur zum Codetest, kein Lauf), Auswertung
    rc 0, alle Pfade (beide Dichten, beide Varianten, beide Regeln, IV0 bis IV3, Bilder) durchlaufen.
- **Zeitfolge der Festlegungen:**
  - Schwellen der Karte unveraendert. Regel sp, S = 0,25, Torusform, n = 1, 2 und die Rauschregeln habe ich nach
    r1 bis r4 festgelegt (nur Netz-, Einbettungs- und Zeitdaten).
  - Die Saatzahlen folgen aus den Laufzeiten von r5 und r6; die blinden Streuungen haben nur die Erwartung zur
    Genauigkeit (Abschnitt 8) bestimmt.
  - Vor dem Einfrieren keine Mittelwerte oder Vorzeichen der Messgroesse gesehen.
