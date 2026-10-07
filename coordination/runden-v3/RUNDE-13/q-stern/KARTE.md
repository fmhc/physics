# Q-STERN: Ueberlebt die erste stille Stelle schwache Eigengravitation? (Runde 13, Vorschlag T2 aus X-BAELLE)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 20:12:26 CEST (date), vor jeder
  Codezeile und jedem Lauf.
- Herkunft:
  - RUNDE-12/x-baelle/X-BAELLE.md, Abschnitt T2. Kleihaus/Kunz/List 2005 nutzen fuer Bosonensterne dieselbe
    Sextik-Familie (an der Quelle geprueft).
  - Schwerpunkt Gesamtformel: Materie-Ball plus Gravitation.
- Frage: Bleibt die bewiesene stille Stelle (l = 0, n = 1; omega^2 = 0,797677, rho = 1,744618) bestehen, wenn der Ball
  sein eigenes Newton-Potential spuert? Wohin wandert sie?

## Modell (Newton-Grenzfall, statischer Hintergrund; bindend)

- Schwaches Feld, Metrik ds^2 = -(1 + 2 Phi) dt^2 + (1 - 2 Phi) dx^2, Wirkung bis erste Ordnung in Phi:
  L = (1 - 4 Phi)|d_t phi|^2 - |grad phi|^2 - (1 - 2 Phi) U(|phi|^2), mit U = S - S^2 + S^3/2.
  - Der Agent prueft diese Entwicklung in HERLEITUNG.md nach, bevor er rechnet. Weicht sie ab, gilt seine Fassung mit
    Begruendung. Die Leitung wird informiert, die Regel bleibt.
- Hintergrund phi = f(r) e^{i omega t}:
  - f'' + (2/r) f' = (1 - 2 Phi) U'(f^2) f - (1 - 4 Phi) omega^2 f
  - Phi'' + (2/r) Phi' = alpha rho_E mit rho_E = omega^2 f^2 + f'^2 + U(f^2)
  - Randbedingungen: f'(0) = 0, Phi'(0) = 0, f(inf) = 0, Phi(inf) = 0
  - selbstkonsistent loesen
- Linearisierung in **Cowling-Naeherung**: Phi bleibt im Hintergrund fest, die Schwingung wirkt nicht auf Phi zurueck
  (delta Phi = 0).
  - Zwei Kanaele omega +- rho wie bisher, nur mit den Faktoren (1 - 4 Phi) an den Frequenztermen und (1 - 2 Phi) an
    U' und U''. Schwelle weiter 1, weil Phi(inf) = 0.
  - Die volle Rechnung erster Ordnung mit delta Phi ist eine spaetere Karte. Diese Karte prueft nur die Naeherung, und
    der Bericht sagt das so.
- Langreichweite: Phi ~ -M/r. Die Abstrahlamplitude ist so auszulesen, dass die Coulomb-Phase das Ergebnis nicht
  verfaelscht. Pruefung K3.

## Kontrollen (bindend)

- K1: alpha = 0 gibt die bewiesene Stelle auf 1e-4, Umlauf -1 auf beiden Stufen.
- K2: Hintergrund auf zwei Gittern. omega, Q, E und Phi(0) stimmen auf 1e-6 relativ ueberein.
- K3: Aussenrand R und 1,5 R. Die Lage einer gefundenen Stelle aendert sich um weniger als 1e-4.
- Verfehlt eine Kontrolle: nicht auswertbar fuer das betroffene alpha.

## Regel (bindend, je alpha in {0,01; 0,03; 0,1})

- **Gesehen:**
  - aufgeloestes Rechteck mit Umlauf +-1 auf beiden Stufen und ein Vorzeichenwechsel von s
  - Lage im Fenster 0,70 <= omega^2 <= 0,90, 1,6 <= rho <= 1,9
  - Lagen der Stufen auf 1e-4 gleich, K3 bestanden
- **Nicht gesehen:** im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.
- alpha = 0,01 ist nur eine Stetigkeitskontrolle. Dort ist "gesehen" wegen der Stetigkeit fast erzwungen, es zaehlt nicht
  als Test. Echte Tests sind alpha = 0,03 und 0,1.
- Der Bericht nennt je alpha die Kompaktheit 2|Phi(0)| und Phi am Ballrand. Ab 2|Phi(0)| > 0,1 ist der Newton-Grenzfall
  fraglich; das wird vermerkt.

## Vorhersage (Leitung, vor jedem Lauf)

- K1 bis K3 bestehen: ~80 %.
- Gesehen bei alpha = 0,03: ~90 %. Bei alpha = 0,1: ~75 %.
- Verschiebung bei alpha = 0,1: |Delta omega*^2| <= 0,05 (~70 %).
- Richtung: omega*^2 sinkt mit alpha (~55 %; die Gravitation bindet staerker, wie ein kleineres omega).
- Umlauf -1 wie bei alpha = 0: ~90 %, falls gesehen.

## Rahmen

Code-Agent. Code aufbauend auf RUNDE-13/bball-leiter/bball2.py bzw. RUNDE-12/afm-kanal2/afm_bic.py, als Kopie unter neuem
Namen. Nur .69 ueber kleintest.sh, Spuren cpu und cpu2, jeder Aufruf hoechstens 10 min. Laufzeit vorab mit Rauchtest
messen. PLAN vor dem ersten Lauf einfrieren. Zeitbox 75 min.
