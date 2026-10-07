# REGEL-1: Plan (Code-Agent, Runde 36, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 01:33:05 CEST; Plantext ab 02:01:49 CEST (date).
  Zeitbox 120 min, also bis 03:33 CEST.
- **Grundlage:** KARTE.md (RG0 bis RG3; Vorhersagen, Wahrscheinlichkeiten und Schwellen unveraendert uebernommen),
  REGEL.md (Abschnitte 2, 4, 7), TENSOR-EIS-N und LAMBDA-1 (PLAN, ERGEBNIS, code/).
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier nur ueber die Vorgaengerkarten);
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher;
  - [H] Hypothese;
  - [M] Mathematik, vorab ableitbar;
  - [E] hier gerechnet (nur Rauchlaeufe, Abschnitt 9);
  - [F] eigene Festlegung, wo die Karte offen ist.
- Alles sind synthetische Gitterrechnungen, keine Messdaten. Einheiten: J = g = 1, Quellkopplung kappa = 1.

## 1. Modell bei c = 1/2 (mit Belegstellen)

- **Gitter und Felder:** Gu/Wen-N-Typ auf dem kubischen Gitter, symmetrische a_ij und E^ij, gestaffelt; Ableitungen
  naechster Nachbarn, Symbol i K_a mit K_a = 2 sin(q_a/2); Frobenius-Orthonormalbasis.
  - Belegt: TENSOR-EIS-N PLAN 1.1 bis 2; Kontrolle K3 dort: Code-Matrizen gleich Gu/Wens k-Raum-Matrix S. 19 auf
    1,3e-15 bzw. 4,3e-14 [S + E].
- **Energie mit eingebauter Regel:** H = (J/2) [E^ij E^ij - (1/2)(E^ii)^2] + (g/2) a_ij R^ij (Gu/Wen Gl. 32), also
  c = 1/2 exakt, **ohne Strafterme** (U_v = U_s = 0, Satz P0).
  - Code: hesse(o, 'N', lam = 0,5), unveraendert aus lam.py (LAMBDA-1 PLAN Abschnitt 1: c ist genau `lam`).
- **Zwangsbedingungen:** d_i E^ij = 0 (Gl. 13, Operator Kv) und R^ii = rho (Gl. 21/31, Zeile c); Eichungen Gl. 15
  (G15) und Gl. 23 (G23).
- **Warum die Regel hier "eingebaut" ist [M, LAMBDA-1]:**
  - Die kinetische Energie ist bei c = 1/2 auf ker Kv invariant unter Gl. 23 (REGEL.md Abschnitt 2).
  - LAMBDA-1 hat gemessen: Invarianzdefekt der Zwangsflaeche unter der Bewegung 8,4e-16 bei c = 1/2, sonst ~ |1 - 2c|
    (ERGEBNIS Tabelle 3.3).
  - Z = ker c x ker Kv ist nur bei c = 1/2 invariant (Dirac-Dimension 8 statt 7, LAMBDA-1 ERGEBNIS 1.4).
- **Statik:** statischer stationaerer Wert unter exakten Bedingungen (TENSOR-EIS-N F2), Kern kappa(q) je q aus dem
  7x7-KKT (kern_statik, unveraendert).
  - Belegt: kappa = -g/(2 K^2), U = -m1 m2/(8 pi r) fern (TENSOR-EIS-N ERGEBNIS 1).
  - Belegt: unabhaengig von c (LAMBDA-1 ERGEBNIS 1.5).
- **Code:** code/regel.py ist lam.py (eingefroren 20261004-004847, sha256 65dac72d...), Zeilen 31 bis 1219 woertlich,
  ohne dessen main(), dazu der neue Abschnitt REGEL-1. code/regel_auswertung.py ist neu.

## 2. Materie: Q-Baelle von M1 in 3D [F]

- **M1:** L = |phi_t|^2 - |grad phi|^2 - U(|phi|^2), U(S) = S - S^2 + S^3/2 (beta = 1/2), phi = f(r) exp(-i omega t).
  - Energiedichte rho_E = omega^2 f^2 + f'^2 + U(f^2); Ladungsmass |phi|^2 = f^2 mit int f^2 = Q/(2 omega).
