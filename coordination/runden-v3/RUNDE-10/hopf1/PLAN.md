# HOPF-1 (Runde 10): Plan, Schreibtischpruefung, Entscheidungsregeln

- **Schreibbeginn: 2026-09-30 10:48:07 CEST (date), vor jeder Rechnung dieser Karte.**
- Bearbeiter: Code-Agent HOPF-1 (Claude). Auftrag: Leitung claude-primary, Karte HOPF-1 in RUNDE-10.md.
- Modell: Codex B.5 (literatur-20260923/SPIN-KONSTRUKTION-codex.md, Zeilen 591 bis 690, gelesen).
- Die Vorhersage der Leitung (RUNDE-10.md, HOPF-1, eingetragen 10:37:41) wird hier **nicht geaendert**. Abweichungen
  der Schreibtischpruefung stehen unten als Vermerke D1 bis D7.
- Alles [H]. Klassische Rechnung: sagt nichts ueber Spin, Fermionen oder Quarks. Bindung ist nicht Stabilitaet.

## 1. Schreibtischpruefung (vor der Rechnung)

Energiedichte (statisch bzw. stationaer, Metrik +,-,-,-): Aus L folgt
H = |d_t phi|^2 + |grad phi|^2 + (v^2/4)(grad n)^2 + (kappa/2) sum_{i<j} H_ij^2 + mu^2 v^2 (1 - n3) + U(s) - gJ Re[(phi* b)^2].

- **D1 Kreuzterm: bestaetigt.** Mit a = S_phi, c = S_b:
  U(a+c) - U(a) - U(c) = -2ac + (1/2)[(a+c)^3 - a^3 - c^3] = -2ac + (3/2)ac(a+c) = a c [-2 + 1,5 (a + c)].
  Alle anderen Terme haengen nur von phi oder nur von n ab und heben sich in E[phi+n] - E[phi] - E[n] exakt weg
  (auch |d_t phi|^2: phi und damit Q sind im Produktansatz unveraendert). Also
  E_int = Int S_phi S_b [-2 + 1,5 (S_phi + S_b)] d^3x - gJ Int Re[(phi* b)^2] d^3x. Vorzeichen des gJ-Terms in der
  Energie: minus (L enthaelt +gJ Re[...]).
- **D2 gJ-Term: bestaetigt mit Einschraenkung.** Mit phi = f e^{-i omega t}: (phi* b)^2 = (v^2/4) f^2 e^{2 i omega t}
  (n1 + i n2)^2. Fuer beide verwendeten h = 1-Ansaetze ist (n1 + i n2)^2 proportional zu e^{2 i phi_az}.
  - Liegt das Ballzentrum auf der Knotenachse (Mitte, Radius-Reihe, Verschiebung entlang der Achse): Das Integral ist
    **exakt null** (Azimutintegral).
  - Liegt das Ballzentrum neben der Achse (Verschiebung in der Knotenebene): Das Integral G ist zu festem t im
    Allgemeinen **nicht null**. Es verschwindet im Zeitmittel (e^{2 i omega t}) und im Mittel ueber die innere Knotenphase.
  - Die Aussage (4) "raeumlich gemittelt nichts" gilt damit fuer koaxiale Lagen exakt, sonst nur im Zeit- oder
    Phasenmittel. Ein mit omega isorotierender Knoten neben der Achse koennte -|gJ| |G| gewinnen; das liegt ausserhalb
    des statischen Produktansatzes. G wird fuer die Verschiebung in der Knotenebene gemessen und berichtet.
- **D3 Mitte gegen Wand, Zahlenwert.** g(S) = S(-2 + 1,5 S) hat sein Minimum -2/3 bei S = 2/3; das stimmt. Die Mitte
  beider Baelle hat aber S0 > 1: fuer omega^2 = 0,7977 ist f0 = 1,02424 (KREIN-1-Profil), also S0 = 1,049; fuer
  omega^2 = 0,6 liegt S0 knapp unter dem Scheitel 1,088 (Formel (2 + sqrt(4 - 6(1 - omega^2)))/3).
  - Damit g(S0) = -0,447 (0,8) bzw. etwa -0,40 (0,6).
  - Die Mitte gibt also etwa 67 % bzw. 60 % der Wandbindung je Knotenmenge, nicht 75 %. Die Richtung von (2) aendert
    sich dadurch nicht.
