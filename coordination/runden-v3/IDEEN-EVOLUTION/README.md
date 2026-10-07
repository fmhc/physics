# Ideen-Evolution: EVO-1 fuer unsere Arbeitsweise (Ablauf einer Generation)

- **Auftrag:** claude-primary nach Finn im Chat: "bau mal eine weiterentwicklung davon angepasst an das was wir immer
  machen: ideen mit neuen ideen und research bewerfen und analogien suchen und ideation sachen machen und gucken was gut
  ist". "Davon" ist EVO-1 (RUNDE-07/GAUNTLET-NEUSTART-PLAN.md).
- **Bearbeiter:** Anthropic-Subagent (Opus 5.5). Beginn (date) 2026-09-30 04:29:57 CEST, Ende (date) 2026-09-30 04:54:13 CEST.
- **Status:** Vorschlag, nichts gestartet. Gilt als Ablauf innerhalb von v3 (evolution-review-20260929/V3-ENTWURF.md), ist
  kein neues Regeldokument und aendert keine v3-Regel. Die Leitung startet.

## 1. Kern

Population sind Ideenkarten (pool.jsonl, 131 Karten aus RUNDE-07/IDEATION-UEBERSICHT.md). Eine Generation waehlt Eltern,
laesst Operatoren daraus neue Karten machen, testet alle Karten klein, laesst sie von einem frischen Leser blind ernten und
schaetzt sie ab. Pflicht ist ein Zufallsarm aus dem Bestand: Bisher war unsere Auswahl nicht besser als Wuerfeln (4 von 27
gewaehlten gegen 1 von 5 Zufallskarten "weiter", IDEATION-UEBERSICHT.md, Kurz 4). Keine Jury, kein Register, kein Dienst.

## 2. Ablauf einer Generation (etwa 65 min Wandzeit)

| Schritt | wer | Zeit | was |
|---|---|---|---|
| 1 Auswahl | Leitung | 5 min | Eltern waehlen: "weiter" und gute "parken", je ein Satz Grund in GEN-NN.md. `python3 ie.py ziehen --gen N --saat S --slots "..."` zeigt Zufallsarm, Reserve und neutrale Nummern; dann dasselbe mit `--eintragen` |
| 2 Operatoren | 2 Agenten parallel | 15 min Zeitbox | Aussen (research, analogie) und innen (mutation, kreuzung, ideation), Vorlagen in vorlagen/. Je Slot genau eine Karte: GEN-NN/<id>/KARTE.md und HERKUNFT.md |
| 3 Testen | 2 Test-Agenten parallel, dann Leitung | 15 min Code, 10 min Rechnung | Test-Agent schreibt fuer jede Karte, auch fuer Z, einen kleinen Test (vorlagen/TEST.md). Die Vorhersage steht vor dem Lauf in KARTE.md. Die Leitung rechnet ueber kleintest.sh (.69) oder lokal |
| 4 Ernte | 1 frischer Agent | 10 min | sieht nur G-Nummern, KARTE.md und Ausgaben, keinen Arm (vorlagen/ERNTE.md). Abgleich in beide Richtungen; schlaegt L1 bis L5 und eine Entscheidung vor |
| 5 Abschaetzung | Leitung | 10 min | Tabelle wie v3, Abschnitt 3; `ie.py setze` fuer entscheidung, latten, vorschlag_blind, testpfad, ergebnis_kurz; dann `ie.py statistik`, ein Journaleintrag, Bericht an Finn |

- Karten mit gleichem Code-Unterbau gehoeren zu einem Test-Agenten. Getrennt vom Operator testet er, damit E, Z und F
  denselben Test-Weg haben; nur so misst der Arm-Vergleich die Auswahl und die Operatoren.
- Z-Karten werden nicht umgebaut: Der Test-Agent bringt sie nur ins Kartenformat. Passt auch ein geschrumpfter Test nicht
  in 10 min, ersetzt die Leitung sie durch die erste Reservekarte (`ie.py setze G1-xx eltern=...`) und vermerkt das.
- Codex als Zweithaus: hoechstens eine "weiter"-Karte je Generation mit hohem Nutzen rechnet Codex blind nach (Karte und
  Vorhersage, nicht unser Ergebnis), wie bei 0,7977. Das haelt die naechste Generation nicht auf.

## 3. Operatoren

