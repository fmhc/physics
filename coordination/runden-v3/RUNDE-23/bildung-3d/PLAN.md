# PLAN BILDUNG-3D (Runde 23, v3 explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary.
  - Beginn 2026-10-02 21:48:38 CEST (date).
  - Plan geschrieben ab 22:04:19 CEST (date), nach dem Rauchlauf und vor jedem echten Lauf.
  - Zeitbox 90 min, also bis 23:18:38 CEST.
- Grundlage: KARTE.md (sha256 1111fff639951d07e0e9b6e576e938df61b823ec3c1d0471d7ccd069b9301eab, ab 21:48:09).
  - Verbindlich und hier unveraendert: Modell M1, radial 3D, Leapfrog mit Absorber und exaktem Startschritt;
    Familie omega^2 0,52 bis 0,90; Klumpen (i) bis (iv); K0; "auf"-Regel; Auswertezeiten 250, 500, 1000; zwei
    Gitter, gewertet dr = 0,02; B3D-0 bis B3D-3; Bedeutung.
  - Explorativ (v3), Deutungen [H, im Modell M1, 3D, l = 0].

## 1. Code

- **code/zeit3d.py** (sha256 c614c1e6498379c9a2ae21e5fa6e87008842447b63ca5bbd77a38d5b24119a3e), neu geschrieben nach
  dem Vorbild RUNDE-22/bildung-leiter/code/zeit2d_v2.py (dort dbd1652e...).
  - Uebernommen: exakter Startschritt (V2-1), Abschnitte bis=/weiter (V2-6), JSON ueber m.jsonfest (V2-4), Absorber
    und dt = 0,4 dr wie dort.
  - Importiert unveraendert RUNDE-22/bildung-leiter/code/bic2_2d_praez_v2.py (sha256 042ba893...ef00): profil (dim = 3),
    f_werte, jsonfest, Konstanten. Auf der .69 liegt eine Kopie im Rechenordner, lokal keine zweite Kopie.
- **hilfs/vergleich.py** (8070d1d7...e1cd): nur Rauchlauf, bitweiser Vergleich zweier Rohdateien.
- Rechenort .69: /home/fmh/fmhc-physics-remote/runde23-bildung-3d/ (aus/, rauch/); Kopie ohne .pt nach lauf-69/.

## 2. Modell und Formeln (vorab festgelegt)

- **Feldgleichung:** psi_tt = lap psi - U'(|psi|^2) psi mit U = S - S^2 + S^3/2, also U' = 1 - 2 S + 1,5 S^2.
- **Gitter:** r_j = j dr, j = 0..N, N = r_max/dr; Dirichlet psi_N = 0.
- **Laplace:** (p[j+1] - 2 p[j] + p[j-1])/dr^2 + (p[j+1] - p[j-1])/(r_j dr) fuer j >= 1; bei r = 0: 6 (p1 - p0)/dr^2.
  - Fuer j >= 1 ist das algebraisch das Schema fuer u = r psi (u_rr / r). p0 haengt nur an p1.
- **Leapfrog:** dt = 0,4 dr, phi_neu = (2 phi - fak_m phi_alt + dt^2 a) fak_p.
  - Absorber gamma = SIGMA0 ((r - r_sd)/(r_max - r_sd))^2 fuer r > r_sd, SIGMA0 = 1.
  - fak_p = 1/(1 + dt gamma/2), fak_m = 1 - dt gamma/2.
- **Integrale:** Trapezregel in r, Gewichte w_0 = 0, w_j = 4 pi r_j^2 dr.
  - Mit diesen Gewichten ist die Ladung im Inneren (ohne Absorber) im Leapfrog exakt erhalten.
- **Ladung:** Q = sum_j w_j (-2 Im(conj(p_j) v_j)), v = (phi(t+dt) - phi(t-dt))/(2 dt).
- **Energie:** E = sum_j w_j (|v_j|^2 + U(|p_j|^2)) + sum_j 4 pi r_(j+1/2)^2 dr |p_(j+1) - p_j|^2/dr^2 (Gradient
  versetzt).
