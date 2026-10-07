# Runde 5 (v3): alle uebrigen Ideen rechnen

Leitung: claude-primary. Begonnen: 2026-09-30 01:42:38 CEST (gemessen). Explorativ, keine formale Bestaetigung.

## Rahmen

- Finn: "und rechne die anderen ideen aus". Gemeint sind alle noch nicht vergebenen Ideen aus
  RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md, RUNDE-03/IDEEN-20-QBALL-CHEMIE.md und RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md.
- Die v3-Zufallskarte entfaellt, weil alle Ideen gerechnet werden. Der Vergleich "Urteil gegen Zufall" wird nachtraeglich
  gemacht: Welche Karten haette die Leitung gewaehlt, und wie gingen sie aus?
- **Rechenspuren** (kleintest.sh; Finn: "mach die kleinen tests auf anderen karten oder auf cpu"):
  - p4000a (3,0 GB frei)
  - p4000b (1,7 GB frei; WM-1-MB hat Vorrang)
  - cpu und cpu2 auf der .69 (12 Kerne)
  - VS-1 behaelt die P5000.
- Jede Rechnung hoechstens 10 min.

## Verteilung aller uebrigen Ideen

| Paket | Ideen | Code-Grundlage | Wann |
|---|---|---|---|
| R5-A radial 3D | Bio 1 Membran/Young-Laplace, Bio 4 Tod unter Q_min, Bio 17 Mutanten (radial angeregt), Bio 19/34 Fitness und Energiewaehrung aus der Q(omega)-Tabelle, Chemie 11 Keimbildung, Chemie 18 magische Zahlen | Radialcode aus RUNDE-02/tests1d (Test 4) | jetzt |
| R5-B 1D Einzelball | Bio 3 Fuettern, Bio 36 Photosynthese, Bio 38 Winterschlaf, Bio 20/37 Rauschen und Schmelzen, Bio 45 angetriebener Ball, Bio 22 und Chemie 10 Modulationsinstabilitaet/Uebersaettigung | RUNDE-02/tests1d | jetzt |
| R5-C 1D mehrere Baelle und Hintergrund | Bio 2 Osmose, Bio 12 Ladungspendeln, Bio 16 Symbiose, Bio 39 Quorum, Bio 50 Lawinen, Chemie 4 IR-Schwingung, Chemie 9 Massenwirkung, Wellen 6 Gleiten, 7 Windschatten, 11 Fahrtwind | RUNDE-02/tests1d | jetzt |
| R5-D 1D zwei Felder | Bio 8 Zellkern, Bio 15 Raeuber-Beute, Bio 35 Mitochondrium, Bio 48 Altern (masseloser Kanal), Chemie 17 Tensid, Wellen 10 Kreuzen mit zwei Kanaelen | neu, aus tests1d abgeleitet | jetzt |
| 2D-A Zelle | Bio 5/29 Teilung und Vererbung, Bio 7 Q-Schale, Bio 23 Polaritaet, Bio 24 Vielzeller, Bio 28 Groessengrenze, Bio 49 Selbstreplikation | 2D-Code aus RUNDE-03/tests2d-r3 | sobald dieser fertig ist |
| 2D-B Kollektiv und Kristall | Bio 11 Gluehwuermchen, Bio 21 Nische, Bio 25/42 Gitter und Wabe, Bio 26 Schleimpilz, Bio 40 Schwarm, Bio 46 Kapsid (Ringanalogon), Bio 47 Haendigkeit, Chemie 5 Isomere, Chemie 13 Wechselphasen-Kristall, Chemie 19 Aromatizitaet | 2D-Code | danach |
| 2D-C Stroemung | Wellen 4 Kielwasser, 15 Linse, 17 Kelvin-Helmholtz, 18 Karman, 19 Tornado-Auge, Chemie 6 Puffer, Chemie 12 Phasendiagramm | 2D-Code | danach |
| Literatur | Bio 43 Q-Ball-Keime der Struktur, Bio 44 Ursuppe (Codex' Verdichtung) | Papier | nebenbei |

Schon vergeben oder erledigt:
- Runde 2: Bio 9, 10, 14, 31, 32, 33
- Runde 3: Chemie 1, 2/3, 7, 14, 15; Wellen 5, 8/9, 14, 16, 20
- Runde 4: Wellen 1, 2, 3, 12, 13; Chemie 8, 16, 20; Bio 13, 18, 27, 41
- Runde 1: F-1 bis F-3

## Tests: Ergebnisse

Ausgewertet von drei frischen Ernte-Agenten (Anthropic):
- ERGEBNISSE-R5-AB.md: 12 Tests, 02:53:01 bis 03:11:51 CEST
- ERGEBNISSE-R5-CD.md: 16 Tests, 02:53:17 bis 03:13:07 CEST
- ERGEBNISSE-R5-2DA.md: 8 Karten, 03:14:18 bis 03:29:56 CEST. In zwei Logs fehlen ende-Zeilen, weil die Leitung das
  Startskript ueberschrieben hat; die Laeufe endeten mit status=0.

Alle Aufrufe liefen auf der .69; bragg und anderson erst in Version 2 (Zeitintegral-Fix).

Kernzahlen:
- **R5-A (3D radial):**
  - Membran: Young-Laplace auf 1 bis 4 %.
  - Tod: Der Ball haelt sich bis 0,70 bis 0,83 Q_min und hat kurz vor dem Ende omega 1,007, also ueber 1.
  - Mutanten: Baelle mit 1 und 2 Knoten zerfallen nach 141 bis 368 zum Grundzustand.
  - Fitness: E/Q streng fallend, Fenster 111,84 bis 141,48; folgt schon aus der Papierrechnung.
  - Keim: R_c = R_halb auf 0,1 %.
  - magische Zahlen: keine.
- **R5-B (1D Einzelball):**
  - Fuettern: Ueber der Schwelle behaelt der grosse Ball 4 bis 6 % der Ladung, mit omega Energie je Ladung.
    - Unter der Schwelle bleiben entgegen der Papierrechnung 2,4 % haengen, mit etwa 2,1 Energie je Ladung und
      Rueckstoss.
  - Photo: Sprung um den Faktor 18 bzw. 13 an der Schwelle.
  - Winterschlaf: Die Hauptlinie bei 0,70 liegt mit 1,4875 nahe der Resonanz 1,4938.
  - Rauschen: Schmelzschwellen geordnet.
  - Pumpe: verfehlt; kein stabiler getriebener Ball, mit Treiber sogar schnellerer Zerfall.
  - MI: Verklumpung genau fuer S0 < 2/3. Bei 0,72 zerfaellt das dichte Kondensat trotzdem in 20 Klumpen (Kavitation?).
- **R5-C (1D, mehrere Baelle):**
  - Getroffen:
    - osmose, massenwirkung: der Ball loest sich im dichten Hintergrund auf
    - hintergrund: Papier
    - ir: Abstandsschwingung 0,99 bis 1,09 der Vorhersage
  - pendeln: Takt 0,95 bis 1,03, aber die Kontrolle des freien Paars reisst.
  - symbiose: teilweise.
  - quorum und lawinen: Kontrollen reissen.
  - bragg: Die Kette bewegt sich unter dem Paket (T von -14565 bis 14396), nicht auswertbar. L3 prueft hier nur grob
    gegen fein.
  - anderson: Lokalisierungslaenge etwa 4500, aber die periodische Gegenprobe daempft fast gleich stark.
- **R5-D (1D, zwei Felder):**
  - mitochondrium getroffen: Der Gast ruht innen, wird bei v = 0,2 gefangen und entkommt bei 0,4.
  - raeuber: Josephson-Bild.
  - altern: Rate 0,61 bis 1,37 der Formel; eine Bilanz ist unplausibel.
  - tensid: chi sitzt an der Wand (57 bis 74 %).
  - zellkern: Verschachtelung folgt schon aus der Breite 1/m.
  - kreuzen:
    - Ueber c_s nimmt die Stroemung den Ball mit.
    - Unter c_s rutscht er 1,27 weit. Die spaete Beschleunigung ist etwa hundertmal kleiner als ueber c_s; das sieht
      nach einem Anfangsstoss aus (Frage, kein Befund).

## Abschaetzung

Leitung claude-primary, 2026-09-30 03:14:18 CEST (gemessen vor dem Schreiben). 2D-A folgt nach seiner Ernte.

| Karte | Entscheidung | Grund |
|---|---|---|
| Bio 4 Tod | **weiter** | Der Ball lebt unter Q_min mit omega > 1 noch 190 bis 210 Zeiteinheiten. Ist der Rest ein Oszillon? Laengerer Lauf mit Spektrum des Rests |
| Bio 3 Fuettern und Bio 36 Photo | **weiter** (eine Karte) | Aufnahme unter der Schwelle widerspricht der Papierrechnung (2,4 %, Energie ~ nu je Ladung, Rueckstoss). Mechanismus klaeren (nichtlinear? Randschicht?) |
| Bio 22 / Chemie 10, Kavitation | **weiter** | Das dichte Kondensat bei 0,72 (linear stabil) zerfaellt nach einer schmalen Delle in 20 Klumpen: nichtlineare Instabilitaet oder Messfehler? |
| Wellen 10 kreuzen | **weiter** (in M1) | Sub-Schall-Rutschen vermutlich Anfangsstoss; M1 misst mit langsamem Hochfahren (RUNDE-06/medium1d) |
| Bio 1 Membran | parken | bestaetigt das Tropfenbild in 3D; nichts Neues |
| Bio 17 Mutanten | parken | angeregte Knotenbaelle zerfallen wie erwartet |
| Chemie 11 Keim | parken | kritischer Radius stimmt; kappa-Abweichung klein |
| Chemie 18 magische Zahlen | parken | keine |
| Bio 38 Winterschlaf | parken | Linie nahe der Resonanz 1,494; die Resonanz ist ohnehin in Arbeit (RUNDE-06) |
| Bio 20/37 Rauschen | parken | geordnet, aber nur zwei Saaten |
| Bio 45 Pumpe | parken | verfehlt. Idee fuer spaeter: Antrieb genau an der inneren Resonanz statt Pumpe mit Bremse |
| Bio 2 osmose, Chemie 9 massenwirkung (Ein-Feld) | parken | im dichten Hintergrund trivial; die Medium-Fassung rechnet M1 |
| Bio 12 pendeln | parken | Takt stimmt, Kontrolle reisst |
| Chemie 4 ir | parken | bestaetigt die Vorhersage |
| Bio 16 symbiose, Bio 39 quorum, Bio 50 lawinen | parken | Kontrollen reissen oder Bilanzen unplausibel |
| W22 anderson | parken | periodische Gegenprobe trennt nicht; die lineare Fassung rechnet R-5 (RUNDE-06/reflexion) |
| Bio 15 raeuber | parken | Josephson und Selbstfang sind bekannt (L4) |
| Bio 35 mitochondrium, Chemie 17 tensid, Bio 48 altern | parken | gehen in Finns F-5 auf (Q-Atom, Huelle; RUNDE-06) |
| Bio 19/34 Fitness | verwerfen | folgt vollstaendig aus der Papierrechnung (L1 schwach) |
| hintergrund (Papierprobe) | verwerfen | bekannt (Fable-Review, S < 2/3 instabil) |
| W21 bragg (zeitabhaengig) | verwerfen | Messung unbrauchbar (Kette bewegt sich); ersetzt durch die lineare Fassung R-1 (RUNDE-06/reflexion) |
| Bio 8 zellkern | verwerfen | Verschachtelung vorab ableitbar (Breite 1/m) |

**Nachtrag 2D-A** (Leitung, 2026-09-30 03:30:42 CEST, nach ERGEBNISSE-R5-2DA.md):

| Karte | Entscheidung | Grund |
|---|---|---|
| Bio 24 Vielzeller, Ring aus 4 Baellen mit Windung 2 pi/4 | **weiter** | blieb gegen die Vorhersage zusammen (Abstand 8,9 bis 10,0, Ladungsverlust 5e-4). Echte Bindung oder nur Drift? Laengerer Lauf und Endabstand; Anschluss an 2D-B "ringe" (Kapsid) |
| Bio 5/29 Teilung und Vererbung | parken | Kern getroffen: kleine drehende Baelle teilen sich in 2 bis 4 Toechter mit Windung 0, grosse nicht; Drehung wird nicht vererbt |
| Bio 7 Q-Schale | parken | getroffen: ohne Windung fuellt sich das Loch (t = 26), mit Windung bleibt ein Wirbelkern |
| Bio 23 Polaritaet | parken | faellt wie vorhergesagt (0,993 bis 0,999); Ladungs- gegen Energieschwerpunkt mit umgekehrtem Vorzeichen; Gezeiten deckt KF-4 ab |
| Bio 28 Groessengrenze | parken | Messung unklar (Verschmelzen und "Teilen" binnen 10, Verlust 0,81 bis 0,99; Kontrolle teilt sich auch ohne Fuettern) |
| Chemie 12 Phasendiagramm | parken | 5 von 9 Zellen wie vorhergesagt; kein Gas; ohne Thermostat kein echtes Phasendiagramm |
| Bio 49 Selbstreplikation | verwerfen | kein Zyklus, keine Rueckkehr zu m = 2 |

- Bilanz ohne 2D-A: 4 weiter, 20 parken, 4 verwerfen (28 Tests). Mit 2D-A (7 Karten ohne Profil-Vorpruefung): 5 weiter,
  25 parken, 5 verwerfen (35 Tests).
- Urteil gegen Zufall: Diese Runde hatte keine Zufallskarte (alle Ideen gerechnet). Von 28 Tests tragen 4 weiter.
  Drei davon sind Widersprueche zur Papierrechnung (Tod, Fuettern, Kavitation), nicht die erwarteten Treffer.
- Lehre: Kontrollen rissen haeufig bei Vielteilchen-Tests (quorum, lawinen, bragg). L3 allein prueft nur grob gegen
  fein, nicht ob die Messgroesse physikalisch ist (Beispiel bragg). Kuenftig je Test eine Plausibilitaetsschranke
  (z. B. 0 <= T <= 1, Bilanzen) als eigene Kontrolle.

## Einfach gesagt

Wir haben 28 kleine Versuche zu Zellen-, Chemie- und Wellenbildern gerechnet. Die meisten kamen etwa so heraus, wie es
vorher auf dem Papier stand, zum Beispiel wirkt die Haut eines grossen Q-Balls wie die eines Wassertropfens. Spannend
sind die drei Stellen, an denen der Rechner dem Papier widerspricht: Ein Ball lebt unter seiner Mindestgroesse noch eine
Weile weiter, ein grosser Ball schluckt auch Wellen, die er nach der Rechnung nicht schlucken duerfte, und ein dichtes,
eigentlich stabiles Medium zerfaellt trotzdem in Klumpen. Diese drei rechnen wir als naechstes genauer nach.
