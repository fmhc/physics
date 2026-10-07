# Tetranetz-Physik: Forschungsarchiv zu Finns gefuelltem Tetraedernetz

**Stand:** 07.10.2026, Export aus dem Arbeitsprojekt.

> **Wichtig:** Alles hier sind synthetische Modellrechnungen und Hypothesen. Nichts davon ist eine Bestaetigung durch
> Messdaten, und nichts ist begutachtet (peer review). Die Texte und der Code sind ueberwiegend von KI-Systemen erstellt
> (siehe [BETEILIGTE.md](BETEILIGTE.md)), unter Leitung und auf Ideen von Finn Hinrichsen.
> Kennzeichen im Material:
> - [E] gerechnet
> - [M] Mathematik am Schreibtisch
> - [L] Literatur aus dem Gedaechtnis
> - [S] an der Quelle gelesen
> - [H] Hypothese

## Worum es geht

Die Idee: Raum ist ein Netz aus Tetraedern, das gefuellte Netz V. Die Kanten tragen Laengen und Winkel, die Dreiecke
Kruemmung und Feldstaerke, die Ecken Phasen und Drehrahmen. Die Zeit laeuft in Zeltschichten. Daraus soll eine
Theorie der Teilchenphysik entstehen.

- Kern ist die **Grundgleichung v3** ([coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md](coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md)).
  Sie ist eine 4D-Wirkung aus Regge-Gravitation, diskretem Maxwell (DEC) und einem Q-Ball-Skalarfeld auf dem
  gefuellten Netz.
- Die Architektur Regge + DEC-Maxwell + Skalar ist **Literatur**, unter anderem McDonald/Miller 2010. Eigen sind nur
  die Rechnungen auf diesem Netz.

## Stand je Schicht (Schaetzung der Leitung, 07.10.2026)

| Schicht | Stand | steht | fehlt |
|---|---|---|---|
| Netz und Raum | 65 % | Netz, Fuellung, Gewichte; traegt Licht und Schwerkraft | Herleitung des Netzes; nichtlineare Netzdynamik (Ausnahmezuege beim Umklappen) |
| Schwerkraft | 55 % | Fernfeld wie ART: Lichtablenkung, Shapiro, beta ~ 1, gleiche Uhr fuer Licht und Wellen | Nahfeld, Perihel, Kollaps |
| Licht | 55 % | klassisch und quantisiert ein masseloses, richtungsgleiches Photon | Kopplungskonstante nicht hergeleitet |
| Materiefeld (Q-Baelle) | 30 % | Q-Baelle sind Vielteilchen-Objekte | Massen kleiner Teilchen |
| Spin 1/2 | 20 % | Fadenenden mit Spin-Vorzeichen per Buchhaltung | eine Dynamik, die es erzwingt |
| Starke Kraft | 35 % | SU(2) auf dem Netz schliesst ein und schmilzt ohne Volumenuebergang (kleine Netze) | Fadenspannung (Grenzfall), SU(3) |
| Mesonen, Baryonen | 5 % | duenne Faeden stabil | fast alles |
| Schwache Kraft, Higgs, Generationen | 0 % | - | alles |
| Vergleich mit Messdaten | 5 % | Schranken (GW170817, Doppelbrechung) | Vorhersagen |
| Quantengravitation | 7 % | dynamisches Netz (CDT-artig) gebaut, Volumina zu klein | alles Weitere |

Gesamt grob 22 % (Stand 07.10.2026; Neues und naechste Schritte in [STAND-UND-NAECHSTE-SCHRITTE.md](STAND-UND-NAECHSTE-SCHRITTE.md)) auf dem Weg zu einer kompletten Theorie.

## Verzeichnisse

- `coordination/runden-v3/`:
  - Rundenprotokolle (RUNDE-*.md)
  - Karten mit Erwartungen vor jeder Rechnung, Ergebnisse, Dossiers und Code (RUNDE-37/<karte>/)
  - netz-gpu (GPU-Engine)
- `coordination/research-journal/`: Forschungsjournal; Eintraege unveraenderlich, Berichtigungen als neue Eintraege.
- `coordination/einfach-gesagt/`: Kurzfassungen in einfacher Sprache.
- `model-lab/papers/`: eigene Papierentwuerfe (Quellen).
- `model-lab/netz-viewer/`: Quelltext der Netz-Ansicht. Die Ansicht laeuft unter https://physics.fmhc.io/netz/.

## Bewusst nicht enthalten

- Versiegelte Vorhersagen und Vertraege laufender Blindtests
- Kopien fremder Literatur
- Personendaten, Betriebs- und Steuerdateien, Rohdatenreihen
- Nicht gepruefte KI-Entwuerfe vom 06./07.10.2026, die Durchbrueche behaupten, ohne dass sie gerechnet oder gegengelesen
  sind

Details in [AUSSCHLUESSE.md](AUSSCHLUESSE.md).

## Lizenz

- Texte, Abbildungen und eigene Daten: [CC BY 4.0](LICENSE), Urheber Finn Hinrichsen.
- Code: [Apache-2.0](LICENSE-CODE).
- Namensnennung siehe [NOTICE](NOTICE).

## English summary

A research archive on a filled tetrahedral network as a model for space, gravity, light and particles. It contains
synthetic model computations and hypotheses only: no confirmation by measured data, not peer-reviewed, mostly written
by AI systems under human direction. Texts are CC BY 4.0, code is Apache-2.0.
