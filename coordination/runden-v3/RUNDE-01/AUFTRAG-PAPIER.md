# Runde 1, Papiertests F-1, F-3 und K-2 (Anthropic)

Auftraggeber: claude-primary (Leitung). 30.09.2026 nach 00:00:02 CEST (Rundenbeginn gemessen). Deutsch. Explorativ, leicht.

## Rahmen

- Finn will einfache Basics statt Prozessapparat. Eine Runde testet Ideen kurz und schaetzt dann ab, was sich weiter lohnt.
- Lies zuerst coordination/runden-v3/RUNDE-01.md und coordination/evolution-review-20260929/V3-ENTWURF.md (Abschnitt 2,
  fuenf Latten L1 bis L5).
  FINN-IDEE-Dateien.
- Unser Q-Ball-Modell: lagebericht/qball-atlas.html. Codex rechnet explorativ mit U = S - S^2 + S^3/2, S = |phi|^2 (pruefe
  am Atlas, ob das dasselbe Potential und dieselbe Normierung ist).

## Drei Papiertests (je etwa 1 h; jeder endet mit einer Zeile L1 bis L5 und einem Vorschlag: weiter, parken oder verwerfen)

1. **F-1:** Welche Brechung der Verschiebungssymmetrie entlang der Extra-Richtung ergaebe eine Einfangregel, die sich
   messbar vom Standardbild unterscheidet? Die vier Kandidaten stehen in ABSCHAETZUNG-RUNDE-1.md unter F-1:
   - Anregungsturm
   - Masse an Ladung gekoppelt
   - Massenaenderung in Stoessen
   - keine statische Anziehung gleichnamiger KK-Teilchen
   Pruefe an der Quelle:
   - Overduin und Wesson, Kaluza-Klein-Uebersicht (Phys. Rep. 1997): Gilt die Kraftfreiheit zwischen KK-Moden?
   - Solitosynthese (Griest und Kolb 1989): Wachsen Q-Baelle durch Einfang freier Quanten?
   - hep-ph/0006344 "Stable Q-balls from extra dimensions"
   Ergebnis: Gibt es mindestens einen bezifferbaren Unterschied, der mit Daten kollidiert oder sie trifft? Wenn nein, ist
   F-1 "andere Sprache fuer Bekanntes"; das ist ein gueltiges Ergebnis.
2. **F-3:**
   - Leite die Duenne-Wand-Grenze unseres Potentials her.
   - Vergleiche sie mit der Beutelformel E(R) = a/R + (4 pi/3) B R^3 (MIT-Beutel) bzw. Friedberg-Lee. Welche unserer
     Groessen spielt B, welche die innere Bewegung?
   - Lies an drei Q-Werten aus dem Atlas M und R ab, falls die Zahlen dort stehen. Bilde das dimensionslose M*R in unseren
     Einheiten und pruefe, ob es konstant ist.
   - Nichts an 938 MeV oder 0,84 fm anpassen.
3. **K-2:**
   - Lies arXiv 2609.24913 (Boson Star Factory; Gervalle u. a.). Welche Potentiale? Gibt es flache Q-Baelle ohne Gravitation
     mit Tabellenwerten (E, Q, omega, gegebenenfalls J)?
   - Passt eines zu unserem Potential, oder laesst sich unser Loeser ohne Umbau auf deren Potential stellen?
   - Schreibe einen Laufplan fuer die .69 von hoechstens 10 min, mit Gegenprobe (zwei Gitter, ein absichtlich falscher
     Koeffizient).
   - Enthaelt die Arbeit keine flachen Q-Baelle, sag das und parke die Karte.

## Abgabe (Ordner coordination/runden-v3/RUNDE-01/)

- F1-PAPIER.md, F3-PAPIER.md, K2-LESUNG.md
- Jede Datei: Ergebnis zuerst, Latten-Zeile, Vorschlag, "Einfach gesagt" (3 bis 5 Saetze)
- Quellen mit arXiv-ID oder DOI; was du nicht selbst gelesen hast, als [aus dem Gedaechtnis] markieren

## Grenzen

- Nur lesen, Web und Schreiben in diesen Ordner. Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik.
- Kein ssh, kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Geheimnisse.
- Gesperrt:
  - KS-1-Ergebnisse, T8-SOLL-*
  - coordination/vertraege-20260925/
  - coordination/vertraege-20260927/ks-1-dk-lauf/ und ks-1-dk-laeufe/
- Zeiten mit `date`. Budget hoechstens 90 Minuten.
