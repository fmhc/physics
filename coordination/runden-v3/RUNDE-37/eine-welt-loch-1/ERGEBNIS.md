# EINE-WELT-LOCH-1: Ergebnis (Code-Agent fuer die Leitung, Runde 41, explorativ)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 16:02:36 CEST. Plantext ab 16:18:39 CEST, vor jeder Rechnung.
  - Rauchlauf r1 14:25:06 bis 14:26:38 UTC, r2 14:29:17 bis 14:29:40 UTC (PLAN Abschnitt 6).
  - Eingefroren 2026-10-04 16:30:31 CEST: PLAN.md.eingefroren-20261004-163031 (sha256 8db468e5...), code/ew.py
    (fa7b6417...), code/ew_auswertung.py (35cd9927...), code/tp.py unveraendert (419d7da6...); Liste in
    EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 14:30:38 bis 14:32:36 UTC, alle rc = 0; Auswertung 14:32:41 bis 14:32:42 UTC.
  - Nachtrag (beschreibend, kein Urteil) 14:36:53 bis 14:38:55 UTC. Text ab 16:40:38 CEST; Berichtigung nach dem
    Gegenlesen ab 17:09:30 CEST.
  - Alle Eingaben der Auswertung nennen ew.py fa7b6417...; die 10 Dateien in lauf-69/PRUEFSUMMEN.txt stimmen lokal
    (sha256sum -c).
- Alle Zahlen sind Gitterrechnungen auf der .69, keine Messdaten.
- **Kennzeichen:** [M] vorab ableitbar, [E] hier gerechnet, [P] im Projekt schon gerechnet, [F] Festlegung im Plan,
  [L] Literatur aus dem Gedaechtnis, [H] Hypothese oder Lesart.
- **Begriffe:** V = Standardfuellung (Lochmitte C mit 12 Speichen, Sechseckmitte H mit 6 Speichen, Kanten C-H);
  S = kantenaermere Fuellung (Lochmitte C, Achse C1-C2 durch jedes Sechseck); "ohne" = B1 von TENSOR-EIS-PYRO-1.
  "Zwangsflaeche" = Raum nach Abzug von Eichbild und skalaren Regeln (strenge Regeln, wie TE2 dort). "Punkt" = eine der
  23 Richtungen bei |k| = 1e-3 oder 2e-3 (PLAN 3).

## 1. Ergebnis zuerst

1. **Eine Welt [E]:** Mit gefuellten Loechern (V) gibt es langwellig genau zwei masselose Moden, beide reine TT-Moden
   (TT-Anteil 1,000), linear in k. Alle uebrigen 26 Moden der Zwangsflaeche haben eine grosse Luecke (kleinster Wert
   omega^2 = 3,43; die masselosen liegen bei |k| = 1e-3 bei 1,2e-7 bis 1,3e-7, bei 2e-3 bei 4,8e-7 bis 5,1e-7); die Luecke
   aendert sich zwischen beiden |k| um den Faktor 1,0000001. An keinem Punkt waechst etwas. EW1 trifft ein, EW2 und EW3
   nicht, nach Plan und nach Kartenwortlaut. Die kantenaermere Fuellung S verhaelt sich gleich (beschreibend).
2. **Warum [M, E]:** Gibt man auch den neuen Tetraedern eine Eichfreiheit an ihren Mitten (B1 sinngemaess, [F]), dann
   erzeugen die Mitten jede Eckverschiebung: Rang M_B1 = Rang M_A = 30 (V) bzw. 18 (S) an allen 811 geprueften k != 0.
   Auf dem gefuellten Netz hat B1 also dasselbe Eichbild wie die Eck-Eichung A: Es bleibt **eine** Eichgruppe, und B hat
   langwellig 3 weiche Richtungen statt 6 ohne Fuellung. Das war im Plan vorab angelegt (PLAN 1.5); EW2 war damit fast
   ausgeschlossen.
3. **Offen war und gemessen ist die Stabilitaet [E]:** Auf der Zwangsflaeche sind Bewegungs- und Lageenergie an allen
   4 095 Gitter-k (L = 16) positiv definit (V: 28, S: 16 positive Moden je k, kein Geist). B hat bei k = 0 9 (V) bzw. 5
   (S) negative Richtungen; bei |k| = 1e-4 kommt eine negative weiche dazu (Lesart: Spurmode). Zusammen sind es so viele,
   wie es Ecken und damit skalare Regeln je Zelle gibt (10 bzw. 6) [E, M]; nach den Regeln bleibt keine negative
   Richtung.
