# ATEM-NETZ-1: Ergebnis (Runde 42, Code-Agent fuer Leitung claude-primary)

- Geschrieben ab 2026-10-04 19:09:35 CEST (date). Agent-Start 18:01:21, Plan ab 18:23:36, Rauchlauf 1 18:21:38-18:29:33,
  Rauchlauf 2 18:33:20-18:35:48, eingefroren 18:36:04, Hauptlaeufe 18:36:27-19:22:52, Nachtrag-1-Lauf 18:52:23-18:57:50,
  Auswertung 19:22:56-19:23:00 (Zeiten aus date bzw. Starter-Log, .69-Zeiten UTC + 2 h).
- Alle Rechnungen auf der .69 ueber kleintest.sh (cpu6, cpu7), je Lauf <= 438 s, <= 73 MB, 1 Thread. Dateien: PLAN.md
  (+ eingefrorene Kopie), EINGEFROREN-SHA256.txt, NACHTRAG-1.md, code/, rauch-69/, lauf-69/ (auswertung.json, drei PNG,
  PRUEFSUMMEN.txt), quellen/.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Gedaechtnis, [S] an der Quelle gelesen, [H] Hypothese.
  Einheiten: Laenge PU (Ruhedurchmesser 1), Zeit Takte. Kopplung kappa = mu k eps^2/(8 omega); eps = 0,1, delta = 0,12,
  schwach kappa = 0,005, Rauschen T = 1e-3 K (Plan Abschn. 3).

## 1. Ergebnis zuerst

1. **Der Schreibtisch haelt, mit einer Ergaenzung.** Die Huelle koppelt gemittelt wie ein XY-Antiferromagnet: Paar, Kette,
   Quadrat und Diamant enden im Gegentakt, Dreiecke im 120-Grad-Muster [E]. Volle und gemittelte Dynamik stimmen auf
   1-2 % ueberein (Paar-Rate 0,9998 x Vorhersage). Gleichtakt entstand nirgends von selbst. Die Gueltigkeitsbedingung der
   Karte war zu schwach: Ein Einzelpunkt-Term ist 4,8 z-mal staerker als die Kopplung und laesst die Takte stehen bleiben
   (Plan K1, vom Leser bestaetigt).
2. **Finns Netz (Pyrochlor):** Nach ~500 Takten traegt jedes Tetraeder zwei Gegentakt-Paare (Zeigersumme 0, "2 + 2" in
   100 %). Die Eisregel mit gemeinsamer Achse bildet sich in 10 000 Takten aber nicht: Kollinearitaet P(1) = 0,29-0,30,
   globale nematische Ordnung S <= 0,05. **AN1 verfehlt.** Die gemittelte Dynamik (Diagnose) erreicht sie erst nach
   ~1e4/K, das sind ~3e5 Takte: P(1) = 0,875, S = 0,91. Ohne Rauschen bleibt sie bei 0,26 stehen; das ist Ordnung durch
   Unordnung, wie bei Moessner/Chalker [S].
3. **Takt-Stillstand:** Alle Punkte frieren schlagartig zugleich ein, im Stillstand alle bei derselben Phase. Das ist kein
   Gleichtakt (Plan K2). **AN2 formal eingetroffen** (R = 1,504 auf dem Raster der Karte, 1,57 im feinen Nachtrag), aber
   **vorab ableitbar**: 1,5 ist das Verhaeltnis der Nachbarzahlen 6/4. Bei gleicher Nachbarzahl (einfach-kubisch gegen
   Pyrochlor) senkt die Frustration die Schwelle nur um 4 % (Kartenmass) bzw. 11 % (voller Stillstand).
4. **Freie Packungen, 2D und 3D:** Es bildet sich nur eine oertliche Gegentakt-Neigung. Die Kontakt-Korrelation liegt bei
   -0,27 bis -0,46, verlangt war <= -0,5: **AN3 verfehlt**. Drehsinn-Gebiete umfassen hoechstens 3 Dreiecke. Das Atmen
   haelt die Packung in Bewegung (MSD nach 100 Takten das 2,5- bis 1,5e8-fache der Kontrolle), im eingeschwungenen Zustand
   aber nur 0,05-0,10 PU rms je 100 Takte.
