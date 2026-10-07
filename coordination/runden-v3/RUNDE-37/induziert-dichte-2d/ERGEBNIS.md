# INDUZIERT-DICHTE-2D: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 07:07:51 CEST; Code ab 07:23:07, Plantext ab 07:34:23 CEST.
  - Rauchlaeufe 05:25:40 bis 05:34:27 UTC, Probe der Auswertung 05:33:32 bis 05:33:36 UTC (PLAN Abschnitt 11).
  - Eingefroren 07:36:39 CEST: PLAN.md.eingefroren-20261004-073639, Code-Kopien *.eingefroren-20261004-073639,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 05:36:55 bis 06:08:37 UTC (11 Starts), Auswertung 06:08:42 bis 06:08:46 UTC, alle rc = 0.
  - Text ab 08:10:05 CEST.
- Nach dem Einfrieren ist der Code unveraendert; die Pruefsummen auf der .69 und lokal stimmen ueberein.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu3 und cpu4).
  Gerechnet ist euklidisch, eine Schleife, ein freies masseloses Skalarfeld. Synthetisch, keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier keine Quelle abgerufen)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik
  - [E] hier gerechnet
  - [F] Festlegung im Plan
  - [K] Kartenpunkt
  - [H] Hypothese
- **Konvention (wie INDUZIERT-ZUFALL-2D):**
  - Gamma = 1/2 log det' K, K = Kotangens-Laplace aus den physikalischen Kantenlaengen.
  - Metrik g = e^(2 sigma) delta auf dem Torus, sigma = s cos(k.x). Polyakov: Gamma'' = -k^2 A/(24 pi), also
    c = -1/(24 pi) = -0,013263.
  - **Dichte-Streuung:** Dieselben Grundpunkte werden mit einer flaechentreuen Abbildung psi_s so verschoben, dass sie
    in der physikalischen Flaeche gleichverteilt sind. Danach wird neu vernetzt (Delaunay in Koordinaten) und mit
    geodaetischen Laengen gerechnet.
  - **Messgroesse:** y = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/(S^2 A) mit S = 0,5. Je Saat wird y = a + c k^2 ueber
    vier k angepasst: a ist das Flaechenglied, c die Steifigkeit pro Flaeche und k^2.

## 1. Ergebnis zuerst

1. **"Zahl = Volumen" beseitigt den grossen Gitterterm [E].**
   - Gleiche Grundpunkte, gleiche Materie, gleiche Konvention. Auf festem Netz ist die konforme Steifigkeit
     c = +0,1590 (ID0, wie INDUZIERT-ZUFALL-2D).
   - Mit Streuung nach physikalischer Flaeche und Neuvernetzung ist c = **-0,0123 +- 0,0012** (N = 64 000, 66 Saaten,
     Steigung ueber abs(k) = 0,05 bis 0,3 nach Abzug des Flaechenglieds).
   - Polyakov waere -0,0133; das Verhaeltnis ist 0,92.
   - Gegenproben: N = 16 000 gibt -0,0131 +- 0,0022 (S = 0,5) und -0,0168 +- 0,0047 (S = 0,25). Die Richtungen 0 und
     90 Grad geben -0,0123 und -0,0122.
2. **Ein Flaechenglied gibt es nicht [E, M]:** a = +0,00028 +- 0,00017 (1,6 SE von 0). Das war fuer feste Punktzahl
   vorhergesagt, weil die Kotangens-Gewichte nur von Winkeln abhaengen.
3. **Grenzen der Aussage:**
   - Gemessen ist die Steigung ueber das k-Fenster. Der Einzelwert beim kleinsten k (Kartenwortlaut) ist nicht
     auswertbar: -0,014 +- 0,025. Dafuer braeuchte es rund 10 700 Saaten.
   - Andere Lesarten liegen weiter von Polyakov weg, 1,0 bis 2,2 SE:
     - mit a = 0 erzwungen: -0,0082 +- 0,0023 (0,61 P; 2,2 SE von P)
     - mit k^4-Glied: -0,0072 +- 0,0059 (1,0 SE von P)
   - Ein k^4-Glied von der Groesse des festen Netzes verschoebe den Wert bei k -> 0 um bis zu +0,003, auf etwa 0,7 P.
   - Jede einzelne Saat streut stark (Std 0,009 bei N = 64 000). Das kommt vom Kantenkippen; das Rauschen haengt nicht
     von k ab und faellt mit N.
