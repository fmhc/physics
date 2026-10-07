# Higgs: wiedergefundene Projektbefunde

Bestandsaufnahme 07.10.2026 auf Precision, TS440 und GPU-Rechner. **Korrektur der bisherigen README-Zusammenfassung:** Es gibt bereits numerische Higgsportal-Arbeit, nicht nur Literatur. Ein eigener Higgsmechanismus aus dem Tetraedernetz ist damit weiterhin nicht hergeleitet.

Dies ist eine Sichtung vorhandener Berichte, Code und Ergebnisdateien, keine Wiederholung der Rechnungen. [E-alt] bezeichnet archivierte numerische Befunde; deren komplette Rohfelder und Laufprovenienz wurden hier nicht unabhängig neu validiert. Die Prozentzahl 2 % bleibt vorläufig auf das ursprüngliche Ziel der Herleitung bezogen; sie beschreibt ausdrücklich nicht den Fertigstellungsgrad des Portal-Solvers.

## Gefundene Modelllinie

| Stand | Vorhandene Arbeit | Reichweite und Grenze |
|---|---|---|
| **B13, 25.09.** | Zwei zusätzliche komplexe Singuletts gekoppelt an eine mitvariierende reale Higgsamplitude. 24 stationäre Relaxationen, acht Parametergruppen mit Gitter-/Boxkontrolle. | Eigene klassische Portalrechnung auf Baumebene; Higgsmasse und Vakuumwert sind Eingaben. Kein vollständiges Standardmodell. |
| **B15, 25.09.** | 28 zeitabhängige 3D-Läufe mit bewegten Einzel- und Mehrfachobjekten, realer dynamischer Higgsamplitude. | Kurzes Fenster T=6; weder langfristige Bahnstabilität noch neue Grundkraft nachgewiesen. |
| **B16, 25.09.** | 16 weitere PDE-Läufe, Raumverfeinerung bis 256³, lokale Flussdiagnostik. | Enddichtevergleich auf gemeinsam abgetasteten Knoten: 0,341–0,654 %. Zeitverfeinerung nur für zwei Fälle, nicht sämtliche Fälle. |
| **B17, 25.09.** | Fest-Q-Minimierung in drei räumlichen Dimensionen; Q=250 liefert einen kontrollierten gebundenen Kandidaten. | E/Q=0,886478 gegenüber freier Schwelle 0,9486833. Numerische Existenz ist kein vollständiger Stabilitätsbeweis. Q ist Modellladung, keine elektrische Ladung. |
| **B21, 25.09.** | 17 zusätzliche Optimierungen für Tochterstarts und Energiekurve. | Untersuchte verfügbare Zerfallskanäle liegen energetisch höher; unentdeckte Tochteräste und andere Instabilitäten bleiben offen. |
| **B22/B23, 26.09.** | Konservative Bildung und längeres Halten aus breiten Anfangspaketen. | Die vorab gesetzten Bildungs-/Haltekriterien wurden verfehlt. Stationäre Existenz darf deshalb nicht als bereits gezeigte spontane Bildung erzählt werden. |

## Konkrete Higgsantwort in B13

[E-alt] Der gespeicherte [B13-Datensatz](B13-SUMMARY.json) meldet 24 von 24 bestandene Einzelprüfungen und acht konvergierte Parametergruppen. Bei Portalkopplung g=0,001 sinkt die Higgsamplitude im Kern relativ zum Vakuum um etwa **4,52–4,53 %**, bei g=0,005 um **24,81–24,93 %**. Diese Angaben sind relative Absenkungen, keine negativen absoluten Higgsamplituden. Die Gesamtenergie sinkt gegenüber einem eingefrorenen Higgsprofil um etwa 0,026–0,030 % beziehungsweise 0,658–0,752 %.

Die [gespeicherten Kontrollen](B13-CHECKS.json) prüfen Energiegradienten und den Grenzfall verschwindender Portalkopplung. Die [B15-Kontrollen](B15-QA.json) enthalten zusätzlich Vakuumstationarität und lineare Higgsmasse. Diese Prüfungen zeigen Konsistenz der jeweiligen Implementierung, keine experimentelle Bestätigung.

