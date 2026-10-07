# INDUZIERT-DICHTE-2D-GROB: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 09:01:24 CEST, Code ab 09:11:37, Plantext ab 09:17:30 CEST.
  - Rauchlaeufe und Proben 07:12:27 bis 07:16:56 UTC (PLAN Abschnitt 10).
  - Eingefroren 09:19:15 CEST: PLAN.md.eingefroren-20261004-091915, Code-Kopien *.eingefroren-20261004-091915,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 07:19:23 bis 07:39:23 UTC (7 Bloecke, alle rc = 0), Auswertung 07:39:34 bis 07:40:53 UTC (rc = 0).
  - Text ab 09:42:33 CEST.
- Plan und Code sind nach dem Einfrieren unveraendert. Die sha256 stimmen lokal und auf der .69.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64; Spuren cpu und cpu7). Gerechnet
  ist euklidisch, eine Schleife, ein freies masseloses Skalarfeld. Synthetisch, keine Messdaten.
- **Kennzeichen:**
  - [E] hier gerechnet, [M] eigene Mathematik, [F] Festlegung im Plan, [K] Kartenpunkt, [H] Hypothese
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen (hier keine Quelle abgerufen)
- **Bezeichnungen:**
  - eps ist der mittlere Netzabstand, x = (k eps)^2, y = Gamma''/N (Gamma'' je Punkt).
  - Modell der Karte: y = a + c x + d x^2. c ist die konforme Steifigkeit fuer k -> 0, d das k^4-Glied in
    Netzabstands-Einheiten.
  - P = -1/(24 pi) = -0,013263 (Polyakov).
  - Datensaetze:
    - M64 und M16: Hauptlauf, eps = 1, N = 64 000 bzw. 16 000.
    - G: Lauf (a), eps = 2, N = 16 000 auf L = sqrt(64 000), 240 neue Saaten.
    - B: Kontrolle (b).

## 1. Ergebnis zuerst

1. **Grenzwert k -> 0 [E]:** c(0) = **-0,01426 +- 0,00095 = 1,075 P +- 0,071 P**.
   - Gemeinsamer Ausgleich ueber Netzabstand 1 (M64, M16; 130 Saaten) und Netzabstand 2 (G; 240 Saaten).
   - Abstand zu Polyakov: 7,5 %, also 1,05 SE. Das Modell passt (chi^2 = 7,9 bei 9 FG, p = 0,55).
2. **Das k^4-Glied ist bestimmt und positiv [E]:** d = **+0,0215 +- 0,0025**.
   - Das Vorzeichen ist dem festen Netz entgegengesetzt (dort etwa -0,035).
   - Die Fenster-Steigung des Hauptlaufs (-0,0123 = 0,92 P) war die Steifigkeit bei k eps ~ 0,3. Sie lag um
     0,0928 d = 0,0020 zu nah an null.
   - Unmittelbar sichtbar bei gleichem k in Torus-Einheiten: Auf dem groben Netz ist die Fenster-Steigung
     -0,0062 +- 0,0003, auf dem feinen -0,0123 +- 0,0012.
3. **Urteile:** IG0, IG1, IG2 und IG3 sind eingetroffen, nach Regel und nach Kartenwortlaut. Ausgeloest sind die
   vorab festgelegten Zweige "IG2 trifft ein" und "IG3 trifft ein" (Abschnitt 7).
4. **Kontrollen [E]:**
   - (b) ist bitgleich zum Hauptlauf (512 von 512 Zeilen).
   - Die Skalenprobe ist bitgleich: Lauf (a) ist exakt das skalierte Hauptlauf-Netz.
   - Tor: 4 864 Bildnetze ohne Fehler.
   - G allein, mit unabhaengigen Saaten: c(0) = -0,0141 +- 0,0013, d = +0,0213 +- 0,0035.
   - Kovarianz-Lesarten und Jackknife aendern c(0) um hoechstens 0,0001 bzw. den SE um 7 %.
