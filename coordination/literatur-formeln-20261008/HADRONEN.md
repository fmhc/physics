# Hadronen: Volltextprüfung vom 8. Oktober 2026

**Abdeckung:** Beide lokalen v1-PDF-Textfassungen vollständig gelesen: 2610.07818, Haupttext S. 1–5 und Supplement S. 9–14; Literaturverzeichnis S. 5–8 überflogen. 2608.26608, sämtliche Abschnitte 1–6, S. 1–24; Literaturverzeichnis S. 24–29 überflogen. Keine numerische Reproduktion. Die folgenden Einwände sind eigene analytische Prüfungen, keine Behauptung eines externen Gutachterkonsenses. PDF-Text kann Formelsatz beschädigen; vor Übernahme fraglicher Gleichungen Originalsatz prüfen.

## 2610.07818v1 — Zhang, Lu, Wang, Zhao

[Fully charmed tetraquarks on the Lattice with controlled errors](https://arxiv.org/abs/2610.07818v1), eingereicht 6. Oktober 2026.

Nichtrelativistisches Quarkpotentialmodell, keine vollständige Gitter-QCD: Hamiltonian und Farb-/Spinpotential in Gl. (1–2), Gesamtantisymmetrie nach Gl. (3). Lanczos liefert Eigenwerte des diskretisierten Modells. Der vorhergesagte niedrigste Viercharmzustand liegt unter der Zweicharmoniumschwelle (Tab. III). Methodisch nützlich sind vollständige Austauschsektoren, Schwellenvergleich und getrennte Volumen-/Gitterprüfungen.

**Eigene Prüfung:** Ωccc ist in Tab. II ausdrücklich nur mit theoretischen Rechnungen verglichen; das Abstract überzieht den experimentellen Benchmark. Das Supplement „Dependence on the lattice spacing“ zeigt keinen kontrollierten Kontinuumsgrenzwert des Tetraquarks. Charmoniumschwellen werden aus dem feineren Gitter als näherungsweise Kontinuumswerte übernommen; ein Vergleich beim identischen endlichen Regulator wäre zusätzlich nötig. Tab. V bezeichnet ungewichtete Residuen als χ²/d.o.f.; daraus folgt kein kalibrierter statistischer Gütenachweis. Unterhalb ηcηc sind nicht automatisch sämtliche starken Zerfälle verboten: Charm-Anticharm-Annihilation bleibt zu untersuchen; der Haupttext nennt selbst weitere hadronische Kanäle. Ein endlicher Eigenwert oberhalb Schwelle beweist allein keine Resonanz. Gl. (8)/Tab. IX: A1 enthält auch J=4; A1-Projektion beweist nicht ausschließlich J=0.

**Entscheidung:** Prüfmethodik übernehmen; keine Quarkparameter, Massen oder starken Stabilitätsbehauptungen als Bestätigung unseres Skalarmodells übernehmen.

## 2608.26608v1 — Copinger, Eto, Nitta

[Fermi gas of domain-wall Skyrmions in QCD in a strong magnetic field](https://arxiv.org/abs/2608.26608v1), eingereicht 27. August 2026.

Zweiflavour-Chiraltheorie plus WZW-Anomalieterm und QED, externes Magnetfeld und Baryonchemiepotential: Gl. (2.3–2.7). Halbperiodenreduktion erzeugt eine CP¹/O(3)-Wandtheorie, Gl. (3.7–3.13). Fermionische Statistik wird aus früheren WZW-Arbeiten übernommen, nicht aus der klassischen Windungszahl allein gewonnen (§3.3). Freie Fermi-Scheibe und Umrechnung zur Volumendichte: Gl. (4.1–4.5); thermische Abschirmung: §5, insbesondere Gl. (5.29–5.38). Der ChPT-Abschirmungsanteil benutzt den Kink-Grenzfall; das verdünnte Gas ist keine allgemeine dichte Baryonenmaterie.

**Eigene Prüfung:** §5.3 schreibt vor Gl. (5.36) eine Dichteumrechnung, die dimensional Gl. (4.4–4.5) widerspricht: Für Flächendichte σ und Wandabstand ℓ/2 gilt n₃=2σ/ℓ, nicht n₃=ℓσ/2. Definitionen und Vorzeichen der Gl. (5.31–5.35) sowie der Mean-Field-Faktor in der Chemiepotentialverschiebung müssen vor Übernahme neu hergeleitet werden. Gl. (4.6) verwendet eine Ableitung bei festgehaltener effektiver Masse und Periodenlänge; entlang selbstkonsistenter Hintergrundänderungen ist das nicht automatisch dieselbe Suszeptibilität.

**Entscheidung:** Für V nur als separate Modellvariante vormerken. WZW-Struktur, physikalische Baryonenzuordnung, externe Felder und Wandreduktion fehlen bislang; die Dichteformel ist kein V-Baryonennachweis.

## Eigene Vorschläge für unsere Formeln und Prüfregeln

Die folgenden Formeln sind **eigene Modell- und QA-Vorschläge**, keine bereits implementierten oder bestandenen Ergebnisse. Natürliche Einheiten ħ=c=1.

### 1. Bindung immer gegen alle zugelassenen Fragmentierungen

Für eine festgelegte Theorie, Gitterweite a, Volumen L und exakt erhaltene Quantenzahlen Q:

\[
E_{\rm thr}^{a,L}(Q)=\inf_{\mathcal P\in\mathcal A(Q)}
\sum_{r\in\mathcal P}E_r^{a,L},\qquad
\Delta E^{a,L}=E_{\rm Kandidat}^{a,L}-E_{\rm thr}^{a,L}(Q).
\]

Die zulässigen Partitionen müssen Ladungen, Spin/Parität und gegebenenfalls weitere exakte Symmetrien berücksichtigen. Bei gekoppelten komplexen Feldern sind nicht automatisch die einzelnen Feldladungen erhalten. Für endliche Boxen müssen notwendige Relativimpulse und Wechselwirkungen der Fragmente berücksichtigt werden; die Summe isolierter Ruhenergien ist die asymptotische Schwelle. Beide Seiten mit gleichem Regulator berechnen, dann Volumen- und Diskretisierungsfehler getrennt bestimmen. Nur robust negatives ΔE belegt Bindung gegenüber den geprüften Kanälen. Resonanzen benötigen eine Streu-/Polanalyse.

### 2. Topologische Ladung und fermionische Statistik getrennt definieren

Eine mögliche SU(2)-Erweiterung benötigt ein normiertes Feld U und eine festgelegte Orientierung. Zum Beispiel mit Lᵢ=U∂ᵢU†:

\[
B_{\rm top}=-\frac1{24\pi^2}\int d^3x\,
\epsilon_{ijk}\operatorname{tr}(L_iL_jL_k).
\]

Diese Größe ist dimensionslos. Ihre Identifikation mit Baryonzahl ist eine zusätzliche physikalische Zuordnung. Bei Feldnullstellen oder nicht fixiertem Rand ist eine beliebige Normierung vorhandener Skalarfelder nicht automatisch zulässig. Auf V benötigt die Ladung eine geometrisch konsistente Diskretisierung und Konvergenzprüfung.

Ein klassisches B=1-Profil ist noch kein Spin-½-Zustand. Erst eine begründete Quantisierung mit geeigneter Konfigurationsraumtopologie und Finkelstein–Rubinstein-/WZW-Bedingung kann etwa eine Minusphase unter 2π-Rotation verlangen. Diese Bedingung darf nicht aus B=1 allein postuliert und anschließend als Resultat ausgegeben werden.

### 3. Kollektive Rotationen ergänzen — erst nach der klassischen Stabilitätsprüfung

Für geeignete langsame Rotationskoordinaten Ω:

\[
L_{\rm coll}=-E_{\rm cl}+\tfrac12\Omega_a\Lambda_{ab}\Omega_b,
\qquad H_{\rm rot}=\tfrac12\hat J_a(\Lambda^{-1})_{ab}\hat J_b.
\]

Λ hat Dimension Energie⁻¹. Nur beim isotropen Rotor reduziert sich dies auf J(J+1)/(2Λ). Der erlaubte Quantenzahlensatz und zusätzliche Isorotationen/Kreuzterme sind gesondert herzuleiten. Auf V misst die Abweichung von isotroper Λ auch Gitteranisotropie. Die Rotation erweitert das Modell; sie korrigiert nicht rückwirkend eine rein klassische Energie zu einer gemessenen Baryonenmasse.

### 4. Dimensionsabhängige Zustandszählung und konsistente Abschirmung

Für ein freies fermionisches Modell mit tatsächlich nachgewiesener Entartung g:

\[
\sigma_{2D}=\frac{gk_F^2}{4\pi},\qquad
n_{3D}^{\rm homogen}=\frac{gk_F^3}{6\pi^2},\qquad
n_{3D}^{\rm Schichten}=\frac{\sigma_{2D}}{d}.
\]

Die erste Größe hat Dimension Energie², die beiden anderen Energie³. Die Schichtformel ersetzt keine homogene dreidimensionale Zustandszählung. Fermionische Entartung, Dispersion und effektive Dimension dürfen nicht durch Anpassung an gewünschte Baryonenzahlen gewählt werden.

Bei einer eigenen lokalen Wechselwirkungsenergiedichte εint=G n²/2 folgt konsistent μint=∂εint/∂n=G n. Ein Rezept, das zunächst Potentialenergie pro Teilchen benutzt und anschließend nochmals variiert, kann einen Faktor zwei verlieren. Für mehrere Spezies ist die statische Abschirmung allgemeiner über Ladungen qi und Suszeptibilitätsmatrix χij=∂ni/∂μj zu definieren: mD²=Σij qi χij qj. Vor Anwendung müssen festgehaltene Hintergrundgrößen, Neutralitätsbedingungen und statischer Grenzübergang feststehen.

## Umfang der empfohlenen Änderung

Jetzt sinnvoll: Literaturverweise, präzisere Schwellen-/Statistikdefinitionen und neue Prüfkarten. Noch nicht gerechtfertigt: Austausch unseres getesteten Potentials gegen Quark- oder ChPT-Parameter, Hochsetzen von Fortschrittsprozenten, oder Übernahme von Screeningkoeffizienten ohne unabhängige Herleitung. Keine numerischen Tests ausgeführt.
