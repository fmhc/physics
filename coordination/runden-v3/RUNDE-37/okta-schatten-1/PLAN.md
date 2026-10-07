# OKTA-SCHATTEN-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 46)

- **Zeiten (date; .69 in UTC, CEST = UTC + 2):** Start 2026-10-05 07:14:07 CEST. Code ab etwa 07:27 CEST, dieser Plan ab
  07:38:25 CEST. Zeitbox 150 min, also bis 09:44 CEST.
- **Rauchtests vor dem Plan** (nur Schluessel, Laufzeiten und technische Proben, Option --rauch; rauch-69/):
  - r1 licht --klein (cpu, 05:36:41 UTC, rc 0, 0,6 s): Einheitenfehler in den dualen Massen (x8 nicht durch 8 geteilt,
    Kantenlaenge 8 statt 1). Behoben (Skalierung x8 -> l), ohne Kenntnis von Ergebnissen.
  - r2 licht --klein (cpu, 05:37:10 UTC, rc 0): gelesen nur die Technik: E 12, V 4, 8 Dreiecke, 4 Sechsecke, Kantenlaenge
    1, je Kante 1 Finn-Tetraeder und 3 Stumpftetraeder, je Plakette 2 Zellen; umkreisbasierte Sterne gleich den
    Handwerten aus 1.2 (Abweichung <= 4,4e-16); Volumenproben 1,000; Patch-Proben 1,1e-16; rot grad 9,2e-16;
    Kontrolle KL (M-D an 3 Richtungen) ok.
  - r3 schwer --klein (cpu7, 05:37:22 UTC, rc 0, 4,1 s): gelesen nur die Technik der sechs Wabenvarianten (E, V, T,
    Zellarten, Volumen 0,25, Diedersumme 2 pi auf 0, D symmetrisch, B hermitesch, B M und c M <= 1,1e-15), K-Kontrolle ok,
    V-Referenz an 2 Richtungen 1,9e-6 neben 6,339 %. Keine Moden, Tempi, Spannen, Urteile.
- **Kennzeichen:** [M] eigene Mathematik (vorab, ungeprueft), [E] gerechnet, [P] Projektdatei, [S] Quelle,
  [F] Festlegung dieses Plans, [H] Hypothese.
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen (exakte Bloch-Matrizen). Keine Messdaten,
  keine Messdatenbestaetigung.

## 0. Gelesen und Rohdatenprobe (vor dem Plan)

- KARTE.md (bindend). LICHT-FINN-NETZ-1: ERGEBNIS, PLAN, code/licht_netz.py. HODGE-L DOSSIER Abschnitte 1 bis 3, 4.2,
  4.4, 5. TT-ISO-1: ERGEBNIS, PLAN, code/tti.py. EINE-WELT-LOCH-1: PLAN, code/ew.py, nachtrag_kinetik.py, tp.py
  (Ausschnitte). PACHNER-TAKT-1 ERGEBNIS Abschnitt 1 und Selbstanzeigen. EIS-1 ERGEBNIS und NETZ-C-1 KARTE (Stellen zum
  Tetraeder-Oktaeder-Netz: steifes Fachwerk, fcc-Federnetz; beides keine TT-Rechnung).
- **Altdaten-Fund [P]:** Die Tetraeder-Oktaeder-Wabe ist im Hamilton-Netz schon einmal gerechnet, als Kontrolle: ew.py
  'ohne' = zwei Kopien der Wabe (Ecken = Mitten einer Sorte, Staebe = verdoppelte Finn-Kanten, starres Oktaeder als
  Regge-Zelle), Bewegungsenergie **nur auf Finns Tetraedern**. TT-ISO-1 Kontrolle (c): alle Werte omega^2/k^2 in
  [0,2499857; 0,2500142], also isotrop. Neu an dieser Karte sind J = 1 auf **allen** Zellen (beide
  Tetraeder-Orientierungen und Oktaeder) und die Oktaeder als zerlegte Regge-Zellen. Diese Kontrolle wird hier als K
  wiederholt.
