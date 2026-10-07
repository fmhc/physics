# DANZER-TT-1: Ergebnis (Runde 48, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. KARTE.md unveraendert und bindend.
- Plan PLAN.md eingefroren 2026-10-05 10:53:30 CEST (PLAN.md.eingefroren-20261005-105330, code/dtt.py.eingefroren-...,
  code/kette-cpu{8,9,10}.sh.eingefroren-..., EINGEFROREN-SHA256.txt). Auf der .69 dieselben Pruefsummen
  (EINGEFROREN-SHA256-69.txt dort). Code nach dem Einfrieren unveraendert; Laufketten geaendert (Selbstanzeige 10).
- **Zeiten (date; die .69 schreibt UTC, CEST = UTC + 2):**
  - Start 10:25:53 CEST; Code ab etwa 10:31; Rauchtests 08:40:23 bis 08:52:33 UTC; Plantext ab 10:47:46 CEST;
    eingefroren 10:53:30 CEST.
  - Laufketten 08:53:45 bis 09:58:04 UTC; Auswertung L99 09:58:09 bis 09:58:11 UTC; Text ab 11:21 CEST.
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen (Python 3.12.3, numpy 2.4.4, scipy 1.18.0
  der gpu-venv, 1 Thread). Keine Messdaten, keine Messdatenbestaetigung.
- **Kennzeichen:** [E] hier gerechnet, [M] eigene Mathematik (ungeprueft), [P] Projektdatei, [K] Kopfrechnung aus
  gerechneten Werten, [R] aus Rauchtests (vor dem Plan gesehen), [H] Hypothese oder Lesart.
- **Begriffe:**
  - Spanne s = max/min - 1 von omega^2/k^2 ueber 52 Werte: 13 Richtungen von TT-ISO-1 x 2 TT-Zweige x |k| = 1e-3, 2e-3.
    s misst das Quadrat der Geschwindigkeit; die Geschwindigkeit selbst streut etwa halb so stark.
  - s26 = dieselbe Groesse ueber 26 Richtungen (die 13 von TT-ISO-1 und die 13 Wuerfelachsen von TT-GLAS-1) bei
    |k| = 1e-3. Beschreibend, nur 1/1 und 2/1.
  - Modell: Hamilton-Netz A1R1 mit J = 1 je Tetraeder (tg.py aus TT-GLAS-1, unveraendert) auf den Ammann-Kramer-
    Naeherungen von DANZER-NAEHERUNG-2 (gleiche Ecken, gleiche Delaunay-Zerlegung, gleiche Saaten).
  - "duenn" = neuer Rechenweg dieser Karte (Sattelpunkt-LU, Block-Inversiteration, Rayleigh-Ritz; PLAN 2); "dicht" =
    tg.punkt (alle Eigenwerte).

## 1. Zeiten und Laeufe

Alle ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Arbeitsordner /home/fmh/fmhc-physics-remote/danzer-tt-1/,
Aufruf `code/dtt.py ...`, Logs in lauf/ (absolute Pfade in den Ketten). Ein Thread (OMP/OPENBLAS/MKL = 1), CPUQuota 100 %,
MemoryMax 4G, RuntimeMaxSec 600. Rauchtests R1 bis R14 siehe PLAN 5. Laufzeit = "Service runtime" aus dem Log.

| Lauf | Spur | Inhalt (dtt.py netz ..., Kurzform) | Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| L01 | cpu8 | kontrolle: V, A15, C15 (duenn und dicht, 26 Punkte, affin) | 08:53:48 | 3,4 s | 0 |
| L02 | cpu8 | 1/1 Saaten 0 bis 7: 13 Richtungen x 2 \|k\|, dicht, Wuerfelachsen, affin, Gitter Lk = 8, dn2 | 08:56:20 | 2 min 32 s | 0 |
| L03 | cpu8 | 1/1 Saat 0 Zitter 1 (wie L02, ohne affin) | 08:56:39 | 20 s | 0 |
| L04 | cpu8 | 2/1 Saat 0 (dicht an allen 26 Punkten, Wuerfelachsen, affin, Gitter Lk = 4, dn2) | 09:00:25 | 3 min 46 s | 0 |
| L05 bis L07 | cpu8 | 2/1 Saaten 1, 2 / 3, 4 / 5, 6 (Wuerfelachsen, affin, Gitter Lk = 4, dn2) | 09:06:25 / 09:12:19 / 09:18:11 | je 5 min 52 s bis 5 min 58 s | 0 |
| L08 | cpu8 | 2/1 Saat 7 | 09:21:07 | 2 min 56 s | 0 |
| L09 | cpu8 | 2/1 Saat 0 Zitter 1 (Wuerfelachsen, dn2) | 09:22:17 | 1 min 8 s | 0 |
| L20a bis d | cpu9 | 3/2 Saat 0: Richtungen 0 bis 6 / 7 bis 12 x 1e-3 / 2e-3 (a mit dn2, affin) | 09:01:52 bis 09:17:29 | 8 min 8 s; 4 min 51 s; 5 min 48 s; 4 min 58 s | 0 |
| L21a, b | cpu9 | 3/2 Saat 1, Teile a, b | 09:26:07; 09:31:39 | 8 min 37 s; 5 min 32 s | 0 |
| L21c, d | cpu9 | 3/2 Saat 1, Teile c, d (aus den Ersatzketten, Selbstanzeige 10) | 09:37:39; 09:42:55 | 6 min 0 s; 5 min 16 s | 0 |
| L22a bis d | cpu10 | 3/2 Saat 2 | 09:01:49 bis 09:17:51 | 8 min 4 s; 5 min 6 s; 5 min 52 s; 5 min 2 s | 0 |
| L23a bis d | cpu8 | 3/2 Saat 3 | 09:31:12 bis 09:49:09 | 8 min 55 s; 4 min 48 s; 6 min 33 s; 6 min 35 s | 0 |
| L24a | cpu9 | 3/2 Saat 4, Teil a | 09:52:55 | **10 min 0 s, abgebrochen (RuntimeMaxSec)** | 1 |
| L24b, c, d | cpu8, cpu10, cpu9 | 3/2 Saat 4, Teile b, c, d (Ersatzketten) | 09:54:54; 09:56:33; 09:58:04 | 5 min 41 s; 6 min 50 s; 5 min 10 s | 0 |
| L30 | cpu10 | 3/2 Saat 0, dicht an [100] (1e-3, mit TT-Anteil) | 09:20:49 | 2 min 58 s | 0 |
| L31a bis c | cpu10 | 3/2 Saat 0, Gitter Lk = 2 dicht (3 + 2 + 2 k) | 09:27:18 bis 09:35:38 | 6 min 27 s; 4 min 14 s; 4 min 4 s | 0 |
| L32a, b | cpu10 | 3/2 Saat 0 Zitter 1, nur 1e-3 (a mit dn2) | 09:43:50; 09:49:33 | 8 min 12 s; 5 min 41 s | 0 |
| Z1 bis Z6 | cpu8, cpu10 | Zwischenauswertungen (Selbstanzeige 4) | 09:00:28 bis 09:49:43 | je 2 bis 2,4 s | 0 |
| L99 | cpu8 | auswerten ueber alle 34 Lauf-Dateien (lauf-69/L99-eingaben.txt), mit Bild | 09:58:11 | 2,0 s | 0 |

