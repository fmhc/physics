# QBALL-DREIPOL-3: Ergebnis (Code-Agent, Runde 43, Fast Lane)

- Code-Agent fuer claude-primary. Start 2026-10-04 19:07:16 CEST; ERGEBNIS begonnen 19:32:40 CEST (date).
- **Unterbrechung (Sitzungslimit):** letzte Aktion vor der Pause 19:53:47 CEST, fortgesetzt 21:35:32 CEST (beides date).
  - Zeitbox: Vor der Pause waren 43 min 29 s offen (bis 20:37:16). Neu gerechnet ab 21:35:32, also bis 22:19:01 CEST.
  - In der Pause lief auf der .69 nichts von mir: Alle Einheiten waren vorher fertig (letzte 17:42:30 UTC); um
    19:35:50 UTC (21:35:50 CEST) lief keine dp3-Einheit.
  - Eingefrorenes unveraendert (EINGEFROREN-SHA256.txt nach der Pause erneut geprueft, alle OK).
  - Der erste frische Gegenleser wurde vom selben Limit abgebrochen (siehe Abschnitt Gegenlesen).
- **Eingefroren** 19:25:49 CEST: PLAN.md und code/{dreipol2.py, dreipol3.py, auswertung3.py, laeufe-p4000a.sh,
  laeufe-p4000b.sh}, je als .eingefroren-20261004-192549, Hashes in EINGEFROREN-SHA256.txt.
  - Auf der .69 vor dem Start geprueft (17:25:55 UTC, Ausgabe nur in der Sitzung): dieselben Hashes. Nach den Laeufen
    erneut (lauf-69/PRUEFSUMMEN.txt, 17:42:51 UTC): gleich.
- **Laeufe** (.69, kleintest.sh, Spuren p4000a und p4000b, torch/CUDA auf Quadro P4000, float64), alle rc = 0:
  - Hauptlaeufe: Start 17:25:59 UTC; bisekt2 fertig 17:27:17, bisekt3 17:28:16, stab3 17:33:43.
  - Auswertung: Aufruf 17:33:46 UTC, wartete auf die Spur p4000a, Ende 17:38:48 UTC (Einheit 8,5 s).
  - Nachtraege nach Sicht, ohne Urteil:
    - N1 Feinabtastung (nach Sicht beider Bisektionen): 3D 17:29:34 bis 17:30:50 UTC; 2D Aufruf 17:29:34, Ende
      17:34:40 UTC (wartete auf stab3).
    - N2 Teil B mit laengerer Wandzeit: gestartet 17:30:53 UTC nach Sicht der Teil-B-Referenz und von V1. V2 bis R20
      waren im Hauptlauf da noch nicht fertig. V1/V2 bis 17:38:39 UTC; L1/L2 Ende 17:42:30 UTC (wartete auf N1 2D).
    - Auswertung der Nachtraege: Ende 17:38:50 UTC.
- **Kennzeichen:** [E] gerechnet im Modell, [M] Mathematik, [P] Projektdatei, [L] Literatur, [H] Hypothese.
- Alles ist eine synthetische Rechnung im Modell (Papier-I-Potential mit drei Komponenten, g4 = -0,1). **Keine
  Messdatenbestaetigung.** 2D und 3D sind getrennt ausgewiesen (AGENTS.md, Dimensionsvergleich).

## Ergebnis zuerst

1. **Kontrollen eingetroffen (DR0) [E].**
   - 3D Q1 = 800: Tropfen 3,3221 unter dem Mischball (N1: 3,32). 3D Q1 = 400: verschmilzt.
   - 2D Q1 = 60: wie DREIPOL-2 (Luecke 0,145617, Paarabstand 1,2453 R).
2. **Schwelle [E]:** Die eingefrorene Bisektion brach in beiden Dimensionen am ersten entmischten Zustand ab, weil
   dessen Paarabstand unter R lag (Ausgang "offen").
   - Klammern nach Plan: **3D 600 bis 800, 2D 52,5 bis 60.**
   - Nachtrag N1 (beschreibend): Die Entmischung beginnt in **3D zwischen Q1 = 600 und 650**, in **2D zwischen 52,5
     und 53,5**.
   - Beide Starts (getrennte Baelle, farbige Sektoren) enden immer im selben Zustand. Die Luecke zum Mischball waechst
     von fast null an (3D: 0,06 bei 650, 0,76 bei 700, 3,32 bei 800). Vor der Schwelle wird der Fluss stark langsamer
     (2D: 22900 Schritte bei 52,5 statt 1750 bei 45).
   - Das passt zu einem **stetigen Uebergang** [Deutung H]: Der Tropfen waechst aus dem Mischball heraus, wo dieser
     weich wird. Ein kleiner Sprung zwischen den Stuetzstellen ist nicht ausgeschlossen; der Paarabstand springt
     zwischen benachbarten Q1 von ~4e-4 R auf 0,48 R (2D) bzw. 0,57 R (3D).
