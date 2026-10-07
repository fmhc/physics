# INDUZIERT-DICHTE-4D: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 08:15:57 CEST; Code ab 08:33, Plantext ab 08:52 CEST.
  - Rauchlaeufe r1 bis r6 und Codeprobe p1: 06:35:25 bis 07:00:16 UTC (PLAN Abschnitt 11).
  - Eingefroren 09:00:39 CEST: PLAN.md.eingefroren-20261004-090039, Code-Kopien *.eingefroren-20261004-090039,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 07:00:48 bis 07:59:49 UTC (18 Starts: 2 Kontrollen, 16 Dichte-Laeufe), Auswertung 07:59:57 bis
    08:00:12 UTC, alle rc = 0. Text ab 10:01 CEST.
- Nach dem Einfrieren ist der Code unveraendert; die Pruefsummen auf der .69 und lokal stimmen ueberein
  (EINGEFROREN-SHA256.txt; lauf-69/PRUEFSUMMEN.txt lokal nachgeprueft).
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu3 und cpu4).
  Gerechnet ist euklidisch, eine Schleife, ein freies masseloses Skalarfeld (P1). Synthetisch, keine Messdaten.
- **Kennzeichen:** [S] an der Quelle gelesen (hier keine Quelle abgerufen), [L] Literatur aus dem Gedaechtnis,
  [L?] unsicher, [M] eigene Mathematik, [E] hier gerechnet, [F] Festlegung im Plan, [K] Kartenpunkt, [H] Hypothese.
- **Konvention:**
  - Gamma = 1/2 log det' K, K = P1-Steifigkeit (Gram-Matrix-Formel aus INDUZIERT-1) auf einem 4D-Delaunay-Netz.
  - Metrik g = e^(2 sigma) delta auf dem Torus 24 x 6,5^3 (V = 6591), sigma = s cos(k x1), abs(k) = 0,262 und 0,524.
  - Messgroesse y = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/(S^2 V) mit S = 0,25; je Saat y = a + c k^2 ueber die
    beiden k. c ist die konforme Steifigkeit je Volumen und k^2: c > 0 heisst steif (Vorzeichen INDUZIERT-1),
    c < 0 heisst Einstein-Vorzeichen (induzierte Gravitation mit positivem G).
  - **Dichte-Variante:** dieselben Grundpunkte, laengs k so verschoben, dass sie im physikalischen Volumen
    gleichverteilt sind (Dichte e^(4 sigma) in Koordinaten), dann neu vernetzt.
  - **Festes Netz:** Grundpunkte und ihr Netz bleiben, nur die Kantenlaengen aendern sich.
  - **Regel sp (Urteil, [K1]):** alle Kanten eines Simplex mit e^(sigma(Schwerpunkt)); **Regel geo+
    (Kartenwortlaut):** geodaetische Kantenlaengen, nur nicht einbettbare Simplizes mit sp.
  - Zwei Dichten bei festem Volumen: rho = 1 (N = 6591, Hauptdichte) und rho = 0,5 (N = 3296).

## 1. Ergebnis zuerst

1. **"Zahl = Volumen" gibt in 4D nicht das Einstein-Vorzeichen [E].** Mit Streuung nach Volumen und Neuvernetzung ist
   die konforme Steifigkeit bei rho = 1 **c = +0,111 +- 0,045** (25 Saaten, Regel sp), also positiv mit 2,5 SE.
   Bei rho = 0,5 ist sie -0,017 +- 0,045 (12 Saaten), mit null vertraeglich. Einstein waere c < 0.
2. **Die Streuung nach Volumen senkt die Steifigkeit, dreht sie aber nicht um [E].** Auf demselben Grundnetz gibt das
   feste Netz +0,1706 +- 0,0002 (rho = 1) und +0,1179 +- 0,0003 (rho = 0,5). Die Dichte-Variante liegt um
   0,060 +- 0,045 (1,3 SE) bzw. 0,135 +- 0,045 (3,0 SE) darunter. In 2D hatte derselbe Schritt +0,159 auf Polyakovs
   -0,013 gebracht.
3. **Ein Volumenterm tritt nicht auf [E, M].** Das k^0-Glied ist genau das exakt bekannte Glied der festen Punktzahl
   (dy = 1,887): roh 1,882 +- 0,019, berichtigt -0,005 +- 0,019 (rho = 1) bzw. +0,014 +- 0,021 (rho = 0,5).
4. **Urteile (Regel sp):** IV0 eingetroffen, aber mit sp vorab entschieden (Konvexitaet, Abschnitt 6 Punkt 5);
   IV1 nicht eingetroffen; IV2 nicht auswertbar; IV3 eingetroffen (berichtigt). Nach Kartenwortlaut (geodaetische
   Laengen geo+): IV0, IV1 und IV3 nicht eingetroffen, IV2 nicht auswertbar; IV3 roh vorab nicht eingetroffen.
5. **Vorbehalte:** Das Rauschen ist gross (Std je Saat 0,22), weil sich in 4D bei S = 0,25 rund 79 % der Simplizes
   neu bilden und die P1-Steifigkeit beim Kippen springt. Die Laengenregel aendert die Zahl stark (geo+: +0,371;
   von Splittern beherrscht). Ausgeloest ist der vorab festgelegte Zweig "IV1 verfehlt: In 4D reicht
   Volumen-Zaehlung allein nicht", als 2,5-SE-Befund bei einer Dichte.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/auswertung4d.py; Werte in lauf-69/auswertung.json (Vermerke per jq
