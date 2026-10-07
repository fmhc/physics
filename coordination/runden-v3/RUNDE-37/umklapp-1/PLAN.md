# UMKLAPP-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 46, Finn-Auftrag "Try it")

- Start 2026-10-05 05:54:29 CEST (date). Plantext ab 06:14:02 CEST (date), vor jeder Hauptrechnung. Zeitbox 120 min, also
  bis 07:54:29 CEST; danach startet kein Lauf.
- Grundlage: KARTE.md (UK0 bis UK3; Wortlaut, Schwellen, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] vorab ableitbar, [E] hier gerechnet, [P] Projektdatei, [F] eigene Festlegung, [H] Hypothese,
  [L] Literatur aus dem Gedaechtnis. Alles ist synthetische Gitterrechnung, keine Messdaten.
- Code: code/uk.py (neu), code/uk_auswertung.py (neu), code/uk_bild.py (neu); tg.py, tg_auswertung.py, ew.py, tp.py
  unveraendert aus TT-GLAS-1 kopiert (sha256 wie dort: ec48a258..., 88cbd2ce..., fa7b6417..., 419d7da6...).
- Vor diesem Text liefen drei Rauchtests (Abschnitt 8); gelesen nur Rueckgabewerte, Laufzeiten, Speicher und Schluessel.

## 1. Ableitbarkeitsprobe

- **UK0 ist vorab ableitbar [M]** (wie die Karte sagt). Ein 2-3-Zug zerlegt die konvexe Doppelpyramide aus zwei
  Tetraedern neu in drei. Die Diederwinkelsumme an jeder Randkante der Doppelpyramide bleibt gleich, die neue Kante d-e
  liegt im Inneren und hat Summe 2 pi. Alle Fehlwinkel bleiben also, was sie waren; im flachen Netz null. Die Rechnung
  prueft nur, dass der Code die Zuege richtig ausfuehrt (Rundung).
  - Zusatz [M, nicht Teil von UK0]: Dasselbe Argument gilt auch auf einem gekruemmten stueckweise flachen Netz, wenn die
    neue Kante die Laenge aus der flachen Einbettung der Doppelpyramide bekommt (zwei Tetraeder sind immer flach
    einbettbar). Die Regge-Wirkung ist dann gegen 2-3-Zuege exakt invariant. Nicht gerechnet.
- **UK1 ist weitgehend vorab ableitbar [M, mit Annahme].** Fuer Poisson-Punkte ist der Randabstand mu einer Flaeche
  (Lage der Gegenecke zur Umkugel, Abschnitt 3) stetig verteilt. Die Wahrscheinlichkeit, dass die Gegenecke in einer
  duennen Schale ausserhalb der Umkugel liegt, ist proportional zur Schalendicke, also hat mu eine endliche, positive
  Dichte bei null [M, Kopfrechnung: Poisson-Dichte mal Kappenflaeche]. Dann ist der Ensemble-Mittelwert des Anteils
  umgeklappter Flaechen bei kleinem a linear in a, ohne Schwelle. Nicht ableitbar sind der Vorfaktor und der Bereich, in
  dem das gilt (Saettigung bei grossem a; endliche Netze haben einen kleinsten Randabstand, also je Netz eine Schwelle,
  die erst das Mittel ueber Netze verwischt). Die Rechnung misst Vorfaktor und Steigung; ein "eingetroffen" waere
  keine Entdeckung.
  - Folge fuer die Statistik [F]: Bei kleinem a traegt die Zahl unabhaengiger Netze (Randabstaende), nicht die Zahl der
    Ziehungen je Netz. Deshalb 48 Netze je N mit je 8 Ziehungen.
- **UK2 und UK3 sind nicht ableitbar.** Nach einem Zug wechseln Kanten und Tetraeder; die Bewegungsenergie (J = 1 je
  Tetraeder) und die Regge-Matrix B haengen an der Zerlegung. Vorab nur: Mit 2-3-Zuegen allein waechst die Zahl der
  Tetraeder um 1 je Zug und die Zahl der Kanten um 1 je Zug [M]; bei f = 0,2 sind das +40 % Tetraeder und etwa +35 %
  Kanten. Das Tempo kann sich schon dadurch aendern [H].
- **Zum Massstab von UK3 [P, H]:** In TT-GLAS-1 streut die Spanne von Netz zu Netz um 25 % (N = 128) bzw. 17 % (N = 256)
  des Mittels [P]. Wird ein Netz durch viele Zuege "neu gewuerfelt", kann sich seine Spanne schon dadurch um ~20 %
  aendern, ohne eine phasonartige Kopplung. Die Auswertung gibt dazu beschreibend das Zufallsniveau aus: Median von
  |s_j / s_i - 1| ueber Paare verschiedener TT-GLAS-1-Netze gleicher Groesse.
