# Y-2 (Runde 11): Quartik je Kanal mit nachgestimmtem U, Y-Knoten oder nicht? Plan und Vorab

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3). **Andere Theorie als die
  Gesamtformel** (+ c sum_a |psi_a|^4 mit b_0 statt 1, bzw. Rabi-Term). Alles [H]: Vorbild, kein Proton, kein QCD.
- Zeiten (date, CEST): Beginn 12:34:36; y2.py kopiert 12:41:52; dieser Plan ab 12:47:01, vor jedem Rauchtest und jedem
  Lauf. Kopie PLAN.md.eingefroren-<Zeit> mit sha256 vor dem ersten Lauf.
- Grundlage: RUNDE-10/alt1/ALT-1.md Abschnitte 0, 1, 5 (ganz gelesen), A4; RUNDE-10/y1/PLAN.md, ERGEBNIS.md, y1.py.
- Belegstufen: [Hand], [num], [H], [nachtr.] wie Y-1.

## 1. Vorschlag aus ALT-1, woertlich (Fundstelle RUNDE-10/alt1/ALT-1.md, Zeilen 224 bis 244)

Zeilen 224 bis 231 (Arme, Geometrien, Umfang):

```
- **Arme** (g = 0,5, Q = 3600, dx 0,3, 12000 Iterationen, Schwerpunktbindung wie Y-1):
  - B (Hauptarm): c = 2, b_0 = 1 + c/3 = 1,6667 (gemischter Ball b = 1,1667 wie Y-1). Vorab-Probe: b_eff(N = 1) = -0,33
    (kein Einzelball), b_eff(zwei Fuellkomponenten) = 0,79, Vakuum stabil (1 - b^2/2 = 0,32 > 0).
  - A (Vergleich): c = 1, b_0 = 1 (b = 0,833). Nach A4 Gleichstand; zeigt, ob das Nachstimmen noetig ist.
  - C (Literatur-Wandtyp): epsilon = 0,3, c = 0, b_0 = 1 (unter der Vakuumschranke 0,32).
  - Geometrien je Arm: gleichseitig 9, gleichseitig 12, kollinear 8, Meson d = 6 / 9 / 12; Saat neutral und Y.
  - Umfang: 3 Arme x 6 Laeufe x 2 Saaten = 36 Laeufe, gebuendelt wie Y-1 (Stapel je Arm); nach Y-1 (225 s je Stapel von
    12) etwa 30 bis 45 min P4000 gesamt.
```

Zeilen 232 bis 237 (Vorab-Erwartungen, bindend):

```
- **Vorab-Erwartungen fuer Arm B** (binden, bevor gerechnet wird): (i) keine Gegenwirbel (eigene Windung um jeden Wirbel
  bei r = 2,5 und 4,5 gleich 1) in >= 4 von 5 Nicht-Meson-Laeufen; (ii) Kopplungsdefizit-Rippe innerhalb 1,5 der
  Steiner-Arme, Knoten (arg-P-Windung 2) innerhalb 1,5 von J; (iii) E(gleich 12) - E(gleich 9) = 3 bis 5 (2 sigma_W bis
  2 sigma_Rand mal 5,2); (iv) Meson linear bis 12 mit Steigung 0,6 bis 1,0; (v) E(kollinear 8) - E(gleich 9) < 1
  (Y: +0,3; Dreieck: +2,0 bei sigma = 0,82). Fuer Arm A: (i) verfehlt in >= 2 von 5. Fuer Arm C: eine Rippe je Arm statt
  zwei.
```

Zeilen 238 bis 244 (Scheiterregel, Wortlaut gilt):

