# KOLL-1 Plan: kollektive Atmungswellen zweier (dreier) Q-Baelle an der stillen Stelle

- Runde 9 (v3), Karte KOLL-1. Bearbeiter: Code-Agent (Anthropic, Opus). Auftrag: Leitung claude-primary, 07:07.
- Anlass: Finn 07:05 "können die teilchen klumpen ggf muster erzeugen die dann schwingungen weiter geben die
  übergeordnet sind?"
- **Plan geschrieben ab 2026-09-30 07:22:55 CEST (date), vor jeder Rechnung dieser Karte.** Gelesen vorher: RUNDE-07.md,
  RUNDE-08.md, RUNDE-09.md, THEORIE-ATMUNGS-NULLSTELLEN.md (Abschnitte 1 bis 4), bic2.py (Kopf), kurve-Bericht
  lauf-lokal/aus-kurve-050, R-2-Abschnitt in RUNDE-06/ERGEBNISSE-R6-A.md, Codex bic-amplitude (ERGEBNIS, PLAN, run.py).
  mode.npz nicht geoeffnet.
- Explorativ. Alles unten ist Hypothese [H] oder Schreibtisch-Schaetzung (Hand), bis ein Lauf es belegt.

## 1. Gleichungen

- Feld: L = |phi_t|^2 - |grad phi|^2 - U(S), U = S - S^2 + S^3/2, S = |phi|^2. Bewegung: phi_tt = lap phi - U'(S) phi,
  U'(S) = 1 - 2S + 1,5 S^2.
- Ball: phi = f(r) e^{i omega t}; f'' + 2 f'/r = (U'(f^2) - omega^2) f; Schwanz f -> A e^{-k0 r}/r, k0 = sqrt(1 - omega^2).
- Linearisierung (eigene Konvention, e^{+i omega t}): phi = e^{i omega t} [F + chi], chi = u e^{i rho t} + v e^{-i rho t}.
  Fuer reelles F und reelle u, v:
  - (-lap + dp - (omega + rho)^2) u + sp v = 0 (offener Kanal, q = sqrt((omega + rho)^2 - 1))
  - (-lap + dp - (omega - rho)^2) v + sp u = 0 (geschlossener Kanal, kappa_c = sqrt(1 - (omega - rho)^2))
  - dp = 1 - 4S + 4,5 S^2, sp = -2S + 3S^2. Das ist bic2s System (dort e^{-i omega t}, Im rho < 0).
- Zwei Baelle: F = F_A + sigma F_B, sigma = -1 (gegenphasig). F bleibt reell, also haengt der Operator nur von
  S_0 = F^2 ab; sigma steckt nur in den Kreuztermen 2 sigma F_A F_B.
- **Kopplungsmodentheorie (Hand, LCAO fuer das quadratische Eigenproblem T(rho) psi = 0, T symmetrisch):**
  - psi = a psi_A + b psi_B. Mit V = [[dp - 1, sp], [sp, dp - 1]] (haengt nicht von rho ab) und
    d T/d rho = diag(-2(omega + rho), 2(omega - rho)):
  - Krein-Norm N = 2 Int[(omega + rho) u^2 + (rho - omega) v^2] d^3x > 0.
  - Sprung (Huepfintegral) t_AB = Int psi_B^T V_A psi_A d^3x, gemeinsame Verschiebung Delta = <psi_A, (V - V_A) psi_A>.
  - Moden rho_+- = rho_0 + (Delta +- t_AB)/N, also **J = t_AB / N**, volle Uebergabe A -> B nach t_tr = pi/(2|J|).
  - Asymptotik (Hand, Greensche Formel, s-Wellen-Anteil des Yukawa-Schwanzes von psi_B am Ort A):
    **t_AB ~ -4 pi C_v^2 e^{-kappa_c d}/d**, mit v(r) -> C_v e^{-kappa_c r}/r. Vorzeichen negativ fuer jedes sigma: die in
    chi symmetrische Mode liegt tiefer. Fuer sigma = -1 heisst das im Dichtebild delta S: Gegentakt (A dehnt, B zieht
    sich zusammen) liegt tiefer.
  - Offener Kanal: am Resonanzpunkt kommt ueber die auslaufende Welle ein komplexer Anteil J_rad ~ Gamma e^{-iqd}/(qd)
    hinzu (Dicke-artig; Betrag Gamma/(qd)). An der stillen Stelle ist A_out = 0, also J_rad = 0 in linearer Ordnung.
  - Verstimmung: Die Paar-Moden schwingen bei rho* +- J, also neben der stillen Frequenz. Nach dem Phasenbild
    (Theorie 4.1) strahlen sie dann mit Gamma_koll ~ C_rho J^2, C_rho ~ C (drho/dPhi-Verhaeltnis)^2 ~ 0,03 (Hand).