- Saat 4 bei 3/2 ist unvollstaendig: L24a brach nach 600 s im siebten Punkt ab (Punkt [110] brauchte bei hoher Last
  161 s statt etwa 105 s). Die Teile b und d (Richtungen 7 bis 12 bei beiden |k|, 12 Punkte) zaehlen nur in der
  Stabilitaet; Teil c (nur 2e-3) wertet dtt.py auswerten nicht aus. Einen Ersatz fuer L24a habe ich nicht gestartet.
- Alle anderen Laeufe endeten regulaer unter 600 s; der laengste regulaere Lauf war L23a mit 535 s.

## 2. Ergebnis zuerst

1. **Die TT-Spanne faellt von Stufe zu Stufe, bleibt aber gross [E]:** Saatmittel 12,2 % (1/1, 8 Saaten), 6,2 % (2/1,
   8 Saaten), 2,6 % (3/2, 4 Saaten; Saat 4 unvollstaendig). Zum Vergleich A15 0,934 %, C15 2,68 %, V 6,34 %.
   - DT1 ist nach Plan eingetroffen (3/2 : 1/1 = 0,215), nach strengem Wortlaut nicht (groesste 3/2-Saat gegen
     kleinste 1/1-Saat: 0,43).
   - DT3 ist nicht eingetroffen: Alle vier 3/2-Saaten liegen ueber A15 (1,17 bis 3,29 %), das Mittel ist 2,8-mal so
     gross [K].
2. **Alle Naeherungen sind stabil und regulaer [E]:** kein wachsender Mode an 5 941 gerechneten k-Punkten (davon 5 371 mit
   vollem Spektrum). An allen Spektrum-Punkten (682 duenn, dazu die dichten) genau zwei masselose Moden; an [100],
   [110], [111] reine TT-Moden (TT-Anteil 1,000). DT2 eingetroffen.
3. **Der neue Rechenweg ist geprueft [E]:** Auf V gibt er 6,33881 % (TT-ISO-1: 6,33881 %, Abweichung 1,7e-8; DT0
   eingetroffen), auf A15 und C15 die Werte von DEFEKT-NETZ-1. Gegen tg.punkt weicht er an allen Vergleichspunkten um
   hoechstens 8,4e-8 ab.
4. **Die Spanne haengt vor allem an der Zerlegung der Gleichstaende [E, H]:**
   - In jeder Stufe haben 41 bis 42 % der Delaunay-Tetraeder weitere Ecken auf ihrer Umkugel. Die A1-Masse (J = 1 je
     Tetraeder) haengt von der willkuerlichen Zerlegung dort ab.
   - Gleiche Ecken mit anderem Zitter: 1/1 9,0 -> 13,1 %, 2/1 2,6 -> 4,5 %, 3/2 1,2 -> 2,6 % (nur |k| = 1e-3).
     Saaten mit gleichen Ecken liegen bis Faktor 2,3 auseinander.
   - Der Abfall je Stufe (0,51 bei 2/1 : 1/1, 0,43 bei 3/2 : 2/1) trennt die Glas-Mittelung (0,50) nicht von der
     Phason-Regel (0,38): Die erste Stufe passt zum Glas, die zweite liegt dazwischen.
5. **Bedeutung [H]:** Der Kartensatz fuer "DT1 und DT2 treffen ein" ist nach Plan formal ausgeloest. Die Rechnung zeigt
   aber nicht, dass die Ikosaeder-Ordnung der Grund ist: Mit dieser Masse ist jede Naeherung zu gut 40 % ein Glas. Fuer
   den Symmetrie-Test braucht es eine Masse ohne Zerlegungsabhaengigkeit. Von GW170817 (1e-15) ist jede Stufe weit
   entfernt.

## 3. Urteile DT0 bis DT3

