# VORTEX-RAD: Drehende Feldklumpen (Wirbel) auf Rad-Graphen (Runde 18)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 14:12:39 CEST (date), vor jeder Rechnung.
- Anlass:
  - arXiv:2610.00774 (gelesen: nur Abstract). Auf einem Sterngraphen mit vier Armen gibt es einen diskreten Wirbel mit
    fester topologischer Ladung, getragen von der Verzweigung.
  - Unsere Rad-Graphen (Ring aus N Knoten plus Nabe, V5 und S6) mit dem Q-Ball-Potential sind das naechste Gegenstueck.
  - Ein Wirbel ist ein drehender Feldklumpen mit ganzzahligem Drehimpuls, ein Gitter-Gegenstueck zum drehenden Q-Ball.
- Dazu Finns Zahlen: N = 11 und 19 sind Primzahlen, 12 und 20 nicht. Bei Wirbeln mit Ladung m auf einem N-Ring
  entscheiden die Teiler von N, welche Ladungen Untersymmetrien haben. Hier kann eine Primzahl einen echten Unterschied
  machen [H].
- Explorativ (v3), Hypothesen [H].

## Modell

- Gleichung wie V5: Psi_i'' + Sum_j J (Psi_i - Psi_j) + V'(|Psi_i|^2) Psi_i = 0 mit V' = 1 - 2S + 1,5 S^2.
- Stationaer gilt Psi_i = phi_i e^{i omega t}, phi komplex.
- **Wirbel mit Ladung m:** phi_j = A_j e^{2 pi i m j/N} auf dem Ring.
  - Fuer m ungleich 0 (mod N) entkoppelt die Nabe: Die Summe der Ringphasen ist null, also ist phi_Nabe = 0 eine Loesung.
  - Gleichfoermiger Wirbel (alle A_j = A), Schreibtisch [ES]: V'(A^2) = omega^2 - J (3 - 2 cos(2 pi m/N)).
- **Stabilitaet:** Linearisierung im mitrotierenden Phasenbild fuer komplexes phi.
  - Volle reelle 2(N+1)-Darstellung mit gyroskopischem Term.
  - Spektral stabil heisst: alle Exponenten auf der imaginaeren Achse, nach Abzug der Phasen-Nullmode.
- **Scan:**
  - N = 4..24 (darin 11, 12, 19, 20), alle m = 1..floor(N/2)
  - grosser und kleiner Ast der Einzelplatzloesung, J in {0,02; 0,05; 0,1}, omega^2 im Existenzfenster
  - Zusaetzlich lokalisierte Wirbel, die aus dem Antikontinuumslimes auf einem Teil des Rings fortgesetzt werden, sofern
    sie existieren.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| W1 | Der gleichfoermige Wirbel erfuellt die Schreibtischformel auf 1e-10; die Nabe bleibt null | 95 % |
| W2 | Auf dem grossen Ast sind Wirbel mit m = 1 bei kleinem J fuer viele N spektral stabil | 60 % |
| W3 | Die Stabilitaet haengt von m/N ab (z. B. instabil nahe m = N/2), nicht davon, ob N prim ist | 60 % |
| W4 | 11 und 19 sind bei gleichem m/N nicht stabiler als ihre Nachbarn 10, 12 bzw. 18, 20 | 70 % |
| W5 | Instabilitaeten sind oszillatorisch (Krein-Kollision), nicht reell | 55 % |

**Bedeutung (vorab):**
- Treffen W2 und W5 ein: Drehende Feldklumpen mit ganzzahligem Drehimpuls gibt es auf dem Rad stabil. Instabil werden
  sie durch Kollision gegenlaeufiger Moden, ein Gitter-Gegenstueck zum drehenden Q-Ball [H].
- W3 und W4 pruefen, ob Finns Primzahlen bei Wirbeln eine Rolle spielen.

## Rahmen

- Code-Agent. V5-Code (RUNDE-16/zwei-seiten/ausprobieren/code/v5_feld.py) und S6-Code
  (RUNDE-16/stabil-6-8-12/code/stabil_s6.py) duerfen gelesen werden.
- Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6, je <= 10 min. Plan vorab einfrieren. Zeitbox 90 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