3. **3D-Tropfen bei Q1 = 800 (DR1): nach Kartenwortlaut eingetroffen, nach Plan nicht auswertbar [E].**
   - Alle sechs Stoerungen kehren zur Form zurueck (Endabstand <= 5,5e-7 R, Energie gleich bis 1,8e-6), auch aus
     der Ebene heraus und nach +34,5 Energie (5 % Farbuebertragung).
   - Vier der sechs Fluesse erreichten das Residuum 1e-8 nicht in den geplanten 60 s (Ende 1,8e-8 bis 3,2e-8), also
     "offen" nach Plan. Mit 2,5-facher Wandzeit (Nachtrag N2) blieben alle vier beim selben Residuum stehen. Die
     Endzustaende sind der Tropfen, als Ganzes leicht verschoben bzw. gedreht (Nullmoden); der Rest passt zu einem
     langsamen Gleiten auf dem Gitter [H].
   - Auch 20 % Rauschen (+1229 Energie) kehrt zurueck (beschreibend).
4. **R* (DR2): nach Plan und Kartenwortlaut nicht auswertbar**, weil die Klammern zu breit blieben (3D 25 %,
   2D 12,5 %; Grenze 10 %). Kein Urteil, keine Lesart. Die Radien im Nachtrag sind nicht die DR2-Pruefgroesse und
   kein Ersatzurteil.
5. **Bedeutung [H]:**
   - In 3D entmischt sich der Ball oberhalb einer Ladung zwischen 600 und 650 (Schaetzungen 614 bis 631).
   - Ein Tropfen im Plansinn (Paarabstand > R) liegt erst ab 750 vor (1,007 R); bei 650 und 700 ist der Endzustand
     entmischt, aber kompakter.
   - Auf Stabilitaet geprueft ist nur Q1 = 800: Nach Kartenwortlaut kehrt er dort in allen gerechneten Richtungen
     zurueck. Kein Einschluss (einzelne Pole stabil, U(1)^3).
   - Der Nachtrag deutet auf einen anderen Mechanismus, als die Karte annahm: eine **Entmischungs-Instabilitaet des
     Mischballs** (stetig, weiche Mode), kein Duennwand-Sprung [Deutung H].

## Urteile (mechanisch, lauf-69/auswertung.json; Vorhersagen der Karte unveraendert)

| Nr | Vorhersage (Karte) | Wahrsch. | Plan | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| DR0 | Kontrollen: Q1 = 800 (3D) gibt den Tropfen 3,32 +- 0,1 unter dem Mischball; Q1 = 400 verschmilzt; 2D-Tropfen bei Q1 = 60 wie DREIPOL-2 | 85 % | **eingetroffen** | **eingetroffen** | 3D 800: E_Misch - E_Ende = 3,32209 (Gitter), Paarabstand 1,0930 R, 900 Schritte. 3D 400: verschmolzen, Paarabstand 6e-5 R, 800 Schritte. 2D 60: Paarabstand 1,24529 R (Abw. 2,4e-4), Luecke 0,145617 (Abw. 0,26 %), 1050 Schritte |
| DR1 | [H] Der 3D-Tropfen bei Q1 = 800 ist ein lokales Minimum: alle 6 Stoerungen kehren zurueck (Endabstand < 2 % R, Energie gleich auf 1e-3) | 55 % | **nicht auswertbar** (V1, V2, L1, L2 "offen": Wandzeit 60 s vor Residuum 1e-8) | **eingetroffen** | d_rms am Ende <= 5,5e-7 R, d_form <= 9,4e-7 R, abs(dE) <= 1,8e-6 bei allen sechs; Residuum am Ende V1/V2/L1/L2 1,8e-8 bis 3,2e-8; P1/P2 bei Schritt 0 (exakte Symmetrie, vorab ableitbar). Nachtrag N2 (ohne Urteil): V1/V2 mit 150 s weiter Residuum 3,2e-8 bzw. 2,9e-8 (12550 bzw. 17700 Schritte), Form und Energie unveraendert; L1/L2 mit 150 s weiter 2,5e-8 bzw. 1,8e-8 (je 19950 Schritte) |
| DR2 | [H, M Duennwand] R* ist in 2D und 3D gleich auf 30 % (eine dimensionsuebergreifende Schwellformel) | 40 % | **nicht auswertbar** | **nicht auswertbar** | Klammern nach Plan 3D [600, 800] (Breite 25 %), 2D [52,5; 60] (12,5 %), Grenze 10 %. Die Radien am oberen Klammerende stehen mechanisch in auswertung.json; sie sind wegen "nicht auswertbar" ohne Bedeutung fuer das Urteil |

- **DR0:** Beide Nachbauten sind bitnah: 3D Q1 = 800 E_Ende 1919,98574643 wie N1 (1919,98574643); 2D Q1 = 60
  E_Ende 138,83507144 wie DREIPOL-2 (138,83507144). Das war Kontrolle per Konstruktion (Plan 2.2).
- **DR1, Lesarten:** Plan verlangt "konvergiert" (Residuum < 1e-8). Vier Fluesse endeten an der Wandzeit 60 s mit
  Residuum 1,8e-8 bis 3,2e-8, Form und Energie schon zurueck. Nach der Planregel ist das "offen", nicht "nicht
  zurueck" (der Abstand fiel von 0,05 bis 0,08 R auf <= 5,5e-7 R). Der Kartenwortlaut prueft nur Abstand und Energie
  am Ende.
- **DR2, Grund fuer "nicht auswertbar":** Die Bisektionsregel (Ausgang "Tropfen" nur bei kleinstem Paarabstand > R,
  Regel aus DREIPOL-2) stoppte am ersten entmischten Zustand nahe der Schwelle, weil dieser kompakter ist (0,98 R in
  2D, 0,87 R in 3D). Siehe Selbstanzeige 1.

