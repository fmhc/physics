# PACHNER-TAKT-1 mit TAKT-KOMMUTATOR-1: Ergebnis (Code-Agent fuer die Leitung, Runde 41/42, explorativ)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 17:01:54 CEST. Plantext ab 17:21:59 CEST, vor jeder Rechnung.
  - Rauchlaeufe r1 15:31:42 bis 15:31:45 UTC, r2 15:32:47 bis 15:32:56 UTC, r3 (ganze Kette klein) danach
    (PLAN Abschnitt 3; gelesen nur technische Kontrollen, Zeiten, Schluessel).
  - Eingefroren 2026-10-04 17:34:34 CEST: PLAN.md.eingefroren-20261004-173434 (sha256 8a4586f4...), code/pt.py
    (bc360991...), code/pt_auswertung.py (1f41ab03...); Liste in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 15:35:06 bis 15:41:37 UTC, alle rc = 0 (laengster Lauf T4 mit 261 s, groesster Speicher 2,2 GB bei
    T3-B); Auswertung 15:42:01 bis 15:42:02 UTC. Alle acht Eingaben der Auswertung nennen pt.py bc360991...; die 18
    Dateien in lauf-69/PRUEFSUMMEN.txt stimmen lokal.
  - Nachtrag (beschreibend, kein Urteil) 15:44:36 bis 15:45:55 UTC. Text ab 17:47:22 CEST; Gegenlesen 17:50:48 bis
    18:02:52 CEST, Berichtigung danach (Abschnitt 11).
- Alle Zahlen sind Gitterrechnungen auf der .69 (euklidisches linearisiertes Regge nach Hoehn), keine Messdaten.
- **Kennzeichen:** [M] vorab ableitbar, [S] an der Quelle gelesen, [P] Projektdatei, [E] hier gerechnet,
  [F] Festlegung im Plan, [L] Literatur aus dem Gedaechtnis, [H] Hypothese. "von Hand" = aus den JSON-Werten mit
  Taschenrechner-Arithmetik, nicht im Code.
- **Begriffe:**
  - Netz: eine B1-Kopie (fcc-Stabnetz der Kopie 1), Oktaeder je mit einer Diagonale; V Ecken, E = 7 V Kanten.
  - Zeltstange: eine Ecke wird durch eine spaetere Kopie ersetzt (Takt je Ecke, Lapse).
  - TT = nur Zeltstangen; B = TT plus 1-4/4-1 in jedem Auf-Tetraeder; C2 = TT plus Flip-Flop der Oktaederdiagonalen
    (2 Wechsel je Oktaeder und Takt); C3 = TT plus Rundlauf (3 Wechsel). Ein Takt = vier Klassenschritte (PLAN 1.5).
  - r = Rang des effektiven Lagrange-Zweiforms zwischen Anfangs- und Endflaeche = Zahl der propagierenden
    Konfigurations-Gravitonen im Sinn von Hoehn (Abschn. 4 und 9 [S]); G = Eichrang auf der Flaeche.
  - D = Kommutator: Abstand der Randimpulse zweier Zeltzug-Reihenfolgen AB und BA bei gleichen Randlaengen.

## 1. Ergebnis zuerst

1. **Reiner Diagonalwechsel auf festen Ecken ist kein Takt [M]; mit Zeltstangen laesst er sich bauen [E].** Der
   Rueckwechsel braucht einen Simplexwinkel ueber pi (hier 4,158 rad), und nie koennen alle Oktaeder zugleich von
   derselben Diagonalrichtung auf dieselbe andere wechseln (Summenregel 5e-15, also null). Ein Wechsel ist genau dann
   vorwaerts, wenn die neue Diagonale hoeher liegt als die alte [M, PLAN 1.3]; der Flip-Flop muss also von den
   Zeltstangen gesteuert werden. So gebaut (C2) ist der Takt geometrisch realisierbar: flach (Innen-Fehlwinkel
   <= 1,8e-15) mit lauter positiven 4-Volumen [E].
2. **Durch einen und zwei C2-Takte propagieren alle E - G Groessen [E].** Das sind 3 je Zelle plus 4 globale, wie beim
   reinen Zeltstangen-Takt; ausser der Eichung gibt es dort keine Zwangsbedingung (Luecke im Spektrum >= 4,3e6). Lesart
   nach Hoehns Fallunterscheidung [H]: Die 3-2-Zuege legen die frischen Gravitonen der 2-3-Zuege fest (Fall b), statt
   alte zu vernichten (Fall a); gerechnet ist nur der Rang der ganzen Schicht, nicht je Zug. B veraendert gegenueber
   dem Zeltstangen-Takt nichts (0 Gravitonen dazu). PT2 trifft nach der Plan-Regel ein.
