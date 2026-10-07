# INDUZIERT-XI-KUGEL-1: Plan (Code-Agent, Runde 40/41)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 13:09:19 CEST (date). Code (code/xi_kugel.py,
  code/auswertung_xi.py) geschrieben bis 13:26:59 CEST (date beim Hochladen), Kontrolle und Rauchlaeufe ab 11:27:06 UTC
  (.69, = 13:27:06 CEST), Codeprobe 11:29 UTC, Plantext ab 13:30:08 CEST (date).
- **Grundlage:** KARTE.md (XI0 bis XI3, Wahrscheinlichkeiten und Bedeutungssaetze unveraendert, Abschnitt 6);
  RUNDE-37/induziert-kugel-2/ (PLAN, ERGEBNIS, code/, lauf-69/auswertung.json: beta_Q,roh = -1,6126 +- 0,0524, M = 40,
  b0 = 0,03879); RUNDE-37/induziert-kugel-1/ (ERGEBNIS, code/kugel.py); RUNDE-37/kugel-gegenlesen/GEGENLESEN.md;
  RUNDE-37/induziert-g-l/DOSSIER.md Abschnitte 1, 6, 8.
- **Code:** code/xi_kugel.py und code/auswertung_xi.py (neu). Unveraendert kopiert und importiert (sha256 gleich den
  eingefrorenen Fassungen von INDUZIERT-KUGEL-2): kugel.py (c2a4d790...), kugel2.py (15dcbd85...), auswertung_kugel.py
  (5b0a7126...), dichte4d.py (2881048e...), induziert.py (b3867eac...), zufall2d.py (37a0fe8f...).
- **Kennzeichen:** [M] eigene Mathematik, [ES] eigener Schluss (grob), [L] Literatur aus dem Gedaechtnis, [F] Festlegung
  dieses Plans, [K] Kartenpunkt (vor dem Einfrieren offengelegt), [H] Hypothese, [E] in Kontrolle oder Rauchlauf gerechnet
  (blind: keine Gamma-Werte).
- **Bezeichnungen:** a^2 = 0,19492 sqrt(N) (Dichte 1), R = 12/a^2 = 61,56/sqrt(N), Int R = 61,56 sqrt(N).
  y(N) = (Gamma_Kugel - Gamma_Torus)/sqrt(N), je Saat y = beta + delta/sqrt(N) (Fit wie KUGEL-1). Die OLS-Gewichte des
  Achsenabschnitts ueber N = 1000, 2000, 4000, 8000 sind (-0,727; 0,068; 0,631; 1,028) [M]; ein Glied g ln N/sqrt(N) in y
  verschiebt beta um g b0 (b0 = 0,03879), ein Glied e/N um -4,1e-4 e.

## 1. Schreibtisch (vor jeder Messung)

