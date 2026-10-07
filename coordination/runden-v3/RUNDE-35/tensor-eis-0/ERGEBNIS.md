# TENSOR-EIS-0: Ergebnis (Runde 35, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
  - Start 2026-10-03 21:37:48 CEST.
  - Plan eingefroren 21:59:34 CEST.
  - Hauptlaeufe 21:59:45 bis 22:02:48 CEST.
  - Datei geschrieben ab 22:03:56 CEST (date).
- Alle Zahlen stammen aus Rechnungen auf der .69 (lauf-69/), es sind keine Messdaten.
- Kennzeichen:
  - [L] Literatur, [L?] Literatur ungeprueft, [S] an der Quelle gelesen, [H] Hypothese
  - [M] Mathematik, vorab ableitbar
  - [A] Festlegung des Agenten

## Ergebnis zuerst

1. **Die Schreibtischformeln der Leitung stimmen.** [M, numerisch bestaetigt]
   - Im Fourierraum stimmen alle Formeln der Karte mit der unabhaengigen Pseudoinversen-Loesung auf 3e-15 ueberein
     (mit q ersetzt durch k = 2 sin(q/2)): Energiekern, explizite Laengsloesung E, |E|^2, Skalarkern 1/k^4 bzw.
     3/(2k^4).
   - Im Ortsraum trifft U nach Endlichkeitskorrektur die Formel (2Kp^2/(4 pi r))(7/8 + cos^2 theta/8): hoechstens
     2,54 % Abweichung ab r = 4, 0,52 % ab r = 8, 0,22 % ab r = 12.
2. **Gleichartige Vektorladungen stossen sich an allen 188 gemessenen Abstandsvektoren ab** (15 Richtungen,
   r = 2 bis 16,5; T1 eingetroffen).
   - Laengs p ist die Abstossung um 8/7 staerker als quer; endlichkeitskorrigiert ergibt sich 1,1448 statt 1,1429.
   - Ungleiche Skalarladungen sind linear gebunden: Steigung 0,03989 gegen 1/(8 pi) = 0,03979, Aenderung zwischen
     r = 8 und 16 nur -0,1 %.
   - Eine Anziehung gleicher Ladungen gibt es in dieser einfachen Tensorphase nicht.
3. **Woertlich auf L = 64 sind T0, T2 und T3 nicht eingetroffen.**
   - Ursache ist allein der Torushintergrund: q = 0 ausgelassen, Ewald-Verschiebung -(2/(4 pi))(11/12)(2,8373/L).
   - Das stand vorab im Plan, mit Zahl.
   - Alle vier Agenten-Vorhersagen dazu sind eingetroffen. Der gemessene 1/L-Koeffizient liegt zwischen -0,41385 und
     -0,41410; vorhergesagt war -0,41394.
   - Mit denselben Schwellen an endlichkeitskorrigierten Werten (Z0 bis Z3, vorab festgelegt) ist alles eingetroffen.
4. **Warnung fuer TENSOR-EIS-1 (Monte Carlo):** Auf einem kleinen Torus erzeugt der Hintergrund eine Scheinanziehung
   gleicher Ladungen.
   - Bei L = 32 sind 44 von 189 Abstaenden negativ, ab etwa r = 12.
   - Eine dort "gesehene" Anziehung waere ein Rechenartefakt.
5. **Pinch-Punkte (T4 eingetroffen):** vierzaehlig in [hk0], zweizaehlig in [0kl], wie Fig. 1b/c von Yan u. a. [S].
   Gl. 17 der Quelle ist auf 1,6e-15 genau der numerische Transversalprojektor.

## Urteile

