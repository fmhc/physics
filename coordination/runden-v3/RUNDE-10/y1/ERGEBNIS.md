# Y-1 (Runde 10): Wirbel-Dreier in einem Ball, Ergebnis

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3). Alles [H]: ein Vorbild,
  kein Proton, kein QCD-Einschluss (kein Eichfeld, kein Spin 1/2).
- Zeitkette (date, CEST; die .69 loggt UTC = CEST - 2 h):
  - Beginn 10:46:26; PLAN.md ab 11:04:20, eingefroren 11:14:12 (PLAN.md.eingefroren-20260930-111412)
  - Rauchtests lokal 11:14 bis 11:31 (CPU, 1 Thread, nice 19, timeout 120; lauf-lokal/)
  - Nachtraege im Plan: 10 (11:19:36, vor jedem .69-Ergebnis), 11 (11:28:44, nach dreier_y und dreier_neutral, vor dem
    zweiten Arm), 12 (11:31:08, nach meson und dreier_kette, vor dreier_k4)
  - .69-Laeufe LAUF1 bis LAUF15 von 11:18:37 bis 11:51:17; alle 13 Rechnungen rc = 0, zwei Wiederholungen im Warten
    abgebrochen (Liste in 9); dieser Text ab 11:46:06
- Belegstufen: [Hand] Herleitung, [A] an der Quelle gelesen, [num] numerisch (eine Gitterstufe), [num+K] mit Kontrolle
  (zweite Saat, zweite Gitterstufe oder exakte Symmetrieprobe), [Bild] aus den PNG gelesen, [H] Hypothese, [nachtr.]
  Deutung oder Teilauswertung erst nach dem Ergebnis.