- **Projektsuche** (grep mit den vorgeschriebenen Ausschluessen ueber RUNDE-37, nur Dateinamen): Zufaellige Pachner-Zuege
  auf Zufallsnetzen mit TT-Auswertung gibt es nicht; PACHNER-TAKT-1 rechnete Diagonalwechsel auf einem regelmaessigen
  Netz mit Zeltstangen [P]. Rohdaten, aus denen UK1 bis UK3 schon folgen, gibt es nicht.

## 2. Der 2-3-Zug (Festlegungen [F])

- **Netz:** periodisches Poisson-Delaunay-Netz von TT-GLAS-1 (tg.zufallsnetz, N Punkte, Dichte 1, Saat
  default_rng([4537, N, saat])). Im Torus sind alle Flaechen innen; jede gehoert zu genau zwei Tetraedern.
- **Erlaubte Flaeche:** Flaeche abc zwischen T1 = abcd und T2 = abce (T2 in den Rahmen von T1 verschoben). Erlaubt, wenn
  1. die drei neuen orientierten Volumina V(abde), V(bcde), V(cade) dasselbe Vorzeichen haben (die Strecke d-e
     durchstoesst das Innere von abc: konvexe Doppelpyramide; dann sind alle drei Volumina positiv und fuellen dasselbe
     Gebiet);
  2. jedes neue Volumen mindestens 1e-3 mal das mittlere Tetraedervolumen des Ausgangsnetzes ist (numerisch positiv;
     etwa das kleinste Delaunay-Tetraeder in TT-GLAS-1 mit 1,1e-3 [P]);
  3. d und e verschiedene Ecken sind (keine Selbstkante) und die Kante d-e (mit Kastenversatz) im Netz noch nicht
     existiert (keine doppelten Kanten).
- **Zug:** T1, T2 werden durch abde, bcde, cade ersetzt; jedes neue Tetraeder wird so verschoben, dass sein Schwerpunkt
  im Grundwuerfel liegt.
- **Zufallsfolge:** Je Schritt wird unter allen derzeit erlaubten Flaechen gleichverteilt eine gewaehlt
  (default_rng([4538, N, saat])); nach jedem Zug wird die Liste neu berechnet. Ziel: n = round(f F0) Zuege, F0 = Zahl der
  Flaechen des Ausgangsnetzes (= 2 T0). Die Folge ist fuer alle f dieselbe; das Netz bei f = 0,05 ist ein Zwischenstand
  der Folge fuer f = 0,2. Gibt es keine erlaubte Flaeche mehr, endet die Folge; ausgewiesen wird f_eff = n / F0.
- Nur 2-3-Zuege, keine 3-2-Zuege (Karte). Ausgewiesen werden je Netz die Anteile konvexer und erlaubter Flaechen zu
  Beginn und am Ende.

## 3. M-B: Delaunay nach Eckverschiebung (Festlegungen [F])

- **Verschiebung:** delta_i = a * lbar / sqrt(3) * xi_i, xi_i standardnormal (3 Komponenten), lbar = mittlere
  Kantenlaenge des Ausgangsnetzes; Effektivwert |delta| = a * lbar. Je Netz 8 Ziehungen xi (default_rng([4539, N, saat])),
  fuer alle a dieselben (gemeinsame Zufallszahlen). a = 1e-4, 1e-3, 1e-2, 3e-2, 1e-1. Lagen nicht zurueckgefaltet.
- **Delaunay neu:** dieselbe periodische Triangulierung wie tg.zufallsnetz (27 Kopien, Saum 4, Schwerpunkt im Wuerfel)
  fuer die verschobenen Lagen. Selbsttest je Netz: ohne Verschiebung entsteht genau die Ausgangsmenge.
- **Gezaehlt (Hauptgroesse, Urteil):** Anteil geaenderter Tetraeder phi_T = |T_alt \ T_neu| / |T_alt| (Tetraeder als
  kanonische Schluessel aus Ecken und relativen Kastenversaetzen).
- **Beschreibend:**
  - Zahl der Zuege: zusammenhaengende Aenderungsbereiche (entfernte und neue Tetraeder, verbunden ueber gemeinsame
    Flaechen) mit Typ (entfernt, neu): (2, 3) = ein 2-3-Zug, (3, 2) = ein 3-2-Zug, sonst zusammengesetzt. Die Zahl der
    Bereiche ist eine Untergrenze der Zugzahl.
  - phi_F = Anteil der Flaechen der alten Verbindung, die nach der Verschiebung die Delaunay-Bedingung verletzen
    (mu < 0, mu = (|e - C1|^2 - R1^2) / R1^2 mit Umkugel (C1, R1) von T1).
  - Randabstaende mu0 im Ausgangsnetz: Zahl der Flaechen mit mu0 < x (x wie a) und Steigung dieser Verteilung (Dichte bei
    null), dazu min mu0 und Zahl mu0 < 0 (Probe, soll 0 sein).
  - Zusatz W (Welle im Grenzfall langer Wellen): affine TT-Dehnung x -> (1 + a h) x mit h = die zwei TT-Polarisationen
    (Frobeniusnorm 1, wie tg.affin) in [100], [110], [111]; gezaehlt nur phi_F.
