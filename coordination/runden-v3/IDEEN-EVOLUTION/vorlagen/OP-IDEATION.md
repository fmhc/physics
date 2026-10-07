# Vorlage Operator "ideation": frische Idee ohne Elternkarte (Arm F)

Die Leitung ersetzt <...> und gibt den Text als Auftrag an einen Anthropic-Agenten (frisch, kein fork).

## Auftrag

- Neue Karte: <G-Nummer>, Ordner /home/fmh/fmhc-physics/coordination/runden-v3/IDEEN-EVOLUTION/GEN-<NN>/<G-Nummer>/.
- Programm: Quantengravitation und Grundlagen, Traeger ist unser Q-Ball-Modell (komplexes Feld, U = S - S^2 + S^3/2,
  S = |phi|^2; Stand in RUNDE-07/IDEATION-UEBERSICHT.md, Abschnitte 5 und 6). Der Bezug zur Grundlagenphysik ist eine
  Hypothese und wird so benannt.
- Schreibe zuerst in HERKUNFT.md fuenf Rohideen in je einer Zeile, dann waehle eine: die mit der schaerfsten Vorhersage,
  die im kleinen Test scheitern kann.
- Keine Umformulierung einer der 131 Poolkarten (`grep` in IDEEN-EVOLUTION/pool.jsonl) und nichts, was BIC-2, R5F, RING
  oder EVO-1 schon rechnen.
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
"Vorhersage geschrieben: <date>"; ab dann bleibt KARTE.md unveraendert, Nachtraege in NACHTRAG.md. HERKUNFT.md: Operator, Rohideen, Quellen, Beginn und Ende (date).

## Grenzen

- Zeitbox 15 min. Zeiten nur mit `date` messen, nie schaetzen.
- Nur in den eigenen Kartenordner schreiben. Nichts rechnen ausser Papier; kein Python-Lauf.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Nicht aendern: gauntlet/ (eingefroren) und laufende Ordner (RUNDE-07/bic2, r5f, ring, evo1).
- Gesperrt, nicht oeffnen: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Explorativ: neue Ideen sind Hypothesen; synthetische Kontrollen sind keine Messdatenbestaetigung.
- Antwort an die Leitung: hoechstens 5 Punkte, Ergebnis zuerst, "Einfach gesagt".
