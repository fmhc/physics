# INDUZIERT-WILSON-2D: Ergebnis (Runde 40, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 11:32:47 CEST. Schreibtisch W4 ab 11:36, drei Abrufe 11:40:06 bis 11:40:11, Code ab 11:42:45,
    Agenten-Vorhersagen 11:47:21, Plantext ab 11:49:26 CEST.
  - Rauchlaeufe und Proben 09:46:05 bis 09:56:23 UTC (PLAN Abschnitt 11).
  - Eingefroren 11:57:13 CEST: PLAN.md.eingefroren-20261004-115713, Code-Kopien *.eingefroren-20261004-115713,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 09:57:20 bis 10:59:21 UTC (17 Bloecke, alle rc = 0), Auswertung 10:59:22 bis 10:59:28 UTC (rc = 0).
  - Text ab 13:02:34 CEST.
- Plan und Code sind nach dem Einfrieren unveraendert; die sha256 stimmen lokal und auf der .69 (vor dem Start und
  vor der Auswertung geprueft).
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64; Spuren cpu und cpu7). Gerechnet
  ist euklidisch, eine Schleife, freie masselose Felder auf festem Hintergrund. Synthetisch, keine Messdaten.
- **Kennzeichen:** [E] hier gerechnet, [M] eigene Mathematik, [S] an der Quelle gelesen (quellen/), [F] Festlegung im
  Plan, [K] Kartenpunkt, [H] Hypothese, [L] Literatur aus dem Gedaechtnis.
- **Bezeichnungen:** P = -1/(24 pi). c_eff = (Gamma''/(k^2 A))/P mit Gamma_F = -1/2 log det'(D^T D) fuer Fermionen
  (Grassmann) und Gamma_B = +1/2 log det' K fuer den Skalar; Dirac +1, Skalar +1. W1 und W05: Wilson-Fermion
  D_W = D_A + r eps K mit r = 1 bzw. 1/2. E1/E2: Netzabstand eps = 1 bzw. 2 (N = 16 001), x = (k eps)^2.

## 1. Ergebnis zuerst

1. **Das Wilson-Glied hebt das Band bei E = 0 vollstaendig an [E].** Ohne Wilson-Glied liegen bei N = 16 001 alle 22
   berechneten Singulaerwerte unter 0,0011. Mit r = 1 oder 1/2 reproduzieren die 22 tiefsten von null verschiedenen
   Singulaerwerte die ersten drei Stufen eines einzelnen Dirac-Fermions im Kontinuum auf 1 bis 1,5 %.
2. **Die Schwerkraft-Antwort ist trotzdem nicht die eines Dirac-Fermions [E]:** c_eff(W1) = **-1,00 +- 0,55**,
   c_eff(W05) = **-0,26 +- 0,56** (64 + 72 Saaten). Der Skalar auf denselben Netzen gibt 0,89 +- 0,14.
   - Der Wert haengt von r ab: Die gepaarte Differenz r = 1/2 minus r = 1 ist **+0,72 +- 0,04** und in allen Lesarten
     0,55 bis 0,87. Eine universelle Anomaliezahl kann nicht von r abhaengen; das k-Fenster (k eps = 0,05 bis 0,6) ist
     fuer das Wilson-Fermion also nicht im Grenzbereich, oder das Zufallsnetz gibt ein r-abhaengiges Zusatzglied [H].
3. **Rauschen [E]:** Das Wilson-Fermion streut je Saat 4,1-mal so stark wie der Skalar (das naive Fermion 7-mal). Die
   Ursache ist nicht mehr das Band, sondern der schwere Teil: Gamma_W ~ -4 Gamma_B + Rest. Die Kombination W1 + 4 B
   streut nur 0,19-mal so stark wie der Skalar und gibt c_eff(W1) + 4 c_eff(B) = 2,55 +- 0,04 (Kontinuum: 5).
4. **Schreibtisch W4 [M, S]:** Die Kaehler-Dirac-Herleitung des Vorgaengers haelt. abs det'(d + delta) = det'Delta_0
   det'Delta_2, Delta_2 isospektral zu Delta_0, also c_KD = -4 im Kontinuum. Die naive Waermeleitungssumme (+2) gilt
   nicht, weil Delta_1 unter Weyl-Skalierung nicht kovariant ist.
5. **Urteile:** W0 eingetroffen, W1 nicht eingetroffen (nach unten verfehlt), W2 nicht eingetroffen, W3 nicht
   eingetroffen (nach Kartenwortlaut eingetroffen), W4 eingetroffen. Von den vorab festgelegten Bedeutungszweigen ist
   nur "W4 haelt" ausgeloest.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/wilson_auswertung.py; Werte in lauf-69/auswertung.json (unbearbeitet).