3. **PT1 nach Plan nicht eingetroffen [E].** Bei drei Takten fiel der Rang unter der vorab festgelegten Schwelle 1e-9
   auf 76 (n = 2) bzw. 254 (n = 3). Nach dem Befund, beschreibend (Nachtrag): Die groesste Luecke des Spektrums liegt
   genau bei E - G (Faktor 1,2e4 bis 7e4), der kleinste physikalische Wert bei 2e-11. Lesart [H]: Die Groessen werden
   in euklidischer Zeit je Takt um einen festen Faktor gedaempft (C2 etwa 2000-fach), nicht vernichtet. Nach
   Kartenwortlaut (reines C auf festen Ecken) ist PT1 vorab verfehlt [M].
4. **C koppelt die zwei Welten nicht [M].** Eine Oktaederdiagonale verbindet zwei Ecken derselben Kopie (sogar derselben
   Klasse); Kanten zwischen Auf- und Ab-Mitten entstehen nie.
5. **Die Reihenfolge zweier lokaler Takte hinterlaesst eine Spur schon in erster Ordnung der Kruemmung [E].** Ohne
   Kruemmung sind AB und BA gleich (1e-15). Mit Kruemmung waechst D wie eps^1 (Steigung 0,998), nicht wie eps^2. Bei
   L/a = 4 bis 32 faellt D wie (a/L)^2,25; die lokale Steigung sinkt von 2,48 auf 2,07 (von Hand). Die Wirkungen selbst
   unterscheiden sich erst in zweiter Ordnung (eps^2,00, von Hand). PT0 (an der eps-Kontrolle) und PT3 treffen nicht ein.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 17:34:34 CEST) durch code/pt_auswertung.py; Urteile und Kennzahlen in
lauf-69/auswertung.json. Nicht dort stehen: die lokalen Steigungen und Quotienten (von Hand aus ko.json) und der
Nachtrag (nachtrag-69/spektrum.json).

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| PT0 | Kontrollen: B 0 Gravitonen; ohne Kruemmung Kommutator null (1e-10); mit Kruemmung ~ eps^2 (Steigung 1,8 bis 2,2) | 85 % | **nicht eingetroffen** | **nicht eingetroffen** | (a) erfuellt: r_B = r_TT und n_x gleich an allen 6 Paaren (n = 2, 3; m = 1, 2, 3); (b) erfuellt: D/\|\|p\|\| = 1,3e-15 (L), 5,4e-16 (G); (c) verfehlt: Steigung 0,998 (D = 9,77e-4 / 2,93e-3 / 9,75e-3 / 2,91e-2 bei eps = 1e-3 / 3e-3 / 1e-2 / 3e-2, L/a = 4) |
| PT1 | [H] C als Takt konsistent: Zwangsbedingungen nach einem Takt loesbar, Rang gleich | 50 % | **nicht eingetroffen** | **nicht eingetroffen [M]** | Plan (C2 mit Zeltstangen): realisierbar (kleinstes 4-Volumen 9,2e-3 relativ, Fehlwinkel <= 1,8e-15), loesbar (4 Zusatz-Nullrichtungen je Schicht, Kopplung <= 4,9e-15), Rang r = 100 / 100 / 76 (n = 2) und 328 / 328 / 254 (n = 3) fuer m = 1 / 2 / 3 mit Schwelle 1e-9, Luecke bei m = 3 nur 1,4 bzw. 1,2. Karte: Summenregel 5,1e-15, Rueckwechsel braucht 4,158 rad > pi |
| PT2 | [H] C-Takt traegt je Zelle >= 1 propagierendes Graviton | 40 % | **eingetroffen** | **eingetroffen** (der Plan setzt C-Takt = C2 mit Zeltstangen; in der Kartenlesart von PT1 gibt es keinen C-Takt, dort ist PT2 gegenstandslos) | m = 3: r/V = 2,375 (n = 2) und 2,352 (n = 3), Zellrate 2,342; m = 1, 2: r/V = 3,125 (n = 2) und 3,037 (n = 3), also 3 + 4/V; Eichprobe <= 8,2e-14 |
| PT3 | [H] Kommutator ~ (a/L)^p mit p in [3; 5] (lokaler Takt) | 40 % | **nicht eingetroffen** | **nicht eingetroffen** | p = 2,252 (Ausgleich L/a = 4, 8, 16, 32 bei eps = 1e-3); D = 9,77e-4 / 1,75e-4 / 3,76e-5 / 8,98e-6; lokal 2,48 / 2,22 / 2,07 (von Hand) |

- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - "PT1 und PT2 treffen ein" ist **nicht** ausgeloest; "rechenbar und traegt Schwerkraft" gilt damit nicht als
    belegt.
  - "PT1 verfehlt: Ein periodischer Flip-Flop auf festem Netz ist inkonsistent. Dann bleibt nur ein unregelmaessiger bzw.
    von der Geometrie gesteuerter Takt" ist **ausgeloest**, nach Kartenwortlaut schon vorab [M]. Mit Zeltstangen
    gesteuert (C2) ist der Takt geometrisch realisierbar; durch einen und zwei Takte propagieren alle E - G Groessen [E].
    Die vorab festgelegte Rangpruefung bei drei Takten scheiterte.
  - "PT3 trifft ein" ist **nicht** ausgeloest: Lokale Takte kommutieren auf feineren Netzen besser, aber nur wie
    (a/L)^2,25 im gerechneten Bereich und linear in der Amplitude.
- **Vermerk zu PT1 nach Plan (beschreibend, nach dem Befund):** Der Nachtrag (Abschnitt 6) zeigt bei drei Takten eine
  klare Luecke genau bei E - G. Mit einer Lueckenregel statt der festen Schwelle waere r_3 = r_1 = r_2. Die Regel wurde
  nicht geaendert; das Urteil bleibt "nicht eingetroffen".
- **Agenten-Vorhersagen** (PLAN 2.3; gehen in kein Urteil ein):

  | Nr | Ergebnis |
  |---|---|
  | V1 | teilweise eingetroffen: TT r = E - G an allen (n, m), G = 4V - 4. **Verfehlt** "n_x = 0": In jeder Schicht gibt es 4 Zusatz-Nullrichtungen, an den Rand nicht gekoppelt (<= 2,2e-14); Lesart [M]: Verschiebung der Endflaeche gegen die Anfangsflaeche als Ganzes (globale Eichung), im Code nicht geprueft |
  | V2 | teilweise eingetroffen: r_B = r_TT, 4 Nullrichtungen je innerer Ecke; "n_x = 0" verfehlt wie V1 |
  | V3 | **verfehlt**: r = E - G nur bei m = 1, 2; bei m = 3 nach der Schwelle 76 bzw. 254. Nach dem Befund: Luecke bei E - G (Nachtrag). Von "PT1 und PT2 eingetroffen" traf nur PT2 ein |
  | V4 | eingetroffen: D ~ eps (Steigung 0,998), PT0 an (c) verfehlt |
  | V5 | **verfehlt**: p = 2,25 liegt knapp ueber [1,8; 2,2]; die lokale Steigung sinkt bis 2,07 |
  | V6 | eingetroffen: Summenregel 5,1e-15; 2 pi - theta = 4,158 > pi |

## 3. R4-Entscheidung fuer C (Schreibtisch, PLAN 1.4) [M]

- In Kopie 1 sind die Ecken die Ab-Mitten (fcc). Die Diagonale eines Oktaeders der Kopie 1 verbindet zwei Ecken dieser
  Kopie, sogar derselben Klasse. Die Auf-Mitten (Ecken der Kopie 2) sitzen in den tet2-Zellen der Kopie 1, nicht in
  ihren Oktaedern. Kanten zwischen Ecken beider Teilgitter entstehen also nie, ebenso wenig durch Zeltstangen.
- **C koppelt die beiden Welten nicht.** Gerechnet wurde eine Kopie; die andere ist ihr Inversionsbild.

## 4. Takte (lauf-69/takt-*.json)