- Quellen: lauf-69/ausgabe/*_ergebnis.json (Feldpfade in eckigen Klammern), *_bericht.txt, PNG, auswertung_bericht.txt;
  Logs lauf-69/LAUF*.log. Code y1.py (Kopie von rot1.py plus Abschnitt "Y-1").

## 0. Ergebnis in fuenf Punkten

1. **Weder Y noch Dreieck: Der festgehaltene Dreier zerfaellt, das Band reisst durch Paarbildung.** In der unveraenderten
   Formel (N = 3, J_ab = 1, g = 0,5 und 0,2) gibt es zwischen den Wirbeln keine Waende und keine Kanaele.
   - Kleine Dreiecke bilden einen gemeinsamen leeren "Beutel": ein Loch mit S -> 0, dessen Rand durch alle drei Wirbel
     laeuft (gleichseitig a = 6 und 9; kollinear l = 5).
   - Groessere Anordnungen schirmen einzelne Wirbel ab: Ein Gegenwirbel derselben Komponente entsteht im entleerten Kern
     (Radius ~3). Der Rest sitzt als ganzer Wirbel (alle drei Komponenten winden, S -> 0) in einer Ecke oder zwischen dem
     naechsten Paar.
   - Gezaehlt sind die Gegenwirbel bei g = 0,2, im zweiten Arm und mit weitem Ring. Bei g = 0,5 mit Ring r < 2 schliesse
     ich sie aus Lochbild, Kernen und Rauchtest; die Wiederholung mit Zaehlung ist nicht gelaufen (8).
   - Die Energie flacht ab: gleichseitig E(a = 6/9/12/15) = 2159,33 / 2165,43 / 2170,90 / 2171,34, Meson (Wirbel plus
     Gegenwirbel) E(d = 6/9/12/15) = 2144,55 / 2148,38 / 2149,02 / 2149,11 [num+K: zwei Saaten gleich auf 3e-5].
2. **"Zweier schlaegt Dreier" tritt auf, aber anders als vorab beschrieben:** Paar plus Einzelwirbel ohne Band zum Rand.
   - Bei gestreckt 9/13, stumpf 6 und kollinear 6,5 teilen sich zwei benachbarte Wirbel einen Schlitz. Der dritte ist
     durch einen Gegenwirbel abgeschirmt [num, Bild].
   - Der Zerfallsausgang nach dem Wortlaut der Regel 7 (Arme zum Rand oder zwei Klumpen) greift nicht: 0 Wandwechsel auf
     dem Kreis um alle drei, ein Klumpen, 12 von 12.
3. **Regel 7 nach Wortlaut: "weder noch"** fuer g = 0,5 und g = 0,2.
   - g = 0,5: Y-Fit RMS 1,62, Dreiecks-Fit RMS 1,32; R = 0,80 +- 0,46 bei Grenze 0,808.
   - g = 0,2: kein Anstieg (R = -2,3).
   - Die Fits mischen Zustaende verschiedener Art (Beutel, Schlitz, Ecke, abgeschirmt). Ein Gesetz fuer "den" Dreier gibt
     es in dieser Formel nicht.
4. **Der Mechanismus haengt am billigen Kern.** Bei N = 3 kostet eine Flaeche ohne die eigene Komponente nur (g/12) S^2
   je Flaeche, bei N = 2 (g/4) S^2 [Hand]. Dort (K1 = ROT-1) haelt der leere Schlitz bis d = 9,5.
   - Ein weiter Klammerring (r < 4) verschiebt das Reissen nur: Meson linear bis d ~ 12, flach ab 15.
   - Der zweite Arm (+ c sum \|psi_a\|^4, c = 0,4, andere Theorie) haelt den Beutel bis a = 12. Regel 7 ergibt dort nach
     Wortlaut "Dreieck", weil die Reihen Beutel und abgeschirmte Zustaende mischen.
   - [nachtr.] Die sieben intakten Beutel allein passen eher zu Y (Restfehler 0,29 gegen 0,41). Beides ist nicht
     belastbar, und das Meson reisst auch mit c.
5. **Kontrollen:**
   - K1: y1.py reproduziert ROT-1 paar auf <= 4e-16.
   - S_3-Vertauschung: <= 4e-16.
   - Neutral- und Y-Saat: gleicher Endzustand in 24 von 24 Geometrien.
   - g = 0: kein Anstieg (-0,33 je Laenge).
   - Feines Gitter: gleiche Zustaende in 3 von 3. Die Differenz der zwei Schluesselgeometrien aendert sich um 23 %
     (Energiedifferenzen +-0,6).

## 1. Tabelle E gegen Geometrie (g = 0,5, unveraenderte Formel, Klammer r < 2)

Beste konvergierte Saat [dreier_*_ergebnis.json: konf[].E, dE1000]. Neutral- und Y-Saat enden in allen 12 Geometrien im
selben Zustand (Differenz <= 3e-5, meist <= 1e-7). Die Kettensaat ist bei gleichseitig 12 und 15 um 0,04 bzw. 0,05 tiefer; das ist
derselbe Zustand in einer anderen, symmetrisch gleichwertigen Ecke (A statt C), also Gitterunschaerfe.

| Geometrie | L_St (Y) | P/2 (Dreieck) | E | Zustand [S_loch, knoten, Bild] |
|---|---|---|---|---|
| gleichseitig 6 | 10,392 | 9,000 | 2159,3348 | Beutel: Loch ueber das ganze Dreieck (S an den Kantenmitten 0,03) |
| gleichseitig 9 | 15,588 | 13,500 | 2165,4282 | Beutel (Kantenmitten 0,07 bis 0,08) |
| gleichseitig 12 | 20,785 | 18,000 | 2170,8991 | ganzer Wirbel in einer Ecke, zwei Wirbel abgeschirmt |
| gleichseitig 15 | 25,981 | 22,500 | 2171,3358 | wie 12 |
| gestreckt 9 | 13,789 | 12,078 | 2165,2463 | Schlitz A-B (Kantenmitte AB leer), C abgeschirmt |
| gestreckt 13 | 19,917 | 17,446 | 2169,0267 | Schlitz A-B, C abgeschirmt |
| stumpf 150 Grad, 6 | 12,000 | 11,796 | 2164,4558 | Schlitz B-C, A abgeschirmt |
| stumpf 150 Grad, 9 | 18,000 | 17,693 | 2169,8774 | ganzer Wirbel in B, A und C abgeschirmt |
| kollinear 5 | 10 | 10 | 2159,8362 | Schlitz A-B-C (Beutel) |
| kollinear 6,5 | 13 | 13 | 2165,4591 | Schlitz B-C, A abgeschirmt |
| kollinear 8 | 16 | 16 | 2168,4117 | ganzer Wirbel in B, A und C abgeschirmt |
| kollinear 10 | 20 | 20 | 2169,8461 | wie 8 |

- Konvergenz: max \|dE\| in 1000 Iterationen <= 1,1e-3 in allen 12 (gleichseitig 15 am langsamsten).
- Messbild: dreier_y_g+0.5_*.png (Spalten: RGB aus (n_1, n_2, n_3)/S, Kopplungsdefizit, arg P, ganzer Ball).
  - Schwarze Flaechen im RGB-Bild: Loecher mit S < 0,05 S_max.
  - Farbige Flecken um die Wirbel: entleerte Kerne (cyan = ohne psi_1, magenta = ohne psi_2, gelb = ohne psi_3).
  - Das Kopplungsdefizit ist nur am Rand dieser Kerne von null verschieden; entlang der Kanten und Steiner-Arme ist es null
    [Bild]. Es gibt also keine Waende.

## 2. Fits beider Gesetze, Steigungsverhaeltnis, Regel 7

Quelle: auswertung_bericht.txt / auswertung_ergebnis.json ["dreier_0.5"], ["dreier_0.2"], ["dreier_0.0"],
["dreier_0.5_c0.4"], ["dreier_0.5_k4"]. Beste Saat je Geometrie; Fits E = E_0 + sigma L ueber alle Geometrien eines Arms.
R = Steigung gleichseitig (a = 9..15) / Steigung kollinear (l = 6,5..10; beim weiten Ring 8,5..12).

| Arm | Fit Y: sigma, RMS (max) | Fit Dreieck: sigma, RMS (max) | R (Y 0,866 / Dreieck 0,750) | Urteil nach Regel 7 |
|---|---|---|---|---|
| g = 0,5 | 0,762 +- 0,111; 1,62 (2,77) | 0,911 +- 0,105; 1,32 (2,13) | 0,804 +- 0,458 | weder noch |
| g = 0,2 | -0,098 +- 0,269; 3,91 (9,86) | -0,065 +- 0,312; 3,93 (10,33) | -2,34 +- 1,60 | weder noch |
| g = 0 (Kontrolle) | -0,328 +- 0,036; 0,52 | -0,365 +- 0,052; 0,66 | 0,82 +- 0,13 | (keine Regel; kein Anstieg) |
| zweiter Arm, c = 0,4 | 1,175 +- 0,159; 2,32 (5,21) | 1,434 +- 0,112; 1,41 (3,48) | 0,646 +- 0,142 | **Dreieck** nach Wortlaut |
| weiter Ring r < 4 | 0,995 +- 0,249; 1,98 (3,19) | 1,132 +- 0,188; 1,43 (2,30) | 1,36 +- 0,39 | weder noch |

- g = 0,5: Der Dreiecks-Fit ist etwas besser (1,32 gegen 1,62), R liegt knapp unter der Grenze, aber mit Fehler 0,46.
  Beide Restfehler sind groesser als 10 % der E-Spanne (12,0). Ausgang: **weder noch**.
- Die Restfehler sind keine Streuung: Sie folgen den Zustandswechseln aus 1 (Beutel, Schlitz, Ecke). Zum Beispiel liegen
  gleichseitig 6 und kollinear 5 (Beutel) im Y-Fit bei -2,8 und -2,0, gleichseitig 15 (Ecke) bei -2,6.
- g = 0,2: Bei gleichseitig 15 hat der ganze Wirbel den Ball verlassen (E faellt um 15). Damit gibt es keinen Anstieg.
- Zweiter Arm: "Dreieck" nach Wortlaut (R = 0,65 < 0,808 und RMS Dreieck 1,41 < 0,77 x 2,32). Die Reihen mischen aber
  intakte Beutel (gleichseitig 6 bis 12, kollinear 5 und 6,5) mit abgeschirmten Zustaenden (kollinear 8 und 10). Die
  kollineare Steigung 3,36 ist ein Sprung zwischen Zustaenden, keine Spannung. Die Teilauswertung der sieben intakten
  Beutel (4.1) zeigt eher Y. Beides ist nicht belastbar.
- Die Zeilen "Vorhersage mit tau_2" im Bericht nutzen die lineare Meson-Steigung ueber abflachende Daten (0,48). Sie sind
  deshalb ohne Aussage.

## 3. Wie der Dreier zerfaellt (Aufgabe 5)

- **Keine Waende.** Vorab erwartet waren je Wirbel zwei W-Waende oder ein Kanal (PLAN 2.2). Tatsaechlich liegt jeder
  Wirbel in einem grossen Kern ohne die eigene Komponente, gefuellt von den beiden anderen [Bild, arme[].na_rel_min_quer].
  - Radius ~2,5 bis 3 bei g = 0,5.
  - Das ist der gefuellte Kern aus ROT-1 1.1, hier mit zwei Fuellkomponenten statt einer.
- **Abschirmung** [num+K fuer g = 0,2, zweiter Arm und dreier_k4: Windungszaehlung windung_um_wirbel,
  wirbel_je_komponente].
  - Im entleerten Kern entsteht ein Gegenwirbel derselben Komponente, knapp ausserhalb des Klammerrings: 1,8 bis 2,1
    (Ring bis 2) bzw. 3,8 bis 4,1 (Ring bis 4) vom festgehaltenen Wirbel.
  - Die eigene Windung um den Wirbel faellt dort auf 0. Ausserhalb des Kerns sind die Phasen dann ohne Wand verriegelt.
  - Beispiel g = 0,2, gleichseitig 12, psi_1: festgehaltener Wirbel bei A (-6,0; -3,5), Gegenwirbel bei (-5,0; -1,6),
    Ausgleichswirbel bei (-0,1; 8,2) neben der Ecke C (0; 6,9). psi_2 spiegelbildlich, psi_3 nur bei C.
- **Der Rest wird ein ganzer Wirbel.** Die drei Ausgleichswirbel (je einer von psi_1, psi_2, psi_3) sitzen zusammen in
  einem Loch mit S -> 0; P = psi.psi windet dort zweimal [P_umlauf, S_loch]. Wo er sitzt, haengt von der Geometrie ab:
  - kleine Dreiecke: das Loch fuellt das Dreieck ("Beutel", kein Gegenwirbel noetig)
  - ein kurzes Paar: Schlitz zwischen den beiden, dritter Wirbel abgeschirmt ("Paar plus Einzelwirbel")
  - sonst: in einer Ecke (dort verschmilzt er mit dem Kern des Eckwirbels), die anderen beiden abgeschirmt
  - g = 0,2, gleichseitig 15: alle drei abgeschirmt, der ganze Wirbel hat den Ball verlassen (Windungen auf dem grossen
    Kreis 0, E = 2456,85 statt 2471,90)
- **Meson** (psi_1-Wirbel plus Gegenwirbel) zerfaellt ebenso: Jeder wird im eigenen Kern abgeschirmt, dazwischen bleibt
  nichts [Bild meson_meson_g+0.5_d15.png].
  - E steigt von d = 6 bis 9 um 3,84 (1,28 je Laengeneinheit) und ist ab d = 12 flach (+0,08 bis d = 15).
  - Das ist ein Band, das zwischen d ~ 9 und 12 reisst. Analogon zum Stringbruch durch Paarbildung [H, Analogie, kein
    QCD-Anspruch].
- **Warum bei N = 3 und nicht bei N = 2** [Hand, nachtr.]:
  - Bei N = 3 fehlt im Kern nur ein Drittel der Kopplung: Kosten (g/12) S^2 je Flaeche, bei g = 0,5 etwa 0,057.
  - Bei N = 2 fehlt die ganze Kopplung: (g/4) S^2 = 0,17. Der Kern ist bei N = 3 dreimal billiger, also groesser, und der
    Gegenwirbel findet Platz.
  - K1 zeigt fuer N = 2 den bekannten leeren Schlitz bis d = 9,5 ohne Gegenwirbel.

## 4. Zweiter Arm (andere Theorie) und weiter Klammerring

### 4.1 Zweiter Arm: + c sum_a \|psi_a\|^4, c = 0,4 > \|g\|/2, g = 0,5 (**andere Theorie**, nicht die Gesamtformel)

- Ausloeser (PLAN 11): Die Karte verlangt den Arm, wenn es keinen stabilen Dreier gibt. Der vorab enger gefasste
  Ausloeser in PLAN 8 griff nach Wortlaut nicht. Abweichung offengelegt.
- Ball: b = 1 + g/3 - c/3 = 1,0333. Energien sind deshalb nicht mit Abschnitt 1 vergleichbar, nur untereinander.

| Geometrie | E (c = 0,4) | Zustand [S_loch, kanten_mitte, windung_um_wirbel] |
|---|---|---|
| gleichseitig 6 / 9 / 12 | 2554,8557 / 2559,5204 / 2564,0962 | Beutel (Kantenmitten S = 0,03 bis 0,08) |
| gleichseitig 15 | 2572,5507 (dE1000 0,014) | ganzer Wirbel in C, A und B abgeschirmt |
| gestreckt 9 | 2557,9211 | Beutel |
| gestreckt 13 | 2565,9424 | Schlitz A-B, C abgeschirmt |
| stumpf 6 / 9 | 2556,9386 / 2569,6252 | Beutel / Loch in B, A und C abgeschirmt |
| kollinear 5 / 6,5 | 2555,2690 / 2557,8944 | Schlitz A-B-C (Beutel) |
| kollinear 8 / 10 | 2564,4053 / 2569,8008 | Schlitz B-C und A abgeschirmt / Loch in B |
| Meson d = 6 / 9 / 12 / 15 | 2548,2061 / 2551,2748 / 2551,4224 / 2551,4352 | reisst zwischen 6 und 9 |

- Mit c haelt der Beutel laenger: gleichseitig bis a = 12 (ohne c bis 9), kollinear bis l = 6,5 (ohne c bis 5).
  Neutralsaat = Y-Saat in den vier Proben (gleichseitig 9 und 15, kollinear 8, gestreckt 13) auf <= 2e-3.
- [nachtr., Teilauswertung nach dem Ergebnis, nicht vorab festgelegt] Die sieben intakten Beutel (gleichseitig 6/9/12,
  gestreckt 9, stumpf 6, kollinear 5/6,5), Handrechnung aus den Tabellenwerten:
  - Fit E = E_0 + sigma L_St: sigma = 0,837, Restfehler (RMS) 0,29, groesster Rest 0,49
  - Fit E = E_0 + sigma P/2: sigma = 1,058, RMS 0,41, groesster Rest 0,72
  - Steigungen: gleichseitig 1,540 je Einheit a (6 bis 12), kollinear 1,750 je Einheit l (5 bis 6,5), R = 0,88
    (Y 0,866, Dreieck 0,750)
  - Das spricht eher fuer Y. Aber es sind sieben Punkte, zwei kollineare, und der Beutel ist kein Y-Netz: Sein Rand laeuft
    ungefaehr den Kanten entlang [Bild dreierc_g+0.5_gleich9_Y_c0.4.png]. Eine Erklaerung, warum ein Loch mit Rand entlang
    der Kanten wie L_St skaliert, habe ich nicht [H]. Nicht belastbar.
- Das Meson reisst auch mit c. Es gibt also auch im zweiten Arm keine Paarspannung tau_2, mit der Y oder Dreieck
  parameterfrei vorherzusagen waeren.

### 4.2 Weiter Klammerring (r < 4 statt r < 2), unveraenderte Formel, g = 0,5 (PLAN 12)

| Lauf | E | Zustand |
|---|---|---|
| gleichseitig 9 / 12 | 2166,6779 / 2172,0604 | Beutel ueber das Dreieck (Windungen 1 bis r = 4,5) |
| gleichseitig 15 | 2179,4950 | Loch in A, B und C abgeschirmt |
| gestreckt 13 | 2175,2135 | Schlitz A-B, C abgeschirmt |
| stumpf 9 | 2174,0307 | Loch in B, A und C abgeschirmt |
| kollinear 8,5 / 10 / 12 | 2172,8472 / 2176,5349 / 2178,4536 | Loch in B, A und C abgeschirmt |
| Meson d = 9 / 12 / 15 / 18 | 2149,7595 / 2155,0364 / 2157,2917 / 2157,6046 | Steigung 1,76 / 0,75 / 0,10 je Laenge |

- Der Gegenwirbel sitzt jetzt am Rand des weiteren Rings (3,8 bis 4,1 vom Wirbel). Der Ring verschiebt das Reissen, er
  verhindert es nicht [num].
- Meson: linear bis d ~ 12 mit etwa 1,76 je Laenge, dann flach. Das ist eine Stringspannung auf kurzer Strecke, groesser
  als 2 sigma_Rand = 0,96 und als 2 sigma_W = 0,82 aus PLAN 2.4. [H] Der Kern mit der festen Phase kostet mit.
- Nur zwei intakte Dreier (gleichseitig 9 und 12). Fuer einen Gesetzesvergleich reicht das nicht.

## 5. Kontrollen

- **K1 (Code gegen ROT-1)** [num+K]: y1.py mit psi_3 = 0 und den ROT-1-paar-Einstellungen (Q = 700, tau 0,3, 6000
  Iterationen, keine Schwerpunktbindung).
  - E gleich paar_ergebnis.json auf <= 4e-16 relativ in 8 von 8 Laeufen, z. B. g = 0,5, d = 9,5: 488,6240918368635 beide.
  - Damit ist auch die neue Kopplungskraft psi_a^* (P - psi_a^2) fuer N = 2 bestaetigt.
  - Bild k1_k1_g+0.5_d9.5.png: der leere Schlitz aus ROT-1.
- **Zwei Saaten** [num+K]: Neutral- und Y-Saat geben in 24 von 24 Geometrien (g = 0,5 und 0,2) denselben Endzustand,
  \|dE\| <= 6e-4. Die Kettensaat trifft bei gleichseitig 6 und gestreckt 9 denselben Zustand, sonst einen Eckzustand
  (gleichseitig 9: +4,65 hoeher; gestreckt 13: +1,24 hoeher; gleichseitig 12/15: gleichwertige Ecke, -0,04/-0,05).
- **S_3** [num+K]: gestreckt 9 mit zyklisch vertauschten Komponenten (312) und mit einer Transposition (213):
  E = 2165,246333044449 / 2165,2463330444484 gegen 2165,246333044448, relativ <= 5e-16.
- **Schwerpunktziel**: gestreckt 13 mit Ziel Steiner-Punkt statt Ursprung: +0,033. Klein gegen alle Unterschiede in 1.
- **Schwerpunktbindung noetig**: aufsummierte Verschiebung ("Schub") 0 bis 23 Laengeneinheiten, gross genau bei den
  Zustaenden mit einem ganzen Wirbel ausserhalb der Mitte. Ohne Bindung waere der Ball weggeglitten (wie BAND-1 statisch).
- **g = 0** (Q_a einzeln fest) [num]: Alle drei Wirbel werden abgeschirmt, die Ausgleichswirbel verlassen den Ball
  (Windungen auf dem grossen Kreis 0; bei kollinear bleibt nur B in der Mitte).
  - E faellt mit der Groesse: gleichseitig 2621,29 -> 2616,08 (a = 6 -> 15), kollinear 2621,47 -> 2618,18 (l = 5 -> 10),
    also etwa -0,33 je Einheit L_St.
  - Kein linearer Anstieg, wie erwartet.
- **Feineres Gitter** (dx 0,2, n = 384; fein_ergebnis.json) [num+K fuer die Zustaende, nicht fuer die Differenzen]:
  - Alle drei Faelle enden im selben Zustand wie grob: gleichseitig 12 mit dem ganzen Wirbel in C, kollinear 8 mit Loch
    in B und zwei abgeschirmten Wirbeln, Meson d = 12 abgeschirmt ohne Band.
  - Absolutwerte steigen um 7,09 / 6,51 / 8,00 (2178,0250 / 2174,9250 / 2157,0288). Die Kerne und Loecher sind bei
    dx 0,3 schlecht aufgeloest.
  - Die Differenz E(gleichseitig 12) - E(kollinear 8) ist fein 3,100, grob 2,528, also +23 %. Energiedifferenzen zwischen
    Geometrien sind damit auf etwa +-0,6 unsicher. Das ist kleiner als die Fit-Restfehler (1,3 bis 1,6); am Urteil
    "weder noch" aendert es nichts.
- **Bilanzgroessen**: omega gemeinsam fuer alle Komponenten (feste Gesamtladung), Q_a/Q zwischen 0,316 und 0,342;
  res_frei (Residuum ausserhalb der Klammer- und Kernzonen) 1e-2 bis 6e-2 [res_frei]. Es enthaelt die Zwangskraft der
  Schwerpunktbindung und die Ringraender; als Konvergenzmass dient dE1000.

## 6. Vorab gegen Ausgang

Vorab: PLAN.md 6 (V1 bis V18, eingefroren 11:14:12), 11 (C1 bis C5, 11:28:44), 12 (K4a bis K4d, 11:31:08).

| Nr. | Vorab (kurz) | Ausgang | Bewertung |
|---|---|---|---|
| V1 | geschlossenes Netz, 0 Wechsel auf dem Kreis um alle drei, 12/12 | 12/12 ohne Wechsel, aber gar kein Wandnetz | nach Wortlaut getroffen |
| V2 | Knoten <= 1,5 von Steiner bzw. B | 6/12 (Plaketten-Knoten; die grobere Klasse bei r = 3 gab 9/12) | verfehlt |
| V3 | Y-Saat tiefste in >= 5 von 6 spitzen | 4/6 (gleichseitig 12/15: Kettensaat 0,04/0,05 tiefer, gleichwertige Ecke) | verfehlt |
| V4 | Neutralsaat endet im Y-Netz, >= 4 von 6 | kein Y-Netz; Neutral = Y-Saat in 24/24 | verfehlt |
| V5 | Kette bleibt Kette, (2 - sqrt3) a tau_2 +- 40 % ueber Y | kein Band; Kettensaat endet im Eckzustand | verfehlt |
| V6 | R in [0,81; 0,92] | 0,804 +- 0,458 | verfehlt (knapp) |
| V7 | RMS Y < RMS Dreieck | 1,62 gegen 1,32 | verfehlt |
| V8 | sigma_Y = tau_2 (Meson) +- 25 % | 0,76 gegen 0,48; Meson ohne feste Steigung | verfehlt |
| V9 | tau_2(0,5) in [0,4; 0,8] | 0,48 (lineare Anpassung), aber keine konstante Spannung | nach Wortlaut getroffen, inhaltlich verfehlt |
| V10 | tau_2(0,2)/tau_2(0,5) in [0,45; 0,65] | 0,91 | verfehlt |
| V11 | Arm = Kanal (n_a/S < 0,1 bei S > 0,5 S_0) | keine Arme; Loecher (S -> 0) und entleerte Kerne | verfehlt |
| V12 | g = 0: \|dE/dL_St\| < 0,2 tau_2 | -0,33 | verfehlt |
| V13 | S_3 <= 1e-9 | 4,2e-16 | getroffen |
| V14 | fein gegen grob: E(gleich 12) - E(kollinear 8) auf 3 % | 3,100 gegen 2,528 (+23 %); Zustaende gleich | verfehlt |
| V15 | K1 <= 1e-8 | <= 3,5e-16 | getroffen |
| V16 | kein "Zweier schlaegt Dreier" mit Band zum Rand | keines mit Band zum Rand; Paar plus abgeschirmter Einzelwirbel in 4/12 | nach Wortlaut getroffen, inhaltlich teilweise |
| V17 | g = 0,2: R in [0,81; 0,92] | -2,34 | verfehlt |
| V18 | paar3 Steigung 0,866 tau_2 +- 30 % | -0,46 tau_2 (bei d = 15 Zustandswechsel, E faellt um 5,9) | verfehlt |
| C1 | mit c kein Gegenwirbel an >= 8/12 | Gegenwirbel an 11/12 (Zaehlung bei r = 4,5; unsicher, wo der Kreis ein Loch schneidet) | verfehlt |
| C2 | Arme n_a/S < 0,1 an >= 6/12 | 6/12, das sind aber Loecher (S -> 0), keine Kanaele | nach Wortlaut getroffen |
| C3 | Y nach Regel 7 | "Dreieck" nach Wortlaut | verfehlt |
| C4 | Meson mit c linear, Steigung 0,8 bis 1,6 | flach ab d = 9 | verfehlt |
| C5 | mit c derselbe abgeschirmte Zustand, E flacht ab | Meson ja; Dreier nein (Beutel haelt laenger, E steigt) | teilweise |
| K4a | weiter Ring: kein Gegenwirbel an >= 6/8 | 2/8 ohne | verfehlt |
| K4b | Arme n_a/S < 0,1 an >= 4/8 | 4/8, Loecher bzw. Gegenwirbelkerne | nach Wortlaut getroffen |
| K4c | Y nach Regel 7 | weder noch | verfehlt |
| K4d | Meson linear bis d = 18, Steigung 0,3 bis 1,0 | linear bis ~12 (1,76), flach ab 15 | verfehlt |

- Summe V1 bis V18: 5 nach Wortlaut getroffen (davon 2 inhaltlich nicht oder teilweise), 13 verfehlt.
- Summe Nachtraege: 2 nach Wortlaut getroffen, 1 teilweise, 6 verfehlt.
- Die Vorab-Tabelle ging vom Wandbild aus (PLAN 2). Das Wandbild war falsch; daher die vielen Fehltreffer.

## 7. Latten, Einordnung, Vorschlag

- L1 ja: Die Frage konnte Y, Dreieck oder Zerfall ergeben; 19 von 27 Vorab-Zeilen verfehlt.
- L2 ja: zwei bzw. drei Saaten, g = 0, K1 gegen ROT-1, S_3, Schwerpunktziel, zweiter Arm, weiter Ring.
- L3 teilweise: Zustaende gitterfest (3 von 3), Energiedifferenzen zwischen Geometrien nur auf etwa +-0,6.
- L4 teilweise:
  - Vortex-Trimere mit Waenden sind bekannt (Eto und Nitta 2012 [A], erste Ordnung, kompakte Dreiecke, kein
    E-gegen-Geometrie-Vergleich).
  - Stringbruch durch Paarbildung ist als Idee aus der QCD bekannt [L?].
  - Neu nach meinem Stand: In der Q-Ball-Fassung mit cos 2 Delta und N = 3 schirmt ein Gegenwirbel im billigen,
    entleerten Kern jeden Bruchwirbel ab, und kompakte Dreier bilden einen gemeinsamen leeren Beutel statt eines
    Wandnetzes. Nicht an Literatur geprueft [H].
- L5 nein: modellintern, kein Messbezug.
- Einordnung [H]: Der Dreier in dieser Formel ist kein Baryon-Vorbild mit Y-String. Er ist entweder ein Beutel (kompakt)
  oder zerfaellt in abgeschirmte Einzelwirbel plus einen ganzen Wirbel. "Kein Einschluss ohne Eichfeld" (BERICHT-FARBEN
  W6) zeigt sich hier konkret als Stringbruch nach wenigen Kernradien.
- Vorschlag:
  - Y-1 als Frage "Y oder Dreieck in der Gesamtformel": **verwerfen** (es gibt kein Band, das man vermessen koennte).
  - "Beutel gegen Stringbruch" (Lochenergie gegen Abschirmung, Abhaengigkeit von g, N und c): **parken**. Wer es aufnimmt:
    die Beutelenergie gegen Umfang und Flaeche des Lochs rechnen, freie (nicht festgehaltene) Dreier zeitlich entwickeln
    und pruefen, ob der Beutel zu einem ganzen Wirbel kollabiert (Eto und Nitta: grosses omega -> Kollaps).
  - Der zweite Arm (c) ist eine andere Theorie und gibt nach Regel 7 "Dreieck", nach der Teilauswertung eher "Y". Nicht
    weiter ohne Auftrag.

## 8. Grenzen, Abweichungen, Verstoesse

- Grenzen:
  - 2D-Querschnitt (Wirbellinien), ein Ball (Q = 3600, R ~ 29), eine Klammerart (Phasenring). Das Ergebnis haengt
    nachweislich vom Ringradius ab (4.2): Der Gegenwirbel sitzt am Ringrand.
  - "Festgehalten" heisst hier: Phase der eigenen Komponente in einem Ring fest. Eine Klammer, die Gegenwirbel im Kern
    verbietet, wuerde andere Zahlen geben; physikalisch gibt es sie ohne zusaetzliche Kraefte nicht.
  - Windungszaehlung (Plaketten, Kreise) ist in Loechern mit S -> 0 unsicher. Die Zustandsnamen in 1 stuetzen sich deshalb
    zuerst auf S_loch, die Kantenmitten und die Bilder, die Windungen nur dort, wo S endlich ist.
  - Die Knotenklasse "Steiner" aus der Umlaufwindung bei r = 3 ist zu grob (gestreckt, stumpf 6: Knoten auf der Kante).
    Sie ist in 1 durch die Plaketten-Lage ersetzt. V2 ist mit der Plaketten-Lage bewertet.
  - Eine Gitterstufe ausser dem Feinlauf (5).
- Abweichungen vom Plan:
  - Knotenmaske und Windungsdiagnosen nach den Rauchtests bzw. nach dreier_y (PLAN 10, 11), nur Auswertung.
  - Zweiter Arm trotz enger gefasstem Ausloeser (PLAN 11). g = -0,5 mit c nicht gerechnet.
  - Weiter Ring als zusaetzlicher Lauf (PLAN 12).
  - PLAN 11 nennt "Energien gleich auf 1e-6" fuer die zwei Saaten; richtig ist <= 3e-5 (gleichseitig 15), sonst <= 1e-7.
  - Die Wiederholungen dreier_y und meson mit Windungsdiagnose (ausgabe_diag) habe ich abgebrochen, bevor sie rechneten:
    Beide warteten hinter fremden Laeufen am Lock, und der Feinlauf hatte Vorrang. Die Prozesse habe ich per PID beendet.
    Die Windungen fuer g = 0,5 ohne c stammen deshalb nur aus dem Rauchtest und aus dem weiten Ring; fuer g = 0,2 und c
    liegen sie vollstaendig vor.
- Verstoesse (Selbstanzeige):
  - Kurz vor 11:17:06 lokal ein leerer `python3 -` mit leerem, gequotetem Heredoc (Rest eines Befehlsmusters). Gerechnet
    wurde nichts.
  - 11:18:37 (09:18:37 UTC): Der erste Startbefehl fuer die p4000b-Kette lief wegen falscher Klammerung im Heimordner der
    .69 statt in runde10-y1. Er startete nichts, hinterliess aber fuenf leere Logdateien in /home/fmh. Ich habe genau diese
    fuenf Dateien per Name geloescht (rm -v, 09:19).
  - Auf der .69 einmal `python -c` zur Syntaxpruefung von y1.py ausserhalb von kleintest.sh (keine Rechnung).
- Kein git, keine Journaleintraege, keine Hooks oder Dienste; fremde Dateien nur gelesen.

## 9. Dateien und Rechenzeit

- Plan: PLAN.md (mit Nachtraegen 10 bis 12), PLAN.md.eingefroren-20260930-111412.
- Code: y1.py, Stand d04cdfd861c11928 (lokal = .69, /home/fmh/fmhc-physics-remote/runde10-y1/y1.py). Codestaende je Lauf
  (sha256-Anfang, jeweils per neue Datei + mv ersetzt):
  - fd60ac15: LAUF1 bis LAUF5
  - 1db0e8f0: LAUF6, LAUF7 (mit Windungszaehlung)
  - f9e483e8 oder d04cdfd8: LAUF9, LAUF10 (Python startete erst nach dem Lock)
  - d04cdfd8: LAUF8, LAUF13, LAUF14, LAUF15
  - Die Physik (Loeser, Energie, Kraft) ist in allen Staenden gleich; neu kamen nur Diagnosen, Unterbefehle und die
    Auswertung hinzu.
- Ausgaben: lauf-69/ausgabe/ (Berichte, JSON, 125 PNG), Logs lauf-69/LAUF1 bis LAUF15; Rauchtests lauf-lokal/.
- Wichtige Bilder:
  - Beutel: dreier_y_g+0.5_gleich9_Y.png, dreier_k4_g+0.5_gleich9_Y_k4.png
  - Paar plus Einzelwirbel: dreier_y_g+0.5_gestreckt13_Y.png
  - Ecke, zwei abgeschirmt: dreier_y_g+0.5_gleich12_Y.png, dreier_y_g+0.5_kollinear8_Y.png
  - Meson ohne Band: meson_meson_g+0.5_d15.png
  - N = 2-Schlitz (K1): k1_k1_g+0.5_d9.5.png
  - Uebersicht E gegen L_St und P/2: auswertung_E_gegen_L.png
- .69-Laeufe (UTC; Spur; Schleifenzeit), alle Rechnungen rc = 0:

| Lauf | Start / Ende | Spur | Schleife |
|---|---|---|---|
| LAUF1 k1 | 09:18:37 / 09:19:53 | p4000a | 63 s |
| LAUF2 dreier_y | 09:19:29 / 09:23:32 | p4000b | 225 s |
| LAUF3 dreier_neutral | 09:19:53 / 09:24:05 | p4000a | 234 s |
| LAUF4 meson | 09:23:32 / 09:27:25 | p4000b | 217 s |
| LAUF5 dreier_kette | 09:24:05 / 09:27:32 | p4000a | 192 s |
| LAUF6 dreier02 | 09:27:25 / 09:31:43 | p4000b | 240 s |
| LAUF7 null | 09:27:32 / 09:31:59 | p4000a | 251 s |
| LAUF8 dreier02n | 09:31:43 / 09:46:34 | p4000b | 238 s |
| LAUF9 dreierc | 09:29:10 / 09:37:21 | p4000a | 296 s |
| LAUF10 mesonc | 09:29:10 / 09:35:35 | p4000b | 214 s |
| LAUF11 dreier_y (Diagnose) | 09:37:21 / 09:44:16 | p4000a | abgebrochen im Warten, rc 143 |
| LAUF12 meson (Diagnose) | 09:35:35 / 09:44:16 | p4000b | abgebrochen im Warten, rc 143 |
| LAUF13 fein | 09:44:24 / 09:51:17 | p4000b | 143 s |
| LAUF14 dreier_k4 | 09:31:15 / 09:42:09 | p4000b | 301 s |
| LAUF15 auswertung | 09:44:38 / 09:47:55 | cpu3 | < 1 s |

- GPU-Zeit zusammen etwa 45 min (P4000); Wartezeit hinter fremden Laeufen bis 15 min je Aufruf.

## Einfach gesagt

Wir haben drei Wirbel, je einen in jedem der drei Felder, in einem grossen Feldklumpen festgehalten. Wir wollten
messen, ob sie wie Quarks im Proton durch einen Y-foermigen Faden oder durch ein Dreieck aus Faeden verbunden sind. Es
gibt aber gar keine Faeden. Liegen die Wirbel nah beieinander, teilen sie sich ein gemeinsames leeres Loch. Liegen sie
weiter auseinander, bildet sich neben jedem Wirbel ein Gegenwirbel, der ihn neutralisiert, und die Verbindung reisst,
aehnlich wie ein Gummiband, das sich selbst durchtrennt. Deshalb waechst die Energie ab etwa neun Laengeneinheiten nicht
mehr mit dem Abstand, und die Frage "Y oder Dreieck" hat in diesem Modell keine Antwort.
