# DANZER-NAEHERUNG-1: Plan (Runde 46, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Karte KARTE.md (bindend; N1 bis N3 und ihre Bedeutung unveraendert).
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):** Start 2026-10-05 06:47:23 CEST. Code ab etwa 07:08 CEST, dieser Plan
  ab 07:18:47 CEST. Zeitbox 150 min, also bis 09:17 CEST.
- **Vor diesem Plan liefen drei Rauchtests** ueber kleintest.sh (cpu5; 05:11:56, 05:16:26 und 05:18:18 UTC; je 30 bis
  60 s). Sie geben nur Bau, Kontrollen und Zeiten aus, keine a2-Werte. Was ich daraus vor dem Plan weiss, steht in
  Abschnitt 7 (Vorab-Kenntnis). Rauchtest 3 senkte die Ritz-Regularisierung von 1e-6 auf 1e-9 (Gegenprobe unveraendert
  4,4e-8 / 9,2e-9 / 3,1e-9 relativ; der Rest ist die Abbruchordnung der k.p-Basis).
- **Nach dem Planentwurf, vor dem Einfrieren:** Rauchtest 4 (rechnen 1/1 S,M Saat 0, 30 Richtungen, 5 s) und
  Rauchtest 5 (auswerten darauf, 2 s), 05:20:43 bis 05:20:51 UTC, nur als Durchlaufprobe der beiden Pfade. Geprueft habe
  ich nur Rueckgabecode (0) und "Traceback/Error" per grep (0 Treffer); Werte habe ich nicht gelesen.
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [E] gerechnet, [P] Projektdatei, [F] Festlegung dieses Plans,
  [H] Hypothese, [R] aus dem Rauchtest (vor dem Plan gesehen).
- Alles ist synthetische Rechnung an gedachten, unendlich periodischen Netzen. Keine Messdaten.

## 0. Gelesen (vor dem Plan)

- KARTE.md; DANZER-L/DOSSIER.md Abschnitte 1, 3, 4, 6; GEGENLESEN-R45 Teil C (haelt; V-6 betrifft nur den
  Laengsschall mit mitlaufenden Phasonen, hier nicht gerechnet); LICHT-FINN-NETZ-1 ERGEBNIS, PLAN, code/licht_netz.py;
  HODGE-L/DOSSIER.md Abschnitt 1 ("In 3D genuegt Delaunay fuer positive umkreisbasierte Hodge-Sterne aller Grade",
  Hirani/Kalyanaraman/VanderZee 2013).
- Kein Projekt-grep ueber die Karte hinaus (Karte: keine Danzer-, Naeherungs- oder Phason-Rechnung im Projekt).

## 1. Bauweg [F]: Schnitt- und Projektionsmenge aus Z^6, periodische Delaunay-Zerlegung (Zusatz der Leitung)

- **Wahl:** der einfachste Weg der Karte (Zusatz Leitung). Danzer aus D6 und die symmetrische Rhomboeder-Zerlegung
  baue ich in der Zeitbox nicht. Grund fuer die zweite [M]: Eine flaechengleiche Zerlegung aller Rhomboeder in
  Tetraeder ohne Zusatzpunkte, die zugleich die Rhomboeder-Symmetrie achtet, gibt es nicht (lange Diagonalen im
  spitzen, kurze im stumpfen Rhomboeder passen an gemeinsamen Flaechen nicht zusammen).
- **6D-Gitter Z^6**, Parallelraum-Vektoren a_i = (+-1, tau, 0)/N zyklisch (sechs 5-zaehlige Achsen, Kantenlaenge 1),
  Senkrechtraum b_i = Galois-Bild (tau -> -1/tau), normiert. Kontrolle: sum a a^T = sum b b^T = 2, sum a b^T = 0.
- **Naeherung p/q** (tau -> p/q; 1/1, 2/1, 3/2): Perioden in 6D t_x = p(e5 + e6) + q(e1 - e2), t_y, t_z zyklisch. Ihr
  Parallelbild ist L e_j mit L = (2 p tau + 2 q)/N, ihr Senkrechtbild delta e_j. Gleichmaessige Phason-Verzerrung
  eps = delta/L = (q tau - p)/(p tau + q): +0,2361 (1/1), -0,0902 (2/1), +0,0344 (3/2) [E aus Rauchtest R, Formel M].
