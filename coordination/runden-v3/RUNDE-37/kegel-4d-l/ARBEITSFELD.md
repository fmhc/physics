# KEGEL-4D-L: Arbeitsfeld (feldforscher, eine Datei, vor jedem Schritt neu gelesen)

- Start 2026-10-05 06:07:04 CEST (date). Zeitbox 60 min, also bis etwa 07:07 CEST.
- Karte gelesen 06:07 (bindend, KB1 bis KB4 unveraendert). Kontext gelesen: GEOMETRIE-XD (R27), UNSCHAERFE-KANTE-L
  (Karte), LICHT-FINN-NETZ-1, DIM-LEITER-QBALL-1, PACHNER-TAKT-1 (je Abschnitt 1).
- Gestrichenes bleibt stehen und wird mit ~~...~~ markiert. Offene Rueckfragen stehen unten und wandern mit.

## Schreibtisch vor den Abrufen (06:10 bis 06:16, ohne Quelle)

### S1 Kegel und Ebene [M]
- Ebene t = a + v x, Kegel t^2 = x^2 + y^2: (1 - v^2) x^2 - 2 a v x + y^2 = a^2 (Karte bestaetigt).
- Halbachsen der Projektion auf (x, y): A = a/(1 - v^2), B = a/sqrt(1 - v^2), Mitte x0 = a v/(1 - v^2).
  e = sqrt(1 - B^2/A^2) = v. Brennpunktabstand e A = x0, also liegt **ein Brennpunkt im Ursprung (Kegelspitze)**.
- Kuerzer: auf dem Kegel gilt r = t = a + v x. Das ist die Brennpunkt-Leitlinien-Form r = e (x + a/e) mit e = v,
  in Polarform r = a/(1 - v cos phi), also **genau die Kepler-Bahngleichung** mit Halbparameter p = a.
- **Vorsicht 1 (Wortlaut):** e = v gilt fuer die Projektion auf die Ruhe-Ebene (x, y), nicht fuer die Kurve in der
  schraegen Ebene selbst. Euklidisch in der Ebene gemessen: e' = v sqrt(2/(1 + v^2)) (Dandelin, Kegelhalbwinkel 45 Grad).
  Mit der von Minkowski induzierten Metrik (ds^2 = (1 - v^2) dx^2 + dy^2) ist der Schnitt fuer v < 1 ein **Kreis**:
  die Gleichzeitigkeitsflaeche des bewegten Beobachters schneidet die Lichtfront rund.
- **Kepler-Lenz [M, Lehrbuch]:** A = p x L - m k r^ ergibt A.r = L^2 - m k r, also r = L^2/(m k) - (A/(m k)).r.
  Der Abstand r ist eine affine Funktion des Ortes; der Exzentrizitaetsvektor e = A/(m k) ist die "Geschwindigkeit"
  der schneidenden Ebene. Energie E = (m k^2/(2 L^2)) (e^2 - 1): gebunden = raumartige Ebene, E = 0 = lichtartige
  Ebene (Parabel), ungebunden = zeitartige Ebene.
- Schluss [ES]: S1 ist eine exakte Umschreibung der Kepler-Bahn, der "Lichtkegel" ist hier aber nur der Graph
  t = |r| der Abstandsfunktion, kein physikalisches Licht. Regime 1 (Umbenennung).

### S5 600-Zelle [M, Gruppentheorie, noch ohne Quelle]
- Ecken = 120 Einheitsquaternionen der binaeren Ikosaedergruppe 2I. Nachbarn von 1: die 12 Elemente mit Realteil
  cos 36 Grad = phi/2, eine Konjugationsklasse (Ordnung 10).
- Damit ist der Graph ein normaler Cayley-Graph: Eigenwert je irreduzibler Darstellung rho:
  lambda_rho = 12 chi_rho(c)/d_rho, Vielfachheit d_rho^2.
- chi_j(c) = sin((2j+1) pi/5)/sin(pi/5): j = 0, 1/2, 1, 3/2, 2, 5/2 gibt 1, phi, phi, 1, 0, -1.
  Adjazenz: 12, 6 phi, 4 phi, 3, 0, -2 mit Vielfachheiten 1, 4, 9, 16, 25, 36; dazu 2', 3', 4':
  6 phi' = -3,708 (4), 4 phi' = -2,472 (9), -3 (16). Spur 0 und Spur A^2 = 1440 geprueft (Kopfrechnung).
