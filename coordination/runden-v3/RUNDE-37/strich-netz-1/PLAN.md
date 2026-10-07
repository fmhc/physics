# STRICH-NETZ-1: Plan (Runde 41, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Arbeitsplatz RUNDE-37/strich-netz-1/, Rechenort .69
  (/home/fmh/fmhc-physics-remote/runde41-strich-netz/), Spuren cpu6 und cpu7.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 15:59:12 CEST. Gelesen bis 16:15 CEST (Karte, SPIN-ZUFALLSNETZ-1, INDUZIERT-Code, AETHER-UHR-1,
    LICHT-GLEICH-L, QCA-TETRA-1, ZWEI-SEITEN v2.2 Abschn. 3 und 4, BLACKMON-MEOW-L Abschn. 4).
  - Abschnitt 0 (Schreibtischpruefung) geschrieben ab 16:15:27 CEST, vor jeder Rechnung und vor dem ersten Code.
- **Kennzeichen:** [M] eigene Mathematik (ungeprueft), [L] Literatur aus dem Gedaechtnis, [L?] unsicher,
  [F] Festlegung dieses Plans, [E] hier gerechnet, [H] Hypothese, [P] Projektdatei, [Z] Zusatzvorgabe der Leitung
  (nicht aus der Karte).
- Alles ist synthetische Netzrechnung. Keine Messdaten, keine Messdatenbestaetigung.

## 0. Schreibtischpruefung der Karte (vor jeder Rechnung)

| Nr | Kartenaussage | Pruefung | Folge |
|---|---|---|---|
| S1 | 3420-Regel, Bogenlaenge = Winkel bei C | **richtig [M].** Blickrichtungen u parallel zur Ebene ABC bilden einen Grosskreis (Laenge 2 pi). C liegt in der Projektion genau dann auf AB, wenn die Gerade durch C in Richtung u die Strecke AB trifft, also u im Winkel ACB oder gegenueber. Das sind zwei Boegen der Laenge gamma_C. Die drei Punkte eines Tripels teilen den Grosskreis lueckenlos: 2 (gamma_A + gamma_B + gamma_C) = 2 pi. 20 x C(19,2) = 3420 = 3 x C(20,3) Paare (Punkt, Strich), jedes mit einem Bogen; auf der Kugel hat jeder Bogen das Mass null | Probe: Bogen gegen Winkel, Summe 2 pi je Tripel |
| S2 | Kreuzungen = konvexe Vierergruppen; P = 1 - Summe Omega_v/(2 pi) | **richtig [M].** Vier Punkte in allgemeiner Lage: konvex, dann kreuzen genau die Diagonalen; sonst liegt einer im Dreieck, keine Kreuzung. Ecke v liegt in der Ansicht u im Dreieck der anderen genau dann, wenn u oder -u im Kegel an v liegt; Anteil 2 Omega_v/(4 pi). 0,649 gilt fuer das regulaere Tetraeder und ist zugleich der Wert fuer Gauss-verteilte Punkte in der Ebene [L?: Baryshnikov/Vitale]. 25/36 und 1 - 35/(12 pi^2) = 0,7045 stimmen [L] | Erwartung fuer projizierte Wuerfelpunkte zwischen beiden, also etwa 3150 bis 3400 [M, grob] |
| S3 | Gabriel-Grad 8 | **richtig [M].** Integral 4 pi r^2 exp(-pi r^3/6) dr = 8 (allgemein 2^d) | - |
| S4 | Anteil gegenseitig naechster Nachbarn 0,62; L-Beruehrung 0,69 N Striche, 0,31 N Inseln | **Fehler: 0,62 ist der 2D-Wert (0,6215) [M].** In 3D: P = Volumen(Kugel)/Volumen(Vereinigung zweier Kugeln mit Mittelpunktabstand r) = (4/3)/(27/12) = **16/27 = 0,5926**. Damit dicht in 3D: Striche (1 - 8/27) N = 0,704 N, Inseln 8/27 N = 0,296 N | **SN7, dritter Teil (0,62 +- 0,01), wird vorab als verfehlt erwartet [M].** SN2 (20 Punkte mit Rand) ist kaum betroffen |
| S5 | Delaunay-Grad 15,54 | **richtig [L]:** 2 + 48 pi^2/35 = 15,535 (Meijering); SPIN-ZUFALLSNETZ-1 mass 15,505 bis 15,581 [P] | - |
| S6 | Maxwell-Zaehlung 3N - 6 - E, "trifft je Netz" | **nur als Untergrenze richtig [M].** Exakt gilt Calladine: Z - 6 - S = 3N - 6 - E (Z Nullmoden, S Eigenspannungen). Bei E > 3N - 6 (alle, Delaunay, meist Gabriel) ist die Zaehlung negativ und als max(0, .) zu lesen. Lokal lose Stellen (z. B. Gabriel-Punkte mit Grad <= 2) geben dann mehr Nullmoden. Wald (L-Beruehrung): exakt, keine Eigenspannung | Der Maxwell-Teil von SN0 kann bei Gabriel scheitern; Calladine wird als Rechenprobe getrennt geprueft |
| S7 | Isotacheia: bei FEM c exakt; Rest offen [H] | **richtig, und weiter ableitbar [M].** Homogenisierung: A_eff = Mittelwert-Tensor minus Korrektor. Der Korrektor verschwindet, wenn die affine Funktion diskret harmonisch ist (Patch-Test). Das gilt fuer FEM (je Tetraeder), fuer den Voronoi-Skalar (Abschluss sum_j A_ij n_ij = 0) und im Weyl-Fall (erste Ordnung entarteter Stoerungsrechnung mit der exakten Identitaet sum_i M_i = L^3 1, SPIN-ZUFALLSNETZ-1). **Fuer k -> 0 ist damit v_Weyl = c_FEM = 1 exakt vorab ableitbar [M, ungeprueft].** Fuer (ii) und (iii) ohne Patch-Test senkt der Korrektor das Tempo unter den Mittelwert (Vorzeichen ableitbar, Groesse nicht) | SN5 ist im Grenzwert vorab ableitbar; gemessen wird, ob die Daten bei endlichem k dorthin laufen (Abschnitt 6). SN6 haengt an der Normierung von (ii), siehe S8 |
| S8 | (ii) "ein Sprung je Takt" | **Normierung fehlt in der Karte.** Ohne Laengenmass hat (ii) kein Tempo in Laengeneinheiten. Mit "Takt = mittlere Kantenlaenge / c" weicht (ii) schon im Mittelwert um sqrt(Grad <d^2>/(6 <d>^2)) ~ 1,6 bis 1,7 ab [M], SN6 waere dann trivial | [F] Hauptlesart: eine globale Konstante aus dem Netz, so dass der Mittelwert-Tensor die Spur 3 hat ("gemittelt auf Kantenlaengen"); dann misst SN6 den Korrektor. Die andere Normierung wird berichtet |
| S9 | kleinste Wellenzahl 0,17 bei N = 50 000 | richtig fuer periodische Randbedingung; mit Verdrillung (Bloch-Phase theta) ist jedes kleinere k zugaenglich [M] | wird fuer den Weyl-Spinor genutzt |
| S10 | L-Beruehrung = "jeder mit seinem naechsten Nachbarn" | Das gleichzeitige Aufblasen mit Anhalten bei erster Beruehrung gibt im Allgemeinen einen anderen Graphen [M] | Kartenlesart (NN-Graph) bleibt Hauptlesart; Wachstumsvariante beschreibend |
| S11 | Laplace des vollstaendigen Graphen: 0 und 20 (19-fach), keine Front | **richtig [M]:** u_j(t) = (1 - cos(sqrt(20) t))/20 fuer alle j ungleich Quelle | Kontrolle |
| S12 | P1-FEM-Skalar und Voronoi-Gewichte | In 3D ist P1-FEM (Gewicht l_kl cot theta_kl / 6 je Tetraeder) nicht gleich dem Voronoi-Operator A/d [M: Ecktetraeder 1/6 gegen 1/4 je Achsenkante]. FEM-Gewichte koennen auf Delaunay in 3D negativ sein; flache Tetraeder (Slivers) machen K steif | Voronoi-Skalar als beschreibendes Zusatzfeld (gleiche Geometrie wie der Weyl-Operator); FEM nicht per KPM |

