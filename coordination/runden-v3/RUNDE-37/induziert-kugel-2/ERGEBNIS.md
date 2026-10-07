# INDUZIERT-KUGEL-2: Ergebnis (Runde 40, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 12:11:57 CEST. code/kugel2.py und code/auswertung_kugel2.py bis etwa 12:28 CEST, Kontrolle und
    Rauchlaeufe 10:29:04 bis 10:31:47 UTC, Codeprobe 10:30:10 bis 10:30:29 UTC, Plantext ab 12:31:18 CEST.
  - Eingefroren 12:33:27 CEST: PLAN.md.eingefroren-20261004-123327, Code-Kopien *.eingefroren-20261004-123327,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 10:33:47 bis 10:58:35 UTC (1 Kontrolle, 19 Messlaeufe, alle rc 0), Auswertung 10:58:43 bis 10:58:45 UTC
    (rc 0). Text ab 13:01:42 CEST.
- Code nach dem Einfrieren unveraendert: sha256 von kugel2.py (15dcbd85...), auswertung_kugel2.py (a2e332e0...),
  kugel.py (c2a4d790...) und auswertung_kugel.py (5b0a7126...) auf der .69 vor der Auswertung gleich den eingefrorenen.
  lauf-69/PRUEFSUMMEN.txt (.69, 42 Dateien) lokal nachgeprueft: 42 von 42 gleich. Die Laufdateien von
  INDUZIERT-KUGEL-1 (Torusseite, Vergleich K2-0) vor der Auswertung auf der .69 gegen deren PRUEFSUMMEN.txt geprueft:
  44 von 44 gleich.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu3, cpu4, cpu5).
  Euklidisch, eine Schleife, freies masseloses Skalarfeld (P1), synthetisch, keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [E] hier gerechnet, [ES] eigener Schluss, [F] Festlegung im Plan,
  [K] Kartenpunkt, [H] Hypothese.
- **Konvention (wie INDUZIERT-KUGEL-1):** y(N) = (Gamma_Kugel - Gamma_Torus)/sqrt(N), je Saat y = beta + delta/sqrt(N),
  beta = Saatmittel, SE aus der Saatstreuung (40 Saaten, dieselben wie INDUZIERT-KUGEL-1). korr = auf das eigene
  Volumen der Regel gleich N umgerechnet (= "umgerechnet" der Karte), roh = ohne. beta < 0 heisst Einsteins Vorzeichen
  (B = beta/61,56 < 0, positives G).
- **Regeln:** C Sehnen; S Sehnen mal J(Schwerpunkt)^(1/4); **Q** Sehnen mal <J>_T^(1/4), <J>_T Mittel des
  Jacobi-Faktors ueber das Simplex (Grundmann-Moeller Grad 5), also Simplexvolumen = Volumen des geodaetischen
  Simplex; **G** geodaetische Kantenlaengen 2a arcsin(c/(2a)); **Gs** (Nebenlesart des Plans) G, aber Q-Laengen in
  den nicht einbettbaren Simplizes.

## 1. Ergebnis zuerst

1. **Regel Q (volumentreu je Simplex) behaelt Einsteins Vorzeichen, ohne Volumenumrechnung [E]:**
   beta_Q,roh = **-1,613 +- 0,052** (t = -30,8), beta_Q,korr = -1,612 +- 0,052; alle 40 Saaten einzeln negativ
   (-2,31 bis -1,01). Die Umrechnung ist praktisch null (-0,0014 sqrt(N) bei N = 1000, -0,00015 bei 8000; Verschiebung
   von beta 0,0006). Gepaart: beta_Q,roh - beta_S,korr = +0,039 +- 0,0004. **K2-2 eingetroffen.**
2. **Regel G (geodaetische Laengen) ist auf diesen Netzen keine flache Simplexgeometrie [E, M]:** In allen 160 Netzen
   sind Simplizes nicht einbettbar, 8,6 % (N = 1000) bis 3,1 % (8000), im Mittel 2373 / 3517 / 5172 / 7525 je Netz.
   Ihre Zahl waechst wie N^0,56 (75 bis 84 mal sqrt(N)), also wie das Signal selbst. Ursache [M, PLAN S2]:
   Geodaetische Laengen verletzen in fast flachen Simplizes die Ptolemaeus- bzw. Cayley-Menger-Bedingung. **K2-1 und
   K2-3: nicht auswertbar** (Spanne C, S, Q = 0,196, also ohne G nicht widerlegt).