| Variante | n | V | E | G | E - G | r bei m = 1 / 2 / 3 | kleinster physikalischer Singulaerwert m = 1 / 2 / 3 (relativ) | Nicht-Eich-Bedingungen m = 1, 2 |
|---|---|---|---|---|---|---|---|---|
| TT | 2 | 32 | 224 | 124 | 100 | 100 / 100 / 100 | 1,3e-3 / 8,6e-6 / 5,6e-8 | 0 |
| B | 2 | 32 | 224 | 124 | 100 | 100 / 100 / 100 | wie TT (auf 8 Stellen gleich) | 0 |
| C2 | 2 | 32 | 224 | 124 | 100 | 100 / 100 / 76 | 9,2e-5 / 4,0e-8 / 2,2e-11 (Nachtrag) | 0 |
| C3 | 2 | 32 | 224 | 124 | 100 | 100 / 100 / 67 | 7,5e-5 / 3,0e-9 / 1,8e-11 (Nachtrag) | 0 |
| TT | 3 | 108 | 756 | 428 | 328 | 328 / 328 / 328 | 2,8e-4 / 8,6e-6 / 5,6e-8 | 0 |
| B | 3 | 108 | 756 | 428 | 328 | 328 / 328 / 328 | wie TT | 0 |
| C2 | 3 | 108 | 756 | 428 | 328 | 328 / 328 / 254 | 9,2e-5 / 4,0e-8 / 2,2e-11 (Nachtrag) | 0 |
| C3 | 3 | 108 | 756 | 428 | 328 | 328 / 328 / 228 | 7,5e-5 / 3,0e-9 / 1,8e-11 (Nachtrag) | 0 |
| TT | 4 | 256 | 1792 | 1020 | 772 | 772 / 772 / - | 9,3e-5 / 8,6e-6 / - | 0 |
| C2 | 4 | 256 | 1792 | 1020 | 772 | 772 / 772 / - | 6,0e-5 / 4,0e-8 / - | 0 |

- E - G = 3 V + 4 an allen Groessen: 3 eichinvariante Konfigurationsgroessen je Zelle (Hoehns E - 4V, mit Diagonale
  7 - 4 = 3) und 4 globale (Torus statt +10) [M, E].
- Bei m = 1 und 2 steht der Rang ueberall auf E - G, mit Luecke s_r/s_{r+1} >= 4,3e6. Vor- und Nachbedingungen sind dann
  genau die Eichung (4V - 4 je Flaeche), es gibt keine weitere Bedingung.
- Der kleinste physikalische Wert ist bei m = 2 fuer n = 2, 3, 4 gleich (TT 8,58e-6, C2 4,03e-8); er gehoert also zu
  einer Mode, die in allen drei Superzellen vorkommt, vermutlich k = 0 [H]. Er faellt je Takt um etwa das 150-fache
  (TT) bzw. 2300- und 1900-fache (C2, n = 2; von Hand). Lesart [H]: In euklidischer Zeit wachsen und fallen Moden
  exponentiell (elliptische Gleichungen); die Wechsel machen eine Mode steifer.
- Zugzahlen je Takt (n = 2, Hauptlauf m = 1): TT 768 Zeltsimplizes; C2 640 Zelt- und 128 Wechselsimplizes (2 Wechsel
  je Oktaeder, je Wechsel 2 Simplizes); C3 640 und 192 (3 Wechsel je Oktaeder); B 1024 Zelt-, 32 1-4- und 32
  4-1-Simplizes. Bei n = 3 dieselben Zahlen mal 108/32.

## 5. Kommutator (lauf-69/ko.json)

- Schicht: 48 Simplizes je Reihenfolge, 3 Innenkanten (AA', BB' und A'B bzw. AB'), 111 Randkanten, keine innere
  Ecke; Konditionszahl von H_ii 2,5 / 2,7 (L, AB / BA) und 2,2 / 4,2 (G); Newton-Rest <= 8,3e-15. Randimpulse
  \|\|p\|\| = 12,86 (L) bzw. 12,53 (G).

| L/a | D lokal (L) | D/\|\|p\|\| (L) | D global (G) | linearer Koeffizient D1 (L / G) |
|---|---|---|---|---|
| 4 | 9,77e-4 | 7,6e-5 | 1,36e-3 | 0,977 / 1,360 |
| 8 | 1,75e-4 | 1,4e-5 | 2,56e-4 | 0,176 / 0,256 |
| 16 | 3,76e-5 | 2,9e-6 | 5,64e-5 | 0,0377 / 0,0566 |
| 32 | 8,98e-6 | 7,0e-7 | 1,36e-5 | 0,0090 / 0,0137 |

(eps = 1e-3 fuer D; D1 = \|\|Delta Q w\|\| je Einheitsamplitude.)

- **eps-Abhaengigkeit (L/a = 4):** D/eps = 0,977 / 0,976 / 0,975 / 0,969 (von Hand); Steigung 0,998 (L), 0,998 (G).
  Der nichtlineare D stimmt mit dem linearen Koeffizienten D1 = 0,9773 ueberein. Die Wirkungsdifferenz |S_AB - S_BA|
  waechst dagegen wie eps^2,00 (1,05e-8 bei 1e-3, 9,54e-6 bei 3e-2; von Hand): Erste Ableitungen stimmen auf flachen
  Daten ueberein, die zweiten nicht.
