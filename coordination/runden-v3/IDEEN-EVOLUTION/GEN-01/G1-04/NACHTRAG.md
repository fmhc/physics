# G1-04 Nachtrag (nach dem Stempel 07:52:18, vor jedem Lauf)

- 2026-09-30 08:12:44 CEST, T-1: **geparkt**, kein Code, keine Formprobe, keine LAUF.txt. Grund: Zeitbox 45 min fuer fuenf Karten;
  G1-02, G1-07 und G1-05 (a) gingen vor. Neuer Code nach eigener Schaetzung 40 bis 60 min.
- Bauhinweise fuer den naechsten Test-Agenten (nur Lesebefunde, keine Rechnung):
  - Bausteine: RUNDE-05/r5b/r5b.py (gitter_periodisch, Laplace ueber torch.roll, rausch_basis, entwickeln mit
    periodisch=True), Klassen aus RUNDE-07/r5f/r5f.py (Auswertung kavitation, Zeilen um 1030 bis 1060):
    heilt = keine Stelle mit S < S0/2 in [T/2, T]; zerfaellt = mindestens 3 Luecken (Median der letzten 10 %);
    sonst Kaverne; t_kav = erste Zeit mit Leerlaenge >= max(10, Leerlaenge(0) + 5). Die Karte nimmt S_mittel/2
    statt S0/2; S_mittel(t) = raeumliches Mittel von S.
  - Kraft: psi_a,tt = psi_a,xx - U'(S) psi_a + g conj(psi_a) psi_b^2; Energiedichte |psi_t|^2 + |psi_x|^2 + U(S)
    - g Re(conj(psi_1)^2 psi_2^2) (je Komponente summiert).
  - Vorzeichen: r5b.ladung ist 2 Im(psi conj(psi_t)), die Ergaenzung in der Karte schreibt 2 Im(conj(psi) psi_t);
    beide unterscheiden sich nur im Vorzeichen, V1 nutzt nur Q_2/Q.
  - Offen und vor dem Lauf festzulegen: "Saat 21 in beiden Komponenten" - dieselbe Saat gaebe beiden Komponenten
    dasselbe Rauschmuster. Vorschlag: Komponente 1 Saat 21, Komponente 2 Saat 21 mit vertauschten psi/psi_t-
    Koeffizienten oder eine zweite Saat; die Leitung entscheidet.
  - Lauf 6 (M-gleichQ) braucht den gemischten stationaeren Zustand psi_1 = psi_2 = sqrt(S_m/2) e^{-i omega_m t} mit
    omega_m^2 = U_eff'(S_m) und gleicher Ladungsdichte wie Lauf 1; S_m = 0,927 (g = 0,5) steht in der Karte.
- Die Karte kann scheitern (drei Wege in V3, dazu Lauf 6); kein "L1 schwach".