4. **Urteile:**
   - ID0, ID1, ID2 und ID3 eingetroffen.
   - Nach Kartenwortlaut ("kleinstes k" als Einzelwert) ist ID1 nicht auswertbar; ID3 nach Vorzeichen allein ist
     eingetroffen.
   - Ausgeloest ist der vorab festgelegte Zweig "ID1 und ID3 treffen ein": "Zahl = Volumen" stellt die geometrische
     Antwort her, der grosse Gitterterm war ein Artefakt des festen Netzes. Das gilt fuer das 2D-euklidische Modell und
     die konforme Mode (Abschnitt 7).

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/dichte_auswertung.py; Werte in lauf-69/auswertung.json (unbearbeitet).
Tor bestanden (Abschnitt 4). Alle Saatzahlen wie geplant (66 bei N = 64 000; 64 bei N = 16 000; 16 im intr-Lauf;
3 fuer ID0).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| ID0 | feste Punkte geben c_P = +0,159 auf 2 % wieder | 85 % | **eingetroffen** | eingetroffen | c = 0,15899 +- 0,00017 (geo-Laengen, Richardson, N = 64 000, n = 2, Achsen, 3 Saaten): 0,007 % von 0,159. Eckenregel je Saat bitgleich zu INDUZIERT-ZUFALL-2D |
| ID1 | [H] Steifigkeit (Saatmittel, kleinstes k, N = 64 000) innerhalb 30 % von -1/(24 pi) | 35 % | **eingetroffen** | nicht auswertbar | c = -0,01226 +- 0,00115 (66 Saaten); Verhaeltnis 0,924, Abweichung 7,6 %; Band [-0,01724; -0,00928]; SE <= 0,00398. Kleinstes k allein: -0,014 +- 0,025 (SE zu gross) |
| ID2 | Ergebnis unterscheidet sich von +0,159 um > 3 SE | 70 % | **eingetroffen** | eingetroffen | Abstand 148 SE |
| ID3 | [H] Vorzeichen negativ | 50 % | **eingetroffen** | eingetroffen | c + 2 SE = -0,0100 < 0 |

- **Unterscheidbarkeit (Brief):** SE = 0,0012 ist weit unter 0,057. Das Rauschen trennt +0,159 und -0,013 also
  sicher (148 SE).
- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "ID1 und ID3 treffen ein" ist ausgeloest. "Zahl = Volumen" stellt die geometrische Antwort her; der grosse
    Gitterterm war ein Artefakt des festen Netzes.
  - Schwerkraft aus Materie wird damit auf einem Netz moeglich, dessen Punkte nach Volumen gestreut sind. Das stuetzt
    die Kausalmengen-Seite von Finns Weiche, als 2D-euklidisches Modell.
  - Die Einschraenkungen stehen in Abschnitt 7.
- **ID1 haengt an der Lesart (vor dem Einfrieren festgelegt, [K3]).** Geurteilt ist die Steigung ueber das Fenster.
  Mit a = 0 erzwungen laege c (0,61 P) knapp ausserhalb des Bandes, innerhalb von 2 SE; die Regel gaebe dann "nicht
  auswertbar".

**Agenten-Vorhersagen** (PLAN Abschnitt 9; A4 war nach den Rauchlaeufen absehbar)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (95 %) | Tor besteht | **eingetroffen**: 3 104 Bildnetze und 256 intr-Netze ohne Fehler |
| A2 (90 %) | ID0 eingetroffen; Eckenregel je Saat <= 1e-9 an INDUZIERT-ZUFALL-2D | **eingetroffen**: Abweichung 0 (bitgleich) in allen sechs Faellen |
| A3 (80 %) | Achsenabschnitt a mit 0 vertraeglich (<= 3 SE) | **eingetroffen**: 1,6 SE (N = 64 000); 1,1 SE (N = 16 000, S = 0,5) |
| A4 (absehbar) | c (N = 64 000) zwischen -0,03 und +0,01 | **eingetroffen**: -0,0123 |
| A5 (75 %) | N = 16 000: S = 0,25 und 0,5 gleich auf 2 SE | **eingetroffen**: -0,0168 +- 0,0047 gegen -0,0131 +- 0,0022 (0,7 SE, gemeinsame Saaten) |
| A6 (85 %) | intr und koord unterscheiden sich um < 0,2 SE | **eingetroffen**: -0,0189 gegen -0,0185, Differenz 0,0004 = 0,1 SE |
| A7 (65 %) | Saatstreuung von c faellt von N = 16 000 nach 64 000 um Faktor 1,5 bis 3 | **eingetroffen**: 0,0177 -> 0,0094, Faktor 1,89 (N^(-0,46)) |