```
- **Scheiterregel (vorab, Wortlaut gilt):**
  - "Quartik traegt das Y nicht": Arm B zeigt Gegenwirbel in >= 2 der 3 Dreier-Geometrien **oder** das Meson ist flach
    (Steigung 9 -> 12 < 0,3 x Steigung 6 -> 9).
  - "Dreieck": keine Gegenwirbel, aber Rippe an den Kantenmitten (n_a/S < 0,1 an >= 2 Kantenmitten) und nicht auf den
    Armen. Kein Scheitern, anderes Vorbild.
  - "Y": (i), (ii) erfuellt und (iii) innerhalb 3 bis 5. Alles andere: "weder noch", wie Y-1.
  - Nicht auswertbar: dE1000 > 0,02 oder Schub > 30 (Ball weggeglitten) in einem der drei Dreier.
```

Dazu ALT-1 Zeile 39 (Abschnitt 0, Punkt 4): "g = 0,5, weiter Ring r < 4". Code-Aenderungen: ALT-1 Zeilen 216 bis 223.

## 2. Vorab-Probe (ALT-1 Zeilen 225/226 und A4 Zeilen 608 bis 611), per Hand nachgerechnet [Hand]

U_eff/S fuer eine Zusammensetzung x_a = n_a/S: m - b_eff S + S^2/2 mit b_eff = b_0 + g C/S^2 - c sum x_a^2; wegen
C/S^2 <= (1 - sum x^2)/2 und g, c >= 0 ist b_eff am groessten bei gleichphasiger Gleichverteilung (sum x^2 = 1/3):
b = b_0 + g/3 - c/3. Vakuum stabil, wenn m - b^2/2 > 0.

| Arm | c | b_0 | eps | b (N = 3, gemischt) | b_eff(N = 1) = b_0 - c | b_eff(zwei Fuellkomp.) = b_0 + g/4 - c/2 | m = 1 - eps | m - b^2/2 |
|---|---|---|---|---|---|---|---|---|
| B | 2 | 1,66667 | 0 | 1,16667 | -0,33333 (kein Einzelball) | 0,79167 | 1 | 0,31944 > 0 |
| A | 1 | 1 | 0 | 0,83333 | 0 (Grenzfall, kein Einzelball) | 0,625 | 1 | 0,65278 > 0 |
| C | 0 | 1 | 0,3 | 1,16667 | 1 | 1,125 | 0,7 | 0,01944 > 0 (knapp) |

Stimmt mit ALT-1 ueberein (-0,33; 0,79; 0,32; Schranke 0,319 - eps). Im Code: b_von(k) = b_0 + g (N-1)/(2N) - c/N,
m_von(k) = 1 - eps (N-1)/2; die Ausgabe druckt b und m des Balls.

## 3. Zusaetze Code-Agent (nicht in ALT-1; vor jedem Lauf festgelegt)

- **Zusatz Code-Agent Z1, Ladung in Arm C: Q_C = 1142,5 statt 3600.** Grund [Hand]: Mit eps = 0,3 liegt der Ball dicht an
  der Vakuumschranke (m - b^2/2 = 0,019). Duennwand: omega^2 = 0,019 + sigma/(R S_0) mit sigma ~ 0,75 (aus Y-1: omega^2 =
  0,341 bei R = 29) ergibt bei Q = 3600 R ~ 50 > L = 38,4 (Kasten, periodisch). Dann fuellt der Ball den Kasten, und eine
  Netto-Windung je Komponente waere auf dem Torus nicht moeglich; Gegenwirbel waeren erzwungen. Exakte Abbildung: das
  radiale Profil haengt nur von b und omega^2 - m ab. Mit omega_B = 0,57758 (Y-1 dreier_y_bericht, Ball b = 1,1667,
  Q = 3600) gilt omega_C^2 = omega_B^2 - 0,3 = 0,033599, Q_C = 3600 omega_C/omega_B = 1142,49. Pruefung im Lauf: Ball in
  Arm C hat S_0 und R_halb wie Arm B (Soll 1,1786 und 29,03, auf 1e-3).
- **Zusatz Code-Agent Z2, Meson-Klammer.** Beide Mesonwirbel sind in psi_1; bei d = 6 ueberlappen Ringe r < 4 (4 + 4 > 6)
  und die Klammer waere widerspruechlich. Hauptreihe: Ring r < min(4, d/2 - 0,5), also d = 6: r < 2,5; d = 9, 12: r < 4.
  Kontrollreihe im selben Stapel: d = 6/9/12 mit einheitlichem Ring r < 2 (wie Y-1 meson/mesonc). Scheiterregel "Meson
  flach" und (iv) werden auf der **Hauptreihe** ausgewertet; die Kontrollreihe wird nur berichtet.
