# OKTA-SCHATTEN-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 46)

- Karte: KARTE.md (unveraendert, bindend). Plan: PLAN.md, eingefroren 2026-10-05 07:40:44 CEST
  (PLAN.md.eingefroren-20261005-074044, code/okta.py.eingefroren-20261005-074044, EINGEFROREN-SHA256.txt; auf der .69
  dieselben Pruefsummen, EINGEFROREN-SHA256-69.txt dort).
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen (exakte Bloch-Matrizen, numpy der
  gpu-venv, 1 Thread). Keine Messdaten, keine Messdatenbestaetigung.
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik (vorab im Plan, ungeprueft), [K] Kopfrechnung aus gerechneten
  Werten, [P] Projektdatei, [S] Quelle, [H] Hypothese.
- Einheiten: Licht in l = Tetraederkante = 1. Wabe in kubischen Einheiten (Kante der Wabe sqrt2/2 = 2 l).

## 1. Zeiten und Laeufe (date; .69 in UTC, CEST = UTC + 2)

- Start 07:14:07 CEST. Kopien der Originale bis 07:27:17 CEST, okta.py danach; Plan ab 07:38:25, eingefroren
  07:40:44 CEST. Text dieser Datei ab 07:47:43 CEST, letzte Aenderung ab 07:50:04 CEST (date unmittelbar davor).
  Zeitbox bis 09:44 CEST, eingehalten. Kein Lauf mehr aktiv.
- Alle Laeufe ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh im Arbeitsordner
  /home/fmh/fmhc-physics-remote/okta-schatten-1/ (1 Thread, RuntimeMaxSec 600).

| Lauf | Spur | Aufruf | Start / Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| r1 (Rauch) | cpu | okta.py licht --klein --rauch | 05:36:41 / 05:36:42 | 0,9 s | 0 |
| r2 (Rauch) | cpu | dasselbe nach Einheitenkorrektur | 05:37:10 / 05:37:11 | 0,9 s | 0 |
| r3 (Rauch) | cpu7 | okta.py schwer --klein --rauch | 05:37:22 / 05:37:26 | 4,4 s | 0 |
| L1 | cpu | okta.py licht --out lauf/licht.json | 05:40:55 / 05:41:22 | 27,5 s | 0 |
| L2 | cpu7 | okta.py schwer --out lauf/schwer.json | 05:41:23 / 05:41:32 | 9,4 s | 0 |
| L3 | cpu | okta.py bild ... | 05:44:04 / 05:44:05 | 1,0 s | **1** (KeyError, Selbstanzeige 2) |
| L4 | cpu7 | Wiederholung L1 -> lauf/licht-wdh.json | 05:44:05 / 05:44:32 | 27,9 s | 0 |
| L5 | cpu | Wiederholung L2 -> lauf/schwer-wdh.json | 05:44:32 / 05:44:42 | 9,5 s | 0 |
| L6 | cpu | bild_okta.py (Nachtrag, eingefroren 07:45:36 CEST) | 05:45:37 / 05:45:40 | 3,6 s | 0 |

- L4 und L5 wiederholen L1 und L2 exakt (jq -S ohne info, Laufzeiten, zeiten: gleiche sha256).
- lauf-69/PRUEFSUMMEN.txt (auf der .69 erzeugt, 11 Dateien) besteht lokal sha256sum -c (11 von 11).

## 2. Ergebnis zuerst

1. **Licht ohne Sechsecke steht still, mit Sechsecken laeuft es isotrop [E; beides vorab abgeleitet, M].** Ohne die
   Sechseck-Plaketten der Loecher sind alle 8 physikalischen Baender flach: 2 Nullbaender und 6 bei omega^2 = 8
   (DEC-Gewichte). Mit ihnen gibt es an keinem der 789 k eine Nullmode mehr. Die zwei Photonen laufen dann mit
   c = 1,00000000 in allen 26 Richtungen (Spannweite 6e-11), ohne Doppelbrechung bis k^2. **Zwei flache Baender bei
   omega^2 = 8 bleiben** fuer jede Sechseck-Kopplung.
