# Runde 2: Gegenargumente, Gegenbeispiele und Korrekturen

Alle zehn Ansätze aus [Runde 1](RUNDE-1.md) wurden erneut geprüft. Dies ist eine zweite analytische Bearbeitungsrunde derselben Sitzung, kein unabhängiges Peer Review. Die hergeleiteten Formeln stehen in [Analytische Bausteine](ANALYTISCHE-BAUSTEINE.md); die Math-Übertragungsprüfung in [OpenAI-Math](OPENAI-MATH.md).

## 01 – Attraktion trägt; lokale Ersetzung wird eingeschränkt

Die quadratische Elimination ergibt ΔE=−<J,K^−1 J>/2 mit K=−Δ+M_H². Das negative Vorzeichen stützt die Idee, zusätzliche Bindung als berechenbare Higgsrückwirkung zu verstehen. Ein universelles lokales Kontaktpotential folgt aber nicht: räumliche Variation und nichtlineare Antwort zählen. Bei B13 mit rund 25 % Kernabsenkung ist die lineare Näherung nicht automatisch klein.

**Revision:** Drei Beschreibungen vergleichen: vollständig dynamisches bzw. stationär mitgelöstes y, statische nichtlokale lineare Antwort, lokale Näherung. Die exakte lokale Minimierung hat zudem einen Zweigwechsel bei S_c. Dessen Auftreten ist ein Warnsignal für die Näherung, kein schon bewiesener Beutel.

## 02 – Übertragung trägt; positive Kanten allein sind nicht die Lösung

Einfach positive Kantengewichte einzusetzen kann die Wirkung verändern. Auf schiefen Tetraedern muss nicht jeder einzelne offdiagonale Matrixeintrag das Vorzeichen eines kartesischen Stencils besitzen. Entscheidend ist die gesamte quadratische Energieform. Für lineare finite Elemente ist K_ij=Σ_T∫_T∇N_i·∇N_j positiv semidefinit, auch wenn eine naive Interpretation jeder Kante problematisch ist.

**Revision:** Positive Massenmatrix M und konsistent assemblierte Steifigkeitsmatrix K festlegen. Potentialquadratur und ihre Ableitung identisch verwenden. Nicht nur Radien vergleichen: zuerst gemeinsame globale U(1), freie Dispersion, Energiebilanz und dieselbe dimensionslose Masse prüfen. Dynamische Regge-Geometrie bleibt ein späterer Schritt.

## 03 – Relative Phase ist keine voreilige Erklärung für Zerfall

Der Mischterm liefert bei eta>0 und gleichen Amplituden eine **positive** quadratische Energie für eine kleine relative Phasenverschiebung. Damit fällt die einfache Vermutung „die übersehene Phase ist instabil“ weg. Dennoch wurden nicht alle komplexen und nicht-radialen Störungen durch reelle Starts geprüft.

**Revision:** Nicht nach einer vorgegebenen Instabilität suchen, sondern den vollständigen eingeschränkten Energieoperator und den dynamischen Hamiltonoperator unterscheiden. Die erwartete gemeinsame Phasennullmode darf nicht als Fehler gelten. Ein negativer Modus oder positiver Realteil einer dynamischen Rate wäre ein Gegenbefund; kein solcher wurde hier numerisch bestimmt.

## 04 – Ein Kern ist kein isolierter stationärer Q-Ball

Q(<r) verändert sich durch Fluss. Eine Kernladung nahe einem stationären Schwellenwert identifiziert deshalb keinen Q-Ball dieses Zweiges. Ebenso hat ein konservatives endliches periodisches System keinen generell anziehenden dissipativen Attraktor. Minimiererrelaxation und freie Zeitentwicklung dürfen nicht vermischt werden.

**Revision:** Von einem „stationären Lösungszweig plus Strahlungsrest“ sprechen. Globale Phase und Lage beim Profilvergleich anpassen, aber danach Restenergie, Restladung und äußere Flüsse separat bilanzieren. Alte B23-Nullkriterien bleiben gültig. Ein längerer Lauf allein wäre keine neue Erklärung; zuerst muss eine trennende Diagnose feststehen.

## 05 – Neue Bindung kann die bestehende Massenschranke nicht wegreden

Aus V≥delta*S folgt E≥sqrt(delta)|Q|. Kleinere Größe, Rotation oder zusätzliche gleichnamig geladene Unterobjekte heben die Aussage nicht auf. Auch eine attraktive effektive Higgskopplung ist kein Gegenbeispiel, solange sie aus dem unveränderten positiven Vollmodell stammt.

**Revision:** Jede Erweiterung muss genau sagen, welche Voraussetzung sich ändert: Potentialuntergrenze, Normierung, Feldinhalt oder Ladungszuordnung. Die Schranke gilt nicht automatisch für neu erfundene Wirkungen; ihr Wegfall beweist umgekehrt keine leichte stabile Materie. Formalisierung zuerst für kleine algebraische Lemmata, nicht als pauschaler „Physikbeweis“.

