# REGGE-HADRON-REF-L: Alle Referenzen von arXiv 2512.21805 pruefen und den Artikel einordnen (Runde 45, Finn-Auftrag)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 04:40:32 CEST (date), vor jedem Abruf des Agenten.
- **Finn (05.10., gegen 04:39), woertlich:** "Check in einem subagents Alle Referenzen hier https://arxiv.org/pdf/2512.21805 und ordne das ein".
- **Artikel [S Abstract-Seite, Abruf der Leitung 04:39]:**
  - D. Winney, A. P. Szczepaniak: "Regge theory in hadron physics", arXiv:2512.21805v1 (25.12.2025), hep-ph.
  - Auftragsartikel fuer die "Encyclopedia of Particle Physics", 23 Seiten, 14 Abbildungen.
  - Inhalt: paedagogische Einfuehrung in Regge-Theorie (Analytizitaet in der komplexen Drehimpulsebene, Geschichte vor und nach QCD, neuere Anwendungen: Austauschprozesse, Niederenergie-Amplituden, Resonanzen in der komplexen Drehimpulsebene).
- **Wichtige Abgrenzung [M]:**
  - Regge-Theorie (Streuamplituden, Regge-Trajektorien J = alpha(0) + alpha' M^2) ist nicht Regge-Kalkuel (Gravitation auf Kantenlaengen von Simplizes), mit dem das Projekt auf Finns Netz rechnet.
  - Gemeinsam ist nur der Namensgeber Tullio Regge.
- **Projektsuche:** "2512.21805" 0 Treffer.
- Kennzeichen: [S] mit Abschnitt bzw. Gleichung, [S Abstract], [L], [L?], [M], [ES], [H].

## Auftrag

1. **Referenzpruefung, vollstaendig:** jede Referenz des Artikels einzeln.
   - Existiert die Arbeit?
   - Stimmen Autoren, Titel, Zeitschrift, Band, Seite, Jahr und arXiv-Nummer?
   - Ist sie im Text an der Stelle zitiert, an der sie etwas belegen soll?
   - Fuer die tragenden Aussagen (Geschichte, Kernsaetze, Zahlen) eine Stichprobe von mindestens 10 Zitaten gegen die zitierte Quelle (Abstract genuegt, wo er die Aussage traegt).
2. **Relevanz je Referenz** fuer das Programm (0, 1 oder 2), mit einer Zeile Grund.
3. **Einordnung:**
   - Was ist der Artikel, wie verlaesslich ist er, wer sind die Autoren (Arbeitsgruppe)?
   - Was davon beruehrt das Programm [H]? Abzuklaeren:
     - Glied 7 der Spin-2-Kette: CEMZ verlangt einen unendlichen Turm massiver hoeherer Spins, also Regge-Verhalten bzw. Strings.
     - Das Pomeron als reggeisiertes Graviton (Brower/Polchinski/Strassler/Tan 2007 [L?]).
     - Q-Baelle als Teilchenmodell (Finn 05.10.: "Nur fürs Teilchenmodell"): Welche Drehimpuls-Masse-Beziehung haetten angeregte bzw. rotierende Q-Baelle gegen lineare Regge-Trajektorien? Nur als Frage und Literaturhinweis, nicht rechnen.
     - Finns Netz mit Flusslinien bzw. Strings: Flussroehren und lineare Trajektorien.

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| RH1 | [H] Alle oder fast alle Referenzen existieren und sind im Kern richtig zitiert (mindestens 97 % ohne sachlichen Fehler) | 80 % |
| RH2 | [H] Mindestens drei Referenzen haben kleine bibliografische Fehler (Jahr, Seite, Band, Schreibweise) | 60 % |
| RH3 | [L?] Der Artikel erwaehnt das Pomeron als reggeisiertes Graviton bzw. Gauge/String-Dualitaet (BPST) | 40 % |
| RH4 | [M] Der Artikel hat ausser dem Namen keinen Bezug zum Regge-Kalkuel | 90 % |
| RH5 | [L?] Der Artikel nennt das String- bzw. Flussroehrenbild der linearen Trajektorien (rotierender String, alpha') | 75 % |

**Bedeutung (vorab):**
- **RH1 trifft ein:** Der Artikel ist eine verlaessliche Uebersicht und als Quelle fuer Regge-Trajektorien nutzbar, etwa fuer Glied 7 und den CEMZ-Turm.
- **RH1 verfehlt:** Liste der Fehler an Finn; der Artikel taugt dann nicht als Quelle.
- **RH4 trifft ein:** Fuer Finns Netz direkt nichts. Bezuege nur ueber Strings, Glied 7 und Isotacheia [H].

## Rahmen

- feldforscher, Zeitbox 90 min.
- **Abrufe:** hoechstens 45, jeder mit Zeit, URL und HTTP-Code in quellen/ABRUFE.log.
  - Volltext per arxiv.org/pdf (pdftotext ist lokal vorhanden).
  - Referenzen gebuendelt ueber die INSPIRE-HEP-API (inspirehep.net/api/literature, Referenzliste mit Zuordnung; Abfragen mit mehreren recid bzw. arxiv-Nummern je Aufruf).
  - Dazu die arXiv-API (export.arxiv.org/api/query?id_list=... mit vielen IDs je Aufruf) und Crossref (api.crossref.org/works/DOI bzw. query.bibliographic) fuer Unzugeordnetes.
  - curl auf genau diese Dienste ist erlaubt; Rohantworten nach quellen/.
  - Websuche hoechstens 3-mal, nur fuer sonst unauffindbare Referenzen (war zuletzt erschoepft).
- Erwartung mit date-Zeit vor jedem Abrufbuendel in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/regge-hadron-ref-l/.
