# LICHT-1: Plan (Code-Agent fuer claude-primary, Runde 34)

- Geschrieben ab 2026-10-03 19:15:52 CEST (date). Wird vor der ersten echten Rechnung eingefroren:
  PLAN.md.eingefroren-<datum-uhrzeit>, code/licht.py.eingefroren-<...>, code/laufplan.eingefroren-<...>.tar.
- Karte: KARTE.md (Schreibtisch, L0 bis L3 und Bedeutung unveraendert).
- Code: code/licht.py (neu; Zeitentwicklung, Boost, Schwamm und Bilanz uebernommen aus RUNDE-34/einfang-1/code/einfang.py)
  und code/kegel_q.py (unveraenderte Kopie von RUNDE-26/kegel-q/code/kegel_q.py.eingefroren-20261003-043140,
  sha256 4de64b080729204c...).
- Rechnen nur auf der .69 ueber kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde34-licht/. Hoechstens eine
  P4000-Spur (p4000a) und eine CPU-Spur (cpu) zugleich; cpu2 und cpu5 nicht.

## 1. Teil A (statisch, radial)

- Ebene radiale Familie wie KEGEL-Q (FV-Gitter, Newton bei festem omega^2), aber abwaerts geometrisch in
  eps = omega^2 - 1/2 (Faktor 0,96 je Schritt bis eps = 0,0065), damit Q' bis ~1,3e4 erreicht wird.
  Je Schritt drei Startwerte (Extrapolation, Vorgaenger, frische Duennwand); der mit dem kleinsten Rest zaehlt.
- Ziel-Ladungen Q' = s * 200 fuer s = 1,2; 1,5; 2; 3; 6; 12; 24; 48 (loese_Q aus kegel_q, erste Klammer mit
  dQ/domega^2 < 0, also stabiler Ast).
- B(s) = E_flach(200) - E_flach(sQ)/s; gamma = 1 + B/E_flach(200) (Karte, K0 = 0); v_Grund = sqrt(1 - 1/gamma^2).
  Beschreibend: gamma_alt = E/(E - B) (Ruhemasse am Grund) und der Grenzwert s -> unendlich, B_inf = E - omega_c Q.
