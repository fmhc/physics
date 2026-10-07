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

<!-- BEGIN RESEARCH GRAPHICS -->
## Forschungsbereiche in Bildern

Die Grafiken sind schematische Erklärbilder, keine Simulationsergebnisse oder Messdaten. Prozentwerte sind subjektive Entwicklungsschätzungen zum Stand 07.10.2026. Durch Anklicken lassen sich die Grafiken vergrößern; die Berichte darunter liefern Befunde und Grenzen.

| | |
|---|---|
| [![Netz und Raum: Geometrie als Ausgangspunkt. 65 % subjektive Schätzung.](assets/research/netz.svg)](assets/research/netz.svg)<br>**Netz und Raum** · [Befunde](coordination/runden-v3/RUNDE-37/volumen-g2-1/ERGEBNIS.md) | [![Schwerkraft: Krümmung verändert Wege. 55 % subjektive Schätzung.](assets/research/gravitation.svg)](assets/research/gravitation.svg)<br>**Schwerkraft** · [Befunde](coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md) |
| [![Licht: Feld auf Kanten und Flächen. 55 % subjektive Schätzung.](assets/research/licht.svg)](assets/research/licht.svg)<br>**Licht** · [Befunde](coordination/runden-v3/RUNDE-37/quant-2/ERGEBNIS.md) | [![Materiefeld · Q-Bälle: Ein gebundener Feldklumpen. 30 % subjektive Schätzung.](assets/research/materie.svg)](assets/research/materie.svg)<br>**Materiefeld · Q-Bälle** · [Befunde](coordination/runden-v3/RUNDE-37/quant-1/ERGEBNIS.md) |
| [![Starke Kraft: Eichfelder auf dem Netz. 40 % subjektive Schätzung.](assets/research/stark.svg)](assets/research/stark.svg)<br>**Starke Kraft** · [Befunde](coordination/runden-v3/RUNDE-37/quant-3/ERGEBNIS-S6.md) | [![Mesonen und Baryonen: Gebundene Paare und Dreier?. 10 % subjektive Schätzung.](assets/research/hadronen.svg)](assets/research/hadronen.svg)<br>**Mesonen und Baryonen** · [Befunde](coordination/runden-v3/RUNDE-37/qball-dreipol-3/ERGEBNIS.md) |
| [![Spin ½: Drehung, Vorzeichen, Statistik. 20 % subjektive Schätzung.](assets/research/spin.svg)](assets/research/spin.svg)<br>**Spin ½** · [Befunde](coordination/runden-v3/RUNDE-37/gerahmter-faden-1/ERGEBNIS.md) | [![Schwache Kraft: Gesucht: chirale Wechselwirkung. 2 % subjektive Schätzung.](assets/research/schwach.svg)](assets/research/schwach.svg)<br>**Schwache Kraft** · [Befunde](coordination/runden-v3/RUNDE-20/ew-baelle/ERGEBNIS.md) |
| [![Higgs: Gesucht: dynamische Massenerzeugung. 2 % subjektive Schätzung.](assets/research/higgs.svg)](assets/research/higgs.svg)<br>**Higgs** · [Befunde](coordination/runden-v3/RUNDE-20/ew-baelle/ERGEBNIS.md) | [![Generationen: Warum drei Teilchenfamilien?. 2 % subjektive Schätzung.](assets/research/generationen.svg)](assets/research/generationen.svg)<br>**Generationen** · [Befunde](coordination/runden-v3/RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md) |
| [![Vergleich mit Messdaten: Vom Modell zur prüfbaren Vorhersage. 5 % subjektive Schätzung.](assets/research/messdaten.svg)](assets/research/messdaten.svg)<br>**Vergleich mit Messdaten** · [Befunde](coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md) | [![Quantengravitation: Das Netz selbst wird dynamisch. 7 % subjektive Schätzung.](assets/research/quantengravitation.svg)](assets/research/quantengravitation.svg)<br>**Quantengravitation** · [Befunde](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/ERGEBNIS.md) |

Modellideen werden auf Passung zum Netz, bekannte Befunde und prüfbare Vorhersagen untersucht. Die Bilder behaupten insbesondere keine Herleitung von Hadronen, Higgs oder Teilchenfamilien.

<!-- END RESEARCH GRAPHICS -->
## Stand je Bereich (07.10.2026)

Je Bereich steht, was gerechnet ist, was Hypothese ist und welcher Mechanismus fehlt. Alle
Rechnungen sind synthetisch, auf kleinen Netzen und nicht begutachtet. Pfade relativ zu `coordination/runden-v3/`.

**Zur Spalte "Schaetzung":** subjektive, grobe Entwicklungsschaetzung der Leitung, wie weit der Bereich von einem vollstaendigen physikalischen Mechanismus entfernt ist. Sie ist keine Wahrscheinlichkeit, kein Messwert und kein bestaetigter Anteil, und sie wird nicht zu einem Gesamtwert gemittelt. Die verlinkten Ergebnisbefunde haben Vorrang.

