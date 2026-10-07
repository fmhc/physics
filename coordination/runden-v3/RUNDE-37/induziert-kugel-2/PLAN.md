# INDUZIERT-KUGEL-2: Plan (Code-Agent, Runde 40)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 12:11:57 CEST (date). Code (code/kugel2.py,
  code/auswertung_kugel2.py) geschrieben bis etwa 12:28 CEST, Kontrolle und Rauchlaeufe ab 10:29:04 UTC (.69,
  = 12:29:04 CEST), Plantext ab 12:31:18 CEST (date).
- **Grundlage:** KARTE.md (K2-0 bis K2-3, Wahrscheinlichkeiten und Bedeutungssaetze unveraendert, Abschnitt 6);
  RUNDE-37/induziert-kugel-1/ (KARTE, PLAN, ERGEBNIS, code/kugel.py, lauf-69/auswertung.json);
  RUNDE-37/kugel-gegenlesen/GEGENLESEN.md (Frage 2, Frage 8, Ableitbarkeitsprobe).
- **Code:** code/kugel2.py und code/auswertung_kugel2.py (neu). Unveraendert kopiert und importiert (sha256 gleich den
  eingefrorenen Fassungen von INDUZIERT-KUGEL-1): kugel.py (c2a4d790...), auswertung_kugel.py (5b0a7126...),
  dichte4d.py (2881048e...), induziert.py (b3867eac...), zufall2d.py (37a0fe8f...).
- **Kennzeichen:** [M] eigene Mathematik, [ES] eigener Schluss (grob), [F] Festlegung dieses Plans, [K] Kartenpunkt
  (vor dem Einfrieren offengelegt), [H] Hypothese, [E] im Rauchlauf oder in der Kontrolle gerechnet (blind: keine
  Gamma-Werte, nur Netz-, Volumen-, Einbettungs- und Zeitdaten).

## 1. Schreibtisch (vor jeder Messung)

