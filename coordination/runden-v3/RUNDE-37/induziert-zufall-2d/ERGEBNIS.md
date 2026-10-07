# INDUZIERT-ZUFALL-2D: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 06:18:44 CEST; Code ab 06:33:36, Plantext ab 06:41:16 CEST.
  - Rauchlaeufe 04:35:45 bis 04:43:17 UTC (PLAN Abschnitt 11).
  - Eingefroren 06:44:09 CEST: PLAN.md.eingefroren-20261004-064409, Code-Kopien *.eingefroren-20261004-064409,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 04:44:22 bis 04:57:23 UTC, Auswertung 04:57:29 bis 04:57:35 UTC, alle rc = 0.
  - Text ab 06:59:14 CEST.
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
- **Konvention (wie INDUZIERT-1 Teil A, Variante P):**
  - Gamma = 1/2 log det' K, K = Kotangens-Laplace aus den Kantenlaengen.
  - Konforme Mode als Ecken-Skalierung l_ij -> l_ij exp(s (sig_i + sig_j)/2) mit sig = cos(k.x).
  - Gemessen wird c_P = Gamma''/(k^2 A). Polyakov waere -1/(24 pi) = -0,013263.

## 1. Ergebnis zuerst

1. **Unordnung macht die Antwort richtungsfrei, aber nicht geometrisch [E].**
   - Auf den Zufallsnetzen ist die konforme Steifigkeit c_P = **+0,15909 +- 0,00008** (N = 64 000, 12 Saaten,
     abs(k) = 0,0497). Polyakov waere -0,01326, also Faktor -12,0.
   - In allen vier Richtungen gleich: Streuung 0,09 %, so gross wie das Saatrauschen (chi^2 = 4,5 bei 3
     Freiheitsgraden). Das regelmaessige Netz liegt je nach Richtung zwischen 0,079 und 0,170.
   - Fuer k -> 0 geht c_P gegen 0,1590 bis 0,1591, numerisch nahe 1/(2 pi) = 0,15915 (Identifikation [H]). Der
     isotrope Teil des regelmaessigen Netzes ist 1/8 [M]; der Gitterterm wird durch Unordnung also um 27 % groesser,
     nicht kleiner.