nachgetragen; Urteile und Werte gleich lauf-69/auswertung.maschine.json).
Tor bestanden (Abschnitt 4). Saaten: N = 6591 26 gerechnet, 1 ausgeschlossen (Saat 105, Saum-Marge -0,015 in einem
Bildnetz), 25 ausgewertet; N = 3296 12 von 12.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (sp) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| IV0 | festes Netz positiv (wie INDUZIERT-1) | 70 % | **eingetroffen** (vorab entschieden, Abschnitt 6) | geo+: **nicht eingetroffen** | sp: c = +0,1706 +- 0,0002, rho = 0,5: +0,1179 +- 0,0003. geo+: c = -0,061 +- 0,008 (rho = 0,5: +0,024 +- 0,012), dazu ein k^0-Glied -0,057 +- 0,002, das es auf einem festen Netz nicht geben duerfte (Splitter) |
| IV1 | [H] Dichte-Variante negativ, Steigung + 2 SE < 0 | 50 % | **nicht eingetroffen** | zweiwertig (sp): nicht eingetroffen; geo+: **nicht eingetroffen** | sp: c = +0,111 +- 0,045, c - 2 SE = +0,021 > 0. rho = 0,5: -0,017 +- 0,045 (nicht auswertbar). geo+: +0,371 +- 0,049 (rho = 0,5: +0,104 +- 0,039) |
| IV2 | [H] Betrag ~ rho^(1/2), Exponent 0,5 +- 0,2 | 35 % | **nicht auswertbar** | geo+: **nicht auswertbar** | sp: c(rho = 0,5) nicht von 0 getrennt. geo+: p = 1,84 +- 0,57 (Abstand zum Band 1,14, knapp unter 2 SE = 1,15). Festes Netz sp (beschreibend): p = 0,534 +- 0,004 |
| IV3 | kein Volumenterm, k^0-Glied innerhalb 3 SE von 0 | 60 % | **eingetroffen** (berichtigt [K2]) | roh: **nicht eingetroffen** (vorab, 99 SE); geo+ berichtigt: **nicht eingetroffen** (3,2 SE) | sp: a_korr = -0,005 +- 0,019 (0,27 SE); rho = 0,5: +0,014 +- 0,021. Roh a = 1,882 +- 0,019 gegen dy = 1,887. geo+: a_korr = +0,062 +- 0,019 |

- **Bedeutung, wie vorab auf der Karte festgelegt:** Ausgeloest ist "IV1 verfehlt: In 4D reicht Volumen-Zaehlung
  allein nicht; dann zaehlt auch die Netzdynamik." Die Zweige "IV1 trifft ein" und "dazu IV2" sind nicht ausgeloest.
- **Staerke des Befunds:** 2,5 SE bei rho = 1; 18 von 25 Saaten positiv (Median +0,127). Bei rho = 0,5 ist c mit null
  vertraeglich. Beschreibend, unter der Annahme c ~ rho^(1/2), gemeinsam auf rho = 1 umgerechnet:
  +0,066 +- 0,037 (1,8 SE; nicht im Plan, von Hand).
- **Noetige Saaten (von Hand):** Fuer abs(c) = 2 SE bei rho = 0,5 braeuchte es beim gemessenen Mittel etwa 335 Saaten.