- Laplace L = 12 - A: 0 (1), 2,292 (4), 5,528 (9), 9 (16), 12 (25), 14 (36), dann 14,472 (9), 15 (16), 15,708 (4).
- Vorlaeufig [M]: die untersten **91** Zustaende tragen genau die Wasserstoff-Schalen n = 1 bis 6 (1, 4, 9, 16, 25, 36)
  in richtiger Reihenfolge; darueber 29 "Spiegelzustaende" (9, 16, 4), kein n = 7. Grund: V_j bleibt unter 2I
  irreduzibel fuer j <= 5/2, bei j = 3 zerfaellt es ~~(3' + 4)~~ (3' + 4'; berichtigt 06:36, siehe unten). Abstaende stimmen nicht: 0 : 2,29 : 5,53 : 9 : 12 : 14
  gegen l(l + 2) = 0 : 3 : 8 : 15 : 24 : 35.
- Folgerung: KB3 ist vorab ableitbar (keine Messung). Ein Zahlentest waere nur Kontrolle meiner Rechnung.
- Zusatz [M/L?]: Finns Diamant-Netz (4 Kanten je Knoten) hat als S^3-Schliessung eher die **120-Zelle** {5,3,3}
  (600 Ecken, Grad 4, Tetraeder-Eckfigur, Fuenferringe), die 600-Zelle {3,3,5} ist die Tetraeder-Dichtpackung
  (Sadoc/Mosseri: a-Si gegen Metallglas) [L?].

### S3 KS mit Ladung [M]
- 4D-Oszillator in C^2 mit Quanten n_a, n_b (Rechts-/Linkskreis), Faserladung s = (n_a - n_b)/2.
  Zustaende zu n_a = n - 1 + s, n_b = n - 1 - s: (n + s)(n - s) = n^2 - s^2. Fuer s = 0: n^2 (Wasserstoff).
- Erwartung [L?]: Faserladung s ungleich 0 ergibt MICZ-Kepler (Kepler + Dirac-Monopol + 1/r^2), Entartung n^2 - s^2.

### S4 Bezout [M/L?]
- Linsengleichung von n Punktmassen: Polynomgrad n^2 + 1 (Witt 1990) [L?], also Bezout-Schranke n^2 + 1.
  Scharfe Schranke 5n - 5 [L?]. Gleich fuer n = 2 (5) und n = 3 (10), verschieden ab n = 4 (17 gegen 15).
- Vier Lichtkegel in 3+1D: Bezout 2^4 = 16, tatsaechlich hoechstens 2 (Differenzen linear, Positionsbestimmung) [M].

## Abrufprotokoll (Erwartung vor dem Abruf, Ausgang danach)

(noch keiner)

## Offene Rueckfragen

- R1: Gibt es Literatur zum Laplace-Spektrum der 600-Zelle mit Wasserstoff-Deutung? (Abruf geplant)
- R2: Finns Netz ist Diamant/Pyrochlor. Ist die 600-Zelle ueberhaupt das richtige S^3-Gegenstueck? (siehe Zusatz S5)

### A1 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:18:15 CEST
- Abruf: arXiv-API, all:"600-cell", nach Einreichdatum absteigend, bis 100 Treffer (deckt das 24-Monats-Fenster und
  aeltere Arbeiten in einem Abruf).
- Erwartung: einige Dutzend Arbeiten zu H4, E8, Quasikristallen, Frustration, Polytopen. Keine Arbeit deutet das
  Graph-Laplace-Spektrum der 600-Zelle als Wasserstoff-Schalen. Im 24-Monats-Fenster 3 bis 10 Eintraege, keiner dazu.
  Moeglich: Gitterfeldtheorie auf S^3 mit 600-Zellen-Verfeinerung (Brower u. a.) [L?].
- **Ausgang A1 (06:18:26 abgerufen, quellen/A1-arxiv-600cell-20261005-061826.xml; ein erster http-Versuch 06:18:19 kam
  leer zurueck, ohne Inhalt, nicht gezaehlt): Erwartung bestaetigt.** 41 Treffer, 6 im 24-Monats-Fenster (2510.01063,
  2604.00255, 2604.12971, 2605.18538, 2605.30373, 2608.30285). In keinem Abstract Laplace-Spektrum oder Wasserstoff.
  Nebenfunde [S Abstract]: 2604.12971 (Laves-Netz, 3 Kanten je Ecke, auf S^3 als Teilnetz der 600-Zelle, 2026);
  2011.04120 (Regge-FLRW-Universum aus 600-Zellen-Verfeinerungen, pendelt zwischen Ausdehnen und Zusammenziehen);
  2207.11077 (klassische Spins auf den 120 Ecken der 600-Zelle); math/0607446 (Cohn/Kumar: 600-Zelle minimiert alle
  vollstaendig monotonen Potentiale).

### A2 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:19:30 CEST
- Abruf: arxiv.org/abs/math/0401188 per WebFetch (Khavinson/Neumann).
- Erwartung (KB4): Abstract nennt hoechstens 5n - 5 Nullstellen von r(z) - conj(z) fuer rationales r vom Grad n >= 2,
  bestaetigt damit Rhies Vermutung zur Bildzahl von n Punktlinsen; Scharfheit (Rhie 2003) nicht im Abstract.
- **Ausgang A2 (06:19:38, quellen/A2-arxiv-linsen-20261005-061938.xml; statt WebFetch ein arXiv-API-Abruf mit drei
  IDs): Erwartung bestaetigt.** Khavinson/Neumann (math/0401188): conj(r(z)) - z hat hoechstens 5n - 5 Nullstellen,
  "settles a conjecture of S. H. Rhie"; Kommentar v2: Scharfheit durch Rhie. Rhie 2001 (astro-ph/0103463): Gleichung
  legt n^2 + 1 nahe, n = 1, 2, 3 erreichen 2, 5, 10. Rhie 2003 (astro-ph/0305166): 5(n - 1) konstruiert; negative
  Bilder uebersteigen positive um n - 1. Meine Schreibtisch-Aussage (Bezout-Grad n^2 + 1 nur bis n = 3 scharf) passt.

### A3 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:19:53 CEST
- Abruf: arXiv-API, all:Kustaanheimo AND all:monopole, nach Datum absteigend, bis 30 Treffer.
- Erwartung (S3): Arbeiten (Nersessian, Mardoyan, Pletyukhov/Tolkachev o. ae.) zeigen: KS-Reduktion des 4D-Oszillators
  mit Faserladung ungleich null ergibt das MICZ-Kepler-System (Kepler + Dirac-Monopol + 1/r^2), mit SO(4)-Entartung;
  dazu die 8D/5D-Fassung (zweite Hopf-Abbildung, SU(2)-Instanton). Im 24-Monats-Fenster 0 bis 2 Treffer.
- **Ausgang A3 (06:19:53, quellen/A3-arxiv-ks-monopol-20261005-061953.xml): Erwartung verletzt, 0 Treffer.**
  Analyse: Entweder technisch (Bindestrich-Wort "Kustaanheimo-Stiefel" oder AND-Syntax der API) oder inhaltlich (die
  Literatur nennt die Abbildung "Hopf", "Hurwitz" oder "Bohlin", nicht KS). A1 mit Phrasensuche lief normal, also
  ist die API nicht allgemein gestoert. Korrigierte Erwartung: Die MICZ-Literatur ist da, aber unter anderem Namen.
  Gegenprobe A4 ueber den Systemnamen statt ueber die Abbildung.

### A4 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:20:12 CEST
- Abruf: arXiv-API, all:MICZ OR all:"MIC-Kepler", nach Relevanz, bis 40 Treffer.
- Erwartung: mindestens 15 Treffer. Mindestens ein Abstract sagt, dass MICZ-Kepler durch Reduktion des 4D-Oszillators
  (Hopf bzw. KS bzw. "Kepler problem in 4D/conformal") mit nicht verschwindender U(1)-Ladung entsteht; Entartung bzw.
  SO(4) bleibt erhalten.
- **Ausgang A4 (06:20:12, quellen/A4-arxiv-micz-20261005-062012.xml): Erwartung bestaetigt (46 Treffer, KS-Dualitaet),
  aber mit zwei Erwartungsverstoessen im Beifang.** A3 war also inhaltlich-sprachlich leer: Die KS-Literatur sagt
  "MIC-Kepler", "charge-dyon", "magnetic flux tube", nicht "monopole".
  - [S Abstract] Mardoyan/Petrosyan 2006 (quant-ph/0604127): verallgemeinertes MIC-Kepler und 4D-Singulaer-Oszillator sind dual,
    die Dualitaet ist eine verallgemeinerte KS-Transformation. Ebenso 1908.03572 (ND-Oszillator, (n+1)D-MICZ).
  - **V-S3 [S Abstract] ~~Nersessian/Pogosyan~~ Nersessian (Einzelautor, berichtigt 06:36) 2000 (math-ph/0010049):** Bohlin-Abbildung: gerade Oszillatorzustaende
    geben das gewoehnliche Coulomb-System, **ungerade Zustaende ein Coulomb-System mit Flussrohr, das halben Spin
    erzeugt**; KS auf Sphaere/Pseudosphaere gibt MIC-Kepler (Ladung-Dyon). Passt zu meiner Zaehlung (Faserladung
    s = 1/2 gibt halbzahlige Drehimpulse, Entartung n^2 - 1/4). Bezug: Projektfrage Spin 1/2.
  - **V-S1 [S Abstract] Meng 2012 (1111.2277, J. Math. Phys. 53, 052901):** "The recent 4D perspective of the Kepler
    problem": Bahnen als Paare von Minkowski-Vektoren (a, l), l.l = -1, a.l = 0, a_0 > 0; **SO+(1,3) x R+ wirkt
    transitiv auf die orientierten elliptischen Bahnen und getrennt auf die parabolischen**, und verbindet Bahnen
    verschiedener Monopolladung. Folge fuer S1: Die Konstruktion ist Literatur (nicht nur [M]); und die Lorentzgruppe
    fuehrt Ellipse in Ellipse, Parabel in Parabel, nie Ellipse in Parabel. Keplers Stetigkeit ueber die Parabel ist
    ein Grenzuebergang v -> 1, keine Lorentz-Transformation.
  - Weitere [S Abstract]: 2601.13028 (Jan. 2026, im 24-Monats-Fenster): MICZ-Analoga auf S^3 und Hyperboloid, Spektren
    mit zwei Quantenzahlen. 0803.3430 (Ballesteros u. a.): Bertrand-Raumzeiten (Perlick 1992), geschlossene Bahnen nur
    mit Kepler- oder Oszillatorpotential, auch auf gekruemmten 3-Raeumen. 1406.5866: MICZ und Gibbons/Manton
    (langsame BPS-Monopole, Taub-NUT) haben je einen Runge-Lenz-Vektor, also Kegelschnittbahnen.
- Korrigierte Erwartung: S1 ist als Lichtkegel-Darstellung der Kepler-Bahnen veroeffentlicht (Meng). A5 sucht die
  Primaerstelle.

### A5 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:21:40 CEST
- Abruf: arXiv-API, au:Meng AND all:Kepler AND (all:cone OR all:Lorentz OR all:Minkowski), nach Datum, bis 30.
- Erwartung: Eine Arbeit von G. Meng (etwa 2011 bis 2013) formuliert das Kepler-Problem auf dem Zukunftslichtkegel des
  Minkowski-Raums (bzw. einer Jordan-Algebra) und beschreibt die Bahnen als Schnitte des Lichtkegels mit Ebenen.
  Ausserdem 0 bis 2 Treffer im 24-Monats-Fenster.
- **Ausgang A5 (06:21:40, quellen/A5-arxiv-meng-kepler-20261005-062140.xml): Erwartung teilweise verletzt.** Nur ein
  Treffer, wieder 1111.2277; die Primaerstelle der "4D perspective" steht nicht mit diesen Woertern im Abstract
  (vermutlich "Jordan algebra" oder "J-Kepler"). 24-Monats-Fenster: 0 Treffer. Korrektur: Die Stelle im Volltext von
  1111.2277 suchen (A6), statt weiter ueber Abstracts zu raten.

### A6 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:22:00 CEST
- Abruf: arxiv.org/pdf/1111.2277 per WebFetch (Volltext, Abschnitt zur 4D-Sicht).
- Erwartung: Der Text identifiziert den Konfigurationsraum R^3 \ {0} mit dem Zukunftslichtkegel (x -> (|x|, x)) und
  beschreibt eine Kepler-Bahn als Schnitt des Lichtkegels mit einer Hyperebene a.X = const (plus l.X = 0). Elliptisch
  bei zeitartigem a, parabolisch bei lichtartigem a. Zitiert wird eine eigene fruehere Arbeit (2011) als Quelle der
  4D-Sicht. Eine Formel e = v steht dort nicht ausdruecklich.
- **Ausgang A6 (06:22, WebFetch konnte das PDF nicht lesen, legte es aber ab; Kopie quellen/A6-arxiv-1111.2277-pdf-...;
  gelesen mit dem Read-Werkzeug, S. 1 bis 7): Erwartung bestaetigt, mit zwei Zusaetzen, die die Erwartung verletzen.**
  - [S Meng, S. 4, Gl. (2.11), (2.12)]: "the projection of the Minkowski space onto R^3 defines a diffeomorphism from
    the future light cone {(x0, r) | x0^2 - r^2 = 0, x0 > 0} onto R^3_*"; die Bahn (2.3) r - A.r = L^2 - mu^2 ist
    der Schnitt des Zukunftslichtkegels mit der Ebene a.x = 1, l.x = 0, a = (1, A)/(L^2 - mu^2),
    l = (mu, L)/sqrt(L^2 - mu^2). Fuer mu = 0 ist das genau S1 mit v = A (Lenz-Vektor), e = |A|.
  - [S Gl. (3.5)]: E = -a^2/(2 a0). Ellipse a^2 > 0, Parabel a^2 = 0, Hyperbel a^2 < 0 [S Thm. 1 (5), S. 3].
  - [S S. 7]: Im elliptischen Fall laesst sich (a, l) per Lorentz-Transformation auf A = 0 bringen: "the magnetic
    charge is zero and the orbit is a circle". **Jede Ellipse ist also zu einem Kreis Lorentz-aequivalent** (KB1).
  - [S S. 3]: Keine entsprechende Wirkung auf hyperbolische Bahnen (a^2 < 0); erst mit den "hyperbolic orbit
    companions" (anderer Ast) wird die Wirkung auf den Parabeln samt Grenzen transitiv (S. 7).
  - **Zusatz 1 (Verstoss): "The Jordan algebra approach to the Kepler problem requires a second temporal dimension,
    and the Lorentz transformations in this note refer to the one that mixes space with this second temporal
    dimension."** Die Kegelzeit x0 ist der Abstand r, nicht die physikalische Zeit. S1 ist also kein Lorentz-Schub
    der wirklichen Raumzeit.
  - **Zusatz 2 (Verstoss): "the magnetic charge mu is relative and becomes zero in a certain 'inertial' frame".**
    Der Schub in der zweiten Zeit erzeugt aus einer Kepler-Bahn eine MICZ-Bahn mit Monopolladung. Meng fragt offen:
    "Is this second temporal dimension more than just a mathematical artifact?"
  - Quelle der 4D-Sicht: [2] G. W. Meng, Euclidean Jordan Algebras, Hidden Actions, and J-Kepler Problems,
    arXiv:0911.2977 (nicht abgerufen).

### A7 (Erwartung vor dem Abruf)
- Zeit: 2026-10-05 06:23:47 CEST
- Abruf: arXiv-API, all:"120-cell", nach Datum absteigend, bis 100 Treffer (24-Monats-Pruefung fuer den
  Kartenvorschlag: Diamant-Gegenstueck auf S^3).
- Erwartung: 20 bis 50 Treffer (Polytope, H4, Quasikristalle, Frustration). Kein Abstract mit Graph-Laplace-Spektrum,
  Wasserstoff-Schalen oder "Diamant auf S^3". Im 24-Monats-Fenster 2 bis 8 Treffer, darunter vielleicht die Gruppe
  hinter 2604.12971 (Netze auf S^3).
- **Ausgang A7 (06:23:47, quellen/A7-arxiv-120cell-20261005-062347.xml): Erwartung bestaetigt.** 24 Treffer, 6 im
  24-Monats-Fenster (zwei Polytop-Abwicklungen, ein Kochen-Specker, drei ML-Arbeiten). Kein Abstract mit Laplace,
  Eigenwert, Spektrum, Wasserstoff oder Diamant (grep: 0). Nebenfund [S Abstract]: Deza/Shtogrin 1999
  (math/9906035): "4-Fullerene" = einfache 4-Polytope mit nur Fuenf- und Sechseck-2-Flaechen; drei unendliche
  Familien sphaerischer 4-Fullerene, Konstruktion A aus verklebten 120-Zellen. Das ist die Verfeinerungsleiter fuer
  Diamant-artige Netze (4 Kanten je Ecke) auf S^3. Dazu 1705.04910: 120-Zellen-Wurzelsystem, Diskretisierung von SU(2).

### A8 (Erwartung vor dem Abruf, letzter Abruf)
- Zeit: 2026-10-05 06:24:12 CEST
- Abruf: arXiv-API, all:Kepler AND (all:Paralipomena OR all:Desargues OR all:"principle of continuity" OR
  all:Witelo OR all:"burning mirror"), nach Relevanz, bis 30.
- Erwartung (KB2, 80 %): 0 bis 5 Treffer, davon hoechstens einer mit der Aussage, Kepler habe 1604 den Begriff
  "focus" eingefuehrt und die Kegelschnitte als stetige Familie mit einem Brennpunkt im Unendlichen bei der Parabel
  behandelt. Wahrscheinlicher Ausgang: kein lesbarer Beleg im Abstract, KB2 bleibt [L?].
- **Ausgang A8 (06:24:12, quellen/A8-arxiv-kepler-1604-20261005-062412.xml): 0 Treffer.** Erwartung (wahrscheinlich
  kein Beleg) bestaetigt; KB2 bleibt [L?], nicht an einer Quelle geprueft. Syntax ist nicht die Ursache (A5 mit AND und
  Klammern lieferte einen Treffer); arXiv-Abstracts fuehren Keplers Optik offenbar nicht unter diesen Woertern.
- **Abrufbudget erschoepft (8 von 8).** Der leere http-Versuch 06:18:19 und das Lesen des von WebFetch abgelegten PDFs
  sind nicht extra gezaehlt.
- Stand 2026-10-05 06:28:08 CEST: Schreibtisch und Gegensweep, danach DOSSIER.

## Schreibtisch nach den Abrufen

- **600-Zelle, dritte Spurprobe [M]:** Spur A^3 = 6 x Zahl der Dreiecke. Jede Ecke hat ein Ikosaeder als Eckfigur
  (30 Kanten), also 120 x 30/3 = 1200 Dreiecke, Soll 7200. Summe m lambda^3 mit den Werten oben: 7199,97. Bestanden.
- **120-Zelle [M, vorlaeufig]:** 600 Ecken, Grad 4, Eckfigur Tetraeder, Fuenferringe: das S^3-Gegenstueck des Diamanten.
  Kantengraph (1200 Ecken, Grad 6) = Pyrochlor-Gegenstueck; sein unteres Spektrum ist das der 120-Zelle plus 2
  (Kantengraph eines 4-regulaeren Graphen: lambda_L = lambda_G + 2), dazu ein flaches Band bei -2 mit Vielfachheit
  mindestens m - n = 600. Ob die unteren Niveaus der 120-Zelle 1, 4, 9, 16, 25, 36 tragen, ist nicht automatisch:
  Die Permutationsdarstellung auf 600 Punkten enthaelt manche Typen doppelt (Stabilisator der Ordnung 24).
- **4D-Simplexe [M + L?]:** Diederwinkel arccos(1/4) = 75,52 Grad. 5 um ein Dreieck: 377,6 Grad, Ueberschuss 17,6 Grad,
  also negative Kruemmung. Regulaere Schliessung: hyperbolische Wabe {3,3,3,5} mit der 600-Zelle als Eckfigur
  (120 Kanten, 600 Simplexe je Ecke) [L? Coxeter]. 4 um ein Dreieck: S^4 ({3,3,3,4}). Das Vorzeichen der Kruemmung bei
  Fuenferzahl kippt also von 3D (S^3) nach 4D (H^4).
- **Kopplung vor Bauteil (Regel 6):** n^2-Entartung bzw. geschlossene Kegelschnitte kommen auf vier Wegen: Runge-Lenz
  (Pauli), Fock-S^3 (Impulsraum), KS-Oszillator (Hopf-Faser), Meng-Lichtkegel (zweite Zeit). Gemeinsame Groesse: die
  konforme bzw. dynamische Gruppe SO(4,2) des 1/r-Potentials [L?, Barut/Kleinert 1967]. Fuer Finns Netz zaehlt also
  nicht Kegel, Sphaere oder Faser, sondern ob das Fernfeld exakt 1/r ist; Gitterkorrekturen ~ (l/r)^2 brechen SO(4) zuerst.

## Gegensweep (Regel 4): Was war selbstverstaendlich?

- G1 geprueft: Die 12 Nachbarn bilden eine Konjugationsklasse von 2I (Realteil phi/2; Klassen 1, 1, 30, 20, 20, 12,
  12, 12, 12). Dazu Spurproben A, A^2, A^3: bestanden. Die Formel lambda = 12 chi/d gilt also.
- G2 geprueft (Projektdateien): Finns Netz ist Diamant/Pyrochlor (LICHT-FINN-NETZ-1, Einheiten-Zeile), nicht die
  12-koordinierte 600-Zelle. Die Karte setzt in S5 beides gleich.
- G3 geprueft (Projekt-grep): Keplers Abstandsgesetz bzw. das Ehrenfest-Argument (stabile Bahnen und Atome nur in
  D = 3) ist Projektbestand: n-dimensionen-grundlagen-20260912.md, DIM-AUSWAHL-L [P]. Nicht als neue Idee fuehren.
  Ebenso Bars' Zwei-Zeiten-Physik: RUNDE-22/dunkel-zeit, Abruf I1d [P]. Mengs "zweite Zeit" dockt dort an.
- G4 nicht geprueft: Fock-S^3 ist der Impulsraum. "Wasserstoff auf der 600-Zelle" vermischt Ort und Impuls, solange das
  Netz im Ortsraum liegt. Aus dem Gedaechtnis [L].
- G5 nicht geprueft: Wasserstoff hat mit Spin 2 n^2 Zustaende; alle n^2-Vergleiche hier sind spinlos.
- G6 nicht geprueft: Die Nullergebnisse A3 und A8 koennten auch an der Wortwahl der Suche liegen (Teilprobe: Syntax ok).

## Offene Rueckfragen

- R1: Gibt es Literatur zum Laplace-Spektrum der 600-Zelle mit Wasserstoff-Deutung? -> In arXiv-Abstracts nicht
  gefunden (A1, A7). Das Graph-Spektrum selbst steht vermutlich in Tabellen distanzregulaerer Graphen [L?].
- R2: Ist die 600-Zelle das richtige S^3-Gegenstueck? -> Nein fuer den Diamanten (120-Zelle bzw. 4-Fullerene); ja fuer
  die Tetraeder-Dichtpackung. Offen fuer die Leitung: Welches Netz meint Finn mit "4D-Tetraeder-Netz"?
- R3 (neu): Ist Mengs zweite Zeit dieselbe wie die zweite Zeit in Bars' 2T-Physik? Nicht geprueft.

## Berichtigungen (06:36, nach Pruefung der Abrufdaten bzw. Nachrechnung)

- Z. 38: Unter 2I gilt V_3 = 3' + 4' (nicht 3' + 4). Charakterprobe an der Klasse 10A: chi(V_3) = -phi,
  chi(3') + chi(4') = phi' - 1 = -phi. Die 4 (= V_3/2, Zentrum -1) und die 4' (A5-Darstellung, Zentrum +1) sind
  verschieden. Am Spektrum aendert das nichts (4' gibt -3, 4 gibt 3).
- Z. 113: math-ph/0010049 hat laut Abrufdaten nur einen Autor (A. Nersessian), Phys. Atom. Nucl. 65, 1070 (2002).
  "Pogosyan" war aus dem Gedaechtnis. Die "half spin"-Aussage gilt dort woertlich fuer die 2D-Bohlin-Abbildung.
- Autoren aller Abstract-Quellen aus den XML-Dateien uebernommen (siehe DOSSIER, Quellenliste).
- Zusatz [M]: Unter H4 zerfaellt der Grad-6-Raum (49) in 9 + 24 + 16 (3'x3', 3'x4' + 4'x3', 4'x4'). FS4 wird damit zur
  Kontrolle statt Literaturprobe. V_7/2 = 2' + 6 (Charakter -phi = phi' - 1).
- 2026-10-05 06:37:07 CEST: DOSSIER.md geschrieben (Text ab 06:29:50) und nach Quellenpruefung berichtigt (Autoren, V2-Lesart, FS4). Kein Lauf, kein Journal, kein Peerbus.
