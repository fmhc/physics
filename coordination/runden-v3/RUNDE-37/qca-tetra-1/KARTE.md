# QCA-TETRA-1: Erzwingt die einfachste richtungsgleiche Quanten-Spielregel auf Finns Tetraederrichtungen Spin 1/2? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 05:54:01 CEST (date), vor jeder Rechnung.
- **Anlass:** Finn, 04.10.: "Wie können wir ggf die spins mit space time symetrien und emergenten Mustern und ggf
  Ansätzen von Game of Life oder simpligizierungen finden".
- **Leitidee [L/H]:**
  - Ein Quanten-Zellautomat ist "Game of Life mit Quantenregel": eine lokale, ueberall gleiche Regel, Schritt fuer
    Schritt, aber unitaer.
  - D'Ariano/Perinotti (2014) [L?] verlangen nur Unitaritaet, Lokalitaet, Homogenitaet und Isotropie. Mit dem kleinsten
    nichttrivialen inneren Raum (2 Zustaende je Knoten) finden sie auf dem BCC-Gitter den Weyl-Automaten, also ein
    masseloses Spin-1/2-Teilchen im Langwellen-Grenzfall.
  - Die BCC-Nachbarn liegen in den Richtungen +-(1,1,1), +-(1,-1,-1), +-(-1,1,-1), +-(-1,-1,1). Das sind genau die vier
    Tetraederrichtungen.
- **Schreibtisch [M]:**
  - Die Drehgruppe des Tetraeders T (12 Elemente) hat nur Darstellungen der Dimension 1, 1, 1 und 3.
  - Soll sie auf 2 inneren Zustaenden nichttrivial und unzerlegbar wirken, muss die Darstellung projektiv sein, also
    eine Darstellung der Doppelgruppe 2T (24 Elemente). Dann ergibt eine Drehung um 360 Grad -1: Spin 1/2.
  - Offen ist, ob auch zerlegbare (lineare) Darstellungen nichttriviale unitaere Automaten zulassen. Ist das nicht so,
    erzwingt "2 Zustaende + Isotropie + Unitaritaet" Spin 1/2.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Teil A (Kontrolle):** den Weyl-Automaten von D'Ariano/Perinotti aus der Quelle nachbauen.
  - W(k) als 2x2-Matrix im Impulsraum.
  - Unitaritaet, Kegel bei k = 0 (Geschwindigkeit laut Quelle), weitere Kegelpunkte in der Brillouin-Zone (Verdoppler).
  - Wirkung der Gitterdrehungen auf die zwei Zustaende (360 Grad -> -1?).
- **Teil B (Suche, "Game of Life"-artig):**
  - Alle isotropen 2-Zustands-Automaten mit Spruengen nur in den 8 Richtungen +-e_a.
  - Je moegliche 2-dim Darstellung V der Tetraeder-Drehgruppe getrennt:
    - linear: trivial plus trivial, 1 plus 1', 1 plus 1'', 1' plus 1''
    - projektiv: die drei 2-dim Darstellungen von 2T
  - Unitaritaetsdefekt numerisch minimieren, viele Zufallsstarts.
  - Loesungen einordnen: trivial (reiner Sprung bzw. konstante Phase) oder nichttrivial (Kegel).
- **Teil C (Finns Diamantnetz):** zwei Untergitter; je Schritt Spruenge A -> B laengs +e_a und B -> A laengs -e_a, mit 2
  Zustaenden je Knoten.
  - Gibt es einen isotropen unitaeren Automaten mit Weyl-Kegel bei k = 0?
  - Oder nur Knotenlinien wie in KITAEV-DIAMANT-1?

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QT0 | Kontrolle Teil A: Der Nachbau ist unitaer (<= 1e-12), hat bei k = 0 einen isotropen Kegel mit der Geschwindigkeit der Quelle (<= 1e-6), und 360 Grad wirken als -1 auf die zwei Zustaende | 80 % |
| QT1 | [H] Teil B: Nichttriviale isotrope unitaere Automaten gibt es nur fuer die projektiven (Spinor-)Darstellungen; fuer alle linearen 2-dim Darstellungen findet die Suche nur triviale Loesungen | 55 % |
| QT2 | [H] Teil C: Auf dem Diamantnetz gibt es einen isotropen unitaeren 2-Zustands-Automaten mit Kegel bei k = 0 (Richtungsstreuung der Geschwindigkeit <= 1e-3 bei abs(k) = 0,05) | 45 % |
| QT3 | Teil A: Der Weyl-Automat hat neben k = 0 weitere Kegelpunkte in der Brillouin-Zone (Verdoppler) | 70 % |

**Bedeutung (vorab):**
- **QT0 und QT1 treffen ein:** Auf Finns Tetraederrichtungen erzwingt die einfachste richtungsgleiche Quanten-Spielregel
  Spin 1/2.
  - Teilchen mit halbem Spin waeren dann kein Zusatz, sondern die Mindestausstattung eines Netzes mit Tetraeder-Symmetrie.
  - Lichtgeschwindigkeit und Lorentz-Symmetrie entstehen bei langen Wellen [L?].
  - Folge: Masse (Dirac-Automat, Zitterbewegung), dann derselbe Automat auf unseren Raumzeit-Netzen (Regge, Kausalmenge).
- **QT1 verfehlt:** Auch lineare Darstellungen gehen; Spin 1/2 ist dann eine Wahl, keine Notwendigkeit.
- **QT2 verfehlt:** Auf dem echten Diamantnetz braucht es mehr innere Zustaende oder andere Spruenge. Das waere ein
  Unterschied zwischen BCC und Finns Netz.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und p4000b; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
