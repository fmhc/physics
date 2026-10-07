# B-BALL-2: Haengen die erste stille Stelle des Sextik- und des Log-Balls stetig zusammen? (Runde 13)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 19:40:07 CEST (date), vor jeder
  Codezeile und jedem Lauf dieser Karte.
- Herkunft: B-BALL-LEITER (ERGEBNIS.md).
  - Nach der Regel der Karte "nicht gesehen" in den Baendern bis omega^2 = 0,80. **Dieser Ausgang bleibt.**
  - Der nachtraegliche Lauf (Nachtrag 1, nach Kenntnis der Hauptlaeufe beschlossen, vor dem eigenen Lauf eingefroren)
    fand eine stille Stelle bei omega^2 = 0,925610, rho = 1,837996: auf zwei Stufen, Umlauf -1 aufgeloest, Breitenminimum
    2,9e-10.
  - Entscheidung der Leitung: Dieser Fund zaehlt nicht fuer die erste Karte. Er ist ein nachtraeglicher Befund ohne Test.
    Die Regel der ersten Karte wird nicht geaendert, deshalb braucht es dafuer keine Fremdstimme.
- Frage dieser Karte: Ist die Log-Stelle dieselbe Stelle wie die bewiesene Sextik-Stelle (omega^2 = 0,797677,
  rho = 1,744618), stetig verschoben? Das waere ein echter Test der Lesart "die erste stille Stelle ist nicht an das
  Sextik-Potential gebunden".

## Modell

- Mischpotential U_t(S) = (1 - t)(S - S^2 + S^3/2) + t ln(1 + S), t in [0, 1]. U_t'(0) = 1 fuer jedes t.
- Code: Kopie von bball.py unter neuem Namen. Einzige Aenderung: das Potential U_t mit U_t' und U_t'' und der Parameter t.
  Diff ablegen.

## Vorhersage (Leitung, vor jedem Lauf): lineare Interpolation zwischen den Endpunkten

| t | omega_t^2 (Vorhersage) | rho_t (Vorhersage) |
|---|---|---|
| 0,25 | 0,8297 | 1,7680 |
| 0,50 | 0,8617 | 1,7913 |
| 0,75 | 0,8936 | 1,8147 |

- Formel: omega_t^2 = 0,7977 + 0,1279 t, rho_t = 1,7446 + 0,0934 t.
- Kontinuitaet traegt (fuer alle drei t gefunden): ~70 %.
- Bei t = 0,5 liegt die gefundene Stelle hoechstens 0,015 in omega^2 von der linearen Vorhersage entfernt: ~60 %.
- Umlauf an allen drei Stellen -1, wie an beiden Endpunkten: ~85 %, falls gefunden.

## Suche

- Je t mindestens 17 Zeilen in omega^2 im Fenster omega_t^2 +- 0,04 (Abstand hoechstens 0,005). Feine rho-Abtastung bzw.
  direkte Nullstellensuche von L(y_b) wie in B-BALL-LEITER. Zwei Gitterstufen h = 0,02 und h = 0,01. Umlaufrechtecke
  wie dort, aufgeloest heisst groesster Phasensprung < 0,4 rad.

## Kontrollen (bindend)

- K1: t = 0 gibt die Sextik-Stelle (0,797677; 1,744618) auf 1e-4, Umlauf -1 auf beiden Stufen.
- K2: t = 1 gibt die Log-Stelle des Nachtrags (0,925610; 1,837996) auf 1e-4, Umlauf -1 auf beiden Stufen.
- Verfehlt K1 oder K2: nicht auswertbar.

## Regel (bindend, je t)

- **Gefunden:** Aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen, dazu ein Vorzeichenwechsel von s. Die Lage liegt
  im Fenster |omega^2 - omega_t^2| <= 0,04 und |rho - rho_t| <= 0,05, und die Stufen stimmen auf 1e-4 ueberein.
- **Nicht gefunden:** Im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.

**Gesamt:**

- "Kontinuitaet traegt": gefunden fuer alle drei t.
- "Kontinuitaet traegt nicht": fuer mindestens ein t nicht gefunden.
- Sonst unentschieden.

## Rahmen

Code-Agent (Fortsetzung des B-BALL-LEITER-Agenten). Nur .69 ueber kleintest.sh, Spuren cpu3 und cpu4, jeder Aufruf
hoechstens 10 min. PLAN-Nachtrag mit den Laeufen vor dem ersten Lauf einfrieren. Zeitbox 45 min.
