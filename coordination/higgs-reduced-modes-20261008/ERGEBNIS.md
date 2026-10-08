# HIGGS-REDUCED-MODES-1: reduzierte Modelle bewahren radiale Energiekrümmungen

08.10.2026 · [E] neue CUDA-Hessianrechnung, Anschluss an [HIGGS-MODES-1](../higgs-modes-20261008/ERGEBNIS.md).

**E3 und Ecomp bestehen den vorab festgelegten radialen Spektralvergleich.** Der maximale relative Fehler der geprüften nichttrivialen Energiekrümmungen beträgt **0,009883 % für E3** und **0,0002517 % für Ecomp**. Beide Näherungen erhalten die gemeinsame Phasen-Nullrichtung und positive übrige Krümmungen.

![Radiale Energiekrümmungen reduzierter Modelle im Vergleich](reduced-mode-errors.svg)

Verglichen wird mit der vollen Theorie, deren Higgsfeld statisch auf eine Materiestörung reagieren darf. Das ist ein anderer Vergleich als das vollständige gekoppelte Spektrum im vorherigen Bericht. Die Aussage gilt ausschließlich für **radiale Störungen (l=0)** des ausgewählten Portalzweigs.

## Was gerechnet wurde

Drei Modelle: volle statische Referenz, E3 und Ecomp. Jeweils die eigenen stationären seed=0-Profile aus HIGGS-MINIMA-1, mit eta=0,05, g=0,005, c8=0 und Q=600. Drei Radialgitter (Basis, fein, größere Box), jeweils reelle Amplituden und imaginäre Phasen: **18 Eigenwertmatrizen**. Keine erneute Relaxation, keine Fits.

Der reelle Sektor enthält beide Materieamplituden und damit auch ihre gegensinnige Änderung. Im imaginären Sektor werden gemeinsame und relative Phasen unterschieden. Die Normierung bleibt radialer 3D-Raum, nicht räumlich 1D. Keine Winkelordnungen l>0 wurden für die reduzierten Energien gerechnet.

Pro Modellvergleich wurden die acht niedrigsten reellen und sieben niedrigsten nichttrivialen imaginären Eigenwerte nach Größe zugeordnet. Die gemeinsame Phase wird separat geprüft und aus dem relativen Fehlervergleich entfernt, weil Division durch einen Nullwert keine sinnvolle Fehlergröße ergibt.

| Vergleichsgröße | E3 | Ecomp |
|---|---:|---:|
| Maximaler relativer Eigenwertfehler | 0,009883 % | 0,0002517 % |
| Beobachteter Fehlerdrift zwischen Gitter/Box | 0,002496 Prozentpunkte | 0,0001350 Prozentpunkte |
| Kleinster quadrierter Eigenvektorüberlapp | 0,9999999442 | 0,999999999941 |
| Größte relative Frobeniusabweichung der Matrizen | 5,55e-7 | 4,41e-9 |
| Gemeinsame Phase korrekt identifiziert | ja, alle drei Stufen | ja, alle drei Stufen |
| Nichttriviale Eigenwerte positiv | ja | ja |
| Vorabkriterium einschließlich Drift | bestanden | bestanden |

Der Vorabgrenzwert war maximal 5 % Fehler einschließlich Drift, mit Drift höchstens 0,5 Prozentpunkte. Es wurden keine Kriterien nach Ergebnisansicht geändert. Alle Zahlen beziehen sich auf die drei endlichen Diskretisierungen. Die Grafik zeigt das feine Gitter mit der beobachteten Gitter-/Boxspanne, keine statistischen Unsicherheiten. Die Frobeniusnorm wird durch große kurzwellige Matrixeinträge mitbestimmt; sie ist nur eine ergänzende Diagnose, kein Ersatz für den Vergleich der niedrigen Eigenwerte.

## Weshalb die volle Referenz ein Schur-Komplement benötigt

[M] In normierten Variablen zerfällt der reelle Fix-Q-Energiehessian der vollen Theorie in Materie und Higgs:

```
H = [ A   B  ]
    [ Bᵀ  C  ]
```

Für eine vorgegebene kleine Materieänderung du minimiert die statische Higgsänderung die quadratische Energie bei `dz=-C^-1 Bᵀ du`, sofern C positiv ist. Einsetzen ergibt den effektiven Materieoperator:

```
S_full = A - B C^-1 Bᵀ.
```

[E] C ist auf allen drei Stufen positiv; sein kleinster gemessener Eigenwert beträgt **4,714586**. Die Lösung des linearen Systems erfolgt mittels Cholesky-Zerlegung. Im imaginären Sektor koppelt das Higgsfeld am reellen Hintergrund in zweiter Ordnung nicht linear an die Phasenstörung; dort ist kein solches Eliminieren nötig.

Die reduzierten Amplitudenhessians wurden direkt aus der **vollständigen zweiten Ableitung von E3 beziehungsweise Ecomp** berechnet. Insbesondere sind alle Kettenregelbeiträge der dichteabhängigen Higgsantwort enthalten. Der Phasenoperator folgt aus der ersten Ableitung der Higgsenergie nach der Gesamtdichte; er wurde gegen unabhängige Gradientendifferenzen der komplex erweiterten Energie geprüft.

Die Vergleichsoperatoren stehen auf den jeweils eigenen stationären Profilen. Die Abweichungen enthalten deshalb sowohl den Näherungsfehler der Energie als auch die kleine Profilverschiebung durch erneute Selbstkonsistenz im früheren Lauf.