3. **Die Nebenlesart Gs (G mit Q-Ersatz) gibt kein lesbares sqrt(N)-Glied [E]:** y steigt von +1,28 (N = 1000) auf
   +3,30 (8000), die Modellprobe ist verworfen (chi^2 = 61,5 bei 2 Freiheitsgraden). Der Formalwert beta_Gs = +4,21 ist
   deshalb kein B; er zeigt, dass jede Reparatur der Splitter auf der Ordnung des Signals wirkt.
4. **Kontrolle K2-0 eingetroffen [E]:** Gamma_C und Gamma_S (und Gamma_M, Summe ln m, V, Umrechnung, lam_min,
   Geometrie, F) in allen 160 Netzen bitgleich mit INDUZIERT-KUGEL-1; die Fits reproduzieren -1,4554 (C) und -1,6515 (S).
5. **Bedeutung:** C, S und Q haben dieselbe intrinsische Simplexform (Normalkoordinaten am geodaetischen
   Umkreismittelpunkt) und unterscheiden sich nur im Massstab je Simplex; Q ist ohne Einbettung definierbar [M, PLAN S3].
   In dieser Familie haengt das Vorzeichen von Gamma weder an der Regel (Spanne 0,20) noch an der Volumenumrechnung.
   Offen bleibt
   eine Regel, die die Form aendert: Mit geodaetischen Laengen ist sie auf Poisson-Delaunay-Netzen ohne neue
   Triangulierung nicht definiert.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/auswertung_kugel2.py; Werte in lauf-69/auswertung.json.
**Haupt-Tor bestanden:** 40 von 40 Saaten bei allen vier N gueltig (160 Kugelnetze, LU fuer C, S, Q und Gs ok; Torus aus
INDUZIERT-KUGEL-1 gueltig), keine Saat ausgeschlossen oder unvollstaendig. **Tor G nicht bestanden:** 0 von 40 Saaten.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| K2-0 | Gamma_C und Gamma_S bitgleich mit INDUZIERT-KUGEL-1 | 90 % | **eingetroffen** | **eingetroffen** | 160 von 160 Netzen gleich (==), groesste Abweichung 0,0; ebenso alle mitverglichenen Felder |
| K2-1 | [H] Regel G: beta_G < 0 mit >= 3 SE (umgerechnet) | 70 % | **nicht auswertbar** (Regel G nicht einbettbar) | **nicht auswertbar** | G in 160 von 160 Netzen verletzt (3,1 bis 8,6 % der Simplizes). Nebenlesart Gs: mechanisch nicht eingetroffen, Merkmal "Vorzeichen gekippt" (beta_Gs,korr = +4,21 +- 0,06), aber Modellprobe verworfen (Abschnitt 3.1): kein lesbares beta |
| K2-2 | [H] Regel Q: beta_Q,roh < 0 mit >= 3 SE und abs(beta_Q,roh - beta_S,korr) <= 0,3 | 55 % | **eingetroffen** | **eingetroffen** | beta_Q,roh = -1,613 +- 0,052 (-30,8 SE); beta_S,korr = -1,651 +- 0,052; Abstand 0,039 (gepaart +0,0389 +- 0,0004) |
| K2-3 | [H] Spanne der vier Regeln C, S, G, Q (Gamma, umgerechnet) <= 0,4 | 55 % | **nicht auswertbar** (Regel G fehlt) | **nicht auswertbar** | Spanne C, S, Q = 0,196 (C -1,455, Q -1,612, S -1,651); mit G nicht bestimmbar. Nebenlesart mit Gs: 5,86, mechanisch nicht eingetroffen (Vorbehalt wie K2-1) |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "K2-1 und K2-2 treffen ein: ... haengt weder an einer nur auf der Kugel intrinsischen Laengenregel noch an der
    Volumenumrechnung": **nicht ausgeloest**, weil K2-1 nicht auswertbar ist. Getroffen ist nur die zweite Haelfte
    (Volumenumrechnung, ueber K2-2).
  - "K2-1 verfehlt (beta_G >= 0 oder < 3 SE): Das Vorzeichen haengt an der Laengenregel": **nicht ausgeloest**; es gibt
    kein beta_G. Die Nebenlesart Gs darf diesen Zweig nicht ersetzen (Modell verworfen, Regelmischung).
  - "K2-3 verfehlt": nicht ausgeloest (nicht auswertbar).