- **Zusatz Code-Agent Z3, Ableitbarkeitsprobe zu (i):** Mit Ring r < 4 ist die Windung bei r = 2,5 durch die Klammer
  erzwungen (Phase der eigenen Komponente im Ring fest). Der Teil "r = 2,5" von (i) kann also nicht scheitern; tragend
  ist nur r = 4,5. Ich werte nach Wortlaut (beide Radien) aus und vermerke das. Ebenso: Nicht-Meson-Laeufe sind 3
  Geometrien x 2 Saaten = **6**, nicht 5. Lesart (bindend): Anteil, also (i) getroffen bei >= 0,8 der Laeufe (>= 5 von
  6); Arm A "(i) verfehlt in >= 2 von 5" bei Anteil >= 0,4 (>= 3 von 6). Die Zaehl-Lesart (>= 4 bzw. >= 2) berichte ich
  daneben.
- **Zusatz Code-Agent Z4, Operationalisierung (ii) und Arm C:**
  - Kopplungsdefizit D = g ((N-1)/(2N) S^2 - C) + eps ((N-1) S/2 - R), R = sum_{a<b} Re(psi_a^* psi_b) (in A und B nur der
    g-Teil wie Y-1; in C beide Kopplungen).
  - Querschnitt senkrecht zum Steiner-Arm bei 0,35 / 0,5 / 0,65 der Armlaenge, t von -4 bis 4 (Schritt 0,25). Rippe = lokales
    Maximum von D mit |t| <= 1,5 und Hoehe >= D_W = 0,25 g S_0^2/12 (ein Viertel der Spitze einer idealen W-Wand).
  - Arm "mit Rippe": Rippe an >= 2 der 3 Querschnitte. Arme mit Laenge < 1 (kollinear: B selbst) zaehlen nicht.
  - (ii) erfuellt: in **allen drei** Dreier-Geometrien (beste Saat) tragen alle Arme eine Rippe **und** die Umlaufwindung
    von P = sum psi_a^2 auf dem Kreis r = 1,5 um J ist 2 (+- 0,1).
  - Arm C "eine Rippe je Arm statt zwei": in der Armmitte (0,5) genau eine Rippe an >= 2/3 aller Arme der drei Geometrien
    (beste Saat).
- **Zusatz Code-Agent Z5, Scheiterregel je Arm und Reihenfolge.** ALT-1 formuliert die Regel fuer Arm B; ich wende denselben
  Wortlaut auf A und C an (Arm-Name ersetzt). Beste Saat je Geometrie = kleinste E unter den Saaten mit dE1000 <= 0,02
  und Schub <= 30 (sonst kleinste E). "Gegenwirbel in einer Geometrie" = bei der besten Saat. Treffen mehrere Ausgaenge
  zu, gilt die Reihenfolge: nicht auswertbar > "Quartik traegt das Y nicht" > "Dreieck" > "Y" > "weder noch"; alle
  zutreffenden werden genannt. "Dreieck": Kantenmitten-Bedingung in beiden gleichseitigen Geometrien (kollinear: Kanten =
  Arme) und dort hoechstens ein Arm mit Rippe; "keine Gegenwirbel" = in keiner der drei Geometrien.
- **Zusatz Code-Agent Z6, (iv) "linear bis 12 mit Steigung 0,6 bis 1,0":** beide Abschnittssteigungen 6 -> 9 und 9 -> 12
  der Hauptreihe in [0,6; 1,0].
- **Zusatz Code-Agent Z7, Reproduktionskontrolle:** im Stapel von Arm A zusaetzlich gleichseitig 9, Y-Saat, c = 0, b_0 = 1,
  eps = 0, Ring r < 4 (= Y-1 dreier_k4 g+0.5_gleich9_Y_k4, E = 2166,6778595004525). Soll: relativ <= 1e-9.
