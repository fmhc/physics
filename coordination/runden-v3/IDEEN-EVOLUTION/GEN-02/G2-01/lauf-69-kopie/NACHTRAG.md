# G2-01 Nachtrag (Test-Agent T-2)

- 2026-09-30 11:27:28 CEST (date): Code, Formprobe und LAUF.txt. KARTE.md unveraendert seit der Zeile "Vorhersage
  geschrieben: 11:06:31" (inhaltlich vollstaendig: Vorhersage mit "Scheitert, wenn", Gegenprobe, Schranke).
- Code teilung_m3.py (Kopie von GEN-01/G1-03/teilung_schwelle.py). Geaendert nur Laufliste, T, L als Argument,
  Kennzahlen und Profilprobe; jede Aenderung mit "G2-01" markiert. Schiessen, Gitter, Zeitschritt, Randschicht,
  Gebietsanalyse und gamma-Fit sind unveraendert.
- Umsetzung der Karte (Lesarten, gekennzeichnet):
  - Drei Teile, weil die Laeufe eines Aufrufs ein gemeinsames Gitter haben: haupt (m = 3, L = 48,0), eich (m = 2,
    L = 38,4), gegen (m = 0, L = 48,0).
  - V1: Folge Teilung ja/nein ueber omega^2 springt hoechstens einmal von nein auf ja; 0,530 und 0,535 teilen nicht,
    0,550 und 0,560 teilen.
  - V2: Gerade gamma^2 gegen omega^2 durch die zwei tiefsten teilenden m = 3-Laeufe mit gamma-Fit, Nullpunkt in
    [0,540; 0,548]; "gamma faellt nicht" = gamma nicht fallend ueber alle teilenden m = 3-Laeufe.
  - V3: m = 2 bei 0,560 und 0,565 teilt nicht (Datei des eich-Aufrufs) UND alle Toechter der m = 3-Teilungen haben
    Windung 0. Ohne eich-Datei ist V3 "None".
  - Ausgaben "scheitert" (V1 bis V3) und "scheitert_hypothese_V1_V2" getrennt, weil laut Karte nur V1 und V2 die
    Hypothese pruefen.
  - L3: gleicher Ausgang und gleiche Toechterzahl, gamma-Aenderung hoechstens 0,2 relativ (wie G1-03).
- **Profilprobe "S_max < 1" (Leitung entscheidet vor dem Lauf):** Die Karten-Schranke ist in 2D physikalisch
  verletzbar. Die hoechste moegliche Dichte eines Balls ist f_top^2 = (2 + sqrt(6 omega^2 - 2))/3; fuer omega^2 > 1/2
  liegt sie ueber 1 (1,047 bei 0,55; 1,033 bei 0,535). Korrekt geschossene 2D-Profile aus RUNDE-07/ring (2048
  Kandidaten) haben fuer m = 0 S_max 1,0465 (0,55) bis 1,0646 (0,59); dieselben Werte liefert die Formprobe. Damit
  faellt die Schranke sicher bei der Gegenprobe (m = 0 bei 0,55 und 0,56) und vermutlich bei m = 3 nahe 0,530 bis 0,540,
  ohne dass ein Profil falsch ist. Ich habe die Schranke nicht geaendert ("plausibilitaet_bestanden" wird dann false).
  Als reine Info steht je Profil "info_f_top2_obergrenze" daneben (nicht in "bestanden"). Vorschlag an die Leitung:
  vor dem Lauf festlegen, ob ein Verfehlen von S_max < 1 bei S_max < f_top^2 als Schrankenfehler gilt.
- Formprobe 11:14:33 bis 11:15:38 und 11:17:04 bis 11:17:33 (lokal, CPU, --rauch --mini): alle Aufrufe rc 0; in der
  laengeren Probe (T = 120 auf dem Mini-Gitter) teilte sich kein m = 3-Ball, der V2-Nullpunktzweig lief deshalb lokal
  nicht, er ist aber bis auf das Band gleich dem auf der .69 gelaufenen G1-03-Code. Zahlen nicht ernten.
- Papiertest: Das Band [0,540; 0,548] stammt aus der veroeffentlichten Evans-Zahl und kann in beide Richtungen verfehlt
  werden; L1 ist nicht schwach.

- 2026-09-30 11:31:44 CEST, Leitung (Entscheidung vor jedem echten Lauf, ohne Ergebnis; Zusatz der Leitung, gekennzeichnet): Die Profilprobe
  "S_max < 1" ist physikalisch falsch gewaehlt.
  - Fuer ein radiales Profil in d >= 2 gilt S_max < S_h(omega^2) = (2 + sqrt(6 omega^2 - 2))/3, der Gipfel des
    effektiven Potentials V = (omega^2 S - U(S))/2, bei beta = 0,5.
  - Das sind 1,047 bei omega^2 = 0,55, 1,0 bei 0,5 und 1,109 bei 0,65. Korrekt geschossene Profile liegen darueber, z. B.
    m = 0 bei 0,55 mit S_max 1,0465.
  - Die Probe lautet deshalb ab jetzt S_max < S_h(omega^2). Das berichtigt eine falsch angesetzte Schranke und lockert
    nichts nach einem Befund; es gibt noch kein Ergebnis.
  - Der Code gibt S_max aus; die Ernte vergleicht mit S_h.
