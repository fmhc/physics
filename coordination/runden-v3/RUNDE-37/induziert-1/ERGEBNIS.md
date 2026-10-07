# INDUZIERT-1: Ergebnis (Runde 37, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 05:22:30 CEST; Code ab 05:46:52, Plantext ab 05:51:57 CEST.
  - Rauchlaeufe 03:51:54 bis 04:00:50 UTC (PLAN Abschnitt 11).
  - Eingefroren 06:01:47 CEST: PLAN.md.eingefroren-20261004-060147, Code-Kopien *.eingefroren-20261004-060147,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 04:01:55 bis 04:03:47 UTC, Auswertung 04:03:55 bis 04:05:07 UTC, alle rc = 0.
  - Nachtrag-Bild 04:07:46 bis 04:07:47 UTC (beschreibend). Text ab 06:08:38 CEST.
- Nach dem Einfrieren ist der Code unveraendert; die Pruefsummen auf der .69 und lokal stimmen ueberein. Neu ist nur
  code/nachtrag_bild.py (ein Bild, nicht eingefroren, nicht geurteilt).
- Alle Zahlen sind linearisierte Gitterrechnungen auf der .69 (numpy/scipy, float64, Spuren cpu3 und cpu4). Gerechnet
  ist euklidisch, eine Schleife, ein freies Skalarfeld. Synthetisch, keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier keine Quelle abgerufen)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik
  - [E] hier gerechnet
  - [F] Festlegung im Plan
  - [K] Kartenberichtigung
  - [H] Hypothese
- **Konvention:** Pi = Hesse-Matrix von Gamma = 1/2 log det K in s = l^2. Das ist das Vorzeichen von H in REGGE-4D-1:
  Einstein waere c2 > 0 und c0s = -2 c2.

## 1. Ergebnis zuerst

1. **Ein Skalarfeld auf dem festen Kuhn-Netz erzeugt keine Einstein-Steifigkeit [E].** Nach dem Gegenterm (Plan P)
   ist die k^2-Form auf h stark richtungsabhaengig und hat nicht Einsteins Struktur:
   - c2 liegt zwischen -0,00003 (Hyperdiagonale) und +0,0080 (Richtung (1,1,-1,-1)).
   - Der Spin-2-Fuenfer ist aufgespalten, in 6 von 8 Richtungen mit negativen Eigenwerten.
   - Der konforme Modus ist steif und **positiv**: c0s = +0,03 bis +0,12, also c0s/c2 = +3,4 bis +142 statt -2.
   - Die Knotenverschiebungen sind nicht weich, sondern 1,8- bis 30-mal steifer als Spin 2.
   - Ergebnis unabhaengig von der Masse (m^2 0,01 gegen 0,04: c2 aendert sich um <= 7,4 %, 0,0025 gegen 0,04 um <= 9,3 %, ausser auf der
     Hyperdiagonale, wo c2 ~ 0 ist) und vom Gitter (L_q = 48 gegen 64 auf 4 bis 5 Stellen).
   - Keine der fuenf Gegenterm-Varianten trifft -2 auf 10 % in irgendeiner Richtung (am naechsten: G auf der Hyperdiagonale mit -2,8).
2. **2D-Kontrolle: Polyakov ist da, aber verdeckt [E].**
   - Die Steifigkeit der konformen Mode ist c_P = +0,1249 statt -1/(24 pi) = -0,0133, also Faktor -9,4. Sie haengt von
     der Richtung ab: (1,0) 0,125; (1,1) 0,080; (1,-1) 0,170.
   - Der universelle, nicht-analytische Anteil (4phi-Harmonische, Teil A2) trifft Polyakov dagegen auf 0,4 %:
     lambda = 0,9962 bei L = 512 und L = 1024.
   - Die Kette ist also richtig normiert. IN1 scheitert an grossen lokalen Gittertermen, nicht an der Normierung.
3. **Die Vakuumenergie hat nicht die Form eines Volumenterms [E].** Die Metrik-Komponenten von Pi(0) stehen fast
   senkrecht auf der Volumen-Variation (Rest 99,96 %). Auch die Vakuumspannung ist anisotrop: Eigenwerte 0,096 (dreifach)
   und 0,213 laengs der Hyperdiagonale, im Kontinuum waere sie isotrop.
4. **Urteile:** IN0 und IN5 eingetroffen; IN1, IN2, IN3 und IN4 nicht eingetroffen. Nach Kartenwortlaut (reine
   Fusspunkt-Lage des Gegenterms, Variante R2) sind die Urteile gleich.
