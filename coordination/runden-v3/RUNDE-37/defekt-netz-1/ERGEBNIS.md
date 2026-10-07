# DEFEKT-NETZ-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 47, Kristall-Zweig)

- Karte KARTE.md unveraendert und bindend. Plan PLAN.md, eingefroren 2026-10-05 08:04:00 CEST
  (PLAN.md.eingefroren-20261005-080400, sha256 2e9b97d4...; code/dn.py 0cd5d13e...; Liste in EINGEFROREN-SHA256.txt,
  auf der .69 dieselben Summen in EINGEFROREN-SHA256-69.txt).
- Zeiten per date. Die .69 schreibt UTC (CEST = UTC + 2). Start 07:41:53 CEST, Rauchtests ab 07:59:51, Plantext ab
  08:02:27, eingefroren 08:04:00, Hauptlaeufe 06:04:18 bis 06:04:59 UTC, Text ab 08:08:04 CEST, Gegenlesen 08:12:06 bis
  08:23:14 CEST, Endfassung ab 08:27:58 CEST.
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen (Python 3.12.3, numpy 2.4.4, scipy 1.18.0
  der gpu-venv, 1 Thread). Keine Messdaten, keine Messdatenbestaetigung.
- **Kennzeichen:** [E] hier gerechnet, [M] Mathematik bzw. Codelesung, [P] Projektdatei, [S] Quelle, [K] Kopfrechnung
  aus gerechneten Werten, [H] Hypothese oder Lesart.
- **Begriffe:**
  - Spanne s = max/min - 1 von omega^2/k^2 ueber 52 Werte (13 Richtungen von TT-ISO-1 x 2 TT-Zweige x |k| = 1e-3,
    2e-3), wie in TT-ISO-1 fuer V.
  - Modell: Hamilton-Netz von EINE-WELT-LOCH-1 (A1R1, J = 1 je Tetraeder), Code tg.py aus TT-GLAS-1 unveraendert.
  - s misst das Quadrat der Geschwindigkeit. Die Geschwindigkeit selbst streut etwa halb so stark: 1,3 % (C15),
    0,47 % (A15), 3,1 % (V) [K].

## 1. Zeiten und Laeufe

Alle Laeufe ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Arbeitsordner
/home/fmh/fmhc-physics-remote/defekt-netz-1/, Aufruf `code/dn.py ...`, Logs in lauf/ bzw. rauch/ (absolute Pfade).
Vor dem Start waren cpu3 und cpu4 frei (kein Eintrag in /proc/locks, 06:04:10 UTC). TAKT-UMKLAPP-1 lief auf cpu8 bis
cpu10. Je Spur liefen die Laeufe nacheinander; keine Spur war doppelt belegt.

| Lauf | Spur | Aufruf (Argumente) | Start bis Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| r1 Rauch | cpu3 | dn0 --rauch --out rauch/r1-dn0.json | 05:59:51 bis 06:00:13 | 20,8 s | 0 |
| r2 Rauch (1. Versuch) | cpu4 | tt --netz C15 ... (falsches Arbeitsverzeichnis meiner ssh-Zeile; Log ueberschrieben, Selbstanzeige 6) | 05:59:51 | 0,04 s | 2 |
| r2 Rauch | cpu4 | tt --netz C15 --bauweg delaunay --rauch | 06:00:24 bis 06:01:02 | 36,9 s | 0 |
| r3 Rauch | cpu3 | tt --netz A15 --bauweg fk --rauch | 06:00:24 bis 06:00:31 | 5,8 s | 0 |
| r4 bis r10 Rauch | cpu3, cpu4 | ganze Kette ohne --rauch nach rauch/v-*.json (Absturzprobe; Werte nicht gelesen) | 06:01:19 bis 06:02:06 | 0,0 bis 23,8 s | 0 |
| Einfrieren | | | 06:04:00 | | |
| L0 | cpu3 | dn0 --out lauf/dn0.json | 06:04:18 bis 06:04:33 | 13,9 s | 0 |
| L1 | cpu3 | tt --netz C15 --dn0 lauf/dn0.json --out lauf/tt-C15.json | 06:04:33 bis 06:04:57 | 23,5 s | 0 |
| L3 | cpu4 | tt --netz V --out lauf/tt-V.json | 06:04:18 bis 06:04:22 | 2,8 s | 0 |
| L4 | cpu4 | tt --netz S --out lauf/tt-S.json | 06:04:22 bis 06:04:24 | 2,0 s | 0 |
| L2 | cpu4 | tt --netz A15 --dn0 lauf/dn0.json --out lauf/tt-A15.json (wartete auf das Ende von L0) | 06:04:34 bis 06:04:38 | 3,0 s | 0 |
| L7 | cpu4 | dn0 --out lauf/dn0-wdh.json (Wiederholung) | 06:04:38 bis 06:04:53 | 13,4 s | 0 |
| L5 | cpu3 | auswertung --dn0 lauf/dn0.json --tt lauf/tt-{C15,A15,V,S}.json --out lauf/auswertung.json | 06:04:57 bis 06:04:58 | 0,0 s | 0 |
| L6 | cpu3 | bild --tt lauf/tt-{C15,A15,V}.json --out lauf/bild-defekt-netz.json (PNG daneben) | 06:04:58 bis 06:04:59 | 0,9 s | 0 |
| N1 Nachtrag | cpu3 | code/nachtrag_bild.py lauf/bild-defekt-netz-v2.png lauf/tt-{C15,A15,V}.json | 06:07:15 bis 06:07:16 | 1,2 s | 0 |

