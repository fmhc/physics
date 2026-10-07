# REGGE-4D-SCHIEF-1: Plan (Code-Agent, Runde 37)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 04:01:00 CEST (date). Plantext ab 04:22:44 CEST (date).
- Grundlage: KARTE.md. Die Vorhersagen SC0 bis SC3 und ihre Schwellen sind unveraendert uebernommen. Was die Karte
  offen laesst, ist als [F] festgelegt.
- Kennzeichen: [S] an der Quelle gelesen (hier nur ueber REGGE-4D-1), [L] Literatur aus dem Gedaechtnis, [L?] unsicher,
  [M] eigene Mathematik, [F] Festlegung dieses Plans, [H] Hypothese, [E] gerechnet.
- **Vor diesem Plan gesehen** (offengelegt): Rauchlauf 0 (.69, 02:19:06 bis 02:19:09 UTC, Spur cpu, rc = 0). Nur die
  Geometrie von A fuer s = 0; 0,1; 0,2: Matrix B, det, Kondition, Simplexvolumina, Winkelbereiche und die 14 Dreiecke an
  der Hyperdiagonale. Keine Flachheit, keine Ableitungen, keine Spektren, keine Form, keine Loesung.
- Code: code/regge_schief.py (neu), code/regge_schief_auswertung.py (neu); code/regge4d.py und code/regge_zeit.py
  unveraendert aus REGGE-ZEIT-1 (sha256 2708f33b... und 889d9b38..., gleich den eingefrorenen Fassungen).

## 1. Netz und A [M, F1]

- Kuhn-Gitter wie REGGE-4D-1: 15 Kanten, 50 Dreiecke, 24 Simplizes je Ecke; Torus L = 4 fuer Weg T. Ecken X -> A X.
- **A = diag(1, A_raum), A_raum = 1 + s B** [F1]. B = default_rng(20261004).uniform(-1, 1, (3, 3)), Zeilen (x, y, z):
  - (-0,90193; -0,18728; 0,24592)
  - (0,86593; -0,82550; 0,90120)
  - (-0,48817; 0,91276; 0,95662)
  - Nicht symmetrisch, allgemein. Summe der Nebendiagonale von B + B^T: 2 x 2,2504.
- Kantenlaengenquadrate s_e = abs(A e)^2 = e^T G e mit G = A^T A. Das Netz ist ein linearer Bild des Kuhn-Gitters, also
  flach und periodisch; Fourier wie in REGGE-4D-1 mit Gitterimpuls k_lat.
- **Gesehen in Rauchlauf 0 [E]:**

| s | det A | Kondition A_raum | Singulaerwerte | Simplexvolumen (alle 24 Typen) | Diederwinkel | Dreieckswinkel |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1, 1, 1 | 1/24 = 0,041667 | 45 bis 90 Grad | 30 bis 90 Grad |
| 0,1 | 0,91022 | 1,32 | 1,134; 0,936; 0,858 | 0,037926 (= det A/24) | 35,5 bis 100,5 Grad | 26,0 bis 100,6 Grad |
| 0,2 | 0,80220 | 1,76 | 1,268; 0,877; 0,721 | 0,033425 (= det A/24) | 27,5 bis 111,4 Grad | 22,0 bis 112,0 Grad |

  - A ist gut konditioniert; alle Simplizes haben dasselbe positive Volumen det(A)/24 (lineares Bild), das
    Mindestvolumen ist also 0,033425 bei s = 0,2.