**Agenten-Vorhersagen** (PLAN Abschnitt 9, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (85 %) | Tor besteht (<= 5 % ausgeschlossen) | **eingetroffen**: 1 von 26 bzw. 0 von 12 Saaten |
| A2 (55 %) | IV3 berichtigt eingetroffen | **eingetroffen**: 0,27 SE |
| A3 (70 %) | sp und geo+ gleiches Vorzeichen von c in beiden Varianten | **nicht eingetroffen**: Dichte gleich (+), festes Netz verschieden (sp +0,171, geo+ -0,061) |
| A4 (40 %) | IV1 eingetroffen | **nicht eingetroffen** |
| A5 (60 %) | IV0 eingetroffen | **eingetroffen** (mit sp zwingend; mit geo+ nicht) |
| A6 (50 %) | IV2 nicht auswertbar | **eingetroffen** |

## 3. Tabellen

### 3.1 Steifigkeit je Datensatz [E]

(S = 0,25; je Saat y = a + c k^2 ueber abs(k) = 0,262 und 0,524; Saatmittel +- SE; dy = exaktes globales Glied)

| Variante, Dichte, Regel | Saaten | c | Std c je Saat | a (roh) | a_korr = a - dy |
|---|---|---|---|---|---|
| **Dichte, rho = 1, sp (Urteil)** | 25 | **+0,111 +- 0,045** | 0,225 | 1,882 +- 0,019 | **-0,005 +- 0,019** |
| Dichte, rho = 0,5, sp | 12 | -0,017 +- 0,045 | 0,154 | 0,958 +- 0,021 | +0,014 +- 0,021 |
| Dichte, rho = 1, geo+ | 25 | +0,371 +- 0,049 | 0,244 | 1,949 +- 0,019 | +0,062 +- 0,019 |
| Dichte, rho = 0,5, geo+ | 12 | +0,104 +- 0,039 | 0,135 | 0,999 +- 0,019 | +0,056 +- 0,019 |
| **Festes Netz, rho = 1, sp** | 25 | **+0,1706 +- 0,0002** | 0,0011 | +0,00056 +- 0,00002 | (kein dy) |
| Festes Netz, rho = 0,5, sp | 12 | +0,1179 +- 0,0003 | 0,0009 | +0,00051 +- 0,00003 | |
| Festes Netz, rho = 1, geo+ | 25 | -0,061 +- 0,008 | 0,042 | -0,057 +- 0,002 | |
| Festes Netz, rho = 0,5, geo+ | 12 | +0,024 +- 0,012 | 0,043 | -0,033 +- 0,003 | |

- dy = 1,8870 (rho = 1) und 0,9435 (rho = 0,5).
- **Homogenitaet am festen Netz (Kontrolle zu [K3] und zu den kurzen Querrichtungen) [E, M]:** c je k (sp) ist
  0,1788 und 0,1727 bei abs(k) h0 = 0,26 und 0,52 (rho = 1) und 0,1253 und 0,1197 bei 0,31 und 0,62 (rho = 0,5).
  Geteilt durch rho^(1/2) liegen die rho = 0,5-Werte auf der rho = 1-Kurve, auf 0,3 % und 0,6 %. Der Exponent
  0,534 statt 0,5 ist genau dieser schwache Abfall von c mit k. Endlichkeitseffekte der duennen Querrichtung zeigen
  sich hier nicht (nur festes Netz geprueft).

### 3.2 Je k [E]

| Datensatz | abs(k) | y (roh) | y - dy | Std y je Saat | c = (y - dy)/k^2 |
|---|---|---|---|---|---|
| Dichte rho = 1, sp | 0,262 | 1,8895 +- 0,0167 | +0,0025 | 0,084 | +0,04 +- 0,24 |
| | 0,524 | 1,9123 +- 0,0121 | +0,0253 | 0,061 | +0,092 +- 0,044 |
| Dichte rho = 0,5, sp | 0,262 | 0,9566 +- 0,0192 | +0,0131 | 0,067 | +0,19 +- 0,28 |
| | 0,524 | 0,9532 +- 0,0174 | +0,0097 | 0,060 | +0,035 +- 0,064 |
| Festes Netz rho = 1, sp | 0,262 | 0,012257 +- 0,000011 | - | 0,000056 | 0,1788 |
| | 0,524 | 0,047346 +- 0,000047 | - | 0,00023 | 0,1727 |
| Festes Netz rho = 1, geo+ | 0,262 | -0,0616 +- 0,0022 | - | 0,011 | (nicht k^2-foermig) |
| | 0,524 | -0,0742 +- 0,0025 | - | 0,012 | |

- Die Streuung von y in der Dichte-Variante haengt nicht von k ab (0,06 bis 0,08), wie fuer Kipprauschen erwartet; im
  festen Netz ist sie 260- bis 1500-mal kleiner. Das Signal waechst wie k^2, deshalb traegt das groessere k die
  Steigung.
- Bilder: lauf-69/bild-konform.png (y - dy gegen k^2 je Variante und Dichte, mit Fits), lauf-69/bild-streuung.png
  (c je Saat, Std von y je k), lauf-69/bild-kippen.png (Kippen und Einbettbarkeit gegen s, aus K5).

### 3.3 Netze im Hauptlauf [E]

| | rho = 1 (N = 6591) | rho = 0,5 (N = 3296) |
|---|---|---|
| Saaten / ausgeschlossen | 26 / 1 (Saat 105) | 12 / 0 |
| neue 4-Simplizes je Bildnetz gegenueber Grundnetz | 78,8 % | 79,1 % |
| geo+: ersetzte Simplizes, Bildnetz (Mittel, max) | 0,43 %, 0,73 % | 0,60 %, 1,03 % |
| geo+: ersetzte Simplizes, festes Netz | 0,32 % | 0,45 % |
| kleinste Saum-Marge | -0,015 (Saat 105), sonst > 0 | 0,091 |
| Qhull-Punkte je Knoten | 6,5 | 8,5 |
| Laufzeit je Saat (beide Varianten, beide Regeln) | 186 bis 213 s | 78 bis 97 s |

- Alle 38 Grundnetze und 151 von 152 Bildnetzen gueltig; 646 LU, alle mit U_ii > 0 und perm_r = perm_c.

## 4. Kontrollen

- **Tor (PLAN Abschnitt 6): bestanden**, fuer sp und fuer geo+ (K3 <= 1e-3).
  - 38 Grundnetze und 151 von 152 Bildnetzen gueltig; das eine (Saat 105, n = 2, -S) scheiterte nur an der
    Saum-Marge (-0,015). Die Saat ist ausgeschlossen (1 von 26 = 3,8 % <= 5 %).
  - 646 LU, alle mit U_ii > 0 und perm_r = perm_c; mit sp alle Simplizes einbettbar, mit geo+ nach Ersatz.
  - Newton-Residuum <= 1e-12 in jedem Bildnetz (K1: 8,9e-16).
- **K1 (Abbildung psi, N = 6591):** Newton-Residuum 8,9e-16 nach 5 bis 6 Schritten; Momente <e^(-4 sigma)> und
  <cos(k x1)> der Bildpunkte gegen 1/I0(4s) und I1(4s)/I0(4s): z-Werte <= 1,02 (s = +-0,125 und +-0,25, n = 1 und 2);
  Querkoordinaten unveraendert (0,0); KS * sqrt(N) 0,64 bzw. 0,48, bei allen s gleich (psi bildet die Grundphasen
  exakt auf die Verteilungsfunktion ab).
- **K2 (Saum und Delaunay):** Mit Saum 2,5 und 4,0 lokalen Abstaenden entstehen dieselben Simplexmengen (Grundnetz
  und Bildnetze bei s = +-0,25, n = 2; N = 6591 und N = 3296). Keine Umkugel enthaelt einen Punkt (kd-Baum ueber alle
  Saumpunkte). Alle Netze gueltig (Euler 0, Facetten gepaart, Koordinatenvolumen exakt V). Bei N = 6591:
  209 236 Simplizes, Qhull mit 40 000 bis 46 000 Punkten, groesster Umkugelradius 1,38 (s = 0) bzw. 1,72 (+-S),
  Saum-Marge 0,49 / 0,31 / 0,11 (s = 0 / +S / -S). Bei N = 3296: 104 276 Simplizes, Umkugelradius bis 2,07,
  Saum-Marge 0,77 / 0,19 / 0,28; einzelne Kanten laenger als Lq/2 (0,52 bis 0,54 Lq), richtig gezaehlt ueber den
  Periodenversatz.
- **K3 (Laengenformel, nur fuer geo+):** Die Geodaeten-Formel zweiter Ordnung trifft die numerisch minimierte
  Weglaenge (Kurvenschar in der Ebene aus d und k, Gauss-Legendre 64) auf <= 8,1e-5 relativ, 60 Zufallskanten mit
  abs(s) k l bis 0,40; die Mittelpunktsregel liegt bis 8,4e-3 daneben.
- **K4 (log det' und P1):** LU gegen dichte slogdet(K + 1 1^T/N) und gegen die Eigenwerte <= 3,2e-12 absolut
  (N = 1500, s = 0 und +-0,25, beide Regeln; relativ etwa 1e-15). Die P1-Matrizen stimmen mit
  induziert.lokal_K_batch aus INDUZIERT-1 auf <= 3,7e-16 relativ ueberein. Bei abs(k) h0 = 1,0 (K4-Netz) ersetzt geo+
  1 070 bzw. 1 106 Simplizes.
- **K5 (Kippen und Einbettbarkeit gegen s, N = 3296, Saat 990, F = 104 000):**

| s | neue 4-Simplizes (n = 1 / 2) | neue Kanten | nicht einbettbar geodaetisch, Bildnetz (n = 1 / 2) | festes Netz (n = 1 / 2) |
|---|---|---|---|---|
| 1e-4 | 0,1 % / 0,1 % | 0,0 % | 0 / 0 | 0 / 1 |
| 1e-3 | 1,0 % / 1,0 % | 0,1 % | 1 / 1 | 0 / 3 |
| 0,01 | 9,3 % / 9,0 % | 1,2 % / 1,1 % | 7 / 18 | 3 / 27 |
| 0,1 | 55 % / 55 % | 11 % | 83 / 373 | 91 / 298 |
| 0,125 | 61 % / 61 % | 13 % | 139 / 465 | 111 / 369 |
| 0,25 | 77 % / 79 % | 24 % | 260 / 982 | 194 / 671 |

  - Das Kippen haengt kaum von k ab und waechst anfangs linear in s, etwa 9 % neue Simplizes je 0,01 in s.
  - Nicht einbettbare Simplizes mit geodaetischen Laengen gibt es schon bei s = 1e-4 bis 1e-3; ihre Zahl waechst
    etwa wie s k^2 (Grund fuer [K1]). Alle Netze gueltig.
- **K6 (beschreibend, Gamma(s) auf feinem s-Gitter, N = 1500 isotrop, abs(k) h0 = 1,0, Regel sp):**
  Gamma(Bildnetz) - Gamma(festes Netz) bei s = 0; 0,002; ...; 0,02: 0; -0,34; +1,98; +3,64; +2,62; +3,76; +2,84;
  -0,26; +1,32; +3,72; +5,72, bei 954 bis 8 037 neuen Simplizes. Das ist eine Zufallsbewegung mit Schritten von
  einigen Einheiten je 0,002 in s; das feste Netz aendert sich glatt. Die Spruenge sind der Grund fuer das grosse
  Saatrauschen (Abschnitt 3).
- **Netzstatistik [E]:** Simplizes je Knoten 31,6 bis 31,8 (Rauchlaeufe, isotrop), mittlerer Grad 37,6 bis 37,8.
  Fuer Poisson-Delaunay in 4D ist ein Mittel von etwa 31,78 Simplizes je Punkt bekannt [L?]; die Werte passen dazu.

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - Das feste Netz haette negativ sein koennen (IV0), die Dichte-Variante positiv oder negativ (IV1); das Kipprauschen
    haette jede Aussage verdecken koennen (so kam es bei rho = 0,5 und bei IV2).
  - Das berichtigte k^0-Glied haette von null verschieden sein koennen (IV3).
  - Netz- und LU-Tore, K2 (Saum 2,5 gegen 4,0) und K4 haetten scheitern koennen.
  - Gescheitert sind die Karten-Hypothese IV1 und meine A3 und A4. IV0 war mit sp dagegen nicht scheiterbar
    (Konvexitaet, Abschnitt 6 Punkt 5); die Latte erfuellt dort nur die geo+-Fassung.
- **L2 (Gegenprobe):**
  - zwei Laengenregeln (sp, geo+) auf denselben Netzen; zwei Dichten; festes Netz und Dichte-Variante auf demselben
    Grundnetz je Saat
  - K2: zweiter Saum (4,0) und leere Umkugeln per kd-Baum; K4: LU gegen dichte Rechnung und gegen INDUZIERT-1
  - Achsenabschnitt roh gegen berichtigt (exaktes globales Glied)
- **L3 (Numerik):** log det' etwa 1e-15 relativ; Newton 8,9e-16; Geodaete 8,1e-5. Statistisch: SE(c) 0,045 in der
  Dichte-Variante (beide Dichten), 0,0002 bis 0,0003 im festen Netz; Std von c je Saat 0,15 bis 0,24.
- **L4 (schon bekannt):**
  - Sakharov 1967, Visser 2002: induzierte Gravitation; ein minimal gekoppelter Skalar gibt im Kontinuum mit
    kovariantem Abschneiden ein Einstein-Glied mit positivem G, Koeffizient ~ Lambda^2 [L]. Daraus [M]: konforme
    Steifigkeit c = -Lambda^2/(32 pi^2) bei Eigenzeit-Abschneiden (Waermeleitungskoeffizient a_1 = R/6 [L]).
  - Das "falsche" Vorzeichen des konformen Modus in der euklidischen Einstein-Wirkung: Gibbons, Hawking, Perry 1978
    [L].
  - "Zahl = Volumen": Bombelli, Lee, Meyer, Sorkin 1987 [L]; Zufallsgitter: Christ, Friedberg, Lee 1982 [L].
  - Splitter in 3D-Delaunay-Netzen und ihre Folgen fuer FEM: z. B. Cheng, Dey, Edelsbrunner, Facello, Teng 2000
    ("sliver exudation") [L]. Primal- (P1) und Dual-Laplace (Voronoi) sind in 3D verschieden, nur der duale hat fuer
    Delaunay-Netze nichtnegative Gewichte: Alexa et al. 2020 [L]. Daraus folgt auch, dass die P1-Steifigkeit beim
    Kippen springt (Beispiel in PLAN K6).
  - Dynamische Triangulierungen in 4D (Ambjoern, Jurkiewicz, Loll) sind ein anderes Ensemble (Summe ueber Netze mit
    Regge-Gewicht) [L].
  - Ob die induzierte konforme Steifigkeit auf Poisson-Delaunay-Netzen mit Streuung nach Volumen in 4D schon
    gerechnet ist, weiss ich nicht [L?].
- **L5 (Messbezug):** keiner (4D euklidisch, synthetisch; der konforme Modus ist nicht direkt messbar).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Laengenregel ("Kantenlaengen physikalisch"):**
  - In 4D-Poisson-Delaunay-Netzen gibt es Splitter: Simplizes mit kleinem Volumen bei normalen Seitenflaechen,
    P(eps < x) etwa 5 x^2 (eps = Volumen relativ zum regulaeren Simplex). Ihre P1-Steifigkeit waechst wie 1/eps.
  - Mit geodaetischen Laengen werden sie schon bei kleinem s nicht einbettbar (Gram-Matrix indefinit): 1 bis 8 bei
    s = 0,001 bis 0,01, bei S = 0,25 einige hundert bis gut tausend je Netz (0,2 bis 0,7 %).
  - Geurteilt ist deshalb mit der Schwerpunktregel sp (immer einbettbar; FEM fuer -div(e^(2 sigma) grad)). Der
    Kartenwortlaut ist geo+ (geodaetisch, nur die nicht einbettbaren Simplizes ersetzt), auf denselben Netzen und mit
    denselben Regeln mitberichtet.
  - Ergebnis: Die Regel aendert die Zahlen stark. Dichte-Variante (rho = 1) sp +0,111, geo+ +0,371; festes Netz sp
    +0,171, geo+ -0,061. Im festen Netz gibt geo+ ausserdem ein k^0-Glied von -0,057 +- 0,002 und kein k^2-foermiges
    y (y = -0,062 und -0,074 bei beiden k). Auf einem festen Netz ist ein solches Glied ohne Artefakt nicht moeglich
    (Gamma ist bei konstantem sigma exakt linear). geo+ wird also von Splittern beherrscht (0,3 bis 0,6 % ersetzt,
    dazu fast entartete Splitter mit Steifigkeit ~ 1/eps). Die Berichtigung war noetig; das Vorzeichen in der
    Dichte-Variante ist in beiden Regeln positiv.
- **[K2] Volumenterm:**
  - Bei fester Punktzahl waechst das physikalische Volumen auf V I0(4S). Weil K in 4D homogen vom Grad 2 in den
    Laengen ist, enthaelt Gamma exakt (N - 1)/4 log I0(4S), also y das k-unabhaengige Glied dy = 1,887 rho (N - 1)/N.
  - Nach Kartenwortlaut (roh) war IV3 damit vorab entschieden.
  - Ergebnis: Das exakte Glied erklaert das k^0-Glied vollstaendig: roh 1,8819 +- 0,0190 gegen dy = 1,8870
    (rho = 1), 0,9578 +- 0,0207 gegen 0,9435 (rho = 0,5); berichtigt -0,005 +- 0,019 und +0,014 +- 0,021.
- **[K3] IV2 und Homogenitaet:** Exakt gilt c(rho, k) = rho^(1/2) c_1(k rho^(-1/4)). Ein Exponent 0,5 folgt fuer jedes
  lokale k^2-Glied; IV2 prueft, ob c im Fenster nicht von k abhaengt. Ergebnis: Im festen Netz (sp) bestaetigt,
  p = 0,534 +- 0,004, und die Abweichung von 0,5 ist genau der gemessene Abfall von c mit k (Abschnitt 3.1). Fuer
  die Dichte-Variante nicht auswertbar.
- **[K4] Feste Punktzahl statt Poisson:** wie INDUZIERT-DICHTE-2D.
- **[K5] S = 0,25, gestreckter Torus 24 x 6,5^3, n = 1 und 2:** Bei S = 0,5 waren 2 bis 4 % der Simplizes nicht
  einbettbar und die Saum-Pruefung schlug fehl; ein isotroper Torus mit N = 6591 haette abs(k) h0 >= 0,7. Die kurzen
  Querrichtungen (6,5) sind ein Endlichkeitsrisiko [H]. Ergebnis: am festen Netz klein (Homogenitaet auf 0,3 bis
  0,6 %, Abschnitt 3.1); fuer die Dichte-Variante nicht geprueft.
- **[K6] Delaunay in Koordinaten:** Kartenwortlaut. Bis zur ersten Ordnung in abs(grad sigma) l ist das gleich dem
  physikalischen Delaunay-Netz (Moebius-Abbildung erhaelt leere Kugeln) [M].
- **[K7] Saatzahl aus der Laufzeit:** 26 bzw. 12 Saaten geplant (PLAN Abschnitt 8); gerechnet 26 und 12, ausgewertet 25 und 12.
- Kartenfehler, die ein Urteil nach Kartenwortlaut veraendern: [K1] (Regel nicht ueberall definiert) und [K2]
  (IV3 roh vorab entschieden). Beide Lesarten sind berichtet.

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:** keine Mittelwerte oder Vorzeichen der Messgroesse. Gesehen habe ich:
   - blinde Standardabweichungen von y aus je 2 bis 3 Rauchsaaten (PLAN Abschnitt 11);
   - in der Kontrollprobe (K6, N = 1500, abs(k) h0 = 1,0) Gamma(Bild) - Gamma(fest) bei s <= 0,02, also das
     Springen von Gamma beim Kippen, keine Messgroesse;
   - Netz-, Zeit- und Einbettungsdaten.
2. **Nach Rauchlaeufen festgelegt (vor dem Einfrieren):** Regel sp statt geodaetischer Laengen ([K1]), S = 0,25 statt
   0,5, gestreckter Torus, n = 1 und 2, Saum nach lokalem Abstand, Zaehlung der Teilsimplizes mit Periodenversatz
   (die erste Fassung verlangte Kanten < L/2; sie haette im duennen Bereich gueltige Netze verworfen).
3. **Codeprobe mit veraenderten Daten:** Fuer den Test der Auswertungspfade habe ich in einer Kopie (rauch/probe2)
   die Saum-Marge per jq auf 1 gesetzt. Nur Codetest, die Probe-Urteile habe ich nicht gelesen.
4. **Abweichungen vom Brief:**
   - Kanonische Auswahl ueber den Schwerpunkt im Grundbereich statt "mindestens eine Ecke im Grundbereich und
     zurueckfalten" (gleichwertig: genau ein Bild je Torus-Simplex).
   - "Groesstes machbares N": gemessen 2000/5000/10000 isotrop (Qhull 7/13/21 s, LU 0,5/5,9/40 s). Gewaehlt ist
     N = 6591 auf dem gestreckten Torus, damit in der Zeitbox mindestens 16 Saaten moeglich sind. N = 10 000 waere
     je Netz machbar gewesen, aber nur mit etwa der Haelfte der Saaten.
   - Exakte LU, keine stochastische Spurschaetzung (Fill-in tragbar).
5. **IV0 mit Regel sp ist vorab entschieden [M], erst nach dem Einfrieren erkannt (notiert 09:11:02 CEST per date,
   vor der Auswertung, ohne Kenntnis der Werte):**
   - Auf dem festen Netz gilt mit sp K(s) = sum_T e^(2 s cos(k c_T)) K_T. Zerlegt man jedes K_T in Rang-1-Teile,
     gibt Cauchy-Binet log det K_(0)(s) = log sum_S w_S e^(s A_S) mit w_S >= 0: eine log-sum-exp-Funktion, also
     konvex in s. Damit ist y >= 0 fuer jede Saat und jedes k.
   - Ausserdem Gamma''(0) = sum_(T,T') M_TT' (cos(k c_T) - cos(k c_T'))^2 mit M_TT' = tr(K^-1 K_T K^-1 K_T') >= 0, also
     Gamma'' = 0 bei k = 0 und Gamma'' >= 0 sonst.
   - Eine positive Steigung c war mit sp also bis auf k^4-Effekte zwingend; IV0 (sp) ist keine Messung. Die
     aussagekraeftige Fassung ist der Kartenwortlaut geo+ (geodaetische Laengen, nicht linear in den Gewichten,
     keine solche Ungleichung).
   - Fuer die Dichte-Variante gilt das nicht: Gamma(+S), Gamma(-S) und Gamma(0) gehoeren zu verschiedenen Netzen.
6. **Nach dem Einfrieren sonst:**
   - Kein Code geaendert (Pruefsummen lokal und auf der .69 gleich, Abschnitt 8).
   - Waehrend der Hauptlaeufe habe ich die Logs nur gefiltert gelesen (Saat fertig, Tor-Verletzungen, Fehler; die
     y-Werte per sed entfernt) und die Kontroll-Ausgaben K1 bis K6. Messwerte habe ich erst in der Auswertung gesehen.
   - In lauf-69/auswertung.json habe ich per jq Felder "vermerk" eingetragen; ohne sie ist die Datei gleich
     auswertung.maschine.json (geprueft), deren Pruefsumme der der .69 entspricht.
   - Lokal ein jq-Filter code/zusammenfassung.jq (nur Lesen von auswertung.json), vorher an der Codeprobe mit
     verworfener Ausgabe getestet.
   - Saat 105 (N = 6591) schied am Saumtor aus (Marge -0,015 in einem Bildnetz). Meine Log-Filterung auf
     "gueltig False" hat das waehrend der Laeufe nicht gemeldet, weil das Protokoll "True/False" schreibt; erst die
     Auswertung fand es. Das Saumtor ist absichtlich streng (Abschwaechung e^(-abs(s) k R)); in K2 waren die Netze mit
     kleinen Margen gleich denen mit Saum 4,0. Die Regel des Plans ist trotzdem so angewandt.
   - Die Starts je Spur liefen nicht in der Reihenfolge der Einreihung (der Lock des Starters ist nicht FIFO), alle
     Saatbereiche wie geplant.
   - Beschreibend und nicht im Plan, von Hand: die gemeinsame Umrechnung beider Dichten (+0,066 +- 0,037), die noetige
     Saatzahl bei rho = 0,5 und die Homogenitaetspruefung am festen Netz (Abschnitt 3.1).
7. **Rauchlaeufe r5 und r6** waren mit mehr Saaten gestartet, als in 600 s passten; sie wurden vom Starter beendet
   (rc 1). Gespeichert waren 2 bzw. 3 Saaten (nach jeder Saat geschrieben).
8. **Spuren und Laeufe:** cpu3 und cpu4, nie mehr als zwei Laeufe zugleich; Starts je Spur ueber den Lock des Starters
   nacheinander, je ssh-Aufruf ein Starter (lokal im Hintergrund wartend). Kein Python-Start ausserhalb des Starters,
   keine Versionsprobe. Auf der .69 ausserhalb des Starters: mkdir, mv, ls, sha256sum, jq (Lesen und, fuer probe2,
   Schreiben einer Testkopie), date, nproc, free, uptime, systemctl --user list-units (nur Anzeige).
9. **Lokal:** kein python, awk oder perl. Benutzt: jq, sed, grep, sha256sum, date, ssh, scp, dazu cp, mv, mkdir, rm,
   ls, cat, head, tail, cut, wc.
10. **Scratchpad:** Ich habe nichts in den Scratchpad der Leitung geschrieben. Die Werkzeugumgebung legt fuer
   Hintergrundbefehle eigene Ausgabedateien unter /tmp/claude-1000/.../tasks/ an; meine Ausgaben gingen per
   Umleitung in den Kartenordner.
11. **Zeitbox:** Start 08:15:57 CEST, Abgabe 10:05:10 CEST (date), innerhalb von 150 min.

## 7. Bedeutung

- **Ausgeloest ist der vorab festgelegte Zweig "IV1 verfehlt":** In 4D reicht Volumen-Zaehlung allein nicht; dann
  zaehlt auch die Netzdynamik.
  - Genauer [E]: Die Streuung nach Volumen senkt die konforme Steifigkeit gegenueber dem festen Netz (rho = 1 um
    0,060 +- 0,045, rho = 0,5 um 0,135 +- 0,045), dreht das Vorzeichen aber nicht in den Einstein-Bereich. Bei rho = 1
    bleibt c mit 2,5 SE positiv, bei rho = 0,5 ist c mit null vertraeglich.
  - Fuer Finns Weiche heisst das [H]: Die 2D-Botschaft ("Zahl = Volumen" stellt die geometrische Antwort her) traegt
    nicht automatisch nach 4D. In 2D gibt es einen universellen, regulatorunabhaengigen Anteil (Polyakov), den das
    Ensemble nur freilegen musste. In 4D ist das Einstein-Glied selbst ein Gitterglied ~ Lambda^2 [L Sakharov]; sein
    Vorzeichen haengt an der Diskretisierung, und dieses P1-Delaunay-Ensemble liefert es im gerechneten Fenster nicht
    (positiv bei rho = 1, null bei rho = 0,5).
  - Was es liefern koennte, bleibt offen: eine andere Materie-Diskretisierung (etwa der beim Kippen stetige
    Voronoi-Laplace), ein Gewicht ueber die Netze (Netzdynamik, wie in dynamischen Triangulierungen) oder andere Felder.

- **Strukturbefund festes Netz [M]:** Geht die Metrik nur ueber positive Elementgewichte ein
  (K = sum_T e^(2 sigma_T) K_T, Regel sp), dann ist Gamma = 1/2 log det' K eine konvexe Funktion der sigma_T
  (log-sum-exp nach Cauchy-Binet). Jede Verformung, die nur diese Gewichte aendert, also jeder konforme Modus, hat
  dann eine nichtnegative Steifigkeit. Ein festes Netz kann so das Einstein-Vorzeichen des konformen Modus nie
  liefern; dafuer muss etwas anderes von der Metrik abhaengen, hier die Punktdichte (oder, beim Kartenwortlaut, die
  Form der Simplizes ueber die geodaetischen Laengen). Das stuetzt die Fragestellung der Karte, beantwortet sie aber
  nicht.

- **Was in 4D anders ist als in 2D [E, M]:**
  - In 2D kippten bei S = 0,5 etwa 19 % der Kanten, und der Kotangens-Laplace ist beim Kippen stetig (nur Knicke).
    Die Differenzen blieben dadurch stark korreliert.
  - In 4D sind bei S = 0,25 rund 78 % der 4-Simplizes neu (schon bei s = 0,01 etwa 9 %), und die P1-Steifigkeit
    springt bei jedem Kippen. Gamma(S) und Gamma(0) sind dann fast unabhaengige Zufallsgroessen; die gemeinsamen
    Zufallszahlen helfen kaum.
  - Dazu kommen Splitter (P(eps < x) etwa 5 x^2) mit Steifigkeit ~ 1/eps. Mit geodaetischen Laengen werden sie schon
    bei kleinem s nicht einbettbar; die Kartenregel ist deshalb nicht ueberall definiert ([K1]).
- **Volumenglied [M, E]:** Bei fester Punktzahl gibt die Homogenitaet von K (Grad 2) exakt
  dy = (N - 1) log I0(4S)/(2 S^2 V). Das ist kein Merkmal der induzierten Wirkung, sondern der Konvention "N fest,
  Gesamtvolumen waechst". Gemessen: Das k^0-Glied ist genau dieses Glied (Rest -0,005 +- 0,019 bzw. +0,014 +- 0,021).
  Ein echtes Volumen- oder Kosmologie-Glied tritt mit "Zahl = Volumen" nicht auf (Regel sp); mit geo+ bleibt ein Rest
  von +0,062 +- 0,019 (3,2 SE), passend zu den Splitter-Effekten.
- **Grenzen:**
  - Eine Schleife, freies masseloses Skalarfeld, euklidisch, feste Punktzahl, Delaunay in Koordinaten.
  - Urteilsregel sp statt geodaetischer Laengen; S = 0,25 endlich (Faktor etwa 0,92 fuer eine reine Einstein-Wirkung,
    [K5]); nur zwei k-Werte, also keine Pruefung der k^2-Form innerhalb einer Dichte.
  - Kurze Querrichtungen (6,5 mittlere Abstaende bei rho = 1, 5,5 bei rho = 0,5; im duennen Bereich bei S = 0,25 etwa
    4,8 bzw. 4,0); Endlichkeitseffekte nur am festen Netz geprueft (klein, Abschnitt 3.1).
  - Nur der konforme Modus; spurfreie Verformungen (c2, Verhaeltnis -2) sind nicht gerechnet.
- **Naechste Schritte [H]:**
  - (a) Mehr Saaten bei N = 3296 (billiger, gleiches Signal-Rausch-Verhaeltnis je Saat) oder ein Rausch-armes Schema:
    zum Beispiel ein Laplace, der beim Kippen stetig ist (dualer Voronoi-Laplace, in 3D und 4D fuer Delaunay-Netze
    mit nichtnegativen Gewichten [L Alexa et al.]).
  - (b) Splitter entschaerfen (gewichtetes Delaunay oder Splitter-Entfernung), damit physikalische Laengen ueberall
    einbettbar sind.
  - (c) Erst danach spurfreie Verformungen und das Verhaeltnis c0s/c2 = -2 (der eigentliche Einstein-Test der Karte).

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-090039, EINGEFROREN-SHA256.txt
- code/:
  - dichte4d.py: Abbildung psi, periodisches 4D-Delaunay mit Saum, Pruefungen, Laengenregeln sp/geo/geo+, P1,
    log det', Modi netztest, einbettung, kontrolle, dichte
  - auswertung4d.py: Tor, Urteile, Tabellen, Bilder
  - induziert.py: unveraendert aus INDUZIERT-1 (sha256 b3867eac...)
  - je mit Kopien *.eingefroren-20261004-090039
- lauf-69/:
  - kontrolle-a.json (K1 bis K4, N = 6591), kontrolle-b.json (K2, K5, K6, N = 3296)
  - dichte-N6591-s{0,2,4,6,8,10,12,14,100,102,104,106,108}.json (je 2 Saaten), dichte-N3296-s{0,4,8}.json (je 4
    Saaten)
  - auswertung.json (Urteile, mit Vermerken per jq), auswertung.maschine.json (unbearbeitet, Pruefsumme wie auf der
    .69), auswertung.log, PRUEFSUMMEN.txt (.69)
  - Bilder: bild-konform.png (y gegen k^2 je Variante und Dichte), bild-streuung.png (Saatstreuung),
    bild-kippen.png (Kippstatistik und Einbettbarkeit)
  - je Lauf ein .log (Starter-Ausgabe)
- rauch-69/: netztest-r1/-r2, einbettung-r3/-r4, rausch-r5/-r6 (blind), Logs; probe/ und probe2/ (Codeprobe)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-induziert-4d/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir haben in einer vierdimensionalen Modellwelt geprueft, ob die Regel "so viele Netzpunkte wie Volumen" dafuer
sorgt, dass das Zittern der Materie die Raumzeit mit dem richtigen Vorzeichen versteift, so wie es Einsteins
Schwerkraft verlangt. In zwei Dimensionen hatte das geklappt. In vier Dimensionen hilft die Regel nur teilweise: Sie
macht die falsche Steifigkeit des festen Netzes kleiner, dreht ihr Vorzeichen aber nicht um; bei der hoeheren
Punktdichte bleibt es knapp messbar beim falschen Vorzeichen, bei der niedrigeren ungefaehr bei null. Die Rechnung ist
stark verrauscht, weil sich das Netz in vier Dimensionen schon bei einer kleinen Verbiegung zu fast vier Fuenfteln neu
knuepft. Die Antwort lautet vorerst: Punkte nach Volumen allein reichen in vier Dimensionen nicht, es braucht noch
etwas anderes, zum Beispiel eine Regel dafuer, welche Netze wie stark zaehlen.