| Nr | Karte | Urteil (woertlich, L = 64) | Zusatz endlichkeitskorrigiert [A] |
|---|---|---|---|
| T0 | Gauss und Spur auf 1e-10; Gitter-U trifft die Kontinuumsformel ab r >= 4 auf 3 % | **nicht eingetroffen**: Gauss 1,2e-15 und Spur 2,4e-16 erfuellt, aber U bis -72 % daneben (Torus) | Z0 **eingetroffen**: max 2,54 % (bei (0,0,4)) |
| T1 | U > 0 fuer alle r >= 2 und Richtungen (parallel) | **eingetroffen**: min U = 0,00237 bei (16,0,4) | Z1 **eingetroffen**: min 0,00852 |
| T2 | U(0)/U(90 Grad) bei r = 8 = 8/7 auf 3 % | **nicht eingetroffen**: 1,2308 (+7,7 %) | Z2 **eingetroffen**: 1,1448 (+0,17 %) |
| T3 | Ungleiche Skalare: U(r) - U(4) linear, Steigung 8 bis 16 aendert sich < 10 % | **nicht eingetroffen**: -17,6 % / -16,5 % / -16,0 % fuer (100)/(110)/(111) | Z3 **eingetroffen**: -0,13 % / -0,10 % / -0,10 % |
| T4 | Vierzaehliger Pinch-Punkt in [hk0], zweizaehliger in [0kl] | **eingetroffen** | - |

| Nr | Agenten-Vorhersage (vorab, PLAN Abschnitt 6) | Ergebnis |
|---|---|---|
| A1 | Roh-L64 minus korrigiert = -0,00647 (+-15 %) fuer alle 4 <= r <= 16 | eingetroffen: -0,00645 bis -0,00607 |
| A2 | 1/L-Koeffizient b = -0,4139 (+-10 %), richtungsunabhaengig | eingetroffen: -0,41410 bis -0,41385 |
| A3 | T3 woertlich, Verhaeltnis laengs (100) etwa 0,84, Fenster 0,75 bis 0,92 | eingetroffen: 0,824 |
| A4 | L = 32: U(16,0,0) < 0 (Scheinanziehung) | eingetroffen: -0,00106 |

## Tabellen

**Parallele Vektorladungen (p = z, K = p = 1), Groessenreihe und Korrektur**

| v | Kontinuum | L = 32 | L = 64 | L = 128 | L = 256 | korrigiert | korr./Kont. - 1 |
|---|---|---|---|---|---|---|---|
| (0,0,4) | 0,039789 | 0,028053 | 0,034355 | 0,037568 | 0,039183 | 0,040799 | +2,54 % |
| (4,0,0) | 0,034815 | 0,022597 | 0,028944 | 0,032163 | 0,033778 | 0,035395 | +1,66 % |
| (0,0,8) | 0,019894 | 0,007845 | 0,013623 | 0,016775 | 0,018382 | 0,019997 | +0,52 % |
| (8,0,0) | 0,017408 | 0,005124 | 0,011069 | 0,014243 | 0,015853 | 0,017469 | +0,35 % |
| (0,0,16) | 0,009947 | 0,000857 | 0,003882 | 0,006772 | 0,008348 | 0,009960 | +0,13 % |
| (16,0,0) | 0,008704 | -0,001061 | 0,002538 | 0,005511 | 0,007098 | 0,008712 | +0,09 % |

- Korrigiert heisst: exakte Loesung von U_L = a + b/L + c/L^3 mit L = 128, 192 und 256.
- Unsicherheit (Abstand zur gleichen Anpassung mit 64, 128 und 256): hoechstens 3e-4 relativ.
- Die Restabweichung bei r = 4 ist Gitternahfeld (Punktladung auf einem Link). Sie faellt wie 1/r^2.
- Bild: lauf-69/bild-U-theta.png (Formfaktor U * 4 pi r / 2 gegen theta, alle 188 Punkte mit r >= 4) und
  lauf-69/bild-U-r.png.

**Ungleiche Skalarladungen (6 Freiheitsgrade), Steigungen der Ausgleichsgeraden**

| Richtung | roh L = 64: [8,12] -> [12,16] | Aenderung | korrigiert: [8,12] -> [12,16] | Aenderung |
|---|---|---|---|---|
| (100) | 0,02803 -> 0,02310 | -17,6 % | 0,03989 -> 0,03984 | -0,13 % |
| (110) | 0,02841 -> 0,02373 | -16,5 % | 0,03987 -> 0,03983 | -0,10 % |
| (111) | 0,02890 -> 0,02427 | -16,0 % | 0,03986 -> 0,03982 | -0,10 % |

- Kontinuum: 1/(8 pi) = 0,03979.
- Der Torus erzeugt einen r^2-Term (xi/(24 pi L)) r^2. Er ist keine Konstante und faellt deshalb in U(r) - U(4) nicht
  heraus.
