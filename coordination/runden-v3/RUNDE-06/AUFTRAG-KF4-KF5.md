
Auftraggeber: claude-primary. Zeit: 30.09.2026, nach 02:39:43 CEST (letzte Messung vor dem Schreiben). Deutsch. Explorativ.
Finn: "weiter rechnen".

## Gemeinsamer Rahmen

- **Karten:** coordination/runden-v3/REVIEW-FABLE-20260930/KARTEN-FABLE.md, Abschnitte KF-5 (ab Z. 113) und KF-4 (ab
  Z. 85). Halte dich an die dortige Hypothese, Gegenprobe und Messung. Wo du abweichst, begruende es.
- **Arbeitsweise:** coordination/runden-v3/README.md (v3, Latten L1 bis L5).
- **Modell:** U = S - S^2 + S^3/2, S = |phi|^2.
- **Gelaufene, verifizierte Codes:**
  - 1D: RUNDE-01/qg1/qg1.py (Fall im Brechungsfeld, Varianten A/B/C, Anker)
  - 1D: RUNDE-02/tests1d/tests1d.py
  - 2D: RUNDE-03/tests2d-r3/tests2d_r3.py (spektraler Laplace, radiales Schiessen m = 0/1, Tropfentest bestanden)
  - Die Ergebnisse liegen jeweils in lauf-69/ bzw. fein-lauf-69/.
- **Bekannt:**
  - Ein duenner Hintergrund S < 2/3 ist modulationsinstabil (Fable-Review).
  - Codex' 3D-Verdichtung bildete Netze statt Tropfen (RUNDE-02/I14-CODEX.md).
  - QG-1 hat den Fall in Varianten A, B und C in 1D bestaetigt (RUNDE-01.md).
- **Abgabe je Agent:**
  - Code mit --geraet cuda|cpu, float64, Unterbefehle, Rauchtest
  - PLAN.md mit Aufrufen ueber `cd /home/fmh/fmhc-physics-remote/<ordner> && bash
    /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> <skript> ...`
  - Laufzeiten, je Aufruf hoechstens 10 min auf einer P4000 bzw. einem CPU-Kern
  - Vorhersagen vor dem Rechnen, Gegenproben, Aufloesungsvergleich (L3), Latten L1 bis L5, "Einfach gesagt"
- **Nicht rechnen:** Die Leitung startet.
- **Grenzen:**
  - Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik; der Code bleibt ungetestet, also einfach halten.
  - Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
  - Gesperrt: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
  - Zeiten mit `date`. Budget hoechstens 80 Minuten.

## Agent KF-5 (Ordner RUNDE-06/kf5/, Remote runde6-kf5)

- **Geburt in 2D:** zufaelliges bzw. schwach gestoertes Anfangsfeld in einer 2D-Box, Laufzeit bis T = 800 (soweit in
  10 min je Aufruf moeglich; sonst in Abschnitten mit Zwischenspeicher).
- **Fragen:**
  - Entsteht ein Netz oder entstehen getrennte Tropfen?
  - Liegen die Tropfen auf der Q(omega)-Familie (Stufe-5-Kriterium der Stabilitaetsleiter)? Pruefbar ueber das
    Verhaeltnis von Ladung zu innerer Frequenz, verglichen mit der 2D-Familie aus dem Radialcode.
- **Gegenproben:** stabile Anfangsdichte ohne Klumpung; zwei Gittergroessen.

## Agent KF-4 (Ordner RUNDE-06/kf4/, Remote runde6-kf4)

- **Gezeitenantwort:** ausgedehnter Q-Ball in einem raeumlich periodischen Brechungsfeld c(x). Verglichen werden
- **Fragen:**
  - Unterscheidet sich die Gezeitenverformung (Dehnung) zwischen A und C, wenn die Schwerpunktbeschleunigung gleich
    gemacht wird?
  - Gibt es eine Resonanz, wenn die Periode des Feldes zur inneren Resonanz des Balls passt (rho ~ 1,494 in 1D)?
- **Gegenproben:** konstantes c ohne Verformung; Variante C mit Gezeiten nach der Metrik; zwei Aufloesungen.