## Tabellen

### A. Teil A, Bisektion nach Plan (Fluss bei festen Ladungen vom beruehrenden Dreieck, g4 = -0,1)

Je Schritt in dieser Reihenfolge gerechnet: Einpolball, Mischball, Sektorlauf (E_Tropfen), Zeile "vorab", dann der
Fluss vom beruehrenden Dreieck. **Kein Schritt war erzwungen**; alle Starts lagen 2,85 bis 35,3 ueber dem Mischball.

**3D** (N = 80, L = 48, h = 0,6; Bild bisektion.png, bisektion_bilder.png):

| Q1 | Rolle | om | R_halb | E_start | E_Misch (Gitter) | E_Tropfen (Sektorlauf) | E_start - E_Misch | erzwungen | Ausgang | Schritte | E_Ende - E_Misch | Paarabstand/R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 800 | Kontrolle oben | 0,7570 | 4,419 | 1956,245 | 1923,3078 | 1919,9857 | +32,938 | nein | Tropfen | 900 | -3,32209 | 1,0930 |
| 400 | Klammer unten | 0,7938 | 3,294 | 1035,264 | 1001,3132 | keiner (Sektorlauf verschmolzen) | +33,951 | nein | verschmolzen | 800 | +1,4e-8 | 6e-5 |
| 600 | Bisektion 1 | 0,7711 | 3,920 | 1500,757 | 1465,4170 | keiner (verschmolzen) | +35,340 | nein | verschmolzen | 4900 | +1,8e-7 | 4,6e-4 |
| 700 | Bisektion 2 | 0,7634 | 4,179 | 1729,457 | 1694,9744 | keiner (Sektorlauf "offen", entmischt) | +34,483 | nein | **offen** (Zwischenform, konvergiert) | 1400 | -0,75951 | 0,8743 |

- Abbruch bei 700 (Regel: offen). Klammer [600, 800].
- E_start - E_Tropfen bei 800: +36,26. Der Sektorstart lag 68,4 bis 90,9 ueber dem Mischball (kein Hilfslauf
  erzwungen).
- Sektorlauf und Dreieckslauf endeten in jedem Schritt im selben Zustand (E gleich bis 1e-8).

**2D** (N = 256, L = 64, h = 0,25):

| Q1 | Rolle | om | R_halb | E_start | E_Misch (Gitter) | E_Tropfen (Sektorlauf) | E_start - E_Misch | erzwungen | Ausgang | Schritte | E_Ende - E_Misch | Paarabstand/R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 60 | Kontrolle oben | 0,7151 | 3,176 | 141,831 | 138,9807 | 138,83507 | +2,851 | nein | Tropfen | 1050 | -0,145617 | 1,2453 |
| 30 | Abstieg | 0,7588 | 2,105 | 76,484 | 73,0182 | keiner (verschmolzen) | +3,466 | nein | verschmolzen | 500 | +7e-12 | 5e-6 |
| 45 | Bisektion 1 | 0,7303 | 2,673 | 109,682 | 106,1999 | keiner (verschmolzen) | +3,482 | nein | verschmolzen | 1750 | +5e-11 | 2e-5 |
| 52,5 | Bisektion 2 | 0,7218 | 2,932 | 125,845 | 122,6284 | keiner (verschmolzen) | +3,217 | nein | verschmolzen | **22900** | +1,4e-9 | 4e-4 |
| 56,25 | Bisektion 3 | 0,7183 | 3,056 | 133,856 | 130,8131 | keiner (Sektorlauf "offen", entmischt) | +3,043 | nein | **offen** (Zwischenform, konvergiert) | 1850 | -0,038186 | 0,9813 |

- Abbruch bei 56,25. Klammer [52,5; 60].
- E_start - E_Tropfen bei 60: +2,996. Sektorstart 6,3 bis 6,8 ueber dem Mischball.

### A'. Nachtrag N1 (ohne Urteil, nach Sicht): Feinabtastung mit Entmischungsregel

- Code: code/nachtrag3.py ruft dreipol3.schritt unveraendert auf, nur andere Q1 und Wandzeit 110 s je Fluss.
- **Regel (beschreibend, N1_*.json .regel):** "entmischt" heisst konvergiert, groesster Paarabstand >= 0,01 R und
  E_Ende < E_Misch; "verschmolzen" heisst konvergiert und groesster Paarabstand < 0,01 R; sonst offen.
- **Pflichtprobe auch hier** (Zeile "vorab", vor dem Dreiecksfluss); kein Start erzwungen:

| Dim | Q1 | E_start | E_Misch (Gitter) | E_Tropfen (Sektorlauf, Hauptregel) | E_start - E_Misch | erzwungen |
|---|---|---|---|---|---|---|
| 3D | 650 | 1615,351 | 1580,3644 | keiner (Sektorlauf "offen", entmischt) | +34,987 | nein |
| 3D | 750 | 1843,109 | 1809,2797 | 1807,3894 | +33,829 | nein |
| 2D | 55,5 | 132,257 | 129,1776 | keiner (Sektorlauf "offen", entmischt) | +3,079 | nein |
| 2D | 54,5 | 130,123 | 126,9958 | keiner (Sektorlauf "offen", entmischt) | +3,127 | nein |
| 2D | 53,5 | 127,986 | 124,8128 | keiner (Sektorlauf "offen", entmischt) | +3,173 | nein |

