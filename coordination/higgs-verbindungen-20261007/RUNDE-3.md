# Runde 3: zehn weiterentwickelte Ideen mit Entscheidungstests

Diese Runde übernimmt die Gegenargumente aus [Runde 2](RUNDE-2.md). Status aller numerischen Vorschläge: **geplant, nicht ausgeführt**. Vor einem Lauf sind Code/Inputs, Messgrößen, Fehlerbudget, Laufzeit und gemeinsame Ressourcen zu binden. Bestehende Arbeit anderer Prozesse zuerst abgleichen. Keine automatische Wiederholung von B13–B23.

Priorität A: unmittelbar aus vorhandener Wirkung/Archiven prüfbar. B: eigene kleine Implementierung oder neues Vergleichsmodell nötig. C: erhebliche Zusatzannahmen; vorerst analytisch. Die Prioritäten sind Arbeitsentscheidungen, keine Erfolgswahrscheinlichkeiten.

## 01 – HIGGS-RESPONSE: Vermittlung aus der Wirkung ableiten · A

**Endfassung:** Die räumliche Higgsantwort als berechenbaren Beitrag zur Bindung behandeln. Drei Modelle desselben Parametersatzes vergleichen: mitgelöstes y, statische Green-Operator-Antwort und lokale Potentialelimination. Die Formeln aus [Bausteinen B/C](ANALYTISCHE-BAUSTEINE.md) legen Vorzeichen und Näherungsgrenzen fest.

**Kleinster Test:** Zuerst vorhandene B13-Profile einschließlich Randbedingungen lokalisieren. Auf denselben Singulettprofilen die verschiedenen Higgsantworten vergleichen; Profilnorm, Energieänderung und Residuum der vollständigen Higgsgleichung getrennt berichten. Nicht zuerst jeden Ansatz neu minimieren, weil sich dann Näherungsfehler und Profiländerung vermischen. Ein späterer Kopplungsgrenzfall g→0 muss zur linearen Antwort konvergieren.

**Entscheidung:** Nur wenn Fehler unter einer vorab gesetzten, für das Bindungssignal ausreichenden Toleranz liegen, die reduzierte Beschreibung für Parameterideen verwenden. Andernfalls volles y behalten. Der 25-%-Fall wird nicht durch bloße Plausibilität freigegeben.

**Erkenntnisgewinn:** Portalstärke und Reichweite einer effektiven Wechselwirkung werden verbunden. Keine neue Fundamentalkraft und keine Herleitung des Higgsparameters. In 1D/2D/3D jeweils den passenden Green-Operator verwenden; Start bleibt 3D.

## 02 – PORTAL-AUF-V: Materie und Netz mit derselben Energie verbinden · B

**Endfassung:** Ein statischer Tetraederadapter erhält positive Massenmatrix M, konsistente Steifigkeitsmatrix K und das unveränderte Portalpotential. Für komplexe Felder gilt diskret Q=2 Im(psi† M dot psi), mit Summe über die Komponenten. Ein gemischter Einsatz verschiedener Volumenmaße ist ausgeschlossen.

**Kleinster Test:** Einfache periodische Kontrolltriangulierung vor V. Konstantes Vakuum, massive freie Mode und gemeinsame U(1)-Drehung müssen die analytischen Kontrollen erfüllen. Energieableitung und Kraft unabhängig vergleichen. Danach ein bereits vorhandenes lokalisiertes Profil auf beiden Geometrien bei gleicher physikalischer Box, Parametern und Ladung prüfen.

**Entscheidung:** Bei verletzter Energie-/Ladungsstruktur stoppt die Übertragung. Geometrieeffekte erst behaupten, wenn sie gegenüber Verfeinerungs- und Interpolationsfehlern bestehen. Keine Anpassung von Kopplungen nur für das Netz, um einen Vergleichspunkt passend zu machen.

**Erkenntnisgewinn:** Direkte Brücke zwischen B13 und V. Zunächst feste 3D-Geometrie; eine dynamische 3+1-D-Geometriekopplung ist eine spätere, eigene Wirkung.

## 03 – FULL-MODES: vollständiges Anregungsspektrum · A

**Endfassung:** Für den bestehenden Q250-Kandidaten alle Amplituden-, relativen Phasen-, Higgs- und nicht-radialen Störungen zulassen. Eingeschränkte Energiekrümmung und dynamische Wachstumsraten werden getrennt behandelt.

