# REGGE-4D-1: Plan (Code-Agent, Runde 36)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 00:54:11 CEST (date). Plantext ab 01:16:51 CEST (date),
  vor jeder Rechnung zu dieser Karte.
- Grundlage: KARTE.md (unveraendert uebernommen: Schreibtisch, Test, G0 bis G3 mit Schwellen).
- **Kennzeichen:**
  - [S] an der Quelle gelesen
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik (Schreibtisch)
  - [F] Festlegung dieses Plans (von der Karte offen gelassen)
  - [H] Hypothese
- **Gelesen** (1 Abruf, PDF arXiv:gr-qc/0012035, Regge/Williams 2000, S. 2-5 und 22-25):
  - S. 2, Gl. 1-2 [S]: "the analogue of the Einstein action I = 1/2 Int R sqrt(g) d^n x ... is given by
    I_R = Sum_hinges |sigma^i| eps_i", eps_i "equal to 2 pi minus the sum of the dihedral angles between the faces
    of the simplices meeting at that hinge".
  - S. 3, Gl. 3 [S]: Schlaefli, die Variation der Winkelterme verschwindet in Summe ueber jedes Simplex.
  - S. 23-24 [S], Rocek/Williams: Hyperkubus "divided into simplices by drawing in various diagonals, giving fifteen
    edges per vertex"; l_i = l_i^(0)(1 + delta_i); delta^2 S = delta_i M_ij delta_j; Fourier in den Richtungen
    (1, 2, 4, 8) (binaere Kantennummern); "M_omega has four zero modes, corresponding to periodic translations of
    points of the lattice, and a fifth zero mode corresponding to periodic fluctuations of the hyperbody diagonal.
    Block diagonalising M_omega decouples four further modes; they enter without omega's ... leaving ten degrees of
    freedom per vertex".
  - S. 24-25 [S], Flaechenvariablen (nicht unser Fall): "four zero modes ... and six further modes scaling with k^2".
  - Primaerquelle Rocek/Williams 1981 (PLB 104, 31) nicht gelesen. Barnes-Rivers: kein Abruf; die Zerlegung ist unten
    selbst hergeleitet [M].

## 1. Gitter und Simplizes [M]

- Kuhn-Zerlegung (Freudenthal) von Z^4: je Wuerfel an x und Permutation p von (0,1,2,3) ein Simplex
  x, x + e_p0, x + e_p0 + e_p1, ..., x + (1,1,1,1). 4! = 24 Simplizes je Ecke.
- Kanten: alle 0/1-Vektoren d != 0, je Ecke 15 (4 Achsen, 6 Flaechen-, 4 Raumdiagonalen, 1 Hyperdiagonale).
- Gelenke (Dreiecke): Ketten x, x + a, x + a + b mit disjunkten, nicht leeren 0/1-Vektoren a, b; je Ecke
  3^4 - 2 * 2^4 + 1 = 50.
- Je Ecke 60 Tetraeder; Euler 1 - 15 + 50 - 60 + 24 = 0 (Torus).
- Torus L = 4 (256 Ecken, 6144 Simplizes, 12800 Dreiecke) fuer den Weg T. Gegenprobe L = 3.
- Inversion x -> -x bildet das Gitter auf sich ab; Spiegelungen einzelner Achsen nicht. Symmetrie: S4 x Z2
  (48 Elemente). Die Hyperdiagonale (1,1,1,1) ist eine ausgezeichnete Richtung.
- Kontrolle n = 3 (Kuhn 3D, 6 Tetraeder je Wuerfel, 7 Kanten je Ecke, Gelenke = Kanten) mit demselben Code.

## 2. Variablen, Formeln, Fourier

- **[F1] Variablen: s_e = l_e^2.**
  - Begruendung: delta(l_e^2) = e^mu e^nu h_mu_nu ist exakt linear in h.
  - Die Signatur haengt nicht davon ab (Sylvester; delta s = 2 l delta l ist diagonal und positiv). Die Zaehlungen
    gelten also auch fuer l und fuer delta = delta l / l (Rocek/Williams).
- **Einbettung:** Gram-Matrix G_ab = (s_0a + s_0b - s_ab)/2 (a, b = 1..4), Cholesky G = P P^T; Zeilen von P sind die
  Ecken im R^4.
- **Diederwinkel am Dreieck t im Simplex sigma:** Die Ecken m, m' von sigma ausserhalb t werden auf das
  2-dimensionale orthogonale Komplement der Dreiecksebene projiziert (QR). Der Winkel zwischen den Projektionen ist
  der Winkel zwischen den Tetraedern t + m und t + m' (atan2, Wert in [0, pi]).
