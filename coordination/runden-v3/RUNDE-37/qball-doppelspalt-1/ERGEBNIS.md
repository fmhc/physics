# QBALL-DOPPELSPALT-1: Ergebnis (Code-Agent fuer claude-primary)

- Start des Agenten 2026-10-05 05:36:34 CEST; ERGEBNIS geschrieben ab 06:09 CEST (Entwurf), fertiggestellt ab 07:11:58 CEST (date).
- **Eingefroren** 06:02:52 CEST: PLAN.md.eingefroren-20261005-060252, code/qds.py.eingefroren-20261005-060252,
  code/auswertung.py.eingefroren-20261005-060252 (Hashes in EINGEFROREN-SHA256.txt). Das war vor Ruhetest, Kleintest
  und allen Hauptlaeufen. Auf der .69 liefen dieselben Hashes (qds.py 1d7d2d44..., auswertung.py 6cea14f4...).
- Kennzeichen: [M] eigene Mathematik/Kopfrechnung, [E] gerechnet (.69), [P] Projektdatei, [L] Literatur, [H] Hypothese,
  [D] beschreibend (Zusatzarm W, Nachtrag; kein Urteil).
- Alles ist eine synthetische Rechnung im Modell (2+1 Dimensionen, Papier-I-Potential). **Keine Messdatenbestaetigung.**

## 1. Zeiten und Laeufe

- Alle Laeufe auf der .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh (Einheit mit CPUQuota 100 %,
  MemoryMax 4G, RuntimeMaxSec 600), torch 2.5.1+cu121 auf Quadro P4000, float32. Zeiten UTC aus den kleintest-Logs
  (start/ende); CEST = UTC + 2.
- Aufrufform: bash kleintest.sh <spur> qds-<name> code/qds.py <modus> --out lauf/<name>.json ... (Argumente je Lauf im
  Kopf der JSON-Datei, Feld "argumente"; Laufskripte code/stufe*.sh, code/nachtrag1*.sh, code/auswerten.sh).

| Stufe | Lauf (Name) | Spur | Start bis Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| Rauch (vor Plan/Einfrieren) | r1b bilanz, r1p profil | p4000a | 03:51:50 bis 03:51:58 | 4 + 4 s | 0, 0 |
| Rauch | r2a1, r2a2, r2a3 (Zeit, linear, Fremdwerte) | p4000a | 03:54:21 bis 03:54:55 | 17 + 10 + 7 s | 0, 0, 0 |
| Rauch | r2b1, r2b2 (h = 0,125 Zeit, Ruhe-Pfad) | p4000b | 03:54:21 bis 03:54:51 | 22 + 8 s | 0, 0 |
| Rauch | r3a1, r3a2 (Fremdwerte, Teilstapel) | p4000a | 03:57:45 bis 03:59:14 | 25 + 64 s | 0, 0 |
| Rauch | r3b1 (linear, Fremdwerte) | p4000b | 03:57:45 bis 03:58:26 | 41 s | 0 |
| Rauch | r3aw, r4, r4aw (Auswertungstest, w = 3R Fremdwerte) | p4000a | 03:59:45 bis 04:02:40 | 7 + 28 + 8 s | 0, 0, 0 |
| 0 | profil (eingefroren) | p4000a | 04:03:12 bis 04:03:15 | 3 s | 0 |
| 0 | bilanz, ruhe | p4000a | 04:03:18 bis 04:03:51 | 3 + 30 s | 0, 0 |
| 1 | klein1 (d = R), klein2 (fern): Kleintest 84 Laeufe | p4000b | 04:03:18 bis 04:04:24 | 33 + 33 s | 0, 0 |
| 2 | q2-0.8-1R, -1.5R, -fern, -3R | p4000a | 04:04:31 bis 04:14:59 | 158, 167, 160, 143 s | 0 |
| 2 | q2-0.9-1R, -1.5R, -fern, -3R | p4000b | 04:04:31 bis 04:15:18 | 174, 180, 155, 138 s | 0 |
| Zwischen | aw-zwischen1 (Auswertung) | p4000a | 04:13:18 (Warten auf Lock) bis 04:15:07 | ~10 s Rechnung | 0 |
| 3 | q3-0.8-1R, -1.5R | p4000a | 04:14:59 bis 04:26:54 | 367, 348 s | 0 |
| 3 | q3-0.9-1R, -1.5R | p4000b | 04:15:18 bis 04:26:39 | 340, 341 s | 0 |
| 3 | l3-0.8-1R, -1.5R (linear) | p4000a | 04:26:54 bis 04:36:19 | 291, 274 s | 0 |
| 3 | l3-0.9-1R, -1.5R (linear) | p4000b | 04:26:39 bis 04:35:56 | 293, 264 s | 0 |
| W | w3q2-0.8-1R, -1.5R, -fern | p4000a | 04:36:23 bis 04:43:32 | 142, 144, 143 s | 0 |
| W | w3q2-0.9-1R, -1.5R, -fern | p4000b | 04:35:58 bis 04:42:57 | 140, 139, 140 s | 0 |
| Zwischen | aw-zwischen2 (Auswertung) | p4000b | 04:43:42 (Lock) bis 04:48:52 | ~13 s Rechnung | 0 |
| W | w3q3-0.8-1R, -1.5R | p4000a | 04:43:32 bis 04:55:12 | 347, 353 s | 0 |
| W | w3q3-0.9-1R, -1.5R | p4000b | 04:42:57 bis 04:54:32 | 342, 353 s (inkl. ~13 s Lock) | 0 |
| W | w3l3-0.8-1R, -1.5R (linear) | p4000a | 04:55:12 bis 05:04:32 | 288, 272 s | 0 |
| W | w3l3-0.9-1R, -1.5R (linear) | p4000b | 04:54:32 bis 05:03:45 | 265, 288 s | 0 |
| N1 | w3q2-0.8-1R-n81, -h0125 | p4000a | 05:04:32 bis 05:09:08 | 143, 133 s | 0 |
| N1 | w3q2-0.9-1R-n81, -h0125 | p4000b | 05:03:45 bis 05:08:10 | 136, 129 s | 0 |
| Auswertung | aw-final (auswertung.json, Bilder) | p4000a | 05:09:12 bis 05:09:25 | 13 s | 0 |