| Nr | Punkt | Befund |
|---|---|---|
| S1 | Regel G: Laenge a arccos(x_i.x_j/a^2) | Gleich 2a arcsin(c/(2a)) mit der Sehne c, denn c^2 = 2a^2(1 - cos t) = 4a^2 sin^2(t/2) [M]. Gerechnet wird ueber arcsin (stabil fuer kleine Winkel), arccos als Kontrolle KG1. d^2 = c^2 + c^4/(12 a^2) + O(c^6/a^4) [M]. Gemeinsame Kanten haben in allen Simplizes dieselbe Laenge (Regge-Geometrie), aber die Form jedes Simplex aendert sich (lange Kanten werden staerker gestreckt) |
| S2 | Einbettbarkeit von G | **Vorab [M, erste Ordnung]: G treibt flache Simplizes (Splitter) aus dem einbettbaren Bereich.** Ein entartetes Simplex aus k+1 Kugelpunkten in einer (k-1)-Ebene liegt auf einer kleinen Sphaere; mit der affinen Abhaengigkeit lambda (Summe lambda_i = 0, Summe lambda_i x_i = 0, auf Laenge 1 normiert) aendert die geodaetische Umrechnung den kleinsten Gram-Eigenwert um delta = -1/2 Summe_ij lambda_i lambda_j c_ij^4/(12 a^2) = -norm(Summe_i lambda_i x_i x_i^T)^2/(6 a^2) <= 0 (x_i vom Mittelpunkt der kleinen Sphaere aus). Beispiel Quadrat auf einem Kreis vom Radius r: delta = -0,44 r^4/a^2; ein Tetraeder dieser Form mit Dicke t wird nicht einbettbar, wenn etwa t < 0,58 r^2/a (Ptolemaeus-Ungleichung verletzt). Dreiecke verletzen nie (sphaerische Dreiecksungleichung). Erwartung: Verletzungen in Splittern; ihr Anteil faellt wie (h/a)^2, also wie N^(-1/2), ihre Zahl je Netz waechst wie N^(1/2) [ES]. Die Konstante haengt an der Splitterstatistik und wird im Rauchlauf gezaehlt |
| S3 | Regel Q: was sie ist | **[M]:** Die Zentralprojektion bildet das flache Sehnensimplex auf das geodaetische Simplex mit denselben Ecken ab, also ist Int_T J dV dessen Riemann-Volumen, und die Summe ueber alle Simplizes ist exakt V_K. Die Ecken liegen alle im Winkelabstand theta = arccos(d0/a) vom sphaerischen Umkreismittelpunkt p = a n_T; Riemann-Normalkoordinaten an p bilden sie auf a theta u_i ab, also auf eine aehnliche Kopie des Sehnensimplex (Faktor a theta/r). Damit ist Q gleich der Regel "Normalkoordinaten am geodaetischen Umkreismittelpunkt, auf das Riemann-Volumen des geodaetischen Simplex skaliert", die ohne Einbettung definierbar ist (auf allgemeinen Mannigfaltigkeiten bis auf Konventionen der Ordnung h^2 Riem bei der Wahl des geodaetischen Simplex). C, S und Q haben dieselbe (intrinsische) Form und unterscheiden sich nur im Massstab je Simplex: C 1, S J(c_T)^(1/4), Q <J>_T^(1/4); C und S brauchen fuer den Massstab die Einbettung, Q nicht. G ist die einzige Regel, die die Form aendert |
| S4 | Quadraturordnung fuer Q [F] | **Grundmann-Moeller vom Grad 5** (21 Punkte bei n = 4, Gewichte (-1)^i 2^(-2s)(d+n-2i)^d n!/(i!(d+n-i)!), s = 2, d = 5; alle Punkte innen). Fehler je Simplex O(theta^6) gegen O(theta^4) bei Grad 2 oder 3; theta^2 ~ h^2/a^2 ~ N^(-1/2). Der globale Anteil des Fehlers faellt in die Umrechnung; der lokale Anteil summiert sich zu N theta^6 ~ N^(-1/2) und beruehrt beta nicht (selbst Grad 2 gaebe N theta^4 = O(1), also nur delta) [M]. Kosten vernachlaessigbar. Kontrollen: KQ1 (Monome bis Grad 5 exakt, Grad 6 nicht), Konvergenz max abs(J_5/J_3 - 1) je Netz, V_Q5/V_K gegen 1 |
| S5 | Umrechnung je Regel | Wie INDUZIERT-KUGEL-1 (S3, S3') und GEGENLESEN Frage 2 [M]: K vom Grad 2, M vom Grad 4 in den Laengen, also Gamma_korr = Gamma + (N-1)/4 ln(V_K/V_R), Gamma_M,korr = Gamma_M - (N-1)/4 ln(V_K/V_R), V_R = Summe der Simplexvolumina der Regel (C, S, Q, G, Gs je eigenes). Fuer Q ist V_Q = Summe V_C,T <J>_T = V_K bis auf den Quadraturfehler, die Umrechnung also fast null (GEGENLESEN mit Grad 2: hoechstens 0,017 sqrt N; mit Grad 5 siehe Abschnitt 10). Kontrollen KB2 (Skalierung der korrigierten Groessen fuer Q und Gs) und KE aus INDUZIERT-KUGEL-1 |
| S6 | Vorab ableitbar (keine Messung) | V_G/V_K, V_Q/V_K, die Umrechnungen, die Einbettbarkeit und die Reproduktion von Gamma_C und Gamma_S (K2-0). Gamma_Q und Gamma_G sind aus den Rohdaten von INDUZIERT-KUGEL-1 nicht ableitbar (GEGENLESEN, Ableitbarkeitsprobe) |
| S7 | Groessenordnung [ES, grob, keine Messung] | Fuer ein regulaeres Simplex mit Winkelradius theta: J(c) = 1 + 2 theta^2, <J> = 1 + (19/12) theta^2 (Mittel von abs(y)^2 = r^2/6), also Laengenfaktor S 1 + theta^2/2, Q 1 + 0,40 theta^2. In der Fassung korr zaehlt nur die Verteilung der Faktoren ueber die Simplizes; linear gedacht laege beta_Q,korr bei beta_C + 0,79 (beta_S - beta_C), also nahe -1,61 bei den Werten von INDUZIERT-KUGEL-1. Das ist eine Schaetzung, kein Ziel |
| S8 | Statistik | Std von beta je Saat etwa 0,33 (INDUZIERT-KUGEL-1), also SE(beta) etwa 0,05 bei 40 Saaten; gepaarte Regeldifferenzen rauschen wie S - C (Std je Saat 0,011). Fuer K2-2 (Schranke 0,3) und K2-3 (0,4) sind die Punktschaetzer damit auf etwa 0,01 bestimmt |

## 2. Konstruktion (code/kugel2.py)

- **Netze [Karte]:** k1.kugelnetz aus kugel.py, unveraendert (Saatschluessel [20261004, 39, 4, N, saat], Qhull,
  Orientierung, alle Tor-Pruefungen von INDUZIERT-KUGEL-1). Reihenfolge je Netz wie dort: Netz, Regel C, Regel S
  (k1.auswerten), danach die neuen Regeln. Damit muessen Gamma_C und Gamma_S bitgleich herauskommen (K2-0).
- **Regel Q [Karte, S3, S4]:** je Simplex alle Sehnenlaengen mal <J>_T^(1/4), <J>_T = Grundmann-Moeller-Mittel vom Grad 5
  von J(x) = a^4 d0/abs(x)^5 ueber das flache Simplex (d0 = Abstand der Facettenebene vom Ursprung). Mitgerechnet
  (beschreibend): Grad 3 (Grundmann-Moeller, 6 Punkte) und Grad 2 (Regel von INDUZIERT-KUGEL-1).
- **Regel G [Karte, S1]:** Laenge 2a arcsin(c/(2a)) je Kante. **Einbettbarkeit [Karte]:** je Simplex Gram-Kriterium
  (kleinster Eigenwert der Gram-Matrix > 0, wie k1.auswerten) und Cayley-Menger-Determinanten aller Seiten:
  V_k^2 = (-1)^(k+1) CM_k/(2^k (k!)^2) > 0 fuer alle 10 Dreiecke, 5 Tetraeder und das 4-Simplex. Gezaehlt je Netz:
  Simplizes mit Verletzung je Seitendimension, Vereinigung, Gram-Kriterium, Uneinigkeit beider, Anteil, Zahl kleiner
  Gram-Eigenwerte (< 1e-2, 1e-3, 1e-4, 1e-6), Volumen der einbettbaren Simplizes. Dieselbe Zaehlung fuer C
  (Kontrolle, muss 0 sein). **Gamma_G nur ohne jede Verletzung** (k1.auswerten bricht sonst vor der LU ab).
- **Regel Gs, Nebenlesart [F]:** G in den einbettbaren Simplizes, Q-Laengen in den nicht einbettbaren (Vereinigung
  beider Kriterien). Zweck: die einzige ueberall definierte Regel, die so weit wie moeglich geodaetische Laengen
  nutzt und intrinsisch bleibt (S3). Vorbehalt: Mischung zweier Regeln; der ersetzte Anteil waechst wie N^(1/2) (S2)
  und liegt damit auf der Ordnung des Signals. Kein Kartenurteil.
- **Gamma, Gamma_M, Umrechnung:** k1.auswerten je Regel (S5).
- **Torus [F, K4]:** nicht neu gerechnet. Die Auswertung uebernimmt Torus-Gamma, Gamma_M, Umrechnung und Gueltigkeit aus
  den Laufdateien von INDUZIERT-KUGEL-1 (.69: /home/fmh/fmhc-physics-remote/runde39-induziert-kugel/lauf/messung-n4-*.json,
  nur lesen; vor der Auswertung gegen deren PRUEFSUMMEN.txt geprueft). Gleiche Saat und gleiches N, also dieselben
  Torusnetze (Torus-Saat 39000 + saat). Grund: 47 s je Saat bei N = 8000 gespart; die Paarung ist identisch.

## 3. Messgroesse und Fit [Karte; unveraendert aus INDUZIERT-KUGEL-1]

- Je Saat j, Regel r (C, S, Q, G, Gs), Groesse q (Gamma, Gamma_M), Fassung v (korr = umgerechnet, roh):
  y_j(N) = (G_Kugel,j(N) - G_Torus,j(N))/sqrt(N); Fit je Saat y_j(N) = beta_j + delta_j/sqrt(N) (OLS ueber die vier N,
  gamma = 0); beta = Mittel der beta_j, SE = Std(beta_j, ddof 1)/sqrt(M). Funktionen fits, stat, y_wert aus
  auswertung_kugel.py (unveraendert importiert), also dieselbe Numerik wie in INDUZIERT-KUGEL-1.
- Gepaart auf denselben Saaten: beta_j(r1) - beta_j(r2) fuer (Q, S), (Gs, S), (Q, C), (Gs, C), (S, C), (Gs, Q), je
  Groesse und Fassung; fuer K2-2 zusaetzlich beta_j(Q, Gamma, roh) - beta_j(S, Gamma, korr). G nur, wenn es auf
  mindestens zwei Saaten bei allen N einbettbar ist (dann auf dieser Teilmenge, mit allen Regeln gepaart).
- Mitberichtet (beschreibend): Dreiparameterfit, WLS auf die Mittelwerte je N mit chi^2, Teilbereiche, y je N,
  Massdifferenz Gamma - Gamma_M je Regel, Volumen-, Einbettungs-, Quadratur- und Zeitstatistik je N.

## 4. Saaten, N, Laeufe [Karte; F nach dem Rauchlauf, blind]

- N = 1000, 2000, 4000, 8000 [Karte]; **Saaten 0 bis 39 (40 je N)**, also genau die Saaten von INDUZIERT-KUGEL-1
  [F]. Regel vor dem Rauchlauf: 40 Saaten, wenn die Hauptlaeufe nach der Rauchzeit hoechstens 30 min Wandzeit
  brauchen, sonst 30, sonst 20 (Karte: mindestens 10). Rauchzeit je Saat 3,0 / 7,0 / 20,4 / 79 s (N = 1000 / 2000 /
  4000 / 8000), also 4540 s Rechenzeit, auf drei Spuren etwa 25 min.
- .69, /home/fmh/fmhc-physics-remote/runde40-induziert-kugel2/, nur ueber kleintest.sh, Spuren cpu3, cpu4, cpu5, je Spur
  eine Kette nacheinander (ein ssh je Spur, Starter je Lauf); bei N = 8000 hoechstens 3 Saaten je Lauf.
  - cpu3: N = 8000 Saaten 0-2, 3-5, 6-8, 9-11, 12-14; N = 4000 Saaten 0-15.
  - cpu4: N = 8000 Saaten 15-17, 18-20, 21-23, 24-26, 27-29; N = 4000 Saaten 16-31.
  - cpu5: kontrolle; N = 8000 Saaten 30-32, 33-35, 36-38, 39; N = 4000 Saaten 32-39; N = 2000 Saaten 0-39;
    N = 1000 Saaten 0-39.
  - Ausgabe lauf/messung-n4-N<N>-s<saat0>.json, lauf/kontrolle.json, Logs je Lauf; jeder Lauf schreibt nach jedem
    (Saat, N).
- **Abbruch [F]:** Nicht fertige (Saat, N) fehlen; Saaten ohne alle N heissen unvollstaendig und fallen aus dem Fit
  (offengelegt). Letzter Start spaetestens 13:50 CEST.
- Danach: auswertung_kugel2.py lauf /home/fmh/fmhc-physics-remote/runde39-induziert-kugel/lauf lauf/auswertung.json
  (ueber den Starter).

## 5. Tor [F]

- Je (Saat, N): Kugelnetz gueltig (k1.kugel_gueltig), Torus gueltig und Torus-LU ok (aus INDUZIERT-KUGEL-1), LU ok
  fuer C, S, Q und Gs (alle U_ii > 0, perm_r = perm_c, alle Simplizes einbettbar).
- Eine Saat mit einem Fehler bei irgendeinem N wird ausgeschlossen und gezaehlt. Mehr als 10 % ausgeschlossen oder
  weniger als 8 Saaten: K2-1 bis K2-3 (Plan) "nicht auswertbar (Tor)".
- **Tor G:** Regel G ist fuer eine Saat definiert, wenn sie bei allen N ohne Verletzung einbettbar ist und die LU ok
  ist. Fallen mehr als 10 % der guten Saaten fuer G aus oder bleiben weniger als 8, ist K2-1 "nicht auswertbar (Regel G
  nicht einbettbar)"; G wird dann, falls auf mindestens 2 Saaten definiert, nur beschreibend berichtet
  (Auswahlverzerrung moeglich).
