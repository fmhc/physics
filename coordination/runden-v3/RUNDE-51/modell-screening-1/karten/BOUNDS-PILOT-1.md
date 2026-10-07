# BOUNDS-PILOT-1 – Schranken an einem Kontrollproblem

Status [H]: Methodenentwurf, noch nicht gerechnet. Quellenkontext: [Volltextvergleich, Abschnitt 4](../VOLLTEXT-VERGLEICH-20261007.md#4-schranken-statt-nur-variationsminima).

Wähle zunächst ein sehr kleines Z2-Eichmodell mit vollständig angebbarer Basis, Hamiltonian und Gauss-Bedingung. Bestimme seine Grundzustandsenergie durch exakte Diagonalisierung und konstruiere unabhängig eine variationale obere sowie eine semidefinite untere Schranke.

Erfolgskriterium: E_unten ≤ E_exakt ≤ E_oben innerhalb ausgewiesener numerischer Toleranzen. Nebenbedingungen, Eigenwertreste, duale Zulässigkeit und Rundung dokumentieren. Eine falsche Inklusion darf nicht durch größere Toleranzen verborgen werden. Observablenschranken zusätzlich am exakten Zustand prüfen.

Erst bei bestandener Kontrolle Aufwand einer Übertragung auf V und kontinuierliche Eichgruppen abschätzen. Endliche Hilbertraumtrunkierung ist eine neue Fehlerquelle. Solvererfolg allein wird nicht als rigoroses Zertifikat bezeichnet. Dieser Pilot ersetzt keine bisherigen SU(2)-Simulationen.