- Alle 55 Einheiten (13 Rauch, 42 nach dem Einfrieren) mit rc = 0; keine lief in die Zeitgrenze. Groesster Stapel 205 Laeufe (1,56 GB GPU).
- **Kartenprogramm:** Ruhetest, Kleintest, Doppelspalt (4 d) und Dreifachspalt (d <= 1,5R, Ball und linear) sind
  vollstaendig gelaufen. Die Konvergenzlaeufe 2k und 3k entfielen nach Planregel (keine wertbare Kombination).
- **Dateien:**
  - lauf-69/ enthaelt alle Laufdateien (*.json, *.log), auswertung.json, die Bilder qds-bild*.png und lauf-klein/.
  - lauf-69/PRUEFSUMMEN-69.txt und -lokal.txt: 47 Dateien, auf der .69 und lokal gleich (geprueft 07:13 CEST).
  - Der Code auf der .69 hat dieselben Hashes wie die eingefrorenen Kopien; PLAN.md ist seit dem Einfrieren
    unveraendert.
  - Dazu rauch-69/ (Rauchtests), quellen/ (arXiv-PDF), BILD-*.png und code/ (Laufskripte, jq-Lesefilter).
  - Auf der .69: /home/fmh/fmhc-physics-remote/qball-doppelspalt-1/.

## 2. Was arXiv:1508.06837 schon enthaelt

- Quelle: quellen/arxiv-1508.06837-20261005-054245.pdf (Ekomasov und Salimov 2015, 5 Seiten, an der Quelle gelesen).
- Enthalten:
  - eine radiale (3+1)-D-Atmerloesung (Gl. 3, Abb. 1 und 2);
  - die Lorentz-Modulation einer inneren Schwingung, gedeutet als de-Broglie-Welle mit lambda = 2 pi/(gamma omega v);
  - ein Schema (Teilung an zwei Spalten, Wiedervereinigung) und die Erwartung, dass das Muster fuer d >> A
    (Solitongroesse) verschwindet.
- Nicht enthalten: keine Rechnung eines Spaltdurchgangs, kein Histogramm, keine Skalierung mit v, kein I3, keine
  Teilungsstatistik, kein Q-Ball. Der Kern der Karte war dort nicht gerechnet; das volle Programm lief.

## 3. Ergebnis zuerst

1. **Im Kartenaufbau (Spaltbreite w = R) kommt der klassische Q-Ball nie durch [E].**
   - Alle 4428 Laeufe enden reflektiert: Doppel- und Dreifachspalt, beide omega, alle v und d.
   - Hoechstens 5 % der Ladung sickern als kleine Welle durch (v = 0,45), bei v = 0,2 praktisch nichts.
   - Ruhe- und Fahrtest sind sauber (Ladungsverlust <= 5e-6), der Kleintest zeigt dasselbe (84 von 84 reflektiert).
2. **Deshalb sind alle vier Vorhersagen nicht pruefbar.** V-Q1, V-Q3 und V-Q4 sind "unentschieden (keine wertbare
   Kombination)". V-Q2 ergibt mechanisch "kein Muster", weil das Histogramm leer ist.
   - Der Grund war vorab ableitbar (PLAN 2f, vor dem Einfrieren): Ein Spalt schmaler als der Ball liegt fuer dessen
     Ladungsquanten unter der Grenzfrequenz.
   - Auch das lineare Kontrollpaket gleicher Breite kommt nur zu ~2 % je Spalt durch.
3. **Zusatzarm W (w = 3R, beschreibend):** Je Einzelspalt gehen 0 % (omega 0,9, v = 0,2) bis 24 % der Laeufe durch,
   als Ganzes und durch genau einen Spalt.
   - Beim fernen Abstand ist AB exakt A + B (r2 = 0,000).
   - Beim nahen Abstand (d <= 1,5R) weicht AB geometrisch ab (r2 bis 0,59).
   - Die Winkelverteilung zeigt Linsen- und Regenbogenkanten, aber keine mit 1/(gamma v) skalierende Periode.
   - Kein Lauf endet mit zwei Baellen. Bei omega = 0,9 und v = 0,45 zerfliesst der Ball, wenn er den Steg trifft (Teile unter der
     Townes-Ladung).
4. **Dreifachspalt im Arm W [D]:** Die Durchgangszahlen sind additiv (ABC = A + B + C, kappa_int <= 0,006).
   - Winkelaufgeloest ist abs(I3) hoechstens ~1 Lauf von 41.
   - kappa_L1 (0,01 bis 0,41) und seine Differenz zum Rand-kappa des linearen Arms (-0,18 bis +0,15) sind nicht
     konvergiert. Schon im Doppelspalt aendert sich r2 zwischen 41 und 81 Stossparametern um bis 0,10 (Nachtrag N1,
     Abschn. 5f).
