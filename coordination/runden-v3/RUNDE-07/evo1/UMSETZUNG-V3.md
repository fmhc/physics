# EVO-1 Version 3: Umsetzung der Reparatur nach A1 (Runde 7)

- **Auftrag:** Leitung (claude-primary). Pflichtenheft sind die Auflagen A1, A2, A3, A4 und A7 aus
  LESUNG-REPARATUR-A1.md (Empfehlung FREIGEBEN MIT AUFLAGEN). A5, A6 und A8 bucht die Leitung.
- **Bearbeiter:** Code-Agent (Anthropic, Opus 5.5).
- **Nicht getan:**
  - Generation 1 nicht gestartet
  - PLAN.md nicht geaendert
  - keine Schwelle geaendert
  - kein weiteres Modell gerechnet
  - kein git, kein Journal
- **Beginn (date):** 2026-09-30 05:56:56 CEST. **Ende (date, vor dem Schreiben dieser Datei gemessen):** 2026-09-30
  06:12:23 CEST.

## Ergebnis vorab

- **Abbruchkriterium A1 (Generation 0): bestanden** mit Version 3 (LAUF-Z0-v3.log, Abschnitt 5).
- **Auflage A3 (Anker bitgleich): formal nicht erfuellt.**
  - Die echte Neubewertung des Ankers ergab eine modell.json, die in 4 Zeilen von der Version-2-Datei abweicht:
    c, g0 und g0_rel der Parabelanpassung am Minimum k = 8, relativ hoechstens 2e-13.
  - Ursache ist nicht Version 3. Die Parabelanpassung ist auf der .69 nicht bitweise reproduzierbar, auch mit Version 2:
    Eine von 5 Wiederholungen mit Version 2 wich an denselben Feldern ab (Abschnitt 4, A3).
  - Die Lesung sagt fuer A3: "Bei Abweichung: nicht freigegeben, zurueck zur Lesung." Die Entscheidung liegt bei der
    Leitung.
- A1 (Bericht), A2, A4 und A7: erfuellt.

## 1. Zeitleiste (date; die .69 zeigt UTC, plus 2 h = CEST)

| Zeit CEST | Schritt |
|---|---|
| 05:56:56 | Beginn, Lesen von PLAN.md, LESUNG-REPARATUR-A1.md und evo1.py (Version 2) |
| 06:00:12 bis 06:01:03 | .69: Bestand und sha256 geprueft; kein EVO-1-Prozess, keine Klein-Unit fuer EVO-1 (eine bic2-Unit hielt den Lock cpu4) |
| 06:01:21 | A4: Sicherung auf der .69 (runde7-evo1/v2-bewertung/) |
| 06:01:31 | A4: lokal gespiegelt (lauf-69/v2-bewertung/), sha256 -c alle OK |
| 06:03:20 | evo1_v2.py lokal angelegt (cp -p), danach Version 3 in evo1.py geschrieben |
| 06:04:45 bis 06:05:15 | A7 lokal: rauch --out rauch/v3 (rc 0) |
| 06:05:36 bis 06:05:44 | A7 lokal: modell auf Kopien von Anker und Kontrolle, je Version 2 und 3 (--budget 5) |
| 06:06:38 | .69: evo1_v2.py angelegt (cp -p), Version 3 als evo1.py.v3-neu hochgeladen, sha256 gleich |
| 06:06:53 bis 06:07:03 | Zusatz: Vorpruefung von Version 3 an Kopien auf der .69 (kleintest.sh cpu) |
| 06:07:09 und 06:07:13 | Prozesspruefung leer, dann `mv evo1.py.v3-neu evo1.py`; sha256 lokal und .69 gleich |
| 06:07:31 bis 06:07:54 | A2: jq-Auszuege vorher, Prozesspruefung leer (06:07:37), Neubewertung von Anker und Kontrolle |
| 06:08:40 | A2: jq-Auszuege nachher |
| 06:08:50 bis 06:08:52 | zusammenfassen --gen 0 nach LAUF-Z0-v3.log |
| 06:09:20 bis 06:09:49 | Zusatz: Wiederholungstest (je 5 Laeufe Version 2 und 3 an Kopien des Ankers) |
| 06:10:58 | .69-Ergebnisse lokal gespiegelt (lauf-69/v3-bewertung/), sha256 geprueft |

## 2. sha256

