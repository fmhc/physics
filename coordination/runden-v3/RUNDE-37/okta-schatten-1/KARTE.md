# OKTA-SCHATTEN-1: Oktaeder, Dodekaeder und Co. als Schattenformen, die Kraefte auf das Tetraeder-Netz uebertragen (Runde 46, Finn-Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 07:12:50 CEST (date), vor jeder Rechnung.
- **Finn (05.10., vor 07:11:59), woertlich:** "Check Noch Mal octahedron Dodecadedron und so als inferierende Schattenformen die Kräfte haben können über den bestehenden Formen bzw Gebilden"
- **Lesart der Leitung:** Schattenformen sind Formen, die im Tetraeder-Netz nicht als Bausteine stehen, aber aus ihm folgen:
  - Loecher: beim Pyrochlor Stumpftetraeder mit Sechseck-Flaechen, beim Tetraeder-Oktaeder-Netz die Oktaeder
  - duale Zellen: bei fcc bzw. Tetraeder-Oktaeder Rhombendodekaeder, bei Frank-Kasper-Netzen Dodekaeder (Weaire/Phelan), bei der 600-Zelle die 120-Zelle mit 120 Dodekaedern
  - Schalen bzw. Eckfiguren: bei der 600-Zelle Ikosaeder, Dodekaeder, Ikosidodekaeder
  - Nach der Hodge-Theorie (HODGE-L) bestimmen die dualen Zellen die Kopplungsgewichte: Hodge-Stern = duales Mass / primales Mass. Die Schattenformen setzen also tatsaechlich, wie stark Kraefte zwischen den Tetraedern wirken [M, S].
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Projektsuche (vor der Karte, alle Dateitypen)

- Tetraeder-Oktaeder-Netz:
  - EIS-1 (steifes Netz, Kraftgesetz eines Fehlpasses) [P]
  - NETZ-C-1 (fcc-Federnetz) [P]
  - TENSOR-EIS-PYRO-1 ("Kruemmung = Regge auf der Tetraeder-Oktaeder-Wabe", Fuellzellen) [P]
  - REGGE-RAND-1: "Gegenprobe Tetraeder-Oktaeder-Wabe nicht gerechnet" [P]
  - Idee A9 OKTAEDER-LUECKE (Q-Ball springt auf Oktaederplaetzen) [P]
- Schwerewellen (TT) und Licht auf dem Tetraeder-Oktaeder-Netz: nicht gerechnet.
- HODGE-L: Die flachen Nullmoden des Lichts auf den Pyrochlor-Kanten kommen von den fehlenden Sechseck-Flaechen (2 flache Baender je k) [M].
- PACHNER-TAKT-1: Diagonalwechsel in Oktaedern als Takt [P].

## Ableitbarkeitsprobe (vor der Karte, Leitung)

- **Vorab ableitbar [M, L]:**
  - Regulaere Tetraeder und regulaere Oktaeder fuellen den flachen Raum ohne Luecke: je Kante 2 Tetraeder und 2 Oktaeder, 2 x 70,53 + 2 x 109,47 = 360 Grad. Es gibt also keine Fehlwinkel und keine Defektlinien.
  - Die Oktaeder sind die Schattenform, die die 7,36-Grad-Frustration aufloest.
  - Das duale Netz sind Rhombendodekaeder [L].
  - Sechseck-Plaketten im Pyrochlor heben die flachen Baender auf, das folgt aus der Zaehlung.
- **Nicht ableitbar:**
  - Tempo und Richtungsmuster des Lichts mit Sechseck-Plaketten
  - ob das Tetraeder-Oktaeder-Netz genau zwei masselose TT-Moden traegt, stabil ist und ohne Abstimmung isotroper ist als Finns gefuelltes Netz V (Spanne 6,34 %). Kubisch ist l = 4 erlaubt, die Groesse offen.

## Rechnung (Code-Agent)

1. **Licht:** Maxwell auf den Pyrochlor-Kanten, (a) ohne und (b) mit Sechseck-Plaketten der Stumpftetraeder-Loecher. Bloch-Werkzeug aus LICHT-FINN-NETZ-1. Messen:
   - Zahl der flachen Baender
   - Tempo und a2-Muster
2. **Schwerewellen:** Tetraeder-Oktaeder-Wabe.
   - Oktaeder als Regge-Zellen, symmetrisch in 4 Tetraeder zerlegt bzw. ueber alle 3 Diagonalen gemittelt; die Wahl steht im Plan.
   - Hamilton-Netz wie EINE-WELT-LOCH-1 bzw. TT-ISO-1, Bewegungsgewichte J = 1 je Zelle.
   - Messen: Zahl der masselosen TT-Moden, Stabilitaet bei kleinem k, Spanne in mindestens 13 Richtungen.
3. **Beschreibend:**
   - Die Diagonalwahl je Oktaeder als verstecktes Drei-Zustands-Feld: Kostet ein Diagonalwechsel im flachen Netz Energie?
   - Die dualen Zellen (Rhombendodekaeder) als Traeger der Hodge-Gewichte.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| OS0 | Kontrolle: Pyrochlor-Maxwell ohne Sechsecke gibt 2 flache Baender je k (HODGE-L) | 85 % |
| OS1 | [H] Mit Sechseck-Plaketten verschwinden die flachen Baender bei allen k != 0, und das langwellige Lichttempo bleibt isotrop | 70 % |
| OS2 | [H] Die Tetraeder-Oktaeder-Wabe traegt genau zwei masselose TT-Moden und ist bei kleinem k stabil | 65 % |
| OS3 | [H] Ihre TT-Spanne ohne Abstimmung liegt unter der von Finns gefuelltem Netz V (6,34 %) | 50 % |

**Bedeutung (vorab):**
- **OS1:** Die Schattenflaechen geben dem Licht Halt. Ohne sie gibt es Nullmoden, also tragen die Schattenformen Kraefte.
- **OS2 und OS3:** Regulaere Tetraeder mit Oktaedern als Schattenform waeren ein flaches, frustrationsfreies Netz fuer Finn, mit weniger Abstimmungsbedarf.
- **OS3 verfehlt:** Auch das Oktaeder-Netz braucht Abstimmung; die Schattenform allein loest die Isotropie nicht.

## Rahmen

- Code-Agent; Code aus licht-finn-netz-1/code und tt-iso-1 bzw. eine-welt-loch-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner: zuerst 1, dann 2.