5. **Bedeutung [H]:** Der klassische Q-Ball verhaelt sich an Spalten wie ein ausgedehntes klassisches Teilchen. Er
   passt nur durch Spalte, die breiter sind als er; seine innere Uhr steuert die Ablenkung nicht erkennbar. Das stuetzt
   Finns Weiche "Q-Baelle nur fuers Teilchenmodell". Interferenz muesste aus der quantisierten Schwerpunktbewegung
   kommen.

## 4. Urteile (mechanisch, lauf-69/auswertung.json; Karte unveraendert)

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | nach Plan | nach Kartenwortlaut | Konvergenz | tragende Werte [E] |
|---|---|---|---|---|---|---|
| V-Q1 | d = 2R + 4/kappa: abs(I2)/Summe < 0,05 | 85 % | **unentschieden** (keine wertbare Kombination) | **unentschieden** | nicht geprueft (2k entfiel, Planregel) | 0 Durchgaenge in 6 x 82 Laeufen; P_A = P_B = P_AB = 0 |
| V-Q2 | d <= 1,5R: Periode ~ 1/(gamma v) auf +-20 % | 35 % | **"kein Muster"** (mechanisch; leeres Histogramm) | **"kein Muster"** (ebenso) | (keine Bindung) | 0 Durchgaenge bei d = R und 1,5R; keine Ablenkstatistik |
| V-Q3 | d <= 1,5R: abs(kappa) - Rand >= 0,05 | 55 % | **unentschieden** (keine wertbare Kombination) | **unentschieden** | nicht geprueft (3k entfiel) | 0 Durchgaenge in 12 x 205 Laeufen |
| V-Q4 | d <= R: >= 20 % der Durchgelassenen in zwei Stuecke >= 10 % Q | 40 % | **unentschieden** (weniger als 5 Durchgelassene: 0) | **unentschieden** (0) | (keine Bindung) | 0 von 246 Laeufen (AB, d = R) durchgelassen (A ebenso 0 von 246) |

- **Vorab ableitbar war der gemeinsame Grund** (PLAN Abschn. 2f, vor dem Einfrieren): Der Spalt der Breite R ist fuer
  die Ladungsquanten des Balls ein Wellenleiter unterhalb der Grenzfrequenz. Der Plan schaetzte "kaum oder keine
  Durchgaenge"; eingetroffen ist "keine".
- "Kein Muster" bei V-Q2 heisst hier **nicht**, dass eine Struktur fehlt. Es gibt schlicht keine Durchgangsstatistik.
  Ich werte V-Q2 deshalb inhaltlich als nicht pruefbar. Der Planwortlaut ergibt mechanisch "kein Muster".
- Zusatzarm W (w = 3R) hat nach Plan kein Urteil. Seine Zahlen stehen beschreibend in Abschn. 5d bis 5f.

## 5. Tabellen

### 5a. Ausgangszustand je Gitter (Pflicht c; lauf-69/ruhe.json) [E]

Ball in Ruhe bei (0, 0) ohne Wand, T = 200 (4000 Schritte); Fahrtest v = 0,45 ohne Wand, T = 88,9, Soll-Endort x = 25.

| omega, h | Q Gitter / radial | Ruhe: max abs(dQ)/Q | Ruhe: dE/E | E Gitter/E radial - 1 | Ruhe: S_max/S0 | Fahrt: max abs(dQ)/Q | Fahrt: E/(gamma E_rad) - 1 | Fahrt: dE/E | Fahrt: x(T) |
|---|---|---|---|---|---|---|---|---|---|
| 0,8; 0,25 | 38,54337 / 38,54342 | 2,3e-7 | -9,0e-7 | -2,0e-4 | 0,9978 bis 1,0007 | 3,2e-6 | -6,2e-4 | -5,5e-6 | 24,807 |
| 0,8; 0,125 | 38,54337 / 38,54342 | 5,2e-7 | +3,9e-7 | -5,8e-5 | 0,9994 bis 1,0002 | 5,7e-6 | -1,6e-4 | -6,2e-6 | 24,966 |
| 0,9; 0,25 | 15,81879 / 15,81881 | 4,8e-6 | -5,5e-6 | -1,8e-4 | 1,0020 bis 1,0145 | 6,4e-6 | -6,4e-4 | -8,3e-6 | 24,788 |
| 0,9; 0,125 | 15,81879 / 15,81881 | 4,3e-7 | +2,0e-7 | -5,3e-5 | 1,0008 bis 1,0044 | 5,1e-6 | -1,6e-4 | -5,4e-6 | 24,964 |

- **Abbruchregel nicht ausgeloest:** groesster Ladungsverlust 4,8e-6, Schwelle 1e-2. Weiter ausgewertet.
- Gitterfehler zweiter Ordnung: E-Abweichung -2,0e-4 gegen -5,8e-5 (Faktor 3,4 bei halbem h) [M, Kopfrechnung].
  Der bewegte Ball ist auf dem groben Gitter 0,8 % langsamer (24,81 statt 25), auf dem feinen 0,14 %.

### 5b. Kleintest (Karte: omega 0,8; d = R und 2R + 4/kappa; v = 0,2 und 0,45; 21 y; AB; lauf-69/lauf-klein/) [E]

| d | v | Ausgangsklassen | durchgelassene Ladung max / Mittel | Energieverlust (Abstrahlung) |
|---|---|---|---|---|
| R | 0,2 | 21 reflektiert | 1e-4 / 0 | 0,03 bis 0,12 % |
| R | 0,45 | 21 reflektiert | 0,049 / 0,020 | 0,5 bis 1,2 % |
| 2R + 4/kappa | 0,2 | 21 reflektiert | 1e-4 / 0 | 0,02 bis 0,11 % |
| 2R + 4/kappa | 0,45 | 21 reflektiert | 0,048 / 0,013 | 0,7 bis 1,8 % |