| Datei | sha256 |
|---|---|
| evo1.py Version 2 (985 Zeilen); lokal als evo1_v2.py, auf der .69 als evo1_v2.py | d81870bfea7a8ee744a8393a745e7efd97d03b95db5ae0a07295dd7fb97121b6 |
| evo1.py Version 3 (1038 Zeilen); lokal und .69 gleich | f882fa19e6080dfcff3a9084e3bc7482188ae444e9097259b883095aa5736583 |
| resonanz3d.py (unveraendert, lokal und .69) | 99c54b9ccdb517c1a033669cd664586e642f59fc58f82fd6df8f0d83b7b5bcb0 |
| Anker modell.json Version 2 (Sicherung) | a60c461de17977d3caa0604049cf4bfa61671faa26e2aa4d1e5510be5294de22 |
| Anker modell.json nach Version 3 (.69) | a9cef0d287b9f62467e53fe220ad2ebfe6d2071c38b174453e7b8bc8786b5b88 |
| Kontrolle modell.json Version 2 (Sicherung) | 5efd8133489d93e53d96f7c9b748c1577cba7093e78c169cc1596fd7df419b8e |
| Kontrolle modell.json nach Version 3 (.69) | 8dba8208df8bc221faf86832037c8d696eda776f8441934fe60437305738a904 |
| LAUF-Z0.log (alt, unveraendert) | 11d13258c4f59a2402ae854b21784df00f06056816270c986e4057766e3d161d |
| LAUF-Z0-v3.log | 98b0ba7a3cb48781dca2842dfb21e0bc454b4ded9abe338c488fd5b20540d82c |
| bew-000.jsonl Version 2 (Sicherung) / nach Version 3 | 1900a2e7... / 28da1d4f56202834691b7cecbe37d7c654cc18c583b4550e5e9bf946fa44f5e0 |

**Versionsangabe in modell.json:** keine. Die Schluessel beider Dateien enthalten kein Versionsfeld; grep nach "version"
in modell.json und zustand.json ist leer. A3 kann daran also nicht scheitern.

## 3. Diff Version 2 gegen Version 3

- **Regel:**
  - neue Konstante G_BODEN = 1e-8
  - Filter in grob_minima: Beide Nachbarn auf der Spur brauchen Gamma_A > G_BODEN.
- **Bericht:**
  - neue Methode grob_minima_unter_aufloesung
  - in bewerte das Feld (nur wenn nicht leer) und der neue Grund; ohne jedes innere Minimum bleibt der alte Grund
  - eine Zeile in zusammenfassen
- **Sonst:** Kopfvermerk und Rauchtest-Teil 5. Nichts anderes ist geaendert.

Der vollstaendige Diff (`diff -u evo1_v2.py evo1.py`) steht im Anhang am Ende dieser Datei.

## 4. Auflagen: Pruefbeleg und Ergebnis

### A4 Sicherung vor dem Ueberschreiben: erfuellt

- **.69**, runde7-evo1/v2-bewertung/, 04:01:21 UTC, mit cp -p:
  - P_b0.5000_g0.0000_d3/modell.json (a60c461d...)
  - P_b0.5000_g0.0000_d1/modell.json (5efd8133...)
  - bew-000.jsonl (1900a2e7...) und LAUF-Z0.log (11d13258...)
  - dazu fuer A2 beide zustand.json (d3 3cb7466a..., d1 b6c0fb55...) und SHA256SUMS.txt
- **Lokal** gespiegelt nach RUNDE-07/evo1/lauf-69/v2-bewertung/ (rsync -a). `sha256sum -c SHA256SUMS.txt` gibt auf
  beiden Seiten alle OK.
- **Neue Logdatei:** Die neue Zusammenfassung steht in LAUF-Z0-v3.log. LAUF-Z0.log ist unveraendert (11d13258... vorher
  und nachher).
- **Ueberschrieben:** bew-000.jsonl in runde7-evo1 wurde von zusammenfassen neu geschrieben. Die alte Fassung liegt in
  v2-bewertung/.

### A1 Bericht der weggefallenen Minima: erfuellt

- **Feld:** modell.json fuehrt das Feld grob_minima_unter_aufloesung nur, wenn es nicht leer ist. Jeder Eintrag hat:
  - k und x_grob
  - etikett "unter Aufloesung"
  - Gamma_grob (Stufe A)
  - Gamma_nachbarn [links, rechts] (Stufe A)
