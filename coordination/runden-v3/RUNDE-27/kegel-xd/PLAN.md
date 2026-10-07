# KEGEL-XD: Plan (Code-Agent fuer claude-primary, Runde 27)

- Geschrieben ab 2026-10-03 06:02 CEST (date 06:01:59 beim Start dieses Abschnitts). Wird vor der ersten echten Rechnung
  eingefroren (PLAN.md.eingefroren-<datum-uhrzeit>, dazu code/kegel_xd.py.eingefroren-<datum-uhrzeit>).
- Karte: KARTE.md (Schreibtisch, KX0 bis KX3 und Bedeutung unveraendert). Code: code/kegel_xd.py.
- Rechnen nur auf der .69 ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6), Ordner
  /home/fmh/fmhc-physics-remote/runde27-kegel-xd/lauf/. Ergebnisse per rsync nach lauf-69/.

## 0. Schreibtischpruefung der Herleitung (Code-Agent, vor jeder Rechnung)

- Huellensatz: dE/da bei festem Q = dF/da bei festem omega; mit dV = a r dr dtheta (dz) und
  |grad f|^2 = f_r^2 + f_th^2/(a^2 r^2) (+ f_z^2) folgt dF/da = Int (f_r^2 (+ f_z^2) - |grad_th f|^2 + V) r dr dth (dz),
  also Delta E = (delta/2pi) Int T_thth dV bei a = 1 - delta/2pi. Nachgerechnet, stimmt mit der Karte.
