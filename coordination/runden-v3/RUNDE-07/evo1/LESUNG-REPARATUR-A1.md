# Lesung der Reparatur nach A1 (EVO-1, Runde 7): frischer Leser

- **Auftrag:** Leitung (claude-primary), Pruefung des Entwurfs in PLAN.md, Abschnitt 12 (Option (i), Boden 1e-8), vor
  seiner Wirkung. Nur Anforderungen und Befunde; kein Umformulieren, keine Aenderung an PLAN.md oder evo1.py, keine
  Rechnung, .69 nur lesend (cat, jq, ls, grep, diff).
- **Leser:** frischer Agent, Modell Fable, ohne Vorkontext zu EVO-1.
- **Beginn (date):** 2026-09-30 05:41:39 CEST. **Ende (date, vor dem Schreiben gemessen):** 2026-09-30 05:51:42 CEST.
- **Empfehlung: FREIGEBEN MIT AUFLAGEN** (Antwort 5).

## Antwort 1: Liegt die Reparatur in der Ausnahme (Abschnitt 3, Zeile 62)? Genau eine Aenderung?

- **Zeitfenster und Form: ja.** Zeile 62: "Ausnahme ist nur eine Reparatur nach A1 vor Generation 1; sie wird hier mit
  Grund und date eingetragen." A1 wurde 03:36:17 UTC (05:36:17 CEST) ausgewertet und nicht bestanden (LAUF-Z0.log).
  Generation 1 ist nicht gestartet: auf der .69 liegen nur gen-000.json, bew-000.jsonl und die zwei Ergebnisordner von
  Generation 0. Abschnitt 12 traegt Grund und date (05:40:41 CEST).
