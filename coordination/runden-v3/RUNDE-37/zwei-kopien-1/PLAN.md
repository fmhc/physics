# ZWEI-KOPIEN-1: Plan (Code-Agent, Runde 43, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 19:48:07 CEST (date). Letzte eigene Messung vor dem
  Abbruch durch das Sitzungslimit: 19:48:45 CEST (.69, 17:48:45 UTC); bis dahin nur gelesen, nichts geschrieben, nichts
  gerechnet. Wiederaufnahme 21:45:58 CEST (date; Leitung: 21:45:28). Plantext ab 21:50:52 CEST (date), vor jeder Rechnung.
  Zeitbox bis 23:10 CEST (Leitung).
- Grundlage: KARTE.md (ZK0 bis ZK2, Baender und Wahrscheinlichkeiten unveraendert). Vorlage: TENSOR-EIS-PYRO-1
  (code/tp.py, sha256 419d7da6..., unveraendert kopiert und importiert; Referenz lauf-69/spektrum.json, sha256
  3c86c372...). EINE-WELT-LOCH-1 gelesen (ERGEBNIS, code/ew.py).
- Kennzeichen: [M] vorab ableitbar (Schreibtisch), [E] hier gerechnet, [P] im Projekt schon gerechnet, [L] Literatur aus
  dem Gedaechtnis, [F] eigene Festlegung, [H] Hypothese. Alles synthetische Gitterrechnung, keine Messdaten.
- Dimensionsvergleich (AGENTS.md): gerechnet wird nur das 3D-Netz (3 Raumrichtungen, Hamilton-Form). In 2+1 Dimensionen
  hat linearisierte Schwerkraft keine Gravitonen (symmetrischer 2x2-Tensor: 3 Komponenten - 2 Eichungen - 1 Regel = 0),
  die Frage entfaellt dort; in d Raumrichtungen gibt es (d+1)(d-2)/2 Polarisationen (d = 3: 2). Die Spur-Aussage in 1.2
  (Mittel ueber die Kanten eines regulaeren Simplex = Spur/d) gilt in jeder Dimension [M]; die Ecken-Anisotropie in 1.4
  ist eine Eigenschaft des Pyrochlor-Netzes.

## 1. Ableitbarkeitsprobe am Schreibtisch (vor jeder Rechnung)

### 1.1 Bau [P, F]

- B1 aus TENSOR-EIS-PYRO-1: Kopie 1 = Auf-Kanten als Staebe zwischen Ab-Mitten (Eichung xi_Ab), Kopie 2 = Ab-Kanten
  zwischen Auf-Mitten (Eichung xi_Auf). Variablen a = delta l/l, 12 je primitiver Zelle. B = Regge (tp.ops_pyro), A =
  Bewegungsenergie je Finn-Tetraeder ((n.n)^2 - 1/2), Gauss M (3 je Kopie), Skalarregel c (1 je Kopie).
- Ecke v = R + r_a gehoert genau dem Auf-Tetraeder R und dem Ab-Tetraeder D = R + 2 r_a.
- **K2 [F, Lesart der Karte]:** phi_v = mittlere Dehnung der 6 Kanten des Auf-Tetraeders minus die der 6 Kanten des
  Ab-Tetraeders; K2 = Summe_v phi_v^2. ("mittlere Kantendehnung beider Tetraeder" = Mittel ueber die Kanten je Tetraeder.)
- **K2e [F, Variante, nur beschreibend]:** wie K2, aber Mittel nur ueber die 3 Kanten je Tetraeder, die an v liegen.
- **K4 [F]:** psi_v^(c) = (LBAR/3) Summe der Fehlwinkel-Aenderungen der 3 Kanten der Kopie c an v (Fehlwinkel aus Regge:
  delta eps = -(1/LBAR) B a); K4 = Summe_v psi_v^(1) psi_v^(2) (Produkt, also indefinit).