- Kontrollen (Abschnitt 7) muessen ihre Schwellen erfuellen, sonst kein Urteil.

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln (mechanisch in auswertung_kugel2.py)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K2-0 | Kontrolle: Gamma_C und Gamma_S bitgleich mit INDUZIERT-KUGEL-1 | 90 % |
| K2-1 | [H] Regel G: beta_G < 0 mit >= 3 SE (umgerechnete Fassung) | 70 % |
| K2-2 | [H] Regel Q: beta_Q,roh < 0 mit >= 3 SE und abs(beta_Q,roh - beta_S,korr) <= 0,3 | 55 % |
| K2-3 | [H] Spanne der vier Regeln C, S, G, Q (Gamma, umgerechnet) hoechstens 0,4 | 55 % |

"Umgerechnet" heisst Fassung korr (Konvention INDUZIERT-KUGEL-1) [K7].
- **K2-0:** Karte = Plan: eingetroffen, wenn fuer jedes hier gerechnete (Saat, N) Gamma_C und Gamma_S als float gleich
  (==) den Werten in den Laufdateien von INDUZIERT-KUGEL-1 sind; sonst nicht eingetroffen (mit groesster Abweichung).
  Mitberichtet: Gamma_M, Summe ln m, V, Umrechnung, lam_min, Geometriedaten (a, V_K, V_C, V_S, V_Q Grad 2), F.
  Ist K2-0 nicht eingetroffen, stehen K2-1 bis K2-3 mechanisch da, mit dem Vermerk "nicht bitgleich" und der
  Abweichung.