- **Kein vorhandener Code liefert 3D-Profile fuer diese Zwecke:** kegel_q.py und licht.py (RUNDE-26, RUNDE-34) sind 2D.
  - Daher eigener Radialloeser Radial3: wie kegel_q.Radial, mit Gewicht r^2 (FV-Gitter, Newton bei festem omega^2,
    Fortsetzung in omega^2, Q per brentq auf dem VK-stabilen Ast).
  - Geprueft gegen die bekannte 3D-Tabelle RUNDE-02/tests1d (Test 4, Q und E bei omega^2 = 0,55 bis 0,90;
    Q_min = 111,84 bei omega^2 = 0,927).
- **Q-Werte [F, Abweichung von der Karte]:** Die Karte nennt Q = 50 und 500 (Zahlen aus 2D).
  - In 3D gibt es Q = 50 nicht: Q_min = 111,84 (RUNDE-02/tests1d; Rauchlauf r1: 111,888 bei omega^2 = 0,925, dem Ende
    meines Gitters).
  - Gerechnet wird daher:
    - klein: Q = 150 (kleinste runde Ladung mit E < Q, also absolut stabil; E = Q liegt bei Q ~ 141);
    - gross: Q = 500 (wie Karte);
    - schwer (dritte Quelle): Q = 5000.
  - Werte aus Rauchlauf r1 (dr = 0,005, vor dem Einfrieren gesehen, Abschnitt 9):

    | Ball | Q | omega^2 | E | E/Q | N/E = int f^2 / E | R_half | R_half/h |
    |---|---|---|---|---|---|---|---|
    | k | 150 | 0,83483 | 149,291 | 0,99528 | 0,54983 | 2,069 | 4,14 |
    | g | 500 | 0,69562 | 450,851 | 0,90170 | 0,66485 | 3,598 | 7,20 |
    | s | 5000 | 0,58166 | 3965,74 | 0,79315 | 0,82657 | 8,834 | 17,67 |

- **Ballradius [F]:** R_half = Radius mit |phi|^2(R_half) = |phi|^2(0)/2 (Halbwertsradius wie KEGEL-Q).
  - "Ballradius" in RG2 und RG3: R = R_half(Q = 500)/h in Gitterabstaenden, also R = 7,196.
- **Gitterweite [F]:** h = 0,5 Laengeneinheiten von M1 je Gitterabstand.
  - **Mindestaufloesung [F]:** R_half(Q = 150)/h >= 4 und |Gittersumme/Radialintegral - 1| <= 1e-4 fuer E und int f^2
    aller drei Baelle; sonst sind RG2 und RG3 "nicht auswertbar".
  - Rauchlauf r1: 4,14; Gittersummen bei h = 0,5 auf <= 5e-8, bei h = 1 auf <= 8e-6.
- **Abtastung [F]:** rho(h |x|) h^3 an den Gitterknoten x, Ball auf einem Knoten zentriert.
  - Kugelschnitt bei r_cut = 40 (also |x| <= 80); Anteil jenseits r_cut <= 4e-14.
  - f und f' aus einem kubischen Spline der Radialloesung (f'(0) = 0 per Spiegelung).
- **Quelle:** R^ii(x) = kappa rho(x) mit rho = rho_E (Energiekopplung) oder rho = |phi|^2 (Ladungskopplung, AEQ-0),
  kappa = 1. Die Quellstaerke ist die Gittersumme S = Sum_x rho(x) (E_gitter bzw. N_gitter).

## 3. Schreibtisch vorab [M]

- **Teil 1:**
  - Auf Z bleiben je q != 0 genau zwei laufende Moden (Helizitaet 2) mit omega^2 = g J K^2 (Gl. 35), entartet.
  - Die dritte Richtung der E-Seite ist die Eichrichtung G23 (omega^2 = 0); auf der a-Seite sind es die drei
    Eichrichtungen G15.
  - Bei |k| = 0,1: v = omega/|k| = sqrt(Sum 4 sin^2(k n_a/2))/|k|, zwischen 0,999583 ([100]) und 0,999861 ([111]).
    Die Streuung ist 2,8e-4.
  - omega^2/k^2 = 1 - (k^2/12) Sum n_a^4 + O(k^4); der k^2-Koeffizient liegt zwischen -1/12 und -1/36.
  - Invarianzdefekt 0 bis auf Rundung. Kein exponentielles Wachstum auf Z, nur Eichdrift E_T -> a_L (Jordankette 2).
