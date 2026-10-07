# ATEM-NETZ-1: Atmende Punkte (Durchmesser 1 PU), die nur an der Huelle koppeln. Gleichtakt oder Gegentakt, was bildet sich aus Zufallsphasen, und pumpt etwas? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 17:59:59 CEST (date), vor jeder
  Rechnung.
- **Finn (04.10.), woertlich:**
  - Zwischen 17:42 und 17:46: "udn wenn punkte einen durchmesser von PU haben, wie verhalten sich dann perspektiven aus
    einem punkt zu anderen punkten. nehmen wir an das punkte auch miteinander viben können vllt - und jeder punkt mit
    anderen punkten koppelt der im gleichen takt läuft (sinus welle einfach) was für pumpenden konstrukte werden dann
    daraus wenn die aneinander koppeln können an ihrer hülle und damit "atmen" und einen takt erzeugen?"
  - Zwischen 17:55 und 17:57: "PU ist meine eigene Punkt Unit einheit mit der wir rechnen können mal auf punkt ebene"
  - Zwischen 17:57 und 17:59: "und check mal game of life und diese anderen sachen diese logik sachen algorithmen welche
    sich davon statistisch gesehen in so einem netzwerk selbst bilden bei zuerst chaotischer aufteilung der werte / des
    pumpens"
- **Einheiten:** Laenge in PU (Punktdurchmesser in Ruhe = 1 PU), Zeit in Takten (2 pi / omega = 1 Takt).
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der
  Quelle gelesen, [P] Projektdatei, [H] Hypothese.

## Schreibtisch der Leitung (vor jeder Rechnung) [M]

**Modell (nach Finns Bild):**
- Punkt i hat den Durchmesser d_i = 1 + eps sin(phi_i) PU.
- Beruehrungsenergie U = (k/2) Summe_(i<j) max(0, (d_i + d_j)/2 - r_ij)^2.
- Phasen: phi_i' = omega_i - mu_phi dU/dphi_i (+ Rauschen sqrt(2T) xi_i).
- Lagen: fest (Teile A und B) oder ueberdaempft frei, x_i' = -mu_x grad_i U (Teil C).

**Zwei Punkte, die sich dauerhaft beruehren** (Vorpressung delta > eps):
- Ueber den schnellen Takt gemittelt gilt <U> = const + (k eps^2 / 8) cos(phi_1 - phi_2).
- Die Phasen laufen diesen Mittelwert bergab. Stabil ist der **Gegentakt** (Differenz pi); der Gleichtakt ist instabil.
- Folge: Die Kopplung an der Huelle ist im Mittel ein XY-Antiferromagnet auf dem Beruehrungsgraphen. Gueltig, solange
  mu_phi k eps^2 / 8 << omega.

**Was daraus vorab folgt (gemittelt, ohne Rauschen):**
- Zweifaerbbare Graphen (1D-Kette, 2D-Quadrat, 3D-Diamant = Tetraedermitten): voller Gegentakt.
- Dreiecksgitter (2D): 120-Grad-Muster mit Drehsinn +-1 je Dreieck. Die Phasen laufen dann reihum: Ein Dreieck "atmet im
  Kreis".
- Pyrochlor (die Ecken von Finns Tetraedern, je Tetraeder vier sich beruehrende Punkte): Die vier Zeiger je Tetraeder
  summieren sich zu null, also zwei Gegentakt-Paare mit freiem Winkel zwischen den Paaren (riesige Entartung).
  - Mit Rauschen waehlt "Ordnung durch Unordnung" vermutlich die kollineare Lage [L?, Moessner/Chalker 1998, n = 2, an
    der Quelle pruefen].
  - Dann ist jedes Tetraeder "zwei so, zwei gegen", also die **Eisregel als Phasenmuster**.
- **Gleichtakt** (Finns "koppelt mit Punkten im gleichen Takt") entsteht durch die Huelle allein nicht. Er braucht ein
  Medium (Bjerknes, RUNDE-42/SCHALTER-UND-ATMEN.md Teil D) oder eine anziehende Kopplung.