- **K2-1** (Regel G, Gamma, korr): Ist das Tor G bestanden: Karte = Plan: eingetroffen, wenn beta_G <= -3 SE; sonst nicht
  eingetroffen; Merkmal "Vorzeichen gekippt" bei beta_G >= 2 SE. Ist es nicht bestanden: Karte und Plan "nicht
  auswertbar (Regel G nicht einbettbar)" [K1]. **Nebenlesart Gs [F]:** dieselbe Regel auf beta_Gs (korr), berichtet,
  kein Kartenurteil.
- **K2-2** (Regel Q): Karte = Plan: eingetroffen, wenn beta_Q,roh <= -3 SE(beta_Q,roh) und
  abs(beta_Q,roh - beta_S,korr) <= 0,3 (Punktschaetzer derselben 40 Saaten); sonst nicht eingetroffen. Beide Teile
  einzeln berichtet, dazu die gepaarte Differenz je Saat und beta_Q,korr. beta_S,korr ist der Wert dieses Laufs auf
  denselben Saaten [K6].
- **K2-3** (Gamma, korr): Mit Regel G (Tor G bestanden): Karte = Plan: eingetroffen, wenn
  max - min von beta_C, beta_S, beta_G, beta_Q <= 0,4; sonst nicht eingetroffen. Ohne Regel G [K2]: Spanne von C, S, Q
  > 0,4 heisst nicht eingetroffen (G kann die Spanne nur vergroessern); sonst "nicht auswertbar (Regel G fehlt)".
  Nebenlesart Gs: Spanne von C, S, Q, Gs, berichtet, kein Kartenurteil.