4. **Grenzen [E, Nachtrag]:** Ohne skalare Regeln haben bei kleinem k 7 (V) bzw. 6 (S) Moden omega^2 < 0. Ob die
   Zwangsflaeche auf dem Gitter L = 8 stabil ist, haengt an der Paarung von Bewegungsenergie und Reduktion: drei von
   sechs Paarungen wachsen an 8 bis 310 (V) bzw. 24 bis 64 (S) von 511 k. Die Zahl masseloser Moden (2 mit, 4 ohne Fuellung) ist an den 6
   Nachtrag-Punkten bei allen sechs Paarungen gleich (TT-Anteil dort nicht berechnet).
5. **Tempo [E]:** omega^2/k^2 = 0,119 bis 0,126 in V (zwei Polarisationszweige, in [111] entartet; Gesamtspanne 6,2 % des
   Mittelwerts), 0,211 bis 0,217 in S (2,6 %). Ohne Fuellung war es isotrop (0,25). Der Wert haengt stark an der
   Festlegung der Bewegungsenergie (Nachtrag, V: 0,005 bis 0,166, mehr als das Dreissigfache), ist also keine Vorhersage.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 16:30:31 CEST) durch code/ew_auswertung.py; Urteile und Kennzahlen in
lauf-69/auswertung.json. Klassen je Mode an 46 Punkten (23 Richtungen x |k| = 1e-3, 2e-3), PLAN Abschnitt 3.

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| EW0 | Kontrolle ohne Fuellung: Modenzahlen gleich, Tempi auf 1e-8 | 90 % | **eingetroffen** | **eingetroffen** | positive Moden je k an allen 4 095 k gleich (4 an 4 092 k, 2 an 3 k, alt wie neu); max \|Delta omega^2/k^2\| = 4,3e-10; Gegenprobe gegen tp.ops_pyro: Spektren B, A, omega^2 auf 1,5e-15 |
| EW1 | Gefuellt: genau zwei masselose TT-Moden, alle uebrigen mit Luecke | 35 % | **eingetroffen** | **eingetroffen** | an allen 46 Punkten 2 masselos, beide TT (min 0,9999999999999998), linear (Abw. <= 8,5e-8), Fit-Rest <= 2,9e-8; 26 mit Luecke, kleinster Wert 3,427 (0,227 des groessten, 15,09), Lueckenquotient 2e-3/1e-3 = 1,0000001; 0 wachsend, 0 unklar |
| EW2 | Gefuellt: vier masselose TT-Moden | 30 % | **nicht eingetroffen** | **nicht eingetroffen** | masselose TT-Moden: 2 an allen 46 Punkten |
| EW3 | Gefuellt: instabil (omega^2 < 0 bei kleinem k) | 25 % | **nicht eingetroffen** | **nicht eingetroffen** | 0 Punkte mit Re omega^2 < 0 oder komplex; kleinstes Re omega^2 = 1,19e-7 (positiv); max \|Im\|/s = 3,9e-16 |

- **Bedeutung, wie auf der Karte vorab festgelegt:** "EW1 trifft ein" ist ausgeloest: Finns Netz bekommt durch Striche
  durch die Loecher eine einzige Schwerkraft-Welt (unter der Uebertragung [F] aus PLAN 1.3). Die Karte nennt als naechste
  Frage, ob die 1/2 dann auch kurzwellig gilt. Dazu beschreibend (Abschnitt 4, ganzes Gitter): Die Spur-Umbenennungen je
  Ecke sind auf dem Gitter L = 16 meist keine Eichungen (Defekt Median 0,91, max 0,98; k -> 0 nicht gerechnet), und ganz
  ohne Zwang waechst an jedem der 4 095 Gitter-k mindestens eine Mode.
