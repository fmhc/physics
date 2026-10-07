# DIM-BEUTEL Plan (Code-Agent, Runde 16)

- Geschrieben ab 2026-10-02 09:57:56 CEST (date), vor jedem .69-Lauf, vor jeder Syntaxpruefung und vor jedem Rauchtest.
- Zeitbox: Start 09:48:35 CEST, Ende spaetestens 11:18 CEST.
- Grundlage: KARTE.md (verbindlich und unveraendert: Modell, G1 bis G4, Messgroessen, D1 bis D5, Bedeutung).
- Vorgeschichte gelesen: beutel-1/KARTE.md, ERGEBNIS.md, PLAN.md, PLAN-NACHTRAG-1.md, Anfang von code/beutel.py.
  Die Graphversion schreibe ich neu (code/dimbeutel.py); vom BEUTEL-1-Code uebernehme ich nur die Konventionen.

## 1. Schreibtisch des Code-Agenten (vor dem Lauf)

- **Gradient** von E(phi, chi) = Q^2/(4 N) + phi^T L phi + (1/2) chi^T L chi + Sum[(1/4)(chi^2 - 1)^2 + 2 chi^2 phi^2],
  mit N = Sum phi^2 und L = D - A (Graph-Laplace, Kantengewicht 1):
  - dE/dphi = 2 [L phi + 2 chi^2 phi - omega^2 phi], mit omega = Q/(2 N).
  - dE/dchi = L chi + chi (chi^2 - 1) + 4 chi phi^2.
  - Vakuum chi = 1, phi = 0: Masse^2 von phi und chi je 2 (wie M3). Beutelkonstante B = 1/4.
- **Identitaet p + h = 1 (exakt, jeder Graph):**
  - Aus der phi-Stationaritaet (mit phi multipliziert und summiert) folgt phi^T L phi + 2 Sum chi^2 phi^2 = omega^2 N.
  - Daraus folgt E = omega Q + E_chi, mit E_chi = (1/2) chi^T L chi + Sum (1/4)(chi^2 - 1)^2.
  - Am Minimum gilt dE/dQ = omega (Einhuellendensatz). Also ist p_loc = d ln E/d ln Q = omega Q/E = 1 - h exakt.
  - Folge: h ist keine unabhaengige Messung, und d aus p/(1 - p) ist identisch mit d aus 1/h - 1. Die "Virial bzw.
    Huellenanteil"-Kontrolle ist damit dieselbe Zahl wie p. Unabhaengig prueft nur die Kette der Energien:
    p_fd = ln(E_k+1/E_k)/ln(Q_k+1/Q_k) gegen omega Q/E (also dE/dQ = omega). Das ist die eigentliche Kontrolle.
  - h = E_chi/E wie in BEUTEL-1 (enthaelt Volumen- und Wandenergie des chi-Felds).
- **Beutel auf dem Sierpinski-Dreieck (Selbstaehnlichkeit):**
  - Laenge x 2 gibt Knotenzahl x 3 und kleine Laplace-Eigenwerte x 1/5 (spektrale Dezimierung, mu' = mu (5 - mu)
    fuer L = 4 - A im Inneren [Schreibtisch]).
  - Ist Omega optimal bei Q, ist das doppelt so grosse Omega optimal bei Q' = 3 sqrt(5) Q = 6,708 Q, mit E' = 3 E
    (Wand- und Gitterkorrekturen vernachlaessigt).
  - Daraus folgt der Mittelwert p = ln 3/ln(3 sqrt 5) = 2 ln3/(2 ln3 + ln5) = 0,5772 = d_s/(d_s + 1). Das bestaetigt die
    Karte. Gleichzeitig folgt: p(Q) schwingt log-periodisch mit Periode Faktor 6,708 in Q [H].
  - Deshalb nehme ich ein Q-Gitter mit 12 Punkten je Periode und werte die Sekante ueber eine volle Periode aus.