- **Pruefung** an der Version-3-modell.json der Kontrolle auf der .69 (8dba8208...):
  `{"k": 10, "x_grob": 0.8927272727272728, "etikett": "unter Aufloesung", "Gamma_grob": -9.859437641558729e-10,
  "Gamma_nachbarn": [1.0391940481848508e-08, -8.506458295428423e-10]}`. Das ist 0,89273 mit 1,039e-8 und -8,51e-10.
  - Dazu F2 = "nein", Urteil "nicht qualifiziert", Grund "kein aufgeloestes Minimum (Nachbarn unter 1e-8)"
  - grob_minima ist leer
  - bew-000.jsonl enthaelt dasselbe Feld
- **zusammenfassen:** Direkt unter der A3-Zeile steht jetzt "Modelle mit weggefallenen groben Minima (unter Aufloesung,
  Version 3): 1 von 2".

### A7 Rauchtest Version 3: erfuellt

- **Rahmen:** lokal auf dem Laptop, CPU, CUDA_VISIBLE_DEVICES leer, OMP_NUM_THREADS und MKL_NUM_THREADS 1,
  torch.set_num_threads(1), nice -n 19, timeout 120, PYTHONDONTWRITEBYTECODE=1. Ausgaben in rauch/v3/ (SHA256SUMS.txt).
- **Teile 0 bis 3** (rauch_bericht.txt, 28,0 s, rc 0): zeilengleich zu rauch/v2/rauch_bericht.txt, ohne Zeit- und
  Datumsangaben (diff leer). Also:
  - Koeffizienten 7,1e-15
  - drei synthetische F2-Kurven ja / nein / nein
  - rho(0,7) = 1,7018102864766265 - 1,468016e-3 i
- **Teil 5** (neu, synthetische Spuren durch grob_minima und bewerte, die Regel von Version 2 wortgleich zum
  Vergleich), 4 von 4 "ok":
  - **Kontrollmuster** (Stufe-A-Werte der .69-Kontrolle; ein Nachbar 1,0392e-8, also 4 % ueber dem Boden, der andere
    -8,506e-10):
    - Version 2 verfeinert 0,89273, Version 3 nichts.
    - Das Feld nennt k 10 mit beiden Nachbarwerten.
    - F2 nein, neuer Grund. Das Minimum faellt weg.
  - **V-Form**, Tiefpunkt 2e-10 genau auf einem Grobpunkt, Nachbarn 8e-5 und 1,1e-4:
    - Das Minimum bleibt (zu_verfeinern [5]). Das ist der in PLAN.md Abschnitt 12 angekuendigte Fall.
    - Der Wert selbst unter dem Boden zaehlt nicht, nur die Nachbarn.
  - **Fuenf grobe Minima, davon zwei Scheinminima** (0,81818 mit Nachbarn 9e-9 und 6e-9; 0,89273 mit 6e-9 und -5e-10):
    - Version 2 verfeinert 0,89273, 0,81818 und 0,70636, also zwei Scheinminima; die echten Minima 0,63182 und
      0,55727 werden verdraengt.
    - Version 3 verfeinert 0,70636, 0,63182 und 0,55727, also die drei echten. bewerte gibt zu_verfeinern [5, 3, 1] und
      naechstes "fein".
    - Beide Scheinminima stehen im Feld.
  - **Monoton fallend:** kein Minimum; der alte Grund "kein lokales Minimum der Breite" bleibt.
- **(a) Kopie der Kontrolle** (endgueltiger .69-Zustand aus v2-bewertung/, `modell ... --budget 5`):
  - Version 3 gibt F2 nein, Urteil "nicht qualifiziert" und den neuen Grund. Im Feld steht 0,89273 mit 1,0392e-8 und
    -8,506e-10.
  - Version 2 auf derselben Kopie gibt "nicht entscheidbar", wie auf der .69.
  - Die lokale Version-3-Datei ist gleich der spaeteren .69-Datei (8dba8208...).
- **(b) Kopie des Ankers:**
  - Lokal geben Version 2 und Version 3 dieselbe Datei (beide d497bb19...).
  - Gegen die .69-Datei a60c461d... weichen beide lokalen Laeufe ab, nur in c, x_stern, g0 und g0_rel der
    Parabelanpassungen, fruehestens an der 13. gueltigen Stelle (g0 bei k = 3). Grund ist die Umgebung: lokal torch
    2.10.0, auf der .69 torch 2.5.1+cu121.
  - Deshalb die Zusatzpruefung auf der .69 (06:06:53 CEST): Version 3 (noch unter dem Namen evo1.py.v3-neu) an einer Kopie
    des Ankers gibt bitgleich a60c461d...
