# OpenAI-Math: gelesene Aussagen und tatsächliche Anschlussstellen

Stand 07.10.2026. Arbeitsannahme für den nicht näher benannten Release: [Sharing AI progress in mathematics, 06.10.2026](https://openai.com/index/sharing-ai-progress-in-mathematics/). Die Rückfrage nach einem anderen gemeinten Release bleibt möglich. Repository: [openai/math](https://github.com/openai/math), gelesener HEAD `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

Die Veröffentlichung stellt Manuskripte und unterstützende Beweisartefakte bereit. Die Repository-Einleitung unterscheidet ausdrücklich Prüfstände; nicht jedes Ergebnis ist formalisiert. Der erwähnte interne Erzeuger ist kein hier neu aufgerufenes Werkzeug. Wir haben weder dessen Rechenläufe wiederholt noch eine allgemeine Korrektheitsgarantie übernommen.

## Lesetiefe

Gelesen: Release-Seite, Repository-README, thematisch durchsuchter Katalog/Überblick, die unten angegebenen Hauptaussagen und Voraussetzungen dreier PDF-Manuskripte sowie die zugehörigen verfügbaren Lean-Scope-Seiten und Comparator-Deklarationen. **Keine vollständige Durchprüfung der langen Beweise; keine lokale Lean-/Comparator-Ausführung.** Ein bereitgestelltes Lean-Artefakt wird deshalb als solches bezeichnet, nicht als von uns erfolgreich geprüft.

### M1: Rekonstruktion von Geometrie und Verbindung

[Manuskript, Familie 365, Einführung und Satz 1.1](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf).

Die behauptete Eindeutigkeit betrifft glatte kompakte Mannigfaltigkeiten ab Dimension drei, ein triviales komplexes Rang-zwei-Bündel und sämtliche passenden Randanregungen auf einem offenen Randstück. Rekonstruktion erfolgt nur bis auf die angegebenen Diffeomorphismen und Eichtransformationen. Das ist weder ein Satz über wenige verrauschte Messwerte noch ein numerischer Rekonstruktionsalgorithmus für unser nichtlineares Portalmodell.

**Wichtige Scope-Prüfung:** Der [Lean-Eintrag 365](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/365.md) verweist auf den anderen Familienbeitrag zur **Nicht-Eindeutigkeit beschränkter messbarer Leitfähigkeiten**. Er formalisiert laut dieser Seite nicht den oben genannten glatten Eindeutigkeitssatz. Die [Comparator-Datei](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Conductivity.lean) wurde nur als Deklaration gesichtet.

Eigene Folgerung: Idee 08 bekommt einen endlichen Rang-/Entartungstest mit expliziten Eichfreiheiten. Keine Berufung auf M1 als Beweis der Identifizierbarkeit.

### M2: Kollektive Ordnung mit präzisem Zustandsbegriff

[Manuskript, Familie 271, Abschnitte 1.1–1.3](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf).

Untersucht wird der isotrope nächste-Nachbar-Quantenferromagnet auf Z^d für d≥3 und positive halb-/ganzzahlige Spins. Die Hauptaussage konstruiert bei hinreichend niedriger positiver Temperatur einen magnetisierten unendlichvolumigen Gleichgewichtszustand. Zustandswahl und Grenzwerte sind wesentlich; der Operatorinhalt ist nicht der unserer Skalarfelder.

Der [Lean-Scope 271](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/271.md) nennt spontane Magnetisierung und die zugrunde liegende Dynamikkonvergenz. Dies deckt nicht automatisch sämtliche weiteren Manuskripte der Familie ab. [Comparator-Deklaration](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Heisenberg.lean).

Eigene Folgerung: Idee 09 muss zuerst ihre eigene Symmetrie, Freiheitsgrade und Grenzfolge definieren. Magnetische Ordnung wird nicht mit lokaler Eichsymmetrie oder chiraler schwacher Kraft gleichgesetzt. Übertragung auf 1D/2D erfolgt nicht.

### M3: Wellenabschätzungen als Werkzeug, nicht als Solitonenbeweis

[Manuskript, Familie 079, Satz 1.1 und Einführung](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf).

Die angegebene Abschätzung betrifft die lineare masselose euklidische Halbwelle in drei Raumdimensionen über ein endliches Zeitintervall, mit positiver Sobolev-Verlustpotenz. Sie behauptet weder einen verlustfreien Endpunkt noch Langzeitstabilität unserer massiven gekoppelten Felder. Der Abruf einer Scope-Datei `lean/docs/079.md` ergab 404; daraus allein folgt keine vollständige Aussage über alle Formalisierungen des Repositorys.

Eigene Folgerung: Für Ideen 03/04 muss der tatsächliche linearisierte massive Operator verwendet werden. Ein abstrakter Glättungssatz ersetzt keine Spektral-, Rand- und Energieflussdiagnose.

### M4: Formales Prüfen als Arbeitsweise

Die [Lean-Anleitung](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/README.md) und [Comparator-Anleitung](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/README.md) beschreiben eine gesonderte Prüfung. Für unser Projekt schlagen wir zunächst kleine eigene Lemmata aus [Bausteinen B–E](ANALYTISCHE-BAUSTEINE.md) vor. Deklaration, Übersetzung der Physikannahmen, Beweiskompilierung und Abhängigkeiten wären getrennt zu auditieren. In dieser Arbeit wurde kein solches Lemma als maschinengeprüft ausgegeben.

## Bewusst nicht übernommen

Der Katalogeintrag zu „Higgs moduli spaces“ ist ohne eine konkrete mathematische Abbildung kein Anschluss an das elektroschwache Higgsfeld. Große Zahlen von Manuskripten, gemeinsame Wörter oder ein Lean-Link auf Familienebene entscheiden keine physikalische Modellwahl. Wir behaupten keine Übertragung der Manuskriptresultate auf V.

## Ergebnis für die zehn Ideen

Der unmittelbare Gewinn ist eine schärfere Beweis- und Messstrategie. M1 beeinflusst 08 und 10, M2 beeinflusst 09, M3 begrenzt 03 und 04, M4 konkretisiert 05. Die anderen Ideen folgen aus unserem Portalpotential bzw. aus bereits gesichteter Fachliteratur. **Keine der zehn Ideen ist ein durch den Release bereits bewiesenes Higgs-/Hadronmodell.**
