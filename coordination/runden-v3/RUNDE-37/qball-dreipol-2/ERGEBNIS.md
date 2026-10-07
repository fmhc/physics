# QBALL-DREIPOL-2: Ergebnis (Code-Agent, Runde 42, Fast Lane)

- Code-Agent fuer claude-primary. Start 2026-10-04 18:03:51 CEST; ERGEBNIS geschrieben ab 18:42:42 CEST (date).
- **Eingefroren** 18:28:06 CEST: PLAN.md und code/{dreipol2.py, auswertung2.py, laeufe-p4000a.sh,
  laeufe-p4000b.sh}, je als .eingefroren-20261004-182806, Hashes in EINGEFROREN-SHA256.txt.
  - Um 18:33:54 CEST (date in der Sitzung) geprueft: unveraendert. Auf der .69 liefen dieselben Hashes
    (lauf-69/PRUEFSUMMEN.txt).
- **Laeufe** (.69, kleintest.sh, Spuren p4000a und p4000b, torch/CUDA auf Quadro P4000, float64):
  - Hauptlaeufe 16:28:15 bis 16:34:16 UTC, alle rc = 0. Auswertung 16:34:41 bis 16:35:05 UTC.
  - Nachtraege N1 und N2 (nach Sicht der Hauptwerte, ohne Urteil) 16:36:56 bis 16:41:26 UTC.
- **Kennzeichen:** [E] gerechnet im Modell, [M] Mathematik, [P] Projektdatei, [L] Gedaechtnis, [S] Quelle,
  [H] Hypothese.
- Alles ist eine synthetische Rechnung im Modell (Papier-I-Potential mit drei Komponenten). **Keine
  Messdatenbestaetigung.**

## Ergebnis zuerst

1. **Kontrolle bestanden (DP0) [E].**
   - Das 2D-Dreieck ist bitnah nachgebaut: E = 138,83507143701712 wie in DREIPOL-1, Paarabstand 1,2453 R,
     Luecke zum Mischball 0,14562.
   - In 3D weichen Gitter und Radialrechnung um hoechstens 2,3e-7 ab (Schwelle 1e-4).
2. **Das 2D-Dreieck ist ein lokales Minimum in allen geprueften Richtungen (DP1 eingetroffen, Plan und Kartenwortlaut)
   [E].**
   - Alle sechs Stoerungen kehren zurueck: Endabstand < 6,1e-7 R, Energie gleich bis 1,2e-13. Die Ladungsstoerung
     kostete am Start +2,89.
   - Einschraenkungen: P1/P2 waren vorab ableitbar (Symmetrie); L1/L2 sind eine Symmetrieklasse. Das Urteil gilt fuer
     "Ladungsverschiebung im Sektor"; unter der Sektorlesart (L3) waere die 2-%-Schwelle verfehlt.
   - Nachtrag N2 ohne Urteil: Auch 9 Zufallsstoerungen kehren zurueck, bis 20 % Rauschen (+70 Energie) und alle drei
     Klumpen verschoben.
   - Ein volles Hesse-Spektrum ist das nicht.
3. **In 3D endet der Fluss bei g4 = -0,1 in einem festen Dreieck unter dem Mischball (DP2 eingetroffen, Plan und
   Kartenwortlaut) [E].**
   - Q1 = 2500: E = 5603,02 gegen 5715,46 fuer den Mischball, Paarabstand 1,48 R, Reinheit 0,87 bis 0,89.
   - **Selbstanzeige:** Bei Q1 = 2500 war das energetisch erzwungen, weil schon der Start (5667,28) unter dem Mischball
     lag. Erkannt habe ich das erst nach dem Lauf (Selbstanzeige 1).
   - Nachtrag N1 ohne Urteil: Bei Q1 = 800 bildet sich das Dreieck auch dort, wo das Verschmelzen moeglich waere
     (3,32 unter dem Mischball). Bei Q1 = 400 und 200 verschmelzen die drei Pole.
   - In 3D ist das Dreieck also ein Effekt grosser Ladung.
4. **Der schiefe Dreier bleibt bis t = 300 beisammen (DP3 eingetroffen; Plan bei g4 = +0,1, Kartenwortlaut bei
   beiden g4) [E].**
   - 4 von 4 Saaten. Groesster Polabstand zur Mitte 1,30 R, das ist die Startlage (Ausstossgrenze 4 R).
   - Kleinster Ladungsanteil im Haufen 0,947 (+0,1) bzw. 0,990 (-0,1).
   - Der Dreier pulsiert mit Periode 38 (+0,1) bzw. 66 (-0,1).
   - Einschraenkungen:
     - Bei g4 = -0,1 war "kein Ausstoss" vorab ableitbar (Plan 2.7).
     - Die vier Saaten verlaufen fast gleich; das Rauschen 1e-3 spielt neben der Schieflage keine Rolle.
     - Bei +0,1 sinkt der Ladungsanteil stetig weiter.