- **Rechte Winkel an der Hyperdiagonale [M, E] (Pruefauftrag der Karte "verschwinden allgemein [M, zu pruefen]"):**
  - Dreiecke (0, a, 1111), a = 14 echte Teilmengen. Winkel an a: cos = -(A a).(A b)/(abs(A a) abs(A b)), b = 1111 - a.
  - Bei s = 0 alle 14 recht (Thales). Bei s = 0,1 und 0,2 bleiben **2 von 14 recht**: a = 1000 und a = 0111. Grund [M]:
    A laesst die Zeitachse senkrecht zum Raum, also (A e_tau).(A b) = 0 fuer raeumliches b.
  - Die anderen 12 werden stumpf: 90,9 bis 98,6 Grad (s = 0,1), 91,3 bis 107,9 Grad (s = 0,2).
  - dA/ds_top = (s_a + s_b - s_top)/(16 A) ist an diesen 12 Dreiecken ungleich 0 (alle negativ; s = 0,2: -0,0057 bis
    -0,081). Die Hyperdiagonale ist damit keine tote Variable mehr.
  - **Berichtigung der Karte:** "Die rechten Winkel verschwinden allgemein" gilt fuer 12 von 14 Dreiecken. Fuer die
    Folgerung (keine tote Variable) reicht das. Keine Vorhersage haengt davon ab.
- **Erste Ordnung in s [M, Schaetzung]:** Bei s = 0 ist d eps/d s_top bei k = 0 nur an den 6 Flaeche-Flaeche-Dreiecken
  (0, a, 1111) mit zwei Einsen in a ungleich 0 (Betrag 1, alle gleich nach der S4-Symmetrie; REGGE-ZEIT-1, Rauchlauf 0).
  Also M_top,top = sum dA/ds_top x d eps/d s_top = O(s): Summe der sechs dA/ds_top = -0,111 (s = 0,1) bzw. -0,218
  (s = 0,2). Die Hyperdiagonal-Mode sollte bei k = 0 einen Eigenwert linear in s bekommen.

## 2. Variablen, Vorzeichen, Fourier (wie REGGE-4D-1)

- Variablen s_e = l_e^2. H = -M, M = Hesse-Matrix von S = sum A_t eps_t; M(k) = A(k)^+ E(k), Mittelpunktskonvention,
  Weg T (Torus L = 4, Richardson h = 1e-3) fuer d eps/d s. Gegenproben: Weg J (lokal) und komplexer Schritt (Weg K).
- Die Inversion X -> -X vertauscht mit A, bleibt also Symmetrie; M(k) reell, gerade in k [M]. Die Permutationen der
  Achsen sind gebrochen.
- **Physikalische Koordinaten:** x = A X. Ebene Welle exp(i k_lat.X) = exp(i k_phys.x) mit **k_phys = A^-T k_lat**,
  also k_lat = A^T k_phys.
- **Metrikstoerung physikalisch:** delta s_d = (A d)^T h (A d) = d^T (A^T h A) d. Abbildung B_phys (15 x 10) in der
  Frobenius-orthonormalen Basis symmetrischer 4 x 4-Matrizen (wie REGGE-4D-1 [F5]).
- **Gitter-Eichmoden:** Eckenverschiebung xi (physikalisch) exp(i k.X): u_d = 4 i sin(k_lat.d/2) (A d).xi [M].
  Exakte Nullvektoren fuer jedes k. Kontinuum: h = k_phys xi + xi k_phys.
- **Normierung [M]:** Die Form je Ecke ist det(A) mal die Form je physikalischem Volumen (Zellvolumen det A). Ich teile
  durch det(A). Erwartung (Karte, [L] Cheeger/Mueller/Schrader): K/det(A) -> (1/4) k_phys^2 (P2 - 2 P0s). Die Karte
  schreibt die Form ohne det(A); das ist die Form je Volumen. SC2 haengt nur von Verhaeltnissen ab, also nicht davon.

## 3. Nullmoden: Schwelle und Punkte [F2, F3]

