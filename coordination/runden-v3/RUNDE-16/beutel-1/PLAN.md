# BEUTEL-1 Plan (Code-Agent, Runde 16)

- Geschrieben ab 2026-10-02 08:57:06 CEST (date), vor jedem .69-Lauf und vor jedem Rauchtest.
- Grundlage: KARTE.md (unveraendert verbindlich: M1-M3, Groessen, B1-B7, Kontrollen, Bedeutung).
- Start der Zeitbox: 08:51:28 CEST, Ende spaetestens 10:06 CEST.

## 1. Pruefung der Karte vor dem Lauf (Schreibtisch)

Nachgerechnet, alles bestaetigt:
- M2-Potential: (1/4)(chi^2-1+2S)^2 + (1/2)S(S-2)^2 ausmultipliziert = (1/4)(chi^2-1)^2 + (1+chi^2)S - S^2 + S^3/2. Richtig.
- Massen im M2-Vakuum: U_S(0,1) = 2, U_chichi(0,1) = 2. Richtig. M3 ebenso 2 und 2.
- M1: U/S = 1 - S + S^2/2, Minimum 1/2 bei S = 1, also E/Q -> 0,7071, S(0) -> 1. Richtig.
- M2: lokal chi = 0 fuer S >= 1/2, chi^2 = 1 - 2S sonst. Auf dem chi^2 = 1-2S-Ast ist U/S = 2 - 2S + S^2/2 >= 1,125.
  Auf dem chi = 0-Ast Minimum bei 4S^3 - 4S^2 - 1 = 0: S0 = 1,17965, omega_0^2 = 0,72807, omega_0 = 0,85327. Richtig.
  Huellenanteil innen 0,25/(2 omega_0^2 S0) = 0,1455. Richtig.
- M3: E = (4 pi/3)(4B)^(1/4) Q^(3/4) = 4,189 Q^(3/4) bei B = 1/4, R^4 = Q, Volumenanteil 1/4. Richtig.
- Gleichungen, E, Q, Virial (T = 3 Int[omega^2 f^2 - U], T = Int f'^2 + (1/2)g'^2) richtig. Daraus folgt
  E - omega Q = (2/3) T > 0, also exakt p = omega Q / E < 1, wenn dE/dQ = omega gilt. Das nutze ich als zweite p-Bestimmung.
- Duennwandradius M1: Wandspannung sigma = Int 2 f'^2 dx = sqrt(2)/4, Druck ~ (omega^2 - 1/2) S0, also
  R ~ 0,71/(omega^2 - 1/2) und E/Q ~ 0,7071 + 0,75/R. Fuer 1 % braucht man R > ~110, Q > ~1e7.

Ein Punkt der Karte ist mehrdeutig, kein Rechenfehler, aber vor dem Lauf festzulegen:
- In 3D geht Q auch am Dickwand-Ende gegen unendlich (kleine Amplitude, kubische NLS mit Q ~ (m^2 - omega^2)^(-1/2)
  [Schreibtisch, H]). "Bei grossem Q" ist deshalb doppeldeutig. Ich werte "grosses Q" in B3, B5 nur auf dem
  Duennwand-Ast (stabiler Ast, dQ/domega < 0). Der Dickwand-Ast wird gesondert berichtet.

## 2. Methode

Ein gemeinsamer Loeser fuer M1, M2, M3 (M1: chi als Attrappe mit U_chi = 0, bleibt exakt 1).

- Diskretisierung: zellzentriertes Gitter r_i = (i + 1/2) dr, i = 0..N-1, Schalenvolumen V_i, Flaechen 4 pi r_{i+1/2}^2.
  Diskretes Funktional F = Sum V_i [U - omega^2 f^2] + Sum a [(Df)^2 + (1/2)(Dg)^2]/dr; Rand f = 0, g = 1 an r = R_max.
  f'(0) = g'(0) = 0 folgt aus a_{-1/2} = 0. Gleichungen = dF = 0; Hesse-Matrix bandfoermig (verschraenkt f,g; Band 2).
- Newton bei festem omega (scipy.linalg.solve_banded) und Newton bei festem Q (geraendertes System, Unbekannte
  lambda = omega^2, Nebenbedingung 2 omega Sum V f^2 = Q; zwei Bandloesungen je Schritt).
