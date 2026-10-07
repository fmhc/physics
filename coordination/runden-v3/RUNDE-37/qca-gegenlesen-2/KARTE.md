# QCA-GEGENLESEN-2: Frischer Leser fuer QCA-BCC-RUECK-1 (Teilbeweis, Ableitbarkeit, Masse mit Rueckspruengen) (Runde 39)

- Leitung claude-primary. Auftrag geschrieben ab 2026-10-04 10:34:49 CEST (date).
- **Anlass:** QCA-BCC-RUECK-1 ist fertig (RUNDE-37/qca-bcc-rueck-1/ERGEBNIS.md; Ernte in RUNDE-39.md).
  - 4 Zustaende unter der vollen Tetraedergruppe T: kein Automat mit Rueckspruengen (Suche plus Teilbeweis, nicht
    gegengelesen).
  - 8 Zustaende (2+2+2'+2'): 17 Automaten mit Rueckspruengen; je vier masselose Weyl-Kegel bei k = 0, in erster Ordnung
    isotrop, 360 Grad = -1, Verdoppler an H, P und P'.
  - Frueher fanden Gegenleser mehrfach zu starke Saetze der Leitung zu QCA (RUNDE-37/qca-gegenlesen/GEGENLESEN.md). Bevor
    die Leitung das Finn meldet, soll ein frischer Leser pruefen, was traegt und was vorab ableitbar war.
- Kennzeichen: [S] an der Quelle gelesen, [M] Mathematik, [ES] eigener Schluss, [L] Literatur aus dem Gedaechtnis.

## Fragen

1. **Teilbeweis (4 Zustaende):** Ist er richtig? Was genau ist bewiesen, was stuetzt sich nur auf die Suche? Laesst sich
   die Luecke am Schreibtisch schliessen oder ein Gegenbeispiel bauen?
2. **Ableitbarkeit von QR2 und der Kegel-Eigenschaften:**
   - Erzwingt Schur bei 2-dimensionalen Spinor-Darstellungen von 2T die Entartung bei k = 0 und damit Kegel?
   - Folgen "masselos unter T ohne Inversion", "isotrop in erster Ordnung" (einziger T-invarianter Tensor in 3 x 3?) und
     "360 Grad = -1" ohne Rechnung?
   - Urteil je Eigenschaft: vorab ableitbar / teilweise / nicht.
3. **Inversion und Rueckspruenge:** Inversion bildet die BCC-Richtungsgruppen S+ und S- aufeinander ab. Erfuellt dann
   jeder inversionskovariante Automat die Rueckspruung-Bedingung der Quelle von selbst? Haben die massiven Loesungen aus
   QCA-DIRAC-T-1 (RUNDE-37/qca-dirac-t-1/) Spruenge in beide Gruppen? Wenn ja: "Masse mit Rueckspruengen" ist dort schon
   gezeigt, und eine Folgekarte QCA-DIRAC-RUECK-1 waere ueberfluessig.
4. **Kartenluecke "direkte Summe":** Ist das Urteil je unzerlegbarem Teilautomaten sauber definiert und richtig
   angewandt? Koppelt die Muenze in den 17 Treffern Vorwaerts- und Rueckwaertsteil wirklich (keine direkte Summe)?
5. **Verdoppler an H, P, P':** zwingend (Nielsen/Ninomiya sinngemaess fuer Automaten) oder Eigenschaft dieser Loesungen?
6. **Rueckwaerts gegen die Texte der Leitung:** die Ernte "QCA-BCC-RUECK-1" in RUNDE-39.md und den Nachtrag 10:26:59 in
   RUNDE-39/WEICHE-STAND-v2.md Satz fuer Satz gegen ERGEBNIS.md und lauf-69/auswertung.json lesen. Jede zu starke,
   falsche oder ungenaue Stelle mit Vorschlag im Wortlaut.

## Quellen (nur lesen)

- RUNDE-37/qca-bcc-rueck-1/: KARTE.md, PLAN.md (eingefroren), ERGEBNIS.md, lauf-69/auswertung.json, code/, Beweistext
  (falls eigene Datei)
- RUNDE-37/qca-dirac-t-1/, RUNDE-37/qca-diamant-4/, RUNDE-37/qca-tetra-1/, RUNDE-37/qca-gegenlesen/GEGENLESEN.md
- Literatur nur, falls noetig: hoechstens 3 gezielte Abrufe (D'Ariano/Erba/Perinotti, PRA 96, 062101 (2017); D'Ariano/
  Perinotti 2014); Fundstellen nur aus selbst gelesenem Text.

## Abgabe

- RUNDE-37/qca-gegenlesen-2/GEGENLESEN.md:
  - Ergebnis zuerst: je Frage ein Urteil in einem Satz
  - Befunde nach Gewicht: A (falsch oder zu stark, muss geaendert werden), B (sollte), C (kann); je Befund Fundstelle und
    Vorschlag im Wortlaut
  - Ableitbarkeitstabelle: Eigenschaft, vorab ableitbar ja/teilweise/nein, Begruendung
  - "Einfach gesagt" (3 bis 5 Saetze)

## Rahmen

- Zeitbox 50 min. Schreibtisch; keine neuen Laeufe. Lokal kein python, awk oder perl; jq, grep, sed zum Lesen erlaubt.
- Versiegeltes nie oeffnen: Dateien mit VERSIEGELT im Namen, coordination/vertraege-20260925/, KS-1-Ergebnisse,
  T8-SOLL-*, ks-1-dk-lauf/, ks-1-dk-laeufe/. Keine Geheimnisdateien.
- Nur in RUNDE-37/qca-gegenlesen-2/ schreiben; nicht in /tmp/claude-1000/ (Scratchpad der Leitung). Zeiten nur per date.
- Nichts an den Dateien anderer Karten oder der Leitung aendern.
