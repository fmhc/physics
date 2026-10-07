# INDUZIERT-DIRAC-2D: Ergebnis (Runde 39, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 09:48:32 CEST, Code ab 10:05:55, Plantext ab 10:20:30 CEST.
  - Rauchlaeufe und Proben 08:09:36 bis 08:23:09 UTC (PLAN Abschnitt 11).
  - Eingefroren 10:23:58 CEST: PLAN.md.eingefroren-20261004-102358, Code-Kopien *.eingefroren-20261004-102358,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 08:24:06 bis 09:22:31 UTC (regulaer L = 127 und 16 Bloecke, alle rc = 0), Auswertung 09:22:39 bis
    09:22:47 UTC (rc = 0).
  - Text ab 11:26:01 CEST.
- Plan und Code sind nach dem Einfrieren unveraendert. Die sha256 stimmen lokal und auf der .69.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64; Spuren cpu und cpu7). Gerechnet
  ist euklidisch, eine Schleife, freie masselose Felder auf festem Hintergrund. Synthetisch, keine Messdaten.
- **Kennzeichen:** [E] hier gerechnet, [M] eigene Mathematik, [F] Festlegung im Plan, [K] Kartenpunkt, [H] Hypothese,
  [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen (hier keine Quelle abgerufen).
- **Bezeichnungen:** P = -1/(24 pi); c_eff = (Gamma''/(k^2 A))/P mit Gamma_F = -log|det' D| fuer Fermionen
  (Grassmann-Vorzeichen) und Gamma_B = +1/2 log det' K fuer den Skalar. Ein Dirac-Fermion im Kontinuum gibt +1, der
  Skalar +1, vier naive Doppler +4. E1/E2: Netzabstand eps = 1 bzw. 2 (N = 16 001), x = (k eps)^2.

## 1. Ergebnis zuerst

1. **Skalar auf denselben Zufallsnetzen [E]:** c_eff(B) = **0,92 +- 0,12** (96 + 96 Saaten, neue Netze mit
   N = 16 001). Das bestaetigt -GROB (1,075 +- 0,071) unabhaengig.
2. **(A) naiver Dirac-Operator auf dem Zufallsnetz [E]:** c_eff(A) = **1,7 +- 1,1**. Das Rauschen ist je Saat siebenmal
   so gross wie beim Skalar.
   - Damit ist weder "ein Fermion" (1) noch "vier Doppler" (4) entschieden; ID-F1 ist nicht auswertbar.
   - Lesarten mit besser passendem Modell (k^6-Glied, Fenster k eps <= 0,4) geben 6 bis 7 +- 2. Das ist ein Hinweis
     auf einen Ueberschuss ueber 1 [H], kein Befund.
   - Im Spektrum verschwinden die Doppler nicht spurlos: Sie werden zu einem dichten Band bei E = 0 [E].
3. **(B) Kaehler-Dirac [E]:** c_eff(KD) = **+48 +- 2,4**, weit weg von der Karte (+2) und von meiner berichtigten
   Kontinuumserwartung (-4 [M]).
   - Fast alles kommt aus dem dualen Teil Delta_2 (+50 +- 2,3). Der primaere Teil gibt -1,5 +- 0,3, nahe -2.
   - Ursache [E, H]: Delta_2 hat Leitwerte 1/w_e. Das Koordinaten-Delaunay hat etwa 1 400 (k eps)^2 Kanten je Netz
     mit w_e < 0 in der physikalischen Metrik, und jede verschiebt Gamma_KD um etwa -0,4 bis -1,1. Ihre Zahl
     waechst wie k^2. Das ist ein nicht-kovariantes Netzartefakt; der Skalar spuert es kaum, weil w dort linear
     eingeht.
4. **Regelmaessiges festes Netz [E]:** (A) gibt c0_eff = **+39,2** statt 4, der Skalar -9,42 (= (1/8)/P, wie bekannt).
   Das feste Netz zaehlt keine Doppler, sondern liefert einen nicht-universellen Wert; er ist etwa das -4-Fache des
   Skalars.
5. **Urteile:** ID-F0 nicht eingetroffen (wegen des regelmaessigen Netzes; Teil Skalar eingetroffen), ID-F1 nicht
   auswertbar, ID-F2 nicht eingetroffen, ID-F3 nicht auswertbar. Keiner der vorab festgelegten Bedeutungszweige ist
   ausgeloest.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 7 durch code/dirac_auswertung.py; Werte in lauf-69/auswertung.json (unbearbeitet).
Vorbedingungen: Tor Netz, A und KD bestanden; 96 Saaten je Datensatz; Modellprobe p >= 0,01 fuer B (0,47), A (0,053)
und KD (0,61).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| ID-F0 | Kontrolle: Regelmaessiges Netz mit (A) gibt c_eff = 4 +- 1 (Doppler); Skalar auf den Zufallsnetzen c_eff = 1 +- 0,2 | 75 % | **nicht eingetroffen** | nicht eingetroffen | regelmaessig L = 127: c0_eff(A) = +39,19 (Band 3 bis 5): nicht eingetroffen. Skalar: 0,922 +- 0,120 (Band 0,8 bis 1,2, SE <= 0,2): eingetroffen |
| ID-F1 | [H] Zufallsnetz mit (A): c_eff = 1 +- 0,4, also keine Doppler in der Anomalie | 35 % | **nicht auswertbar** | nicht eingetroffen | c_eff(A) = 1,69 +- 1,15 (Birge 1,48); Abstand zum Band 0,29 = 0,25 SE; SE > 0,4 |
| ID-F2 | Zufallsnetz mit (B) Kaehler-Dirac: c_eff = 2 +- 0,5 | 55 % | **nicht eingetroffen** | nicht eingetroffen | c_eff(KD) = +48,4 +- 2,4; Abstand 45,9 = 18,8 SE. Berichtigt [K1] -4 +- 1: ebenfalls nicht eingetroffen (21 SE) |
| ID-F3 | [H] Vorzeichen wie beim Skalar (Polyakov-Vorzeichen) fuer beide Bauweisen | 60 % | **nicht auswertbar** | eingetroffen | (A): 1,69 +- 1,15, Vorzeichen innerhalb 2 SE offen. KD: +48,4 +- 2,4, positiv |

- **Lesart ID-F0:** Teil (i) verfehlt aus dem vorab offengelegten Grund [K2]: Das feste Netz ist kein kovarianter
  Regulator. Der Skalar-Teil ist eingetroffen.
- **Lesart ID-F3:** Nach Kartenwortlaut eingetroffen. Das positive KD-Vorzeichen kommt aber vermutlich vom
  Netzartefakt (Abschnitt 3.4 [H]), nicht von einer Anomalie. Fuer (A) ist das Vorzeichen offen.

**Agenten-Vorhersagen** (PLAN Abschnitt 10, notiert 10:18:20 CEST)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| C1 (90 %) | Tor besteht | **eingetroffen**: 3 072 Bildnetze und 192 Grundnetze ohne Fehler |
| C2 (75 %) | Skalar: Punktwert in [0,8; 1,2] | **eingetroffen**: 0,922 |
| C3 (55 %) | KD in [-5; -3] | **nicht eingetroffen**: +48,4 |
| C4 (85 %) | KD0 = -2 c_eff(B) innerhalb 2 SE | **nicht eingetroffen**: KD0 = -1,47 gegen -1,84; die Differenz ist das lokale Glied Summe log m mit 0,41 +- 0,15 (2,7 SE) |
| C5 (60 %) | (A) ausserhalb [0,6; 1,4] | Punktwert 1,69 ausserhalb, aber nur 0,25 SE neben dem Band: nicht entschieden |
| C6 (70 %) | regelmaessig (A) ausserhalb [3; 5] | **eingetroffen**: +39,2 (aus dem Rauchlauf L = 63 schon vor dem Einfrieren bekannt, aber vorher notiert) |
| C7 (80 %) | regelmaessig Skalar innerhalb 10 % von -9,42 | **eingetroffen**: -9,424 |

## 3. Tabellen [E]

### 3.1 Gemeinsamer Ausgleich je Operator (E1 + E2, je 96 Saaten; c_eff und d_eff in Einheiten von P)

| Operator | c_eff(0) | SE (GLS mit Birge) | Jackknife-SE | d_eff | p (5 FG) |
|---|---|---|---|---|---|
| Skalar B | **+0,922** | 0,120 | 0,121 | -1,10 +- 0,32 | 0,47 |
| (A) naiv | **+1,69** | 1,15 (GLS 0,78, Birge 1,48) | 0,83 | +3,2 +- 3,1 | 0,053 |
| (B) KD | **+48,4** | 2,44 | 2,50 | -69,7 +- 6,4 | 0,61 |
| KD0 (primaer, -log det'Delta_0) | -1,47 | 0,27 | 0,27 | +6,1 +- 0,7 | 0,88 |
| KD2 (dual, -log det'Delta_2) | +49,9 | 2,30 | 2,38 | -75,9 +- 6,0 | 0,57 |
| A mit Massenmatrix (Gamma_A + 2 Summe log m) | +2,41 | 0,94 | 0,85 | +11,1 +- 2,5 | 0,25 |
| A - B (je Saat gepaart) | +0,78 | 1,21 | 0,89 | +4,3 +- 3,2 | 0,065 |
| KD + 4 B (gepaart; Kontinuum [M]: 0) | +52,2 | 2,19 | 2,26 | -74,2 +- 5,8 | 0,66 |
| lokal Summe log m_i | +0,41 | 0,15 | 0,15 | +3,8 +- 0,4 | 0,39 |
| lokal Summe log A_T | +0,10 | 0,61 | 0,64 | +2,8 +- 1,6 | 0,91 |

- **Lesarten (beschreibend, c_eff +- SE, p):**

| Operator | nur E1 | nur E2 | mit k^6 | a je Datensatz | Fenster k eps <= 0,4 | nur k^2, Fenster 0,4 |
|---|---|---|---|---|---|---|
| Skalar B | -0,10 +- 0,54 (0,56) | 0,95 +- 0,15 (0,62) | 0,56 +- 0,33 (0,52) | 0,92 +- 0,13 (0,34) | 0,68 +- 0,28 (0,46) | 0,76 +- 0,07 (0,59) |
| (A) naiv | 9,2 +- 3,8 (0,45) | 0,87 +- 2,3 (0,018) | 7,4 +- 2,1 (0,60) | 1,69 +- 1,28 (0,027) | 5,9 +- 1,75 (0,47) | 2,0 +- 0,66 (0,10) |
| (B) KD | 64 +- 13 (0,37) | 47,2 +- 3,2 (0,57) | 56 +- 7 (0,71) | 48,4 +- 2,4 (0,59) | 54 +- 5,5 (0,67) | 37,7 +- 2,4 (0,038) |

- **(A) haengt am Modell:**
  - Das Urteilsmodell (k^0, k^2, k^4) passt nur knapp (p = 0,053, Birge 1,48).
  - Mit k^6 passt es gut (p = 0,60) und gibt 7,4 +- 2,1; im Fenster bis 0,4 sind es 5,9 +- 1,75. Beide liegen etwa
    3 SE ueber 1 und innerhalb 2 SE von 4.
  - Das spricht eher fuer einen Ueberschuss als fuer ein einzelnes Fermion [H]. Entschieden ist es nach Plan nicht.
- **Skalar:** Alle Lesarten liegen zwischen 0,56 und 0,95 (nur E1 allein ist zu unscharf). Das passt zu -GROB, wo das
  k^6-Glied den Wert ebenfalls nach unten zog (0,91 P).
- **KD:** Alle Lesarten liegen zwischen 38 und 64. Der Wert ist kein Rauschen.

### 3.2 Je Zelle: c_eff(k) = (y - a)/(x P) (Saatmittel +- SE)

| Satz | k eps | Skalar B | (A) naiv | KD | KD2 | mittl. Kanten mit w < 0 je Netz |
|---|---|---|---|---|---|---|
| E1 | 0,050 | 5 +- 9 | -39 +- 69 | 53 +- 220 | 59 +- 208 | 3,5 |
| E1 | 0,099 | 0,6 +- 2,2 | -11 +- 17 | 88 +- 52 | 89 +- 49 | 14 |
| E1 | 0,199 | 0,59 +- 0,61 | 3,1 +- 4,0 | 56 +- 14 | 57 +- 13 | 55 |
| E1 | 0,298 | 0,88 +- 0,26 | 1,5 +- 1,8 | 45,5 +- 5,7 | 46,7 +- 5,4 | 123 |
| E2 | 0,099 | 0,78 +- 2,0 | 3,6 +- 17 | 15 +- 52 | 16 +- 49 | 14 |
| E2 | 0,199 | 0,71 +- 0,53 | 6,5 +- 4,4 | 41 +- 14 | 42 +- 13 | 55 |
| E2 | 0,397 | 0,74 +- 0,14 | 2,2 +- 1,0 | 35 +- 3,3 | 35 +- 3,2 | 216 |
| E2 | 0,596 | 0,52 +- 0,06 | 3,04 +- 0,46 | 23 +- 1,4 | 22 +- 1,3 | 468 |

- Die SE je Zelle enthalten den Versatz je Saat (Gamma(0) ist fuer alle k einer Saat gleich); die Zellen eines
  Datensatzes schwanken gemeinsam. Der Ausgleich nutzt die volle Kovarianz.
- Saatstreuung von y_eps je Saat: Skalar 0,0026 bis 0,0031, (A) 0,021 bis 0,022, KD 0,064 bis 0,071. Der Versatz je
  Saat macht bei allen etwa 80 % der Varianz aus.
- Bild: lauf-69/bild-ck-gegen-k2.png (je Bauweise c_eff(k) gegen (k eps)^2 mit Ausgleichsgerade und Linien
  c = 1, 2, 4; bei KD auch -2 und -4; viertes Feld: regelmaessiges Netz). Die Legende nennt "N = 16 000";
  gerechnet ist N = 16 001.

### 3.3 Regelmaessiges festes Netz (Richardson, h = 0,01; Mittel ueber 0 und 90 Grad, beide gleich)

| L | n | k^2 | c_eff (A) | c_eff Skalar | (A) + 4 Skalar |
|---|---|---|---|---|---|
| 127 | 1 | 0,00245 | +39,601 | -9,420 | +1,92 |
| 127 | 2 | 0,00979 | +38,154 | -9,408 | +0,52 |
| 127 | 4 | 0,0392 | +37,733 | -9,360 | +0,29 |
| 127 | k -> 0 (c0 + b k^2) | 0 | **+39,19** | **-9,424** | - |
| 63 (Rauch) | 1 / 2 / 4 | - | +39,58 / +38,08 / +37,47 | -9,406 / -9,357 / -9,168 | - |

- S-Schema (S = 0,5) gibt c0_eff(A) = +39,17, also dasselbe. Der Skalar trifft (1/8)/P = -9,425.
- Die Werte haengen vor allem von n ab, nicht von k allein (bei gleichem k verschieden, bei gleichem n fast gleich).
  Das ist vermutlich ein Endlichkeitseffekt der Doppler mit verdrehten Raendern (L ungerade) [H].
- Auf dem festen Netz gilt also ungefaehr Gamma_A ~ -4 Gamma_B: Die vier Doppler tragen je den negativen
  Fest-Netz-Wert des Skalars. Das ist kein Anomalie-Zaehler.

### 3.4 Woher der KD-Wert kommt (beschreibend, nach der Auswertung per jq aus den Laufdateien)

- Je Zelle wurden die mittlere Zahl der Kanten mit w_e < 0 (physikalische Laengen auf dem Koordinaten-Delaunay) und das
  Mittel von y(KD2) bestimmt (Tabelle 3.2, letzte Spalte).
- Die Zahl waechst wie (k eps)^2: etwa 1 400 x je Netz (1 417 / 1 418 / 1 393 / 1 379 in E1, 1 408 bis 1 318 in E2).
- y(KD2) - a faellt dazu ungefaehr proportional: etwa -2e-4 bis -5e-4 je Kante in y_eps, also -0,4 bis -1,1 in
  Gamma_KD2 je Kante mit w_e < 0 im Mittel ueber +S und -S (je Kante etwas weniger bei grossem k eps).
- **Lesart [H]:** Delta_2 hat Leitwerte 1/w_e und ist bei w_e = 0 singulaer. Kanten, die im Koordinaten-Delaunay
  liegen, in der physikalischen Metrik aber nicht Delaunay sind, verschieben log det'Delta_2 je um O(1). Ihre Zahl ist
  proportional zu k^2 A und erscheint deshalb als riesiges k^2-Glied.
- Beim Skalar gehen die w_e linear ein; derselbe Netzfehler wirkt dort kaum (intr gegen koord in INDUZIERT-DICHTE-2D:
  <= 3e-5 in y).
- Auch das lokale Glied Summe log m_i (m_i enthaelt w_e) zeigt mit 0,41 +- 0,15 eine kleine k^2-Antwort, die ein
  kovariantes Ensemble nicht haette.
- Geprueft ist die Lesart nicht: Ein Lauf mit intrinsischem Delaunay oder positiven Hodge-Sternen fehlt.

## 4. Kontrollen

- **Tor: bestanden [E].**
  - Alle 3 072 Bildnetze (E1 und E2 je 1 536) und 192 Grundnetze erfuellen die Netzpruefungen aus -GROB; jede
    Skalar-LU hatte U_ii > 0 und perm_r = perm_c; Newton-Residuum <= 1,8e-15.
  - (A): Nullvektor-Residuum <= 1,1e-13 (relativ), Gram-Matrix komplex strukturiert auf 2,6e-11 (relativ).
  - (B): alle m_i > 0 (kleinstes 0,0025), kleinstes abs(w_e) 1,2e-8 (Schwelle 1e-12); der groesste Leitwert 1/w_e in
    Delta_2 ist also etwa 1e8.
  - Kanten mit w_e < 0: im Mittel 0,10 % (E1) bzw. 0,39 % (E2), hoechstens 0,32 % bzw. 1,09 %. Neue Kanten gegenueber
    dem Grundnetz: 19 %.
  - Regelmaessiges Netz L = 127: Euler, Kanten, Delaunay in Ordnung; Nullvektor-Residuum <= 9e-14.
- **Determinanten-Formeln gegen dichte Eigenwerte (Kontrolle K1, N = 151, s = 0 und +-0,5) [E]:**
  - (A): log|det' D| ueber den geschuetzten Nullvektor gegen das Produkt der dichten Eigenwerte ohne die zwei
    Nullmoden: <= 6e-13 absolut.
  - (B): det'Delta_0 det'Delta_2 gegen die dichten Eigenwerte von d + delta (6N x 6N) ohne die vier harmonischen
    Formen: <= 1,1e-11. (d + delta)^2 ist blockdiagonal auf 1e-13, d1 d0 = 0 exakt.
- **Paritaet [M, E]:** Bei geradem N hat (A) bei s = 0 vier exakte Nullmoden (N = 150, 152), bei ungeradem N zwei
  (N = 151, 153). Bei ungeradem N bleiben die zwei Nullmoden auch bei s = +-0,5 exakt null (1e-16).
  - Grund: Mit zeta = a + i b ist D antilinear mit der komplex antisymmetrischen Matrix G_ij = w_ij d_ij. Bei geradem
    N erzwingt die Antisymmetrie einen zweiten Nullvektor; bei ungeradem N ist der eine geschuetzt.
  - Auf dem Quadratnetz: L = 8 hat 8 Nullmoden (4 Doppler x 2), L = 9 nur 2 (die Doppler sehen verdrehte Raender).
- **Doppler im Spektrum (Kontrolle K2, K3) [E]:**
  - Quadratnetz: Spektrum von (A) = sqrt(sin^2 p_x + sin^2 p_y) auf 1e-14, also genau die 4 Kegel des naiven
    Gitterfermions.
  - Zufallsnetz (N = 4 001 und 16 001, s = 0): Neben den zwei Nullmoden liegen die 38 naechsten Eigenwerte von (A)
    alle unter 0,0082 bzw. 0,0018. Die erste Kontinuumsstufe eines Dirac-Fermions liegt bei 2 pi/L = 0,099 bzw.
    0,050 (Verhaeltnis hoechstens 0,025 bzw. 0,010).
  - Statt einzelner Doppler-Kegel gibt es also ein dichtes Band bei E = 0 (Kramers-Quartette). Die Zustandsdichte
    dort ist etwa 1,2 bis 1,4 je Flaeche und Energie, unabhaengig von N; das Kontinuum haette E/pi, also nahe 0.
- **Regelmaessiges Netz, Glaette in s:** Richardson h gegen 2h <= 3e-7; S-Schema (S = 0,5) gleich Richardson auf
  0,1 %. L = 63 und L = 127 geben bei gleichem n fast dieselben Werte: (A) auf 0,1 bis 0,7 %, Skalar auf 0,1 bis 2 %
  (Tabelle 3.3).
- **Selbsttest (synthetisch, vor dem Einfrieren):** 64 + 64 Saaten, wahres c = P: Mittel -0,013270, Zug-Std 1,08 bis
  1,10. Die GLS-SE ist bei dieser Saatzahl etwa 10 % zu klein; das Jackknife steht deshalb in Tabelle 3.1.

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - Der Skalar haette auf den neuen Netzen danebenliegen koennen.
  - (A) haette klar bei 1 oder klar bei 4 liegen koennen; es blieb unentschieden.
  - KD hat beide vorab genannten Werte (+2 der Karte, -4 meiner Berichtigung) deutlich verfehlt.
  - Meine Vorhersagen C3 und C4 sind gescheitert.
- **L2 (Gegenprobe):**
  - beide Determinanten-Formeln gegen dichte Eigenwerte; Paritaetsprobe
  - Skalar auf denselben Netzen (Kalibrierung des Zaehlers)
  - KD zerlegt in KD0 und KD2; KD0 gegen -2 Skalar
  - lokale Glieder Summe log m und Summe log A_T
  - je Zelle Zahl der w_e < 0 gegen KD2
  - E1 und E2 einzeln, k^6, Fenster, Jackknife
  - regelmaessig: Richardson gegen S-Schema, L = 63 gegen 127, Spektrum gegen sin-Formel
- **L3 (Numerik):** Determinanten auf 6e-13 (A) bzw. 1,1e-11 (KD) gegen dicht; Nullvektor-Residuum <= 1,1e-13;
  Richardson <= 3e-7. Statistisch: SE(c_eff) = 0,12 (Skalar), 1,15 (A), 2,4 (KD).
- **L4 (schon bekannt):**
  - Polyakov 1981; c = 1 fuer ein Dirac-Fermion; c = -2 fuer symplektische Fermionen bzw. verdrehte N = 2-Fermionen [L].
  - Kaehler-Dirac-Felder sind im gekruemmten Raum keine Dirac-Fermionen ("geometric fermions", Banks/Dothan/Horn
    1982 [L?]); Kaehler-Dirac auf DT: Catterall/Laiho/Unmuth-Yockey 2018 [L?, RUNDE-22].
  - Zufallsgitter-Fermionen: Christ/Friedberg/Lee 1982 [L]; Griffin/Kieu 1992 (Doppler kehren mit Eichfeld zurueck),
    Kieu/Markham/Paranavitane 1994 (Zufall allein reicht nicht), Cohen 2006 [S Abstract, laut SPIN-KAUSAL-L].
  - Zustandsdichte bei E = 0 in chiralen Unordnungsklassen (Gade/Wegner 1991 [L?]).
  - Ob die Paritaetsaussage (G komplex antisymmetrisch) oder die induzierte Anomalie von Fermionen auf neu vernetzten
    Poisson-Delaunay-Netzen schon gerechnet ist, weiss ich nicht [L?].
- **L5 (Messbezug):** keiner (2D, euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Kaehler-Dirac im gekruemmten Raum: c = -4 statt +2 [M].**
  - Exakt gilt |det'(d + delta)| = det'Delta_0 det'Delta_2, auch auf dem Netz (Kontrolle K1 auf 1e-11).
  - Im Kontinuum sind Delta_2 und Delta_0 ueber den Hodge-Stern isospektral. Also Gamma_KD = -2 log det'Delta_0 =
    -4 Gamma_B, und c_eff = -4.
  - Die Gleichung "Kaehler-Dirac = 2 Dirac-Fermionen" gilt nur flach. Formen haben ganzzahligen Spin und koppeln
    anders an die Kruemmung; der Geschmacksindex dreht sich mit.
  - **Was daraus wurde:** Weder +2 noch -4: c_eff(KD) = +48,4 +- 2,4. Der primaere Teil KD0 = -1,47 +- 0,27 liegt nahe
    der Erwartung -2 (Abweichung = lokales Glied Summe log m). Der duale Teil KD2 = +49,9 +- 2,3 ist vom Netzartefakt
    der Leitwerte 1/w_e beherrscht (Abschnitt 3.4).
  - Die Kontinuumsaussage -4 ist damit weder bestaetigt noch widerlegt; auf diesem Netz ist sie nicht messbar. Das
    Kartenurteil (2 +- 0,5) ist eindeutig nicht eingetroffen.
- **[K2] Regelmaessiges Netz:** Ein festes Netz ist kein kovarianter Regulator. Eingetreten wie offengelegt: (A) gibt
  +39,2, der Skalar -9,42. Teil (i) von ID-F0 ist deshalb nicht eingetroffen. Den Doppler-Zaehler leistet dort nur das
  Spektrum (4 Kegel exakt).
- **[K3] N = 16 001 statt 16 000:** noetig wegen der Paritaet (Abschnitt 4). Folge: kein Bitvergleich mit -GROB; der
  Skalar ist auf denselben Netzen neu gerechnet.
- **[K4] Unordnungsband:** Bestaetigt im Spektrum (Abschnitt 4). Ob es zur k^2-Antwort beitraegt, bleibt offen:
  c_eff(A) = 1,7 +- 1,1 trennt 1 und 4 nicht. Das Band ist vermutlich auch die Quelle des grossen Rauschens von (A)
  [H].
- **[K5] Rauschregeln** wie -GROB; der Kartenwortlaut steht in Tabelle 2 daneben.
- **[K6] Vorzeichen:** geurteilt in der Fermion-Konvention (Grassmann). Mit +log|det| waeren alle Fermion-Werte
  umgekehrt.

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:**
   - Das feste regelmaessige Netz L = 63 (Kartenkontrolle ID-F0 Teil i) habe ich vor dem Einfrieren gerechnet und
     gesehen: c_eff(A) = +39,6 / +38,1 / +37,5. Die Schwelle der Karte (4 +- 1) blieb unveraendert; C6 und C7 standen
     vorher fest (10:18:20 CEST, AGENT-VORHERSAGEN-ENTWURF.txt).
   - Auf Zufallsnetzen habe ich vor dem Einfrieren nur Eigenwerte, Zeiten und Tor-Kennzahlen gesehen, keine y- oder
     c_eff-Werte. Die Probe der Auswertung lief auf Rauchdaten; ich habe weder ihre Zahlen noch ihr Bild angesehen.
2. **Code vor dem Einfrieren berichtigt:**
   - Erste Fassung: Nullmoden von (A) per Eigenwert-Abzug. Sie war falsch fuer gerades N (vier Nullmoden, Kontrolle
     K1 um 3,11 daneben). Ersetzt durch die exakte Nullvektor-Formel mit N ungerade.
   - Die Ordnung MMD_AT_PLUS_A fuer D blieb haengen (Diagonale null). Ich habe meine zwei Einheiten nach 70 s selbst
     gestoppt (systemctl --user stop, nur eigene Einheiten) und bin auf COLAMD zurueck.
   - In dirac_auswertung.py stand ein Rest der ersten Fassung (KeyError in der Probe); berichtigt vor dem Einfrieren.
3. **Nach dem Einfrieren:**
   - Code und Plan sind unveraendert (sha256 lokal und auf der .69 vor der Auswertung geprueft).
   - Waehrend der Laeufe habe ich nur Logzeilen (Nullvektor-Residuum, Gram-Abweichung, Zahl negativer w_e, Zeiten)
     und per jq die Tor-Kennzahlen von e1-s0 angesehen, keine y-Werte.
   - Die Zusatzbloecke (Saaten 72 bis 95 und 1072 bis 1095) habe ich um 10:26 CEST nach der Uhr gestartet, bevor
     Werte vorlagen. Sie waren um 11:22 fertig (Grenze 11:40).
   - Nach der Auswertung habe ich per jq beschreibend die Zellmittel von y(KD2) gegen die Zahl der w_e < 0 gestellt
     (Abschnitt 3.4). Das stand nicht im Plan; es ist keine Urteilsgrundlage.
   - Die Urteile hat die Auswertung mechanisch geliefert. Die Regressionszahl c0_eff = +39,19 (regelmaessig) stimmt
     mit meiner Handrechnung aus den Logwerten ueberein.
4. **Abweichungen vom Brief:**
   - N = 16 001 statt der Groessen aus -GROB (Paritaet, [K3]); E2 mit A = 4 N = 64 004.
   - Der Skalar ist auf denselben Netzen neu gerechnet, nicht aus -GROB uebernommen.
   - Kein Kaehler-Dirac auf dem regelmaessigen Netz (Diagonalen haben w = 0, also 1/w unendlich); die Karte verlangt
     dort nur (A).
5. **Spuren und Starts:**
   - Nur cpu und cpu7; 30 Starts.
   - Rauch und Proben: 12 Starts. Zwei davon (MMD-Versuch) habe ich selbst gestoppt, einer (erste Probe der
     Auswertung) endete mit rc = 1.
   - Hauptphase: regulaer L = 127, 16 Bloecke, Auswertung; alle rc = 0. Die Bloecke dauerten 6 min 18 s bis
     7 min 32 s (Grenze 10 min).
   - Die Bloecke einer Spur habe ich vorab gestartet; sie warteten am Lock der Spur. Es rechneten nie mehr als zwei
     zugleich. Je ssh-Aufruf ein Starteraufruf (teils mit mv und sha256sum davor im selben Aufruf).
6. **Auf der .69 ausserhalb des Starters:** mkdir, cp (Probe-Ordner aus Rauchdateien), mv, ls, sha256sum, jq,
   systemctl --user list-units und stop (nur meine Einheiten), sleep, date. Kein Python ausserhalb des Starters, keine
   Versionsprobe.
7. **Lokal:** kein python, awk oder perl. Benutzt: jq, ssh, scp, sha256sum, date, grep, sed, diff. Ausserhalb der
   Liste: mkdir, cp, ls, cat, head, tail, tr, cut, wc, rm (eine Hilfsdatei fuer sed) und sleep in Warteschleifen.
8. **Scratchpad:** Ich habe nichts in den Scratchpad der Leitung geschrieben. Die Werkzeugumgebung legt fuer
   Hintergrundbefehle eigene Ausgabedateien unter /tmp/claude-1000/.../tasks/ an; meine Ausgaben gingen per Umleitung
   in den Kartenordner.
9. **ssh-Multiplexing:** Mit bis zu 18 wartenden Verbindungen war der gemeinsame Multiplex-Socket voll. ssh fiel
   dann auf direkte Verbindungen zurueck (Meldung "Session open refused by peer" in einigen Logs). Alle Laeufe sind
   gestartet; andere Nutzer des Sockets haetten in dieser Zeit dasselbe gesehen.

## 7. Bedeutung

- **Vorab festgelegte Zweige:** "ID-F1 trifft ein" ist nicht ausgeloest. "ID-F1 verfehlt (c_eff ~ 4)" auch nicht:
  ID-F1 ist nicht auswertbar.
- **Was gilt [E]:**
  - Der Doppler-Zaehler funktioniert fuer den Skalar auf neuen, unabhaengigen Netzen: 0,92 +- 0,12. Die Aussage aus
    -GROB ("Zahl = Volumen" gibt Polyakov) haelt.
  - Der naive Dirac-Operator hat auf dem Zufallsnetz keine Doppler-Kegel, aber ein dichtes Band von Zustaenden bei
    E = 0. Seine Anomaliezahl ist mit 96 + 96 Saaten nur auf +-1,1 bestimmt (1,7). Fuer +-0,4 braeuchte man nach
    der Skalierung etwa 8-mal so viele Saaten.
  - Die Kaehler-Dirac-Bauweise mit zirkumzentrischen Hodge-Sternen ist auf diesem Netz unbrauchbar: Ihr dualer Teil
    misst vor allem, wie viele Kanten in der physikalischen Metrik nicht Delaunay sind (+48 statt -4 bzw. +2).
- **Was sich aendert [M, E]:**
  - Die Karte nennt Kaehler-Dirac als Ausweg, falls die Doppler bleiben. Das traegt nicht: Selbst im Kontinuum hat
    Kaehler-Dirac im gekruemmten 2D-Raum c = -4, also das falsche Vorzeichen fuer "Materie gibt die richtige
    Schwerkraft-Antwort" [M]. Auf dem Netz kommt noch das Artefakt dazu.
  - Das regelmaessige feste Netz taugt nicht als Doppler-Kontrolle fuer die Anomalie (+39 statt 4).
- **Naechste Schritte [H]:**
  - (a) (A) mit mehr Saaten oder geringerem Rauschen: etwa 800 Saaten je Netzabstand fuer SE 0,4 (etwa 8 h auf
    zwei Spuren), oder ein Wilson-Glied, das das Band bei E = 0 anhebt, als Gegenprobe "mit/ohne Doppler-Ersatz".
  - (b) KD auf dem intrinsischen Delaunay-Netz (Kanten nach physikalischer Metrik kippen, Variante intr aus
    INDUZIERT-DICHTE-2D) oder mit positiven Hodge-Sternen (baryzentrisch bzw. Whitney). Erwartung [M]: Der duale Teil
    faellt auf etwa -2, KD auf etwa -4.
  - (c) Die Paritaetsaussage (bei geradem N eine erzwungene zweite Nullmode) ist allgemein fuer naive Fermionen auf
    Dreiecksnetzen; fuer SPIN-ZUFALLSNETZ-1 (3D) waere zu pruefen, ob dort Entsprechendes gilt.
- **Rahmen:** 2D, euklidisch, gequenchtes Netzmittel, nur die konforme Mode, S = 0,5, Modell k^0 + k^2 + k^4.

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-102358, EINGEFROREN-SHA256.txt,
  AGENT-VORHERSAGEN-ENTWURF.txt (Agenten-Vorhersagen mit Zeit vor den Rauchlaeufen L = 63)
- code/:
  - dirac2d.py: Operatoren (A) und (B), Skalar, Modi dichte, regulaer, kontrolle
  - dirac_auswertung.py: Tor, Urteile, Ausgleich (Funktionen aus grob_auswertung.py), Bilder, Selbsttest
  - dichte2d_grob.py, zufall2d.py, induziert.py, grob_auswertung.py unveraendert aus -GROB
  - je mit Kopien *.eingefroren-20261004-102358
- lauf-69/:
  - e1-s0 bis e1-s84.json: E1 (N = 16 001, eps = 1), Saaten 0 bis 95
  - e2-s1000 bis e2-s1084.json: E2 (N = 16 001, A = 64 004, eps = 2), Saaten 1000 bis 1095
  - regulaer-L127.json: festes Quadratnetz
  - je mit .log; auswertung.json (Urteile), auswertung.log, PRUEFSUMMEN.txt (.69)
  - bild-ck-gegen-k2.png: c_eff(k) gegen (k eps)^2 je Bauweise und Netz, Linien c = 1, 2, 4 (KD auch -2, -4)
- rauch-69/: Logs der Rauchlaeufe und Proben, dirac2d.py.rauch1 (erste Codefassung)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde39-induziert-dirac/ (code/, rauch/, lauf/)

## 9. Einfach gesagt

Wir wollten wissen, ob Teilchen mit halbem Spin (wie Elektronen) auf einem Zufallsnetz mit "so viele Punkte wie Flaeche"
die richtige Antwort auf Schwerkraft geben, oder ob sie sich wie auf einem Schachbrett-Gitter vierfach zaehlen. Fuer
gewoehnliche Teilchen ohne Spin klappt der Test: Sie geben die richtige Zahl (0,92, richtig waere 1). Fuer die
einfachste Art von Spin-Teilchen ist die Messung zu verrauscht: Heraus kam 1,7 mit einer Unsicherheit von 1,1, das
passt sowohl zu "einfach" als auch beinahe zu "vierfach". Die zweite Bauart, die in der Literatur als Ausweg gilt, gibt
eine voellig falsche Zahl (48); das liegt an einer Schwachstelle unseres Netzes, und selbst ohne sie haette diese
Bauart nach unserer Rechnung das falsche Vorzeichen. Ausserdem sieht man: Die vierfachen Doppelgaenger des
Schachbretts verschwinden auf dem Zufallsnetz nicht einfach, sie verwandeln sich in einen Haufen fast energieloser
Zustaende.