## 0a. Agenten-Vorhersagen (geschrieben ab 16:27:37 CEST, nach dem Start der Rauchlaeufe, vor dem Lesen jeder Rauchzahl)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | SN1: mittlere Gabriel-Strichzahl bei 20 Punkten im Wuerfel in [90; 110] | 60 % |
| A2 | SN2 eingetroffen (NN-Graph etwa 14 Striche, 6 Inseln) | 90 % |
| A3 | SN3: mittlere Kreuzungszahl L-alle in [3150; 3400] | 70 % |
| A4 | SN7 nicht eingetroffen, und zwar nur am NN-Anteil (0,593 +- 0,005) | 90 % |
| A5 | SN6: (ii) weicht langwellig um mehr als 5 % von (i) ab (Normierung Abschnitt 3) | 40 % |
| A6 | SN5 eingetroffen (Abweichung der Grenzwerte < 1 %) | 75 % |
| A7 | SN4 eingetroffen | 55 % |
| A8 | SN0 eingetroffen (Risiko: Maxwell-Teil bei Gabriel) | 35 % |
| A9 | Laengenregel (iii): homogenisiertes Tempo weicht um mehr als 2 % von 1 ab | 60 % |
| A10 | Kuerzeste Wege auf Delaunay: Fronttempo in [0,90; 0,97] | 60 % |

