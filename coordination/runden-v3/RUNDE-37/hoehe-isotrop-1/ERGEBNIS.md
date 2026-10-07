# HOEHE-ISOTROP-1: Ergebnis (Runde 49, Code-Agent fuer die Leitung claude-primary)

## Kopf

- **Zeiten (date; CEST, die .69 laeuft in UTC = CEST - 2 h):**
  - Start 2026-10-05 13:19:50. Gelesen bis 13:29:28, Plantext ab 13:29:31, Code ab 13:36:14.
  - Plan-Nachtraege vor jedem Lauf: K1-Schwelle 1e-11, SLSQP maxiter 60, Zeitwaechter, Pfadtests (alle vor R1).
  - Rauchtests R1 bis R8: 11:40:21 bis 11:42:33 UTC (13:40:21 bis 13:42:33 CEST). Rauch-Abschnitt im Plan ab 13:42:39.
  - **Eingefroren 13:43:10 CEST** (PLAN.md.eingefroren-20261005-134310, code/hi.py.eingefroren-20261005-134310,
    EINGEFROREN-SHA256.txt; auf der .69 gleiche Pruefsummen).
  - Hauptlaeufe H1 bis H7: 11:43:17 bis 11:59:49 UTC; Auswertung H8: 11:59:59 bis 12:00:00 UTC.
  - lauf-69/PRUEFSUMMEN-69.txt (24 Dateien, auf der .69 erzeugt): lokal sha256sum -c, alle OK (14:00:19 CEST).
  - Ergebnistext ab 14:01:49 CEST. Ende: letzte Zeile dieser Datei.
- **Laeufe:** 16 kleintest-Einheiten auf der .69 (p4000a, p4000b), alle rc = 0. 8 Rauchtests (laengster 48 s),
  8 Hauptlaeufe (laengster H5 mit 320 s). Kein Lauf ueber 600 s, kein Rauchtest ueber 120 s. Kein Nachtrag-Lauf.
- **Code nach dem Einfrieren unveraendert.** Unveraenderte Kopien aus REGULAER-V-1: rv.py, ew.py, tp.py,
  danzer_naeherung.py, licht_netz.py (Pruefsummen wie dort).
- **Dateien:** PLAN.md (+ .eingefroren), code/hi.py (+ .eingefroren), kette-p4000a.sh, kette-p4000b.sh,
  rauch-kette-a.sh, rauch-kette-b.sh, lauf-69/ (mitte, proben, f43-0, f43-1, null, gitter, l2, auswertung, Logs H1 bis
  H8, PRUEFSUMMEN-69.txt), rauch-69/ (R1 bis R8). Auf der .69: /home/fmh/fmhc-physics-remote/hoehe-isotrop-1/.
- Synthetische Rechnung an einem gedachten, unendlich periodischen Netz. **Keine Messdaten, keine
  Messdatenbestaetigung.**
- Kennzeichen: [M] Schreibtisch, [E] gerechnet, [K] Kopfrechnung aus gerechneten Werten, [P] Projekt,
  [L] Gedaechtnis-Literatur, [H] Hypothese.
- Einheiten: a = kubische Kante; a2 und beta in a^2 (Umrechnung auf die Finn-Tetraederkante l_P: mal 8); Gewichte und
  Margen in (a/8)^2. "Licht" = Maxwell auf V (DEC) mit gewichteten *1, *2 aus dem Potenzdiagramm (Plan 1.1 bis 1.4).

## Ergebnis zuerst

1. **Die Hoehe hebt das Wuerfelmuster des Lichts am skalaren Nullpunkt nicht auf (HI1 verfehlt).** Am beta-Nullpunkt
   w0* (Skalar isotrop, beta = -4e-12 a^2) hat das Licht noch beta_L = 8,5e-5 a^2, also 7,4 % des Werts in der
   Kammermitte (1,14e-3). Gefordert war < 0,1 %. An allen 7 gefundenen skalaren Nullpunkten liegt das Verhaeltnis
   zwischen 5 % und 34 %.