- Zahlen der Punkte (aus kurve-050 und Theorie; Hand):

  | Punkt | omega | rho | Gamma | q | kappa_c | k0 |
  |---|---|---|---|---|---|---|
  | still, omega^2 = 0,7976768 | 0,893128 | 1,7446175 (reell) | 0 (linear) | 2,4408 | 0,52437 | 0,44980 |
  | Vergleich, omega^2 = 0,76 | 0,871780 | 1,728147 | 1,988e-3 | 2,3999 | 0,51636 | 0,48990 |

## 2. Vorab-Erwartungen (Hand, 2026-09-30 07:22:55 CEST, vor jeder Rechnung)

Schaetzung von K = 4 pi C_v^2/N: Mode sitzt als Schalenzustand in der Wand (R ~ 2,9 bis 4, Breite ~ 1,5); mit
u_w ~ v_w folgt K ~ 2, Spanne 0,5 bis 6 (Verhaeltnis v/u und Anschlussradius unbekannt). Also |J| ~ K e^{-kappa_c d}/d.

| Groesse | d = 10 | d = 12 | d = 14 |
|---|---|---|---|
| e^{-kappa_c d}/d, still | 5,3e-4 | 1,5e-4 | 4,6e-5 |
| **\|J\| still** (K ~ 2, Faktor 4 in jede Richtung) | ~1e-3 | ~3e-4 | ~1e-4 |
| **t_tr = pi/(2\|J\|) still** | ~1500 (400 bis 6000) | ~5000 | ~16000 |
| \|J_ev\|(0,76) / \|J_ev\|(still) | 1,0 bis 1,3 (kappa_c kleiner, Mode aehnlich) | | |
| \|J_rad\| = Gamma/(qd) bei 0,76 | 8e-5 | 7e-5 | 6e-5 |

- **E1 (Verlust, gehaltene Baelle, linear):**
  - still: Energieverlust pro Uebergabe unter 1e-2 (Gamma_koll ~ 0,03 J^2 ~ 3e-8, Gitter- und Verschiebungsreste unter
    1e-5). B erreicht mindestens 0,9 der Anfangsamplitude von A.
  - 0,76: exp(-pi Gamma/|J|) mit Gamma/|J| ~ 2 bei d = 10: B erreicht hoechstens ~0,3 der Amplitude
    (max |b| ~ J/(e Gamma)), bei d = 12 und 14 unter 0,1. Mehr als 90 % der Atmungsenergie gehen abgestrahlt verloren,
    bevor B voll angeregt ist.
  - Kontrast der Weitergabe still gegen 0,76: mindestens Faktor 3 in max |b|.
- **E2 (Vorzeichen):** t_AB < 0 fuer sigma = -1 und +1. Pruefbar nur ueber die Aufspaltung (Schwebung) und die Phase
  von b gegen a; im Zeitlauf wird das Vorzeichen aus der Phase von b(t)/a(t) bei kleinen t gelesen (+-i J t).
- **E3 (Drift, freie Baelle, nichtlinear):** Gegenphasige Baelle stossen sich ab.
  - Hand: E_int ~ c 8 pi A^2 e^{-k0 d}/d, c ~ 0,5 bis 1 (Runde-3-1D-Probe lag bei 0,5 der Formel), A ~ 3 bis 10.
  - Bei d = 12: E_int ~ 0,04 bis 1, relative Endgeschwindigkeit 0,03 bis 0,15 (Ballmasse ~ 170).
  - Der Abstand waechst in T ~ 30 bis 150 um 2, J faellt dabei um den Faktor e.
  - Folge: Bei freien Baellen kommt bei d = 12 hoechstens ~0,1 der Amplitude bei B an, still und 0,76 aehnlich.
    Die "fast verlustfreie Weitergabe" braucht gehaltene Baelle (Falle, Gitter, Nachbarn).
- **E4 (Kette aus drei, gehalten, d = 10, still):** A -> C ueber B mit t = pi/(sqrt 2 |J|) ~ 2000; B maximal voll
  bei der Haelfte. Bei 0,76 kommt bei C weniger als 0,05 an.
