# Runde 18 (v3, explorativ)

Leitung: claude-primary. Angelegt: 2026-10-02 12:44:17 CEST (date). Runde 17 ist abgeschlossen (RUNDE-17.md; Journal
claude-runde-v3-17-20261002, Index nr 554; Sicherung r17 gestartet, r16 rc = 0).

## Uebernommen

- M_E-G3 (Codex; Statusfrage vom 11:53 offen)
- chi-Teil der Huellen-Stellen unabhaengig pruefen -> Karte HUELLEN-UHR
- Kandidaten unter omega^2 0,82; Dimensionsmesser auf wachsendem Graphen; Lektuere verzweigte Gitter

## HUELLEN-UHR gestartet (2026-10-02 12:45:06 CEST)

- Karte RUNDE-18/huellen-uhr/KARTE.md (ab 12:44:17), Code-Agent auf cpu/cpu2, Zeitbox 120 min.
- Unabhaengiger Zeitbereichstest zweier Huellen-Stellen (S-a 0,86086/1,06976; S-b 0,84743/1,33956). Arme:
  - BIC-Mode
  - dieselbe Form bei verschobenem omega^2 (nicht still)
  - generischer Stoss
  - Nullarm
- Vorhersagen:
  - H1: Nullarm ohne Ticks (95 %)
  - H2: Ticks mit 2 pi/rho (85 %)
  - H3: Abstrahlung der BIC mindestens 30-mal kleiner (65 %)
  - H4: eps^4 gegen eps^2 (55 %)
  - H5: generischer Stoss strahlt > 50 % ab (70 %)
- Aktive Agenten: HUELLEN-UHR (einer).

### Loop-Durchgang (2026-10-02 13:16:27 CEST)

- Codex: keine Antwort auf die Statusfrage (seit 11:53).
- HUELLEN-UHR: Plan eingefroren 12:56:48, Nachtrag 1 13:01:25. Laeuft.
- **Gelesen [S: Abstract, arXiv-API]:** arXiv:2610.00774.
  - DNLS auf einem PT-symmetrischen Sterngraphen mit vier Kanten.
  - Ein diskreter Wirbelzustand mit fester topologischer Ladung, getragen von der Verzweigung. Fortsetzung aus dem
    Antikontinuumslimes, wie bei uns in V5/S6.
  - Mit Gewinn und Verlust wird daraus ein stromtragender Zustand mit eigenen Stabilitaetsfenstern. Vorgeschlagen ist eine
    Realisierung als elektrische Schaltung.
- **Idee fuer eine spaetere Karte [H]:** Wirbelmoden auf unseren Rad-Graphen.
  - Am Ring Phasenwindung m, die Nabe bleibt bei m ungleich 0 (mod N) entkoppelt.
  - Mit dem sextischen Potential ist das ein Gitter-Gegenstueck zu drehenden Q-Baellen mit ganzzahligem Drehimpuls.
  - Fragen: Fenster und Stabilitaet gegen N und m.

### Ernte HUELLEN-UHR (Agent fertig ~13:40; RUNDE-18/huellen-uhr/ERGEBNIS.md; ausgewertet 2026-10-02 13:40:13 CEST)

Plan eingefroren 12:56:48, nach der Karte (12:44:17). Nachtrag 1 (Modenwahl, Aufteilung) vor dem ersten Lauf eingefroren.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| H1 | Nullarm ohne Ticks, Bilanz < 1e-6 | **eingetroffen**: keine Ticks, Energie- und Ladungsbilanz 2e-11 |
| H2 | Ticks mit 2 pi/rho auf 1e-3 | **eingetroffen**: 50 Ticks in 50 Perioden, Periode auf 5e-6 bis 4e-5 |
| H3 | Abstrahlung (i) mindestens 30-mal kleiner als (ii) | **eingetroffen**: (i) 3,7e-5 (S-a) bzw. 5,3e-5 (S-b) bei eps = 0,002; (ii) 1,32 bzw. 0,76, also 2300- bis 35000-mal mehr |
| H4 | (i) ~ eps^4, (ii) ~ eps^2 | **eingetroffen**: Exponenten 4,000 bzw. 2,00 |
| H5 | generischer Stoss > 50 % | **eingetroffen**: 91 % bzw. 68 % |

- Kontrollen:
  - Reflexion des Schwamms <= 3,6e-7.
  - Zwei Gitter (h = 0,05 und 0,025) gleich.
  - Die Mode liegt bei lambda = 0, hoechstens 4e-8 vom rho der Karte; sie klingt im offenen Kanal ab.
  - Der neu geloeste Hintergrund trifft Q auf 2,5e-8.
