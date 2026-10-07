# EINFANG-1: Plan (Code-Agent fuer claude-primary, Runde 34)

- Geschrieben ab 2026-10-03 18:04:35 CEST (date). Wird vor der ersten echten Rechnung eingefroren:
  PLAN.md.eingefroren-<datum-uhrzeit>, code/einfang.py.eingefroren-<datum-uhrzeit>, code/laufplan.eingefroren-<...>.tar.
- Karte: KARTE.md (EF0 bis EF3 und ihre Bedeutung unveraendert).
- Code: code/einfang.py (neu) und code/kegel_q.py (unveraenderte Kopie von
  RUNDE-26/kegel-q/code/kegel_q.py.eingefroren-20261003-043140, sha256 4de64b080729204c...).
- Rechnen nur auf der .69 ueber kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde34-einfang/lauf/. Spuren p4000a und
  p4000b (CUDA, torch 2.5.1+cu121; im Rauchlauf 2,3 bis 2,6 ms je Schritt gegen 22 ms auf der CPU-Spur).

## 1. Modell und Methode

1. **Netz:** kegel_q.Netz(n, h, R) mit n = 5 (Fuenfer-Ecke), 6 (eben, Kontrolle), 7 (Siebener-Ecke). R = 60, Dirichlet
   phi = 0 auf den Randecken. Startstrahl theta0 = 0 (Sektorgrenze, Gitterrichtung). Gegenstrahl phi = +-Theta/2
   (bei n = 5, 7 Sektormitte, bei n = 6 Gitterrichtung). Das Netz ist spiegelsymmetrisch zu dieser Achse, ein Ball auf
   der Achse bleibt darauf (Stossparameter 0).
2. **Gleichung** (Normierung wie im statischen Funktional von KEGEL-Q):
   - A_i phi_i'' = -(L phi)_i - A_i U'(|phi_i|^2) phi_i - A_i gamma_i phi_i', U(S) = S - S^2 + S^3/2,
     (L phi)_i = Sum_j w_ij (phi_i - phi_j).
   - Energie E = Sum A |phi'|^2 + phi^H L phi + Sum A U(|phi|^2); Ladung Q = 2 Sum A Im(conj(phi') phi).
   - Der statische Netzball phi = f exp(-i omega t) ist damit exakt stationaer (Rauchlauf: Ort fest auf 1e-4 ueber
     t = 100, Ballladung auf 6e-8 relativ).
3. **Integrator:** Stoermer-Verlet (Kick-Drift-Kick), komplexes Feld als zwei reelle Komponenten, float64.
   - **CFL-Probe** (Rauchlauf, h = 0,3): dt = 0,2 stabil, dt = 0,25 instabil (nach t = 12).
   - Gewaehlt: dt = 0,1 bei h = 0,3 und dt = 0,05 bei h = 0,2.
   - Energieschwankung ohne Schwamm im Rauchlauf: 1e-4 (dt = 0,1) bzw. 1,7e-3 (dt = 0,2) bei E = 121.
4. **Schwamm:** gamma(r) = g_max ((r - r_s)/(R - r_s))^2 fuer r > r_s (geodaetischer Abstand zur Spitze), r_s = 45,
   g_max = 1. Exakter Faktor exp(-gamma dt/2) vor und nach jedem Schritt (Strang-Teilung).
   - Die entzogene Energie E_damp und Ladung Q_damp werden exakt aufsummiert.
   - Bilanz: E_tot(t) + E_damp(t) = E_tot(0) bis auf den Verlet-Fehler.
   - Der Ball (Mitte |x| <= 25, Schwanz) bleibt mindestens 14 vom Schwammbeginn weg.
5. **Start:**
   - Statischer Netzball mit Q_lat = Q/gamma_v (gamma_v = 1/sqrt(1 - v^2)) aus kegel_q.loese_ball, harmonischer
     Schwerpunkt W = d0^s auf dem Startstrahl, d0 = 25. Startprofil: radiales Kontinuumsprofil.
   - Boost (Netzfassung), Laufrichtung zur Spitze (u = -v entlang X = r cos phi):
     - phi(0) = f exp(-i omega gamma_v v (X - d0))
     - phi'(0) = [v d_X f - i omega gamma_v f] exp(...), d_X f aus dem radialen Kontinuumsprofil.
   - Damit ist die Laborladung exakt Q = 200. Die Lorentz-Kontraktion fehlt (Fehler O(v^2)); EF0 prueft den Lauf.
   - Rauchlauf v = 0,15, Q = 150: gemessen v = 0,1497.
