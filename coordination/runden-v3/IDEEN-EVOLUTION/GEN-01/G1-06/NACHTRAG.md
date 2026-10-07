# G1-06 Nachtrag (nach dem Stempel 07:52:18, vor jedem Lauf)

- 2026-09-30 08:12:44 CEST, T-1: **geparkt**, kein Code, keine Formprobe, keine LAUF.txt. Grund: Zeitbox 45 min fuer fuenf Karten;
  G1-02, G1-07 und G1-05 (a) gingen vor. Neuer Code (Detektor-Zeitreihen mit Bandfiltern, mitgefuehrtes
  Ballfenster, eigene eps/nu-Listen) nach eigener Schaetzung 45 bis 60 min.
- Bauhinweise fuer den naechsten Test-Agenten (nur Lesebefunde und Kopfrechnung, keine Rechnung auf dem Rechner):
  - Basis RUNDE-07/r5f/r5f.py Befehl fuettern (importiert unveraenderte Kopien r5a.py und r5b.py aus demselben
    Ordner; alle drei mitkopieren).
  - Zeitachse: Gruppengeschwindigkeit bei nu = 2,118 etwa sqrt(nu^2 - 1)/nu = 0,88; Paketmitte von x0 = -150 bei
    etwa t = 170 am Ball; Speicher bei omega^2 = 0,55 nach 8/0,0102 = 784 auf e^-8; Messung ab t - Ankunft >= 800
    passt in T = 1200. Abtastung alle 0,25 gibt Nyquist 12,6, reicht fuer die Linie bei 3,5 bzw. 3,8.
  - Beim Filter beachten: Auch das einlaufende Paket kann ueber den kubischen Term direkt bei 2 nu - omega
    abstrahlen (ebenfalls Ordnung eps^4 in der Ladung). Die Karte trennt das nicht; das ist ein Hinweis, keine
    Aenderung.
- Die Karte kann scheitern (Exponent, Linie, Bilanz); kein "L1 schwach".
