# LOG-NACHBAU: Blinder, unabhaengiger Nachbau der stillen Stelle im Log-Potential (Runde 16)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-02 07:45:25 CEST (date), vor jeder
  Codezeile und jedem Lauf.
- Herkunft: RUNDE-13 (B-BALL). Im Log-Potential U = ln(1 + S) wurde eine stille Stelle nur nachtraeglich gefunden, nach
  Kenntnis der Hauptlaeufe und mit demselben Code. Ein Test war das nicht.
- Ziel: ein unabhaengig geschriebener Code mit blinder Suche in einem weiten Fenster. Der Agent kennt die gefundene Lage
  nicht und darf sie nicht nachschlagen.

## Problem (vollstaendig hier beschrieben; der Agent schreibt seinen Code selbst)

- Komplexes Skalarfeld phi in 3D, Lagrangedichte |d_t phi|^2 - |grad phi|^2 - U(|phi|^2).
  - Kontrollmodell: U(S) = S - S^2 + S^3/2.
  - Testmodell: U(S) = ln(1 + S).
  - Beide haben U'(0) = 1, also Masse 1.
- Q-Ball: phi = f(r) e^{i omega t} mit f'' + (2/r) f' = (U'(f^2) - omega^2) f, f'(0) = 0, f(inf) = 0, f > 0 ohne
  Knoten.
- Radiale Linearisierung l = 0: phi = e^{i omega t} (f + a(r) e^{i rho t} + b(r) e^{-i rho t}), a und b reell. Das gibt
  zwei gekoppelte Kanalgleichungen mit den Frequenzen omega + rho und omega - rho und der Schwelle 1. Herleitung durch den
  Agenten, mit U' und U''.
- Im Fenster 1 - omega < rho < 1 + omega ist ein Kanal offen (auslaufende Welle) und einer geschlossen (abfallend).
- **Stille Stelle:** ein Punkt (omega^2, rho), an dem die regulaere Loesung im offenen Kanal keine Abstrahlung hat. Die
  Abstrahlamplitude W(omega^2, rho) wird null.
  - Kriterien: Vorzeichenwechsel einer reellen Kenngroesse s an den Nullstellen der geschlossenen Bedingung, und ein
    Umlauf der Phase von W um ein kleines Rechteck in der (omega^2, rho)-Ebene von +-1.
  - Aufgeloest heisst: groesster Phasensprung zwischen benachbarten Randpunkten < 0,4 rad.

## Kontrollen (bindend)

- K1: Mit dem Kontrollmodell findet der eigene Code die bewiesene Stelle bei omega^2 = 0,797677, rho = 1,744618 auf 1e-4,
  Umlauf +-1 auf zwei Gitterstufen.
- K2: Profile des Log-Balls auf zwei Gittern, Ladung Q und Energie E auf 1e-6 relativ gleich.
- Verfehlt K1 oder K2: nicht auswertbar.

## Blinde Suche (bindend)

- Testmodell, omega^2 von 0,70 bis 0,98, Zeilenabstand hoechstens 0,005. Je Zeile alle Nullstellen der geschlossenen
  Bedingung im Fenster und s, zwei Gitterstufen.
- Jeder Vorzeichenwechsel von s zwischen benachbarten Zeilen wird mit einem kleinen Rechteck lokalisiert.
- **Gefunden:** jede Stelle mit aufgeloestem Umlauf +-1 auf beiden Stufen; Lagen der Stufen auf 1e-4 gleich.

## Vorhersage (Leitung, vor jedem Lauf; dem Agenten nicht mitgeteilt)

- Die Vorhersage steht verschluesselt in VORHERSAGE.sha256: sha256 eines Textes mit Lage, Umlauf und
  Wahrscheinlichkeit.
- Der Klartext liegt ausserhalb des Agentenzugriffs in der Runden-Datei der Leitung und wird nach dem Lauf offengelegt.

## Rahmen

- Code-Agent, frischer Kontext.
- **Nicht lesen:** RUNDE-13/bball-leiter/ (alles), RUNDE-13.md, RUNDE-16.md, RUNDE-12/x-baelle/X-BAELLE.md, Journal-Eintraege
  ab nr 550. Dazu jeden Code der Linie bic2, afm_bic, bball, qstern.
- Der Code wird selbst geschrieben.
- Nur .69 ueber kleintest.sh, Spuren cpu3 und cpu4, jeder Aufruf hoechstens 10 min. Plan vor dem ersten Lauf einfrieren.
  Zeitbox 90 min.
