# Vorlage Ernte-Agent: frischer Leser, blind zum Arm

Die Leitung ersetzt <...> und gibt den Text als Auftrag an einen frischen Anthropic-Agenten (nie als fork: ein fork erbt
den Kontext der Leitung und ist nicht blind).

## Auftrag

- Karten: <G-Nummern> in /home/fmh/fmhc-physics/coordination/runden-v3/IDEEN-EVOLUTION/GEN-<NN>/. Je Karte: KARTE.md,
  NACHTRAG.md (falls da), LAUF.txt, lauf-69.log bzw. lokales Protokoll, Ausgaben.
- Du weisst nicht, woher eine Karte kommt, und sollst es nicht herausfinden: nicht lesen pool.jsonl, GEN-<NN>.md,
  HERKUNFT.md.
- Je Karte pruefen:
  1. **Vorab:** Liegt "Vorhersage geschrieben" zeitlich vor der "start"-Zeile des Laufs? Sonst "nicht als vorab
     belegbar" (RUNDE-06.md, Berichtigung 04:05:59, Punkt 2).
  2. **Vorwaerts:** Jede Zahl und jede Aussage der Karte zum Ergebnis steht in einer Ausgabedatei.
  3. **Rueckwaerts:** Jede Ausgabedatei auf rc ungleich 0, "bestanden": false, NaN, Warnungen, gerissene Schranke,
     fehlende Gegenprobe durchsehen. Steht das im Text? (Lehre: der Rueckwaertsdurchgang fand frueher falsche Zahlen.)
  4. **Latten:** L1 kann scheitern (ja oder schwach); L2 Effekt groesser als in der Gegenprobe; L3 Effekt mindestens
     fuenfmal so gross wie die Aenderung bei halbem Schritt; L4 schon bekannt (mit Fundstelle, sonst "nicht geprueft");
     L5 Messbezug.
  5. **Vorschlag:** weiter, parken oder verwerfen, ein Satz Grund. L1 schwach kann nicht weiter. L2 oder L3 gerissen:
     verwerfen oder parken mit Umbauvorschlag. Bekannt (L4): parken "bekannt".
- **Wortlaut der Belegebene:** nur sagen, was gemessen ist (Wert, Ort, Stufe, Haus); unter der Aufloesung nur obere
  Schranke; "auf dem Raster nicht gesehen" statt "gibt es nicht"; "verlaesst den Suchkasten" statt "erreicht die Kante";
  Deutungen als Hypothese.
- Ausgabe: GEN-<NN>/ERNTE.md mit Tabelle
  `| G-Nummer | vorab belegbar | Vorhersage getroffen | L1 | L2 | L3 | L4 | L5 | Vorschlag | Grund |`,
  darunter die Liste der Abweichungen in beide Richtungen und "Einfach gesagt".

## Grenzen

- Zeitbox 10 min. Zeiten nur mit `date` messen, nie schaetzen (Beginn und Ende in ERNTE.md).
- Nur lesen und ERNTE.md schreiben. Nichts rechnen, kein Python-Lauf.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrt, nicht oeffnen: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Antwort an die Leitung: hoechstens 5 Punkte, Ergebnis zuerst, "Einfach gesagt".