- **Ohne Kruemmung:** flach verschobene Ecken (eps = 3e-2): D/\|\|p\|\| = 1,3e-15 (L), 5,4e-16 (G); Delta Q
  verschwindet auf allen Eckverschiebungs-Richtungen (7e-16 relativ), wie vorab abgeleitet [M]. Insgesamt ist Delta Q
  nicht klein: groesster Eintrag 0,50 (L) bzw. 0,60 (G) des groessten Eintrags von Q.
- **Gitterweite:** p = 2,25 (L) und 2,21 (G) aus dem Ausgleich; lokal 2,48 / 2,22 / 2,07 (L) und 2,41 / 2,18 / 2,05 (G),
  von Hand. Der lineare Koeffizient gibt dieselben Exponenten (2,250 bzw. 2,209).
- **Erwarteter Grenzwert [M, bedingt]:** Die Welle cos(k (x - x_A)) hat am Ort A keinen Term erster Ordnung in k, und ihr
  k-unabhaengiger Teil ist eine Eckverschiebung, die Delta Q annulliert. Ist D linear in eps, folgt daraus D1 ~ k^2 fuer
  kleines k, also p -> 2. Gemessen ist das nicht; gemessen ist 2,25 mit sinkender lokaler Steigung. Damit hing PT3
  vorab an PT0 (c): Bei D ~ eps^2 waere p gegen 4 gegangen.
- **Lokal gegen global:** Gleiche Zeltstangen (G) heben die Spur nicht auf; D(G)/D(L) = 1,39 bei L/a = 4 bis 1,51 bei
  L/a = 32 (von Hand).
- Lesart [H]: AB und BA sind zwei Triangulierungen derselben flachen Region (Innenkante A'B gegen AB'), und das
  linearisierte 4D-Regge haengt fuer gekruemmte Randdaten von der Triangulierung ab. TETRAEDER-L nennt Invarianz der
  Regge-Wirkung unter 5-1 und 4-2 [P, dort S Abstract]; welche Pachner-Zuege AB und BA verbinden, habe ich nicht
  bestimmt.

## 6. Nachtrag nach dem Einfrieren (beschreibend; code/nachtrag_spektrum.py, nachtrag-69/spektrum.json)

- Grund: Bei m = 3 lag die Rangschwelle 1e-9 in einem glatten Auslauf (Luecke 1,0 bis 1,4).
- Ganzes Singulaerwertspektrum, eingefrorenes pt.py unveraendert importiert:

| Fall | E - G | Werte > 1e-9 / 1e-10 / 1e-11 / 1e-13 | groesste Luecke nach Index (Faktor) | kleinster physikalischer / erster Eichwert |
|---|---|---|---|---|
| TT n = 2, m = 3 | 100 | 100 / 100 / 100 / 100 | 100 (5,5e6) | 5,6e-8 / 1,0e-14 |
| C2 n = 2, m = 3 | 100 | 76 / 97 / 100 / 100 | 100 (1,2e4) | 2,2e-11 / 1,8e-15 |
| C3 n = 2, m = 3 | 100 | 67 / 99 / 100 / 100 | 100 (7,3e4) | 1,8e-11 / 2,5e-16 |
| C2 n = 2, m = 2 | 100 | 100 / 100 / 100 / 100 | 100 (6,6e6) | 4,0e-8 / 6,1e-15 |
| C2 n = 3, m = 3 | 328 | 254 / 318 / 328 / 328 | 328 (1,3e4) | 2,2e-11 / 1,7e-15 |
| C3 n = 3, m = 3 | 328 | 228 / 313 / 328 / 328 | 328 (3,8e4) | 1,8e-11 / 4,8e-16 |

- In allen Faellen liegt die groesste Luecke genau bei E - G. Bei Schwellen zwischen 1e-11 und 1e-13 ist r_3 = E - G
  auch fuer C2 und C3. Lesart [H]: gedaempft, nicht vernichtet.

## 7. Kontrollen

- **Zellen:** Schlaefli <= 2,1e-15; M symmetrisch <= 2,1e-15 relativ.
- **Flachheit:** groesster Innen-Fehlwinkel 1,8e-15 ueber alle 28 Takt-Faelle; kleinstes 4-Volumen relativ 7,9e-4
  (B), 9,2e-3 (C2).
- **Eichung:** H Y_innen <= 1,1e-15 relativ; Nullraum von H_ii = 4 je innerer Ecke + 4 weitere (Lesart [M]: globale
  Verschiebung der Endflaeche), Kopplung an den Rand <= 2,2e-14; Omega~ annulliert die Rand-Eckverschiebungen auf
  <= 4,8e-12.
