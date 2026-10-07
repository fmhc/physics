# PHASE-WAND: Plan (Runde 26, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 03:54:55 CEST (date).
- Plan geschrieben ab 04:17:48 CEST (date), nach den Rauchlaeufen (Abschnitt 8), vor jedem echten Lauf und vor jedem
  Vergleich der Formel mit den bekannten Sprossen. Zeitbox 120 min (bis 05:54:55 CEST).
- Ordner: lokal coordination/runden-v3/RUNDE-26/phase-wand/ (code/, lauf-69/, rauch-69/); .69:
  /home/fmh/fmhc-physics-remote/runde26-phase-wand/ (phase_wand.py, leiter_1d_beta.py, start*.sh, lauf/, rauch/).
- Markierungen: [K] Wortlaut der KARTE, [L] Vorgabe der Leitung im Auftrag, [A] Festlegung des Code-Agenten,
  [H] Hypothese.

## 1. Karte (bindend, unveraendert) [K]

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PW1 | beta = 1/2: Die Formel trifft die bekannten Sprossen 3 bis 5 (eps < 1e-4) innerhalb +-2 % in ln(1/eps) und mit der richtigen Paritaet | 60 % |
| PW2 | beta = 1: Es gibt 1D-Sprossen; die zwei kleinsten-eps-Schritte liegen innerhalb +-5 % von 1,3093 | 60 % |
| PW3 | beta = 1: Die eingefrorene Formel trifft jede Sprosse mit eps < 1e-3 innerhalb +-3 % in ln(1/eps), mit richtiger Paritaet | 45 % |

- Bedeutung (vorab, Karte):
  - PW1 und PW3 treffen ein: Die ebene Wand liefert Abstand und Lage der Leiter ohne Eichung (in 1D). Damit sind theta
    und c des Papiers im Duennwandgrenzfall berechnet statt geeicht [H, 1D].
  - PW1 trifft ein, PW3 nicht: Die Formel ist bei beta = 1/2 brauchbar, aber nicht uebertragbar. Beschreiben, z. B.
    Endlichkeitskorrekturen oder eine falsche Phasenkonvention.
  - PW2 trifft nicht ein: Die 1D-Leiter bei beta = 1 fehlt oder liegt ausserhalb. Beschreiben.

## 2. Formel und Konventionen [A]

### 2.1 Exaktes 1D-Profil

- Modell M1, U = S - S^2 + beta S^3, S = f^2, omega^2 = omega_min^2 + eps, omega_min^2 = 1 - 1/(4 beta), S_c = 1/(2 beta).
- Erste Integralform: S'^2 = 4 S^2 g(S) mit g(S) = 1 - omega^2 - S + beta S^2 = beta (S_c - S)^2 - eps.
- Wurzeln von g: S_-+ = S_c -+ sqrt(eps/beta) = [1 -+ sqrt(1 - 4 beta (1 - omega^2))]/(2 beta). Das Profil startet bei
  S = 0 und erreicht zuerst die **kleinere** Wurzel: S0 = S_c - sqrt(eps/beta). Das bestaetigt die Berichtigung aus
  RUNDE-25 fuer allgemeines beta.
- Geschlossene Form: u = 1/S erfuellt u'^2 = 4 (m2 u^2 - u + beta) mit m2 = 1/(4 beta) - eps. Die Loesung ist
  u = (1 + a cosh(b x))/(2 m2), also
  - S(x) = 2 m2/(1 + a cosh(b x)), a = 2 sqrt(beta eps), b = 2 sqrt(m2).
  - S(0) = 2 m2/(1 + a) = (1 - a)/(2 beta) = S0. Fuer beta = 1/2 ist das die RUNDE-25-Form.
  - beta = 1: S(x) = (1/2 - 2 eps)/(1 + 2 sqrt(eps) cosh(sqrt(1 - 4 eps) x)), S0 = 1/2 - sqrt(eps).
- Kontrolle im Lauf (k0): Reste der ersten Integralform und der Bewegungsgleichung, Quadratur x(S) gegen die
  geschlossene Form.

### 2.2 Wandlage

- Konvention [K]: S(x_w) = S_c/2.
- 1D, exakt: cosh(b x_w) = (1 - 8 beta eps)/(2 sqrt(beta eps)), x_w = arccosh(...)/sqrt(1/beta - 4 eps). Das gilt fuer
  eps < 1/(16 beta), sonst hat das Profil keine Wand (S0 < S_c/2). Asymptotisch: x_w ~ (sqrt(beta)/2) ln(1/(beta eps)).
