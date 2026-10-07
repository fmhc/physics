# Modell: Nullstellen der Abstrahlungsbreite als Duennwand-Phasenbedingung (Karte MOD-1, Runde 9)

- **Beginn: 2026-09-30 07:57:10 CEST (date).** Schreibbeginn: 08:07:52 CEST (date). Ende: letzte Zeile.
- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung (Finn: "wie bekommen wir das uebergeleitet auf ein modell?").
  Nur Papier und Handrechnung, kein Interpreter.
- **Kennzeichen:**
  - **[A]** an der Quelle gelesen: Textauszug der PDF unter coordination/resonance-20260930/papers/, Stelle genannt
  - **[ES]** eigene Herleitung oder eigener Schluss
  - **[H]** Hypothese
  - **[L?]** Literatur aus dem Gedaechtnis, nicht nachgeprueft
  - **(abgel.)** von mir aus Berichtswerten gebildet
- **Messwerte:**
  - RUNDE-07.md (BIC-2), RUNDE-08.md (BIC-3), RUNDE-09.md (BIC-4, ABSTAND, GF-BIC-2), RUNDE-08/gf-bic/ERGEBNIS.md
    (Abschnitt 3)
  - resonance-20260930/BIC-TESTPAKET-ERGEBNIS.txt und feshbach-20260930/TABLE.txt
  - SP-1-Ergebnisse habe ich nicht geoeffnet; die SP-1-Vorhersagen sind noch offen.
- Belegstufe aller Messwerte: numerisch im abgeschnittenen radialen linearen Modell, keine Messdaten. Stelle n = 1 bei
  beta = 0,5: rechnergestuetzter Beweis vom Autor gemeldet, Gegenpruefung laeuft (RUNDE-09.md).

---

## Modell (Abschnitt fuer das Paper)

### M.1 Aufgabe