- **Vermerk zum Wortlaut "eichinvariante Moden" (Selbstanzeige 2):** Der Plan liest sie als Moden auf der
  Zwangsflaeche. Wer darunter nur die Vektoreichung versteht (ohne skalare Regel), findet bei kleinem k 7 (V) bzw. 6 (S)
  Moden mit omega^2 < 0, davon 6 (V) bzw. 5 bis 6 (S) in der Plan-Klasse "wachsend"; dann waere EW1 verfehlt und EW3
  eingetroffen.
- **Variante S (beschreibend, gleiche Regeln):** wie EW1 eingetroffen, wie EW2 und EW3 nicht. 2 masselose TT-Moden an
  allen 46 Punkten (TT 1,000, linear 4,8e-8), 14 mit Luecke (kleinster Wert 5,82 von 12,34), nichts waechst.
- **Agenten-Vorhersagen** (PLAN Abschnitt 4; gehen in kein Urteil ein):

  | Nr | Ergebnis |
  |---|---|
  | Z1 | eingetroffen: Rang M_A = Rang M_B1 = Rang [M_A, M_B1] = 30 (V) bzw. 18 (S) an 511 Gitter-k (L = 8) und 300 Zufalls-k; 27 bzw. 15 bei k = 0 |
  | Z2 | eingetroffen: B flach bei k = 0 in 33 (V) bzw. 21 (S) Richtungen; bei \|k\| = 1e-4 (nur dieses \|k\| gerechnet) in allen 23 Richtungen genau 3 Eigenwerte unter 1e-6; der betragsmaessig naechste ist negativ: -0,82 (V) bzw. -1,37 (S) |
  | Z3 | eingetroffen: physikalische Dimension 28 (V), 16 (S), 4 (ohne) an allen 4 095 Gitter-k |
  | Z4 | im ersten Teil eingetroffen (EW0), im zweiten **verfehlt**: Tempo-Abweichung 4,3e-10, nicht <= 1e-10 |
  | V1 | eingetroffen: 2 masselose Moden, TT >= 0,99 (V und S) |
  | V2 | **verfehlt** (60 % auf Wachstum gesetzt): kein Wachstum bei kleinem k, weder V noch S |
  | V3 | eingetroffen: je Zweig richtungsabhaengig (unterer Zweig 0,1189 bis 0,1214, 2,1 %; oberer 0,1214 bis 0,1264, 4,1 %); Gesamtspanne beider Zweige 6,2 % des Mittelwerts |

## 3. Schreibtisch und Zaehlung (lauf-69/zaehlung.json)

| Netz | Kanten E | Ecken V | Tetraeder | Eichrang (k != 0 / k = 0) | Rang Eichung + Skalar | physikalisch | B flach bei k = 0 | B bei k = 0: negativ / positiv |
|---|---|---|---|---|---|---|---|---|
| ohne (B1) | 12 | 2 (Mitten) | 6 Zellen (Wabe) | 6 / 0 | 8 / 2 | 4 | alle 12 [M] | (Zaehlung bedeutungslos, Selbstanzeige 7) |
| V | 68 | 10 | 58 | 30 / 27 | 40 / 36 | 28 | 33 | 9 / 26 |
| S | 40 | 6 | 34 | 18 / 15 | 24 / 20 | 16 | 21 | 5 / 14 |

- **Fuellung [F, M]:** Die Sechseckmitte ist ein Inversionszentrum, das Auf- und Ab-Kanten vertauscht; drei Diagonalen
  (jede zweite Ecke) braechen es. Deshalb V mit Sechseckmitte, S mit Achse durch sie. Beide Fuellungen haben volle
  Wuerfelsymmetrie; Volumensumme je Zelle 0,25, Diedersumme je Kante 2 pi auf <= 1,8e-15 (flach).
- **B1 sinngemaess [F]:** Eichfreiheit an den Mitten aller Tetraeder, jede Ecke folgt dem Mittel ihrer Tetraedermitten
  (P in 32 Tetraedern bei V, 20 bei S).
- **Folge [M bei k = 0, E an 811 k]:** Die B1-Eichung erzeugt dieselben Kantenaenderungen wie alle Eckverschiebungen
  (Bild M_B1 = Bild M_A; kleinster relativer Singulaerwert von M_B1 innerhalb des Rangs >= 0,10). Ihre Parameter an den
  Tetraedermitten (V 58, S 34 je Zelle) sind dafuer redundant. Ohne Fuellung (jede Ecke in genau zwei Tetraedern) waren
  es zwei getrennte Eichgruppen [P].