## 3. Tabellen

### 3.1 Steifigkeit je Datensatz [E]

(Steigung c von y = Gamma''/A gegen k^2 je Saat, Saatmittel +- SE; abs(k) = 0,0497 / 0,0993 / 0,199 / 0,298;
Polyakov P = -0,01326)

| Datensatz | Saaten | c | c/P | Std je Saat | a (Flaechenglied) | c mit a = 0 | c mit k^4-Glied |
|---|---|---|---|---|---|---|---|
| **N = 64 000, S = 0,5 (Urteil)** | 66 (0 bis 65) | **-0,01226 +- 0,00115** | 0,92 | 0,0094 | +0,00028 +- 0,00017 | -0,0082 +- 0,0023 | -0,0072 +- 0,0059 |
| N = 16 000, S = 0,5 | 64 (0 bis 63) | -0,01311 +- 0,00222 | 0,99 | 0,0177 | +0,00040 +- 0,00035 | -0,0072 +- 0,0051 | -0,011 +- 0,011 |
| N = 16 000, S = 0,25 | dieselben 64 | -0,0168 +- 0,0047 | 1,27 | 0,0377 | +0,0015 +- 0,0007 | +0,005 +- 0,010 | -0,025 +- 0,024 |
| N = 16 000, S = 0,5, koord | 16 (100 bis 115) | -0,0185 +- 0,0042 | 1,39 | 0,0168 | -0,0004 +- 0,0007 | -0,024 +- 0,011 | -0,025 +- 0,017 |
| dieselben, intr | 16 | -0,0189 +- 0,0042 | 1,42 | 0,0168 | -0,0004 +- 0,0007 | -0,024 +- 0,011 | -0,025 +- 0,017 |
| festes Netz (ID0, geo) | 3 (0 bis 2) | +0,1590 (bei abs(k) = 0,05) | -12,0 | 0,0003 | entfaellt | - | Fit-Regel etwa 0,156 |

- **Richtungen (N = 64 000):** 0 Grad -0,01228 +- 0,00151, 90 Grad -0,01224 +- 0,00168. Bei N = 16 000 (S = 0,5):
  -0,0114 +- 0,0031 und -0,0148 +- 0,0036.
- **Alle unabhaengigen Saaten zusammen** (N = 64 000; N = 16 000 S = 0,5; intr-Lauf koord; gewichtet mit 1/SE^2,
  beschreibend, von Hand): -0,0128 +- 0,0010.
- **a bei S = 0,25:** 2,2 SE von 0. Dieselben Saaten haben bei S = 0,5 1,1 SE. Der Versatz durch Gamma(0) geht mit 1/S^2
  in a ein und ist in beiden S derselbe; die beiden Werte sind also nicht unabhaengig (Verhaeltnis 3,6, erwartet 4).

### 3.2 Je k, N = 64 000, S = 0,5 [E]

| abs(k) | y = Gamma''/A | Std je Saat | c = (y - a)/k^2 | y/k^2 (ohne Abzug) | Polyakov y = P k^2 | festes Netz c |
|---|---|---|---|---|---|---|
| 0,0497 | +0,000244 +- 0,000170 | 0,00138 | -0,014 +- 0,025 | +0,099 +- 0,069 | -0,000033 | 0,15899 |
| 0,0993 | +0,000112 +- 0,000184 | 0,00149 | -0,0169 +- 0,0054 | +0,011 +- 0,019 | -0,000131 | 0,15872 |
| 0,199 | -0,000124 +- 0,000179 | 0,00145 | -0,0102 +- 0,0022 | -0,0031 +- 0,0045 | -0,000524 | 0,15763 |
| 0,298 | -0,000841 +- 0,000156 | 0,00126 | -0,0126 +- 0,0012 | -0,0095 +- 0,0018 | -0,001178 | 0,15598 |

- Die Streuung von y je Saat haengt nicht von k ab (0,0013 bis 0,0015), wie fuer Kipprauschen erwartet. Das Signal
  waechst wie k^2. Deshalb traegt das groesste k die Steigung, und der Einzelwert beim kleinsten k ist 20-mal
  verrauschter als c.