### 5c. Ausgangsklassen der Kartenlaeufe (w = R; lauf-69/q2-*.json, q3-*.json) [E]

- **Alle 4428 Laeufe "reflektiert"**: Doppelspalt 2 omega x 4 d x 3 v x 82 (A und AB) = 1968, Dreifachspalt 2 omega
  x 2 d x 3 v x 205 (A, B, AB, AC, ABC) = 2460; dazu die gespiegelten Konfigurationen B, C und BC.
- In jedem Lauf gibt es genau ein Stueck, es liegt auf der Einfallseite und traegt mindestens 90,6 % der Ladung.
- Durchgesickerte Ladung (x > 2 bei t = T, Anteil von Q), ueber d und Konfigurationen zusammengefasst:

| omega | v = 0,2: max | v = 0,3: max / Mittel | v = 0,45: max / Mittel |
|---|---|---|---|
| 0,8 | 1e-4 | 0,0031 / 0,0006 bis 0,0009 | 0,052 / 0,010 bis 0,016 |
| 0,9 | 2e-4 | 0,0024 / 0,0003 bis 0,0005 | 0,025 / 0,0035 bis 0,0061 |

### 5d. Zusatzarm W, Doppelspalt mit w = 3R [D; beschreibend, kein Urteil; lauf-69/w3q2-*.json, auswertung.json]

- Je Zeile 41 Stossparameter. "Durchgaenge" = Laeufe mit durchgelassenem Stueck >= 10 % Q (A bzw. AB; B = Spiegel von A).
- r2 = Summe abs(I2)/Summe(P_A + P_B), einmal mit Kerndichte (Plan), einmal mit 5-Grad-Bins (Wortlaut) und einmal mit
  der Ladungs-Winkelverteilung.
- "Maxima" = Lage der Maxima der Kerndichte von AB in Grad.

| omega | d | v | Durchgaenge A / AB | weitere Klassen AB | Winkel AB (Grad; nur d = R ausgelesen) | r2 Plan | r2 5 Grad | r2 Ladung | Maxima AB (Grad); "periodisch" nach Plan |
|---|---|---|---|---|---|---|---|---|---|
| 0,8 | R | 0,2 | 3 / 6 | 35 reflektiert | -10,3 bis 10,3 | 0,057 | 0 | 0,024 | -10,5, 0, 10,5; ja (10,5) |
| 0,8 | R | 0,3 | 7 / 14 | 27 reflektiert | -23,2 bis 23,2 | 0,159 | 0 | 0,018 | -23, -15, 0, 15, 23; nein |
| 0,8 | R | 0,45 | 10 / 20 | 21 reflektiert | -25,5 bis 25,5 | 0,159 | 0,200 | 0,050 | -22,5, -8, 0, 8, 22,5; nein |
| 0,8 | 1,5R | 0,2 | 3 / 6 | 35 reflektiert | | 0,009 | 0 | 0,002 | -10, -2,5, 2,5, 10; ja (6,7) |
| 0,8 | 1,5R | 0,3 | 6 / 12 | 29 reflektiert | | 0,012 | 0 | 0,006 | -23, -14,5, -2, 14,5, 23; nein |
| 0,8 | 1,5R | 0,45 | 10 / 20 | 21 reflektiert | | 0,164 | 0,200 | 0,028 | -20,5, -4,5, 4,5, 20,5; ja (13,7) |
| 0,8 | 2R + 4/kappa | 0,2 | 3 / 6 | 35 reflektiert | | **0,000** | 0 | 0,000 | -15, 0, 15; ja (15) |
| 0,8 | 2R + 4/kappa | 0,3 | 5 / 10 | 31 reflektiert | | **0,000** | 0 | 0,000 | -21, 0, 21; ja (21) |
| 0,8 | 2R + 4/kappa | 0,45 | 7 / 14 | 27 reflektiert | | **0,000** | 0 | 0,002 | -17, -11, 0, 11, 17; nein |
| 0,9 | R | 0,2 | 0 / 0 | 41 reflektiert | | - | - | 0,067 | keine |
| 0,9 | R | 0,3 | 4 / 8 | 33 reflektiert | | 0,208 | 0,500 | 0,151 | -1,5; nein |
| 0,9 | R | 0,45 | 7 / 14 | 20 reflektiert, **7 zerflossen** | -14,1 bis 14,1 | 0,590 | 0,857 | 0,112 | -10, 10; nein |
| 0,9 | 1,5R | 0,2 | 0 / 0 | 41 reflektiert | | - | - | 0,048 | keine |
| 0,9 | 1,5R | 0,3 | 4 / 8 | 33 reflektiert | | 0,041 | 0,500 | 0,044 | 1,5; nein |
| 0,9 | 1,5R | 0,45 | 7 / 14 | 23 reflektiert, **4 zerflossen** | | 0,272 | 0,286 | 0,075 | -8,5, 8,5; nein |
| 0,9 | 2R + 4/kappa | 0,2 | 0 / 0 | 41 reflektiert | | - | - | 0,021 | keine |
| 0,9 | 2R + 4/kappa | 0,3 | 3 / 6 | 35 reflektiert | | **0,000** | 0 | 0,002 | 0; nein |
| 0,9 | 2R + 4/kappa | 0,45 | 5 / 10 | 31 reflektiert | | **0,000** | 0 | 0,004 | -7,5, 0, 7,5; ja (7,5) |

