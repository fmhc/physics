# ERGEBNIS zzz-abgleich (Runde 22, Literatur- und Schreibtisch-Agent)

- Geschrieben ab 2026-10-02 20:27:03 CEST (date). Zeitbox ab 20:08:35 CEST. Rohprotokoll mit Vorhersage vor jedem Abruf und
  jeder Rechnung: ARBEITSFELD.md (gleicher Ordner).
- Gegenstand: G.-D. Zhang, S.-Y. Zhou, M.-F. Zhu, "Q-ball superradiance: Analytical approach", arXiv:2510.27064v1
  (im Folgenden ZZZ). Volltext S. 1-17 selbst gelesen (PDF ueber WebFetch geladen, mit dem Read-Werkzeug gelesen).
- Marken: [S] gelesen; [L?] nur Abstract, Titel oder Zitat; [H] eigene Schlussfolgerung; [E] Rechnung (.69 oder Kopf).
- Die Erwartungen Z1 bis Z3 stammen von der Leitung und sind unveraendert; hier nur gewertet.
- Abbildung der Bezeichnungen (ARBEITSFELD Abschn. 1a, A2): ihr omega_Q = unser omega, ihr omega = unser rho, ihr g = unser
  beta, ihr 1 + U = unser D, ihr W = unser C, ihr f0^2 = unser S im Inneren.

## 1. Ergebnis (5 Punkte)

1. **Z1 trifft ein, und zwar woertlich.** ZZZ rechnen in unserem Modell: V = |Phi|^2 - |Phi|^4 + g|Phi|^6 (Gl. 3) ist
   U(S) = S - S^2 + g S^3 [S]. Ihre Stoerkoeffizienten U = -4f^2 + 9g f^4 und W = -2f^2 + 6g f^4 (Gl. 22-23) sind unser
   D - 1 und C [S]. Ihre erste Innenwellenzahl sqrt(-rho_1) (Gl. 101) ist bei f0^2 = 1/(2 beta) genau das k_in des Papiers
   (main.tex Z. 299-301); die Differenz ist numerisch 0 [E]. Ihre Hauptbeispiele nutzen g = 1/3, nicht 1/2 [S].
2. **Der Leiterabstand ist die halbe Wellenlaenge der einen Innenwelle sqrt(-rho_1). Eine Summen- oder Differenzwelle
   ist er nicht; Z2 trifft im Wortlaut nicht ein.**
   - An allen Leiterstellen ist -rho_2 < 0 (-0,93 bis -1,43) [E]. Die zweite Innenwelle ist dort evaneszent.
     sigma_+- = k1 +- i kappa_2 haben beide den Realteil k1 = sqrt(-rho_1).
   - Gemessen ist Delta R_halb = 1,637 bis 1,640 (3D, n = 6 bis 10) und 1,634 bis 1,636 (2D, n = 6 bis 8) [E].
   - Je Sprosse waechst k1 R um 0,995 pi bis 1,009 pi (3D) bzw. 1,002 pi bis 1,005 pi (2D) [E]. Lokal ist
     Delta R/(pi/k1) = 1,02 bis 1,04 mit gemessenem S0 und 1,03 bis 1,07 mit S_c = 1 [E].
   - Alle reellen Summen- und Differenzkandidaten liegen 16 bis 66 % daneben [E]: k1 +- kappa_2, |sigma|, und die
     ZZZ-Grenzformen 2 rho und 2 omega.
3. **ZZZ rechnen in einem anderen Regime. Frage 4 ist bei unseren Parametern nicht auswertbar; Z3 bleibt offen.**
   - ZZZ verlangen beide Aussenkanaele offen: |omega_Q +- omega| > 1 (Gl. 26), also "omega > 1 + omega_Q" (S. 9) [S].
   - Die Leiter liegt unter dieser Schwelle: rho - (1 + omega) = -0,149 bis -0,172, und Kanal B ist zu (k_-^2 = -0,28 bis
     -0,31) [E].
   - Bei einem einzigen offenen Kanal erzwingt ihre Teilchenzahlerhaltung (Gl. 59-60) N^out = N^in. Ihre Verstaerkung ist
     dort also identisch 1 [H]. Maxima oder Minima, auf die eine stille Stelle fallen koennte, gibt es dort nicht.
4. **Bedeutung gemaess Karte: Die Lage liegt zwischen den beiden Aesten und naeher am Ast "Z2 trifft ein".**
   - Gemeinsam ist der Baustein: die Innenwellenzahl der konstanten Kanalmatrix und die Halbwellenphase an der Wand [H].
   - Verschieden sind Regime und Mechanismus. Bei ZZZ erzeugen zwei propagierende Innenwellen und zwei offene Kanaele
     Verstaerkungsspitzen. Bei uns gibt es eine propagierende und eine evaneszente Innenwelle, und die Amplitude im
     einzigen offenen Kanal loescht sich exakt aus.
   - Folgerung [H]: Das Papier sollte ZZZ zitieren und k_in = sqrt(-rho_1) nennen. Neu ist die exakte, per Windung bzw.
     Intervall belegte Stille unterhalb der zweiten Kanalschwelle, nicht der Halbwellenabstand. Ein Textvorschlag steht
     in Abschnitt 5.
5. **Nebenbefunde.**
   - Die zwei Felder von ZZZ Abb. 2 mit g = 1/2 erfuellen ihre eigenen Existenzbedingungen nicht [E]:
     - omega_Q = 0,55 und 0,65 liegen unter omega_Q,min = 0,707 (Gl. 8);
     - bei omega_Q = 0,75 liegt f0 = 1,20 ueber f_max = 1,028 (Gl. 14-15).
     - Ihr Stufenmodell behandelt f0 und r_* als freie Parameter.
   - Unser S0 stimmt an n = 6 bis 10 auf 2,3e-6 mit f_max^2 nach ZZZ Gl. (14) ueberein [E]. Die Innenamplitude ist also
     kein freier Wert, und die Lesart S0 ist die zum Profil passende.
   - Keine der vier zitierenden Arbeiten behandelt den Fall mit nur einem offenen Kanal [L?, nur Titel].
   - Die Karte nennt v0.25 und "um Z. 435". main.tex ist jetzt "Draft 0.37" (Z. 13), die Herleitung steht in Z. 288-347,
     Z. 435 liegt im Schluss [S].

