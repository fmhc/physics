# HIGGS-MODES-1: zweite Energievariation des vollen Portalzweigs

Vorabplan 08.10.2026, Ausgangspunkt HIGGS-MINIMA-1 (7331499).
Nur volle Theorie, seed=0, eta=.05, g=.005, c8=0, Q=600.
Archivierte Basis-/Feingitter-/Boxprofile unverändert; keine neue Relaxation.
Input RESULT.json SHA256 a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9.

Zweite Variation der Energie bei fester gemeinsamer Ladung Q, keine
Zeitentwicklungsfrequenzen. Reelle Amplituden und Higgsantwort (3 Felder)
sowie imaginäre Singulettstörungen (2 Felder) getrennt. Sphärische
Harmonische l=0,1,2,3, Entartung 2l+1; 24 symmetrische Matrizen insgesamt.
Normierte radiale Variablen (u1,u2,z/sqrt(2)) und (v1,v2).
H ist Energiehessian geteilt durch 8πh. Nur der reelle l=0-Sektor
enthält die positive Fix-Q-Rang-eins-Korrektur 4omega² U U^T/sum(u²),
U=(u1,u2,0). Für l>0 entfällt sie wegen des verschwindenden Winkelmittels.
Alle Sektoren erhalten l(l+1)/r². Gemeinsame Phase und Translation sind
erwartete Symmetrierichtungen, nicht automatisch zu entfernende Eigenwerte.

QA vor Einordnung: analytische Matrizen gegen unabhängige Autograd-Hessian-
Vektorprodukte der vollen komplexen Energie, deterministische glatte Probe,
relativer Fehler <1e-9. Für l>0 Grandpotential mit festem omega und separat
quadratischem Winkelterm. Eigensolver: niedrigste acht Eigenpaare,
absolutes Residuum <1e-7, Orthogonalitätsfehler <1e-10.
Phasen-Ward-Residuum ||H_phase,0 U||/||U|| <1e-6.
Keine CPU-Eigenwertrechnung: dichte torch.linalg.eigh auf CUDA float64.

Symmetriediagnose: Quadratoverlap >.95 mit gemeinsamer Phase (imag l=0)
oder diskret abgeleitetem Verschiebungsprofil (real l=1).
Phase zusätzlich |lambda|<1e-6 auf allen Stufen.
Translation zusätzlich |lambda_fein| <= .4 |lambda_basis| +1e-6;
Boxverschiebung <= max(.1 |lambda_basis|,1e-6).
Sonst keine Symmetrie-Ausnahme und Einordnung unentschieden.
Eigenwerte und Überlappungen auch bei nicht bestandener Diagnose ausweisen.

Für den niedrigsten nicht als Symmetrie identifizierten Eigenwert jedes
Sektors Drift d=max(|fein-basis|,|box-basis|).
Positiv aufgelöst: min lambda -2d >1e-6.
Negativ aufgelöst: max lambda +2d < -1e-6.
Sonst unentschieden. Das ist eine Pilotentscheidung, kein rigoroser
Kontinuumsnachweis. Alle Rohspektren, auch negative Werte, veröffentlichen.
Zusätzlich antisymmetrischen Materieanteil und Higgsanteil der acht
niedrigsten Eigenvektoren ausweisen. Keine nachträgliche Gateänderung.

GPU-Rechner P5000; gemeinsamer GPU-Lock und halbe Pacht; CPU100%, RAM2G,
RuntimeMaxSec1200. GPU-Speicherbedarf vor Start prüfen; Dienste unverändert.
CPU nur Ablauf, IO, skalare Tabellen und Grafik. Lauf bei QA-Fehler stoppen.

Grenzen: ein Parameterpunkt, lineare energetische Richtungen, keine
nichtlineare Langzeitstabilität, keine Eichfelder/Fermionen, kein Netz V.
Eine hohe l-Barriere darf analytisch diskutiert werden, ohne weitere
numerische l-Sektoren als gerechnet auszugeben.