Mechanisch nach PLAN.md Abschnitt 6 (dtt.py auswerten, eingefroren; lauf-69/auswertung.json, Feld urteile).

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. (Leitung) | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| DT0 | Kontrolle: Der TT-Code gibt auf V die TT-ISO-1-Spanne 6,34 % auf 1e-3 wieder | 90 % | **eingetroffen** | **eingetroffen** | s_V = 0,06338810 (duenn); gegen TT-ISO-1 1,7e-8, gegen 6,34 % 1,9e-4 relativ; V regulaer |
| DT1 | [H] Die TT-Spanne faellt von 1/1 zu 3/2 auf hoechstens ein Drittel | 50 % | **eingetroffen** | **nicht eingetroffen** (streng) | Saatmittel 1/1 12,20 % (8 Saaten), 3/2 2,63 % (4 Saaten): R = 0,215; streng: groesste 3/2-Saat 3,29 % / kleinste 1/1-Saat 7,66 % = 0,429 |
| DT2 | [H] 1/1 bis 3/2 an allen gerechneten k stabil | 60 % | **eingetroffen** | **eingetroffen** | 0 wachsende Moden an 5 941 gerechneten k-Punkten (1/1: 4 950, 2/1: 855, 3/2: 136), davon 5 371 mit vollem Spektrum (3/2: 8); A_red ueberall positiv definit, B_red ohne negative Richtung (dicht geprueft) |
| DT3 | [H] Bei 3/2 liegt die TT-Spanne ohne Abstimmung unter A15 (0,934 %) | 45 % | **nicht eingetroffen** | **nicht eingetroffen** | 3/2: Saaten 1,17 / 3,06 / 3,29 / 2,98 %, Mittel 2,63 %; s_A15 = 0,934 % |

- **DT0 war vorab praktisch entschieden** (PLAN 7): Der dichte Weg ist die Rechnung von DEFEKT-NETZ-1, der duenne Weg
  war im Rauchtest auf 5e-8 gleich. Geprueft ist der neue Rechenweg, keine Physik.
- **DT1, Lesarten:** Plan = Verhaeltnis der Saatmittel. Kartenwortlaut streng gelesen = jede gerechnete 3/2-Saat gegen
  die kleinste 1/1-Saat. Die Saatstreuung ist gross (SD/Mittel 37 % bei 1/1 und 3/2). Ohne die kleinste 3/2-Saat
  (Saat 0) waere R = 0,25, mit deren Zitter-Netz statt Saat 0 (nur 1e-3) 0,24 [K]; beides unter 1/3.
- **DT2, Umfang:** "An allen gerechneten k" heisst hier: An allen Spektrum-Punkten (duenn: nur die zwei tragenden Werte),
  an den dichten Gegenprobe-Punkten und an den Gittern (dicht: alle Eigenwerte, A_red, B_red). Voll geprueft sind
  5 371 k-Punkte, davon bei 3/2 nur 8 (Saat 0).
- **DT3:** Keine 3/2-Saat erreicht A15. Die kleinste (Saat 0, 1,17 %) liegt 25 % darueber [K] und steigt mit anderem
  Zitter auf 2,59 % (nur 1e-3).
- **Bedeutung laut Karte (vorab):**
  - "DT1 und DT2 treffen ein: Ikosaedrische Ordnung ist ein Grund fuer die Richtungsgleichheit der Schwerewellen, ohne
    Abstimmung, und damit emergent. Der Quasikristall-Zweig waere fuer GW170817 der natuerliche Kandidat."
    Nach Plan formal ausgeloest (DT1 und DT2 eingetroffen). Die Lesart "Grund = ikosaedrische Ordnung" stuetzt die
    Rechnung aber nicht (Abschnitte 2 und 5): Der Abfall ist mit Glas-Mittelung ebenso vertraeglich, und die Spanne haengt
    an der zufaelligen Zerlegung.
  - "DT1 verfehlt: Die Symmetrie setzt sich erst bei hohen Stufen durch, oder es gibt einen Boden."
    Nach strengem Wortlaut ausgeloest (DT1 dort verfehlt). Einen Boden zeigt die Rechnung nicht: Die Spanne faellt von
    Stufe zu Stufe (Faktor 0,51 und 0,43).

### 3.1 Agenten-Vorhersagen (PLAN 8, vor jeder Hauptrechnung)

| Nr | Vorhersage | Wahrsch. | Ergebnis |
|---|---|---|---|
| B1 | DT0 nach Plan eingetroffen | 95 % | **eingetroffen** (vorab praktisch entschieden) |
| B2 | Gegenprobe duenn gegen dicht an allen gerechneten Punkten <= 1e-5 | 85 % | **eingetroffen** (<= 8,4e-8) |
| B3 | Zitter-Kontrolle: Spanne von 1/1 oder 2/1 aendert sich um mehr als 1e-4 (absolut) | 60 % | **eingetroffen** (1/1: +4,1, 2/1: +1,8 Prozentpunkte) |
| B4 | Saatmittel s(2/1) < s(1/1) | 75 % | **eingetroffen** (6,17 gegen 12,20 %) |
| B5 | DT1 nach Plan eingetroffen | 55 % | **eingetroffen** (nach Plan; streng nicht) |
| B6 | DT2 eingetroffen | 70 % | **eingetroffen** |
| B7 | DT3 nach Plan eingetroffen | 45 % | **nicht eingetroffen** |

## 4. Tabellen

### 4.1 Netze und Gleichstaende (alle Saaten; lauf-69/auswertung.json) [E]

