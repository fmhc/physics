# Anweisung: Dashboard-Sektion „Einfach gesagt" (Entwurf claude-primary, 13.09.2026; zum Codex-Review)

Zweck: Finn will zu jedem Lauf, Vertrag, Review und Rundenstand eine Erklärung von 3 bis 5 Sätzen auf Zehntklass-Niveau, mit Bild.
Die Erklärungen stehen NICHT im Forschungsjournal (dessen Einträge sind unveränderlich und fachlich), sondern in einer eigenen,
anhängbaren Quelle, die der Dashboard-Generator liest.

## Datenquelle
coordination/einfach-gesagt/einfach-gesagt.jsonl, eine JSON-Zeile je Erklärung, Felder:
- id (kebab-case, eindeutig), zeit (ISO mit Zone), bezug (Liste: Journal-IDs, Behauptungs-IDs wie "VB1.2", Vertragspfade),
- titel (≤ 80 Zeichen, Alltagssprache), text (3 bis 5 Sätze, keine unerklärten Fachwörter, keine Zahl ohne Quelle im bezug),
- bild (Pfad relativ zum Repo, PNG oder SVG unter model-lab/bilder/, optional), bildtext (ein Satz, was das Bild zeigt),
- stand (Freitext: „läuft", „Bronze", „verworfen", „Hypothese"), quelle (Pfad des Berichts).
Regeln: nur anhängen; Korrektur = neue Zeile mit gleicher bezug-Liste und Feld ersetzt (id der alten Zeile); Generator zeigt je
bezug die jüngste Zeile. Fehlende Bilder oder Felder dürfen den Bau nicht abbrechen (Warnung, Platzhalter).

## Darstellung im Dashboard (Generator model-lab/build_dashboard.py, nur dort)
- Eigene Sektion „Einfach gesagt" direkt unter „Heute neu", Anker #einfach-gesagt, Karten neueste zuerst; je Karte: Bild links
  (max 320 px, mit bildtext als alt und Bildunterschrift), rechts titel, text, Stand-Pille, Verweise auf bezug (Behauptungen als
  Anker ins Register, Journal-IDs als Anker in den Verlauf, Pfade als Links).
- Filter: alle / nur laufende / nur Bronze und höher; Standard alle, höchstens 12 Karten, Rest einklappbar.
- Schriften und Farben des bestehenden Dashboards, keine externen Ressourcen. Bilder werden nicht kopiert, sondern relativ
  verlinkt (Dashboard und Bilder liegen im selben Baum).
- Beim Bau: Warnung, wenn ein bezug auf eine unbekannte Behauptungs-ID oder Journal-ID zeigt oder ein Bild fehlt.

## Was Codex prüfen soll
1. Ist das Schema vollständig und robust (Korrekturkette, fehlende Felder, Encoding)? 2. Kollidiert die Sektion mit dem
Watch-Modus, der Signaturbildung oder den bestehenden Blöcken? 3. Barrierefreiheit (alt-Texte, Kontrast) und Phone-Breite.
4. Verbesserungsvorschläge in drei Zeilen, dann Umsetzung im Generator (Backup), Neubau, HTML-Prüfung.