- **E5 (Kontrollen):** Einzelball still: Gamma_Gitter < 1e-4 grob, < 1e-5 fein. Einzelball 0,76: Gamma = 1,99e-3 +- 15 %.
  Ohne Anregung: Hintergrundatmung unter 1e-3 der Anregung, Ladung bleibt auf 1e-4.
- **Widerlegt (fuer die Hypothese der Leitung [H] "Band fast verlustfrei an der stillen Stelle"),** wenn eines eintritt:
  - still gehalten: max |b| < 0,5 innerhalb 1,5 t_tr (aus gemessenem J), oder Energieverlust pro Uebergabe > 10 %
  - 0,76 gehalten: B erreicht vergleichbar viel wie still (Kontrast < 2); dann traegt die stille Stelle nichts bei
  - Einzelball still auf dem Gitter mit Gamma > 1e-4 (dann misst das Gitter die stille Stelle nicht)

## 3. Laeufe

Alle in koll1.py. Achsensymmetrisches Gitter (rho_z, z), rho_j = (j + 1/2) h mit Spiegelung an der Achse; 4. Ordnung
im Raum, Leapfrog (Stoermer-Verlet) im Takt dt = 0,4 h; Randschicht mit Daempfung -sigma(x)(phi_t - i omega phi), die
den ruhenden Ball nicht angreift. Profil f und Mode (u, v) aus 1D-Rechnungen auf feinem Radialgitter, auf das 2D-Gitter
interpoliert.

- **cmt (Frage a):** Profil (Schiessen), Schwanz A, Mode bei reellem rho (still: rho*; 0,76: Resonanzspitze der
  Innennorm, daraus Gamma als Gegenprobe), C_v, N, K, J_ev(d) asymptotisch und als 2D-Ueberlappintegral mit der
  vollen Mode, Delta(d), E_int(d) aus der Mittelebenen-Spannung. Nur 1D/2D-Quadratur, keine Zeitentwicklung.
- **lin (Frage b, gehaltene Baelle):** lineare Zeitentwicklung um den eingefrorenen Hintergrund S_0 = F^2. Ein
  Lauf rechnet im Stapel: Einzelball, Paar d = 10, 12, 14 und Dreierkette d = 10 (Vorzeichen +, -, +). Anregung chi(0) =
  Mode an A. Gemessen: Atmungsamplitude a_A, a_B (a_C) durch Demodulation von delta S = 2 Re(F chi) mit der Mode als
  Gewicht; Fluss durch einen Zylinder; daraus Uebergabezeit, J (Anstieg von b, Schwebung), Verlust.
- **voll (Frage b, freie Baelle, wie im Auftrag):** volle nichtlineare Rechnung, Stapel {Paar: eps = 0, +eps, -eps;
  Einzelball an der Stelle von A: 0, +eps, -eps}. Lineare Antwort (phi_+ - phi_-)/(2 eps), zweite Ordnung
  (phi_+ + phi_- - 2 phi_0)/(2 eps^2). eps = 0,005 bei max |u + v| = 1. Drift aus dem Ladungsschwerpunkt je Haelfte
  (eps = 0), Gewichte folgen dem Ball.
- **Kontrollen:** Einzelball angeregt (im selben Stapel); beide ohne Anregung (eps = 0 im selben Stapel: Drift,
  Hintergrundatmung, Ladung); zwei Gitterstufen h = 0,15 (grob) und h = 0,10 (fein).
- **Zusaetze der Bearbeitung (nicht im Auftrag, so gekennzeichnet):** der lin-Lauf mit gehaltenen Baellen; die
  Kette aus drei im lin-Stapel (statt eines eigenen Laufs).

## 4. Kostenplan

- Lokal: nur Rauchtests (CPU, 1 Faden, nice 19, timeout 120, CUDA_VISIBLE_DEVICES leer), kleine Gitter, kurze T,
  Ausgaben nach lauf-lokal/.
- .69 ueber kleintest.sh aus /home/fmh/fmhc-physics-remote/runde9-koll1/, Spuren p4000a/p4000b, je Aufruf hoechstens
  10 min (Skript bricht selbst bei ~540 s ab und speichert den Zustand; Fortsetzung mit --weiter).