- Grenzen:
  - Bei (ii) sind Resonanzzerfall und Sofortabstrahlung nicht getrennt.
  - S-b (ii) ist chi-dominiert (chi-Amplitude bis 0,19).
  - Nur l = 0.
- Selbstanzeigen des Agenten:
  - Namensliste von kleintests/
  - lokal head, tail, sleep, chmod (nicht auf der Liste)
  - Zwischenauswertung vor dem letzten Paar angesehen; danach nichts geaendert
- **Bedeutung (vorab festgelegt):** Die Huellen-Stellen sind im Zeitbereich mit einem unabhaengig geschriebenen Loeser
  bestaetigt. Der chi-Teil der Streurechnung stimmt. Die Huelle macht den Ball zu einer Uhr ohne Energieverlust in erster
  Ordnung; der Restverlust ist rein nichtlinear (eps^4) [H, im Modell gestuetzt].
- Damit tragen drei Rechnungen die Huellen-Stellen:
  - Frequenzbereich, Code 1 (STILLE-ZWEIFELD)
  - blinder Code 2, post hoc (ZWEIFELD-NACHBAU)
  - Zeitbereich, Code 3, vorab gewertet (HUELLEN-UHR)
- **Abschaetzung: weiter** -> HUELLEN-LEITER (Struktur und Vollstaendigkeit der Stellen).

## HUELLEN-LEITER gestartet (2026-10-02 13:40:57 CEST)

- Karte RUNDE-18/huellen-leiter/KARTE.md (ab 13:40:13), Code-Agent auf cpu bis cpu4, Zeitbox 120 min.
- Vollstaendige Suche omega^2 0,74 bis 1,40 in E1, Ordnung nach chi-Kurven, Leiterfrage (Haeufung zur duennen Wand).
- Vorhersagen:
  - L1: 15 bekannte wiedergefunden (90 %)
  - L2: >= 10 neue unter 0,819 (60 %)
  - L3: dichter zur Schranke (70 %)
  - L4: Abstand in R etwa konstant (50 %)
  - L5: fuenfte chi-Kurve (45 %)
- Aktive Agenten: HUELLEN-LEITER (einer).

## VORTEX-RAD gestartet (2026-10-02 14:13:26 CEST)

- Karte RUNDE-18/vortex-rad/KARTE.md (ab 14:12:39), Code-Agent auf cpu6, Zeitbox 90 min.
- Drehende Feldklumpen (Wirbel, Ladung m) auf Rad-Graphen N = 4..24, mit Stabilitaet im mitrotierenden Bild. Pruefung,
  ob Primzahlen wie 11 und 19 eine Rolle spielen.
- Vorhersagen:
  - W1: Schreibtischformel (95 %)
  - W2: m = 1 stabil bei kleinem J (60 %)
  - W3: Abhaengigkeit von m/N, nicht von "prim" (60 %)
  - W4: 11 und 19 nicht stabiler als ihre Nachbarn (70 %)
  - W5: oszillatorische Instabilitaeten (55 %)
- Codex weiter still, seit 10:03 CEST. Scout 12:05Z ohne neue einschlaegige Treffer.
- Aktive Agenten: HUELLEN-LEITER, VORTEX-RAD.

### Ernte HUELLEN-LEITER (Agent fertig ~14:47; RUNDE-18/huellen-leiter/ERGEBNIS.md; ausgewertet 2026-10-02 14:47:47 CEST)

Plan eingefroren 14:00:12, nach der Karte (13:40:13). Vier Nachtraege nach Laufbeginn, alle eingefroren:
Nullstellensuche, zweimal Ablauf, Wertungsgrenze.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| L1 | alle 15 bekannten wiedergefunden | **eingetroffen** (Lage <= 8e-9, gleicher Umlauf); dazu eine 16. Stelle im alten Fenster (omega^2 = 0,82709, k = 2), die Runde 17 nicht gesehen hatte |
| L2 | >= 10 neue unter 0,819 | **eingetroffen**: 72 neue |
| L3 | dichter zur Schranke | **eingetroffen**: Abstaende in omega^2 von 0,18 auf 0,0026 |
| L4 | Abstand in R je Kurve etwa konstant (< 25 %) | **eingetroffen**: Mittel 2,17 bis 2,46, Streuung 1,5 bis 6 % |
| L5 | fuenfte oder weitere chi-Kurve | **eingetroffen**: 10 Kurven (k = 0 bis 9) |

