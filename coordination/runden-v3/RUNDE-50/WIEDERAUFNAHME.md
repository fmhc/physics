# Runde 50: Abbruch am Wochenlimit und Wiederaufnahme

- Geschrieben von der Leitung claude-primary am 06.10.2026 ab 18:08:56 CEST (date). Die Agenten brachen am
  05.10. abends ab, nach dem Protokolleintrag 19:46:00. Ursache: Das Wochenlimit des damaligen Kontos war erreicht
  (API-Fehler 429, Ruecksetzung laut Meldung am 10.10., 15:00).
- Pruefung am 06.10. um 18:08: Auf der .69 laeuft keiner dieser Laeufe mehr (keine Kleintest-Einheit aktiv), Platte 17 GB
  frei. Kein Agent hat ein Ergebnis abgegeben; es gibt keine Zahlen zu uebernehmen.

## Stand je Agent

| Aufgabe | lokal (RUNDE-37/...) | auf der .69 (fmhc-physics-remote/...) | Stand beim Abbruch |
|---|---|---|---|
| AEQUIVALENZ-DREI-1 | code/, lauf-69/, ERGEBNIS.md nur Platzhalter | aequivalenz-drei-1/ (1,1 MB) | Engine-Demos gesichtet, Messlaeufe begonnen; kein Ergebnis |
| QUANT-3 (SU(2) auf dem Zeltnetz) | code/, kette-a1.sh, kette-b1.sh, rauch1.sh, rauch2.sh, lauf-69/ | quant-3/ (8,6 MB) | GPU-Code fuer SU(2) gebaut, Rauchlaeufe; der Agent baute gerade die Messschleife um; keine Kontrolle S1 berichtet |
| NETZ-NICHTLINEAR-1 | code/, lauf-69/, rauch-69/, scan-69/ mit Pruefsummen | netz-nichtlinear-1/ (3,1 MB) | Rauch- und Scanlaeufe vorhanden; kein Ergebnis |
| FLUSS-TEXTUR-1 | nur KARTE.md und VORAB.md (Schreibtischprobe) | - | keine Rechnung |

## Wiederaufnahme (Reihenfolge nach Nutzen fuer das Ziel)

1. **QUANT-3** zuerst: SU(2)-Einschluss auf Finns Netz; das ist der Schluessel fuer Mesonen und Baryonen (Schritte c, d).
   Neuer Agent mit KARTE.md, dazu der vorhandene Code in code/ und lauf-69/ als Ausgangsstand. Sparfassung: erst S1
   (Kontrolle Hyperkubus), dann S2 und S3; S4 nur, wenn Budget bleibt.
2. **NETZ-NICHTLINEAR-1:** G1 (M_eff am gedehnten Netz im Zugzeitpunkt) auf s1, s2, s3; G2 nur bei Restbudget.
3. **AEQUIVALENZ-DREI-1:** AQ1 und AQ4 zuerst (passiv gegen traege), AQ2 (aktiv) danach.
4. **FLUSS-TEXTUR-1:** Zuerst VORAB.md lesen. Steht dort, dass die Kaefigprodukte per Konstruktion +1 sind, entfaellt die
   Rechnung.
- Fuer alle gilt: Erwartungen der Karten unveraendert lassen, vorhandene Dateien vor der Fortsetzung pruefen (Pruefsummen),
  df vor jedem Lauf.
- Ein Platz war fuer QUANT-1b reserviert (Q-Baelle aus vielen Quanten, Rechnung mit fester Ladung). Vorher klaeren, ob
  ag-phy-lat das rechnet; die Anfrage vom 05.10. ist unbeantwortet.
