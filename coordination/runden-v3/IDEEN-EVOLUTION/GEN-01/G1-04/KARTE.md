# G1-04 Domaenenwaende als Keime: ein Kondensat mit zweiter Komponente reisst ohne Delle auf

- Hypothese: Ein dichtes Kondensat, das einkomponentig linear stabil ist (S0 = 0,72, zwischen der Spinodale 2/3 und 1),
  wandelt sich mit zweiter Komponente und Paarkopplung g von selbst in eine Mischung mit Domaenen psi_2 ~ +psi_1 und
  psi_2 ~ -psi_1 um, und es reisst genau an den Domaenenwaenden auf, ohne aeussere Delle [H].

- Modell [A]: Gesamtformel mit N = 2 und J = 1, coordination/gesamtformel-20260921/KANDIDAT.md, Abschnitt 2.2:
  psi_a,tt - psi_a,xx + U'(S) psi_a - g psi_a^* psi_b^2 = 0 (b != a), U = S - S^2 + S^3/2, S = |psi_1|^2 + |psi_2|^2.
  Die Vakuumschranke g <= 1,657 (N = 2) ist bei g = 0,2 und 0,5 eingehalten.

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Einkomponentig: omega^2 = U'(0,72) = 0,3376.
  - Paarumwandlung: Linearisiert man psi_2 um psi_1 = sqrt(S0) e^{-i omega t}, gilt fuer e^{ikx + st}:
    (s^2 + k^2)^2 + 4 omega^2 s^2 = (g S0)^2.
    - Bei k = 0: s0 = 0,300 (g = 0,5) und 0,123 (g = 0,2).
    - Band 0 < k < sqrt(g S0) = 0,60 bzw. 0,38; nahe k = 0 gilt s ~ s0 - c k^2 mit c = 0,196 bzw. 0,089.
    - Die wachsende Mode steht etwa 38 Grad gegen psi_1 (g = 0,5); ihr Vorzeichen ist je Bereich zufaellig. Daraus
      entstehen Domaenen mit Waenden, an denen psi_2 = 0 ist.
  - Gemischt (psi_1 = psi_2): U_eff = S - a S^2 + S^3/2 mit a = 1 + g/4.
    - Spinodale S < 2a/3: 0,75 (g = 0,5) bzw. 0,70 (g = 0,2)
    - Druck P = S^2 (S - a), negativ (Zug) fuer S < a; kritischer Keim mit kleinster Dichte S_t = 2a - 2S
  - Bei erhaltener Ladungsdichte (homogen) hat die Mischung S_m = 0,927 (g = 0,5) bzw. 0,793 (g = 0,2):
    - linear stabil, aber unter Zug: P = -0,170 bzw. -0,162; S_t = 0,395 bzw. 0,513
    - Die Umwandlung setzt 0,084 bzw. 0,029 Energie je Laenge frei (13 bzw. 5 % der Energiedichte).
  - An einer Wand ist psi_2 = 0. Einen homogenen einkomponentigen Zustand mit omega^2 < 1/3 gibt es nicht (min U' = 1/3),
    und nach der Umwandlung liegt omega^2 bei 0,20 bzw. 0,28. Die Dichte muss an der Wand also einbrechen.

- Kleiner Test:
  - Code-Basis:
    - RUNDE-05/r5b/r5b.py (periodische Box, Rauschen, Klumpenzaehlung)
    - RUNDE-07/r5f/r5f.py, Befehl kavitation (Klassen heilt/zerfaellt/Kaverne, Leerlaenge, t_kav)
    - Zweikanal-Integration wie coordination/gesamtformel-20260921/kontrolle/kontrolle_gesamtformel.py
    - Neu (unter 1 h): Kraftterm g psi_a^* psi_b^2 im Verlet-Schritt; Wandzaehlung als Vorzeichenwechsel von
      Re(psi_1^* psi_2) dort, wo |psi_2|^2 > 0,01 S0
  - 1D, periodisch, L = 200, dx = 0,1, dt = 0,05 (fein dx/2, dt/2), T = 600, Rauschen 1e-6 (Saat 21) in beiden
    Komponenten, keine Delle.
  - Laeufe:
    1. E-0,5: einkomponentig S0 = 0,72, psi_2 nur Rauschen, g = 0,5 (Hauptlauf)
    2. E-0,2: wie 1 mit g = 0,2 (Hauptlauf)
    3. E-0,5-S80: wie 1 mit S0 = 0,80 (Nebenlauf)
    4. G0: wie 1 mit g = 0 (Gegenprobe)
    5. LEER: wie 1, psi_2 exakt 0 (Gegenprobe)
    6. M-gleichQ: gemischt stationaer bei gleicher Ladungsdichte wie 1 (S = 0,927, g = 0,5), Rauschen 1e-6 (Gegenprobe
       ohne Waende und ohne Energieueberschuss)
    7. M-gleichS: gemischt stationaer bei S = 0,72, g = 0,5 (Kontrolle; liegt unter der gemischten Spinodale 0,75)
  - Rechenort: .69 ueber kleintest.sh, Spur p4000a (sonst cpu, cpu2). 7 Laeufe mit 2000 Punkten und 12000 Schritten,
    grob und fein, geschaetzt unter 5 min.
  - Messung:
    - Q_1, Q_2, Q, E; S(x, t) alle 5
    - Wandzahl; Leerlaenge (S < S_mittel/2), Zahl der Luecken, Klumpen
    - Lage der ersten Luecken gegen die Wandlagen bei t_kav - 5
    - mittleres S in [T/2, T]; Anfangsrate von Q_2

- Vorhersage vorab:
  - V1 Umwandlung (Kontrolle, folgt aus dem Papier): Q_2 waechst anfangs mit 2 s0 = 0,60 (g = 0,5) bzw. 0,25 (g = 0,2),
    je +-15 %. Q_2/Q ueberschreitet 0,3 bei t = 30 bis 80 (g = 0,5) bzw. 80 bis 200 (g = 0,2).
  - V2 Domaenen (grobe Schaetzung aus der Bandform): 4 bis 25 Waende, wenn Q_2/Q zum ersten Mal 0,3 ueberschreitet,
    fuer beide g.
  - V3 (Kern): Lauf 1 und 2 reissen ohne Delle auf, Klasse "zerfaellt" oder "Kaverne" bis T. Mindestens 70 % der ersten
    Luecken liegen innerhalb +-3 an einer Wand.
  - V4: Lauf 6 bleibt homogen (keine Stelle mit S < S_mittel/2 in [T/2, T], rms/S_mittel < 1e-2). Lauf 7 verklumpt
    (mindestens 3 Klumpen bis T).
  - V5 (nur Richtung): Lauf 3 wandelt nach derselben Formel um (s0 aus omega^2 = U'(0,80) = 0,36); er reisst spaeter
    oder an weniger Waenden auf als Lauf 1.
  - **Scheitert, wenn** eines davon eintritt:
    - Lauf 1 und 2 bleiben bis T ohne Luecke (Klasse "heilt"). Dann gilt die Gegenhypothese "die Umwandlung verdichtet
      und stabilisiert" (S_mittel in [T/2, T] zwischen 0,80 und 0,95).
    - Es entstehen Luecken, aber weniger als 40 % liegen innerhalb +-3 an einer Wand.
    - Lauf 6 (ohne Waende) reisst ebenso auf. Dann sind nicht die Waende die Keime.
  - Nicht entscheidbar, wenn V1 verfehlt ist (Kraftterm oder Vorzeichen falsch) oder Lauf 4 oder 5 nicht homogen bleibt.

- Gegenprobe:
  - Lauf 4 (g = 0) und Lauf 5 (leere zweite Komponente): keine Umwandlung (Q_2/Q < 1e-6 bzw. exakt 0), keine Wand,
    keine Luecke, rms/S0 < 1e-3, wie ein einkomponentiges Kondensat bei 0,72 ohne Delle.
  - Lauf 6: gleiche Ladungsdichte wie Lauf 1, aber keine Waende und kein Energieueberschuss; der Effekt muss fehlen.

- Plausibilitaetsschranke:
  - |dQ|/Q < 1e-10 (periodisch, keine Daempfungsschicht); |dE|/E < 1e-4
  - -0,01 <= Q_2/Q <= 1,01; S >= 0 ueberall
  - g unter der Vakuumschranke 1,657

- Latten erwartet:
  - L1 ja: V3 kann auf drei Wegen scheitern.
  - L2: Laeufe 4, 5 und 6.
  - L3: dx/2 und dt/2; Klasse gleich, Wandzahl auf +-30 %, Anteil an Waenden auf +-15 Prozentpunkte.
  - L4 teilweise: Spin-Mischung und spontane Domaenen nach einem Quench sind aus Spinor-Kondensaten bekannt [L: Sadler
    u. a., Nature 2006; Stamper-Kurn und Ueda, Rev. Mod. Phys. 2013; aus dem Gedaechtnis, nicht nachgelesen]. Dass die
    Waende Keime fuer das Aufreissen eines Kondensats unter Zug sind, ist mir nicht bekannt [H].
  - L5 Analogie: Domaenen in Spinor-Kondensaten sind gemessen; kein Zahlvergleich.

- Ergaenzung T-1 vor dem Stempel (nur Messregeln):
  - Q_a = Integral von 2 Im(conj(psi_a) psi_a,t) dx; einzeln nicht erhalten, nur Q = Q_1 + Q_2.
  - Anfangsrate fuer V1 = Steigung von ln(Q_2/Q) (kleinste Quadrate) im Bereich 1e-9 < Q_2/Q < 1e-4, verglichen mit 2 s0.

- Einfach gesagt: Ein dichter Nebel aus unserem Feld ist bei dieser Dichte "halb stabil": Er reisst nur auf, wenn man ihn
  kraeftig eindellt. Gibt man dem Feld eine zweite Sorte, in die es sich umwandeln kann, wandelt sich der Nebel von selbst
  um, aber nicht ueberall gleich: Es entstehen Bereiche mit zwei verschiedenen Vorzeichen, getrennt durch duenne Waende.
  Wir sagen voraus, dass der Nebel genau an diesen Waenden aufreisst, so wie Blasen im Sprudel an Kratzern im Glas
  entstehen. Bleibt der Nebel ganz oder reisst er anderswo auf, ist die Idee falsch.

- Karte geschrieben: 2026-09-30 07:38:34 CEST
- Vorhersage geschrieben: 2026-09-30 07:52:18 CEST
