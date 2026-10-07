# KOPPLUNG-TETRA-1: Plan (Code-Agent, Runde 42, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 16:50:35 CEST; Plantext ab 17:06:30 CEST (date), vor jeder
  Rechnung. Zeitbox 150 min, also bis 19:20 CEST.
- Grundlage: KARTE.md (KT0 bis KT3; Vorhersagen, Schwellen und Wahrscheinlichkeiten unveraendert uebernommen).
- Vorlage: RUNDE-37/tensor-eis-pyro-1/code/tp.py, unveraendert kopiert (sha256 419d7da6...), Geometrie und C_A(k).
- Kennzeichen: [M] Mathematik (vorab ableitbar), [S] an der Quelle gelesen, [P] im Projekt schon gerechnet (mit
  Fundstelle), [E] hier gerechnet, [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [F] eigene Festlegung.
- Alle Rechnungen sind synthetische Gitterrechnungen, keine Messdaten.

## 1. Literatur (Abrufe 15:00 und 15:01 UTC, quellen/)

- Abruf 1: rruff.info, Am. Mineral. 81, 1057 (Hammonds u. a. 1996): **404**, keine Quelle (quellen/FEHLABRUF-404-...).
- Abruf 2: F. Wegner, "Rigid Unit Modes in Tetrahedral Crystals", arXiv cond-mat/0703486v3 (23.07.2007),
  quellen/wegner2007-cond-mat-0703486.pdf (sha256 df9821db...). Gelesen: S. 1 bis 8 und 17 bis 19. [S]:
  - S. 2: CRUSH behandelt die starren Tetraeder als einzelne Molekuele, "harmonic forces are added between the two
    'split' atoms, which should be one" (Split-Atom-Methode, Giddy u. a. 1993, Hammonds u. a. 1994).
  - S. 2 bis 5 (Gl. 11, 20, 21): Wegner rechnet RUM als Sauerstoff-Verschiebungen, die alle 6 n_t Tetraederkanten in
    erster Ordnung festhalten; RUM gibt es, wo die Determinante der 6 n_t x 6 n_t Kantenmatrix verschwindet.
  - S. 6: Mit Inversionszentrum ist die (umnormierte) Determinante reell, also eine Bedingung fuer drei Unbekannte:
    generisch **Flaechen** von RUM; ohne Inversion generisch Linien.
  - S. 8, beta-Cristobalit (Gl. 40 bis 44): gleiche fcc-Vektoren wie tp.py (a1 = a/2 (e2 + e3) usw.), Determinante
    proportional zu (1 - rho1)(1 - rho2)(1 - rho3)(rho1 - rho2)(rho1 - rho3)(rho2 - rho3), rho_k = exp(i a_k . q);
    "Thus all RUMs are located in the planes" (0, eta, zeta), (xi, 0, zeta), (xi, eta, 0), (xi, xi, zeta),
    (xi, eta, xi), (xi, eta, eta) in der Basis b_i. Das sind genau die sechs Scharen k . a_m = 0 mod 2 pi mit
    a_m aus {a1, a2, a3, a1 - a2, a2 - a3, a3 - a1}. "The planes of RUMs found agree completely with those given in
    ref. [1]" = Hammonds, Dove, Giddy, Heine, Winkler, Am. Mineral. 81, 1057 (1996).
  - S. 7: Wegner bestimmt die Entartungen nicht ("we will not determine the degeneracies").
- Abruf 3: nicht genutzt (Reserve).

## 2. Schreibtisch (vor jeder Rechnung)

### 2.1 Geometrie [P]

- Wie tp.py: kubische Kante a = 1, fcc-Vektoren a1 = (0,1,1)/2, a2 = (1,0,1)/2, a3 = (1,1,0)/2; Auf-Tetraeder U(R)
  Mitte R, Ecken R + r_a, r_a = R8[a]/8; Ab-Tetraeder D(R) Mitte R + 2 r_0, Ecken = Plaetze (R + s_b, b) mit
  s_0 = 0, s_1 = a1, s_2 = a2, s_3 = a3. Platz (R, a) liegt bei R + r_a und gehoert zu U(R) und D(R - s_a).
- Ecken = Pyrochlor (Sauerstoff), Mitten = Diamant (Silizium): Topologie von ideal beta-Cristobalit [S, Wegner
  Gl. 40: Si bei +-(1/8,1/8,1/8), O bei 0 und a_i/2]. Jede geteilte Ecke ist Inversionszentrum (D3d).
- Je primitiver Zelle 4 Ecken, 2 Tetraeder, 12 Kanten.

### 2.2 Modelle [F]

- **(a) Split-Atom:** starre Tetraeder mit t_T, omega_T (6 je Tetraeder, 12 je Zelle); Feder kappa = 1 zwischen den
  zwei Haelften jeder Ecke. Fehlpass an Platz (R, a):
  m = (t_U - [r_a]x omega_U) - (t_D + [r_a]x omega_D), U = U(R), D = D(R - s_a).
  Bloch (Feld x(R) = x e^{i k.R}): K(k) 12 x 12, Zeile a: [I, -[r_a]x, -p_a I, -p_a [r_a]x], p_a = e^{-i k.s_a}.
  Steifigkeit Phi = K^dagger K. Fuer Spektren (beschreibend): Eckmasse 1 halb auf jedes Tetraeder, also m_T = 2,
  I_T = (8/3)(1/2)|r|^2 = 1/16.
- **(b) Federnetz:** Masse 1 je Ecke, Feder 1 je Kante (Zentralkraft), gemeinsame Ecken. D_b(k) = C^dagger C mit
  C = tp.C_A(k)/sqrt2 (tp.py nutzt Kantenvektoren der Laenge sqrt2, Phase e^{i k.x} am wirklichen Ort).
- Masse und Traegheit beeinflussen die Nullmoden nicht.

### 2.3 Folgerung: KT1 und KT2 sind vorab ableitbar [M, S, P]

- **Satz [M]:** dim ker K(k) = dim ker C_A(k) fuer jedes k. Grund: Ein Tetraeder mit sechs Kanten ist infinitesimal
  starr (3 . 4 - 6 = 6 Kanten, voller Rang). Eine Eckverschiebung, die alle Kantenlaengen haelt, bewegt also jedes
  Tetraeder starr; das ist ein RUM. Umgekehrt definiert ein RUM an jeder Ecke eine eindeutige Verschiebung, die alle
  Kanten haelt; verschwindet sie an allen Ecken, ist der RUM null. Das Federnetz (b) hat damit genau dieselben
  Nullmoden wie (a). Wegner rechnet RUM genau so (Abschnitt 1).
- **Folge:** Die RUM-Menge ist die Nullstellenmenge von det C_A. TENSOR-EIS-PYRO-1 hat det C_A = 1024 prod
  sin(k . a_m/2) und die exakten Raenge 12 / 11 / 10 / 9 / 6 (allgemein / eine Ebene / Linie zweier / dreier Scharen /
  k = 0) gefunden [P, RUNDE-37/tensor-eis-pyro-1/ERGEBNIS.md Abschnitt 2]. Also: **0 / 1 / 2 / 3 / 6 RUM je k**,
  auf genau den sechs Ebenenscharen, wie bei Wegner [S] und (nach Wegner) Hammonds u. a. 1996.
- **Damit ist KT2 (Deckung mit den Tensor-Eis-Ebenen) vorab ableitbar**, entgegen der Karte ("nicht ableitbar"), und KT1
  ist an der Quelle belegt. Beide werden nur noch als Kontrolle meines Codes gerechnet. Ihre Urteile zaehlen nicht als
  Treffer einer Vorhersage (Selbstanzeige in ERGEBNIS.md).
- Bei k = 0 sind die 6 RUM: 3 Translationen und 3 gegenlaeufige Drehungen (omega_D = -omega_U) [M].

### 2.4 Triplett [P, M]

- Einzel-Federtetraeder (Masse 1, Feder 1): omega^2 = 0 (6), 1, 1 (E), 2, 2, 2 (T2), 4 (A1) [P, TETRAEDER-20261001;
  Spur 12 = 2 + 6 + 4, M].
- Paar mit gemeinsamer Ecke (7 Massen, 12 Federn, Inversion durch die Ecke, D3d): 21 - 6 starre = 15; 12 Federn, also
  mindestens 3 weitere Nullmoden (Drehungen um das Gelenk) [M]. Die 12 Schwingungen zerfallen in 2 A1g + 2 Eg + 2 A2u
  + 2 Eu, also 4 Singuletts und 4 Dubletts, kein Triplett [M, Gruppentheorie C3v/D3d]. Die Groesse der Aufspaltung ist
  nicht ableitbar und wird gemessen.
- Gitter (b) bei k = 0: Auf- und Ab-Kanten geben dieselben Dehnungsquadrate, D_b(0) = 2 D_einzel, also omega^2 = 0 (6),
  2, 2, 4, 4, 4, 8 [M]; das Triplett bleibt bei Gamma dreifach (O_h). An anderen Punkten gemessen.

### 2.5 Eichprobe: Festlegungen [F] und Vorueberlegung [H]

- **Ring:** sechs Tetraeder um ein Kagome-Sechseck (Diamant-Sesselring), Folge der Platztypen (a, b, c, a, b, c):
  T1 = U(0), T2 = D(-s_a), T3 = U(-s_a + s_b), T4 = D(-s_a + s_b - s_c), T5 = U(s_b - s_c), T6 = D(-s_c); gemeinsame
  Ecken (0, a), (-s_a + s_b, b), (-s_a + s_b, c), (s_b - s_c, a), (s_b - s_c, b), (0, c). Hauptring (a, b, c) =
  (1, 2, 3); Gegenring (0, 1, 2) nur als Symmetrieprobe. Ringnormale n (Probe: die sechs Ecken liegen in einer Ebene,
  regelmaessiges Sechseck mit Seite l_P = sqrt2/4).
- **Verdrehung:** kleine Drehvektoren theta_1 .. theta_6 der Ringtetraeder um ihre Mitten (18 Zahlen). Energie zweiter
  Ordnung E = (1/2) theta^T S theta, Split-Atom-Modell (a), kappa = 1, periodische Superzelle L x L x L.
- **Holonomie [F]:** Haupt H+ = Summe theta_i (die Tetraeder sind die Uebertragungen zwischen aufeinanderfolgenden
  Ringecken; die nullkostende gegenlaeufige Drehung ist dann flach, H+ = 0). Variante H- = Summe s_i theta_i
  (s = +1 Auf, -1 Ab), nur beschreibend. In zweiter Ordnung ist alles abelsch; ob die Kopplung nichtabelsch waere,
  kann diese Probe nicht entscheiden.
- **Was relaxiert [F]:**
  - V0 nackt: alles andere fest.
  - V1: Translationen der sechs Ringtetraeder frei, Umgebung fest.
  - V2: Umgebung frei, Ringtranslationen fest.
  - **V3 (Haupt, "entlang der RUM"): alles ausser den 18 Ringdrehungen frei.**
  - Rechenweg (Bloch, vor dem Rauchlauf festgelegt; ersetzt die erste Fassung mit dichter QR) [M]: Phi = A^T A ist auf
    der L-Superzelle blockzirkulant mit Bloecken Phi(k) = K^dagger K. Minimum von (1/2) x^T Phi x unter C x = theta
    (C waehlt die festgehaltenen Koordinaten): Nullmoden Z = ker Phi (Kernvektoren von K(k) auf dem L-Gitter),
    W = C Z (welche Ringmuster RUM erreichen), M = C Phi^+ C^T (Phi^+ blockweise, SVD-Schwelle 1e-9), dann
    S = Q (Q^T M Q)^-1 Q^T mit Q = Orthonormalbasis von W-senkrecht. V3: C = 18 Ringdrehungen; V2: C = 18 Drehungen und
    18 Translationen, S_V2 = Drehblock; V0 = Drehblock von Phi; V1 = Schur-Komplement des 36er-Blocks von Phi auf die
    Drehungen. Ist W der ganze Raum, ist S = 0.
  - Superzellen L = 8, 16, 24, 32 (Bloch); dichte Gegenprobe bei L = 4 (A dicht, Phi = A^T A, verallgemeinertes
    Schur-Komplement mit pinv, Schwelle 1e-10): S_dicht gegen S_Bloch fuer V0 bis V3.
- **Verteilungen [F]** je Holonomierichtung H in {n, e1, e2} (e1 = Mitte -> erste Ringecke, e2 = n x e1), |H| = 1,
  Summe theta_i = H: konzentriert auf T_j (6), gleich H/6 (1), Paar T_j, T_{j+3} je H/2 (3), nur Auf je H/3 (1), nur Ab
  (1), 10 skalare Zufallsgewichte (Dirichlet(1), Saat 7) und 10 vektorielle (H/6 + eta_i - Mittel, eta ~ N(0, 1/36),
  Saat 8): 32 Verteilungen.
- **Kennzahlen:** U_H = (E_max - E_min)/E_max ueber die 32; U = max_H U_H. Eichverletzung G = lambda_max(S auf
  ker H)/lambda_max(S) (G = 0 genau dann, wenn E nur von der Holonomie abhaengt). Bezugsskala e_ref = lambda_max(S_V0).
- **Vorueberlegung [H], vor der Rechnung:** Jede gerade Kantenkette traegt im starren Geruest einen RUM: jedes
  Tetraeder an der Kette dreht um die Achse seiner Gegenkante, abwechselnd im Sinn; die Gegenkanten-Ecken bleiben
  stehen [M, Linienmode]. Durch die sechs Ringtetraeder laufen 18 solche Ketten (6 Sechseckkanten-Ketten, 6
  Aussenketten an den Ringecken, 6 Gegenkanten-Ketten). Spannen ihre Drehanteile alle 18 Richtungen auf, ist S_V3 = 0:
  jede Ringverdrehung kostet nach Relaxation nichts, unabhaengig von der Holonomie. Das ist nicht gerechnet.
- **Werkzeugprobe W [F]:** Dieselbe Auswertung auf zwei kuenstlichen Formen: Eichform S = H+^T H+ muss U = 0 und G = 0
  geben (<= 1e-12), Massenform S = Einheit muss U >= 0,5 und G = 1 geben. Faellt W, ist KT3 nicht auswertbar.

## 3. Messgroessen und Laeufe (code/kt.py, Auswertung code/kt_auswertung.py)

- **kontrolle:** Einzeltetraeder; Paar (7 Massen); gekoppeltes Paar (8 Massen, Split-Feder kappa in {1e-3, 1e-2, 0,1,
  1, 10, 100, 1e4}) mit T2-Anteil je Mode (Projektor auf die Spanne der T2-Moden beider Tetraeder); Werkzeugprobe W;
  Kontrolle der Ringgeometrie.
- **rum:** BZ-Gitter L = 24 (13 824 k, wie TENSOR-EIS-PYRO-1), 20 000 Zufalls-k (Saat 5), 2 000 Zufalls-k je Ebenenschar
  (durch Gamma oder um 2 pi verschoben, je zur Haelfte), je 200 Zufalls-k auf den drei Linien zweier Scharen
  ([100], [010], [001]) und den vier Linien dreier Scharen ([111]-Typ). Je k: n_a = 12 - Rang K(k), n_b = 12 - Rang
  C_A(k) (SVD, Schwelle 1e-9 relativ), n_fam (Zahl der Scharen durch k; Gitter ganzzahlig). Kernabbildung: jeder Kernvektor
  von K wird auf Eckverschiebungen abgebildet (u_a = t_U - [r_a]x omega_U, Phase e^{-i k.r_a}) und |C_A u|/(|C_A| |u|)
  gemessen; Hauptwinkel zwischen Bild und ker C_A. Spektren (a) und (b) an Gamma, X, L, W, K, U mit T2-Anteil (b);
  Bandbreite der T2-reichen Baender (b) auf dem Gitter L = 16 (beschreibend). Bild der RUM-Flaechen (Schnitt k_z =
  0,3 . 2 pi: log10 kleinster Singulaerwert von K mit den analytischen Ebenenspuren; 3D-Punktwolke n_a >= 1).
- **eich:** S_V0 bis S_V3 fuer Hauptring und Gegenring, L = 4 (mit dichter Gegenprobe), 8, 16, 24, 32 (Bloch). Faellt
  L = 32 nach dem Rauchlauf ueber 400 s, nur bis L = 24 (vorab festgelegt). Kontrollen: Ringgeometrie, Symmetrie von
  S, Imaginaerteile der Realraumbloecke, Kondition von Q^T M Q, Gegenring gleiche Eigenwerte, dichte Gegenprobe.

## 4. Urteilsregeln (mechanisch in kt_auswertung.py, vor dem Rauchlauf festgelegt)

- **KT0** (Kontrollen): eingetroffen genau dann, wenn
  1. Einzeltetraeder: |omega^2 - Soll| <= 1e-12 fuer alle 12 Werte (Soll 0 x 6, 1, 1, 2, 2, 2, 4), und
  2. Paar: genau 9 Nullmoden (omega^2 <= 1e-10), unter den 12 positiven keine dreifache Stufe (Stufen: relativer
     Abstand <= 1e-9), und die 6 Moden mit dem groessten T2-Anteil bilden genau zwei Singuletts und zwei Dubletts.
  - Nach Kartenwortlaut gleich. Kennzahl "wie stark": Delta = (max - min der 6 T2-reichsten omega^2)/2 und die
    Aufspaltung je Paritaet; dazu Delta(kappa) beim gekoppelten Paar (beschreibend).
  - Nachgetragen nach Rauchlauf r1 (Abschnitt 7): Hauptkennzahl fuer "wie stark" ist Delta_proj = (max - min)/2 der
    Eigenwerte des auf die T2-Spanne projizierten Blocks Q^T D Q (Einheit 2 k/m); Delta bleibt beschreibend. Die
    Urteilsregel KT0 ist unveraendert.
- **KT1** (RUM auf Flaechen wie fuer beta-Cristobalit beschrieben):
  - Nach Plan: eingetroffen genau dann, wenn alle 12 000 Ebenenpunkte n_a >= 1 haben (Flaechen) und alle 20 000
    Zufalls-k n_a = 0 (kein Volumen).
  - Nach Kartenwortlaut zusaetzlich "wie beschrieben": jede Schar traegt RUM und kein Gitterpunkt mit n_a >= 1 liegt
    ausserhalb der sechs Scharen (Wegners Ebenen).
- **KT2** (RUM-Flaechen = die sechs Ebenenscharen von TENSOR-EIS-PYRO-1):
  - Nach Plan: eingetroffen genau dann, wenn an allen Gitter-, Zufalls-, Ebenen- und Linienpunkten n_a = n_b gilt,
    auf dem Gitter n_a = n_fam (k != 0) und n_a = 6 bei k = 0, und die Kernabbildung ueberall <= 1e-9 relativ trifft.
  - Nach Kartenwortlaut ("fallen zusammen"): {k : n_a >= 1} = {k : n_b >= 1} = Vereinigung der sechs Scharen auf allen
    Punkten (ohne Vielfachheit).
- **KT3** (Eichprobe), aus V3, Hauptring, H+, groesstes gerechnetes L:
  - Entartet, wenn lambda_max(S_V3) <= 1e-8 e_ref: Die Verdrehung kostet nach Relaxation nichts, fuer jede Holonomie.
    Nach Plan dann **nicht eingetroffen (entartet)**: Es gibt keine von der Holonomie abhaengige Energie, also weder
    Kleber noch Masse. Nach Kartenwortlaut **nicht auswertbar** (Quotient 0/0).
  - Sonst nach Plan: eingetroffen genau dann, wenn U < 0,05 (alle 32 Verteilungen, alle drei H).
  - Sonst nach Kartenwortlaut (zwei Verteilungen, "gleichmaessig" gegen "alles auf T1"): eingetroffen genau dann, wenn
    max_H |E_konz,1 - E_gleich|/max(E_konz,1, E_gleich) < 0,05.
  - Voraussetzungen: Werkzeugprobe W bestanden; sonst nicht auswertbar. Aendert sich das Urteil zwischen den zwei
    groessten L, wird das als "nicht konvergiert" vermerkt (Urteil vom groessten L).
  - V0 bis V2 und H- nur beschreibend, mit denselben Kennzahlen.

## 5. Agenten-Vorhersagen (vorab; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| Z1 | n_a = n_b = n_fam an allen 13 824 Gitterpunkten (0 / 1 / 2 / 3 / 6); Kernabbildung <= 1e-12 (folgt aus 2.3) |
| Z2 | Gamma (b): 0 x 6, 2, 2, 4, 4, 4, 8 auf 1e-12; RUM je Symmetriepunkt (a): Gamma 6, X 2, L 3, W 0, K 1, U 1 |
| Z3 | Paar: 9 Nullmoden; Delta der T2-Moden zwischen 0,1 und 0,5 (in Einheiten 2 k/m) |
| Z4 | V0: U >= 0,5 (konzentriert etwa viermal teurer als gleichverteilt), G >= 0,3 |
| Z5 | V3 entartet (S_V3 = 0 bis auf Rundung) mit 55 %; falls nicht entartet, U >= 0,05 mit 90 % |
| Z6 | V1 und V2 nicht entartet, U >= 0,05 |

## 6. Laeufe auf der .69 (kleintest.sh, Spuren cpu5 und cpu3; je Lauf <= 10 min, 1 Thread, 4 GB)

| Lauf | Aufruf |
|---|---|
| KO | kt.py kontrolle --out lauf/kontrolle.json |
| RU | kt.py rum --L 24 --out lauf/rum.json --bild lauf/rum-karte.png |
| EI | kt.py eich --L_liste 8 16 24 32 --dicht 4 --out lauf/eich.json (L = 32 entfaellt nach Abschnitt 3) |
| AW | kt_auswertung.py --lauf lauf --out lauf/auswertung.json |

- Rauchlauf vorher (rauch/): kontrolle ganz (KT0-Zahlen darf ich ansehen), rum mit L = 6 und wenigen Zufallspunkten,
  eich mit kleinen L (4 dicht, 8, 16); davon nur Rueckgabewert, Zeit, Speicher und Schluessel ansehen, keine KT1- bis
  KT3-Werte. Die Auswertung laeuft im Rauch nur mit Ausgabe in eine Datei, von der ich nur die Schluessel lese.
- Danach Einfrieren: PLAN.md, code/kt.py, code/kt_auswertung.py als .eingefroren-<zeit>, Hashes in
  EINGEFROREN-SHA256.txt; code/tp.py unveraendert (Hash mitgelistet).

## 7. Rauchlaeufe vor dem Einfrieren (offengelegt; geschrieben ab 17:19:48 CEST)

- **r1** (15:17:58 bis 15:18:03 UTC, kt.py 7ab55b4a...): kontrolle (cpu5, 0,1 s, 42 MB) und rum mit L = 6, 500 Zufalls-k,
  50 je Ebene, 20 je Linie, Bild (cpu3, 4,2 s, 216 MB). Gelesen: alle KT0-Zahlen, Ringgeometrie, Werkzeugprobe; von rum
  nur Rueckgabewert und Zeit (Bild nicht angesehen).
  - KT0-Zahlen: Einzeltetraeder max. Abweichung 1,8e-15; Paar 9 Nullmoden, positive Stufen 4 Singuletts und 4
    Dubletts (0,586 g; 0,691 g x2; 1,191 u x2; 1,809 g x2; 2,309 u x2; 2,586 u; 3,414 g; 5,414 u), T2-Muster
    [1, 1, 2, 2]. Die zwei A1g-Singuletts 0,586 und 3,414 haben beide T2-Anteil 0,5; die Wahl des vierten "T2-reichsten"
    Werts entschied Rundungsrauschen (3e-16). Das Muster haengt nicht daran, Delta schon (0,80 mit 3,414, 1,00 mit
    0,586). Deshalb die projizierte Kennzahl Delta_proj (Abschnitt 4), eingefuehrt vor r2.
  - Gekoppeltes Paar: eine T2-Dreiergruppe bleibt fuer jedes kappa exakt bei omega^2 = 2 (Muster [1, 2, 3]).
  - Ringgeometrie: Ecken passen, Sechseck eben (Rest 6e-17), Seiten = Radien = l_P, Mitten abwechselnd +-0,0722 ueber
    und unter der Ebene (Sessel); Gegenring ebenso. Werkzeugprobe W bestanden (Eichform U = 9e-16, G = 6e-33;
    Massenform U = 0,833, G = 1).
- **r2** (15:19:29 bis 15:19:32 UTC, kt.py ca684a28...): kontrolle mit Delta_proj (cpu3): Paar Delta_proj = 0,774
  (Stufen 1,786 x2, 2,000, 2,278 x2, 3,333). eich mit L = 4 (dicht), 8, 16 (cpu5, 2,6 s, 191 MB). Gelesen nur
  Laufzeiten (L = 16: 1,2 s fuer beide Ringe) und Schluessel, keine Werte.
- Agenten-Vorhersage Z3 ist damit vor dem Einfrieren als verfehlt bekannt (Delta_proj 0,77 > 0,5); sie bleibt
  unveraendert stehen.
- L = 32 bleibt im Hauptlauf (Schaetzung aus r2 etwa 10 s).
