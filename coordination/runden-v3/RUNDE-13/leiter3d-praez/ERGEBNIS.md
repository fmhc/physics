# LEITER-3D-PRAEZ: Ergebnis (Runde 13, explorativ)

- Code-Agent im Auftrag der Leitung claude-primary. Geruest ab 2026-10-01 19:32:21 CEST, Hauptteil ab 19:46:12 CEST
  (date); letzte Aenderung in der letzten Zeile.
- Beginn 19:08:31 CEST. Plan eingefroren 19:23:48 (PLAN.md.eingefroren-20261001-192348; PLAN.md seither unveraendert,
  gleicher sha256). Kein Nachtrag, kein Folgelauf.
- Alle Laeufe: .69, Spuren cpu und cpu2, ueber kleintest.sh, aus einem einmaligen Starter (start.sh, nohup), 17:23:53
  bis 17:44:21 UTC (19:23:53 bis 19:44:21 CEST), alle rc = 0.
- Markierungen: [A] Auslegung des Code-Agenten (vor den Laeufen im Plan festgelegt), [H] Deutung/Hypothese.
  Alles gilt im linearen, radialen Zweikanalmodell (l = 0, beta = 1/2, abgeschnittener Rand): numerische Evidenz im
  Modell, keine Messung.

## 1. Ergebnis zuerst

1. **Kontrollen bestanden:** K1 (n = 1) und K2 (n = 6) auf beiden Stufen h = 0,04 und h/2 = 0,02. Der Lauf ist
   auswertbar.
2. **Ausgang nach der Regel der Karte: n = 7 gesehen, n = 8 gesehen, n = 9 gesehen, n = 10 gesehen.**
   - Der Vorzeichenwechsel von s liegt bei 0,5598482 / 0,5526191 / 0,5469399 / 0,5423644.
   - Der Umlauf ist auf beiden Stufen aufgeloest (Sprung hoechstens 0,300 rad), mit -1 / +1 / -1 / +1.
   - Die beiden Stufen stimmen auf hoechstens 2,3e-8 ueberein.
   - Das gilt in der strengen Lesart [A] und ebenso in der milderen.
3. **Lage:**
   - Abstand zur Polsuch-Lage der Karte: +4,8e-5 / +1,9e-5 / -6,0e-5 / -3,6e-5. Alle liegen unter 1e-4; die Regel
     verlangt +-3e-4.
   - Abstand zu den genaueren DATENPAKET-Lagen (signierte Wurzel der Polsuche) bei n = 7 bis 9: nur -1,5e-6 /
     -0,8e-6 / -2,7e-6.
   - Die Polbreiten derselben Laeufe (Zusatz) wiederholen die alten Polsuch-Werte in allen gedruckten Stellen. Ihre
     signierten Wurzeln treffen den Wechsel auf hoechstens 2,2e-6.
   - Damit tragen zwei verschiedene Kriterien die 3D-Leiter n = 6 bis 10.
4. **Kernwachstum:**
   - Am Kandidaten: 2,3e5 / 1,3e6 / 7,3e6 / 4,1e7, also unter 1e8.
   - Als Fenstermaximum: 1,6e7 / 1,8e8 / 1,8e9 / 1,9e10. Das alte kurve gibt nur das Fenstermaximum aus; seine
     "1,1e7" (n = 7) und "1,0e9" (n = 8, 9) passen zu diesen Werten. Am Kandidaten liegt das Kernwachstum hier 70- bis
     480-mal darunter.
   - s bleibt gut bestimmt. |s| ist mindestens 1,5e-7. Die Stufen unterscheiden sich in s um hoechstens 8,3e-10, die
     Ausloeschung betraegt hoechstens 7e8.
5. **Keine Zweigmischung:** In jeder Zeile aller zwoelf Laeufe hat L(y_b) im ganzen rho-Fenster genau eine Nullstelle
   (auf der Abtastung mit 400 + 401 Punkten).
   - [H, nicht getestet] Das alte Versagen kam wie in 2D von der linearen Interpolation auf dem groben Raster.
   - Nebenbefund: K2 legt n = 6 neu auf 0,5693598, 3,7e-5 unter dem alten DATENPAKET-Wert.
   - Die Schritte in u = 1/(omega*^2 - 0,5) von n = 5 bis 11 sind damit 2,284 / 2,291 / 2,296 / 2,299 / 2,301 /
     2,300. Bis auf den letzten steigen sie gleichmaessig; n = 11 kommt nur aus der alten Polsuche mit Abstand 6e-4.