2. **Neu gemessen: die Dispersion des Lichts mit Schattenflaechen [E, Form K].** Es gilt a2 = -5/64 + S4/24:
   -0,0365 laengs der Achsen, -0,0573 laengs der Flaechendiagonalen, -0,0642 laengs der Raumdiagonalen. Das Mittel
   ist -0,0546, die Spannweite 51 % des Mittels. Das Licht ist damit schwaecher dispersiv als Maxwell auf den
   Diamant-Kanten (M-D: -1/12 bis -1/9). Das Tempo setzt die Sechseck-Kopplung q = w_H/w_D:
   c^2 = 8q/(1 + 2q) [K, an 7 Werten von q getroffen]. Die Schattenflaechen bestimmen also das Lichttempo.
3. **Die Tetraeder-Oktaeder-Wabe mit zerlegten Oktaedern (H3, Haupt) ist bei kleinem k instabil [E].** Wachsende
   Moden gibt es in 3 von 13 und in 12 von 23 Richtungen. In [210] hat ein TT-Zweig omega^2/k^2 = -0,28. Am Gitter
   (511 k) ist A_red an 6 k nicht positiv. Damit ist **OS2 nicht eingetroffen und OS3 nicht entscheidbar**; die
   "Spanne" von H3 ist wegen omega^2 < 0 nicht definiert.
4. **Isotrop ist die Wabe nur mit dem Oktaeder als starrer, ganzer Zelle (R12) [E; vorab abgeleitet, M].** R12 hat
   omega^2/k^2 = 1,5 in allen Richtungen (Spanne 3,9e-7 einschliesslich Dispersion, Grenzwert 5e-9), ist an allen
   Punkten stabil und traegt genau zwei TT-Moden.
   - Zerlegt man das Oktaeder anders, verliert die Wabe die Isotropie: mit Mittelpunkt (Z8) 100 % Spanne, mit einer
     Diagonale (D1z) 95 %. Beides ist weit ueber V (6,34 %).
   - Z8 ist an allen gerechneten Punkten stabil. D1z hat in 2 von 23 Richtungen eine wachsende Diagonalmode.
5. **Die Diagonalwahl kostet im flachen Netz nichts; sichtbar ist sie nur in der Bewegungsenergie [E].**
   - Schur-Komplement ueber die Diagonale = starres Oktaeder, auf 7e-9.
   - Der umkreisbasierte Stern *1 der Diagonale ist 0.
   - Der Takt-Operator ist bei allen Wahlen gleich.
   - Die Rhombendodekaeder (duale Zellen) tragen die Takt-Gewichte exakt: W^+ B W = -2 Summe_e *1_e |1 - e^{ik.T_e}|^2
     an allen 524 k (auf 1e-8), mit *1 = Rautenflaeche/Kante = 1/4.

## 3. Urteile (mechanisch nach PLAN.md Abschnitt 4; Werte in lauf-69/licht.json und schwer.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut | vorab ableitbar? | tragende Zahlen [E] |
|---|---|---|---|---|---|---|
| OS0 | ohne Sechsecke 2 flache Baender je k | 85 % | **eingetroffen** | **nicht eingetroffen** | **ja, beide** (PLAN 2.1) | an allen 789 k genau 2 Nullmoden; flache Baender: 0 (x2) und 8,000 (x6); Eichrang 4 |
| OS1 | [H] mit Sechsecken verschwinden die flachen Baender bei allen k != 0, langwelliges Tempo isotrop | 70 % | **eingetroffen** | **geteilt** | **ja, beide** (PLAN 2.1) | Nullmoden an 789 k: 0; flach: 8,000 (x2); c = 0,99999999998 / 1,00000000002, Spannweite 6,2e-11 / 8,4e-11 |
| OS2 | [H] Wabe traegt genau zwei masselose TT-Moden und ist bei kleinem k stabil | 65 % | **nicht eingetroffen** | **nicht eingetroffen** | "genau zwei" ja (Zaehlung), Stabilitaet nein | H3: wachsend in [100], [210], [310] und 12 von 23 Zufallsrichtungen; in [210] nur 1 masselos (anderer TT-Zweig omega^2/k^2 = -0,283); TT-Anteil der masselosen >= 1 - 1e-13 |
| OS3 | [H] TT-Spanne ohne Abstimmung unter V (6,34 %) | 50 % | **nicht entscheidbar** | Code: "eingetroffen"; **inhaltlich nicht entscheidbar** (Selbstanzeige 3) | nein | H3 nicht Z-gueltig (negative Mode); "Spanne" -5,42 ist kein Streumass; V in diesem Lauf 6,3388 % |

