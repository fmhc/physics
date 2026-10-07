# GUERTEL-FELD-STAB-1: Plan (Runde 42; Sattel oder Rast?)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 19:00:04 CEST (date). Code 19:07 bis 19:10 CEST;
  Plantext ab 19:11:11 CEST (date), vor jedem Hauptlauf. Zeitbox 75 min, also bis 20:15:04 CEST.
- Karte: KARTE.md (GS0, GS1; Rechnung, Vorhersage, Ableitbarkeitsprobe, Scheitern und Bedeutung woertlich aus
  GUERTEL-2). Daran aendert dieser Plan nichts. Festlegungen [F] machen die Karte rechenbar; Zusaetze sind als
  **Zusatz** markiert und nicht urteilsbildend.
- Kennzeichen: [M] Mathematik; [E] Rechnung im Modell; [L] Literatur oder Gedaechtnis; [H] Hypothese; [F] Festlegung
  dieses Plans; [R] im Rauchlauf gesehen. Alles ist eine synthetische Modellrechnung, keine Messdatenbestaetigung.
- Bezugswerte (GUERTEL-2, Nachtrag N1, eingaben-n1/feld-3d-r12-R24-prot-saat.json, Kopie, per jq gelesen):
  E_schritt(420) = 14642,4466 (Sonde 0,612); E_schritt(450) = 16725,5839 (0,521); E_gitter(450) = 16722,3747
  (0,489; fmax nach FIRE 150 noch 4,8e-4, also nicht auskonvergiert); E_gitter(270) = 6161,0577;
  E_schritt(300) = 7585,2077.

## 0. Ableitbarkeit und Dimensionen (vorab)