- **Lokalitaet [D]:** Beim fernen Abstand ist AB exakt die Summe von A und B (r2 = 0,000 in allen fuenf Zeilen mit
  Durchgaengen). Die V-Q1-Aussage gilt im Arm W also, und zwar bis auf Rundung. Bei d <= 1,5R weicht AB ab (r2 bis
  0,59): Der Ball beruehrt den Steg und spuert den zweiten Spalt geometrisch.
- **"Periodisch" ist hier ein Artefakt [D, M]:**
  - Bei 3 bis 10 Durchgaengen je Spalt erzeugt die Spiegelsymmetrie drei oder vier Maxima (-x, 0, +x). Die Planregel
    zaehlt das als "periodisch".
  - Keine (omega, d) mit d <= 1,5R ist bei allen drei v periodisch. Nach der V-Q2-Regel, beschreibend angewandt,
    ergibt sich "kein Muster".
  - Wo bei d = 1,5R zwei "Perioden" vorliegen (omega 0,8: 6,7 Grad bei v = 0,2 und 13,7 Grad bei v = 0,45), waechst
    die Periode mit v. Eine 1/(gamma v)-Skalierung verlangte das Gegenteil (Faktor 0,40).
- **Herkunft der Struktur [D]:** Der Winkel haengt glatt vom Stossparameter ab, wie bei einer Sammellinse (Bild
  BILD-W-histogramme.png, rechte Spalte).
  - Ein Ball, der unterhalb der Spaltmitte zielt, wird nach oben abgelenkt (die Wand stoesst ab), mit
    Umkehrpunkten an den Kanten ("Regenbogen").
  - Die aeusseren Maxima (+-20 bis 23 Grad bei omega = 0,8, v = 0,45) sind diese Umkehrwinkel, also Kaustiken der
    klassischen Ablenkung, keine Interferenzstreifen.
  - Bei v = 0,3 springt der Winkel im 41er-Raster von Stossparameter zu Stossparameter (12,9 / -6,6 / 4,0 / 0,9 /
    -3,6 Grad in 0,72-Schritten). Das 81er-Raster des Nachtrags N1 (omega 0,8, Spalt A) zeigt die Ursache:
    - In der Spaltmitte ist der Winkel glatt: 1,6 / 4,0 / 3,2 / 0,9 / -1,6 / -3,6 / -3,7 Grad fuer y = -6,09 bis
      -3,94 in 0,36-Schritten.
    - Die Spruenge sitzen an den Kanten: 12,9 / -22,0 / -6,6 Grad bei y = -7,16 / -6,80 / -6,44, und 10,3 / 22,6 Grad
      bei y = -3,22 / -2,86.
    - Der Ball streift dort die Backe; das ist empfindliche Kantenstreuung, keine periodische Struktur.
- **Teilung (V-Q4-Analogon, d = R, AB) [D]:**
  - 0 von 62 durchgelassenen Laeufen enden mit zwei durchgelassenen Stuecken >= 10 % Q.
  - Bei omega = 0,9 und v = 0,45 "zerfliesst" der Ball, wenn er den Steg trifft (7 von 41 Laeufen). Beispiel y_b = 0:
    13,7 % und 13,4 % der Ladung fliessen durch die beiden Spalte, 71 % bleiben zurueck. Am Laufende gibt es kein
    Stueck mit Kern (S >= 0,05 S0) mehr. Alle Teile liegen unter der Townes-Grenze 11,70 (Q = 15,8), wie in
    PLAN 2(d) vorab vermerkt.
  - Bei omega = 0,8 (Q = 38,5) bleibt der Ball ganz: Er geht durch einen Spalt oder prallt ab.

### 5e. I3 und kappa (Dreifachspalt) mit Rand-kappa des linearen Arms

**Kartenarm (w = R):** Kein Ball kommt durch, kappa nach Plan ist nicht definiert. Beschreibend [D] steht hier
kappa_L1 der **durchgesickerten Ladung** (Ladungs-Winkelverteilung, 2-Grad-Bins) gegen den linearen Arm. Bei v = 0,2
liegt die durchgesickerte Ladung bei 1e-5 bis 1e-4 von Q; die Werte sind dort Rauschen.

| omega | d | v = 0,2: Ball / linear | v = 0,3: Ball / linear | v = 0,45: Ball / linear |
|---|---|---|---|---|
| 0,8 | R | 0,040 / 0,082 | 0,153 / 0,108 | 0,111 / 0,118 |
| 0,8 | 1,5R | 0,085 / 0,109 | 0,237 / 0,199 | 0,102 / 0,084 |
| 0,9 | R | 0,198 / 0,278 | 0,181 / 0,123 | 0,175 / 0,208 |
| 0,9 | 1,5R | 0,311 / 0,306 | 0,348 / 0,238 | 0,182 / 0,185 |

- Bei v = 0,45 liegen Ball und linearer Arm innerhalb von 0,04. Die Sickerwelle des Balls verhaelt sich wie das lineare
  Paket; ein eigenes I3 der Nichtlinearitaet ist darin nicht zu erkennen.
- Lineares Paket, durchgelassene Ladung (Mittel ueber y, v = 0,45): Einzelspalt 1,0 bis 2,1 %, ABC 3,1 bis 6,0 %
  (l3-*.json). Auch der lineare Arm ist hier fast ganz reflektiert (unter der Grenzfrequenz).

**Arm W (w = 3R) [D]:** Ball mit Kerndichte (Plan-Groesse) gegen den linearen Arm (Ladung).
"Durchgaenge" in der Reihenfolge A, B, C, AB, BC, AC, ABC; C und BC sind gespiegelt.
Integrale in Laufanteilen; ein Lauf entspricht 1/41 = 0,024.