- Bei N = 16 000 ist die Streuung je k doppelt so gross (0,0028 bis 0,0030; S = 0,25: 0,0056 bis 0,0058).
- Bilder:
  - lauf-69/bild-konform.png: y gegen k^2 mit Fits; Steifigkeit/k^2 gegen k mit festem Netz und Polyakov-Linie
  - lauf-69/bild-streuung.png: c je Saat, Streuung von y je k
  - lauf-69/bild-kippen.png: Kantenkippen und negative Gewichte gegen s

### 3.3 Netze im Hauptlauf [E]

- **Kippen:** Bei S = 0,5 sind 19 % der Kanten gegenueber dem Grundnetz neu, bei S = 0,25 etwa 11 % (Mittel ueber alle
  Bildnetze 16,4 %).
- **Abweichung vom physikalischen Delaunay (koord):** negative Kotangens-Gewichte im Mittel 0,084 %, hoechstens 0,31 %
  der Kanten (3 104 Bildnetze). Die Summe der negativen Gewichte betraegt im extremsten Netz -1,98.
- **intr gegen koord** (16 Saaten, 256 Netze): Kippen dort, wo es das Gewicht verbessert, aendert die Saatmittel von y
  um hoechstens 3,4e-5 und c um -0,0004 (0,1 SE).

## 4. Kontrollen

- **Tor (PLAN Abschnitt 6): bestanden.** Alle 3 104 Bildnetze, die 256 intr-Netze und alle Grundnetze erfuellen Euler,
  E = 3N, F = 2N, "jede Kante in genau zwei Dreiecken", Orientierung > 0, Koordinatenflaeche = L^2, physikalische
  Flaechen > 0 und laengste Kante < L/4. Jede LU hatte U_ii > 0 und perm_r = perm_c; das Newton-Residuum von psi
  war hoechstens 8,9e-16. K1 bis K4 unter den Schwellen (unten).
- **K1 (Abbildung psi):**
  - Newton-Residuum 8,9e-16 nach 5 bis 6 Schritten.
  - Momente <e^(-2 sigma)> und <cos(k.x)> der Bildpunkte gegen 1/I0(2s) und I1(2s)/I0(2s): z-Werte <= 0,34
    (s = +-0,25 und +-0,5; kint = (2,0) und (3,3); N = 64 000).
  - Die Querkoordinate bleibt auf 2,2e-15 unveraendert.
  - KS * sqrt(N) = 1,09 bzw. 0,75, bei allen s gleich: psi bildet die Grundphasen exakt auf die Verteilungsfunktion ab.
- **K2 (Randstreifen-Delaunay):** Dreiecksmengen gleich der 9-Kopien-Fassung aus INDUZIERT-ZUFALL-2D (N = 4 000 und
  16 000) und gleich einer 9-Kopien-Triangulierung der Bildpunkte bei s = 0,5. Gamma stimmt auf alle Stellen.
- **K3 (Laengen):**
  - Die Geodaeten-Formel zweiter Ordnung trifft die numerisch minimierte Weglaenge auf <= 2,4e-4 relativ, bei
    abs(s) k l bis 0,51.
  - Mittelpunktsregel und Eckenregel liegen bis 1,2e-2 bzw. 1,1e-2 daneben.