| Operator | was | Eltern | Vorlage |
|---|---|---|---|
| research | Literatur und arXiv zur Elternkarte; Mechanismus oder Messung, die die Karte schaerft, stuetzt oder als bekannt ausweist | 1 | OP-RESEARCH.md |
| analogie | Mechanismus aus einem anderen Feld (Biologie, Chemie, Wellen, Festkoerper, Optik, Kernphysik, Oekonomie ...) auf den Befund uebertragen | 1 | OP-ANALOGIE.md |
| kreuzung | zwei Karten verbinden: Mechanismus der einen auf den Befund der anderen | 2 | OP-KREUZUNG.md |
| mutation | eine Annahme der Karte variieren: Dimension, Potential, Kopplung, Randbedingung | 1 | OP-MUTATION.md |
| ideation | frische Idee ohne Elter (Arm F) | 0 | OP-IDEATION.md |
| zufall | keine Variation; Bestandskarte, mit fester Saat gezogen (Arm Z) | 1 | nur TEST.md |

Kartenformat (alle Vorlagen): Hypothese; kleiner Test mit Rechenort und hoechstens 10 min; Vorhersage vorab mit
"scheitert, wenn"; Gegenprobe, in der der Effekt verschwinden muss; Plausibilitaetsschranke (0 <= T <= 1, Bilanzen, v < 1);
erwartete Latten L1 bis L5; "Einfach gesagt". Herkunft (Eltern, Operator, Quellen) steht nur in HERKUNFT.md.

## 4. Regeln, die jede Generation braucht

- **Scheitern koennen:** Eine Karte ohne Test, der scheitern kann, bekommt L1 "schwach" und kann nicht "weiter".
  `ie.py pruefen` meldet "weiter" ohne "L1 ja".
- **Vorhersage vor Ergebnis:** Der Test-Agent setzt fuer alle Arme gleich vor jedem Lauf (auch vor der Formprobe) die
  Zeile "Vorhersage geschrieben: <date>" in KARTE.md; danach bleibt die Datei unveraendert. Die Ernte vergleicht die
  Zeile mit der "start"-Zeile von kleintest.sh. Liegt sie nicht davor, heisst es "nicht als
  vorab belegbar" (RUNDE-06, Berichtigung 04:05:59, Punkt 2).
- **Wortlaut der Belegebene** (dieselbe Berichtigung): nur sagen, was gemessen ist (kleinster Wert, Ort, Stufe, Haus);
  unter der Aufloesung nur obere Schranke; "auf dem Raster nicht gesehen" statt "gibt es nicht"; Deutungen als Hypothese.
- **Jede eingetragene Karte bekommt eine Entscheidung.** Nicht gelieferte oder nicht entscheidbare Karten zaehlen als
  nicht "weiter".
- Neuer Code hoechstens 1 h je Karte, sonst parken (v3, Abschnitt 6). Formale Tests nur nach v3, Abschnitt 5.

## 5. Statistik und Vorsprungsregel (vorab festgelegt, vor Generation 1 nicht mehr aendern)

- `ie.py statistik` zaehlt je Generation und Arm: entschiedene Karten, "weiter" der Leitung, "weiter" des blinden
  Ernte-Vorschlags; dazu "weiter" je Operator (nur beschreibend).
- **Regel:** Die Evolution (Arm E) gilt als besser als Zufall (Arm Z), wenn ueber Generation 1 und 2 zusammen gilt:
  q_E >= 1,5 q_Z und q_E - q_Z >= 0,20, beides mit der Entscheidung der Leitung und mit dem blinden Vorschlag;
  dazu n_E >= 10 und n_Z >= 6. Fehlen Daten (offene Karten, blinde Vorschlaege), zaehlt Generation 2 und 3.
- **Trennschaerfe, ehrlich** (Binomial von Hand, nur Leitungsurteil): Bei gleicher wahrer Quote 17 % in beiden Armen
  meldet die Regel mit etwa 12 % Wahrscheinlichkeit faelschlich Vorsprung; ein echter grosser Vorsprung (40 % gegen 17 %)
  wird nur mit etwa 56 % erkannt. Die Regel trennt also nur grosse Unterschiede.
- **Folge:** Vorsprung: weiter in Generationen, Z bleibt mit 2 Karten als laufende Kontrolle. Kein Vorsprung: die
  Operatoren bleiben normale v3-Variation, der Bestand wird per Zufall abgearbeitet; das wird als vierter Werkzeugtest
  ("kluge Suche ohne belegten Vorteil") aufgeschrieben.

## 6. Abbruch

- Spaetestens nach Generation 3: Schlussstatistik, Journal, Bericht.
- Mehr als 30 % der Tests einer Generation nicht entscheidbar (Kontrolle oder Messgroesse gerissen): anhalten, zuerst
  TEST.md reparieren (Lehre aus Runde 5).
