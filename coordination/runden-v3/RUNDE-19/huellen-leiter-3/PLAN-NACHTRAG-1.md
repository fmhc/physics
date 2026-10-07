# PLAN-NACHTRAG-1 (HUELLEN-LEITER-3) - NACHTRAEGLICH

- Geschrieben ab 16:37:52 CEST (date), nach Laufbeginn (Ketten seit 16:31:48) und nach der formalen K0'-Auswertung
  (16:36, bestanden). Gesehen hatte ich vorher: K0' vollstaendig; von den Testlaeufen die Logzeilen von Stufe 1 Teil b
  (k = 3 / 41,93; k = 0 / 42,00; k = 2 / 42,36; k = 1 / 42,62), Stufe 1 Teil a bis k = 3 / 39,77 und Stufe 2 Teil b
  (k = 2 / 40,24; k = 1 / 40,51), sowie die Zeilen-Knotenzahlen der Stufe 1 Teil b.
- **Befund:** Beide k = 3-Sprossen scheitern auf Stufe 1 nur an der Knotenzahl (Plan 4: muss dem Wert der Runde 18
  gleichen, k = 3 -> 2). Unter Variante S hat die Nullstelle mit Rang 3 die Knotenzahl 3; Rang, Fenster, Konvergenz und
  Rangabfall sind erfuellt (R = 39,765 bzw. 41,912).
- **Ursache (aus erlaubten Daten von HUELLEN-LEITER-2, aus/laeufe, nach dem Befund nachgesehen):** Unter S hat k = 3
  schon im K0-Bereich die Knotenzahl 3 (Zeilen 100, 105, 108, 110 der Stufe 1, R = 33,9 bis 38,95; Stufe 2 Zeile 110
  ebenso), Runde 18 dort 2. Die Knotenzahl der c-Komponente haengt also wie das Vorzeichen von s von der Saat ab. Das
  Kriterium in Plan 4 vergleicht eine S-Knotenzahl mit einer Knotenzahl der Kopplung der Runde 18. Das ist ein Fehler
  meines Plans; ich haette die Zeilen von HUELLEN-LEITER-2 vorher pruefen koennen.
- **Wertung bleibt unveraendert nach PLAN.md.eingefroren-20261002-163036:** Annahme, P1', P2', Kontrolle und
  Bedeutung werden genau wie dort festgelegt ausgewertet (Befehl ausw-test, Code unveraendert). Nichts wird nach dem
  Ergebnis umgedeutet.
- **Diagnose D1 (nachtraeglich, keine Wertung):** An den S-Wurzeln aller 8 Sprossen (Stufe 1, und Stufe 2 bei Zeit)
  Rang und Knotenzahl mit Variante F und mit der Kopplung der Runde 18 (alt), je eine Zeilenrechnung zeile_k.
  Erwartung [H]: F gibt fuer k = 0 bis 3 die Knotenzahlen 0, 0, 2, 2 wie Runde 18. Neuer Code nur in
  code/diag_knoten.py (importiert huellen_leiter3.py unveraendert). Bericht getrennt als Diagnose.