## Ableitbarkeitsprobe und Projekt-grep

**Vorab ableitbar:**
- Gegentakt beim Paar und auf zweifaerbbaren Graphen, 120 Grad auf Dreiecken, Grundzustaende auf Pyrochlor (oben).
- Vergroeberung von Wirbeln im gemittelten 2D-Fall, n ~ ln(t)/t [L].
- Der Pyrochlor-Ausgang mit Rauschen haengt an der Literatur [L?].

**Nicht ableitbar:**
- (a) Starke Kopplung (mu_phi k eps^2 ~ omega): Bleibt der Takt, oder frieren Phasen ein ("Takt-Stillstand")? Ist
  Finns frustriertes Netz anders als der Diamant?
- (b) Freie Lagen nahe der Verklemmung: Welche Muster bilden sich aus Zufallsphasen (Gegentakt-Gebiete, Drehsinn-Gebiete,
  Wirbel, eingefrorene Takte)? Erhoeht das Atmen die Beweglichkeit?
- (c) Pumpen: Drehen sich Dreiecke, die im Kreis atmen, je Takt um einen kleinen Winkel mit dem Vorzeichen ihres
  Drehsinns (geometrische Phase wie bei der "fallenden Katze", Shapere/Wilczek [L])?
- (d) Erreicht die Dynamik auf Pyrochlor wirklich die Eisregel (Anteil "2 + 2", Kollinearitaet), oder bleibt sie im
  entarteten Haufen haengen?

**Projekt-grep (17:46 bis 17:59):**
- Diskrete Life-Regeln auf Finns Netzen sind gerechnet: LIFE-DIAMANT-1 (alle 512 Regeln) und LIFE-FCC-1 (7098 Regeln).
  In keiner Regel entstand aus Zufallsstarts ein Gleiter; es bleiben Asche, Stilleben und Blinker (RUNDE-37/life-*).
- Diese Karte ist die kontinuierliche Fassung: Phasen statt Ja/Nein, Kopplung ueber die Huelle.
- Weitere Treffer:
  - Bjerknes: laser-experimente-20260928/BERICHT-LASER.md
  - Q-Baelle verschmelzen gleichphasig: RUNDE-02
  - Eisregel: TENSOR-EIS, Fluss-Eis
  - Eshelby: RUNDE-17, RUNDE-34
- Keine Karte mit atmenden Kugeln oder Phasen-Eis.

## Auftrag (Code-Agent)

**0. Literatur (hoechstens 2 Abrufe, nur arXiv, keine Websuche):**
- Moessner/Chalker 1998 (Ordnung durch Unordnung bei n = 2 auf Pyrochlor).
- "pulsating active matter" (Zhang/Fodor 2023?) [L?].
- Den Befund in den Plan schreiben, bevor gerechnet wird.

**1. Teil A, Kontrollen (feste Lagen, Abstand 1 - delta mit delta > eps):**
- Paar, 1D-Kette, 2D-Quadrat, 2D-Dreieck, 3D-Diamant.
- Volle Dynamik gegen die gemittelte XY-Vorhersage bei schwacher Kopplung.

**2. Teil B, Finns Netz (feste Lagen, Pyrochlor):**
- Zufallsphasen, kleines Rauschen T, schwache und starke Kopplung.
- Messen:
  - Anteil der Tetraeder mit Zeigersumme ~ 0
  - Kollinearitaet (nematische Ordnung)
  - Anteil "2 + 2"
  - Dichte der Fehlstellen "3 + 1" ueber die Zeit
  - Anteil eingefrorener Takte (Phasengeschwindigkeit < 0,1 omega)
- Diamant als zweifaerbbare Kontrolle unter gleichen Bedingungen.