## 2. Kontrollen K1 und K2: beide bestanden, auf beiden Stufen

| Kontrolle | h | Wechsel zwischen | omega*^2 | rho* | Abstand zum Soll (omega^2 / rho) | Umlauf (Kreuzung) | groesster Sprung | aufgeloest | Kernwachstum Kandidat / Fenster |
|---|---|---|---|---|---|---|---|---|---|
| K1 (n = 1) | 0,04 | 0,797427 / 0,797677 | 0,79767659 | 1,74461748 | -4,1e-7 / -5,2e-7 | -1 (-1) | 0,289 rad | ja | 3,25 / 5,56 |
| K1 (n = 1) | 0,02 | 0,797427 / 0,797677 | 0,79767678 | 1,74461754 | -2,2e-7 / -4,6e-7 | -1 (-1) | 0,289 rad | ja | 3,21 / 5,39 |
| K2 (n = 6) | 0,04 | 0,56915 / 0,56940 | 0,56935980 | 1,59913308 | -4,0e-5 / - | +1 (+1) | 0,286 rad | ja | 4,19e4 / 1,48e6 |
| K2 (n = 6) | 0,02 | 0,56915 / 0,56940 | 0,56935983 | 1,59913311 | -4,0e-5 / - | +1 (+1) | 0,300 rad | ja | 4,14e4 / 1,44e6 |

- **K1:** Soll laut Karte 0,797677 / 1,744618 auf 1e-4. Gegen den Beweiswert (0,797676787 / 1,744617545) liegt h = 0,02
  bei -1,2e-8 / -4,0e-9, h = 0,04 bei -1,9e-7 / -6,5e-8.
- **K2:** Soll laut Karte 0,56940 +- 2e-4.
  - Die neue Lage 0,5693598 liegt 3,7e-5 unter dem DATENPAKET-Wert 0,5693970. Dieser stammt aus dem alten
    kurve-Feinschritt und hat die Klasse "interpoliert".
  - Die Polbreiten am Zielast (Zusatz, h = 0,02) bilden ein V mit Minimum 6,7e-7 bei 0,5694.
  - Ihre signierte Wurzel (jq, Vorzeichenwahl "Mitte -" mit den Steigungen -20,8 / -20,6) liegt bei 0,5693606, also
    8e-7 neben dem neuen Wechsel.
- **regel** (auf der .69):
  - "Kontrolle k1: je Stufe [True, True] -> bestanden"
  - "Kontrolle k2: je Stufe [True, True] -> bestanden"
  - Die Kette lief danach weiter (KETTE.log: "KONTROLLEN BESTANDEN 2026-10-01T17:29:50+00:00").

## 3. Tabellen je Stelle

- **Zeilen:** je Stelle 9 Zeilen omega^2 = Polsuch-Lage der Karte + k * 2,5e-4, k = -4 .. 4, also +-1e-3. Auf beiden
  Stufen sind alle 9 Profile vorhanden.
- **Abtastung je Zeile:** 400 grobe rho-Punkte im ganzen Fenster, 401 dichte in rho_ref +- 0,02.
- **Nullstellen:** Illinois auf jeder Klammer von L(y_b), bis die Endklammer < 1e-13 ist.
  - Hoechstens 12 Schritte, alle konvergiert.
  - Rest |L(y_b)| hoechstens 1,3e-9 (n = 10), sonst hoechstens 6e-10.
  - s wird exakt an der Nullstelle gerechnet.
- **Paarung:** In jeder Zeile aller Laeufe gibt es genau eine Nullstelle von L(y_b). Der Zielast ist in allen Laeufen
  durchgehend gepaart (ast_konsistent ja). Auf anderen Aesten gibt es keine Wechsel.
- **Rechteck:** omega^2-Seiten sind die Zeilen i - 3 bis i + 4 um den Wechsel (8 Zeilen), rho* +- 0,01.
  - Auf den omega^2-Seiten liegen alle Spruenge bei hoechstens 1,2e-4 rad (K1: 2,5e-3 rad).
  - Die ganze Drehung geschieht auf den rho-Seiten. Dort ist sie nach 5 bis 22 Halbierungsrunden aufgeloest.
