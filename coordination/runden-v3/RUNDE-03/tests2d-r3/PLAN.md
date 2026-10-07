# Runde 3, 2D-Tests: Laufplan (Wellen 16, 8/9, 14; Zufallskarte 20 als Papier)

Bearbeiter: Anthropic-Agent (Opus 5.5), Auftrag RUNDE-03/AUFTRAG-2D.md. Beginn 2026-09-30 01:20:35 CEST (gemessen),
Plan begonnen 02:03:24 CEST (gemessen), Ende in der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**.
Explorativ. Beruecksichtigt die zwei Nachrichten der Leitung: Rechenort P4000 (01:31) und Fable-Hinweis zum Hintergrund
(ca. 02:00).

## Kurzfassung

- **Code:** tests2d_r3.py. Sprache PyTorch, float64 bzw. complex128, nur CUDA. Drei Unterbefehle:
  - `profile`: Schiessen fuer m = 0 und m = 1, ohne Zeitentwicklung
  - `tropfen`: Test 1, Wellen 16
  - `brechung`: Test 3, Wellen 14
- **Wellen 16, Tropfenschwingung:** Vorhersage ohne freie Parameter nach der 2D-Rayleigh-Formel
  Omega_l^2 = (l^3 - l) sigma/(rho R^3).
  - Dichte: rho = Enthalpiedichte w = 2 omega^2 S_c.
  - Bei omega^2 = 0,52 etwa Omega_2 = 0,019 (Periode 325) und Omega_3 = 0,039 (Periode 163).
  - Das Verhaeltnis Omega_3/Omega_2 = 2 haengt nicht von sigma, rho und R ab.
- **Wellen 8/9, Magnus und Flettner: im Ein-Feld-Modell nicht umsetzbar.** Es gibt keinen stabilen duennen Hintergrund
  (Papierpruefung in Abschnitt 3). Kein Code, keine Scheinmessung.
- **Wellen 14, Brechung:** Statt einer Dichtestufe eine Stufe im Potential, also ein ortsabhaengiger Massenkoeffizient
  V(x)|psi|^2. Das hat die Leitung erlaubt, ein Hintergrund entfaellt.
  - Vorhersage aus Energie- und Tangentialimpulserhaltung: sin theta2 = sin theta1 * v1/v2, v_y bleibt gleich.
  - Anziehende Stufe: Knick zum Lot, n_eff etwa 1,29.
  - Abstossende Stufe: Totalreflexion ab etwa 34 bis 37 Grad.
- **Laufzeit auf der P4000 (geschaetzt):**
  - profile etwa 1,5 min
  - tropfen etwa 6 min (4 bis 9)
  - brechung etwa 3 min
  - Rauchtest aller Teile etwa 4 bis 5 min
  - GPU-Speicher unter 1 GB
- **Wellen 20:** KNOTEN-PAPIER.md.
  - Ein-Feld-Modell: keine geknoteten Q-Baelle (keine Knotenzahl).
  - C x S^2: isorotierende Hopfionen sind Literatur. Ein gebundener Knoten-Q-Ball ist offen und braucht das Fenster
    1/2 < omega^2 < min(1, v^2/(2 kappa)); das gehoert zum CX-1-Strang.

## 1. Festlegungen fuer alle Tests (vor dem Lauf)

