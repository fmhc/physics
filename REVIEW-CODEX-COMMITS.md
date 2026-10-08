# Review der Codex-Commits vom 07./08.10.2026

Review durch Claude (Leitung) am 08.10.2026, Commits 68d46a5 bis b55eff4 (9 Commits, 102 Dateien). Geprueft: Aussagen
gegen die verlinkten Ergebnisdateien (Stichproben mit jq), Ueberzeichnungen, relative Links, Exportbereinigung,
Dateigroessen. Keine Rechnung wiederholt.

## Ergebnis

Die Higgs-Berichte sind sorgfaeltig: Vorabkriterien, QA, Grenzen, Fehlversuch und Exportaenderungen sind offen gelegt;
Prozentwerte werden ausdruecklich nicht angehoben. Keine Ueberzeichnung im Sinne von "bewiesen" oder "Durchbruch"
gefunden. Alle relativen Links in den geaenderten Markdown-Dateien existieren; die zitierten arXiv-Kennungen sind
abrufbar. Beide Eingabe-Hashes (B13-PROFILES.json, higgs-minima RESULT.json) stimmen mit den Dateien ueberein.

| Commit | Inhalt | Befund |
|---|---|---|
| 68d46a5 | zwoelf Bereichsgrafiken | als Schema gekennzeichnet. **Korrigiert:** Die Higgs-Karte sagte "Literaturvorarbeiten vorhanden" und verlinkte die EW-Literaturauswertung, obwohl 07cbeaa die Portalrechnungen B13 bis B23 nachgetragen hat; Text, Link und Generator angepasst. |
| 039e9ee | Literaturvergleich, Kandidatenmatrix, sieben Karten | sauber als [S]/[H] gekennzeichnet, keine neuen Simulationen behauptet. |
| 07cbeaa | Higgs-Bestandsaufnahme | Zahlen gegen B13-SUMMARY plausibel; Korrektur der frueheren README-Aussage offen gelegt. **Korrigiert:** die Higgs-Zeile in STAND-UND-NAECHSTE-SCHRITTE.md sprach noch von reiner Literaturvorarbeit. |
| 5e61c34 | zehn Verbindungsideen, OpenAI-Math-Notiz | Papierarbeit [M]/[H], Geltungsbereich der fremden Saetze sauber abgegrenzt. |
| bd26c78 | HIGGS-RESPONSE-1 | Tabellenspannen gegen RESULT.json nachgeprueft (Feingitter), stimmen. N2 wurde erst nach dem Scheitern von N bei g = 0,005 geplant; das ist im Bericht offen gelegt und in README/RESULTS jetzt ebenfalls genannt. |
| 9194f15 | HIGGS-FORCE-1 | alle 24 Gruppenwerte der Tabelle gegen RESULT.json geprueft, stimmen. |
| 7331499 | HIGGS-MINIMA-1 | Tabellenwerte gegen SUMMARY.json geprueft, stimmen. |
| 9dcebf0 | HIGGS-MODES-1 | Eigenwerttabelle gegen SUMMARY.json geprueft, stimmen. |
| b55eff4 | HIGGS-REDUCED-MODES-1 | **Korrigiert:** vier Werte waren aufgerundet statt gerundet (0,009883 statt 0,009882 %, 0,0002517 statt 0,0002516 %, 0,0001350 statt 0,0001349 Prozentpunkte, 5,55e-7 statt 5,54e-7). Konservativ, aber nicht wie angegeben. |

## Hinweise ohne Korrektur

- **Dateigroessen:** keine Datei ueber 2 MB. Fuenf JSON-Dateien mit Profilen liegen bei 1,0 bis 1,5 MB (zusammen etwa
  6 MB); sie sind Eingabe bzw. Rohprofile fuer die Reproduktion und bleiben. Ein Entfernen wuerde die Historie nicht
  verkleinern.
- **Rechnernamen:** Provenienz- und Ergebnisdateien nennen den Rechenrechner. Das
  ist Forschungsprotokoll und entspricht dem frueheren Export.
- **Darstellung:** Die README hatte fuenf aufeinanderfolgende Abschnitte "Neuer Befund". Sie sind jetzt in einem
  Abschnitt "Higgsportal-Linie" zusammengefasst, alle Links und Grafiken bleiben.
- **Offen:** Die Uebersicht der Verbindungsideen nennt unter "naechste Schritte" noch Tests, die inzwischen gerechnet
  sind (Nachtrag nur fuer Idee 01). Kein Fehler, aber veraltet.
