# Gauntlet v2, Runde 8 eingefroren (Wiederaufnahme nach needs_evidence; F1 neu, M1.5/T4.3 gepatcht)

- Zeit: 2026-09-12 06:30
- Quelle: run.json Wiederaufnahme (Backup run.json.bak-20260912-wiederaufnahme-r8), runde.py briefe; rounds/008/manifest.json
- Ergebnis: Lauf stand nach Runde 7 auf needs_evidence (zwei Runden ohne Stufenwechsel). Neue Evidenz: F1 (Faden-Vertrag 1, Nachtrag 3 Q-Kriterium), M1.5 und T4.3 mit umgesetzten Patches. Nutzerfreigabe Runde 8 (Relais claude-x1). Runde 8 eingefroren, acht Behauptungen auf drei Briefe, Wasserlinie 400. KEINE Codex-Richter durch claude-primary gestartet (Marken-Tagessumme 2,79 Mio ueber der 2-Mio-Regel; Freigabe nur relayed); Jury dieser Runde faehrt claude-x1 ueber OpenRouter auf Finns Wort wie in Runden 1 und 2.
- Bedeutung: Ernte bleibt bei claude-primary nach Eingang der Urteile in der koordination-Tabelle.

- Befund 2026-09-12 11:16: Vertrag 4 (Morse-Kette/Helix, Rev. 12b, Startsignal 5f53014a gueltig seit 08:2x) hat seit 08:14 keine Bahn, keine Pacht und keine laufende Einheit auf .69; Anstoss (10:16) und Erinnerung (10:46) an claude-x1 blieben unbeantwortet. Ausfuehrung bleibt bei claude-x1; Uebernahme nur auf Nutzerwort.
- Aufloesung 11:35: Ursache des Stillstands war ein Verbindungsabbruch x1 -> precision waehrend der Validierung; der Controller wurde nie gestartet. Jetzt Runner als Unit auf precision (morse-runner-x1-20260912-1132), Validierung 12b 24/24 bestanden, Blockcontroller laeuft unter halber GPU-Pacht claude-x1. Kein vertragsseitiges Hindernis.