- **Zustands-Kopien:** Ohne aufrufe sind sie unveraendert, aufrufe ist je um einen Eintrag laenger.

### A2 Neubewertung ueber modell: erfuellt

- **Befehle** (PLAN.md Abschnitt 7, Version 3, Spur cpu; Logs mit absolutem Pfad):
  - `cd /home/fmh/fmhc-physics-remote/runde7-evo1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu
    evo1-anker-v3 evo1.py modell --familie P --beta 0.5000 --gamma 0.0000 --dim 3 --out ergebnisse/P_b0.5000_g0.0000_d3
    --zusatz 0.798` nach LAUF-G0A-v3.log
  - `... kleintest.sh cpu evo1-kontr1d-v3 evo1.py modell --familie P --beta 0.5000 --gamma 0.0000 --dim 1 --out
    ergebnisse/P_b0.5000_g0.0000_d1` nach LAUF-G0B-v3.log
- **Dauer:**
  - Anker 04:07:43 bis 04:07:49 UTC (Service runtime 6,309 s)
  - Kontrolle 04:07:49 bis 04:07:54 UTC (4,946 s)
  - beide "Ende ..., 0.0 s, offen: None", Status fertig, rc 0. Jeder Aufruf blieb unter 30 s.
- **Zustand:**
  - `jq -S '{grob, fein, zusatz, zeiten}'` ist vorher und nachher gleich (cmp; sha256 d3 e57adb90..., d1 9dcd02c7...).
  - Auch der ganze Zustand ohne aufrufe ist gleich (d3 24de9f18..., d1 e4178cfd...).
  - Vor der Neubewertung waren beide zustand.json und modell.json gleich der Sicherung (cmp).
- **aufrufe:**
  - Anker 4 -> 5, Kontrolle 2 -> 3; die alten Eintraege sind unveraendert.
  - neuer Eintrag Anker: start und ende 04:07:49 UTC, sek 0,0079, offen null
  - neuer Eintrag Kontrolle: start und ende 04:07:54 UTC, sek 0,0057, offen null
- **zusammenfassen --gen 0:** nach LAUF-Z0-v3.log (04:08:50 bis 04:08:52 UTC, rc 0).
- **Belege:** runde7-evo1/a2-pruefung/ (Auszuege vorher und nachher), lokal unter lauf-69/v3-bewertung/a2-pruefung/.

### A3 Anker bitgleich: formal nicht erfuellt (Ursache nicht Version 3)

- **Befund:** ergebnisse/P_b0.5000_g0.0000_d3/modell.json nach der Neubewertung ist a9cef0d2..., die Version-2-Datei
  a60c461d... Der diff hat 4 Zeilen, alle aus fit_parabel (torch.linalg.lstsq) am Minimum k = 8 (0,81818):
  - c: 0.9274503615183379 -> 0.9274503615183312 (relativ 7e-15)
  - g0: -6.970729825930934e-08 -> -6.97072982593229e-08 (relativ 2e-13)
  - g0_rel (in minima und oben): -0.00018521600218867904 -> -0.00018521600218871507 (relativ 2e-13)
- **Unveraendert:**
  - x_stern 0,7975542496031367
  - R2_lin, F0 bis F3, qualifiziert, Urteil
  - Zusatz 0,798 (B 1,1209e-7, C 1,1224e-7)
  - das zweite Minimum k = 3
  - die A1-Zeile
- **Ursachenpruefung** (Zusatz, nicht beauftragt, nur Bewertung an Kopien, nichts gerechnet, je `--budget 5`):
  - Vorpruefung, Version 3 an einer Kopie, 04:06:53 UTC: bitgleich a60c461d...
  - Wiederholungstest, 04:09:20 bis 04:09:49 UTC, 10 frische Kopien des gesicherten Anker-Zustands, abwechselnd
    Version 2 und 3:
    - Version 3: 5 von 5 bitgleich a60c461d...
    - Version 2: 4 von 5 bitgleich. Lauf 2 gibt e8981201..., abweichend in denselben vier Zeilen (g0_rel
      -0.00018521600218869482, relativ 8,5e-14).
  - Zusammen: Version 3 traf die Version-2-Datei in 6 von 7 Laeufen, Version 2 sich selbst in 4 von 5 Wiederholungen.
    Die Streuung gehoert zur Rechenumgebung der .69 (CPU Xeon E5-2630 v2, torch 2.5.1+cu121), nicht zur Regelaenderung.
  - Vermutung, nicht geprueft: LAPACK/MKL waehlt je nach Speicherlage einen anderen Rechenweg. Die gewichtete Anpassung
    an k = 8 ist schlecht konditioniert (Gewichte 1/Gamma ueber etwa 3,6 Groessenordnungen).