- **Abstand:** Wechselort minus Polsuch-Lage der Karte (0,5598 / 0,5526 / 0,5470 / 0,5424). In Klammern steht der
  Abstand zur DATENPAKET-Lage (0,5598497 / 0,5526199 / 0,5469426; n = 10 dort nur Formelwert 0,5424).

### 3a. Wechsel, Lage, Umlauf, Kernwachstum

| Stelle | h | Wechsel zwischen den Zeilen | omega*^2 | rho* | Abstand Karte (DATENPAKET) | Stufen-Differenz | Umlauf (Kreuzung) | groesster Sprung | aufgeloest | Rechteck: Zeilen, Punkte, Runden | Kernwachstum Kandidat / Fenster | Ausloeschung am Kandidaten |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| n = 7 | 0,04 | 0,55980 / 0,56005 | 0,55984822 | 1,58991995 | +4,82e-5 (-1,5e-6) | | -1 (-1) | 0,294 rad | ja | 0,55905 .. 0,5608; 182; 16 | 2,29e5 / 1,58e7 | 6,5e6 |
| n = 7 | 0,02 | 0,55980 / 0,56005 | 0,55984824 | 1,58991997 | +4,82e-5 (-1,5e-6) | 2,1e-8 | -1 (-1) | 0,295 rad | ja | gleich; 180; 16 | 2,31e5 / 1,63e7 | 6,1e6 |
| n = 8 | 0,04 | 0,55260 / 0,55285 | 0,55261909 | 1,58271435 | +1,91e-5 (-0,8e-6) | | +1 (+1) | 0,293 rad | ja | 0,55185 .. 0,5536; 185; 18 | 1,28e6 / 1,76e8 | 6,2e7 |
| n = 8 | 0,02 | 0,55260 / 0,55285 | 0,55261911 | 1,58271438 | +1,91e-5 (-0,8e-6) | 2,3e-8 | +1 (+1) | 0,287 rad | ja | gleich; 191; 18 | 1,28e6 / 1,76e8 | 6,2e7 |
| n = 9 | 0,04 | 0,54675 / 0,54700 | 0,54693988 | 1,57692536 | -6,01e-5 (-2,7e-6) | | -1 (-1) | 0,296 rad | ja | 0,5460 .. 0,54775; 188; 20 | 7,27e6 / 1,80e9 | 8,8e7 |
| n = 9 | 0,02 | 0,54675 / 0,54700 | 0,54693990 | 1,57692537 | -6,01e-5 (-2,7e-6) | 1,6e-8 | -1 (-1) | 0,294 rad | ja | gleich; 192; 20 | 7,27e6 / 1,81e9 | 8,8e7 |
| n = 10 | 0,04 | 0,54215 / 0,54240 | 0,54236441 | 1,57217653 | -3,56e-5 (Formel) | | +1 (+1) | 0,300 rad | ja | 0,5414 .. 0,54315; 192; 22 | 4,00e7 / 1,88e10 | 7,1e8 |
| n = 10 | 0,02 | 0,54215 / 0,54240 | 0,54236442 | 1,57217654 | -3,56e-5 (Formel) | 1,4e-8 | +1 (+1) | 0,275 rad | ja | gleich; 193; 22 | 4,06e7 / 1,95e10 | 6,6e8 |

- **Regel** (Kommando regel auf der .69, LAUF-regel-n7 bis -n10): je Stelle "Ausgang gesehen; Paare 1; alle Rechtecke
  aufgeloest True; vollstaendig True; (Lesart ohne Kernwachstums-Auslegung: gesehen = True)".
- **Kernwachstum am Kandidaten** ist das groessere der beiden Zeilen um den Wechsel. Das Maximum im dichten Fenster
  (rho_ref +- 0,02) betraegt 3,3e5 / 1,9e6 / 1,1e7 / 6,8e7, ebenfalls unter 1e8.
  - Wo im rho-Fenster das Fenstermaximum liegt, habe ich nicht ausgewertet; die Lage wird nicht gespeichert.
  - r_m (Median R_halb): 12,0 / 13,7 / 15,3 / 16,9.
