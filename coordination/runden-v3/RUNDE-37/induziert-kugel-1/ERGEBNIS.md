# INDUZIERT-KUGEL-1: Ergebnis (Runde 39, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 10:40:21 CEST. code/kugel.py geschrieben bis 10:55:59, code/auswertung_kugel.py bis 10:57:54 CEST
    (Datei-Zeitstempel). Plantext ab 11:00:55 CEST.
  - Kontrolle und Rauchlaeufe 08:56:16 bis 09:00:02 UTC, Codeprobe 08:58:22 bis 08:59:23 UTC (PLAN Abschnitt 10).
  - Eingefroren 11:02:55 CEST: PLAN.md.eingefroren-20261004-110255, Code-Kopien *.eingefroren-20261004-110255,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 09:03:07 bis 09:39:51 UTC (1 Kontrolle, 20 Messlaeufe, alle rc = 0), Auswertung 09:40:05 bis 09:40:06 UTC
    (rc 0). Text ab 11:42:36 CEST.
- Code nach dem Einfrieren unveraendert: Pruefsummen von kugel.py und auswertung_kugel.py auf der .69 vor der
  Auswertung gleich den eingefrorenen (c2a4d790..., 5b0a7126...). lauf-69/PRUEFSUMMEN.txt (.69) lokal nachgeprueft:
  44 von 44 Dateien gleich.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu3, cpu4, cpu5). Euklidisch,
  eine Schleife, freies masseloses Skalarfeld (P1). Synthetisch, keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [E] hier gerechnet, [F] Festlegung im
  Plan, [K] Kartenpunkt, [H] Hypothese.
- **Konvention:**
  - Gamma = 1/2 log det' K, K = P1-Steifigkeit aus Kantenlaengen (Gram-Formel). Gamma_M = 1/2 log det'(M^-1 K),
    M = konzentrierte Masse.
  - Kugel S^n mit N gleichverteilten Punkten, Volumen N (Dichte 1); Netz = konvexe Huelle (sphaerisches Delaunay).
    Regel C: Sehnenlaengen. Regel S: je Simplex alle Laengen mal J^(1/n) (Jacobi-Faktor der Radialprojektion am
    Schwerpunkt).
  - Referenz: flacher Torus gleicher Dichte und gleichen N (Delaunay, Koordinatenlaengen).
  - y(N) = (Gamma_Kugel - Gamma_Torus)/sqrt(N); je Saat y = beta + delta/sqrt(N); beta = Saatmittel, SE aus der
    Saatstreuung. **korr** (Urteil): Gamma auf das eigene Volumen der Regel gleich N umgerechnet (exakt,
    Homogenitaet); **roh**: ohne diese Umrechnung.
  - **Vorzeichen:** beta = 61,56 B mit Gamma ⊃ B Int sqrt(g) R. beta < 0 heisst B < 0, also positives induziertes G
    (Einsteins Vorzeichen); beta > 0 heisst negatives G (wie das Torus-c aus INDUZIERT-DICHTE-4D).

## 1. Ergebnis zuerst

1. **Auf dem exakt kovarianten S^4-Netz hat das induzierte Regge-Glied Einsteins Vorzeichen [E].** Regel S:
   **beta = -1,651 +- 0,052** (40 Saaten, -31,5 SE), also B = -0,0268 +- 0,00085 und ein positives induziertes G.
   Regel C: -1,455 +- 0,053. Jede der 40 Saaten liegt einzeln im Negativen (beta_j: Regel S -2,34 bis -1,05, Regel C
   -2,15 bis -0,86).
2. **Die 2D-Kontrolle ist sauber [E]:** beta_2D = +0,020 +- 0,029 (80 Saaten, 0,7 SE). Die Kugel-Konstruktion
   erzeugt dort kein sqrt(N)-Glied.
3. **In der Urteilsfassung (korr) haengt das Vorzeichen weder an der Laengenregel noch am Mass [E]:** Regel S liegt
   gepaart um -0,196 +- 0,002 unter Regel C. Gamma_M gibt -1,509 +- 0,055 (S) und -1,521 +- 0,054 (C). Gepaart ist
   beta(Gamma) - beta(Gamma_M) bei Regel S -0,142 +- 0,040 (3,6 SE), bei Regel C +0,066 +- 0,038 (1,7 SE). In der rohen
   Fassung (ohne Volumenumrechnung) bleibt Gamma negativ (S -1,19, C -3,14); nur Gamma_M mit Sehnen wird roh positiv
   (+0,16 +- 0,055). Die Volumenkonvention ist also der einzige gefundene Hebel, der ein Vorzeichen drehen kann.