**Kleinster Test:** Vorhandenes stationäres Profil mit nachprüfbarem Residuum auswählen. Den linearen Operator im mitrotierenden Rahmen ableiten. Gemeinsame Phasennullmode und Translationsrichtungen als Kontrollen benutzen. Erst eine kleine Zahl der niedrigsten relevanten Moden bestimmen; bei einem radialen Profil verschiedene Winkelkanäle berücksichtigen. Eine radiale Vorprüfung kann Instabilität finden, aber nicht alle 3D-Instabilitäten ausschließen.

**Entscheidung:** Ein unter Verfeinerung stabiler negativer eingeschränkter Modus oder ein positiver Realteil einer dynamischen Rate führt zu einem gezielten Störungslauf. Numerisch nahezu null bleibt unentschieden. Ein unauffälliges Teilspektrum ist kein globaler Stabilitätsbeweis.

**Erkenntnisgewinn:** Prüft den bisher fehlenden Anschluss von gebundener Energie an Lebensdauer. M3 aus dem Math-Release liefert keinen Ersatz für diesen massiven gekoppelten Operator.

## 04 – FORMATION-MAP: Bildung von Startanpassung unterscheiden · A

**Endfassung:** Die B23-Dynamik wird als mögliche Kombination aus zeitabhängigem Kern, stationärem Vergleichsprofil und auslaufendem Rest untersucht. Keine Umetikettierung einer Radiusladung als isoliertes Teilchen.

**Kleinster Test:** Prüfen, ob archivierte komplexe Felder und Impulse vorhanden sind. Reine Dichtebilder reichen für Phasen-/Modenprojektion nicht. Falls vorhanden: Translation und globale Phase abgleichen, anschließend feld- und impulsgewichteten Rest sowie regionale E/Q-Flüsse über mehrere feste Zeitfenster auswerten. Falls nicht vorhanden: die fehlende Information dokumentieren; einen neuen Diagnose-Lauf erst gesondert planen.

**Entscheidung:** Wiederkehrende Atmung mit stabilen Bilanzgrößen, monotone Leckage und bloße Anfangsanpassung sind konkurrierende Ausgänge. Kein besonders günstiger Endzeitpunkt wird ausgewählt. Die bestehenden verfehlten B22/B23-Kriterien bleiben unverändert.

**Erkenntnisgewinn:** Liefert einen Mechanismus für Erfolg oder Scheitern von Bildung. Ein späterer Vergleich abgeglichener Gesamt-E/Q-Anfangsfamilien muss prüfen, ob dieser Abgleich überhaupt lösbar ist; zusätzliche eingebrachte Wellenenergie wird offengelegt. 3D-Hauptfrage, radial nur vorgeschalteter Filter.

## 05 – BOUND-CERT: neue Modelle an expliziten Schranken prüfen · A

**Endfassung:** Ein kleiner Satzkatalog bindet Annahmen und Folgerungen: lokale Higgsminimierung, Vakuumuntergrenze, E/Q-Schranke, Fest-Q-Virialidentität. Die hier vorhandenen Papierableitungen werden in [Bausteinen B–E](ANALYTISCHE-BAUSTEINE.md) festgehalten.

**Kleinster Test:** Eine formale Aufgabe zunächst rein algebraisch: Für a>0 und z≥0 das zweigweise Minimum aus B beweisen. Danach die endliche diskrete Ladungsungleichung mit positiven Quadraturgewichten. Physikalische Parameterumrechnung und Kontinuumsexistenz nicht im selben Schritt verstecken.

**Entscheidung:** Ein Formalisierungsartefakt zählt erst nach tatsächlicher Prüfung und Audit der angenommenen Sätze. Für jede neue Wirkung eine Tabelle „Voraussetzung erhalten/verletzt/offen“. Beim Verlust einer Untergrenze nach Vakuuminstabilität suchen, bevor eine niedrige Teilchenmasse als Erfolg gilt.

**Erkenntnisgewinn:** Beschleunigt Modellausschluss ohne große Parameterläufe. M4 ist der methodische Anschluss. Die algebraische Energieungleichung ist dimensionsunabhängig; physikalische Normierung und Virialidentität sind dimensionsabhängig.

## 06 – SKYRME-PORTAL: Topologie und Higgsrückwirkung · B, nach 02/05