- **Vorzeichen des Umlaufs** (nur berichtet): n gerade +1, n ungerade -1, wie die bisherige Regel. Das gilt auch fuer
  K1 (n = 1: -1) und K2 (n = 6: +1).
- Vergleich mit der Vorhersage MOD-2 fuer n = 10 (0,542382 +- 2e-5): Der Wechsel liegt 1,8e-5 darunter. Das ist
  derselbe Versatz von etwa -2e-5 wie bei n = 11 bis 15 (RUNDE-09).

### 3b. s auf dem Zielast je Zeile (h = 0,02)

h = 0,04 gibt dieselben Werte bis auf hoechstens 8,3e-10 absolut (rho_b bis auf 4,9e-10).

| Zeile k (omega^2 = Lage + k * 2,5e-4) | -4 | -3 | -2 | -1 | 0 | +1 | +2 | +3 | +4 |
|---|---|---|---|---|---|---|---|---|---|
| n = 7 (Lage 0,5598) | +3,373e-5 | +2,666e-5 | +1,894e-5 | +1,063e-5 | +1,794e-6 | -7,501e-6 | -1,718e-5 | -2,716e-5 | -3,735e-5 |
| n = 8 (0,5526) | -1,591e-5 | -1,266e-5 | -8,955e-6 | -4,840e-6 | -3,652e-7 | +4,412e-6 | +9,428e-6 | +1,461e-5 | +1,989e-5 |
| n = 9 (0,5470) | +6,959e-6 | +5,486e-6 | +3,724e-6 | +1,703e-6 | -5,389e-7 | -2,957e-6 | -5,500e-6 | -8,111e-6 | -1,073e-5 |
| n = 10 (0,5424) | -3,167e-6 | -2,588e-6 | -1,829e-6 | -9,084e-7 | +1,507e-7 | +1,317e-6 | +2,553e-6 | +3,818e-6 | +5,067e-6 |

- s ist in jeder Stelle glatt und monoton und wechselt genau einmal das Vorzeichen.
- Die Werte liegen bei n = 7 und 8 im Bereich von 1e-5, bei n = 10 nur bei einigen 1e-6. In 2D verschob das alte
  400-Punkte-Verfahren s um 6e-6 bis 1,1e-4 (RUNDE-12). Ein Fehler dieser Groesse verdeckt die Wechsel hier [H].

### 3c. Zusatz, nicht Teil der Regel: Polbreiten Gamma = -Im rho am Zielast (Pluecker-Newton, h = 0,02)

| Zeile k | -4 | -3 | -2 | -1 | 0 | +1 | +2 | +3 | +4 | signierte Wurzel (jq) | minus Wechsel |
|---|---|---|---|---|---|---|---|---|---|---|---|
| n = 7 | 8,50e-4 | 4,91e-4 | 2,30e-4 | 6,78e-5 | **1,811e-6** | 3,00e-5 | 1,49e-4 | 3,56e-4 | 6,46e-4 | 0,5598493 | +1,1e-6 |
| n = 8 | 1,30e-3 | 7,39e-4 | 3,34e-4 | 8,92e-5 | **4,658e-7** | 6,36e-5 | 2,73e-4 | 6,21e-4 | 1,10e-3 | 0,5526197 | +6,0e-7 |
| n = 9 | 1,71e-3 | 9,13e-4 | 3,69e-4 | 6,87e-5 | **6,236e-6** | 1,73e-4 | 5,58e-4 | 1,15e-3 | 1,93e-3 | 0,5469421 | +2,2e-6 |
| n = 10 | 2,64e-3 | 1,44e-3 | 6,01e-4 | 1,28e-4 | **3,083e-6** | 2,14e-4 | 7,44e-4 | 1,57e-3 | 2,68e-3 | 0,5423664 | +1,9e-6 |

- Das Minimum liegt jeweils in der mittleren Zeile, also an der Kartenlage.
- Die Mittelwerte bei n = 7, 8, 9 stimmen in allen gedruckten Stellen mit den alten Polsuch-Laeufen ueberein
  (RUNDE-09: 1,81e-6 / 4,66e-7 / 6,24e-6). Die Realteile der Pole stimmen auf wenige 1e-9 (z. B. n = 7 1,58975673
  gegen 1,5897567257).