### 1b. Erwartungsverstoesse (das Wichtigste zuerst)

1. **Die Vergleichsgroesse der Karte gibt es im Leiterregime nicht.** Die Karte uebernahm aus R21 das Bild "Maxima im
   Abstand einer halben Summen- bzw. Differenzwelle". Dieses Bild setzt zwei reelle Innenwellen und zwei offene Kanaele
   voraus (ZZZ Gl. 26, 108-109) [S]. An unseren Stellen ist beides nicht erfuellt (-rho_2 < 0, k_-^2 < 0) [E]. Ich hatte
   die evaneszente zweite Innenwelle vorab als Hypothese notiert (ARBEITSFELD 1a). Nicht erwartet hatte ich, dass Frage 4
   und Z3 damit gegenstandslos werden: Ihre Verstaerkung ist dort konstant 1 [H].
2. **Gleiches Modell statt "Familie bis auf Skalierung".** Meine Vorhersage war "nicht genau beta = 1/2". Tatsaechlich ist
   der Potentialansatz identisch (g = beta) und die Wellenzahl des Papiers dieselbe Formel (Gl. 101) [S/E]. g = 1/2 kommt
   bei ZZZ vor, aber nur in zwei Feldern von Abb. 2, und dort ausserhalb ihrer eigenen Existenzbedingungen [E].
3. **Klein:** Vorhergesagt hatte ich, dass bei omega_Q = 0,65 und g = 1/2 kein f_max existiert. f_max = 0,954 existiert;
   es fehlt nur f_z (Gl. 16 verletzt: g_max = 0,433) [E]. Die Aussage "keine Q-Ball-Loesung" bleibt wegen Gl. (8) bestehen.
4. **Verfahren:** Beim Zitationsabruf (Semantic Scholar) habe ich die Vorhersage erst nach dem Abruf eingetragen. Sie war
   vorher formuliert, aber nicht festgehalten (ARBEITSFELD A3).

## 2. Antworten auf die Fragen

### Frage 1: Was zeigen Zhang/Zhou/Zhu?

- **Arbeit:** arXiv:2510.27064v1 [hep-th], eingereicht am 31.10.2025, 21 Seiten, 8 Abbildungen. Die abs-Seite nennt keine
  Zeitschrift [S].
- **Modell und Potential** [S]:
  - Gl. (1): V = m~^2|Phi~|^2 - lambda~|Phi~|^4 + g~|Phi~|^6. Umskalierung Gl. (2) mit g = g~ m~^2/lambda~^2.
  - Gl. (3): V = |Phi|^2 - |Phi|^4 + g|Phi|^6, mit g > 1/4.
  - Gl. (8): omega_Q,min^2 = 1 - 1/(4g), gleich unserem omega_c^2 (main.tex Z. 94).
  - Gl. (10) ist mit d = 3 unsere Profilgleichung (main.tex Z. 88) [S/H].
  - Antwort zur Karte: gleich unserer Sextik U = S - S^2 + S^3/2, sogar ohne weitere Skalierung, wenn g = 1/2.
- **Parameter:**
  - g = 1/3 in Abb. 1 und 3 bis 7. g = 1/2 nur in zwei Feldern von Abb. 2 [S, Legenden].
  - Dort liegen omega_Q = 0,55/0,65 unter 0,707, und f0 = 1,20 liegt ueber f_max = 1,028 [E].
- **Hintergrund:**
  - (n+1)-Stufenfunktion (Gl. 18-19). Der Duennwandfall n = 1 hat f_Q = f0 fuer r < r_* und 0 aussen (Abschn. IV A) [S].
  - Die Duennwandformel haengt von fuenf freien Parametern ab: omega_Q, g, f0, r_*, omega (S. 11) [S].
  - Hauptrechnung in d = 2; d > 2 ueber Gl. (50)-(53) mit Bessel-Ordnung delta = (d-2)/2 [S].
- **Zwei Kanaele** [S]:
  - Gl. (24): phi = (eta_+ e^{-i omega t} + eta_- e^{i omega t}) e^{-i omega_Q t}, omega_+- = omega_Q +- omega.
  - Gl. (25): gekoppelte Gleichungen mit k_+-^2 = omega_+-^2 - 1.
  - Gl. (26): Ausbreitung nur fuer |omega_Q +- omega| > 1; S. 9: "omega > 1 + omega_Q".
- **Zwei Innenkanaele** [S]:
  - Gl. (40)-(42): gamma = ((U - k_+^2, W), (W, U - k_-^2)) = lambda^-1 diag(rho_1, rho_2) lambda.
  - Gl. (47)-(48): Innenloesung J0(sqrt(-rho_1) r) und J0(sqrt(-rho_2) r), "characteristic perturbative wavenumbers" (S. 7).
  - Gl. (101): -rho_1 = omega_Q^2 + omega^2 + sqrt(W^2 + 4 omega_Q^2 omega^2) - (1+U).
  - Gl. (102): dieselbe Formel mit Minus vor der Wurzel.
- **Verstaerkung gegen den Wandradius** [S]:
  - Exakt im Duennwandfall: Gl. (96), N_+^out = cos^2 theta_H(v23, w)/cos^2 theta_H(v13, w).
  - Fuer grosses r_* (Bessel-Asymptotik Gl. 107): Gl. (108). N_+^out ist dort eine rationale Funktion von cos(sigma_- r_*),
    sin(sigma_+ r_*), cos(sigma_+ r_*) und sin(sigma_- r_*).
  - Gl. (109): sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2), C_+- = sqrt(rho_1 rho_2) +- k_+ k_-. Gl. (110): D_+-, F_+-.
  - Die Verstaerkungsfaktoren folgen aus N^out ueber Gl. (74)-(77).