5. **Pumpen:** Ein einzelnes Dreieck, das im Kreis atmet, dreht sich je Takt um (pi/2) eps^2 = 0,0157 rad, mit dem
   Vorzeichen seines Drehsinns. Das ist die geometrische Phase der "fallenden Katze", gerechnet [M] und bestaetigt [E]. In
   Packungen dreht sich nichts mit dem Drehsinn (abs(r) <= 0,022): **AN4 verfehlt**.
6. **Literatur:** Laut Abstract entspricht das Modell "pulsating active matter" (Zhang/Fodor 2023), dort mit zusaetzlicher
   Synchronisation [S Abstract, Gleichungen nicht gelesen]. Neu sind hier nur der Eis-Test auf festen Pyrochlor-Lagen, der
   Stillstand-Vergleich bei gleicher Nachbarzahl und die Pump-Messung.

## 2. Urteile (Regeln aus PLAN.md Abschn. 7, eingefroren 18:36:04; auswertung.json)

| AN | Karte | nach Plan | nach Kartenwortlaut | Kennzahlen (Hauptlauf) |
|---|---|---|---|---|
| AN0 | 85 % | **eingetroffen** | **verfehlt** (Quadrat Saat 4: 0,931; Dreieck: kleinstes abs(chi) 0,004) | Paar: 8 von 8 Saaten pi - abs(Delta) <= 1,4e-5 rad; Rate voll/2K Median 0,9998 (0,9985-1,0001), gemittelt 0,9991-0,9992. Gegentakt (voll) Kette 0,987-0,994, Quadrat Median 0,9999998 (Saaten 4, 6: 0,931, 0,960), Diamant 6 von 6 >= 0,9999996. Dreieck: Mittel abs(chi) Median 0,925 (0,900-0,930), Anteil abs(chi) >= 0,9: 78-84 %, Minimum je Saat 0,004-0,43. t_halb voll/gemittelt Median: Kette 1,001, Quadrat 0,983, Dreieck 0,993, Diamant 0,989 |
| AN1 | 40 % | **verfehlt** | **verfehlt** | Takt 10 000, Saat 1 / 2: Summe/4 < 0,1 in 100 % / 100 %; 2 + 2: 100 % / 100 %; P(1) 0,297 / 0,289; S 0,008 / 0,052; Tetraeder-Kollinearitaet 0,61 / 0,61; eingefroren 0. P(1) waechst etwa logarithmisch (0,22 bei Takt 1000, 0,30 bei 10 000). Diamant-Kontrolle: Gegentakt 0,9997 |
| AN2 | 40 % | **eingetroffen**, vorab ableitbar (K4) | **eingetroffen**, vorab ableitbar | Raster der Karte (Schritt 14,6 %): Pyrochlor springt zwischen kappa 0,0297 und 0,0340 von 0 auf 100 %, Diamant zwischen 0,0447 und 0,0512; beide Saaten gleich. kappa_50 = 0,0318 / 0,0478, R = 1,504. Bei vollem Sprung kann R auf diesem Raster nur 1,146^n sein; 1,504 ist n = 3 |
| AN3 | 45 % | **verfehlt** | **verfehlt** | 2D, Fuellgrad 0,84, schwach: Kontakt-Korrelation -0,460 (Schwelle <= -0,5). MSD 0-100: 0,065 gegen 0,0020 in der Kontrolle (32-fach, erfuellt); MSD 100-200: 0,0109 gegen 2,5e-5 (Plan-Schwelle 0,01 knapp erfuellt). Es scheitert allein die Korrelation |
| AN4 | 25 % | **verfehlt** | **verfehlt** | r = -0,0017 / -0,022 / +0,017 (0,80 / 0,84 / 0,88; je 1,5e5-2,1e5 Paare Dreieck x Takt); Steigung 2e-6 bis 3e-5 rad je Einheit chi gegen 0,0157 beim Einzeldreieck (C0) |