- **[F2] Nullmode:** abs(lambda) < 1e-6 x Mittel(abs(lambda)), Mittel ueber alle 15 Eigenwerte von H(k) am selben
  Punkt (Karte SC1: "1e-6 mal Mittel").
  - **Begruendung:** Rauschen exakter Nullmoden in REGGE-4D-1 bis 3,9e-13 x Lambda, mit Lambda/Mittel ~ 8 also
    ~3e-12 x Mittel. Kleinster physikalischer Eigenwert bei abs(k) = 0,05 (s = 0): 8,6e-6 x Lambda ~ 7e-5 x Mittel.
    Die Schwelle liegt 5,5 Groessenordnungen ueber dem Rauschen und 1,8 unter dem kleinsten k^2-Eigenwert.
  - Berichtet werden je Punkt die acht kleinsten abs(lambda)/Mittel und der kleinste Nicht-Eich-Eigenwert (Spektrum von
    H auf dem Komplement der analytischen Eichmoden). So sieht man, ob eine Mode nur "fast" null ist.
- **[F3] "Allgemeines k":** 64 Gitterimpulse gleichverteilt in [-pi, pi]^4 (Saat 20261006) und alle 80 Leiterpunkte
  (Abschnitt 4), zusammen 144 Punkte. k = 0 getrennt. Beschreibend dazu die Brillouin-Zone 8^4 (Zaehlung
  null/positiv/negativ) und die Kurve kleinster Eigenwerte gegen s (s = 0; 0,025; 0,05; 0,1; 0,15; 0,2).

## 4. Lange-Wellen-Form in physikalischen Koordinaten [F4, F5, F6]

- **[F4] Richtungen** (physikalisch, 16): die 8 aus REGGE-4D-1 ((1,0,0,0) bis (1,2,3,4), normiert) und 8 Zufallsrichtungen
  (Normalverteilung, Saat 20261005, normiert). Betraege abs(k_phys) = 0,05; 0,075; 0,1; 0,2; 0,4. k_lat = A^T k_phys.
- **[F5] Schur-Komplement:** K = B^T H B - B^T H C (C^T H C)^+ C^T H B mit **C = [e_top, C4]** wie REGGE-4D-1 (C4:
  Orthonormalbasis des Komplements von range(B_phys ohne top-Zeile) in R^14). Pseudoinverse mit rcond 1e-8.
  - Bei s = 0 ist das genau REGGE-4D-1. Bei s != 0 wird die Hyperdiagonale als Gittermode ausintegriert.
  - [M] Der k^2-Koeffizient ist unabhaengig vom Komplement (direkte Form B^T H2 B). Das Komplement wirkt in
    O(k^4/lambda_C); ist die Hyperdiagonal-Mode leicht (kleines lambda_C), wird das bei abs(k) = 0,1 sichtbar.
  - Varianten (nur Bericht): C = orthogonales Komplement von range(B_phys) in R^15 ("orth") und direkte Form.
- **Projektoren** mit n = k_phys/abs(k_phys) und der Einheitsmetrik (physikalisch euklidisch), Formeln wie REGGE-4D-1:
  c2 = tr(P2 K)/(5 k^2), c0s = s^T K s/k^2 (s = theta/sqrt 3), Spin-2-Block = 5 Eigenwerte von Q2^T K Q2/k^2, alles mit
  K/det(A).