- **Kruemmung, Regel, Bewegung [F]:** linearisierter Regge-Kalkuel auf der Triangulierung selbst; skalare Regel je Ecke
  Summe l_e eps_e; Bewegungsenergie woertlich [F3] je Tetraeder ((n_e . n_f)^2 - 1/2, J = 1).
- **Weiche Richtungen von B auf dem eichfreien Raum** bei \|k\| = 1e-4, durch k^2 geteilt (alle 23 Richtungen genau 3):
  V [100]: -0,0189 / +0,0245 / +0,0346; S [100]: -0,0284 / +0,0466 / +0,0478; ohne: 6 Stueck (+-0,25 usw., zwei
  Kopien). Signatur (-, +, +), wie im Kontinuum fuer (Spur, TT, TT) erwartet [L]; die Zuordnung der Eigenvektoren ist
  nicht gemessen.

## 4. Modentabelle (Zwangsflaeche)

**Kleines k** (\|k\| = 1e-3, Werte omega^2; Klassen nach PLAN 3):

| Netz | masselos (omega^2/k^2 je Zweig) | TT-Anteil | Luecke: Werte omega^2 bei [100] |
|---|---|---|---|
| V | [100] 0,11889 / 0,12643; [110] 0,11889 / 0,12435; [111] 0,12140 / 0,12140; alle 23: 0,1189 bis 0,1264 | 1,000 | 3,427 (x3), 4,978 (x3), 5,189, 5,479, 7,647, 8,444, 8,486, 10,163 (x3), 10,521 (x3), 11,349 (x3), 12,000, 13,377 (x3), 15,090 (x2) |
| S | [100] 0,21130 / 0,21698; [110] 0,21275 / 0,21698; [111] 0,21509 / 0,21509; alle 23: 0,2113 bis 0,2170 | 1,000 | 5,820, 5,821, 8,624 (x3), 9,391 (x3), 10,674 (x2), 12,273, 12,3375 (x3) |
| ohne | 4 Zweige, je 0,2500 (zwei Kopien) | 1,000 | keine (4 physikalische Moden) |

- Linearitaet omega^2(2e-3)/(4 omega^2(1e-3)) - 1 <= 8,5e-8 (V), 4,8e-8 (S). Die Luecke aendert sich zwischen den beiden
  |k| um den Faktor 1,0000001.
- Die zwei TT-Zweige von V spalten in [100] und [110] (um 6,3 % bzw. 4,6 % des unteren Werts), in [111] nicht. Fuer die
  zwei TT-Polarisationen erzwingt bei kubischer Symmetrie nur die dreizaehlige Achse Entartung [M] (anders als bei
  Scherwellen eines kubischen Kristalls, die auch in [100] entartet sind [L]). Der untere Wert 0,11889 ist in [100] und
  [110] gleich.

**Ganzes Gitter** (L = 16, 4 095 k):

| Groesse | V | S | ohne (Kontrolle) |
|---|---|---|---|
| positive omega^2 je k | 28 an allen k | 16 an allen k | 4 (4 092 k), 2 (3 X-Punkte) |
| negativ / komplex / null | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 2 Moden an den 3 X-Punkten |
| A_phys, B_phys mit negativem Eigenwert | 0 k / 0 k | 0 k / 0 k | 0 k / 0 k |
| kleinstes omega^2 relativ zur Skala | 1,2e-3 | 5,4e-3 | -7,6e-16 (X-Punkte, Rundung) |
| Konditionszahl A_phys max | 6,9 | 1,9 | 1,6e15 (singulaer an den X-Punkten, Selbstanzeige 8) |
| Spur-Eichdefekt max / Median | 0,98 / 0,91 | 0,99 / 0,92 | 1,00 / 0,76 (wie TENSOR-EIS-PYRO-1) |
| ganz ohne Zwang: k mit mindestens einer wachsenden Mode | 100 % | 100 % | 98 % (wie TENSOR-EIS-PYRO-1) |

