# PACHNER-TAKT-1 mit TAKT-KOMMUTATOR-1: Plan (Code-Agent, Runde 41/42, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 17:01:54 CEST (date). Plantext ab 17:21:59 CEST (date), vor
  jeder Rechnung. Zeitbox 150 min, also bis 19:31 CEST.
- Grundlage: KARTE.md (PT0 bis PT3; Wortlaut, Schwellen und Wahrscheinlichkeiten unveraendert). Gelesen: TETRAEDER-L
  (Frage 3, K1, Gegensweep), Hoehn 2014 (quellen/F13, Abschn. 3, 4, 7, 9, 11), Dittrich/Hoehn 2012 (nur Abstract, F8),
  TAKT-UMBENENNUNG-L (Abschn. 4, 5, 8), TENSOR-EIS-PYRO-1 (PLAN, ERGEBNIS, tp.py), EINE-WELT-LOCH-1 (ERGEBNIS), RUNDE-36/REGEL.md.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [S] an der Quelle gelesen, [P] Projektdatei, [E] hier gerechnet,
  [F] Festlegung dieses Plans, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- Alles sind synthetische Gitterrechnungen, keine Messdaten.

## 1. Schreibtisch (vor jeder Rechnung)

### 1.1 Netz [M, F]

- Eine B1-Kopie (Kopie 1 aus TENSOR-EIS-PYRO-1): Ecken = Ab-Mitten (fcc), Staebe = Auf-Kanten in doppelter Laenge.
  Kubische Kante 1; Stablaenge a := 1/sqrt2 (Gitterweite fuer PT3); Oktaederdiagonale = 1.
- Zellen der Tetraeder-Oktaeder-Wabe je primitiver Zelle: zwei Tetraeder (tet2 = Finns Auf-Tetraeder vergroessert, tet1),
  ein Oktaeder. Jedes Oktaeder bekommt genau eine Diagonale und zerfaellt in 4 Tetraeder. Je primitiver Zelle dann
  V = 1, E = 7, Dreiecke 12, Tetraeder 6 (Euler 1 - 7 + 12 - 6 = 0) [M].
- Periodische Superzelle aus n x n x n kubischen Zellen, V = 4 n^3. n >= 2, damit keine Kante eine Ecke mit ihrem eigenen
  Bild verbindet (Diagonale = kubische Kante).
- Vier kubische Untergitter des fcc (Klassen 0, X, Y, Z nach der Paritaet von 2x). Naechste Nachbarn liegen immer in
  verschiedenen Klassen, beide Enden einer Diagonale in derselben. Ein Oktaeder beruehrt drei Klassen und verfehlt eine;
  seine drei Diagonalen tragen die drei beruehrten Klassen [M].
- Einbettung in den flachen euklidischen R^4 (Hoehn rechnet euklidisch [S, S. 4]): Raum x, Zeit t; jede Flaeche Sigma ist
  ein Graph t = h(x).

### 1.2 Linearisiertes kanonisches Regge nach Hoehn [S, M]

- Quadratische Wirkung um flach: H = -Summe_sigma M^sigma (+ Randterme mit d^2 A psi, die nur Kanten derselben Randflaeche
  koppeln und Omega nicht beruehren), M^sigma_ee' = Summe_t (dA_t/dl_e)(dtheta^sigma_t/dl_e'), Schlaefli macht M^sigma
  symmetrisch. Diederwinkel aus Eckkoordinaten (komplexer Schritt), d theta/dl = J C^+ wie tp.py.
- Globaler Schritt Sigma_0 -> Sigma_T: Innenkanten (bulk) eliminieren; Omega~ = Kreuzblock (Sigma_0 x Sigma_T) der
  effektiven Form. Nach Hoehn Abschn. 4 und 9 [S]: N_{0->T} = 2E - 2 #(Vorbedingungen bei 0) = 2 rank Omega~. Also:
  **r := rank Omega~ = Zahl der von Sigma_0 nach Sigma_T propagierenden Konfigurations-Gravitonen.**
- Vorbedingungen #pre = E_0 - r, Nachbedingungen #post = E_T - r. Eichteil G = Rang der Eckverschiebungen auf der Flaeche
  (4 je Ecke minus 4 globale Translationen auf dem Torus, falls die Flaeche geknickt ist) [M]. Nicht-Eich-Bedingungen
  = #pre - G_0 bzw. #post - G_T. Obergrenze r <= E - G = 3 je Zelle + global [M].