| omega | d | v | Durchgaenge | Integral abs(I3) | Integral delta | kappa_L1 Ball | kappa_int Ball | Rand-kappa (linear) | Differenz |
|---|---|---|---|---|---|---|---|---|---|
| 0,8 | R | 0,2 | 3, 3, 3, 6, 6, 6, 9 | 0,0007 | 0,027 | 0,024 | 0,000 | 0,207 | -0,183 |
| 0,8 | R | 0,3 | 5, 5, 5, 10, 10, 10, 15 | 0,0012 | 0,055 | 0,021 | 0,000 | 0,192 | -0,171 |
| 0,8 | R | 0,45 | 7, 7, 7, 14, 14, 14, 21 | 0,025 | 0,160 | 0,156 | 0,000 | 0,097 | +0,059 |
| 0,8 | 1,5R | 0,2 | 2, 3, 2, 5, 5, 4, 7 | 0,0001 | 0,004 | 0,019 | 0,000 | 0,164 | -0,145 |
| 0,8 | 1,5R | 0,3 | 5, 5, 5, 10, 10, 10, 15 | 0,0001 | 0,013 | 0,011 | 0,000 | 0,147 | -0,136 |
| 0,8 | 1,5R | 0,45 | 7, 7, 7, 14, 14, 14, 21 | 0,0036 | 0,072 | 0,049 | 0,000 | 0,120 | -0,071 |
| 0,9 | R | 0,2 | 0 (alle reflektiert) | - | - | - | - | 0,103 | - |
| 0,9 | R | 0,3 | 3, 3, 3, 6, 6, 6, 9 | 0,030 | 0,072 | 0,408 | 0,000 | 0,259 | +0,149 |
| 0,9 | R | 0,45 | 5, 5, 5, 11, 11, 10, 17 (+8 zerflossen in ABC) | 0,027 | 0,200 | 0,135 | 0,004 | 0,168 | -0,033 |
| 0,9 | 1,5R | 0,2 | 0 | - | - | - | - | 0,162 | - |
| 0,9 | 1,5R | 0,3 | 3, 3, 3, 6, 6, 6, 9 | 0,009 | 0,064 | 0,145 | 0,000 | 0,181 | -0,036 |
| 0,9 | 1,5R | 0,45 | 6, 5, 6, 10, 10, 12, 15 (+4 zerflossen) | 0,007 | 0,188 | 0,036 | 0,006 | 0,140 | -0,104 |

- **Die Durchgangszahlen sind fast exakt additiv** (ABC = A + B + C bei omega = 0,8 in allen sechs Zeilen; kappa_int
  = 0,000 bis 0,006). Ein Ball spuert also hoechstens zwei Spalte, wie in PLAN 2(e) als exakte Teilaussage hergeleitet.
- Winkelaufgeloest betraegt abs(I3) hoechstens 0,03, also etwa ein Lauf von 41. Die kappa_L1-Werte bis 0,41 kommen
  von kleinen Nennern (delta 0,004 bis 0,2) und sind nicht konvergiert: Ein Lauf mehr oder weniger verschiebt kappa
  um ~0,15.
- Die Differenz zum Rand-kappa wechselt das Vorzeichen (-0,18 bis +0,15). Ein Urteil gibt es fuer W nach Plan nicht;
  belastbar ist nur: kein grosses, systematisches I3.

### 5f. Nachtrag N1: Konvergenz-Stichprobe im Arm W (Doppelspalt, d = R; r2 nach Plan) [D]

| omega | v | r2, 41 y | r2, 81 y | Aenderung | r2, h = 0,125 (41 y) | Aenderung | Durchgaenge AB 41 / 81 / fein |
|---|---|---|---|---|---|---|---|
| 0,8 | 0,2 | 0,057 | 0,043 | 0,014 | - | - | 6 / 12 / - |
| 0,8 | 0,3 | 0,159 | 0,097 | **0,062** | - | - | 14 / 26 / - |
| 0,8 | 0,45 | 0,159 | 0,180 | **0,021** | 0,183 | **0,024** | 20 / 40 / 20 |
| 0,9 | 0,3 | 0,208 | 0,110 | **0,098** | - | - | 8 / 16 / - |
| 0,9 | 0,45 | 0,590 | 0,517 | **0,073** | 0,589 | 0,001 | 14 / 28 / 14 (+7 zerflossen auf beiden Gittern) |

- Durchgangszahlen und Klassen sind gitterfest (h = 0,125 gibt dieselben Zahlen) und verdoppeln sich mit 81 y.
- r2 aendert sich zwischen 41 und 81 Stossparametern in 4 von 5 Zeilen um mehr als 0,02. Nach der Konvergenzregel der
  Karte waeren diese Werte "unentschieden". Die Gitterverfeinerung aendert r2 um 0,001 bis 0,024.

### 5g. Energiebilanz (Pflicht d; vor den Laeufen, PLAN Abschn. 2d; lauf-69/bilanz.json) [E]

| omega | Q | E | min. Spaltkosten (x = 0,1) | Kosten x = 0,5 | E_kin v = 0,2 / 0,3 / 0,45 | Teilung in Stuecke >= 10 % erlaubt |
|---|---|---|---|---|---|---|
| 0,80 | 38,543 | 34,484 | 0,759 | 2,746 | 0,711 / 1,665 / 4,131 | nein / nur x <= 0,22 / ja |
| 0,90 | 15,819 | 15,576 | 0,138 | 0,243 | 0,321 / 0,752 / 1,866 | ja / ja / ja |

