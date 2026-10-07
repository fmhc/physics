# Vorlage Operator "research": Literatur und arXiv auf eine Karte werfen

Die Leitung ersetzt <...> und gibt den Text als Auftrag an einen Anthropic-Agenten (frisch, kein fork).

## Auftrag

- Elternkarte <ID>: <Befund in zwei Saetzen>, Belege <Pfade>. Neue Karte: <G-Nummer>, Ordner
  /home/fmh/fmhc-physics/coordination/runden-v3/IDEEN-EVOLUTION/GEN-<NN>/<G-Nummer>/.
- Vor dem ersten Suchabruf: eine Zeile Erwartung in HERKUNFT.md, was die Literatur vermutlich sagt (mit `date`).
- Suche in arXiv (die letzten 24 Monate zuerst) und in den Standardarbeiten. Jedes Zitat an der Quelle lesen (Abstract
  oder Volltext); ein Suchtreffer-Schnipsel ist kein Beleg. Kennzeichen: [L] Literatur, [S] eigene Papierrechnung,
  [A] Projektdatei.
- Liefere zwei Dinge:
  1. In HERKUNFT.md eine L4-Notiz zur Elternkarte: bekannt, teilweise bekannt oder nichts gefunden, mit Fundstelle.
  2. Genau eine neue Karte (KARTE.md): ein Mechanismus oder eine Messung aus der Literatur, die unseren Befund testbar
     schaerft. Messbezug (L5) bevorzugt: eine veroeffentlichte Zahl, gegen die unser Modell im kleinen Test antritt.
- Kein "widerlegt" ohne Suche ueber 24 Monate. Bezug zu Quantengravitation und Grundlagen als Hypothese kennzeichnen.

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
- Nicht doppeln: `grep` in IDEEN-EVOLUTION/pool.jsonl und RUNDE-07.md; keine Frage, die BIC-2, R5F, RING oder EVO-1
  (beta, gamma) schon stellt.
- Explorativ: neue Ideen sind Hypothesen; synthetische Kontrollen sind keine Messdatenbestaetigung.
- Antwort an die Leitung: hoechstens 5 Punkte, Ergebnis zuerst, "Einfach gesagt".