5. **Gestalt [E]:** Das "Dreieck" ist ein kompakter Tropfen mit drei einfarbigen Sektoren, kein Dreier aus drei
   getrennten Baellen (Bilder teilA_bilder.png, teilB_3d.png).
   - Auch zwei Farben verschmelzen bei g4 = -0,1 in 2D nicht ganz: Schwerpunkte 0,79 R auseinander, 0,03 unter dem
     Mischpaar (S.json).
6. **Bedeutung [H]:** Die Kartenbedeutung "DP1 und DP2 treffen ein" ist ausgeloest, mit Einschraenkungen.
   - Bei g4 < 0 entmischen sich drei Farben zu einem festen Dreifarbentropfen. In 2D ist er bei Q1 = 60 vorhanden, in
     3D nur ab einer Ladung zwischen 400 und 800.
   - Es gibt keinen Einschluss: Ein einzelner Pol ist stabil, die Ladungen sind U(1)^3.
   - Die 3D-Stabilitaet ausserhalb des symmetrischen Unterraums ist nicht geprueft.

## Urteile (mechanisch, lauf-69/auswertung.json; Vorhersagen der Karte unveraendert)

| Nr | Vorhersage (Karte) | Wahrsch. | Plan | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| DP0 | Kontrolle: 2D-Dreieck nachgebaut (1,245 R auf 2 %, Luecke 0,146 auf 10 %); 3D-Gitter gegen 3D-radial auf 1e-4 | 85 % | **eingetroffen** | **eingetroffen** | 2D: Paarabstand 1,24529 R (Abw. 2,4e-4), Luecke 0,145617 (Abw. 0,26 %), 1050 Schritte. 3D: Einpolball 2,28e-7 / 0,94e-7, Mischball 1,24e-7 / 0,91e-7 (g4 = -0,1 / +0,1) |
| DP1 | Das 2D-Dreieck ist ein lokales Minimum: alle 6 Stoerungen kehren zurueck (Endabstand < 2 % R, Energie gleich auf 1e-3) | 45 % | **eingetroffen** | **eingetroffen** | V1, V2, L1, L2 nach 1500 bis 1550 Schritten konvergiert: d_rms <= 3,4e-7 R, d_form <= 6,1e-7 R, abs(dE) = 1,1e-13. P1, P2 bei Schritt 0 (exakte Symmetrie, vorab ableitbar) |
| DP2 | In 3D endet der Fluss bei g4 = -0,1 in einem festen Dreieck aus drei einfarbigen Klumpen unter dem 3D-Mischball | 30 % | **eingetroffen** | **eingetroffen** | Q1 = 2500, N = 80: konvergiert nach 1050 Schritten, Paarabstand 1,482 R, Reinheit 0,869 bis 0,890. E_Ende - E_Misch = -112,44 (Gitter) / -112,44 (radial). **Weitgehend vorab ableitbar:** E_Start - E_Misch = -48,17 (Selbstanzeige 1) |
| DP3 | Der schiefe 2D-Dreier bleibt beisammen: >= 3 von 4 Saaten bis t = 300 ohne Ausstoss und je Pol >= 90 % im Haufen | 55 % | **eingetroffen** (g4 = +0,1; Nebenurteil -0,1 ebenfalls eingetroffen) | **eingetroffen** (beide g4) | g4 = +0,1: 4/4, max Abstand 1,296 R (Startlage; ab t = 5 hoechstens 1,20 R), min Anteil (alle t) 0,9474, bei t = 300: 0,947 bis 0,962. g4 = -0,1: 4/4, 1,296 R (Startlage; ab t = 5 hoechstens 1,27 R), 0,9900; "kein Ausstoss" vorab ableitbar. dE/E <= 2,9e-6, dQ <= 1,2e-15 |

- **DP1, Lesart:** Phasenversatz heisst gleichfoermiger Versatz je Komponente. Ladungsverschiebung heisst Uebertragung
  im Sektor, alle Q_a bleiben 60. Endabstand heisst Formabstand (Plan 9a).
  - Die Sektorlesart L3 (Q = 63/57/60) stand vorab ausserhalb des Urteils, weil sie ein anderer Ladungssektor ist (Plan
    9a.2). Sie endet in einem nahen, schiefen Dreieck: d_rms 0,038 R, d_form 0,062 R, dE -0,0079.
  - **Lesartabhaengigkeit (nach Sicht):** Haette "Ladungsverschiebung" die Sektorlesart bedeutet, waere DP1 an der
    2-%-Schwelle gescheitert. Die Abweichung ist kein Weglaufen: Der Fluss findet das nahe Gleichgewicht des neuen
    Sektors. Das Urteil "eingetroffen" gilt also fuer die Lesart im Sektor.