## 1. Vorhersagen der Karte (unveraendert uebernommen)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SN0 | Kontrollen: L-alle 190 Striche; vollstaendiger Graph ohne Front; Maxwell-Zaehlung trifft je Netz (Abweichung hoechstens 1 durch Sonderlagen); FEM-Skalar langwellig c = 1 innerhalb 2 %; die 3420-Regel trifft an jeder Stichprobe | 90 % |
| SN1 | [M] L-Gabriel bei 20 Punkten im Wuerfel: im Mittel 75 bis 110 Striche | 60 % |
| SN2 | [M] L-Beruehrung: im Mittel 12 bis 16 Striche und 4 bis 8 Inseln je Saat | 75 % |
| SN3 | [M] Kreuzungen je zufaelliger Ansicht fuer L-alle: Mittel zwischen 2900 und 3500 | 80 % |
| SN4 | [H] Auf L-Gabriel und L-Delaunay mit N >= 2000 laeuft ein Stoss als Front mit festem Tempo (Frontradius linear in t ueber mindestens 5 Netzschritte, Streuung ueber Richtungen <= 15 %) | 60 % |
| SN5 | [H] Isotacheia im Mittel: Das langwellige Tempo des Weyl-Spinors (v) weicht fuer k -> 0 um weniger als 1 % vom FEM-Skalar (i) ab | 40 % |
| SN6 | [H] Ungewichtet (ii) weicht langwellig um mehr als 5 % von (i) ab oder ist richtungsabhaengig | 70 % |
| SN7 | [M, L] Bei N = 50 000 periodisch: mittlerer Gabriel-Grad 8,0 +- 0,1, mittlerer Delaunay-Grad 15,54 +- 0,1, Anteil gegenseitig naechster Nachbarn 0,62 +- 0,01 | 85 % |

Die Bedeutungssaetze der Karte gelten unveraendert.

## 2. Punkte, Rand, Lesarten

- **Teil A:** 20 Punkte gleichverteilt im Einheitswuerfel [0, 1]^3, kein periodischer Rand. Saaten 1 bis 2000,
  Zufall default_rng([41, 20, saat]). Rauchsaaten 9001 bis 9120 (nie im Hauptlauf).
- **Teile B und C:** N = 50 000 Poisson-Punkte mit Dichte 1 im periodischen Wuerfel, L = 36,84. Netzbau unveraendert
  mit spinnetz.zufallsnetz (SPIN-ZUFALLSNETZ-1, sha256 460c0af6; Zufall default_rng([39, N, saat])), Hauptsaaten 1
  und 2, Rauchsaat 901. Die Tetraeder werden mit demselben Verfahren (Saum-Kopien, Qhull, Schwerpunkt im
  Grundwuerfel) neu bestimmt; Pruefung: Kantenmenge gleich der von spinnetz. Netz einmal bauen, als .npz speichern.
- **Lesarten [F, Karte]:**
  - alle: jedes Paar.
  - gabriel: keine weitere Punkt in der offenen Kugel mit dem Strich als Durchmesser (periodisch per cKDTree mit
    boxsize; als Teilmenge der Delaunay-Kanten, Pruefung "Gabriel in Delaunay" bei N = 20).
  - delaunay: Kanten der Delaunay-Tetraeder (Qhull).
  - beruehrung: jeder Punkt mit seinem naechsten Nachbarn (Kartenlesart, NN-Graph).
  - wachstum (beschreibend, S10): alle Kugeln wachsen gleich schnell und halten bei der ersten Beruehrung an.
- Fuer N = 50 000 gibt es "alle" nur als Kontrolle ohne Geometrie (L = N 1 - J matrixfrei).

## 3. Felder, Gewichte, Normierung (Teile B und C)

- Gemeinsame Form der Skalare: m_i u_i'' = -sum_j w_ij (u_i - u_j); Kantenvektor d_ij = Bildvektor von i nach j.
- **(i) fem:** P1-FEM auf den Delaunay-Tetraedern, lokale Steifigkeit aus induziert.lokal_K_batch (INDUZIERT-1,
  unveraendert, sha256 b3867eac), konzentrierte Masse m_i = sum V_T/4. Gewichte w_ij = -K_ij duerfen negativ sein.
