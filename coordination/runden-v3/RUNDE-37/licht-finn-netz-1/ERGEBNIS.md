# LICHT-FINN-NETZ-1: Ergebnis (Runde 43, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Karte: KARTE.md (unveraendert, bindend).
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 19:48:25 CEST. Gelesen bis zur Unterbrechung: Karte, WEYL-LINEAR-1 (ERGEBNIS, PLAN), Anfang von
    STRICH-NETZ-1/ERGEBNIS, QCA-DIAMANT-4/ERGEBNIS, die Dimensionsregel in AGENTS.md, kleintest.sh, ein Projekt-grep.
    Nach der Wiederaufnahme: Dossier Z. 85 bis 96, spinnetz.py (Kopf, matrix), Teile von qca_diamant.py, Felder der
    QCA-Dateien.
  - **Unterbrechung:** letzte eigene Messung 19:51:58 CEST (date -u auf der .69: 17:51:58 UTC). Abbruch durch das
    Sitzungslimit, laut Leitung gegen 19:53 CEST. Bis dahin kein Code, kein Plan, keine Rechnung.
  - **Wiederaufnahme** laut Leitung 21:44:09 CEST, eigene Messung 21:44:52 CEST. Zeitbox bis 23:09 CEST.
  - Code ab 21:53:14 CEST, Plan ab 21:57:21 CEST. Reine Syntaxpruefung ueber kleintest.sh 19:58:43 UTC (gibt keine
    Werte aus). **Eingefroren 21:59:14 CEST** (PLAN.md.eingefroren-20261004-215914, code/licht_netz.py.eingefroren-
    20261004-215914, EINGEFROREN-SHA256.txt; auf der .69 dieselben Pruefsummen).
  - Laeufe nach dem Einfrieren, alle rc = 0: L1 Rechnung (cpu4) 19:59:21 bis 19:59:49 UTC; L2 Bild (cpu11) 19:59:57 bis
    20:00:00 UTC; L3 Wiederholung (cpu11) 20:00:00 bis 20:00:27 UTC. Erste Sicht auf Werte nach L1.
  - Nachtrag Phase/Gruppe (Zusatz der Leitung): eingefroren 22:10:30 CEST, Syntaxpruefung 20:10:23 UTC, Lauf N1
    (cpu11) 20:10:38 UTC, rc = 0 (NACHTRAG-PHASE-GRUPPE.md).
  - Text ab 22:04:35 CEST (date unmittelbar vor der ersten Fassung). Letzte Aenderung ab 22:13:25 CEST (date
    unmittelbar vor dieser Zeile). Danach kein weiterer Lauf.
- **Code nach dem Einfrieren unveraendert.** lauf-69/PRUEFSUMMEN.txt (auf der .69 erzeugt, 14 Dateien) besteht lokal
  sha256sum -c (14 von 14).
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen (exakte Bloch-Eigenwerte, numpy der
  gpu-venv, 1 Thread). Keine Messdaten, keine Messdatenbestaetigung.
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik (ungeprueft), [P] Projektdatei, [S] Quelle, [H] Hypothese,
  [K] Kopfrechnung aus gerechneten Werten.
- **Einheit:** l = 1 PU = Tetraederkante (Pyrochlor-Abstand); Diamant-Kante b = 1,2247 PU. a1, a2, a4 fuer k in 1/PU
  aus omega/(c k) = 1 + a1 (k l) + a2 (k l)^2 + a3 (k l)^3 + a4 (k l)^4 + ...

## 1. Ergebnis zuerst

1. **Licht im engeren Sinn (Maxwell in der Coulomb-Phase auf Finns Netz) [E]:** Das langwellige Tempo ist isotrop (auf
   6e-15), beide Polarisationen sind gleich. Bei kurzen Wellen wird es langsamer: a2 = -1/12 laengs der Achsen,
   -5/48 laengs der Flaechendiagonalen, -1/9 laengs der Raumdiagonalen; Richtungsmittel -0,1015, Spannweite 27 % des
   Mittels. a4 liegt zwischen +0,0021 und +0,0064. Eine Doppelbrechung gibt es bis (k l)^4 nicht.