- **Teil 2:** U(d) = Sum_x,y rho1(x) G(x - y + d) rho2(y) mit G -> -1/(8 pi r).
  - Fuer kugelsymmetrische, getrennte Baelle gilt im Kontinuum der Schalensatz exakt, also U d/(E1 E2) = -1/(8 pi).
  - Auf dem Gitter bleiben die kubische Anisotropie der Greenfunktion (~ 0,26/r^2: 3e-4 bei d = 4 R, TENSOR-EIS-N 3.1)
    und die Ueberlappung der Schwaenze (~ exp(-2 sqrt(1 - omega^2) Luecke), < 1e-3 bei d = 4 R).
  - Erwartung: Streuung ~ 5e-4, also RG2 eingetroffen.
- **Teil 3:**
  - Energiekopplung: a_i = F_i/E_i = -grad(G_eff E_s/d), unabhaengig vom Ball (Schalensatz). Erwartet eta_E ~ 1e-6 oder
    kleiner.
  - Ladungskopplung: a_i ~ N_i/E_i (Quelle und Antwort ueber |phi|^2, Traegheit = Energie).
    eta_Q = 2 |r_k - r_g|/(r_k + r_g) mit r = N/E, also 0,1894 (Werte r1).
  - RG3 also eingetroffen.
- **Folge:** RG0 bis RG3 sind vorab ableitbar (wie bei TENSOR-EIS-N und LAMBDA-1). Scheitern koennen nur Rekonstruktion,
  Quellankopplung, Torus-Korrektur und Numerik. L1 (kann scheitern) ist damit schwach.

## 4. Messvorschriften

### 4.1 Teil 1, Wellen (Modus wellen)

- **Gitter:** BZ mit L = 32, alle 32 767 q != 0 (wie LAMBDA-1 F7).
- **Bewegung auf Z:**
  - Z_a = ker c (5-dim.) und Z_E = ker Kv (3-dim.), Orthonormalbasen per SVD (physraeume).
  - M1 = Z_a^T A Z_E, M2 = Z_E^T B Z_a; omega^2 = eig(M2 M1) (3x3).
  - **Laufend:** Re omega^2 > TAU_LAUF s mit s = |M1|_2 |M2|_2, TAU_LAUF = 1e-6 [F].
  - **Null:** |omega^2| <= TAU_LAUF s. Klassifikation: Anteil des Null-Eigenvektors (in R^6) an G23 und Rest |M2 Z_a^T G15|.
  - **Wachstum:** -Re omega^2 > TAU s oder |Im omega^2| > TAU s, TAU = 1e-6 (wie TENSOR-EIS-N, LAMBDA-1).
- **Gegenproben auf Z:** zwang_scan (Projektion, Invarianzdefekt der Bewegung) und dirac_scan (groesster invarianter
  Unterraum), beide unveraendert aus lam.py, bei c = 1/2, P0.
- **Invarianzdefekt unter Gl. 23 [F: die Karte nennt ein Mass, ich messe drei, RG0 nimmt das groesste]:**
  1. Energie, Fourier: max_q |Z_E^T A G23| / (|A| |G23|) (linearer Term), dazu der quadratische Term
     |G23.A.G23| / (|A| |G23|^2); BZ L = 32 und alle Richtungsproben.
  2. Bewegung (Mass von LAMBDA-1): |(1 - P_Z) D P_Z| / |D|, max ueber q.
  3. Ortsraum L = 6 (Stencils): |Z^T M_J G23_ort| / (|M_J| |G23_ort|) mit Z = Kern der Ortsraum-Divergenz.
  - Dazu beschreibend: c = 0,45 und 0,55 (Kontrast), TT-Identitaet Z_E^T (A - P_TT) Z_E.
- **Dispersion [F]:**
  - Richtungen: 100 Fibonacci-Richtungen auf der Kugel plus [100], [110], [111], also 103 (>= 50).
  - Je Richtung n und |k| in {0,025; 0,05; 0,1; 0,2}: q = |k| n, die zwei laufenden omega^2.
  - Je Richtung und Mode Ausgleich omega^2/k^2 = v0^2 + b k^2 (kleinste Quadrate ueber die vier |k|).
  - v(n) := omega(|k| = 0,1)/0,1.
