# HIGGS-MODES-1: keine negative Energierichtung im geprüften Portalzweig

08.10.2026 · [E] neue CUDA-Eigenwertrechnung an den vollen stationären Profilen aus [HIGGS-MINIMA-1](../higgs-minima-20261008/ERGEBNIS.md).

**Die zweite Energievariation ist in allen acht untersuchten Sektoren nach Abzug der identifizierten Symmetrierichtungen positiv aufgelöst.** Geprüft wurden Amplituden einschließlich Higgsantwort und beide Phasenrichtungen für die Winkelordnungen l=0,1,2,3, jeweils auf drei Radialgittern. Damit sind auch gegensinnige Komponentenänderungen, relative Phasen und nicht-kugelsymmetrische Störungen enthalten, die die vorherigen Relaxationsstarts nicht geprüft hatten.

![Energiekrümmungen und Symmetrierichtungen](mode-spectrum.svg)

Dies ist ein begrenzter **energetischer Stabilitätsbefund** bei fester gemeinsamer Ladung. Die Zahlen sind keine dynamischen Schwingungsfrequenzen und keine Teilchenmassen. Es wurde keine Zeitentwicklung gerechnet.

## Umfang und vorab festgelegte Entscheidung

Ein Parameterpunkt: eta=0,05, g=0,005, c8=0, Q=600. Ausschließlich volle Portaltheorie, jeweils seed=0 aus dem vorherigen Lauf. Basis R=20,h=0,05; fein R=20,h=0,025; Box R=30,h=0,05. Keine erneute Relaxation und keine Parameteranpassung.

Pro Gitter vier Winkelordnungen und zwei Sektoren, zusammen **24 symmetrische Matrizen**. Der reelle Sektor hat drei radiale Felder (zwei Materieamplituden und Higgs), der imaginäre zwei. Für jedes l sind die 2l+1 Winkelrichtungen entartet. Das ist die harmonische Zerlegung von Störungen im **dreidimensionalen Raum**, kein räumlich eindimensionales Modell.

Die vollständigen diskreten Matrizen wurden diagonalisiert; die acht niedrigsten Eigenwerte samt Komponentenanteilen und Prüfgrößen sind gespeichert. Das Minimum des Gesamtspektrums und die Anzahl der Werte unter -1e-6 sind ebenfalls gespeichert. **Keine Matrix enthält einen Wert unter -1e-6.**

Nach den [Vorabkriterien](PLAN.md) muss der niedrigste nicht als Symmetrie identifizierte Wert auch nach Abzug des doppelten beobachteten Gitter-/Boxunterschieds über 1e-6 liegen. Alle acht Sektoren bestehen dieses Pilotkriterium. Es ersetzt keine rigorose Kontinuumsfehlerschranke.

| Sektor | l | Basis | Feines Gitter | Größere Box | Einordnung |
|---|---:|---:|---:|---:|---|
| Amplituden + Higgs | 0 | 0,485108 | 0,485079 | 0,485101 | positiv |
| Phasen, ohne gemeinsame Drehung | 0 | 0,100000 | 0,100000 | 0,100000 | positiv |
| Amplituden + Higgs, ohne Verschiebung | 1 | 0,558503 | 0,558491 | 0,525455 | positiv |
| Phasen | 1 | 0,304743 | 0,304751 | 0,304743 | positiv |
| Amplituden + Higgs | 2 | 0,284302 | 0,284281 | 0,284302 | positiv |
| Phasen | 2 | 0,579594 | 0,579582 | 0,538749 | positiv |
| Amplituden + Higgs | 3 | 0,617903 | 0,617888 | 0,556292 | positiv |
| Phasen | 3 | 0,623907 | 0,623894 | 0,556372 | positiv |

Dimensionslose Eigenwerte der normierten zweiten Energievariation. Einige höhere Sektoren zeigen deutliche Boxabhängigkeit. Ihr Vorzeichen ist im Pilotvergleich robust; die einzelnen Werte sind damit noch nicht als isolierte physikalische Eigenmoden im unendlichen Raum gesichert. Die Balken in der Grafik zeigen die beobachtete Gitter-/Boxspanne, keine statistischen Unsicherheiten.

## Symmetrien werden geprüft, nicht blind entfernt

Die gemeinsame U(1)-Phasendrehung ist eine erwartete Nullrichtung. Ihre quadrierte Überlappung mit dem niedrigsten imaginären l=0-Eigenvektor beträgt auf allen Stufen mehr als 0,99999999999999. Die zugehörigen Eigenwerte liegen zwischen 6,3e-14 und 3,6e-9. Das verbleibende kleine Phasenresiduum folgt auch aus der endlichen Genauigkeit der stationären Ausgangsprofile.