- **Wandkorrekturen (Erwartung, nicht Wertung):** Mit Wandspannung sigma gilt E = A/R + b R^d + c R^(d-1). Daraus
  folgt p = d/(d+1) + O(sigma/(B R)), in 3D etwa -y/16 mit y = 3 sigma/(B R). BEUTEL-1 (Kontinuum) sah p von oben
  kommend (0,7593 bei Q ~ 900). Auf dem Gitter ist die chi-Wand nur etwa 1,4 Gitterabstaende dick. Haftung der
  Wand am Gitter (Peierls-Nabarro) kann Knicke in E(Q) geben.

## 2. Graphen und Startknoten

| Graph | Haupt | Groessenkontrolle | Startknoten |
|---|---|---|---|
| G1 Kette | n = 4096 | n = 8192 | Mitte |
| G2 Quadratgitter | 256 x 256, offener Rand | 192 x 192 | (L/2, L/2) |
| G3 kubisch | 64^3, offener Rand | 48^3 | (L/2, L/2, L/2) |
| G4 Sierpinski g = 10 | 88575 Knoten | g = 9 (29526 Knoten) | s1, Kontrolle s2 |

- Offener Rand: Der Graph wird so genommen, wie er ist; kein Knoten wird festgehalten. chi = 1 ist das Vakuum, die
  Randknoten haben weniger Nachbarn. Ob der Rand stoert, pruefen Groessenkontrolle und Randwerte.
- **Sierpinski-Graph der Generation g:**
  - Knoten sind ganzzahlige (a, b) mit a, b >= 0 und a + b <= 2^g.
  - Kleinste Dreiecke liegen bei (a, b) mit (a AND b) = 0 und a + b < 2^g (Pascal mod 2). Ihre Ecken sind (a, b),
    (a+1, b) und (a, b+1); jedes Dreieck hat 3 Kanten.
  - Daraus folgen (3^(g+1) + 3)/2 Knoten und 3^(g+1) Kanten (wird im Code geprueft). Lage x = a + b/2, y = b sqrt(3)/2.
- **s1 = (H, H) mit H = 2^(g-2)** (bei g = 10 ist das (256, 256)):
  - Der Knoten liegt in der Mitte der Seite des linken unteren Teildreiecks (Generation 1), die zum zentralen Loch
    zeigt. Er liegt also geometrisch im Inneren und hat Grad 4.
  - Er verbindet zwei Teildreiecke der Seitenlaenge H. Bis zum Graphabstand H sieht seine Umgebung exakt
    selbstaehnlich aus (zwei an einer Ecke verklebte Teildreiecke).
  - Abstand zur naechsten Aussenecke (Grad 2): 2H.
  - Begruendung: groesste selbstaehnliche Reichweite bei geometrisch innerer Lage.
- **s2 = (H + 8, 8)** (Kontrolle):
  - Ein Knoten niedriger Generation; er verbindet nur zwei Teildreiecke der Seite 8.
  - Ab Graphabstand 8 ist seine Umgebung nicht mehr selbstaehnlich zentriert.

## 3. Rechnung

- **Q-Gitter fuer alle Graphen:** Q_k = r^k mit r = (3 sqrt 5)^(1/12) = 1,17213. Zwoelf Schritte sind genau eine
  Sierpinski-Periode (Faktor 6,708).
  - Saat bei k_s = 40 (Q = 569), von dort aufwaerts bis K_max und abwaerts bis k = 0 (Q = 1), jeweils mit
    Fortsetzung (die Loesung bei Q_k ist der Start fuer Q_k+-1; phi wird dabei mit r^(+-1/(d+1)) skaliert).
  - K_max: G1 und G2 79 (Q = 2,8e5), G3 77 (Q = 2,0e5), G4 87 (Q = 9,8e5).
  - Kontrollen: 8192 bis 79; 192^2 bis 73 (Q = 1,1e5); 48^3 bis 70 (Q = 6,6e4); g = 9 bis 75 (Q = 1,5e5);
    s2 bis 87.
- **Startform A (Saat):**
  - Kugel vom Radius R0 um den Startknoten (Gitter euklidisch, Sierpinski Graphabstand).
  - Innen chi = 0, aussen 1; innen phi ~ 1 - (r/R0)^2, sonst 0.
  - R0 = Q^(1/(d+1)) (Gitter, nach Hinweis der Leitung mit 4B = 1); Sierpinski R0 = Q^0,4 (neutral, nur Startwert).
