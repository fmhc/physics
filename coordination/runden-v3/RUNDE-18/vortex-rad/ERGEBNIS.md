# ERGEBNIS: VORTEX-RAD, drehende Feldklumpen (Wirbel) auf Rad-Graphen (Runde 18)

- Code-Agent im Auftrag von claude-primary.
- Zeiten (date):
  - Zeitbox ab 14:13:24 CEST.
  - Plan eingefroren 14:34:03 (PLAN.md.eingefroren-20261002-143403).
  - Laeufe 14:34 bis 15:07.
  - Bericht geschrieben ab 15:09:36 CEST.
- Alle Zahlen stammen aus Laeufen auf der .69 (kleintest.sh, Spur cpu6). Lokal lief kein Python.
- Explorativ (v3). Synthetische Rechnung an einem Spielzeugmodell, keine Messdaten. Deutungen sind Hypothesen [H].

## 1. Ergebnis zuerst

1. **Stabile Wirbel gibt es, aber auf dem anderen Ast als vorhergesagt.**
   - Kleiner Ast, m/N > 1/4: fast immer spektral stabil, bei allen drei J (6540 von 6792 Rasterpunkten). Jeder dieser stabilen Punkte hat Moden negativer Krein-Signatur.
   - Kleiner Ast, m/N < 1/4: instabil (57 stabile von 5383 Punkten).
   - Grosser Ast, m = 1: nur fuer kleine N stabil, und zwar N = 5..12 bei J = 0,02 (8 von 21 N), N = 5..9 bei 0,05 und N = 5..8 bei 0,1. **W2 nicht eingetroffen.**
2. **Die Nabe destabilisiert den m = 1-Wirbel des grossen Asts** [ES, nachtraeglich, Selbstanzeige 1].
   - Die Ringsteifigkeit der Phasenmode mit Index k = m faellt wie (2 pi m/N)^2.
   - Die Nabe koppelt genau an diese Mode und senkt deren Energie um etwa NJ/(2(NJ + 1 - omega^2)).
   - Ueberwiegt die Nabe, bekommt K zwei negative Richtungen (n(K) = 2). Der Wirbel wird dann oszillatorisch instabil (ein Quartett).
   - Die Zeitentwicklung bestaetigt die Linearisierung: Wachstumsrate 0,0457 gegen max Re 0,0458.
   - Die Verzweigung traegt den Wirbel hier also nicht, sie stoert ihn [H].
3. **W5 eingetroffen: 72,6 % der instabilen Punkte sind oszillatorisch dominant.**
   - Die Indexzaehlung N_r + 2N_c + 2n_K^- = n(K) - n(D) stimmt an jedem Punkt ausser m/N = 1/4 (0 Abweichungen bei 24 x 10^3 Punkten).
   - Damit passen die Quartette zu Kollisionen von Moden entgegengesetzter Krein-Signatur.
   - Direkt nachverfolgt (stabiler Rasternachbar mit n_K^- >= 1) ist das nur an 167 von 11914 oszillatorischen Punkten.
4. **Finns Primzahlen spielen keine Rolle. W4 eingetroffen, W3 formal nicht.**
   - W3(b) erfuellt: Fehlerquote 7,2 % bei primem N gegen 6,3 % bei zusammengesetztem N.
   - W3(a) verfehlt: Auf dem grossen Ast haengt die Stabilitaet ueber die Nabe zusaetzlich von N J ab (Trefferquote der m/N-Schwelle 89 % und 83 % statt 90 %). Auf dem kleinen Ast trennt die Schwelle m/N = 0,244 zu 97 bis 100 %.
   - Teiler wirken an zwei Stellen, beide als Mechanismus [ES] und mit Zahlen belegt:
     - (i) Bei 4 | N und m = N/4 liegt der Wirbel auf einer exakten Familie stationaerer Loesungen (zusaetzliche Nullmode von K, |Eigenwert| <= 1,6e-12).
     - (ii) Symmetrische Teilring-Wirbel gibt es nur fuer Teiler von N. Fast symmetrische Dreierwirbel existieren aber auch fuer N = 7, 11, 13, 17, 19, 23 und sind ebenso oft stabil: N = 11 hat 25/18/7 stabile Punkte (J = 0,02/0,05/0,1), N = 12 hat 25/18/8.
