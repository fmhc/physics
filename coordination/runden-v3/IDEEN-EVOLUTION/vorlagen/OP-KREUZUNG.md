# Vorlage Operator "kreuzung": zwei Karten verbinden

Die Leitung ersetzt <...> und gibt den Text als Auftrag an einen Anthropic-Agenten (frisch, kein fork).

## Auftrag

- Elternkarte A <ID>: <Befund>, Belege <Pfade>. Elternkarte B <ID>: <Befund>, Belege <Pfade>. Neue Karte: <G-Nummer>,
  Ordner /home/fmh/fmhc-physics/coordination/runden-v3/IDEEN-EVOLUTION/GEN-<NN>/<G-Nummer>/.
- Nimm den Mechanismus der einen Karte und setze ihn auf den Befund der anderen, oder frage, ob beide Befunde denselben
  Grund haben.
- Die Kreuzung muss etwas vorhersagen, was keine Elternkarte allein vorhersagt. Sonst ist L1 "schwach", und die Karte
  kann nicht "weiter".
- Guter Test: ein Eingriff, der die zwei Deutungen trennt ("wenn A den Befund von B erklaert, dann aendert die Stoerung X
  das Ergebnis um Y; sonst bleibt es").
- Liefere genau eine Karte (KARTE.md) und HERKUNFT.md. Kennzeichen [L], [S], [A].

## Kartenformat KARTE.md (ohne Herkunft; die Ernte liest blind)

```
# <G-Nummer> <Titel>
- Hypothese: ein Satz.
- Kleiner Test: Code-Basis (vorhandenes Rundenskript oder Papier), Rechenort (.69-Spur p4000a/p4000b/cpu..cpu4,
  Laptop-CPU oder Papier), Laufzeit hoechstens 10 min, neuer Code hoechstens 1 h.
- Vorhersage vorab: Zahl oder Richtung mit Spanne; "scheitert, wenn ...".
- Gegenprobe: Lauf oder Vergleich, in dem der Effekt verschwinden muss.
- Plausibilitaetsschranke: z. B. 0 <= T <= 1, Ladungs- und Energiebilanz, v < 1.
- Latten erwartet: L1 kann scheitern (ja/schwach), L2 Gegenprobe, L3 Numerik (halber Schritt), L4 bekannt, L5 Messbezug.
- Einfach gesagt: 3 bis 5 Saetze auf Niveau zehnte Klasse.
- Karte geschrieben: <Ausgabe von date>   (die Zeile "Vorhersage geschrieben" setzt der Test-Agent)
```

Regel: Die Vorhersage steht vor dem Entstehen jeder Ergebnisdatei. Der Test-Agent setzt vor jedem Lauf die Zeile
"Vorhersage geschrieben: <date>"; ab dann bleibt KARTE.md unveraendert, Nachtraege in NACHTRAG.md. HERKUNFT.md: Operator, Eltern, Quellen, Beginn und Ende (date).

## Grenzen

- Zeitbox 15 min. Zeiten nur mit `date` messen, nie schaetzen.
- Nur in den eigenen Kartenordner schreiben. Nichts rechnen ausser Papier; kein Python-Lauf.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Nicht aendern: gauntlet/ (eingefroren) und laufende Ordner (RUNDE-07/bic2, r5f, ring, evo1).
- Gesperrt, nicht oeffnen: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Nicht doppeln: `grep` in IDEEN-EVOLUTION/pool.jsonl und RUNDE-07.md; keine Frage, die BIC-2, R5F, RING, EVO-1 oder
  Codex (R-2) schon stellt.
- Explorativ: neue Ideen sind Hypothesen; synthetische Kontrollen sind keine Messdatenbestaetigung.
- Antwort an die Leitung: hoechstens 5 Punkte, Ergebnis zuerst, "Einfach gesagt".
