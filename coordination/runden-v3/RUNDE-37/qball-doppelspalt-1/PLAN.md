# QBALL-DOPPELSPALT-1: Plan (Code-Agent fuer claude-primary)

- Start des Agenten 2026-10-05 05:36:34 CEST; dieser Plan geschrieben ab 05:58:08 CEST (date), vor jedem Haupt-, Ruhe-
  und Kleinlauf. Karte (KARTE.md) unveraendert und bindend.
- Kennzeichen: [M] eigene Mathematik/Kopfrechnung, [E] gerechnet (.69), [P] Projektdatei, [L] Literatur, [H] Hypothese.
- Bereits gesehen (Rauchtests, Abschn. 11): Energiebilanz (d), Profilzahlen, Laufzeiten, Erhaltung des frei fahrenden
  Balls bei omega = 0,9, ein Funktionslauf mit Fremdwerten (d = 2R, v = 0,4). Keine Ablenkungs- oder I2/I3-Werte.

## 1. Pflicht (a): arXiv:1508.06837 an der Quelle

- Abruf 05:42 CEST (curl, arxiv.org/pdf/1508.06837; die API-Abfrage kam leer zurueck): quellen/arxiv-1508.06837-
  20261005-054245.pdf (5 Seiten, Ekomasov und Salimov, Bashkir State University, nlin.PS, 27.08.2015).
- **Was dort steht [L, gelesen]:**
  - Gl. (1)-(3), Abb. 1 und 2: eine radiale (3+1)-D-Atmerloesung von u_rr + 2u_r/r - u_tt = u^(3/7); sonst keine Rechnung.
  - Gl. (4)-(7): Lorentz-Transformation einer inneren Schwingung cos(omega_j t) gibt die raeumliche Modulation
    cos(omega_j (t' - v x')/sqrt(1 - v^2)) "als de-Broglie-Welle" (Beispiel: bewegter Sinus-Gordon-Atmer).
  - Abb. 3: Schema (Soliton 1 teilt sich an zwei Spalten in 2 und 3, die sich zu 4 vereinen; die Richtungsverteilung
    von 4 "kann" ein Muster bilden). Aussage: Bei d >> A (Solitongroesse) verschwindet das Muster; bei Wellen bleibt es
    unter proportionaler Vergroesserung von L und d.
  - Abschn. 3: Groessenabschaetzung (Elektronen ~100 m/s, C60 vorgeschlagen).
- **Was fehlt:** Es gibt keine Simulation eines Spaltdurchgangs, kein Histogramm, keine Geschwindigkeitsskalierung,
  kein I3, keine Teilungsstatistik, kein Q-Ball-Modell. **Der Kern der Karte ist dort nicht gerechnet.** Die Arbeit
  liefert nur die Lesart lambda = 2 pi/(gamma omega v) (unsere lambda_omega, V-Q2) und die qualitative Erwartung von V-Q1.
  Deshalb volles Programm, keine Meldung "Kern schon gerechnet".

## 2. Pflichten (c), (d), (e)

### (c) Ausgangszustand je Gitter (Ruhetest, Abbruchregel)

- Profil: radialer Gradientenfluss bei fester Ladung (Klasse Radial aus DREIPOL-2, dr = 0,01, rmax = 60), Q aus der
  Projekt-Kurve (DIM-LEITER-QBALL-1, d2.json fein): Q = 38,5434 (omega = 0,8) und 15,8188 (omega = 0,9).
- Ruhetest je omega und je h (0,25 und 0,125): Ball in Ruhe bei (0, 0), ohne Wand, T = 200, dt = 0,05. Gemessen: Q(t),
  E(0), E(T), max S, Ort. Zusaetzlich Fahrtest v = 0,45 ohne Wand (Q, E gegen gamma E_rad, Ort gegen x0 + vT).
- **Abbruch (Karte):** Verliert der Ball im Ruhetest mehr als 1 % Ladung (max |Q(t) - Q(0)|/Q(0) > 0,01 bei irgendeinem
  omega oder h), wird nicht weiter ausgewertet.

