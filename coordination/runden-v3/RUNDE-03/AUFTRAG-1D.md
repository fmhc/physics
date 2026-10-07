# Runde 3, 1D-Tests: Chemie 1, 2/3, 7, 15, 14 (Zufall) und Wellen 5 (Anthropic)

Auftraggeber: claude-primary. Rundenbeginn 2026-09-30 01:19:16 CEST (gemessen). Deutsch. Explorativ, leicht.

## Rahmen

- Lies coordination/runden-v3/README.md und RUNDE-03.md.
- Die Ideen stehen in RUNDE-03/IDEEN-20-QBALL-CHEMIE.md (Nr. 1, 2, 3, 7, 14, 15) und
  RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md (Nr. 5).
- **Modell:** L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.
- **Verifizierter Ausgangscode:** coordination/runden-v3/RUNDE-01/qg1/qg1.py (Schiessen gegen analytischen Anker,
  Zeitentwicklung mit bestandenen Kontrollen). Uebernimm Schiessen, Gitter, Zeitschritt und Integrator; aendere so wenig
  wie moeglich.
- Ein anderer Agent schreibt parallel RUNDE-02/tests1d/. Beruehre diesen Ordner nicht; schreibe nur in
  RUNDE-03/tests1d-r3/.

## Tests (je hoechstens 10 min GPU, zusammen moeglichst unter 15 min)

1. **Chemie 1, Elektronegativitaet.**
   - Zwei nahe gleichphasige Baelle, omega^2 = 0,8 (klein) und 0,6 (gross); Abstand so, dass sich die Auslaeufer
     ueberlappen.
   - Ladung links/rechts ueber die Zeit.
   - Vorhersage: Ladung fliesst von klein nach gross.
   - Gegenprobe: gleiche omega, dann kein Nettofluss.
2. **Chemie 2/3, Bindungskurve.**
   - E(d) des Paars bei fester Ladung fuer Delta phi = 0 und pi, bei 8 bis 12 Abstaenden (Relaxation bei fester Ladung
     oder stationaere Paarloesung; begruende die Wahl).
   - Morse-Anpassung E(d) = D (1 - exp(-a (d - d0)))^2 + const fuer Delta phi = 0 und Vergleich mit der asymptotischen
     Form ~ -cos(Delta phi) exp(-kappa d), kappa = sqrt(1 - omega^2).
   - Falls es ein Minimum gibt: Kruemmung, daraus die Schwingungsfrequenz (Idee 4 als Nebenprodukt).
3. **Chemie 7, Aktivierungsenergie.**
   - 1D-Stoesse zweier gleicher Baelle (omega^2 = 0,7), Delta phi in {0, pi/2, pi}, v in 4 bis 6 Werten.
   - Ausgang: verschmolzen, abgeprallt oder durchgelaufen.
   - Phasendiagramm und "Barriere" (kleinstes v fuer Verschmelzen) je Delta phi.
4. **Chemie 15, Redox ueber Bruecke.**
   - Spender (omega^2 = 0,85), Empfaenger (0,6), dazwischen 0 bis 3 Bruecken-Baelle (0,7) mit festem Abstand.
   - Transferrate (Anfangssteigung der Empfaengerladung).
   - Vorhersage: exponentieller Abfall mit der Brueckenzahl. Scheitert, wenn nicht.
5. **Chemie 14, Zufallskarte: Q und Anti-Q.**
   - Ball exp(-i omega t) neben Anti-Ball exp(+i omega t) im Abstand d (4 Werte).
   - Zeit bis zur Vernichtung von 50 % der Betragsladung; Endzustand (Strahlung, Restball?).
6. **Wellen 5, Rumpfgeschwindigkeit.**
   - Homogener Hintergrund (duenn, S_bg so, dass er stabil ist; begruende die Wahl mit der linearen Stabilitaet).
   - Ball mit Geschwindigkeit v (6 Werte) hindurch; Bremskraft aus der Impulsaenderung, Abstrahlung.
   - Vorhersage: Schwelle nach dem Landau-Kriterium v_c = min eps(k)/k der Hintergrundanregungen (vorher ausrechnen).
   - Gegenprobe: ohne Hintergrund keine Bremsung.

## Abgabe (RUNDE-03/tests1d-r3/)

- tests1d_r3.py: CUDA, float64, je Test ein Unterbefehl oder alle nacheinander
- PLAN.md:
  - Aufruf mit Lock wie RUNDE-01/QG1-PLAN.md
  - Laufzeitschaetzung je Test
  - Vorhersage je Test vor dem Rechnen
  - Gegenproben
  - Latten L1 bis L5
  - "Einfach gesagt"
- Nicht rechnen: Die Leitung startet in einer VS-1-Portionsluecke.

## Grenzen

- Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik. Der Code bleibt ungetestet; halte ihn einfach.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrte Ordner wie ueblich:
  - KS-1-Ergebnisse, T8-SOLL-*
  - coordination/vertraege-20260925/
  - ks-1-dk-lauf/ und ks-1-dk-laeufe/
- Zeiten mit `date`. Budget hoechstens 90 Minuten.
