# TAKT-RAND-4D-1: Plan des Code-Agenten (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 17:33:06 CEST (date). Gelesen: KARTE.md (ganz),
  qca-windung-1/ERGEBNIS.md (Teil 1), teil2-dreieck-takt/ (ERGEBNIS.md, PLAN.md, code/teil2.py, code/auswertung2.py,
  code/windung.py in Teilen), chiral-l/DOSSIER.md Abschn. 4 bis 7.
- Ordner: lokal RUNDE-37/takt-rand-4d-1/, auf der .69 /home/fmh/fmhc-physics-remote/runde42-takt-rand-4d/ (code/, rauch/,
  lauf/). Spuren cpu3 und cpu5.
- Kennzeichen wie in der Karte: [M] eigene Mathematik (nicht gegengelesen), [E] Messung im Modell, [L] Literatur aus dem
  Gedaechtnis, [S] an der Quelle gelesen, [H] Hypothese; dazu [F] Festlegung dieses Plans, [R] im Rauchlauf gesehen,
  [P] Projektdatei.
- Die Vorhersagen und Wahrscheinlichkeiten der Karte (TR0 90 %, TR1 30 %, TR2 30 %) bleiben unveraendert. Meine eigenen
  Erwartungen stehen getrennt in Abschn. 1 und aendern nichts daran.

## 0. Literatur

### 0.1 Erwartungen vor den Abrufen (geschrieben ab 17:45:04 CEST, vor Abruf 1)

- Schon im Projekt (kein Abruf): Higashikawa/Nakagawa/Ueda 2019 (teil2-dreieck-takt/quellen/, lokal gelesen per
  pdftotext ab 17:41) [S]: "In fact, a single Weyl fermion presented in this paper corresponds to a surface state of a
  four-dimensional topological insulator [72] and to class A in d = 3 in Table I"; [72] = Qi/Hughes/Zhang, PRB 78,
  195424 (2008). Ferner: "the K-group of Floquet operators of a symmetry class in d dimensions is given by that of static
  TIs/TSCs of the same symmetry class in (d + 1) dimensions"; Literatur zu "unitary loops" [69] = Roy/Harper, PRB 96,
  155118 (2017). Kaplan, Vorlesungen arXiv:0912.2560 (chiral-l/quellen/, Text), Abschn. 3.2 bis 3.4 Domain-Wall-Fermionen.
- **F1 Rudner/Lindner/Berg/Levin, PRX 3, 031005 (2013), arXiv:1212.3324.** Erwartung [L?]: Quadratgitter mit zwei
  Teilgittern A, B; Takt aus fuenf gleich langen Schritten: in den Schritten 1 bis 4 Sprung J zwischen A und je einem
  B-Nachbarn (rechts, oben, links, unten), Schritt 5 Teilgitterpotential +-delta ohne Sprung. Bei J T/5 = pi/2 kehrt
  jedes Volumenteilchen nach einer Periode an seinen Platz zurueck (U_F = 1 bis auf die delta-Phasen), am Rand laeuft es
  einseitig um. Invariante W[U] = (1/8 pi^2) Int dt dkx dky Tr(U^-1 d_t U [U^-1 d_kx U, U^-1 d_ky U]) fuer die
  Schleife mit U(T) = 1; Zahl der Randmoden in jeder Luecke = W.
- **F2 Qi/Hughes/Zhang, PRB 78, 195424 (2008), arXiv:0802.3537.** Erwartung [L?]: 4D-Gitter-Dirac-Modell
  h(k) = Sum_i sin k_i Gamma^i + (m + c Sum_i cos k_i) Gamma^0 mit fuenf 4x4-Gamma-Matrizen; zweite Chern-Zahl
  C2 = +-1 bzw. -+3 je nach m; auf der 3D-Oberflaeche ein einzelner Weyl-Kegel (bei C2 = +-1); das ist die Gitterfassung
  der Domain-Wall-Fermionen.
- **F3 Roy/Harper, PRB 96, 155118 (2017), arXiv:1603.06944.** Erwartung [L?]: Periodensystem der Floquet-Isolatoren;
  Klasse A in geraden d: Z x Z (statische Chern-Zahl und anomale Schleifen-Windung W_{d+1}); fuer d = 4 ist W5 die
  Windung von U(k, t) ueber T^4 x S^1; kein konkretes 4D-Schrittmodell.

