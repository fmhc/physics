# INDUZIERT-DIRAC-2D: Plan (Code-Agent, Runde 39)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 09:48:32 CEST (date). Code ab 10:05:55 CEST, Plantext
  ab 10:20:30 CEST (date). Zeitbox 150 min, also bis 12:18 CEST.
- **Vor diesem Plantext gerechnet** (Abschnitt 11): Kontrollen (dichte Pruefungen, Paritaet, Spektren), das feste
  regelmaessige Netz L = 63 und Zeitlaeufe mit Rauchsaaten >= 902. Den Wert der Kartenkontrolle "regelmaessiges Netz"
  habe ich damit vor dem Einfrieren gesehen (L = 63, Abschnitt 11). c_eff-Werte auf Zufallsnetzen habe ich vor dem
  Einfrieren nicht angesehen.
- **Grundlage:** KARTE.md (ID-F0 bis ID-F3 mit Schwellen unveraendert); INDUZIERT-DICHTE-2D und -GROB (eingefrorener
  Code 20261004-091915, PLAN, ERGEBNIS, GEGENLESEN); SPIN-KAUSAL-L (DOSSIER); SPIN-ZUFALLSNETZ-1 (KARTE); RUNDE-22
  geometrie-stand (Kaehler-Dirac auf zufaelliger Geometrie, Catterall/Laiho/Unmuth-Yockey 2018 [L?]).