Vorbedingungen: Tor Netz, W1 und W05 bestanden; 64 (E1) und 72 (E2) Saaten; Modellprobe p >= 0,01 fuer W1 (0,60),
W05 (0,60) und die Differenz W05 - W1 (0,07).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| W0 | Kontrolle: Skalar und (A) ohne Wilson auf denselben Saaten bitgleich mit INDUZIERT-DIRAC-2D | 85 % | **eingetroffen** | eingetroffen | Skalar 2 112 von 2 112 (E1, 64 Saaten) und 2 376 von 2 376 Werten (E2, 72 Saaten) gleich; (A) 264 von 264 (8 Saaten) und 297 von 297 (9 Saaten); groesste Abweichung 0 |
| W1 | [H] Wilson r = 1: c_eff im Band [0,7; 1,3] mit SE <= 0,3 | 40 % | **nicht eingetroffen** | nicht eingetroffen | c_eff(W1) = -0,995 +- 0,552 (Birge 1, p = 0,60); Abstand zum Band 1,70 = 3,1 SE; SE > 0,3 |
| W2 | [H] Streuung je Saat des Wilson-Fermions hoechstens doppelt so gross wie die des Skalars | 55 % | **nicht eingetroffen** | nicht eingetroffen | Q(W1) = 4,11 +- 0,01 (je Zelle 4,09 bis 4,13); Q(W05) = 4,28 +- 0,03; SE(c_eff) W1/B = 4,0 |
| W3 | [H] r = 1/2 und r = 1 stimmen innerhalb 2 SE ueberein | 55 % | **nicht eingetroffen** | eingetroffen | Delta = c_eff(W05) - c_eff(W1) = +0,736; SE gepaart 0,042 (17,6 SE); ungepaart 0,78 (0,94 SE) |
| W4 | Schreibtisch: Die KD-Beziehung gilt, und c_KD = -4 in der Normierung der Karte (Kontinuum) | 75 % | **eingetroffen** | eingetroffen | Herleitung Abschnitt 5 (PLAN Abschnitt 1), vor jeder Rechnung |

- **Lesart W1:** nach unten verfehlt, nicht nach oben. Das Urteil haengt aber am Modell (Abschnitt 3.2): Mit k^6-Glied
  ist c_eff(W1) = 0,89 +- 1,50, im Fenster k eps <= 0,4 0,38 +- 1,25, also nicht entschieden. Die rauscharme
  Kombination W1 + 4 B verwirft das Modell der Karte (k^0, k^2, k^4) mit p < 0,001; fuer W1 allein faellt das wegen
  des Rauschens nicht auf.
- **Lesart W3:** Gepaart (beide r auf denselben Netzen) ist der Unterschied scharf bestimmt und gross. Ungepaart, wie
  die Karte es lesen laesst, verdeckt das Rauschen ihn.

**Agenten-Vorhersagen** (PLAN Abschnitt 10, notiert 11:47:21 CEST)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| C1 (85 %) | Tor besteht in allen Hauptlaeufen | **eingetroffen**: 2 176 Bildnetze und 136 Grundnetze ohne Fehler |
| C2 (95 %) | W0 bitgleich | **eingetroffen** |
| C3 (60 %) | c_eff(W1) Punktwert in [0,7; 1,3] | **nicht eingetroffen**: -0,995 |
| C4 (55 %) | Q(W1) <= 2 | **nicht eingetroffen**: 4,11 (aus der Probe vor dem Einfrieren schon absehbar, Abschnitt 7) |
| C5 (60 %) | abs Delta <= 2 SE gepaart | **nicht eingetroffen**: 17,6 SE |
| C6 (60 %) | abs d_eff(W05) > abs d_eff(W1) | **eingetroffen** (Punktwerte 2,10 gegen 1,19; gepaart d_eff(W05 - W1) = +0,94 +- 0,11). Meine Begruendung (k^4 ~ 1/r^2) passt aber nicht zum Befund; siehe Abschnitt 8 |
| C7 (70 %) | Skalar: c_eff(B) in [0,6; 1,4] | **eingetroffen**: 0,888 |

## 3. Tabellen [E]

### 3.1 Gemeinsamer Ausgleich (E1 + E2; 64 + 72 Saaten; c_eff und d_eff in Einheiten von P)

| Operator | c_eff(0) | SE (GLS mit Birge) | Jackknife-SE | d_eff | p (5 FG) |
|---|---|---|---|---|---|
| Skalar B | **+0,888** | 0,137 | 0,143 | -1,05 +- 0,36 | 0,66 |
| Wilson r = 1 (W1) | **-0,995** | 0,552 | 0,577 | +1,19 +- 1,46 | 0,60 |
| Wilson r = 1/2 (W05) | **-0,259** | 0,555 | 0,578 | +2,10 +- 1,47 | 0,60 |
| W05 - W1 (gepaart) | **+0,720** | 0,042 (GLS 0,029, Birge 1,43) | 0,031 | +0,94 +- 0,11 | 0,07 |
| W1 - B (gepaart) | -1,88 | 0,69 | 0,72 | +2,24 +- 1,82 | 0,61 |
| W05 - B (gepaart) | -1,15 | 0,69 | 0,72 | +3,15 +- 1,84 | 0,61 |
| W1 + 4 B (gepaart; Kontinuum 5) | **+2,545** | 0,043 (GLS 0,019, Birge 2,25) | 0,023 | -2,98 +- 0,12 | < 0,001 |
| W05 + 4 B (gepaart; Kontinuum 5) | **+3,267** | 0,075 (GLS 0,047, Birge 1,59) | 0,051 | -2,04 +- 0,20 | 0,027 |

