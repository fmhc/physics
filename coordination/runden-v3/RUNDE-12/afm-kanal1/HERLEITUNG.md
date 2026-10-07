# AFM-KANAL-1: Herleitung der Kanalgleichungen (vor jeder Zahl)

- Code-Agent, Auftrag AFM-KANAL-1 (Neustart). Start 2026-10-01 17:12:01 CEST (date). Diese Datei begonnen
  2026-10-01 17:22:15 CEST (date), vor jeder Codezeile und vor jedem Lauf. Handrechnung [ES], nicht gegengelesen.

## 1 Modell und Profil

- n = (sin t cos p, sin t sin p, cos t), L = (1/2)(d_t n)^2 - (1/2)|grad n|^2 - U, U = (1/2)(s + kappa s^2), s = sin^2 t.
- In Winkeln: L = (1/2)[t_t^2 + sin^2 t p_t^2 - |grad t|^2 - sin^2 t |grad p|^2] - U(t).
- Ball: t = Theta(r), p = Omega t_zeit (Feld entlang z nur ueber Omega = omega + h). Dann
  L_0 = (1/2) Omega^2 sin^2 Theta - (1/2) Theta'^2 - U(Theta), also wirksames Potential
  U_Omega = U - (1/2) Omega^2 sin^2 Theta = (1/2) sin^2 Theta (1 - Omega^2 + kappa sin^2 Theta).
- U'(Theta) = sin Theta cos Theta (1 + 2 kappa sin^2 Theta). Profilgleichung (3D radial):
  Theta'' + (2/r) Theta' = G(Theta) := sin Theta cos Theta [1 - Omega^2 + 2 kappa sin^2 Theta].
  **Gleich MESS-3A R2.**
- G'(Theta) = cos 2Theta (1 - Omega^2 + 2 kappa sin^2 Theta) + kappa sin^2 2Theta.
- Fenster: U_Omega < 0 irgendwo genau fuer Omega^2 > 1 + kappa; Vakuum stabil fuer Omega^2 < 1. Also
  1 + kappa < Omega^2 < 1, kappa < 0. **Gleich MESS-3A K.**
- Mit Omega^2 = 1 + kappa + f |kappa| (Familie): 1 - Omega^2 = |kappa| (1 - f), U_Omega = (1/2)|kappa| sin^2 Theta
  (cos^2 Theta - f). Nullstelle von U_Omega: sin^2 Theta_z = 1 - f (untere Schiessgrenze), Gipfel bei pi/2.
  Duennwand f -> 0, Dickwand f -> 1.
- Duennwand-Abschaetzung [ES]: Wandspannung sigma = int sqrt(2 U_Omega(f=0)) dTheta = sqrt|kappa|/2,
  Energiedichtedifferenz eps = (1/2)|kappa| f, Radius R ~ 2 sigma/eps = 2/(sqrt|kappa| f); Kink
  sin^2 Theta = 1/(1 + e^{2 sqrt|kappa| (r - R)}), 10-90 %-Breite delta ~ ln 9/sqrt|kappa| ~ 2,2/sqrt|kappa|.

## 2 Entwicklung bis zur 2. Ordnung

Ansatz t = Theta + u, p = Omega t_zeit + chi. Mit sin^2(Theta + u) = sin^2 Theta + sin 2Theta u + cos 2Theta u^2 + O(u^3):

- (1/2) t_t^2 -> (1/2) u_t^2.
- (1/2) sin^2 t (Omega + chi_t)^2, Anteil 2. Ordnung: (1/2) sin^2 Theta chi_t^2 + Omega sin 2Theta u chi_t
  + (1/2) Omega^2 cos 2Theta u^2. (1. Ordnung: Omega sin^2 Theta chi_t ist totale Zeitableitung; der Rest
  verschwindet mit der Profilgleichung.)
- -(1/2)|grad t|^2 -> -(1/2)|grad u|^2; -(1/2) sin^2 t |grad chi|^2 -> -(1/2) sin^2 Theta |grad chi|^2.
- -U -> -(1/2) U''(Theta) u^2.

Tangentialkoordinate v = sin Theta chi (Bogenlaenge in Azimutrichtung):
- sin^2 Theta chi_t^2 = v_t^2; Omega sin 2Theta u chi_t = 2 Omega cos Theta u v_t.
- sin^2 Theta |grad chi|^2 = |grad v - v cot Theta grad Theta|^2 = |grad v|^2 - cot Theta grad Theta . grad(v^2)
  + v^2 cot^2 Theta Theta'^2.