- Licht auf den Pyrochlor-Kanten mit oder ohne Sechsecke ist im Projekt nicht gerechnet (LICHT-FINN-NETZ-1 PLAN Z. 48 bis
  50 nennt nur die flachen Nullmoden [P]).

## 1. Geometrie und Operatoren [F]

### 1.1 Licht: Pyrochlor-Komplex

- Koordinaten wie ew.py (kubische Kante 1, Orte in Einheiten 1/8); Laengeneinheit fuer alle Lichtzahlen
  **l = Tetraederkante = 1** (Faktor 2 sqrt2 gegen kubisch), wie LICHT-FINN-NETZ-1.
- Je fcc-Zelle: 4 Ecken, 12 Kanten (Finn-Kanten), 8 Dreiecke (Flaechen der Auf- und Ab-Tetraeder), 4 Sechsecke
  (Mitte H_a = C1 - r_a, Ecken C1 + 2 r_b + r_d mit a nicht in {b, d}, zyklisch wie ew.sechseck_zyklus), Zellen: 2 Finn-
  Tetraeder, 2 Stumpftetraeder (Mitten C1, C2). Euler 4 - 12 + 12 - 4 = 0. Jede Sechseckkante gehoert zu einem
  anderen Finn-Tetraeder.
- Maxwell: A auf den Kanten, d0 (Ecken -> Kanten), C (Plaketten x Kanten, Bloch-Phasen der Gitterverschiebung),
  K = C^+ W C mit W = *2 je Plakette, *1 = s1 fuer alle Kanten (alle Kanten gleichwertig). Gauss-Gesetz: Komplement von
  Bild d0(k) (orthogonal, weil *1 proportional zur Einheit). omega^2 = Eigenwerte von K auf diesem Komplement / s1.
  8 physikalische Zweige je k != 0.

### 1.2 Plaketten-Kopplung der Sechsecke [M, im Rauchtest r2 technisch bestaetigt]

- Umkreisbasierte Hodge-Sterne (DEC), aus den Zellmitten:
  - Duale Kante eines Dreiecks: Finn-Mitte (Abstand sqrt6/12) bis Stumpf-Mitte (5 sqrt6/12), zusammen sqrt6/2.
    Duale Kante eines Sechsecks: zwei Stumpf-Mitten (je sqrt6/4), zusammen sqrt6/2.
  - *2(Dreieck) = (sqrt6/2)/(sqrt3/4) = 2 sqrt2; *2(Sechseck) = (sqrt6/2)/(3 sqrt3/2) = sqrt2/3; **w_H/w_D = 1/6**.
  - Duale Flaeche einer Kante: Viereck aus 1 Finn-Mitte und 3 Stumpf-Mitten, Flaeche sqrt2; *1 = sqrt2.
  - Proben: Summe |e||*e|/3 = Summe |f||*f|/3 = Zellvolumen 4 sqrt2; die Gleichfelder sind *1- bzw. *2-koharmonisch.
- **Varianten:** ohne (nur Dreiecke, DEC-Gewicht), **dec (Haupt)**, eins (alle Gewichte 1, beschreibend), ohne_eins,
  Abtastung w_H/w_D in {0; 1e-3; 1e-2; 0,1; 1/6; 1; 10; 100} bei DEC-w_D und DEC-s1 (beschreibend).

### 1.3 Schwerewellen: Tetraeder-Oktaeder-Wabe

- Eine Kopie wie ew 'ohne', Kopie 1: Ecken auf fcc (Ab-Mitten, D0 = (2,2,2)/8), 6 Kanten je Zelle der Laenge sqrt2/2
  (kubisch; = 2 Finn-Kanten). Zellen je Ecke: tet_auf (Mitte 0), tet_ab (Mitte C2), Oktaeder (Mitte C1), alle regulaer.
  Je Kante 2 Tetraeder (je 70,53 Grad) und 2 Oktaeder (je 109,47 Grad): 360 Grad, flach ohne Fehlwinkel [M, Karte].