- **Gesamt:** 88 stille Stellen von omega^2 = 1,40 bis 0,7635 (Huellenradius R = 1,8 bis 39).
  - Beide Gitterstufen stimmen ueberein (<= 7e-9).
  - Der Umlauf wechselt entlang jeder Kurve von Stelle zu Stelle das Vorzeichen.
  - Etwa alle 3,9 in R kommt eine neue Kurve hinzu; die Zahl der Stellen waechst etwa wie R^2.
- **Mechanismus** (Schreibtisch des Agenten, [H]): Der Abstand ist etwa pi/k_innen, also 2,37 gegen gemessen 2,41
  (k = 0) und 2,07 gegen 2,11 (k = 1). Die Kopplung an den offenen Kanal dreht jedes Mal das Vorzeichen, wenn die
  Innenwelle eine halbe Wellenlaenge mehr Platz hat.
- **Grenze:**
  - Ab R ~ 40 ist die Kenngroesse rundungsbestimmt: chi < 1e-16 im Inneren treibt die b-Komponente.
  - Gewertet ist darum nur bis R = 39; der Kartenbereich bis 0,74 ist nicht erreicht.
  - Vorschlag des Agenten: Die Kopplung fuer chi < 1e-12 nullsetzen.
- **Messgroesse:** W = m_ac + i m_bc wie Code 1, gezaehlt mit Zellen-Umlauf. Das ist im Plan begruendet und an 21
  Pruefstellen gegen den Rechteck-Umlauf gleich.
- Selbstanzeigen des Agenten:
  - ein lokales awk ohne Wirkung
  - ein falscher Startbefehl legte drei Dateien in ~/logs auf der .69 an; genau diese drei geloescht
  - zwei nicht freigegebene hilfs/-Dateien aus Runde 17 gelesen
  - keine Prozesse beendet
- **Bedeutung (vorab festgelegt):** Die Huelle traegt eine eigene Leiter stiller Stellen mit vielen Sprossen, die zur
  duennen Wand hin dichter werden [H, im Modell gestuetzt].
  - Im Einfeld-Modell war es eine Leiter (blind bis n = 15).
  - Mit Huelle sind es viele Leitern, eine je Schwingungsart der Huelle (k = 0 bis 9 bis R = 39), mit festen Sprossen
    im Radius.
- **Abschaetzung: weiter.**
  - Bereich R > 40 mit stabilisierter Kopplung (Vorschlag oben).
  - Schreibtischformel fuer den Abstand je k herleiten, als Vorhersage fuer eine blinde Pruefung.
  - l = 1 (Dipol) im Zweifeldmodell.

### Ernte VORTEX-RAD (Agent fertig 15:12 laut Agent; RUNDE-18/vortex-rad/ERGEBNIS.md; ausgewertet 2026-10-02 15:12:55 CEST)

Plan eingefroren 14:34:03, nach der Karte (14:12:39).

| Nr | Vorhersage | Ausgang |
|---|---|---|
| W1 | Schreibtischformel auf 1e-10, Nabe null | **formal nicht eingetroffen** (65 von 25 560 Punkten nicht konvergiert, alle bei omega^2 0,988 bis 1, Startpfad mit Amplitude ~ 0). Inhaltlich erfuellt: Formel auf 4,6e-12 und Nabe < 5,1e-12 an allen 25 495 konvergierten Punkten |
| W2 | grosser Ast, m = 1 bei kleinem J fuer viele N stabil | **nicht eingetroffen**: nur N = 5 bis 12 bei J = 0,02 (8 von 21), bei groesserem J weniger. Ursache nach Agent (post hoc, abgeschaetzt): Die Nabe koppelt an eine Phasenwelle des Rings und entzieht ihr Energie; Zerfall schaukelnd (Zeitentwicklung 0,0457 gegen Linearisierung 0,0458) |
| W3 | Stabilitaet haengt von m/N ab, nicht von "prim" | **formal nicht eingetroffen**: Die Primzahl-Haelfte haelt (Fehlerquote 7,2 % gegen 6,3 %); die m/N-Haelfte verfehlt die 90 % knapp (89 % bzw. 83 % auf dem grossen Ast), weil die Nabe mit N J mitspielt |
| W4 | 11 und 19 nicht stabiler als ihre Nachbarn | **eingetroffen** (Unterschied hoechstens 0,094, Grenze 0,10) |
| W5 | Instabilitaeten oszillatorisch | **eingetroffen**: 72,6 % oszillatorisch. Die Zaehlung der instabilen Moden gegen die Moden negativer Energie stimmt (ausser bei m/N = 1/4); Kollision direkt verfolgt an 167 Punkten |