- **Bild:** omega(|q|) laengs [100], [110], [111] bis pi.

### 4.2 Teil 2, Newton (Modus statik)

- **Kern:** kappa(q) je q per 7x7-KKT auf dem rfft-Gitter; Vergleich mit -g/(2 K^2) (Kontrolle). q = 0: kappa = 0
  (neutralisierender Hintergrund, TENSOR-EIS-N F3).
- **Quellspektren:** rfftn der eingebetteten Baelle (Realteil; Imaginaerteil als Kontrolle, Kugelsymmetrie).
- **Wechselwirkung:** U_L(s) = irfftn(kappa rho_a,q rho_b,q)(s) = Sum rho_a(x) G_L(x - y) rho_b(y - s) fuer alle s
  zugleich.
  - Das ist genau E(Paar) - E(a) - E(b) der statischen Loesung mit beiden Quellen (das Problem ist je q entkoppelt).
  - Gegenprobe im Ortsraum: Kontrolle K3.
- **Linien:** s = n e mit e = (1,0,0), (1,1,0), (1,1,1), d = n |e|.
- **Torus-Korrektur [F, Ewald wie LAST-1 3.2 im Geist]:**
  - U_inf(s) = U_L(s) + (g/2) S_a S_b [W_L(s) + (m2_a + m2_b)/(6 L^3)].
  - W_L(s) = G_per,L(s) - 1/(4 pi s): neutralisierte periodische Kontinuums-Greenfunktion minus freier Kern, per Ewald
    (alpha = 8/L, Realraum |n_i| <= 2, k-Raum |m_i| <= 16).
  - m2 = zweites Moment der abgetasteten Dichte (Gittereinheiten).
  - **Begruendung [M]:**
    - G_L,Gitter - G_inf,Gitter = Bildsumme. Die Gitterkorrektur der Bilder ist O(1/L^3) und glatt, ~ 1e-6 relativ.
    - Der Kontinuumsteil W erfuellt Laplace W = 1/L^3. Fuer kugelsymmetrische Dichten gibt die Mittelwerteigenschaft
      genau W(s) + <r^2>/(6 L^3).
    - Probe vorab an TENSOR-EIS-N: U_L64(2,0,0) = -0,019682 plus (1/2) W_64 = -0,0017627 ergibt -0,0214447 gegen
      U_korr = -0,0214447 (Schreibtisch).
- **Groessenreihe:** L = 192, 224, 256; Hauptwert L = 256 [F].
  - Die 3-Punkt-Anpassung von TENSOR-EIS-N taugt hier nicht (d/L bis 0,38; Fehler ~ (d/L)^5), sie wird nicht benutzt.
- **Messgroesse:** y(d) = U_inf(d) d / (S_a S_b) fuer das Paar (Q = 150, Q = 500), Energiekopplung.
  - Alle Linienpunkte mit 4 R <= d <= 10 R auf den drei Linien, R = 7,196 [F].
  - Beschreibend: Paare (500, 500), (150, 150) und Ladungskopplung.

### 4.3 Teil 3, Fallen (Modus statik, dieselben Laeufe)

- **Anordnung:** Schwere Quelle s (Q = 5000) im Ursprung, Testball k bzw. g einzeln bei s = n* e.
  - n* = round(8 R/|e|), also d = 58 ([100]), 57,98 ([110]), 57,16 ([111]).
  - Lineare Theorie, daher getrennt; die Selbstkraft eines symmetrischen Balls ist null.
- **Kraft [F]:** F_i = -[U_inf((n* + 1) e) - U_inf((n* - 1) e)] / (2 |e|).
  - Das ist gleich dem mit rho_i gefalteten zentralen Gitter-Gradienten des Feldes von s (Abschnitt 4.2, Identitaet
    der Faltung).
- **Beschleunigung:**
  - Energiekopplung: a_i = F_i/E_i mit E_i = E_gitter (Quelle rho_E fuer s und i).
  - Ladungskopplung: Quelle und Antwort ueber |phi|^2, a_i = F_i/E_i mit derselben Traegheit E_i (Energie).
