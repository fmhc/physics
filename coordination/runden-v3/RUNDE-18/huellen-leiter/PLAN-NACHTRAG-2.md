# PLAN-NACHTRAG-2 (HUELLEN-LEITER) - NACHTRAEGLICH

- Geschrieben ab 14:21 CEST (date), nach Laufbeginn. Nur Ablauf (Zeitnot, PLAN 7), kein Verfahren, keine Wertungsregel.
- Anlass: Mit Nachtrag 1 (Illinois) kostet eine Zeile bei R ~ 33 auf Stufe 1 etwa 12 s statt 3,6 s; hochgerechnet reicht
  die Zeitbox nicht fuer alle 263 Zeilen auf beiden Stufen. Bloecke ueberschreiten teils die 600-s-Grenze.
- Ablauf ab jetzt:
  1. Die Bloecke unterhalb der Zeile ~210 (R > ~88), die noch nicht begonnen hatten, werden nicht gestartet
     (Anspruchsordner vorbelegt): Stufe 1 220-235, 235-250; Stufe 2 213-222, 222-231, 231-240, 240-248, 248-255.
     Bereits laufende bzw. schon beanspruchte Bodenbloecke (Stufe 1 250-262, Stufe 2 255-262) laufen zu Ende. Ihre
     Zeilen bilden eine "Insel" an der Schranke (R ~ 110 bis 116), getrennt ausgewertet und als Insel berichtet.
  2. Lueckenfueller: Nach dem Ende jedes Blocks (auch bei Abbruch an der 600-s-Grenze) rechnet ein zweiter Aufruf
     desselben Blocks nur die fehlenden Zeilen und Paare (bestehende Dateien werden gelesen).
  3. Gewertet wird der zusammenhaengende Bereich von omega^2 = 1,40 abwaerts bis zur tiefsten Zeile, bis zu der auf
     beiden Stufen alle Zeilen und Paare vorliegen (PLAN 7: "nicht erreicht" unterhalb). L2 bis L5 werden auf diesem
     Bereich gewertet; die Insel wird zusaetzlich berichtet und nicht in L3/L4 eingerechnet, weil zwischen Bereich und
     Insel Stellen fehlen.
