# PLAN STILLE-ZWEIFELD (Runde 17)

- Code-Agent, Start 2026-10-02 09:54:01 CEST (date), Plan geschrieben ab 10:14:11 CEST (date), vor jedem .69-Lauf.
- Verbindlich aus der Karte: Modell M2, Bereiche, K1 bis K3, S1 bis S4, Bedeutung. Nichts davon wird nach dem Ergebnis
  geaendert. Code: code/stille3.py (eigener Code; BEUTEL-1 code/beutel.py unveraendert nur fuer Saat und K2).

## 1 Herleitung (eigene, vor dem Lauf)

- Ansatz der Karte, psi = e^{i w t}(f + a e^{i rho t} + b e^{-i rho t}), chi = g + c cos(rho t). Linear in a, b, c:
  - e^{+i rho t}: [-Lap + U_S - (w+rho)^2] a + S U_SS (a+b) + f U_Schi c/2 = 0
  - e^{-i rho t}: [-Lap + U_S - (w-rho)^2] b + S U_SS (a+b) + f U_Schi c/2 = 0
  - chi: [-Lap + U_chichi - rho^2] c + 2 f U_Schi (a+b) = 0
  - M2: U_Schi = 2g, also g f c und 4 g f (a+b). **Die Skizze der Leitung ist richtig.**