- Energie (1/2) a^dagger (B + kappa K) a, kappa in {0,01; 0,1; 1} (Haupt), Bloch-Phasen an den wirklichen Orten.
- Die alternative Lesart "Skalarkruemmung jeder Kopie an ihrem Platz" fuer K4 verschwindet auf der Zwangsflaeche
  identisch (c^dagger a = 0) [M]; sie wird nicht gerechnet.

### 1.2 Schritt 0: Ist K2 unter xi_Ab = Mittel(xi_Auf) invariant? Nein [M]

- Mittlere Kantendehnung unter Eichung: eps_Auf(R) = (1/(3 l_P^2)) Summe_a r_a . xi_Ab(R + 2 r_a),
  eps_Ab(D) = -(1/(3 l_P^2)) Summe_a r_a . xi_Auf(D - 2 r_a) (diskrete Divergenz; Summe der Paare ergibt 4 Summe r_a.x_a).
- Gegenbeispiel: xi_Auf = Punktquelle xi an der Auf-Mitte R0, xi_Ab(D) = (1/4) Summe_b xi_Auf(D - 2 r_b). An der Ecke
  R0 + r_a: eps_Auf(R0) = 0 (nur Terme r_a . xi mit Summe 0), eps_Ab(R0 + 2 r_a) = -(1/(3 l_P^2)) r_a . xi. Also
  phi = r_a . xi/(3 l_P^2) != 0. **K2 ist nicht invariant; B-b ist auf diesem Weg nicht ableitbar, die Karte schrumpft
  nicht zur Kontrolle.** Im Bloch-Bild gilt die Gleichheit nur in erster Ordnung in k (beide Seiten i k . xi/8).
- Was K2 stattdessen erhaelt [M]: phi_a(k) ~ u . xi_Ab + e^{2 i k.r_a} conj(u) . xi_Auf mit u(k) = Summe_a r_a e^{2 i k.r_a}.
  Exakt invariant bleiben fuer jedes k die 4 Eichrichtungen u . xi_Ab = 0 und conj(u) . xi_Auf = 0 (je Kopie die
  "quere" Eichung, getrennt), gebrochen sind 2 (je Kopie die Laengs-Eichung). Eine diagonale Eichung entsteht nicht.

### 1.3 Folgerung fuer die Baender [M]

- Lesart P (Zwangsflaeche wie TENSOR-EIS-PYRO-1, alle 6 Gauss-Regeln und beide Skalarregeln bleiben): Die vier
  physikalischen Moden je k sind langwellig reine TT-Moden. Fuer ein regulaeres Tetraeder ist Summe_e n_e n_e^T = 2 I,
  also mittlere Kantendehnung = Spur(h)/3. TT-Moden haben Spur 0: **K2 verschwindet auf ihnen fuer k -> 0, alle vier
  bleiben masselos; Erwartung K2: Band B-a, gegen ZK1** (K2 ist >= 0, also kein omega^2 < 0 in P). Offen bleibt nur, wie
  stark kappa die Tempi verschiebt (Ordnung kappa k^2 in omega^2).
- K4: Fehlwinkel sind eichinvariant (B M = 0 [P]), die Kopplung ist von der Ordnung k^4 gegen k^2 der Regge-Energie.
  **n0 = 4 fuer k -> 0 ist ableitbar; B-b und B-c sind fuer K4 ausgeschlossen.** Offen ist nur, ob das indefinite Produkt
  bei endlichem k ein omega^2 < 0 erzeugt (B-d), also die Instabilitaetsschwelle kappa_c.
- K2e (Variante): Fuer die Differenzmode (h_1 = -h_2, TT) gibt Summe der vier Ecken (16/9)(h_xy^2 + h_yz^2 + h_zx^2):
  eine kubisch-anisotrope Masse nur fuer die Nebendiagonale. Erwartung: Laengs <100> bleibt die Polarisation
  h_yy - h_zz der Differenz masselos (n0 = 3), sonst n0 = 2; Luecke omega^2 linear in kappa (p = 1/2 fuer omega).
