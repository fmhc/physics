# Runde 8, Karte SP-1: Stille Stellen fuer l > 0 (Ergebnis)

- Bearbeiter: Anthropic-Code-Agent (Opus). Explorativ, v3. Geschrieben ab 2026-09-30 07:55:03 CEST, letzter Stand
  2026-09-30 08:05:40 CEST (date).
- Code: RUNDE-07/bic2/bic2.py Version 3 (SHA-256 ee1ef6d2...). Pruefbelege in PRUEFBELEGE.md, Diff in bic2-v2-v3.diff.
- Modell: U = S - S^2 + 0,5 S^3, 3D, lineares radiales Problem mit abgeschnittenem Rand.
- Rechenort: alle 26 Laeufe auf der .69 (kleintest.sh, Spuren cpu und cpu2), alle rc = 0, jeder unter 430 s. Ausgaben
  in lauf-69/.
- "exakt" heisst hier immer: Umlaufzahl +-1 von W auf einem Rechteck um die Stelle, groesster Phasensprung < 0,4 rad.
  Das ist numerische Evidenz im Modell, kein Beweis.

## Kurzfassung

- **l = 1 hat bei omega*^2 = 0,754496 eine exakte Nullstelle der Abstrahlungsbreite.** Umlauf -1 auf beiden
  Rechtecken, aufgeloest, h = 0,01. Die Handschaetzung "Minimum nahe 0,7554" aus V6 lag 9e-4 zu hoch: Gamma(0,755) =
  2,3e-7 lag schon auf der steigenden Seite.
- **Darunter folgt fuer l = 1 eine Folge**, alle exakt (aufgeloest): 0,660280 (+1), 0,617105 (-1), 0,592242 (+1),
  0,576074 (-1). In 1/(omega^2 - 0,5) ist der Schritt konstant 2,30 (2,310 / 2,300 / 2,302 / 2,304). Ein Kandidat
  n = 6 bei ~0,5648 ist nicht verfeinert.
- **l = 2:** Der Ast liegt nur unterhalb von omega^2 ~ 0,675 im Einkanal-Fenster. Drei exakte Stellen: 0,643905 (+1),
  0,606981 (-1), 0,585391 (+1). Schritte 2,40 und 2,36. Die naechste Stelle nach der Schrittregel (0,571) ist nicht
  gesehen.
- Die Umlaufzahlen wechseln entlang jedes Astes das Vorzeichen, wie bei l = 0.
- Version 3 rechnet l = 0 bitgleich wie Version 2 (P0) und trifft die V6-Pole fuer l = 1 auf alle Stellen (P1).

## 1. Tabellen

u = 1/(omega*^2 - 0,5) [Hand, bc]. omega*^2 ist die Nullstelle von A_out (Phasentest in exakt, h = 0,01). Gegenproben
im selben Lauf: W-Fit und s(x) = 0.

### l = 1

| n | omega*^2 | rho* | u | Schritt | Umlauf (+-5e-4 / +-1e-4) | groesster Sprung (rad) | Belegstufe | Laeufe |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,7544960 | 1,826342 | 3,9293 | - | -1 / -1 | 0,299 / 0,296 | exakt (Umlauf) | sp1a2; sp1a (Rechteck neben der Stelle 0, neu gelegt -1) |
| 2 | 0,6602797 | 1,717301 | 6,2391 | 2,310 | +1 / +1 | 0,296 / 0,299 | exakt (Umlauf) | sp1d12; kurve b2 |
| 3 | 0,6171053 | 1,666050 | 8,5393 | 2,300 | -1 / -1 | 0,300 / 0,246 | exakt (Umlauf) | sp1d13; kurve b1 |
| 4 | 0,5922424 | 1,636295 | 10,8410 | 2,302 | +1 / +1 | 0,298 / 0,299 | exakt (Umlauf) | sp1d14r (--u-n 3000); sp1d14 (+1, Sprung 0,485); kurve b1 |
| 5 | 0,5760743 | 1,616829 | 13,1451 | 2,304 | -1 / -1 | 0,293 / 0,291 | exakt (Umlauf) | sp1d15 (--u-n 3000); kurve b6 (Minimum) |
| 6? | ~0,5648 (h = 0,02) | ~1,6034 | ~15,43 | ~2,29 | - | - | Kandidat: Feinverfahren nicht konvergiert, Gamma 3,6e-6 | kurve b5 |

