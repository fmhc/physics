# Runde 21, bio28-weiter: Ergebnis

Code-Agent (Opus 5.5) fuer claude-primary. Karte KARTE.md, Plan PLAN.md.eingefroren-20261002-182221 (eingefroren
18:22:21 CEST, vor jedem Lauf). Hauptlauf auf der .69, Spur p4000b (Quadro P4000, wie Runde 5), 16:23:51 bis
16:26:50 UTC (18:23:51 bis 18:26:50 CEST), rc 0. Bericht begonnen 18:30:12 CEST (date). Explorativ (v3), [H].

## 1. Ergebnis

1. **K0 bestanden (Y0 eingetroffen).** Alle zehn Zeilen aus Runde 5 sind exakt reproduziert: Verschmelzen bei 5
   und Teilung bei 10 bzw. 15 (5er-Raster), Endzahl 0, Ladungsverlust 0,81 bis 0,99. Die 5er-Gebietslisten sind in 9 von 10 Laeufen
   in allen ausgegebenen Stellen gleich. In fein w60_nachbarn2 sind nur bei t = 0 die zwei gleich grossen Nachbarn
   in der Reihenfolge vertauscht.
2. **Y1 eingetroffen (grob und fein, alle vier).** Die Gebietszahl faellt schon bei t = 1,5 bis 2,0 auf 1. Sie
   bleibt 5,0 bis 11,5 Zeiteinheiten ohne Unterbrechung bei 1 (11 bis 24 Proben). Danach teilt sich das eine Gebiet
   bei t = 7,0 bis 14,0. Y1 im Wortlaut war vor dem Lauf ableitbar (PLAN Abschnitt 1).
3. **Y2 eingetroffen nach Wortlaut, Y3 nicht eingetroffen.** Die Endzahl ist in allen vier Laeufen 0. Das eine
   Gebiet traegt bis zur letzten Probe vor der Teilung die Windung 1, mit S_min_kreis 0,006 bis 0,08. Die Windung
   verschwindet erst mit der Teilung: Ab t = 15 haben alle Bruchstuecke die Windung 0.
4. **Bedeutung nach Karte (Y1 und Y2):** Es gibt keine Groessengrenze mit Teilung, sondern eine Instabilitaet nach
   dem Verschmelzen. Bio 28 wird verworfen. Der Befund "gemischter Ball zerfaellt" wird als [H] notiert.
5. **Zwei Vorbehalte (Beobachtungen, keine Kriterien; Frage an die Leitung):**
   - (a) Das eine Gebiet ist weit ausgedehnt: r_mittel 4,7 bis 8,4. Ein runder Ball derselben Flaeche haette grob
     4,4 bis 6,0 [S, Ring-r_mittel mit der Wurzel des Flaechenverhaeltnisses skaliert]. Am deutlichsten ist das bei
     zwei Nachbarn (w60: 8,3 gegen etwa 6,0), kaum bei w75 mit einem Nachbarn (4,7 bis 4,9 gegen etwa 4,4). Die
     Bruchstuecke entstehen auf der alten Verbindungsachse zwischen Zentrum und alten Nachbarplaetzen. Ob die Baelle
     verschmolzen sind oder nur als verbundene Lappen zusammenhaengen, kann die Maske nicht trennen.
   - (b) Nach den 5er-Listen entsteht die Endzahl 0 in der Randschicht, nicht durch Zerstreuen im Inneren. Nach der
     Teilung behalten die Bruchstuecke etwa 110 bis 175 Zeiteinheiten lang fast ihre ganze Ladung und wandern nach
     aussen. Ladung verlieren sie erst, wenn ihr Schwerpunkt bei einer Koordinate von etwa 27 bis 29 liegt
     (Randschicht ab 30,4). Ob Y2 hier "ueberleben nicht als Baelle" misst, ist offen. Diese Spaetzeit-Auswertung
     stand nicht im Plan, sie ist nachtraeglich.

## 2. K0 im Detail

