# TETRA-KOPPLUNG: Plan des Code-Agenten (Runde 17, v3 explorativ)

- Code-Agent im Auftrag der Leitung claude-primary. Start 2026-10-02 10:54:07 CEST (date), Plan geschrieben ab
  11:08 CEST, vor jedem .69-Lauf. Verbindlich bleiben Medien, Quellen, E_int, Kontrollen, K1 bis K5 und Bedeutung
  aus KARTE.md. Hier stehen nur Praezisierungen, Abweichungen mit Grund und die vorab festgelegten Auswerteregeln.

## 1. Modell (Praezisierungen)

- Lineare Elastizitaet um das spannungsfreie Gitter. Bindung b von Knoten i nach j: Einheitsvektor e_b, Ruhelaenge
  L_b, Federkonstante k_b. Defektbindung: Ruhelaenge L_b (1 - eps), also Verkuerzung s_b = eps L_b.
- Energie E = (1/2) Sum_b k_b (e_b . (u_j - u_i) + s_b)^2, Kraft f_i = Sum_b k_b s_b e_b (zieht i zu j).
  K u = f, K = Sum_b k_b e_b e_b^T (Stern), Minimum E = (1/2) s^T k s - (1/2) f^T u.
- **Medien:**
  - M-iso: Dreiecksgitter, Naechstnachbarn, k = 1, L = 1.
  - M-aniso2: Quadratgitter, erste Nachbarn (k1 = 1, L = 1) und zweite Nachbarn (k2 = 1, L = sqrt 2, Ruhelaenge
    geometrisch). Elastische Konstanten [ES]: C11 = k1 + k2 = 2, C12 = C66 = k2 = 1, Anisotropie
    A = 2 C66/(C11 - C12) = 2 (wie M-fcc). Stabil (C66 > 0, C11 > C12).
  - M-fcc: kubisch flaechenzentriert, 12 Naechstnachbarn, k = 1, L = 1 (A = 2).
  - **Zusatzkontrolle M-iso4 (nicht in der Karte, als Zusatz markiert):** Quadratgitter mit k2 = 0,5. Dann gilt
    C11 - C12 = 2 C66, das Medium ist elastisch isotrop bei quadratischer Gittergeometrie. Trennt "Anisotropie
    koppelt" von "Quadratgeometrie koppelt".
- **Quellen (eps = 0,05):**
  - Q-A: alle Bindungen eines Knotens verkuerzt (M-aniso2: alle 8, auch die zweiten Nachbarn, je relativ eps).
  - Q-B: zwei Naechstnachbar-Knoten a, b; Vereinigung beider Bindungssterne, die gemeinsame Bindung a-b einmal um
    eps verkuerzt (Dreieck 11, Quadrat 15, fcc 23 Bindungen). Achse: Dreieck a1 = 0 Grad, Quadrat x, fcc [110].
  - Zweite Q-B-Orientierung ("gedreht"): Dreieck 60 Grad (Achse a2), Quadrat 90 Grad (y), fcc 90 Grad ([1-10]).
- **Abstand d:** Mittelpunkt zu Mittelpunkt (Q-B-Mitte = Bindungsmitte), in Einheiten der Naechstnachbarlaenge.
- **E_int** = E(beide) - E(nur 1) - E(nur 2) + E(keine). Fuer getrennte Bindungsmengen (d >= 3) gilt exakt
  E_int = -f1^T K^-1 f2 (bilinear). Hauptrechnung bilinear, Kontrolle mit den vier Termen.

## 2. Methode und begruendete Abweichungen vom Hinweis

- **Periodischer Rand, Loesung per FFT** statt spsolve: Das periodische Gitter ist translationsinvariant, K ist
  blockzirkulant. u(k) = D(k)^-1 f(k), D(k) = Sum_b k_b (1 - cos(k . Delta_b)) e_b e_b^T, Nullmoden (k = 0, beim
  fcc-Einbett zusaetzlich k = (pi, pi, pi)) auf null. Das ist die exakte Loesung desselben linearen Systems
  (Mittelwert null), kein Naeherungsverfahren. Pruefung gegen spsolve auf kleinen Gittern (Kontrolle C1).
- E_int fuer alle Lagen der zweiten Quelle in einem Schritt: E(r) = -IFFT( Sum_c conj(f2_c(k)) u1_c(k) ).
- **Groessen (groesser als im Hinweis, weil FFT billig ist und Bildquellen kleiner werden):**
  - 2D: n x n Knoten mit n = 100, 200, 400 (Dreieck als Rhombus, Quadrat als Quadrat).
  - fcc: M^3 kubische Zellen mit M = 16, 32, 64 (Einbettung als gerade Plaetze eines einfach kubischen Rasters
    2M x 2M x 2M). M = 64 hat 1 048 576 Knoten. Falls Speicher (4 GB) oder Zeit nicht reichen: M = 48.