2. **Auch mit Massenmatrix kein Polyakov [E]:** c_D (det'(M^-1 K) ohne Flaechenglied) = +0,052 statt -0,0133. Der
   isotrope Teil des regelmaessigen Netzes ist hier -1/24 = -0,042.
3. **Knotenverschiebungen sind nicht weich [E]:**
   - Je Amplitude kosten sie etwa so viel wie die konforme Mode: Gamma''/(k^2 A) = 0,1754, laengs und quer gleich,
     bei allen N, k und Richtungen.
   - Je Kantenlaengen-Norm sind sie bei abs(k) = 0,05 bis 0,07 das 596- bis 3585-fache der konformen Mode. Das
     Verhaeltnis waechst wie 1/k^2.
4. **Die Antwort mittelt sich selbst [E]:** Die Saatstreuung faellt wie N^(-0,57) (Bootstrap 68 %: -0,67 bis -0,51).
   Schon ein Netz mit 64 000 Knoten legt c_P auf 0,15 % fest.
5. **Urteile:**
   - IZ0, IZ2 und IZ4 eingetroffen; IZ1 und IZ3 nicht eingetroffen. Nach Kartenwortlaut gleich.
   - Ausgeloest ist die vorab festgelegte Bedeutung "IZ1 verfehlt, IZ2 trifft ein": Unordnung macht die Antwort
     richtungsfrei, aber nicht geometrisch. Ue1 braucht ein schwankendes Netz oder Feinabstimmung.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/zufall_auswertung.py; Werte in lauf-69/auswertung.json (unbearbeitet).
Tor bestanden (Abschnitt 4). Alle Saatzahlen wie geplant (64 / 24 / 12).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| IZ0 | regelmaessiges Netz gibt +0,1249 aus INDUZIERT-1 auf 1e-3 wieder | 85 % | **eingetroffen** | eingetroffen (absolut 2,2e-5) | c_P = 0,1249217198 (L = 256, 0 Grad, n = 2) gegen 0,1249217183: 1,2e-8 relativ |
| IZ1 | Saatmittel bei kleinstem k, N = 64 000, innerhalb 20 % von -1/(24 pi) | 25 % | **nicht eingetroffen** | nicht eingetroffen | cbar = +0,15909 +- 0,00008 (Achsen, abs(k) = 0,0497); Verhaeltnis -11,99; vier Richtungen 0,15902 |
| IZ2 | Richtungsstreuung des Saatmittels <= 5 % | 70 % | **eingetroffen** | eingetroffen | Std/Mittel 0,092 %, Spanne 0,21 %; Saatrauschen allein 0,085 % |
| IZ3 | Verschiebungen <= 10 % der konformen Steifigkeit bei kleinstem k | 30 % | **nicht eingetroffen** | nicht eingetroffen (mit Vorzeichen) | Verhaeltnis 596 bis 3585 (je Kantenlaengen-Norm, n = 2, alle positiv) |
| IZ4 | Saatstreuung faellt wie N^(-1/2), Steigung -0,5 +- 0,15 | 60 % | **eingetroffen** | eingetroffen | Std 0,00116 / 0,00065 / 0,00024; Steigung -0,568; Bootstrap 68 % [-0,67; -0,51], 95 % [-0,82; -0,45] |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "IZ1 und IZ3 treffen ein" ist nicht ausgeloest.
  - **"IZ1 verfehlt, IZ2 trifft ein" ist ausgeloest:** Unordnung macht die Antwort richtungsfrei, aber nicht
    geometrisch. Ein fester Rest bleibt; Ue1 braucht ein schwankendes Netz (Summe ueber Netze) oder Feinabstimmung.
  - "IZ4 verfehlt" ist nicht ausgeloest: Die Antwort mittelt sich selbst, ein einzelnes grosses Netz reicht.
- **IZ4 am Rand der Statistik:** Das 95-%-Bootstrap-Intervall reicht bis -0,82, also ueber die Schwelle -0,65 hinaus.
  Beschreibend gibt die Streuung bei n = 1 (vier Richtungen, abs(k) = 0,0993 / 0,0497 / 0,0248) die Steigung -0,47.

**Agenten-Vorhersagen** (PLAN Abschnitt 9; A3, A5 und A7 waren nach den Rauchlaeufen absehbar)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (95 %) | Tor besteht (log det' <= 1e-12, Differenzen <= 1e-7) | **eingetroffen**: 1,0e-15 und 5,6e-8 |
| A2 (95 %) | IZ0 mit Abweichung <= 1e-6 | **eingetroffen**: 1,2e-8 |
| A3 (absehbar) | IZ1 nicht; c_P = +0,15 bis +0,17, Faktor ~ -12 | **eingetroffen**: 0,1591, Faktor -12,0 |
| A4 (85 %) | IZ2 mit Streuung <= 1 % | **eingetroffen**: 0,09 % |
| A5 (absehbar) | IZ3 nicht; Verhaeltnis > 100 bei abs(k) = 0,05, waechst wie 1/k^2 | **eingetroffen**: 1189 bis 3585 bei 0,0497; Faktor 3,99 je Halbierung von k (N = 16 000, 4 000) |
| A6 (45 %) | IZ4 eingetroffen | **eingetroffen** (-0,568) |
| A7 (absehbar) | c_D verfehlt Polyakov um > 20 % | **eingetroffen**: +0,052 |
| A8 (90 %) | c_P(Zufall) > 0,125 | **eingetroffen**: 0,159 |

## 3. Tabellen

### 3.1 Konforme Mode c_P, Saatmittel +- Standardfehler [E]

(Standardfehler in Einheiten von 1e-5; letzte Spalte: Streuung ueber Saaten des Vier-Richtungen-Mittels)

| N (Saaten) | n | abs(k) Achse / Diagonale | 0 Grad | 45 Grad | 90 Grad | 135 Grad | Std |
|---|---|---|---|---|---|---|---|
| 4 000 (64) | 1 | 0,0993 / 0,140 | 0,15842 +- 22 | 0,15805 +- 19 | 0,15885 +- 21 | 0,15848 +- 20 | 0,00101 |
| 4 000 (64) | 2 | 0,199 / 0,281 | 0,15751 +- 22 | 0,15612 +- 19 | 0,15794 +- 21 | 0,15652 +- 19 | 0,00093 |
| 16 000 (24) | 1 | 0,0497 / 0,0702 | 0,15878 +- 17 | 0,15882 +- 20 | 0,15893 +- 22 | 0,15888 +- 18 | 0,00065 |
| 16 000 (24) | 2 | 0,0993 / 0,140 | 0,15853 +- 20 | 0,15828 +- 18 | 0,15867 +- 18 | 0,15828 +- 16 | 0,00056 |
| 64 000 (12) | 1 | 0,0248 / 0,0351 | 0,15928 +- 13 | 0,15902 +- 16 | 0,15885 +- 18 | 0,15910 +- 16 | 0,00028 |
| 64 000 (12) | **2 (Urteil)** | 0,0497 / 0,0702 | 0,15923 +- 12 | 0,15890 +- 12 | 0,15895 +- 17 | 0,15900 +- 13 | 0,00025 |
| 64 000 (12) | 4 | 0,0993 / 0,140 | 0,15882 +- 11 | 0,15853 +- 13 | 0,15868 +- 16 | 0,15840 +- 13 | 0,00027 |

- **k-Abhaengigkeit:** c_P = c0 + b k^2 (kleinste Quadrate ueber alle Punkte je N) gibt c0 = 0,15911 (N = 64 000),
  0,15897 (16 000) und 0,15896 (4 000), mit b = -0,033 bis -0,035. Beim kleinsten k (0,0248; N = 64 000, Achsen) ist
  c_P = 0,15907 +- 0,00006.
- **Endliche Groesse:** Bei gleichem abs(k) = 0,0993 (Achsen) ist c_P = 0,15863 / 0,15860 / 0,15875 fuer N = 4 000 /
  16 000 / 64 000. Einen Gang mit N gibt es im Rahmen der Fehler nicht.
- **Naehe zu 1/(2 pi) = 0,159155 [H]:**
  - Die Werte c0 liegen 0,03 % (N = 64 000) bis 0,12 % (N = 4 000) darunter.
  - Den Fehler von c0 habe ich nicht bestimmt; die Einzelwerte haben Standardfehler 1e-4 bis 2e-4.
  - Hergeleitet ist das nicht. Auffaellig ist, dass auch die Verschiebungsmoden des regelmaessigen Netzes auf der
    Achse 1/(2 pi) ergeben (3.3).

### 3.2 Regelmaessig gegen zufaellig, abs(k) ~ 0,05 bis 0,07 (n = 2) [E]

| Netz, Groesse | 0 Grad | 45 Grad | 90 Grad | 135 Grad | isotroper Teil (k -> 0) |
|---|---|---|---|---|---|
| regelmaessig, c_P | 0,12492 | 0,07946 | 0,12492 | 0,17034 | 1/8 [M] |
| zufaellig (N = 64 000), c_P | 0,15923 | 0,15890 | 0,15895 | 0,15900 | 0,1591 |
| regelmaessig, c_D | -0,04161 | -0,25320 | -0,04161 | +0,17041 | -1/24 [M] |
| zufaellig (N = 64 000), c_D | 0,05253 | 0,05169 | 0,05182 | 0,05217 | 0,0518 |
| Polyakov | -0,01326 | -0,01326 | -0,01326 | -0,01326 | -0,01326 |

- **Isotroper Teil [M]:** Fuer eine skalare Mode ist der lokale k^2-Koeffizient eine Form T_ab n_a n_b, hat also nur
  die Winkelmoden 0 und 2. Der Polyakov-Anteil ist fuer die konforme Mode isotrop.
  - Aus c(0 Grad) = c(90 Grad) folgt deshalb: Der isotrope Teil ist c(0 Grad) = (c(45 Grad) + c(135 Grad))/2.
  - Mit den Grenzwerten aus INDUZIERT-1 gibt das 1/8 fuer c_P und -1/24 fuer c_D.
  - Abstand des isotropen Teils von Polyakov in c_P: regelmaessig 1/8 + 1/(24 pi) = 0,138, zufaellig 0,172. In c_D:
    regelmaessig -0,028, zufaellig +0,065.
  - Das Zufallsnetz entfernt also den Richtungsanteil (Mode 2), aber nicht den isotropen Gitterterm; der wird sogar
    groesser.
- **c_D gegen k:** c0_D = 0,0518 / 0,0516 / 0,0517 (N = 64 000 / 16 000 / 4 000), Steigung in k^2 +0,05 bis +0,07.
  Statistische Fehler der Einzelwerte 0,0002 bis 0,0007.

### 3.3 Knotenverschiebungen [E]

| Netz | Richtung | Gamma''/(k^2 A) laengs | quer | Verhaeltnis zur konformen Mode je Kantenlaengen-Norm, laengs / quer |
|---|---|---|---|---|
| zufaellig N = 64 000, n = 2 | 0 Grad | 0,1753 | 0,1750 | 1189 / 3564 |
| | 45 Grad | 0,1755 | 0,1757 | 596 / 1790 |
| | 90 Grad | 0,1755 | 0,1758 | 1193 / 3585 |
| | 135 Grad | 0,1754 | 0,1752 | 596 / 1782 |
| regelmaessig L = 256, n = 2 | 0 Grad | 0,15914 | 0,15914 | 1410 / 4229 |
| | 45 Grad | 0,0685 | 0,2499 | 286 / 5215 |
| | 135 Grad | 0,2499 | 0,0683 | 2436 / 666 |

- Auf den Zufallsnetzen sind laengs und quer in allen N, k und Richtungen gleich: 0,1743 bis 0,1762, Fehler je
  Eintrag 0,0001 bis 0,0004. Im Mittel bei N = 64 000, n = 2: 0,17542 und 0,17544. Ueber alle 20 Vergleiche liegt
  die Differenz im Mittel bei 0,3 Standardfehlern, hoechstens bei 2,9.
- **[M], nachtraeglich hergeleitet, nicht vorhergesagt:** Fuer ein isotropes Netz, dessen Gamma unter globaler Streckung
  exakt invariant ist, verschwinden im Mittel Vorspannung und Kompressionsmodul. Dann kosten Laengs- und Querwelle
  dasselbe; beide haengen nur am Schermodul der Vakuumenergie.
- Das Verhaeltnis quer/laengs = 3 kommt nur aus der Norm: Die Summe der quadrierten Kantenaenderungen ist bei der
  Querwelle dreimal kleiner (Winkelmittel 1/8 gegen 3/8) [M].
- Regelmaessig, Grenzwerte (Identifikation [H]): 1/(2 pi) auf der Achse, 1/4 und 1/pi - 1/4 = 0,0683 auf den
  Diagonalen.
- **Skalierung:** Das Verhaeltnis waechst wie 1/k^2, zum Beispiel N = 16 000 laengs 0 Grad: 1193 bei 0,0497 und 299
  bei 0,0993.

### 3.4 Saatstreuung gegen N (IZ4) [E]

| N | Saaten | n (Achsen) | Std von c_P, abs(k) = 0,0993 | relativ | beschreibend: Std bei n = 1, vier Richtungen |
|---|---|---|---|---|---|
| 4 000 | 64 | 1 | 0,00116 | 0,73 % | 0,00101 (abs(k) 0,0993) |
| 16 000 | 24 | 2 | 0,00065 | 0,41 % | 0,00065 (0,0497) |
| 64 000 | 12 | 4 | 0,00024 | 0,15 % | 0,00028 (0,0248) |

- Steigung -0,568 (Urteil); beschreibend bei n = 1: -0,47. Bild: lauf-69/bild-streuung.png.
- **Bilder:**
  - lauf-69/bild-konform.png: c_P und c_D gegen abs(k) je N, mit Polyakov und dem regelmaessigen Netz
  - lauf-69/bild-richtung.png: Richtungen, Einzelsaaten und Mittel
  - lauf-69/bild-verschiebung.png: Verschiebungen je Amplitude und je Kantenlaengen-Norm

## 4. Kontrollen

- **Tor (PLAN Abschnitt 6): bestanden.**
  - (a) Netze: Alle 100 Zufallsnetze erfuellen V - E + F = 0, E = 3N, F = 2N, "jede Kante in genau zwei
    Dreiecken", positive Orientierung, Flaechensumme = L^2 (<= 1,1e-16) und Delaunay. Die knappste Kante hat die
    Gegenwinkelsumme pi - 7,0e-8 (fast kozirkular), das kleinste Kotangens-Gewicht ist 3,7e-8 > 0.
  - Jede der 9508 LU auf den Zufallsnetzen hatte U_ii > 0 (kleinstes 0,51) und perm_r = perm_c.
  - Mittlere Kantenlaenge 1,1317 gegen 32/(9 pi) = 1,1318 fuer Poisson-Delaunay bei Dichte 1 [L Miles 1970];
    mittleres Kantenquadrat 1,5913 gegen 5/pi = 1,5915 [L?].
  - (b) log det' per Erdung und LU gegen dichte Rechnung: <= 1,0e-15 relativ (K2: 1,4e-13 absolut bei Gamma = 151,5;
    K3: <= 2,8e-13 absolut bei Gamma = 282 bis 639).
  - (c) Differenzenschema gegen die exakte Blasensumme aus INDUZIERT-1: <= 3,0e-8 (K4, L = 16 und 64) und <= 5,6e-8
    (L = 256, N = 65 536), konform und beide Verschiebungen.
- **K1:** Kotangens-Formel gegen Gram-Formel (lokal_K_batch) 2,4e-11 relativ auf 500 Zufallsdreiecken. Die Grenze kommt
  von der Inversion von G bei duennen Dreiecken in der Gram-Formel.
- **K2:** Matrix des regelmaessigen Netzes (L = 16) gegen induziert.torus_K: 8,9e-16.
- **K3:** Symmetrie exakt, Zeilensummen <= 1,4e-14, kleinster Eigenwert ungleich null 0,04 bis 0,09 (Rang N - 1).
- **K5 (Schritte):** Auf N = 4 000 (Saat 999) aendern h = 0,005 / 0,01 / 0,02 c_P um <= 2,3e-9 relativ und die
  Verschiebungen um <= 2,3e-7 relativ.
- **Netze, beschreibend:** kleinster Winkel 0,049 Grad, groesster 176,4 Grad, kuerzeste Kante 0,0011,
  laengste 4,55 (< L/4 in allen Netzen). Die duennen Dreiecke stoeren weder LU noch Differenzen.
- **Regelmaessiges Netz:** Die Differenzen treffen die Blasensumme auch bei den Verschiebungen auf 5,6e-8. Damit ist
  auch das Glied zweiter Ordnung der Laengen (2 N Summe Gamma'_d (1 - cos k.d), Abschnitt 3 im Plan) bestaetigt.

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - IZ1 und IZ3 haetten eintreffen koennen; IZ2 und IZ4 haetten an echter Anisotropie bzw. fehlender Selbstmittelung
    scheitern koennen.
  - IZ0 und das Tor pruefen den neuen Code gegen eine unabhaengige, exakte Rechnung.
  - Meine eigene A6 (IZ4 mit 45 %, eingetroffen) war offen.
- **L2 (Gegenprobe):**
  - Differenzen gegen die exakte Blasensumme (drei Torusgroessen, konform und Verschiebungen)
  - LU gegen dichte slogdet und Eigenwerte; Kotangens gegen Gram-Formel
  - drei Schrittweiten; drei N; vier Richtungen; 64/24/12 Saaten; zwei bzw. drei k je N
  - Netzpruefungen (Euler, Mannigfaltigkeit, Delaunay, Flaeche) in jedem Netz
- **L3 (Numerik):** 1e-15 (log det'), 5e-8 (Differenzen), statistische Fehler siehe Tabellen.
- **L4 (schon bekannt):**
  - Polyakov 1981 [L].
  - Zufallsgitter stellen Rotations- und Translationssymmetrie im Mittel wieder her (Christ, Friedberg, Lee 1982,
    "random lattice field theory") [L]. IZ2 war damit erwartbar.
  - Die Ecken-Skalierung ist die "diskrete konforme Aenderung" von Luo 2004 und Bobenko, Pinkall, Springborn 2015 [L].
    Ob es dafuer eine diskrete Polyakov-Formel gibt, weiss ich nicht [L?].
  - log det des Laplace auf isoradialen Graphen ist rein lokal (Kenyon, Acta Math., um 2000) [L?]. Das passt dazu,
    dass der k^2-Koeffizient auf festen Netzen lokal bestimmt ist.
  - In 2D fuehrt die annealte Summe ueber zufaellige Triangulierungen mit Materie auf Liouville- bzw.
    Polyakov-Gravitation (David 1985, Kazakov 1985, KPZ 1988, David 1988, Distler/Kawai 1989) [L]. Das ist ein
    schwankendes Netz, nicht das feste Mittel von hier.
  - Neu hier: die Zahlen fuer periodische Poisson-Delaunay-Netze. Ob c_P ~ 0,159 dafuer bekannt ist, weiss ich nicht
    [L?].
- **L5 (Messbezug):** keiner (2D, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **Flaechenglied [K]:** In der Kartengroesse 1/2 log det' K gibt es kein Flaechenglied; es gehoert zu det'(M^-1 K)
  (INDUZIERT-1 K1). Gewertet wurde c_P wie in INDUZIERT-1; c_D ist beschreibend und verfehlt Polyakov ebenso
  (+0,052).
- **Kleinstes k [F]:** nur Achsen bei abs(k) = 0,0497. Das Vier-Richtungen-Mittel (0,15902) und der kleinste
  gerechnete Wert (0,15907 bei abs(k) = 0,0248) geben dasselbe Urteil.
- **IZ0 relativ [F]:** 1,2e-8; nach Kartenwortlaut absolut 2,2e-5. Beides eingetroffen.
- **IZ3 mit Betrag [F]:** Alle Verhaeltnisse sind positiv; mit Vorzeichen gilt dasselbe Urteil.
- **IZ4 bei festem k [F]:** Bei festem n = 1 (beschreibend) waere die Steigung -0,47, ebenfalls im Band.
- **Kartenfehler,** die ein Urteil aendern, habe ich nicht gefunden.
- **Zum Schreibtisch der Karte:**
  - "Jede lokale k^2-Steifigkeit ist ein Gitterterm, der von der Form der Dreiecke abhaengt" ist bestaetigt.
  - "Auf einem zufaelligen Netz mittelt sich die Richtung heraus, aber nicht zwingend der Betrag" ist ebenfalls
    bestaetigt.
  - Die Erwartung der Leitung (isotroper Rest, Polyakov verdeckt) ist eingetroffen.

## 6. Selbstanzeigen

1. **Vor dem Einfrieren absehbar:** IZ1 und IZ3 (aus K5 und dem Zeitlauf: c_P ~ +0,16, Verschiebungen je Amplitude
   ~ 0,17) sowie wahrscheinlich IZ2 (in einer Saat isotrop auf 0,6 %). Im Probebild sah ich c_D ~ +0,05. Das steht
   im Plan (Abschnitt 11). Die Schwellen sind die der Karte.
2. **Festlegungen nach ersten Zahlen:** Die [F]-Regeln (nur Achsen fuer IZ1, Fenster n >= 2, IZ4 bei festem k,
   Rauschgrenze bei IZ2, Betrag bei IZ3) habe ich nach kontrolle-r1 und dem Zeitlauf geschrieben, aber vor r2.
   Mit den anderen naheliegenden Lesarten waeren die Urteile gleich (Abschnitt 5).
3. **Probe-Urteile gesehen:** Die Probe der Auswertung auf r2 (3/2/2 Saaten) zeigte IZ4 "nicht eingetroffen"
   (Steigung -0,03, statistisch leer). Die Hauptlaeufe hatten danach die im Plan festgelegten Saatzahlen.
4. **Code vor dem Einfrieren geaendert:**
   - Verschiebungsmoden nur fuer eine n-Liste (nach dem Zeitlauf, Rechenzeit).
   - Nach der Probe habe ich in zufall_auswertung.py die Regel "mindestens 8 Saaten bei N = 64 000" eingebaut. Sie
     stand schon im Plantext.
   - Keine Schwelle geaendert.
5. **Nach dem Einfrieren:** kein Code geaendert.
6. **Gemeinsamer Scratchpad:**
   - Um 06:46:30 CEST habe ich eine Kopie von kontrolle.json per Umleitung ">" in den Scratchpad der Leitung
     geschrieben, unter dem Namen kontrolle.json.
   - Ob dort vorher eine gleichnamige Datei eines anderen Agenten lag, kann ich nicht ausschliessen; sie waere
     ueberschrieben.
   - Danach habe ich sie in IZ2D-runde38-kontrolle-kopie.json umbenannt. Sonst habe ich dort nichts geschrieben.
7. **Nicht gerechnet:**
   - der nicht-analytische Anteil (4phi-Harmonische) auf Zufallsnetzen (Zeitbox, Plan Abschnitt 2)
   - die Varianten "linear in l" und "linear in s" (rauschbeherrscht, Plan Abschnitt 2)
8. **Abweichungen vom Brief, beide gleichwertig und geprueft:**
   - det' per Erdung statt Rang-1-Ergaenzung (die waere dicht)
   - Dreiecksauswahl per Schwerpunkt statt "mindestens eine Ecke im Grundbereich, Duplikate entfernen"
9. **[H] ohne Rechnung:** Die Ueberlegung zur Aufloesung (Weyl-Anomalie, Abschnitt 7) ist weder gerechnet noch an der
   Quelle geprueft.
10. **Spuren und Laeufe:**
    - cpu3 und cpu4, nie mehr als zwei zugleich.
    - 17 Starts: 7 Rauch (mit Probe), 9 Haupt und 1 Auswertung. Die Ketten liefen als nohup sh -c um den Starter.
    - Kein Interpreterstart ausserhalb des Starters, keine Versionsprobe.
11. **Lokal:** kein python, awk oder perl. Benutzt habe ich jq, sed, grep, sha256sum, date, ssh und scp, dazu cp,
    mv, mkdir, ls und cat.
12. **Zeitbox:** Start 06:18:44 CEST, Abgabe 07:05:07 CEST, innerhalb von 120 min.

## 7. Bedeutung

- **Finns Weiche "Hilft Unordnung?": nur bei der Richtung.**
  - Ja fuer die Richtung: Das Zufallsnetz ist isotrop; die Richtungsstreuung (0,09 %) ist reines Saatrauschen.
    Beim regelmaessigen Netz sind es 0,079 bis 0,170. Das ist der bekannte Vorteil von Zufallsgittern [L].
  - Nein fuer den Betrag: Der k^2-Koeffizient der konformen Mode bleibt ein Gitterterm.
    - Er ist isotrop, mittelt sich aber nicht weg, sondern zu einer festen Zahl: c_P = 0,159, also -12 mal Polyakov.
    - Er ist sogar groesser als der isotrope Teil des regelmaessigen Netzes (1/8).
  - Die Umbenennungsmoden (Knotenverschiebungen) bleiben steif. Das Zufallsnetz hat einen Schermodul der
    Vakuumenergie. Je Kantenlaengen-Norm kostet eine Verschiebung bei abs(k) = 0,05 bis 0,07 das 600- bis
    3600-fache der konformen Mode.
- **Ausgeloest ist der Kartenzweig "IZ1 verfehlt, IZ2 trifft ein":**
  - Unordnung macht die Antwort richtungsfrei, aber nicht geometrisch.
  - Ein fester Rest bleibt, der von der Dreiecksform abhaengt.
  - Ue1 braucht ein schwankendes Netz (Summe ueber Netze) oder eine Feinabstimmung.
  - Fuer die Feinabstimmung reicht in 2D ein lokales, isotropes Gegenglied -0,172 Integral (grad sigma)^2 in der
    konformen Mode. Es beseitigt aber nicht die Steifigkeit der Verschiebungen.
- **[H] Warum das Mitteln ueber feste Netze nicht reicht:**
  - Auf einem festen Netz aendert die konforme Mode auch die physikalische Aufloesung: Die Punktdichte je
    physikalischer Flaeche ist rho_0 e^{-2 sigma}.
  - Lokale Glieder in der Aufloesung sind erlaubt und geben k^2-Steifigkeit. Ein Mittel ueber feste Netze entfernt
    sie nicht.
  - Wirkt das Netz lokal wie ein kovarianter Regulator mit Lambda^2 ~ rho, so dreht schon die lokale Weyl-Anomalie
    -1/(24 pi) zu +1/(24 pi) (PLAN Abschnitt 9). Dazu kommt ein nicht universeller Rest; gemessen ist c_D = +0,052,
    also +3,9/(24 pi).
  - Gerechnet ist das nicht.
- **Was ein schwankendes Netz anders macht [L, H]:**
  - In 2D gibt die annealte Summe ueber Triangulierungen mit Materie die Liouville- bzw. Polyakov-Gravitation [L].
  - Dort wird die Punktdichte selbst integriert, und die lokalen Glieder gehen in Kopplungen auf, die ohnehin
    renormiert werden.
  - Die Karte nennt mit "Summe ueber Netze" also den in 2D bekannten Weg. Ob er in 4D traegt, ist offen.
- **Naechste Schritte [H]:**
  - (a) Netz mitschwanken lassen: Pachner-2-2-Flips oder Punktbewegung mit Gewicht det'^{-1/2}, dann die konforme
    Antwort des Ensembles.
  - (b) Die 4phi-Harmonische (INDUZIERT-1 Teil A2) auf Zufallsnetzen mit vielen Saaten. Trifft der universelle
    Anteil auch hier Polyakov?
  - (c) Pruefen, ob c_P(k -> 0) = 1/(2 pi) fuer Poisson-Delaunay exakt ist (Herleitung oder N = 256 000 mit mehr
    Saaten).

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-064409, EINGEFROREN-SHA256.txt
- code/:
  - zufall2d.py: Netze, Kotangens-Laplace, log det' per Erdung und LU, Moden, Differenzen, Kontrollen
  - zufall_auswertung.py: Tor, Urteile, Tabellen, Bilder
  - induziert.py: unveraendert aus INDUZIERT-1 (exakte Blasensumme fuer die Kontrollen)
  - je mit Kopien *.eingefroren-20261004-064409
- lauf-69/:
  - kontrolle.json, regulaer-L256.json, regulaer-L64.json
  - zufall-N4000-s0.json, zufall-N16000-s0.json, zufall-N16000-s12.json, zufall-N64000-s0.json, -s4.json, -s8.json
  - je mit .log, dazu kette-cpu3.log und kette-cpu4.log
  - auswertung.json (Urteile), auswertung.log, PRUEFSUMMEN.txt (.69)
  - Bilder: bild-konform.png, bild-richtung.png, bild-streuung.png, bild-verschiebung.png
- rauch-69/: kontrolle-r1.json/.log, zeit-N64000.json/.log, r2/ (Rauchdaten, Logs, Probe p/ mit Probebildern)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-induziert-zufall/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir wollten wissen, ob ein zufaelliges Netz (wie ein Schaum) besser ist als ein regelmaessiges Gitter, damit die
Schwerkraft sauber aus dem Zittern der Materie entsteht. Das Zufallsnetz hilft bei einer Sache: Seine Antwort ist in
alle Richtungen gleich, waehrend das regelmaessige Gitter je nach Richtung bis zum Doppelten verschieden reagiert. Die
Staerke der Antwort wird aber weiter vom Netz bestimmt und nicht von der Physik: Sie ist zwoelfmal so gross wie die
bekannte richtige Zahl (Polyakov) und hat das falsche Vorzeichen. Ausserdem kostet das blosse Verschieben der Knoten,
das eigentlich gar nichts kosten duerfte, hunderte- bis tausendmal mehr als die echte Verformung. Unordnung allein
reicht also nicht; man braeuchte ein Netz, das selbst mitschwankt, oder muesste die Zahlen von Hand nachstellen.
