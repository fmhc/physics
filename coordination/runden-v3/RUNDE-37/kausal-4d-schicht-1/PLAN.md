# KAUSAL-4D-SCHICHT-1: Plan (Code-Agent fuer die Leitung, Runde 38, explorativ nach v3)

- Start des Code-Agenten 2026-10-04 08:53:29 CEST (date). Plantext ab 09:07:48 CEST (date vor dem Schreiben).
- Karte: KARTE.md. Vorhersagen SH0 bis SH3, Schwellen und Scheiterregeln unveraendert uebernommen (Abschnitt 7).
- Vor dem Plantext liefen nur Rauchlaeufe, die keine Werte von V-0 oder V-M zeigen (Abschnitt 10).
- Code (code/):
  - kausal4d.py, kontinuum4d.py: unveraendert aus KAUSAL-WELLE-4D (sha256 46311620... bzw. 4462504d..., die dort
    eingefrorenen Fassungen); nur importiert.
  - schicht_feld.py: Teil B. Links und 1-Element-Intervalle aus einem GEMM, drei Varianten je Streuung, Probe, Repro.
  - schicht_kont.py: Teil A. Pole, Argumentprinzip, zweites Blatt, Erwartung je Variante, Kontinuum, Linkzahlen.
  - schicht_auswertung.py: Urteile, Bilder, auswertung.json.
- Kennzeichen: [S] an der Quelle gelesen (hier: ueber Dossier/Arbeitsfeld bzw. KAUSAL-WELLE-4D); [L] Literatur aus dem
  Gedaechtnis, [L?] unsicher; [M] eigene Mathematik; [F] Festlegung dieses Plans (von der Karte offengelassen);
  [E] im Rauch gesehen; [H] Hypothese.

## 1. Varianten

- Sprungregel: Phi = sum_n a_n L_n. L_n[y, x] = 1, wenn y vor x und das offene Intervall I(y, x) genau n Elemente der
  Menge enthaelt. L_0 = Links, L_1 = 1-Element-Intervalle. Halt b = -m^2/rho in allen drei Varianten (Johnston (3.44)).
- a = sqrt(rho)/(2 pi sqrt 6) (Johnston (3.44), [S] in KAUSAL-WELLE-4D):

  | Variante | a_0 (Links) | a_1 (1-Element) | sigma = a_0 + a_1 |
  |---|---|---|---|
  | V-J | a | 0 | +a |
  | V-0 | 2a | -2a | 0 |
  | V-M | 3a | -4a | -a |

- **Technik:** C (float32) wie KAUSAL-WELLE-4D. Je Block P = C[I0:I1, I0:J1] C[I0:J1, J0:J1]. Links: C = 1 und P = 0;
  1-Element-Intervalle: C = 1 und P = 1.
  - Zwischenindex auf [I0, J1) beschraenkt; das ist vollstaendig, weil die Menge nach t sortiert ist.
  - Zaehler sind ganze Zahlen < N < 2^24, in float32 also exakt.
- **Rekursion [M]:** Phi^T = a (c0 L_0^T + c1 L_1^T). psi = J - (m^2/rho) Phi^T psi (Dreieckssystem), phi = (1/rho) Phi^T psi.
  - Herleitung: phi(x) = (1/rho) sum_y (K - I)(y, x) J(y), K - I = Phi (I - b Phi)^-1; transponiert
    (I - b Phi^T)^-1 Phi^T = Phi^T (I - b Phi^T)^-1.
- **Zuschauer (Palm):** phi(p) = (1/rho) sum_y Phi(y, p) psi(y). S = C Pm zaehlt die Elemente in I(y, p); Link bei S = 0,
  1-Element-Intervall bei S = 1.
- **Gebiet D** kausal konvex wie in KAUSAL-WELLE-4D [M]: Jedes Intervall zwischen Punkten von D liegt in D. Damit sind
  auch die 1-Element-Intervalle in D exakt, und phi ist an jedem Punkt von D exakt.

## 2. Normierung mit Herleitung [M]

