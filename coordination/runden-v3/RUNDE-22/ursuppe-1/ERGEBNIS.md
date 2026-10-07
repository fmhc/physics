# URSUPPE-1: Ergebnis (Leitung, Runde 22, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, cpu4 und cpu6), Laeufe 20:41 bis ~21:00 CEST, alle rc = 0.
- Karte: KARTE.md (20:30). Plan eingefroren 20:40:58 (PLAN.md.eingefroren-20261002-204058).
- Code: code/ursuppe.py (sha256 beginnt mit 3681689651b6af0a). Rohdaten in aus/.

## Ergebnis zuerst

1. **Aus einer Suppe ohne Regel entsteht keine Dimension.** Zufaellige 6- und 12-regulaere Graphen (je zwei Saaten)
   haben kein Plateau der spektralen Dimension: ein Zufallsnetz ohne endliche Dimension (U0 eingetroffen).
2. **"Moeglichst viele Dreiecke" laesst die Suppe klumpen statt Raum bilden.**
   - Bei z = 6 zerfallen die Netze in Komponenten. Die abgespaltenen Stuecke sind vollstaendige 7er-Klumpen (K7, jeder
     Knoten mit jedem): Saat 1 hat fuenf (565 + 5 x 7), Saat 2 einen (593 + 7). Clusterkoeffizient 0,71 bis 0,74.
   - Bei z = 12 bleibt ein Netz mit Clusterkoeffizient 0,49 (knapp unter der Klumpenschwelle 0,5).
   - Ein Plateau gibt es nirgends.
3. **Die Flaechenregel (jede Kante in genau zwei Dreiecken) erzeugt keine Flaeche, jedenfalls nicht in dieser
   Abkuehlzeit.**
   - Die Energie faellt um 85 % (~7000 -> ~1000); 42 bis 49 % der Kanten liegen in genau zwei Dreiecken, fast alle
     uebrigen in einem.
   - Es entstehen Flaechenflicken mit Raendern, keine geschlossene Flaeche; d_s ~ 3,8 ohne Plateau.
   - Bei z = 12 liegen sogar 55 % der Kanten in zwei Dreiecken, aber ebenfalls ohne Plateau.
4. **Warum (Kopfrechnung aus GEOMETRIE-STAND [E] und eigene Lesart [H]):**
   - Eine geschlossene Flaeche, in der jeder Knoten Grad 6 hat, muss ein Torus sein (Euler). Die Abkuehlung muesste also
     eine globale Form finden.
   - Grad 12 ueberall ergaebe bei N = 600 eine stark hyperbolische Flaeche (Geschlecht ~301), also gar keine endliche
     Dimension.
   - Lokale Regeln in einer ungerichteten Suppe reichen hier nicht. CDT umgeht das, indem es Bausteine fester Dimension
     nach einer Zeitregel zu einer Mannigfaltigkeit verklebt (Literatur, GEOMETRIE-STAND).
5. **Messgeraet geeicht:** Das Dreiecksgitter auf dem Torus ergibt ein Plateau mit d_s = 2,04 (Schwankung 3,2 %); der
   Zufallsgraph hat keins.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| K0 | Gitter Plateau 1,6 bis 2,4, Zufall ohne Plateau | **bestanden**: 2,04 (3,2 %); kein Plateau |
| U0 | E0: kein Plateau mit d_s <= 4 (85 %) | **eingetroffen**: 4 von 4 ohne Plateau |
| U1 | E_tri: klumpt (Komponenten > 1 oder Cluster > 0,5); kein Plateau 1,5 bis 3,5 (65 %) | **nicht eingetroffen, knapp**: z = 6 ja (Komponenten 6 bzw. 2, Cluster 0,74/0,71), z = 12 nein (1 Komponente, Cluster 0,489/0,487); kein Plateau in allen vier Laeufen |
| U2 | E_man, z = 6: >= 80 % t_e = 2 und Plateau 1,6 bis 2,4 (40 %) | **nicht eingetroffen**: 41,5 % / 48,5 %; d_s 3,85 / 3,83 mit 25 % Schwankung (kein Plateau) |
| U3 | E_man, z = 12: < 50 % t_e = 2 (55 %) | **nicht eingetroffen**: 55,2 % / 55,5 % |

**Bedeutung (vorab festgelegt):**
- Der erste Fall (U0 und U1) ist nicht vollstaendig ausgeloest; U1 verfehlt knapp bei z = 12.
- Ausgeloest ist "U2 trifft nicht ein: Die Flaechenregel allein reicht nicht, oder die Abkuehlung bleibt haengen; Grund
  beschreiben". Gruende: die Abkuehlung bleibt in Flicken mit Raendern haengen, und die globale Euler-Bedingung (Torus bei
  Grad 6) muss gefunden werden (Punkt 4).

## Kontrollen

- Energiebuchhaltung: Die laufend mitgefuehrte Energie stimmt am Ende in allen Laeufen exakt mit der Neuberechnung
  (z. B. 1125 = 1125).
- Grade bleiben konstant (alle Laeufe).
- Annahmen: z = 6 man ~34 000 von 2 Mio. Tauschen, tri ~240 000; z = 12 man ~12 000 von 1 Mio., tri ~47 500.

## Latten (v3)

- L1: ja
- L2: ja (Gitter und Zufall als Gegenproben)
- L3: teilweise (zwei Saaten, gleiche Ausgaenge; nur ein N)
- L4: teilweise (Klumpen bei Dreiecksmaximierung und das Entropie-Problem sind Literatur, z. B. Quantum Graphity, nach
  GEOMETRIE-STAND)
- L5: nein

## Selbstanzeigen

- Der erste Zufallsgraph-Erzeuger scheiterte im Rauchlauf und wurde vor den echten Laeufen ersetzt (Zirkulant plus
  Mischen).
- Die Plateau-Grenze wurde fuer mehrere Komponenten auf P(t) > 2 c/N angepasst, im Plan vor den Laeufen.
- Nur N = 600, eine Abkuehlrate.

## Einfach gesagt

Wir haben 600 Punkte zufaellig verbunden und dann nach drei verschiedenen Regeln umsortiert. Ohne Regel bleibt ein
wirres Netz ohne erkennbare Dimension. Mit der Regel "moeglichst viele Dreiecke" ballen sich die Punkte zu dichten Klumpen.
Mit der Regel "jede Kante gehoert zu genau zwei Dreiecken" entstehen Flaechenstuecke, aber keine zusammenhaengende Flaeche.
Eine Dimension entsteht also nicht von selbst aus einer Suppe: Man braucht zusaetzlich eine Bauregel fuer das Ganze, wie
sie andere Forscher mit ihrer Zeitregel einfuehren.
