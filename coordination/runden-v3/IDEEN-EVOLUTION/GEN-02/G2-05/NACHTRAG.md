# G2-05 Nachtrag (Test-Agent T-2): geparkt mit Bauhinweisen

- 2026-09-30 11:29:42 CEST (date): KARTE.md vollstaendig (Vorhersage mit "Scheitert, wenn", Gegenprobe, Schranke);
  Zeile "Vorhersage geschrieben: 11:06:31" gesetzt, seitdem unveraendert. Kein Code, keine Formprobe, keine LAUF.txt.
- Grund: Die Karte verlangt neuen Code (radiale 3D-Zeitentwicklung mit einlaufender Kugelschale, Fensterladung, Born-
  Schaetzung der s-Welle; laut Karte etwa 1 h). Das passt nicht in die Zeitbox von 45 min fuer fuenf Karten.
- Bauhinweise (kuerzer als in der Karte geschaetzt, etwa 30 bis 45 min):
  1. Basis nicht r5a.py, sondern RUNDE-07/bic2/bic2_v2.py, Funktion zeitlauf mit art = "nl0": Sie rechnet bereits die
     nichtlineare radiale 3D-Gleichung fuer Phi = r psi (l = 0) mit Leapfrog, Dirichlet bei r = 0 und r_max und
     Daempfungsschicht r > r_sd, auf dem 3D-Profil profil(w2, 3.0, BETA, dr). Kopieren, nicht aendern.
  2. Einlaufende Kugelschale auf Phi addieren: Phi_p = eps exp(-(r - r0)^2/(2 sigma^2)) exp(-i k (r - r0)),
     k = sqrt(nu^2 - 1), Zeitableitung wie paket_sigma in RUNDE-07/r5f/r5f.py mit vz = -1 (einlaufend). sigma = 32,
     eps = 0,01; r0 so, dass Ballschwanz und Paket sich nicht ueberlappen (r0 etwa R_halb + 30 + 4 sigma, also um 170);
     r_max um 450, r_sd um 380. Bei dr 0,05 sind das 9000 Punkte, also Sekunden bis eine Minute je Lauf auf der CPU.
  3. Fensterladung: Q_win(t) = 4 pi Int_0^R_win 2 Im(conj(Phi) Phi_t) dr (r^2 kuerzt sich mit Phi = r psi), ebenso E_win.
     C_Q = [Q_win(Ball + Paket) - Q_win(Ball allein)] / Q(Paket allein, einlaufend), zu einer Zeit, zu der die
     auslaufenden Wellen das Fenster verlassen haben (r0/v_g plus Laufweg durch das Fenster plus 4 sigma/v_g).
  4. Spektrum der auslaufenden Welle: Phi an einem Messradius zwischen R_win und r_sd aufzeichnen; matrix_pencil aus
     bic2_v2.py oder FFT; Linie bei nu - 2 omega.
  5. Born-Schaetzung der s-Welle: Fuer l = 0 ist das lineare Problem in Phi ein 1D-Problem auf der Halbachse mit
     Phi(0) = 0. Die 1D-Born-Rechnung aus r5f.py (Kopplung U''(S) S) mit Sinus- statt ebenen Wellen und dem 3D-Profil
     S(r) uebernehmen.
  6. Laeufe und Baender wie in der Karte (0,55: nu 1,2 / 2,0 / 2,6 / 2,8 / 3,1; 0,70: 2,0 / 2,8 / 3,1; Paket allein;
     0,90 bei 3,1). Grob dr 0,05, fein dr 0,025, dt = 0,4 dr wie in zeitlauf. Rechenort cpu oder cpu2 (1D-Gitter).
- Papiertest: Die Baender der Karte koennen in beide Richtungen verfehlt werden; L1 ist nicht schwach.

- 2026-09-30 11:31:44 CEST, Leitung: bleibt geparkt, nicht getestet (Bau 30 bis 45 min), wie die ungetesteten Karten in Generation 1.
