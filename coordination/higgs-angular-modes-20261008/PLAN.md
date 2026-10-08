# HIGGS-ANGULAR-MODES-1: reduzierte winkelabhängige zweite Variation

Vorabplan 08.10.2026; Anschluss b55eff4. Noch keine Ergebnisse.
Eigene stationäre MINIMA-Profile full/E3/Ecomp, seed0, g=.005 eta=.05 c8=0
Q600, drei Gitter. Keine neue Relaxation. Input SHA256
 a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9.

Winkelordnungen l=1 und l=2, reelle und imaginäre Materiestörungen:
36 Matrizen (3 Modelle x3 Gitter x2 Winkel x2 Sektoren).
Volle Referenz: Schur-Komplement mit winkelabhängigem Higgsblock.
Reduzierte Referenz: exakte zweite Variation der definierten E3/Ecomp-
Funktionale. Dichte S=S0+eps*s1*Y_l+eps²*s2*Y_l², mit Winkelmittel
<Y_l>=0, <Y_l²>=1. Higgsantwort jeweils Hintergrund, erste Winkelvariation
mit K_l^-1 und gemittelte zweite Variation mit K_0^-1. Alle Kreuz- und
Kettenregelterme beibehalten. Keine bloße Zentrifugaladdition an einen
fertigen radialen Amplitudenhessian. Imaginäre Störungen haben s1=0.

Unabhängige QA der quadratischen Expansion: direkte endliche Winkelenergie
mittels Legendre-Zerlegung bis L=8 und 24-Punkt-Gauß-Legendre-Quadratur,
alles CUDA. Dies reicht für S und die definierte Antwort chi1+chi2 bei l<=2.
Energie differenzieren mit eps=.003,.0015,.00075 in einer glatten
vorab definierten Störrichtung; kleinster Schritt relativer Krümmungsfehler
<1e-4, beide reduzierte Modelle, beide Winkelordnungen, beide Sektoren,
auf Basisgitter. Vollständige Schrittfolge berichten.
Zusätzlich radiale l=0-Jet-HVP gegen direkte Autograd der alten Energie
mit Fix-Q-Rangterm, relativ <1e-9 auf allen Gittern; keine erneute radiale
Spektralrechnung. Quadraturorthogonalität <1e-12; lineare Löser Residuum
<1e-10; rohe Hessianasymmetrie <1e-8; Eigenresiduum <1e-7,
Orthogonalität <1e-10. QA-Abbruch vor Einordnung dokumentieren.

Translationsdiagnose nur real l=1: quadrierter Überlapp >.95 mit r*F',
|lambda_fein|<=.4|lambda_basis|+1e-6 und Boxverschiebung
<=max(.1|lambda_basis|,1e-6). Sonst unentschieden, keine manuelle Entfernung.
Niedrigste acht Eigenpaare pro Matrix speichern; Translation separat.
Vergleich aller verbleibenden Werte nach sortierter Reihenfolge zwischen
Modellen auf derselben Stufe. Relative Fehler zur vollen statischen Referenz.
Gate je reduziertem Modell: übrige Eigenwerte >1e-6, alle QA/Translation
bestanden, max relativer Fehler über Sektoren und Stufen + Drift <=5%,
Drift=max Änderung desselben Fehlerindexes grid-base,box-base <=.005.
Eigenvektorüberlappungen zusätzlich berichten, kein verstecktes Zusatzgate.

CUDA float64 P5000; CPU IO/Steuerung/skalare Tabellen/Grafik. Gemeinsamer
GPU-Lock, halbe Pacht, CPU100%, RAM2G, RuntimeMaxSec900; Dienste unverändert.
Alle negativen Werte und Fehler veröffentlichen. Keine dynamischen
Frequenzen, keine Langzeitstabilität, kein weiterer Parameterpunkt, kein V.
