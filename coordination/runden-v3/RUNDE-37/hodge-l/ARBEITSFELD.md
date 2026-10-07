# HODGE-L: Arbeitsfeld (feldforscher, eine Datei fuer alle Zwischenstaende)

- Start 2026-10-05 06:02:48 CEST (date). Zeitbox 60 min, also bis 07:02:48 CEST.
- Karte gelesen (KARTE.md, bindend, HO1 bis HO4 unveraendert).
- Gelesen vor dem ersten Abruf: materie-netz-1/ERGEBNIS.md (ganz, Abschn. 5, Selbstanzeige 10), licht-finn-netz-1/PLAN.md
  (Hodge-Stelle Z. 49), tt-iso-1/ERGEBNIS.md (ganz, Abschn. 1 und 7), torsion-steif-1/ERGEBNIS.md (Abschn. 1 und 6),
  umklapp-1/KARTE.md, pumpe-netz-1/KARTE.md (nur lesen).
- Regeln: hoechstens 10 Abrufe, keine Websuche; Erwartung mit date-Zeit vor jedem Abruf; gestrichenes bleibt stehen
  (~~so~~); offene Fragen wandern sichtbar mit.

## Projektsuche (06:03 bis 06:04, grep mit allen Ausschluessen)

- "Hodge" in 508 Dateien, davon viele Hodge-Vermutung (Millennium) oder Scout-Cache. Gezielt:
  - Hodge-Zerlegung / Hodge-Stern: INDUZIERT-DIRAC-2D, INDUZIERT-WILSON-2D (2D, Code dirac2d.py) [P]
  - Hodge-Gewicht / Hodge-Form: MATERIE-NETZ-1 (mn.py), LICHT-FINN-NETZ-1 PLAN, PUMPE-NETZ-1 KARTE, RUNDE-46.md [P]
  - **Rippa: schon im Projekt** (KOVARIANZ-2D-GEGENPROBE, KOVARIANZ-EPS-1, INDUZIERT-DICHTE-2D/gegenlesen,
    RUNDE-46.md). Muss ich lesen, bevor ich Rippa "neu" nenne.
  - Christiansen: TORSION-STEIF-1 (Quelle 2312.11709 lokal als Text!), REGGE-TORSION-L DOSSIER, RUNDE-44/45.md
  - "well-centered": 0; "gut zentriert": nur diese Karte; "HodgeRank": nur diese Karte;
    "discrete exterior calculus": nur ein Scout-XML; "finite element exterior": 2312.11709 und Scout-Cache.
  - Scout-Cache (research-scout-claude-20260913/http-cache) enthaelt "Hodge Laplac" / "Hodge-Laplace" in ~30 Dateien:
    pruefen, ob dort 24-Monats-Arbeiten stehen (spart Abrufe).

## Offene Rueckfragen (wandern mit)

- R1: Was sagen die Rippa-Stellen im Projekt (Kovarianz-Karten)? -> lesen
- R2: Steht in 2312.11709 etwas ueber Christiansen 2011 (Regge = FEEC) und ueber Exaktheit des Regge-Komplexes? -> lokal lesen
- R3: Betti-Zahlen von Netz V auf dem 3-Torus: Zellzahlen je Zelle aus dem Projekt (Euler-Charakteristik = 0 als Probe)

## Lokale Funde vor den Abrufen (06:05 bis 06:11, kein Abruf)

- **Christiansen/Hu/Lin 2023 lokal** (torsion-steif-1/quellen/B2-2312.11709v1.txt) [S Einleitung, S. 1 und 3; Satz 5.1]:
  - "Christiansen [11] interpreted Regge calculus as a finite element scheme ... and extended the Regge space to a
    discrete version of the elasticity complex (Regge complex)." [11] = Numer. Math. 119 (2011).
  - "Although Regge calculus/finite elements have drawn significant attention, its cohomology remains an open question"
    (S. 3). Satz 5.1: Kohomologie des Regge-Komplexes (3D) = de Rham tensor RM.
  - **Erwartungsverstoss zu HO3 (Teil):** Die Exaktheit (Kohomologie) war 2011 nicht gezeigt, erst 2023. HO3 sagt
    "Christiansen zeigt ... mit exaktem Komplex". -> Urteil HO3 "teilweise".
- **INDUZIERT-DIRAC-2D [P]:** Kaehler-Dirac mit umkreisbasiertem Hodge-Stern auf 2D-Zufallsnetz (Koordinaten-Delaunay,
  physikalisch nicht Delaunay): c_eff = +48 statt -4; dualer Teil Delta_2 mit Leitwerten 1/w_e, ~1 400 (k eps)^2 Kanten
  mit w_e < 0 je Netz. "Ein Lauf mit intrinsischem Delaunay oder positiven Hodge-Sternen fehlt." -> Stelle 3 ist im
  Projekt in 2D schon getroffen worden, ohne den Namen.
