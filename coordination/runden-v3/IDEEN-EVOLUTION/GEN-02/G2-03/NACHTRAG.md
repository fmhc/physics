# G2-03 Nachtrag (nach dem Stempel 11:16:14, vor jedem Lauf)

- 2026-09-30 11:29:12 CEST, T-1: **geparkt**, kein Code, keine Formprobe, keine LAUF.txt.
  - Grund: Zeitbox 45 min fuer alle fuenf Karten; G2-04, G2-02 und G2-08 gingen vor (zusammen etwa 50 min neuer Code).
    Der neue Zeitschritt mit aeusserem Potential braucht nach Karte etwa 45 min, nach eigener Schaetzung 45 bis 60 min
    mit Ladungs- und Energiebuchfuehrung; halb gebaut waere er wertlos.
  - Bauhinweise fuer den naechsten Test-Agenten (Lesebefunde und Kopfrechnung, keine Rechnung auf dem Rechner):
    - Basis RUNDE-05/r5b/r5b.py kopieren (Box [-150, 150], Schwamm ab |x| = 110, profil_anker_x, ladung, gitter);
      Box und Schwamm wie Karte umstellen (Box +-150, Schwamm ab 120 laut Karte; Konstanten L_BOX/X_SPONGE).
    - Zeitschritt in Hamiltonform mit pi = psi_t - i V psi: psi_t = pi + i V psi, pi_t = psi_xx - U'(S) psi + i V pi.
      Strang: halbe exakte Drehung psi -> e^{i V dt/2} psi, pi -> e^{i V dt/2} pi; dann Verlet-Schritt
      (pi += dt/2 F(psi); psi += dt pi; pi += dt/2 F(psi)); dann die zweite halbe Drehung. Der Schwamm daempft pi,
      nicht psi_t (eichkovariant). Mit V = 0 muss der Schritt bitgleich den alten Verlet-Schritt geben: erste
      Kontrolle vor jedem Lauf.
    - Ladungsdichte rho = 2 Im(psi conj(pi)) (Konvention wie r5b, bei V = 0 gleich 2 Im(psi conj(psi_t))); die Drehung
      laesst rho unveraendert. Energie mit statischem V: |pi|^2 + |psi_x|^2 + U(S) plus ein Term V mal Ladungsdichte;
      Vorzeichen vor dem Einbau an einer ebenen Welle pruefen (Om + V0 = +-sqrt(k^2 + 1) aus der Karte).
    - Anfangsfeld: ruhender Ball psi = f, pi = -i omega f (bei x = 0 ist V ~ V0 e^{-2D} klein, bei D = 8 etwa 1e-7 V0;
      das gibt einen kleinen Anfangsstoss, am besten V in t < 50 glatt einschalten und den Fit wie die Karte erst ab
      t = 200 beginnen).
    - Messung wie Karte: Q_Ball in |x| < 15, Q_fern (x > D + 5 bis Schwamm plus geschluckt = Gesamt(0) - Gesamt(t)),
      Fluss j(D + 5, t) = -2 Im(psi conj(psi_x)) (bei V = 0), omega(t) am Maximum; Geradenfit dQ_Ball/dt auf
      [200, 800]; Steigung ln|dQ/dt| gegen D aus drei D.
    - Zeitbedarf: 11 Laeufe, T = 1200, dx = 0,1 (3001 Punkte) wie r5b; auf einer P4000 nach R5-D-Erfahrung
      (8000 Schritte 16 s fuer 11 Laeufe) etwa 40 s grob und 2 bis 3 min fein; auch auf einer CPU-Spur unter 10 min.
  - Die Karte kann scheitern (Vorzeichen, Schwellen, Steigung); kein "L1 schwach".

- 2026-09-30 11:30:37 CEST, Leitung: bleibt geparkt, nicht getestet (Bau 45 bis 60 min passte nicht in die Zeitbox). Das wird wie die
  ungetesteten Karten in Generation 1 behandelt.
