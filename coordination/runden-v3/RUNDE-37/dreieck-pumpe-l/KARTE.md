# DREIECK-PUMPE-L: Dreiecke, die an den Ecken binden: Was entsteht, kann ein Netz aus vielen Dreiecken gleichmaessig "atmen" und pumpen, und was aendern ungleich grosse Dreiecke? (Literatur- und Schreibtischkarte, Runde 42)

- Leitung claude-primary. Karte, Schreibtisch und Erwartungen geschrieben ab 2026-10-04 18:10:33 CEST (date), vor jedem
  Abruf.
- **Finn (04.10.), woertlich:**
  - Zwischen 18:05 und 18:08: "und was wenn zwei dreieicke im freien raum aufeinander treffen was gibt das dann für die
    kanten, wenn die sich an den ecken binden können"
  - Zwischen 18:08 und 18:10: "kann daraus ein in der mitte gleich fließendes netz aus vielen dreiecken werden und somit
    ein teil was pumpt? was wenn die dreiecke unterschiedlich groß sind?"
- Einheit: Kantenlaenge bzw. Punktdurchmesser 1 PU (Finns Punkt-Unit).
- Kennzeichen: [S] an der Quelle gelesen, [S Abstract], [P] Projektdatei, [L] Gedaechtnis, [L?] unsicher, [M] eigene
  Mathematik, [ES] eigener Schluss, [H] Hypothese.

## Schreibtisch der Leitung (vor jedem Abruf)

**1. Zwei starre gleichseitige Dreiecke mit klebrigen Ecken [M]:**
- Eine Bindung ist ein Kugelgelenk: 3 freie Drehungen.
- Zwei Bindungen bilden eine gemeinsame Kante, also ein Scharnier. Rechnung: 12 - 3 - 2 = 7 Freiheitsgrade, ohne die 6
  der starren Bewegung bleibt 1 Faltwinkel.
  - **Die Kante bekommt damit einen eigenen Wert, den Faltwinkel.** Er folgt nicht aus den Ecken. Genau so ein eigener
    Kantenwert fehlte dem gerichteten Dreieck (RUNDE-42/SCHALTER-UND-ATMEN.md, B2) und den Gluonen (GLUONEN-L).
- Bei Faltwinkel arccos(1/3) = 70,5 Grad liegen die freien Spitzen 1 PU auseinander (Abstand sqrt(3) sin(theta/2)).
  Binden sie auch, entsteht ein Tetraeder, also Finns Baustein: 5 Kanten der Dreiecke plus 1 neue.
- Drei Bindungen: Die Dreiecke fallen zusammen.

**2. Zaehlung nach Maxwell, je Dimension (AGENTS.md) [M]:**
- Eckenteilende D-Simplexe (jede Ecke in genau zwei) sind in jeder Dimension genau ausgeglichen (isostatisch):
  D(D+1)/2 Freiheitsgrade gegen (D+1) D / 2 Bedingungen.
  - Dreiecke in 2D ergeben das Kagome-Gitter.
  - Tetraeder in 3D ergeben Finns Netz (Pyrochlor bzw. beta-Cristobalit).
  - 4-Simplexe in 4D.
- Dreiecke in 3D (jede Ecke in zwei): 6 - 4,5 = 1,5 lose Moden je Dreieck. Solche Netze sind wackelig; starr werden sie
  erst mit geschlossenen Schalen oder Zusatzbindungen.

**3. Wie viele Dreiecke an einer Ecke, das ist Kruemmung [M, L, P]:**
- Winkeldefizit 2 pi - n 60 Grad.
  - n = 6: flach
  - n = 5: Ikosaeder; genau 12 solche Ecken schliessen eine Kugel (Gauss-Bonnet)
  - n = 4: Oktaeder
  - n = 3: Tetraeder
  - n = 7: Sattel
- Im Projekt: KUGELSCHALE-1, eine Dreieckskugel beult zum Ikosaeder mit 12 Fuenfer-Ecken [P].

**4. Gleichmaessiges Atmen eines Dreiecksnetzes [L, P]:**
- Das Kagome-Gitter hat eine Bewegung ohne Energie, bei der alle Dreiecke gegeneinander drehen und das ganze Netz
  gleichmaessig waechst oder schrumpft (Guest-Hutchinson-Mode; verdrehtes Kagome mit Kompressionsmodul null, Sun, Souslov,
  Mao, Lubensky 2012 [P, RUNDE-34/eis-1]).
