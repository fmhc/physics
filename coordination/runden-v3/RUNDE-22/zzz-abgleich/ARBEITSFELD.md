# ARBEITSFELD zzz-abgleich (Runde 22, Literatur- und Schreibtisch-Agent)

- Beginn 2026-10-02 20:08:35 CEST (date). Zeitbox 75 min, also bis etwa 21:23 CEST.
- Diese Datei ist das gemeinsame Feld (Regel 5). Gestrichenes bleibt mit ~~...~~ stehen. Offene Rueckfragen stehen
  unten in "Offen" und wandern mit.
- Marken: [S] gelesen, [L?] nur Abstract/Zitat, [H] eigene Schlussfolgerung, [E] Rechnung (Kopf oder .69).

## 0. Schon gelesen (vor dem ersten Abruf), 20:08-20:10

- KARTE.md ganz [S].
- main.tex Z. 1-470 [S]. Phasenbedingung: Abschnitt "A thin-wall phase-matching description" Z. 288-347.
  - Z. 292: R_tw ~ 1/(2 sqrt(beta) eps), eps = omega^2 - 1/2.
  - Z. 299-301: k_in^2 = omega^2 + rho^2 - D_c + sqrt(4 omega^2 rho^2 + C_c^2), D_c = 1 + 1/(4 beta) = 3/2, C_c = 1/(2 beta) = 1.
    Das ist der groessere Eigenwert der konstanten Innen-Kanalmatrix (Z. 297 "Diagonalizing the constant interior channel matrix").
  - Z. 308-312: k_in(omega_n, rho_n) R_tw(omega_n) ~ pi [n + theta(eps_n)], rho_n ~ omega_n + c(eps_n); theta und c kalibriert (Z. 313-317).
  - Z. 321-326: eps_n ~ 1/(b_inf n), b_inf = 2 sqrt(beta) pi / k_inf; Schritte in 1/eps 2,3043 / 2,3054 / 2,3055 (n = 12-15);
    kalibriert 2,298, nackte Wandzustands-Schaetzung 2,334.
  - Z. 339-345: 2D-Folge, letzte Schritte ~4,62 gegen ~2,305 in 3D.
- Tabelle tab:ladder Z. 188-228 [S]: omega^2 fuer n = 1-15.
- Radialgleichungen Z. 104-118 [S]: Ansatz e^{i omega t}[a e^{i rho t} + b e^{-i rho t}]; A-Kanal Frequenz omega+rho (offen),
  B-Kanal omega-rho (geschlossen); D = 1 - 4S + 9 beta S^2, C = -2S + 6 beta S^2.
