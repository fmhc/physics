# HIGGS-MINIMA-1: selbstkonsistenter radialer Vergleich bestanden

08.10.2026 · [E] neue CUDA-Relaxationen, Anschluss an [HIGGS-FORCE-1](../higgs-force-20261008/ERGEBNIS.md).

**Alle 18 Relaxationen konvergieren.** Die zwei reduzierten Higgsenergien E3 und Ecomp bestehen die vorher festgelegten Kriterien für Materieprofil, Gesamtenergie und Frequenz bei festem Q. Das erweitert die vorherige Auswertung festgehaltener Profile: Hier durften die Materieprofile auf die veränderte Energie reagieren.

![Selbstkonsistente Profile und Frequenzen im Vergleich](minima-errors.svg)

## Begrenzter Versuch

Ein ausgewählter Parameterfall: eta=0,05, g=0,005, c8=0, Q=600. Volle Theorie sowie E3 und Ecomp auf Basisgitter (R=20,h=0,05), feinem Gitter (R=20,h=0,025) und größerer Box (R=30,h=0,05). Jeweils zwei Starts: Archivprofil und eine vorab festgelegte lokale 3-%-Verformung. Insgesamt 3 Modelle × 3 Gitter × 2 Starts = 18 Relaxationen. Die volle Theorie wurde als notwendige Referenz desselben Optimierungsvergleichs erneut relaxiert; keine breite Wiederholung des Archivs.

Es handelt sich um reelle radiale Amplituden zweier komplexer Singulettfelder im 3D-Raum. Die gemeinsame Ladung wird über Q²/(4I) festgehalten. Kein 1D-Modell, keine volle räumliche 3D-Stabilitätsrechnung. Beide Starts liegen nahe am bekannten Zweig und sind gleichartig in beiden Komponenten gestört; sie prüfen keine unabhängigen relativen Phasen oder antisymmetrischen Störrichtungen.

## Ergebnis

Maximaler relativer Fehler über alle drei Gitter und beide Starts, gegenüber der jeweils neu relaxierten vollen Theorie:

| Größe | E3 | Ecomp | Vorabgrenze |
|---|---:|---:|---:|
| Materieprofil, radiale L2-Norm | 0,003103 % | 0,00006556 % | 1 % |
| Gesamtenergie | 0,001752 % | 0,00002366 % | 0,1 % |
| Frequenz omega bei festem Q | 0,002658 % | 0,0001124 % | 0,5 % |
| Rekonstruierte Higgsabweichung chi | 0,6464 % | 0,6530 % | nur berichtet |

Die Gates enthalten zusätzlich den im [Vorabplan](PLAN.md) festgelegten Gitter-/Boxaufschlag; beide Modelle bestehen auch damit. Die Fehlerwerte sind keine Messunsicherheiten oder Wahrscheinlichkeiten. Die Gesamtenergie hat hier ausdrücklich einen anderen Nenner als der isolierte Higgsenergiefehler in HIGGS-FORCE-1.

Die Higgsrekonstruktion nutzt für beide reduzierten Modelle chi1+chi2 aus der vorangegangenen Näherung; bei E3 ist das eine ergänzende Rekonstruktion, keine unabhängig variierte Higgsvariable. Der deutlich größere Higgsprofilfehler zeigt: Sehr genaue Materieprofile und Energien bedeuten keine gleichermaßen genaue Higgsamplitude.

- Alle Endresiduen unter **9,93e-8**, vorgegebene Konvergenzgrenze 1e-5.
- Größter Materieprofilabstand zwischen den zwei Starts innerhalb desselben Modells/Gitters: **6,03e-8** relativ; Grenze 0,001.
- Alle Lösungen erfüllen die geprüften Bindungsbedingungen E/Q und omega < sqrt(1-eta).
- Größter Außenladungsanteil jenseits 0,8R: **6,20e-9**, Grenze 1e-6.
- Keine Aussage über alle Fissionskanäle, globale Minimalität oder dynamische Stabilität.

## QA und dokumentierter Fehlversuch