5. **W1 formal nicht eingetroffen, inhaltlich erfuellt.**
   - An allen 25495 konvergierten Punkten trifft der Wirbel die Formel auf 4,6e-12, die Nabe bleibt bei <= 5,1e-12.
   - 65 von 25560 Punkten konvergierten nicht: alle kleiner Ast, Pfad A, omega^2 zwischen 0,988 und 1. Dort geht die Startamplitude bei J = 0 gegen null; das ist ein Problem des Startpfads, nicht der Formel.
   - **Bedeutung gemaess Karte:** Die Bedingung "W2 und W5" ist nicht erfuellt (W2 nein, W5 ja). Stabile drehende Feldklumpen mit ganzzahligem Drehimpuls gibt es auf dem Rad trotzdem: auf dem kleinen Ast bei grosser Ladung (Phasenschritt > pi/2) [H]. Instabil werden sie meist oszillatorisch, im Einklang mit der Krein-Zaehlung.
   - W3 und W4 zeigen keinen Primzahl-Effekt.

## 2. Vorhersagen W1 bis W5

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| W1 | Schreibtischformel auf 1e-10, Nabe bleibt null (95 %) | **nicht eingetroffen** (formal; Planregel verlangt Konvergenz an allen Punkten), inhaltlich erfuellt | 25495/25560 konvergiert; Formelabweichung <= 4,6e-12, Nabe <= 5,1e-12, Phasenabweichung <= 2,4e-11 rad (bei m/N = 1/4 bis 6,4e-6: Drift entlang der Familie, s. 6.); 65 Ausfaelle (kleiner Ast, Pfad A, omega^2 0,988 bis 1) |
| W2 | Grosser Ast, m = 1, kleines J, fuer viele N stabil (60 %) | **nicht eingetroffen** | J = 0,02: 8 von 21 N mit f >= 0,5 (N = 5..12), Soll >= 14; J = 0,05: 5; J = 0,1: 4. Ab N = 15 (J = 0,02) ist kein Punkt stabil |
| W3 | Stabilitaet haengt von m/N ab, nicht davon, ob N prim ist (60 %) | **nicht eingetroffen** (a verfehlt, b erfuellt) | Kleiner Ast: Schwelle 0,244, "stabil darueber", 100/97/97 %. Grosser Ast: Schwelle 0,22/0,20, "stabil darunter", 89,4/83,1 %; bei J = 0,1 stuft der beste Klassifikator alles instabil ein (93,7 %, die 9 Fehler sind die 9 stabilen Paare). Prim 7,2 % gegen zusammengesetzt 6,3 % Fehler. "Instabil nahe m = N/2": grosser Ast ja (f = 0 fuer m/N >= 0,45), kleiner Ast nein (f = 0,92 bis 0,96) |
| W4 | 11 und 19 bei gleichem m/N nicht stabiler als 10, 12 bzw. 18, 20 (70 %) | **eingetroffen** | Alle 12 Delta <= 0,094 (groesstes: N = 11, J = 0,1, klein; durch m = 5 mit +0,40); N = 19: \|Delta\| <= 0,031 |
| W5 | Instabilitaeten oszillatorisch (Krein-Kollision), nicht reell (55 %) | **eingetroffen** | 11914 von 16421 instabilen Punkten (72,6 %) oszillatorisch dominant; 6166 haben (auch) ein reelles Paar; Indexzaehlung ausserhalb m/N = 1/4 ohne Abweichung |

Je Ast (instabil / oszillatorisch dominant):

| Ast | J = 0,02 | J = 0,05 | J = 0,1 |
|---|---|---|---|
| klein | 1840 / 1002 | 1890 / 1184 | 1881 / 1546 |
| gross | 3168 / 2155 | 3594 / 2732 | 4048 / 3295 |

Nach m/N (alle J):

| Ast | m/N < 1/4 | m/N = 1/4 | m/N > 1/4 |
|---|---|---|---|
| klein | 57 von 5383 stabil; dominant 1846 reell, 3480 osz. | 507 von 540 stabil (Rest: Jordan-Rauschen, s. 6.) | 6540 von 6792 stabil, alle mit n_K^- > 0; 252 osz. |
| gross | 1970 von 5400 stabil (535 mit n_K^- > 0); 3430 osz. | 0 von 540 stabil; 540 osz. | 0 von 6840 stabil; 2628 reell, 4212 osz. |