- **Familie** (je Gitter, je omega^2 = 0,52, 0,53, ..., 0,90, also 39 Punkte):
  - m.profil(w2, 3.0, BETA, dr), m.f_werte, f_N = 0, dann Newton (30 Schritte, tridiagonal) auf
    lap f + (w2 - U'(f^2)) f = 0 desselben Gitters.
  - Q_F = 2 omega sum w_j f_j^2 (= 2 omega Integral f^2 4 pi r^2 dr).
  - E_F = sum w_j (omega^2 f_j^2 + U(f_j^2)) + Gradient wie oben.
  - R_rms = sqrt(sum w r^2 f^2 / sum w f^2).
  - Ein Punkt zaehlt nur, wenn der Newton-Rest < 1e-8 ist ("ok").
  - Berichtet werden auch S0, r_halb, Virialrest (Derrick 3D: E_grad = 3 (E_kin - E_pot)), Schwanz S(r_sd)/S0.
- **Klumpen** psi(r, 0) = A exp(-r^2/(2 s^2)), psi_t(r, 0) = -i w0 psi:
  - Die Ladung des 3D-Gauss ist Q = 2 w0 A^2 pi^(3/2) s^3. Gesetzt wird Q = Q_F, also A = sqrt(Q_F / (2 w0 pi^(3/2) s^3)).
  - rms-Radius von |psi|^2 = A^2 exp(-r^2/s^2) ist s sqrt(3/2). Also s = fak R_rms,F sqrt(2/3).
  - (i): omega^2 = 0,60, fak 1,0; (ii): fak 1,3; (iii): fak 0,7; (iv): omega^2 = 0,55, fak 1,0.
  - Jeweils w0 = omega_F = sqrt(omega^2). Q_F und R_rms,F stammen aus dem diskreten Profil desselben Gitters.
  - Vorzeichen wie in BILDUNG-1 und zeit2d_v2: psi_t = -i w0 psi, damit Q = +Q_F.
- **K0:** Reihe "exakt", das diskrete Familienprofil bei omega^2 = 0,60 und bei 0,55 (je ein Lauf je Gitter).
- **Start (alle Reihen):** phi(-dt) = phi - q dt vel + dt^2/2 a(phi), mit q = sqrt(1 - w0^2 dt^2/4) je Reihe.
  - Fuer K0 ist das die exakte Leapfrog-Drehung f exp(-i w_d t) mit w_d = (2/dt) asin(w0 dt/2).
  - Fuer die Klumpen aendert q nur Terme der Ordnung dt^3.
- **Messung:**
  - alle 0,2 Zeiteinheiten (dr 0,02: genau 0,2; dr 0,04: 12 dt = 0,192):
    - psi(0, t)
    - Q und E in r < 10, 20, 30, 40, r_sd, r_max
  - alle 50 Einheiten |psi|^2 im Abstand 0,2 (Schnappschuss)

## 3. Box (Begruendung) und Rauchlauf

- **Box:** r_sd = 60, r_max = 120 (Absorber 60 dick wie in zeit2d_v2, dort 80/140).
  - **Baelle:** R_rms,F = 6,12 (omega^2 0,60) und 11,42 (0,55), r_halb 7,21 bzw. 14,38 (Rauchlauf, dr 0,04).
    - r_sd ist also mehr als das 5-fache des rms-Radius.
    - Der Familienschwanz am Absorberbeginn betraegt S(60)/S0 = 1,5e-31 bzw. 1,5e-28.
  - **Starts:** Fuer (iv), den breitesten Klumpen (s = 9,33), ist S(60)/S(0) = 1,1e-18. Fuer (i) bis (iii) ist der
    Wert kleiner als 1e-37.
  - **Bewegung:** Die Laeufe sind radial, der Ball kann sich also nicht verschieben. Um r_sd bis T = 1000 zu
    erreichen, muesste sich Ballladung mit im Mittel >= (60 - 15)/1000 = 0,045 nach aussen bewegen. Das waere
    Zerfliessen. Die "auf"-Regel sieht das als Ladungsverlust.
  - **Probe nachher** (nur berichtet): Anteil von Q_Ball in r < 30 und Ladung in r < 10 / 20 / 30 / 40 je Fenster,
    dazu die Dichteschnappschuesse.
  - **Abwaegung:** Ein groesseres r_sd haelt langsame Abstrahlung (Gruppengeschwindigkeit nahe 0) laenger im
    Messvolumen und erhoeht damit Q_Ball. 60 haelt beides klein; der Kernanteil wird mitberichtet.
- **Rauchlauf** (vor diesem Plan; .69, 20:00:49 bis 20:04:12 UTC; lauf-69/rauch/):
  - **Familie dr 0,04, r_max 110 und 120** (0,52 / 0,55 / 0,58 / 0,60 / 0,62 / 0,65 / 0,90):
    - Q_F = 280322 / 19772 / 5291 / 2873 / 1760 / 980 / 115,6
    - E/Q = 0,728 / 0,760 / 0,791 / 0,812 / 0,832 / 0,861 / 1,015
    - Newton-Rest 1e-13 bis 5e-13, Virialrest -7e-5 (O(dr^2))
    - 5,4 bis 9,7 s je Punkt
  - **Zeitlauf T = 20**, dr 0,04 (6 Reihen) und dr 0,02 (K0-0.60, i):
    - K0-Mass 8,1e-13 / 2,2e-12 (dr 0,04) bzw. 2,9e-12 (dr 0,02)
    - K0: omega_mess = sqrt(0,6) auf 1e-14 genau, Abweichung Q_Ball gegen Q_F -1,9e-5 (O(dt^2)), E/Q gleich der
      Familie auf 1e-6
  - **Abschnitte:** bis=10 und weiter sind bitgleich zum Einmal-Lauf (zentrum, ladung, energie, schnapp).
  - **Zeit je Schritt:**
    - dr 0,02, 2 Reihen, N = 6000: 1,63 ms. T = 1000 heisst 125000 Schritte, also ~205 s, mit Profil ~220 s.
    - dr 0,04, 6 Reihen, N = 3000: 2,12 ms, also ~135 s.
  - **Startwerte** (dr 0,04):
    - A^2 = 2,67 (i), 1,22 (ii), 7,78 (iii), 2,95 (iv), gegen S0 = 1,09 bzw. 1,05 der Baelle.
    - E/Q zu Beginn: 0,905 (i), 0,870 (ii), **3,10 (iii)**, 0,918 (iv); Familie 0,812 bzw. 0,760.
    - Q auf dem Gitter = Q_F auf 1e-15.
  - **Folge fuer den Code (vor diesem Plan geaendert, Rauchlauf danach wiederholt):** Bei (iii) erreichte der
    Phasensprung je Messpunkt bis t = 20 3,08 rad. Neu ist deshalb die Regel "Phase unsicher" (Abschn. 4).
- **Empfindlichkeit der "auf"-Regel** (vorab, aus dem Rauchlauf):
  - Bei omega^2 = 0,60 ist d ln Q_F / d omega^2 ~ -27,5 (0,58 bis 0,62). 10 % in Q entsprechen dort
    Delta omega ~ 0,0023.
  - Bei 0,55 ist die Kurve steiler, dort entsprechen 10 % etwa Delta omega ~ 0,0012.
  - Die Regel prueft also eine Frequenz auf 0,2 bis 0,3 %.

## 4. Auswertung (fest)

- **omega_mess** je Fenster [T - 50, T], T = 250, 500, 1000:
  - Phase am Zentrum abgewickelt, als Summe der Hauptwerte arg(psi_n+1 / psi_n).
  - Linearer Fit phase = a + b t im Fenster, w_d = -b.
  - Umrechnung auf den Familienparameter: omega_mess = (2/dt) sin(w_d dt/2). Das ist die exakte Umkehrung der
    Leapfrog-Drehung; die Aenderung ist ~1e-6.
- **Q_Ball** = Mittel der Ladung in r < r_sd ueber dasselbe Fenster. **Ladungsanteil** = Q_Ball / Q(r < r_sd, t = 0).
- **Q_F(omega_mess):** kubischer Spline (scipy CubicSpline, not-a-knot) von ln Q_F ueber omega^2, durch die
  ok-Punkte der Familie desselben Gitters. Ebenso fuer E_F/Q_F, S0 und R_rms (nur berichtet).
- **"auf"** zu T:
  - abw = (Q_Ball - Q_F(omega_mess)) / Q_F(omega_mess); "auf", wenn |abw| < 0,10, sonst "nicht auf".
  - **Sonderfaelle**, in dieser Reihenfolge:
    - Groesster Phasensprung je Messpunkt im Fenster > pi/2: "offen (Phase unsicher)".
    - omega_mess <= 0, omega_mess^2 <= 0,5 oder >= 1: Fuer M1 gibt es dort keinen Q-Ball. Urteil "nicht auf (keine
      Familie)".
    - omega_mess^2 in (0,5; 0,52) oder (0,90; 1): ausserhalb der Tabelle, "offen (ausserhalb der Tabelle)".
