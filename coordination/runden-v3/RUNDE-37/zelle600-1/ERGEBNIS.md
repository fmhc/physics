# ZELLE600-1: Ergebnis (Code-Agent fuer die Leitung claude-primary)

- **Auftrag (Finn, woertlich):** "Welche 600 Zelle? Bau die". Karte KARTE.md bindend, Z0 bis Z4 unveraendert.
- **Kennzeichen:** [E] gerechnet auf der .69, [M] eigene Schreibtischrechnung, [L] Literatur aus dem Gedaechtnis.
  Alles ist Geometrie und Darstellungstheorie, keine Messdaten. Z0 bis Z4 waren vorab ableitbar (PLAN.md, 06:18:41,
  eingefroren 06:19:25 mit SHA256); die Rechnung bestaetigt sie nur.

## 1. Zeiten und Laeufe

- **Start** 2026-10-05 06:12:00 CEST (date). PLAN.md ab 06:18:41, eingefroren 06:19:25. Diese Datei ab 06:48:00,
  Hauptteil fertig 06:49:54 (date, danach nur diese Zeile). Gebraucht rund 38 von 90 min.
- **Rechenort:** .69, /home/fmh/fmhc-physics-remote/zelle600-1/, Aufruf
  `bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <name> <skript> <ordner>`. Ein Thread
  (OMP/OPENBLAS/MKL = 1 laut lauf.json), CPU, numpy 2.4.4, Python 3.12.3.

| Lauf | Skript | Spur | Aufruf (lokal, date) | Ende | Laufzeit | rc |
|---|---|---|---|---|---|---|
| 1 | code/zelle600.py (Bau, Z0 bis Z4, Ring) | cpu | 06:24:16 CEST | 06:24:23 CEST | 3,39 s Unit (Skript 3,21 s) | 0 |
| 2 | code/schalenform.py (Form jeder Schale) | cpu | 06:28:08 CEST | 06:30:44 CEST | 0,155 s Unit (rund 2,5 min am Lock gewartet) | 0 |
| 3 | code/zelle120.py (Nachtrag 120-Zelle) | cpu2 | 06:41:43 CEST | 06:41:44 CEST | 0,876 s Unit (Skript 0,71 s) | 0 |

- Unit-Namen: fmhc-physics-klein-zelle600-042416, fmhc-physics-klein-zelle600form-042808, fmhc-physics-klein-zelle120-044143.
- Protokolle: lauf-69/log-lauf1.txt bis log-lauf3.txt. Hashes aller JSON: lauf-69/SHA256SUMS.txt.
- **Ansicht lokal (nur Darstellung):** zelle600.html, zelle600.png per headless Chrome mit dem Aufruf aus dem Auftrag
  (letzte Fassung 06:46). Fuenf Pruefbilder in pruefbilder/.

## 2. Ergebnis zuerst

1. **Gebaut und geprueft [E]:**
   - Die 120 Quaternionen nach dem Rezept der Karte bilden die Gruppe 2I: abgeschlossen (groesster Fehler 5,6e-17),
     9 Konjugationsklassen.
   - Daraus folgen 120 Ecken, 720 Kanten, 1200 Dreiecke, 600 Tetraeder und Euler-Zahl 0.
   - Je Ecke 12 Nachbarn und 20 Tetraeder, je Kante 5 Tetraeder; jede Eckfigur ist ein Ikosaeder.
   - Alle Kanten sind 1/phi lang, alle Tetraeder regulaer.
2. **Kruemmung [E, vorab ableitbar]:**
   - Jede der 720 Kanten hat den Fehlwinkel 7,3561 Grad.
   - Summe(l delta) = 57,131 R gegen 6 pi^2 R = 59,218 R, also -3,52 %. Bei gleichem Volumen statt gleichem Umkreis +2,02 %.
3. **Wasserstoff-Muster [E, vorab ableitbar]:**
   - Die Laplace-Niveaus haben von unten die Vielfachheiten 1, 4, 9, 16, 25, 36, danach nur noch 9, 16, 4.
   - Die sechs untersten Niveaus sind exakt die Kugelfunktionen auf S^3 vom Grad k = 0 bis 5 (Restnorm hoechstens 5e-14),
     also n = 1 bis 6 nach Fock.
   - Grad 6 faltet sich auf 9 + 16, Grad 7 auf 4. 120 Ecken tragen nur 91 + 29 Muster.
   - Die Abstaende folgen dem Kontinuum nur grob: bei k = 3 liegt das Verhaeltnis um 21,5 % unter k(k+2)/3.
