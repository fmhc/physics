# HIGGS-MINIMA-1: selbstkonsistenter radialer Pilot

Vorabplan 08.10.2026, Anschluss an HIGGS-FORCE-1 (9194f15).
Nur stärkere Kopplung g=.005, eta=.05, c8=0, Q=600.
Drei vorhandene B13-Gitter: base, grid, box. Keine Parameteranpassung.
Vergleich volle stationäre Portalenergie, E3, Ecomp gemäß HIGGS-FORCE-1.
Je zwei Startwerte: archivierte Singulettprofile und dieselben Profile
multipliziert mit 1+.03 exp(-r²/9); volle Higgsantwort als Archivstart,
bei zweitem Start ebenfalls mit diesem Faktor gestört. Somit 18 Relaxationen.
Ziel ist ein selbstkonsistenter stationärer Zweig, kein globaler Minimalitätsbeweis.

Feste Ladung mittels Q²/(4I), I=4πh sum(u_i²), radialer 3D-Raum.
B13-Quadratur und Nullränder. Reduzierte Energie mit voller Kettenregel.
CUDA float64 Autograd; inverser freier radialer Operator als Präconditionierer;
600 Iterationen maximal, Schritte 4*2^-k, k=0..11, nur Energieabnahme akzeptieren.
Abbruch bei Residuum <1e-7 oder keinem akzeptierten Schritt.
Residuum sqrt(4πh sum(metric*g²)/Q), g=Egradient/(8πh metric),
metric=(1,1,.5) für volle Felder, (1,1) reduziert.

QA: Archivenergie der vollen Theorie relativ <1e-10 reproduzieren;
analytischer voller B13-Gradient relativ <1e-9 gegen Autograd.
Für reduzierte Energien gelten bereits geprüfte Ableitungen aus HIGGS-FORCE-1.

Einordnung pro reduziertem Modell nur wenn volle Referenz auf allen Stufen
und beide Starts konvergieren (Residuum <1e-5). Beide Starts müssen innerhalb
eines Modells je Stufe einen Singulettprofilabstand <.001 ergeben.
Vergleich jeweils gleicher Start/Gitter mit neu relaxierter voller Theorie:
Singulettprofil-L2 relativ <=1%, totale Energie relativ <=.1%, omega relativ
<=.5%. Zusätzlich Higgsprofilfehler berichten, aber kein neuer Gatewert dafür.
Für jede Fehlergröße maximalen base/grid/box-Unterschied d bestimmen:
max Fehler + d <= Grenze für bestanden; min Fehler - d > Grenze für verfehlt;
sonst unentschieden. Bei fehlender Konvergenz: unentschieden, nicht Modellwiderlegung.
Gesondert Bindung E/Q und omega <sqrt(1-eta), Außenladungsanteil <1e-6.
Keine retrospektive Lockerung. Alle Läufe und Abbrüche veröffentlichen.

Eingabe B13 SHA256 1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d.
Ausführung auf GPU-Rechner/P5000, CUDA; CPU nur Steuerung, IO und Zusammenfassung.
Gemeinsamer GPU-Lock, halbe Ressourcenpacht, CPU100%, RAM2G, Laufzeitlimit600s.
Keine Zeitentwicklung, kein nicht-radialer Stabilitätsnachweis, keine V-Netzrechnung.