- **Berichtet** je Fenster:
  - E/Q (Mittel E / Mittel Q in r < r_sd) gegen E_F/Q_F(omega_mess)
  - Atmungsamplitude: Spanne der Zentraldichte (max - min) absolut und relativ zum Fenstermittel
  - Ladungsanteil, Kernanteil Q(r < 30)/Q_Ball, R_rms in r < 30 (aus dem Schnappschuss bei T)
  - S0 gegen S0_F(omega_mess)
  - Restfehler des Phasenfits
  - Atmungsfrequenz: Periodogramm-Gipfel der Zentraldichte in [T - 200, T]
- **B3D-0** (dr 0,02): K0-0.60 und K0-0.55, max_t |S(0, t) - S(0, 0)| / S(0, 0) ueber [0; 1000].
  - Beide < 1e-8: **eingetroffen**.
  - Einer >= 1e-8: **nicht eingetroffen**.
  - Fehlt ein Lauf: **offen**.
- **B3D-1** (dr 0,02): (i) bei T = 500 "auf" heisst **eingetroffen**, "nicht auf ..." **nicht eingetroffen**, sonst
  **offen**.
- **B3D-2** (dr 0,02): (ii) und (iii) bei T = 1000 beide "auf" heisst **eingetroffen**. Einer "nicht auf ..." heisst
  **nicht eingetroffen**, sonst **offen**.