Vor der ersten Relaxation wurde die ursprüngliche B13-Energie gegen den Archivwert sowie der volle analytische B13-Gradient gegen automatische Differentiation geprüft. Der erste Start stoppte im Gradientencheck: Ein Kontrolltensor war versehentlich float32 statt float64. Die Reparatur änderte ausschließlich dessen Datentyp, keine Toleranzen oder physikalischen Parameter. [Reparaturnotiz](REPAIR.md), [alter Code](initial-failure/run.py) und [ursprüngliche Provenienz](initial-failure/results/PROVENANCE.json) sind erhalten. Im erfolgreichen Lauf bestehen die Kontrollen auf allen drei Gittern; Einzelwerte stehen in [QA.json](results/QA.json).

Reduzierte Energien und ihre vollständigen Ableitungen stammen aus HIGGS-FORCE-1. Die Optimierung verwendet energieabnehmende, präconditionierte Schritte und Autograd, keine nachträglich zugeschnittenen Kraftformeln. Alle 18 Fälle erreichen das vorab gesetzte Zielresiduum; keine nachträgliche Änderung der Schrittzahl oder Gates.

CUDA float64 auf Quadro P5000, Torch 2.5.1+cu121; rund **15,97 s** für den erfolgreichen Relaxationslauf, **18,616 s** einschließlich Dienststart. CPU für Steuerung, IO und Diagramm; Profilnormen auch in der Auswertung auf CUDA. Gemeinsamer GPU-Lock und begrenzte Ressourcenpacht, anschließend freigegeben. Kein Geschwindigkeitsvergleich der Modellklassen: Diese Laufzeiten belegen keine Beschleunigung gegenüber der vollen Theorie.

## Daten und Reproduktion

[Rechencode](run.py) · [Auswertung/Grafik](analyse.py) · [Rohprofile aller 18 Läufe](results/RESULT.json) · [Zusammenfassung/Gates](SUMMARY.json) · [Abschlussstatus](results/STATUS.json) · [Laufprovenienz](results/PROVENANCE.json) · [Exportänderungen](EXPORT.json).

Eingabe: [B13-PROFILES.json](../higgs-response-20261008/B13-PROFILES.json), SHA256 `1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d`. Für eine Wiederholung einen frischen Ergebnisordner mit PLAN.md, run.py und analyse.py neben dem Eingabeordner anlegen; `python run.py` und anschließend `python analyse.py` benötigen CUDA. Der archivierte results-Ordner darf nicht als Ausgabe überschrieben werden; der Code verweigert das. Der Export ersetzt ausschließlich den internen Eingabepfad durch die öffentliche Nachbardatei; beide Codehashes sind dokumentiert. Der Code unter initial-failure ist nur Archivmaterial.

## Einordnung für die Modellsuche

[E] Idee 1, die kontrollierte Higgsrückwirkung, ist damit erstmals auch in diesem selbstkonsistenten Pilotvergleich geprüft. Die reduzierte Energie erhält den untersuchten radialen Zweig sehr gut. Das motiviert eine spätere Übertragung auf V mit korrekt gewichteten Operatoren.

[Offen] Der nächste inhaltliche Engpass sind unabhängige Störrichtungen: antisymmetrische Komponenten, relative Phasen und nicht-radiale Moden. Erst eine solche Modenprüfung kann die Aussage über einen stationären Zweig zu einer begrenzten Stabilitätsaussage erweitern. Die zwei nahen Starts ersetzen sie nicht. Zeitentwicklung und Energieerhalt reduzierter Modelle sind ebenfalls noch ungeprüft.

[M] Die Methode der Energieableitung gilt in anderen Raumdimensionen, die hier gemessenen Fehler und Bindungsbedingungen lassen sich aber nicht unverändert übertragen: räumliches Maß, Green-Funktion, Ladungsnormierung und Randwerte ändern sich. Auf V fehlt diese Rechnung weiterhin.

Keine neue Herleitung von Higgsmasse, elektroschwacher Symmetrie oder Hadronen. Subjektive Entwicklungsschätzungen unverändert: Higgs 2 %, schwache Kraft 2 %, Mesonen/Baryonen 10 %.