## 3. Stabilitaetskarte (N, m) je J und Ast, Existenzfenster

**Lesart der Karten:** f = Anteil spektral stabiler Punkte im 30-Punkte-Raster (c von 0,344 bis 0,989).
- Erstes Zeichen: S = alle stabil, T = teils stabil, - = keiner stabil.
- Zweites Zeichen: dominante Instabilitaet unter den instabilen Punkten, r = reell, o = oszillatorisch, g = gleich viele.

```
J=0.02 Ast=klein:
m\N    4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
  1   Tr  To  -r  To  Tr  To  Tr  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r
  2   To  To   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r
  3           To  To   S   S   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r
  4                   To   S   S   S   S   S   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r
  5                           To   S   S   S   S   S   S   S   S   S  Tr  -o  -r  -o  -r
  6                                    S   S   S   S   S   S   S   S   S   S   S   S  Tr
  7                                            S   S   S   S   S   S   S   S   S   S   S
  8                                                    S   S   S   S   S   S   S   S   S
  9                                                            S   S   S   S   S   S   S
 10                                                                    S   S   S   S   S
 11                                                                            S   S   S
 12                                                                                    S
J=0.02 Ast=gross:
m\N    4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
  1   -o  To   S   S  To  To  To  To  To  To  To  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o
  2   -r  -o  -r  -o  -o  To  To  To   S  To  To  To  To  To  To  To  To  To  To  To  To
  3           -r  -o  -r  -o  -r  -o  -o  To  To  To  To  To  To  To  To  To  To  To  To
  4                   -r  -o  -r  -o  -r  -o  -r  -o  -o  -o  To  To  To  To  To  To  To
  5                           -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -o  -o  -o  To  To
  6                                   -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -o  -o  -o
  7                                           -r  -o  -o  -o  -r  -o  -r  -o  -r  -o  -r
  8                                                   -r  -o  -o  -o  -r  -o  -r  -o  -r
  9                                                           -r  -o  -o  -o  -r  -o  -r
 10                                                                   -r  -o  -o  -o  -o
 11                                                                           -r  -o  -o
 12                                                                                   -r
J=0.05 Ast=klein:
m\N    4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
  1   Tr  To  Tr  To  Tr  To  Tr  To  Tr  To  Tr  To  Tr  To  -r  -o  -r  -o  -r  -o  -r
  2   To  To   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r
  3           To  To   S   S   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r  -o  -r
  4                   To  To   S   S   S   S   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r
  5                           To   S   S   S   S   S   S   S   S   S  Tr  -o  -r  -o  -r
  6                                    S   S   S   S   S   S   S   S   S   S   S   S  Tr
  7                                            S   S   S   S   S   S   S   S   S   S   S
  8                                                    S   S   S   S   S   S   S   S   S
  9                                                            S   S   S   S   S   S   S
 10                                                                    S   S   S   S   S
 11                                                                            S   S   S
 12                                                                                    S
J=0.05 Ast=gross:
m\N    4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
  1   -o  To  To  To  To  To  To  To  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o
  2   -r  -o  -r  -o  -o  -o  To  To  To  To  To  To  To  To  To  To  -o  -o  -o  -o  -o
  3           -r  -o  -r  -o  -r  -o  -o  -o  -o  To  To  To  To  To  To  To  To  To  To
  4                   -r  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o  -o  To  To  To  To  To
  5                           -r  -o  -r  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o  -o  -o
  6                                   -r  -o  -o  -o  -r  -o  -r  -o  -r  -o  -o  -o  -o
  7                                           -r  -o  -o  -o  -r  -o  -r  -o  -r  -o  -o
  8                                                   -r  -o  -o  -o  -g  -o  -r  -o  -r
  9                                                           -r  -o  -o  -o  -o  -o  -r
 10                                                                   -r  -o  -o  -o  -o
 11                                                                           -r  -o  -o
 12                                                                                   -r
J=0.1 Ast=klein:
m\N    4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
  1   Tr  To  Tr  To  To  To  To  To  To  To  To  To  To  To  To  To  To  To  To  To  To
  2    S  To   S   S  Tr  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o
  3            S  To   S   S   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o
  4                   To  To   S   S   S   S   S   S  Tr  -o  -r  -o  -r  -o  -r  -o  -r
  5                           To   S   S   S   S   S   S   S   S   S  Tr  -o  -r  -o  -r
  6                                   To   S   S   S   S   S   S   S   S   S   S   S  Tr
  7                                            S   S   S   S   S   S   S   S   S   S   S
  8                                                    S   S   S   S   S   S   S   S   S
  9                                                            S   S   S   S   S   S   S
 10                                                                    S   S   S   S   S
 11                                                                            S   S   S
 12                                                                                    S
J=0.1 Ast=gross:
m\N    4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24
  1   -o  To  To  To  To  To  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o
  2   -r  -o  -r  -o  -o  -o  -o  To  To  To  To  To  -o  -o  -o  -o  -o  -o  -o  -o  -o
  3           -r  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o  To  To  To  To  -o  -o  -o  -o
  4                   -r  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o  -o
  5                           -r  -o  -r  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o  -o  -o
  6                                   -r  -o  -o  -o  -r  -o  -r  -o  -o  -o  -o  -o  -o
  7                                           -r  -o  -o  -o  -r  -o  -r  -o  -r  -o  -o
  8                                                   -r  -o  -o  -o  -o  -o  -r  -o  -r
  9                                                           -r  -o  -o  -o  -o  -o  -o
 10                                                                   -r  -o  -o  -o  -o
 11                                                                           -r  -o  -o
 12                                                                                   -r
```

