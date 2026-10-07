# PLAN-NACHTRAG-1 SPROSSEN-L1L2 (nachtraeglich, nach Laufbeginn)

- Geschrieben ab 2026-10-02 18:20:53 CEST (date), **nach** den Testlaeufen und der formalen Auswertung (ausw test
  16:19:43 UTC). Nachtraeglich; aendert keine Wertung und kein Kriterium.
- Anlass: Satz B, l = 2, k = 2, zweite Sprosse (P_lin 22,504) ist nicht angenommen. Newton fand von allen drei Starts
  (22,504; 22,254; 22,754) auf beiden Stufen dieselbe Wurzel (R = 22,2923, rho = 1,270287, Rang 2, abs(W) <= 2,1e-11).
  Die Stetigkeit verfehlte die Schwelle: Fehler 0,0057 bei d_nb 0,0414, Verhaeltnis 0,138 > 0,1. Den Rechteck-Umlauf
  rechnet der Testcode nur fuer lokal angenommene Versuche; hier fehlt er also.
- Frage (nur berichtet): Ist die Wurzel eine stille Stelle mit aufgeloestem Umlauf +-1 auf beiden Stufen, und setzt sie
  den Wechsel auf l = 2, k = 2 fort (17,68: +1, 20,01: -1, erwartet +1)?

## Verfahren

- Unveraenderter Vorlaeuferbefehl `quadrupol.py ell=2 umlauf` (HL.cmd_umlauf): Anker = naechste Zeile mit omega^2 <=
  Start, Newton S3.newton_E1 ab der Wurzel, Rechteck S3.umlauf_mit_rueckfall mit Halbbreite min(1e-3; 0,4 Randabstand;
  0,25 Luecke; 0,5 Zeilenabstand). Beide Stufen, Start = Wurzel der jeweiligen Stufe aus dem Test, Luecke = gap der
  Testzeile (0,0414340), Zeilenabstand 0,001422944988 (Zeilen 0,790622911565 / 0,789199966577). Eingaben
  hilfs/nachtrag1-punkt-st1.json und -st2.json, Ausgaben aus/nachtrag1/umlauf-st1.json und -st2.json.
- Zusaetzlich, reine Datenrechnung mit jq: Stetigkeitsmass derselben Wurzel (Fehler / d_nb der Testzeile) mit der
  Geraden in 1/R durch die letzten zwei bekannten Stellen (15,268 / 17,68) und mit der verketteten Parabel durch
  15,268 / 17,68 / 20,0114 (neue Sprosse dieses Tests).

## Wertung

- Keine. Die Sprosse bleibt formal "nicht angenommen". W1 bis W4 sind nicht beruehrt (nur Satz A). Im ERGEBNIS
  erscheint der Nachtrag getrennt und als nachtraeglich markiert.