- BDGH [L]: verbietet nichttriviale Kreuzkopplung masseloser Spin-2-Felder (wesentlich ab kubischer Ordnung); auf
  quadratischer Ebene bleiben nur Mischung (wegtransformierbar) oder Massenterme. K2 ist ein reiner Spur-Massenterm (nicht
  Fierz-Pauli) der Differenz, K4 eine Mischung hoeherer Ableitung. Beides passt zu "Kopplung im Kontinuum trivial fuer die
  TT-Moden" (B-a). Ein Widerspruch zu BDGH entstuende erst bei B-b mit Kopplung an die Energie; das prueft diese Karte
  nicht (linear).
- EINE-WELT-LOCH-1 [P]: Dort entschied die Eichstruktur (gefuellte Loecher machen das B1-Eichbild gleich dem Eck-Eichbild,
  eine Welt). Hier bleibt in Lesart P die Eichstruktur von Hand unveraendert; eine Welt kann nur ueber eine Masse der
  Differenz entstehen, und die sieht K2 nicht (1.3 oben).
- **Was vorab feststeht, wird nur als Kontrolle gerechnet:** n0(K2, P) = 4, n0(K4) = 4 bei kleinem kappa, Exponent fuer
  K2e. **Offen und gemessen:** kappa_c fuer K4 (B-d), Tempi und Streuung s unter K2, Lesart R (unten), Konkurrenzzustaende.

### 1.4 Lesart R (Resteichung, vorab festgelegt, beschreibend; nicht Grundlage der Urteile)

- K2 bricht 2 der 6 Eichrichtungen (1.2). Dann kann man deren Gauss-Regeln nicht widerspruchsfrei verlangen. Lesart R:
  physikalischer Raum = Komplement von [M N, c], N = Kern von K M (relative Schwelle 1e-8 der Singulaerwerte). Fuer K4
  ist K M = 0, also R = P. Fuer K2 kommen 2 Moden je k dazu (je Kopie die Laengs-Eichrichtung).
- Erwartung [M, H]: In R ist B + kappa K2 >= 0 (B M = 0, K2 >= 0); eine Laengsmode der Summe bekommt omega^2 ~ kappa k^2
  (masselos, aber Helizitaet 0: Konkurrenzzustand), die der Differenz eine Luecke ~ kappa. Ob A darauf positiv bleibt
  (Norm), ist offen: A0 je Tetraeder ist auf gleichmaessiger Dehnung negativ (Eigenwert -1).

## 2. Messgroessen (code/zk.py)

- **Kleine k:** 26 Richtungen (alle (i, j, l) aus {-1, 0, 1}^3 ohne 0, normiert), |k| = eps1 = 1e-3 und eps2 = 2e-3.
  Je Punkt alle omega^2 = Eigenwerte von (S^dagger A S)(S^dagger (B + kappa K) S), TT-Anteil je Mode (tp.tensor_aus je
  Kopie, Zaehler und Nenner von tp.tt_anteil ueber beide Kopien summiert), Kopienanteil w1 = |a_1|^2/|a|^2, Eigenwerte von
  A_phys und B'_phys.
- **Kontrollrichtungen (ZK0):** die 23 Richtungen von TENSOR-EIS-PYRO-1 ([100], [110], [111], 20 Zufall, Saat 3) bei
  eps1, eps2 und kappa = 0.
- **BZ-Gitter L = 16** (4 095 k ohne 0, wie TENSOR-EIS-PYRO-1): je k Zahl positiver / negativer / komplexer / Null-Moden,
  A_phys und B'_phys negativ, kleinstes Re omega^2 relativ.
- **kappa-Leiter (beschreibend):** kappa in {1e-3, 3e-3, 1e-2, 3e-2, 0,1, 0,3, 1, 3, 10, 30, 100}, Gitter L = 8 und die 26
  Richtungen; je kappa n0, Band, kleinstes omega^2.
- **Pfad (Bild):** Gamma -> X [001], Gamma -> K [110], Gamma -> L [111], je 40 Punkte, alle Moden, kappa = 0, 0,1, 1.

## 3. Klassen und Baender (mechanisch in code/zk_auswertung.py)