**Kurz gelesen:**
- Kleiner Ast: Die Grenze liegt auf m = N/4. Darunter instabil (bei J = 0,02 abwechselnd r/o je nach Paritaet von N), darueber stabil.
  - Ausnahmen bei kleinem N (<= 12) nahe m = N/2: teils oszillatorisch instabil.
  - Bei J = 0,1 ist m = 1 teilweise stabil.
- Grosser Ast: Fuer m/N > 1/4 nie stabil. Stabil nur in einem Band bei m/N < 1/4, das mit J schrumpft.
  - Zahl der (N, m) mit f >= 0,5: 41, 26 und 9 bei J = 0,02, 0,05 und 0,1.
  - Fuer m = 1 schliesst die Nabe das Band ab N ~ 13 (J = 0,02).

**Existenzfenster:**
- U, gleichfoermiger Wirbel [ES]:
  - Kleiner Ast fuer c in (1/3; 1), also omega^2 in (1/3 + J g_m; 1 + J g_m) mit g_m = 3 - 2 cos(2 pi m/N).
  - Grosser Ast fuer c > 1/3; gerechnet nur bis c < 1.
  - Numerisch 25495 von 25560 Punkten (Ausfaelle siehe W1).
- L-a, Teilring, K | N, 3 <= K < N, 54 Faelle:
  - Fortsetzung gelingt an 95 bis 133 von 180 Rasterpunkten je Fall.
  - Kleiner Ast: omega^2 von 0,41 (J = 0,02), 0,48 bis 0,50 (0,05) bzw. 0,57 bis 0,63 (0,1) bis 0,90 bis 0,99.
  - Grosser Ast: kuerzer, oberes Ende 0,68 bis 0,99.
  - Stabil nur auf dem kleinen Ast, und zwar genau in den Faellen mit 4m' >= K (Phasenschritt >= pi/2). Das gilt in allen 54 Faellen, z. B. K = 12: m' = 1, 2 instabil, m' = 3, 4, 5 stabil.
  - Grosser Ast: nie stabil.
- L-b, Dreierwirbel an {0, round(N/3), round(2N/3)}:
  - Existiert fuer alle 12 N (7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23), auch fuer Primzahlen.
  - Abweichung des Phasenschritts von 2 pi/3: 1,19 rad (N = 7), 0,15 (N = 11), 0,007 (N = 19), 0,003 (N = 22, 23).
  - Stabil nur auf dem kleinen Ast (N = 11: 50 von 90 Punkten, N = 19: 52).
  - Auf dem grossen Ast existiert er bei N = 11 nur an 10 Punkten, bei N = 19 an 44. Das liegt an der ungleichen Ortswahl bei kleinem N, nicht an der Primzahl: 19 ist auch prim.