- **Summen- und Differenzwelle** [S]:
  - Fuer grosses omega gilt sigma_+ ~ 2 omega und sigma_- ~ 2 omega_Q (S. 13).
  - Gl. (114)-(118) mit den Phasen phi_+- aus Gl. (117); fuehrend ist sin^2(2 r_* omega_Q + phi_-).
  - Der Satz im Abstract "peak spacing is simply the inverse of the Q-ball size" meint den Spitzenabstand in omega bei
    festem r_*, also den Faktor cos(2 r_* omega + phi_+) [S/H].
- **Abb. 3** [S]: Karten ueber (omega, r_*) fuer omega_Q = 0,52, f0 = 1,20, g = 1/3, n = 1.
- **Regimegrenze in ihrer eigenen Abb. 3** [E]: Bei diesen Parametern ist -rho_2 < 0 fuer 1,52 < omega < 1,875 (Nullstelle
  bei 1,875121). Auch dort gibt es also nur eine propagierende Innenwelle. Bei omega = 2 sind pi/sigma_+ = 1,083,
  pi/sigma_- = 1,871 und pi/k1 = 1,372.
- **Nicht behandelt:** gebundene oder eingebettete Moden und der Fall mit einem geschlossenen Kanal. Gesehen sind
  S. 1-17 [S]; S. 18-21 (Literaturliste) nicht gelesen.

### Frage 2: Welche Phasenbedingung nutzt das Papier?

- Ort: Abschnitt sec:thinwall, main.tex Z. 288-347 (Draft 0.37) [S]. Z. 435 ist der Schluss.
- Gleichungen [S]:
  - eq:thinwall (Z. 291-294): R_tw ~ 1/(2 sqrt(beta) eps), eps = omega^2 - 1/2, f^2 ~ S_c/(1 + exp[(r - R_tw)/sqrt(beta)]).
  - eq:interior (Z. 298-302): k_in^2 = omega^2 + rho^2 - D_c + sqrt(4 omega^2 rho^2 + C_c^2), mit D_c = 1 + 1/(4 beta) und
    C_c = 1/(2 beta). Laut Z. 296-297 ist das die propagierende Wellenzahl nach Diagonalisieren der konstanten
    Innenmatrix.
  - eq:phase (Z. 308-312): k_in(omega_n, rho_n) R_tw(omega_n) ~ pi [n + theta(eps_n)], rho_n ~ omega_n + c(eps_n).
    theta und c sind kalibriert (Z. 313-317).
  - eq:spacing (Z. 321-324): eps_n ~ 1/(b_inf n), b_inf = 2 sqrt(beta) pi/k_inf.
- Vergleichswerte im Text [S]:
  - Schritte in 1/eps fuer n = 12 bis 15: 2,3043 / 2,3054 / 2,3055. Kalibriert ergibt sich 2,298, die nackte
    Wandzustands-Schaetzung 2,334 (Z. 325-327).
  - In 2D sind die letzten Schritte etwa 4,62 (Z. 339-347).
- Datenquellen [S]:
  - tab:ladder (Z. 188-228). Die Zeilen n = 6 bis 10 stammen aus R13 (Z. 153-154, 167-176), die 2D-Folge aus R12
    (Z. 457-459).
  - Aus R13 praez.json habe ich je Stelle omega*^2, rho*, S0 = f0^2 (Code Z. 1980) und R_halb (S faellt auf S0/2, Code
    Z. 298-306) uebernommen. Fuer 2D dienen kurve.json f6/fein/f8 und die Lagen aus R12 ERGEBNIS Z. 81, 153 und 196.
- **[H] Lesart:** Die Bedingung des Papiers quantisiert eine einzige Innenwelle auf Halbwellen. Die zweite Wurzel (Minus
  vor der Wurzel) verwendet das Papier nicht. Sie ist in seinem Regime negativ, also evaneszent [E].

### Frage 3: Stimmt der Leiterabstand mit pi/sigma_+ oder pi/sigma_- ueberein?

- **Mit einer reellen Summen- oder Differenzwelle: nein** [E]. Im Leiterregime ist -rho_2 < 0. Die Summen- und
  Differenzwelle von ZZZ sind dann komplex, sigma_+- = k1 +- i kappa_2. Fuer die reellen Ersatzgroessen ist
  Delta R_halb/(pi/X) an den Schritten n >= 6 (3D und 2D):

  | Ersatzgroesse X | Verhaeltnis |
  |---|---|
  | k1 + kappa_2 | 1,56 bis 1,66 |
  | k1 - kappa_2 | 0,42 bis 0,55 |
  | \|sigma\| | 1,16 bis 1,21 |
  | 2 rho | 1,62 bis 1,66 |
  | 2 omega | 0,76 bis 0,78 |

- **Mit dem gemeinsamen Realteil Re sigma_+- = k1 = sqrt(-rho_1) = k_in: ja** [E].
  - Der Phasentest Delta(k1 R)/pi pro Sprosse ergibt 1,004 bis 1,009 mit R_halb und 0,995 bis 0,999 mit R_tw (3D).
    In 2D sind es 1,002 bis 1,005.
  - Lokal ist Delta R_halb/(pi/k1) = 1,030 bis 1,043 (S0) bzw. 1,049 bis 1,070 (S_c) in 3D.
  - Die 5-%-Schranke der Karte haelt lokal also nur mit S0. Mit S_c haelt sie erst ab 9 -> 10, beim Phasentest ueberall.
  - Der Unterschied zwischen lokal und Phasentest kommt von der Drift: k1 faellt entlang der Leiter von 2,059 auf 2,009
    (S_c), und R waechst mit. Die Phasenbedingung des Papiers enthaelt diese Drift.
- **Nur durch die Innenwelle bestimmt** [E]: Die Schritte in 1/eps verdoppeln sich von 3D (2,29 bis 2,30) zu 2D (4,62). Der
  Abstand in R bleibt dagegen gleich: 1,634 bis 1,640 in beiden Dimensionen. Das passt zu R_tw = (d-1)/(4 sqrt(beta) eps)
  (Laplace mit sigma_w = sqrt(beta) S_c^2/2; fuer d = 3 gleich main.tex Z. 292) und zu einer festen Halbwelle pi/k1.