### 0.2 Gelesen (3 von 3 Abrufen, keine Websuche; PDFs per Abrufwerkzeug als Datei, Text per pdftotext)

- **F1 (17:45, quellen/rudner-lindner-berg-levin-1212.3324.pdf, sha256 44353c01...e9b2ee) [S]. Erwartung bestaetigt.**
  - Eq. (1): "H(k, t) = - Sum_{n=1}^{4} J_n(t) (e^{i b_n.k} sigma^+ + e^{-i b_n.k} sigma^-) + delta_AB sigma_z";
    "b1 = -b3 = (a, 0) and b2 = -b4 = (0, a)"; "One driving cycle consists of five equal length segments, of duration
    T/5"; "During step 5 all hopping amplitudes are set to 0, but the sublattice potential is still allowed to act."
  - Sonderfall: "JT/5 = pi/2 and delta_AB = 0 ... over one complete driving cycle each particle makes a loop around a
    plaquette and returns to its initial position. Therefore the bulk Floquet operator for this case is simply the
    identity"; Randmoden "with group velocities d eps/dk = +-1/T"; "the time-reversed cycle (5 - 4 - 3 - ...), which has
    the opposite chirality".
  - Eq. (4) W[U] wie erwartet; Eq. (5) "n_edge = W[U]". Fig. 3: delta_AB = 0,5 pi/T; J = 0,5 pi/T (W0 = 0, Wpi = 0),
    J = 1,5 pi/T (W0 = 0, Wpi = 1, C = 1), J = 2,5 pi/T (W0 = 1, Wpi = 1, C = 0); Streifen "unit cell 2a".
- **F2 (17:46, quellen/qi-hughes-zhang-0802.3537.pdf, sha256 02970672...afdbc) [S]. Erwartung bestaetigt.**
  - Eq. (62): "H = Sum_k psi_k^dag [Sum_i sin k_i Gamma^i + (m + c Sum_i cos k_i) Gamma^0] psi_k".
  - Eq. (67): C2(m) = 0 fuer m < -4c oder m > 4c; 1 fuer -4c < m < -2c; -3 fuer -2c < m < 0; 3 fuer 0 < m < 2c;
    -1 fuer 2c < m < 4c.
  - Eq. (68): Platte offen in w, Sprung "(c Gamma^0 - i Gamma^4)/2". Eq. (69): "there are |C2| branches of gapless
    surface states with linear dispersion ... |C2| flavors of chiral fermions"; "The factor sgn(C2) ensures that the
    chirality of the surface states is determined by the sign of the Chern number." Fig. 9: "For m = -3 there is one
    Dirac point at Gamma point while for m = -1 there are three of them at X points."
- **F3 (17:46, quellen/roy-harper-1603.06944.pdf, sha256 9c89aea1...dc5abc) [S]. Erwartung teils.**
  - Theorem III.1: "Every unitary U in U^S_{0,pi} can be continuously deformed to a composition of a unitary loop L and a
    constant Hamiltonian evolution C ... L and C are unique up to homotopy." "static topological insulators correspond
    to compositions of nontrivial constant Hamiltonian evolutions with trivial unitary loops. More general dynamical
    topological phases arise through compositions of constant evolutions with nontrivial unitary loops."
  - Table II, Klasse A: d = 0, 2, 4, 6: "Z x Z"; Eq. (35): Schleifen der Klasse A klassifiziert durch K^0(X).
  - Eine W5-Formel und ein 4D-Beispielmodell habe ich im Text nicht gefunden (grep; nicht ganz gelesen).

## 1. Schreibtisch [M] (vor jeder Rechnung)