- **Startform B (Kontrolle):** Gauss-Klumpen phi ~ exp(-r^2/R0^2) mit chi = 1 ueberall. Der Beutel muss sich dann
  selbst bilden.
- **Minimierer:** scipy L-BFGS-B mit analytischem Gradienten, Schranke phi >= 0, Laplace als scipy.sparse-CSR.
  - Optional Jacobi-Skalierung der Variablen (aus der Hesse-Diagonale des Startpunkts je Q-Schritt).
  - Stopp: maximale Gradientenkomponente <= gtol (Ziel 1e-7) oder maxiter.
  - Skalierung ja/nein, gtol und maxcor lege ich nach dem Rauchtest fest und berichte sie. Physik, Graphen,
    Q-Gitter und Wertung aendern sie nicht.
- **Rauchtest:** zuerst kleine Graphen auf der .69 (Spur cpu), nur zur Laufzeit- und Konvergenzmessung.
  Rauchtest-Zahlen gehen nicht in die Wertung ein.
- **Je Punkt gespeichert:**
  - Q, E, omega, p_loc = omega Q/E, E_chi, h und der Identitaetsrest |E - omega Q - E_chi|/E.
  - Gradientennorm, Iterationen, chi am Startknoten, min chi und max phi.
  - V_bag = #(chi < 1/2), Volumenradius und groesster Graphabstand der Beutelknoten vom Startknoten.
  - Randwerte: max phi und max |1 - chi| ueber Knoten mit Graphabstand >= D_out. D_out ist bei Gittern der Abstand
    zum naechsten Rand minus 2; bei Sierpinski s1 ist D_out = H, bei s2 ebenfalls H.
  - Profile bei k = 40, 52, 64, 76 und 86 (soweit vorhanden). Gitter: Schnitt durch die Mitte; Sierpinski: alle
    Knoten mit Graphabstand.
- **Startform-Kontrolle:** frische Minimierung (ohne Fortsetzung) aus A und B bei k = 30, 50 und 70 (G4 auch 80,
  soweit im Bereich), Hauptgraph. Verglichen wird E mit dem Fortsetzungsast.
- **d_s-Direktmessung (Sierpinski):**
  - (a) Alle Eigenwerte von L fuer g = 7 und g = 8 (dicht, eigvalsh). Zaehlfunktion N(lambda); d_s/2 aus der Sekante
    ueber eine Spektralperiode: ln(N(lambda)/N(lambda/5))/ln 5 bei lambda = 0,3 x 5^(-j).
  - (b) Rueckkehrwahrscheinlichkeit der traegen Irrfahrt P = (I + D^-1 A)/2 von s1 und s2 auf g = 10, exakt per
    Matrix-Vektor-Produkten bis t = 5^6. Daraus d_s/2 = -ln(P(5t)/P(t))/ln 5.
  - Erwartung [L?]: d_s/2 = ln3/ln5 = 0,6826.
- **Literatur:** arXiv-API zu d_s des Sierpinski-Dreiecks, zu d_w = 2 d_H/d_s und zu Beutel-/FLS-Skalierung in d
  Dimensionen. Mindestens 6 s Abstand, bei HTTP 429 Abbruch.

## 4. Wertungsregeln (vor dem Lauf festgelegt)

- **Gueltiger Punkt (Beutelbereich nach oben):**
  - konvergiert: Gradient <= 10 x gtol und Identitaetsrest <= 1e-6;
  - min chi < 0,1 (Beutel vorhanden);
  - Randwerte max phi <= 1e-6 x max phi (Mitte) und max |1 - chi| <= 1e-6.
  - K_v ist das groesste k, bis zu dem alle Punkte ab k_s gueltig sind.
- **Wertungswerte je Graph (Hauptgraph):**
  - p* = ln(E(Q_Kv)/E(Q_Kv-12))/ln(6,708) (Sekante ueber die letzte volle Periode).
  - h* = Mittel von h ueber k = K_v - 12 bis K_v.
  - Dimension d_p = p*/(1 - p*) und d_h = 1/h* - 1.
