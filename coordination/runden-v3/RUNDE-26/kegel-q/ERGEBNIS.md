# KEGEL-Q: Ergebnis (Code-Agent fuer claude-primary, Runde 26, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6):
  - 32 Laeufe von 02:31:43 bis 02:43:46 UTC (04:31 bis 04:44 CEST), dazu die Auswertung um 02:43:52 UTC.
  - Alle rc = 0; der laengste Lauf dauerte 5 min 34 s (Grenze 600 s).
- **Eingefroren** um 04:31:40 CEST, vor der ersten echten Rechnung:
  - PLAN.md.eingefroren-20261003-043140
  - code/kegel_q.py.eingefroren-20261003-043140 (sha256 beginnt mit 4de64b080729204c)
  - code/laufplan.eingefroren-20261003-043140.tar (Spurskripte)
- **Rohdaten:** lauf-69/ (72 JSON-Dateien einschliesslich auswertung.json, 33 Logs). Die mechanischen Urteile stehen
  in lauf-69/auswertung.json. Rauchlaeufe: rauch-69/.
- Geschrieben ab 04:46:45 CEST (date).
- **Einheiten:** Modell M1 in 2D, Masse 1. B in Energieeinheiten des Modells, Abstaende in 1/Masse.
- Q = 200 heisst: Ball mit Halbwertsradius R_half = 6,26, Ballenergie 157,3.

## Ergebnis zuerst

1. **Die Fuenfer-Ecke bindet den Q-Ball, die Siebener-Ecke stoesst ihn ab.**
   - Die Bindung folgt der exakten Abbildung B(Q) = E_eben(Q) - E_eben(sQ)/s.
   - Bei h = 0,2 trifft das Gitter alle vier Q auf 0,037 bis 0,060 %. Die Abweichung faellt genau wie h^2 (h = 0,4 / 0,3
     / 0,2: 0,15 / 0,085 / 0,037 % bei Q = 400).
   - Nach Richardson (h -> 0) bleibt ein Rest von 2 bis 3e-6. Das ist die Genauigkeit des radialen Vergleichs.
   - Werte: B = +0,74 / +1,05 / +1,45 / +2,00 an der Fuenfer-Ecke und -0,68 / -0,96 / -1,34 / -1,85 an der
     Siebener-Ecke (Q = 50 / 100 / 200 / 400).
2. **Kraftgesetz (Q = 200, h = 0,2):**
   - An der Fuenfer-Ecke steigt E(d) streng monoton. An der Siebener-Ecke faellt es, bis auf eine Stufe von +4e-9 am
     randnahen Ende.
   - Die groesste Kraft ist 0,29 bei d ~ 7,2 (Fuenfer) bzw. 0,28 bei d ~ 4,8 (Siebener). Sie wirkt also, waehrend die
     Ballwand ueber die Spitze laeuft (R_half = 6,26).
   - Ab d ~ R_half + 2/kappa (d = 9,6) ist der Rest kleiner als 1 % von B, bei d = 13,2 kleiner als 3e-5 von B.
3. **Schwanz:**
   - |E(d) - E(unendlich)| faellt mit der Rate 1,36 (Fuenfer) bzw. 1,28 (Siebener); 2 kappa = 1,33.
   - Genauer gilt im Schwanz (d >= 9,6) E(d) - E(unendlich) = -0,48 bis -0,51 f^2(Spitze) an der Fuenfer-Ecke und +0,52
     bis +0,54 f^2(Spitze) an der Siebener-Ecke, fast gleich fuer Q = 100, 200, 400 und alle h.
   - Der Betrag liegt nahe delta/2 = pi/6 = 0,524 [H]. Die Spitze "spuert" den Ball nur ueber die Felddichte an
     ihrem Ort.
