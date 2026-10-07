# G2-10 Nachtrag (Test-Agent T-2)

- 2026-09-30 11:29:42 CEST (date): Code, Formprobe und LAUF.txt. KARTE.md unveraendert seit "Vorhersage geschrieben:
  11:06:31".
- Code bic2_2d.py = Kopie von RUNDE-07/bic2/bic2_v2.py. Aenderungen mit "G2-10" markiert:
  - --dim: Raumdimension der Profile in profile_stapel und nu = (dim - 1)/2 (l = 0) an allen vier Stellen im Befehl kurve
    (W-Abtastung, Newton, Verfeinerung). Vorgabe 3 = bisheriges Verhalten. Die uebrigen Befehle (exakt, pole, ...) sind
    unveraendert.
  - barriere: nur Profile; S0, dp(S0) = 1 - 4 S0 + 9 beta S0^2, c(eps)^2, B = dp - c^2, Q und Virialrest in dim
    Dimensionen; x_B = groesstes omega^2 der Liste mit B > 0 (Kartenwortlaut). Kein Pol geht ein. Eigener Aufruf vor der
    Polsuche (Stufe A in LAUF.txt), wie von der Leitung verlangt.
  - leiter: liest kurve.json und barriere.json und wertet nach der Karte aus; rechnet nichts neu.
- Raster (Abweichung vom Kartenraster, von der Karte selbst vorgesehen): Das Raster 0,002 passt nicht in 10 min (Profile
  auf der .69 15 bis 28 s, 83 Profile). Die Karte sagt "sonst Raster 0,004"; LAUF.txt nutzt 0,004 in sieben Stuecken mit
  je einem gemeinsamen Randwert.
- Verfeinerung (Lesart, gekennzeichnet): "Minima mit der signierten Wurzel verfeinern" setze ich wie in den 3D-Leiter-
  laeufen um: kurve sucht Vorzeichenwechsel von s = L(y_a) entlang eines Asts (Nulldurchgang der signierten Wurzel)
  und verfeinert mit der Sekante in omega^2 (4 Schritte, je ein neues Profil). Das feine Zusatzraster der Karte
  (+- 0,002 mit Schritt 0,0002, 21 Profile je Stelle) ist NICHT eingeplant; es kostet etwa zwei Aufrufe je Stelle und
  laesst sich mit kurve --omega2-liste nachholen. Leitung entscheidet.
- Lesarten in leiter (gekennzeichnet):
  - Stelle = Vorzeichenwechsel von s; Lage = verfeinerter Schritt mit kleinstem |s|, sonst lineare Schaetzung.
  - Zuordnung zu n: naechster Tabellenwert der Karte; fehlt ein n = 2 bis 5, zaehlt es in V1 als ausserhalb.
  - V2: Schritte in 1/eps nur zwischen n = 3 und 4 sowie 4 und 5.
  - V3: theta_2D = k_c R_2D/pi - n + 1/4 mit R_2D = (d - 1)/(4 sqrt(beta) eps) (Duennwandformel der Karte) und k_c aus
    dem gemessenen omega*^2 und Re rho* des Pols am verfeinerten Schritt. V3 steht nicht im Scheiterkatalog der Karte und
    wird nur berichtet.
  - V4: keine Stelle oberhalb x_B(2D). Liegt B > 0 auf dem ganzen Raster, ist x_B = 0,699 (Rasterende) und V4 auf dem
    Raster ohne Aussage; "x_B_zusammenhaengend_von_unten" steht als Info daneben.
  - Umlaufzahl: gibt der Code nicht aus.
  - Plausibilitaet: Im rho <= 1e-12 an allen konvergierten Polen, Re rho im offenen Fenster, Virialrest 2D <= 1e-6 (aus
    den barriere-Profilen, Trapez), Q ueber das Raster streng monoton.
  - Gegenprobe d = 1 mit nu = 0 (gerader Sektor, wie l = 0 in 1D).
- L3 braucht die Lagen aus dem Hauptlauf: Stufe E in LAUF.txt ist ein Handschritt der Leitung (x_lo, x_hi je Stelle aus
  leiter.json), ein Aufruf je Stelle mit --h 0,01 (halber Schritt, f_rand 1e-8 statt 1e-6, also groesserer Aussenrand).
- Formprobe 11:23:11 bis 11:23:42 (lokal, CPU, 1 Thread): barriere an 0,60 und 0,70, kurve --dim 2 an 0,595 und 0,599
  (60 rho-Punkte), leiter; alle rc 0. Ein 2D-Profil kostet lokal etwa 5 s. Zahlen nicht ernten.
- Passt nicht in 10 min als Ganzes: 22 Aufrufe je unter 10 min, etwa 100 CPU-Minuten (siehe LAUF.txt).

- 2026-09-30 11:31:44 CEST, Leitung (vor jedem echten Lauf): angenommen sind das Ausweichraster 0,004 (von der Karte vorgesehen), die
  eingebaute Verfeinerung statt eines Zusatzrasters, Stufe A (x_B) vor Stufe B und L3 (Stufe E) als Handschritt nach
  Stufe D. Die Leitung fuehrt die Stufen in dieser Reihenfolge aus.