- **K4 (log det'):** LU gegen dichte slogdet und Eigenwerte <= 3,4e-13 absolut bei Gamma = 286 (1e-15 relativ).
  Das gilt auch mit 14 negativen Gewichten (koord) und nach dem Kippen (intr).
- **K5 (Kantenkippen gegen s, Saat 990), neue Kanten gegenueber s = 0 (koord):**

| s | N = 16 000 (E = 48 000) | N = 64 000 (E = 192 000) |
|---|---|---|
| 1e-4 | 1 bis 2 | 5 bis 6 |
| 1e-3 | 16 bis 23 | 90 bis 94 |
| 1e-2 | 194 bis 220 | 857 bis 900 |
| 0,1 | 2 171 bis 2 206 | 8 595 bis 8 802 |
| 0,5 | 9 225 bis 9 330 (19 %) | 36 611 bis 36 944 (19 %) |

  - Die Spannen gehen ueber die vier k (abs(k) = 0,05 bis 0,3). Das Kippen haengt also kaum von k ab und waechst
    linear in s, etwa 1,4 neue Kanten je Punkt und Einheit s.
  - Negative Kotangens-Gewichte mit physikalischen Laengen bei s = 0,5 (Abweichung vom Delaunay der physikalischen
    Metrik): 2 / 12 / 42 / 122 (N = 16 000) und 12 / 47 / 208 / 520 (N = 64 000) fuer abs(k) = 0,05 / 0,1 / 0,2 /
    0,3, hoechstens 0,27 % der Kanten.
  - Nach dem Kippen (intr) bleiben davon 83 bis 100 % (Vierecke, deren Kruemmungsdefekt groesser ist als ihr Abstand vom
    Kozirkularen).
- **ID0 je Saat:** Die Eckenregel auf festem Netz gibt die Werte von INDUZIERT-ZUFALL-2D (Saaten 0 bis 2, N = 64 000,
  n = 2, 0 und 90 Grad) bitgleich wieder (relative Abweichung 0 in allen sechs Faellen). Netzbau mit Randstreifen,
  Netz und LU sind also dieselben.
- **Festes Netz, Laengenregeln (beschreibend, Saatmittel ueber 3 Saaten und beide Achsen):**

| abs(k) | geo (Richardson, Urteil ID0) | Ecken | Mittelpunkt | geo, S = 0,5 |
|---|---|---|---|---|
| 0,0497 | 0,15899 | 0,15902 | 0,15906 | 0,15900 |
| 0,0993 | 0,15872 | 0,15869 | 0,15885 | 0,15875 |
| 0,199 | 0,15763 | 0,15764 | 0,15829 | 0,15775 |
| 0,298 | 0,15598 | 0,15604 | 0,15753 | 0,15625 |

  - Die Laengenregel aendert c auf dem festen Netz um hoechstens 0,0016 (Mittelpunkt bei abs(k) = 0,3). Das ist ein
    O(k^2)-Effekt, wie in PLAN Abschnitt 2 erwartet.
  - Das S-Schema mit S = 0,5 trifft auf festem Netz den Richardson-Wert auf <= 0,0003. Grosses S verfaelscht dort also
    nichts Wesentliches.
  - Die Fit-Regel (y = a + c k^2 ueber diese vier k) ergaebe auf dem festen Netz etwa c = 0,1558 und a = 3e-5 (von Hand
    aus den Tabellenwerten gerechnet, nicht vom eingefrorenen Code). Das k^4-Glied
    (c(k) faellt um 0,003 bis abs(k) = 0,3) verschiebt die Fit-Steigung um -0,0032 gegen den Wert bei k -> 0.

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - c haette positiv bleiben koennen, etwa durch nicht kovariante Reste aus Koordinaten-Delaunay oder Laengenregel,
    oder nahe +0,159 liegen.
  - a haette ungleich 0 sein koennen.
  - ID0 haette am neuen Netzbau (Randstreifen) oder an der neuen Laengenregel scheitern koennen.
  - Das Kipprauschen haette "nicht auswertbar" ergeben koennen.
- **L2 (Gegenprobe):**
  - Eckenregel auf festem Netz bitgleich zu INDUZIERT-ZUFALL-2D; K1 bis K4.
  - Zwei N, zwei S, zwei Richtungen.
  - koord gegen intr (wo moeglich physikalisch Delaunay).
  - Fit mit und ohne Achsenabschnitt, mit k^4-Glied, Einzelwerte je k.
- **L3 (Numerik):** log det' 1e-15 relativ, Laengen 2,4e-4. Statistisch: SE von c 0,0012 (9 % von Polyakov),
  Saatstreuung 0,009 je Saat.
- **L4 (schon bekannt):**
  - Polyakov 1981; Formel fuer log det' unter konformer Aenderung mit Flaechenglied log A (Alvarez 1983;
    Osgood, Phillips, Sarnak 1988) [L].
  - "Zahl = Volumen" und Poisson-Streuung sind das Grundprinzip der Kausalmengen (Bombelli, Lee, Meyer, Sorkin 1987)
    [L].
  - Zufallsgitter mit Poisson-Punkten und Delaunay/Voronoi: Christ, Friedberg, Lee 1982 [L]. Ob dort schon Punkte mit
    Dichte nach sqrt(g) fuer gekruemmte Hintergruende vorgeschlagen sind, weiss ich nicht sicher [L?].
  - Diskrete Polyakov-Formeln fuer Diskretisierungen flacher Flaechen (Kenyon um 2000 fuer isoradiale Graphen; Finski
    um 2020) [L?].
  - Ob die konforme Anomalie fuer Poisson-Delaunay-Netze mit Streuung nach physikalischer Flaeche schon gerechnet ist,
    weiss ich nicht [L?].
  - 2D-Gravitation aus dynamischen Triangulierungen (David 1985, Kazakov 1985, KPZ 1988) [L]. Das ist ein anderes
    Ensemble: Gewicht det^(-1/2) und Summe ueber Triangulierungen, hier dagegen das gequenchte Mittel ueber
    Poisson-Netze.