- **Kontrollvariable** (beschreibend, nach dem Rauchlauf festgelegt): c_eff(W) = c_eff(W + 4 B) - 4 c_eff(B) mit dem
  Skalar aus allen 96 + 96 Saaten des Vorgaengers (0,922 +- 0,120): W1 -1,14 +- 0,48, W05 -0,42 +- 0,49. Der Fehler
  kommt fast ganz vom Skalar (4 x 0,12).

### 3.2 Lesarten (beschreibend; c_eff +- SE, p)

| Operator | nur E1 | nur E2 | mit k^6 | a je Datensatz | Fenster k eps <= 0,4 | nur k^2, Fenster 0,4 |
|---|---|---|---|---|---|---|
| Skalar B | 0,16 +- 0,56 (0,45) | 0,92 +- 0,17 (0,36) | 0,47 +- 0,37 (0,77) | 0,89 +- 0,14 (0,52) | 0,59 +- 0,31 (0,72) | 0,73 +- 0,08 (0,80) |
| W1 | 2,04 +- 2,27 (0,42) | -1,17 +- 0,71 (0,30) | 0,89 +- 1,50 (0,77) | -1,00 +- 0,55 (0,46) | 0,38 +- 1,25 (0,71) | -0,87 +- 0,34 (0,66) |
| W05 | 2,64 +- 2,31 (0,37) | -0,44 +- 0,73 (0,29) | 1,59 +- 1,52 (0,74) | -0,26 +- 0,56 (0,46) | 1,10 +- 1,27 (0,69) | 0,01 +- 0,34 (0,69) |
| W05 - W1 | 0,55 +- 0,36 (0,10) | 0,73 +- 0,04 (0,44) | 0,75 +- 0,16 (0,04) | 0,73 +- 0,03 (0,38) | 0,75 +- 0,13 (0,04) | 0,87 +- 0,03 (0,03) |
| W1 + 4 B | 2,64 +- 0,21 (0,14) | 2,51 +- 0,07 (0,004) | 2,82 +- 0,09 (0,14) | 2,55 +- 0,04 (< 0,001) | 2,76 +- 0,07 (0,17) | 2,06 +- 0,07 (< 0,001) |
| W05 + 4 B | 3,19 +- 0,57 (0,11) | 3,24 +- 0,09 (0,10) | 3,57 +- 0,25 (0,06) | 3,28 +- 0,07 (0,11) | 3,51 +- 0,20 (0,07) | 2,93 +- 0,07 (< 0,001) |

- **W1 und W05 haengen am Modell:** Die Urteilslesart gibt -1,0 bzw. -0,26; mit k^6 oder im kleineren Fenster liegen
  die Werte bei 0,4 bis 1,6, aber mit SE 1,2 bis 1,5. Allein entscheiden die Daten das nicht.
- **Die rauscharmen Kombinationen sind scharf:** W1 + 4 B braucht ein k^6-Glied (dann 2,82 +- 0,09, p = 0,14).
  W05 - W1 liegt in allen Lesarten zwischen 0,55 und 0,87.

### 3.3 Je Zelle: c_eff(k) = (y - a)/(x P) (Saatmittel +- SE; a aus dem jeweiligen gemeinsamen Ausgleich)

| Satz | k eps | Skalar B | W1 | W05 | W05 - W1 | W1 + 4 B | W05 + 4 B |
|---|---|---|---|---|---|---|---|
| E1 | 0,050 | 2 +- 11 | -6 +- 47 | -1 +- 49 | 3,5 +- 3,2 | 3,7 +- 2,2 | 7,4 +- 5,3 |
| E1 | 0,099 | -0,3 +- 2,7 | 4,6 +- 11 | 7 +- 12 | 2,1 +- 0,7 | 3,34 +- 0,52 | 5,5 +- 1,2 |
| E1 | 0,199 | 0,55 +- 0,76 | 0,4 +- 3,1 | 1,3 +- 3,3 | 0,89 +- 0,22 | 2,61 +- 0,15 | 3,51 +- 0,36 |
| E1 | 0,298 | 0,76 +- 0,31 | -0,6 +- 1,3 | 0,3 +- 1,4 | 0,92 +- 0,09 | 2,41 +- 0,06 | 3,34 +- 0,15 |
| E2 | 0,099 | 1,6 +- 2,3 | -4,6 +- 9,4 | -4,7 +- 9,8 | -0,4 +- 0,7 | 2,03 +- 0,43 | 1,7 +- 1,1 |
| E2 | 0,199 | 0,73 +- 0,58 | -0,5 +- 2,4 | 0,2 +- 2,5 | 0,55 +- 0,19 | 2,47 +- 0,12 | 3,04 +- 0,30 |
| E2 | 0,397 | 0,75 +- 0,16 | -0,97 +- 0,64 | -0,15 +- 0,66 | 0,81 +- 0,04 | 2,04 +- 0,03 | 2,85 +- 0,07 |
| E2 | 0,596 | 0,51 +- 0,06 | -0,57 +- 0,26 | 0,47 +- 0,27 | 1,03 +- 0,02 | 1,48 +- 0,01 | 2,51 +- 0,03 |