- Signierte Wurzel: aus den drei Punkten um das Minimum, Vorzeichenwahl mit den aehnlicheren Steigungen (n = 7:
  -27,5 / -27,3; n = 8: -35,0 / -34,6; n = 9: -43,1 / -42,6; n = 10: -52,2 / -51,4).
- Breitenminimum und Vorzeichenwechsel liegen auf hoechstens 2,2e-6 beieinander. In 2D waren es 2e-6 (RUNDE-12).

## 4. Vorab gegen Ausgang

| Vorab (Karte, Leitung; PLAN Abschnitt 1) | Ausgang |
|---|---|
| K1 und K2 bestehen: ~85 % | bestanden, beide Stufen |
| n = 7 gesehen: ~70 % | gesehen |
| n = 8 gesehen: ~70 % | gesehen |
| n = 9 gesehen: ~55 % | gesehen |
| n = 10 gesehen: ~55 % | gesehen |
| Grund: dieselbe Abtastursache wie in 2D | vereinbar, aber nicht direkt getestet [H]: s ist hier exakt gerechnet, das alte Verfahren lief nicht mit |
| Hauptrisiko Kernwachstum am Kandidaten (alt bis 1,1e7 bzw. 1e9) | am Kandidaten 2,3e5 bis 4,1e7, unter 1e8; 1e9 und mehr nur als Fenstermaximum (1,8e9 bei n = 9, 1,9e10 bei n = 10) |
| "ob das am Kandidaten oder nur im Fenstermaximum war, ist unklar" | Fenstermaximum: am Kandidaten 7,3e6 (n = 9) gegen 1,8e9 im Fenster |
| Wenn gesehen: Abstand zur Polsuch-Lage < 1e-4 | getroffen: 4,8e-5 / 1,9e-5 / 6,0e-5 / 3,6e-5 zur Kartenlage; 1,5e-6 / 0,8e-6 / 2,7e-6 zur DATENPAKET-Lage |
| Vergleich 2D: Vorzeichen- und Breitenkriterium auf 2e-6 beieinander | 3D: 0,6e-6 bis 2,2e-6 (Abschnitt 3c) |

| Vorab (Code-Agent, PLAN Abschnitt 7) | Ausgang |
|---|---|
| K1 und K2 bestehen: 0,85 | bestanden |
| n = 7 gesehen: 0,85 (nicht blind, Rauchtest) | gesehen |
| n = 8 gesehen: 0,75; n = 9: 0,6; n = 10: 0,45 | alle gesehen |
| Kernwachstum am Kandidaten: n = 8 ~2e6, n = 9 ~1e7, n = 10 ~7e7 | 1,3e6 / 7,3e6 / 4,1e7: richtige Groessenordnung, je 1,4- bis 1,7-mal zu hoch geschaetzt |
| n = 10 "leicht unentschieden" nach der strengen Lesart | nicht eingetreten (4,1e7 < 1e8) |
| Abstand zur DATENPAKET-Lage < 3e-5 | getroffen (hoechstens 2,7e-6) |
| Abstand zur Kartenlage < 1e-4 | getroffen |
| n = 10 bei 0,54238 +- 3e-5 | getroffen (0,5423644, Abstand -1,6e-5) |
| Umlauf n gerade +1, n ungerade -1: 0,8 | getroffen (6 von 6 einschliesslich K1, K2) |

## 5. Laufzeiten und Hashes

### Laeufe (.69, kleintest.sh, Zeiten UTC = CEST - 2 h; Rechenzeit laut Programm)