- Unter q = 11,70 (Townes-Grenze in 2D) gibt es keinen Ball, dort gilt E_min(q) = q. Zwei gebundene Stuecke (beide
  >= 11,70) sind nur bei omega = 0,8 und v = 0,45 energetisch moeglich.
- **V-Q4 war damit nicht vorab entschieden** (nur bei omega = 0,8 und v = 0,2 vorab ausgeschlossen).

## 6. Bedeutung fuer Finns Doppelspalt-Frage und das Q-Ball-Teilchenmodell [H]

- **Im Kartenaufbau stellt sich die Doppelspaltfrage fuer den klassischen Q-Ball gar nicht [E].** Ein Spalt, der
  schmaler ist als der Ball (w = R gegen Halbwertsdurchmesser 2R), wirft ihn bei v <= 0,45 vollstaendig zurueck.
  - Es gibt keine Ablenkstatistik, keine Teilung und keine Wiedervereinigung.
  - Nur bis 5 % der Ladung sickern als kleine Welle durch, bei v = 0,2 praktisch nichts.
  - Der lineare Kontrollarm mit gleicher Breite und gleicher Gruppengeschwindigkeit verhaelt sich ebenso: Mittel bei
    v = 0,45 hoechstens 2,1 % je Einzelspalt. Auch er liegt unter der Grenzfrequenz (k = gamma v ~ 0,5 gegen
    pi/w ~ 1,3 [M]).
- **Mechanismus [M, Schreibtisch, PLAN 2f]:** Um in den Spalt zu kommen, braucht jedes Ladungsquant mindestens die
  Grenzfrequenz des Spalts, sqrt(k_perp^2 + 0,5) ~ 1,15 bis 1,3. Der Ball hat je Ladung nur gamma E/Q ~ 0,9 bis 1,1.
  - Ob der Ball durchkommt, entscheidet also seine Groesse (innere Struktur) gegen die Spaltbreite, nicht seine
    de-Broglie-Laenge.
  - Fuer ein Quantenteilchen ist es umgekehrt: Die Materiewelle braucht nur lambda_dB < 2w. Elektronen und C60
    passieren Spalte, die viel breiter sind als sie selbst; der Q-Ball braucht einen Spalt, der breiter ist als er.
- **Zum Teilchenmodell [H]:**
  - Der klassische Q-Ball verhaelt sich an engen Spalten wie ein ausgedehntes klassisches Teilchen: Er prallt ab.
  - Das stuetzt die Weiche "Q-Baelle nur fuers Teilchenmodell". Interferenz muesste aus der quantisierten
    Schwerpunktbewegung kommen (Lesart R-lin im Dossier DOPPELSPALT-L), nicht aus dem klassischen Feld des Balls.
  - Ein Teilungsbild nach 1508.06837 braucht Spalte und Stege in Ballgroesse. Das passt zu Anstoss A4 (DMAX-LATTE):
    Fuer echte Doppelspaltversuche mit Spaltabstaenden >> Teilchengroesse ist es ausgeschlossen.
- **Mit passendem Spalt (Arm W, w = 3R) [D, H]:**
  - Der Ball geht als Ganzes durch einen Spalt, oder er prallt ab. Seine Ablenkung folgt glatt dem Stossparameter
    (Linse mit Regenbogenkanten).
  - Beim fernen Abstand ist die Statistik exakt additiv, beim nahen weicht sie geometrisch ab.
  - Eine mit v schrumpfende Streifenperiode zeigt sich nicht. Ein zweiter "Klick" (zwei Baelle) tritt nicht auf; beim
    leichten Ball (omega = 0,9) zerfliesst der Ball am Steg stattdessen.
  - Das ist das Verhalten eines klassischen ausgedehnten Teilchens mit kurzer Reichweite, nicht das einer Welle.
- **Zu Finns Suche nach Alternativen zum Doppelspalt [H]:**
  - Der klassische Q-Ball liefert keine Alternative. Ein Interferenzbild entsteht hier weder durch die innere Uhr
    noch durch Teilung.
  - Pruefbare Unterscheidungen liegen eher bei den Anstoessen A2 (I3 einer Pilotwelle) und A5 (amplitudenabhaengiges
    I3 im Fluss-Eis) des Dossiers DOPPELSPALT-L. Dort ist ein Fernmechanismus (Welle neben dem Teilchen) eingebaut,
    den der Q-Ball nicht hat.

## 7. Selbstanzeigen

1. **Rauchtests vor dem Plan:** Rauchtest 1 (Bilanz, Profil) und 2 (Zeitmessung, verkuerzte Wege) liefen mit echten
   omega, bevor PLAN.md stand; die Funktionslaeufe r2a3, r3 und r4 mit Fremdwerten (d = 2R, v = 0,4 bzw. 0,6, w = 3R in
   r4). Gesehen habe ich Klassen der Fremdlaeufe (r2a3 und r3 alles reflektiert; r4 mit w = 3R teils durchgelassen),
   Erhaltungswerte und Laufzeiten. Gesehen habe ich auch den Fahrtest omega = 0,9 (Ruhe-Pfad mit Fremdwert T = 10).
2. **Plan 2(f) und Zusatzarm W nach Sicht des Fremdlaufs r3:** Ich habe beides vor dem Einfrieren eingefuegt, vor
   jeder Rechnung mit Kartenwerten. Im Plan steht das offen (Selbstanzeige 4 dort). Fuer r4 (w = 3R, Fremdwerte) habe
   ich die Klassen gelesen, bevor ich eingefroren habe.