4. **30er-Ring [E]:**
   - Jede Kette von Tetraedern, die je ein Dreieck teilen, schliesst nach genau 30 Tetraedern (alle 14400 geordneten Starts).
   - Insgesamt gibt es 240 Ringe, jedes Tetraeder liegt in 12 davon.
   - Die Bahn eines Rings unter Linksmultiplikation zerlegt alle 600 Tetraeder in 20 disjunkte Ringe.
5. **Nachtrag 120-Zelle [E]:** Auch das Diamant-Gegenstueck auf S^3 (4 Nachbarn je Ecke, 600 Ecken) traegt exakt
   1, 4, 9, 16, 25, 36 als unterste Niveaus.
   - Danach spaltet n = 7 in 24 + 16 + 9, statt abzubrechen.
   - Das exakte Muster haengt an der Symmetrie, nicht an der Kantenzahl. Das feinere Netz folgt dem Kontinuum besser
     (k = 3: -4,4 % statt -21,5 %).

## 3. Urteile Z0 bis Z4

| Nr | Vorhersage (Karte) | Urteil | Art |
|---|---|---|---|
| Z0 | 120/720/1200/600, Euler 0, 5 je Kante, 20 je Ecke, alle regulaer | **erfuellt** | Kontrolle, vorab ableitbar, keine Messung |
| Z1 | 9 Adjazenz-Eigenwerte, Vielfachheiten 1, 4, 9, 16, 25, 36, 9, 16, 4 | **erfuellt** (fallend genau diese Folge, Abstand zu den geschlossenen Formen hoechstens 9e-15) | vorab ableitbar (PLAN.md, Cayley-Graph von 2I, Charaktere); keine Messung |
| Z2 | Laplace steigend: erste sechs 1, 4, 9, 16, 25, 36, dann Abbruch | **erfuellt** (danach 9, 16, 4) | vorab ableitbar; die Identitaetsprobe mit den Kugelfunktionen ist zusaetzlich gerechnet |
| Z3 | Regge-Summe innerhalb 5 % bei 6 pi^2 R | **erfuellt** (-3,52 %) | vorab ableitbar (PLAN.md: 57,131 gegen 59,218); keine Messung |
| Z4 | Niveaus k = 1, 2, 3 folgen k(k+2)/3 auf 10 % | **nicht erfuellt**: k = 2 -9,55 % (knapp drin), k = 3 -21,46 % | vorab ableitbar; PLAN.md sagte "nicht erfuellt" voraus |

## 4. Tabellen

### 4.1 Zahlen der 600-Zelle [E, lauf-69/pruefungen.json]

| Groesse | Wert |
|---|---|
| Ecken / Kanten / Dreiecke / Tetraeder | 120 / 720 / 1200 / 600 |
| Euler-Zahl | 0 |
| Nachbarn je Ecke | 12 (min = max) |
| Tetraeder je Kante / je Ecke / je Dreieck | 5 / 20 / 2 |
| Dreiecke je Kante | 5 |
| Eckfigur | Ikosaeder (12 Ecken, 30 Kanten, 20 Dreiecke, Grad 5) an allen 120 Ecken |
| Kantenlaenge (Radius 1) | 0,618033988749895 = 1/phi (min = max) |
| Tetraedervolumen | 0,027820877951849 = l^3/(6 sqrt 2) (min = max); Kantenabweichung in Tetraedern hoechstens 1e-16 |
| Gruppe 2I | abgeschlossen (Fehler 5,6e-17), Gruppentafel lateinisches Quadrat, Inverse da, Assoziativ-Stichprobe ok |
| Konjugationsklassen (Realteil: Anzahl) | 1: 1, phi/2: 12, 1/2: 20, 1/(2 phi): 12, 0: 30, -1/(2 phi): 12, -1/2: 20, -phi/2: 12, -1: 1 |
| Elementordnungen | 1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24 |
| Diederwinkel (alle 3600) | 70,5287793655 Grad = arccos(1/3) |
| Fehlwinkel je Kante (alle 720) | 7,3561031725 Grad = 0,128388 rad |
| Summe(l delta) | 57,1307644866 R |
| 6 pi^2 R | 59,2176264065 R, Verhaeltnis 0,96476 (-3,52 %) |
| gleiches Volumen | 600 flache Tetraeder 16,6925 R^3 gegen 2 pi^2 R^3 = 19,7392, R_eff = 0,94565 R, Verhaeltnis 1,0202 (+2,02 %) |