| Stufe | L | eps | N / E / T | Tetraeder mit Kugel-Gleichstand | Zusatzpunkte auf Umkugeln | Fensterpunkte < 1e-5 am Rand | dn2-Gegenprobe (Kanten, Ecken, Euler) | *1-Klassen (Saaten) |
|---|---|---|---|---|---|---|---|---|
| 1/1 | 2,7528 | +0,23607 | 32 / 224 / 192 | 80 (41,7 %) | 160 | 12 | gleich in 9 von 9 Netzen | 629fa1d0 (0 bis 7) |
| 2/1 | 4,4541 | -0,09017 | 136 / 952 / 816 | 336 (41,2 %) | 672 | 50 | gleich in 9 von 9 | aa531d10 (0, 2, 5), 272cb870 (1, 6), d8e6e9c4 (3), 9a270bc1 (4, 7) |
| 3/2 | 7,2068 | +0,03444 | 576 / 4032 / 3456 | 1424 (41,2 %) | 2848 | 98 | gleich in 5 von 5 (Saat 4 nicht geprueft, L24a abgebrochen) | 42c27cb6 (0, 3), 7a267aa0 (1), 70291885 (2) |

- Die Klassen stimmen mit DANZER-NAEHERUNG-2 (Tabelle 4.3) ueberein. Jede Saat hat eine eigene Zerlegung (verschiedene
  Tetraeder-Fingerabdruecke), auch bei gleicher Eckenmenge (1/1: 6 Eckenmengen fuer 8 Saaten).
- In allen Netzen: Delaunay-Leerkugel nicht verletzt, kein flaches Tetraeder, Tetraedervolumen 0,0784 bis 0,1268,
  Diederwinkel 36,0 bis 110,9 Grad, Kantenlaengen 0,563 bis 1,451, Volumensumme gegen L^3 <= 4,4e-16, Diedersumme je
  Kante 2 pi auf <= 1,8e-15.

### 4.2 TT-Spanne je Saat [E]

**1/1** (8 Saaten und Zitter-Netz):

| Saat | Ecken | Zerlegung | s (52 Werte) | s26 | Spanne der Zweigmittel | groesste Aufspaltung (Richtung) | omega^2/k^2 Mittel |
|---|---|---|---|---|---|---|---|
| 0 | 87ac45cf | 1ab58f0b | 9,01 % | 11,68 % | 0,91 % | 8,58 % ([320]) | 3,145 |
| 1 | 0d3359ff | 913417a3 | 15,35 % | 16,51 % | 1,50 % | 14,56 % ([331]) | 3,162 |
| 2 | 0d3359ff | fee5ed52 | 7,96 % | 19,57 % | 1,41 % | 7,96 % ([100]) | 3,142 |
| 3 | bb88191d | b8055128 | 19,45 % | 19,74 % | 0,55 % | 19,45 % ([100]) | 3,165 |
| 4 | bb88191d | 3a8128f5 | 8,48 % | 10,77 % | 1,54 % | 7,15 % ([111]) | 3,122 |
| 5 | b18bf7c0 | f4b796b4 | 7,66 % | 17,98 % | 2,88 % | 7,66 % ([111]) | 3,172 |
| 6 | 61eafd05 | 6e1dfbad | 16,07 % | 21,69 % | 3,00 % | 15,81 % ([110]) | 3,168 |
| 7 | 214af753 | 69de3a17 | 13,65 % | 19,57 % | 4,18 % | 11,24 % ([100]) | 3,159 |
| 0, Zitter 1 | 87ac45cf | dde9873d | 13,13 % | 13,13 % | 1,17 % | 12,57 % ([310]) | 3,172 |

**2/1** (8 Saaten und Zitter-Netz):

| Saat | Klasse | Zerlegung | s (52 Werte) | s26 | Spanne der Zweigmittel | groesste Aufspaltung (Richtung) | omega^2/k^2 Mittel |
|---|---|---|---|---|---|---|---|
| 0 | aa531d10 | afdf5519 | 2,65 % | 7,74 % | 0,54 % | 2,65 % ([100]) | 3,114 |
| 1 | 272cb870 | cf9dcfbc | 8,88 % | 8,88 % | 0,75 % | 8,48 % ([110]) | 3,137 |
| 2 | aa531d10 | 7a315f82 | 8,89 % | 8,93 % | 0,46 % | 8,89 % ([310]) | 3,140 |
| 3 | d8e6e9c4 | 6809f0fa | 6,50 % | 9,16 % | 0,40 % | 6,50 % ([111]) | 3,136 |
| 4 | 9a270bc1 | 09f65a33 | 6,36 % | 7,97 % | 0,40 % | 6,36 % ([111]) | 3,127 |
| 5 | aa531d10 | 8b7e22f3 | 7,05 % | 12,40 % | 0,97 % | 6,51 % ([110]) | 3,121 |
| 6 | 272cb870 | 105599d4 | 5,88 % | 7,83 % | 1,10 % | 5,23 % ([310]) | 3,133 |
| 7 | 9a270bc1 | a6918ff9 | 3,15 % | 6,02 % | 0,45 % | 3,14 % ([100]) | 3,126 |
| 0, Zitter 1 | aa531d10 | 5b0e6cb5 | 4,48 % | 5,02 % | 0,56 % | 4,48 % ([110]) | 3,128 |

**3/2** (4 vollstaendige Saaten; Saat 4 unvollstaendig; Zitter-Netz nur |k| = 1e-3):

| Saat | Klasse | Ecken | Zerlegung | s (52 Werte) | s nur bei 1e-3 (13 Richtungen, 26 Werte) | Spanne der Zweigmittel | groesste Aufspaltung (Richtung) | omega^2/k^2 Mittel |
|---|---|---|---|---|---|---|---|---|
| 0 | 42c27cb6 | 403fbd27 | dbb29bcc | 1,17 % | 1,17 % | 0,18 % | 1,05 % ([111]) | 3,129 |
| 1 | 7a267aa0 | 0d253f0e | b591ad03 | 3,06 % | 3,06 % | 0,40 % | 3,04 % ([111]) | 3,133 |
| 2 | 70291885 | 82141940 | a76c7974 | 3,29 % | 3,29 % | 0,27 % | 3,12 % ([311]) | 3,138 |
| 3 | 42c27cb6 | 86d0f7e2 | 0a1967d8 | 2,98 % | 2,98 % | 0,17 % | 2,98 % ([100]) | 3,129 |
| 4 | (70291885 laut DANZER-NAEHERUNG-2) | | | unvollstaendig (L24a nach 600 s abgebrochen) | | | | |
| 0, Zitter 1 | 42c27cb6 | 403fbd27 | 73f2400c | nicht gerechnet (nur 1e-3) | 2,59 % | | | |

