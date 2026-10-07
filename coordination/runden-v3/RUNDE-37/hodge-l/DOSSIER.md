# HODGE-L: Dossier (feldforscher fuer die Leitung claude-primary, Runde 46, Finn-Auftrag "Review auch Hodge Theorie")

- **Zeiten (date):** Start 2026-10-05 06:02:48 CEST. Text dieses Dossiers ab 06:25:15 CEST. Zeitbox 60 min (bis 07:02:48).
- **Grundlage:** KARTE.md (bindend, HO1 bis HO4 unveraendert). Alle Zwischenstaende, Erwartungen vor jedem Abruf und
  Berichtigungen stehen in ARBEITSFELD.md. 10 Abrufe (F1 bis F10, F7 gab HTTP 403); Kopien in quellen/ mit Abrufzeit
  (quellen/abrufzeiten.txt).
- **Kennzeichen:** [S] an der Quelle gelesen (mit Abschnitt, Satz oder Gleichung), [S Abstract], [L] Gedaechtnis,
  [L?] unsicher, [M] eigene Mathematik (ungeprueft, kein zweiter Leser), [ES] eigener Schluss, [H] Hypothese,
  [P] Projektdatei.
- **Alles hier ist Literatur und Schreibtisch.** Keine Rechnung, keine Messdaten, keine Messdatenbestaetigung.

## 1. Ergebnis zuerst

1. **Hodge-Theorie ist fuer Finns Netz beides, je nach Groesse.** Der Moderator ist "topologisch gegen metrisch".
   - Zaehlgroessen (Betti-Zahlen, Eichnullen, Zahl der Photonen, flache Nullbaender, ker B = Bild M) benennt sie nur
     um. Dafuer stehen jetzt Saetze statt Numerik.
   - Metrische Groessen sagt sie voraus: Vorzeichen der Hodge-Sterne, Vertraeglichkeit der Bewegungsenergie mit der
     Spur, Kopplung der Materie an TT-Wellen. Dort laufen "Umbenennung" und "Werkzeug" messbar auseinander.
2. **HO1 ist verfehlt (wichtigster Erwartungsverstoss).** In 3D genuegt Delaunay fuer positive umkreisbasierte
   Hodge-Sterne aller Grade (Hirani/Kalyanaraman/VanderZee 2013, Saetze 5 bis 7). Gut zentriert ist nur hinreichend.
   - Finns gefuelltes Netz V ist **weder gut zentriert noch Delaunay** [M, von Hand, Abschn. 4.3]. An 12 von 116
     Flaechen je Zelle (Sechseck-Sechseck-Kanten der Loecher) liegt die Nachbar-Sechseckmitte in der Umkugel, und der
     umkreisbasierte Stern *2 ist dort negativ.
   - Fuer UMKLAPP-1 heisst das: V ist nicht kugel-entartet. M-B wuerde dort strikt klappen; 12 symmetrische 2-3-Zuege je
     Zelle erhalten Fd-3m.
3. **Stelle 4: Der Spur-Eichdefekt ist keine fehlende Exaktheit des raeumlichen Komplexes [ES].**
   - Der 3D-Regge-Komplex ist auf jeder Triangulierung exakt bis auf de Rham x RM (Christiansen/Hu/Lin 2023, Satz 5.1).
   - 4D-Regge, linear um flach, hat auf jeder triangulierten Cauchy-Flaeche Zwaenge erster Klasse (Dittrich/Hoehn 2010).
   - **Neu fuer das Projekt:** Christiansen/Lin (Maerz 2026) zeigen, dass Regge-Metriken schlecht zu Eckskalierungen
     passen. Die Spur lebt auf den Zellen (P0), die Skalierung an den Ecken (P1). Die ART-Form |h|^2 - (tr h)^2, also die
     A3-Form von TT-ISO-1, ist auf Standard-Regge-Elementen nicht stabil invertierbar. Woertlich: "Also the constraints
     would benefit". Das ist die naechste Literaturspur zum Defekt [H].
4. **Takt = Hodge-Laplace [H; Satz zitiert, nicht gerechnet].** Nach Glickenstein 2011 (Satz 34) ist die konforme
   Ableitung der Regge-Kruemmung auf flachem Netz ein Laplace mit den Gewichten l*/l, also mit *1.
   - Der positive Takt-Operator von MATERIE-NETZ-1 (MN2) waere dann eine DEC-Positivitaetsaussage.
   - Auf umgeklappten Netzen kann sie kippen (Bezug UMKLAPP-1).
5. **Stelle 5 [M]: Die statische Kopplung (Spur) merkt nicht, wie der Hodge-Stern gebaut ist, die TT-Kopplung schon.**
   - Mit den Gewichten von MATERIE-NETZ-1 (feste, gleichmaessige Volumenanteile; 4 Diamant-Richtungen) waere die
     Spannungskopplung an TT-Wellen stark richtungsabhaengig. Fuer "+" laengs der Wuerfelachsen ist sie null.
   - Geometrische Gewichte (P1-FE je Tetraeder) sind fuer affine Verzerrungen exakt.
   - Das ist ein Hinweis fuer PUMPE-NETZ-1. Dort habe ich nichts geschrieben.

## 2. Erwartungsverstoesse (das eigentliche Ergebnis; Reihenfolge nach Gewicht)

1. **HO1 (Karte, 70 %) verfehlt:** In 3D genuegt Delaunay.
   - "For planar triangle meshes and for tetrahedral meshes in three dimensions pairwise Delaunay is same as Delaunay"
     [S HKV 2013, Abschn. 1 und 5].
   - Positiv sind die Duale der Flaechen (Satz 3), der inneren Kanten (Satz 5: konvexes Polygon mit positiver
     Flaeche) und der inneren Ecken (Satz 6). Mit "one-sided" Randsimplizes gilt das in allen Dimensionen fuer
     n = N = 3 (Satz 7).
   - Gut zentriert war "sufficient but perhaps not necessary" [S Abschn. 1].
   - Kalibrierung: Die Annahme von HO1 steht noch 2025 in der Literatur: DEC "requires circumcentric duality and
     well-centred meshes" [S Abstract, Berbatov/Jivkov 2025]. HO1 war gewachsene Gewissheit, keine gepruefte.