- **Rippa im Projekt [P, L]:** KOVARIANZ-2D-GEGENPROBE, KOVARIANZ-EPS-1 ("Delaunay ist in 2D energieminimal (Rippa), in
  4D nicht [L]"), INDUZIERT-DICHTE-2D-Gegenlesen. Nie an der Quelle gelesen.
- **EINE-WELT-LOCH-1 PLAN 1.2 [P]:** V je Zelle 10 Ecken, 68 Kanten, 116 Dreiecke, 58 Tetraeder (Euler 0);
  S 6/40/68/34; "Beide sind Triangulierungen des Raums" -> Betti (1,3,3,1) auf dem 3-Torus [M].
  Ohne Fuellung: zwei Kopien, Regge-Zellen = Tetraeder-Oktaeder-Wabe (nicht simplizial).
- **Eigene Ueberlegung [ES, M] zu Stelle 4 (vor Abruf festgehalten):**
  - Erste Klasse der Skalarregel heisst A c_v in Bild M (TT-ISO-1 Abschn. 7). Kontinuum: c(N) = (dd - delta Lap) N,
    ADM-Kinetik pi.pi - (1/2) pi^2 gibt hdot = hess N = def(grad N), also reine Eichung, **nur** mit dem
    DeWitt-Spurkoeffizienten 1/2 (3D). Mit Spurkoeffizient lambda' != 1/2 bleibt (2 lambda' - 1) delta Lap N, nicht Eichung.
  - Folge [H]: Der "Spur"-Eichdefekt misst, ob die Kinetik A (= inverse Massenmatrix = Hodge-Stern auf dem Regge-Raum)
    das Diagramm hess = def o grad diskret vertauschen laesst. Das ist eine Vertraeglichkeit zwischen Hesse-Komplex und
    Elastizitaetskomplex ueber die Massenmatrix, keine fehlende Exaktheit des raeumlichen Komplexes (der ist nach
    CHL 2023 Satz 5.1 auf jeder Triangulierung exakt bis auf de Rham x RM).
- **Eigene Ueberlegung [M] zu Stelle 1/2 (LICHT-FINN-NETZ-1 Z. 49, "flache Nullmoden"):** Pyrochlor-Kanten mit nur
  Dreiecken: jede Kante und jedes Dreieck gehoert genau einem Tetraeder; Rang d1 = 3 je Tetraeder, also 6 je Zelle;
  Kern d1 = 12 - 6 = 6, Eichrang 4 bei k != 0, **2 flache Nullbaender**. b1 des 2-Komplexes = 2 L^3 + 1 (Euler 4 - 12 + 8 = 0,
  b2 = 2 L^3 Tetraederraender). Mit den 4 Sechsecken + Zellen: exakt, b1 = 3.
- **Eigene Ueberlegung [H] zu Takt und Hodge:** Glickenstein (konforme Variationen, 3D) [L?]: Die konforme Ableitung der
  Regge-Kruemmung ist ein diskreter Laplace mit Gewichten |e*|/|e| (Hodge-Stern *1). Dann waere der Takt-Operator
  P = -W^H B W von MATERIE-NETZ-1 ein Hodge-Laplace des Netzes; positiv, solange die dualen Gewichte positiv sind.
  Pruefen per Abruf.

## Abrufprotokoll (Erwartung vor Abruf, Ausgang danach)

### F1 (Erwartung geschrieben 06:11:31 CEST) arXiv-API: Hirani/Kalyanaraman/VanderZee "Delaunay Hodge star", VanderZee u. a. "well-centered", Glickenstein (Laplace/konform)

- **Erwartung:** HKV zeigen, dass auf (paarweise) Delaunay-Netzen die vorzeichenbehafteten umkreisbasierten dualen
  Volumina in **jeder** Dimension positiv sind (Randbedingung mild). Das widerspraeche HO1 (dort: in 3D nur gut
  zentriert). VanderZee u. a.: gut zentriert ist hinreichend, schwer zu erzeugen in 3D. Glickenstein: konforme Variation
  der Regge-Kruemmung = Laplace mit dualen Gewichten.