- **Kantenbilanz:** E = 7 V und 6 V Tetraeder auf beiden Flaechen, keine Kante zugleich in Anfangs- und Endflaeche.
- **Kommutator:** bei eps = 0 D/\|\|p\|\| = 1,1e-15; flach Innen-Fehlwinkel <= 8,9e-15, Gradient <= 9,6e-15; keine
  Kante ueber den Kastenrand.
- **Reines C (kc):** Summenregel max 5,1e-15 an 200 Zufallshoehen mit Neigung; Anteil der Oktaeder, deren x-Diagonale
  hoeher liegt als die z-Diagonale, 34 % bis 63 %, nie alle. Die beiden Wechselsimplizes haben 4-Volumen +-0,00625
  (Vorzeichen nur aus der Eckreihenfolge).
- **Latten:**
  - L1 (kann scheitern): vorab ableitbar waren PT1 nach Karte, PT0 (a), PT0 (b), die Summenregel und die Winkelprobe [M];
    nicht ableitbar waren PT1 nach Plan, PT2 und PT0 (c); PT3 nur bedingt (Abschnitt 5, Grenzwert).
  - L2 (Gegenprobe): drei Superzellen (n = 2, 3, 4), zwei Wechselvarianten (C2, C3), zwei Kontrolltakte (TT, B),
    nichtlinear gegen linear beim Kommutator (D/eps = 0,9770 gegen D1 = 0,9773), zwei Lapse-Varianten.
  - L3 (Numerik): Identitaeten 1e-15; Rangluecken bei m <= 2 >= 4,3e6; bei m = 3 Schwellenproblem (Abschnitt 6).
  - L4 (schon bekannt): Graviton-Zaehlung E - 4V und die Rolle der Zuege sind Hoehn 2014 [S]; Invarianzen der 4D-Regge-
    Wirkung unter Pachner-Zuegen [P, TETRAEDER-L]. Neu fuers Projekt: der gesteuerte Flip-Flop auf Finns Netz, seine
    Propagation durch zwei Takte und der Kommutator erster Ordnung mit p = 2,25 im Bereich L/a = 4 bis 32.
  - L5 (Messbezug): keiner.

## 8. Lesepunkt arXiv:2610.00593 (optional, ein Abruf)

- Erwartung vor dem Abruf (2026-10-04 17:35:21 CEST, date): Regge mit Torsion als Einstein-Cartan auf Simplizes;
  Torsion als Fehlschluss der Kantenvektoren zwischen Nachbarsimplizes; Kopplung an Spin; kein Bezug zu Pachner- oder
  Zeltzuegen, keine Aussage zur 1/2.
- Abruf (ein WebFetch der Abstract-Seite): Yan, Ding, Ma, Zhang, "Dynamics of Regge calculus with torsion". Kanten tragen
  Kantenvektoren, Uebergaenge Holonomien; "The torsion manifests itself as the difference between an edge vector on an
  interface belonging to one simplex and the parallel transported edge vector ... belonging to the adjacent simplex";
  Einstein-Cartan-Wirkungen in 3D und 4D, torsionsfrei gleich Regge; "the torsion-free holonomies satisfy the latter
  equation as in the continuous case" [S Abstract].
- Ausgang: Torsion als Kantenvektor-Fehlschluss eingetroffen; Spin-Kopplung steht nicht im Abstract; kein Bezug zu
  Zuegen eingetroffen. Bezug zu K-AM [H]: Fermionen auf Finns Netz braeuchten Kantenvektoren und Holonomien statt
  Laengen; im Vakuum bleibt die Torsion null, an dieser Karte aendert das nichts.

## 9. Bedeutung [M, E, H]

- **Finns Flip-Flop als Umbau-Takt:** Er geht nur zusammen mit Zeltstangen, und dann wird er von der Geometrie
  gesteuert: Eine Diagonale kann nur zur hoeher liegenden wechseln [M]. So gebaut ist er realisierbar, und durch einen
  und zwei Takte propagieren alle 3 eichinvarianten Groessen je Zelle [E]; die vorab festgelegte Pruefung nach drei
  Takten bestand er nicht (Schwellenbefund, Abschnitt 6). Im Rang bei m = 1, 2 gleicht er dem reinen Zeltstangen-Takt,
  im Spektrum nicht: Er daempft einzelne Moden je Takt viel staerker (etwa 2000- statt 150-fach). Lesart [H]: neue
  Gravitonen entstehen und vergehen paarweise (2-3 und 3-2), gerechnet ist das nicht je Zug.