**Endfassung:** Neues separates SU(2)-Zielfeld U mit gewöhnlichen positiven Zweiderivativ- und Skyrme-Energieanteilen. Beispiel einer ausdrücklich gewählten, nicht hergeleiteten Kopplung:

```text
c_j(y) = c_j0 * [1 + epsilon_j*tanh((y²−y0²)/y0²)],
c_j0>0, |epsilon_j|<1, j=2,4.
```

So bleiben beide Koeffizienten von null getrennt. Das garantiert noch keine stabile Lösung des gesamten diskreten Modells.

**Kleinster Test:** Zuerst Grad-1-Kontrollfall bei epsilon=0 mit validiertem Topologiezähler. Dann die führende Parameterableitung der stationären Energie bei epsilon=0 als Vorhersage formulieren und später gegen eine kleine Kopplungsänderung prüfen. Volumen-/Auflösungsänderungen und Rückwirkung von y getrennt verfolgen.

**Entscheidung:** Unklarer Grad oder Entwinden durch Diskretisierung stoppt die Interpretation. Ein beobachteter Radius-/Energieeffekt rechtfertigt ein hybrides Solitonenmodell, noch keinen Baryonenstatus. Quantisierung, Spin 1/2 und elektrische Ladung bleiben zusätzliche Aufgaben. Die relevante räumliche Windungszahl ist hier 3D; 2D-Baby-Skyrmionen wären andere Modelle.

## 07 – NEUTRAL-RESONANCE: Gegenladung als eigene Dynamikfrage · C

**Endfassung:** Ein echter +Q/−Q-Start wird auf endliche Lebensdauer und charakteristische Frequenzen geprüft, nicht mit dem Q=0-Minimierer gesucht. Die globalen Ladungen können sich aufheben; räumliche Energie und Anregungen bleiben.

**Kleinster Test:** Zunächst aus der vorhandenen Wirkung offene lineare Strahlungskanäle und Symmetriesektoren bestimmen. Anfangsfelder und Impulse müssen die gewünschten lokalen Ladungsvorzeichen tatsächlich liefern. Ein möglicher numerischer Pilot vergleicht gleiche Startgeometrie im vollen und im passenden freien Modell; verschiedene Energien werden ausgewiesen.

**Entscheidung:** Ohne eine Lebensdauer deutlich jenseits der freien Dispersionszeit und ohne Randkontrolle bleibt es eine Überlagerung. Ein langer, aber endlicher Zustand wäre eine Resonanz, kein Beweis absoluter Stabilität. Kein Proton-/Mesonlabel ohne passende Quantenzahlen.

**Erkenntnisgewinn:** Andere Objektklasse jenseits des gleichnamig geladenen Q-Ball-Zweiges. Die 1D/2D-Lebensdauer ist kein 3D-Nachweis; zuerst analytischer Ausschlussfilter, dann gegebenenfalls 3D.

## 08 – RESPONSE-TOMOGRAPHY: Geometrie gegen Materiekopplung testen · B

**Endfassung:** Eine kleine endliche Messmatrix unterscheidet geometrische Verzerrung und Portal-/Mischparameter. M1 motiviert die Frage; sein Kontinuumssatz wird nicht angewandt.

**Kleinster Test:** Geometrieverzerrung, g und eta zunächst mit höchstens drei freien Richtungen parametrisieren. Mindestens drei unabhängige, symmetrieberücksichtigte Antworten wählen, z.B. räumliche Richtungsdispersion, statische Higgsantwort und Modenaufspaltung. Vor Simulation klären, welche Antworten überhaupt auf welchen Parameter reagieren: Im leeren Vakuum S=0 ist eine Portalantwort auf g unter Umständen blind.

**Entscheidung:** Skalierte Sensitivitätsmatrix samt Fehlern untersuchen. Rangverlust oder zu kleine singuläre Werte verlangen eine andere Anregung; sie werden nicht durch Sortieren von Eigenwerten verborgen. Auf periodischen Boxen interne Quellen verwenden oder einen eigenen Randversuch definieren, keine fiktiven Randdaten annehmen.

**Erkenntnisgewinn:** Ein nachvollziehbarer Test der Idee „Geometrie erzeugt scheinbare Massenstruktur“. Fester 3D-Kontrollfall; die drei Parameter sind keine drei Teilchenfamilien.

