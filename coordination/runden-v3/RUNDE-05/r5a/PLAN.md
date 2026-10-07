# Runde 5, Paket R5-A: Laufplan fuer sechs Q-Ball-Ideen in 3D-Radialsymmetrie

Bearbeiter: Agent R5-A (Anthropic, Opus), Auftrag ../AUFTRAG-R5.md. Beginn 2026-09-30 01:43:40 CEST (gemessen), Ende in
der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ.

## Kurzfassung

- **Code:** r5a.py, ein Unterbefehl je Idee plus Rauchtest. PyTorch, float64 bzw. complex128, `--geraet cuda` oder
  `--geraet cpu`. Torch-Speicher auf der Karte hoechstens 1,5 GB; gebraucht werden unter 0,1 GB.
- **Eingabe:** eingabe/tests1d_ergebnis_runde2.json ist eine unveraenderte Kopie von
  RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_ergebnis.json (Q(omega)-Tabelle; nur fuer `fitness`).
- **Aus tests1d.py (Test 4) unveraendert:** Taylor-Form um f_top, RK4 in u = f_top - f, h = 0,05 bis r = 150,
  Einschachteln in s = -ln(f_top - f(0)) mit 1024 Kandidaten x 4 Runden, Schwanz ab |f| < 1e-3 f(0), Integrale.
- **Erweitert:**
  - h als Argument (fuer L3: h/2)
  - Knotenzahl n: Ueberschuss = mehr als n Nulldurchgaenge; Unterschuss = die Bahn kehrt vor dem naechsten
    Nulldurchgang um. Fuer n = 0 ist das woertlich die Regel von tests1d.
- **Neu:** radiale Zeitentwicklung mit chi = r psi.
  - chi_tt = chi_rr - U'(|chi/r|^2) chi, chi(0) = 0
  - Verlet-Schritt, dr = 0,1 und dt = 0,05 (fein dr/2, dt/2), Daempfungsschicht wie tests1d (r = 110 bis 150)
  - Bad -gamma (psi_t + i omega_b psi): omega_b = 0 ist ein gleichmaessiger Abfluss, dQ/dt = -gamma Q. omega_b > 0
    ist ein Reservoir mit festem chemischem Potential; fuer einen ruhenden Ball gilt dQ/dt = -gamma (1 - omega_b/omega) Q.
- **Sicherung:** Nach 540 s werden laufende Zeitentwicklungen gekuerzt und die feine Stufe entfaellt; Bericht und JSON
  entstehen trotzdem (kleintest.sh bricht bei 600 s ab).
- **Kernvorhersagen:**
  - Tropfenbild mit Young-Laplace gilt fuer duenne Waende (Y -> 1).
  - Der Tod unter Q_min kommt schlagartig.
  - Angeregte Profile existieren und zerfallen.
  - E/Q faellt streng mit Q; magische Zahlen gibt es nicht. Das folgt vorab aus Papier (siehe Abschnitt 4).
  - Der kritische Keim ist der Ball mit omega = omega_b.

## 1. Aufrufe (Leitung, auf der .69 ueber kleintest.sh)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde5-r5a/ mit r5a.py und eingabe/tests1d_ergebnis_runde2.json darin (den
Ordner r5a/ so kopieren). Das Programm braucht nur torch und schreibt nur in --out.

**Rauchtest** (alle sechs verkleinert: Laufzeiten x 0,05, 2 Schiessrunden, kurze omega-Listen). Einmal je Geraet, weil
beide Wege gebraucht werden:

```
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5a-rauch-gpu r5a.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5a/rauch-cuda
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5a-rauch-cpu r5a.py rauch --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5a/rauch-cpu
```

**Hauptlaeufe**, nur nach Rauchtest mit rc = 0 auf dem jeweiligen Geraet. Vorschlag zur Spurverteilung:

```
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5a-fitness r5a.py fitness --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5a/ausgabe-fitness
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5a-membran r5a.py membran --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5a/ausgabe-membran
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5a-tod r5a.py tod --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5a/ausgabe-tod
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5a-mutanten r5a.py mutanten --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5a/ausgabe-mutanten
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5a-magisch r5a.py magisch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5a/ausgabe-magisch
cd /home/fmh/fmhc-physics-remote/runde5-r5a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r5a-keim r5a.py keim --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5a/ausgabe-keim
```

- Ist p4000b gesperrt (WM-1-MB laeuft), `keim` auf p4000a nach `magisch` oder auf cpu2 mit `--geraet cpu`.
- Jeder Unterbefehl laeuft auf beiden Geraeten. Auf einer cpu-Spur immer `--geraet cpu`, weil kleintest.sh dort
  CUDA_VISIBLE_DEVICES leer setzt.
