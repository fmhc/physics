# Formelabgleich: Higgsantwort, Spektren und neue Modellzweige

08.10.2026. **[M] Eigene analytische Herleitung, [H] noch zu prüfende Erweiterung. Keine neue Simulation.** Ausgangspunkt sind die [analytischen Bausteine](../higgs-verbindungen-20261007/ANALYTISCHE-BAUSTEINE.md) und die veröffentlichten [statischen Winkeltests](../higgs-angular-modes-20261008/ERGEBNIS.md). Quellenkritik und Lesedeckung: [Literaturreview](README.md).

## Entscheidung

Die gelesene Literatur begründet **keine Änderung der bereits geprüften statischen Portalenergie oder ihrer Parameter**. Sie motiviert eine explizite dynamische Erweiterung, eine sorgfältigere Prüfung von Grenzübergängen und getrennte Quanten-/Fermion-/Kosmologiezweige. Die Formeln unten ergänzen den Modellvertrag; historische Rechencodes, Eingaben und Resultate bleiben als ausgeführte Stände erhalten.

| Bereich | Konsequenz für unsere Formeln | Status |
|---|---|---|
| Statisches Higgsportal | E3/Ecomp und vollständige Kettenregel beibehalten | bereits geprüfter Anwendungsbereich |
| Dynamische Higgsantwort | zeitabhängigen inversen Operator und mitrotierende Amplituden-/Phasenkopplung ergänzen | unten hergeleitet, numerisch offen |
| Fix-Q-Hessian | radialen Rang-eins-Term nicht blind als dynamische Steifigkeit übernehmen | unten präzisiert |
| Grenzübergänge | Gitter-/Box-/Quellenbreite getrennt halten, gleichmäßige Schranken verlangen | analytische Bedingungen und Prüfplan |
| Hadronen | gemeinsame Zerfallsschwellen, Quantenzahlen und Spin/Statistik definieren | eigener Modellzweig, siehe HADRONEN.md |
| Quantisierte Q-Balls | Mittelwert und Fluktuationen samt renormierter Wirkung und Gesamtladung behandeln | neue Näherung, siehe QUANTEN-PORTAL.md |
| Schwache Kraft | Diracoperator, chirales Maß, Eichdarstellungen und Anomalien ergänzen | neue Theorie, siehe CHIRAL.md |
| Kosmologisches Portal | Expansion, thermische und radiative Terme nur nach Normierungs-/Matchingvertrag | kein Term für den bisherigen Vakuumbenchmark |

## 1. Unsere unveränderte Ausgangswirkung

In den bisherigen dimensionslosen Konventionen, bei Minkowski-Signatur (+,−,…,−):

```text
L = Σ_i |∂ψ_i|² + 1/2 (∂y)² − V,
ρ_i=|ψ_i|², S=ρ_1+ρ_2, D=y²−y0²,
V = Σ_i(ρ_i−ρ_i²+ρ_i³/2+c8*λ*ρ_i⁴/4)
    −ρ_1ρ_2/2−2η Re(ψ_1* ψ_2)+a D²/4+b D S/2.
```

Das sind zwei komplexe Singuletts und eine reelle Amplitude. Ein SU(2)-Higgsdublett, chirale Fermionen, eine Quarkfarbladung oder Baryonzahl entstehen nicht durch Umbenennung dieser Variablen. Die B13-Skalen und die bisher geprüften Parameter bleiben unverändert.

## 2. Die Higgsantwort erhält eine Zeitentwicklung

Aus der Wirkung folgt exakt

```text
(∂t²−Δ)y + a(y²−y0²)y + b S y = 0.
```

Mit y=y0+χ, M_H²=2a y0² und K=−Δ+M_H² folgt

```text
(∂t²+K)χ = −b y0 S − b S χ − 3a y0 χ² − a χ³.       (D1)
```

Die bisherige statische Entwicklung χ1=−K⁻¹b y0 S wird dadurch nicht falsch. Ihre dynamische Verallgemeinerung benötigt Anfangsdaten oder eine kausale Randbedingung. Bei verschwindender einlaufender freier Higgsanregung lautet die formale Portalentwicklung

```text
G_R = (∂t²+K)⁻¹_ret,
χ1 = −G_R(b y0 S),
χ2 = −G_R(b S χ1 + 3a y0 χ1²).                       (D2)
```

Bei allgemeinen Anfangsdaten kommt die homogene Lösung hinzu. Ein symmetrischer inverser Operator einer gewöhnlichen Wirkung ist nicht ohne Weiteres der retardierte Operator einer Anfangswertaufgabe. Für geschlossene reduzierte Gleichungen entweder die kausale Lösung einsetzen oder einen passenden Realzeitformalismus verwenden.

Für e^(−iνt), zunächst linear um das Vakuum, wird die Antwort

```text
χ1(ν) = −[K−(ν+i0)²]⁻¹ b y0 S(ν).                  (D3)
```