- **[F6] Lesart von SC2** (Karte: "fuenf Spin-2-Werte gleich auf 1 %, Verhaeltnis -2 +- 0,02, Richtungsstreuung
  <= 1 %"):
  - (a) je Punkt max abs(x_i/Mittel_5 - 1) <= 0,01 ueber die 5 Spin-2-Werte;
  - (b) je Punkt abs(c0s/c2 + 2) <= 0,02;
  - (c) je Betrag max ueber die 16 Richtungen von abs(c2/Mittel - 1) <= 0,01.
  - "abs(k_phys) = 0,05 bis 0,1" = die Betraege 0,05; 0,075; 0,1. Mitberichtet: Streuung aller 80 Spin-2-Werte (Art von
    REGGE-4D-1 G3), c2/(1/4), Mischungen, Abweichung von (1/4) k^2 (P2 - 2 P0s).

## 5. Ruhende Masse (Teil 2) [M, F7 bis F10]

- **Wie REGGE-ZEIT-1:** euklidisch, statisch (k_tau = 0), linear, G = M = 1. Weltlinie auf den Zeitkanten bei X = 0.
  Die Zeitkante hat weiter Laenge 1 (A laesst tau unveraendert), also Quelle M(k) u = 4 pi G M e_tau.
- **[F7] Nullraum und Festlegung:**
  - s = 0 (Kontrolle): analytischer Nullraum = 4 Eichmoden + e_top, Fixierung durch Projektion (kleinste Fehlwinkel je
    k) wie REGGE-ZEIT-1. Kalibrierung: 4 Gittermoden C4 versklavt, dann projiziert.
  - s = 0,2: Nullraum = nur die 4 Eichmoden sin(k.d/2)(A d); **keine Fixierung**; die Hyperdiagonale folgt aus der
    Gleichung. Kalibrierung: alle 5 Gittermoden C = [e_top, C4] versklavt (C^T M0 (ds_kin + C w) = 0), keine Projektion.
    [M] Das versklavte Ergebnis haengt nicht von der Wahl des Komplements ab, weil M0 range(B) = 0.
- **[F8] "Fehlwinkel ohne Festlegung eindeutig"** (SC3 Teil a): Auf L = 32 hat H(k) an allen statischen k != 0 genau 4
  Nullmoden (Schwelle [F2]), und die Eichmoden aendern die Fehlwinkel nicht: max norm(E G)/(norm(E) norm(G)) <= 1e-9.
- **Kalibrierung neu** (Dreiecke schief): konstante physikalische Kruemmung, h(x) = 1/2 Hd x x, umgerechnet auf
  Gitterkoordinaten Hd_lat = A^T (x) A^T (x) A^T (x) A^T Hd; Kantenaenderungen per Linienintegral (exakt fuer quadratisches h),
  Fehlwinkel ueber die Schablone von Weg T. Teile N (h_tautau = 2 Phi) und S (h_ij = -2 Phi delta_ij), 6
  Phi-Komponenten physikalisch. Kontrollen: Riemann-Normalkoordinaten gegen statisch, Ursprungsverschiebung.
- **[F9] Achse und Messung:**
  - Physikalische Achse = Gerade durch die Masse in Richtung A e_x (traegt Gitterpunkte X = (x0, 0, 0)), r = x0 abs(A e_x).
  - Zeit-Quadrate (tau, x) mit Zentren (x0 +- 1/2, 0, 0) gegen Quer-Quadrate (y, z) mit Zentren (x0, +-1/2, +-1/2), je
    physikalisch abgebildet. Vorhersagen P^N, P^S an den exakten physikalischen Zentren mit
    Phi_ij = -G M (3 x_i x_j - r^2 delta_ij)/r^5. 2x2-Loesung: gamma = beta/alpha, alpha = G_gemessen/G_Wirkung.
  - Beschreibend auch die Achsen A e_y und A e_z.
  - **Torus-Korrektur:** Bilder in einer physikalischen Kugel abs(A_raum n) <= 16 (Einheit L) und Hintergrund aus dem
    Mittel von F(k) ueber k_phys = +-kappa e_i (physikalische Raumachsen, kappa = 0,02 und 0,01, Richardson). [M] F(k)
    ist fuer k -> 0 eine quadratische Form in k_phys-Dach; das 6-Punkt-Mittel ist dann das Kugelmittel, passend zur
    Kugelform der Bildsumme. Ein Wuerfel in Gitterkoordinaten (REGGE-ZEIT-1) waere physikalisch ein Spat und braeuchte
    einen Formterm.
  - **gamma(r = 6):** lineare Interpolation in 1/r^2 zwischen den beiden Achsenpunkten, die r = 6 einschliessen.
    Mitberichtet: gamma am Gitterpunkt x0 = 6.
- **Groessen:** s = 0,2 auf L = 24, 32, 48; geurteilt auf L = 32 (Karte). s = 0 auf L = 32 (Kontrolle).
- **[F10] Kontrolle mit demselben Code:** s = 0, L = 32, x-Achse, x0 = 6 muss REGGE-ZEIT-1 (1,0872270) auf 0,002
  treffen, sonst SC3 nicht auswertbar.

## 6. Kartenwortlaut und Berichtigungen

- SC0 bis SC3 und ihre Schwellen gelten unveraendert. Berichtigungen (keine aendert eine Schwelle):
  1. Rechte Winkel: 12 von 14 verschwinden, 2 bleiben (Abschnitt 1).
  2. Normierung der Form: je physikalischem Volumen (Abschnitt 2).
- Fuer SC3 vergleicht die Karte mit 1,087 (REGGE-ZEIT-1). Geurteilt wird mit der festen Schwelle 0,044 der Karte;
  mitberichtet die Haelfte der Abweichung meiner s = 0-Kontrolle.

## 7. Urteilsregeln (mechanisch in code/regge_schief_auswertung.py)

- **SC0 eingetroffen**, wenn alle Teile gelten (Karte):
  - (a) max abs(eps) <= 1e-12 auf dem Torus L = 4 fuer s = 0; 0,1; 0,2;
  - (b) max ueber 64 Zufalls-k und 80 Leiterpunkte von max abs(M - M^+)/max abs(M) <= 1e-10, fuer alle drei s;
  - (c) s = 0: bei k = 0 genau 11 Nullmoden, an allen 144 allgemeinen Punkten genau 5 (Schwelle [F2]).
- **SC1 eingetroffen**, wenn fuer s = 0,1 und s = 0,2 gilt: bei k = 0 genau 10 Nullmoden und an allen 144 allgemeinen
  Punkten genau 4 (Schwelle [F2]; das ist "kleinster Nicht-Eich-Eigenwert > 1e-6 mal Mittel").
- **SC2 eingetroffen**, wenn bei s = 0,2 fuer alle 16 Richtungen und abs(k_phys) = 0,05; 0,075; 0,1 die Teile (a), (b),
  (c) aus [F6] gelten (Schur-Form mit C = [e_top, C4]).
- **SC3 eingetroffen**, wenn bei s = 0,2 auf L = 32 (a) [F8] gilt und (b) abs(gamma(r = 6) - 1) < 0,044 (Karte).
  Ist (a) verfehlt, lautet das Urteil "nicht eingetroffen".
- **Sperren "nicht auswertbar"** [F11]:
  - SC1 bis SC3: max abs(eps) > 1e-8 (Geometrie falsch) oder benoetigter Lauf fehlt.
  - SC1: Eichmoden (allgemeines k) oder affine Moden (k = 0) nicht im Nullraum: norm(H Q)/Lambda > 1e-6.
  - SC2: Im Schur-Komplement wird bei s = 0,2 ein Eigenwert von C^T H C verworfen (Komplement singulaer).
  - SC3, ausgewertet vor (a) und (b):
    - Kontrolle [F10] verfehlt;
    - Kondition des Versklavungssystems C^T M0 C > 1e8;
    - Imaginaerteil der Fehlwinkelfelder > 1e-8 oder Eichresiduum > 1e-6;
    - **zeilennormierte Kondition des 2x2-Systems > 10** an einem der beiden Stuetzpunkte von r = 6. Lehre aus
      REGGE-ZEIT-1: Dort lief Kondition 828 durch; 10 laesst bei Eingangsfehlern um 1e-3 hoechstens etwa 1 % Fehler in
      gamma zu (Achse REGGE-ZEIT-1: 1,5);
    - gamma(6) auf L = 48 weicht um mehr als 0,01 von L = 32 ab (Torus oder Resonanz nicht beherrscht).

## 8. Agenten-Vorhersagen (vor jeder Rechnung mit Spektrum, Form oder Quelle)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | SC0 eingetroffen: flach <= 1e-14, hermitesch <= 1e-11, s = 0 zaehlt 11 bzw. 5 | 90 % |
| A2 | Die Hyperdiagonal-Mode wird in erster Ordnung gehoben: Bei k = 0 ist der 11. kleinste abs(lambda) linear in s (Verhaeltnis s = 0,2 zu 0,1 zwischen 1,6 und 2,4) und liegt bei s = 0,2 zwischen 0,05 und 1 mal Mittel | 70 % |
| A3 | SC1 eingetroffen | 75 % |
| A4 | SC2 eingetroffen; die Schur-Korrektur der leichten Mode bleibt bei 0,1 unter 0,5 % | 60 % |
| A5 | SC3 (a) eindeutig erfuellt | 75 % |
| A6 | SC3 (b) erfuellt: abs(gamma(6) - 1) < 0,044. Begruendung fuer die niedrige Zahl: Der Newton-Teil der Abweichung (alpha - 1 ~ 1,6/r^2) haengt in REGGE-ZEIT-1 nicht an der Diagonale, und die Gitterdispersion O(a^2/r^2) bleibt im schiefen Netz | 25 % |
| A7 | Kontrolle s = 0 trifft REGGE-ZEIT-1 auf <= 1e-4 (Kugel- statt Wuerfelbilder) | 85 % |
| A8 | Codeproben: Drehung (A_raum orthogonal) gibt c2 und c0s/c2 wie s = 0 auf 1e-9 und dieselbe gamma-Reihe; Streckung diag(1,15; 0,9; 1,05) gibt bei 0,05 c2/(1/4) und c0s/c2/(-2) auf 0,1 % | 80 % |

## 9. Kontrollen (beschreibend)

- Flachheit (auch skaliert), Weg T gegen J und K, Schlaefli je Simplex und global, Gram-Winkel gegen winkel().
- Hermitezitaet, Imaginaerteil; affine Moden bei k = 0 und Eichmoden bei k != 0 im Kern; Nullraum ausserhalb.
- Schur gegen orth gegen direkt; Kontinuums-Eichmoden; Mischungen; Kww-Eigenwerte.
- Teil 2: Quelle auf dem Nullraum, Gleichungsresiduum, Nullraumresiduum, kleinster Nicht-Null-Eigenwert, Eichmoden und
  Fehlwinkel, Imaginaerteil; Kalibrierung RNC gegen statisch, Verschiebung, Versklavungsanteil, Kss-Eigenwerte;
  Hintergrund-Richardson; Groessenreihe L = 24/32/48; Achsen A e_y, A e_z; kinematische gamma (ohne Versklavung).
- Codeproben (nicht geurteilt): Drehung und Streckung in Teil 1, Drehung in Teil 2.

## 10. Laeufe

- **Ort:** .69, /home/fmh/fmhc-physics-remote/runde37-schief/ (code/, rauch/, lauf/); Start nur ueber kleintest.sh,
  Spuren cpu und cpu6, hoechstens zwei zugleich.
- **Rauchlauf 1** (vor dem Einfrieren): `teil1 r1.json 0 test` (s = 0 und die Codeproben, keine s != 0-Spektren);
  `teil2 r1-s0.json 0 16`; `teil2 r1-rot.json rot 16`; `teil2 r1-s02.json 0.2 8` (Codepfad ohne Fixierung, kein
  Punkt im Urteilsbereich). Probe der Auswertung auf diesen Dateien.
- **Hauptlaeufe:** `teil1 teil1.json 0,0.1,0.2 test kurve bz`; `teil2 teil2-s0.json 0 24,32`;
  `teil2 teil2-s02.json 0.2 24,32,48`; dann die Auswertung. Je Lauf unter 10 min erwartet.
- **Abbruch:** Teilrechnung nach zwei ernsthaften Versuchen nicht lauffaehig: "nicht gerechnet" mit Grund.
  Code-Aenderungen nach dem Einfrieren nur bei echten Fehlern, offengelegt.

## 11. Rauchlaeufe (Protokoll)

- Abschnitte 1 bis 10 standen vor Rauchlauf 1 und sind danach unveraendert, Schwellen und Vorhersagen eingeschlossen.
  Der Code ist seit Rauchlauf 0 unveraendert (regge_schief.py sha256 374806ed..., Auswertung e8d7c682...).
- Alle Laeufe .69, Spuren cpu/cpu6, rc = 0. Zeiten UTC aus den Logs.
- **Startfehler (meiner):** Der erste Sammelaufruf startete wegen falscher Klammerung nur r1; die Teil-2-Starts brachen
  vor dem Programmstart ab (Logpfad nicht gefunden). Danach einzeln gestartet.
- **r1** (teil1 s = 0 mit Codeproben, 02:24:34 bis 02:25:07 UTC). Gesehen:
  - s = 0 = REGGE-4D-1: flach 1,8e-15; hermitesch 3,3e-12; k = 0 11 Nullmoden (bis 6,8e-12 x Mittel, dann 2,14 x
    Mittel); an allen 144 allgemeinen Punkten 5. c2 = 0,24991 bis 0,24999 und c0s/c2 = -1,9999 bis -2,0004 bei 0,05 in
    den 8 alten Richtungen, wie REGGE-4D-1. Damit ist SC0 (a, b, c) fuer s = 0 sichtbar.
  - Drehung: Zeitrichtung (gleiche Gitterrichtung) c2 auf 5e-9 gleich s = 0. **Planfehler in A8:** Die anderen
    physikalischen Richtungen treffen im gedrehten Gitter andere Gitterrichtungen; dort ist "gleich s = 0" nicht
    erwartet (Unterschiede bis 3e-5). A8 bleibt im Wortlaut stehen und wird so beurteilt.
  - Streckung: k = 0 11, allgemein 5 Nullmoden (rechte Winkel bleiben); bei 0,05 c2/(1/4) >= 0,9996, c0s/c2 = -1,99997
    bis -2,0005.
- **r1-s0** (teil2 s = 0, L = 16, 02:25:25 bis 02:25:36 UTC) und **r1-rot** (Drehung, L = 16, cpu6, gleiche Zeit):
  - gamma(x0 = 6) = 1,0912322 gegen REGGE-ZEIT-1 1,0912267 (L = 16; Kugel- statt Wuerfelbilder). Drehung gleich auf
    5e-8 entlang der gedrehten Achse. Zeilennormierte Kondition 1,50.
- **r1-s02** (teil2 s = 0,2, L = 8, 02:26:50 bis 02:27:00 UTC, kein Punkt im Urteilsbereich). Gesehen, nur Codepfad:
  - Gleichungsresiduum 1,4e-11, Nullraumresiduum 1,2e-12, Imaginaerteil 9,4e-15, Fehlwinkel der Eichmoden 5,5e-13,
    flach 4,4e-15 (Teil von SC0 (a) fuer s = 0,2), T gegen K 6,4e-12, RNC gegen statisch 4,8e-12 bzw. 1,3e-11.
  - **Unbeabsichtigt gesehen** (stand in der Logzeile): Eigenwerte des Versklavungssystems C^T M0 C bei s = 0,2:
    -12,07; -3,61; -2,21; -1,74; **+0,360** (Vorzeichen von M; in H = -M ist die gehobene Hyperdiagonal-Mode also
    **negativ**), Kondition 33,5. Hintergrund max abs(F0) 16,3, kappa-Differenz 2,1e-4.
  - Nicht angesehen: Nullmodenzahlen und gamma-Werte auf L = 8 (gamma fuer s != 0 wird nicht ausgegeben).
- **r1-s0L32** (teil2 s = 0, L = 32, 02:26:50 bis 02:27:14 UTC, cpu6): Kontrolle [F10] gamma(6) = 1,08722717 gegen
  1,08722700 (1,7e-7). A7 damit sichtbar erfuellt.
- **Probe der Auswertung** (02:27:41 bis 02:27:44 UTC): auf r1 mit umbenannten Codeproben als "s = 0,1/0,2" und r1-s0L32
  als beide Teil-2-Dateien. Alle Codepfade liefen; die Urteile dieser Probe sind bedeutungslos. Probebilder angesehen
  (nur bild-gamma.png, mit s = 0-Daten).