5. **Bedeutung:**
   - In 2D ist nur der nicht-analytische Anteil des k^2-Terms universell. Ihn trifft das Gitter, der Gesamtkoeffizient
     wird aber von lokalen Gittertermen beherrscht.
   - In 4D ist der Einstein-Term selbst ein solcher lokaler Term (Koeffizient ~ Lambda^2 [L]). Auf einem festen Netz
     ohne kovarianten Regulator legt ihn deshalb nichts fest.
   - Materie allein waehlt die 1/2 hier nicht. Ue1 braucht eine umbenennungsfreie Materie-Diskretisierung oder eine
     Feinabstimmung (Abschnitt 7).

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/induziert_auswertung.py; Werte in lauf-69/auswertung.json. Die Felder
"vermerk" sind per jq nachgetragen; Urteile und Werte sind gegen lauf-69/auswertung.maschine.json identisch (diff).
Tor (Torus-Gegenprobe) bestanden: <= 4,4e-8.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| IN0 | Symbol = sum 4 sin^2(q/2) auf <= 1e-12; Pi(k) hermitesch auf <= 1e-9 | 70 % | **eingetroffen** | gleich | Symbol 5,3e-15 (n = 4); Hermitezitaet 6,0e-16 (alle 4D-Punkte) |
| IN1 | 2D: Steifigkeit/(Flaeche k^2) = -1/(24 pi) auf 3 % beim kleinsten k im Fenster | 55 % | **nicht eingetroffen** | gleich [K1] | c_P = +0,12492 bei L = 1024, n = 8, abs(k) = 0,049; Verhaeltnis -9,42 |
| IN2 | c2 > 0 wie in REGGE-4D-1 | 60 % | **nicht eingetroffen** | nicht eingetroffen | 7 von 8 Richtungen c2 > 0 (0,00076 bis 0,0080); Hyperdiagonale c2 = -3,0e-5 (m^2 0,01) bzw. -6,9e-5 (0,04), bei allen abs(k) |
| IN3 | c0s/c2 = -2 auf 10 % (k -> 0) | 25 % | **nicht eingetroffen** | nicht eingetroffen | r = +3,4 bis +142, Hyperdiagonale -3900 bzw. -1700 (abs(k) = 0,05) |
| IN4 | Knotenverschiebungen <= 5 % der Spin-2-Steifigkeit bei abs(k) = 0,2 | 25 % | **nicht eingetroffen** | nicht eingetroffen | Verhaeltnis 1,78 bis 23 (m^2 0,01), 1,83 bis 30 (0,04); Hyperdiagonale kappa2 < 0 |
| IN5 | Pi(0) weicht in Metrik-Komponenten > 10 % vom Volumen-Vielfachen ab | 70 % | **eingetroffen** | gleich | Rest 0,9996 (m^2 0,01), 0,9992 (0,04); alpha = 0,0044 bzw. 0,0061 |

- Gitterkonvergenz [F13]: Die Urteile auf L_q = 48 sind gleich. Die Kennzahlen der Variante P stimmen zwischen 48 und
  64 auf 4 bis 5 Stellen ueberein (Tabelle 3.3).
- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "IN3 oder IN4 verfehlt" ist ausgeloest: Das feste Netz bricht die Umbenennung auch bei langen Wellen. Materie
    allein waehlt die 1/2 nicht. Ue1 braucht eine umbenennungsfreie Materie-Diskretisierung.
  - "IN5 trifft ein" ist ausgeloest: Ohne Gegenterm macht die Vakuumenergie die Metrik bei k = 0 steif (Variante U:
    Eigenwerte von K/k^2 bei abs(k) = 0,05 von -62 bis +19). Sie muss feinabgestimmt werden.
  - "IN1 verfehlt: Die Kette ist nicht richtig normiert" trifft **nicht** zu. Die Torus-Gegenprobe (4e-8) und Teil A2
    (lambda = 0,996) zeigen, dass die Kette richtig normiert ist. IN1 scheitert an lokalen Gittertermen. Teil B wird
    deshalb nicht nur beschreibend gewertet.

**Agenten-Vorhersagen** (PLAN Abschnitt 9, vor jeder Rechnung)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (95 %) | IN0 eingetroffen | **eingetroffen** |
| A2 (80 %) | Torus-Gegenprobe <= 1e-7 | **eingetroffen**: 4,4e-8 (nach Schrittverkleinerung im Rauchlauf; mit 1e-2 waren es 6,8e-6) |
| A3 (70 %) | IN1 nicht eingetroffen; dGamma/ds_(1,0) = (2/pi - 1)/4 | **eingetroffen**: c_P = -9,4 x Polyakov; dGamma/ds_(1,0) = -0,0908451 = (2/pi - 1)/4 auf 1e-10 |
| A4 (75 %) | c_P-Spanne ueber 3 Richtungen > 10 % | **eingetroffen**: 0,0795 bis 0,1704 (73 % des Mittels) |
| A5 (55 %) | IN2 eingetroffen | **nicht eingetroffen** (Hyperdiagonale) |
| A6 (85 %) | IN3 nicht eingetroffen | **eingetroffen** |
| A7 (85 %) | IN4 nicht eingetroffen | **eingetroffen** |
| A8 (95 %) | IN5 eingetroffen; Pi(0) entlang der Spur negativ, Volumen positiv | **eingetroffen**: s0^T Pi0 s0 = -0,50000 (exakt -1/2 bis O(m^2) [M]), s0^T V'' s0 = +2 |
| A9 (75 %) | Varianten unterscheiden sich in r um > 20 % | **eingetroffen** (z. B. Achse: P 32,6; R1 11,7; R2 81; G 5,9; L 24,2) |
| A10 (60 %) | c2 schwach massenabhaengig (< 10 %) | **teilweise**: 7 von 8 Richtungen <= 7,4 % (0,01 gegen 0,04); Hyperdiagonale (c2 ~ 0) Faktor 2,3 |