Die Verschiebung des ganzen Objekts liegt im reellen l=1-Sektor. Ihr Eigenwert fällt von **2,78591e-5 auf 6,96432e-6**, wenn h halbiert wird — ungefähr Faktor vier. Die größere Box ergibt 2,78574e-5. Die quadrierte Überlappung mit dem aus dem Profil abgeleiteten Verschiebungsvektor liegt über **0,99999989**. Beide Symmetrierichtungen bestehen die vorher festgelegte Diagnose. Die Translation hat im endlichen diskreten Problem einen kleinen positiven Wert; ein exakt translationsinvariantes Kontinuum wird damit nicht behauptet.

Die **relative Phase** ist dagegen keine Symmetrie: eta koppelt die beiden Materiefelder. Ihre niedrigste Energiekrümmung beträgt hier ungefähr **0,1 = 2 eta**. Der zugehörige Eigenvektor ist antisymmetrisch zwischen den Komponenten. Ebenso ist die niedrigste reelle radiale Richtung antisymmetrisch; sie hat auf dem feinen Gitter **0,485079** und praktisch keinen Higgsanteil. Die zuvor offene gegensinnige Komponentenstörung ist damit ausdrücklich enthalten.

[M] Für den hier symmetrischen Hintergrund u1=u2 zerfällt der Phasenoperator in gleiche und gegensinnige Komponenten. Die beiden Operatoren unterscheiden sich um 2 eta. Aus der gemeinsamen Phasen-Nullrichtung folgt daher die relative Phasenkrümmung 2 eta, bis auf den numerischen Stationaritätsfehler. Das ist eine Konsistenzprüfung des Portalmodells, keine Herleitung einer schwachen Eichbosonmasse.

## Welcher Operator gerechnet wurde

[M] Die räumliche Energie bei optimierten Zeitimpulsen und fester gemeinsamer Ladung enthält `Q²/(4I)`, mit `I=4πh sum(u_i²)` und `omega=Q/(2I)`. Für radial reelle Störungen erzeugt dessen zweite Ableitung neben dem lokalen Term `-omega²` eine positive Rang-eins-Korrektur. Für l>0 verschwindet die erste Variation von I durch das Winkelmittel; dann bleibt nur der lokale Beitrag.

Mit `rho_i=(u_i/r)²`, `S=rho1+rho2`, `y=y0+z/r`, `D=y²-y0²`, `b=g/0,01=0,5`, `a=125²/(2*246²*0,01)`, `y0=0,492`:

```
L_l = -d²/dr² + l(l+1)/r²
W_i = 1 - 2 rho_i + 1,5 rho_i² - 0,5 rho_j + b D/2 - omega²

H_imag,ii = L_l + W_i
H_imag,12 = -eta

H_real,ii = L_l + W_i - 4 rho_i + 6 rho_i²
H_real,12 = -eta - u1*u2/r²
H_real,HH = L_l + a*(3 y²-y0²) + b*S
H_real,iH = sqrt(2)*b*y*u_i/r

zusätzlich nur bei l=0 im reellen Sektor:
H_Q = 4 omega² U U^T / sum(u_i²), U=(u1,u2,0).
```

Die normierten Variablen sind `(u1,u2,z/sqrt(2))` beziehungsweise die zwei imaginären Singulettamplituden. In der radialen Normierung entspricht H dem Energiehessian geteilt durch 8πh. Bei l>0 wird die entsprechende quadratische Winkelvariation betrachtet. Radiale Endpunkte sind null; die Singularbarriere l(l+1)/r² und die Gitterverfeinerung behandeln das Verhalten am Ursprung in der gewählten Finite-Differenzen-Diskretisierung.

Für l>=1 unterscheiden sich die reellen Operatoren nur durch den positiven Zentrifugalterm; dasselbe gilt für die imaginären. **Auf denselben endlichen Gittern** liegt daher für l>3 keine niedrigere Eigenwertunterkante als bei l=3 vor. Das ist eine analytische Folgerung aus der Matrixstruktur, keine zusätzliche Eigenwertrechnung und keine bewiesene Übertragung auf das Kontinuum.

## Numerische Kontrollen

Alle vorab festgelegten Kontrollen bestanden:

