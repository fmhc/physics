# G2-07 Nachtrag (Test-Agent T-2)

- 2026-09-30 11:27:28 CEST (date): Code, Formprobe und LAUF.txt. KARTE.md unveraendert seit "Vorhersage geschrieben:
  11:06:31".
- Code ring_skalierung.py = Kopie von RUNDE-07/ring/ring.py. Neu nur der Unterbefehl "skalierung" (Abschnitt G2-07 vor
  dem Hauptprogramm) und --w2. Aufbau des Rings (Seite d = 2 R_halb + Luecke, Phase k pi/2, Saat als Amplitude
  1 + 1e-6 auf Ball 0), Zeitentwicklung, C4-Projektion, Verfolger und vierer_auswerten (Klasse, Bruch, Drehrate) sind
  unveraendert.
- Lesarten und Zusaetze (gekennzeichnet):
  - Fitfenster: Die Karte nennt "Spreizung 1e-5 bis 1e-2". Das Original fittet von 10 x Startspreizung bis 3e-2. Die
    Steigung, die Punkte und L3 benutzen "gamma_karte" (Kartenfenster, vor dem Bruch, mindestens 8 Punkte); das
    Original-gamma steht als "gamma_spreizung" zum Vergleich daneben. Die Vergleichswerte der Karte bei 0,70 (0,0534,
    0,0275) kommen aus dem Originalfenster.
  - Nachbarabstand d = sqrt(2) r_mittel (r = mittlerer Abstand der vier Verfolger vom Mittelpunkt, bis zum Ende der
    Gueltigkeit, also vor dem Bruch). Die Schranke [0,8; 1,25] d_start pruefe ich ueber r_min und r_max relativ zu r_start
    (fuer das Quadrat gleichwertig).
  - Ein Punkt zaehlt nur mit Klasse "Ladungstausch", gamma_karte vorhanden und Abstand in der Schranke. Fehlt mehr als ein
    Punkt je omega^2: "nicht entscheidbar". "ausgang" = nicht entscheidbar / scheitert / offen / bestanden.
  - V3 (Linearitaet) braucht mindestens drei Punkte; mit zwei Punkten ist V3 "None".
  - Gegenprobe mit derselben Saat wie die Hauptlaeufe und C4-Projektion; die Spreizung wird ab t = 1 gewertet, weil der
    Startwert die Saat selbst ist (2e-6). Formprobe: ab t = 1 etwa 3e-16, die Projektion entfernt die Saat.
  - fein: T = 2000 wie grob (die Karte nennt fuer fein kein T; das Original nutzte 1000). Ohne Bruch vor T gibt es kein
    gamma fuer L3.
  - Bilanz fuer die Schranke "Q, E, J auf 1e-4 bis zum Bruch": Rest wie in bilanz() des Originals (Box plus geschluckte
    Menge in der Randschicht), aber nur bis t_Bruch; Q und J relativ zu Q_Box(0), E zu E_Box(0).
  - t_Bruch-Probe: t_Bruch gegen ln(0,1 / Spreizung_Start) / gamma_karte auf 30 %.
- Formprobe 11:18:41 bis 11:19:09 und 11:24:56 bis 11:25:31 (lokal, CPU, --rauch --mini, T = 40): alle Aufrufe rc 0.
  Im Mini-Fenster gibt es keinen Tausch; der Steigungszweig lief lokal nicht. Zahlen nicht ernten.
- Papiertest: Die Baender um -kappa/2 koennen verfehlt werden (-kappa und -2 kappa liegen ausserhalb); L1 nicht schwach.

- 2026-09-30 11:31:44 CEST, Leitung (vor jedem echten Lauf): angenommen sind die Steigung im Fitfenster der Karte (1e-5 bis 1e-2), wobei
  beide Werte ins JSON kommen, der Feinlauf mit T = 2000 und die Gegenprobe mit derselben Saat.