4. **Urteile (Plan = Kartenwortlaut):** KU0 eingetroffen; KU1 nicht eingetroffen, und zwar ueber den Kartenzweig "beta < 0
   mit >= 3 SE"; KU2 nicht eingetroffen (5,7 bzw. 6,0 kombinierte SE vom Zielwert); KU3 nicht eingetroffen (beide
   negativ); KU4 eingetroffen (Regel S, 3,6 SE), ohne Vorzeichenwechsel.
5. **Bedeutung, vorab auf der Karte festgelegt:** "Das Torus-Vorzeichen kam aus nicht kovarianten Anteilen; ein
   kovariantes Netz kann Einsteins Vorzeichen geben. Ue1 waere in 4D wieder offen, mit S^4 als Bauplan [H]." Das
   kovariante B entspraeche auf dem Torus c = -0,148 (S); gemessen war dort +0,111 +- 0,045.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/auswertung_kugel.py; Werte in lauf-69/auswertung.json.
**Tor bestanden:** 2D 80 von 80 Saaten (je 3 N), 4D 40 von 40 Saaten (je 4 N); 400 Kugel- und 400 Torusnetze
gueltig, 1 200 LU ok; keine Saat ausgeschlossen oder unvollstaendig. Kontrollen KA bis KH erfuellt (Abschnitt 4).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen (korr, Gamma, sofern nicht anders gesagt) |
|---|---|---|---|---|---|
| KU0 | 2D: abs(beta_2D) <= 2 SE und <= 0,05 | 75 % | **eingetroffen** | **eingetroffen** | beta_2D = +0,020 +- 0,029 (0,70 SE, M = 80). Gamma_M: -0,010 +- 0,060 (beide Regeln). Regel S = C exakt |
| KU1 | [H] 4D, Regel S: beta > 0 mit >= 3 SE | 50 % | **nicht eingetroffen** | **nicht eingetroffen** | beta_S = -1,651 +- 0,052 (t = -31,5, M = 40); **Zweig "verfehlt durch beta < 0 mit >= 3 SE" ausgeloest**. Roh -1,190 +- 0,053; Regel C -1,455 +- 0,053 (gleicher Zweig) |
| KU2 | [H] beta(S) innerhalb 2 SE von 10,26 c_Torus = +1,14 +- 0,46 | 35 % | **nicht eingetroffen** (Ziel 1,242 +- 0,504: Abstand 2,89 = 5,7 SE_komb) | **nicht eingetroffen** (Abstand 2,79 = 6,0 SE_komb) | Auch die enge Lesart (nur SE(beta)) und roh: nicht eingetroffen. Vorzeichen entgegengesetzt |
| KU3 | [H] beta(C) und beta(S) verschiedenes Vorzeichen | 30 % | **nicht eingetroffen** (beide > 2 SE, beide negativ) | **nicht eingetroffen** | beta_C = -1,455 +- 0,053, beta_S = -1,651 +- 0,052; gepaart S - C = -0,196 +- 0,002 (Std je Saat 0,011). Roh: ebenso nicht eingetroffen |
| KU4 | [H] beta aus Gamma und Gamma_M um mehr als 2 SE verschieden | 50 % | **eingetroffen** (Regel S) | **eingetroffen** | d = beta(Gamma) - beta(Gamma_M) = -0,142 +- 0,040 (3,6 SE); beta_M = -1,509 +- 0,055, gleiches Vorzeichen. Regel C: d = +0,066 +- 0,038 (1,7 SE), nicht eingetroffen. Roh (S): eingetroffen |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - KU0 eingetroffen: kein Stopp; die 4D-Lesart ist erlaubt.
  - KU1 verfehlt durch beta < 0 mit >= 3 SE: "Das Torus-Vorzeichen kam aus nicht kovarianten Anteilen; ein kovariantes
    Netz kann Einsteins Vorzeichen geben. Ue1 waere in 4D wieder offen, mit S^4 als Bauplan [H]." Ausgeloest.
  - KU3 nicht eingetroffen: Nach der Dossier-Spalte "kann scheitern" heisst das: das Vorzeichen ist robust gegen die
    Laengenregel.
  - KU4 eingetroffen: Kartensatz "Das Mass bestimmt das Vorzeichen mit". **Einschraenkung:** Das Mass verschiebt beta
    nur um 9 % (Regel S) und dreht das Vorzeichen in der Urteilsfassung nicht; bei Regel C ist die Verschiebung nicht
    signifikant. Der Kartensatz ist damit nur im Wortlaut (> 2 SE) getroffen, nicht im Sinn (Vorzeichen). Nur in der
    rohen Fassung mit Sehnen dreht Gamma_M das Vorzeichen (Abschnitt 3.1).

