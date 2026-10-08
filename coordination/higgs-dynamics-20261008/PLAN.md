# HIGGS-DYNAMICS-1 — Vorabplan

08.10.2026. Nutzerauftrag: dynamische reduzierte Higgsbeschreibung gegen das volle gekoppelte Modell rechnen. Referenzherleitung: physics main 1e885fd0c1c03edef8ff4b2be3b8d983f5d21ac1, coordination/literatur-formeln-20261008/FORMEL-ABGLEICH.md. Keine Parameteranpassung, keine erneute Relaxation.

## Eingabe und Umfang

HIGGS-MINIMA-1 RESULT.json SHA256 a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9. Jeweils seed=0, eta=.05,g=.005,c8=0,Q=600; base R20 h.05, grid R20 h.025, box R30 h.05. Radialer 3D-Hintergrund mit Störungen l=0,1,2. Keine Übertragung auf V oder andere räumliche Dimensionen; andere d brauchen anderes Maß und Winkeloperatoren.

Sieben Beschreibungen pro Gitter und l, insgesamt 63 Spektralprobleme:
1. full: volle lineare Dynamik auf vollem Profil;
2. Schur-static: exakte statische Higgs-Elimination, kanonische Materieträgheit;
3. Schur-inertia: gleiche statische Energie plus I+BC^-2B^T;
4./5. E3-static / E3-inertia auf eigenem E3-Profil;
6./7. Ecomp-static / Ecomp-inertia auf eigenem Ecomp-Profil.

Ecomp-Kinetik ist Pullback der vollen Kinetik unter z=z1+z2: M=I+(J1+J2)^T(J1+J2), Jk=(1/sqrt2) dzk/du. E3 verwendet die konsistente Portalordnung bis b^3: M=I+J1^TJ1+J1^TJ2+J2^TJ1. Positivität jeder M wird geprüft; keine stille Reparatur.

## Spektralproblem und Ladung

qdd-2ωpd+Aq+Bh=0; pdd+2ωqd+Dp=0; hdd+Ch+B^Tq=0.
A ist fixed-omega, nicht fixed-Q. Radial R_Q=4ω²uu^T/(u^Tu) vom Fix-Q-Hessian abziehen. Setze P=pd+2ωq, P=D^(1/2)w auf range(D), und fixiere den gemeinsamen Ladungssektor ker(P)=0. Dann symmetrischer voller Operator

H=[[A+4ω²I,-2ωD^(1/2),B],[-2ωD^(1/2),D,0],[B^T,0,C]].

Für E3/Ecomp B/C nicht mehr explizit; A durch reduzierte fixed-omega-Krümmung ersetzen und verallgemeinerten Massblock diag(Mq,I) verwenden. Der Nullraum von D wird nur in l=0 als gemeinsame Phase entfernt, wenn |λ|<1e-6 und quadrierter Überlapp mit u >1-1e-8. Alle übrigen D-Eigenwerte müssen >1e-6 sein. Bei Scheitern Abbruch statt Clipping; andere Nullräume/negative D benötigen eine neue vollständige Hamiltonanalyse. Erwartete globale Phasen-Nullrichtung wird zusätzlich über D u geprüft und dokumentiert. Die entfernte reine Phase wird nicht als fehlende Instabilität ausgegeben.

## QA vor physikalischer Wertung

- Rekonstruktion der vollen originalen gekoppelten Gleichungen aus niedrigen Eigenmoden, normiertes Residuum <1e-7.
- Eigenresiduen <1e-7 normiert; M-Orthonormalität <1e-9; Rohasymmetrie <1e-8.
- Hintergrund-Phasenresiduum <1e-6; rekonstruierte lineare Ladung für radiale nichttriviale Modi <1e-7 normiert.
- C und alle verwendeten M positiv (Cholesky). Schur-Lösungsresiduum <1e-10.
- Frequenzabhängiges Schur-Residuum bei vollen Moden <1e-7; ausgeschlossene Polnähe wird explizit gemeldet, kein Invertieren am Pol.
- Referenzzweig auf gleichem Profil: geordnete ν²_full <= ν²_inertia <= ν²_static bis absolut 1e-7; folgt aus Rayleigh–Ritz und positivem M, nicht auf E3/Ecomp mit anderen Profilen übertragen.
- E3/Ecomp: J1/J2-Tangente gegen z1/z2-Autograd-JVP in einer vorab glatten Richtung <1e-9; radiale reduzierte Energiehessians gegen unabhängige Energiedifferentiation <1e-9. Winkeljets stammen aus dem bereits unabhängig geprüften HIGGS-ANGULAR-MODES-1; ihre Übernahme wird gehasht.

## Entscheidungskriterien

Vergleiche acht niedrigste nichttriviale positive Frequenzen ν, keine Quadratwurzeln statischer Fix-Q-Hessians. Für l=1 wird ausschließlich die erste Mode separat als Translation behandelt, wenn ihr Materieüberlapp mit d(u)/dr-u/r >.99 ist, |ν²|<1e-3 und der Betrag auf feinem Gitter <.4 des Basiswerts; sonst keine Ausnahme. Höhere entartete Paare werden nicht nach Ergebnis ausgesucht.

Näherungsentscheidung für jede reduzierte Beschreibung: maximaler relativer Frequenzfehler <=5 %, Fehlerdrift über Gitter/Box <=0.5 Prozentpunkte, keine negativen ν²<-1e-6. Dynamische Verbesserung durch Zusatzträgheit nur behaupten, wenn der Maximalfehler kleiner als ohne Zusatzträgheit ist; nicht vorausgesetzt. Fehlernachweis beschränkt auf acht niedrige Moden; ν²_min und Anzahl negativer ν² werden aus dem gesamten endlichen Spektrum gemeldet. Lineare Stabilität nur für die geprüften Sektoren und Profile. Keine nichtlineare Langzeit-/Quantenstabilität, keine Teilchenmassen.

## Ressourcen und Provenienz

.69, Quadro P5000, CUDA float64/cuSOLVER. Halbe GPU-Pacht, gemeinsamer gauntlet-gpu.lock, CPUQuota100%, MemoryMax3G, RuntimeMaxSec900. Bestehende Dienste bleiben bestehen, sofern der freie Speicher genügt. Numerische Matrizen/Linearsysteme/Eigenprobleme auf CUDA; CPU für Ablauf, IO, skalare Zusammenfassung und Grafik. Eingabe-/Code-/Planhashes, Status und Rohresultate archivieren. Vorhandene Ergebnisordner niemals überschreiben. Abbruch/Fehlversuch erhalten; Kriterien nach Datenansicht nicht lockern.