- **D4 Lokale Abstossungsschwelle.** Lokal abstossend ist der Kreuzterm, wo S_phi + S_b > 4/3. Mit S_b <= v^2/4
  (Maximum auf der Schale n3 = 0) beginnt lokale Abstossung in der Ballmitte schon bei v^2/4 > 4/3 - S0: also
  0,28 (0,8) bzw. etwa 0,245 (0,6), nicht erst bei 1/3. Bei v = 1 (v^2/4 = 0,25) liegt die Mitte des grossen Balls an
  der Kante.
  - Entscheidend fuer (3) ist aber das Integral. Exakt gilt E_U(c) = c A1 + c^2 A2 mit c = v^2/4,
    A1 = Int S_phi s (-2 + 1,5 S_phi), A2 = Int 1,5 S_phi s^2 und s = n1^2 + n2^2.
  - Vorzeichenwechsel bei c* = -A1/A2.
  - Staerkste Bindung bei c*/2. Oberhalb davon waechst die Bindung mit v^2 nicht mehr, sie nimmt ab.
  - Fuer einen Knoten ganz in der Mitte des grossen Balls erwarte ich c* zwischen 0,25 und 0,45, je nach Schalenform
    (<s^2>/<s>). Punkt (3) ist dort also ein echter Test, kein sicherer Ausgang.
- **D5 Was koppelt.** b verschwindet an beiden Polen. Der Knotenkern (n3 = -1) koppelt nicht, nur die Schale
  n3 ~ 0 (Hinweis der Leitung aus SPIN-1 G1). "Roehre in der Wand" heisst hier: Die n3 = 0-Schale liegt in der Wand.
  Die Radius-Reihe laeuft deshalb mit der Knotengroesse relativ zum Ballradius durch Mitte, Wand und aussen. Je Lage
  wird <S_phi>_s = Int S_phi s / Int s berichtet, also wo die koppelnde Schale im Ball sitzt.
- **D6 Nachbemerkung zur Relaxation (Stufe B), Standardargument, [H].** Sind Ball (Minimierer bei festem Q) und Knoten
  (relaxierter h = 1-Knoten) exakte Einzelloesungen, so hat der Produktzustand dasselbe Q und dasselbe h. Deshalb gilt
  inf E(Q, h) <= E_Q + E_H + E_int^prod. Ein negatives E_int^prod bleibt also nach Relaxation als obere Schranke
  erhalten. Der Ansatz-Knoten ist aber kein Minimierer; das Argument greift erst mit relaxiertem Knoten. Ob ein
  Minimierer existiert, sagt es nicht.
- **D7 Radius des grossen Balls.** Duennwandformel R = 1/(2 sqrt(beta) (omega^2 - 1/2)) gibt fuer omega^2 = 0,6
  R ~ 7,1 (KREIN-1-Profil bei 0,6314: R_tw 5,4, r(S = 1/2) 5,6). Der Auftrag nennt "Radius etwa 5". Ich rechne mit
  omega^2 = 0,6 wie genannt und berichte den gemessenen Radius.

## 2. Rechnung Stufe A

- **Q-Ball:** Profil f(r) aus krein.py (KREIN-1, unveraendert importiert: Schiessen mit Bisektion, DOP853, danach
  analytischer Schwanz), tabelliert auf r = 0 bis 80, dr = 0,001. omega^2 = 0,6 (gross) und 0,8 (klein). Dazu Q, E_Q,
  S0, Radien bei S = 0,9 S0, S0/2, 2/3 und 0,1 S0.
- **Knoten h = 1, zwei Ansaetze:**
  - **A, Hopfabbildung** (Sutcliffe-Typ W = Z1/Z0): Z1 = (x + i y) sin f/r, Z0 = cos f + i z sin f/r,
    n1 + i n2 = 2 Z1 conj(Z0), n3 = |Z0|^2 - |Z1|^2. Profil f(r) = 2 atan(sinh(R_h/w)/sinh(r/w)): f(0) = pi,
    f(R_h) = pi/2, exponentieller Schwanz. Kernring bei r = R_h in der Ebene z = 0. Die n3 = 0-Schale schneidet die
    Ebene bei etwa R_h +- 0,881 w.
  - **B, kompakter Torus:** delta = Abstand zum Kernring (Radius R_h), Theta = pi (1 - delta/a) fuer delta < a, sonst 0.
    n1 + i n2 = sin Theta e^{i(phi_az + chi)}, chi = atan2(z, rho - R_h); a < R_h. Die n3 = 0-Schale liegt bei delta = a/2.
  - **Hopfzahl** beider Ansaetze numerisch pruefen: Whitehead-Integral h = (1/16 pi^2) Int A.B, mit B_i = (1/2)
    eps_ijk n.(d_j n x d_k n) und curl A = B per FFT.