- Gegenproben n = 1 bis 4: A_out-Nullstelle, W-Fit und s(x) = 0 liegen je innerhalb 2,3e-6 beisammen. Bei n = 5 liegt
  der W-Fit 1,1e-5 daneben (cond J 9,9e3, Fitrest 1,1e-3); A_out und s(x) = 0 stimmen auf 1e-6.
- d_min/|A'| (naechster Abstand der A_out-Kurve zum Ursprung, in omega^2): 4,7e-11 / 2,2e-11 / 5,2e-12 / 1,2e-11 /
  2,8e-10 fuer n = 1 bis 5.
- Stufen: kurve (h = 0,02) gegen exakt (h = 0,01) weichen um 8e-9 (n = 2), 1,8e-7 (n = 3), 7,7e-7 (n = 4) und 5e-6
  (n = 5) ab. Der Rauchtest bei h = 0,08 fand n = 1 bei 0,754496, also dieselbe Lage.
- Oberhalb von n = 1 (kurve b3 und b4, 0,68 bis 0,83) bleibt s ohne Wechsel: positiv unter 0,7545, negativ darueber.
  Ab 0,85 liegt der l = 1-Ast nicht mehr im Fenster. Dort ist keine weitere Stelle gesehen.
- n = 5 im Grobraster: Das Vorzeichen von s ist dort unzuverlaessig, weil |s| < 1e-4 unter dem Interpolationsfehler der
  400-Punkte-Abtastung liegt. Die Scheinwechsel bei 0,5742 und 0,5753 (kurve b6) kommen daher. Belastbar waren die
  Breiten (1,3e-3 / 3,4e-4 / 1,6e-6 / 2,4e-4 / 9,7e-4 bei 0,574 bis 0,578). exakt hat die Stelle dann bestaetigt.
- n = 6: Der Kandidat liegt dort, wo die Schrittregel die naechste Stelle erwartet (0,56474). Er war nicht vorhergesagt
  und nicht mit exakt gerechnet. Im Duennwandbereich springt die Astverfolgung (Gamma 7e-3 bei 0,57).

### l = 2

| k (von oben) | omega*^2 | rho* | u | Schritt | Umlauf (+-5e-4 / +-1e-4) | groesster Sprung (rad) | Belegstufe | Laeufe |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,6439055 | 1,762082 | 6,9490 | - | +1 / +1 | 0,274 / 0,299 | exakt (Umlauf) | sp1d20 (--u-n 3000); kurve c12 |
| 2 | 0,6069811 | 1,694040 | 9,3474 | 2,398 | -1 / -1 | 0,282 / 0,284 | exakt (Umlauf) | sp1d22r (--u-n 3000); sp1d22 (-1, Sprung 0,430); kurve c1 |
| 3 | 0,5853911 | 1,655298 | 11,7108 | 2,363 | +1 / +1 | 0,290 / 0,298 | exakt (Umlauf) | sp1d21r (--u-n 3000); sp1d21 (+1, Sprung 1,42); kurve c1 |
| 4? | Schrittregel: 0,571 | - | ~14,07 | - | - | - | nicht gesehen | kurve c0 |

- Existenz im Fenster (1 - omega, 1 + omega): Kandidaten (Nullstellen von L(y_b)) gibt es fuer l = 2 bei 0,55 bis 0,67,
  keine bei 0,68 bis 0,95 (kurve c2, c3, c4). Der Ast liegt dort also ueber 1 + omega, mit zwei offenen Kanaelen; eine
  Einkanal-Nullstelle gibt es dann nicht.
- Unter 0,58 (kurve c0, Abstand 0,002): kein Vorzeichenwechsel gesehen. s ist bei 0,570 fast null (-2,5e-5), die
  Nachbarn bei 0,568 und 0,572 liegen bei -2,3e-3 und -3,4e-3. Die Breite dort ist 4,5e-4, also kein stilles Minimum.
  Die Breiten springen im Duennwandbereich zwischen 2e-4 und 7e-3; die Astverfolgung ist dort unsicher.