- Alle Laeufe unter 10 min, ein Thread (OMP/OPENBLAS/MKL = 1, CPUQuota 100 %). Auf cpu4 liefen L3, L4, L2, L7 in
  dieser Reihenfolge (die Plantabelle nannte L2 zuerst; L2 brauchte dn0.json aus L0).
- lauf/PRUEFSUMMEN.txt (auf der .69 nach L7 erzeugt) besteht lokal: 17 von 17 Lauf-Dateien, 6 von 6 Code-Dateien.
  Alle Laufdateien nennen dn.py 0cd5d13e... (eingefroren); tt-C15, tt-A15 und auswertung nennen dn0.json 90564ea0....
  Den Nachtrag N1 deckt lauf/PRUEFSUMMEN-nachtrag.txt (3 von 3).
- **L7 gegen L0:** Ohne info, laufzeit_s, maxrss_MB und ende_utc ist dn0-wdh.json gleich dn0.json (gleiche sha256 nach
  jq -S).
- **Rauchkette gegen Hauptlaeufe (nachtraeglich, nur Hashes):** Ohne Zeit- und info-Felder sind rauch/v-*.json und
  lauf/*.json fuer dn0, tt-C15, tt-A15, tt-V, tt-S und auswertung bitgleich (jq -S auf der .69, sha256).

## 2. Ergebnis zuerst

1. **Beide Kristalle sind sauber gebaut [E].**
   - Die Delaunay-Zerlegung hat keinen Gleichstand: An jeder Umkugel liegen genau 4 Punkte. Der naechste fremde Punkt
     liegt mindestens 49,6 % (C15) bzw. 40 % (A15) des Radius weiter aussen.
   - Delaunay ist damit gleich der kristallographischen FK-Zerlegung (136 bzw. 46 Tetraeder).
   - Jede Kante traegt 5 oder 6 Tetraeder, q = 5,1 (C15) und 46/9 (A15) exakt. Die 16 6er-Kanten von C15 bilden das
     Diamantnetz der Mg, die 6 von A15 gerade Cr-Ketten.
   - **DN0 trifft ein**, wie vorab ableitbar.
   - Zusatz der Leitung, Punkt 3: Die volle kubische Symmetrie bleibt erhalten, das Grundtempo ist isotrop.
2. **C15 ist Finns Netz S [M, E].**
   - Die kantenaermere Fuellung S aus EINE-WELT-LOCH-1 ist, um (3/8, 3/8, 3/8) verschoben, Tetraeder fuer Tetraeder die
     C15-Zerlegung (136 von 136 gleich).
   - Deshalb war s(C15) = 2,6847 % schon vorhanden (TT-ISO-1, Netz S). Auch die Praemisse der Karte "Den Kristall-Zweig
     deckte bisher nur V ab" stimmte also nicht.
   - **DN1 (2,68 % < 6,34 %) und DN3 (2,68 % < 3 %) treffen ein, waren aber vorab aus Projektdaten ableitbar** (PLAN 1.1,
     vor jeder Hauptrechnung; Zeitpunkt siehe Selbstanzeige 3).
   - Die C15-Rechnung ist eine Reproduktion, keine Messung: s(C15) = 2,684718 % gegen 2,684717 % (S, TT-ISO-1).
3. **A15 ist das neue Ergebnis: s(A15) = 0,934 % [E].**
   - Das ist etwa ein Drittel von C15 (2,68 %) und ein Siebtel von V (6,34 %).
   - **DN2 (s(C15) < s(A15)) ist verfehlt**, nach Plan und nach Kartenwortlaut.
   - Fuer dieses eine Paar ist das Netz mit weniger Ikosaederplaetzen (A15: 1/4, C15: 2/3) das isotropere [E fuer die
     Zahlen, H fuer jede Verallgemeinerung].
4. **Alle drei Kristalle (C15, A15, V) sind regulaer [E].**
   - An allen 26 Messpunkten gibt es genau 2 masselose Moden, linear in k; nichts waechst. Auch an den 511 k des Gitters
     L = 8 waechst nichts.
   - Reine TT-Moden (TT-Anteil 1,000) sind sie in [100], [110] und [111]; dort ist der TT-Anteil gemessen (6 Werte je
     Netz). An den uebrigen 10 Richtungen sind die Moden nur gezaehlt.
   - Die Spanne ist in allen drei Netzen die Aufspaltung der zwei Polarisationen in [100]. Die Zweigmittel streuen ueber
     die Richtungen nur um 0,16 % (A15), 0,44 % (C15) bzw. 1,03 % (V).
5. **Bedeutung [H]:**
   - Fuer "DN1 trifft ein, DN2 verfehlt" hat die Karte keinen Bedeutungssatz; keiner der drei Saetze ist ausgeloest.
   - Im Kristall-Zweig gibt es jetzt ein Netz unter 1 % ohne jede Abstimmung (A15).
   - Die kubische Restanisotropie bleibt aber in allen drei Kristallen fest und liegt zwischen 0,9 und 6,3 %, weit
     entfernt von 1e-15.

## 3. Urteile DN0 bis DN3

Mechanisch durch code/dn.py auswertung (eingefroren), lauf-69/auswertung.json; Regeln PLAN Abschnitt 4.

| Nr | Vorhersage (Kartenwortlaut, Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| DN0 | Kontrolle: Delaunay gibt nur Tetraeder; jede Kante traegt 5 oder 6; q = 5,1000 (C15), 46/9 (A15) auf 1e-9; 6er-Kanten von C15 = Diamantnetz | 85 % | **eingetroffen** | **eingetroffen** | Gleichstaende 0 und 0; Punkte auf der Umkugel genau 4 an 136 + 46 Tetraedern; q 5,1 und 5,111111 (Abw. 0,0); Kanten C15 144 x 5, 16 x 6; A15 48 x 5, 6 x 6; Diamantprobe: alle 6 Teilproben wahr |
| DN1 | [H] s(C15) < s(V) = 6,34 % | 55 % | **eingetroffen** (vorab ableitbar) | **eingetroffen** (vorab ableitbar) | s(C15) = 0,02684718; s(V) = 0,06338808 (dieser Lauf; TT-ISO-1 0,06338810) |
| DN2 | [H] s(C15) < s(A15) | 55 % | **verfehlt** | **verfehlt** | s(C15) = 0,02684718 > s(A15) = 0,00933868 |
| DN3 | [H] s(C15) < 3 % | 30 % | **eingetroffen** (vorab ableitbar) | **eingetroffen** (vorab ableitbar) | s(C15) = 0,02684718 |

- **Vorab-Vermerk DN1 und DN3 [P, M, E]:**
  - Die Identitaet S = C15 stand im Plan (1.1) vor jeder Hauptrechnung. Die Verschiebung (3/8, 3/8, 3/8) und die
    Identitaetsprobe standen schon im Code, als r1 lief (r1-dn0.json nennt dn.py 0cd5d13e..., die eingefrorene Fassung).
  - L0 bestaetigt die Identitaet: 136 von 136 Tetraedern gleich, keiner nur in S oder nur in C15.
  - Mit s(S) = 0,026847167 aus TT-ISO-1 (lauf-69/gitter-S-A1R1.json) waren beide Urteile entschieden, sobald Delaunay =
    FK feststand. Diese Zahl ist keine neue Messung.
- **Vorab-Vermerk DN0 [M]:** Die Zaehlung (q, f6, 6er-Kanten) war vorab ableitbar (Leitung und PLAN 1.2). Gemessen ist
  hier nur, dass Delaunay nicht entartet und dieselben Tetraeder liefert.
- **Bauweg nach der Regel:** Gleichstaende 0 in beiden Kristallen, also Delaunay, wie die Karte sagt. Delaunay = FK; die
  Urteile gelten fuer beide Bauwege gleich.
- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - "DN1 und DN2 treffen ein" ist **nicht** ausgeloest (DN2 verfehlt).
  - "DN1 scheitert" ist **nicht** ausgeloest (DN1 eingetroffen).
  - "DN0 scheitert" ist **nicht** ausgeloest.
  - Den eingetretenen Fall (DN1 ja, DN2 nein) deckt die Karte nicht ab. Meine Lesart steht in Abschnitt 5 als [H].
- **Agenten-Vorhersagen** (PLAN 5, kein Urteil; notiert nach der Rauchkette, deren Werte ich nicht gelesen habe):
  A1 (DN0, Delaunay = FK) eingetroffen; A2 (Delaunay(C15) = S, s = 2,6847 % auf 1e-6) eingetroffen (Abweichung 6,4e-7);
  A3 (A15 regulaer) eingetroffen; A4 (s(A15) > s(C15)) verfehlt; A5 (s(A15) < s(V)) eingetroffen.

**Zusatz der Leitung (getrennt gekennzeichnet).** Er wirkt auf DN0 bis DN3 ueber den Bauweg. Die Gleichstands-Zaehlung
steckt ausserdem in der Plan-Regel DN0 (a), weil der Fehlerzweig der Karte Entartung als Scheitern von DN0 nennt
(Selbstanzeige 11).

| Punkt des Zusatzes | Ergebnis [E] |
|---|---|
| 1. Gleichstaende vor dem Bau zaehlen | C15: 0 Tetraeder mit 5 oder mehr Punkten auf der Umkugel (von 136), kleinste Marge 0,496 R; A15: 0 (von 46), Marge 0,400 R. An den FK-Tetraedern gezaehlt: dieselben Zahlen. Alle Umkugeln liegen mindestens 0,64 Zellkanten innerhalb des Kopienbereichs. |
| 2. Bei Gleichstaenden FK statt Zitter | Nicht noetig: Bauweg Delaunay. Delaunay = FK (Schluesselmengen gleich, 0 und 0 Abweichungen). |
| 3. Volle kubische Symmetrie, Grundtempo isotrop | Lagen: 192 Operationen (C15, 48 x 4 fcc) bzw. 48 (A15); unter keiner ist die Tetraedermenge verletzt. Grundtempo (skalarer Graph-Laplace, Einheitsgewichte): Spanne nach Richardson 2,7e-8 (C15), 8,1e-9 (A15), 5,3e-8 (V), Schwelle 1e-6, also isotrop. TT an 48 Bildern einer allgemeinen Richtung gleich auf 9,4e-8 (C15) bzw. 4,5e-8 (A15). Vorab ableitbar, nur Kontrolle. |
| Spanne wie TT-ISO-1, Stabilitaet, masselose TT-Moden | Abschnitt 4. Kontrolle: s(V) mit demselben Code 0,06338808, gegen TT-ISO-1 3,3e-7 relativ (Schwelle 1e-5). |

## 4. Tabellen

**4.1 Bau je Netz** (lauf-69/dn0.json; V und S aus tt-V.json, tt-S.json)

| Netz | Ecken / Kanten / Tetraeder je Zelle | Tetraeder je Kante | q = 6T/E | f6 | Gleichstaende | Bauweg | Koordination | Kantenlaengen (a = 1; Tetraeder je Kante) |
|---|---|---|---|---|---|---|---|---|
| C15 | 24 / 160 / 136 (kubisch) | 144 x 5, 16 x 6 | 5,1000000000 | 0,100 | 0 (Marge 0,496 R) | Delaunay (= FK) | 16 x Z12 (Cu), 8 x Z16 (Mg) | Cu-Cu 0,3536 (5), Mg-Cu 0,4146 (5), Mg-Mg 0,4330 (6) |
| A15 | 8 / 54 / 46 | 48 x 5, 6 x 6 | 5,1111111111 = 46/9 | 0,111 | 0 (Marge 0,400 R) | Delaunay (= FK) | 2 x Z12 (Si), 6 x Z14 (Cr) | Cr-Cr Kette 0,5000 (6), Cr-Si 0,5590 (5), Cr-Cr 0,6124 (5) |
| S (= C15) | 6 / 40 / 34 (primitiv) | nicht gezaehlt | 5,1 [K] | nicht gezaehlt | entfaellt | ew-Zellen | wie C15 | wie C15 |
| V | 10 / 68 / 58 (primitiv) | nicht gezaehlt | 5,118 [K] | nicht gezaehlt | entfaellt | ew-Zellen (Finns Fuellung) | | 0,2165 bis 0,4146 |

- Netzproben (Delaunay, beide Kristalle):
  - Volumensumme = Zellvolumen auf <= 4,4e-16; jedes der 272 (C15) bzw. 92 (A15) Dreiecke in genau 2 Tetraedern;
    Euler V - E + F - T = 0; Diedersumme je Kante 2 pi auf 8,9e-16; kein Punkt innen; kein von Qhull ausgelassener
    Punkt.
  - Diederwinkel C15 60,0 bis 74,2 Grad, A15 53,1 bis 78,5 Grad (V 35,3 bis 90,0). Kleinstes Volumen / Mittel: C15
    0,708, A15 0,958 (V 0,906).
- Diamantprobe C15 (alle wahr): nur Mg-Mg; Grad 4 an jedem Mg; Menge der 6er-Kanten = die 16 naechsten Mg-Mg-Paare;
  Vektoren (1/4)(+-1, +-1, +-1); Tetraederwinkel (Skalarprodukte -1/3); Vorzeichenprodukt -1 an 4 und +1 an 4 Mg (zwei
  sich abwechselnde Untergitter).
- Kettenprobe A15 (beschreibend): nur Cr-Cr, Laenge 0,5, je Cr zwei gegenlaeufige 6er-Kanten, je zwei Cr laengs x, y, z.
- Schalen: kein Paarabstand in +-0,03 um die Nachbarschwelle (0,52 bzw. 0,66); naechste Abstaende jenseits: 0,612
  (C15), 0,866 (A15).

**4.2 TT-Spektrum** (lauf-69/tt-*.json, auswertung.json)

| Groesse | C15 | A15 | V (Kontrolle) | S (Kontrolle) |
|---|---|---|---|---|
| Spanne s (52 Werte, Plan) | **2,6847 %** | **0,9339 %** | 6,3388 % | 2,6847 % |
| omega^2/k^2 min / max / Mittel | 0,21130 / 0,21698 / 0,21478 | 0,61481 / 0,62055 / 0,61709 | 0,11889 / 0,12643 / 0,12179 | 0,21130 / 0,21698 / 0,21478 |
| [100]: unterer / oberer Zweig (\|k\| = 1e-3) | 0,211303 / 0,216976 | 0,614811 / 0,620553 | 0,118890 / 0,126426 | wie C15 |
| [110] | 0,212752 / 0,216976 | 0,614811 / 0,619454 | 0,118890 / 0,124353 | wie C15 |
| [111] (entartet) | 0,215085 | 0,616725 | 0,121402 | wie C15 |
| Spanne an 23 ew-Richtungen / 91 Keil-Richtungen (beschreibend) | 2,6847 % / 2,6847 % | 0,9339 % / 0,9339 % | 6,3388 % / 6,3388 % | 2,6847 % / 2,6847 % |
| Richtungsspanne der Zweigmittel / groesste Aufspaltung | 0,44 % / 2,68 % | 0,16 % / 0,93 % | 1,03 % / 6,34 % | 0,44 % / 2,68 % |
| Grundtempo c (skalar), Spanne nach Richardson | 0,5951; 2,7e-8 | 0,8660; 8,1e-9 | 0,5477; 5,3e-8 | 0,5951; 3,4e-8 |
| TT an 48 Bildern, groesste Abweichung | 9,4e-8 | 4,5e-8 | 1,7e-7 | 3,4e-8 |
| masselose Moden je Punkt (26 Punkte) | 2 an 26 | 2 an 26 | 2 an 26 | 2 an 26 |
| TT-Anteil min ([100], [110], [111], 6 Werte) | 1,000 | 1,000 | 1,000 | 1,000 |
| linear (2e-3 gegen 1e-3), max | 7,8e-8 | 8,5e-8 | 1,1e-7 | 5,2e-8 |
| wachsend / unklar an den 26 Punkten | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| reduzierte Bewegungsmatrix pos. definit / Lagematrix ohne neg. Richtung | 26 / 26 | 26 / 26 | 26 / 26 | 26 / 26 |
| kleinster Lueckenwert omega^2 | 5,24 | 5,33 | 3,43 | 5,82 |
| Gitter L = 8 der Zelle (511 k): k mit Wachstum; kleinstes omega^2/max | 0; 0,0104 | 0; 0,0198 | 0; 0,0145 | 0; 0,0311 |
| Keil 91 Richtungen: (masselos, wachsend, unklar) | (2, 0, 0) an 91 | (2, 0, 0) an 91 | (2, 0, 0) an 91 | (2, 0, 0) an 91 |
| Superzelle 2 x 2 x 2, Abweichung an [100], [110], [111] | 9,2e-8 (192 Ecken) | 3,2e-8 (64 Ecken) | nicht gerechnet | nicht gerechnet |
| affine Regge-Steifigkeit / Volumen: min, max, Spanne | 0,9999995; 0,9999995; 3,5e-8 | 0,9999989; 0,9999991; 2,4e-7 | 0,9999995; 0,9999998; 2,2e-7 | 0,9999995; 0,9999995; 3,5e-8 |

- Absolutwerte von omega^2/k^2 sind eine Festlegung (Skala a = 1, J = 1 je Tetraeder; sie skalieren wie a^3) [M]. Nur
  die Spannen sind vergleichbar.
- Die Spanne ist in allen drei Kristallen die Aufspaltung der Polarisationen in [100] (auf 1e-8 genau). Je ein Zweig
  ist fuer k in einer Wuerfelebene konstant (C15 der obere 0,216976; A15 und V der untere). Darum liegen die
  numerischen Extrema teils auch in [110] oder [210], mit Unterschieden unter 1e-8.
- C15 und S sind dasselbe Netz in verschiedenen Zellen (kubisch mit 24 Ecken, primitiv mit 6). Die kubische Zelle faltet
  Zweige zurueck, und ihr Gitter L = 8 enthaelt andere k. Darum unterscheiden sich der kleinste Lueckenwert (5,24 gegen
  5,82) und das kleinste omega^2/max auf dem Gitter (0,0104 gegen 0,0311) [M]. Die masselosen Werte sind gleich
  (Superzellen- und S-Vergleich).
- **Bild:** lauf-69/bild-defekt-netz-v2.png (Nachtrag N1, Legende verschoben) bzw. lauf-69/bild-defekt-netz.png (L6,
  eingefrorener Code; dort laeuft die V-Kurve durch die Legende).
  - Gezeigt: omega^2/k^2 beider Zweige relativ zum Mittel je Netz laengs [100] -> [110] -> [111] -> [100].
  - V schwankt um +3,8 / -2,4 %, C15 um +1,0 / -1,6 %, A15 um +0,6 / -0,4 %.
- **Numerik [E]:**
  - B hermitesch auf 3,9e-16, B M = 0 auf 5,0e-16, c M = 0 auf 1,4e-15 (C15, [100]).
  - Der kleinste relative Singulaerwert von [M, c] an den 13 Richtungen (|k| = 1e-3) betraegt 1,2e-8 (C15), 3,4e-8
    (A15) bzw. 6,2e-9 (V); er waechst wie k^2. Die Rangschwelle liegt bei 1e-9, bei V also nur um den Faktor 6 unter
    dem kleinsten Wert.
    Der Rang ist ueberall voll, und V gibt mit diesem Weg dieselbe Spanne wie TT-ISO-1 (anderer Rechenweg) auf 3,3e-7.

## 5. Bedeutung fuer Finns Weiche Kristall / Glas [H]

- **Kristall-Zweig, jetzt drei Netze** (alle regulaer, alle ohne Abstimmung, J = 1):
  - V 6,34 %, C15 (= S) 2,68 %, A15 0,93 %.
  - Die Anisotropie ist fest. Fuer C15 und A15 ist sie in der Superzelle 2 x 2 x 2 dieselbe (auf 1e-7).
  - In allen drei sitzt sie als Doppelbrechung in [100]: Die zwei Polarisationen laufen dort verschieden schnell. Das
    Mittel der Zweige ist viel gleichmaessiger (0,16 bis 1,03 %).
- **Glas-Zweig (TT-GLAS-1 [P]):**
  - Bisher gerechnete Glasproben: 11,4 % +- 1,9 % bei N = 256 (12 Netze) und eine Probe mit 7,2 % bei N = 512. A15
    (0,93 %) und C15 (2,68 %) liegen darunter.
  - Nach der Geraden von TT-GLAS-1 (Exponent -0,47) erreichte eine typische Glasprobe die Spanne von C15 erst bei
    N ~ 5 500 und die von A15 bei N ~ 50 000 Punkten [K, grob].
  - Die Messung dort war etwas anders: 26 Werte an 13 Wuerfelachsen, |k| = 1e-2.
- **Was die Karte erwartete und was nicht eintritt:**
  - Die Karte las fuer den Fall "DN1 und DN2" die ikosaedrische Nahordnung (600-Zellen-Mitte) als Weg zur
    TT-Isotropie. Fuer dieses Paar ist das Gegenteil gerechnet: A15 (1/4 Ikosaeder) ist knapp dreimal so isotrop wie
    C15 (2/3 Ikosaeder).
  - Lesart [H]: Der Anteil ikosaedrischer Plaetze ordnet die kubische Anisotropie nicht, jedenfalls nicht allein. Das
    beruht auf einem einzigen Paar. Eine Zerlegung nach Kugelfunktionen ist nicht gerechnet; die Zweigmittel von C15 sind
    nicht rein l = 4 (Verhaeltnis ([100] - [111]) / ([110] - [111]) = 4,27 statt 4,0 [K]).
  - Eine einfache Formzahl ordnet die drei Netze auch nicht. Die Volumen-Gleichmaessigkeit (kleinstes / mittleres
    Volumen) trennt A15 (0,96) von C15 (0,71), aber V (0,91) ist am anisotropsten. V hat dafuer die staerksten
    Verzerrungen (Diederwinkel 35 bis 90 Grad gegen 53 bis 78 bzw. 60 bis 74 Grad) [E fuer die Zahlen, H fuer die
    Lesart].
  - Ein Unterschied der Defektnetze faellt auf [H, nicht gerechnet]: In A15 laufen die 6er-Linien als gerade Ketten in
    drei senkrechten Richtungen, in C15 als Diamantnetz. Ob das die Doppelbrechung in [100] ordnet, ist offen.
- **Fuer Finns Weiche:**
  - Beide Zweige liefern Restanisotropie. Der Kristall-Zweig hat feste Prozent-Werte, die von der Zelle abhaengen. Der
    Glas-Zweig hat zufaellige, die mit der Probengroesse fallen.
  - Fuer c_T/c - 1 ~ 1e-15 reicht keiner der drei Kristalle ohne Abstimmung.
  - Mit Abstimmung: In TT-ISO-1 kamen V mit zwei Gewichtsverhaeltnissen auf 1,1e-5 und S, also C15, auf 4,3e-6 (mit
    allen Arten 2,2e-6) [P]. Ob A15 mit weniger oder ohne Abstimmung tiefer kommt, ist nicht gerechnet.
- **Naechste Schritte (Vorschlag, nicht gerechnet):** weitere FK-Kristalle (Z, sigma, C14) gegen dieselbe Messung, um zu
  sehen, was die Rangfolge V > C15 > A15 ordnet; A15 mit Bewegungsgewichten wie TT-ISO-1.

## 6. Selbstanzeigen

1. **Vorab ableitbar, gegen die Ableitbarkeitsprobe der Leitung:** DN1 und DN3 waren ueber die Identitaet S = C15 aus
   TT-ISO-1 entschieden. Das steht im Plan (1.1) vor jeder Hauptrechnung und ist in L0 bestaetigt. Die Karte nannte DN1
   bis DN3 "nicht ableitbar" und schrieb, den Kristall-Zweig habe bisher nur V abgedeckt. Neu gemessen ist nur DN2 (A15).
2. **Quelle:** Die zwei AFLOW-Adressen gaben 404. Gelesen habe ich den NRL-Spiegel atomic-scale-physics.de (c15.html,
   a15.html), also weder Bilbao noch AFLOW. Zusammen 4 Abrufe, die Grenze ist eingehalten. Die Lagen dort decken sich
   mit meinem Gedaechtnis [L] und mit Finns Netz S (1.1). Die Abrufzeit "gegen 07:51 CEST" im Plan ist geschaetzt; per
   date belegt ist nur: nach 07:41:53 und vor 07:50:55 CEST.
3. **Zeitpunkt des Plans:** Die Rauchtests r1 bis r10 liefen vor dem Plantext (ab 07:59:51 CEST, Plan ab 08:02:27). Die
   Ueberschriften im eingefrorenen Plan, "Ableitbarkeitsprobe (vor jeder Rechnung)" und "Agenten-Vorhersagen (vor der
   Rechnung)", stimmen deshalb nicht genau. Richtig ist: vor jeder Hauptrechnung, nach der Rauchkette.
4. **Rauchkette r4 bis r10 ohne --rauch:** Sie erzeugte vor dem Einfrieren alle Werte (rauch/v-*.json), um auswertung
   und bild auf Absturz zu pruefen. Gelesen habe ich nur Rueckgabewerte, Laufzeiten und die Dateiliste, keine Werte und
   nicht das Bild. Das laesst sich von aussen nicht pruefen. Nachtraeglich per Hash verglichen: Die Rauchwerte sind ohne
   Zeit- und info-Felder bitgleich mit den Hauptlaeufen (Abschnitt 1). Die Agenten-Vorhersagen A1 bis A5 entstanden
   nach dieser Kette.
5. **Delaunay nicht mit demselben Code wie TT-GLAS-1:** Die Karte verlangt woertlich "denselben Code". dn.py baut die
   Zerlegung mit einer eigenen Funktion: 27 volle Kopien statt Saum-Kopien, generische Zuordnungsverschiebung, Schluessel
   je Tetraeder. Der Weg ist derselbe (scipy Delaunay auf periodischen Kopien, je Tetraeder eine Kopie in der Zelle),
   der Code nicht; tg.zufallsnetz erzeugt Zufallspunkte und laesst sich nicht direkt verwenden. Das stand im Plan
   (Abschnitt 2), hier nachgetragen. An den Ergebnissen aendert es nichts (keine Gleichstaende, Delaunay = FK).
6. **r2, erster Versuch:** Meine ssh-Zeile setzte das Arbeitsverzeichnis nur fuer den ersten Hintergrundauftrag; der
   zweite lief in /home/fmh und fand code/dn.py nicht (rc 2, keine Ausgabe). Die Wiederholung schrieb in dieselbe
   Logdatei; das Log des ersten Versuchs ist dadurch ueberschrieben.
7. **Nachtrag nach dem Einfrieren:** code/nachtrag_bild.py (neue Datei, beschreibend, kein Urteil) zeichnet dasselbe
   Bild mit verschobener Legende, weil im L6-Bild die V-Kurve durch den Legendentext lief. dn.py ist unveraendert; beide
   Bilder liegen vor.
8. **Nicht gespeichert, obwohl im Plan genannt:** die Klassenzaehlung an den 23 ew-Richtungen und an den 73
   Pfad-Richtungen. Gespeichert sind dort nur die zwei masselosen Werte (an allen 73 Pfad-Richtungen vorhanden). Die
   Klassen stehen fuer die 26 Plan-Punkte, die 48 Bilder (nur Zahl der Punkte ohne zwei Werte: 0) und die 91
   Keil-Richtungen.
9. **Harness-Dateien unter /tmp/claude-1000:** ssh-Befehle und das Warten auf den Gegenleser liefen ueber die
   Hintergrund-Option des Werkzeugs. Das Werkzeug schreibt deren Bildschirmausgabe (Logzeilen, rc, Dateiliste) nach
   /tmp/claude-1000/.../tasks/. Ich selbst habe dort nichts angelegt; die Regel "nie nach /tmp/claude-1000" ist damit
   dem Buchstaben nach beruehrt.
10. **jq und sed:** jq habe ich ueber das Lesen hinaus genutzt: einmal min ueber eine Liste (kleinster
    Singulaerwert), einmal length und select zum Zaehlen, zweimal jq -S mit del bzw. walk und sha256sum fuer Vergleiche
    (L0 gegen L7 lokal; Rauch gegen Haupt auf der .69). sed nur in Pipes (Pfadersetzung fuer sha256sum -c), nicht an
    Dateien. Lokal lief kein python, awk oder perl.
11. **DN0-Regel (a)** liest "nur Tetraeder" als: keine Gleichstaende, kein Punkt innen, positive Volumina,
    Volumensumme, jedes Dreieck zweimal. Das ist mehr als der Wortlaut, folgt aber aus dem Fehlerzweig der Karte
    ("entartet, kosphaerische Punkte"). Plan und Wortlaut sind deshalb gleich gewertet.
12. **Grundtempo** ist hier der skalare Graph-Laplace mit Einheitsgewichten (wie DANZER S), nicht Maxwell. Fuer die
    Symmetriekontrolle reicht das; die TT-Probe an 48 Bildern und die Raumgruppenprobe der Tetraedermenge sind staerker.
13. **Zahlen von Hand [K]:** Prozentwerte, Rundungen, die Geschwindigkeits-Spannen, q(V) = 6 x 58/68, die Verhaeltnisse
    der Spannen, das l = 4-Verhaeltnis 4,27 und die Glas-Hochrechnung. Die Glas-Hochrechnung nutzt das Mittel bei N = 256
    und den Exponenten aus TT-GLAS-1; sie ist grob.
14. **Gegenlesen:** Ein frischer Leser (pruefer-opus, nur lesend, 08:12:06 bis 08:23:14 CEST nach seiner Messung)
    pruefte rund 250 Zahlen und fand die Urteilszuordnung DN0 bis DN3 korrekt. Er meldete einen A-Befund (die
    Zeitangabe "vor jeder Rechnung"), fuenf B-Befunde (Geschwindigkeit gegen ihr Quadrat im Einfach-gesagt-Teil;
    "isotroper als jede Glasprobe" zu stark; TT-Anteil nur an 3 Richtungen gemessen; fehlende Selbstanzeige zum
    Delaunay-Code; Lesart "l = 4" und Ikosaeder-Rangfolge zu stark) und etwa ein Dutzend C-Befunde (unter anderem
    N ~ 5 000 statt ~ 5 500, "1 bis 6 %", die Feldliste L0/L7, Extrema nur auf 1e-8 in [100], Gitterwerte C15 gegen S,
    fehlende Klassen an 23 und 73 Richtungen, Reihenfolge auf cpu4, geschaetzte Abrufzeit, Trennung des Zusatzes).
    Ich habe alle uebernommen; kein Urteil hat sich geaendert. Diese Endfassung hat er nicht mehr gesehen.

## 7. Einfach gesagt

Wir haben zwei echte Kristallbauweisen aus der Metallkunde, C15 und A15, als Netze aus Tetraedern gebaut und darauf am
Computer Schwerewellen laufen lassen. Ueberraschung eins: C15 ist genau ein Netz, das wir schon hatten; seine Zahl war
also schon bekannt: Das Quadrat der Wellengeschwindigkeit haengt um 2,7 % von der Richtung ab, die Geschwindigkeit
selbst um etwa 1,3 %. Ueberraschung zwei: A15 ist mit 0,9 % (Geschwindigkeit etwa 0,5 %) noch gleichmaessiger, obwohl
es weniger von der "Ikosaeder-Ordnung" hat, die wir fuer den Schluessel hielten. Beide Kristalle und Finns Netz V haben
genau die zwei Schwerewellen-Arten, und bei den gerechneten Wellen schaukelt sich nichts auf. Jeder behaelt aber einen
festen Rest an Richtungsabhaengigkeit, der weit groesser ist als die Genauigkeit, mit der man die Geschwindigkeit
echter Schwerewellen kennt (etwa 1e-15).

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261005-080400, EINGEFROREN-SHA256.txt (lokal), EINGEFROREN-SHA256-69.txt (.69).
- code/: dn.py (neu; Bau, Gleichstaende, Symmetrie, Spektrum, Urteile, Bild) mit .eingefroren-20261005-080400;
  tg.py (TT-GLAS-1), tti.py, nachtrag_kinetik.py (TT-ISO-1), ew.py, tp.py unveraendert, je mit eingefrorener Kopie;
  nachtrag_bild.py (Nachtrag N1).
- lauf-69/: dn0.json, dn0-wdh.json, tt-C15.json, tt-A15.json, tt-V.json, tt-S.json, auswertung.json,
  bild-defekt-netz.png (+ .json), bild-defekt-netz-v2.png, Logs L0 bis L7 und N1, PRUEFSUMMEN.txt,
  PRUEFSUMMEN-nachtrag.txt.
- rauch-69/: Logs r1 bis r10, r1-dn0.json, r2-ttC15.json, r3-ttA15fk.json (nur Schluessel). Die Werte der Rauchkette
  (v-*.json) liegen nur auf der .69 in rauch/.
- Auf der .69: /home/fmh/fmhc-physics-remote/defekt-netz-1/ (code/ schreibgeschuetzt, lauf/, rauch/).

Abschluss der Datei 2026-10-05 08:30:08 CEST (date). Zeitbox 120 min ab 07:41:53 CEST (bis 09:41:53) eingehalten; kein eigener
Lauf mehr aktiv (0 Units fmhc-physics-klein-dn-* auf der .69). Journal, Peerbus und Commit uebernimmt die Leitung.
