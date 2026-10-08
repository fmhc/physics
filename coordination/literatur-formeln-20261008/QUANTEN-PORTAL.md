# Volltextprüfung: Quanten-Q-Balls und kosmologisches Higgsportal

Stand: 8. Oktober 2026. Gelesen wurden beide lokalen PDF-Textextraktionen vollständig: 2605.25243v1, Haupttext §§1–4 und Anhang A (A.1–A.32), sowie 2610.07331v1, Haupttext I–VI und Anhänge A–C. Auch Bildunterschriften, Fußnoten und Literaturverzeichnisse wurden gesichtet; referenzierte Fremdarbeiten und numerische Codes wurden damit nicht unabhängig geprüft. Vergleichsgrundlage: `ANALYTISCHE-BAUSTEINE.md` des eigenen Higgs-Verbindungsberichts. Keine Numerik oder Tests ausgeführt.

## Quellenbefunde (jeweils unter 200 Wörter)

### Su, Xie, Zhou: Quantum-Corrected Q-balls in the Friedberg-Lee-Sirlin Model

[arXiv:2605.25243v1, 24.05.2026](https://arxiv.org/abs/2605.25243v1). Das 3+1-dimensionale FLS-Modell enthält ein komplexes und ein reelles Feld; sein quartisches Potential ist nicht unser sechst-/achtgradiges Zweikomponentenpotential. Die Autoren entwickeln räumlich inhomogene Mittelwerte und Zweipunktfunktionen in einer Hartree-Näherung. Maßgebliche Anker: Potential (2.12), Kovarianzen (2.18–2.28), gekoppelte Gleichungen (2.29–2.55), stochastische Darstellung (2.57–2.65), gewählte Vakuumsubtraktion (2.67–2.74), Ladungszerlegung (2.84–2.87), Austauschquellen (3.5), 2PI-Ableitung Anhang A. Die Simulationen zeigen Ladungsaustausch und Fälle, die klassisch stabil, in dieser Näherung aber instabil sind. „Kein Zerfall“ gilt nur im beobachteten Zeitfenster. Streuung, Dissipation und nichtlokale Gedächtniseffekte jenseits Hartree fehlen. Die dargestellte Massensubtraktion ist kein Beleg für eine universelle Renormierung unseres EFTs. Das Paper rechtfertigt eine zusätzliche Quantenprüfung, keine nachträgliche Änderung der Ergebnisse unserer klassischen Rechnungen.

### Henrich, Mambrini, Olive: Spectator Dark Matter and the Higgs Portal

[arXiv:2610.07331v1, 05.10.2026](https://arxiv.org/abs/2610.07331v1). Ein reeller Z₂-Spektator mit SM-Higgsdublett wird in einer expandierenden Kosmologie untersucht. Portalinduzierte Schleifen- und thermische Beiträge beeinflussen Kondensatentwicklung und Anfangsbedingungen. Anker: Normierung (3), effektive Masse und Hochtemperaturkoeffizient (5–9), Oszillationsbedingung (10), Isokurvatur (18–19), adiabatische Entwicklung (71–72), Krümmungskopplung (106–114), Verdampfung Anhang A, gemeinsames O(4)-Higgs/Spektator-Maß Anhang B, Freeze-in Anhang C. Wesentlich: Die thermisch beginnende Minimalvariante scheitert innerhalb der untersuchten Annahmen an kombinierten Bedingungen; Krümmungskopplung kann sie wieder ermöglichen. Eine rein thermische Beschreibung ist kein generischer Dunkle-Materie-Nachweis. Die Hochtemperaturnäherung darf nicht unterhalb des elektroschwachen Übergangs fortgesetzt werden. Die Näherungskoeffizienten der Reliktdichte enthalten teilweise relevante Übergangskorrekturen. Unser statisches, geladenes Solitonenmodell hat weder den vorausgesetzten SM-Wärmehaushalt noch diese kosmologischen Anfangsbedingungen.

## Eigene Herleitungen und vorgeschlagene Änderungen

Die folgenden Gleichungen sind eigenständige Übertragungen auf das vorhandene Projektpotential, keine Ergebnisse der beiden Papers. Sie sind als analytische Erweiterung zu markieren, nicht als implementierte oder validierte Simulation.

### 1. Quantum-Sektor als konsistentes Fünffeldsystem formulieren

Für die vorhandene Kinetik setzen wir

```text
ψ₁=(q₁+i q₂)/√2,  ψ₂=(q₃+i q₄)/√2,  q₅=y,
Lkin=½ Σ_A (∂q_A)²,  A=1,…,5,
Φ_A=⟨q_A⟩, δq_A=q_A−Φ_A,
C_AB(x)=½⟨{δq_A(x),δq_B(x)}⟩.
```

Die vollständige Kovarianz gehört zur Variablenmenge. Anfangs verschwindende Mischkovarianzen dürfen später nicht pauschal auf null gesetzt werden. Für ein lokal reguliertes polynomiales Potential definiert die Gauß-Faktorisierung formal

```text
𝒲(Φ,C)=exp[½ C_AB ∂Φ_A ∂Φ_B] V(Φ),
□Φ_A + ∂𝒲/∂Φ_A = 0,
𝓜²_AB = ∂²𝒲/(∂Φ_A∂Φ_B)  [C bei diesen Ableitungen fest].
```

Die Exponentialreihe terminiert für unser Polynom. Diese Form vermeidet falsch übernommene FLS-Faktoren und berücksichtigt auch Wick-Kontraktionen aus ρ³ und ρ⁴. Für eine konkrete Quantenimplementierung müssen Zustand, kanonische Normierung, regulierte Gegenwirkung und konsistente Kovarianzentwicklung gemeinsam festgelegt werden. Das ist eine Gauß-Näherung, keine exakte Quantenlösung. In unserer 3D-Projektnormierung trägt die Wirkung insgesamt den Faktor 1/λ; dementsprechend dürfen die Kovarianzen nicht mit einer unbemerkt anders gewählten effektiven ℏ-Normierung initialisiert werden.

Explizites Beispiel für den vorhandenen Portal-/Higgsteil: Y=Φ₅, a,b,y₀ wie im Projekt, S_Φ=½Σ_{a=1}⁴Φ_a². Die Gauß-gemittelte Kraft in der y-Gleichung lautet

```text
F_y = a[Y³+3Y C₅₅−y₀²Y]
      +b[Y S_Φ + (Y/2) Σ_a C_aa + Σ_a Φ_a C₅a].
```

Die Portal-Kraft einer kanonischen Materiekomponente lautet

```text
F_a,portal = (b/2)[(Y²+C₅₅−y₀²)Φ_a + 2Y C₅a].
```

Bereits diese Ableitung zeigt: Nur `y² → Y²+C₅₅` zu ersetzen und Mischkovarianzen zu verwerfen wäre unvollständig. Die übrigen Materiekräfte müssen aus demselben 𝒲 abgeleitet werden.

### 2. Ladungsdiagnostik erweitern, klassische Ladung nicht umdefinieren

Für a_i=2i−1, b_i=2i gilt in den kanonischen Variablen

```text
Q_total = Σ_i ∫d³x [Φ_ai ∂tΦ_bi − Φ_bi ∂tΦ_ai
                    +⟨δq_ai ∂tδq_bi − δq_bi ∂tδq_ai⟩]
        = Q_mean + Q_fluct.
```

Dies folgt direkt aus dem Noetherstrom des eigenen gemeinsamen U(1). Wegen η≠0 sind bereits die beiden Speziesladungen nicht unabhängig erhalten. Mit Fluktuationen ist auch Q_mean nicht allein erhalten. Ein Rückgang der zentralen Mittelwertamplitude beweist daher noch keinen Ladungsverlust oder Zerfall: zusätzlich Gesamtladung, Fluss durch die Beobachtungsgrenze und Lokalisierung messen. Die bestehende klassische Fix-Q-Rechnung bleibt als C=0-Vergleich erhalten; ein Quanten-Fix-Q-Verfahren muss die Gesamtladung beschränken. Q_phys=Q_total/λ gilt nur mit der vorhandenen 3D-Skalierung.

### 3. Renormierung vor einer Quantenaussage neu festlegen

Unsere ρ³- und gegebenenfalls ρ⁴-Terme sind in 3+1 Dimensionen höhere EFT-Operatoren. Deshalb reichen die FLS-Massenverschiebungen nicht als Rezept. Vor einer Quantenrechnung sind physikalischer Cutoff, Matchingbedingungen, Gegenoperatoren und der zu prüfende Energiebereich anzugeben. Vakuummasse, Vakuumlage und gewählte Kopplungen sollen über Gitterverfeinerungen dieselben renormierten Größen bezeichnen. Subtraktionen dürfen nicht unabhängig in Kraft, Energie und Kovarianzentwicklung eingebaut werden; diese müssen aus einer gemeinsamen regulierten Näherung stammen. Ein neuer Lauf bei anderem Gitterabstand ist sonst gleichzeitig eine Änderung der Theorie.

### 4. Thermischen SM-Koeffizienten nicht in das Ein-Amplitudenmodell kopieren

Rückübersetzung des Projektportals in dimensionierte Felder Ψ_i,h:

```text
V_portal = (g/2)(h²−v²) Σ_i |Ψ_i|².
```

Ein einzelner kanonischer reeller Materieanteil s erhält g(h²−v²)s²/4. Bei genau dieser Normierung würde ein tatsächlich vorhandenes relativistisches Wärmebad einer einzigen reellen h-Komponente mit ⟨δh²⟩_T=T²/12 den Beitrag

```text
δm_s² = (g/2)⟨δh²⟩_T = g T²/24
```

erzeugen. Ein SM-Dublett mit vier thermischen reellen Komponenten ergäbe unter denselben Hochtemperaturannahmen gT²/6. Der Faktor vier stammt von anderer Feldzahl, nicht von einer verbesserten numerischen Genauigkeit. Unsere y-Amplitude allein liefert kein SM-Wärmebad. Außerdem setzt die Hochtemperaturformel relativistisch leichte thermische Moden voraus; große Hintergrundmassen können sie ungültig machen. Temperatur, Abkühlung und Verteilungsfunktionen sind bisher zusätzliche Modellannahmen.

Ebenso wichtig ist die Vakuumsubtraktion: Im Projekt verschwindet der Portal-Massenbeitrag bei h=v bereits. Eine zusätzlich eingetragene Verschiebung +g v²/2 würde die bestehende Vakuumdefinition doppelt ändern. Bei Umformulierung in ein unverschobenes Portal ist stattdessen m₀²=m²−g v²/2 zu setzen. Mit dem vorhandenen Mischterm sind die beiden freien Materie-Massenquadrate bei h=v gleich m²(1∓η), nicht beide m². Die im Spektatorpaper verwendete zusätzliche Annahme eines nichtnegativen unverschobenen nackten Massenquadrats darf nicht stillschweigend auf unsere parametrisierte EFT übertragen werden.

### 5. Kosmologie nur als ausdrückliche neue Modellvariante

Bei gewünschter FLRW-Erweiterung seien A(t) der Skalenfaktor (nicht der Potentialparameter a) und H=Ȧ/A. Die klassischen Felder erfüllen dann bei minimaler Kopplung

```text
q̈_A + 3H q̇_A − A(t)⁻² Δ_com q_A + ∂V/∂q_A = 0,
Q_com = ∫d³x_com A(t)³ j⁰.
```

Bei erhaltener globaler U(1)-Symmetrie bleibt Q_com ohne Randfluss konstant. Erst danach lassen sich Temperaturbeiträge, eine konkret spezifizierte Krümmungskopplung und Inflation/Reheating ergänzen. Für einen schwach gedämpften nahezu harmonischen Modus folgt unter H/ω≪1 und |ω̇|/ω²≪1 das adiabatische Verhalten E_mode/ω näherungsweise konstant; für ein homogenes expandierendes Kondensat entsprechend ρ A³/ω. Das ist keine automatisch gültige Invariante eines räumlich lokalisierten, intern rotierenden oder fragmentierenden Q-Balls. Nahe Resonanzen und Instabilitäten muss die volle Dynamik untersucht werden.

## Entscheidung für die bestehenden Formeln

- **Behalten:** klassisches Potential, statische Antwort, Fix-Q-Minima und deren dokumentierte klassische Gültigkeitsbereiche.
- **Jetzt ergänzen:** klare Gesamtladungsformel für eine Quantenvariante, Fünffeld-/Kovarianzansatz, EFT-Matchingpflicht sowie Abgrenzung statischer Stabilität von Quantendynamik.
- **Nicht pauschal einsetzen:** FLS-Grenzfrequenzen, deren Gegenparameter, SM-Thermalmasse, Spektator-Isokurvaturgrenzen oder Reliktdichteformeln.
- **Neue Studienvariante:** eine vorab definierte, renormierte Gauß-/Hartree-Dynamik nach erfolgreicher klassischer Zeitentwicklung; kosmologische Variante separat. Keine Prozentanhebung durch diesen Literaturvergleich.