- **Lagen:**
  - F1A, Radius-Reihe, Ansatz A, w = 0,75, gleiches Zentrum: R_h = 0,5 bis R_Ball + 4 in Schritten von 0,5. Deckt Mitte,
    Wand und "Knoten umschliesst den Ball" ab.
  - F1S, Radius-Reihe selbstaehnlich: w = R_h/2, feste Form, nur skaliert. Das entspricht einer kappa-Reihe, denn die
    Knotengroesse ist proportional zu sqrt(kappa)/v.
  - F1B, Radius-Reihe, Torus: a = 1,5, R_h = 2 bis R_Ball + 4.
  - F2z, Verschiebung entlang der Knotenachse: kleiner Knoten (A: R_h = 0,75, w = 0,35) und mittlerer Knoten
    (A: R_h = 1,5, w = 0,7), d = 0 bis R_Ball + 5 in Schritten von 0,5.
  - F2x, Verschiebung in der Knotenebene: kleiner Knoten; dient auch der gJ-Messung neben der Achse.
- **Groessen je Lage** (v-unabhaengig, daraus exakt fuer jedes v):
  - A1 und A2, auch aufgeteilt nach Region: innen S_phi > 0,9 S0; Wand 0,1 S0 < S_phi <= 0,9 S0; aussen S_phi <= 0,1 S0.
  - M_b = Int s (Knotenmenge), <g> = A1/M_b (Bindung je Knotenmenge), <S_phi>_s, c* = -A1/A2.
  - G = Int S_phi (n1 + i n2)^2 (komplex).
  - Gegenprobe der Algebra: fuer v = 0,5 und 1,0 direkt Int [U(S_phi + S_b) - U(S_phi) - U(S_b)] gegen c A1 + c^2 A2.
- **Gitter:**
  - 3D-Mittelpunktsgitter, Wuerfel um das Ballzentrum, Halbkante L = R_Ball + 9, zwei Stufen h = 0,2 und h = 0,1.
  - Fuer alle koaxialen Lagen zusaetzlich ein achsensymmetrisches 2D-Integral in (rho, z), h = 0,01, als dritte,
    unabhaengige Quadratur.
- **Rechenort:** .69 ueber kleintest.sh aus /home/fmh/fmhc-physics-remote/runde10-hopf1/. Rauchtest auf cpu6 (kleines
  Gitter); Hauptlaeufe p4000b (falls WM-1-MB nicht laeuft) oder p4000a, torch float64, je Aufruf <= 10 min.

## 3. Entscheidungsregeln (vorab, vor der ersten Zahl)

Sie legen fest, wie die Vorhersage der Leitung gelesen wird; die Vorhersage selbst bleibt unveraendert.

- **(1) Anziehung:**
  - Bestanden, wenn E_int(v) < 0 in allen Lagen mit Ueberlapp, beide Baelle, v = 0,5 und 1,0, feines Gitter.
  - Gescheitert, wenn in irgendeiner Lage E_int > 0 ueber dem Gitterfehler liegt.
- **(2) Wand vor Mitte.** Hauptmass: fester Knoten, verschoben (F2z, F2x).
  - Bestanden, wenn das Minimum von E_int(d) bei einer Lage mit S_phi(d) in der Wandregion liegt und E_int(0) > E_int(d_min).
  - Gescheitert ("Mitte bindet tiefer"), wenn d = 0 das Minimum ist.
  - Nebenmasse: <g> = A1/M_b in der Radius-Reihe (Knoten mit Schale in der Wand gegen kleinen Knoten in der Mitte),
    dazu das Gesamt-E_int der Radius-Reihe.
  - Verhaeltnis Mitte/Wand: E_int(0)/E_int(d_min) gegen die 75 % der Leitung (D3 erwartet 60 bis 67 %).