- **DP2, Feinlauf** (N = 96, h = 0,5, ohne Urteil): gleiche Gestalt, E_Ende 5603,019550 gegen 5603,019548
  (Differenz 1,6e-6), Paarabstand 10,18935 in beiden Laeufen.
- **DP3:** Den Vermerk "kein Ausstoss bei g4 = -0,1 vorab ableitbar" schreibt die Auswertung mechanisch aus S.json.
  E_Start 139,745 liegt 0,656 unter der kleinsten Ausstossschwelle.

## Tabellen

### A. Teil A (2D, g4 = -0,1, Q1 = 60, L = 64, N = 256; Bilder teilA_fluss.png, teilA_bilder.png)

**Referenz:** E_ref = 138,83507143700376 (Residuum 8,1e-10), Paarabstand 1,245288 R, R = 3,17582. Mischball Q = 180:
138,98068828929 (Gitter gegen radial 1,5e-7; DREIPOL-1 a.json 138,98068828929456).

| Stoerung | Start: d_rms / d_form (R), dE | Ende: d_rms / d_form (R), dE | Schritte | Plan | Kartenwortlaut |
|---|---|---|---|---|---|
| V1 Pol 1 um 0,15 R tangential | 0,0500 / 0,0814, +0,0533 | 3,3e-7 / 5,4e-7, 1,1e-13 | 1500 | zurueck | zurueck |
| V2 Pol 2 um 0,15 R radial | 0,0707 / 0,1319, +0,1045 | 3,2e-7 / 6,0e-7, 1,1e-13 | 1500 | zurueck | zurueck |
| L1 5 % Farbe 2 nach Klumpen 1 | 0,1009 / 0,2300, +2,888 | 3,0e-7 / 4,9e-7, 1,1e-13 | 1550 | zurueck | zurueck |
| L2 5 % Farbe 1 nach Klumpen 2 | 0,1009 / 0,2300, +2,888 | 3,0e-7 / 4,9e-7, 1,1e-13 | 1550 | zurueck | zurueck |
| P1 Phase Komp. 2 um pi/2 | 4e-16 / 0, 0 | gleich | 0 | zurueck (ableitbar) | zurueck |
| P2 Phasen 2pi/3, 4pi/3 | 4e-16 / 1e-16, 0 | gleich | 0 | zurueck (ableitbar) | zurueck |
| L3 Sektor 63/57/60 (ohne Urteil) | 0 / 0, +0,0086 | 0,0385 / 0,0623, -0,0079 | 1500 | (nicht zurueck) | (nicht zurueck) |

- L1 und L2 liefern am Start dieselben Abstaende und Energien (bis 1e-16), am Ende dieselben bis auf Rundungsrauschen.
  Die Reinheiten am Start sind zwischen den Farben vertauscht (L1 0,624 / 0,578 / 0,661, L2 0,577 / 0,632 / 0,654).
  Beides passt zur Symmetrieklasse (Plan 2.4).
- Der Abstand faellt in allen vier nichttrivialen Faellen exponentiell, ohne Zwischenanstieg (teilA_fluss.png).
- **Reinheit** (eigene Voronoi-Zelle, |psi_a|^2) im Dreieck, Komponenten 1 / 2 / 3: 0,649 / 0,656 / 0,641.
  - Rund 35 % jeder Farbe liegen in fremden Zellen; die Klumpen ueberlappen stark.
  - Die Streuung um 1 % trotz Symmetrie kommt vermutlich von der Zellgrenze auf dem Gitter: Ein Gleichstand auf der
    Achse x = 0 geht an Komponente 2 [H].

### B. Teil B (3D, Q1 = 2500, L = 48, N = 80; Bild teilB_3d.png)

| g4 | E_1 (om, R_halb) | 3 E_1 | E_Start (beruehrend) | E_Misch Gitter / radial | E_Ende | Gestalt | Paarabstand | Reinheit |
|---|---|---|---|---|---|---|---|---|
| -0,1 | 1902,2643 (0,7144; 6,875) | 5706,79 | 5667,28 | 5715,4568 / 5715,4561 | **5603,02** | Dreieck | 1,482 R | 0,869 bis 0,890 |
| +0,1 | 2157,9410 (0,8302; 6,878) | 6473,82 | 6417,32 | 5999,9948 / 5999,9943 | 5999,9948 | verschmolzen | < 1e-16 R | (entfaellt) |