- **Schiefe Projektion** (Duneau/Katz/Oguey): P'(x) = pi_perp(x) - eps pi_par(x) projiziert laengs des rationalen
  Schnittraums. Ecke x genau dann, wenn P'(x) - gamma im Fenster W = {sum s_i (b_i - eps a_i), abs(s_i) <= 1/2} liegt.
  W ist die Projektion des 6D-Einheitswuerfels; fuer eps -> 0 wird es das rhombische Triakontaeder der Karte (bei 1/1
  ein Kuboktaeder-artiges Zonoeder mit flachen Tripeln). **Lesart [F]:** "Fenster: rhombisches Triakontaeder" heisst
  hier dieses Fenster der rationalen Naeherung; nur so entsteht eine echte Ammann-Kramer-Pflasterung (zwei goldene
  Rhomboeder mit Kante 1, Parallelbild unveraendert).
- Ecken per Breitensuche ueber +-e_i, kanonisch in der Zelle [0, L)^3 (Reduktion mit t_x, t_y, t_z).
- **Fenster-Entartung [F]:** gamma = eta xi_Saat mit eta = 1e-7 und Zufallsrichtung xi je Saat. gamma0 = 0 ist der
  T_h-symmetrische Punkt; liegen Gitterpunkte genau auf dem Fensterrand, waehlt die kleine Verschiebung je Saat eine
  gueltige Pflasterung aus.
- **Delaunay [F]:** scipy.spatial.Delaunay (Qhull) der Ecken mit 26 Nachbarbildern; behalten werden die Tetraeder, deren
  Schwerpunkt in [0, L)^3 liegt. **Kugel-Entartungen** bricht ein Zitter der Ecken sigma_D = 1e-6 (Normalverteilung je
  Ecke und Saat, periodisch). Der Zitter bestimmt nur die Kombinatorik; alle Kantenvektoren, Volumina, Phasen und
  Hodge-Sterne nutzen die exakten Ecken.
- **Saaten [F]:** 8 je Ordnung, Saat s = 0..7, Zufallsgenerator default_rng([3746, p, q, s]) (erst xi, dann Zitter).
  Gemittelt wird ueber die Saaten (arithmetisch).

## 2. Zahlen je Ordnung (Saat 0, aus dem Rauchtest [R]; gleich fuer alle Saaten erwartet)

| Ordnung | L (Kante = 1) | eps | Ecken V (erwartet L^3 vol(W)/8) | Kanten E | Dreiecke F | Tetraeder T | Rhomboeder |
|---|---|---|---|---|---|---|---|
| 1/1 | 2,7528 | +0,23607 | 32 (32,000) | 224 | 384 | 192 | 32 (4 Typen fehlen: Fenster flach) |
| 2/1 | 4,4541 | -0,09017 | 136 (136,000) | 952 | 1632 | 816 | 136 |
| 3/2 | 7,2068 | +0,03444 | 576 (576,000) | 4032 | 6912 | 3456 | 576 |

- E = 7 V, F = 12 V, T = 6 V: Die Zaehlung passt zu "jedes Rhomboeder in 6 Tetraeder" (Kanten 3V + 3V Flaechen- + V
  Raumdiagonalen) [R, Lesart].

## 3. Traegt das Netz? Pruefungen je Saat (mechanisch im Code, Funktion netz) [F]

- **Zusammenhaengend:** Quotientengraph hat 1 Komponente.
- **Periodisch und raumfuellend:** Summe abs(Tetraedervolumen) = L^3 (rel. < 1e-9); jedes Dreieck in genau 2 Tetraedern;
  Euler V - E + F - T = 0 (3-Torus).
- **Alle Volumina positiv:** kein Tetraeder mit abs(Volumen) < 1e-10 (exakte Ecken).
- **Delaunay:** kein Punkt echt in einer Umkugel (relativ 1e-9); Zahl der Zusatzpunkte auf Umkugeln (Entartung)
  beschreibend.
- **Ammann-Kramer gueltig:** Rhomboeder nach der Dual-Bedingung fuellen die Zelle (Volumensumme = L^3), alle 8 Ecken
  jedes Rhomboeders sind Ecken; V = L^3 vol(W)/8.
- **Beschreibend:** Grad min/max, Kantenlaengen, Zahl der Rand-nahen Fensterpunkte, Vorzeichen von *1 und *2
  (umkreisbasiert: *1 = Dualflaeche/Kantenlaenge, *2 = Dualkante/Dreiecksflaeche; negativ, null, positiv mit Schwelle
  1e-9 des Betragsmaximums).
- Faellt eine Pruefung, steht das im Ergebnis; die Messung laeuft trotzdem und wird so gekennzeichnet.