- **Fehlerband:** delta p = |p* - p*_vor| + |Delta p_Groesse|.
  - p*_vor ist die Sekante ueber die Periode davor (K_v - 24 bis K_v - 12).
  - Delta p_Groesse ist der Unterschied von p_loc zwischen Haupt- und Kontrollgraph beim groessten gemeinsamen
    gueltigen Q.
  - delta d = delta p/(1 - p*)^2.
- **D1 bis D3:** eingetroffen, wenn |p* - Soll| <= 0,02 UND |h* - Soll_h| <= 0,03. Soll ist 0,50/0,50, 0,667/0,333
  bzw. 0,75/0,25.
- **D4:** eingetroffen, wenn p* naeher an 0,5772 liegt als an 0,6131, also p* < 0,5951. Berichtet werden zusaetzlich
  die Sekanten aller vollen Perioden im Plateau und dieselbe Zahl fuer s2 und fuer g = 9.
- **D5:** Fuer G1 bis G3 gilt:
  - Q_pl ist das kleinste Q_k, ab dem p_loc(Q_j) fuer alle j bis K_v innerhalb +-0,02 um p* liegt.
  - Die Plateaulaenge ist L_pl = log10(Q_Kv/Q_pl).
  - (a) "weicht deutlich ab": Es gibt einen gerechneten Punkt mit Q < Q_pl und |p_loc - p*| >= 0,05.
  - (b) L_pl(G3) < L_pl(G2) und L_pl(G3) < L_pl(G1).
  - Eingetroffen, wenn (a) fuer alle drei und (b) gelten. Fuer G4 wird dasselbe mit der Ein-Perioden-Sekante
    berichtet, aber nicht gewertet.
  - Vorbehalt: L_pl haengt von der gewaehlten Graphgroesse ab (K_v). Das wird im Ergebnis genannt.
- **Offen:** Erreicht ein Graph weniger als eine Dekade gueltiges Q oberhalb von Q_pl, oder bricht die Rechnung ab,
  ist die betreffende Vorhersage "offen".
- **Startform-Kontrolle:** bestanden, wenn |E_A - E_Ast|/E und |E_B - E_Ast|/E <= 1e-6. Liegt eine frische Loesung
  tiefer, ist das ein Konkurrenzzustand. Er wird berichtet, die Wertung bleibt aber auf dem Fortsetzungsast.
- **Groessenkontrolle:** bestanden, wenn |Delta E/E| <= 1e-6 und |Delta p_loc| <= 1e-4 im gemeinsamen gueltigen
  Bereich ab k_s.
- **dE/dQ = omega:** |p_fd - (p_loc,k + p_loc,k+1)/2| je Intervall, Median und Hoechstwert im gueltigen Bereich.
  Zusaetzlich Spline-Integral von omega Q ueber ln Q gegen E_Kv - E_ks.
- Zusatz (keine Wertung): Fit p_loc = p_inf + a Q^(-1/(d+1)) ueber das Plateau der Gitter.

## 5. Rechnen

- Code in dim-beutel/code/, per rsync nach /home/fmh/fmhc-physics-remote/runde16-dim-beutel/.
- Aufruf nur ueber kleintest.sh, Spuren cpu und cpu2, je Aufruf <= 600 s.
  - Das Skript bricht nach 540 s geordnet ab und schreibt jeden Punkt sofort (punkte.jsonl, Zustand als .npz).
  - Ein weiterer Aufruf setzt am letzten Zustand fort.
- Threads: OMP/OPENBLAS/MKL_NUM_THREADS = 1 vor dem numpy-Import.
- Lokal kein python/awk/bc. Syntaxpruefung per py_compile auf der .69.
- Reicht die Zeit nicht, verkleinere ich zuerst die Kontrollen (Q-Bereich, Startform-Punkte), dann K_max der
  Hauptlaeufe. Mindestens eine Dekade gueltiges Q je Graph.
- Abbildungen mit matplotlib auf der .69.