### (d) Energiebilanz (vor den Laeufen; [E] aus code/qds.py bilanz, Rauchtest 1, Quelle d2.json)

- E(q) aus der 2D-Projektkurve (102 Punkte, h = 0,0125). Unter der kleinsten tabellierten Ladung q = 11,702 (Townes-
  Grenze, DIM-LEITER: "Q faellt auf 11,70 zu") gibt es in 2D keinen Ball; dort gilt E_min(q) = q (m = 1, Infimum,
  zerfliessende Ladung).
- Spaltkosten K(x) = E_min(x Q) + E_min((1 - x) Q) - E(Q), Stuecke x >= 0,10; kinetische Energie (gamma - 1) E(Q):

| omega | Q | E | K(0,10) = min | K(0,2) | K(0,3) | K(0,5) | E_kin v = 0,2 / 0,3 / 0,45 |
|---|---|---|---|---|---|---|---|
| 0,80 | 38,543 | 34,484 | 0,759 | 1,489 | 2,184 | 2,746 | 0,711 / 1,665 / 4,131 |
| 0,90 | 15,819 | 15,576 | 0,138 | 0,226 | 0,243 | 0,243 | 0,321 / 0,752 / 1,866 |

- **Folgerungen (vorab, keine Messung):**
  - omega = 0,8, v = 0,2: E_kin < K_min. Eine Teilung in zwei Stuecke >= 10 % Q ist energetisch verboten.
  - omega = 0,8, v = 0,3: erlaubt nur fuer x <= 0,22 (das kleine Stueck liegt dann unter der Townes-Grenze).
  - omega = 0,8, v = 0,45 und omega = 0,9 bei allen v: erlaubt.
  - **V-Q4 ist damit nicht vorab entschieden**, aber an einer Stelle (0,8; 0,2) vorab begrenzt.
  - **Townes-Vorbehalt [M, L]:** Bei omega = 0,9 erzeugt jede Teilung ein Stueck unter 11,70 Ladung, bei omega = 0,8
    jede Teilung mit x < 0,31. Solche Stuecke haben in 2D keinen Ruhezustand und zerfliessen. "Zwei getrennte Stuecke
    am Laufende" ist dann ein Zustand zur festen Endzeit, kein Endzustand. Zwei gebundene Stuecke (beide >= 11,70)
    sind nur bei omega = 0,8 und v = 0,45 energetisch moeglich (K(0,31) = 2,25 < 4,13).

### (e) Ableitbarkeit (Zusatz der Leitung, hier ausgefuehrt)

- **V-Q1** nahezu ableitbar (Leitung). Am fernen Spalt wirkt nur der Schwanz ~e^(-kappa r).
- **V-Q3, exakte Teilaussage [M]:** Fuer jeden Stossparameter, dessen Ausgang von einem der drei Spalte nicht
  abhaengt, ist der Beitrag zu I3 exakt null (Moebius-Summe ueber diesen Spalt hebt sich auf, P_leer = 0 fuer
  Durchgangswinkel). Ein kappa != 0 kommt also nur von Laeufen, die alle drei Spalte "spueren", oder von chaotischer
  Verstaerkung kleiner Fernwirkungen. Bei d = R liegen die inneren Kanten der aeusseren Spalte 1,5 R von der
  Mittelspaltmitte; der Halbwertskern (Radius R) erreicht sie nie. Ob |kappa| >= 0,05 wird, ist nicht ableitbar.
- **V-Q2:** nur die Skalierung ist ableitbar (falls phasengetrieben): gamma v = 0,2041 / 0,3145 / 0,5039, also
  Perioden im Verhaeltnis 1 : 0,649 : 0,405 [M].
- **V-Q4:** nach (d) nicht vorab entschieden.

### (f) Durchgangsschranke des Spalts (Zusatz des Agenten, vorab; ab 06:01 CEST)