4. **Der Ball liegt auf dem flachen Netz ortsunabhaengig auf 5e-15 (Maschinengenauigkeit).**
   - Es gibt also keine messbare Gitterhaftung (Peierls-Nabarro).
   - Die Bindung an die Spitze ist reine Geometrie und kein Gittereffekt.
5. **Duennwand-Bild:**
   - B/(sigma 2 pi R_half) = 0,118 / 0,111 / 0,104 / 0,099 (Fuenfer) und -0,107 / -0,102 / -0,096 / -0,092 (Siebener).
   - Beide Reihen naehern sich mit wachsendem R langsam den Grenzwerten 0,087 bzw. -0,080 der Karte.
   - Das Bild des Tropfens im Kegel traegt also [H, Kapillar-Analogie].

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang (mechanisch nach PLAN.md) |
|---|---|---|
| KQ0 | Flacher Flicken: Energie ortsunabhaengig, Schwankung < 1e-4 (85 %) | **eingetroffen**: groesste Schwankung 5,2e-15 (12 Dateien: 3 h x 4 Q, je 6 Orte, auch zwischen den Ecken) |
| KQ1 | Fuenfer-Ecke, d = 0: B trifft E_eben(Q) - E_eben(sQ)/s auf 5 % bei mindestens drei Q (65 %) | **eingetroffen**: 4 von 4 Q bei h = 0,2, Abweichung -0,056 / -0,046 / -0,041 / -0,037 % |
| KQ2 | Fuenfer-Ecke zieht an (E(d) steigt), Siebener-Ecke stoesst ab (E(d) faellt) (75 %) | **eingetroffen**: Q = 200, h = 0,2, je 17 Abstaende 0 bis 19,2. Fuenfer: kleinste Stufe +6e-8 (streng steigend). Siebener: groesste Stufe +4e-9 (Toleranz 1,3e-4), sonst fallend |
| KQ3 | Fuer d > R_ball + 4/kappa ist \|E(d) - E(unendlich)\| < 1 % von \|B\| (60 %) | **eingetroffen**: Schwelle d > 12,25, sechs Punkte je Netz. Groesster Rest 3,6e-5 (Fuenfer) bzw. 1,9e-5 (Siebener) gegen die Schranken 0,0145 bzw. 0,0134 |

- **Gegenprobe:** Bei h = 0,4 und 0,3 ergeben KQ2 und KQ3 nach denselben Regeln dasselbe Urteil (auswertung.json,
  gegenproben_andere_h).
- **Ableitbarkeit:** KQ1 war fast ableitbar. Die Karte sagt selbst, dass B(d = 0) exakt aus der ebenen Familie folgt;
  geprueft wurde hier nur, ob das Dreiecksgitter mit Kotangens-Laplace die Abbildung traegt. KQ0, KQ2 und KQ3 konnten
  scheitern.

**Bedeutung (nach Karte, Fall "KQ1 bis KQ3 treffen ein"):**
- Q-Baelle werden von Fuenfer-Ecken (positive Kruemmung) mit einer kurzreichweitigen Kraft gebunden und von
  Siebener-Ecken abgestossen, wie ein Tropfen im Kegel (Kapillaritaet [L?]).
- Auf einer facettierten Dreieckskugel saessen Q-Baelle an den 12 Spitzen [H]. Das waere eine Bruecke zwischen
  Geometrie-Teilchen (Defekten) und Feld-Teilchen [H].
- Einschraenkungen dieser Lesart:
  - Gerechnet ist nur die Energie, keine Dynamik. Ob ein laufender Ball eingefangen wird, braucht Abstrahlung oder
    Reibung und ist offen.
  - Auf der KUGELSCHALE-1 sind die Spitzen bei grossem gamma echte Knicke, bei kleinem gamma glatt verteilte Kruemmung.
    Gerechnet ist hier der exakte Kegel mit Defizit pi/3.
  - Auf einer glatten runden Kugel gaebe es keinen bevorzugten Ort (Schreibtisch der Karte, nicht gerechnet).

