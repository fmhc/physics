# Literatur- und Formelreview vom 8. Oktober 2026

**Sieben ausgewählte arXiv-Volltexte gelesen und mit unserem Modell verglichen.** Die vorhandene statische Portalenergie bleibt in ihrem geprüften Bereich bestehen. Neu dokumentiert sind die dynamische Higgsantwort, Voraussetzungen für Quanten-/Fermionmodelle und konkrete Quellenkritik. Keine neue Simulation, keine neu gemessene Teilchenmasse.

[S] Quellenlektüre · [M] eigene analytische Prüfung/Herleitung · [H] noch ungeprüfte Modellvariante. Fortschrittsschätzungen bleiben Higgs **2 %**, schwache Kraft **2 %**, Mesonen/Baryonen **10 %**; keine Wahrscheinlichkeiten.

## Literaturliste und Entscheidungen

| Quelle, v1-Einreichung | Einordnung im Projekt | Detailreview |
|---|---|---|
| [Craig: A gauge-invariant measure for lattice chiral fermions](https://arxiv.org/abs/2610.09093v1), 06.10.2026 | Neuer Kandidat für chirales Eichfermionmaß; eigene Referenztheorie erforderlich, keine direkte V-Übertragung | [Chiral](CHIRAL.md) |
| [Barceló/Mitra: Schur elimination of brane-localised Higgs mass spectra…](https://arxiv.org/abs/2609.39910v1), 30.09.2026 | Blockelimination/Grenzübergänge nützlich; Verallgemeinerungen teilweise analytisch problematisch | [Quellenkritik](SCHUR-QUELLENKRITIK.md) |
| [Zhang et al.: Fully charmed tetraquarks on the Lattice with controlled errors](https://arxiv.org/abs/2610.07818v1), 06.10.2026 | Nichtrelativistisches Potentialmodell; Schwellen-/Regulatorvergleich übernehmen, keine Hadronbestätigung | [Hadronen](HADRONEN.md) |
| [Topa: Mass as pairing…](https://arxiv.org/abs/2610.07735v1), 06.10.2026 | Bereits am 07.10. erfasst; jetzt vertiefte Volltextprüfung, keine Doppelzählung als neuer Fund | [Chiral](CHIRAL.md) |
| [Henrich/Mambrini/Olive: Spectator Dark Matter and the Higgs Portal](https://arxiv.org/abs/2610.07331v1), 05.10.2026 | Kosmologische Modellvariante; Feldzahl, Wärmebad, Normierung und Anfangsbedingungen unterscheiden sich | [Quanten/Portal](QUANTEN-PORTAL.md) |
| [Su/Xie/Zhou: Quantum-Corrected Q-balls in the Friedberg-Lee-Sirlin Model](https://arxiv.org/abs/2605.25243v1), 24.05.2026 | Älterer Treffer, bereits im internen Q-Ball-Scan vom 25.09.; jetzt Formelübertragung geprüft | [Quanten/Portal](QUANTEN-PORTAL.md) |
| [Copinger/Eto/Nitta: Fermi gas of domain-wall Skyrmions in QCD in a strong magnetic field](https://arxiv.org/abs/2608.26608v1), 27.08.2026 | Ältere spezielle Chiraltheorie mit Magnetfeld und WZW-Struktur; Dichten/Quantisierung nicht blind übertragen | [Hadronen](HADRONEN.md) |

Versionen, Downloadhashes und Lesedeckung stehen maschinenlesbar in [QUELLEN.json](QUELLEN.json), zitierfähig in [references.bib](references.bib). Die Veröffentlichung enthält unsere Analyse und Verweise, keine Kopien fremder Papers.

## Was sich an unseren Formeln ändern sollte

Die vollständige eigene Herleitung samt Konventionen steht im [Formelabgleich](FORMEL-ABGLEICH.md). Priorität hat die **dynamische Erweiterung** der statischen Higgsantwort: frequenzabhängiger inverser Higgsblock, zusätzliche Trägheit und die Amplituden-/Phasenkopplung des rotierenden Hintergrunds. Für den radialen dynamischen Operator muss der Fix-Q-Rang-eins-Zusatz korrekt behandelt werden. Ein bloßes Ziehen der Quadratwurzel aus bisherigen Energiekrümmungen wäre falsch.

Für eine spätere Quantenvariante sind fünf kanonische reelle Felder, deren Kovarianzen, Gesamtladung einschließlich Fluktuationen und EFT-Matching nötig. Ein thermischer Beitrag hängt von den tatsächlich vorhandenen Feldkomponenten ab. Chirale Fermionen und Baryonenquantisierung werden als neue Wirkungszweige formuliert, nicht als zusätzliche Fitkonstanten im vorhandenen Skalarpotential.

## Präzisierungen gegenüber dem ersten Abstract-Scan

- Die allgemeine Rang-zwei-Behauptung für geglättete Kopplungen im Schur-Paper hält unserer analytischen Gegenprüfung nicht stand. Der endliche Schur-Formalismus bleibt verwendbar.
- Die Tetraquarkarbeit zeigt keinen kontrollierten Kontinuumsnachweis des Vierquarkzustands. Unter einer Zweicharmoniumschwelle zu liegen schließt nicht sämtliche starken Prozesse aus.
- Im Domain-Wall-Paper ist eine Dichteumrechnung vor Gl. (5.36) dimensional widersprüchlich; die betreffende Stelle wurde zusätzlich im gerenderten PDF geprüft. Sie wird nicht übernommen.
- Die SMG-Arbeit benennt selbst Quellenüberlappung, eingeschränkte Modenvergleiche und unentschiedene Tests. Das ist kein allgemeines Anti-Seesaw-Ergebnis.

Diese Einordnung unterscheidet explizit zwischen eigenen analytischen Einwänden, Einschränkungen der Autoren und künftig zu prüfenden Übertragungen. Wir behaupten keinen externen Gutachterkonsens.

## Was „gelesen“ hier bedeutet

Die sieben heruntergeladenen **Haupt-PDFs** wurden in aufgeteilten Fachreviews vollständig im extrahierten Volltext gelesen, einschließlich ihrer technischen Anhänge beziehungsweise des im Tetraquark-PDF enthaltenen Supplements. Bildunterschriften, Tabellen und Gleichungen wurden einbezogen; Referenzlisten gesichtet, zitierte Fremdwerke nicht sämtlich nachgelesen. Lesenumfang und genaue Abschnitts-/Gleichungsanker stehen in den Teilreviews.

Nicht eingeschlossen sind Craigs separat verlinkte mathematische/Lean-/2D-Begleitdateien, fremde Codeausführung und Rohdatenreproduktion. Insbesondere wurden der umfangreiche chirale Beweis und seine Formalisierung nicht unabhängig vollständig verifiziert. Volltextlektüre, analytische Gegenprüfung und Reproduktion sind unterschiedliche Evidenzstufen.

## Anschluss an den Bestand

[Literaturvergleich 07.10.](../runden-v3/RUNDE-51/modell-screening-1/VOLLTEXT-VERGLEICH-20261007.md) · [Kandidatenmatrix](../runden-v3/RUNDE-51/modell-screening-1/KANDIDATENMATRIX.md) · [bisherige Portalherleitungen](../higgs-verbindungen-20261007/ANALYTISCHE-BAUSTEINE.md) · [letzte statische Winkelprüfung](../higgs-angular-modes-20261008/ERGEBNIS.md).

Die nächste numerische Aufgabe ist in Abschnitt 6 des Formelabgleichs konkretisiert, aber noch nicht gestartet. Laufende Skyrme-Prüfungen erhalten durch diesen Literaturreview weder neue Kriterien noch rückwirkend geänderte Eingaben.