## 4. Operatoren (Bloch, exakte Netze) [F]

- **S Skalar:** Graph-Laplace mit Einheitsgewichten, L(k)_ij = deg_i delta_ij - sum_Bindungen e^{i k.d}; akustischer Zweig
  omega = sqrt(kleinster Eigenwert), dicht (numpy eigvalsh). Gegenprobe je Saat an 3 Zufalls-k gegen licht_netz.op_skalar.
- **M Maxwell, Coulomb-Phase:** A auf Kanten, Fluss auf den Dreiecken, K = C^dag C mit Einheitsgewichten, Phasen aus
  den Lagen (Kantenmitte relativ zur Dreiecksmitte). Photonen = die zwei kleinsten Eigenwerte ausserhalb der Eichnullen.
  - Rechenweg: K' = C^dag C + G G^dag (G Gradient; C G = 0). Die Eigenvektoren mit G^dag v = 0 sind die Photonen,
    Laengsmoden werden verworfen.
  - Fuer Tempo: Rayleigh-Ritz in einer k.p-Basis je Richtung (harmonische Formen H bei k = 0 und R K_m B_(j-m) bis
    Ordnung 4, R = (K0 + 1e-9)^-1 auf dem Komplement). Gegenprobe je Saat an 2 Richtungen und 2 k gegen exakte
    Shift-Invert-Eigenwerte (scipy eigsh); **Schwelle: relative Abweichung <= 1e-6**, sonst ist der Maxwell-Teil der
    Saat als unsicher gekennzeichnet (Wert ritz_kontrolle im JSON, im Ergebnis abgelesen). Zusaetzlich bei 1/1
    Gegenprobe gegen licht_netz.op_maxwell (dicht).
  - Zweige: lo, hi (je Richtung nach Groesse sortiert) und "mittel" = sqrt((omega_lo^2 + omega_hi^2)/2).
- Kontrollen: C G = 0 (3 Zufalls-k), K0 H = 0, C0 D = 0.

## 5. Messung von a2(n) und Zerlegung [F]

- **Richtungen:** 40 Fibonacci-Richtungen auf der oberen Halbkugel (a2(-n) = a2(n), Zeitumkehr der reellen Netze).
- **Fenster je Richtung:** k in [0,03; 0,12] pi/L, 8 Punkte (Hauptfenster). Probe (beschreibend, nur Saat 0):
  [0,015; 0,06] pi/L, 8 Punkte. **Abweichung vom Werkzeug-Hauptfenster [F]:** Das feste Fenster k <= 0,30 aus
  LICHT-FINN-NETZ-1 liegt fuer 3/2 hinter der Zonengrenze pi/L = 0,436; deshalb skaliert das Fenster mit pi/L.
- **Fit:** licht_netz.fit(kk, omega, 6, gerade=True): omega/k = c (1 + a2 k^2 + a4 k^4 + a6 k^6), k in Einheiten der
  Kante 1. Nur gerade Potenzen, weil omega(k)^2 analytisch und gerade ist [M]. Kontrolle: voller Fit (alle Potenzen):
  a1 ~ 0 und a2 gleich.
- **Zerlegung je Saat und Zweig [F]:** Kleinste Quadrate von a2(n) an die 28 reellen Kugelflaechenfunktionen mit
  l = 0, 2, 4, 6 (RMS-normiert, d.h. Mittel von Y^2 ueber die Kugel = 1):
  - l = 4-Anteil = Koeffizient beta von S4 = sum n_i^4 (Projektion auf K4 = S4 - 3/5, die einzige O_h- und
    T_h-Invariante bei l = 4); also a2 ~ alpha + beta S4 im kubischen Teil (LICHT-FINN-NETZ-1: Maxwell auf Finns Netz
    beta = 1/24).
  - l = 6-Anteil = RMS der Projektion auf die zwei T_h-invarianten l = 6-Funktionen (l = 6-Teil von S6 und
    (x^2 - y^2)(y^2 - z^2)(z^2 - x^2)); dazu die Projektion auf die ikosaedrische l = 6-Funktion (l = 6-Teil von
    sum_i (a_i . n)^6) mit Vorzeichen.
  - Beschreibend: RMS je l (alle Komponenten), nichtkubischer l = 4-Rest, Restfehler des Fits, Konditionszahl.
  - Dieselbe Zerlegung fuer a4 und fuer c^2 (beschreibend).