2. **Die Hoehe verkleinert das Muster aber stark.** In 1131 Kammerpunkten wird beta_L nie negativ; das Minimum ist
   0,5 % der Mitte (F-43m-Schnitt). Am Nullpunkt w0* schrumpft die Richtungsspanne von a2 von ~37 % auf ~3 % des
   Mittels [K]. Dafuer bleibt dort eine Doppelbrechung von 8e-5 a^2, so gross wie der verbliebene l = 4-Anteil: Licht
   auf V spaltet die beiden Polarisationen schon in Ordnung (k a)^2.
3. **Das gemittelte a2 des Lichts bleibt ueberall negativ, schwankt aber mehr als den Faktor 2 (HI2 verfehlt).** Alle
   1131 Stichproben sind unterlichtschnell (a2 < 0). Bezogen auf die Mitte (-2,01e-3 a^2) reicht a2 vom 0,59- bis zum
   3,28-Fachen. HI2 scheitert am Faktor, nicht an einem Nulldurchgang.
4. **Die LHAASO-Schranke aendert sich zwischen Mitte und Nullpunkt kaum (HI3 eingetroffen).** Mittel-Schranke
   l < 1,58e-27 m (Mitte) gegen 1,65e-27 m (w0*), Faktor 1,05. Achsen/Raumdiagonalen: Faktoren 1,09 bis 1,11. Der
   Operator ist DEC-Maxwell auf V; die Zahl 7,0e-28 m der Karte gehoert zu einem anderen Operator (M-D, Plan 1.1).
5. **Kontrollen (HI0 eingetroffen):** beta aus REGULAER-V-1 an drei Stichpunkten auf <= 2,5e-7 relativ, alle 158 alten
   Stichproben exakt. Das Licht hat fuer jedes w exakt c = 1 (Schreibtisch [M], gerechnet |c - 1| <= 2e-10). Die neue
   Identitaet sum *2 A^2 n n^T = Vol I gilt auf <= 3e-15.

## 1. Urteile HI0 bis HI3

Mechanisch durch code/hi.py (Funktion urteilen), Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Karte, woertlich) | Wahrsch. | Urteil nach Plan | Urteil nach Wortlaut | Kennzahl |
|---|---|---|---|---|---|
| HI0 | Kontrolle [P, M]: Der Code gibt beta aus REGULAER-V-1 an drei Stichpunkten auf 1e-6 wieder, und im F-43m-Schnitt gibt es einen Punkt mit beta = 0 innerhalb der Kammer | 90 % | **eingetroffen** | **eingetroffen** | Kammermitte und w = 0 bitgleich; F-43m-Punkt (N2 ort_min) 2,5e-7 relativ (7e-11 a^2). w0* gefunden: beta = -4,0e-12 a^2, Marge 0,4927 (a/8)^2, alle Sterne > 0 |
| HI1 | [H] Am Punkt beta = 0 ist auch der l = 4-Anteil von a2 beim Licht (Maxwell, gewichtete *1 und *2) kleiner als 1e-3 seines Werts bei w = Kammermitte | 40 % | **nicht eingetroffen** | **nicht eingetroffen** | R = abs(beta_L(w0\*)) / abs(beta_L(Mitte)) = 8,463e-5 / 1,1386e-3 = 0,0743. Wortlaut (rms_l4): lo 0,099, hi 0,048. Alle 7 Nullpunkte: R = 0,052 bis 0,340 |
| HI2 | [H] Das richtungsgemittelte a2 des Lichts bleibt in der ganzen Kammer negativ (unterlichtschnell) und aendert sich um hoechstens den Faktor 2 | 55 % | **nicht eingetroffen** | **nicht eingetroffen** | 1131 gueltige L = 1-Stichproben, alle a2 < 0; Faktor zur Mitte bis 3,28 (Plan). Wortlaut: 1136 Stichproben mit L = 2, alle drei Zweige negativ, Spanne max/min = 5,56 |
| HI3 | [H] Die bedingte LHAASO-Schranke an l aendert sich zwischen Kammermitte und beta-Nullpunkt um weniger als den Faktor 3 | 55 % | **eingetroffen** | **eingetroffen** | Mittel-Schranke 1,578e-27 m -> 1,650e-27 m, Faktor 1,046. Wortlaut (konservativ, streng; lo, hi): Faktoren 1,087 / 1,097 / 1,087 / 1,105 |