1. **Kontinuum, radiales Profil [M]:**
   - Die Vorwaertsverdrillung liegt in SU(2) auf dem Grosskreis durch 1 und z: q(r) = cos phi + z sin phi, mit
     phi = 0 am Rand und Phi = theta/2 am Kern. Die Euler-Lagrange-Gleichung ist (r^(d-1) phi')' = 0.
   - Zweite Variation fuer eine Stoerung eta(r) u senkrecht dazu (u fester Einheitsvektor in span(x, y)): mit
     c = r^(d-1) phi' gilt d2E = c Integral_0^Phi (eta_phi^2 - eta^2) dphi, eta(0) = eta(Phi) = 0.
   - Kleinster Eigenwert (pi/Phi)^2 - 1; negativ genau fuer Phi > pi, also theta > 360 Grad (konjugierter Punkt).
     Instabile Mode eta = sin(pi phi/Phi). Werte: theta = 420: (180/210)^2 - 1 = -0,27; theta = 450:
     (180/225)^2 - 1 = -0,36 (in Einheiten von c). Der Ast ist im Kontinuum also ein Sattel, die Instabilitaet ist
     schwach.
   - Das gilt fuer radiale Profile in d = 1, 2 und 3 gleich; nur c haengt von d ab.
   - **Endpunkt:** kurzer Bogen von 1 nach q_z(theta) = q_z(theta - 720 Grad). Wegen der Symmetrie q -> q quer (die
     Energie haengt nur von q_a . q_b ab; Gitterkugel und Energie sind auch auf dem Gitter invariant) gilt
     E_min = E(720 - theta), auf dem Gitter exakt gleich der relaxierten Vorwaertsverdrillung bei 720 - theta.
   - **Gittersprung:** Er wechselt die SU(2)-Klasse. Danach ist das Feld effektiv glatt mit Kern
     -q_z(theta) = q_z(theta - 360 Grad); voll relaxiert E(60) bzw. E(90) (691,7), mit moeglichen Zwischenzustaenden
     (N1: 13178 bei 540 Grad).
2. **Der Stoss [M]:** Abschnitt 2 erzeugt fuer kleines eps eta(r) = eps sin(pi f_i) sin(beta/2) >= 0, nur in der
   inneren Haelfte, entlang des festen Vektors u = q_z(theta/2) x. Das hat einen positiven Anteil an der instabilen
   Mode. Allein auf der inneren Haelfte (Laenge Phi/2 < pi) waere die Stoerung stabil; wachsen kann nur ihr Anteil an
   der globalen Mode.
3. **Nicht ableitbar [E, Gegenstand der Rechnung]:**
   - ob das Gitter (Bindungswinkel bei 450 Grad bis 2,1 rad, Karte) den Ast metastabil macht;
   - ob der Stoss ohne Gittersprung durchlaeuft;
   - wie schnell das in FIRE 3000 geschieht.
4. **Dimensionen (AGENTS.md):**
   - **Innere Symmetrie:** gerechnet wird nur SO(3). Fuer ein SO(2)-Feld (Ebene der Werte) gibt es keine
     Kipprichtung; pi_1(SO(2)) = Z schuetzt die Verdrillung, eine Staley-Richtung existiert nicht. Die Frage ist dort
     leer [M]. GUERTEL-2 (GZ4) [E] zeigte das Anwachsen um etwa k^2 auf (16, 64). Hier nicht gerechnet.
   - **Raum:** gerechnet wird nur das Z^3-Kugelgitter. Die Kontinuumsaussage in Punkt 1 gilt radial fuer d = 1, 2, 3
     [M]. Die Gitterwinkel skalieren dagegen verschieden (3D etwa theta/(r0 (1 - r0/R)), 2D theta/(r0 ln(R/r0)),
     GUERTEL-2 B1). Das Gitterergebnis wird deshalb nicht auf 1D oder 2D uebertragen.
   - Der Stoss prueft eine Richtung. Auch ein "faellt zurueck" waere kein voller 3D-Stabilitaetsnachweis.

## 1. Protokoll und GS0 [F]

- code/stab.py, Modus prot. Feld, FIRE, Praediktor, Rauschen und setze stammen unveraendert aus guertel2.py (Kopie,
  sha256 c9374a98...). protokoll() ist eine wortgleiche Kopie von g2.feld_protokoll; zusaetzlich speichert sie
  Zustaende.
- Parameter wie N1: dim 3, r0 = 12, R = 24, Schritt 10 Grad, FIRE 30 je Schritt, Gitterwinkel alle 90 Grad mit
  FIRE 150, ftol 1e-5, dtmax 0,1, Rauschen 1e-3, Saat default_rng([42, 3, 120, 24]).
- Abweichung: tmax = 450 statt 720. Die Zufallsfolge bis 450 Grad ist dieselbe.
- Gespeichert werden die Zustaende bei 270 (nach Gitter-FIRE), 300 (Schritt), 420 (Schritt; kein Gitterwinkel) und
  450 (nach Gitter-FIRE).

## 2. Stoss in Staley-Richtung [F]

- **Innere Haelfte** wie in GUERTEL-2: h >= 1/2, f_i = clip(2h - 1, 0, 1); h harmonisch, auf (12, 24) also
  h = 24/r - 1, Naht bei r = 16.
- **Kippprofil** delta(r) = eps sin(pi f_i): 0 an der Naht und am Kern, eps in der Mitte der inneren Haelfte (h = 3/4,
  r etwa 13,7). Groesster Kippwinkel = eps (rad).
  - Begruendung: Ein gleichfoermiges Kippen braeche das Feld am Kern. Der Kern ist fest bei q_z(theta), und fuer
    theta ungleich 720 haengt sein Wert von der Achse ab. Das gaebe einen Sprung an den Kernbindungen, wo die
    Bindungswinkel am groessten sind, und koennte einen kuenstlichen Gittersprung ausloesen.
- **Operation:** q -> q_s q_y(delta) q_s^-1 q q_y(-delta), q_s = q_z(theta/2). Fuer den idealen Zustand
  q = q_s q_z(beta) ergibt das q_s q_n(beta) mit n = (sin delta, 0, cos delta): Die Achse kippt um delta von z nach x.
  Angewandt auf den relaxierten Protokollzustand. Kern, Rand und aeussere Haelfte bleiben, danach setze.
- **Laeufe:** eps = 0,01, 0,1 und 0,3 bei theta = 420 und 450 (sechs Stoesse).
- **Zusatz (nicht aus der Karte, nicht urteilsbildend):**
  - Kontrolle eps = 0 bei 420 und 450: FIRE 3000 ohne Stoss. Zerfaellt oder springt der Ast von selbst?
  - Referenzen: FIRE 3000 ab den Protokollzustaenden bei 300 und 270. Daraus E_ref(720 - theta); damit wird
    "E(720 - theta)" auf demselben Gitter zahlenmaessig bestimmt.

## 3. Relaxation und Sonde [F]

- FIRE wie g2.fire_feld (fire_log ist eine wortgleiche Kopie mit Aufzeichnung): hoechstens 3000 Schritte,
  ftol 1e-5, dtmax 0,1, dtstart 0,02, Schritt je Platz <= 0,05, B = 1.
- **Gittersprung-Sonde** wie GUERTEL-2: min ueber Bindungen q_a . q_b, an jedem Schritt. "Ohne Gittersprung" heisst:
  das Minimum ueber den ganzen Lauf (einschliesslich des Zustands direkt nach dem Stoss) ist > 0.
- **Je Schritt aufgezeichnet:** E, Sonde, fmax, Kipp-Amplitude P = sqrt(Summe ueber freie Plaetze von q1^2 + q2^2).
  P misst den Anteil ausserhalb der (1, z)-Ebene; Vorwaerts- und Rueckwaertsast haben ideal P = 0.
- **Struktur am Ende:**
  - mittleres q_z der aeusseren Haelfte (h < 1/2): vorwaerts > 0, umgekehrt < 0;
  - min q0;
  - q entlang der +x- und der +z-Achse.

## 4. Urteilsregeln [F] (mechanisch in code/auswertung.py)

- **Groessen je Lauf:**
  - E_Ast(theta) := E des Protokollzustands bei theta vor dem Stoss.
  - E_ref := E am Ende des Referenzlaufs bei 720 - theta. Nur gueltig, wenn dessen Sonde im Lauf > 0 ist; sonst ist
    GS1 nicht auswertbar.
  - rho := (E_end - E_ref) / (E_Ast - E_ref).
  - P_0, P_end: Kipp-Amplitude direkt nach dem Stoss und am Ende.

| Klasse | nach Plan | nach Kartenwortlaut |
|---|---|---|
| sprung | Sonde im Lauf <= 0 | gleich |
| umgekehrt | kein Sprung, rho <= 0,10 und mittleres q_z aussen < 0 | kein Sprung und abs(E_end - E_ref) <= 0,10 E_ref ("etwa E(720 - theta)") |
| ast | kein Sprung, rho >= 0,90 und P_end <= P_0 (Stoss abgeklungen) | kein Sprung und abs(E_end - E_Ast) <= 0,10 E_Ast ("faellt in den Ast zurueck") |
| dazwischen | sonst (auch rho >= 0,90 mit wachsendem P: langsam unterwegs) | sonst |

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| GS0 | abs(E_neu - E_N1)/E_N1 <= 1e-6 fuer E_schritt(420), E_schritt(450), E_gitter(450), und die Sonde ist an allen drei > 0 ("gueltig nach N1") | nur die drei Energien auf 1e-6 relativ |
| GS1 | eingetroffen: alle sechs Stoesse "umgekehrt"; nicht eingetroffen: mindestens ein Stoss "sprung" oder "ast" (Scheitern der Karte); sonst nicht entschieden | dasselbe mit den Wortlaut-Klassen |

- Die Kontrollen eps = 0 werden klassifiziert, sind aber nur beschreibend.
- **Ebenfalls beschreibend:**
  - E bei den Schritten 0, 250, 500, 1000, ..., 3000;
  - erster Schritt mit Gittersprung;
  - P_max und dessen Schritt;
  - Bild energie-verlauf.png (E, Sonde und P ueber die FIRE-Schritte, je theta).

## 5. Laufplan [F]

- Nur .69, ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu3 und cpu5. Je Lauf <= 10 min
  (RuntimeMaxSec 600), 1 Thread, Logs mit absolutem Pfad. Ordner /home/fmh/fmhc-physics-remote/guertel-feld-stab-1/
  (code/, rauch/, lauf/, eingaben-n1/).
- **Rauchlauf:** Protokoll bis 20 Grad; Stoss bei 20 Grad (eps 0,3, 100 Schritte; eps 0, 60 Schritte); Referenz bei
  10 Grad; Auswertung mit --thetas 20. Kein Wert bei 270 bis 450 Grad wird dabei erzeugt oder angesehen.
- **Hauptlaeufe** (eingefrorener Code, je genau einmal):
  - cpu3: prot (tmax 450), dann Stoss 450 mit eps 0,01, 0,1, 0,3, danach Kontrolle 450 eps 0, danach Referenz 270
    eps 0.
  - cpu5 (wartet auf prot): Stoss 420 mit eps 0,01, 0,1, 0,3, danach Kontrolle 420 eps 0, danach Referenz 300 eps 0.
  - Danach die Auswertung auf cpu3.
- Bricht ein Lauf ab (Zeit, Absturz), wird er mit Grund als Nachtrag wiederholt. Die Werte des abgebrochenen Laufs
  sehe ich nicht an.

## Rauchlauf und Festlegungen vor dem Einfrieren [R]

- Rauchlaeufe 17:10:44 bis 17:11:08 UTC, Spur cpu3, fuenf Units, alle rc = 0.
- **Laufzeit:** 100 FIRE-Schritte 6,0 s, 60 Schritte 3,6 s; Protokoll bis 20 Grad 3,8 s. Also etwa 60 ms je Schritt
  (B = 1). Erwartet:
  - FIRE 3000 etwa 3 min je Lauf;
  - Protokoll bis 450 Grad (etwa 2100 FIRE-Schritte) etwa 2,1 min;
  - alles unter 10 min.
- **Gesehen:** nur Laufzeit, Codepfad und die Werte bei 10 und 20 Grad.
  - Bei 20 Grad steigt E durch den Stoss eps = 0,3 von 34,34 auf 36,21; P steigt von 0,017 auf 0,80, an 9924 Plaetzen.
  - Nach 100 Schritten ist der Stoss abgeklungen: E 34,20, P 0,008, Klasse "ast".
  - Das Bild hat den erwarteten Aufbau.
- **Keine Aenderung** an Code oder Plan nach dem Rauchlauf.
