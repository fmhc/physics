# BEWEIS-PLAN BEWEIS-1 (M0): Strahlungsfreie Atmungsmode des 3D-Q-Balls, linear

- Autor: Beweis-Agent (Claude, Haus Anthropic), Auftrag RUNDE-07/beweis/BRIEF.md.
- Begonnen 2026-09-30 05:35:09 CEST (date). Stand dieser Fassung siehe STAND.md.
- Status (Fassung nach M3 und nach der Lesung LESUNG-PLAN.md): Lemmata mit Beweisen, Rechnerteil ausgefuehrt und
  bestanden. Der endgueltige Satz mit allen Zahlen steht in BEWEIS.md, Abschnitt 1; massgeblich ist jene Fassung.
  Einarbeitung der Lesung: Abschnitt 9.

## 1. Satz (Zielwortlaut; Zahlen und endgueltige Fassung in BEWEIS.md)

Bezeichnungen: U(S) = S - S^2 + S^3/2, N(f) := (1 - omega^2) f - 2 f^3 + (3/2) f^5.

Wortwahl nach der Lesung:
- "Eingebettet" heisst operational: rho* liegt im Kontinuum des freien Bueschels, (omega* + rho*)^2 > 1, und es
  gibt eine nichttriviale L^2-Loesung (W3).
- "Zeitperiodisch" gilt nur im mitrotierenden Rahmen (Periode 2 pi/rho*); delta phi selbst ist quasiperiodisch (W3).
- f ist die Loesung des Anfangswertproblems zu (a*, omega*); ob sie die einzige positive radiale Loesung ist,
  wird nicht behauptet [L?] (K1).
- Nicht behauptet: die Nichtexistenz weiterer Nullstellen in Z (K2).

**Satz (im linearen Modell).** Es gibt einen Kasten Z (BEWEIS.md 1 und 3.2, explizite dyadische Grenzen) und darin
(a*, c*, rho*, omega*) mit omega*^2 in [0,797676787111865191750 +- 4,8e-22] und
rho* in [1,744617544837398735781 +- 6,8e-22], so dass gilt:

1. **Profil.** Die Loesung f von f'' + (2/r) f' = N(f), f(0) = a*, f'(0) = 0, existiert auf [0, unendlich),
   ist positiv, und f(r) r e^{kappa0 r} -> c* > 0 fuer r -> unendlich (kappa0 = sqrt(1 - omega*^2)).
   phi = e^{i omega* t} f(|x|) ist also ein positiver radialer Q-Ball der NLKG
   phi_tt - Laplace phi + U'(|phi|^2) phi = 0.
2. **Eingebettete Eigenfrequenz.** Mit S = f^2, V_pm = U'(S) + U''(S) S - (omega* pm rho*)^2 und C = U''(S) S
   hat das System A'' = V_+ A + C B, B'' = V_- B + C A eine nichttriviale reelle Loesung mit A(0) = B(0) = 0 und
   |A(r)| + |B(r)| <= K e^{-kappa_c r} fuer r >= L, kappa_c = sqrt(1 - (omega* - rho*)^2) > 0.
3. **Folgerung.** a(x) = A(|x|)/|x| und b(x) = B(|x|)/|x| sind glatte, exponentiell abfallende radiale
   Funktionen (in jedem H^s(R^3)), und
   delta phi(t, x) = e^{i omega* t} ( a(x) e^{i rho* t} + b(x) e^{-i rho* t} )
   loest die um phi linearisierte NLKG. Es gilt 1 - omega* < rho* < 1 + omega*: Der Kanal omega* + rho* ist
   offen (k = sqrt((omega* + rho*)^2 - 1) > 0), der Kanal omega* - rho* geschlossen. Die Mode ist ein gebundener
   Zustand im Kontinuum (l = 0) der Linearisierung: im mitrotierenden Rahmen 2 pi/rho*-periodisch, raeumlich lokalisiert,
   ohne Abstrahlung.

Nicht behauptet: nichtlineare Strahlungsfreiheit (Codex zeigt Abstrahlung in der zweiten Harmonischen, Fluss
~ epsilon^4; bic-proof/), Eindeutigkeit von (rho*, omega*) im Kasten, Aussagen fuer l > 0.
Ob f "der" Q-Ball ist (Eindeutigkeit positiver radialer Loesungen), ist Literaturfrage [L?], nicht tragend.

## 2. Modellabgleich (Auftrag Abschnitt 1)