- L-c, Bogen (Negativkontrolle): 0 von 96 Versuchen existieren (86 Phasensprung, 10 Newton-Abbruch). Das war vorab erwartet: Die Bedingung erster Ordnung am Bogenende verbietet Phasenschritte ausser 0 und pi.

## 4. Kontrolle gegen V5 (m = 0, reelle Moden, neuer komplexer Code)

| Groesse | V5-ERGEBNIS | hier |
|---|---|---|
| Ring klein, J = 0,05 | [0,475; 0,945 bis 0,960], stabil bis 0,93 bis 0,95 | [0,475; 0,945 bis 0,96], stabil bis 0,93 bis 0,95 |
| Ring gross, J = 0,05 | [0,475; 0,775 bis 0,79], stabil; drei oszillatorische Einzelpunkte bei 0,945 | [0,475; 0,775 bis 0,79], stabil bis 0,775 bis 0,79; drei oszillatorische Punkte (Fensterende bis 0,945) |
| Ring klein, J = 0,1 | [0,59; 0,885 bis 0,925], stabil bis 0,87 bis 0,90 | [0,59 bis 0,595; 0,885 bis 0,925], stabil bis 0,87 bis 0,90 |
| Ring gross, J = 0,1 | [0,59; 0,705 bis 0,74], stabil | [0,59 bis 0,595; 0,705 bis 0,74], stabil |
| Nabenmode, J = 0,05 | N = 8 [0,68; 0,835], N = 11 [0,76; 0,795] | gleich (kleiner Ast); nur N <= 11 |
| N_max der Nabenmode, J = 0,03..0,08 | 20, 15, 11, 9, 7 | 20, 15, 11, 9, 7 (J N_max = 0,54 bis 0,60) |
| Stabilitaetsregel | trifft an 3954 Punkten | trifft an 3623 von 3623 Punkten; Indexzaehlung 0 Abweichungen; Im phi exakt 0 |

- Bestanden nach Planregel: N_max gleich, Fenstergrenzen innerhalb eines Rasterschritts, Regel an 100 %.
- Hier nur J = 0,05 und 0,1 (V5 zusaetzlich 0,2), daher 3623 statt 3954 Punkte.

## 5. Abbildungen und Zeitentwicklung

- `aus/stabilitaetskarte.png`: f je (N, m), sechs Tafeln (Ast x J), Buchstabe = dominante Instabilitaet, rote Linie m = N/4, * = prim.
- `aus/stabil_mN.png`: f gegen m/N; N = 11 rot, N = 19 blau, andere Primzahlen orange.
- `aus/wirbelprofil.png`: Betrag und Phase als Zeiger auf dem Rad und als Balken/Punkte:
  - U: N = 12, m = 1, J = 0,1, grosser Ast, omega^2 = 0,738, oszillatorisch instabil.
  - L-a: N = 12, K = 4, m' = 1, kleiner Ast, stabil.
  - L-b: N = 11, kleiner Ast, stabil.
- `aus/zeit.png`: Abstand zur mitrotierenden Loesung, gestrichelt exp(max Re t).

Zeitentwicklung (Stoerung ~2e-6, T = 400, DOP853 rtol 1e-10; Energie- und Ladungsfehler <= 2,4e-9):

| Fall | max Re (Art) | Rate aus Fit | Verlauf |
|---|---|---|---|
| N = 12, m = 1, gross, c = 0,6, J = 0,05 | 0,0458 (osz., Im 0,019) | 0,0457 | zerfaellt (Abstand bis 2,2) |
| N = 12, m = 5, gross, c = 0,6, J = 0,05 | 0,277 (gemischt, dom. reell) | 0,253 | zerfaellt |
| N = 12, m = 1, klein, c = 0,6, J = 0,05 | 0,179 (gemischt, dom. reell) | 0,163 | zerfaellt |
| N = 12, m = 5, klein, c = 0,6, J = 0,05 | stabil | - | bleibt <= 1,1e-5 (Start 2,2e-6) |
| N = 11, m = 5, gross, c = 0,989, J = 0,1 (groesstes osz. max Re bei N = 11, 12) | 0,424 (osz.) | 0,408 | zerfaellt |

## 6. Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Selbstanzeigen:**

