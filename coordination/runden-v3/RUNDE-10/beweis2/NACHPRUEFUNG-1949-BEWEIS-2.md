Urteil: umgesetzt mit Resten (3 Textreste, 1 Punkt mit Hinweisen; Strenge von T1 und T2 unberuehrt)

# Nachpruefung der Aenderungen 1949 an BEWEIS-2 (frischer Leser, Haus Anthropic)

- Beginn (date): 2026-09-30 19:52:17 CEST
- Auftrag: Leitung claude-primary, Nachricht im Chat (keine BRIEF-Datei mit Pfad und sha256 genannt; Auftrag = Nachrichtentext)
- Gegenstand: diff BEWEIS-2.md, BEWEIS-2-PLAN.md, STAND.md gegen *.bak-20260930-1949
- Grundlage der Befunde: LESUNG-LETZTE-SCHICHT-BEWEIS-2.md (L1 bis L5, OpenAI A4)
- Werkzeuge: nur date, ls, diff, grep, sed -n, jq, sha256sum

## Frage 1: Umsetzung der Befunde L1 bis L5 und OpenAI A4

| Befund | Stelle (neue Zeilen) | umgesetzt | Anmerkung |
|---|---|---|---|
| L1 Ordnungswoerter, Knotenaussage | BEWEIS-2.md 34, 68, 493-497; PLAN 25-26 | ja | "erste Schwapp-Stelle", "naechste", "erste Schwappschwingung", "hat mehr Knoten" sind weg; Plan: "Leiteretikett ..., keine zertifizierte Knotenzahl". Kleine Unschaerfe 497: "Ihre Nummern stammen aus der Datensammlung", obwohl "Einfach gesagt" keine Nummern mehr nennt und 21/Plan 25 "Datenpaket" sagen (Hinweis). |
| L2 R < r_j nur fuer r_j > 0; R_kleiner_rj_alle | 114-117, 131-133, 153, 208; 459 als "ueberholt" markiert | ja | Bildung "(R < r_j) oder r_j = 0" stimmt mit pruef-l0.py:590; true in schritte_punkt und schritte_kasten aller 5 ZERT (jq). |
| L3 Quelle N, qfac; Mechanismus | 112-113, 118-120, 131-133, 208 | ja | Code nachgelesen: bewkern.py:359-360 Fehler("R >= rj"); 575-583 except -> Rt * 7/10, raise erst bei Rt < 1/1000; 567 Rt = min(Rmax, rfrac r_j), dyf = floor (527-530), also R <= r_j/2 exakt. Kleinigkeit 112: kommandozeile ist Unterfeld von parameter (jq: .kommandozeile = null, .parameter.kommandozeile vorhanden). |
| L4 Einfach gesagt zuruecknehmen, "linear"; Abschnitt 8 und STAND | 493-502; 470-484; STAND 33-34 | teilweise | "linear" zweimal, offene Punkte genannt, 13:15-Aenderungen nachgetragen. Rest: Die Lesung nannte als dritten Grund die nicht umgesetzten OpenAI-Codehinweise. Sie fehlen in "Offen bleiben" (500-502), obwohl Tabelle 469 sagt "Vermerkt, keine Codeaenderung" (Bereichspruefung l, alte Kommentare A'(0) = 1). Veraltete Kommentare sind selbst Beschreibungsfehler, die nicht berichtigt sind. Damit ist "die gefundenen Beschreibungsfehler sind berichtigt" (500) noch etwas zu weit. |
| L5 kaum kleiner; :238; OpenAI je Satz | 256-257, 402-403; 249-251; 22-23, 361-362, 449-450, STAND 34 | ja | Richtung stimmt (jq), Fehlerausschluss begrenzt. Zitat 22-23 mit Zusatz, siehe Frage 2 (c). STAND 31 bleibt als Protokollzeile unveraendert, der Nachtrag steht in 34; das ist vertretbar. |
| OpenAI A4 (n als Leiterzuordnung) | ueber L1; 21, 377, 467 | ja | Nach L1 bleibt kein Ordnungswort und keine positive Knotenaussage (Frage 3). |
| Befund 9 (Hinweis) | 267-269 | ja, aber | aufgenommen; Schluss zu stark, siehe Frage 2 (a). |

## Frage 2: Neue Behauptungen, neue Zahlen gegen zertifikat/*.json

**Zahlen (jq, Rechnung im Kopf); alle stimmen:**
- N = 64/48 bzw. 72/44, --q 3 bzw. 4 (112-113): ZERT-T1-A parameter N_punkt 64, N_kasten 48, "--q 3"; T1-B 72, 44, "--q 4". Stimmt.
- 1,64e-3 und 1,54e-3 (B) gegen 1,34e-3 und 1,26e-3 (A) (256-257): D_relbreite[2][0] und [3][0] in T2-B = T2-B2 0,00164 und 0,00154, T2-A 0,00134 und 0,00126. Stimmt.
- "zwoelfmal" (257): delta[0] 2,1107e-20 gegen 1,7451e-21. 1,7451 * 12 = 20,941, Rest 0,166, also Faktor 12,1. Stimmt.
- 42,0 = 19,1 + 22,9 (250): 19,1 + 22,9 = 42,0; protokoll.zeilensumme_gewichtet 41,99858. Die Aufteilung 19,09 und 22,91 stammt aus der Lesung (Zeilen 71-73). Stimmt.
- M1 19,10 (250): M1.rowsum 19,102934. Stimmt.
- delta_c mal 2^17, "allein" (250): Der einzige Parameterunterschied B/B2 ist dcexp 17. delta[1] 9,0274e-10 gegen 6,8874e-15; 6,8874 * 1,31072 = 9,0275, also Faktor 1,3107e5 = 2^17. delta[0], [2], [3] sind gleich. Stimmt.
- 26282 (267): T1-A schritte_kasten.relw_f_bei_L 26282,36. Stimmt; 2872 ist T2-A mit 2871,54.
- Faktor 29 (268): T1-A 7,33e-5 und 5,50e-5, T1-B 2,54e-6 und 1,90e-6. 73,3 / 2,54 = 28,9 (2,54 * 29 = 73,66) und 55,0 / 1,90 = 28,9 (1,90 * 29 = 55,1). Stimmt.
- R < 1/1000, R <= r_j/2 (119-120): Code, siehe Frage 1 L3. Stimmt.
- "erster Schritt bei r_j = 0 ist die Reihe um 0 nach Lemma T0" (114): bewkern.py:354-357 hat einen eigenen Zweig first = (rj == 0) ohne 1/r; Zeile 106 ordnet T0 der Vorwaertsintegration zu. Das ist konsistent; einen Lemma-Wortlaut habe ich nicht gelesen.

**Neue Aussagen, die mehr sagen als belegt:**
- (a) **267-269 "Ein breites f allein erklaert die l = 1-Breite also nicht."** Der Gegenfall vergleicht nur Absolutwerte (T1-A 26282 gegen T2-A 2872). Von A nach B aendert sich f bei L aber in beiden Saetzen in dieselbe Richtung wie die D-Breite (jq relw_f_bei_L Kasten):
  - T2: f von 2872 auf 14558, also etwa x5,1 (2872 * 5 = 14360); D-Breite von 1,34e-3 auf 1,64e-3, also x1,22.
  - T1: f von 26282 auf 9595, also etwa /2,7 (9595 * 2,7 = 25907); D-Breite /29, bei delta_a /383.
  - Der Befund widerlegt Kandidat 2 also nicht. Der Satz steht zudem direkt vor "Beides ist ungeprueft" (270).
  - Anforderung: als Hinweis fassen (etwa "spricht gegen f als alleinige Ursache der Hoehe, nicht der Aenderung"), nicht als Schluss. Das stammt schon aus Befund 9 der Lesung und beruehrt T1 und T2 nicht.
- (b) **500 "die gefundenen Beschreibungsfehler sind berichtigt"**: nicht fuer die veralteten Code-Kommentare (OpenAI-Codehinweis, 469). Siehe L4.
- (c) **22-23 "T1 'traegt' im eingeschraenkten linearen radialen Sinn"**: Der Zusatz "linearen radialen" geht ueber das Zitat der Lesung hinaus ("im eingeschraenkten Sinn", LESUNG-LETZTE-SCHICHT:200). GESAMT-REVIEW.txt:6-13 habe ich nicht geoeffnet. An der Quelle pruefen oder die Anfuehrung auf "traegt" begrenzen. In 361-362 und 449-450 fehlt der Zusatz; dort ist er stimmig.
- (d) Hinweis: 470-471 datieren die Aenderungen auf 13:15. BEWEIS-2.md.bak-20260930-1949 hat mtime 13:18, PLAN.bak 13:15. Aus den Dateien ist die Zeit nur fuer den Plan belegbar; die Zeitangabe ist aber ohne Folgen.

## Frage 3: Ordnungswoerter und Knotenaussagen ausserhalb der geaenderten Zeilen

grep -n -i -E 'erste|naechst|zweite (Sprosse|Atmung|Schwapp|Mode|Schwingung|Stelle)|dritte|Sprosse|Knoten|Oberton|Grund(zustand|mode|schwingung|ton)|angeregt|hoehere', dazu 'zweit|Stufe|tiefst|unterst' in BEWEIS-2.md und BEWEIS-2-PLAN.md:
- "erste/erster" betrifft nur Integrationsschritte oder Fassungen, keine Leiter: BEWEIS-2.md 114, 127, 154, 209, 228 ("die erste Fassung"), 321, 322; PLAN 45 ("vor dem ersten T2-Lauf").
- "hoeherem l" (405) meint den Drehimpuls l, nicht n.
- "Knoten" steht nur verneint ("keine zertifizierte Knotenzahl"): 21, 377, 467, PLAN 25.
- "zweit" steht nur in "zweites Programm" oder "zweites Seitenband" (25, 93, 251, 366, 487, 500).
- Kein "naechste", keine "Sprosse", kein "Grundzustand" o. ae.
- **Ergebnis: keine Fundstelle, die "n nur als Leiteretikett" widerspricht.** "eine weitere Atmungsschwingung" (495) und "Schwapp-Leiter" (68) ordnen nicht.

## Reste und Urteil

Urteil: **umgesetzt mit Resten** (alle Reste Text; keiner beruehrt T1 oder T2).
1. 267-269: "also nicht" ist ein Schluss, den der Gegenfall nicht traegt. Von A nach B laeuft die f-Breite bei L in beiden Saetzen gleichsinnig mit der D-Breite (Frage 2 a).
2. 500-502 (L4 teilweise): Der OpenAI-Codehinweis (veraltete Kommentare A'(0) = 1, Bereichspruefung l; 469) fehlt in "Offen bleiben". "die gefundenen Beschreibungsfehler sind berichtigt" ist deshalb noch zu weit.
3. 22-23: Der Zusatz "im eingeschraenkten linearen radialen Sinn" im OpenAI-Zitat ist an der Quelle ungeprueft; die Lesung zitiert nur "im eingeschraenkten Sinn".
4. Hinweise: 497 "Ihre Nummern ... Datensammlung" (keine Nummern im Absatz; sonst "Datenpaket"); 112 "Felder parameter und kommandozeile" (kommandozeile ist Unterfeld); 470-471 "13:15" nur fuer den Plan per mtime belegbar.

- Letzte Zeitmessung vor diesem Eintrag (date): 2026-09-30 19:59:13 CEST. Dauer ab Beginn 19:52:17: 6 min 56 s (19:52:17 + 7 min = 19:59:17, minus 4 s). Zeitbox 12 min eingehalten.
- Quote: 6 von 6 Befunden (L1 bis L5, OpenAI A4) umgesetzt, davon 5 ganz und 1 teilweise (L4). 9 von 9 neuen Zahlengruppen stimmen mit zertifikat/ bzw. Code ueberein. 3 Reste, dazu 1 Punkt mit Hinweisen.