5. **Grenze:**
   - c(0) ist eine Extrapolation mit k^0-, k^2- und k^4-Glied bis k eps = 0,6.
   - Mit zusaetzlichem k^6-Glied wird c(0) = -0,0121 +- 0,0025 (0,91 P +- 0,19 P). Das k^6-Glied selbst ist
     0,05 +- 0,05, also unauffaellig. Die 15-%-Aussage ist dann aber nicht mehr gesichert.
   - Weiter gilt: 2D, euklidisch, gequenchtes Netzmittel, nur die konforme Mode, S = 0,5.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/grob_auswertung.py; Werte in lauf-69/auswertung.json (unbearbeitet).
Vorbedingungen erfuellt: Tor (a) und (b) bestanden, IG0 eingetroffen, 240 Saaten in (a), Modellprobe p = 0,548 >= 0,01.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| IG0 | Kontrolle (b): Kopie-Code mit L = sqrt N gibt den Hauptlauf (N = 16 000: -0,0131 +- 0,0022) innerhalb 2 SE wieder | 90 % | **eingetroffen** | eingetroffen | c_b = -0,013110 +- 0,002218 (64 Saaten) = c_M16; Abstand 0. Saat fuer Saat bitgleich (512 Zeilen: Gamma(0), Gamma(+-S), D, y) |
| IG1 | d (k^4-Glied) ist auf <= +-0,01 bestimmt | 70 % | **eingetroffen** | eingetroffen | d = +0,0215, SE_U = 0,0025 (Birge-Faktor 1); Schwelle 0,01 |
| IG2 | [H] Grenzwert k -> 0 zwischen 0,7 P und 1,2 P | 60 % | **eingetroffen** | eingetroffen | c(0) = -0,01426 +- 0,00095 = 1,075 P; Band [-0,01592; -0,00928]; SE <= 0,00332 |
| IG3 | [H] Grenzwert innerhalb 15 % von P | 35 % | **eingetroffen** | eingetroffen | Abweichung 7,5 % (1,05 SE); Band [-0,01525; -0,01127]; SE 0,00095 <= 0,00199 |

- **Lesart IG0 [K3]:** Mit denselben Saaten war Bitgleichheit erwartet und festgelegt. Die Probe zeigt, dass die Kopie
  mit L-Option bei L = sqrt N exakt der eingefrorene Code ist.
- **IG3 haengt am Modell [K5]:** Geurteilt ist der vorab festgelegte Ausgleich mit k^4 und ohne k^6.
  - Die Modellprobe gibt keinen Grund fuer ein k^6-Glied.
  - Mit k^6 waere der SE 0,0025 statt 0,00095. IG3 waere dann "nicht auswertbar", IG2 weiter im Band (0,91 P).

