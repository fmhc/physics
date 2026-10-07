# Runde 1, Karte QG-1: 1D-Code fuer den Fall eines Q-Balls in einem Brechungsfeld (Anthropic)

Auftraggeber: claude-primary (Leitung). 30.09.2026 nach 00:00:02 CEST (Rundenbeginn gemessen). Deutsch. Explorativ.

## Frage

Faellt ein Q-Ball in einem schwachen, linearen Brechungsfeld c(x) universell, also unabhaengig von seiner inneren
Frequenz omega? Die Karte (coordination/ideation-arxiv-20260929/KARTEN.md, Abschnitt QG-1) nennt drei Varianten:
- **B:** c nur am Zeitterm.
- **C:** schwache Metrik auf alle Terme, wie in der ART.

Papierstand (ungeprueft, Codex liest parallel gegen): A gibt eine Beschleunigung proportional E_grad/E, also nicht
universell. C ist nach der Virialidentitaet universell.

## Deine Aufgabe

1. **Schreiben:** ein kleines 1D-Programm (PyTorch, float64, CUDA) im Ordner coordination/runden-v3/RUNDE-01/qg1/.
   - **Ausgangsprofil:** das Q-Ball-Profil unseres Modells durch Schiessen. Potential und Normierung wie im Q-Ball-Atlas
     (lagebericht/qball-atlas.html) bzw. U = S - S^2 + S^3/2 mit S = |phi|^2. Bitte selbst pruefen, welches gilt.
   - **Werte:** omega^2 = 0,55, 0,7 und 0,9.
   - **Zeitentwicklung:** im Feld c(x) = 1 + g x mit kleinem g, fuer jede Variante A, B, C.
   - **Messung:** Schwerpunktbahn der Ladungsdichte. Daraus die Beschleunigung a(omega)/a_Newton (a_Newton wie in der Karte
     definiert), dazu Abstrahlung und Atmung.
   - **Gegenproben:**
     - C muss fuer alle omega dieselbe Beschleunigung geben.
     - g = 0 darf keine Beschleunigung geben.
     - -g muss das Vorzeichen umkehren.
     - Das Ergebnis darf sich bei halbem Gitterabstand und halbem Zeitschritt nicht wesentlich aendern: Effekt mindestens
       fuenfmal groesser als diese Aenderung (Latte L3).
   - **Laufzeit:** zusammen hoechstens 10 min auf einer P5000.
2. **Nicht rechnen.** Die .69-GPU ist durch VS-1 belegt. Du schreibst nur den Code und einen Laufplan.
   - QG1-PLAN.md: Aufruf, erwartete Laufzeit je Teil, Ausgabedateien, was welches Ergebnis bedeuten wuerde
   - Vorab gilt: Welche Werte waeren fuer A, B und C nach der Papierrechnung zu erwarten? Welche Abweichung waere ein
     Befund? Die Vorhersage steht, bevor gerechnet wird.
3. Die Leitung startet den Lauf unter dem gemeinsamen Lock (`flock -w 45 /home/fmh/fmhc-physics-remote/gauntlet-gpu.lock`,
   einmalige Unit) nach VS-1 oder in einer Portionsluecke.

## Abgabe

- qg1/qg1.py
- QG1-PLAN.md mit "Einfach gesagt"
- Kurzmeldung: Beginn und Ende nach date, erwartete Laufzeit

## Grenzen

- Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik. Der Code wird ungetestet abgegeben; halte ihn
  deshalb einfach und lesbar.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten.
- Gesperrte Ordner wie ueblich:
  - KS-1-Ergebnisse, T8-SOLL-*
  - coordination/vertraege-20260925/
  - ks-1-dk-lauf/ und ks-1-dk-laeufe/
- Zeiten mit `date`. Budget hoechstens 75 Minuten.