- RUNDE-13/leiter3d-praez/ERGEBNIS.md ganz [S]; praez.json (lauf-69/*-h002) per jq: x (= omega^2-Zeilen), S0 (= f0^2,
  Code Z. 1980), R_halb (S faellt auf S0/2, Code Z. 298-306), ziel_wechsel (omega*^2, rho*).
- RUNDE-21/fls-stille/ERGEBNIS.md ganz [S]; resonance-20260930/ERGEBNIS.txt Z. 20-35 [S] (2510.27064 dort nur
  "analytische Streuapproximation", Z. 29).

## 1. Methode (festgelegt 20:10, VOR dem Abruf von 2510.27064)

### 1a. Wellenzahlen aus der Arbeit uebernehmen

- Laut R21 (ERGEBNIS Z. 49-50): sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2) (2510.27064 Gl. 101-102, 109); Periode im
  Wandradius pi/sigma_+- (Gl. 114-118). rho_1, rho_2 sind vermutlich die Eigenwerte der konstanten Innen-Kanalmatrix
  im Stufenhintergrund. Das pruefe ich am Volltext.
- Vorgehen: (i) Gl. 101-102 woertlich abschreiben (mit deren Symbolen). (ii) Ihre Groessen auf unsere abbilden:
  ihre Stoerfrequenz omega <-> unser rho, ihre Q-Ball-Frequenz omega_Q <-> unser omega [H, erwartet wegen gleicher
  Kanalfrequenzen omega_Q +- omega]; ihr Potential auf U(S) = S - S^2 + S^3/2 skalieren; ihr Innenwert phi_0 bzw.
  |phi_0|^2 <-> unser S im Inneren. (iii) Die Abbildung an einem Grenzfall pruefen: grosses omega muss
  sigma_+ ~ 2 omega, sigma_- ~ 2 omega_Q geben (S. 13).
- Erwartete Folge [H, vorab]: In unserem Regime (1 - omega < rho < 1 + omega) ist nur EIN Innenkanal propagierend.
  Kopfrechnung n = 7 mit S = 1 [E]: k_+^2 = 1,5877 + 2,5809 = 4,169 (k_+ = 2,042), k_-^2 = 1,5877 - 2,5809 = -0,993
  (evaneszent, kappa = 0,997). Dann sind sigma_+- = k_+ +- i kappa komplex mit gleichem Realteil k_+ = k_in.
  Sollte das stimmen, fallen Summen- und Differenzwelle in ihrem schwingenden Anteil zusammen, und pi/Re sigma_+- =
  pi/k_in waere genau die Phasenbedingung des Papiers. Das ist eine Hypothese ueber die analytische Fortsetzung
  ihrer Formel in ein Regime, das sie womoeglich nicht behandeln (Kanaloffenheit als Moderator, Regel 1).

### 1b. Auswertung an unseren Leiterstellen

- Groessen aus unseren Dateien:
  - omega*^2, rho* fuer n = 1, 6, 7, 8, 9, 10: RUNDE-13 praez.json ziel_wechsel (h = 0,02).
  - S0 = f0^2 und R_halb je Zeile (9 Zeilen je Stelle): praez.json; an omega*^2 linear interpolieren.
  - omega^2 fuer n = 2-5, 11-15: tab:ladder (main.tex Z. 198-212); rho dort nicht im Papier -> nur
    mit rho ~ omega + c, c aus R13 extrapoliert [H], oder weglassen. Entscheidung unten.
  - 2D (RUNDE-12): omega^2 und rho_b fuer n = 7, 8 (ERGEBNIS Abschn. 1, 2a); R_halb/S0 nur, wenn in den Laufdateien.
- Zwei Lesarten der Innenamplitude: (A) Duennwand S = S_c = 1 (wie das Papier, D_c = 3/2, C_c = 1);
  (B) gemessenes S0 der Leiterstelle (D(S0), C(S0)).
- Gemessener Abstand: Delta R_halb zwischen benachbarten Stellen (n -> n+1) und, unabhaengig von R, die Schritte in
  1/eps (Papier Z. 325-326).
- Verglichen werden: Delta R_halb gegen pi/k_+ (Papier), pi/Re sigma_+, pi/Re sigma_- (ZZZ), und falls beide Innenkanaele
  reell: pi/(k_1 + k_2), pi/(k_1 - k_2). Toleranz fuer Z2: 5 % (Karte).
- Rechnung: kleines Skript auf der .69 (kleintest.sh, Spur cpu), oder Kopfrechnung [E].

## 2. Abrufe mit Vorhersage (Regel 3)

### A1 (geplant 20:10): arxiv.org/abs/2510.27064 und /html/2510.27064 (bzw. v1)
- **Vorhersage:** Einfeld-Sextik V = m^2|phi|^2 - lambda|phi|^4 + g|phi|^6 (o. ae.), Stufenhintergrund phi_0 fuer r < r_*,
  1+1 oder 3+1 D mit l = 0; zwei Kanaele omega_Q +- omega; Superradianz-Regime mit BEIDEN Kanaelen offen aussen;
  sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2) mit rho_i Eigenwerten der Innenmatrix; Verstaerkung als rationale Funktion
  von cos(sigma_- r_*), sin(sigma_+ r_*) (Gl. 108). Ihre Parameter entsprechen nach Skalierung NICHT genau beta = 1/2.

### A1 Ausgang (20:10-20:11): abs-Seite
- Bestaetigt (eine Zeile): Titel "Q-ball superradiance: Analytical approach", Zhang/Zhou/Zhu, v1 31.10.2025, 21 S., 8 Abb.,
  keine Zeitschriftenangabe auf der abs-Seite [S].

### A2 (20:11:20): PDF v1 per WebFetch (binaer gespeichert unter ~/.claude/projects/.../tool-results/webfetch-1790964682001-qqmruj.pdf),
mit dem Read-Werkzeug S. 1-17 gelesen (bis 20:15:49).
- Vorhersage wie A1-Plan (Abschnitt 2).
- Ausgang je Teil:
  - Modell: BESTAETIGT, sogar staerker. Gl. (1)-(3): V = |Phi|^2 - |Phi|^4 + g|Phi|^6 nach Umskalierung g = g~ m~^2/lambda~^2.
    Mit S = |Phi|^2 ist das U(S) = S - S^2 + g S^3, also unser Modell mit g = beta. Gl. (8): omega_Q,min^2 = 1 - 1/(4g)
    (= unser omega_c^2). Gl. (10) = unsere Profilgleichung (main.tex Z. 88) mit d = 3. Gl. (22)-(23): U = -4f^2 + 9g f^4,
    W = -2f^2 + 6g f^4, also unser D = 1 + U und C = W [S].
  - Parameter: Hauptbeispiele g = 1/3 (Abb. 1, 3-7); g = 1/2 nur in zwei Feldern von Abb. 2 [S, Legenden].
    ERWARTUNGSVERSTOSS (klein, nicht vorhergesagt): Abb. 2 unten rechts (g = 1/2, f0 = 1,25, r_* = 4) zeigt omega_Q = 0,55
    und 0,65. Nach ihrer Gl. (8) existiert bei g = 1/2 ein Q-Ball nur fuer omega_Q > 0,7071 [E]. Oben rechts
    (omega_Q = 0,75, f0 = 1,20, g = 1/2): f_max = 1,028 nach Gl. (14), also f0 ausserhalb von Gl. (15) [E]. Der Stufenansatz
    behandelt f0, r_* als freie Parameter; diese Felder sind keine Q-Ball-Loesungen ihrer eigenen Gl. (17).
  - Kanaele: BESTAETIGT. Gl. (24): phi = (eta_+ e^{-i omega t} + eta_- e^{i omega t}) e^{-i omega_Q t}, omega_+- = omega_Q +- omega.
    Abbildung auf uns: ihr omega <-> unser rho, ihr omega_Q <-> unser omega [S/H].
  - Regime: BESTAETIGT und entscheidend. Gl. (26): |omega_Q +- omega| > 1 (beide Kanaele aussen offen); S. 9: "omega > 1 +
    omega_Q, corresponding to propagating solutions" [S]. Unser Leiterregime 1 - omega < rho < 1 + omega liegt UNTER
    ihrer Schwelle (ihr omega < 1 + omega_Q): ein Kanal aussen geschlossen.
  - Innenwellenzahlen: BESTAETIGT, Gl. (40)-(42), (47)-(48): Innen J0(sqrt(-rho_1) r), J0(sqrt(-rho_2) r); "can be interpreted
    as characteristic perturbative wavenumbers" (S. 7) [S]. Gl. (101): -rho_1 = omega_Q^2 + omega^2 + sqrt(W^2 + 4 omega_Q^2 omega^2)
    - (1+U); Gl. (102) dasselbe mit Minus vor der Wurzel [S].
    -> -rho_1 ist WORTGLEICH unser k_in^2 (main.tex Z. 299-301), nach Abbildung omega_Q -> omega, omega -> rho, 1+U -> D, W -> C [H, Algebra trivial].
  - Verstaerkung gegen r_*: Gl. (108) (d = 2, n = 1, grosses r_*, Bessel-Asymptotik Gl. 107): N_+^out rationale Funktion von
    cos(sigma_- r_*), sin(sigma_+ r_*) [S]; Gl. (109): sigma_+- = sqrt(-rho_1) +- sqrt(-rho_2), C_+- = sqrt(rho_1 rho_2) +- k_+ k_-;
    Gl. (110) D_+-, F_+- [S]. Grosses omega: Gl. (114)-(118), sigma_+ ~ 2 omega, sigma_- ~ 2 omega_Q (S. 13, S. 14) [S].
    Abstract "peak spacing is simply the inverse of the Q-ball size" meint den Abstand in omega bei festem r_* (cos(2 r_* omega + phi_+),
    Gl. 115/118) [S/H].
  - Schwelle: Gl. (111)-(113): omega = 1 + omega_Q + eps, eps -> 0: N_+-^out -> 1, A^b -> 1 [S].
  - Keine Aussage zum Regime mit geschlossenem Kanal, zu gebundenen oder eingebetteten Moden (S. 1-17 durchgesehen) [S].

## 3. Befunde

- B1 [H, 20:16]: In unserem Regime ist -rho_2 < 0 (Kopfrechnung n = 7: -0,993 bei S = 1; -1,379 bei S = S0 [E]). Dann ist
  sqrt(-rho_2) = i kappa_2, sigma_+- = k_in +- i kappa_2, Re sigma_+ = Re sigma_- = k_in. Summen- und Differenzwelle fallen im
  schwingenden Anteil zusammen. Die "zwei Wellen" von ZZZ entarten zu EINER Innenwelle, und das ist k_in des Papiers.
- B2 [H]: Ihr Verstaerkungsfaktor ist bei uns nicht auswertbar: k_-^2 = omega_-^2 - 1 < 0 (Kanal B geschlossen), es gibt
  nur einen offenen Kanal; Teilchenzahlerhaltung (Gl. 59-60) laesst dann nur N^out = N^in = 1, also Verstaerkung 1.
  Ihre Formel (108) setzt reelle Bessel-Asymptotik beider Innenkanaele und beider Aussenkanaele voraus.
- B3 [E, Kopf, wird auf der .69 nachgerechnet]: Delta R_halb (3D, R13): 6->7 1,640; 7->8 1,638; 8->9 1,638; 9->10 1,637.
  pi/k_in lokal (n = 7): 1,539 (S = 1) bzw. 1,575 (S0 = 1,0553). Delta(k_in R_halb)/pi (7->8): 1,0068 (S = 1), 1,0054 (S0).
  Naive reelle Summe/Differenz (k_in +- kappa_2, n = 7, S = 1): pi/3,038 = 1,034 und pi/1,045 = 3,006.
  Grosses-omega-Formen: pi/(2 rho) = 0,988, pi/(2 omega) = 2,099.
- B4 [E]: 2D (R12): Delta R_halb 7->8 = 1,635, fast gleich wie 3D (1,638), obwohl die Schritte in 1/eps doppelt so gross sind
  (4,62 gegen 2,30). Duennwand: R_tw = (d-1)/(4 sqrt(beta) eps) [E, Laplace mit sigma_w = sqrt(beta) S_c^2/2; fuer d = 3 gleich
  main.tex Z. 292]; das erklaert den Faktor 2 in 1/eps bei gleichem Abstand in R.

### R1 (Rechnung .69, Vorhersage 20:18:12, vor dem Start)
- Skript code/zzz_abgleich.py (sha256 59447d83...), Eingabe code/eingabe.json (70ef2f2e..., per jq aus R13 praez.json h002/h004
  und R12 kurve.json f6/fein/f8; Lagen/rho 2D aus R12 ERGEBNIS Z. 81, 153, 196).
- Vorhersage: (a) Selbstpruefung ZZZ-(101) bei S_c gleich main.tex k_in auf Rundung. (b) -rho_2 < 0 an allen Stellen
  (3D und 2D). (c) Phasentest Delta(k1 R_halb)/pi = 1,00 bis 1,01 fuer 6->7 ... 9->10 (S_c und S0), Delta(k1 R_tw)/pi
  ~ 0,99-1,00. (d) Delta R_halb/(pi/k1) lokal 1,04-1,07. (e) naive Summe/Differenz, |sigma|, 2 rho, 2 omega alle > 5 % daneben.
  (f) 2D 6->7, 7->8 wie 3D. (g) 1->6 schlechter (n = 1 dickwandig).

### R1 Ausgang (Lauf zzz2, .69 Spur cpu, 18:18:43 UTC, rc = 0, 0,044 s CPU; zzz1 vorher rc = 1 wegen Schluesselkollision
"S0" im Skript, behoben, sha256 neu ae04936d...; Ergebnis code/zzz_abgleich.json 79de08e3..., Log code/LAUF-zzz2.log)
- (a) bestaetigt: chk = 0 (2D n = 6: -2,2e-16).
- (b) bestaetigt: -rho_2 = -0,93 bis -1,01 (S_c) bzw. -1,26 bis -1,43 (S0) in 3D; -1,02/-1,03 bzw. -1,20/-1,24 in 2D.
- (c) bestaetigt: Delta(k1 R_halb)/pi 3D = 1,0089/1,0068/1,0057/1,0045 (S_c), 1,0071/1,0054/1,0047/1,0036 (S0);
  Delta(k1 R_tw)/pi = 0,9974/0,9980/0,9988/0,9989 (S_c), 0,9954/0,9965/0,9976/0,9978 (S0).
- (d) bestaetigt: Delta R_halb/(pi/k1) = 1,070/1,061/1,055/1,049 (S_c), 1,043/1,038/1,034/1,030 (S0).
- (e) bestaetigt: Verhaeltnis Delta R_halb/(pi/X): naive Summe 1,57-1,66; naive Differenz 0,42-0,55; |sigma| 1,17-1,21;
  2 rho 1,64-1,66; 2 omega 0,77-0,78.
- (f) bestaetigt: 2D Delta R_halb = 1,636/1,634; Phasentest R_halb 1,0048/1,0031 (S_c), R_tw 1,0034/1,0020.
  Achtung: 2D n = 6 nur zwei Zeilen im Abstand 0,002; R_halb-Interpolation in x gegen u unterscheidet sich um 8,8e-3,
  also Phasenunsicherheit etwa +-0,006 fuer 6->7.
- (g) bestaetigt: 1->6 (5 Stufen) Phasentest R_halb 1,0146 (S_c) / 0,9843 (S0); R_tw 0,9779 / 0,9485.
- Zusatz: h = 0,04 gibt dieselben Werte auf allen gedruckten Stellen.
- Zusatz: Schritte in u aus tab:ladder: Delta u 2,042 (1->2) steigt auf 2,307 (14->15); k_eff = 2 sqrt(beta) pi/Delta u
  = 2,175 -> 1,926. Lokales k1 (S_c) an n = 6 ... 10: 2,059 ... 2,009. Die Luecke (k_eff < k1) ist die Drift von k1 entlang
  der Leiter; der Phasentest beruecksichtigt sie.
- Kein Erwartungsverstoss in R1.

### A3 (Gegensweep, ~20:20:20): Semantic Scholar, Zitationen von arXiv:2510.27064
- Vorhersage: 0 bis 5 zitierende Arbeiten, keine zu gebundenen oder eingebetteten Moden im Ein-Kanal-Regime.
  SELBSTANZEIGE: Diese Vorhersage hatte ich vor dem Abruf formuliert, aber erst danach eingetragen (Edit und Abruf liefen
  im selben Schritt). Regel 3 hier nur im Kopf eingehalten.
- Ausgang (bestaetigt, eine Zeile): 4 Treffer: Evslin et al. 2026 (2604.07713, schon im Papier als Evslin2026),
  Jaramillo et al. 2026 (2603.16995, Q-Stern-Schatten), DeVries/Vassallo/Verhaaren 2026 (2602.15196, rotierende Q-Baelle),
  Galushkina/Kim/Nugaev/Shnir 2025 (2511.16210, rotierende Klumpen in der Ebene) [L?, nur Titel].

### Lokale Pruefungen 20:21-20:23
- LITERATURE.tex (89 Z.) und bibliography.tex: 2510.27064, "Zhang", "superradian" kommen in main.tex, sections/*.tex und
  README.txt nicht vor (grep leer) [S].
- Version: README.txt Z. 2 "v0.25"; main.tex Z. 13 "Draft 0.37" (mtime 06:38:27). Die Karte nennt v0.25 und "um Z. 435";
  Z. 435 ist im aktuellen main.tex der Schluss ("phase-matching description"), die Herleitung steht Z. 288-347 [S].
- [E] S0 der Leiterstellen ist praktisch f_max^2 nach ZZZ Gl. (14): n = 7, g = 1/2, omega_Q^2 = 0,5598:
  f_max^2 = (1 + sqrt(1 - 1,5 * 0,4402))/1,5 = 1,05523 gegen S0 = 1,05527. Im Stufenbild von ZZZ entspricht unsere
  Innenamplitude also f0 = f_max(omega), die Lesart S0 ist die passende; S_c = 1 ist deren Grenzwert fuer eps -> 0.

### R2 (Rechnung .69, code/zzz_zusatz.py; Vorhersage eingetragen vor dem Start, ~20:24)
- Vorhersage: (1) |S0 - f_max^2| < 1e-3 an allen 3D-Stellen n >= 6 und in 2D; bei n = 1 groesser. (2) omega_Q,min = 0,70711;
  fuer omega_Q = 0,55 und 0,65 ist g_max (Gl. 16) < 1/2, also kein f_max; bei 0,75 f_max = 1,028. (3) -rho_2 = 0 bei
  omega ~ 1,875; Regime II fuer 1,52 < omega < 1,875.

### R2 Ausgang (Lauf zzz3, .69 cpu, 18:24:15 UTC, rc = 0, 0,033 s CPU; Log code/LAUF-zzz3.log; Skript sha256 d9f71125...)
- (1) bestaetigt, schaerfer: S0 - f_max^2 = -2,3e-6 / -1,3e-7 / +4,1e-8 / +2,0e-7 / +1,5e-7 (3D n = 6-10); 2D +2,3e-5 /
  -1,9e-7 / +2,1e-6; n = 1: -0,174 (dickwandig).
- (2) teils verletzt (klein): omega_Q,min = 0,70711 bestaetigt; omega_Q = 0,55: kein f_z, kein f_max; omega_Q = 0,65:
  f_max = 0,954 EXISTIERT, nur f_z fehlt (g_max = 0,433 < 1/2); 0,75: f_z = 0,804, f_max = 1,0284. Vorhersage "kein f_max bei
  0,65" war falsch; die Aussage "ausserhalb ihrer Existenzbedingungen" bleibt (Gl. 8 und Gl. 16 verletzt).
- (3) bestaetigt: -rho_2 = 0 bei omega = 1,875121; an der Schwelle 1,52: -0,906. Regime III (beide Innenwellen reell) z. B.
  omega = 2,0: pi/sigma_+ = 1,083, pi/sigma_- = 1,871, pi/k1 = 1,372.

## 3b. Wertung (20:23, vor dem Schreiben von ERGEBNIS.md)
- Z1: eingetroffen, staerker als erwartet (identisch, g = beta; nicht nur "bis auf Skalierung").
- Z2: im Wortlaut NICHT eingetroffen: Es gibt in unserem Regime keine reelle Summen- oder Differenzwelle; alle reellen
  Kandidaten liegen 17-66 % daneben. In der Sache: Der Abstand ist die Halbwelle von ZZZ's erster Innenwelle sqrt(-rho_1)
  (= k_in), auf 1 % im Phasentest, auf 3-4 % (S0) bzw. 5-7 % (S_c) lokal. Re sigma_+ = Re sigma_- = k1.
- Z3: offen (nicht pruefbar). Ihre Verstaerkung ist bei unseren Parametern identisch 1 (ein offener Kanal); "weder Maxima
  noch Minima" ist dort trivial wahr. Die Begruendung "Kopplung null statt Interferenz" ist damit nicht geprueft.
- Bedeutung: zwischen den beiden Aesten der Karte. Gemeinsamer Baustein (Innenwellenzahl, Halbwellenphase an der Wand),
  verschiedener Mechanismus und verschiedenes Regime. Zitieren; Neuheit nur bei der exakten, per Windung/Intervall belegten
  Stille, nicht beim Abstand.

## 3c. Gegensweep (Regel 4)
1. Zeilenbezug/Version der Karte: geprueft (siehe oben): v0.25 gegen Draft 0.37; Herleitung Z. 288-347.
2. n fortlaufend (keine ausgelassene Sprosse): geprueft [E]: Phase k1 R/pi waechst je Schritt um 0,995-1,009, von n = 1 bis 6
   um 5,07 (S_c, R_halb) bzw. 4,92 (S0). Keine fehlende Halbwelle im Phasenbild.
3. R_halb = r_* von ZZZ: teilweise geprueft mit R_tw; Abstaende 1,637-1,640 gegen 1,620-1,627, beide Phasentests <= 1 %.
4. ZZZ's g = 1/2-Felder seien Q-Baelle: geprueft, nein [E] (Gl. 8, 14-15).
5. Folgearbeiten zum geschlossenen Kanal: geprueft (A3), keine.
6. S0 = f0^2: geprueft (bic2_3d_praez.py Z. 1980).
7. Gilt ZZZ Gl. (108) auch im Regime II (beide Aussenkanaele offen, aber -rho_2 < 0)? NICHT geprueft -> Offen.
   [E] Fuer ihre Abb.-3-Parameter (omega_Q = 0,52, f0 = 1,2, g = 1/3) liegt -rho_2 = 0 bei omega = 1,875; Schwelle 1,52.

## 4. Erwartungsverstoesse

1. (A2, Regime) Nicht vorhergesagt in dieser Schaerfe: Die ZZZ-Analyse beginnt erst an der Schwelle omega = 1 + omega_Q;
   die Leiter liegt darunter (eps_ZZZ = rho - 1 - omega ~ -0,16). Damit ist Frage 4 nicht im Sinne von "Maxima/Minima"
   beantwortbar; ihre Verstaerkung ist dort identisch 1.
2. (A2, Modell) Vorhergesagt war "nicht genau beta = 1/2". Tatsaechlich ist die Familie identisch (g = beta), und zwei Felder
   von Abb. 2 nutzen g = 1/2, aber mit Parametern ausserhalb ihrer eigenen Existenzbedingungen (Gl. 8, 15).
3. (B1) Die Wellenzahl des Papiers ist nicht "aehnlich", sondern dieselbe Formel wie ZZZ Gl. (101).

## Offen

- Welche Leiterstellen ohne rho (n = 2-5, 11-15) werden ausgewertet? (Entscheidung nach dem Lesen.)

## 5. Abschluss
- ERGEBNIS.md geschrieben ab 20:27:03 (date); Korrekturen per sed: Schritt 14 -> 15 = 2,3068 (Lauf zzz2, vorher
  Kopfwert 2,3067), Wortlaut "Einfach gesagt". Letzter Stempel 20:30:55 (date).
- Offen (wandert mit): Regime-II-Probe mit ZZZ Gl. (96); Versionsfrage v0.25/Draft 0.37; Text Z. 326 (2,3055) gegen
  tab:ladder (2,3068); Entscheidung ueber den Vorschlag fuer LITERATURE.tex (Leitung/Finn).
