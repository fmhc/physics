# GAMMA-NETZ-L: Wenn Finns Netz der Raum ist, lenkt es Licht richtig ab? Was legt gamma (PPN) im Netz fest? (Literatur-, Code-Lese- und Schreibtischkarte, Runde 43)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 19:32:45 CEST (date), vor jedem Abruf.
- **Finn (04.10., zwischen 19:28 und 19:31), woertlich:** "3: der raum ist das netz denke ich. raum sind punkte die linien
  ergeben die mehrdimensionalität erscahffen und diese linien sind die geometrien, das netz auf dem sich alles abspielt,
  ggf gibt es noch geometrien in den linien"
  - Antwort auf R1 aus GEMEINSAMES-NETZ-L: Das Netz ist die Geometrie, kein festes Geruest. Marolfs Satz trifft dann
    nicht unmittelbar; Umbauten muessen Umbenennungen sein (wie Regge/CDT).
- **Messanker:** Cassini gamma - 1 = (2,1 +- 2,3)e-5 (STRANG-ANKER-L).
- **Projektstand (zuerst lesen):**
  - RUNDE-35/SCHREIBTISCH-QBALL-EIS-LAPSE.md (Wege zur Lichtablenkung; Spin 2 an T_mu_nu gibt die volle Ablenkung)
  - RUNDE-37/eine-welt-loch-1/ (ERGEBNIS.md und code/ew.py: Finns Netz mit gefuellten Loechern, eine Welt mit 2
    TT-Moden, alle anderen Moden mit Luecke, Stabilitaet nur mit "skalaren Regeln" je Ecke)
  - RUNDE-37/pachner-takt-1/ (3+1 mit Zeltstangen)
  - RUNDE-37/takt-umbenennung-l/DOSSIER.md (1/2 als Passbedingung)
  - RUNDE-37/gemeinsames-netz-l/DOSSIER.md (Marolf, BDGH)
- **Schreibtisch der Leitung [M, nicht gegengelesen]:**
  - Sind ausser den 2 masselosen TT-Moden alle Moden gelueckt, geben die gelueckten Skalare nur Yukawa-Beitraege
    ~ e^(-m r). Langwellig bleibt gamma dann bei dem Wert, den die Zwangsbedingungen (Hamilton-Bedingung) festlegen.
  - gamma = 1 verlangt, dass die "skalaren Regeln" die diskrete Hamilton-Bedingung sind (raeumliche Kruemmung aus der
    Energiedichte) und dass die Lapse (h_00) aus derselben Kopplung folgt.
  - Ist die Regel etwas anderes, kann gamma von 1 abweichen.
- Kennzeichen: [S], [S Abstract], [P], [L], [L?], [M], [ES], [H].

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung |
|---|---|
| E1 | Linearisierte Regge-Rechnung gibt im Kontinuumsgrenzfall die linearisierte ART samt Graviton-Propagator (Rocek/Williams 1981-84) [L] |
| E2 | Eine Hamilton-Fassung von Regge mit Zwangsbedingungen je Ecke existiert; die Zwangsbedingungen sind auf gekruemmtem Hintergrund nicht exakt erster Klasse (Dittrich/Hoehn, Bahr/Dittrich) [L] |
| E3 | Gelueckte Zusatzmoden (massive Skalare) geben Yukawa-Korrekturen; gamma - 1 ~ (Kopplung) e^(-m r) wie bei massiven Brans-Dicke-Skalaren [L] |
| E4 | Fuer emergente Gravitonen aus Gittermodellen ist gamma meist nicht berechnet; wo doch, haengt es an der Kopplung der Materie an die Geometrie [L?] |

## Fragen

1. Was sind die "skalaren Regeln" in EINE-WELT-LOCH-1 (code/ew.py lesen): Sind sie die diskrete Hamilton-Bedingung, eine
   Eichfixierung oder etwas anderes?
2. Folgt gamma = 1 fuer Finns Netz mit gefuellten Loechern dann vorab (ableitbar), oder bleibt ein rechenbarer Rest?
3. Welche Literatur berechnet gamma bzw. die statische Antwort fuer Regge- oder Gitter-Gravitation?
4. Hoechstens ein Rechenkartenvorschlag mit Ableitbarkeitsprobe, nur fuer den nicht ableitbaren Rest (zum Beispiel
   statische Punktmasse auf dem gefuellten Netz mit Lapse aus PACHNER-TAKT-1).

## Auftrag (feldforscher)

- **Abrufe:**
  - Hoechstens 8 gezielte Abrufe (arXiv; jeder API-Aufruf zaehlt als einer).
  - Keine Websuche. Lokale Kopien in quellen/.
- **Code nur lesen:** RUNDE-37/eine-welt-loch-1/code/, RUNDE-37/pachner-takt-1/code/. Nichts ausfuehren.
- **Projekt-grep** nur mit Ausschluss versiegelter Pfade: --exclude-dir=vertraege-20260925, --exclude-dir=ks-1-dk-lauf,
  --exclude-dir=ks-1-dk-laeufe und Dateien mit VERSIEGELT oder T8-SOLL im Namen.
- **Arbeitsweise:** Feld-Regeln (Erwartung vor Abruf mit date-Zeit, eine Arbeitsdatei ARBEITSFELD.md, Gegensweep) und
  Dimensionsvergleich (3+1 gegen 2+1: in 2+1 keine Gravitonen).
- **Abgabe:** DOSSIER.md mit:
  - Ergebnis zuerst
  - Pruefung des Schreibtischs
  - Erwartungen mit Ausgang
  - Antworten 1 bis 4
  - Selbstanzeigen
  - "Einfach gesagt" (3 bis 5 Saetze, fuer Finn)
- **Rahmen:** Zeitbox 75 min. Kein Rechnen; lokal kein python, awk oder perl; nichts in den Scratchpad der Leitung.