- **Modell:** L = |psi_t|^2 - |grad psi|^2 - U(S) - V(x) S mit U = S - S^2 + S^3/2. Das ist die Atlas-Normierung wie in
  qg1.py, hier in 2D.
  - Bewegungsgleichung: psi_tt = Lap psi - (U'(S) + V) psi.
  - V = 0 ausser in Test 3.
  - Q-Ball: psi = f(r) e^{i m theta - i omega t}, Ladung Q = 2 omega N mit N = Int f^2 dA,
    Energie E = omega^2 N + G + V_U.
  - 2D-Virial (Derrick): V_U = omega^2 N, also E = omega Q + G mit G = Int |grad f|^2 dA.
- **Profile durch Schiessen** (RK4, h = 0,01 wie qg1.py; bis r = 60; Einschachteln mit 2048 Kandidaten in 5 Runden):
  - Start bei r = h aus der Reihe um r = 0:
    - m = 0: f = p + g r^2/4
    - |m| = 1: f = p r + ((1 - omega^2) p/8) r^3 mit p = f'(0)
  - Klassifikation:
    - m = 0: Ueberschuss heisst f < 0 oder f > f_top. Unterschuss heisst f' > 0 jenseits der Talsohle, also bei
      f < f_tal.
    - m = 1: Ueberschuss heisst f > f_top, Unterschuss heisst f' < 0.
    - f_top^2 und f_tal^2 sind die Wurzeln von U'(S) = omega^2.
    - Die Talbedingung verhindert, dass ein Kandidat genau auf der Kuppe durch Rundung als Unterschuss zaehlt.
  - Schwanz ab f < 1e-3 f_max (im Abfall): asymptotisch e^{-kappa0 r} r^{-1/2} (1 + (4m^2 - 1)/(8 kappa0 r)), das ist
    K_m(kappa0 r), mit kappa0^2 = 1 - omega^2.
  - Genauigkeit beim duennwandigen Ball omega^2 = 0,52 (R etwa 17,5):
    - Die Startabweichung von der Kuppe ist etwa 3e-11, die Klammer erreicht die float64-Aufloesung (2e-16).
    - Nach Handabschaetzung liegt der wachsende Anteil an der Schwanzschwelle bei etwa 0,4 Prozent des abfallenden.
      Die Bahn erreicht die Schwelle also sicher.
    - Scheitert es doch, bricht der Code mit "Schiessbahn verlaesst den Separatrixweg" ab. Ausweg: 0,52 durch 0,53
      ersetzen; das entscheidet die Leitung.
  - Kontrollen je Profil: Virialrest (V_U - omega^2 N)/(V_U + omega^2 N), Klammerbreite, Schwanzbeginn.
- **Zeitentwicklung:** Velocity-Verlet wie qg1.py.
  - Laplace **spektral** (FFT, periodische Box) statt finiter Differenzen. Begruendung:
    - Der 5-Punkt-Laplace ist anisotrop, der Fehler hat einen cos(4 theta)-Anteil proportional zu dx^2. Diese
      Anisotropie koppelt an die Formmoden, die Test 1 misst.
    - Spektral ist isotrop und fuer glatte Felder exponentiell genau. Deshalb reicht dx = 0,3, was auf der P4000 zaehlt.
  - Randschicht: Breite 8, sigma = (Tiefe/8)^2, nach jedem Schritt psi_t -> psi_t e^{-sigma dt}.
  - Aufloesungen: **grob dx = 0,3, dt = 0,05; fein dx = 0,2, dt = 0,025** (dt halbiert wie in qg1.py).
    - Stabilitaet: dt < 2/k_max, also 0,135 bzw. 0,09. Eingehalten.
  - Profil auf dem 2D-Gitter: kubische Hermite-Interpolation aus der Radialtabelle, Fehler O(h^4), etwa 1e-9.
  - Messungen alle 1,0 Zeiteinheiten, nur auf der GPU:
    - Schwerpunkt mit Gewicht S^2 im Fenster um den letzten Schwerpunkt
    - Ladung und Energie im Fenster und in der Box
    - S_max, Radien, Formmomente
- **Profilkontrolle** (Unterbefehl `profile`, nur Schiessen):
  - m = 0 und m = 1 bei omega^2 = 0,52 / 0,55 / 0,6 / 0,7 / 0,8
  - Tabelle mit Q, E, E/Q, R_halb, bei m = 1 auch der innere Halbwertsradius ("Auge")
  - Virialrest; dE/dQ/omega aus Nachbarpunkten
  - Erwartung:
    - Virialrest unter 1e-5
    - dE/dQ / omega = 1 auf etwa 1 Prozent (Differenzenquotient ueber grobe omega-Schritte)
    - bei m = 1 ist S(0) = 0
  - **Nebenprodukt fuer Idee 19 ("Auge des Tornados"), Vorhersage [S]:**
    - Der Kern des m = 1-Balls wird von der Heilungslaenge xi = 1/sqrt(2 S U'') (etwa 0,7) bestimmt, nicht von der
      Ladung.
    - Der innere Halbwertsradius liegt daher bei etwa sqrt(2) xi, also etwa 1 (0,7 bis 1,5), und bleibt fuer
      omega^2 <= 0,6 nahezu gleich, waehrend Q stark waechst.
    - "Der Kern waechst mit Q" waere im Duennwandbereich damit falsch.
  - Scheitert eine m = 1-Bahn an der Praezision, markiert der Unterbefehl die Zeile als ungueltig, statt abzubrechen.

## 2. Test 1, Wellen 16: Tropfenschwingung

### 2.1 Die 2D-Formel (hergeleitet, **[S]**)

- **Aufbau:** Scheibe mit Radius R, Rand r = R + eps cos(l theta) e^{-i Omega t}. Innen reibungsfrei, zunaechst
  inkompressibel. Geschwindigkeitspotential Phi = A r^l cos(l theta). Aussen Vakuum.
- **Kinematik:** eps_t = d_r Phi (R) = l A R^{l-1}.
- **Dynamik:**
  - Linearisierter Bernoulli-Druck: delta p = -rho Phi_t.
  - Kruemmung der gestoerten Randkurve: kappa = 1/R + (l^2 - 1) eps cos(l theta)/R^2.
  - Am Rand gilt also delta p = sigma (l^2 - 1) eps / R^2.
- **Ergebnis:** Omega_l^2 = l (l^2 - 1) sigma / (rho R^3) = (l^3 - l) sigma/(rho R^3). l = 1 gibt 0 (Verschiebung).
  Die 3D-Form waere l(l - 1)(l + 2).
- **Welche Dichte (vorab festgelegt): rho = Enthalpiedichte w = epsilon + p = mu n = 2 omega^2 S_c.**
  - Mit psi = sqrt(S) e^{-i chi} ist die Lagrangedichte L = P(X), X = chi_t^2 - |grad chi|^2. Das ist ein
    relativistisches Superfluid.
  - Mit chi = omega t + phi ist die Stroemungsgeschwindigkeit v = grad phi/omega, und die kinetische Energie ist
    S |grad phi|^2 = (1/2)(2 omega^2 S) v^2.
  - Der Druck aendert sich um delta p = n delta mu = 2 omega^2 S Phi_t mit Phi = phi/omega. Traege Masse und Druck
    passen also nur mit rho = w zusammen.
  - Die **Ladungsdichte** n = 2 omega S hat nicht die Einheit einer Massendichte; es fehlt der Faktor mu = omega.
    Mit ihr waeren die Frequenzen um den Faktor sqrt(omega) kleiner, also 0,85-mal so gross.
  - Im duennwandigen Grenzfall p -> 0 ist w gleich der Energiedichte epsilon. Bei 0,52 unterscheiden sich w und
    epsilon um 2 Prozent (1 Prozent in Omega), bei 0,55 um 4,6 Prozent.
- **sigma und R aus dem Profil:**
  - Festgelegt ist P1: sigma_G = G/(pi R_Q).
    - Nach dem 2D-Virial gilt E - omega Q = G, und im Duennwandbild gilt E - omega Q = -p pi R^2 + 2 pi sigma R
      = pi sigma R.
    - R_Q = sqrt(N/(pi S_c)) ist der Aequimolarradius der Ladung.
  - Vergleichswerte, nicht bindend:
    - P2: sigma = p_c R_Q (Laplace)
    - P3: sigma0 = sqrt(2)/4 (ebene Wand, F-3-Papier)
    - P4: rho = n (Ladungsdichte)
    - P5: rho = epsilon (Energiedichte)
    - P6: P1 mit Kompressibilitaet und Wandtraegheit.
  - Korrekturen in P6:
    - Kompressibilitaet: Faktor 1 - (Omega R/c_s)^2/(2 l (l + 1)) auf Omega^2, mit
      c_s^2 = S U''/(S U'' + 2 omega^2). Die Formel folgt aus q J_l'(qR)/J_l(qR) = l/R - q^2 R/(2(l + 1)).
    - Wandtraegheit: Die Wand hat Energie sigma je Laenge und bewegt sich mit; das gibt den Faktor
      1/(1 + sigma l/(w R)).

### 2.2 Vorhersage (vor dem Rechnen, Handrechnung im Duennwandbild; der Code rechnet P1 bis P6 aus dem Profil, bevor er entwickelt)

| omega^2 | S_in | p | R etwa sigma0/p | w | c_s | P1 Omega_2 (Periode) | P1 Omega_3 (Periode) | P6/P1 l = 2 und 3 | P4/P1 (Ladungsdichte) |
|---|---|---|---|---|---|---|---|---|---|
| 0,52 | 1,0194 | 0,0202 | 17,5 | 1,060 | 0,714 | 0,0193 (325) | 0,0386 (163) | 0,972 / 0,954 | 0,849 |
| 0,55 | 1,0467 | 0,0512 | 6,9 | 1,151 | 0,721 | 0,0748 (84) | 0,1496 (42) | 0,938 / 0,898 | 0,861 |

- **Bindend ist die Formel P1 mit den Profilgroessen.** Die Zahlen sind Handwerte im Duennwandbild. Bei 0,55 ist der
  Ball klein, dort sind sie nur grob.
- **Verhaeltnis:** Omega_3/Omega_2 = 2 inkompressibel, mit P6-Korrekturen 1,96 (0,52) bzw. 1,92 (0,55). Es haengt nicht
  von sigma, rho und R ab und ist die schaerfste parameterfreie Probe des (l^3 - l)-Gesetzes.
- **Meine Erwartung:**
  - Bei 0,52 liegt Omega_mess/P1 bei etwa 0,93 bis 0,99 (P6-Korrekturen plus etwa 5 Prozent Unsicherheit durch
    Wandlage und Tolman-Laenge). Omega_3/Omega_2 liegt bei etwa 1,95.
  - Bei 0,55 liegt die Abweichung bei 5 bis 15 Prozent.
  - Kriterium A mit p = 0,65, B mit p = 0,10, C mit p = 0,25.
- **Kriterien** (bei omega^2 = 0,52, feine Stufe):
  - **A, Tropfenbild quantitativ getragen:** 0,90 <= Omega/P1 <= 1,05 fuer l = 2 und 3, und
    1,85 <= Omega_3/Omega_2 <= 2,05.
  - **B, Befund gegen das reine Tropfenbild:** Omega/P1 < 0,85 oder > 1,10, oder Omega_3/Omega_2 ausserhalb
    [1,80; 2,10].
  - **C, dazwischen:** Der Trend entscheidet.
    - Schrumpft |1 - Omega/P1| von 0,55 nach 0,52 mindestens auf die Haelfte, ist es ein Tropfen mit
      Endlichkeitskorrektur.
    - Sonst ist es ein Befund-Kandidat, etwa fuer eine andere Traegheit: Die Ladungsdichte gaebe 0,85.
- **Laeufe:**

| Stufe | omega^2 | Laeufe (Randauslenkung dR) | T |
|---|---|---|---|
| grob | 0,52 | l = 2 (0,25), l = 3 (0,25), l = 2 (0,5), Ruhe | 1000 |
| grob | 0,55 | dieselben vier | 400 |
| fein | 0,52 | l = 2, l = 3 (je 0,25) | 1000 |
| fein | 0,55 | l = 2, l = 3 | 400 |

- Box: halbe Laenge 48 bei 0,52 und 36 bei 0,55.
- Formstoerung als r -> r (1 - eps cos(l theta)) mit eps = dR/R_Q; psi_t = -i omega psi.
- **Messgroesse:**
  - Formmoment c_l(t) = Sum S Re(z^l)/Sum S |z|^l um den Schwerpunkt, im Fenster R_Q + 12.
  - Frequenz aus einem Periodogramm: Kleinste Quadrate a + b tau + c cos(Omega t) + d sin(Omega t) auf einem Raster in
    [1,5 * 2 pi/T; 0,6], danach verfeinert.
  - Ausgegeben werden Omega, erklaerter Varianzanteil R2 und die drei tiefsten Nebenminima (akustische Moden,
    Transparenz).

### 2.3 Gegenproben

- **Ruhelauf** (ohne Stoerung): c_2 und c_3 bleiben bei Rundungsrauschen (Gittersymmetrie). Berichtet werden die Atmung
  (Spannweite von R_rms) und der Schwerpunkt.
- **Linearitaet:** Doppelte Auslenkung (dR = 0,5) aendert Omega um weniger als 1 Prozent. Die nichtlineare Verschiebung
  ist von der Ordnung (dR/R)^2, also 1e-3.
- **l-Verhaeltnis:** Omega_3/Omega_2 ohne sigma, rho, R, siehe oben.
- **Dichtevarianten:** P4 (Ladung) gegen P1 und P5 trennt um 15 Prozent; P1 gegen P5 nur um 1 bis 2 Prozent, das wird
  nicht aufgeloest.
- **Aufloesung (L3):** |Omega_fein/Omega_grob - 1| <= max(0,2 * |Omega_fein/P1 - 1|; 0,005) fuer l = 2 und 3.
- **Erhaltung:** Q_Box und E_Box. Die Randschicht nimmt nur die Einschwingstrahlung; erwartet ist ein Verlust unter
  1e-4 bzw. 1e-3.

## 3. Wellen 8/9, Magnus und Flettner: im Ein-Feld-Modell nicht umsetzbar

- **Papierpruefung der Stabilitaet eines homogenen Hintergrunds [S]:**
  - Ansatz: psi = (sqrt(S) + delta) e^{-i mu t}, mu^2 = U'(S). Linearisieren gibt die Bogoliubov-Relation
    (Omega^2 - q^2)(Omega^2 - q^2 - beta) = 4 mu^2 Omega^2 mit beta = 2 S U''(S) = -4 S + 6 S^2.
  - Lange Wellen: Omega^2 = c_s^2 q^2 mit c_s^2 = beta/(beta + 4 mu^2).
  - Fuer 0 < S < 2/3 ist beta < 0. Dann gibt es ein instabiles Band 0 < q^2 < -beta (Modulationsinstabilitaet).
    Die groesste Wachstumsrate ist etwa |beta|/(4 mu).
  - Beispiel S = 0,003: Wachstumsrate etwa 0,003, e-Faltungszeit etwa 330.
  - Stabil ist der Hintergrund erst ab S > 2/3. Dann ist er aber so dicht wie das Ballinnere (S = 0,8: omega_bg = 0,6).
    Das deckt sich mit dem Fable-Review (REVIEW-FABLE.md, Z. 39-45).
- **Warum auch ein "langsam instabiler" duenner Hintergrund nicht taugt:**
  - Ich hatte zuerst S = 0,003 mit gamma T < 1 vorgesehen und ohne Rechnung verworfen.
  - Grund: Ball (omega etwa 0,73) und Hintergrund (omega_bg etwa 1,03) schwingen verschieden und sind inkohaerent.
    Der Hintergrund wirkt dann wie ein Wellengas, das am Ball streut, nicht wie eine superfluide Umstroemung.
  - Die Windung m des Balls setzt sich nicht in den Hintergrund fort. Im Fernfeld ist die Gesamtwindung 0, also gibt es
    keine Zirkulation und keine Kutta-Joukowski-Kraft.
  - Im dichten stabilen Hintergrund ist ein "drehender Ball" nur ein Wirbel in Q-Materie. Die Magnuskraft auf einen
    Wirbel ist Lehrbuchwissen (L4).
- **Ergebnis:** Die Karte ist so nicht umsetzbar. Es gibt keinen Code, keine Laeufe und keine Scheinmessung.
- **Mit dem Medium als zweitem Feld** (stabiles Kondensat chi mit abstossender Selbstwechselwirkung, an psi ueber die
  Dichten gekoppelt) ginge es, aber nur, wenn der Ball im Kern eines chi-Wirbels sitzt. Erst dann hat das Medium
  Zirkulation, und es ist die bekannte Magnuskraft auf einen Wirbel mit gefuelltem Kern (L4). Das ist ein Modellwechsel
  und eine neue Karte.
- Hinweis fuer den 1D-Test Wellen 5 (anderer Agent): Dieselbe Rechnung gilt in 1D. Einen "duennen stabilen
  Hintergrund" gibt es auch dort nicht.

## 4. Test 3, Wellen 14: Brechung an einer Stufe im Potential

### 4.1 Aufbau (vorab)

- **Stufe:** V(x) = V2 (1 + tanh(x/B))/2 mit B = 1. Das ist ein ortsabhaengiger Koeffizient des Massenterms; ein
  Hintergrund entfaellt (Erlaubnis der Leitung).
- **Lesart:** Im Mittelfeld wirkt eine echte Dichtestufe eines Mediums auf den Ball wie eine solche Stufe. Eine Stufe
  in einem echten Medium ginge nur mit einem zweiten Feld (Abschnitt 3).
- **Ball:** m = 0, omega^2 = 0,70 (klein, dickwandig).
  - Lorentz-geboostet mit v1 = 0,2 unter dem Winkel theta1 zur Stufennormalen.
  - Start bei x0 = -16, y0 = -v1 sin(theta1) T/2.
  - Box: halbe Laenge 42, T = 280.
- **Laeufe:**
  - anziehend (V2 = -0,02) bei theta1 = 20, 40, 60 Grad
  - anziehend bei senkrechtem Einfall (0 Grad)
  - abstossend (V2 = +0,02) bei 20 und 45 Grad
  - ohne Stufe bei 40 Grad
  - fein: die drei schraegen anziehenden Laeufe

### 4.2 Gesetz (hergeleitet **[S]**, vor dem Rechnen)

- **Erhaltung:**
  - V haengt nur von x ab, also ist p_y exakt erhalten. Die Stufe ist statisch, also ist die Gesamtenergie erhalten.
  - Nimmt der Ball keine innere Anregung und keine Strahlung mit, gilt E_tot = gamma1 M1 = gamma2 M2.
- **Ruhemasse im Medium** (M2 bei fester Ladung):
  - Im Medium ist f das Profil der alten Familie bei Omega^2 = omega2^2 - V2. Die Stufe verschiebt nur die Masse.
  - Es gilt E2 = omega2 Q + G(Omega^2) (2D-Virial), mit Q = 2 omega2 N(Omega^2) = Q1.
  - Der Code schiesst dafuer eine Familie von 61 Profilen (Omega^2 = 0,64 bis 0,76) und interpoliert.
- **Brechungsgesetz:**
  - p2^2 = E_tot^2 - M2^2 und sin theta2 = p_y/p2.
  - Gleichwertig: **v_y bleibt exakt gleich**, sin theta2 = sin theta1 * v1/v2, n_eff = p2/p1 = v2/v1. Das ist
    korpuskulare Brechung.
  - Ist p_y > p2, wird der Ball total reflektiert.
- **Erste Ordnung** (Delta M = V2 N):
  - p2^2/p1^2 = 1 - 2 V2 N/(gamma^2 M1 v1^2), mit N/M1 = (1 - G/E)/(2 omega^2), G/E etwa 0 bis 0,07.

| Lauf | theta1 | Vorhersage theta2 | v2 | Ausgang |
|---|---|---|---|---|
| V2 = -0,02 | 20 Grad | etwa 15,4 Grad | etwa 0,258 (n_eff 1,28 bis 1,30) | durch |
| V2 = -0,02 | 40 Grad | etwa 29,9 Grad | etwa 0,258 | durch |
| V2 = -0,02 | 60 Grad | etwa 42,2 Grad | etwa 0,258 | durch |
| V2 = -0,02 | 0 Grad | 0 | etwa 0,258 | durch |
| V2 = +0,02 | 20 Grad | etwa 36 Grad (35 bis 38) | etwa 0,116 (n_eff 0,56 bis 0,60) | durch |
| V2 = +0,02 | 45 Grad | Reflexion unter 45 Grad | 0,2 | reflektiert (Grenzwinkel etwa 34 bis 37 Grad) |
| V2 = 0 | 40 Grad | 40 Grad | 0,2 | gerade |

- **Bindend** ist die Vorhersage, die der Code vor der Entwicklung aus dem Profil rechnet ("Vorhersage"-Block im
  Bericht). Zusaetzlich rechnet er dieselbe Vorhersage aus der gemessenen Einfallsbahn.
- **Kriterien:** Das Gesetz gilt, wenn fuer alle sechs Laeufe mit Stufe (grobe Stufe) gleichzeitig gilt:
  - |theta2_mess - theta2_vorh| <= 1 Grad
  - |v2_mess/v2_vorh - 1| <= 2 Prozent
  - der Ausgang (durch oder reflektiert) stimmt
  - Sonst ist es ein Befund-Kandidat. Zuerst ist zu pruefen, ob Energie ins Innere des Balls gegangen ist.
    Der Durchgang dauert 30 bis 60 Zeiteinheiten, das ist nur knapp adiabatisch gegen innere Perioden von 15 bis 30.
- **Meine Erwartung:**
  - Winkel innerhalb 1 Grad mit p = 0,65; Geschwindigkeiten innerhalb 2 Prozent mit p = 0,6.
  - Innere Anregung macht v2 eher zu klein, bei den abstossenden Laeufen am deutlichsten.
  - Die Totalreflexion bei 45 Grad sehe ich mit p = 0,9.

### 4.3 Gegenproben

- **Ohne Stufe:** Knick unter 0,2 Grad und v2/v1 = 1 auf 1e-3. Das prueft den Boost-Anfangszustand und den Fit.
- **Senkrechter Einfall:** Nur die Geschwindigkeitsaenderung zaehlt, also reine Energieerhaltung.
- **Totalreflexion:** Scharfer Ausgang, Reflexionswinkel gleich Einfallswinkel.
- **Interpolation:** M2 bei V2 = 0 muss M1 treffen (Kontrolle K_interpolation, erwartet unter 1e-5; misst den Virialrest).
- **v_y-Erhaltung:** vy2/vy1 wird berichtet; die Abweichung misst abgestrahlte Energie.
- **Aufloesung (L3):** |theta2_fein - theta2_grob| <= max(0,2 * Knick; 0,2 Grad).
- **Verluste:** Ladung und Energie im Fenster am letzten gueltigen Messpunkt.

## 5. Aufruf (Leitung, P4000 mit eigener Sperre)

- **Vorschlag:** tests2d_r3.py nach /home/fmh/fmhc-physics-remote/r3-tests2d-20260930/ kopieren. Das Programm braucht nur
  torch, schreibt nur in --out (Vorgabe: Ordner `ausgabe/` bzw. `rauchtest/` neben dem Skript) und rechnet nichts auf
  der CPU.
- **Rauchtest**, alle drei Teile, etwa 4 bis 5 min, vor allem Schiessen:

```
cd /home/fmh/fmhc-physics-remote/r3-tests2d-20260930 && \
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3-2d-rauch tests2d_r3.py alle --rauch
```

- **Hauptlaeufe**, je ein Aufruf und je hoechstens 10 min:

```
cd /home/fmh/fmhc-physics-remote/r3-tests2d-20260930 && \
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3-2d-profile tests2d_r3.py profile
cd /home/fmh/fmhc-physics-remote/r3-tests2d-20260930 && \
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3-2d-tropfen tests2d_r3.py tropfen
cd /home/fmh/fmhc-physics-remote/r3-tests2d-20260930 && \
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3-2d-brechung tests2d_r3.py brechung
```

- **Hochrechnung:** Der Rauchtest druckt je Test "Hochrechnung Hauptlauf" (Schiessen plus 20-mal Entwicklung).
  - Liegt tropfen ueber 540 s, zwei Aufrufe: `tropfen --omega2 0.52` und `tropfen --omega2 0.55`. Sie schreiben
    tropfen_0.52_* bzw. tropfen_0.55_*.
  - Reicht auch das nicht: `--nur-grob`. Dann fehlt die Latte L3; die Leitung entscheidet.
- **"alle" ohne --rauch nicht in einem Aufruf**, das waere laenger als 10 min.
- Die Zahlen des Rauchtests gelten nicht, die Fitfenster sind zu kurz.

## 6. Laufzeit und Speicher (Schaetzung fuer die P4000, nicht gemessen)

- **Grundlage:**
  - qg1 auf der P5000: Schiessen 84 s fuer etwa 40 000 RK4-Schritte; es zaehlen die Kernelstarts.
  - 2D-Schritt: 2 FFT und etwa 13 elementweise Operationen auf complex128. Geschaetzt 4 ns je Gitterpunkt auf der
    P5000, 7 ns auf der P4000 (Faktor 1,7 laut Leitung), plus 25 Prozent fuer die Messungen.

| Teil | Arbeit | erwartet |
|---|---|---|
| profile | 10 Profile schiessen (bis zu 5 x 6000 RK4-Schritte, frueher Abbruch) | 1 bis 2 min |
| tropfen: Schiessen | 2 Profile | 1 bis 1,5 min |
| tropfen: 0,52 grob | 4 Laeufe, 320^2, 20 000 Schritte | etwa 1,2 min |
| tropfen: 0,52 fein | 2 Laeufe, 480^2, 40 000 Schritte | etwa 2,7 min |
| tropfen: 0,55 grob + fein | 4 Laeufe 240^2 x 8000 Schritte; 2 Laeufe 360^2 x 16 000 Schritte | etwa 0,9 min |
| **tropfen zusammen** | | **etwa 6 min (4 bis 9)** |
| brechung: Schiessen | 61 Profile (Familie) | 1 bis 1,5 min |
| brechung: grob + fein | 7 Laeufe 280^2 x 5600 Schritte; 3 Laeufe 420^2 x 11 200 Schritte | etwa 1,3 min |
| **brechung zusammen** | | **etwa 3 min** |

- **Speicher:** Der groesste Stapel (fein, 480^2, 2 Laeufe) braucht etwa 10 bis 20 MB je Feld. Das Periodogramm braucht
  etwa 0,2 GB, der CUDA-Kontext etwa 0,4 GB. Zusammen unter 1 GB, Grenze 2,5 GB.

## 7. Ausgaben (im --out-Ordner)

- `<test>_bericht.txt` (auch auf stdout):
  - Profile, Vorhersage, Messung, Kennzahlen, Kontrollen
  - "Urteil nach PLAN.md" mit Kriterium A, B oder C bzw. dem Brechungsurteil
- `<test>_ergebnis.json`: alle Zahlen einschliesslich Periodogramm-Nebenminima, Vorhersagen aus Profil und Messung
- `<test>_zeitreihen.pt`: Zeitreihen je Lauf; bei `profile` die Radialtabellen f, f'

## 8. Was welches Ergebnis bedeuten wuerde

- **Tropfen A:** Das Tropfenbild aus F-3 traegt quantitativ, auch dynamisch.
  - Die Traegheit des Tropfens ist die Enthalpiedichte, nicht die Ladungsdichte.
  - Weitgehend bekannt (L4): Q-Materie als Fluessigkeit bei Coleman. Die Formel ist Rayleigh (1879) in 2D.
  - Neu waeren nur die Zahlen zur Wandkorrektur.
- **Tropfen B:** Die Oberflaeche schwingt nicht wie ein Tropfen.
  - Zuerst pruefen: das Periodogramm (Nebenminima, R2), die Linearitaetsprobe und L3.
  - Haelt der Befund, dann liest ein zweites Haus.
- **Tropfen C mit Ladungsdichte-Naehe** (Omega/P1 etwa 0,85 bei beiden omega): Befund-Kandidat fuer eine andere
  Traegheit. Das ist die interessanteste Abweichung.
- **Brechung erfuellt:** Q-Baelle brechen wie Teilchen, Snellius mit n = p2/p1. Das ist vorab ableitbar (L4); gemessen
  wird nur die Adiabasie.
- **Brechung verfehlt, Winkel ok, v2 zu klein:** Innere Anregung beim Stufenwechsel. Das ist die Messgroesse.
- **Totalreflexion falsch vorhergesagt:** Befund-Kandidat, zuerst M2 und die Interpolation pruefen.
- **Rauch- oder Hauptlauf bricht beim Schiessen ab:** Codefehler oder Praezisionsgrenze, keine Aussage. Siehe Ausweg in
  Abschnitt 1.

## 9. Grenzen

- **Ungetestet:** Kein Interpreter auf dem Laptop. Zuerst der Rauchtest.
- **2D statt 3D:** Die 3D-Formel hat l(l - 1)(l + 2); Kernoberflaechen (Bohr-Mottelson) sind nur Analogie.
- **Duennwandig nur bedingt:** Bei omega^2 = 0,52 ist die Wanddicke (etwa 3) nicht klein gegen R (17,5). Die Korrekturen
  O(Wand/R) stecken in der Unsicherheit von etwa 5 Prozent.
- **Brechung mit Potentialstufe:** Sie modelliert eine Mediumsstufe nur im Mittelfeld. Reibung, Nachlauf und Streuung an
  einem echten Medium fehlen, dafuer braucht es ein zweites Feld.
- **Literatur** zu Oberflaechenmoden duennwandiger Q-Baelle nicht gesucht (Auftrag: Web nur fuer die Knotenliteratur).
  Wahrscheinlich gibt es sie.

## Latten (Vorschlag, die Leitung entscheidet)

| Karte | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Wellen 16 Tropfen | ja: Omega/P1 und Omega_3/Omega_2 mit Befundgrenzen; Ladungsdichte trennbar (15 %) | ja: Ruhe, Linearitaet, l-Verhaeltnis, Dichtevarianten | geplant: fein gegen grob, Faktor 5 | teilweise: Q-Materie-Tropfen (Coleman), Rayleigh; Oberflaechenmoden nicht gesucht | nein (Kernschwingungen nur Analogie) |
| Wellen 8/9 Magnus/Flettner | entfaellt | entfaellt | entfaellt | ja: Magnuskraft auf Wirbel | nein; **im Ein-Feld-Modell nicht umsetzbar** |
| Wellen 20 Knoten (Papier) | ja | teilweise | entfaellt | ja | nein |

**Vorschlag:**
- Wellen 16: rechnen. Das ist die Kernkarte, sie kann klar scheitern.
- Wellen 14: rechnen, Erwartung "bekannt". Messwert ist nur die Adiabasie.
- Wellen 8/9: als "im Ein-Feld-Modell nicht umsetzbar" parken; mit zweitem Feld nur als L4-Karte.
- Wellen 20: Ein-Feld-Fassung verwerfen, C x S^2 zum CX-1-Strang.

## Einfach gesagt

Wir pruefen am Rechner, ob ein grosser Q-Ball wirklich wie ein Wassertropfen wackelt. Stoesst man einen Tropfen an, schwingt
er als Ei oder Dreieck, und Lord Rayleighs Formel sagt aus Oberflaechenspannung, Dichte und Radius genau voraus, wie
schnell. Diese drei Zahlen lesen wir aus dem Q-Ball selbst ab, anpassen duerfen wir nichts. Beim grossen Ball erwarten wir
eine Schwingungsdauer von etwa 325 Zeiteinheiten fuer das Ei und halb so viel fuer das Dreieck. Weicht der Rechner deutlich
ab, ist das Tropfenbild falsch. Der zweite Test schickt einen Q-Ball schraeg ueber eine Stufe im Feld und prueft, ob er
wie ein Teilchen gebrochen oder ab einem Grenzwinkel zurueckgeworfen wird. Den Magnus-Test mit dem angeschnittenen Ball
lassen wir weg: In unserem Modell gibt es keinen duennen, ruhigen "Wind", in dem der Ball fliegen koennte, denn so ein
Hintergrund klumpt von selbst zu neuen Baellen zusammen.

Ende der Bearbeitung: 2026-09-30 02:08:02 CEST (gemessen mit date). Beginn 2026-09-30 01:20:35 CEST.