- **Bedeutung nach Karte, angewandt:**
  - HI1 trifft nicht ein. Die vierte Richtung (Hoehe) hebt das kubische Kurzwellen-Muster des Lichts am skalaren
    Nullpunkt nicht auf. Sie drueckt es dort auf 7 %.
  - HI3 trifft ein, HI2 nicht. Die Datenschranke haengt am gemittelten a2. Zwischen Mitte und Nullpunkt aendert sie sich
    nur um 5 %. Ueber die ganze Kammer schwankt das gemittelte a2 bis zum Faktor 3,3; die Schranke aendert sich dann um
    bis zu 1,8 [K].
  - Der Kartenzweig "HI2 verfehlt (a2 laesst sich auf null bringen)" trifft **nicht** zu. a2 bleibt in jeder Stichprobe
    negativ; der kleinste Betrag ist 59 % der Mitte. Die n = 2-Schranke behaelt ihren Griff.

## 2. Tabellen

**2.1 beta-Nullpunkt im F-43m-Schnitt [E]** (z = (u1, u2, v) = (w_C1 - w_P, w_C2 - w_P, w_H - w_P) in (a/8)^2; Suche nach
Plan Abschnitt 5: 128 Strahlen, brentq, dann SLSQP auf groesste Marge)

| Punkt | Quelle | z | Marge (a/8)^2 | beta Skalar | beta_L Licht | R = beta_L/beta_L(Mitte) | a2_L Kugelmittel |
|---|---|---|---|---|---|---|---|
| Kammermitte (Fd-3m) | Plan 4 | (-3,286; -3,286; -4,571) | 1,7143 | 1,2440e-3 | 1,1386e-3 | 1 | -2,0121e-3 |
| **w0\*** | SLSQP ab Strahl 59 | **(-3,490; 1,532; -3,486)** | **0,4927** | -4,0e-12 | **8,463e-5** | **0,0743** | -1,8736e-3 |
| Spiegelpunkt | SLSQP ab Strahl 81 | (1,533; -3,488; -3,485) | 0,4927 | 5,3e-11 | 8,453e-5 | 0,0742 | -1,8733e-3 |
| Strahl 46 | brentq | (-2,925; 1,727; -3,143) | 0,456 | -5,7e-12 | 5,98e-5 | 0,052 | -1,795e-3 |
| Strahl 59 | brentq | (-3,933; 1,157; -4,255) | 0,133 | -2,5e-12 | 1,252e-4 | 0,110 | -1,991e-3 |
| Strahl 81 | brentq | (1,009; -7,872; -6,358) | 0,074 | 3,6e-11 | 3,877e-4 | 0,340 | -2,573e-3 |
| Strahl 44 | brentq | (2,116; -3,200; -2,843) | 0,043 | -4,0e-13 | 7,38e-5 | 0,065 | -1,887e-3 |

- w0* als Gewichtsvektor (Summe 0, (a/8)^2): w_P = 1,590, w_C1 = -1,900, w_C2 = 3,123, w_H = -1,896. Die eine Lochmitte
  ist schwerer, die andere so leicht wie die Sechseckmitten. Marge 0,49 (a/8)^2 = 0,062 l_P^2 [K], 29 % der groessten
  Marge der Kammer (12/7) [K].
- Alle drei SLSQP-Laeufe endeten an der Iterationsgrenze 60 (status 9). Sie landeten auf demselben Punkt bzw. seinem
  Spiegelbild (Margen gleich bis 1,3e-7, Lage bis ~1e-3). Fuer HI1 aendert das nichts (R 0,0743 gegen 0,0742).
- Stufe 1 fand 4 Strahl-Nullpunkte (Stufe 1b lief deshalb nicht); 1864 Skalar-Auswertungen.

**2.2 a2-Anteile je Kammerpunkt [E]** (Licht = Zweig maxwell_mittel; Skalar zum Vergleich; Doppelbrechung = max ueber 40
Richtungen von abs(a2_hi - a2_lo))