- **Vom Plan vorab festgelegt [K3]:** Q ist intrinsisch definierbar; mit K2-2 ist daher gezeigt: Eine ohne Einbettung
  definierbare, volumentreue Regel gibt Einsteins Vorzeichen auf dem symmetrischen Netz.

**Agenten-Vorhersagen** (PLAN Abschnitt 9, nach dem Rauchlauf, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (95 %) | Haupt-Tor ohne Ausschluss | **eingetroffen** |
| A2 (85 %) | K2-0 eingetroffen | **eingetroffen** |
| A3 (99 %) | K2-1 nicht auswertbar | **eingetroffen** (vor dem Einfrieren aus Kontrolle und Rauchlauf absehbar) |
| A4 (75 %) | K2-2 eingetroffen | **eingetroffen** |
| A5 (85 %) | Nebenlesart Gs: beta_Gs,korr <= -3 SE | **nicht eingetroffen** (+4,21; Modell verworfen) |
| A6 (85 %) | K2-3 (Plan) "nicht auswertbar (Regel G fehlt)" | **eingetroffen** (Spanne 0,196) |
| A7 (65 %) | beta_Q,korr zwischen beta_C,korr und beta_S,korr | **eingetroffen** (80 % des Wegs von C nach S; PLAN S7 schaetzte 79 %, also -1,610) |

## 3. Tabellen

### 3.1 beta je Regel, Groesse und Fassung [E]

(je Saat y = beta + delta/sqrt(N) ueber N = 1000 bis 8000; Mittel +- SE, M = 40; WLS = Fit auf die Mittelwerte je N,
chi^2 bei 2 Freiheitsgraden; "neg" = Saaten mit beta_j < 0)

| Regel / Groesse / Fassung | beta | Std je Saat | delta | WLS beta (chi^2, p) | neg |
|---|---|---|---|---|---|
| **Q / Gamma / roh (K2-2)** | **-1,613 +- 0,052** | 0,331 | -1,3 +- 2,6 | -1,620 +- 0,054 (2,47; 0,29) | 40 |
| Q / Gamma / korr | -1,612 +- 0,052 | 0,331 | -1,4 +- 2,6 | -1,619 +- 0,054 (2,46; 0,29) | 40 |
| Q / Gamma_M / korr | -1,513 +- 0,055 | 0,345 | -0,1 +- 2,8 | -1,520 +- 0,060 (2,41; 0,30) | 40 |
| Q / Gamma_M / roh | -1,512 +- 0,055 | 0,345 | -0,2 +- 2,8 | -1,519 +- 0,060 (2,41; 0,30) | 40 |
| S / Gamma / korr (= KUGEL-1) | -1,651 +- 0,052 | 0,331 | -1,7 +- 2,6 | -1,659 +- 0,054 (2,45; 0,29) | 40 |
| S / Gamma / roh | -1,190 +- 0,053 | 0,332 | -0,5 +- 2,6 | -1,197 +- 0,054 (2,47; 0,29) | 40 |
| S / Gamma_M / korr | -1,509 +- 0,055 | 0,346 | -0,1 +- 2,8 | -1,516 +- 0,060 (2,41; 0,30) | 40 |
| S / Gamma_M / roh | -1,971 +- 0,054 | 0,343 | -1,3 +- 2,8 | -1,977 +- 0,060 (2,41; 0,30) | 40 |
| C / Gamma / korr (= KUGEL-1) | -1,455 +- 0,053 | 0,332 | -1,0 +- 2,6 | -1,462 +- 0,054 (2,51; 0,29) | 40 |
| C / Gamma / roh | -3,135 +- 0,052 | 0,329 | -2,6 +- 2,6 | -3,143 +- 0,053 (2,46; 0,29) | 40 |
| C / Gamma_M / korr | -1,521 +- 0,054 | 0,342 | -0,2 +- 2,7 | -1,528 +- 0,060 (2,41; 0,30) | 40 |
| C / Gamma_M / roh | +0,159 +- 0,055 | 0,349 | +1,4 +- 2,8 | +0,152 +- 0,061 (2,40; 0,30) | 14 |
| Gs / Gamma / korr (Nebenlesart) | +4,21 +- 0,06 | 0,369 | -97,5 +- 2,9 | +4,26 +- 0,06 (**61,5; < 1e-13**) | 0 |
| Gs / Gamma / roh | +2,19 +- 0,06 | 0,360 | -92,5 +- 2,8 | +2,23 +- 0,06 (**63,1**) | 0 |
| Gs / Gamma_M / korr | +4,15 +- 0,06 | 0,369 | -96,0 +- 3,0 | +4,18 +- 0,07 (**43,5**) | 0 |
| Gs / Gamma_M / roh | +6,17 +- 0,06 | 0,381 | -100,9 +- 3,1 | +6,21 +- 0,07 (**42,0**) | 0 |

- **Q beschreibend:** Teilbereiche ohne N = 1000: -1,553 +- 0,081, ohne N = 8000: -1,584 +- 0,091; Dreiparameterfit
  -1,48 +- 0,36 (gamma -3,4 +- 9,2); mit gamma auf dem Kontinuumswert -1,609. B_Q = -1,612/61,56 = -0,0262, induziertes
  G = 0,76 in Einheiten des mittleren Punktabstands hoch 2 (von Hand).
- **Gs beschreibend:** Teilbereiche +4,75 (ohne 1000) und +3,76 (ohne 8000), Dreiparameterfit +7,1 +- 0,4 mit
  gamma = -75 +- 10: Das Ergebnis haengt am N-Bereich; ein sqrt(N)-Glied ist nicht trennbar.

### 3.2 Gepaarte Regeldifferenzen [E]

(beta_j(r1) - beta_j(r2) auf denselben 40 Saaten; Mittel +- SE, in Klammern Std je Saat)

| Differenz | Gamma, korr | Gamma, roh | Gamma_M, korr |
|---|---|---|---|
| Q - S | +0,0395 +- 0,0004 (0,0026) | -0,422 +- 0,0004 | -0,0035 +- 0,0003 |
| Q - C | -0,1565 +- 0,0014 (0,0086) | +1,523 +- 0,001 | +0,0081 +- 0,0010 |
| S - C | -0,1961 +- 0,0018 (0,0111) | +1,945 +- 0,002 | +0,0116 +- 0,0013 |
| Gs - Q | +5,82 +- 0,01 (0,077) | +3,80 +- 0,01 | +5,66 +- 0,01 |
| **Q roh - S korr (K2-2)** | **+0,0389 +- 0,0004 (0,0026)** | | |

- Massdifferenz beta(Gamma) - beta(Gamma_M), korr: Q -0,099 +- 0,039 (2,5 SE), S -0,142 +- 0,040, C +0,066 +- 0,038.
- In der Fassung korr liegt Q bei 80 % des Wegs von C nach S (-0,1565/-0,1961 = 0,798), so wie die Schreibtischschaetzung
  PLAN S7 (Laengenfaktoren 1 + 0,40 theta^2 gegen 1 + theta^2/2) es vorab nahelegte.

### 3.3 y je N [E]

(y = Delta Gamma/sqrt(N), Mittel +- SE ueber 40 Saaten)

| Datensatz | N = 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|
| Q, Gamma, roh | -1,637 +- 0,039 | -1,688 +- 0,041 | -1,592 +- 0,044 | -1,638 +- 0,036 |
| Q, Gamma, korr | -1,639 +- 0,039 | -1,689 +- 0,041 | -1,592 +- 0,044 | -1,638 +- 0,036 |
| S, Gamma, korr | -1,688 +- 0,039 | -1,736 +- 0,041 | -1,637 +- 0,044 | -1,681 +- 0,036 |
| C, Gamma, korr | -1,470 +- 0,039 | -1,525 +- 0,040 | -1,429 +- 0,044 | -1,477 +- 0,036 |
| Gs, Gamma, korr | +1,276 +- 0,045 | +1,800 +- 0,045 | +2,576 +- 0,046 | +3,298 +- 0,040 |
| Gs, Gamma, roh | -0,592 +- 0,043 | -0,111 +- 0,043 | +0,632 +- 0,045 | +1,328 +- 0,039 |

- Q ist ueber den Faktor 8 in N flach wie C und S (Schwankung +-0,05). Gs nicht: y(Gs) - y(Q) = 2,92 / 3,49 / 4,17 /
  4,94 waechst je Verdopplung um den Faktor 1,18 bis 1,20, also Delta Gamma(Gs - Q) etwa wie N^0,75 [E, beschreibend].
  Ein Glied der Ordnung N/a (erste Ordnung in h/a je Simplex) haette genau diese Potenz; woher es kommt, ist nicht
  getrennt [H: aus den Simplizes, die G an die Einbettungsgrenze schiebt].

### 3.4 Netze, Einbettung, Volumen [E]

| | N = 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|
| Simplizes je Netz F | 27 456 | 57 356 | 118 249 | 241 679 |
| G nicht einbettbar je Netz (Mittel, min bis max) | 2373 (2202 bis 2504) | 3517 (3393 bis 3714) | 5172 (4943 bis 5372) | 7525 (7311 bis 7742) |
| Anteil | 8,64 % | 6,13 % | 4,37 % | 3,11 % |
| davon mit verletzter Tetraederseite | 899 | 1113 | 1379 | 1687 |
| Netze mit Verletzung | 40 von 40 | 40 von 40 | 40 von 40 | 40 von 40 |
| G: Gram-Eigenwert < 0,01 (inkl. nicht einbettbare) / C: < 0,01 | 3955 / 1728 | 6896 / 3588 | 12 244 / 7391 | 22 047 / 14 999 |
| V_C/V_K | 0,8030 | 0,8577 | 0,8977 | 0,9268 |
| V_S/V_K | 1,0650 | 1,0445 | 1,0308 | 1,0214 |
| V_Q/V_K (Grad 5) | 1,000180 | 1,000058 | 1,000019 | 1,0000066 |
| V_Q/V_K (Grad 2, wie KUGEL-1) | 0,99791 | 0,99901 | 0,99952 | 0,99976 |
| V_Gs/V_K | 0,789 | 0,843 | 0,884 | 0,916 |
| V_G (nur einbettbare)/V_K | 0,759 | 0,825 | 0,873 | 0,909 |
| Umrechnung korr - roh, Gamma, in sqrt(N): C / S / Q / Gs | +1,733 / -0,497 / -0,0014 / +1,868 | +1,716 / -0,486 / -0,0006 / +1,911 | +1,707 / -0,479 / -0,0003 / +1,944 | +1,699 / -0,474 / -0,00015 / +1,970 |
| max abs(J_5/J_3 - 1) je Simplex | 2,5 % | 0,95 % | 0,46 % | 0,23 % |
| Laufzeit je Saat (Kugel, alle Regeln) | 2,9 s | 7,1 s | 19,9 s | 77,9 s |

- Die nicht einbettbaren G-Simplizes: Dreiecke nie verletzt (sphaerische Dreiecksungleichung), sonst Tetraeder- und
  4-Simplex-Bedingung; Gram-Kriterium und Cayley-Menger-Vereinigung in allen 160 Netzen einig. Zahl je Netz geteilt
  durch sqrt(N): 75,0 / 78,6 / 81,8 / 84,1; Exponent 0,555; Anteil etwa wie N^(-1/2), wie in PLAN S2 erwartet.
- Der Quadraturfehler von V_Q faellt wie N^(-1,6) (Grad 5, erwartet theta^6 ~ N^(-1,5)) gegen N^(-1,05) bei Grad 2.
  Laengenfaktor Q/S je Simplex 0,962 bis 0,998 (N = 1000) und 0,987 bis 0,9995 (8000).
- C und Q: in allen 160 Netzen 0 Verletzungen. LU: kleinstes U_ii 2,77 (C), 2,80 (Q), 2,99 (Gs); RSS bis 1011 MB.

## 4. Kontrollen

- **Haupt-Tor und Tor G (PLAN Abschnitt 5):** Abschnitt 2.
- **K2-0 (Reproduktion):** 160 von 160 Netzen bitgleich in Gamma, Gamma_M, Summe ln m, V, Umrechnung und lam_min fuer C
  und S, dazu a, V_K, V_C, V_S, V_Q (Grad 2) und F. Die Fits von C und S stimmen mit INDUZIERT-KUGEL-1 ueberein
  (-1,4554 und -1,6515 und alle Nebenwerte in Tabelle 3.1).
- **Kontrolllauf lauf-69/kontrolle.json (10:33:47 bis 10:33:56 UTC, cpu5, rc 0), alle Schwellen erfuellt:**
  - KQ1 (Quadratur): Grundmann-Moeller Grad 5 (21 Punkte) exakt fuer alle baryzentrischen Monome bis Grad 5
    (<= 3,1e-15 relativ), Grad 6 Fehler 0,095 (Negativprobe schlaegt an); Grad 3 exakt bis 3, Grad 4 Fehler 0,20.
  - KCM (Cayley-Menger): regulaeres Simplex ohne Verletzung; verletzte Dreiecksungleichung erkannt (CM2, CM3, CM4 und
    Gram); Quadrat-Tetraeder auf der Kugel (a = 3, r = 1, Dicke etwa 0,05) mit Sehnen einbettbar (lam_min 7,7e-4), mit
    geodaetischen Laengen nicht (CM3 und CM4, lam_min -0,054). Das ist die Probe zum Mechanismus (PLAN S2).
  - KQ2/KG1 (Netze Saat 991): J und V_Q (Grad 2) neu gerechnet bitgleich mit kugelnetz; V_Q5/V_K - 1 = +1,7e-4
    (N = 1000) und +6,1e-5 (2000) gegen -2,0e-3 und -1,0e-3 bei Grad 2; arcsin gegen arccos <= 4,0e-13; C und Q ohne
    Verletzung, Gram und Cayley-Menger einig.
  - KB2 (S^4, N = 400): Q und Gs, LU gegen dichte Eigenwerte und slogdet <= 3,4e-13, Gamma_M gegen verallgemeinerte
    Eigenwerte <= 1,1e-13, korrigierte Groessen skalenfrei <= 1,8e-11.
- **In jedem Netz (160):** J neu gegen kugelnetz 0,0; arcsin gegen arccos <= 2,4e-12; C ohne Verletzung, Gram und CM
  einig; fuer G Gram und CM-Vereinigung einig.
- **Modellprobe:** Q chi^2 = 2,47 bei 2 Freiheitsgraden (p = 0,29); Gs verworfen (Abschnitt 3.1).
- Aus INDUZIERT-KUGEL-1 gelten weiter KA bis KE und KG fuer den unveraenderten Code (P1, LU, Gamma_M, Skalierung,
  Negativproben).

**Latten (v3):**
- **L1 (kann scheitern):** ja. beta_Q haette positiv oder weit von S liegen koennen (K2-2), G haette einbettbar sein und
  ein anderes Vorzeichen geben koennen (K2-1), die Reproduktion haette abweichen koennen (K2-0). Die Einbettungspruefung
  hat eine Negativprobe (KCM), die Quadratur eine (KQ1).
- **L2 (Gegenprobe):** vier Regeln auf denselben Netzen, zwei Masse, zwei Fassungen, bitgleiche Reproduktion von C und S,
  Teilbereiche, Dreiparameterfit, WLS, LU gegen dicht.
- **L3 (Numerik):** log det' etwa 1e-13 absolut (KB2); Quadratur Grad 5 auf 2e-4 bis 7e-6 des Volumens; SE(beta) 0,052.
- **L4 (schon bekannt):** dass Regge-Kalkuel duenne Simplizes ("Splitter") schlecht vertraegt und Delaunay in 3D/4D
  Splitter erzeugt, ist bekannt [L, aus dem Gedaechtnis]; die geodaetische Verletzung auf der Kugel und ihr Anteil
  ~ N^(-1/2) habe ich nicht in der Literatur gesucht [L?].
- **L5 (Messbezug):** keiner (4D euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] G nicht einbettbar:** bestaetigt in allen 160 Netzen; K2-1 nicht auswertbar, wie vor dem Einfrieren absehbar
  (A3, 99 %). Die Wahrscheinlichkeit der Karte (70 %) bezog sich auf ein Vorzeichen, das es nicht gibt.
- **[K2] K2-3 ohne G:** Spanne C, S, Q = 0,196 <= 0,4, also nicht auswertbar; mit G waere die Vorhersage noch zu
  entscheiden gewesen.
- **[K3] Q intrinsisch definierbar:** traegt die Lesart von K2-2 ueber die Volumenfrage hinaus (Abschnitt 7).
- **[K4] Torus uebernommen:** dieselben Netze; die Torus-Gueltigkeit kam aus den geprueften Laufdateien von
  INDUZIERT-KUGEL-1 (alle 160 gueltig).
- **[K5] Quadratur Grad 5:** Volumenfehler 1,8e-4 bis 6,6e-6; mit Grad 2 waere die Umrechnung von Q 12- bis 35-mal
  groesser gewesen, aber ebenfalls vernachlaessigbar (GEGENLESEN: hoechstens 0,017 sqrt N).
- **[K6] beta_S,korr aus diesem Lauf:** -1,6515, gleich INDUZIERT-KUGEL-1.
- **[K7] "umgerechnet" = korr**, **[K8] 40 Saaten:** wie geplant.

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:** keine Gamma-Werte, Mittelwerte oder Vorzeichen der Messgroesse (Rauchdateien blind,
   per jq geprueft: kein Feld gamma). Gesehen habe ich: Einbettungszaehlungen fuer G (Kontrolle und Rauchlauf: jedes
   Netz verletzt), Volumina, Quadraturfehler, Zeiten, LU-Gueltigkeit, die Abweichungen der Kontrollen und von der
   Codeprobe nur die Struktur (jq keys, dazu M = 3 und M_G = 0). **Damit stand der Ausgang von K2-1 (nicht auswertbar)
   vor dem Einfrieren fest**; offengelegt als [K1] und A3.
2. **Zeitfolge:** Code (Regeln, Einbettungspruefung, Quadratur, Nebenlesart Gs, Tor G, Urteilsregeln) bis etwa 12:28
   CEST, Kontrolle ab 12:29:04 CEST, Plantext ab 12:31:18 CEST, also nach dem Start der Kontrolle. Die Formel in PLAN S2
   habe ich vorher hergeleitet, aber erst nach der Kontrolle in den PLAN geschrieben; dass ich den Mechanismus vorher
   erwartet habe, belegt nur die Negativprobe "quadrat_geodaetisch" in kugel2.py (vor der Kontrolle geschrieben).
3. **Nebenlesart Gs vor dem Rauchlauf festgelegt**, ihr Ausgang (positiv, Modell verworfen) war nicht absehbar; meine
   Vorhersage A5 (85 % negativ) ist nicht eingetroffen.
4. **Nach dem Einfrieren:** kein Code geaendert. Die Laufprotokolle enthalten keine Gamma-Werte (nur Gueltigkeit,
   Einbettung, Volumen, Zeiten). Eine Ueberwachung (Monitor-Werkzeug) hat alle 60 s per ssh die Zeilen "ende", Fehler
   und "gueltig False" der Logs abgefragt. Messwerte habe ich erst in auswertung.json gesehen.
5. **ssh-Verbindungen:** Waehrend der Hauptlaeufe lief fuer etwa eine Minute ein zweiter Abfragebefehl neben der
   Ueberwachung; in dieser Zeit waren kurz bis zu 5 gleichzeitige Verbindungen moeglich (3 Spurketten, 2 kurze
   Abfragen). Danach gestoppt.
6. **Auf der .69 ausserhalb des Starters:** mkdir, ls, cat (kleintest.sh), sha256sum, grep, cut, tail, wc, date, uptime,
   nproc, free, /usr/bin/jq (Struktur der Probe, Blindprobe) und einmal paste mit bc (Summe der Gueltigkeitszaehlung).
   Kein Python ausserhalb des Starters.
7. **Lokal:** kein python, awk oder perl. Benutzt: jq, grep, sha256sum, date, ssh, scp, cp, mkdir, ls, cat, cut, comm,
   sort, wc, printf und sleep in Warteschleifen (bash-Schleifen). Nichts geloescht.
8. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
   unter /tmp/claude-1000/.../tasks/ an (nur Rueckgabecodes und Endzeilen).
9. **ERGEBNIS-Entwurf:** Um etwa 12:38 CEST habe ich ERGEBNIS.md nur mit dem Kontrollabschnitt angelegt (Kontrollwerte,
   keine Messwerte); diese Fassung ersetzt ihn.
10. **Feldname:** "V_Q2_neu_gegen_KUGEL1_rel" in den Laufdateien vergleicht mit dem in derselben Rechnung von kugelnetz
    erzeugten Wert, nicht mit den gespeicherten Dateien von INDUZIERT-KUGEL-1; den Dateivergleich macht K2-0.
11. **Zeitbox:** Start 12:11:57 CEST, Text fertig 13:05:30 CEST (date), also 54 min von 120.

## 7. Bedeutung

- **Was gezeigt ist [E]:**
  - Auf denselben 40 S^4-Saaten und vier N gibt die volumentreue Regel Q ein negatives sqrt(N)-Glied
    (-1,613 +- 0,052), ohne dass eine Volumenumrechnung noetig ist; sie liegt 0,04 neben S und 0,16 neben C. Die
    Volumenumrechnung von INDUZIERT-KUGEL-1 war also kein Hebel fuer das Vorzeichen von Gamma.
  - Geodaetische Kantenlaengen ergeben auf Poisson-Delaunay-Netzen der S^4 in jedem Netz 3 bis 9 % nicht einbettbare
    Simplizes; ihre Zahl waechst wie sqrt(N). Regel G ist daher nicht rechenbar, und jede lokale Reparatur wirkt auf der
    Ordnung des Signals (Gs: y nicht flach, kein beta).
- **Was ich daraus schliesse [M, ES]:**
  - C, S und Q geben jedem Simplex dieselbe Form, naemlich die Form in Riemann-Normalkoordinaten an seinem geodaetischen
    Umkreismittelpunkt, und unterscheiden sich nur im Massstab je Simplex. Q waehlt den Massstab intrinsisch (Riemann-
    Volumen des geodaetischen Simplex). Fuer diese Familie ist Einsteins Vorzeichen robust (Spanne 0,20, alle negativ).
  - Nicht geprueft ist eine Regel, die die Form der Simplizes aendert. Die naheliegende (geodaetische Laengen) scheitert
    an den Splittern der Delaunay-Zerlegung, nicht an der Physik.
  - Mit dem Satz des Gegenlesers (A1) zusammen: Gedeckt ist "auf dem isometrie-invarianten S^4-Netz ist das
    sqrt(N)-Glied fuer drei Regeln gleicher Form und verschiedener Volumenzuordnung negativ (-1,46 bis -1,65), darunter
    eine ohne Einbettung definierbare und eine volumentreue". Nicht gedeckt ist "jede kovariante Laengenregel".
- **Grenzen:** eine Schleife, freies masseloses Skalarfeld, euklidisch, feste Punktzahl, eine Kruemmung (positiv,
  homogen). Q ist auf allgemeinen Mannigfaltigkeiten nur bis auf Konventionen der Ordnung h^2 Riem definiert (Wahl des
  geodaetischen Simplex). Die Nebenlesart Gs ist eine Regelmischung und kein Mass fuer G.
- **Naechste Schritte [H]:**
  - (a) G auf einem Netz ohne Splitter: Punktprozess mit Mindestabstand (oder gestoertes Gitter) auf S^4, oder
    intrinsische Delaunay-Umordnung (bistellare Flips) bezueglich der geodaetischen Laengen. Erst dann ist K2-1
    entscheidbar.
  - (b) Die Gs-Beobachtung als eigene Frage: Wie stark haengt Gamma an fast entarteten Simplizes? Etwa C gegen
    "C mit kuenstlich gedrueckten Splittern" auf denselben Netzen.
  - (c) Weiter offen aus INDUZIERT-KUGEL-1: die Torus-Diskrepanz (c = +0,111 gegen kovariant erwartete -0,14).

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-123327, EINGEFROREN-SHA256.txt.
- code/: kugel2.py (Regeln Q, G, Gs, Einbettung, Quadratur, Kontrollen), auswertung_kugel2.py (Tor, Fits, Urteile);
  unveraendert kopiert kugel.py, auswertung_kugel.py, dichte4d.py, induziert.py, zufall2d.py; je mit Kopie
  *.eingefroren-20261004-123327.
- rauch-69/: kontrolle.json/.log, rauch-a/-b (blind) .json/.log, probe/ (Codeprobe, Werte ungelesen), probe-4.log,
  probe-aw.log.
- lauf-69/: kontrolle.json/.log; messung-n4-N<N>-s<saat0>.json/.log (19 Laeufe); auswertung.json (Urteile, Fits,
  Differenzen, K2-0-Vergleich je Netz, beschreibende Tabellen), auswertung.log; PRUEFSUMMEN.txt (.69, 42 Dateien,
  lokal geprueft).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde40-induziert-kugel2/ (code/, rauch/, lauf/).

## 9. Einfach gesagt

Letztes Mal kam auf einem zufaelligen Punktnetz auf einer vierdimensionalen Kugel Einsteins Vorzeichen fuer die
Schwerkraft heraus, aber mit zwei Regeln fuer die Kantenlaengen, die nur auf der Kugel sauber sind, und mit einer grossen
Umrechnung. Jetzt haben wir eine Regel genommen, bei der jedes Baustueck genau so viel Volumen hat wie das Kugelstueck,
das es abdeckt; sie braucht keine Umrechnung und kommt ohne die Einbettung aus. Auch sie gibt deutlich Einsteins
Vorzeichen, in allen 40 Wiederholungen. Die zweite neue Regel, echte Kugelabstaende als Kantenlaengen, laesst sich
dagegen gar nicht bauen: Einige Prozent der Baustuecke sind so flach, dass es mit diesen Laengen kein echtes Baustueck
gibt, und ein Notbehelf verfaelscht das Ergebnis staerker, als das Signal gross ist. Ob das Vorzeichen auch bei einer
Regel haelt, die die Form der Baustuecke aendert, ist deshalb noch offen.