- Ebene Wand: S(x) = S_c/(1 + exp(x/sqrt(beta))), also x_w = 0 in derselben Konvention.
- leiter_1d.py benutzt einen anderen Bezugspunkt x_s (S(x_s) = 2 m2/2) nur fuer den Integrationsstart und die Normierung.
  Das aendert keine Nullstelle; leiter_1d_beta.py behaelt ihn bei (bitgleiche Rechnung bei beta = 1/2).

### 2.3 Phase der ebenen Wand

- Innen (S = S_c) hat die symmetrische Matrix P_in die orthonormalen Eigenvektoren e1 (laufend, k = k_in) und e2
  (abklingend, kappa = kappa_in); Vorzeichen wie wand_beta.py (erste Komponente >= 0).
- z_p ist die Loesung bei rho_z mit A = e^(-q x) und B = 0 aussen. Bei rho_z hat sie innen keine wachsende e2-Mode
  (c_in(rho_z) = 0; RUNDE-24).
- Mit der Tiefe d = x_w - x gilt im Plateau:
  - e1.z_p = R cos(k d + phi)
  - e2.z_p = c+ e^(-kappa d) + c- e^(kappa d), mit c- = c_in
- **Definition:** Aus y1 = e1.z und y1' = e1.z' (Ableitung nach x) folgen theta = atan2(y1'/k, y1) = k d + phi und
  phi = (theta - k d) mod pi in [0, pi). Ein Vorzeichenwechsel von z_p oder e1 verschiebt phi um pi. Die Lagebedingung
  ist mod pi, also spielt das keine Rolle.
- **Bezug zur Karte:** Die Karte schreibt e1 cos(k_in (x - x_w) + phi_K). Es gilt cos(k (x - x_w) + phi_K) =
  cos(k d - phi_K), also phi_K = -phi (mod pi). Die Kartenform "k_in x_w = n pi - phi" gilt mit dem phi dieses Plans.

### 2.4 Lagebedingung in 1D (Herleitung)

- Das 1D-Profil ist gerade, die rechte Wand liegt bei +x_w(eps). Dort ist das Profil die verschobene ebene Wand, bis
  auf O(eps) und den Schwanz der linken Wand (2.6).
- Eine stille Stelle ist eine Loesung, die auf beiden Seiten in A abklingt und in B verschwindet. Die Loesung mit diesen
  Bedingungen rechts ist bis auf einen Faktor eindeutig. Aus der Spiegelsymmetrie folgt: Die stille Loesung ist gerade
  (z'(0) = 0) oder ungerade (z(0) = 0). Das sind die Bedingungen (F1, F2) der W-Abbildung von RUNDE-25.
- In der Mitte (x = 0, also d = x_w) gilt:
  - e1.z(0) = R cos(k x_w + phi) und e1.z'(0) = R k sin(k x_w + phi)
  - e2.z(0) = c+ e^(-kappa x_w) + c- e^(kappa x_w) und e2.z'(0) = kappa (c+ e^(-kappa x_w) - c- e^(kappa x_w))
- Gerade: sin(k x_w + phi) = 0 und c- = +c+ e^(-2 kappa x_w).
- Ungerade: cos(k x_w + phi) = 0 und c- = -c+ e^(-2 kappa x_w).
- Weil c-(rho) = c_in(rho) ~ c' (rho - rho_z), folgt rho_n = rho_z +- (c+/c') e^(-2 kappa x_w): Die Sprossen laufen
  exponentiell gegen rho_z. Die e1-Bedingung bei rho_z ist die Formel.
- Verbindung zum Verfahren von RUNDE-25 [A]: Auf der Linie F1 = 0 ist F2 in fuehrender Ordnung proportional zu
  sin(k x_w + phi) (gerade) bzw. cos(k x_w + phi) (ungerade). Die Vorzeichenwechsel von F2 liegen also an den Lagen der
  Formel.

### 2.5 Formel (wird so eingefroren)

- Phi(eps) = k_in(rho_z) x_w(eps) + phi.
- Lagen eps_m aus Phi(eps_m) = m pi/2 mit ganzem m; m gerade bedeutet gerade Mode, m ungerade ungerade Mode.
- Kein freier Parameter:
  - k_in und phi kommen aus der ebenen Wand bei omega_min(beta)
  - x_w(eps) kommt aus dem exakten Profil (2.2)
- Asymptotisch: ln(1/eps_m) ~ (2/(k sqrt(beta))) (m pi/2 - phi) + ln(beta). Der Schritt zwischen m und m + 1 ist
  pi/(k sqrt(beta)) = lambda pi/k_in, also 2,3100 bzw. 1,3093 (Karte).

### 2.6 Endlichkeitskorrekturen (nur Fehlerabschaetzung, nicht angepasst, ohne Einfluss auf Urteile)

- (a) Plateau-Absenkung durch den Schwanz der linken Wand (S_c - S0 = sqrt(eps/beta)):
  - dPhi_a ~ (e1.M.e1/(2 k)) S_c e^(-b x_w)/b, mit M = dP/dS bei S_c = ((5, 4), (4, 5)).
  - Groessenordnung sqrt(eps).
- (b) e2-Ueberlapp:
  - drho = +-(c+/c') e^(-2 kappa x_w), dPhi_b = (dk/drho x_w + dphi/drho) drho
  - Groessenordnung eps^(kappa/b) ln(1/eps)
- (c) O(eps): omega - omega_min, b(eps) und 2 m2 - S_c.
- d ln(1/eps) = -dPhi/(dPhi/d ln(1/eps)). (a) und (b) stehen je vorhergesagter Lage in formel-*.json.

## 3. Verfahren Phase (code/phase_wand.py, Kommando phase) [A]

- **rho_z:** brentq auf c_in, wie wand_beta.py: DOP853, rtol 1e-12, von x_b = 43 sqrt(beta) nach x_a = -36 sqrt(beta),
  xtol 1e-14. Die Klammer kommt aus der Konfigurationsdatei: R24-Wert +- 1e-5.
- **Phase:** Loesung bei rho_z mit DOP853 (rtol 1e-12) an den Tiefen d = 12, 14, ..., 24 sqrt(beta). Gewertet wird phi
  bei d = 20 sqrt(beta). Dort ist der Wandschwanz e^(-20) ~ 2e-9.
- **e2-Anteile:** c+ und c- je Tiefe; berichtet als |c-| e^(kappa d)/R (wachsend) und |c+| e^(-kappa d)/R.
- **Gegenproben** bei d = 20 sqrt(beta), je mit eigenem rho_z:
  - DOP853 mit rtol 1e-10
  - Gebiet x_b + 10 sqrt(beta)
  - klassisches RK4 mit festem Schritt h = 0,01 und 0,005 (reines Python, eigene Implementierung)
- **Ableitungen fuer 2.6:** c' = dc_in/drho, dphi/drho und dk/drho mit delta = 1e-6 und 1e-7.

## 4. Formel und Vergleich (phase_wand.py, Kommandos formel und vergleich) [A]

- **formel:**
  - alle m mit eps_m in [1e-8; 0,05], brentq in ln(1/eps) auf 1e-14
  - Monotonie von Phi auf 20001 Punkten geprueft
  - Ausgabe: m, Paritaet, ln(1/eps), eps, x_w, Abschaetzungen (2.6), K-Phase (Abschnitt 6)
- **vergleich:**
  - Je gerechnete Sprosse wird die naechste vorhergesagte Lage in ln(1/eps) gesucht, gleich welcher Paritaet.
  - "Getroffen" heisst: gleiche Paritaet und |d ln(1/eps)| <= Toleranz x ln(1/eps) der gerechneten Sprosse.
  - Gewertet werden die Sprossen im Wertungsbereich. Die Zuordnung muss eindeutig sein (keine zwei Sprossen auf
    dieselbe Lage). K0 der Sprossen-Datei und K-Phase muessen bestanden sein.
  - Berichtet, ohne Regel: vorhergesagte Lagen im Wertungsbereich ohne Partner.

## 5. Leiter bei beta = 1 (code/leiter_1d_beta.py) [A]

- **Aenderungen gegen leiter_1d.py** (sha256 f236d377..., RUNDE-25):
  1. --konfig (JSON) fuer jedes Kommando. Daraus kommen beta, omega_min^2, S_c, 9 beta, 6 beta, 3 beta, rho_z
     (Bezug), der Bezugsschritt, das Band, E0 (eps_j = 10^(E0 + j/40)), j_max, das Leiterfenster, der eps-Bereich, die
     k0-Stuetzstellen und G2-10 (nur beta = 1/2).
  2. par(eps): om = sqrt(omega_min^2 + eps), a = 2 sqrt(beta eps), Aa = 2 (1/(4 beta) - eps), b = sqrt(2 Aa).
     Bei beta = 1/2 ist das bitgleich (sqrt(4 y) = 2 sqrt(y) und 2 (0,5 - eps) = 1 - 2 eps exakt in IEEE).
  3. W = 1 - 4 S + 9 beta S^2, C = -2 S + 6 beta S^2 (W_physik, W_dop, ebene_wand_cin); omega_min^2 statt 0,5 in scan,
     rho_wurzel_lokal und verfeinere.
  4. ebene_wand_cin: S_c/(1 + e^(x/sqrt(beta))), Gebiet 43 und -36 sqrt(beta), W_in = 1 + 1/(4 beta),
     C_in = 1/(2 beta).
  5. k0: Profilproben fuer allgemeines beta (g(S) = beta (S_c - S)^2 - eps, U' = 1 - 2 S + 3 beta S^2,
     S0 = (1 - a)/(2 beta), Quadratur-Integrand 1/((S0 - u^2) sqrt(a + beta u^2)), beide Wurzeln, x_w der Formel).
     Stuetzstellen aus der Konfiguration; G2-10 nur bei beta = 1/2.
  6. aeste(): Das Fenster wird zur Laufzeit gelesen. In leiter_1d.py war es ein Vorgabeargument, also fest (1,30; 1,70).
  7. regel: K0 wie RUNDE-25. Gezaehlte Sprossen wie RUNDE-25. PW2 statt L1D-1 bis L1D-3. "Laufen zu rho_z" nur
     berichtet. Dekaden des Hauptasts ueber den ganzen Bereich.
- Bitgleich bei beta = 1/2: Im Rauchlauf ist das gezeigt (Abschnitt 8). Kontrolle C1 im echten Lauf: scan-h002 ueber
  j = 0 bis 252 gegen RUNDE-25 lauf-69/scan-h002.json (sha256 faae7982...).
- **Einstellungen bei beta = 1** (lauf/k-leiter-b1.json):
  - eps_j = 10^(-8 + j/40), j = 0 bis 280 (1e-8 bis 0,1)
  - Leiterfenster [1,50; 1,864] (rho_z = 1,77345; 1 + omega_min = 1,86603); n_rho = 2001
  - Uebersicht ueber das ganze Fenster (4001 Punkte, jedes vierte eps)
  - Stufen h = 0,02 und h = 0,01 (D = 30); Kontrollen D = 40 und DOP853-Newton
  - Umlauf-Rechteck rho +- 0,01, ln(1/eps) +- 0,5 (gleichparitaetige Nachbarn liegen ~2,6 auseinander)
- **Sprosse (gezaehlt), wie RUNDE-25:**
  - Die feine Stufe ist konvergiert, und es gibt eine grobe Entsprechung (gleiche Paritaet, |d l| < 0,3).
  - Die Stufen stimmen auf 1e-4 in ln(1/eps) und 1e-5 in rho ueberein.
  - Der Umlauf ist auf beiden Stufen aufgeloest, mit |U| = 1 und gleichem Vorzeichen.
  - Die Sprosse liegt im Leiterfenster, mit eps in [1e-8; 0,05].

## 6. Regeln (mechanisch) [A]

- **K-Phase** (je beta, Kommando formel):
  - wachsender e2-Anteil/R <= 1e-4 bei d = 20 sqrt(beta)
  - max |phi(d) - phi(20 sqrt(beta))| ueber d >= 16 sqrt(beta) <= 1e-5 rad
  - alle Gegenproben |d phi| <= 1e-5 rad
  - |rho_z - R24| <= 1e-8 (1,5241497621 bzw. 1,7734530718)
  - Phi monoton
  - Faellt K-Phase durch, ist der PW mit dieser Phase nicht auswertbar (= nicht eingetroffen).
- **PW1:** vergleich(formel-b05, RUNDE-25 lauf-69/auswertung.json, Feld sprossen_im_bereich, sha256 fc9307bb...).
  - Toleranz 0,02; gewertet eps < 1e-4 (die Sprossen 3 bis 5); mindestens 3 gewertete Sprossen.
  - Jede ist getroffen, die Zuordnung ist eindeutig, K0 (RUNDE-25) und K-Phase sind bestanden.
  - Die Sprossen 1 und 2 werden berichtet, nicht gewertet.
- **PW2:** regel(beta = 1).
  - K0: Profilreste <= 1e-10, Quadratur <= 1e-9, ebenes rho_z (RK4, h = 0,01 und 0,005) auf 1e-6 an 1,7734530718.
  - Mindestens 3 gezaehlte Sprossen in [1e-8; 0,05].
  - Die zwei Schritte mit den kleinsten eps liegen in [0,95; 1,05] x 1,3093 = [1,243835; 1,374765].
- **PW3:** vergleich(formel-b1 eingefroren, auswertung-b1, Feld sprossen_im_bereich).
  - Toleranz 0,03; gewertet 1e-8 <= eps < 1e-3; mindestens 1 gewertete Sprosse.
  - Jede ist getroffen, die Zuordnung ist eindeutig, K0 und K-Phase sind bestanden.
- **Auslegungen [A]:**
  - "innerhalb +-x % in ln(1/eps)" heisst: relativ zum ln(1/eps) der gerechneten Sprosse.
  - "mit richtiger Paritaet" heisst: Die naechste vorhergesagte Lage (gleich welcher Paritaet) hat die Paritaet der
    Sprosse. Das ist strenger als "naechste Lage gleicher Paritaet".
  - "die zwei kleinsten-eps-Schritte" heisst wie in RUNDE-25: die zwei Schritte mit den kleinsten eps.

## 7. Kontrollen (berichtet, keine Regel)

- C1: bitgleiche Wiederholung von RUNDE-25 scan-h002 mit leiter_1d_beta.py (beta = 1/2).
- Hauptast je Paritaet gegen rho_z(1), Uebersicht ueber das ganze Fenster, zwei Stufen, D = 40, DOP853-Newton.
- k0 bei beta = 1: RK4 gegen DOP853 und die ebene Wand mit demselben RK4.
- Phase: Tiefenverlauf, e2-Anteile, Gegenproben, Ableitungen.
- Schreibtisch [H], vor den Laeufen, aus Rauchlauf und 2.6:
  - Die Abweichung Formel minus Rechnung waechst mit eps und wechselt mit der Paritaet das Vorzeichen.
  - Abschaetzung (b) erklaert sie in Groesse und Vorzeichen; (a) ist kleiner.

## 8. Rauchlaeufe vor diesem Plan (ungueltig fuer jede Wertung; offengelegt)

- .69, 02:13:48 bis 02:16:41 UTC (rauch1.sh, rauch2.sh und ein Neustart von phase). Parameter in keinem echten Lauf:
  - beta = 0,6, h = 0,025, D = 25, eps_j = 10^(-6 + j/40), j = 0 bis 200, n_rho 801, Fenster [1,40; 1,76]
  - bei beta = 1/2 nur der RUNDE-25-Rauch-Scan (h = 0,025, D = 25, j = 232 bis 252, n_rho 501)
- **Code vor dem Einfrieren geaendert:**
  - phase: doppelte t_eval-Stelle (Tiefe 20 zweimal); der erste phase-Rauchlauf brach ab, rc = 1
  - danach: K-Phase in formel, K0- und Phasen-Tor in vergleich
- **Ergebnisse:**
  - selbsttest: 13 von 13.
  - beta = 1/2: Rauch-Scan bitgleich zu RUNDE-25 rauch-69/scanb.json (32 Wurzeln; rho, F2, F1-Rest, Ynorm, Iterationen).
  - phase bei beta = 0,6:
    - rho_z = 1,609558064742, k_in = 2,086473, kappa_in = 0,915797, phi = 2,448463
    - Streuung ueber d >= 16 sqrt(beta) 6,8e-8; Gegenproben <= 5,3e-8
    - wachsender e2-Anteil/R 2,4e-9; c' = -0,607
  - **Formel gegen Rauch-Leiter bei beta = 0,6 [offengelegt]:**
    - Fuenf Rauch-Sprossen bei eps = 6,1e-6 bis 9,9e-3.
    - Die Formel trifft alle mit richtiger Paritaet. Abweichungen in ln(1/eps), von kleinem zu grossem eps: -0,025 %,
      +0,097 %, -0,48 %, +2,0 %, -6,6 %.
    - Abschaetzung (b) gibt +0,0029, -0,010, +0,037, -0,13 und +0,41 in ln(1/eps); beobachtet sind +0,0030, -0,0097,
      +0,039, -0,12 und +0,30.
    - Danach habe ich an Formel, Konvention und Toleranzen nichts geaendert. Das Ergebnis bei 0,6 legt nahe, dass PW1
      wahrscheinlich eintrifft [H]. Die Karte setzte die Wahrscheinlichkeiten vorher.
  - Der Rauch-Vergleich selbst meldet "nicht eingetroffen", weil K0 der Rauch-Regel mit dem Platzhalter rho_z = 1,59
    durchfiel. Das Tor funktioniert also.

## 9. Laeufe (je Aufruf eine Kleintest-Einheit, 1 Kern, <= 600 s)

| Phase | Skript | Spur | Inhalt |
|---|---|---|---|
| A | startA.sh | cpu | phase beta = 1/2, formel b05, vergleich PW1 (lauf/r25-auswertung.json = RUNDE-25 auswertung.json) |
| A | startA.sh | cpu2 | phase beta = 1, formel b1 (Vorhersage) |
| Einfrieren | (Hand) | - | formel-b1.json: sha256, chmod a-w auf der .69 und lokal, date; erst danach Phase B |
| B | startB.sh | cpu, cpu2, cpu3, cpu4, cpu6 | k0 b1, dann C1 (Wiederholung beta = 1/2); scan-h002; scan-h001-a/-b; Uebersicht |
| C | startC.sh | cpu2, cpu3, cpu4 | sprossen h = 0,02; h = 0,01; h = 0,01 mit D = 40 |
| D | startD.sh | cpu6, cpu | dop853, regel (PW2) -> auswertung-b1.json, vergleich PW3 |

- startB.sh prueft selbst, dass formel-b1.json existiert und schreibgeschuetzt ist.
- Phase C startet nach rc = 0 aller Scans von B, Phase D nach C.
- Urteile in lauf/vergleich-pw1.json, auswertung-b1.json (PW2) und vergleich-pw3.json; zusammengefasst mit jq in
  lauf-69/urteile.json.

## 10. Zeitplan und Grenzen

- Keine geschaetzten Endzeiten. Faellt ein Aufruf aus (rc != 0) oder erreicht er 600 s: berichten. Ein Nachlauf nur als
  offen benannte Abweichung.
- Nach dem Einfrieren keine Aenderung an Plan, Code, Konfigurationen und Startskripten. Abweichungen offen mit Grund
  und Zeit im ERGEBNIS.

## 11. Code, Konfigurationen und Skripte (sha256, vor dem Einfrieren; lokal = .69)

```
c9add78215a755c33fd368ac7d154e190e4b3647dc78246882bb9dedb52f0397  phase_wand.py
eafe2404630b7557fd855d4d3e4812c2850038cc2d0524171b3b9df41591ff5f  leiter_1d_beta.py
7956c30d443b0a47f1999a89172687864cfc0250decb13c127bf50c9abfcd103  startA.sh
033da8ca99b22662a158b5bddff222d34720040eefa36d161de5d6770579a0e6  startB.sh
715bde046e175b36e630400a1d6822ab61c3d5fb8fbdf05ef75da0ddbbb3a045  startC.sh
9eef96b03d77c5382aede8bd911fa93b8fe585962e63c9e73af0fe96238bfe59  startD.sh
96bbb5afa7db1796c1b865a68f624bac226310e648444f64726da138b9e6a646  lauf/k-formel-b05.json
a83913f12ecda30b9f1e545eb9f1a9c4762a4a06f870cfcbedab4c8bf645fcb0  lauf/k-formel-b1.json
a016cfb48ec5957324476e25b08e8d68fbd0139dd2b3d9f14977fe168650ab68  lauf/k-leiter-b05.json
019e66666fe023c25367780740342b7f0f27c8ecc0109fed655d9180fc7b804b  lauf/k-leiter-b1.json
ea9b80c160faa5cb64af4a068b0214f3bc1bb9d73a80fd3abe31abecb2da07dd  lauf/k-phase-b05.json
9ca72d6c2fe0002dde9d97143bd61a69ceea36d314519c2a54ee25a7adbf2a28  lauf/k-phase-b1.json
dd2903debecb0f3ae38d1d58d70704883e2adebc6709c9fd8fa874d66d308d61  lauf/k-vergleich-pw1.json
5a767ef7df49add02a9a9a64205589806aee9aa221f12149f344befee4cae62d  lauf/k-vergleich-pw3.json
```

- RUNDE-25 lauf-69/auswertung.json = .69 lauf/r25-auswertung.json: fc9307bba538808ba37b157c2d2b8fd77d797ab6b5abf8502ab845896c78d861
- RUNDE-25 lauf-69/scan-h002.json (Kontrolle C1): faae7982b48f734561f1b52863793abc8c0a6461784fd476444293da111d26ae
