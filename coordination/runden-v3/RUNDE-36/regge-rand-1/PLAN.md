# REGGE-RAND-1: Plan des Code-Agenten (Runde 36)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-03 23:04:00 CEST (date). Plan geschrieben ab 23:26:14 CEST
  (date), vor jeder Rechnung und vor jedem Rauchlauf.
- Karte: KARTE.md (unveraendert). Vorhersagen RR0 bis RR5 und ihre Schwellen sind woertlich uebernommen.
- Kennzeichen: [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen, [H] Hypothese,
  [M] eigene Mathematik, **[A]** = vom Agenten festgelegt, weil die Karte es offenlaesst.
- Code: code/rr.py (linear, Modi rauch und linear), code/rr_nl.py (RR5), code/rr_auswertung.py (Urteile, Bilder).

## 1. Gitter, Fehlwinkel, Eckenregel

- **Kuhn-Gitter:** Ecken n in Z^3, periodisch mit Kantenlaenge L. Je Ecke 7 positive Kantenrichtungen: 3 Achsen (Laenge 1),
  3 Flaechendiagonalen (1,1,0), (1,0,1), (0,1,1) (Laenge Wurzel 2), 1 Raumdiagonale (1,1,1) (Laenge Wurzel 3). Grad 14.
  - Je Wuerfel 6 Tetraeder, einer je Permutation p der Achsen: Pfad P0 = n, P1 = P0 + e_p1, P2 = P1 + e_p2,
    P3 = n + (1,1,1).
  - Um jede Achsenkante liegen 6 Tetraeder, um jede Flaechendiagonale 4, um jede Raumdiagonale 6 (im Code gezaehlt).
- **Diederwinkel [M]:** Der Pfad-Tetraeder (Orthoschema) hat an P0P1 pi/4, P1P2 pi/2, P2P3 pi/4, P0P2 pi/2, P1P3 pi/2 und
  P0P3 pi/3. Die Summen um jede Kante sind 2 pi: Achse 2 pi/4 + 2 pi/2 + 2 pi/4, Flaeche 4 pi/2, Raum 6 pi/3.
- **Formel im Code:** Diederwinkel an der Kante (i,j), uebrige Ecken k, l, aus den quadrierten Kantenlaengen ueber das
  Gram-Schema. Mit a = P_j - P_i, b = P_k - P_i, c = P_l - P_i gilt
  cos theta = (b.c - (a.b)(a.c)/a.a) / Wurzel((b.b - (a.b)^2/a.a)(c.c - (a.c)^2/a.a)).
  Alle Skalarprodukte folgen aus den Kantenlaengen. Die Formel ist analytisch, also fuer den komplexen Schritt geeignet.
- **Fehlwinkel:** eps_e = 2 pi - Summe der Diederwinkel der Tetraeder um e.
- **Konformer Ansatz (Karte):** psi_e = (psi_a + psi_b)/2 (Mittel der zwei Ecken, also psi am Kantenmittelpunkt) und
  l_e = l0_e psi_e^2.
  - [M] Linear gilt dl_e/l0_e = dpsi_a + dpsi_b. Das ist dasselbe wie bei l_e = l0_e psi_a psi_b. Der lineare Operator
    haengt also nicht davon ab, wie psi auf die Kante gemittelt wird.
- **Eckenregel (Karte):** F_v(psi) = Summe_{e an v} l_e eps_e = 16 pi G m_v. Einheiten G = 1, Gesamtquelle M = 1.
- **Linearisierung:** (A dpsi)_v = Summe_{e an v} l0_e deps_e (am flachen Hintergrund ist eps = 0). Zwei unabhaengige Wege:
  1. Lokale 6x6-Jacobi-Matrix d theta / d l je Tetraeder-Orientierung per komplexem Schritt (h = 1e-30), Gegenprobe mit
     zentraler Differenz (h = 1e-6). Zusammengesetzt: A = B^T K B mit B_{e,v} = l0_e fuer v in e und
     K_ef = d eps_e / d l_f.
  2. Komplexer Schritt durch die volle nichtlineare Eckenregel: A dpsi = Im F(1 + i h dpsi)/h.
- **Symmetrie [M]:** Fuer jeden Tetraeder ist theta_e = d S_t / d l_e mit S_t = Summe l_e theta_e (Schlaefli). Daher ist K
  symmetrisch und A = B^T K B ebenfalls, per Konstruktion. Geprueft wird es trotzdem: dicht auf L = 8, 10, 12.
- **Reichweite [M]:** A_vw ist nur dann ungleich 0, wenn w im Stern von v liegt.
  - Es entsteht eine 15-Punkt-Schablone. Wegen Achsenvertauschung und Inversion hat sie nur 3 freie Zahlen: a_A
    (Achse), a_F (Flaeche), a_R (Raum).
  - Die Mitte ist a_0 = -2(3 a_A + 3 a_F + a_R).
- **Kleines k [M]:** Symbol A(k) ~ -(a_A + 2 a_F + a_R)|k|^2 - 2(a_F + a_R) Summe_{i<j} k_i k_j.
  - Richtungsfrei im Fernfeld genau dann, wenn a_F + a_R = 0.
  - Die Normierung der Karte verlangt -(a_A + a_F) = 8 (Kontinuum -8 Laplace entspricht 8 k^2).

## 2. Normierungspruefung (vor dem Einfrieren, im Rauchlauf)

- **Kontinuum [L]:** Fuer g = psi^4 delta gilt R sqrt(g) = -8 psi Laplace psi, linear also R = -8 Laplace dpsi.
  - Die Eckensumme ist ein Zellintegral: Summe_{e an v} l_e eps_e ~ Integral ueber die Zelle von R sqrt(g). Jede Kante
    zaehlt halb je Ecke, das Zellvolumen ist 1.
  - Zusammen mit R = 16 pi G rho folgt -8 Laplace dpsi = 16 pi G rho, also dpsi = G M/(2 r).
- **Einfacher Fall:** dpsi = x_i x_j / 2 um eine Ecke c (Kontinuum: konstante Kruemmung R = -8 delta_ij). F_c haengt nur
  von psi im Stern von c ab, die periodische Naht auf L = 12 stoert also nicht.
  - Gerechnet wird mit komplexem Schritt, ueber den Jacobi-Weg und nichtlinear mit h = 1e-4.
- **Kriterium [A]:**
  - |F_c - (-8 delta_ij)| <= 1e-10 fuer alle sechs (i,j), auf beiden linearen Wegen;
  - A(k)/(8 k^2) = 1 auf 1e-4 bei k = 2 pi/256 in den Richtungen (100), (110), (1-10), (111), (11-1), (123).
- **Folge:** Ist das erfuellt, gilt der Faktor 16 pi G, und im Fernfeld folgt dpsi -> G M/(2 r).
- **Wenn nicht:** offenlegen. Die Eckenregel der Karte bleibt unveraendert (keine Umnormierung), RR2 wird woertlich
  geurteilt, der gemessene Faktor wird berichtet.

## 3. Rand und Hintergrund [A]

- **Rand:** periodisch (Karte, erste Wahl), Loesung per FFT: dpsi(k) = 16 pi G m(k)/A(k) fuer k ungleich 0. k = 0 entfaellt.
  Das ist ein gleichfoermiger Hintergrund -mquer mit mquer = M/L^3.
- **Residuum:** Beide Operatorwege (Jacobi und komplexer Schritt durch F) werden auf die FFT-Loesung angewandt und mit
  16 pi G (m - mquer) verglichen. Sollwert <= 1e-10 relativ (Code-Kontrolle).
- **Hintergrundkorrektur (Punktquelle an Ecke 0):** dpsi_korr(x) = dpsi_L(x) - G M [xi/(2L) + pi |x|^2/(3 L^3)] mit
  xi = -2,837297 [L].
  - Herkunft: Torus-Green-Funktion G_L = 1/(4 pi r) + xi/(4 pi L) + r^2/(6 L^3) + O(r^4/L^5) [L] und dpsi = 2 pi G M G_L.
  - TENSOR-EIS-0 hat den 1/L-Koeffizienten numerisch auf 4e-4 bestaetigt.
- **Kugelklumpen:** dpsi_korr = dpsi_L - G M xi/(2L) - pi G (M |x|^2 + Summe_y m_y |y|^2)/(3 L^3).
- **Restfehler [M, grob]:** Der naechste Torusterm (Hexadekapol) ist relativ etwa 7,5 K4(x) r^5/L^5 mit
  K4 = Summe x_i^4/r^4 - 3/5. Bei r = 16 und L = 64 sind das hoechstens 0,3 %.
- **Gegenprobe ohne Urteil:** Groessenreihe L = 64, 128, 256 (Punktquelle, 13 Strahlen, r <= 16). Je Punkt exakte
  Loesung von dpsi_L = a + b/L + c/L^3, dann dpsi_FS = a und xi_fit = 2b/(G M).
- **Gauss-Massen:** Hintergrundzusatz + mquer |D_R| (fuer den Operatorfluss exakt).

## 4. Messvorschriften

- Koordinaten zentriert an der Quellecke (Klumpenmitte), Komponenten von -L/2 bis L/2 - 1.
  f(x) = |x| dpsi_korr(x) / (G M/2).
- **Quellen:**
  - (a) m = M = 1 an Ecke 0.
  - (b) m_v = M/N_b fuer alle Ecken mit |x| <= 6 (gleichfoermige Gitterkugel, N_b Punkte).
- **RR2-Groesse [A]:** max |f(x) - 1| ueber *alle* Gitterpunkte mit 6 <= |x| <= L/4 = 16 (L = 64), Punktquelle. Das ist
  strenger als einige Strahlen, weil alle Richtungen eingehen.
- **RR3-Groesse [A]:** Schale 11,5 <= |x| <= 12,5, Punktquelle, S = (max f - min f)/Mittel f (Spitze-Spitze,
  korrigiert).
  - Grund fuer f statt dpsi: In der Schale schwankt |x| um +-4 %; r dpsi nimmt diesen trivialen Radialgang heraus.
  - Berichtet werden zusaetzlich die relative Standardabweichung und die Rohwerte.
- **Strahlen (Bilder):** 13 Richtungen (100), (010), (001), (110), (1-10), (101), (10-1), (011), (01-1), (111), (11-1), (1-11),
  (-111); darunter die Kuhn-Diagonalen und Richtungen quer zu ihnen.
- **Gauss-Massen [A]:** Wuerfel D_R = {max_i |x_i| <= R} um die Quelle, R = 10, 12, 14, 16, 18, 20, 24, 28 (L = 64; bei
  L = 32 nur R <= 14).
  - **M_G(R)** = -(1/(2 pi G)) Summe ueber Achsenlinks v in D, w nicht in D von (dpsi_w - dpsi_v) + mquer |D_R|. Das ist
    die Kartendefinition (Gradientenfluss durch die Wuerfelflaeche, Flaeche 1 je Link). **Danach wird RR4 geurteilt.**
  - **M_op(R)** = (1/(16 pi G)) Summe_{v in D, w nicht in D} a(w - v)(dpsi_w - dpsi_v) + mquer |D_R|: Fluss des
    Regge-Operators selbst (Beispiel der Leitung).
    - [M] Diskreter Gauss-Satz: Fuer jeden symmetrischen Operator mit Zeilensumme 0 ist M_op exakt die eingeschlossene
      Quelle. Das ist eine Identitaet, also Code-Kontrolle und keine Messung.
  - **M_kugel(R)** (nur Bericht): 4000 Fibonacci-Punkte, radiale Differenz +-0,5 mit trilinearer Interpolation, Zusatz
    mquer (4/3) pi R^3.
  - **Hinweis vorab [M]:** Ist A = 8(-Laplace_7) (siehe AP1), dann ist M_G identisch M_op. Dann ist auch RR4 vorab
    ableitbar.

## 5. Gittergroessen und Laeufe (alle ueber kleintest.sh, Spur p4000a, nacheinander)

- L = 8, 10, 12 dicht: Symmetrie, Konstante, volles Spektrum, Abgleich mit dem Symbol (RR0, RR1).
- Symbol auf dem k-Gitter von L = 64 (RR1: inkommensurable Nullstellen) und an Zonenrandpunkten.
- L = 32 und 64: Loesungen und Messgroessen fuer (a) und (b). Die Urteile fallen auf L = 64 (Karte).
- L = 128 und 256: nur Punktquelle und Strahlen (Groessenreihe).
- **Rauchlauf:** rr.py --modus rauch (L = 8 und 12), rr_nl.py klein. Hauptlauf: rr.py --modus linear (geschaetzt unter
  3 min), rr_nl.py (RR5), rr_auswertung.py.
- **Gegenprobe Tetraeder-Oktaeder-Wabe:** nur wenn Zeit bleibt (voraussichtlich nicht).

## 6. Urteilsregeln (eingefroren)

- **RR0** eingetroffen genau dann, wenn alle drei gelten:
  - (a) max |eps_e| bei psi = 1 auf L = 8 und L = 64 < 1e-12.
  - (b) max |A - A^T| / max |A| <= 1e-12 auf L = 8, 10, 12 (dicht, Jacobi-Weg).
  - (c) max |A 1| / max |A| <= 1e-12 auf L = 8, 10, 12 (gleichmaessige Skalierung ist Nullmode).
  - Zusatz (Bericht): F bei psi = 1,3 ueberall, eps < 1e-12 (Skalierung auch nichtlinear flach).
- **RR1** eingetroffen genau dann, wenn alle drei gelten:
  - Fuer L = 8, 10, 12 gibt es genau einen Eigenwert mit |lambda| <= 1e-9 lambda_max. Sein Eigenvektor ueberlappt mit
    der normierten Konstanten zu mindestens 1 - 1e-9.
  - Kein Eigenwert < -1e-9 lambda_max.
  - Auf dem k-Gitter von L = 64 ist min_{k ungleich 0} A(k) > 1e-9 max A(k).
  - Die Zonenrandpunkte (pi,0,0), (pi,pi,0), (pi,pi,pi) (Schachbrettmoden) sind darin enthalten und werden einzeln
    berichtet.
- **RR2** eingetroffen, wenn bei L = 64 (Punktquelle, korrigiert) max |f - 1| <= 0,03 ueber alle Gitterpunkte mit
  6 <= |x| <= 16.
- **RR3** eingetroffen, wenn bei L = 64 (Punktquelle, korrigiert) S(12) < 0,02.
- **RR4** eingetroffen, wenn bei L = 64 fuer alle R in {10, 12, 14, 16, 18, 20, 24, 28} gilt:
  |M_G(a)/M_G(b) - 1| <= 0,01.
- **RR5** siehe Abschnitt 7.
- "nicht auswertbar", wenn der Lauf fehlt, abbricht oder (RR5) nicht konvergiert.

## 7. RR5 (nichtlinear, wahlweise, geringste Prioritaet) [A]

- **Aenderungen nach Rauchlauf 3 (23:34, vor dem Einfrieren, offengelegt in Abschnitt 9):**
  - Kasten L = 64 statt 48, Mitte c = (32, 32, 32).
  - Randkorrektur: Geurteilt wird Q_kasten statt Q (siehe unten).
  - Ein Lauf je d.
  - Die Schwelle 0,20 und die Menge der neun Paare bleiben unveraendert.
- **Rand:** Dirichlet-Kasten. Torus L, alle Ecken mit einem Index 0 ("Naht") fest auf psi = 1; unbekannt sind die
  inneren Ecken.
- **Klumpen:** gleichfoermige Gitterkugeln vom Radius a = 3 mit Eigenmasse m_v = m/N_a (Karte: Eckenregel mit m_v).
  - Mittelpunkte c +- (d/2) x-Richtung, d in {12, 16, 20}.
  - m/d in {0,025, 0,05, 0,1}, also m = (m/d) d. Neun Paare; je Paar drei Loesungen: Paar, nur +, nur -.
- **Loesung:** Richardson-Iteration psi <- psi - omega P^-1 (F(psi) - 16 pi G m) auf den inneren Ecken.
  - Vorkonditionierer P = 8(-Laplace_7) mit Dirichlet-Rand (DST-I).
  - omega = 1; steigt das Residuum, wird omega halbiert.
  - Abbruch bei max |Residuum| <= 1e-10 x 16 pi G max m_v, sonst "nicht konvergiert" (nach 300 Schritten).
- **Randmasse:** M_bd = (1/(16 pi G)) x Fluss des linearen Regge-Operators durch die Oberflaeche des Wuerfels D_R um c.
  Angewandt auf dpsi = psi - 1, Wuerfel wie in Abschnitt 4.
  - Geurteilt bei R = 18; berichtet auch R = 16 und 20, dazu Summe m_v/psi_v (Kontinuumsidentitaet fuer M_ADM).
- **Groesse:** DeltaM = M_bd(Paar) - M_bd(+) - M_bd(-), Q = DeltaM / (-G M+ M- / d) mit M+- = M_bd(einzeln).
- **Randkorrektur (nach Rauchlauf 3):**
  - Im Dirichlet-Kasten ist der Newton-Kern zwischen den Klumpen nicht 1/d. Er ist um die Spiegelbilder kleiner.
  - Im Rauchlauf (L = 24, d = 8) war d <K> = 0,46. Q = 0,40 entstand also fast ganz aus dem Kasten.
  - Deshalb geurteilt: Q_kasten = DeltaM / (-G M+ M- <K>), mit
    <K> = 4 pi Summe_v m+_v u_-(v) / (m+ m-) und u_- = (-Laplace_7)^-1 m- im selben Kasten (DST-I).
  - Im freien Raum gilt nach dem Schalensatz <K> = 1/d, also Q_kasten = Q. Q ohne Korrektur wird mitberichtet.
- **Urteil:** RR5 eingetroffen, wenn |Q_kasten - 1| <= 0,20 fuer alle neun Paare (alle haben m/d <= 0,1).
- **Kontrolle ohne Urteil:** m = 0,01 bei d = 12. Erwartet Q_kasten -> 1 fuer m -> 0 [M]. Grund: F(lambda psi) =
  lambda^2 F(psi) gibt die Newtonsche Bindung exakt in fuehrender Ordnung.
- **Erwartung des Agenten [M, Kontinuum in zweiter Ordnung, vorab]:**
  - Fuer ruhende Materie mit fester Eigenmasse gilt Q ~ 1 - (<phi_1> + <phi_2>) - G(M1 + M2)/(2d). Dabei ist
    <phi> = (1/m) Summe m_v dpsi_v^selbst, fuer die Kontinuumskugel 3 G m/(5a). Im Kasten wird 1/d durch <K>
    ersetzt; Q_kontinuum wird mit gemessenem <phi> mitberichtet.
  - Bei a = 3: Q ~ 0,86, 0,82, 0,78 (m/d = 0,025), 0,71, 0,63, 0,55 (0,05), 0,42, 0,26, ~0,1 (0,1; dort versagt die
    Stoerungsrechnung).
  - Also RR5 voraussichtlich **nicht eingetroffen**. Der Grund ist Kontinuumsphysik (Korrekturen in erster
    post-Newtonscher Ordnung durch die Kompaktheit), kein Gittereffekt.
  - Brill-Lindquists exakte Beziehung M = m1 + m2 mit nackten Massen gilt fuer Punktierungen (schwarze Loecher), nicht
    fuer ruhende Materie [L].
  - Pruefbar bleibt, ob das Gitter Q nahe der Kontinuumsformel liefert. <phi> wird aus der Einzelloesung gemessen.

## 8. Vorhersagen des Agenten [A] (vor jeder Rechnung; keine Kartenvorhersagen)

| Nr | Vorhersage | Urteilsregel |
|---|---|---|
| AP1 | A = 8(-Laplace_7): a_A = -8, a_F = a_R = 0. Die Diagonalen tragen linear nichts bei. [H] Grund: Glickenstein-artige Dualitaet [L?], die konforme Variation der Eckenkruemmung ist der Finite-Volumen-Laplace mit Gewicht 8 x (duale Flaeche)/(Kantenlaenge) [L?]. Das Kuhn-Gitter ist eine entartete Delaunay-Zerlegung; die dualen Flaechen der Diagonalen haben Flaeche 0 [M]. 70 % | max(|a_A + 8|, |a_F|, |a_R|) <= 1e-10 |
| AP2 | Wenn AP1: zweitkleinster Eigenwert = 8(2 - 2 cos(2 pi/L)), A(pi,pi,pi) = 96 ist das Maximum (Schachbrett am steifsten) | Abweichung <= 1e-9 relativ |
| AP3 | RR2: max |f - 1| <= 0,01. Gitterkorrektur (1/(8 r^2))(5 Summe x_i^4/r^4 - 3) [L?] <= 0,7 % bei r = 6, Torusrest <= 0,3 % | Wert <= 0,01 |
| AP4 | RR3: S(12) <= 0,005 | Wert <= 0,005 |
| AP5 | RR4: |M_G(a)/M_G(b) - 1| <= 1e-10 (Identitaet, wenn AP1) | Wert <= 1e-10 |
| AP6 | RR5 nicht eingetroffen, Q < 0,7 fuer alle drei Paare mit m/d = 0,1 | alle drei Q < 0,7 |
| AP7 | Ohne Torus-Korrektur wuerde RR2 bei L = 64 scheitern (xi/(2L) = -0,0222 gegen G M/(2r) = 0,031 bei r = 16) | Rohwert max |f_roh - 1| > 0,5 |

## 9. Rauchlaeufe vor dem Einfrieren (offengelegt)

Alle Rauchlaeufe liefen ueber kleintest.sh auf Spur p4000a. Die Abschnitte 1 bis 8 standen vor rauch1, mit Ausnahme
der unten genannten RR5-Aenderungen.

- **rauch1** (21:28 UTC, rr.py --modus rauch, L = 8 und 12, 2,5 s): Normierungspruefung und Schablone. **Gesehen:**
  - Flach: max |eps| = 2,7e-15. Tetraeder je Kante 6/6/6/4/4/4/6. Skalierung psi = 1,3: eps <= 5,3e-15.
  - Jacobi-Matrix: komplexer Schritt gegen Differenzen 2,8e-10, gleich fuer alle 6 Orientierungen. Jacobi-Weg gegen
    komplexen Schritt durch F auf L = 8: 1,1e-13.
  - **Schablone:** a_A = -8,000 (auf 2e-15), a_F und a_R <= 7,4e-15, a_0 = 48. Also A = 8(-Laplace_7) auf
    Maschinengenauigkeit; AP1 hat sich damit schon im Rauchlauf gezeigt.
  - **Normierung bestanden:**
    - F_c fuer x_i x_j/2 ist -8,000000000000005 (Diagonale) bzw. <= 8e-15 (ausserhalb), auf beiden Wegen.
    - Nichtlinear (h = 1e-4) Diagonale -8,000000018; ausserhalb 3,5e-4, also ~3,5 h. Das ist ein Gitterterm zweiter
      Ordnung, im Kontinuum waere er 0.
    - A(k)/(8 k^2) bei k = 2 pi/256: 0,99995 (100) bis 0,99998 (111). Der Faktor 16 pi G gilt; dpsi -> G M/(2r).
  - L = 8 dicht: Symmetrie 4,8e-17, A 1 8e-16, Eigenwerte 1e-13, dann 4,6863 (= 8(2 - Wurzel 2)), Maximum 96.
- **rauch2** (21:31 UTC, rr.py --modus linear --groessen 24,32, 19 s): Codepfad des Hauptlaufs. **Gesehen:**
  - L = 8/10/12 dicht: je genau eine Nullmode (Konstante), keine negativen Eigenwerte, Abgleich mit dem Symbol 1e-13,
    zweitkleinster Eigenwert wie AP2.
  - L = 32 (nicht urteilsrelevant):
    - RR2-Groesse 0,85 % (bei (0,0,6), r <= 8); roh 67 %.
    - S(12) = 4,2 %. Bei L = 32 liegt r = 12 jenseits von L/4; das ist der Torusrest.
    - M_G = M_op = 1 auf 1e-13; Kugelflaeche 1,0027 bei R = 10.
  - Residuen der FFT-Loesung <= 1,5e-13.
- **rauch3/rauch4** (21:31 UTC; rr_nl.py L = 24, d = 8, m = 0,4; Auswertung mit --L_haupt 32): Codepfade
  durchlaufen. **Gesehen:**
  - Q = 0,40 gegen eine Kontinuumserwartung von 0,83. Ursache ist der Kasten: d <K> = 0,46, gemessen in rauch5.
  - **Folge:** Randkorrektur Q_kasten und L = 64 eingefuehrt (Abschnitt 7).
  - Das ist eine methodische Korrektur vor dem Einfrieren, keine Schwellenaenderung. Sie verschiebt Q nach oben, also
    in Richtung "eingetroffen". Die unkorrigierte Fassung wird deshalb mitberichtet, und AP6 bleibt auf Q (ohne
    Korrektur) wie vorab formuliert.
- **rauch5/rauch6** (21:34 UTC; mit Randkorrektur; Kontrolle m = 0,004):
  - Q_kasten = 0,869 (m = 0,4) gegen 0,859 Kontinuum zweiter Ordnung.
  - Bei m = 0,004 ist Q_kasten = 0,992 (R = 10) bzw. 0,983 (R = 8), Summe m/psi 0,9985.
  - Die R-Abhaengigkeit stammt aus Flaechen dicht an den Klumpen (Kasten L = 24).
- **Behobene Codefehler vor dem Einfrieren:** keine Rechenfehler. Nur Hilfsparameter der Auswertung (--L_haupt,
  --R_urteil, nur fuer den Rauchlauf) und das Zusammenfuehren mehrerer rr_nl*.json.
- **Hauptlaeufe (nach dem Einfrieren):**
  - rr.py --modus linear --groessen 32,64,128,256
  - rr_nl.py je d (12 mit Kontrolle m = 0,01; 16; 20)
  - rr_auswertung.py --lauf lauf