| Ort | a2_L Kugelmittel | beta_L | beta Skalar | a2 Skalar | Doppelbrechung | Bemerkung |
|---|---|---|---|---|---|---|
| Kammermitte | -2,012e-3 | 1,139e-3 | 1,244e-3 | -4,080e-3 | 1,04e-4 | l = 2, nichtkub. l = 4, l = 6 <= 7e-11 |
| w0* | -1,874e-3 | 8,46e-5 | -4e-12 | -4,034e-3 | 8,3e-5 | rms_l4 lo 2,0e-5, hi 9,1e-6 |
| S1 Ecke (7, 4), s = 0,99 | -4,442e-3 | 2,742e-3 | 3,002e-3 | -5,917e-3 | 2,6e-4 | |
| S1 Ecke (-5, -8), s = 0,99 | -3,216e-3 | 2,2626e-3 | 2,2633e-3 | -4,554e-3 | 7e-7 | Licht und Skalar fast gleich |
| S1 Ecke (-11, -8), s = 0,99 | -6,591e-3 | 5,179e-3 | 5,186e-3 | -4,701e-3 | 7e-6 | groesstes beta |
| S1 Kantenmitte (1, -2), s = 0,9 | -1,316e-3 | 9,88e-5 | 1,53e-4 | -3,927e-3 | 5,3e-5 | kleinstes beta_L in S1 |
| S3 Extrem w_C (Td), s = 0,99 | -2,274e-3 | 6,65e-4 | 2,48e-5 | | 6,3e-4 | Skalar fast isotrop, Licht nicht |
| S3 Extrem w_P (max), s = 0,99 | -3,885e-3 | 3,259e-3 | 3,900e-3 | | 1,9e-3 | l = 2 bis 2,5e-4 (kubisch gebrochen) |
| G kleinstes abs(a2_L): (x, y) = (-0,03; -1,53) | -1,188e-3 | | | | | 0,59 der Mitte, Marge 0,84 |
| G groesstes abs(a2_L): (-10,68; -7,97) | -6,609e-3 | | | | | 3,28 der Mitte, Marge 0,017 |
| F43 kleinstes beta_L: Strahl 46, s = 0,9 | -2,100e-3 | 5,7e-6 | -9,2e-5 | | | 0,5 % der Mitte, Marge 0,17 |
| L = 2, Mitte gekachelt | -2,012e-3 | 1,139e-3 | 1,244e-3 | | 1,04e-4 | K7: gleich L = 1 bis 2e-7 [K] |
| L = 2, 4 Zufallsrichtungen, s = 0,9 | -2,012e-3 bis -2,084e-3 | 1,02e-3 bis 1,22e-3 | | | bis 2,0e-4 | beschreibend (Wortlaut HI2) |

- Ueber alle 1131 gueltigen L = 1-Stichproben: beta_L von 5,7e-6 bis 5,18e-3, **nie negativ**. F-43m-Schnitt (640
  Strahlpunkte): Skalar 6-mal negativ, Licht 0-mal; kein Strahl mit Vorzeichenwechsel von beta_L. Fd-3m-Gitter (325):
  beta_L >= 9,7e-5, Skalar >= 1,2e-4.
- Licht gegen Skalar: Im Fd-3m-Schnitt liegt beta_L nahe am Skalar (Mitte 8 % darunter, Ecke (-5, -8) gleich bis 3e-4
  relativ) [K]. Im F-43m-Schnitt trennen sie sich: Wo der Skalar null wird, bleibt das Licht positiv.

**2.3 Bedingte LHAASO-Schranke (woertlich wie LICHT-FINN-NETZ-1: 26 Richtungen, Fenster W0, l = hbar c /
(E_QG,2 sqrt(2 abs(a2))), E_QG,2 = 6,9e11 GeV, l = Finn-Tetraederkante) [E]**