- Die SE je Zelle enthalten den Versatz je Saat; die Zellen eines Datensatzes schwanken gemeinsam. Der Ausgleich nutzt
  die volle Kovarianz.
- W1 + 4 B steigt zu kleinem k hin an (E1: 2,41 / 2,61 / 3,3 +- 0,5 / 3,7 +- 2,2). Ob es bei k -> 0 den
  Kontinuumswert 5 erreicht, ist mit diesen Daten offen.
- Bild: lauf-69/bild-ck-gegen-k2.png (Skalar, W1, W05 und W05 - W1 gegen (k eps)^2 mit Ausgleichsgerade und Band W1).

### 3.4 Rauschen je Saat

| Datensatz | Groesse | Skalar B | W1 | Verhaeltnis |
|---|---|---|---|---|
| E1 | Rest sigma (je k) | 0,00116 | 0,00470 | 4,1 |
| E1 | Versatz tau (je Saat) | 0,00276 | 0,01143 | 4,1 |
| E2 | Rest sigma | 0,00119 | 0,00483 | 4,1 |
| E2 | Versatz tau | 0,00232 | 0,00954 | 4,1 |

- Q (gepoolt ueber 8 Zellen): W1 4,11, W05 4,28; W1 + 4 B 0,19; W05 - W1 0,28.
- **Lesart [M, E]:** Fuer grosses r ist D_W ~ r eps K x 1, also Gamma_W -> -2 log det'K = -4 Gamma_B + konst. Die
  schweren Moden schwanken mit dem Netz wie -4 Skalare. Das erklaert das Verhaeltnis 4,1 und die Ausloeschung in
  W + 4 B. Das Rauschen des naiven Operators (7-mal) kam vom Band; das des Wilson-Fermions kommt von den schweren
  Anteilen.

## 4. Kontrollen

- **Determinanten-Formel gegen dichte Singulaerwerte (K1, N = 151) [E]:**
  - s = 0 und s = +-0,5 (drei Saaten), r = 1, 1/2 und 2: Abweichung hoechstens 2,3e-13.
  - Bei s = 0 sind genau zwei Singulaerwerte null (<= 2e-15), danach folgt ein Kramers-Paar bei 0,42 bis 0,57. Bei
    s = +-0,5 liegt das angehobene Paar bei 0,0077 bis 0,0098, der Rest ab 0,42.
  - Die Cauchy-Binet-Formel (s = 0) und der Weg ueber LU plus Block-Inversiteration (s != 0) sind damit beide
    bestaetigt.
- **Spektrum nahe null bei s = 0 (K2) [E]:** kleinste Singulaerwerte (ohne die zwei Nullmoden) gegen das Kontinuum
  eines Dirac-Fermions (2 pi abs(m)/L, je Impuls zweifach).

| N | Operator | Singulaerwerte 3 bis 10 | 11 bis 18 | 19 bis 24 | Kontinuum (je achtfach) |
|---|---|---|---|---|---|
| 4 001 | (A), r = 0 | 0,00058 / 0,00123 | 0,0020 bis 0,0045 (Band) | - | 0,0993 / 0,1405 |
| 4 001 | Wilson r = 1 | 0,0974 bis 0,1010 | 0,1393 bis 0,1395 ... | bis 0,1995 | 0,0993 / 0,1405 / 0,1987 |
| 4 001 | Wilson r = 1/2 | 0,0971 bis 0,1005 | 0,1383 bis 0,1385 ... | bis 0,1965 | |
| 16 001 | (A), r = 0 | 0,00007 / 0,00032 | 0,0005 bis 0,0009 | bis 0,0010 | 0,0497 / 0,0702 / 0,0993 |
| 16 001 | Wilson r = 1 | 0,0492 bis 0,0501 | 0,0696 bis 0,0709 | 0,0983 bis 0,0995 | 0,0497 / 0,0702 / 0,0993 |
| 16 001 | Wilson r = 1/2 | 0,0492 bis 0,0500 | 0,0695 bis 0,0707 | 0,0980 bis 0,0991 | |

  - Ohne Wilson-Glied liegen bei N = 16 001 alle 22 berechneten von null verschiedenen Singulaerwerte unter 0,0011
    (Kontinuum: erste Stufe 0,0497). Mit Wilson-Glied reproduzieren die ersten drei Stufen (8, 8 und 6 berechnete
    Werte) das Kontinuum eines einzelnen Dirac-Fermions auf 1 bis 1,5 %. **Das Band ist mit beiden r vollstaendig
    angehoben.**
