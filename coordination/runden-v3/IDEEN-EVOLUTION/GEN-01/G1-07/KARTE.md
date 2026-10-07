# G1-07 Tod ohne Mindestladung: In 1D verliert ein entleerter Ball seine Familie erst bei Q_d ~ sqrt(gamma)

- Hypothese: In 1D, wo die Ballfamilie keine Mindestladung hat, stirbt ein gleichmaessig entleerter Ball nicht an einer
  festen Ladung, sondern verliert die Familie erst, wenn die Abflussrate gamma die Bindungsfrequenz 1 - omega erreicht;
  die Todesladung skaliert deshalb wie Q_d ~ gamma^(1/2), und ein danach gestoppter Rest bildet wieder einen Ball [H].

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Modell U = S - S^2 + S^3/2, 1D. Kleiner Ball (omega -> 1): f = sqrt(eps) sech(sqrt(eps) x) mit eps = 1 - omega^2.
    Daraus Q = 4 omega sqrt(eps), also 1 - omega ~ Q^2/32 und Breite ~ 4/Q.
  - Q(omega) faellt in 1D bis Q -> 0: keine Mindestladung. In 3D ist die Familie dagegen durch Q_min nach unten begrenzt
    [A: 3D-Familie des Modells, Q_min = 111,84 bei omega^2 = 0,927].
  - Abfluss -gamma psi_t ueberall: dQ/dt = -gamma Q exakt, also Q_erw(t) = Q0 e^{-gamma t}.
  - Adiabatisch folgt der Ball der Familie, solange gamma << 1 - omega(Q). Bruch bei gamma = kappa (1 - omega) mit
    kappa = O(1), also Q_d = sqrt(32 gamma/kappa). Fuer kappa zwischen 0,25 und 4 und gamma = 1e-3: Q_d = 0,09 bis 0,36.
  - Nach dem Bruch zerfliesst der Rest dispersiv. Stoppt man den Abfluss kurz danach, enthaelt ein 1D-Paket mit genug
    "Flaeche" wieder einen Ball [L: Zakharov-Shabat-Bild der NLS, aus dem Gedaechtnis].

- Kleiner Test:
  - Code-Basis:
    - RUNDE-05/r5b/r5b.py: 1D-Anker (anker_q_e, Profil), entwickeln mit gleichmaessiger Daempfung gamma, Schwamm,
      Messhilfen
    - Auswertung t90/t50/t10 und q_rel wie in RUNDE-07/r5f/r5f.py (auswertung_tod), auf 1D uebertragen
    - Neu (unter 1 h): Treiber mit Abfluss und Stopp, Fenster um den Ballmittelpunkt, Familienvergleich
  - Start: ruhender 1D-Ball bei omega^2 = 0,80, Q0 aus anker_q_e.
  - Dauerabfluss gamma = 2e-3, 1e-3 und 5e-4, ohne Stopp. Box +-600, Schwamm ab |x| = 550, Fenster |x| < 100;
    dx = 0,1, dt = 0,05 (fein dx/2, dt/2); T = ln(Q0/0,05)/gamma + 500.
  - Stopp-Lauf: gamma = 1e-3; der Abfluss endet bei Q_erw = 0,8 Q_d(1e-3). Q_d kommt aus dem Dauerlauf (Regel vor dem
    Lauf festgelegt), danach 2000 Zeiteinheiten ohne Abfluss.
  - Gegenprobe-Lauf: gamma = 0, T = 2000.
  - Rechenort: .69 ueber kleintest.sh. p4000a: alle Laeufe grob (etwa 3 min); p4000b: fein fuer gamma = 1e-3 und
    2e-3, je Aufruf unter 8 min. CPU-Ausweg: je gamma eine Spur (cpu bis cpu4), nur grob.
  - Messung:
    - Q_in (Fenster), Q_tot, E; q_rel = Q_in/Q_erw
    - Zentraldichte S_c(t) gegen den Familienwert S_c,fam(Q_erw(t)) aus dem Anker
    - Phasenfrequenz omega(t) im Zentrum, Breite
  - Todesladung Q_d := Q_erw beim Adiabatik-Bruch, dem ersten Zeitpunkt mit |S_c/S_c,fam - 1| > 0,1. Dazu t90, t50 und
    t10 aus q_rel.

