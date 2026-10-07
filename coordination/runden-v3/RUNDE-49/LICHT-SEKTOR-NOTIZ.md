# LICHT-SEKTOR-NOTIZ: Welches Licht gehoert in die Grundgleichung v3? (Runde 49, Leitung, Schreibtisch)

- Leitung claude-primary, geschrieben ab 2026-10-05 15:14:15 CEST (date). Schreibtischnotiz, keine Rechnung. Nicht
  gegengelesen; ein frischer Leser folgt.
- Kennzeichen: [M] vorab ableitbar (Rechenweg hier), [P] Projektdatei, [S] an der Quelle gelesen (aus Dossiers
  uebernommen), [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- Anlass: Finn, "o wie kommen wir weiter" (05.10.); meine Abwaegung "vorlaeufig Fluss-Eis" von 14:4x war zu kurz
  (RUNDE-49.md, Eintrag 15:02:02).

## 1. Die Randbedingung aus den Daten

- GW170817 begrenzt den Unterschied der Tempi von Licht und Schwerewellen auf etwa 1e-15 [L; im Projekt RUNDE-23 und
  RUNDE-41].
- RUNDE-41 [P]: Finns Pfeil-Eis-Netz traegt am meisten, aber nur mit Feinabstimmung der Tempi (GW170817; Collins u. a.
  zur Feinabstimmung bei Lorentz-Bruch [L]).
- Folge [H]: Ein Lichtsektor, dessen Tempo eine eigene Konstante ist, braucht eine Abstimmung auf 15 Stellen. Das Licht
  sollte sein Tempo aus derselben Geometrie beziehen wie die Schwerewellen. Das gilt klassisch; Quantenkorrekturen koennen
  die Tempi wieder trennen (Collins u. a. [L]); dafuer braeuchte es eine Schutzsymmetrie.

## 2. Befund L1: Fluss-Eis auf allen Dreiecken von V ist geometrisches Licht [M]

- Fluss-Eis-Lesart auf dem gefuellten Netz V: Fluss E auf jedem Dreieck (duale Kante), Eisregel (Gauss) in jedem
  Tetraeder (duale Ecke), Wirbelgroesse auf den Kanten (duale Flaechen), Kopplungen = duale Hodge-Sterne aus der
  Geometrie von V (*1~ = *2^-1, *2~ = *1^-1).
- Primale DEC-Maxwell-Theorie auf V: A auf den Kanten, omega^2 *1 A = d1^T *2 d1 A.
- Mit Y = *2^(1/2) d1 *1^(-1/2) ist der symmetrisierte primale Operator Y^T Y, der duale Y Y^T. Beide haben dasselbe
  Spektrum ungleich null [M]. Die Fluss-Eis-Lesart auf V und DEC-Maxwell auf V sind also spektral dasselbe Licht.
- Damit erbt das Fluss-Eis auf V die Projektbefunde fuer DEC-Licht auf V:
  - c = 1 fuer jede zulaessige Hebehoehe, gerechnet |c - 1| <= 2e-10 (HOEHE-ISOTROP-1 [P]); dasselbe Tempo wie die
    langen Regge-Wellen (REGGE-WELLE-1: Schwerewellen mit c [P]).
  - Doppelbrechung in (ka)^2 von 1e-4 (Kammermitte) bis 1,9e-3 (HOEHE-ISOTROP-1 [P]); nur als Empfindlichkeit
    begrenzt (a ~ 7,8e-30 m), streng a <= 1,4e-22 m (DOPPELBRECHUNG-V-L [S]).
- Folgt das Licht jeder Verzerrung? [M, Begruendung, nicht an einer Quelle geprueft]: Die Energie eines konstanten
  Feldes ist bei umkreisbasierten (bzw. gewichteten) Hodge-Sternen exakt (lineare Praezision, Konsistenz der DEC). Das gilt
  fuer jede Lage der Ecken, solange die Zerlegung (gewichtet) Delaunay bleibt. Eine affine Verzerrung des Netzes liefert
  also wieder c = 1 in jeder Richtung des verzerrten Raums: Das Licht folgt der Geometrie.

## 3. Befund L2: Fluss-Eis nur auf dem Diamant-Teilnetz kann nicht jeder Verzerrung folgen [M]

- Das Diamant-Teilnetz (Finns auf/ab-Tetraeder) hat je Knoten vier Verbindungsrichtungen (tetraedrisch) und je Ring eine
  von vier Normalen. Bei Kopplungen je Verbindung (diagonal, wie M-D bzw. Benton) ist die langwellige Dielektrizitaet
  eps_ij proportional zu Summe_i w_i l_i l_i^T.
- Fuer die vier tetraedrischen Richtungen hat jede Kombination Summe_i w_i l_i l_i^T gleiche Diagonalelemente
  (Rechnung: jede l_i l_i^T hat die Diagonale (1/3, 1/3, 1/3)); erreichbar sind nur a I plus beliebige Nebendiagonale,
  also 4 von 6 Komponenten.
- Folgen soll das Licht einer Metrik g: verlangt ist eps proportional zu g^-1. Fuer eine Verzerrung laengs der
  Wuerfelachsen (z. B. g^-1 = diag(1 + 2e, 1 - 2e, 1)) ist das unmoeglich, gleich wie die Gewichte aus der Geometrie
  berechnet werden [M].
- In Darstellungen der Wuerfelgruppe: Verzerrungen zerfallen in A1g (Dehnung, 1), Eg (Achsen-Scherung, 2) und T2g
  (Scherung, 3). Diagonale Kopplungen auf dem Diamant-Teilnetz folgen A1g und T2g, aber nicht Eg [M].
- Folge [H]:
  - Ein statisches Newton-Feld ist raeumlich konform flach (A1g) und waere kein Problem.
  - Eine Schwerewelle mit Plus-Polarisation laengs einer Wuerfelachse ist Eg. Ihr koennte dieses Licht nicht folgen;
    das Licht saehe dort die unverzerrte Bezugsgeometrie. Das waere ein Bruch des Aequivalenzprinzips fuer Licht in
    erster Ordnung der Verzerrung.
- Ausweg nur mit nichtdiagonalen Kopplungen (z. B. Feldrekonstruktion je Knoten aus den vier Verbindungen) [M]. Ob
  Bentons Polarisations-Entartung dann bleibt, ist offen.
- Bentons M-D bleibt ein gutes Modell fuer flaches Licht ohne Doppelbrechung (DOPPELBRECHUNG-V-L), ist aber als
  Lichtsektor mit Schwerkraft so nicht tragfaehig.

## 4. Vorschlag fuer v3 [H]

- Licht = Fluss-Eis auf allen Dreiecken von V mit Kopplungen aus der Geometrie (spektral gleich DEC-Maxwell auf V).
  - Vorteile: dasselbe Tempo wie die Schwerewellen ohne Abstimmung; folgt jeder Verzerrung (L1).
  - Preis: kleine Doppelbrechung (ka)^2, nach strengen Daten erlaubt.
- Finns Fluss-Eis-Bild bleibt erhalten, aber auf dem ganzen gefuellten Netz statt nur auf dem Diamant-Teil.
- Offen:
  - O1 aus DOPPELBRECHUNG-V-L (linearer Term a1 an allgemeinen Kammerpunkten)
  - Lichtablenkung und Shapiro an einer echten Masse auf V im selben H
  - Quantenkorrekturen der Tempi (Collins u. a.)

## Einfach gesagt

In der Natur sind Licht und Schwerkraft auf 15 Stellen genau gleich schnell. Das klappt im Netz am einfachsten, wenn das
Licht dieselbe Geometrie benutzt wie die Schwerkraft. Finns Fluss-Eis kann das, wenn der Fluss durch alle Dreiecke des
gefuellten Netzes laeuft. Nur auf dem Diamant-Teil fehlen dem Licht Richtungen: Es koennte dann bestimmten Verzerrungen
des Raums, etwa einer Schwerewelle laengs einer Wuerfelachse, nicht folgen.

## Berichtigung nach dem frischen Leser (15:40:13, date; RUNDE-37/licht-pruefliste-leser/BEFUNDE.md)

- **L1 und L2 sind richtig (Leser rechnete von Hand nach).** L2 gilt sogar exakt: Diagonale Kopplungen auf dem Diamant-Teil erreichen keine Eg-Verzerrung, auch nicht in hoeherer Ordnung. Fuer eps^-1 im Flussbild gilt die Formel exakt; im Potentialbild kommt ein Untergitterterm zweiter Ordnung dazu. Der Ring- bzw. B-Teil hat dieselbe Struktur.
- **A14 (zu stark):** "dasselbe Tempo wie die Schwerewellen ohne Abstimmung" ist nicht gerechnet. Die zwei Werte c = 1 stammen aus verschiedenen Netzen und Regimen (DEC-Licht auf V mit aeusserer Zeit; Wellen auf Kuhn, formal fortgesetzt). Im Regime H auf V sind die Wellen ohne Abstimmung anisotrop, im Regime K gibt es noch kein Licht. Gleiche Tempi sind [H]; die fehlende Rechnung lautet: Licht und Schwerewellen im selben Netz mit derselben Uhr.
- **A15 (fehlender Befund):** Ungewichtet ist V nicht Delaunay; *2 ist an 12 von 116 Flaechen je Zelle negativ (RUNDE-46 Z. 206). Der Vorschlag braucht gewichtete Sterne mit zulaessiger Hoehe (HOEHE-ISOTROP-1). Die Gewichte sind gesetzte Gitterfreiheiten ohne eigene Dynamik, das ist der Preis. Im dualen Bild erbt *1~ = 1/*2 das Vorzeichen.
- **A16:** Der Beweis zu "folgt Verzerrungen" steht schon in RUNDE-37/hoehe-isotrop-1/PLAN.md Z. 38-49, fuer E und B, numerisch <= 7,8e-16. Er gilt nur fuer raeumliche, homogene Verzerrungen im Langwellenlimes, mit neu berechneten Sternen und Gewichten, solange alle Sterne positiv bleiben. Lapse und Shift deckt er nicht. Billige Kontrolle: eine Eg- bzw. T2g-verzerrte Zelle mit dem vorhandenen Code.
- **A17:** Die Wellen kommen aus der hinzugefuegten Dynamik (Bewegungsterm *1~, Wirbelterm *2~), nicht aus der Eisregel. Finns Eisregel allein gibt ruhendes Coulomb ohne Wellen (FLUSS-1, RUNDE-41 Z. 204). Ob diskretes Eis auf den Dreiecken von V eine Coulomb-Phase hat, ist ungeprueft.
- **A18:** Doppelbrechung (ka)^2 von 7e-7 (S1-Ecke) ueber 1e-4 (Kammermitte) bis 1,9e-3, a = kubische Kante. 7,8e-30 m gilt nur fuer guenstige Richtung und Psi = pi/4; streng 0,8e-22 bis 1,4e-22 m; beides [M] des Dossiers.
- **A19:** RUNDE-41 Z. 198-204 ist ein Gutachterurteil [ES], keine Projektrechnung; RUNDE-23 fuehrt GW170817 als [L?]. Den Satz zu Quantenkorrekturen tragen RUNDE-38 Z. 164 und RUNDE-37/blackmon-meow-l/ARBEITSFELD.md Z. 17.
- **A20, A21:** "Ausweg nur mit nichtdiagonalen Kopplungen" gilt innerhalb des Diamant-Teils; mehr Verbindungsarten fuehren zu L1. "Newton-Feld kein Problem" braucht Laengengewichte und eine Takt-Kopplung (MATERIE-NETZ-1). Ein Bruch des Aequivalenzprinzips setzt Materie voraus, die Eg sieht. RUNDE-46 Z. 209 deutet an, dass die Materiekopplung mit festen Volumenanteilen selbst Eg-blind sein koennte; dann waeren Eg-Wellen fuer Licht und Materie zugleich unsichtbar, ein anderer Fehler.
- **Vorschlag fuer v3, berichtigt [H]:** Licht = Maxwell auf V mit gewichteten Hodge-Sternen, gelesen als Fluss auf den Dreiecken mit Eisregel je Tetraeder, plus Dynamik. Pruefstein: gleiches Tempo wie die Schwerewellen im selben Netz mit derselben 4D-Uhr. Das ist noch nicht gerechnet.