**Je Stufe (Zitter 0; Plan-Groesse s):**

| Stufe | Saaten | Mittel +- SD | min / max | Verhaeltnis zur Vorstufe | \|eps\|-Verhaeltnis | Glas-Erwartung (N^-0,475) [K] |
|---|---|---|---|---|---|---|
| 1/1 | 8 | 12,20 % +- 4,51 % | 7,66 / 19,45 % | | | |
| 2/1 | 8 | 6,17 % +- 2,31 % | 2,65 / 8,89 % | 0,506 | 0,382 | 0,503 |
| 3/2 | 4 | 2,63 % +- 0,98 % | 1,17 / 3,29 % | 0,426 | 0,382 | 0,504 |
| 3/2 : 1/1 | | | | 0,215 | 0,146 | 0,254 |

- s26 ist bei 1/1 und 2/1 fast immer groesser als s: Die Zerlegungen brechen die Wuerfelsymmetrie, der O_h-Keil der
  13 Plan-Richtungen erfasst das Maximum nicht immer.
- Die Spanne ist fast ganz die Aufspaltung der zwei Polarisationen; die Zweigmittel streuen ueber die Richtungen nur um
  0,4 bis 4,2 % (1/1) bzw. 0,4 bis 1,1 % (2/1).
- omega^2/k^2 liegt in allen Stufen bei 3,11 bis 3,17 (Absolutwert eine Festlegung von J, wie TT-GLAS-1).

### 4.3 Zitter-Kontrolle (gleiche Ecken, anderer Zitter) [E]

| Netz | Zerlegung gleich? | s Zitter 0 | s Zitter 1 | Differenz | groesste relative Aenderung eines Werts (1e-3) |
|---|---|---|---|---|---|
| 1/1 Saat 0 | nein | 9,01 % | 13,13 % | +4,12 Prozentpunkte | 3,3 % |
| 2/1 Saat 0 | nein | 2,65 % | 4,48 % | +1,83 Prozentpunkte | 1,7 % |
| 3/2 Saat 0 (nur 1e-3, 26 Werte) | nein | 1,17 % | 2,59 % | +1,42 Prozentpunkte | 1,3 % |

### 4.4 Stabilitaet (DT2) [E]

| Stufe | Netze (Saaten + Zitter) | gerechnete k-Punkte | davon voll (dicht: alle Eigenwerte) | k mit wachsender Mode | k mit A_red nicht pos. def. | k mit B_red-Negativrichtung | Gitter |
|---|---|---|---|---|---|---|---|
| 1/1 | 9 (8 + 1) | 4 950 | 4 833 | 0 | 0 | 0 | Lk = 8 (511 k) je Netz |
| 2/1 | 9 (8 + 1) | 855 | 530 | 0 | 0 | 0 | Lk = 4 (63 k) je Saat, nicht im Zitter-Netz |
| 3/2 | 6 (Saaten 0 bis 4, Zitter-Netz) | 136 | 8 | 0 | 0 | 0 | Lk = 2 (7 k), nur Saat 0 |

- Die 13 Wuerfelachsen je Netz (1/1, 2/1; |k| = 1e-3) liefen ueber den dichten Weg (tg.punkt) und sind in "voll" nicht
  mitgezaehlt (je 117 Punkte bei 1/1 und 2/1, alle ohne wachsende Mode).
- An allen Spektrum-Punkten aller Netze: genau zwei masselose Werte, beide positiv. Der duenne Weg prueft dabei nur die
  zwei tragenden Werte; die volle Pruefung (alle Eigenwerte, Luecke, A_red, B_red) leisten die dichten Punkte.
- Kleinstes omega^2 / groesstes auf den Gittern: 1/1 >= 0,0049, 2/1 >= 0,0079, 3/2 >= 0,012.
- Werte "unklar" (zwischen 30 und 100 |k|^2) gibt es an Gitterpunkten mit grossem |k| (z. B. 65 je 1/1-Netz); das
  sind keine Instabilitaeten, sondern die Klassengrenzen von tg.punkt bei grossem |k|.
- Dichte Gegenprobe 3/2 Saat 0 an [100] (1e-3): genau 2 masselos, Luecke 2,19, A_red positiv definit, B_red ohne
  negative Richtung, TT-Anteil 1,000.

### 4.5 Kontrollen und Gegenproben [E]

| Netz | s duenn | s dicht | DEFEKT-NETZ-1 / TT-ISO-1 [P] | duenn gegen dicht (26 Punkte, max. rel.) | affine Regge-Steifigkeit / Volumen: Spanne |
|---|---|---|---|---|---|
| V | 6,338810 % | 6,338808 % | 6,338808 % / 6,338810 % | 8,4e-8 | 2,2e-7 |
| A15 | 0,933867 % | 0,933868 % | 0,933868 % | 2,3e-8 | 2,4e-7 |
| C15 | 2,684716 % | 2,684718 % | 2,684718 % | 5,8e-8 | 3,5e-8 |

- Gegenprobe duenn gegen dicht auf den Naeherungen: 1/1 alle 9 Netze an allen 26 Punkten <= 3,6e-8; 2/1 Saat 0 an
  26 Punkten 3,6e-8; 3/2 Saat 0 an [100] (1e-3) 3,9e-9. Schwelle 1e-5: nirgends ueberschritten.
