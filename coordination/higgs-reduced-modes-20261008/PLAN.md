# HIGGS-REDUCED-MODES-1: radialer statischer Krümmungsvergleich

Vorabplan 08.10.2026. Vergleich E3/Ecomp gegen statisch mitreagierendes Higgs
in der vollen Theorie. Ausschließlich l=0, beide Materieamplituden und
beide Phasen; keine reduzierte Winkelrechnung. Ausgangspunkt 9dcebf0.
Je eigene stationäre Profile (seed=0) aus HIGGS-MINIMA-1, g=.005 eta=.05
c8=0 Q600, base/grid/box. Keine neue Relaxation, kein Parameterfit.
Input SHA256 a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9.

Referenz: voller reeller Fix-Q-Hessian in normierten Variablen
(u1,u2,z/sqrt(2)). Matter-Schur-Komplement S=A-B C^-1 B^T,
C=Higgs-Higgs-Block. Positivität von C prüfen; bei nichtpositivem C stoppen.
Dieser Operator beschreibt die statische Higgs-Mitreaktion und ist weder
das volle gekoppelte Spektrum noch ein dynamisches Frequenzquadrat.
Imaginärer Sektor entkoppelt auf reellem Hintergrund bereits vom Higgs.

Reduzierter reeller Hessian durch vollständige doppelte Autograd-Ableitung
von E3/Ecomp, geteilt durch 8πh; keine naiv eingesetzte Kraft. Imaginärer
Operator aus dEH/dS und den übrigen Potentialtermen. Die Energie hängt vom
Higgs nur über die festgelegte Dichtefunktion ab; eta mischt die Phasen.

QA: Symmetrie der Rohhessians maximal absolut <1e-8, anschließend
numerisch symmetrisieren. Unabhängige zentrale Differenzen des Gradienten
in deterministischer glatter Richtung mit eps=.001,.0005,.00025;
relativer HVP-Fehler beim kleinsten Schritt <1e-5 für E3/Ecomp real und imag.
Schur-Solve-Residuum relativ <1e-10. Eigenresiduum niedrigster 8 Paare
absolut <1e-7; Orthogonalität <1e-10. Gemeinsame Phase: Quadratoverlap>.95,
|lambda|<1e-6; sonst unentschieden, keine Entfernung nach Augenmaß.

Vergleich der acht niedrigsten reellen und sieben niedrigsten nichttrivialen
imaginären Eigenwerte, sortiert und zwischen Modellen auf derselben Stufe
zugeordnet. Relative Fehler bezogen auf jeweils vollen statischen Referenzwert.
Gate je reduziertem Modell: alle nichttrivialen Eigenwerte positiv >1e-6;
max relativer Spektralfehler über beide Sektoren/Stufen plus Drift <=5%,
Drift=max Änderung desselben Fehlerindexes grid-base,box-base <=.005.
Bei fehlender QA/Phasendiagnose: unentschieden. Zusätzlich Eigenvektor-
Quadratoverlaps und relative Frobeniusnorm der Operatorabweichung berichten;
diese haben keinen zusätzlichen Freigabewert. Boxabhängige Moden nicht als
isolierte Teilchenanregungen interpretieren. Alle Ergebnisse veröffentlichen.

CUDA float64 P5000 für Hessians, Matrixlöser, Normen, Eigenwerte.
CPU nur IO, Steuerung, skalare Zusammenfassung, Grafik. Halbe Ressourcenpacht,
bestehender GPU-Lock, CPU100%, RAM2G, RuntimeMaxSec600. Dienste unverändert.
Grenzen: statischer radialer Pilot eines Parameterpunkts; keine zeitliche
Higgsantwort, Winkelmoden reduzierter Modelle oder nichtlineare Stabilität.
