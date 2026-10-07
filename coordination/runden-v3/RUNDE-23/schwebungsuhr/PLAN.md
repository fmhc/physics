# PLAN SCHWEBUNGSUHR (Runde 23), Code-Agent im Auftrag der Leitung claude-primary

- Geschrieben 2026-10-02 ab 21:37:05 CEST (date), nach dem Rauchlauf, vor jedem echten Lauf und jedem Literaturabruf.
- Karte: KARTE.md (unveraendert). Vorhersagen S0 bis S4 und ihre Bedeutung gelten wie auf der Karte.
- Code: code/schwebung1d.py, sha256 bd0fd1b7ff5db656f8504d14a695b3a46e84c3a8a9051b3c57b113b368862c45.

## Rauchlauf (vor dem Einfrieren, dokumentiert, nicht gewertet)

- 21:35 CEST, .69, Spuren cpu und cpu2, Ausgaben in hilfs/rauch/.
- `profil 0.1` und `profil 0.05`: diskrete Profile und D-Tabelle (unten). Newton-Residuum 1,7e-14 (dx 0,1), 7,7e-14 (dx 0,05).
  Zentraldichte S0 diskret/kontinuierlich: 0,60: 0,55290/0,55279 (dx 0,1); 0,65: 0,45237/0,45228.
- `paar 0.70 0.75 10.0 0.5 0.05 460 900`: absichtlich ein Parametersatz, der in keinem echten Lauf vorkommt (nur
  Laufzeit und Absturzfreiheit). 1,64 ms je Schritt bei N = 36000; Analyse 5 s, kein Analysefehler.
  Hochgerechnet: feines Gitter T = 3000 etwa 250 s Schleife plus etwa 30 s Analyse, grobes etwa 70 s.

## D aus den diskreten Profilen (vor dem Einfrieren)

Regel: Zentren auf Knoten beider Gitter, also D Vielfaches von 0,2. Gewaehlt wird der Kandidat 5,6 ... 7,4, dessen
geometrisches Mittel der beiden Nachbardichten am eigenen Zentrum (Dichte von Ball b am Zentrum von a, von a am
Zentrum von b) in log10 am naechsten an 1e-3 liegt. Ergebnis auf beiden Gittern gleich:

| D | S_b am Zentrum a | S_a am Zentrum b | geom. Mittel | S_a(D/2) | S_b(D/2) |
|---|---|---|---|---|---|
| 6,4 | 1,31e-3 | 1,09e-3 | 1,19e-3 | 0,0579 | 0,0535 |
| **6,6** | **1,04e-3** | **0,85e-3** | **0,94e-3** | 0,0514 | 0,0479 |
| 6,8 | 0,82e-3 | 0,66e-3 | 0,73e-3 | 0,0457 | 0,0429 |
| D' = 4,6 | 1,09e-2 | 1,05e-2 | 1,07e-2 | 0,156 | 0,135 |
| Zusatz 14,6 | 8,0e-8 | 3,4e-8 | 5,2e-8 | 3,5e-4 | 4,5e-4 |

**D = 6,6, D' = 4,6.** Ball a (omega^2 = 0,60, Q = 3,163) links bei x = -D/2, Ball b (0,65, Q = 2,759) rechts bei +D/2.

## Aufbau (alle Laeufe)

- M1 in 1D, psi_tt = psi_xx - U'(|psi|^2) psi. Gitter x_j = (j - N/2) dx auf [-900, 900], Dirichlet an den Enden,
  Daempfungsschicht |x| > 840 (SIGMA0 = 1, quadratisch), Leapfrog dt = 0,4 dx. Gitter **dx = 0,1 (grob) und 0,05 (fein)**.
- Profile: Newton auf der diskreten Gleichung (Startwert die geschlossene Loesung S = 2k^2/(1 + s cosh 2kx)).
- Start: psi = f_a(x - x_a) + e^(i pi theta) f_b(x - x_b); Startschritt je Ball exakt: psi(-dt) = f_a e^(+i w_a,d dt)
  + e^(i pi theta) f_b e^(+i w_b,d dt), w_d = (2/dt) asin(w dt/2). Phasenlage **theta = 0** in den Hauptlaeufen.
- Startstoerung: nichtlineare Kreuzbeschleunigung -U'(|psi|^2) psi + U'(|psi_a|^2) psi_a + U'(|psi_b|^2) psi_b (max und
  L2) und Wechselwirkungsenergie E(0) - E_a - E_b werden je Lauf berichtet.
- T = 3000 (Paare), T = 500 (Einzelbaelle). Messung alle 0,2 Zeiteinheiten. Bilder |psi|^2 alle 100 Einheiten.

## Laeufe (alle vor dem ersten Lauf festgelegt)

| Name | w_a^2 | w_b^2 | D | theta/pi | Gitter | wofuer |
|---|---|---|---|---|---|---|
| K1/K3 | 0,60 | - | - | - | 0,1 / 0,05 | Stationaritaet Einzelball |
| K2/K4 | 0,65 | - | - | - | 0,1 / 0,05 | Stationaritaet Einzelball |
| H1/H2 | 0,60 | 0,65 | 6,6 | 0 | 0,1 / 0,05 | S1, S2, S3 |
| H3/H4 | 0,60 | 0,65 | 4,6 | 0 | 0,1 / 0,05 | S4 |
| C1/C2 | 0,60 | 0,60 | 6,6 | 0 | 0,1 / 0,05 | S0 (Phasenlage 0) |
| C3/C4 | 0,60 | 0,60 | 6,6 | 1 | 0,1 / 0,05 | S0 (Phasenlage pi) |
| Z1 | 0,60 | 0,65 | 6,6 | 1 | 0,1 | Zusatz: Phasenlage pi bei D, nicht gewertet |
| Z2/Z3 | 0,60 | 0,65 | 14,6 | 0 | 0,1 / 0,05 | Zusatz: schwache Kopplung, nicht gewertet |