- **(i') voronoi (beschreibend, S12):** w_ij = A_ij/d_ij (Voronoi-Facette), Masse V_i (Voronoi-Volumen); dieselbe
  Geometrie wie der Weyl-Operator. Sein lokaler Tensor ist genau der Weyl-Tensor M_i [M].
- **(ii) ungew ("ein Sprung je Takt"):** w_ij = kappa fuer jede Kante, Masse 1. [F] kappa = 3 N / sum_e d_e^2, so dass
  der Mittelwert-Tensor (1/V) sum_e w_e d_e d_e^T die Spur 3 hat (mittleres Quadrat des Sprungtempos = c^2).
  Berichtet, nicht geurteilt: Takt = mittlere Kantenlaenge / c, also w = 1/<d>^2 (S8).
- **(iii) laenge (Laengenregel):** w_ij = kappa/d_ij^2, Masse 1, kappa = 3 N / E. Begruendung: Jede Kante wird in der
  Zeit d_ij/c durchlaufen; in einer Kette mit Abstand d gibt w = c^2/d^2 genau das Tempo c. Die eine globale Konstante
  kappa ersetzt "2 x Dimension / Grad" und macht die Spur des Mittelwert-Tensors exakt 3. Sie wird aus der Kantenzahl
  gebildet, nicht aus einem gemessenen Tempo.
- **(iv) kuerzeste Wege:** Kantenzeit d_ij/c mit c = 1, Dijkstra; Fronttempo = Abstand/Laufzeit.
- **(v) weyl:** spinnetz.matrix unveraendert (H = V^-1/2 H0 V^-1/2, H0_ij = (i/2) A_ij sigma.n_ij e^(i theta.s_ij)),
  Zweig E > 0 mit Helizitaet sigma.k^ = -1 (Vorzeichenkonvention von spinnetz).
- **Normierung:** fem, voronoi und weyl haben keine freie Konstante; ihr Mittelwert-Tensor ist exakt 1 [M; FEM je
  Tetraeder V_T 1, Voronoi und Weyl ueber sum_i M_i = L^3 1]. ungew und laenge erhalten je eine globale Konstante mit
  Spur 3. Damit haben alle Felder im Mittelwert dasselbe Tempo 1; gemessen wird, was Unordnung daraus macht.

## 4. Verfahren

**Teil A (je Saat):**
- Zaehlungen je Lesart: Striche E, Grade, Inseln (Zusammenhangskomponenten), Delaunay-Tetraeder, Huellpunkte,
  Anteil gegenseitig naechster Nachbarn.
- 2000 Blickrichtungen gleichverteilt auf der Kugel (default_rng([41, 20, saat, 1])). Orientierung eines Tripels in
  der Ansicht u: Vorzeichen von u . ((x_b - x_a) x (x_c - x_a)).
  - Kreuzungen L-alle: Zahl der Vierergruppen in konvexer Lage (Radon-Vorzeichen: genau zwei positive unter
    (chi_bcd, -chi_acd, chi_abd, -chi_abc)). Kontrolle in den ersten drei Saaten jedes Blocks: gleich der direkten
    Paarzaehlung.
  - Kreuzungen der anderen Lesarten: direkte Zaehlung kreuzender Paare disjunkter Striche.
  - Punkt-nahe-Strich-Beruehrungen (eps = 0,01 und 0,02) fuer alle, gabriel, delaunay: [F, Laufzeit] auf den ersten
    500 der 2000 Ansichten (Rauchlauf: 2000 Ansichten kosten etwa 1,5 s je Saat).
- 3420-Probe: in den ersten 10 Saaten jedes Blocks je 10 Tripel; Bogen auf dem Grosskreis aus 200 000 Richtungen
  gezaehlt gegen 2 gamma_C; Summe der drei Boegen gegen 2 pi.
- Federnetz je Lesart (Federkonstante 1): Starrheitsmatrix R, Rang per SVD (Schwelle 1e-8 sigma_max), Nullmoden
  Z = 3N - Rang, Eigenspannungen S = E - Rang, Maxwell-Abweichung (Z - 6) - max(0, 3N - 6 - E); Beteiligungsverhaeltnis
  der drei tiefsten Nicht-Null-Moden.
- Skalare je Lesart: ungewichtet und laengengewichtet (w = 1/d^2, Masse 1), bei Delaunay zusaetzlich FEM (Neumann,
  konzentrierte Masse). Nullmoden, Beteiligungsverhaeltnis, Aehnlichkeit der drei tiefsten Moden mit ebenen Wellen
  (Anteil im Raum der affinen Funktionen x, y, z bei Masse M).
- Stoss (ersten 200 Saaten je Block 1, sonst die ersten stoss Saaten des Blocks; ungewichtet; v(0) = e_s an dem Punkt
  naechst der Wuerfelmitte), exakt ueber die Eigenzerlegung: Spread der Nicht-Quellen-Punkte (vollstaendiger Graph),
  Abgleich mit u_j(t) = t/n - sin(sqrt(n) t)/(n sqrt(n)), Korrelation der Ankunftszeit (halbe maximale kinetische
  Energie) mit Abstand und Netzschritten.

**Teil B (N = 50 000):**
- Stoss v(0) = e_s/m_s, u(0) = 0; Leapfrog mit dt = min(0,5/omega_max, 0,05), omega_max per ARPACK; bis t = 16 (alle:
  t = 2). Je 0,25 Zeiteinheiten: Knotenenergie (kinetisch plus halbe Kantenenergie, bei FEM ein Viertel der
  Tetraederenergie), R50 und R90 (Radius, in dem 50 bzw. 90 % der Energie liegen; echter Abstand, Minimalbild),
  R90 je Richtungskegel (14 Kegel: 6 Achsen, 8 Raumdiagonalen; Zuordnung zur naechsten Richtung), Netzschritte
  (energiegewichtetes Mittel und H90), Energie ausserhalb der Insel der Quelle.
- Laeufe: gabriel/ungew und delaunay/ungew mit 4 Quellen; gabriel/laenge, delaunay/laenge, delaunay/fem mit 2
  Quellen; beruehrung/ungew 1 Quelle; alle (matrixfrei) 1 Quelle.
- Scheibenbilder: |z - z_Quelle| < 1 bei t = 4, 8, 12, erste Quelle.
- Tiefe Moden als ebene Wellen: Anteil jeder tiefen Eigenmode (Teil C, Schalen 1 bis 4) in den ebenen Wellen ihrer
  Schale.

**Teil C (N = 50 000, Saat 1; Saat 2 als Gegenprobe fuer Homogenisierung und Zaehlungen):**
- **Exakter Grenzwert k -> 0 der Skalare (Homogenisierung) [M]:** A_eff = (1/V) sum_e w_e d_e d_e^T - (1/V) B^T K^+ B,
  b_i = sum_j w_ij d_ij, Korrektor per CG mit Jacobi-Vorkonditionierer (rtol 1e-11); c(n) = sqrt(n.A_eff.n / rho),
  rho = sum m / V, fuer 13 Richtungen (3 Achsen, 6 Flaechen-, 4 Raumdiagonalen), Anisotropie (max - min)/Mittel.
  Kontrolle K3: geschichtetes Gitter mit harmonischem Mittel 1,5.
- **Weyl bei k -> 0 [M]:** erste Ordnung entarteter Stoerungsrechnung, v(n) = |M_vol n| mit M_vol = (1/V) sum_i M_i.
- **Endliches k, Skalare:** theta = 0, die 40 tiefsten Eigenpaare (Shift-Invert-Lanczos, sigma = -1e-3, SuperLU mit
  MMD_AT_PLUS_A); fuer die 16 ebenen Wellen der Schalen |m|^2 = 1, 2, 3, 4 (k = 0,171; 0,241; 0,296; 0,341) das
  gewichtete Mittel der Eigenwerte ihrer Schale (Schale = rint(lambda/(c_h^2 k_1^2)), c_h aus der Homogenisierung):
  c(k) = sqrt(lambda_Zentrum)/k. Kontrolle K2: 7-Punkt-Laplace auf dem Gitter L = 37 gegen analytisch.
- **Endliches k, Weyl:** KPM (spinnetz.kpm_block, jackson, kpm_dichte, unveraendert), M = 4096 Momente,
  Spektralfunktion je ebener Welle; Zentrum = gewichtetes Mittel der KPM-Dichte im Fenster +-4 sigma_E um das
  Maximum (sigma_E = pi a/M); Vergleichswert mit M/2. Wellen: theta = 0 die 16 Schalenwellen; verdrillt
  theta = theta0 e mit theta0 = 0,8; 1,6; 2,4 und e = x (Wellen m = 0, +-e_x: k = 0,022 bis 0,236) bzw.
  e = (1,1,1)/sqrt 3 (m = 0, +-(1,1,1): k = 0,022 bis 0,339). Kontrolle K1: kubisches Gitter L = 37 gegen
  E = sqrt(sum sin^2 k_a).
- **(iv):** Dijkstra von 16 Quellen; Fit Laufzeit = r/v + t0 auf 8 <= r <= L/2 - 1; je Kegel; Umwegfaktor fern.
- **Abhaengigkeit von N und Mittelungsgroesse:** Homogenisierung bei N = 2000 (10 Saaten) und N = 8000 (4 Saaten),
  Streuung ueber Saaten; dazu [Z] lokale Tempi.
- **[Z] Streuung der lokalen Tempi (Zusatzvorgabe der Leitung, beschreibend, keine Vorhersage):** je Feld der
  Knotentensor T_i = 1/2 sum_j w_ij d_ij d_ij^T und Masse m_i; c^2(n) = n.T.n/m je Knoten und je Teilwuerfel mit
  Kante L/2, L/4, L/8 (8, 64, 512 Zellen), 7 Richtungen (Achsen, Raumdiagonalen); Standardabweichung relativ zum
  Mittel ueber Zellen und Richtungen, je Richtung ueber Zellen, je Zelle ueber Richtungen; Quantile. FEM je
  Tetraeder ist exakt isotrop (V_T 1) [M]; die Knotenaufteilung zeigt die Kantengewichte. Dazu die Streuung der
  homogenisierten Tempi ueber Saaten (N = 2000, 8000) und ueber Richtungen.

## 5. Laeufe (je Lauf <= 600 s, 1 Thread, 4 GB; Ordner /home/fmh/fmhc-physics-remote/runde41-strich-netz/lauf/)

- **cpu6:** H1 `netz 50000 1 lauf/netz-1.npz`; H2 `dicht lauf/netz-1.npz lauf/dicht-1.json`; H3 `weyl lauf/netz-1.npz
  lauf/weyl-1-0.json 4096 0`; H4 `eigen ... lauf/eigen-1-fem.json felder=fem`; H5 `eigen ... felder=voronoi`;
  H6 `welle ... lauf/welle-gabriel-ungew gabriel ungew 4`; H7 `welle ... delaunay ungew 4`; H8 bis H11
  `teilA 1|251|501|751 250 lauf/teilA-b1..b4.json stoss=250`; H12 `kontrolle lauf/kontrolle.json M=4096`.
- **cpu7:** H13 `netz 50000 2 lauf/netz-2.npz`; H14 `dicht lauf/netz-2.npz lauf/dicht-2.json`; H15 `klein 2000 1 10
  lauf/klein-2000.json`; H16 `klein 8000 1 4 lauf/klein-8000.json`; H17 `eigen lauf/netz-1.npz ... felder=ungew`;
  H18 `... felder=laenge`; H19 `weyl lauf/netz-1.npz lauf/weyl-1-x.json 4096 x`; H20 `weyl ... d`; H21 bis H25
  `welle` gabriel/laenge 2, delaunay/laenge 2, delaunay/fem 2, beruehrung/ungew 1, alle/ungew 1 (tmax = 2);
  H26 bis H29 `teilA 1001|1251|1501|1751 250 lauf/teilA-b5..b8.json stoss=250`.
- Danach H30 `bilder.py lauf` und H31 `auswertung.py lauf`. Ergebnisse per scp nach lauf-69/, Pruefsummen auf der .69.
- Teil A: Stoss in allen Saaten (billig); 3420-Probe in den ersten 10 Saaten jedes Blocks (80 Saaten, 800 Tripel).

## 6. Urteilsregeln (mechanisch in code/auswertung.py)

- **SN0** eingetroffen, wenn alle fuenf Teile gelten, sonst nicht eingetroffen:
  - (a) L-alle hat in jeder der 2000 Saaten 190 Striche.
  - (b) Keine Front im vollstaendigen Graphen: N = 20 Spread der Nicht-Quellen-Punkte <= 1e-12 und Abstand zur
    analytischen Loesung <= 1e-10 (alle Stoss-Saaten); N = 50 000 matrixfrei Spread <= 1e-12 zu allen Zeiten.
  - (c) Maxwell: fuer jedes der 8000 Netze (vier Kartenlesarten x 2000 Saaten) abs((Z - 6) - max(0, 3N - 6 - E)) <= 1.
  - (d) FEM langwellig: homogenisiertes c in allen 13 Richtungen (Saaten 1 und 2) und c der drei Achsenwellen bei
    k = 0,171 (Saat 1) in [0,98; 1,02].
  - (e) 3420-Probe: max abs(Bogen - 2 gamma) <= 1e-3 und max abs(Summe - 2 pi) <= 1e-3.
- **SN1:** Mittel der Gabriel-Strichzahl ueber 2000 Saaten in [75; 110].
- **SN2:** Mittel der NN-Graph-Striche in [12; 16] und Mittel der Inseln in [4; 8].
- **SN3:** Mittel der L-alle-Kreuzungen ueber alle Saaten und Ansichten in [2900; 3500].
- **SN4 [F: Front, Fenster, Linearitaet]:**
  - Je Quelle: Fenster aller Abtastzeiten mit 2 l <= R90 <= L/2 - 4 (l mittlere Kantenlaenge der Lesart);
    linear, wenn die Spanne von R90 im Fenster >= 5 l, R^2 der Geraden >= 0,99 und die Steigungen der beiden
    Fensterhaelften auf 10 % gleich sind. Richtungsstreuung: Variationskoeffizient der 14 Kegelsteigungen im selben
    Fenster.
  - Eine Lesart erfuellt SN4, wenn alle Quellen linear sind und der mittlere Variationskoeffizient <= 0,15 ist.
  - Plan-Urteil: Feld ungew auf Gabriel und Delaunay; eingetroffen, wenn beide erfuellen. Nicht auswertbar, wenn
    ein Fenster weniger als 6 Abtastzeiten hat. Wortlaut-Urteil: alle gerechneten Felder auf Gabriel und Delaunay.
- **SN5 [F: Extrapolation]:**
  - Weyl: Fit v(k) = v0 + a1 k + a2 k^2 an alle Weyl-Zentren mit k <= 0,35 und Fenstergewicht >= 0,5
    (theta = 0 und verdrillt). FEM: Fit c(k) = c0 + b2 k^2 an die 16 Schalenwellen.
  - Delta5 = abs(v0 - c0)/c0, SE aus den Fit-Kovarianzen. Eingetroffen bei Delta5 < 0,01, sonst nicht eingetroffen.
  - Nicht auswertbar, wenn K1 scheitert (max abs(v_KPM - v_exakt) > 1e-3) oder 2 SE > 0,005.
  - Berichtet: Delta bei k = 0,171 (Achsenwellen), die kleinsten verdrillten k, die Grenzwerte erster Ordnung bzw.
    der Homogenisierung (beide vorab 1 [M]).
- **SN6 [F: Normierung Abschnitt 3; Schwelle "richtungsabhaengig"]:** Delta6 = abs(c_ungew - c_fem)/c_fem der
  richtungsgemittelten homogenisierten Tempi (Saat 1); Anisotropie a6 von c_ungew ueber 13 Richtungen. Eingetroffen,
  wenn Delta6 > 0,05 oder a6 > 0,02 [F: 0,02 liegt deutlich ueber der erwarteten statistischen Anisotropie
  ~ 1/sqrt(E) bei N = 50 000]. Gegenprobe Saat 2; anderes Urteil gibt einen Vermerk.
- **SN7:** Mittel der Saaten 1 und 2: Gabriel-Grad in 8,0 +- 0,1, Delaunay-Grad in 15,54 +- 0,1, NN-Anteil in
  0,62 +- 0,01; eingetroffen nur, wenn alle drei gelten.
- Die Urteile nach Kartenwortlaut stehen in ERGEBNIS.md neben den Plan-Urteilen.

## 7. Kontrollen (Gueltigkeit, kein eigenes Urteil)

- K1 Weyl-KPM-Zentren gegen exakt (kubisches Gitter L = 37, 16 Schalenwellen plus verdrillt): <= 1e-3, sonst SN5
  nicht auswertbar.
- K2 Skalar-Eigenpaare gegen exakt (7-Punkt-Laplace L = 37): <= 1e-6.
- K3 Homogenisierung geschichtet: A_xx = 1,5 auf 1e-6.
- K4 Netz N = 1000: Kantenmenge gleich spinnetz, FEM-Kopie gegen Gradientenformel <= 1e-8, Patch-Test (Drift) FEM
  und Voronoi <= 1e-10.
- Je Hauptnetz: Euler 0, Abschluss, Kantenmenge gleich, FEM-Kopie, Masse = Volumen, Drift fem/voronoi.
- Teil A: Gabriel in Delaunay; Kreuzungen konvex gleich Paarzaehlung; Spread und Analytik des vollstaendigen Graphen.

## 8. Kartenwortlaut, Lesarten, Kartenfehler (vor dem Einfrieren)

- **K-S4 (SN7, Kartenfehler):** 0,62 ist der 2D-Wert; in 3D gilt 16/27 = 0,593 [M, Abschnitt 0]. SN7 wird deshalb
  nach Plan und Wortlaut voraussichtlich am dritten Teil scheitern. Die Regel bleibt wie in der Karte.
- **K-S6 (SN0, Maxwell):** "trifft je Netz" ist als (Z - 6) = max(0, 3N - 6 - E) +- 1 gelesen. Calladine
  (Z - S = 3N - E) gilt per Rangsatz immer und ist keine Probe; die Lesart prueft, ob Eigenspannungen und lose
  Stellen fehlen.
- **K-S8 (SN6):** Die Karte legt die Normierung von (ii) nicht fest. Plan-Lesart: Mittelwert-Tensor mit Spur 3.
  Mit "Takt = mittlere Kantenlaenge / c" waere SN6 vorab ableitbar eingetroffen; das wird berichtet.
- **K-S7 (SN5):** Der Grenzwert k -> 0 ist vorab ableitbar (beide 1). Die Regel urteilt deshalb auf den Fits an
  gemessene Werte bei endlichem k; scheitern kann der Fit (Abweichung oder zu grosse Unsicherheit) und meine Herleitung.
- **K-SN1 (aus dem Rauchlauf R1, vor dem Einfrieren gesehen):** Die Karte sagt "am Rand werden es mehr". Bei
  20 Punkten im Einheitswuerfel fehlen aber vor allem die moeglichen Partner ausserhalb des Wuerfels; der mittlere
  Gabriel-Grad liegt in den Rauchsaaten bei 3,9 bis 4,7 (39 bis 47 Striche). Eine grobe Rechnung
  C(20,2) E[(1 - Vol(Kugel im Wuerfel))^18] gibt ebenfalls etwa 50 [M, grob]. SN1 (75 bis 110) wird daher voraussichtlich
  verfehlt; Regel unveraendert.
- **K-Teil-B:** Die Karte nennt N = 20 und 2000 (bis 20 000); der Nachtrag legt N = 50 000 fest. Federnetze und
  Maxwell nur bei N = 20 (2000 Saaten); bei N = 50 000 waere die Nullmodenzaehlung (150 000 Freiheitsgrade) in 10 min
  nicht sicher. "L-alle" bei N = 50 000 nur matrixfrei und ungewichtet.
- **K-Ansichten:** Beruehrungen auf 500 statt 2000 Ansichten je Saat (Laufzeit); Kreuzungen auf allen 2000.
- **Kartenfehler insgesamt:** S4 (0,62 statt 0,593), "am Rand mehr" bei SN1, fehlende Normierung bei SN6.

## 9. Rauchlaeufe (offengelegt; .69-Zeiten UTC; Ordner rauch/ bzw. rauch-69/)

- **Gelesen habe ich nur Zeiten, Speicher, Codepfade und Teil-A-Zahlen der Rauchsaaten.** Teil-C-Tempi (Homogenisierung,
  Eigen-Schalen, Weyl-Zentren, kuerzeste Wege) und die SN7-Zahlen habe ich nicht angesehen; die Logzeilen wurden per
  grep -o bzw. sed auf Zeit- und Speicherfelder beschnitten.
- R1 `teilA 9001 5` (cpu6, 14:26:53 bis 14:27:06, Code 20b6e7c5): 2,1 s je Saat mit 2000 Beruehrungs-Ansichten.
  **Gesehen:** Gabriel 39 bis 47 Striche, L-alle-Kreuzungen 3192 bis 3348 je Saat, NN-Graph 13 bis 15 Striche und 5 bis
  7 Inseln, Delaunay 90 bis 95 Striche, Maxwell-Abweichung 0 in allen 25 Netzen, 3420-Probe max 5,9e-5 rad, Spread
  des vollstaendigen Graphen 3,3e-15. SN1 ist damit vor dem Hauptlauf absehbar verfehlt (Abschnitt 8, K-SN1).
- R2 `netz 50000 901`: 18 s, 705 MB; T = 338 418, E = 388 418, Kantenmenge gleich, FEM-Kopie 4,1e-11,
  FEM-Gewichte negativ 33,7 %.
- R3 `dicht` (Saat 901): 10,8 s; CG-Residuen <= 1e-11.
- R4 `eigen felder=fem,ungew`: FEM: LU 166,5 s, nnz(LU) 1,38e8, 279 s, RSS 3,16 GB; das zweite Feld lief in die
  600-s-Grenze (Unit beendet). **Folge:** ein Feld je Lauf.
- R5 `welle delaunay fem 1 tmax=1`: lambda_max = 1078, dt = 0,0152, Energiedrift -1,9e-4; gesehen: Energieanteil an der
  Quelle 0,54 / 0,13 / 0,22 / 0,13 bei t = 0,25 bis 1.
- R6 `weyl x` mit M = 256: a = 3,668, 7,5 s je Verdrillung (3 Wellen).
- R7 `kontrolle` (320 s): K1 1,7e-6, K2 2,8e-14, K3 exakt 1,5, K4 Kanten gleich, FEM-Kopie 2e-13, Drift FEM 4,7e-15,
  Voronoi 1,7e-15. Die Tempi des N = 1000-Netzes in K4 habe ich nicht angesehen.
- R8 `welle alle` und R9 `welle beruehrung`: Codepfade; R10 `teilA 9101 20` mit 500 Beruehrungs-Ansichten:
  0,78 s je Saat (gesehen: Gabriel 43, Kreuzungen 3286 bei Saat 9101).
- R11 bis R14: Netz N = 8000 (Saat 902), `eigen` je ein Feld, `weyl 0` mit M = 256: nur Codepfad und Zeit.
- R15 bis R17: auswertung.py und bilder.py auf umbenannten Rauchdateien (rauch/ausw-test; dicht-1.json ist R3 mit per
  jq gesetzter Saat 1, nur fuer den Codepfad). Angesehen: nur die Schluesselstruktur von auswertung.json und
  bild-A-netze.png (Rauchsaat 9001) fuer das Layout; nicht angesehen: Urteile, bild-C-tempo.png, bild-B-*.
- **Aenderungen nach Rauchlaeufen (vor dem Einfrieren):** Verdrillte Weyl-Wellen auf 3 je Verdrillung (Laufzeit),
  Beruehrungen auf 500 Ansichten (Laufzeit), 3420-Probe in jedem Block, Bildlayout (Mittelwert abgezogen,
  Beschriftung). Keine Schwelle wurde nach einem Rauchergebnis gesetzt oder geaendert; die Regeln in Abschnitt 6 und
  auswertung.py stammen aus der Karte bzw. sind [F] ohne Ansicht von Teil-B/C-Werten geschrieben.
- **Regelabweichung (Selbstanzeige):** Um 16:25 CEST habe ich eine Sicherungskopie von strichnetz.py in den
  Sitzungs-Scratchpad (/tmp/claude-1000/...) geschrieben; um 16:26 geloescht. Sonst nichts dort abgelegt; die
  Werkzeug-Ausgabedateien der Hintergrundaufrufe legt das Werkzeug selbst dort an (leer, Ausgaben umgeleitet).

## 10. Einfrieren

- Eingefroren um 2026-10-04 16:39:11 CEST: PLAN.md.eingefroren-20261004-163911 und code/*.py.eingefroren-20261004-163911; Pruefsummen in
  EINGEFROREN-SHA256.txt (lokal) und auf der .69 (code/EINGEFROREN-SHA256.txt).