- Laeufe: Haupt dr = 0,01, rmax = 90; Probe dr = 0,005 (rmax 90); Probe rmax = 120 (dr = 0,01).
- Kontrollen je s: dQ/domega^2 < 0, E/Q < 1, Rest des Newton, f^2 in den letzten 5 Einheiten vor rmax,
  rmax - R_half, dE/dQ = omega (numerisch, +-1e-3 Q') bei s = 1,2; 2; 6; 48.

## 2. Teil B (Netz n = 3, s = 2)

1. **Netz** kegel_q.Netz(3, h, R = 60), Startstrahl theta0 = 0 (Gitterrichtung), Gegenstrahl |phi| = Theta/2 = pi/2
   (Sektormitte, auch Gitterrichtung). Spiegelsymmetrisch; Stossparameter 0.
2. **Statik** (CPU): loese_ball (KEGEL-Q) bei Q = 200, h = 0,3, harmonischer Schwerpunkt W = d^2 fuer
   d = 0, 1, ..., 12, 14, 16, 25. B_gitter = E(25) - E(0); V(d) = E(d) - E(25). B_exakt(2) aus der radialen Familie.
3. **Zeitentwicklung** (P4000, float64) wie EINFANG-1: Stoermer-Verlet, Schwamm r_s = 45, g_max = 1, Start mit
   statischem Netzball (Q_lat = Q/gamma_v) bei d0 = 25 und Boost v0 = 0,01 zur Spitze, h = 0,3, dt = 0,1.
   Diagnose alle 0,5 Zeiteinheiten.
4. **Messgroessen der Geschwindigkeit** (alle in jedem Lauf aufgezeichnet):
   - **v_rms (Urteilsmass fuer L2 und L3):** Ladungsfluss J je Ecke (kleinste Quadrate aus den Kantenfluessen
     2 Im(conj phi_i phi_j); die Spitzenecke selbst ausgenommen), rho = Ladungsdichte, Ecken mit |phi|^2 > 0,01 und
     rho > 0: v_rms^2 = Sum A |J|^2/rho / Sum A rho.
   - v_mean = Sum A |J| / Sum A rho (beschreibend).
   - v_x: |dx/dt| des harmonischen Ladungsschwerpunkts von EINFANG-1 (beschreibend).
   - v_ax: |d xi_c/dt| des axialen Ladungsschwerpunkts auf der Spiegelachse (beschreibend).
   - v_fm: |d xi_m/dt| des Feldmaximums auf der Achse, Parabel durch die drei hoechsten Achsenpunkte (beschreibend).
   - Ableitungen: lokale Gerade ueber +-1 Zeiteinheit (5 Punkte).
   - **Begruendung der Wahl** (vor dem Einfrieren, nach Schreibtisch und Rauchlauf; siehe Abschnitt 7):
     - Fuer jeden starr bewegten Ball ist J/rho = v an jeder Ecke; v_rms ist dann genau die
       Schwerpunktgeschwindigkeit von EINFANG-1, ohne Koordinate. v_rms^2 ist das ladungsgewichtete Mittel von u^2 und
       damit die Groesse, die zur Bewegungsenergie gehoert (Vergleich mit der Energieerhaltung).
     - Der harmonische Schwerpunkt ist an der Spitze singulaer: W ist ungerade und glatt im Versatz delta, fuer eine
       starre Scheibe W ~ (4R/3 pi) delta, also x ~ sqrt(delta) und dx/dt -> unendlich beim Durchgang.
     - Der axiale Schwerpunkt springt, sobald die Ballfront die Spitze erreicht (die Ladung auf dem Gegenstrahl
       erscheint ploetzlich im 1D-Schnitt); das Feldmaximum springt auf dem flachen Ballkopf zwischen Spitze und
       Ballmitte (Rauchlauf).
5. **Durchgang** = Vorzeichenwechsel von xi_c nach dem Eintritt (xi_c > -R_c, R_c = 9,2551 wie EINFANG-1); Zeit linear
   interpoliert. Fenster des k-ten Durchgangs: von der Mitte zwischen Durchgang k-1 und k (k = 1: t = 0) bis zur Mitte
   zwischen Durchgang k und k+1 (letzter: Laufende).
6. **Stoppregel:** Laufende 80 Zeiteinheiten nach dem zweiten Durchgang, oder |xi_c| > 24 nach einem Durchgang
   (entkommen), oder T_max. Zustand nach 540 s Wandzeit sichern und fortsetzen (wie EINFANG-1).
7. **Energieerhaltung (L2):** v_ein = Steigung von x(t) fuer t >= 20, x <= -12, vor dem Eintritt (wie EINFANG-1);
   K0 = (gamma(v_ein) - 1) E_fern; gamma_E = 1 + (K0 + B_gitter)/E_fern; v_E = sqrt(1 - 1/gamma_E^2), E_fern und
   B_gitter aus der Statik desselben Netzes (n = 3, h = 0,3, R = 60).
8. **Netz traegt** (Entscheidung n = 3 oder n = 4, vor Teil B mechanisch):
   - Netzpruefung: Grad der Spitze 3, Defekt pi (auf 1e-9), Euler 1, alle anderen Innenecken Grad 6.
   - |B_gitter - B_exakt(2)| / B_exakt(2) < 1 % (h = 0,3).
   - Ruhender Kegelball auf der Spitze (T = 200): Drift von xi_c < 0,1 und relative Aenderung von E_ball < 1e-3.
   - Faellt eine Bedingung: Teil B mit n = 4 (s = 1,5), sonst gleich; offenlegen.

## 3. Laeufe

| Name | Rolle | Befehl | Parameter | Spur |
|---|---|---|---|---|
| radial-haupt | Teil A, L0, L1 | radial | dr 0,01, rmax 90, s = 1,2 ... 48 | cpu |
| radial-dr | Probe dr | radial | dr 0,005, rmax 90 | cpu |
| radial-rmax | Probe rmax | radial | dr 0,01, rmax 120 | cpu |
| statik-n3-h0.3 | B_gitter, V(d), Netz traegt | statik | n 3, h 0,3, R 60, d = 0..12, 14, 16, 25 | cpu |
| li-t3-v0.01 | L2, L3 (Haupt) | lauf | n 3, h 0,3, dt 0,1, v0 0,01, d0 25, T_max 3000 | p4000a |
| li-t3-ruhe | Kontrolle, Netz traegt | lauf | n 3, h 0,3, dt 0,1, v 0, d0 0, T 200, keine Stoppregel | p4000a |
| li-t3-v0.01-dt0.05 | Konvergenz dt | lauf | wie Haupt, dt 0,05 | p4000a |
| li-t3-v0.01-h0.2 | Konvergenz h | lauf | wie Haupt, h 0,2, dt 0,05 | p4000a |

- Falls "Netz traegt" scheitert: dieselben Laeufe mit n = 4 (statik-n4-h0.3, li-t4-...), L2/L3 dann an n = 4.

## 4. Urteile (mechanisch, vorab festgelegt; Vorhersagen woertlich aus der Karte)

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| L0 | Kontrolle: Die exakte Abbildung bei s = 1,2 trifft B = 1,4465 (KEGEL-Q, Q = 200) auf 0,2 % | 90 % |
| L1 | Grundgeschwindigkeit aus Teil A: n = 4: 0,15 bis 0,23; n = 3: 0,19 bis 0,29; n = 1: 0,26 bis 0,40; fuer alle s unter 0,45 | 75 % |
| L2 | Teil B: Die hoechste gemessene Schwerpunktgeschwindigkeit beim ersten Durchgang liegt innerhalb 15 % des Werts aus Energieerhaltung mit dem statischen B(s = 2) desselben Netzes | 70 % |
| L3 | Teil B: Beim zweiten Durchgang ist die Hoechstgeschwindigkeit kleiner als beim ersten (der Ball wird langsamer, nicht schneller) | 85 % |

- **L0:** eingetroffen, wenn |B(s = 1,2) - 1,4465| / 1,4465 < 0,002 (radial-haupt).
- **L1:** eingetroffen, wenn v_Grund(1,5) in [0,15; 0,23], v_Grund(2) in [0,19; 0,29], v_Grund(6) in [0,26; 0,40] und
  v_Grund < 0,45 fuer alle gerechneten s und den Grenzwert s -> unendlich (radial-haupt). Fehlt ein s: nicht
  entscheidbar.
- **L2:** eingetroffen, wenn |v_rms,max(1. Durchgang) / v_E - 1| < 0,15 (li-t3-v0.01). Konvergenzproben: weicht ihr
  Urteil nach derselben Regel ab, Vermerk "nicht konvergiert"; das Urteil bleibt.
- **L3:** eingetroffen, wenn v_rms,max(2. Durchgang) < v_rms,max(1. Durchgang) (li-t3-v0.01). Ohne zweiten Durchgang
  bis Laufende: nicht entscheidbar. Konvergenzvermerk wie L2.
- Fehlt ein Lauf bis 20:05 CEST: zugehoerige Vorhersage nicht entscheidbar. Bei n = 4 (Abschnitt 2.8) gelten L2/L3
  am n = 4-Netz mit B(s = 1,5) desselben Netzes.

## 5. Beschreibend (nicht gewertet)

- L2 und L3 mit den anderen Massen (v_mean, v_x, v_ax, v_fm, xi_S).
- Umkehrpunkte nach jedem Durchgang (max |x_S| zwischen den Durchgaengen, Koordinate wie KEGEL-Q) gegen V(d) der Statik:
  Verlust im ersten Durchgang K0 - V(d_1), im zweiten V(d_1) - V(d_2); relativ zu K0 + B_gitter.
- Atmung (S_max), abgestrahlte Energie (E_damp, Energie ausserhalb der Ballscheibe 15), Bild v(t) (lauf-69/v-t.png).
- Teil A: gamma_alt, Duennwand-Formel der Karte gegen exakt, R_half(sQ).

## 6. Kontrollen

- Energiebilanz max |E_tot + E_damp - E_tot(0)|, Ladungsbilanz, Spiegelsymmetrie max |Im W|.
- Far-Zone: v_rms gegen v_ein vor dem Eintritt (Eichung des Urteilsmasses).
- Ruhender Kegelball (li-t3-ruhe), Konvergenz dt und h, Teil-A-Proben dr und rmax.

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt; Parameter kommen in keinem echten Lauf vor)