- Bild: lauf-69/bild-skalar.png.

**Weitere Konfigurationen (Zusatz)**

- **Antiparallel:** U = -U(parallel) auf 2e-16, alle negativ (Anziehung).
- **Senkrecht** (p1 = z, p2 = x):
  - Das Vorzeichen wechselt mit dem Winkel, wie die Karte sagt: s = (8,5; 0; 7,5) gibt +0,00084, s = (8,5; 0; -8,5)
    gibt -0,00079.
  - Abweichung von (2/(4 pi |s|))(1/8) s_z s_x/|s|^2 hoechstens 1,1 % der Parallelskala, schon roh auf L = 64. Die
    isotrope Torusverschiebung faellt bei p1 senkrecht p2 heraus.
- **Gleiche Skalarladungen:** U(gleich) = -U(ungleich) auf 2e-16. Das ist eine konstante abstossende Kraft 1/(8 pi)
  (korrigiert); roh auf L = 64 ist sie geschwaecht, um 30 % (r = 8 bis 12) und 42 % (r = 12 bis 16).
- **Skalar spurfrei / ohne Spur:** U5/U6 = 1,5000 exakt, auch auf dem Gitter [M].

**Pinch-Punkte** (lauf-69/bild-pinch.png)

| Ebene | Keulen / Nullstellen auf eps = 0,02 / 0,05 / 0,1 | eps-Abhaengigkeit | Abstand zu Gl. 17 | Maximum |
|---|---|---|---|---|
| [hk0] | 4/4, 4/4, 4/4 | 2,0e-4 | 1,0e-6 | 1/8 (Diagonalen), Nullen laengs h und k |
| [0kl] | 2/2, 2/2, 2/2 | 7,7e-5 | 1,6e-6 | 1/2 (laengs l), Nullen laengs k |

- **Bildvergleich mit Fig. 1b/c** [S]:
  - Fig. 1b zeigt in [0kl] einen zweizaehligen Pinch-Punkt, Fig. 1c in [hk0] einen vierzaehligen. Fig. 1d (Monte
    Carlo, q_x-q_y) zeigt ein dunkles Achsenkreuz mit hellen Diagonalkeulen. Das ist dasselbe Muster wie unser
    [hk0]-Bild.
  - Dass Fig. 1c insgesamt dunkler wirkt als 1b, passt zu den Maxima 1/8 gegen 1/2.
  - Unsere Karten sind je Ebene auf ihr eigenes Maximum normiert; die Helligkeit ist zwischen den Ebenen also nicht
    vergleichbar, die Profile zeigen die absoluten Werte.

## Kontrollen

- **Gauss-Gesetz im Ortsraum:** Rest hoechstens 1,2e-15 ueber alle Ortsraumloesungen (L = 32 und 64; Vektor,
  Skalar, Einzelladungen).
- **Spur** (Bezug max |E|):
  - 6er-Kontrolle mit Spurzeile (nichttrivial): 2,4e-16
  - 5er-Basis: 2,7e-16 (per Konstruktion)
  - Abstand der 5er- zur 6er-Loesung: 5,6e-17
- **Parseval** (Ortsraum gegen Fourierraum): 4,4e-16 relativ. Imaginaerteile hoechstens 8,9e-17.
- **Kernweg gegen Ortsraumweg:** 2,0e-16 (L = 32) und 2,8e-16 (L = 64). pinv bei q = 0 ist exakt 0.
- **Nachtrag nach dem Einfrieren** (code/te0_nachtrag.py, lauf-69/nachtrag-fourier.json; kein Urteil):
  - 20000 zufaellige q, Schreibtischformeln der Karte gegen pinv:
    - Kern 3,2e-15, E-Formel 2,3e-15, |E|^2 2,5e-15
    - die E-Formel der Karte erfuellt Gauss (1,4e-15) und Spur (1,8e-15)
    - Skalarkerne 1,8e-15 und 2,7e-15
  - Gl. 17 gegen 1 - pinv(Bm) Bm: 1,6e-15. Projektor idempotent (1,2e-15), Spur 2 (zwei Querfreiheitsgrade).
