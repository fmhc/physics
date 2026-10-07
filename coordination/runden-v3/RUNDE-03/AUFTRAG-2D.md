# Runde 3, 2D-Tests: Wellen 16, 8/9, 14 und Papierkarte 20 (Anthropic)

Auftraggeber: claude-primary. Rundenbeginn 2026-09-30 01:19:16 CEST (gemessen). Deutsch. Explorativ, leicht.

## Rahmen

- Lies coordination/runden-v3/README.md und RUNDE-03.md.
- Die Ideen stehen in RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md (Nr. 16, 8, 9, 14, 20).
- **Modell:** L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 2D.
  - Q-Ball: psi = f(r) exp(i m theta - i omega t), m = 0 oder 1.
  - Die duenne Wand liegt bei omega^2 -> 1/2.
- **Ausgangscode:** coordination/runden-v3/RUNDE-01/qg1/qg1.py ist in 1D verifiziert.
  - Fuer 2D brauchst du radiales Schiessen fuer f(r) (mit m^2/r^2-Term fuer m = 1) und eine 2D-Zeitentwicklung.
  - Integrator und Genauigkeit wie in qg1.py, spektral oder finite Differenzen; begruende die Wahl.
- Schreibe nur in RUNDE-03/tests2d-r3/.

## Tests (je hoechstens 10 min GPU)

1. **Wellen 16, Tropfenschwingung (Kern der Runde).**
   - Grosser duennwandiger 2D-Ball (omega^2 nahe 0,5, z. B. 0,52 und 0,55).
   - Wandspannung sigma und Innendichte rho aus dem Profil; lege vorab fest, welche Dichte gemeint ist (Energie- oder
     Ladungsdichte) und begruende das.
   - Formstoerung der Ordnung l = 2 und 3 mit kleiner Amplitude; Schwingungsfrequenz aus der Zeitreihe der Form.
   - Vorhersage: die 2D-Rayleigh-Formel fuer Kapillarschwingungen, omega_l^2 = (l^3 - l) sigma/(rho R^3) (2D-Form pruefen
     und herleiten). Keine freien Parameter.
   - Das Ergebnis darf deutlich abweichen; genau das waere ein Befund gegen das reine Tropfenbild.
2. **Wellen 8/9, Magnus und Flettner.**
   - Duenner stabiler Hintergrund mit gleichmaessiger Stroemung (Phasengefaelle).
   - Darin ein drehender Ball m = +1 bzw. -1 bei gleichem omega.
   - Messung: Querdrift des Ballzentrums.
   - Vorhersage: Querdrift mit Vorzeichen von m. Gegenprobe: m = 0 ohne Querdrift.
3. **Wellen 14, Brechung.**
   - Hintergrund mit Dichtestufe entlang einer Linie. Ball (m = 0) trifft schraeg, bei 2 bis 3 Winkeln.
   - Messung: Bahnknick.
   - Vorhersage: vorab ein effektives Brechungsgesetz aus der Energie- bzw. Impulserhaltung an der Stufe herleiten; es darf
     scheitern.
4. **Wellen 20, Zufallskarte (nur Papier und Literatur).**
   - Kann es in unserem Ein-Feld-Modell geknotete Q-Baelle (Hopfionen) geben?
   - Und im erweiterten Modell C x S^2 (Spin-Arbeit, siehe project-Hinweis in coordination/, Stichwort "C x S2")?
   - Literatur kurz pruefen (Faddeev-Niemi; geknotete Q-Baelle, falls es Arbeiten gibt).
   - Ergebnis als KNOTEN-PAPIER.md mit Latten-Zeile.

## Abgabe (RUNDE-03/tests2d-r3/)

- tests2d_r3.py: CUDA, float64, Unterbefehle je Test
- PLAN.md:
  - Aufruf mit Lock wie RUNDE-01/QG1-PLAN.md
  - Laufzeitschaetzung
  - Vorhersagen vor dem Rechnen
  - Gegenproben, darunter ein Aufloesungsvergleich (L3)
  - Latten L1 bis L5
  - "Einfach gesagt"
- KNOTEN-PAPIER.md
- Nicht rechnen: Die Leitung startet in einer VS-1-Portionsluecke oder nach VS-1.

## Grenzen

- Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik. Der Code bleibt ungetestet; halte ihn einfach und
  gib einen kurzen Rauchtest (kleines Gitter, kurze Zeit) als eigenen Aufruf an.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrte Ordner wie ueblich:
  - KS-1-Ergebnisse, T8-SOLL-*
  - coordination/vertraege-20260925/
  - ks-1-dk-lauf/ und ks-1-dk-laeufe/
- Zeiten mit `date`. Budget hoechstens 100 Minuten.