- Hamilton-Netz **unveraendert ew.py** (EINE-WELT-LOCH-1 1.3): a_e = delta l / l, B = -l d eps/d l l (Regge, komplexer
  Schritt), Eichung = Eckverschiebung M, skalare Regel c_v = -B w_v, Bewegungsenergie A1 je Zelle
  A0 = (n_e . n_f)^2 - 1/2 mit **J = 1 je Zelle**, Reduktion R1 (A_red = S^+ A S, S = Komplement von Bild [M, c]).
  Paarung A1R1 wie der Hauptlauf von TT-ISO-1 (dort V: 6,34 %).
- **Oktaeder als Regge-Zellen (vorab festgelegt):**
  - **H3 (Haupt) = "in 4 Tetraeder zerlegt, gemittelt ueber alle 3 Diagonalen":** je Achse x, y, z die vier
    Viertel-Tetraeder (N, S, E_m, E_m+1) um die Diagonale N-S; alle 12 mit Gewicht 1/3 in B und A (also das Oktaeder
    als Ganzes mit J = 1). Die drei Diagonalen sind eigene Kantenvariablen (Laenge 1 kubisch). B = (1/3) Summe_d B_d,
    jede Zerlegung ist flach, also B M = 0. Volle Wuerfelsymmetrie (Fm-3m).
  - R12 (beschreibend): starres Oktaeder als eine Zelle (12 Kanten, Diederwinkel aus den Kantenlaengen, ew.okt),
    Bewegungsenergie A0 ueber seine 12 Kanten, J = 1.
  - Z8 (beschreibend, "symmetrische Zerlegung"): Oktaedermitte als neue Ecke, 8 Tetraeder (Mitte + Flaeche).
  - D1x, D1y, D1z (beschreibend): nur eine Diagonale in jedem Oktaeder (tetragonal), fuer Teil 3a.
  - Eine wuerfelsymmetrische Zerlegung in 4 Tetraeder gibt es nicht (jede Diagonale zeichnet eine Achse aus) [M];
    deshalb ist "symmetrisch" hier entweder H3 (Mittel) oder Z8 (8 Tetraeder). Haupt ist H3, weil die Karte
    ausdruecklich 4 Tetraeder nennt.
- Zaehlung je Zelle [M]:

| Variante | Kanten E | Ecken V | Eichung 3V | Regel V | physikalisch E - 4V | davon langwellig masselos |
|---|---|---|---|---|---|---|
| H3 | 9 (6 + 3 Diagonalen) | 1 | 3 | 1 | 5 | 2 (TT) + 3 Diagonalmoden mit Luecke |
| R12 | 6 | 1 | 3 | 1 | 2 | 2 (TT), keine weiteren |
| Z8 | 12 (6 + 6 Speichen) | 2 | 6 | 2 | 4 | 2 (TT) + 2 mit Luecke |
| D1z | 7 | 1 | 3 | 1 | 3 | 2 (TT) + 1 mit Luecke |
| K (ew 'ohne', 2 Kopien) | 12 | 2 | 6 | 2 | 4 | 4 (2 je Kopie) |

## 2. Ableitbarkeitsprobe (vor jeder Rechnung)

### 2.1 Licht [M]