| Schranke (Zweig) | abs(a2) Mitte (l_P^2) | l Mitte | abs(a2) w0* | l w0* | Faktor |
|---|---|---|---|---|---|
| konservativ, Achsen (lo = hi) | 0,01245 | 1,81e-27 m (1,1e8 l_Planck) | 0,01472 | 1,67e-27 m | 1,087 |
| **Mittel (maxwell_mittel), Plan** | 0,01642 | **1,58e-27 m** | 0,01501 | **1,65e-27 m** | **1,046** |
| Mittel lo / hi | 0,01662 / 0,01623 | 1,57e-27 / 1,59e-27 m | 0,01517 / 0,01486 | 1,64e-27 / 1,66e-27 m | |
| streng (lo / hi) | 0,01853 | 1,49e-27 m | 0,01540 / 0,01517 | 1,63e-27 / 1,64e-27 m | 1,097 / 1,105 |
| Kugelmittel (beschreibend) | 0,01610 | 1,59e-27 m | 0,01499 | 1,65e-27 m | |

- Vergleich LICHT-FINN-NETZ-1 (M-D, Coulomb-Phase auf den Diamant-Kanten): 7,0e-28 / 6,3e-28 / 6,1e-28 m. DEC-Maxwell
  auf V ist in der Kammermitte rund 6-mal weniger dispersiv (Kugelmittel -0,016 statt -0,10 l_P^2), die Schranke darum
  rund 2,5-mal schwaecher [K]. Beides sind bedingte Schranken an verschiedene gedachte Operatoren [H].
- Ueber die ganze Stichprobe (a2 zwischen 0,59- und 3,28-fach der Mitte) reicht die Kugelmittel-Schranke von ~8,8e-28
  bis ~2,1e-27 m [K].
- Fensterprobe (W0, Wk, Wg) in der Mitte: Richtungsmittel von a2 gleich bis ~3e-5 relativ, Extremwerte bis ~1e-4 [K];
  Tempo-Spanne <= 7e-10.

**2.4 Kontrollen [E]**

| Kontrolle | Ergebnis |
|---|---|
| K1 Bau | 10/68/116/58, Euler 0; d1 d0 = 4,0e-16; Nullen 12 bei k = 0 (soll 12), 10 bei kleinem k (soll 10) |
| K2 Identitaeten I1, I2, I3 | <= 7,8e-16 an Mitte und 3 Zufallsgewichten; I3 <= 2,7e-15 ueber alle Stichproben; Vorzeichen *2 = g |
| K3 Skalar aus meinem d0 gegen rv | 9,5e-15 relativ |
| K4 c = 1 | Mitte und w0*: abs(c - 1) <= 1e-12; ueber alle Stichproben abs(c - 1) <= 1,9e-10, Spanne <= 1,6e-9 |
| K5 Probe-Fenster | beta_L relativ 4,9e-7 (Mitte), 1,2e-5 (w0*, absolut 1,0e-9) [K] |
| K6 Symmetrie (maxwell_mittel) | l = 2, nichtkub. l = 4, l = 6: <= 6,6e-11 (Mitte), <= 1,7e-10 (w0*) |
| K7 L = 2 gekachelt | beta_L 2,0e-7, a2 2e-8 relativ zu L = 1 [K] |
| Gueltigkeit | 1131 von 1131 (L = 1) und 5 von 5 (L = 2) gueltig: Marge > 0, alle Sterne > 0, null_rel <= 1e-8, Luecke >= 1,5, Fit <= 1e-6 |
| Skalar gegen REGULAER-V-1 | 158 von 158 Stichproben bitgleich |

## 3. Bedeutung [H]

- **Lichtgeschwindigkeit im Netz:**
  - Auf Finns Netz V mit Hebehoehe laeuft langwelliges Licht fuer jede zulaessige Hoehe exakt mit c = 1, in jeder
    Richtung. Das folgt am Schreibtisch aus zwei Identitaeten (Plan 1.3, I2 und I3) und ist gerechnet. Die Hoehe ist
    also keine Stellschraube fuer c.
  - Sie stellt nur die Kurzwellen-Korrektur a2 (k a)^2 ein. Das Licht bleibt dabei in allen 1136 Stichproben
    unterlichtschnell. Die n = 2-Datenschranke bleibt deshalb bestehen; sie verschiebt sich innerhalb der Kammer um
    hoechstens ~1,8 [K].