- **OS0:** Nach Plan zaehlen die Nullbaender (HODGE-L: "2 flache Nullbaender"), nach Kartenwortlaut alle flachen
  Baender (8). Beides stand vorab im Plan. Es ist eine Kontrolle, keine Messung.
- **OS1:** (i) Die Nullbaender verschwinden (Plan). Nach Kartenwortlaut verschwinden nicht alle flachen Baender: Zwei
  bleiben bei omega^2 = 4 w_D/s1. Das stand vorab im Plan (Kern von C_H auf dem Wirbelraum der Tetraeder). (ii) Die
  Isotropie folgt aus der Wuerfelsymmetrie; am Code bei k != 0 geprueft: 26 Richtungen, dazu 48 Bilder bei
  k = 0,2/l gleich auf 5e-15.
- **OS2:** Nach der EW1-Regel faellt H3 an 6 von 26 und an 24 von 46 Punkten durch, jeweils mit wachsenden Moden.
  - Zwei Arten: eine Diagonalmode mit omega^2 von -0,34 bis -3,84, konstant in k, und TT-Zweige mit omega^2 ~ -k^2
    ([210] -0,283 k^2, z2 -16,9 k^2).
  - B_red ist ueberall positiv definit. Das negative Vorzeichen kommt aus A_red, der zellweisen Bewegungsenergie.
  - Die Zahl "zwei" war vorab ableitbar; das Scheitern liegt an der Stabilitaet.
- **OS3:** Nach Plan nicht entscheidbar, weil H3 nicht Z-gueltig ist (Regel vorab). Die Kartenwortlaut-Regel im Code
  prueft die Gueltigkeit nicht und vergleicht -5,42 < 0,0634. Ihre Ausgabe "eingetroffen" ist ein Artefakt; ich werte
  OS3 auch nach Kartenwortlaut als nicht entscheidbar.
- **Bedeutung nach der Karte:** Der Fall "OS2 und OS3" ist nicht ausgeloest. Der Fall "OS3 verfehlt" ist formal auch
  nicht ausgeloest. Beschreibend gilt: Mit zerlegten Oktaedern braucht die Wabe Abstimmung oder ist instabil; die
  Schattenform allein loest die Isotropie nur als ganze, starre Zelle (R12).

### 3.1 Agenten-Vorhersagen (PLAN Abschnitt 5, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. | Ergebnis |
|---|---|---|---|
| A1 | DEC-Licht c = 1 auf 1e-6, Polarisationen gleich | 85 % | eingetroffen (c - 1 <= 2e-11; Zweige gleich auf 1,2e-10) |
| A2 | mit Sechsecken genau 2 flache Baender bei 8, keine Nullmode | 75 % | eingetroffen |
| A3 | DEC: a2 < 0 in allen 26 Richtungen, Spannweite > 10 % | 60 % | eingetroffen (-0,0365 bis -0,0642; 51 %) |
| A4 | H3 genau 2 masselose TT, stabil | 60 % | nicht eingetroffen |
| A5 | H3 Spanne < 6,34 % | 55 % | nicht entscheidbar (instabil) |
| A6 | R12 Spanne < 1e-4 | 80 % | eingetroffen (3,9e-7) |
| A7 | Schur gegen R12 <= 1e-10 relativ | 85 % | nicht eingetroffen (3,7e-9 bis 6,7e-9; Rundung bei kleinem k, Selbstanzeige 6) |
| A8 | P(k)/L(k) fuer R12 konstant auf 1e-8 | 50 % | eingetroffen (4,5e-9) |

## 4. Tabellen

### 4.1 Licht auf den Pyrochlor-Kanten (789 k; Dispersion W0, 26 Richtungen)