## Tabelle B(Q): Bindung an der Spitze

- B_gitter = E_flach(Q) - E_Spitze(Q); beide Baelle sind auf einer Ecke zentriert, R = 40.
- B_exakt aus der radialen Familie (dr = 0,01; dr = 0,005 aendert B um <= 1,9e-6).
- R_half und kappa gehoeren zum ebenen Ball mit Ladung Q.

| Q | R_half | kappa | omega | B_exakt (Fuenfer) | h = 0,4 | h = 0,3 | h = 0,2 | Abw. h = 0,2 | h -> 0 (Richardson) |
|---|---|---|---|---|---|---|---|---|---|
| 50 | 2,84 | 0,618 | 0,7865 | 0,741260 | 0,739577 | 0,740316 | 0,740842 | -0,056 % | +3,1e-6 |
| 100 | 4,25 | 0,648 | 0,7613 | 1,045113 | 1,043184 | 1,044031 | 1,044634 | -0,046 % | +2,8e-6 |
| 200 | 6,26 | 0,667 | 0,7449 | 1,446502 | 1,444139 | 1,445177 | 1,445915 | -0,041 % | +2,5e-6 |
| 400 | 9,07 | 0,680 | 0,7336 | 1,998572 | 1,995557 | 1,996881 | 1,997823 | -0,037 % | +2,4e-6 |

| Q | B_exakt (Siebener) | h = 0,4 | h = 0,3 | h = 0,2 | Abw. h = 0,2 | h -> 0 (Richardson) |
|---|---|---|---|---|---|---|
| 50 | -0,676563 | -0,674934 | -0,675649 | -0,676158 | +0,060 % | -3,2e-6 |
| 100 | -0,964600 | -0,962746 | -0,963560 | -0,964139 | +0,048 % | -2,9e-6 |
| 200 | -1,337789 | -1,335549 | -1,336533 | -1,337233 | +0,042 % | -2,6e-6 |
| 400 | -1,847947 | -1,845113 | -1,846357 | -1,847243 | +0,038 % | -2,4e-6 |

- Das Gitter unterschaetzt |B| leicht; die Abweichung skaliert wie h^2 (Verhaeltnisse 2,26 und 4,02 bei Soll 2,25
  und 4).
- Die zweite Bestimmung mit dem fernen Ball (d = 19,2) auf demselben Kegelnetz statt im flachen Flicken gibt dieselben
  Zahlen (Unterschied <= 1,5e-6, Randeinfluss bei Q = 400).
- Die Bindung ist klein gegen die Ballenergie (0,9 % bei Q = 200), aber 10 % der Wandenergie sigma 2 pi R_half.

## Tabelle E(d): Kraftgesetz (Q = 200, h = 0,2, R = 40, Laufrichtung entlang einer Gitterrichtung)

- E(unendlich) := E_flach = 157,295346.
- dE/dd aus dem Lagrange-Multiplikator.
- f^2(Sp.) = Felddichte an der Spitze.