- Vorhersage vorab:
  - V1 (Kern): Q_d(gamma) ~ gamma^p mit p = 0,50 +- 0,12 (Fit in log-log ueber die drei gamma); Q_d(1e-3) zwischen 0,08
    und 0,40.
  - V2: Bis zum Bruch folgt der Ball der Familie: |omega(t) - omega_fam(Q_erw)| < 2e-3, solange Q_erw > 2 Q_d; das hoechste
    gemessene omega vor dem Bruch liegt unter 1.
  - V3: Q_d(5e-4)/Q_d(2e-3) liegt zwischen 0,38 und 0,62 (p = 0,5 ergibt 0,5).
  - V4 Stopp: Der gestoppte Rest bleibt lokalisiert, q_rel(t_stop + 2000) >= 0,5 bezogen auf Q_erw(t_stop), und omega
    faellt wieder unter 1.
  - **Scheitert, wenn** eines davon eintritt:
    - p < 0,3 (eine feste Schwelle wie bei einer Mindestladung) oder p > 0,7
    - omega > 1 vor dem Bruch, obwohl die Familie dort existiert
    - der gestoppte Rest zerlaeuft (q_rel < 0,1 bei t_stop + 2000)

- Gegenprobe:
  - gamma = 0: |dQ_in|/Q < 1e-3 bis T; omega = sqrt(0,80) = 0,8944 auf 1e-3; S_c konstant auf 1 %.
  - Vergleich 3D radial mit demselben Abfluss (RUNDE-05/r5a/r5a.py tod bzw. RUNDE-07/r5f/r5f.py tod, gleiche gamma; neu
    oder aus vorhandenen Laeufen desselben Codes): Dort begrenzt Q_min die Familie. Erwartung: Die Todesladung bleibt
    nahe Q_min und haengt kaum von gamma ab (p < 0,2). Der sqrt(gamma)-Effekt muss dort fehlen.

- Plausibilitaetsschranke:
  - Q_tot(t) <= Q_erw(t) (der Schwamm nimmt nur); vor dem Bruch |Q_tot/Q_erw - 1| < 1e-3
  - q_rel <= 1,02; 0 < omega; E_in <= E_tot

- Latten erwartet:
  - L1 ja: Exponent, omega < 1 und Stopp koennen je einzeln scheitern.
  - L2: gamma = 0 und der 3D-Vergleich.
  - L3: dx/2 und dt/2; Q_d auf 5 %, p auf 0,05.
  - L4 bekannt fuer die kubische NLS: adiabatisch gedaempfte Solitonen, Bruch bei eta^2 ~ Gamma [L: Karpman und Maslov
    1977; Kivshar und Malomed, Rev. Mod. Phys. 1989; aus dem Gedaechtnis, nicht nachgelesen]. Fuer unser Modell mit
    Abfluss neu.
  - L5 Analogie: Solitonen in verlustbehafteten Glasfasern verbreitern sich adiabatisch (gemessen) [L]; kein Zahlvergleich.

- Einfach gesagt: Einem Ball wird langsam Ladung abgesaugt. In drei Dimensionen gibt es eine Mindestgroesse, darunter kann
  er nicht bestehen. In einer Dimension gibt es diese Grenze nicht: Der Ball wird einfach immer kleiner und breiter. Wir
  sagen voraus, dass er trotzdem irgendwann zerfaellt, naemlich dann, wenn man schneller absaugt, als er sich innerlich
  anpassen kann. Wer halb so schnell absaugt, bringt den Ball auf eine etwa 1,4-mal kleinere Ladung, bevor er zerfaellt;
  hoert man kurz danach auf, formt sich der Rest wieder zu einem Ball.

- Karte geschrieben: 2026-09-30 07:40:50 CEST
- Vorhersage geschrieben: 2026-09-30 07:52:18 CEST