- **Je Ordnung:** Mittel und Standardabweichung ueber die 8 Saaten.
- **Grundtempo-Spanne:** (max c - min c)/Mittel c ueber die 40 Richtungen, je Saat und Zweig.

## 6. Urteilsregeln (mechanisch, Funktion urteilen; Werte im Auswerte-JSON)

- **N1 (Kartenwortlaut "auf jeder Naeherung"):** Grundtempo-Spanne < 1e-6 fuer jede Ordnung, jede Saat und jeden Zweig
  (skalar, maxwell_lo, maxwell_hi): eingetroffen; sonst nicht eingetroffen (alle Werte stehen im Ergebnis).
- **N2 (Kartenwortlaut):** je Hauptgroesse (skalar, maxwell_mittel): R = abs(Mittel beta(3/2))/abs(Mittel beta(1/1)).
  R <= 1/3: eingetroffen; R > 1/3: nicht eingetroffen ("bleibt hoeher als ein Drittel seines Startwerts").
  Gesamt: beide eingetroffen -> eingetroffen; keiner -> nicht eingetroffen; sonst geteilt. maxwell_lo und maxwell_hi
  stehen beschreibend daneben (Urteil "Karte alle Zweige"). Fehlt 3/2: nicht auswertbar.
- **N3 (Kartenwortlaut "bleibt endlich und naehert sich einem Grenzwert"):** je Hauptgroesse mit A6 = Mittel des
  T_h-invarianten l = 6-RMS: eingetroffen, wenn (i) A6 bei allen drei Ordnungen ueber dem Boden
  max(1e-7, 3 x Restfehler des Fits) liegt, (ii) A6(3/2) >= A6(1/1)/3 (bleibt, faellt nicht wie in N2) und
  (iii) abs(A6(3/2) - A6(2/1)) <= abs(A6(2/1) - A6(1/1)) (naehert sich). Sonst nicht eingetroffen. Gesamt wie N2.
- **Lesart [F]:** "endlich" lese ich als "von null verschieden, nicht wie l = 4 verschwindend".
- Beschreibend, ohne Urteil: Vorzeichen von beta je Ordnung gegen das Vorzeichen von eps; Verhaeltnisse
  beta(2/1)/beta(1/1) und beta(3/2)/beta(1/1) gegen eps-Verhaeltnisse 0,382 und 0,146; Probe-Fenster; a4-Zerlegung;
  *1, *2.

## 7. Vorab ableitbar und Vorab-Kenntnis aus dem Rauchtest

- **N1 ist nur fuer kubische Netze ableitbar** (Tensor 2. Stufe unter T_h isotrop). **[R] Die Netze sind je Saat nicht
  kubisch:**
  - Bei 1/1 liegen Gitterpunkte von P'(Z^6) (ein fcc-Gitter) bei gamma0 = 0 auf dem Fensterrand; ebenso beim zweiten
    T_h-Fixpunkt [M]. Eine gueltige 1/1-AK-Pflasterung mit voller T_h-Symmetrie gibt es in diesem Bau also nicht.
  - Die Delaunay-Zerlegung ist stark kugel-entartet (Zusatzpunkte auf Umkugeln: 160, 672, 2848 je Zelle); der Zitter
    entscheidet diese Faelle je Saat zufaellig.
  - Im Rauchtest unterschieden sich die beiden Photon-Eigenwerte bei k = 0,12 pi/L laengs (1; 0,3; 0,2) um 0,4 % (1/1)
    bzw. 0,3 % (2/1, 3/2) in omega^2. Das ist eine Aufspaltung schon im Grundtempo.
  - **Erwartung daraus: N1 nach Kartenwortlaut scheitert, und zwar am Bau (Symmetriebruch je Saat), nicht an einer
    Aussage ueber ikosaedrische Netze.** Das ist vorab erkennbar und keine Messung.
- **N3 ist fuer skalar und maxwell_mittel vorab ableitbar [M]:** omega^2 ist analytisch und gerade in k; mit isotropem
  Grundtempo ist a2(n) = Q4(n)/(2 c^2) eine quartische Form, hat also nur l = 0, 2, 4. Fuer Maxwell gilt das fuer die
  Spur der beiden Photonen (Summe der Eigenwerte eines analytischen Spektralprojektors). Ein l = 6-Anteil entsteht nur
  ueber die Anisotropie des Grundtempos je Saat (zweite Ordnung im Symmetriebruch). **Erwartung: N3 fuer skalar und
  maxwell_mittel nicht eingetroffen (A6 nahe am Boden oder Rauschen ohne Grenzwert); das ist ableitbar, keine Messung.**
  - Fuer maxwell_lo und maxwell_hi kommt l = 6 aus der Doppelbrechung (Eigenwerte einer 2x2-Matrix, nicht polynomial).
    Der Grenzwert ist ableitbar null: Ein ikosaedrisch invarianter Tensor 4. Stufe ist isotrop (DANZER-L 3.2), also
    gibt es dort bei k^4 keine Doppelbrechung. Die Zahlen auf den Naeherungen sind nicht ableitbar.
  - Die erste ikosaedrische Richtungsabhaengigkeit sitzt nach DANZER-L 3.3 bei k^6 in omega^2, also in a4. Die
    a4-Zerlegung rechne ich deshalb beschreibend mit (Zusatz, ohne Urteil).
