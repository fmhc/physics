# INDUZIERT-XI-KUGEL-1: Ergebnis (Runde 40/41, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 13:09:19 CEST. code/xi_kugel.py und code/auswertung_xi.py bis 13:26:59 CEST, Kontrolle und
    Rauchlaeufe 11:27:06 bis 11:29:36 UTC, Codeprobe 11:29:12 bis 11:29:23 UTC, Plantext ab 13:30:08 CEST.
  - Eingefroren 13:32:30 CEST: PLAN.md.eingefroren-20261004-133230, Code-Kopien *.eingefroren-20261004-133230,
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 11:32:42 bis 11:54:56 UTC (1 Kontrolle, 12 Messlaeufe, alle rc 0), Auswertung 11:55:26 bis 11:55:27 UTC
    (rc 0). Text ab 13:57:47 CEST.
- Code nach dem Einfrieren unveraendert: sha256 von xi_kugel.py (178b8188...), auswertung_xi.py (87df598b...) und der
  sechs unveraendert kopierten Dateien auf der .69 vor der Auswertung gleich den eingefrorenen. lauf-69/PRUEFSUMMEN.txt
  (.69, 28 Dateien) lokal nachgeprueft: 28 von 28 gleich. Laufdateien von INDUZIERT-KUGEL-1 (Torus) und
  INDUZIERT-KUGEL-2 (XI0) vor der Auswertung gegen deren PRUEFSUMMEN.txt geprueft: 44 von 44 und 42 von 42 gleich.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu3, cpu4, cpu5).
  Euklidisch, eine Schleife, freies Skalarfeld (P1) mit Kruemmungsglied, synthetisch, keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [E] hier gerechnet, [ES] eigener Schluss, [F] Festlegung im Plan,
  [K] Kartenpunkt, [H] Hypothese, [L] Literatur aus dem Gedaechtnis.
- **Konvention (wie INDUZIERT-KUGEL-1/-2):** Regel Q (volumentreu je Simplex), Fassung roh. y(N) = (Gamma_Kugel -
  Gamma_Torus)/sqrt(N), je Saat y = beta + delta/sqrt(N) ueber N = 1000 bis 8000, beta = Saatmittel, SE aus der
  Saatstreuung (40 Saaten, dieselben wie KUGEL-1/-2). beta < 0 heisst Einsteins Vorzeichen. Operator K + xi R M mit
  R = 12/a^2 und konzentrierter Masse M = diag(m_i); fuer xi > 0 ist das Glied der frueheren Nullmode,
  1/2 ln(xi R V_R/N), je Netz exakt abgezogen (PLAN S2). gamma = d beta/d xi (gepaart je Saat), xi* = -beta(0)/gamma.

## 1. Ergebnis zuerst

1. **Das Einstein-Vorzeichen kippt auf dem S^4-Netz nicht bei xi = 1/6, sondern erst bei xi* = 0,555 +- 0,018 [E].**
   beta(xi) = -1,613 / -1,370 / -1,127 / -0,886 fuer xi = 0 / 1/12 / 1/6 / 1/4 (je +- 0,052); bei jedem xi sind alle 40
   Saaten einzeln negativ. Steigung gamma = 2,905 +- 0,004 (gepaart, 722 SE), linear bis auf 0,0005. xi* liegt 22 SE
   ueber 1/6. **XI2 und XI3 nicht eingetroffen.** Bei der konformen Kopplung ist beta(1/6) = -1,127 +- 0,052 (-21,7 SE).
2. **Lesart [M, ES]:** gamma = 30,78 g0 misst das Netzmoment g0 = Tr'(K^-1 M)/N = 0,094 (16 % unter dem scharfen
   Modenschnitt 0,1125). Ein Eigenzeit-Regler mit diesem Moment gaebe beta(0) = -gamma/6 = -0,484; das Netz gibt -1,613,
   also das 3,3-Fache (= 6 xi*). Nimmt man g0 als Reglermoment, stammen rund 70 % des Einstein-Glieds des minimal
   gekoppelten Netz-Skalars nicht aus dem 1/6-Stueck, sondern aus gitterspezifischen O(h^2 R)-Anteilen (mit dem Moment
   der konsistenten Masse 87 %).