- Bei g4 = -0,1 liegt der Mischball **ueber** drei getrennten Baellen (+8,66).
  - Grund [M]: Bei g4 < 0 ist im Inneren eines einfarbigen Balls die Energie je Ladung kleiner. Die Duennwandgrenze
    ist om_c = 0,628 gegen 0,683 gemischt.
  - Bei Q1 = 2500 (duenne Wand) ueberwiegt dieser Volumenterm die Oberflaeche.
  - In 2D bei Q1 = 60 lag der Mischball dagegen 6,6 unter 3 E_1. Dort war das Dreieck also nicht erzwungen
    (DREIPOL-1).
- Bei g4 = +0,1 verschmilzt der Dreier wie in 2D zum gleich gemischten Ball (E_Ende - E_Misch = 4,5e-8).

### B'. Nachtrag N1 (ohne Urteil, nach Sicht): 3D-Dreiecksfluss bei g4 = -0,1 und kleinerer Ladung

Eingefrorener Code, nur andere Argumente (code/laeufe-nachtrag-3d.sh, N = 80, L = 36/40/48). Bild:
lauf-69/nachtrag/teilB_ladungsreihe.png.

| Q1 | om | R_halb | 3 E_1 | E_Misch | E_Start - E_Misch | Flussende | E_Ende - E_Misch | Paarabstand |
|---|---|---|---|---|---|---|---|---|
| 200 | 0,844 | 2,40 | 566,53 | 525,83 | +24,84 | verschmolzen | +3e-9 | 3e-5 R |
| 400 | 0,794 | 3,29 | 1055,24 | 1001,31 | +33,94 | verschmolzen | +1e-8 | 6e-5 R |
| 800 | 0,757 | 4,42 | 1982,22 | 1923,31 | +32,94 | **Dreieck** | **-3,32** | 1,093 R |
| 2500 | 0,714 | 6,87 | 5706,79 | 5715,46 | **-48,17** | Dreieck | -112,44 | 1,482 R |

- Bei Q1 = 800 haette der Fluss den Mischball erreichen koennen (Start 32,9 darueber). Er endet trotzdem im Dreieck,
  3,32 (0,17 %) tiefer.
  - Das ist der nichttriviale Fall, wie in 2D bei Q1 = 60.
- Die Schwelle zwischen Verschmelzen und Dreieck liegt in 3D zwischen Q1 = 400 (om = 0,794) und 800 (om = 0,757).
- In 2D ist nur Q1 = 60 (om = 0,715) gerechnet; dort gibt es das Dreieck. Wo die 2D-Schwelle liegt, ist offen.

### C. Teil C (2D, echte Zeit, T = 300; Bilder teilC_dynamik.png, teilC_bilder.png)

Start: Grunddreieck d0 = 2R, Pol 1 mit Abstand 1,1 d0 zu Pol 2 und 3, Pol 2 mit Q = 57. Klumpengebiet R_K = 4,15 R.

| g4 | Saaten gueltig / beisammen | max Abstand Pol-Mitte | min Q_a,in/Q_a (alle t) | Q_a,in/Q_a bei t = 300 | Mittendurchgaenge | Periode | dE/E |
|---|---|---|---|---|---|---|---|
| +0,1 | 4 / 4 | 1,296 R (Start); ab t = 5: 1,20 R | 0,9474 | 0,947 bis 0,962 | 8 (t = 20; 59; 98,5; ...; 288) | 38,3 | 2,55e-6 |
| -0,1 | 4 / 4 | 1,296 R (Start); ab t = 5: 1,27 R | 0,9900 | 0,990 bis 0,992 | 4 (Saat 1: t = 33; 98,5; 164,5; 229,5) | 65,5 bis 65,7 | 2,86e-6 |

- Der groesste Polabstand zur Mitte ist in allen acht Laeufen die Startlage (Pol 1 liegt 10 % weiter aussen).
- Die vier Saaten stimmen in Ladungsanteilen, Polabstand, Energie und Periode bis in die dritte Stelle ueberein. Nur
  die Paarabstaende bei t = 300 (g4 = -0,1) streuen in der zweiten Stelle (0,155 bis 0,172 R bzw. 0,319 bis 0,333 R).
  - Die Schieflage ist deterministisch; das Rauschen 1e-3 setzt keinen eigenen Zerfallsweg in Gang.
- Bei g4 = -0,1 liegen die Mittendurchgaenge der Saaten 2 und 3 teils 0,5 spaeter (165,0; 230,0).
- **Energiebilanz (S.json, Plan 2.7):**
  - +0,1: E_Start 153,737 liegt 2,31 bzw. 2,17 ueber den Ausstossschwellen. Ein Ausstoss war erlaubt, trat aber
    nicht ein; die Pole kamen nie ueber 1,3 R hinaus.
  - -0,1: E_Start liegt 0,656 unter der kleinsten Schwelle, also war kein Ausstoss moeglich.