- **Zwei Welten bleiben zwei Welten:** C koppelt Auf und Ab nicht (R4). Eine Welt gibt es nur ueber gefuellte Loecher
  (EINE-WELT-LOCH-1 [P]) oder andere Kanten zwischen den Teilgittern.
- **Die 1/2 im Feinen:** Lokale Takte sind auf diesem Netz nicht weg-unabhaengig. Die Spur der Reihenfolge ist linear
  in der Amplitude und faellt im gerechneten Bereich wie (a/L)^2,25 mit sinkender lokaler Steigung; nach dem bedingten
  Grenzwert (Abschnitt 5) ginge sie wie die Kruemmung je Zelle gegen null [M, bedingt]. Dass die freie
  Zeitumbenennung im Feinen nur in diesem Mass zurueckkommt, ist eine Lesart [H].
- **Grenzen:** euklidische Signatur (wie Hoehn); keine Drift ueber viele Takte gerechnet; nur eine Wellenrichtung und
  eine Polarisation; nur zwei Lapse-Paare; Kommutator an einem Kantenpaar.

## 10. Selbstanzeigen

1. **Lesart mit Zeltstangen [F]:** Lesart C der Karte enthaelt keine Zeltstangen. Weil reines C auf festen Ecken
   unmoeglich ist [M], rechnet der Plan C2 und C3 mit Zeltstangen. Die Urteile "nach Plan" (und PT2 auch nach
   Kartenwortlaut, Plan 2.2) betreffen diesen gesteuerten Takt; "nach Kartenwortlaut" steht PT1 vorab fest.
2. **Schwelle bei m = 3:** PT1 nach Plan ist an der festen Rangschwelle 1e-9 gescheitert. Der Nachtrag zeigt die Luecke
   bei E - G. Ich habe die Regel nicht nachtraeglich geaendert.
3. **n_x = 4 nicht vorhergesagt:** vier zusaetzliche Nullrichtungen im Innenraum in jeder Schicht, an den Rand nicht
   gekoppelt. Lesart [M]: die Verschiebung der Endflaeche gegen die Anfangsflaeche als Ganzes (globale Eichung); der Code
   prueft nicht, dass es diese Richtungen sind. In TT und B gleich, also ohne Folge fuer PT0 (a) und PT1 (2).
4. **Gravitonen-Begriff [F]:** "Gravitonen je Takt" ist Hoehns Zahl propagierender eichinvarianter
   Konfigurationsgroessen (Rang von Omega~), nicht die Zahl der Kontinuums-Polarisationen. Die 3 je Zelle enthalten die
   Diagonalengroesse; welche davon Kontinuums-Gravitonen sind, ist nicht gerechnet. "B gibt 0 Gravitonen" heisst: B
   aendert gegenueber TT nichts.
5. **Kommutator-Definition [F]:** Randwertform (gleiche Randlaengen, Vergleich der Randimpulse) statt Anfangswertform
   mit frei gewaehltem Lapse; der Lapse steckt in der Endflaeche. Die Erwartung "eps^2" der Karte bezieht sich auf
   Kruemmung im Hintergrund (Bahr/Dittrich, nichtlinear); hier ist der Hintergrund flach und die Kruemmung sitzt in den
   Randdaten. Wer D als Wirkungsdifferenz liest, findet eps^2,00 (beschreibend).
6. **Vor dem Einfrieren geaendert** (ohne Kenntnis von Ergebnissen): ebene Ausgangsflaeche des Kommutators durch die
   geknickte ersetzt (r1 brach mit singulaerem H_ii ab), Schur-Komplement ohne dichte Pseudoinverse, Lauf T4 und m = 3
   fuer n = 3 ergaenzt. Die Newton-Schwelle 1e-15 wird an der Rundungsgrenze nicht erreicht (dann 40 Schritte, Rest
   <= 8,3e-15); harmlos.
7. **kc-Winkelprobe ist vorab ableitbar:** 2 pi - theta > pi gilt fuer jeden nicht entarteten Simplex (theta < pi); sie
   veranschaulicht 1.3, prueft aber nichts. Auch das "genau dann" der Vorwaerts-Bedingung ist nur am Schreibtisch
   gezeigt [M], nicht von kc geprueft.
8. **Nicht gerechnet:** Drift ueber viele Takte, Auf- gegen Ab-Kopie (nach Inversion gleich [M]), kleinste
   Hesse-Eigenwerte auf gekruemmtem Hintergrund (Bahr/Dittrich-Kriterium), Lorentz-Signatur.
