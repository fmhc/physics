# REGIME-K-2: Plan (Code-Agent fuer die Leitung claude-primary, Runde 49)

- Start 2026-10-05 12:47:50 CEST (date). Plantext ab 12:57:11 CEST (date), vor jedem Rauchtest und vor jeder Rechnung.
  Zeitbox 150 min ab Start (Ende spaetestens 15:17:50 CEST).
- Grundlage: KARTE.md (RQ0 bis RQ4, Wortlaut, Schwellen und Wahrscheinlichkeiten unveraendert).
- Gelesen: KARTE.md; regime-k-1/ (KARTE, PLAN.md.eingefroren-20261005-121006, ERGEBNIS, code/rk.py, code/pt.py);
  regge-welle-1/ (KARTE, PLAN.md.eingefroren-20261004-044955, ERGEBNIS, code/regge_welle.py); regge-4d-schief-1/ERGEBNIS;
  RUNDE-36/regge-4d-1/ERGEBNIS (Abschnitt 1); tt-iso-1/ (KARTE, ERGEBNIS, code/ew.py Netzaufbau, code/tp.py Konstanten);
  hodge-l/DOSSIER.md (Punkt 1a und Abschnitt 4.3, Delaunay-Probe); dazu regge-welle-schief-1/ERGEBNIS (nur grep nach
  "Zensus", "instabil").
- Kennzeichen: [M] Mathematik (vorab, Schreibtisch), [S] an der Quelle gelesen, [P] Projektdatei, [E] hier gerechnet,
  [F] Festlegung dieses Plans, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- Alles synthetische, linearisierte Gitterrechnung um flach. Keine Messdaten, keine Messdatenbestaetigung.

## 1. Vorab

### 1.1 Projekt-grep (Pflicht, 12:52:10 CEST, runden-v3/RUNDE-*.md, mit allen Ausschluessen)