- **Ausgang F1 (06:12:15, Datei quellen/F1-api-...-20261005-061215.xml; erster Versuch per http leer, geloescht):**
  - HKV 2013 (1204.0747, CAD 45, 540-544) [S Abstract]: "for pairwise Delaunay triangulations with mild boundary
    assumptions these signed dual volumes are positive" (alle Dimensionen). **Erwartung getroffen, HO1 damit
    voraussichtlich verletzt** -- haengt an der Definition "pairwise Delaunay" (in 3D = Delaunay?). Volle Analyse: F2.
  - Doehrman/Glickenstein 2021 (2108.07308) [S Abstract]: Finite-Volumen-Laplace mit orthogonalen Dualen kann negative
    Volumina haben (Beispiel: 2D nicht Delaunay); "in many cases two- and three-dimensional Laplacians can be shown to be
    negative semidefinite with a kernel consisting of constants". **Neu (nicht erwartet):** negative Gewichte zerstoeren
    die Semidefinitheit nicht automatisch -> fuer den Takt-Operator wichtig.
  - Glickenstein 2011 (0906.1560, JDG 87) [S Abstract]: Ableitungen der Kruemmung unter konformer Variation "resemble
    the formulas for the change of scalar curvature under a conformal variation"; beschreibt die Variation von Regges
    Einstein-Hilbert-Funktional und dessen Konvexitaet. Gewichte (duale Flaechen) stehen nicht im Abstract -> [L?] bleibt.
  - VanderZee u. a. 2009 (0912.3097) [S Abstract]: in 3-well-centered (2-well-centered) Tetraedernetzen hat jede innere
    Ecke mindestens 7 (9) Kanten; unendlich viele Eckumgebungen verbieten Wohlzentriertheit in R^3.
    -> [M] Netz V: H-Ecke hat 6 H-Speichen + 2 C-H = 8 Kanten < 9: V ist nicht 2-well-centered. Direkt: C-H steht
    senkrecht auf dem Sechseck, Dreieck C-H-v rechtwinklig bei H; Umkugelmitte des Sechsecktetraeders liegt ausserhalb
    (Rechnung im Dossier). V ist also nicht gut zentriert; Positivitaet haengt an Delaunay.
  - VanderZee u. a. 2010 (0802.2108, SIAM J Sci Comput 31) [S Abstract]: Beziehungen zu Delaunay, Optimierungsverfahren.

### F2 (Erwartung geschrieben 06:13:11 CEST) arxiv.org PDF 1204.0747v4 (HKV, Volltext, Erwartungsverstoss-Zyklus)

- **Erwartung:** "pairwise Delaunay" = je zwei benachbarte n-Simplizes erfuellen die Leerkugel-Bedingung (lokal
  Delaunay), in 3D gleichwertig zu Delaunay fuer Triangulierungen ohne Rand; Satz: alle vorzeichenbehafteten dualen
  Volumina >= 0 (positiv bei Nicht-Entartung), in jeder Dimension. Rand: Umkreismitten der Randsimplizes innen.
- **Ausgang F2 (06:13:26, quellen/F2-1204.0747v4-20261005-061326.pdf, Text per pdftotext):** Erwartung getroffen, also
  **HO1 verletzt** (voller Zyklus, weil Erwartungsverstoss gegen die Karte):
  - [S Abschn. 1 und 5] "For planar triangle meshes and for tetrahedral meshes in three dimensions pairwise Delaunay is
    same as Delaunay."
  - [S Satz 5] innere Kante einer Delaunay-Tetraedertriangulierung: Dual ist konvexes Polygon mit positiver Flaeche;
    [S Satz 6] innere Ecke: duales Volumen positiv; [S Satz 3] Kodimension 1 positiv; [S Satz 7] mit "one-sided"
    Randsimplizes alle Dimensionen positiv (n = N = 3).
  - [S Abschn. 1] "completely well-centered meshes were sufficient but perhaps not necessary" -- gut zentriert ist nur
    hinreichend.
  - [S Lemma 2] verlangt "non-degenerate Delaunay pair": bei Kugel-Entartung (kospharische Punkte) ist die duale Laenge
    null, nicht negativ -> Eintrag 0, inverser Stern singulaer (Bezug INDUZIERT-DIRAC-2D, Leitwerte 1/w_e).
  - [S Abschn. 1] Galerkin-Hodge-Sterne (FEEC-Massenmatrizen) sind nicht diagonal; "Our results do not apply to that
    case directly" -> [L, M] Massenmatrizen aus Whitney-Formen sind als Gram-Matrizen auf jedem Netz positiv definit.
  - [S Anhang-Hinweis, v4] Korrigierte Abb. 1: DEC loest Poisson auch auf einem Netz mit nicht positivem *1 richtig
    ("It appears that DEC produces correct solution even for these cases").
  - **Korrigierte Erwartung:** In 3D reicht Delaunay (periodisch ohne Rand) fuer positive umkreisbasierte Hodge-Sterne
    aller Grade; gut zentriert ist nicht noetig. Finns V ist nicht gut zentriert (F1), Positivitaet haengt also an der
    Delaunay-Eigenschaft von V (nicht geprueft; Kandidat fuer Kartenvorschlag).

### F3 (Erwartung geschrieben 06:13:44 CEST) arXiv-API: Rippa in 3D, "harmonic triangulations" (Alexa), Dirichlet-Energie und Delaunay

- **Erwartung:** Alexa 2019 (ACM TOG, "Harmonic triangulations") [L?]: In 3D gibt es i. A. keine Triangulierung, die
  die Dirichlet-Energie fuer alle Funktionen minimiert (Gegenbeispiel); bistellare Fluesse (Pachner) aendern die Energie
  fuer alle Funktionen mit gleichem Vorzeichen. Falls nicht auf arXiv: andere Arbeiten, die "Rippa gilt in 2D, nicht in
  3D" sagen. HO2 trifft dann ein; neu waere der Teil "Vorzeichen des Flips unabhaengig vom Feld".