Vergleich gegen RUNDE-05/r5-2d-a/lauf-69/ausgabe/groesse_ergebnis.json (Kopie hilfs/r5_groesse_ergebnis.json).
Toleranz 10 % relativ, n_ende gleich, None nur gegen None.

| Stufe Lauf | t verschmolzen r5 / r21 | t Teilung r5 / r21 | n Ende r5 / r21 | Q-Verlust r5 / r21 | 5er-Gebiete gleich |
|---|---|---|---|---|---|
| grob w60_nachbarn0 | None / None | None / None | 1 / 1 | 4,07514e-9 / 4,07514e-9 | ja |
| grob w60_nachbarn1 | 5 / 5 | 15 / 15 | 0 / 0 | 0,937254 / 0,937254 | ja |
| grob w60_nachbarn2 | 5 / 5 | 10 / 10 | 0 / 0 | 0,814786 / 0,814786 | ja |
| grob w75_nachbarn0 | None / None | 255 / 255 | 0 / 0 | 0,966124 / 0,966124 | ja |
| grob w75_nachbarn1 | 5 / 5 | 15 / 15 | 0 / 0 | 0,990496 / 0,990496 | ja |
| grob w75_nachbarn2 | 5 / 5 | 10 / 10 | 0 / 0 | 0,966185 / 0,966185 | ja |
| fein w60_nachbarn1 | 5 / 5 | 15 / 15 | 0 / 0 | 0,937229 / 0,937229 | ja |
| fein w60_nachbarn2 | 5 / 5 | 10 / 10 | 0 / 0 | 0,814778 / 0,814778 | nein (nur Reihenfolge bei t = 0) |
| fein w75_nachbarn1 | 5 / 5 | 15 / 15 | 0 / 0 | 0,990487 / 0,990487 | ja |
| fein w75_nachbarn2 | 5 / 5 | 10 / 10 | 0 / 0 | 0,966079 / 0,966079 | ja |

- "5er-Gebiete gleich" heisst: Die gerundete Liste aus verlauf_kurz stimmt fuer alle 121 Analysen ueberein. Diese
  Spalte ist kein Kriterium.
- Abweichung in fein w60_nachbarn2: Nur der Eintrag bei t = 0 unterscheidet sich. Dort sind die beiden Nachbarn mit
  gleichem Q 48,1519 bei x = +-12,663 vertauscht. Die anderen 120 Eintraege sind gleich.
- Der Messtakt 0,5 statt 1 hat die Entwicklung also nicht veraendert, wie erwartet.

## 3. Zeitreihe je Lauf (Kurzform)

Grob. Fein gibt dieselben Ein-Gebiet-Zeiten und Q-Werte innerhalb 0,9 % (Abschnitt 5, L3). Q ist die Ladung im
Gebiet, w die Windung, (X, Y) der Schwerpunkt und d12 der Abstand der zwei groessten Gebiete. "Verschmelzen" ist die
erste Probe mit n = 1, "Teilung" die erste Probe danach mit n >= 2. Die Maske fasst bei t = 0 in den gefuetterten
Laeufen nur 65 bis 70 % von Q_box (Schwanz unter der Schwelle). Das eine Gebiet hat denselben Anteil (0,66 bis 0,74), und Q_box bleibt bis
t = 30 konstant.

