# ROHR-DREHUNG-1: Werden Teilchen, die durch schief verschweisste Rohre laufen und dabei mitgedreht werden, von selbst zu Spin-1/2-Fermionen? (Schachbrett in 3D auf Finns Netz, mit Verdrillung je Kante; schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-06 22:11:07 CEST (date), vor jeder Rechnung.
- **Finn, 06.10. abends:**
  - "jede kante einzeln zaehlt fuer die torsionssache, also drei mal bzw. vier mal"
  - "torsion von einem 3d dreieck ... ggf quantisiert"
  - "wie drei rohre die schief aneinander geschweisst sind, und jedes mal wenn eins durchgeht, dreht sich das, was da durchgeht"
- **Herkunft [P]:**
  - SCHACHBRETT-KAUSAL-1 (Runde 38): Feynmans Schachbrett in 1+1D, ein Fermion aus dem Zaehlen der Ecken.
  - GERAHMTER-FADEN-1: Das 2-pi-Vorzeichen kommt aus der Hebung (SU(2) statt SO(3)).
  - REGGE-TORSION-L: Torsion als Zusatzdrehung; Spin 1/2 braucht Spin(n)-Holonomien.
  - TORSION-STEIF-1: 4 freie Torsionsrichtungen je Zelle.
  - QCA-TETRA-1 und KAC-DIAMANT-WICK-1: Quanten- und Kac-Gaenge, Dirac-Paare.
  - Projektsuche (22:10, mit Sperrausschluessen): Spinfaktor nichts, Writhe/Calugareanu nur am Rand, Schachbrett nur in
    1+1D.
- **Literatur [L, aus dem Gedaechtnis]:**
  - Polyakovs Spinfaktor: Ein Pfad, dessen Spinor bei jedem Knick mitgedreht wird, ergibt in der Pfadsumme den
    Dirac-Propagator. Eine geschlossene ebene Schleife gibt -1, das Vorzeichen der Fermionschleife.
  - Calugareanu: Verschlingung = Verdrillung + Windung. Die Verschlingung ist fuer geschlossene Baender ganzzahlig; das ist
    der Kandidat fuer Finns "quantisiert".

## Modell

- **Netz:** Diamant (n = 2 bis 4) und, wenn moeglich, die Dreiecke von V.
- **Laeufer:** traegt einen 2-Spinor.
- **Je Schritt laengs Kante e:**
  - (i) Verdrillung um die Kantenachse um psi_e. Das ist Finns Torsion je Kante.
  - (ii) An der Ecke die kleinste SU(2)-Drehung, die die eingehende auf die ausgehende Richtung bringt. Das ist das
    schiefe Schweissen.
  - Amplitude je Schritt: ein Huepfparameter.
- **Transferoperator** T(k) mit Bloch-Wellen, Spektrum.

## Messgroessen

- M1: Holonomie um jede kleinste geschlossene Schleife ohne Verdrillung.
- M2: Verdrillungsregeln psi (einheitlich oder je Kantenklasse, auch Vielfache von 2 pi/3), die alle kleinsten
  Schleifen auf -1 bringen.
- M3: Spektrum von T(k) mit dieser Regel: Dirac- oder Weyl-Kegel? Isotrop?
- M4: Darstellung der Netzdrehungen auf den niedrigen Moden: projektiv (2 pi = -1) oder linear?

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | So kann sie scheitern | Wahrsch. |
|---|---|---|---|
| R1 | [M, vorab] Ohne Verdrillung gibt jede ebene geschlossene Schleife (Dreieck von V) die Holonomie -1, weil die Tangente sich um 2 pi dreht | Ein ebenes Dreieck gibt nicht -1 (Vorzeichen- oder Bauregelfehler) | 90 % (Kontrolle) |
| R2 | Ohne Verdrillung gibt das Sessel-Sechseck des Diamanten (nicht eben) eine Holonomie, die nicht +-1 ist | Holonomie genau +-1 | 75 % |
| R3 | Es gibt eine Verdrillungsregel mit wenigen Werten je Kantenklasse, die alle kleinsten Schleifen auf -1 bringt; bis auf Eichung eindeutig | Keine solche Regel, oder ein Kontinuum davon | 40 % |
| R4 | Mit der Regel aus R3 hat T(k) masselose, isotrope Dirac- bzw. Weyl-Kegel (Tempostreuung < 5 %) | Keine Kegel, oder anisotrop | 30 % |
| R5 | Die niedrigen Moden tragen eine projektive Darstellung der Netzdrehungen (2 pi = -1) | lineare Darstellung | 50 % |

- R1 ist vorab ableitbar (Kontrolle). R2 kann man am Schreibtisch ausrechnen (Raumwinkel der Tangentenbahn).
- Der Agent rechnet R2 zuerst am Schreibtisch, in VORAB.md. Ist R2 damit festgelegt, wird es als vorab gekennzeichnet.
- Echt offen: R3, R4, R5.
- Synthetisch, keine Messdaten.