- **Pulsation:**
  - Die Pole laufen wie in DREIPOL-1 durch die Mitte und stehen danach als umgekehrtes Dreieck.
  - Bei +0,1 ist die Schwingung von Anfang an unregelmaessig. Der mittlere Paarabstand startet bei 2,13 R; seine Maxima
    liegen bei 1,71 / 1,49 / 1,83 / 1,64 / 1,31 / 1,37 / 1,42 R (t = 38 bis 274,5).
    - Die letzten beiden Durchgaenge (t = 255,5 und 288) sind nur flache Minima (0,42 bzw. 0,87 R). Nur die ersten
      sechs laufen wirklich durch die Mitte.
  - Bei -0,1 bleibt sie regelmaessig (Maxima 2,04 / 2,12 / 1,95 / 2,06 R).
- **Ladungsverlust:** Bei +0,1 verlaesst Ladung das Klumpengebiet laufend (5,3 % bis t = 300).
  - Eine deutliche Stufe gibt es nur beim ersten Mittendurchgang (t ~ 20: 0,7 %). Danach geht zwischen den Durchgaengen
    etwa ebenso viel verloren wie an ihnen (Gegenleser, Saat 1, Pol 2).
  - Linear fortgesetzt waere die 90-%-Grenze um t ~ 550 bis 600 erreicht [H, Extrapolation, nicht gerechnet].

### D. Nachtrag N2 (ohne Urteil, nach Sicht): 2D-Dreieck mit Zufallsstoerungen (code/nachtrag2.py)

Glattes komplexes Rauschen (k_c = 2) auf allen drei Komponenten, Amplitude 5 % bzw. 20 % der lokalen Feldstaerke. In
der dritten Form zusaetzlich jeder Klumpen um 0,15 R in zufaellige Richtung verschoben. Saaten 11, 12, 13.

| Art | Start: d_rms / d_form (R), dE | Ende (alle drei Saaten) | Schritte |
|---|---|---|---|
| Rauschen 5 % | 0,010 bis 0,019 / 0,022 bis 0,047, +3,9 bis +4,2 | d_rms <= 4,1e-7, d_form <= 7,7e-7, dE <= 1,8e-13 | 1250 bis 1300 |
| Rauschen 20 % | 0,072 bis 0,094 / 0,169 bis 0,194, +69,3 bis +71,6 | d_rms <= 4,2e-7, d_form <= 7,4e-7, dE <= 2,3e-13 | 1400 bis 1500 |
| Verschiebung 0,15 R + 5 % | 0,022 bis 0,084 / 0,034 bis 0,204, +3,9 bis +4,3 | d_rms <= 3,9e-7, d_form <= 7,1e-7, dE <= 1,8e-13 | 1400 bis 1500 |

- Alle 9 Fluesse sind konvergiert (Residuum < 1e-8) und kehren zum selben Dreieck zurueck.
- Das stuetzt "lokales Minimum" ueber die sechs gewaehlten Richtungen hinaus, bleibt aber eine Stichprobe.

## Kontrollen

- **Portierung:** 2D-Einpolball torch gegen DREIPOL-1 (numpy): relativ 2,2e-16 (rauch-69/r1.json).
  - Mischball 2D gegen DREIPOL-1 a.json: 4e-16 relativ. Nachbau-Dreieck: E gleich in allen 17 Stellen.
- **Gitter 3D** (r2, Einpolball Q = 2500): N = 80 gegen 128: 2,3e-9; N = 96 gegen 128: 2,5e-12. Dreiecksfluss N = 80
  gegen 96: 3e-10 relativ.
- **Erhaltung in Teil C:** Ladung je Komponente <= 1,2e-15, Energie <= 2,9e-6 (Tor 1e-3).
- **Konvergenz:** alle Fluesse mit Residuum unter der Toleranz (2D 1e-7 bis 1e-9, 3D 1e-6). Radiale Bezuege
  Residuum <= 7,4e-12.
- **Schwellenlauf:** S (eingefrorener Code) gleich r3 (vor dem Einfrieren) in allen Stellen.

## Gegenlesen (frischer Leser, nur lesend, 18:47 bis 19:01 CEST)

- Der Leser hat alle Zahlen gegen die Rohdaten geprueft, in beiden Richtungen. **Urteile:** Alle vier, dazu
  Nebenurteil und Vermerke, stimmen mit auswertung.json. Alle Status lauten "konvergiert" bzw. "fertig".
