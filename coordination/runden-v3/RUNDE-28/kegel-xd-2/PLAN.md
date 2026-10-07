# KEGEL-XD-2: Plan (Code-Agent fuer claude-primary, Runde 28)

- Geschrieben ab 2026-10-03 06:44 CEST (date 06:44:01 beim Start dieses Abschnitts). Wird vor der ersten echten Rechnung
  eingefroren (PLAN.md.eingefroren-<datum-uhrzeit>, dazu code/kegel_xd2.py.eingefroren-<datum-uhrzeit> und
  code/laufplan.<datum-uhrzeit>.tar mit den Spurskripten).
- Karte: KARTE.md (Schreibtisch, K2-0 bis K2-2 und Bedeutung unveraendert). Code: code/kegel_xd2.py.
- Rechnen nur auf der .69 ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6; nicht cpu5, keine GPU), Ordner
  /home/fmh/fmhc-physics-remote/runde28-kegel-xd-2/lauf/. Ergebnisse per rsync nach lauf-69/.

## 0. Schreibtisch (Code-Agent)

- Die Herleitung ist in KEGEL-XD (PLAN Abschnitt 0) nachgerechnet; hier nichts Neues.
- Zur Lage d [A]: Die Definition von d (harmonischer Schwerpunkt mit s = 2 pi/Theta) ist glatt in delta. Sie verschiebt
  den ungeraden Teil erst in Ordnung delta^3 (Lageverschiebung O(delta) mal Kraft O(delta^2) des geraden Teils), also
  in der Ordnung, die r misst. Weil sie fuer alle delta dieselbe ist wie in KEGEL-Q, bleibt unter Lesart (A) r ~ delta^2;
  K2-0 vergleicht ohnehin dieselbe Definition.
- Erwartete Gitterfehler: Die Abweichung bei delta = pi/12 soll unter (A) ~9e-4 absolut sein (0,26 % von
  |Delta E_1(0)| ~ 0,35). Der Gitterfehler von O muss deutlich darunter liegen; Kontrolle ueber zwei Gitter und
  Richardson (Abschnitt 4).

## 1. Zielwerte (Befehl ziel, nach dem Einfrieren und vor allen Kegel-Laeufen, danach versiegelt)

- Ebenes M1-Radialprofil (beta = 1/2), Q = 200, dieselbe Familie wie KEGEL-Q/KEGEL-XD Teil A (dr = 0,01, r_max = 60,
  Start omega^2 = 0,62); Probe dr = 0,005.
- Delta E_1(d; delta) = -delta Int_d^inf (rho - d) g drho fuer delta = pi/3, pi/6, pi/12 an den 17 Abstaenden
  0; 1,2; ...; 19,2 (fuer -delta das Negative). Dazu Kraft d(Delta E_1)/dd, Schwanzformel -(delta/2) f^2(d) und die
  exakte Kegelabbildung E_eben(sQ)/s - E_eben(Q) fuer alle sechs Defizite (d = 0).
- Datei lauf/ziel-2d.json, danach chmod a-w auf der .69 und lokal (lauf-69/ziel-2d.json). Zielwerte nie als
  Befehlszeilen-Argumente; die Auswertung liest die Datei.

## 2. Gitter und Loeser (Befehl ball2d)

- **Polarkoordinaten** (r, phi), Zellmitten r_j = (j + 1/2) dr, phi_l = (l + 1/2) dphi, Halbgebiet phi in [0, Theta/2]
  mit Spiegeln (Neumann) bei phi = 0 und phi = Theta/2, Faktor 2 in allen Gewichten. Theta = 2 pi - delta,
  delta = k pi/12 mit k = +-4 (pi/3), +-2 (pi/6), +-1 (pi/12) und k = 0 (flach).
- **FV-Gewichte:** Volumen 2 r_j dr dphi; radiale Flaechen 2 r_(j+1/2) dphi/dr; Winkelflaechen 2 dr/(r_j dphi).
  Dirichlet f = 0 in der Geisterzelle hinter r_max (wie KEGEL-XD).
- **Gleiche Winkelweite [A]:** dphi = pi/(24 m) fuer jedes k, Zellzahl im Halbgebiet Np = (24 - k) m. Damit ist die
  Winkelweite fuer +delta, -delta und flach exakt gleich (nicht nur fast, wie in KEGEL-XD). Alle Kegelgitter sind
  dasselbe Polargitter; sie unterscheiden sich nur darin, wo der hintere Spiegel liegt. Gitterfehler am Ball heben sich
  im ungeraden Teil daher bis auf Anteile der Ordnung delta heraus.