Die Kontrolle gleiche Takte nutzt omega^2 = 0,60 fuer beide Baelle.

## Messgroessen (je 0,2 Zeiteinheiten)

- Maxima p1(t), p2(t): Ort der groessten Dichte in x < 0 bzw. x > 0 (Innengebiet), parabolisch verfeinert.
  Abstand d = p2 - p1. Mitte m = (p1 + p2)/2.
- Mittelpunktsdichte S_mitte = |psi(m)|^2 (lineare Interpolation; gewertet); zum Vergleich S_null = |psi(0)|^2.
- Ladungen Q1, Q2: Integral von -2 Im(psi* psi_t) links bzw. rechts von m, Absorber ausgenommen, psi_t zentral.
  Zum Vergleich Q1_null, Q2_null mit fester Grenze x = 0. Schwerpunkte X1, X2 = ladungsgewichtete Orte je Seite.
- Phasen ph_i = arg psi(p_i) (interpoliert, abgewickelt); omega_i = -d ph_i/dt.

## Auswertung und Urteilsregeln (vor dem Lauf festgelegt)

- Delta_nom = sqrt(0,65) - sqrt(0,60) = 0,031629; Schwebungsperiode P = 2 pi/Delta_nom = 198,65.
- Fenster: Anfang [50, 50 + 2P] = [50, 447,3], Ende [T - 2P, T] = [2602,7, 3000] (gleiche Takte: P = 200 ersatzweise).
  Zeitdrittel [50, 1000], [1000, 2000], [2000, 3000].
- omega_i Anfang/Ende/je Drittel: lineare Fits der abgewickelten Phase im Fenster. Gleitend: Fenster 50, Schritt 5
  (berichtet, nicht gewertet).
- Pencil: matrix_pencil (K = 12) auf Signal minus Mittelwert; "dominant" = groesste Amplitude unter |Re| >= 0,005.
- Verschmolzen: Median von d ueber [T - 100, T] < 1,5.
- **S1** (H1/H2): in allen drei Dritteln | |Re_dom(S_mitte)| - Delta_nom | <= 1 % Delta_nom, und nicht verschmolzen.
- **S2** (H1/H2): |Q1_Ende - Q1_Anfang| < 5 % Q1_Anfang (Fenstermittel) UND in allen drei Dritteln
  | |Re_dom(Q1)| - Delta_nom | <= 5 % Delta_nom, und nicht verschmolzen.
- **S3** (H1/H2): | |Delta|_Ende - |Delta|_Anfang | / |Delta|_Anfang < 10 % (gemessene Fenster), und nicht verschmolzen.
  Zusaetzlich berichtet: Aenderung gegen Delta_nom.
- **S4** (H3/H4): dieselbe Aenderung >= 10 % oder verschmolzen.
- **S0** (C1/C2 und C3/C4): Phasenlage 0: min d ueber [0, 500] < D - 1 UND verschmolzen; Phasenlage pi: Median d ueber
  [T - 100, T] > D + 1. Beides noetig.
- Gitter: Ein Urteil gilt, wenn beide Gitter es tragen; sonst "offen (Gitter uneinig)".
- Stationaritaet (K1-K4): max |S(0, t) - S(0, 0)|/S(0, 0) bis T = 500 < 1e-8.
- Rand: erreicht ein Maximum |x| > 820, wird die Zeit vermerkt.

## Vorab-Abschaetzung der Code-Agentin (Schreibtisch, Hypothese [H], aendert keine Vorhersage)

- Kraft zwischen den Baellen aus dem Impulsfluss T_xx im Mittelpunkt (Schwanznaeherung U ~ S): Kreuzterm
  2 f_a f_b (1 + k_a k_b - w_a w_b) cos(Phasendifferenz). Bei D = 6,6: f_a f_b(D/2) = 0,0496, also F ~ 0,074.
  Mit E_Ball ~ 2,6 Beschleunigung ~ 0,03. Bei Phasenlage 0 (anziehend) waeren die Baelle nach grob 15 bis 25 Einheiten
  zusammen, die Schwebungsperiode ist aber 199. Kennzahl a k/Delta^2 ~ 18 >> 1: Bei D bewegen sich die Baelle innerhalb
  einer Schwebung stark. Erwartung der Code-Agentin [H]: Zusammenstoss frueh im ersten Viertel der Schwebung; S1 und S3
  dann gefaehrdet. Bei D = 14,6 (Zusatz) ist die Kennzahl ~ 0,14 (schwache Kopplung).

## Ablauf

- Code per rsync nach /home/fmh/fmhc-physics-remote/runde23-schwebungsuhr/, Laeufe ueber kleintest.sh auf den Spuren cpu,
  cpu2, cpu3, cpu4, cpu6, je Aufruf ein Lauf (< 600 s). Ausgaben lauf/<name>.json und .roh.npz, Logs lauf/<name>.log.
- Literatur (L4) erst nach allen Laeufen.