- **Eotvos-Groesse:** eta = 2 |a_k - a_g| / (a_k + a_g) je Linie und Kopplung.
- **Beschreibend:** eta(d) laengs [100] fuer 4 R <= d <= 10 R; eta bei L = 192 und 224; eta ohne Torus-Korrektur.

## 5. Kontrollen (Modus kontrolle und radial; Tore in Abschnitt 6)

- **K1, Radialloeser:**
  - Q und E gegen RUNDE-02/tests1d (sechs omega^2, Toleranz 1e-3 beschreibend);
  - dr = 0,01 gegen 0,005;
  - Virial G + 3 V - 3 omega^2 I;
  - dE/dQ = omega am Ball.
- **K2, Aufloesung:** Gittersummen bei h = 1; 0,75; 0,5; 0,25 (exakt per Vielfachheiten r_3(n)); Tor nach Abschnitt 2.
- **K3, Statik im Ortsraum (L = 6, Stencils, KKT per pinv):**
  - zwei unsymmetrische Quellen gegen ifftn(kappa rho1 conj rho2);
  - zwei symmetrische Kugelquellen gegen genau den Hauptpfad (rfftn, Realteil, irfftn, Linien).
- **K4, voller 16x16-KKT** (E- und a-Teil, c = 1/2, Kv E = 0) gegen den 7x7-Kern an 3000 Zufalls-q.
- **K5, Ortsraum-Invarianz** (Mass 3 in 4.1), dazu div G23 = 0 und c = G23^T im Ortsraum.
- **K6, Zeitentwicklung im Ortsraum** (L = 8, Leapfrog dt = 0,05, Anfangsdaten auf Z per Projektion) [beschreibend]:
  - c = 1/2 bis T = 200: Zwangsresiduen, Energie, |R| = |inc a| (eichinvariant), |E|;
  - Kontrast c = 0,45 bis T = 20.
- **K7, Torus:**
  - Ewald unabhaengig von alpha (8/L gegen 6/L);
  - Punktquellen korrigiert gegen TENSOR-EIS-N U_korr (r = 2 bis 16);
  - Groessenreihe (Tor in Abschnitt 6).
- **K8, Kern:** kappa gegen -g/(2 K^2), Zwangsresiduen; Imaginaerteil der Quellspektren.

## 6. Urteilsregeln (mechanisch in code/regel_auswertung.py)

- **Tore [F]:**
  - Aufloesung: R_half(150)/h >= 4 und alle |Gittersumme/Radial - 1| <= 1e-4. Verfehlt: RG2 und RG3 "nicht
    auswertbar".
  - Torus: max |y_L/y_256 - 1| <= 1e-3 fuer L = 192 und 224 an allen RG2-Punkten (Paar k-g, Energie). Verfehlt: RG2
    "nicht auswertbar".
- **RG0** (Karte: Invarianzdefekt unter Gl. 23 bei c = 1/2 < 1e-12; kein Wachstum auf der Zwangsflaeche).
  **Eingetroffen** genau dann, wenn beide Bedingungen gelten:
  1. Das groesste der Masse aus 4.1 (Energie linear und quadratisch auf BZ und Richtungen, Bewegung, Ortsraum L = 6)
     ist < 1e-12.
  2. Kein q mit Wachstum: Projektion, Dirac und Modenzerlegung auf der BZ L = 32 sowie alle Richtungsproben.
  - Sonst nicht eingetroffen.
- **RG1** (Karte: je k genau 2 laufende Moden mit omega^2 = v^2 k^2 (1 + O(k^2)); v ueber 50 Richtungen bei
  |k| = 0,1 innerhalb 1 % gleich). **Eingetroffen** genau dann, wenn (a), (b) und (c) gelten:
  - (a) An jedem q der BZ L = 32 und an jeder Richtungsprobe genau 2 laufende Moden.
  - (b) [F] Je Richtung und Mode: v0^2 > 0,01 und max ueber die vier |k| von |omega^2/(v0^2 k^2) - 1| / k^2 <= 1
    ("1 + O(k^2)" mit Koeffizient hoechstens 1).
  - (c) Ueber alle 103 Richtungen und beide Moden: (max v - min v)/Mittel v <= 0,01 bei |k| = 0,1.
  - Sonst nicht eingetroffen.