**Agenten-Vorhersagen** (PLAN Abschnitt 9, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (90 %) | Tor besteht in beiden Dimensionen | **eingetroffen** (0 Ausschluesse) |
| A2 (70 %) | KU0 (Plan) eingetroffen | **eingetroffen** |
| A3 (55 %) | Punktschaetzer beta_S > 0 | **nicht eingetroffen** (-1,651) |
| A4 (60 %) | abs(beta_S - beta_C) > 2 SE (gepaart) | **eingetroffen** (111 SE) |
| A5 (65 %) | KU4 eingetroffen | **eingetroffen** |
| A6 (70 %) | Modellprobe (WLS, S, Gamma, korr) p >= 0,05 | **eingetroffen** (p = 0,29) |

## 3. Tabellen

### 3.1 beta je Regel, Groesse und Fassung [E]

(je Saat y = beta + delta/sqrt(N) ueber alle N; Mittel +- SE; WLS = Fit auf die Mittelwerte je N mit chi^2 bei 2 bzw.
1 Freiheitsgrad)

| n | Regel/Groesse/Fassung | beta | Std je Saat | delta | WLS beta (chi^2, p) |
|---|---|---|---|---|---|
| 4 | **S / Gamma / korr (Urteil)** | **-1,651 +- 0,052** | 0,331 | -1,7 +- 2,6 | -1,659 +- 0,054 (2,45; 0,29) |
| 4 | C / Gamma / korr | -1,455 +- 0,053 | 0,332 | -1,0 +- 2,6 | -1,462 +- 0,054 (2,51; 0,29) |
| 4 | S / Gamma_M / korr | -1,509 +- 0,055 | 0,346 | -0,1 +- 2,8 | -1,516 +- 0,060 (2,41; 0,30) |
| 4 | C / Gamma_M / korr | -1,521 +- 0,054 | 0,342 | -0,2 +- 2,7 | -1,528 +- 0,060 (2,41; 0,30) |
| 4 | S / Gamma / roh | -1,190 +- 0,053 | 0,332 | -0,5 +- 2,6 | -1,197 +- 0,054 (2,47; 0,29) |
| 4 | C / Gamma / roh | -3,135 +- 0,052 | 0,329 | -2,6 +- 2,6 | -3,143 +- 0,053 (2,46; 0,29) |
| 4 | S / Gamma_M / roh | -1,971 +- 0,054 | 0,343 | -1,3 +- 2,8 | -1,977 +- 0,060 (2,41; 0,30) |
| 4 | C / Gamma_M / roh | **+0,159 +- 0,055** | 0,349 | +1,4 +- 2,8 | +0,152 +- 0,061 (2,40; 0,30) |
| 2 | **C = S / Gamma (Urteil KU0)** | **+0,020 +- 0,029** | 0,261 | -4,1 +- 3,0 | +0,020 +- 0,031 (0,52; 0,47) |
| 2 | C / Gamma_M / korr | -0,010 +- 0,060 | 0,536 | -0,9 +- 6,2 | -0,008 +- 0,060 (0,96; 0,33) |

- **Volumenumrechnung (vorab je Netz exakt, keine Messung):** korr minus roh in Einheiten sqrt(N): Gamma Regel C +1,73 /
  +1,72 / +1,71 / +1,70 (N = 1000 / 2000 / 4000 / 8000), Regel S -0,50 / -0,49 / -0,48 / -0,47; Gamma_M jeweils mit
  umgekehrtem Vorzeichen. Sie verschiebt beta um +1,68 (C) und -0,46 (S). Das Vorzeichen von Gamma haengt nicht daran;
  das von Gamma_M mit Sehnen schon (roh +0,16, korr -1,52).
- **gamma-Empfindlichkeit [K3]:** b0 = 0,0388 (4D) und 0,0164 (2D). Mit gamma auf dem Kontinuumswert (-29/360 bzw.
  -1/6) verschiebt sich beta um 0,003 (beta_S = -1,648, beta_2D = +0,023).
- **Dreiparameterfit (beschreibend):** beta_S = -1,52 +- 0,36, gamma = -3,4 +- 9,2; beta_C = -1,32 +- 0,36; 2D
  beta = -0,08 +- 0,14, gamma = +6 +- 8. gamma ist erwartungsgemaess unbestimmt (PLAN S5), beta bleibt negativ.
- **Teilbereiche (beschreibend):** ohne N = 1000: beta_S = -1,593 +- 0,081, beta_C = -1,396 +- 0,081; ohne N = 8000:
  -1,624 +- 0,091 und -1,428 +- 0,092. 2D: -0,013 +- 0,056 bzw. +0,054 +- 0,054. Die kleine, stark gekruemmte Kugel
  (N = 1000, [K6]) treibt das Ergebnis nicht.

### 3.2 y je N [E]

(y = Delta Gamma/sqrt(N), Mittel +- SE ueber die Saaten, in Klammern Std je Saat)

| Datensatz | N = 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|
| 4D S, Gamma, korr | -1,688 +- 0,039 (0,247) | -1,736 +- 0,041 (0,256) | -1,637 +- 0,044 (0,279) | -1,681 +- 0,036 (0,226) |
| 4D C, Gamma, korr | -1,470 +- 0,039 (0,248) | -1,525 +- 0,040 (0,256) | -1,429 +- 0,044 (0,279) | -1,477 +- 0,036 (0,226) |
| 4D S, Gamma_M, korr | -1,503 +- 0,046 | -1,554 +- 0,048 | -1,458 +- 0,047 | -1,533 +- 0,040 |
| 4D C, Gamma, roh | -3,203 +- 0,039 | -3,241 +- 0,040 | -3,136 +- 0,044 | -3,176 +- 0,036 |

| Datensatz | N = 4000 | 16 000 | 64 000 |
|---|---|---|---|
| 2D Gamma | -0,049 +- 0,027 (0,241) | +0,003 +- 0,025 (0,225) | -0,005 +- 0,024 (0,218) |
| 2D Gamma_M (C) | -0,037 +- 0,051 | +0,021 +- 0,047 | -0,038 +- 0,049 |

- In 4D ist y ueber einen Faktor 8 in N konstant (Schwankung +-0,05): Delta Gamma waechst genau wie sqrt(N), delta ist
  mit null vertraeglich. Die Streuung je Saat ist in y-Einheiten konstant (0,23 bis 0,28), also waechst
  Std(Delta Gamma) wie sqrt(N), wie im Fit angenommen.
- Beschreibend, gemittelt: Gamma/N = 1,212 / 1,242 / 1,264 / 1,279 (Kugel, C, roh) gegen 1,313 / 1,315 / 1,313 / 1,314
  (Torus). Std je Netz 0,16 bis 0,19 sqrt(N) (Kugel), 0,15 bis 0,22 sqrt(N) (Torus). 2D: Gamma/N = 0,7053 bis 0,7063.

### 3.3 Umrechnung und Vergleich [E, M]

- **B = beta/61,56:** Regel S -0,0268 +- 0,00085, Regel C -0,0236 +- 0,00085. Induziertes G = -1/(16 pi B) = 0,74 (S) bzw.
  0,84 (C) in Einheiten des mittleren Punktabstands hoch 2 (Dichte 1), also eine Planck-Laenge von etwa 0,9 Abstaenden
  (beschreibend, von Hand).
- **Gegen den Torus:** Ein kovariantes B gaebe dort c = 6 B mal 0,9168 = -0,148 (S) bzw. -0,130 (C). Gemessen war
  +0,111 +- 0,045, also 5,7 kombinierte SE daneben (KU2, in beta-Einheiten gerechnet).
- **Gegen H-Kont (-0,58):** gleiches Vorzeichen, Betrag 2,8-mal groesser (20 SE). Das Dossier hielt dort nur das
  Vorzeichen fuer belastbar.

### 3.4 Netze [E]

| | N = 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|
| Kugelradius a | 2,483 | 2,953 | 3,511 | 4,175 |
| Simplizes je Punkt, Kugel (Torus 31,4 bis 32,2 bei N = 1000, 31,7 bis 31,8 bei 8000) | 27,46 | 28,68 | 29,56 | 30,21 |
| V_C/V_K | 0,8030 | 0,8577 | 0,8977 | 0,9268 |
| V_S/V_K | 1,0650 | 1,0445 | 1,0308 | 1,0214 |
| V_Q/V_K (Quadratur von J) | 0,99791 | 0,99901 | 0,99952 | 0,99977 |
| Regge-Summe/(1/2 Int R), Regel C | 0,9203 | 0,9434 | 0,9598 | 0,9715 |
| Laufzeit je Saat (Kugel + Torus, alle Pruefungen) | 6,2 s | 11,9 s | 25,6 s | 84 s |

- Alle Kugelnetze: Euler 2, Facetten gepaart und entgegengesetzt orientiert, keine Kappe mit Punkt innen, eigene
  Normale gegen Qhull cos >= 1 - 7e-16, kleinstes Simplexvolumen 8e-6 (4D) bzw. 2e-5 (2D, Flaeche). 2D: Gauss-Bonnet
  auf <= 1,6e-11 exakt, V_C/V_K = 0,9985 / 0,99962 / 0,99991.
- LU: kleinstes U_ii 2,8 (4D) bzw. 0,48 (2D), Zeilensumme von K <= 1,5e-15 relativ, RSS bis 1,18 GB.

## 4. Kontrollen

- **Tor (PLAN Abschnitt 5): bestanden** (Abschnitt 2).
- **Kontrolllauf lauf-69/kontrolle.json (09:03:07 bis 09:03:25 UTC, cpu3, rc 0), alle Schwellen erfuellt:**
  - KA (P1): gegen dichte4d.p1_lokal 1,6e-16, gegen induziert.lokal_K_batch 1,4e-15 relativ (n = 4); 2D gegen die
    Kotangens-Formel 1,8e-10 (Schwelle 1e-9).
  - KB (LU gegen dicht): <= 1,0e-12 absolut gegen Eigenwerte und slogdet(K + 1 1^T/N) (S^4 N = 400 beide Regeln, S^2
    N = 400, T^4 N = 600, T^2 N = 400).
  - KC (Gamma_M gegen verallgemeinerte Eigenwerte von (K, M)): <= 3,4e-13.
  - KD (eigene Gamma gegen die vorhandenen Codes): gegen dichte4d.gamma 2,3e-12, gegen zufall2d.Netz.gamma 0,0.
  - KE (Skalierung mit lambda = 1,37): Gamma, Gamma_M und die korrigierten Groessen <= 1,8e-10.
  - KG (Negativproben): Fehlt ein Punkt in der Huelle, zeigt der Kappentest 141 (S^4) bzw. 3 (S^2) Kappen mit Punkt
    innen; fehlt ein Simplex, scheitert die Facettenpaarung und Euler wird 1. Die Netzpruefungen koennen also scheitern.
  - KH: 2D Gamma Regel S gegen Regel C 0,0 (K vom Grad 0).
  - KF (beschreibend, Saat 991): V_C/V_K = 0,8057 / 0,8563 / 0,8974 (N = 1000 / 2000 / 4000), V_S/V_K = 1,0638 /
    1,0450 / 1,0309, V_Q/V_K = 0,99800 / 0,99898 / 0,99951; Regge-Verhaeltnis 0,9213 / 0,9429 / 0,9598. S^2: V_C/V_K
    0,99851 und 0,99963, V_Q/V_K 1 - 9e-7 und 1 - 6e-8, Gauss-Bonnet exakt.
- **Jacobi-Faktor (Regel S):** Die Quadratur zweiten Grades von J summiert sich auf V_K bis auf 2e-3 (N = 1000) bzw.
  2e-4 (8000), waehrend die Mittelpunktsregel 2 bis 6,5 % ueber V_K liegt; das bestaetigt die Formel J = a^4 d0/abs(x)^5.
- **Modellprobe:** chi^2 = 2,45 bei 2 Freiheitsgraden (p = 0,29), Teilbereiche und Dreiparameterfit verschieben beta
  innerhalb ihrer SE (Abschnitt 3.1).

**Latten (v3):**
- **L1 (kann scheitern):** ja. beta haette positiv sein koennen (KU1, A3: ich hatte 55 % auf positiv gesetzt), die
  Regeln haetten verschiedene Vorzeichen geben koennen (KU3), die 2D-Kontrolle haette ein sqrt(N)-Glied zeigen koennen
  (KU0), y haette mit N driften koennen (Modellprobe). Die Netztests haben Negativproben (KG).
- **L2 (Gegenprobe):** zwei Laengenregeln, zwei Masse (Gamma, Gamma_M), zwei Fassungen (korr, roh), 2D-Kontrolle,
  Teilbereiche, Dreiparameterfit, WLS gegen Saatfit; LU gegen dichte Rechnung; eigene Gamma gegen dichte4d und zufall2d.
- **L3 (Numerik):** log det' etwa 1e-15 relativ; statistisch SE(beta) 0,052 bei 40 Saaten, Std je Saat 0,33.
- **L4 (schon bekannt):** Sakharov 1967 und Visser 2002 (induzierte Gravitation; kovariante Regler mit positivem
  Gewicht geben fuer den minimal gekoppelten Skalar positives G) [L, Dossier S]; Regge-Kalkuel [L]; Poisson-Delaunay
  auf der Kugel als konvexe Huelle [L]. Eine 4D-Vorzeichenrechnung von G_ind aus einem Gitter-Skalar auf S^4 ist nach
  dem Recherchestand des Dossiers nicht belegt; ich habe nicht weiter gesucht [L?].
- **L5 (Messbezug):** keiner (4D euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Fehler 1, Zielwert von KU2:** Unter H-kov gilt beta = 11,19 c_Torus = +1,24 +- 0,50 (Faktor 0,9168 des
  Torus-Schemas), nicht 10,26 c_Torus. Ergebnis: Fuer das Urteil folgenlos; beide Lesarten liegen 5,7 bzw. 6,0
  kombinierte SE daneben, mit entgegengesetztem Vorzeichen.
- **[K2] Volumenumrechnung je Regel und fuer Gamma_M:** Ergebnis: Sie verschiebt beta um +1,68 (C) und -0,46 (S),
  bei Gamma_M umgekehrt. Mit ihr liegen alle vier Kombinationen (C, S) x (Gamma, Gamma_M) bei -1,45 bis -1,65. Ohne sie
  streuen sie von -3,14 bis +0,16. Die Urteile KU1 bis KU3 sind in beiden Fassungen gleich; KU4 auch (Regel S).
- **[K3] gamma = 0:** Verschiebung 0,003 (Abschnitt 3.1); der freie Dreiparameterfit laesst gamma unbestimmt
  (+-9) und beta negativ.
- **[K4] KU4 ist eine Netzgroesse:** d = beta(Gamma) - beta(Gamma_M) kommt aus 1/2 sum ln m_i. Es ist bei Regel S
  -0,142 +- 0,040, bei Regel C +0,066 +- 0,038; die Massenkonvention traegt also ein kleines sqrt(N)-Glied, dessen
  Vorzeichen von der Laengenregel abhaengt.
- **[K5] Regel S ist keine Regge-Geometrie:** Regge-Summe nur fuer C berichtet.
- **[K6] Kleine Kugel bei N = 1000:** Ohne N = 1000 aendert sich beta um +0,06 (innerhalb der SE).
- **[K7] Saatzahl:** 40 bzw. 80 statt 4 bis 6 (Karte). Die Std je Netz liegt bei 0,15 bis 0,22 sqrt(N) (Dossier:
  0,15), die Std von beta je Saat bei 0,33 (4D) bzw. 0,26 (2D), weil zwei Netze eingehen und der Zweiparameterfit das
  Rauschen etwa 1,4-fach verstaerkt. Mit 4 bis 6 Saaten waere SE(beta) etwa 0,15 gewesen (Dossier: 0,05 bis 0,1); mit
  40 Saaten ist sie 0,052.
- **[K8] Torus-Form:** isotrop; die Torus-Werte Gamma/N sind ueber N konstant (1,313 bis 1,315).

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:** keine Mittelwerte oder Vorzeichen der Messgroesse. Gesehen habe ich: blinde
   Standardabweichungen von y aus 2 bis 4 Rauchsaaten je N (die Rauchdateien enthalten keine Gamma-Werte), Volumen-,
   Regge-, Netz- und Zeitdaten, die Abweichungen der Kontrollen (keine Gamma-Werte) und von der Codeprobe nur die
   Struktur (jq keys).
2. **Berichtigung einer Planangabe:** PLAN Abschnitt 10 sagt, Konstruktion, Fit und Urteilsregeln haetten "vor den
   Rauchlaeufen im Code" gestanden. Fuer kugel.py stimmt das (10:55:59 CEST, Rauchstart 10:56:16 CEST). auswertung_kugel.py
   habe ich waehrend der Rauchlaeufe geschrieben (fertig 10:57:54 CEST), nachdem ich die Kontrollabweichungen gesehen
   hatte und bevor ich die blinden Streuungen (ab 10:58:10 CEST) und die Codeprobe sah.
3. **Nach den Rauchlaeufen festgelegt (vor dem Einfrieren):** Saatzahlen 40 und 80 (Karte: 4 bis 6) und die
   Laufaufteilung. Die Smoke-Streuungen bei N = 4000 und 8000 (je 2 Saaten: 0,02 und 0,04) waren, wie im Plan
   vermerkt, nicht belastbar; im Hauptlauf liegt die Streuung bei allen N bei 0,23 bis 0,28.
4. **Meine Festlegungen, die Urteile beruehren:** Urteil auf der Fassung korr ([K2]); "2 SE" in KU2 als kombinierte
   SE von beta und Zielwert gelesen; dreiwertige Planregeln fuer KU0, KU1 und KU3; KU4 mit Regel S. Alle vor dem
   Einfrieren im Code und im PLAN. Fuer die Ausgaenge dieses Laufs fallen Plan und Kartenwortlaut ueberall zusammen.
5. **Schreibtischfehler:** Faktor 0,9168 (S2', [K1]), Volumenumrechnung fuer Regel S und Gamma_M (S3', [K2]),
   Rauschschaetzung des Dossiers zu optimistisch (S7). Alle vor jeder Messung im PLAN festgehalten.
6. **Codeprobe nicht blind:** auf kleinen N (4D 600, 1200; 2D 500, 1000, 2000; Saaten 950 bis 952). Deren Werte und
   Urteile habe ich nicht gelesen; die Dateien liegen ungelesen in rauch-69/probe/.
7. **Nach dem Einfrieren:** Kein Code geaendert. Die Laufprotokolle enthalten keine Gamma-Werte (nur Gueltigkeit,
   Volumen, Regge, Zeiten); ich habe sie waehrend der Laeufe gelesen. Eine Ueberwachung (Monitor-Werkzeug) hat alle 60 s
   per ssh die Zeilen "ende" und Fehlerzeilen der Logs abgefragt. Messwerte habe ich erst in auswertung.json gesehen.
8. **ERGEBNIS-Entwurf:** Um 11:09 CEST habe ich eine Entwurfsdatei ERGEBNIS.md nur mit dem Kontrollabschnitt angelegt
   (Kontrollwerte, keine Messwerte); sie ist durch diese Fassung ersetzt.
9. **Spuren und Regeln:** cpu3, cpu4, cpu5, je Spur eine Kette nacheinander; nie mehr als drei Laeufe zugleich; jeder
   Lauf <= 6,5 min, 1 Thread, MemoryMax 4G (Starter). Auf der .69 ausserhalb des Starters nur mkdir, ls, sha256sum,
   grep, tail, cut, sed, wc, sort, date, uptime, nproc, free, systemctl --user list-units (Anzeige) und /usr/bin/jq
   (nur Struktur der Probe). Kein Python ausserhalb des Starters, keine Versionsprobe.
10. **Lokal:** kein python, awk oder perl. Benutzt: jq, sed, grep, sha256sum, date, ssh, scp, cp, mkdir, ls, cat, head,
    tail, cut, tr, sort, comm, wc, stat. Nichts geloescht.
11. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
    unter /tmp/claude-1000/.../tasks/ an (nur Rueckgabecodes und Laufmeldungen).
12. **Zeitbox:** Start 10:40:21 CEST, Text fertig 11:47:23 CEST (date), also 67 min von 150.

## 7. Bedeutung

- **Ausgeloest ist der vorab festgelegte Zweig "KU1 verfehlt durch beta < 0 mit >= 3 SE":** Das Torus-Vorzeichen kam
  aus nicht kovarianten Anteilen; ein kovariantes Netz kann Einsteins Vorzeichen geben. Ue1 ist in 4D wieder offen,
  mit S^4 als Bauplan [H].
- **Was genau gezeigt ist [E]:** Fuer zwei Laengenregeln, zwei Masse und Poisson-Delaunay-Netze auf S^4 (N = 1000 bis
  8000) ist das sqrt(N)-Glied der induzierten Wirkung gegenueber dem flachen Torus negativ, mit 27,6 bis 31,5 SE
  (Fassung korr), und folgt ueber den Faktor 8 in N genau sqrt(N). Im kovarianten Ensemble ist das das Einstein-Glied
  mit positivem G. Die 2D-Kontrolle schliesst ein sqrt(N)-Artefakt der Kugel-Konstruktion aus, soweit es auch in 2D
  wirken wuerde (Volumenfragen gibt es dort nicht, K ist skaleninvariant).
- **Was der Torus dann gemessen hat [H]:** Das Torus-c (+0,111) ist nicht das kovariante B (dieses gaebe c = -0,15). Moegliche
  Quellen, alle von derselben Ordnung h^2 k^2 wie das Signal: Delaunay in Koordinaten statt in der physikalischen Metrik
  (nur in erster Ordnung gleich, PLAN-4D [K6]), die Schwerpunktregel sp, endliches S = 0,25 bei 79 % Kippen,
  k^4-Glieder im Zwei-Punkt-Fit. Welche davon, ist nicht getrennt.
- **Grenzen:**
  - Eine Schleife, freies masseloses Skalarfeld, euklidisch, feste Punktzahl.
  - Eine Kruemmung (positiv, homogen). Das Vorzeichen von B ist aus einer Geometrie gelesen; die konforme Mode oder
    negative Kruemmung sind auf diesem Weg nicht geprueft.
  - Die Umrechnung auf "Dichte 1 bezogen auf das eigene Volumen" ist eine Konvention. Fuer Gamma aendert sie das
    Vorzeichen nicht; fuer Gamma_M mit Sehnen schon (roh +0,16).
  - Sehnen sind nicht die Geodaeten; Regel S ist keine Regge-Geometrie. Eine dritte Regel (geodaetische Laengen) ist
    nicht gerechnet. Die beiden gerechneten Regeln unterscheiden sich um 0,20 bei beta um -1,5.
  - Der Betrag (-1,65) ist eine Gittergroesse (Reglermoment); er liegt beim 2,8-Fachen der Kontinuumsschaetzung H-Kont.
- **Naechste Schritte [H]:**
  - (a) Geodaetische Laengen als dritte Regel auf denselben Netzen (billig, gleiche Laeufe).
  - (b) Die Torus-Diskrepanz eingrenzen: konforme Mode auf dem Torus mit physikalischem statt Koordinaten-Delaunay,
    oder S^4 mit einer kleinen konformen Verbiegung (dort waere das Netz kovariant und der Vergleich mit c direkt).
  - (c) Tensorform: Kugel gegen gestauchte Kugel (spurfreie Verformung), um das Verhaeltnis c0s/c2 = -2 kovariant zu
    pruefen.

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-110255, EINGEFROREN-SHA256.txt.
- code/: kugel.py (Netze, Pruefungen, Gamma, Gamma_M, Kontrollen), auswertung_kugel.py (Tor, Fits, Urteile),
  unveraendert kopiert dichte4d.py, induziert.py, zufall2d.py; je mit Kopie *.eingefroren-20261004-110255.
- rauch-69/: kontrolle.json/.log, rauch-a/-b/-c (blind) .json/.log, probe/ (Codeprobe, ungelesen), PRUEFSUMMEN.txt.
- lauf-69/: kontrolle.json/.log; messung-n4-N<N>-s<saat0>.json/.log (16 Laeufe), messung-n2-s<saat0>.json/.log (4
  Laeufe); auswertung.json (Urteile, Fits, beschreibende Tabellen), auswertung.log; PRUEFSUMMEN.txt (.69, 44 Dateien,
  lokal geprueft).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde39-induziert-kugel/ (code/, rauch/, lauf/).

## 9. Einfach gesagt

Wir wollten wissen, ob das Zittern eines Materiefelds auf einem zufaelligen Punktnetz die Raumzeit so versteift, wie es
Einsteins Schwerkraft verlangt, oder genau falsch herum, wie es unsere letzte Rechnung auf einem flachen,
verbogenen Netz nahelegte. Diesmal haben wir die Punkte auf eine vierdimensionale Kugel gestreut, wo jede Stelle
gleichberechtigt ist und das Netz keine Vorzugsrichtung hat. Dort kommt sehr deutlich das richtige, also Einsteins
Vorzeichen heraus, mit beiden Regeln fuer die Kantenlaengen und beiden Arten, die Punkte zu gewichten; die Kontrolle
in zwei Dimensionen zeigt, dass die Kugel selbst keinen Fehler einschleppt. Das falsche Vorzeichen vom letzten Mal lag
also wahrscheinlich an der Art, wie wir das flache Netz verbogen hatten, und nicht am Netz an sich; welcher Teil
davon es war, wissen wir noch nicht.
