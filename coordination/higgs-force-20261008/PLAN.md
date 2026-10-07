# HIGGS-FORCE-1: statische reduzierte Energie und Portalkräfte

Vorabplan 08.10.2026. Anschluss an HIGGS-RESPONSE-1, veröffentlicht bd26c78.
Alle 24 unveränderten B13-Profile, keine Optimierung oder Zeitentwicklung.
Eingabe SHA256: 1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d.
Quelle sind zwei komplexe Singuletts und reale Higgsamplitude, radialer 3D-Fall.

chi1=-K^-1(b*y0*S), chi2=-K^-1(b*S*chi1+3*a*y0*chi1²).
K=-Delta+6.25, radiales z=r*chi mit denselben Randwerten und Quadraturen wie B13.
Vollständige statische Higgsenergie:
EH=1/2<chi,Kchi>+<b*y0*S,chi>+b/2∫S chi²+a*y0∫chi³+a/4∫chi⁴.

Vier Beschreibungen, vorher festgelegt:
E2=-1/2<J,K^-1J>, C2=dE2/dS=b*y0*chi1.
E3=E2+b/2∫S chi1²+a*y0∫chi1³,
C3=b*y0*(chi1+chi2)+b/2*chi1².
Ecomp=EH[chi1(S)+chi2(S),S], Ccomp=vollständige Autograd-Ableitung nach S.
Cplug=b*y0*(chi1+chi2)+b/2*(chi1+chi2)², ohne Kettenregel:
bewusst zu prüfende Abkürzung, kein vorweg als konservativ erklärtes Modell.
Referenz Cref=b/2*(y_ref²-y0²), gespeichertes stationäres Higgsprofil.

Primäre Fehlernorm: ||u*(C-Cref)||/||u*Cref||, u_i=r*F_i,
Summation über beide Komponenten und alle Radialpunkte. Sie misst den
zusätzlichen Portal-Kraftterm, nicht die größere Gesamtbeschleunigung.
Energiefehler bei E2/E3/Ecomp relativ zum Higgsbeitrag der Vollreferenz.
Cplug hat hier keine eigene separat festgelegte Energie: nicht als Modell
mit Ecomp und gleichzeitig Cplug ausgeben.

Pilotgates E2/E3/Ecomp: Kraft- UND Energiefehler <=5%, unterstützt durch
base/grid/box-Indikator d analog HIGGS-RESPONSE-1: max Fehler+d<=.05 und
d<=.005 brauchbar; min_stufe(max(Kraft,Energie))-d>.05 und d<=.005 unzureichend;
sonst unentschieden. Für Cplug nur beschreibende Kraftfehler, keine Freigabe.

Konsistenz-QA: analytisches C3 gegen Autograd, relative Norm <1e-10.
Unabhängige zentrierte Richtungsdifferenzen der Energien E3/Ecomp auf
Dichtevariation dS=S*(sin(.7r)+.3cos(1.1r)) mit eps=.01,.005,.0025;
kleinster Schritt relativer Fehler <1e-6. Folge der Fehler berichten,
kein erzwungener Faktor4 bei Rundungsgrenze.
Gemischte Richtungsableitungen mit dS1=S*exp(-r²/4), dS2=S*r²/(1+r²):
Symmetriedefekt für E3/Ecomp <1e-8 relativ zur größeren Kreuzantwort.
Für Cplug Defekt messen, kein Ergebnis vorwegnehmen.
Zusätzlich ||Fplug-Fcomp||/||Fcomp|| berichten.
G=0-Nullgrenze absolut <1e-12. Alle QA auf allen Profilen vor Einordnung.

CUDA float64 .69/P5000, halbe GPU-Pacht, bestehender gauntlet-gpu.lock,
CPU100%, MemoryMax2G, RuntimeMaxSec120. CPU nur IO/Steuerung/skalare Tabellen.
Keine neuen Parameterfits, keine Neuberechnung alter Relaxationen.
Quell- und Planhash vor Lauf festhalten, Resultat unabhängig vom Ausgang publizieren.
Grenzen: nur statische Kräfte auf archivierten Profilen, kein dynamischer
Energieerhalt, kein eigenständiger Spektral-/Stabilitätsnachweis.
