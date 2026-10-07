# G2-04 Nachtrag (nach dem Stempel 11:16:14, vor jedem echten Lauf)

- 2026-09-30 11:28:26 CEST, T-1:
  - Code: gleiten_mc2.py, Kopie von RUNDE-06/medium1d/medium1d.py; neu nur der Abschnitt "G2-04" (Unterbefehle
    gleiten_mc2 = Hauptlauf mit 23 Laeufen, gleiten_mc2_gegen = Gegenprobe mit 4 Laeufen) und zwei TESTS-Eintraege.
    Dynamik, Box, Rampen, Falle, Messfenster [370, 570] und Hann-Mittel unveraendert. Neuer Code etwa 15 min.
  - Vor jedem Lauf festgelegt, wo die Karte offen ist:
    - u/c_s und k' mit dem mc2 des Laufs (das Original rechnete in auswertung_kraft mit mc2 = 1; im neuen Abschnitt
      berichtigt, der alte Code bleibt unberuehrt).
    - u_10: log-linear in F zwischen den Rasterpunkten; ist F am oberen Punkt <= 0, linear.
    - Sammelprobe: log10(F/F_max) oberhalb des Maximums bis F/F_max = 1e-3, je Punkt gegen die lineare Interpolation
      der anderen Kurve (nur im gemeinsamen Bereich); "zusammen" heisst hoechstens log10 3 fuer alle drei Paare.
      mc2 = 1 hat nur die drei Punkte 0,30 / 0,50 / 0,60.
    - Spiegel: F(-0,90) gegen einen Partnerlauf +0,90 im selben Aufruf (deshalb 4 Gegenproben-Laeufe, nicht 3).
    - Medium allein, "am Ende C0 auf 1e-3": relativ gelesen, |C_fern/C0 - 1| <= 1e-3.
    - "F >= 0" woertlich ohne Toleranz.
    - L3: F auf 10 % (nur |F| >= F_MIN) und F-Effekt >= 5 x Aenderung; u_10 auf 0,01 und Verschiebung gegen mc2 = 1
      >= 5 x Aenderung.
  - Hinweis vor dem Lauf (Lesebefund, keine neue Rechnung): Im bekannten Lauf RUNDE-06 gleiten (mc2 = 1) weicht
    F_Falle von -F_med um 15 % (u = 0,5) und 54 % (u = 0,6) ab, bei 0,8 und 0,9 ist |F_Falle| viel groesser als |F_med|
    (F_std >> F). Die 20-%-Fallenbilanz der Plausibilitaet kann deshalb an Punkten mit kleinem F reissen. Die Regel
    "nicht entscheidbar" der Karte betrifft nur die beiden Rasterpunkte um u_10 bei mc2 = 0 und 0,25; die Karte bleibt
    unveraendert.
  - Formprobe (lokal, CPU, 1 Faden, nice 19, Zeitfaktor 0,02, 11:21:38 bis 11:22:12): beide Unterbefehle rc 0,
    alle Pruefungen und L3 laufen durch. Keine Aussage daraus.
  - Die Karte kann scheitern (u_10 bei zwei mc2, Gegenbilder G-Mach und G-u); kein "L1 schwach".