- **Grenzwert** [E, Kopfrechnung; H wegen Extrapolation]: Ich habe rho - omega aus n = 6 und 10 linear nach eps -> 0
  verlaengert, c(0) ~ 0,822. Damit wird k_inf ~ 1,9287 und b_inf = 2 sqrt(beta) pi/k_inf ~ 2,3035. Gemessen sind fuer
  12 -> 15 die Werte 2,304 bis 2,307 aus tab:ladder.
- **Die drei Lesarten der Innenamplitude lassen sich nicht trennen.** S0 und S_c sowie R_halb und R_tw liegen im
  Phasentest alle innerhalb von 1 %.

### Frage 4: Liegen die stillen Stellen auf ihren Verstaerkungsmaxima, -minima oder auf keinem von beiden?

- **Bei unseren Parametern ist ihre Formel nicht auswertbar.**
  - Ihre Gl. (26) verlangt omega > 1 + omega_Q [S]. Unsere Stellen haben rho - (1 + omega) = -0,149 (n = 1) bis -0,164
    (n = 10) in 3D und -0,170 bis -0,172 in 2D. Dabei ist k_-^2 = (rho - omega)^2 - 1 = -0,275 bis -0,315 [E].
  - Die Aussenformen von Gl. (29) fuer den Minus-Kanal werden dann exponentiell. Ein- und auslaufende Amplituden A_-, B_-
    gibt es nicht, und Fall b (Einfall im Minus-Kanal) existiert nicht [H].
  - Mit einem offenen Kanal erzwingt M_eta = 0 (Gl. 58-59) |A_+| = |B_+|. Dann ist N_+^out = 1 und A^a_tt = 1 [H].
- **Ihre Kurven enden an unserer Regimegrenze mit dem Wert 1:** Gl. (111)-(113), lim eps -> 0 N_+-^out = 1 und
  A^b -> 1 [S].
- **Antwort: auf keinem von beiden.** Der Grund ist nicht eine andere Bedingung an derselben Groesse. Ihre Groesse ist im
  Leiterregime konstant.
- Vergleichbar waere die Breite der nahen Resonanz (Fano-Kollaps an der stillen Stelle, R13 Abschn. 3c). Diese Groesse
  rechnen ZZZ nicht [H].

### Frage 5: Saetze fuer LITERATURE.tex

Siehe Abschnitt 5 (nur Vorschlag, das Papier ist unveraendert).

## 3. Erwartungen Z1 bis Z3 (Leitung) und Ausgang

| Nr | Erwartung (Leitung, vorab) | Wahrsch. | Ausgang | Beleg |
|---|---|---|---|---|
| Z1 | Zhang/Zhou/Zhu nutzen dieselbe Sextik-Familie (bis auf Skalierung) | 60 % | **eingetroffen**, staerker als erwartet: identischer Ansatz, g = beta; Hauptbeispiele mit g = 1/3, g = 1/2 nur in zwei Feldern von Abb. 2 (dort keine Q-Ball-Parameter) | Gl. (1)-(3), (8), (10), (22)-(23) [S]; Gl. (101) = main.tex Z. 299-301, Differenz 0 [E]; Abb. 2 gegen Gl. (8), (14)-(16) [E] |
| Z2 | Der Leiterabstand des Papiers ist die halbe Wellenlaenge einer ihrer beiden Wellen (Summe oder Differenz), auf 5 % | 55 % | **nicht eingetroffen (Wortlaut)**: Eine reelle Summen- oder Differenzwelle gibt es im Leiterregime nicht, und reelle Ersatzgroessen liegen 16-66 % daneben. **In der Sache:** Der Abstand ist die Halbwelle der ersten ZZZ-Innenwelle sqrt(-rho_1) = Re sigma_+- (Phasentest <= 0,9 %, lokal 2-4 % mit S0) | Abschn. 4a/4b; zzz_abgleich.json [E]; Gl. (101), (109) [S] |
| Z3 | Die stillen Stellen liegen weder auf ihren Maxima noch auf ihren Minima (andere Bedingung: Kopplung null statt Interferenz) | 50 % | **offen (nicht pruefbar)**: Ihre Verstaerkung ist bei unseren Parametern identisch 1, Maxima und Minima gibt es dort nicht. Der Wortlaut ist trivial wahr, die Begruendung ungeprueft. Das Papier selbst beschreibt die Stille als Ausloeschung durch Interferenz (main.tex Z. 64-66, 303-306) | Gl. (26), S. 9, Gl. (58)-(60), (111)-(113) [S]; k_-^2 < 0 [E]; N^out = 1 [H] |

### 3b. Regime und Moderatoren (Regel 1)

- **Drei Regime [H, gestuetzt auf E und S]:**
  - **I (unsere Leiter):** Aussen ist ein Kanal offen (k_-^2 < 0). Innen gibt es eine propagierende und eine evaneszente
    Welle (-rho_2 < 0). Beobachtbar sind exakte Nullstellen der Amplitude im offenen Kanal im Abstand pi/k1.
  - **II (ZZZ nahe der Schwelle):** Aussen sind beide Kanaele offen, innen ist weiter -rho_2 < 0. Bei ihren Abb.-3-Parametern
    gilt das fuer 1,52 < omega < 1,875 [E]. ZZZ rechnen dort, besprechen das Regime aber nicht.
  - **III (ZZZ bei grossem omega):** Beide Innenwellen sind reell. Es entsteht die Struktur mit sigma_+- und mehreren
    Spitzen (Abb. 3, Gl. 114-118).
- **Moderatoren:** das Vorzeichen von k_-^2 (rho gegen 1 + omega) und das Vorzeichen von -rho_2. Die Dimension aendert nur
  die Wandphase (Bessel-Ordnung delta), nicht den Abstand in R: 2D und 3D stimmen auf 0,3 % ueberein [E].
