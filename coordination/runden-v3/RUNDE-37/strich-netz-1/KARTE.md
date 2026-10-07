# STRICH-NETZ-1: Wie viele Striche ergeben 20 Zufallspunkte, was sieht man von allen Seiten, wie laeuft eine Welle darauf, und gibt "Isotacheia relativ zu Kantenlaengen" allen Feldern dasselbe Tempo? (Runde 41)

- Leitung claude-primary. Karte, Schreibtisch und Wahrscheinlichkeiten geschrieben ab 2026-10-04 15:47:14 CEST (date),
  vor jeder Rechnung. Ordner angelegt 15:40:24.
- **Auftraege von Finn (04.10., woertlich):**
  - Nachricht zwischen 15:28 und 15:40: "untersuche auch noch mal eigenschaften von "strich" - zwei punkte in einem 2d
    raum haben eine länge und fläche von 1-2 und berühren sich nur an einem punkt. wenn man jetzt 20 punkte random in
    einen 3d raum packt, und den von allen seiten anschaut, wie viele punkt-strich verbindungen ergeben sich und wie kann
    eine bewegung darauf (eine welle?) aussehen?"
    isotacheia geschichte ggf gemittelt auf kantenlängen relativ funktioniert"
- **Zusammengelegt (Kopplung):** Beide Fragen betreffen Wellen und Tempo auf Netzen aus Zufallspunkten und Strichen.
  Ein Code-Agent, groesseres Budget.
- **Lesarten von "Strich" (vorab festgelegt; alle rechnen, keine bevorzugen):**
  - L-alle: jedes Paar
  - L-Gabriel: "die zwei beruehren sich, kein Dritter dazwischen" = keine weitere Kugel in der Kugel mit dem Strich als
    Durchmesser
  - L-Delaunay: natuerliche Nachbarn
  - L-Beruehrung: Punkte als Kugeln bis zur ersten Beruehrung aufgeblasen = jeder mit seinem naechsten Nachbarn
- **Projektbezug:**
  - SPIN-ZUFALLSNETZ-1: eingesetzter Weyl-Spinor auf einem Zufallsnetz mit Voronoi-Gewichten, im Mittel isotrop
    normiert (v = 1). v_Spitze 0,975 bis 1,008 bei abs(k) 0,14 bis 0,47; Rasterunsicherheit +-0,0025/abs(k), also bei
    kleinem k grob.
  - INDUZIERT-*: P1-FEM-Skalar auf Delaunay ("Zahl = Volumen").
  - AETHER-UHR-1: Nur eine gemeinsame Grenzgeschwindigkeit macht die Bewegung gegen das Netz unsichtbar.
  - LICHT-GLEICH-L: Gemeinsames Tempo braucht Abstimmung oder Symmetrie.
  - QCA-TETRA-1 QT3: DP-Weyl-Automat langwellig 1/sqrt(3) der Sprunggeschwindigkeit.
  - RUNDE-16/zwei-seiten: Finns Ticks als Vorzeichenwechsel der Orientierung.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [E] Messung im Modell, [H] Hypothese, [P] Projektdatei.

## Schreibtisch der Leitung (vor der Rechnung) [M, L; ungeprueft]

- **Alle Paare:** 20 Punkte ergeben 190 Striche.
- **Von allen Seiten:**
  - Fuer jedes Tripel A, B, C gibt es einen Grosskreis von Blickrichtungen (parallel zur Ebene ABC), in denen die drei
    auf einer Linie erscheinen.
  - C liegt dabei genau dann auf dem Strich AB, wenn die Blickrichtung innerhalb des Winkels ACB liegt (und
    gegenueber). Die Bogenlaenge ist der Winkel bei C.
  - Damit beruehrt jeder Punkt jeden Strich der anderen in irgendeiner Ansicht: 20 x 171 = 3420 Punkt-Strich-
    Beruehrungen, jede als Bogen von Blickrichtungen. In einer einzelnen zufaelligen Ansicht ist es fast sicher keine
    exakte.
- **Kreuzungen in einer Ansicht** (alle 190 Striche gezeichnet):
  - Ihre Zahl ist gleich der Zahl der Vierergruppen, die in dieser Ansicht ein konvexes Viereck bilden (dessen
    Diagonalen kreuzen); Vierergruppen mit einem Punkt im Dreieck kreuzen nie.
  - Erwartung: C(20,4) x P(Viereck) = 4845 x P.
  - Je Tetraeder ist P(Viereck) = 1 - Summe_v Omega_v/(2 pi), mit Omega_v dem Raumwinkel an Ecke v. Fuer das regulaere
    Tetraeder ist das 0,649; fuer Gleichverteilung im Quadrat bzw. in der Scheibe gilt 25/36 bzw. etwa 0,705 [L].
