# HIGGS-RESPONSE-1: eingefrorener Auswertungsplan

08.10.2026. Neue Diagnose vorhandener B13-Profile, keine erneute Relaxation.
Eingabe: B13 results/RESULT.json, SHA256
1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d.
Alle 24 gespeicherten Profile verwenden; keine Auswahl nach Ausgang.

Vergleich bei festgehaltenen Singuletts und identischer radialer Quadratur:
Referenz gespeichertes volles Higgsprofil; N nichtlokale lineare Antwort;
L lokale lineare Antwort; P punktweise exakte Potentialminimierung ohne Gradient.
N löst (-d²/dr²+6.25) z = -b*y0*r*S mit z=r*chi, z(0)=z(R)=0.
L: chi=-b*y0*S/6.25. P: chi=sqrt(max(y0²-b*S/a,0))-y0.
Alle Näherungen anschließend im vollständigen diskreten Higgs-Energiefunktional
bewerten, einschließlich Gradienten. Keine Neuoptimierung der Singuletts.

Messgrößen: volumenbezogener relativer L2-Fehler von chi; relativer Fehler im
Higgs-Energiebeitrag gegen die Referenz (nicht relativ zur viel größeren
Gesamtenergie); vollständiges Gleichungsresiduum relativ zur linearen Quelle;
maximale |chi|/y0, maximale b*S/6.25, relative Fehler der Kernabsenkung.
5%-Pilotkriterium gilt gemeinsam für L2- und Higgs-Energiefehler.
Pro Parametergruppe werden base/grid/box verglichen: d=max der absoluten
Änderungen dieser beiden Fehlermaße grid-base und box-base. d ist ein
beobachteter Diskretisierungsindikator, keine rigorose Schranke.
Brauchbar: max aller Fehler+d <=.05 und d<=.005.
Unzureichend: min über Stufen von max(L2,Energiefehler)-d >.05 und d<=.005.
Sonst unentschieden. Kriterien bleiben nach dem Ergebnis unverändert.

QA vor Auswertung: FFT-Inverse gegen dichten unabhängigen CUDA-Solve und
Sinus-Eigenmode; Higgs-Energiegradient per Autograd gegen Gleichung;
b=0 ergibt verschwindende Antwort/Energie. Toleranz 1e-10 für relative
Operator-/Gradientenprüfungen; Nullantwort <1e-12 absolut.
Referenz muss positive Higgsamplitude und negative Higgs-Korrektur besitzen;
Quellnorm und Korrektur dürfen für relative Größen nicht null sein.
Referenzresiduum wird berichtet, nicht aus bereits bestandenen Altgates erfunden.

Rechenort .69, P5000 CUDA float64, ein CPU-Thread für Steuerung/I/O.
Maximal 1 CPU-Äquivalent, 2 GiB RAM, 120 Sekunden, eine halbe GPU-Pacht,
exklusiver vorhandener gauntlet-gpu.lock; keine Änderungen fremder Dienste.
GPU-Analyse kleiner Arrays, keine CPU-Numerik als Ersatz. Die vorhandene
platz-Steuerung wird als private Kopie auf dem Rechenhost mit lokaler I/O
statt SSH-zu-sich-selbst verwendet; keine systemweite Installation.
Quell-, Plan- und Eingabehashes sowie tatsächlicher Rechenweg werden gespeichert.
Grenzen: radialer 3D-Stationärvergleich, kein 1D-Modell, kein Stabilitätsbeweis,
keine dynamische Gültigkeit oder Nachweis eines zusätzlichen Teilchens.