- **Zwei Gitter (Verhaeltnis 1,6 in dr und dphi):**
  - fein: dr = 0,1, m = 16 (dphi = pi/384 = 0,00818); Np = 320 / 352 / 368 / 384 / 400 / 416 / 448 fuer
    k = 4 / 2 / 1 / 0 / -1 / -2 / -4; bis 179 200 Zellen.
  - grob: dr = 0,16, m = 10 (dphi = pi/240 = 0,01309); bis 70 000 Zellen.
- **Winkelaufloesung am Ball:** Die Zellbreite r dphi waechst mit r. Fein: 0,12 an der Ballwand fuer d <= 8,4
  (r <= 14,7, dort liegt die Wandzone mit der groessten Abweichung), 0,157 im Ballzentrum bei d = 19,2 und 0,209 an
  dessen aeusserer Wand (r = 25,5). Das ist feiner als bzw. vergleichbar mit KEGEL-Q (h = 0,2). Grob 1,6-fach.
  Radial ist dr = 0,1 (fein) ueberall.
- **Gebiet:** r_max = 40 wie die KEGEL-Q-Scheibe (R = 40), fuer alle d. Randprobe mit r_max = 48 (Abschnitt 3).
- **Ball:** M1, Q = 200, E = Q^2/(4 Sum w f^2) + G + V; reelles f, Startprofil = ebenes Profil (dr = 0,01) um den Zielort
  im geodaetischen Abstand; bei d = 0 das ebene Profil zur Ladung sQ.
- **Lage d (wie KEGEL-Q/KEGEL-XD):** W = <r^s cos(s phi)>_{f^2 dA} = d^s, s = 2 pi/Theta, auch bei d = 0 (W = 0).
  Augmented Lagrangian mu = 5, hoechstens 8 Aussenschritte, Ziel |c| < 1e-9; ausgewertet E_korr = E + m c.
  Kraft aus dem Multiplikator dE/dd = -m (N/N0) s d^(s-1).
- **Loeser:** L-BFGS-B (maxcor 12, ftol 1e-16, gtol 1e-12) in den Variablen y mit f = w^(-1/2) IDCT_phi(D y), DCT-II in
  phi (Neumann an beiden Spiegeln), D = (1 + mu_m/(r dphi)^2/(4/dr^2))^(-1/2) wie KEGEL-XD. Ein Thread.
- **Laufzeit (Rauchlaeufe, Abschnitt 6):** fein ~50 s je Punkt in der Wandzone, 15 bis 20 s weit draussen, 5 s bei d = 0;
  grob 2 bis 14 s je Punkt. Daher fein drei Teillaeufe je k, grob ein Lauf je k. tmax = 560 s im Skript: danach wird der
  beste Stand mit abgebrochen = true geschrieben; die restlichen d des Laufs fehlen dann.

## 3. Laeufe (Spurskripte code/laufplan/spur-*.sh)

| Rolle | k | Gitter | d | Name |
|---|---|---|---|---|
| haupt | +-4, +-2, +-1 | fein | a: 0; 1,2; 2,4; 3,6 / b: 4,8; 6,0; 7,2; 8,4 / c: 9,6 bis 19,2 | b2-f-pK-a/b/c, b2-f-mK-a/b/c |
| haupt | +-4, +-2, +-1 | grob | alle 17 | b2-g-pK, b2-g-mK |
| flach | 0 | fein und grob | alle 17 (wie oben geteilt) | b2-f-00-a/b/c, b2-g-00 |
| rand | +-4, +-1 | grob, r_max = 48 | 7,2; 19,2 | b2-r-pK, b2-r-mK |

- Vorrang: fein +-4, +-2, +-1; dann grob; dann flach; dann rand. Verteilung auf fuenf Spuren nach geschaetzter Dauer
  (Listen in den Spurskripten). Fehlt danach ein Punkt (abgebrochen), wird nur dieser Teillauf einmal wiederholt.
- Danach Befehl auswertung (eine kleintest-Rechnung).

## 4. Urteile (mechanisch, vorab festgelegt; urteile.json)

- Definitionen: O(d; delta) = [E(+delta, d) - E(-delta, d)]/2 aus E_korr; r(d; delta) = [O - Delta E_1(d; delta)] /
  |Delta E_1(0; delta)| mit Delta E_1 aus ziel-2d.json (dr = 0,01).