| d | Fuenfer: E - E_flach | dE/dd | f^2(Sp.) | Siebener: E - E_flach | dE/dd | f^2(Sp.) |
|---|---|---|---|---|---|---|
| 0 | -1,44592 | 0 | 1,046 | +1,33723 | 0 | 1,054 |
| 1,2 | -1,42542 | +0,041 | 1,046 | +1,26814 | -0,100 | 1,053 |
| 2,4 | -1,33946 | +0,104 | 1,044 | +1,10388 | -0,174 | 1,042 |
| 3,6 | -1,17272 | +0,173 | 1,038 | +0,84937 | -0,251 | 0,962 |
| 4,8 | -0,92522 | +0,238 | 1,020 | +0,52036 | -0,278 | 0,670 |
| 6,0 | -0,60757 | +0,289 | 0,952 | +0,23124 | -0,190 | 0,333 |
| 7,2 | -0,24768 | +0,294 | 0,694 | +0,07162 | -0,081 | 0,120 |
| 8,4 | -0,03529 | +0,055 | 0,083 | +0,01603 | -0,021 | 0,030 |
| 9,6 | -5,9e-3 | +8,5e-3 | 1,2e-2 | +3,0e-3 | -4,3e-3 | 5,9e-3 |
| 10,8 | -1,06e-3 | +1,5e-3 | 2,1e-3 | +5,6e-4 | -7,9e-4 | 1,1e-3 |
| 12,0 | -1,95e-4 | +2,7e-4 | 3,9e-4 | +1,02e-4 | -1,4e-4 | 2,0e-4 |
| 13,2 | -3,6e-5 | +5,0e-5 | 7,2e-5 | +1,9e-5 | -3,0e-5 | 3,7e-5 |
| 14,4 | -6,7e-6 | +9,9e-6 | 1,3e-5 | +3,5e-6 | -5,0e-6 | 6,8e-6 |
| 15,6 | -1,3e-6 | (Rauschen) | 2,5e-6 | +6,6e-7 | (Rauschen) | 1,3e-6 |
| 16,8 | -2,4e-7 | (Rauschen) | 4,6e-7 | +1,2e-7 | (Rauschen) | 2,4e-7 |
| 18,0 | -3,9e-8 | | 8,8e-8 | +2,9e-8 | | 4,5e-8 |
| 19,2 | +2,1e-8 (Rand) | | 1,7e-8 | +3,4e-8 (Rand) | | 8,5e-9 |

- **Fuenfer-Ecke:** Der Ball haelt sich an der Spitze fest. Bei d = 7,2 (also schon ausserhalb von R_half) sitzt die
  Spitze noch bei f^2 = 0,69. Die Wand beult zur Spitze hin aus, danach reisst die Bindung schnell ab (8,4: f^2 = 0,08).
- **Siebener-Ecke:** Die Wand weicht der Spitze aus. Schon bei d = 4,8 ist f^2(Sp.) = 0,67.
- **Reichweite** gegen die Ballgroesse (h = 0,3): Rest < 1 % von B ab d = 7,2 / 9,6 / 12,0 bei Q = 100 / 200 / 400,
  also bei etwa R_half + 3. Die groesste Kraft liegt bei R_half + 0,5 bis 1 (Fuenfer) bzw. R_half - 0,7 bis -3
  (Siebener); das d-Raster ist 1,2.

## Kontrollen

- **Netz** (alle drei h, n = 5, 6, 7):
  - Genau eine Innenecke vom Grad 5 bzw. 7, alle anderen vom Grad 6.
  - Winkeldefekt an der Spitze +-1,047198 = +-pi/3; an allen anderen Innenecken <= 2,2e-14.
  - Euler V - E + F = 1, w = 1/sqrt(3) auf 1e-14, A_Spitze/A_regulaer = 5/6 bzw. 7/6.
  - Groesse: 30 246 bis 169 226 Ecken.
- **dE/dQ = omega:**
  - Radial an allen vier Ziel-Q auf <= 1,9e-8.
  - Auf dem Gitter (h = 0,3, Q = 199,8/200,2): flach -1,5e-8, Fuenfer-Spitze -2,0e-8.
  - Entlang der ganzen Familie (grobe omega-Schritte) <= 1,1e-3. Das ist der Differenzenfehler der Schrittweite.
- **VK:** Q faellt in der Familie monoton bis omega^2 = 0,9; alle Q und sQ liegen auf dem stabilen Ast.
- **Radialgitter:** dr = 0,01 gegen 0,005 aendert E um <= 1,9e-5 und B um <= 1,9e-6.
- **Randabstand** (R = 48 gegen 40, Q = 400, h = 0,4):
  - Ball auf der Spitze: |dE| <= 2e-13.
  - Ferner Ball (d = 19,2, Wand 11,8 vor dem Rand): dE = -1,6e-6 an beiden Kegeln.
  - Daher ist der letzte Schwanzpunkt (19,2) randbeeinflusst; KQ3 ist davon nicht beruehrt (Schranke 0,013).