9. **Werkzeuge lokal:** jq, sed, grep, sha256sum, date, ssh, scp, cp, mv, mkdir; dazu chmod (Schreibschutz der
   eingefrorenen Kopien) und zur Anzeige cat, ls, head, tail, paste sowie until-Schleifen mit sleep zum Warten. Kein
   Interpreter lokal; auf der .69 nur ueber den Starter (Spuren cpu8 und cpu9). Ein WebFetch fuer den Lesepunkt.
10. **ssh:** hoechstens drei Verbindungen zugleich (zwei Laufketten und eine Warteschleife).
11. **Erste Textfassung zu stark und mit vier falschen Angaben:** siehe Abschnitt 11.

## 11. Gegenlesen

- Frischer Leser (pruefer-opus, nur lesend, 17:50:48 bis 18:02:52 CEST nach seiner Angabe) gegen KARTE, eingefrorenen
  PLAN, alle JSON-Dateien und den Nachtrag. Urteile PT0 bis PT3 und die uebrigen Zahlen bestaetigt, auch die lokalen
  Steigungen.
- Berichtigt (alle gegen die Daten nachgeprueft):
  - falsche Angaben: laengster Lauf (261 s bei T4, nicht 247 s), Newton-Rest (8,3e-15, nicht 7,7e-15), Verhaeltnis
    G zu L (1,39 bis 1,51, nicht "etwa 1,4"), Latte L1 (Liste des vorab Ableitbaren war falsch), fehlende Zeitbox-Zeile;
  - zu stark: "nur an der festen Schwelle", Wiedergabe der nicht ausgeloesten Bedeutung "traegt Schwerkraft",
    "macht nichts, was der Zeltstangen-Takt nicht macht", "(a/L)^2" als Messwert, "Einfach gesagt";
  - Kennzeichen: Fall-b-Lesart und "gedaempft, nicht vernichtet" jetzt [H]; Vorwaerts-Bedingung [M]; n_x-Lesart [M];
    Grenzwert p -> 2 als [M, bedingt]; Quellenangabe zu den Pachner-Invarianzen einheitlich [P];
  - unklar: Werte der Variante G getrennt angegeben, Wechsel gegen Simplizes, "bzw." in der PT2-Zeile, B "auf 8 Stellen
    gleich", von Hand gerechnete Zahlen gekennzeichnet.
- Nicht geprueft vom Leser: Abschnitt 8 und die Rauchlaufzeiten (keine Datei im Auftrag), die Pruefsummen (nur gezaehlt).

## 12. Einfach gesagt

Wir haben eine von drei Lesarten von Finns Flip-Flop gerechnet (C, die Standardlesart, solange Finn nichts anderes
sagt): In jedem Oktaeder wechselt die Diagonale, die es in vier Tetraeder teilt. Ohne dass die Ecken in der Zeit
weiterruecken, geht das nicht, denn ein Hin-und-Her-Klappen auf der Stelle waere ein Schritt rueckwaerts in der Zeit.
Rueckt jede Ecke mit, laesst sich der Takt bauen; durch einen und zwei Takte laufen alle Groessen des Netzes durch, die
vorab festgelegte Pruefung nach drei Takten bestand er aber nicht, und die zwei getrennten Welten verbindet er nicht.
Welche von zwei benachbarten Ecken zuerst tickt, macht schon in erster Ordnung der Kruemmung einen Unterschied; er sinkt
auf feineren Netzen etwa wie die Kruemmung pro Zelle. Alles sind Gitterrechnungen, keine Messdaten.

## 13. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-173434, EINGEFROREN-SHA256.txt
- code/: pt.py (Netz, Zuege, Regge-Geometrie, Laeufe), pt_auswertung.py (Urteile), beide mit eingefrorenen Kopien;
  nachtrag_spektrum.py (Nachtrag).
- lauf-69/: takt-n2.json, takt-n3-TT.json, takt-n3-B.json, takt-n3-C2.json, takt-n3-C3.json, takt-n4.json, kc.json,
  ko.json, auswertung.json, Logs, PRUEFSUMMEN.txt.
- rauch-69/: r1-*, r2-*, r3/ (Kette mit kleinen Groessen).
- nachtrag-69/: spektrum.json, nt.log, PRUEFSUMMEN.txt.
- Auf der .69: /home/fmh/fmhc-physics-remote/runde42-pachner-takt/ (code/, rauch/, lauf/, nachtrag/).

## Zeitbox

- Start 17:01:54 CEST; Abgabe in der folgenden Zeile (date).
- Abgabe 2026-10-04 18:07:57 CEST (date), also nach 66 min, innerhalb der 150 min.
