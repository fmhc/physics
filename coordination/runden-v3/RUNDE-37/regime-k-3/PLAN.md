# REGIME-K-3: Plan (Code-Agent fuer die Leitung claude-primary, Runde 49)

- Start 2026-10-05 14:13:04 CEST (date). Projekt-grep 14:30:35 CEST. Plantext ab 14:30:46 CEST (date), vor jedem
  Rauchtest und vor jeder Rechnung. Zeitbox 150 min ab Start (Ende spaetestens 16:43:04 CEST).
- Grundlage: KARTE.md (RT0 bis RT3, Wortlaut, Schwellen und Wahrscheinlichkeiten unveraendert).
- Gelesen: KARTE.md; regime-k-2/ (KARTE, PLAN.md.eingefroren-20261005-130842, ERGEBNIS, code/rk.py, code/rk2.py,
  diff code-fix); regge-welle-1/ (ERGEBNIS, PLAN.md.eingefroren-20261004-044955 Abschnitte 1 bis 4); pachner-takt-1/
  (ERGEBNIS, code/pt.py: geometrie, Schicht, analyse_takt); ueberleitung-kh-1/ERGEBNIS; licht-gleich-l/DOSSIER.md
  Zeilen 88 bis 108 (Projekt-grep-Treffer "Transfermatrix").
