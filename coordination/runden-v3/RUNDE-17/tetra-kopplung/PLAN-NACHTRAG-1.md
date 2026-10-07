# Nachtrag 1 zum Plan (NACHTRAEGLICH, nach Laufbeginn und nach Kenntnis der Ergebnisse)

- Geschrieben nach den Laeufen pruef, haupt2d, hauptfcc, auswert, rand (Zeitstempel im Dateinamen der eingefrorenen
  Fassung, per date).
- Anlass: K4 ist nach der vorab festgelegten Regel "offen", weil im fcc-Fernfenster [7,5, 22,6] auf [111] nur zwei
  Punkte in der unteren Fensterhaelfte liegen (Punkte bei d = 2,449 s); der Halbfenster-Exponent ist nicht berechenbar.
- Zusatzrechnung (aendert keinen Ausgang, K4 bleibt nach Regel "offen"): dieselbe Stufe hauptfcc mit M = 20, 40, 80
  kubischen Zellen. Fenster mit derselben Vorschrift wie im Plan, aber auf M = 80 bezogen: gesamt [3, L/4],
  fern [L/12, L/4] mit L = 80 sqrt 2 (L/4 = 28,3). Dann liegen auf [111] drei Punkte in der unteren und fuenf in der
  oberen Haelfte.
- Ausgabe als hauptfcc-nachtrag-<zeit>.json; wird im Ergebnis nur als nachtraegliche Zusatzinformation berichtet.
- Code-Aenderung dafuer: Fenster der Stufe hauptfcc aus der groessten angegebenen Groesse abgeleitet (fuer die
  Standardgroessen 16, 32, 64 identisch mit dem Plan), Ausgabename mit Zusatz "-nachtrag", wenn Groessen angegeben sind.