- **Finns vierte Richtung:**
  - Die Hoehe kann das kubische Muster des Lichts stark verkleinern (am skalaren Nullpunkt auf 7 %, in der Stichprobe
    bis 0,5 %). Ganz aufgehoben hat sie es in keiner Stichprobe.
  - Skalar und Licht werden nicht am selben Punkt isotrop. Eine einzige Hoehe macht also nicht alle Felder zugleich
    richtungsfrei. Ob es fuer das Licht allein eine Nullflaeche gibt, ist offen (Minimum 0,5 %, kein Vorzeichenwechsel
    gefunden).
  - **Neu und nicht vorhergesagt:** Licht auf V hat Doppelbrechung in Ordnung (k a)^2 (Mitte 1e-4 a^2, bis 1,9e-3
    a^2). M-D (LICHT-FINN-NETZ-1) hatte keine. Die Hoehe macht sie nicht weg; am Nullpunkt ist sie so gross wie der
    verbliebene l = 4-Anteil. KUBISCH-ANKER-L nennt Doppelbrechungsschranken, die 7 bis 8 Groessenordnungen schaerfer
    sind als die Laufzeitschranken [P]. Traegt V das Licht als DEC-Maxwell, waere die Doppelbrechung vermutlich der
    schaerfere Test [H, nicht umgerechnet].
- **Grenzen:** Gewichte sind hier eingesetzte Gitterfreiheiten, keine Dynamik. "Ganze Kammer" heisst 1131 Stichproben
  in 9 Dimensionen (dazu 5 bei L = 2), kein Beweis.

## 4. Selbstanzeigen

1. **jq zum Zaehlen (zweimal):** Vor dem Plan habe ich mit jq group_by/length die Gruppengroessen der alten kammer1.json
   gezaehlt (S1 18, S2 120, S3 20; standen schon in REGULAER-V-1). Waehrend des Schreibens habe ich mit jq length die
   Zahl der Richtungen gezaehlt (40, bekannt). Keine Messzahl ist so entstanden.
2. **Schreiben in den Sitzungs-Scratchpad:** Ein scp-Befehl legte mitte.json (Hauptlauf H1) auch in
   /tmp/claude-1000/.../scratchpad ab. Das ist verboten. Ich habe die Datei etwa eine Minute spaeter geloescht. Dazu
   legt das Werkzeug fuer meine Hintergrund-Warteschleifen und den Monitor Ausgabedateien unter /tmp/claude-1000/.../tasks
   an. Dort steht nur Laufstatus.
3. **CPU statt CUDA:** Eigenwerte (68 x 68 bzw. 544 x 544), Fits, brentq und SLSQP liefen auf der CPU in den
   kleintest-Einheiten der GPU-Spuren p4000a/p4000b (wie REGULAER-V-1). Die Projektregel "auf CUDA" ist nicht woertlich
   erfuellt.
4. **w0\* mit u1 < u2:** Plan 1.6 sagt "den mit u1 > u2". Die mechanische Regel (Plan 5, Code) nimmt aber die
   groesste Marge und vergleicht u1 - u2 erst bei Gleichstand (<= 1e-9). Weil SLSQP an der Iterationsgrenze stoppte,
   lag der Spiegelpunkt 1,3e-7 tiefer. Nach Plan 1.5 sind beide Punkte gleichwertig; gerechnet R 0,0743 gegen 0,0742.
5. **SLSQP nicht konvergiert:** Alle drei Laeufe endeten mit status 9 (Iterationsgrenze). Der Punkt groesster Marge ist
   damit nur auf ~1e-3 in z und ~1e-7 in der Marge bestimmt. Die Rauchtests hatten Stufe 2 nicht durchlaufen.
6. **Rauchtest mit Vorinformation:** Die Fortschrittszeile von R3 zeigte, dass Stufe 1b lief, also weniger als 3
   Nullpunkte auf 6 Strahlen lagen. Das habe ich vor dem Einfrieren gesehen.
7. **Diagnosefeld geteilt:** An der Mitte und an w0* enthaelt 'diagnose' auch die Aufrufe von Probe-Fenster und LHAASO
   (n = 5520). 'gueltig' wurde vorher bestimmt. Das betrifft nur die Dokumentation.