2. **Skalar [E, vorab abgeleitet M]:** Auf dem Diamant- und auf dem Pyrochlor-Graphen ist der Skalar exakt gleich
   (Pyrochlor ist der Kantengraph des Diamanten, Abschnitt 6): a2 von -0,0208 (Achsen) bis -0,0486 (Raumdiagonalen),
   Mittel -0,0390, Spannweite 71 %. Das stand vor der Rechnung im Plan.
3. **Spin-1/2-Operatoren haben ein lineares Glied [E].** Der Weyl-Operator auf dem Diamanten spaltet die beiden
   Haendigkeiten schon in erster Ordnung: a1 = -0,354 bzw. +0,354 laengs der Flaechendiagonalen, null nur laengs Achsen
   und Raumdiagonalen (so vorab im Plan abgeleitet, getroffen auf 4e-12). Der kopierte Weyl-Automat aus QCA-DIAMANT-4
   hat dazu ein richtungsabhaengiges Grundtempo (Spannweite 56 %) und a1 bis +-1,13. Der Grover-Lauf ist isotrop,
   ohne lineares Glied, mit a2 = 0 laengs der Achsen.
4. **Urteile:** LF0 nach Plan eingetroffen, nach Kartenwortlaut nicht eingetroffen. Das liegt nur am Weyl-Automaten
   ohne kubische Symmetrie, und das war vorab bekannt. LF1 und LF2 sind in beiden Lesarten eingetroffen.
5. **Bedingte Schranke:** Wenn das Netz das Licht traegt (Maxwell), verlangt LHAASO eine Tetraederkante
   l < 7,0e-28 m (Achsen; konservativ, weil die Ausrichtung unbekannt ist) bzw. < 6,1e-28 m (Raumdiagonalen). Das
   sind etwa 4e7 Planck-Laengen. Truege ein Spin-1/2-Operator mit linearem Glied das Licht, muesste l unter 0,2 l_P
   liegen. Der Richtungsanker (bis 33 % mehr Laufzeitversatz je nach Himmelsrichtung) ist [H]. Alle a-Werte sind
   Phasenkoeffizienten (omega/k); die Schranke ist in der Konvention der LHAASO-Arbeit gerechnet (Nachtrag).

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 5 durch code/licht_netz.py (Funktion urteile); Werte in lauf-69/ergebnis.json.

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | nach Plan | nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| LF0 | Langwelliges Tempo isotrop (Spannweite < 1e-6) fuer alle gerechneten Operatoren; Z^3 gibt a2 = -1/24 je Achse | 85 % | **eingetroffen** | **nicht eingetroffen** | Spannweite von c: hoechstens 3,7e-11 bei allen Operatoren mit kubischer bzw. tetraedrischer Symmetrie (S-D, S-P, W-D, Q-G, M-D, Z3-S, Z3-W, Z3-M), dazu 1D/2D; Q-W 0,565 (alle vier Zweige). Z3-S Achsen: abs(a2 + 1/24) <= 3,7e-9 |
| LF1 | [H] abs(a2) im Richtungsmittel zwischen 0,01 und 0,2 | 60 % | **eingetroffen** (M-D: 0,1015 in beiden Zweigen) | **eingetroffen** (alle 12 Zweige auf Finns Netz) | S-D 0,0390; S-P 0,0390; W-D 0,1303; M-D 0,1015; Q-W 0,0922; Q-G 0,0182 |
| LF2 | [H] Richtungsabhaengigkeit von a2 > 10 % des Mittels | 50 % | **eingetroffen** (M-D: 27,4 %) | **eingetroffen** (alle 12 Zweige) | Spannweite/abs(Mittel): S-D 0,712; S-P 0,712; W-D 0,639; M-D 0,274; Q-W 3,80; Q-G 1,53 |