- **Ohne Sechsecke ist alles flach.** Jede Kante und jedes Dreieck gehoert genau einem Finn-Tetraeder (eckenteilend).
  C ist also blockdiagonal je Tetraeder; die k-Abhaengigkeit ist eine reine Phase. Je Tetraeder ist C^+ C = 4 P_c mit
  P_c Projektor auf den 3-dim Wirbelraum (d1 d1^T = 4 I - J auf den 4 Flaechen). Je k: 6 Nullwerte, davon 4 Eichung,
  also **2 flache Nullbaender**, und **6 flache Baender bei omega^2 = 4 w_D / s1** (DEC: 8; Einheitsgewichte: 4).
  Das Licht laeuft nicht (Gruppentempo 0).
  - **OS0 nach Plan (2 flache Nullbaender) ist damit vorab ableitbar eingetroffen; nach Kartenwortlaut ("2 flache
    Baender", alle gezaehlt) vorab ableitbar nicht eingetroffen (8).** Gerechnet wird es als Kontrolle.
- **Mit Sechsecken verschwinden die Nullbaender.** Der Komplex (4, 12, 12, 4) ist eine Zerlegung des 3-Torus; mit einem
  nichttrivialen Bloch-Charakter (k != 0) ist er exakt, also Kern C(k) = Bild d0(k): keine physikalische Nullmode
  [M, HODGE-L Abschn. 5].
- **Aber zwei flache Baender bleiben.** C_H(k) hat nur 4 Zeilen. Auf dem 6-dim Wirbelraum V_c der beiden Tetraeder hat
  es also einen Kern der Dimension >= 2. Fuer v darin gilt K v = 4 w_D v + w_H C_H^+ C_H v = 4 w_D v, und v ist
  senkrecht zum Eichbild. **Also >= 2 flache Baender bei genau omega^2 = 4 w_D / s1, fuer jedes w_H** (DEC: 8).
  - **OS1 nach Kartenwortlaut (alle flachen Baender verschwinden) ist in Teil (i) vorab ableitbar verfehlt.**
- **Langwelliges Tempo:** isotrop und fuer beide Polarisationen gleich, wegen Wuerfelsymmetrie und Eichinvarianz
  (Tensoren 2. Stufe). **OS1 nach Plan ist damit vorab ableitbar eingetroffen.** Geprueft wird es am Code bei k != 0:
  26 Richtungen und 48 Bilder bei k = 0,2/l.
- **DEC-Tempo c = 1** [M]: Mit den umkreisbasierten Sternen sind die Gleichfelder koharmonisch und die Patch-Proben
  exakt, also eps_eff = mu_eff = 1. Mit Einheitsgewichten ist eps_eff = 1/sqrt2, mu_eff nicht vorab (Relaxation an den
  Sechsecken); gemessen.
- **Nicht ableitbar:** a2- und a4-Muster, Doppelbrechung bei k^2, Tempo mit Einheitsgewichten, ob mehr als 2 flache
  Baender bleiben.

### 2.2 Schwerewellen [M]

- **Zahl der masselosen Moden** folgt aus der Zaehlung (Tabelle 1.3): Bei k = 0 sind die flachen Richtungen von B die 6
  gleichfoermigen Dehnungen und das Eichbild. Rang B(0) = E - 6 - (3V - 3): H3 3, R12 0, Z8 3, D1z 1, alle positiv
  (Diagonale laenger heisst Diedersumme > 2 pi). Also langwellig genau 2 masselose Moden (TT), sofern die Raenge
  halten und A auf dem physikalischen Raum regulaer ist. **Das "genau zwei" in OS2 ist vorab ableitbar; die
  Stabilitaet (Vorzeichen von A_red) nicht.**
- **R12 ist langwellig isotrop** [M]: Jede Zelle (beide Tetraeder, Oktaeder) enthaelt jede der 6 Kantenrichtungen
  gleich oft (Oktaeder je 2). A(k -> 0) ist damit die isotrope DeWitt-Form auf dem Tensor E = Summe E_e n_e n_e (die
  6 Kanten sind eine Bijektion auf Sym2). Die Regge-Steifigkeit der affinen TT-Welle ist isotrop [P TT-ISO-1], Eich-
  und Regelrichtungen sind isotrop. Also ist die TT-Spanne von R12 nur Dispersion (erwartet <= 1e-4). Ebenso die
  Kontrolle K (jede Kante in genau einem kinetischen Tetraeder) [M, P].
- **H3 und Z8:** Die Diagonalen bzw. Speichen sind steife Zusatzgroessen. Langwellig folgen sie adiabatisch; die
  effektive TT-Masse ist dann eine Form auf Sym2 mit Wuerfel-, nicht Drehsymmetrie (m_E != m_T generisch). Die Spanne
  ist also generisch > 0, ihre Groesse ist nicht vorab ableitbar. **OS3 ist nicht ableitbar.**
- **D1z** ist tetragonal (D4h), also sicher anisotrop [M]; die Groesse ist offen.

### 2.3 Diagonalwahl und duale Zellen [M]

- Jede der drei Diagonalwahlen gibt eine flache Triangulierung (Diedersumme 2 pi an jeder Kante, auch an der
  Diagonale: 4 x 90 Grad). Die Regge-Wirkung ist in allen drei Zustaenden null.
- Quadratisch: Wird die Diagonale ueber ihre eigene Gleichung (Fehlwinkel 0) eliminiert, ist die Wirkung die des
  starren Oktaeders. **Schur-Komplement von B ueber die Diagonale = B von R12, fuer jede Wahl** (Argument: auf der
  Loesung ist d S/d l_d = eps_d = 0). Fuer das Potential ist der Diagonalwechsel also kostenlos. Gerechnet wird die
  Abweichung am Code.
- Die 6 Oktaederecken liegen auf einer Kugel (Delaunay-entartet). Alle vier Viertel-Tetraeder haben die Oktaedermitte
  als Umkreismitte; **der umkreisbasierte Stern *1 der Diagonale ist 0**. Auch der Takt-Operator (Glickenstein-
  Laplace mit *1, HODGE-L 4.4 b) sieht die Diagonale nicht.
- Sichtbar werden kann die Wahl nur ueber die zellweise Bewegungsenergie A1: die Viertel-Tetraeder einer Diagonale
  haben andere Kantenrichtungen als die einer anderen. Gemessen: TT-Tempi von D1x, D1y, D1z gegen H3 und R12.
- **Duale Zellen der Wabe = Rhombendodekaeder** (Voronoi-Zellen von fcc) [L, M]. Umkreisbasierte Hodge-Gewichte
  (kubisch, a = 1): *0 = Volumen des Rhombendodekaeders = 1/4; duale Flaeche einer Kante = Raute mit Diagonalen
  1/sqrt2 und 1/2, Flaeche 1/(4 sqrt2), *1 = 1/4; duale Kante eines Dreiecks = Tetraedermitte bis Oktaedermitte
  sqrt3/4, *2 = 2. Beschreibend gerechnet: diese Sterne aus der Geometrie und das Verhaeltnis
  P(k) = W^+ B W zu L(k) = Summe_e *1_e |1 - e^{i k.T_e}|^2 (W = Eckskalierung, a_e = (f_i + f_j)/2) an 511 k und
  kleinem k. Ist es konstant, tragen die Rhombendodekaeder die Takt-Gewichte [H, HODGE-L 4.4 b].

## 3. Messgroessen [F]

- **Licht (Varianten ohne, dec, eins, ohne_eins):** omega^2 an 789 k (Gitter L = 8 ohne k = 0, 200 Zufalls-k Saat 46,
  26 Richtungen x |k| in {1e-3, 1e-2, 1e-1}/l). Je k Zahl der Nullmoden (|omega^2| <= 1e-10 max|omega^2|). **Flache
  Baender kreuzungsfest gezaehlt:** ein Wert, der an allen k mit fester Vielfachheit vorkommt (Toleranz 1e-9 S,
  S = groesstes |omega^2|); Wert, Vielfachheit, null oder nicht. Bandpfad Gamma-X-W-L-Gamma-K fuer das Bild.
- **Dispersion (dec, eins):** die zwei untersten Zweige (Photonen) mit licht_netz.operator_auswerten (unveraendert):
  26 Richtungen, Fenster W0 [0,01; 0,30]/l (60 Punkte, Grad 8), Proben Wk, Wg, Kugelmittel (200 Fibonacci-Richtungen).
  Tempo c, a1, a2, a4 je Richtung und Zweig; Spannweiten; Doppelbrechung = groesste Differenz der Zweige. Dazu 48 Bilder
  einer allgemeinen Richtung bei k = 0,2/l. Abtastung: Nullmoden, flache Baender, Tempo bei |k| = 1e-3/l (13
  Richtungen) je w_H/w_D.
- **Kontrolle KL:** Maxwell M-D von LICHT-FINN-NETZ-1 mit dem kopierten Fit: a2 = -1/12, -5/48, -1/9 auf <= 1e-6.
- **Schwerewellen (H3, R12, Z8, D1z; D1x, D1y nur Spanne):** an 13 Richtungen (TT-ISO-1) und 23 Richtungen (ew) x |k| =
  1e-3, 2e-3:
  - Z-Verfahren wie tti.auswerten (B_red = L L^+, 1/omega^2 = groesste |Eigenwerte| von L^-1 A_red^-1 L^-+): omega^2/k^2
    der zwei masselosen Zweige, Luecke |ev3|/|ev2|, negative Moden.
  - Direkt wie ew.spektrum_punkt: alle omega^2 = eig(A_red B_red), Klassen nach EINE-WELT-LOCH-1 PLAN 3 (wachsend,
    masselos, Luecke, unklar), TT-Anteil je masseloser Mode (ew.tensor_fit, tp.tt_anteil).
  - **Spanne = max/min - 1 ueber 52 Werte (13 Richtungen x 2 Zweige x 2 |k|), wie TT-ISO-1.** Beschreibend: Spanne je |k|,
    an 23 Richtungen, Richardson-Grenzwert w0 = (4 w(1e-3) - w(2e-3))/3.
  - Stabilitaet am Gitter L = 8 (511 k): k mit negativem oder komplexem omega^2, B_red bzw. A_red nicht positiv definit.
  - 48 Bilder einer allgemeinen Richtung (|k| = 1e-3); affine Steifigkeit a^+ B a/k^2 auf TT (beschreibend).
- **Kontrollen:** K = ew 'ohne' wie TT-ISO-1 (c): alle omega^2/k^2 an 13 x 2 Punkten, |w - 0,25| <= 2,5e-4.
  V = Finns gefuelltes Netz, A1R1, J = 1, 13 Richtungen: Spanne ueber tti.w2_klein (unveraendert) und ueber die eigene
  Kette; erwartet 6,339 % (TT-ISO-1 TB0).
- **Teil 3 (beschreibend):** Diedersummen je Zerlegung; Schur-Abweichung D1x/D1y/D1z/H3 gegen R12 an 23 k; Spanne und
  [100]-Werte von D1x/D1y/D1z/H3/R12; umkreisbasierte Sterne der Wabe (R12, D1z); P(k)/L(k) fuer R12, D1z, H3.

## 4. Urteilsregeln (mechanisch in code/okta.py, Funktionen urteile_licht, urteile_schwer)

| Nr | Karte | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| OS0 | ohne Sechsecke 2 flache Baender je k (85 %) | **eingetroffen**, wenn an allen 789 k genau 2 Nullmoden und diese ein flaches Nullband der Vielfachheit 2 bilden (Variante ohne, DEC-Gewicht). Sonst nicht eingetroffen. | eingetroffen, wenn die Zahl aller flachen Baender (null oder nicht) genau 2 ist. Vorab: 8, also nicht eingetroffen [M]. |
| OS1 | [H] mit Sechsecken verschwinden die flachen Baender bei allen k != 0, langwelliges Tempo isotrop (70 %) | Variante dec. (i) keine Nullmode an den 789 k und kein flaches Nullband; (ii) Spannweite rel. von c ueber 26 Richtungen < 1e-6 fuer beide Photonzweige (W0). Beide: eingetroffen; eines: geteilt; keines: nicht eingetroffen. | wie Plan, aber (i) verlangt, dass gar kein flaches Band bleibt (auch nicht bei omega^2 != 0) und keine Nullmode. Vorab: (i) verfehlt [M]. |
| OS2 | [H] Wabe traegt genau zwei masselose TT-Moden und ist bei kleinem k stabil (65 %) | Variante H3, A1R1, J = 1: an allen 26 Punkten (13 Richtungen) und allen 46 Punkten (23 Richtungen) gilt die EW1-Regel: keine Mode wachsend oder unklar; genau 2 masselos, beide positiv, TT-Anteil >= 0,99, linear (omega^2(2e-3)/(4 omega^2(1e-3)) - 1 <= 0,01); alle uebrigen in der Klasse Luecke, Luecke konstant (Quotient in [0,5; 2]). Dann eingetroffen, sonst nicht. | wie Plan (die Wabe der Karte ist H3). Beschreibend dieselbe Regel fuer R12, Z8, D1z. |
| OS3 | [H] TT-Spanne ohne Abstimmung unter der von V (6,34 %) (50 %) | Spanne(H3) < Spanne(V), beide in diesem Lauf gerechnet (V ueber tti.w2_klein). H3 muss Z-gueltig sein (an allen 26 Punkten B_red positiv definit, beide masselos positiv, keine negative Mode, Luecke < 1e-2), sonst nicht entscheidbar. | Spanne(H3) < 6,34 % (Kartenwert). |

- Beschreibend, ohne Urteil: eins, ohne_eins, Abtastung, Wk/Wg, Kugelmittel, R12, Z8, D1x/y/z, K, Teil 3, Richardson,
  Spannen an 23 Richtungen und je |k|, Stabilitaet am Gitter.
- Bricht ein Lauf ab, ist das betroffene Urteil "nicht entscheidbar".

## 5. Agenten-Vorhersagen (vor jeder Rechnung; gehen in kein Kartenurteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | DEC-Licht: c = 1 auf 1e-6, beide Polarisationen gleich | 85 % |
| A2 | Mit Sechsecken genau 2 flache Baender (bei omega^2 = 8, DEC), keine Nullmode | 75 % |
| A3 | DEC-Licht: a2 < 0 in allen 26 Richtungen, Spannweite rel. > 10 % | 60 % |
| A4 | H3: genau 2 masselose TT, stabil bei kleinem k (EW1-Regel) | 60 % |
| A5 | H3: Spanne < 6,34 % | 55 % |
| A6 | R12: Spanne < 1e-4 (nur Dispersion) | 80 % |
| A7 | Schur D1x/y/z und H3 gegen R12 <= 1e-10 relativ | 85 % |
| A8 | P(k)/L(k) fuer R12 an allen k konstant auf 1e-8 | 50 % |

## 6. Laeufe (nach dem Einfrieren; .69, kleintest.sh, je <= 600 s, 1 Thread; Logs mit absolutem Pfad)

- Arbeitsordner /home/fmh/fmhc-physics-remote/okta-schatten-1/ (code/, rauch/, lauf/). Code dort gleich dem lokalen
  (sha256).
- L1 (cpu): `okta.py licht --out lauf/licht.json` (geschaetzt <= 60 s).
- L2 (cpu7): `okta.py schwer --out lauf/schwer.json` (geschaetzt <= 120 s).
- L3 (cpu): `okta.py bild --licht lauf/licht.json --schwer lauf/schwer.json --png lauf/bild-okta-schatten.png`.
- L4 (cpu7) und L5 (cpu): Wiederholungen von L1 und L2 (lauf/licht-wdh.json, lauf/schwer-wdh.json); Vergleich mit jq -S
  ohne info, laufzeit_s, zeiten, maxrss_MB, ende_utc.
- Faellt ein Lauf mit Fehler aus, wird das vermerkt; eine Codeaenderung danach waere eine Selbstanzeige mit neuer
  eingefrorener Fassung.

## 7. Einfrieren

- PLAN.md und code/okta.py als Kopien *.eingefroren-<Zeit>; sha256 aller Code-Dateien (okta.py, ew.py, tp.py,
  licht_netz.py, tti.py, nachtrag_kinetik.py) in EINGEFROREN-SHA256.txt; auf der .69 dieselben Pruefsummen. Danach keine
  Aenderung an Plan, Code oder Regeln.