- **Feldtheorie:** Komplexes Skalarfeld mit U(|phi|^2) = S - S^2 + beta S^3, S = |phi|^2, Masse 1.
- **Q-Ball:** phi = f(r) e^{i omega t}.
- **Stoerung:** delta phi = e^{i omega t}(u e^{i rho t} + v* e^{-i rho t}).
- **Radiale Gleichungen** fuer l = 0 mit U = r u, V = r v:

      U'' = [dp(r) - (omega + rho)^2] U + sp(r) V
      V'' = sp(r) U + [dp(r) - (omega - rho)^2] V
      dp = (S U'(S))' = 1 - 4S + 9 beta S^2,    sp = S U''(S) = -2S + 6 beta S^2

- **Kanaele:** Fuer 1 - omega < Re rho < 1 + omega ist U offen, Wellenzahl q^2 = (omega + rho)^2 - 1. V ist geschlossen,
  Abfall kappa^2 = 1 - (omega - rho)^2.
- **Gebundener Zustand im Kontinuum:** eine reelle Loesung (rho, omega) mit U -> 0 und V -> 0 fuer r -> unendlich.
  - Die bei r = 0 regulaeren reellen Loesungen bilden eine Ebene.
  - Gefordert sind drei lineare Bedingungen: kein wachsendes V, kein sin(qr) in U, kein cos(qr) in U.
  - Das sind zwei reelle Bedingungen an (rho, omega^2), also isolierte Punkte, Kodimension 1 in omega^2 [ES,
    THEORIE-ATMUNGS-NULLSTELLEN.md, 3.4].
  - Codex' und unsere Testabbildungen (W bzw. F) sind je ein Paar reeller Funktionen. Ihre gemeinsame Nullstelle traegt
    die Umlaufzahl +-1.

### M.2 Drei Zonen (angepasste asymptotische Entwicklung in w/R, w = Wandbreite)

**(a) Hintergrund: Duennwand-Q-Ball.**
- U(S)/S ist bei S_c = 1/(2 beta) minimal. Dort gilt omega_c^2 = 1 - 1/(4 beta).
- Fuer epsilon = omega^2 - omega_c^2 -> 0 ist der Ball ein Plateau S ~ S_c mit duenner Wand bei r = R.
- Radius aus dem Gleichgewicht von Wandspannung und Druck [ES]:

      R = (d - 1) / (4 sqrt(beta) epsilon),   in 3D:  R_tw = 1 / (2 sqrt(beta) epsilon)

  - Das ist fuehrend gleich Kovtun, Nugaev, Shkerin 2018 (arXiv:1805.03518v2), Gl. (46): R = sqrt(delta) v^2/(2
    omega_min (omega - omega_min)) [A]. Umrechnung: delta = beta, v^2 = 1/(2 beta), omega^2 - omega_c^2 ~ 2 omega_c
    (omega - omega_c).
  - Die Duennwandnaeherung geht auf Coleman 1985 zurueck (Nucl. Phys. B 262, 263; zitiert bei Kovtun u. a. als [8] [A]).
- Wandprofil (Teilchenbild bei omega = omega_c, Energieerhaltung f'^2 = beta f^2 (f_c^2 - f^2)^2) [ES]:

      S(r) = S_c / (1 + exp((r - R)/sqrt(beta))),   Wandbreite w = sqrt(beta)

- Probe: omega^2 = 0,6, beta = 0,5 gibt R_tw = 7,07; die Profilrechnung nennt R_Q = 7,41 (ERGEBNISSE-R6-B.md, Abschn. 5).

**(b) Innen (r < R - O(w)): stehende Welle der gekoppelten Mode.**
- Mit S = S_c sind die Koeffizienten konstant: dp_c = 1 + 1/(4 beta), sp_c = 1/(2 beta).
- Die zwei Kanaele mischen zu zwei Eigenmoden [A: Kovtun u. a., Gl. (51) bis (53), dort als Innenloesungen j_{l+1/2}
  und i_{l+1/2}]:

      propagierend:  k_c^2     = omega^2 + rho^2 - dp_c + sqrt(4 omega^2 rho^2 + sp_c^2)
      evaneszent:    kappa_c^2 = dp_c - omega^2 - rho^2 + sqrt(4 omega^2 rho^2 + sp_c^2)

- **Berichtigung des Auftragsbilds [ES]:**
  - Die stehende Welle im Inneren ist die propagierende Mischmode. Sie ist ueberwiegend vom offenen Typ: V/U = -0,16 an
    der Stelle n = 1, beta = 0,5 (Hand).
  - Der geschlossene Kanal ist im Inneren verboten. Er traegt dort nur den evaneszenten Teil, kappa_c = 0,97 bei n = 1,
    weil dp_c > (omega - rho)^2.
- Regulaer bei r = 0 heisst: propagierender Anteil a sin(k_c r) (allgemein die Riccati-Bessel-Funktion psi_l(k_c r)),
  evaneszenter Anteil b sinh(kappa_c r).

**(c) Wand (|r - R| = O(w)): der geschlossene Kanal ist dort gebunden.**
- Mit x = r - R und T = tanh(x/(2 sqrt(beta))) wird das Potential des geschlossenen Kanals [ES, Hand]:

      dp(x) = 1 + 1/(8 beta) - T/(8 beta) - (9/(16 beta)) sech^2(x/(2 sqrt(beta)))

  - Das ist ein Rosen-Morse-II-Topf (tanh-Stufe plus sech^2-Mulde). Innen geht er gegen dp_c, aussen gegen 1.
- **Grundzustand in geschlossener Form** [ES; per Einsetzen geprueft: psi_0 = cosh^{-A/alpha}(alpha x) e^{-(B/A) x}
  loest die Gleichung zu W = A tanh(alpha x) + B/A]:

      alpha = 1/(2 sqrt(beta)),   A = [-alpha + sqrt(alpha^2 + 9/(4 beta))]/2,   B = -1/(16 beta)
      E_w = 1 + 1/(8 beta) - A^2 - B^2/A^2,     c_w = sqrt(E_w)   (nackt, ebene Wand)

  - Fuer beta = 0,35 bis 0,60 gibt es genau einen gebundenen Wandzustand, denn fuer den zweiten waere (A - alpha)^2 >
    |B| noetig, und das ist nicht erfuellt.
  - Also gibt es einen Atmungsast [ES].
  - Codex' Arm A bestaetigt das numerisch: Ohne Kopplung laeuft der Pol in einen gebundenen Zustand des geschlossenen
    Kanals (rho_c = 1,7335 bei 0,7977) [feshbach TABLE.txt].
  - Die Kopplung sp = S(6 beta S - 2) wechselt in der Wand bei S = 1/(3 beta) das Vorzeichen.

**(d) Aussen (r > R + O(w)):** U = sin(qr + delta), V ~ e^{-kappa r}.

### M.3 Die Phasenbedingung [ES]

1. In fuehrender Ordnung in w/R ist das Wandproblem eben und von R unabhaengig.
2. R geht nur auf zwei Wegen ein:
   - ueber die Phase Psi := k_c R, mit der die stehende Welle a sin(k_c(R + x)) an der Wand ankommt
   - ueber den Betrag e^{kappa_c R} des evaneszenten Teils; er geht in die freie Amplitude b ein
3. Die drei Randbedingungen aussen sind lineare Gleichungen in (a sin Psi, a cos Psi, b). Die Koeffizienten haengen nur
   von (rho, omega, beta) ab.
4. Eliminiert man b und das Verhaeltnis der Amplituden, bleibt eine Bedingung der Form

       sin(Psi - pi theta(rho, omega, beta)) = 0

   zusaetzlich zur Resonanzbedingung rho ~ omega + c.
   - Sie hat die Periode pi in Psi, weil a -> -a dieselbe Loesung gibt.
5. Anschaulich (Feshbach-Form): Die Kopplung des Wandzustands an die offene Welle ist

       g(omega) = < U_reg | sp | V_w >  ~  A_in |F_w| sin(Psi - pi theta)

   - F_w = Integral dx e^{i phi(x)} sp V_w ist der von R unabhaengige Formfaktor der Wandquelle.
   - Die Abstrahlung verschwindet, wenn die Wand an einer bestimmten Phase der inneren stehenden Welle sitzt.

**Modellformel fuer die Stellen** (l = 0):

    k_c(omega*, rho*) R_tw(omega*) = pi (n + theta(epsilon)),        n = 1, 2, 3, ...
    Re rho* = omega* + c(epsilon),
    theta(epsilon) = theta_inf + theta_1 epsilon + theta_2 epsilon^2       (Kruemmung ~ 1/R ~ epsilon)
    c(epsilon)     = c_inf + c_1 epsilon  (n >= 3),   c_inf = c_w + delta_c   (delta_c: Niveauverschiebung durch sp)

**Asymptotisch** (n gross, epsilon -> 0; explizit):

    1/(omega*_n^2 - omega_c^2)  =  b_inf (n + theta_eff) + O(1/n),     b_inf = 2 sqrt(beta) pi / k_inf,
    k_inf = k_c(omega_c, omega_c + c_inf),   also   omega*_n^2 - omega_c^2 ~ 1/(b_inf n)

In LaTeX (zur Uebernahme):

    \Psi \equiv k_c R_{\rm tw},\quad R_{\rm tw}=\frac{1}{2\sqrt\beta\,(\omega^2-\omega_c^2)},\quad
    k_c^2=\omega^2+\rho^2-\Big(1+\tfrac{1}{4\beta}\Big)+\sqrt{4\omega^2\rho^2+\tfrac{1}{4\beta^2}},
    \qquad \Psi(\omega_n^*,\rho_n^*)=\pi\,[\,n+\theta(\epsilon_n)\,],
    \qquad \Gamma(\omega^2)\simeq\Gamma_{\rm env}\,\sin^2\!\big(\Psi-\pi\theta\big),
    \qquad \frac{1}{\omega_n^{*2}-\omega_c^2}\xrightarrow{n\to\infty} b_\infty\,(n+\theta_{\rm eff}),\ b_\infty=\frac{2\sqrt\beta\,\pi}{k_\infty}.

### M.4 Modell gegen Messung

**Wandzustand und Grenzschritt (Hand):**

| beta | E_w (nackt) | c_w | c_inf (Fit n >= 3, Messung) | delta_c | b_inf mit c_w | b_inf mit c_inf | letzter gemessener Schritt in 1/(x - x_c) |
|---|---|---|---|---|---|---|---|
| 0,35 | 0,4840 | 0,6957 | 0,765 (n = 3, 4) | 0,070 | 2,611 | 2,476 | 2,448 (n = 3 -> 4) |
| 0,40 | 0,5485 | 0,7406 | - | - | 2,438 | - | 2,286 (2 -> 3) |
| 0,45 | 0,5987 | 0,7738 | - | - | 2,363 | - | 2,230 (2 -> 3) |
| 0,50 | 0,6388 | 0,7993 | 0,826 (n = 3 bis 9) | 0,027 | 2,334 | 2,298 | 2,27 bis 2,30 (n = 4 bis 9) |
| 0,55 | 0,6717 | 0,8196 | 0,848 (n = 3 bis 5) | 0,028 | 2,332 | 2,296 | 2,273 (4 -> 5) |
| 0,60 | 0,6990 | 0,8361 | 0,861 (n = 3 bis 5) | 0,025 | 2,345 | 2,314 | 2,285 (4 -> 5) |

- Der Grenzschritt b_inf (Kehrwert-Gesetz der Karte ABSTAND) folgt ohne freien Parameter aus Wandzustand und
  Innenwellenzahl.
  - Mit dem nackten Wandzustand liegt er 1 bis 2 % ueber den gemessenen Schritten, die noch wachsen.
  - Mit der gemessenen Niveauverschiebung trifft er sie (beta = 0,5: 2,298 gegen 2,29, der Wert, mit dem BIC-4 die Leiter
    blind fortsetzte).
- Bei beta = 0,35 ist die Niveauverschiebung dreimal so gross (Kopplung sp_c = 1/(2 beta) groesser). Der Fit hat dort
  nur zwei Punkte [H].

**Stellen: Modell gegen Messung.**
- Psi/pi habe ich von Hand aus gemessenem omega*^2 und Re rho* gebildet. theta_mess = Psi/pi - n.
- theta_mod ist das Gesetz theta(epsilon), je beta an n = 2, 3, 4 angepasst (drei Punkte, exakt). Bei beta = 0,40 und 0,45
  gibt es kein n = 4; dort ist es linear an n = 2, 3 angepasst.
- Delta theta = theta_mess - theta_mod.
- Delta x = x_Modell - x_mess = Delta theta pi / \|dPsi/dx\|, mit \|dPsi/dx\| ~ (0,87 bis 0,95) Psi/epsilon (Hand).
- Angepasste Punkte sind mit "Fit" markiert. Alle anderen Zeilen sind Vorhersagen des Gesetzes.

| beta | n | omega*^2 (Messung) | Re rho* | epsilon | Psi/pi | theta_mess | theta_mod | Delta theta | Delta x |
|---|---|---|---|---|---|---|---|---|---|
| 0,35 | 1 | 0,621873 | 1,598633 | 0,33616 | 1,6713 | 0,6713 | 0,6671 | +0,0042 | +1,0e-3 |
| 0,35 | 2 | 0,476457 | 1,498694 | 0,19074 | 2,6471 | 0,6471 | Fit | - | - |
| 0,35 | 3 | 0,416453 | 1,443322 | 0,13074 | 3,6422 | 0,6422 | Fit | - | - |
| 0,35 | 4 | 0,384751 | 1,410362 | 0,09904 | 4,6404 | 0,6404 | Fit | - | - |
| 0,40 | 1 | 0,699702 | 1,663041 | 0,32470 | 1,7139 | 0,7139 | 0,6973 | +0,0166 | +3,6e-3 |
| 0,40 | 2 | 0,566347 | 1,583776 | 0,19135 | 2,6764 | 0,6764 | Fit | - | - |
| 0,40 | 3 | 0,508115 | 1,535876 | 0,13312 | 3,6673 | 0,6673 | Fit | - | - |
| 0,45 | 1 | 0,755738 | 1,709290 | 0,31129 | 1,7537 | 0,7537 | 0,7328 | +0,0209 | +4,3e-3 |
| 0,45 | 2 | 0,633380 | 1,644470 | 0,18894 | 2,7008 | 0,7008 | Fit | - | - |
| 0,45 | 3 | 0,577365 | 1,602162 | 0,13292 | 3,6862 | 0,6862 | Fit | - | - |
| 0,50 | 1 | 0,797677 | 1,744618 | 0,29768 | 1,7916 | 0,7916 | 0,7772 | +0,0144 | +2,7e-3 |
| 0,50 | 2 | 0,685129 | 1,690357 | 0,18513 | 2,7224 | 0,7224 | Fit | - | - |
| 0,50 | 3 | 0,631449 | 1,652588 | 0,13145 | 3,7014 | 0,7014 | Fit | - | - |
| 0,50 | 4 | 0,601422 | 1,628113 | 0,10142 | 4,6911 | 0,6911 | Fit | - | - |
| 0,50 | 5 | 0,582417 | 1,611309 | 0,08242 | 5,6852 | 0,6852 | 0,6851 | +0,0001 | +2e-6 |
| 0,50 | 6 | 0,56940 | 1,5992 (Kandidat) | 0,06940 | 6,6776 | 0,6776 | 0,6813 | -0,0037 | -4e-5 |
| 0,50 | 7 | 0,559856 (abgel.) | 1,58994 (interp.) | 0,05986 | 7,6776 | 0,6776 | 0,6786 | -0,0010 | -8e-6 |
| 0,50 | 8 | 0,552628 (abgel.) | 1,58275 (interp.) | 0,05263 | 8,6752 | 0,6752 | 0,6766 | -0,0014 | -9e-6 |
| 0,50 | 9 | 0,546951 (abgel.) | 1,57698 (interp.) | 0,04695 | 9,6734 | 0,6734 | 0,6751 | -0,0017 | -9e-6 |
| 0,55 | 1 | 0,829984 | ~1,7727 (geschaetzt) | 0,28453 | 1,8279 | 0,8279 | 0,8146 | +0,0133 | +2,4e-3 |
| 0,55 | 2 | 0,726130 | 1,726321 | 0,18068 | 2,7425 | 0,7425 | Fit | - | - |
| 0,55 | 3 | 0,674782 | 1,692366 | 0,12933 | 3,7141 | 0,7141 | Fit | - | - |
| 0,55 | 4 | 0,645620 | 1,669798 | 0,10017 | 4,7001 | 0,7001 | Fit | - | - |
| 0,55 | 5 | 0,627042 | 1,654130 | 0,08159 | 5,6913 | 0,6913 | 0,6920 | -0,0007 | -1e-5 |
| 0,60 | 1 | 0,855443 | ~1,7958 (geschaetzt) | 0,27211 | 1,8632 | 0,8632 | 0,8423 | +0,0209 | +3,5e-3 |
| 0,60 | 2 | 0,759294 | 1,755242 | 0,17596 | 2,7618 | 0,7618 | Fit | - | - |
| 0,60 | 3 | 0,710164 | 1,724518 | 0,12683 | 3,7264 | 0,7264 | Fit | - | - |
| 0,60 | 4 | 0,681916 | 1,703626 | 0,09858 | 4,7078 | 0,7078 | Fit | - | - |
| 0,60 | 5 | 0,663791 | 1,688955 | 0,08046 | 5,6961 | 0,6961 | 0,6965 | -0,0004 | -6e-6 |

**Angepasste Wandphasen:**

| beta | theta_inf | theta_1 | theta_2 |
|---|---|---|---|
| 0,35 | 0,638 | -0,006 | 0,271 |
| 0,40 | 0,647 (linear) | 0,156 | - |
| 0,45 | 0,652 (linear) | 0,261 | - |
| 0,50 | 0,664 | 0,209 | 0,576 |
| 0,55 | 0,664 | 0,272 | 0,907 |
| 0,60 | 0,653 | 0,478 | 0,802 |

- **Herkunft der Zahlen bei n = 7 bis 9:**
  - Die Lagen habe ich aus je drei Polen der Leitung (RUNDE-09.md, BIC-4) gebildet: signierte Wurzel der Breite, linear
    durch null.
  - Das Raster war 0,0006; die Rasterminima sind 0,5598 / 0,5526 / 0,5470.
  - Re rho ist dort linear interpoliert.
- **Ergebnis:**
  - Fuer n >= 5 trifft das Gesetz jede nicht angepasste Stelle auf \|Delta x\| <= 4e-5 (7 Stellen, 3 Werte von beta).
  - n = 1 liegt ausserhalb der Duennwand-Gueltigkeit. Das Gesetz aus n >= 2 verfehlt dort um +1,0e-3 bis +4,3e-3 in
    omega^2; theta bei n = 1 ist um 0,004 bis 0,021 groesser als hochgerechnet.
  - Die angepasste Asymptote theta_inf = 0,64 bis 0,66 haengt kaum von beta ab [H: universelle Wandphase].
- **Einschraenkung:** Das Modell braucht Re rho* als Eingabe. Fuer eine reine Vorhersage von omega* muss man c(epsilon)
  hochrechnen, wie in den blinden Runden.
  - Gemessenes c = Re rho* - omega*:
    - beta = 0,5: 0,8515 / 0,8626 / 0,8580 / 0,8526 / 0,8481 / 0,8446 / 0,8417 / 0,8394 / 0,8374 (n = 1 bis 9)
    - Ab n = 3 gilt c ~ 0,826 + 0,24 epsilon auf 0,002.
  - Ein Fehler von 0,002 in c verschiebt omega* um ~0,6 epsilon Delta c ~ 1e-4 (Hand).
  - In den blinden Runden gab das 8 von 8 Treffern auf etwa 1e-4 (RUNDE-08.md).

### M.5 Was das Modell erklaert

1. **Abwechselnde Umlaufzahl** [ES]
   - Nahe dem Wandzustand gilt fuer die Testabbildung L(y_b) ~ c_0 (rho - rho_c) und L(y_a) = s ~ g(omega) ~
     sin(Psi - pi theta).
   - Die Jacobi-Determinante ist daher ~ (dL_b/drho)(ds/dx). Der erste Faktor hat entlang des Asts festes Vorzeichen; der
     zweite wechselt, weil sin durch aufeinanderfolgende Nullstellen mit abwechselnder Steigung laeuft.
   - Also ist der Umlauf (-1)^n, bis auf die Konvention fuer n = 1.
   - Gemessen: alle aufgeloesten Umlaeufe bei beta = 0,35 bis 0,60 folgen dem (RUNDE-08.md: 7 von 8 im Blindtest
     aufgeloest getroffen).
   - Bei beta = 0,5, n = 5 und beta = 0,35, n = 4 war der Umlauf nicht aufgeloest, das Vorzeichen stimmte.
2. **Kruemmungskoeffizient C** in Gamma ~ C (x - x*)^2 [ES]
   - Aus Gamma ~ Gamma_env sin^2(Psi - pi theta) folgt C_n = Gamma_env (dPsi/dx)^2 an der Stelle.
   - Asymptotisch ist dPsi/dx ~ -Psi/epsilon ~ -pi b (n + theta)^2, also **C_n ~ C_0 (n + theta)^4**.
   - Beta = 0,5, von Hand aus den Polen:

     | n | C_n gemessen | Quelle | Gamma_env = C_n/(dPsi/dx)^2 |
     |---|---|---|---|
     | 1 | 1,079 | exakt-Tabelle | 4,0e-3 |
     | 2 | 8,8 | exakt-Tabelle | 5,4e-3 |
     | 3 | 35,6 | exakt-Tabelle | 5,9e-3 |
     | 7 | 750 | drei Pole, signierte Wurzel | 6,1e-3 |
     | 8 | 1210 | dito | 5,9e-3 |
     | 9 | 1830 | dito | 5,8e-3 |

   - Fuer n >= 3 ist Gamma_env nahezu fest, ~5,9e-3. Das Modell beschreibt also den Anstieg von C ueber drei
     Groessenordnungen mit einer Zahl. Nur n = 1 (dicke Wand) liegt tiefer.
   - Probe zwischen den Stellen: Das sin^2-Gesetz trifft Gamma auf 0,62 bis 0,80 auf ~12 %
     (THEORIE-ATMUNGS-NULLSTELLEN.md, 4.1).
3. **Haeufung wie 1/n** [ES]
   - Aus Psi = k_c/(2 sqrt(beta) epsilon) = pi (n + theta) folgt epsilon_n ~ k_c/(2 sqrt(beta) pi (n + theta)).
   - Das ist das Kehrwert-Gesetz, das bei allen beta am besten passt (Karte ABSTAND). Der Nachbarfaktor faellt wie
     (n + 1 + c)/(n + c), gemessen c = 0,43.
   - Der Schritt waechst von 2,0 auf b_inf, weil k_c zur duennen Wand hin faellt (beta = 0,5: 2,37 bei n = 1 bis 2,02
     bei n = 9).
   - Bei beta = 0,5 ist 1/epsilon_n = 2,298 (n + 0,27 bis 0,31) fuer n >= 3.
4. **Fehlen in 1D und im Log-Potential: Innenbarriere** [ES/H]
   - Das Bild braucht einen an die Wand gebundenen geschlossenen Zustand, also ein fuer V verbotenes Inneres:
     B = dp(S0) - (omega - rho)^2 > 0.
   - **1D:**
     - Ohne Reibungsterm ist S0 = 1 - sqrt(2 omega^2 - 1) (beta = 0,5): 0,37 bei 0,7, 0,68 bei 0,55. Damit ist B < 0 fuer
       omega^2 >= 0,545 (Hand).
     - Zudem waechst die Plateaulaenge nur wie ln(1/epsilon) statt wie 1/epsilon.
     - Beides passt zu "keine Stelle auf 0,55 bis 0,88".
     - Die Literaturpruefung nennt einen 1D-Satz ohne eingebettete Eigenwerte fuer die NLS-Klasse (Collot, Germain,
       Pacherie 2025, laut L4-BIC-FAMILIE-LITERATUR.md; dort [A], hier nicht selbst gelesen).
   - **Log-Potential U = ln(1 + S):**
     - dp = 1/(1 + S)^2 < 1 ueberall, also B < 0 und keine Wand-Mulde; V_c ist ein Hohlraumzustand.
     - Die Quelle ist glatt, ihr Formfaktor hat keine Nullstelle. Gamma faellt monoton (gesehen: 0,10 bis 0,90).
   - **Zusammenhang (Satz, THEORIE 4.3):** Eine Duennwandgrenze (Minimum von U/S) erzwingt einen Vorzeichenwechsel von
     U''. Ohne Minimum (Log) fehlen Plateau, Wand und Barriere zusammen.
   - Oberhalb der Barrierengrenze gibt es keine Stellen (beta = 0,5: x_B ~ 0,878). Das ist auf dem Raster 0,86 bis 0,96
     bestaetigt (V4).
5. **l > 0: Zusatzversatz** [ES/H]
   - Die regulaere Innenloesung ist die Riccati-Bessel-Funktion psi_l(k_c r) (Kovtun u. a.: Innenloesungen j_{l+1/2}
     [A]). Ihre Phase an der Wand ist Psi - l pi/2 + delta_l(Psi) mit:
     - delta_1 = arctan(1/Psi)
     - delta_2 = arctan(3 Psi/(Psi^2 - 3))
   - Der Wandzustand verschiebt sich zentrifugal: c_l^2 ~ c_0^2 + l(l+1)/R_w^2 mit R_w ~ R_tw + 0,65.
   - Folgen:
     - Die l = 1-Stellen verzahnen sich mit denen von l = 0.
     - Der l = 2-Ast erreicht bei ~0,67 die Kante 1 + omega.
   - Gemessen: l = 1-Minimum bei ~0,7554 (Leitung). Meine Eichung setzt die Stelle nach vier Breitenwerten auf 0,7556.
   - Die blinden SP-1-Vorhersagen (0,6620 und 0,6178 fuer l = 1; 0,6505, 0,6094 und 0,5865 fuer l = 2) sind noch offen.
     Ich habe ihre Ergebnisse nicht gelesen.
6. **Zweite Leiter, Gegenlaeufer psi_2** [ES/H]
   - Der geschlossene "Zustand" ist dort die Drehmode psi_2 ~ f. Sie ist nicht an die Wand gebunden, sondern fuellt das
     Volumen.
   - Die Kopplung -g J S speist den offenen Kanal bei 3 omega mit der Quelle f^3 (gf-bic/ERGEBNIS.md, 3.1).
   - Eine gleichfoermig gefuellte Kugel hat den Formfaktor ~ j_1(k_a R)/(k_a R). Er verschwindet bei den Nullstellen von
     j_1: k_a R/pi = 1,430 / 2,459 / 3,471 / 4,477 / 5,482. Dabei ist k_a^2 = 9 omega^2 - omega_c^2 innen (Hand).
   - Probe an den fuenf gut aufgeloesten Nullstellen der fuehrenden Ordnung (0,86575 / 0,71079 / 0,64568 / 0,61061 /
     0,58852):
     - k_a R_tw/pi = 1,662 / 2,593 / 3,561 / 4,548 / 5,569
     - Abstaende 0,93 / 0,97 / 0,99 / 1,02, also gegen 1 wie bei der Atmungsleiter
     - Versatz gegen die j_1-Nullstellen 0,23 / 0,13 / 0,09 / 0,07 / 0,09, schrumpfend
   - Deutung [H]: gleiche Phasenregel, aber mit **Volumen-** statt Wandquelle. Das erklaert die aehnlichen Schritte
     (2,0 bis 2,3) und den festen Versatz gegen die Atmungsleiter.
   - Umlaufzahlen der zweiten Leiter: -1 / +1 / +1 (Z1, Z2, Z3; RUNDE-09.md). Z1 und Z2 sind Nachbarn (n = 2, 3 der
     fuehrenden Ordnung).
   - Z3 (0,5512) ist nach derselben Zaehlung die neunte Stelle: Im Raster ist eine uebersprungen, die Schritte in
     1/(x - 0,5) sind 2,0 bis 2,3.
   - Damit passen alle drei Umlaufzahlen zur Paritaet (-1)^(n+1) dieser Leiter [ES].

### M.6 Effektives Zwei-Niveau-Bild (Fano, Feshbach) und Topologie

- **Feshbach-Form:**
  - Ein diskreter Zustand |w> (Wandzustand, Energie E_w(omega) + Re Sigma) koppelt ueber g(omega) = <E|sp|w> an ein
    einziges Kontinuum |E> (offene Welle).
  - Die Breite ist Gamma = 2 pi \|g\|^2 (Zustandsdichte, Normierung) [ES; allgemeines Resonanzbild, L?].
  - Das Modell legt g fest: g(omega) ~ \|F_w\| sin(Psi(omega) - pi theta). Die Kopplung ist reell und wechselt periodisch in
    Psi das Vorzeichen.
  - Im Fano-Bild [L?] heisst das: Die Resonanz koppelt an den Stellen gar nicht an den Streukanal. Das Profil wird dort
    beliebig schmal (Breite ~ g^2).
  - Hinweis aus Codex' Kopplungsleiter eta (feshbach TABLE.txt) [ES, grob]:
    - Bei kleiner Kopplung ist Gamma/eta^2 an 0,7977 nicht klein (6,8e-5; bei 0,8: 1,07e-4).
    - Die Nullstelle der nackten goldenen Regel liegt also woanders. Aus dem Verhaeltnis 1,57 folgt nach dem sin^2-Gesetz
      etwa 0,790.
    - Die Kopplung ("Anziehen" des Wandzustands) verschiebt die Wandphase theta um ~0,04. Die Leiterstruktur bleibt.
- **Abgrenzung zu Friedrich-Wintgen:**
  - Friedrich und Wintgen "suggested that BICs may appear from the destructive interference of two resonances coupled to
    a single radiation channel" (Yu, Lu 2025, arXiv:2504.19573v1, Abstract [A]).
  - Die typische Lage ist eine Kreuzung zweier gebundener Zustaende, deren Kopplung an denselben Kanal zu einem reellen
    Eigenwert fuehrt (dort Abschn. 1 [A]).
  - Zum Naeherungsmodell von Friedrich und Wintgen: "Friedrich and Wingten showed that a BIC of (3.3) must satisfy
    [(3.5)] N(s, λ) = D(s, λ) = 0, where N and D are real functions of s and λ" (Yu, Lu, Abschn. 3 [A]; Schreibweise des
    Originals).
  - **Unser Fall ist kein Zwei-Resonanzen-Fall.** Es gibt nur einen Wandzustand im Fenster:
    - Rosen-Morse-Zaehlung, M.2 c
    - Argumentprinzip der Runde 6: genau ein l = 0-Pol im Kasten, Partner mit Gamma < 0,1 ausgeschlossen
      (L4-BIC-LITERATUR.md, Abschn. 4)
  - Die Zaehlung ist aber dieselbe: zwei reelle Funktionen (bei uns L(y_a), L(y_b)) in zwei reellen Groessen.
  - Die Ausloeschung geschieht zwischen zwei Wegen desselben Zustands in denselben Kanal: direkte Wandabstrahlung
    gegen den Umweg ueber die innere stehende Welle. Deshalb haengt sie an der Phase Psi [ES].
- **Topologische Ladung (Zhen, Hsu, Lu, Stone, Soljacic 2014, PRL 113, 257401 [A]):**
  - "A resonance turns into a BIC when the outgoing power is zero, which happens if and only if c_x = c_y = 0."
  - Bei passender Symmetrie koennen c_x, c_y reell gewaehlt werden; BIC sind dann Kreuzungen zweier Knotenlinien.
  - Die Ladung ist die Windungszahl q = (1/2 pi) Umlaufintegral des Winkels.
  - "When system parameters vary continuously, the winding number defined on this path remains invariant, unless there
    are BICs crossing the boundary."
  - "Annihilation of BICs is only possible when charges of opposite signs are present."
  - **Bei uns** [ES]:
    - W = L(y_a) + i L(y_b) spielt die Rolle von c_x + i c_y. Die Ebene (Re rho, omega^2) ersetzt den Impulsraum; die
      Realitaet folgt aus der reellen Radialgleichung bei reellem rho.
    - Die Leiter ist eine Kette von Ladungen mit wechselndem Vorzeichen.
    - Folge: Unter stetiger Verformung (beta, Dimension d, Kopplung g) kann eine Stelle nicht einzeln verschwinden. Sie
      verschwindet nur paarweise mit einem Nachbarn entgegengesetzter Ladung oder am Rand des Gebiets (Kante 1 + omega,
      Barrierengrenze).
    - Das passt dazu, dass die Folge ueber beta = 0,35 bis 0,60 luecklos verfolgbar war. Als Vorhersage [H] gilt es fuer
      die Dimensionsbruecke: Nullstellenlinien in (d, omega^2) enden paarweise oder am Rand.

### M.7 Grenzen

1. **Kleines n (dicke Wand).**
   - Bei n = 1 ist R_tw ~ 2,4, das sind nur drei bis vier Wandbreiten.
   - theta weicht dort um 0,004 bis 0,021 vom Gesetz der n >= 2 ab, Lagefehler 1,0e-3 bis 4,3e-3.
   - Die Einhuellende ist kleiner (Gamma_env 4,0e-3 statt 5,9e-3).
   - Das Modell ist dort qualitativ, nicht quantitativ.
2. **Die Wandphase theta und die Niveauverschiebung delta_c sind angepasst, nicht hergeleitet.**
   - Hergeleitet sind: Radius, Innenwellenzahl, nackter Wandzustand (geschlossen), Periode pi, Paritaet, Haeufung, C ~
     (n + theta)^4, Grenzschritt.
   - Offen ist das ebene Zweikanal-Wandproblem mit Kopplung. Es liefert theta_inf und delta_c als reine Zahlen je beta; das
     ist eine eindimensionale Rechnung.
   - Solange sie fehlt, hat das Modell je beta zwei bis drei Wandkonstanten.
3. **Grenzen der Gueltigkeit.**
   - Oberhalb der Barrierengrenze (B < 0) gibt es keinen Wandzustand. Nahe der Kante 1 + omega (l > 0) ist der Zustand
     schwach gebunden, und das Bild darf versagen.
   - Zur duennen Wand hin (n >= 7) mischen in der Numerik zwei Aeste. Der Vorzeichentest versagte dort (Kernwachstum
     1e9); die Lagen stammen aus Breitenminima.
4. **Nichtlinear ist die Stelle keine Null mehr.**
   - Die Quellen zweiter Ordnung bei omega + 2 rho und omega - 2 rho liegen in offenen Kanaelen.
   - Codex misst einen auslaufenden Restfluss, der sich bei Verdopplung der Anregung um 15,97 bzw. 15,89 vergroessert.
     Das ist mit epsilon^4 vertraeglich (3,3e-6 / 5,3e-5 / 8,5e-4 bei epsilon = 0,01 / 0,02 / 0,04;
     BIC-TESTPAKET-ERGEBNIS.txt).
   - Die Stellen sind daher nichtlineare Quasi-BIC:
     - Energieverlust ~ A^4
     - generisch A ~ t^(-1/2)
     - Lage verschiebt sich wie A^2
   - Zeitlaeufe mit ausgeglichener Stossverschiebung geben bei eta = 0,01 hoechstens 5e-7 (obere Schranke).
5. **Weitere Grenzen der Numerik und des Beweises.**
   - Abgeschnittener Aussenrand.
   - Die Umlaeufe sind abgetastet, nicht intervallzertifiziert.
   - Beweis nur fuer n = 1, beta = 0,5, l = 0; die Gegenpruefung laeuft.
   - Nur radial, nur die Polynomfamilie und ein Log-Potential.
6. **Literatur.**
   - Die NLS-Mathematik erwartet fuer Grundzustaende keine eingebetteten Eigenwerte (Cuccagna, Maeda, laut
     L4-BIC-FAMILIE-LITERATUR.md, dort [A]).
   - Das Modell loest den Widerspruch nicht. Es zeigt nur, wo die Stellen im relativistischen Duennwandfall herkommen.
     Familie statt Einzelsoliton ist dabei wesentlich (Kodimension 1).

---

## Bericht (5 Punkte)

1. **Modell:**
   - Ein Duennwand-Q-Ball hat drei Zonen:
     - innen eine stehende Welle der gekoppelten Mode (Wellenzahl k_c nach Kovtun u. a. [A])
     - eine Wand, in der der geschlossene Kanal genau einen Zustand bindet (Rosen-Morse, Energie in geschlossener Form)
     - aussen die offene Welle
   - In fuehrender Ordnung geht der Radius nur ueber die Phase Psi = k_c R_tw ein. Die Abstrahlung verschwindet bei
     Psi = pi (n + theta).
2. **Gegen die Messung:**
   - Mit drei Wandkonstanten je beta (angepasst an n = 2, 3, 4) trifft das Gesetz alle freien Stellen mit n >= 5 auf
     \|Delta x\| <= 4e-5 (7 Stellen, beta = 0,50 / 0,55 / 0,60).
   - n = 1 verfehlt es um 1,0e-3 bis 4,3e-3 (dicke Wand).
   - Der Grenzschritt b_inf = 2 sqrt(beta) pi/k_inf kommt ohne freien Parameter heraus: 2,33 nackt, 2,30 mit
     Niveauverschiebung; gemessen ~2,29.
3. **Erklaert** [ES]:
   - wechselnde Umlaufzahl (Vorzeichenwechsel der Kopplung ~ sin(Psi - pi theta))
   - C_n = Gamma_env (dPsi/dx)^2 ~ (n + theta)^4: fuer n = 3 bis 9 mit einer Einhuellenden ~5,9e-3, ueber drei
     Groessenordnungen in C
   - Haeufung wie 1/n
   - keine Stellen in 1D und bei ln(1 + S) (Innenbarriere fehlt)
   - l > 0 ueber den Riccati-Bessel-Versatz
   - die zweite Leiter als Formfaktor einer gefuellten Kugel: Nullstellen von j_1, Abstaende gegen pi, Versatz 0,07 bis
     0,23
4. **Einordnung:**
   - Kein Friedrich-Wintgen-Fall: Es gibt nur einen Wandzustand. Die Ausloeschung laeuft zwischen zwei Wegen desselben
     Zustands.
   - Die Zaehlung ist dieselbe (zwei reelle Funktionen; Yu, Lu 2025 [A]).
   - Topologisch sind die Stellen Ladungen +-1 mit wechselndem Vorzeichen (Zhen u. a. 2014 [A]). Sie koennen nur paarweise
     verschwinden [ES].
5. **Grenzen:**
   - Die Wandphase theta und die Niveauverschiebung sind angepasst. Das ebene Zweikanal-Wandproblem, das sie liefern
     wuerde, ist der naechste Rechenschritt.
   - Das Modell gilt nur fuer duenne Wand und linear.
   - Nichtlinear strahlt die zweite Harmonische (Fluss ~ epsilon^4, Codex). Die Stellen sind deshalb Quasi-BIC mit
     algebraischem Zerfall.

## Einfach gesagt

Ein grosser Q-Ball ist wie ein Tropfen mit duenner Haut. In der Haut sitzt eine gefangene Schwingung, und innen laeuft
eine stehende Welle hin und her. Die gefangene Schwingung kann nur ueber diese Welle nach aussen leaken. Wenn die Haut
genau an einer bestimmten Stelle der stehenden Welle sitzt, heben sich die Beitraege auf, und nichts dringt nach aussen.
Weil der Tropfen beim Wachsen immer mehr halbe Wellen fasst, gibt es eine ganze Leiter solcher stillen Groessen. Unsere
Formel sagt, wo die Sprossen liegen, und sie trifft die gerechneten Stellen fast auf den Punkt; nur beim kleinsten Tropfen
ist die Haut zu dick fuer die einfache Rechnung.


**Ende: 2026-09-30 08:11:43 CEST (date, nach dem Schreiben gemessen).** Budget etwa 90 min.