**Ohne skalare Regel** (nur Vektoreichung entfernt; \|k\| = 1e-3, alle 23 Richtungen): V 38 Moden, davon 7 mit
omega^2 < 0 (6 bei -2,3 bis -5,8 und eine schwach negative bei -3,8e-10 in [100], die ich als Spurmode deute [H]);
S 22 Moden, davon 6 negativ (5 stark, eine schwach). Die beiden positiven masselosen Moden bleiben positiv (V [100]:
0,1264 und 0,1271 statt 0,1189 und 0,1264; TT-Anteil hier nicht berechnet).

## 5. Nachtrag nach dem Einfrieren (beschreibend; code/nachtrag_kinetik.py, nachtrag-69/kinetik.json)

- **Grund:** Die Stabilitaet haengt an der Festlegung [F] der Bewegungsenergie und an der Reduktion des Werkzeugs
  (S^dagger A S). Da B_phys positiv definit ist, hat omega^2 die Vorzeichen der reduzierten Bewegungsmatrix (Sylvester).
- **Varianten:** A1 = Hauptlauf; A2 = volumengewichtet (J_t = V_Finn/V_t); A3 = Lagrange-Form je Tetraeder
  (K = Summe V_t/V_Finn Phi^-T G^-1 Phi^-1, A = K^-1; ohne Fuellung gleich A1). Reduktion R1 = S^dagger A S (Werkzeug),
  R2 = (S^dagger A^-1 S)^-1 (Zwangsbedingung auf den Lagen). Gitter L = 8 (511 k) und 6 Punkte bei kleinem k ([100],
  [110], [111], je |k| = 1e-3 und 2e-3). Die skalare Regel (Gewicht l_e) ist in allen Varianten dieselbe.

| Netz | A1-R1 (Hauptlauf) | A1-R2 | A2-R1 | A2-R2 | A3-R1 | A3-R2 |
|---|---|---|---|---|---|---|
| V: k mit Wachstum (von 511), kleinstes omega^2 | 0; 0,22 | 8; -14,6 | 0; 0,28 | 310; -774 | 142; -0,77 | 0; 0,0092 |
| S: k mit Wachstum (von 511), kleinstes omega^2 | 0; 0,39 | 64; -19,3 | 0; 0,28 | 24; -9,6 | 28; -0,16 | 0; 0,0095 |
| V: omega^2/k^2 masselos, [100] | 0,1189 / 0,1264 | 0,1264 / 0,1271 | 0,1481 / 0,1568 | 0,1568 / 0,1659 | 0,0052 / 0,0058 | 0,0052 / 0,0052 |
| V: kleinster Luecken-Wert, [100], \|k\| = 1e-3 | 3,43 | 4,20 | 4,31 | 5,65 | 0,086 | 0,229 |
| ohne: omega^2/k^2, [111] | 0,2500 | 0,2222 | 0,2500 | 0,2222 | 0,2500 | 0,2222 |

- An den 6 Punkten bei kleinem k haben **alle** Varianten genau 2 masselose Moden (ohne Fuellung 4) und keine negative
  Mode. Wo auf dem Gitter das Wachstum liegt, ist nicht gespeichert; an den 6 Punkten bei kleinem k liegt es nicht.
- Ohne Wachstum an den 511 k sind A1-R1, A2-R1 und A3-R2, in V und S. Lesart [H]: Das sind die "sortenreinen" Paarungen,
  bei denen die Form je Tetraeder und die Reduktion im selben Raum wirken (Hamilton-Form mit Reduktion der Impulse,
  Lagrange-Form mit Reduktion der Lagen).
- Auch ohne Fuellung haengt die Isotropie an R1: Mit R2 gibt dieselbe Kontrolle in [111] 0,2222 statt 0,25.

## 6. Kontrollen

- **Zellen:** D symmetrisch <= 6,4e-16; l^T D <= 1,1e-15 (Schlaefli); Diedersumme je Kante 2 pi auf <= 1,8e-15;
  Volumina 4, 5, 3 (V: Finn, Kegel, Sechsecktetraeder) bzw. 4, 5, 6 (S) mal 1/768, Summe 0,25 je Zelle.
- **Operatoren:** B hermitesch <= 4,2e-16, B M <= 2,2e-15 relativ (Regge flach eichinvariant), c M <= 4,0e-15, auf dem
  ganzen Gitter (V, S, ohne).