- Duenner Weg: Ritz-Rang an jedem Punkt 2, Residuum der TT-Paare <= 3,4e-10, Linearitaet (2e-3 gegen 1e-3) <= 2,4e-7,
  TT-Anteil an [100], [110], [111] in allen Netzen 1,000.
- Affine Regge-Steifigkeit: auf allen Naeherungsnetzen 0,99999 x Volumen, Spanne ueber 13 Richtungen <= 1,8e-6. Die
  Anisotropie kommt also nicht aus der affinen Steifigkeit (wie TT-ISO-1, TT-GLAS-1).

## 5. Bedeutung fuer Finns Weiche Kristall / Glas / Quasikristall und GW170817 [H]

- **Was gerechnet ist [E]:**
  - Auf den Ammann-Kramer-Naeherungen ist die TT-Spanne mit A1 (J = 1 je Tetraeder) und R1 gross, streut stark von Saat
    zu Saat und faellt mit der Stufe: Mittel 12,2 % / 6,2 % / 2,6 % (1/1, 2/1, 3/2).
  - Sie liegt in jeder Stufe ueber A15 (0,934 %); bei 1/1 im Mittel auch ueber V (6,34 %), bei 2/1 etwa gleich V.
  - Alle Netze sind an allen gerechneten k stabil und haben genau die zwei masselosen TT-Moden.
- **Woher die Spanne kommt [E, H]:**
  - Die Delaunay-Zerlegung der Ammann-Kramer-Ecken ist stark entartet: In allen Stufen haben 41 bis 42 % der Tetraeder
    weitere Ecken auf ihrer Umkugel (1/1: 80 von 192; 2/1: 336 von 816; 3/2: 1424 von 3456). Der Zitter waehlt dort eine
    von mehreren gleich guten Zerlegungen.
  - Die DEC-Gewichte von DANZER-NAEHERUNG-2 haengen davon nicht ab, die A1-Masse und die Regge-Steifigkeit schon (Summen
    ueber Tetraeder) [M].
  - Gerechnet: Gleiche Ecken, anderer Zitter aendern die Spanne bei 1/1 von 9,0 auf 13,1 % (2/1: 2,6 auf 4,5 %;
    3/2: 1,2 auf 2,6 %, nur |k| = 1e-3). Saaten mit gleichen Ecken (1/1: 1 und 2; 3 und 4) liegen bei 15,4 gegen 8,0 %
    und 19,4 gegen 8,5 %. Die Spanne sitzt fast ganz in der Aufspaltung der zwei Polarisationen, wie in den Kristallen.
  - Die zufaellige Zerlegung bricht auch die Wuerfelsymmetrie der Naeherung: ueber 26 Richtungen ist die Spanne bei 1/1
    und 2/1 meist groesser als ueber die 13 Keil-Richtungen (Tabelle 4.2).
  - Lesart [H]: Mit dieser Masse ist jede Naeherung zu gut 40 % ein Glas. Gerechnet faellt die Spanne um 0,51
    (2/1 : 1/1) und 0,43 (3/2 : 2/1). Glas-Mittelung (~N^-0,475 nach TT-GLAS-1) erwartet 0,50 je Stufe [K], die
    Phason-Regel (|eps|) 0,38. Die erste Stufe passt zum Glas, die zweite liegt dazwischen; mit 4 Saaten bei 3/2
    (SD/Mittel 37 %) lassen sich beide nicht trennen.
- **Was das fuer die Symmetrie-Begruendung heisst [M, H]:**
  - Die Karte setzt eine Masse voraus, die die Ikosaedersymmetrie behaelt. A1 mit J = 1 je Tetraeder tut das an den
    Gleichstaenden nicht; geprueft ist hier also "Quasikristall-Ecken plus zufaellige Zerlegung", nicht der ideale
    Quasikristall.
  - DT1 und DT2 sind nach Plan eingetroffen; der Bedeutungssatz der Karte ("Ikosaedrische Ordnung ist ein Grund ...")
    ist formal ausgeloest. Getragen wird der Abfall nach dieser Rechnung aber mindestens ebenso gut von der Mittelung
    ueber mehr Zufallsentscheidungen je Zelle. Dass die Ordnung der Grund ist, zeigt die Rechnung nicht.
  - Ein sauberer Test braucht eine Masse ohne Zerlegungsabhaengigkeit, z. B. Hodge-/DEC-artige Gewichte wie in
    DANZER-NAEHERUNG-2 oder Gewichte je Rhomboeder (Vorschlag, nicht gerechnet). LUND-REGGE-MASSE-1 rechnet eine
    volumengewichtete geschwindigkeitsseitige Masse; ob sie an Gleichstaenden eindeutig ist, habe ich nicht geprueft.
- **Weiche Kristall / Glas / Quasikristall (nur TT, nur diese Masse):**
  - Kristall (DEFEKT-NETZ-1 [P], hier mit beiden Wegen nachgerechnet): feste Spannen V 6,34 %, C15 2,68 %, A15 0,934 %.
  - Glas (TT-GLAS-1 [P]): 11,4 % bei N = 256 (andere Richtungen, |k| = 1e-2), faellt wie N^-0,47.
  - Quasikristall-Naeherungen mit A1 (hier): 12,2 % (1/1, 32 Ecken), 6,2 % (2/1, 136 Ecken), 2,6 % (3/2, 576 Ecken).
  - Grob verglichen [K]: Ein Glas mit gleich vielen Punkten laege nach der Geraden von TT-GLAS-1 bei etwa 29 %, 15 % und
    8 %. Die Naeherungen sind also zwei- bis dreimal isotroper als ein Glas gleicher Punktzahl, aber anisotroper als
    A15 und C15, bei 1/1 auch als V. Der Vergleich ist grob: TT-GLAS-1 hat Dichte 1, andere Richtungen und |k| = 1e-2.
  - Lesart [H]: Der geordnete Anteil (knapp 60 % der Tetraeder ohne Gleichstand) hilft; der zufaellige Anteil
    (gut 40 %) bestimmt die Groessenordnung und die Saatstreuung.