| Lauf | Start t = 0 | Verschmelzen | eine Phase bis | Teilung | t = 30 | danach bis t = 600 |
|---|---|---|---|---|---|---|
| w60_nachbarn1 | n 2: 100,4 w1 (0,17; 0) + 48,1 w0 (12,66; 0); d12 12,49 (1,5: 12,20) | t 2,0: Q 153,7 w1 (4,41; 0,01), r_mittel 6,22, Smin 0,018 | 13,5: Q 148,8 w1, r_mittel 5,82, Smin 0,006 | t 14,0: 92,0 w0 (8,58; 0,71) + 56,7 w1 (Smin 0,005) (-1,80; -1,28); d12 10,57; ab 15,0 beide w0 | n 2: 97,9 w0 (7,53; 2,84) + 55,3 w0 (-0,86; -4,28); d12 11,00 | beide wandern nach aussen bei fast fester Ladung (t 100: 89,9 und 54,3); Verlust ab Koordinate etwa 28; erstes n 0 bei 245 |
| w60_nachbarn2 | n 3: 104,0 w1 (0; 0) + 2 x 48,1 w0 (+-12,66; 0); d12 12,66 | t 2,0: Q 210,6 w1 (0; 0), r_mittel 8,27, Smin 0,028 | 8,5: Q 202,5 w1, r_mittel 8,40, Smin 0,013 | t 9,0: 2 x 100,45 w0 bei +-(7,42; 1,02); d12 14,98 | n 2: 2 x 103,7 w0 bei +-(6,43; 3,39); d12 14,54 | 2 x 97 bis 103 bis t 180 (Koordinate 26,6), dann Verlust in der Randschicht; erstes n 0 bei 320 |
| w75_nachbarn1 | n 2: 46,4 w1 (0,32; 0) + 13,4 w0 (10,34; 0); d12 10,03 (1,0: 9,73) | t 1,5: Q 62,8 w1 (2,98; 0,03), r_mittel 4,90, Smin 0,065 | 12,0: Q 62,3 w1, r_mittel 4,65, Smin 0,011 | t 12,5: 36,1 w0 (6,60; 1,07) + 25,1 w1 (Smin 0,0006) (-1,36; -1,53); d12 8,38; ab 13,0 beide w0 | n 2: 36,7 w0 + 23,8 w0; d12 11,77 | 35,7 und 23,7 bis t 100; Verlust ab Koordinate etwa 29; erstes n 0 bei 175 |
| w75_nachbarn2 | n 3: 49,6 w1 (0; 0) + 2 x 13,3 w0 (+-10,36; 0); d12 10,36 | t 1,5: Q 82,7 w1 (0; 0), r_mittel 6,28, Smin 0,094 | 6,5: Q 84,6 w1, r_mittel 6,36, Smin 0,077 | t 7,0: 2 x 41,3 w0 bei +-(5,52; 1,05); d12 11,24; von 13,5 bis 19,5 n 4 (2 x 36,5 + 2 x 7,2, alle w0), ab 20,0 wieder n 2 | n 2: 2 x 44,3 w0; d12 13,22 | 2 x 37 bis 38 bis t 170 (Koordinate 27,1), dann Verlust; erstes n 0 bei 225 (fein 230) |
| w60_nachbarn0 (Kontrolle) | n 1: 115,47 w1, Smin 0,853 | - | - | - | n 1: 115,47 w1, Smin 0,853 | bleibt ganz bis 600 |
| w75_nachbarn0 (Kontrolle) | n 1: 53,50 w1, Smin 0,443 | - | - | - | n 1: 53,51 w1, Smin 0,444 | Teilung 255, erstes n 0 bei 385 (Runde-5-Regel) |

- Beobachtung [H]: Bei zwei Nachbarn traegt jedes Bruchstueck etwa einen Nachbarn plus einen halben Ring
  (w60: 48,1 + 104,0/2 = 100,2 gegen 100,45). Bei einem Nachbarn waechst das Stueck auf der Nachbarseite
  (48,1 auf 92,0 bzw. 13,4 auf 36,1), das Stueck auf der Ringseite schrumpft (100,4 auf 56,7 bzw. 46,4 auf 25,1).
- Nach der Teilung entfernen sich die Bruchstuecke vom Zentrum, jeweils gegenlaeufig zueinander, vor allem in
  y-Richtung. Der Drehimpuls steckt dann in dieser Bahnbewegung, nicht mehr in einer Windung [H].