- Analytische Hessianwirkung gegen unabhängige Autograd-Hessian-Vektorprodukte einer deterministischen glatten Probe in allen fünf Feldrichtungen: maximaler relativer Fehler **6,06e-14**. Für l=0 volle Fix-Q-Energie, für l>0 Grandpotential bei festem omega plus quadratischer Winkelterm.
- Absolutes Residuum der acht niedrigsten Eigenpaare: maximal **3,32e-11**.
- Orthogonalitätsfehler: maximal **4,48e-15**.
- Phasen-Ward-Residuum `||H U||/||U||`: maximal **1,35e-8**.

CUDA float64 auf Quadro P5000, Torch 2.5.1+cu121, cuSOLVER. Eigenwertlauf rund **9,51 s**, begrenzter Dienst einschließlich Start **12,306 s**. CPU nur Steuerung, Datei-I/O, skalare Zusammenfassung und Matplotlib. Gemeinsamer GPU-Lock und freigegebene Ressourcenpacht; bestehende Dienste blieben unverändert. Kein CPU-Fallback für Hessians, Normen oder Eigenwerte.

## Literaturabgleich und Grenzen

[S] Chen, Andersson und Li entwickeln in [arXiv:2509.18656v1, Abschnitt 3.1, Gleichungen 18–21](https://arxiv.org/html/2509.18656v1#S3.SS1) ein dynamisches Störungsproblem mit gekoppelten Seitenbändern, Winkelharmonischen und frequenzabhängigen Termen. Diese Passage wurde für die methodische Abgrenzung gelesen. Unser selbstadjungierter Fix-Q-Energiehessian ist ein anderer Operator; seine Eigenwerte dürfen nicht ohne weitere Herleitung als deren dynamische Frequenzen interpretiert werden. Zudem behandelt die Arbeit ein anderes Feldmodell.

[S] [Smolyakov, arXiv:1711.05730v2](https://arxiv.org/abs/1711.05730v2), hier Abstract gelesen, weist auf nötige Beiträge höherer Störungsordnung bei Ladung und Energie zeitabhängiger Moden hin. Daraus übernehmen wir keine numerischen Resultate und behaupten keinen bereits geprüften dynamischen Energieerhalt.

[E] Der neue Befund stützt lokale energetische Stabilität des ausgewählten Portalzweigs gegenüber den untersuchten infinitesimalen Richtungen. Die Prüfung betrifft **die volle Theorie**, nicht die Hessians von E3/Ecomp. Offen bleiben die Übertragung auf weitere Parameter, die dynamische Modenrechnung, endliche Störungen, Langzeitentwicklung und die Übertragung auf V. Positive zweite Variation beweist weder globale Minimalität noch Stabilität gegen alle endlichen Fissionsprozesse.

Das zugrunde liegende Modell enthält zwei komplexe Singuletts und eine reale Higgsamplitude. Keine chirale Materie, elektroschwachen Eichfelder oder Hadronenquantenzahlen wurden hinzugefügt. Die Fortschrittsschätzungen bleiben Higgs 2 %, schwache Kraft 2 %, Mesonen/Baryonen 10 %.

## Reproduzierbarkeit und nächster Schritt

[Vorabplan](PLAN.md) · [Rechencode](run.py) · [Auswertung und Grafik](analyse.py) · [Eigenwerte, Symmetrieüberlappungen und Komponentenanteile](results/RESULT.json) · [QA](results/QA.json) · [Gruppenentscheidungen](SUMMARY.json) · [Laufstatus](results/STATUS.json) · [Provenienz](results/PROVENANCE.json) · [Exportänderung](EXPORT.json).

Die unveränderte [Eingabe aus HIGGS-MINIMA-1](../higgs-minima-20261008/results/RESULT.json) hat SHA256 `a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9`. Für Wiederholungen PLAN.md, run.py und analyse.py in einen frischen Nachbarordner des Eingabeordners kopieren. `python run.py` erfordert CUDA und verweigert einen bestehenden results-Ordner; danach erzeugt `python analyse.py` die Zusammenfassung und Grafik. Im Export wurde nur der Eingabepfad angepasst; Original- und Exporthash bleiben dokumentiert.

Die Verbindungsideen haben jetzt zwei getrennte Befunde: **Idee 1** liefert eine kontrollierte reduzierte statische Energie; **Idee 3** hat für den vollen Pilotzweig eine Prüfung der energetischen Störrichtungen. Ein sinnvoller nächster Test ist, ob die reduzierten Energien auch diese zweiten Variationen und Symmetrierichtungen bewahren. Erst dann lässt sich ihre Eignung für eine reduzierte Stabilitätsanalyse beurteilen. Dieser Folgetest ist noch nicht gerechnet.