### 4.2 Schalen um den Pol (Ecke 1 = (1, 0, 0, 0)) [E, lauf-69/schalen.json, schalenform.json]

| Schale | Winkel | Skalarprodukt | Ecken | Form (Lauf 2) | Radius stereogr. tan(Winkel/2) | Graphabstand |
|---|---|---|---|---|---|---|
| 0 | 0 Grad | 1 | 1 | Punkt (Pol) | 0 | 0 |
| 1 | 36 Grad | phi/2 | 12 | Ikosaeder | 0,325 | 1 |
| 2 | 60 Grad | 1/2 | 20 | Dodekaeder | 0,577 | 2 |
| 3 | 72 Grad | 1/(2 phi) | 12 | Ikosaeder | 0,727 | 2 |
| 4 | 90 Grad | 0 | 30 | Ikosidodekaeder | 1 | 3 |
| 5 | 108 Grad | -1/(2 phi) | 12 | Ikosaeder | 1,376 | 3 |
| 6 | 120 Grad | -1/2 | 20 | Dodekaeder | 1,732 | 4 |
| 7 | 144 Grad | -phi/2 | 12 | Ikosaeder | 3,078 | 4 |
| 8 | 180 Grad | -1 | 1 | Punkt (Gegenpol) | unendlich | 5 |

- **Nach Graphabstand** 0 bis 5: 1, 12, 32, 42, 32, 1.
- **Abstand 2** mischt 60 Grad (3 gemeinsame Nachbarn mit dem Pol) und 72 Grad (1). Der Kantengraph ist also nicht
  abstandsregulaer.

### 4.3 Eigenwerte mit Vielfachheiten, neben S^3 und Wasserstoff [E, lauf-69/spektrum.json]

| Niveau | Laplace L = 12 - A | Adjazenz A | geschlossen | Vielf. | Darstellung von 2I | Kugelfunktion | Wasserstoff n, n^2 | S^3: k(k+2) | lambda_k / lambda_1 gegen k(k+2)/3 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 12 | 12 | 1 | 1 = V_0 | Grad 0 | 1, 1 | 0 | - |
| 1 | 2,29180 | 9,70820 | 6 phi | 4 | 2 = V_1/2 | Grad 1 | 2, 4 | 3 | 1 gegen 1 |
| 2 | 5,52786 | 6,47214 | 4 phi | 9 | 3 = V_1 | Grad 2 | 3, 9 | 8 | 2,412 gegen 2,667 (-9,55 %) |
| 3 | 9 | 3 | 3 | 16 | 4s = V_3/2 | Grad 3 | 4, 16 | 15 | 3,927 gegen 5 (-21,46 %) |
| 4 | 12 | 0 | 0 | 25 | 5 = V_2 | Grad 4 | 5, 25 | 24 | 5,236 gegen 8 (-34,5 %) |
| 5 | 14 | -2 | -2 | 36 | 6 = V_5/2 | Grad 5 | 6, 36 | 35 | 6,109 gegen 11,67 (-47,6 %) |
| 6 | 14,47214 | -2,47214 | -4/phi | 9 | 3' | aus Grad 6 gefaltet | (n = 7 haette 49) | 48 | - |
| 7 | 15 | -3 | -3 | 16 | 4 aus A5 | aus Grad 6 gefaltet | | | - |
| 8 | 15,70820 | -3,70820 | -6/phi | 4 | 2' | aus Grad 7 gefaltet | (n = 8 haette 64) | 63 | - |

- Spurprobe: Spur A = 0, Spur A^2 = 1440 = 2 * 720.
- **Rang der Polynome vom Grad <= k auf den 120 Ecken**, k = 0 bis 8: 1, 5, 14, 30, 55, 91, 116, 120, 120.
  - Kontinuum: 1, 5, 14, 30, 55, 91, 140, 204.
  - Saubere Luecke der Singulaerwerte: kleinster behaltener 0,088, groesster verworfener 1e-14.