- Innenraum: Nullraum von H_ii; erwartet genau 4 je innerer Ecke (Eckverschiebung). Zusaetzliche Nullrichtungen n_x und
  ihre Kopplung an die Randdaten werden gemessen.

### 1.3 Reines C auf festen Ecken ist kein periodischer Takt [M]

- Ein 4-4-Wechsel d -> K im Oktaeder (2-3 fuegt K ein, 3-2 nimmt d heraus [S, Hoehn S. 6]) klebt die zwei 4-Simplizes
  "alle sechs Ecken ohne +m" und "ohne -m" (m = dritte Diagonale). Beide liegen vorwaerts (positive 4-Volumen, Region
  zwischen d-Flaeche und K-Flaeche) genau dann, wenn die Mittelpunktshoehe von K ueber der von d liegt [M].
- Reines C erzeugt und bewegt keine Ecke (2-3 und 3-2 aendern nur Kanten). Ein voller periodischer Takt bringt also
  dieselbe Flaeche an dieselbe Stelle zurueck, mit 4-Volumen null; jeder Vorwaertszug fuegt positives Volumen hinzu.
  Widerspruch. Gleichwertig: Der Rueckwechsel K -> d direkt danach braucht am neuen Innendreieck den Winkel 2 pi - theta
  > pi, also keinen flachen Simplex [M]. Summenregel: Summe ueber alle Oktaeder (Mitte_x - Mitte_z) = 0 fuer jede
  (auch geneigt-)periodische Hoehenfunktion, also koennen nie alle Oktaeder zugleich z -> x wechseln [M].
- Dasselbe gilt fuer B (1-4 und 4-1 an demselben Tetraeder ohne Bewegung der Ecken: Rueckfaltung) [M].
- **Folge:** Ein periodischer Takt auf festem Netz braucht Zeltstangen (Takt je Ecke, Lapse). Gerechnet werden deshalb
  C und B jeweils mit Zeltstangen (1.5). PT1 nach Kartenwortlaut (Lesart C = nur Diagonalwechsel, feste Ecken):
  **nicht eingetroffen [M]**; der Rechner prueft das nur nach (Kontrolle KC, Abschn. 2.4).

### 1.4 R4-Entscheidung fuer C [M]

- Ein Diagonalwechsel in einem Oktaeder der Kopie 1 erzeugt eine Kante zwischen zwei Ab-Mitten (beide Enden einer
  Diagonale in derselben Kopie, sogar derselben Klasse). Kanten zwischen Auf- und Ab-Mitten entstehen nie; die
  Auf-Mitten liegen in den tet2-Zellen der Kopie 1, nicht in ihren Oktaedern. Fuer Kopie 2 gilt dasselbe mit vertauschten
  Rollen. **C koppelt die beiden Welten nicht.** Die Zeltstangen (Ecke -> spaetere Ecke derselben Kopie) ebenso nicht.
  Gerechnet wird daher eine Kopie; die andere ist ihr Inversionsbild [M].

### 1.5 Takt-Varianten [F]