- **Netze:** N = 128 und 256, je Saaten 1 bis 48.

## 4. Wirkung auf die TT-Wellen (Festlegungen [F])

- Netz nach round(f F0) Zuegen (Abschnitt 2), dann unveraendert tg.modell und tg.spektrum (Modell von EINE-WELT-LOCH-1,
  A1R1, J = 1 je Tetraeder, |k| = 1e-2 in 13 Wuerfelrichtungen, dazu 2e-2 in [100], [110], [111]; Klassen wie TT-GLAS-1).
  Kennzahlen je Netz mit tg_auswertung.netz_kennzahlen (unveraendert): regulaer, Spanne (max/min - 1 der 26 Werte
  omega^2/k^2), mittleres omega^2/k^2, Aufspaltung, Richtungsspanne, wachsend, unklar, A_red positiv definit, B_red
  negativ, TT-Anteil, Linearitaet, Luecke. Dazu mittleres Tempo = Mittel von sqrt(omega^2/k^2).
- **Netze:** f = 0, 0,05, 0,2.
  - N = 128: Saaten 1 bis 4 bei f = 0 (selbst gerechnet; Vergleich mit TT-GLAS-1), 0,05 und 0,2.
  - N = 256: f = 0 aus TT-GLAS-1 (lauf/netz-N256-s1..3.json, gleicher Code, gleiche Netze [P]); Probe: Richtung [100]
    selbst gerechnet, Abweichung ausgewiesen. f = 0,2: Saaten 1 und 2, Saat 3 wenn die Zeit reicht; f = 0,05: Saat 1,
    wenn die Zeit reicht. (Grund: Rauchtest r3, 55 bis 58 s je k-Punkt bei N = 256 und f = 0,2, also ~15 min je Netz.)

## 5. Urteilsregeln (mechanisch in code/uk_auswertung.py)

- **UK0** (alle Kontrollnetze N = 128 und 256, Saaten 1 bis 4, f = 0,05 und 0,2; nur Netze mit mindestens einem Zug):
  S = sum_e l_e (2 pi - sum_t theta_te).
  - Nach Plan: eingetroffen genau dann, wenn max |S_f - S_0| / (2 pi sum_e l_e) <= 1e-10.
  - Nach Kartenwortlaut ("auf <= 1e-10"): max |S_f - S_0| <= 1e-10 (absolut, Laengeneinheit = Punktabstand bei Dichte 1).
  - Beschreibend: groesster Fehlwinkel, Volumensumme, affine TT-Steifigkeit (tg.affin) vor und nach den Zuegen.
- **UK1** (phi_T je a = Mittel ueber Netze des Mittels ueber Ziehungen; Steigung = Kleinste-Quadrate-Gerade ln phi_T
  gegen ln a ueber a = 1e-3, 1e-2, 3e-2):
  - Nach Kartenwortlaut: Steigung ueber alle 96 Netze (beide N gemeinsam) in [0,8; 1,2].
  - Nach Plan: Steigung fuer N = 128 und fuer N = 256 je in [0,8; 1,2], und "ohne Schwelle": phi_T(1e-4) > 0 fuer beide N
    und lokale Steigung zwischen 1e-4 und 1e-3 (alle Netze) in [0,8; 1,2].
  - Fehlt ein N, ist UK1 nicht entscheidbar.
- **UK2** (alle vollstaendigen Netze bei f = 0,2):
  - Nach Plan: jedes ist "regulaer" nach TT-GLAS-1 (an allen 16 Punkten genau 2 masselose Moden, beide positiv, keine
    wachsende oder unklare Mode, TT-Anteil >= 0,99 an [100], [110], [111], linear auf 1 %).
  - Nach Kartenwortlaut: an allen 16 Punkten genau 2 masselose Moden, beide positiv, TT-Anteil >= 0,99 an den drei
    TT-Richtungen, keine wachsende Mode (stabil).
  - Kein vollstaendiges Netz: nicht entscheidbar; fehlt ein N, steht das als Vermerk dabei.