**3. Teil C, freie Punkte in 2D und 3D:**
- Fuellgrade:
  - 2D: 0,80, 0,84, 0,88 bei N ~ 500
  - 3D: 0,60, 0,64, 0,68 bei N ~ 1000
- Zufallsphasen; schwache und starke Kopplung; Kontrolle eps = 0.
- "Was bildet sich von selbst" (Zaehlung wie bei Life-Asche):
  - Gegentakt-Korrelation an Beruehrungen
  - Drehsinn-Gebiete auf Beruehrungsdreiecken
  - Wirbel (2D: Phasenwindung um Delaunay-Dreiecke; 3D: Wirbellinien, wenn machbar)
  - eingefrorene Takte
  - mittlere Verschiebung gegen die Kontrolle
  - Drehung je Takt von Beruehrungsdreiecken gegen deren Drehsinn (Pumpen)

**4.** Plan, Rauchlauf und Einfrieren wie ueblich; Auswerte-Code vor jeder Sicht auf Hauptergebnisse einfrieren.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| AN0 | Kontrollen: Paar endet im Gegentakt (Differenz pi auf 0,05 rad); Kette, Quadrat und Diamant mit Gegentakt-Ordnung >= 0,95; Dreieck mit Drehsinn-Betrag >= 0,9 je Dreieck; volle und gemittelte Dynamik bei schwacher Kopplung auf 10 % gleich | 85 % |
| AN1 | [H, L?] Pyrochlor, schwache Kopplung, kleines Rauschen: >= 90 % der Tetraeder mit Zeigersumme / 4 < 0,1, Kollinearitaet >= 0,8 und >= 80 % der Tetraeder "2 + 2" (Eisregel als Phasenmuster) | 40 % |
| AN2 | [H] Starke Kopplung: Die Kopplung, bei der >= 50 % der Takte einfrieren, liegt auf Pyrochlor um mindestens Faktor 1,5 tiefer als auf dem Diamant | 40 % |
| AN3 | [H] Freie Punkte, 2D, Fuellgrad 0,84, schwache Kopplung: Gegentakt-Korrelation an Beruehrungen <= -0,5, und die mittlere quadratische Verschiebung nach 100 Takten ist >= 2-mal die der Kontrolle eps = 0 | 45 % |
| AN4 | [H] Pumpen: In freien 2D-Packungen korreliert die Drehung je Takt von Beruehrungsdreiecken mit ihrem Phasen-Drehsinn (Korrelation >= 0,3, gleiches Vorzeichen in >= 2 von 3 Fuellgraden) | 25 % |

**Bedeutung (vorab):**
- **AN1 trifft ein:** Atmende Punkte an Finns Tetraederecken bilden von selbst das Fluss-Eis, als Muster aus
  Gleich- und Gegentakt. Die Fehlstellen "3 + 1" waeren die bekannten Eis-Monopole [H].
- **AN1 verfehlt:** Die Phasen bleiben im entarteten Haufen oder frieren ein; Eis entsteht so nicht.
- **AN4 trifft ein:** Ein Haufen atmender Punkte pumpt oertlich, mit dem Drehsinn als Richtung (Ratsche aus
  Gegentakt-Frustration) [H].
- **AN4 verfehlt:** Pumpen braucht einen von aussen gesetzten Phasenversatz.
- **Gleichtakt** entsteht in keinem Teil von selbst. Das waere nur ein Gegenbefund zum Schreibtisch, wenn er doch
  auftritt.

## Dimensionsvergleich (AGENTS.md, Finn 04.10.)

- Raeumlich: 1D (Kette), 2D (Quadrat, Dreieck, frei) und 3D (Diamant, Pyrochlor, frei) getrennt ausweisen.
- Die Phase ist ein innerer Freiheitsgrad (U(1) des Atmens), keine Raumrichtung.
- Wirbel sind in 2D Punkte und in 3D Linien.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und cpu7 (frei seit WOLFRAM-RUHE-1). Je Lauf <= 10 min,
  1 Thread. Zeitbox 150 min.