## 4. Y0 bis Y3

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| Y0 | K0 bestanden | 85 % | eingetroffen | 10 von 10 Zeilen, alle Groessen gleich (Abschnitt 2) |
| Y1 | In allen vier gefuetterten Laeufen faellt die Gebietszahl vor der "Teilung" auf 1 | 60 % | eingetroffen (grob und fein) | Ein-Gebiet-Proben vor t_T: w60n1 2,0 bis 13,5 (24, t_T 15); w60n2 2,0 bis 8,5 (14, t_T 10); w75n1 1,5 bis 12,0 (22, t_T 15); w75n2 1,5 bis 6,5 (11, t_T 10); jeweils lueckenlos. Q_box dabei 100 % von Q_box(0). Vorab ableitbar (PLAN 1) |
| Y2 | Bruchstuecke ueberleben nicht als Baelle: Endzahl 0 | 70 % | eingetroffen nach Wortlaut (grob und fein) | n_ende 0 in allen vier; erstes n 0 bei 245 / 320 / 175 / 225 (fein 245 / 320 / 175 / 230). Vorbehalt 1(5b): Verlust in der Randschicht |
| Y3 | Der verschmolzene Ball verliert die Windung vor dem Zerfall | 55 % | nicht eingetroffen (grob und fein) | Windung bei t_1,letzt = 1 in allen vier (S_min_kreis 0,0064 / 0,0134 / 0,0106 / 0,0768); an keiner Ein-Gebiet-Probe Windung 0. Bei einem Nachbarn traegt das Ring-Bruchstueck danach noch kurz w1 (w60: 14,0 und 14,5; w75: 12,5; S_min_kreis 0,0006 bis 0,005), ab 15,0 bzw. 13,0 w0. Bei zwei Nachbarn haben beide Bruchstuecke sofort w0 |

- Zusammenfassung nach PLAN 4.5: grob und fein gleich, also gelten die Ausgaenge wie oben. Bedeutung siehe 1.4.

## 5. Latten (v3)

- **L1 (kann scheitern): teilweise.** Y1 war vorab ableitbar und konnte nur ueber K0 scheitern. Y2 war schon in
  Runde 5 gemessen. Y3 konnte scheitern und ist gescheitert.
- **L2 (Gegenprobe): ja.** Ohne Nachbarn bleibt der m = 1-Ball von 0 bis 30 ganz (n 1, Windung 1, Q fest,
  S_min_kreis 0,85 bzw. 0,44). Verschmelzen und Teilung kommen also von den Nachbarn. Die Kontrolle w75 zerfaellt
  aber auch ohne Futter (Teilung 255).
- **L3 (Numerik): bestanden.**
  - grob und fein: gleiche Ausgaenge Y0 bis Y3 und identische Ein-Gebiet-Zeiten
  - Q der Bruchstuecke innerhalb 0,9 % (z. B. 56,69 gegen 56,40)
  - erstes n 0 gleich, bis auf w75n2 (225 gegen 230)
- **L4 (schon bekannt): weitgehend.** Drehende Solitonen zerfallen in Stuecke ohne Windung, und die Windung wird zu
  Bahndrehimpuls. Das war schon in Runde 5 als bekannte Wirbelzerfallsphysik eingeordnet (PLAN 10) [L, nicht
  nachgelesen].
- **L5 (Messbezug): nein.**

## 6. Grenzen, Selbstanzeigen, Laufzeiten, sha256

- **Selbstanzeigen:**
  - Vor dem Plan habe ich die 5er-Gebietsliste von grob w60_nachbarn1 fuer t = 0 bis 25 gesehen (PLAN 0).
  - Y1 im Wortlaut war ableitbar (PLAN 1).
  - Die Spaetzeit-Auswertung (Lage und Ladung der Bruchstuecke nach t = 30, Vorbehalt 5b) stand nicht im Plan. Ich
    habe sie nach dem Lauf aus den 5er-Listen gelesen. Sie aendert keinen Ausgang.
  - py_compile hat auf der .69 einen Ordner __pycache__ in meinem Ordner angelegt.
- **Grenzen:**
  - Die Maske (Schwelle 0,5 des Anfangsmaximums) zaehlt verbundene Lappen als ein Gebiet (Vorbehalt 5a).
  - Die Windung auf dem Kreis ist im einen Gebiet unsicher: S_min_kreis 0,005 bis 0,09 gegen 0,44 bis 0,85 beim
    Einzelball. Der Kreis laeuft dort durch duenne Bereiche.
  - Die Box hat eine absorbierende Randschicht. "Endzahl 0" misst hier das Verlassen des Fensters (Vorbehalt 5b).
  - Die Abstaende sind ohne periodisches Bild gerechnet. Im Fenster 0 bis 30 liegen alle Gebiete bei |X|, |Y| <= 12,7,
    weit weg vom Rand.
  - 2D, ein Feld, Futter statt Bad (wie Runde 5).