- **Zusatz Code-Agent Z8, Residuum:** Die Diagnose res_frei hat denselben Ausdruck wie die Kraft; ich aendere ihn mit
  (vierte Stelle neben den drei aus ALT-1), sonst waere das Residuum in B und C falsch. Keine Wirkung auf den Fluss.
- Kein Gitterfeinlauf: ALT-1 verlangt keinen. Die Gitterunsicherheit der Energiedifferenzen aus Y-1 (+-0,6 bei dx 0,3)
  gilt auch hier und wird bei (iii) und (v) genannt.

## 4. Code (y2.py = Kopie von RUNDE-10/y1/y1.py)

- y1.py sha256 d04cdfd861c1192888ba9829485fa8198c7289a4e28c04749eb7cffac8d1e986 (unveraendert). y2.py: Hash in 8.
- Aenderungen (Zeilen in y1.py -> y2.py, aus diff):
  - Kopf 2 -> 2..8 (Beschreibung).
  - ALT-1 Punkt 1, b_0 an drei Stellen: upot 100/101 -> 106/107 (Parameter m dazu, Vorgabe 1); Flussgleichung 2120 ->
    2141/2142 ("1.0 + S*(1.5*S - 2.0*b0k)"); energie() 2097 -> 2115 (upot mit b_0); b_von 2003 -> 2010..2019 (b_0 statt 1;
    neu m_von, ball_key); b0k-Tensor 2077 -> 2093..2095.
  - ALT-1 Punkt 2, eps: energie() 2102/2106/2107 -> 2121..2123/2127/2128 (- eps R, R = (|Psi|^2 - S)/2); Kraft 2120 ->
    2141/2142 (- (eps/2)(Psi - psi)); radialer Ball mit Massenterm m: Radial.energie 134/140 -> 140/146, loesen 153/169/
    176/177/184/185 -> 160/176/183/184/191/192, Ausgabe 200 -> 207, residuum 211/213 -> 218/220; Ball-Schluessel (b, m)
    2019/2021/2022/2031/2159 -> 2035/2037/2038/2047/2183.
  - Zusatz: Residuum 2147 -> 2170/2171 (Z8); Ring je Konfiguration 2059 -> 2075 (Z2); Rl 2143 -> 2166; Defizit D und
    Rippen 2162 -> 2187..2193 und 2242 -> 2274..2279 (Z4); Windung r = 2,5 2200 -> 2231 (Z3); Ausgabefelder 2275..2277 ->
    2312..2316; Bild zeigt D 2332 -> 2375 (Titel); Berichtszeilen 2288/2296/2297 -> 2327/2328/2336..2340; Arme, Stapel
    und Auswertung 2352 -> 2396..2522 (Y2_ARME, y2_konf, y2_auswertung); Unterbefehle y2b/y2a/y2c 2387 -> 2558..2565;
    Registrierung 2616/2619 -> 2794/2795/2799.
- Unveraendert: Loeser (halbimplizit, tau 0,5, 12000 Iterationen), Klammer, Schwerpunktbindung, Saaten, alle
  Y-1-Diagnosen, Q = 3600 (A, B), dx 0,3, L 38,4.

## 5. Stapel und Aufrufe

- Je Arm ein Stapel von 12 Konfigurationen (Arm A: 13 mit Z7), g = 0,5, Ring r < 4:
  - Dreier: gleichseitig 9, gleichseitig 12, kollinear 8, je Saat neutral und Y (6)
  - Meson Hauptreihe d = 6 (r < 2,5), 9, 12 (r < 4) (3); Kontrollreihe d = 6/9/12 mit r < 2 (3)
