# Netz-, Feld- und Kontaktmodelle

Stand: 21. Oktober 2026.

Dieses Repository dokumentiert ein KI-gestütztes Forschungsvorhaben unter der Leitung von Finn Hinrichsen.
Ausgangspunkt ist ein räumliches Tetraedernetz mit Feldern. Aktuell untersuchen wir, wie sich diese
Netz- und Feldbeschreibung mit Kontaktmodellen in einer gemeinsamen Wirkung zusammenführen lässt.
A/B-Bereiche und Membran- beziehungsweise Kontaktgeometrien sind dabei Modellannahmen, deren Zusammenhang
weiter geklärt wird.

Im Mittelpunkt stehen positive Energiebilanzen, die Rückwirkung zwischen den beteiligten Bereichen
und die Bedingungen für gebundene, stabile Konfigurationen. Die Verbindung der Teilmodelle zu einem
gemeinsam geprüften Gesamtmodell bleibt eine offene Forschungsaufgabe.

Der räumliche Vergleich behandelt Fragestellungen in einer, zwei und drei Dimensionen. Raumdimension,
Feldkomponenten und innere Symmetrien werden getrennt ausgewiesen; Ergebnisse eines Modells gelten
nicht automatisch in einer anderen Dimension.

Mathematische Ableitungen, numerische Prüfungen und formale Nachweise werden separat dokumentiert.
Für die aktuellen Kontaktableitungen steht die formale Bestätigung durch Lean weiterhin aus.
Die bisherigen Modellrechnungen begründen keine experimentell bestätigte Theorie und keine Herleitung
von Elementarteilchen oder Atomen.

GitHub dient als kuratierte Übersicht mit ausgewählten reproduzierbaren Ergebnissen. Laufende Modelle,
Reviews und Notebooks werden im internen Forgejo geführt. Neue Ergebnisse erhalten vor einer öffentlichen
Übernahme eine gesonderte Prüfung und Freigabe. Bereits veröffentlichte Ergebnisdokumente bleiben
mit ihrem ursprünglichen Datum und Geltungsbereich erhalten.

**Nachtrag 29. Oktober 2026 (nach gesonderter Prüfung freigegeben).** Der Q-Ball-Preprint 0.51
(*Radiative cancellations and localized linear modes in three-dimensional sextic Q-balls*, Finn Hinrichsen; ein
Kontinuumsmodell, keine Rechnung auf dem Netz) ist als Release
[qball-bic-v0.51](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.51) mit Quellen in
[model-lab/papers/qball-bic-ladder-v0.51/](model-lab/papers/qball-bic-ladder-v0.51/README.md) veröffentlicht: drei
computergestützte Existenzeinschlüsse linearer Moden, alles Weitere numerisch oder bedingt, nicht begutachtet.
Aktuelle Fassung ist der Preprint 0.52 vom selben Tag (Release
[qball-bic-v0.52](https://github.com/fmhc/physics/releases/tag/qball-bic-v0.52), Quellen in
[model-lab/papers/qball-bic-ladder-v0.52/](model-lab/papers/qball-bic-ladder-v0.52/README.md)): neu sind eine Widmung,
ein allgemeinverständlicher Überblick und eine Übersichtsabbildung; Ergebnisse und Zahlen sind unverändert.
Seit dem 28. Oktober rechnen wir zuerst die reine SU(3)-Eichtheorie (nur Gluonen) auf dem Netz BCC-r\* × Z; Universalität
und Kontinuumsexistenz sind dabei Setzungen, Confinement ist offen. Erste Skalen- und Topologiebefunde, ihre Fehlschläge
und Grenzen stehen im [Stand vom 29.10.](STAND-UND-NAECHSTE-SCHRITTE.md) und in
[RESULTS](RESULTS.md#status-29-oct-2026), Abbildungen in [assets/stand-20261029/](assets/stand-20261029/README.md).

- [Aktueller Stand und nächste Schritte](STAND-UND-NAECHSTE-SCHRITTE.md)
- [Historische Ergebnisse mit Methoden und Grenzen](RESULTS.md)
- [Ausgewählte Reproduktionspakete](REPRODUCIBILITY.md)
- [Beteiligte und KI-Unterstützung](BETEILIGTE.md)
- [Bewusste Ausschlüsse des öffentlichen Archivs](AUSSCHLUESSE.md)

Texte, Abbildungen und eigene Daten: [CC BY 4.0](LICENSE). Code: [Apache-2.0](LICENSE-CODE).
Hinweise zur Namensnennung stehen in [NOTICE](NOTICE). Ausnahme: Der Q-Ball-Preprint (Fassungen 0.51 und 0.52) und sein Begleitarchiv
stehen für Text, Abbildungen, Daten und Zertifikate unter CC BY 4.0 und für Code unter der MIT-Lizenz.