- Spur cpu, 17:13:56 bis 17:14:22 UTC: Q = 150, n = 3, h = 0,5, R = 30, r_s = 22.
- radial (dr 0,02, rmax 60, eps_min 0,012, s = 1,2; 2; 12): Familie 113 Punkte, Rest <= 7,8e-12, Q_max 3782.
  B(1,2; Q = 150) = 1,2649, v(2) = 0,2585, v(12) = 0,3853, dE/dQ auf 5,5e-9.
- statik (d = 0, 3, 6, 9, 15): B_gitter(2) = 4,2074 gegen B_exakt 4,2183 (-0,26 %).
- lauf v0 = 0,05, d0 = 12, T bis 206 (Stoppregel griff nach 2 Durchgaengen): Durchgaenge bei t = 109,2 und 175,7.
  - v_rms zu Beginn 0,0498 (v0 = 0,05); v_rms,max = 0,227 (1. Durchgang) und 0,195 (2.).
  - v_E dieses Rauchlaufs (K0 = 0,1495, B = 4,2074, E = 119,885): 0,2625; v_rms/v_E - 1 = -0,13.
  - v_ax,max 0,385 (Spruenge), v_x,max 1,73 (Singularitaet), v_fm bis 5,8 (Spruenge); Bild rauch-69/rauch-t3.png.
  - Grosser Schwammverlust (E_damp 3,7 bis t = 200), weil der Schwamm bei r = 22 nahe an der Bahn lag.
- ruhender Kegelball (T = 40): Drift xi_c 1e-5, E_ball 9e-7 relativ, v_rms <= 5e-4.
- **Damit war die Tendenz von L2 und L3 vor dem Einfrieren sichtbar (Selbstanzeige).** Die Wahl von v_rms als
  Urteilsmass fiel nach diesem Rauchlauf.
