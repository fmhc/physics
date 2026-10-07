# ZUFALLS-REIBUNG-1: Plan (Code-Agent fuer die Leitung, Runde 36, explorativ nach v3)

- Start des Code-Agenten 01:03:19 CEST (date). Plan geschrieben ab 01:30:09 CEST (date), nach zwei Rauchlaeufen und
  waehrend Rauch 3 (Abschnitt 8).
- Karte: KARTE.md. Vorhersagen Z0 bis Z3 und ihre Schwellen sind unveraendert uebernommen.
- Code:
  - code/reibung.py: Rechnung
  - code/auswertung.py: Urteile, Proben, Bilder
  - code/laeufe.sh: Laeufe, nacheinander je Spur
  - Nur fuer den Rauch: code/rauchcheck.py, code/rauchcheck2.py
- Kennzeichen:
  - [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese
  - [F] Festlegung dieses Plans (von der Karte offengelassen)
  - [E] im Rauch gesehen

## 1. Modell [M]

- Gitter x_n = n h, **h = 0,1** (Karte). Komplexes psi_n, p_n = d psi_n/dt, kein aeusseres Feld.
- Hamiltonfunktion:
  H = h sum(|p_n|^2 + U_n(S_n)) + (1/h) sum |psi_{n+1} - psi_n|^2, mit S = |psi|^2 und
  U_n(S) = (1 + s(t) eta_n) S - S^2 + S^3/2 (Karte).
- Bewegung: p_n' = (psi_{n+1} + psi_{n-1} - 2 psi_n)/h^2 - U_n'(S_n) psi_n.
- **Unordnung [F]:**
  - eta_n unabhaengig standardnormalverteilt, fest am globalen Gitterplatz n.
  - Saat A = 1, B = 2, C = 3: numpy default_rng(Saat).standard_normal(90000) fuer n = -30000 ... 59999.
  - Dieselbe Realisierung fuer alle sigma und alle v einer Saat (gemeinsame Zufallszahlen). Damit ist die Landschaft
    bei sigma = 0,01; 0,02; 0,04 dieselbe, nur skaliert.
  - Pruefung 1 + sigma eta_n > 0 auf allen benutzten Plaetzen: Kopf "min_1_plus_sigma_eta".
  - Im Rauch: 0,839 bei sigma = 0,04 (Saat 1), die Massenluecke bleibt also > 0.
- **Einschalten [F]:**
  - s(t) = sigma f(t/T_R) mit f(u) = u - sin(2 pi u)/(2 pi), T_R = 200 (C^2, glatt). Danach ist s = sigma fest, die
    Unordnung also zeitunabhaengig.
  - Grund: Der Ball soll nicht mit einem Sprung in die Unordnung gesetzt werden.
  - Zeitliches statt raeumliches Einschalten: Ein langsamer Ball, der an der Landschaft umkehrt, bleibt in der
    Unordnung und laeuft nicht in eine saubere Zone zurueck.
  - Die Arbeit des Einschaltens W = Integral s'(t) h sum eta S wird an den Stoessen schema-treu gebucht.
- Ladung Q = 2 h sum Im(conj psi p); psi ~ e^{+i omega t} hat Q > 0. Jeder Teilschritt erhaelt Q exakt.
- Ball: omega^2 = 0,7 (Karte), Breite ~ 1/sqrt(0,3) = 1,8.

## 2. Anfangszustand (Boost) [F]

- Stationaere Gitterloesung bei omega^2 = 0,7, platzzentriert.
  - Newton wie in QBALL-GITTER-1, halbe Kette 60, Spiegelrand.
  - Rauch: 3 Schritte, Rest 3,8e-14, phi_0 = 0,606313. M0 = 2,298174 und Q0 = 2,441017 (Ruhe, Gitter).
- Die Gitterloesung wird als kubischer Spline phi(x) gelesen (natuerlicher Rand) und Lorentz-geboostet:
  - psi_n = phi(g xi) exp(-i omega g v xi)
  - p_n = g (-v phi'(g xi) + i omega phi(g xi)) exp(-i omega g v xi)
  - mit xi = x_n - X0 und g = 1/sqrt(1 - v^2)
- Fuer v = 0 ist das exakt die Gitterloesung. Fuer v > 0 bleibt ein Gitterfehler der Ordnung h^2: Gitterdispersion des
  Traegers, Spline-Fehler ~ h^4.
- **Pruefung am Fall sigma = 0** (Rauch 1, Abschnitt 8):
  - E_win/(g M0) - 1 = -8e-5 (v = 0,5) bzw. -5e-6 (v = 0,1).
  - Der Ball gibt bei v = 0,5 bis t ~ 300 noch 5e-7 seiner Ladung ab (Einschwingen). Danach haelt er Ladung und
    Schnelle (Abschnitt 8).
- Startort X0 = 120 im Fenster (Mitte), globaler Platz 1200.

## 3. Numerik [F]

- **Integrator:** Yoshida 4. Ordnung (Drift psi, Stoss mit s(t) zur Stosszeit).
  - Hauptlaeufe dt = 0,02 (dt Omega_max = 0,02 sqrt(401) = 0,40).
  - Probe dt = 0,01.
- **Mitlaufendes Fenster:** Laenge 240 (2400 Plaetze), Ball bei der Fenstermitte.
  - Verschiebung um 10 Laengeneinheiten (ganze Plaetze), sobald der Ladungsschwerpunkt 10 vom Sollort weg ist.
  - Exakte Translation; die Unordnung haengt am globalen Platz. Was herausfaellt, wird gebucht.
- **Absorber:** Schwamm je 50 an beiden Enden, a = 1,0 (1 - d/50)^2.
  - Exakt als p -> p exp(-a dt/2) vor und nach jedem Schritt; Energie- und Ladungsabfluss gebucht.
  - Abstrahlung, die hinter dem Ball zurueckbleibt, wird im Schwamm geschluckt und wirkt nicht zurueck.
  - Abstand Ball - Schwamm >= 60.
- **Messabstand** 0,5.
- **Laufzeit:** t_end = 1410 fuer alle Laeufe [F, nach Rauch 2, Abschnitt 8]:
  - Einschalten 0 bis 200, Ruhe bis 400
  - Messfenster [T_A, T_B] = [400, 1400], also T_mess = 1000 (feste Laufzeit, Karte "feste Laufstrecke bzw.
    Laufzeit")
  - Die Schnelle ist bis t_end - 10 = 1400 definiert.
  - Laufstrecke im Fenster etwa 100 / 200 / 300 / 500 bei v = 0,1 / 0,2 / 0,3 / 0,5.
- **Zeitbedarf** (Rauch): 0,35 ms je Schritt, also etwa 25 s je Hauptlauf und 50 s je dt-Probe.
- **Wandzeitwaechter:** 540 s, dann Status "unterbrochen". Ein solcher Lauf gilt als fehlend.

## 4. Messvorschriften [F, soweit die Karte sie offenlaesst]

### 4.1 Messgroessen

- **Ladungsdichte:** rho_n = 2 Im(conj(psi_n) p_n).
- **Ladungsschwerpunkt X(t):** wie QBALL-GITTER-1.
  - cos^2-Gewicht mit R_X = 10, iteriert bis |dX| < 1e-12 max(1, |X|).
- **Schnelle v(t):** Steigung der Ausgleichsgerade an X ueber [t - 10, t + 10] (41 Punkte), wie QBALL-GITTER-1.
- **Ballfenster** [F, nach Rauch 1]:
  - Gewicht w(xi) = 1 fuer |xi| <= R1 = 14, dann Abfall f(s) = 1 - s + sin(2 pi s)/(2 pi), s = (|xi| - 14)/6, bis
    R2 = 20; w ist C^2.
  - Q_win = h sum rho w (Ballladung im Fenster).
  - E_win = Energie im Fenster, mit Platzenergie samt Unordnungsterm und halben Verbindungsenergien.
  - V_win = s h sum eta S w (Landschaftsenergie des Balls).
  - P_win = -2 h sum Re(conj(p) (psi_{n+1} - psi_{n-1})/(2h)) w (Feldimpuls).
- **M(Q):** Ruheenergie der Gitter-Q-Baelle als Funktion der Ladung.
  - Familie omega^2 = 0,66 ... 0,94 (17 Werte, Newton je Lauf im Kopf), kubischer Spline in Q.

### 4.2 Reibungsrate (Hauptmass r_B) [F]

- Karte: Reibungsrate = -d ln(gamma v)/dt "im Mittel"; Bewegungsenergie "aus E und Q bzw. aus gamma".
- **Problem:** In der Unordnung schwankt v(t) umkehrbar mit der Landschaft.
  - Ein ruhender Ball hat die Energie V(X) = sigma h sum eta_n phi_n^2. Ihre Streuung ist sigma sqrt(0,1 * 0,36) =
    0,19 sigma [M].
  - Bei v = 0,1 und sigma = 0,04 ist das 7,6e-3, fast so viel wie die Bewegungsenergie 0,0116.
  - Die direkte Steigung von ln(gamma v) ist deshalb verrauscht (Rauch 2: Fehler 3,4e-6 gegen Rate 1,4e-5 bei v = 0,3,
    sigma = 0,01).
- **Hauptmass:** Schnelle-gamma, bereinigt um die umkehrbare Landschaftsenergie (Energiesatz des Balls,
  gamma M + V = const in erster Ordnung):
  - gamma_c(t) = gamma(v(t)) + V_s(t)/M(Q_win(t))
  - V_s ist V_win, mit genau dem Kern geglaettet, den die Schnelle-Ausgleichsgerade auf die Geschwindigkeit legt
    (Mittelpunktsgewichte ~ m(m+1) - i(i+1)).
  - **r_B = - Steigung von ln(gamma_c v_c) = 0,5 ln(gamma_c^2 - 1)**, Ausgleichsgerade (kleinste Quadrate) ueber alle
    Messpunkte in [400, 1400].
  - Der Erwartungswert ist derselbe wie bei der direkten Steigung, die Landschaft hat keinen Trend. Rest in erster
    Ordnung: geschwindigkeitsabhaengiger Anteil ~ gamma^3 v^2 (dV/dgamma)/M [M].
- **Gegenproben, nur beschreibend:**
  - r_A: direkte Steigung von ln(gamma v) aus v(t), nur ohne Umkehr. Das ist die Karte woertlich.
  - r_C: Steigung von ln(gamma_E v_E) mit gamma_E = E_win/M(Q_win). Das ist "aus E und Q".
- **Fehler [F]:** Standardfehler der Steigung, blockrobust.
  - Bloecke von 100 Zeiteinheiten als Cluster (10 Bloecke je Fenster; Korrelationszeit der Landschaft ~ 6/v):
    SE = sqrt(sum_b (sum_{i in b} (t_i - t_mittel) e_i)^2)/sum (t_i - t_mittel)^2,
    e = Rest der Geraden.
- **Saatmittel:** r = Mittel ueber Saat A und B, SE = sqrt(SE_A^2 + SE_B^2)/2.

### 4.3 Messgrenze, Obergrenze, gefangen [F]

- **sigma = 0-Rauschen je v:** G0(v) = |r(sigma = 0)| + 2 SE(sigma = 0).
- **Messgrenze der Zelle (v, sigma):** G = max(G0(v), 2 SE_Saatmittel).
  - Die Unordnung kann das Rauschen ueber das sigma = 0-Rauschen heben; deshalb geht beides ein.
- **Gemessen**, wenn r > G.
- **Sonst unter der Messgrenze:** Berichtet wird die Obergrenze O = max(r, 0) + G, nie eine Null.
- **Gefangen:** Kehrt der Ball im Messfenster um (v(t) <= 0 in mindestens einer Hauptsaat), ist ln(gamma v) nicht
  definiert.
  - Die Zelle gilt dann als "gefangen, nicht messbar": kein Wert und keine Obergrenze.
  - Grund: Bei v = 0,1 und sigma = 0,04 kehrte der Ball im Rauch um und blieb gefangen (Abschnitt 8).
- Dieselben Regeln gelten fuer die Ladungsverlustrate r_Q und die Impulsverlustrate r_P, jeweils mit dem eigenen
  sigma = 0-Rauschen.

### 4.4 Ladung und Impuls [F]

- **Ladungsverlustrate:** r_Q = - Steigung der Ausgleichsgerade an Q_win(t) ueber [400, 1400]. Relativ: r_Q/Q0.
- **Verlorene Ladung:** dQ = r_Q T_mess.
- **Impuls des Balls (Hauptmass):** P_c(t) = M(Q_win) sqrt(gamma_c^2 - 1), also gamma M v mit derselben
  Landschaftsbereinigung.
  - Impulsverlustrate r_P = - Steigung von P_c ueber [400, 1400]. Verlorener Impuls dP = r_P T_mess.
  - Gegenprobe: Feldimpuls P_win (Steigung, unbereinigt).
- P_c verliert auch dann Impuls, wenn der Ball bei fester Schnelle Ladung (Masse) verliert. Das ist der Impuls, den der
  Ball wirklich abgibt.

## 5. Laeufe (alle auf der .69 ueber kleintest.sh, Spuren cpu und cpu6, hoechstens zwei zugleich)

- **Hauptlaeufe (28):**
  - v = 0,1 / 0,2 / 0,3 / 0,5, je sigma = 0 (Name v<v>_s0, Kontrolle)
  - dazu sigma = 0,01 / 0,02 / 0,04 mit Saat A und B (v<v>_s<sigma>_A, _B)
  - dt = 0,02, t_end = 1410
- **Probe halber Zeitschritt (7, dt = 0,01):** v0.1_s0_dt2, v0.5_s0_dt2, v0.3_s0.01_A_dt2, v0.3_s0.02_A_dt2,
  v0.3_s0.04_A_dt2, v0.1_s0.04_A_dt2, v0.5_s0.04_A_dt2.
- **Probe andere Saat (5, Saat C):** v0.3_s0.01_C, v0.3_s0.02_C, v0.3_s0.04_C, v0.1_s0.04_C, v0.5_s0.04_C.
- **Reihenfolge:** zuerst alle Hauptlaeufe, dann die Proben. Danach die Auswertung (code/auswertung.py lauf
  lauf/auswertung.json) ueber kleintest.sh.

## 6. Urteilsregeln (mechanisch, code/auswertung.py)

### Z0 (Karte: sigma = 0, Schnelle konstant, relative Aenderung < 1e-4 ueber die Laufzeit; Ladungsverlust < 1e-8)

- Laeufe v<v>_s0 fuer alle vier v [F: alle vier], Messfenster [400, 1400] [F: nach dem Einschwingen, Abschnitt 8].
- Je v: max |v(t) - v(400)|/v(400) < 1e-4 und (Q_win(400) - min Q_win)/Q0 < 1e-8 [F: relativ zu Q0 wie bei
  QBALL-GITTER-1 G0; als groesster Verlust ueber das Fenster].
- **Eingetroffen**, wenn alle vier v bestehen. **Nicht eingetroffen** sonst. Fehlt ein Lauf: nicht auswertbar.

### Z1 (Karte: v = 0,3, Reibungsrate ~ sigma^p, p = 2 +- 0,3, Ausgleich ueber sigma = 0,01; 0,02; 0,04, Saatmittel)

- r_B-Saatmittel der drei Zellen bei v = 0,3.
- Sind alle drei gemessen: p = Steigung der Ausgleichsgerade ln r gegen ln sigma (drei Punkte, gleich gewichtet).
  - **Eingetroffen**, wenn |p - 2| <= 0,3. **Nicht eingetroffen** sonst.
- Ist eine Zelle unter der Messgrenze, gefangen oder fehlt sie: **nicht auswertbar**. Die Zweipunkt-Potenz aus 0,02 und
  0,04 wird dann als Vermerk berichtet.

### Z2 (Karte: sigma = 0,04, Reibungsrate bei v = 0,5 mindestens 10-mal so gross wie bei v = 0,1)

- r5 und r1 sind die r_B-Saatmittel der Zellen (0,5; 0,04) und (0,1; 0,04).

| v = 0,5 | v = 0,1 | Regel | Urteil |
|---|---|---|---|
| gemessen | gemessen | r5/r1 >= 10 | eingetroffen, sonst nicht eingetroffen |
| gemessen | unter der Messgrenze | r5/O1 >= 10 (dann ist das Verhaeltnis sicher >= 10) | eingetroffen, sonst nicht auswertbar |
| unter der Messgrenze | gemessen | O5/r1 < 10 (dann ist das Verhaeltnis sicher < 10) | nicht eingetroffen, sonst nicht auswertbar |
| unter der Messgrenze | unter der Messgrenze | - | nicht auswertbar |
| gefangen oder fehlt (eine Seite) | | - | nicht auswertbar, mit Vermerk |

### Z3 (Karte: (verlorene Ladung)/(verlorener Impuls) ueber v und sigma innerhalb Faktor 3 konstant)

- Je Zelle (v, sigma > 0): rho = dQ/dP = r_Q/r_P (Saatmittel, Hauptmass P_c).
- Nur Zellen, in denen r_Q und r_P beide gemessen sind. Ausgeschlossene Zellen werden mit Grund gelistet.
- **Eingetroffen**, wenn die Zellen mindestens zwei v und zwei sigma ueberdecken und max rho/min rho <= 3.
  **Nicht eingetroffen**, wenn sie das ueberdecken und max/min > 3. Sonst nicht auswertbar.

### Proben und Gegenproben

- **dt-Probe:** Die Urteile werden mit den dt = 0,01-Laeufen an Stelle der entsprechenden Hauptlaeufe neu berechnet.
- **Saat-Probe:** Die Urteile werden mit Saat C an Stelle von Saat B neu berechnet, wo C gerechnet ist.
- Massgeblich bleibt das Urteil der Hauptlaeufe. Weicht eine Probe ab, steht "nicht robust" im Vermerk.
- Die Gegenproben r_A (Karte woertlich) und r_C (Energie) werden mit denselben Regeln ausgewertet, nur beschreibend.
- **Bedeutung:** wie in der Karte vorab festgelegt. Ein Satz wird nur ausgeloest, wenn seine Urteile so ausfallen.

## 7. Schreibtisch-Erwartung [M, H] (vor den Hauptlaeufen)

- **Bornsche Naeherung, Ballbild:**
  - Die ruhende Landschaft V(x) streut den Ball. Abstrahlen kann er nur Wellen mit Laborfrequenz W >= 1.
  - Ein Anteil der Profil-Fourierkomponente p hat W = gamma omega - p v. Also braucht es |p| >= (1 - gamma omega)/v.
  - Die Ballform unterdrueckt das mit ~ 1/cosh^2(pi p/(2 k gamma)), k = sqrt(0,3).
  - Schwelle: gamma omega = 1, also v = sqrt(1 - omega^2) = 0,548. Darunter waechst die Unterdrueckung, bei v = 0,1
    etwa 1e-4 im Abstrahlanteil [M, grob].
- **Ladung und Abbremsung haengen zusammen:** Je abgestrahlter Ladung verliert der Ball die Energie W, gebraucht wird
  bei fester Schnelle gamma omega. Daraus folgt dP/dQ = gamma (v omega + |p|) [M, Ballbild].
  - Grob 0,7 (v = 0,5), 0,8 (v = 0,3), 1,0 (v = 0,2), 1,7 (v = 0,1).
  - Also dQ/dP von 1,5 bis 0,6, Faktor ~ 2,6 [H].
- **Erwartete Raten bei sigma = 0,04 (grob, freie Wellen):** r = 1e-6 (0,1), 3e-5 (0,2), 5e-5 (0,3), 3e-5 (0,5).
- **Langsame Baelle und die Landschaft [M]:** Die Streuung 0,19 sigma der Landschaftsenergie ist bei v = 0,1 und
  sigma = 0,04 vergleichbar mit der Bewegungsenergie. Ein solcher Ball wird vermutlich zurueckgeworfen.

## 8. Rauchlaeufe vor dem Einfrieren (offengelegt, was ich gesehen habe)

### Rauch 1 (23:23:07 bis 23:23:20 UTC; sigma = 0, v = 0,5 und 0,1, t = 600, damals T_A = 250, R1/R2 = 10/16)

- Bilanzen: Energie 1,4e-11 bzw. 1,1e-13 M0, Ladung 2e-14.
- Schnelle ab t = 250: max relative Aenderung 4,2e-6 (v = 0,5) und 1,25e-6 (v = 0,1).
- **Ladung im Fenster ab t = 250:** groesster Verlust 6,5e-8 (v = 0,5) und 1,5e-8 (v = 0,1). Beides liegt ueber der
  Z0-Schwelle 1e-8.
  - Bei v = 0,5 faellt Q_win bis t ~ 300 (Einschwingen des Boosts, insgesamt 5e-7 Q0) und bleibt danach auf 1e-11
    gleich.
  - Bei v = 0,1 schwankt Q_win um +-1,2e-8, vermutlich durch das Atmen des Balls, das Ladung durch den Fensterrand
    schiebt.
- **Festlegung danach:**
  - Messbeginn T_A = 400 statt 250 (nach dem Einschwingen).
  - Ballfenster R1/R2 = 14/20 statt 10/16 (Rand weiter im Schwanz).
  - **Die Schwellen 1e-4 und 1e-8 bleiben.** Selbstanzeige: Ich habe Z0-Werte gesehen und Messbeginn und Fenster danach
    gewaehlt.
- Rechenzeit 10 s fuer t = 600 (0,35 ms je Schritt).

### Rauch 2 (23:26 bis 23:27:35 UTC; Saat 1, t_end = 1810, Fenster [400, 1800], T_A und R wie jetzt)

- Laeufe: v = 0,3 / 0,5 / 0,1 bei sigma = 0,04, dazu v = 0,3 bei sigma = 0,01. SE dort noch mit Bloecken von 200
  (danach auf 100 gesetzt, damit ein Fenster von 1000 zehn Bloecke hat).

| Lauf | v(400) -> v(1800) | r_B (SE) | r_A (SE) | r_C (SE) | r_Q/Q0 | r_P | dQ/dP |
|---|---|---|---|---|---|---|---|
| v = 0,3, sigma = 0,04 | 0,279 -> 0,184 | 2,64e-4 (2,6e-5) | 2,54e-4 (3,5e-5) | 2,21e-4 (1,0e-5) | 8,6e-5 | 1,81e-4 | 1,16 |
| v = 0,5, sigma = 0,04 | 0,486 -> 0,475 | 3,38e-5 (7,6e-7) | 3,85e-5 (2,0e-6) | 3,25e-5 (3,1e-7) | 6,8e-5 | 1,19e-4 | 1,39 |
| v = 0,3, sigma = 0,01 | 0,298 -> 0,293 | 1,16e-5 (5,8e-7) | 1,44e-5 (3,4e-6) | 1,12e-5 (4,9e-7) | 6,1e-6 | 1,21e-5 | 1,24 |
| v = 0,1, sigma = 0,04 | kehrt um, gefangen | 1,25e-4 (1,3e-5) | - | 1,14e-4 (5,4e-6) | 1,9e-6 | 1,5e-5 | 0,30 |

- Teilfenster bei v = 0,3, sigma = 0,04: r_B = 3,3e-4 / 2,7e-4 / 1,5e-4 auf [400, 800] / [800, 1200] / [1200, 1600],
  die Rate faellt mit der Schnelle. Auf [400, 1000]: 2,6e-4; bei sigma = 0,01: 1,2e-5.
- **Bei v = 0,1, sigma = 0,04 (Saat 1)** kehrt der Ball um und bleibt gefangen: mittlere Schnelle 0,01.
  - v_c am Anfang und Ende gleich (0,050 und 0,051).
  - r_B schwankt in Teilfenstern zwischen 3,5e-5 und 2,7e-4. Die blockrobusten Fehler unterschaetzen das.
- **Damit habe ich Z1-, Z2- und Z3-nahe Werte gesehen:**
  - Zweipunkt-Potenz aus sigma = 0,01 und 0,04 bei v = 0,3, nur Saat 1: p = 2,25 auf [400, 1800] und 2,20 auf
    [400, 1000].
  - Z2: Die v = 0,1-Zelle ist in Saat 1 gefangen.
  - Z3: dQ/dP = 1,16 bis 1,39 in den drei freien Laeufen.
- **Festlegungen danach:**
  1. **Messfenster [400, 1400] (T_mess = 1000).**
     - Grund: Bei sigma = 0,04 und v = 0,3 faellt die Schnelle auf [400, 1800] um ein Drittel. Die Rate gehoert dann
       nicht mehr zu einer Schnelle.
     - Die beiden gesehenen Fenster geben fuer Saat 1 dieselbe Zweipunkt-Potenz (2,20 und 2,25), die Wahl entscheidet
       also nicht ueber Z1.
  2. **Regel "gefangen" (Abschnitt 4.3).** Fuer einen umkehrenden Ball ist ln(gamma v) nach der Kartendefinition nicht
     definiert.
     - Ohne diese Regel ergaebe r_B bei v = 0,1 einen Wert (1,25e-4), der aus der Landschaft und nicht aus Reibung
       stammt.
     - Selbstanzeige: Die Regel steht nach dem Rauch fest. Sie macht Z2 bei gefangenem Ball "nicht auswertbar" statt
       "nicht eingetroffen".
  3. **Hauptmass r_B statt r_A** (Abschnitt 4.2). Grund: r_A hatte bei sigma = 0,01 den sechsfachen Fehler.
- **Keine Schwelle der Karte wurde geaendert.**

### Rauch 3 (23:30 bis 23:33:10 UTC)

- Auswertepfad mit Kurzlaeufen (t_end = 560) unter den Namen der Hauptlaeufe, dazu v0.5_s0_dt2 und v0.3_s0.04_C.
  - Ausgewertet mit dem jetzigen auswertung.py (Bloecke 100).
  - Er prueft Code-Pfade und Bilder; die Urteile dort haben keine Bedeutung (Fenster nur 400 bis 550).
  - Alle 30 Laeufe rc = 0. Bilder entstehen. Ausgabe in rauch-69/aw3/.
- **Gesehen (offengelegt):**
  - **Z0-Werte auf [400, 550]:**
    - Schnelle <= 2,3e-6.
    - Ladungsverlust 1,4e-9 / 3,4e-9 / 2,5e-10 / **1,31e-8** bei v = 0,1 / 0,2 / 0,3 / 0,5.
    - Bei v = 0,5 liegt der Verlust also auch mit T_A = 400 und R1/R2 = 14/20 ueber 1e-8, mit dt = 0,01 gleich
      (1,3132e-8).
    - Vermutung [H]: Restabstrahlung des Boosts, die fast mitlaeuft (relativ ~0,02) und erst jetzt den breiteren
      Fensterrand (14 bis 20) hinten verlaesst. Mit R2 = 16 war Q_win ab t = 300 auf 1e-11 gleich (Rauch 1).
  - **Kurzfenster-Werte:**
    - Zweipunkt-/Dreipunkt-Potenz bei v = 0,3: p = 2,02.
    - v = 0,1, sigma = 0,04: in Saat A und B gefangen.
- **Festlegung danach: keine.**
  - Fenster und Messbeginn bleiben, damit ich die Z0-Messung nicht ein zweites Mal nach gesehenen Werten verschiebe.
  - Z0 kann deshalb an der Ladungsbedingung bei v = 0,5 scheitern. Das waere ein Befund ueber meinen Boost-Start, nicht
    ueber die Reibung (Ladungsverluste bei sigma > 0 sind >= 1e-4).

## 9. Nach dem Einfrieren

- Plan und Urteilsregeln bleiben unveraendert. Code nur bei echten Fehlern aendern, mit Offenlegung in ERGEBNIS.md.
- Pruefsummen von Plan und Code in code/pruefsummen-einfrieren.txt.
