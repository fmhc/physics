# LIN-WIRBEL-1: Lineare Stabilitaet drehender 2D-Q-Baelle (Windung m), NLS-Form gegen KG-Form

- Geschrieben: 2026-09-30 11:25:18 CEST (date direkt vor dem Schreiben). Noch kein Lauf gestartet.
- Autor: Beweis-Agent der Leitung claude-primary.
- **Reihenfolge-Vermerk:** Der Hinweis der Leitung (PDF liegt lokal; "Verschiebung sollte mit m schrumpfen",
  ausdruecklich als Hypothese der Leitung) kam **vor** dem Schreiben dieser Datei. Die Herleitung unten (Identitaet
  P_KG = P_NLS - nu^2) und die Zahlen aus Tabelle 1 habe ich vorher selbst an der Quelle gelesen (PDF-Seiten 17 bis 24,
  eigene Abrufkopie; dieselbe Tabelle steht in quellen/pego-warchall-nlin0108009.txt, Zeile 1119 ff.).
- Karte GEN-02/G2-01/KARTE.md ist eingefroren und wird nur gelesen.

## 1. Quelle (Pego und Warchall, arXiv nlin/0108009, an der Quelle gelesen)

- Gleichung (1.1) -i u_t - Laplace u = g(u), (1.2) g = |u|^2 u - |u|^4 u, Welle u0 = e^{i omega t} e^{i m theta} w(r),
  Profil w'' + w'/r - m^2 w/r^2 + g(w) - omega w = 0, omega_* = 3/16.
- Tabelle 1 (PDF-Seite 20): omega_cr = 0,1487 / 0,1619 / 0,1700 / 0,1769 / 0,1806 fuer m = 1 ... 5;
  lambda_cr = 0,0478i / 0,0271i / 0,0136i / 0,0063i / 0,0033i. Stabil fuer omega_cr <= omega < omega_*.
- Mechanismus (Seite 20): "A pair of purely imaginary gap eigenvalues, always with index j = 2, collides when
  omega = omega_cr at lambda = lambda_cr ... creating an unstable eigenvalue." Also Hamilton-Hopf, nicht Austritt aus null.
- Normierung: identisch mit der NLS der Karte (Omega = omega_PW). Umrechnung auf unser Modell:
  f = sqrt(4/3) g, r = sqrt(3/8) rho, Omega = (3/8)(1 - omega^2), also omega_c^2 = 1 - (8/3) Omega_cr:
  0,6035 / 0,5683 / 0,5467 fuer m = 1, 2, 3.

## 2. Gleichungen (unsere Einheiten)

- KG: phi_tt - Laplace phi + U'(|phi|^2) phi = 0, U(S) = S - S^2 + S^3/2. Stoerung
  w = e^{i m theta}[a(r) e^{iJ theta} e^{lambda t} + conj(b(r)) e^{-iJ theta} e^{conj(lambda) t}]:
  - -Delta_{m+J} a + (dp - (omega - i lambda)^2) a + sp b = 0
  - -Delta_{m-J} b + (dp - (omega + i lambda)^2) b + sp a = 0
  - dp = 1 - 4S + 4,5 S^2, sp = -2S + 3S^2, S = f^2, Delta_n = d_rr + d_r/r - n^2/r^2.
- Mit lambda = i nu: P_KG(nu) v = 0, P_KG(nu) = K - 2 omega nu sigma_3 - nu^2, K = [[-Delta_{m+J} + dp - omega^2, sp],
  [sp, -Delta_{m-J} + dp - omega^2]] (selbstadjungiert in L^2(r dr)^2).
- NLS-Form = KG ohne lambda^2: P_NLS(nu) = K - 2 omega nu sigma_3. Weil K(omega) = (8/3) K_NLS(Omega) exakt gilt,
  ist das das NLS-Spektrum mit lambda_NLS = (3 omega / 4) lambda. Kollisionsfrequenz aus Tabelle 1 in unseren Einheiten:
  nu_c = (4/(3 omega)) * 0,0478 = 0,082 (m = 1), 0,048 (m = 2), 0,0245 (m = 3).

## 3. Erwartung vorab (vor dem ersten Lauf)

- **E1 (Pruefung NLS-Form):** Schwellen 0,6035 / 0,5683 / 0,5467 auf +-0,0005 in omega^2 (Gitter und Box), kritischer
  Index J = 2 fuer alle drei m, Kollisionsfrequenz in NLS-Einheiten 0,0478 / 0,0271 / 0,0136 auf +-5 %.