- **Identitaetsprobe:** Der Spann der Polynome vom Grad <= k ist fuer k = 0 bis 5 genau der Eigenraum der k+1 untersten
  Niveaus (Restnorm 1,9e-15 bis 4,9e-14).
  - Neue Dimensionen bei Grad 6: 9 in Niveau 6 und 16 in Niveau 7.
  - Bei Grad 7: 4 in Niveau 8 (lauf-69/spektrum.json, grad_auf_niveaus_verteilung).

## 5. Was die Ansicht zeigt

- **Dateien:**
  - HTML: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/zelle600-1/zelle600.html
  - PNG: /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/zelle600-1/zelle600.png
- **Technik:** Eine Datei, Canvas 2D, kein externes Skript, keine Module. Laeuft per file:// und offline.
  - Daten inline: lauf-69/ansicht.json und lauf-69/ansicht120.json.
  - Beide Einbettungen per diff gegen `jq -c` geprueft: byteweise gleich, SHA256 9a93acc5... fuer ansicht.json.
- **Ansicht:**
  - Stereographische Projektion S^3 -> R^3 vom Gegenpol. Der Pol liegt in der Mitte, die Schalen sind konzentrische Kugeln.
  - Kanten sind projizierte Grosskreisboegen, die 12 Kanten zum Gegenpol (im Unendlichen) nur blass.
  - Ecken nach Schale gefaerbt (rot = Polseite, grau = Aequator, blau = Gegenseite). Die Groesse folgt gedaempft dem
    Massstab der Projektion.
- **Bedienung:**
  - Schieberegler fuer die 4D-Drehungen xw, yw, zw und ein Knopf, der die 4D-Drehung abspielt.
  - Maus- und Touch-Drehung in 3D, Zoom mit Mausrad oder zwei Fingern.
  - Legende mit Winkel, Anzahl und Form je Schale. Ein Klick blendet eine Schale aus.
  - Umschalter "nach Schritten im Netz" (1, 12, 32, 42, 32, 1).
- **Knoepfe und Texte:**
  - "Ring hervorheben" zeigt einen 30er-Ring als Band aus Tetraedern. Startring 6 von 20 laeuft nicht durch den Pol;
    Ring 1 geht durch Pol und Gegenpol, also durchs Unendliche. "Naechster Ring" laeuft durch alle 20 der Zerlegung.
  - Kurztext oben (3 Absaetze, deutsch): was die 600-Zelle ist, Luecke wird Kruemmung, Wasserstoff-Muster.
  - Punktbild der Vielfachheiten als n x n Bloecke (1, 4, 9, 16, 25, 36 blau, 9, 16, 4 grau) mit Eigenwerten. Dazu eine
    Tabelle der Niveaus.
  - Kacheln mit den Zahlen und der Regge-Summe.
  - Nachtrag: Umschalter 600-Zelle, 120-Zelle oder beide.
  - Schema Auto, Hell oder Dunkel; Handy-Breite geprueft.
- **Sichtprobe (Read):**
  - zelle600.png zeigt Kopftext, Projektion, Legende, Regler und Punktbild ohne Ueberlappung.
  - pruefbilder/ring.png: geschlossenes Band aus 30 Tetraedern um den Pol.
  - pruefbilder/ring-xw50-dunkel.png: Ring nach 4D-Drehung, dunkles Schema.
  - pruefbilder/dunkel-beide.png und nur120.png: 120-Zelle gruen, Fuenfecke sichtbar.
  - pruefbilder/handy.png: 390 px breit, Text gestapelt, Bild darunter.
  - In der ersten Fassung waren die Strahlen ins Unendliche zu kraeftig. Die Beschriftung "Pol" ging im Punktgewirr
    unter, und Ring 1 fuellte das halbe Bild mit riesigen Flaechen nahe dem Projektionspunkt. Alle drei Punkte sind behoben.

## 6. Nachtrag der Leitung (06:39): 120-Zelle

- **Erwartung vor der Rechnung:** NACHTRAG-120-ERWARTUNG.md, geschrieben ab 06:40:03 (date), eingefroren 06:40:31 mit
  SHA256. Lauf 3 startete 06:41:43.