- **UK3** (Paare gleicher Saat und gleichen N, f = 0 und f = 0,2 beide regulaer; r = Spanne(0,2) / Spanne(0) - 1):
  - Nach Plan: eingetroffen genau dann, wenn der Median von |r| > 0,2.
  - Nach Kartenwortlaut ("je Netz um mehr als 20 %"): jedes |r| > 0,2.
  - Beschreibend: r auch fuer f = 0,05; Aenderung von mittlerem omega^2/k^2 und Tempo; Zufallsniveau (Abschnitt 1).
- Bricht ein Lauf ab, gehen nur vollstaendige Netze ein (13 Richtungen).

## 6. Agenten-Vorhersagen (vorab; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Zu Beginn sind zwischen 30 % und 70 % der Flaechen 2-3-erlaubt (alle Bedingungen) | 60 % |
| A2 | f = 0,2 wird in allen Netzen erreicht (f_eff = 0,2) | 75 % |
| A3 | Mittleres omega^2/k^2 bei f = 0,2 liegt im Mittel mehr als 10 % ueber f = 0 (mehr Tetraeder mit J = 1) | 60 % |
| A4 | phi_T / a bei a = 1e-3 (alle Netze) liegt zwischen 1 und 10 | 55 % |
| A5 | Bei a = 1e-3 sind mindestens 90 % der Aenderungsbereiche einzelne 2-3- oder 3-2-Zuege | 70 % |

## 7. Laeufe auf der .69 (kleintest.sh, Spuren cpu3 und cpu4, je 1 Thread, <= 600 s)

- Einmalige Laufketten code/kette-cpu3.sh und code/kette-cpu4.sh, gestartet per ssh aus der Laptop-Sitzung (kein Dienst,
  kein Timer). Schlusszeit: nach 05:10:00 UTC (07:10 CEST) startet kein neuer Lauf. Danach code/uk_auswertung.py
  (--lauf lauf --ttglas /home/fmh/fmhc-physics-remote/tt-glas-1/lauf) und code/uk_bild.py (Spur cpu3). Arbeitsordner
  /home/fmh/fmhc-physics-remote/umklapp-1/.
- cpu3 (Schaetzung aus den Rauchtests): uk-ko128 und uk-ko256 (Kontrolle, Saaten 1-4, ~2 min); uk-mb128 (Saaten 1-48,
  ~3 min); uk-tt128-f0 (Saaten 1-4, ~2,5 min); uk-tt128-f02a/b (Saaten 1-2 bzw. 3-4, je ~4,5 min); uk-tt256-s1-f02-A/B/C
  (Richtungen 0-3, 4-8, 9-12; je ~5 bis 6 min); uk-tt256-s3-f02-A/B.
- cpu4: uk-mb256a/b (Saaten 1-24 bzw. 25-48, je ~2 min); uk-tt256-s2-f02-A/B/C; uk-tt128-f005 (Saaten 1-4, ~3 min);
  uk-tt256-f0p (f = 0, Saaten 1-3, nur Richtung 0, ~2 min); uk-tt256-s1-f005-A/B (Richtungen 0-5, 6-12); uk-tt256-s3-f02-C.
- Geschaetzt ~40 min je Spur. Was nach der Schlusszeit nicht startet, fehlt und wird ausgewiesen.

## 8. Rauchtests vor diesem Plan (.69 in UTC)

- r1 (04:11:08 bis 04:11:14): Kontrolle N = 128, Saat 901, --rauch. r2 (04:11:08 bis 04:11:10): M-B N = 256, Saat 901,
  2 Ziehungen, --rauch. r3 (04:11:14 bis 04:13:30): TT N = 256, Saat 901, f = 0,2, nur Richtung 0, --rauch.
- Gelesen: Rueckgabewerte (alle 0), Laufzeiten (5,7 s; 1,4 s; 135,6 s, davon 57,9 s fuer den k-Punkt mit TT-Anteil),
  Speicher (<= 805 MB), Schluessel. Keine Werte.
- Nachtrag 06:18:37 CEST (date), nach dem Plantext Abschnitte 1 bis 6: r4 (04:16:02 bis 04:18:10 UTC) ohne --rauch auf
  Rauchsaaten (Kontrolle N = 128 Saat 901; M-B N = 128 Saaten 901, 902 und N = 256 Saat 901 mit 2 Ziehungen; TT N = 128
  Saat 901 bei f = 0 und 0,2; Auswertung und Bild als Absturzprobe). Gelesen: Rueckgabewerte (alle 0), Laufzeiten (TT
  N = 128: 34,6 s bei f = 0, 124,9 s bei f = 0,2) und die Schluessel der Auswertung. Dabei sichtbar: UK3 hat in r4 nur
  die Schluessel plan/wortlaut, es entstand also kein Paar; mindestens eines der zwei Rauchnetze ist nicht regulaer.
  Werte und Gruende habe ich nicht gelesen. Regeln (Abschnitte 2 bis 5) unveraendert.
