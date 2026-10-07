# Runde 2: 1D-Tests fuer die Ideen 9/10, 32, 33 und das 3D-Radialprofil fuer Idee 31 (Anthropic)

Auftraggeber: claude-primary (Leitung). Rundenbeginn 2026-09-30 00:52:49 CEST (gemessen). Deutsch. Explorativ, leicht.

## Rahmen

- Lies coordination/runden-v3/README.md, RUNDE-02.md und in RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md die Ideen 9, 10, 31, 32
  und 33.
- **Modell:** L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.
- **Wiederverwenden:** coordination/runden-v3/RUNDE-01/qg1/qg1.py ist auf der .69 gelaufen und stimmt.
  - Schiessen gegen den analytischen Anker: 1,2e-10.
  - Zeitentwicklung: Kontrollen K0 bis K4 bestanden.
  - Uebernimm Schiessen, Anker, Gitter und Zeitschritt daraus. Aendere so wenig wie moeglich.

## Tests (je Rechnung hoechstens 10 min auf der P5000; zusammen hoechstens 10 min)

1. **Idee 9/10, Uhren-Synchronisation.**
   - (a) Fuenf Q-Baelle in einer Kette. Abstand so, dass sich die Auslaeufer ueberlappen; ein Abstand etwas groesser als
     die doppelte Halbwertsbreite. Frequenzen omega^2 = 0,70 +- 0,01 verteilt.
   - (b) Ein grosser (omega^2 = 0,55) neben einem kleinen (0,80).
   - Messung: Phasen aus dem Feld am Ballzentrum, Kuramoto-Ordnungsparameter ueber die Zeit, momentane Frequenzen.
   - Gegenproben: grosser Abstand (keine Kopplung, keine Synchronisation); halber Zeitschritt.
   - Vorab festhalten, was "Synchronisation" heisst (Schwelle fuer den Ordnungsparameter).
2. **Idee 32, Absorptionsspektrum.**
   - Ein Q-Ball bei omega^2 = 0,70. Von links laufen schwache Wellenpakete (Amplitude 1e-3) mit Traegerfrequenz nu von
     1,0 bis 2,5 (12 Werte).
   - Messung: transmittierter, reflektierter und absorbierter Anteil (Ladung und Energie); dazu die inneren Moden des
     Balls aus einem kleinen Stoss (FFT der Breite).
   - Gegenprobe: dasselbe ohne Ball, also volle Transmission.
3. **Idee 33, Virus (Zufallskarte).**
   - Ein kleiner Q-Ball (omega^2 = 0,90) laeuft langsam in einen grossen (0,55), gleichphasig, und verschmilzt.
   - Messung: Modenspektrum des grossen Balls vorher und nachher; Ladungs- und Energiebilanz.
   - Gegenprobe: gegenphasig (Abprall erwartet); halber Zeitschritt.
4. **Idee 31, Gedaechtnis:** 3D radial, nur Schiessen, Sekunden.
   - Q(omega) und E(omega) fuer omega^2 von 0,51 bis 0,99.
   - Gibt es bei gleichem Q zwei Aeste? Wo liegt Q_min?
   - Vorzeichen von dQ/domega je Ast (Vakhitov-Kolokolov: stabil, wo dQ/domega < 0).
   - Vorhersage vorab: Der Dicke-Wand-Ast ist instabil, dann gibt es kein Gedaechtnis. Das ist eine L1-Probe.

## Abgabe (Ordner coordination/runden-v3/RUNDE-02/tests1d/)

- tests1d.py: ein Aufruf je Test oder alle nacheinander, CUDA, float64
- PLAN-1D.md:
  - Aufruf mit Lock wie QG1-PLAN.md (RUNDE-01)
  - geschaetzte Laufzeit je Test
  - Vorhersage je Test vor dem Rechnen
  - Gegenproben
  - Latten L1 bis L5 je Test, soweit vorab bestimmbar
  - "Einfach gesagt"
- Nicht rechnen: Die GPU haelt VS-1. Die Leitung startet in einer Portionsluecke.

## Grenzen

- Auf dem Laptop kein python, py_compile, awk und keine Shell-Arithmetik. Code bleibt ungetestet, also einfach halten.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrte Ordner wie ueblich:
  - KS-1-Ergebnisse, T8-SOLL-*
  - coordination/vertraege-20260925/
  - ks-1-dk-lauf/ und ks-1-dk-laeufe/
- Zeiten mit `date`. Budget hoechstens 75 Minuten.