- **Bau [E]:**
  - 600 Ecken (normierte Tetraedermitten), 1200 Kanten (gemeinsame Dreiecke), Grad 4.
  - Kantenwinkel 15,5225 Grad, Sehne 0,270091 = 1/(sqrt 2 phi^2), alle gleich. Die naechsten Nachbarn nach Geometrie
    sind genau die Graphkanten.
  - 720 Fuenfecke (um die Kanten der 600-Zelle), 120 Dodekaeder (um ihre Ecken), Euler 600 - 1200 + 720 - 120 = 0.
- **Laplace-Niveaus der 120-Zelle (L = 4 - A), unten [E, lauf-69/zelle120.json]:**

| Niveau | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Laplace | 0 | 0,14590 | 0,38197 | 0,69722 | 1,07458 | 1,48180 | 1,76393 | 2,20871 | 2,38197 | 2,61803 | 2,82181 | 3 |
| Vielfachheit | 1 | 4 | 9 | 16 | 25 | 36 | 24 | 16 | 24 | 9 | 36 | 40 |
| traegt Grad | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 6 | 7 (+5) | 8 |

- Insgesamt 27 verschiedene Eigenwerte. Spur A^2 = 2400 = 2 * 1200.
- Rang der Polynome vom Grad <= k: 1, 5, 14, 30, 55, 91, 140, 204, 285. Bis Grad 8 bleibt alles erhalten, auch Grad 6
  mit 49 und Grad 7 mit 64.
- Niveau 1 = 1/phi^4 und Niveau 2 = 1/phi^2, exakt.
- Grad 3 verteilt sich auf zwei 16er-Niveaus: 0,69722 = (5 - sqrt 13)/2 und 4,30278 = (5 + sqrt 13)/2. Das sind die
  zwei Kopien, die die T-Invarianten vorhersagen. Grad 4 und Grad 5 verteilen sich auf je drei Niveaus.
- Anteil der Grad-k-Funktionen im untersten passenden Niveau: k = 3: 99,98 %, k = 4: 99,78 %, k = 5: 97,89 %.
- Kontinuum lambda_k/lambda_1 gegen k(k+2)/3: k = 2: -1,82 %, k = 3: -4,42 %, k = 4: -7,93 %, k = 5: -12,95 %.

| Nr | Erwartung (06:40) | Urteil |
|---|---|---|
| N1 | 600 / 1200 / Grad 4 / alle Kanten 15,52 Grad (97 %) | erfuellt (Kontrolle, vorab ableitbar) |
| N2 | unterste sechs Niveaus 1, 4, 9, 16, 25, 36 (70 %) | erfuellt |
| N3 | Niveau 1 und 2 exakt 1/phi^4 und 1/phi^2 (90 %) | erfuellt (vorab ableitbar) |
| N4 | kein 49er-Niveau; Grad 6 auf 9, 12, 12, 16 (80 %) | erfuellt im Kern. Einzelheit: die beiden 12er erscheinen als ein 24-faches Niveau. [M] Deutung: Die Spiegelungen von H4 vertauschen beide Faktoren; nicht gerechnet. |
| N5 | k = 2 und 3 innerhalb 10 % von k(k+2)/3 (80 %) | erfuellt (-1,8 % und -4,4 %) |
| N6 | Anteil ueber 90 % fuer k = 3 bis 5 (60 %) | erfuellt (97,9 % bis 99,98 %) |

- **Antwort auf die Frage "Haengt das Wasserstoff-Muster an der Zahl der Kanten je Knoten?":** Nein, das exakte
  Muster nicht.
  - Beide Netze tragen exakt n^2 fuer n = 1 bis 6 und kein exaktes n = 7. Das legt die gemeinsame Symmetriegruppe H4 fest.
  - Was sich unterscheidet, ist das Danach. Die 600-Zelle (12 Kanten, 120 Ecken) bricht hart ab (9, 16, 4 am oberen Rand).
    Die 120-Zelle (4 Kanten, 600 Ecken) traegt n = 7 und n = 8 als aufgespaltene Haufen weiter (24 + 16 + 9;
    24 + 36 + 4) und folgt dem Kontinuum enger.
  - Mit nur zwei Netzen laesst sich nicht trennen, ob das an der Kantenzahl oder an der Eckenzahl (Aufloesung) liegt;
    beide aendern sich hier gegenlaeufig. [M] Meine Lesart ist die Aufloesung.
  - Alles ist vorab ableitbar oder reine Mathematik am endlichen Graphen, keine Messung.