| Variante | w_D / w_H / s1 | Nullmoden je k | flache Baender (Wert x Zahl) | Tempo c (Spannweite rel.) | a2 100 / 110 / 111 | a2 Mittel (26) / Kugel | a2 Spannweite rel. | a4 Bereich | Doppelbrechung |
|---|---|---|---|---|---|---|---|---|---|
| ohne Sechsecke (DEC-Gewichte) | 2,828 / - / 1,414 | 2 (alle 789 k) | 0 x 2, 8 x 6 | 0 (laeuft nicht) | - | - | - | - | - |
| ohne Sechsecke (Gewichte 1) | 1 / - / 1 | 2 | 0 x 2, 4 x 6 | 0 | - | - | - | - | - |
| **mit Sechsecken, DEC (Haupt)** | 2,828 / 0,471 / 1,414 | **0** | **8 x 2** | **1,00000000 (6e-11)** | **-0,036458 / -0,057292 / -0,064236** | -0,05462 / -0,05313 | **0,509** | -0,0042 bis -0,0006 | a2 <= 3,8e-7, c <= 1,2e-10 |
| mit Sechsecken, Gewichte 1 | 1 / 1 / 1 | 0 | 4 x 2 | 1,1547005 = 2/sqrt3 (6e-11) | -0,027778 / -0,048611 / -0,055556 | -0,04594 / -0,04445 | 0,605 | -0,0040 bis -0,0001 | a2 <= 2,5e-7 |
| Kontrolle M-D (LICHT-FINN-NETZ-1) | - | - | - | - | -1/12 / -5/48 / -1/9 auf 2,8e-11 | - | - | - | - |

- Hodge-Sterne aus der Geometrie [E] = Handwerte des Plans [M]: *1 = sqrt2, *2(Dreieck) = 2 sqrt2,
  *2(Sechseck) = sqrt2/3 (Abweichung <= 4,4e-16). Duale Volumenproben 1,000; Patch-Proben <= 1,1e-16; rot grad
  <= 9,2e-16.
- Form [K, an den Klassenwerten abgelesen, auf 2e-7]: DEC a2 = -5/64 + S4/24 (-7/192, -11/192, -37/576); Gewichte 1
  a2 = -5/72 + S4/24. Die absolute Richtungsspanne ist wieder 1/36, wie bei allen Operatoren von LICHT-FINN-NETZ-1.
  Das Kugelmittel -0,05313 passt zu S4-Kugelmittel 3/5 [K].
- Probefenster: a2 aus Wk und Wg weicht <= 1,0e-6 von W0 ab. Fit-Rest relativ <= 2,2e-12.
- Bandobergrenze omega^2: 32/3 (DEC), 12 (Gewichte 1). Photon bei X: omega = 1,63/l (DEC, Bild a).

**Abtastung der Sechseck-Kopplung** (DEC-w_D und -s1; 116 k; Tempo bei |k| = 1e-3/l, 13 Richtungen):

| w_H/w_D | 0 | 1e-3 | 1e-2 | 0,1 | 1/6 (DEC) | 1 | 10 | 100 |
|---|---|---|---|---|---|---|---|---|
| Nullmoden je k (max) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| flache Baender | 8 (0 x 2, 8 x 6) | 2 (bei 8) | 2 | 2 | 2 | 2 | 2 | 2 |
| c | 0 | 0,0894 | 0,2801 | 0,8165 | 1,0000 | 1,6330 | 1,9518 | 1,9950 |
| Spannweite rel. von c | - | 5,7e-7 | 6,9e-8 | 3,1e-8 | 2,7e-8 | 2,8e-8 | 3,2e-8 | 1,6e-7 |

- Alle sieben c-Werte erfuellen c^2 = 8q/(1 + 2q) auf 4 Stellen [K]. Allgemein mit den Gewichten 1:
  1/c^2 = s1/(4 w_H) + s1/(2 w_D) (Reihenschaltung von Sechseck- und Dreieckskopplung) [K, nicht hergeleitet].

### 4.2 Schwerewellen: Tetraeder-Oktaeder-Wabe (A1R1, J = 1 je Zelle) gegen V