Die Näherung K⁻¹ gilt nur weit genug unter den betreffenden Higgsanregungen. Im einfachen positiven, zeitunabhängigen Fall:

```text
(K−ν²)⁻¹ = K⁻¹ + ν² K⁻² + O(ν⁴),
‖(K−ν²)⁻¹−K⁻¹‖ ≤ ν² / [κ(κ−ν²)],
K ≥ κ I > 0,  0 ≤ ν² < κ.                           (D4)
```

Diese Schranke setzt einen selbstadjungierten Operator, reelles ν und dieselben Randbedingungen und Hilbertraumnormen voraus. Sie gilt nicht unmittelbar für komplexe instabile Frequenzen und ist keine direkte Fehlerschranke für Modenfrequenzen oder Resonanzen. Kleine Feldabsenkung allein garantiert keine adiabatische Antwort.

## 3. Dynamik um einen rotierenden Q-Ball: der entscheidende Zusatz

Sei ψ_i=e^(iωt)[f_i+(q_i+i p_i)/√2], y=y_*+h. Die reellen Störungen sind damit kanonisch normiert. In der quadratischen kinetischen Wirkung steht neben den Geschwindigkeitsquadraten

```text
ω Σ_i(q_i ∂t p_i−p_i ∂t q_i).
```

Die Hintergrundfrequenz ω ist von der Störfrequenz ν zu unterscheiden. A_ω und D_ω seien die Amplituden- und Phasenblöcke der zweiten Variation von E_spatial−ω²∫S; B ist die Amplituden-Higgs-Kopplung, C der Higgsblock. Für den reellen Hintergrund gibt es keine lineare p-h-Kopplung. Die linearen Bewegungsgleichungen lauten

```text
q̈ − 2ω ṗ + A_ω q + B h = 0,
p̈ + 2ω q̇ + D_ω p       = 0,
ḧ           + Bᵀ q + C h = 0.                      (D5)
```

In kontinuierlichen kanonischen Variablen:

```text
C = −Δ + a(3y_*²−y0²)+b S_*,
B_i = √2 b y_* f_i  (Multiplikationsoperator).
```

Für e^(−iνt) und invertierbares C−ν²I ergibt die exakte lineare Elimination

```text
[ A_ω−ν²I−B(C−ν²I)⁻¹Bᵀ     2iωνI ] [q] = 0.
[       −2iωνI              D_ω−ν²I ] [p]             (D6)
```

An Polen des eliminierten Blocks ist das volle System (D5) maßgeblich; dort darf man keine Modi durch eine singuläre Schur-Inversion verlieren. Für offene Strahlungskanäle ist außerdem die auslaufende/retardierte Randbedingung explizit festzulegen. Eine geschlossene endliche Box beschreibt ein anderes Spektralproblem.

**Die vorhandenen Fix-Q-Hessians dürfen nicht direkt für A_ω eingesetzt werden.** Im radialen Code steht zusätzlich

```text
R_Q = 4ω² |u><u| / <u,u>,  u=(r f_1,r f_2),
A_Q = A_ω + R_Q.                                    (D7)
```

Diese Identität gilt in der Normierung von HIGGS-MODES-1 und auf demselben Hintergrund. Für l=0 muss der Rang-eins-Term beim Aufbau des unbeschränkten mitrotierenden Systems abgezogen werden. Für l>0 verschwindet dieser Beitrag wegen des Winkelmittels. Die Ladungserhaltung folgt dann aus den Bewegungsgleichungen. Will man auf δQ=0 beschränken, muss man die vollständige linearisierte Ladung einschließlich Geschwindigkeiten benutzen, nicht nur eine Amplitudenprojektion.

Direkt aus Q=2 Im∫Σψ_i*∂tψ_i folgt in dieser Konvention

```text
δQ = √2 ∫ Σ_i f_i (2ω q_i + ṗ_i).                  (D8)
```

Bei stationärem Hintergrund, selbstadjungiertem D_ω und verschwindendem Randfluss gilt D_ω f=0 und damit d(δQ)/dt=−√2⟨f,D_ω p⟩=0. Numerische Hintergrundresiduen begrenzen diese Identität. Bei zeitlich exponentiellen Modi mit nichtverschwindendem Exponenten muss die konservierte lineare Ladung null sein. Die gemeinsame Phase und die Behandlung ihrer Nullrichtung sind gesondert zu kontrollieren.

Für ν²≪λ_min(C) ergibt (D6) im Amplitudenblock

```text
A_ω − B C⁻¹Bᵀ − ν²[I + B C⁻²Bᵀ] + O(ν⁴).
```

Die führende zusätzliche Trägheit ist daher **+B C⁻²Bᵀ**, positiv semidefinit für positiv selbstadjungiertes C. Die Phasenkopplung ±2iων bleibt bestehen. Auch mit dieser Trägheit sind Quadratwurzeln der statischen Fix-Q-Eigenwerte keine allgemeinen dynamischen Frequenzen.