## 7. Selbstanzeigen

1. Um 06:12 lief auf der .69 einmal `fmhc-physics-gpu-venv/bin/python -c "import numpy, scipy; print(...)"`. Das war eine
   Versionsabfrage, keine Rechnung, aber nicht ueber kleintest.sh.
2. Chrome meldete beim Bildlauf "Failed to initialize vulkan surface" und "kTransientFailure". Das PNG entstand trotzdem.
   Ob die Canvas-Rasterung wirklich auf der GPU lief, habe ich nicht geprueft (kein nvidia-smi waehrend des Laufs).
3. Nicht verlangt, aber gebaut:
   - fuenf Pruefbilder in pruefbilder/;
   - Adresszusaetze in der HTML (#ring, #dunkel, #hell, #graph, #netz=120 oder beide, #xw= usw.), nur fuer diese Bilder.
     Sie speichern nichts.
4. Die 120-Zelle in der Ansicht leitet die Seite aus der eingebetteten Tetraederliste ab: Mitten normiert, Kanten ueber
   gemeinsame Dreiecke. Das ist Darstellung, nicht Laufdaten. Die Seite zeigt ihre Kantenzahl (1200) neben der aus lauf-69 (1200).
5. Den Paletten-Pruefer des dataviz-Skills habe ich nicht laufen lassen, weil er einen lokalen Interpreter braucht. Die
   Farben stammen von Hand aus den Referenzrampen. Die hellen Schalen 72 und 108 Grad haben auf hellem Grund wenig
   Kontrast; Umrandung, Legende und Tabelle tragen die Zuordnung mit.
6. Lauf 2 wartete rund 2,5 min am cpu-Lock auf einen fremden Lauf.
7. Um 06:13 lag kurz eine Hilfsdatei .kleintest-remote-check.txt im Kartenordner (Vergleich der kleintest.sh-Fassungen)
   und wurde gleich wieder geloescht. Die .69-Fassung kennt zusaetzlich die Spuren cpu8 bis cpu11; genutzt habe ich cpu und cpu2.
8. Welche Seite (Links- oder Rechtsmultiplikation) die 20er-Zerlegung liefert, hatte PLAN.md offen gelassen. Links: 20
   disjunkte Ringe, alle 600 Tetraeder. Rechts: 12 disjunkte Ringe mit 360 Tetraedern.
9. Die Formnamen der Schalen (Ikosaeder, Dodekaeder, Ikosidodekaeder) sind in Lauf 2 gerechnet: Grad und Kantenzahl des
   Naechste-Nachbarn-Graphen je Schale.
10. Die Deutung der 24er-Niveaus der 120-Zelle als Paar vertauschter Darstellungen ist [M], nicht gerechnet. Ebenso die
    Lesart "Aufloesung statt Kantenzahl".

## 8. Einfach gesagt

Die 600-Zelle ist ein Koerper in vier Dimensionen aus 600 gleichen Tetraedern; wir haben ihn aus 120 besonderen Zahlen
(Quaternionen) gebaut, und alle Pruefzahlen stimmen. Im flachen Raum bleibt um jede Kante eine kleine Luecke von 7,36 Grad;
auf der gekruemmten 3-Sphaere schliesst sie sich, und diese Luecken zusammen ergeben fast genau die Kruemmung der Kugel.
Wenn man das Netz "schwingen" laesst, kommen die Schwingungsmuster in Paketen von 1, 4, 9, 16, 25 und 36, genau wie die
Schalen im Wasserstoffatom, danach ist Schluss, weil 120 Punkte nicht mehr Muster tragen. Das Gegenstueck mit nur 4
Nachbarn je Punkt (die 120-Zelle) zeigt dasselbe Muster bis 36 und macht danach ungefaehr weiter. Das Muster kommt also aus
der Symmetrie, nicht aus der Zahl der Kanten, und war vorher ausrechenbar: ein schoenes Bild, aber keine neue Messung.