- **Bildquellen-Untergrund:** Periodisch gilt fuer d << L: E_per(r; N) = E_inf(r) + b/N + O(r^2/L^(D+2)).
  - b wird aus den zwei groessten Systemen bei 3 <= d <= 8 bestimmt: b = (E_N2 - E_N3)/(1/N2 - 1/N3), Median ueber
    alle Strahlpunkte, Streuung berichtet. Dazu b aus N1, N2 als Pruefung der 1/N-Skalierung.
  - Isotrope Faelle (M-iso und M-iso4 mit Q-A/Q-A): b analytisch, b = P^2/(A0 C11) mit P = Dipolstaerke, A0 = Flaeche
    je Knoten. Numerisches b wird daneben berichtet.
  - E_inf(r) = E_per(r; N3) - b/N3. Groessenunabhaengig bis zum groessten d, bei dem E_inf aus N2 und N3 um weniger
    als 5 % abweicht (Achsenstrahl; auch roh ohne Abzug berichtet).
- **Fester Rand (optional, nur falls die Zeitbox reicht):** 2D, eingespanntes Sechseck (M-iso) bzw. Quadrat
  (M-aniso2), Halbweite R = 50 und 100, spsolve, Quelle 1 in der Mitte. Vergleich mit E_inf bei d = 5, 10, 20.

## 3. Strahlen, Fenster, Fit

- Richtungen (Mittelpunktsvektor):
  - M-iso: 0 Grad (Achse), 30 Grad (Diagonale, a1 + a2), 19,1 Grad (Zwischen, 2 a1 + a2); fuer Q-B dazu 60 und
    90 Grad.
  - M-aniso2, M-iso4: 0 Grad (Achse), 45 Grad (Diagonale), 26,6 Grad (Zwischen, (2,1)); fuer Q-B dazu 63,4 und
    90 Grad.
  - M-fcc: [100], [110], [111]; fuer Q-B dazu [1-10] und [001].
  - Wo der Mittelpunktsversatz der gedrehten Q-B keine exakten Strahlpunkte zulaesst, nehme ich die naechsten Punkte
    (Abstand zum Strahl <= 0,55) und markiere den Strahl als "naeherungsweise" (d_unten = 5 statt 3).
- Fenster (Abfallgesetz, je mindestens Faktor 3 in d):
  - 2D: gesamt [3, 50], fern [16, 50] (L3/8 mit n = 400, damit der r^2-Bildterm unter etwa 1 % bleibt).
  - fcc: gesamt [3, 22,6], fern [7,5, 22,6] (L/4 bei M = 64, L = 64 sqrt 2).
- Exponent n = -Steigung von log abs(E_inf) gegen log d (kleinste Quadrate) im Fernfenster. Band: Fits auf der
  unteren und der oberen Haelfte (in log d) des Fernfensters. Dazu der Gesamtfenster-Fit.
- Vorzeichen im Fernfenster: "+" (alle positiv), "-" (alle negativ), sonst "wechselnd" mit Ort des Wechsels.
  E_int < 0 heisst: gemeinsam tiefer, also Anziehung entlang dieses Strahls.
- Unsicherheit durch den Untergrundabzug: Punkte mit abs(E_inf) < 10 x (Streuung von b)/N3 gelten als unsicher.
  Liegen im Fernfenster weniger als 4 sichere Punkte, ist der Exponent "offen".

## 4. Entscheidungsregeln fuer K1 bis K5 (vorab, nach dem Lauf unveraendert)

- "~ 1/d^m" heisst: abs(n - m) <= 0,3 und beide Halbfenster-Exponenten in [m - 0,5, m + 0,5].
- **K1** (M-iso, Q-A/Q-A, faellt schneller als 1/d^2): eingetroffen, wenn in allen drei Pflichtrichtungen
  n >= 2,5 und beide Halbfenster >= 2,2. Zusatzaussage "Rest ~ 1/d^4" separat nach der ~1/d^m-Regel mit m = 4.
- **K2** (M-aniso2, Q-A/Q-A, ~ 1/d^2, Vorzeichenwechsel Achse gegen Diagonale): eingetroffen, wenn ~ 1/d^2 auf
  Achse und Diagonale gilt und die Vorzeichen dort entgegengesetzt und je eindeutig sind. Die Zwischenrichtung wird
  berichtet, entscheidet aber nicht (sie kann nahe einem Nulldurchgang liegen).
- **K3** (M-iso, Q-B/Q-B, ~ 1/d^2, ungleich null, Vorzeichen haengt von der Orientierung ab): eingetroffen, wenn fuer
  parallele Q-B ~ 1/d^2 in den drei Pflichtrichtungen gilt (Strahlen mit Vorzeichenwechsel im Fenster ausgenommen,
  hoechstens einer) und in mindestens einer der fuenf Richtungen die Vorzeichen fuer parallel und gedreht
  entgegengesetzt sind.
- **K4** (M-fcc, Q-A/Q-A, ~ 1/d^3, Vorzeichenwechsel [100] gegen [111]): eingetroffen, wenn ~ 1/d^3 in [100], [110],
  [111] gilt und die Vorzeichen in [100] und [111] entgegengesetzt und eindeutig sind.
