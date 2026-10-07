# Vorlage Test-Agent: kleiner Test je Karte, gleich fuer alle Arme

Die Leitung ersetzt <...> und gibt den Text als Auftrag an einen Anthropic-Agenten (frisch, kein fork). Der Agent erfaehrt
nicht, aus welchem Arm eine Karte stammt.

## Auftrag

- Karten: <G-Nummern>, Ordner /home/fmh/fmhc-physics/coordination/runden-v3/IDEEN-EVOLUTION/GEN-<NN>/<G-Nummer>/.
- Liegt dort noch keine KARTE.md, bekommst du eine alte Karte (Quelle <Pfad>, Kennung <ID>, bisheriges Ergebnis <Text>).
  Bringe sie nur ins Kartenformat unten, ohne neue Idee. War sie geparkt, nimm als Test den naechsten Schritt aus dem
  Parkgrund.
- Reihenfolge je Karte:
  1. **Karte fertig machen, bevor irgendetwas laeuft:** Vorhersage mit "scheitert, wenn", Gegenprobe und
     Plausibilitaetsschranke pruefen oder ergaenzen. Dann die Zeile "Vorhersage geschrieben: <Ausgabe von date>"
     eintragen und KARTE.md speichern. Danach KARTE.md nicht mehr aendern; Nachtraege in NACHTRAG.md. Die Vorhersage
     steht vor dem Entstehen jeder Ergebnisdatei, auch vor der Formprobe.
  2. **Code:** Kopie eines vorhandenen Rundenskripts in den Kartenordner, float64, Parameter als Argumente. Unveraendert
     lassen: das Original. Ausgabe als JSON und wenige Textzeilen. Pflicht im Code:
     - Hauptlauf und Gegenprobe als getrennte Laeufe
     - grob und fein (halber Zeit- bzw. Gitterschritt) fuer L3; Effekt mindestens fuenfmal so gross wie die Aenderung
     - die Plausibilitaetsschranke als eigene Pruefung mit "bestanden": true/false (Lehre aus Runde 5)
  3. **Formprobe:** lokal hoechstens 120 s, 1 Thread, `nice -n 19`, kleines Gitter; nur pruefen, dass der Code laeuft.
     Keine Aussage aus der Formprobe ernten.
  4. **LAUF.txt fuer die Leitung:** der Aufruf, z. B.
     `cd <Ordner auf der .69> && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> <skript.py> <argumente> | tee lauf-69.log`
     oder der lokale Aufruf mit `date` davor. Dazu die geschaetzte Laufzeit aus der Formprobe. Ueber 10 min: teilen oder
     "passt nicht in 10 min" melden.
  5. **Papiertest** zaehlt, wenn er scheitern kann (Vergleich mit einer veroeffentlichten Zahl oder einer eigenen
     Rechnung mit festgelegtem Ausgang). Kann eine Karte nicht scheitern, schreibe "L1 schwach" in NACHTRAG.md.
- Spuren: p4000a und p4000b sind GPU-Spuren (p4000b nur, wenn WM-1-MB nicht laeuft; kleintest.sh prueft das); cpu bis
  cpu4 nur fuer ausdruecklich CPU-faehige Skripte. Rechnen tut die Leitung, nicht du.
- Code-Basen (nur kopieren): RUNDE-06/resonanz3d/resonanz3d.py (3D-Pole, Bruecke ueber dim), RUNDE-02/tests1d/tests1d.py,
  RUNDE-03/tests2d-r3/tests2d_r3.py, RUNDE-05/r5a|r5b|r5c|r5d/*.py, RUNDE-05/r5-2d-a/r5_2d_a.py,
  RUNDE-05/r5-2d-b/r5_2d_b.py, RUNDE-06/weber/weber.py, RUNDE-06/medium1d/medium1d.py, RUNDE-06/medium2d/medium2d.py,
  RUNDE-01/qg1/qg1.py, RUNDE-06/kf4/kf4.py, RUNDE-06/reflexion/reflexion.py (alle unter coordination/runden-v3/).

## Grenzen

- Zeitbox 15 min fuer alle Karten zusammen. Zeiten nur mit `date` messen, nie schaetzen.
- Nur in die genannten Kartenordner schreiben. Keine Laeufe ausser der Formprobe.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Nicht aendern: gauntlet/ (eingefroren), die Original-Rundenskripte und laufende Ordner (RUNDE-07/bic2, r5f, ring, evo1).
- Gesperrt, nicht oeffnen: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Nicht lesen: IDEEN-EVOLUTION/pool.jsonl, GEN-<NN>.md und HERKUNFT.md (sie verraten den Arm).
- Antwort an die Leitung: je Karte eine Zeile (Code, Spur, geschaetzte Minuten, Formprobe ok), dann "Einfach gesagt".