- **B3D-3** (dr 0,02, (iv) bei T = 1000). Die Vorhersage nennt einen Grund ("weil er weiter deutlich atmet"), deshalb
  muessen beide Teile gelten:
  - "nicht auf ..." und Spanne_rel im Fenster [950; 1000] > 0,05: **eingetroffen**.
  - "auf": **nicht eingetroffen**.
  - "nicht auf ..." mit Spanne_rel <= 0,05: **nicht eingetroffen**, weil der genannte Grund nicht zutrifft.
  - Sonst **offen**.
- dr 0,04 wird mit denselben Regeln berichtet (Latte L3 Numerik), aber nicht gewertet.
- **Bedeutung:** wortgleich nach Karte, mechanisch aus den Ausgaengen.
- Die Wertung rechnet zeit3d.py auswerten (Funktion wertung) auf der .69; jq nur fuer Tabellen.

## 5. Laeufe

- **Zeitlaeufe** (T = 1000, r_sd 60, r_max 120, je ein Aufruf ohne Abschnitte; geschaetzt 150 bis 230 s):

| Aufruf | Spur | dr | Reihen |
|---|---|---|---|
| l02-a | cpu | 0,02 | K0-0.60, i |
| l02-b | cpu2 | 0,02 | ii, iii |
| l02-c | cpu3 | 0,02 | K0-0.55, iv |
| l04 | cpu4 | 0,04 | alle sechs |

- **Familie** (r_max 120, r_sd 60; geschaetzt 6 bis 12 s je Punkt):
  - dr 0,02 in drei Aufrufen: 0,52 bis 0,64 / 0,65 bis 0,77 / 0,78 bis 0,90
  - dr 0,04 in zwei Aufrufen: 0,52 bis 0,70 / 0,71 bis 0,90
- **Ketten je Spur:**
  - cpu: l02-a, dann fam04-a
  - cpu2: l02-b, dann fam04-b
  - cpu3: l02-c
  - cpu4: l04, dann fam02-b
  - cpu6: fam02-a, dann fam02-c
  - Danach ein Aufruf "auswerten" mit allen vier Rohdateien und allen fuenf Familiendateien.
- **Falls ein Aufruf an 600 s faellt:** Wiederholung mit bis=500 und weiter, dokumentiert. Die Rechnung ist dabei
  bitgleich (Rauchlauf).
- **Nach dem Einfrieren** aendere ich weder Code noch Regeln. Nachtraege nur eingefroren und als nachtraeglich markiert.
