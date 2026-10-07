# ATEM-NETZ-1, Nachtrag 1 zum eingefrorenen Plan (Hinweis der Leitung, frischer Leser SCHREIBTISCH-LESER)

- Geschrieben ab 2026-10-04 18:47:02 CEST (date). Der Plan war seit 18:36:04 eingefroren (EINGEFROREN-SHA256.txt), die
  Hauptlaeufe liefen seit 18:36:27. Am Plan und an den Urteilsregeln wird nichts geaendert. Alles hier ist
  **[Zusatz Leitung], beschreibend**, kein Urteil nach Plan oder Kartenwortlaut.
- Quelle: Nachricht der Leitung, eingegangen waehrend der Hauptlaeufe; Datei des Lesers
  RUNDE-37/schreibtisch-leser/GEGENLESEN.md (Pruefobjekt 3, A4, B13, B14, B21), nur gelesen.
- Hinweis zum Stand meiner Sicht: Zum Zeitpunkt der Nachricht hatte ich die Hauptergebnisse A1 (Paar, Kette, Quadrat)
  und B1 Pyrochlor Saat 1 schon angesehen (nach dem Einfrieren erlaubt). Die Einfrier-Abtastung B2 lief noch.

## Punkt fuer Punkt

1. **Gueltigkeit der Mittelung (A4):** Steht schon vor dem Einfrieren im Plan, Abschn. 2 K1: der Term erster Ordnung
   a_i = mu k (eps/2) z delta ist um 4 z delta/eps groesser als K, hier 4,8 z. Nachgerechnet, gleich mit dem Leser
   (Leser: "mindestens 4z", wegen delta > eps).