6. **Diagnose** alle 2 Zeiteinheiten:
   - **Ort:** harmonischer Schwerpunkt W = Sum A rho w / Sum A rho mit w = r^s exp(i s phi), s = 6/n, phi gegen den
     Startstrahl.
     - Gewicht rho = Ladungsdichte auf den Ecken mit |phi|^2 > 0,01 (Hauptgroesse x).
     - Vergleich: |phi|^2 auf allen Ecken (x_S, Definition von KEGEL-Q).
     - Bahnkoordinate x = -Re W |W|^(1/s - 1): x = -25 am Start, x = 0 auf der Spitze, x > 0 auf dem Gegenstrahl.
       Exakt fuer runde Baelle, die die Spitze nicht ueberdecken; nahe der Spitze ist x eine Reaktionskoordinate.
   - **Energie und Ladung** im Ball: geodaetische Scheibe mit Radius 15 um den Ballort. Dazu E_tot, Q_tot, E_damp,
     Q_damp, max |phi|^2 und |phi|^2 an der Spitze.
7. **Ende eines Laufs:** bei T_max, oder sobald der Ball nach dem Austritt |x| > 24 erreicht.
   - Abschnitte: Nach 540 s Wandzeit wird der Zustand gespeichert und mit --fortsetzen weitergerechnet.

## 2. Parameter (fest)

- Q = 200 (KEGEL-Q: R_half = 6,2551, kappa = 0,667, B = +1,445 bzw. -1,336 bei h = 0,3). R_c = R_half + 3 = 9,2551.
- h = 0,3, dt = 0,1, R = 60, r_s = 45, g_max = 1, Schwellwert |phi|^2 > 0,01, Ballscheibe 15, d0 = 25.

## 3. Laeufe

| Name | Rolle | n | v | h | dt | T_max | Spur |
|---|---|---|---|---|---|---|---|
| f5-v0.02 | EF2 | 5 | 0,02 | 0,3 | 0,1 | 3200 | p4000a |
| f5-v0.05 | EF1 | 5 | 0,05 | 0,3 | 0,1 | 1200 | p4000b |
| f5-v0.1 | EF1 | 5 | 0,1 | 0,3 | 0,1 | 600 | p4000b |
| s7-v0.05 | EF3 | 7 | 0,05 | 0,3 | 0,1 | 1200 | p4000b |
| e6-v0.05 | EF0 | 6 | 0,05 | 0,3 | 0,1 | 1200 | p4000b |
| f5-v0.02-dt0.05 | Konvergenz (dt) | 5 | 0,02 | 0,3 | 0,05 | 3200 | p4000a |
| f5-v0.02-h0.2 | Konvergenz (h) | 5 | 0,02 | 0,2 | 0,05 | 3200 | p4000b |
| e6-v0 | Kontrolle: ruhender Ball | 6 | 0 | 0,3 | 0,1 | 300 | p4000a |
| e6-v0.05-ohne | Kontrolle: ohne Schwamm (g_max = 0) | 6 | 0,05 | 0,3 | 0,1 | 300 | p4000a |

- **Beschreibend** (nicht gewertet, nur wenn die Zeitbox reicht):
  - f5-v0.035 (n = 5, v = 0,035, d0 = 25, T_max = 2000)
  - f5-v0.01 (n = 5, v = 0,01, d0 = 16, T_max = 3200; bei d = 16 ist das statische Potential < 3e-7)

## 4. Begriffe und Urteile (mechanisch, vorab festgelegt)

- **Eintritt:** t_ein = erste Diagnosezeit mit x > -R_c.
- **Durchgang:** Vorzeichenwechsel von x nach t_ein.
- **Austritt:** t_aus = erste Diagnosezeit nach t_ein mit |x| > R_c.
- **Ausgang:**
  - "durchgelaufen": Austritt bei x > 0 nach genau einem Durchgang.
  - "zurueckgeworfen": Austritt bei x < 0 ohne Durchgang.
  - "nach k Durchgaengen ausgetreten": sonst, falls ein Austritt erfolgt.
  - **"eingefangen"** (Karte): kein Austritt bis Laufende, also |x| <= R_c von t_ein bis T_ende. Dazu mindestens zwei
    Durchgaenge oder T_ende - t_ein >= 4 R_c/v. Ein freier Ball braucht 2 R_c/v durch die Scheibe; "laengst
    draussen" heisst das Doppelte.
  - "offen (Lauf zu kurz)": kein Austritt, aber keine der beiden Bedingungen erfuellt.
- **Geschwindigkeiten:**
  - v_ein: Steigung von x(t) ueber alle Diagnosepunkte mit t >= 20, x <= -12 und t < t_ein.
  - v_aus: Steigung von |x|(t) ueber alle Punkte nach t_aus mit |x| >= 12. Bei |x| >= 12 ist der Rest des statischen
    Potentials < 2e-4.