- Klassenfolge 0, X, Y, Z: Ein Schritt hebt alle Ecken einer Klasse um 1 (kubische Einheiten; Zeltzug Ecke fuer Ecke,
  v' = v + 1 e_t). Anfangshoehen 0 / 0,25 / 0,5 / 0,75 fuer 0 / X / Y / Z; die gerade gehobene Klasse ist danach die
  hoechste. Ein Takt = vier Schritte; danach ist jede Ecke genau einmal ersetzt, also Sigma_0 und Sigma_T kantenfremd.
- **TT** (Kontrolle): nur Zeltstangen, keine Wechsel.
- **C2** (Flip-Flop, Hauptvariante): Oktaeder, das Klasse M verfehlt, pendelt zwischen den Klassen M+1 und M+3 (zyklisch
  0, X, Y, Z); Wechsel zur Klasse K direkt nach dem Heben von K (vorwaerts nach 1.3, weil K dann am hoechsten liegt).
  Zwei Wechsel je Oktaeder und Takt.
- **C3** (Rundlauf, beschreibend): Wechsel zur Klasse K nach jedem Heben einer beruehrten Klasse; drei Wechsel je Takt.
- **B** (Kontrolle): Zu Taktbeginn 1-4 in jedem tet2 (neue Ecke im Schwerpunkt, Hoehe Mittel + 0,1), dann die vier
  Schritte, am Ende 4-1 an jeder neuen Ecke.
- Anfangsdiagonalen: der jeweils zuletzt erreichte Zustand (periodisch im Takt). Netto je Takt Delta E = Delta V = 0, also
  nach Hoehns Zaehlung Delta N_p = 0 fuer alle Varianten [M]. Gemessen wird die Propagation durch den Takt.

### 1.6 Kommutator (TAKT-KOMMUTATOR-1) [F, M]

- Ausgangsflaeche mit den Klassenhoehen 0 / 0,25 / 0,5 / 0,75 wie in den Takten (Superzelle n = 4), Diagonalen wie C2.
  A = Ecke in der Kastenmitte (Klasse 0), B = A + (1/2, 1/2, 0) (Klasse Z), naechste Nachbarn. Zeltzuege
  A -> A' = A + N_A e_t, B -> B' = B + N_B e_t. (Geaendert nach Rauchlauf r1, siehe Abschnitt 3: Auf einer ebenen
  Sigma_0 legen die Randlaengen die Normallage von A und B linear nicht fest, H_ii war singulaer.)
  - Reihenfolge AB: erst Zelt A auf Sigma_0, dann Zelt B auf Sigma_1 (enthaelt A'); BA umgekehrt. Beide Schichten haben
    denselben Rand (Sigma_0-Sterne von A, B unten, Sigma_2-Sterne von A', B' oben) und keine innere Ecke; sie
    unterscheiden sich in der Innenkante A'B gegen AB'.
  - Lokaler Takt (L): N_A = 0,3, N_B = 0,5. Globaler Takt (G): N_A = N_B = 0,4.
- **Definition:** Gleiche Randlaengen fuer AB und BA, Innenkanten nichtlinear nach Regge geloest (Newton). Kommutator
  D := || p^AB - p^BA ||_2 ueber alle Randkanten, p_e = dS/dl_e = Summe_t (dA_t/dl_e) (eps_t bzw. psi_t). Das ist
  Weg-Unabhaengigkeit der Hamilton-Jacobi-Funktion (gleiche Randdaten, Vergleich der Impulse = Enddaten bis auf eine
  umkehrbare lineare Abbildung). Beschreibend: |S^AB - S^BA| und der lineare Koeffizient D1 = ||Delta Q w|| aus den
  flachen Hesse-Formen.
- **Randdaten:** l_e = sqrt(E_e^T (1 + eps H(x_e)) E_e), E_e flacher 4D-Kantenvektor, x_e Kantenmitte; H raeumlich
  transversal-spurfrei, k = (2 pi/L) [100], H_yy = -H_zz = cos(k (x - x_A)). Ohne Kruemmung: Ecken flach verschoben
  X -> X + eps xi(X) mit glattem 4D-Feld xi (exakt flach einbettbar).
- Vorab [M]: Bei flachen Randdaten sind beide Loesungen flach, p ist eine Funktion der Randgeometrie allein, also D = 0
  (das ist die Kontrolle "ohne Kruemmung null"). Delta Q verschwindet auf allen flach einbettbaren Richtungen.
  Nicht ableitbar: ob Delta Q auf Kruemmungsrichtungen verschwindet (dann D ~ eps^2 oder hoeher), sonst D ~ eps; und der
  Exponent in a/L.

## 2. Messgroessen und Urteilsregeln (mechanisch in code/pt_auswertung.py)

### 2.1 Laeufe auf der .69 (kleintest.sh, Spuren cpu8 und cpu9; je <= 10 min, 1 Thread, 4 GB)

| Lauf | Inhalt |
|---|---|
| KC | Kontrolle reines C: Summenregel an 200 Zufallshoehen (n = 2), Rueckwechsel-Winkel an einem Oktaeder |
| T2 | Takte TT, B, C2, C3 bei n = 2, m = 1, 2, 3 Takte |
| T3 | Takte TT, B, C2, C3 bei n = 3, m = 1, 2, 3 (m = 3, weil der Rauchlauf weit unter 8 min liegt; aufgeteilt auf zwei Laeufe) |
| T4 | beschreibend, in keiner Regel: TT und C2 bei n = 4, m = 1, 2 (Zellrate mit drei Groessen) |
| KO | Kommutator: Varianten L und G; eps in {1e-3, 3e-3, 1e-2, 3e-2} bei L/a = 4; L/a in {4, 8, 16, 32} bei eps = 1e-3; flache Kontrolle bei eps = 3e-2 |
| AW | Auswertung |

- Je Takt-Fall: E, V, G_0, G_T, r_m (Rang mit Schwelle 1e-9 mal groesster Singulaerwert, dazu die Luecke
  s_r/s_{r+1}), #pre, #post, n_innen (innere Ecken), Nullraum von H_ii, n_x, Kopplung der Zusatz-Nullrichtungen an den
  Rand (relativ), kleinstes 4-Volumen (relativ), groesster Innen-Fehlwinkel, Eichprobe ||Omega~ Y|| (relativ).

### 2.2 Urteilsregeln

- **PT0** ("Kontrollen: Lesart B gibt 0 Gravitonen; ohne Kruemmung ist der Kommutator null (auf 1e-10); mit Kruemmung
  waechst er wie eps^2 (Steigung 1,8 bis 2,2)"). Eingetroffen genau dann, wenn alle drei gelten:
  - (a) B: r_B(m) = r_TT(m) und n_x(B) = n_x(TT) fuer alle gerechneten (n, m). "0 Gravitonen" heisst: Die 1-4- und
    4-1-Zuege aendern gegenueber dem reinen Zeltstangen-Takt weder die propagierenden noch die freien Groessen.
  - (b) D(flach, eps = 3e-2) / ||p|| <= 1e-10 in L und G.
  - (c) Steigung von log D gegen log eps (Variante L, L/a = 4, Ausgleichsgerade ueber die vier eps) in [1,8; 2,2].
  - Nach Plan = nach Kartenwortlaut.
- **PT1** ("Lesart C ist auf dem festen periodischen Netz als Takt konsistent: Nach einem vollen Takt sind die
  Zwangsbedingungen wieder loesbar, und ihr Rang ist gleich").
  - Nach Plan (C2 mit Zeltstangen): eingetroffen genau dann, wenn fuer n = 2 und n = 3
    1. realisierbar: kleinstes 4-Volumen > 1e-8 relativ und groesster Innen-Fehlwinkel <= 1e-10;
    2. loesbar: jede Nullrichtung von H_ii, die keine Eckverschiebung ist, koppelt hoechstens 1e-8 relativ an den Rand;
    3. Rang gleich: r_1 = r_2 (und = r_3, wo gerechnet), also gleich viele Bedingungen nach jedem Takt.
  - Nach Kartenwortlaut (reines C, feste Ecken): nicht eingetroffen [M] nach 1.3, sofern KC die Summenregel
    (Mittelwert der Differenzen <= 1e-12) und den Rueckwechsel-Winkel > pi bestaetigt; sonst "unklar".
- **PT2** ("Ein C-Takt traegt je Zelle mindestens ein propagierendes Graviton (nicht nur Eichung)"). Nach Plan (C2) =
  nach Kartenwortlaut: eingetroffen genau dann, wenn beim groessten gerechneten m (fuer beide n gleich)
  r_m(n)/V(n) >= 1 fuer n = 2 und 3 und die Zellrate (r_m(3) - r_m(2))/(V(3) - V(2)) >= 1 und die Eichprobe
  ||Omega~ Y|| <= 1e-9 relativ gilt (dann zaehlt r nur eichinvariante Groessen).
- **PT3** ("Lokaler Takt: Der Kommutator faellt mit der Gitterweite wie (a/L)^p mit p zwischen 3 und 5"). Nach Plan =
  nach Kartenwortlaut: p = Steigung von log D gegen log(a/L), Variante L, eps = 1e-3, L/a in {4, 8, 16, 32}
  (Ausgleichsgerade); eingetroffen genau dann, wenn p in [3; 5] und D bei L/a = 4 ueber 1e-13 liegt (sonst "unter
  Rundung", Urteil nicht eingetroffen).

### 2.3 Agenten-Vorhersagen (vorab; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| V1 | TT: r = E - G an allen (n, m) (Zeltstangen propagieren alles); G = 4V - 4; n_x = 0 |
| V2 | B: r_B = r_TT; 4 Nullrichtungen je innerer Ecke, n_x = 0 |
| V3 | C2: r = E - G an allen (n, m) (jeder 3-2 legt das frische Graviton des 2-3 fest, Hoehns Fall b), also PT1 und PT2 nach Plan eingetroffen (60 %) |
| V4 | Kommutator: D1 > 0, also D ~ eps (Steigung 0,9 bis 1,1); PT0 an (c) verfehlt (55 %) |
| V5 | p liegt in [1,8; 2,2] (Kruemmung ~ (a/L)^2, D linear darin); PT3 verfehlt (40 %) |
| V6 | KC: Summenregel exakt (<= 1e-12), Rueckwechsel-Winkel 2 pi - theta > pi |

### 2.4 Kontrollen (technisch, gehen ueber die Urteile hinaus)

- Zellen: Schlaefli (Summe_t A_t d theta_t/dl = 0 je Simplex) <= 1e-12; M^sigma symmetrisch <= 1e-12 relativ.
- Flachheit: alle Innendreiecke Winkelsumme 2 pi (<= 1e-10).
- Eichung: H Y_v = 0 fuer innere Ecken (<= 1e-10 relativ); Omega~ annulliert Rand-Eckverschiebungen.
- Kommutator: Newton-Rest <= 1e-13 relativ; bei eps = 0 sind beide Schichten bitgleich flach.

## 3. Rauchlauf und Einfrieren

- Rauchlauf: kleine Faelle (n = 2, m = 1; Kommutator mit zwei eps und zwei L), nur Zeit, Speicher, Kontrollen und
  Schluessel ansehen; keine Ranks, keine D-Werte, keine Urteile lesen. Danach PLAN.md und code/ als .eingefroren-<zeit>
  kopieren, sha256 in EINGEFROREN-SHA256.txt.
- Faellt ein Fall an der 600-s-Grenze: n = 3 nur mit m = 1, 2; das wird in ERGEBNIS vermerkt. Vorab festgelegt.
- **Rauchlauf r1** (cpu8/cpu9, 15:31:42 bis 15:31:45 UTC, pt.py 17df4d92...): Takte TT, B, C2, C3 bei n = 2, m = 1
  und kc liefen (je unter 2 s, 64 MB). Gelesen nur: Schlaefli <= 1,9e-15, M symmetrisch <= 2,1e-15, kleinstes
  4-Volumen relativ >= 7,9e-4, Innen-Fehlwinkel <= 1,8e-15, H Y_innen 2,8e-16 (B), keine Kantenueberlappung,
  E = 224 = 7 V, 192 = 6 V Tetraeder auf beiden Flaechen, Zugzahlen; bei kc nur die Schluessel. Nicht gelesen: r, G,
  Nullraeume, n_x, kc-Werte. Der Kommutator brach ab: H_ii singulaer auf ebener Sigma_0 (Normallage von A, B linear
  frei). Aenderung: geknickte Ausgangsflaeche (1.6).
- **Rauchlauf r2** (cpu9, 15:32:47 bis 15:32:56 UTC, pt.py 16baf5d6...): Kommutator mit eps 1e-2, 3e-2 und L/a 4, 8.
  Gelesen nur: 48 Simplizes, 3 Innenkanten, 111 Randkanten, keine innere Ecke, keine Kastenueberschreitung, flach
  Innen-Fehlwinkel <= 8,9e-15, Gradient <= 9,6e-15, Konditionszahl H_ii 2,2 bis 4,2, Newton-Rest <= 8,3e-15 (die
  Schwelle 1e-15 im Code wird an der Rundungsgrenze nicht erreicht, dann 40 Schritte; harmlos), D bei eps = 0
  relativ 1,1e-15 (Kontrolle). Nicht gelesen: D, D_rel, D1, dQ, Steigungen.
- Danach im Code: Schur-Komplement ohne dichte Pseudoinverse (gleiche Rechnung, weniger Aufwand), neuer Lauf T4.
- **Rauchlauf r3** (cpu8, pt.py bc360991..., pt_auswertung.py 1f41ab03...): ganze Kette klein (Takte n = 2, m = 1, 2;
  kc; Kommutator mit zwei eps und zwei L; Auswertung). Gelesen nur Rueckgabewerte (alle 0), Laufzeiten (Takte bis 6 s,
  Kommutator 9 s) und die Schluessel der auswertung.json. Keine Zahl und kein Urteil gelesen.
- Eingefroren ab 2026-10-04 17:34:34 CEST (date); Kopien mit Endung .eingefroren-20261004-173434.