- **L-Gabriel**, dichte Zufallspunkte ohne Rand: im Mittel 8 Nachbarn je Punkt [M: Integral von 4 pi r^2 lambda
  exp(-lambda pi r^3/6) dr = 8]. Am Rand werden es mehr, weil ein Teil der leeren Kugel ausserhalb liegt.
- **L-Beruehrung:** ein Wald aus Inseln mit etwa 0,69 N Strichen und etwa 0,31 N Inseln (Anteil gegenseitig naechster
  Nachbarn etwa 0,62 [L]). Ueber das Ganze laeuft dann keine Welle.
- **L-Delaunay**, dicht ohne Rand: etwa 15,5 Nachbarn je Punkt [L, Meijering]. Bei 20 Punkten sind es wegen des Rands
  weniger.
- **Welle auf L-alle:**
  - Der Laplace des vollstaendigen Graphen hat die Eigenwerte 0 und 20 (19-fach). Ein Stoss erreicht alle Punkte
    zugleich und gleich stark; es gibt keine Front.
  - Eine Welle braucht Nachbarschaft.
- **Isotacheia:**
  - Mit "jeder Sprung eine Kante je Takt" haben alle Felder denselben Kegel (Hoechsttempo), aber nicht unbedingt
    dasselbe langwellige Tempo (DP-Weyl 1/sqrt(3)).
  - "Relativ zu Kantenlaengen": Jede Kante wird mit der Zeit Laenge/c durchlaufen bzw. jede Feldkopplung aus derselben
    Netzgeometrie gebildet. Dann ist das gemittelte Tempo fuer alle Felder gleich, wenn jede Kopplung dieselbe Metrik
    konsistent abbildet (Patch-Test). Bei FEM ist c dann exakt.
  - Offen ist, ob Unordnung die Tempi verschiedener Felder in zweiter Ordnung verschieden verschiebt. Das waere ein
    bleibendes, messbares Ruhesystem [H].
  - Signalfront entlang kuerzester Wege: Tempo c geteilt durch den Umwegfaktor des Netzes (> 1).

## Auftrag (Code-Agent)

**Teil A, Zaehlen:**
- 20 Punkte gleichverteilt im Einheitswuerfel, 2000 Saaten.
- Je Lesart: Zahl der Striche, Grade, Inseln.
- Je Saat 2000 zufaellige Blickrichtungen:
  - Kreuzungen fuer L-alle und L-Gabriel
  - Punkt-nahe-Strich-Beruehrungen mit Toleranz eps = 0,01 und 0,02 (Wuerfelkante 1)
  - Probe der 3420-Regel an einigen Tripeln: Bogenlaenge gleich dem Winkel

**Teil B, Bewegung:**
- Eigenschwingungen je Lesart:
  - skalar: Graph-Laplace ungewichtet und laengengewichtet, bei Delaunay auch FEM
  - elastisch: Federn laengs der Striche, 3D-Verschiebungen
  - Messgroessen: Nullmoden gegen Maxwell-Zaehlung 3N - 6 - E, Beteiligungsverhaeltnis, Aehnlichkeit tiefer Moden mit
    ebenen Wellen
- Stoss an einem Punkt (Wellengleichung u'' = -L u), Front in Netzabstand und in echtem Abstand gegen die Zeit:
  - N = 20 und N = 2000; wenn in 10 min moeglich auch 20 000, periodisch
  - vollstaendiger Graph als Kontrolle
- Bilder fuer Finn: Netz mit Welle zu drei Zeiten, je Lesart.

**Teil C, Isotacheia relativ zu Kantenlaengen:**
- Netz: periodisches Zufalls-Delaunay-Netz, N = 2000 bis 20 000.
- Langwelliges Tempo fuer:
  - (i) Skalar FEM
  - (ii) Skalar ungewichtet (ein Sprung je Takt)
  - (iii) eine einfache Laengenregel (im Plan festlegen und begruenden)
  - (iv) Signalfront entlang kuerzester Wege mit Zeit = Laenge/c
  - (v) Weyl-Spinor nach SPIN-ZUFALLSNETZ-1 (Code von dort nur kopieren)