- **RG2** (Karte: U d/(E1 E2) konstant innerhalb 1 % fuer d >= 4 Ballradien, nach Torus-Korrektur).
  **Eingetroffen** genau dann, wenn beide Bedingungen gelten:
  1. [F: "Newton" heisst anziehend] U_inf < 0 an allen RG2-Punkten.
  2. (max y - min y)/|Median y| <= 0,01 ueber alle Linienpunkte mit 4 R <= d <= 10 R auf [100], [110], [111].
  - Paar Q = 150 mit Q = 500, Energiekopplung, L = 256 Ewald-korrigiert.
  - [F] Die Karte nennt nur "d >= 4"; die Obergrenze 10 R steht in Teil 2 der Karte.
  - Sonst nicht eingetroffen; Torverfehlung: nicht auswertbar.
- **RG3** (Karte: Energiekopplung eta < 1e-3 bei d = 8 Ballradien des grossen Balls; Ladungskopplung eta > 5e-2).
  **Eingetroffen** genau dann, wenn alle drei Bedingungen gelten:
  1. Alle a > 0 (Fallen zur schweren Quelle hin), beide Baelle, beide Kopplungen, drei Linien.
  2. eta_E < 1e-3 auf allen drei Linien.
  3. eta_Q > 5e-2 auf allen drei Linien.
  - L = 256 Ewald-korrigiert. Sonst nicht eingetroffen; Aufloesungstor verfehlt: nicht auswertbar.
- Bilder: lauf-69/bild-dispersion.png, bild-newton.png, bild-eta.png.

## 7. Agenten-Vorhersagen (vorab, mit Zahl; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| A1 | RG0: alle Defektmasse <= 1e-14; Kontrast c = 0,45/0,55: 0,1 = abs(1 - 2c) (Energie, Fourier und Ortsraum) |
| A2 | RG1: v(0,1) zwischen 0,99958 und 0,99987, Streuung 2,8e-4 +- 0,2e-4; v0^2 = 1 auf 1e-4; k^2-Koeffizient zwischen -0,084 und -0,027 |
| A3 | RG2: y 8 pi zwischen -1,002 und -0,998, Streuung <= 2e-3; Paare (500, 500) und (150, 150) ebenso; Ladungskopplung: y = -1/(8 pi) mit N statt E ebenso |
| A4 | RG3: eta_E <= 1e-5 auf allen Linien; eta_Q = 0,189 +- 0,002 auf allen Linien |
| A5 | Torus: Groessenreihe y_L/y_256 - 1 <= 1e-5; Punktquellen gegen TENSOR-EIS-N <= 3e-4 (deren Anpassungsunsicherheit) |
| A6 | K3: Ortsraum gegen Fourier <= 1e-12; K4 <= 1e-12; K6: Zwangsresiduen bei c = 1/2 <= 1e-9, Energie beschraenkt (Leapfrog-Schwankung <= 1 %), \|R\| beschraenkt; bei c = 0,45 waechst \|R\| um Faktoren > 1e3 |

## 8. Laeufe auf der .69 (kleintest.sh, Spuren cpu3 und cpu4, hoechstens zwei zugleich)

| Lauf | Spur | Aufruf (im Ordner runde36-regel) | erwartet |
|---|---|---|---|
| S1 | cpu3 | code/regel.py statik --L 192 --L 224 --out lauf/statik-192-224.json | ~ 200 s |
| S2 | cpu4 | code/regel.py statik --L 256 --out lauf/statik-256.json | ~ 190 s |
| RA | cpu4 | code/regel.py radial --dr 0.01 --out lauf/radial.json | ~ 10 s |
| WE | cpu3 | code/regel.py wellen --L 32 --nfib 100 --out lauf/wellen.json | ~ 60 s |
| KO | cpu4 | code/regel.py kontrolle --Lort 6 --Lzeit 8 --out lauf/kontrolle.json | ~ 60 s |
| AW | cpu3 | code/regel_auswertung.py --lauf lauf --out lauf/auswertung.json | ~ 10 s |

- Standardwerte im Code: h = 0,5, Q = 150,500,5000, r_cut = 40, dr = 0,005, rmax = 60, chunk = 2, hliste
  1,0/0,75/0,5/0,25.