**Agenten-Vorhersagen** (PLAN Abschnitt 9, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| B1 (90 %) | Tor besteht in (a) und (b) | **eingetroffen**: 3 840 + 1 024 Bildnetze und alle Grundnetze ohne Fehler |
| B2 (97 %) | (b) in allen 64 Saaten bitgleich | **eingetroffen**: 512 von 512 Zeilen |
| B3 (75 %) | Modellprobe p >= 0,01 | **eingetroffen**: p = 0,548 |
| B4 (80 %) | Saatstreuung G bei k eps = 0,099 und 0,199 wie M16 (Faktor 0,8 bis 1,25) | **eingetroffen**: 0,98 und 1,06 |
| B5 (55 %) | d < 0 (wie festes Netz) | **nicht eingetroffen**: d = +0,0215 +- 0,0025 |

## 3. Tabellen [E]

### 3.1 Gemeinsamer Ausgleich und Lesarten (Netzabstands-Einheiten)

| Lesart | c(0) | c(0)/P | d | chi^2/FG (p) |
|---|---|---|---|---|
| **Urteil:** 12 Zellen, freie Kovarianz je Datensatz, gemeinsames a | **-0,01426 +- 0,00095** | **1,075** | **+0,0215 +- 0,0025** | 7,9/9 (0,55) |
| eigenes a je Datensatz | -0,01425 +- 0,00095 | 1,074 | +0,0216 +- 0,0025 | 4,8/7 (0,68) |
| Kovarianz nach Versatz-Modell (sigma^2 I + tau^2 J) | -0,01430 +- 0,00092 | 1,078 | +0,0217 +- 0,0025 | 6,8/9 (0,66) |
| feste Saatversaetze (Achsenabschnitt je Saat) | -0,01422 +- 0,00092 | 1,072 | +0,0216 +- 0,0025 | - |
| nur N = 16 000 (M16 + G, ohne M64) | -0,01437 +- 0,00122 | 1,084 | +0,0219 +- 0,0032 | 3,4/5 (0,64) |
| G allein, je Saat a + c x + d x^2 | -0,01409 +- 0,00135 | 1,062 | +0,0213 +- 0,0035 | - |
| Fenster k eps <= 0,40 (ohne G bei 0,60) | -0,01281 +- 0,00196 | 0,966 | +0,011 +- 0,013 | 7,2/8 (0,52) |
| mit k^6-Glied (f = +0,046 +- 0,048) | -0,01205 +- 0,00249 | 0,909 | -0,001 +- 0,024 | 7,0/8 (0,54) |
| ohne k^4, alle k | -0,00656 | 0,49 | - | 79,7/10 (6e-13) |
| ohne k^4, Fenster k eps <= 0,40 | -0,01119 +- 0,00061 | 0,84 | - | 7,9/9 (0,54) |

- Jackknife ueber Saaten (geschichtet, Kovarianz je Durchgang neu): SE(c) = 0,00102 und SE(d) = 0,0027. Das ist das
  1,07- bzw. 1,06-Fache des GLS-Werts.
- c und d sind im Urteilsmodell stark korreliert (-0,96). Das Mittel a = +0,00018 +- 0,00012 liegt 1,6 SE von 0.
- **Lesart:**
  - Alle Lesarten mit dem vollen k-Hebel geben c(0) = 1,06 P bis 1,08 P.
  - Lesarten mit weniger Hebel (Fenster 0,4 oder k^6 frei) geben 0,91 P bis 0,97 P mit doppeltem bis dreifachem SE.
    Sie sind innerhalb von 1 SE vertraeglich.
  - Ohne k^4 passt das Modell ueber alle k nicht (p = 6e-13). Das k^4-Glied ist also noetig.
  - Im kleinen Fenster passt das Modell ohne k^4 zwar, verschiebt c aber auf 0,84 P, wegen des Hebels von d.

### 3.2 Je Zelle (y = Gamma''/N, Saatmittel +- SE; c(k) = (y - a)/x mit a = +0,00018 aus dem Ausgleich)

| Satz | k eps | y | Std je Saat | c(k) | Modell c + d x |
|---|---|---|---|---|---|
| M64 (66) | 0,050 | +0,000244 +- 0,000170 | 0,00138 | +0,025 +- 0,069 | -0,0142 |
| M64 | 0,099 | +0,000112 +- 0,000184 | 0,00149 | -0,007 +- 0,019 | -0,0140 |
| M64 | 0,199 | -0,000124 +- 0,000179 | 0,00145 | -0,0078 +- 0,0045 | -0,0134 |
| M64 | 0,298 | -0,000841 +- 0,000156 | 0,00126 | -0,0115 +- 0,0018 | -0,0124 |
| M16 (64) | 0,050 | +0,000441 +- 0,000380 | 0,00304 | +0,10 +- 0,15 | -0,0142 |
| M16 | 0,099 | +0,000159 +- 0,000370 | 0,00296 | -0,003 +- 0,038 | -0,0140 |
| M16 | 0,199 | -0,000053 +- 0,000346 | 0,00277 | -0,0060 +- 0,0088 | -0,0134 |
| M16 | 0,298 | -0,000778 +- 0,000370 | 0,00296 | -0,0108 +- 0,0042 | -0,0124 |
| G (240) | 0,099 | -0,000225 +- 0,000187 | 0,00290 | -0,041 +- 0,019 | -0,0140 |
| G | 0,199 | -0,000544 +- 0,000190 | 0,00294 | -0,0184 +- 0,0048 | -0,0134 |
| G | 0,397 | -0,001765 +- 0,000184 | 0,00285 | -0,0123 +- 0,0012 | -0,0109 |
| G | 0,596 | -0,002370 +- 0,000184 | 0,00285 | -0,0072 +- 0,0005 | -0,0066 |

- Die SE je Zelle enthalten den Versatz je Saat. Er ist innerhalb eines Datensatzes fuer alle k derselbe
  (Korrelation zwischen den k in G 0,80 bis 0,86).
- Die Zellen eines Datensatzes schwanken deshalb gemeinsam. Bei kleinem k wird das durch 1/x stark vergroessert. Der
  Ausgleich nutzt die volle Kovarianz.
- G liegt bei k eps = 0,099 und 0,199 um z = -0,93 bzw. -1,24 neben M16 (gleiches N, gleiches k eps, unabhaengige
  Saaten, nach Skalengleichheit dasselbe Ensemble): vertraeglich.
- Bilder:
  - lauf-69/bild-ck-gegen-k2.png: links y gegen (k eps)^2 mit Ausgleichskurve und Polyakov-Linie. Rechts c(k)
    gegen (k eps)^2 fuer beide Dichten mit Ausgleichsgerade c + d x, c(0) +- SE, Polyakov-Linie und IG2-Band.
  - lauf-69/bild-streuung-grob.png: Saatstreuung je k.

### 3.3 Fenster-Steigungen bei gleichen k in Torus-Einheiten (eingefrorene Regel: je Saat a + c k^2 ueber die vier k)

| Datensatz | Netzabstand | Fenster-Steigung | Hebel auf d | Modell c(0) + Hebel d |
|---|---|---|---|---|
| M64 (Hauptlauf) | 1 | -0,01226 +- 0,00115 | 0,093 | -0,01227 |
| M16 (Hauptlauf) | 1 | -0,01311 +- 0,00222 | 0,093 | -0,01227 |
| G (Lauf a) | 2 | -0,00617 +- 0,00029 | 0,371 | -0,00629 |

- Differenz G - M64: +0,0061 +- 0,0012 (5,1 SE). Daraus d = +0,0219 +- 0,0043, als Zwei-Punkt-Schaetzung ohne
  gemeinsamen Ausgleich.
- Bei derselben Wellenlaenge halbiert das doppelt so grobe Netz die gemessene Fenster-Steigung. Die Fenster-Steigung
  ist also kein Kontinuumswert. Der Grenzwert liegt auf der anderen Seite des Hauptlauf-Werts als das feste Netz
  vermuten liess.

### 3.4 Rauschen und Saatzahl

| Datensatz | Saaten | Rest sigma (je k) | Versatz tau (je Saat) | Versatzanteil |
|---|---|---|---|---|
| M64 | 66 (0 bis 65) | 0,00065 | 0,00124 | 78 % |
| M16 | 64 (0 bis 63) | 0,00122 | 0,00267 | 83 % |
| G | 240 (200 bis 439) | 0,00120 | 0,00262 | 83 % |

- Die Streuung von y je Saat haengt in G bis k eps = 0,6 nicht von k ab (0,00285 bis 0,00294).
- Noetige Saaten in G fuer SE(d) = 0,005 (gemeinsamer Ausgleich, Kovarianz skaliert): 16; fuer 0,01: 4.
  Fuer G allein: 117. Vorab geschaetzt waren 16 bzw. etwa 100.
- **Netze im Lauf (a):**
  - Gegenueber dem Grundnetz sind 19,1 % der Kanten neu.
  - Negative Kotangens-Gewichte: im Mittel 0,39 %, hoechstens 1,10 % der Kanten. In (b) sind es 0,10 % und 0,31 %.
    Bei k eps = 0,6 weicht das Koordinaten-Delaunay also staerker vom physikalischen ab; das ist Teil von d.

## 4. Kontrollen

- **Tor: bestanden.**
  - Alle 3 840 Bildnetze in (a), 1 024 in (b) und alle 304 Grundnetze erfuellen die eingefrorenen Pruefungen: Euler,
    E = 3N, F = 2N, jede Kante in genau zwei Dreiecken, Orientierung > 0, Koordinatenflaeche = L^2, physikalische
    Flaechen > 0, laengste Kante < L/4, Grundnetz Delaunay.
  - Jede LU hatte U_ii > 0 und perm_r = perm_c. Das Newton-Residuum von psi war <= 1e-12 (in a-s200 hoechstens
    1,8e-15).
- **IG0 / Kopie-Code:** (b) mit L = sqrt N ist Saat fuer Saat bitgleich zum Hauptlauf N = 16 000. Das gilt fuer alle
  64 Saaten, beide Richtungen und alle vier n, fuer Gamma(0), Gamma(+-S), D und y.
- **Skalenprobe (vor dem Einfrieren, rauch-69/vergleich-a-skala-s0.json):**
  - (a) mit A = 64 000, Saaten 0 und 1, n = 2 und 4, ist bitgleich zu M16 bei derselben Saat und demselben n. Das gilt
    fuer Gamma(0), Gamma(+-S), D und y_eps.
  - Damit sind die Skalengleichheit [M] und der mitskalierte Randstreifen [K2] exakt belegt: Der grobe Lauf ist das
    Hauptlauf-Ensemble bei doppeltem k eps.
- **Unabhaengige Bestaetigung durch G allein:** Die 240 neuen Saaten ohne Hauptlauf geben c(0) = -0,0141 +- 0,0013
  und d = +0,0213 +- 0,0035, beides wie im gemeinsamen Ausgleich.
- **Selbsttest (synthetisch, vor dem Einfrieren):**
  - Wahre Werte a = 3e-4, c = P, d = -0,035, Rauschmodell wie gemessen, 300 Wiederholungen.
  - Zug-Std 0,99 / 1,02 / 1,00; chi^2-Mittel 9,4 bei 9 FG; Fehlalarm der Modellprobe 1,3 %.
  - Ein k^6-Glied 0,5 x^3 wird erkannt (p = 5e-17). Erwartete SE bei 240 Saaten: c 0,00089, d 0,0024; gemessen 0,00095
    und 0,0025.
- **Modellprobe:** p = 0,548, Birge-Faktor 1. Das k^6-Glied ist mit 0,046 +- 0,048 unauffaellig.

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - d haette unbestimmt bleiben koennen (IG1).
  - Das Modell haette an k^6 scheitern koennen (Modellprobe).
  - c(0) haette bei 0,7 P oder darunter liegen koennen, wie der Gegenleser fuer ein k^4 vom festen Netz schaetzte.
  - (b) haette vom Hauptlauf abweichen koennen.
- **L2 (Gegenprobe):** bitgleiche Kontrolle (b) und Skalenprobe; G allein gegen den gemeinsamen Ausgleich; sieben
  Lesarten des Ausgleichs; Jackknife; G gegen M16 bei gleichem k eps.
- **L3 (Numerik):** wie im Hauptlauf (log det' 1e-15 relativ, Laengen 2,4e-4 bei abs(s) k l <= 0,5).
  - Bei k eps = 0,6 ist abs(s) k l fuer lange Kanten groesser als in K3 geprueft. Ein Fehler der Laengenformel
    waere aber ein Gitterglied hoeherer Ordnung in k eps und steckte in d bzw. f.
  - Statistisch: SE(c) = 0,00095 = 7 % von P.
- **L4 (schon bekannt):**
  - Polyakov 1981; die Formel von Osgood, Phillips und Sarnak ist fuer endliches sigma exakt quadratisch [L].
  - "Zahl = Volumen" ist das Grundprinzip der Kausalmengen (Bombelli, Lee, Meyer, Sorkin 1987) [L].
  - Ob die konforme Anomalie fuer nach physikalischer Flaeche gestreute Poisson-Delaunay-Netze schon gerechnet ist,
    weiss ich nicht [L?].
- **L5 (Messbezug):** keiner (2D, euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Skalengleichheit:**
  - Lauf (a) ist rechnerisch N = 16 000 mit L = sqrt N bei n = 2, 4, 8, 12. Die "groebere Dichte" ist dasselbe wie
    doppeltes k eps.
  - Belegt durch die bitgleiche Skalenprobe. Deshalb bekam (a) neue Saaten (200 bis 439).
  - Ein Unterschied zwischen den Dichten kann nur ueber k eps entstehen. Der Ausgleich in Netzabstands-Einheiten ist
    die passende Form.
- **[K2] Randstreifen:**
  - Die Kopie skaliert RAND = 8 mit dem mittleren Abstand. Das ist neben L die einzige inhaltliche Aenderung
    (code/AENDERUNG.diff).
  - Bei L = sqrt N ist das bitgleich (IG0), bei L = sqrt(64 000) exakt das skalierte Netz (Skalenprobe).
  - Die Kartenwortlaut-Fassung mit festen 8 Einheiten (bei eps = 2 nur 4 Abstaende) ist nicht gerechnet.
- **[K3] IG0 mit denselben Saaten:** Bitgleichheit erwartet und eingetreten, Abstand 0.
- **[K4] Rauschregeln IG1 bis IG3** wie ID1 im eingefrorenen Plan. Der Kartenwortlaut (Punktwert im Band) gibt
  dieselben Urteile.
- **[K5] Grenzwert = Achsenabschnitt des Modells mit k^0, k^2 und k^4.** Die Modellprobe besteht. Die Abhaengigkeit
  von dieser Wahl steht in Abschnitt 3.1 (k^6 frei: 0,91 P +- 0,19 P).
- **[K6] "Ausgleich wie eingefroren"** gilt fuer IG0 und die Fenster-Steigungen (Abschnitt 3.3).
- Kartenfehler, die ein Urteil aendern, habe ich nicht gefunden.

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehene Werte:**
   - Gesehen habe ich nur bekannte Hauptlaufwerte. Die Probe der Auswertung (G als Kopie von M64) zeigte c = -0,0066
     +- 0,0038 und d = -0,062. Das ist der k^4-Fit des Hauptlaufs; der Fehler ist durch die doppelte M64 zu klein.
   - Die Rauchlaeufe b-s0 und a-skala-s0 sind bitgleiche Wiederholungen des Hauptlaufs.
   - Werte bei k eps > 0,3 habe ich vor dem Einfrieren weder gerechnet noch gesehen.
2. **Code vor dem Einfrieren berichtigt:**
   - In grob_auswertung.py trat bei der Probe eine Division durch null auf (G = M64-Kopie, gleicher Hebel). Berichtigt
     mit einem Schutz.
   - Der Vergleich G gegen M16 laeuft seitdem nur bei eps = 2.
3. **Nach dem Einfrieren:**
   - Code und Plan sind unveraendert (sha256 lokal und auf der .69 geprueft).
   - Waehrend der Laeufe habe ich per jq die Plausibilitaet von a-s200 und b-s0 geprueft: Flaechen, negative Gewichte,
     l_max, Newton. y-Werte waren nicht dabei.
   - Beim Blick auf den Logkopf von b-s32 sah ich eine y-Zeile (Saat 32, n = 1). Sie ist eine bitgleiche Wiederholung
     eines Hauptlaufwerts.
4. **Abweichungen vom Brief:**
   - Randstreifen mitskaliert [K2].
   - L wird ueber die Torusflaeche gesetzt (Option A, L = sqrt A). So bleibt A = N bei L = sqrt N exakt der
     eingefrorene Wert.
   - (b) mit denselben, (a) mit neuen Saaten [K1, K3].
5. **Spuren und Starts:**
   - Nur cpu und cpu7; 15 Starts (7 Rauch und Proben, 7 Bloecke, 1 Auswertung).
   - Alle Starts endeten mit rc = 0, ausser dem ersten Probe-Versuch der Auswertung vor dem Einfrieren (rc = 1,
     Division durch null, Punkt 2).
   - Der laengste Block dauerte 363 s.
   - Je Spur habe ich den naechsten Block gestartet, waehrend der vorige lief. Er wartete am Lock der Spur und rechnete
     erst danach. Es rechneten nie mehr als zwei zugleich.
   - Je ssh-Aufruf ein Starteraufruf. Einmal liefen die beiden Vergleiche vor dem Einfrieren in einem lokalen Befehl
     nacheinander, je mit eigenem ssh. Das war lokal, keine Kette auf der .69.
6. **Auf der .69 ausserhalb des Starters:** mkdir, cp (Probe-Ordner rauch/probe mit Kopien der Hauptlauf-Dateien,
   nur fuer den Codepfad-Test), mv, ls, sha256sum, jq, du, uptime, date. Kein Python ausserhalb des Starters, keine
   Versionsprobe.
7. **Lokal:**
   - Kein python, awk oder perl.
   - Benutzt: jq, ssh, scp, sha256sum, date, grep, sed, diff, sort mit LC_ALL=C.
   - Ausserhalb der Liste: mkdir, cp, ls, cat, head, tail, tr, comm und timeout (zum Warten auf Blockenden mit
     tail -f), dazu einmal versehentlich uptime lokal.
8. **Scratchpad:**
   - Ich habe nichts in den Scratchpad der Leitung geschrieben.
   - Die Werkzeugumgebung legt fuer Hintergrundbefehle und einen Log-Monitor eigene Ausgabedateien unter
     /tmp/claude-1000/.../tasks/ an. Meine Ausgaben gingen per Umleitung in den Kartenordner.
9. **Zeitbox:** Start 09:01:24 CEST, Text ab 09:42:33 CEST, innerhalb von 90 min (Abgabezeit in der Schlussmeldung).

## 7. Bedeutung

- **Ausgeloest sind die vorab festgelegten Zweige:**
  - "IG2 trifft ein: Das 2D-Ergebnis haelt auch bei kurzer Netzweite relativ zur Welle. 'Zahl = Volumen' gibt
    Polyakovs Antwort in der Groesse."
  - "IG3 trifft ein: Die Aussage darf auf 'Polyakov innerhalb 15 %' verschaerft werden."
- **Was sich gegenueber dem Hauptlauf aendert [E]:**
  - Der Gegenleser hatte recht: -0,0123 war eine Fenster-Steigung bei k eps ~ 0,3, kein Kontinuumswert.
  - Das k^4-Glied ist positiv, nicht negativ wie auf dem festen Netz. Das Hauptlauf-ERGEBNIS hatte nur die Richtung zu
    0,7 P genannt; der Gegenleser hatte beide Vorzeichen offen gelassen.
  - Der Grenzwert liegt auf der anderen Seite von Polyakov als die Fenster-Steigung: 1,075 P +- 0,071 P statt 0,92 P.
    Der Abstand zu P ist etwa gleich gross, aber jetzt ist der Netzfehler gemessen statt nur abgeschaetzt.
  - Die Spanne 0,7 P bis 1,2 P aus dem Gegenlesen ist damit auf 1,00 P bis 1,15 P (1 SE) eingeengt.
- **Gesicherte Aussage:** Fuer das gequenchte Mittel ueber Poisson-Delaunay-Netze mit Punkten nach physikalischer
  Flaeche ist die konforme Steifigkeit eines P1-Skalars fuer k -> 0 gleich -0,0143 +- 0,0010, also Polyakov innerhalb
  15 %. Das gilt in 2D, euklidisch, fuer die konforme Mode, bei S = 0,5 und mit dem Modell k^0 + k^2 + k^4.
- **Vorbehalte:**
  - **k^6:** Mit freiem k^6-Glied ist c(0) = 0,91 P +- 0,19 P. Die Daten verlangen das Glied nicht. Die
    15-%-Aussage haengt aber an dieser Modellwahl, die 0,7-P-bis-1,2-P-Aussage nicht.
  - **S:**
    - d haengt von S ab; R^2-artige Glieder wachsen bei S = 0,5 um etwa den Faktor 1,6 (Gegenlesen 2b).
    - Dass c(0) nicht von S abhaengt, folgt aus der Kovarianz des Ensembles [M, H]. Empirisch ist es nur schwach
      geprueft (Hauptlauf, S = 0,25 bei N = 16 000).
  - **Rahmen:** 2D ist ein Sonderfall (Integral sqrt(g) R topologisch). Knotenverschiebungen sind nicht gerechnet. Der
    Satz "Schwerkraft aus Materie wird moeglich" bleibt eine Hochrechnung [H].
- **Naechste Schritte [H]:**
  - (a) k^6 trennen: Saaten bei k eps = 0,8 (N = 16 000, n = 16) oder ein feineres Netz. Die Skalengleichheit macht
    beides zu Laeufen bei N = 16 000 bzw. 64 000 mit anderem n.
  - (b) S = 0,25 auf dem groben Netz: Haengt nur d von S ab, oder auch c(0)?
  - (c) Knotenverschiebungen im Dichte-Ensemble (wie im Hauptlauf vorgeschlagen).

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-091915, EINGEFROREN-SHA256.txt
- code/:
  - dichte2d_grob.py: Kopie mit L-Option (Diff in AENDERUNG.diff)
  - grob_auswertung.py: Tor, Urteile, Ausgleich, Bitvergleich, Selbsttest, Bilder
  - zufall2d.py und induziert.py unveraendert
  - je mit Kopien *.eingefroren-20261004-091915
- lauf-69/:
  - a-s200 / a-s248 / a-s296 / a-s344 / a-s392.json: Lauf (a), Saaten 200 bis 439
  - b-s0.json, b-s32.json: Kontrolle (b)
  - je mit .log; auswertung.json (Urteile), auswertung.log, PRUEFSUMMEN.txt (.69)
  - Bilder: bild-ck-gegen-k2.png, bild-streuung-grob.png
- rauch-69/:
  - b-s0 und a-skala-s0 (JSON und Logs), vergleich-*.json
  - selbsttest.json, auswertung-probe.json, probe/bild-ck-gegen-k2-probe.png
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-induziert-grob/ (code/, rauch/, lauf/). Der Hauptlauf-Ordner
  runde38-induziert-dichte/lauf wurde nur gelesen.

## 9. Einfach gesagt

Wir haben die Rechnung "so viele Punkte wie Flaeche" noch einmal mit einem doppelt so groben Netz gemacht, um zu sehen,
wie stark das Netz selbst die Zahl verfaelscht. Das Netz verfaelscht tatsaechlich etwas, aber in die andere Richtung
als befuerchtet: Die fruehere Zahl war nicht zu gross, sondern etwas zu klein. Rechnet man den Netzfehler heraus, liegt
der Wert fuer ein unendlich feines Netz 7 Prozent neben der bekannten richtigen Zahl (Polyakov), bei einer
Messunsicherheit von ebenfalls etwa 7 Prozent. Das gute Ergebnis haelt also der genaueren Nachpruefung stand, und jetzt
ist auch der Netzfehler gemessen statt nur geschaetzt. Es gilt aber weiter nur in einer zweidimensionalen Modellwelt
und unter der Annahme, dass der Netzfehler die einfache Form hat, die wir angesetzt haben.