| Lauf | Spur | Start | Ende | rc | Rechenzeit | Profil je Zeile (max) |
|---|---|---|---|---|---|---|
| k2-h002 | cpu | 17:23:53 | 17:27:51 | 0 | 221 s | 17,3 s |
| k1-h002 | cpu2 | 17:23:53 | 17:27:19 | 0 | 187 s | 16,6 s |
| k2-h004 | cpu2 | 17:27:19 | 17:29:33 | 0 | 131 s | 9,9 s |
| k1-h004 | cpu | 17:27:51 | 17:29:44 | 0 | 110 s | 9,2 s |
| regel-k1, regel-k2 | cpu | 17:29:44 | 17:29:50 | 0, 0 | je < 1 s | - |
| n7-h002 | cpu | 17:29:50 | 17:33:52 | 0 | 239 s | 17,7 s |
| n7-h004 | cpu2 | 17:29:50 | 17:32:15 | 0 | 142 s | 10,5 s |
| n8-h002 | cpu2 | 17:32:15 | 17:36:37 | 0 | 259 s | 18,8 s |
| n8-h004 | cpu | 17:33:52 | 17:36:25 | 0 | 150 s | 10,7 s |
| n9-h002 | cpu | 17:36:25 | 17:40:59 | 0 | 271 s | 20,3 s |
| n9-h004 | cpu2 | 17:36:37 | 17:39:20 | 0 | 160 s | 11,1 s |
| n10-h002 | cpu2 | 17:39:20 | 17:44:09 | 0 | 287 s | 20,0 s |
| n10-h004 | cpu | 17:40:59 | 17:43:48 | 0 | 166 s | 11,5 s |
| regel-n7 bis regel-n10 | cpu | 17:44:09 | 17:44:21 | 0 (4x) | je < 1 s | - |

- Kein Aufruf kam an die Budgetgrenze (500 s) oder an RuntimeMaxSec (600 s). "entfallen" ist ueberall leer; die Pole
  (Zusatz) liefen ueberall mit.
- Lokale Rauchtests (ungueltig fuer die Regel): rauch1 20,0 s, rauch2 51,0 s, zweimal regel unter 5 s (lauf-lokal/).

### sha256

- Original RUNDE-07/bic2/bic2.py: ee1ef6d226e8ec2c262e40a6d0e1b571a2a6fe40d334831f8e4ccb0856df12ce
- bic2_3d_praez.py (lokal = .69): ba86ae6a61eb31b3afbbefcd630771ae627dfcaaa33b9bd7903b768d44838e9b
- bic2_3d_praez.diff: 4083e083a3cce35a5b2e8a25640221fbda86a1203e3b17257dccd294fc486f3d
- PLAN.md.eingefroren-20261001-192348 (= PLAN.md, lokal = .69): 75911bb69cdbf7dfd5b69ed0e49e1d26083ffc6b8b2c1008e1aa8662b1f9e34a
- start.sh (lokal = .69): 8438a87950a874c1b5e63feef5c3af771d5fd173952630f8963e908a405823bf
- tabellen.jq: 0e09ea6e5999725610367a3fd3c7899a43a5d3908616d27c952016f063dbcb65
- Ausgaben (lokal in lauf-69/, Kopie der .69):
  - k1-h004/praez.json 0c7ecd601cc88dd4ddc950bd0e9b30f41ec10d153c1e08932d487e188ff84b59
  - k1-h002/praez.json 6da03f633fd180fd08147123b8d944e25e7ce34c906acf6944c00505198cf20c
  - k2-h004/praez.json fc45eda57e530da75fd767ed42e3557e4dfe85573fa31b0a3122a74fcdb5e599
  - k2-h002/praez.json 04879345d3a17b4507b5ecc748896072c21deed41b88593f6cc64411c344e5c8
  - n7-h004/praez.json 7ce2a7270a4c7976a08cf739f98376f7e14b6de59d02212dce85b3a750f10e76
  - n7-h002/praez.json 6ca17417b27bd2790a4aef134295b10504257dc76e175b3ad51aa2d9c735332e
  - n8-h004/praez.json b88af9fb3d565bfa9b691738578e5b0b64f7aa8002b1ced7fa30d22ed818341a
  - n8-h002/praez.json 207f8e41dccba966807caaa27dfb4d1ab717401e90f211d69fb3b106e74a960d
  - n9-h004/praez.json dfee8115f5eea9053d0bfd159be371f9cb994d9ce0d57d2760095e81ad22c2e9
  - n9-h002/praez.json be75f6cd8cae2ae2e9cd34ec4bce493f101b64aa53c5dac82ed4b9c3e0a8cfdb
  - n10-h004/praez.json 38eb276b8d8f80f0fc2c6b42a2609500a36bf273c3740670b2f3f2626a177884
  - n10-h002/praez.json 21b23184b8e220e7a64f629dc8ab9afb99961d578739c397f51315d7b437512f (lokal = .69 geprueft)
  - regel-k1/regel.json 003f9300c8c2d8ea69b5a7eb849a5e390cbf076c3d7d49b5f2fe73e2d4974ab5
  - regel-k2/regel.json faf3f68d864d95ae5f17d657c802461ea221b1b11df40c9292652dbce7f037ec
  - regel-n7/regel.json 39b4b2c529f27eb3e4393045882819d0bf93354041f65b71c0e12e703827c4dc
  - regel-n8/regel.json fc949fb1629a9475c2fc1ac4ebec2ee74dd9b2188598b03625f36e38ac0b86a5
  - regel-n9/regel.json 174c921479f7dc0981771f1a98bc270f07da811eb3e74f3823b4c00f57c65626
  - regel-n10/regel.json 6c621b0d538dcbb36980409dd95a419fdaf4a4015d1ba321d15c4212f9844330
  - KETTE.log ccea1b34befe4aa54af8586fac790ce165538169112209b97cab19bd6e75735d

