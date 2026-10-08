# Schur-Paper: tragfähiger Kern und Grenzen

[S] Volltextlektüre von [Barceló/Mitra, 2609.39910v1](https://arxiv.org/abs/2609.39910v1), Abschnitte I–VI und Anhänge A–C; Referenzliste gesichtet, zitierte ältere Arbeiten nicht vollständig nachgelesen. Keine Reproduktion der Abbildung.

Der brauchbare Kern ist die endliche Blockelimination in III und Anhang A sowie das explizite Fourierbeispiel in IV/Anhang B: punktweiser Grenzwert und unendliche Summe können verschiedene Antworten liefern. Die Weiterverallgemeinerungen in IV.C und V verlangen jedoch mehr Voraussetzungen, als dort angegeben. Deshalb kein ungeprüftes Übernehmen einer universellen Rang-zwei- oder Einkanal-Konvergenzaussage. Die Quelle betrifft zunächst eine zusätzliche Raumdimension; unser glattes 3D-Portal ist ein anderes Modell.

## [M] Eigene Gegenprüfung der Rangbehauptung

Die in Gleichung (30) angegebene Gauß-Überlappmatrix enthält einen Term
`cos((i−j)y*/R) exp(−(i−j)²ε²/2)` und einen entsprechenden Summenindexterm. Bei festem ε>0 und i=j→∞ bleibt der erste Term gleich eins, während der Summenindexterm verschwindet. Wählt man beliebig viele hohe Indizes mit paarweisen Abständen deutlich größer als 1/ε, wird die zugehörige normierte Hauptuntermatrix beliebig nahe an eine Einheitsmatrix beliebiger endlicher Größe gebracht.

Jede Rang-zwei-Matrix hat auf einem dreidimensionalen solchen Unterraum eine Nullrichtung. Dort kann ihr Operatornormfehler gegenüber einer beinahe Einheitsmatrix nicht klein werden. Schneller Abfall mit **Indexdifferenz** begründet daher keine gleichmäßig kleine Rang-zwei-Näherung der ganzen Überlappmatrix. Eine durch schwere Propagatoren gewichtete Niederenergieantwort könnte trotzdem gut approximierbar sein; das wäre eine andere, eigens zu begründende Behauptung.

## [M] Eigene Gegenprüfung der Einkanal-Konvergenz

Für eine Summe der Form `Σ f_n²/M_n` reicht „ein Kanal“ nicht aus. Schon `f_n=1`, `M_n=M n`, n≥1, ergibt die divergente harmonische Reihe. Benötigt werden konkrete spektrale Wachstums-/Überlappabfallbedingungen oder eine konsistente Regulierung und Renormierung. Dies ist ein Gegenbeispiel zur pauschalen Begründung, keine Behauptung, dass jedes physikalisch ausgearbeitete KK-Neutrinomodell divergiert.

Zusätzlich sind die in (10) definierten ungedämpften Sinus-/Kosinusfolgen auf dem unendlichen Turm im Allgemeinen nicht ℓ². Die endliche Rangdarstellung bleibt gültig; ein unendlicher punktförmiger Kopplungsoperator benötigt einen präzisen Definitionsbereich oder eine Formulierung als regulierte quadratische Form. Die problematischen Erweiterungen widerlegen nicht automatisch das konkrete Fourierresultat des Papers.

## Konsequenz für unser Projekt

Die [dynamische Herleitung](FORMEL-ABGLEICH.md) wird aus unserer eigenen Wirkung gewonnen. Der Literaturvergleich motiviert die Prüfung von Resolventen und Grenzübergängen, liefert aber weder neue Portalparameter noch eine Berechtigung, große Matrizen pauschal durch Rang zwei zu ersetzen. Diese analytischen Einwände wurden innerhalb des Reviews nochmals gegengelesen; eine externe Begutachtung oder Autorenkorrespondenz ist nicht erfolgt.