- **Verlust je Durchgang:**
  - Delta K = K_ein - K_aus mit K = (gamma(v) - 1) E_rest(Q_ball) und E_rest(Q) = E_lat + omega (Q - 200).
  - Q_ball und E_ball sind Mittel ueber das jeweilige Geschwindigkeitsfenster.
  - Dazu Delta E_ball, Delta Q_ball, abgestrahlte Energie (E_damp + E ausserhalb der Ballscheibe) und innere Anregung
    E_ball - E_rest(Q_ball) - K.
- **EF0** (e6-v0.05): eingetroffen, wenn |v(350..450)/v(20..120) - 1| < 0,05 und |Q_ball(400)/Q_ball(0) - 1| < 0,01.
  - v(a..b) ist die Steigung von x(t) ueber die Diagnosepunkte in [a, b]; Q_ball(400) am naechsten Diagnosepunkt.
- **EF1:** eingetroffen, wenn f5-v0.1 und f5-v0.05 beide austreten und keiner "eingefangen" ist.
- **EF2:** eingetroffen, wenn f5-v0.02 den Ausgang "eingefangen" hat. Nicht eingetroffen bei jedem Austritt. Bei
  "offen" ist EF2 nicht entscheidbar.
  - Konvergenzproben f5-v0.02-dt0.05 und f5-v0.02-h0.2: Weicht ein Ausgang ab, erhaelt das Urteil den Vermerk "nicht
    konvergiert". Das Urteil selbst bleibt.
- **EF3:** eingetroffen, wenn s7-v0.05 den Ausgang "zurueckgeworfen" hat (x bleibt < 0, Austritt bei x < -R_c).
- Abgebrochene Laeufe zaehlen mit den Diagnosepunkten, die sie geschrieben haben. Fehlt ein Lauf bis 19:35 CEST, ist
  die zugehoerige Vorhersage "nicht entscheidbar".

## 5. Beschreibend (nicht gewertet)

- Verlust je Durchgang gegen v (Delta K absolut und relativ zu K, Delta E_ball, Delta Q_ball, abgestrahlte Energie).
- Umkehrpunkt gegen das statische Potential V(d) = E(d) - E_flach aus KEGEL-Q (h = 0,3, Q = 200, Koordinate x_S):
  - Siebener-Ecke: V(d_umkehr) gegen K_ein.
  - Fuenfer-Ecke (falls eine Umkehr nach dem ersten Durchgang): Verlust im ersten Durchgang = K_ein - V(d_umkehr).
- Atmung (max |phi|^2 gegen t), Ladungsverlust, Bild der Bahnen x(t) (lauf-69/bahnen.png).

## 6. Kontrollen

- **Ruhender Ball** (e6-v0, Q = 200): Drift von x, relative Aenderung von E_ball und Q_ball ueber t = 300.
- **Ohne Schwamm** (e6-v0.05-ohne): |E_tot(t) - E_tot(0)| und |Q_tot(t) - Q_tot(0)|.
- **In jedem Lauf:** Bilanz max |E_tot + E_damp - E_tot(0)| und max |Q_tot + Q_damp - Q_tot(0)|; EF0 als Laufkontrolle.
- **Konvergenzproben:** dt = 0,05 und h = 0,2 fuer den Lauf f5-v0.02.
- **Netzpruefung** je Lauf (aus kegel_q: Grade, Defekt, Euler).

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt; Parameter kommen in keinem echten Lauf vor)

- **rauch-gpu-ruhend / rauch-cpu-ruhend:** n = 6, h = 0,35, Q = 150, v = 0, T = 100 bzw. 30.
  - Ball stationaer: x = -25,0001 fest; Q_ball 149,99987 -> 149,99988.
  - E_damp 9e-6 aus der Startabweichung durch den Zeitschritt.
  - 2,48 ms je Schritt (P4000) gegen 22,3 ms (CPU-Spur).
- **rauch-boost:** n = 6, h = 0,35, Q = 150, v = 0,15, T = 160.
  - x(t) linear, v = 0,1497 (Soll 0,15).
  - E_ball konstant auf 7e-4, Q_ball -5e-4, E_damp 7e-4.
  - **Damit war die Tendenz von EF0 vor dem Einfrieren sichtbar (Selbstanzeige).**
- **rauch-cfl01 / -cfl02 / -cfl025:** n = 6, h = 0,3, Q = 150, v = 0,15, ohne Schwamm, T = 60.
  - dt = 0,1 und 0,2 stabil, dt = 0,25 instabil.
  - Energieschwankung 1e-4 bzw. 1,7e-3; Q_tot konstant auf 1e-12.
- **Auswertung und Bild auf den Rauchdaten** (Pipeline-Probe, Spur cpu):
  - rauch-boost ergibt "offen (Lauf zu kurz)", v_ein = 0,14967.
  - Der ruhende Ball atmet mit 0,1 % in max |phi|^2. Ursache ist die Startabweichung durch den Zeitschritt,
    (omega dt)^2/8 ~ 7e-4.