- **Ausgang F3 (06:14, quellen/F3-api-rippa-harmonic-*.xml, 7 Treffer):** Erwartung **nicht** getroffen, aber kein
  Widerspruch: Alexa "Harmonic triangulations" ist nicht auf arXiv (nicht gefunden). Gefunden:
  - Bobenko/Springborn 2007 (math/0503219, DCG 38) [S Abstract]: intrinsischer Delaunay-Laplace hat positive Gewichte;
    "Using Rippa's Theorem we show that ... Musin's harmonic index provides an optimality criterion for Delaunay
    triangulations" (Flaechen, 2D).
  - Lam 2022 (2203.03846) [S Abstract]: gewichtete Graphen auf dem Torus; die Dirichlet-Energie, minimiert ueber alle
    euklidischen Tori und Realisierungen, gibt genau dann Gewichte aus einer gewichteten Delaunay-Zerlegung (2D).
  - Dym/Lipman/Slutsky (1711.02221) [S Abstract]: H1-Konvergenz auch auf Nicht-Delaunay-Netzen (2D).
  - **Stand HO2:** 2D-Teil gestuetzt (Rippa im Abstract von Bobenko/Springborn genannt, Satz selbst nicht gelesen);
    3D-Teil nach Recherchestand nicht belegt (nur [L?] Alexa 2019). Pruefabruf auf Verlagsseite eingeplant (F6).

### F4 (Erwartung geschrieben 06:14:20 CEST) arXiv-API: Christiansen + Regge, Regge-FE der letzten Jahre (nach Datum)

- **Erwartung:** Christiansen 2011 ("On the linearization of Regge calculus") ist nicht oder als Preprint auf arXiv;
  juengere Treffer (Gawlik, Neunteufel, Hu, Lin, Li) zu Regge-Elementen und Kruemmung; in 24 Monaten nichts zu
  Eichdefekten bzw. zweiter Klasse auf Regge-FE.
- **Ausgang F4 (06:14:5x, quellen/F4-api-christiansen-regge-fe-*.xml, 24 Treffer, nach Datum):** zwei Verstoesse.
  - **Verstoss 1:** Christiansen 2011 steht auf arXiv (1106.4266) [S Abstract]: 3D-Regge linearisiert um die
    euklidische Metrik; quadratische Form explizit, bezogen auf curl^T curl (quadratischer Teil der
    Einstein-Hilbert-Wirkung, auch im Elastizitaetskomplex); Regge-Metriken in einer diskreten Fassung dieses Komplexes
    "equipped with densely defined and commuting interpolators"; Eigenpaare von curl^T curl konvergieren, gelesen als
    **nicht-konformes** FE-Verfahren. -> HO3: FE-Deutung ja, kommutierende Interpolatoren ja, Exaktheit (Kohomologie)
    nicht (laut CHL 2023 offen bis 2023). HO3 "teilweise".
  - **Verstoss 2 (24 Monate):** Christiansen/Lin, 14.03.2026, "Regge metrics with enhanced trace" (2603.13977)
    [S Abstract]: Varianten der Regge-Metriken, deren Spur **surjektiv** auf stetige FE-Funktionen abbildet, und
    Skalar mal Einheitstensor liegt wieder im Metrikraum; Anwendungen auf ART und konforme Geometrie "sketched".
    Das trifft den Spur-Sektor (Spur-Eichdefekt) direkt. Volle Analyse: F5.
  - Hu/Lin/Zhang 2023 (2311.15482) [S Abstract]: diskrete Hesse- und divdiv-Komplexe (BGG) in 2D/3D, Kohomologie wie
    im Kontinuum.
  - McDonald/Miller 2008 (0804.0279) [S Abstract]: Regge-Kalkuel mit Voronoi-Dual (umkreisbasiert): Skalarkruemmung an
    einer Ecke = gewichtetes Mittel der Fehlwinkel pro gewichtetes Mittel der dualen Flaechen. -> Die Eckregel des
    Projekts (Summe l_e eps_e) hat eine Hodge-Stern-Form.
  - Kein Treffer zu Eichdefekt / zweiter Klasse in der Regge-FE-Literatur (24 Monate und frueher, in dieser Abfrage).

### F5 (Erwartung geschrieben 06:15:05 CEST) arxiv.org PDF 2603.13977v1 (Christiansen/Lin 2026, Volltext)