1a. **V ist nicht Delaunay** [M, von Hand, kein Abruf, Arbeitsfeld 06:31]. Das hat meine eigene Vorab-Erwartung im
    Kartenentwurf verletzt (HT1 "V Delaunay", 60 %) und ebenso die Lesart der Leitung in UMKLAPP-1 ("regelmaessige
    Netze mit Kugel-Entartung").
    - Im Loch (Mitte C) teilen zwei Sechsecktetraeder (C, H_a, v, v') und (C, H_b, v, v') die Flaeche (C, v, v'), wenn
      v v' eine Sechseck-Sechseck-Kante ist.
    - Mit Lochkante 2 sqrt2 und C = 0: Umkugelmitte von A ist (11/6, -1/6, 1/6), Radius^2 = 123/36. H_b = (1, -1, 1)
      hat davon Abstand^2 75/36 und liegt also innen.
    - Die vorzeichenbehaftete duale Laenge von (C, v, v') ist -(2/3)/sqrt2. Es gibt 12 solche Flaechen je Zelle.
2. **Christiansen/Lin, 14.03.2026 (24-Monats-Fund, nicht auf der Karte):** Regge-Metriken und Spur.
   - Regge-Metriken "do not behave well with respect to such [conformal] scalings, for all applications" [S Abschn. 1,
     S. 2]. Bei Luo liegt die Skalierung "at vertices (continuous P1), not at faces where the trace of Regge metrics
     lives a priori (discontinuous P0)".
   - Die ART-Form S (mu = 1/2, lambda = -1) ist auf Standard-Regge-Elementen nicht stabil invertierbar. Ihre
     diskreten Eigenwerte sind "spread out, including near 0" (numerisch, Arnold, persoenliche Mitteilung, Fussnote 1).
     Woertlich: "Also the constraints would benefit from this property" [S Abschn. 1, um Gl. 1.30].
   - Varianten mit stetiger Spur ("enhanced trace") haben die kontinuierlichen Eigenwerte [S ebenda].
   - Ich hatte hoechstens eine Randbemerkung zur unstetigen Spur erwartet, keine direkte Aussage zu Kinetik und
     Zwaengen.
3. **HO3 (Karte, 70 %) nur teilweise:** Christiansen 2011 liest Regge als **nicht-konformes** FE-Verfahren.
   - Es steht in einem diskreten Elastizitaetskomplex mit kommutierenden Interpolatoren, und die Eigenpaare
     konvergieren [S Abstract 1106.4266].
   - Die Kohomologie (Exaktheit) des Regge-Komplexes war "an open question" bis Christiansen/Hu/Lin 2023 [S S. 3;
     Satz 5.1].
4. **Negative Gewichte zerstoeren die Semidefinitheit nicht automatisch.** Doehrman/Glickenstein 2021 [S Abstract]:
   Auch mit nicht positiven dualen Volumina sind 2D- und 3D-Laplace-Operatoren "in many cases" negativ semidefinit mit
   Kern = Konstanten. HKV v4 [S Hinweis zu Abb. 1]: DEC loest Poisson auch auf einem Netz mit nicht positivem *1
   richtig. Erwartet hatte ich "negativ heisst kaputt".
5. **Rippa in 3D: keine Quelle gefunden** (erwartet: Alexa 2019, "Harmonic triangulations"). Das ist kein
   Widerspruch. HO2 bleibt im 3D-Teil offen.

## 3. Urteile HO1 bis HO4

| Nr | Erwartung (Karte) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| HO1 | Umkreisbasierter DEC-Hodge-Stern in 3D nur auf gut zentrierten Netzen positiv; Delaunay allein genuegt nicht | 70 % | **verfehlt** | HKV 2013 (1204.0747v4) Saetze 3, 5, 6, 7 und Abschn. 1/5 [S]: Delaunay genuegt in 3D (mit mildem Randkriterium; periodisch ohne Rand). Einschraenkungen: Lemma 2 verlangt "non-degenerate"; bei kospharischen Punkten ist ein Eintrag null, nicht negativ. Glickenstein 2011, Abschn. 6.2 [S]: l*_ij >= 0 ist in 3D nicht gleichwertig zu (gewichtet) Delaunay. Delaunay ist also hinreichend, nicht notwendig. |
| HO2 | Rippa gilt in 2D, in 3D nicht allgemein | 65 % | **offen** (2D gestuetzt, 3D nach Recherchestand nicht belegt) | 2D: Bobenko/Springborn 2007 (math/0503219) [S Abstract] nutzen "Rippa's Theorem" fuer Delaunay-Optimalitaet; den Satz selbst habe ich nicht gelesen. 3D: Alexa 2019 [L?] nicht lesbar (ACM 403); arXiv-Suche F3/F8 inkl. 24 Monate ohne Treffer. Das Projekt sagt "in 4D nicht" ebenfalls nur aus dem Gedaechtnis (KOVARIANZ-EPS-1 [P, L]). |
| HO3 | Christiansen: linearisierter Regge-Kalkuel ist FEEC-Verfahren mit exaktem Komplex | 70 % | **teilweise eingetroffen** | Christiansen 2011 (1106.4266) [S Abstract]: 3D, linearisiert um die euklidische Metrik; quadratische Form = curl^T curl (quadratischer Teil von Einstein-Hilbert und Elastizitaetskomplex); diskreter Komplex mit kommutierenden Interpolatoren; Eigenpaare konvergieren; "non-conforming finite element method". Exaktheit: erst CHL 2023, Satz 5.1 [S, lokal]. Nur 3D und euklidisch, keine Zeit. |
| HO4 | [H] Eine Arbeit verbindet zweite Klasse bzw. gebrochene Eichsymmetrie im Regge-Kalkuel mit Diskretisierung bzw. Komplexen | 50 % | **eingetroffen**, aber im Kern schon im Projekt | Bahr/Dittrich 2009 (0905.1670) [S Abstract]: gebrochene Eichsymmetrie, Pseudo-Zwaenge, "consistent constraint algebra ... equivalent to ... an action with exact diffeomorphism symmetries". Dittrich/Hoehn 2010 (0912.1817) [S Abstract]: linear um flach erste Klasse "for arbitrary triangulated Cauchy surfaces". Beides steht schon in TAKT-UMBENENNUNG-L und GAMMA-NETZ-L [P]. Neu ist der Strang "Komplexe": Christiansen/Lin 2026 (Spur, Stabilitaet von S, Zwaenge) [S Abschn. 1], ohne Klassenanalyse. |

**Bedeutung nach der Karte:** HO1 bis HO3 treffen nicht alle ein. Die Lesart "Hodge-Theorie ist die Mathematik hinter
Finns Netz" bleibt richtig, mit zwei Aenderungen:

- Die Bedingung an den Glas-Zweig ist **Delaunay** (nicht "gut zentriert"). Zufalls-Delaunay-Netze (TT-GLAS-1)
  erfuellen sie per Bau.
- Finns regelmaessiges V erfuellt sie nicht: 12 negative *2-Eintraege je Zelle [M]. Fuer Licht mit umkreisbasierten
  Sternen auf V ist das ein Warnzeichen. Fuer den Takt nicht unbedingt, denn *1 > 0 ist in 3D schwaecher als Delaunay,
  und P > 0 ist gerechnet [P].
- "Regge ist FEEC" gilt als nicht-konformes FE; exakt erst mit CHL 2023.

HO4 trifft ein: Fuer den Spur-Eichdefekt gibt es eine Literaturspur, und sie zeigt auf die Bewegungsenergie
(Abschn. 4.4). Ein Weg zu L1 waere eine Kinetik aus 4D-Regge (Hoehn) oder aus Regge-Metriken mit stetiger Spur
(Christiansen/Lin 2026). Beides ist nicht gerechnet.

## 4. Die fuenf Stellen

### 4.1 Fluss-Eis: Zerlegung von Kantenfluessen

- **Literatur:**
  - Jiang/Lim/Yao/Ye 2011 (0811.1067) [S Abstract]: Jeder Kantenfluss zerfaellt orthogonal in einen Gradientenfluss
    und einen divergenzfreien Fluss. Dieser zerfaellt weiter in "a curl flow (locally cyclic) and a harmonic flow
    (locally acyclic but globally cyclic)". Berechnet wird das per kleinste Quadrate.
  - Lim 2015/2020 (1507.05379) [S Abstract]: "a large part of cohomology and Hodge theory is nothing more than the
    linear algebra of matrices satisfying AB = 0".
- **Fuer Finns Netz [M, H]:**
  - Spins auf den Pyrochlor-Ecken sind Fluesse auf den Diamant-Kanten. Die Eisregel ist ker d0^T (quellenfrei an den
    Tetraedermitten).
  - Quellenfrei = Wirbel + harmonisch. Die Wirbel kommen aus den 4 Sechsringen je Zelle: 2 je k != 0, also genau die
    zwei Photon-Polarisationen der Coulomb-Phase. Harmonisch sind 3 auf dem 3-Torus: die globalen Fluss- bzw.
    Windungssektoren (Abschn. 5).
  - Die Zahl haengt nicht am Hodge-Stern, die Zerlegung eines gegebenen Flusses schon: Orthogonalitaet heisst
    "bezueglich *1". Mit Einheitsgewichten ist es die topologische, mit *1 die physikalische Zerlegung.
  - Nur mit einem Stern, der den Patch-Test besteht, sind die harmonischen Fluesse genau die gleichfoermigen Felder
    (lineare Funktionen sind dann diskret harmonisch; vgl. LICHT-FINN-NETZ-1 PLAN, S-D [P]).
- **Im Projekt:**
  - Hodge-Zerlegung nur in 2D: INDUZIERT-WILSON-2D, (d + delta)^2 = Delta_0 + Delta_1 + Delta_2 [P].
  - Fuer Fluss-Eis in 3D nicht ausdruecklich gerechnet. Implizit enthalten ist sie in M-D von LICHT-FINN-NETZ-1
    (K = C^dag C, 2 Eichnullen, 2 Photonzweige) [P].
- **Unterscheidungspunkt:** keiner. Die Zerlegung ist eine Identitaet der linearen Algebra, also hier reine
  Umbenennung. Empirisch unterscheidbar wird nur die Wahl des inneren Produkts (Stelle 2).

### 4.2 Licht: Der Hodge-Stern traegt die Metrik

- **Literatur:**
  - Desbrun/Hirani/Leok/Marsden 2005 (math/0508341) [S Abstract]: umkreisbasiertes Dual "is crucial" fuer eine DEC
    mit Formen und Vektorfeldern.
  - HKV 2013 [S Abschn. 1]: Das DEC-Skalarprodukt ist a^T *p b, mit *p diagonal = Verhaeltnis von primalen und dualen
    Volumina. "For this to define a genuine inner product the entries have to be positive."
  - FEEC-Massenmatrizen ("Galerkin Hodge stars") sind die Alternative; fuer sie gilt HKV "not directly" [S ebenda].
  - Arnold/Falk/Winther 2010 (0906.4325) [S Abstract]: Stabilitaet folgt aus "subcomplex" plus "bounded cochain
    projection"; Hodge-Theorie wird vom Kontinuum ins Diskrete uebertragen.
- **Fuer Finns Netz [M]:**
  - In Maxwell E = (1/2)(e^T *1 e + b^T *2 b) sind d0 und d1 reine Inzidenzmatrizen. Die Metrik steckt nur in *1, *2.
  - Mit Einheitsgewichten (* = I) sieht die Theorie keine Laengen. Das ist genau MATERIE-NETZ-1 Abschn. 5: mit
    Einheitsgewichten 2,828427 bei jedem lambda, mit Laengengewichten 2,800423 = 2,828427/1,01 [P].
  - Das ist **Umbenennung**: Der Befund war vorab ableitbar (stand so im Plan dort).
  - LICHT-FINN-NETZ-1 PLAN Z. 49 [P]: "Maxwell auf den Pyrochlor-Kanten mit Dreiecken ... flache Nullmoden". Das ist
    eine Exaktheitsluecke durch fehlende 2-Zellen. Mit nur Dreiecken gehoert jede Kante und jedes Dreieck genau einem
    Tetraeder, Rang d1 = 3 je Tetraeder, also 6 je Zelle; Kern d1 = 6, Eichrang 4 bei k != 0. Damit **2 flache
    Nullbaender je k**, b1 des 2-Komplexes = 2 L^3 + 1 [M]. Mit den 4 Sechsecken je Zelle (und den Zellen
    dahinter) ist der Komplex exakt, b1 = 3 (Abschn. 5).
  - Fuer die Lichtablenkung (isotropes Phi) liefert **jeder** geometrische Stern die volle Ablenkung, denn alle skalieren
    bei homogener Streckung gleich [M].
- **Im Projekt:** MATERIE-NETZ-1 Abschn. 5 (nur homogene Streckung). mn.py Z. 380-396: diagonaler Stern mit
  **festen, gleichmaessigen Volumenanteilen** ("V_e = V/4", "V_f = V/nringe"); positiv per Bau, weder umkreisbasiert
  noch Galerkin [P, Gegensweep].
- **Unterscheidungspunkt:**
  - Einheits- gegen geometrischen Stern: trennt bei jeder Laengenaenderung (gemessen bei lambda = 1,01 [P]).
  - Geometrische Sterne untereinander (feste Anteile, umkreisbasiert, Galerkin) sind bei homogener Streckung gleich.
    Sie trennen erst bei **anisotroper (TT-)Verzerrung** und auf unregelmaessigen Netzen (Stelle 5).
  - Jacobson u. a. 2024 (2406.08647) [S Abstract] dazu: Die Wahl der Simplexmitten entscheidet ueber "continuity with
    respect to vertex positions, positive semi-definiteness ..., positivity of the mass matrix, and unbiased-ness on
    regular grids". Lineare FE "exhibit bias on tetrahedralized regular grids".

### 4.3 Zufallsnetze und Umklappen: Positivitaet und Rippa

- **Literatur:**
  - Positivitaet: HKV 2013 (siehe HO1) [S]. Glickenstein 2011 [S Abschn. 6.2, Prop. 39(1)]: Mit l*_ij > 0 an allen
    Kanten ist der Laplace negativ semidefinit mit Kern = Konstanten. Doehrman/Glickenstein 2021 [S Abstract]: oft auch
    ohne Positivitaet.
  - Konvergenz: Mohamed/Hirani/Samtaney 2018 (1802.04506) [S Abstract]: DEC konvergiert numerisch auch auf
    Nicht-Delaunay-Flaechen. Mai 2025 (2505.08966) [S Abstract]: Konvergenz und Stabilitaet von DEC **in 2D** auf
    "non-degenerate Delaunay and shape regular" Netzen, ueber FEEC. Fuer 3D steht das nicht im Abstract.
  - Gut zentriert: VanderZee/Hirani/Guoy/Zharnitsky/Ramos 2009 (0912.3097) [S Abstract]: In einem 3-well-centered
    (2-well-centered) Tetraedernetz hat jede innere Ecke mindestens 7 (9) Kanten. Unendlich viele Eckumgebungen
    verbieten Wohlzentriertheit in R^3.
  - Rippa: siehe HO2.
- **Finns V ist nicht gut zentriert [M, aus EINE-WELT-LOCH-1 PLAN 1.1/1.2]:**
  - Die H-Ecke (Sechseckmitte) hat 6 H-Speichen + 2 C-H-Kanten = 8 < 9 Kanten. Damit ist V nicht 2-well-centered.
  - Direkt: C-H steht senkrecht auf dem regelmaessigen Sechseck. Das Dreieck C-H-v ist bei H rechtwinklig, seine
    Umkreismitte liegt auf der Hypotenuse.
  - Die Umkugelmitte des Sechsecktetraeders (C, H, v_i, v_i+1) liegt auf halber Hoehe ueber dem Schwerpunkt des
    gleichseitigen Dreiecks H v_i v_i+1. In baryzentrischen Koordinaten des halben Querschnitts ist alpha + beta = 4/3 > 1,
    also liegt sie ausserhalb.
- **Teilprobe Delaunay [M, von Hand, kubische Kante 1]:**
  - Paar Finn-Tetraeder / Kegel (gemeinsames Dreieck): lokal Delaunay, nicht entartet. Umkugel des Kegels: Radius 0,238,
    Abstand zur Finn-Spitze 0,412. Umgekehrt C1 im Abstand 0,433 > 0,217 von der Finn-Mitte.
  - Sechsecktetraeder-Paare um eine Achse: Ihre Umkugelmitten liegen je auf der eigenen Seite der gemeinsamen Flaeche
    C-H-v, das duale Stueck ist also positiv.
  - **Nicht Delaunay: Paar Sechsecktetraeder / Sechsecktetraeder ueber eine Sechseck-Sechseck-Kante desselben Lochs
    [M, beim Gegenlesen, 06:31].**
    - Koordinaten: Lochmitte C = 0, Ecken = Permutationen von (+-3, +-1, +-1) mit gerader Zahl von Minuszeichen,
      H_a = (1,1,-1), H_b = (1,-1,1), v = (3,1,1), v' = (3,-1,-1).
    - Umkugel von A = (C, H_a, v, v'): Mitte (11/6, -1/6, 1/6), Radius^2 = 123/36. Abstand^2 zu H_b ist 75/36, also
      innen.
    - Die duale Laenge der Flaeche (C, v, v') ist -(2/3)/sqrt2 (Kante 2 sqrt2), also *2 < 0.
    - 12 solche Flaechen je Zelle (6 je Loch). Ein 2-3-Zug ersetzt sie durch die Kante H_a-H_b (deren Mitte (1,0,0)
      liegt im Inneren der Flaeche). Alle 12 zugleich erhalten Fd-3m.
  - **Ungeprueft:** Paar Kegel / Sechsecktetraeder (gemeinsame Flaeche C, v_i, v_i+1 an Sechseck-Dreieck-Kanten). Dort
    liegt die Umkugelmitte des Sechsecktetraeders ebenfalls auf der dem H abgewandten Seite (Hoehe h/2 > h/3 der
    Flaeche). Ob der Kegel das ausgleicht, entscheidet die Rechnung.
- **Umklappen ueber Feldenergie [H, ES]:**
  - In 2D treibt die Dirichlet-Energie jedes Feldes die Kantenwechsel zur Delaunay-Triangulierung (Rippa, ueber
    Bobenko/Springborn [S Abstract]). Das Ziel haengt nicht vom Feld ab, das Feld setzt nur, ob und wie oft geklappt
    wird. M-A (energetisch, Feld) faellt in 2D also mit M-B (Delaunay) zusammen.
  - In 3D gibt es nach Alexa 2019 [L?] keinen allgemeinen Minimierer. Dass auch dort das Vorzeichen eines Zuges vom Feld
    unabhaengig ist ("harmonische Zuege"), ist nur [L?] (Quelle nicht lesbar).
- **Kopplung an UMKLAPP-1 [H]:**
  - UK0 (flache 2-3-Zuege aendern die Regge-Wirkung nicht) bleibt richtig. Die Zuege aendern aber *1 und *2, die an der
    Triangulierung haengen.
  - Ein Zug, der eine Flaeche nicht-Delaunay macht, gibt einen negativen *2-Eintrag. Die Richtung "lokal Delaunay =>
    positiv" steht in HKV (Lemma 2, Satz 3) [S]. Die Umkehrung ("nicht Delaunay => negativ") ist mein Schluss [M],
    nicht gelesen. Ob auch *1 negativ wird, haengt am Fall.
  - Nach Abschn. 4.4b ist der Takt-Operator P = -W^H B W ein *1-Laplace. Verliert P eine positive Richtung, so folgt aus
    der Traegheitsadditivitaet (Haynsworth, Schur-Komplement [L]): Auf der Zwangsflaeche der Eckregel entsteht genau
    eine negative Mode mehr, sofern B seine Zahl negativer Richtungen behaelt.
  - Das waere ein Mechanismus, an dem UK2 ("stabil, zwei masselose TT") scheitern kann. Doehrman/Glickenstein sprechen
    eher dagegen, dass wenige negative Gewichte reichen.
- **Im Projekt [P]:**
  - INDUZIERT-DIRAC-2D: Kaehler-Dirac mit umkreisbasierten Hodge-Sternen auf 2D-Netzen, die physikalisch nicht Delaunay
    sind. Ergebnis c_eff = +48 statt -4, weil Delta_2 Leitwerte 1/w_e hat (ca. 1 400 (k eps)^2 Kanten mit w_e < 0).
    Vorgeschlagen wurden intrinsisches Delaunay oder "positiven Hodge-Sternen (baryzentrisch bzw. Whitney)". Das sind
    genau die Auswege von HKV bzw. FEEC.
  - INDUZIERT-DICHTE-2D (intr gegen koord), KOVARIANZ-2D-GEGENPROBE und KOVARIANZ-EPS-1: Rippa nur [L].
  - TT-GLAS-1 (tg.py): periodische Delaunay-Netze mit Umkugel-Pruefung. Werkzeug vorhanden.
- **Unterscheidungspunkt:** "Positivitaet braucht gut zentriert" (HO1) gegen "Delaunay genuegt" (HKV) trennt sich auf
  Netzen, die Delaunay, aber nicht gut zentriert sind.
  - V ist kein solcher Kandidat (nicht Delaunay, s. o.).
  - Kandidaten sind V_D (V nach den 12 symmetrischen Zuegen, falls dann Delaunay) und die Zufalls-Delaunay-Netze von
    TT-GLAS-1. HO1 sagte dort moegliche negative Eintraege voraus, HKV sagt positiv bzw. null bei Entartung.

### 4.4 Schwerewellen: Regge als FEEC; Spur-Eichdefekt und Exaktheit [H]

- **Literatur:**
  - Christiansen 2011 und Christiansen/Hu/Lin 2023: siehe HO3. CHL 2023, Satz 5.1: Kohomologie des Regge-Komplexes in
    3D = de Rham x RM [S, lokal: torsion-steif-1/quellen].
  - Hu/Lin/Zhang 2023 (2311.15482) [S Abstract]: diskrete Hesse- und divdiv-Komplexe (BGG) in 2D/3D auf
    Triangulierungen, Kohomologie wie im Kontinuum.
  - McDonald/Miller 2008 (0804.0279) [S Abstract]: Skalarkruemmung an einer Ecke = "a vertex-based weighted average of
    deficits per weighted average of dual areas" (Voronoi-Dual). Die Eckregel des Projekts (Summe l_e eps_e) hat damit
    eine Hodge-Stern-Form.
  - Bahr/Dittrich 2009, Dittrich/Hoehn 2010, Hoehn 2015 (1411.5672): siehe HO4. Hoehn [S Abstract]: Der 1-4-Zug
    erzeugt 4 Lapse/Shift-Variablen, 2-3 ein Graviton, 3-2 die einzige nichttriviale Bewegungsgleichung; "the Pachner
    moves preserve the vertex displacement generators".
  - Christiansen/Lin 2026: Erwartungsverstoss 2.
- **(a) Warum "Spur" [M, Kontinuum, linearisiert um flach]:**
  - Die Eckregel c(N) entspricht (dd - delta Lap) N, also dem linearisierten Hamilton-Zwang.
  - Mit der ADM-Kinetik pi.pi - (1/2) pi^2 (3D) erzeugt sie hdot = hess N = def(grad N). Das ist eine reine
    Eckverschiebung, also erste Klasse (A c in Bild M).
  - Mit einem anderen Spurkoeffizienten lambda' statt 1/2 bleibt ein Rest (2 lambda' - 1) delta Lap N. Der ist keine
    Eichung, also zweite Klasse.
  - Erste Klasse haengt also an der **Spur** der Kinetik, relativ zur Spur der Kruemmung. Das passt zum Namen
    "Spur-Eichdefekt" und zur Definition in TT-ISO-1 Abschn. 7 (A c_v in Bild M?) [P].
- **(b) Takt-Operator [S Glickenstein Satz 34 und Beweis von Satz 24; M]:**
  - In 3D gilt dK_i/dt = -2 Summe_j (l*_ij/l_ij)(df_j - df_i) + Terme mit K_ij und K_i. Auf flachem Netz bleibt nur
    der Laplace mit *1-Gewichten.
  - Fuer Eckskalierung sind die Mitten die Kantenmitten, die Duale also umkreisbasiert.
  - Mit B = -l deps/dl l (EINE-WELT-LOCH-1 1.3; mn.py Kopf: "d_eps = -(B a)/l" [P]) folgt: P = -W^H B W ist bis auf
    die Normierung von W der Hodge-Laplace d0^T *1 d0 von V [H, Normierung nicht geprueft].
  - Die Isotropie der weichen Richtung (0,2 k^2 in [100], [110], [111] auf 1e-7, MATERIE-NETZ-1 [P]) folgt dann aus dem
    Patch-Test, sofern die umkreisbasierten *1-Gewichte in 3D die P1-FE-Gewichte sind [L?].
- **(c) Antwort auf die Kartenfrage [ES]: nein, keine fehlende Exaktheit.**
  - V ist eine flache Triangulierung des 3-Torus (Diedersumme 2 pi je Kante auf 1,8e-15, Euler 0 [P]). Nach CHL 2023
    ist ihr Regge-Komplex exakt bis auf die Kohomologie.
  - Das deckt sich mit EINE-WELT-LOCH-1 1.4 [P]: 3V - 3 + 6 flache Richtungen bei k = 0. Die numerisch gepruefte
    Annahme "ker B = Bild M" von MATERIE-NETZ-1 (PLAN 1.1, L = 16) ist damit ein Satz. Fuer k != 0 und den Torus ist das
    meine Uebertragung [ES].
  - Fuer eine Kinetik aus 4D-Regge waeren die Zwaenge auf **jeder** triangulierten Cauchy-Flaeche erster Klasse
    (Dittrich/Hoehn 2010 [S Abstract]). Der Defekt sitzt also in der gewaehlten Bewegungsenergie (Paarung), nicht im
    Netz. Das ist dasselbe wie "Regime G-b" in TAKT-UMBENENNUNG-L [P].
  - Christiansen/Lin 2026 nennen den strukturellen Grund, warum eine Kinetik je Tetraeder (Spur P0) mit Eckskalierungen
    (P1) schlecht zusammengeht [H]. Kandidat-Erklaerungen, nicht gerechnet:
    - der O(1)-Defekt auf V (0,76 bis 0,99 je Ecke, TT-ISO-1 [P]);
    - die fast singulaere K_red bei A3R2 (TT-ISO-1, Selbstanzeige 5 [P]): Die A3-Form ist genau S mit mu = 1/2,
      lambda = -1 auf stueckweise konstanten Metriken.
- **Unterscheidungspunkt "fehlende Exaktheit" gegen "Kinetik bzw. Spur-Vertraeglichkeit":**
  - Die Kinetik wechseln, das Netz behalten.
  - (i) Kinetik aus 4D-linearisiertem Regge (Zelt- bzw. Pachner-Zuege, Hoehn) auf V: Die Exaktheits-Lesart sagt
    "Defekt bleibt", die Kinetik-Lesart "Defekt -> 0".
  - (ii) Kinetik aus Regge-Metriken mit stetiger Spur (CL 2026): Die Kinetik-Lesart sagt "Defekt -> 0 oder ~ k".
  - Die Literatur entscheidet (i) schon fuer die Kinetik-Lesart, falls die Zeltkonstruktion des Projekts 4D-Regge ist.
    PACHNER-TAKT-1 rechnet euklidisches linearisiertes Regge nach Hoehn [P]; den Spur-Eichdefekt hat dort niemand
    gemessen.
  - Die Exaktheits-Lesart waere nur zu retten, wenn das Projekt-Netz keine Triangulierung waere. Das ist widerlegt
    (Gegensweep 1).

### 4.5 Materie und Abstrahlung: Hodge-Stern und Spannungskopplung

- **Literatur:** HKV 2013 [S Abschn. 1] (positive Eintraege noetig; Galerkin-Sterne als Alternative); Jacobson u. a.
  2024 [S Abstract] (Wahl der Mitten bestimmt Stetigkeit, Positivitaet, Unverzerrtheit); Glickenstein 2011 [S]
  (Eckskalierung entspricht umkreisbasierten Dualen).
- **Rechnung am Schreibtisch [M]:**
  - Gradientenenergie eines Skalars: E = Summe_e w_e (phi_i - phi_j)^2 mit festen Volumenanteilen, w_e = 3 V_e/|e|^2
    (wie mn.py).
  - Unter einer Verzerrung h aendert sich nur |e|^2 -> |e|^2 (1 + n_e h n_e). Der TT-Teil der Antwort ist
    -h_kl g_i g_j Summe_e w_e |e|^2 n_i n_j n_k n_l fuer ein Feld phi = g.x.
  - Fuer die 4 Diamant-Richtungen (+-1,+-1,+-1)/sqrt3 hat der Tensor 4. Stufe die Teile b = 4/9 (isotrop) und
    a = -8/9 (kubisch).
  - Fuer "+" mit h = diag(1, -1, 0) und g laengs x verschwindet die Kopplung: T_xxxx - T_xxyy = 4/9 - 4/9 = 0. Fuer "x"
    mit g laengs (1,1,0) ist sie voll (8/9 g^2). Im Kontinuum ist sie in beiden Faellen gleich gross.
  - Mit geometrischen Gewichten (P1-FE je Tetraeder, aus allen sechs Kantenlaengen neu berechnet) ist die Energie eines
    linearen Feldes fuer jede konstante Metrik exakt. Die TT-Kopplung ist dann die des Kontinuums.
- **Bedeutung [H]:**
  - Die statische Kopplung (Spur bzw. Volumen, Newton) ist bei allen geometrischen Sternen gleich. Deshalb konnten
    MATERIE-NETZ-1 und die MN-Urteile davon nichts merken.
  - Die Abstrahlung (TT) trennt die Sterne. Baut PUMPE-NETZ-1 die Gewichte wie mn.py (feste Anteile, nur |e|
    veraenderlich), koennen PN1 und PN2 an der Bauweise scheitern statt an der Physik.
  - MATERIE-NETZ-1 hat das in Selbstanzeige 10 selbst angedeutet ("nur die Homogenitaet wichtig") [P].
- **Unterscheidungspunkt:** Statische Newton-Kopplung und TT-Kopplung derselben Quelle, einmal mit festen Anteilen und
  einmal mit P1-FE-Gewichten. Die statische muss gleich bleiben, die TT-Kopplung nicht. In PUMPE-NETZ-1 (Arm S) ist das
  mit einem Schalter messbar.
- **Im Projekt:** nicht gerechnet. Ich habe nichts nach pumpe-netz-1/ geschrieben.

## 5. Betti-Zahlen und harmonische Fluesse auf dem 3-Torus (Kontrolle)

Zellzahlen je primitiver Zelle aus EINE-WELT-LOCH-1 PLAN 1.1, 1.2 und 1.3 [P]. Betti-Zahlen [M]: Simpliziale bzw.
zellulaere Homologie einer echten Zerlegung des 3-Torus ist (1, 3, 3, 1). Alles auf L^3 Zellen.

| Komplex | Ecken, Kanten, Flaechen, Zellen je Zelle | Euler | b0, b1, b2, b3 | harmonische Kantenfluesse | Bemerkung |
|---|---|---|---|---|---|
| V (gefuellt, Triangulierung) | 10, 68, 116, 58 | 0 | 1, 3, 3, 1 | 3 | gleichfoermige Stroeme, sofern *1 den Patch-Test besteht |
| S (kantenaermer) | 6, 40, 68, 34 | 0 | 1, 3, 3, 1 | 3 | wie V |
| Diamant + 4 Sechsringe + 2 Adamantan-Zellen (Fluss-Eis, Maxwell M-D) | 2, 4, 4, 2 | 0 | 1, 3, 3, 1 | 3 | quellenfrei: 2 L^3 + 1 = (2 L^3 - 2) Wirbel + 3 harmonisch; je k != 0 2 Eichnullen, 2 Photonen, 0 flach [M]; passt zu LICHT-FINN-NETZ-1 [P] |
| Pyrochlor-Kanten + nur Dreiecke (2-Komplex) | 4, 12, 8, - | 0 | 1, 2 L^3 + 1, 2 L^3, - | 2 L^3 + 1 | **2 flache Nullbaender je k** [M] = "flache Nullmoden" von LICHT-FINN-NETZ-1 Z. 49 |
| Pyrochlor + Dreiecke + 4 Sechsecke + 2 Tetraeder + 2 Stumpf-Tetraeder | 4, 12, 12, 4 | 0 | 1, 3, 3, 1 | 3 | exakt, keine flachen Nullmoden [M] |
| ohne Fuellung: je Kopie Tetraeder-Oktaeder-Wabe auf fcc (2 Kopien) | je 1, 6, 8, 3 | 0 | je 1, 3, 3, 1 | je 3 | zwei getrennte Komplexe, zusammen 6 [M] |

- Die Kontrolle der Karte (b1 = 3 auf dem 3-Torus) trifft fuer alle echten Zerlegungen zu. Mehr als 3 harmonische
  Fluesse gibt es nur im Pyrochlor-2-Komplex ohne Sechsecke, und dort extensiv viele.
- Nicht gerechnet, nur gezaehlt. Die Rangangabe "Rang d1 = 3 je Tetraeder" beruht darauf, dass Kanten und Dreiecke
  verschiedener Finn-Tetraeder disjunkt sind (eckenteilend) [M].

## 6. Regime, Moderatoren, Unterscheidungspunkte (Zusammenfassung)

| Erklaerungspaar | Moderator | Wo sie auseinanderlaufen | Zugaenglich? |
|---|---|---|---|
| Hodge als Umbenennung / als Werkzeug | topologische gegen metrische Groesse | Vorzeichen der Sterne auf Nicht-Delaunay-Netzen; TT-Kopplung; Spur-Vertraeglichkeit der Kinetik | ja, billig (Abschn. 7) |
| gut zentriert noetig (HO1) / Delaunay genuegt (HKV) | Netzklasse | Delaunay, aber nicht gut zentriert (V_D?, Zufalls-Delaunay) | ja |
| Spur-Defekt = fehlende Exaktheit / = Kinetik bzw. Spur | Bauweise der Bewegungsenergie bei festem Netz | Kinetik aus 4D-Regge bzw. mit stetiger Spur | mittel (PACHNER-TAKT-1-Werkzeug) |
| feste Volumenanteile / geometrischer Stern | Verzerrungsart | homogen: gleich; TT: verschieden | ja (PUMPE-NETZ-1, Arm S) |
| Rippa in 3D gilt / gilt nicht | Dimension | 3D-Gegenbeispiel (Alexa [L?]) | Quelle nicht lesbar; nicht unterscheidbar ohne Volltext |

## 7. Kartenvorschlag (einer): HODGE-TAKT-1

**Frage:** Ist der Takt-Operator von Finns Netz der umkreisbasierte Hodge-Laplace, ist V Delaunay, und was machen
Umklappungen mit dem Takt?

1. **HT0 (Kontrolle, vorab ableitbar):** Auf V und S gilt P = -W^H B W = c d0^T *1 d0 mit einem festen c an allen k
   (auf 1e-10). Grundlage: Glickenstein Satz 34, flach. Die Kontrolle kann scheitern, wenn W nicht die Eckskalierung mit
   Kantenmitten ist oder anders normiert.
2. ~~HT1 [H, 60 %]: V und S sind Delaunay. Alle *1- und *2-Eintraege sind > 0; Nullen gibt es hoechstens an
   kospharischen Stellen.~~ Beim Gegenlesen von Hand fuer V verfehlt (Abschn. 4.3, 12 negative *2 je Zelle).
   **Neu HT1' [H, 55 %]:** Auf V sind trotz der negativen *2 alle *1-Eintraege > 0, passend zu P > 0 [P]. V_D (V nach
   den 12 symmetrischen 2-3-Zuegen je Zelle) ist Delaunay. S: offen, 50 %.
3. **HT2 [H, 55 %]:** Nach f = 0,2 zufaelligen 2-3-Zuegen (UMKLAPP-1-Netze) gibt es negative *2-Eintraege, und P bleibt
   trotzdem an allen k positiv semidefinit (Doehrman/Glickenstein-Tendenz).
4. **HT3 (Folge, vorab ableitbar):** Bekommt P eine negative Richtung, hat B auf der Zwangsflaeche der Eckregel genau
   so viele negative Moden mehr (Haynsworth), sofern B seine Zahl negativer Richtungen behaelt.

**Ableitbarkeitsprobe:**

- Vorab ableitbar:
  - HT0 (Satz) und HT3 (lineare Algebra). Beides sind nur Kontrollen.
  - Dass V nicht gut zentriert ist (8 Kanten an H; rechter Winkel bei H) [M].
  - Dass V nicht Delaunay ist (Sechseck-Sechseck-Flaechen, *2 < 0) [M]. Das ist eine Kontrolle fuer den Code.
  - Teilweise lokal Delaunay: Paar Finn/Kegel und Paare im Sechseckfaecher [M].
- Nicht ableitbar:
  - Vorzeichen von *1 auf V, das Paar Kegel/Sechsecktetraeder, Delaunay-Eigenschaft von V_D und S (also HT1');
  - die Vorzeichen nach Zuegen (HT2);
  - die Zahl negativer Richtungen von B nach Zuegen.
- Die Konstante c ist nicht vorab bekannt. Ich erwarte 8, wenn die Kantendehnung je Kante gleich der Summe der zwei
  Eckwerte ist [H, nicht geprueft]. Sie geht in kein Urteil ein.

**Projekt-grep (06:25, alle Ausschluesse):**

- "circumcent", "Umkugel", "Voronoi", "gut zentriert", "well-centered": Treffer nur in RUNDE-24/tetra-stab,
  WEICHE-STAND-v6..v8 ("Voronoi-Skalar", patch-test-konsistent), RUNDE-36/zufallsnetz-1 (Netzdaten) und TT-GLAS-1
  (tg.py: periodisches Delaunay, Umkugel-Pruefung).
- Keine Datei rechnet umkreisbasierte Hodge-Sterne auf V oder S oder vergleicht P mit einem Hodge-Laplace.
- Glickenstein, Christiansen/Lin 2026, 1106.4266 und 2311.15482 stehen nirgends im Projekt.

**Rahmen:** Code-Agent; Bausteine aus materie-netz-1/code (B, W) und tt-glas-1/code (Delaunay, Umkugel). Kleintest,
Sekunden je Netz.

**Bedeutung (vorab):**

- Treffen HT0 und HT1' ein: MN2 (Einsteins Vorzeichen) ist eine Positivitaetsaussage der diskreten Hodge-Theorie
  (*1 > 0), nicht des Delaunay-Charakters, und Newtons Staerke folgt aus dem Volumen.
- Ist V_D Delaunay: Fuer M-B (UMKLAPP-1) gibt es dann eine symmetrische Delaunay-Fassung von Finns Netz, mit
  zusaetzlichen H-H-Kanten. Ihre TT-Eigenschaften waeren neu zu rechnen.
- Verfehlt HT2 (P kippt): Umklappungen ohne Delaunay-Bedingung machen den Takt instabil. Dann ist M-B (Delaunay) fuer
  Finns Takt Pflicht, nicht Wahl.

## 8. Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **V ist eine echte flache Triangulierung des 3-Torus. Geprueft [P]:** Diedersumme 2 pi je Kante auf <= 1,8e-15,
   Volumensumme 0,25 je Zelle (EINE-WELT-LOCH-1 ERGEBNIS Z. 92), Euler 0 (PLAN 1.2). Damit tragen Betti (1,3,3,1) und CHL.
2. **Die "Hodge-Gewichte" von MATERIE-NETZ-1 sind ein geometrischer Stern. Geprueft [P]:** mn.py Z. 380-396 nimmt feste,
   gleichmaessige Volumenanteile. Daraus folgt der Befund zu Stelle 5.
3. **B ist in MATERIE-NETZ-1 und EINE-WELT-LOCH-1 dasselbe. Geprueft [P]:** mn.py Kopf Z. 13, "d_eps = -(B a)/l".
4. **Der Spur-Eichdefekt ist normunabhaengig. Gelesen [P]:** Er ist euklidisch definiert (QR von M, TT-ISO-1 Abschn. 7).
   Ja/Nein (erste Klasse) haengt daran nicht, die Zahlen 0,76 bis 0,99 schon. In einer Massen- bzw. Hodge-Norm waeren sie
   andere.
5. **Nicht geprueft:**
   - Henley-Literatur zur Coulomb-Phase (harmonische Sektoren) [L];
   - ob in 3D die P1-FE-Gewichte gleich den umkreisbasierten *1-Gewichten sind [L?];
   - ob V im Paar Kegel/Sechsecktetraeder lokal Delaunay ist.
6. **Nachtrag beim Rueckwaertslesen:** Die Annahme "V ist Delaunay, bis auf das eine ungepruefte Paar" war selbst
   ungeprueft. Das Paar Sechsecktetraeder/Sechsecktetraeder hatte ich uebersehen. Von Hand geprueft: nicht Delaunay
   (Abschn. 4.3). Das ist der wichtigste Befund des Gegensweeps.

## 9. Kalibrierung

- **(a) Gemessen:** nichts in dieser Karte. Alle Zahlen mit [P] stammen aus anderen Karten.
- **(b) Nuetzlich verdichtet:**
  - die Trennung topologisch/metrisch;
  - Takt = *1-Laplace (Satz plus [M]);
  - der Ort des Spur-Defekts in der Kinetik (CHL + Dittrich/Hoehn + CL 2026);
  - die TT-Anisotropie fester Volumenanteile [M].
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - HO1 war ein verbreiteter Glaube, kein gelesener Satz.
  - Meine Erwartung "V ist Delaunay" (HT1, 60 %) kam aus der Symmetrie des Netzes, nicht aus einer Pruefung. Die
    Rechnung von Hand hat sie widerlegt.
  - Meine Sicherheit, dass der Spur-Defekt "in der Kinetik sitzt", ist waehrend der Recherche gestiegen, waehrend die
    Frage feiner wurde (von "Exaktheit?" zu "P0-Spur gegen P1-Skalierung"). Sie stuetzt sich auf Analogien. CL 2026
    reden ueber FE fuer das Anfangswertproblem der ART, nicht ueber Finns Paarungen. Gerechnet ist nichts.

## 10. Offene Fragen (wandern mit)

1. ~~Ist V Delaunay?~~ Nein, von Hand [M]. Offen sind: Vorzeichen von *1 auf V; das Paar Kegel/Sechsecktetraeder;
   ob V_D (nach 12 symmetrischen Zuegen je Zelle) und S Delaunay sind; T2-Loecher (gespiegelte Geometrie
   angenommen).
2. Gilt P = c d0^T *1 d0 auf V, und welche Konstante c?
3. Verschwindet der Spur-Eichdefekt mit einer Kinetik aus 4D-Regge (Hoehn, PACHNER-TAKT-1-Werkzeug) oder aus Regge-Metriken
   mit stetiger Spur (CL 2026)?
4. Rippa in 3D: Alexa 2019 im Volltext. Sind 3D-Zuege "harmonisch" (Vorzeichen unabhaengig vom Feld)?
5. TT-Kopplung eines Materiefelds: feste Volumenanteile gegen P1-FE-Gewichte (PUMPE-NETZ-1, Arm S).
6. Kontinuums-Rechnung (Abschn. 4.4a) und Diamant-Tensor (Abschn. 4.5) hat kein zweiter Leser gesehen.

## 11. Quellen (Abrufzeiten in quellen/abrufzeiten.txt)

- Hirani, Kalyanaraman, VanderZee (2013): Delaunay Hodge Star. Computer-Aided Design 45(2), 540-544. arXiv:1204.0747v4.
  https://arxiv.org/abs/1204.0747 (Volltext F2, gelesen: Abschn. 1, 3, 4, 5, Saetze 3, 5, 6, 7, Lemma 2)
- VanderZee, Hirani, Guoy, Ramos (2010): Well-Centered Triangulation. SIAM J. Sci. Comput. 31(6), 4497-4523.
  arXiv:0802.2108. https://arxiv.org/abs/0802.2108 (Abstract)
- VanderZee, Hirani, Guoy, Zharnitsky, Ramos (2009): Geometric and Combinatorial Properties of Well-Centered
  Triangulations in Three and Higher Dimensions. arXiv:0912.3097. https://arxiv.org/abs/0912.3097 (Abstract)
- Glickenstein (2011): Discrete conformal variations and scalar curvature on piecewise flat two and three dimensional
  manifolds. J. Differential Geom. 87, 201-237. arXiv:0906.1560. https://arxiv.org/abs/0906.1560 (Volltext F9: Satz 34,
  Beweis Satz 24, Abschn. 6.2, Prop. 39, Satz 41)
- Glickenstein (2005): Geometric triangulations and discrete Laplacians on manifolds. arXiv:math/0508188 (Abstract)
- Doehrman, Glickenstein (2021): Determinant of the finite volume Laplacian. arXiv:2108.07308.
  https://arxiv.org/abs/2108.07308 (Abstract)
- Christiansen (2011): On the linearization of Regge calculus. Numer. Math. 119, 613-640. arXiv:1106.4266.
  https://arxiv.org/abs/1106.4266 (Abstract)
- Christiansen, Hu, Lin (2023): Extended Regge complex for linearized Riemann-Cartan geometry and cohomology.
  arXiv:2312.11709 (lokal: RUNDE-37/torsion-steif-1/quellen/B2-2312.11709v1.txt; Einleitung S. 1 und 3, Satz 5.1)
- Christiansen, Lin (2026): Regge metrics with enhanced trace. arXiv:2603.13977v1 (14.03.2026).
  https://arxiv.org/abs/2603.13977 (Volltext F5: Abschn. 1, S. 2 und 9-10, Gl. 1.30, Fussnote 1)
- Hu, Lin, Zhang (2023): Distributional Hessian and divdiv complexes on triangulation and cohomology. arXiv:2311.15482
  (Abstract)
- McDonald, Miller (2008): A Discrete Representation of Einstein's Geometric Theory of Gravitation: The Fundamental Role
  of Dual Tessellations in Regge Calculus. arXiv:0804.0279 (Abstract)
- Bahr, Dittrich (2009): (Broken) Gauge Symmetries and Constraints in Regge Calculus. Class. Quant. Grav. 26, 225011.
  arXiv:0905.1670 (Abstract)
- Dittrich, Hoehn (2010): From covariant to canonical formulations of discrete gravity. arXiv:0912.1817 (Abstract)
- Hoehn (2015): Canonical linearized Regge Calculus: counting lattice gravitons with Pachner moves. Phys. Rev. D 91,
  124034. arXiv:1411.5672 (Abstract)
- Bobenko, Springborn (2007): A discrete Laplace-Beltrami operator for simplicial surfaces. Discrete Comput. Geom. 38,
  740-756. arXiv:math/0503219 (Abstract)
- Lam (2022): Delaunay decompositions minimizing energy of weighted toroidal graphs. arXiv:2203.03846 (Abstract)
- Dym, Lipman, Slutsky (2017): A Linear Variational Principle for Riemann Mappings and Discrete Conformality.
  arXiv:1711.02221 (Abstract)
- Lim (2015/2020): Hodge Laplacians on graphs. arXiv:1507.05379 (Abstract; SIAM Review 62 laut Karte [L])
- Jiang, Lim, Yao, Ye (2011): Statistical ranking and combinatorial Hodge theory. arXiv:0811.1067 (Abstract)
- Desbrun, Hirani, Leok, Marsden (2005): Discrete Exterior Calculus. arXiv:math/0508341 (Abstract)
- Arnold, Falk, Winther (2010): Finite element exterior calculus: from Hodge theory to numerical stability.
  Bull. Amer. Math. Soc. 47, 281-354. arXiv:0906.4325 (Abstract)
- Mohamed, Hirani, Samtaney (2018): Numerical Convergence of Discrete Exterior Calculus on Arbitrary Surface Meshes.
  arXiv:1802.04506 (Abstract; Autoren aus der API-Kopie F8)
- Jacobson (2024): Optimized Dual-Volumes for Tetrahedral Meshes. arXiv:2406.08647 (Abstract; laut API-Kopie F8 ein
  Autor; im Text oben steht "Jacobson u. a.", gemeint ist diese Arbeit)
- Berbatov, Jivkov (2025): Variational formulations of transport phenomena on combinatorial meshes. arXiv:2505.09443
  (Abstract)
- Zhu, Christiansen, Hu, Hirani (2025): Convergence and Stability of Discrete Exterior Calculus for the Hodge Laplace
  Problem in Two Dimensions. arXiv:2505.08966 (Abstract; Autoren aus der API-Kopie F10)
- Nicht gelesen, nur [L?]: Alexa (2019), Harmonic Triangulations, ACM Trans. Graph. 38(4) (dl.acm.org: HTTP 403);
  Rippa (1990), Minimal roughness property of the Delaunay triangulation, CAGD 7; Hirani (2003), Thesis; Arnold/Falk/
  Winther (2006), Acta Numerica.

## 12. Selbstanzeigen

1. **F1 waren zwei HTTP-Anfragen:** Die erste (http) war leer (0 Byte, geloescht), die zweite (https) lief. Gezaehlt als
   ein Abruf.
2. **F7 (ACM) gab HTTP 403** und hat einen der zehn Abrufe ohne Inhalt verbraucht. Er steht nicht mit eigener
   date-Messung in abrufzeiten.txt; nachgetragen mit Zeitfenster.
3. **Zeitangaben im Arbeitsfeld waren teils geschaetzt** (F4-Ausgang "06:14:5x", F9 "06:19", F10 "06:21" u. a.). Sie
   sind im Abschnitt "Berichtigungen" mit den gemessenen Werten aus abrufzeiten.txt ersetzt, ohne Loeschung.
4. **pdftotext** lief lokal fuer drei PDFs (Textauszug, keine Rechnung). Lokal liefen kein python, awk oder perl.
   Zum Lesen nutzte ich grep, sed, tr, cut und paste.
5. **Abrufe ueber curl** (arXiv-API, arxiv.org-PDF) statt WebFetch, um Rohkopien in quellen/ abzulegen. F7 lief ueber
   WebFetch.
6. **Alle [M]-Stellen sind ohne zweiten Leser und ungeprueft:** Kontinuums-Spurrechnung, Diamant-Tensor, Rang- und
   Betti-Zaehlungen, Umkugel-Teilprobe.
7. **grep ohne die Pflicht-Ausschluesse:** Alle rekursiven greps ueber Projektpfade hatten die sechs Ausschluesse.
   Mehrere greps auf einzeln genannte Dateien liefen ohne die Flags, ebenso ein nicht rekursiver grep auf
   research-scout-claude-20260913/http-cache/*.json. Das betraf Karten von RUNDE-37, mn.py, tg.py, tetra_stab.py,
   WEICHE-STAND und RUNDE-42.md. Versiegeltes oder KS-1-Ergebnisse habe ich weder getroffen noch geoeffnet.
8. Kein Journal, kein Peerbus, kein Commit. Geschrieben nur in RUNDE-37/hodge-l/.

## 13. Einfach gesagt

Hodge-Theorie ist die Mathematik, die sagt, wie man Stroemungen auf einem Netz in "aus Quellen", "Wirbel" und "um den
ganzen Raum herum" zerlegt, und wo im Netz die Laengen versteckt sind: nur im sogenannten Hodge-Stern. Vieles, was wir
schon gerechnet hatten, ist damit bekannte Mathematik, zum Beispiel, dass Licht die Laengen nur mit laengenabhaengigen
Gewichten bemerkt. Neu ist: In 3D reicht schon ein "Delaunay"-Netz, damit diese Gewichte positiv sind, aber Finns gefuelltes Netz
erfuellt das an einigen Stellen in den Loechern nicht, und dort koennten Zellen von selbst umklappen. Fuer das Problem mit der Regel an den Ecken zeigt eine Arbeit vom Maerz
2026, dass die Art, wie wir die Bewegung der Kanten aufschreiben, schlecht zu Skalierungen an den Ecken passt; das ist
eine Spur, keine Loesung. Und fuer Gravitationswellen ist wichtig, wie man die Gewichte baut: Einfache Gewichte geben
die richtige Schwerkraft, koennten aber die Abstrahlung in manchen Richtungen ganz verschlucken.

Abschluss des Textes 2026-10-05 06:33:07 CEST (date). Die Zeitbox von 60 min ab 06:02:48 CEST endet um 07:02:48 und ist eingehalten. Journal, Peerbus und Commit uebernimmt die Leitung.