- Auf der CPU schiesst das Programm von selbst mit 256 Kandidaten x 5 Runden statt 1024 x 4. Die Klammerbreite ist
  gleich (150/255^5 = 1,4e-10 gegen 150/1023^4 = 1,4e-10), die Arbeit ein Drittel. Aendern mit `--kand`, `--runden`.
- Ausgabe je Aufruf: r5a_<unterbefehl>_bericht.txt (auch auf stdout), r5a_<unterbefehl>_ergebnis.json und fuer tod,
  mutanten und keim r5a_<unterbefehl>_zeitreihen.pt. Die Zeitreihen haben die Spalten Q_tot, Q_in (r < 25), E_tot,
  S_c = |psi(0)|^2, Phase, max |psi|^2, Ladungsradius und Dichteabweichung.

## 2. Laufzeiten (Schaetzung, nicht gemessen)

Grundlage sind Messungen auf der P4000 aus RUNDE-02/tests1d/lauf-69/LAUF.log:
- radiales Schiessen 2,9 ms je RK4-Schritt fuer 52 x 1024 Kandidaten, durch Kernelstarts begrenzt (43,7 s fuer
  5 x 2999 Schritte)
- Verlet-Schritt 1,0 bis 1,3 ms

Die Knotenlogik kostet etwa 20 % mehr: 3,5 ms je Schiessschritt. Ein Schiessen hat (Runden + 1) x 2999 Schritte bei
h = 0,05 und doppelt so viele bei h/2. CPU-Werte sind grob (Faktor 2 bis 3 unsicher): ein Kern, etwa 10 us je Operation
plus Arbeit proportional zu Zeilen x Kandidaten.

| Unterbefehl | Arbeit | P4000 | CPU (ein Kern) | Spur |
|---|---|---|---|---|
| rauch | alles verkleinert | 3,5 bis 5 min | 1 bis 3 min | p4000a und cpu |
| fitness | nur Tabelle | unter 10 s | unter 10 s | cpu |
| membran | 19 Zeilen, h und h/2 (15000 + 30000 Schritte) | 2,5 bis 3 min | 1 bis 3 min | cpu |
| tod | 1 Zeile schiessen; 6 Laeufe x T = 1500 (30000 + 60000 Verlet-Schritte) | 2,5 bis 3 min | 1 bis 2,5 min | cpu2 |
| mutanten | 89 Zeilen, h und h/2; 8 Laeufe x T = 1000 | 4 bis 5 min | 2,5 bis 7,5 min | p4000a |
| magisch | 137 Zeilen bei h, 97 bei h/2 | 3 bis 4 min | 2,5 bis 7,5 min | p4000a |
| keim | 15 Zeilen; 21 Laeufe x T = 800 | 2 bis 2,5 min | 2 bis 6,5 min | p4000b |

- **Hochrechnung aus dem Rauchtest:** Er druckt je Teil "ms je Schritt".
  - Schiessen: ms je Schritt x (Runden + 1) x 2999 fuer h, x 5999 fuer h/2. Auf der CPU zusaetzlich x (Zeilen x
    Kandidaten voll / Rauch).
  - Zeitentwicklung: ms je Schritt x T/dt (grob T/0,05, fein T/0,025 mit etwas mehr je Schritt).
  - Liegt ein Unterbefehl ueber 9 min, nicht starten, sondern auf eine GPU-Spur legen. Die Leitung entscheidet.
- Speicher: groesste Felder 137 x 6001 float64 (Bahnen, 6,6 MB) und 21 x 3001 complex128. Insgesamt unter 0,1 GB.

## 3. Aufbau je Idee (vor dem Lauf festgelegt)

Bezeichnungen:
- S0 = f(0)^2
- S_top = (2 + sqrt(4 - 6 (1 - omega^2)))/3 ist die dichte Phase: U'(S) = omega^2, groessere Wurzel.
- P_bulk = omega^2 S_top - U(S_top) ist ihr Druck.
- Flache Wand bei omega^2 = 1/2: f' = -(f/sqrt 2)(1 - f^2), also sigma_inf = Int 2 f'^2 dx = sqrt(2)/4 = 0,35355.

**Bio 1 Membran (`membran`).**
- Profile: omega^2 = 0,51 / 0,52 / 0,53 / 0,54 / 0,55 / 0,57 / 0,60 / 0,65 / 0,70 / 0,75 / 0,80 / 0,85 / 0,90 / 0,93 /
  0,95 / 0,98 in d = 3; dazu d = 1 bei den drei Karten-Q 0,52 / 0,55 / 0,60. Jeweils mit h und h/2.