- **K5** (M-fcc, abs(E_int) fuer Q-B/Q-B groesser als fuer Q-A/Q-A bei gleichem d): Vergleich parallele Q-B gegen
  Q-A auf [100], [110], [111] an allen gemeinsamen Punkten in [3, 22,6]. Eingetroffen, wenn in jeder der drei
  Richtungen mindestens 90 % der Punkte das Verhaeltnis > 1 haben; nicht eingetroffen, wenn in einer Richtung
  weniger als 50 %; sonst offen. Zusatz (nicht entscheidend): Verhaeltnis normiert auf die Dipolspuren.
- Fehlen Daten (Fit unmoeglich, zu wenige sichere Punkte), ist der Ausgang "offen".

## 5. Kontrollen

- **C1 Loeser:** FFT gegen spsolve (periodisch, ein Knoten fest, danach Mittelwert abgezogen) auf kleinen Gittern
  (2D n = 16, fcc M = 3), fuer Q-A und Q-B, alle Medien. Soll: max. Abweichung < 1e-10 relativ.
- **C2 quadratisch in eps:** eps = 0,025; 0,05; 0,1. E_self und E_int (vier Terme) skalieren mit eps^2:
  E(2 eps)/E(eps) = 4 auf 1e-9 relativ.
- **C3 vier Terme gegen bilinear:** E(beide) - E(nur 1) - E(nur 2) + E(keine) aus Bindungssummen (E(nur 1) und
  E(nur 2) getrennt gerechnet) gegen -f1^T K^-1 f2, bei d = 3, 4, 6 auf der Achse, alle Medien, kleine Gitter.
- **C4 Energieformel:** Bindungssumme gegen (1/2) s^T k s - (1/2) f^T u.
- **C5 elastische Konstanten:** D(k)/(A0 k^2) bei kleinem k gegen C11, C12, C66 (C44) aus der Formel.
- **C6 zwei Systemgroessen:** siehe Abschnitt 2 (drei Groessen, b-Skalierung, groessenunabhaengiges d).
- **C7 Einzelquelle gegen Eshelby, nur Groessenordnung [L?]:** 2D-Kreiseinschluss
  E = P^2 mu/(2 pi a^2 (lambda + mu)(lambda + 2 mu)), 3D-Kugel E = 2 mu P^2/(3 K (lambda + 2 mu) V), mit a = 1 und mit
  dem Wigner-Seitz-Radius; anisotrope Medien mit Voigt-Mitteln. Dazu der Anteil E_self/((1/2) Sum k s^2).
- **C8 Symmetrie:** Bei Q-A/Q-A muessen gleichwertige Strahlen gleich sein (M-iso 0 = 60 Grad, 30 = 90 Grad;
  Quadrat 0 = 90 Grad; fcc [110] = [1-10], [100] = [001]).

## 6. Eigene Erwartungen des Agenten vor dem Lauf [ES, Kontinuumsrechnung im Kopf, nicht bindend]

- M-iso, Q-A/Q-A: Kontinuumsterm null; Diskretheit ueber den anisotropen q^4-Term der Dispersion, also
  E ~ c cos(6 theta)/d^4. Dann wechselt das Vorzeichen zwischen 0 und 30 Grad.
- M-aniso2, Q-A/Q-A (P = 0,3): E_inf ~ (-0,0028 cos 4 theta + 0,0007 cos 8 theta)/d^2, also Achse etwa -0,0022/d^2
  (Anziehung), Diagonale etwa +0,0035/d^2 (Abstossung), 26,6 Grad nahe null (+0,0002/d^2).
- M-iso, Q-B/Q-B parallel: Fuehrend ist das Kreuzglied isotroper Teil mal deviatorischer Teil:
  E_inf ~ (-0,0034 cos 2 theta + 0,0003 cos 4 theta)/d^2, axial negativ, seitlich (90 Grad) positiv.
  60 Grad gedreht: etwa -0,0017 cos(2 theta - 60 Grad)/d^2.
- M-fcc, Q-A/Q-A: ~ 1/d^3, Vorzeichen in [100] und [111] verschieden (Analogie zu 2D, nicht gerechnet).
- M-iso4: wie M-iso schneller als 1/d^2.
- Untergrund b/N: in 2D bei n = 200 etwa 5e-7, also bei d = 50 groesser als ein 1/d^4-Signal. Ohne Abzug waere K1 nicht
  entscheidbar.

## 7. Ablauf (alles auf der .69 ueber kleintest.sh, Spur cpu6, je <= 600 s)

1. `pruef` (C1 bis C5, C7, Versionen, matplotlib vorhanden?) -> aus/pruef-<zeit>.json
2. `haupt2d` (M-iso, M-aniso2, M-iso4; drei Groessen) -> aus/haupt2d-<zeit>.json, .npz
3. `hauptfcc` (M-fcc; drei Groessen) -> aus/hauptfcc-<zeit>.json, .npz
4. `auswert` (Untergrund, Fits, K1 bis K5, C6, C8) -> aus/auswert-<zeit>.json
5. `bilder` -> aus/*.png
6. optional `rand` (fester Rand 2D)
- Jede Stufe schreibt neue Dateien mit Zeitstempel; nichts wird ueberschrieben. Ausgaben per rsync zurueck nach
  RUNDE-17/tetra-kopplung/aus/, Logs nach logs/.