- **L5 (Messbezug):** keiner (2D, euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Kleines s0 (Brief):**
  - "So klein, dass wenige Kanten kippen" hiesse s0 <~ 1e-4 (1 bis 6 Kippungen, K5).
  - Dann misst die Differenz die Scher-Steifigkeit des festen Netzes plus seltene, grosse Knicke, mit einer Varianz
    ~ 1/s0.
  - Gerechnet wurde S = 0,5. Etwa 19 % der Kanten kippen; die Kopplung bleibt erwartungstreu (K1).
  - Auf festem Netz trifft das S-Schema den Richardson-Wert auf <= 0,0003 (Abschnitt 4).
- **[K2] Flaechenglied:**
  - Bei fester physikalischer Dichte waechst die erwartete Punktzahl wie A I0(2s). Hier blieb N fest.
  - Weil K skaleninvariant ist, wirkt eine globale Dichteaenderung nicht, und ein Flaechenglied ist nicht zu erwarten
    [M].
  - Gemessen: a = +0,00028 +- 0,00017 (1,6 SE). Die Regel der Karte (Abzug per Ausgleich ueber k) wurde trotzdem
    angewandt.
- **[K3] "kleinstes k":**
  - Nach Abzug des Flaechenglieds gibt es keinen Einzelwert bei einem k; geurteilt wurde die Steigung ueber
    abs(k) = 0,05 bis 0,3.
  - Der Kartenwortlaut (Einzelwert beim kleinsten k) ist mitberichtet: -0,014 +- 0,025, nicht auswertbar; noetig
    waeren etwa 10 700 Saaten bei N = 64 000.
- **[K4] Feste Punktzahl statt Poisson:** wie INDUZIERT-ZUFALL-2D; noetig fuer gemeinsame Zufallszahlen.
- **[K5] Delaunay in Koordinaten:**
  - Kartenwortlaut, so gerechnet. Die Abweichung vom Delaunay der physikalischen Metrik ist klein (K5).
  - Die Variante intr (wo moeglich gekippt) aendert c um -0,0004 (0,1 SE, 16 Saaten).
- Kartenfehler, die ein Urteil aendern, habe ich nicht gefunden. [K3] ist eine Lesart; beide Lesarten sind berichtet.

## 6. Selbstanzeigen

1. **Werte vor dem Einfrieren gesehen:**
   - In der Probe p1 (10 Rauchsaaten, N = 16 000) sah ich c = -0,0093 +- 0,0067, dazu y-Werte aus r1, r2 und r3
     (PLAN Abschnitt 11).
   - ID2 war damit absehbar; ID1 und ID3 waren als Tendenz sichtbar.
   - Die Schwellen sind die der Karte. Die Urteils- und Rauschregeln standen im Auswertungscode, bevor p1 lief.
2. **S = 0,5 nach Rauchlaeufen gewaehlt:** nach r1 (y-Werte zweier Saaten gesehen) und dem Rauschvergleich in r2.
   S = 0,25 laeuft bei N = 16 000 beschreibend mit.
3. **Fehler im eigenen Code vor dem Einfrieren:**
   - Die erste Fassung von intr kippte bedingungslos und pendelte (r1).
   - Berichtigt zur Regel "nur verbessern"; intr ist seitdem nur beschreibend.
   - Nach der Probe p1 habe ich die Regel "mindestens 16 Saaten bei N = 64 000" in den Auswertungscode eingefuegt
     (stand im Plantext, haengt nicht von Werten ab).
4. **Nach dem Einfrieren:**
   - Kein Code geaendert.
   - Waehrend der Hauptlaeufe habe ich einmal per jq auf der .69 in die fertigen Saaten geschaut (44 Saaten,
     Zwei-Punkt-Steigung -0,0129). Code, Regeln und Saatzahlen blieben unveraendert.
   - bild-kippen.png hat eine abgeschnittene Achsenbeschriftung und sich wiederholende Farben (eingefrorener Code;
     nur Darstellung).
5. **Abweichungen vom Brief:**
   - grosses S statt kleinem s0 ([K1])
   - feste Punktzahl ([K4])
   - periodische Delaunay-Triangulierung ueber Randstreifen statt 9 Kopien; gleichwertig nach K2
6. **Von Hand gerechnet:** die Fit-Steigung des festen Netzes (0,1558, Abschnitt 4) aus den Tabellenwerten, nicht vom
   eingefrorenen Code.
7. **Spuren und Laeufe:**
   - cpu3 und cpu4, nie mehr als zwei zugleich.
   - 19 Starts: 7 Rauch (mit Probe p1), 11 Haupt, 1 Auswertung. Der laengste Hauptlauf dauerte 462 s.
   - Je Spur liefen die Starts nacheinander in einer ssh-Sitzung, mit tee in Protokolldateien. Kein nohup, nichts im
     Hintergrund auf der .69.
   - Kein Python-Start ausserhalb des Starters, keine Versionsprobe.
   - Auf der .69 ausserhalb des Starters: mkdir, cp, mv, ls, sha256sum, date und jq (Lesen der JSON-Dateien).
8. **Lokal:**
   - Kein python, awk oder perl.
   - Benutzt: jq, sed, grep, sha256sum, date, ssh, scp, dazu cp, mv, mkdir, ls, cat, head, tail, cut, tr und wc
     (Textwerkzeuge ausserhalb der genannten Liste, keine Interpreter).
   - Ein "sleep 45" wurde vom Werkzeug abgewiesen und lief nicht.
9. **Scratchpad:**
   - Ich habe nichts in den Scratchpad der Leitung geschrieben.
   - Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien unter /tmp/claude-1000/.../tasks/ an.
     Meine Ausgaben gingen per Umleitung in den Kartenordner; diese Dateien sind leer oder enthalten nur Zeitstempel.
10. **Zeitbox:** Start 07:07:51 CEST, Text ab 08:10:05 CEST, Abgabe 08:13:32 CEST, also innerhalb von 120 min.

## 7. Bedeutung

- **Ausgeloest ist der vorab festgelegte Kartenzweig "ID1 und ID3 treffen ein":**
  - "Zahl = Volumen" stellt die geometrische Antwort her.
  - Der grosse Gitterterm war ein Artefakt des festen Netzes.
  - Das stuetzt die Kausalmengen-Seite von Finns Weiche, als 2D-euklidisches Modell und nur fuer die konforme Mode.
- **Was genau gezeigt ist [E]:**
  - Gleiche Grundpunkte, gleiche Materie, gleiche Konvention. Festes Netz: +0,159. Streuung nach Flaeche:
    -0,0123 +- 0,0012.
  - Der Unterschied von 0,171 (13-mal Polyakov) kommt allein daher, wie die Punkte in der gekruemmten Flaeche
    verteilt sind.
  - Die Antwort ist ein Mittel ueber Netze: gequenchtes Mittel von log det' ueber Poisson-Delaunay-Netze mit dem Mass
    "gleichverteilt in der physikalischen Flaeche".
  - Ein einzelnes Netz ist weit davon entfernt: Je Saat streut c um 0,009 (N = 64 000), weil beim Neuvernetzen etwa
    19 % der Kanten kippen.
  - INDUZIERT-ZUFALL-2D hatte ueber Netze mit Punkten gleichverteilt in Koordinaten gemittelt und +0,159 erhalten.
    Entscheidend ist also das Mass "Zahl = Volumen", nicht das Mitteln allein.
- **Mechanismus [H, M]:**
  - Auf festem Netz ist die physikalische Punktdichte rho_0 e^(-2 sigma). Die Abschneidelaenge wandert mit der Mode.
  - Lokale Glieder in log rho sind dann erlaubt. Zum Beispiel gibt der Waermeleitungskoeffizient a_1 = R/(24 pi)
    [L] das Glied (1/(48 pi)) Integral sqrt(g) R log eps^2. Mit eps^2 ~ e^(2 sigma) ist das
    +(1/(12 pi)) Integral (grad sigma)^2, also +0,027 in c [M].
  - Der Rest des Unterschieds zwischen festem Netz und Polyakov (0,172 - 0,027 = 0,145) sind nicht universelle Glieder
    in grad log rho.
  - Bei Streuung nach Flaeche ist rho konstant. Diese Glieder werden dann konstant oder topologisch: Integral sqrt(g) R
    ist auf dem Torus 0. Uebrig bleibt der universelle, nichtlokale Polyakov-Teil.
  - Ein Flaechenglied fehlt, weil N fest und K skaleninvariant ist [M]. Gemessen: a bei 1,6 SE.
- **Grenzen:**
  - **2D ist ein Sonderfall.** Integral sqrt(g) R ist topologisch. Geprueft ist also: keine nicht kovarianten
    k^2-Glieder, und die universelle Zahl stimmt.
    - In 4D ist der Einstein-Term selbst lokal und nicht universell (Koeffizient ~ Wurzel der Abschneidedichte
      [L Sakharov]).
    - Ein kovariantes Ensemble legte dort die Tensorform fest (c0s/c2 = -2, INDUZIERT-1 IN3), nicht die Groesse [H].
  - **Nur die konforme Mode.** Knotenverschiebungen (Umbenennungen) sind hier nicht gerechnet; INDUZIERT-ZUFALL-2D fand
    sie auf festem Netz 600- bis 3600-mal zu steif.
    - [H, M] Im Dichte-Ensemble haengt die Verteilung des physikalischen Netzes nur von der Geometrie ab.
      Umbenennungen sollten im Mittel nichts kosten, bis auf die kleine Abweichung des Koordinaten-Delaunay.
  - **Genauigkeit:**
    - Sicher ist "negativ und Polyakov-gross", mit 148 SE Abstand zu +0,159.
    - Die 30-%-Aussage haengt an der Lesart: Steigung ueber das Fenster 0,92 P; mit a = 0 erzwungen 0,61 P +- 0,17 P;
      mit k^4-Glied 0,54 P +- 0,45 P.
    - Ein k^4-Glied wie auf dem festen Netz verschoebe den Grenzwert k -> 0 auf etwa 0,7 P.
  - Eine Schleife, freies masseloses Skalarfeld, euklidisch, feste Punktzahl, Delaunay in Koordinaten (Abweichung
    gemessen und klein).
- **Naechste Schritte [H]:**
  - (a) Knotenverschiebungen im Dichte-Ensemble: Ist ihre Steifigkeit im Mittel null?
  - (b) Grenzwert k -> 0 genauer: mehr Saaten bei abs(k) = 0,1 bis 0,2. Der Aufwand waechst wie 1/k^4.
  - (c) 4D: Poisson-Delaunay nach Volumen gestreut; trifft die induzierte Steifigkeit c0s/c2 = -2?
  - (d) Gewichtetes Mittel mit det^(-1/2) als Schritt zur Summe ueber Netze (dynamische Triangulierungen).

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-073639, EINGEFROREN-SHA256.txt
- code/:
  - dichte2d.py: Abbildung psi, periodisches Delaunay, Geodaeten-Laengen, Kippen (intr), Modi kontrolle, fest, dichte
  - dichte_auswertung.py: Tor, Urteile, Tabellen, Bilder
  - zufall2d.py und induziert.py: unveraendert aus INDUZIERT-ZUFALL-2D
  - je mit Kopien *.eingefroren-20261004-073639
- lauf-69/:
  - kontrolle.json, fest-N64000-s0.json
  - dichte-N64000-s{0,11,22,33,44,55}.json, dichte-N16000-s{0,32}.json, intr-N16000-s100.json
  - je mit .log; kette-cpu3.log, kette-cpu4.log
  - auswertung.json (Urteile), auswertung.log, PRUEFSUMMEN.txt (.69)
  - Bilder: bild-konform.png, bild-streuung.png, bild-kippen.png
- rauch-69/: kontrolle-r1/-r2, dichte-r1 bis -r4 (JSON und Logs), p1/ (Probe der Auswertung mit Probebildern)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-induziert-dichte/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir haben die Punkte des Netzes so verteilt, dass auf jedes gleich grosse Stueck der gebogenen Flaeche gleich viele
Punkte kommen ("so viele Punkte wie Flaeche"), und das Netz bei jeder Verbiegung neu geknuepft. Dann haben wir
gemessen, wie stark sich das Zittern der Materie gegen das Verbiegen wehrt. Beim festen Netz war diese Antwort
zwoelfmal zu gross und hatte das falsche Vorzeichen; mit der Verteilung nach Flaeche kommt im Rahmen der
Messgenauigkeit die bekannte richtige Zahl (Polyakov) heraus. Es hilft also: Der grosse Fehler kam daher, dass beim
festen Netz die Punkte beim Verbiegen dichter oder duenner wurden. Gezeigt ist das bisher nur in einer
zweidimensionalen Modellwelt und nur fuer eine Art von Verbiegung, nicht schon fuer echte Schwerkraft in vier
Dimensionen.