| Variante | E / V / phys. Dim. | masselos (EW1-Regel, 13 + 23 Richtungen) | wachsend bei kleinem k | Gitter L = 8 (511 k): k mit omega^2 < 0 / A_red nicht pd | omega^2/k^2 (13 R., \|k\| = 1e-3) | Spanne 13 (max/min - 1) | Grenzwert w0 | 48 Bilder | affine Steifigkeit |
|---|---|---|---|---|---|---|---|---|---|
| **H3 (Haupt): 3 Diagonalen gemittelt** | 9 / 1 / 5 | 1 bis 2; Regel verfehlt | 3 von 13, 12 von 23 Richtungen | 6 / 6 | -0,283 bis 1,25 | nicht definiert (-5,42) | - | 2,0e-8 | 0,25 (1,1e-8) |
| R12: starres Oktaeder | 6 / 1 / 2 | 2 TT, Regel erfuellt | keine | 0 / 0 | 1,5 in allen Richtungen | **3,9e-7** | 5,4e-9 | 1,9e-9 | 0,25 (2,5e-8) |
| Z8: Oktaedermitte, 8 Tetraeder | 12 / 2 / 4 | 2 TT, Regel erfuellt | keine | 0 / 0 | 0,500 bis 1,000 | **1,000** | 1,000 | 1,4e-8 | 0,25 (1,4e-8) |
| D1z: eine Diagonale | 7 / 1 / 3 | 2 TT; Regel an 23 R. verfehlt | 2 von 23 Richtungen (Diagonalmode, omega^2 = -5,35 und -4,13) | 0 / 0 | 0,769 bis 1,500 | 0,950 | 0,950 | 0,283 (tetragonal) | 0,25 (2,8e-8) |
| D1x / D1y (nur Spanne) | 7 / 1 / 3 | - | - | - | [100]: 0,75 / 1,5 bzw. 0,80 / 1,5 | 1,000 / 0,875 | - | - | - |
| Kontrolle K (ew 'ohne', TT-ISO-1 c) | 12 / 2 / 4 | - | - | - | 0,24998568 bis 0,25001425 | (1,1e-4, nur Dispersion) | - | - | - |
| **V (Finn, gefuellt), Referenz** | 68 / 10 / 28 | - | - | - | 0,11889 bis 0,12643 | **6,3388 %** (tti = eigene Kette auf 7e-16) | - | - | - |

- K trifft TT-ISO-1 (c) genau ([0,2499857; 0,2500142]); V trifft TB0 (6,339 %) auf 1,9e-6.
- Die Regge-Steifigkeit der affinen TT-Welle ist in allen Varianten isotrop 0,25. Die ganze Anisotropie und die
  Instabilitaet sitzen in der Bewegungsenergie (wie in TT-ISO-1 fuer V).
- R12: Jede Zelle traegt jede der 6 Kantenrichtungen gleich oft, also ist die Masse die isotrope DeWitt-Form; der
  Wert 1,5 = 6 x 0,25 (zwei Tetraeder und ein Oktaeder mit doppeltem Gewicht gegen einen Tetraeder in K) [K].
- H3 in den Keilrichtungen: [100] 1/6 und 1,25; [110] 0,117 und 1,25; [111] 0,889 doppelt; [320] 0,061 und 1,25.
  Wo H3 stabil ist, ist es also extrem anisotrop (Faktor ~20).

### 4.3 Diagonalwahl und duale Zellen (beschreibend)

| Groesse | Wert [E] |
|---|---|
| Diedersumme - 2 pi je Zerlegung (D1x, D1y, D1z, H3 je Diagonale, R12, Z8) | 0 (alle) |
| Schur-Komplement ueber die Diagonale(n) gegen B von R12 (23 k) | D1x 6,0e-9; D1y 6,7e-9; D1z 6,0e-9; H3 3,7e-9 |
| [100], \|k\| = 1e-3: omega^2/k^2 | D1x 0,75 / 1,5; D1y 0,80 / 1,5; D1z 0,80 / 1,5; H3 0,167 / 1,25; R12 1,5 / 1,5 |
| *1 der Wabenkanten (Raute/Kante) | 0,25 (Raute 0,17678 = 1/(4 sqrt2)); Volumenprobe 1,000; Patchprobe 0 |
| *1 der Diagonale (D1z) | 0 (alle vier Viertel-Tetraeder haben die Oktaedermitte als Umkreismitte) |
| kappa = P(k)/L(k), 511 Gitter-k + 13 kleine k | R12 -2,0000000 (Spannweite 4,5e-9); D1z -2,0000000 (1,4e-8); H3 -2,0000000 (1,3e-8) |
| *2 der Wabendreiecke | nicht gerechnet (Codefehler, Selbstanzeige 4); vorab [M]: 2 |

## 5. Bedeutung fuer Finns Schattenformen [H]

- **Licht:** Die Sechseckflaechen der Loecher sind fuer Licht auf Finns Kanten eine Bedingung. Ohne sie steht jede
  Welle (alle Baender flach), mit ihnen laeuft Licht langwellig isotrop. Das Tempo haengt nur an ihrer Kopplung
  (c^2 = 8q/(1 + 2q)) [E, K]. Mit den Hodge-Gewichten der dualen Zellen ist c = 1 exakt. In diesem Sinn tragen die
  Schattenformen Kraefte (Bedeutung OS1 der Karte), aber das war vorab ableitbar. Zwei lokale Schwingungen je Zelle
  erreichen die Sechsecke nicht und bleiben flach.