- Mit den Hauptschritten zusammen (Ordnungsparameter: Luecke E_Misch - E_Ende und Paarabstand):

| Dim | Q1 | om | Ausgang (Dreieck = Sektor) | Schritte | E_Misch - E_Ende | Paarabstand/R | min. Reinheit |
|---|---|---|---|---|---|---|---|
| 3D | 600 | 0,7711 | verschmolzen | 4900 | -1,8e-7 | 4,6e-4 | 0,317 (gemischt) |
| 3D | **650** (N1) | 0,7670 | **entmischt** | 4050 | 0,0592 | 0,566 | 0,491 |
| 3D | 700 | 0,7634 | entmischt | 1400 | 0,7595 | 0,874 | 0,597 |
| 3D | **750** (N1) | 0,7601 | entmischt (Tropfen) | 1050 | 1,8902 | 1,007 | 0,646 |
| 3D | 800 | 0,7570 | entmischt (Tropfen) | 900 | 3,3221 | 1,093 | 0,678 |
| 2D | 52,5 | 0,7218 | verschmolzen | 22900 | -1,4e-9 | 4e-4 | 0,327 (gemischt) |
| 2D | **53,5** (N1) | 0,7208 | **entmischt** | 8500 | 0,00137 | 0,479 | 0,435 |
| 2D | **54,5** (N1) | 0,7198 | entmischt | 3550 | 0,00954 | 0,740 | 0,501 |
| 2D | **55,5** (N1) | 0,7189 | entmischt | 2300 | 0,0239 | 0,895 | 0,542 |
| 2D | 56,25 | 0,7183 | entmischt | 1850 | 0,0382 | 0,981 | 0,565 |
| 2D | 60 | 0,7151 | entmischt (Tropfen) | 1050 | 0,1456 | 1,245 | 0,641 |

- **Schwelle der Entmischung [E]:** 3D zwischen 600 und 650, 2D zwischen 52,5 und 53,5.
- **Stetig [E, Deutung H]:** Die Luecke geht gegen null; ihre Wurzel steigt in 2D fast linear (je Einheit Q1: 0,061,
  0,057, 0,054, 0,050; Kopfrechnung aus der Tabelle).
  - Landau-Form (Luecke ~ (Q1 - Q1c)^2) ergibt Q1c ~ 52,9 in 2D. In 3D gibt das Paar 650/700 Q1c ~ 631, der
    Paarabstand (~ Wurzel) ~ 614 [E, grobe Schaetzung].
  - **Unabhaengige dritte Schaetzung** aus der verschmolzenen Seite (nachtrag_aw.json): Die Abklingrate des Residuums
    (weichste Mode des Mischballs) faellt zur Schwelle hin, 2D 0,0262 / 0,0065 / 0,0003 je Schritt bei 30 / 45 / 52,5,
    3D 0,0132 / 0,0016 bei 400 / 600. Linear auf null verlaengert: **2D 52,87, 3D 626,7**.
  - Zusammen fuer 2D: 52,89 (Luecke), 52,78 (Paarabstand), 52,87 (Rate), also **Q1c(2D) ~ 52,8 bis 52,9**. Fuer 3D:
    631, 614, 627, also **Q1c(3D) ~ 614 bis 631** [E, Zwei-Punkt-Schaetzungen].
  - Dass der Mischball dort weich wird, wo der Tropfen erscheint, ist das Kennzeichen eines stetigen Uebergangs
    (Gabelung). Bei einem Sprung laege die Instabilitaet des Mischballs ueber dem Auftauchen des Tropfens [M, Deutung
    H].
  - Der Paarabstand nimmt zur Schwelle hin ab (0,48 R bei 53,5 in 2D, 0,57 R bei 650 in 3D), springt aber zwischen
    den benachbarten Stuetzstellen von ~4e-4 R auf diese Werte. Ein kleiner Sprung ist damit nicht ausgeschlossen.
  - Kein Hinweis auf zwei Endzustaende: Sektor- und Dreiecksstart enden bei jedem Q1 im selben Zustand (Energie
    gleich bis 1e-8).
  - Die Flussdauer waechst zur Schwelle hin von beiden Seiten (2D: 1750, 22900 | 8500, 3550, 2300 Schritte; 3D: 800,
    4900 | 4050, 1400, 1050). Deutung [H]: eine weiche Mode an der Schwelle.
- **Radien an der Schwelle (beschreibend):**

| Dim | Q1 | R_eq Einpolball | R_eq Mischball | R_eq Endzustand | Endzustand / Einpolball |
|---|---|---|---|---|---|
| 3D | 600 | 4,214 | 6,269 | 6,269 (gemischt) | 1,488 |
| 3D | 650 | 4,338 | 6,450 | 6,460 | 1,489 |
| 3D | 800 | 4,678 | 6,943 | 6,896 | 1,474 |
| 2D | 52,5 | 3,153 | 5,620 | 5,620 (gemischt) | 1,782 |
| 2D | 53,5 | 3,184 | 5,676 | 5,695 | 1,789 |
| 2D | 60 | 3,379 | 6,029 | 6,082 | 1,800 |

- An der Entmischungsschwelle hat der Endzustand die Groesse des Mischballs. Das ist nicht die DR2-Pruefgroesse
  (R_eq des Tropfens im Plansinn am oberen Klammerende, Plan 4) und kein Ersatzurteil.