**Klassen je Mode und Richtung** (omega^2 je eps nach Realteil sortiert, Index j zugeordnet; s = max |omega^2| je eps):
- wachsend: an einem eps Re omega^2 < -1e-9 s oder |Im omega^2| > 1e-9 s.
- q_j = Re omega^2_j(eps2) / Re omega^2_j(eps1).
- masselos: nicht wachsend, Re omega^2_j(eps1) > 1e-9 s, 3,0 <= q_j <= 5,0 und Re omega^2_j(eps2) <= 100 eps2^2.
- Luecke: nicht wachsend, 0,8 <= q_j <= 1,25 und Re omega^2_j(eps1) >= 1e-5.
- unklar: alles andere.
- Helizitaet 2: TT-Anteil >= 0,99 an beiden eps.
- n0(Richtung) = Zahl der Moden "masselos und Helizitaet 2". Konkurrenz: "masselos, nicht Helizitaet 2" und "unklar".

**Groessen je Fassung, kappa, Lesart:**
- n0 = gemeinsamer Wert ueber die 26 Richtungen, sonst "variabel" (min, max).
- Delta = Wurzel des kleinsten Re omega^2(eps1) ueber alle Richtungen und alle Moden "Luecke und Helizitaet 2"
  (angehobene Zweige); Delta_alle ebenso ueber alle Luecke-Moden.
- p = Steigung von log Delta gegen log kappa (kleinste Quadrate ueber die drei Haupt-kappa), nur wenn Delta bei allen
  dreien definiert ist; 2p fuer omega^2.
- s = (max - min)/Mittel von Re omega^2(eps1)/eps1^2 ueber alle masselosen Helizitaet-2-Moden aller 26 Richtungen.
- Kopienanteil der masselosen Helizitaet-2-Moden: min und max von w1.

**Baender je Fassung und kappa** (Rangfolge: B-d zuerst, dann nach n0):
- B-d nach Plan: wachsend an einem der 52 Punkte, oder am Gitter L = 16 ein Re omega^2 < -1e-9 s bzw. |Im| > 1e-9 s,
  oder A_phys mit Eigenwert < -1e-9 max|A_phys| (negative Norm), oder B'_phys mit Eigenwert < -1e-9 max|B'_phys|
  (negative Energie: Zustand unter dem Vakuum), an irgendeinem Gitter-k oder kleinen Punkt.
- B-d nach Kartenwortlaut ("omega^2 < 0 oder negative Norm"): nur wachsend/omega^2 < 0 bzw. komplex und A_phys negativ.
- B-a: n0 = 4 an allen 26 Richtungen.
- B-b: n0 = 2 an allen 26 Richtungen, an jeder Richtung genau 2 Moden "Luecke und Helizitaet 2" (Delta > 0), s < 0,05.
- B-c: n0 = 0 an allen 26 Richtungen.
- sonst: kein Band.

## 4. Urteilsregeln (Lesart P, Fassungen K2 und K4)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| ZK0 | kappa = 0: n0 = 4 an allen 26 Richtungen, an allen 23 Kontrollrichtungen und beiden eps max abs(omega^2/k^2 - Referenz) <= 1e-8 (Referenz: sortierte Vereinigung pyro1 + pyro2 aus spektrum.json), und positive Moden je Gitter-k gleich der Referenz an allen 4 095 k | n0 = 4 und Tempi v = omega/k an den 23 Richtungen auf <= 1e-8 gleich |
| ZK1 | Band(K2, kappa) = B-b fuer alle drei kappa | wie Plan, zusaetzlich "Kombination": jede masselose Helizitaet-2-Mode hat 0,1 <= w1 <= 0,9; B-d nur nach Kartenwortlaut |
| ZK2 | Band(K4, kappa) = B-a fuer alle drei kappa | wie Plan, B-d nur nach Kartenwortlaut |

- Teilergebnis: Trifft die Vorhersage nur fuer einen Teil der kappa ein, heisst das Urteil "nicht eingetroffen" mit
  Angabe der kappa, fuer die es gilt.
- K2e und Lesart R gehen in kein Urteil ein; sie stehen getrennt im Ergebnis.

## 5. Agenten-Vorhersagen (vorab; in keinem Urteil)

