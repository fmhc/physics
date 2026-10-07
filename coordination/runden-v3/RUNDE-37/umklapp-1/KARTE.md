# UMKLAPP-1: Zellen umklappen. Wie und mit welchem Mechanismus klappen Tetraeder in Finns Netz um, und was macht das mit den Schwerewellen? (Runde 46, Finn-Auftrag "Try it")

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 05:51:58 CEST (date), vor jeder Rechnung.
- **Finn (05.10., vor 05:50:21), woertlich:** "Meine Tetraeder können zufällig und unregelmäßig sein. Zellen umklappen - wie und mit welchem Mechanismus? Try it."
- **Herkunft:**
  - DANZER-L: Die Phasonen (Kachel-Umklappungen) entscheiden, ob ein geordnetes Netz von selbst isotrop bleibt. Ruhen sie, ist es isotrop; laufen sie frei mit, gibt es Zusatzfelder und Anisotropie. Frisch gegengelesen.
  - PACHNER-TAKT-1: Der Diagonalwechsel (2-3/3-2-Zug) auf festen Ecken ist allein kein Takt; mit Zeltstangen gesteuert laesst er sich bauen [P].
  - TT-GLAS-1: Zufalls-Delaunay-Netze tragen genau zwei masselose TT-Moden; Code und Maschine liegen vor (tt-glas-1/code/ew.py) [P].
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Der Elementarzug

Der Elementarzug ist der Pachner-Zug auf festen Ecken. 2-3: zwei Tetraeder mit gemeinsamer Flaeche werden zu drei Tetraedern um eine neue Kante; 3-2 ist der Rueckweg.

## Mechanismen, die verglichen werden (Leitung)

- **M-A energetisch:** Ein Zug geschieht, wenn er Energie senkt; bei Zufall bzw. Rauschen auch entropisch.
- **M-B geometrisch (Delaunay):** Die Verbindungen folgen den Eckenlagen. Bewegen sich die Ecken, etwa durch eine Welle, klappen Zellen um, sobald die Delaunay-Bedingung kippt.
- **M-C taktgesteuert:** Die Zuege sind selbst die Zeitentwicklung (PACHNER-TAKT-1, Zeltstangen).
- **M-D quantenmechanisch:** Ueberlagerung von Triangulierungen (Spin-Schaum bzw. CDT). Nur Literatur bzw. Einordnung, keine Rechnung.

## Ableitbarkeitsprobe (vor der Karte, Leitung)

- **Vorab ableitbar [M]:**
  - Im flachen Raum mit festen Ecken trianguliert ein 2-3-Zug dasselbe flache Gebiet neu. Alle Fehlwinkel bleiben null, also aendert sich die Regge-Wirkung nicht (Delta S = 0).
  - Ein flacher Umklapp kostet damit keine Regge-Energie. Er ist eine Umdiskretisierung, keine Geometrieaenderung.
  - Folge fuer M-A: Im flachen Vakuum treibt die Regge-Energie keine Zuege und haelt sie auch nicht auf.
- **Nicht ableitbar:**
  - Was ein Umklapp mit den Feldern auf dem Netz macht. Die Bewegungsgewichte je Tetraeder (J = 1) und die Kanten wechseln, die Geometrie nicht.
  - Ob danach weiter genau zwei masselose TT-Moden da sind, ob das Netz stabil bleibt und wie sich Tempo und Spanne langer Wellen aendern.
  - Wie oft eine Welle der Amplitude a auf einem Zufallsnetz Delaunay-Umklappungen ausloest (M-B). Am Schreibtisch [M, Vermutung]: linear in a ohne Schwelle, weil die Abstaende zur Kugel-Entartung eine Dichte bei null haben.
  - Auf regelmaessigen Netzen mit Kugel-Entartung gilt M-B nicht; das Netz ist dort durch die Verbindungen festgelegt.

## Rechnung (Code-Agent)

1. **Kontrolle:** Zufaellige 2-3-Zuege auf einem flachen Zufallsnetz (N = 128 und 256) aendern die Regge-Wirkung nicht.
2. **M-B:**
   - Zufaellige Eckverschiebungen mit Effektivwert a, relativ zur mittleren Kantenlaenge: a = 1e-4, 1e-3, 1e-2, 3e-2, 1e-1.
   - Zaehlen, wie viele Flaechen bzw. Zuege die Delaunay-Bedingung wiederherstellen.
   - Anteil gegen a, Steigung im log-log-Bild, mehrere Saaten.
3. **Wirkung auf die TT-Wellen:**
   - Auf festen Ecken einen Anteil f der inneren Flaechen per 2-3 umklappen (f = 0, 0,05, 0,2; nur Zuege mit positiven Volumina).
   - Danach mit demselben Code wie TT-GLAS-1 rechnen: Zahl der masselosen TT-Moden, Stabilitaet bei kleinem k, Spanne und mittleres Tempo in mindestens 13 Richtungen.
4. **Beschreibend:** Welche der Mechanismen M-A bis M-D waere fuer Finns Takt logisch? Kurz, mit PACHNER-TAKT-1.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UK0 | Kontrolle [vorab ableitbar]: flache 2-3-Zuege aendern die Regge-Wirkung auf <= 1e-10 nicht | 90 % |
| UK1 | [H] M-B: Der Anteil der Delaunay-Umklappungen waechst ohne Schwelle linear mit der Amplitude (log-log-Steigung 1 +- 0,2 zwischen 1e-3 und 3e-2) | 60 % |
| UK2 | [H] Nach f = 0,2 zufaelligen Zuegen hat jedes Netz bei kleinem k weiter genau zwei masselose TT-Moden und ist stabil | 65 % |
| UK3 | [H] Die Zuege aendern die Spanne langer TT-Wellen je Netz um mehr als 20 % relativ (sie koppeln wie Phasonen an die Wellen) | 50 % |

**Bedeutung (vorab):**
- **UK0 und UK2 treffen ein, UK3 verfehlt:** Umklappen ist bei langen Wellen eine neutrale Umdiskretisierung. Es bringt in Finns Netz keine neuen masselosen Felder, anders als Phasonen in echten Quasikristallen. Fuer DANZER hiesse das: Die Isotropie bleibt, auch wenn Zellen umklappen [H].
- **UK3 trifft ein:** Umklappungen koppeln wie Phasonen an die Wellen. Dann entscheidet der Mechanismus: ein gepinnter haelt sie fest, ein freier bringt Anisotropie.
- **UK1 trifft ein:** In einem Glas loest jede Welle Umklappungen aus. Mit M-B gehoeren sie dann zur Dynamik, ohne Schwelle.

## Rahmen

- Code-Agent; Code aus tt-glas-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner.
