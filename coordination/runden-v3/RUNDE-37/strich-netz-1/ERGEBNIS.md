# STRICH-NETZ-1: Ergebnis (Runde 41, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 15:59:12 CEST. Schreibtischpruefung ab 16:15:27 CEST, vor jeder Rechnung (PLAN Abschnitt 0).
  - Rauchlaeufe 14:26:53 bis 14:38:12 UTC (PLAN Abschnitt 9).
  - Eingefroren 16:39:11 CEST: PLAN.md.eingefroren-20261004-163911, code/*.eingefroren-20261004-163911,
    EINGEFROREN-SHA256.txt.
  - Hauptlaeufe H01 bis H29: 14:39:27 bis 15:11:49 UTC, alle rc = 0. Bilder H30 15:11:56 bis 15:12:10 UTC,
    Auswertung H31 15:12:10 bis 15:12:12 UTC.
  - Text ab 17:00:13 CEST (date unmittelbar vor der ersten Fassung); letzte Aenderung 17:20:58 CEST.
- **Code nach dem Einfrieren unveraendert:** strichnetz.py b542b386, auswertung.py 6adde7a7, bilder.py 6e8698e5,
  spinnetz.py 460c0af6 (unveraendert aus SPIN-ZUFALLSNETZ-1), induziert.py b3867eac (unveraendert aus INDUZIERT-1).
  lauf-69/PRUEFSUMMEN.txt (auf der .69 erzeugt) enthaelt Code, Laufdateien und Bilder; die lokalen Kopien bestehen
  sha256sum -c (79 von 79; die zwei Netzdateien netz-1.npz und netz-2.npz habe ich danach lokal geloescht, sie liegen
  auf der .69).
- Alles ist synthetische Rechnung auf der .69 (numpy 2.4.4, scipy 1.18.0, 1 Thread, Spuren cpu6 und cpu7). Keine
  Messdaten, keine Messdatenbestaetigung.
- **Kennzeichen:** [E] hier gerechnet, [M] eigene Mathematik (ungeprueft), [F] Festlegung im Plan, [L] Literatur aus dem
  Gedaechtnis, [H] Hypothese, [P] Projektdatei, [Z] Zusatzvorgabe der Leitung.

## 1. Ergebnis zuerst

1. **"Isotacheia gemittelt auf Kantenlaengen" reicht allein nicht [E].**
   - Stellt man nur das mittlere Sprungtempo auf c ein (eine globale Konstante aus den Kantenlaengen), laufen lange
     Wellen langsamer, und jede Regel anders: ungewichtet 0,939, Laengenregel 0,972, Signal entlang kuerzester Wege
     0,937 (Delaunay, N = 50 000). Auf Gabriel: 0,899, 0,952 und 0,887.
   - Die Werte haengen weder von der Saat noch von N ab (N = 2000 bis 50 000, Streuung ueber Saaten hoechstens 0,0011).
   - Ursache [M, Zahlen E]: Um jeden Punkt heben sich die Kantenvektoren nicht auf. Eine lange Welle muss dann im
     Zickzack laufen (Korrektor der Homogenisierung), und das kostet auf Delaunay 3 bis 6 %, auf Gabriel 5 bis 11 % Tempo.
2. **Mit geometrisch passenden Gewichten haben Skalar und Spinor langwellig genau dasselbe Tempo; SN5 ist eingetroffen [E].**
   - P1-FEM-Skalar und Voronoi-Skalar: c = 1 auf 1e-14, in allen 13 Richtungen, beide Saaten, auch bei N = 2000.
   - Weyl-Spinor mit Voronoi-Gewichten: in erster Ordnung exakt 1. Gemessen sind 0,9999 bei k = 0,022, und der Fit gibt
     1,0001 +- 0,0003; die FEM-Extrapolation gibt 1,00002.
   - Bei endlichem k trennen sich die Felder aber: k = 0,171: Weyl 0,9968 gegen FEM 0,9994 (0,26 %); k = 0,341: 0,9864
     gegen 0,9975 (1,1 %).
   - Die Weyl-Welle ist dazu verbreitert, also gedaempft: Bei k = 0,17 liegen 8 % ihres Spektralgewichts ausserhalb
     von +-0,011 um die Spitze, bei 0,34 schon 30 %. Bei der FEM-Welle liegen weniger als 0,01 % ausserhalb der tiefen
     Eigenzustaende ihrer Schale (ein anderes Mass; beide zeigen, wie viel Gewicht neben der Spitze liegt).
3. **Finns 20 Punkte [E]:**
   - "Strich" als jedes Paar gibt 190 Striche, als Gabriel ("kein Dritter dazwischen") im Mittel 43, als Delaunay 91.
     Nach dem naechsten Nachbarn sind es 14 Striche in 6 Inseln.
   - Von allen Seiten gesehen beruehrt jeder Punkt jeden Strich der anderen in irgendeiner Blickrichtung: 3420
     Punkt-Strich-Beruehrungen, jede auf zwei gegenueberliegenden Boegen von Blickrichtungen, jeder so lang wie der Winkel am Punkt
     (800 Proben, genau auf 6e-5).
   - In einer einzelnen Zufallsansicht beruehrt kein Punkt exakt einen Strich. Mit 1 % Toleranz (eps = 0,01) sind es
     im Mittel 37 Beinahe-Beruehrungen, und es kreuzen sich 3286 Strichpaare (68 % der 4845 Vierergruppen liegen konvex).
4. **Welle [E]:**
   - Auf 20 Punkten ist keine Front zu erkennen: Die Ankunftszeit haengt kaum vom Abstand ab (Korrelation 0,05 bis 0,12).
   - Im vollstaendigen Graphen bewegen sich alle anderen 19 Punkte exakt gleich (Abweichung 4e-15).
   - Im Naechster-Nachbar-Wald bleibt die Welle in ihrer Insel.
   - Auf 50 000 Punkten laeuft ein schwacher Ring etwa mit dem langwelligen Tempo nach aussen (im Bild gesehen, nicht gemessen). Der groesste Teil der
     Energie bleibt aber in einem rauen Kern, der sich langsam und gebremst ausbreitet: Der 90-%-Energieradius waechst
     nur mit 0,2 bis 0,8 je Zeiteinheit. Deshalb ist SN4 nach Plan-Regel nicht eingetroffen.
5. **Karte und Kontrollen [E, M]:**
   - SN7 scheitert am Anteil gegenseitig naechster Nachbarn: gemessen 0,592, vorab berechnet 16/27 = 0,593 [M]; die
     Karte hatte den 2D-Wert 0,62.
   - SN1 scheitert: Gabriel gibt 43 statt 75 bis 110 Striche, weil am Wuerfelrand Partner fehlen [M, grob].
   - SN0 scheitert nur am Maxwell-Teil: 25 von 2000 Gabriel-Netzen haben 2 bis 3 lose Moden mehr als die Zaehlung.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/auswertung.py; Werte in lauf-69/auswertung.json (unveraendert, ohne
nachgetragene Vermerke).

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| SN0 | Kontrollen: 190; keine Front; Maxwell je Netz +-1; FEM c = 1 +- 2 %; 3420-Regel | 90 % | **nicht eingetroffen** (Maxwell) | **nicht eingetroffen** | 190 in allen Saaten; Spread 3,7e-15 (N = 20) und 0 (N = 50 000); Maxwell-Abweichung max 3, bei 1,25 % der Gabriel-Netze > 1, sonst 0; FEM homogenisiert 1 +- 1e-14, bei k = 0,171 0,99938 bis 0,99939; 3420-Probe max 6,2e-5 rad (800 Tripel) |
| SN1 | Gabriel, 20 Punkte: 75 bis 110 Striche | 60 % | **nicht eingetroffen** | **nicht eingetroffen** | 43,2 +- 4,3 (29 bis 57) |
| SN2 | NN: 12 bis 16 Striche, 4 bis 8 Inseln | 75 % | **eingetroffen** | **eingetroffen** | 14,07 Striche, 5,93 Inseln |
| SN3 | Kreuzungen L-alle 2900 bis 3500 | 80 % | **eingetroffen** | **eingetroffen** | 3285,9 +- 2,1 je Ansicht, P(konvex) = 0,678 |
| SN4 | [H] Front mit festem Tempo, linear ueber >= 5 Schritte, Richtungsstreuung <= 15 % | 60 % | **nicht eingetroffen** | **nicht eingetroffen** fuer die Energiefront; Vorderkante nicht gemessen (2.1) | Steigung von R90: Delaunay ungew 0,17 bis 0,41, FEM 0,51 und 0,76, Gabriel ungew 0,21 bis 0,37; keine Quelle linear (Spanne < 5 Schritte oder Haelften > 10 % verschieden); Kegel-Streuung 0,14 bis 0,49 |
| SN5 | [H] Weyl gegen FEM fuer k -> 0 < 1 % | 40 % | **eingetroffen** | **eingetroffen** (Grenzwert vorab ableitbar, 2.1) | Delta5 = 7e-5 +- 2,6e-4; v0 = 1,0001 +- 0,0003 (33 Punkte); c0 = 1,00002 +- 0,00001; bei k = 0,171: 0,26 % |
| SN6 | [H] ungewichtet > 5 % ab oder richtungsabhaengig | 70 % | **eingetroffen** | **eingetroffen**, normierungsabhaengig (2.1) | Delta6 = 6,13 % (Saat 2: 6,10 %); Anisotropie 0,34 %; mit "Takt = mittlere Kantenlaenge/c" 1,59 (+59 %) |
| SN7 | 8,0 +- 0,1; 15,54 +- 0,1; 0,62 +- 0,01 | 85 % | **nicht eingetroffen** | **nicht eingetroffen** | Gabriel-Grad 7,983, Delaunay-Grad 15,529, NN-Anteil 0,592 (16/27 = 0,593) |

### 2.1 Lesarten und Vermerke

- **SN0 (Maxwell):**
  - Die Kartenlesart "Nullmoden = max(0, 3N - 6 - E) +- 1" scheitert an lokal losen Stellen.
  - Gabriel hat bei 20 Punkten im Mittel E = 43 < 3N - 6 = 54. Die Zaehlung gibt dann ~11 lose Moden, und so ist es
    meist auch. In 75 Saaten (3,75 %) sind es mehr, weil an anderer Stelle Eigenspannungen sitzen; in 25 Saaten
    (1,25 %) liegt die Abweichung bei 2 oder 3.
  - Calladine (Z - S = 3N - E) gilt immer, ist aber per Rangsatz keine Probe. Die vier anderen Teile von SN0 gelten.
- **SN4:**
  - Die Karte sagt nicht, was "Front" ist. Der Plan misst R90, den Radius, in dem 90 % der Energie liegen.
  - In den Scheibenbildern (bild-B-scheiben.png) sieht man zusaetzlich einen schwachen Ring nahe r = t. Er traegt
    wenig Energie. Gemessen habe ich ihn nicht.
  - Urteil deshalb: fuer die Energiefront nicht eingetroffen. Zur Vorderkante gibt es kein Urteil (Luecke,
    Selbstanzeige 4).
- **SN5:**
  - Der Grenzwert k -> 0 war am Schreibtisch ableitbar: beide 1 (PLAN S7 [M]). Geprueft hat die Rechnung diese
    Herleitung und den Weg dorthin.
  - Fits: Weyl v = 1,0001 - 0,0011 k - 0,117 k^2 (rms 4e-4), FEM c = 1,00002 - 0,0218 k^2 (rms 1e-5). Das lineare
    Glied von Weyl ist klein (-0,0011; seinen Standardfehler gibt die Auswertung nicht aus).
  - Bei k = 0,34 betraegt die Abweichung 1,1 %. "Fuer k -> 0" ist SN5 also eingetroffen, bei den kuerzesten
    gerechneten Wellen nicht mehr.
- **SN6:**
  - Das Urteil haengt an der Normierung von (ii), die die Karte offen laesst (PLAN S8).
  - Plan-Normierung (mittleres Quadrat des Sprungtempos = c^2): -6,1 %. Diese Zahl war vorab nicht ableitbar.
  - Mit "Takt = mittlere Kantenlaenge/c" waere (ii) um 59 % schneller; SN6 traefe dann trivial ein.
  - "Richtungsabhaengig" ist (ii) nicht: Die Anisotropie betraegt 0,34 % und faellt mit N (N = 2000: 1,25 %).
- **SN7:** Kartenfehler S4 (2D-Wert). Gabriel- und Delaunay-Grad treffen.

### 2.2 Agenten-Vorhersagen (PLAN 0a; geschrieben nach dem Start, vor dem Lesen der Rauchlaeufe)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (60 %) | Gabriel-Mittel in [90; 110] | **nicht eingetroffen** (43,2) |
| A2 (90 %) | SN2 eingetroffen | **eingetroffen** |
| A3 (70 %) | Kreuzungen in [3150; 3400] | **eingetroffen** (3285,9) |
| A4 (90 %) | SN7 scheitert nur am NN-Anteil, 0,593 +- 0,005 | **eingetroffen** (0,592) |
| A5 (40 %) | SN6: mehr als 5 % | **eingetroffen** (6,1 %) |
| A6 (75 %) | SN5 eingetroffen | **eingetroffen** |
| A7 (55 %) | SN4 eingetroffen | **nicht eingetroffen** |
| A8 (35 %) | SN0 eingetroffen | **nicht eingetroffen** (Maxwell, wie befuerchtet) |
| A9 (60 %) | Laengenregel > 2 % unter 1 | **eingetroffen** (2,8 %) |
| A10 (60 %) | kuerzeste Wege auf Delaunay in [0,90; 0,97] | **eingetroffen** (0,937) |

## 3. Teil A: 20 Punkte im Wuerfel, von allen Seiten (2000 Saaten)

### 3.1 Striche, Grade, Inseln

| Lesart | Striche (Mittel +- Streuung, Bereich) | Grad | Inseln | zusammenhaengend |
|---|---|---|---|---|
| alle Paare | 190 | 19 | 1 | 100 % |
| Gabriel | 43,2 +- 4,3 (29 bis 57) | 4,32 | 1 | 100 % |
| Delaunay | 91,2 +- 3,3 (79 bis 102) | 9,12 | 1 | 100 % |
| Beruehrung (NN-Graph) | 14,07 +- 1,06 (11 bis 17) | 1,41 | 5,93 +- 1,06 | 0 % |
| Aufblasen mit Anhalten (beschreibend) | 12,85 +- 0,94 (10 bis 16) | 1,29 | 7,15 +- 0,94 | 0 % |

- Gabriel liegt in allen 2000 Saaten in Delaunay.
- Anteil gegenseitig naechster Nachbarn bei 20 Punkten: 0,5926; das liegt auf vier Stellen beim Dichtewert 16/27 (ob das mehr als Zufall ist, habe ich nicht geprueft).
- Das Aufblasen mit Anhalten gibt im Mittel 1,2 Striche weniger und 1,2 Inseln mehr als der NN-Graph.

### 3.2 Von allen Seiten: Kreuzungen und Beinahe-Beruehrungen je Ansicht

| Lesart | Kreuzungen je Ansicht (2000 Ansichten) | Beruehrungen eps = 0,01 | eps = 0,02 | Ansichten mit mindestens einer (eps = 0,01) |
|---|---|---|---|---|
| alle Paare | 3285,9 (P konvex 0,678) | 36,9 | 75,6 | 100 % |
| Gabriel | 29,3 | 3,32 | 7,03 | 93 % |
| Delaunay | 266,1 | 10,8 | 22,6 | 99,99 % |
| Beruehrung (NN) | 1,1 | - | - | - |
| Aufblasen | 0,9 | - | - | - |

- Beruehrungen wurden auf 500 der 2000 Ansichten je Saat gezaehlt (PLAN 4). Sie wachsen linear mit eps (75,6/36,9 = 2,05).
- Exakt (eps = 0) gilt fuer L-alle: 3420 Paare (Punkt, Strich), jedes mit zwei gegenueberliegenden Richtungsboegen von zusammen 2 x Winkel am Punkt
  auf 6,2e-5 rad, die drei Boegen eines Tripels ergeben 2 pi auf 9e-16 (800 Proben). Auf der Kugel hat jeder Bogen das Mass null.
- Kontrolle: Kreuzungszahl aus konvexen Vierergruppen gleich der direkten Paarzaehlung (erste drei Saaten jedes Blocks).

### 3.3 Federnetz und Skalarmoden

| Lesart | Nullmoden Z (Mittel) | Eigenspannungen S | Maxwell-Abweichung ungleich 0 | groesser 1 | Maximum |
|---|---|---|---|---|---|
| alle Paare | 6 | 136 | 0 | 0 | 0 |
| Gabriel | 16,9 | 0,06 | 3,75 % | 1,25 % | 3 |
| Delaunay | 6 | 37,2 | 0 | 0 | 0 |
| Beruehrung (NN) | 45,9 | 0 | 0 | 0 | 0 |
| Aufblasen | 47,1 | 0 | 0 | 0 | 0 |

- Delaunay und alle Paare sind immer starr; der Wald ist es nie.
- Rangschnitt: kleinster Nicht-Null-Singulaerwert mindestens 1,9e-4 sigma_max (Gabriel) bzw. 0,11 (Delaunay), groesster
  Null-Wert 4e-16; die Rangbestimmung ist eindeutig.
- **Tiefste Skalarmode als ebene Welle** (Anteil im Raum der affinen Funktionen):
  - FEM 0,977
  - Delaunay laengengewichtet 0,946, ungewichtet 0,854
  - Gabriel ungewichtet 0,79
  - alle Paare 0,16; der Eigenwert 20 ist dort 19-fach, die Richtung also beliebig.

## 4. Wellenbefund (Teil B)

**N = 20 (exakt, 2000 Saaten, Stoss am Punkt naechst der Wuerfelmitte):**
- Vollstaendiger Graph: Die 19 anderen Punkte haben zu jeder Zeit dieselbe Auslenkung (Spread <= 3,7e-15) und folgen
  u = t/20 - sin(sqrt(20) t)/(20 sqrt 20) auf 6,7e-16. Es gibt keine Front.
- Gabriel und Delaunay: Die Korrelation der Ankunftszeit mit dem Abstand betraegt 0,12 bzw. 0,05. Bei 20 Punkten und
  2 bis 3 Netzschritten Durchmesser ist keine Front zu erkennen.
- NN-Wald: Nur die Punkte der eigenen Insel bewegen sich.
- Bild: lauf-69/bild-A-netze.png (Saat 1, fuenf Lesarten, t = 0,6 / 1,5 / 3; Farbe Auslenkung minus Mittelwert).

**N = 50 000 periodisch (Saat 1), Stoss v(0) = e_s/m_s:**

| Lesart/Feld | Quellen | lambda_max, dt | R90 bei t = 4 / 8 / 12 / 16 (Mittel der Quellen) | Energie ausserhalb der Insel |
|---|---|---|---|---|
| Gabriel/ungew | 4 | 11,6; 0,05 | 2,63 / 4,00 / 5,07 / 5,97 | 0 |
| Gabriel/laenge | 2 | 3828; 0,0081 | 2,54 / 4,07 / 5,06 / 5,86 | 0 |
| Delaunay/ungew | 4 | 7,0; 0,05 | 2,32 / 3,66 / 4,65 / 5,38 | 0 |
| Delaunay/laenge | 2 | 1969; 0,0113 | 2,38 / 3,85 / 4,88 / 5,51 | 0 |
| Delaunay/fem | 2 | 2074; 0,011 | 3,91 / 6,44 / 9,02 / 11,40 | 0 |
| Beruehrung/ungew | 1 | 68; 0,05 | 0 (Energie bleibt in der Insel) | 0 |
| alle (matrixfrei) | 1 | 50 000; 0,0022 | Spread der Nicht-Quellen-Punkte exakt 0 bis t = 2 | - |

- Der 90-%-Energieradius waechst gebremst: Die Steigung der zweiten Fensterhaelfte ist 21 bis 48 % kleiner als die der
  ersten. Ausnahme ist eine FEM-Quelle mit 0,67 gegen 0,83.
- An der Quelle bleibt bei t = 16 noch 0,7 bis 17 % der Energie.
- In Netzschritten (H90) erreicht die Energie bei t = 16 nur 4 bis 6 Schritte (Delaunay/ungew; Gabriel 5 bis 8, FEM 8 bis 10).
- Die Richtungsstreuung der Kegel-Steigungen liegt je Quelle bei 0,05 bis 0,77, im Mittel je Feld bei 0,14 bis 0,49 (raue Umgebung der
  Quelle).
- Bilder: lauf-69/bild-B-scheiben.png (Scheibe |z| < 1 um die Quelle, t = 4, 8, 12; gepunktet: Radius t) und
  lauf-69/bild-B-front.png (R90 und H90 gegen t).
- **Beschreibend aus den Bildern [E, nicht gemessen]:** Ein schwacher roter Ring laeuft knapp innerhalb von r = t nach
  aussen, bei FEM am deutlichsten. Innen bleibt ein dunkler, zitternder Kern. Der Ring ist der langwellige Anteil
  (Tempo um 0,94 bzw. 1), der Kern die kurzwelligen, ungeordneten Schwingungen.
- **Tiefe Moden als ebene Wellen (N = 50 000, Teil-C-Eigenpaare):** Die 32 tiefsten Nicht-Null-Moden liegen zu 99,997 %
  (FEM), 99,999 % (Voronoi), 99,3 % (ungew, mindestens 96,5 %) und 99,4 % (laenge) in den ebenen Wellen ihrer Schale.

## 5. Teil C: Isotacheia relativ zu Kantenlaengen (N = 50 000, Delaunay, Saat 1; [Saat 2])

### 5.1 Langwelliges Tempo je Feld, Richtung und k

Bei k -> 0 ist das Tempo exakt aus der Homogenisierung bestimmt (Skalare) bzw. aus der ersten Ordnung (Weyl).
Endliche k: Skalare aus den 40 tiefsten Eigenpaaren (Residuum <= 2,3e-12), Weyl aus KPM-Zentren (M = 4096). Die Spanne
gibt die Streuung ueber die Richtungen derselben Schale.

| Feld | k -> 0 (Extremwerte ueber alle Richtungen) | k = 0,171 (3 Achsen) | k = 0,241 (6 Flaechendiag.) | k = 0,296 (4 Raumdiag.) | k = 0,341 (3 Achsen, abs m = 2) |
|---|---|---|---|---|---|
| (i) FEM | 1,00000 +- 1e-14 [1,00000] | 0,99938 bis 0,99939 | 0,99875 bis 0,99877 | 0,99810 bis 0,99814 | 0,99747 bis 0,99749 |
| (i') Voronoi-Skalar | 1,00000 +- 1e-14 [1,00000] | 0,99881 bis 0,99882 | 0,99762 bis 0,99764 | 0,99641 bis 0,99645 | 0,99523 bis 0,99526 |
| (ii) ungewichtet | 0,93874 (0,93736 bis 0,94105) [0,93895] | 0,93482 bis 0,93669 | 0,93148 bis 0,93444 | 0,92818 bis 0,93133 | 0,92563 bis 0,92697 |
| (iii) Laengenregel | 0,97199 (0,97110 bis 0,97303) [0,97203] | 0,96855 bis 0,97030 | 0,96649 bis 0,96783 | 0,96389 bis 0,96491 | 0,96073 bis 0,96201 |
| (v) Weyl | 1 (erste Ordnung, +- 2e-16) | 0,9966 bis 0,9969 | 0,9924 bis 0,9935 | 0,9890 bis 0,9903 | 0,9861 bis 0,9867 |
| (iv) kuerzeste Wege | Fronttempo 0,9368 +- 0,0003 [0,9371 +- 0,0002], 14 Kegel 0,9359 bis 0,9384 | | | | |

- **Weyl bei kleinem k (verdrillte Randbedingung):**
  - Laengs x: k = 0,022 / 0,043 / 0,065 gibt v = 0,9999 / 0,9998 / 0,9996.
  - Laengs der Raumdiagonale gleich: 0,9999 / 0,9998 / 0,9996.
  - Weitere verdrillte Punkte (k = 0,105 bis 0,339) liegen auf derselben Kurve, siehe bild-C-tempo.png.
- **Unsicherheit der Weyl-Zentren:**
  - M gegen M/2: hoechstens 7e-4.
  - Gitterkontrolle K1: 1,7e-6.
  - Die Spitzen sind breiter als die KPM-Aufloesung. Im Fenster +-4 sigma_E liegen 0,99 (k = 0,022), 0,92 (0,171) und
    0,70 (0,341) des Gewichts. Das Zentrum ist also ein abgeschnittenes Mittel; eine Verzerrung durch schiefe Flanken
    habe ich nicht beziffert.
- **Gabriel:** ungewichtet 0,8993 [0,8998], Laengenregel 0,9521 [0,9514], kuerzeste Wege 0,8867 [0,8858] (Umweg 1,153).
- **Delaunay, kuerzeste Wege:** Umwegfaktor in der Ferne 1,080. Die Signalfront ist auf 0,07 % isotrop.
- Bild: lauf-69/bild-C-tempo.png.

### 5.2 Abhaengigkeit von N (Homogenisierung, Mittel +- Streuung ueber Saaten)

| N (Saaten) | FEM | Voronoi | ungewichtet | Laengenregel | Anisotropie ungewichtet |
|---|---|---|---|---|---|
| 2000 (10) | 1 (+- 1e-15) | 1 (+- 7e-16) | 0,9389 +- 0,0011 | 0,9719 +- 0,0010 | 1,25 % |
| 8000 (4) | 1 | 1 | 0,9390 +- 0,0006 | 0,9721 +- 0,0005 | 0,62 % |
| 50 000 (2) | 1 | 1 | 0,9387 / 0,9390 | 0,9720 / 0,9720 | 0,34 % / 0,37 % |

- Der Abstand zu 1 ist eine Volumeneigenschaft und kein Rand- oder Endlicheffekt.
- Die Streuung ueber Saaten und die Anisotropie fallen etwa wie 1/sqrt(N).

### 5.3 [Z] Streuung der lokalen Tempi (Zusatzvorgabe der Leitung; beschreibend)

Lokales Mittelwert-Tempo c(n) = sqrt(n.T.n/m) je Knoten bzw. Teilwuerfel, 7 Richtungen. Angegeben ist die
Standardabweichung relativ zum Mittel ueber Zellen und Richtungen, Saat 1 [Saat 2].

| Feld | je Knoten | Teilwuerfel L/8 (~98 Punkte) | L/4 (~780) | L/2 (~6250) | homogenisiertes Tempo: Streuung ueber Saaten (N = 2000) |
|---|---|---|---|---|---|
| Weyl = Voronoi-Skalar | 8,0 % [8,0 %] | 0,43 % [0,44 %] | 0,11 % [0,11 %] | 0,025 % [0,028 %] | 0 (1e-15) |
| FEM (Kantenaufteilung) | 44,7 %, 7,4 % der Werte c^2 < 0 [44,4 %] | 2,3 % [3,4 %] | 0,60 % [0,97 %] | 0,15 % [0,30 %] | 0 (1e-15) |
| ungewichtet | 26,2 % [26,3 %] | 4,0 % [4,0 %] | 1,6 % [1,5 %] | 0,60 % [0,59 %] | 0,11 % |
| Laengenregel | 13,1 % [13,1 %] | 1,3 % [1,25 %] | 0,47 % [0,43 %] | 0,17 % [0,16 %] | 0,10 % |
| Gabriel ungewichtet | 33,5 % | 4,9 % | 1,9 % | 0,51 % | - |
| Gabriel Laengenregel | 17,7 % | 2,2 % | 0,78 % | 0,22 % | - |

- **Weyl und Voronoi-Skalar haben dieselbe lokale Streuung,** weil ihr Knotentensor derselbe ist [M].
- **FEM:** Je Tetraeder ist der FEM-Tensor exakt isotrop (V_T 1) [M]. Die grosse Knotenstreuung kommt nur von der
  Aufteilung auf Kanten; 33,6 % der FEM-Kantengewichte sind negativ.
- **Skalierung mit der Zellgroesse l:**
  - Bei den Feldern mit Patch-Test (Weyl/Voronoi, FEM) faellt die Zellstreuung etwa wie l^-2. Faktor 3,2 bis 4,3 je Verdopplung
    deutet auf einen reinen Oberflaechenbeitrag [M].
  - Bei ungewichtet und Laengenregel faellt sie etwa wie l^-1,4, nahe dem Zufallsgesetz l^-1,5.
- **Vorsicht:** Die lokalen Mittelwert-Tempi mitteln bei allen Feldern auf 1. Die tatsaechlichen 0,939 bzw. 0,972 der
  einfachen Regeln sieht man in keinem lokalen Mittel; sie entstehen erst durch den Korrektor, also durch die
  Korrelationen zwischen Nachbarn. Die lokale Streuung misst deshalb nicht das, was eine lange Welle spuert.

## 6. Kontrollen

- **K1** Weyl-KPM-Zentren gegen exakt (kubisches Gitter L = 37, 16 Schalenwellen und verdrillt): max 1,7e-6.
- **K2** Skalar-Eigenpaare gegen exakt (7-Punkt-Laplace L = 37): max 2,9e-14.
- **K3** Homogenisierung, geschichtetes Gitter: A_xx = 1,5 exakt (harmonisches Mittel; der Mittelwert-Tensor waere 2).
- **K4** Netz N = 1000:
  - Kantenmenge aus den neu bestimmten Tetraedern gleich der von spinnetz.
  - FEM-Kopie (induziert.lokal_K_batch) gegen Gradientenformel 2e-13.
  - Patch-Test erfuellt: Drift FEM 4,7e-15, Voronoi 1,7e-15.
  - Mittelwert-Tensoren 1 auf 3e-15.
- **Hauptnetze** (N = 50 000, Saaten 1 und 2):
  - Euler 0, jedes Dreieck in genau zwei Tetraedern, keine Umkugel ausserhalb des Saums, Abschluss <= 7e-15.
  - Kantenmenge gleich; FEM-Kopie <= 1,6e-10; Masse = Volumen auf 2e-16.
  - Drift FEM <= 2,4e-13, Voronoi <= 1,3e-14; CG-Residuen <= 1e-11.
  - Kleinstes Tetraedervolumen 6,6e-5 (Mittel 0,148).
- **Teil A:** Gabriel in Delaunay (alle Saaten); keine flachen FEM-Tetraeder; Tetraedervolumen = Huellvolumen auf 7e-16;
  Kreuzungszaehlung zweifach gleich.
- **Waechter:** abs(mu_n) <= 1 in allen KPM-Laeufen. Energiedrift der Leapfrog-Laeufe zwischen erster und letzter
  Abtastung: <= 6e-4 (ungewichtet, dt = 0,05), <= 5e-5 (laenge, fem), 5,7e-3 im NN-Wald (Schwingung der diskreten
  Energie bei omega dt = 0,4).

## 7. Selbstanzeigen

1. **Vorwissen aus Rauchlaeufen** (PLAN 9):
   - Gesehen habe ich Teil-A-Zahlen der Rauchsaaten (Gabriel 39 bis 47, Kreuzungen 3192 bis 3348). Damit war SN1 vor
     dem Hauptlauf absehbar verfehlt (PLAN 8, K-SN1).
   - Teil-C-Tempi und SN7-Zahlen habe ich vor dem Einfrieren nicht angesehen. Meine Vorhersagen A1 bis A10 stehen vor
     jedem Rauchergebnis.
2. **Scratchpad:** Um 16:25 CEST habe ich eine Sicherungskopie von strichnetz.py in /tmp/claude-1000/... geschrieben und
   um 16:26 geloescht (Regelverstoss). Sonst habe ich dort nichts abgelegt. Das Werkzeug legt je Hintergrundaufruf
   selbst eine Ausgabedatei dort an; alle Ausgaben habe ich in den Kartenordner umgeleitet.
3. **Rauchlauf R4** (zwei Felder in einem Lauf) schrieb seine Datei nach 598 s; danach beendete systemd die eigene Unit
   an der 600-s-Grenze (rc = 1, Spitzenspeicher 4,1 GB). PLAN 9 sagt dazu irrtuemlich, das zweite Feld sei in die Grenze
   gelaufen; das habe ich erst beim Abholen der Rauchdateien nach dem Hauptlauf gesehen. Die Folge (ein Feld je Lauf,
   Laufzeit und Speicher) bleibt richtig. Fremde Prozesse und Units habe ich nicht angefasst.
4. **SN4-Frontmass:**
   - R90 misst die Energiefront, also hier den rauen Kern. Den schwachen Ring, der etwa mit c laeuft, misst es nicht.
   - Ein Vorderkanten-Mass habe ich nicht geplant; das ist eine Luecke des Plans. Das Urteil bleibt.
   - Die Ring-Aussage stuetzt sich nur auf die Bilder.
5. **Abweichungen von der Karte** (vor dem Einfrieren festgelegt, PLAN 8):
   - Beruehrungen auf 500 statt 2000 Ansichten.
   - Federnetze und Maxwell nur bei N = 20.
   - Teile B und C mit N = 50 000 (Nachtrag) statt 2000 bis 20 000.
   - "Alle Paare" bei N = 50 000 nur matrixfrei und ungewichtet.
   - Laengengewichtet bei N = 20 heisst w = 1/d^2 ohne Normierung.
   - Unstimmigkeit im eingefrorenen PLAN: Abschnitt 4 nennt fuer den Stoss bei N = 20 "die ersten 200 Saaten je
     Block 1", Abschnitt 5 und die Laeufe (stoss=250) nehmen alle 2000 Saaten. Es gilt Abschnitt 5.
6. **Kosmetik in den Logs:** "R90(t=8) None" bei dt, das 0,25 nicht teilt; "E-Drift -0,31" bei "alle" (dort ist nur die
   kinetische Energie gerechnet); eine RuntimeWarning in der Auswertung (Hop-Korrelation bei "alle": alle Abstaende 1).
   Urteile und Tabellen beruehrt das nicht.
7. **Weyl-Zentren:** abgeschnittenes Mittel breiter Spitzen (5.1); die Verzerrung durch schiefe Flanken ist nicht
   beziffert. M und M/2 stimmen auf 7e-4.
8. **Ungeprueft [M]:** Patch-Test- und Homogenisierungsargument, erste Ordnung fuer Weyl, 16/27, l^-2-Deutung. Numerisch
   gestuetzt, nicht gegengelesen.
9. **Lokal:**
   - kein python, awk oder perl
   - benutzt: jq (auch zum Setzen der Saat in einer Rauch-Testdatei), sed, grep, sha256sum, date, ssh, scp, cp, mv,
     mkdir, rm, ls, cat, cut, head, tail, wc, tr
   - sleep nur in Warteschleifen
10. **Auf der .69 ausserhalb des Starters:** kein Python; mkdir, cp, mv, cat, ls, grep, ps, sha256sum, date, uptime,
    sleep in Warteschleifen.
11. **Spuren:** nur cpu6 und cpu7, je Spur nacheinander, hoechstens zwei eigene ssh-Ketten zugleich.

## 8. Bedeutung

- **Finns Frage 1 ("Strich"):**
  - Wie viele Striche es sind, haengt ganz an der Lesart: 190 (alle), 91 (Delaunay), 43 (Gabriel), 14 (naechster
    Nachbar, 6 Inseln).
  - "Von allen Seiten" beruehrt jeder Punkt jeden Strich der anderen auf zwei gegenueberliegenden Boegen von
    Blickrichtungen, jeder so lang wie der Winkel am Punkt. Das gibt 3420 Beruehrungen; eine einzelne Zufallsansicht
    verfehlt sie fast sicher alle.
- **Welle:**
  - Sie braucht Nachbarschaft und Groesse. Auf 20 Punkten ist keine Front zu erkennen, auf dem vollstaendigen Graphen
    gibt es keine, auf dem Wald keine Ausbreitung ueber die Insel hinaus.
  - Auf 50 000 Punkten sieht man einen langwelligen Ring etwa mit dem Feldtempo (nur im Bild, nicht gemessen). Der
    groesste Teil der Stossenergie bleibt als rauer Kern zurueck, der nur langsam waechst.
- **Finns Frage 2 (Isotacheia "gemittelt auf Kantenlaengen relativ") [E, Deutung H]:**
  - Funktioniert, wenn jedes Feld seine Kopplungen aus derselben, konsistent gebildeten Geometrie nimmt: Voronoi-Flaechen
    und Volumina oder P1-Elemente. Dann ist das langwellige Tempo fuer Skalar und Spinor gleich, bei k -> 0 exakt
    [E, M]. Unordnung verschiebt es dort nicht, auch nicht in zweiter Ordnung, weil der Korrektor verschwindet.
  - Funktioniert nicht, wenn nur das mittlere Sprungtempo stimmt ("ein Sprung je Takt" oder "Zeit = Laenge/c" mit
    einer globalen Konstante). Dann laufen die Felder auf Delaunay 3 bis 6 % langsamer (Gabriel 5 bis 11 %) und
    verschieden schnell. Nach AETHER-UHR-1 wuerde eine Bewegung gegen das Netz dann messbar [P].
  - Auch bei gleichem Grenztempo bleiben bei kurzen Wellen Unterschiede: Weyl kruemmt sich fuenfmal staerker als FEM
    (-0,117 k^2 gegen -0,022 k^2) und ist gedaempft. Das waere eine Schranke an die Netzweite, wie bei SPIN-ZUFALLSNETZ-1
    [H].
- **Bedeutungssaetze der Karte, einzeln:**
  - **"SN5 trifft ein: Ruhesystem langwellig unsichtbar; offen bleiben Wechselwirkung und kurze Wellen":** gilt fuer die
    beiden konsistent gebauten Felder. Kurze Wellen unterscheiden sich schon frei, bei k = 0,34 um 1,1 %.
  - **"SN6 trifft ein: Der Laengenbezug ist Pflicht":** genauer: Ein Laengenbezug je Kante reicht nicht (Laengenregel
    -2,8 %, kuerzeste Wege -6,3 %). Gleich wurden hier nur die Felder, deren Gewichtung den Patch-Test erfuellt
    (sum_j w_ij d_ij = 0 an jedem Punkt, Mittelwert-Tensor exakt isotrop). Die anderen muesste man nachtraeglich auf
    das gemessene Tempo abstimmen (LICHT-GLEICH-L: Abstimmung oder Symmetrie) [P].
- **[Z] zur Streuung (BLACKMON-MEOW-L):**
  - Die lokale Streuung ist je Feld verschieden: je Knoten 8 % (Weyl, Voronoi) bis 45 % (FEM-Kantenaufteilung).
  - Fuer lange Wellen zaehlt aber nicht sie, sondern das homogenisierte Tempo. Das ist bei den Patch-Test-Feldern
    exakt 1, ohne Streuung ueber Saaten und Richtungen.
  - Ob eine zusammengesetzte Uhr die lokale Streuung trotzdem spuert, zeigt diese Rechnung nicht [H]. Die
    Blackmon-Skizze ist ein Bild mit Punktlaeufern; Wellen mitteln ueber den Korrektor anders.
- **Messbezug:** keiner. Alles ist ein freies, klassisches Modell auf einem gedachten Netz.

## 9. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-163911, EINGEFROREN-SHA256.txt
- code/:
  - strichnetz.py, auswertung.py, bilder.py
  - spinnetz.py (SPIN-ZUFALLSNETZ-1), induziert.py (INDUZIERT-1)
  - je mit Kopie *.eingefroren-20261004-163911
- rauch-69/: Logs und Dateien der Rauchlaeufe R1 bis R17 (ohne die Netzdateien netz-901.npz und netz-902.npz, die
  auf der .69 liegen), ausw-test/ (Testlauf von Auswertung und Bildern auf umbenannten Rauchdaten)
- lauf-69/:
  - Logs H01 bis H31
  - teilA-b1 bis b8, dicht-1/2, klein-2000/8000, eigen-1-{fem,voronoi,ungew,laenge}, weyl-1-{0,x,d},
    welle-*.json/.npz, kontrolle.json, netz-1/2.npz.json
  - auswertung.json, PRUEFSUMMEN.txt
  - Bilder: bild-A-netze.png, bild-A-zaehlung.png, bild-B-scheiben.png, bild-B-front.png, bild-C-tempo.png
- Auf der .69: /home/fmh/fmhc-physics-remote/runde41-strich-netz/ (code/, rauch/, lauf/ mit netz-1.npz und netz-2.npz)

## 10. Einfach gesagt

Zwanzig zufaellige Punkte im Wuerfel kann man auf vier Arten mit Strichen verbinden; je nach Regel sind es 190, 91, 43
oder nur 14 Striche. Schaut man von allen Seiten, liegt jeder Punkt in irgendeiner Blickrichtung genau auf jedem Strich
der anderen. In einer zufaelligen Ansicht kreuzen sich dagegen etwa 3300 Strichpaare. Eine Welle braucht viele Punkte:
Auf 50 000 Punkten laeuft ein Ring nach aussen, waehrend sich der meiste Stoss nur langsam als Zittern ausbreitet. Zu Finns
zweiter Frage: Stellt man nur das mittlere Tempo der Spruenge richtig ein, laufen lange Wellen trotzdem 3 bis 6 %
langsamer, und jede Regel anders. Bauen dagegen ein Skalarfeld und ein Spinfeld ihre Kopplungen aus denselben
Netzflaechen und -volumen, haben sie bei langen Wellen genau dasselbe Tempo; bei kuerzeren Wellen trennen sie sich
wieder um bis zu 1 %. Das ist eine Rechnung auf einem gedachten Netz, keine Messung.