- "Regge-Welle": RUNDE-36 (Folge von REGGE-4D-1), RUNDE-37 (REGGE-WELLE-1 und REGGE-WELLE-SCHIEF-1 geerntet), RUNDE-40
  (Hinweis auf gestaffelte Moden in REGGE-WELLE-SCHIEF-1), RUNDE-49 (Abschaetzung zu REGIME-K-1: "REGIME-K-2 auf dem
  gefuellten Netz V ... Methode REGGE-WELLE-1").
- "Kuhn": RUNDE-36 (REGGE-4D-1, Rand, Newton), RUNDE-37 (REGGE-4D-SCHIEF-1, REGGE-WELLE-1), RUNDE-38 (INDUZIERT-1),
  RUNDE-44 (TORSION-STEIF-1 erwogen), RUNDE-49.
- "Zelt": RUNDE-41/42 (PACHNER-TAKT-1: Zeltstangen-Takt, Flip-Flop), RUNDE-44, RUNDE-48 (REGIME-K-1 gestartet;
  ZELT-PACHNER-BRUECKE-1 in der Warteschlange), RUNDE-49 (REGIME-K-1 geerntet). Sonst nur "Einzelteil", "Belegstufe".
- "gefuellt": RUNDE-41/42 (EINE-WELT-LOCH-1), RUNDE-43/44 (TT-ISO-1), RUNDE-45 (Danzer), RUNDE-48 (Restleckage),
  RUNDE-49 (Vorbehalt REGIME-K-1). Sonst "Plaetze gefuellt" usw.
- "4D" (ohne Gross-/Kleinschreibung, 21 Tabellen): die 4D-Regge-Karten oben, dazu viele fremde Treffer.
- **Was es schon gibt [P]:** 4D-Regge-Bloch-Hesse euklidisch auf dem Kuhn-Gitter (REGGE-4D-1), auf dem schiefen
  Kuhn-Gitter (REGGE-4D-SCHIEF-1, mit Vorzeichenzaehlung), auf dem B1-Zeltstangen-Gitter ohne Fuellung (REGIME-K-1);
  echte Zeit ueber komplexes k_tau auf Kuhn (REGGE-WELLE-1) und schiefem Kuhn (REGGE-WELLE-SCHIEF-1). **Nicht gefunden:**
  irgendeine 4D-Regge-Rechnung (euklidisch oder echte Zeit) auf dem gefuellten Netz V. Die Kartenzeile "ein Ergebnis
  fuer das gefuellte V mal Zeit ist nicht bekannt" ist bestaetigt.

### 1.2 Kartenberichtigung: V hat keine Oktaeder [P, M]

- Das gefuellte Netz V aus TT-ISO-1 (code/ew.py, geometrie('V')) besteht nur aus Tetraedern: je fcc-Grundzelle 2
  Finn-Tetraeder (finn_auf, finn_ab), 8 Kegel (Kegel der Lochmitte C ueber den Dreiecksflaechen des Lochs) und 48
  Sechsecktetraeder (C, H, v_i, v_i+1; H = Sechseckmitte). Oktaeder mit Diagonalen gibt es nur in der B1-Kopie **ohne**
  Fuellung (pt.py, REGIME-K-1). "Oktaeder-Diagonalen" der Karte trifft V also nicht.
- **Lesart der Diagonalwahl [F]:** Zwei Loecher (C1, C2) teilen je ein Sechseck; zusammen bilden ihre Kegel ueber dem
  Sechseck eine Sechseck-Doppelpyramide. Sie laesst sich auf zwei Arten fuellen, beide in TT-ISO-1 vorhanden:
  - **V** (TT-ISO-1-Hauptnetz): neue Ecke H in der Sechseckmitte, Kanten C-H und H-v_i (12 Tetraeder je Sechseck).
  - **S** (TT-ISO-1 beschreibend, "kantenaermer"): die Achse C1-C2 als Diagonale der Doppelpyramide (6 Tetraeder).
  - Hauptarm ist V, wie in TT-ISO-1 und auf der Karte. Kontrollarm "zweite Diagonalwahl" ist S.
- **Zweite Wahl in 4D [F]:** Die Zeltstangen-Treppe braucht eine Hubfolge der Ecken; sie legt fest, welche
  Diagonalen die 4D-Prismen bekommen (Kanten u'-v). Zusaetzlicher Kontrollarm V-B: dasselbe V mit umgekehrter Hubfolge.

### 1.3 Ableitbarkeit (je Vorhersage)

- **RQ0:** (a) vorab ableitbar [P]: REGGE-WELLE-1 hat genau diese Groesse auf dem Kuhn-Gitter gerechnet (0,99979 bis
  0,99986) und als Wuerfelgitter-Formel sinh^2(omega/2) = Summe sin^2(k_i/2) erkannt; geprueft wird nur mein Code.
  (b) vorab ableitbar [P]: REGIME-K-1 9,7e-10 mit demselben rk.py; geprueft wird nur der Import. Das ist der Sinn einer
  Kontrolle; scheitern kann sie an Fehlern im neuen Code (Laurent-Form, Komplement, Wurzelsuche, Netzaufbau).
- **RQ1:** nicht ableitbar. FFLR nur Abstract [S ueber REGGE-KINETIK-L]; gezeigt fuer Kuhn und B1 [P]. V ist nicht
  Delaunay und nicht gut zentriert (HODGE-L 1a, 4.3 [P]); fuer die Regge-Wirkung spielt das nach Lehrmeinung keine Rolle
  [L], fuer die Gittermoden womoeglich schon.
- **RQ2:** nicht ableitbar. Eine tote Kante braucht an allen ihren Dreiecken einen rechten Winkel gegenueber der Kante
  (REGGE-4D-1, Thales [P]). In V ist das 3D-Dreieck (C, H, v) bei H rechtwinklig (HODGE-L 4.3 [P]), also gegenueber der
  Kante C-v. In der Treppe liegen C, H und v auf verschiedenen Hoehen, der Winkel ist dann generisch nicht recht [M];
  die anderen Dreiecke an C-v sind nicht am Schreibtisch geprueft.
- **RQ3:** nicht ableitbar. Haynsworth [L]: Zahl der negativen Eigenwerte von H_E(k) = negative im Gitterblock +
  negative der Schur-Form (diese hat langwellig genau einen: konform). RQ3 ist also "Gitterblock positiv definit".
- **RQ4:** bedingt ableitbar: Trifft RQ1 ein, hat die fortgesetzte Form langwellig eine Doppelnullstelle bei
  omega = abs(k) mit 1 - v = O((k a)^2) [M, wie REGGE-WELLE-1 PLAN 2]. Nicht ableitbar: der Koeffizient auf V, weitere
  Nullstellen im Bereich R (z. B. aus negativen Gittermoden, REGGE-WELLE-SCHIEF-1 [P]), Aufspaltung oder Anwachsen.

## 2. Gitter [F, M]

### 2.1 Raum

- **V:** aus tt-iso-1/code/ew.py (unveraendert kopiert, mit tp.py): geometrie('V') liefert 10 Untergitter je fcc-Zelle
  (Pyrochlor r_0..r_3 = R8/8, Lochmitten C1 = (-2,-2,-2)/8, C2 = (4,4,4)/8, Sechseckmitten H_a = C1 - R8[a]/8) und
  58 Tetraeder; zerlege() gibt je Ecke (Untergitter, Gitterkoeffizienten in a1..a3). Kubische Kante 1, Translationen
  AV (fcc). Erwartet [M]: 68 Kanten, 116 Dreiecke, 58 Tetraeder je Zelle (Euler 10 - 68 + 116 - 58 = 0).
- **S:** geometrie('S'): 6 Untergitter (r_0..r_3, C1, C2), 34 Tetraeder, 40 Kanten [M].
- **B1, KW:** unveraendert aus rk.py (REGIME-K-1): B1-Kopie ohne Fuellung (kubische Zelle, 4 Ecken), Kuhn-Gitter.

### 2.2 Zeit: Zeltstangen-Treppe (rk.Gitter, unveraendert)

- Je Takt wird jede Ecke einmal um tau gehoben; ueber jedem Tetraeder v0 < v1 < v2 < v3 (Hubfolge) die vier
  4-Simplizes S_j = {v0', ..., vj', vj, ..., v3}, Volumen tau V_tet / 4 [M, REGIME-K-1 PLAN 2.2]. Gueltige Triangulierung
  fuer jede translationsinvariante Gesamtordnung der Ecken [M].
- **Hubfolge V-A (Hauptarm):** Untergitter in der Reihenfolge von ew.py: r_0, r_1, r_2, r_3, C1, C2, H_0, H_1, H_2, H_3;
  Hoehen j/10 mal tau (j = Rang), Hub tau. Gleichmaessig gestaffelt wie REGIME-K-1 (0, 1/4, 1/2, 3/4). Begruendung: Finns
  Netz zeichnet keine Folge aus; die Code-Reihenfolge ist die einfachste ohne Abstimmung. Ordnungsschluessel (Rang,
  x, y, z), also auch bei Kanten innerhalb eines Untergitters eindeutig (erwartet: keine solche Kante [M], im Code
  gezaehlt).
- **V-B (Kontrollarm Hubfolge):** umgekehrte Reihenfolge H_3, ..., r_0, Hoehen j/10.
- **S-A (Kontrollarm Fuellung):** r_0..r_3, C1, C2, Hoehen j/6.
- **tau = 1** fuer alle Arme (wie B1-t1 in REGIME-K-1; Hub = kubische Kante). Zellvolumen V_c = tau det(AV) = 1/4
  (V, S), 1 (B1, KW).
- Zaehlung je Zelle [M]: V: 2 x 68 + 10 = 146 Kanten, 232 4-Simplizes, 40 Eichfreiheiten; S: 86, 136, 24.
- Flachheit, Pseudomannigfaltigkeit, Volumensumme, Schlaefli, tote Kanten: rk.Gitter.kontrollen (unveraendert).

### 2.3 Arme

| Arm | Netz | Zweck |
|---|---|---|
| KW | Kuhn, tau = 1 | Pipeline (PK, PK-V) und RQ0 (a) |
| B1-t1 | B1 ohne Fuellung, tau = 1 | RQ0 (b); Vorzeichen und echte Zeit beschreibend |
| V-A | gefuelltes V, Hubfolge A | RQ1 bis RQ4 (Hauptarm) |
| V-B | V, Hubfolge umgekehrt | Kontrollarm, beschreibend |
| S-A | S (Achse C1-C2), Hubfolge A | Kontrollarm "zweite Diagonalwahl", beschreibend |

## 3. Euklidisch (wie REGIME-K-1, Code rk.py unveraendert)

- H(k) = Bloch-Hesse von S = Summe A_t eps_t (rk.Gitter.H), Eichabbildung G(k), Nullmoden (|lambda| <= 1e-12 max),
  Eichabzug im Komplement des numerischen Nullraums, Metrikabbildung mit Kantenmitten, transversale Basis (Spalte 0
  Spur), Schur-Form M6, "gerade" = Re M6 (Hauptgroesse), "voll" = M6, "affin" beschreibend; Normierung lambda/(|k|^2 V_c);
  konformer Modus = groesstes Spur-Gewicht (rk.analyse, unveraendert).
- 92 Richtungen in 4D (rk.richtungen, Saat 20261005; 25 raeumlich), kl-Raster 0,005 bis 0,2 mit l = mittlere
  Kantenlaenge der Kantenklassen, Extrapolation w0 + w2 x^2 + w4 x^4 ueber kl in {0,005; 0,01; 0,02; 0,05; 0,1}
  ("voll": kubisch), TT-Spanne = max|w|/min|w| - 1 (nur bei einheitlichem Vorzeichen), Exponent p ueber 0,05 bis 0,2
  (rk.kennzahlen, rk.w0_fit unveraendert).
- Neu nur: konform/TT **je Richtung** r(d) = c0(d) / Mittel_j w0(d, j) (extrapoliert), dazu der Gesamtwert wie
  REGIME-K-1 (Mittel c0 / Mittel w0).

## 4. Vorzeichenzaehlung (wie REGGE-4D-1 und REGGE-4D-SCHIEF-1) [F]

- Gezaehlt in H_E = -H (H = Hesse von S wie in rk.py). H_E hat das Vorzeichen der euklidischen Einstein-Wirkung:
  TT positiv, konform negativ (REGGE-4D-1 [P]).
- Je k: Eigenwerte von H_E(k) (hermitesch symmetrisiert); null: |lambda| <= 1e-12 max|lambda|; positiv/negativ sonst.
  Dazu Rang G(k) (Singulaerwerte > 1e-10 s_max) und kleinster Nicht-Null-Betrag relativ.
- **Punkte:** (i) Brillouin-Zone 8^4: k = 2 pi A^-T m / 8, m in {0..7}^4 (4096 Punkte, davon q = 0 einer);
  (ii) alle 92 x 9 = 828 Punkte des euklidischen Rasters.
- Fuer die 828 Punkte zusaetzlich: Vorzeichen der Schur-Werte (TT und konform) aus rk.analyse.

## 5. Echte Zeit ueber komplexes k_tau (Verfahren REGGE-WELLE-1, auf rk.Gitter uebertragen) [M, F]

- **Laurent-Form [M]:** H(k)_ee' = Summe_sigma Summe_ij H^sigma_ij exp(-i k.T_i) exp(i k.T_j) ist analytisch in k
  (fuer reelles k gleich rk.Gitter.H). Die Zeitanteile der Zellversaetze sind 0 oder tau, also
  H = Summe_{m=-1..1} C_m(k_s) z^m mit z = exp(i k_tau tau). Mit k_tau = i omega: z = exp(-omega tau).
- **Nullbasis N(k):** rk.Gitter.G(k) (analytisch, 4 NV Spalten) plus Einheitsvektoren toter Kanten.
- **Komplement [F]:** Q0(k_s) = orthonormales Komplement von range N(0, k_s) (komplex, fest in omega);
  F(omega) = Q0^H H(i omega, k_s) Q0, analytisch in omega.
- **Nullstellen:** alle Wurzeln von det F per Polynom-Eigenwertproblem in z (Begleitmatrix, scipy.linalg.eig wie
  REGGE-WELLE-1; Koeffizienten unter 1e-10 relativ weggelassen und berichtet), omega = -log(z)/tau (Hauptzweig);
  Verfeinerung der Kandidaten in R' (R um 20 % vergroessert) per Aberth auf det F.
- **Bereich R** = {0 < Re omega <= 3 abs(k), abs(Im omega) <= 0,5 abs(k)} (REGGE-WELLE-1 [F4]); Windungszahl von det F
  laengs des Randes (2 x 1000 + 2 x 200 Punkte, Verdopplung bis x4 bei Phasenspruengen >= 0,5 rad).
- **Je Nullstelle in R:** v = Re omega/abs(k), Im omega/abs(k), Pruefwert s = sigma_min/sigma_max von F,
  rho = sigma_min(Qn0^H Qn(omega)) (Regularitaet des Komplements), Physikalitaet = Abstand des Kernvektors von range
  N(omega) relativ, TT-Anteil der Klasse u + range N (eichinvariant wie REGGE-WELLE-1, Kontinuums-TT-Moden h_+, h_x
  ueber P(k)) beschreibend.
- **Kontrollen W0 (je Arm):** (a) Laurent-Form bei reellem k gegen rk.Gitter.H, 64 Zufallspunkte, <= 1e-12 relativ;
  (b) Nullvektoren bei komplexem k_tau: max |H N| / (|H|_2 |N|) <= 1e-10 an 64 Zufallspunkten (k_tau = a + i b,
  a in [-pi, pi], b in [-2,4; 2,4]).
- **Richtungen [F]:** "rw24" = die 24 raeumlichen Richtungen aus REGGE-WELLE-1 (12 feste, 12 Fibonacci); "rk25" = die
  25 raeumlichen Richtungen der 92 (rk.richtungen). Fuer V-A, V-B, S-A, B1-t1 beide (49 Eintraege, einige doppelt), fuer
  KW rw24.
- **Betraege [F]:** Hauptlesart abs(k) = 0,05 in Koordinaten (kubische Kante 1; beim Kuhn-Gitter = Gitterabstand wie
  REGGE-WELLE-1). Nebenlesart kl = 0,05 (l = mittlere Kantenlaenge, wie REGIME-K-1), also abs(k) = 0,05/l.
  Beschreibend: abs(k) = 0,1 und 0,2 (rw24).
- **Echtheitspruefung (nach Rauchtest r1 ergaenzt, Abschnitt 10):** s_voll = (r+1)-kleinster Singulaerwert der vollen
  H(k_s, i omega) relativ zum groessten, r = Rang der Nullbasis (Eichung + tote Kanten). Komplementfrei: Eine echte
  Nullstelle hat s_voll ~ 0; eine Scheinnullstelle des festen Komplements nicht. Schwelle "echt": s_voll <= 1e-8.
- **Zensus light (beschreibend):** alle PEP-Wurzeln mit 0 < Re omega <= 2,4 ausserhalb R: Zahl, und davon die mit
  s <= 1e-9 und s_voll <= 1e-8 ("intrinsisch") und abs(Im omega) > 1e-6 abs(k); das alte Kriterium (s, rho,
  Physikalitaet) wird mitgezaehlt. Keine Aberth-Verfeinerung; geht in kein Urteil ein.

## 6. Urteilsregeln (mechanisch in code/rk2.py, Modus auswertung)

- **Pipeline-Kontrollen** (aus Projektbefunden; gehen nur ueber die Sperren unten in Urteile ein):
  - PK (KW euklidisch, wie REGIME-K-1): s0 (gerade) < 1e-6, Mittel w0 auf 1e-3 gleich -1/4, |konform/TT + 2| <= 2e-3.
  - PK-V (KW Vorzeichen, REGGE-4D-1 [P]): bei q = 0 genau 11 null, 4 positiv, 0 negativ; an allen 4095 q != 0 genau
    5 null, 9 positiv, 1 negativ.
  - W0 (a) und (b) fuer KW und V-A.
- **RQ0** ("Der Code gibt auf dem Kuhn-Gitter REGGE-WELLE-1 wieder (v bei |k| = 0,05 zwischen 0,9997 und 0,9999; zwei
  laufende Moden) und auf der B1-Kopie ohne Fuellung REGIME-K-1 (TT-Spanne extrapoliert < 1e-8)"):
  - (a) KW, abs(k) = 0,05, alle 24 Richtungen rw24: Windungszahl in R = 2, genau 2 verfeinerte Nullstellen in R, beide
    laufend (abs(Im omega) <= 1e-6 abs(k)) und mit v in [0,9997; 0,9999]; kein Punkt gesperrt (Sperren wie bei RQ4).
  - (b) B1-t1: s0 (gerade, 92 Richtungen) < 1e-8.
  - Nach Plan: eingetroffen genau dann, wenn (a) und (b). Nach Kartenwortlaut: wie Plan, aber (b) mit gerade **und**
    voll < 1e-8; gehen gerade und voll auseinander, "unklar".
- **RQ1** ("Gefuelltes V mal Zeit, euklidisch: Die extrapolierte TT-Spanne ueber mindestens 50 Richtungen liegt unter
  1e-6, und konform/TT = -2 auf 1e-4"), V-A, 92 Richtungen:
  - Nach Plan: eingetroffen genau dann, wenn s0 (gerade) < 1e-6 **und** max_d |r(d) + 2| <= 1e-4 (r(d) je Richtung,
    Abschnitt 3; absolute Toleranz, also auch relativ erfuellt).
  - Nach Kartenwortlaut: dasselbe mit gerade und voll; beide ja -> eingetroffen, beide nein -> nicht eingetroffen, sonst
    unklar.
  - Faellt PK oder RQ0 (b) nach Plan: "unklar (Pipeline)", Werte trotzdem berichtet.
- **RQ2** ("genau 4 Nullmoden je Ecke der Grundzelle an jedem k ungleich 0 (keine tote Kante)"), V-A: eingetroffen genau
  dann, wenn
  - an allen 828 Rasterpunkten: genau 40 Nullmoden, Luecke >= 1e3, Rang G = 40, ||H G|| rel <= 1e-12, Sinus
    Nullraum/Eichraum <= 1e-6;
  - an allen 4095 BZ-Punkten q != 0: genau 40 Nullmoden und Rang G = 40;
  - Liste toter Kanten leer.
  - Nach Plan = nach Kartenwortlaut.
- **RQ3** ("keine Gittermode mit negativer Steifigkeit ausser der konformen Richtung (Vorzeichenzaehlung wie
  REGGE-4D-SCHIEF-1)"), V-A: eingetroffen genau dann, wenn
  - an allen 828 Rasterpunkten und allen 4095 BZ-Punkten q != 0 genau **ein** negativer Eigenwert von H_E;
  - bei q = 0 **kein** negativer;
  - an allen 828 Rasterpunkten die fuenf TT-Werte positiv und der konforme Wert negativ in H_E (Schur-Form "gerade";
    damit ist der eine negative die konforme Richtung).
  - Nach Plan = nach Kartenwortlaut. Faellt PK-V: "unklar (Pipeline)".
- **RQ4** ("In echter Zeit (komplexes k_tau wie REGGE-WELLE-1): bei |k| = 0,05 in allen gerechneten Richtungen genau zwei
  laufende Moden mit v zwischen 0,999 und 1,001"), V-A, 49 Richtungen (rw24 + rk25):
  - Je Punkt **gesperrt** (REGGE-WELLE-1 [F7]), wenn: Windungszahl mehr als 0,05 von einer ganzen Zahl oder
    Phasensprung >= 0,5 rad auch bei vierfacher Dichte; Windungszahl != Zahl der verfeinerten Nullstellen in R; eine
    Nullstelle in R mit s > 1e-9, rho < 0,05 oder Physikalitaet < 0,1; min rho auf dem Rand von R < 0,05; dazu (nach r1)
    eine Nullstelle in R mit s_voll > 1e-8 (Scheinnullstelle, "unecht").
  - Je Punkt **erfuellt**, wenn genau 2 Nullstellen in R (Windung 2), beide abs(Im omega) <= 1e-6 abs(k) und
    v in [0,999; 1,001].
  - Dreiwertig: ein ungesperrter Punkt verfehlt -> nicht eingetroffen; sonst ein gesperrter Punkt -> nicht auswertbar;
    sonst eingetroffen.
  - Nach Plan: Hauptlesart (abs(k) = 0,05 in Koordinaten). Nach Kartenwortlaut: Haupt- und Nebenlesart (kl = 0,05)
    gleich -> dieses Urteil; verschieden -> unklar.
  - Faellt RQ0 (a) oder W0 auf V-A: "unklar (Pipeline)".

## 7. Kontrollen (technisch)

- rk.Gitter.kontrollen je Arm: Fehlwinkel, jedes Tetraeder zweimal, Summe |Vol| = V_c, Simplizes verschieden,
  Schlaefli, Symmetrie von M^sigma, tote Kanten; Hermitezitaet von H(k); k = 0 (erwartet V: 10 + 4 x 9 = 46 Nullmoden,
  S: 10 + 20 = 30 [M]); Superzelle 2 x 2 x 2 x 2 gegen 16 Bloch-Spektren (rk.lauf_gitter, unveraendert).
- Netzaufbau V und S: Zahl der Tetraeder je Art, Kanten je Zelle, Kanten innerhalb eines Untergitters (erwartet 0),
  Euler-Charakteristik der Raumzelle.
- KW gegen REGGE-WELLE-1-Wuerfelgitter-Formel (beschreibend): v_hk = 2 asinh(sqrt(Summe sin^2(abs(k) n_i/2)))/abs(k).

## 8. Laeufe auf der .69

- Ordner /home/fmh/fmhc-physics-remote/regime-k-2/ (code/, rauch/, lauf/). Aufruf ueber
  /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu2, cpu3, cpu4; je Lauf <= 600 s, 1 Thread, 4 GB.
- Code: code/rk2.py (neu), dazu unveraendert kopiert: rk.py, pt.py (regime-k-1/code), ew.py, tp.py (tt-iso-1/code).
- Modi: gitter (euklidisch, rk.lauf_gitter), vorzeichen (BZ 8^4 und 828 Punkte), welle (echte Zeit), auswertung.
- Hauptlaeufe (nach den Rauchtests festgelegt, Laufzeit V-Welle ~12 s je Punkt):
  - cpu2: gitter KW, B1-t1 (mit KP), V-A, V-B, S-A; vorzeichen KW, V-A, B1-t1, V-B, S-A; welle KW (0,05, rw24, geurteilt
    RQ0 a) und B1-t1 (0,05, rw24, beschreibend).
  - cpu3: welle V-A 0,05 Koordinaten rw24; V-A kl = 0,05 rw24; V-A 0,2 rw24 (beschreibend).
  - cpu4: welle V-A 0,05 Koordinaten rk25; V-A kl = 0,05 rk25; S-A 0,05 rw24; V-B 0,05 rw24 (beide beschreibend).
  - Die Auswertung fuegt rw24- und rk25-Dateien derselben Lesart zusammen (49 Punkte).
  - Zusatzlaeufe (beschreibend) nur, wenn Zeit bleibt; sie gehen in kein Urteil ein.
- Rauchtests (je <= 120 s): nur Laufzeit, Rueckgabewert, Schluessel und Netzaufbau (Zaehlungen, Volumensumme,
  Schlaefli, Superzelle, Hermitezitaet, W0). Fuer KW darf alles ausser abs(k) = 0,05 gelesen werden; KW-Welle im
  Rauchtest nur bei abs(k) = 0,3 und 0,6 (Vergleich mit REGGE-WELLE-1-Rauchwerten und der Wuerfelgitter-Formel).
  **Nicht gelesen:** fuer B1, V, S keine Nullmoden, tote Kanten, Vorzeichen, Spektren, TT-Werte, Wellenwurzeln, Urteile.
- Danach PLAN.md und code/ als *.eingefroren-<zeit> kopieren, sha256 in EINGEFROREN-SHA256.txt (lokal und .69).

## 9. Agenten-Vorhersagen (vorab, gehen in kein Urteil ein)

| Nr | Vorhersage |
|---|---|
| A1 | RQ0 eingetroffen (90 %) |
| A2 | RQ1 nach Plan eingetroffen, TT-Mittel -1/4 je k^2 V_c auf 1e-6 (70 %) |
| A3 | RQ2 eingetroffen: keine tote Kante, 40 Nullmoden ueberall, 46 bei k = 0 (70 %) |
| A4 | RQ3 nicht eingetroffen: V hat mindestens eine Gittermode mit negativer Steifigkeit (nicht Delaunay, stumpfe Winkel) (55 %) |
| A5 | RQ4 eingetroffen (55 %); falls A4 eintrifft, liegt trotzdem keine Zusatzwurzel in R (60 %) |
| A6 | V-B und S-A: s0 (gerade) < 1e-6 wie V-A (75 %) |

## 10. Rauchtests (vor dem Einfrieren; alle rc = 0, Zeiten der .69 in UTC)

- **r1** (11:03:44 bis 11:03:46 UTC, cpu2, rk2.py a639bee9...): KW gitter, vorzeichen (BZ 2^4), welle bei abs(k) = 0,3
  und 0,6 (x+, xyz+, fib05). Alles gelesen (KW, keine Kartenvorhersage bei diesen Betraegen):
  - Welle: je Punkt Windung 2,000 und 2 Nullstellen in R, v (x+) = 0,9925830 / 0,9712652 (0,3 / 0,6), (1,1,1) 0,9950517 /
    0,9807939, fib05 0,9941320 / 0,9772447; REGGE-WELLE-1-Rauchwerte 0,99258 / 0,97127, 0,99505 / 0,98079, 0,99413 /
    0,97724 [P]; Wuerfelgitter-Formel auf <= 1e-14 gleich. abs(Im omega)/abs(k) <= 2e-14, TT-Anteil >= 0,9997, W0 (a)
    5,6e-16, (b) 8,4e-16, tote Kante = Hyperdiagonale.
  - Vorzeichen: q = 0 11/4/0, alle 15 q != 0 5/9/1, Raster 5/9/1 (wie REGGE-4D-1 [P]). Gitter: flach 1,8e-15, k = 0 11
    Nullmoden, TT -0,24999 bei kl = 0,1 in a_x.
  - **Befund mit Folge:** Der Zensus light zaehlte nach dem alten Kriterium (s, rho, Physikalitaet) 2 bis 3 Wurzeln
    ausserhalb R als "intrinsisch". Das widerspricht REGGE-WELLE-SCHIEF-1 (Kuhn: genau 2 intrinsische [P]). Ursache [M]:
    F = Q0^H H Q0 wird auch singulaer, wenn H u (nicht u) in den Eichraum bei k_tau = 0 faellt; rho und Physikalitaet
    pruefen nur die rechte Seite. **Aenderung vor dem Einfrieren:** komplementfreie Echtheitspruefung s_voll (Abschnitt 5)
    als zusaetzliche Sperre "unecht" (RQ4, RQ0 a) und als Zensus-Kriterium. Keine Schwelle und keine Regel gelockert.
- **r2** (11:05:37 bis 11:05:38 UTC, cpu2, rk2.py b05845a9...): KW welle wie r1 mit s_voll. Lichtkegelpaar s_voll
  ~1e-16 (echt); alle Wurzeln ausserhalb R s_voll >= 9e-4 (unecht); Zensus: 0 weitere intrinsische (wie
  REGGE-WELLE-SCHIEF-1).
- **r3** (11:05:58 bis 11:06:38 UTC, cpu2 bis cpu4, rk2.py b05845a9...): B1-t1 (gitter mit KP, vorzeichen, welle 0,3),
  V-A (gitter, vorzeichen, welle 0,3), V-B (gitter), S-A (gitter, welle 0,3). **Gelesen nur:** Laufzeiten, rc, Zaehlungen
  und Netzaufbau: V: 68 Kanten, 116 Dreiecke, 58 Tetraeder je Zelle (Arten 1/1/4/24/4/24), Euler 0, keine Kante im
  Untergitter; 4D: 146 Kanten, 232 Simplizes, jedes Tetraeder zweimal, Summe |Vol| exakt, kleinstes Volumen 0,0051
  l^4, Schlaefli 8,0e-16, M symmetrisch 1,8e-15, Superzelle (2,1,1,2) 4,5e-15, Hermitezitaet 6,7e-16, W0 (a) 3,6e-16,
  (b) 1,9e-16; V-B dieselben Zaehlungen; S: 40 / 68 / 34, 4D 86 Kanten, 136 Simplizes; B1 wie REGIME-K-1 (KP 2304 von
  2592, 1300 von 1300). Welle V-A ~12 s je Punkt, S-A ~3 s, B1 ~1,2 s; Aberth erreichte bei V-A 2 von 3 Punkten die
  Grenze 80 (Doppelwurzel). **Nicht gelesen:** Fehlwinkel, tote Kanten, Nullmoden, k = 0, Vorzeichen, Spektren,
  TT-Werte, Wurzeln, Windungen (B1, V, S).
- **r4** (11:08:10 bis 11:08:11 UTC, cpu2, rk2.py eb361e43...): Probe der Auswertung auf den Rauchdateien (V-A-Welle
  bei 0,3 fuer beide Lesarten eingesetzt). Gelesen nur: rc, Schluessel der Ausgabe und welche Urteile ein Feld
  "plan_vor_PK" tragen (RQ3, RQ4: ja, erwartet, weil PK-V nur 15 BZ-Punkte und die KW-Welle 0,3/0,6 hat; RQ1: nein).
  Das letzte verraet, dass PK und RQ0 (b) auf 6 Richtungen der Rauchdaten bestanden waeren (Selbstanzeige).
- Einzige Codeaenderungen nach r1: s_voll (Sperre, Zensus), Zusammenfuehren der rw24-/rk25-Dateien in der Auswertung.