**Das Schur-Komplement beschreibt eine statische Antwort.** Ein zeitabhängiges Higgsfeld besitzt Trägheit; dessen Eliminierung führt im Allgemeinen zu einer frequenzabhängigen Antwort. Die hier ausgewiesenen Eigenwerte sind daher weder die Eigenwerte des vollständigen gekoppelten Hessians noch dynamische Frequenzquadrate. Keine neue Teilchenmasse wird aus ihnen abgeleitet.

## Nullrichtung und numerische Prüfung

Die gemeinsame Phasendrehung wird bei allen neun Modell-/Gitterkombinationen mit quadriertem Überlapp größer als 0,99999999999998 erkannt. Ihre Eigenwerte liegen betragsmäßig unter **1,16e-8**. Zwei dieser kleinen Werte sind negativ (E3 fein, Ecomp größere Box); sie bleiben ausdrücklich in den Rohdaten und erfüllen die vorab gesetzte Nullrichtungsgrenze 1e-6. Sie werden nicht als negative physikalische Störrichtung ausgegeben. Die endliche Stationaritätsgenauigkeit begrenzt insbesondere die letzten Stellen der kleinsten Fehlerangaben.

Alle vorgelagerten QA-Kriterien bestanden:

- Rohhessians vor numerischer Symmetrisierung: größte absolute Asymmetrie **4,45e-16**.
- Unabhängige zentrale Differenzen des Energiegradienten, Schritte 0,001; 0,0005; 0,00025, in einer vorab festgelegten glatten Richtung: größter relativer Fehler beim kleinsten Schritt **3,26e-7**. Beide reduzierten Modelle und beide Sektoren auf allen Gittern geprüft; vollständige Folgen gespeichert.
- Schur-Systemlösung: größtes relatives Residuum **7,73e-15**.
- Acht niedrigste Eigenpaare: größtes absolutes Residuum **1,40e-11**, Orthogonalitätsfehler **3,39e-15**.

CUDA float64 auf Quadro P5000 mit Torch 2.5.1+cu121 und cuSOLVER. Rechenlauf rund **11,59 s**, begrenzter Dienst einschließlich Start **14,406 s**. Gemeldeter maximaler Tensor-Speicher rund 284 MB, ohne CUDA-Kontext. CPU nur für Steuerung, IO, skalare Tabellen und Matplotlib. Gemeinsamer GPU-Lock und anschließend freigegebene Pacht; keine anderen Dienste geändert. Diese Zahlen sind kein kontrollierter Geschwindigkeitsvergleich der Modelle.

## Einordnung für die Verbindungsideen

Idee 1 (reduzierte Higgsrückwirkung) und Idee 3 (Störrichtungen) greifen nun **im statischen radialen Pilot** ineinander: Nicht nur Profile, Energie und Kräfte stimmen gut überein; auch die niedrigen Krümmungen der Energie und die gemeinsame Phasensymmetrie bleiben erhalten. Ecomp ist in diesem Vergleich genauer als E3. Daraus folgt keine universelle Überlegenheit für andere Parameter oder Zeitentwicklungen.

Die volle Theorie wurde zuvor auch in Winkelordnungen l=1,2,3 untersucht. **Diese Winkelprüfung ist nicht auf E3/Ecomp übertragbar.** Deren nichtlokale Higgsantwort muss bei nicht-radialen Störungen mit dem passenden winkelabhängigen inversen Operator variiert werden. Es reicht nicht, an den fertigen radialen reduzierten Hessian einfach l(l+1)/r² anzuhängen: Auch die eliminierte Antwort verändert sich.

Ein sinnvoller nächster Test ist deshalb die winkelabhängige zweite Variation der reduzierten Energien, zunächst gegen die volle statische Antwort in l=1 und l=2. Die Translationsrichtung bietet dabei eine wichtige Kontrolle. Noch offen bleiben dynamische Frequenzen, endliche Störungen, weitere Parameterpunkte und die gewichteten Operatoren auf V.

Keine elektroschwache Eichstruktur, chirale Materie oder Hadronenidentifikation hinzugefügt. Entwicklungsschätzungen unverändert: Higgs 2 %, schwache Kraft 2 %, Mesonen/Baryonen 10 %.

## Reproduzierbarkeit

[Vorabplan](PLAN.md) · [Rechencode](run.py) · [Auswertung/Grafik](analyse.py) · [Eigenwerte und Phasenüberlappungen](results/RESULT.json) · [Vergleiche mit der vollen Referenz](results/COMPARISONS.json) · [QA](results/QA.json) · [Zusammenfassung/Gates](SUMMARY.json) · [Laufstatus](results/STATUS.json) · [Provenienz](results/PROVENANCE.json) · [Exportanpassung](EXPORT.json).

Eingabe: [HIGGS-MINIMA-1/RESULT.json](../higgs-minima-20261008/results/RESULT.json), SHA256 `a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9`. Für Wiederholungen PLAN.md, run.py und analyse.py in einen frischen Nachbarordner des Eingabeverzeichnisses kopieren; `python run.py` erfordert CUDA, anschließend `python analyse.py`. Ein bestehender results-Ordner wird nicht überschrieben. Im öffentlichen Rechencode wurde nur der Eingabepfad angepasst; Original- und Exporthash sind getrennt vermerkt, keine unnötige Wiederholung wegen des Exports.