- **Lagrange-Multiplikator:** Die Trapez-Summe der Multiplikator-Kraefte trifft die Energiestufen auf <= 3,5 % bis
  d = 7,2 (h = 0,2), wo die Kraft gross ist. Im exponentiellen Abfall weicht sie bis 30 % ab; das ist der
  Trapezfehler bei Schritt 1,2 und Rate 1,3 (~ 20 %).
- **Konvergenz je Punkt:**
  - Restgradient (Feldgleichung) <= 1,2e-5, Median 1,4e-7 (311 Punkte).
  - Nebenbedingungsrest |c| <= 1,6e-6; L-BFGS stoppt an der Maschinengenauigkeit von E.
  - Ausgewertet ist E_korr = E + m c (erste Ordnung); die Korrektur ist <= 5e-7.
- **Ort:** harmonischer Schwerpunkt W = <r^s e^{i s phi}>, d = |W|^(1/s).
  - W = 0 fuer den zentrierten Ball. W = d^s ist exakt, sobald der Ball die Spitze nicht ueberdeckt
    (Mittelwerteigenschaft von z^s).
  - Nahe der Spitze (d < R_half) ist d eine Reaktionskoordinate, kein geometrischer Mittelpunkt.
  - Der Schwerpunkt im aufgeschnittenen Kegel ist fuer den zentrierten Ball nicht null und wurde deshalb nicht genommen.

## Latten (v3)

- **L1: teilweise.** KQ0, KQ2 und KQ3 konnten scheitern. KQ1 pruefte nur die Diskretisierung einer exakten Abbildung
  (Ableitbarkeitspruefung der Karte).
- **L2: ja.**
  - Drei Gitterweiten mit sauberem h^2-Gesetz.
  - B auf zwei Wegen (flacher Flicken, ferner Ball auf demselben Kegel).
  - Multiplikator-Kraft gegen Energiestufen, dE/dQ auf dem Gitter, Randprobe.
- **L3: ja.** Richardson-Rest 2 bis 3e-6; Ortsunabhaengigkeit auf Maschinengenauigkeit.
- **L4: teilweise.**
  - Die Skalierung E_Kegel(Q) = E_eben(sQ)/s ist elementare Mathematik.
  - Das Duennwand-Bild entspricht dem isoperimetrischen Problem im Kegel [L?, Morgan und Ritore 2002: im Kegel mit
    Winkel < 2 pi sind Kreisscheiben um die Spitze isoperimetrisch] und der Kapillaritaet im Keil [L, Concus und Finn
    1969].
  - Dass Defekte an die Gausssche Kruemmung koppeln, ist fuer Wirbel und Disklinationen bekannt [L, Vitelli und Nelson
    2004; Vitelli und Turner 2004; Turner, Vitelli und Nelson 2010, Rev. Mod. Phys. 82, 1301]. Dort wirkt ein
    geometrisches Potential, das Vorzeichen haengt vom Objekt ab [L?, Einzelheiten nicht nachgeprueft].
  - Fuer nichttopologische Solitonen (Q-Baelle) an einer Kegelspitze ist das Kraftgesetz hier gerechnet. Es wurde nicht
    gesucht, ob es schon bekannt ist (Websuche erschoepft).
  - Alle Literaturangaben stammen aus dem Gedaechtnis und sind nicht an der Quelle nachgelesen.
- **L5: nein.**
  - Moegliche Analogien [H]: Tropfen auf Kegeln (Benetzung), Adsorbate oder lokalisierte Zustaende an Fuenfer-Ringen in
    Kohlenstoff-Kegeln, Tropfen-artige BEC auf gekruemmten Flaechen.