- Zwei Generationen ohne "weiter" in allen Armen: den Eingang wechseln, nicht die Regeln (v3, Abschnitt 6).
- Eine Generation braucht mehr als das Doppelte (130 min): mit Finn neu planen, nicht still weiter.

## 7. Rollen

- **Leitung:** waehlt Eltern und Slots, ruft ie.py, startet Agenten und Rechnungen, schaetzt ab, schreibt Journal und Bericht.
- **Operator-Agenten (2):** je Slot eine Karte, nichts gerechnet ausser Papier und Literatur.
- **Test-Agenten (1 bis 2):** kleine Tests fuer alle Arme gleich, lokale Formprobe hoechstens 120 s.
- **Ernte-Agent (1, frisch):** blind zum Arm, Abgleich in beide Richtungen, Vorschlag je Karte.
- **Codex:** Zweithaus fuer hoechstens einen tragfaehigen Befund je Generation.

## 8. Dateien und Befehle

- **pool.jsonl:** Felder id, titel, quelle, stand, entscheidung, modellbezug, generation, eltern, operator, arm, testpfad,
  ergebnis_kurz; ab Generation 1 dazu latten und vorschlag_blind. Generation 0 gibt IDEATION-UEBERSICHT.md wieder (Stand
  04:04 bis 04:17): entscheidung ist die Abschaetzung woertlich (erstes Wort zaehlt), testpfad die Spalte "getestet"
  woertlich, operator die Herkunftsgruppe, arm "Z" fuer die fuenf v3-Zufallskarten, sonst "bestand".
- **Nachtragen vor Generation 1:** R7 (MT-1 und V-3 als Papier fertig, RUNDE-07.md), M1 und M2 (gerechnet, nicht geerntet)
  und die 18 "offen" per `ie.py setze`. Laufende Karten (stand "laeuft") zieht ie.py nie.
- **ie.py:** `pruefen`, `ziehen`, `setze`, `statistik` (Kopf der Datei). Nur `ziehen --eintragen` und `setze` schreiben,
  vorher pool.jsonl.bak-JJJJMMTT-HHMMSS.
- **GEN-NN.md** (wie RUNDE-NN.md) und GEN-NN/<id>/ mit KARTE.md, HERKUNFT.md, Code, Ausgaben.
- **Journal:** je Generation eine JSON-Meldung wie research-journal/claude-runde-v3-06-20260930.json (evidenzart "modell";
  der Arm-Vergleich "verfahren"), dann `python3 coordination/research_journal.py pruefen <datei>` und
  `python3 coordination/research_journal.py <datei>`. Nur die Leitung, kein Skript.

## 9. Rauchtest (zwischen 04:44:06 und 04:46:06 laut date, Laptop, nice 19, timeout 60, nur Standardbibliothek)

- `python3 ie.py pruefen`: 131 Karten, weiter 19, parken 49, verwerfen 11, offen 18, ungetestet 32, indirekt 2, gleich
  IDEATION-UEBERSICHT.md, Abschnitt 1; "pruefen: ok".
- `python3 ie.py ziehen --gen 1 --saat 20260930`: rc 0, pool.jsonl unveraendert (sha256 vorher und nachher gleich).
- `python3 ie.py statistik` am echten Pool (nur lesend): Generation 0 mit Z 1 von 5 und Bestand 18 von 74 "weiter".
- `setze` und `ziehen --eintragen` nur an einer Kopie im Scratchpad, dazu zwei ausgedachte Generationen: .bak entsteht,
  doppeltes Eintragen wird abgelehnt, "weiter" mit L1 schwach wird gemeldet, die Vorsprungsregel rechnet (Testdaten, kein
  Befund).
- ie.py hat 169 Zeilen, etwas mehr als die angepeilten 150.

## Einfach gesagt

Wir behandeln unsere Ideen wie eine Zucht: Die besten Ideen bekommen "Kinder", indem Agenten Literatur dazu suchen,
Vergleiche aus anderen Fachgebieten finden, zwei Ideen kreuzen oder eine Annahme veraendern. Jede Idee wird dann in
hoechstens zehn Minuten getestet, und ein unabhaengiger Leser, der nicht weiss, woher die Idee kommt, bewertet das Ergebnis.
Zum Vergleich testen wir jedes Mal auch ein paar zufaellig gezogene alte Ideen. Nur wenn die gezuechteten Ideen deutlich
oefter tragen als die zufaelligen, lohnt sich die Zucht; sonst sparen wir uns den Aufwand.