- Selbstadjungiert: nicht in (a, b, c) (Kopplung g f gegen 4 g f), wohl aber mit c' = c/2. Dann ist die Matrix
  M = [[U_S + S U_SS, S U_SS, 2gf], [S U_SS, U_S + S U_SS, 2gf], [2gf, 2gf, U_chichi]] symmetrisch. Grund: Gewicht von c
  in der zeitgemittelten Wirkung ist 1/4 gegen 1 fuer a, b. Mit u = r (a, b, c') gilt u'' = (M - E) u,
  E = diag((w+rho)^2, (w-rho)^2, rho^2); die Wronski-Form W[Y,Z] = sum (u_Y u_Z' - u_Y' u_Z) ist erhalten.
  Numerische Probe: Isotropie der regulaeren Loesungen mit c' (soll ~1e-12) und mit c (soll deutlich verletzt sein).
- Ein-Feld-Grenzfall: U_Schi = 0 entkoppelt c; a, b sind dann genau LOG-NACHBAU (V = U' + S U'', Kopplung S U'').
- Kanaele im Unendlichen: k_a^2 = (w+rho)^2 - 2, k_b^2 = (w-rho)^2 - 2, k_c^2 = rho^2 - 2.
- **Abweichung von der Skizze (Bereiche):** b oeffnet bei rho > w + sqrt(2) (2,27 bis 2,81 im Fenster). Bis rho = 3,0
  gibt es also einen Bereich mit drei offenen Kanaelen. Benennung hier:
  - E0: rho < sqrt2 - w; E1: sqrt2 - w < rho < sqrt2 (nur a offen); E2: sqrt2 < rho < sqrt2 + w (a, c offen);
    E3: sqrt2 + w < rho <= 3,0 (a, b, c offen; Zusatz, von der Karte als "E2" mitgemeint).
  - S2 wird auf E2 und E3 zusammen bewertet (Karte: "E2" = rho > sqrt2).

## 2 Stille Stelle, Kenngroessen

- Regulaere Loesungen R (3-dim, u(0) = 0), Lagrange-Raum der Wronski-Form. D = Loesungen, die in den geschlossenen
  Kanaelen abklingen und in den offenen keine Amplitude haben (dim = Zahl n_c der geschlossenen Kanaele).
- Stille Stelle <=> R geschnitten D nicht 0 <=> G = [W[Y_x, Z_y]] (3 x n_c) hat Rang <= n_c - 1 (Lagrange-Argument
  wie LOG-NACHBAU). E1: 3x2-Matrix, Rang <= 1, zwei Bedingungen (Kodim. 2). E2: 3x1, G = 0, drei Bedingungen
  (Kodim. 3, generisch keine Stelle). E3: keine geschlossenen Kanaele; Stelle <=> eine regulaere Loesung hat in allen
  drei Kanaelen Amplitude 0.
- Numerik (gegen Ausloeschung bei grossen Baellen): Y_x von r = 0 nach aussen, Z_y von R_inf nach innen, beide mit
  Gram-Schmidt alle ca. 0,5 Laengeneinheiten (Y: Ordnung (c, b, a) in E1, (b, c, a) in E2; Ankerung an festen Radien).
  Abgleich bei r_m = Halbwertsradius des Profils (auf das RK4-Gitter gerundet; bei Verfeinerungen fest).
  Die Gram-Schmidt-Transformationen sind dreieckig mit positiver Diagonale: Nullstellen, Vorzeichen von s und
  Umlaufzahlen bleiben gleich (Herleitung in ERGEBNIS).
- **E1:** W = m_ac + i m_bc (2x2-Minoren von G mit Zeile c). Geschlossene Bedingung: m_bc = 0 (aus Y_b, Y_c laesst sich
  eine in b und c abklingende Loesung bilden). Kenngroesse s = m_ac an deren Nullstellen. Im Grenzfall (c entkoppelt)
  ist W = G_cc (G_a + i G_b) mit G_cc < 0, also LOG-NACHBAU bis auf einen orientierungstreuen Faktor.
  Echtheitsprobe jeder Nullstelle: sigma_2/sigma_1(G) < 1e-6 (sonst Scheinnullstelle mit Zeile c = 0).
- **E2:** G (3-Vektor) mit orthonormalem Y und Einheits-Z. Geschlossene Bedingung G_b = 0 (Y_b klingt in b ab).
  Zwei Abstrahlamplituden s_a = G_a, s_c = G_c; Gesamtabstrahlung T = |G| (in [0, 1]).
- **E3 (Zusatz):** T3 = sigma_min / sigma_max der 6x3-Amplitudenmatrix (sqrt(k)-normiert) der regulaeren Loesungen.

## 3 Numerik

- Profil M2: Numerov (4. Ordnung) fuer F = r f, H = r (g-1), F = H = 0 bei r = 0 und R_bg; Newton (Bandloeser).
  R_bg = 1,5 r_half + 25/mu + 5 (mu = sqrt(m^2 - w^2)), auf Vielfache von 0,02 aufgerundet, aus dem eigenen r_half
  (damit auf beiden Stufen gleich). Saat: BEUTEL-1-Fluss bei Q = 200 (beutel.py, unveraendert), dann Fortsetzung in
  w^2 mit adaptiver Schrittteilung. r_m = r_half auf Vielfache von 0,02 gerundet (mind. 0,2), auf beiden Stufen gleich.
  Bei Verfeinerungen (Newton, Rechteck, Gauss-Newton) gelten Gitter, R_bg und r_m der naechsten Zeile (Anker).
- Kanaele: RK4, Schritt h = 2 hp, Profilwerte auf hp. Stufe 1: hp = 0,01; Stufe 2: hp = 0,005.
- Zeilen: w^2 = 0,75 + 0,02 j, j = 0..60. Je Zeile 301 rho-Punkte in E1 und in E2, 151 in E3, Abstand zu jeder
  Schwelle 1e-3. Nullstellen von m_bc (E1) und G_b (E2) per kubischer Interpolation, s an der Nullstelle ebenso.
- Ergebnisse je Zeile sofort als JSON.

## 4 Kontrollen

- **K1 (bindend, Gate fuer alles):** Grenzfall U = (1/4)(chi^2-1)^2 + S - S^2 + S^3/2 (chi-Kopplung aus, Schwelle 1
  fuer a, b). Zwei Varianten, da die Karte die c-Masse offenlaesst:
  - K1-E1: chi-Potential (1/2)(chi^2-1)^2 (m_c^2 = 4, c an der Stelle zu): E1-Maschine, W-Nullstelle.
  - K1-E2: chi-Potential (1/4)(chi^2-1)^2 (m_c^2 = 2, c an der Stelle offen): E2-Maschine, T-Minimum.
  - Zeilen w^2 = 0,78 bis 0,82 (Abstand 0,01), rho 1,70 bis 1,79 (91 Punkte), beide Stufen.
  - Bestanden: Lage auf 1e-4 an 0,797677 / 1,744618 auf beiden Stufen; K1-E1 Umlauf -1 aufgeloest; K1-E2 T_min < tau_E2
    und Umlauf von G_a + i G_b gleich -1 aufgeloest. K1-E1 gated E1, K1-E2 gated E2/E3.
- **K2:** Q und E/Q meiner Stufe-2-Profile gegen BEUTEL-1-Code (newton_w, dr = 0,01, gesaet mit meinem Profil) bei
  w^2 = 0,76; 0,90; 1,10; 1,30; 1,50; 1,70; 1,84; 1,94. Bestanden: alle relativen Abweichungen <= 1e-4.
- **K3:** jede Stelle auf beiden Stufen; Lagen in w^2 und rho je <= 1e-4 gleich.

## 5 Suche und Wertung

- **E1:** Detektor 1 (Nullstellen von m_bc benachbarter Zeilen wechselseitig naechste, Abstand <= 0,1; Vorzeichenwechsel
  von s), Detektor 2 (Zellen-Umlauf von W aus Eckwerten). Kandidaten < 5e-3 zusammengelegt. 2D-Newton auf (Re W, Im W)
  (Differenzen 1e-6, Schritt <= 0,01, Ende bei Schritt < 1e-10, hoechstens 12). Rechteck Halbbreite 1e-3 (verkleinert,
  falls naeher an einer Schwelle), 16 Punkte je Kante, Halbierung jedes Abschnitts mit Sprung >= 0,4 rad.
  **Adaptiv: hoechstens 24 Runden oder bis aufgeloest, hoechstens 3000 Randpunkte.** Begruendung: 24 Halbierungen
  verkleinern einen Abschnitt auf 2^-24 (Randlaenge ~ 1e-10), unter der Newton-Genauigkeit; LOG-NACHBAU brauchte 10.
  Bleibt es unaufgeloest: zweiter Versuch mit Halbbreite 1e-4 (vorab festgelegt). Gefunden = Umlauf +-1 aufgeloest auf
  beiden Stufen, sigma_2/sigma_1 < 1e-6, K3.
- **E2/E3:** lokale Minima von T bzw. T3 auf dem Zeilengitter (8 Nachbarn, indexgleich). E2-Minima: Gauss-Newton auf G
  (Kleinste Quadrate, hoechstens 15 Schritte). E3-Minima nur verfeinert (Nelder-Mead), wenn T3 < 100 tau_E3.
  "Beide null" heisst T_min < tau auf beiden Stufen und K3.
- **Schwelle tau (vor dem Hauptlauf eingefroren):** Eichzeilen w^2 = 0,85; 1,25; 1,65; 1,93 auf beiden Stufen.
  nu = groesste Abweichung |T_St1 - T_St2| ueber alle Gitterpunkte (E2 bzw. E3). tau = max(10 nu, 1e-10).
  Ablage hilfs/schwelle.json mit date, vor dem Start des Hauptlaufs.
- **S1:** eingetroffen, wenn mindestens eine E1-Stelle "gefunden" ist.
- **S2:** eingetroffen, wenn keine E2- oder E3-Stelle "beide null" erfuellt.
- **S3:** nur bei S1: alle E1-Stellen mit w^2 < 1,4 und chi(0) < 0,5; sonst nicht eingetroffen; ohne S1 offen.
- **S4 (Homotopie):** U_lam = (1/4)(chi^2-1)^2 + (1 + lam chi^2) S - S^2 + S^3/2, lam = 0; 0,05; ...; 1 (lam = 0 ist
  K1-E2, lam = 1 ist M2). Die M1-Stelle wird verfolgt (Start am K1-Fund; je Schritt Gauss-Newton auf G in E2-Art bzw.
  W-Newton, falls der Punkt nach E1 wandert). Nachfolger lebt bei lam, wenn T_min < tau (E2-Art) bzw. W-Newton mit
  sigma_2/sigma_1 < 1e-6 (E1-Art). S4 eingetroffen, wenn der Nachfolger vor lam = 1 erlischt oder bei lam = 1 nicht in
  E1 liegt; nicht eingetroffen, wenn bei lam = 1 eine lebende E1-Stelle erreicht wird.
- Bedeutung: woertlich nach Karte.

## 6 Laufliste (Spuren cpu3/cpu4, je <= 10 min)

- L0 Rauchtest (.69): Profil und je ein Punkt E1/E2/E3, grob. L1 Profile (beide Stufen, alle Zeilen + K2-Werte).
  L2 K2. L3 K1 (beide Varianten, beide Stufen). L4 Eichung tau. L5 Hauptzeilen (Stufen getrennt, in Bloecken).
  L6 Kandidaten E1/E2/E3 je Stufe. L7 Homotopie S4 (beide Stufen). L8 Abbildung.
- Folgelaeufe nur mit eingefrorenem PLAN-NACHTRAG-n.md, als nachtraeglich markiert.