## 6. Selbstanzeigen

- **Gitterstufen h = 0,04 und h/2 = 0,02** statt der in RUNDE-07 bis 09 ueblichen 0,02 / 0,01.
  - Im Plan vor den Laeufen festgelegt und begruendet: Neun Profile bei h = 0,01 haetten allein etwa 5 min je Aufruf
    gekostet.
  - h = 0,02 ist die Stufe der Polsuche. Eine Stufe h = 0,01 fehlt.
- **Der Rauchtest vor dem Einfrieren zeigte n = 7 schon.**
  - rauch2 (lokal, 3 Zeilen, h = 0,04) fand den Wechsel bei 0,559848 mit aufgeloestem Umlauf -1.
  - Meine eigene Vorhersage fuer n = 7 ist darum nicht blind; das steht im Plan.
  - Die Vorhersage der Leitung stand vorher. Regel, Zeilen und Kriterien kommen aus der Karte und wurden nicht
    geaendert.
- **Auslegungen [A]**, im Plan vor den Laeufen festgelegt, nicht von der Leitung:
  - strenge Lesart von "auch Kernwachstum > 1e8 oder ein nicht aufgeloestes Rechteck" (gilt auch fuer "gesehen");
  - K2 verlangt zusaetzlich Umlauf +-1 (Wortlaut: "Umlauf aufgeloest");
  - Zielast, Lage per linearer Interpolation von s, Kernwachstum am Kandidaten = groesseres der beiden Nachbarzeilen.
  - Der Ausgang haengt an keiner dieser Auslegungen: Beide Lesarten geben "gesehen", und K2 besteht auch mit +-1.
- **Lokale Befehle:**
  - python3 nur fuer Rauchtests: rauch1 20 s, rauch2 51 s, zweimal regel je unter 5 s; je 1 Thread, nice 19, timeout.
  - Sonst lokal jq (auch fuer Rechnungen: Abstaende, u-Schritte, signierte Wurzeln), sha256sum, rsync, ssh, date, grep,
    sed.
  - Dazu die reinen Datei- und Anzeigebefehle cp, mkdir, chmod, diff (fuer die Diff-Datei), ls, cat, head, tail, wc,
    sort, comm.
  - Kein awk.
- **Sperren geprueft:** Vor dem Start habe ich auf der .69 mit `flock -n <lock> true` geprueft, ob cpu und cpu2 frei
  sind. Das nimmt die Sperre fuer einen Augenblick und gibt sie sofort zurueck; es lief dabei nichts.
- **Startbefehl:** Der ssh-Aufruf, der start.sh per nohup setsid startete, kehrte im Werkzeug nicht zurueck. Die
  entfernte Shell wartete auf ihr Hintergrundkind. Er lief als lokaler Hintergrundauftrag bis zum Kettenende weiter und
  hatte keinen Einfluss auf die Kette.
- **Beobachtung waehrend der Laeufe:**
  - lesende ssh-Abfragen (grep, cat, tail) alle 15 bis 30 s, ueber das Monitor-Werkzeug und Warteschleifen;
  - nichts gestartet oder beendet.
  - Die Ausgaben der Warteschleifen legte das Werkzeug selbst unter /tmp/claude-1000/.../tasks/ ab. Das sind keine von
    mir angelegten Hilfsdateien.