- **EW0:** allgemeiner Baukasten gegen TENSOR-EIS-PYRO-1 (gespeicherte Zahlen, sha256 3c86c372...) und gegen
  tp.ops_pyro (Spektren auf 1,5e-15). Spur-Eichdefekt und Anteil freien Wachstums ohne Fuellung wie dort (1,00 / 0,76;
  98 %).
- **Klassen:** an keinem der 46 Punkte "unklar"; masselose Moden <= 5,1e-7 (bei |k| = 2e-3), Luecke >= 3,43, also
  Faktor 6,8e6 Abstand (V). Konditionszahl von A_phys an den 46 Punkten hoechstens 7,0 (V) bzw. 1,9 (S); A_phys und
  B_phys dort ohne negativen Eigenwert.
- **Latten:**
  - L1 (kann scheitern): EW1 haette an Wachstum, Geist oder einer weichen Mode scheitern koennen; EW2 war nach PLAN 1.5
    fast ausgeschlossen [M].
  - L2 (Gegenprobe): EW0 gegen gespeicherte Zahlen und gegen tp.ops_pyro; zweite Fuellung S; sechs Paarungen im Nachtrag.
  - L3 (Numerik): Identitaeten 1e-16 bis 4e-15; Linearitaet 8,5e-8; keine Klasse in der Grauzone.
  - L4 (schon bekannt): Dass Regge auf einer Triangulierung langwellig ein Graviton traegt, ist Literatur [L]
    (Rocek/Williams am hyperkubischen Gitter); die Zaehlung E - 4V je Zelle (hier 28, 16, 4) passt zu Hoehns Zaehlung aus
    TETRAEDER-L [P]. Neu fuer das Projekt: die Fuellung von Finns Netz, das gleiche Eichbild von B1 und A darauf, die
    Stabilitaet der Gu/Wen-artigen Hamilton-Form auf der Zwangsflaeche und ihre Abhaengigkeit von der Paarung.
  - L5 (Messbezug): keiner.

## 7. Bedeutung [M, E, H]

- **Was die Fuellung macht:** Sie verbindet nicht nur Auf und Ab ueber neue Kanten; sie macht jede Ecke zu einem Punkt
  vieler Tetraeder. Damit erzeugen die Mitten jede Eckverschiebung, und die zwei Eichgruppen von B1 fallen auf die
  gewoehnliche Regge-Eichung zusammen [M, E]. Die Frage "eine oder zwei Welten" entscheidet die Eichstruktur; Fuellung
  und Uebertragung [F] entscheiden sie zugunsten einer Welt. Neue Kanten ohne diese Folge (Ecken nur an Finns Mitten)
  waeren nach PLAN 1.5 mit einem Regge-Potential nicht widerspruchsfrei [M, nicht gerechnet].
- **Was nicht schon vorher feststand:**
  - B hat auf dem eichfreien Raum bei kleinem k so viele negative Richtungen, wie es skalare Regeln gibt (V 10, S 6), und
    nach den Regeln bleibt an allen 4 095 Gitter-k keine [E]. Ob die Regeln genau diese Richtungen herausnehmen, ist
    nicht gemessen. Lesart [H]: Die negativen Richtungen sind die oertlichen Umskalierungen um jede Ecke, die Gitterform
    des konformen Modus.
  - Die 26 Zusatzmoden sind im Hauptlauf hart (kleinster Wert 3,43, das ist 0,23 des groessten omega^2; mit A3 im
    Nachtrag kleiner: 0,086 bzw. 0,229 absolut, in [100] bei |k| = 1e-3).
  - Die Hamilton-Form ist mit der Reduktion R1 geisterfrei; mit R2 nicht an allen k (Nachtrag).
- **Was offen bleibt:**
  - Die Stabilitaet folgt nicht aus der Bauweise allein; im Nachtrag haengt sie an der Paarung Bewegungsenergie/Reduktion.
    Welche Paarung "richtig" ist, legt erst eine Zeitrichtung fest (Lagrange gegen Hamilton, Takt) [H].
  - Die Spur-Umbenennungen je Ecke sind auf dem Gitter L = 16 meist keine Eichungen (Defekt Median 0,91; k -> 0 nicht
    gerechnet), und ganz ohne Zwang waechst an jedem Gitter-k mindestens eine Mode. [H]: In dieser Bauweise muss die 1/2
    kurzwellig wohl als Regel gefordert werden; ob sie langwellig von selbst gilt wie ohne Fuellung [P], ist offen.
  - Das Tempo und seine Anisotropie (6 %) sind Gitter- und Festlegungseigenschaften, kein Messbezug.