- **K2-0:** feines Gitter, delta = pi/3: |O(d) - O_KQ(d)| <= 0,003 |Delta E_1(0; pi/3)| an allen 17 d. O_KQ =
  [E_5 - E_7]/2 aus den KEGEL-Q-Laeufen kraft-n5/n7-h0.2-Q200-a/b (E_korr_erste_ordnung), Kopie in
  eingabe-kegel-q/ (sha256 wie in KEGEL-XD).
- **K2-1:** feines Gitter, delta = pi/6: 0,006 <= max_d |r| <= 0,016 ueber die 17 d.
- **K2-2:** feines Gitter, delta = pi/12: 0,0015 <= max_d |r| <= 0,0045 und 3 <= max|r(pi/6)|/max|r(pi/12)| <= 5,5.
- Fehlt ein Punkt, lautet das Urteil "nicht entscheidbar". Ein abgebrochener Punkt zaehlt mit seinem besten Stand und
  wird gekennzeichnet.
- **Bedeutung** nach der Karte, mechanisch zugeordnet: K2-1 und K2-2 eingetroffen -> Fall (A); max|r(pi/12)| > 2 % ->
  Fall (B); sonst "dazwischen", beschreiben ohne nachtraegliche Bereiche.

## 5. Beschreibend (nicht gewertet)

- Tabelle r(d; delta) fuer alle drei delta (fein, grob, Richardson mit Ansatz h^2, Faktor 1,6^2 = 2,56).
- Skalierung je d: r(pi/3)/r(pi/6) und r(pi/6)/r(pi/12) (unter (A) je ~4) und r/(3 delta/pi)^2.
- Gerader Teil P(d; delta) = [E(+delta) + E(-delta)]/2 - E_flach(d), E_flach aus dem flachen Lauf am selben d und Gitter.
- r(pi/3) des Kontinuumscodes gegen r aus den KEGEL-Q-Daten (KEGEL-XD Teil A).
- Ungerader Teil der Multiplikator-Kraft gegen d(Delta E_1)/dd.

## 6. Kontrollen

- d = 0: Delta E(k) = E(k, 0) - E(0, 0) gegen die exakte Kegelabbildung (alle sechs k, beide Gitter); exakter Wert
  r(0; delta) aus der Radialfamilie.
- Flache Laeufe: Spanne von E_flach(d) ueber die 17 d (Scheinkraft des Polargitters; gerade in delta, faellt aus O).
- Randprobe r_max = 48 gegen 40 (grob, k = +-4 und +-1, d = 7,2 und 19,2): Aenderung von O.
- Zwei Gitter; dr-Probe der Zielwerte (0,01 gegen 0,005); Impulsfluss-Probe Int g drho = 0.
- Je Punkt: Restgradient, Nebenbedingungsrest c, d_W, Feld am Rand, abgebrochen, Funktionsaufrufe, Dauer.

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt) und Selbstanzeigen

- Ausserhalb der echten Parameter: delta = +-pi/4 (k = +-3) und flach, Q = 150, 04:40 bis 04:42 UTC, je <= 52 s:
  - fein k = -3, d = 6: 51 s, 1072 Aufrufe, Restgradient 8e-7, c = -6e-9
  - fein k = +3, d = 6 und 0: 39 s und 5 s; Restgradient 4,8e-4 bei d = 6 (vermutlich in den kleinen Zellen an der
    Spitze; E_korr ueber die Aussenschritte 3 bis 7 auf 1e-11 gleich)
  - grob k = -3, d = 0, 6, 12: 2 s, 14 s, 6 s
  - fein flach, d = 18: 14 s; Multiplikator 1,5e-4 (Scheinkraft des Polargitters)
- Mit der Formel der Karte habe ich die Rauchlaeufe nicht verglichen; aus ihnen stammen nur Laufzeiten und Konvergenz.
- Code der Rauchlaeufe: kegel_xd2_rauch1.py auf der .69 (gleich dem einzufrierenden Code).
- **Selbstanzeige:** Beim ersten Start der Rauchlaeufe gingen drei Aufrufe wegen eines Shell-Fehlers (Variablen in einer
  &&-Kette im Hintergrund) nicht los; sie wurden eine Minute spaeter neu gestartet. Keine Rechnung ausserhalb der Spur.