- **Tor: bestanden [E].**
  - Alle 2 176 Bildnetze (E1 1 024, E2 1 152) und 136 Grundnetze erfuellen die Netzpruefungen aus -GROB (Skalar-LU
    mit U_ii > 0 und perm_r = perm_c, Newton-Residuum <= 1e-12).
  - Grundnetze: Nullvektor-Residuen rechts und links <= 4,8e-17 (Logs, r = 1).
  - Bildnetze: Luecke sigma_2/sigma_3 hoechstens 0,052 (E1) bzw. 0,139 (E2) fuer r = 1 und 0,032 bzw. 0,105 fuer
    r = 1/2 (Schwelle 0,5); hoechstens 14 Iterationen; groesstes sigma_2 0,0030 (E1) bzw. 0,016 (E2, in E2-Einheiten),
    kleinstes sigma_3 0,050 bzw. 0,112.
  - Kanten mit w < 0 (physikalische Laengen auf dem Koordinaten-Delaunay): im Mittel 0,10 % (E1) und 0,39 % (E2), wie
    im Vorgaenger. Die Kotangens-Matrix K im Wilson-Glied ist damit auf den Bildnetzen nicht ueberall positiv; das
    Tor hat das nicht gestoert.
- **W0 (Bitvergleich) [E]:** Skalar auf allen 136 Saaten (4 488 Werte: Gamma(0), Gamma(+-S), D, y) und (A) auf 17
  Saaten (561 Werte) exakt gleich (==) mit INDUZIERT-DIRAC-2D.
- **Skalengleichheit [K1]:** Singulaerwerte in E2 = 2 x E1 bei gleichem k eps (Rauchlauf, Abschnitt 6).
- **Skalar auf diesen Saaten:** 0,888 +- 0,137, im Einklang mit 0,922 +- 0,120 des Vorgaengers (96 + 96 Saaten, davon
  sind diese eine Teilmenge) und 1,075 +- 0,071 aus -GROB.

**Latten (v3):**
- **L1 (kann scheitern):** ja. W1 haette im Band liegen koennen (C3 sagte 60 %), W3 haette gepaart uebereinstimmen
  koennen, das Band haette bleiben koennen (K2). Meine Vorhersagen C3 bis C5 sind gescheitert.
- **L2 (Gegenprobe):** Bitvergleich (W0); Formel gegen dicht (K1); Spektrum gegen Kontinuum (K2); r = 1 gegen 1/2
  gepaart; W + 4 B als rauscharme Kombination; Lesarten, Jackknife, Kontrollvariable mit dem Skalar des Vorgaengers.
- **L3 (Numerik):** Determinanten auf 2,3e-13 gegen dicht; Nullvektor-Residuen <= 4,8e-17; Iteration auf 1e-13 in
  log(sigma_1 sigma_2). Statistisch: SE(c_eff) = 0,14 (Skalar), 0,55 (W1, W05), 0,04 (gepaarte Differenz und W1 + 4 B).
- **L4 (schon bekannt):** Wilson-Fermionen und die gamma5-Hermitezitaet (Wilson 1974; Standardlehrbuch) [L];
  Kaehler-Dirac nur flach gleich Dirac-Kopien [S Catterall u. a. 2018]; (1,0)-Fermionen c = -2 [S Kausch 2000]. Ob
  die konforme Antwort von Wilson-Fermionen auf neu vernetzten Zufallsnetzen schon gerechnet ist, weiss ich nicht.
- **L5 (Messbezug):** keiner (2D, euklidisch, synthetisch).

## 5. Schreibtisch W4 (PLAN Abschnitt 1, vor jeder Rechnung)