## 09 – CURVATURE-ORDER: klar benannte Erweiterung statt verstecktem SU(2) · C

**Endfassung:** Die direkte SU(2)-Deutung der zwei Singuletts wird verworfen. Als neue Verbindung zur Geometrie bleibt ein separat eingeführtes Higgsdublett H mit einer Kopplung xi*R*H†H. Für vorgegebenes konstantes R und λ_H>0 liefert die Modellwahl

```text
V_H = λ_H (X−v²/2)² + xi*R*X,   X=H†H≥0,
X_* = max(0, v²/2 − xi*R/(2λ_H)).
```

Das ist eine bedingte algebraische Verschiebung des Minimums, keine Berechnung unseres V-Netzes und keine Herleitung des gegebenen v.

**Kleinster Test:** Wirkung samt Geometrienormierung, Randtermen und Rückwirkung definieren. Zuerst fragen, ob ein relevanter gemittelter Krümmungswert im gewünschten Hintergrund überhaupt entsteht; anschließend das gekoppelte Vakuum und die positiv normierten Fluktuationen bestimmen. Ein extern eingesetztes R darf nicht als dynamisch erzeugt bezeichnet werden.

**Entscheidung:** Ohne stabile selbstkonsistente Hintergrundlösung und kontrollierte Skalen bleibt es eine Hypothese. SU(2)L×U(1), Eichfelder, Fermionen und Anomalien wären ausdrücklich zusätzliche Struktur. M2 motiviert nur sorgfältige Zustands-/Grenzwertdefinitionen. Der Krümmungsterm benötigt eine 3+1-D-Wirkung; ein 3D-Spinmodell beweist ihn nicht.

## 10 – MULTI-OBSERVABLE: Modelle an einer zurückgehaltenen Größe trennen · A

**Endfassung:** Vergleiche vorhandenes Portalmodell, seine kontrollierte Reduktion und später das topologische Hybridmodell mit denselben modellinternen Größen. Kandidaten: E/Q, Normradius, relative Higgsantwort, eine nichttriviale Stressobservable und niedrigste physikalische Anregungsfrequenz.

**Kleinster Test:** Zunächst nur ein oder zwei freie Parameter zulassen. Eine Größe zur Anpassung verwenden, eine andere vor der Anpassung als Vorhersage festlegen. Bei Spannungsmomenten den Energie-Impuls-Tensor samt Verbesserungsfreiheit und Randbedingungen definieren; Diskretisierungsreste schätzen. Sensitivitäts-/Rangprüfung aus 08 schützt vor mehrfach gezählter Information.

**Entscheidung:** Liegen Vorhersageunterschiede unter Fehlern, ist die Messgröße nicht diskriminierend. Ein Unterschied zwischen Modellkurven ist noch kein experimenteller Erfolg. Die Hadronliteratur motiviert unabhängige Größen; ohne Zustandsabbildung nennen wir einen Q-Ball-Spannungsmoment nicht Nukleon-D-Formfaktor.

**Erkenntnisgewinn:** Auswahl nach Vorhersagekraft statt passender Bilder. Erste Auswertung nutzt vorhandene 3D-Daten; 1D/2D-Vergleiche nur bei getrennt festgelegten Normierungen.

## Reihenfolge, die unnötige Rechnungen vermeidet

1. **05 und 01:** Papierableitungen sind in diesem Paket vorhanden; als Nächstes kleine Formalisierungs-/Archivprüfungen.
2. **03 und 04:** Spektrum bzw. vorhandene Zeitdaten klären den zentralen Unterschied zwischen Existenz und Bildung.
3. **02 und 10:** Erst ein kontrollierter Netzanschluss, dann vergleichbare Vorhersagen.
4. **08:** Bei messbarer Parameterentartung gezielt die nächste Antwort auswählen.
5. **06:** Neues topologisches Hybridmodell erst nach bestandener Grundkontrolle.
6. **07 und 09:** Analytisch interessant, aber derzeit die meisten offenen Voraussetzungen.

Keine zusätzliche Rechenfreigabe wird hier fingiert. Ein numerischer Folgeauftrag muss einen konkreten Vorabplan besitzen; die vorhandene Projektfreigabe für Arbeit und Veröffentlichung bleibt davon unberührt. Es wurden keine neuen Hintergrundjobs, APIs oder Lean-Builds gestartet.