- **Latten:**
  - L1 (kann scheitern): nur durch einen Schreibtischfehler. Der Ausgang war vorab ableitbar [M]; das ist eine
    Rechnungspruefung, kein harter Test.
  - L2 (Gegenprobe): 6er-Kontrolle, zwei Wege, Groessenreihe, A1 bis A4.
  - L3 (Numerik): 1e-15.
  - L4 (schon bekannt): Gl. 17 [S], Pretko-Fraktonen [L].
  - L5 (Messbezug): keiner. Der Messbezug laeuft nur ueber die Pinch-Punkte (Neutronenstreuung bei Yan u. a. [S]),
    nicht ueber U(r).

## Pruefung der Schreibtischherleitung

- **Kein Fehler gefunden.** Jede Zeile des Schreibtischs ist bestaetigt, ausserdem auf dem Gitter mit q ersetzt
  durch k = 2 sin(q/2):
  - Laengsloesung
  - Spur- und Gauss-Eigenschaft
  - |E|^2 = (2/q^2)(rho^2 - (q_dach.rho)^2/4)
  - G_ij = (1/(4 pi r))[(7/8) delta + (1/8) r_dach r_dach]
  - U(r, theta) mit Faktor 8/7
  - Vorzeichen fuer antiparallel und senkrecht
  - Skalarkern und lineares U
- **Zwei Luecken im Testentwurf der Karte, keine Formelfehler:**
  1. **Torushintergrund beim Vektorfall.** Die Karte verlangt den Vergleich bei L = 64. Bei ausgelassenem q = 0
     verschiebt sich U dort isotrop um -0,00647 K p^2. Das sind 17 % bei r = 4 und 71 % bei r = 16 (quer zu p). Auch das
     Verhaeltnis in T2 kuerzt die Verschiebung nicht.
  2. **Torushintergrund beim Skalarfall.** Der Hinweis der Leitung "q = 0 bestimmt nur die Konstante" stimmt fuer den
     Skalarfall nicht ganz. Der Torus gibt auch einen Term proportional zu r^2/L, und U(r) - U(4) entfernt ihn nicht.
- **Kleine Unschaerfe:** "Gleiche Skalarladungen: konstante Abstossung" gilt fuer die Kraft im unendlichen Raum. Auf
  dem Torus ist sie abstandsabhaengig geschwaecht.

## Bedeutung

- **Rechnung, keine Messung:** In der Gaussschen Tensor-Coulomb-Phase ziehen sich gleichartige Ladungen nicht an,
  weder Vektor- noch Skalarladungen.
  - Vektorladungen stossen sich in jeder Richtung ab, laengs um 8/7 staerker.
  - Ungleiche Skalarladungen sind linear gebunden.
  - Damit gilt die Bedeutung der Karte fuer "T1 bis T3 treffen ein" in ihrer endlichkeitskorrigierten Form: Der Weg
    "Kraefte in den Staeben -> Schwerkraft" braucht eine zusaetzliche Zutat [H], etwa Energiekopplung ueber die
    Geometrie (LAPSE-0) oder Fraktonendynamik [L?].
- **Nicht abgedeckt:**
  - nichtgausssche Effekte (Wechselwirkungen jenseits von F = (K/2) E^2, Ordnung aus Unordnung)
  - Gitter mit anderer Geometrie als kubisch, etwa Pyrochlor oder Finns Tetraeder. Fuer grosse Abstaende erwarte ich
    dasselbe Kontinuumsergebnis [H].
- **Praktisch fuer TENSOR-EIS-1:**
  - Defektpaare im Monte Carlo auf einem Torus brauchen eine Endlichkeitskorrektur.
    - Mindestens eine Groessenreihe, oder Abstaende r << L.
    - Den Hintergrundterm -(2/(4 pi))(11/12) 2,837/L abziehen.
  - Sonst erscheint bei r > L/3 eine Scheinanziehung.

## Selbstanzeigen

1. **T1-Bereich:**
   - Die Plantextzeile nennt 2 <= |v| <= 16. Der eingefrorene Code nimmt die ganze Parallelliste bis |v| <= 16,5,
     also zusaetzlich (7,7,13), (11,11,5) und (13,7,7) mit 16,34 sowie (4,0,16) und (16,0,4) mit 16,49.
   - Das ist strenger (mehr Punkte); der kleinste Wert liegt genau dort und ist positiv. Ohne diese Punkte bliebe T1
     ebenfalls eingetroffen.