- Vermerk bei nicht bestandenem Haupt-Tor: K2-1 bis K2-3 (Plan) "nicht auswertbar (Tor)".

## 7. Kontrollen (code/kugel2.py kontrolle; Schwellen vor dem Lauf)

- **KQ1 (Quadratur):** Grad-5-Regel exakt fuer alle baryzentrischen Monome bis Grad 5 (relativ <= 1e-12) und nicht
  exakt bei Grad 6 (> 1e-6, Negativprobe); Grad-3-Regel exakt bis 3, nicht bei 4; Gewichtssumme 1.
- **KCM (Cayley-Menger):** regulaeres Simplex ohne Verletzung; verletzte Dreiecksungleichung wird erkannt (CM2 und
  Gram); Quadrat-Tetraeder auf der Kugel (a = 3, r = 1, Dicke etwa 0,05) mit Sehnen einbettbar, mit geodaetischen
  Laengen nicht (CM3, Gram); das ist zugleich die Probe zu S2.
- **KQ2/KG1 (Netze Saat 991, N = 1000 und 2000):** J neu gegen kugelnetz relativ <= 1e-12; V_Q (Grad 2) neu gegen den
  Wert aus kugelnetz relativ <= 1e-12; abs(V_Q5/V_K - 1) <= 1e-3 und kleiner als bei Grad 2; arcsin gegen arccos
  relativ <= 1e-10; C und Q ohne Verletzung, Gram und CM einig.