- Saat je Modell: Gradientenfluss (imaginaere Zeit, halbimplizit) auf dem Funktional
  E_Q[f,g] = Q^2/(4 Int f^2) + Int[f'^2 + (1/2)g'^2 + U] bei festem mittlerem Q, Start mit Stufenprofil
  (f = sqrt(S0) innen, chi = 0 innen; M3: sin(pi r/R)/(pi r/R) innen, chi = 0 innen). Danach Newton-Politur.
  Mittleres Q: M1 R0 ~ 5, M2 R0 ~ 5, M3 Q ~ 300.
- Ast 1 (stabil, duenne Wand bzw. Beutel): Fortsetzung in ln Q von der Saat aufwaerts, Praediktor = radiale Streckung
  um (Q_neu/Q_alt)^(1/3) (M3: ^(1/4)). Ziel: M1, M2 bis R ~ 250-300 (Q ~ 1e8); M3 bis Q >= 1e4.
- Ast 2: Fortsetzung in mu = m^2 - omega^2 (m^2 = 1 bzw. 2) von der Saat zu kleinerem mu, also omega aufwaerts,
  durch die Faltung Q_min hindurch bis mu = 0,01 (M1 omega^2 = 0,99; M2, M3 omega^2 = 1,99). Schrittweite adaptiv,
  Halbierung bei Nichtkonvergenz.
- Astzuordnung: Vorzeichen von dQ/domega aus Nachbarpunkten; dQ/domega < 0 = klassisch stabil [L?].
- Je Loesung: omega, Q, E, E/Q, S(0), chi(0), h, T, Virialfehler, Restfehler, Halbwertsradius, f(R_max),
  min f (Knoten), Monotonie von chi.
- p(Q) zentral aus Nachbarpunkten (ln E gegen ln Q) und zusaetzlich p = omega Q/E; dE/dQ zentral gegen omega.

## 3. Kontrollen

- Zwei Gitter: dr = 0,04 und dr = 0,02 bei gleichem R_max; zusaetzlich R_max x 1,5 bei dr = 0,04.
  Vergleich Q, E (omega-Ast, gleiches omega) bzw. E, omega (Q-Ast, gleiches Q). Ziel 1e-4 relativ.
- Virial relativ < 1e-3 je Loesung (diskret nicht exakt, also echte Probe).
- dE/dQ = omega entlang der Aeste.
- f knotenfrei, chi monoton, f(R_max) klein (< 1e-6 relativ zu f(0)).

## 4. Wertungsregeln (vor dem Lauf festgelegt)

- "->" (B1, B4, B5): Grenzwert aus Fit a + b x + c x^2 in x = Q^(-1/3) ueber die Punkte mit R >= 50 auf dem
  Duennwand-Ast. Zusaetzlich Rohwert beim groessten Q angegeben. Eingetroffen, wenn der Grenzwert im Band liegt.
  B1 "auf 1 %": |E/Q - 0,7071| <= 0,0071 und |S(0) - 1| <= 0,01.
- B2, B6 "Q^(3/4)-Strecke": je Ast getrennt (stabil, instabil) die laengste zusammenhaengende Q-Strecke mit
  p in [0,70; 0,80]. Strecke vorhanden, wenn Q_hi/Q_lo >= 3. p aus Nachbarpunkten; p = omega Q/E nur als Probe.
- B3: chi(0) < 0,1 beim groessten Q des Duennwand-Asts UND chi(0) > 0,8 beim groessten berechneten omega^2
  (Ziel 1,99, mindestens 1,95).
- B5: Band [0,13; 0,17] fuer den Grenzwert, Rohwert beim groessten Q ebenfalls angegeben.
- B7: Werte beim groessten berechneten Q (>= 1000) des Beutel-Asts: p in [0,72; 0,78] (p aus Nachbarpunkten),
  h in [0,22; 0,28], E/Q^(3/4) in [3,56; 4,82].
- Erreicht ein Ast die Zielgroesse nicht (Laufzeit, Konvergenz), wird die Vorhersage "offen" gewertet.

## 5. Rechnen

- Code in beutel-1/code/, per rsync nach /home/fmh/fmhc-physics-remote/runde16-beutel-1/, Aufruf nur ueber
  kleintest.sh Spur cpu6, je Aufruf <= 10 min; Aufteilung je Modell und Gitter.
- Lokal nur Rauchtest (System-python3, timeout 120, nice 19, ein Thread) mit kleinem Q-Bereich.
- Abbildungen mit matplotlib auf der .69.
- Literatur: arXiv-API zu Friedberg-Lee-Sirlin und Beutelgrenzfall, Abstand >= 5 s.