- **Fehlwinkel:** eps_t = 2 pi - sum_{sigma enthaelt t} theta_{sigma,t} [S, S. 2].
- **Flaeche:** Heron in s: 16 A^2 = 2 s_a s_b + 2 s_b s_c + 2 s_c s_a - s_a^2 - s_b^2 - s_c^2, also
  dA/ds_a = (s_b + s_c - s_a)/(16 A) [M]. In 3D: dl/ds = 1/(2 l).
- **Zweite Ordnung** [M, Schlaefli; S, S. 3]:
  - dS/ds_e = sum_t (dA_t/ds_e) eps_t exakt, also im flachen Gitter
    M_ee' = d^2 S/ds_e ds_e' = sum_t (dA_t/ds_e)(d eps_t/ds_e').
  - S = sum_t A_t eps_t, Hesse-Konvention: S^(2) = 1/2 sum M_ee' ds_e ds_e'.
- **[F2] Vorzeichen: H(k) := -M(k).**
  - S = sum A eps entspricht 1/2 Int R sqrt(g) [S, Gl. 1-2].
  - Die euklidische Einstein-Hilbert-Wirkung ist I_E = -(1/16 pi G) Int R sqrt(g) = -(1/8 pi G) sum A eps [L]. Auf sie
    beziehen sich "Spin 2 positiv, konformer Modus negativ" der Karte.
  - H hat dieses Vorzeichen. Die rohe Hesse-Matrix von S hat die umgekehrte Signatur; sie wird mitberichtet.
- **[F3] Fourier, Mittelpunktskonvention:**
  - ds_(x,d) = sum_k exp(i k.(x + d/2)) u_d(k).
  - M_dd'(k) = sum_R M_(0,d),(R,d') exp(i k.(R + d'/2 - d/2)) = sum_tau conj(A_tau,d(k)) E_tau,d'(k), mit
    A, E den Fourier-Bildern (50 x 15) von dA/ds und d eps/ds (Bezugspunkt der Dreiecke: Schwerpunkt, faellt heraus).
  - Wegen der Inversionssymmetrie ist M(k) dann reell, symmetrisch und gerade in k [M]. Geprueft wird der Imaginaerteil.
  - Pro Ecke S^(2) = (N/2) sum_k u^+ M(k) u.
- **[F4] Ableitungen d eps_t/ds_e:**
  - Weg T (Karte): Torus L = 4, Kante (0, d) um +-h verstimmt, alle Fehlwinkel neu. Zentrale Differenz mit Richardson
    aus h = 1e-3 und h/2; Fehlerschaetzung gegen Richardson aus 2h und h.
  - Nicht betroffene Dreiecke ergeben bitgleich 0. Betroffene Dreiecke werden in [-1, 2]^4 abgewickelt. Es wird
    geprueft, dass alle in [-1, 1]^4 liegen, also keine Ueberlappung mit Bildern vorliegt [M: alle Simplizes, die
    (0, d) enthalten, liegen in [-1, 1]^4]. L = 3 als Gegenprobe der Torusgroesse.
  - Weg J (Gegenprobe): lokale 10 x 10-Jacobimatrix d theta/ds je Simplextyp (24), ohne Torus zusammengesetzt.

## 3. Abbildung h -> Kanten; Eichmoden

- **[F5]** h als 10-Vektor in der Frobenius-orthonormalen Basis der symmetrischen 4 x 4-Matrizen (E_mm und
  (E_mn + E_nm)/sqrt 2).
  - B0: ds_d = d^mu d^nu h_mu_nu (Karte), 15 x 10, k-unabhaengig in der Mittelpunktskonvention.
  - Die Variante mit Sehnenfaktor sinc(k.d/2) wird nicht verwendet.
- **Gitter-Eichmoden** (Eckenverschiebung xi exp(i k.x)): u_d = 4 i sin(k.d/2) (d.xi). Exakte Nullvektoren von M(k)
  fuer jedes k [M]. Im Kontinuum h = i(k xi + xi k).
- **Bei k = 0** sind die affinen Verzerrungen range(B0) exakte Nullvektoren (10).

## 4. Effektive 10 x 10-Form (Schur-Komplement)

- K = B0^T H B0 - B0^T H C (C^T H C)^+ C^T H B0.
- **[F6] Komplement:** C = [e_top, C4].
  - e_top ist die Hyperdiagonale.
  - C4 ist die Orthonormalbasis des orthogonalen Komplements von range(B0 ohne Hyperdiagonal-Zeile) in R^14, also
    4-dimensional.
  - Pseudoinverse ueber die Eigenzerlegung, Eigenwerte unter 1e-8 * max verworfen.
  - Begruendung siehe A1: e_top ist voraussichtlich exakter Nullvektor und koppelt nicht. Ein Komplement ohne e_top
    machte C^T H C bei k -> 0 fast singulaer.
  - Ist e_top kein Nullvektor, bleibt C ein gueltiges Komplement; die Formel gilt unveraendert.
- **Variante (nur berichtet):** direkte Form B0^T H B0 ohne Ausintegrieren.
  - Wegen M(k) = M0 + O(k^2) und M0 B0 = 0 ist B0^T H C = O(k^2), also die Schur-Korrektur O(k^4) [M].
  - Die Wahl des Komplements wirkt erst in O(k^4).

## 5. Spinprojektoren und Normierung [M]

- n = k/abs(k), theta = 1 - n n, omega = n n.
- Projektoren auf symmetrische X:
  - P2 X = theta X theta - theta tr(theta X)/(d - 1)
  - P1 X = theta X omega + omega X theta
  - P0s X = theta tr(theta X)/(d - 1)
  - P0w X = omega tr(omega X)
  - Raenge 5, 3, 1, 1 (d = 4); in d = 3: 2, 2, 1, 1.
- **Koeffizienten:**
  - c_J = tr(P_J K)/(Rang_J k^2)
  - c0s = s^T K s/k^2 mit s = theta/sqrt(d - 1); c0w und c0sw entsprechend
  - Spin-2-Block: 5 Eigenwerte von Q2^T K Q2 / k^2 (Q2 Orthonormalbasis von range P2)
  - Mischungen: norm(P_J K P_J')/norm(K)
- **Kontinuum [M]:**
  - (sqrt(g) R)^(2) = -(1/4) h k^2 (P2 - (d - 2) P0s) h (Fourier).
  - Geprueft am TT-Modus: -(1/4)(d h)^2.
  - Geprueft am konformen Modus h = 2 sigma delta: Int sqrt(g) R = (d - 1)(d - 2) Int (d sigma)^2, in d = 4 also 6.
  - Mit S = 1/2 Int sqrt(g) R und der Normierung aus [F3] folgt fuer H = -M:
    K -> (1/4) k^2 (P2 - (d - 2) P0s).
  - Also c2 = 1/4 und c0s = -1/2 in 4D (Verhaeltnis -2, Karte), in 3D c0s = -1/4 (Verhaeltnis -1).
  - Eichinvarianz: c1 = c0w = c0sw = 0 im Kontinuum.

## 6. k-Punkte und Zaehlregeln

- **[F8] Richtungen** (8): (1,0,0,0), (1,1,0,0), (1,-1,0,0), (1,1,1,0), (1,1,1,1), (1,1,-1,-1), (1,1,1,-1),
  (1,2,3,4), je normiert. Betraege abs(k) = 0,05; 0,1; 0,2; 0,4; dazu k = 0.
- **[F9] Klassen je k-Punkt** (Eigenwerte lambda von H(k), Lambda = max abs(lambda)):
  - Null: abs(lambda) < 1e-6 Lambda (Karte: "< 1e-6 relativ").
  - h-Anteil eta = v^T Pi_h v, Pi_h = Orthogonalprojektor auf range(B0).
  - Kontinuumsmode: nicht null und eta > 1/2. Gittermode: nicht null und eta <= 1/2.
  - Begruendung: Bei k = 0 ist range(B0) im Kern, Eigenvektoren mit lambda != 0 stehen senkrecht darauf (eta = 0).
    Kontinuumsmoden haben eta = 1 - O(k^4).
- Beschreibend: feine Kurven abs(k) = 0,01 bis pi je Richtung; Brillouin-Zone 8^4 Gitterimpulse (Zaehlung
  null/positiv/negativ).

## 7. Urteilsregeln (vor jeder Rechnung)

- **G0 eingetroffen**, wenn alle drei Teile gelten:
  - (a) max abs(eps_t) < 1e-12 auf dem Torus L = 4 (Karte).
  - (b) [F10] Hermitezitaet: max ueber k von max abs(M - M^+)/max abs(M) < 1e-8, auf 64 Zufalls-k und allen
    Leiterpunkten.
  - (c) Bei k = 0 genau 10 Eigenwerte mit abs(lambda) < 1e-6 Lambda, und die affinen Verzerrungen liegen im Kern
    (norm(H Q_B)/Lambda < 1e-6) (Karte).
- **G1 eingetroffen**, wenn an allen 32 Punkten mit abs(k) in {0,05; 0,1; 0,2; 0,4} gilt (Karte, mit [F11]):
  - (a) Zahl der Nullmoden 4 oder 5 (die fuenfte ist laut Karte erlaubt).
  - (b) Die 4 Gitter-Eichmoden liegen im Nullraum: norm(H Q_G)/Lambda < 1e-6.
  - (c) Kontinuumsmoden: genau 5 positiv und genau 1 negativ (in H).
  - (d) [F11] k^2-Skalierung, je Richtung: die sortierten Werte lambda/k^2 der Kontinuumsmoden bei abs(k) = 0,1 und
    0,2 weichen von denen bei 0,05 um hoechstens 10 % ab.
  - (e) [F11] Gittermoden O(1), je Richtung: die sortierten Gitter-Eigenwerte bei 0,1 und 0,2 haben zu denen bei 0,05
    das Verhaeltnis 0,5 bis 2.
  - Die Gittermoden sind dann 9 minus Zahl der Nullmoden, also 5 oder 4 plus die Nullmode.
- **G2 eingetroffen**, wenn fuer alle 8 Richtungen und abs(k) in {0,05; 0,1; 0,2} gilt:
  abs(r/(-2) - 1) <= 0,10, mit r = c0s/c2 aus der Schur-Form (Karte; [F7]: c_J wie in Abschnitt 5).
- **G3 eingetroffen**, wenn fuer jedes abs(k) in {0,05; 0,1; 0,2} gilt: Ueber alle 8 Richtungen x 5
  Spin-2-Eigenwerte/k^2 (40 Werte) ist max abs(x/Mittel - 1) <= 0,05. Das umfasst "nicht von der Richtung abhaengig"
  und "fuenffach entartet" [F12].
- **Nicht auswertbar:**
  - G1 bis G3, wenn max abs(eps) > 1e-8 (Geometrie falsch) oder die Schur-Form fehlt.
  - Ein Verfehlen von G0 (c) allein sperrt G1 bis G3 nicht.
- Urteile mechanisch durch code/regge4d_auswertung.py nach lauf-69/auswertung.json.

## 8. Agenten-Vorhersagen (Schreibtisch, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Die Hyperdiagonale ist bei **jedem** k ein exakter Nullvektor von M(k). Grund [M]: Die 14 Dreiecke, die (0, 1111) enthalten, sind (0, a, 1111). Ihr Winkel an a ist recht, denn (-a).(1111 - a) = 0 (Thales). Also gilt dA_t/ds_hd = (s_b + s_c - s_hd)/(16 A) = 0; die Zeile von M verschwindet, wegen der Symmetrie auch die Spalte. Das ist Rocek/Williams' fuenfte Nullmode [S]. **Folge: Bei k = 0 gibt es 11 Nullmoden, G0 (c) und damit G0 sind nicht eingetroffen**, wenn die Numerik stimmt | 90 % |
| A2 | Bei k != 0 genau 5 Nullmoden (4 Eichmoden + Hyperdiagonale); 6 Kontinuumsmoden (5+, 1-); 4 Gittermoden O(1), die bei k -> 0 gegen feste Werte gehen | 75 % |
| A3 | Die Schur-Form trifft (1/4) k^2 (P2 - 2 P0s): c2 = 1/4 und r = -2 auf <= 1 % bei abs(k) = 0,05 und <= 3 % bei 0,2. G2 und G3 eingetroffen | 70 % |
| A4 | Schur-Form und direkte Form unterscheiden sich bei abs(k) = 0,1 um < 1 % (relativ, Frobenius) | 80 % |
| A5 | 3D-Kontrolle: keine Zusatz-Nullmode; bei k = 0 genau 6 Nullmoden, bei kleinem k 3 Eichmoden, 2 positive und 1 negative Kontinuumsmode, 1 Gittermode; c2 = 1/4 und c0s/c2 = -1 auf <= 1 % bei abs(k) = 0,05 | 75 % |
| A6 | Hermitezitaet und Weg T gegen J auf <= 1e-9; Fehlwinkel flach auf <= 1e-13 | 85 % |
| A7 | Keine weiteren Nullmoden in der Brillouin-Zone ausser bei q = 0 (dort 11) | 60 % |

- Wenn A1 zutrifft, ist das Urteil "G0 nicht eingetroffen" kein Geometriefehler. Die Karte hat die fuenfte Nullmode
  bei k = 0 nicht vorgesehen; sie steckt dann schon in den Kanten- und Flaechenformeln.

## 9. Kontrollen (beschreibend, nicht geurteilt)

- Flachheit unter gleichmaessiger Skalierung (l * 1,3) und unter zufaelliger affiner Verzerrung.
- Simplizes je Dreieck und je Kante; die Werte der flachen Diederwinkel.
- Schlaefli je Simplex: sum_t A_t d theta_t/ds_e = 0; global: sum_tau A_tau E_tau,d(0) = 0.
- Weg T gegen Weg J; L = 3 gegen L = 4; Richardson-Fehlerschaetzung.
- Imaginaerteil von M(k) (Mittelpunktskonvention).
- Kontinuums-Eichmoden h = k xi + xi k gegen K (Rest O(k^2) erwartet).
- Mischungen P_J K P_J' und c1, c0w, c0sw.
- Variante direkte Form.
- 3D-Kontrolle mit demselben Code (Erwartung A5).

## 10. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde36-regge4d/, Start nur ueber kleintest.sh, Spuren cpu3 und cpu4.
- **Rauchlauf** (vor dem Einfrieren):
  - `regge4d.py rauch`: n = 3 vollstaendig (Kontrolle, nicht geurteilt).
  - n = 4 nur Geometrie: Flachheit, Diederwinkel, Schlaefli, Weg T gegen J, Hermitezitaet auf Zufalls-k.
  - Kein 4D-Spektrum und keine 4D-Form im Rauchlauf.
- **Hauptlauf** `regge4d.py haupt` (n = 3, n = 4, L = 3), dann `regge4d_auswertung.py`. Je Lauf deutlich unter
  10 min erwartet.
- **Abbruch:**
  - Flachheit nach zwei ernsthaften Versuchen verfehlt: "nicht gerechnet".
  - Code-Aenderungen nach dem Einfrieren nur bei echten Fehlern, offengelegt.

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren)

- Abschnitte 1 bis 10 sind nach den Rauchlaeufen unveraendert, Schwellen eingeschlossen.
- **rauch1** (.69 23:18:42 bis 23:18:52 UTC, Spur cpu3, rc = 0; Code-sha256 d20a892e...): n = 3 vollstaendig, n = 4
  nur Geometrie. Gesehen bei n = 4:
  - Flach: max abs(eps) 1,8e-15; skaliert (l x 1,3) 1,8e-15; zufaellig affin verzerrt 3,6e-15.
  - Simplizes je Dreieck 4 bis 6, je Kante 12 bis 24. Flache Diederwinkel nur pi/4, pi/3, pi/2.
  - Schlaefli je Simplex 8,4e-13, global bei k = 0 3,6e-11.
  - Richardson-Fehlerschaetzung 7,5e-12; Weg T gegen Weg J 1,9e-12.
  - Betroffene Dreiecke je Kantentyp 47 bis 89, alle in [-1, 1]^4.
  - dA/ds der Hyperdiagonale ist in allen 14 Dreiecken exakt 0,0. Das ist der Mechanismus von A1; das Spektrum
    selbst ist nicht gerechnet.
  - Hermitezitaet auf 64 Zufalls-k 3,5e-12; Imaginaerteil 1,7e-12.
  - Damit sind die Teile G0 (a) und G0 (b, Zufalls-k) schon vor dem Einfrieren sichtbar erfuellt.
- **rauch1, n = 3 (Kontrolle, nicht geurteilt):**
  - Bei k = 0 genau 6 Nullmoden.
  - Bei kleinem k: 3 Nullmoden, 2 positive und 1 negative Kontinuumsmode, 1 Gittermode (3,5, Kww = 0,5 konstant).
  - c2 = 0,24995 und c0s/c2 = -0,99999 bis -0,99986 bei abs(k) = 0,05.
  - Schur gegen direkt 9e-5 bei 0,05, wachsend wie k^2.
- **Fehler gefunden:** Die Auswertung suchte die Betraege als berechnete Normen (0,05000000000000002). Behoben mit
  "betrag_nominal". Ausserdem rechnet der Rauchmodus jetzt die n = 3-Kurven, damit der Bildcode geprueft wird.
- **rauch2** (23:20:47 bis 23:20:58 UTC, cpu3, rc = 0) und Probe der Auswertung auf den 3D-Daten (23:21:03 bis
  23:21:08 UTC, rc = 0):
  - Mit den d = 3-Entsprechungen der Regeln (6 bzw. 3 Nullmoden, 2+/1-, Ziel -1) ergeben sich vier mal
    "eingetroffen"; r weicht hoechstens 0,22 % ab, die Spin-2-Streuung bei 0,2 betraegt 0,29 %.
  - Das ist nur eine Probe des Codes, kein Urteil zur Karte. Die Bilder wurden erzeugt.
- **Kein 4D-Spektrum und keine 4D-Form gerechnet oder gesehen.**