### B. Teil B (3D, Q1 = 800, N = 80, L = 48; Bilder stab3_fluss.png, stab3_bilder.png)

**Referenz:** E_ref = 1919,98574642, E_Misch = 1923,30784 (Luecke 3,3221), Paarabstand 1,0930 R, R = 4,4188, Reinheit
0,678 bis 0,712. Die Referenz erreichte das Ziel 1e-9 nicht: Wandzeit 90 s nach 13650 Schritten, Residuum 3,59e-9.

| Stoerung | Start: d_rms / d_form (R), dE | Start unter E_Misch | Ende: d_rms / d_form (R), dE | Residuum Ende | Schritte, Status | Plan | Kartenwortlaut |
|---|---|---|---|---|---|---|---|
| V1 Pol 1 um 0,15 R tangential + 0,15 R aus der Ebene | 0,0505 / 0,0917, +2,265 | ja | 2,3e-7 / 3,7e-7, -1,3e-6 | 3,2e-8 | 8450, Wandzeit | offen | zurueck |
| V2 Pol 2 um 0,15 R radial + 0,15 R aus der Ebene | 0,0755 / 0,1413, +3,558 | nein (+0,24) | 1,1e-7 / 2,5e-7, -1,8e-6 | 2,9e-8 | 8250, Wandzeit | offen | zurueck |
| L1 5 % Farbe 2 nach Klumpen 1 | 0,0836 / 0,1905, +34,54 | nein | 5,5e-7 / 9,4e-7, +3,9e-7 | 2,5e-8 | 8100, Wandzeit | offen | zurueck |
| L2 5 % Farbe 1 nach Klumpen 2 | 0,0836 / 0,1905, +34,54 | nein | 1,3e-7 / 2,7e-7, +4,3e-7 | 1,8e-8 | 8100, Wandzeit | offen | zurueck |
| P1 Phase Komp. 2 um pi/2 | 3e-16 / 0, 0 | ja | gleich | 3,6e-9 | 0, konvergiert | zurueck (ableitbar) | zurueck |
| P2 Phasen 2pi/3, 4pi/3 | 1e-16 / 2e-16, 0 | ja | gleich | 3,6e-9 | 0, konvergiert | zurueck (ableitbar) | zurueck |
| Z1 Pol 1 um 0,15 R aus der Ebene (ohne Urteil) | 0,0056 / 0,0102, +1,184 | ja | 1,2e-7 / 2,7e-7, -5,9e-7 | 9,6e-9 | 1250, konvergiert | (zurueck) | (zurueck) |
| R5 Rauschen 5 % (ohne Urteil) | 0,0017 / 0,0039, +75,96 | nein | 1,7e-7 / 3,2e-7, -4,8e-9 | 9,9e-9 | 1000, konvergiert | (zurueck) | (zurueck) |
| R20 Rauschen 20 % (ohne Urteil) | 0,0703 / 0,1475, +1229 | nein | 1,2e-7 / 1,8e-7, -1,1e-8 | 9,0e-9 | 1400, konvergiert | (zurueck) | (zurueck) |

- **Nichttrivial** sind V1, V2 und L1/L2 (eine Klasse).
  - V2, L1, L2, R5 und R20 starteten **ueber** dem Mischball; das Verschmelzen war energetisch moeglich und trat nicht
    ein.
  - Bei V1 (Start 1,06 unter dem Mischball, Kopfrechnung) war Verschmelzen ausgeschlossen, die Rueckkehr nicht.
- **Grenze des Abstandsmasses:** Drei Schwerpunkte liegen immer in einer Ebene. Eine Verschiebung aus der Ebene
  aendert die Paarabstaende erst in zweiter Ordnung (Z1: d_form 0,0102 bei 0,15 R).
  - Dass V1, V2 und Z1 zurueckkehren, stuetzt sich daher vor allem auf Energie und Residuum: Endzustand stationaer
    und energiegleich mit dem Tropfen bis ~1e-6.
  - Gegen eine Kippung ist das blind (Nullmode). Nach V1, V2 und Z1 liegt die verschobene Farbe am Ende 0,53 bis 0,60
    ueber den beiden anderen (z-Schwerpunkte in stab3.json), bei gleicher Form und Energie. Deutung [H, nur aus
    Schwerpunkten und Energie, Felder nicht verglichen]: der ganze Tropfen, um 7 bis 8 Grad gekippt (Kopfrechnung),
    also eine Drehung (Nullmode). Die Seitenansicht (Projektion ueber y) zeigt das nur schwach.
- **Nachtrag N2 (ohne Urteil):** Teil B mit Referenz bis 150 s und 150 s je Stoerung (eingefrorener Code, andere
  Argumente).
  - Die Referenz blieb bei 3,59e-9 (18000 Schritte), V1 bei 3,22e-8 (12550 Schritte), V2 bei 2,92e-8 (17700
    Schritte). Das sind dieselben Werte wie im Hauptlauf; Abstand und Energie aenderten sich nicht.
  - L1/L2: Residuum 2,47e-8 bzw. 1,82e-8 nach je 19950 Schritten, ebenfalls wie im Hauptlauf (Referenz dort
    3,59e-9 nach 15400 Schritten).
  - **Deutung [H]:** Der Rest ist kein Weglaufen. Der Tropfen ist um eine Nullmode verschoben bzw. gedreht und gleitet
    auf dem Gitter sehr langsam. Die Endenergie liegt bei V1/V2 1,3e-6 bzw. 1,8e-6 unter E_ref, bei L1/L2 3,9e-7 bzw.
    4,3e-7 darueber, also 2e-10 bis 9e-10 relativ. Die Schwerpunkte wandern zwischen 60-s- und 150-s-Lauf um 5e-5 bis
    2e-4 (Gegenleser), bei konstantem Residuum. Das Konvergenzziel 1e-8 lag unter diesem Sockel.