- Die Luecke zwischen den Laeufen c1 (bis 0,64) und c2 (ab 0,65) hat erst der Lauf c12 geschlossen. kurve erkennt keinen
  Wechsel ueber die Grenze zweier Laeufe; die uebrigen Grenzen (l = 1: 0,625/0,63 und 0,675/0,68) habe ich von Hand
  geprueft, dort wechselt s nicht.

### Vergleich mit l = 0 (beta = 0,5, RUNDE-07 BIC-2)

| n | u(l = 0) | u(l = 1) | u(l = 1) - u(l = 0) | u(l = 2) | u(l = 2) - u(l = 1) |
|---|---|---|---|---|---|
| 1 | 3,359 | 3,929 | 0,570 | - (Ast nicht im Fenster) | - |
| 2 | 5,402 | 6,239 | 0,837 | 6,949 | 0,710 |
| 3 | 7,608 | 8,539 | 0,931 | 9,347 | 0,808 |
| 4 | 9,860 | 10,841 | 0,981 | 11,711 | 0,870 |
| 5 | 12,133 | 13,145 | 1,012 | - | - |

- Die Zuordnung von l = 2 zu n = 2 bis 4 ist eine Hypothese **[H]**: Die l = 2-Stelle liegt jeweils knapp ueber der
  l = 1-Stelle mit gleichem n. Eine l = 2-Stelle zu n = 1 laege bei u ~ 4,6 (omega^2 ~ 0,72). Dort ist der Ast nicht im
  Fenster.
- Muster **[H, Hand]**:
  - Der Schritt ist fuer alle drei l etwa gleich: l = 0 naehert sich 2,28, l = 1 hat 2,30 von Anfang an, l = 2 hat
    2,36 bis 2,40.
  - Der Versatz zwischen benachbarten l waechst mit n; bei l = 1 gegen l = 0 von 0,57 auf 1,01. Ein halber Schritt
    waere 1,15.
  - Das passt zum Formfaktor-Bild mit der Phase l pi/2 der Kugelwellen, ist aber nur eine Deutung.

## 2. Erwartung gegen Ausgang (PLAN.md, vor dem Rechnen, und Nachtraege dort)

| Punkt | vorab | Ausgang | Wertung |
|---|---|---|---|
| E1 Umlauf +-1 bei l = 1 um 0,755 (85 %) | +-1, aufgeloest | -1 / -1, aufgeloest | getroffen |
| E1 Lage | 0,7557 +- 0,0003 | 0,754496 | verfehlt (1,2e-3 daneben; meine Hochrechnung aus V6 hatte denselben Fehler wie die Handschaetzung) |
| E1 Vorzeichen -1 (55 %) | -1 | -1 | getroffen (fast Muenzwurf) |
| E2 n = 2 | u = 6,0 +- 0,4; x 0,661 bis 0,672 | u = 6,239; x = 0,66028 | in u getroffen. Das x-Fenster war falsch umgerechnet (richtig 0,656 bis 0,679); nach dem geschriebenen x-Fenster 7e-4 daneben |
| E2 n = 3 | u = 8,2 +- 0,6; x 0,615 bis 0,630 | 8,539; 0,61711 | getroffen |
| E2 n = 4 | u = 10,5 +- 0,8; x 0,589 bis 0,603 | 10,841; 0,59224 | getroffen |
| E2 Vorzeichen wechseln | ja | -1, +1, -1, +1, -1 | getroffen |
| E2 mindestens zwei Wechsel in 0,58 bis 0,75 (70 %) | ja | drei | getroffen |
| E3 x_c fuer l = 2 | ~0,70 (0,62 bis 0,80) | ~0,675 (letzter Kandidat 0,67, keiner ab 0,68) | getroffen |
| E3 Stellen l = 2 | 0,645 / 0,610 / 0,590, je +- 0,01 | 0,6439 / 0,6070 / 0,5854 | getroffen |
| E3 mindestens ein Wechsel (60 %), keiner ueber 0,80 (80 %) | ja / ja | drei / keiner | getroffen |
| E4 P1 | Re auf 1e-7, Gamma auf 1 % | Re gleich auf alle Stellen, Im auf 3e-17 | getroffen |
| E5 P0 | bitgleich | Bericht und JSON bitgleich (ohne Zeiten) | getroffen |
| Nachtrag 07:14:50, l = 1 n = 5 | 0,57609 +- 0,0003, Umlauf -1; scheitert bei keinem Wechsel in 0,565 bis 0,585 "oder einer ausserhalb 0,5758 bis 0,5764" | 0,576074, Umlauf -1 (aufgeloest); im Grobraster aber weitere Wechsel bei 0,5666 (b5), 0,5742 und 0,5753 (b6) | gemischt: Lage und Umlauf getroffen. Die geschriebene Scheiterbedingung ist nach Wortlaut erfuellt. Dass diese Wechsel Interpolationsfehler bzw. der Kandidat n = 6 sind, ist nach dem Ausgang gedeutet; ich zaehle den Punkt darum nicht als Treffer |
| Nachtrag 07:26:25, l = 2 Umlauf | +1 bei 0,5854, -1 bei 0,6070 | +1 und -1, beide aufgeloest (--u-n 3000) | getroffen |
| Nachtrag 07:26:25, naechste Stelle darueber | 0,6427 +- 0,002 | 0,643905 | getroffen |
| Nachtrag 07:26:25, danach | 0,714 +- 0,01 | Ast dort nicht im Fenster | verfehlt (die eigene Schwelle x_c aus E3 nicht beachtet) |
| Nachtrag 07:26:25, bei 0,571 | Paar oder keiner | keiner gesehen | eine der zwei erlaubten Moeglichkeiten; schwacher Test |