- **Kennzeichen:** [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen
  (hier keine Quelle abgerufen), [F] Festlegung dieses Plans (von der Karte offen gelassen), [K] Kartenpunkt,
  [H] Hypothese, [E] hier gerechnet.

## 1. Code

- code/dichte2d_grob.py, zufall2d.py, induziert.py, grob_auswertung.py: unveraendert aus -GROB (eingefroren
  20261004-091915; sha256 152de683..., 37a0fe8f..., b3867eac..., caa58ab2..., gleich den dortigen Pruefsummen).
- **code/dirac2d.py (neu):** Netz, Abbildung psi, Neuvernetzung, Laengen (geo) und Skalar werden aus dichte2d_grob.py
  bzw. zufall2d.py aufgerufen, nicht kopiert. Neu sind die Operatoren (A) und (B), die Modi dichte, regulaer und
  kontrolle.
- **code/dirac_auswertung.py (neu):** Tor, Urteile, Ausgleich (Funktionen aus grob_auswertung.py), Bilder,
  Selbsttest.

## 2. Vorzeichenkonvention [M, F]

- **Skalar:** Gamma_B = +1/2 log det' K, wie -GROB. Polyakov fuer c = 1: Gamma_B'' = P k^2 A mit P = -1/(24 pi).
- **Fermion (Grassmann):** Z = det D, also Gamma_F = -log|det' D_F| = -1/2 log det'(D^T D).
  - Fuer ein Dirac-Fermion gilt [M, L]: Die konforme Variation von log det(D_g^2) ist entgegengesetzt gleich der von
    log det' Delta_0. Heat-Kernel: a_1(D^2) = -R/(24 pi) gegen a_1(Delta_0) = +R/(24 pi).
  - Also Gamma_F'' = +P k^2 A, dieselbe Steifigkeit wie der Skalar (c = 1, Bosonisierung).
- **Festlegung:** c_eff = (Gamma''/(k^2 A))/P mit Gamma = Gamma_F (Fermion) bzw. Gamma_B (Skalar).
  - Ein einzelnes Dirac-Fermion gibt +1, der Skalar +1. Naive Doppler (4 Dirac-Fermionen) gaeben +4.
  - Ohne Grassmann-Vorzeichen (+log|det|) waeren alle Fermion-Werte umgekehrt. Beschreibend mitberichtet ist nur
    das Vorzeichen; geurteilt wird in der Fermion-Konvention.

## 3. Operatoren

### 3.1 (A) naiver Dirac-Operator mit eingesetztem Rahmen

- **Form:** D_ij = (1/2) w_ij l_ij (gamma . n_ij) fuer jede Kante ij, D_ji = -D_ij, D_ii = 0.
  - w_ij: Kotangens-Gewicht aus den physikalischen Laengen, wie beim Skalar. l_ij: physikalische Laenge (geo).
  - n_ij: Richtung der Kante in Koordinaten (Sehne).
  - gamma_1 = sigma_x, gamma_2 = sigma_z (reell, hermitesch, antivertauschend). D ist damit reell antisymmetrisch
    (2N x 2N); die Karte schreibt (i/2) w (sigma . n), also H = i D. |det| ist gleich.
- **Gewicht [M, F]:** (1/2) w_ij l_ij ist die halbe Laenge der Voronoi-Kante (w = l*/l).
  - Begruendung (Gauss ueber die Dualzelle): Integral ueber V_i von gamma . grad psi = Summe_j l*_ij gamma . n_ij
    (psi_i + psi_j)/2. Der psi_i-Anteil faellt weg, weil Summe_j l*_ij n_ij = 0 (geschlossene Zelle).
  - Fuer lineares psi gilt Summe_j w_ij d_ij (x) d_ij = 2 V_i 1 im Mittel; die Summe ueber alle Knoten ist exakt
    (Kotangens-Identitaet je Dreieck: Summe cot theta_e e e^T = 2 A_T 1). Je Knoten schwankt der spurfreie Teil
    ("zufaelliges Vierbein").
  - Die Karte sagt "Gewichte w_ij aus Delaunay bzw. Voronoi wie beim Skalar". Das ist hier w_ij^Karte = l*_ij.
- **Rahmen und Spin-Zusammenhang [M]:**
  - Eingesetzt ist der konforme Rahmen e_a = e^(-sigma) d_a. In ihm hat die Sehne dieselbe Richtung wie in
    Koordinaten.
  - Mit l_ij ~ e^(sigma(m_ij)) l0_ij gilt Summe_j D_ij psi_j = V_i^phys D_g psi + O(eps^2). Dabei ist
    D_g = e^(-sigma) (gamma . d + 1/2 gamma . d sigma) der kovariante Dirac-Operator. Der Spin-Zusammenhang entsteht
    aus der Laengenskalierung.
  - Die Drehung des Rahmens gegen den Paralleltransport kuerzt sich bei symmetrischem Transport exakt:
    e^(i a sigma_z) gamma_a e^(i a sigma_z) = gamma_a. Ein U_ij ist deshalb nicht noetig.
  - Konstruktion aus inneren Daten (Laengen) plus Sehnenrichtung: kovariant bis auf das Koordinaten-Delaunay
    (wie beim Skalar).
- **Nullmoden [M, E]:**
  - Mit zeta = a + i b je Knoten wirkt D antilinear: zeta -> (i/2) conj(G zeta) mit G_ij = w_ij d_ij (komplexer
    Kantenvektor). G ist komplex antisymmetrisch (N x N).
  - Bei geradem N erzwingt das neben den konstanten Spinoren eine zweite exakte Nullmode. Bei ungeradem N gibt es
    genau eine komplexe Nullmode, und sie ist fuer jedes s geschuetzt. Das passt zum Kontinuum: D_g e^(-sigma/2) u = 0
    fuer jedes sigma.
  - Rauchlauf (K1b): N = 150 und 152 haben 4 Nullmoden von D, N = 151 und 153 haben 2. Regelmaessig L = 8: 8, L = 9: 2.
  - Bei N = 16 000 und s = 0,5 liegen die Nullmoden dagegen als Kramers-Quartett bei 1e-5 bis 1e-4, mitten im
    tiefen Spektrum (Rauchlauf r902). Das waere keine saubere Abtrennung.
  - **Festlegung [F, K3]:** N = 16 001 (ungerade), regelmaessige Netze mit ungeradem L.
- **log|det' D| exakt [M]:** D_(0) ist D ohne die zwei Zeilen und Spalten von Knoten 0.
  - Die Nullvektoren v_k mit v_k(Knoten 0) = e_k (k = 1, 2) folgen aus D_(0) x_k = -D[Rest, k] (gleiche LU).
  - Jacobi (D normal): |det' D| = |det D_(0)| det(V^T V). Bei s = 0 ist das log|det D_(0)| + 2 log N.
  - Pruefung: K1 gegen dichte Eigenwerte (N = 151, s = 0 und +-0,5): <= 6e-13 absolut. Kramers-Struktur der
    Gram-Matrix (g11 = g22, g12 = 0) und Nullvektor-Residuum werden je Netz geprueft (Tor).
  - LU: scipy splu, COLAMD, Pivotsuche (Diagonale ist null). log|det| = Summe log|U_ii| (math.fsum).

### 3.2 (B) Kaehler-Dirac (DEC)

- **Form:** d + delta auf Omega^0 + Omega^1 + Omega^2 des Delaunay-Netzes. d0 und d1 sind kombinatorisch, delta ist
  *^-1 d^T * mit Hodge-Sternen aus physikalischen Laengen:
  - *0 = m_i = Summe_j w_ij l_ij^2/4 (zirkumzentrische Dualflaeche)
  - *1 = w_e (Kotangens-Gewicht = l*/l)
  - *2 = 1/A_T
- **Exakte Zerlegung [M, E]:** (d + delta)^2 = Delta_0 + Delta_1 + Delta_2, und det'Delta_1 = det'Delta_0 det'Delta_2
  (Hodge-Zerlegung; gilt auch diskret, ohne Positivitaet).
  - Also |det'(d + delta)| = det'Delta_0 |det'Delta_2|.
  - Delta_0 = *0^-1 K: log det'Delta_0 = log det K_(0) + log Summe m - Summe log m = 2 Gamma_B - log N + log Summe m
    - Summe log m.
  - Delta_2 = K_2 *2 mit K_2 = Laplace des Dualgraphen (Dreiecke, Leitwert 1/w_e je Kante):
    log det'Delta_2 = log|det K_2,(0)| + log Summe A_T - Summe log A_T.
  - Nullmoden: genau die harmonischen Formen (1 + 2 + 1 = 4 auf dem Torus). Sie fallen durch die Erdung von K und K_2
    exakt heraus.
  - Pruefung: K1 gegen dichte Eigenwerte von d + delta (6N x 6N, N = 151): <= 1,1e-11. (d + delta)^2 blockdiagonal auf
    1e-13, d1 d0 = 0.
- **Gamma_KD = -log|det'(d + delta)| = Gamma_KD0 + Gamma_KD2** mit Gamma_KD0 = -log det'Delta_0 und
  Gamma_KD2 = -log|det'Delta_2|. Beide Teile werden einzeln mitberichtet.
- **Heikel:** K_2 hat Leitwerte 1/w_e. Beim Koordinaten-Delaunay mit physikalischen Laengen sind 0,005 bis etwa 1 % der
  w_e negativ (Rauchlaeufe: 2 bis 456 Kanten je Netz); kleine abs(w_e) geben grosse Leitwerte. K_2 kann dann indefinit
  sein; gerechnet wird log|det| mit Pivotsuche. Tor: abs(w_e) > 1e-12 und m_i > 0.

### 3.3 Skalar

- Gamma_B = zufall2d.Netz.gamma(l), unveraendert: Kotangens-Steifigkeit, LU mit SymmetricMode, U_ii > 0 geprueft.
  Gerechnet auf denselben Netzen und Laengen wie (A) und (B).

## 4. Geometrie, Ensemble, Messgroesse (wie -GROB)

- Torus, sigma = s cos(k.x), Punkte nach physikalischer Flaeche (psi), Neuvernetzung je Verformung (Delaunay in
  Koordinaten, koord), physikalische Laengen (geo), S = 0,5, Richtungen 0 und 90 Grad.
- D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2 je Operator, y = D/A, A = L^2.
- **Datensaetze [F, K3]:**
  - E1: N = 16 001, A = N (eps = 1), n = 1, 2, 4, 6, also k eps = 0,050 / 0,099 / 0,199 / 0,298. Saaten 0 bis 71.
  - E2: N = 16 001, A = 4 N = 64 004 (eps = 2), n = 2, 4, 8, 12, also k eps = 0,099 / 0,199 / 0,397 / 0,596.
    Saaten 1000 bis 1071.
  - Nach der Skalengleichheit aus -GROB [K1 dort] ist E2 rechnerisch E1 bei doppeltem k eps. Deshalb bekommen beide
    getrennte Saaten.
- **Ausgleich (wie -GROB):** y_eps = y A/N, x = (k eps)^2, y_eps = a + c x + d x^2 gemeinsam ueber E1 und E2.
  - GLS auf den 8 Zellmitteln mit freier Kovarianz je Datensatz (4 x 4, ddof 1), Birge-Faktor, Modellprobe
    chi^2 bei 5 FG.
  - c_eff = c/P, SE(c_eff) = SE_U(c)/abs(P).
  - Getrennt fuer B, A, KD, KD0, KD2. Dazu je Saat gepaart: A - B, KD + 4B, A mit Massenmatrix
    (Gamma_A + 2 Summe log m), lokale Glieder Summe log m und Summe log A_T (erwartet c = 0).

## 5. Regelmaessiges Netz (Kartenkontrolle ID-F0)

- Quadrate mit (1,1)-Diagonale, L = 127 (ungerade: die Doppler haben verdrehte Randbedingungen und keine Nullmoden).
  Diagonalen haben bei s = 0 das Gewicht 0; (A) ist dann exakt der naive Gitteroperator mit 4 Dopplern.
  - Kontrolle K2 (Rauchlauf): Spektrum = sqrt(sin^2 p_x + sin^2 p_y) auf 1e-14.
- **Festes Netz:** Die konforme Mode wirkt nur ueber die physikalischen Laengen (geo), wie die Variante "feste
  Punkte". Auf einem regelmaessigen Netz gibt es keine Punkte nach Flaeche (Kartenpunkt [K2]).
- c(k) = Gamma''(0)/(k^2 A) per Richardson mit h = 0,01 (wie INDUZIERT-ZUFALL-2D), n = 1, 2, 4, 0 und 90 Grad
  gemittelt.
- **Urteilswert [F]:** c0_eff aus c(k) = c0 + b k^2 (kleinste Quadrate ueber n = 1, 2, 4), c0_eff = c0/P. Gleiches
  fuer den Skalar.
- Beschreibend: S-Schema (S = 0,5) und L = 63 (Rauchlauf).

## 6. Vorhersagen der Karte (unveraendert)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ID-F0 | Kontrolle: Regelmaessiges Netz mit (A) gibt c_eff = 4 +- 1 (Doppler); Skalar auf den Zufallsnetzen c_eff = 1 +- 0,2 | 75 % |
| ID-F1 | [H] Zufallsnetz mit (A): c_eff = 1 +- 0,4, also keine Doppler in der Anomalie | 35 % |
| ID-F2 | Zufallsnetz mit (B) Kaehler-Dirac: c_eff = 2 +- 0,5 | 55 % |
| ID-F3 | [H] Vorzeichen der induzierten konformen Steifigkeit wie beim Skalar (Polyakov-Vorzeichen) fuer beide Bauweisen | 60 % |

## 7. Urteilsregeln (mechanisch durch code/dirac_auswertung.py nach lauf-69/auswertung.json)

- **Tor [F]:**
  - Netz (alle Operatoren): jedes Netz erfuellt die eingefrorenen Pruefungen aus -GROB (Euler, E = 3N, F = 2N, jede
    Kante in genau zwei Dreiecken, Orientierung > 0, Koordinatenflaeche = L^2, physikalische Flaechen > 0, laengste
    Kante < L/4, Grundnetz Delaunay, Skalar-LU mit U_ii > 0 und perm_r = perm_c, Newton-Residuum <= 1e-12).
  - Tor A: log|det'| endlich, det(Gram) > 0, Nullvektor-Residuum <= 1e-8 (relativ), Gram komplex strukturiert
    (abs(g11 - g22) + abs(g12) <= 1e-6 g11).
  - Tor KD: m_i > 0, abs(w_e) > 1e-12, A_T > 0, log|det'| endlich.
  - Faellt Tor Netz, sind alle Zufallsnetz-Teile nicht auswertbar; faellt Tor A bzw. KD, die Teile mit A bzw. KD.
- **Vorbedingungen je Ausgleich:** mindestens 16 Saaten je Datensatz; Modellprobe p >= 0,01 (sonst "nicht
  auswertbar": das Modell der Karte traegt dann nicht).
- **Bandregel (wie -GROB) [F]:** fuer ein Band [lo, hi] in c_eff:
  - eingetroffen: c_eff im Band und SE <= halbe Bandbreite
  - nicht eingetroffen: Abstand zum Band > 2 SE
  - sonst nicht auswertbar
  - Kartenwortlaut (Punktwert im Band) wird mitberichtet.
- **ID-F0:**
  - Teil (i), regelmaessig (A): c0_eff (L = 127) in [3; 5] -> eingetroffen, sonst nicht eingetroffen
    (deterministisch, kein Rauschen).
  - Teil (ii), Skalar auf den Zufallsnetzen: Bandregel mit [0,8; 1,2].
  - Beide eingetroffen -> eingetroffen; einer nicht eingetroffen -> nicht eingetroffen; sonst nicht auswertbar.
- **ID-F1:** Bandregel fuer c_eff(A) mit [0,6; 1,4].
- **ID-F2 (Kartenwortlaut):** Bandregel fuer c_eff(KD) mit [1,5; 2,5].
  - **Mitberichtet [K1], kein Kartenurteil:** dieselbe Regel mit der berichtigten Erwartung [-5; -3] (also -4 +- 1).
- **ID-F3 [F: 2-SE-Regel]:** Polyakov-Vorzeichen heisst c_eff > 0 (Fermion-Konvention, Abschnitt 2).
  - Eingetroffen: c_eff(A) - 2 SE > 0 und c_eff(KD) - 2 SE > 0.
  - Nicht eingetroffen: fuer eine Bauweise (mit erfuellten Vorbedingungen) c_eff + 2 SE < 0.
  - Sonst nicht auswertbar. Kartenwortlaut (Punktwerte beide > 0) wird mitberichtet.
- **Bedeutung:** wie auf der Karte vorab festgelegt (ID-F1 trifft ein / ID-F1 verfehlt).

## 8. Beschreibend (kein Urteil)

- je Operator: Ausgleich nur E1 bzw. nur E2, mit k^6, eigenes a je Datensatz, Fenster k eps <= 0,40, nur k^2 im
  Fenster, Jackknife-SE
- c_eff(k) = (y - a)/(x P) je Zelle mit SE; Saatstreuung, Versatz- und Restanteil
- KD0 und KD2 einzeln; gepaart A - B und KD + 4 B; A mit Massenmatrix; lokale Glieder Summe log m, Summe log A_T
- Tor-Kennzahlen: Nullvektor-Residuum, Gram-Abweichung, Anteil negativer w_e, neue Kanten
- regelmaessiges Netz: c(k) je n fuer A und Skalar, S-Schema, L = 63
- Spektrum (Kontrolle K3): tiefste Eigenwerte von D auf Zufallsnetzen gegen das Kontinuum eines Dirac-Fermions
- Bild lauf-69/bild-ck-gegen-k2.png: c_eff(k) gegen (k eps)^2 je Bauweise (Skalar, A, KD) und Netzabstand, mit
  Ausgleichsgerade und Linien c = 1, 2, 4 (bei KD auch -2 und -4); viertes Feld: regelmaessiges Netz

## 9. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Kaehler-Dirac gibt im gekruemmten Raum nicht c = 2, sondern c = -4 [M]:**
  - Exakt gilt |det'(d + delta)| = det'Delta_0 det'Delta_2 (Abschnitt 3.2). Im Kontinuum sind Delta_2 und Delta_0 ueber
    den Hodge-Stern isospektral, fuer jede Metrik.
  - Also Gamma_KD = -2 log det'Delta_0 = -4 Gamma_B, und damit c_eff = -4 (Fermion-Konvention; Dirac = +1).
  - Grund: Die Aequivalenz "Kaehler-Dirac = 2 Dirac-Fermionen" gilt nur im flachen Raum. Kaehler-Dirac-Felder sind
    Formen (ganzzahliger Spin) und koppeln anders an die Kruemmung als Spinoren. Der Geschmacksindex dreht sich mit.
  - Gegenprobe [L?]: Ein Paar Grassmann-Skalare mit Laplace-Wirkung ("symplektische Fermionen") hat Z = det'Delta_0
    und c = -2. Z_KD = (det'Delta_0)^2 entspricht zwei solchen Paaren, also c = -4. Das passt zu den topologisch
    verdrehten Fermionen eines N = 2-Modells (bc-Systeme mit Gewichten 1 und 0, je c = -2).
  - Die Heat-Kernel-Summe Summe_p a_1(Delta_p) = -R/(12 pi) (das waere "2 Dirac") ist keine konforme Variation,
    weil Delta_1 nicht kovariant skaliert. Die Spektralidentitaet ist dagegen exakt.
  - **Folge:** Nach Kartenwortlaut (2 +- 0,5) erwarte ich "nicht eingetroffen". Mitberichtet wird die berichtigte
    Regel mit -4 +- 1. Ein Urteil "eingetroffen" fuer -4 waere kein Kartenurteil.
  - Auch ID-F3 erwarte ich deshalb nicht eingetroffen (KD mit umgekehrtem Vorzeichen).
- **[K2] Regelmaessiges Netz:**
  - Ein festes Netz ist kein kovarianter Regulator. Schon der Skalar gibt dort c_eff = -9,4 statt 1 (c_P = 1/8,
    INDUZIERT-1 und -ZUFALL-2D).
  - Die Doppler-Zahl 4 ist deshalb in c_eff nicht isoliert: c_eff(regelmaessig, A) = 4 + nicht-universeller Anteil.
  - Rauchlauf L = 63 (Abschnitt 11): c_eff(A) = +39,6 / +38,1 / +37,5 bei n = 1, 2, 4; Skalar -9,41 / -9,36 / -9,17.
    Teil (i) von ID-F0 wird also nach Kartenwortlaut nicht eintreffen; geurteilt wird trotzdem mit L = 127.
  - Den Doppler-Zaehler leistet hier das Spektrum: K2 zeigt die 4 Kegel exakt (L gerade: 8 Nullmoden).
  - Eine kovariante Fassung des regelmaessigen Netzes gibt es nicht: psi staucht nur laengs k, ein Quadratnetz wuerde
    anisotrop.
- **[K3] N = 16 001 statt 16 000:**
  - Bei geradem N erzwingt die Antisymmetrie eine zweite Nullmode (Abschnitt 3.1). Bei ungeradem N ist det'
    eindeutig und exakt.
  - Folge: Die Netze sind neu (die Saat haengt an N). Ein Bitvergleich des Skalars mit -GROB ist nicht moeglich. Der
    Skalar wird auf denselben Netzen wie die Fermionen gerechnet (Kartenwortlaut "auf denselben Netzen").
- **[K4] Halber Spin und "Doppler" auf dem Zufallsnetz:**
  - Rauchlauf K3 (N = 4 001 und 16 001, s = 0): Die tiefsten Eigenwerte von (A) liegen beim 0,001- bis 0,025-Fachen
    des Kontinuumswerts eines Dirac-Fermions.
  - Das ist eine dichte Zustandsdichte bei E = 0 (Unordnungsband, Kramers-Quartette), kein einzelner Kegel.
  - Die Doppler des Quadratnetzes verschwinden also nicht spurlos. Sie werden zu einem Band bei null (wie SZ3 der
    3D-Karte).
  - Ob dieses Band zur k^2-Antwort beitraegt, ist die Messfrage von ID-F1. Kein Kartenfehler; es aendert aber die
    Lesart von "keine Doppler".
- **[K5] Rauschregeln** fehlen auf der Karte. Festgelegt wie -GROB (Abschnitt 7). Kartenwortlaut wird mitberichtet.
- **[K6] "Vorzeichen wie beim Skalar"** gilt in der Fermion-Konvention (Abschnitt 2), also mit Grassmann-Vorzeichen.
  Mit +log|det| waere es umgekehrt; die Karte legt das nicht fest.

## 10. Agenten-Vorhersagen

Notiert 10:18:20 CEST (date), vor dem Lesen der Rauchlaeufe regulaer-L63 und vor jedem c_eff-Wert auf Zufallsnetzen
(Datei AGENT-VORHERSAGEN-ENTWURF.txt). C6 und C7 waren damit vor dem Rauchlauf L = 63 festgelegt.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| C1 | Tor (Netz, A, KD) besteht in allen Hauptlaeufen | 90 % |
| C2 | Skalar auf den Zufallsnetzen: Punktwert c_eff(B) in [0,8; 1,2] | 75 % |
| C3 | (B) Kaehler-Dirac: c_eff(KD) in [-5; -3] (Kontinuum [M]: -4) | 55 % |
| C4 | Teil KD0 = -2 c_eff(B) innerhalb 2 SE (KD0 = -2 Gamma_B + lokal) | 85 % |
| C5 | (A) naiv auf dem Zufallsnetz: c_eff(A) ausserhalb [0,6; 1,4] (Unordnungsband bei E = 0) | 60 % |
| C6 | regelmaessiges festes Netz, (A): c0_eff ausserhalb [3; 5] | 70 % |
| C7 | regelmaessiges festes Netz, Skalar (geo-Laengen): c0_eff innerhalb 10 % von -9,42 | 80 % |

## 11. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC; Rauchsaaten >= 902)

- **kontrolle** (08:09:36 bis 08:09:57, cpu, rc 0; erste Codefassung, sha256 94306efb..., in rauch-69/dirac2d.py.rauch1):
  - KD-Zerlegung gegen dicht <= 2,3e-12 bei N = 150.
  - (A) bei s = 0 um 3,11 daneben: N = 150 hat 4 Nullmoden statt 2. Bei s = +-0,5 erschien ein Kramers-Quartett.
    Daraus entstand die Paritaetsanalyse (Abschnitt 3.1).
- **dichte-r902** (08:09:38 bis 08:10:40, cpu7, rc 0, erste Fassung): N = 16 000, Saat 902. Erste Fassung mit
  Eigenwert-Abzug (ARPACK): Nullmoden-Quartett bei 1e-5 bis 1e-4, naechste Eigenwerte 1,2e-4 bis 3,4e-4, also nicht
  getrennt. Laufzeit 55 s je Saat. Angesehen habe ich nur Eigenwerte und Zeiten, keine y-Werte.
- **Berichtigung vor dem Einfrieren:** exakte Nullvektor-Formel, N ungerade. Codefassung 3503cd1a... (= Einfrierfassung,
  sofern nicht unten anders vermerkt).
- **kontrolle2** (08:16:24 bis 08:16:36, cpu, rc 0):
  - K1 (N = 151): KD gegen dicht <= 1,1e-11; (A) gegen dicht <= 6e-13 bei s = 0 und +-0,5. Die zwei Nullmoden bleiben
    bei s = +-0,5 exakt null (1e-16), wie [M] verlangt.
  - K1b: Paritaet bestaetigt (4 / 2 / 4 / 2 Nullmoden bei N = 150 / 151 / 152 / 153).
  - K2: regelmaessig L = 8 und 9, Spektrum auf 1e-14, 8 bzw. 2 Nullmoden.
  - K3: tiefstes Spektrum von (A) auf Zufallsnetzen beim 0,001- bis 0,025-Fachen des Kontinuums (Abschnitt 9, K4).
- **dichte-r903** (08:16:26 bis 08:17:44, cpu7, rc 0): N = 16 001, Saaten 903 und 904. 38,6 bis 39,0 s je Saat
  (Dirac-LU 1,2 bis 2,2 s je Netz, KD 0,2 bis 0,3 s, Skalar 0,12 s). Nullvektor-Residuum <= 1,3e-14, Gram-Abweichung
  <= 4,6e-6 absolut (relativ etwa 1e-10). y-Werte nicht angesehen.
- **Versuch mit Ordnung MMD_AT_PLUS_A** (08:17:40, cpu7 und cpu): kein Fortschritt nach 70 s (Diagonale null). Beide
  Einheiten habe ich um 08:18:57 selbst gestoppt (systemctl --user stop, nur meine Einheiten); zurueck auf COLAMD.
- **regulaer-L63** (08:19:20 bis 08:19:33, cpu, rc 0): siehe [K2]. Richardson-Abweichung <= 3e-7, S-Schema gleich
  Richardson auf 0,1 %. Die Nullvektor-Formel ist also glatt in s.
- **dichte-r905-e1 / -e2** (08:19:39 bis 08:22:39, cpu und cpu7, rc 0): Rauchsaaten 905 bis 907 (E1) und 905 bis 909
  (E2, A = 64 004), nur fuer die Probe der Auswertung. 36,9 bis 39 s je Saat.
- **Selbsttest** (08:22:26 bis 08:22:29, cpu, rc 0): synthetisch, 64 + 64 Saaten, Rauschen wie der Skalar in -GROB,
  wahres c = P, d = +0,02, 400 Wiederholungen. Mittel c = -0,013270 (P = -0,013263), Zug-Std 1,08 / 1,10 / 1,10,
  Fehlalarm der Modellprobe 0,5 %. Die GLS-SE ist bei 64 Saaten je Satz also etwa 10 % zu klein (geschaetzte
  Kovarianz); das Jackknife wird mitberichtet. Erwartete SE(c_eff) fuer den Skalar: 0,14.
- **Probe der Auswertung** (rauch/probe: Kopien der Rauchdateien; 08:22:51 rc 1, 08:23:03 bis 08:23:09 rc 0):
  - Erster Versuch: KeyError (Rest der ersten Fassung im Teil "regelmaessig"); berichtigt.
  - Zweiter Versuch: Codepfad, Tor und Bild laufen; Urteile "nicht auswertbar" (5 Saaten). Angesehen habe ich nur
    Struktur und Tor-Kennzahlen (Tor bestanden, Nullvektor-Residuum <= 1,3e-14, negative w_e bis 1,04 % der Kanten bei
    k eps = 0,6), keine c_eff-Werte und nicht das Bild.

## 12. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde39-induziert-dirac/ (code/, rauch/, lauf/), nur ueber kleintest.sh,
  Spuren cpu und cpu7, je ssh-Aufruf ein Start, hoechstens zwei zugleich.
- **Laufzeit (gemessen):** 39 s je Saat (17 Netze). Bloecke zu 12 Saaten: etwa 470 s, unter 600 s.
- **cpu:** E1 in sechs Bloecken zu 12 Saaten (0 bis 71): e1-s0, e1-s12, e1-s24, e1-s36, e1-s48, e1-s60.
- **cpu7:** regulaer L = 127 (n = 1, 2, 4), dann E2 in sechs Bloecken zu 12 Saaten (1000 bis 1071): e2-s1000 bis e2-s1060.
- **Zusatzbloecke [F]:** e1-s72, e1-s84 und e2-s1072, e2-s1084 (also bis 96 Saaten je Datensatz) nur, wenn sie nach der
  Uhr bis 11:40 CEST fertig werden. Die Entscheidung haengt nur an der Uhrzeit, nicht an Werten; angesehen wird vorher
  nichts ausser Logkoepfen und Tor-Kennzahlen.
- Der naechste Block einer Spur darf gestartet werden, waehrend der vorige laeuft; er wartet am Lock der Spur.
- **Abbruch:** Fehlen Bloecke (Zeitbox, Abbruch nach 600 s), wird mit den fertigen Saaten geurteilt (offengelegt).
  Unter 16 Saaten je Datensatz sind die Zufallsnetz-Teile nicht auswertbar.
- **Danach:** dirac_auswertung.py auswerten lauf lauf/auswertung.json.