- **D1 Schrittplan (streng lokal).** Gamma_1..Gamma_3 = tau_x (x) sigma_{x,y,z}, Gamma_4 = tau_y (x) 1,
  Gamma_5 = tau_z (x) 1 (paarweise antikommutierend, Quadrat 1). Je Richtung j: A_j(k_j) = sin k_j Gamma_j -
  cos k_j Gamma_5, A_j^2 = 1, also W_j(a) = exp(-i a A_j) = cos a - i sin a A_j mit Fourier-Anteilen nur bei 0 und
  +-e_j (Reichweite 1). Massenschritt W_5(beta) = exp(-i beta Gamma_5) (vor Ort).
  - Palindromischer Takt (P4a, P4b, P4t): W_1 W_2 W_3 W_4 W_5 W_4 W_3 W_2 W_1 mit a = tau/2, beta = M tau. BCH:
    U = exp(-i tau h(k) + O(tau^3)) mit h = Sum_j sin k_j Gamma_j + (M - Sum_j cos k_j) Gamma_5.
  - Abbildung auf QHZ Eq. (62): Gamma^0 = -Gamma_5, c = 1, m = -M. Also P4a (M = 3): m = -3, C2 = 1 (in der Orientierung
    der Quelle), ein Oberflaechenkegel bei k_par = 0; P4b (M = 1): m = -1, C2 = -3, drei Kegel an den X-Punkten;
    P4t (M = 5): m = -5, C2 = 0, keine Randkegel.
  - Ecken-Massen (Pruefung): an den 16 Ecken kommutieren alle Schritte, U = exp(-i tau (M - 4 + 2 n_pi) Gamma_5)
    (n_pi = Zahl der Komponenten gleich pi). Ein Randkegel bei k_par entsteht, wo die zwei auf k_par projizierten Ecken
    (k4 = 0, pi) verschiedene Vorzeichen haben: P4a nur k_par = 0 (-tau, +tau); P4b die drei X-Punkte (-tau, +tau);
    P4t nirgends. Groesster Betrag 7 tau = 2,1 < pi: keine Randknoten in der Luecke bei pi erwartet.
- **D2 Platte.** Der Schritt in x4 ist A_4 = -B T_+ - B^dag T_- mit B = (Gamma_5 + i Gamma_4)/2, B^2 = 0,
  BB^dag = Q = (1 - i Gamma_5 Gamma_4)/2 (Projektor vom Rang 2). A_4 koppelt nur Q bei w mit (1 - Q) bei w + 1, also
  getrennte Dimere. Auf L Lagen (offen) bleiben (1 - Q) bei w = 0 und Q bei w = L - 1 ungepaart; A_4^2 = Pi
  (Dimer-Projektor), W_4 = (1 - Pi) + cos a Pi - i sin a A_4 ist exakt unitaer und hat Reichweite 1. Das ist dieselbe
  Randbedingung wie QHZ Eq. (68) mit c = 1. Die Platte ist ein endlichreichweitiger 3D-Automat mit 4L inneren Zustaenden.
- **D3 Ableitbarkeit [M, mit S].** Fuer kleines tau ist der Takt stetig mit exp(-i tau h) verbunden; solange die
  Luecken bei 0 und pi offen bleiben, aendert sich die Topologie nicht. Damit ist TR1 fuer P4a **vorab ableitbar**
  (QHZ Eq. 67, 69, Fig. 9), sofern die Luecken offen sind. Die Rechnung prueft die Ausfuehrung: streng lokaler
  Schrittplan, Dimer-Rand, Zahl, Ort, Chiralitaet und Zuordnung der Randknoten, Isotropie. Das steht so im Ergebnis.
- **D4 Reiner Takt in 4D [M, haengt an T2 aus Teil 2, ungeprueft].** Hat ein streng lokaler 4D-Schrittplan im Volumen
  exakt U_F = 1 (wie Rudners Sonderpunkt in 2D), dann zerfaellt die Platte in U_oben (+) 1 (+) U_unten; U_oben wirkt auf
  endlich viele Lagen und ist ein endlichreichweitiger 3D-Automat. Nach T2 gilt W3(U_oben) = 0, nach Bessho/Sato
  Theorem 3' [S, Teil 1] ist dann die Netto-Chiralitaet der Randknoten bei jeder Quasienergie 0. **Ein reiner Takt kann
  in 4D also keinen ungepaarten Rand-Weyl tragen**; in 2D geht es, weil die 1D-Randwelle eine Verschiebung mit
  Windung von det sein darf. Ein ungepaarter Rand-Weyl braucht in 4D Volumenbaender mit C2 ungleich 0 (statischer Anteil
  nach Roy/Harper) oder quasilokale Schritte. Nicht gerechnet, nur als Folgerung.
- **D5 Takt-Umkehr [M].** U_rueck(tau, beta) = [U_vor(-tau, -beta)]^dag: gleicher Term erster Ordnung, Term zweiter
  Ordnung mit umgekehrtem Vorzeichen. Bleiben die Luecken offen und ist der Weg zum statischen Modell stetig, dann haben
  P4c und P4cr dieselbe Rand-Chiralitaet. Anders als in 2D (Rudner: Umkehr dreht die Chiralitaet, Quelle S. 4), wo die
  Haendigkeit allein aus dem Takt kommt. Erwartung [H]: gleiches Vorzeichen; falls eine Luecke schliesst, nicht
  auswertbar.