- **GW170817 [H]:** verlangt |c_T/c - 1| unter etwa 1e-15. Die Spanne der Geschwindigkeit ist bei 3/2 noch etwa halb so
  gross wie s, also im Prozentbereich. Bei einem Abfall um 0,3 bis 0,5 je Stufe braeuchte 1e-15 grob 30 bis 50 weitere
  Stufen [K]. Ein Grund fuer exakte Isotropie im Grenzfall bleibt die Ikosaedersymmetrie (PLAN 7), aber nur mit einer
  symmetrischen Masse und bis auf einen moeglichen l = 6-Rest der Steifigkeit [M].

## 6. Selbstanzeigen

1. **Rauchtest ueber 120 s:** R4 (3/2, erster duenner Weg mit ARPACK) lief 138 s. Ich habe ihn um 08:43:49 UTC gestoppt.
   Danach bekamen die Rauchtests einen Selbstabbruch nach 110 s (Option --alarm). R7, R9 und R10 endeten so nach 110 bis
   111 s, ohne vollstaendige Ausgabe.
2. **Rechenweg vor dem Einfrieren mehrfach geaendert:**
   - ARPACK ohne Nachiteration (R3: bei V 5,2e-5 neben dem dichten Weg), dann mit Nachiteration (R5: <= 5,2e-8), dann
     Ritz mit 12 Richtungen (R6: bis 3,2e-3, verworfen), dann Ritz nur mit den tragenden Richtungen (R8: <= 5,5e-8;
     Hauptweg).
   - LU-Ordnung COLAMD statt MMD_AT_PLUS_A nach R9/R10; Argumentlesen (parse_intermixed_args) nach R13.
   - Gesehen habe ich dabei nur relative Abweichungen zwischen den Wegen, Laufzeiten, Raenge und Schluessel, keine
     TT-Werte und keine Spannen.
3. **Werte vor dem Einfrieren erzeugt, nicht gelesen:** R11 (1/1 Saat 0, zwei Richtungen), R12 (Kontrolle V, A15, C15,
   also auch s_V) und R14 (Auswertung darauf). Gelesen habe ich nur rc, einen grep auf Fehler und die Zeilenzahl. Von
   aussen pruefen laesst sich das nicht.
4. **Zwischenauswertungen Z1 bis Z6 und Z3b** (nicht in der Laufliste): dtt.py auswerten (eingefroren) auf den bis dahin
   fertigen Lauf-Dateien, waehrend die Ketten liefen (Ende Z1 09:00:28, Z2 09:12:49, Z3 09:20:51, Z3b 09:21:09,
   Z4 09:27:21, Z5 09:43:52, Z6 09:49:43 UTC). Sie rechnen nichts Neues und gehen in kein Urteil ein; bindend ist L99.
   Sie liefen je zwischen zwei Kettenlaeufen und verzoegerten L05, L22d, L31a, L09, L31b, L32b und L24c um je 2 bis 3 s.
   Mit ihren Zahlen habe ich den Bericht vorgeschrieben; die Endzahlen stammen aus L99.
5. **/tmp/claude-1000:** Ein Warte-Befehl (ssh mit until-Schleife auf L03, dann Z1) ueberschritt 180 s; die
   Werkzeugumgebung hat ihn in den Hintergrund verschoben und seine Bildschirmausgabe nach /tmp/claude-1000/.../tasks/
   geschrieben (Zeiten und rc). Gewaehlt habe ich das nicht, mein Befehl hat es ausgeloest. Danach habe ich jedes Warten
   mit timeout 160 bis 170 s begrenzt.
6. **sed zum Bearbeiten:** Meinen eigenen Code (dtt.py) habe ich vor dem Einfrieren mehrfach mit sed -i geaendert, nicht
   nur gefiltert. Ein leerer Heredoc (cat > /dev/null) blieb ohne Wirkung. Lokal lief kein python, awk oder perl.
7. **jq ueber Lesen hinaus:** Meist nur lesend, mit Objektbau zur Anzeige. Ein Versuch mit min/max scheiterte an der
   Syntax. Ein zweiter Aufruf hat einmal ein Maximum gebildet (groesstes Residuum, 3,4e-10), bevor er abbrach; danach
   habe ich nur Listen gelesen und Extremwerte von Hand abgelesen [K]. Die Kennzahlen stammen aus
   lauf-69/auswertung.json (auf der .69 gerechnet) oder sind als [K] markiert (Prozente, Rundungen, wenige Quotienten,
   Glas-Vergleich). grep, sort -u und wc dienten nur zum Zaehlen von Feldwerten (Ritz-Rang, masselos, wachsend).
8. **TT-GLAS-2** kenne ich nur aus der Karte LUND-REGGE-MASSE-1 ("bis 1e-5 projizierte affine Wellen"); das Ergebnis
   selbst habe ich nicht gelesen. Die Ableitbarkeitspruefung (PLAN 7) stuetzt sich teilweise darauf.
9. **Messung bei Naeherungen ohne Wuerfelsymmetrie:** Die Plan-Spanne s nutzt die 13 Richtungen von TT-ISO-1, die nur
   den O_h-Keil abdecken. Die Zerlegungen brechen die Wuerfelsymmetrie; ueber 26 Richtungen ist die Spanne bei 1/1 und
   2/1 meist groesser (Tabelle 4.2). Die Urteile nutzen nach Plan s; s26 steht daneben. Bei 3/2 ist s26 nicht gerechnet.