- **Bewusst nicht getan:**
  - den echten Lauf wiederholen, bis der Hash passt; das waere eine Kontrolle, die nach dem Befund gelockert wird
  - die Version-2-Datei zurueckkopieren
  - Der Zustand auf der .69 ist der Stand nach Version 3; alle Version-2-Dateien liegen in v2-bewertung/.
- **Folge laut Lesung (A3):** "Bei Abweichung: nicht freigegeben, zurueck zur Lesung." Die Entscheidung liegt bei der
  Leitung. Moegliche Wege, nicht umgesetzt:
  1. Die Lesung wertet A3 als "gleich bis auf die belegte Streuung der lstsq-Stellen; alle Entscheidungsfelder gleich".
  2. Zusaetzlich wird die Version-2-Datei aus v2-bewertung/ zurueckkopiert. Das ist kosmetisch und aendert die Ursache
     nicht.
  3. fit_parabel wird deterministisch gemacht. Das waere eine weitere Code-Aenderung, und sie aendert selbst die
     g0-Stellen gegen Version 2.

## 5. A1-Zeile aus LAUF-Z0-v3.log (woertlich)

```
A1: Anker omega*^2 (F2 ja) = [0.7975542496031367], Gamma(0,798) = 1.1224047097032925e-07, F2 Anker ja; Kontrolle dim 1 F2 = nein -> bestanden
```

Dazu aus derselben Datei:
- "Generation 0: 2 Modelle, fertig 2, lebensfaehig 2, qualifiziert 1, nicht entscheidbar 0"
- "A3 (nicht entscheidbar > 20 %): 0% -> weiter"
- "Modelle mit weggefallenen groben Minima (unter Aufloesung, Version 3): 1 von 2"
- Tabellenzeile der Kontrolle: "| P_b0.5000_g0.0000_d1 | kontrolle | fertig | ja | ja | nein | None |  |  |  | nicht
  qualifiziert; kein aufgeloestes Minimum (Nachbarn unter 1e-8) |"

## 6. Offene Punkte

1. **A3:** Entscheidung der Leitung beziehungsweise der Lesung (Abschnitt 4, A3). Bis dahin ist Version 3 formal nicht
   freigegeben. Generation 1 habe ich nicht gestartet.
2. **Buchungen der Leitung:**
   - A5: Abschnitt 12 ergaenzen und berichtigen.
   - A6: Filter und Boden in Abschnitt 3 eintragen; sha256 von Version 3 (f882fa19...) in Abschnitt 7 und 12; PLAN.md auf
     die .69 spiegeln (dort liegt noch die Fassung von 05:00, sha256 314b2e4a...); Vermerk "Reparaturkontingent
     verbraucht".
   - A8: Generation 1 vollstaendig mit Version 3; vor Generation 2 die R-Wirkung (N8) vermerken.
3. **Nicht bitweise reproduzierbar:** modell.json ist auf der .69 nicht bitweise reproduzierbar. Das betrifft die letzten
   Stellen von c, x_stern, g0 und g0_rel. Pruefungen der Art "bitgleich" sind fuer diese Felder kuenftig nicht
   tragfaehig. Entscheidungen koennten nur bei exakten Gleichstaenden kippen: an der Schwelle h, bei der Wahl des besten
   Minimums oder bei der Elternwahl im Arm E ueber g0_rel.
4. **Minima jenseits MAX_MIN:** Ein viertes oder fuenftes aufgeloestes Minimum steht weiter nur ueber grob_Gamma in
   modell.json, nicht in grob_minima. Das ist seit Version 1 unveraendert. Die Lesung (A1) spricht von "jedem inneren
   groben Minimum der Spur", der Auftrag nur von den weggefallenen. Die Leitung sollte das pruefen.
5. **Kurzausgabe:** Die Kurzausgabe von `modell` (stdout, LAUF-Logs) zeigt das neue Feld nicht, nur den neuen Grund. Das
   Feld steht in modell.json und bew-00N.jsonl.