- Keine Aussage ueber Quanten- oder nichtlineare Effekte.

## 8. Selbstanzeigen

1. **Vorab ableitbar:** Die eine Welt folgt aus meiner Uebertragung [F] (Eichung an allen Tetraedermitten), wie in
   PLAN 1.5 vor der Rechnung festgehalten. EW2 war damit fast ausgeschlossen; gemessen wurden nur noch die Rang- und
   Kernproben, die Wirkung der skalaren Regel, die Luecke, die Stabilitaet und das Tempo.
2. **Lesart "eichinvariante Moden":** Der Plan zaehlt auf der Zwangsflaeche (wie TE2 in TENSOR-EIS-PYRO-1). Ohne
   skalare Regeln haben bei kleinem k 7 (V) bzw. 6 (S) Moden omega^2 < 0, davon 6 (V) bzw. 5 bis 6 (S) in der
   Plan-Klasse "wachsend"; die uebrige ist die schwach negative Mode (Lesart Spurmode). In dieser Lesart waere EW1
   verfehlt und EW3 eingetroffen.
3. **Festlegungen mit Gewicht:** Bewegungsenergie [F3] woertlich je Tetraeder (J = 1), skalare Regel je Ecke mit
   Gewicht l_e, Reduktion des Werkzeugs (S^dagger A S). Der Nachtrag variiert Bewegungsenergie und Reduktion, nicht das
   Gewicht der skalaren Regel. Die Zahl masseloser Moden bleibt an 6 Punkten gleich; Stabilitaet auf dem Gitter L = 8,
   Tempo und Lueckengroesse ([100], |k| = 1e-3: 3,43 bis 5,65 bei A1/A2, 0,086 bzw. 0,229 bei A3) haengen davon ab.
4. **Vor dem Einfrieren geaendert** (ohne Kenntnis von Ergebnissen mit Fuellung, PLAN 2, 3, 6): Tensor-Fit mit
   Eichspalten, Lueckenschwellen (1e-3 s und 1e4 eps^2 auf 1e-4 s und 2e3 eps^2) samt neuer Konstanzbedingung, ein
   Volumen-Tippfehler.
   - Mit den alten Schwellen waeren die Urteile gleich (kleinste Luecke 3,43 liegt ueber beiden Fassungen).
   - Auch der alte Fit aendert nichts: Die Auswertung von r1 (alte Fassungen ew.py 630f8c2b, ew_auswertung.py
     ca0945a7; dieselben 46 Punkte) gibt dieselben Urteile, TT min 0,99999 [E, erst nach dem Hauptlauf gelesen].
   - PLAN 1.2 nennt bei der Volumenberichtigung irrtuemlich r2; gemeint ist r1 (Volumina aus rauch-69/za.log).
   - Das im PLAN genannte Aenderungsfenster "ab 16:26:26" ist eine Schranke; die Aenderungen begannen nach der
     Rueckmeldung der r1-Auswertung (date 16:26:38 CEST), deren Urteile ich nicht gelesen habe.
5. **Vorab gesehen:** EW0-Zahlen und technische Identitaeten aus den Rauchlaeufen (erlaubt, PLAN 6); keine Zahl mit
   Fuellung ausser Zellzahlen, Volumina, Kantenlaengen und Identitaeten.
6. **Nachtrag** nach dem Einfrieren: eigene Datei, eingefrorenes ew.py unveraendert importiert, kein Urteil.
7. **Zaehlfehler im Code (ohne Folge fuer Urteile):** "B flach bei k = 0" fuer das Netz ohne Fuellung meldet 0 flache,
   8 negative, 4 positive Richtungen. Dort ist B(0) = 0 exakt [M] (ein Platz je Kopie, alle Dehnungen bei k = 0 sind
   gleichfoermig); die relative Schwelle wertete Rundungsrauschen. Ebenso zwei RuntimeWarnings (0/0) in der
   Kontrollzeile k = 0 dieses Netzes.