8. **Lesart "Maxwell auf V":** Die Karte nennt LICHT-FINN-NETZ-1 "Maxwell auf V". Dort war es aber M-D auf den
   Diamant-Kanten. Ich habe DEC-Maxwell auf V gerechnet (Plan 1.1). Die LHAASO-Umrechnung ist woertlich uebernommen,
   der Operator ist ein anderer. Die Zahlen 7,0e-28 m und 1,6e-27 m sind deshalb nicht direkt vergleichbar.
9. **Kopfrechnungen [K]:** Umrechnungen a^2 -> l_P^2, Prozent- und Faktorangaben in 2.1 bis 2.4 (K5, K7, Spannen,
   Schranken-Bereich 8,8e-28 bis 2,1e-27 m, "6-mal", "2,5-mal"). Alle anderen Zahlen stammen aus den Laeufen.
10. **Werkzeuge:** Lokal date, ls, mkdir, cp, rm, chmod, sha256sum, sed (eine Ersetzung in hi.py vor dem Einfrieren;
    Pfade fuer sha256sum -c), grep, cat, scp, ssh, jq (lesen und auswaehlen). Kein python, awk oder perl. Eine
    versehentliche Kopie von code/*.py nach lauf-69/code/ habe ich sofort wieder entfernt. Auf der .69 ausserhalb
    von kleintest.sh: mkdir, cp, mv, ls, cat, grep, sha256sum, wc, date, uptime, systemctl --user list-units
    (WM-1-Pruefung), nohup bash fuer die Kettenskripte. Kein python ausserhalb von kleintest.sh. Lock-Dateien nicht
    angefasst.
11. **Nachtraege nach Sicht:** keine Laeufe. Die Vergleiche Licht/Skalar und die Doppelbrechung in Abschnitt 2 und 3 sind
    Beschreibungen vorhandener Laufwerte.

## 5. Negativliste (nicht behaupten)

- Nicht: "Die Hoehe hebt das Wuerfelmuster des Lichts auf." Am skalaren Nullpunkt bleiben 7 %, in keiner Stichprobe
  wechselt beta_L das Vorzeichen.
- Nicht: "Fuer das Licht gibt es keinen isotropen Punkt." Das ist offen; das Minimum liegt bei 0,5 %.
- Nicht: "a2 laesst sich auf null bringen." Alle 1136 Stichproben haben a2 < 0; der kleinste Betrag ist 59 % der Mitte.
- Nicht: "Die LHAASO-Schranke auf Finns Netz ist 1,6e-27 m statt 7,0e-28 m." Es sind zwei bedingte Schranken an zwei
  verschiedene gedachte Operatoren.
- Nicht: "Licht auf V ist frei von Doppelbrechung" (das galt nur fuer M-D).
- Nicht: "w0\* ist der isotrope Punkt." beta = 0 ist eine Flaeche; w0* ist nach Plan der Punkt groesster Marge (mit
  Spiegelpunkt).
- Nicht: "Die Gewichte sind ein physikalisches Feld." Eine Dynamik ist nicht gerechnet.
- Nicht: Messdatenbestaetigung irgendeiner Art.

## 6. Einfach gesagt

Finns Netz kann man mit einer "Hoehe" ueber jedem Eckpunkt verformen, ohne dass es sich umbaut. Wir haben geprueft, ob
diese Hoehe das Licht im Netz in allen Richtungen gleich schnell machen kann, auch bei sehr kurzen Wellen. Die
Grundgeschwindigkeit des Lichts bleibt immer exakt gleich, egal wie die Hoehe steht. Den Richtungsunterschied bei kurzen
Wellen kann die Hoehe stark verkleinern, auf etwa ein Vierzehntel, aber nicht ganz wegmachen; dafuer teilt sich das Licht
in zwei leicht verschieden schnelle Sorten. Fuer die Grenze aus den Gammastrahl-Messungen aendert das fast nichts:
Die Masche muesste weiterhin kleiner als etwa 1,6e-27 m sein, wenn das Netz das Licht so traegt.

---
Ende Ergebnistext: siehe naechste Zeile (date).
Abgabe ERGEBNIS.md: 2026-10-05 14:05:08 CEST (date).
