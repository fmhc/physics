# WEYL-LINEAR-2: Plan (Runde 42, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Arbeitsplatz RUNDE-37/weyl-linear-2/, Rechenort .69
  (/home/fmh/fmhc-physics-remote/weyl-linear-2/), Spur cpu10.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 18:59:51 CEST, Zeitbox 75 min.
  - Gelesen bis 19:03 CEST: Karte, WL1 (ERGEBNIS, PLAN, KARTE, code/, Laufzeiten aus lauf-69/L*.log), kleintest.sh.
  - Budgetlauf 17:03:45 bis 17:06:13 UTC (Abschnitt 0).
  - **Laufkette gestartet 17:09:49 UTC, also vor diesem Plan** (Abschnitt 1, Punkt 3).
  - Dieser Plan ab 2026-10-04 19:15:15 CEST, vor jeder Sicht auf neue lambda1-Werte.
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [E] gerechnet, [P] Projektdatei, [S] Quelle, [H] Hypothese,
  [F] Festlegung dieses Plans.
- Alles ist synthetische Netzrechnung. Keine Messdaten, keine Messdatenbestaetigung.

## 0. Budget (vorab gemessen)

- **N = 128 000** (Saat 1, eine Welle k = 0,15 laengs x; dieses k gehoert zu keinem Fenster, der Wert wird nicht
  ausgewertet) [E]:
  - Netzbau 22,8 s, RSS 1562 MB.
  - KPM 113,0 s je Wellenpaar (beide Aeste in einem Block, M = 2048).
  - Lauf gesamt 147,4 s (Service runtime 2 min 28 s); also etwa 125 s je Wellenpaar.
- **N = 32 000** (WL1-Logs) [P]: KPM 20 s je Wellenpaar, 284 s je Netz mit 12 Wellenpaaren.
- **Antwort auf die Budgetfrage: Bei N = 128 000 passt in einen 10-min-Lauf kein einziges vollstaendiges Netz** im
  WL1-Zuschnitt (12 Wellenpaare, etwa 1520 s = 25 min). Ein Lauf traegt hoechstens 4 Wellenpaare (etwa 520 s, zu knapp an
  600 s); ich nehme 2 Wellenpaare je Lauf (etwa 275 s).
- Das Kartenprogramm (12 neue Netze bei 32 000 und 4 Netze bei 128 000, je 12 Wellenpaare) braucht etwa 2,6 h auf
  einer Spur. Zeitbox 75 min, eine Spur: nicht machbar. Daher die Abweichungen in Abschnitt 1.

## 1. Abweichungen von der Karte (begruendet, vor dem Einfrieren)

1. **N = 128 000:** 4 Netze (Saaten 1 bis 4), je **eine** Richtung (x, y, z, x) statt drei, k = 0,06; 0,12; 0,18; 0,24.
   Zwei Laeufe je Netz (k-Paare). Damit gilt "mindestens 4 Netze", aber je Netz nur eine Richtung.
2. **N = 32 000:** statt 16 Netzen die 4 alten (WL1, drei Richtungen, k bis 0,24) und **bis zu 7 neue** (Saaten 5 bis 11,
   je eine Richtung, k = 0,06 bis 0,36 in Schritten von 0,06). Wie viele neue fertig werden, entscheidet allein die
   Schlusszeit (Punkt 5). Die neuen Netze reichen bis k = 0,36, damit es das groessere Probefenster gibt (WL1-Selbstanzeige
   13).
3. **Laufkette vor dem Plan gestartet** (17:09:49 UTC): Die Netzrechnung ist der unveraenderte WL1-Code
   (weyllinear.py 5bca0d80, spinnetz.py 460c0af6); Saaten, Richtungen und k stehen fest in code/kette.sh. Ich sehe vor der
   Endauswertung nur kette.log (Rueckgabecodes, Zeiten) und die Laufzeilen ohne Gewichte. Grund: Zeitbox.
4. **N = 2000 und 8000:** nur die WL1-Netze (Kopien, gleiche Pruefsummen), keine neuen.
5. **Schlusszeit:** Nach 17:58:00 UTC startet kein Lauf mehr. Ausgewertet wird jedes Netz, das die Soll-k eines Fensters
   vollstaendig hat. Keine Auswahl nach Werten, keine nachgelegten Saaten.
6. **WM0** nutzt die alten WL1-Dateien der Saaten 1 bis 4 (nicht neu gerechnet). Dazu die Kontrolle KR: eine Welle von
   Saat 1 (N = 32 000, k = 0,06 laengs x) neu gerechnet, Vergleich mit der WL1-Datei.

## 2. Fits, Fenster, Einheiten [F]