- **Erwartung:** Abschnitt "Applications" skizziert ART: Lapse bzw. konformer Faktor als stetige Skalarfunktion, die
  mit Regge-Metriken vertraeglich sein muss (z. B. York-Zerlegung, Hamilton-Zwang oder lineare Elastizitaet mit
  Inkompressibilitaet). Keine Aussage zu Zwangsklassen (erste/zweite Klasse). Moeglicherweise: Standard-Regge-Spur
  ist nur stueckweise konstant und unstetig, was konforme Moden schlecht darstellt.
- **Ausgang F5 (06:15:20, quellen/F5-2603.13977v1-20261005-061520.pdf, Text per pdftotext): Erwartung uebertroffen,
  wichtigster Verstoss bisher.**
  - [S Abschn. 1, S. 2] "It appears that Regge metrics do not behave well with respect to such [conformal] scalings, for
    all applications. This can be interpreted similarly to locking phenomena ... in the incompressible limit." Grund:
    "the kernel of the linearized curvature operator on Regge elements consists of deformations of continuous P1 vector
    fields and imposing divergence freeness on the latter is problematic on general meshes." Und: bei Luo [32]
    (Combinatorial Yamabe flow, 2004) "the scaling is defined to take place at vertices (continuous P1), not at faces
    where the trace of Regge metrics lives a priori (discontinuous P0)."
  - [S Abschn. 1, Gl. 1.30 und Fussnote 1] S sigma = 2 mu sigma + lambda tr(sigma) I; "The case mu = 1/2 and lambda = -1
    is relevant to general relativity" (Eigenwerte 1 und -2, also die DeWitt-Form |h|^2 - (tr h)^2). "The stable
    invertibility seems not to hold when Sigma_h is the standard Regge element space." Numerisch (Arnold, persoenl.
    Mitteilung): die diskreten Eigenwerte von S auf Regge-Elementen "are spread out, including near 0". "Also the
    constraints would benefit from this property." "At this point it seems that a good finite element formulation of the
    initial value problem of GR is not available."
  - **Bezug [ES]:** Die Lagrange-Form A3 von TT-ISO-1 ist genau diese Form (V_t/V_F)(|h|^2 - (tr h)^2) auf stueckweise
    konstanten Metriken je Tetraeder. Die Skalarregel bzw. Eckskalierung w_v lebt an den Ecken (P1, wie Luo), die Spur der
    Kinetik je Tetraeder (P0). Das ist dieselbe Unvertraeglichkeit, die CL 2026 benennen. Kandidat-Erklaerung fuer
    (a) K_red fast singulaer bei A3R2 (TT-ISO-1 Selbstanzeige 5), (b) den O(1)-Spur-Eichdefekt auf V. [H], nicht gerechnet.
  - **Korrigierte Erwartung:** Es gibt Literatur, die die Spurstruktur diskreter Regge-Metriken mit der Stabilitaet von
    Kinetik und Zwaengen der ART verbindet (CL 2026), aber ohne Klassenanalyse (erste/zweite Klasse).

### F6 (Erwartung geschrieben 06:15:45 CEST) arXiv-API: Regge + Pseudo-Zwaenge / zweite Klasse / gebrochene Eichsymmetrie (nach Datum), dazu Alexa + Dirichlet

- **Erwartung:** Bahr/Dittrich 2009 ("Broken gauge symmetries and constraints in Regge calculus"): auf gekruemmten
  Loesungen keine exakte Eichsymmetrie, erste Klasse wird zu Pseudo-Zwaengen; um flache Hintergruende exakt. Dazu
  Dittrich/Hoehn (kanonische Pachner-Zuege). In 24 Monaten wenig (vielleicht Spinschaum/effektive Regge). Alexa nicht
  auf arXiv.