- Die Nachtraege lagen nach den ersten Ergebnissen. Sie sind Fortschreibungen der gefundenen Schrittregel, keine
  unabhaengigen Vorhersagen.

## 3. Latten

- **L1 (kann scheitern):** Die E1-Lage ist gescheitert. Der Rest haette scheitern koennen (Umlauf 0, andere Schritte).
- **L2 (Gegenprobe):**
  - Das erste Rechteck von sp1a lag neben der Stelle (0,75515 bis 0,75565). Es gab 0,0000, aufgeloest. Das ist eine
    echte Negativkontrolle.
  - Drei Wege zur Lage (A_out, W-Fit, s(x)) stimmen fuer l = 1, n = 1 bis 4 je auf <= 2,3e-6 ueberein. Wo der W-Fit
    schlechter ist (l = 1, n = 5: 1,1e-5; l = 2 bei 0,5854: 7,7e-6; Fitrest 1e-3 bis 6e-3), stimmen A_out und s(x) auf
    1e-6.
  - Gamma_Fluss = Gamma_Newton auf 4 bis 5 Stellen.
- **L3 (Numerik):**
  - h = 0,02 gegen h = 0,01: Lagen auf <= 5e-6 gleich.
  - Die nicht aufgeloesten Umlaeufe lagen an zu grober Abtastung der rho-Seiten, nicht an den x-Seiten: W dreht dort
    auf weniger als 1e-7 in rho, weil J stark anisotrop ist (cond J 2,5e3 bis 1e4). Mit --u-n 3000 (nur Argument, kein
    Code) sind alle aufgeloest: l = 1 bei 0,5922 (vorher 0,485 rad), l = 2 bei 0,6070 (0,430) und 0,5854 (1,42). Die
    Umlaufzahl blieb dabei jedes Mal gleich.
- **L4 (schon bekannt):** BICs durch Parameterabstimmung (Hsu u. a. 2016) laut L4-BIC-LITERATUR.md. Fuer innere
  l > 0-Moden von Q-Baellen kenne ich keine Arbeit **[L?, nicht gesucht]**.
- **L5 (Messbezug):** keiner. Spielzeug-Q-Ball.

## 4. Grenzen

- Alles ist linear. Ob eine nichtlineare Anregung an einer l = 1-Stelle lange lebt, ist nicht gerechnet. Fuer l = 0
  fand Codex nichtlineare Abstrahlung in der zweiten Harmonischen mit Fluss ~ epsilon^4.
- Die Stellen gelten fuer den radialen Kanal zu festem l. Wegen der Kugelsymmetrie gilt eine l = 1-Stelle fuer
  m = -1, 0, +1 zugleich. Ein langlebiger ganzzahliger innerer Drehimpuls (m = +-1) ist damit moeglich, aber eine
  Hypothese **[H]**. Spin 1/2 ist es nicht.
- Unter omega^2 ~ 0,58 (Duennwand) ist die Astverfolgung unsicher. Die Grobraster-Vorzeichen von s sind dort bei
  |s| < 1e-4 nicht belastbar.