- Linearisierung selbst nachgerechnet: phi = e^{i omega t}(f + psi), |phi|^2 = f^2 + f (psi + psi*) + O(psi^2).
  Erste Ordnung: psi_tt + 2 i omega psi_t - omega^2 psi - Laplace psi + U'(S) psi + U''(S) S (psi + psi*) = 0.
  Ansatz psi = a e^{i rho t} + b e^{-i rho t}, a, b reell: Koeffizient von e^{i rho t} gibt
  -Laplace a + (U' + U'' S - (omega + rho)^2) a + U'' S b = 0, von e^{-i rho t} die zweite Gleichung. Stimmt mit dem
  BRIEF ueberein. Mit U' + U'' S = 1 - 4S + (9/2) S^2 und U'' S = -2S + 3S^2.
- bic2.py (Zeilen 27-33, lin_aufbau, direkt_m): dp = 1 - 4S + 9 beta S^2, sp = -2S + 6 beta S^2, beta = 1/2:
  identisch. Konvention dort phi = [f + u e^{-i rho t} + v* e^{i rho t}] e^{-i omega t}: konjugiert gleichwertig.
  Profil F(f) = a0 f - 2 f^3 + 3 beta f^5, a0 = 1 - omega^2: identisch. W-Funktion dort = Wronski-Form der
  regulaeren Loesungen mit der abklingenden geschlossenen Loesung: gleiche BIC-Bedingung.
- Codex (3D-ABLEITUNG-CODEX.txt, bic-tail/run.py): D0 = 1 - 4f^2 + 4.5 f^4, S0 = -2f^2 + 3f^4, Profil
  f'' + 2f'/r = (1 - omega^2) f - 2 f^3 + 1.5 f^5, Rueckwaertsstart (u, v, u', v')(R) = (0, 1, 0, -kappa):
  identisch mit dem BRIEF. Abweichung nur in der Randbehandlung: Codex setzt das Potential jenseits R null
  (Codex nennt das selbst Naeherung); hier wird der Schwanz streng behandelt (Lemma P, Lemma J).
- Ergebnis: keine Abweichung in den Gleichungen gefunden.

## 3. Nullstellenformulierung (Abweichung vom Architekturvorschlag, begruendet)

Statt F(rho, x) mit einem vorab als stetig in omega bewiesenen Profilast werden **alle** Groessen gleichzeitig
gesucht: z = (a, c, rho, omega), a = f(0), c = Schwanzamplitude. Grund: Die Stetigkeit und Eindeutigkeit des
Profilasts in omega ist dann nicht noetig. Die Brouwer-Aussage liefert direkt ein zusammenpassendes Paar
(Profil, Mode). Das deckt Punkt (c) "Eindeutigkeit und Stetigkeit in omega" des Vorschlags ab, ohne Literatur.

Festes L (dyadisch, Vorwahl L = 40), feste Referenzwellenzahl khat (dyadisch, nahe k(z0)).

- Vorwaerts von 0 bis L (streng, Abschnitt 5): Profil f_a (Schuss mit f(0) = a) und zwei regulaere Loesungen
  R_1 (A(0) = 0, A'(0) = 1, B(0) = B'(0) = 0) und R_2 (A(0) = A'(0) = 0, B(0) = 0, B'(0) = 1), gerechnet mit f_a.
- Schwanz ab L (analytisch, Lemma P und J): Profil f_c(r) ~ c e^{-kappa0 r}/r, Jost-Loesung Psi mit
  e^{kappa_c r} Psi -> (0, 1), gerechnet mit f_c.
- H(z) = H_0(z) + E(z) mit
  - H_0,1 = s1 (f_a(L) - c e^{-kappa0 L}/L),
  - H_0,2 = s1 (f_a'(L) + c (kappa0 + 1/L) e^{-kappa0 L}/L),
  - H_0,3 = s3 (B_1'(L) + kappa_c B_1(L)),  H_0,4 = s3 (B_2'(L) + kappa_c B_2(L)),
  - s1 = L e^{kappa0 L}, s3 = e^{-kappa_c L} als feste dyadische Konstanten (nur Skalierung),
  - E = Schwanzkorrekturen, stetig in z, mit expliziten Schranken |E_i| <= eps_i auf Z (Lemma P, J).
- H(z*) = 0 bedeutet: Profil passt bei L in Wert und Ableitung an den abklingenden Schwanz (also globale
  Loesung), und W(Psi, R_i) = 0 fuer i = 1, 2, also Psi(0) = 0 (Lemma W): BIC.

H_0,3 und H_0,4 sind W(J_0, R_i) mit J_0 = (A, B, A', B') = (0, 1, 0, -kappa_c) (normierte freie Jost-Daten);
E_3, E_4 = s3 W(Psi_n - J_0, R_i) mit Psi_n = e^{kappa_c L} Psi(L).

## 4. Lemmata mit Beweisen

### Lemma P (Profilschwanz, stabile Mannigfaltigkeit), explizite Konstanten

Voraussetzungen: omega in (1/sqrt 2, 1), kappa0 = sqrt(1 - omega^2), L > 0, c > 0, phibar > 0. Setze
- K := (2 + (3/2) phibar^2) e^{-2 kappa0 L} / (4 kappa0^2 L^2),  eta := 2 K c^3,  m := c + eta,
- Lambda := (6 + (15/2) phibar^2) m^2 e^{-2 kappa0 L} / (4 kappa0^2 L^2).
Es gelte (i) m e^{-kappa0 L}/L <= phibar, (ii) K m^3 <= eta, (iii) Lambda < 1, (iv) c > eta.

Aussage: Es gibt genau ein stetiges u~ auf [L, oo) mit sup |u~ - c| <= eta und
u~(r) = c + int_r^oo G(r,s) q(s) u~(s) ds, G(r,s) = (1 - e^{-2 kappa0 (s-r)})/(2 kappa0),
q = -2 f^2 + (3/2) f^4, f(s) := e^{-kappa0 s} u~(s)/s. Dieses f ist C^2, loest f'' + (2/r) f' = N(f) auf [L, oo),
0 < f(r) <= m e^{-kappa0 r}/r, und mit eta0 := K m^3:
- |L e^{kappa0 L} f(L) - c| <= eta0,
- |e^{kappa0 L} (L f'(L) + f(L)) + kappa0 c| <= 2 kappa0 eta0.
(f(L), f'(L)) haengt stetig von (c, omega) ab.

Beweis. X = {u~ in C_b([L, oo)): ||u~ - c|| <= eta} ist vollstaendig. Fuer u~ in X gilt |u~| <= m,
|f(s)| <= m e^{-kappa0 s}/s <= phibar nach (i) (e^{-kappa0 s}/s faellt), also
|q(s)| <= (2 + 1.5 phibar^2) m^2 e^{-2 kappa0 s}/s^2. Mit 0 <= G <= 1/(2 kappa0) und
int_r^oo e^{-2 kappa0 s} s^{-2} ds <= e^{-2 kappa0 r}/(2 kappa0 r^2) folgt |T u~(r) - c| <= K m^3 <= eta nach (ii).
Die Abbildung u~ -> q u~ = -2 e^{-2 kappa0 s} s^{-2} u~^3 + 1.5 e^{-4 kappa0 s} s^{-4} u~^5 hat auf X die Ableitung
<= (6 + 7.5 phibar^2) m^2 e^{-2 kappa0 s}/s^2 dem Betrag nach, also ist T eine Kontraktion mit Konstante
Lambda < 1 (iii). Banach liefert den Fixpunkt. u := e^{-kappa0 r} u~ erfuellt
u(r) = c e^{-kappa0 r} + int_r^oo sinh(kappa0 (s - r))/kappa0 q u ds; zweimaliges Ableiten gibt
u'' - kappa0^2 u = q u, also f = u/r: f'' + 2f'/r = (kappa0^2 + q) f = N(f). Positivitaet aus u~ >= c - eta > 0 (iv).
Randwerte: |u~(L) - c| <= K m^3 aus der Selbstabbildungsschranke bei r = L;
e^{kappa0 r} u'(r) + kappa0 c = -int_r^oo (1 + e^{-2 kappa0 (s - r)})/2 q u~ ds, Betrag
<= (2 + 1.5 phibar^2) m^3 e^{-2 kappa0 r}/(2 kappa0 r^2) = 2 kappa0 K m^3 bei r = L; u' = f + r f'.
Stetigkeit: T haengt stetig von (c, omega) ab, gleichmaessig kontrahierend in einer Umgebung. QED.

Folgerung fuer E_1, E_2 (mit E0 := e^{-kappa0 L}):
|E_1| <= s1 E0 eta0 / L und |E_2| <= s1 E0 (2 kappa0 eta0 / L + eta0 / L^2).

### Lemma J (Jost-Loesung), explizite Konstanten

Voraussetzungen: k = sqrt((omega + rho)^2 - 1) > 0, kappa_c = sqrt(1 - (omega - rho)^2) > 0, S stetig auf
[L, oo) mit 0 <= S(s) <= m^2 e^{-2 kappa0 s}/s^2 und S <= phibar^2 (aus Lemma P). Setze
Q := (6 + (15/2) phibar^2) m^2 e^{-2 kappa0 L}/(2 kappa0 L^2), mu := max(1/k, 1/(2 kappa_c)), eps := e^{mu Q} - 1.

Aussage: Das System A'' + k^2 A = dV A + C B, B'' - kappa_c^2 B = dV B + C A (dV = -4S + 4.5 S^2,
C = -2S + 3S^2; das ist A'' = V_+ A + C B, B'' = V_- B + C A) hat eine Loesung Psi = (A_d, B_d) auf [L, oo) mit
A~ = e^{kappa_c r} A_d, B~ = e^{kappa_c r} B_d und fuer alle r >= L:
- |A~| <= eps/(mu k), |B~ - 1| <= eps/(2 mu kappa_c),
- |A~' - kappa_c A~| <= (sqrt(1 + kappa_c^2/k^2) + kappa_c/k) eps/mu, |B~' - kappa_c (B~ - 1)| <= (3/2) eps/mu.
Insbesondere |A_d(r)| + |B_d(r)| <= (1 + eps/(mu k) + eps/(2 mu kappa_c)) e^{-kappa_c r}, Psi ist nicht null, und
Psi_n := e^{kappa_c L} Psi(L) = J_0 + E_J mit den obigen Komponentenschranken. Psi haengt stetig von
(rho, omega, c) ab.

Beweis. Volterra-System A~ = int_r^oo K_A (dV A~ + C B~), B~ = 1 + int_r^oo K_B (dV B~ + C A~) mit
K_A(r,s) = sin(k(s-r)) e^{-kappa_c (s-r)}/k, K_B(r,s) = (1 - e^{-2 kappa_c (s-r)})/(2 kappa_c);
|K_A| <= 1/k, 0 <= K_B <= 1/(2 kappa_c). Mit q_J := |dV| + |C| <= 6S + 7.5 S^2 und
Q(r) := int_r^oo q_J <= Q konvergiert die Picard-Reihe gleichmaessig (n-tes Glied <= (mu Q)^n/n!).
psi := max(|A~|, |B~|) erfuellt psi(r) <= 1 + mu int_r^oo q_J psi, Gronwall: psi <= e^{mu Q(r)}.
Dann |A~(r)| <= (1/k) int q_J psi <= (1/k)(e^{mu Q} - 1)/mu, denn int_r^oo q_J e^{mu Q(s)} ds = (e^{mu Q(r)} - 1)/mu;
ebenso |B~ - 1|. Ableitungen: A~' = int d_r K_A (...) mit |d_r K_A| <= sqrt(1 + kappa_c^2/k^2),
B~' = -int e^{-2 kappa_c (s - r)} (...), |.| <= (e^{mu Q} - 1)/mu. Differenzieren der Volterra-Gleichungen zeigt,
dass (A_d, B_d) das System loest. Stetigkeit: gleichmaessige Konvergenz mit stetigen Kernen. QED.

Folgerung: |E_{2+i}| <= s3 (|E_A| |A_i'(L)| + |E_B| |B_i'(L)| + |E_A'| |A_i(L)| + |E_B'| |B_i(L)|), i = 1, 2.

### Zusatz S (Stetigkeit von E auf ganz Z, Auflage W5)

Die Konstanten von Lemma P und J werden in Kugelarithmetik **ueber ganz Z** ausgewertet: c geht als obere Schranke
cab von |c| ueber Z ein, omega und rho als Kugeln. Die Bedingungen (i)-(iv) und k^2 > 0, kappa_c^2 > 0 gelten
dann fuer jedes z in Z (keine Monotonie noetig; Zahlen in BEWEIS.md, Tabelle 3.2).
- Lemma P: Sei X' := {u~ : sup |u~ - c0| <= delta_c + eta}. Fuer jedes z in Z ist die eigene Kugel X_z in X'
  enthalten. Auf X' gilt |u~| <= m, also die Lipschitz-Schranke Lambda < 1 fuer jedes T_z. Fuer z, z' in Z:
  ||u~_z - u~_z'|| <= Lambda ||u~_z - u~_z'|| + ||(T_z - T_z') u~_z'||, also
  ||u~_z - u~_z'|| <= (1 - Lambda)^{-1} sup_{X'} ||(T_z - T_z') u~||.
  Der letzte Term geht gegen 0 fuer z' -> z. Denn T haengt linear von c ab, und der Kern G sowie die Gewichte
  e^{-2 kappa0 s}/s^2 haengen stetig von omega ab und sind fuer omega in Z durch eine integrierbare Funktion
  majorisiert (dominierte Konvergenz). Damit sind (f(L), f'(L)) und E_1, E_2 stetig auf Z. Ebenso ist das
  Schwanzprofil f_z auf [L, oo) stetig in der gewichteten Supremumsnorm.
- Lemma J: Die Picard-Iterierten sind stetig in (rho, omega, c) (Kerne stetig, S = f_z^2 stetig). Sie konvergieren
  gleichmaessig ueber Z (n-tes Glied <= (mu Q)^n/n! mit den Z-Konstanten). Also ist Psi_n(z) stetig. R_i(L)
  haengt nach ODE-Theorie glatt von z ab, also sind E_3, E_4 stetig. QED.

### Lemma E (Einfachheit der Mode, Auflage W4)

Voraussetzung: 2 kappa0 > kappa_c auf Z (gemessen: 2 kappa0 - kappa_c >= 0,375236). Sei z* wie im Satz, Psi die
Jost-Loesung, und Phi eine Loesung von A'' = V_+ A + C B, B'' = V_- B + C A auf (0, oo) mit Phi in L^2((L, oo)).
Dann ist Phi ein Vielfaches von Psi. Insbesondere ist der Raum der L^2-Loesungen mit Phi(0) = 0 gleich span{Psi}.

Beweis.
1. Abfall von Phi: Auf [L, oo) sind die Koeffizienten beschraenkt. Aus Phi in L^2 folgt Phi'' = M Phi in L^2. Mit
   der Interpolationsungleichung auf Einheitsintervallen, int_I |Phi'|^2 <= C (int_I |Phi|^2 + int_I |Phi''|^2),
   folgt Phi' in L^2. Also Phi, Phi' in H^1((L, oo)), und damit Phi(r), Phi'(r) -> 0.
2. Oszillierende Loesungen: Es gibt Loesungen Psi_c, Psi_s auf [L, oo) mit Psi_c - (cos kr, 0) -> 0 und
   Psi_s - (sin kr, 0) -> 0 samt Ableitungen. Konstruktion (fuer cos) durch das Volterra-System
   - A(r) = cos(kr) + int_r^oo sin(k(s-r))/k (dV A + C B)(s) ds,
   - B(r) = int_r^oo sinh(kappa_c (s-r))/kappa_c (dV B + C A)(s) ds.
   Kernschranke fuer L <= r <= s: max(1/k, e^{kappa_c (s-L)}/(2 kappa_c)) =: kt(s). Mit q_J <= const e^{-2 kappa0 s}/s^2
   ist Qt := int_L^oo kt q_J ds endlich, weil 2 kappa0 > kappa_c. Die Picard-Reihe konvergiert (n-tes Glied
   <= Qt^n/n!). Die Integralterme und ihre Ableitungen gehen gegen 0 (Reste konvergenter Integrale, fuer B mit
   e^{kappa_c (s - r)} e^{-2 kappa0 s} <= e^{-(2 kappa0 - kappa_c) s}).
3. Wronski-Formen: W(Psi_c, Psi_s) = lim (cos kr * k cos kr + k sin kr * sin kr) = k != 0. W(Psi, Psi_c) = 0 und
   W(Psi, Psi_s) = 0, weil Psi, Psi' -> 0 und Psi_c, Psi_s beschraenkt sind (Ableitungen ebenso). Nach Schritt 1
   ebenso W(Phi, Psi) = W(Phi, Psi_c) = W(Phi, Psi_s) = 0.
4. W ist eine nichtausgeartete schiefe Bilinearform auf dem vierdimensionalen Loesungsraum (Standardform auf den
   Cauchy-Daten). V3 := span{Psi, Psi_c, Psi_s} ist dreidimensional:
   - Psi_c und Psi_s sind unabhaengig, weil W = k != 0.
   - Psi liegt nicht in span{Psi_c, Psi_s}: Dort hat jede Loesung die A-Komponente beta cos kr + gamma sin kr + o(1),
     die fuer (beta, gamma) != 0 nicht gegen 0 geht, waehrend Psi -> 0 und Psi != 0.
   Das W-Komplement von V3 ist eindimensional und enthaelt Psi, ist also span{Psi}. Nach 3 liegt Phi darin. QED.

Folge: Die BIC-Mode ist im Sektor l = 0 einfach. Codex' Hypothesen H1/H4 (OBSTRUCTION.txt: einfache radiale Mode,
kein zweiter unabhaengiger Modenanteil bei rho) sind damit fuer l = 0 abgedeckt. Nicht abgedeckt: Moden mit l > 0
bei derselben Frequenz.

### Lemma W (Wronski-Form, BIC-Kriterium)

Fuer Loesungen Psi, Phi von Y'' = M(r) Y mit symmetrischem M = [[V_+, C], [C, V_-]] ist
W(Psi, Phi) = Psi . Phi' - Psi' . Phi konstant (W' = Psi . M Phi - M Psi . Phi = 0). Fuer Phi = R_i gilt bei r = 0:
W(Psi, R_i) = Psi_i(0). Bei z* ist das Profil f_a auf [0, L] und f_c auf [L, oo) eine einzige Loesung (gleiche
Cauchy-Daten bei L), die Jost-Loesung setzt sich als Loesung auf (0, oo) fort, und H_{2+i}(z*) = s3 W(Psi_n, R_i) = 0
fuer i = 1, 2 heisst Psi(0) = 0. Mit Psi != 0 (Lemma J) ist das der BIC. Umkehrung (jede L^2-Loesung ist Vielfaches
von Psi) wird fuer den Satz nicht gebraucht.

### Lemma T (strenger Taylor-Schritt)

System y' = F(r, y), F analytisch auf Dt x B (Auflage W2 der Lesung: fuer das Profil steht 2/r in F, also muss das
Quadrat r_j + Dt den Punkt 0 ausschliessen, d. h. **R < r_j**; das wird vor jedem Schritt in Kugelarithmetik geprueft,
bewkern.apriori: `if not (R < rj): raise`; im Gitter gilt R <= r_j/2; Protokollfeld R_kleiner_rj_alle = true).
D = {|r - r_j| <= R}, B kompakte konvexe Menge (Produkt komplexer Rechtecke),
Y0 reelle Kugeln der Anfangswerte. Gilt in Kugelarithmetik Y0 + Dt * F(Dt, B) in B (Dt = Quadrat mit
Halbseite R, enthaelt D), dann hat fuer jedes y0 in Y0 die Loesung eine analytische Fortsetzung auf D mit Werten
in B. Fuer n >= 1 gilt |y_n| <= beta R^{-n} (beta = maximaler Abstand eines Punkts von B zur Mitte, je Komponente),
und fuer 0 < h < R:
y(r_j + h) in sum_{n<N} y_n h^n + [-beta q^N/(1-q), beta q^N/(1-q)], q = h/R.

Beweis. Picard-Operator T y(r) = y0 + int_{[r_j, r]} F(s, y(s)) ds auf der abgeschlossenen Menge
{y stetig auf D, analytisch im Innern, y(D) in B}. Das Integral ist (r - r_j) mal ein Mittel von F-Werten, liegt also
in (r - r_j) conv F(D x B) und damit in Dt * F(Dt, B) (Rechtecke sind konvex): T bildet die Menge in sich ab.
T^m ist Kontraktion (Volterra-Abschaetzung (Lambda R)^m/m!), der Fixpunkt ist analytisch und stimmt auf der reellen
Strecke mit der Loesung ueberein. Cauchy-Ungleichung fuer y - Mitte auf Kreisen |t| = R' < R, dann R' -> R.
Die y_n (n < N) werden aus Y0 per Rekursion in Kugelarithmetik berechnet; Inklusionsisotonie. QED.

Suche und Pruefung der Huelle sind getrennt (Auflage K5): Die Suche (epsilon-Inflation, Faktor 9/8, hoechstens 14
Runden) ist beliebig; zaehlt nur der anschliessende Einschlusstest Y0 + Dt F(Dt, B) in B (acb_contains fuer jede
Komponente). Ein Schritt wird nur mit bestandenem Test angenommen, sonst wird R verkleinert. Protokoll je Schritt:
zertifikat/*-SCHRITTE-KASTEN.json (r_j, R, h, Inflationsrunden, Fehlversuche, Rest).

**Zusatz J (Jet-System, Auflage W6).** Im Kastenlauf werden 38 reelle Komponenten gemeinsam integriert:
Profil (f, g = f') [2]; Profilvariationen (phi_a, psi_a), (phi_om, psi_om) mit phi'' + (2/r) phi' = N'(f) phi + d_p N,
d_a N = 0, d_om N = -2 om f, phi_a(0) = 1, phi_om(0) = 0 [4]; R_1, R_2 in (al, be, B, B') [8]; deren Ableitungen nach
a, rho, om [24]. Kettenregel in den Koeffizienten: d_p S = 2 f phi_p, d_p dV = (9S - 4) d_p S, d_p C = (6S - 2) d_p S;
explizit d_rho P = -2(om + rho), d_rho Q = 2(om - rho), d_om P = -2(om + rho), d_om Q = -2(om - rho) mit
P = dV + khat^2 - k^2, Q = dV + kappa_c^2. In H_0 kommen hinzu: d_rho kappa_c = (om - rho)/kappa_c,
d_om kappa_c = -(om - rho)/kappa_c, d_om e^{-kappa0 L} = L om e^{-kappa0 L}/kappa0, d_om kappa0 = -om/kappa0, und die
c-Ableitungen der Profilzeilen. Gemessene relative Breiten von D = DH_0(Z): <= 1,92e-9 (Lauf A). Die Huellen des
Zustands selbst sind im Kastenlauf bei L breit (relativ 34 fuer f, 58 fuer R_i; Folge der Parameterbreite mal
e^{kappa0 L}); das betrifft nur E_3, E_4 (dort in den Schranken enthalten), nicht D.

### Lemma T0 (Start bei r = 0)

Profil: f(r) = a + r^2 int_0^1 tau (1 - tau) N(f(tau r)) dtau, f'(r) = r int_0^1 tau^2 N(f(tau r)) dtau; ebenso fuer die
Profilvariationen (Quelle N'(f) phi + d_omega N). Bedingung: a + (Dt^2/6) N(B_f) in B_f, dann B_g := (Dt/3) N(B_f).
Der Rest fuer f'(h) kommt aus der Cauchy-Schranke von g = f' mit beta_g aus B_g (Mitte 0), Koeffizienten
g_n = (n+1) f_{n+1} (Auflage K4).
Das lineare System in (A, B) ist bei 0 regulaer (l = 0): Standardfall von Lemma T. Koeffizienten:
(n+2)(n+3) f_{n+2} = [N(f)]_n. Beweis wie Lemma T; der Integraloperator ist vom Volterra-Typ
(Iterierte <= (Lambda R^2)^m/(2m+1)!). QED.

### Lemma K (Brouwer-Krawczyk mit Stoerterm)

Z = z0 + [-delta, delta] in R^4, H = H_0 + E stetig auf Z, H_0 in C^1 mit DH_0(z) in einer Intervallmatrix D fuer
alle z in Z, |E_i| <= eps_i auf Z, Y eine feste reelle Matrix. Gilt
Kr := z0 - Y H_0(z0) + (I - Y D)(Z - z0) + |Y| [-eps, eps] in Z,
dann hat T(z) = z - Y H(z) nach Brouwer einen Fixpunkt z* in Z. Ist zusaetzlich die kastengewichtete Zeilensumme
max_i sum_j |I - Y D|_ij delta_j / delta_i < 1, so ist Y invertierbar und H(z*) = 0. (Die ungewichtete Norm ist bei
stark verschieden skalierten Unbekannten ungeeignet: in Lauf A ist sie <= 27253, die gewichtete <= 5,7e-9.)

Beweis. Fuer jede Zeile k gilt nach dem Mittelwertsatz (z - Y H_0(z))_k = (z0 - Y H_0(z0))_k +
((I - Y DH_0(xi_k))(z - z0))_k mit xi_k in Z, also in Kr_k ohne den E-Anteil; -Y E(z) liegt in |Y| [-eps, eps].
Also T(Z) in Kr in Z. Invertierbarkeit: fuer A = DH_0(z0) in D gilt |I - Y A| <= P := |I - Y D| (eintragsweise) und
P delta < delta mit delta > 0, also Spektralradius rho(I - Y A) <= rho(P) < 1 (Perron-Frobenius), Y A invertierbar. QED.

### Lemma Pos (Positivitaet des Profils)

Auf [0, L_p] folgt f > 0 aus den reellen Teilen der A-priori-Huellen (untere Schranke > 0). Auf [L_p, L] gelte
|f| < sqrt(S_-), S_- = (2 - sqrt(4 - 6 kappa0^2))/3 (kleinere Nullstelle von kappa0^2 - 2S + 1.5 S^2). Dann ist
V := kappa0^2 - 2 f^2 + 1.5 f^4 > 0, und u = r f erfuellt u'' = V u. Mit u(L_p) > 0 und u(L) > 0 (Lemma P) hat u auf
[L_p, L] kein nichtpositives inneres Minimum: bei u(r3) < 0 waere u''(r3) = V u < 0, bei u(r3) = 0 = u'(r3) waere
u = 0. Also f > 0 auf [0, oo) (auf [L, oo) nach Lemma P). QED.

### Lemma R (Regularitaet und Abfall der Eigenfunktion)

f ist gerade und analytisch bei 0 (Reihe in r^2), also sind die Koeffizienten von Y'' = M Y gerade. Mit Psi(0) = 0
ist Psi ungerade (Z(r) := -Psi(-r) loest dasselbe Anfangswertproblem), also a = A/r, b = B/r gerade analytisch in r
und glatt als Funktionen von |x|. Abfall nach Lemma J; Ableitungen fallen ueber die Gleichung ebenso ab, also
a, b in H^s(R^3) fuer alle s. Die l = 0-Reduktion (Laplace(A/r) = A''/r fuer r > 0) gibt die PDE auf R^3.
1 - omega* < rho* < 1 + omega* ist gleichwertig zu k^2 > 0 und kappa_c^2 > 0, geprueft auf ganz Z. QED.

## 5. Zertifizierungsalgorithmus

1. Startwert (nicht streng, float): Schiessen fuer a bei omega^2 = 0,7976767871108792 (Codex), c aus dem Abfall.
2. Newton (nicht streng, Kugelarithmetik-Mittelpunkte) auf H_0 = 0 in (a, c, rho, omega) mit Fortsetzung in L
   (12, 20, 30, 40). Ergebnis z0 exakt dyadisch in z0.json.
3. Strenge Punktauswertung H_0(z0): Profil, Profilvariationen nicht noetig, R_1, R_2 mit Lemma T0/T, N = 64.
4. Vorkonditionierer Y = mid(DH_0(z0))^{-1} (exakte dyadische Matrix; darf nicht streng sein).
5. Kastenradien delta aus |Y H_0(z0)| und |Y| eps (Vorschaetzung), mit Sicherheitsfaktor; Aenderungen in STAND.md.
6. Strenge Kastenauswertung DH_0(Z): Jets (Variationsgleichungen) in a, rho, omega mit Kugelparametern ueber Z.
7. Schwanzschranken eps ueber Z (Lemma P, J in Kugelarithmetik).
8. Test Kr in Z (Lemma K) und || |I - Y D| || < 1. Positivitaet (Lemma Pos) aus den Schrittprotokollen.
9. M1: dieselbe Pruefung eingeschraenkt auf (a, c) bei festem omega = omega0 (2x2). M2: Huelle von
   F(rho0, omega0) = (W(Psi_n, R_1), W(Psi_n, R_2)) fuer das Profil aus M1.
10. Ausgabe: Protokoll, JSON mit allen Huellen, sha256 von Code und Ausgaben.

Technik gegen den Einwickeleffekt: offener Kanal in Variation der Konstanten mit fester Referenzwellenzahl
khat (A = al cos(khat r) + be sin(khat r)); im Schwanz sind (al, be) fast konstant, keine Drehung. Die
Parameterabhaengigkeit von k steckt im kleinen Term (khat^2 - k^2) A. Alles polynomial in Zustand und Parametern.

## 6. Parameterwahl, Vorrechnung, Budget (gemessen)

- Vorrechnung (nicht streng, eigener Kern mit Mittelpunkten): Newton mit L-Fortsetzung 12, 20, 30, 40, N = 48,
  q = 1/3, 256 bit, 297 s. Abgleich mit Codex' Punkt: Abstand 9e-13 in rho, 1e-12 in omega^2 (Codex rechnet mit
  abgeschnittenem Potential).
- Gewaehlt: L = 40 (Schwanzfehler eps_1,2 ~ 1,5e-16, eps_3,4 ~ 2e-26), khat = 2683731777057 * 2^-40,
  Rmax = 1, R <= r_j/2, q = h/R = 1/3, Punktlauf N = 64, Kastenlauf N = 48, Praezision 256 bit, Kastenfaktor 8.
  Erster Schritt (Reihe um 0; berichtigt nach der Code-Lesung, Befund W1): Startversuch R0 = 1, angenommen nach
  sieben Verkleinerungen R = 13/64, h0 = 13/128, q = 1/2, Ordnung 2N; die Reihe um 0 traegt bis r = 13/128.
  Wiederholung: L = 44, q = 1/4, N = 72/44, 320 bit.
- Budget (Auflage W1 der Plan-Lesung), gemessen (Untergrenzen abgerundet, Obergrenzen aufgerundet):
  - Die Zeile H_0,1 verstaerkt Schrittreste etwa um L e^{2 kappa0 L}.
  - Groesster Schrittrest <= 3,5e-30 ergibt eine Breite von H_0,1(z0) von <= 1,3e-7. Wegen dH_0,1/dc = -1 wirkt das
    fast nur auf c, daher delta_c ~ 1,0e-6; in a, rho, omega bleiben delta ~ 1e-22.
  - Innenabstand von Kr zu Z: >= 0,87499 delta je Koordinate. Das Budget schliesst also mit Faktor 8.
  - Mit q = 1/4, N = 72, 320 bit: Breite <= 6,7e-18, delta_c ~ 1,2e-15, ebenfalls geschlossen.
  - Den Hinweis der Lesung, q = 1/2 scheitere, habe ich nicht erprobt; q = 1/3 und 1/4 waren vorher gesetzt.
- Laufzeiten (gemessen): Beweislauf A 50,6 s (Punkt 6,9 s, Jacobi am Punkt 18,4 s, Kasten 18,3 s),
  Wiederholung B 69,9 s, Kontrollen 78,2 s, Frei-Test 3,8 s. Nach der Code-Lesung: A2 113,1 s, B2 123,2 s
  (drei zusaetzliche Punktlaeufe fuer die Empfindlichkeitskontrolle, etwa 25 s in A2; Hashen 0,2 s; dazu langsamere
  Kernlaeufe bei gleichen Ergebnissen durch Last auf der .69, z. B. A2-Kasten 41,0 s gegen 18,3 s in A), kontr2 95,9 s.
- Alle Einzelzahlen (Z dyadisch, eps_1..4, (i)-(iv), k^2, kappa_c^2, Zeilensummen, relative Breiten, Schrittzahl):
  BEWEIS.md, Tabelle 3.2, und zertifikat/ZERT-A2-L40.json, Feld protokoll (gleiche Zahlen wie ZERT-A-L40.json).

## 7. Lueckenliste (Stand nach der Code-Lesung)

1. Code und Zertifikat frisch gegengelesen (LESUNG-CODE.md, 30.09., Haus Anthropic): traegt mit Auflagen W1, K1-K8,
   eingearbeitet (BEWEIS.md 7). Es fehlen eine Lesung aus einem fremden Haus und ein zweites unabhaengiges Programm.
2. Vertrauensannahme Software: python-flint 0.9.0 / FLINT (libflint-6839011d.so.24.0.0, sha256
   871a4132fd1e9f3638391b2208e07088f8e3e72a10e41d45f58b150a60c2a1a9).
3. Kein zweites unabhaengiges Programm (moeglich ueber Codex' CONTINUUM-MEMBERSHIP-Plan; Entscheidung der Leitung).
4. Eindeutigkeit positiver radialer Loesungen [L?] (Killip-Oh-Pocovnicu-Visan 2017, Serrin-Tang 2000; Skalierung
   siehe BEWEIS.md 5.4), nicht an der Quelle geprueft, nicht tragend.
5. Eindeutigkeit von (rho*, omega*) in Z nicht gezeigt (E nur stetig, keine C^1-Schranke).
6. Wesentliches Spektrum des vollen Bueschels nicht behauptet (Weyl-Satz [L?]); l > 0 nicht behandelt.

## 8. Abgleich mit Codex' Parallelplan (Auflage W7)

Gelesen: bic-proof/analytic/CONTINUUM-MEMBERSHIP.txt (05:55). Kein Code uebernommen, nur verglichen.
1. Gleichungen: identisch (p = omega^2, D = 1 - 4f^2 + 4.5 f^4, C = -2f^2 + 3f^4, Profil).
2. Profil-Schwanz:
   - Codex parametrisiert mit dem Wert A = g(R) (g = r f) und dem Dirichlet-Greenkern; hier wird mit der
     asymptotischen Amplitude c und dem Kern (1 - e^{-2 kappa0 (s-r)})/(2 kappa0) parametrisiert.
   - Codex' Konstanten sind scharfer (nach der Lesung um Faktor 2 kubisch, 6 quintisch); beide Schranken sind richtig.
   - Bei L = 40 ist der Unterschied bedeutungslos (Lambda <= 6,2e-17).
3. BIC-Schwanz: dieselben Volterra-Gleichungen (Codex' Lemma B = Lemma J). Codex nutzt eine gewichtete Norm mit
   gamma = 2 alpha + beta; hier Gronwall mit mu = max(1/k, 1/(2 kappa_c)). Beide richtig; Codex etwas schaerfer.
4. Anschluss:
   - Codex: sechsdimensional bei r_m = 6 mit Rueckwaertsintegration des Schwanzes und Normierung v'(0) = 1 am
     Ursprung.
   - Hier: vierdimensional (a, c, rho, omega), nur vorwaerts, Wronski-Formen, Normierung im Unendlichen.
   - Die Vorwaertsverstaerkung, vor der Codex warnt, ist gemessen und im Budget enthalten (Abschnitt 6).
5. Eindeutigkeit: Codex verlangt Parameterableitungen der Schwanzabbildungen (fuer Krawczyk-Eindeutigkeit). Hier
   ersetzt Brouwer mit Stoerterm diese Ableitungen; dafuer nur Existenz (Luecke 5).
6. Konstanten, soweit vergleichbar: kappa0 = alpha = 0,449804, kappa_c = beta = 0,524371, k = 2,440840.
   Codex' Pruefgroessen qP, qB wurden nicht ausgewertet (kein Codex-Code gelesen oder gerechnet).

## 9. Einarbeitung der Lesung LESUNG-PLAN.md (06:58)

| Befund | Erledigung |
|---|---|
| B1 Zahlen im Satz | BEWEIS.md 1 und 3.2: dyadische Grenzen von Z, K_J, L, q, N, Praezision, Schrittzahl, eps_1..4, (i)-(iv), k^2, kappa_c^2, Zeilensumme, Innenabstand, Laufzeit |
| W1 Budget | Abschnitt 6 und BEWEIS.md 3.3 (gemessen, schliesst mit Innenabstand >= 0,87499 delta) |
| W2 R < r_j | Wortlaut in Lemma T; strenge Pruefung im Code vor jedem Schritt; Protokoll R_kleiner_rj_alle = true |
| W3 eingebettet, zeitperiodisch | Abschnitt 1 und BEWEIS.md 1.4 |
| W4 Umkehrung / Einfachheit | Lemma E mit Beweis (Wronski-Komplement) |
| W5 Stetigkeit auf Z | Zusatz S; Bedingungen ueber ganz Z in Kugelarithmetik protokolliert |
| W6 Jets, Breiten | Zusatz J; relative Breiten von D <= 1,92e-9; Schrittprotokoll mit relativen Breiten |
| W7 Codex-Abgleich | Abschnitt 8 |
| K1, K2 | Abschnitt 1, BEWEIS.md 1 und 5 |
| K3 | s1, s3 sind feste dyadische Zahlen nahe L e^{kappa0 L} bzw. e^{-kappa_c L}; ihr genauer Wert ist unerheblich (BEWEIS.md 3.2) |
| K4 | Lemma T0, Zusatz zum Rest von f' |
| K5 | Lemma T, Zusatz Suche/Pruefung; Schrittprotokoll |
| K6 | z0.json mit Zaehler/Exponent, 197 bis 200 Nachkommabits; sha256 in SHA256SUMS.txt |
| K7 | Versionen und sha256 von Interpreter und libflint in BEWEIS.md 4 |
| K8 | Kanalzahlen in BEWEIS.md 3.2 |
| K9 | kein Handlungsbedarf |