Die B13-Datei enthält auch einen historischen bedingten Vergleich unsichtbarer Higgsbreiten. Er wird unverändert als historische Auswertung archiviert, hier weder als aktueller experimenteller Grenzwert noch als umfassende Zulässigkeitsprüfung bestätigt.

## Was wir noch nicht haben

- Keine Herleitung von Higgsmasse, Vakuumwert oder Portalstärke aus dem Netz; diese Größen sind gesetzt.
- Keine gemeinsam simulierten chiralen Fermionen und elektroschwachen Eichfelder in dieser Portalmodelllinie.
- Keine nachgewiesenen Elektronen, Quarks oder Baryonen; Bindung von Singulettfeldern liefert deren Quantenzahlen nicht.
- Keine vollständige Stabilitäts-, Quanten- oder experimentelle Gesamtprüfung.
- Keine ungeprüfte Übertragung auf V: die genannten Dynamikläufe verwenden kartesische Raumgitter, keine Rechnung auf dem Tetraedernetz.

Die räumliche Dimension ist 3; zwei komplexe und ein reelles Feld sind die inneren Feldkomponenten, nicht zusätzliche Raumdimensionen. Ergebnisse werden hier nicht auf 1D/2D übertragen.

## Zwei andere Higgs-Spuren getrennt halten

**Gitterverzerrung und Massenhierarchie:** Das ältere Skript `coordination/runden-v3/RUNDE-37/higgs_masse_hierarchie.py` nennt Hoppingwerte an drei fest gewählten Impulsen Massen und sortiert sie. Die bereits vorhandene [Nachprüfung](../runden-v3/RUNDE-37/antigravity-nachbau-1/ERGEBNIS.md) verwirft daraus abgeleitete Vorhersagen: ohne Spin-Bahn-Kopplung fehlen echte globale Lücken; einstellbare Hierarchien sind keine Herleitung. Das Skript ist kein zusätzlicher Higgsnachweis.

**Elektroschwache Kugeln:** Die [EW-BAELLE-Auswertung](../runden-v3/RUNDE-20/ew-baelle/ERGEBNIS.md) ist Literaturarbeit. Sie ist weder B13 noch eine eigene elektroschwache Simulation. Der neue [HIGGS-NETZ-1-Entwurf](../runden-v3/RUNDE-51/modell-screening-1/karten/HIGGS-NETZ-1.md) ist wiederum eine andere Modellvariante: SU(2)-Eichfelder mit festlängigem Materiefeld.

## Ablage und Suchumfang

Auf Precision liegen die Berichte unter `coordination/field-higgs-portal-20260925/`, `field3d-duals-20260925/`, `field-next-20260925/`, `field-fixedq-20260925/`, `field-branches-20260925/`, `field-formation-20260926/` und `field-retention-20260926/`. Die fünf erstgenannten Rechenordner wurden auch auf dem GPU-Rechner als vorhanden bestätigt. Die Berichte nennen CUDA auf einer Quadro P5000 als numerischen Rechenweg.

Auf TS440 ergab die gezielte Dateinamen- und Textsuche im Labor, seinen Experimenten, Dokumentation und Läufen keinen eigenen Higgsportal-Befund. Ein Q-Ball-Modenversuch grenzt sich ausdrücklich vom vollen B17-Portalmodell ab. Das ist keine Garantie, dass keinerlei weitere Kopie außerhalb des Suchbereichs existiert.

[Auszüge weiterer Ergebniszusammenfassungen](RESULT-EXCERPTS.json) enthalten Quellpfade und SHA256 der gelesenen Originaldateien. B13-Zusammenfassung und B13/B15-Kontrolldateien sind unveränderte Kopien. B22/B23 wurden hier anhand ihrer Ergebnisberichte gesichtet.

## Konsequenz für die weitere Suche

B13–B23 bilden eine vorhandene Ausgangsbasis für neue Portalvarianten. Als Nächstes Wirkung, Normierungen und Gitterdiskretisierung explizit mit den neuen Kandidaten vergleichen; vorhandene Läufe nicht allein wegen dieser Wiederentdeckung wiederholen. Der festlängige SU(2)-Pilot und die radiale Portalrechnung beantworten verschiedene Fragen und dürfen sich nicht gegenseitig als Validierung ersetzen.
