# Chiraler Sektor: Volltextlektüre und Formelentscheidungen

Stand: 8. Oktober 2026. Arbeitsnotiz für die Literaturintegration; keine neue Simulation und keine Änderung eines Produktionsmodells.

## Lesedeckung

- Nathaniel Craig, **A gauge-invariant measure for lattice chiral fermions**, [arXiv:2610.09093v1](https://arxiv.org/abs/2610.09093v1), eingereicht 6.10.2026: Haupttext §§1–13 und technische Anhänge A–F vollständig in der lokalen PDF-Textextraktion gelesen (gedruckte Seiten 1–118); Literaturverzeichnis überflogen. Die separaten mathematischen, Lean- und zweidimensionalen Supplements wurden nicht gelesen oder ausgeführt. Volltextlektüre bedeutet hier keine unabhängige Prüfung aller Beweise.
- Piotr S. Topa, **Mass as pairing: an explicit Majorana mass on half of a generation does not seesaw in symmetric mass generation**, [arXiv:2610.07735v1](https://arxiv.org/abs/2610.07735v1), eingereicht 6.10.2026: Haupttext §§I–VIII, Anhänge A–B und Tabellen I–XVII vollständig gelesen; Referenzen überflogen. Begleitcode und Rohdaten nicht reproduziert. Zweispaltige Textextraktion erschwert stellenweise Formeltypografie; maßgeblich bleiben die angegebenen PDF-Gleichungen.

## Literaturbefund Craig — komprimierte Quellenzusammenfassung

Die Konstruktion betrifft vierdimensionale euklidische periodische Gitter, Overlap-Fermionen und eine hinreichend kleine Plaquettenschranke (2.3). Ausgangspunkt ist SU(5) mit vollständigem Multiplet 10 ⊕ 5̄, kein skalares Portalmodell. Formelkette: Overlap/Ginsparg–Wilson (2.6–2.9), Maßanomalie (4.12), globale Integrabilität (4.17), Vergleichsstrom (6.8), SM-Einschränkung (10.4, 10.9). Kubische Anomaliefreiheit und zusätzliche Paarungsbedingungen tragen die Verallgemeinerung (11.1–11.2).

Anhänge A–D behandeln Rekonstruktion, Spektrallücke, Lokalität und globale Phasen. Endliche Polynomapproximationen erhalten die exakten Integrabilitätsbedingungen nicht automatisch (E.20, F.11–F.13). Hilfsverfeinerung, klassischer Kontinuumsgrenzfall und Approximationsgrenze sind verschiedene Grenzprozesse (Abb. 12). §12 beschreibt Lean als Prüfung formalisierter Aussagen unter dokumentierten Annahmen. §13 lässt praktische Implementierung, Reflexionspositivität und wechselwirkende Kontinuumstheorie offen.

**Einordnung:** bedeutender Kandidat für einen neuen Eich-Fermion-Zweig; keine unmittelbare Übertragung auf ein unregelmäßiges V-Netz und keine Ableitung unserer Higgsparameter.

## Literaturbefund Topa — komprimierte Quellenzusammenfassung

Das Modell (2) ist ein vierdimensionales reduziertes Staggered-Fermionmodell mit Hilfsfeld σ und Majoranaquelle; ohne Eichfeld und ohne Higgsfeld. Satz 1 und Proposition 1 (§III) verbieten massenartige leichte Bilineare unter genau spezifizierten Rest- und Zustandsymmetrien. Die zusätzlichen Annahmen A3/A4 sind für eine Propagatornullstelle nötig. Eine Lückenskalierung allein entscheidet nicht über den Mechanismus.

Die numerische Reichweite ist L ≤ 8; Paar-Korrelatoren haben kein gesichertes Massenplateau (§IV, Abb. 1). Kritisch: auf 8⁴ besitzt die Quelle einen leichten Block mit Frobenius-Normanteil 0,368, während die Taste-Zerlegung auf 6⁴ nur 19,8 % der Impulse erfasst (§IV, Tabelle IV). Vergleiche unterschiedlicher Modenmengen können Wachstum vortäuschen; eingeschränkte Vergleiche ändern dessen Vorzeichen (§VII A). Viele vorab definierte Urteile bleiben MIXED/VOID/unentschieden (Tabelle V). Die diskrete Restanomalie ist nicht berechnet (§III).

**Einordnung:** bedingte Symmetrieaussage und begrenztes Modellresultat; weder allgemeine Widerlegung des Seesaw-Mechanismus noch Nachweis eines Higgsersatzes. Die offengelegten Einschränkungen sind nicht als von uns entdeckte Widersprüche auszugeben.

## Eigene Formelentscheidungen für fmhc-physics

### 1. Bestehendes skalares Portal: Parameter unverändert

Unser bisheriger Feldinhalt aus zwei komplexen skalaren Singuletts und einer reellen Higgsamplitude enthält keine chiralen Grassmann-Felder, Eichlinks oder Yukawa-Matrizen. Daher rechtfertigen diese beiden Arbeiten **keine** Änderung von a, b, η, c₈, des statischen Potentials oder der bereits geprüften Antwortkoeffizienten. Ein neuer Fermionzweig braucht eine eigene Wirkung, Symmetrietabelle und Validierung. Die Zuordnung einer skalaren Schwingung zu Quark-, Lepton- oder Neutrinomasse bleibt unbegründet.

### 2. Sofort sinnvolle Präzisierung: Krümmung ist keine Polmasse

Für unsere Störungskoordinaten q sei die quadratische Wirkung zunächst ausdrücklich definiert:

\[
L^{(2)}=\frac12\dot q^T M\dot q-\frac12q^T Hq.
\]

Dann lautet das Spektralproblem

\[
Hv=\Omega^2 Mv,
\]

nicht allgemein Ω² = Eigenwert(H). Diese Gleichung setzt positive kinetische Matrix M und fehlende gyroskopische Terme voraus. Auf rotierenden Q-Ball-Hintergründen können Terme linear in der Zeit-/Frequenzableitung entstehen; dort ist die vollständige linearisierte Dynamik erforderlich. Bis dahin heißen unsere publizierten Hessianwerte Energiekrümmungen. Auch ein korrekt berechnetes klassisches Ω ist noch kein renormierter Quantenpol und keine experimentelle Teilchenmasse.

### 3. Symmetrieprüfung vor jedem neuen Massenansatz

Für eine geplante Majorana-Matrix m und eine konkrete Darstellung U_g muss im ungebrochenen Zweig gelten:

\[
U_g^T m U_g=m\quad\text{für alle erhaltenen Symmetrien }g.
\]

Dies folgt direkt aus der Invarianz von ψᵀmψ. Für einen Dirac-Term ist stattdessen die passende links/rechts-Darstellung zu verwenden. Wir müssen zunächst alle zulässigen Matrizen bestimmen; erst danach darf eine Massenmatrix gefittet werden. Eine später gewählte unregelmäßige Geometrie besitzt gegebenenfalls weniger Symmetrien als eine kubische Referenz. Deshalb dürfen Nullstellen und verbotene Terme nicht von der Referenz ungeprüft auf V übertragen werden.

Konkreter eigener Kontrollwert für einen beliebigen behaupteten schweren Quellenblock J und vorab definierte Projektoren:

\[
\epsilon_{LL}=\frac{\|P_LJP_L\|_F}{\|J\|_F},\qquad
\epsilon_{LR}=\frac{\|P_LJP_R\|_F}{\|J\|_F}.
\]

Ein nur rechts angesetzter Quellterm erfordert beide Werte null bis zur begründeten Diskretisierungs-/Rundungsgenauigkeit. Beim Gittervergleich müssen identische physikalische Impulsbereiche verglichen werden; sonst ändert sich der gemessene Operator mit der Auflösung.

Diese Schreibweise behandelt J als Operator in einer orthonormalen Blockbasis. Für die Koeffizientenmatrix eines Majorana-Bilinears ist die Projektion entsprechend bilinear vorzunehmen, also etwa P_Lᵀ J P_L; Operator- und Bilineartransformation dürfen nicht vermischt werden.

### 4. Eigenständiger schwacher Zweig statt zusätzlicher skalarer Fitkonstante

Zunächst ein kubischer Referenzzweig mit ausdrücklich festgelegtem fermionischem Feldinhalt, Eichgruppe und Randbedingungen. Eine SM-Interpretation erfordert zusätzlich einen elektroschwachen Higgs-Dublettsektor; die bisherige reelle Amplitude genügt dafür nicht.

Als eigene Abnahmekriterien festhalten: korrekte Zahl leichter Fermionen, Eichkovarianz, Anomalieprüfung des **gesamten** Multiplets, endliche Lokalisierungslänge und kontrollierte Maßphase auch entlang geschlossener Feldpfade. Erst nach einer unabhängigen Referenzvalidierung folgt die Übertragung auf V. Dabei jede Gitteridentität und jedes Rest-Symmetrieargument neu prüfen. Literaturaufnahme allein verändert keinen Fortschrittsprozentwert.

## Entscheidung

**Jetzt übernehmen:** Quellen, Lesestatus, Symmetrieanforderungen und präzisere Bezeichnungen der Spektralgrößen. **Als neuen Forschungszweig vorbereiten:** chirale Eichfermionen und explizite Quellen-/Projektorkontrollen. **Nicht aus diesen Quellen ableiten:** neue numerische Portalparameter, bestätigte Teilchenmassen, universelles Anti-Seesaw-Gesetz oder bereits gelöste schwache Kraft auf V.