3. **xi* haengt an der Diskretisierung des Massenglieds [E, K5]:** Mit konsistenter P1-Masse ist gamma_k = 1,291 +- 0,002
   (0,44 der konzentrierten) und xi*_k = 1,25 +- 0,04. Beide Lesarten liegen weit ueber 1/6 und ueber 1/4; mit Gamma_M
   statt Gamma ist xi*_M = 0,521 +- 0,018. "xi*" ist eine Eigenschaft von Netz plus Massendiskretisierung.
4. **Kontrollen [E]:** XI0 eingetroffen (160 von 160 Netzen bitgleich, beta(0) = -1,612574487200885 wie KUGEL-2).
   XI1 eingetroffen, war aber vorab praktisch entschieden [K2]; die strenge gepaarte Linearitaetsprobe verfehlt (Reste
   +-0,0005 bei gepaarter SE 5e-6, Muster konkav wie von den ln-N-Gliedern erwartet). Die Nullmode verschiebt beta genau
   um -b0/4 (-0,009698 gegen -0,009696); ein freier ln-N-Fit (F3) gibt dieselben ln-Koeffizienten wie das Kontinuum und
   xi* = 0,558 +- 0,020.
5. **Bedeutung, wie vorab auf der Karte festgelegt:** "XI2 verfehlt: Das Netz-B ist gitterspezifisch; das Vorzeichen fuer
   einen Materietyp ist eine Eigenschaft dieses Netzes, nicht des Kontinuums (wie INDUZIERT-G-L allgemein erwartet)."
   **Ausgeloest.** Zusatz aus [K5]: Das gilt fuer beide natuerlichen Massendiskretisierungen.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch code/auswertung_xi.py; Werte in lauf-69/auswertung.json.
**Tor bestanden:** 40 von 40 Saaten bei allen vier N gueltig (160 Kugelnetze, je fuenf LU ok: xi = 0, 1/12, 1/6, 1/4 und
konsistente Masse; Torus aus INDUZIERT-KUGEL-1 gueltig), keine Saat ausgeschlossen oder unvollstaendig.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| XI0 | Kontrolle: beta(0) bitgleich mit KUGEL-2 (Regel Q) | 90 % | **eingetroffen** | **eingetroffen** | Gamma_Q(0) in 160 von 160 Netzen == KUGEL-2 (groesste Abweichung 0,0; ebenso Gamma_M, Summe ln m, V, korr, korr_M, lam_min, a, V_K, F); beta(0) = -1,612574487200885, SE und jedes beta_j == Fit der KUGEL-2-Daten und == gespeicherter KUGEL-2-Wert |
| XI1 | beta(xi) steigt (gamma > 0 mit >= 3 SE) und ist linear (Rest <= 2 SE je Punkt) | 75 % | **eingetroffen** | **eingetroffen** | gamma = 2,9047 +- 0,0040 (722 SE); Reste -0,00048 / +0,00046 / +0,00052 / -0,00050 bei SE je Punkt 0,052 (hoechstens 0,010 SE). Vorab praktisch entschieden [K2]. Strenge gepaarte Probe: nicht linear (87 bis 101 gepaarte SE) |
| XI2 | [H] xi* in [0,10; 0,25] | 40 % | **nicht eingetroffen** | **nicht eingetroffen** | xi* = 0,5552 +- 0,0177 (Jackknife 0,0177); kein Grenzfall. Alle Lesarten ausserhalb: 0,555 bis 0,562 (Fassungen), 0,558 (F3), 0,521 (Gamma_M), 1,249 (konsistente Masse) |
| XI3 | [H] xi* in [0,133; 0,200] | 25 % | **nicht eingetroffen** | **nicht eingetroffen** | xi* - 1/6 = 0,389 = 22,0 SE |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "XI2 verfehlt: Das Netz-B ist gitterspezifisch; das Vorzeichen fuer einen Materietyp ist eine Eigenschaft dieses
    Netzes, nicht des Kontinuums (wie INDUZIERT-G-L allgemein erwartet)": **ausgeloest.**
  - "XI3 trifft ein: ... Gitter-Regler wie Eigenzeit-Regler": nicht ausgeloest.
  - "XI1 verfehlt: ... Lesart von beta als R-Koeffizient zu pruefen": nicht ausgeloest (beta reagiert linear und mit
    festem Vorzeichen der Steigung auf das Massenglied).