- **Ansatz A:** v - 1 = l1 k + l2 k^2. **Ansatz B:** v - 1 = l1 k + l2 k^2 + l3 k^3 + l4 k^4. Achsenabschnitt 1,
  ungewichtet, kleinste Quadrate, je Ast (plus: E > 0, minus: |E| des Asts E < 0).
- **Fenster:**
  - W0 (Haupt): k <= 0,24, also k = 0,06; 0,12; 0,18; 0,24. A und B.
  - Wk (kleiner, beschreibend): k <= 0,18. Nur A; B hat 4 Parameter und nur 3 k.
  - Wg (groesser, beschreibend): k <= 0,36 (6 k). Nur die neuen Netze bei N = 32 000.
  - Eine Einheit geht nur ein, wenn jede ihrer Richtungen alle Soll-k des Fensters hat.
- **Einheiten:** "netz" = alle Richtungen eines Netzes in einem Fit (wie WL1); "richtung" = Netz x Richtung.
- **Gleichteil** lambda_S = (l1+ + l1-)/2, **Gegenteil** lambda_A = (l1+ - l1-)/2.
- **Statistik** je N, Fenster, Ansatz, Einheit: Mittel, SD, SE = SD/sqrt(n); **Bootstrap ueber Netze** (B = 4000; die
  Einheiten eines Netzes bleiben zusammen). Zeilen mit a_fest_ok ungleich True fallen heraus (gezaehlt).
- **N-Exponent:** Gerade durch log SD gegen log N; Intervall per Bootstrap ueber Netze je N (B = 2000, beschreibend).
- **Gepoolt (beschreibend):** lambda_S in W0 ueber alle N, invers-varianzgewichtet mit SE_boot.

## 3. Urteilsregeln (mechanisch in code/auswertung2.py)

| Nr | Nach Plan [F] | Nach Kartenwortlaut (Lesarten) |
|---|---|---|
| WM0 | Alte Netze (Saaten 1 bis 4) bei N = 32 000, A, W0, Einheit netz: abs(Mittel lambda_S - 0,0010) <= 1e-4 **und** abs(Mittel lambda_A) < 2 SE_boot | dasselbe mit sigma = SE_boot und sigma = SD/sqrt(n) |
| WM1 | N = 128 000, B, W0, Einheit netz (hier eine Richtung je Netz): abs(Mittel lambda_S) < 2 SE_boot; mindestens 3 Netze, sonst nicht auswertbar | sigma in {SE_boot, SD/sqrt(n)} x Einheit in {netz, richtung} |
| WM2 | SD von l1 je Ast ueber Einheiten "richtung", A, W0, bei N = 2000, 8000, 32 000, 128 000; p(E > 0) und p(E < 0) beide in [-0,65; -0,35]; alle vier N noetig | Ansatz in {A, B} x Einheit in {netz, richtung} x Ast in {E > 0, E < 0}: 8 Lesarten |

- Kartenwortlaut: eingetroffen nur, wenn alle Lesarten eintreffen; nicht eingetroffen, wenn keine; sonst
  "uneindeutig (x von y)".
- **Warum "richtung" fuer WM2 nach Plan:** Bei 128 000 hat jedes Netz eine Richtung, die alten Netze mitteln drei. Nur
  die Einheit Netz x Richtung ist ueber alle N gleich gebaut. Die Lesart "netz" mischt bei 32 000 und 128 000 Netze mit
  einer und drei Richtungen; sie zieht p nach oben (flacher), weil Einrichtungs-Netze staerker streuen.

## 4. Schreibtisch (vor jeder Sicht) [M, Kopfrechnung; der Code rechnet die Koeffizienten im Teil "leck" nach]

- **Leck eines k^4-Glieds in l1 von Ansatz A:** W0 -0,0100 x l4; Wk -0,0044 x l4; Wg -0,032 x l4. Ist der Gleichteil
  +0,0010 ein Leck, dann l4_S etwa -0,1, und der A-Gleichteil waere etwa +0,0004 (Wk), +0,0010 (W0), +0,0032 (Wg). Ein
  echtes lineares Glied waere vom Fenster unabhaengig.
- Nach D4 (WL1, ungeprueft, von den Daten nicht gestuetzt) hat der Gleichteil von v nur gerade Potenzen; dann
  l1_S = l3_S = 0.
- **Rauschverstaerkung B gegen A** in W0 (4 k, gleiches Rauschen je Punkt): SD(l1_A) = 0,756 sigma_v/h,
  SD(l1_B) = 5,18 sigma_v/h (h = 0,06), Faktor etwa 6,9. In W0 ist B je Richtung exakt bestimmt (4 Parameter, 4 k).