## 4. Netzgewichte und Dimensionen explizit halten

Bei nichtkanonischen diskreten Variablen lautet das lineare Problem allgemein

```text
[K_lin + s G + s² M] ξ = 0,
M=Mᵀ>0, G=−Gᵀ,
D_eff(s)=D_mm(s)−D_mh(s)D_hh(s)⁻¹D_hm(s).           (D9)
```

M enthält Volumen-/Kinetikgewichte. Ein algebraisch symmetrischer Graph-Laplacian ohne diese Zuordnung ersetzt weder die physikalische Kinetik noch die zugehörige Norm. Bei blockdiagonaler Kinetik ist der Higgsblock C+s²M_h; nach Massennormierung wird daraus die Form in (D6). Gewichtete Adjungierte oder eine explizite Transformation mit M^(−1/2) sind erforderlich.

Die lokalen Feldgleichungen (D1),(D5) gelten in d Raumdimensionen mit dem jeweiligen Δ und Maß. Für radiale Zerlegung gilt vor Transformation

```text
−Δ_l = −∂r²−(d−1)∂r/r + l(l+d−2)/r².
```

Nach Multiplikation mit r^((d−1)/2) kommt die Barriere
`[l(l+d−2)+(d−1)(d−3)/4]/r²` hinzu. In 2D sind Winkelmoden ganzzahlige Fouriermoden (l=|m|), in 3D Kugelflächenfunktionen; in 1D benutzt man den eindimensionalen Operator mit Randbedingungen/Parität statt eines ungeprüften l-Schemas. Ein radialer 3D-Lauf bleibt ein dreidimensionales Modell. Die alten 3D-Umrechnungen von Energie und Ladung werden nicht auf andere Dimensionen kopiert.

## 5. Was aus dem Schur-Paper tatsächlich folgt

Das endliche Schur-Komplement ist reine Blockalgebra. Grenzübergänge brauchen zusätzliche analytische Kontrolle. Für unseren glatten Quellenzweig sind weder eine punktförmige Brane noch der spezielle komplementär-chirale KK-Kanal implementiert. Eine dort auftretende Zweideutigkeit ist deshalb kein nachgewiesener Fehler unserer statischen Rechnung.

Eine hinreichende Struktur für einen regulären Vergleich ist ein gemeinsamer Funktionsraum mit konsistenten Projektionen/Einbettungen, eine gleichmäßige Lücke `C_h≥cI>0` und Konvergenz der relevanten Lösungen und Kopplungen. Über

```text
C_h⁻¹−C⁻¹ = C_h⁻¹(C−C_h)C⁻¹
```

kann man nach passender Identifikation der Räume Fehler abschätzen. Für unbeschränkte Kontinuumsoperatoren ist Operatornormkonvergenz von C_h selbst meist nicht die richtige Forderung; nötig ist eine geeignete Resolventen-/Formkonvergenz. Endliche positive Matrizen allein beweisen keine gleichmäßige Kontinuumslücke.

Falls künftig eine Quellenbreite ε eingeführt wird, zuerst bei festem physikalischem ε das Gitter verfeinern und die Quelle auflösen. Ein zusätzlicher ε→0-Grenzfall ist ein eigenständiges Modellproblem. R→∞, h→0 und ν→0 sind ebenfalls getrennte Schritte. Im bisherigen Benchmark gibt es keinen ε-Regulator, dessen Vertauschung wir bereits getestet hätten.

## 6. Konkreter nächster Prüfvertrag

1. Auf denselben archivierten Profilen A_ω, D_ω, B, C und die kinetischen Gewichte aufbauen; (D7) gegen die bekannten Fix-Q-Blöcke prüfen.
2. Die linearen Gleichungen gegen die direkt variierte zeitabhängige Wirkung prüfen: Vorzeichen der ±2ω-Kopplung, Ladung (D8), Phasen- und Translationsrichtungen.
3. Volles System (D5) gegen frequenzabhängige Elimination (D6) vergleichen. Erst danach die niederfrequente Trägheitsnäherung bewerten; Polbereiche separat behandeln.
4. Auf den vorhandenen Gitter-/Boxstufen Konvergenz, Eigenresiduen, Ladungsfehler und bei instabilen Modi Re(s)>0 ausweisen. Akzeptanzgrenzen vor Ausführung einfrieren.
5. Quanten-Hartree, fermionische Eichstruktur und kosmologische Terme bekommen jeweils eigene Wirkungs-/Normierungsverträge. Kein Vermischen ihrer Parameter mit dem statischen Pilot.

Dies ist eine analytisch konkretisierte Aufgabenliste, **kein gestarteter oder bestandener Lauf**. Die Entwicklungsschätzungen bleiben Higgs 2 %, schwache Kraft 2 %, Mesonen/Baryonen 10 %.