- **Regel 6 [H]:** Periodische Strukturen im Radius erzeugen drei Wege:
  - Verstaerkungsspitzen (ZZZ, Regime III);
  - stille Stellen (Papier, Regime I);
  - "more peaks" bei FLS (2503.04657) und Abstrahlungs-Dips bei Oszillonen (2004.01202), beides laut R21.

  Gemeinsame Groesse ist die Phase der Innenwelle an der Wand, k R. Das Bauteil (welcher Kanal, welcher Effekt)
  entscheidet nur, was bei dieser Phase passiert.

### 3c. Unterscheidungspunkte (Regel 2)

- **"Halbwelle von sqrt(-rho_1)" gegen "Halbwelle von sigma_+-":**
  - Die beiden Lesarten laufen nur in Regime III auseinander. Bei omega = 2 und den Abb.-3-Parametern ist pi/k1 = 1,372,
    pi/sigma_+ = 1,083, pi/sigma_- = 1,871 [E].
  - In Regime I und II ist sigma_+- komplex. Dort sind sie nicht getrennt definiert, und die Halbwelle der einzigen
    reellen Innenwelle bleibt.
  - Eine stille Stelle in Regime III muesste zwei Kanalamplituden zugleich ausloeschen [H]. Das sind zwei Bedingungen,
    generisch also keine Leiter. Deshalb ist "gleicher Mechanismus" an der Leiter selbst nicht pruefbar, nur ueber die
    Regimegrenze.
- **S0 gegen S_c, R_halb gegen R_tw:**
  - Im Phasentest liegen alle Lesarten innerhalb von 1 % und sind nicht unterscheidbar.
  - Am ehesten trennt sie der dickwandige Bereich. Von n = 1 nach 6 ergibt der Phasentest 1,015 (S_c) gegen 0,984 (S0)
    mit R_halb und 0,978 gegen 0,949 mit R_tw. Fuer n = 2 bis 5 fehlen rho und R_halb.
- **Pruefbar in ZZZ selbst:** Ich vermute [H], dass ihre exakte Gl. (96) in Regime II die r_*-Periode pi/sqrt(-rho_1)
  zeigt und nicht pi/sigma_+-. Die Probe waere omega in (1,52; 1,875) bei omega_Q = 0,52, f0 = 1,2, g = 1/3. Sie ist nicht
  gerechnet.

### 3d. Gegensweep (Regel 4): Was war zu selbstverstaendlich?

1. **Dass der Zeilenbezug der Karte stimmt.** Geprueft: Die Karte nennt v0.25 und Z. 435. main.tex ist Draft 0.37, die
   Herleitung steht in Z. 288-347. README.txt nennt weiter v0.25 [S].
2. **Dass n eine lueckenlose Sprossenzaehlung ist.** Geprueft [E]: k1 R/pi waechst je Schritt um 0,995 bis 1,009. Von n = 1
   bis 6 waechst es um 5,07 (S_c, R_halb) bzw. 4,92 (S0). Im Phasenbild fehlt keine Halbwelle. Das Papier selbst nennt n
   nur ein Fortsetzungsetikett (Z. 59-60).
3. **Dass R_halb das r_* von ZZZ ist.** Teilweise geprueft mit R_tw: Abstaende 1,637-1,640 gegen 1,620-1,627, beide
   Phasentests <= 1 %.
4. **Dass ZZZ mit g = 1/2 echte Q-Baelle rechnen.** Geprueft: nein (Abb. 2) [E].
5. **Dass keine Folgearbeit den Ein-Kanal-Fall behandelt.** Geprueft ueber Semantic Scholar: 4 zitierende Arbeiten. Davon
   ist nur Evslin et al. 2026 (2604.07713) linear, und sie steht schon im Papier [L?].
6. **Dass S0 in praez.json f0^2 ist und nicht f0.** Geprueft: bic2_3d_praez.py Z. 1980.
7. **Dass ZZZ Gl. (108) in Regime II gilt.** Nicht geprueft, siehe offene Fragen.

### 3e. Kalibrierung

- **(a) Gemessen bzw. gelesen:**
  - ZZZ S. 1-17 selbst gelesen. main.tex Z. 1-470, LITERATURE.tex und bibliography.tex gelesen.
  - R13 praez.json und R12 kurve.json per jq ausgelesen; zwei Rechnungen auf der .69.
  - Zitationsliste nur als Titel.
- **(b) Nuetzlich verdichtet [H]:** "ein Baustein (sqrt(-rho_1)), drei Regime"; "Verstaerkung im Leiterregime identisch 1".
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** dass der Halbwellenabstand "nicht neu" sei.
  - ZZZ zeigen die Periode pi/sigma_+- in Regime III. Die Periode pi/sqrt(-rho_1) zeigen sie nirgends.
  - Gemeinsam sind die Formel der Innenwellenzahl und das Stufen-Bessel-Bild. Diese Formel ergibt jede Diagonalisierung
    derselben konstanten Matrix; als Prioritaetsfrage taugt sie kaum.
  - **Warnzeichen:** Waehrend der Arbeit wurde die Frage schmaler, von "Summe oder Differenz" zu "die eine Innenwelle".
    Zugleich stieg meine Sicherheit, dass beides "denselben Ursprung" hat. Der Formulierungsvorschlag sagt deshalb
    "related" und nicht "the same".

## 4. Tabellen der Leiterstellen

### 4a. Je Schritt: gemessener Abstand gegen Halbwellen

Erlaeuterungen:
- Delta R ist je Sprosse angegeben (fuer 1 -> 6 als Mittel ueber 5 Sprossen).
- pi/X ist mit dem Mittel von X an beiden Enden gebildet. "Sc/S0" heisst Innenamplitude S = 1/(2 beta) = 1 bzw.
  gemessenes S0.
- Abweichung = Delta R_halb/(pi/X) - 1.
- Paper-Phasenbedingung = Delta(k_in R_tw)/pi mit S_c, also eq:phase bei festem theta.
- Phasentest R_halb = Delta(k1 R_halb)/pi.
- Quelle: code/zzz_abgleich.json, Log code/LAUF-zzz2.log [E].