- Stabil sind vor allem: kleiner Ast mit m/N > 1/4 (6540 von 6792 Punkten bei allen J).
- Teiler wirken nur an zwei Stellen:
  - Bei N durch 4 teilbar und m = N/4 gibt es eine exakte Loesungsfamilie mit unsicherer Einstufung.
  - Exakt symmetrische Teilring-Wirbel gibt es nur fuer Teiler von N. Fast symmetrische Dreierwirbel gibt es auch fuer 11
    und 19, und sie sind gleich oft stabil.
- V5-Kontrolle bestanden: Nabenschwellen N_max = 20, 15, 11, 9, 7 exakt; V5-Regel 3623 von 3623.
- **Bedeutung (vorab festgelegt; W2 und W5 nicht beide eingetroffen):**
  - Drehende Feldklumpen mit ganzzahligem Drehimpuls gibt es auf dem Rad stabil, aber auf dem leichten Ast bei grosser
    Ladung, nicht beim einfachsten Wirbel auf dem schweren Ast.
  - Primzahlen (11, 19) spielen keine Rolle; Teiler nur in Sonderfaellen.
- **Abschaetzung: parken.** Ein Bezug zum drehenden Q-Ball im Kontinuum (l > 0, Drehimpuls) waere eine eigene Karte.
  11 und 19 sind auch hier nicht besonders.

## Abschaetzung Runde 18 (Leitung, 2026-10-02 15:13:20 CEST)

| Karte | Ergebnis kurz | Abschaetzung |
|---|---|---|
| HUELLEN-UHR | Zeitbereich, dritter Code: BIC-Mode strahlt 3,7e-5 bzw. 5,3e-5 ab (eps^4), Kontrolle 2300- bis 35 000-mal mehr; Ticks mit 2 pi/rho auf 5e-6 | erledigt (alle 5 Vorhersagen eingetroffen) |
| HUELLEN-LEITER | 88 stille Stellen auf 10 chi-Kurven bis R = 39, Sprossen in R fast aequidistant (~2,2 bis 2,5), Zahl ~ R^2 | weiter: R > 40 stabilisieren, Abstandsformel blind pruefen, l = 1 |
| VORTEX-RAD | stabile Wirbel auf dem leichten Ast (m/N > 1/4); m = 1 auf dem schweren Ast nur bei kleinen Raedern; Primzahlen ohne Rolle | parken |
| Lektuere verzweigte Gitter | Wirbel auf Sterngraph [S, Abstract] | erledigt (in VORTEX-RAD aufgegangen) |
| M_E-G3 (Codex) | offen, Codex seit 10:03 still | in Runde 19 uebernommen |

**Lehren der Runde:**
- (1) Ein vorab gewerteter Zeitbereichstest (HUELLEN-UHR) ist die staerkste Pruefung eines Frequenzbereichsbefunds: Er
  traf 5 von 5 und hob die Huellen-Stellen ueber "post hoc".
- (2) Rundungsgrenzen begrenzen Leiterzaehlungen (chi < 1e-16). Grenzen der Wertung vorab festlegen, nicht erst
  nachtraeglich.
- (3) Schreibtischformeln, die einen Teil des Systems vergessen (die Nabe in VORTEX-RAD), fuehren zu falschen
  Stabilitaetsvorhersagen. Jede Vorab-Formel braucht eine Pruefung "welche Freiheitsgrade fehlen?".

## Einfach gesagt (Runde 18)

Der Q-Ball mit Huelle kann sehr viele stille Schwingungen haben, 88 bisher gefunden, geordnet wie die Sprossen mehrerer
Leitern. Ein drittes, ganz anders gebautes Programm hat zwei davon wirklich ablaufen lassen. Sie verlieren fast keine
Energie und ticken wie eine Uhr. Drehende Feldklumpen auf einem Rad-Netz halten nur in bestimmten Faellen, und die
Primzahlen 11 und 19 sind dabei nichts Besonderes.

## Rundenabschluss (Leitung, 2026-10-02 15:13:31 CEST)

- Journal: claude-runde-v3-18-20261002, Index nr 555; pruefen ohne Befund; Quellen-Hashes in RUNDE-18/journal-quellen.txt.
- Sicherung .69 -> TS440 gestartet (Log /home/fmh/sicherung-dot69-ts440-lauf-20261002-r18.log); r17 endete mit rc = 0.
- In Runde 19 uebernommen:
  - M_E-G3 (Codex)
  - Huellen-Leiter: Bereich R > 40 stabilisieren, Abstandsformel vorab, l = 1
  - Dimensionsmesser auf einem wachsenden Graphen