- **Bedingte Schranke [K]:** Traegt dieses Netz das Licht, folgt wie in LICHT-FINN-NETZ-1 Abschnitt 4 aus
  |a2| = 7/192 (konservativ, Achsen) eine Tetraederkante l < etwa 1,1e-27 m. Das ist eine Kopfrechnung, keine Messung
  einer Masche.
- **Schwerewellen:** Das Oktaeder als Schattenform macht das Netz flach ohne Fehlwinkel [M]. Isotrop und stabil wird
  es nur, wenn das Oktaeder eine starre, ganze Zelle ohne innere Groesse ist (R12, ableitbar). Jede innere Groesse
  (Diagonale oder Mittelpunkt) wird ueber die Bewegungsenergie zur eigenen Dynamik: Sie zerstoert die Isotropie (Z8,
  D1z) oder macht das Netz instabil (H3, D1z). Lesart: Schattenformen muessen starre Einheiten sein, um ohne
  Abstimmung zu helfen.
- **Verstecktes Drei-Zustands-Feld:** Die Diagonalwahl ist fuer das Potential, die Hodge-Gewichte und den Takt
  unsichtbar und kostet im flachen Netz keine Energie [E]. Sie ist aber keine reine Umbenennung, denn die
  zellweise Bewegungsenergie sieht sie (andere Tempi, Instabilitaet). Das passt zu PACHNER-TAKT-1 ("B veraendert
  nichts") [P].
- **Duale Zellen:** Die Rhombendodekaeder tragen die Takt-Gewichte auf der Wabe exakt (kappa = -2 an allen k). Das
  bestaetigt HODGE-L 4.4 b an diesem Netz. Fuer Finns V ist es nicht geprueft; V ist nicht Delaunay (HODGE-L).
- **Nicht gerechnet:** Fuenfeck-Dodekaeder (Frank-Kasper, Weaire/Phelan, 120-Zelle) aus Finns Wortlaut. Die Karte
  rechnet Oktaeder, Stumpftetraeder (Sechsecke) und Rhombendodekaeder.

## 6. Selbstanzeigen

1. **Rauchtest r1:** Einheitenfehler in den dualen Massen (x8-Koordinaten nicht durch 8 geteilt). Vor dem Einfrieren
   behoben. Gelesen habe ich dabei nur die Technik (PLAN, Kopf).
2. **Lauf L3 fehlgeschlagen:** okta.bild las L['varianten'] statt L['ergebnis']['varianten'] (KeyError). Danach habe
   ich ein neues Skript code/bild_okta.py geschrieben, eingefroren (07:45:36 CEST, NACHTRAG-BILD-SHA256.txt) und
   gerechnet (L6).
   - Es zeichnet nur und liest die Ergebnisdateien unveraendert; okta.py ist unveraendert.
   - Zusaetzlich zeichnet es H3 als "instabil" statt als Balken 1e-12. Das habe ich nach Sicht auf die Ergebnisse
     geaendert. Panel (b) hat einen abgeschnittenen Titel.
3. **OS3-Kartenwortlaut-Regel ohne Gueltigkeitspruefung:** Der eingefrorene Code vergleicht die Zahl -5,42 mit 6,34 %
   und gibt "eingetroffen" aus. Bei omega^2 < 0 ist max/min - 1 kein Streumass. Ich nenne die Codeausgabe und werte
   inhaltlich "nicht entscheidbar"; die Regel habe ich nicht geaendert.
4. **toh_duale verschiebt die Wabendreiecke doppelt:** Fuer keines wurden die zwei Nachbarzellen gefunden. In
   schwer.json sind deshalb stern2 leer, summe_flaechen_doppelpyramiden_durch_V = 0 und patch_2form_abw = 1 Artefakte.
   *1, Rauten, Volumenprobe und Takt laufen ueber die Kanten und sind nicht betroffen. *2 = 2 steht nur als [M].
5. **Stichprobenabhaengigkeit:** D1z ist an 13 Richtungen und am Gitter L = 8 stabil, an 2 der 23 Zufallsrichtungen
   nicht. Stabilitaetsaussagen gelten nur fuer die gerechneten Punkte. Die 13 Richtungen liegen im kubischen Keil und
   tasten die tetragonale Variante D1z nicht voll ab.
6. **A7-Schwelle zu eng:** Die Schur-Abweichung 6e-9 entsteht an den kleinen k (B ~ k^2, Rundung ~1e-15/1e-6); die
   Gleichheit gilt bis auf Rundung. Gewertet ist sie trotzdem als "nicht eingetroffen".
7. **Volumenprobe R12:** ew setzt fuer das Oktaeder kein Volumen; der Code nimmt 1/6 fest an. Fuer R12 ist die
   Volumenprobe also nicht unabhaengig.
8. **Lesart [F]:** "J = 1 je Zelle" heisst in H3: jedes Viertel-Tetraeder mit 1/3, also das Oktaeder als Ganzes mit 1.
   Andere Lesarten (J = 1 je Viertel-Tetraeder) sind nicht gerechnet.
9. **Planerwartung teilweise falsch:** Im Plan standen fuer H3 "3 Diagonalmoden mit Luecke". Gerechnet sind die
   Diagonalmoden in manchen Richtungen negativ (omega^2 bis -3,84).
10. **Lokale Werkzeuge:** date, ls, mkdir, cp, mv, chmod, cat, sha256sum, grep, sed (Lesen; einmal sed -i an der
    Kopie okta.py.neu fuer die Einheitenkorrektur vor dem Einfrieren, danach mv), ssh, scp. jq nur zum Lesen; fuer den
    Wiederholungsvergleich hat jq Zeitfelder geloescht (del) und sortiert. Kein python, awk oder perl lokal; nichts
    nach /tmp/claude-1000 oder /dev/shm.
11. **Auf der .69 ausserhalb von kleintest.sh:** mkdir, mv (atomarer Ersatz von okta.py nach r1 und bild_okta.py),
    sha256sum, cat, ls, find, grep und sed -n (kleintest.sh lesen), uptime, date. Kein Python ausserhalb des Starters.
12. **Kopfrechnungen [K]:** die a2-Bruchformen, das Kugelmittel, die c^2-Formel aus der Abtastung, der Faktor 6 bei
    R12, die bedingte Schranke 1,1e-27 m, die Faktoren in Abschnitt 4.2. Alle anderen Zahlen stammen aus den JSON-Dateien.
13. **Kein Gegenlesen** durch einen frischen Leser in der Zeitbox; das bleibt der Leitung.

## 7. Einfach gesagt

Wir haben ausgerechnet, was die "Luecken-Formen" in Finns Tetraeder-Netz bewirken. Fuer Licht sind die
Sechseck-Flaechen der Loecher entscheidend: Ohne sie bewegt sich gar nichts, mit ihnen laeuft Licht in alle Richtungen
gleich schnell, und wie schnell, bestimmen genau diese Flaechen. Fuer Schwerewellen hilft das Oktaeder nur, wenn es als
ganzer, starrer Block zaehlt; dann laufen die Wellen in alle Richtungen exakt gleich schnell. Teilt man das Oktaeder
innen auf (wie die Karte es verlangt), wird das Netz je nach Richtung sehr ungleich schnell oder sogar instabil.
Alles ist eine Rechnung an einem gedachten Netz, keine Messung.

## 8. Dateien

- KARTE.md, PLAN.md, PLAN.md.eingefroren-20261005-074044, EINGEFROREN-SHA256.txt, NACHTRAG-BILD-SHA256.txt,
  ERGEBNIS.md, bild-okta-schatten.png
- code/: okta.py (mit .eingefroren-20261005-074044), bild_okta.py (mit .eingefroren-20261005-074536); unveraendert
  kopiert: ew.py, tp.py, nachtrag_kinetik.py, tti.py (TT-ISO-1), licht_netz.py (LICHT-FINN-NETZ-1), Pruefsummen gleich
  den eingefrorenen Originalen.
- lauf-69/: licht.json, schwer.json (L1, L2), licht-wdh.json, schwer-wdh.json (L4, L5), bild-okta-schatten.png (L6),
  Logs L1 bis L6, PRUEFSUMMEN.txt. rauch-69/: r1 bis r3 (nur Schluessel und Technik).
- Auf der .69: /home/fmh/fmhc-physics-remote/okta-schatten-1/ (code/, rauch/, lauf/, PRUEFSUMMEN-69.txt,
  EINGEFROREN-SHA256-69.txt).