10. **Laufliste nach dem Einfrieren geaendert (Nachlauf):**
    - Um 09:28 UTC lief L23a (3/2 Saat 3) wegen hoeherer Last der .69 (Last 5 bis 6) langsamer. Ich habe geschaetzt,
      dass er die 600 s ueberschreitet, und dass Saat 4 (L24a bis L24d auf cpu9) dasselbe Risiko traegt und erst gegen
      10:11 UTC fertig wuerde.
    - Darauf habe ich um 09:28:58 UTC die Kette cpu9 beendet (vor L21c) und Ersatzketten gestartet
      (code/kette-nachlauf-cpu9.sh, -cpu8.sh; sha256 in NACHLAUF-SHA256.txt): L21c und L21d mit denselben Argumenten, dazu
      ein Ersatz fuer L23a in zwei kleineren Teilen (N1, N2).
    - Die Schaetzung war falsch: L23a endete nach 535 s regulaer. Um 09:31:5x UTC habe ich beide Ersatzketten beendet,
      bevor N1 oder N2 starteten, und Saat 4 mit denselben vier Laeufen wie in kette-cpu9.sh auf cpu8, cpu9 und cpu10
      verteilt (code/kette-nachlauf2-cpu{9,8,10}.sh). L21c lief aus der ersten Ersatzkette weiter.
    - Code, Saaten, Richtungen, |k| und Auswertung blieben unveraendert; geaendert hat sich nur, welche Kette welchen Lauf
      startet. Die Kettenprotokolle zu L21c fehlen (das Log lauf-69/L21c.log ist vollstaendig).
    - L24a brach dann tatsaechlich nach 600 s ab (Abschnitt 1); Saat 4 ist unvollstaendig. In der urspruenglichen Kette
      waere L24a zur selben Zeit auf derselben Spur gelaufen. Einen Ersatz habe ich wegen der Zeitbox nicht gestartet.
    - Die Kettenregel "kein neuer Lauf nach 10:15 UTC" galt in den Ersatzketten nicht; ihr letzter Lauf endete 09:58:04.
11. **Kein Gegenlesen** durch einen frischen Leser in der Zeitbox.

## 7. Einfach gesagt

Wir haben Netze gebaut, die sich Stufe fuer Stufe einem Quasikristall mit Ikosaeder-Symmetrie annaehern, und darauf am
Computer Schwerewellen laufen lassen. Je hoeher die Stufe, desto weniger haengt die Wellengeschwindigkeit von der Richtung
ab: im Quadrat von etwa 12 % ueber 6 % auf gut 2,5 %, die Geschwindigkeit selbst etwa halb so stark. Das ist aber immer
noch mehr als beim besten bisher gerechneten Kristall (A15, knapp 1 %) und unvorstellbar weit von der Genauigkeit, mit der
man die Geschwindigkeit echter Schwerewellen kennt. Der Grund liegt im Bau: In diesen Netzen liegen sehr viele Punkte
genau auf gemeinsamen Kugeln, dort muss das Programm zufaellig entscheiden, wie es den Raum in Tetraeder zerlegt, und
diese Zufallswahl macht die Netze zu gut 40 % zu einem Glas. Ob die Ikosaeder-Ordnung selbst die Wellen richtungsgleich
macht, laesst sich erst mit einer Masse pruefen, die von dieser Zufallswahl nicht abhaengt.

## 8. Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-105330, EINGEFROREN-SHA256.txt, NACHLAUF-SHA256.txt,
  ERGEBNIS.md, bild-danzer-tt.png (Kopie aus lauf-69/, auf der .69 erzeugt).
- code/:
  - dtt.py (neu: Bau wie dn2.netz2, duenner Rechenweg, Messung, Auswertung, Bild) und dtt.py.eingefroren-20261005-105330;
    kette-cpu8.sh, kette-cpu9.sh, kette-cpu10.sh mit eingefrorenen Kopien; kette-nachlauf-cpu{9,8}.sh und
    kette-nachlauf2-cpu{9,8,10}.sh (Selbstanzeige 10).
  - Unveraenderte Kopien: danzer_naeherung.py, licht_netz.py, dn2.py (DANZER-NAEHERUNG-2), tg.py, ew.py, tp.py
    (TT-GLAS-1), tti.py, nachtrag_kinetik.py (TT-ISO-1), dn.py (DEFEKT-NETZ-1); sha256 in EINGEFROREN-SHA256.txt.
- lauf-69/: kontrolle.json, n11.json, n11-z1.json, n21-*.json, n32-*.json, auswertung.json, bild-danzer-tt.png, alle
  Logs (L*, Z*, Ketten), L99-eingaben.txt, Zwischenauswertungen z1 bis z6 und z3b (mit Bildern), PRUEFSUMMEN.txt
  (auf der .69 erzeugt, 111 Dateien, lokal mit sha256sum -c geprueft: 111 OK).
- rauch-69/: R1 bis R14 (Logs) und r3, r5, r6, r8 (nur Abweichungen und Zeiten), r11, r12, r14 (Werte vor dem
  Einfrieren nicht gelesen), r14.png.
- Auf der .69: /home/fmh/fmhc-physics-remote/danzer-tt-1/ (code/ schreibgeschuetzt, rauch/, lauf/, EINGEFROREN-SHA256-69.txt,
  NACHLAUF-SHA256-69.txt).

## Zeitbox

- Abschluss der Datei 2026-10-05 12:01:26 CEST (date). Zeitbox 150 min ab 10:25:53 CEST (bis 12:55:53 CEST) eingehalten. Kein Lauf mehr
  aktiv (0 Units fmhc-physics-klein-dtt-* auf der .69, keine Kette). Journal, Peerbus und Commit uebernimmt die Leitung.