2. **Einfrieren ableitbar, AN2 prueft z (A4):** Steht im Plan, Abschn. 2 K1 und K4 (vorab: R = 1,5 fuer alle
   gleichfoermigen Zustaende, 1,55 fuer den geordneten laufenden Pyrochlor-Zustand; "ein Treffer waere die
   Koordinationszahl, kein Frustrationsbefund"). AN2 bleibt wie eingefroren und wird im Ergebnis als **vorab ableitbar**
   gekennzeichnet.
   - **Zusatzvergleich einfach-kubisch (z = 6, zweifaerbbar) gegen Pyrochlor (z = 6)**, neue Datei
     code/nachtrag_kubisch.py (importiert die eingefrorene atem.py, gleiche Einstellungen wie B2: 26 kappa-Werte
     0,01-0,3, Saaten 1 und 2, 200 Takte, W = 50, T = 3,14e-5 je Takt), Gitter 10 x 10 x 10 periodisch, N = 1000,
     Beruehrungsabstand 1 - delta, naechst-naechste Nachbarn bei 1,245 PU (beruehren nie).
   - Vorab [M]: einfach-kubisch und Pyrochlor haben dieselbe gleichfoermige Schwelle (0,0347, gleichphasiger Stillstand
     0,0283). Der geordnete laufende Zustand gibt auf dem kubischen Gitter (Gegentakt) 0,0347, auf Pyrochlor 0,0335.
     Erwartung also R_kub = kappa_50(kubisch)/kappa_50(Pyrochlor) zwischen 1,00 und 1,04.
   - **Lesart, vor dem Lauf festgelegt:** R_kub >= 1,10: "Frustration senkt die Schwelle um mindestens 10 %";
     0,91 < R_kub < 1,10: "kein Frustrationseffekt ueber 10 %"; R_kub <= 0,91: "Frustration hebt die Schwelle".
     Beschreibend, kein AN-Urteil.
3. **Literatur:** Zhang/Fodor bestaetigt (wie Plan Abschn. 1). **Moessner/Chalker:** Der Leser hatte nur das Abstract.
   Ich habe in Abruf 2 den Volltext gelesen (quellen/moessner-chalker-cond-mat-9807384v1.pdf). Dort steht S. 9 woertlich
   "The predicted collinear order for XY spins is confirmed: there is long-range order in P(r)" und S. 8-9 "the only
   cases in which there is order by disorder are q = 4, n = 2 (the XY pyrochlore model) and q = 3, n = 3". Fuer mich
   ist "kollinear bei n = 2" damit [S] (Volltext), nicht [L?]. Eine zweite Person hat diese Stelle nicht gelesen.
4. **Wirbel und Drehsinn messen fast dasselbe (B14):** Richtig, und mein Plan trennt sie nicht. Zusatz [M]:
   - Die Windung w eines Dreiecks ist +-1 genau dann, wenn die drei Phasenzeiger den Nullpunkt umschliessen; dann ist
     w = Vorzeichen von chi.
   - Liegt der Nullpunkt ausserhalb, ist abs(chi) <= 4/(3 sqrt 3) = 0,77. Also folgt aus abs(chi) > 0,77 immer w != 0.
   - Die Zaehlungen "Windung != 0" und "abs(chi) >= 0,9" sind damit geschachtelt (die zweite ist Teilmenge der ersten).
     Im Ergebnis werden sie **als eine Groesse** gefuehrt ("Drehsinn-Wirbel"), nicht als zwei Befunde.
   - Eine Untergitter-gedrehte Definition ist in freien Packungen nicht moeglich (keine Untergitter). Auf dem festen
     Dreiecksgitter (Teil A) waere sie moeglich; sie ist nicht gerechnet.
5. **0, 120, 240 Grad sind eine volle Windung:** Gleich mit Punkt 4; mein Plan zaehlt w so.
6. **Neuheit (B21):** Freie Packungen atmender Punkte mit Phasenkopplung ueber die Abstossung sind das Modell von
   Zhang/Fodor (dort mit zusaetzlicher Synchronisation). Neu sind hier hoechstens: feste Pyrochlor-Lagen (Eisregel-Frage),
   der Einfrier-Vergleich bei gleichem z und die Pump-Messung an Beruehrungsdreiecken. Das wird im Ergebnis so
   eingegrenzt.

## Lauf

- nachtrag_kubisch.py auf der .69 ueber kleintest.sh, Spur cpu7 (nach den laufenden Hauptlaeufen der Spur oder
  dazwischen, je nachdem, wer die Sperre zuerst bekommt), Ausgabe lauf/N1_kubisch.json. Ergebnis im ERGEBNIS.md unter
  "Nachtrag 1".

## Aenderung vor dem Start (2026-10-04 18:49:24 CEST, date)

- Nach dem Schreiben von Punkt 2 habe ich die Hauptergebnisse B2 Pyrochlor angesehen: Der Stillstand springt dort
  zwischen zwei Rasterpunkten von 0 auf 100 % (kappa 0,0297 -> 0,0340). Das B2-Raster hat 14,6 % Schrittweite; der
  erwartete Frustrationseffekt ist 3,5 %. Eine Lesart mit 10-%-Grenzen auf diesem Raster wuerde nur die Rasterlage
  messen.
- Deshalb habe ich nachtrag_kubisch.py **vor seinem Start** abgebrochen (wartete auf die Sperre der Spur cpu7; per PID
  beendet, keine Rechnung gelaufen, Log umbenannt in lauf/N1_kubisch_abgebrochen.log) und durch
  **code/nachtrag_fein.py** ersetzt: Pyrochlor und einfach-kubisch mit 19 kappa-Werten 0,0280-0,0400 (Schritt 2,0 %),
  Diamant mit 22 Werten 0,0400-0,0620 (Schritt 2,1 %), Saat 1, sonst wie B2 (200 Takte, W = 50, T = 3,14e-5).
  Ausgabe lauf/N1_fein.json. Schwelle als Klammer (letzter Wert unter 50 %, erster ueber 50 %) und interpoliert.
- **Lesart, vor dem Lauf festgelegt (beschreibend):** R_kub = kappa_50(kubisch)/kappa_50(Pyrochlor):
  >= 1,10 "Frustration senkt die Schwelle um >= 10 %"; 1,02-1,10 "kleiner Frustrationseffekt (2-10 %)";
  0,98-1,02 "kein messbarer Effekt"; < 0,98 "Frustration hebt die Schwelle". Dazu R_dia_pyro und R_dia_kub (vorab [M]:
  1,50-1,55 bzw. 1,50).
- Auch AN2 selbst (B2-Raster, eingefroren) wird im Ergebnis mit dieser Rastergrenze gemeldet: Auf einem Raster mit 14,6 %
  Schritt kann R nur Potenzen von 1,146 annehmen, wenn beide Gitter ganz springen.