- **KB2 (S^4, N = 400, Saat 990):** fuer Q und Gs LU gegen dichte Eigenwerte und slogdet <= 1e-8, Gamma_M gegen
  verallgemeinerte Eigenwerte <= 1e-8, korrigierte Groessen skalenfrei <= 1e-8.
- **In jedem Netz:** J neu gegen kugelnetz <= 1e-12, arcsin gegen arccos <= 1e-10, C ohne Verletzung, Gram und CM fuer C
  einig; Uneinigkeit fuer G wird berichtet (G-Kriterium ist die Vereinigung).
- Aus INDUZIERT-KUGEL-1 gelten weiter KA bis KE und KG (P1, LU, Gamma_M, Skalierung, Negativproben): derselbe Code.

## 8. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Regel G ist auf diesen Netzen nicht einbettbar.** S2 sagt es vorab, Kontrolle und Rauchlauf zeigen es (Abschnitt
  10): 3 bis 9 % der Simplizes je Netz, in jedem gerechneten Netz. Die Karte legt keine Behandlung fest. Plan: Tor G
  (Abschnitt 5) und K2-1 "nicht auswertbar"; Nebenlesart Gs. Die Wahrscheinlichkeit der Karte (70 %) bleibt stehen.
- **[K2] K2-3 ohne G:** Regel wie in Abschnitt 6 (drei Regeln koennen die Vorhersage widerlegen, nicht bestaetigen).
- **[K3] Q ist intrinsisch definierbar (S3).** K2-2 prueft damit nicht nur die Volumenumrechnung, sondern auch eine
  Regel, die ohne Einbettung auskommt. Der Satz "eine allgemein intrinsische Regel steht aus" ist durch Q zum Teil,
  durch G nicht gedeckt.
- **[K4] Torus uebernommen** statt neu gerechnet (Abschnitt 2).
- **[K5] Quadraturordnung:** Grad 5 (S4); die Karte verlangt nur die Festlegung.
- **[K6] beta_S,korr in K2-2** aus diesem Lauf auf denselben Saaten; mit 40 Saaten und K2-0 ist er gleich dem Wert von
  INDUZIERT-KUGEL-1 (-1,651).
- **[K7] "umgerechnet"** = Fassung korr.
- **[K8] Saatzahl** 40 statt mindestens 10 (Karte: "mehr, wenn die Zeit reicht").
- Kartenfehler, die ein Urteil nach Kartenwortlaut aendern koennen: [K1] (K2-1 und K2-3 ohne G nicht im Kartenwortlaut
  entscheidbar).

## 9. Agenten-Vorhersagen (nach den Rauchlaeufen, vor den Hauptlaeufen; ohne Kenntnis der Messwerte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Haupt-Tor besteht ohne Ausschluss (C, S, Q, Gs in allen 160 Netzen gueltig) | 95 % |
| A2 | K2-0 eingetroffen (bitgleich) | 85 % |
| A3 | K2-1 nicht auswertbar (G in jedem Netz verletzt) | 99 % |
| A4 | K2-2 eingetroffen | 75 % |
| A5 | Nebenlesart Gs: beta_Gs,korr <= -3 SE | 85 % |
| A6 | K2-3 (Plan) "nicht auswertbar (Regel G fehlt)", also Spanne von C, S, Q <= 0,4 | 85 % |
| A7 | beta_Q,korr liegt zwischen beta_C,korr und beta_S,korr | 65 % |

## 10. Rauchlaeufe und Kontrolle (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC; Rauchsaaten 900 und 901, Probesaaten 950 bis 952)