- **Frage:** Gilt abs det'(d + delta) = det'Delta_0 det'Delta_2 mit Delta_2 isospektral zu Delta_0, und folgt c_KD = -4
  in der Normierung der Karte (Skalar +1, Dirac +1, Gamma_F = -log abs det')?
- **Herleitung [M]:**
  - (d + delta)^2 = Delta_0 + Delta_1 + Delta_2. Die Hodge-Zerlegung gibt fuer jede Metrik
    log det'Delta_1 = log det'Delta_0 + log det'Delta_2 (exakte und koexakte Formen).
  - Also abs det'(d + delta) = det'Delta_0 det'Delta_2.
  - In 2D ist der Hodge-Stern eine Isometrie Omega^0 -> Omega^2 mit Delta_2 * = * Delta_0; konform explizit
    Delta_2 = e^(2 sigma) Delta_0 e^(-2 sigma). Also det'Delta_2 = det'Delta_0 fuer jede Metrik.
  - Gamma_KD = -2 log det'Delta_0 = -4 Gamma_B, also c_KD = -4. Der Flaechenfaktor der Nullmode wirkt nur auf a.
- **Warum die Waermeleitungssumme +2 kein Gegenargument ist [M]:** a_1(Delta_0) + a_1(Delta_1) + a_1(Delta_2) =
  (1 - 4 + 1) R/(24 pi) gaebe "2 Dirac-Fermionen". Die Anomalieformel gilt aber nur fuer Operatoren, die unter
  Weyl-Skalierung kovariant sind (delta A = -2 delta sigma A). Delta_1 ist das in 2D nicht; die exakte Zerlegung
  ersetzt die Formel (Delta_1 wirkt wie 2 Delta_0).
- **Literatur (3 Abrufe, 11:40:06 bis 11:40:11 CEST; Kopien und sha256 in quellen/):**
  - [S] Catterall, Laiho, Unmuth-Yockey, arXiv:1810.10626: Kaehler-Dirac ist "equivalent to four copies of Dirac
    fermions, but they differ in the presence of curvature" (4D-Text, Z. 128 bis 130 der Textfassung).
  - [S] Kausch, hep-th/0003029: konjugierte Fermionfelder der Gewichte 1 und 0 haben "central charge c = −2"
    (Z. 145 bis 152).
  - Zusammen [M + S]: Z_KD = (det'Delta_0)^2 entspricht zwei solchen (1,0)-Systemen, also c = -4 (topologisch
    verdrehte Fermionen).
  - Ginsparg (hep-th/9108028) war fuer die bc-Formel abgerufen; in der Textfassung nicht gefunden, nicht verwendet.
  - Eine Quelle, die c = -4 fuer das 2D-Kaehler-Dirac-Feld woertlich nennt, habe ich nicht.
- **Gegen den Vorgaenger und die Leitung:** gleiche Herleitung wie [K1] in INDUZIERT-DIRAC-2D; ich finde keinen Fehler.
  Die Erwartung der Leitung (75 %) bestaetigt sich.
- **Urteil W4: eingetroffen** (Plan und Kartenwortlaut), vor jeder Rechnung festgehalten. Damit gilt der vorab
  festgelegte Zweig "W4 haelt": Kaehler-Dirac ist als schwerkrafttaugliche Fermion-Bauart in 2D ausgeschlossen
  (falsches Vorzeichen schon im Kontinuum, c = -4 statt +2). Ein Gitterbeleg fuer -4 fehlt weiterhin.

## 6. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Einheit von r:** D_W = D_A + r eps K mit eps = sqrt(A/N). Fuer E1 ist das woertlich die Karte; fuer E2 haelt
  es die Skalengleichheit (E2 = skaliertes E1 bei gleichem r). Bestaetigt: Die Singulaerwerte in E2 sind das Doppelte
  der E1-Werte bei gleichem k eps (z. B. 7,87e-4 gegen 3,94e-4).
- **[K2] Normierung:** Karten-r = 1/2 entspricht auf dem Quadratnetz dem ueblichen Wilson-Parameter 1. Gerade dieser
  Wert liegt naeher an 1 als r = 1 (Abschnitt 3.1).
- **[K3] Saaten:** dieselben Saaten wie INDUZIERT-DIRAC-2D, aber nur 64 + 72 der dortigen 96 + 96 (Uhrregel 12:55).
- **[K4] (A)** nur auf der ersten Saat jedes Blocks (17 Saaten); W0 ist fuer (A) ein Teilvergleich.
- **[K5] W2:** "Streuung je Saat" wie die "Saatstreuung" des Vorgaengers, gepoolt ueber 8 Zellen. Jede Lesart gibt
  dasselbe: Q je Zelle 4,09 bis 4,13, SE-Verhaeltnis 4,0.
- **[K6] W3:** im Plan die SE der gepaarten Differenz; ungepaart (Kartenwortlaut) waere W3 eingetroffen. Hier
  unterscheiden sich Plan und Kartenwortlaut im Urteil.
- **[K7] r bei W2:** r = 1 geurteilt; r = 1/2 gibt dasselbe (Q = 4,28).

## 7. Selbstanzeigen

1. **Vor dem Einfrieren gesehen (Rauchsaaten >= 902, keine Hauptlauf-Saat):**
   - K1, K2 bei N = 4 001 und 16 001 (Band angehoben), Logzeilen mit Singulaerwerten, Iterationen und Zeiten.
   - **Rauschen** aus der Probe der Auswertung (6 + 5 Rauchsaaten): Q(W1) = 4,04, Q(W05) = 4,11; Rest und Versatz je
     etwa viermal so gross wie beim Skalar; W1 + 4 B streut 0,10-mal, W05 - W1 0,18-mal so stark wie der Skalar.
     Damit war vor dem Einfrieren absehbar, dass W2 nach meiner Regel wahrscheinlich verfehlt und W1 an der
     SE-Schwelle 0,3 scheitert. Die Regeln W0 bis W3 standen vorher fest (Plantext ab 11:49:26, erste Probe 11:53:44)
     und sind unveraendert; die Karte ohnehin.
   - c_eff-Werte habe ich vor dem Einfrieren nicht angesehen, auch nicht das Probe-Bild.
2. **Code vor dem Einfrieren geaendert:**
   - wilson2d.py: einmal vor dem ersten Start (Rueckgabe der Singulaerwerte in K2 als Paare); seitdem unveraendert.
   - wilson_auswertung.py: W0-Logik berichtigt (eine fehlende Vergleichszeile gibt "nicht auswertbar", wie im Plan),
     vor der ersten Probe. **Nach dem Blick auf das Rauschen** (erste Probe) kamen in zwei Schritten beschreibende
     Groessen dazu: Ausgleich fuer W + 4 B, Streuung von W1 + 4 B und W05 - W1, Kontrollvariable. Sie aendern kein
     Urteil. Der eingefrorene Plan sagt in der Kopfzeile von Abschnitt 11 ungenau "einmal vor der Probe berichtigt";
     vollstaendig steht es dort unter "Codeaenderungen vor dem Einfrieren".
3. **Nach dem Einfrieren (11:57:13):** Plan und Code unveraendert (sha256 lokal und auf der .69 vor dem Start und vor
   der Auswertung geprueft). Waehrend der Laeufe habe ich nur Logzeilen (Singulaerwerte, Iterationen, Zeiten, rc)
   angesehen, keine y-Werte. Die Uhrregel hat entschieden: kein Start nach 12:55:00 (e1-s64 und e2-s1072 nicht
   gestartet, 12:57:40 bzw. 12:59:21).
4. **Abweichungen vom Brief:**
   - (A) nur auf der ersten Saat jedes Blocks (Zeit); W0 fuer (A) damit ein Teilvergleich.
   - Nur 64 + 72 der 96 + 96 Saaten des Vorgaengers (Uhrregel, Zeitbox).
   - Faktor eps im Wilson-Glied (Kartenpunkt K1).
5. **Spuren und Starts:** nur cpu und cpu7; 27 Starts, alle rc = 0.
   - Rauch und Proben: 9 Starts (hoechstens drei ssh-Verbindungen zugleich).
   - Hauptphase: 17 Bloecke und die Auswertung; je Spur eine lokale Schleife mit einem ssh-Aufruf je Block, also
     hoechstens zwei ssh-Verbindungen zugleich. Blockdauer E1 7:17 bis 7:59 min, E2 6:36 bis 7:12 min (Grenze 10 min).
6. **Auf der .69 ausserhalb des Starters:** mkdir, cp (Probe-Ordner aus Rauchdateien und Kopien von Rauchdateien und
   auswertung.json des Vorgaengers, nur gelesen), mv, ls, sha256sum, jq, cat (Starter gelesen), systemctl --user
   list-units (nur lesend), uptime, date. Kein Python ausserhalb des Starters.
7. **Lokal:** kein python, awk oder perl. Benutzt: jq, sed, grep, sha256sum, date, ssh, scp, cp, mv, mkdir, curl,
   pdftotext. Ausserhalb der Liste: ls, cat, head, tail, cut, wc, diff, sleep (in Warteschleifen), rm (zwei eigene
   Dateien: die unnoetige Kopie code/induziert.py und eine Hilfskopie von wilson_auswertung.py).
8. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
   unter /tmp/claude-1000/.../tasks/ an; meine Ausgaben gingen per Umleitung in den Kartenordner.
9. **Abrufe:** genau drei (erlaubt drei), keine Websuche.

## 8. Bedeutung

- **Vorab festgelegte Zweige:** "W1 und W2 treffen ein" nicht ausgeloest. "W1 verfehlt mit c_eff > 1,3" auch nicht:
  W1 ist nach unten verfehlt (-1,0). Ausgeloest ist nur "W4 haelt".
- **Was gilt [E]:**
  - Das Standardmittel wirkt auf das Spektrum: Mit Wilson-Glied hat das Fermion auf dem Zufallsnetz mit
    "Zahl = Volumen" genau das Spektrum eines einzelnen Dirac-Fermions (22 tiefste Werte auf 1 bis 1,5 %).
  - Die Schwerkraft-Antwort im gemessenen Fenster ist dennoch nicht die eines Dirac-Fermions und haengt deutlich von r
    ab (-1,0 bei r = 1, -0,26 bei r = 1/2; Unterschied 0,72 +- 0,04).
  - Das Rauschen ist kleiner als beim naiven Operator (4-mal statt 7-mal der Skalar), aber nicht klein. Es stammt aus
    den schweren Anteilen und faellt in W + 4 B fast ganz heraus.
- **Lesart [H]:** Das Wilson-Fermion wird oberhalb von k ~ 1/(r eps) "Laplace-artig" (Grenzfall r -> unendlich:
  c = -4). Im Fenster k eps = 0,05 bis 0,6 ist dieser Uebergang offenbar noch nicht abgeklungen: c_eff(k) von
  W1 + 4 B steigt zu kleinem k hin an, und kleineres r liegt naeher an 1. Fuer r -> 0 laesst sich aus zwei r-Werten
  nicht sauber extrapolieren (linear in r gaebe etwa 0,5 +- 0,6). Meine Begruendung zu C6 (Doppler-Glied ~ 1/r^2) passt
  dazu nicht; der Befund spricht eher fuer Gitterartefakte, die mit r wachsen.
- **Was sich aendert:**
  - Die Karte erwartete, dass das Anheben des Bandes die Antwort repariert. Das Band ist weg, die Antwort nicht
    repariert. Das Problem des Vorgaengers war also nicht nur das Band.
  - Kaehler-Dirac bleibt ausgeschlossen (W4, Kontinuum c = -4).
- **Naechste Schritte [H]:**
  - (a) Kleinere r (1/4, 1/8) mit derselben Messung: Wandert c_eff gegen 1, und wie (linear oder quadratisch in r)?
  - (b) Kleinere k eps durch groesseres N (64 001), mit W + 4 B als rauscharmer Groesse.
  - (c) Rauscharm messen: c_eff(W) = c_eff(W + 4 B) - 4 c_eff(B). Der Skalar allein ist viel billiger als das
    Fermion (LU 0,12 s je Netz im Vorgaenger; Netzbau nicht getrennt gemessen), seine Saatzahl laesst sich
    vervielfachen. Fuer SE(c_eff(W)) = 0,3 braucht es SE(B) <= 0,075, also etwa 500 Skalar-Saaten.
- **Rahmen:** 2D, euklidisch, gequenchtes Netzmittel, nur die konforme Mode, S = 0,5, Modell k^0 + k^2 + k^4.

## 9. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-115713, EINGEFROREN-SHA256.txt,
  AGENT-VORHERSAGEN-ENTWURF.txt (C1 bis C7, 11:47:21)
- quellen/: drei abgerufene PDFs mit Textfassung (pdftotext) und QUELLEN-SHA256.txt
- code/:
  - wilson2d.py: Wilson-Operator, Gamma_W, Modi dichte und kontrolle
  - wilson_auswertung.py: Tor, Bitvergleich W0, Urteile W0 bis W4, Ausgleich, Bild
  - dirac2d.py, dirac_auswertung.py, dichte2d_grob.py, zufall2d.py, grob_auswertung.py unveraendert aus
    INDUZIERT-DIRAC-2D
  - je mit Kopien *.eingefroren-20261004-115713
- rauch-69/: kontrolle (K1, K2 bei N = 4 001), kontrolle-k2-16001, Rauchsaaten dichte-r902-e1, -r902-e2, -r904-e1,
  -r905-e2 (JSON und Logs), Probe der Auswertung (Logs, probe/auswertung-probe*.json)
- lauf-69/:
  - e1-s0 bis e1-s56.json: E1 (N = 16 001, eps = 1), Saaten 0 bis 63
  - e2-s1000 bis e2-s1064.json: E2 (N = 16 001, A = 64 004, eps = 2), Saaten 1000 bis 1071
  - je mit .log; schleife-cpu.log, schleife-cpu7.log (Start- und Endzeiten der Bloecke)
  - auswertung.json (Urteile), auswertung.log, PRUEFSUMMEN.txt (.69), bild-ck-gegen-k2.png
- Auf der .69: /home/fmh/fmhc-physics-remote/runde40-induziert-wilson/ (code/, rauch/, lauf/). Der Ordner
  runde39-induziert-dirac/ wurde nur gelesen.

## 10. Einfach gesagt

Das naive Fermion hatte auf dem Zufallsnetz einen Haufen falscher Zustaende fast ohne Energie. Ein Zusatzglied (Wilson)
raeumt sie vollstaendig weg: Danach sieht das Spektrum genau so aus wie das eines einzigen echten Teilchens mit halbem
Spin. Die Schwerkraft-Antwort kommt trotzdem nicht richtig heraus: Statt 1 messen wir -1,0 bzw. -0,3, je nachdem, wie
stark das Zusatzglied eingestellt ist. Weil die richtige Zahl von dieser Einstellung nicht abhaengen darf, sind unsere
Wellen offenbar noch nicht lang genug, oder das Netz verfaelscht die Antwort auf eine Weise, die von der Einstellung
abhaengt. Die Nachpruefung am Schreibtisch bestaetigt ausserdem, dass die Bauart Kaehler-Dirac im gekruemmten Raum das
falsche Vorzeichen hat und damit ausscheidet.