## Bilder

- lauf-69/bisektion.png: E - E_Misch je Schritt (Start, Ende, Sektorlauf, 3 E_1), 3D und 2D.
- lauf-69/bisektion_bilder.png: Endfelder an den Klammerenden (3D: Ebene z = 0).
- lauf-69/stab3_fluss.png: d_rms, d_form und E - E_ref im Fluss je Stoerung.
- lauf-69/stab3_bilder.png: Teil B, Ebene z = 0 und Seitenansicht (Projektion ueber y), Start und Ende.
- lauf-69/nachtrag/uebergang.png: Ordnungsparameter und Abklingrate gegen Q1, 3D und 2D (Nachtrag, beschreibend).

## Gegenlesen

- **Erster Versuch:** frischer Leser, nur lesend, gestartet zwischen 19:42:55 und 19:46:18 CEST (date davor und
  danach). Das Sitzungslimit brach ihn ab, ohne Bericht.
- **Zweiter Versuch:** gestartet zwischen 21:35:32 und 21:36:58 CEST, Bericht vor 21:50:44 CEST (date). Er hat rund
  300 Zahlen gegen die Rohdaten geprueft, in beiden Richtungen.
  - **Urteile:** Alle drei folgen mechanisch aus PLAN 6 und stimmen mit auswertung.json; die Bisektionen folgen
    PLAN 4.
  - **A, berichtigt:** R_halb bei 2D Q1 = 56,25 ist 3,056, nicht 3,057 (Rundung).
  - **B, berichtigt:**
    1. Die Hashpruefung vor dem Start ist nur in der Sitzung belegt; PRUEFSUMMEN.txt ist die Pruefung danach.
    2. "Fester Tropfen ab 600 bis 650" vermischte Entmischung und Tropfen im Plansinn (dieser erst ab 750).
    3. "Zeigt"/"nicht zu sehen" zum stetigen Uebergang war zu stark; der Paarabstand springt zwischen benachbarten
       Stuetzstellen. Jetzt als Deutung [H] mit diesem Vorbehalt.
    4. Die Radien des Nachtrags und die Verhaeltnisse 1,12/1,20 standen direkt beim DR2-"nicht auswertbar" und liessen
       sich als Ersatzurteil lesen. Ich habe die Verhaeltnisse gestrichen und den Vorbehalt "nicht die
       DR2-Pruefgroesse" ergaenzt.
    5. Der Satz "Ein Ziel 1e-7 haette gepasst" gab dem DR1-"nicht auswertbar" eine Richtung (Regel nach dem Ausgang).
       Er ist gestrichen.
    6. "Weiterrutschen" in "Einfach gesagt" stand als Tatsache; jetzt als Vermutung.
  - **C, berichtigt:**
    - drei (2D) bzw. zwei (3D) Halbierungen
    - N1-Regel vollstaendig
    - Q1c(3D) einheitlich 614 bis 631
    - N2 startete nach Sicht nur der Referenz und von V1
    - Startzeit des ersten Lesers aus date statt geschaetzt
    - Energievorzeichen und relative Spanne im N2-Abschnitt
    - Kippung und weiche Mode als [H] markiert
  - **Ungeprueft** blieben laut Leser die Bilder, der Code, der N1-Bezugswert aus DREIPOL-2 (ausserhalb seiner
    Pfade) und die Angaben zur Pause.
- Die Fassung vor diesem Gegenlesen liegt als ERGEBNIS.md.vor-gegenlesen daneben. Die danach geaenderten Saetze hat
  kein weiterer frischer Leser gelesen.

## Selbstanzeigen

1. **Ausgangsregel zu eng (Planfehler, nach dem Lauf erkannt):**
   - Ich habe die Gestaltregel aus DREIPOL-2 uebernommen: "Tropfen" nur bei kleinstem Paarabstand > R, alles
     dazwischen "offen" mit Abbruch der Bisektion.
   - Nahe der Schwelle ist der entmischte Zustand kompakter (2D 0,98 R bei 56,25; 3D 0,87 R bei 700). Beide
     Bisektionen brachen deshalb nach drei (2D) bzw. zwei (3D) Halbierungen ab; DR2 wurde so nicht auswertbar.
   - In der Ableitbarkeitsprobe habe ich nur an einen Sprung gedacht (Duennwand: Tropfen ab R*). Dass der Tropfen
     stetig aus dem Mischball wachsen kann, ist mir erst nach dem Lauf aufgefallen. Die Abfrage "Ausgang offen" hat
     das immerhin sichtbar gemacht, statt einen Zwischenzustand als Tropfen oder Verschmelzen zu zaehlen.