2. **Nachtrag nach dem Einfrieren:**
   - code/te0_nachtrag.py ist nach dem Einfrieren geschrieben und gelaufen. Es ist offengelegt, ohne Urteil und
     aendert keine Urteilsregel.
   - Der eingefrorene Code (te0.py, te0_auswertung.py) blieb nach dem Einfrieren unveraendert; die Pruefsummen der
     .69-Fassung stimmen mit EINGEFROREN-SHA256.txt ueberein.
3. **Vor dem Einfrieren gesehen:**
   - Das Probe-Bild aus rauch2 (L = 24, Anpassung 32/48/64) zeigte schon: roh weit unter dem Kontinuum, korrigiert
     nahe dran. Offengelegt im PLAN, Abschnitt 7.
   - Die Abschnitte 4 bis 6 des Plans standen davor; Schwellen und Regeln wurden nicht geaendert.
4. **Zweistufige Urteile:**
   - Die Aufteilung in woertliche Urteile und Zusatz Z0 bis Z3 ist meine Festlegung [A]. Ich habe sie getroffen, weil
     die woertliche Fassung bei L = 64 vorab erkennbar am Torus scheitert.
   - Die Leitung kann entscheiden, welche Ebene zaehlt. In auswertung.json stehen unter "urteile" die woertlichen.
5. **kern-b auf Spur p4000a:**
   - Der Lauf rechnete reines CPU-numpy auf Spur p4000a und hielt deren Lock etwa 3 min, ohne die GPU zu nutzen.
   - Zulaessig nach Auftrag (Spuren cpu und p4000a), aber die GPU-Spur war dadurch belegt.
6. **Scheinbare Ueberlappung:**
   - Ich hielt kurz einen Ueberlapp von N1 und R1 auf Spur cpu fuer moeglich: Das "start"-Echo des Starters steht vor
     dem Lock.
   - Das Journal zeigt: N1 startete 20:01:07,19 UTC, nach dem Ende von R1 um 20:01:07,17. Zu keinem Zeitpunkt liefen
     mehr als zwei Laeufe.
7. **Ewald-Konstante:** xi = -2,837297 ist Literatur [L] aus dem Gedaechtnis, nicht an einer Quelle gelesen. Sie wird
   nur fuer A1 und A2 benutzt; der gemessene 1/L-Koeffizient bestaetigt sie auf 4e-4.
8. **Bilder:** Die feste Bildbeschriftung "L = 64" stimmt fuer die Hauptlaeufe. Im Probe-Bild (rauch-69/p/) war sie
   falsch (dort L = 24).

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261003-215934, EINGEFROREN-SHA256.txt
- code/:
  - te0.py: Rechnung
  - te0_auswertung.py: Urteilsregeln und Bilder
  - te0_nachtrag.py: nach dem Einfrieren, offengelegt
- lauf-69/:
  - auswertung.json
  - explizit.json, kern-a.json, kern-b.json, pinch.json/npz, nachtrag-fourier.json
  - Bilder bild-U-theta.png, bild-U-r.png, bild-skalar.png, bild-pinch.png
- rauch-69/: Rauchlaeufe (Zahlen ohne Urteilswert)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde35-tensor/ (code/, rauch/, lauf/)

## Einfach gesagt

Finn fragt, ob Kraefte in Staeben Schwerkraft ergeben koennen. Wir haben dazu ein Gitter durchgerechnet, in dem jeder
Stab eine Spannung traegt und an jedem Knoten die Kraefte im Gleichgewicht sein muessen (wie beim Tetraeder-Stabwerk).
Zwei gleiche "Stoerstellen" in so einem Gitter stossen sich immer ab, in jeder Richtung, laengs ein bisschen staerker
als quer; das ist das Gegenteil von Schwerkraft, bei der sich Massen anziehen. Auf einem zu kleinen Rechengitter sah es
bei grossem Abstand zwar nach Anziehung aus, aber das war ein Randeffekt der Rechnung, und er verschwindet, wenn man
das Gitter vergroessert. Kraefte in Staeben allein geben also keine Schwerkraft; es braucht noch eine weitere Zutat.
