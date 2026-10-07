# G2-06 Nachtrag (nach dem Stempel 11:16:14, vor jedem Lauf)

- 2026-09-30 11:29:12 CEST, T-1: **erneut geparkt**, kein Code, keine Formprobe, keine LAUF.txt.
  - Grund: Zeitbox 45 min fuer alle fuenf Karten; die guenstigeren Karten G2-04, G2-02 und G2-08 gingen vor. Der
    neue Code (Detektor-Zeitreihen mit Bandfiltern, mitgefuehrtes Ballfenster, eigene eps/nu-Listen) braucht nach den
    Bauhinweisen aus G1-06 40 bis 60 min und passte nicht mehr hinein. Zweimal geparkt aus Zeitgruenden: Die Leitung
    entscheidet, ob sie die Karte einem eigenen Test-Agenten mit 60 min gibt oder durch die Reservekarte ersetzt.
  - Bauhinweise (aus GEN-01/G1-06/NACHTRAG.md uebernommen, dazu eigene Lesebefunde; keine Rechnung):
    - Basis RUNDE-07/r5f/r5f.py, Befehl fuettern (Teile mechanik, raster55, raster70; importiert die unveraenderten
      Kopien r5a.py und r5b.py aus demselben Ordner, alle drei in den Kartenordner kopieren). RUNDE-07/r5f ist ein
      laufender Ordner: nur kopieren, nichts darin aendern.
    - Paket: r5f.paket_sigma(x, nu, eps, vz, sigma, x0); die Laufliste fu_laeufe(teil) durch eine eigene Liste
      ersetzen (omega^2 = 0,55: nu_r = 2,118, eps = 0,005 bis 0,05; omega^2 = 0,70: nu_r = 2,330; Gegenproben laut
      Karte), --T 1200.
    - Zeitachse: Gruppengeschwindigkeit bei nu = 2,118 etwa 0,88; Paketmitte von x0 = -150 bei etwa t = 170 am Ball;
      Speicher bei 0,55 nach 8/0,0102 = 784 auf e^-8; Messung ab t - Ankunft >= 800 passt in T = 1200. Abtastung alle
      0,25 gibt Nyquist 12,6, reicht fuer die Linie bei 3,5 bzw. 3,8.
    - Beim Filter beachten: Auch das einlaufende Paket kann ueber den kubischen Term direkt bei 2 nu - omega
      abstrahlen (ebenfalls Ordnung eps^4 in der Ladung). Die Karte trennt das nicht; die Gegenprobe "Paket allein"
      misst genau diesen Anteil und muss mit dem Ball-Lauf verglichen werden.
    - Linienenergie: E_Linie/Q_Linie aus Energie- und Ladungsfluss am Detektor (x = +-100) nach Bandfilter; bei einer
      einfarbigen Linie muss das Verhaeltnis 2 nu - omega sein (Plausibilitaet der Karte).
  - Die Karte kann scheitern (Exponent, Linie, Bilanz); kein "L1 schwach".

- 2026-09-30 11:30:37 CEST, Leitung: bleibt geparkt, nicht getestet (zum zweiten Mal; Bau 40 bis 60 min). Das wird wie die ungetesteten
  Karten in Generation 1 behandelt (G1-08, ebenfalls Arm Z, zaehlte ungetestet mit). Kein Ersatz durch die Reserve,
  damit die Behandlung ueber beide Generationen gleich bleibt.