| Nr | Vorhersage |
|---|---|
| V1 | ZK0 eingetroffen, Tempo-Abweichung <= 1e-10 |
| V2 | K2 (P): Band B-a fuer alle drei kappa; ZK1 nicht eingetroffen |
| V3 | K4 (P): B-a bei kappa = 0,01 und 0,1; bei kappa = 1 offen (50 % B-d); kappa_c der Leiter zwischen 0,1 und 30 |
| V4 | K2e (P): n0 = 2 an allen Richtungen ausser den 6 <100>-Richtungen (dort 3), also kein Band; p = 0,50 +- 0,02 |
| V5 | K2 (R): 4 masselose TT-Moden, eine weitere masselose Mode ohne Helizitaet 2 (Konkurrenz), eine Luecke; Norm offen (50 %) |
| V6 | s(K2, P, kappa = 1) > 1 % (Tempi werden richtungsabhaengig verschoben) |

## 6. Laeufe auf der .69 (kleintest.sh, Spuren cpu8 und cpu9, je <= 10 min, 1 Thread)

| Lauf | Aufruf (in /home/fmh/fmhc-physics-remote/zwei-kopien-1) | Spur |
|---|---|---|
| R0 | Rauchlauf nach dem Einfrieren: zk.py lauf --fassung K2 --L 4 --Lleiter 2 --npfad 4 --out rauch/... (nur rc, Zeit, Schluessel) | cpu8 |
| L2 | zk.py lauf --fassung K2 --L 16 --Lleiter 8 --npfad 40 --ref ref/spektrum.json --out lauf/zk-K2.json | cpu8 |
| L4 | zk.py lauf --fassung K4 ... --out lauf/zk-K4.json | cpu9 |
| LE | zk.py lauf --fassung K2e ... --out lauf/zk-K2e.json | cpu8 |
| AW | zk_auswertung.py --lauf lauf --out lauf/auswertung.json | cpu9 |
| BI | zk_bild.py --lauf lauf --out lauf/spektrum.png | cpu9 |

- Einfrieren vor jedem Lauf: PLAN.md, code/zk.py, code/zk_auswertung.py, code/zk_bild.py, code/tp.py (Kopien
  *.eingefroren-<Zeit>, sha256 in EINGEFROREN-SHA256.txt). Der Rauchlauf kommt erst nach dem Einfrieren; scheitert er an
  einem Programmfehler, wird die Berichtigung offengelegt und neu eingefroren (Selbstanzeige), ohne Ergebniswerte zu
  lesen.
- Faellt ein Lauf an der 600-s-Grenze: L = 12 statt 16 (vorab festgelegt).

## 7. Zusatz Leitung 21:5x, beschreibend (eingetragen ab 21:52:14 CEST, date; vor dem Einfrieren)

- Kein Urteil, keine Aenderung an ZK0 bis ZK2; steht im Ergebnis getrennt unter "beschreibend".
- Fuer jede masselose TT-Mode (Klasse "masselos und Helizitaet 2"), die nach der Eckkopplung bleibt: omega^2/k^2 in den
  Richtungen [100], [110], [111] (unter den 26 Richtungen enthalten), je |k| = 1e-3 und 2e-3, je Fassung (K2, K4, K2e),
  kappa (0,01; 0,1; 1) und Lesart (P, R).
- Dazu die Spanne max/min - 1 ueber alle Richtungen und alle verbleibenden Zweige, je |k|: einmal ueber die drei
  Richtungen [100], [110], [111], einmal ueber alle 26.
- Bezug: dieselbe Angabe fuer das ungekoppelte Netz (kappa = 0).
- Grund (Leitung): Auf dem gefuellten Netz aus EINE-WELT-LOCH-1 laufen die TT-Zweige richtungsabhaengig (2,6 bis
  10,6 %), ohne Fuellung mit der Reduktion R1 isotrop (0,25). Gefragt ist, ob die Eckkopplung die Isotropie erhaelt.
- Umsetzung: zk_auswertung.py, Abschnitt "zusatz_isotropie" der auswertung.json; Daten aus denselben Laeufen.