- **Als Kontrolle, nicht als Befund** (Plan Abschn. 7): AN0 ganz; in AN1 Zeigersumme und 2 + 2, die auf der
  Grundzustandsmenge immer gelten (K5); AN2 als Nachbarzahl-Verhaeltnis (K4); in AN3 das Verhaeltnis zur Kontrolle (K6).
- Rauchlaeufe: gleiche Richtung, siehe rauch-69/; C0 dort und im Hauptlauf bitgleich.

## 3. Was sich aus Zufallsphasen von selbst bildet (Zaehlung je Dimension, wie eine Life-Asche)

Bezug Zufall [M]: Bei unabhaengigen Phasen haben 14,4 % der Paare cos > 0,9 und ebenso viele cos < -0,9; ein Dreieck
umschliesst den Nullpunkt (Windung != 0) mit 25 %.

| Dim. | System | was sich bildet [E] |
|---|---|---|
| 1D | Kette (offen, 32) | Gegentakt 0,99 je Beruehrung; Restverdrillung ueber die Laenge (Untergitter-Ordnung 0,37-0,82, langsamste Mode ~ 3000 Takte) |
| 2D | Quadrat 16 x 16 | Gegentakt; 4 von 6 Saaten perfekt, 2 behalten Verdrillung oder Wirbelpaar (0,93 und 0,96) |
| 2D | Dreieck 18 x 18 | 120-Grad-Muster, aber **zwei Drehsinn-Gebiete nebeneinander**: Das mittlere Vorzeichen der Aufwaerts-Dreiecke liegt nach 3000 Takten zwischen -0,30 und +0,43, nicht bei +-1 (Z2-Waende) |
| 2D | frei 0,80 / 0,84 / 0,88, schwach | Kontakt-Korrelation -0,425 / -0,460 / -0,365. Gegentakt-Paare 25 / 26 / 23 %, Gleichtakt-Paare 9 / 10 / 10 % (Zufall je 14 %). Drehsinn-Dreiecke abs(chi) >= 0,5: 49 / 41 / 40 %, davon abs(chi) >= 0,9: 10 / 8 / 7 %. Windung != 0: 40 / 36 / 34 % (Zufall 25 %). Gebiete: 278 / 284 / 313, groesstes 3 / 2 / 3 Dreiecke. Eingefroren 0 |
| 2D | frei, stark (kappa 0,05, 50 Takte) | Korrelation -0,24 / -0,16 / -0,10, Gleichtakt-Paare 10 / 11 / 14 %, eingefroren 0, Taktrate 0,999 / 0,995 / 0,985 |
| 3D | Diamant 5^3 | Gegentakt perfekt (6 von 6 Saaten, Untergitter-Ordnung 1,000) |
| 3D | Pyrochlor 4^3 | Zeigersumme 0 und 2 + 2 nach ~500 Takten in 100 %. "3 + 1"-Fehlstellen ("Monopole"): 48 % am Anfang, 0,4-0,8 % bei Takt 100, 0 ab Takt 200. In 10 000 Takten wird es nicht kollinear (P(1) ~ 0,3); gemittelt nach ~1e4/K schon (P(1) 0,875, S 0,91) |
| 3D | frei 0,60 / 0,64 / 0,68, schwach | Korrelation -0,431 / -0,379 / -0,273; Gegentakt-Paare 23 / 24 / 22 %, Gleichtakt 9 / 9 / 11 %; Drehsinn-Dreiecke 46 / 44 / 39 %; Windung (Durchstosspunkte von Wirbellinien) 39 / 37 / 32 %. Eingefroren 0 |
| 3D | frei, stark (15 Takte) | Korrelation -0,17 / -0,11 / -0,05; Taktrate 0,995 / 0,98 / 0,91 |
| alle | Gleichtakt | nie von selbst. Einzige gleichphasige Form: der Stillstand fester Gitter bei starker Kopplung (alle Punkte bei sin phi von +0,03 bis -0,89, je nach kappa) |