- Partielle Integration: -(1/2) cot Theta grad Theta . grad(v^2) -> +(1/2) v^2 div(cot Theta grad Theta)
  = (1/2) v^2 [cot Theta Lap Theta - Theta'^2/sin^2 Theta]. Mit cot^2 - 1/sin^2 = -1 bleibt fuer v^2:
  -(1/2) v^2 [cot Theta Lap Theta - Theta'^2] = -(1/2) v^2 Lap(sin Theta)/sin Theta.

Ergebnis:

    L_2 = (1/2)(u_t^2 + v_t^2) + 2 Omega cos Theta u v_t - (1/2)(|grad u|^2 + |grad v|^2) - (1/2) V_u u^2 - (1/2) V_v v^2

    V_u = U''(Theta) - Omega^2 cos 2Theta = G'(Theta)
        = cos 2Theta (1 - Omega^2 + 2 kappa sin^2 Theta) + kappa sin^2 2Theta
    V_v = Lap(sin Theta)/sin Theta = cot Theta Lap Theta - Theta'^2
        = cot Theta U'(Theta) - Omega^2 cos^2 Theta - Theta'^2      (mit der Profilgleichung)
        = cos^2 Theta (1 - Omega^2 + 2 kappa sin^2 Theta) - Theta'^2  (ohne 0/0 bei Theta -> 0)

Euler-Lagrange:

    u_tt - Lap u + V_u u - 2 Omega cos Theta v_t = 0
    v_tt - Lap v + V_v v + 2 Omega cos Theta u_t = 0

Moden e^{-i rho t}: (-Lap + V_u - rho^2) U + 2 i Omega rho cos Theta V = 0, (-Lap + V_v - rho^2) V - 2 i Omega rho
cos Theta U = 0. Mit w = U + i V und w~ = U - i V (U = (w + w~)/2, i V = (w - w~)/2):

    [-Lap + (V_u + V_v)/2 + 2 Omega rho cos Theta - rho^2] w  + C w~ = 0     (geschlossen)
    [-Lap + (V_u + V_v)/2 - 2 Omega rho cos Theta - rho^2] w~ + C w  = 0     (offen)
    C = (V_u - V_v)/2

## 3 Grenzwerte und Proben (Hand)

- Vakuum Theta -> 0: V_u, V_v -> 1 - Omega^2, C -> 0. Geschlossen: -Lap + 1 - (rho - Omega)^2, Kontinuum ab
  rho = 1 + Omega; offen: -Lap + 1 - (rho + Omega)^2, Kontinuum ab rho = 1 - Omega.
- Innenraum Theta = pi/2 (Spin-Flop): V_u = Omega^2 - 1 - 2 kappa = (1 + f)|kappa|, V_v = 0, cos Theta = 0. Nackter
  geschlossener Kanal innen: (1 + f)|kappa|/2 - rho^2. Bei rho ~ 1 + Omega ist der Innenraum also ein tiefer, klassisch
  erlaubter Bereich (W ~ -4), aussen W ~ 0 [ES]. Folge fuer die Suche: Bei grossen Baellen liegen sehr viele
  Nullstellen lambda_k(rho_c) = 0 (Hohlraummoden des Innenraums) unter jedem moeglichen Wandzustand; "die untersten
  k <= 5" (R4) erreichen dann nur rho ~ sqrt((1 + f)|kappa|/2). Siehe PLAN.md, Abschnitt Suche.
- Phasenmode: rho = 0, v = sin Theta: [-Lap + V_v] sin Theta = 0 identisch (V_v = Lap(sin Theta)/sin Theta).
- Translationsmode: Ableitung der Profilgleichung nach r: Lap(Theta') - 2 Theta'/r^2 = G'(Theta) Theta' = V_u Theta',
  also [-Lap + 2/r^2 + V_u] Theta' = 0 (l = 1).
- K0 (kappa = 0): U_Omega = (1/2)(1 - Omega^2) sin^2 Theta >= 0, pi/2 ist im r-Bild ein Tal von -U_Omega; jeder Start
  in (0, pi/2] pendelt um pi/2 und erreicht 0 nicht ("Unterschuss" fuer alle Kandidaten): keine Loesung.

## 4 Vergleich mit MESS-3A (Abschnitt K und R)

| Groesse | MESS-3A | hier | Abweichung |
|---|---|---|---|
| Profilgleichung | Theta'' + (2/r)Theta' = sin cos [1 - Omega^2 + 2 kappa sin^2] | gleich | keine |
| V_u | U''(Theta) - Omega^2 cos 2Theta | gleich (= G'(Theta)) | keine |
| V_v | cot(Theta) U'(Theta) - Omega^2 cos^2 Theta - Theta'^2 | gleich; aequivalent Lap(sin Theta)/sin Theta (V0b E11) | keine (nur die Form ohne 0/0 fuer die Rechnung) |
| Kopplung | 2 Omega rho cos Theta im Diagonalterm, C = (V_u - V_v)/2 | gleich | keine |
| Kanalzuordnung | geschlossen w = u + i v, offen w~ = u - i v, Zeitfaktor e^{-i rho t} | gleich | keine; bei e^{+i rho t} tauschen w und w~ die Rollen |
| Schwellen | 1 + Omega (geschl.), 1 - Omega (offen) | gleich | keine |
| Innenwerte | V_u = Omega^2 - 1 - 2 kappa, V_v = 0 | gleich, = (1 + f)|kappa| | keine |
| Zusatztopf | -2 Omega rho (1 - cos Theta) | gleich | keine |

- **Keine Abweichung in den Formeln.** Zwei Lesepunkte, die keine Formelabweichung sind, aber die Rechnung betreffen:
  1. MESS-3A R4 sucht "fuer die untersten k <= 5". Nach Abschnitt 3 sind das bei duennwandigen Baellen nur die
     untersten Hohlraummoden bei kleinem rho. Ein Zustand nahe 1 + Omega waere dort ein Eigenwert mit hohem Index.
  2. Der Wandanteil F_w misst das Gewicht in |r - R_w| < 2 delta. Mit R_w ~ 2/(sqrt|kappa| f) und
     delta ~ 2,2/sqrt|kappa| ueberdeckt das Fenster einen Anteil ~ 4 delta/R_w ~ 4,4 f des Ballinneren [ES]. Fuer
     f >= 0,2 erreicht damit schon ein gleichmaessig verteilter Innenraumzustand F_w > 0,5. Der Test trennt dort
     Wand- und Volumenzustaende nicht. Beides gehoert in PLAN.md und ERGEBNIS.md als Befund, die Regel bleibt
     unveraendert.