| Bereich | Schaetzung | Gerechnet [E] | Hypothese [H] | Fehlt |
|---|---|---|---|---|
| Netz und Raum | 65 % | Netz V mit Gewichten; Umklappen mit Traegheit am Netz ([UMKLAPP-FOLGE-1](coordination/runden-v3/RUNDE-37/umklapp-folge-1/ERGEBNIS.md), [NETZ-NICHTLINEAR-1](coordination/runden-v3/RUNDE-37/netz-nichtlinear-1/ERGEBNIS.md)); mit fester 4-Volumen-Bedingung laufen 3 von 4 Testnetzen stabil, ohne sie keins ([VOLUMEN-G2-1](coordination/runden-v3/RUNDE-37/volumen-g2-1/ERGEBNIS.md)) | Volumenerhalt (unimodular) als Grundregel | voll nichtlineare Rechnung mit allen Ableitungen; Herleitung des Netzes |
| Schwerkraft | 55 % | Fernfeld wie ART (Lichtablenkung, Shapiro, beta ~ 1; [GRUNDGLEICHUNG-v3](coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md)); Perihel-Faktor aus diesen Netzwerten 0,993 bis 1,000 (PPN-Arithmetik, [ANTIGRAVITY-NACHBAU-1](coordination/runden-v3/RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md)) | - | Nahfeld, Kollaps, nichtlineare Dynamik |
| Licht | 55 % | DEC-Maxwell auf V; quantisiert ein masseloses, richtungsgleiches Photon ([QUANT-2](coordination/runden-v3/RUNDE-37/quant-2/ERGEBNIS.md)) | - | Kopplungskonstante nicht hergeleitet |
| Materiefeld (Q-Baelle) | 30 % | Q-Ball-Feld quantisiert (HMC): kein belastbarer Bindungsnachweis fuer 2 bis 5 Quanten, klassische Q-Baelle erst ab etwa 112/lam Quanten ([QUANT-1](coordination/runden-v3/RUNDE-37/quant-1/ERGEBNIS.md)) | Q-Baelle als schwere Vielteilchen-Objekte | Massen kleiner Teilchen |
| Starke Kraft | 40 % | SU(2) auf dem Netz: Einschluss, Deconfinement ohne Volumenuebergang; Flow-Skalen bei zwei Gitterabstaenden auf etwa 1 bis 3 % wie der Hyperkubus, begrenzt durch die Unsicherheit von beta_c ([QUANT-3](coordination/runden-v3/RUNDE-37/quant-3/), S5, S6) | - | SU(3); Fadenspannung (unentschieden); groessere Volumina |
| Mesonen, Baryonen | 10 % | Unveraenderte Q-Baelle sind keine Hadronen: bosonisch, Drehimpulssprung um die ganze Ladung, keine Regge-Gerade ([QBALL-HADRON-1](coordination/runden-v3/RUNDE-37/qball-hadron-1/ERGEBNIS.md)). Q-Ball-Dreierbuendel binden ([QBALL-DREIPOL-1](coordination/runden-v3/RUNDE-37/qball-dreipol-1/ERGEBNIS.md)). Positive Strukturbefunde mit Grenzen: Das 2D-Dreieck ist in allen geprueften Stoerrichtungen ein lokales Minimum ([-2](coordination/runden-v3/RUNDE-37/qball-dreipol-2/ERGEBNIS.md)); 3D-Dreieck und endliche Stabilitaet sind gerechnet ([-3](coordination/runden-v3/RUNDE-37/qball-dreipol-3/ERGEBNIS.md)). Die Symmetrie bleibt aber U(1)^3, kein SU(3), kein Einschluss, kein Baryonennachweis. Negative Wirbelmodelltests: Wirbel-Dreier und -Paare werden abgeschirmt bzw. als Beutel gebunden statt durch einen belastbaren Y-Faden ([Y-1](coordination/runden-v3/RUNDE-10/y1/ERGEBNIS.md), [Y-2](coordination/runden-v3/RUNDE-11/y2/ERGEBNIS.md)) | Faeden mit zwei bzw. drei Enden als Meson bzw. Baryon | jeder Mechanismus mit Einschluss und Quantenzahlen |
| Spin 1/2 | 20 % | Fadenenden mit Fermion-Statistik (Twist); 2-pi-Vorzeichen nur per Buchhaltung, aus einer getrennten Regel ([GERAHMTER-FADEN-1](coordination/runden-v3/RUNDE-37/gerahmter-faden-1/ERGEBNIS.md)) | doppelte Wertung (SU(2)-Rahmen) als Dynamik | eine Dynamik, die Spin und Statistik koppelt |
| Schwache Kraft | 2 % | Kein eigener Mechanismus; Vorarbeit ist eine Literaturauswertung mit Hypothesen zu Abstrahlkanaelen ([RUNDE-20/ew-baelle](coordination/runden-v3/RUNDE-20/ew-baelle/ERGEBNIS.md)) | - | eigener Mechanismus (SU(2)xU(1)) |
| Higgs | 2 % | Kein eigener Mechanismus; nur dieselbe Literaturvorarbeit ([RUNDE-20/ew-baelle](coordination/runden-v3/RUNDE-20/ew-baelle/ERGEBNIS.md)); der KI-Entwurf zur Massenhierarchie hielt nicht ([ANTIGRAVITY-NACHBAU-1](coordination/runden-v3/RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md)) | - | eigener Mechanismus |
| Generationen | 2 % | Negativbefund: Ohne Spin-Bahn-Term geben 64 Flussmuster des Diamanten keine isolierten Knoten; die Massenfolge waere frei einstellbar ([ANTIGRAVITY-NACHBAU-1](coordination/runden-v3/RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md)) | - | Mechanismus fuer drei Generationen |
| Vergleich mit Messdaten | 5 % | nur Schranken (GW170817, Doppelbrechung) | - | Vorhersagen |
| Quantengravitation | 7 % | CDT-artiges dynamisches Netz mit Feldern ([NETZ-DYN-1](coordination/runden-v3/RUNDE-37/netz-dyn-1/ERGEBNIS.md)); Messwerkzeug geeicht, konvergiert langsam ([DS-EICHUNG-2D-1](coordination/runden-v3/RUNDE-37/ds-eichung-2d-1/ERGEBNIS.md)) | 4D aus Zeitschichten | grosse Volumina |

Neues und naechste Schritte: [STAND-UND-NAECHSTE-SCHRITTE.md](STAND-UND-NAECHSTE-SCHRITTE.md).

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