## 06 – Gleicher Zielraum ist noch kein topologischer Schutz

Ein normalisierter Singulett-Doppelpack kann lokal wie ein S³-Feld aussehen, ist bei verschwindender Gesamtdichte aber nicht definiert. Seine Orientierung ist durch die bestehende Wirkung außerdem nicht frei SU(2)-symmetrisch. Ein Skyrmion lässt sich deshalb nicht ohne weitere Annahmen aus jedem Q-Ball herauslesen.

**Revision:** U als separates Feld führen. Die Kopplung darf die stabilisierenden Koeffizienten nicht auf null treiben, sonst kann die Energiebarriere verschwinden. Eine mögliche Modellwahl sind glatte, streng positiv beschränkte c2(y), c4(y). Erst den entkoppelten Grad-1-Kontrollfall, danach Rückwirkung prüfen. Spin/Statistik und Eichbaryonenzahl bleiben offen.

## 07 – Neutralität beseitigt eine Schranke, nicht die Energie

Bei Q_total=0 sagt die Ladungsschranke nur E≥0. Das Vakuum ist zulässig, und der vorhandene Fest-Q-Minimierer kann die gewünschte zeitabhängige Gegenladungsstruktur gar nicht erzwingen. Ein behaupteter statischer „neutraler Q-Ball aus Plus und Minus“ wäre damit falsch begründet.

**Revision:** Nur als dynamische Resonanz-/Oszillonfrage weiterführen. Anfangsdaten müssen entgegengesetzte lokale Noetherladungen besitzen; Komponentenbezeichnungen allein reichen nicht, da die Mischung nur Gesamt-Q erhält. Erforderlich wäre eine Lebensdauer gegenüber kontrollierter freier Ausbreitung, keine bloße Momentaufnahme eines kompakten Kerns.

## 08 – Endlich viele Antworten können Parameter entarten lassen

Der gelesene Rekonstruktionssatz setzt sämtliche Randdaten und glatte Kontinuumsgeometrie voraus. Unsere periodische Box hat nicht einmal denselben Randversuch. Die Lean-Formalisation der Familie betrifft einen anderen, nicht-eindeutigen Leitfähigkeitsfall.

**Revision:** Eigener endlicher Pilot: Parameter theta=(Geometrieverzerrung, g, eta) und eine klar definierte Antwortmatrix. Die Sensitivität J_ab=∂O_a/∂theta_b auf Rang nach Herausnahme von Symmetrierichtungen untersuchen. Rangverlust bedeutet „mit diesen Observablen nicht trennbar“, nicht „zwei Naturgesetze identisch“. Ein kleiner singulärer Wert relativ zum Fehlerbudget zählt als praktische Entartung.

## 09 – Aus zwei Singuletts entsteht nicht automatisch schwaches SU(2)

Die vorhandene Wirkung enthält explizite innere Anisotropie und eta-Mischung. Schon diese algebraische Prüfung widerlegt den direkten Schluss auf ein SU(2)-Dublett. Eine globale Ordnungsrichtung liefert zudem keine lokale Eichredundanz und keine chirale Kopplung an Fermionen.

**Revision:** Zwei getrennte neue Modelle erwägen: (a) bewusst symmetrisierter globaler Orientierungssektor als Kontrollmodell, (b) ausdrücklich eingeführtes Eichdublett mit kovarianter Dynamik. Das zweite wäre eine Erweiterung, keine Herleitung. Der Heisenberg-Satz kann in keinem der beiden Fälle ohne neue Abbildung als Existenzbeweis dienen. Direkte schwache-Standardmodell-Deutung zurückstellen.

## 10 – Formfaktoren brauchen denselben Zustandsbegriff

Ein Normradius ist kein elektrischer Radius, ein Druckprofil noch kein Nukleon-D-Formfaktor. Stress-Verbesserungsterme und die Definition des Energie-Impuls-Tensors beeinflussen die Zuordnung. Die vorhandene kartesische Impulsbilanz besitzt Gitterreste; diese sind keine zusätzliche Wechselwirkung.

**Revision:** Zunächst modellinterne, dimensionslose Observablen mit derselben Definition vergleichen. E/Q allein wird durch mindestens eine nicht angepasste Antwortgröße ergänzt. Erst nach Identifikation der Zustände und Quantenzahlen ist ein Hadronvergleich zulässig. Die Literatur motiviert die Auswahl unabhängiger Größen, ersetzt aber die fehlende Zustandsabbildung nicht.

## Ergebnis dieser Runde

01–05, 08 und 10 werden als direkte Analyse-/Methodenanschlüsse geschärft. 06 bleibt ein explizit neues topologisches Modell. 07 bleibt eine riskantere Dynamikhypothese. 09 wird von einer vermeintlichen SU(2)-Herleitung auf zwei sauber benannte Erweiterungen zurückgestuft. Keine Idee wurde durch eine neue Simulation bestätigt.

Weiter: [Runde 3 – konkrete Entscheidungstests und Priorität](RUNDE-3.md).