- **A-Befund, berichtigt:** Bei g4 = +0,1 stand "nach t = 150 nur noch 1,3 bis 1,6 R statt 2,1 R".
  - 2,13 R ist nur der Startwert; schon die erste Schwingung erreichte 1,71 R.
  - Neu in Tabelle C: Maxima einzeln aufgefuehrt, Unregelmaessigkeit von Anfang an.
- **B-Befunde, berichtigt:**
  - Ladungsverlust laufend statt "stufig"; eine Stufe gibt es nur beim ersten Durchgang.
  - Saaten nicht durchweg gleich bis zur dritten Stelle: Die Paarabstaende bei t = 300 (g4 = -0,1) streuen in der
    zweiten.
  - Laufzeiten getrennt nach Rechenzeit und Einheitenlaufzeit; S lief 89 s statt "< 1 min".
- **C-Befunde, berichtigt:**
  - Obergrenzen nach oben gerundet (3,4e-7 / 6,1e-7 / 1,2e-15 sowie die N2-Tabelle)
  - Polabstand 1,296 R als Startlage gekennzeichnet
  - Mittendurchgaenge mit Saatangabe
  - Reinheit nach Komponenten geordnet
  - L1/L2: Reinheiten vertauscht statt "dieselben Zahlen"
  - "6 + 9 Richtungen" ersetzt durch "drei Klassen und 9 Zufallsstoerungen"
  - "Einfach gesagt" auf Stoerungen ohne Ladungsaenderung eingeschraenkt
  - Dateiliste ohne S_bilder.npz
  - Zeitangaben, die nur aus der Sitzung stammen, als solche markiert
- Die Fassung vor dem Gegenlesen liegt als ERGEBNIS.md.vor-gegenlesen daneben.
  - Danach geaenderte Saetze hat kein weiterer frischer Leser gelesen.

## Selbstanzeigen

1. **Ableitbarkeitsprobe fuer DP2 unvollstaendig (nach dem Lauf erkannt):**
   - In 3D bei g4 = -0,1 und Q1 = 2500 liegt der Mischball ueber drei getrennten Baellen. Das zeigen schon die
     radialen Loesungen (5715,46 gegen 5706,79); der beruehrende Start liegt mit 5667,28 noch tiefer.
   - Der Fluss senkt E stetig. Er konnte den Mischball also nie erreichen, und "unter dem Mischball" war erzwungen.
   - Mit erhaltener D3-Symmetrie blieb fast nur ein Dreieck als Ende. Offen waren allein Konvergenz, die Grenze
     min D > R und die Reinheit.
   - Die Karte nennt den radialen Vergleich ausdruecklich. Den radialen 3D-Mischball habe ich vor dem Plan nicht
     gerechnet (Sekundensache); im Plan 2.6 steht deshalb faelschlich "nicht ableitbar".
   - DP2 ist damit weitgehend vorab ableitbar. Der nichttriviale Fall steht nur im Nachtrag N1 (Q1 = 800), ohne
     Urteil.
2. **Python auf der .69 ausserhalb von kleintest.sh:** Beim Pruefen des Leitungstests (kurz nach 16:25:06 UTC, date
   in der Sitzung) lief einmal `~/fmhc-physics-gpu-venv/bin/python -c pass` direkt. Es war ein Versehen ohne Rechnung,
   aber gegen die Regel.
3. **Fehlstart Spur b:** Startbefehl und `mv` des Laufskripts standen im selben Befehl. Der Start kam vor dem `mv`
   (Startbefehl 16:28:15 bis 16:28:17 UTC laut A.log und date-Ausgabe; Fehlermeldung "No such file" in
   lauf-69/start-b-fehlstart.log).
   - Neustart 16:30:25 UTC, ohne Folgen fuer die Werte.
4. **ssh offen gehalten:** Zweimal hielt ein Hintergrund-ssh die Verbindung, bis die Einheit fertig war. Das waren der
   Neustart von Spur b (~4 min) und der Start von N2 (~2 min). Dazu kamen die Warteschleife und kurze Abfragen; kurz
   koennen vier Verbindungen gleichzeitig offen gewesen sein.
5. **Reihenfolge:** Code, r1, r2, r3 und der Leitungstest liefen vor dem Plantext (im Plan offen gelegt).
   - Gesehen habe ich Einzelball-Werte, Zeiten, die Schwellen fuer DP3 und die Urteilsfelder der Testauswertung mit
     Fremdwerten. Hauptwerte habe ich nicht gesehen.
