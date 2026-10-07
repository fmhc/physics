# NETZ-NICHTLINEAR-1: Verschwinden die Ausnahmezuege, wenn die Traegheit am gedehnten (mitbewegten) Netz gerechnet wird? (Runde 50, Grundgleichung v3 schliessen, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 19:23:00 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - GRUNDGLEICHUNG-v3 (RUNDE-50): stetige Zeitgrenze der 4D-Wirkung, ADM-Form mit Potential B, Lapse-Multiplikator
    nach Eckregel R1. M_eff hat je Ecke genau eine negative Richtung (konform, DeWitt).
  - UMKLAPP-FOLGE-1: In Lesart H (Operatoren am ungedehnten Hintergrund) heizen passende Zuege nicht. Ausnahmezuege
    sind 2-3-Zuege an einer Flaeche, die am Hintergrund Delaunay ist. Nach ihnen hat M_eff 130 statt 128 negative
    Richtungen, und es entsteht eine wachsende Mode: s1 und s2 23 von 23, s3 mit Kaskade. Lesart dort [H]: Die
    Traegheit muss am mitbewegten Netz gerechnet werden.
  - Projektsuche der Leitung (19:20, mit Sperrausschluessen; mitbewegt, co-moving, nichtlinear mit M_eff): keine
    nichtlineare 4D-Netzdynamik im Projekt.
- **Ableitbarkeit:**
  - [M] Faellt der Zug genau auf den Kreuzungszeitpunkt (mu = 0 im gedehnten Netz), beschreiben alte und neue Zerlegung
    dort dieselbe Geometrie. Rechnet man M_eff am gedehnten Netz, sollte der Sprung stetig sein. Das ist eine Skizze,
    keine Rechnung.
  - Nicht ableitbar: ob die zusaetzlichen negativen Richtungen dabei wirklich verschwinden, ob die Kaskade in s3
    ausbleibt und wie gross die Restdrift ist.

## Modell

- Aufbau wie UMKLAPP-FOLGE-1: Glas s1 bis s4 (N = 128), Kastenmode A = 1e-3, 10 Perioden, Ereignissuche, Arme P und R,
  Referenz ohne Umklappen. Code aus RUNDE-37/umklapp-folge-1/code und umklapp-4d-1/code.
- Neu, Lesart G (gedehnt):
  - G1 (billig): M_eff und B am gedehnten Netz im Zugzeitpunkt rechnen, mit der neuen Zerlegung; bis zum naechsten
    Zug festhalten.
  - G2 (voll nichtlinear, wenn das Budget reicht): M_eff(l) laufend nachfuehren, mit den Ableitungstermen dM/dl in
    den Bewegungsgleichungen. Dafuer einen Integrator fuer nicht separable Hamiltonfunktionen nehmen (implizite
    Mitte oder verallgemeinerter Leapfrog).

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| N1 | In G1 bleibt die Zahl der negativen M_eff-Richtungen nach jedem Zug bei 128, auch bei den frueheren Ausnahmezuegen in s1 und s2 | 60 % |
| N2 | In G1 bleibt die Kaskade in s3 aus: \|H - H0\|/H0 bleibt ueber 10 Perioden unter 1e-3 | 50 % |
| N3 | In G1 liegt die Drift in s1 und s2 nach 10 Perioden unter 1e-5 relativ, also auf dem Niveau regulaerer Zuege | 40 % |
| N4 | Kontrolle G2 ohne Zuege: Die Energie bleibt ueber 10 Perioden auf 1e-8 relativ erhalten (Integrator) | 85 % |

## Rahmen

- Code-Agent ohne Einfrieren und Leser (Finn: einfach machen).
- Spuren cpu2 bis cpu4 ueber kleintest.sh, je Lauf hoechstens 10 min. GPU-Spuren nur, wenn M_eff dort deutlich
  schneller wird; sie sind mit QUANT-3 und AEQUIVALENZ-DREI-1 geteilt.
- df vor jedem Lauf, abbrechen unter 10 GB frei.
- Synthetisch, keine Messdaten.