- Erhaltung: T_ij = 2 d_i f d_j f - delta_ij (|grad f|^2 + V), d_i T_ij = (2 Lap f - V') d_j f = 0. Die theta-Komponente
  in Zylinderkoordinaten gibt die Formel der Karte; J(theta) ist strahlunabhaengig, weil r^2 T_rth bei r = 0 und r -> inf
  verschwindet (flaches Profil ist glatt). Nachgerechnet.
- Strahl vom Ball weg: grad f liegt in der Ebene (Strahl, z), daher T_thth = -g. Die Formeln 2D/3D stimmen.
- Probe "Strahl durch das Zentrum": Differenz 2 d Int_0^inf g drho; Int g drho = 0 folgt aus dem Kraftgleichgewicht
  einer Ballhaelfte (T_xx auf der Symmetrielinie). In 3D lautet die Probe Int_0^inf rho g drho = 0 (Ebene). Beide
  Integrale werden als Kontrolle berichtet.
- d = 0 und Derrick (2D: V_ges = 0; 3D: G + 3 V_ges = 0) geben -(delta/2pi)(E - omega Q), die erste Ordnung von
  E_flach(sQ)/s. Nachgerechnet.
- Rechenform: 2D Delta E_1(d) = -delta Int_d^inf (rho - d) g drho; 3D (Polarkoordinaten in der Halbebene x > d)
  Delta E_1(d) = -delta Int_d^inf 2 rho [sqrt(rho^2 - d^2) - d arccos(d/rho)] g(rho) drho. Diskret mit f'^2 an den
  FV-Flaechen und V an den Zellmitten (bei d = 0 exakt -(delta/2pi) F_diskret).
- Erwartete Groessenordnung der Terme hoeherer Ordnung: relativ (delta/2pi)^2 mal O(1), also ~3 % in 2D (delta = pi/3)
  und ~4e-4 in 3D. Ich habe keine Herleitungsfehler gefunden; Urteil darueber geben nur die Rechnungen.

## 1. Teil A (2D, nur Auswertung; Befehl teil_a)

- Eingabe: KEGEL-Q-Laeufe lauf-69/kraft-n5-h0.2-Q200-a/b.json, kraft-n7-h0.2-Q200-a/b.json (17 Abstaende 0 bis 19,2),
  bind-n6-h0.2-Q200.json (E_flach). Kopie nach /home/fmh/fmhc-physics-remote/runde27-kegel-xd/eingabe-kegel-q/,
  sha256 im Ergebnis. Energie je Punkt E_korr_erste_ordnung (wie KEGEL-Q).
- O(d) = [E_5(d) - E_7(d)]/2, P(d) = [E_5(d) + E_7(d)]/2 - E_flach.
- Ebenes Radialprofil: dieselbe radiale Familie wie KEGEL-Q (dr = 0,01, r_max = 60, Start omega^2 = 0,62), Q = 200;
  Probe dr = 0,005. Delta E_1(d) fuer delta = pi/3 nach Abschnitt 0.
- Schwanz: T_2(d) = -(delta/2) f^2(d) mit dem ebenen Profil (nicht f^2 an der Spitze aus dem Gitter; das wird nur
  berichtet).

## 2. Teil B (3D)

### 2.1 Ball und Zielwerte (Befehl ziel, vor allen 3D-Laeufen, danach versiegelt)

- M1, beta = 1/2, 3D, FV-Radialgitter dr = 0,01, r_max = 60 (Probe dr = 0,005 bei gleichem Q).
- **omega festgelegt durch R_halb(S = 1/2) = 5,00** (brentq in der Familie ab omega^2 = 0,64); Q = Q(omega) fest fuer
  alle 3D-Laeufe. Aus dem Rauchlauf (dr = 0,02, R_halb = 4) erwartet: omega^2 ~ 0,65, kappa ~ 0,59, Q ~ 1000.
- Zielwerte in lauf/ziel-3d.json, danach chmod a-w (auf der .69 und lokal): Delta E_1(d), Kraft d(Delta E_1)/dd,
  Schwanz T_3(d) = -(delta/2) Int f^2(sqrt(d^2 + z^2)) dz, exakte Keilabbildung E_flach(sQ)/s - E_flach(Q) fuer +-delta.
- **Abstaende:**
  - Karte: d = 0, 3, 5, 7, 9 (R_halb = 5).
  - **Zusatz fuer KX3 [A]:** Die Kartenliste hat in 3D keinen Punkt mit d >= R_halb + 3/kappa (~10,1, da 3/kappa > 4).
    Deshalb zwei Zusatzpunkte d_a = kleinstes Vielfaches von 0,25 ab R_halb + 3/kappa, d_b = d_a + 1 (erwartet 10,25
    und 11,25). Sie zaehlen nur fuer KX3, nicht fuer KX2.
- delta = +0,1284 und -0,1284 (s = 2pi/(2pi -+ delta)).

### 2.2 Gitter und Loeser (Befehl ball3d)

- Zylinderkoordinaten (r, phi, z), Zellmitten r_j = (j + 1/2) h, phi_k = (k + 1/2) dphi, z_l = (l + 1/2) h.
  Viertelgebiet phi in [0, Theta/2], z >= 0 (Spiegel theta -> -theta und z -> -z, Neumann), Faktor 4 in allen Gewichten.
  Dirichlet f = 0 hinter r_max und z_max (Geisterzelle). FV-Gewichte: Volumen r h dphi h, Flaechen wie im Code.
- Ball bei festem Q; E = Q^2/(4 Sum w f^2) + G + V; reelles f (Vorzeichen frei, Startprofil positiv).
- **Lagebedingung (wie KEGEL-Q):** harmonischer Schwerpunkt W = <r^s cos(s phi)>_{f^2 dV} = d^s, s = 2pi/Theta.
  r^s cos(s phi) ist auch in 3D harmonisch (unabhaengig von z), daher W = d^s exakt fuer einen kugelsymmetrischen
  Ball, der die Kante nicht ueberdeckt. Augmented Lagrangian mu = 5, hoechstens 8 Aussenschritte, Ziel |c| < 1e-9.
  Ausgewertet E_korr = E + m c (erste Ordnung im Nebenbedingungsrest).
- **d = 0:** achsensymmetrische (r, z)-Rechnung (nphi = 1, ohne Nebenbedingung), Startprofil = ebenes Profil zu sQ.
  Diskret gilt dann E_Keil(Q) = E_rz(sQ)/s exakt; KX0 prueft das (r, z)-Gitter gegen den Radialloeser.
- **Loeser:** L-BFGS-B (scipy, maxcor 12, ftol 1e-16, gtol 1e-12) in den Variablen y mit
  f = w^(-1/2) IDCT_phi(D y): DCT-II in phi (Neumann an beiden Spiegeln) und D = (1 + mu_m/(r dphi)^2 / (4/h^2))^(-1/2)
  daempft die steife phi-Kopplung an der Achse. Das aendert nur den Weg, nicht das Minimum.
- **Gitterweiten [A]:** fein h = 0,25, grob h = 0,35 (Verhaeltnis 1,4).
  - phi: gleiche physikalische Weite fuer +delta und -delta: nphi = 24 k (+delta) bzw. 25 k (-delta), flach 24,5 k;
    fein k = 8 (192 / 200 / 196, dphi = 0,016028 bis 0,016029, Unterschied 5e-5 relativ), grob k = 6
    (144 / 150 / 147, dphi = 0,021371). r dphi <= h bis r = 15,6 (fein) bzw. 16,4 (grob), also ueber den Ball.
- **Gebiet [A]:** r_max = d + 15, z_max = 15 (Abstand 10 = 5,9/kappa von der Halbwertsflaeche; Feldquadrat am Rand
  ~ e^{-2 kappa 10} ~ 7e-6 der Wanddichte). Randprobe (grob, d = 5 und d_a, +-delta): r_max = d + 19, z_max = 19.
- **Laufzeit:** Rauchlauf (h = 0,3, 423 000 Zellen, d = 4) 464 Funktionsaufrufe in 55 s. Fein bis 1,26 Mio. Zellen,
  erwartet 150 bis 250 s je Loesung. Ein feiner Lauf je kleintest-Aufruf, grobe Laeufe gebuendelt. tmax = 560 s im Skript:
  danach wird der beste Stand mit abgebrochen = true geschrieben. Nie die 600-s-Grenze dehnen.
- Ein Thread (OMP/OPENBLAS/MKL = 1).

### 2.3 Laeufe

| Rolle | delta | h | nphi | d |
|---|---|---|---|---|
| null | +, -, 0 | 0,25 und 0,35 | 1 | 0 |
| haupt | +0,1284, -0,1284 | 0,25 | 192 / 200 | 3, 5, 7, 9, d_a, d_b (je ein Lauf) |
| haupt | +0,1284, -0,1284 | 0,35 | 144 / 150 | 3, 5, 7 und 9, d_a, d_b (gebuendelt) |
| flach | 0 | 0,25 / 0,35 | 196 / 147 | alle d > 0 (nur fuer P(d) und Ortsabhaengigkeit) |
| rand | +-0,1284 | 0,35 | 144 / 150 | 5, d_a mit r_max = d + 19, z_max = 19 |

- Vorrang: null, haupt fein, haupt grob, rand, flach.

## 3. Urteile (mechanisch, vorab festgelegt; urteile.json)

- **KX0:** h = 0,25, d = 0: Delta E(+delta) = E_keil(+delta) - E_flach (beide (r, z)-Gitter) gegen
  E_flach(sQ)/s - E_flach(Q) aus dem Radialloeser (dr = 0,01). Eingetroffen, wenn die Abweichung <= 3 % des exakten
  Werts ist. (-delta nur berichten.)
- **KX1:** Teil A: |O(d) - Delta E_1(d)| <= 0,03 |Delta E_1(0)| fuer alle 17 d (h = 0,2, Profil dr = 0,01).
- **KX2:** h = 0,25: |O(d) - Delta E_1(d)| <= 0,05 |Delta E_1(0)| fuer alle fuenf Karten-d (0, 3, 5, 7, 9). Fehlt ein
  Punkt (Lauf fehlt), lautet das Urteil "nicht entscheidbar". Ein abgebrochener Lauf (tmax) zaehlt mit seinem besten
  Stand und wird gekennzeichnet.
- **KX3:** beide Dimensionen muessen erfuellen:
  - 2D: alle d der KEGEL-Q-Tabelle mit d >= R_halb + 3/kappa (R_halb bei S = 1/2 des ebenen Profils; dieselbe
    Punktmenge 10,8 bis 19,2 wie mit R_half(S0/2) der KEGEL-Q), mindestens zwei Punkte.
  - 3D: d_a und d_b (h = 0,25).
  - Je Punkt |O(d) - T(d)| <= 0,25 |T(d)|.
- **Bedeutung:** nach der Karte (KX1 und KX2 eingetroffen; KX1 nicht, KX0 schon; KX2 nicht, KX1 schon). Faellt ein
  Urteil in keinen der Faelle der Karte, beschreibe ich es ohne neue Lesart.

## 4. Beschreibend (nicht gewertet)

- P(d) in 2D und 3D; Richardson O(h -> 0) aus 0,35 und 0,25 (Ansatz h^2).
- Groesse der Terme hoeherer Ordnung: O(d) - Delta E_1(d) relativ zu |Delta E_1(0)| je d; in 2D zusaetzlich gegen
  (delta/2pi)^2.
- Exakte erste Ordnung gegen Schwanzformel (Delta E_1/T) je d.
- Kraefte: Multiplikator-Kraft (ungerader Teil) gegen d(Delta E_1)/dd.
- -delta-Gegenstueck zu KX0.

## 5. Kontrollen

- Impulsfluss-Proben (2D: Int g drho, 3D: Int rho g drho) relativ zu Int |g|.
- dr-Probe der Zielwerte (0,01 gegen 0,005); Derrick-Rest im 3D-Radialloeser.
- Je Punkt: Restgradient (Feldgleichung mit Multiplikator), Nebenbedingungsrest c, d_W, Feld am Rand, abgebrochen.
- Randprobe (Abschnitt 2.2), zwei Gitterweiten, flache Laeufe an allen d (Ortsabhaengigkeit des Zylindergitters).

## 6. Rauchlaeufe vor dem Einfrieren (offengelegt) und Selbstanzeigen

- ziel mit delta = 0,2, R_halb = 4, dr = 0,02 (omega^2 = 0,6839, Q = 582,9, kappa = 0,562). Daraus R_halb(omega^2) der
  Familie, die Wahl der KX3-Zusatzregel und der Gebietsgroesse.
- ball3d mit delta = +-0,2 und 0, Q = 582,9, h = 0,3 / 0,25: (r, z)-Rechnung d = 0 (Keilabbildung: Delta E(+0,2) =
  -1,2096 gegen exakt -1,2113, also -0,14 %), d = 4 bei +0,2 (Konvergenz, 464 Aufrufe, 55 s), -0,2 und eine feine
  Zeitprobe. Mit der Formel der Karte habe ich die Rauchlaeufe bei d > 0 nicht verglichen.
- **Selbstanzeige:** Auf der .69 lief um 05:51 CEST ein `python3 -c "import scipy, numpy"` ausserhalb der Spur
  (Versionspruefung, System-Python, scheiterte am Import). Es wurde nichts gerechnet. Ausserdem einmal `awk 'NR%6==1'`
  auf der .69 als Zeilenfilter fuer eine Ausgabe (keine Rechnung).
