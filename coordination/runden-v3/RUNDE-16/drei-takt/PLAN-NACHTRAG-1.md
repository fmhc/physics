# PLAN-NACHTRAG-1 (nachtraeglich, vor den betroffenen Laeufen eingefroren)

- Geschrieben ab 2026-10-02 09:01:33 CEST (date). Nachtraeglich zum eingefrorenen PLAN (08:47:17).
- Anlass: Lauf 3 (D3, N = 4 ohne Takt, P = 2000) wurde nach 600 s von RuntimeMaxSec beendet (rc = 1, keine Ausgabe).
  N = 3 mit Takt (P = 2000) brauchte 528 s. Die Kosten je Schritt sind auf der .69 hoeher als geschaetzt.
- Bekannt vor diesem Nachtrag: nur die Kurzzahlen von N = 3 mit Takt (Lauf 4: lambda_max 0,29, 97 Punkte > 0,01).
  Die Aenderungen betreffen nur Aufteilung und Nachrechnung, nicht Schwellen, Modelle oder Vorhersagen.

## Aenderungen

1. D3, N = 4 ohne Takt: zwei Aufrufe mit P = 1000 (Seeds 21 und 22) statt einem mit P = 2000; zusammen 2000 Punkte,
   gleiches Protokoll (dt 0,02, Einschwingen 500, Messung 2000). Reicht die Zeitbox nicht, bleibt es bei Seed 21
   (1000 Punkte); das wird im ERGEBNIS als Abweichung gemeldet.
2. Nachrechnen neu mit code/d3_nach.py statt d3_kuramoto.py nachrechnen:
   - Alle Faelle in einem gemeinsamen Lauf, auf N = 4 aufgefuellt (Maske), damit der Python-Aufwand je Schritt nur
     einmal anfaellt.
   - Fehler im alten Nachrechnen behoben: Varianten dt/2 und doppelte Zeit benutzen jetzt die urspruenglichen
     Anfangswerte (exakt neu gezogen), die Variante "andere Anfangsbedingung" Seed + 3000.
   - Code-Pruefung: lambda(T) aus dem Lauf mit urspruenglichen Anfangswerten muss den Stichprobenwert wiedergeben
     (lokaler Rauchtest: Abweichung 0,0).
   - Je Fall hoechstens 40 Treffer (die groessten); Gesamtzahl der Treffer wird gemeldet. Schwellen: 0,005 fuer
     N = 2 mit Takt und N = 3 ohne Takt, 0,01 fuer N = 3 mit Takt und N = 4 ohne Takt. Robust = alle drei Varianten
     ueber der Schwelle des Falls.
   - Zwei Aufrufe: Modus BC (dt, Messung bis 2T; Variante C mit T) und Modus A (dt/2, T).
3. Werden in einem Kontrollfall mehr als 40 Punkte ueber 0,005 gefunden, gilt D3-1 nur fuer die 40 groessten als
   geprueft; der Rest wird als nicht nachgerechnet gemeldet.