- In 3D entsprechen dem die Gegendrehungen der Tetraeder in Finns Netz (RUM). Darum schrumpfen Geruest-Kristalle wie
  Cristobalit beim Erwaermen [L].

**5. Ungleich grosse Dreiecke [L, P, M]:**
- (a) Richtung: Verformte Kagome-Gitter schieben alle weichen Moden an einen Rand (topologische Polarisation,
  Kane/Lubensky 2014 [L]). In 3D tragen verallgemeinerte Pyrochlor-Gitter "Weyl lines" und topologische Randzustaende
  (Stenull/Kane/Lubensky 2016 [P, TETRAEDER-L, S Abstract]).
- (b) Pumpen: Das gleichmaessige Atmen kann die Polarisation umschalten (Rocklin u. a. 2017 [L?]). Ein Atem-Zyklus koennte
  dann etwas von einem Rand zum anderen tragen (mechanische Thouless-Pumpe) [H].
- (c) Kruemmung: Ungleiche Kantenlaengen sind eine Regge-Metrik; die Ecken bekommen Winkeldefizite [M].
- (d) Zufaellige Groessen: weiche Moden lokalisieren; das gleichmaessige Atmen zerfaellt vermutlich in Flecken [H].

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung |
|---|---|
| E1 | Jedes periodische Maxwell-Gitter hat mindestens eine Verformung ohne Energie (Guest/Hutchinson 2003) [L?] |
| E2 | Kane/Lubensky 2014: Die Polarisation folgt aus der Geometrie; im verformten Kagome sitzen die weichen Moden exponentiell an einem Rand [L] |
| E3 | Rocklin u. a. 2017: Die Guest-Hutchinson-Verformung schaltet die Polarisation um ("transformable") [L?] |
| E4 | Mechanische Thouless-Pumpe: Langsame zyklische Aenderung der Gitterparameter traegt einen Randzustand quer durch das Gitter (etwa Rosa u. a. 2019) [L?] |
| E5 | Selbstbau: Dreiklebige Janus-Kugeln bilden in 2D Kagome (Chen/Bae/Granick 2011) [L]; DNA-Origami-Dreiecke mit festem Faltwinkel bilden Ikosaederschalen (Sigl u. a. 2021) [L?]; ohne Winkelvorgabe entstehen in 3D wackelige Gele [H] |
| E6 | Solitonen in topologischen Maxwell-Ketten (Chen/Upadhyaya/Vitelli 2014): Eine Verformungsfront laeuft durch die Kette, also "Pumpen" einer Verformung [L] |

## Fragen

1. Was bilden zwei und viele Dreiecke, die an den Ecken binden (Dimere, Scharniere, Tetraeder, Schalen, Gele), getrennt
   nach 2D und 3D?
2. Kann ein Netz aus eckengebundenen Dreiecken bzw. Tetraedern gleichmaessig atmen und dabei in eine Richtung pumpen?
   Welcher Mechanismus der Literatur passt am besten zu Finns Bild?
3. Was aendern ungleiche Groessen: Polarisation, Kruemmung, Unordnung?
4. Hoechstens ein Rechenkartenvorschlag mit Ableitbarkeitsprobe, moeglichst in Finns 3D-Netz (verallgemeinertes Pyrochlor,
   Anschluss an ATEM-NETZ-1).

## Auftrag (feldforscher)

- **Abrufe:**
  - Hoechstens 10 gezielte Abrufe (arXiv-Abstracts, arXiv-API, Volltexte), keine Websuche.
  - Lokale Kopien in quellen/; Fundstellen nur aus selbst gelesenem Text.
  - Was im Projekt schon steht (Sun u. a. 2012, Stenull u. a. 2016, Lubensky u. a. 2015), nicht neu abrufen, sondern als
    [P] zitieren.
- **Arbeitsweise:** Feld-Regeln (Erwartung vor Abruf mit date-Zeit, eine Arbeitsdatei ARBEITSFELD.md, Gegensweep) und
  Dimensionsvergleich (2D gegen 3D getrennt).
- **Abgabe:** DOSSIER.md mit:
  - Ergebnis zuerst
  - Erwartungen mit Ausgang
  - Antworten auf die Fragen 1 bis 4
  - Ankertabelle, soweit messnah (Materialien, Experimente)
  - Quellenliste
  - Selbstanzeigen
  - "Einfach gesagt" (3 bis 5 Saetze, fuer Finn)
- **Rahmen:** Zeitbox 75 min. Kein Rechnen; lokal kein python, awk oder perl.