1. Die Schreibtischrechnung im Plan (Abschnitt 6) liess die Nabe aus.
   - Ihre Erwartung "grosser Ast stabil fuer m/N < 1/4" trifft nur fuer kleines N J zu.
   - Der Rauchtest zeigte n(K) = 2 beim m = 1-Wirbel (vor den Hauptlaeufen). Die Nabenkorrektur in Punkt 1.2 ist eine nachtraegliche Abschaetzung mit einer Phasen-Testfunktion, kein eigener Lauf.
   - Sie trifft die Lage der Grenze grob, z. B. N = 13, J = 0,02, Fenstermitte negativ, f = 0,40.
2. Die exakte Familie bei m/N = 1/4 war nicht vorhergesehen; der Plan nannte nur "entartet in erster Ordnung".
   - Herleitung [ES]: Bei Phasenschritt pi/2 verschwindet an jedem Ringknoten die Nachbarsumme fuer jede Wahl theta_ungerade - theta_gerade. Gerade und ungerade Knoten tragen je alternierende Phasen, die Nabe bleibt null. Zur Familie gehoert eine reelle Loesung.
   - Folgen:
     - 578 Abweichungen der Indexzaehlung, alle bei m/N = 1/4.
     - Die Einstufung stabil/reell wechselt an 101 Punkten (Schwelle 1e-6) bzw. 232 Punkten (1e-10), ebenfalls alle bei m/N = 1/4. Ausserhalb 0 Wechsel.
     - Die 33 "reell"-Einstufungen des kleinen Asts dort (max Re 1e-8 bis 5,2e-7) sind Rauschen des Jordan-Blocks. Auf dem grossen Ast ist max Re dort >= 0,0195, also echt instabil.
     - Newton driftet dort entlang der Familie: Phasenabweichung bis 6,4e-6 rad, ausserhalb <= 2,4e-11.
3. Die W1-Regel "alle Punkte konvergieren" liess W1 an einem Startproblem von Pfad A scheitern (65 Punkte, omega^2 >= 0,988). Nicht nachgerechnet; nach dem Ergebnis aendere ich die Regel nicht.
4. Neustart mit Stoerung 1e-3 (nur berichtet, wie geplant):
   - 552 von 25495 ohne Konvergenz.
   - 326 auf einer anderen Loesung (Abstand > 1e-8, bis 1,23), davon 101 bei m/N = 1/4.
   - Welche Loesungen das sind, ist nicht untersucht.
5. Die Krein-Kollision ist nur mittelbar ueber die Indexzaehlung belegt. Direkt nachverfolgt ist sie an 167 von 11914 oszillatorischen Punkten. Die Kollisionsstellen selbst sind nicht aufgeloest.
6. W3(a) faellt knapp (89,4 % bei J = 0,02, gross). Die falsch eingestuften Paare sind m = 1, 2 bei grossem N, also der Nabeneffekt, nicht Primzahlen.
7. L-a mit K = 4 bei N = 16, 20, 24: 24, 48 und 64 Abweichungen der Indexzaehlung. Mutmasslich (nicht geprueft) dieselbe Phasenschritt-pi/2-Entartung, numerisch durch Steifigkeit ~ J^d (d = 4..6).
   - L-a wurde im symmetrischen Teilraum geloest, die Stabilitaet aber im vollen System gerechnet.
   - 1 Punkt ausserhalb m/N = 1/4 mit unklarer Krein-Signatur.
8. Lauffolge anders als im Plan aufgelistet (Scans zuerst). Kein Aufruf lief in die 600-s-Grenze. Groesste Laufzeit: nmax mit 7 min 54 s.

**Grenzen:**

- Raster mit 30 Punkten je Fall (Schritt in c 0,022). Fenstergrenzen nur auf diese Genauigkeit.
- Grosser Ast nur c < 1 (S < 4/3).
- Stabil heisst spektral stabil (linear). Zeitentwicklung nur fuer 5 Faelle bis T = 400, keine nichtlineare Stabilitaetsaussage.
- Gleiches J auf allen Kanten. Literatur nicht geprueft (arXiv:2610.00774 nur aus der Karte).
- L-b: eine Ortswahl je N. L-c: nur m = 1, K = 3 und 4, zwei omega^2.

**Laufzeiten (.69, systemd):**