- **D6 Summenregel [M].** Die Platte ist endlichreichweitig, also W3(Platte) = 0 (T2); damit ist die Netto-Chiralitaet
  aller Knoten bei jeder Quasienergie 0. In einer Volumenluecke gilt also netto(oben) = -netto(unten). Das ist eine
  Pruefung der Suche, kein Urteil.

## 2. Rechnungen [F]

- **R2 (2D-Kontrolle, Rudner u. a. Eq. 1):** T = 1, Streifen periodisch in x (k), offen in y, W = 40 Zellen, Basis
  A(m), B(m); Term e^{i b.k} sigma^+ <-> A(r) - B(r + b). Je Abschnitt exakte Exponentialfunktion (eigh). Faelle:
  R1_sonder (J = 2,5 pi, delta = 0), R2_anomal (J = 2,5 pi, delta = 0,5 pi; Fig. 3c), R2r_anomal_umkehr (Takt
  5-4-3-2-1), R3_chern (J = 1,5 pi, delta = 0,5 pi; Fig. 3b).
  - Volumenluecken: halbe Breite um 0 und pi aus 240^2 k-Punkten; eine Luecke gilt als offen ab 0,05.
  - **Randfluss ohne Zustandsverfolgung:** N_b(phi0) = - Int dk Re Tr[P_b g(U(k)) V(k)], V = -i U^dag dU/dk
    (Mittendifferenz, h = 1e-4), g = Kosinusfenster um phi0 mit Integral 1, halbe Breite dw = min(0,5 x halbe Luecke,
    0,5); P_b = Projektor auf die obere bzw. untere Haelfte, dazu P = 1 ("alle"). Jeder volle Durchgang eines Randzustands
    durch das Fenster gibt +-1 (Vorzeichen von d eps/dk, eps = -phi). Basisfrei, auch bei Entartung. 1200 k-Werte.
  - **K-chi:** Chiralitaetskonvention an U = exp(-i d.sigma), d = (sin k1, sin k2, sin k3): H = +k.sigma bei Gamma gibt
    chi = +1; Soll Gamma +1, X1 = (pi,0,0) -1, X12 = (pi,pi,0) +1, R = (pi,pi,pi) -1.
- **P4 (4D):** Modelle P4a (tau = 0,3, M = 3, palindromisch, L = 16), P4b (M = 1), P4t (M = 5), P4c (M = 3, Takt
  1-2-3-4-5 mit a = tau: U = W5 W4 W3 W2 W1), P4cr (M = 3, Takt 5-4-3-2-1: U = W1 W2 W3 W4 W5), P4aL24 (wie P4a, L = 24).
  - Volumenluecken: halbe Breite um 0 und pi aus 20^4 k-Punkten (Ecken enthalten); offen ab 0,05.
  - Randzustaende: Eigenzerlegung der Platte (komplexe Schur-Form); in fast entarteten Haufen (Phasenabstand < 1e-7)
    wird die Basis so gedreht, dass sie P_oben diagonalisiert. Rand oben: Gewicht in der oberen Haelfte > 0,9; unten:
    < 0,1. Fenster: |phi| < 0,97 x halbe Luecke (bei 0) bzw. |phi| > pi - 0,97 x halbe Luecke (bei pi).
  - **Knotensuche je Rand und Luecke:** Gitter A (20^3, ohne Versatz) und Gitter B (17^3, halber Versatz); bei L = 24
    wegen der Laufzeit 14^3 und 11^3. Kandidaten: lokale Minima des kleinsten Abstands benachbarter Randphasen
    (< 0,6, hoechstens 60 je Rand und Luecke) und alle exakt entarteten Paare an den 8 Punkten mit Komponenten 0 oder pi.
    Newton auf den sigma-Anteil des Paares (wie Teil 1), Treffer bei Paarabstand <= 1e-9; zusammenfassen (k auf 1e-5,
    Phase auf 1e-6).
  - **Chiralitaet:** chi = Vorzeichen von det V, V = -M, M_lj = Re tr(G_l sigma_j)/2, G_l = e^{-i phi_c} Q^dag d_l U Q / i
    (H_eff = Sum q_l V_lj sigma_j; Konvention per K-chi gesichert).
  - **Vollstaendig:** Gitter A und B geben je Rand und Luecke dieselben Knoten (Zahl, Lage auf 1e-5, Chiralitaet).
  - **Isotropie des tiefsten Kegels je Rand** (kleinstes |phi| ueber alle offenen Luecken): v(n) = |Delta phi|/(2 q) der
    zwei Randphasen des Rands, die dem Knoten am naechsten liegen, an k_W + q n fuer 400 Fibonacci-Richtungen, q = 0,01,
    0,05, 0,2; Mass (max - min)/Mittel. Dazu linear: Singulaerwerte von V.