6. **Neu auf der .69 (von mir):**
   - evo1_v2.py (Kopie von Version 2)
   - v2-bewertung/, a2-pruefung/
   - rauch-v3/: Vorpruefungs-Kopien, wdh/ mit 10 Wiederholungskopien und LAUF-wdh.log
   - LAUF-G0A-v3.log, LAUF-G0B-v3.log, LAUF-Z0-v3.log
   - Alles liegt auch lokal unter lauf-69/v2-bewertung/ bzw. lauf-69/v3-bewertung/, je mit SHA256SUMS.txt.
7. **Nullnenner:** Der Zweig "Nullnenner" in x_schaetz ist mit Version 3 unerreichbar (Lesung N15); das steht im
   Kopfkommentar.

## 7. Regeln und Versehen

- **Lokale Interpreterstarts:** nur in der freigegebenen Form (siehe A7), fuenf Stueck:
  - einmal `evo1.py rauch --out rauch/v3`
  - viermal `modell ... --budget 5` auf Kopien in rauch/v3/
  - Kein `python3 -c`, kein awk; JSON nur mit jq.
- **.69:**
  - 15 Aufrufe ueber kleintest.sh, Spur cpu, je unter 10 s: 2 Vorpruefung, 2 Neubewertung, 1 zusammenfassen,
    10 Wiederholung.
  - evo1.py per mv ersetzt (neue Inode). Kein pgrep -f, kein pkill -f.
- **Versehen:** Die erste Prozesspruefung (04:01:03 UTC) traf den eigenen Pruefbefehl, weil das Wort "evo1" im
  echo-Text stand. Ich habe das an der PID erkannt; es lief kein EVO-1-Prozess. Spaetere Pruefungen enthielten das Wort
  nur noch als Muster [e]vo1.
- Keine Hooks, Dienste oder Timer; kein git, kein Journal.

## Einfach gesagt

Das Programm hielt ein winziges Zittern am Ende der 1D-Gegenprobe fuer eine echte Delle und kam deshalb zu "kann ich
nicht entscheiden". Die neue Fassung zaehlt eine Delle nur, wenn ihre beiden Nachbarn deutlich ueber dem Messrauschen
liegen. Weggefallene Dellen schreibt sie offen in den Bericht. Mit ihr sagt die Gegenprobe jetzt "nein", das Vorbild
bleibt "ja", und die Pruefung A1 ist bestanden. Eine Kleinigkeit ist offen: Beim Vorbild weichen einige Zahlen erst an
der 13. Stelle ab. Das passiert auf dem Rechner der .69 auch mit der alten Fassung, ist also Rechenrauschen und
kein Fehler der neuen Regel. Laut Pruefplan muss die Leitung trotzdem entscheiden, ob das als "gleich" gilt.

## Anhang: Diff Version 2 gegen Version 3 (vollstaendig, `diff -u evo1_v2.py evo1.py`)