- **Ausgang F6 (06:16, quellen/F6-api-regge-zwaenge-*.xml, 40 Treffer nach Datum):** Erwartung getroffen (eine Zeile):
  Bahr/Dittrich 2009 (0905.1670), Dittrich/Hoehn 2010 (0912.1817: "For linearized Regge calculus on a flat background
  -- which exhibits exact gauge symmetries -- we derive local and first class constraints for arbitrary triangulated
  Cauchy surfaces"), Hoehn 2015 (1411.5672, PRD 91 124034), alle [S Abstract]; **im Projekt schon gelesen**
  (TAKT-UMBENENNUNG-L, GAMMA-NETZ-L, PACHNER-TAKT-1) [P]. In 24 Monaten kein Treffer zu Regge + zweite Klasse /
  Pseudo-Zwaenge / gebrochene Eichsymmetrie. Alexa nicht auf arXiv.
- **Projekt-grep 06:17 (alle Ausschluesse):** 2603.13977, "enhanced trace", 1106.4266, 2311.15482, Glickenstein stehen
  nirgends im Projekt ausser hier -> neu fuer das Projekt [P].

### F7 (Erwartung geschrieben 06:17:40 CEST) WebFetch dl.acm.org/doi/10.1145/3306346.3322986 (Alexa 2019, "Harmonic Triangulations", Abstract)

- **Erwartung:** Abstract sagt: Delaunay = harmonische Triangulierung in 2D (Rippa); in 3D existiert eine
  harmonische Triangulierung i. A. nicht (explizites Gegenbeispiel); bistellare Fluesse sind "harmonisch" (senken sie
  die Dirichlet-Energie fuer eine Funktion, dann fuer alle); lokal harmonische Triangulierungen lassen sich berechnen
  und reduzieren Splitter-Tetraeder. Risiko: Seite gesperrt (403), dann HO2-3D nur [L?].
- **Ausgang F7 (06:17:5x):** HTTP 403, nichts gelesen. Abruf verbraucht. HO2-3D bleibt [L?].

### F8 (Erwartung geschrieben 06:18:xx CEST, siehe date in abrufzeiten.txt) arXiv-API: "harmonic triangulation(s)", Dirichlet-Energie in 3D, Hodge-Stern + Delaunay/well-centered (nach Datum; deckt 24 Monate ab)

- **Erwartung:** Einige Arbeiten (2019-2026) zitieren Alexa: in 3D minimiert Delaunay die Dirichlet-Energie nicht
  allgemein; ein oder zwei juengere DEC-Arbeiten zu Hodge-Sternen auf Nicht-Delaunay-Netzen. Nichts, das HO1 (nach F2)
  wieder umdreht.
- **Ausgang F8 (06:18, quellen/F8-api-harmonic-3d-hodgestar-*.xml, 7 Treffer):** Erwartung nur teils getroffen.
  - Kein Abstract mit "harmonic triangulation(s)"; keine Quelle fuer Rippa in 3D. HO2-3D: nach Recherchestand nicht
    belegt (24 Monate abgedeckt: Treffer 2025-01 und 2025-05, beide ohne Aussage dazu).
  - Berbatov/Jivkov 2025 (2505.09443) [S Abstract]: "Discrete Exterior Calculus, which requires circumcentric duality
    and well-centred meshes" -> die Annahme von HO1 ist in juengerer Literatur noch verbreitet, obwohl HKV 2013 sie
    abraeumt (Kalibrierung: HO1 war "gewachsene Gewissheit").
  - Jacobson u. a. 2024 (2406.08647, Juni 2024, knapp ausserhalb 24 Monate) [S Abstract]: Wahl der Simplexmitten
    entscheidet ueber Stetigkeit in den Eckpositionen, positive Semidefinitheit der Dirichlet-Energie, Positivitaet der
    Massenmatrix, Unverzerrtheit auf regelmaessigen Gittern; lineare FE "exhibit bias on tetrahedralized regular grids".
  - Mohamed/Hirani/Samtaney 2018 (1802.04506) [S Abstract]: DEC konvergiert auf Nicht-Delaunay-Flaechennetzen mit
    vorzeichenbehaftetem diagonalem Hodge-Stern (numerisch, 2D-Flaechen).

### F9 (Erwartung geschrieben 06:19 CEST, date in abrufzeiten.txt) arxiv.org PDF 0906.1560 (Glickenstein 2011, Volltext)

- **Erwartung:** Satz fuer 3D: konforme Variation (Eckskalierung) der Kantenlaengen gibt fuer die Eck-Kruemmung
  K_v = Summe (1/2) l_e eps_e eine Ableitung = diskreter Laplace mit Gewichten (duale Flaeche der Kante)/(Kantenlaenge)
  plus Kruemmungsterme; auf flachem Netz nur der Laplace. Folge: Takt-Operator -W^H B W = Hodge-Laplace (*1). [H]
- **Ausgang F9 (06:18:5x, quellen/F9-0906.1560v1-*.pdf, Text per pdftotext): Erwartung getroffen** (eine Zeile, plus
  Belegstellen fuer das Dossier):
  - [S Satz 34, Gl. 31] 3D: dK_i/dt = -2 Summe_j (l*_ij/l_ij)(df_j/dt - df_i/dt) + Terme mit K_ij (Kanten-Fehlwinkel)
    und K_i. Flach: nur der Laplace mit Gewichten (duale Flaeche)/(Kantenlaenge) = *1.
  - [S Beweis Satz 24] zweite Variation von EHR in konformen Richtungen = Summe (2 l*/l - q K/l)(Differenzen)^2 + K-Terme.
  - [S Abschn. 6.2, S. 30-31] l*_ij > 0 fuer alle Kanten => Laplace negativ semidefinit mit Kern = Konstanten (Prop. 39(1));
    "In three dimensions, the property l*_ij >= 0 is not equivalent to a weighted Delaunay condition"; gut zentriert
    hinreichend. [S Satz 41] EHR konvex auf bestimmten Mengen (K_i >= 0).
  - Folge [M, H]: Fuer Eckskalierung (Mitten = Kantenmitten, also umkreisbasierte Duale) ist der Takt-Operator
    P = -W^H B W (mit B = -l deps/dl l, EINE-WELT-LOCH-1 1.3) bis auf Normierung der Hodge-Laplace d0^T *1 d0 des Netzes.
    Positiv an allen k, wenn alle l*_e > 0 (Delaunay genuegt, HKV Satz 5). Nicht gerechnet.

### F10 (Erwartung geschrieben 06:21 CEST, date in abrufzeiten.txt) arXiv-API: Lim (Hodge-Laplace auf Graphen), HodgeRank/kombinatorische Hodge-Theorie, DEC (Hirani/Desbrun), FEEC (Arnold/Falk/Winther)

- **Erwartung:** Lim 2015/2020 (SIAM Review 62): Hodge-Laplace auf Graphen und Komplexen, Zerlegung
  Gradient + Rotation + harmonisch, harmonischer Anteil = Kohomologie. Jiang/Lim/Yao/Ye 2011 (Math. Program.):
  HodgeRank, Ranking als Gradient, Inkonsistenz = Rotation + harmonisch. Hirani 2003 (Thesis, ggf. nicht auf arXiv),
  Desbrun/Hirani/Leok/Marsden 2005 (math/0508341): DEC mit umkreisbasiertem Dual. AFW 2006 (Acta Numerica) bzw. 2010
  (Bull. AMS): FEEC, Stabilitaet ueber kommutierende Projektionen und Kohomologie. Alles Bestaetigung.
- **Ausgang F10 (06:20:0x, quellen/F10-api-lim-hodgerank-dec-feec-*.xml, 22 Treffer): Erwartung getroffen** (eine Zeile):
  Lim 2015/2020 (1507.05379), Jiang/Lim/Yao/Ye (0811.1067), Desbrun/Hirani/Leok/Marsden 2005 (math/0508341), AFW 2010
  (0906.4325, Bull. AMS 47), alle [S Abstract]. Neu im 24-Monats-Fenster: 2505.08966 (Mai 2025) [S Abstract]: DEC
  konvergent und stabil fuer Hodge-Laplace **in 2D** auf nicht-entarteten Delaunay-Netzen (ueber FEEC); 3D nicht.
- **Abrufbudget erschoepft (10 von 10; F7 war 403).** Ab hier nur lokale Pruefungen.

## Gegensweep (06:20, vor dem Dossier): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. V ist eine echte Triangulierung des 3-Torus (sonst gelten Betti (1,3,3,1) und CHL-Exaktheit nicht). -> pruefen [P]
2. Die "Hodge-Gewichte" von MATERIE-NETZ-1 sind ein diagonaler Hodge-Stern (welche Duale?). -> pruefen im Code
3. B in MATERIE-NETZ-1 ist dasselbe B wie in EINE-WELT-LOCH-1 (B = -l deps/dl l); traegt die Glickenstein-Lesart. -> pruefen
4. Der Spur-Eichdefekt ist in der euklidischen Norm der Kantendehnungen definiert (QR von M), nicht in einer Hodge-
   bzw. Massennorm: Ja/Nein (erste Klasse) haengt nicht daran, die Zahlen 0,76 bis 0,99 schon. -> gelesen (TT-ISO-1 Abschn. 7)
5. Spin-Eis-Literatur (Henley 2010) zu Windungssektoren = harmonischer Anteil: nicht abgerufen, nur [L].

## Berichtigungen (geschrieben 2026-10-05 06:22:41 CEST; nichts oben geloescht)

- Zeitangaben in den Kopfzeilen bzw. Ausgaengen waren teils geschaetzt statt gemessen. Gemessen (quellen/abrufzeiten.txt,
  date direkt vor bzw. nach dem Abruf): F4 abgerufen 06:14:33 (oben "06:14:5x" ~~geschaetzt~~); F7 ohne eigene Messung,
  zwischen 06:17:53 und 06:18:08 (oben "06:17:5x"); F8-Erwartung 06:18:08 (oben "06:18:xx"); F9-Erwartung 06:18:45 und
  Abruf 06:18:46 (oben ~~06:19~~ bzw. ~~06:18:5x~~); F10-Erwartung 06:19:57 (oben ~~06:21~~), Ausgang gelesen 06:20:02
  (oben "06:20:0x"). Selbstanzeige im Dossier.
- Im Ausgang F3 steht "Pruefabruf ... eingeplant (F6)"; gemeint war F7.
- F7 steht nicht in abrufzeiten.txt (WebFetch, keine Datei). Nachgetragen dort.

## Gegensweep: Pruefergebnisse (lokal, ohne Abruf)

1. **V ist eine flache Triangulierung des 3-Torus [P, geprueft]:** EINE-WELT-LOCH-1 ERGEBNIS Z. 92: "Volumensumme je
   Zelle 0,25, Diedersumme je Kante 2 pi auf <= 1,8e-15 (flach)"; PLAN 1.2: Euler 10 - 68 + 116 - 58 = 0. Damit
   Betti (1,3,3,1) [M] und CHL-Satz 5.1 anwendbar.
2. **Hodge-Gewichte von MATERIE-NETZ-1 [P, geprueft]:** mn.py Z. 380-396: w_link = (3V/4)/b^2 ("|*e|/|e| mit |*e| =
   3 V_e/|e|, V_e = V/4"), u_ring = (3V/nringe)/Ar^2. Diagonaler Hodge-Stern mit **gleichmaessig verteilten**
   Volumenanteilen, weder umkreisbasiert noch Galerkin; positiv per Bau; nur fuer homogene Streckung gerechnet.
   -> Folge fuer Stelle 5 [M]: Bei TT-Verzerrung haengt die Spannungskopplung an der Wahl der Duale (siehe Dossier).
3. **B identisch [P, geprueft]:** mn.py Kopf Z. 13: "Fehlwinkel d_eps = -(B a)/l", also B a = -l d_eps, wie
   EINE-WELT-LOCH-1 1.3 (B = -l deps/dl l). Glickenstein-Lesart damit anwendbar, Normierung von W nicht geprueft.
4. **Defektnorm [P, gelesen]:** TT-ISO-1 Abschn. 7: P_M ueber QR von M (euklidisch). Ja/Nein unabhaengig, Betrag nicht.
5. Nicht geprueft: Henley-Spin-Eis-Literatur; ob V Delaunay ist (nur: nicht gut zentriert); Identitaet P1-FE-Gewichte =
   umkreisbasierte *1-Gewichte in 3D [L?].

## Nachtrag beim Gegenlesen des Dossiers (2026-10-05 06:31:21 CEST): V ist nicht Delaunay [M, von Hand]

- Anlass: Rueckwaertslesen der Teilprobe "Kegel/Sechsecktetraeder ungeprueft". Dabei fiel auf: Es gibt auch Paare
  Sechsecktetraeder/Sechsecktetraeder ueber die Flaeche (C, v, v'), wenn v v' eine Kante zwischen zwei Sechsecken
  desselben Lochs ist (EINE-WELT-LOCH-1 1.1: "Die 6 Kanten zwischen zwei Sechsecken sind Ab-Kanten").
- Koordinaten: regelmaessiger Stumpf-Tetraeder, Mitte C = 0, Ecken = Permutationen von (+-3, +-1, +-1) mit gerader
  Zahl von Minuszeichen (Kante 2 sqrt2). Sechseck a (Normale (1,1,-1)): Mitte H_a = (1,1,-1); Sechseck b (Normale
  (1,-1,1)): H_b = (1,-1,1); gemeinsame Kante v = (3,1,1), v' = (3,-1,-1).
- Tetraeder A = (C, H_a, v, v'): Umkugelmitte c_a = (11/6, -1/6, 1/6), Radius^2 = 123/36 (alle vier Abstaende
  nachgerechnet). Abstand^2 von c_a zu H_b = 75/36 < 123/36: **H_b liegt in der Umkugel von A.**
- Flaeche F = (C, v, v'), Normale (0,1,-1)/sqrt2: H_a und H_b auf verschiedenen Seiten; c_a liegt auf der Seite von H_b,
  c_b = (11/6, 1/6, -1/6) auf der Seite von H_a. Vorzeichenbehaftete duale Laenge von F nach HKV: -(2/3)/sqrt2 = -0,471
  (Kantenlaenge 2,83), also *2(F) < 0.
- Je Loch 6 solche Flaechen, 2 Loecher je Zelle: 12 von 116 Flaechen je Zelle (fuer T2 gespiegelt, gleiche Geometrie
  angenommen). Ein 2-3-Zug je Flaeche (neue Kante H_a-H_b; Mittelpunkt (1,0,0) liegt im Inneren von F, s = t = 1/6) ist
  moeglich; alle 12 zugleich erhalten die Fd-3m-Symmetrie [M].
- **Folgen:** HT1 des Kartenvorschlags ("V Delaunay", 60 %) ist von Hand verfehlt -> Karte umbauen. Fuer UMKLAPP-1:
  V ist nicht kugel-entartet, sondern verletzt Delaunay strikt an 12 Flaechen je Zelle; M-B wuerde dort klappen
  (Hinweis an die Leitung; in umklapp-1 nichts geschrieben). P > 0 an allen k (MATERIE-NETZ-1) ist damit kein
  Delaunay-Befund; entweder sind alle *1 > 0 (in 3D nicht gleichwertig zu Delaunay, Glickenstein 6.2) oder negative
  Gewichte werden ausgeglichen.

## Abschluss

- DOSSIER.md abgeschlossen 2026-10-05 06:33:07 CEST (date). Offene Rueckfragen R1 bis R3 vom Anfang: R1 (Rippa im Projekt) beantwortet: nur [L]; R2 (Christiansen in 2312.11709) beantwortet; R3 (Betti von V) beantwortet: (1,3,3,1), Euler 0 [P, M].