- **N2:** Nur die Richtung ist ableitbar (Karte). Aus der linearen Kopplung folgt zusaetzlich [M, H]: beta_n ~ eps_n,
  also wechselndes Vorzeichen (+, -, +) und Betragsverhaeltnisse 0,382 und 0,146 gegen 1/1. Nicht ableitbar sind
  Vorfaktoren und der Beitrag der Delaunay-Zufallswahl.
- **Hodge-Vorzeichen:** Fuer Delaunay sind *1 und *2 nicht negativ (HODGE-L, Hirani u. a. 2013) [P, S dort]. [R] Der
  Rauchtest zeigte 0 negative Werte und viele Nullen (Entartung). Das ist ableitbar und nur beschreibend.

## 8. Laeufe (nach dem Einfrieren; je <= 600 s, 1 Thread, kleintest.sh, Logs mit absolutem Pfad)

- Spur cpu5 (cpu3 und cpu4 belegt durch UMKLAPP-1 beim Planen; werden sie frei, nutze ich sie fuer 3/2).
- Arbeitsordner .69: /home/fmh/fmhc-physics-remote/danzer-naeherung-1/ (code/, lauf/, rauch/).

| Lauf | Aufruf (danzer_naeherung.py ...) | erwartete Dauer |
|---|---|---|
| L1 | rechnen 1/1 S,M 0,1,2,3,4,5,6,7 lauf/n11.json --probe | < 1 min |
| L2 | rechnen 2/1 S,M 0,1,2,3,4,5,6,7 lauf/n21.json --probe | ~ 2 min |
| L3a | rechnen 3/2 S,M 0,1 lauf/n32a.json --probe | ~ 6 min |
| L3b, L3c, L3d | rechnen 3/2 S,M 2,3 / 4,5 / 6,7 lauf/n32b.json usw. | je ~ 4,5 min |
| L4 | auswerten lauf/auswertung.json lauf/bild-danzer-naeherung.png lauf/n11.json lauf/n21.json lauf/n32*.json | < 1 min |
| L5 | Wiederholung L1 nach lauf/n11-wdh.json (beschreibend; Vergleich mit jq ohne argv und Laufzeiten) | < 1 min |

- Reihenfolge: L1, L2 zuerst (Teilbericht moeglich), dann 3/2. Reicht die Zeit nicht fuer alle 3/2-Saaten, wertet L4
  die vorhandenen aus; die Zahl der Saaten steht im Ergebnis.
- Faellt ein Lauf aus (Fehler, 600 s), steht das im Ergebnis. Eine Codeaenderung danach waere eine Selbstanzeige mit
  neuer eingefrorener Fassung.

## 9. Agenten-Vorhersagen (vor jeder Hauptrechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | N1 nach Kartenwortlaut nicht eingetroffen (Bau, Abschnitt 7) | 85 % |
| A2 | Ritz-Gegenprobe <= 1e-6 in allen Saaten | 90 % |
| A3 | Skalar: beta wechselt das Vorzeichen mit eps (+, -, +) im Saatmittel | 45 % |
| A4 | N2 fuer skalar eingetroffen (R <= 1/3) | 50 % |
| A5 | N3 fuer skalar und maxwell_mittel nicht eingetroffen | 80 % |
| A6 | Saatstreuung von beta bei 3/2 groesser als abs(Mittel) | 40 % |

## 10. Einfrieren

- Eingefroren werden PLAN.md und code/danzer_naeherung.py als Kopien *.eingefroren-<Zeit>, sha256 in
  EINGEFROREN-SHA256.txt, auf der .69 dieselben Pruefsummen. code/licht_netz.py ist die unveraenderte Kopie
  (sha256 98d3960a...). Danach keine Aenderung an Plan, Code oder Regeln.
