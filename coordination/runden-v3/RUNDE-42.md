# Runde 42 (v3, explorativ)

- Leitung claude-primary. Eroeffnet 2026-10-04 16:37:21 CEST nach dem Abschluss von Runde 41 (RUNDE-41.md, Abschnitt "Abschluss Runde
  41").
- Regeln wie in den Runden davor (README.md, v3): Karten mit Vorhersagen vor jeder Rechnung, kleine Tests <= 10 min auf
  ein Journaleintrag je Runde.

## Karten (Ordner unter RUNDE-37/)

| Karte | Inhalt | Stand |
|---|---|---|
| STRICH-NETZ-1 | Striche aus 20 Zufallspunkten, Ansichten, Wellen auf 50 000 Punkten; Isotacheia relativ zu Kantenlaengen (Finn 04.10.) | geerntet: Isotacheia nur mit geometrisch passenden Gewichten (Patch-Test); einfache Regeln 3 bis 6 % langsamer und regelabhaengig |
| WOLFRAM-RUHE-1 | Verschwindet das Ruhesystem eines Wolfram-Kausalgraphen im Grossen? r(eta) gegen Kontrollen | laeuft (Code-Agent, cpu6 und cpu7) |
| EINE-WELT-LOCH-1 | Gefuellte Loecher in Finns Netz: eine Graviton-Welt statt zwei? | geerntet: EW1 eingetroffen (eine Welt, zwei masselose TT-Moden), stabil nur mit skalaren Regeln; Tempo keine Vorhersage |
| KOVARIANZ-2D-GEGENPROBE | Dieselbe Verformungs-Vorschrift auf S^2: Polyakov-Antwort oder Wachstum mit N? | geerntet: in 2D keine Spur des 4D-Musters; gemeinsamer Code als Ursache ausgeschlossen; KG1 nicht auswertbar |
| KOVARIANZ-EPS-1 | 4D: Ist die Antwort glatt in eps, liegt die Anomalie am Neuvernetzen? (+-eps; mitgenommene Verbindungen) | laeuft (Code-Agent, cpu und cpu4) |
| GUERTEL-2 (mit Teil B "Guertel im Feld") | Sperre auf dem Staley-Weg; Orientierungsfeld um drehenden Kern, 3D gegen 2D (Finn 04.10.) | laeuft (Code-Agent, cpu10) |
| QBALL-DREIPOL-1 | Q-Baelle mit drei Polen (drei Komponenten mit Richtung): Wechselwirkung, Dreier-Bindung (Finn 04.10.) | laeuft (Code-Agent, p4000a und p4000b geteilt) |
| DREIECK-TAKT-1 (mit QCA-WINDUNG-2) | Lokaler Takt mit Drehsinn je Dreieck: W3 != 0 moeglich? 2D-Randwellen | geerntet: 2D einseitige Randwelle, Richtung durch den Drehsinn; 3D streng lokal W3 = 0 (104 Automaten; K-Theorie-Argument ungeprueft) |
| KOPPLUNG-TETRA-1 | Eckenverknuepfte Tetraeder: starre Einheitsmoden, Deckung mit Tensor-Eis-Ebenen, Eichprobe fuer die Verdrehung (Finn 04.10.) | geerntet: RUM-Ebenen = Tensor-Eis-Ebenen (vorab ableitbar, Wegner 2007); Triplett-Aufspaltung 77 %; Eichprobe: kein Kleber (KT3 nein) |
| STRANG-ANKER-L | Gerichtete Abstrahlung umlaufender Energie an Faeden; Messanker fuer Dimensionen (Finn 04.10.) | laeuft (feldforscher, 90 min) |
| TAKT-RAND-4D-1 | 3D-Rand eines getakteten 4D-Netzes: ungepaartes Weyl-Teilchen? | laeuft (Code-Agent, cpu3 und cpu5) |
| WINDUNG-LESER | Frischer Leser fuer DREIECK-TAKT-1 (K-Theorie-Argument W3 = 0) | laeuft (pruefer-opus, 60 min) |
| GLUONEN-L | Wie koennten Gluonen (nichtabelscher Kleber) in Finns Netz entstehen? Quantenlinks, String-Netze, endliche Untergruppen (Finn 04.10.) | laeuft (feldforscher, 90 min) |
| KERNMASSE-LESER | Frischer Leser fuer KAUSAL-4D-KERNMASSE-1 | geerntet: haelt mit Einschraenkung; Bedeutungssatz zu stark, berichtigt (Journal-Berichtigung) |
| PACHNER-TAKT-1 mit TAKT-KOMMUTATOR-1 | Flip-Flop als Umbau-Takt; kommutieren lokale Takte? | laeuft (Code-Agent, cpu8 und cpu9) |
| DUNKEL-FLIP-L | Negativseite: Zitterbewegung, negative Dimensionen, Spiegelwelt, Branen; messnah | geerntet: kein Messbefund fuer die Negativseite; Flip-Flop = Masse (Foster/Jacobson); Vorschlag SPIEGEL-HAELFTE-1 |
| SPIEGEL-HAELFTE-1 | Verborgene Haelfte mit eigenem Takt je Knoten: wird die sichtbare doppler-frei? (Finns dark tick) | laeuft (Code-Agent, cpu11) |

## Warteschlange

0. KOPPLUNG-TETRA-1 (Karte RUNDE-37/kopplung-tetra-1/KARTE.md; Finns Rechenauftrag 16:45 bis 16:47; erster freier Platz)
1. PACHNER-TAKT-1 mit TAKT-KOMMUTATOR-1 (Karte RUNDE-37/pachner-takt-1/KARTE.md)
2. KERNMASSE-LESER (Karte RUNDE-37/kernmasse-leser/KARTE.md, pruefer-opus, 60 min; Herleitung der Ortsraumform, Urteile, Nebenbefund)
3. GUERTEL-2 (Karte RUNDE-37/guertel-2/KARTE.md; Staley-Weg, Sperre S gegen dE_360)
4. DUNKEL-FLIP-L (Karte RUNDE-37/dunkel-flip-l/KARTE.md, ab 16:56:40; Negativseite: Zitterbewegung, Grassmann, Dark Dimension, Spiegelwelt, Dirac-See, Randall/Sundrum,
   Bondi)
5. EIN-TAKT-1 (gemeinsames Tempo; Pflicht: lokaler gegen globalen Takt)
6. WOLFRAM-RUHE-1 und WOLFRAM-BUEHNE-1
8. Lesepunkte: arXiv 2610.00593 (Regge mit Torsion, zu PACHNER-TAKT-1) und 2606.15855 (lokalisierte Zustaende auf
   Pyrochlor, zu Q-Baellen auf Finns Netz)
9. Weichenstand Fassung 6 (RUNDE-42/WEICHE-STAND-v6.md), sobald die vier laufenden Karten geerntet sind; mit frischem
   Leser und der Negativliste (A2, A4 aus TAKT-UMBENENNUNG-L; die frueheren Gegenleser)

## Gestartet und Protokoll

- 2026-10-04 16:37:21 CEST: Runde 42 eroeffnet. Aktive Agenten 5: STRICH-NETZ-1, EINE-WELT-LOCH-1, KOVARIANZ-2D-GEGENPROBE,
- 2026-10-04 16:39:31 CEST: Journal claude-runde-v3-41-20261004 nach pruefen (0 Befunde) veroeffentlicht (16 Quellen in RUNDE-41/journal-quellen.sha256; result-Feld vor dem Pruefen auf 1719 Zeichen gekuerzt, Grenze 1800).
- 2026-10-04 16:40:17 CEST: Finn (Nachricht zwischen 16:37 und 16:39), woertlich: "koennten wir quasi quark farben bauen aus einer
  richtung auf den tetraeder der die polarisierung oder den kantenzustand bzw drehung des impulses darin beschreibt?"
- Antwort der Leitung:
  - Im Tetraeder steckt eine Drei: drei Paare gegenueberliegender Kanten bzw. drei C2-Achsen. Dazu das dreifach
    entartete Biege-Triplett des Federtetraeders, omega^2 = 2 k/m [P, Codex 01.10.].
  - Drei gleich hohe Schwingungen haben eine verborgene SU(3) wie der isotrope 3D-Oszillator (Jauch/Hill 1940; Elliott
    1958) [L]. Schwingungsquanten bilden ein Triplett, ihre Gegenstuecke ein Antitriplett; das Komplexe kommt aus Phase
    bzw. Umlaufsinn [M].
  - Haken:
    - Die Tetraedersymmetrie erlaubt die kubische Invariante x y z, die SU(3) anharmonisch bricht [M].
    - Echte Farbe ist lokal geeicht (8 Gluonen, Einschluss) und braucht Verbindungsgroessen zwischen Tetraedern
      (nichtabelsche String-Netz-Marken, CHIRAL-L).
    - An Raumrichtungen gebundene Farben drehen mit dem Raum; das Farbsingulett eps_ijk waere ein Spatprodukt, also
      spiegelungsungerade [H].
  - Bild [H]: 4 Ecken = 1 + 3 unter A4, wie Pati-Salam (Lepton als vierte Farbe).
- **Warteschlange neu: FARBE-TETRA-1** (kleiner Test; nach dem Schreibtisch RUNDE-42/FARBE-SCHREIBTISCH.md ueberwiegend vorab ableitbar, nur auf Finns Wunsch):
  - Wie stark bricht die Anharmonizitaet des Federtetraeders die SU(3) des Tripletts (Aufspaltung gegen Amplitude)?
  - Laesst sich eine Kopplung benachbarter Tetraeder ueber Kanten bauen, die SU(3) lokal erhaelt?
  - Ableitbar ist, dass x y z erlaubt ist und in erster anharmonischer Ordnung bricht. Gemessen werden die Groesse und die
    Frage, ob eine Kopplung sie aufhebt.
- 2026-10-04 16:45:10 CEST: Finn: "mach weiter". Karten fuer die naechsten Plaetze geschrieben: KERNMASSE-LESER (ab 16:44:03), GUERTEL-2 (ab 16:44:40). Farb-Schreibtisch RUNDE-42/FARBE-SCHREIBTISCH.md: FARBE-TETRA-1 ueberwiegend vorab ableitbar. Stand der laufenden Karten: STRICH-NETZ-1 eingefroren 16:39:11; EINE-WELT-LOCH-1 mit ERGEBNIS.md (Abschluss laeuft); KOVARIANZ-2D-GEGENPROBE eingefroren 16:41:40; DREIECK-TAKT-1 in der Planung.
- 2026-10-04 16:48:28 CEST: Finn (Nachricht zwischen 16:45 und 16:47), woertlich: "rechne einen kommplungsmechanismus zwischen tetraedern". Karte KOPPLUNG-TETRA-1 geschrieben (ab 16:47:47; KT0 bis KT3): eckenverknuepfte Tetraeder (Diamantgitter der Mitten, Topologie von beta-Cristobalit), starre Einheitsmoden, Vergleich mit den Nullebenen aus TENSOR-EIS-PYRO-1, Eichprobe fuer die Verdrehung als "Kleber". Erster freier Platz.
- 2026-10-04 16:50:40 CEST: Finn: "mach weiter". EINE-WELT-LOCH-1 hat sein ERGEBNIS.md um 16:43:50 abgeschlossen; Abschlussmeldung des Agenten steht noch aus. Erste Lesung: EW1 eingetroffen (eine Welt, genau zwei masselose TT-Moden mit gefuellten Loechern). KOPPLUNG-TETRA-1 gestartet (Code-Agent, cpu5 und cpu3, Zeitbox 150 min) auf dem Platz von EINE-WELT-LOCH-1; der Agent rechnet seit 16:32 nicht mehr. Fuer die Minuten bis zu seiner Abschlussmeldung sind sechs Agenten aktiv (gekennzeichnet).
- 2026-10-04 17:02:16 CEST: Finn, woertlich:
  - Nachricht zwischen 16:57 und 16:59: "mach weiter mehr plaetze"
  - Nachricht zwischen 16:59 und 17:00: "die gluonen sache aufrollen"
- Umsetzung:
  - **Neue Obergrenze der Leitung: 10 Agenten** (beide Sitzungen zusammen), davon hoechstens 7 mit Rechenlaeufen.
  - Spuren cpu8, cpu9, cpu10 in kleintest.sh ergaenzt: neue Datei, bash -n, Sicherung kleintest.sh.bak-20261004-cpu10,
    mv; .69-Last vorher 4,05 von 12 Kernen.
  - Karte GLUONEN-L geschrieben (ab 17:00:27, E1 bis E6).
  - Gestartet: GLUONEN-L, KERNMASSE-LESER, PACHNER-TAKT-1 (cpu8, cpu9), DUNKEL-FLIP-L.
  - Aktive Agenten bei uns 9: STRICH-NETZ-1, KOVARIANZ-2D-GEGENPROBE, DREIECK-TAKT-1, KOPPLUNG-TETRA-1, die vier neuen,
- Hinweis: Das Artifact "Die 1/2-Regel" (LHQ7ta8uUmEub75WTw8roR) ist laut Watch-Meldung nicht mehr auffindbar (geloescht
  oder nicht geteilt). Quelle liegt in coordination/lagebericht/halbe-regel-20261004/. Finn fragen, ob neu
  veroeffentlichen.

### Ernte KOVARIANZ-2D-GEGENPROBE (RUNDE-37/kovarianz-2d-gegenprobe/ERGEBNIS.md; eingetragen 2026-10-04 17:04:57 CEST)

- Code-Agent, 59 von 120 min; 120 von 120 Saaten; rundes Gamma_C bei N = 4000 in 80 von 80 Faellen bitgleich mit
  INDUZIERT-KUGEL-1.
- **Urteile:**
  - KG0 eingetroffen: b_M = -1,7e-12 +- 1,7e-12, vorab als Codekontrolle entschieden.
  - KG1 nicht auswertbar: b(-0,1 / -0,2 / -0,4) = +0,067 +- 0,057 / +0,087 +- 0,102 / -0,081 +- 0,143.
  - KG2 eingetroffen: Aenderung 1000 auf 4000 +0,13 +- 0,15 (0,9 SE).
  - KG3 nach Plan nicht entschieden, nach Wortlaut eingetroffen. Das ist ein Zufallstreffer (r = 0,92 +- 1,64), nicht
    zitierfaehig.
- **Ergebnis:**
  1. In 2D keine Spur des 4D-Musters. Bei eps = -0,1 ist Delta Gamma +0,04 +- 0,07 / -0,01 +- 0,09 / +0,17 +- 0,13 /
     -0,19 +- 0,17 fuer N = 1000 bis 8000; in 4D waren es -16 / -27 / -48. Weder Wachstum mit N noch ein in abs(eps)
     lineares Glied; Schranke 0,6 bis 1,3 % der 4D-Groesse je Punkt.
  2. Derselbe Codepfad: Der n-allgemeine Code gibt mit n = 4 kovarianz.py bitgleich wieder. Transport, Huelle,
     Einbettungssehnen, Neuvernetzung, Paarung und Gamma-Auswertung sind als gemeinsame Ursache ausgeschlossen.
  3. Die Volumenzuordnung je Simplex prueft der Test fuer Gamma nicht (in 2D haengt der Kotangens-Laplace nur von
     Winkeln ab; QI = CI auf 1e-9).
  4. Den Polyakov-Betrag misst der Test nicht; das Signal liegt unter dem Rauschen.
- **Folge:**
  - Die 4D-Zahlen von KOVARIANZ-KUGEL-1 sind kein Fehler im gemeinsamen Code.
  - Die Ursache liegt in etwas 4D-Eigenem: laengenabhaengige Steifigkeit, Neuvernetzung (60 % neue Simplizes gegen 13 %)
    oder Grobheit (Sehnenvolumen 20 % zu klein).
  - Folgekarte KOVARIANZ-EPS-1 gestartet (Karte ab 17:04:02, KE0 bis KE4; cpu und cpu4).
- **Selbstanzeigen des Agenten:**
  - E_FIT und die KG3-Amplitude standen schon vor dem Rauchlauf im Code.
  - Nach dem Rauchlauf nur der Auswerteteil geaendert.
  - Zwei beschreibende Nachtraege nach der Auswertung.
  - 5 min Wartezeit am Lock von cpu4.
- **Abschaetzung:** erledigt; weiter mit KOVARIANZ-EPS-1.
- 2026-10-04 17:06:35 CEST: Finn (Nachricht zwischen 17:06 und 17:06), woertlich: "aber wenn ggf 4d in 3d nur instabil ist, ist das dann
  unser tick vllt?"
- Antwort der Leitung:
  - Faehrt man eine 3D-Scheibe durch ein 4D-Simplex-Netz, aendert sich die Scheibe nicht stetig, sondern in
    Pachner-Zuegen. In der kanonischen Regge-Rechnung ist genau das die Zeitentwicklung (Dittrich/Hoehn;
    TETRAEDER-L [S]). Jeder ueberquerte 4D-Baustein ist ein Tick; nur 2-3-Zuege tragen Gravitonen.
  - Das Neuvernetzen in KOVARIANZ-KUGEL-1 ist dasselbe Umschalten. Im Ruhebild (feste euklidische 4D-Kugel) ist es ein
    Stoereffekt; im Ablaufbild waere es die Uhr selbst [H].
  - KOVARIANZ-EPS-1 zaehlt umgeklappte Simplizes und prueft, ob die Anomalie am Umschalten liegt.
- **Warteschlange neu: TICK-SCHNITT-1** (kleiner Test; nach RUNDE-42/TICK-SCHNITT-SCHREIBTISCH.md vorab ableitbar, nicht gerechnet):
  - Eine 3D-Scheibe wird durch ein zufaelliges 4D-Delaunay-Netz gefahren; Ticks sind Pachner-Zuege.
  - Gezaehlt wird, wie viele es je 4D-Volumen sind (vorab ableitbar: proportional zum ueberstrichenen Volumen) und
    welcher Anteil 2-3 gegen 1-4/4-1 ist (nicht ableitbar).
  - Gefragt ist, ob dieser Anteil von der Neigung der Scheibe abhaengt. Das waere ein Ruhesystem der Ticks.
- 2026-10-04 17:10:53 CEST: Finn (Nachricht zwischen 17:08 und 17:10): Guertel-Effekt im Feld zwischen Innen- und Aussenfeld eines tickenden bzw. drehenden Objekts.
  - Antwort: Finkelstein/Rubinstein-Mechanismus (das Feld als Guertel; 3D Z_2, 2D Z); passt zu GUERTEL-1 (Verdrillen im Raum 65-mal billiger); Q-Baelle nur mit C x S^2.
  - GUERTEL-2 um Teil B "Guertel im Feld" erweitert (Karte ab 17:10:47): SO(3)-Orientierungsfeld um einen drehenden Kern, 2D-Kontrolle; GZ4 bis GZ6. Ein Agent, naechster freier Platz.

### Ernte EINE-WELT-LOCH-1 (RUNDE-37/eine-welt-loch-1/ERGEBNIS.md; eingetragen 2026-10-04 17:12:39 CEST)

- Code-Agent, 16:02:36 bis 17:11:52; eingefroren 16:30:31; Spuren cpu3 und cpu4.
- Der Agent hat selbst einen frischen Leser (pruefer-opus) eingesetzt: 7 schwere, 14 mittlere, 4 leichte Maengel; alle
  eingearbeitet, kein Urteil geaendert.
- **Urteile (Plan und Kartenwortlaut gleich):**
  - EW0 eingetroffen: Modenzahlen an allen 4 095 k gleich, Tempo-Abweichung 4,3e-10.
  - **EW1 eingetroffen:** 2 masselose TT-Moden an 46 von 46 Punkten; 26 Moden mit Luecke >= 3,43.
  - EW2 und EW3 nicht eingetroffen.
- **Einschraenkungen:**
  1. Die eine Welt folgt aus der Festlegung, auch den neuen Tetraedern Eichfreiheit an den Mitten zu geben. Dann
     erzeugen die Mitten jede Eckverschiebung (Rang 30 an 811 k), B1 und A fallen zusammen. Das stand vorab im Plan
     (1.5); EW2 war fast ausgeschlossen.
  2. Gezaehlt ist auf der Zwangsflaeche mit skalaren Regeln je Ecke. Ohne diese Regeln haben 7 (V) bzw. 6 (S) Moden
     omega^2 < 0.
  3. Die Stabilitaet haengt an der Paarung von Bewegungsenergie und Reduktion: 3 von 6 Paarungen wachsen an 8 bis 310
     von 511 k. Die Zahl masseloser Moden bleibt in allen Paarungen 2 (TT-Anteil dort nicht berechnet).
  4. Tempo omega^2/k^2 = 0,119 bis 0,126 (V), 0,211 bis 0,217 (S), zwei Polarisationszweige, nur in [111] gleich. Je
     nach Bewegungsenergie schwankt es um mehr als das Dreissigfache; keine Vorhersage.
- **Selbstanzeigen:** Siehe Punkte 1 bis 3. Dazu:
  - drei Aenderungen vor dem Einfrieren ohne Fuellungsergebnisse
  - drei kleine Fehler ohne Einfluss auf die Urteile (B-flach-Zaehlung, fehlende Code-Regel fuer singulaeres A_phys,
    r2 statt r1)
- **Abschaetzung:** weiter, als Baustein fuer K-AM bzw. Finns Netz mit gefuellten Loechern. Offen sind die
  Stabilitaetsbedingung (skalare Regeln, Paarung), das richtungsabhaengige Tempo und ob die 1/2 auch kurzwellig gilt.
- **Bedeutung:**
  - Finns Netz kann mit gefuellten Loechern eine einzige Schwerkraft-Welt mit genau zwei Spin-2-Wellen tragen.
  - Das folgt weitgehend aus der Eich-Festlegung und braucht Zusatzregeln fuer die Stabilitaet. Das Tempo ist
    richtungsabhaengig und modellabhaengig.
- 2026-10-04 17:21:33 CEST: Finn: "mach weiter". Ableitbarkeitsprobe zu TICK-SCHNITT-1 (RUNDE-42/TICK-SCHNITT-SCHREIBTISCH.md): Anteil der Zugtypen folgt aus N0 und N4 (2 N0/N4 leere Zuege), also vorab ableitbar; nicht gerechnet. Die Aussage an Finn von 17:08 wird berichtigt.

### Ernte STRICH-NETZ-1 (RUNDE-37/strich-netz-1/ERGEBNIS.md; eingetragen 2026-10-04 17:23:26 CEST)

- Code-Agent, eingefroren 16:39:11, rund 82 von 180 min; Kontrollen K1 bis K4 bestanden, 79 Pruefsummen stimmen.
- **Urteile (Plan und Kartenwortlaut gleich):**
  - SN0 nicht eingetroffen: nur der Maxwell-Teil; 25 von 2000 Gabriel-Netzen weichen um 2 bis 3 ab.
  - SN1 nicht eingetroffen: Gabriel 43,2 +- 4,3 Striche; am Wuerfelrand fehlen Partner.
  - SN2 eingetroffen: 14,07 Striche, 5,93 Inseln.
  - SN3 eingetroffen: 3285,9 Kreuzungen je Ansicht.
  - SN4 nicht eingetroffen (Energiefront; zur Vorderkante kein Urteil).
  - SN5 eingetroffen.
  - SN6 eingetroffen (haengt an der Normierung).
  - SN7 nicht eingetroffen, Kartenfehler der Leitung: 0,62 ist der 2D-Wert; in 3D gilt 16/27 = 0,593, gemessen 0,592.
- **Ergebnis:**
  1. **Isotacheia im Mittel nur mit geometrisch passenden Gewichten [E, M]:**
     - P1-FEM, Voronoi-Skalar und Weyl-Spinor mit Voronoi-Gewichten haben bei k -> 0 alle genau das Tempo 1 (1e-14).
       Sie erfuellen den Patch-Test. Der Grenzwert war am Schreibtisch ableitbar (im PLAN vorab).
     - Bei endlichem k trennen sich die Felder: Weyl ~ 1 - 0,117 k^2, FEM ~ 1 - 0,022 k^2 (0,26 % bei k = 0,171;
       1,1 % bei k = 0,341). Die Weyl-Welle ist zusaetzlich gedaempft.
  2. **Einfache Regeln sind langsamer und regelabhaengig [E]:** Auf Delaunay (N = 50 000) ungewichtet 0,939,
     Laengenregel 0,972, kuerzeste Wege 0,937; auf Gabriel 0,899, 0,952, 0,887. Das ist unabhaengig von Saat und N
     (2000 bis 50 000, Streuung <= 0,0011). Ursache ist der Homogenisierungs-Korrektor (Zickzack).
  3. **Streuung der lokalen Tempi (Zusatz der Leitung):**
     - je Knoten 8 % (Weyl, Voronoi), 13 % (Laengenregel), 26 % (ungewichtet), 45 % (FEM auf Kanten)
     - in Teilwuerfeln faellt sie etwa wie l^-2 (Patch-Test-Felder) bzw. l^-1,4 (einfache Regeln)
     - Lokal mitteln alle Felder auf 1; die 0,939 und 0,972 entstehen erst ueber die Nachbarn.
  4. **Finns 20 Punkte:**
     - 190 (alle Paare), 91 (Delaunay), 43 (Gabriel), 14 (naechster Nachbar, 6 Inseln)
     - 3420 Punkt-Strich-Beruehrungen von allen Seiten (an 800 Tripeln auf 6e-5 rad geprueft)
     - 3286 Kreuzungen je Ansicht (68 % der Vierergruppen konvex)
  5. **Welle:**
     - Auf 20 Punkten keine Front; im vollstaendigen Graphen bewegen sich alle gleich; im Naechster-Nachbar-Wald bleibt
       die Welle in ihrer Insel.
     - Auf 50 000 Punkten im Bild ein schwacher Ring mit etwa c (nicht gemessen); der Grossteil der Energie bleibt als
       rauer Kern.
- **Selbstanzeigen des Agenten:**
  - Sicherungskopie im Scratchpad der Leitung angelegt und wieder geloescht (Regelverstoss)
  - Teil-A-Zahlen aus Rauchlaeufen gesehen
  - R90 misst den Kern, nicht die Vorderkante
  - Rauchlauf-Zeitangabe berichtigt
  - Abweichungen von der Karte vor dem Einfrieren festgelegt
- **Abschaetzung:** erledigt. Fuer EIN-TAKT-1 folgt: Ein gemeinsames Tempo verlangt patch-test-konsistente Kopplungen aller
  Felder an dieselbe Geometrie. EIN-TAKT-1 wird damit ueberwiegend vorab ableitbar und geparkt.
- **Bedeutung:**
  - Finns "gemittelt auf Kantenlaengen relativ" funktioniert langwellig exakt, aber nur, wenn jedes Feld seine Kopplungen
    nach derselben geometrischen Regel bildet (Patch-Test). "Ein Sprung je Takt" reicht nicht und verraet das Netz.
  - Bei kurzen Wellen trennen sich die Felder um Prozente. Das ist eine Lorentz-Verletzung auf der Gitterskala, durch
    Messungen nur bei Gitterweiten weit unter heutiger Reichweite erlaubt [L].
- WOLFRAM-RUHE-1 gestartet (Karte ab 17:22:24, WR0 bis WR2; cpu6 und cpu7).

### Ernte DREIECK-TAKT-1 mit QCA-WINDUNG-2 (RUNDE-37/qca-windung-1/teil2-dreieck-takt/ERGEBNIS.md; eingetragen 2026-10-04 17:28:27 CEST)

- Folgeauftrag an den QCA-WINDUNG-1-Agenten, 16:33 bis 17:27; eingefroren 17:00:38; gueltige Auswertung lauf-69/
  auswertung2.json.
- **Urteile:**
  - DT0 eingetroffen.
  - DT1 nicht eingetroffen.
  - DT2 nicht auswertbar.
  - DT3 nach Plan nicht eingetroffen (Zaehlfehler der eingefrorenen Randzaehlung bei pi: Summe +1 statt 0, wegen
    det U = 1 unmoeglich), ~~nach Kartenwortlaut eingetroffen~~ **[berichtigt nach WINDUNG-LESER A2: auch nach
    Kartenwortlaut nicht eingetroffen; die eingefrorene PLAN.md Z. 134 band den Kartenwortlaut an "DT0 bis DT3 wie
    oben", die Lockerung von "beide Luecken" auf "eine Luecke" kam nach dem Ergebnis. Der Inhalt gilt als Diagnose.]**
- **Ergebnis:**
  1. **2D [E]:** Finns Dreiecks-Takt auf dem Wabengitter (Kitagawa u. a. 2010, zyklischer Sprung ueber die drei
     Bindungsrichtungen) gibt eine einseitige Randwelle: oben netto in die eine Richtung, unten in die andere. Die
     Umkehr des Drehsinns dreht beide um.
     - Im rein lokalen Takt sind die Volumenbaender flach mit Chern 0, trotzdem gibt es Randwellen (anomale
       Floquet-Phase). Bei lambda = 3 Chern +-1.
  2. **3D [E, M?]:** Ein streng lokaler Takt (endlichreichweitiger Automat) traegt keine Netto-Haendigkeit: W3 = 0.
     - Herleitung des Agenten ueber K-Theorie (SK_1 von Laurent-Polynomringen ist 0), Saetze aus dem Gedaechtnis, nicht
       gegengelesen.
     - Alle 104 gerechneten Automaten haben abs(W3) <= 5,3e-15: 72 Zufallsprodukte, 6 Pyrochlor-Dreieckstakte (beide
       Drehsinne), 25 allgemeine Suchtreffer, das Literaturmodell als Ganzes.
     - Der Satz der Leitung (Produkte aus Teilverschiebungen und Muenzen haben W3 = 0) stimmt und ist ein Sonderfall.
       Damit war W3 = 0 in QCA-WINDUNG-1 vorab ableitbar.
  3. **Literaturmodell (Higashikawa u. a. 2019) exakt nachgebaut (5,6e-16):** Ihr W = 1 gilt nur fuer den Block der
     unteren Baender; die andere Haelfte hat -1, der ganze Automat 0. Der Partner-Weyl-Punkt sitzt bei k3 = 2 pi,
     ebenfalls bei Quasienergie 0. Der Kegel ist isotrop (Spannweite 3,4e-5).
  4. **Tick-Umkehr:** Bei reellen Spruengen ist die Umkehr der Reihenfolge die Zeitumkehr. In 2D kehrt sie die
     Randrichtung um, in 3D aendert sie W3 nicht.
- **Selbstanzeigen des Agenten:**
  - Suchlauf N = 3 zweimal an der 10-min-Grenze; dritter Versuch mit 3 von 30 Starts (Abweichung von der Regel)
  - Literaturmodell zuerst mit falschem Vorzeichen, vor dem Einfrieren berichtigt
  - vor dem Einfrieren W3 der Produkte und 2D-Chern-Zahlen gesehen
  - Kitagawa-Parameter nach Sicht gewaehlt (Quelle widerspruechlich)
  - Randzaehlung ohne Summenprobe eingefroren; Diagnose nach dem Einfrieren
  - eigene Units gestoppt
- **Abschaetzung:** weiter mit einer Folgekarte. ~~Die Haendigkeit kann bei einem Takt nur am Rand eines hoeherdimensionalen
  Takt-Netzes sitzen, wie die 1D-Randwelle am 2D-Netz.~~ **[gestrichen nach WINDUNG-LESER A1: als unbedingter Satz
  falsch. Dagegen stehen der Higashikawa-Block (Weyl-Teilchen im Volumen bei abgetrenntem Bandraum), die
  Grad-1-Kontrolle und Bessho/Sato (nicht unitaer, w3 = 1). Richtig: Ein unitaerer, streng lokaler,
  translationsinvarianter Takt freier Teilchen traegt im Volumen keine Netto-Haendigkeit (Read 2017); Auswege sind
  ein abgetrennter Bandraum, Verluste oder ein Rand.]** Folgekarte TAKT-RAND-4D-1: Traegt der 3D-Rand eines getakteten
  4D-Netzes ein ungepaartes Weyl-Teilchen? Das waere die Floquet-Fassung der Domain-Wall-Fermionen, passend zu CHIRAL-L
  "Platte in einer 4. Raumrichtung" [H].
  - Gegenlesen des K-Theorie-Arguments vormerken.
- **Bedeutung:**
  - Finns Dreiecks-Takt erzeugt in der Flaeche einseitige Wellen, deren Richtung der Drehsinn waehlt.
  - Im Raum hebt sich die Haendigkeit bei streng lokalem Takt immer weg. Ein einzelnes links- oder rechtsdrehendes
    Teilchen gibt es nur mit abgetrenntem Bandraum, ~~langer Reichweite~~ oder am Rand einer hoeheren Dimension [H].
    **[Nach WINDUNG-LESER: Geltungsbereich "unitaer, freie Teilchen, translationsinvariant, im Volumen" (B2); "lange
    Reichweite" gestrichen, weil bei Hamilton-Treibung keine Reichweite hilft (B4); Verluste (nicht unitaer) als
    weiterer Ausweg (Bessho/Sato).]**
- 2026-10-04 17:30:37 CEST: KERNMASSE-LESER geerntet (Gesamturteil haelt mit Einschraenkung, kein A-Befund, 11 B-Befunde; RUNDE-37/kernmasse-leser/GEGENLESEN.md). B1 umgesetzt: Berichtigung RUNDE-42/BERICHTIGUNG-R41-KERNMASSE.md und Journal claude-runde-v3-41-berichtigung-kernmasse-20261004 (supersedes R41-Eintrag, korrektur true, widerruft zwei woertliche Stellen; pruefen 0 Befunde) veroeffentlicht. N1 (Nebenbefund durch anderes Haus) und N3 (Propagator ohne Gleichung) offen. Negativliste: "Kausalmenge traegt massive Materie stabil" nicht wiederholen.

### Ernte KOPPLUNG-TETRA-1 (RUNDE-37/kopplung-tetra-1/ERGEBNIS.md; eingetragen 2026-10-04 17:33:34 CEST)

- Code-Agent, Text um 17:30; Literatur 3 Abrufe (einer 404).
- **Urteile (Plan und Kartenwortlaut gleich):**
  - KT0 eingetroffen: Einzeltetraeder auf 1,8e-15; Paar mit 9 Nullmoden; Aufspaltung 0,77 in Einheiten von 2 k/m.
  - KT1 eingetroffen (Kontrolle): 12 000 Ebenenpunkte mit 1 Mode, 20 000 Zufallspunkte ohne.
  - KT2 eingetroffen, aber vorab ableitbar: starres Modell und Federnetz an 47 224 Punkten gleich.
  - KT3 nicht eingetroffen: U = 1, Eichverletzung G = 1 bei L = 32; 15 von 18 Mustern kosten nichts.
- **Kartenfehler der Leitung:** KT2 war als nicht ableitbar angegeben. Tatsaechlich hat ein Federnetz genau dann eine
  Nullmode, wenn sich jedes Tetraeder starr bewegt (RUM); damit haengt beides an derselben Determinante. Wegner (2007,
  an der Quelle) gibt fuer beta-Cristobalit genau die sechs Ebenenscharen an. Vierter Ableitbarkeits-Rueckfall des Tages
  (siehe Projekt-Gedaechtnis "Vorab ableitbare Kennzahl").
- **Ergebnis:**
  1. Die weichen Drehungen (RUM) liegen auf den sechs Ebenenscharen k . a_m = 0 mod 2 pi; das sind dieselben wie in
     TENSOR-EIS-PYRO-1. Finns Netz ist mechanisch das beta-Cristobalit-Geruest.
  2. Die Ecken-Kopplung spaltet das Biege-Triplett stark auf (1 + 2 je Paritaet, Spanne 77 % von 2 k/m). Im Gitter ist
     es an den gerechneten Symmetriepunkten nur bei Gamma dreifach.
  3. **Eichprobe: kein Kleber.**
     - Wenn alles andere nachgeben darf, kostet die Gesamtverdrehung um den Sechsring nichts.
     - Energie kosten nur drei ungleiche Muster ohne Holonomie: gleichsinnig um die Radialachse 0,126; um die Ringachse
       mit cos/sin-Verlauf 0,065, zweifach.
     - Ohne Nachgeben wirkt die Kopplung wie ein Massenterm (ganze Drehung auf einem Tetraeder 1/16, gleich verteilt
       etwa ein Viertel davon).
     - U >= 0,75 gegen die Schwelle 0,05.
  4. Folgerung [H]: Die gegenseitige Verdrehung ist kein Eichfeld; fuer Farbe braeuchte es zusaetzliche Regeln
     (String-Netz-Marken). Gerechnet ist nur die zweite Ordnung (abelsch).
- **Selbstanzeigen des Agenten:**
  - einmal lokal awk (Zeilenlaengen pruefen; Regelverstoss)
  - pdfinfo, ls, cat, chmod ausserhalb der Liste
  - Kennzahl und Rechenweg vor dem Einfrieren umgestellt
  - kein frischer Leser
- **Abschaetzung:** erledigt. Der Kleber muss aus anderen Regeln kommen; GLUONEN-L laeuft.
- **Bedeutung:** Finns Netz ist mechanisch ein bekanntes Geruest (beta-Cristobalit) mit weichen Drehmoden auf sechs
  Ebenen. Die gegenseitige Verdrehung der Tetraeder gibt aber keinen Gluonen-Kleber.

- 2026-10-04 17:33:34 CEST: Finn (Nachricht zwischen 17:27 und 17:29), woertlich: "und wenn gluonen zwei-punkt-symmetrien sind die
  sich umeinander drehen und 1-2 einheiten groß sein können und relativistisch bei 3/4... das mal checkn als idee, und
  dann noch mal folgendes checken: was wenn energie in einer dimension um den faden schwingt in eine richtung und das
  abstrahlt und gerichtet wird? wo haben wir feste größen in dimensionsmessungen an denen wir uns lang hangeln können?"
  - Karten STRANG-ANKER-L, TAKT-RAND-4D-1 und WINDUNG-LESER geschrieben (je ab 17:31:03) und gestartet.
  - Gluonen-Paar-Idee am Schreibtisch (Chat-Antwort); Rechnung nach GLUONEN-L.
  - Aktive Agenten 10: GLUONEN-L, PACHNER-TAKT-1, DUNKEL-FLIP-L, KOVARIANZ-EPS-1, GUERTEL-2, QBALL-DREIPOL-1,
    WOLFRAM-RUHE-1, STRANG-ANKER-L, TAKT-RAND-4D-1, WINDUNG-LESER.

### Ernte DUNKEL-FLIP-L (RUNDE-37/dunkel-flip-l/DOSSIER.md; eingetragen 2026-10-04 17:35:50 CEST)

- feldforscher; Selbstanzeige: Foster/Jacobson schon in RUNDE-39 bekannt (grep uebersehen), zwei Abrufe teils doppelt,
  einer leer.
- **Ergebnis:** Fuer keine Lesart der Negativseite gibt es einen Messbefund; die gelesenen direkten Suchen sind
  Nullresultate.
- **Erwartungen:**
  - E1 eingetroffen: Zitterbewegung beim freien Elektron nicht beobachtet, in fuenf Simulatoren nachgestellt, zuletzt
    2026.
  - E2 in 1+1 eingetroffen, in 3+1 verletzt: Foster/Jacobson haben eine 3+1-Fassung mit Spin und ohne Doppler, mit Masse
    als Flip i eps m zwischen zwei Tetraeder-Schrittsaetzen, aber nicht unitaer [S].
  - E3 eingetroffen nur oberhalb d ~ 5,1 (in 3D heben sich Grassmann-Richtungen nicht auf).
  - E4 im Kern eingetroffen: Spiegelneutron-Anomalien seit 02/2026 zu 99,98 % ausgeschlossen.
  - E5 eingetroffen: RS1 gibt der sichtbaren Brane negative Vakuumenergie (Wortlaut "vacuum energy").
  - E6 eingetroffen (Bondi ueber Kaplan/Sundrum gelesen).
  - E7 gestuetzt ohne eigenen Abruf.
- **Erwartungsverstoesse:**
  - Garriga/Tanaka: Materie auf der anderen Brane zieht an, lenkt Licht aber 25 % schwaecher ab. Ohne Stabilisierung ist
    die Schwerkraft auf der negativen Brane falsch.
  - Am woertlichsten passt zu Finns Bild die Geisterkopie des Standardmodells (Kaplan/Sundrum). Sie stoesst ab, gemischte
    Paare laufen davon, und sie verlangt einen Bruch der Schwerkraft unter etwa 30 bis 100 Mikrometer.
  - Unitaere Netze tragen den Spiegelpartner mit; das doppler-freie Schachbrett verliert dafuer Norm. Herleitung des
    Agenten, ungeprueft: FJ ist eine Haelfte unseres Einbahn-Automaten aus QCA-DIAMANT-4.
- **Messnahe Schranken:**

  | Lesart | Schranke | Quelle |
  |---|---|---|
  | Spiegelneutronen, gleiche Masse | Oszillationszeit > 352 s | PSI 2021, 2026 |
  | Spiegelneutronen, Massenabstand | > 20 s | PSI 08/2026 |
  | Orthopositronium, unsichtbarer Zerfall | < 4,2e-7 | ETH 2007 |
  | Spiegel-Dunkle-Materie, Mischung | < 2e-10 | CDEX-10 |
  | Kurzabstand | Yukawa gravitationsstark bis 38,6 Mikrometer ausgeschlossen | Eot-Wash 2020 |
  | Geisterkopie | Fenster 20 bis 98 Mikrometer | Eot-Wash 2007 |
  | Dunkle Blase | L <= 9,3 Mikrometer | BLASE-EW (Projekt) |

  - Einzige Abweichung von null: kosmische Doppelbrechung 0,277 +- 0,057 Grad (4,8 sigma, Planck und ACT); die
    Winkelkalibrierung ist ungeklaert.
- **Rueckfrage an Finn (vom Agenten):** Was heisst "negativ": negative Energie, gespiegelte Haendigkeit, Gegentakt oder
  zeitgespiegelt?
- **Abschaetzung:** erledigt; SPIEGEL-HAELFTE-1 gestartet (Karte ab 17:34:35, SH0 bis SH2; Spur cpu11, neu eingerichtet
  nach demselben Verfahren, .69-Last 0,6).
- **Bedeutung:** Die Negativseite ist in allen Lesarten bisher ohne Messbefund. Finns Flip-Flop zwischen Auf- und
  Ab-Tetraeder hat in der Literatur eine genaue Entsprechung: die Masse im 3+1-Schachbrett von Foster/Jacobson.
- 2026-10-04 17:37:18 CEST: Finn: "mach weiter". Alle 10 Plaetze belegt.
  - arXiv-Scout (Lauf 15:00Z) mit passenden Titeln zu Glueballs: 2610.01988 (EFT, Formfaktor-Radien), 2610.00484 (X(2370)), OpenAlex (dimensionslose Glueball-Verhaeltnisse SU(N), G2).
  - Karte GLUON-PAAR-L geschrieben (ab 17:36:49; E1 bis E5): Finns rotierendes Zwei-Punkt-Gluon gegen Glueball-Spektrum, Groessen und Messkandidaten; naechster freier Platz.
  - Warteschlange danach: Rueckfrage "3/4" offen; N1 aus KERNMASSE-LESER (ASS 2.14 durch ein anderes Haus) offen; WEICHE-STAND-v6 nach KOVARIANZ-EPS-1 und WINDUNG-LESER.
- 2026-10-04 17:39:48 CEST: Finn (Nachricht zwischen 17:37 und 17:39), woertlich: "ueberpruefe verschiedene lesarten dazu. negativ koennte auch links/rechts oder anderweitig sein,". Schreibtisch RUNDE-42/NEGATIV-LESARTEN.md (ab 17:39:07): neun Lesarten mit Projektstand, Messlage und Test; neu N9 (Verlustseite eines PT-symmetrischen Paars als "Ausgleich"); nicht gegengelesen. GLUON-PAAR-L um Lesarten von "3/4" ergaenzt.

### Ernte GLUONEN-L (RUNDE-37/gluonen-l/DOSSIER.md; eingetragen 2026-10-04 17:50:44 CEST)

- feldforscher; Abgabe 17:39:07, in der Zeitbox; 12 von 12 Abrufen, lokale Kopien in quellen/.
- **Ergebnis [S, M]:**
  - Finns Netz hat die Form einer Gittereichtheorie: Tetraeder = Plaetze (Ladung), Ecken = Kanten (Kleber), Sechsringe =
    Plaketten.
  - Die Verdrehung starrer Tetraeder ist reine Eichung (Ringprodukt O_1^-1 O_2 ... O_6^-1 O_1 = 1, in der Literatur
    "Higgs-Term"). Als T-Eichfeld beschreibt sie Disklinationen, keine Gluonen.
  - Gluonen brauchen je Ecke eine eigene SU(3)-Variable und je Tetraeder eine nichtabelsche Eisregel (Farbsingulett).
  - T, T_d, 2T und SO(3) reichen nicht. 2T friert auf dem Hyperkubus bei beta_f = 2,24 ein, am Beginn des
    SU(2)-Skalenbereichs (2,2).
- **Erwartungsverstoesse:**
  - V1: "Gluonen aus String-Netzen" ist behauptet, nicht gebaut. Exakt loesbare 3+1D-String-Netze geben nur Eichtheorien
    endlicher Gruppen. **Das Zitat in RUNDE-35 (graviton-netz-l DOSSIER Z. 100 bis 101) ist zu stark.** Es steht nicht im
    Journal (grep INDEX: kein Levin); die Quelle bleibt unveraendert, der Vermerk steht hier.
  - V4: Nichtabelsche Laborlaeufe gibt es nur auf Quantenrechnern (Ionen-Qudits 2026); kalte Atome mit Rishons sind
    weiter nur ein Vorschlag.
  - V6: Chandrasekharan 2026 schlaegt ein Kontinuum ueber einen kritischen Punkt endlicher Gittermodelle vor, ohne 5.
    Dimension. Begruendet, nicht gezeigt.
  - V7: Nichtabelsche Anyonen gibt es nur in 2+1D; in Finns 3D-Netz nur Ladung gegen Fluss-Schleife.
- **Neu [M, Agent, nicht gegengelesen]:** Farbiges Pfeil-Eis (SU(3), minimal) heisst "null oder drei rein" statt "zwei
  rein, zwei raus"; zwei Drittel der Tetraeder sind Baryon-Knoten.
  - 2D-Gegenstueck im Material: Biexzitonen auf Wabengitter-Kanten (Kagome), "genuine non-Abelian lattice gauge field"
    (arXiv:2504.16694 [S Abstract]). Wabengitter : Kagome = Diamant : Pyrochlor, also Finns Tetraederecken.
  - Die 5. Dimension der D-Theorie liefert zugleich chirale Quarks als Domain-Wall-Fermionen [S]; Anschluss an CHIRAL-L
    und TAKT-RAND-4D-1.
- **Hinweis R1 des Agenten (KOPPLUNG KT3 vorab ableitbar, falls ueber O_i^-1 O_j definiert):** trifft nicht zu.
  KOPPLUNG-TETRA-1 hat die Produkt-Holonomie ausdruecklich verworfen (ERGEBNIS Z. 194 bis 196) und die Winkelsumme
  genommen. Die Schlussfolgerung (kein Kleber) stuetzt GLUONEN-L unabhaengig.
- **Kartenvorschlaege:**
  - K1 ZWEI-T-AUSFRIER-1 (2T gegen SU(2) auf Diamant x Zeit): **parken**. Finns Netz hat T, nicht 2T, und Finns
    Rueckfrage R2 ist offen.
  - K2 FARB-EIS-1: **Warteschlange**. Die Zaehlung (ein Drittel leer) ist ableitbar, der Zusammenhang unter lokalen
    Zuegen nicht. Vorher R3 (Rishonzahl im SU(3)-Quantenlink, nur Abstract gelesen).
- **Rueckfragen:** R2 an Finn: Sind mit "Gluonen" nur die acht SU(3)-Gluonen gemeint oder jeder nichtabelsche Kleber?
  R3 (Literatur) offen.
- **Negativliste (nicht wiederholen):** "String-Netze geben Gluonen und Quarks" als gezeigt.
- **Abschaetzung:** erledigt.
- **Bedeutung:** Finns Netz ist die richtige Buehne fuer einen Kleber. Der Kleber selbst braucht aber eigene Variablen an
  den Ecken; die Mechanik der Tetraeder liefert ihn nicht.
- 2026-10-04 17:50:44 CEST: Finn, zwei Nachrichten (zwischen 17:40 und 17:46), woertlich in RUNDE-42/SCHALTER-UND-ATMEN.md (Strich-Schalter, gerichtetes Dreieck; Punkte mit Durchmesser, atmende Punkte im Gleichtakt). Schreibtisch dort: Kreuzungsvorzeichen = Haendigkeit des Tetraeders aus den vier Endpunkten, aus jeder Richtung gleich [M]; Umlauf um ein Dreieck nur mit eigenem Kantenwert [M]; Sichtlaenge 2d/(3 phi) [M]; Gleichtakt zieht ueber ein Medium an (Bjerknes), ist aber Spin 0; Pumpen braucht Phasenversatz (Shapere/Wilczek) [L]. Kartenvorschlag ATEM-NETZ-1 in der Warteschlange (Rechenplatz noetig).

### Ernte WOLFRAM-RUHE-1 (RUNDE-37/wolfram-ruhe-1/ERGEBNIS.md; eingetragen 2026-10-04 17:51:45 CEST)

- Code-Agent; Plan eingefroren 17:46:04, Hauptlaeufe 17:46:29 bis 17:46:46 auf der .69 (cpu6, cpu7); Abgabe ~17:50.
- **Ergebnis:**
  - Wolframs "lorentzartige" 2D-Regel R2 ist vom Standardanfang keine 1+1-Raumzeit. Sie ist eine Kette: genau 1 Ereignis
    je Generation in 50 000 von 50 000 Generationen, jedes Ereignis haengt vom vorigen ab [E]. Das war vorab ableitbar:
    Je Ereignis wird genau eine Marke verbraucht und erzeugt, ab Ereignis 3 bleibt ein aktiver Ort [M, im Plan vor dem
    Lauf].
  - R2 ist nicht kausalinvariant: 5 von 8 Zufallsreihenfolgen geben bei Tiefe 25, 50 und 100 einen anderen
    Kausalgraphen [E]. Damit greifen weder das Lorentz-Argument der TI (S. 366, nur bei Kausalinvarianz [S]) noch
    Gorards Vergroeberung [S].
  - WR0 formal verfehlt; in der Sache arbeiten die Kontrollen: Poisson ohne Trend, Gitter exakt cosh(eta). Verfehlt
    durch den vorab benannten Endlichkeitseffekt und ein falsch angelegtes Plan-Kriterium (S2, nach dem Befund nicht
    geaendert).
  - WR1 verfehlt (Kegel-Exponent 2,25 statt 1,8 bis 2,2; Generationskegel 0,98, also Kette).
  - WR2 nicht geprueft (eta fuer R2 nicht definiert; alle 6000 Intervalle Ketten).
- **Selbstanzeigen des Agenten:**
  - S1: rauch.py versehentlich ein zweites Mal gestartet (cpu6, Ausgabe verworfen, kein Ergebnis gesehen).
  - S2: Plan-Kriterium G(ii) falsch angelegt.
  - S3, S4: Zaehlweise und Partnerwahl, vorab im Plan.
  - S5: lokal ls, cat, wc, head, tail, diff, rm, sleep; keine Interpreter.
  - Kein frischer Leser.
- **Selbstanzeige der Leitung:** Die Ableitbarkeitsprobe der Karte ("fuer den Wolfram-Graphen ist r(eta) nicht
  ableitbar") war fuer R2 vom Standardanfang falsch. Der Agent hat es im Plan vor dem Lauf gezeigt. Damit sind es am
  04.10. sieben Rueckfaelle (Gedaechtnis-Eintrag ergaenzt).
- **Abschaetzung:** erledigt fuer R2. Weitere Wolfram-Regeln nur, wenn eine kausalinvariante Regel mit vielen
  gleichzeitigen Orten vorliegt [H]: parken.
- **Bedeutung:** Wolframs Vorzeigebeispiel hat eine absolute Uhr, die auch im Grossen bleibt (Seite A der Weiche). Es
  ist kein Beleg fuer Lorentz-Invarianz aus Kausalgraphen.

### Ernte WINDUNG-LESER (RUNDE-37/windung-leser/GEGENLESEN.md; eingetragen 2026-10-04 18:04:36 CEST)

- pruefer-opus, frisch, kein Fork; 17:33:16 bis 17:55:45; 2 von 2 Abrufen (Read 2017, lokale Kopie in quellen/).
- **Gesamturteil: haelt mit Einschraenkung; 2 A-Befunde, 11 B-Befunde.**
  - Frage 1 (K-Theorie) haelt. Der Satz steht in der Literatur: Read 2017, PRB 95, 115309, Abschn. IV, Gl. (39).
    Unitaritaet ist tragend; Bessho/Sato (nicht unitaer, endlichreichweitig) hat w3 = 1.
  - Frage 2 (Numerik) haelt mit Einschraenkung. "An 104 Automaten bestaetigt" ueberzeichnet: 79 sind schon nach den
    einfacheren Saetzen null, unabhaengig sind nur die 25 Suchtreffer.
  - Frage 3 (Higashikawa) haelt.
  - Frage 4 (2D) haelt mit Einschraenkung. Die Randwelle traegt (Kitagawa S. 8), aber der Zaehler ist nicht validiert.
    Die Richtungsumkehr ist durch die Zeitumkehr erzwungen, kein eigener Befund.
- **A1:** "Haendigkeit nur am Rand" faellt als unbedingter Satz. **A2:** DT3 "nach Kartenwortlaut eingetroffen" faellt;
  die Bedingung wurde nach dem Ergebnis gelockert. Beide sind oben in der Ernte DREIECK-TAKT-1 berichtigt (gestrichen,
  mit Vermerk).
- **Umgesetzt:**
  - B1: T2 jetzt als gegengelesen gefuehrt, mit Read 2017.
  - B2: Geltungsbereich in RUNDE-42/NEGATIV-LESARTEN.md und RUNDE-42/SCHALTER-UND-ATMEN.md.
  - B4: "lange Reichweite" gestrichen.
- **B9 (Kalibrierung):** WI1 (20 %) und DT1 (35 %) waren nach dem Satz vorab unmoeglich. Das ist ein weiterer Fall vorab
  ableitbarer Vorhersagen (Gedaechtnis-Eintrag ergaenzt).
- **Negativliste (nicht wiederholen):**
  - "Haendigkeit bei einem Takt nur am Rand eines hoeherdimensionalen Netzes" (unbedingt)
  - "DT3 nach Kartenwortlaut eingetroffen"
  - "an 104 Automaten bestaetigt" (ohne Einschraenkung)
- **Abschaetzung:** erledigt. WEICHE-STAND-v6 wartet nur noch auf KOVARIANZ-EPS-1.

### Ernte QBALL-DREIPOL-1 (RUNDE-37/qball-dreipol-1/ERGEBNIS.md; eingetragen 2026-10-04 18:04:36 CEST)

- Code-Agent; eingefroren 17:42:24; Laeufe 15:42 bis 15:55 UTC (p4000a/b, CPU); 2D-Gitter L = 64, N = 256, dazu radial.
- **Urteile:**

  | Nr | Plan | Kartenwortlaut |
  |---|---|---|
  | QD0 | eingetroffen, vorab ableitbar | eingetroffen |
  | QD1 | eingetroffen (knapp, 0,331 gegen 1/3) | nicht eingetroffen (relaxiert 0,370 bis 0,553) |
  | QD2 | eingetroffen, vorab ableitbar | eingetroffen |
  | QD3 | eingetroffen, durch Energieerhaltung weitgehend erzwungen | eingetroffen |

- **Ergebnis [E]:**
  - Verschiedene Pole wechselwirken auf Abstand wie e^{-2 kappa d} statt e^{-kappa d} (Raten auf 2 % an 2 kappa).
    Bei d = 2R ist "gleicher Pol in Phase" eingespannt abstossend (Wandueberlapp).
  - Bei g4 = +0,1 verschmilzt der Dreier zum Mischball (Bindung 9,6 %).
  - **Neu, ohne Urteil:** Bei g4 = -0,1 entsteht ein festes Dreieck aus drei einfarbigen Klumpen (Paarabstand 1,245 R),
    0,146 unter dem Mischball. Nur im symmetrischen Unterraum gerechnet.
  - In echter Zeit pulsiert der Dreier: Die Pole laufen alle 40 bis 70 Zeiteinheiten durch die Mitte und kehren um
    ("atmender Klumpen"). Mindestens 96,5 % jeder Polladung bleiben bis t = 200 im Haufen.
- **Selbstanzeigen des Agenten:**
  - Code, Rauchlauf und QD0 vor fertigem Plantext
  - Ueberlauf vor dem Einfrieren behoben
  - Leitungs-Test angesehen, danach Energietor 1e-4 auf 1e-3 (kein Einfluss)
  - 5 statt 7 Abstaende
  - QD3-Erzwungenheit erst nach dem Lauf gesehen
  - nachtrag.py nach Sicht
  - zeitweise bis zu fuenf ssh-Verbindungen
- **Selbstanzeige der Leitung:** Die Ableitbarkeitsprobe der Karte fuehrte QD2 als nicht ableitbar. Bei konkavem E(Q)
  ist Verschmelzen aber immer guenstig. QD3 war durch die Energiebilanz erzwungen. Das ist der achte Rueckfall am 04.10.
  (Gedaechtnis ergaenzt).
- **Abschaetzung:** weiter (Fast Lane). QBALL-DREIPOL-2 gestartet: Ist das Dreieck bei g4 = -0,1 ein Minimum? Gibt es es
  in 3D? Bleibt ein schiefer Dreier gebunden?
- **Bedeutung [H]:** Ein "Baryon-Q-Ball" existiert im Modell, aber nichts zeichnet die Drei aus: Q-Baelle kleben generell
  zusammen, einzelne Pole sind stabil, und die Ladungen sind U(1)^3, nicht SU(3). Fuer Einschluss fehlt weiter der
  Kleber.

### Ernte STRANG-ANKER-L (RUNDE-37/strang-anker-l/DOSSIER.md; eingetragen 2026-10-04 18:10:33 CEST)

- feldforscher; 14 von 14 Abrufen (einer leer).
- **Ergebnis [S]:** Laeuft Energie auf einem Faden nur in eine Richtung, strahlt er nicht. Bei genug Strom bleibt eine
  Schleife in jeder Form stehen ("Vorton", Blanco-Pillado/Olum/Vilenkin 2001, Volltext). Gebuendelte Strahlung entsteht
  erst, wenn Wellen aus beiden Richtungen zusammentreffen: an Spitzen ein enger Kegel, an Knicken ein Faecher. Dieselbe
  Regel gilt in fuenf Systemen, auch bei Wirbelfaeden in Suprafluiden [ES].
- **Feste Anker:**
  - Cassini gamma - 1 = (2,1 +- 2,3)e-5
  - Photonmasse < 1e-14 eV (Labor)
  - GW170817: D = 4,02 +0,07/-0,10; Tempo Schwerewelle gegen Licht -3e-15 bis +7e-16
  - Newton von 52 Mikrometer bis 3 mm
  - LHAASO: E_QG,1 > 1,0e20 GeV, E_QG,2 > 6,9e11 GeV
  - Modellabhaengig: G mu (LVK 1,5e-15 bis 5,1e-7; CMB < 1,5e-7), NANOGrav nur metastabile Strings
- **Folgen fuers Netz (bedingt, eigene Rechnung des Agenten):**
  - Spitzen sind nur in hoechstens drei Raumdimensionen generisch (O'Callaghan u. a. 2010); gebuendelte Stringblitze
    waeren selbst ein Dimensionsanker.
  - Netzweite unter 6e-28 bis 1,4e-27 m. Ist das lineare Weyl-Glied aus STRICH-NETZ-1 (-0,0011 k, ohne Fehler) echt,
    dann unter 55 bis 450 Planck-Laengen.
  - Ein String auf einem Planck-Netz haette G mu ~ 2, muesste also um mindestens 1e7 leichter sein oder brechen.
- **Selbstanzeigen:**
  - einmal lokal awk (Formatieren)
  - Projekt-grep lief anfangs ueber KS-1-Vertragstexte, ohne Anzeige; versiegelte Pfade waren ausgeschlossen
  - E2-Primaerquelle nicht gelesen
  - eigene Fehllesung (RUNDE-34-Dossier: 9,6e20 GeV ist eine Photon-Schranke) berichtigt
- **Kartenvorschlaege:**
  - K1 WEYL-LINEAR-1 (Altdaten, messnah): **gestartet** (siehe unten).
  - K2 GEGENVERKEHR-1: groesstenteils ableitbar, **geparkt**.
- **Abschaetzung:** erledigt.
- **Bedeutung:** Ein Faden mit Strom in nur eine Richtung ist ruhig. Finns "gerichtetes Abstrahlen" braucht Gegenverkehr
  auf dem Faden. Die festen Messanker fuer das Netz sind Licht- und Schwerewellen-Tempo, Lichtablenkung und das
  Abstandsgesetz.

### Ernte PACHNER-TAKT-1 / TAKT-KOMMUTATOR-1 (RUNDE-37/pachner-takt-1/ERGEBNIS.md; eingetragen 2026-10-04 18:10:33 CEST)

- Code-Agent; eingefroren 17:34:34; Abgabe 18:07:57; frischer Leser im Agentenlauf (vier falsche Angaben berichtigt).
- **Urteile:**

  | Nr | Plan | Kartenwortlaut | Kennzahl |
  |---|---|---|---|
  | PT0 | nicht eingetroffen | nicht eingetroffen | Kommutator-Steigung 0,998 statt erwartet 2 |
  | PT1 | nicht eingetroffen | nicht eingetroffen | Rang nach drei Takten 76 bzw. 254 unter der festen Schwelle |
  | PT2 | eingetroffen | eingetroffen | r/V = 2,38 / 2,35 |
  | PT3 | nicht eingetroffen | nicht eingetroffen | p = 2,25 |

- **Ergebnis [E, M]:**
  - Reines Umklappen der Diagonale auf festen Ecken ist kein Takt; das war am Schreibtisch ableitbar und wurde
    nachgerechnet (Rueckwechsel braeuchte einen Winkel ueber pi).
  - Mit Zeltstangen (Ecken ruecken in der Zeit mit) ist Finns Flip-Flop baubar (flach auf 1,8e-15, alle 4-Volumen
    positiv).
  - Durch ein und zwei Flip-Flop-Takte laufen genau E - G = 3 Groessen je Zelle (wie beim reinen Zeltstangen-Takt).
    Nach drei Takten faellt der Rang unter die feste Schwelle; ein beschreibender Nachtrag zeigt Daempfung, nicht
    Vernichtung [H].
  - Das Umklappen koppelt die zwei Welten nicht.
  - Reihenfolge zweier Nachbarecken: ohne Kruemmung vertauschbar (1e-15). Mit Kruemmung waechst der Unterschied linear
    mit eps und faellt mit der Gitterweite wie (a/L)^2,25. Ein globaler Takt hebt ihn nicht auf.
- **Selbstanzeigen des Agenten:**
  - Lesart C der Karte ohne Zeltstangen hat gar keinen Takt; PT2 gilt fuer C mit Zeltstangen.
  - 4 zusaetzliche Nullrichtungen je Schicht, nicht vorhergesagt
  - Aenderungen vor dem Einfrieren ohne Ergebnis-Sicht
  - lokale Werkzeuge ausserhalb der Liste (chmod, paste, sleep)
- **Abschaetzung:** parken. Der Flip-Flop ist als Takt nur mit Zeltstangen moeglich und bringt gegenueber dem
  Zeltstangen-Takt nichts Neues. Offen bleibt nur die Daempfung nach drei Takten; ein Folgelauf erst mit Grund.
- **Bedeutung:** Finns Hin-und-Her-Klappen braucht, dass die Ecken in der Zeit weiterruecken. Dann laufen die
  Schwerkraftwellen-Groessen durch, aber die zwei Welten bleiben getrennt, und die Reihenfolge des Tickens macht einen
  Unterschied von der Groesse der Kruemmung.

### Ernte TAKT-RAND-4D-1 (RUNDE-37/takt-rand-4d-1/ERGEBNIS.md; eingetragen 2026-10-04 18:18:56 CEST)

- Code-Agent; eingefroren 18:00:04; Abgabe 18:15:31; 3 von 3 Abrufen.
- **Urteile:**

  | Nr | Plan | Kartenwortlaut |
  |---|---|---|
  | TR0 | eingetroffen | eingetroffen |
  | TR1 | nicht eingetroffen (Hauptmodell P4a: 0 Funde, Methodenfehler) | eingetroffen (P4b, P4c, P4cr) |
  | TR2 | nicht auswertbar | eingetroffen nur ueber P4b, **nicht robust** (S3): beim Einkegel-Modell P4a 29 % Abweichung, also verfehlt |

- **Ergebnis [E]:** Der 3D-Rand eines streng lokalen 4D-Schrittplans traegt ungepaarte Weyl-Teilchen; der Gegenrand
  traegt die umgekehrte Haendigkeit (Floquet-Fassung der Domain-Wall-Fermionen).
  - P4b: drei gleichsinnige Kegel je Rand (+3 / -3).
  - P4c und P4cr: ein Kegel bei k = 0 (-1 / +1).
  - Kontrolle P4t (C2 = 0) ohne Randknoten.
  - Zahl und Ort passen zu Qi/Hughes/Zhang 2008.
  - P4a: Bei 16 Lagen koppeln die Raender schwach (4e-6, ueber der eingefrorenen Toleranz 1e-7), daher 0 Funde. Bei 24
    Lagen ein Kegel je Rand; die Kopplung faellt wie exp(-L/1,37) (Restmasse, Kaplan).
- **Wo die Haendigkeit sitzt:** Sie folgt der Chern-Zahl des Volumens, nicht dem Drehsinn der Schrittfolge; die Umkehr
  des Takts laesst sie gleich. Die Kartenhypothese "Haendigkeit im Takt der vierten Richtung" ist nicht gestuetzt; sie
  sitzt am Rand der vierten Richtung.
- **Isotropie haengt am Plan:** Rund ist nur der Dreifach-Kegel P4b (2,9e-4). Die Einzelkegel sind verzerrt (P4a 29 %,
  P4c 139 %). Ein einzelnes rundes Rand-Weyl-Teilchen ist also nicht erreicht.
- **Vorab ableitbar:** TR1 folgt fuer palindromische Plaene aus Qi/Hughes/Zhang plus Stetigkeit. Neu ist nur die streng
  lokale Floquet-Ausfuehrung mit Zahlen, Orten, Chiralitaeten und Isotropie.
- **Selbstanzeigen des Agenten:**
  - einmal python --version auf der .69 ausserhalb des Starters
  - ungepruefte Annahme zur Randkopplung
  - TR2-Regel nicht robust
  - P4a-Ergebnis vor Ende aller Hauptlaeufe gesehen (Code eingefroren)
  - Diagnoseskripte nach dem Einfrieren
  - lokale Werkzeuge ausserhalb der Liste
  - Stuetze auf das K-Theorie-Argument; inzwischen von WINDUNG-LESER gegengelesen (haelt)
- **Abschaetzung:** parken. Die Haendigkeit am 4D-Rand ist bekannte Physik in streng lokaler Ausfuehrung. Offen bleibt
  ein einzelner runder Randkegel (anderer Plan); weiter nur mit Grund.
- **Bedeutung:** Ein getaktetes 4D-Netz kann an seiner 3D-Oberflaeche ein einzelnes links- oder rechtsdrehendes Teilchen
  tragen; den Drehsinn setzt das ganze Netz, nicht die Reihenfolge der Schritte. Rund ist es bisher nur als Dreiergruppe.

### Ernte GLUON-PAAR-L (RUNDE-37/gluon-paar-l/DOSSIER.md; eingetragen 2026-10-04 18:21:29 CEST)

- feldforscher; 10 von 10 Abrufen (einer leer).
- **Ergebnis [S]:**
  - Finns Bild trifft Glueballs, nicht das einzelne Gluon. Zwei Gluonen, die sich an einem Flussrohr umeinander drehen,
    sind ein eingefuehrtes Modell. Meyer/Teper 2004 deuten die fuehrende, Pomeron-aehnliche Gitter-Trajektorie (2++,
    4++) als rotierendes Paar; das leichteste 0++ ist bei ihnen ein geschlossener Ring.
  - Ein Paar fester Groesse haette Ruhemasse und gaebe leichte J = 1-Zustaende, die das Gitter nicht zeigt.
- **Gitter-Anker (3+1D, dimensionslos):**
  - m(0++)/sqrt(sigma) = 3,405(21)
  - m(2++)/m(0++) = 1,437(11)
  - m(0-+)/m(0++) = 1,550(16)
  - Radius r sqrt(sigma) ~ 0,61(7) (von Hand, eine Gitterweite)
  - In 2+1D andere Zahlen (4,368(7) und 1,658(5)); dort liegt das 0++ selbst auf der Paar-Trajektorie.
- **Regge-Steigung:** Gitter 0,281(22) (Meyer/Teper), aus Athenodorou/Teper 2020 0,372(20). Masseloses Paar 0,444,
  Ring 0,25 bis 0,33. Der Anker haengt an der Zuordnung des 4++.
- **"3/4":** Keine Lesart laesst sich auszeichnen. Die 3/4 steckt mehrfach in Paar-Formeln (WKB n + L/2 + 3/4;
  J ~ (M^2)^(3/4); Masse Paar zu Ring bei gleichem J); bei so vielen Kandidaten ist ein Zufallstreffer zu erwarten.
  Lesart (a) (Enden mit 3/4 c) passt nur unter unphysikalischer Annahme; mit den Daten von 2020 folgt v ~ 0,93.
- **Berichtigung der Leitung:** Mein Schreibtisch-Satz "gleiche Enden heisst nur gerade J" gilt nur fuer den starren
  String. Zwei masselose Gluonen erlauben auch J = 3 und 5, nie J = 1; massive Enden bringen J = 1 auch bei gleichen
  Enden. Er steht in der Karte und in meiner Chat-Antwort (17:33).
  - **Negativliste:** "gleiche Enden -> nur gerade J" (unbedingt).
- **Selbstanzeigen des Agenten:**
  - geschaetzte Uhrzeit berichtigt
  - lokale Werkzeuge ausserhalb der Liste
  - Handrechnungen nicht gegengelesen (K(v), 0,372(20), r sqrt(sigma))
  - r0 = 0,5 fm aus dem Gedaechtnis
  - zwei Quellen ohne Autoren
- **Kartenvorschlag PAAR-REGGE-1** (rotierendes Paar mit fester Endmasse gegen die Gitter-Trajektorie, beide Datensaetze):
  Warteschlange, Rechenplatz.
- **Rueckfragen an Finn:** einzelnes Gluon oder Glueball? Einheit = Netzweite oder Flussrohrdicke?
- **Abschaetzung:** erledigt.
- **Bedeutung:** Finns rotierendes Paar ist ein bekanntes Glueball-Bild fuer die Pomeron-Trajektorie. Als einzelnes
  Gluon passt es nicht, und die 3/4 allein beweist nichts.

### Ernte SPIEGEL-HAELFTE-1 (RUNDE-37/spiegel-haelfte-1/ERGEBNIS.md; eingetragen 2026-10-04 18:22:08 CEST)

- Code-Agent; Spur cpu11; kein frischer Leser.
- **Urteile:**

  | Nr | Plan | Kartenwortlaut | Kennzahl |
  |---|---|---|---|
  | SH0 | eingetroffen | eingetroffen (mit Berichtigungen) | Bloch auf 1e-13; Kegel 1/3, entgegengesetzte Haendigkeit |
  | SH1 | nicht eingetroffen | nicht eingetroffen | w_2(100) = 0,717 gegen FJ 0,496; groesste Abweichung 0,448 |
  | SH2 | eingetroffen (knapp) | eingetroffen | Tempo 0,3048 bei W = 2 pi |

- **Ergebnis [M, E]:**
  - Teil A haelt mit zwei Berichtigungen: Die Kompression auf Haelfte 2 ist FJ mit den Projektoren der anderen
    Haendigkeit; die Doppler bei H, P, P' sind die vier entkoppelten fcc-Familien des BCC-Gitters.
  - **Neu und exakt [M, E]:** Bei W = 2 pi ist die ueber die Unordnung gemittelte Amplitude genau der FJ-Zustand
    (Ueberlapp 0,4947 +- 0,0005 gegen FJ-Norm 0,4956).
  - **Aber:** In jeder einzelnen Welt ist die verborgene Haelfte keine Senke. Etwa 44 % des abgeflossenen Gewichts kommen
    zurueck, verwuerfelt; alle Saaten liegen zwischen 0,444 und 0,450.
  - Die Doppler wachsen statt zu verschwinden: 31 % des Gewichts auf 2 liegen bei grossen Wellenvektoren (bei W = 0
    0,11 %, bei FJ 0,013 %).
  - Das Tempo faellt mit W von 0,3237 auf 0,3048 und bleibt knapp ueber der Bandkante 0,300.
- **Selbstanzeigen des Agenten:**
  - SH1 war naeher an ableitbar als die Karte annahm (exakter Mittelwert, grobe Rueckkehr 1/2 im Plan vor dem Lauf).
  - Urteil haengt an der vorab festgelegten Paketbreite.
  - Teil-A-Berichtigungen nicht gegengelesen
  - eine Genauigkeitsangabe im Plan zu klein (6e-11 statt 3e-11)
  - lokale Werkzeuge ausserhalb der Liste
- **Abschaetzung:** erledigt.
  - Finns "dark tick je Knoten" macht die sichtbare Welt nur im Mittel zum doppler-freien Schachbrett, nicht in einer
    einzelnen Welt.
  - PT-AUSGLEICH-1 (Lesart N9) bleibt in der Warteschlange; vor dem Schreiben Ableitbarkeitsprobe gegen dieses Ergebnis.
- **Bedeutung:** Eine verborgene Haelfte mit eigenem Takt je Knoten ist keine echte Senke. Sie gibt gut 40 % zurueck,
  verwuerfelt ueber alle Wellenlaengen; nur der Mittelwert ueber viele Welten sieht aus wie das Schachbrett.
- 2026-10-04 18:30:35 CEST: Finn, woertlich: "Weiter recherchieren und abrufen was trägt" (zwischen 18:23 und 18:27) und "Geh noch mal alles durch in Kurzform Teilmodell für das Quantenmodell, was für Komponenten brauchen wir?" (zwischen 18:27 und 18:29). Abrufe der Leitung F1 bis F3 mit Erwartungen vorab (ARBEITSFELD 18:29:09; Texte RUNDE-42/quellen-leitung/ABRUFE-1830.md): verzweigte PT-Gitter (2601.03189), Pushmepullyou (math-ph/0501049), Drei-Kugel-Schwimmer (cond-mat/0402070); dazu 2610.00774 aus den Scout-Rohdaten. Kurzuebersicht RUNDE-42/KOMPONENTEN-KURZ.md (fuenf Komponenten mit Stand und Luecken; nicht gegengelesen; Eingang fuer WEICHE-STAND-v6).
- 2026-10-04 18:33:58 CEST: Finn, woertlich: "arbeite weiter an einem gemeinsamen netz was fehlt dabei zur erklärung" (zwischen 18:31 und 18:33). Entwurf RUNDE-42/GEMEINSAMES-NETZ-v1.md (ab 18:33:03): Tabelle Teil des Netzes -> Groesse, Luecken L1 bis L9, Karten FINN-PLATTE-1, EIN-TEMPO-2, MATERIE-NETZ-1 in der Warteschlange; Beobachtung [ES]: Haendigkeit (4D-Rand) und Kleber-Kontinuum (D-Theorie) zeigen auf dieselbe Zusatzrichtung; nicht gegengelesen. Bitte um unabhaengige Lueckenliste an Codex (ag-phy-coordination) per Bus, optional.

### Ernte KOVARIANZ-EPS-1 (RUNDE-37/kovarianz-eps-1/ERGEBNIS.md; eingetragen 2026-10-04 18:45:56 CEST)

- Code-Agent; 103 von 150 min.
- **Urteile:**

  | Nr | Plan | Kartenwortlaut | Kennzahl |
  |---|---|---|---|
  | KE0 | nicht eingetroffen | nicht eingetroffen | Reproduktion ja; Moebius -6 SE, vorab abgeleitet |
  | KE1 | eingetroffen | eingetroffen | gleiches Vorzeichen bei +-eps, >= 15 SE; Steigung 1,31 +- 0,06 |
  | KE2 | eingetroffen | eingetroffen | Steigung 2,010 +- 0,022 |
  | KE3 | nicht eingetroffen | nicht eingetroffen | +126 % von N = 1000 auf 4000 |
  | KE4 | nicht eingetroffen | nicht eingetroffen | -11,2 +- 0,4 mal Einstein, falsches Vorzeichen |

- **Ergebnis [E]:** Die Nicht-Glaette liegt an der Neuvernetzung, aber keine Bauweise gibt Einstein.
  - (a) Neu geknuepftes Netz: gleiches Vorzeichen fuer +-eps, Wachstum wie eps^1,31, ungerader Anteil 14 bis 18 %,
    waechst mit N. Der Erwartungswert ist exakt die Differenz zweier frisch gebauter Ensembles, kein Paarungsartefakt.
  - (b) Mitgenommene Verbindungen: glatt und quadratisch, aber positiv und 11-mal zu gross. Ursache ist der Scherterm des
    festen Netzes (Delta Gamma = N <tr H^2>/24, vorab vorhergesagt, gemessen 0,72 bis 1,17 der Vorhersage); er
    ueberdeckt das Einstein-Glied.
  - eps = +0,1 ist nicht baubar (Einbettung nur bis 0,05).
- **Selbstanzeigen des Agenten:**
  - eine Kontrolle vor dem Einfrieren gesehen, Vorhersagen A4/A5 danach
  - Datei lauf.tmp versehentlich 21 s im fremden Ordner runde41-kovarianz-kugel/, ungelesen verschoben; dort alle 38
    Pruefsummen unveraendert
  - Handwert Faktor 2 falsch, Code richtig
  - Scherkontrolle D kalibriert nicht
- **Abschaetzung:** erledigt; Kovarianz-Strang auf dem S^4-Punktnetz parken. Weder Neuknuepfen noch festes Netz gibt
  Einstein. WEICHE-STAND-v6 kann jetzt geschrieben werden (KOVARIANZ-EPS-1 und WINDUNG-LESER fertig).
- **Bedeutung:** Auf diesem 4D-Punktnetz kommt Einsteins Schwerkraft auf keinem der beiden Wege heraus. Neu geknuepft
  reagiert das Netz unsauber, fest verknuepft wird es geschert, und die Scherung ueberdeckt alles.

### Ernte SCHREIBTISCH-LESER (RUNDE-37/schreibtisch-leser/GEGENLESEN.md; eingetragen 2026-10-04 18:45:56 CEST)

- pruefer-opus, frisch; 18:21:13 bis 18:43:02; 32 Rechenschritte nachgerechnet: 24 halten, 3 mit Einschraenkung,
  5 fallen; 2 Abrufe.
- **A-Befunde (alle in RUNDE-42/SCHALTER-UND-ATMEN.md als BERICHTIGUNG eingetragen):**
  - **A1:** Finns Raute ist bei gleicher Kopplung nicht im 120-Grad-Zustand, sondern A = B, C = D gegenphasig. Damit
    fallen Teil E, die RAUTE-ATEM-1-Statik und der Klapptakt-Antrieb. An den laufenden Agenten gemeldet (18:44,
    vor dem Einfrieren erbeten).
  - **A2:** Sichtlaenge fuer harte Kugeln 2d(1 - phi)/(3 phi); "sieht nur Beruehrungsnachbarn" zu stark.
  - **A3:** Phasen koennen um ein Dreieck eine volle Windung haben; B2 gilt nur fuer reelle Groessen.
  - **A4:** ATEM-NETZ-1: Gueltigkeitsbedingung zu schwach; Einfrieren bei mu k eps z delta/2 = omega ableitbar; AN2
    misst nur z. An den laufenden Agenten gemeldet.
- **Selbstanzeige der Leitung:** A1 und A3 habe ich Finn um 18:23 bzw. 17:5x als Ergebnis gemeldet ("Deine Skizze
  stimmt", "Umlauf null bei Taktphase"). Berichtigung an Finn in der naechsten Meldung.
- **Negativliste (nicht wiederholen):**
  - "Finns Raute ist der Grundzustand bei gleicher Kopplung"
  - "Umlauf nur mit eigenem Kantenwert (auch fuer Phasen)"
  - "lambda = 2d/(3 phi) fuer harte Kugeln"
  - "sieht nur seine Beruehrungsnachbarn"
  - "Statik: das Gegenteil von Finns Kraftbild"

### Ernte PAAR-REGGE-1 (RUNDE-37/paar-regge-1/ERGEBNIS.md; eingetragen 2026-10-04 18:45:56 CEST)

- Code-Agent; Spur cpu11; Abgabe 18:43:38.
- **Urteile:** PR0, PR1 und PR2 nicht eingetroffen, nach Plan und nach Kartenwortlaut.
- **Ergebnis [E]:**
  - Das rotierende Paar mit Endmassen traegt die fuehrende Gitter-Trajektorie in keinem Datensatz: (A) chi^2 = 371
    bzw. 202; (B) chi^2 = 70 bzw. 67.
  - Es scheitert am festen Intercept, nicht an der 3/4. Schon das masselose Paar ist beim 2++ zu schwer (5,317 bzw.
    5,205 gegen 4,894); Endmassen machen es schwerer.
  - Nur eine lose Lesart (Korrelation weggelassen) laesst "masselos" zu; nicht robust.
- **Formelfehler im Dossier GLUON-PAAR-L:** Bindend ist sigma_A sqrt(1 - v^2) = gamma m v^2 / R. Damit gibt "konstantes
  v = 3/4" den Wert 6,331 statt 6,80; der Sonderfall verschiebt sich auf v ~ 0,71 / 0,83. Die Probe dE/dJ = omega haelt
  auf 3,5e-9.
- **2+1D (beschreibend):** passt mit schweren Enden; v_end(4) ~ 0,73 erst nach der Rechnung gesehen, kein Befund.
- **Selbstanzeigen des Agenten:**
  - Bildskript nach dem Einfrieren (nur Zeichnung)
  - Hauptlesart nach Sicht gewaehlt (offengelegt, alle Lesarten im Urteil)
  - **grep ueber "regge-anschluss" schloss KS-1- und VERSIEGELT-Pfade nicht aus**: maschinell gelesen, nichts angezeigt
  - Werkzeuge ausserhalb der Liste
- **Abschaetzung:** verwerfen (Lesart "Enden mit 3/4 c" an der Gitter-Trajektorie); erledigt.
- **Bedeutung:** Finns rotierendes Paar mit Enden bei 3/4 c trifft die Glueball-Massen nicht. Das liegt an der Lage der
  Trajektorie, nicht an der 3/4.

### Ernte GUERTEL-2 (RUNDE-37/guertel-2/ERGEBNIS.md; eingetragen 2026-10-04 18:49:35 CEST)

- Code-Agent; eingefroren 17:50:29; 18 Hauptlaeufe und Nachtrag N1; fertig 18:46.
- **Urteile:** GZ4 eingetroffen (Ebene: Verdrillung sammelt sich ~ k^2 an, E(1440)/E(360) = 15,56). GZ0 und GZ1 nicht
  eingetroffen; GZ2, GZ3, GZ5 und GZ6 nicht auswertbar.
- **Ergebnis [E]:**
  - Weder im Fadenmodell noch im Feld wurde der Guertel-Trick gefunden; die Sperre S ist nicht bestimmt. Das ist ein
    Methodenfehlschlag, kein Befund ueber eine hohe Sperre.
    - Der Staley-Weg ist bei 16 bzw. 12 Segmenten nicht durchdringungsfrei (kleinster Fadenabstand 0,00045).
    - Die Stringrelaxation repariert das nicht.
  - Im Raum (SO(3)) springt das Feld auf dem Gitter, sobald an einer Bindung der Drehwinkel pi erreicht ist. Danach ist
    E 360-periodisch: E(720) = E(360), nicht E(0).
  - Die tiefere Energie bei 90 Grad in GUERTEL-1 ist Geometrie (Abstand Ansatz-Anker) [M].
- **Selbstanzeigen:**
  - Code vor Plantext
  - String-Parameter nach zwei Blicken auf eine Kontrolle gewaehlt (Regel blieb)
  - GZ0a im Rauchlauf verfehlt, Bau bewusst nicht geaendert
  - lokale Werkzeuge ausserhalb der Liste
- **Kartenvorschlaege:** gezielter Stoss in Staley-Richtung; GUERTEL-3 (32 Segmente, String mit FIRE-Dynamik).
  **Warteschlange.**
- **Abschaetzung:** weiter, aber nur mit feinerem Faden (GUERTEL-3).
- **Bedeutung:** Der Guertel-Trick ist in unseren Rechnungen weiter nicht gezeigt; die Gitter springen vorher. Fuer den
  halben Spin im Netz fehlt damit noch die Dynamik (Luecke L4 in GEMEINSAMES-NETZ-v1).

### Ernte DREIECK-PUMPE-L (RUNDE-37/dreieck-pumpe-l/DOSSIER.md; eingetragen 2026-10-04 18:49:35 CEST)

- feldforscher; 10 Abrufe (je API-Aufruf einer gezaehlt; nach Selbstanzeige grosszuegig ausgelegt).
- **Zwei Fehler im Schreibtisch der Leitung:**
  - (1) Der Faltwinkel ist kein eigener Kantenwert im Sinn von B2. Er ist die relative Drehung zweier Dreiecke; um jede
    Ecke ist das Ringprodukt 1. Einen echten Umlauf gibt nur das Winkeldefizit, also die Kantenlaengen.
  - (2) Geschlossene Schalen aus eckenteilenden Dreiecken sind nicht starr. Das Kuboktaeder hat 6 innere
    Freiheitsgrade ("Jitterbug").
  - Maxwell-Zaehlung und arccos(1/3) halten. Die Winkeldefizite gelten nur fuer Netze, in denen sich Dreiecke Kanten
    teilen.
- **Ergebnis [S]:**
  - Jedes Maxwell-Gitter hat d(d-1)/2 gleichfoermige Verformungen ohne Energie, in 2D eine und in 3D drei, bei beliebiger
    Dreiecksform (Rocklin u. a. 2017, Volltext).
  - In Finns 3D-Netz schrumpft die einfachste Atembewegung nur quer zu einer Achse; gleichmaessiges Atmen in alle
    Richtungen ist offen.
  - Gleichmaessiges Atmen pumpt nichts. Pumpen braucht eine laufende Phase: Randzustaende im Experiment (Xia u. a.
    2021), Kink-Solitonen mit Reibung (Juergensen u. a. 2025). Pumpen durch das Atmen selbst ist nach Recherchestand
    nicht belegt (24-Monats-Abfrage).
  - Einseitig wird das Netz erst durch ungleich **geformte** Dreiecke, nicht durch ungleich grosse gleichseitige [ES].
    Zufaellige Groessen zerstoeren das Atmen nicht.
- **Kartenvorschlag ISO-ATEM-1:** Hat Finns Netz in der kubischen Zelle mit 8 starren Tetraedern einen endlichen
  Mechanismus, der in alle Richtungen gleich schrumpft? Vorher pruefen, ob das P2_13-Modell von beta-Cristobalit das schon
  klaert. **Naechster Rechenplatz.**
- **Selbstanzeigen:**
  - einmal awk (Zeilenlaengenprobe)
  - erster Abruf leer
  - Abrufzaehlung grosszuegig
  - Zeiten und Zeilenangaben berichtigt
  - eine Unter-grep ohne volle Ausschluesse (laut Namenspruefung keine gesperrten Dateien)
  - E2 nur sekundaer
- **Negativliste:**
  - "Faltwinkel ist ein eigener Kantenwert"
  - "Cristobalit schrumpft beim Erwaermen" (nicht belegt)
  - "ungleich grosse Dreiecke machen das Netz einseitig"
- **Abschaetzung:** erledigt; ISO-ATEM-1 in die Warteschlange (vorne).
- **Bedeutung:** Ein Dreiecksnetz kann als Ganzes atmen, auch mit ungleichen Dreiecken. In eine Richtung pumpt es aber
  nur mit einer durchlaufenden Welle.

### Ernte WEYL-LINEAR-1 (RUNDE-37/weyl-linear-1/ERGEBNIS.md; eingetragen 2026-10-04 18:59:04 CEST)

- Code-Agent; eingefroren 18:33:24; Laeufe cpu8/cpu9; fertig 18:58.
- **Ergebnis [E]:** In keinem Ast ist ein lineares Glied nachweisbar.
  - N = 32 000, 4 Netze: lambda1 = +0,0010 +- 0,0007 (E > 0) und +0,0010 +- 0,0009 (E < 0).
  - Das "-0,0011" aus STRICH-NETZ-1 haelt nicht: Es stammt aus einem Fit mit freiem Achsenabschnitt. Mit dem
    Kartenansatz (Achsenabschnitt 1) ist das Vorzeichen positiv.
- **Urteil WL1:** eingetroffen (1,5 bzw. 1,2 Fehlerbreiten). Der gegenlaeufige Teil war vorab ableitbar
  (spiegelsymmetrisches Ensemble); scheitern konnte WL1 nur am Gleichteil.
- **Neu [E]:** Jedes einzelne Netz hat ein eigenes, zufaelliges lambda1, das mit der Netzgroesse wie etwa N^(-1/2)
  schrumpft (Streuung 0,0070, 0,0023 und 0,0013 bei N = 2000, 8000 und 32 000).
- **Offen:** Die erwarteten Gegenvorzeichen je Ast fehlen (Korrelation +0,16). Ein Gleichteil +0,0010 +- 0,0006
  (1,7 sigma) bleibt; Verdacht des Agenten: ein k^4-Glied, das der Fit nicht kennt (nicht bewiesen).
- **Netzweite (bedingt, "wenn das Netz das Photon traegt"):**
  - Verschwindet lambda1, gilt nur der quadratische Anker: l < 5,9e-28 m.
  - Waere der Gleichteil echt, verlangte LHAASO l < ~55 Planck-Laengen.
  - Formeln und Zahlen des Dossiers geprueft; LHAASO und JLM an der Quelle gelesen.
- **Selbstanzeigen des Agenten:**
  - 16 Altwerte vor dem Einfrieren gesehen (Spannen standen schon im STRICH-Bericht)
  - Rohwerte zwischen Einfrieren und Endauswertung per jq angesehen
  - jq hat lokal einmal gerechnet
  - Kopfrechnungen
  - lokale Werkzeuge ausserhalb der Liste
  - nur 4 Netze bei N = 32 000
  - eigene Stoerungsrechnung von den Daten widerlegt
- **Abschaetzung:** weiter (Fast Lane, messnah): WEYL-LINEAR-2 klaert den Gleichteil mit mehr Netzen, groesserem N und
  k^4 im Fit.
- **Bedeutung:** Ein Zufallsnetz zeigt im Mittel keine gleichmaessige Tempo-Aenderung mit der Energie. Wenn es das Licht
  traegt, muss seine Masche nur unter etwa 6e-28 m liegen. Ein kleiner Rest ist noch zu klaeren.

### Ernte RAUTE-ATEM-1 (RUNDE-37/raute-atem-1/ERGEBNIS.md; eingetragen 2026-10-04 19:00:17 CEST)

- Code-Agent; Plan und Code eingefroren 18:39; Berichtigung der Leitung (SCHREIBTISCH-LESER A1) als eigener Nachtrag
  eingefroren 18:48, vor jeder Sicht auf Hauptergebnisse; fertig 18:58.
- **Urteile (Hauptmodell):**

  | Nr | Plan | Kartenwortlaut |
  |---|---|---|
  | RA0 | nicht eingetroffen | nicht eingetroffen (nach A1 vorab ableitbar) |
  | RA1 | eingetroffen | eingetroffen (ableitbar) |
  | RA2 | nicht eingetroffen | nicht eingetroffen |
  | FP | nicht eingetroffen | nicht eingetroffen |

- **Ergebnis [E]:**
  - Mit Medium faltet die Raute in 3D in allen 12 Laeufen zum Tetraeder (C-D schliesst nach 31 bis 92 Takten); ohne
    Medium bleibt sie flach.
  - Kein Klapptakt: in keinem Lauf eine Wiederoeffnung, C-D bleibt unter 65 Grad Phasendifferenz. Im geschlossenen
    Zustand rueckt stattdessen das Scharnierpaar A-B um 43 bis 69 Grad auseinander.
  - Phasen wie vom Leser vorhergesagt: A und B fast gleich, C und D gleich, zwischen den Paaren 126 bis 166 Grad; kein
    120-Grad-Muster.
  - Kraefte im geschlossenen 3D-Tetraeder: Die groesste traegt der Schliessstab C-D (Druck 0,67 bis 1,10 B), die
    Aussenkanten Zug 0,47 bis 0,88 B, das Scharnier 0,36 bis 0,81 B. FP trifft in keinem der 12 Laeufe ein.
  - 2D (flache Raute, getrennt ausgewiesen): Dort traegt das Scharnier die groesste mittlere Kraft (0,67 bis 0,79 B).
  - **Variante der Leitung (beschreibend, Regeln vor dem Lauf):** C und D atmen mit halber Amplitude, wie die kleinen
    Kreise in Finns Skizze. Finns Kraftbild trifft in 9 von 12 Laeufen ein: Scharnier 0,66 B Zug, Aussenkanten 0,12 bis
    0,18 B, C-D 0,56 B Druck. Der Grund ist, dass A und B gegeneinander atmen. Auch hier kein 120 Grad und kein
    Klapptakt.
- **Selbstanzeigen des Agenten:**
  - falschen 120-Grad-Grundzustand der Karte ungeprueft uebernommen
  - einmal python direkt auf der .69 (Import und Versionsnummern, keine Rechnung)
  - zwei Rauchlaeufe vor dem Plantext, danach Parameter geaendert (im Plan begruendet)
  - Werkzeugprobe teils doppelt
  - Variante ohne Rauchlauf
  - Bildskripte nach dem Einfrieren
- **Abschaetzung:** erledigt; Klapptakt verworfen. Finns Kraftbild gilt nur in der Variante mit kleinen Seitenpunkten
  (beschreibend) und in der flachen 2D-Raute.
- **Bedeutung:** Die Raute klappt durch Gleichtakt-Anziehung zum Tetraeder und bleibt zu. Finns Kraftbild (gross durchs
  Scharnier, klein aussen) stimmt, wenn die Seitenpunkte schwaecher atmen, wie in seiner Zeichnung.
- 2026-10-04 19:00:17 CEST: Gestartet: WEYL-LINEAR-2 (Karte ab 18:59:04; WM0 bis WM2; cpu10; 75 min) und GUERTEL-FELD-STAB-1 (Karte ab 18:59:32; Vorschlag 1 aus GUERTEL-2 woertlich; GS0, GS1; cpu3/cpu5; 75 min). Aktiv 9: ATEM-NETZ-1, QBALL-DREIPOL-2, DIM-LEITER-QBALL-1, VERSCHRAENK-DIM-1, ISO-ATEM-1, WEYL-LINEAR-2, GUERTEL-FELD-STAB-1 (7 mit Rechenlaeufen), DIM-AUSWAHL-L, GEMEINSAMES-NETZ-L. Ein Platz Puffer.

## Abschluss Runde 42 (geschrieben ab 2026-10-04 19:02:31 CEST)

| Karte | Ausgang kurz | Abschaetzung |
|---|---|---|
| KOVARIANZ-2D-GEGENPROBE | Gemeinsamer Code als Ursache ausgeschlossen; die 4D-Anomalie ist 4D-spezifisch | erledigt, Folge KOVARIANZ-EPS-1 |
| EINE-WELT-LOCH-1 | Gefuellte Loecher: eine Welt mit 2 TT-Moden, grossteils aus der Eichwahl; Stabilitaet braucht skalare Regeln; Tempo richtungsabhaengig | weiter als Baustein (Finns Netz mit gefuellten Loechern) |
| STRICH-NETZ-1 | Isotacheia langwellig exakt nur mit patch-test-konsistenten Kopplungen; naive Regeln langsamer (0,94 bis 0,97); Dispersion Weyl 1 - 0,117 k^2 | erledigt |
| DREIECK-TAKT-1 (QCA-WINDUNG-2) | 2D: einseitige Randwelle (Richtung durch Zeitumkehr erzwungen, bekannt); 3D: W3 = 0; DT3 nach Plan und Kartenwortlaut nicht eingetroffen | erledigt, Folge TAKT-RAND-4D-1 |
| KOPPLUNG-TETRA-1 | Finns Netz = beta-Cristobalit; RUM-Ebenen = Tensor-Eis-Ebenen (ableitbar); Verdrehung ist kein Kleber | erledigt |
| KERNMASSE-LESER | haelt mit Einschraenkung; Bedeutung der R41-Aussage zu stark, Journal-Berichtigung veroeffentlicht | erledigt |
| DUNKEL-FLIP-L | Kein Messbefund fuer eine Negativseite; Foster/Jacobson: Masse als Flip zwischen Tetraeder-Schrittsaetzen (nicht unitaer); Anker PSI, Eot-Wash, o-Ps, Doppelbrechung 0,28 Grad | erledigt, Folge SPIEGEL-HAELFTE-1 |
| GLUONEN-L | Finns Netz hat die Form einer Gittereichtheorie; Verdrehung = reine Eichung; Gluonen brauchen SU(3) je Ecke; Farb-Eis "null oder drei rein" [M]; String-Netz-Gluonen nur behauptet | erledigt; FARB-EIS-1 wartet (R3), ZWEI-T-AUSFRIER-1 geparkt |
| WOLFRAM-RUHE-1 | Wolframs 2D-Regel R2 ist eine Kette mit absoluter Uhr, nicht kausalinvariant (vorab ableitbar) | erledigt; geparkt |
| WINDUNG-LESER | K-Theorie-Satz haelt (Read 2017); "nur am Rand" und DT3-Etikett fallen; Geltungsbereich unitaer, frei, translationsinvariant, Volumen | erledigt |
| QBALL-DREIPOL-1 | Dreifarbige Q-Baelle binden (ableitbar) und pulsieren; neu: einfarbiges Dreieck bei g4 = -0,1 (nur symmetrisch gerechnet) | weiter: QBALL-DREIPOL-2 laeuft |
| STRANG-ANKER-L | Einseitiger Strom strahlt nicht (Vortonen); Buendelung braucht Gegenverkehr; feste Anker Cassini, GW-Tempo, LHAASO, Abstandsgesetz | erledigt; WEYL-LINEAR-1 daraus |
| PACHNER-TAKT-1 | Flip-Flop nur mit Zeltstangen; E - G = 3 je Zelle fuer zwei Takte; koppelt die Welten nicht; Reihenfolge-Unterschied linear in eps | parken |
| TAKT-RAND-4D-1 | 3D-Rand eines lokalen 4D-Schrittplans traegt ungepaarte Weyl-Teilchen (Drehsinn aus der Chern-Zahl); rund nur als Dreiergruppe | parken |
| GLUON-PAAR-L | Rotierendes Paar = Glueball-Bild (Meyer/Teper), nicht einzelnes Gluon; 3/4 ohne Auszeichnung; Berichtigung "gleiche Enden" | erledigt |
| SPIEGEL-HAELFTE-1 | Verborgene Haelfte mit eigenem Takt: im Mittel exakt FJ, einzeln 44 % Rueckfluss; SH1 nicht eingetroffen | erledigt |
| KOVARIANZ-EPS-1 | Neuvernetzung unglatt (eps^1,31), festes Netz geschert (11-mal, falsches Vorzeichen); keine Bauweise gibt Einstein | erledigt; Kovarianz-Strang geparkt |
| SCHREIBTISCH-LESER | 32 Schritte: 24 halten, 5 fallen; A1 Raute, A2 Sichtlaenge, A3 Phasenwirbel, A4 ATEM-Gueltigkeit | erledigt; Berichtigungen eingetragen |
| PAAR-REGGE-1 | Paar mit Endmassen traegt die Gitter-Trajektorie nicht (am Intercept, nicht an der 3/4); Formelfehler im Dossier | verwerfen (Lesart a) |
| GUERTEL-2 | Guertel-Trick weiter nicht gezeigt (Methodenfehlschlag; Gitterspruenge); Ebene ~ k^2 | weiter: GUERTEL-FELD-STAB-1 laeuft |
| DREIECK-PUMPE-L | Maxwell-Gitter atmen ohne Energie (d(d-1)/2 Moden); Pumpen braucht laufende Phase; zwei Schreibtischfehler der Leitung (Faltwinkel, starre Schalen) | erledigt; ISO-ATEM-1 laeuft |
| WEYL-LINEAR-1 | Kein lineares Glied im Mittel; Einzelnetz-Streuung ~ N^(-1/2); Gleichteil 1,7 sigma offen | weiter: WEYL-LINEAR-2 laeuft |
| RAUTE-ATEM-1 | Raute faltet zum Tetraeder und bleibt zu; kein Klapptakt; FP verfehlt (Variante halbe Amplitude: 9/12 beschreibend) | erledigt |

- **Schreibtisch der Leitung in Runde 42** (nicht gegengelesen, ausser SCHALTER-UND-ATMEN durch SCHREIBTISCH-LESER):
  - RUNDE-42/NEGATIV-LESARTEN.md
  - RUNDE-42/SCHALTER-UND-ATMEN.md (mit Berichtigung)
  - RUNDE-42/KOMPONENTEN-KURZ.md
  - RUNDE-42/GEMEINSAMES-NETZ-v1.md
  - RUNDE-42/quellen-leitung/ABRUFE-1830.md
- **In Runde 43 laufen weiter:** ATEM-NETZ-1, QBALL-DREIPOL-2, DIM-LEITER-QBALL-1, VERSCHRAENK-DIM-1, ISO-ATEM-1,
  WEYL-LINEAR-2, GUERTEL-FELD-STAB-1, DIM-AUSWAHL-L, GEMEINSAMES-NETZ-L.
- **Warteschlange fuer Runde 43:**
  - WEICHE-STAND-v6 (Leitung, danach frischer Leser)
  - GUERTEL-3
  - FARB-EIS-1 (nach R3)
  - PT-AUSGLEICH-1
  - FINN-PLATTE-1, EIN-TEMPO-2, MATERIE-NETZ-1
  - KERNMASSE N1 und N3
- **Rueckfaelle "vorab ableitbar" am 04.10.:** acht (zuletzt WOLFRAM-RUHE-1, QBALL-DREIPOL-1), im Gedaechtnis vermerkt.
- 2026-10-04 19:03:48 CEST: Runde 42 geschlossen; Journaleintrag claude-runde-v3-42-20261004 (Quellen RUNDE-42/journal-quellen.sha256, Filter RUNDE-42/journal-filter.jq). Weiter in RUNDE-43.md; diese Datei wird nicht mehr geaendert.