- **(3) v-Abhaengigkeit:**
  - Bestanden, wenn |E_int(v = 1)| > |E_int(v = 0,5)| und c* >= 1/3 in allen Lagen.
  - Gescheitert, wenn eine Lage fuer v^2/4 < 1/3 positiv wird (c* < 1/3). Das ist exakt aus A1, A2, kein Extrapolieren.
  - Berichtet werden min c* ueber alle Lagen und die Lage dazu.
- **(4) gJ-Term:**
  - Bestanden, wenn |G| fuer koaxiale Lagen auf Rundungsniveau null ist (|G| < 1e-10 |A1|).
  - Neben der Achse wird |G| gemessen. Der Beitrag gJ c Re[G e^{2 i omega t}] ist im Zeitmittel exakt null. Berichtet
    wird max |gJ c G| / |E_U| mit |gJ| = 4(sqrt 2 - 1) = 1,657 (Codex' Schranke).
- **Gitter:**
  - Gut, wenn h = 0,1 und die 2D-Quadratur auf 1 % (relativ) uebereinstimmen.
  - Sonst werden nur die 2D-Werte (koaxial) berichtet und die 3D-Werte als "unsicher" markiert.

## 4. Stufe B (nur wenn Stufe A in unter 60 min Code steht, also bis etwa 11:48)

- Gradientenfluss fuer n mit Normzwang, phi fest ("mitgefuehrt"), koaxiale Startlage. Das Zentrum bleibt dann aus
  Symmetriegruenden fest, der Ringradius ist frei.
- Parameter: v = 1, mu = 1, kappa so, dass der relaxierte Knoten in etwa die gewuenschte Groesse hat.
- Vergleich mit demselben Fluss ohne Ball, gleiche Schrittzahl.
- Fragen: Bleibt E_int < 0? Wandert der Ringradius zur Wand oder zur Mitte?
- Sonst "offen" mit Kostenschaetzung.

## 5. Protokoll

Nachgetragen 2026-09-30 11:25:03 CEST (date). Laufzeiten aus kleintest.sh, UTC auf der .69 (CEST = UTC + 2).

- **Hinweise der Leitung waehrend der Arbeit:**
  - Aus SPIN-1: Nur die Schale n3 ~ 0 koppelt; die Knotengroesse relativ zum Ballradius mitvariieren; E_int nach
    innen, Wand und aussen aufteilen. Beides umgesetzt: Radius-Reihen F1A, F1S, F1B und Regionen in hopf1.py.
  - Abstimmung mit Codex: Die zentrierte Relaxation macht Codex, Stufe B hier nur aussermittig "falls billig";
    Vergleich mit Codex' zentriertem Wert in ERGEBNIS.md, Abschnitt 6.
  - Die Vorhersage blieb unveraendert.
- **Laeufe Stufe A (hopf1.py):**
  - Rauchtest cpu6: 08:52:46 bis 08:52:52.
  - Zeittest p4000a (nur F1A): 08:53:45 bis 08:54:06.
  - omega^2 = 0,6, p4000a: 08:54:31 bis 08:56:25, 177 Lagen.
  - omega^2 = 0,8, p4000a: 08:56:25 bis 08:56:55, 106 Lagen.
  - Alle rc = 0.
- **Laeufe Stufe B (verworfen, siehe ERGEBNIS.md, Abschnitt 7):**
  - hopf1b.py in 3D:
    - Rauchtest cpu6: 09:02:53 bis 09:04:39, rc = 1 (Formatfehler bei NaN; der Knoten war auf h = 0,25 schon abgewickelt).
    - p4000a L-BFGS: 09:05:31 bis 09:07:20.
    - p4000a Fluss: 09:08:41 bis 09:11:31, von mir per `systemctl --user stop` des eigenen Units gestoppt.
  - hopf1c.py in 2D, cpu6:
    - Fluss dt = 0,004: 09:13:01 bis 09:14:15.
    - Fluss mit festem Rand, dt = 0,003: 09:15:19 bis 09:16:55.
    - L-BFGS mit festem Rand: 09:17:42 bis 09:18:08.
    - Fluss dt = 0,001: 09:18:44 bis 09:20:22.
- **Regelvermerk:** Einmal lief awk auf der .69 innerhalb eines ssh-Befehls, nur als Zeilenfilter fuer eine Logdatei,
  nicht lokal. Lokal lief kein Interpreter; der Rauchtest lief ebenfalls auf der .69 (cpu6).