**Agenten-Vorhersagen** (PLAN Abschnitt 9, nach Kontrolle und Rauchlauf, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (95 %) | Tor ohne Ausschluss | **eingetroffen** |
| A2 (90 %) | XI0 eingetroffen | **eingetroffen** |
| A3 (97 %) | XI1 eingetroffen | **eingetroffen** |
| A4 (60 %) | Strenge gepaarte Linearitaetsprobe verfehlt | **eingetroffen** (Reste 87 bis 101 gepaarte SE) |
| A5 (65 %) | xi* in [0,25; 0,50] | **nicht eingetroffen** (0,555) |
| A6 (25 %) | XI2 eingetroffen | nicht eingetroffen |
| A7 (7 %) | XI3 eingetroffen | nicht eingetroffen |
| A8 (80 %) | gamma_k < gamma, also xi*_k > xi* | **eingetroffen** (gamma_k/gamma = 0,444; xi*_k = 1,25) |
| A9 (55 %) | F3: freie ln-Koeffizienten innerhalb 2 SE von -1/4 + xi - 3 xi^2 | **eingetroffen** (0,3 / 0,05 / 0,2 SE) |

## 3. Tabellen

### 3.1 beta je xi [E]

(Hauptfassung, Regel Q, Gamma, roh; je Saat y = beta + delta/sqrt(N); Mittel +- SE, M = 40; WLS = Fit auf die Mittelwerte
je N, chi^2 bei 2 Freiheitsgraden; "neg" = Saaten mit beta_j < 0)

| xi | beta | Std je Saat | delta | WLS beta (chi^2, p) | Bereich beta_j | neg |
|---|---|---|---|---|---|---|
| 0 (= KUGEL-2) | **-1,6126 +- 0,0524** | 0,331 | -1,3 +- 2,6 | -1,620 +- 0,054 (2,47; 0,29) | -2,31 bis -1,01 | 40 |
| 1/12 | **-1,3696 +- 0,0522** | 0,330 | -0,5 +- 2,6 | -1,377 +- 0,053 (2,48; 0,29) | -2,06 bis -0,77 | 40 |
| 1/6 | **-1,1275 +- 0,0521** | 0,329 | -0,1 +- 2,6 | -1,135 +- 0,053 (2,49; 0,29) | -1,81 bis -0,53 | 40 |
| 1/4 | **-0,8864 +- 0,0519** | 0,328 | +0,1 +- 2,6 | -0,894 +- 0,053 (2,50; 0,29) | -1,56 bis -0,29 | 40 |
| 1/6, konsistente Masse | -1,3974 +- 0,0523 | 0,331 | -0,8 +- 2,6 | -1,405 +- 0,053 (2,47; 0,29) | -2,09 bis -0,80 | 40 |
| 0, Gamma_M (= KUGEL-2) | -1,5122 +- 0,0545 | 0,345 | -0,2 +- 2,8 | -1,519 +- 0,060 (2,41; 0,30) | -2,21 bis -0,75 | 40 |

- Teilbereiche (beschreibend): ohne N = 1000 -1,554 / -1,311 / -1,069 / -0,828, ohne N = 8000 -1,585 / -1,342 / -1,099 /
  -0,858 (xi = 0 / 1/12 / 1/6 / 1/4, SE 0,08 bzw. 0,09); Dreiparameterfit -1,48 / -1,24 / -1,00 / -0,75 (SE 0,36). Die
  Abstaende zwischen benachbarten xi liegen in allen diesen Fits bei 0,240 bis 0,243 je 1/12.

### 3.2 Steigung, Linearitaet und xi* [E]

| Lesart | gamma (gepaart) | xi* +- SE (Delta; Jackknife) | Reste der Geraden (xi = 0 / 1/12 / 1/6 / 1/4) | in SE je Punkt / gepaarter SE |
|---|---|---|---|---|
| **Haupt (Plan): Nullmode abgezogen** | **2,9047 +- 0,0040** | **0,5552 +- 0,0177 (0,0177)** | -0,00048 / +0,00046 / +0,00052 / -0,00050 | <= 0,010 / 87 bis 101 |
| ohne Nullmoden-Abzug (null_drin) | 2,8698 +- 0,0040 | 0,5619 +- 0,0179 | +0,0024 / -0,0034 / -0,0005 / +0,0014 | <= 0,065 / bis 641 |
| zusaetzlich (xi - 3 xi^2) ln N abgezogen (log_voll) | 2,8950 +- 0,0040 | 0,5570 +- 0,0177 (mit gamma_kont: 0,5559) | +0,00033 / -0,00034 / -0,00029 / +0,00031 | <= 0,007 / 57 bis 64 |
| F3: freier ln-N-Fit auf die gepaarten Differenzen | 2,890 +- 0,026 | 0,558 +- 0,020 | -0,00023 / +0,00025 / +0,00019 / -0,00021 | <= 0,005 / - |
| Gamma_M (gleiche Steigung, PLAN S8) | 2,9047 +- 0,0040 | 0,5206 +- 0,0183 | wie Haupt | - |
| konsistente Masse, Steigung aus (0; 1/6) | 1,2911 +- 0,0016 | 1,249 +- 0,040 | - | - |

- Gerade der Hauptfassung: Achsenabschnitt -1,6121, Nullstelle 0,5550 (gegen xi* = 0,5552 aus dem gemessenen beta(0)).
  Korrelation von beta_j(0) und gamma_j je Saat: -0,51.
- Sekanten je 1/12: 0,2430 / 0,2421 / 0,2410 (beta(1/12) - beta(0), usw.); zweite Differenzen je Saat -0,000894 +-
  0,000011 und -0,001069 +- 0,000010, also d^2 beta/d xi^2 etwa -0,13 bis -0,15. Das ln-N-Glied des Kontinuums
  (-3 xi^2 mal b0) liesse -0,23 erwarten; gemessen ist 55 bis 66 % davon. log_voll zieht also etwas zu viel ab (Reste
  kippen auf konvex).
- Nullmoden-Glied: null_drin - haupt = -0,0096983 +- 1,4e-8 bei jedem xi > 0, erwartet -b0/4 = -0,0096964 (Rest aus
  1/2 ln(V_R/N)); Steigungsverschiebung -0,0349, wie in PLAN S2 vorhergesagt (-0,035).
- Konsistente Masse bei xi = 1/6: beta_k - beta = -0,2699 +- 0,0004 (gepaart).

### 3.3 Zuwachs y(xi) - y(0) je N [E]

(Hauptfassung; Mittel ueber 40 Saaten, in Klammern Std je Saat)

| xi | N = 1000 | 2000 | 4000 | 8000 | beta-Differenz (N -> unendlich) |
|---|---|---|---|---|---|
| 1/12 | 0,2678 (0,0025) | 0,2607 (0,0014) | 0,2555 (0,0011) | 0,2517 (0,0008) | 0,2430 |
| 1/6 | 0,5242 (0,0049) | 0,5130 (0,0028) | 0,5049 (0,0023) | 0,4988 (0,0015) | 0,4851 |
| 1/4 | 0,7710 (0,0073) | 0,7583 (0,0041) | 0,7489 (0,0034) | 0,7418 (0,0023) | 0,7261 |
| 1/6, konsistent | 0,2321 (0,0019) | 0,2275 (0,0011) | 0,2239 (0,0009) | 0,2210 (0,0006) | 0,2152 |

- Der Zuwachs waechst wie sqrt(N) mit einer kleinen Korrektur delta/sqrt(N) (N-freie IR-Glieder, die nur von
  m^2 a^2 = 12 xi abhaengen; PLAN S5). Seine Streuung je Saat faellt etwa wie 1/sqrt(N) (PLAN S9); daher die kleine
  SE(gamma).

### 3.4 Freie ln-N-Koeffizienten (F3) [E]

(Dreiparameterfit beta + g ln N/sqrt(N) + delta/sqrt(N) je Saat auf y(xi) - y(0) ohne Nullmoden-Abzug)

| xi | g frei | erwartet (Kontinuum, -1/4 + xi - 3 xi^2) | Abstand |
|---|---|---|---|
| 1/12 | -0,207 +- 0,063 | -0,1875 | 0,3 SE |
| 1/6 | -0,173 +- 0,124 | -0,1667 | 0,05 SE |
| 1/4 | -0,158 +- 0,184 | -0,1875 | 0,2 SE |

### 3.5 Netze, LU, Zeiten [E]

| | N = 1000 | 2000 | 4000 | 8000 |
|---|---|---|---|---|
| Kugelradius a | 2,483 | 2,953 | 3,511 | 4,175 |
| Simplizes je Netz F | 27 456 | 57 356 | 118 249 | 241 679 |
| V_Q/V_K - 1 | 1,8e-4 | 5,8e-5 | 1,9e-5 | 6,6e-6 |
| Nullmoden-Glied 1/2 ln(xi R V_R/N), xi = 1/12 / 1/6 / 1/4 | -0,909 / -0,563 / -0,360 | -1,083 / -0,736 / -0,533 | -1,256 / -0,909 / -0,707 | -1,429 / -1,083 / -0,880 |
| LU je xi | 0,06 s | 0,32 s | 1,9 s | 12,6 s |
| Laufzeit je Saat (Netz und fuenf LU) | 1,4 s | 4,2 s | 14,8 s | 74,6 s |
| kleinstes U_ii (xi > 0) | 3,29 | 3,30 | 2,91 | 2,81 |

- Nullmoden-Glied zwischen N = 1000 und 8000: -0,520 = -1/4 ln 8, wie PLAN S2. RSS bis 865 MB.

## 4. Kontrollen

- **Tor (PLAN Abschnitt 5):** bestanden (Abschnitt 2).
- **XI0 (Reproduktion):** 160 von 160 Netzen bitgleich in Gamma_Q(0), Gamma_M, Summe ln m, V, korr, korr_M, lam_min, a,
  V_K und F; der Fit reproduziert -1,612574487200885 (Mittel, SE und alle 40 beta_j gleich, auch gegen die gespeicherte
  KUGEL-2-Auswertung).
- **Kontrolllauf lauf-69/kontrolle.json (11:32:49 bis 11:32:51 UTC, cpu5, rc 0), alle Schwellen erfuellt, Werte gleich
  dem Kontrolllauf vor dem Einfrieren:**
  - KX0: Gamma_Q(0), Gamma_M, Summe ln m, V, korr, lam_min ueber den eigenen Weg gleich (==) kugel2.eine_messung (S^4,
    N = 400, Saat 990; dort laufen vorher C und S).
  - KX1: duenne LU gegen dicht (slogdet) <= 1,7e-13 fuer alle xi und beide Massen.
  - KX2: exakte Nullmoden-Identitaet (PLAN S2) gegen die dichten verallgemeinerten Eigenwerte <= 8,1e-14; mu_0 = 2,9e-14
    (konzentriert) und 1,6e-13 (konsistent).
  - KX3: monoton und konkav. KX4: mit Nullmoden-Abzug 6,9e-8 bei xi = 1e-9, ohne 9,80 (Negativprobe schlaegt an).
  - KX5: Summe m = V_R (0,0), Zeilensumme M_k = m (7,9e-16), 1^T M_k 1 = V_R (0,0), R a^2 = 12,0, M_k symmetrisch und
    positiv definit (kleinster Eigenwert 0,039).
  - KX6: Skalierung mit 1,37: Gamma~(xi) - Gamma(0) unveraendert (1,1e-13), Gamma(0) um (N-1) ln 1,37 verschoben
    (1,8e-11).
- **In jedem Netz (160):** Formpruefung erfuellt (Gamma(0) < Gamma~(1/12) < Gamma~(1/6) < Gamma~(1/4), konkav;
  Gamma~_k(1/6) > Gamma(0)); Massenproben <= 1,6e-15; R a^2 - 12 <= 1,8e-15.
- **Nullmoden-Verschiebung:** -0,0096983 gegen -b0/4 = -0,0096964 (Abweichung 1,9e-6 <= 1e-4).
- **Modellprobe:** WLS chi^2 = 2,47 bis 2,50 bei 2 Freiheitsgraden (p = 0,29) fuer jedes xi.
- Aus INDUZIERT-KUGEL-1 gelten weiter KA bis KG fuer den unveraenderten Code (P1, LU, Gamma_M, Netzpruefungen,
  Negativproben); aus KUGEL-2 KQ1 bis KB2 fuer die Regel Q.

**Latten (v3):**
- **L1 (kann scheitern):** XI2 und XI3 konnten eintreffen (das Fenster XI2 ist breit), XI0 konnte an der Bitgleichheit
  scheitern, die strenge Linearitaetsprobe konnte bestehen oder scheitern. XI1 konnte praktisch nicht scheitern [K2].
- **L2 (Gegenprobe):** drei Fassungen des Fits, freier ln-N-Fit, zwei Massen, Gamma und Gamma_M, Delta-Methode gegen
  Jackknife, Zuwachs je N, LU gegen dicht, exakte Identitaet gegen Eigenwerte.
- **L3 (Numerik):** log det etwa 1e-13 absolut (KX1, KX2); SE(gamma) 0,004, SE(xi*) 0,018.
- **L4 (schon bekannt):** Kontinuum: Koeffizient (1/6 - xi) mal Reglermoment (Visser 2002, ueber das Dossier [S]);
  Reglerabhaengigkeit des induzierten G (Dossier); zeta(0) = -1/90 des konform gekoppelten Skalars auf S^4 [L]. Eine
  Gittermessung von xi* auf S^4-Zufallsnetzen kenne ich nicht; nicht gesucht [L?].
- **L5 (Messbezug):** keiner (4D euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] Regel Q steht in kugel2.py:** benutzt; XI0 bitgleich, also derselbe Weg wie KUGEL-2.
- **[K2] XI1 praktisch vorab entschieden:** bestaetigt. gamma liegt 722 SE ueber null, die Reste bei 0,01 SE je Punkt.
  Die strenge gepaarte Probe verfehlt mit 87 bis 101 SE; sie misst die ln-N-Glieder des Fitmodells (Muster konkav wie
  erwartet, PLAN S5), nicht den R-Koeffizienten.
- **[K3] Nullmode:** exakter Abzug; Verschiebung genau -b0/4; der freie Fit F3 findet die ln-Koeffizienten des Kontinuums
  (Abschnitt 3.4) und dasselbe xi* (0,558 +- 0,020). Kein Einfluss auf ein Urteil.
- **[K4] Fenster XI3:** ohne Folge (xi* = 0,555).
- **[K5] Massendiskretisierung:** xi* = 0,555 (konzentriert) gegen 1,249 (konsistent); gamma_k/gamma = 0,444. Der
  Bedeutungssatz zu XI3 haette nur fuer die gewaehlte Masse gegolten; XI2 verfehlt in beiden.
- **[K6] Torus-Referenz:** fair fuer die Frage der Karte; gamma ist ein Flachraum-Moment des Netzes (g0 = 0,094).
- **[K7] beta(0) in xi*:** gemessener Wert; die Nullstelle der Geraden (0,5550) weicht um 0,0002 ab.
- **[K8] 40 Saaten:** wie geplant.

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:** keine Gamma-Werte, Mittelwerte oder Vorzeichen der Messgroesse (Rauchdateien blind,
   per jq geprueft). Gesehen habe ich: die Kontrollabweichungen, Gueltigkeit, Zeiten, Volumen- und Massenproben, die
   Formpruefung (Wahrheitswerte) und von der Codeprobe nur Struktur und Kontrollfelder (M = 3, Tor, XI0-Wahrheitswerte,
   Formzaehlung).
2. **Kontrollwert KX4 als Hinweis auf gamma:** 6,9e-8 bei xi = 1e-9 (N = 400) entspricht grob Summe' 1/mu etwa 45 gegen
   etwa 47 beim scharfen Modenschnitt, also einem g0 nahe 0,11. Ich habe das vor den Agenten-Vorhersagen A5 bis A7
   gesehen und im PLAN (Abschnitt 10) offengelegt; der Wert liegt im numerischen Rauschen der LU nahe der Singularitaet.
   Die Schaetzung PLAN S3' (xi* etwa 0,25 bis 0,5) stand vorher. Gemessen ist g0 = 0,094, also noch steifer; A5 verfehlt.
3. **Schreibtischfehler S3':** Ich hatte aus der Spur je Punkt (mittlerer Eigenwert 6,7 fuer regulaere Simplizes) ein
   weicheres Spektrum und g0 etwa 0,2 erwartet. Die Spur sagt wenig ueber das Mittel von 1/mu; gemessen ist g0 = 0,094,
   16 % unter dem scharfen Modenschnitt.
4. **Zeitfolge:** Code mit Operator, Massenwahl, Nebenlesarten, Nullmoden-Abzug, Fit, Tor und Urteilsregeln bis 13:26:59
   CEST, Kontrolle ab 13:27:06 CEST, Plantext ab 13:30:08 CEST, also nach dem Start von Kontrolle und Rauchlauf. Die
   Zeitregel fuer die Saatzahl stand vorher nur in meinen Notizen, im PLAN erst nach dem Rauchlauf (wie in KUGEL-2).
5. **ERGEBNIS-Entwurf:** Um 13:36 CEST habe ich ERGEBNIS.md nur mit Kontrollteilen angelegt (keine Messwerte); diese
   Fassung ersetzt ihn.
6. **Nach dem Einfrieren:** kein Code geaendert. Die Laufprotokolle enthalten keine Gamma-Werte. Eine Ueberwachung
   (Monitor-Werkzeug) hat alle 60 s per ssh die Zeilen "ende", Fehler und "gueltig False" der Logs abgefragt (13:33 bis
   13:55 CEST). Messwerte habe ich erst in auswertung.json gesehen.
7. **ssh-Verbindungen:** drei Spurketten und hoechstens eine kurze Abfrage zugleich, also hoechstens vier.
8. **Auf der .69 ausserhalb des Starters:** mkdir, ls, cat, grep, head, tail, wc, sha256sum (auch -c), date, uptime,
   nproc, free. Kein Python ausserhalb des Starters.
9. **Lokal:** kein python, awk oder perl. Benutzt: jq, sed (nur Lesen), grep, sha256sum, date, ssh, scp, cp, mkdir, ls,
   cat, cut, head, tail, wc, sort, comm, printf und sleep in Warteschleifen. Nichts geloescht.
10. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
    unter /tmp/claude-1000/.../tasks/ an (nur Rueckgabecodes, Endzeilen und Laufmeldungen).
11. **Gelesen vor dem Plan:** KUGEL-2/lauf-69/auswertung.json per jq (beta_Q,roh, b0, beta_Q,M); diese Werte standen
    schon in Karte und ERGEBNIS von KUGEL-2.
12. **Zeitbox:** Start 13:09:19 CEST, Text bis auf die Endpruefung fertig 14:01:43 CEST (date), also 52 min von 120.

## 7. Bedeutung

- **Was gezeigt ist [E]:**
  - Auf den 40 S^4-Saaten von KUGEL-1/-2 verschiebt ein Kruemmungsglied xi R phi^2 das sqrt(N)-Glied linear,
    beta(xi) = -1,613 + 2,905 xi (Reste 0,0005). Bis xi = 1/4 bleibt es in jeder Saat negativ; die Nullstelle liegt bei
    xi* = 0,555 +- 0,018 (konzentrierte Masse) bzw. 1,25 +- 0,04 (konsistente Masse).
  - Die Steigung ist das Flachraum-Moment g0 des Netzes (0,094 bzw. 0,042), die freien ln-Koeffizienten stimmen mit dem
    Kontinuum ueberein.
- **Was ich daraus schliesse [M, ES]:**
  - Im Kontinuum gilt fuer jeden Regler, der eine Funktion des vollen Operators ist, beta(0) = -gamma/6, also xi* = 1/6.
    Auf dem Netz ist beta(0) das 3,3-Fache (konzentrierte Masse) bzw. 7,5-Fache (konsistente Masse) dieses Werts. Der
    Netz-Regler behandelt Kruemmung und Massenglied also verschieden; der groessere Teil des Einstein-Glieds kommt aus den
    O(h^2 R)-Anteilen des Netzes (Laengenregel, Simplexform), die das Dossier als "xi_eff" bezeichnet.
  - Eine natuerliche P1-Diskretisierung mit xi* = 1/6 muesste g0 = 0,31 haben, das 3,3-Fache der konzentrierten Masse.
    Die konzentrierte Masse ist bereits die im UV schwerere der beiden natuerlichen Wahlen (die konsistente verringert
    g0 auf das 0,44-Fache). gamma ist linear in M; selbst die Mischung 2 M_konz - M_kons (gleiche Zeilensumme, positiv
    definit) gaebe nur gamma = 2 mal 2,905 - 1,291 = 4,52 und xi* = 0,36. Ich sehe keine naheliegende Diskretisierung,
    die 1/6 erreicht [ES].
  - Fuer das Projekt: Das Einstein-Vorzeichen auf dem S^4-Netz (KUGEL-1/-2) ist robust gegen ein Kruemmungsglied bis
    xi = 1/4, aber es ist kein Abbild des Kontinuums mit Eigenzeit-Regler. Fuer einen Materietyp ist es eine Eigenschaft
    von Netz plus Diskretisierung, wie das Dossier INDUZIERT-G-L allgemein erwartet.
- **Grenzen:** eine Schleife, freies Skalarfeld, euklidisch, feste Punktzahl, eine Geometrie (S^4, R konstant, also
  xi R = Masse). Eine Kopplung an ortsabhaengige Kruemmung ist auf S^4 nicht trennbar. Nur Regel Q; C und S nicht mit
  xi gerechnet. Konsistente Masse nur bei xi = 1/6 (Steigung aus zwei Punkten). Die Zerlegung "1/6-Stueck gegen
  Gitteranteil" setzt voraus, dass g0 das Reglermoment ist; mit der konsistenten Masse faellt sie anders aus.
- **Naechste Schritte [H]:**
  - (a) Ein Netz, auf dem xi R nicht nur eine Masse ist: S^4 mit konformer Verbiegung oder S^2 x S^2; dort trennt sich
    die Kruemmungskopplung vom Massenglied.
  - (b) Dieselbe Messung fuer die Regeln C und S (gleiche Netze, eine Laufrunde): Haengt gamma an der Laengenregel kaum
    (Flachraum-Moment), beta(0) aber deutlich, verschiebt sich xi* entsprechend.
  - (c) Das 1/6-Stueck des Netzes direkt messen: Waermeleitungsspur Tr exp(-s M^-1 K) auf S^4 gegen T^4 bei
    mittleren s; ihr R-Koeffizient ist der Eigenzeit-Anteil, der Rest von beta(0) der Gitteranteil [H].

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-133230, EINGEFROREN-SHA256.txt.
- code/: xi_kugel.py (Operator, Nullmode, konsistente Masse, Kontrollen KX0 bis KX6), auswertung_xi.py (Tor, Fits,
  Steigung, xi*, Nebenlesarten, Urteile); unveraendert kopiert kugel.py, kugel2.py, auswertung_kugel.py, dichte4d.py,
  induziert.py, zufall2d.py; je mit Kopie *.eingefroren-20261004-133230.
- rauch-69/: kontrolle.json/.log, rauch-a/-b (blind) .json/.log, probe/ (Codeprobe; nur Struktur und Kontrollfelder
  gelesen), probe-4.log, probe-aw.log.
- lauf-69/: kontrolle.json/.log; messung-n4-N8000-s<saat0>.json/.log (8 Laeufe), messung-n4-N4000-s0/-s14/-s27,
  messung-n4-N2000-1000-s0 (.json/.log); auswertung.json (Urteile, Fits, Fassungen, Nebenlesarten, XI0 je Netz,
  beschreibende Tabellen), auswertung.log; PRUEFSUMMEN.txt (.69, 28 Dateien, lokal geprueft).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde40-induziert-xi/ (code/, rauch/, lauf/).

## 9. Einfach gesagt

Ein schwingendes Feld auf einem zufaelligen Punktnetz auf einer vierdimensionalen Kugel erzeugt eine Art Schwerkraft,
und die hatte in den letzten Rechnungen Einsteins Vorzeichen. In der Theorie ohne Netz gibt es eine bestimmte Staerke
1/6 fuer eine Zusatzkopplung des Felds an die Kruemmung, bei der dieser Effekt genau verschwindet. Wir haben diese
Kopplung auf dem Netz schrittweise eingeschaltet: Der Effekt wird gleichmaessig schwaecher, verschwindet aber erst bei
etwa 0,56 statt bei 1/6, und schreibt man das Zusatzglied auf eine andere, ebenso erlaubte Art, sogar erst bei 1,25.
Das Einstein-Vorzeichen des Netzes stammt also nach unserer Lesart zum groessten Teil aus Eigenheiten des Netzes und
nicht aus dem Mechanismus, den die Theorie ohne Netz dafuer vorsieht.