| Schritt | Delta R_halb (Delta R_tw) | pi/Re sigma_+- = pi/k1 (Sc / S0) | pi/k_Summe naiv, pi/(k1+kappa_2) (Sc / S0) | pi/k_Differenz naiv, pi/(k1-kappa_2) (Sc / S0) | ZZZ grosses omega: pi/(2 rho) / pi/(2 omega) | Paper-Phasenbedingung | Phasentest R_halb (Sc / S0) | Abweichungen gegen k1 / Summe / Differenz (Sc; S0) |
|---|---|---|---|---|---|---|---|---|
| 3D 6 -> 7 | 1,6397 (1,6202) | 1,5323 / 1,5715 | 1,0317 / 0,9863 | 2,9762 / 3,8642 | 0,9851 / 2,0905 | 0,9974 | 1,0089 / 1,0071 | +7,0 / +58,9 / -44,9 %; +4,3 / +66,3 / -57,6 % |
| 3D 7 -> 8 | 1,6383 (1,6232) | 1,5437 / 1,5786 | 1,0358 / 0,9952 | 3,0296 / 3,8151 | 0,9902 / 2,1062 | 0,9980 | 1,0068 / 1,0054 | +6,1 / +58,2 / -45,9 %; +3,8 / +64,6 / -57,1 % |
| 3D 8 -> 9 | 1,6379 (1,6259) | 1,5529 / 1,5843 | 1,0389 / 1,0023 | 3,0732 / 3,7777 | 0,9943 / 2,1185 | 0,9988 | 1,0057 / 1,0047 | +5,5 / +57,7 / -46,7 %; +3,4 / +63,4 / -56,6 % |
| 3D 9 -> 10 | 1,6368 (1,6270) | 1,5603 / 1,5889 | 1,0415 / 1,0081 | 3,1094 / 3,7483 | 0,9976 / 2,1284 | 0,9989 | 1,0045 / 1,0036 | +4,9 / +57,2 / -47,4 %; +3,0 / +62,4 / -56,3 % |
| 3D 1 -> 6 (Mittel) | 1,6177 (1,5639) | 1,4189 / 1,4499 | 0,9839 / 0,9447 | 2,5435 / 3,1167 | 0,9395 / 1,9067 | 0,9779 | 1,0146 / 0,9843 | +14,0 / +64,4 / -36,4 %; +11,6 / +71,3 / -48,1 % |
| 2D 6 -> 7 | 1,6363 (1,6348) | 1,5819 / 1,6029 | 1,0483 / 1,0238 | 3,2221 / 3,6910 | 1,0078 / 2,1545 | 1,0034 | 1,0048 / 1,0042 | +3,4 / +56,1 / -49,2 %; +2,1 / +59,8 / -55,7 % |
| 2D 7 -> 8 | 1,6344 (1,6333) | 1,5878 / 1,6064 | 1,0503 / 1,0287 | 3,2522 / 3,6643 | 1,0103 / 2,1627 | 1,0020 | 1,0031 / 1,0025 | +2,9 / +55,6 / -49,7 %; +1,8 / +58,9 / -55,4 % |

- **|sigma| = sqrt(k1^2 + kappa_2^2):** Delta R_halb/(pi/|sigma|) = 1,17 bis 1,21 (3D, n >= 6) und 1,16 bis 1,17 (2D).
- **Grosses-omega-Formen:** Delta R_halb/(pi/(2 rho)) = 1,62 bis 1,66. Delta R_halb/(pi/(2 omega)) = 0,76 bis 0,78.
- **2D, Schritt 6 -> 7:** Die Stelle n = 6 hat nur zwei Profilzeilen im Abstand 0,002. R_halb aendert sich mit der
  Interpolationsart (x oder u) um 8,8e-3, die Phase also um etwa +-0,006.
- **h = 0,04 statt 0,02:** gleiche Werte auf allen gedruckten Stellen.

### 4b. Je Stelle: Eingaben und Innenwellenzahlen

| Stelle | omega^2 | rho | S0 | R_halb | R_tw | -rho_1 (Sc / S0) | -rho_2 (Sc / S0) | k1 (Sc / S0) | kappa_2 (Sc / S0) | k_-^2 aussen | rho - (1+omega) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3D n = 1 | 0,7976768 | 1,744618 | 1,04906 | 2,3051 | 2,3754 | 5,6142 / 5,4259 | -0,9315 / -1,2554 | 2,3694 / 2,3294 | 0,9651 / 1,1204 | -0,2750 | -0,1485 |
| 3D n = 6 | 0,5693598 | 1,599133 | 1,06334 | 10,3939 | 10,1948 | 4,2389 / 4,0168 | -0,9857 / -1,4331 | 2,0589 / 2,0042 | 0,9928 / 1,1971 | -0,2867 | -0,1554 |
| 3D n = 7 | 0,5598482 | 1,589920 | 1,05527 | 12,0336 | 11,8150 | 4,1686 / 3,9761 | -0,9932 / -1,3809 | 2,0417 / 1,9940 | 0,9966 / 1,1751 | -0,2916 | -0,1583 |
| 3D n = 8 | 0,5526191 | 1,582714 | 1,04902 | 13,6718 | 13,4382 | 4,1144 / 3,9446 | -0,9992 / -1,3412 | 2,0284 / 1,9861 | 0,9996 / 1,1581 | -0,2955 | -0,1607 |
| 3D n = 9 | 0,5469399 | 1,576925 | 1,04403 | 15,3097 | 15,0641 | 4,0714 / 3,9196 | -1,0041 / -1,3101 | 2,0178 / 1,9798 | 1,0021 / 1,1446 | -0,2988 | -0,1626 |
| 3D n = 10 | 0,5423644 | 1,572177 | 1,03997 | 16,9465 | 16,6911 | 4,0365 / 3,8991 | -1,0083 / -1,2850 | 2,0091 / 1,9746 | 1,0041 / 1,1336 | -0,3016 | -0,1643 |
| 2D n = 6 | 0,5338453 | 1,560892 | 1,03231 | 10,2613 | 10,4462 | 3,9607 / 3,8505 | -1,0203 / -1,2425 | 1,9902 / 1,9623 | 1,0101 / 1,1147 | -0,3107 | -0,1698 |
| 2D n = 7 | 0,5292654 | 1,556457 | 1,02808 | 11,8976 | 12,0809 | 3,9275 / 3,8320 | -1,0238 / -1,2163 | 1,9818 / 1,9576 | 1,0118 / 1,1029 | -0,3128 | -0,1710 |
| 2D n = 8 | 0,5257800 | 1,552990 | 1,02486 | 13,5320 | 13,7143 | 3,9018 / 3,8175 | -1,0266 / -1,1965 | 1,9753 / 1,9538 | 1,0132 / 1,0939 | -0,3146 | -0,1721 |