- Aufrufe auf der .69 (Ordner /home/fmh/fmhc-physics-remote/runde11-y2/, y2.py per neue Datei + mv):
  - LAUF1: `cd /home/fmh/fmhc-physics-remote/runde11-y2 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a y2b y2.py y2b --out ausgabe --budget 500 | tee /home/fmh/fmhc-physics-remote/runde11-y2/LAUF1-y2b.log`
  - LAUF2: dasselbe mit p4000b, y2a, LAUF2-y2a.log
  - LAUF3: p4000a (nach LAUF1) bzw. die zuerst freie Spur, y2c, LAUF3-y2c.log
  - LAUF4: y2auswertung (nur gespeicherte Zahlen) auf p4000a, LAUF4-y2auswertung.log
- Budget: Y-1 dreier_k4 (12 Konfigurationen) 301 s Schleife, 5 min 21 s Dienstzeit; hier 12 bis 13, erwartet 5 bis 6 min je
  Aufruf, RuntimeMaxSec 600. --budget 500 bricht die Schleife vor der Dienstgrenze ab (dann Ausgabe "Abbruch True", Arm
  nach Scheiterregel "nicht auswertbar", wenn dE1000 > 0,02).
- Rauchtest lokal vorher: CPU, 1 Thread (OMP_NUM_THREADS=1, MKL_NUM_THREADS=1), nice -n 19, CUDA_VISIBLE_DEVICES leer,
  timeout 120 fuer alle drei Aufrufe zusammen, `--rauch --geraet cpu` (dx 0,6, 300 Iterationen, je 3 Konfigurationen).
  Zahlen ungueltig, nicht geerntet.

## 6. Auswertung

- y2auswertung liest y2b/y2a/y2c_ergebnis.json und wendet 1 (Wortlaut) mit den Lesarten Z3 bis Z6 an; ERGEBNIS.md
  zitiert Tabelle, Urteil je Arm, Kontrollen (dE1000, Schub, Windungen, Ball S_0/R_halb, Z7), Laufzeiten, Hashes.
- Keine nachtraegliche Aenderung von Geometrien, Schwellen oder Lesarten. Nachtraege nur mit date und offengelegt.

## 7. Grenzen vorab

- 2D-Querschnitt, ein Ball, eine Klammerart; die Klammer bestimmt nachweislich die Lage des Gegenwirbels (Y-1 4.2).
- Energiedifferenzen auf etwa +-0,6 unsicher (Y-1 fein gegen grob); (iii) und (v) liegen in dieser Groessenordnung.
- ALT-1 A4 ist nach eigener Angabe um Faktor >= 2,5 unsicher; der Test kann in beide Richtungen ausgehen.

## 8. Hashes und Zeiten

- Eingefroren 2026-09-30 12:48:22 CEST (date). y2.py sha256 3de388e0e52bfbe64bde90fd0736aa0e5172aa2eef9c517f9c97259d8939b8a5
  (Stand beim Einfrieren, vor dem Rauchtest). y1.py sha256 d04cdfd861c1192888ba9829485fa8198c7289a4e28c04749eb7cffac8d1e986
  (unveraendert).

## 9. Nachtrag 12:50:43 (date), nach dem lokalen Rauchtest, vor jedem Lauf auf der .69

- Eingefrorene Kopie: PLAN.md.eingefroren-20260930-124834, sha256 f79c87f082bd6864069d9c6a204228ed7e3d1cc7e4f327ac250710ec58119997.
- Rauchtest lokal 12:48:42 bis 12:50:38 (CPU, 1 Thread, nice 19, CUDA_VISIBLE_DEVICES leer, dx 0,6, 300 Iterationen,
  je 3 Konfigurationen; zusammen etwa 70 s; lauf-lokal/). Zahlen ungueltig, nicht geerntet.
- Zwei Programmfehler behoben, keine Physik:
  - Berichtszeile "Ball radial" formatierte den neuen Schluessel (b, m) als Zahl (TypeError, rc 1 in allen drei Armen).
  - y2auswertung brach bei fehlenden Geometrien ab (Rauchdaten); jetzt werden fehlende Geometrien uebersprungen (nan).
- y2.py sha256 jetzt e0f4559ace72d2c82b1004028cb04bdcf5457bff29a79490e1175f283682f5af (dieser Stand geht auf die .69).