## 3. Tabellen

### 3.1 Teil A (2D): Steifigkeit der konformen Mode pro Flaeche und k^2 [E]

(Torus L = 1024, masselos, det'; Polyakov -1/(24 pi) = -0,013263)

| Richtung | abs(k) | c_P (Plan: det' K, Ecken-Skalierung) | det' K linear in l | det' K linear in s | c_D: det'(M^-1 K), ohne Flaechenterm |
|---|---|---|---|---|---|
| (1,0) | 0,0061 | +0,12500 | +0,14771 | +0,17042 | -0,04167 |
| (1,0) | **0,0491 (Urteil)** | **+0,12492** | +0,14763 | +0,17034 | -0,04161 |
| (1,0) | 0,393 | +0,12027 | +0,14269 | +0,16511 | -0,03774 |
| (1,1) | 0,0694 | +0,07946 | +0,14752 | +0,21559 | -0,25320 |
| (1,-1) | 0,0694 | +0,17034 | +0,14763 | +0,12493 | +0,17042 |

- **Endliche Groesse:** abs(k) = 0,0491 auf L = 256, 512 und 1024 gibt c_P = 0,12492 dreimal gleich.
- **Tadpole:** dGamma/ds = (-0,0908451; -0,0908451; +0,0908451) fuer (1,0), (0,1), (1,1). Die Werte sind
  (2/pi - 1)/4 [M, A3], Summe mit s gewichtet 0 (Skaleninvarianz in 2D).
- **Grenzwerte k -> 0** [E, Identifikation H]: c_P(1,0) = 0,12500 = 1/8, c_P(1,1) = 0,0796 = 1/(4 pi),
  c_P(1,-1) = c_s(1,0) = 0,17042 = (1 - 1/pi)/4.
  - Die l-lineare Fassung ist isotrop: 0,14771 = 3/16 - 1/(8 pi).
  - c_D(1,0) = -0,04167 = -1/24.
  - Die Zahlen sind numerisch erkannt und nicht hergeleitet. Sie zeigen, dass die lokalen Terme Gitterkonstanten der
    Art 2/pi sind (wie Widerstaende im Quadratgitter [L]).
- **Knotenverschiebungen (beschreibend):** roh ~ 1/k^2 (Vakuumenergie). Mit Gegenterm (in 2D ganz Pi(0), symmetrisch
  gelegt) liegen sie bei 0,000 bis 0,027 k^2, also so steif wie die konforme Mode (0,004 k^2) oder steifer, und in
  (1,-1) einmal negativ.
- Bild: lauf-69/bild-teilA.png.

### 3.2 Teil A2 (2D, beschreibend): universeller Polyakov-Anteil [E]

| L | abs(k) | Richtungen | lambda = gemessen/Polyakov | Rest |
|---|---|---|---|---|
| 512 | 0,049 bis 0,147 | 198 | **0,99625** | 0,43 % |
| 1024 | 0,025 bis 0,074 | 198 | **0,99621** | 0,43 % |

- Zum Beispiel (L = 1024) cos(4phi)-Koeffizient von h01-h01: gemessen 0,0016538, Polyakov 0,0016579. sin(4phi) von h00-h01:
  -0,0011723 gegen -0,0011723 (auf 1e-5); h00-h00 -0,000820 gegen -0,000829 (1,1 %).
- Die Fit-Reste (rms) liegen bei <= 2,8e-5, bei Eintraegen der Groesse 1e-2 (relativ <= 1,2e-3).
- Bild: lauf-69/bild-teilA2-harmonische.png. Die Gitterpunkte liegen nach Abzug der Moden 0 und 2 auf Polyakovs Kurve.

### 3.3 Teil B (4D), Plan P, abs(k) = 0,05, L_q = 64 [E]

| Richtung | c2 (m^2 0,01) | c0s | r = c0s/c2 | Spin-2-Eigenwerte/k^2 | c2 (m^2 0,04) | r (0,04) | Eich/Spin2 bei 0,2 (0,01; 0,04) |
|---|---|---|---|---|---|---|---|
| (1,0,0,0) | 0,00222 | 0,0724 | 32,6 | -0,0034 (2x); 0,0024; 0,0078 (2x) | 0,00206 | 35,2 | 3,8; 4,3 |
| (1,1,0,0) | 0,00295 | 0,0819 | 27,8 | -0,0015; -0,0012; 0,0054; 0,0055; 0,0065 | 0,00285 | 28,8 | 3,9; 4,0 |
| (1,-1,0,0) | 0,00498 | 0,0372 | 7,5 | -0,0047; 0,0027; 0,0053; 0,0059; 0,0158 | 0,00485 | 7,7 | 1,8; 1,8 |
| (1,1,1,0) | 0,00153 | 0,1014 | 66 | -0,0021; -0,0005 (2x); 0,0054 (2x) | 0,00146 | 69 | 4,7; 4,9 |
| (1,1,1,1) | **-0,00003** | 0,1184 | -3900 | -0,0036 (3x); 0,0053 (2x) | **-0,00007** | -1700 | kappa2 < 0 |
| (1,1,-1,-1) | 0,00804 | 0,0277 | 3,4 | 0,0006; 0,0057; 0,0083; 0,0128 (2x) | 0,00788 | 3,5 | 3,0; 3,0 |
| (1,1,1,-1) | 0,00469 | 0,0585 | 12,5 | 0,0026 (2x); 0,0056; 0,0063 (2x) | 0,00456 | 12,8 | 3,4; 3,5 |
| (1,2,3,4) | 0,00082 | 0,1088 | 132 | -0,0036; -0,0028; -0,0004; 0,0054; 0,0055 | 0,00076 | 143 | 23; 30 |

- **Ergaenzend (m^2 0,01, 0,05):**
  - c1 = -0,0044 bis 0,0061 und c0w = 0,005 bis 0,062. Im Kontinuum waeren beide null (Eichsektor).
  - Spinmischung 2-0 bis 0,25.
  - Abweichung von k^2 c2 (P2 - 2 P0s) (normiert): 2,5- bis 66-fach, Hyperdiagonale 2000-fach.
- **k-Abhaengigkeit:** abs(k) = 0,025 und 0,05 geben c2 auf 1e-4 relativ gleich; das sind echte k^2-Koeffizienten.
  Bis 0,4 aendert sich c2 um <= 4,6 % (ausser Hyperdiagonale).
- **Gitter:** L_q = 32, 48, 64 geben c2 und r auf 3 bis 5 Stellen gleich (Achse m^2 0,01: 0,002220 / 0,002219 /
  0,002219). Die in auswertung.json genannte groesste Abweichung (4,3 %) stammt aus Groessen nahe null.
- **Masse:** m^2 = 0,0025 / 0,01 / 0,04 gibt c2(Achse) = 0,002261 / 0,002219 / 0,002061 (UV-dominiert, wie erwartet).
- **Schur gegen direkt:** gleich auf 1e-4 relativ bei 0,05, wie vorhergesagt (Metrik-Teil, Schur erst in O(k^4)).
- Bilder: lauf-69/bild-teilB-n4.png (c2, r, Eichverhaeltnis ueber abs(k) je Richtung und Masse) und
  lauf-69/bild-nachtrag-c0s-c2.png (c0s gegen c2 mit Einsteins Gerade; Nachtrag, beschreibend).

### 3.4 Gegenterm-Varianten (m^2 0,01, abs(k) = 0,05) [E]

| Variante | c2-Bereich ueber 8 Richtungen | r-Bereich | Eich/Spin2 (0,05) |
|---|---|---|---|
| P (Plan: Metrik-Teil, symmetrisch) | -0,00003 bis 0,0080 | 3,4 bis 132; Hyper -3900 | 1,8 bis 23 |
| R2 (Kartenwortlaut: Fusspunkt) | -0,00099 bis 0,0086 | 3,2 bis 81; Hyper -128; (1,2,3,4) -1246 | 3,8 bis 132 |
| R1 (Taylor in Mittelpunkts-Konvention) | 0,00059 bis 0,0084 | 4,3 bis 204 | 1,0 bis 6,6 |
| G (ganz abgezogen) | -0,0055 bis 0,026 | -79 bis 5,9 | 1,6 bis 8,7 |
| L (Laengen statt Quadrate) | 0,00016 bis 0,0082 | 3,4 bis 734 | 1,7 bis 11 |
| U (roh, ohne Gegenterm) | -15,6 bis +10,8 | -5,3 bis 15 | 0,35 bis 5,4 |

- Keine Variante trifft in irgendeiner Richtung -2 auf 10 %. Am naechsten liegen U (roh, Hyperdiagonale -2,31) und G (Hyperdiagonale -2,77). Nur G und U haben c0s < 0; G hat dabei c2 mit beiden
  Vorzeichen.
- Die Lage des Gegenterms (P gegen R1 gegen R2) aendert c2 in einzelnen Richtungen um einen Faktor 2 bis 6. Das ist die
  in PLAN Abschnitt 5 erwartete Mehrdeutigkeit: Pi(0) ~ 0,05 bis 0,2, c2 ~ 0,002.

### 3.5 Vakuumteil bei k = 0 (IN5) [E]

- Metrik-Block B0^T Pi0 B0, Eigenwerte (m^2 0,01): -0,184; -0,082; -0,064 (3x); +0,031 (3x); +0,048 (2x).
- Volumen B0^T V'' B0: -0,5 (9x), +0,5 (Spur), wie im Kontinuum [M].
- Bestes alpha = 0,0044, Rest 99,96 %. Mit Schur-Fassung 98,6 %, voll 15 x 15 42 %.
- **Exakte Probe [M]:** Entlang der Spur gilt s0^T Pi0 s0 = -0,50000 (m^2 = 0,0025: -0,5000002), weil K bei Streckung
  um lambda wie lambda^2 skaliert. Das Volumen gibt +2. Schon das Vorzeichenmuster verbietet ein Vielfaches.
- **Vakuumspannung** dGamma/ds je Kantentyp: Achsen 0,0475; Flaechendiagonalen 0,0231; Raumdiagonalen 0,0023;
  Hyperdiagonale 0,0014. Das Volumen hat nur auf den Achsen einen Gradienten (0,5), auf den Diagonalen 0.
  - Als Matrix: T_mu_nu = 0,125 delta_mu_nu + 0,029 (1 - delta_mu_nu), Eigenwerte 0,096 (3x) und 0,213 (laengs (1,1,1,1)); im Kontinuum waere T proportional zu delta.
- **Pi0 - CT** (Gittermoden nach dem Metrik-Teil): Eigenwerte -0,010; 0,054 (3x); 0,230. Eine Gittermode ist bei
  k = 0 leicht instabil.

### 3.6 Leitungszusatz (beschreibend, nicht geurteilt): Richtungsabhaengigkeit im kleinsten k

Nachricht der Leitung waehrend des Plantexts, vor dem Einfrieren in den Plan aufgenommen. Plan P, L_q = 64.

| Gruppe | Richtung | c2 (0,025; m^2 0,01) | r (0,025) | c2 (0,025; m^2 0,04) | r |
|---|---|---|---|---|---|
| Achse | (1,0,0,0) | 0,002219 | 32,6 | 0,002061 | 35,1 |
| Flaechendiagonale | (1,1,0,0) / (1,-1,0,0) | 0,002944 / 0,004984 | 27,7 / 7,45 | 0,002852 / 0,004846 | 28,7 / 7,69 |
| Raumdiagonale | (1,1,1,0) | 0,001534 | 65,7 | 0,001465 | 69,0 |
| Hyperdiagonale | (1,1,1,1) | -0,000030 | -3950 | -0,000069 | -1717 |
| uebrige | (1,1,-1,-1) / (1,1,1,-1) / (1,2,3,4) | 0,00804 / 0,00469 / 0,00082 | 3,44 / 12,4 / 131 | 0,00788 / 0,00456 / 0,00076 | 3,52 / 12,8 / 142 |

- **Streuung ueber die 8 Richtungen (P, abs(k) = 0,025, m^2 0,01):**
  - c2: Spanne/abs(Mittel) = 2,56; Standardabweichung/abs(Mittel) = 0,78 (78 %).
  - r: Spanne/abs(Mittel) = 8,9, Standardabweichung 2,9 (wegen der Hyperdiagonale).
  - Bei m^2 0,04 und 0,0025 praktisch gleich (c2: 0,80 bzw. 0,78), ebenso bei 0,05.
- **Andere Varianten (abs(k) = 0,05, m^2 0,01):**
  - c2-Standardabweichung/abs(Mittel): P 0,78; R2 1,07; U (roh) 2,8.
- **Vergleich:** REGGE-4D-1 mit eingegebener Regge-Wirkung: c2 = 0,24991 bis 0,24999 bei 0,05, also 0,03 % Spanne.
  Induziert: Spanne 256 %, Standardabweichung 78 %.
- Auch Richtungen mit gleichem Betragsmuster unterscheiden sich: (1,1,0,0) gegen (1,-1,0,0) 0,0029 gegen 0,0050;
  (1,1,1,1) gegen (1,1,-1,-1) -0,00003 gegen 0,0080. Die ausgezeichnete Hyperdiagonale des Kuhn-Netzes schlaegt bis in
  den k^2-Teil durch.

### 3.7 3D (beschreibend) [E]

- Kontinuum waere c0s/c2 = -1.
- Gerechnet (P, L_q = 128, abs(k) = 0,05): c2 von -0,082 bis +0,020, r von -38 bis +5,3.
- Der Metrik-Block von Pi(0) ist fast singulaer (kleinster Eigenwert 9,5e-4 bzw. 1,4e-4). Der Metrik-Gegenterm ist
  deshalb schlecht konditioniert, und P haengt in 3D stark von der Masse ab (Achse c2 -0,082 gegen -0,615). P ist
  in 3D nicht belastbar.
- Variante G (ganz): c2 -0,018 bis +0,020, r -247 bis 94. Auch hier nirgends -1.

## 4. Kartenberichtigungen (vor dem Einfrieren offengelegt) und was daraus wurde

- **K1 (Flaechenglied):**
  - Das "globale Flaechenglied" der Karte gehoert zu det'(M^-1 K), nicht zu det' K. Exakt gilt
    det'(M^-1 K) = det' K A/(N det M) [M].
  - In der Karten-Groesse c_P gibt es also kein Flaechenglied. In c_D faellt es exakt heraus.
  - Selbst das kontinuierliche Flaechenglied (1/2)(log A)'' haette bei L = 1024, n = 8 nur 4e-4 zu c beigetragen,
    also 0,3 % von c_P. Das Urteil haengt nicht daran.
- **K2 (Lage des Gegenterms):**
  - Ein reiner Fusspunkt-Gegenterm bricht die Inversionssymmetrie. Er bringt einen ungeraden O(k)-Anteil, der nur im
    Schur-Komplement und in den Eigenwerten wirkt.
  - Plan: symmetrisch an Anfangs- und Endpunkt.
  - Nach Kartenwortlaut (R2) sind alle Urteile gleich (Tabelle 2, Spalte "Kartenwortlaut"). R2 ist in der Eich- und
    Hyperdiagonalen-Groesse sogar noch weiter von Einstein entfernt (Tabelle 3.4).

## 5. Kontrollen

- **Torus-Gegenprobe (Tor):** Blasensumme gegen direkt per slogdet gerechnetes 1/2 log det.
  - Ebene Wellen in 2D (L = 16, masselos und m^2 0,04), 3D (L = 6) und 4D (L = 5, masselos und m^2 0,04).
  - Dazu die konforme Mode (Ecken-Skalierung) in 2D und der Tadpole-Vektor gegen erste Differenzen.
  - Hoechstens 4,4e-8 relativ; Tadpole <= 1e-9.
- **Lokale Ableitungen:** analytisch gegen komplexen Schritt 1,8e-16 bis 4,4e-16 (dK) und 6e-16 bis 8e-16 (d2K). Gegen
  die zentrale Differenz komplexer Schritte 2e-8 bis 3,5e-8 (h = 1e-4, Abbruchfehler).
- **Symbol:** 5,3e-15 (n = 4), 3,6e-15 (n = 3), 1,8e-15 (n = 2). Das Stencil-Gewicht der Diagonalkanten ist exakt 0:
  Auf dem flachen Kuhn-Netz ist die P1-Steifigkeit der Wuerfelgitter-Laplace [M, Plan Abschnitt 2].
- **Konventionen:** Imaginaerteil von Pi^mid <= 1,4e-17 relativ, also reell wie vorhergesagt. Separables Symbol gegen
  allgemeines auf allen Gittern <= 1,2e-14.
- **Skalierungsidentitaeten [M]:**
  - 2D: Summe dGamma/ds s = 0 auf 1e-16.
  - 4D: s0^T Pi0 s0 = -1/2 + O(m^2), s0^T V'' s0 = 2; V_Zelle = 1, Massenmatrix 1 je Knoten.
- **Gitter und Masse:** siehe 3.3; L = 256/512/1024 in 2D gleich auf 1,5e-5 relativ (c_P 0,1249217 / 0,1249231 / 0,1249235).

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - IN2 bis IN4 haetten eintreffen koennen; Sakharov im Kontinuum sagt genau das [L].
  - Teil A2 haette lambda != 1 ergeben koennen; auch die Gegenprobe kann scheitern.
  - Meine eigenen A5 (IN2) und A10 (teilweise) sind gescheitert.
- **L2 (Gegenprobe):**
  - Torus direkt gegen Blase, analytisch gegen komplexen Schritt
  - Gitter 32/48/64, drei Massen, fuenf Gegenterm-Varianten
  - Schur gegen direkt, 2D in drei Torusgroessen
  - die universelle 4phi-Harmonische als unabhaengige Normierung
- **L3 (Numerik):** 1e-8 bis 1e-16.
- **L4 (schon bekannt):**
  - Sakharov 1967, Visser 2002: Im Kontinuum mit kovariantem Regulator entstehen nur Volumen- und
    Kruemmungsterm [L].
  - Dass ein nicht kovarianter Regulator (Gitter, harter Impulsschnitt) nicht kovariante lokale Terme der Ordnung
    Lambda^2 erzeugt, ist bekanntes Feinabstimmungs-Problem [L, z. B. Collins/Perez/Sudarsky/Urrutia/Vucetich 2004 fuer
    Lorentz-Verletzung; nicht an der Quelle geprueft].
  - Polyakov 1981 [L]. Neu hier: die Zahlen fuer das Kuhn-Netz und die Trennung universell gegen lokal ueber die
    4phi-Harmonische.
  - Ob die Grenzwerte 1/8, 1/(4 pi), (1 - 1/pi)/4 bekannt sind, weiss ich nicht [L?].
- **L5 (Messbezug):** keiner. Indirekt: Die gemessene Isotropie der Gravitation (z. B. GW170817, Sonnensystem [L]) waere
  mit der hier gefundenen Anisotropie (Standardabweichung von c2 78 %) ohne Feinabstimmung unvereinbar [H].

## 6. Selbstanzeigen

1. **IN1 vor dem Einfrieren absehbar.** Der Rauchlauf teilA (L = 64, 128) zeigte c_P = +0,1249 und Teil A2 zeigte
   lambda = 0,998. Plan, Festlegungen und Schwellen standen da schon (PLAN Abschnitt 11).
2. **4D-Zahlen vor dem Einfrieren nicht angesehen.** Rauchlaeufe teilB liefen nur fuer Laufzeit und Codeprobe; die
   Probe-Urteile habe ich nicht gelesen. Die IN2-Ueberraschung (Hyperdiagonale) war fuer mich neu.
3. **Code vor dem Einfrieren geaendert:**
   - Schritt der Torus-Gegenprobe 1e-2 -> 2,5e-3 (Abbruchfehler; Schwelle unveraendert).
   - Teil A2 und Leitungszusatz ergaenzt, beide beschreibend.
   - Probe-Schalter probe16.
4. **Nach dem Einfrieren:** kein Code geaendert. Neu nur nachtrag_bild.py (ein Bild aus auswertung.json).
5. **Bild bild-teilB-n4.png:** Die r-Achse wird von der Hyperdiagonale (r ~ -4000) bestimmt, das Band um -2 ist darin
   nicht lesbar. Deshalb das Nachtrag-Bild c0s gegen c2.
6. **auswertung.json nachbearbeitet:** Die Felder "vermerk" sind per jq eingetragen. Urteile und Werte sind gegen
   auswertung.maschine.json identisch.
7. **Festlegungen mit Gewicht:**
   - [F3] Ecken-Skalierung (in 2D aendert die Fortsetzung zweiter Ordnung c um bis zu 0,05, Tabelle 3.1)
   - [F9] Metrik-Teil
   - [K2] symmetrische Lage
   - Keine Wahl bringt IN1 oder IN3 in die Naehe der Schwellen (3.1, 3.4).
8. **Spuren und Laeufe:**
   - cpu3 und cpu4, nie mehr als zwei zugleich.
   - 25 Starts: 12 Rauch, 12 Haupt (mit Auswertung), 1 Nachtrag. Der laengste dauerte 72 s (Auswertung).
   - Kein Interpreterstart ausserhalb des Starters, keine Versionsprobe.
9. **Lokal:** kein python, awk oder perl. Benutzt habe ich jq, sed, grep, sha256sum, date, ssh, scp, dazu cp, mkdir und
   ls.
10. **Reichweite:**
    - Ein freies, minimal gekoppeltes Skalarfeld, P1 auf einem festen Kuhn-Netz.
    - Euklidisch, eine Schleife, lineare Antwort um das flache Netz.
    - Andere Felder (Fermionen, Eichfelder) oder andere Diskretisierungen sind nicht gerechnet.
11. **Zeitbox:** Start 05:22:30, Text ab 06:08:38 CEST, innerhalb von 150 min.

## 7. Bedeutung

- **Zu Ue1 ("Schwerkraft als Echo der Materie"):** Auf Finns festem Laengennetz erzeugt ein Skalarfeld zwar eine
  Steifigkeit gegen Verbiegen, aber nicht Einsteins. Die induzierte Steifigkeit
  - haengt stark von der Richtung ab (Standardabweichung von c2 ueber 8 Richtungen 78 %),
  - hat negative Spin-2-Anteile,
  - macht den konformen Modus positiv und steif,
  - laesst die Knotenverschiebungen nicht frei.
  Sakharovs Argument "nur Volumen und Kruemmung sind moeglich" braucht einen kovarianten Regulator [L]. Das feste Netz
  ist keiner.
- **Was der 2D-Teil lehrt:**
  - Der universelle Anteil (Polyakov, lambda = 0,996) kommt richtig heraus, die Kette rechnet also richtig.
  - Der k^2-Koeffizient ist trotzdem von lokalen Gittertermen beherrscht, die rund zehnmal groesser sind.
  - In 4D gibt es keinen universellen k^2-Anteil, der Einstein-Term ist selbst lokal (~ Lambda^2). Ihn legt auf einem
    festen Netz nichts fest.
- **Fuer P3 (die 1/2 aus Symmetrie):** Mit diesem Netz nicht erreichbar. Moegliche Auswege [H]:
  - eine umbenennungsfreie Materie-Diskretisierung, die Knotenverschiebungen exakt respektiert (vgl. PONZANO-1,
    Pachner-invariante Bauweisen);
  - Mittelung ueber viele Netze bzw. ein dynamisches Netz;
  - lokale Gegenterme, also Feinabstimmung der Art Collins et al. [L].
- **Finns Weiche "feste Nachbarn oder nicht" (Leitungszusatz):** Ein festes Netz zeigt seine Richtungen nicht nur bei
  kurzen Wellen. Ueber die Materie schlagen sie voll bis in den langwelligen k^2-Teil der Schwerkraft durch: 78 % Streuung
  (Standardabweichung von c2; Spanne 256 %) gegen 0,03 % Spanne bei eingegebener Regge-Wirkung. Das spricht gegen "feste Nachbarn plus induzierte Gravitation"
  ohne zusaetzliche Symmetrie [H].
- **Naechste Schritte [H]:**
  - (a) Dasselbe mit einer Diskretisierung, die Knotenverschiebungen respektiert, zum Beispiel einer
    Mittelung ueber zufaellige Delaunay-Netze. Wird die Anisotropie dann klein?
  - (b) Die universellen Anteile in 4D (k^4 log k^2: Weyl^2 und R^2) wie in Teil A2 ueber Winkelstruktur pruefen.
    Diese Zahlen sollten auch auf dem Gitter stimmen.
  - (c) Pruefen, ob eine Kombination Skalar plus Regge-Gegenterm eine abgestimmte Einstein-Form erreicht, und wie
    viele Parameter das kostet.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-060147, EINGEFROREN-SHA256.txt, KARTE.md (Leitung)
- code/:
  - induziert.py: Simplex-Ableitungen, Blasensumme per FFT, Torus-Gegenprobe, Teil A, A2, B
  - induziert_auswertung.py: Gegenterme, Schur, Spins, Urteile, Bilder
  - regge4d.py: unveraendert aus REGGE-4D-1
  - je mit Kopien *.eingefroren-20261004-060147
  - nachtrag_bild.py: Nachtrag, nicht eingefroren
- lauf-69/:
  - kontrolle.json, teilA.json, teilB-n4-m{0.0025,0.01,0.04}-L{32,48,64}.json (vorhandene Kombinationen),
    teilB-n3-m{0.01,0.04}-L128.json, je mit .log
  - auswertung.json (Urteile mit Vermerken), auswertung.maschine.json, auswertung.log
  - Bilder: bild-teilA.png, bild-teilA2-harmonische.png, bild-teilB-n4.png, bild-teilB-n3.png,
    bild-nachtrag-c0s-c2.png
  - PRUEFSUMMEN.txt (.69), PRUEFSUMMEN-NACHTRAG.txt
- rauch-69/: kontrolle-r1.json/.log, kontrolle.json und kontrolle-r2.log, teilA.json und teilA-r1.log, teilB-n4-m0.04-L16/L64.json mit teilB-r1/r2.log, p1/ (Probe), p2/ (teilA2 rauch, grobe teilB, Probe der Urteilslogik)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde37-induziert/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir wollten wissen, ob die Schwerkraft von selbst entsteht, wenn auf Finns Strich-Netz ein Materiefeld zittert, ohne
dass man Einsteins Regel hineinsteckt. Das Zittern macht das Netz tatsaechlich steif gegen Verbiegen. Diese
Steifigkeit sieht aber nicht wie Einsteins Schwerkraft aus: In verschiedene Richtungen ist sie verschieden stark
(bis zum Zehnfachen), manche Verbiegungen kosten sogar negative Energie, und blosses Verschieben der Knoten, das gar
nichts veraendern duerfte, kostet mehr als echte Kruemmung. In der zweidimensionalen Kontrolle steckt die bekannte
richtige Zahl (Polyakov) zwar drin, wird aber von zehnmal groesseren "Netzeffekten" ueberdeckt. Auf einem festen Netz
kommt die Schwerkraft also nicht sauber aus der Materie heraus; dafuer braeuchte man ein Netz ohne Vorzugsrichtungen
oder muesste die Zahlen von Hand abstimmen.