- Kennzeichen: [M] Mathematik (Schreibtisch, vorab), [P] Projektdatei, [E] hier gerechnet, [F] Festlegung dieses Plans,
  [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- Alles synthetische, linearisierte Gitterrechnung um flach. Keine Messdaten, keine Messdatenbestaetigung.

## 1. Vorab

### 1.1 Projekt-grep (14:30:35 CEST, runden-v3/RUNDE-*.md und RUNDE-37/**/*.md, mit allen Ausschluessen)

- "Transfermatrix|symplekt" in den Rundentabellen: RUNDE-49 (Start dieser Karte), RUNDE-48 (Symplektik bei 3-2- und
  4-1-Zuegen, Dittrich/Hoehn [P]). In RUNDE-37: LICHT-GLEICH-L (DOSSIER Zeilen 92 bis 105: "euklidische,
  reflexionspositive Wirkung ... T = exp(-a H) eine Transfermatrix"; "negative Transfermatrix-Eigenwerte, sobald die
  euklidische Symmetrie gebrochen ist" [P]). **Keine** Transfermatrix-Rechnung auf Kuhn, B1 oder V gefunden.
- Verwandt [P]: PACHNER-TAKT-1 (Hoehns Lagrange-Zweiform Omega~ der Schicht, Rang = E - G, euklidisch; nur Rang, keine
  Eigenwerte eines Takts); UEBERLEITUNG-KH-1 (Lapse = Zeltstange, Shift = affiner Teil der Diagonalen, Grenzfall
  h -> 0 auf Kuhn); REGIME-K-2 (Laurent-Form H(k_s, z), Nullstellen in R und Zensus).

### 1.2 Ableitbarkeit (Agent; die Karte nennt RT1 bis RT3 "nicht ableitbar")

- **[M] Kern der Sache:** Die Eigenwerte der Takt-Transfermatrix (Abschnitt 2) sind genau die Nullstellen z der
  eichreduzierten Laurent-Form det' H(k_s, z) = 0 mit z = exp(i k_tau tau), also dieselben z wie das
  Polynom-Eigenwertproblem von REGIME-K-2 (Schur-Komplement und Eichreduktion erhalten die Nullstellen). Mit der
  Konvention von REGGE-WELLE-1 (Abschnitt 2.5) ist abs(lambda) = exp(abs(Arg z)).
- **Folge [P, M]:** REGIME-K-2 fand auf V-A bei abs(k) = 0,05 TT-Nullstellen mit abs(Im omega)/abs(k) bis 1,9e-4, echt
  (s_voll <= 3,9e-16). Daraus folgt vorab abs(lambda) - 1 ~ abs(Im omega) tau ~ 9,5e-6 fuer die TT-Moden:
  - RT1 (Schwelle 1e-8) ist **bedingt vorab verfehlt**, RT2 (Schwelle 1e-6) **bedingt vorab eingetroffen**, beides nur
    unter der Bedingung, dass REGIME-K-2 richtig gerechnet hat. Dazu kommen die Zensus-Wurzeln mit abs(z) = 1
    (Im omega ~ 2,57), die nach 2.5 abs(lambda) ~ e^2,57 ergaeben.
  - Die Lesart der Karte zu RT1 ("die komplexen Frequenzen aus REGIME-K-2 waeren dann ein Effekt der Nullstellensuche")
    prueft diese Rechnung trotzdem: Der Weg hier (Schicht, Bulk-Elimination, z-unabhaengige Eichreduktion, volles
    Spektrum) ist unabhaengig vom festen Komplement Q0, vom Bereich R und von der Aberth-Verfeinerung in REGIME-K-2.
- **Nicht ableitbar:** RT0 (Kuhn hat neben dem TT-Paar je k eine dritte Konfigurationsgroesse, Abschnitt 2.3; deren
  Eigenwertpaar liegt nach dem REGIME-K-2-Zensus nicht in 0,09 <= abs(z) < 1 [P], Lage und Vorzeichen unbekannt), RT3
  (Zaehlung auf B1 gegen V an allen k), die Zahl und Lage aller instabilen Eigenwerte, der BZ-Rand.

## 2. Transfermatrix eines Takts [M, F]

### 2.1 Schicht, Randdaten, Bulk

- Gitter unveraendert aus REGIME-K-2 (rk2.baue2, tau = 1): Zeltstangen-Treppe; je Takt wird jede Ecke einmal um tau
  gehoben; ueber jedem Tetraeder v0 < v1 < v2 < v3 die vier 4-Simplizes S_j = {v0', ..., vj', vj, ..., v3}.
- **Schicht n** = alle 4-Simplizes eines Takts zwischen den Flaechen Sigma_n (Ecken auf Stufe n) und Sigma_n+1. Die Kanten
  eines Simplex sind (nach den Stufenindizes ihrer Ecken):
  - **Randdaten l_n:** Kanten mit beiden Ecken auf Stufe n (die raeumlichen Kanten des 3D-Netzes; wegen der gestaffelten
    Hoehen hb liegen sie bei B1 und V nicht in einer Ebene). E_s je Zelle: Kuhn 7, B1 28, V 68.
  - **Randdaten l_n+1:** dieselben Kanten auf Stufe n+1.
  - **Bulk b_n:** gemischte Kanten = Zeltstangen (v, v') und Diagonalen v' - w (v vor w in der Hubfolge), NB = E_s + NV je
    Zelle. Jede Bulk-Kante liegt in genau einer Schicht.
  - Zaehlung: 2 E_s + NV = NE (Kuhn 15, B1 60, V 146) wie in REGIME-K-2 [P].
- **Schicht-Hesse H_S(k_s)** (Bloch nur im Raum): aus rk.Gitter.Hloc (= -M je Simplex, unveraendert), mit Phasen
  exp(i k_s . T) der raeumlichen Basisversaetze; Bloecke (l, b, l'). Ohne die Randterme A''psi der offenen Schicht:
  Sie heben sich zwischen Nachbarschichten weg und verschieben die Impulse nur um K l (kanonische Abbildung
  [[I, 0], [K, I]]), Eigenwerte unveraendert [M].
- **Lapse und Shift [M, wie UEBERLEITUNG-KH-1 P]:** Lapse = Zeltstange, Shift = Diagonalen (affiner Teil); beide sind
  Bulk und werden je Schicht eliminiert. Ihr Eichinhalt sind die 4D-Eckverschiebungen der Stufen n und n+1:
  - raeumlich (3 je Ecke, Shift-artig) und zeitlich (1 je Ecke, Lapse-artig) wirken auf l_n ueber G_l (2.3);
  - liegt Sigma_n flach (Kuhn, alle hb = 0), wirkt die zeitliche Verschiebung in erster Ordnung **nur** im Bulk: H_bb
    hat dann je Ecke eine Nullrichtung "Lapse unten" und "Lapse oben", und ihre Kopplung an den Rand ist die lineare
    Hamilton-Bedingung c^H l_n = 0 (2.2). Bei B1 und V (gestaffelt) erwartet: H_bb regulaer, keine eigene Bedingung.

### 2.2 Bulk-Elimination (Hoehn) [M, F]

- H_bb = U diag(w) U^H; Nullrichtungen N_b: abs(w) <= 1e-10 max abs(w). Auf dem Komplement Schur-Elimination:
  E = H_rr - H_rb U_+ diag(1/w_+) U_+^H H_br (r = Rand l, l'); Bloecke A = E[l,l], B = E[l,l'], B' = E[l',l], D = E[l',l'].
  **Meldung (Ausweichpfad "Pseudo-Inverse im Bulk"):** Das ist die Pseudo-Inverse von H_bb; sie ist nur zulaessig, wenn
  die Nullrichtungen wie folgt eingeordnet sind. Gezaehlt und berichtet je Netz.
- Kopplungen der Nullrichtungen: P = H_lb N_b (unten), P' = H_l'b N_b (oben). Einordnung (Singulaerwerte <= 1e-10 relativ
  zu max abs(H_S)):
  - entkoppelt (P = P' = 0: tote Kante), nur unten (P' = 0: Vor-Bedingung P^H l_n = 0), nur oben (P = 0:
    Nach-Bedingung P'^H l_n+1 = 0), **gemischt** (Rest).
  - Bedingungsraum C = Bild der Vor-Bedingungen; gefordert: Bild der Nach-Bedingungen = C (groesster Sinus der
    Hauptwinkel <= 1e-8) und keine gemischte Richtung. Sonst ist der Punkt **gesperrt** ("bulk").
- Rekursion (Bewegungsgleichung fuer l_n) [M]: B' l_n-1 + (A + D) l_n + B l_n+1 + C mu_n = 0, C^H l_n = 0, mu_n frei
  (Lapse-Multiplikator). Bloch in der Zeit (l_n = u z^n) gibt F(z) = B'/z + A + D + B z, genau das Schur-Komplement von
  H(k_s, z) aus REGIME-K-2 bezueglich des Bulks; z = exp(i k_tau tau) wie dort.

### 2.3 Eichung, Bedingungen, reduzierter Phasenraum [M, F]

- G_l(k_s) (E_s x 4 NV): Laengenaenderung der Randkanten unter 4D-Verschiebung der Ecken einer Stufe (Kantenvektor u_e
  4D, Phase exp(i k_s . d) wie rk.Gitter.G).
- **Eichidentitaeten [M]:** Aus der Invarianz der Gesamtwirkung unter Verschiebung einer einzelnen Stufe folgt
  B G_l = 0, B^H G_l = 0, (A + D) G_l = 0 und C^H G_l = 0. Geprueft je Punkt (relativ <= 1e-9, sonst
  **gesperrt** "eichung"); dazu B' = B^H (<= 1e-12 relativ, beschreibend).
- **Reduktion:** W = Orthonormalbasis von (Bild [G_l, C])^perp, d = dim W. Eichfixierung G_l^H l = 0 und Bedingung
  C^H l = 0 zugleich; die Multiplikatoren fallen auf W heraus [M]. Erwartet bei k_s != 0 [M]: d = E_s - 4 NV, also
  Kuhn 7 - 3 - 1 = 3 (Rang G_l = 3 NV, eine Hamilton-Bedingung), B1 28 - 16 = 12, V 68 - 40 = 28; Phasenraum 2d.
  Davon 2 TT-Moden; der Rest sind Gittermoden (Kuhn 1, B1 10, V 26). Abweichendes d wird berichtet, sperrt aber nicht.
- **Randdaten und Impulse:** v = W^H l_n (gauge-fixiert), Impuls pi_n = W^H p_n mit p_n = B^H l_n-1 + D l_n (Nach-Impuls
  der Schicht n-1) = -(A l_n + B l_n+1) (Vor-Impuls der Schicht n); auf W ist das Paar (v, pi) kanonisch [M].

### 2.4 Transfermatrix, Symplektizitaet

- B_W = W^H B W, A_W, D_W, B'_W. Ist cond(B_W) <= 1e12:
  T = [[-B_W^-1 A_W, -B_W^-1], [B_W^H - D_W B_W^-1 A_W, -D_W B_W^-1]] auf (v, pi), Groesse 2d.
  Sonst **Ausweichpfad mit Meldung:** Begleit-Buendel von F_W(z) = W^H F(z) W (QZ); Eigenwerte mit abs(z) < 1e-10 oder
  > 1e10 bzw. Nenner 0 heissen "nicht propagierend" und zaehlen nicht als physikalisch; keine Symplektizitaetsprobe.
- **Symplektizitaet [M]:** T^H J T = J mit J = [[0, I], [-I, 0]] (aus der Erzeugenden S(v, v'): fuer zwei Loesungen ist
  v_x^H pi_y - pi_x^H v_y vor und nach dem Takt gleich, beide Seiten = v'_x^H B^H v_y - v_x^H B v'_y). Folge: Eigenwerte in
  Paaren z, 1/conj(z). Kennzahlen je Punkt:
  s_sym = max abs(T^H J T - J) / max(1, max abs(T)^2); Paarfehler p_err = max_j min_i abs(z_i - 1/conj(z_j)) abs(z_j).
  Beide <= 1e-8, sonst **gesperrt** ("symplektisch").
- **Eigenwerte:** eig(T) (Hauptweg); Kontrolle: QZ des Begleit-Buendels von F_W; Fehlerschaetzung je Eigenwert
  err_j = abs(z_T - z_QZ) (naechster Partner), eps_j = err_j/abs(z_j) als Unsicherheit von Arg z.
- **Echtheit (komplementfrei, wie REGIME-K-2 s_voll):** fuer jeden Eigenwert z der (r+1)-kleinste Singulaerwert der vollen
  4D-Form H(k_s, z) (rk2.Laurent) relativ zum groessten, r = Rang der 4D-Nullbasis (Eichung + tote Kanten) bei diesem z.
  Jeder Eigenwert mit s_voll > 1e-8 sperrt den Punkt ("unecht").

### 2.5 Lorentz-Fortsetzung (Konvention von REGGE-WELLE-1) [F, M, L]

- **Festlegung:** wie REGGE-WELLE-1 und REGIME-K-2 die formale Fortsetzung k_tau = i omega der euklidischen Form bei
  festem Gitter: z = exp(i k_tau tau) = exp(-omega tau), omega = -Log(z)/tau (Hauptzweig, Arg in (-pi, pi]). Eine
  Eigenmode des euklidischen Takts mit Eigenwert z ist in echter Zeit die Welle exp(-i omega t); ihr Faktor je Takt ist
  lambda = exp(-i omega tau) = exp(i Log z), also abs(lambda) = exp(-Arg z).
- **Begruendung:**
  - Die Karte verlangt diese Konvention; nur sie macht RT0 mit REGGE-WELLE-1 vergleichbar (dort laufen die Kuhn-Wellen
    genau dann, wenn z reell positiv ist).
  - [L] Osterwalder-Schrader bzw. Luescher (Gitter-Transfermatrix): Ist die euklidische Transfermatrix positiv,
    T = exp(-tau H), dann ist H = -Log(T)/tau selbstadjungiert und exp(-i H t) die Echtzeit-Entwicklung. Das ist dieselbe
    Zuordnung omega = -Log z/tau; LICHT-GLEICH-L nennt "negative Transfermatrix-Eigenwerte" als Bruchstelle [P].
  - **Zweigfrage:** abs(exp(i (Log z + 2 pi i m))) = exp(-(Arg z + 2 pi m)) = 1 genau fuer z > 0 und m = 0. "Auf dem
    Einheitskreis" ist also **zweigunabhaengig** gleichbedeutend mit z reell positiv [M]; der Hauptzweig ist der einzige,
    der bei z -> 1 stetig lambda -> 1 gibt. Zweigabhaengig bleibt nur, ob ein Eigenwert abseits des Kreises waechst oder
    abklingt.
  - Nicht gerechnet: die geometrische Fortsetzung tau -> i T (Lorentz-Regge mit zeitartigen Zeltstangen). Bei tau = 1 waere
    z. B. die Kuhn-Diagonale (1, 0, 0, 1) lichtartig, und sie ist nicht die Konvention von REGGE-WELLE-1.
- **Kennzahl [F]:** delta(z) = abs(Arg z) in [0, pi]. Weil T(-k_s) = conj T(k_s) exakt gilt (Hloc reell) [M], hat ein
  reelles Feld mit Wellenvektoren +k_s und -k_s den Faktor exp(delta) je Takt (Hauptzweig). Festlegung:
  **abs(lambda) := exp(delta(z))**, also "abs(lambda) - 1" = exp(delta) - 1 >= 0; fuer z < 0 (delta = pi, auf dem Schnitt)
  ist das die ungunstigere Seite des Schnitts. Partner z und 1/conj(z) haben dasselbe delta.
- **Sicherheit:** Ein Test mit Schwelle theta auf exp(delta) - 1 ist je Eigenwert "erfuellt", wenn
  exp(delta + eps) - 1 < theta, "verletzt", wenn exp(delta - eps) - 1 > theta, sonst "unsicher" (Punkt fuer diesen Test
  gesperrt). eps = max(eps_j, 1e-15).
- Beschreibend je Eigenwert: abs(z), Arg z, omega, "euklidisch auf dem Kreis" (abs(abs(z) - 1) <= 1e-8: euklidischer
  Nulldurchgang, REGIME-K-2 4.5), "Schnitt" (abs(Arg z) >= pi - max(eps, 1e-9): z < 0, gestaffelte Gitterwelle).

### 2.6 Zuordnung TT gegen Gittermoden [F]

- TT-Kandidaten an einem Punkt: Eigenwerte mit abs(Log z) <= 3 abs(k_s) tau (Lichtkegelnaehe; erwartet 4 = zwei Moden,
  je vorwaerts und rueckwaerts).
- TT-Anteil (eichinvariant wie REGGE-WELLE-1, rk2.tt_klasse): Kernvektor u = W v (Randkanten), Klasse u + Bild G_l gegen
  das Kantenbild der Kontinuums-TT-Moden h_+, h_x (raeumlich, transversal zu k_s, spurfrei):
  delta l_e = E_e^T h E_e/(2 l_e) exp(i k_s . x_e) exp(Log(z) t_e/tau) (x_e, t_e: Kantenmitte; der Zeitfaktor
  beruecksichtigt die gestaffelten Hoehen).
- Ein Punkt ist **TT-zuordenbar**, wenn genau 4 Kandidaten und jeder TT-Anteil >= 0,9; sonst fuer RT1 **gesperrt** ("tt").
- Gittermoden = alle uebrigen physikalischen Eigenwerte.

## 3. Netze, Arme, k-Raster [F]

| Arm | Netz | Zweck |
|---|---|---|
| KW | Kuhn, tau = 1 (rk2.baue2('KW')) | RT0 (Kontrolle) |
| V-A | gefuelltes V, Hubfolge A, tau = 1 (Hauptarm von REGIME-K-2) | RT1, RT2, RT3 |
| B1-t1 | B1-Kopie ohne Fuellung, tau = 1 | RT3 |
| V-B, S-A | Zeitspiegel von V-A bzw. Fuellung S | nur beschreibend, nur wenn Zeit bleibt |

- **Raster (wie REGIME-K-2):** 49 raeumliche Richtungen = rw24 (REGGE-WELLE-1) + rk25 (raeumliche der 92 Richtungen),
  aus rk2 unveraendert; Betraege: die 9 kl-Werte des euklidischen Rasters (0,005; 0,01; 0,02; 0,03; 0,05; 0,07; 0,1; 0,14;
  0,2; abs(k) = kl/lmean, lmean = mittlere 4D-Kantenlaenge wie REGIME-K-2) und abs(k) = 0,05 und 0,2 in Koordinaten
  (Echtzeit-Betraege von REGIME-K-2). 49 x 11 = 539 Punkte je Netz.
- **Brillouin-Zone:** k_s = 2 pi A3^-T m / 8, m in {0..7}^3 ohne m = 0: 511 Punkte (enthaelt bei V die Punkte X, L, W, K, U
  und bei den kubischen Netzen X, M, R) [M].
- **BZ-Rand [F]:** Gitterpunkte auf dem Rand der Wigner-Seitz-Zelle des reziproken Gitters: die zwei kleinsten Abstaende
  abs(k_s - G) ueber G = 2 pi A3^-T n, n in {-2..2}^3, sind gleich (auf 1e-9 relativ). Je Netz gezaehlt und in einer
  eigenen Tabelle berichtet.
- -k_s ist nicht eigens gerechnet: T(-k_s) = conj T(k_s) [M]; Probe an den Paaren x+/x-, xy+/xy-, xyz+/xyz-,
  123/-1-2-3 der rw24 (Eigenwertmengen konjugiert auf <= 1e-9).
- k_s = 0 ist ausgeschlossen (Jordan-Bloecke bei z = 1, globale Verschiebungen); "an allen gerechneten k" heisst Raster
  plus 511 BZ-Punkte.

## 4. Urteilsregeln (mechanisch in code/rk3.py, Modus auswertung)

- **Gesperrt** ist ein Punkt bei: "bulk" (gemischte Nullrichtung oder Vor- und Nach-Bedingungen verschieden), "eichung",
  "symplektisch" (nur wenn T existiert), "unecht" (s_voll > 1e-8). Pro Test zusaetzlich "unsicher" (2.5) und fuer RT1 "tt"
  (2.6). Ausweichpfad "Buendel" (cond(B_W) > 1e12) und "Pseudo-Inverse im Bulk" sperren nicht, werden aber gezaehlt.
- **Dreiwertig** fuer RT0, RT1, RT2 (wie REGIME-K-2): ein Verstoss an einem ungesperrten Punkt entscheidet; sonst ein
  gesperrter Punkt -> "nicht auswertbar"; sonst das Ergebnis.
- **RT0** ("Auf Kuhn liegen alle physikalischen Eigenwerte der Takt-Transfermatrix auf dem Einheitskreis (abs(lambda) - 1 <
  1e-10) an allen gerechneten k, passend zu REGGE-WELLE-1"), KW, 539 + 511 Punkte:
  - eingetroffen, wenn jeder physikalische Eigenwert an jedem Punkt exp(delta) - 1 < 1e-10 erfuellt; ein verletzter
    Eigenwert an einem ungesperrten Punkt -> nicht eingetroffen.
  - Nach Plan = nach Kartenwortlaut ("auf dem Einheitskreis" ist zweiseitig; der einseitige Klammerausdruck folgt daraus).
- **RT1** ("Auf V liegen fuer die zwei TT-Moden bei abs(k) <= 0,1 die Eigenwerte auf dem Einheitskreis (abs(lambda) - 1 <
  1e-8)"), V-A:
  - Nach Plan: Rasterpunkte mit abs(k_s) <= 0,1 in Koordinaten (kubische Kante 1); an jedem die 4 TT-Eigenwerte (2.6) mit
    exp(delta) - 1 < 1e-8.
  - Nach Kartenwortlaut: dasselbe zusaetzlich mit der Lesart kl <= 0,1 (wie REGIME-K-2 RQ4); gleiche Urteile -> dieses
    Urteil, verschiedene -> unklar.
  - **Pipeline (gilt fuer RT1, RT2, RT3):** PK-T (auf KW an allen Rasterpunkten mit abs(k) <= 0,1 genau 4 TT-Kandidaten,
    TT-Anteil >= 0,9, exp(delta) - 1 < 1e-10: das ist der Teil von RT0, den REGGE-WELLE-1 schon belegt), K1 auf allen Armen
    und K6 auf KW, B1-t1 und V-A. Faellt eines: "unklar (Pipeline)", Werte trotzdem berichtet. RT0 selbst: "unklar
    (Pipeline)", wenn K1 oder K6 auf KW faellt. (Ein Verfehlen von RT0 durch die dritte Kuhn-Mode ist Physik, keine
    Pipeline.)
- **RT2** ("Auf V gibt es an mindestens einem gerechneten k einen Eigenwert mit abs(lambda) > 1 + 1e-6 (Instabilitaet,
  vermutlich aus den Gittermoden negativer Steifigkeit)"), V-A, 539 + 511 Punkte:
  - Nach Plan: eingetroffen, wenn an einem ungesperrten Punkt ein physikalischer Eigenwert "verletzt" mit Schwelle 1e-6
    ist (exp(delta - eps) - 1 > 1e-6, Schnitt-Eigenwerte eingeschlossen); sonst bei Sperren nicht auswertbar; sonst nicht
    eingetroffen.
  - Nach Kartenwortlaut: wie Plan, aber abs(lambda) auf dem Hauptzweig bei +k und -k (Schnitt-Eigenwerte z < 0 klingen dort
    an beiden ab und zaehlen nicht). Gleich -> dieses Urteil, sonst unklar.
  - Die Klammer "vermutlich aus den Gittermoden" ist Lesart, kein Urteilsteil; berichtet wird, welche Moden (TT,
    Gittermoden, euklidisch auf dem Kreis, Schnitt) instabil sind.
- **RT3** ("Auf B1 ohne Fuellung gibt es hoechstens halb so viele instabile Eigenwerte je k wie auf V"):
  - N_inst(k) = Zahl der physikalischen Eigenwerte mit Status "verletzt" bei Schwelle 1e-6 (wie RT2 nach Plan).
  - Nach Plan eingetroffen, wenn (a) an jedem Rasterpunkt (gleiche Richtung und gleiche Betragsangabe, also gleiches kl
    bzw. gleiches abs(k) in Koordinaten; beide ungesperrt) N_B1(k) <= N_V(k)/2, (b) ueber die BZ max N_B1 <= max N_V / 2
    und (c) Mittel N_B1 <= Mittel N_V / 2 (BZ-Gitter beider Netze verschieden, daher nur Verteilungen).
  - Nach Kartenwortlaut: dasselbe mit der Zaehlung der Kartenlesart von RT2 (ohne Schnitt-Eigenwerte); gleich -> dieses
    Urteil, sonst unklar.
  - Mehr als 10 % gesperrte Punkte auf einem der beiden Netze -> nicht auswertbar.

## 5. Kontrollen (technisch)

- **K1** Schicht gegen rk.Gitter: H_voll(z) aus den Schichtbloecken
  [[H_ll + H_l'l' + z H_ll' + H_l'l/z, H_lb + H_l'b/z], [H_bl + z H_bl', H_bb]] gegen rk.Gitter.H(k_s, k_tau) bei 32
  Zufallspunkten: Spektren gleich auf <= 1e-12 relativ.
- **K2** Eichidentitaeten (2.3), Hermitezitaet, B' = B^H.
- **K3** Symplektizitaet und Paarfehler (2.4); T gegen QZ-Buendel (err).
- **K4** s_voll je Eigenwert (2.4).
- **K5** -k-Probe an den rw24-Paaren (3).
- **K6** Reproduktion REGIME-K-2 (dort eingefroren gerechnet, Dateien auf der .69 unveraendert gelesen): je Richtung
  bei abs(k) = 0,05 (Koordinaten) liegt zu jeder Nullstelle omega in R ein Takt-Eigenwert mit
  abs(z - exp(-omega tau)) <= 1e-8 abs(z) (V-A 49 Richtungen, KW und B1-t1 je 24). Faellt K6 auf V-A: RT1 "unklar
  (Pipeline)".
- **K7** Zaehlungen: E_s, NB, NE, Nullrichtungen von H_bb und ihre Einordnung, Rang G_l, Rang C, d je Punkt.
- Beschreibend: KW-TT gegen die Wuerfelgitter-Formel sinh^2(omega/2) = Summe sin^2(k_i/2) (REGGE-WELLE-1 [P]).

## 6. Laeufe auf der .69

- Ordner /home/fmh/fmhc-physics-remote/regime-k-3/ (code/, rauch/, lauf/). Aufruf ueber
  /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu8, cpu9, cpu10; je Lauf <= 600 s, 1 Thread, 4 GB.
- Code: code/rk3.py (neu); unveraendert kopiert aus RUNDE-37/regime-k-2/code (eingefroren): rk.py, rk2.py, pt.py, ew.py,
  tp.py. REGIME-K-2-Referenzen fuer K6: /home/fmh/fmhc-physics-remote/regime-k-2/lauf/welle-*-koord-*.json (nur gelesen).
- Modi: transfer --arm X --satz raster|bz [--teil i/n], auswertung --ein ..., Laufketten je Spur.
- Hauptlaeufe (nach den Rauchtests festgelegt): cpu8 KW raster, KW bz, B1-t1 raster, B1-t1 bz; cpu9 V-A raster; cpu10
  V-A bz; danach auswertung; V-B und S-A nur beschreibend, wenn Zeit bleibt.

## 7. Rauchtests (je <= 120 s, nach diesem Plantext)

- Nur Laufzeit, Rueckgabewert, Schluessel, Zaehlungen (E_s, NB, NE, Nullrichtungen von H_bb und Einordnung, Rang G_l,
  Rang C, d) und technische Kontrollen (K1, K2, s_sym, p_err, err, s_voll-Maximum, K5) an wenigen Punkten.
- **Nicht gelesen** fuer alle Netze: Eigenwerte, delta, abs(lambda), Zaehlungen instabiler Eigenwerte, TT-Zuordnung,
  K6-Abstaende, Urteile. Die Rauch-Ausgabe schreibt dafuer einen eigenen Abschnitt "kontrollen"; nur dieser wird gelesen.
- Danach PLAN.md und code/ als *.eingefroren-<zeit> kopieren, sha256 in EINGEFROREN-SHA256.txt (lokal und .69).

## 8. Agenten-Vorhersagen (vorab, gehen in kein Urteil ein)

| Nr | Vorhersage |
|---|---|
| A1 | K6 auf V-A erfuellt: die Takt-Eigenwerte geben die TT-Nullstellen von REGIME-K-2 auf <= 1e-10 wieder (85 %) |
| A2 | RT1 nicht eingetroffen, TT-Wert exp(delta) - 1 bei 0,05 bis ~1e-5 (85 %) |
| A3 | RT2 eingetroffen, groesster Wert aus Gittermoden mit abs(z) = 1 (delta bis ~2,6) (85 %) |
| A4 | RT0 eingetroffen (55 %); das dritte Kuhn-Paar hat z > 0 (55 %) |
| A5 | RT3 nicht eingetroffen (55 %): B1 hat je k ein Schnitt-Paar (z < 0) wie in REGIME-K-2, V an vielen BZ-k nur wenige |
| A6 | d = E_s - 4 NV an allen generischen k (Kuhn 3, B1 12, V 28) (75 %); H_bb regulaer bei B1 und V, bei Kuhn 3 Nullrichtungen je k (tote Kante, Lapse unten und oben) (65 %) |

## 9. Rauchtests und Aenderungen vor dem Einfrieren (Nachtrag ab 14:55:51 CEST, date)

- Alle Rauchtests ueber kleintest.sh (cpu8, cpu9, cpu10), je 4 Punkte Raster und 4 Punkte BZ je Netz, rc = 0, je
  <= 34 s. Gelesen nur der Abschnitt "kontrollen" (Zaehlungen, Kontrollnormen, Zeiten), keine Eigenwerte, kein delta,
  keine Urteile. Codestaende r3 und r4 liegen als rauch-69/rk3-stand-r3.py.txt und rk3-stand-r4.py.txt bei.
- **r1** (12:38:49 UTC, KW; B1/V wegen eines Shellfehlers nicht gestartet): K1 1,1e-15. H_bb hat 3 Nullrichtungen je k
  (entkoppelt 1 = tote Kante, nur unten 1, nur oben 1 = Lapse), Rang C = 1, d = 3. **Befund 1:** die ungeprojizierten
  Eichidentitaeten B G_l = 0 usw. gelten bei Kuhn nicht (0,2 bis 0,8), weil die Lapse-Multiplikatoren mitwandern; gelten
  muss nur W^H B G_l = 0 usw. [M, 2.3 berichtigt]: Die Gesamtgleichung ist in (l, mu) eichinvariant, und die
  C-Anteile fallen auf W heraus. **Befund 2:** B_W ist bei Kuhn exakt singulaer (Rang d - 1; cond 7e9 bis 1e16): eine
  Randrichtung ohne Traegheit (wie die Raumdiagonale in UEBERLEITUNG-KH-1 [P]). Die Transfermatrix mit B_W^-1 war dort
  unbrauchbar (Paarfehler 3e5).
- **Aenderungen nach r1:**
  - Eichpruefung auf W projiziert; Schwelle 1e-6 statt 1e-9; ungeprojizierte Werte beschreibend ("eich_roh").
  - Sinus Vor-/Nach-Bedingungen: Schwelle 1e-5 statt 1e-8 (bei kl = 0,005 numerisch 2,6e-7, faellt wie k^-4: Rundung).
  - **Statische Richtungen (neu):** Singulaerwerte von B_W <= 1e-8 relativ; ist ihr rechter Kern gleich dem linken
    (Sinus <= 1e-6), werden sie statisch eliminiert (Schur ueber (A + D) auf dem Kern), wie die Regel "Raumdiagonale
    statisch" aus UEBERLEITUNG-KH-1 [P]. Danach T auf dem Rest mit symmetrischer Aufteilung A = D = M_eff/2 (Eigenwerte
    unabhaengig von der Aufteilung [M]). Ihre formalen Eigenwerte 0 und unendlich heissen "nicht propagierend" und zaehlen
    **nicht** als physikalische Eigenwerte (Festlegung, Selbstanzeige im Ergebnis). Sonst Buendel-Ausweichpfad.
  - **Verfeinerung (neu):** Jeder T-Eigenwert wird mit Newton (logarithmische Ableitung) auf der vollen 4D-Form
    det Ql^H H(k_s, z) Qr = 0 nachgeschaerft (Ql, Qr feste Komplemente der Eichnullraeume links N(1/conj z0) und rechts
    N(z0); rk2.Laurent, unabhaengig von der Bulk-Elimination). err_j = 2 x letzter Newton-Schritt (statt T gegen QZ);
    Abbruch bei Schritt <= 1e-15 abs(z), wenn der Schritt ab der dritten Iteration nicht mehr faellt, oder nach 50.
    Laufen zwei verschiedene Startwerte (Abstand > 1e-6 relativ) auf dieselbe Nullstelle (<= 1e-12), werden sie
    nacheinander mit Deflation neu gesucht. Neue Sperre "verfeinerung": Verschiebung > VERF_MAX relativ oder bleibende
    Duplikate. Paarfehler p_err jetzt an den verfeinerten Eigenwerten; T-Paarfehler beschreibend.
- **r2** (12:44:39 bis 12:45:47 UTC, alle drei Netze): KW ohne Sperre. B1 und V bei kl = 0,005 und 0,02: H_bb hat dort
  einen Eigenwert unter 1e-10 relativ, als "gemischte Nullrichtung" eingeordnet -> Sperre "bulk" und unbrauchbare
  Eigenwerte. **Befund 3:** Das ist keine Eichrichtung, sondern die bei k -> 0 weich werdende Relativverschiebung der
  Stufen (Eigenwert etwa ~ (kl)^4); die Bulk-Elimination wird dort schlecht konditioniert. V-A brauchte 8 s je Punkt.
- **Aenderungen nach r2:** TOL_BB 1e-14 statt 1e-10 (Kuhns echte Nullrichtungen liegen bei <= 5e-17); kleinster
  H_bb-Eigenwert wird berichtet (bb_min_rel); Newton mit Stagnationsabbruch (Laufzeit).
- **r3, r4** (12:48:54 bis 12:52:31 UTC): r3 wie oben; r4 probierte einen zweiten Eigenwertweg (Begleitbuendel der vollen
  4D-Form mit fester Eichfixierung auf den Randkanten). Er gab 38 bis 90 statt 24 bzw. 56 endliche Eigenwerte (Jordan-
  Haufen bei 0 und unendlich) und wurde **verworfen** (nicht im eingefrorenen Code).
- **r5** (12:54:40 bis 12:55:03 UTC, eingefrorener Stand bis auf VERF_MAX): KW 8 Punkte ohne Sperre (s_voll <= 1,4e-16,
  err <= 5,2e-13, Paarfehler <= 4,2e-13). B1: 7 von 8 Punkten ohne Sperre; kl = 0,02 gesperrt (symplektisch, unecht:
  Deflation nicht konvergiert). V-A: 7 von 8 ohne Sperre; kl = 0,005 gesperrt (bulk: H_bb-Eigenwert 6,9e-15 relativ).
  Laufzeit V-A ~2,1 bis 2,5 s je Punkt, B1 ~0,14 s, KW ~0,015 s.
- **Aenderung nach r5:** VERF_MAX = 1e-2 statt 1e-4 (r5 gesperrt sonst V bei kl = 0,02 und 0,07 mit Verschiebungen
  4,3e-3 und 1,5e-4 trotz s_voll <= 6e-16 und ohne Duplikate). Die Zaehlung plus Duplikatpruefung plus s_voll sichert,
  dass die 2d verfeinerten Werte die 2d verschiedenen Nullstellen sind [M: det F_W hat genau 2d Nullstellen].
- **r6** (12:55 UTC): Auswertung auf den r5-Dateien, nur rc = 0 und Schluessel gelesen (K6 dort ohne passende Punkte).
- **Erwartete Folgen fuer die Urteile (vorab benannt):** Bei kl = 0,005 (V, wohl auch B1 bei einzelnen kleinen k) sind
  Punkte gesperrt; RT1 bleibt entscheidbar, wenn an einem ungesperrten Punkt ein Verstoss liegt; RT3 wird bei mehr als
  10 % gesperrten Punkten "nicht auswertbar". Keine Schwelle einer Vorhersage wurde geaendert.
- **Hauptlaeufe (festgelegt):** Raster und BZ je in 4 Teile fuer V-A (--teil i/4); cpu8: KW raster, KW bz, B1-t1 raster,
  B1-t1 bz, V-A bz 3/4, V-A raster 3/4; cpu9: V-A raster 0/4, 1/4, 2/4; cpu10: V-A bz 0/4, 1/4, 2/4. Danach auswertung
  (cpu8) mit den REGIME-K-2-Referenzen welle-V-A-koord-rw24, welle-V-A-koord-rk25, welle-KW-koord-rw24,
  welle-B1-t1-koord-rw24 (.69, regime-k-2/lauf, nur gelesen). V-B und S-A entfallen (Zeit).