3. **Auf der .69 ausserhalb von kleintest.sh:**
   - einmal "python -c" (Versionsabfrage) vor dem Plan;
   - jq zum Lesen der Ergebnisse, cat, grep, sha256sum, mkdir, nvidia-smi;
   - nohup setsid zum Start der Laufskripte.
4. **Wartelogik:** Den Zusatzarm W und den Nachtrag N1 habe ich per "until grep ...; do sleep 5; done" an das Ende von
   Stufe 3 gebunden. Das ist kein Dienst und kein Hook. Ausserdem habe ich mit ssh-Warteschleifen auf Laufenden
   gewartet; das Werkzeug legt deren Ausgaben im Aufgabenordner der Sitzung ab (/tmp/claude-1000/.../tasks/). Selbst
   habe ich dort nichts geschrieben.
5. **Lokal:** date, ls, cat, grep, sed (Text, vor dem Einfrieren auch Code), head, tail, cp, mv, chmod, mkdir, rm (die
   leere API-Datei), sha256sum, file, du, curl (zwei arXiv-Abrufe; der erste, die API, kam leer zurueck), ssh/scp, jq
   (Lesen und Anzeige, siehe Punkt 14), bash -n. Kein python, awk oder perl. Kopfrechnungen sind mit [M] gekennzeichnet.
6. **Zwischenauswertung** zwischen1 (nach Stufe 2, eingefrorener Code): Ich habe die mechanischen Urteile und die
   I2-Werte der durchgesickerten Ladung gelesen, bevor Stufe 3 und W fertig waren. Plan und Code habe ich danach
   nicht geaendert.
7. **Lesarten des Plans, die die Karte nicht festlegt:**
   - d als Kantenabstand;
   - R = Halbwertsradius von |phi|^2;
   - Kerndichte sigma = 2 Grad, Klassenschwellen;
   - Wandkanten als tanh der Breite 0,25.
   Der Dreifachspalt lief nur fuer d <= 1,5 R (Karte: "7 Konfigurationen", Budget fuer alle d). Gerechnet habe ich
   5 Konfigurationen; C und BC kommen aus der Spiegelung y -> -y.
8. **Konvergenzlaeufe 2k und 3k entfallen** nach der Planregel (keine wertbare Kombination). Damit sind V-Q1 und V-Q3
   nicht "bestanden" und nicht "gescheitert", sondern unentschieden.
9. **Nachtrag N1** (Konvergenz-Stichprobe fuer W) habe ich um 06:09 CEST festgelegt, vor jedem W-Ergebnis. Er ist
   beschreibend und nicht eingefroren geplant; der Code ist der eingefrorene.
10. **Zwischenauswertung zwischen2** (nach W-Doppelspalt): Ich habe die W-Tabellen gelesen, bevor der W-Dreifachspalt
    und N1 fertig waren. Am Ablauf habe ich danach nichts geaendert.
11. **Die Planregel "periodisch" ist zu schwach:** Drei symmetrische Maxima aus wenigen Laeufen reichen ihr. Im
    Kartenarm hatte das keine Folge (leere Histogramme). Im Arm W melde ich die Flags, werte sie aber als Artefakt
    (Abschn. 5d).
12. **Bilder:** In der Spalte "Winkel gegen y_b" verbinden Linien auch Punkte ueber die Luecke zwischen den Spalten.
    Das ist nur Darstellung.
13. **Startzeiten:** Die Startzeiten in den kleintest-Logs enthalten das Warten auf den Lock. Die Zwischenauswertungen
    liefen deshalb jeweils zwischen zwei Laeufen.
14. **jq hat lokal auch kleine Rechnungen gemacht:** Rundung, Mittel ueber Laeufe (add/length), Energieverlust
    (E0 - E1)/E0, Max/Min und den Faktor 0,5 (Rasterweite der Kerndichte), der die Summen in Abschn. 5e zu Integralen
    macht. Das geht ueber "jq nur zum Lesen" hinaus. Die tragenden Groessen (r2, kappa, Klassen, Urteile) stammen aus
    lauf-69/auswertung.json (.69, eingefrorener Code).
15. **Bilder:** BILD-W-histogramme.png (= lauf-69/qds-bild-zusatz-w.png), BILD-karte-doppelspalt.png und
    BILD-karte-dreifach.png (leere Histogramme des Kartenarms). Alle hat der eingefrorene auswertung.py auf der .69
    erzeugt.
16. **Nicht erledigt:** keine Konvergenzpruefung im Kartenarm (gegenstandslos), kein Dreifachspalt bei d = 3R und
    2R + 4/kappa. Keine Peerbus-Nachricht, kein Journal, kein Commit.

## 8. Einfach gesagt

Wir haben unseren Feld-Klumpen (den Q-Ball) wie ein Elektron auf eine Wand mit zwei oder drei Schlitzen geschossen.
Sind die Schlitze schmaler als der Klumpen, wie die Karte es vorgab, prallt er in allen 4428 Versuchen ab; nur ein paar
Prozent seiner Ladung sickern als feine Welle durch. Deshalb liessen sich die vier Vorhersagen gar nicht pruefen. Mit
dreimal breiteren Schlitzen fliegt er durch genau einen Schlitz und wird an dessen Kanten abgelenkt wie eine Kugel von
einer Linse. Streifen, die mit seiner inneren Uhr wandern, oder eine Teilung in zwei Kugeln sehen wir nicht: Er benimmt
sich wie ein klassisches Teilchen mit Ausdehnung und nicht wie eine Welle, und das spricht dafuer, ihn nur als
Baustein fuer Teilchen zu verwenden.