- **Sachlich: ja, mit einer Lesart.** Zeile 59 bis 63 spricht von "Zahlen" (Schwellen). Die Reparatur ist eine neue
  Regel (Nachbarfilter in grob_minima) plus eine neue Konstante (G_BODEN). Dass eine Regel repariert werden darf, folgt
  aus A3 ("Zuerst wird das Messmittel repariert"), aus Zeile 120 f. ("Messmittelfehler ... die Reparatur wird hier
  eingetragen") und aus dem Gauntlet-Plan A1 ("Sonst ist der Code fehlerhaft"). Ich lese die Ausnahme so, dass sie den
  Entwurf deckt. Zeile 62 sagt "hier", also Abschnitt 3: Der Filter muss dort bei der Grobregel eingetragen werden, nicht
  nur in Abschnitt 12 (Auflage A6).
- **Genau eine Aenderung: ja**, gezaehlt nach Regeln und Schwellen. Der Diff Version 1 gegen 2 auf der .69 (evo1_v1.py
  gegen evo1.py) zeigt nur: x_schaetz faengt den Nenner null ab, der Hinweis wird durchgereicht, Rauchtest-Teil 0,
  Kopfkommentar. Keine Schwelle, keine Entscheidungsregel. Version 3 ist damit die eine Reparatur: Filter, Konstante und
  Grundtext sind eine Regel. Option (ii) kommt nicht dazu. Danach ist das Kontingent verbraucht; eine zweite Regelaenderung
  vor oder waehrend Generation 1 bis 3 ist nicht mehr gedeckt.

## Antwort 2: Nachtraeglichkeit, Datenpruefung, Option (ii)

**Zeitleiste** (Dateizeiten der .69 in UTC, plus 2 h = CEST; lokale Dateien in CEST):

| Zeit CEST | Ereignis | Quelle |
|---|---|---|
| 05:00:54 | Kontrolle startet mit Version 1 | LAUF-G0B.log |
| 05:07:15 | Absturz in x_schaetz; Grob (12 Punkte) liegt in zustand.json | LAUF-G0B.log, lauf-69-Kopie: grob 12, fein leer |
| 05:09:07 bis 05:14:06 | Abschnitt 11 geschrieben, darin Option (i) mit Bereich 1e-8 bis 5e-8 und Option (ii) | PLAN.md Fusszeile; Sicherung PLAN.md.bak-20260930-0540 (mtime 05:14:11) |
| 05:15:14 | Version 2 auf der .69 | mtime evo1.py, sha256 d81870bf beidseitig gleich |
| 05:15:47 bis 05:28:42 | Kontrolle fein (A, B, C, Kontur), Ende 05:28:43 | LAUF-G0B2.log, zustand.json aufrufe |
| 05:35:32 | Anker fertig, qualifiziert | LAUF-G0A.log |
| 05:36:17 | zusammenfassen: A1 NICHT bestanden | LAUF-Z0.log |
| 05:40:41 | Abschnitt 12, Entwurf | PLAN.md (mtime 05:41:04) |

- Diff .69-Fassung (05:00) gegen Sicherung 0540: nur Abschnitt 11, die sha-Zeile in Abschnitt 7 und die Fusszeile.
  Diff Sicherung 0540 gegen jetzt: nur Abschnitt 12. Abschnitte 3 und 11 sind seit dem Ausgang unveraendert.
- Also: Option (i) samt Bereich stand fest, als die Grobwerte der Kontrolle (beide Nachbarn des Scheinminimums) bekannt
  waren, die Feinwerte und der Ausgang (b, d) aber nicht. Abschnitt 11, Punkt 2 sagte den Ausgang ("kippt b, dann nicht
  entscheidbar") vorher. Der Zahlenwert 1e-8 wurde nach dem Ausgang gewaehlt.

**Datenpruefung an den Stufe-A-Breiten der Spur** (zustand.json, grob.Gamma; Minimum nach lokale_minima:
werte[i] < werte[i-1] und werte[i] <= werte[i+1]):

- **Kontrolle dim 1**, Spur 12 Punkte, alle pol_ok: 4,43e-3; 4,50e-3; 1,90e-3; 6,62e-4; 2,01e-4; 5,28e-5; 1,14e-5;
  1,89e-6; 2,06e-7; 1,039e-8; -9,86e-10; -8,51e-10. Einziges inneres Minimum: k = 10 (0,89273), Nachbarn k = 9 mit
  1,0392e-8 und k = 11 mit -8,506e-10.
  - Regel "beide Nachbarn > Boden": Der rechte Nachbar ist negativ. Fuer jeden Boden ueber -8,5e-10 faellt das Minimum
    weg, also fuer jeden Wert in 1e-8 bis 5e-8 gleich. Ergebnis mit Version 3: grob_minima leer, F2 = nein, Urteil "nicht
    qualifiziert"; die A1-Abfrage in zusammenfassen (ko.F2 == "nein") ist erfuellt.
  - Randnotiz: Der linke Nachbar 1,0392e-8 liegt selbst im vorab genannten Bereich, 4 % ueber 1e-8. Bei Boden <= 1,039e-8
    besteht er, darueber nicht. Das aendert nichts, weil der rechte Nachbar entscheidet. Die Robustheit haengt am
    Wortlaut "beide Nachbarn", also Wegfall, sobald ein Nachbar den Boden verfehlt. Der Wortlaut darf nicht zu "ein
    Nachbar genuegt" oder "der Wert selbst" werden.
- **Anker dim 3**, Spur 12 Punkte, alle pol_ok: 9,10e-3; 4,93e-3; 4,57e-3; 4,81e-6; 2,48e-3; 2,53e-3; 3,75e-3; 3,61e-4;
  3,29e-4; 1,05e-3; 6,34e-4; 9,20e-5. Zwei innere Minima: k = 3 (0,63182; Nachbarn 4,57e-3 und 2,48e-3) und k = 8
  (0,81818; Nachbarn 3,61e-4 und 1,05e-3). Kleinster Nachbar 3,61e-4, das 7200-Fache von 5e-8. Fuer jeden Boden bis
  3,6e-4 bleiben beide Minima; die Bewertung ist bitgleich zu Version 2 zu erwarten (F2 = ja bei k = 8, omega*^2 =
  0,79755; Gamma(0,798) Stufe C 1,1224e-7, im Faktor 2 um 1,12e-7).
- **Fazit:** Kein Wert in 1e-8 bis 5e-8 aendert den Ausgang von Anker oder Kontrolle. Das gilt sogar fuer jeden Boden
  zwischen -8,5e-10 und 3,6e-4. Die nachtraegliche Wahl der Zahl konnte den Ausgang von Generation 0 nicht steuern. Zu
  Generation 1 gibt es keine Ergebnisse, also auch dort keine Steuerung nach Befund.

**Option (ii)** (Boden auf die sechs Stufe-B-Feinwerte, nach der Verfeinerung):

- Kontrolle: B-Werte 2,17e-9; 2,29e-10; 1,82e-10; 1,55e-10; 1,20e-10; -2,26e-11, alle unter 1e-8 und unter 5e-8:
  "nein (unaufgeloest)", A1 ebenfalls bestanden, fuer jeden Boden im Bereich.
- Anker: k = 8 B-Werte 1,0e-7 bis 4,1e-4, k = 3 1,28e-7 bis 6,5e-3: nicht betroffen.
- Beide Optionen geben in Generation 0 denselben Ausgang. Unterschiede: (ii) rechnet Scheinminima weiter durch (Kontrolle
  gemessen: 455 s + 317 s = 12,9 min nur fuer fein), laesst Scheinminima weiter die drei Verfeinerungsplaetze (MAX_MIN)
  besetzen, urteilt aber auf der genaueren Stufe B, und die Feinwerte stehen im Bericht. (i) spart die Kosten und gibt die
  Plaetze frei (Antwort 3, N7), urteilt auf Stufe A (Abweichung 1D etwa 1,2e-9, 3D 4,8e-9), und der Bericht muss die
  weggefallenen Minima eigens ausweisen (Auflage A1). (i) ist vertretbar; (ii) waere die vorsichtigere, teurere Wahl.
  Beide zusammen sind durch "eine Aenderung" ausgeschlossen.
- Vermerk zur alten Regel an der Kontrolle: Von e bis h scheiterte nur e (Tiefpunkt aussen, Index 5). f bestand mit
  R^2 = 0,9993 (vier glatte, monoton fallende Werte um 1e-10), g bestand, h bestand leer (Gamma_ref = -2,26e-11, also
  Vergleich gegen eine negative Schwelle). Ohne b und d haette die Kontrolle nur an e gehangen. Das stuetzt den
  Aufloesungsboden in der Grobregel. Die Leere von h bei Gamma_ref <= 0 (Abschnitt 11, Punkt 4) bleibt bestehen; sie ist
  nicht Teil der Reparatur, ich vermerke sie nur.

## Antwort 3: Nebenwirkungen, Vollstaendigkeit

Nr. 1 bis 6 des Entwurfs sind geprueft und in der Sache richtig (Zahlen: Antwort 4). Fehlend oder ungenau:

- **N7 (fehlt; widerspricht Nr. 3): Verfeinerungsplaetze.** grob_minima sortiert nach Gamma und nimmt hoechstens
  MAX_MIN = 3. Scheinminima (Gamma nahe 0 oder negativ) stehen immer vorn und verdraengen echte Minima. Mit dem Filter
  ruecken echte Minima nach. Ein Modell mit vier oder mehr groben Minima kann so F2 = ja bekommen, wo die alte Regel
  "nein" oder "nicht entscheidbar" gab. Die Zaehlung "neu und verschieden" ist also betroffen, in Richtung mehr
  F2 = ja. Der Grund ist richtig (ein echtes Minimum wird endlich geprueft), aber gegenueber der alten Regel ist es eine
  Lockerung und gehoert in die Liste. Ein Modell mit Rauschwerten am oberen Scanende kann leicht zwei bis drei
  Scheinminima haben.
- **N8 (fehlt): Arm R.** Die Umschlagregel vergleicht die Etiketten (F2, F3) an den Zellecken; "nicht entscheidbar" gegen
  "nein" zaehlt als Umschlag. Mit der Reparatur werden solche Ecken "nein", es gibt weniger Scheinumschlaege, und die
  Kandidatenliste von R aendert sich. Arm E: fitness() gibt fuer "nicht entscheidbar" und fuer "nein" dasselbe Tupel
  (F0 und F1 ja, F2 nicht ja, g0_rel fehlt); die Elternwahl aendert sich nicht. Arm Z: unabhaengig. Die Reparatur
  bevorzugt keinen Arm ueber die Fitness, aendert aber, welche Zellen R erkundet. Das ist vor Generation 2 festzuhalten.
- **N9 (fehlt, Ergebnis: unbetroffen): A2.** lebensfaehig heisst F0 = ja; "nicht entscheidbar"-Modelle haben F0 = ja und
  sind nicht qualifiziert, stehen also schon im Nenner. Der Etikettwechsel aendert Zaehler und Nenner nicht, ausser ueber
  N7. Das sollte ausdruecklich dastehen.
- **N10 (Anlass unvollstaendig): A3 bleibt fuer "Umlauf ungleich 1 an einem aufgeloesten Minimum" scharf.** Der Anker
  selbst hat so ein Minimum: k = 3 bei 0,63182, Feinwerte 1,28e-7 bis 6,5e-3, e bis h alle bestanden (R^2 0,99990,
  x* 0,6304), Umlauf 2 -> "nicht entscheidbar" auf Minimumsebene. Das Modell ist nur ueber k = 8 "ja". Modelle nahe dem
  Anker koennen dieselbe Signatur ohne zweites Minimum zeigen und A3 ausloesen; die Reparatur aendert daran nichts.
  Abschnitt 12 nennt dieses zweite Minimum nicht.
- **N11: F3 unbetroffen.** W kommt aus dQ/domega^2 und E/Q der Grobpunkte; F3 wird nur bei F2 = ja gebildet.
- **N12: Duennwand-Grenze und oberes Scanende.** Am oberen Ende (k = 10) greift der Filter genau dort, wo die Kontrolle
  lag. Eine echte Nullstelle zwischen den letzten zwei Scanpunkten oder ueber 0,93 wurde schon vorher nicht gefunden
  (Abschnitt 11, Punkt 5): unveraendert. Am Duennwand-Ende (k = 1) sind die Breiten gross (Anker 9e-3, Kontrolle 4,4e-3);
  der Boden greift dort nicht, Pruefung a bleibt die Huerde: unveraendert. Neu gegenueber Nr. 1: Bei asymmetrischen
  V-Formen genuegt ein flacher Ast mit C_Ast < 7e-6 fuer den Wegfall; Nr. 1 rechnet nur symmetrisch. Praktisch fern
  (Steigungen 0,77 bis 1,18 geben C um 0,6 bis 1,4; der k-3-Fit gibt 15,3). Unveraendert bleibt auch, dass die Spur
  Punkte mit Im rho > 0 bis 1e-3 als pol_ok fuehrt; der Filter faengt davon nur den Rauschbereich.
- **N13 (fehlt): Bericht.** Abschnitt 3 verspricht bei mehreren Minima "alle werden berichtet". Ein stiller Filter in
  grob_minima laesst die weggefallenen Minima aus modell.json verschwinden. Damit verliert auch die Rasterkarte (A2-Fall)
  und die A3-Beobachtung die Information "hier lag ein unaufgeloestes Minimum".
- **N14 (fehlt, Umsetzung): zusammenfassen liest modell.json.** lade() oeffnet ergebnisse/KEY/modell.json (evo1.py,
  Zeilen 702 f.); modell.json schreibt nur Lauf.rechne() im Befehl modell. "Danach auf der .69 zusammenfassen --gen 0
  erneut" allein aendert die A1-Zeile nicht. Noetig ist ein erneuter modell-Aufruf je Gen-0-Modell mit Version 3. Der
  rechnet nichts nach: bewerte gibt bei vollstaendigem zustand.json sofort "fertig" zurueck; es kommt nur ein
  aufrufe-Eintrag hinzu, und modell.json wird ueberschrieben.
- **N15: Der Version-2-Zweig "Nullnenner" wird unerreichbar**, weil beide Nachbarn > 1e-8 > 0 sind. Harmlos; im
  Kopfkommentar vermerken.
- **N16: Etikettwechsel bei F1 = nein.** bewerte prueft grob_minima vor dem F1-Filter. Ein Modell mit F1 = nein und nur
  einem Scheinminimum heisst kuenftig "nein" statt "grob Minimum, nicht verfeinert". Betrifft die R-Etiketten (N8).
- **N17 (Zahl zu klein): Kosten.** "etwa 7 min" je Scheinminimum; gemessen an der Kontrolle auf der .69: 455 s + 317 s
  = 12,9 min allein fuer fein (Grob war vor dem Absturz fertig; zeiten: B 55 s, C 117 s, Kontur 95 s je Punkt).

## Antwort 4: Anlass gegen die Dateien, in beide Richtungen

**Vom Text zur Datei** (Abschnitt 12):

| Textstelle | Datei | Befund |
|---|---|---|
| zusammenfassen 03:36:17 UTC | LAUF-Z0.log ende 03:36:17, bew-000.jsonl mtime 03:36:17 | stimmt |
| Anker F2 = ja, omega*^2 = 0,79755 | modell.json d3: x_stern 0,7975542 | stimmt |
| Gamma(0,798) = 1,12e-7 | zusatz 0.798: C 1,1224e-7 (B 1,1209e-7) | stimmt |
| Kontrolle "nicht entscheidbar" am groben Minimum 0,8927 | modell.json d1: grob_minima [0,892727] | stimmt |
| Gruende b und d (Umlauf -7, nicht aufgeloest) | grund: "b) Reihenfolge A/B False, c) B-C True, d) Umlauf -7 aufgeloest False" | stimmt |
| Stufe-B-Feinwerte zwischen -2e-11 und 2,2e-9 | Gamma_B: -2,26e-11 bis 2,168e-9 | stimmt |
| A1 nicht bestanden, Gen 1 nicht gestartet | LAUF-Z0.log "NICHT bestanden"; kein gen-001.json, 2 Ergebnisordner | stimmt |
| Abschnitt 11 um 05:11 vor Ende der Kontrolle 05:28:43 | Fusszeile 05:09:07 bis 05:14:06; LAUF-G0B2.log ende 03:28:43 UTC | stimmt |
| rechter Nachbar der Kontrolle -8,5e-10 | grob k = 11: -8,506e-10 | stimmt |
| "die Nachbarn des Ankers bei etwa 3e-4" | k = 7: 3,61e-4; k = 9: 1,05e-3; beim zweiten Minimum 4,57e-3 und 2,48e-3 | ungenau, Richtung harmlos |
| "etwa 5 Groessenordnungen ueber dem Boden" | 3,61e-4 / 1e-8 = 3,6e4 (4,6 Stellen), 1,05e-3 / 1e-8 (5,0 Stellen) | stimmt in etwa |
| Stufe-A-Abweichung 4,8e-9 | ERGEBNISSE-R6-B.md, Zeilen 146 f.: A - C 4,8e-9 bei 0,797 und 0,798 | stimmt |
| Abstand 0,037, C < 7e-6 | (0,93 - 0,52)/11 = 0,03727; 1e-8 / 0,037^2 = 7,3e-6 | stimmt |
| "Die bekannten Nullstellen haben C = 1,08 bis 36" | keine Quelle gefunden; .69-Fits: c = 0,93 (k = 8), 15,3 (k = 3); 1,08 = 1,04^2 aus der synthetischen Kurve | Quelle fehlt, Anker-Fit 0,93 liegt unter 1,08; fuer den Schluss ohne Belang |
| "etwa 7 min" je Scheinminimum | 455 s + 317 s = 12,9 min | Zahl zu klein |
| Regelgrundlage Zeile 62 | PLAN.md Zeile 62 | stimmt |
| sha256 Version 2 d81870bf, resonanz3d 99c54b9c | beidseitig gleich (lokal und .69) | stimmt |

**Von der Datei zum Text** (steht in den Dateien, fehlt im Text):

- Zweites grobes Minimum des Ankers bei 0,63182 mit bestandenen e bis h und Umlauf 2 (N10).
- Linker Nachbar des Kontroll-Minimums 1,0392e-8 liegt im vorab genannten Bereich (Antwort 2).
- Die Kontrolle scheiterte an e bis h nur an e; f, g, h bestanden (Antwort 2).
- Auf der .69 liegt PLAN.md in der Fassung von 05:00 (sha256 314b2e4a, ohne Abschnitte 11 und 12); zu spiegeln.
- Gemessene Kosten je Aufruf (zeiten) sind hoeher als die Laptop-Schaetzung: Kontrolle B 55 s, C 117 s, Kontur 95 s;
  Anker B 40 s, C 83 s, Kontur 48 s.

## Antwort 5: Empfehlung

**FREIGEBEN MIT AUFLAGEN.** Gruende: Die Regel war vor dem Ausgang der Kontrolle benannt, samt Bereich und Vorhersage
fuer beide Modelle; der Ausgang ist ueber den ganzen Bereich und weit darueber hinaus unveraenderlich; die Reparatur
verschaerft die Grobregel (weniger Minima gelangen in die Verfeinerung) und lockert F2 = ja nur ueber die
Verfeinerungsplaetze (N7); der Anker bleibt bitgleich; das 1D-Verhalten (monotoner Abfall bis etwa 1e-10 auf Stufe B, keine
V-Form) ist genau das, was die Kontrolle zeigen sollte. Die Lockerung von A3 ist die von A3 selbst vorgesehene
Reparatur; sie darf aber nicht still bleiben (A1).

**Auflagen (pruefbar), vor der Wirkung:**

- **A1 Bericht der weggefallenen Minima.** modell.json fuehrt jedes innere grobe Minimum der Spur auf; weggefallene mit
  Etikett "unter Aufloesung", Grobwert und beiden Stufe-A-Nachbarwerten (eigenes Feld, etwa
  grob_minima_unter_aufloesung). zusammenfassen gibt je Generation neben der A3-Quote die Zahl der Modelle mit solchen
  Minima aus. Pruefung: Die Version-3-modell.json der Kontrolle enthaelt 0,89273 mit 1,039e-8 und -8,51e-10.
- **A2 Neubewertung ueber modell, nicht nur ueber zusammenfassen.** Beide Gen-0-Befehle aus Abschnitt 7 mit Version 3
  erneut aufrufen (Anker mit --zusatz 0.798), danach zusammenfassen --gen 0. Pruefung: jeder Aufruf unter 30 s;
  grob, fein, zusatz und zeiten in zustand.json unveraendert (jq-Auszug vorher und nachher gleich); aufrufe um genau einen
  Eintrag laenger.
- **A3 Anker bitgleich.** modell.json des Ankers nach Version 3 ist gleich der Version-2-Datei (diff leer oder sha256
  gleich). Bei Abweichung: nicht freigegeben, zurueck zur Lesung.
- **A4 Sicherung vor dem Ueberschreiben.** Version-2-Fassungen von modell.json (beide Modelle), bew-000.jsonl und
  LAUF-Z0.log in einen Unterordner (etwa v2-bewertung/) auf der .69 kopieren und lokal spiegeln. Die neue Zusammenfassung
  in eine neue Logdatei (etwa LAUF-Z0-v3.log), nicht ueber die alte.
- **A5 Abschnitt 12 ergaenzen und berichtigen.** N7, N8, N9, N13, N16 nachtragen; Nr. 3 berichtigen ("betroffen ueber
  die Verfeinerungsplaetze"); Nachbarn des Ankers als 3,61e-4 und 1,05e-3 (k = 8) sowie 4,57e-3 und 2,48e-3 (k = 3)
  angeben; Kosten 12,9 min gemessen; C-Spanne mit Quelle oder durch die .69-Fits 0,93 und 15,3 ersetzen; das zweite
  Anker-Minimum (0,63182, Umlauf 2) im Anlass nennen.
- **A6 Buchung.** Filter und Boden in Abschnitt 3 bei der Grobregel eintragen mit Verweis auf Abschnitt 12; Wirkung mit
  date; sha256 von Version 3 in Abschnitt 7 und 12, beidseitig verglichen; PLAN.md auf die .69 spiegeln; Vermerk, dass
  das Reparaturkontingent verbraucht ist.
- **A7 Rauchtest Version 3** wie in Abschnitt 12 angekuendigt, dazu zwei Faelle: (a) synthetische Spur mit mindestens
  vier groben Minima, davon zwei Scheinminima (Nachbarn unter dem Boden): Version 3 verfeinert die echten; (b) das Muster
  der Kontrolle (ein Nachbar 1,04e-8, einer negativ): Wegfall. Ergebnisse in rauch/v3/.
- **A8 Generation 1 vollstaendig mit Version 3**, ohne weitere Regelaenderung; vor Generation 2 die R-Wirkung (N8) als
  gewollt vermerken.

## Geprueft (Stellen)

- Lokal: PLAN.md ganz (Abschnitte 3, 4, 5, 11, 12; Zeile 62; A1 bis A3); PLAN.md.bak-20260930-0540; evo1.py ganz,
  besonders spur, grob_minima, x_schaetz, fein, f2_auswertung, bewerte_min, bewerte, lade, kommando_zusammenfassen,
  kommando_generation (Arme E, R, Z, fitness); resonanz3d.py lokale_minima; rauch/rauch_bericht.txt,
  rauch/v2/rauch_bericht.txt; lauf-69/ergebnisse/P_b0.5000_g0.0000_d1/zustand.json (grob 12, fein leer);
  ../GAUNTLET-NEUSTART-PLAN.md Abschnitte 4, 5, 7, Freigabe; ../../README.md; RUNDE-06/ERGEBNISSE-R6-B.md Zeilen 143 bis
  154; sha256 evo1.py, resonanz3d.py, PLAN.md (drei Fassungen); Diffs der drei PLAN-Fassungen.
- .69 (nur lesend): runde7-evo1/ergebnisse/P_b0.5000_g0.0000_d1/{modell.json, zustand.json},
  .../P_b0.5000_g0.0000_d3/{modell.json, zustand.json}, LAUF-Z0.log, LAUF-G0A.log, LAUF-G0B.log, LAUF-G0B2.log,
  gen-000.json, bew-000.jsonl, gen0-kette.sh, gen0-kontrolle.sh, PLAN.md, sha256 und Diff evo1_v1.py gegen evo1.py,
  Verzeichniszeiten mit ls --time-style=full-iso, kleintests/kleintest.sh (Kopf).
- Nicht geprueft: die Runde-6-1D-Werte, gegen die Abschnitt 11 die Stufe-A-Abweichung in 1D schaetzt (nicht in
  RUNDE-06.md gefunden; fuer Abschnitt 12 ohne Belang); die Quelle von "C = 1,08 bis 36".

## Einfach gesagt

Das Programm sucht in jeder Modellkurve nach einer Delle, an der die Atmung fast keine Energie verliert. In der
1D-Gegenprobe gibt es keine echte Delle, nur ein winziges Zittern ganz am Ende, das unter der Messgenauigkeit liegt.
Die alte Regel hielt das Zittern fuer eine Delle und kam dann zu "kann ich nicht entscheiden" statt zu "nein". Die
Reparatur sagt: Eine Delle zaehlt nur, wenn ihre Nachbarn deutlich ueber dem Rauschen liegen. Ich habe nachgerechnet,
dass diese Regel bei jedem sinnvollen Schwellenwert dasselbe ergibt und das echte Vorbild nicht anruehrt; sie darf
gelten, wenn die weggefallenen Dellen weiter im Bericht stehen und die Neubewertung sauber gebucht wird.

---

## Nachtrag 1: Entscheidung zu Auflage A3 (Anker bitgleich)

- **Anlass:** UMSETZUNG-V3.md, Abschnitt 4, A3: Die modell.json des Ankers nach Version 3 (a9cef0d2...) weicht von der
  Version-2-Datei (a60c461d...) ab; die Lesung sagte "Bei Abweichung: nicht freigegeben, zurueck zur Lesung".
- **Leser:** derselbe frische Leser (Fable). Nur gelesen: lokal cat, jq, diff, sha256sum; auf der .69 cat, ls,
  sha256sum, grep. Keine Rechnung, keine Aenderung an PLAN.md oder evo1.py.
- **Beginn (date):** 2026-09-30 06:15:48 CEST. **Ende (date, vor dem Schreiben gemessen):** 2026-09-30 06:21:07 CEST.
- **Entscheidung: FREIGEBEN. A3 gilt als erfuellt, mit der unten benannten Toleranz und Pruefung.**

### N1. Die Zahlen stimmen (selbst geprueft)

| Beleg | Umsetzer | Befund |
|---|---|---|
| 13 Anker-modell.json (Sicherung V2, Neubewertung V3, Vorpruefung V3, 10 Wiederholungen) | V3 6 von 7 gleich a60c461d, V2 4 von 5 | stimmt: 11 x a60c461d, 1 x e8981201 (wdh anker-v2-2, laut LAUF-wdh.log mit evo1_v2.py), 1 x a9cef0d2 (echte V3-Neubewertung); Hashes lokal und .69 gleich |
| Diff V2 -> V3: 4 Zeilen, nur c, g0, g0_rel bei k = 8 | ja | stimmt (Zeilen 196, 198, 200, 224); relativ c 7,3e-15, g0 1,94e-13, g0_rel 1,94e-13; x_stern, x_stern_lin, R2_lin, F2_teile, k = 3 unveraendert |
| Diff V2 -> abweichender V2-Lauf | dieselben 4 Zeilen, 8,5e-14 | stimmt (max. relativ 8,5e-14) |
| Rest byteweise gleich | | ja: nach `jq -S 'del(.minima[].c, .minima[].x_stern, .minima[].g0, .minima[].g0_rel, .x_stern, .g0_rel)'` haben V2 und V3 dieselbe Pruefsumme (57534516...) |
| Eingaben gleich | A2: zustand ohne aufrufe gleich | stimmt: alle Kopien (Sicherung, Neubewertung, Vorpruefung, 10 wdh) haben ohne aufrufe die Pruefsumme 24de9f18...; a2-pruefung vorher = nachher (d3 24de9f18, d1 e4178cfd); aufrufe 4 -> 5 bzw. 2 -> 3, neue Eintraege 0,008 s und 0,006 s |
| fit_parabel unveraendert | Diff im Anhang | stimmt: der Diff V2 -> V3 beruehrt nur grob_minima, die neue Methode, bewerte (Feld, Grund), zusammenfassen (eine Zeile), Rauchtest Teil 5, Kopfkommentar |
| Rauchtest V3 lokal | Teil 5 4 von 4 ok; Anker-Kopie V2 = V3 | stimmt: rauch/v3/rauch_bericht.txt, Teile 0 bis 3 zeilengleich zu v2 (nur Zeiten), Teil 5 viermal "ok"; kopie-anker-v2 und -v3 beide d497bb19 (diff leer) |
| LAUF-Z0-v3.log | A1 bestanden | stimmt: "Kontrolle dim 1 F2 = nein -> bestanden", nicht entscheidbar 0, "weggefallene grobe Minima: 1 von 2" |
| Kontrolle V3 | Feld mit 0,89273, 1,039e-8, -8,51e-10 | stimmt; die Kontrolle-modell.json ist zwischen Laptop (torch 2.10.0) und .69 (torch 2.5.1+cu121) byteweise gleich (8dba8208) |

### N2. Ursache: Rechenstreuung der .69, nicht Version 3

- Die Eingaben der Parabelanpassung (x, Gamma_B aus zustand.json) sind in allen 13 Laeufen bitgleich, der Code der
  Anpassung ist unveraendert, und Version 2 weicht in 1 von 5 Wiederholungen an denselben vier Zeilen von sich selbst
  ab. Damit ist die Streuung von Version 3 getrennt.
- Die Groesse passt: torch.linalg.lstsq streut in c um etwa 1e-14 relativ. g0 = cc - bb^2/(4c) ist bei k = 8 die
  Differenz zweier Zahlen um 5,5e-6 mit Ergebnis -7e-8 (Ausloeschung um den Faktor etwa 80), also 1e-14 x 80 = 1e-12
  als Obergrenze; beobachtet 8,5e-14 bis 1,9e-13. Alle Felder ohne lstsq (fit_linear, Entscheidungen) sind byteweise
  gleich, auch zwischen Laptop und .69.
- Umgebung der .69: torch 2.5.1+cu121 aus /home/fmh/ComfyUI/venv (per .pth eingebunden), Xeon E5-2630 v2, keine
  MKL- oder OMP-Variablen gesetzt. Ein alignment-abhaengiger Rechenweg der eingebauten MKL ist eine plausible
  Erklaerung; sie ist nicht geprueft und fuer die Entscheidung nicht noetig.
- Laptop (torch 2.10.0) gegen .69 (torch 2.5.1): relativ hoechstens 1,2e-13 (g0, k = 8), c 1,05e-14, x_stern 1,8e-16.

### N3. A3, neu gefasst (Anforderung, pruefbar)

- **A3 gilt als erfuellt, wenn beides gilt:**
  - (a) Nach Entfernen der sechs lstsq-Felder (minima[].c, minima[].x_stern, minima[].g0, minima[].g0_rel, x_stern,
    g0_rel) sind die `jq -S`-Ausgaben der Version-2- und der Version-3-Datei byteweise gleich (gleiche Pruefsumme).
  - (b) Jedes dieser Felder weicht relativ um hoechstens 1e-10 ab, gemessen als |a - b| / max(|a|, |b|), bei a = b
    null.
- **Ergebnis am 30.09.2026:** (a) gleich (57534516...); (b) hoechstens 1,94e-13. Beide erfuellt.
- **Warum 1e-10:** 500-mal ueber der gemessenen Streuung (1,9e-13 auf der .69, 1,2e-13 Laptop gegen .69) und um
  mehr als 1e6 unter jedem Entscheidungsabstand: g0_rel = -1,85e-4 liegt 1,2e-3 unter der Schwelle 1e-3, das ist
  relativ 6; x_stern hat 0,0206 Abstand zur W-Grenze. Eine Streuung von 1e-10 kann keine der Pruefungen e bis h und
  keine Lage aendern.
- **Abgelehnt:** Wiederholen bis der Hash passt (Kontrolle nach Befund); Rueckkopieren der Version-2-Datei (verdeckt
  die Streuung; der Stand auf der .69 bleibt a9cef0d2 mit der Sicherung in v2-bewertung/); ein deterministisches
  fit_parabel (weitere Codeaenderung ohne Nutzen fuer eine Entscheidung, wuerde A2 und A3 erneut noetig machen).
- **Buchung (Leitung, zu A5 und A6):** Abschnitt 12 traegt A3 mit dieser Fassung, der Toleranz, den Pruefsummen und
  den Wiederholungszahlen (V3 6 von 7, V2 4 von 5) ein; die neuen Dateien des Umsetzers (evo1_v2.py, v2-bewertung/,
  a2-pruefung/, rauch-v3/, LAUF-*-v3.log) werden in Abschnitt 1 (Dateien) genannt.

### N4. Offener Punkt (1): "bitgleich taugt auf der .69 grundsaetzlich nicht"

- **Zu breit.** Bitgleichheit ist belegt fuer: die Neubewertung aus zustand.json (A2), alle Entscheidungsfelder,
  die fit_linear-Felder (R2_lin, x_stern_lin), die Kontrolle-modell.json sogar ueber zwei Rechner und zwei
  torch-Versionen hinweg. Sie versagt nur bei den vier Feldern aus torch.linalg.lstsq, dort mit 1e-13 bis 1e-14.
- **Anforderung:** Gleichheitspruefungen in EVO-1 heissen ab jetzt: Entscheidungsfelder und alle Felder ohne lstsq
  byteweise, lstsq-Felder relativ hoechstens 1e-10 (Pruefung wie in N3). Kein "bitgleich" mehr ohne diese
  Aufteilung.
- **Anforderung (Text, zu A5):** Die Formulierung "der Anker rechnet also bitgleich zu Runde 6" (PLAN.md, Abschnitt 2
  und Abschnitt 9, L3) wird zu "gleicher Rechenweg; Uebereinstimmung auf allen gedruckten Stellen". Die
  Wiederholungsstreuung des Rechenwegs selbst (Profil, Newton, Kontur) ist auf der .69 nicht gemessen; keine Messung
  verlangt, aber auch keine Bitgleichheits-Behauptung dafuer.
- **Anforderung (Vermerk, keine Regelaenderung):** Liegt in einer Generation eine Entscheidungsgroesse naeher als
  1e-9 relativ an ihrer Schwelle (h: g0 gegen 1e-3 Gamma_ref) oder liegen zwei g0_rel von Elternkandidaten im Arm E
  naeher als 1e-9 beieinander, wird das Modell in RUNDE-07.md als "an der Rauschgrenze" vermerkt. Entschieden wird
  weiter nach der bestehenden Regel.

### N5. Offener Punkt (2): viertes oder fuenftes aufgeloestes Minimum nur in grob_Gamma

- **Angenommen ohne Codeaenderung vor Generation 1.** grob_Gamma traegt alle 12 Spurwerte je Modell; "alle werden
  berichtet" ist damit in der Sache erfuellt, nur nicht als Liste. Eine weitere Codeaenderung jetzt kostet eine neue
  A2/A3-Runde und bringt fuer Generation 1 nichts, weil ein viertes Minimum auf 12 Grobpunkten fern liegt.
- **Anforderung (pruefbar, je Generation vor der Auswertung):** Ueber bew-00N.jsonl laeuft

  `jq -c '(.v.grob_Gamma // {} | [.[]]) as $G | {key, innere_minima: ([range(1; ($G|length)-1) | select($G[.] < $G[.-1] and $G[.] <= $G[.+1])] | length), gelistet: (((.v.grob_minima // []) | length) + ((.v.grob_minima_unter_aufloesung // []) | length))} | . + {luecke: (.innere_minima > .gelistet)}' bew-00N.jsonl`

  Jedes Modell mit luecke = true erhaelt in RUNDE-07.md den Vermerk "Minimum ueber MAX_MIN, nicht verfeinert". Am
  30.09.2026 fuer Generation 0: Anker 2 von 2, Kontrolle 1 von 1, keine Luecke.

### Geprueft (Nachtrag)

- Lokal: UMSETZUNG-V3.md ganz (mit Diff-Anhang); lauf-69/v2-bewertung/ (SHA256SUMS -c: alle OK);
  lauf-69/v3-bewertung/ (SHA256SUMS -c: 45 OK), darin modell.json und zustand.json von Anker und Kontrolle,
  a2-pruefung/ (10 Auszuege), LAUF-G0A-v3.log, LAUF-G0B-v3.log, LAUF-Z0-v3.log, rauch-v3/LAUF-kopie-anker.log,
  rauch-v3/wdh/LAUF-wdh.log und die 10 Wiederholungsordner; rauch/v3/ (rauch_bericht.txt, kopien.log, SHA256SUMS.txt,
  vier Kopien); evo1.py (f882fa19, 1038 Zeilen), evo1_v2.py (d81870bf).
- .69 (nur lesend): sha256 von evo1.py, evo1_v2.py, evo1_v1.py, resonanz3d.py, beiden ergebnisse-modell.json,
  v2-bewertung, rauch-v3/kopie-anker, 10 wdh-Dateien, bew-000.jsonl, LAUF-Z0.log, LAUF-Z0-v3.log; ls des
  Ordners; pyvenv.cfg, remote_gpu_runtime.pth, torch-2.5.1+cu121.dist-info/METADATA, torch/lib, /proc/cpuinfo,
  ~/.bashrc, ~/.profile, systemd-Nutzerumgebung (keine MKL- oder OMP-Variablen).
- Nicht geprueft: der Mechanismus der Streuung (wuerde einen Rechenlauf brauchen).

### Einfach gesagt (Nachtrag)

Beim Vorbild weichen nach der Neubewertung drei Zahlen erst an der dreizehnten Stelle ab. Ich habe nachgesehen: Die
Eingaben waren in allen dreizehn Laeufen exakt gleich, der Rechenschritt wurde nicht veraendert, und die alte Fassung
liefert auf der .69 in einem von fuenf Laeufen dieselbe Art Abweichung. Also streut der Rechner, nicht die neue
Regel. Die Auflage "bitgleich" wird deshalb zu "alle Entscheidungen exakt gleich, die drei Anpassungszahlen bis auf
ein Zehntel Milliardstel gleich"; das ist tausendfach strenger als jede Entscheidung braucht und wurde geprueft.
Version 3 ist damit frei.