- **E2 (KG gegen NLS): nicht gleich, verschoben.**
  - Grund: Der Umschlag ist eine Krein-Kollision bei nu ungleich 0 (Tabelle 1). Exakte Identitaet:
    P_KG(nu) = P_NLS(nu) - nu^2 * 1. Die Eigenwertaeste mu_k(nu) des selbstadjungierten Buendels werden also genau um
    -nu^2 verschoben, die Eigenvektoren bleiben. NLS-Schwelle: Extremum eines Astes beruehrt 0. KG-Schwelle: dasselbe
    Extremum beruehrt nu^2. Verschiebung ungefaehr -nu_c^2 / (d mu_ext / d omega^2). Gleich waeren die Schwellen nur bei
    einem Austritt durch null (nu_c = 0).
  - Groesse: nu_c^2 = 0,0067 / 0,0023 / 0,0006. Mit |d mu_ext / d omega^2| zwischen 0,5 und 3: Betrag der Verschiebung
    m = 1: 0,002 bis 0,013; m = 2: 0,001 bis 0,005; m = 3: 0,0002 bis 0,0012. Sie schrumpft mit m ungefaehr wie nu_c^2.
  - Vorzeichen: haengt davon ab, ob der Ast an der Kollision ein Maximum (KG frueher instabil, Schwelle tiefer) oder
    ein Minimum hat (KG spaeter instabil). Ich erwarte **tiefer**, weil beide Zeitentwicklungen unter den NLS-Werten
    liegen (m = 1: 0,59 bis 0,60 gegen 0,6035; m = 2: 0,567 gegen 0,5683) und ihr Verhaeltnis (etwa 2,7) zum
    Verhaeltnis der nu_c^2 (2,9) passt.
  - Erwartete KG-Schwellen: m = 1 etwa 0,599 (0,594 bis 0,602), m = 2 etwa 0,5668 (0,564 bis 0,568),
    m = 3 etwa 0,5463 (0,5455 bis 0,5467). Kritisch wieder J = 2.
- **E3 (Zeitentwicklung):** lineares KG-gamma bei m = 2: omega^2 = 0,57 etwa 0,010, bei 0,59 etwa 0,027 (G1-03: 0,0098
  und 0,0265), Abweichung hoechstens 25 %. m = 1: gamma(0,60) etwa 0,004 (RING-T 0,0041), gamma(0,59) null oder unter 0,002.
- **Was die Erwartung widerlegt:** E1 verfehlt (dann ist der Loeser falsch, E2 wird nicht bewertet); Verschiebung
  |KG - NLS| kleiner als die doppelte numerische Unsicherheit (dann "gleich"); Vorzeichen positiv; Verschiebung waechst
  mit m; kritischer Index nicht J = 2.

## 4. Verfahren

- Profil: Schiessen (f = c r^m (1 + kappa^2 r^2/(4(m+1))) am Start, Bisektion in c), danach Newton auf demselben
  FD-Gitter wie das Eigenwertproblem (diskretes Profil, Residuum < 1e-11).
- Radial-FD 2. Ordnung, zellzentriert r_i = (i - 1/2) h, Flussform mit Gewicht r (symmetrisiert mit sqrt(r)),
  Dirichlet am Boxrand R. Aufloesungen h = 0,1 und h = 0,05, R = 40 (Boxprobe R = 50 an einer Stelle).
- NLS-Form: nu = eig(sigma_3 K)/(2 omega), dicht. KG: reelle Begleitmatrix [[0, 1], [K, -2 omega sigma_3]] fuer nu,
  dicht bei h = 0,1; bei h = 0,05 Shift-Invert (scipy eigs) um die Kollisionsstelle. Wachstum gamma = max |Im nu|.
- Filter gegen Box-Artefakte: instabile Eigenwerte nur zaehlen, wenn der Eigenvektor lokalisiert ist (Anteil der Norm
  in r > 0,75 R unter 1e-3); sonst als Boxmode ausweisen.
- Scan: m = 1, 2, 3; J = 1 bis 6; omega^2 um die NLS-Schwelle (-0,04 bis +0,04). Schwellen aus der Diskriminante
  D = (nu_1 - nu_2)^2 des kollidierenden Paares (glatt, Vorzeichenwechsel an der Schwelle) mit Nullstellensuche;
  Gegenprobe gamma^2 linear in omega^2. Dritte Pruefung ueber die Aeste mu_k(nu) (Extremum gegen 0 bzw. nu^2).
- Rechenort: .69, kleintest.sh, Spur cpu5, je Aufruf unter 10 min, ein Thread.