- Vor AW: TENSOR-EIS-N lauf/auswertung.json (auf der .69 in runde36-tensorn/lauf/) als lauf/tensor-eis-n-auswertung.json
  daneben (nur Kontrolle K7).
- Zeiten aus den Rauchlaeufen: Kern L = 96 in 8,4 s, L = 128 in 19,6 s, also ~ 18 bis 19 Mikrosekunden je q.

## 9. Rauchlaeufe (vor dem Einfrieren; offengelegt)

Alle auf der .69 ueber kleintest.sh, Zeiten UTC. Code regel.py sha256 5929f0e3... seit dem ersten Hochladen vor r1
unveraendert; regel_auswertung.py einmal hochgeladen vor r7 (mit der Option --Lhaupt fuer den Rauchtest), danach
unveraendert.

| Lauf | Spur | Zeit | Inhalt | gesehen |
|---|---|---|---|---|
| r1 | cpu3 | 23:56:46 bis 23:56:48 | radial, dr 0,01/0,005, h 1,0/0,5 | alles (Werte in Abschnitt 2) |
| r2 | cpu3 | 23:57:14 bis 23:57:15 | wellen, L = 8, 10 Fibonacci-Richtungen | Kennzahlen, siehe unten |
| r3 | cpu4 | 23:57:16 bis 23:57:19 | kontrolle, Lort 4 | Abbruch: Kugelkasten 5 > L = 4 |
| r4 | cpu4 | 23:57:26 bis 23:57:42 | kontrolle, Lort 6, Lzeit 4 | Kennzahlen, siehe unten |
| r5 | cpu3 | 23:58:15 bis 23:58:26 | statik L = 96, 128, r_cut 30 | Abbruch: Ball (121) > L = 96; Kernzeit L = 96 |
| r6 | cpu3 | 00:00:11 bis 00:00:34 | statik L = 128, r_cut 30 | nur Laufzeit |
| r7 | cpu4 | 00:01:02 bis 00:01:05 | Auswertung auf r1/r2/r4/r6 mit --Lhaupt 128 | rc = 0; Urteilszeile nicht gelesen; Bilder nicht geoeffnet; per jq nur die Kontrollen unten |

- **Gesehen in r2 (L = 8)** [E]: Diese Groessen gehen in RG0/RG1 ein; sie sind vorab ableitbar (Abschnitt 3).
  - Invarianzdefekt Energie 2,1e-16, quadratisch 1,8e-16, TT-Identitaet 8e-16, Bewegung 4,2e-16;
  - Kontrast c = 0,45/0,55: 0,1;
  - an allen 511 q genau 2 laufende Moden und eine Null, Null-Mode zu 100 % G23, a-Rest 3,5e-16;
  - kein Wachstum, Dirac-Dimension 8;
  - Richtungsproben (10 Richtungen) je 2 laufende Moden; erste Zeile omega^2 = K^2.
- **Gesehen in r4 (L = 6, Lzeit 4)** [E]:
  - Ortsraum-Invarianz 3,6e-16 (0,1 bei c = 0,45/0,55); div G23 = 0; c = G23^T auf 6e-17;
  - Statik Ortsraum gegen Fourier 1,4e-15 (unsymmetrisch) und 3,3e-15 (symmetrisch, Hauptpfad);
  - voller KKT 1,0e-15;
  - Zeit (L = 4), c = 1/2: Zwangsresiduen bis 2,9e-10 (Anstieg aus 4e-14, Rundung), Energie 0,29 %, |R| <= 0,98,
    |a| linear bis 60 (Eichdrift); c = 0,45: Wachstum (|R| bis 6e6).
- **Gesehen in r7 per jq (L = 128):**
  - Punktquellen Ewald-korrigiert gegen TENSOR-EIS-N 3,9e-5;
  - Kern gegen Formel 4,2e-15;
  - Imaginaerteil 1,3e-16; Ewald-alpha 2e-18; Aufloesungstor bestanden.
- **Folge:** Nach den Rauchlaeufen wurde weder Code noch Schwelle noch Urteilsregel geaendert. r3 und r5 waren
  Bedienfehler (L kleiner als der Kugelkasten), keine Codefehler.