| Aufruf | Start (CEST) | Laufzeit |
|---|---|---|
| vortex_rad.py schnell | 14:34:15 | 2,9 s |
| vortex_rad.py scan 0,02 | 14:36:03 | 4 min 0 s |
| vortex_rad.py scan 0,05 | 14:40:04 | 3 min 51 s |
| vortex_rad.py scan 0,1 | 14:43:55 | 3 min 34 s |
| vortex_rad.py lokal | 14:47:29 | 7 min 37 s |
| vortex_rad.py kontrolle | 14:55:06 | 3 min 58 s |
| vortex_rad.py nmax | 14:59:04 | 7 min 54 s |
| vortex_rad.py zeit | 15:06:58 | 16 s |
| auswertung.py | 15:07:14 | 9 s |

- Laufordner auf der .69: /home/fmh/fmhc-physics-remote/runde18-vortex-rad/.
- Kette: hilfs/kette.sh, Log hilfs/kette.log.
- Code auf der .69 und lokal bitgleich (sha256 geprueft).

**sha256:**

```
466f1c61a40739b79e3dd567573fda2e0475e28e89a87349f9293365dbb874f7  code/vortex_rad.py
eee34d679be4e77a592a0a8fcbb3810caf8578c7333dd2e7aa17a4d575380438  code/auswertung.py
3b815c78f09406dadfbecc29e6238e33629b3b54d4cb03a10a826f2102e98ff4  PLAN.md.eingefroren-20261002-143403
83320e5a339f976d281c664a999773da5cec5481133559b181db0cf166d249b5  aus/scan_J0.02.json
871f3858d9bb5179d2bfcf8c1ddd76754dd5344be7e08ad8257ad0aa1ba7ec7f  aus/scan_J0.05.json
5bf4bd0df62e12d20fdff35a51fc89f83795752fd0f7b0337a451974465d6f23  aus/scan_J0.1.json
0d73ecec893fd9368600279568a26531c5468dcbba3888763fa2037ba6de83c0  aus/lokal.json
acd77325f650237bcbc09cc172e2dd20f9530e9010d765c5c4d5c7df4f731b78  aus/kontrolle.json
52389826aa4830c2378ba4c17790735f7ef7b61adbcf842cb357976294051319  aus/nmax.json
c6f72423d1627d45dda1c7b949411f682b7c55501443fcd72490a9b6f1033e55  aus/zeit.json
fbea4f9eaa1de835392947632bc03c66681b50afbaef6d83a71d9e5a7c4bbb77  aus/schnell.json
f98739363267eef55c9767825b71b584b9b41e5561139927641c0c4d7e847559  aus/auswertung.json
4303d44344a82bac2b0ed122c071b426f5f6a276745b962dac8c6445cb4d8b30  aus/auswertung.txt
1cee5b5bb9dc3fe0231d74528d0c15235264707f086a396a66fa5f119c9f8a4c  aus/stabilitaetskarte.png
8ee2708dd84bca1a24bf2823ecdc9d328a681aa869d4a9a357ba79c14417193c  aus/stabil_mN.png
d99055a69aab2e9219dc07b91b312f4e6e716ef8f1653ed6db654f0cc35354dc  aus/wirbelprofil.png
62dd6071a98b2e0307719abbf5071af29bc1544732edbd214af9e060d6d6bbc0  aus/zeit.png
e164654304b84051bc804c1150c2c4431c4480c4df60ecff485bab13c7a35eec  hilfs/kette.sh
```

## 7. Einfach gesagt

Wir haben auf einem Rad aus N Knoten mit Nabe Feldklumpen gerechnet, die sich drehen und dabei eine ganze Zahl von Umdrehungen um die Nabe tragen (Ladung m). Solche drehenden Klumpen koennen stabil sein: auf dem "leichten" Ast, wenn sich die Phase von Knoten zu Knoten um mehr als eine Vierteldrehung weiterdreht. Der einfachste Wirbel mit m = 1 auf dem "schweren" Ast haelt dagegen nur bei kleinen Raedern. Bei grossen Raedern zieht die Nabe, die mit allen Knoten verbunden ist, Energie aus seiner Drehung, und er faellt schaukelnd auseinander. Die Primzahlen 11 und 19 verhalten sich wie ihre Nachbarn. Teiler spielen nur bei Sonderfaellen eine Rolle, etwa bei Raedern mit durch 4 teilbarer Knotenzahl, wo der Wirbel zu einer ganzen Familie gleichwertiger Loesungen gehoert.