2. **Konvergenzziel in Teil B zu streng gewaehlt (Planfehler):**
   - Die Wandzeit 60 s je Stoerung beruhte auf 1500 bis 3000 Schritten aus 2D (DREIPOL-2). In 3D blieben V1, V2, L1
     und L2 bei Residuum 1,8e-8 bis 3,2e-8 stehen, obwohl Form und Energie laengst zurueck waren.
   - Auch die Referenz kam nicht unter 3,6e-9 (Ziel 1e-9).
   - Auch mit 2,5-facher Wandzeit (N2, ein Lauf je Stoerung) blieb das Residuum gleich. Welches Ziel gepasst haette,
     lasse ich offen; eine Regel nach dem Ausgang aendere ich nicht, DR1 bleibt nach Plan ohne Urteil.
   - Die Laufzeitprobe hat nur die Zeit je Schritt gemessen, nicht die noetige Schrittzahl.
3. **ssh offen gehalten (vor dem Einfrieren):** Leitungstest und Laufzeitprobe startete ich mit "cd X && nohup
   setsid ... &". Die Hintergrund-Unterschale hielt die ssh-Sitzung bis zum Ende offen (~35 s und ~66 s). Fuer die
   Hauptlaeufe und Nachtraege habe ich ohne "&&" gestartet; die Rueckkehr war sofort.
4. **Reihenfolge:** Code, Leitungstest und Laufzeitprobe liefen vor dem Plantext (im Plan offen gelegt). Gesehen habe
   ich dort nur Fremdwerte (g4 = +0,1), keine Hauptwerte.
5. **Nachtraege nach Sicht:**
   - N1 (Feinabtastung, code/nachtrag3.py, code/laeufe-nachtrag.sh)
   - N2 (Teil B mit laengerer Wandzeit, eingefrorener Code mit anderen Argumenten, code/laeufe-nachtrag2.sh)
   - Auswertung der Nachtraege (code/nachtrag_aw3.py)
   - Alle sind neu und nicht eingefroren (Hashes in lauf-69/PRUEFSUMMEN.txt). Sie aendern kein Urteil; die
     Kartenwahrscheinlichkeiten bleiben unberuehrt.
6. **Auswertung wartete auf der .69 per Schleife:** Den Start der Auswertung habe ich mit einer bash-Warteschleife
   ("until grep ...; do sleep 5") an das Ende von stab3 gebunden, weil die Spur p4000a noch belegt war. Das ist kein
   Dienst und kein Hook, aber eine kleine Wartelogik ausserhalb von kleintest.sh.
7. **Lokale Befehle:** `bash -n` (Syntaxpruefung), `sed -i` (eine Codezeile vor dem Einfrieren, sonst nur Text in
   ERGEBNIS.md), cp, chmod,
   sha256sum, jq, scp/ssh. Python, awk oder perl liefen lokal nicht. Einige Verhaeltnisse und Differenzen in diesem
   Bericht habe ich im Kopf gerechnet (gekennzeichnet "Kopfrechnung"); die tragenden Zahlen stehen in den JSON-Dateien
   der .69.
8. **Auf der .69:** jq (Testklammer im Leitungstest, Auszuege), rm einer Testdatei im eigenen Ordner, mkdir/mv/cp.
   Kein python ausserhalb von kleintest.sh, kein pkill, kein pgrep.
9. **Gelesen:** ~/.ssh/config, nur die ControlMaster-Zeilen (per grep), um das offene ssh zu verstehen. Nicht
   geoeffnet: versiegelte Pfade, Geheimnisdateien, Codex-Dateien.
10. **Nicht erledigt:** keine Peerbus-Nachricht, kein Commit, kein Journaleintrag (Schreibrechte nur in zwei Ordnern;
    das liegt bei der Leitung).
11. **Zeiten:** .69-Stempel in UTC aus Starter und Logs, lokale Zeiten in CEST per date.
    - **Verstoss:** Im Entwurf stand die Startzeit des ersten Lesers geschaetzt ("~19:47"). Der Gegenleser fand das;
      jetzt steht das date-Fenster da.
    - Im Entwurf hiess es auch, beide Nachtraege kaemen "nach Sicht der Hauptwerte". N2 startete aber schon, als im
      Hauptlauf erst Referenz und V1 fertig waren. Jetzt berichtigt.
12. **Unterbrechung:** Sitzungslimit von 19:53:47 bis 21:35:32 CEST (date). Die Zeitbox habe ich nach Vorgabe der
    Leitung um die Pause verlaengert (Rest 43 min 29 s, bis 22:19:01 CEST).
13. **Sitzungsordner:** Die Ausgaben meiner Hintergrund-Befehle und der Gegenleser legt das Werkzeug selbst unter
    /tmp/claude-1000/.../tasks/ ab. In den Scratchpad der Leitung habe ich nichts geschrieben.

## Bedeutung (nach der Vorab-Bedeutung der Karte)

- **DR1 im Kartenwortlaut eingetroffen, nach Plan nicht auswertbar.** Nach Kartenwortlaut ist die Bedeutung "In 3D
  gibt es oberhalb einer Schwellladung einen stabilen Dreifarben-Tropfen; kein Einschluss" ausgeloest; nach Plan
  bleibt DR1 ohne Urteil. Einschraenkungen:
  1. Geprueft sind drei nichttriviale Klassen (tangential/radial mit Anteil aus der Ebene, Farbuebertragung), eine
     reine z-Verschiebung und zwei Rauschstoerungen. Ein Hesse-Spektrum ist das nicht.
  2. Das Schwerpunktmass ist fuer Verschiebungen aus der Ebene in erster Ordnung blind; dort tragen Energie und
     Residuum.
  3. Fluss bei festen Ladungen, keine 3D-Zeitentwicklung.