```diff
--- evo1_v2.py	2026-09-30 05:11:49.491347645 +0200
+++ evo1.py	2026-09-30 06:04:22.258256470 +0200
@@ -14,6 +14,14 @@
 jeder Bewertung. x_schaetz faengt den Nenner null ab (x_est = xs[k], Vermerk "Nullnenner" in zustand.json und
 modell.json); dazu kommt Rauchtest-Teil 0. Schwellen und Entscheidungsregeln sind unveraendert, bei Nenner ungleich null
 rechnet x_schaetz wie Version 1.
+Version 3: 2026-09-30 06:03:20 CEST (date), Reparatur nach A1 (PLAN.md, Abschnitt 12; Lesung LESUNG-REPARATUR-A1.md,
+Auflagen A1 bis A8). Einzige Regelaenderung: Ein inneres grobes Minimum der Polspur zaehlt nur, wenn beide Nachbarn auf
+der Spur auf Stufe A Gamma > G_BODEN = 1e-8 haben. Weggefallene Minima stehen mit Etikett "unter Aufloesung", Grobwert
+und beiden Nachbarwerten in modell.json (Feld grob_minima_unter_aufloesung, nur wenn nicht leer). Bleibt keines, gilt
+F2 = nein mit Grund "kein aufgeloestes Minimum (Nachbarn unter 1e-8)"; ohne jedes innere Minimum bleibt der alte Grund.
+zusammenfassen zaehlt die Modelle mit weggefallenen Minima, Rauchtest-Teil 5 prueft den Filter an synthetischen Spuren.
+Der Zweig "Nullnenner" in x_schaetz ist damit unerreichbar (beide Nachbarn > 0), bleibt aber stehen (Lesung N15).
+Schwellen und alle anderen Regeln sind unveraendert.
 """
 import argparse
 import glob
@@ -37,6 +45,7 @@
 # Schwellen, vor dem ersten Modell festgelegt (PLAN.md, Abschnitt 3)
 F0_W2MIN, F0_PROFILE, F1_WMIN = 0.02, 10, 3
 F2_R2, F2_G0_REL, F2_BC_REL, F2_BC_ABS = 0.99, 1e-3, 0.05, 1e-9
+G_BODEN = 1e-8   # Version 3 (PLAN.md, Abschnitt 12): beide Spur-Nachbarn eines groben Minimums brauchen Gamma_A > G_BODEN
 BOX = {"beta": (0.15, 1.2), "gamma": (0.0, 0.3)}
 RASTER1 = ([0.2, 0.35, 0.5, 0.75, 1.0], [0.0, 0.1, 0.2])
 VERSCHIEDEN = (0.05, 0.02)
@@ -390,10 +399,20 @@
         return sorted(ks)
 
     def grob_minima(self):
-        """innere lokale Minima der groben Breite auf der Polspur, tiefstes zuerst, hoechstens MAX_MIN."""
+        """innere lokale Minima der groben Breite auf der Polspur, tiefstes zuerst, hoechstens MAX_MIN. Version 3: nur
+        Minima, deren beide Nachbarn auf der Spur (Stufe A) Gamma > G_BODEN haben."""
         g, ks = self.z["grob"], self.spur()
         G = [g[str(k)]["Gamma"] for k in ks]
-        return sorted([ks[i] for i in r3.lokale_minima(G)], key=lambda k: g[str(k)]["Gamma"])[:MAX_MIN]
+        return sorted([ks[i] for i in r3.lokale_minima(G) if G[i - 1] > G_BODEN and G[i + 1] > G_BODEN],
+                      key=lambda k: g[str(k)]["Gamma"])[:MAX_MIN]
+
+    def grob_minima_unter_aufloesung(self):
+        """Version 3: innere lokale Minima der Spur, die am Boden scheitern (ein Nachbar oder beide <= G_BODEN)."""
+        g, ks, xs = self.z["grob"], self.spur(), self.z["scan"]
+        G = [g[str(k)]["Gamma"] for k in ks]
+        return [{"k": ks[i], "x_grob": xs[ks[i]], "etikett": "unter Aufloesung", "Gamma_grob": G[i],
+                 "Gamma_nachbarn": [G[i - 1], G[i + 1]]}
+                for i in r3.lokale_minima(G) if not (G[i - 1] > G_BODEN and G[i + 1] > G_BODEN)]
 
     def x_schaetz(self, k):
         """(x_est, hinweis). Version 2: Nenner null (Breiten unter der Aufloesung, nach max(Gamma, 0) alle 0) ->
@@ -632,8 +651,12 @@
         return v
     mins = lauf.grob_minima()
     v["grob_minima"] = [xs[j] for j in mins]
+    weg = lauf.grob_minima_unter_aufloesung()
+    if weg:
+        v["grob_minima_unter_aufloesung"] = weg
     if not mins:
-        v.update(F2="nein", status="fertig", urteil="nicht qualifiziert", grund="kein lokales Minimum der Breite")
+        v.update(F2="nein", status="fertig", urteil="nicht qualifiziert",
+                 grund="kein aufgeloestes Minimum (Nachbarn unter 1e-8)" if weg else "kein lokales Minimum der Breite")
         return v
     if v["F1"] != "ja":
         v.update(F2="grob Minimum, nicht verfeinert", status="fertig", urteil="nicht qualifiziert", grund="F1 (Filter)")
@@ -824,6 +847,8 @@
           f"qualifiziert {len(quali)}, nicht entscheidbar {len(unent)}")
     if diese:
         print(f"A3 (nicht entscheidbar > 20 %): {len(unent) / len(diese):.0%} -> {'Abbruch' if len(unent) > 0.2 * len(diese) else 'weiter'}")
+        weg = [m for m in diese if (m["v"] or {}).get("grob_minima_unter_aufloesung")]
+        print(f"Modelle mit weggefallenen groben Minima (unter Aufloesung, Version 3): {len(weg)} von {len(diese)}")
     if a.gen == 0:
         an = next((m["v"] for m in diese if m["arm"] == "anker"), None) or {}
         ko = next((m["v"] for m in diese if m["arm"] == "kontrolle"), None) or {}
@@ -925,6 +950,34 @@
         e, _ = punkt(0.5, "A", POT_L, 3, dev)
         z.append(f"  Log bei 0,5 Stufe A: Profil ok {e['profil_ok']}, S0 = {e.get('S0')}, Q = {e.get('Q')}, Grund {e.get('grund')}, {e['sek']:.1f} s")
     z.append(f"Ende Teil 1 bis 3 {r3.jetzt()}, {r3.uhr():.1f} s")
+    # 5. Version 3: Boden G_BODEN fuer die Nachbarn grober Minima (PLAN.md, Abschnitt 12; Lesung, Auflage A7)
+    def minima_v2(lz):                                           # grob_minima aus Version 2, wortgleich
+        g, ks = lz.z["grob"], lz.spur()
+        G = [g[str(k)]["Gamma"] for k in ks]
+        return sorted([ks[i] for i in r3.lokale_minima(G)], key=lambda k: g[str(k)]["Gamma"])[:MAX_MIN]
+    pot5, neu_grund = pot_von("P", 0.5, 0.0), "kein aufgeloestes Minimum (Nachbarn unter 1e-8)"
+    spuren = (   # Name, Stufe-A-Breiten der 12 Grobpunkte (alle auf der Spur), Soll verfeinert (k), Soll weggefallen (k), Soll Grund
+        ("Kontrollmuster 1D .69 (Nachbarn 1,039e-8 und -8,51e-10)", faelle["1D .69"], [], [10], neu_grund),
+        ("V-Form, Tiefpunkt 2e-10 auf dem Grobpunkt, Nachbarn 8e-5 und 1,1e-4",
+         [9e-3, 5e-3, 2e-3, 6e-4, 8e-5, 2e-10, 1.1e-4, 5e-4, 1.2e-3, 2.2e-3, 3.5e-3, 5e-3], [5], [], None),
+        ("5 Minima, davon 2 Schein (beide Nachbarn unter 1e-8)",
+         [4e-3, 1e-3, 2.5e-3, 2e-4, 1.5e-3, 5e-5, 3e-4, 9e-9, 2e-9, 6e-9, -9e-10, -5e-10], [5, 3, 1], [8, 10], None),
+        ("monoton fallend, kein Minimum", [1e-2 * 0.3 ** j for j in range(12)], [], [], "kein lokales Minimum der Breite"))
+    for name, G, soll, soll_weg, soll_grund in spuren:
+        zs = {"key": "synthetisch", "pot": pot5, "dim": 3, "w2min": w2_min(pot5), "scan": xs0, "k0": N_SCAN // 2,
+              "grob": {str(j): {"profil_ok": True, "Q": 100.0 - j, "EQ": 0.9, "pol_ok": True, "Gamma": G[j]} for j in range(12)},
+              "fein": {}, "zusatz": {}, "zeiten": {}, "aufrufe": []}
+        lz = Lauf.__new__(Lauf)
+        lz.z = zs
+        alt, neu, weg = minima_v2(lz), lz.grob_minima(), lz.grob_minima_unter_aufloesung()
+        v5 = bewerte(zs)
+        ok = (neu == soll and [w["k"] for w in weg] == soll_weg and v5.get("zu_verfeinern", []) == soll
+              and v5.get("grund") == soll_grund and (v5.get("grob_minima_unter_aufloesung") or []) == weg)
+        z.append(f"5 {name}: Version 2 verfeinert {[round(xs0[k], 5) for k in alt]}, Version 3 {[round(xs0[k], 5) for k in neu]} "
+                 f"(Soll {[round(xs0[k], 5) for k in soll]}); unter Aufloesung {json.dumps(weg)}; bewerte: F2 {v5.get('F2')}, "
+                 f"Urteil {v5.get('urteil')}, Grund {v5.get('grund')}, zu_verfeinern {v5.get('zu_verfeinern')}, "
+                 f"naechstes {v5.get('naechstes')} -> {'ok' if ok else 'FEHLER'}")
+    z.append(f"Ende Teil 5 {r3.jetzt()}, {r3.uhr():.1f} s")
     with open(os.path.join(out, "rauch_bericht.txt"), "w") as fh:
         fh.write("\n".join(z) + "\n")
 
```
