# Analytische Bausteine aus dem vorhandenen Portalmodell

[M] Eigenständige Herleitungen auf Papier aus dem gelesenen B13-Plan und `engine.py`. Keine neue Numerik, keine Lean-Kompilierung, kein unabhängiger Beweisreview. Geltungsbereich: klassisches Baumpotential, zunächst feste Geometrie. Historische Befunde: [Bestandsaufnahme](../higgs-bestandsaufnahme-20261007/BESTAND.md).

## A. Tatsächliche Wirkung und Symmetrie

Mit rho_i = |psi_i|², S = rho_1 + rho_2, D = y² − y0² lautet das implementierte Potential:

```text
V = Σ_i [rho_i − rho_i² + rho_i³/2 + c8*lambda*rho_i⁴/4]
    − rho_1*rho_2/2 − 2*eta*Re(conj(psi_1)*psi_2)
    + a*D²/4 + b*D*S/2.

a = mh²/(2*v²*lambda), b = g/lambda, y0 = sqrt(lambda)*v/m.
L_kin = Σ_i |∂psi_i|² + (∂y)²/2.
```

B13 verwendet m=50 GeV, lambda=0,01, mh=125 GeV, v=246 GeV. B17 hat eta=0,1 und g=0,001; B16 verwendet g=0,005. Diese Familien dürfen nicht parameterblind verglichen werden.

Unter psi_i → exp(i alpha) psi_i bleibt V invariant. Separate Phasen alpha_1 und alpha_2 verändern bei eta≠0 den Mischterm. Ebenso ist der Singulett-Doppelpack nicht SU(2)-invariant: Summe der rho_i² und rho_i³ sowie der Mischterm wählen innere Richtungen. Zwei komplexe Komponenten sind deshalb kein bereits implementiertes schwaches Dublett.

## B. Exakte punktweise Elimination der Higgsamplitude

Für festes S≥0 und a>0 setze z=y²≥0. Der y-abhängige Teil ist eine konvexe quadratische Funktion von z. Für b>0 gilt:

```text
z_* = max(0, y0² − (b/a) S),
S_c = a*y0²/b,
min_y V_H = −b²*S²/(4a)                         für S≤S_c,
            a*y0⁴/4 − b*y0²*S/2                 für S≥S_c.
```

Herleitung: Ableitung nach z gleich a(z−y0²)/2+bS/2; der unbeschränkte Minimierer wird auf z≥0 projiziert. Beide Zweige und ihre ersten Ableitungen stimmen bei S_c überein. Für b=0 ist min V_H=0. Mit den B13-Konventionen ist a*y0²=3,125, also S_c=31,25 bei g=0,001 und S_c=6,25 bei g=0,005.

**Reichweite:** Dies minimiert die lokale Potentialdichte, nicht das gesamte Feldfunktional. Der Gradient von y kostet Energie. Weglassen dieses positiven Beitrags liefert eine untere Energieschranke, aber keine exakte räumliche Lösung. Insbesondere beweist z_*=0 in einer lokalen Näherung keinen existierenden Higgs-Beutel.

## C. Kontrollierte schwache, statische Higgsantwort

Schreibe y=y0+chi. Zur führenden Ordnung in einer schwachen Quelle J=b*y0*S:

```text
E_chi = 1/2 <chi, K chi> + <J,chi> + höhere Terme,
K = −Δ + M_H²,       M_H² = 2*a*y0² = (mh/m)² = 6,25.
chi_* = −K^(-1) J,
ΔE_eff = −1/2 <J,K^(-1)J>.
```

K ist für die geeigneten periodischen oder abklingenden Randbedingungen positiv. Somit ist die führende Energieänderung nichtpositiv. Bei räumlich getrennten positiven Dichten erzeugt der positive massive Green-Kern einen attraktiven Kreuzterm in dieser Näherung. Nicht behauptet ist eine universelle Kraft bei starker Überlappung oder beliebigen Phasen.

Die Entwicklung vernachlässigt unter anderem b*S*chi²/2 und kubische Higgs-Terme. Kleine |chi|/y0 allein reicht als universelle Fehlerkontrolle nicht; auch b*S/M_H² und die räumlichen Frequenzen sind zu prüfen. Der lokale Grenzfall K^(-1)≈M_H^(-2) reproduziert −b²*S²/(4a). Bei einer Absenkung nahe 25 % ist eine ungeprüfte lineare Ersetzung besonders fragwürdig.

In d Raumdimensionen lautet der Fouriermultiplikator 1/(k²+M_H²). Die Ortsraum-Kerne unterscheiden sich: exp(−M_H|x|)/(2M_H) in 1D, K0(M_H r)/(2π) in 2D und exp(−M_H r)/(4πr) in 3D. Diese Standardkerne sind durch Fourierinversion bzw. das zugehörige Fundamentalproblem definiert; die Nullabstands-Singularität verlangt bei ausgedehnten Quellen Integration. Auf endlichen Gittern ist der diskrete Operator maßgeblich. Ein radialer 3D-Kern ist kein 1D-Modell.

## D. Ladungs- und Dimensionsschranke

Angenommen V≥delta*S mit delta>0 und positive räumliche Kinetik. Dann in jeder räumlichen Dimension mit denselben normierten Feldern:

```text
E ≥ ∫ Σ_i (|dot psi_i|² + delta |psi_i|²)
  ≥ 2 sqrt(delta) ∫ Σ_i |psi_i| |dot psi_i|
  ≥ sqrt(delta) |Q|,
Q = 2 Im ∫ Σ_i conj(psi_i) dot psi_i.
```

Das erste Ungleichheitszeichen verwirft positive Beiträge, das zweite folgt aus einem Quadrat, das dritte aus Dreiecksungleichung und |Im z|≤|z|. Die vorhandene hinreichende delta-Schranke bleibt eine Voraussetzung, die bei neuen Termen neu zu prüfen ist. Die physikalische Umrechnung E_phys=(m/lambda)E und Q_phys=Q/lambda ist hier die **3D-Projektnormierung**; sie wird nicht unverändert auf dimensionell andere Theorien übertragen.

Für die B13-Benchmarks ist delta>0,10 dokumentiert. Daraus folgt in 3D E_phys>m*sqrt(0,10)*|Q_phys|, also mehr als etwa 15,8 GeV je Ladungseinheit bei m=50 GeV. Für Q_total=0 ist diese spezielle Schranke leer; daraus folgt weder ein masseloses Objekt noch ein stabiler Neutralverbund. Unter denselben positiven Voraussetzungen hat der statische Q=0-Minimierer das Vakuum als globalen Minimalzustand.

## E. Fest-Q-Virialbedingung in d Dimensionen

Für lokalisierte Kontinuumsprofile und Größenänderung x→x/s gilt bei festem Q:

```text
E_Q(s) = s^(−d) A + s^(d−2) T + s^d V,
A = Q²/(4 I), I = ∫S,
(d−2) T + d V − d A = 0  am stationären Punkt.
```

In 1D: −T+V−A=0; in 2D: V−A=0; in 3D: T+3V−3A=0. Dies ist eine notwendige Stationaritätsbedingung, keine hinreichende Existenz- oder Stabilitätsbedingung. Endliche Boxen und Gitter brechen die exakte Skalierung.

## F. Formulierung einer vollständigen Störungsprüfung

Für psi_i=exp(i omega t)(f_i+u_i+i v_i) und y=y_*+chi ist die Dynamik im mitrotierenden Rahmen gekoppelt. Zur Quadratik gehören alle reellen u_i, v_i, chi und ihre Impulse. Die zweite Variation des reduzierten E_Q beurteilt die eingeschränkte stationäre Energiefrage. Die dynamischen Wachstumsraten benötigen zusätzlich den Hamiltonschen linearen Operator, einschließlich omega-abhängiger Kopplungen. Eigenwerte eines beliebigen Potential-Hessians sind nicht automatisch Teilchenmassen.

Bei gleicher Amplitude f ist der Mischterm −2 eta f² cos(theta_rel). Seine quadratische Änderung ist +eta f² theta_rel² für eta>0. Das spricht gegen eine pauschale Behauptung einer instabilen relativen Phase. Räumlich variierende, amplitudengemischte Störungen bleiben trotzdem zu prüfen. Gemeinsame U(1)-Phase und Translationen erzeugen erwartete Nullrichtungen bzw. Gitterreste, die von echten Instabilitäten getrennt werden müssen.

## Herkunft

Gelesene Projektdateien, SHA256 zur Wiederauffindbarkeit:

```text
337eee726a25ff8f3269214929d3f5ee9f8de45a37961cff5e1127d7dd4fa87c  model-lab/simulation-environment/field3d/engine.py
b3d7239d5eb19ff9c43b6ba965639eff51d673bfa73459e6e92e63e792a14091  coordination/field-higgs-portal-20260925/PLAN.md
bfb11366837ea8f08a5317d5a375ceee195f37cc4d3b8def910f04e5480d4d52  coordination/field-fixedq-20260925/review/ANALYTIC.md
02a81bf02139508810d07c8c12928053983c1241cad1375361891dff98c9d3d2  coordination/field-retention-20260926/BEFUND.md
eec83602c6d4e4b7efb6416eeef628bb78539c5fbe8668b367773bf80ad958dc  coordination/field-next-20260925/flux/THEORY.md
```

Ein Hash bindet die gelesene Datei, bestätigt aber nicht ihre Physik. Die Gleichungen A–F sind explizite Zwischenresultate der Analyse; sie wurden nicht durch den OpenAI-Math-Release bewiesen.

## G. Dynamische und quantisierte Erweiterungen — Nachtrag 08.10.2026

Die statischen Herleitungen A–F bleiben bestehen. Der [neue Formelabgleich](../literatur-formeln-20261008/FORMEL-ABGLEICH.md) leitet die zeitabhängige Higgsantwort, das gekoppelte Amplituden-/Phasenproblem, die Zusatzträgheit und den Unterschied zwischen Fix-Q- und dynamischem Operator her. [Quanten- und thermische Erweiterungen](../literatur-formeln-20261008/QUANTEN-PORTAL.md) benötigen eigene Kovarianz-, Ladungs- und Matchingkonventionen. Dies sind analytische Vorschläge, keine nachträglich veränderten oder neu ausgeführten Rechenergebnisse.