| Nr | Punkt | Befund |
|---|---|---|
| S1 | Operator [Karte, F] | A(xi) = K + xi R M auf S^4, K = P1-Steifigkeit der Regel Q, R = 12/a^2 exakt (Kugel vom Radius a). **M = konzentrierte P1-Masse diag(m_i), m_i = Summe V_T/5** ("P1-Volumengewichte" der Karte; dieselbe Masse wie Gamma_M in KUGEL-1/-2). Gruende: (i) dieselbe Gewichtung wie in den Vorlaeufen; (ii) diagonal, also gleiche Struktur wie K und eine LU je xi; (iii) exakt fuer Konstanten (M 1 = m, 1^T M 1 = V_R). Die konsistente Masse (exaktes Int phi^2 fuer P1) ist ebenso berechtigt; siehe S7 und Nebenlesart Mk. Torus: R = 0, Referenz unveraendert (Karte) |
| S2 | Nullmode [M] | Der konstante Vektor ist exakter verallgemeinerter Eigenvektor von (A(xi), M) zum Eigenwert xi R (K 1 = 0). Mit den verallgemeinerten Eigenwerten mu_k von (K, M) und det' K = N det K_(0) gilt **exakt** Gamma(xi) = 1/2 ln(xi R V_R/N) + Gamma(0) + 1/2 Summe'_k ln(1 + xi R/mu_k) (Beweis: det(K + eps M) = det M eps Prod'(mu_k + eps), und der Grenzwert eps -> 0 gibt det M Prod' mu_k = (V_R/N) det' K). Das Nullmoden-Glied ist 1/2 ln(xi R V_R/N) = -1/4 ln N + 1/2 ln(12 xi) - 1/4 ln(3/(8 pi^2)) + 1/2 ln(V_R/N), also genau "gamma ln N" mit gamma = -1/4 plus eine N-freie Konstante. **Behandlung [F, K3]:** Gamma~(xi) = Gamma(xi) - 1/2 ln(xi R V_R/N) wird je Netz exakt abgezogen; Gamma~(xi) -> Gamma(0) fuer xi -> 0. Unbehandelt verschoebe es jedes beta(xi > 0) um -b0/4 = -0,0097 (Steigung -0,035, Reste bis 0,004). Ein freier ln-N-Parameter im Fit kostete das 7-fache an SE (KUGEL-1: 0,36 statt 0,052); er laeuft als Nebenlesart F3 mit |
| S3 | Kontinuum und Lesart von gamma [M] | Fuer kleine xi R/mu ist Gamma~(xi) - Gamma(0) = 1/2 xi R Tr'(K^-1 M) + ..., und Tr'(K^-1 M) = Summe' 1/mu_k = N g0 + O(IR), g0 = gemittelter Netz-Propagator am gleichen Punkt (Kontinuum: Lambda^2/(16 pi^2)). Also **gamma = 30,78 g0** (= 61,56/2). Im Kontinuum mit Eigenzeit-Regler ist B(xi) = -(1/6 - xi) g0/2, also beta(0) = -5,13 g0 und xi* = 1/6 genau dann, wenn beta(0) = -gamma/6. Mit beta(0) = -1,613 (KUGEL-2): **XI3 <=> gamma in [8,06; 12,09] <=> g0 in [0,262; 0,393]; XI2 <=> gamma in [6,45; 16,13] <=> g0 in [0,210; 0,524]** |
| S3' | Groessenordnung von g0 [ES, grob, keine Messung] | Scharfer Modenschnitt bei Dichte 1 (Lambda^4 = 32 pi^2, Lambda^2 = 17,77): g0 = 2/Lambda^2 = 0,1125, gamma = 3,46, xi* = 0,47; das ist zugleich H-Kont des Dossiers (beta = -5,13 mal 0,1125 = -0,577). Hyperkubisches Gitter, Abstand 1: g0 = 0,155 [L], gamma = 4,77, xi* = 0,34. P1 auf regulaeren 4-Simplizes mit dem mittleren Volumen der Netze (1/30,2): Spur(M^-1 K)/N = 5 mal 1,6/L^2 = 6,7 (scharfer Schnitt 11,8, hyperkubisch 8); bei gleicher Spektralform waere g0 = 0,20, gamma = 6,1, xi* = 0,26. Splitter erhoehen die Spur. **Erwartung: xi* zwischen etwa 0,25 und 0,5; XI3 verlangte ein 2,3- bis 3,5-fach weicheres Spektrum als der scharfe Schnitt.** Das ist eine Schaetzung, kein Ziel |
| S4 | gamma > 0 [M] | Gamma~(xi) - Gamma(0) = 1/2 Summe' ln(1 + xi R/mu_k) ist in jedem Netz streng steigend und streng konkav in xi (exakt). beta_j ist eine Gewichtssumme der y_j(N) mit einem negativen Gewicht (-0,727 bei N = 1000); weil der Zuwachs je sqrt(N) bis auf O(ln N/sqrt N) N-unabhaengig ist, ist auch die Steigung von beta positiv. **XI1 Teil 1 steht damit vorab fest; scheitern kann er nur durch einen Fehler [K2]** |
| S5 | Linearitaet und ln-N-Glieder [M] | Kontinuum (Waermeleitungskern, universell): zeta(0) von -Box + xi R auf S^4 ist 29/90 + 12 xi^2 - 4 xi fuer xi > 0 (Probe: xi = 1/6 gibt -1/90, den bekannten Wert des konform gekoppelten Skalars; xi = 0 mit Nullmode 29/90 - 1, daraus gamma_kont = 61/360 - 1/4 = -29/360 wie in KUGEL-1). Mit Gamma ⊃ -(zeta(0)/4) ln N folgt fuer Gamma~(xi) - Gamma(0) das Glied (xi - 3 xi^2) ln N, dazu die Nullmode -1/4 ln N (S2). Der Lambda^2-Koeffizient selbst ist exakt linear in xi; Kruemmung entsteht nur ueber ln N (in beta: b0 (xi - 3 xi^2), Steigung +0,0097, Reste +-0,0008) und ueber O(1)-Glieder, die nur von m^2 a^2 = 12 xi abhaengen und in delta fallen. **Erwartete Nichtlinearitaet von beta(xi): etwa 0,001; SE je Punkt etwa 0,05. Die Kartenschwelle "Rest <= 2 SE je Punkt" kann nur bei einer Kruemmung von etwa 0,1 scheitern; XI1 Teil 2 steht damit praktisch vorab fest [K2].** Strenge Nebenprobe: Rest gegen die gepaarte SE der Reste (Streuung je Saat); sie kann an O(1/N)-Gliedern scheitern, deren Groesse ich nicht abschaetzen kann. Nebenfassung log_voll zieht (xi - 3 xi^2) ln N zusaetzlich ab |
| S6 | Ist der masselose Torus fair? [M, ES] | Ja, fuer die Frage der Karte: Auf T^4 ist R = 0, das Glied xi R phi^2 verschwindet dort, und der Vergleich misst den Koeffizienten von Int R fuer den Operator -Box + xi R. Ein Torus mit derselben Masse m^2 = 12 xi/a^2 zoege genau das Glied m^2 V Lambda^2 ab (V_S = V_T = N), und gamma waere bis auf O(1) null; das wuerde "Masse" pruefen, nicht "Kruemmungskopplung". **Einschraenkung der Lesart:** Auf S^4 ist xi R = m^2 konstant; gamma ist deshalb ein reines Flachraum-Moment des Gitters (g0), beta(0) die Kruemmungsantwort. xi* vergleicht zwei Momente desselben Reglers; im Kontinuum sind sie fuer jeden Regler, der eine Funktion des vollen Operators ist, gleich (xi* = 1/6). Die Fragestellung traegt also, misst aber ein Momentenverhaeltnis, keine Kopplung |
| S7 | Haengt xi* an der Diskretisierung von xi R phi^2? [M, ES] | Ja, in O(1): Konzentrierte und konsistente Masse stimmen langwellig bis O(h^2) ueberein, unterscheiden sich aber bei k ~ 1/h um Faktoren bis 3 (Zeilensumme gleich, Diagonale 2/30 statt 6/30 von V_T). In 4D ist das Spektralgewicht von 1/mu flach in mu, also traegt der UV-Bereich voll zu g0 bei. Erwartung [ES]: konsistente Masse gibt kleineres gamma und groesseres xi*. **Nebenlesart Mk (kein Kartenurteil):** konsistente Masse bei xi = 1/6 (eine LU mehr je Netz), Steigung aus (0; 1/6), xi*_k. Liegen xi* und xi*_k weit auseinander, ist "xi* = 1/6?" ohne Festlegung der Massendiskretisierung nicht wohldefiniert [K5] |
| S8 | Gamma_M [M] | Gamma_M~(xi) - Gamma_M(0) = Gamma~(xi) - Gamma(0) exakt (die Glieder in m sind xi-frei), also gleiche Steigung. xi*_M = -beta_M(0)/gamma mit beta_M(0) = -1,512 (KUGEL-2), also xi*_M = 0,94 xi*; beschreibend |
| S9 | Statistik [ES] | SE(beta(0)) = 0,052 bei 40 Saaten (0,074 bei 20). Der Zuwachs je Netz ist eine Summe lokaler Beitraege, sein Rauschen in y etwa 1/sqrt(N) klein; SE(gamma) daher klein gegen gamma, und SE(xi*) etwa SE(beta(0))/gamma, etwa 0,01 bis 0,015. Delta-Methode mit gepaarter Kovarianz, Jackknife als Probe |
| S10 | Vorab ableitbar | gamma > 0 (S4), Linearitaet im Kartensinn (S5), die Verschiebung durch die Nullmode (genau -b0/4 je xi > 0, Kontrolle), gamma_M = gamma (S8), V_Q/V_K. Nicht ableitbar: gamma selbst (braucht Tr'(K^-1 M) auf diesen Netzen; KUGEL-1/-2 enthalten keine K^-1-Daten, Karte) und damit xi* |

## 2. Konstruktion (code/xi_kugel.py)

- **Netze [Karte]:** k1.kugelnetz aus kugel.py, unveraendert (Saatschluessel [20261004, 39, 4, N, saat]). Regel Q mit
  denselben Operationen in derselben Reihenfolge wie kugel2.eine_messung (q_laengen: Grundmann-Moeller Grad 5, Sehnen
  mal <J>_T^(1/4)). Gamma_Q(0) = k1.auswerten (geerdete LU, 1/2 log det' K, dazu Gamma_M, Summe ln m, V, korr);
  daraus K und m (Option dicht, gleiche Rechnung). Damit muss Gamma_Q(0) bitgleich mit KUGEL-2 herauskommen (XI0).
- **xi > 0 (1/12, 1/6, 1/4) [Karte]:** A = K + xi R diag(m), R = n(n-1)/a^2; Gamma(xi) = 1/2 Summe ln U_ii der duennen LU
  ohne Erdung (MMD_AT_PLUS_A, diag_pivot_thresh 0, SymmetricMode, keine Equilibrierung, math.fsum). Gespeichert: gamma,
  nullmode = 1/2 ln(xi R V_R/N), gamma_tilde = gamma - nullmode, LU-Daten.
- **Nebenlesart Mk [F]:** A_k = K + (1/6) R M_k, M_k konsistente P1-Masse V_T (1 + delta_ij)/30; gleiche Speicherung.
- **Formpruefung je Netz [M, S4]:** Gamma(0), Gamma~(1/12), Gamma~(1/6), Gamma~(1/4) streng steigend und streng konkav;
  Gamma~_k(1/6) > Gamma(0). Nur Wahrheitswerte.
- **Torus [F]:** nicht neu gerechnet (R = 0). Die Auswertung uebernimmt Torus-Gamma und Gueltigkeit aus den Laufdateien
  von INDUZIERT-KUGEL-1 (.69: /home/fmh/fmhc-physics-remote/runde39-induziert-kugel/lauf/, nur lesen, vor der Auswertung
  gegen deren PRUEFSUMMEN.txt geprueft), wie in KUGEL-2.
- **XI0-Daten:** Laufdateien von INDUZIERT-KUGEL-2 (.69: /home/fmh/fmhc-physics-remote/runde40-induziert-kugel2/lauf/, nur
  lesen, gegen PRUEFSUMMEN.txt geprueft) und deren auswertung.json.
- **Blind (Rauchlaeufe):** gamma, gamma_M, sum_log_m, gamma_tilde werden vor dem Speichern entfernt. Die Logs enthalten
  nie Gamma-Werte.

## 3. Messgroessen und Fit (code/auswertung_xi.py)

- **Hauptfassung [F, K3]:** y(N, 0) = (Gamma_Q(0) - Gamma_T)/sqrt(N), gerechnet mit k1a.y_wert wie in KUGEL-2 (Regel Q,
  Gamma, roh); y(N, xi) = (Gamma~_Q(xi) - Gamma_T)/sqrt(N) fuer xi > 0. "roh" (keine Volumenumrechnung): die Karte
  verlangt Regel Q ohne Umrechnung; V_Q/V_K - 1 = 2e-4 bis 7e-6.
- **Fit wie KUGEL-1 [Karte]:** je Saat und xi k1a.fits (y = beta + delta/sqrt(N), OLS ueber die vier N), dazu WLS,
  Dreiparameterfit, Teilbereiche, y je N.
- **Steigung [Karte]:** je Saat OLS-Gerade von beta_j(xi) ueber xi in {0, 1/12, 1/6, 1/4}: Achsenabschnitt b_j,
  Steigung gamma_j; gamma = Mittel, SE = Std/sqrt(M). Gerade der Mittelwerte = Mittel der Saatgeraden.
- **Linearitaet:** Rest r(xi) = beta(xi) - (b + gamma xi); SE je Punkt = Std(beta_j(xi))/sqrt(M) (Karte); gepaarte SE
  des Rests = Std(r_j(xi))/sqrt(M) (strenge Nebenprobe); zweite Differenzen je Saat (beschreibend).
- **xi* [Karte]:** xi* = -beta(0)/gamma mit dem gemessenen beta(0) (= KUGEL-2-Wert auf denselben Saaten); SE per
  Delta-Methode mit gepaarter Kovarianz von (beta_j(0), gamma_j), Jackknife ueber die Saaten als Probe. Mitberichtet:
  Nullstelle der Geraden -b/gamma.
- **Beschreibende Fassungen und Nebenlesarten (kein Kartenurteil):** null_drin (ohne Nullmoden-Abzug; muss genau um
  -b0/4 verschoben sein), log_voll (zusaetzlich (xi - 3 xi^2) ln N abgezogen; dazu beta(0) mit gamma_kont = -29/360),
  F3 (freier Dreiparameterfit beta + g ln N/sqrt(N) + delta/sqrt(N) auf die gepaarten Differenzen y(xi) - y(0) ohne
  Nullmoden-Abzug, also die woertlichste Lesart von "im Fit mit gamma ln N aufnehmen"; die freien g werden gegen
  -1/4 + xi - 3 xi^2 berichtet), Mk (konsistente Masse bei xi = 1/6), Gamma_M (xi*_M).

## 4. Saaten, N, Laeufe [Karte; F nach dem Rauchlauf, blind]

- N = 1000, 2000, 4000, 8000 [Karte]. Regel vor dem Rauchlauf: 40 Saaten (0 bis 39, genau die von KUGEL-1/-2), wenn die
  Hauptlaeufe nach der Rauchzeit hoechstens 30 min Wandzeit brauchen, sonst 30, sonst 20 (Karte: mindestens 20).
- Rauchzeit je Saat (alle fuenf LU) 1,4 / 4,0 / 15,1 / 74,2 s (N = 1000 / 2000 / 4000 / 8000), also 3790 s Rechenzeit fuer
  40 Saaten, auf drei Spuren etwa 22 min. **Also 40 Saaten.**
- .69, /home/fmh/fmhc-physics-remote/runde40-induziert-xi/, nur ueber kleintest.sh, Spuren cpu3, cpu4, cpu5, je Spur eine
  Kette nacheinander (ein ssh je Spur); bei N = 8000 hoechstens 5 Saaten je Lauf (etwa 6,2 min).
  - cpu3: N = 8000 Saaten 0-4, 5-9, 10-14; N = 4000 Saaten 0-13.
  - cpu4: N = 8000 Saaten 15-19, 20-24, 25-29; N = 4000 Saaten 14-26.
  - cpu5: kontrolle; N = 8000 Saaten 30-34, 35-39; N = 4000 Saaten 27-39; N = 2000 und 1000 Saaten 0-39 (ein Lauf).
  - Ausgabe lauf/messung-n4-N<N>-s<saat0>.json (N = 2000 und 1000 gemeinsam in messung-n4-N2000-1000-s0.json),
    lauf/kontrolle.json, Logs je Lauf; jeder Lauf schreibt nach jedem (Saat, N).
- **Abbruch [F]:** Nicht fertige (Saat, N) fehlen; Saaten ohne alle N heissen unvollstaendig und fallen aus dem Fit
  (offengelegt). Letzter Start spaetestens 14:40 CEST.
- Danach (ueber den Starter): auswertung_xi.py lauf <KUGEL-1 lauf> <KUGEL-2 lauf> lauf/auswertung.json
  <KUGEL-2 lauf/auswertung.json>.

## 5. Tor [F]

- Je (Saat, N): Kugelnetz gueltig (k1.kugel_gueltig), LU ok fuer xi = 0, 1/12, 1/6, 1/4 und Mk (alle U_ii > 0,
  perm_r = perm_c, alle Simplizes einbettbar), Torus gueltig und Torus-LU ok (aus KUGEL-1).
- Eine Saat mit einem Fehler bei irgendeinem N wird ausgeschlossen und gezaehlt. Mehr als 10 % ausgeschlossen oder
  weniger als 18 gute Saaten (90 % der Kartenzahl 20): XI1 bis XI3 (Plan) "nicht auswertbar (Tor)".
- Kontrollen (Abschnitt 7) muessen ihre Schwellen erfuellen; sonst stehen die Urteile mit Vermerk da.

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln (mechanisch in auswertung_xi.py)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| XI0 | Kontrolle: beta(0) bitgleich mit KUGEL-2 (Regel Q) | 90 % |
| XI1 | beta(xi) steigt mit xi (gamma > 0 mit >= 3 SE) und ist ueber die vier Werte linear (Rest der Geraden <= 2 SE je Punkt) | 75 % |
| XI2 | [H] xi* liegt in [0,10; 0,25] | 40 % |
| XI3 | [H] xi* liegt innerhalb 20 % von 1/6 (in [0,133; 0,200]) | 25 % |

- **XI0:** Plan: eingetroffen, wenn fuer jedes hier gerechnete (Saat, N) Gamma_Q(0) als float gleich (==) dem Wert in den
  Laufdateien von KUGEL-2 ist und beta(0) (Mittel, SE und jedes beta_j) gleich (==) dem Fit der KUGEL-2-Daten auf
  denselben Saaten mit derselben Funktion; sonst nicht eingetroffen (mit groesster Abweichung). Karte: eingetroffen, wenn
  beta(0) == beta_Q,roh von KUGEL-2 auf denselben Saaten. Mitberichtet: Gamma_M, Summe ln m, V, korr, korr_M, lam_min,
  a, V_K, F je Netz; bei 40 Saaten zusaetzlich der gespeicherte Wert -1,612574487200885 aus KUGEL-2/auswertung.json.
  Ist XI0 nicht eingetroffen, stehen XI1 bis XI3 mechanisch da, mit Vermerk.
- **XI1 (Plan = Karte):** eingetroffen, wenn gamma >= 3 SE(gamma) und fuer alle vier xi abs(r(xi)) <= 2 SE(beta(xi))
  (SE je Punkt, Abschnitt 3); sonst nicht eingetroffen. Beide Teile einzeln berichtet. Strenge Nebenprobe (gepaarte SE
  des Rests) mechanisch berichtet, kein Kartenurteil.
- **XI2 (Plan = Karte):** eingetroffen, wenn 0,10 <= xi* <= 0,25 (Punktschaetzer); sonst nicht eingetroffen. Merkmal
  "Grenzfall", wenn xi* +- 2 SE eine Fenstergrenze enthaelt.
- **XI3:** Plan: eingetroffen, wenn 2/15 <= xi* <= 1/5 (genau 20 % um 1/6); Karte: wenn 0,133 <= xi* <= 0,200
  (gedruckte Grenzen) [K4]. Dazu Abstand (xi* - 1/6)/SE und Merkmal "Grenzfall".
- Vermerk bei nicht bestandenem Tor: XI1 bis XI3 (Plan) "nicht auswertbar (Tor)".

## 7. Kontrollen (code/xi_kugel.py kontrolle und in jedem Netz; Schwellen vor dem Lauf)

- **KX0:** S^4, N = 400, Saat 990: Gamma_Q(0), Gamma_M, Summe ln m, V, korr, lam_min ueber den eigenen Weg gleich (==)
  kugel2.eine_messung (dort laufen vorher C und S). Prueft den XI0-Weg.
- **KX1:** duenne LU gegen dicht (slogdet von K + xi R M bzw. K + xi R M_k) <= 1e-8 fuer alle xi.
- **KX2:** exakte Nullmoden-Identitaet (S2) gegen die dichten verallgemeinerten Eigenwerte: abs((Gamma~(xi) - Gamma(0))
  - 1/2 Summe' ln(1 + xi R/mu_k)) <= 1e-8, fuer beide Massen; kleinster Eigenwert mu_0 <= 1e-10.
- **KX3:** Formpruefung (S4) im Kontrollnetz.
- **KX4:** Grenzwert xi = 1e-9: abs(Gamma~ - Gamma(0)) <= 1e-6; Negativprobe ohne Abzug > 1.
- **KX5:** Summe m = V_R, Zeilensumme M_k = m, 1^T M_k 1 = V_R (relativ <= 1e-12), R a^2 = 12 (<= 1e-12), M_k positiv
  definit.
- **KX6 (Skalierung):** Laengen mal 1,37 und a mal 1,37: Gamma~(xi) - Gamma(0) unveraendert (<= 1e-8), Gamma(0)
  verschoben um (N-1) ln 1,37 (<= 1e-8).
- **In jedem Netz:** Formpruefung, Massenproben (<= 1e-12), R a^2 - 12 (<= 1e-12), LU-Gueltigkeit (Tor).
- **In der Auswertung:** XI0; Verschiebung null_drin - haupt = -b0/4 = -0,0097 je xi > 0 (Abweichung <= 1e-4; nur
  ln(V_R/N) und Rundung tragen bei).
- Aus KUGEL-1 gelten weiter KA bis KG fuer den unveraenderten Code (P1, LU, Gamma_M, Netzpruefungen, Negativproben).

## 8. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Code der Regel Q:** Die Karte nennt "kugel.py aus RUNDE-37/induziert-kugel-2/code/ (Regel Q)". Regel Q steht in
  kugel2.py (j_mittel, GM5); kugel.py enthaelt nur C und S. Benutzt: beide unveraendert (q_laengen bildet den Weg von
  kugel2.eine_messung nach; KX0 prueft die Bitgleichheit).
- **[K2] XI1 steht praktisch vorab fest** (S4, S5): gamma > 0 folgt exakt aus der Monotonie von log det in xi; die
  Kartenschwelle fuer die Linearitaet (2 SE je Punkt, etwa 0,1) liegt rund hundertmal ueber der erwarteten Kruemmung
  (etwa 0,001). XI1 prueft damit Code und Fit, nicht die Physik. Die Wahrscheinlichkeit der Karte (75 %) bleibt stehen.
  Die strenge gepaarte Probe laeuft mit, ohne Kartenurteil.
- **[K3] Nullmode:** Die Karte will den Beitrag "im Fit mit gamma ln N aufnehmen". Sein Koeffizient ist exakt bekannt
  (-1/4, S2); der Plan zieht das Glied je Netz exakt ab, was einem Fit mit festem gamma = -1/4 entspricht (der N-freie
  Rest faellt in delta). Kein Unterschied im Urteilsweg; der freie Fit (F3) wird berichtet.
- **[K4] Fenster XI3:** 20 % um 1/6 ist [0,1333; 0,2000]; die Karte druckt [0,133; 0,200]. Plan: genaue 20 %, Karte:
  gedruckte Zahlen. Verschieden nur fuer xi* in [0,1330; 0,1333).
- **[K5] Diskretisierung des Massenglieds** (S7): xi* haengt in O(1) davon ab, wie xi R phi^2 diskretisiert wird
  (konzentriert oder konsistent). Der Bedeutungssatz zu XI3 ("Gitter-Regler wie Eigenzeit-Regler") gilt nur fuer die
  gewaehlte Masse; Nebenlesart Mk zeigt die Spanne.
- **[K6] Torus-Referenz** (S6): fair fuer die Frage der Karte; gamma ist dabei ein Flachraum-Moment, xi* ein
  Momentenverhaeltnis.
- **[K7] beta(0) in xi*:** der gemessene Wert bei xi = 0 (Kartenformel), nicht der Achsenabschnitt der Geraden; beide
  berichtet.
- **[K8] Saatzahl** 40 statt mindestens 20 (Zeitregel Abschnitt 4).
- Kartenfehler, die ein Urteil nach Kartenwortlaut aendern koennen: [K4] (nur im schmalen Bereich). [K2] aendert kein
  Urteil, wohl aber, was XI1 aussagt.

## 9. Agenten-Vorhersagen (nach Kontrolle und Rauchlauf, vor den Hauptlaeufen; ohne Kenntnis der Messwerte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor ohne Ausschluss (160 Netze, alle fuenf LU gueltig) | 95 % |
| A2 | XI0 eingetroffen (Plan und Karte) | 90 % |
| A3 | XI1 eingetroffen | 97 % |
| A4 | Strenge gepaarte Linearitaetsprobe (Hauptfassung) verfehlt | 60 % |
| A5 | xi* liegt in [0,25; 0,50] | 65 % |
| A6 | XI2 eingetroffen | 25 % |
| A7 | XI3 eingetroffen (Plan) | 7 % |
| A8 | Nebenlesart Mk: gamma_k < gamma, also xi*_k > xi* | 80 % |
| A9 | F3: freie ln-Koeffizienten bei allen drei xi innerhalb 2 SE von -1/4 + xi - 3 xi^2 | 55 % |

## 10. Kontrolle, Rauchlaeufe, Codeprobe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC)

- **kontrolle** (11:27:06 bis 11:27:08, cpu5, rc 0), alle Schwellen erfuellt [E]:
  - KX0: Gamma_Q(0), Gamma_M, Summe ln m, V, korr, lam_min gleich (Abweichung 0,0) kugel2.eine_messung.
  - KX1: LU gegen dicht <= 1,7e-13 (alle xi, beide Massen), Vorzeichen +1.
  - KX2: Identitaet <= 8,1e-14; mu_0 = 2,9e-14 (konzentriert) und 1,6e-13 (konsistent).
  - KX3: monoton und konkav; KX4: mit Abzug 6,9e-8, ohne 9,80 (Negativprobe schlaegt an).
  - KX5: Massenproben <= 7,9e-16, R a^2 = 12,0, M_k symmetrisch (4e-17) und positiv definit.
  - KX6: Skalierung 1,1e-13, Gamma(0)-Verschiebung 1,8e-11.
- **rauch-a** (11:27:07 bis 11:29:36, cpu3, rc 0), N = 8000, Saaten 900 und 901, blind: beide gueltig, alle LU ok,
  Formpruefung erfuellt, 74,1 und 74,2 s je Saat (je LU 12,3 bis 13,6 s), RSS bis 832 MB.
- **rauch-b** (11:27:09 bis 11:27:51, cpu4, rc 0), N = 1000, 2000, 4000, Saaten 900 und 901, blind: alle gueltig, Form
  erfuellt, Massenproben <= 1,2e-15, 1,4 / 4,0 / 15,1 s je Saat, RSS bis 348 MB.
- **Blindheit geprueft (jq):** In rauch-a.json und rauch-b.json ist blind = true und kein Objekt hat ein Feld gamma,
  gamma_tilde, gamma_M oder sum_log_m.
- **Codeprobe** (11:29 UTC, cpu4): nicht blind auf N = 600 und 1200, Saaten 950 bis 952 (Torus aus der Probe von
  KUGEL-1, Regel Q aus der Probe von KUGEL-2), dann Auswertung; rc 0 fuer beide. Nur Struktur und Kontrollfelder gelesen
  (jq keys; M = 3, Tor nicht bestanden wie erwartet, 6 von 6 Netzen XI0-gleich, Fit-Ebene gleich, Formpruefung in 6 von 6
  Netzen). Keine Werte von beta, gamma oder xi* gelesen.
- **Zeitfolge der Festlegungen:** Operator, Massenwahl, Nebenlesart Mk, Nullmoden-Abzug, Fassungen, Fit, Steigung,
  xi*, Tor und Urteilsregeln standen vor der Kontrolle im Code (bis 13:26:59 CEST). Nach Kontrolle und Rauchlauf
  festgelegt: Saatzahl 40 (nach der vorab notierten Zeitregel), Laufaufteilung, Agenten-Vorhersagen, der Plantext.
- **Selbstanzeige zur Kontrolle:** Der Kontrollwert KX4 (6,9e-8 bei xi = 1e-9, N = 400) ist zugleich eine grobe
  Schaetzung von 1/2 xi R Tr'(K^-1 M) im Kontrollnetz (Summe' 1/mu etwa 45 bei N = 400, scharfer Modenschnitt etwa 47);
  er liegt aber im numerischen Rauschen der LU nahe der Singularitaet (etwa 1e-7) und ist deshalb nicht belastbar. Ich
  habe ihn gesehen, bevor ich die Agenten-Vorhersagen A5 bis A7 schrieb; die Schaetzung S3' stand vorher.