- **Abweichungen** (alle vor dem Lauf, PLAN 2): Messtakt 0,5, eigene Messfunktion (Kopie von lauf_standard.messen),
  Index 10 je 5er-Analyse, eigene Ausgabe. r5_2d_a.py ist unveraendert.
- **Laufzeiten (.69, kleintest.sh, p4000b, Lock ohne Wartezeit):**
  - Rauchlauf (nur grob, t_end 1, mit Selbsttest der Auswertung, "ok": true): 16:22:26 bis 16:23:34 UTC, 1 min 8 s.
    Davon Schiessen 63,9 s.
  - Hauptlauf: 16:23:51 bis 16:26:50 UTC, 2 min 59 s. Schiessen 63,2 s; grob 32,5 s (davon 175 Analysen 7,8 s);
    fein 80,2 s (davon 175 Analysen 6,7 s).
- **sha256:**
  - r5_2d_a.py 4b7a00b22e427ab9889056057437fc2199ca0fe6fff0ccf4847c11f62892bc7b (lokal und .69 gleich)
  - bio28_weiter.py 13b61b3f5ec3f3503ecdf5fb05f3ab9bcfe7dfd4736a8d540becf67898df3f4a (lokal und .69 gleich)
  - hilfs/r5_groesse_ergebnis.json a708b364f41c61ed7aafd195161be11abbba30c0157abf49ea377c6062a8ecb0 (gleich dem
    Runde-5-Original)
  - PLAN.md.eingefroren-20261002-182221 c805f427d78a6c42131d7b6b034d4bccfaa8dddb64677c35670aa25e12d3f56e
  - lauf-69/ausgabe/bio28_weiter_roh.json e49e080731d48804d197f8da84925ad8b09c1c7702ee903ef7631378094995dc
  - lauf-69/ausgabe/bio28_weiter_ergebnis.json a91dd02a338e932a8fcb206fc8100f4b1c1d18e6644b65e12baa8a7713249456
  - lauf-69/ausgabe/bio28_weiter_bericht.txt 07be39b33d5ae9b4b1046eb66a9fbc948a574121b1fc645b2d0192806fe79fe2
- **Dateien:**
  - bio28_weiter.py
  - PLAN.md und PLAN.md.eingefroren-20261002-182221
  - lauf-69/HAUPT.log, lauf-69/RAUCH.log
  - lauf-69/ausgabe/ (Hauptlauf), lauf-69/rauch/ (Rauchlauf, Zahlen ungueltig)
  - hilfs/r5_groesse_ergebnis.json
  - Auf der .69: /home/fmh/fmhc-physics-remote/runde21-bio28-weiter/

## 7. Einfach gesagt

Wir haben den Versuch aus Runde 5 genau wiederholt und dabei in der ersten halben Minute zehnmal so oft
hingeschaut. Die Zahlen von damals kamen exakt wieder heraus. Die Nachbarbaelle kleben schon nach etwa 2 Zeiteinheiten
mit dem drehenden Ball zu einem Klumpen zusammen. Dieser Klumpen haelt 5 bis 11 Zeiteinheiten und reisst dann in zwei
Stuecke ohne Drehwirbel. Die Stuecke fliegen langsam auseinander. Dass am Ende keine Baelle mehr da sind, liegt
daran, dass sie den Rand der Box erreichen und dort geschluckt werden, nicht daran, dass sie zerfliessen. Nach den
Regeln der Karte ist Bio 28 damit verworfen. Ob die Stuecke ausserhalb unserer Box weiterleben wuerden, bleibt offen.

Ende der Bearbeitung: 2026-10-02 18:34:06 CEST (date). Beginn 2026-10-02 18:10:59 CEST.