- **Windung und Drehsinn sind eine Groesse** (Nachtrag 1 Punkt 4, [M]): w != 0 heisst chi mit gleichem Vorzeichen, und
  abs(chi) > 0,77 erzwingt w != 0. Die Zeilen "Drehsinn-Dreiecke" und "Windung" zaehlen also fast dasselbe.
- Die Phase ist ein innerer Freiheitsgrad. Raeumlich unterscheiden sich die Dimensionen nur dadurch, ob das Netz
  zweifaerbbar ist (Kette, Quadrat, Diamant: voller Gegentakt) oder Dreiecke hat (Dreieck, Pyrochlor, freie Packungen:
  Frustration). In freien Packungen sehen 2D und 3D fast gleich aus.

## 4. Nachtrag 1 [Zusatz Leitung, beschreibend; NACHTRAG-1.md]

- Feine Abtastung (Schritt 2 %, Saat 1), lauf-69/N1_fein.json und bild_N1_stillstand.png:
  - **50-%-Schwelle:** Pyrochlor 0,0306 (Klammer 0,0303-0,0309); einfach-kubisch 0,0319 (0,0315-0,0322); Diamant 0,0480
    (0,0473-0,0483). R_dia/pyro = 1,570; R_dia/kub = 1,508, also z allein; R_kub/pyro = 1,041. Vorab-Lesart: "kleiner
    Frustrationseffekt (2-10 %)"; Vorhersage [M] 1,036.
  - **Voller Stillstand** (alle Punkte, Taktrate 0): einfach-kubisch ab 0,0348, Diamant ab 0,0525. Die Rasterklammern (0,0341-0,0348 bzw.
    0,0514-0,0525) enthalten die Adler-Schwelle kappa_c = eps/(4 z delta) = 0,0347 bzw. 0,0521 [E bestaetigt M]. Pyrochlor springt
    schon bei 0,0309, 11 % unter seinem gleichfoermigen Wert und 8 % unter dem Wert des geordneten Zustands (0,0335).
    Verhaeltnis voller Stillstand kubisch/Pyrochlor 1,13.
  - **Muster:** Die zweifaerbbaren Gitter haben unterhalb des vollen Stillstands einen Mischbereich (kubisch 0,0315-0,0335,
    Diamant 0,0473-0,0503: 3-99 % eingefroren, dazwischen Einzelwerte, die zurueckspringen). Pyrochlor friert alles oder
    nichts. Welche Punkte im Mischbereich stehen, habe ich nicht gespeichert (offen).
- **Bedeutung:** AN2 misst fast nur die Nachbarzahl. Die Frustration macht Finns Netz etwas leichter einfrierbar
  (Schwelle 4 % bzw. 11 % tiefer, je nach Mass), und es friert gemeinsam statt stueckweise.

## 5. Bilder (lauf-69/)

- **bild_B.png:** links B1 Pyrochlor ueber 10 000 Takte (Summe und 2 + 2 sofort bei 1, P(1) und S unten), Diamant-Gegentakt
  gepunktet. Mitte: Stillstand gegen kappa auf dem Raster der Karte, mit Vorhersage-Linien. Rechts: B3, gemittelte
  Dynamik bis 5e4/K; P(1) und S steigen nur mit Rauschen auf ~0,9.
- **bild_A_C.png:** links freie 2D-Packung (0,84, schwach) am Ende, Farbe = Phase. Mitte: Drehung je Takt gegen Drehsinn
  fuer alle drei Fuellgrade, schwarze Linie = Einzeldreieck. Rechts: Teil A, volle gegen gemittelte Dynamik (Saat 1).