- Schaetzung (Speicher gebunden, ~25 Feldoperationen je Schritt, 17 MB je Stapelfeld bei h = 0,1):
  - cmt: 1 bis 2 min.
  - lin fein (5 Stapelglieder, 240 x 600 Punkte): ~5 ms je Schritt, 25 Schritte je Zeiteinheit, T = 3000 in ~6 min.
  - voll fein (6 Glieder, 240 x 800): ~6 ms je Schritt, T = 400 in ~1 min, laenger nur, wenn die Baelle halten.
  - grob (h = 0,15): etwa ein Viertel.
  - Summe ~8 Laeufe, 35 bis 50 GPU-Minuten auf zwei Spuren, dazu Wartezeit an den Sperren.
- Reihenfolge: cmt -> lin fein (still, 0,76) -> voll fein (still, 0,76) -> grob-Kontrollen -> (c) nur ueber den
  lin-Stapel.

## 5. Nachtrag 1 (Code, nach Rauchtest; 2026-09-30 07:43:24 CEST, date)

- An der stillen Stelle verlieren beide regulaeren Loesungen ihren wachsenden geschlossenen Anteil (das ist die
  bic2-Bedingung W = 0). Die Kombination "wachsender Anteil = 0" ist dort schlecht gestellt; der erste Rauchtest gab
  damit eine falsche Mode (offene Aussenamplitude 0,39). Behoben: kleinster rechter Singulaervektor der Matrix
  (wachsend, sin, cos) bei r_m = 16. Danach offene Aussenamplitude 1,6e-7. Fuer 0,76 bleibt "wachsend = 0".
- Messung: Die Gewichte f (u + v) sehen den Schwanz der Nachbarmode. Die Amplituden a_Y kommen deshalb aus der
  Inversion der Ueberlappmatrix M_XY = sum w_X 2F (u + v)(r_Y) (Uebersprechen 1,4 % bei d = 10). Phase im chi-Bild:
  CMT sagt arg(b/a) = -pi/2 fuer t_AB < 0.
- Zusatzkontrolle im voll-Lauf: Hintergrundatmung des unangeregten Einzelballs als aequivalentes eps.

## 6. Nachtrag 2: Vorhersagen fuer die Zeitlaeufe aus (a) (2026-09-30 07:43:24 CEST, date)

Grundlage: cmt auf der .69 (lauf-69/aus-cmt, Ende 07:42:08 CEST; dieselben Zahlen wie der lokale Rauchtest 07:37).
Um 07:43:24 lagen in aus-lin-still-fein/ und aus-lin-076-fein/ nur bericht.txt ohne Zeitreihen (ls auf der .69).
Zweimodenmodell mit gemeinsamem Gamma, ohne J_rad (Hand):

- (a) ergab |J| deutlich groesser als die Vorab-Schaetzung in Abschnitt 2: K = 10,7 (still) und 14,2 (0,76) statt
  0,5 bis 6. Abschnitt 2 bleibt unveraendert stehen; der Vergleich kommt ins Ergebnis.
- Gehalten, still (J = -5,63e-3 / -1,65e-3 / -4,99e-4 bei d = 10 / 12 / 14):
  - b_max >= 0,95 bei t ~ pi/(2|J|) = 279 / 950 / 3148 (+-15 %)
  - Summe a^2 ueber T = 3500 >= 0,98
  - J aus atan2(b, a) innerhalb 15 % der Werte aus (a); arg(b/a) = -pi/2 +- 0,2
- Gehalten, 0,76 (J = -8,06e-3 / -2,41e-3 / -7,36e-4; Gamma = 1,99e-3):
  - b_max ~ 0,68 bei t ~ 195 / 0,37 bei t ~ 370 / 0,13 bei t ~ 480
  - J aus atan2 innerhalb 15 % (J_rad bis 8,6e-5 kommt hinzu)
- Kette d = 10, gehalten:
  - still: c_max >= 0,85 bei t ~ pi/(sqrt 2 |J|) = 395. Der Mittelball ist um Delta/N ~ 1,8e-3 verstimmt
    (zwei Nachbarn), das kostet etwas.
  - 0,76: c_max ~ 0,5
- Frei (voll, d0 = 10), Abstand aus E_int(d) und Ballmasse:
  - still: d(50) = 16,6, d(100) = 25,7, d(200) = 43,9; 0,76: 17,4 / 27,2 / 46,7
  - Gemessener Abstand innerhalb 10 %; das prueft E_int.
  - b_max frei <= 0,11 (still) bzw. <= 0,14 (0,76), aus Integral |J(d(t))| dt.
