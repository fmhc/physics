# PONZANO-1: Plan des Code-Agenten (Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 02:28:56 CEST (date). Karte gelesen ab 02:28:56,
  Hintergrund (REGEL.md 1/3/8, REGGE-4D-1 ERGEBNIS, regge_nach.py) bis 02:31 CEST. Plantext ab 02:46:30 CEST.
- Rechnungen nur auf der .69 (/home/fmh/fmhc-physics-remote/runde37-ponzano/), Start nur ueber kleintest.sh, Spur cpu.
- **Kennzeichen:** [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [M] eigene Mathematik, [F] Festlegung dieses Plans
  (von der Karte offen gelassen), [H] Hypothese, [R] im Rauchlauf gesehen (vor dem Einfrieren).
- Die Vorhersagen PO0 bis PO3 und ihre Schwellen stehen unveraendert auf der Karte; hier stehen nur Messvorschriften,
  Formen und Urteilsregeln.

## 1. Code

- code/ponzano.py: exakte 6j-Symbole, Geometrie, Teile geometrie, zeit, konvention (Rauch), po0, po1, po2, po3.
- code/auswertung.py: liest lauf/*.json, wendet Abschnitt 5 mechanisch an, schreibt lauf/auswertung.json und die Bilder.
- code/umgebung.py: Bibliotheksprobe (Rauch). Ergebnis [R]: numpy 2.4.4, scipy 1.18.0, mpmath 1.3.0, sympy 1.13.1
  mit sympy.physics.wigner.wigner_6j, matplotlib 3.11.2.

## 2. Konventionen [F]

1. **Kantenzuordnung:** {j1 j2 j3; j4 j5 j6} ist das Tetraeder ABCD mit j1 = BC, j2 = AC, j3 = AB, j4 = AD, j5 = BD,
   j6 = CD.
   - Triaden = Flaechen: (j1 j2 j3) = ABC, (j1 j5 j6) = BCD, (j4 j2 j6) = ACD, (j4 j5 j3) = ABD.
   - Gegenueberliegende Kanten (j1, j4), (j2, j5), (j3, j6) [M].
2. **Zulaessig:** jede Triade erfuellt die Dreiecksungleichung und hat ganzzahlige Summe; sonst ist das Symbol 0.
   Intern doppelte Spins J = 2j.
3. **Racah-Formel** [L], ohne Zusatzphase:
   - {6j} = Delta(j1 j2 j3) Delta(j1 j5 j6) Delta(j4 j2 j6) Delta(j4 j5 j3) sum_z (-1)^z (z+1)! / [prod_i (z-a_i)!
     prod_j (b_j-z)!]
   - a_i = Triadensummen, b_1 = j1+j2+j4+j5, b_2 = j2+j3+j5+j6, b_3 = j3+j1+j6+j4, z von max a_i bis min b_j.
   - Delta(abc)^2 = (a+b-c)!(a-b+c)!(-a+b+c)!/(a+b+c+1)!.
   - **Exakt:** Mit M = prod_i (zmax-a_i)! prod_j (b_j-zmin)! ist jeder Summand mal M eine ganze Zahl. Die Summe wird
     als ganze Zahl I aufgebaut (Rekursion von Summand zu Summand, exakt teilbar). Damit ist {6j} = (I/M) prod sqrt(Delta^2):
     - {6j}^2 rational, Vorzeichen = sign(I);
     - Zahlwert erst am Ende: mpmath, 50 Stellen (DPS = 50). Es gibt keine Ausloeschung, weil I exakt ist.
   - Probe des Vorzeichens am Sonderwert {a b c; 0 c b} = (-1)^(a+b+c)/sqrt((2b+1)(2c+1)) [L, von Hand nachgerechnet M].
4. **Ponzano-Regge** [L: Ponzano/Regge 1968, Roberts 1999]: {6j} ~ PR = cos(sum_e l_e theta_e + pi/4)/sqrt(12 pi V).
   - l_e = j_e + 1/2 sind die Kantenlaengen, V das Volumen dieses Tetraeders.
   - theta_e = pi - (innerer Diederwinkel an e), also der Aussenwinkel. Den Innenwinkel liefert die Einbettung A = 0,
     B auf der x-Achse, C in der xy-Ebene, D oben (wie newton-nachrechnung/regge_nach.py, hier in mpmath).
   - V kommt aus der Einbettung, die Gegenprobe aus der Cayley-Menger-Determinante (V^2 = CM/288).
   - **Konventionsprobe [R], vor dem Einfrieren, am gleichseitigen Tetraeder** (j = 10, 20, 40, 80; nicht Teil von PO1):
     - Aussenwinkel mit +pi/4: e = 6,8e-3 / 9,6e-4 / 3,0e-4 / 1,5e-5.
     - Die drei anderen Moeglichkeiten (Aussen -pi/4, Innen +-pi/4): e = 0,4 bis 2,0.
     - Festgelegt ist also Aussenwinkel und +pi/4, wie aus der Literatur erinnert.
5. **Biedenharn-Elliott** [L: Edmonds Gl. 6.2.12, aus dem Gedaechtnis]:
   - Identitaet: sum_x (-1)^(S+x) (2x+1) {a b x; c d p}{c d x; e f q}{e f x; b a r} = {p q r; e a d}{p q r; f b c},
     mit S = a+b+c+d+e+f+p+q+r.
   - **Geometrie [M]:** Rechts stehen die Tetraeder T1 = ABCD und T2 = ABCE auf dem gemeinsamen Dreieck ABC:
     - p = BC, q = AC, r = AB;
     - e = AD, a = BD, d = CD;
     - f = AE, b = BE, c = CE.
   - Links stehen BCDE, ACDE und ABDE um die innere Kante x = DE. Alle zwoelf Triaden habe ich gegen diese Zuordnung
     geprueft.
   - **Formprobe:** PO0 rechnet die Identitaet exakt. Faellt sie durch, pruefe ich mit sympy-Werten, ob Form oder Code
     falsch ist. Eine falsche Form macht den BE-Teil "nicht auswertbar"; nachgebessert wird nach dem Einfrieren nicht.

## 3. Formen [F] (alle vor jeder 6j-Rechnung an diesen Formen festgelegt; Geometrie im Rauchlauf geprueft [R])

- Reihenfolge b = (BC, AC, AB, AD, BD, CD); j_e = lambda b_e; l_e = lambda b_e + 1/2.
- Geometriedaten aus rauch/geometrie.json [R]. V_reg ist das Volumen des regulaeren Tetraeders mit der mittleren
  Kantenlaenge. "Flaechenrand" ist der kleinste Wert min(a+b-c)/(a+b+c) ueber die vier Flaechen.

| Form | b | Zweck | V^2(b)/V_reg^2 | Flaechenrand | V^2-Vorzeichen fuer lambda = 1..200 |
|---|---|---|---|---|---|
| A | (6, 7, 8, 7, 9, 5) | PO1, geometrisch, unsymmetrisch | +0,48 | 0,10 | konstant + |
| B | (4, 9, 7, 10, 8, 6) | PO1, geometrisch, unsymmetrisch, flacher | +0,25 | 0,10 | konstant + |
| N | (10, 6, 7, 9, 6, 5) | **PO2 (geurteilt)**: BC und AD zu lang | -1,14 | 0,048 | konstant - |
| N_rand | (6, 7, 8, 7, 9, 13) | PO2 beschreibend: Form A mit CD = 13 (groesstes ganzes CD mit gueltigen Flaechen; geometrisch bis CD ~ 12,1) | -0,33 | 0,037 | konstant - |

- **2-3-Zug** (p, q, r, e, a, d, f, b, c) = (BC, AC, AB, AD, BD, CD, AE, BE, CE).
  - K1 = (5, 5, 6, 4, 4, 4, 5, 4, 4) und K2 = (5, 6, 7, 5, 4, 4, 4, 6, 5), beide unsymmetrisch.
  - Beide sind vor der Geometrieprobe festgelegt worden (Code-Konstante KONFIG).
  - **Geometrie [R]:**
    - Beide Bipyramiden sind konvex. Die Strecke DE durchstoesst ABC innen, baryzentrisch (0,30; 0,42; 0,28) bzw.
      (0,44; 0,30; 0,27).
    - Das Defizit an DE bei x* ist hoechstens 3e-50, also eine unabhaengige Bestaetigung von x*.

| Konfig | lambda | x* | x_fold | geometrischer x-Bereich | Dreiecks-x-Bereich |
|---|---|---|---|---|---|
| K1 | 50 / 100 / 200 | 278,1 / 555,9 / 1111,4 | 52,2 / 104,9 / 210,3 | 53-300 / 105-600 / 210-1200 | 50-400 / 100-800 / 200-1600 |
| K2 | 50 / 100 / 200 | 308,4 / 616,4 / 1232,4 | 108,6 / 217,6 / 435,6 | 108-328 / 216-656 / 433-1311 | 100-450 / 200-900 / 400-1800 |

- **x* [M]:** D liegt oberhalb, E unterhalb der Ebene ABC; x* = abs(DE) - 1/2.
- **x_fold [M]:** Die zweite flache Einbettung derselben neun Laengen (E an ABC gespiegelt, gleiche Seite wie D);
  x_fold = abs(DE') - 1/2.

## 4. Schreibtisch [M/L], vor den Hauptlaeufen

- **Stationaere Phase:**
  - Jedes 6j ist nach PR ein Kosinus, also ist der Summand des 2-3-Zugs eine Summe von 8 Phasenkombinationen.
  - Mit Schlaefli (dS/dl_x = theta_x) ist die Kombination mit gleichen Vorzeichen stationaer, wenn
    pi + sum_i theta_i = 0 mod 2 pi, also wenn sum_i phi_i = 2 pi: flacher Schluss bei x*.
  - Kombinationen mit einem Minus sind stationaer, wenn phi_k = phi_i + phi_j: gefaltete Einbettung, x_fold.
  - Passend dazu zerfaellt die rechte Seite nach PR in zwei gleich grosse Terme [M]:
    - R_PR = [cos(S1 + S2 + pi/2) + cos(S1 - S2)]/(24 pi sqrt(V1 V2)), mit S_i = sum l theta von T1, T2;
    - konvex (x*): cos(S1 + S2 + pi/2);
    - gefaltet (x_fold): cos(S1 - S2).
- **Folge fuer PO3 [H, Agent]:**
  - Der Schwerpunkt nach Betrag misst nicht die Phase, sondern die Huellkurve (2x+1)/sqrt(V1 V2 V3) ueber den ganzen
    geometrischen Bereich.
  - Dessen Schwerpunkt aus der Geometrie [R, ohne 6j]:
    - K1: 181,5 / 360,0 / 719,3 gegen x* = 278 / 556 / 1111, also etwa 35 % darunter;
    - K2: 219,9 / 439,7 / 879,1 gegen x* = 308 / 616 / 1232, also etwa 29 % darunter.

## 5. Messvorschriften und Urteilsregeln (mechanisch in auswertung.py)

Urteile: "eingetroffen", "nicht eingetroffen", "nicht auswertbar" (Lauf fehlt, rc != 0, Zeitabbruch oder Kennzahl
nicht berechenbar).

### PO0 (Karte: exakt rational bzw. 1e-30 mpmath; Fremdbibliothek exakt)

- **(a) Orthogonalitaet, exakt rational:**
  - 10 Zufallssaetze (a, b, c, d) mit 2j <= 16 (Saat 37001), je mindestens zwei zulaessige f und ein x.
  - Alle Paare f <= f' werden geprueft: sum_x (2x+1)(2f+1){a b x; c d f}{a b x; c d f'} = delta_ff'.
  - Exakt heisst: Die Summe wird als (rationale Zahl) x sqrt(Produkt der Delta^2 mit ungerader Vielfachheit)
    dargestellt. Die rationalen Teile muessen gleich sein.
- **(a2) Orthogonalitaet mit mpmath bei groesseren j [F]:**
  - a, b, c, d = (AD, BD, BC, AC) von Form A bei lambda = 10, also j = 70, 90, 60, 70.
  - Vier Paare (f, f'); verlangt wird max abs(Abweichung) <= 1e-30.
- **(b) Biedenharn-Elliott, exakt wie (a):**
  - 20 Zufallssaetze, neun Spins mit 2j <= 16.
  - Angenommen wird ein Satz, wenn alle sieben Triaden der rechten Seite zulaessig sind und es mindestens zwei
    zulaessige x gibt.
  - Dazu die mpmath-Abweichung abs(L - R) / max(sum abs(Summanden), abs(R)) <= 1e-30 [F].
- **(c) Symmetrien:** alle 24 Tetraedersymmetrien an 50 zulaessigen Zufallssymbolen (2j <= 16), exakt (Vorzeichen und
  rationales Quadrat).
- **(d) Fremdbibliothek sympy.physics.wigner.wigner_6j, exakt** (Vorzeichen und rationales Quadrat):
  - alle 5^6 Tupel mit 2j <= 4, unzulaessige eingeschlossen; dort muessen beide 0 geben, wirft sympy einen Fehler,
    muss meine Seite 0 sein;
  - 200 zulaessige Zufallssymbole mit 2j <= 24;
  - die Formen A, B, N bei lambda = 5 und 10 (j bis 100).
- **(e) Sonderwert** {a b c; 0 c b}, alle zulaessigen (a, b, c) mit 2j <= 12, exakt.
- **(f) mpmath-Pfad gegen exakten Pfad:** 100 Zufallssymbole, relative Abweichung <= 1e-30.
- **Urteil:** eingetroffen genau dann, wenn (a) bis (f) alle bestanden sind. Jeder einzelne Fehler heisst
  "nicht eingetroffen", ausser im BE-Formfall aus Abschnitt 2, Punkt 5.

### PO1 (Karte: Steigung in log-log zwischen -1,3 und -0,7; e(100) < 0,02 an beiden Formen)

- e(lambda) = abs(6j - PR) / (1/sqrt(12 pi V)) mit PR nach Abschnitt 2, Punkt 4.
- **Steigung [F]:** Kleinste-Quadrate-Gerade von ln e gegen ln lambda ueber genau lambda = 5, 10, 20, 50, 100, 200,
  je Form.
- **Urteil:** eingetroffen genau dann, wenn fuer A und fuer B gilt: Steigung in [-1,3; -0,7] und e(100) < 0,02.
- **Beschreibend (nicht geurteilt), Phase:**
  - Form A, lambda = 50, j6 = CD laeuft ueber den ganzen Dreiecksbereich.
  - Gezaehlt wird im inneren geometrischen Bereich (ohne je 10 % der Breite an beiden Umkehrpunkten).
  - Vorzeichenwechsel des 6j zwischen x und x+1 gegen Vorzeichenwechsel von PR im selben Intervall: Anzahl, Treffer,
    groesster Lageunterschied der linear interpolierten Nullstellen.
  - Dazu das dichte e(lambda) fuer lambda = 1..200 (Bild).

### PO2 (Karte: ln abs(6j) sinkt linear in lambda, R^2 > 0,99 ueber lambda = 20 bis 200)

- **Form N [F]:** alle ganzen lambda = 20, 21, ..., 200 (181 Punkte), Kleinste-Quadrate-Gerade ln abs(6j) gegen lambda.
- **Urteil:** eingetroffen genau dann, wenn R^2 > 0,99 und Steigung < 0 [F: "sinkt"]. Ist ein 6j exakt 0, ist PO2
  "nicht auswertbar".
- **Beschreibend:** Form N_rand mit derselben Rechnung, dazu lambda = 1..19 im Bild.

### PO3 (Karte: Schwerpunkt nach Betrag innerhalb +-10 % von x* bei lambda >= 50)

- s(x) = (-1)^(S+x) (2x+1) {a b x; c d p}{c d x; e f q}{e f x; b a r} fuer alle zulaessigen ganzen x
  (Dreiecksbereich, auch die exponentiell kleinen Raender).
- x_c = sum x abs(s(x)) / sum abs(s(x)).
- x* wie in Abschnitt 3.
- **Urteil [F]:** eingetroffen genau dann, wenn abs(x_c - x*)/x* <= 0,10 fuer K1 und K2 bei lambda = 50, 100 und
  200 (alle sechs Faelle). Fehlt ein Lauf, ist das Urteil "nicht auswertbar", ausser die vorhandenen Faelle verfehlen
  schon; dann "nicht eingetroffen".
- **Kontrolle:** sum_x s(x) gegen das Produkt der rechten Seite; relative Abweichung <= 1e-30, sonst ist der Fall
  "nicht auswertbar".
- **Beschreibend (nicht geurteilt):**
  - Fenstersummen um x* und x_fold: Plateau +-w und cos^2-Uebergang bis +-2w, w = 3 sqrt(lambda). Sie werden mit den
    PR-Termen cos(S1+S2+pi/2)/(24 pi sqrt(V1V2)) und cos(S1-S2)/(24 pi sqrt(V1V2)) verglichen.
  - Lage des Maximums von abs(sum_x s(x) exp(-(x-c)^2/(2 lambda))).
  - Betragssumme durch abs(rechte Seite), also wie stark sich die Summanden wegheben.

## 6. Agenten-Vorhersagen (vor den Hauptlaeufen, nicht geurteilt)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | PO0 eingetroffen; die Formprobe zeigt Edmonds 6.2.12 in dieser Form | 90 % |
| A2 | PO1: e(100) < 0,02 an beiden Formen; die Steigung schwankt, weil der 1/lambda-Term selbst oszilliert. Beide Steigungen im Band | 60 % |
| A3 | PO2 eingetroffen fuer N; N_rand ebenfalls R^2 > 0,99 | 85 % / 60 % |
| A4 | PO3 nicht eingetroffen: x_c liegt nahe beim Huellkurvenschwerpunkt (29 bis 35 % unter x*), in allen sechs Faellen ausserhalb +-10 % | 85 % |
| A5 | Beschreibend: Die vorzeichenbehaftete Summe sammelt sich bei x* und bei x_fold. Die Fenstersumme um x* trifft den konvexen PR-Term auf <= 30 %, bei lambda = 200 | 50 % |

## 7. Rauchlaeufe (vor dem Einfrieren, alles hier offengelegt)

- **umgebung:** Bibliotheken wie in Abschnitt 1.
- **geometrie:** nur Geometrie, ohne 6j: Tabellen in Abschnitt 3 sowie die Huellkurvenschwerpunkte aus Abschnitt 4.
- **zeit:** Ein 6j bei lambda = 200 braucht 0,06 bis 0,09 s. Eine Zeile des 2-3-Zugs (drei 6j) bei K1, lambda = 200,
  braucht 0,15 s; es gibt 1401 Zeilen. Gerechnet, aber nicht angesehen: drei 6j-Werte (Formen A, B, N bei
  lambda = 200) und drei Zeilenwerte.
- **konvention:** gleichseitiges Tetraeder (Abschnitt 2, Punkt 4). Dabei sah ich vier 6j-Werte und dass PR dort mit
  Aussenwinkeln und +pi/4 aufgeht.
- Keine Rechnung an A, B, N, N_rand, K1 oder K2 mit 6j-Werten vor dem Einfrieren. Keine Schwelle geaendert.

## 8. Hauptlaeufe (nach dem Einfrieren, Spur cpu, nacheinander)

- po0, po1, po2: je unter 2 min.
- po3: K1 und K2 bei lambda = 50, 100 und 200. Bei 200 sind es etwa 4 min je Lauf.
- Danach auswertung.py.
- Ausgaben nach lauf/, Kopie nach RUNDE-37/ponzano-1/lauf-69/.

## 9. Bilder (lauf-69/)

- bild-spinfolge.png: 6j und PR ueber j6 (Form A, lambda = 50), mit Huellkurve +-1/sqrt(12 pi V) und dem verbotenen
  Bereich.
- bild-fehler-loglog.png: e(lambda) fuer A und B, dicht und mit den sechs geurteilten Punkten, Steigung -1 zum
  Vergleich.
- bild-abfall.png: ln abs(6j) gegen lambda fuer N (mit Ausgleichsgerade) und N_rand.
- bild-pachner-K1.png und bild-pachner-K2.png: Summand s(x) bei lambda = 100, x*, x_fold, x_c, Huelle, geglaettetes
  Profil und Teilsummen.