6. **Nachtraege nach Sicht:** N1 (3D, Q1 = 200/400/800), N2 (Zufallsstoerungen) und das Nachtragsbild entstanden nach
   den Hauptwerten.
   - Neuer, nicht eingefrorener Code: code/nachtrag2.py, code/nachtrag_bild.py, code/laeufe-nachtrag-3d.sh. Hashes in
     lauf-69/PRUEFSUMMEN.txt.
   - Sie aendern kein Urteil. Die Kartenwahrscheinlichkeiten bleiben unberuehrt.
7. **DP1 testet weniger Klassen, als die Zahl sechs nahelegt:** P1/P2 waren trivial, L1/L2 sind eine Symmetrieklasse
   (beides im Plan vorab genannt). Nichttrivial sind drei Klassen: tangential, radial und Farbuebertragung.
8. **DP3:**
   - Die vier Saaten sind praktisch ein Test (Abweichungen meist erst in der dritten Stelle).
   - Die Ausstossgrenze 4 R aus der Karte wurde nie annaehernd erreicht. Der Hoechstwert 1,30 R ist die Startlage;
     danach hoechstens 1,27 R.
   - Bei g4 = -0,1 war "kein Ausstoss" vorab ableitbar (Plan 2.7).
9. **Lokale Befehle:** `bash -n` (Syntaxpruefung der Laufskripte) und `sed -i` (Codebearbeitung) liefen auf dem
   Laptop. Python, awk oder perl liefen lokal nicht.
10. **Laufzeiten im Plan:**
    - Die Obergrenzen (bis 8,5 min) lagen weit ueber den echten Laufzeiten. Die Rechenzeit laut JSON (sek) lag bei 8,1
      bis 61,7 s, die Einheitenlaufzeit mit torch/CUDA-Start bei 11 s bis 1 min 29 s.
    - Ausnahme: Der Schwellenlauf S stand im Plan mit "< 1 min" und lief als Einheit 89 s (Rechenzeit 23 s).
    - Die Wandzeiten haben nirgends gegriffen.
11. **Nicht geoeffnet:** Versiegeltes (VERSIEGELT, vertraege-20260925, KS-1, T8-SOLL, ks-1-dk-*), Geheimnisdateien und
    Codex-Dateien. Gelesen habe ich DREIPOL-1 und AGENTS.md (Abschnitt Dimensionsvergleich).
12. **Nicht erledigt:** keine Peerbus-Nachricht, kein Commit, kein Journaleintrag. Die Schreibrechte waren auf zwei
    Ordner begrenzt; das liegt bei der Leitung.
13. **Zeiten:** .69-Stempel in UTC aus der Starter-Ausgabe, lokale Zeiten in CEST per date.
14. **Sitzungsordner und Scratchpad:**
    - Die Ausgaben meiner Hintergrund-Befehle legt das Werkzeug selbst unter /tmp/claude-1000/.../tasks/ ab
      (Warteschleifen, ssh-Rueckgaben, Gegenleser).
    - **Verstoss:** Um 18:51 CEST habe ich eine Hilfsdatei (remote-npz.sha, Hashliste der Bilder und npz-Dateien der
      .69) in den Scratchpad der Sitzung geschrieben. Das ist der Scratchpad der Leitung.
    - Ich habe sie um 18:51:33 CEST wieder geloescht (rm, date). Inhalt: nur Hashes, die auch in
      lauf-69/PRUEFSUMMEN.txt stehen; alle 15 stimmten.
15. **Gegenlesen:** Ein frischer Gegenleser (Unteragent, nur lesend) hat die Zahlen dieses Berichts gegen die Rohdaten
    geprueft; Befunde und Korrekturen stehen im Abschnitt "Gegenlesen".

## Bedeutung (nach der Vorab-Bedeutung der Karte)

**"DP1 und DP2 treffen ein" ist ausgeloest.** Die Karte sagt dazu: Im Q-Ball-Modell gibt es einen echten Dreier aus
drei "Farben", der weder verschmilzt noch zerfaellt; Kandidat fuer Finns Drei-Pol-Teilchen, aber kein Farbeinschluss.
Dazu fuenf Einschraenkungen:

1. **Gestalt [E]:** Der Dreier ist ein kompakter Tropfen aus drei einfarbigen Sektoren mit gemeinsamen Grenzflaechen,
   eher ein "Mercedes-Stern" als drei Baelle.
2. **Mechanismus [M, H]:** Bei g4 < 0 ist das Innere einer reinen Farbe energetisch billiger als ein gemischtes.
   - Der Tropfen entmischt sich, sobald dieser Volumengewinn die Kosten der Grenzflaechen uebersteigt.
   - Das gilt nicht nur fuer drei Farben: Zwei Farben verschmelzen in 2D ebenfalls nicht ganz (Schwerpunkte 0,79 R
     auseinander; S.json).
   - Die Drei ist damit nicht ausgezeichnet.
