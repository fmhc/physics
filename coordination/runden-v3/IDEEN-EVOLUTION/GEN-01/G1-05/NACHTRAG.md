# G1-05 Nachtrag (nach dem Stempel 07:52:18, vor jedem echten Lauf)

- 2026-09-30 08:11:45 CEST, T-1:
  - Geparkt: Teil (b) (medium1d.py landau mit T = 1500, Box 1600, Solitonzaehler an der Sonde x = +40, F_spaet,
    Kraft je 100er-Fenster, Gegenproben lam = 0 und u = 0). Grund: Zeitbox; medium1d.py hat 1058 Zeilen, der Umbau
    braucht nach eigener Schaetzung 30 bis 45 min und laeuft laut Karte ohnehin erst nach (a).
  - Teil (a): Das in der Karte beschriebene Schiessen "vom stromauf liegenden Fixpunkt ab x = -60" ist numerisch
    nicht machbar: der noetige Abstand vom Fixpunkt liegt bei exp(-kappa 60), fuer C0 = 0,3 und kleines u unter 1e-20,
    und beim gestreckten Profil stoert dessen Schwanz den Start. Die erste Formprobe (08:08) fand darum beim
    gestreckten Profil gar keine Loesung. Umgestellt auf Schiessen von der Mitte (a(0) = a_c, a'(0) = 0) mit
    Klassifizierung ueber/unter a0; gesucht ist dieselbe symmetrische Loesung, die gegen den Fixpunkt laeuft. Das ist
    eine Aenderung des Rechenwegs, nicht der Vorhersage; keine Zahl der Formprobe wurde verwendet.
  - u-Raster: erst 0,05 c_s, dann 0,005 c_s vor dem ersten u ohne Loesung (Karte: Schritte von 0,005 c_s); ein
    Wiederauftauchen einer Loesung ueber einer Luecke wird gemeldet (Plausibilitaet).
  - Kontrollen (lam = 0,01 und vierfach gestrecktes S) rechnet der Code fuer alle drei C0; die Karte nennt kein C0.
  - Die Liste fuer Teil (b) (u_SN + 0,30 c_s) kann ueber c_s liegen; dann waere dieser Lauf ueberschallig.
  - Papiertest kann scheitern (V1 gegen die gemessenen Klammern); kein "L1 schwach".