- **Schreibtisch [M, grob]:** Ein Spalt der Breite w in einer Wand V_w = 4 ist ein Wellenleiter. Die Grundmode des
  Topfs (Breite w, Tiefe 4) hat k_perp^2 ~ 0,86 (w = 2,44, omega = 0,8) bzw. ~1,16 (w = 1,80, omega = 0,9).
  - Ladung q im Spalt kostet mindestens q * sqrt(k_perp^2 + min U(S)/S) = q * sqrt(k_perp^2 + 0,5): 1,17 q bzw. 1,29 q
    (Ungleichung |pi|^2 + mu^2 |phi|^2 >= mu |rho|).
  - Verfuegbar sind je Ladung gamma E/Q = 0,92 bis 1,00 (omega = 0,8) bzw. 1,00 bis 1,10 (omega = 0,9).
  - Liegt beim Durchgang ein Anteil ~0,4 der Ladung im Spalt (Wanddicke 2 gegen Balldurchmesser ~5), fehlen grob
    0,4 Q (1,17 - 0,9) ~ 4 bzw. 0,4 Q (1,29 - 0,95) ~ 2,1 Energieeinheiten; E_kin betraegt hoechstens 4,1 bzw. 1,9.
- **Fremdlauf [E] (Rauchtest r3, omega = 0,9, d = 2R, v = 0,6, also E_kin = 3,9):** alle 41 Stossparameter in allen
  7 Konfigurationen reflektiert, obwohl die grobe Schranke (2,1) dort unterschritten waere.
- **Erwartung (vorab, keine Messung):** Bei w = R und v <= 0,45 kommen kaum oder keine Baelle durch. Dann sind V-Q1 bis
  V-Q3 nach Abschn. 6 "unentschieden (keine wertbare Kombination)" bzw. "kein Muster", V-Q4 "unentschieden".
  - Das waere ein Ausgang des Aufbaus, nicht des Balls: Die Karte setzt w = R, und der Spalt ist dann fuer die
    Ladungsquanten unterhalb der Grenzfrequenz.
  - Den Aufbau aendere ich nicht. Ich ergaenze einen **Zusatzarm W** (Abschn. 7a, beschreibend, ohne Urteil) mit
    w = 3R. Dort liegt die Schranke unter omega (k_perp^2 ~ 0,14, sqrt(0,64) = 0,8 [M]).

## 3. Modell, Code, Gitter, Wand

- Code: code/qds.py (neu; Radial-Klasse und Verlet-Schema wie DREIPOL-2 kopiert), code/auswertung.py.
- Modell: L = |phi_t|^2 - |grad phi|^2 - U(S) - V_w(x, y) S, U(S) = S - S^2 + S^3/2 (Papier I, beta = 1/2, m = 1),
  Ladung Q = 2 int Im(phi* pi). Linearer Arm: U(S) -> S.
- Gitter: Gebiet x in [-64, 64), y in [-32, 32) (128 x 64), h = 0,25 (512 x 256) und h = 0,125 (1024 x 512).
  Isotroper 9-Punkt-Laplace, Feld ausserhalb = 0, Schwammschicht 8 Einheiten an allen Raendern (pi *= exp(-gamma dt),
  gamma = s^2, s = Eindringtiefe/8). Geschwindigkeits-Verlet, **dt = 0,05 auf beiden Gittern** (stabil: max. Eigenwert
  des 9-Punkt-Operators 5,33/h^2, omega_max dt = 0,48 bzw. 0,93 < 2 [M]). float32 auf der GPU (torch, CUDA, P4000).
- Wand: V_w = 4 fuer 0 <= x <= 2 (Dicke 2 zwischen den Halbwertskanten), Kanten als tanh mit Breite 0,25, fest und
  unabhaengig von h; Spalte sind y-Intervalle der Breite w mit denselben Kanten.
- **R = R_halb** (Halbwertsradius von |phi|^2 des radialen Profils): 2,4410 (omega = 0,8) und 1,8018 (0,9);
  kappa = sqrt(1 - omega^2) = 0,6000 und 0,4359. **w = R.**