8. **Regel aus PLAN 3 nicht im Code:** "A_phys singulaer (Konditionszahl > 1e12) -> nicht entscheidbar" ist in
   ew_auswertung.py nicht umgesetzt. An den 46 Punkten von V und S ist die Konditionszahl hoechstens 7,0 bzw. 1,9. Im
   Kontrollnetz ist A_phys an den 3 X-Punkten des Gitters singulaer (1,6e15), wie in TENSOR-EIS-PYRO-1; fuer seine 46
   Punkte ist sie nicht gespeichert. "Punkt" lese ich wie in PLAN 3 definiert (Richtung, eps); wer Gitter-k darunter
   versteht, bekaeme fuer EW0 "nicht entscheidbar".
9. **Vorgaben:** Spuren cpu3 und cpu4 (vorher geprueft: keine kov-Units), hoechstens zwei ssh-Verbindungen zugleich,
   kein Python ausserhalb des Starters, lokal kein Interpreter. Skripte per scp auf .neu und mv ersetzt.
10. **Gegenlesen:** Abschnitt 11.

## 9. Einfach gesagt

In Finns Tetraeder-Netz gibt es Loecher; ohne Fuellung zerfiel es im Rechenmodell in zwei Schwerkraft-Welten, die sich
nicht spueren. Wir haben jedes Loch mit Mittelpunkten und Strichen gefuellt und die Rechnung von vorher am Computer
wiederholt. Jetzt gibt es nur noch eine Schwerkraft-Welle mit zwei Schwingungsrichtungen, alles andere ist steif. Das
war nach unserer Bauweise fast zu erwarten: Jede Ecke haengt jetzt an vielen Tetraedern, deshalb gibt es nur noch eine
Art, das Netz zu verschieben. Ob sich nichts aufschaukelt, haengt aber davon ab, wie man die Bewegung festlegt: Bei
unserer Wahl und zwei weiteren bleibt alles ruhig, bei drei anderen nicht.

## 10. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-163031, EINGEFROREN-SHA256.txt
- code/: ew.py (Baukasten, Laeufe), ew_auswertung.py (Urteile), beide mit eingefrorenen Kopien; tp.py (unveraendert
  aus TENSOR-EIS-PYRO-1); nachtrag_kinetik.py (Nachtrag).
- lauf-69/: zaehlung.json, kontrolle.json, spektrum-V.json, spektrum-S.json, auswertung.json, Logs, PRUEFSUMMEN.txt.
- rauch-69/: r1 (oberste Ebene) und r2/ (Kette mit kleinen Groessen).
- nachtrag-69/: kinetik.json, nt.log, PRUEFSUMMEN.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/runde41-eine-welt-loch/ (code/, ref/, rauch/, lauf/, nachtrag/).

## 11. Gegenlesen und Abschluss

- Frischer Leser (pruefer-opus, nur lesend; gestartet nach 16:43:56, Ergebnis gelesen nach 17:08:42 CEST, date). Er
  pruefte rund 230 Zahlen vorwaerts und die Kennzahlen rueckwaerts und fand keine falsche Urteilszuordnung, aber 7
  A-Befunde (ein fehlendes Vorzeichen, eine falsche Kristall-Analogie, fuenf Aussagen staerker als die Daten), 14
  B- und 4 C-Befunde.
- Ich habe alle uebernommen (Berichtigung ab 17:09:30 CEST): Vorzeichen Z2; Analogie Abschnitt 4; Nachtrag ohne
  TT-Anteil und ohne Variation der Regelgewichte; "genau diese Richtungen" zurueckgenommen; Wachstum ohne Zwang als
  "mindestens eine Mode je k"; Einfach gesagt mit der Abhaengigkeit von der Paarung; Zahlen je |k|; Klasse "wachsend"
  gegen Vorzeichen; L = 8 statt "ganzes Gitter"; Bezugsgroessen 6,2 % / 6,3 %; Kennzeichen; Konditionszahl und
  fehlende Plan-Regel (Selbstanzeige 8); PLAN-Verweis r1/r2; Rundung 12,3375; Groesse des Wachstums im Nachtrag.
- Kein Urteil hat sich geaendert.
- Abschluss der Datei 17:11:52 CEST (date); Zeitbox 150 min ab 16:02:36 eingehalten.