- **Quellen der Eingaben:**
  - 3D: R13 lauf-69/*-h002/praez.json (ziel_wechsel, x, S0, R_halb).
  - 2D: R12 lauf-69/f6, fein, f8 kurve.json; Lagen und rho aus R12 ERGEBNIS Z. 81 (n = 6), 196 (n = 7), 153 (n = 8).
  - S0 und R_halb sind linear in u = 1/(omega^2 - 1/2) zwischen den einschliessenden Zeilen interpoliert.
  - R_tw = (d-1)/(4 sqrt(beta) eps).
- **Ohne rho und R_halb:** n = 2 bis 5 und 11 bis 15. Dort gibt es nur die Schritte in 1/eps aus tab:ladder:
  2,042 (1 -> 2), steigend bis 2,307 (14 -> 15). Daraus folgt k_eff = 2 sqrt(beta) pi/Delta u = 2,175 bis 1,926.
- **Nebenbei [E]:** Aus den Tabellenwerten ergibt sich fuer 14 -> 15 ein Schritt von 2,3068 (Lauf zzz2). Der Text (Z. 326) nennt
  2,3055. Der Unterschied entspricht etwa 1e-6 in omega^2_15, also der Rundung von "~0,528469". Die Herkunft ist nicht
  geprueft.

## 5. Formulierungsvorschlag fuer LITERATURE.tex (nur Vorschlag; Papier unveraendert)

Einzufuegen nach dem Absatz zu Azatov2024 (LITERATURE.tex Z. 24-31):

> Zhang, Zhou, and Zhu treat wave scattering off thin-wall and multi-step Q-balls of the same sextic potential, with
> their $g$ equal to our $\beta$, analytically in terms of Bessel functions~\cite{ZhangZhouZhu2025}. For an interior
> value $f_0^2=1/(2\beta)$ their characteristic interior wavenumber $\sqrt{-\rho_1}$ coincides with $k_{\mathrm{in}}$ in
> Eq.~\eqref{eq:interior}; in their regime of two open exterior channels, $\rho>1+\omega$ in our notation, the
> amplification oscillates with the wall radius through the sum and difference of the two interior wavenumbers. The
> spacing description of Section~\ref{sec:thinwall} is related but applies below that threshold, where the second
> interior wave is evanescent, one interior half-wave per sequence step remains, and only one channel carries
> radiation. We therefore do not regard the near-uniform spacing as new; the results examined here concern the exact
> cancellation of the remaining open-channel amplitude.

Dazu ein Eintrag in bibliography.tex (Stil wie Azatov2024):

```
\bibitem{ZhangZhouZhu2025}
G.-D.~Zhang, S.-Y.~Zhou, and M.-F.~Zhu,
``$Q$-ball superradiance: Analytical approach,''
\href{https://arxiv.org/abs/2510.27064v1}{arXiv:2510.27064v1} (2025).
```

Pruefpunkte vor der Uebernahme:
- "coincides" gilt nur fuer f0^2 = 1/(2 beta), denn eq:interior benutzt D_c und C_c. Mit dem gemessenen S0 ist es dieselbe
  Formel an einer anderen Stelle.
- "only one channel carries radiation" folgt aus main.tex Z. 113-121.
- Die Aussage, ihre Verstaerkung sei dort trivial, ist [H] und steht bewusst nicht im Vorschlag.
- Die Superradianz-Reihe und die FLS-Arbeiten (R21) sind hier nicht eingearbeitet.

## 6. Grenzen, Suchprotokoll, Laufzeiten

**Grenzen:**
- **Lektuere:** Nur ZZZ v1 gelesen; eine spaetere Fassung zeigt die abs-Seite nicht. S. 18-21 (Literaturliste) nicht
  gelesen. Die Abbildungen sind nur in der Seitendarstellung des Read-Werkzeugs gesehen; Abb. 3 ist nicht vermessen.
- **Ungepruefte Fortsetzung:** Dass Gl. (108) in Regime II mit komplexem sigma_+- die Periode pi/k1 gibt, ist eine
  Vermutung [H].
- **Datenlage:** Leiterstellen mit rho, S0 und R_halb gibt es nur fuer n = 1, 6 bis 10 (3D) und n = 6 bis 8 (2D). Die
  Wandlage ist R_halb (S = S0/2) oder R_tw; das r_* von ZZZ ist eine scharfe Stufe.
- **Grenzwert:** b_inf ~ 2,3035 beruht auf einer linearen Extrapolation von rho - omega aus zwei Punkten
  (Kopfrechnung, [E/H]).
- **Zitationsabfrage:** nur Semantic Scholar, nur Titel. WebSearch stand nicht zur Verfuegung.

**Suchprotokoll (Zeiten per date, CEST):**

| Zeit | Abruf bzw. Schritt | Ergebnis |
|---|---|---|
| 20:08:35 | Start; Karte, main.tex, R13, R21, Resonanz Z. 20-35 gelesen | ARBEITSFELD Abschn. 0 |
| 20:10:34 | ARBEITSFELD.md mit Methode und Vorhersage angelegt | vor jedem Abruf |
| 20:10-20:11 | arxiv.org/abs/2510.27064 | Titel, v1 vom 31.10.2025, keine Zeitschrift |
| 20:11:20 | arxiv.org/pdf/2510.27064v1 per WebFetch | Abrufmodell kann das PDF nicht lesen; Datei unter ~/.claude/projects/.../tool-results/webfetch-1790964682001-qqmruj.pdf, S. 1-17 mit dem Read-Werkzeug gelesen (bis 20:15:49) |
| 20:20:14-20:20:46 | api.semanticscholar.org, Zitationen von arXiv:2510.27064 | 4 Titel |

**Laeufe (.69, kleintest.sh, Spur cpu, Verzeichnis /home/fmh/fmhc-physics-remote/runde22-zzz/):**

| Lauf | Start (CEST) | rc | CPU | Inhalt |
|---|---|---|---|---|
| zzz1 | 20:18:23 | 1 | 0,04 s | Abbruch: Schluessel "S0" doppelt belegt; Skript lokal per sed berichtigt, per rsync neu uebertragen |
| zzz2 | 20:18:43 | 0 | 0,044 s | zzz_abgleich.py: Wellenzahlen, Abstaende, Phasentests |
| zzz3 | 20:24:15 | 0 | 0,033 s | zzz_zusatz.py: f_max^2 gegen S0, ZZZ Abb. 2, Regimegrenze Abb. 3 |

- Syntaxpruefung auf der .69 (py_compile bzw. ast.parse, ohne __pycache__).
- Lokal nur jq, grep, sed, cat, ls, mkdir, rsync, ssh, sha256sum, date, wc und head; kein python, awk oder bc.
- Nichts im Scratchpad. Kein git, kein Peerbus, keine Unteragenten, keine Prozesse beendet.

**Dateien (sha256):**
- code/eingabe.json `70ef2f2ee873d2db7a23ac28298ec9468921cef081e6584a17af9c86545c35b9`, per jq aus den Laufdateien.
- code/zzz_abgleich.py `ae04936dfbd038b3f2c82858f87a45fb0d8be4cc9ae1f28536564dbb059f11ef` (lokal = .69).
- code/zzz_zusatz.py `d9f71125d026c9f6b57e814192ed712ae8cb52e454cab1132e2c8b93ea8ea136`.
- code/zzz_abgleich.json `79de08e3bab5c09f2576d715d7f781315b4ea9d0f83c38981bb883a84587dc0d` (lokal = .69).
- code/LAUF-zzz1.log `37d46a62...`, LAUF-zzz2.log `e6332d1e...`, LAUF-zzz3.log `33304800...`.

**Offene Fragen:**
- **An die Leitung bzw. Finn:**
  - Soll der Vorschlag aus Abschnitt 5 ins Papier, zusammen mit den R21-Luecken (Superradianz-Reihe, FLS, Oszillon-Dips)?
  - Welche Version gilt, v0.25 (README.txt) oder Draft 0.37 (main.tex)?
- **Pruefbar mit ZZZ Gl. (96) [H]:** Zeigt ihre Verstaerkung in Regime II die r_*-Periode pi/sqrt(-rho_1)? Probe bei
  omega_Q = 0,52, f0 = 1,2, g = 1/3 und omega in (1,52; 1,875).
- **Zum Papier:** Woher kommt der Unterschied 2,3055 (Text Z. 326) gegen 2,3068 (aus tab:ladder) fuer den Schritt
  14 -> 15?

**Quellen:**
- Zhang, G.-D.; Zhou, S.-Y.; Zhu, M.-F. (2025): Q-ball superradiance: Analytical approach. arXiv:2510.27064v1,
  https://arxiv.org/abs/2510.27064 [S, S. 1-17].
- Semantic Scholar Graph API, Zitationen von arXiv:2510.27064,
  https://api.semanticscholar.org/graph/v1/paper/arXiv:2510.27064/citations [L?]:
  - Evslin et al. 2026 (2604.07713)
  - Jaramillo et al. 2026 (2603.16995)
  - DeVries/Vassallo/Verhaaren 2026 (2602.15196)
  - Galushkina/Kim/Nugaev/Shnir 2025 (2511.16210)
- Projekt:
  - model-lab/papers/qball-bic-ladder-20260930/main.tex (Draft 0.37), sections/LITERATURE.tex, sections/bibliography.tex,
    README.txt;
  - coordination/runden-v3/RUNDE-13/leiter3d-praez/ (ERGEBNIS.md, lauf-69/*/praez.json, bic2_3d_praez.py);
  - coordination/runden-v3/RUNDE-12/leiter2d-praez/ (ERGEBNIS.md, lauf-69/f6, fein, f8);
  - coordination/runden-v3/RUNDE-21/fls-stille/ERGEBNIS.md;
  - coordination/resonance-20260930/ERGEBNIS.txt Z. 20-35.

## 7. Einfach gesagt

Unser Papier beschreibt eine Leiter von "stillen Stellen". Das sind Ballgroessen, bei denen eine Schwingung im Ball keine
Welle nach aussen abgibt. Von Sprosse zu Sprosse waechst der Ball um eine halbe Wellenlaenge der Welle im Inneren. Die Arbeit von
Zhang, Zhou und Zhu rechnet mit genau unserem Modell und benutzt genau dieselbe Formel fuer diese Innenwelle. Sie schaut
aber auf einen anderen Fall: Dort koennen Wellen in zwei Kanaelen ein- und auslaufen, und der Ball verstaerkt sie
manchmal. In unserem Fall ist einer der beiden Kanaele zu, und Verstaerkung gibt es dort gar nicht. Der Abstand der
Sprossen ist also kein neues Prinzip, wohl aber, dass die Abstrahlung an diesen Stellen exakt null wird. Das sollte das
Papier mit einem Zitat so sagen.

---
Letzte Aenderung dieser Datei: 2026-10-02 20:30:55 CEST (date, vor dem Anhaengen dieser Zeile gemessen). Zeitbox 75 min ab 20:08:35 eingehalten.