- **kontrolle** (10:29:04 bis 10:29:13, cpu5, rc 0), alle Schwellen erfuellt [E]:
  - KQ1: Grad 5 exakt bis Grad 5 (<= 3,1e-15), Grad 6 Fehler 0,095; Grad 3 exakt bis 3, Grad 4 Fehler 0,20.
  - KCM: regulaer ohne Verletzung; Dreiecksverletzung erkannt (CM2, CM3, CM4, Gram); Quadrat mit Sehnen einbettbar
    (lam_min 7,7e-4), mit geodaetischen Laengen nicht (CM3 und CM4, lam_min -0,054).
  - KQ2/KG1 (Saat 991): J und V_Q (Grad 2) bitgleich mit kugelnetz (Abweichung 0,0); V_Q5/V_K - 1 = +1,7e-4
    (N = 1000) und +6,1e-5 (2000), Grad 2 -2,0e-3 und -1,0e-3, Grad 3 -3,3e-3 und -1,7e-3; max abs(J_5/J_3 - 1) =
    1,8 % und 0,7 %; arcsin gegen arccos 2,7e-14 und 4,0e-13. C und Q ohne Verletzung. **G: 2243 von 27 392 Simplizes
    (8,2 %) und 3569 von 57 576 (6,2 %) nicht einbettbar**; Dreiecke nie verletzt, Tetraeder-Seiten in 861 bzw. 1123
    Simplizes, 4-Simplex-CM in allen verletzten; Gram und CM einig.
  - KB2 (N = 400): Q und Gs LU gegen dicht <= 3,4e-13, Gamma_M <= 1,1e-13, Skalierung <= 1,8e-11 (G dort 1301
    Simplizes nicht einbettbar).
- **rauch-b** (10:29:09 bis 10:30:10, cpu4, rc 0), N = 1000, 2000, 4000, Saaten 900 und 901, blind: alle Netze und
  LU (C, S, Q, Gs) gueltig; G nicht einbettbar 2342 / 2310 (N = 1000, Anteil 8,5 %), 3452 / 3405 (2000, 6,0 %),
  5257 / 5377 (4000, 4,5 %); CM2 immer 0; V_Q5/V_K = 1,00020 / 1,000059 / 1,000020; V_G(einbettbar)/V_K 0,755 /
  0,826 / 0,873; 3,0 / 7,0 / 20,4 s je Saat; RSS bis 412 MB.
- **rauch-a** (10:29:06 bis 10:31:47, cpu3, rc 0), N = 8000, Saaten 900 und 901, blind: beide gueltig, G nicht
  einbettbar 7453 von 241 508 (3,1 %) und 7311 von 241 564 (3,0 %), V_Q5/V_K = 1,0000066 und 1,0000065, LU je 13,2 bis
  14,2 s, 79 und 81 s je Saat, RSS bis 940 MB.
- **Blindheit geprueft (jq):** In rauch-a.json und rauch-b.json hat keine Regel ein Feld gamma.
- **Codeprobe** (10:30:10 bis 10:30:29, cpu4): nicht blind auf N = 600 und 1200, Saaten 950 bis 952 (Torus aus der
  Probe von INDUZIERT-KUGEL-1), dann Auswertung; rc 0 fuer beide. Nur Struktur geprueft (jq keys: Urteile K2-0 bis
  K2-3, Fits fuer C, S, Q, Gs, Tor-Felder; M = 3, M_G = 0); Werte und Urteile der Probe nicht gelesen.
- **Skalierung der G-Verletzungen [E, beschreibend]:** Anteil 8,5 / 6,0 / 4,5 / 3,1 % bei N = 1000 / 2000 / 4000 / 8000,
  je Verdopplung Faktor 1,42 / 1,33 / 1,45, also etwa N^(-1/2); Zahl je Netz etwa wie N^(1/2), wie in S2 erwartet.
- **Zeitfolge der Festlegungen:** Regeln, Quadraturordnung, Einbettungspruefung, Nebenlesart Gs, Tor G, Fit und
  Urteilsregeln standen vor den Rauchlaeufen im Code (kugel2.py und auswertung_kugel2.py bis etwa 12:28 CEST, Start
  der Kontrolle 12:29:04 CEST). Nach den Rauchlaeufen festgelegt: Saatzahl 40 (nach der vorab notierten Zeitregel),
  Laufaufteilung, Agenten-Vorhersagen; Text von S2 (die Formel stand vorher nur in meinen Notizen, die Zaehlung im
  Code). Vor dem Einfrieren keine Gamma-Werte, Mittelwerte oder Vorzeichen der Messgroesse gesehen.