## Selbstanzeigen

1. **Rauchlaeufe vor dem Einfrieren** (h = 0,5 / 0,45, R = 25 / 30, Q = 123,5 / 201,3) zeigten die Tendenz von KQ0
   bis KQ2:
   - B auf -0,3 %
   - flacher Ball ortsunabhaengig
   - Fuenfer steigend, Siebener fallend

   Offengelegt im Plan, Abschnitt 7. Die Q-Liste wurde nach dem radialen Rauchlauf (R_half) gewaehlt.
2. **Verstoss gegen die Laptop-Regel:** Kurz vor 04:27:00 (date) lief lokal versehentlich `python3 -` mit leerer
   Eingabe (Tippfehler am Anfang eines grep-Befehls). Es wurde nichts gerechnet, die Regel ist trotzdem verletzt.
3. **Technik:**
   - Unter kleintest.sh (CPUQuota = 100 %) liefen die mehrfaedigen BLAS-Aufrufe im ersten Rauchlauf etwa 20-fach
     langsamer.
   - Behoben im eigenen Skript (OMP/OPENBLAS/MKL_NUM_THREADS = 1). kleintest.sh ist nicht geaendert.
   - Andere numpy/scipy-Laeufe auf den Spuren koennten denselben Bremseffekt haben (Hinweis an die Leitung).
4. **Randeinfluss:** Der Ball bei d = 19,2 traegt einen Randeinfluss von ~1e-6 (Q = 400) bzw. ~2e-8 (Q = 200). Dadurch
   kippt das Vorzeichen des letzten Schwanzpunkts an der Fuenfer-Ecke. Ohne Einfluss auf die Urteile.
5. **Nebenbedingung und Restgradient:**
   - Die Nebenbedingung ist nur auf |c| <= 1,6e-6 erfuellt, weil L-BFGS an der Maschinengenauigkeit von E stoppt (oft 12
     Aussenschritte, die Obergrenze). Daher gilt die Erste-Ordnung-Korrektur E_korr (im Plan festgelegt).
   - Der Restgradient ist an einem Punkt (Siebener, d = 1,2, h = 0,2) mit 1,2e-5 groesser als sonst.
6. **Schwanz-Gesetz:** -0,48 bis -0,51 bzw. +0,52 bis +0,54 f^2(Spitze) und die Naehe zu delta/2 sind nachtraeglich
   gefunden, nicht vorab vorhergesagt [H].
7. **KQ0 war kaum zu verfehlen** (ausser durch einen Codefehler). Eine Abschaetzung nach dem Lauf: Der Fourier-Anteil
   der Ballwand bei der kleinsten Gitterwellenzahl k = 4 pi/(sqrt3 h) ist ~ exp(-pi k/sqrt2), also ~ 1e-17 bei h = 0,4.
   Die Schranke 1e-4 lag damit weit weg [Schreibtisch, nachtraeglich].

## Einfach gesagt

Wir haben ein Netz aus lauter gleichen Dreiecken gebaut, das an einer Stelle eine Spitze hat wie eine Eistuete (dort
treffen sich fuenf statt sechs Dreiecke) oder eine Sattelstelle (sieben Dreiecke). Darauf liegt ein Q-Ball, ein
Feldklumpen, der sich wie ein Wassertropfen mit Oberflaechenspannung verhaelt. Auf der Fuenfer-Spitze spart der Klumpen
Energie und bleibt haengen; an der Siebener-Stelle kostet es Energie, und er wird weggeschoben. Wie gross diese Bindung
ist, sagt eine einfache Formel auf weniger als ein Promille genau voraus. Die Kraft wirkt nur, solange der Klumpen die
Spitze beruehrt, und ist danach praktisch weg; auf einer Kugel aus Dreiecken mit 12 Spitzen sollten solche Klumpen
deshalb an den Spitzen sitzen bleiben.