- **Erwartungswert:** Die offenen Intervalle entlang einer Kette sind paarweise disjunkt (Dossier 3.1).
  - Die Poisson-Wahrscheinlichkeit "genau n_i Elemente in I_i" faktorisiert deshalb.
  - Mecke: E[#Pfade mit Sprungtypen n_1 ... n_j] = rho^(j-1) (mu_(n_1) * ... * mu_(n_j)).
  - Dabei mu_n(tau) = (c tau^4)^n/n! exp(-c tau^4) mit c = pi rho/24 (V = (pi/24) tau^4, Johnston (3.33)).
  - Daraus K_P~ = k~_gen/(1 + m^2 k~_gen), k~_gen = sum_n a_n mu_n~ (b rho = -m^2).
- **Fouriertransformierte** (KAUSAL-WELLE-4D, Dossier 3.1, ASS (3.7) laut Dossier):
  F(Z) = (4 pi/Z) int tau^2 f(tau) K1(Z tau) dtau mit Z^2 = |k|^2 - omega^2 und Re Z > 0.
- **Fuehrende Ordnung** (K1(x) ~ 1/x): mu_n~ ~ (4 pi/Z^2) int tau mu_n dtau. Mit u = c tau^4 gilt
  int tau mu_n dtau = Gamma(n + 1/2)/(4 sqrt(c) n!), also mu_n~ ~ (pi/sqrt c) (Gamma(n + 1/2)/n!)/Z^2.
  - Kontinuumsgrenze 1/Z^2 genau dann, wenn sum_n a_n Gamma(n + 1/2)/n! = sqrt(c)/pi.
  - Johnston: a Gamma(1/2) = a sqrt(pi) = sqrt(rho)/(sqrt 24 sqrt pi) = sqrt(c)/pi. Das ist die Normierung.
- **Pruefung der Varianten:**
  - V-J: a sqrt(pi).
  - V-0: 2a sqrt(pi) - 2a (sqrt(pi)/2) = a sqrt(pi).
  - V-M: 3a sqrt(pi) - 4a (sqrt(pi)/2) = a sqrt(pi).
  - **Alle drei haben dieselbe fuehrende Ordnung. Die Kartenkoeffizienten stimmen; kein Kartenfehler.**
- **Naechste Ordnungen** (K1(x) = 1/x + (x/2) ln(x/2) + (x/4)(2 gamma - 1) + (x^3/16) ln(x/2) + ...):
  - ln Z^2-Koeffizient: (pi/(4c)) sum a_n, denn int tau^3 mu_n dtau = 1/(4c) fuer jedes n. Fuer V-J ist das
    eps = sqrt 6/(2 pi sqrt rho).
  - Z^2 ln Z^2-Koeffizient: (pi/(32 c^(3/2))) sum a_n Gamma(n + 3/2)/n!.
    Die Summe ist +a sqrt(pi)/2 (V-J), -a sqrt(pi)/2 (V-0) bzw. -3a sqrt(pi)/2 (V-M).
  - Konstante fuer V-0: -eps, also Massenschale bei M^2 = m^2/(1 - eps m^2).
- **Schreibtisch-Pole [M, erste nichtverschwindende Ordnung, grob bei m^2/sqrt(rho) >= 0,25]:**
  - V-J: Im omega = (sqrt 6/4) m^4/(omega sqrt rho), Wachstum.
  - V-0: Im omega = 3 M^6/(16 rho omega), Wachstum. Bei k = 0 gibt das 0,081 / 0,034 / 0,015 (rho = 4 / 8 / 16), wie
    die Karte.
  - V-M: erster Term -(sqrt 6/4) m^4/(omega sqrt rho). Die Nullstelle liegt dann auf dem zweiten Blatt (Abschnitt 4),
    also Zerfall.

## 3. Erwartung und Kontinuum (Teil A)

- **Kontinuum:** k-Raum (exakt je Mode) und direkte Faltung mit Johnston (3.25), gekappt, Funktionen aus kontinuum4d.py
  unveraendert. Bezug fuer Zuwachs und Streuung ist die gekappte direkte Faltung (wie KV1/KV2).
  - Norm n_c,k je Zeitscheibe aus dem k-Raum, wie KV3.
- **Erwartung E[phi_v]:** wie kontinuum4d.johnston_punkte, mit k~_gen statt a mu~. Quadratur:
  - tau: 64 Gauss-Legendre-Knoten auf [0, (40/c)^(1/4)]
  - omega: Gitter 0,05 auf der Linie Im omega = Gamma
  - k: Spline mit dk = 0,1
- **Gamma [F]:** Gamma_1 = max(0,8; groesstes Im omega aller gefundenen Nullstellen bei k = 0 + 0,5), Gamma_2 = Gamma_1 + 0,6.
  - Das gilt je Variante und Dichte. Gegenprobe: E bei Gamma_1 gegen Gamma_2.
  - [M] Bei k = 0 liegt fuer jede Nullstelle das groesste Im omega: Bei festem Z0^2 gilt omega^2 = k^2 - Z0^2, mit k
    waechst Re omega bei festem Im omega^2. Jede Nullstelle des physikalischen Blatts erscheint bei k = 0 in
    Im omega > 0.
- **Punkte:** 18 Pruefpunkte und 17 Profilpunkte (wie KAUSAL-WELLE-4D), dazu 19 Achsenpunkte (0, 0, v t) mit
  t = 0,4 bis 4,0 in Schritten von 0,2 (nur Bild "Zuwachs gegen t").
- **Dichten:** rho = 4, 8, 16 und 10^6 (Grenzfall, nur Gamma_1).
- **Erwartete Linkzahlen [M]:** L0/N und L1/N fuer D bei rho = 8 und 16, nur beschreibend.
  - Innen (6/pi) int dOmega dchi sinh^2 chi mal [1 - e^-U] bzw. [1 - (1 + U) e^-U], U = c tau_max^4.
  - Grobe Aufloesung von kontinuum4d.linkzahl_erwartung.

## 4. Pole und Argumentprinzip (Teil A)

- **g(omega) = 1 + m^2 k~_gen(Z)**, Z = Hauptwert sqrt(k^2 - omega^2), Re Z > 0. Analytisch in Im omega > 0, denn der Kern
  ist beschraenkt und retardiert. Nullstellen dort sind wachsende Moden.
  - Spiegelsymmetrie omega -> -conj(omega), weil der Kern reell ist.
  - tau-Quadratur 128 Knoten; Probe 256 Knoten an der Schalennullstelle und auf dem Bogen.
- **Zweites Blatt [M]:** Fortsetzung aus Im omega > 0 ueber den zeitartigen Schnitt (Re omega > k) nach Im omega < 0:
  k~_II = k~_gen - D, D(Z) = (4 pi^2 i/Z) int tau^2 f I1(Z tau) dtau.
  - Herleitung aus K1(z e^(-i pi)) = -K1(z) + i pi I1(z) [L, DLMF 10.34]. Fuehrend ist D = 2 pi i (pi/(4c)) sum a_n,
    der Sprung von ln Z^2.
  - Probe: Stetigkeit g_I(x + i e) gegen g_II(x - i e).
- **Regionen [F]** (k = 0 und k = p = sinh 0,5):
  - **A:** abs(omega) < 10 und Im omega > 0,05 (Kartenwortlaut). Kontur: Strecke Im omega = 0,05 von links nach rechts,
    dann Bogen abs(omega) = 10.
  - **S, "nahe der Massenschale":** Re omega in [0,5; 2,0], Im omega in [0,002; 1,0]. Rechteck, positiv orientiert.
    Nullstellen mit 0 < Im omega < 0,002 sieht die Zaehlung nicht (Aufloesungsgrenze).
- **Zaehlung:** Windungszahl von g laengs der Kontur, adaptiv verfeinert.
  - Zwei Aufloesungen: 2 000 Startpunkte je Stueck mit Schranke 0,25 rad je Schritt, und 4 000 mit 0,12 rad.
  - "Stabil" heisst: Beide Aufloesungen sind aufgeloest und geben dieselbe ganze Zahl.
  - Synthetische Probe mit bekannten Nullstellen.
- **Lokalisierung:** lokale Minima von abs(g) auf einem Gitter (A: Schritt 0,1; S: Schritt 0,01), dann Newton. Die Zahl
  der gefundenen Nullstellen wird gegen die Zaehlung geprueft.
- **Massenschalen-Nullstelle [F]:**
  - Ist N_S >= 1: die Nullstelle in S, die omega_0 = sqrt(k^2 + m^2) am naechsten liegt (Blatt I).
  - Ist N_S = 0: die Nullstelle von g_II nach Newton ab omega_0 - 0,05 i (Blatt II), gueltig bei Im omega < 0 und
    Re omega > k.
  - Im omega(v, rho, k) ist ihr Imaginaerteil, auf Blatt II also negativ.
- **Weitere Nullstellen:** N_weitere = N_A minus 2 fuer das Schalenpaar (omega_s, -conj(omega_s)), wenn die
  Schalennullstelle auf Blatt I liegt und Im omega_s > 0,05; sonst minus 0.
- **Groessenprobe (beschreibend):** max abs(m^2 k~_gen) auf abs(omega) = 10 und 20. Ist sie << 1, gibt es dort keine
  Nullstellen.

## 5. Felder (Teil B)

- Gebiet D, Quelle (sigma = 1, eta = 0 und 0,5, Kappe R_S = 3,5), Pruefpunkte, Profil, Zeitscheiben und Normmessung
  unveraendert aus KAUSAL-WELLE-4D (kausal4d.py).
- Je Saat eine Streuung, darauf alle drei Varianten und beide Konfigurationen.
- **Saaten [F]:** rho = 16 und rho = 8, je Saaten 1 bis 12, SeedSequence([20261004, 38, 141, 1000 rho, s]).
  - Das ist eine neue Folge; KAUSAL-WELLE-4D hatte Tag 81, also sind die V-J-Werte nicht dieselben wie dort.
  - Rauch: Saat 91. Probe: Tag 143, rho = 1,2.
- **Laeufe:** rho = 16 in vier Bloecken zu drei Saaten, Zeitgrenze 540 s je Lauf. Fehlende Saaten folgen in weiteren
  Laeufen mit denselben Nummern. rho = 8 in einem Lauf.

## 6. Statistik und Groessen

- **Saatmittel und Standardfehler:** SE_c = sqrt(var Re + var Im)/sqrt(n), ddof = 1, wie KAUSAL-WELLE-4D.
- **Relative Streuung** je Punkt sd/abs(K) mit sd = sqrt(var Re + var Im) und K = gekappte direkte Faltung.
  - s_v(rho) ist das geometrische Mittel ueber die 18 Pruefpunkte, wie KV2.
- **Zuwachs [F]:** Z_v,c = [abs(E_v)/abs(K)](t = 3,2) / [abs(E_v)/abs(K)](t = 2,0) an Lage A (Paketmitte) der
  Konfiguration c, bei rho = 16.
  - E_v ist die Erwartung aus Teil A bei Gamma_1, K die gekappte Faltung.
  - Zur Kontrolle: Fuer V-J und eta = 0 ergab KAUSAL-WELLE-4D 1,62/1,30 = 1,25.
  - Z_v ist das Maximum ueber beide Konfigurationen (strenge Lesart).
  - Beschreibend daneben dieselbe Groesse aus den Saatmitteln, die Werte je Konfiguration und an den Lagen B und C.
- **Norm:** R_k = Saatmittel(n_k)/n_c,k und G = R_4/R_1 je Variante, wie KV3 (nur beschreibend).

## 7. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| SH0 | Kontrolle: Das Saatmittel von V-J trifft Johnstons Erwartung an >= 15 von 18 Punkten innerhalb 3 SE | 85 % |
| SH1 | Im omega(V-0, rho = 16, k = 0) liegt in [0; 0,05] (Schaetzung 0,015) und faellt von rho = 4 bis 16 mindestens um den Faktor 3. V-M hat keinen Pol mit Im omega > 0 nahe der Massenschale. Keine weitere Nullstelle mit Im omega > 0,05 bei abs(omega) < 10 | 50 % |
| SH2 | Das Saatmittel von V-0 trifft seine eigene Erwartung an >= 15 von 18 Punkten. Der Zuwachs abs(E phi)/abs(Kontinuum) von t = 2,0 bis 3,2 ist <= 1,10 (V-J: 1,25), bei V-M unter 1 | 50 % |
| SH3 | [H, Preis] Die relative Streuung je Saat ist bei V-0 groesser als bei V-J (0,33 bei rho = 16); Prognose 0,5 bis 1,0 | 55 % |

- **Scheitern (Karte):**
  - SH1 scheitert bei Im omega(V-0) > 0,075, wenn V-M nicht das Vorzeichen wechselt, oder bei einer weiteren
    Nullstelle mit Im omega > 0,05 bei abs(omega) < 10.
  - SH2 scheitert bei Zuwachs > 1,15.
  - SH3 ist in beide Richtungen informativ: unter 0,33 heisst "kein Preis", ueber 1,5 heisst "unbrauchbar".
- **Lesart von Vorhersage und Scheiterregel [F]:** Die Karte laesst einen Graubereich offen (SH1: 0,05 < Im omega <= 0,075;
  SH2: 1,10 < Zuwachs <= 1,15).
  - "eingetroffen" heisst: Jeder Teil des Vorhersagewortlauts gilt.
  - Sonst "nicht eingetroffen". In werte steht getrennt "scheiterregel_ausgeloest" (ja/nein).
  - Im Graubereich lautet das Urteil "nicht eingetroffen", mit Vermerk "Graubereich, Scheiterregel nicht ausgeloest".
  - Die Bedeutungszeile "SH1 verfehlt" der Karte knuepfe ich an die Scheiterregel.
- Alle Urteile rechnet code/schicht_auswertung.py mechanisch.

### 7.1 SH0 [F]

- Bei rho = 16, an den 18 Pruefpunkten: abs(Saatmittel V-J - E_VJ) <= 3 SE_c.
- Eingetroffen bei >= 15 von 18. rho = 8 nur beschreibend.
- Nicht auswertbar, wenn bei rho = 16 weniger als 12 Saaten vorliegen, ein Wert nicht endlich ist oder die
  Gamma-Gegenprobe von E_VJ(16) > 1e-6 relativ ist.

### 7.2 SH1 [F]

Teile:
- (a) Im omega(V-0, 16, k = 0) liegt in [0; 0,05]. Massgeblich ist die Massenschalen-Nullstelle aus Abschnitt 4; auf
  Blatt II ist Im omega < 0, dann ist (a) nicht erfuellt.
- (b) Im omega(V-0, 4, 0) >= 3 Im omega(V-0, 16, 0).
- (c) Fuer V-M ist N_S = 0 bei rho = 4, 8, 16 und k = 0, p, also keine Nullstelle mit Im omega > 0 nahe der
  Massenschale. Das ist zugleich "V-M wechselt das Vorzeichen".
- (d) N_weitere = 0 fuer V-0 und V-M bei rho = 4, 8, 16 und k = 0, p.
  - V-J wird nur beschreibend gezaehlt. "weitere" bezieht sich auf die geaenderten Sprungregeln.

Urteil:
- Eingetroffen, wenn (a), (b), (c) und (d) gelten.
- Scheiterregel ausgeloest bei (i) Im omega(V-0, 16, 0) > 0,075, (ii) nicht (c) oder (iii) nicht (d).
- Nicht auswertbar, wenn eine benoetigte Zaehlung nicht stabil ist oder die Schalennullstelle von V-0 bei rho = 4 oder
  16 (k = 0) nicht bestimmbar ist.

### 7.3 SH2 [F]

- (a) Bei rho = 16, an den 18 Pruefpunkten: abs(Saatmittel V-0 - E_V0) <= 3 SE_c an >= 15 Punkten.
- (b) Z_V0 <= 1,10 (Maximum ueber beide Konfigurationen, Abschnitt 6).
- (c) Z_VM < 1 (Maximum ueber beide Konfigurationen).
- Urteil: eingetroffen, wenn (a), (b) und (c) gelten. Scheiterregel ausgeloest bei Z_V0 > 1,15.
- Nicht auswertbar, wenn bei rho = 16 weniger als 12 Saaten vorliegen, ein Wert nicht endlich ist oder die
  Gamma-Gegenprobe von E_V0(16) oder E_VM(16) > 1e-6 relativ ist.

### 7.4 SH3 [F]

- Bei rho = 16: s_V0 und s_VJ wie in Abschnitt 6, auf denselben Saaten.
- Eingetroffen, wenn s_V0 > s_VJ und 0,5 <= s_V0 <= 1,0.
- Vermerke nach Kartenwortlaut: s_V0 < 0,33 heisst "kein Preis", s_V0 > 1,5 heisst "unbrauchbar".
- Beschreibend daneben: s_V0/s_VJ, s_VM, rho = 8, die Streuung bezogen auf abs(E_v) und die Steigung von 8 nach 16.
- Nicht auswertbar bei weniger als 12 Saaten (rho = 16) oder nicht endlichen Werten.

## 8. Kontrollen (ohne Urteilskraft)

- **Codeprobe** (rho = 1,2, N ~ 1 500, Bloecke 256):
  - Links und 1-Element-Intervalle aus dem GEMM gegen dichtes C C (float64)
  - C gegen Koordinaten
  - Rekursion je Variante gegen dichte Loesung und Reihe
  - Zuschauer je Variante gegen eine Schleife, die die Elemente in I(y, p) explizit zaehlt
- **Repro:** V-J mit der Saatfolge von KAUSAL-WELLE-4D (rho = 4, Saat 1) gegen deren gespeicherte Werte.
- **Teil A:**
  - synthetische Windungsprobe; zwei Aufloesungen je Zaehlung; lokalisierte Zahl gegen gezaehlte Zahl
  - Blattstetigkeit; tau-Quadratur 128 gegen 256 (Pole) bzw. 64 gegen 128 (Erwartung, V-0 und V-M bei rho = 4)
  - Gamma-Gegenprobe; rho = 10^6 gegen den k-Raum fuer alle drei Varianten
  - V-J-Pole und V-J-Erwartung gegen KAUSAL-WELLE-4D
- **Teil B:** L0/N und L1/N gegen die exakten Integrale (3 SE, beschreibend); max abs(phi) je Variante; Endlichkeit.

## 9. Hinweise zur Karte (vor dem Einfrieren)

1. **Normierung:** geprueft (Abschnitt 2). Die drei Koeffizientensaetze haben dieselbe fuehrende Ordnung; kein
   Kartenfehler. Die Urteile nach Kartenwortlaut sind deshalb dieselben wie nach diesem Plan.
2. **Offen gelassen und festgelegt [F]:**
   - Dichte fuer SH0, SH2(a) und SH3: rho = 16.
   - Bedeutung von "E phi" in SH2: die Erwartung aus Teil A, wie beim V-J-Bezugswert 1,25.
   - Lage, Konfiguration und Maximum fuer den Zuwachs.
   - Regionen A und S, Kontur, Aufloesungen, Definition der Schalennullstelle und von "weitere".
   - Fuer (c) und (d): alle drei Dichten und k = 0, p.
   - Lesart des Graubereichs (Abschnitt 7).
   - Saatfolge.
3. **Eigene Vorab-Erwartung [M/H], vor jedem Wert von V-0 oder V-M:**
   - SH0 eingetroffen (90 %): KAUSAL-WELLE-4D hatte 18 von 18 bei rho = 16. Neue Saaten.
   - **SH1: Risiko durch UV-Nullstellen.** Fuer abs(Z) >> c^(1/4) gilt k~_gen ~ 8 pi a_0/Z^4, und a_0 ist bei V-0
     doppelt, bei V-M dreimal so gross wie bei V-J.
     - 1 + m^2 k~ = 0 verlangt dann Z^4 ~ -8 pi a_0 m^2, also abs(Z) ~ 1,9 (V-0, rho = 16) bzw. ~1,8 (V-M, rho = 4).
       Das waere Im omega ~ 1,2 bis 1,4 bei abs(omega) ~ 2.
     - Die Naeherung gilt dort nicht (abs(Z)/c^(1/4) ~ 1,6 bis 2). Wechselnde Vorzeichen (vgl. BD bei ASS) machen
       solche Nullstellen aber plausibel.
     - Meine Erwartung: SH1 eingetroffen 35 %. Die Schalennullstelle von V-0 schaetze ich aus der Spektraldichte auf
       Im omega ~ 0,013 (rho = 16); der Wert faellt nach der Formel um ~5 von rho = 4 bis 16.
   - SH2 (40 %): Gibt es eine UV-Nullstelle, dominiert sie die Erwartung, und der Zuwachs ist gross.
   - SH3 (55 %): Grobe Abschaetzung aus den Zaehlern. Bei rho = 4 ist L1/L0 ~ 0,4 (Repro-Rauch, Abschnitt 10).
     Unabhaengige Beitraege geben s_V0/s_VJ ~ sqrt(4 (1 + 0,4)) ~ 2,4, also s_V0 ~ 0,8; s_VM ~ 1,3 [H].

## 10. Rauch (vor dem Plantext und vor dem Einfrieren)

Ordner rauch-69/ (Kopie aus /home/fmh/fmhc-physics-remote/runde38-kausal-schicht/rauch/); .69-Zeiten in UTC, alle rc = 0.

- **Codeprobe** (07:03:45 bis 07:04:23 UTC, rho = 1,2, N = 1 478, L0 = 32 134, L1 = 11 369):
  - Links und 1-Element-Intervalle aus dem GEMM gleich dichtem C C: ja. C gleich Koordinaten: ja.
  - Rekursion gegen dichte Loesung: 3,2e-16 / 4,5e-16 / 4,4e-16 (V-J / V-0 / V-M). Reihe: <= 3,2e-16.
  - Zuschauer gegen Schleife: <= 6,5e-16.
  - Gesehen habe ich nur diese Pruefgroessen, keine Feldwerte.
- **Repro** (07:03:47 bis 07:03:53 UTC, rho = 4, Saat 1, Tag 81):
  - N = 5 089 und L0 = 237 138 gleich KAUSAL-WELLE-4D.
  - phi_p(V-J) bitgleich (Abweichung 0,0), Normsummen 3e-17 relativ.
  - Dabei gesehen: L1 = 95 815, ein Zaehler ohne Feldwert.
- **Pole nur V-J, rho = 16** (07:06:43 bis 07:07:05 UTC, 22 s):
  - k = 0: 1,0545310671831 + 0,1523220987990 i. KAUSAL-WELLE-4D (96 statt 128 Knoten): 1,0545310671831 +
    0,1523220987990 i.
  - k = p: 1,17434 + 0,13678 i.
  - N_A = 2 (das Schalenpaar), N_S = 1, N_weitere = 0; beide Aufloesungen stabil; lokalisiert = gezaehlt.
  - 256 Knoten aendern die Nullstelle um 3e-15. max abs(m^2 k~) auf abs(omega) = 10: 7e-4.
  - Synthetische Windungsprobe 3/3 und 1/1.
  - Blattstetigkeit bei e = 1e-7: 3e-6. Das passt zu 2 e abs(g') nahe dem Lichtkegel. Die Probe laeuft im
    Hauptlauf mit e = 1e-6 und 1e-8.
- **Zeit rho = 16, Saat 91** (p4000a, 07:06:28 bis 07:08:44 UTC):
  - N = 20 385, L0 = 2 140 832, L1 = 942 371; Links 122,5 s, gesamt 134,7 s je Saat; 1,72 GB; endlich.
  - Angesehen habe ich nur die Druckzeile (Zeit, Speicher, N, L0, L1, endlich), keine Feldwerte.
  - Folge: drei Saaten je Lauf passen unter 540 s.
- **Erwartung nur V-J, rho = 16** (cpu6, 07:10:01 bis 07:11:20 UTC, 78,5 s):
  - Gamma 0,8 / 1,4; Gegenprobe 1,1e-14. rho = 10^6 gegen k-Raum: 0,72 % (54 Punkte).
  - E[L0]/E[N] = 105,37049 wie KAUSAL-WELLE-4D; E[L1]/E[N] = 46,476.
  - Zeit: Kontinuum 28 s, je Variante und Dichte ~17 s (zwei Gamma).
- **Nicht gerechnet vor dem Einfrieren:** Pole, Erwartung oder Felder von V-0 und V-M ausser der Codeprobe und der
  Druckzeile des Zeitlaufs. schicht_auswertung.py ist vor dem Einfrieren nicht gelaufen (Abschnitt 11).

## 11. Laeufe nach dem Einfrieren

- **cpu6:** pole (rho 4, 8, 16; alle Varianten), dann erwartung, dann feld 16 Saaten 4 bis 6, dann feld 16 Saaten 10
  bis 12.
- **p4000a:** feld 16 Saaten 1 bis 3, feld 16 Saaten 7 bis 9, feld 8 Saaten 1 bis 12.
- Pfadprobe der Auswertung: nach pole und erwartung einmal auf dem Rauchfeld (Saat 91, rho = 16, n_soll = 1).
  Bricht sie ab, ist das ein Codefehler; die Behebung wird offengelegt. Die Urteile dieser Probe zaehlen nicht.
- Danach schicht_auswertung.py auf lauf/ (rho 8, 16; 12 Saaten).
- Hoechstens zwei Laeufe zugleich. Je ssh-Aufruf ein Starteraufruf.
- Die Spur p4000a nutze ich nur als Lock; das Skript rechnet auf der CPU mit einem Gewinde, die GPU bleibt unbenutzt.

## 12. Einfrieren

- Kopie PLAN.md.eingefroren-JJJJMMTT-HHMMSS (Zeit per date), Code-Kopien mit derselben Endung, sha256 in
  code/pruefsummen-einfrieren.txt.
- Danach aendern sich Plan und Urteilsregeln nicht. Code nur bei echten Fehlern, offengelegt im ERGEBNIS.