- **bild_N1_stillstand.png:** feiner Stillstand-Vergleich Pyrochlor, einfach-kubisch und Diamant, mit Taktrate.

## 6. Was das bedeutet

- **Fuer Finns Frage "was pumpt":** An der Huelle gekoppelte Punkte wollen gegeneinander atmen, nicht miteinander.
  Ein einzelnes, im Kreis atmendes Dreieck dreht sich wirklich (0,0157 rad je Takt, also 1 Umdrehung in ~400 Takten).
  Das ist eine echte Pumpe ohne Medium [M, E]. In einem Haufen sperren sich die Dreiecke gegenseitig, und es bleibt kein
  messbarer Netto-Dreh (Steigung in 2D 500- bis 7000-mal kleiner als beim Einzeldreieck).
- **Fuer das Fluss-Eis:** Die Eisregel als Phasenmuster ist erreichbar, aber nur ueber Rauschen und sehr langsam
  (gemittelte Dynamik ~3e5 Takte). Die Endwerte passen zu Moessner/Chalker: P(1) 0,875 bei T/K = 1e-3 [E], abgelesen
  ~0,84 [S, Abb. 12]. Die "Monopole" (3 + 1) verschwinden in ~200 Takten und kommen bei diesem Rauschen nicht wieder.
- **Fuer "Life-Logik":** Wie bei den diskreten Life-Regeln (LIFE-DIAMANT-1, LIFE-FCC-1) bleibt aus Zufall Asche: oertliche
  Paare, kleine Drehsinn-Flecken, auf festen Gittern Gebiete und Waende. Gleiter, wandernde Muster oder Gleichtakt-Inseln
  traten nicht auf. Auf das Modell mit Synchronisationsterm (Zhang/Fodor: Spiralwellen, Defekt-Turbulenz) ist das nicht
  uebertragbar.
- **Offen [H]:**
  - Was die freien Packungen bei sehr langen Zeiten tun.
  - Ob Verstimmung durch ungleiche Nachbarzahl (K3) die Ordnung dort verhindert.
  - Welche Muster im Mischbereich des Stillstands stehen.
  - Ob ein Dreieck, das durch eine aeussere Klammer gehalten wird, in der Packung doch pumpt.

## 7. Selbstanzeigen

- **S1 (Literatur):** Drei HTTP-Abrufe statt zwei. Der erste (http, 18:10:03) lieferte 0 Byte (Weiterleitung) und wurde
  ueber https wiederholt. Inhaltlich sind es 2 Abrufe (arXiv-API, Moessner/Chalker-Volltext); das PDF habe ich mit dem
  Lesewerkzeug gelesen (S. 1-10).
- **S2 (Sicht vor dem Einfrieren):** Grobe B2-Rauchwerte (6 kappa-Werte, 1 Saat) habe ich vor dem Einfrieren gesehen. Im
  Plan Abschn. 10 vermerkt; keine Regel danach geaendert.
- **S3 (Rauchlauf-Start):** Die cpu7-Kette des Rauchlaufs 1 startete beim ersten Versuch nicht und wurde neu gestartet.
  Ein ssh-Aufruf hing dabei 2 min. Es lief nichts doppelt.
- **S4 (lokale Werkzeuge ausserhalb der Liste):**
  - ls, cat, mkdir, cp, mv, chmod, rm (zwei eigene Hilfsdateien), paste, cut, wc, date.
  - jq auch mit kleinen Divisionen fuer die Anzeige (Raten/2K, t_halb-Verhaeltnisse). Das ist lokale Rechnung im Kleinen.
  - Ein lokales sleep 45 wurde vom Werkzeug blockiert, also nicht ausgefuehrt.
  - Kein python, awk oder perl.
- **S5 (.69 ausserhalb des Starters):**
  - Lesebefehle: ls, ps, systemctl list-units, sha256sum, grep, cat.
  - mkdir; mv (Log umbenannt, atomarer Ersatz in rauch2/); Warte-Schleifen mit sleep/timeout.
  - kill auf drei PIDs meines eigenen, noch wartenden Nachtrag-Laufs. Kein pkill, kein pgrep -f.