- **LF0:** Die Planlesung nimmt den Weyl-Automaten Q-W aus, weil die Kartenpraemisse ([M] kubische Symmetrie) fuer ihn
  nicht gilt; das stand vor der Rechnung im Plan (Abschnitt 2 und 5). Nach dem Kartenwortlaut ("alle gerechneten
  Operatoren") scheitert LF0 an Q-W. Der Ausgang war vorab bekannt [P: QCA-DIAMANT-4 nennt 7 bis 52 % Streuung].
- **LF1 und LF2 fuer S-D und S-P** waren am Schreibtisch ableitbar (Plan Abschnitt 2: Mittel -0,0390, Spannweite 71 %).
  Getroffen auf 3e-8. Offen waren M-D, W-D, Q-W und Q-G.
- **Laengeneinheit:** Die Urteile gelten fuer l = Tetraederkante. In Einheiten der Diamant-Kante sind alle a2 durch 1,5
  zu teilen; M-D gaebe dann 0,068 und bliebe im LF1-Band, Q-G gaebe 0,0121 [K].

### 2.1 Agenten-Vorhersagen (PLAN Abschnitt 7, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. | Ergebnis |
|---|---|---|---|
| A1 | S-D trifft die Schreibtischformel auf 1e-6 | 85 % | **eingetroffen** (2,7e-8) |
| A2 | W-D: abs(a1) > 0,1 laengs 110, null laengs 100 und 111 | 65 % | **eingetroffen** (0,3536; Formel auf 4e-12) |
| A3 | M-D: abs(Mittel a2) in [0,01; 0,2] | 60 % | **eingetroffen** (0,1015) |
| A4 | M-D: Spannweite > 10 % | 70 % | **eingetroffen** (27 %) |
| A5 | M-D: Polarisationen unterscheiden sich in a2 um > 1e-3 in mindestens einer Richtung | 50 % | **nicht eingetroffen** (gleich auf ~1e-10 in allen 26 Richtungen, abgelesen) |
| A6 | LF0 nach Plan eingetroffen, nach Kartenwortlaut nicht | 70 % | **eingetroffen** |

## 3. a2 und a4 je Operator (Hauptfenster W0, 26 Richtungen)

Fit je Richtung und Zweig mit allen Potenzen bis k^8 an k = 0,01 bis 0,30 (1/PU). Richtungsmittel = arithmetisches
Mittel ueber die 26 Richtungen; Kugelmittel (200 Richtungen) nur beschreibend.

| Operator (Zweig) | Tempo c, Spannweite rel. | a1 (Bereich) | a2 Mittel | a2 100 / 110 / 111 | a2 Spannweite (rel.) | a2 Kugel | a4 Mittel | a4 min bis max |
|---|---|---|---|---|---|---|---|---|
| S-D Skalar Diamant | 1,0000; 8,6e-12 | 0 (<= 8e-10) | -0,03900 | -0,02083 / -0,04167 / -0,04861 | 0,02778 (0,712) | -0,03750 | -0,00079 | -0,00346 bis +0,00053 |
| S-P Skalar Pyrochlor | 1,0000; 3,7e-11 | 0 (<= 2e-9) | -0,03900 | wie S-D (auf 1e-7) | 0,02778 (0,712) | -0,03750 | -0,00079 | -0,00346 bis +0,00053 |
| W-D Weyl, Zweig lo | 0,8165; 3,8e-14 | -0,3536 bis 0 | -0,13034 | -0,08333 / -0,16667 / -0,11111 | 0,08333 (0,639) | -0,12857 | +0,00547 | +0,00208 bis +0,00833 |
| W-D Weyl, Zweig hi | 0,8165; 5,4e-14 | 0 bis +0,3536 | -0,13034 | wie lo | 0,08333 (0,639) | -0,12857 | +0,00547 | wie lo |
| **M-D Maxwell, beide Polarisationen** | 2,8284 (Code-Einheit); 6e-15 | 0 (<= 8e-13) | **-0,10150** | **-0,08333 / -0,10417 / -0,11111** | **0,02778 (0,274)** | -0,10000 | **+0,00457** | **+0,00208 bis +0,00638** |
| Q-W Weyl-Automat (4 Zweige, 2 Kegel) | 0,446 bis 0,864; 0,565 | -1,135 bis +1,135 | -0,0922 | stark richtungsabhaengig | 0,350 (3,80) | -0,0973 | -0,0042 | -0,041 bis +0,156 |
| Q-G Grover-Lauf (Kegelzweige) | 1,4142; 3e-13 | 0 (<= 1,1e-11) | -0,01816 | 0 / -0,02083 / -0,02778 | 0,02778 (1,53) | -0,01667 | -0,00206 | -0,00532 bis 0 |
| Z3-S Skalar Wuerfel (Kontrolle) | 1; 5e-12 | 0 | -0,02350 | -0,04167 / -0,02083 / -0,01389 | 0,02778 (1,18) | | +0,00020 | +0,00006 bis +0,00052 |
| Z3-W Weyl Wuerfel | 1; 9e-15 | 0 | -0,09402 | -0,16667 / -0,08333 / -0,05556 | 0,11111 | | +0,00317 | +0,00093 bis +0,00833 |
| Z3-M Maxwell Wuerfel (Yee) | 1; 4e-15 | 0 | -0,02350 | wie Z3-S, beide Pol. | 0,02778 | | +0,00020 | +0,00006 bis +0,00052 |
| K1-S Kette 1D | 1 | 0 | -0,04167 | (nur eine Achse) | 0 | | +0,00052 | |
| Q2-S Quadrat 2D | 1; 6e-12 | 0 | -0,03125 | Achse -0,04167, Diagonale -0,02083 | 0,02083 | | +0,00035 | |
| WB-S Wabe 2D | 0,8660; 3e-12 | 0 | -0,03125 | isotrop (Spannweite 2,6e-8) | 0 | | -0,00049 | |

- **Genauigkeit [E]:** Die Probefenster Wk (k <= 0,15) und Wg (k <= 0,60) geben a2 gleich auf <= 2e-7 (Q-W
  <= 1,5e-6). a4 ist bei Maxwell auf ~5e-9 stabil, bei Weyl auf ~1e-7, bei den Skalaren nur auf ~1e-5 (S-D -0,00079 /
  -0,00080 / -0,00079; Kontrolle Z3-S gegen die Formel 2,2e-6). Restfehler der Fits relativ <= 2e-12.
- **Kartenmodell nur mit geraden Potenzen** (beschreibend): gleich dem vollen Fit bei S-D, S-P, M-D, Q-G und den
  Kontrollen; bei W-D und Q-W sinnlos (a2 = -1,66 bzw. +1,38, a4 ~ +-35), weil dort ein lineares Glied steht.
- **Form [K, abgelesen; die Form selbst ist durch die kubische Symmetrie erzwungen, M]:** Mit S4 = sum n_i^4 gilt
  M-D: a2 = -1/8 + S4/24; S-D: a2 = -1/16 + S4/24; Q-G: a2 = (S4 - 1)/24; Z3-S und Z3-M: a2 = -S4/24. Die absolute
  Richtungsspanne ist bei allen vier 1/36. Auf Finns Netz sind die Achsen am wenigsten verlangsamt, auf dem Wuerfel am
  meisten.
- **Q-W** ist ein einzelner Vertreter einer Familie (QCA-DIAMANT-4: 40 Treffer mit verschiedenen Tempi) und steht nicht
  fuer "den" Weyl-Automaten. Bei k = 0 hat W(0) zwei Zweifach-Cluster (Eigenphasen -0,810 und 2,077), also zwei
  Weyl-Kegel. a2 bezieht sich je Richtung auf das eigene Tempo c(n).

## 4. Bedingte Maschen-Schranke ("wenn das Netz das Licht traegt")

- **Formel [M, nachgerechnet]:** Gruppentempo c (1 + 3 a2 (k l)^2) gleich LHAASO c [1 - (3/2)(E/E_QG,2)^2] mit
  E = hbar c k gibt l = hbar c / (E_QG,2 sqrt(2 abs(a2))). Einheiten: GeV m / GeV = m. E_QG,2 > 6,9e11 GeV
  (subluminal; STRANG-ANKER-L Z. 86 [P]; im Nachtrag an der Quelle gelesen, lhaaso-2402.06009.txt Z. 469-471 [S]).
  Kopfprobe im Code: kappa = 0,117 gibt 5,912e-28 m, wie
  WEYL-LINEAR-1 (5,91e-28 m). Alle a2 < 0 (subluminal), ausser Q-G laengs der Achsen (dort a2 = 0).
- l ist die **Tetraederkante**; die Diamant-Kante ist 1,2247 l.
- **[Nachtrag nach Zusatz der Leitung 22:1x, beschreibend; Einzelheiten in NACHTRAG-PHASE-GRUPPE.md]:**
  - Alle a1, a2, a4 dieses Berichts sind **Phasenkoeffizienten** (Fit an omega/k). Das Gruppentempo hat 2 a1, 3 a2 und
    5 a4; fuer Maxwell ist g2 = 3 a2 = -0,25 (Achsen) bis -0,33 (Raumdiagonalen).
  - Die Schranken oben entsprechen der Konvention der Quelle (LHAASO Gl. (1) Z. ~165-172, Gl. (2) Z. 141-147, Grenzen
    Z. 466-471). Ein eigener Nachtrag-Lauf rechnet sie ueber Phase und Gruppe, beide Wege stimmen auf 3e-16 ueberein.
  - Die WEYL-LINEAR-1-Zahl 5,9e-28 m ordnet Phase und Gruppe richtig zu (Faktor 1).

| Operator | konservativ (kleinstes abs(a2)) | Richtungsmittel | streng (groesstes abs(a2)) | lineares Glied (E_QG,1 = 1,0e20 GeV) |
|---|---|---|---|---|
| **M-D Maxwell** | **7,0e-28 m (4,3e7 l_P), Achsen** | 6,3e-28 m | 6,1e-28 m (Raumdiagonalen) | keines |
| S-D, S-P Skalar | 1,4e-27 m | 1,0e-27 m | 9,2e-28 m | keines |
| W-D Weyl | 7,0e-28 m | 5,6e-28 m | 5,0e-28 m | **2,8e-36 m (0,17 l_P)** fuer fast alle Richtungen (a1 = 0 nur laengs Achsen und Raumdiagonalen) |
| Q-W Weyl-Automat | 1,7e-27 m | 6,7e-28 m | 3,3e-28 m | **8,7e-37 m (0,05 l_P)** |
| Q-G Grover | keine (a2 = 0 laengs der Achsen) | 1,5e-27 m | 1,2e-27 m | keines |

- **Lesart [H]:** Traegt Finns Netz das Licht als Maxwell-Feld, muss die Tetraederkante unter etwa 7e-28 m liegen.
  Das ist eine bedingte Schranke an ein gedachtes Netz, keine Messung einer Masche.
- **Richtungsanker [H]:** a2 von M-D unterscheidet sich zwischen Achsen (1/12) und Raumdiagonalen (1/9) um den
  Faktor 4/3 [K]. Gammablitze aus verschiedenen Himmelsrichtungen saehen bei festem Netz bis 33 % verschiedene
  quadratische Laufzeitversaetze. Ein Test braeuchte mehrere Quellen mit Energie-Laufzeit-Messung; die Schranke oben
  stammt aus einer Quelle mit unbekannter Ausrichtung.
- **Doppelbrechungsanker:** Maxwell auf Finns Netz hat bis (k l)^4 keine Doppelbrechung (beide Polarisationen in allen
  26 Richtungen gleich auf ~1e-10 in a2 und ~3e-9 in a4). Die Spin-1/2-Operatoren W-D und Q-W haben eine lineare
  Aufspaltung der Haendigkeiten; fuer Photonen waere das lineare Doppelbrechung. Der Anker des Dossiers dafuer
  (> 1,8e34 GeV [P]) ist nur genannt und nicht auf l umgerechnet.

## 5. Bild

bild-licht-finn-netz.png (auch lauf-69/), aus dem eingefrorenen Code:
- (a) a2 je Richtung und Zweig (blau 100, orange 110, gruen 111), grau das LF1-Band.
- (b) a4 je Richtung.
- (c) omega/(c k) - 1 gegen k fuer 100, 110 und 111. **Vorsicht:** Normiert ist mit dem Richtungsmittel von c. Bei
  Q-W gibt das die Versaetze bei k = 0 (-0,4 und -0,07), weil sein Tempo richtungsabhaengig ist. Die schraegen
  Geraden sind die linearen Glieder von W-D (110) und Q-W.
- (d) bedingte Schranke je Zweig (Punkt Mittel, Strich von streng bis konservativ), rot die Planck-Laenge.
  **Vorsicht:** Die Q-G-Striche bis 3e-23 m kommen aus Fitrauschen (a2 ~ 2e-10 laengs der Achsen) und bedeuten
  "keine Schranke". Die leeren Spalten Q-G/1 und Q-G/2 sind die flachen Grover-Zweige.

## 6. Kontrollen, Schreibtisch, Dimensionsvergleich

- **Code-Kontrollen [E]:**
  - 4 Sechsringe je Zelle, rot grad <= 1,2e-15, Eichnullen <= 5,4e-15, kleinster Photon-Eigenwert bei 50 zufaelligen k
    2,08 (keine weiteren Nullmoden)
  - QCA unitaer <= 4,9e-15; W-D hermitesch (0,0); Tetraederkante 1,0; 6 Pyrochlor-Nachbarn, alle im Abstand 1
  - L3 wiederholt L1 bis auf argv und Laufzeiten exakt (jq -S ohne diese Felder, gleiche sha256)
- **Schreibtisch gegen Rechnung:**

| Formel (Plan, vor der Rechnung) | groesste Abweichung |
|---|---|
| S-D a2 = -(3 - 2 S4)/48 | 2,7e-8 |
| W-D a1 = +-(b/sqrt3) abs(q^ x n) | 4,3e-12 |
| Z3-S a2 / a4 | 1,2e-8 / 2,2e-6 |
| Z3-W a2 / a4 | 3,4e-11 / 5,5e-9 |
| Z3-M a2 / a4 | 2,2e-11 / 4,1e-9 |
| K1-S a2 | 2,6e-9 |
| Q2-S a2 | 1,4e-8 |
| WB-S a2 = -1/32 | 1,5e-8 |

- **Nachtraeglich erklaert [M, ungeprueft]:** S-P = S-D exakt. Der Pyrochlor-Graph ist der Kantengraph des
  Diamanten. Mit der (vorzeichenlosen) Inzidenzmatrix B gilt fuer die Laplace-Matrix L_P = 8 - B^T B, und fuer den
  4-regulaeren Diamanten B B^T = 4 + A_D = 8 - L_D. Die von null verschiedenen Eigenwerte von B^T B sind die von
  B B^T. Also hat L_P je k genau die Eigenwerte von L_D und dazu zwei flache Zweige bei 8. Der akustische Zweig ist
  derselbe.
- **Dimensionsvergleich (AGENTS.md):**
  - Allgemein gilt: Das langwellige Tempo ist bei diesen Operatoren isotrop, sobald die Gittersymmetrie den Tensor
    2. Stufe festlegt. Das k^2-Glied ist ein Tensor 4. Stufe.
  - 1D: nur eine Richtung (-1/24).
  - 2D: Das Quadratgitter ist anisotrop (-1/24 gegen -1/48). Die Wabe, das 2D-Gegenstueck des Diamanten, ist isotrop
    (-1/32): Die Sechszaehligkeit macht den Tensor 4. Stufe isotrop.
  - 3D: Kubische bzw. tetraedrische Symmetrie kann das nicht. Auf Finns Netz bleibt bei den kubisch-symmetrischen
    Operatoren eine Anisotropie von 27 % (Maxwell) ueber 64 % (Weyl) und 71 % (Skalar) bis 153 % (Grover).
  - Das ist gerechnet fuer diese nearest-neighbour-Operatoren, kein Satz ueber alle Netze.

## 7. Selbstanzeigen

1. **Unterbrechung:** Lauf vom Sitzungslimit abgebrochen. Letzte eigene Messung 19:51:58 CEST, Wiederaufnahme
   21:44:09 CEST (Leitung) bzw. 21:44:52 CEST (eigene Messung). Zwischen 19:52 und 21:44 habe ich nichts getan.
2. **grep vor der neuen Ausschlussregel:** Mein einziger Projekt-grep (QCA-DIAMANT, gegen 19:50 CEST) folgte dem
   ersten Auftrag: --exclude-dir fuer vertraege-20260925, ks-1-dk-lauf, ks-1-dk-laeufe, dazu --exclude fuer Dateien mit
   VERSIEGELT oder T8-SOLL im Namen. Ein --exclude-dir=VERSIEGELT fehlte; diese Regel kam erst mit der Nachricht der
   Leitung. Ausgegeben wurden nur Dateinamen (-l), keiner in einem versiegelten Pfad. Keine versiegelte Datei geoeffnet,
   keine KS-1-Ergebnisse.
3. **Syntaxpruefung vor dem Einfrieren:** einmal python -c "ast.parse(...)" ueber kleintest.sh (cpu4). Sie gibt keine
   Werte aus. Ein Rauchlauf fand nicht statt; L1 war die erste Rechnung.
4. **Planfehler bei L3:** Der Plan erwartete gleiche sha256. Die Ergebnisdatei enthaelt aber argv und Laufzeiten,
   deshalb sind die Pruefsummen verschieden. Verglichen habe ich mit jq -S ohne diese Felder; das Ergebnis ist gleich.
5. **Lokale Werkzeuge ueber die Liste hinaus:** date, ls, mkdir, cp, cat, head, tail, wc und sort (nur Anzeige); kein
   python, awk oder perl.
   - jq hat nur gelesen. Ausnahmen: In der Anzeige hat jq die Richtungsvektoren auf drei Stellen gerundet und Felder
     geloescht (fuer den L3-Vergleich).
   - Einmal hat eine Anzeige mit Stringkuerzung Zahlen in E-Schreibweise abgeschnitten (2,18e-10 sah aus wie 2,18). Ich
     habe es vor dem Schreiben an den vollen Werten bemerkt; im Text stehen nur die vollen Werte.
6. **Kopfrechnungen im Text [K]:**
   - die Schreibtischwerte im Plan (S-D-Formel und Zahlen, W-D a1 = 0,354)
   - die Formen a2 = alpha + beta S4 aus den abgelesenen Klassenwerten
   - der Faktor 4/3 bzw. 33 %
   - die a2-Werte in Diamant-Kanten-Einheiten (0,068; 0,0121)
   - der Vergleich der Polarisationen (abgelesen, nicht gerechnet)
   - Alle anderen Zahlen stammen aus ergebnis.json.
7. **Auf der .69 ausserhalb von kleintest.sh:** mkdir, cp (QCA-DIAMANT-4-Dateien nach alt/, Pruefsummen gleich), cat,
   ls, grep (auf kleintest.sh, Spuren nachsehen), uptime, sha256sum, wc, date. Kein Python ausserhalb von
   kleintest.sh, kein Dienst, keine Laufkette vor dem Einfrieren.
8. **Bild nicht nachgebessert:** Panel (c) ist bei Q-W irrefuehrend normiert; Panel (d) zeigt bei Q-G eine
   Rausch-Schranke. Beides steht in Abschnitt 5.
9. **Q-G-Schranke im JSON:** Der Code wertet a2 ~ 2e-10 laengs der Achsen nicht als null. Deshalb steht dort
   "konservativ 3,1e-23 m" und a2_alle_negativ = false. Das ist Rauschen; im Text steht "keine Schranke".
10. **Lesarten, vor dem Einfrieren festgelegt:**
    - "Maxwell auf Kanten" als Coulomb-Phase auf den Diamant-Kanten; Maxwell auf den Pyrochlor-Kanten ist nicht
      gerechnet (Plan Abschnitt 2).
    - Laengeneinheit = Tetraederkante.
    - Richtungsmittel = arithmetisch ueber die 26 Richtungen.
    - LF1/LF2 nach Plan nur fuer Maxwell.
    - Das Urteil haengt an der Einheit nur bei Q-G (0,0182 bzw. 0,0121): beide liegen im Band.
11. **Q-W ist ein Vertreter:** Seine Zahlen (Grundtempo-Spannweite 56 %, a1 bis 1,13) stehen fuer einen Zufallspunkt
    der L2:P+P-Familie. QCA-DIAMANT-4 nennt 7 bis 52 % "Streuung" mit einem anderen Mass. Der Vergleich ist nicht
    geprueft.
12. **Ungeprueft [M]:** Schreibtischformeln (bestaetigt nur durch die Numerik), die Kantengraph-Erklaerung,
    Einheitenrechnung der Schranke (nachgerechnet, nicht gegengelesen). Im Hauptteil keine Quelle neu gelesen
    (LHAASO-Werte aus dem Dossier [P]); im Nachtrag die LHAASO-Arbeit an den genannten Zeilen gelesen [S].
13. **Nachtrag nach Sicht auf die Ergebnisse:** Auf den Zusatz der Leitung (22:1x) habe ich ein neues Skript
    (code/nachtrag_gruppe.py) geschrieben, vor seinem Lauf eingefroren und ueber kleintest.sh (cpu11) gerechnet. Es ist
    beschreibend und aendert kein Urteil. Der eingefrorene Code ist unberuehrt. Weitere Selbstanzeigen dazu stehen in
    NACHTRAG-PHASE-GRUPPE.md (N2). In diesen Bericht habe ich danach nur gekennzeichnete Hinweise eingefuegt
    (Abschnitte 1.5 und 4, Zeiten, Dateien).

## 8. Einfach gesagt

Wir haben ausgerechnet, wie schnell Wellen auf Finns Netz aus Tetraedern laufen, wenn sie sehr kurz werden. Lange
Wellen laufen in alle Richtungen gleich schnell. Kurze Wellen werden langsamer, und zwar je nach Richtung verschieden
stark: Beim "Licht" des Netzes (Maxwell) betraegt der Unterschied zwischen den Richtungen etwa ein Viertel. Weil
Messungen an Gammastrahlen keine solche Verlangsamung finden, muesste die Tetraederkante kleiner als etwa 7e-28 m
sein, wenn das Netz das Licht traegt. Das ist eine Rechnung an einem gedachten Netz, keine Messung.

## 9. Dateien

- KARTE.md, PLAN.md, PLAN.md.eingefroren-20261004-215914, EINGEFROREN-SHA256.txt, ERGEBNIS.md, bild-licht-finn-netz.png
- code/licht_netz.py und code/licht_netz.py.eingefroren-20261004-215914
- lauf-69/: ergebnis.json (L1), ergebnis-wdh.json (L3), bild-licht-finn-netz.png (L2), L1-rechnen.log, L2-bild.log,
  L3-wdh.log, S0-syntax.log, PRUEFSUMMEN.txt
- Auf der .69: /home/fmh/fmhc-physics-remote/licht-finn-netz-1/ (code/, alt/, lauf/, syntax/, PLAN.md, Kopien)
- **Nachtrag (22:1x):** NACHTRAG-PHASE-GRUPPE.md (mit .eingefroren-20261004-221030), NACHTRAG-EINGEFROREN-SHA256.txt,
  code/nachtrag_gruppe.py (mit Kopie), lauf-69/nachtrag-gruppe.json, N1-nachtrag.log, S1-syntax-nachtrag.log,
  lauf-69/PRUEFSUMMEN-NACHTRAG.txt

## Vermerk der Leitung (05.10.2026, 14:06:37 CEST, date; nach HOEHE-ISOTROP-1)

- Der hier gerechnete Operator ist M-D (Coulomb-Phase auf den Diamant-Kanten, Fluss-Eis-Licht), nicht DEC-Maxwell auf den Kanten von V. Die bedingte Schranke l < 7,0e-28 m gilt fuer M-D.
- DEC-Maxwell auf V (HOEHE-ISOTROP-1): Laufzeitschranke l < 1,6e-27 m (Mittel), dazu Doppelbrechung schon in Ordnung (k a)^2 (1e-4 bis 1,9e-3 a^2). Text oben unveraendert; Sicherung ERGEBNIS.md.bak-vermerk-operator.