## 3. Lehre aus Teil 1 und 2 [F]

- Keine relativen Schwellen auf verschwindende Groessen. Absolute Schwellen: Unitaritaet <= 1e-10; ganzzahlig heisst
  |N - round(N)| < 0,05 (Karte); offen heisst halbe Luecke >= 0,05.
- Randfluss mit Summenprobe: N_alle muss 0 sein (|N_alle| < 0,05), sonst gilt der Fall nicht als einseitig.
- Zaehlung basisfrei (Fensterformel), kein Eigenvektor-Ueberlapp.

## 4. Urteilsregeln (mechanisch in code/auswertung.py)

- **Vorbedingungen:** alle Laeufe Modus haupt mit rc = 0; K-chi trifft alle vier Soll-Vorzeichen.
- **TR0 (Plan):** Vorbedingungen und Unitaritaet aller R-Faelle <= 1e-10; benoetigte Luecken offen: R1 bei pi, R2,
  R2r und R3 bei 0 und pi. "Einseitig" heisst: N_oben, N_unten ganzzahlig, |N_alle| < 0,05, round(N_oben) ungleich 0,
  round(N_unten) = -round(N_oben). "Null" heisst: beide gerundet 0, ganzzahlig, |N_alle| < 0,05.
  Eingetroffen genau dann, wenn: R1 bei pi einseitig; R2 bei 0 und pi einseitig; R3 bei 0 null und bei pi einseitig
  (Quelle Fig. 3b: W0 = 0, Wpi = 1); R2r bei 0 und pi einseitig mit round(N_oben) = -round(N_oben von R2). Sonst nicht
  eingetroffen; fehlt eine Vorbedingung oder Luecke: nicht auswertbar.
  **Kartenwortlaut:** R2 in mindestens einer Luecke einseitig.
- **TR1 (Plan, Hauptmodell P4a):** Vorbedingungen; Unitaritaet von Platte und Volumen <= 1e-10; Suche vollstaendig;
  mindestens eine Luecke offen. Eingetroffen genau dann, wenn es eine offene Luecke gibt, in der der obere Rand eine
  ungerade Zahl von Knoten mit Netto-Chiralitaet ungleich 0 traegt und der untere Rand eine ungerade Zahl mit
  netto(unten) = -netto(oben). Sonst nicht eingetroffen; fehlt eine Vorbedingung: nicht auswertbar.
  **Kartenwortlaut:** "bei einer Quasienergie" lese ich als "in einer Quasienergie-Luecke". Dieselbe Regel fuer jeden
  vorab genannten streng lokalen Schrittplan P4a, P4b, P4c, P4cr: eingetroffen, wenn einer sie erfuellt; nicht
  eingetroffen, wenn alle auswertbar sind und keiner; sonst nicht auswertbar. P4t (Gegenprobe) und P4aL24 (Dicke) zaehlen
  nicht mit.
- **TR2 (Plan):** nur wenn TR1 (Plan) eingetroffen, sonst nicht auswertbar. Eingetroffen genau dann, wenn bei P4a der
  tiefste Kegel beider Raender bei q = 0,05 alle 400 Richtungen gefunden hat und (max - min)/Mittel <= 0,10.
  **Kartenwortlaut:** erstes Modell in der Reihenfolge P4a, P4b, P4c, P4cr, das TR1 nach Kartenwortlaut erfuellt; der
  tiefste Kegel (kleinstes |phi| ueber beide Raender; bei Gleichstand auf 1e-6 alle gleich tiefen) isotrop wie oben.
