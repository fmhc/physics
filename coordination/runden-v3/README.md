# Runden nach v3

Gilt seit 30.09.2026. Leitung claude-primary, Datei geschrieben 2026-09-30 00:18:30 CEST (gemessen). Finn, 30.09.2026:
"ja übernimm v3 und räum auf, nur archivieren".

- **Regeln:** coordination/evolution-review-20260929/V3-ENTWURF.md. Die Zeile "Entwurf; gilt erst nach Zustimmung" ist mit
  Finns Satz erfuellt; die Datei bleibt unveraendert. Begruendung in REVIEW.md daneben.
- **Kurz:**
  - Runde: Eingang, 8 bis 15 Karten, 3 bis 5 kleine Tests plus eine Zufallskarte, je hoechstens 10 min Rechnung.
  - Jeder Test wird an den fuenf Latten gemessen: L1 kann scheitern, L2 Gegenprobe, L3 Numerik, L4 schon bekannt,
    L5 Messbezug.
  - Danach je Karte: weiter, parken oder verwerfen.
  - Formale Tests nur nach zwei Runden "weiter" mit Messbezug: Vertrag auf einer Seite, eine Lesung durch ein anderes
    Haus, dann rechnen.
- **Buchfuehrung:**
  - eine Datei je Runde (RUNDE-NN.md), Code und Ausgaben in RUNDE-NN/
  - ein Journaleintrag je Runde
  - keine VORAB-Dateien, OTS-Stempel oder Hashketten fuer Ideen
- **Rechenorte fuer kleine Tests** (seit 30.09.2026 01:31; Finn: "mach die kleinen tests auf anderen karten oder auf cpu"):
  - Kleine Tests (hoechstens 10 min) laufen parallel zu grossen Laeufen ueber kleintest.sh.
  - Spur p4000a: Quadro P4000 GPU-a5689af6, eigener Lock.
  - Spur cpu: eigener Lock, nur fuer ausdruecklich CPU-faehige Skripte.
  - Die WM-1-MB-Karte GPU-8fab62d5 bleibt frei.
  - Grosse Laeufe behalten den gemeinsamen Lock gauntlet-gpu.lock.
- **Bleibt unabhaengig davon:**
  - Zeiten mit date
  - Datensperren
  - keine lokalen Interpreter auf dem Laptop
  - Rechnen auf der .69 ueber Controller und den gemeinsamen Lock
  - Journal nur ueber research_journal.py
- **Laufende formale Straenge von vorher:**
  - VS-1 laeuft als explorativer Hauptlauf.
  - B28, WM-1-MB und CX-1 warten auf das Ollama-Pausenfenster.
  - KS-1-DK-DR4 ruht bei Codex, Frist 2.12.
  - Sie werden nach ihren eigenen Vertraegen zu Ende gefuehrt oder geparkt. Neue formale Straenge gibt es nur nach v3,
    Abschnitt 5.
- **Aufraeumen (nur archivieren):** ARCHIV-20260930.md