- **S6 (AN2-Raster):** "eingetroffen" mit R = 1,504 liegt auf der Rasterstufe n = 3 knapp ueber 1,5. Mit einer Stufe
  anders gelegen waere es 1,31 oder 1,72 gewesen. Das Urteil steht, ist aber auch Rasterglueck. Der feine Nachtrag
  (1,57) stuetzt die Richtung.
- **S7 (Laufzeiten nach Rauchlauf):** B1 von 20 000 auf 10 000 Takte gekuerzt; B1 T = 0 gestrichen; B2 200 statt 300
  Takte; B3 kuerzer; Teil C stark nur 50 (2D) bzw. 15 (3D) Takte, 3D schwach und Kontrolle 200 Takte. Alles vor dem
  Einfrieren, Plan Abschn. 10.
- **S8 (Kontroll-Entspannung):** 50 Takte Entspannung reichten bei den dichtesten Packungen nicht ganz. Die Kontrolle
  bewegt sich noch: MSD 0-100 bei 2D 0,88 = 0,027, bei 3D 0,64 = 0,0079, bei 3D 0,68 = 0,012. Das betrifft das
  Verhaeltnis dort (2D 0,88: nur 2,5-fach), nicht AN3 (0,84: Kontrolle 0,0020).
- **S9 (Nachtrag nach Sicht):** Den ersten Nachtrag-Lauf (grobes Raster) habe ich vor seinem Start abgebrochen und durch
  das feine Raster ersetzt. Grund: das B2-Ergebnis, das ich nach dem Einfrieren angesehen hatte (NACHTRAG-1.md). Er ist
  beschreibend und ohne AN-Urteil.
- **S10 (Messgroessen):**
  - Geometrische Nachbarn (Takt-Abstand < 1,1) schliessen Paare ein, die sich selten beruehren (z 5-10). Die
    Zaehltabelle nutzt sie, AN3 die momentanen Beruehrungen.
  - Windung und Drehsinn sind fast eine Groesse (Abschn. 3).
  - Nahe der Stillstand-Schwelle ist das Takt-Mittel der Phase verschmiert, weil die Taktrate auf 0,3-0,6 omega faellt.
    Die dort gespeicherten cos-Werte laufender Paare (B2, kappa 0,0297: +0,11 / +0,13) sind daher nicht als Gleichtakt
    lesbar und werden nicht benutzt.
- **S11:** Die Bezugslinie im Pump-Bild nutzt das Vorzeichen aus C0, das ich schon im Rauchlauf kannte.
- **S12:** Kein frischer Leser hat diese Datei gegengelesen. Die Rechnung zur geometrischen Phase (K7) habe ich allein
  gefuehrt. C0 bestaetigt die Zahl, nicht jeden Schritt.

## 8. Einfach gesagt

Stell dir viele kleine Baelle vor, die regelmaessig dicker und duenner werden und sich nur an der Haut beruehren. Dann
atmen Nachbarn am liebsten abwechselnd: Einer wird dick, waehrend der andere duenn wird, weil sie sich so am wenigsten
druecken. In Finns Tetraeder-Netz klappt das nicht fuer alle Paare zugleich; jedes Tetraeder teilt sich schnell in "zwei so,
zwei gegen", aber die schoene gemeinsame Ordnung wie bei Spin-Eis braucht Rauschen und ungefaehr 300 000 Takte. Drueckt man
die Baelle zu fest zusammen, bleiben alle auf einmal stehen, ziemlich genau dort, wo es die Zahl der Nachbarn vorhersagt.
Ein einzelnes Dreieck aus drei Baellen, die reihum atmen, dreht sich wie eine fallende Katze jeden Takt ein kleines Stueck;
in einem vollen Haufen blockieren sich die Dreiecke aber gegenseitig, und Gleichtakt entsteht nie von selbst.