- Nicht gerechnet: l = 1 zwischen 0,83 und 0,85 (dort verlaesst der Ast das Fenster), l >= 3, andere beta, n = 6.
- Berichtigung zum Codekopf von Version 3: Der Potenzfaktor im "Kernwachstum" ist etwa (r_m/h)^l r_m/(l+1), nicht
  (r_m/h)^(l+1). Beispiel l = 1, r_m = 2,7, h = 0,01: gemeldet 4,9e2. Der Satz im Codekopf ist zu grob; am Rechenweg
  aendert das nichts.
- Werkzeug: Fuer l > 0 sollte exakt kuenftig --u-n 3000 als Vorgabe nehmen. Das habe ich nicht eingebaut, um den
  l = 0-Rechenweg nicht zu aendern.

## 5. Laeufe (.69, Zeiten UTC aus den Berichten; Logs lauf-69/KETTE-SP1-*.log, Skripte sp1/kette-sp1-*.sh)

| Lauf | Zweck | Start | Ende, Dauer |
|---|---|---|---|
| p0 | P0, l = 0 gegen aus-kurve-050-dicht | 04:54:19 | 04:56:39, 141 s |
| b2 | l = 1 kurve 0,63 bis 0,675 | 04:52:22 | 04:56:27, 245 s |
| b1 | l = 1 kurve 0,58 bis 0,625 | 04:56:31 | 05:02:20, 349 s |
| a | l = 1 exakt um 0,75565 | 04:59:18 | 05:06:24, 426 s |
| d12 | l = 1 exakt n = 2 | 05:06:27 | 05:12:05, 338 s |
| b3 | l = 1 kurve 0,68 bis 0,75 | 05:06:38 | 05:08:50, 131 s |
| a2 | l = 1 exakt n = 1, zentriert | 05:08:55 | 05:14:34, 339 s |
| p1 | P1, l = 1 kurve 0,72 / 0,75 | 05:12:08 | 05:13:28, 79 s |
| d13 | l = 1 exakt n = 3 | 05:13:30 | 05:19:23, 353 s |
| c1 | l = 2 kurve 0,55 bis 0,64 | 05:18:35 | 05:25:16, 401 s |
| c3 | l = 2 kurve 0,75 bis 0,84 | 05:23:43 | 05:26:27, 165 s |
| b5 | l = 1 kurve 0,565 bis 0,585 | 05:25:19 | 05:28:44, 205 s |
| d14 | l = 1 exakt n = 4 | 05:26:30 | 05:32:56, 386 s |
| c2 | l = 2 kurve 0,65 bis 0,74 | 05:32:48 | 05:35:29, 161 s |
| c4 | l = 2 kurve 0,85 bis 0,95 | 05:32:59 | 05:37:01, 242 s |
| d22 | l = 2 exakt 0,60698 | 05:35:32 | 05:41:42, 370 s |
| d21 | l = 2 exakt 0,58539 | 05:37:07 | 05:44:02, 415 s |
| b6 | l = 1 kurve 0,574 bis 0,579 | 05:41:45 | 05:47:04, 318 s |
| c0 | l = 2 kurve 0,562 bis 0,58 | 05:44:07 | 05:47:13, 186 s |
| b4 | l = 1 kurve 0,77 bis 0,95 | 05:47:07 | 05:50:44, 217 s |
| d21r | l = 2 exakt 0,58539, --u-n 3000 | 05:47:16 | 05:53:20, 364 s |
| c12 | l = 2 kurve 0,635 bis 0,655 | 05:50:46 | 05:53:31, 165 s |
| d14r | l = 1 exakt n = 4, --u-n 3000 | 05:53:23 | 05:58:45, 322 s |
| d22r | l = 2 exakt 0,60698, --u-n 3000 | 05:53:34 | 05:58:31, 297 s |
| d15 | l = 1 exakt n = 5, --u-n 3000 | 05:58:34 | 06:05:17, 403 s |
| d20 | l = 2 exakt 0,64391, --u-n 3000 | 05:58:49 | 06:03:35, 286 s |

- Lokal nur Rauchtests (CPU, 1 Thread, nice 19, timeout 120): lauf-lokal/, siehe PRUEFBELEGE.md.