3. **Dimensionsvergleich (AGENTS.md):**
   - 2D: Bei Q1 = 60 ist das Dreieck ein lokales Minimum in drei nichttrivialen Stoerungsklassen und 9
     Zufallsstoerungen [E]. Das Verschmelzen waere energetisch moeglich gewesen.
   - 3D: Das Dreieck gibt es erst ab einer Ladung zwischen 400 und 800. Darunter verschmelzen die Pole [E, Nachtrag].
   - In 3D ist nur die Existenz als Fixpunkt des symmetrischen Flusses gezeigt (Spiegelung z -> -z und D3 bleiben
     erhalten). Ein Stabilitaetsnachweis in 3D fehlt.
   - Allgemein gilt die Duennwand-Ueberlegung (Volumen gegen Oberflaeche) [M]. Wo die Schwelle liegt, haengt von der
     Dimension ab.
4. **Kein Einschluss:** Einzelne Pole sind stabile Q-Baelle, die drei Ladungen sind getrennt erhaltene U(1). Es gibt
   kein SU(3) und kein Singulett.
5. **Dynamik [E]:** Der schiefe Dreier bleibt beisammen und atmet weiter.
   - Bei g4 = +0,1 (Ausstoss erlaubt) blieb er bis t = 300 beisammen, verliert aber stetig Ladung als Strahlung.
   - Der Endzustand bei langer Zeit ist offen.

**Moegliche Fortsetzung (Entscheidung bei der Leitung):**
- 3D-Stabilitaet bei Q1 = 800 ohne Symmetriezwang: Zufallsstoerungen wie N2, dazu eine 3D-Zeitentwicklung.
- Die 2D-Ladungsschwelle des Dreiecks bestimmen.
- Teil C bis t ~ 600 bei g4 = +0,1, um den 90-%-Schnitt zu sehen.

**Lattenbezug:** DP1 bis DP3 haetten verfehlen koennen. DP2 nur eingeschraenkt (Selbstanzeige 1), DP3 bei g4 = -0,1
nur beim 90-%-Kriterium. L5 (Messbezug) fehlt; alles ist synthetisch.

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-182806, EINGEFROREN-SHA256.txt, KARTE.md (Leitung)
- ERGEBNIS.md.vor-gegenlesen (Fassung vor dem Gegenlesen)
- **code/:**
  - dreipol2.py, auswertung2.py, laeufe-p4000a.sh, laeufe-p4000b.sh, je mit .eingefroren-20261004-182806
  - pipe-test.sh (Leitungstest), dreipol-vorlage-qd1.py (Kopie der eingefrorenen DREIPOL-1-Vorlage)
  - Nachtraege: nachtrag2.py, nachtrag_bild.py, laeufe-nachtrag-3d.sh (nicht eingefroren)
- **rauch-69/:**
  - r1.json/.log (Portierung, 3D-Radialabtastung), r2.json/.log (3D-Gitterprobe), r3_schwellen.json/.log
  - pipe/ (Leitungstest mit Fremdwerten)
- **lauf-69/:**
  - auswertung.json (Urteile), PRUEFSUMMEN.txt
  - A.json, B_m01.json, B_p01.json, B_m01_fein.json, C_p01.json, C_m01.json, S.json, je mit Log und (ausser S.json)
    mit _bilder.npz
  - Bilder: teilA_fluss.png, teilA_bilder.png, teilB_3d.png, teilC_dynamik.png, teilC_bilder.png
  - nachtrag/: B_m01_Q200/400/800.json (+ Log, npz), N2.json/.log, teilB_ladungsreihe.png
- **Auf der .69:** /home/fmh/fmhc-physics-remote/qball-dreipol-2/ (code/, rauch/, lauf/)

## Einfach gesagt

Wir haben drei verschiedenfarbige Q-Baelle zusammengelegt, die lieber unter sich bleiben (g4 negativ). In 2D bilden
sie einen runden Tropfen mit drei farbigen Teilen, der nach jedem Anstupsen ohne Ladungsaenderung genau in dieselbe
Form zurueckkehrt, auch nach Verschieben, Hinueberschieben von Farbe und kraeftigem Rauschen. In 3D gibt es denselben
Dreifarbentropfen nur, wenn die Baelle gross genug sind; kleine Baelle verschmelzen zu einem gemischten Ball, und bei
der zuerst gewaehlten Groesse war das Ergebnis schon vorher aus den Energien klar. Stoesst man den Dreier schief an,
schwingt er hin und her, wirft aber bis zum Ende der Rechnung keinen Ball hinaus. Das sieht aus wie ein Teilchen aus drei Bausteinen, ist aber
kein Quark-Einschluss, denn jeder Ball kann auch allein bestehen.