- **Zusaetzlich gerechnet** (nicht Teil der Regel, im Plan als Zusatz angekuendigt):
  - Polbreiten am Zielast und ihre signierten Wurzeln (jq).
  - u-Schritte mit den DATENPAKET-Werten n = 5, 11 und 12.
- **Sonst:**
  - kein git, kein Peerbus, keine Unteragenten, keine Dienste, Timer oder Hooks;
  - nur die Spuren cpu und cpu2, jeder Aufruf unter 10 min;
  - auf der .69 nichts in place ueberschrieben;
  - Dateien nur in RUNDE-13/leiter3d-praez/ und runde13-leiter3d-praez/.

## 7. Grenzen

- Nur zwei Stufen 0,04 / 0,02; die Polsuche lief bei 0,02. Eine Stufe h = 0,01 fehlt.
- **Lage:** Je Stelle 9 Zeilen im Abstand 2,5e-4; die Lage des Wechsels ist linear zwischen zwei Zeilen interpoliert,
  ohne Verfeinerung in omega^2.
  - Fuer die Regel (+-3e-4, Stufen 1e-4) reicht das.
  - Die Interpolationsunsicherheit schaetze ich aus der Kruemmung von s ueber die Zeilen auf wenige 1e-6 [A].
  - Die Abstaende von 0,6e-6 bis 2,2e-6 zur signierten Wurzel liegen in dieser Groesse.
- Die Rechtecke benutzen die Zeilen als omega^2-Seiten (keine neuen Profile); nur die rho-Seiten werden halbiert.
- **Kernwachstum:** Es enthaelt den Faktor des regulaeren Starts und haengt am Anschluss r_m = Median R_halb (lin_multi,
  unveraendert). Die Grenze 1e8 ist eine Konvention aus RUNDE-08, kein abgeleiteter Fehlerwert.
- **Unabhaengigkeit:** Vorzeichentest und Polsuche teilen Profile, Gleichungen und Code (bic2). Sie sind zwei
  verschiedene Kriterien (Nullstelle von W bei reellem rho gegen Minimum der Polbreite), aber keine zwei unabhaengigen
  Programme.
- **Ursache des alten Versagens:** Ich habe sie nicht nachgerechnet. Das alte Verfahren (kurve, 400 Punkte) lief hier
  nicht mit. "Abtastursache" ist darum eine Hypothese, gestuetzt nur durch die 2D-Rechnung (RUNDE-12) und durch die
  Groesse von s.
- **n = 10:** Die Polsuch-Lage 0,5424 der Karte ist laut DATENPAKET ein Formelwert, kein Polsuch-Minimum. Die Regel habe
  ich wie vorgegeben gegen 0,5424 angewandt.
- **Modell:** linear, radial, l = 0, beta = 1/2, abgeschnittener Rand. Keine Aussage ueber l > 0 oder die nichtlineare
  Dynamik.
- **Offene Frage an die Leitung:** Welche Lesart von "auch Kernwachstum > 1e8" ist gemeint? Fuer diesen Lauf ist die
  Frage folgenlos, fuer hoehere n (Kernwachstum am Kandidaten ~4e7 bei n = 10, wachsend) nicht.

## 8. Einfach gesagt

Die stillen Stellen sind besondere Frequenzen, an denen ein schwingender Ball fast gar keine Wellen abstrahlt. In 3D
gab es fuer die Stufen 7 bis 10 bisher nur einen Hinweis, eine sehr kleine Abstrahlbreite; der zweite Test, ein
Vorzeichenwechsel, hatte dort versagt. Jetzt habe ich diesen Test mit einer genauen Nullstellensuche statt einer groben
Abtastung wiederholt. Bei allen vier Stufen wechselt das Vorzeichen genau einmal, an fast derselben Stelle
wie das Breitenminimum, und der Rundlauf-Test zeigt jedes Mal sauber eine Drehung, abwechselnd links- und rechtsherum.
Zwei verschiedene Kriterien sagen also dasselbe, und die Leiter steht in 3D bis Stufe 10 auf festeren Fuessen,
allerdings nur im Rechenmodell.

---
Letzte Aenderung dieser Datei: 2026-10-01 19:49:47 CEST (date). Zeitbox 75 min ab 19:08:31 eingehalten.