- **Lesart d = Kantenabstand (Steg zwischen benachbarten Spalten)**, Mittenabstand p = d + w. Begruendung: Als
  Mittenabstand waere d = R mit w = R ein einziger Spalt der Breite 2R (Steg 0). Spaltmitten: Doppelspalt +-p/2,
  Dreifachspalt 0 und +-p. Werte d: omega = 0,8: 2,441 / 3,662 / 7,323 / 11,549; omega = 0,9: 1,802 / 2,703 / 5,406 /
  12,780 (fuer R / 1,5R / 3R / 2R + 4/kappa).
- Start: Ballmitte x0 = -15, Stossparameter y_b, Geschwindigkeit v in +x, exakter Lorentz-Boost des radialen Profils
  (phi = f(r') e^{-i omega gamma v (x - x0)}, pi aus der Zeitableitung). Laufzeit T = 40/v (frei: Endort x = +25).
- Stossparameter: 41 gleichabstaendige y_b in [-Y, Y], Y = groesste Spaltmitte + w/2 + R + 2/kappa (je omega und d);
  81er-Gitter = dieselben 41 plus 40 Zwischenpunkte.
- **Linearer Kontrollarm:** Gauss-Paket |phi|^2 = exp(-r^2/sigma^2) mit demselben Halbwertsradius R, Traeger k = gamma v
  (Gruppengeschwindigkeit v), rein positive Frequenz bezueglich des Gitteroperators, Q = 1; gleiche Wand, gleiche
  Spalte, gleiche Stossparameter und Laufzeiten.
- Spiegelung: B (Doppelspalt) sowie C und BC (Dreifachspalt) werden aus A bzw. AB durch y -> -y gewonnen (das Gitter
  ist unter y -> -y exakt symmetrisch, y = 0 ist Gitterpunkt). Gerechnet: Doppelspalt A, AB; Dreifachspalt A, B, AB,
  AC, ABC.

## 4. Messgroessen je Lauf (code/qds.py)

- Fluss der Ladung durch die Ebene x = 3 (zentrale Differenz, jeder Schritt), aufgeteilt in y-Zonen (naechste
  Spaltmitte): Anteil je Spalt.
- Endzustand (t = T): Kerne = Zusammenhangskomponenten (8er) von S >= 0,05 S0 (S0 = |phi(0)|^2 des Balls); jeder Punkt
  mit S >= 1e-4 S0 im Abstand <= 3R geht an den naechsten Kern. Je Stueck: Ladung, Schwerpunkt, Impuls
  P = int -2 Re(pi* grad phi). Stuecke unter 2 % Q werden nicht gefuehrt.
- **Ablenkwinkel** = atan2(P_y, P_x) des groessten durchgelassenen Stuecks (Schwerpunkt x > 2 + R/2, Ladung >= 10 % Q).
- **Ausgangsklasse** (Reihenfolge der Pruefung):
  - geteilt: >= 2 durchgelassene Stuecke je >= 10 % Q;
  - geteilt_wiedervereint: genau 1 durchgelassenes Stueck, aber >= 10 % Q flossen durch jeden von >= 2 Spalten;
  - ein_spalt: genau 1 durchgelassenes Stueck, Fluss >= 10 % nur durch einen Spalt;
  - reflektiert: kein durchgelassenes, aber ein zurueckgeworfenes Stueck (x < -R/2, >= 10 % Q);
  - steckt / zerflossen: sonst. Zusatzmerkmal teilreflexion (durch und zurueck je >= 10 %).
- Winkelverteilung der Ladung: Ladung bei x > 5 (ausserhalb des Schwamms) nach Winkel atan2(y, x - 2), 90 Bins zu 2 Grad.
- Kontrolle je Lauf: Q(0), E(0), E(T) (Energieverlust = Abstrahlung in den Schwamm).

## 5. Statistik, I2, I3, kappa (code/auswertung.py)

- Gewicht je Stossparameter 1/n (n = 41 bzw. 81). Durchgangswinkel nur von -90 bis 90 Grad (P_leer = 0).
- **Plan-Histogramm:** Gauss-Kerndichte des Ablenkwinkels, sigma = 2 Grad, Raster 0,5 Grad; P_S(theta).
  **Wortlaut-Histogramm:** gewoehnliches Histogramm, 5-Grad-Bins.
- **I2** = P_AB - P_A - P_B; Mass r2 = sum |I2| / sum (P_A + P_B).
- **I3** = P_ABC - P_AB - P_BC - P_AC + P_A + P_B + P_C; delta = |I_AB| + |I_BC| + |I_AC| (I_XY = P_XY - P_X - P_Y).
  - kappa_L1 = sum |I3| / sum delta (Plan), kappa_int = sum I3 / sum delta (beschreibend).
  - Wortlaut-Lesart nach Sinha: kappa = I3/delta im Bin, der 0 Grad enthaelt.
- **Rand-kappa:** dieselben Groessen aus der Ladungs-Winkelverteilung des linearen Arms (2-Grad-Bins).
  - Plan: kappa_korr = kappa_L1(Ball, Kerndichte) - kappa_L1(linear, Ladung).
  - Lesart "Ladung": kappa_L1(Ball, Ladung) - kappa_L1(linear, Ladung).
  - Wortlaut: kappa_Sinha(Ball, 5 Grad) - kappa_Sinha(linear, Ladung).
- **Periode (V-Q2):** Maxima der Kerndichte P_AB mit Prominenz >= 10 % des Maximums; "periodisch", wenn >= 3 Maxima
  und Variationskoeffizient der Abstaende <= 0,25; Periode = mittlerer Abstand.

## 6. Urteilsregeln (vorab, mechanisch in auswertung.py)

- Kombinationen mit weniger als 3 Durchgaengen (Summe der Einzelspalte) werden nicht gewertet.
- **Konvergenz (Karte):** Ein Wert gilt nur, wenn er sich zwischen 41 und 81 Stossparametern UND zwischen h = 0,25 und
  h = 0,125 (je 41) um weniger als 0,02 aendert. Fehlt eine Pruefung, ist der Wert "unentschieden".
- **V-Q1** (d = 2R + 4/kappa, je omega und v, 6 Kombinationen): bestanden, wenn alle gewerteten Kombinationen
  konvergiert sind und r2 < 0,05; gescheitert, wenn eine konvergierte r2 >= 0,05 hat; sonst unentschieden.
- **V-Q2** (Doppelspalt AB, d = R und 1,5R, je omega): "kein Muster", wenn keine (omega, d) bei allen drei v
  periodisch ist; sonst je solcher (omega, d): c_v = Periode(v) * gamma v, bestanden, wenn max |c_v/mittel - 1| <= 0,20
  fuer alle solchen (omega, d), sonst gescheitert.
- **V-Q3** (Dreifachspalt, d = R und 1,5R, je omega und v, 12 Kombinationen): bestanden, wenn alle gewerteten und
  konvergierten |kappa_korr| >= 0,05; gescheitert, wenn alle < 0,05; gemischt sonst; unentschieden, wenn nicht alle
  gewerteten konvergiert sind.
- **V-Q4** (Doppelspalt AB, d = R, gepoolt ueber omega und v): Anteil der durchgelassenen Laeufe (>= 1 durchgelassenes
  Stueck >= 10 % Q) mit >= 2 durchgelassenen Stuecken je >= 10 % Q; bestanden ab 20 % (mindestens 5 durchgelassene).
  Wortlaut-Lesart: >= 2 Stuecke je >= 10 % Q irgendwo (auch eines zurueckgeworfen). Keine Konvergenzbindung (Karte).
- Ein Ausgang, der aus der Energiebilanz folgt, wird als "vorab ableitbar" vermerkt.

## 7. Laufliste (.69, kleintest.sh, p4000a und p4000b; jede Einheit < 10 min, eigene Zeitgrenze 560 s)

Rauchtest-Laufzeiten [E]: h = 0,25: 33,7 ms je Schritt bei 205 Laeufen im Stapel (linear 26,8); h = 0,125: 55,7 ms
bei 82. Schritte je Lauf: 4000 / 2667 / 1778 (v = 0,2 / 0,3 / 0,45).

| Stufe | Auftrag | Stapel | geschaetzt |
|---|---|---|---|
| 0 | profil (radial), ruhe (2 omega x 2 h, T = 200, Fahrtest) | 1 | ~2 min |
| 1 | Kleintest: omega 0,8; d = R und 2R + 4/kappa; v = 0,2 und 0,45; 21 y; nur AB (84 Laeufe) | 21 | ~2 min |
| 2 | Doppelspalt, h = 0,25, 41 y, A und AB, 3 v: 2 omega x 4 d (8 Auftraege) | 82 | 8 x ~2,2 min |
| 2k | V-Q1-Konvergenz: fern, 40 Zwischen-y (2 Auftraege); fern, h = 0,125 (4 Auftraege, je Konfiguration) | 80 / 41 | 2 x 2 + 4 x 4 min |
| 3 | Dreifachspalt, d = R und 1,5R, h = 0,25, 41 y, 5 Konfigurationen: Ball (4), linear (4) | 205 | 4 x 5 + 4 x 4 min |
| 3k | V-Q3-Konvergenz: 40 Zwischen-y Ball und linear (8); h = 0,125 nur v = 0,45, Ball und linear (8, je Konfiguration nacheinander) | 200 / 41 | 8 x 4,5 + 8 x 4,3 min |

- Summe ~150 GPU-Minuten auf zwei Karten, also ~75 min. Reihenfolge der Karte gilt: Ruhetest, Kleintest, Doppelspalt
  (mit 2k), Dreifachspalt (mit 3k). Was in der Zeitbox nicht fertig wird, faellt weg; die Urteile werden dann
  "unentschieden". **Absehbar [M]:** Die h = 0,125-Pruefung fuer V-Q3 deckt nur v = 0,45 ab. Nach der Regel in
  Abschn. 6 bleibt V-Q3 dann "unentschieden"; die Teilwerte werden berichtet.
- Dreifachspalt bei d = 3R und 2R + 4/kappa wird nicht gerechnet (V-Q3 betrifft nur d <= 1,5R; Zeitbox).
- **Konvergenzlaeufe (2k, 3k) nur fuer wertbare Kombinationen** (>= 3 Durchgaenge in den Einzelspalten, Abschn. 6),
  mechanisch aus den Durchgangszahlen der 41er-Laeufe bestimmt. Ohne wertbare Kombination entfallen sie; ihr Urteil
  ist ohnehin "unentschieden (keine wertbare Kombination)". Die frei werdende Zeit geht an den Zusatzarm W.

## 7a. Zusatzarm W (beschreibend, ohne Urteil; vor jeder Hauptrechnung festgelegt)

- Wie Stufe 2 und 3, aber Spaltbreite **w = 3R** (Option --wf 3); d = R, 1,5R und 2R + 4/kappa (Doppelspalt, A und AB),
  dazu Dreifachspalt d = R und 1,5R (Ball, dann linear), h = 0,25, 41 y, 3 v.
- Ausgewertet mit denselben Groessen (Klassen, Kerndichte, r2, Periode, kappa, Teilungsanteil), gekennzeichnet "W".
  Kein Urteil ueber V-Q1 bis V-Q4; die Zahlen zeigen nur, was der Ball tut, wenn er durch den Spalt passt.
- Reihenfolge: nach Stufe 2 und den Dreifachspalt-Laeufen der Karte (Stufe 3), vor 3k nur, falls 3k entfaellt.
- Rohdaten auf der .69 unter /home/fmh/fmhc-physics-remote/qball-doppelspalt-1/lauf/ (Kleintest: lauf-klein/), danach per
  scp nach lauf-69/.
- Auswertung und Bilder: kleintest.sh p4000a qds-aw code/auswertung.py (CPU-Arbeit in der Einheit).

## 8. Erwartungen des Agenten (vorab, ohne Urteil)

- Ruhetest: Ladungsverlust << 1 % (Rauch-Fahrtest bei omega = 0,9: 7e-6).
- Ein Spalt der Breite R ist schmaler als der Halbwertsdurchmesser 2R. Ich erwarte viele Reflexionen bei v = 0,2,
  besonders bei omega = 0,8 (60 %).
- V-Q1: bestanden, falls konvergiert (80 %); Risiko: wenige Durchgaenge.
- V-Q2: "kein Muster" (65 %).
- V-Q4: gescheitert (65 %), weil der Ball nach (d) bei omega = 0,8 nur bei v = 0,45 zwei gebundene Stuecke bilden kann.

## 9. Selbstanzeigen bis zum Einfrieren

1. Rauchtests vor diesem Plan (Abschn. 11) mit echten omega; Funktionslaeufe mit Fremdwerten (d = 2R, v = 0,4 bzw. 0,6).
   Gesehen: Ausgangsklassen des Fremdlaufs (alle 10 reflektiert), Erhaltungswerte, Laufzeiten.
2. Auf der .69 einmal "python -c 'import sys; print(sys.version)'" ausserhalb von kleintest.sh (Versionsabfrage).
3. Die Energiebilanz (d) habe ich mit dem Code vor dem Einfrieren gerechnet (Rauchtest 1); ihre Zahlen stehen oben.
4. Den Abschnitt 2(f) und den Zusatzarm W habe ich **nach** Sicht des Fremdlaufs r3 (alles reflektiert) eingefuegt,
   vor jeder Rechnung mit Kartenwerten. Code-Zusatz dafuer: Option --wf (Spaltbreite in R), Bildteil "zusatz-w".

## 10. Was ich nicht aendere

- Frage, Aufbau, V-Q1 bis V-Q4, Bedeutung, Konvergenzbindung und Abbruch der Karte. Lesarten (d als Kantenabstand,
  R = R_halb, Kerndichte, Klassenschwellen) sind oben vor jeder Hauptrechnung festgelegt.

## 11. Rauchtests (vor dem Einfrieren; .69, kleintest.sh)

| Test | Spur | Inhalt | Ende (UTC) | rc |
|---|---|---|---|---|
| r1b | p4000a | bilanz | 03:51:54 | 0 |
| r1p | p4000a | profil (omega 0,8: E 34,48418, omega 0,80000005, R_halb 2,44105; 0,9: E 15,57579, R_halb 1,80184; beide konvergiert, Residuum <= 2,6e-11) | 03:51:58 | 0 |
| r2a1 | p4000a | Dreifachspalt, 205 Laeufe, Weg 4 (Zeitmessung) | 03:54:38 | 0 |
| r2a2 | p4000a | linear, ebenso | 03:54:48 | 0 |
| r2a3 | p4000a | Fremdwerte d = 2R, v = 0,4, 5 y, A und AB, voller Weg | 03:54:55 | 0 |
| r2b1 | p4000b | h = 0,125, 82 Laeufe, Weg 2 (Zeitmessung, GPU 2,5 GB) | 03:54:43 | 0 |
| r2b2 | p4000b | Ruhetest-Pfad omega 0,9, T = 10 (Fremdwert), Fahrtest | 03:54:51 | 0 |
| r3a1, r3a2 | p4000a | Fremdwerte omega 0,9, d = 2R, v = 0,6: Doppelspalt (82), Dreifachspalt in Teilstapeln (chunk 2) | 03:58:10, 03:59:14 | 0 |
| r3b1 | p4000b | ebenso, linearer Arm, Dreifachspalt (205) | 03:58:26 | 0 |
| r3aw | p4000a | Auswertung der Fremdlaeufe (Urteilspfade, Bilder) | 03:59:52 | 0 |