- **Trennschaerfe von WM1 [M, grob]:** Streuung je Netz von lambda_S unter A bei 32 000 (WL1, drei Richtungen) 0,0013.
  Fuer eine Richtung und N = 128 000 etwa 0,001 (wenn N^(-1/2) gilt und die Richtungen unabhaengig sind). Unter B
  etwa 7-mal mehr, also etwa 0,007 je Netz; mit 4 Netzen SE etwa 0,0035.
  - Ein echter Gleichteil von +0,001 laege unter B bei etwa 0,3 sigma. **WM1 traefe also auch dann ein, wenn der
    Gleichteil echt waere.** Ein Eintreffen traegt die vorab festgelegte Bedeutung der Karte ("kein lineares Glied")
    deshalb nicht. Nur ein Verfehlen (abs(lambda_S,B) ueber etwa 0,007) waere aussagekraeftig.
  - Trennschaerfer sind die Fensterprobe (G1) und der gepoolte Wert; beide sind beschreibend bzw. Agenten-Vorhersage.
- **WM0** ist eine Kontrolle der Auswertekette: gleiche Daten, gleicher Fit wie WL1. Erwartet ist Gleichheit bis auf
  Rundung, also vorab ableitbar.
- **Gepoolter A-Gleichteil:** Die Altdaten allein geben etwa +0,0011 +- 0,0005 (2,3 sigma, Kopfrechnung aus den
  WL1-Tabellenwerten). Er ist teilweise vorab bekannt; deshalb **G2 nur beschreibend**, ohne Wahrscheinlichkeit.

## 5. Agenten-Vorhersage (vor jeder Sicht auf neue lambda1-Werte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| G1 | [H] N = 32 000, neue Netze: Der A-Gleichteil waechst von W0 nach Wg (Differenz je Netz Wg - W0, Mittel > 2 SE_boot) | 45 % |
| G2 | nur beschreibend: gepoolter A-Gleichteil in W0 > 2 SE | - |

## 6. Laufliste (code/kette.sh, einmalig gestartet 17:09:49 UTC)

- Rauch (winzige Netze, nur Struktur): R0 N = 400, Saaten 1 bis 3, x, k bis 0,36; R1 N = 800, Saaten 1 bis 3, y, k bis
  0,24.
- KR: N = 32 000, Saat 1, x, k = 0,06 (kontrolle/repro-32000-s1-x-k006.json).
- P01 N = 32 000, Saaten 5 und 8, x, k bis 0,36. P02 bis P09 N = 128 000, Saaten 1 (x), 2 (y), 3 (z), 4 (x), je zwei
  Laeufe (k = 0,06 und 0,12; k = 0,18 und 0,24). P10 bis P14 N = 32 000, Saaten 6 (y), 7 (z), 9 (y), 10 (z), 11 (x), k bis
  0,36, soweit vor der Schlusszeit gestartet.
- Alle Laeufe: M = 2048, feste Skala a = 4 (sigma_E = 0,0061), 1 Thread, <= 600 s, Logs mit absolutem Pfad in lauf/.
- Rauchtest der Auswertung (R2) auf den Rauchnetzen und den WL1-Altdaten: 17:15:12 bis 17:17:25 UTC, rc = 0, 75 s.
  Angesehen nur Schluessel, Einheitenzahlen je Fenster, die Leck- und Verstaerkungs-Koeffizienten (Designgroessen aus
  den k-Listen, keine Daten: W0 -0,01003, Wk -0,00437, Wg -0,0321 je l4; Verstaerkung B/A 6,86 in W0, 5,45 in Wg) und
  KR (bestanden, Abweichung 0 in beiden Aesten). Keine lambda1-Werte, kein Bild angesehen.

## 7. Kontrollen

- KR: abs(Delta v) <= 1e-12 in beiden Aesten gegen zweig-32000-1.json (WL1).
- Gueltigkeit: a_fest_ok in allen Zeilen, kleinstes Fenstergewicht, abs(mu) <= 1, Euler 0.
- Gittertest nicht wiederholt: Netz- und Operatorcode sind bytegleich mit WL1 (Pruefsummen oben), dort bestanden.

## 8. Einfrieren

- PLAN.md, code/auswertung2.py, code/weyllinear.py, code/spinnetz.py und code/kette.sh als Kopien
  *.eingefroren-<Zeit>, Pruefsummen in EINGEFROREN-SHA256.txt (lokal und auf der .69).
- Danach bis zur Endauswertung keine Rohwerte. Bewertet wird nach Plan und nach Kartenwortlaut, getrennt.