- **Vermerke (zaehlen nicht):** Zaehlung, Lage und Chiralitaet aller Modelle; Summenregel je Luecke; P4t (Erwartung:
  keine Knoten); P4b (Erwartung: drei je Rand); Takt-Umkehr P4c gegen P4cr; Dicke P4a gegen P4aL24; Isotropie bei
  q = 0,01 und 0,2 und linear.

## 5. Rauchlauf, Sichtregel, Laufplan

- Rauchlaeufe (Modus rauch): R2 ganz sichtbar (Kontrolle, W = 24, 300 k-Werte); P4 nur Zeiten, Speicher, Unitaritaet
  und ob die Kette ohne Ausnahme durchlaeuft (kleines Suchgitter 5^3, Ergebnis nicht geschrieben; keine Volumenluecken,
  Knoten, Zahlen, Chiralitaeten, Isotropie).
- Hauptlaeufe: R2, P4a, P4b, P4t, P4c, P4cr, P4aL24 abwechselnd auf cpu3 und cpu5 (hoechstens zwei zugleich), danach
  auswertung.py. Ein Lauf, der ausserhalb des Codes scheitert (Starter, Netz), darf einmal wiederholt werden; Fehler im
  eingefrorenen Code machen die betroffenen Urteile "nicht auswertbar". Kein Code-Wechsel nach dem Einfrieren;
  Diagnosen nur als eigene Skripte und als solche gekennzeichnet.

## 6. Rauchlaeufe [R] (vor dem Einfrieren)

- R2 rauch (15:56:07 bis 15:56:23 UTC, cpu3, rc = 0, 16,2 s, 84 MB): Volumen-Halbluecken R1 (0; pi), R2 und R2r
  (0,266; 2,305), R3 (0,449; 0,921). Randfluss (oben, unten, alle): R1 bei pi (-2,000; +2,000; 0); R2 bei 0 (-2,000;
  +2,000; 0) und bei pi (-2,000; +2,000; 0); R2r jeweils (+2; -2; 0); R3 bei 0 (0; 0; 0), bei pi (-2,000; +2,000; 0).
  Unitaritaet <= 1,8e-15. K-chi: Gamma +1, X1 -1, X12 +1, R -1 (alle wie Soll).
  - **Faktor 2 gegenueber W = 1 der Quelle [M]:** In meiner Zellbeschriftung (A(r) - B(r + b)) zerfaellt der Graph nach
    der Paritaet von x + m in zwei entkoppelte Kopien von Rudners Gitter; ausserdem gilt H(k + (pi, pi)) = sigma_z H(k)
    sigma_z, die k-Zone [-pi, pi]^2 ueberdeckt die echte Zone also zweimal. Jede Kopie traegt eine Randmode je Rand. Die
    Quelle rechnet den Streifen mit "unit cell 2a". Die Regeln verlangen nur ganzzahlig, ungleich 0 bzw. 0 und
    entgegengesetzt; keine Regel geaendert.
- P4a rauch (15:56:07 bis 15:56:09 UTC, cpu5, rc = 0, 1,5 s, 76 MB): Unitaritaet Platte und Volumen 1,3e-15; eine
  Zerlegung (D = 64) 8,3 ms; Suche 5^3 1,3 s. Hochgerechnet: Gitter A und B (12 913 Punkte) etwa 110 s, mit Newton und
  Isotropie etwa 2 bis 3 min.
- P4c rauch (15:57:15 bis 15:57:17 UTC, cpu5, rc = 0): Unitaritaet 7,8e-16; 7,1 ms je Zerlegung.
- P4aL24 rauch (15:57:15 bis 15:57:20 UTC, cpu3, rc = 0, 97 MB): 26 ms je Zerlegung (D = 96). Mit 20^3 und 17^3 waeren es
  etwa 6 min nur fuer die Gitter; deshalb vor dem Einfrieren fuer L = 24 die Suchgitter 14^3 und 11^3 festgelegt
  (etwa 2 min plus Isotropie etwa 1 min).
- Aenderungen: vor dem ersten Rauchlauf die Ausgabe der Zahl der Newton-Starts im P4-Rauchmodus gestrichen (zu nah an
  einer Knotenzahl); nach dem ersten Rauchlauf nur die Suchgitter je Plattendicke (oben). Keine Urteilsregel geaendert,
  keine 4D-Physikwerte gesehen.
- Test der Auswertung (rauch/test/): auswertung.py an handgeschriebenen Schein-Dateien (keine Rechenwerte), nur auf
  Laufzeitfehler und Regelpfade geprueft.