- **DR2 nicht auswertbar** (Plan und Kartenwortlaut). Keine der beiden Vorab-Bedeutungen ist ausgeloest; ich lese das
  Ergebnis in keine Richtung. Unabhaengig davon zeigt der Nachtrag (beschreibend):
  - Die Entmischung setzt wohl stetig ein: Der Tropfen waechst aus dem Mischball, wo dieser weich wird [Deutung H;
    ein kleiner Sprung zwischen den Stuetzstellen ist nicht ausgeschlossen].
  - Die Schwellladungen sind 3D 600 bis 650 (om ~0,77) und 2D 52,5 bis 53,5 (om ~0,72) [E]. Ueber die Dimension
    waechst Q1* also stark; ein einheitliches om gibt es nicht.
  - **Neue Hypothese [H, M-Skizze, nach Sicht]:** Bei einer Instabilitaet zaehlt die tiefste Entmischungsmode im
    Ball (Drehimpuls 1). Fuer eine harte Kugel mit Neumann-Rand liegt ihre Wellenzahl bei 1,841/R (Scheibe) und
    2,082/R (Kugel). Bei gleicher Entmischungsstaerke im Inneren gaebe das R*_3D/R*_2D ~ 1,13.
    - Das ist eine Skizze ohne die om-Abhaengigkeit der Entmischungsstaerke, nach Sicht entstanden und nicht
      getestet. Pruefen liesse sie sich mit einer linearen Stabilitaetsrechnung des Mischballs (tiefster Eigenwert
      gegen Q1) in 2D und 3D, mit vorab gebundener Vorhersage.
- **Kein Einschluss:** Einzelne Pole sind stabile Q-Baelle, U(1)^3, kein SU(3)-Singulett (wie DREIPOL-2).
- **Lattenbezug:** DR0 und DR1 (Kartenwortlaut) haetten verfehlen koennen. Fuer DR2 im Kartenwortlaut hatte der Plan
  "weitgehend vorab ableitbar" vermerkt (2.4). Messbezug (L5) fehlt; alles ist synthetisch.

**Moegliche Fortsetzung (Entscheidung bei der Leitung):**
- Lineare Stabilitaet des Mischballs: tiefster Eigenwert der Entmischungsmode gegen Q1 in 2D und 3D. Das prueft
  "stetig" direkt und gibt die Schwelle ohne Fluss.
- Teil B neu, mit einem vorab an der gemessenen Sockelhoehe des Gitters gebundenen Konvergenzkriterium und einem
  Feldabstand nach Ausrichtung statt der Schwerpunkte.
- 3D-Zeitentwicklung des Tropfens bei Q1 = 800.

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-192549, EINGEFROREN-SHA256.txt, KARTE.md (Leitung),
  ERGEBNIS.md.vor-gegenlesen (Fassung, die der zweite Gegenleser las)
- **code/:**
  - dreipol2.py (Kopie aus DREIPOL-2, unveraendert), dreipol3.py, auswertung3.py, laeufe-p4000a.sh,
    laeufe-p4000b.sh, je mit .eingefroren-20261004-192549
  - pipe-test.sh (Leitungstest), zeit-test.sh (Laufzeitprobe)
  - Nachtraege (nicht eingefroren): nachtrag3.py, laeufe-nachtrag.sh, laeufe-nachtrag2.sh, nachtrag_aw3.py
- **rauch-69/:** pipe/ (Leitungstest), pipe2/ (Auswertungstest mit Testklammer), zeit/ (Laufzeitprobe),
  pipe-start.log
- **lauf-69/:**
  - auswertung.json (Urteile), auswertung.log, PRUEFSUMMEN.txt
  - bisekt3.json/.log, bisekt2.json/.log, stab3.json/.log, je mit _bilder.npz
  - Bilder: bisektion.png, bisektion_bilder.png, stab3_fluss.png, stab3_bilder.png
  - nachtrag/: N1_3d, N1_2d, stab3_V12, stab3_L12 (je .json, .log, _bilder.npz), nachtrag_aw.json/.log,
    uebergang.png, laeufe-nachtrag.log
- **Auf der .69:** /home/fmh/fmhc-physics-remote/qball-dreipol-3/ (code/, rauch/, lauf/)

## Einfach gesagt

Wir haben gesucht, ab welcher Groesse drei verschiedenfarbige Q-Baelle einen Tropfen mit drei getrennten Farbfeldern
bilden, statt sich zu einem gemischten Ball zu vermengen. In 3D beginnen sich die Farben ab einer Ladung zwischen 600
und 650 je Ball zu trennen, klar getrennt sind sie ab etwa 750; in 2D beginnt es bei etwa 53. Es sieht so aus, als
trennten sich die Farben nach und nach, wie eine Mischung, die sich langsam entmischt; ganz sicher ist das noch
nicht. Der 3D-Tropfen bei Ladung 800 kehrt nach jedem gerechneten Anstupsen in seine Form zurueck, auch wenn man eine
Farbe aus der Ebene schiebt oder Farbe hinueberschiebt; vier Faelle kamen nicht ganz zur Ruhe, vermutlich weil der
Tropfen dabei ganz langsam als Ganzes weiterrutscht. Eine einfache Formel fuer die Schwelle ueber alle Dimensionen
konnten wir so nicht pruefen, weil unsere Suchregel zu frueh stoppte.