- Grenzfall k -> 0 mit feinem Energieraster bzw. aus Wellenpaketen; Richtungsabhaengigkeit; Abhaengigkeit von N und
  von der Mittelungsgroesse.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SN0 | Kontrollen: L-alle 190 Striche; vollstaendiger Graph ohne Front; Maxwell-Zaehlung trifft je Netz (Abweichung hoechstens 1 durch Sonderlagen); FEM-Skalar langwellig c = 1 innerhalb 2 %; die 3420-Regel trifft an jeder Stichprobe | 90 % |
| SN1 | [M] L-Gabriel bei 20 Punkten im Wuerfel: im Mittel 75 bis 110 Striche | 60 % |
| SN2 | [M] L-Beruehrung: im Mittel 12 bis 16 Striche und 4 bis 8 Inseln je Saat | 75 % |
| SN3 | [M] Kreuzungen je zufaelliger Ansicht fuer L-alle: Mittel zwischen 2900 und 3500 | 80 % |
| SN4 | [H] Auf L-Gabriel und L-Delaunay mit N >= 2000 laeuft ein Stoss als Front mit festem Tempo (Frontradius linear in t ueber mindestens 5 Netzschritte, Streuung ueber Richtungen <= 15 %) | 60 % |
| SN5 | [H] Isotacheia im Mittel: Das langwellige Tempo des Weyl-Spinors (v) weicht fuer k -> 0 um weniger als 1 % vom FEM-Skalar (i) ab | 40 % |
| SN6 | [H] Ungewichtet (ii) weicht langwellig um mehr als 5 % von (i) ab oder ist richtungsabhaengig | 70 % |

**Bedeutung (vorab):**
- **SN5 trifft ein:** "Relativ zu Kantenlaengen gemittelt" gibt zwei verschiedenen Feldern dasselbe Tempo. Das
  Ruhesystem bliebe langwellig unsichtbar (AETHER-UHR-1); offen bleiben Wechselwirkung und kurze Wellen.
- **SN5 verfehlt:** Die Felder sehen verschiedene gemittelte Tempi; der Baustein braucht eine Symmetrie oder
  Abstimmung (LICHT-GLEICH-L).
- **SN6 trifft ein:** Der Laengenbezug ist Pflicht. "Ein Sprung je Takt" ohne Laengenbezug verraet das Netz.
- **Teil A und B** sind ueberwiegend Veranschaulichung; neu sind nur die Zahlen fuer 20 Punkte mit Rand und die
  Wellenbilder.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, auf den Spuren, die die Leitung beim Start eintraegt; je Lauf
  <= 10 min, 1 Thread.
- Plan, Rauchlauf, Einfrieren wie ueblich. Zeitbox 180 min.

## Nachtrag vor dem Start (Leitung, 2026-10-04 15:52:41 CEST; vor jeder Rechnung)

- **Finn (Nachricht zwischen 15:49 und 15:52, woertlich):** "kannst du einen test mit 50000 punkten machen in einem
  subagent"
- **Umsetzung:**
  - Teil A bleibt bei 20 Punkten (Finns urspruengliche Frage, mit Rand); dazu ein Lauf mit N = 50 000 periodisch als
    Kontrolle gegen die bekannten Werte fuer dichte Zufallspunkte.
  - Teile B und C laufen als Hauptlaeufe mit N = 50 000 (periodischer Wuerfel, Dichte 1). Die kleinste Wellenzahl ist
    dann 2 pi / 36,8, etwa 0,17.
  - Wenn ein Lauf mit 1 Thread und 4 GB nicht in 10 min passt, nach Plan in Teilstuecke schneiden: z. B.
    Netzaufbau einmal, speichern, dann Wellen und Spektren in getrennten Laeufen. Bei Speichermangel KPM bzw.
    Zeitentwicklung statt Eigenzerlegung, und so im Plan begruenden.
  - Bilder: Welle auf einem Ausschnitt (Scheibe durch den Wuerfel) zu drei Zeiten.
- **Zusatzvorhersage (Kontrolle, vorab ableitbar):**

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SN7 | [M, L] Bei N = 50 000 periodisch: mittlerer Gabriel-Grad 8,0 +- 0,1, mittlerer Delaunay-Grad 15,54 +- 0,1, Anteil gegenseitig naechster Nachbarn 0,62 +- 0,01 | 85 % |

- **Spuren beim Start:** cpu6 und cpu7 (frei seit KAUSAL-4D-KERNMASSE-1).