- Spannungstensor eines stationaeren Profils:
  - p_r = f'^2 + omega^2 f^2 - U
  - p_t = omega^2 f^2 - f'^2 - U
  - Impulserhaltung: dp_r/dr = -(4/r) f'^2
- Gemessen:
  - Innendruck P_in = p_r(0) = omega^2 S0 - U(S0) und P_bulk
  - Wandspannung sigma = Int (p_r - p_t) dr = Int 2 f'^2 dr
  - Identitaet dP_mech = Int (4/r) f'^2 dr gegen P_in (nur Numerik)
  - Radien: R_halb (f^2 = S0/2), R_grad (f'^2-gewichtet), R_Q (Ladungsaequivalent)
  - Young-Laplace-Verhaeltnisse Y = P_in R / (2 sigma) fuer alle drei Radien
  - Vorhersage ohne Profil Y_vorh = P_bulk R_halb / (2 sigma_inf), also R_halb gegen R_YL = 2 sigma_inf / P_bulk
  - Membranbreite (Gebiet mit p_t < 0) und Int p_t dort
  - Tolman-Laenge delta = R_halb (1 - Y_halb)/2 und ihr Fit ueber omega^2 <= 0,60
  - p_r(r), p_t(r) der drei Karten-Q im JSON
- Hinweis: Mit R_grad gilt Y_grad >= 1 exakt (Jensen: Y_grad = R_grad <1/r>, gewichtet mit f'^2). Die Aussage mit R_grad
  kann also nicht scheitern. Die pruefbaren Aussagen stehen deshalb bei Y_halb und vor allem bei Y_vorh.

**Bio 4 Tod unter Q_min (`tod`).**
- Start: Ball omega^2 = 0,80 (Q = 186,1). Runden-2-Werte: Q_min = 111,84 bei omega^2 = 0,927.
- Sechs Laeufe, T = 1500, Messung alle 1:
  - Abfluss gamma = 2e-3, 1e-3 und 5e-4 ohne Stopp. Q_erw = Q_min wird bei t = 255 / 509 / 1018 erreicht.
  - gamma = 1e-3 mit Stopp bei Q_erw = 1,1 Q_min (t = 414)
  - gamma = 1e-3 mit Stopp bei Q_erw = 0,9 Q_min (t = 615)
  - ohne Abfluss
- Messung:
  - q_rel = Q_in(r < 25) / Q_erw mit Q_erw = Q(0) exp(-gamma min(t, t_stop))
  - Zeiten t90, t50, t10 (q_rel faellt unter 0,9 / 0,5 / 0,1)
  - Todesladung Q_in(t90) / Q_min
  - omega kurz vor dem Tod (aus der Zentralphase)
  - hoechste Verlustrate (-d ln Q_in/dt ueber 10) im Verhaeltnis zu gamma
  - gamma x (t10 - t90)
  - Verzoegerung tau = t50 - t(Q_erw = Q_min) und ihr Exponent p in tau ~ gamma^-p
- Klassen (vorab):
  - schlagartig: gamma (t10 - t90) < 0,1 und Rate/gamma > 10
  - allmaehlich: gamma (t10 - t90) > 0,3 oder Rate/gamma < 3
  - sonst unklar; ueberlebt: q_rel faellt nie unter 0,5
- **Abweichung vom Wortlaut "Abfluss am Rand":** Der Abfluss ist gleichmaessig (-gamma psi_t ueberall). Ein Abfluss nur am
  Rand saugt ueber den Auslaeufer und ist exponentiell empfindlich gegen den Randabstand (Rate ~ exp(-2 kappa d)), also
  nicht einstellbar. Der gleichmaessige Abfluss fuehrt den Ball dagegen genau entlang seiner Familie (dE = omega dQ).

**Bio 17 Mutanten (`mutanten`).**
- Schiessen in drei Familien, jeweils mit h und h/2:
  - n = 0: omega^2 = 0,51 bis 0,99 in 0,01
  - n = 1 und 2: 0,60 bis 0,98 in 0,02 (darunter werden die Radien fuer r <= 150 zu gross)
- Gueltig heisst: Stopp im Schwanz nach genau n Knoten und s < 149,5.
- Je Profil: Q, E, E/Q, Pohozaev-Rest und E - E_0 bei gleichem Q (E_0 vom duennen Ast der n = 0-Familie, E/Q linear in
  ln Q). Je Familie: Q_min, Monotonie von E/Q(Q), omega^2 mit E > Q.
- Dynamik (T = 1000, gamma = 0), Saat psi und psi_t mal 1,001:
  - n = 1 und 2 bei omega^2 = 0,70 / 0,80 / 0,90
  - Kontrollen n = 0 bei 0,80 (VK-stabil) und 0,95 (dicke Wand, VK-instabil)
  - Laeufe mit r_cut > 90 fallen weg (Daempfungsschicht ab 110) und werden gemeldet.
- Gemessen:
  - Dichteabweichung Int (S - S_0)^2 r^2 / Int S_0^2 r^2 (r < 110)
  - Zerfallszeit: Abweichung > 0,1
  - Anwachsrate lambda aus dem Durchgang 1e-4 -> 1e-2 (Abweichung ~ Amplitude^2)
  - Q_in und Q_tot am Ende, S_c am Ende, omega am Ende

**Bio 19/34 Fitness und Waehrung (`fitness`, nur Auswertung der Runde-2-Tabelle, 49 Zeilen in d = 3).**
- Je Zeile:
  - E/Q
  - freie Energie je Ladung b = 1 - E/Q
  - Grenzgewinn je Quant 1 - omega (ein ruhendes freies Quant hat die Energie 1)
  - Bindung Q - E
  - Duennwand-Konstante (E/Q - omega_c) Q^(1/3) / C_DW. Oberflaechenenergie 4 pi sigma R^2 gibt
    E/Q - omega_c = (3 sigma_inf / (2 omega_c)) (8 pi omega_c / 3)^(1/3) Q^(-1/3) = 1,357 Q^(-1/3).
- Q-Fenster:
  - Q_min (Parabel wie tests1d)
  - Q_abs, wo auf dem duennen Ast E = Q wird
  - dazwischen metastabil (VK-stabil, aber E > Q)
- Fusion auf dem duennen Ast fuer Q1, Q2 aus {120, 150, 200, 300, 500, 1e3, 3e3, 1e4, 1e5, 1e6} mit Q1 + Q2 <= 2,17e6:
  - dE = E(Q1) + E(Q2) - E(Q1+Q2)
  - dE/Q1, Wirkungsgrad dE/(E1 + E2)
  - omega(Q1) gegen omega(Q2): Richtung des Ladungsflusses

**Chemie 11 Keimbildung (`keim`).**
- Bad mit festem chemischem Potential omega_b: -gamma (psi_t + i omega_b psi), gamma = 0,02. Das ist die relativistische
  Form der gedaempften Gross-Pitaevskii-Gleichung mit (H - mu).
- Aufbau:
  - omega_b^2 = 0,55 / 0,60 / 0,70
  - Startbaelle omega^2 = omega_b^2 + (-0,02, -0,005, 0, +0,005, +0,02)
  - Gegenprobe: dieselben Baelle bei +-0,02 ohne Bad
  - T = 800
- Gemessen:
  - kappa = d ln Q_tot/dt in [T/8, T/2] gegen kappa_vorh = gamma (omega_b/omega - 1)
  - Q_T/Q_0 und Klasse waechst / schrumpft / bleibt (Schwelle 0,1 %)
  - kritischer Radius R_c = R_halb, bei dem kappa das Vorzeichen wechselt
  - Vergleich mit R_halb(omega_b), R_CNT = 2 sigma_inf / P_bulk(omega_b) (klassische Keimbildung: Wandspannung gegen
    Druckdifferenz zum Reservoir, Aussendruck 0) und R_YL = 2 sigma / P_in aus dem eigenen Profil
- **Warum kein expliziter Hintergrund (kleinste sinnvolle Form):**
  - Ein homogener Hintergrund ist genau dann linear stabil, wenn U''(S) = 3 S - 2 > 0 ist, also S > 2/3.
    Modulationsanalyse: (k^2 - Omega^2 + 2 S U'')(k^2 - Omega^2) = 4 omega^2 Omega^2. Anwachsrate fuer kleines S etwa
    S |U''| / (2 omega).
  - Stabile Hintergruende mit 1/2 < omega_b^2 < 1 haben S = 1 bis 4/3. Das ist die dichte Phase selbst, also das
    Ballinnere.
  - Ein duenner Hintergrund, dessen omega_b einen duennwandigen kritischen Keim haette (omega_b^2 < 0,927, S_b > 0,037),
    zerfaellt selbst: Anwachsrate 0,037 bei S_b = 0,037 bis 0,10 bei S_b = 0,11, also e-fach in 10 bis 27 Zeiteinheiten.
  - Klassische Keimbildung aus einem metastabilen duennen Medium gibt es in diesem Modell also nicht; der duenne
    Hintergrund ist ueberall spinodal. Das Bad ersetzt das Medium durch ein Reservoir mit festem omega_b.

**Chemie 18 magische Zahlen (`magisch`).**
- Schiessen:
  - n = 0 fein: omega^2 = 0,51 bis 0,99 in 0,005 (97 Werte), mit h und h/2
  - n = 1 und 2 grob: 0,60 bis 0,98 in 0,02, mit h
- Je Familie:
  - Monotonie von E/Q(Q) auf beiden Aesten
  - vierte Differenzen von E/Q entlang omega^2. "Auffaellig" heisst: mehr als das Zehnfache des Medians der Nachbarn
    (Abstand 3 bis 8) und mehr als das Zwanzigfache des Rauschens |E/Q(h) - E/Q(h/2)|.
  - erster Hauptsatz dE/dQ = omega (zentrale Differenzen, ohne die zwei Punkte am Minimum)
  - Schranke E/Q > omega
  - Q_min, Q_abs
- Kreuzen die Familien? Gezaehlt wird E_n < E_0 bei gleichem Q.

## 4. Vorhersagen (vor dem Rechnen, von Hand)

**Papier vorab (gilt fuer 19/34 und 18):**
- In d = 3 gilt nach dem Virialsatz E - omega Q = (2/3) Int |grad psi|^2 > 0.
- Mit dE/dQ = omega folgt d(E/Q)/dQ = (omega - E/Q)/Q = -(2/3) G / Q^2 < 0 auf jedem glatten Ast einer Familie.
- Eine "optimale Groesse" oder magische Zahl (lokales Minimum von E/Q) ist innerhalb einer Familie deshalb
  ausgeschlossen.
- Moeglich waeren nur Knicke der unteren Einhuellenden: Q_min (darunter kein Ball, E/Q der freien Quanten = 1), Q_abs
  (E/Q kreuzt 1) oder Kreuzungen zweier Familien.

**Bio 1 Membran.**
- V1a Identitaet: |dP_mech/P_in - 1| < 1e-3 in allen gueltigen d = 3-Zeilen (Trapezfehler, reine Numerik).
- V1b Gegenprobe d = 1: |P_in| < 1e-8 bei 0,52 / 0,55 / 0,60. Ohne Kruemmung gibt es keinen Druckunterschied.
- V1c Wandspannung: sigma/sigma_inf liegt bei omega^2 <= 0,53 zwischen 0,95 und 1,05. Die Abweichung waechst etwa linear
  mit omega^2 - 1/2.
- V1d Young-Laplace ohne Profil: Y_vorh = R_halb / R_YL, mit R_YL = 35,0 / 13,8 / 6,76 bei 0,52 / 0,55 / 0,60.
  - 0,52: 0,97 bis 1,04
  - 0,55: 0,93 bis 1,08
  - 0,60: 0,95 bis 1,20
  - Grundlage: r_cut aus Runde 2 minus etwa 10 Laengen Schwanz, von Hand.
- V1e Tolman: |Y_halb - 1| R_halb bleibt fuer omega^2 <= 0,60 etwa konstant; |delta| < 2 (von der Groesse der Wanddicke).
- V1f Grenze des Tropfenbilds: Y_grad - 1 < 0,01 bei omega^2 <= 0,53, unter 0,1 bis 0,60 und ueber 0,1 ab 0,80. Das ist
  unsicher.
- **Gegenhypothese (L1):** Y_vorh weicht bei 0,52 um mehr als 5 % von 1 ab, oder sigma/sigma_inf bei 0,51 bis 0,53 um
  mehr als 10 %. Dann ist das Ballinnere nicht die homogene dichte Phase, oder die Wand nicht die flache Wand. Das
  Tropfenbild waere dann falsch.

**Bio 4 Tod.**
- V4a Schwelle: In allen drei Abflusslaeufen ohne Stopp stirbt der Ball erst, nachdem Q_erw unter Q_min faellt. Also gilt
  tau = t50 - t(Q_erw = Q_min) > 0, und gamma tau < 0,3. Kurz vor dem Tod liegt omega^2 bei 0,90 bis 0,93
  (omega 0,95 bis 0,965).
- V4b schlagartig: Klasse "schlagartig" mindestens fuer gamma = 1e-3 und 5e-4, also Rate/gamma > 10 und
  gamma (t10 - t90) < 0,1. Begruendung: Q_min ist ein Faltpunkt; darunter gibt es keinen Ball, der Rest zerstreut sich
  auf der dynamischen Zeitskala (10 bis 100), nicht auf 1/gamma. Bei gamma = 2e-3 ist "unklar" moeglich.
- V4c Stopp-Paar: Stopp bei 1,1 Q_min ueberlebt bis T (q_rel(T) > 0,9). Stopp bei 0,9 Q_min stirbt (q_rel(T) < 0,1),
  obwohl der Abfluss vorher endet.
- V4d Verzoegerung: tau zwischen 10 und 300. Exponent p zwischen 0,1 und 0,45; erwartet etwa 0,2 (Normalform eines
  Sattel-Zentrum-Punkts, tau ~ gamma^(-1/5)). p nahe 1/3 hiesse: die Daempfung beherrscht den Durchgang. Das ist
  unsicher.
- Gegenprobe ohne Abfluss: q_rel(T) > 0,99 und S_c(T)/S_c(0) zwischen 0,95 und 1,05.
- **Gegenhypothese (L1), allmaehlich:** Q_in folgt Q_erw glatt unter Q_min (q_rel bleibt nahe 1 bis weit unter Q_min),
  oder ein langlebiger atmender Rest ueberlebt den Stopp bei 0,9 Q_min.

**Bio 17 Mutanten.**
- V17a Existenz: Fuer n = 1 und n = 2 sind mindestens 15 von 20 omega^2 gueltig. Bei gleichem omega gilt Q_n > Q_0. Jede
  Familie hat ein eigenes Minimum mit Q_min,2 > Q_min,1 > Q_min,0 = 111,8.
- V17b Energie: Bei gleichem Q gilt E_n > E_0 in allen gueltigen Zeilen (min(E - E_0) > 0) und E_2 > E_1.
- V17c Lebensdauer: Alle n = 1- und n = 2-Laeufe zerfallen vor T = 1000, mit lambda > 0,005 und Zerfallszeiten von
  etwa 50 bis 500. Kontrollen: n = 0 bei 0,80 lebt (Abweichung am Ende < 1e-3); n = 0 bei 0,95 (VK-instabil) zerfaellt vor
  T.
- V17d Zerfallsprodukt: Meist bleibt ein Grundzustandsball (S_c(T) > 0,3, Q_in(T) > Q_min); der Rest wird abgestrahlt.
  Das ist unsicher.
- **Gegenhypothese (L1):** Ein angeregtes Profil lebt bis T (Abweichung < 0,1), also ein langlebiger "Mutant". Oder die
  angeregten Familien existieren nicht (gueltig < 5 von 20).
- **Grenze:** Radial sieht der Code nur kugelsymmetrische Stoerungen (l = 0). Nichtradiale Instabilitaeten fehlen. Die
  Lebensdauern sind daher obere Schranken.

**Bio 19/34 Fitness.** Die Tabelle ist bekannt. Die Zahlen unten habe ich beim Schreiben von Hand gegen drei
Tabellenzeilen geprueft; sie sind keine blinde Vorhersage.
- F1: E/Q faellt auf beiden Aesten streng mit Q (0 Verstoesse). Groesser ist immer "fitter"; eine optimale Groesse gibt
  es nicht (Papier, Abschnitt 4).
- F2: E/Q - omega > 0 in allen Zeilen. Der Grenzgewinn 1 - omega ist also immer groesser als die gespeicherte Energie je
  Ladung b = 1 - E/Q.
- F3: (E/Q - omega_c) Q^(1/3) / 1,357 liegt bei 1,00 bis 1,03 (0,51), bei 1,02 bis 1,04 (0,52) und unter 1,07 (0,55).
- F4: Das Q-Fenster ist [Q_min, Q_abs] = [111,8; etwa 142] (E = Q zwischen omega^2 0,84 und 0,85). Das ist ein Faktor
  1,27 metastabiler Baelle. Auf dem dicken Ast gilt ueberall E > Q.
- F5: Fusion setzt fuer alle Paare Energie frei (dE > 0). Ladung fliesst immer vom kleinen zum grossen Ball. dE/Q1 naehert
  sich E/Q(Q1) - omega(Q2); fuer Q1 = 150 und Q2 = 1e6 sind das etwa 0,28 je Ladung.
- Die Waehrung b reicht von -0,017 (Q_min) bis +0,282 (Q = 2,2e6); die Grenze fuer grosse Q ist 1 - 1/sqrt 2 = 0,293.

**Chemie 11 Keim.**
- K1 Vorzeichen: Mit Bad wachsen die groesseren Baelle (Versatz -0,02 und -0,005, also omega < omega_b), die kleineren
  (+0,005, +0,02) schrumpfen; das gilt fuer alle drei omega_b. Der Ball mit Versatz 0 aendert Q um weniger als 20 % der
  Aenderung bei +-0,005.
- K2 adiabatisch: kappa/kappa_vorh liegt zwischen 0,75 und 1,25 fuer alle Versaetze ungleich 0. Der Ball folgt seiner
  Familie; die Abweichung kommt aus der Aenderung von omega im Messfenster.
- K3 kritischer Radius: R_c (dynamisch) = R_halb(omega_b) auf 3 %. R_CNT / R_c: 0,92 bis 1,08 bei 0,55; 0,83 bis 1,05
  bei 0,60; bei 0,70 offen (dicke Wand, dort darf die klassische Keimbildungsformel scheitern).
- Gegenprobe ohne Bad: |Q_T/Q_0 - 1| < 1e-3, |kappa| < 1e-6.
- **Gegenhypothese (L1):** Vorzeichen andersherum, oder kein Vorzeichenwechsel; das Bad wuerde dann den Ball anders
  antreiben als ueber omega. Oder R_CNT weicht bei 0,55 um mehr als 15 % ab: Die klassische Keimbildung passte dann
  selbst fuer duenne Waende nicht.

**Chemie 18 magische Zahlen.**
- M1 (n = 0): 0 Monotonie-Verstoesse, keine auffaelligen vierten Differenzen, dE/dQ = omega im Median unter 3e-4 und
  min(E/Q - omega) > 0.
- M2: Q_min = 111,84 +- 0,05 bei omega^2 = 0,927 +- 0,002; Q_abs = 142 +- 3.
- M3: n = 1 und 2 sind ebenfalls glatt und monoton je Ast, jeweils mit eigenem Q_min.
- M4: Die Familien kreuzen nicht (0 Faelle E_n < E_0).
- Folgerung: Die untere Einhuellende hat nur zwei Knicke. Bei Q_min endet die Ballfamilie (darunter freie Quanten), bei
  Q_abs wird E/Q = 1. Es gibt keine magischen Zahlen; die Karte ist L1-schwach, weil das Papier (Abschnitt 4) das vorab
  festlegt.
- **Gegenhypothese (L1):** Ein auffaelliger Punkt oder ein Monotonie-Verstoss, der L3 besteht (groesser als das
  Zwanzigfache des h/2-Rauschens), oder eine Familienkreuzung.

## 5. Gegenproben und Aufloesungsvergleich

| Idee | Gegenprobe (Effekt muss verschwinden) | Aufloesungsvergleich (L3) |
|---|---|---|
| Bio 1 | d = 1 bei denselben omega: P_in = 0; Identitaet dP_mech = P_in | h gegen h/2 fuer P_in, sigma, Y_halb - 1, Y_vorh - 1 |
| Bio 4 | ohne Abfluss; Stopp bei 1,1 Q_min (darf nicht sterben) | dr/2 und dt/2 fuer Rate/gamma, q_rel(T), Todesladung |
| Bio 17 | n = 0 bei 0,80 (darf nicht zerfallen); n = 0 bei 0,95 als positive Kontrolle | h/2 fuer E - E_0; dr/2 und dt/2 fuer die Zerfallszeit |
| Bio 19/34 | keine eigene; Kontrollen der Tabelle (Virial 1,3e-6, dE/dQ = omega auf 6e-4, 1D-Anker 3e-8) | nicht moeglich (nur Auswertung); `magisch` liefert E/Q mit h/2 zum Vergleich |
| Chemie 11 | dieselben Baelle ohne Bad; Ball mit omega = omega_b | dr/2 und dt/2 fuer kappa |
| Chemie 18 | Kontrollen dE/dQ = omega, E/Q > omega | h/2: Rauschen von E/Q und Q; Auffaelligkeit erst ab dem Zwanzigfachen |

"Halber Zeitschritt": In den Zeitentwicklungen halbiert die feine Stufe wie in tests1d dr und dt zugleich. Beim Schiessen
halbiert h/2 die Schrittweite des Integrators.

## 6. Latten (Vorschlag, die Leitung entscheidet)

| Latte | Bio 1 Membran | Bio 4 Tod | Bio 17 Mutanten | Bio 19/34 Fitness | Chemie 11 Keim | Chemie 18 magisch |
|---|---|---|---|---|---|---|
| L1 kann scheitern | ja, ueber Y_vorh und sigma/sigma_inf (Y_grad >= 1 ist exakt und zaehlt nicht) | ja: allmaehlich, oder Rest ueberlebt 0,9 Q_min | ja: langlebiger Mutant oder keine angeregte Familie | schwach: F1 und F2 folgen aus Virial und dE/dQ = omega | ja: Vorzeichen, R_CNT bei 0,55 | schwach: Papier schliesst Minima je Familie aus; offen nur Kreuzungen |
| L2 Gegenprobe | d = 1 | ohne Abfluss, Stopp 1,1 | n = 0 stabil und instabil | nur Tabellenkontrollen | ohne Bad | Hauptsatz, Virial |
| L3 Numerik | h/2 im Code | dr/2 und dt/2 im Code | h/2 und dr/2 im Code | nicht anwendbar | dr/2 und dt/2 im Code | h/2-Rauschen im Code |
| L4 schon bekannt | vermutlich: Duenne-Wand-Theorie (Coleman 1985), Spannungstensor und "Tropfen" bei Q-Baellen (Mai und Schweitzer 2012) | teilweise: Q_min bekannt; der dynamische Tod mit Abfluss weniger | vermutlich: radial angeregte Q-Baelle (Volkov und Woehnert 2002; Mai und Schweitzer 2012) | ja: E/Q(Q), Coleman; Virialsatz | teilweise: gedaempfte GPE mit mu als Reservoir; kritische Ladung wie bei Solitosynthese (Griest und Kolb 1989) | ja, vorab aus dem Papier |
| L5 Messbezug | nein | nein | nein | nein | nein | nein |

Literatur aus dem Gedaechtnis, nicht nachgelesen.

## 7. Grenzen

- **Ungetestet:** Das Programm ist nie gelaufen; deshalb zuerst die beiden Rauchtests. Wahrscheinlichste Fehlerstellen:
  - Tensorformen in der Knotenlogik (schiessen_radial, radial_bahn)
  - die Verwaltung der Laeufe in `mutanten`, wenn Profile fehlen
  - Randfaelle mit nan in den Auswertungen
- **Nur l = 0:** Alle Zeitentwicklungen sind kugelsymmetrisch. Nichtradiale Instabilitaeten, Teilung und Verformung sind
  unsichtbar. Das betrifft vor allem die Lebensdauern (Bio 17) und den Tod (Bio 4).
- **Bad statt Medium (Chemie 11) und gleichmaessiger Abfluss (Bio 4):** Beides sind phaenomenologische Kopplungen an ein
  Reservoir, keine Felder. Die Gleichung fuer dQ/dt eines stationaeren Balls folgt aus ihnen exakt; gemessen wird, ob der
  Ball ihr adiabatisch folgt und was am Faltpunkt geschieht.
- **Profile auf dem Gitter:** Die Anfangsfelder sind Kontinuumsprofile (h = 0,05), auf dr = 0,1 bzw. 0,05 abgetastet.
  Der Ball startet um O(dr^2) angeregt; das ist die Hintergrundsaat neben der gesetzten Saat 1e-3.
- **Q_in:** Die Ladung im Ballgebiet zaehlt fuer r < 25. Angeregte Profile koennen darueber hinausreichen; deshalb
  meldet `mutanten` auch Q_tot.
- **omega-Gitter:** In `mutanten` und `magisch` sind die angeregten Familien mit 0,02 grob abgetastet; Q_min,n ist dort
  nur auf etwa 1 % genau.

## Einfach gesagt

Wir pruefen sechs Ideen, bei denen ein kugelrunder Q-Ball sich wie eine Zelle oder ein Atom verhalten soll. Die Haut des
Balls ist wie die Haut eines Wassertropfens: Innen herrscht ein Ueberdruck, und wir messen, ob er genau so gross ist, wie
es die Tropfenformel aus Spannung und Radius verlangt. Laesst man einem Ball langsam Ladung abfliessen, sollte er bei
einer Mindestgroesse ploetzlich zerfallen statt langsam zu verblassen. Baelle mit Ringen im Inneren ("Mutanten") gibt es
wohl, sie sollten aber schnell zerfallen. Dass grosse Baelle je Ladung am wenigsten Energie haben und es keine besonders
stabilen "magischen" Groessen gibt, folgt schon aus einer Rechnung auf Papier. In einem Ladungsbad sollten kleine Baelle
schrumpfen und grosse wachsen, mit einer Grenzgroesse wie bei Regentropfen in Wolken. Gerechnet ist noch nichts; die
Leitung startet jeden Test auf einer Grafikkarte oder einem Prozessorkern, jeden in hoechstens zehn Minuten.

Beginn 2026-09-30 01:43:40 CEST, Ende 2026-09-30 02:21:23 CEST (beide mit date gemessen).
