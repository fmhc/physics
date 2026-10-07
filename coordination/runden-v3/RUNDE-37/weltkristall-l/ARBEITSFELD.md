# WELTKRISTALL-L: Arbeitsfeld (feldforscher)

- Start 2026-10-05 07:05:07 CEST (date). Datei angelegt 07:09:29 CEST (date). Zeitbox bis ca. 08:05.
- Eine Datei fuer alles (Feld-Regel 5): Erwartung vor jedem Abruf (mit date-Zeit), danach Ausgang. Gestrichenes bleibt
  stehen und wird als ~~gestrichen~~ markiert. Offene Fragen wandern sichtbar mit (Abschnitt "Offen").
- Kennzeichen: [S] Quelle mit Abschnitt/Gl., [S Abstract], [L] Gedaechtnis, [L?] unsicher, [M] Schreibtisch (Kopfrechnung),
  [ES] eigener Schluss, [H] Hypothese, [P] Projektdatei.
- Abrufbudget: hoechstens 8 Netzabrufe (arXiv-API, INSPIRE-API, arxiv.org, freie Verlagsseiten), keine Websuche.
  Lokale Projektquellen zaehlen nicht als Abruf; auch fuer sie steht vorher eine Erwartung hier.

## 0. Schon gelesen (Projekt, 07:05-07:09)

- [P] ZELLE600-1: 600-Zelle gebaut; Fehlwinkel 7,3561 Grad an allen 720 Kanten; Summe(l delta) = 57,13 R gegen 6 pi^2 R
  (-3,52 %); 20 disjunkte 30er-Ringe (Linksmultiplikation); Wasserstoff-Schalen n = 1..6.
- [P] GEOMETRIE-XD: 70,53 Grad, 5,104 je Kante, 7,36 Grad Luecke, 63,2 Grad Ueberlapp; d = 4: 75,52 Grad, n flach 4,767.
- [P] RUNDE-22/geometrie-stand: Kleman/Friedel 2008 [S] S. 37-40 ("decurving", {3,3,5} -> F&K-Netz, Nelson 1983a nur
  ueber K/F); Schmidt/Kohler 2001: Regge-Disklination = Kruemmung, Versetzung = Torsion [L?]; Katanaev 2005 [S].
- [P] WEITERGEDACHT (R34): Kleinert-Weltkristall [L], Disklination -> Kruemmung, Versetzung -> Torsion.
- [P] KEGEL-4D-L: Fock/KS [L], KS-Zaehlung n^2 - s^2 [M]; Abfrage A1 all:"600-cell" (41 Treffer, 06:18) liegt als
  Datei vor: quellen/A1-arxiv-600cell-20261005-061826.xml in kegel-4d-l. **Darin schon:** Barrett/Galassi/Miller/Sorkin
  u. a. 1994 (gr-qc/9411008, "600-cell Friedmann cosmology"), De Felice/Fabri 2000/2001 (gr-qc/0009093, gr-qc/0106077:
  600-Zellen-Evolution, "already studied before"), Tsuda 2021 (2011.04120: "Collins-Williams formalism ... regular
  4-polytopes", Lambda > 0, pseudo-regulaere Verfeinerung der 600-Zelle). Das deckt den 24-Monats-Check "600-cell" ab
  (Abfrage von heute 06:18).
- [P] Gielen/Ried 2610.03479v1: Abschn. IV (Z. ~891): "In table 3 of [5] the authors show that the more refined 600-cell
  model results in much better agreement with the continuum"; [5] = Dittrich/Gielen/Schander 2022, CQG 39, 035012,
  arXiv 2109.00875. Abschn. V: "Both models are based on the 5-cell ... it would be worth investigating models based on
  more refined triangulations, again perhaps along the lines of [5]." Ausserdem: klassische Loesungen der unimodularen
  Fassung "mostly the same as the ones of standard Regge calculus".
- [P] TORSION-STEIF-1, Abschn. 1: 4 freie Rahmendrehungen je Zelle (18 Drehungen gegen 14 Bedingungen), x = D omega,
  Weitzenboeck-Typ, ohne Energie in der reinen Einstein-Cartan-Wirkung.
- [P] GLIED-10: everpresent Lambda; Simon 2026 (Zenodo, unbegutachtet): SN-Gewinner scheitern an DESI DR2 (+128 bis
  +1974); DNY II (JCAP 2024): Daten atypisch; ZAS 2018: "fits as well as LCDM" (Existenzfrage). Zwei Auswerte-Regime.

## 1. Erste Schreibtischbefunde (vor jedem Abruf) [M, Kopfrechnung]

- **M1 (H1-Formel):** Fehlwinkel delta5 = 2 pi - 5 theta = 0,128388 rad, delta6 = 2 pi - 6 theta = -1,10257 rad,
  theta = arccos(1/3) = 1,230959 rad. Mittel null: (1 - f) delta5 + f delta6 = 0 -> f* = delta5/theta = 0,10430.
  Aequivalent: mittlere Tetraederzahl je Kante q = 5 + f = 2 pi/theta = 5,1043. **Die Karte rechnet richtig.**
- **M2 (Kruemmung je Delta f):** Summe_e delta_e = N1 theta (f* - f). Regge: Integral R dV = 2 Summe_e l delta_e.
  Mit N1/N3 = 6/q und V = N3 l^3/(6 sqrt 2): <R> = 2 l N1 theta Delta f / V = 72 sqrt(2) theta Delta f /(q l^2)
  ~ 24,6 Delta f / l^2 (q = 5,10). Die Karte ("~ Delta f x 70,5 Grad / l^2") stimmt in der Skalierung, der Vorfaktor
  ist ~ 20 (fuer den Ricci-Skalar). Probe 600-Zelle (q = 5, f = 0, l = 1/phi, R = 1): <R> = 2 * 1,2 * 8,485 * 0,128388
  / 0,381966 = 6,845, ZELLE600-1: 2 * 57,131/16,6925 = 6,845. Kontinuum 6/R^2 = 6. **Passt zu Regges Summe.**
- **M3 (DT-Verdacht):** Fuer gleichseitige Tetraeder ist Summe_e delta_e = 2 pi N1 - 6 theta N3, also haengt die
  Regge-Kruemmung nur an Zaehlzahlen. Mit Euler (chi = 0) und N2 = 2 N3: N1 = N0 + N3. Flach im Mittel <=> N1/N3 =
  6 theta/(2 pi) = 1,1755 <=> N0/N3 = 0,1755. **Das ist die Wirkung der (euklidischen) dynamischen Triangulierung
  (S = k0 N0 - k3 N3 in 3D, k4 N4 - k2 N2 in 4D) [L].** H1 waere dann eine Umformulierung von DT, keine neue Idee.
  Zu pruefen (Abruf).
- **M4 (Coxeter-Verdacht):** q = 5,1043 ist Coxeters "statistische Wabe" {3,3,5,104} (Coxeter 1958, "Close-packing
  and froth") [L]. Ueber Z (Nachbarn je Ecke): Tetraeder je Ecke = 2Z - 4, q = 6 (Z - 2)/Z -> Z = 12/(6 - q) = 13,397.
  A15: Z = 13,5 -> q = 5,111 (f6 = 0,111); C15 (Laves): Z = 13,333 -> q = 5,100 (f6 = 0,100) [M]. Frank-Kasper-Phasen
  liegen also beidseits von f* (sie sind verzerrt, also nicht regulaer). Zu pruefen.
- **M5 (Lambda gegen Flachheit, Dimension):** Ein 3D-Netz (Raumschnitt) misst die Raumkruemmung (Omega_k), nicht
  Lambda. Lambda ist 4D: Scharnier = Dreieck, theta4 = arccos(1/4) = 75,52 Grad, q4 = 2 pi/theta4 = 4,767; mit 4er- und
  5er-Dreiecken f5* = (2 pi - 4 theta4)/theta4 = 0,767 [M]. H1 als "Lambda" verlangt die 4D-Zaehlung.
- **M6 (Zufallszaehlung, nur d = 4):** Poisson-Schwankung des mittleren Fehlwinkels ~ N^(-1/2). Mit N ~ (H l_P)^(-d)
  Zellen im Hubble-Volumen ist <R> ~ l_P^-2 (H l_P)^(d/2). Nur fuer d = 4 ist das ~ H^2 (Sorkin-Numerik). Fuer d = 3
  (Raumschnitt) waere R_3/H^2 ~ (H l_P)^(-1/2) ~ (8,5e60)^(1/2) ~ 3e30, also Omega_k ~ 1e30 statt < 2e-3 [M].
  **Die 3D-Zufallsform von H1 ist um ~33 Groessenordnungen ausgeschlossen; nur die 4D-Form (Volumen-konjugiert) traegt.**
- **M7 (Zahl 1e-122):** Lambda l_P^2 = 3 Omega_L (H0 l_P/c)^2 = 3 * 0,685/(8,49e60)^2 = 2,85e-122 [M]. Mit
  <R4> = 4 Lambda und Vorfaktor ~100 (4D, gleichseitig, l = l_P): Delta f ~ 1e-123 (nur wenn l = l_P; allgemein
  Delta f ~ Lambda l^2). Raumflachheit |Omega_k| < 2e-3: |R3| < 6 * 2e-3/7,2e121 = 1,7e-124 l_P^-2, Delta f < ~7e-126.

## 2. Abrufe (Erwartung vorher, Ausgang nachher)

(folgt)

## 3. Offen

- O1: Wo genau steht bei Nelson 1983 die Dichte der -72-Grad-Linien? (PRB 28, 5515 nicht frei; ueber Tarjus u. a. 2005
  oder Kleman/Friedel 2008 lokal lesen.)
- O2: Benutzen Collins/Williams 1973 wirklich die 600-Zelle (WK3)?
- O3: Wo ist die Hopf-Faserung der 600-Zelle mit Ikosaeder-Basis belegt (WK2)?
- O4: Kleinert: Lambda aus Defektdichte?

### L1 (lokal, kein Netzabruf): Tarjus u. a. 2005 (cond-mat/0509127, Text in RUNDE-17/quellen-frustration/hilfs) und Kleman/Friedel 2008 (0704.3055, Text in RUNDE-22/geometrie-stand/hilfs)
- Zeit vor dem Lesen: 07:10:29 (date)
- Erwartung: Beide nennen Nelsons "decurving" der {3,3,5} durch -72-Grad-Disklinationslinien; mindestens einer nennt die
  Liniendichte bzw. den mittleren Defektanteil als Folge der Kruemmungsbilanz und Coxeters statistische Wabe (q = 5,104,
  Z = 13,4). Lambda oder Kosmologie kommt in keinem vor.
- **Ausgang L1 (07:11:50, date): teils bestaetigt, teils verletzt.**
  - Bestaetigt: Tarjus u. a. 2005, S. 9-10 [S]: {3,3,5} auf S^3 mit Radius 5/pi mal Abstand; Sadoc/Kleman/Mosseri
    "decurving", Nelson-Gruppe Landau-Theorie; "flat on average" steht woertlich in Fussnote [44]: "positive and negative
    disclinations must balance each other to ensure that space is 'flat' on average [27, 33]"; die andere Lesart: relativ
    zur Ikosaeder-Vorlage "an excess of disclinations of a given sign (essentially, wedge disclinations carrying a 'charge'
    of -72 Grad)". Typischer Defektabstand "one or two particle diameters at most" (S. 10). Kein Lambda, keine Kosmologie.
  - Verletzt: **Weder Tarjus noch Kleman/Friedel nennen Coxeters statistische Wabe oder die Zahl 5,104 bzw. 13,4**
    (grep leer). Die Abzaehlform (f6 = 10,43 %) steht in diesen beiden Texten nicht ausdruecklich. Erwartung korrigiert:
    Die Bilanz "flach im Mittel" ist Literatur [S], die Zahl f* ist bisher nur [M] + [L] Coxeter 1958.
  - **Unerwartet (Erwartung verletzt, Nebenfund fuer H2/H4):** Kleman/Friedel 2008, Abschn. VII.C.2 (S. 57) [S]:
    In der {3,3,5} heissen die gekruemmten Versetzungen "Disvektionen" (rechte Schraube x e^(alpha q), linke e^(-alpha q) x).
    Ihr "Burgers-Vektor" liegt tangential an den Clifford-Parallelen der Hopf-Faserung zu q (Fig. 36, Anhang D). Fuer
    alpha = pi/5 ist er genau eine Kante (R/tau). Die Bahn ist ein Grosskreis aus 10 Kanten; es gibt 72 solche C5 (6 je
    Ecke). Anhang D [S]: Rechts-Schrauben erzeugen Clifford-Parallelen, "S3 as a fiber bundle of great circles S1 over a
    great sphere S2, the Hopf fibration". **Damit sind H2 (Hopf) und H4 (Versetzungen) in der 600-Zelle dieselbe Struktur:
    Translation laengs der Hopf-Faser = Disvektion.**

### F1 (Abruf 1 von 8), 07:12:00 (date): arXiv-API id_list = gr-qc/0307033, 1501.07614, 1502.03000, 2109.00875, 1612.06536
- Erwartung: Kleinert/Zaanen 2004 erklaeren das Fehlen der Torsion mit einem "nematischen" Weltkristall (Versetzungen
  proliferiert), Lambda kommt nicht vor. Liu/Williams 2016 (zwei Arbeiten): Collins/Williams-Formalismus mit 5-, 16- und
  600-Zelle, mit Lambda bzw. mit Massen auf den Ecken; 600-Zelle am naechsten am Kontinuum. Dittrich/Gielen/Schander
  2022: Lorentz-Pfadintegral mit Polytop-Diskretisierung, darunter die 600-Zelle. 1612.06536: Tsuda-Vorlaeufer in 3D.
- **Ausgang F1 (07:12:25): im Kern bestaetigt (eine Zeile je Quelle).** Kleinert/Zaanen 2004 [S Abstract]: Gravitation aus
  einem Weltkristall nach Quanten-Phasenuebergang in eine nematische Phase "by a condensation of dislocations"; kein Lambda.
  Liu/Williams 2016a [S Abstract]: Collins/Williams- und Brewin-Modelle fuer Lambda-FLRW; besser mit mehr Tetraedern; alle
  Modelle enden, wenn zeitartige Streben lichtartig werden; **die 600-Zelle ist im Abstract nicht genannt**. Liu/Williams
  2016b: Gitter-Universen mit Massen, CW-Form. DGS 2022 [S Abstract]: einfaches und unterteiltes 4-Polytop, Schalen von
  3-Sphaeren, Lambda, Lorentz-Pfadintegral; 600-Zelle nur ueber Gielen/Ried (Tabelle 3 von [5]). Tsuda/Fujiwara 2017: 3D.
  Nebenbefund fuer H4: Bei Kleinert/Zaanen ist der Versetzungssektor kondensiert, Torsion daher unsichtbar.

### F2 (Abruf 2 von 8), 07:12:25 (date): INSPIRE-API, Collins/Williams 1973, PRD 7, 965
- Erwartung: Titel "Dynamics of the Friedmann universe using Regge calculus"; Abstract nennt geschlossenes Staub-Universum,
  3-Sphaere aus regulaeren Polytopen (5-, 16-, 600-Zelle), 600-Zelle am besten. Falls kein Abstract: nur Metadaten.
- **Ausgang F2 (07:12:36): bestaetigt.** INSPIRE [S Abstract, Quelle APS]: "Models for the Friedmann Universe are constructed
  from 5, 16, or 600 dust-filled tetrahedrons connected so as to form a closed space. Using the techniques of Regge
  calculus the time development ... compared with the standard analytic solution". 61 Zitate. WK3 eingetroffen.

### F3 (Abruf 3 von 8), 07:12:36 (date): arXiv-API, (au:Sadoc OR au:Mosseri) AND (abs:Hopf OR abs:fibration OR abs:polytope OR abs:helix)
- Erwartung: Sadoc/Mosseri bzw. Sadoc/Charvolin zu Faserungen der S^3 in der kondensierten Materie; mindestens ein Abstract
  nennt die {3,3,5} mit Grosskreis-Fasern (Zehnecke) ueber Ikosaeder-Basis oder die Boerdijk-Coxeter-Helix. Kein Bezug zu
  Kepler, Wasserstoff oder Kustaanheimo/Stiefel.
- **Ausgang F3 (07:12:57): Erwartung verletzt.** 5 Treffer, keiner zur {3,3,5}-Faserung: Mosseri/Sadoc 2025 (2511.15450,
  im 24-Monats-Fenster) bauen eine "phyllotactic set on the hypersphere S3 ... using a Hopf fibration approach" [S Abstract];
  Charvolin/Sadoc 2011/2013 (Kollagen, "the Hopf fibration ... ideal template for a twisted bundle"); Mosseri 2001/2003
  (Qubits, Bloch-Kugel als Hopf-Basis). **Die Hopf-Faserung der 600-Zelle mit Ikosaeder-Basis ist bei Sadoc/Mosseri auf
  arXiv nicht belegt**; Beleg nur Kleman/Friedel 2008, Anh. D und VII.C [S] (Clifford-Parallelen, Zehneck-Grosskreise,
  12 Nachbarn auf dem Ikosaeder). Sadoc/Mosseri 1999 (Buch) bleibt [L?]. Korrektur: Die konkrete Zerlegung (12 Zehnecke
  ueber Ikosaeder, 20 Ringe ueber Dodekaeder) muss ich am Schreibtisch herleiten [M].

### F4 (Abruf 4 von 8), 07:12:57 (date): arXiv-API, abs:Kustaanheimo AND (discrete OR lattice OR polytope OR 600-cell OR icosahedral OR graph OR finite)
- Erwartung: Keine Arbeit verbindet KS mit der 600-Zelle oder einer diskreten Hopf-Faserung. Treffer eher zu numerischer
  Regularisierung (Himmelsmechanik), diskreter Zeit (integrable Diskretisierung) oder Gittermodellen ohne Polytop.
- **Ausgang F4 (07:14:34): bestaetigt.** 2 Treffer, keiner diskret im Sinn eines Polytops: Zheng u. a. 2026 (2609.19159, im
  24-Monats-Fenster) [S Abstract]: KS + "fiber invariance under the Hopf fibration" liefert E_n ~ 1/n^2 und g_n = n^2
  (Kontinuum, Festkoerper-Anwendung); Kibler/Negadi 2004: q-Deformation des KS-Oszillators. Keine Verbindung KS zur
  600-Zelle oder zu einer diskreten Hopf-Faserung (nach Recherchestand, Stichwortsuche in Abstracts).

### F5 (Abruf 5 von 8), 07:14:34 (date): arXiv-API, abs:"world crystal" OR (abs:"cosmological constant" AND (disclination(s) OR polytetrahedral OR "geometrical frustration" OR "defect density"))
- Erwartung: Kleinert-Arbeiten zum Weltkristall (2000er/2010er), Jizba/Kleinert/Scardigli (Unschaerfe auf dem Weltkristall),
  vielleicht ein bis drei Arbeiten anderer Autoren. **Keine** Arbeit leitet Lambda oder Flachheit aus dem Anteil von
  Defektkanten eines Tetraedernetzes ab (WK4). Falls Lambda bei Kleinert vorkommt, dann als Zusatzterm, nicht als Zaehlung.
- **Ausgang F5 (07:15:17): WK4-Kern bestaetigt, H4-Lesart verletzt.** 7 Treffer (2 fachfremd: Kutinait, SymmCD).
  - Keine Arbeit leitet Lambda oder Flachheit aus dem Anteil von Defektkanten ab (Suche ueber alle Jahre, sortiert, das
    24-Monats-Fenster ist mit 4 Treffern aus 2025 abgedeckt). Naechster Treffer 2509.01635 (Sept. 2025) [S Abstract]:
    umgekehrte Richtung, Lambda regularisiert den Kern einer 2D-Disklination in 2+1 D; Lambda > 0 gibt einen kompakten
    Raum mit positiver Kruemmung. Kein Zaehlargument.
  - Kleinert-Linie: Jizba/Kleinert/Scardigli 2010 (0912.2253): Unschaerfe auf dem Weltkristall (Gitterabstand ~ Planck);
    kein Lambda.
  - **Verletzt (H4):** 1209.2155 (2012) [S Abstract] beschreibt Kleinerts Weltkristall mit einer **neuen Eichsymmetrie**:
    "Einstein's gravitation has a zero torsion as a special gauge, while a zero connection is another equivalent gauge with
    nonzero torsion which corresponds to ... teleparallelism. Any intermediate choice ... is also allowed." Erwartet hatte
    ich nur "Versetzung = Torsion". Korrektur: Die 4 freien Weitzenboeck-Rahmendrehungen aus TORSION-STEIF-1 sind in Kleinerts
    Bild zuerst **Kandidaten fuer Eichrichtungen** (Torsion gegen Kruemmung verschiebbar), nicht automatisch physikalische
    Versetzungen. Zusammen mit Kleinert/Zaanen (F1: Versetzungen kondensiert, Torsion unsichtbar) ist "Energie null" genau
    das, was dieses Bild erwartet [ES].

### F6 (Abruf 6 von 8), 07:15:27 (date): arxiv.org PDF 1203.3591 (Ambjorn/Goerlich/Jurkiewicz/Loll 2012, Phys. Rep. 519, 127), lokal per pdftotext
- Erwartung: Fuer gleichseitige Simplexe wird die Regge-Wirkung eine Zaehlung: 4D EDT S = k4 N4 - k2 N2 (bzw. k0 N0);
  3D S = k3 N3 - k0 N0 (bzw. k1 N1); CDT mit N0, N4^(4,1), N4^(3,2) und Delta. Die nackte kosmologische Kopplung k4 muss
  auf ihren kritischen Wert k4^c abgestimmt werden, damit N4 gegen unendlich geht; die renormierte kosmologische Konstante
  folgt aus dem Abstand k4 - k4^c. Ein "Anteil an 6er-Kanten" kommt nicht vor, wohl aber das Verhaeltnis N0/N3 bzw. N2/N4.
- **Ausgang F6 (07:16:24): Erwartung bestaetigt und uebertroffen; fuer H1 der groesste Verstoss gegen die Karte.**
  - Abschn. 2.5 [S]: Fuer jede Dimension "the action becomes simple, depending only on the global number of simplices and
    (d - 2)-subsimplices".
  - Gl. (70) [S], 3D, alle Tetraeder gleichseitig: S_E = -2 pi kappa N1 + N3 (6 kappa arccos(1/3) + (sqrt 2/12) lambda),
    dazu Gl. (71) N0 - N1 + N3 = 0. "One recognizes arccos 1/3 as the dihedral angle of an equilateral tetrahedron, and
    the term 2 pi N1 as coming from the 2 pi which enters in the definition of the deficit angle". **Der Einstein-Term
    verschwindet genau fuer N1/N3 = 6 arccos(1/3)/(2 pi), also q = 5,1043, also f6 = 10,43 %, wenn nur 5er- und 6er-Kanten
    vorkommen [M aus S]. H1 Teil 1 ist Gl. (70).**
  - Gl. (73) [S]: 4D CDT S_E = -(k0 + 6 Delta) N0 + k4 (N4^(4,1) + N4^(3,2)) + Delta (...); k4 wird auf den kritischen
    Wert k4(k0, Delta) gesetzt (S. 32).
  - Abschn. 7.1, S. 68 [S]: "The cosmological-constant term contributes at the same leading order as the entropy (the
    number of triangulations with a given number N4 of four-simplices) ... the exponential growth defines a critical point,
    to which one has to fine-tune the bare cosmological constant ... the renormalized, physical cosmological constant is
    defined by this approach to the critical value". 2D: lambda = lambda_c + Lambda a^2 (Gl. 114, 127) [S].
  - **Korrektur der Erwartung (protokolliert):** "Lambda als Abzaehlproblem" ist in DT/CDT nicht nur eine Lesart, sondern
    die Definition: Die physikalische Lambda ist der kleine Abstand der nackten Kopplung von der Entropieschwelle der
    Zaehlung. Neu waere hoechstens die Sprache "Defektanteil f6" und die Bruecke zu Frank-Kasper/Nelson.

### F7 (Abruf 7 von 8), 07:16:24 (date): arXiv-API, all:"statistical honeycomb" OR (abs:Coxeter AND abs:foam)
- Erwartung: 0 bis 5 Treffer; mindestens einer nennt Coxeters statistische Wabe mit 5,104 Kanten je Flaeche bzw.
  Tetraedern je Kante und 13,4 Flaechen je Zelle (Schaum-Dual). Kein Kosmologie-Bezug.
- **Ausgang F7 (07:18:03): Erwartung verletzt (0 Treffer).** Coxeters statistische Wabe ist auf arXiv unter diesen Stichworten
  nicht zu finden. q = 5,1043 und Z = 13,397 bleiben [M] mit Zuschreibung [L] (Coxeter 1958, Illinois J. Math. 2, 746;
  Nelson/Spaepen 1989). Korrektur: Im Dossier nicht als [S] fuehren.
- **Nachlese in F6 (keine neue Abrufzahl), 07:18:03:** AGJL 2012, S. 83 [S]: 4D-EDT hat bei kappa0 = 0 (feste N4, "no action,
  but only the entropy") die "crumpled phase": "a few links and their vertices acquire a very high order, such that they
  are shared by almost all four-simplices"; "These 'crumpled' triangulations are the generic, entropically preferred
  triangulations." Mit wachsendem kappa0 folgt ein Phasenuebergang erster Ordnung zu verzweigten Polymeren (Fussnote 19).
  **Bedeutung fuer H1 [ES]:** Reine Zaehlung (Entropie) waehlt nicht von selbst den flachen Mittelwert, sondern Knaeuel.
  Die "Zufalls-Restschwankung ~ N^-1/2" setzt voraus, dass der Mittelwert schon abgestimmt ist.

### F8 (Abruf 8 von 8, letzter), 07:18:03 (date): arXiv-API, abs:unimodular AND (Regge OR simplicial OR triangulation(s) OR polytope OR "600-cell"), nach Datum
- Erwartung: Gielen/Ried 2026 als einzige Regge-Arbeit mit unimodularer Zeit; daneben unimodulare Varianten von CDT,
  Spinschaum oder Gruppenfeldtheorie (z. B. Lambda als Volumen-Konjugierte). **Kein** 600-Zellen-Modell mit unimodularer
  Zeit im 24-Monats-Fenster.
- **Ausgang F8 (07:19:27): im Kern bestaetigt, Abdeckung unvollstaendig.** 50 juengste Treffer (bis 2025-06-24 zurueck): einziger
  Gravitations-Treffer ist Gielen/Ried, "Unimodular boundary time for Regge calculus" (2026-10-02). Alle anderen 49 sind
  Kombinatorik ("unimodular triangulations", Ehrhart). **Ein 600-Zellen-Modell mit unimodularer Zeit ist im Fenster
  2025-06-24 bis 2026-10-05 nicht belegt; das Teilfenster 2024-10 bis 2025-06 ist durch diese Abfrage nicht abgedeckt.**
  Abrufbudget damit erschoepft (8 von 8).

### L2 (lokal, kein Netzabruf), 07:22:55: Doye/Wales 2001 (cond-mat/0012333, Text in RUNDE-17/quellen-frustration/hilfs/p11)
- Erwartung (vor dem Lesen notiert, 07:20): nennt FK-Phasen als geordnete Disklinationsnetze (schon im Projekt, R17).
- **Ausgang: Erwartung uebertroffen (Verstoss gegen die Projektlage).** S. 3 [S]: "There are two bulk Frank-Kasper phases
  that involve such networks, the C14 and C15 phases. In the C15 phase the disclination network has the structure of the
  diamond lattice and in the C14 phase the wurtzite structure." Projekt-grep (*.md): Diamant + Disklination nicht
  gefunden. [L] Im C15-Prototyp MgCu2 bilden die Cu-Atome eckverknuepfte Tetraeder (Pyrochlor), die Mg-Atome ein
  Diamantgitter. **Finns Diamant-/Pyrochlor-Netz ist im flachen Raum das Defektgeruest der geordnet "geplaetteten"
  600-Zelle (C15).**

## 4. Schreibtisch zu H2 (nach den Abrufen) [M, Kopfrechnung]

- **D1 Zehnecke:** Rechte Nebenklassen x C10_q in 2I (q 5-zaehlige Achse): 120/10 = 12 Grosskreis-Zehnecke (Kante = 36 Grad
  Bogen, 1/phi Sehne). Hopf-Bild x q x^-1 = I-Bahn von q = 12 Punkte = Ikosaeder-Ecken.
- **D2 Faser-invarianter Sektor (s = 0):** In Niveau rho x rho* ist die Zahl der rechts-C10-invarianten Funktionen
  dim(rho) x (Vielfachheit des Gewichts 1). Gewichte von g = e^(q pi/5) im Spin j: e^(i m 2 pi/5); Gewicht 1 nur fuer
  m = 0, also nur ganzzahliges j. Ergebnis: k = 0: 1, k = 2: 3, k = 4: 5, Niveau 3': 3 (Galois-Bild von Spin 1),
  k = 1, 3, 5, 4', 2': 0. Summe 12 = Zahl der Zehnecke. Probe bestanden.
- **D3 Quotient = Ikosaeder, Laplace verdoppelt:** Ikosaeder-Graph: Adjazenz 5, sqrt 5, -1, -sqrt 5 (1, 3, 5, 3) [L],
  Laplace 0, 5 - sqrt 5, 6, 5 + sqrt 5. Mal 2: 0; 5,5279; 12; 14,4721. ZELLE600-1 [P]: Niveaus 0; 5,52786 (k = 2);
  12 (k = 4); 14,47214 (3'). **Exakt gleich.** Mit allgemeinem ikosaedrischem Ansatz (Gewichte w1 Nachbarn, w2 zweite
  Nachbarn, w3 Gegenpunkt) erzwingen die drei Eigenwerte w1 = 2, w2 = 0, w3 = 0: Jede Ecke hat 2 Nachbarn auf ihrem eigenen
  Zehneck und je 2 auf den 5 benachbarten Zehnecken (2 + 5 x 2 = 12).
- **D4 Fock gegen KS:** Die n^2-Schalen (Grad k = n - 1) sind Focks S^3. Die ungeraden Schalen n = 2, 4, 6 haben keinen
  s = 0-Anteil. In KS liegt Wasserstoff im s = 0-Sektor mit Graden 0, 2, ..., 2(n - 1) und braucht den Radius; auf einer
  einzigen S^3-Schale bleibt davon nur der Winkelteil l = 0, 1, 2 (+ Bruchstueck l = 3 als 3' aus Grad 6, passend zu
  "3' aus Grad 6 gefaltet" in ZELLE600-1). **Die 600-Zelle ist eine diskrete Fock-Kugel, keine KS-Bruecke; als Hopf-Bild
  liefert sie nur den Winkelteil (Ikosaeder) und eine Z10-Faser (Faserladung nur modulo 10 definiert).**
- **D5 Ringe:** ZELLE600-1: 20 Linkstranslate eines Rings sind disjunkt -> Links-Stabilisator Ordnung 6 (in 2I gibt es
  nur C6 dieser Ordnung) -> Achse 3-zaehlig. Lesart "12 disjunkte Rechtstranslate" -> Rechts-Stabilisator C10_q.
  Dann sind die 20 Ringe Roehren um 20 Fasern derselben rechten q-Faserung, Basis = I-Bahn einer 3-zaehligen Richtung =
  20 Dodekaeder-Ecken = Flaechenmitten des Ikosaeders. Jeder Ring = 3 Zehnecke (die drei Ecken seiner Ikosaederflaeche),
  30 Ecken; jedes Zehneck in 5 Ringen (12 x 5 = 20 x 3). [M, haengt an der Lesart "Rechts-Stabilisator C10"; nicht
  gegengerechnet.]

## 5. Schreibtisch zu H1 (Ergaenzung) [M]

- **D6 Irrationalitaet:** Summe_e delta_e = 2 pi N1 - 6 theta N3 = 0 verlangt theta/pi = N1/(3 N3) rational. Nach Niven
  ist arccos(1/3)/pi irrational (cos rational und Winkel rationales Vielfaches von pi nur fuer 0, +-1/2, +-1) [L-Satz].
  **Kein endliches oder periodisches Netz regulaerer Tetraeder ist im Mittel exakt flach;** f* = 0,10430... ist irrational.
  Periodische FK-Phasen haben rationale q: A15 46/9 = 5,1111 (Z = 27/2), C15 51/10 = 5,1000 (Z = 40/3) [M aus Z-Werten L].
  Sie liegen beidseits von q* = 5,1043 und sind verzerrt (flacher Raum, Spannung statt Kruemmung).
- **D7 Probe 600-Zelle in DT-Form:** N0 - N1 + N3 = 120 - 720 + 600 = 0 (Gl. 71) [P, S]. N0/N3 = 0,2 > 0,1755 (flach),
  also positiv gekruemmt, richtiges Vorzeichen [M].
- **D8 Regel 6 (drei Wege zu "Lambda klein"):** (1) nackte Kopplung an die Entropieschwelle abgestimmt (DT/CDT, AGJL 7.1);
  (2) Schwankung ~ V^-1/2 bei abgestimmtem Mittel (everpresent); (3) Integrationskonstante, konjugiert zur 4D-Volumenzeit
  (Henneaux/Teitelboim, Gielen/Ried). **Gemeinsame Groesse: das 4D-Volumen bzw. die Zahl N4 der 4-Simplexe.** H1 und H3
  haengen an derselben Kopplung Lambda <-> N4 ("Finns Takt zaehlt Volumen") [ES].

## 6. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 **geprueft:** Dass der Fasersektor der 600-Zelle wirklich das Ikosaeder ist (D2/D3, gegen die Eigenwerte aus ZELLE600-1).
  Bestanden, und die Pruefung ergab zusaetzlich die Nachbarzahlen 2 + 5 x 2.
- G2 **geprueft:** Vorzeichen und Normierung der DT-Form an der 600-Zelle (D7). Bestanden.
- G3 **geprueft (Literatur, F6 S. 83):** Dass reine Zaehlung den flachen Mittelwert waehlt. **Nicht der Fall:** Entropie
  bevorzugt Knaeuel (crumpled). Die everpresent-Form setzt einen abgestimmten Mittelwert voraus.
- G4 nicht geprueft: Dass die 4 Nullmoden aus TORSION-STEIF-1 genau Kleinerts "neue Eichsymmetrie" sind (Kleinert 2010
  nicht abgerufen; Budget).
- G5 nicht geprueft: Dass H1 "Lambda" und nicht "Omega_k" meint. Die Karte sagt "Lambda bzw. Flachheit". Ein 3D-Netz misst
  Omega_k; Lambda ist 4D (M5). Im 4D-Fall ist das Ideal mit 5 Simplexen je Dreieck hyperbolisch ({3,3,3,5}, KEGEL-4D-L [P]).
- G6 nicht geprueft: die Lesart "Rechts-Stabilisator C10" fuer D5.

## 7. Berichtigungen (07:24:23, date)

- **B1 (Selbstanzeige):** Bei L2 steht "Erwartung (vor dem Lesen notiert, 07:20)". Das ist ~~vor dem Lesen notiert~~
  **falsch:** Ich habe Doye/Wales um ca. 07:20 gelesen und die Erwartung erst um 07:22 in diese Datei geschrieben. Die
  Erwartung war nur im Kopf vorher. Der Ausgang (C15 = Diamant) bleibt ein Verstoss gegen die Projektlage, aber nicht
  gegen eine protokollierte Erwartung.
- **B2 (Zwei Zahlen, dasselbe?):** "Delta = +0,0043" in R17/R22 ist eine Energiedifferenz (zwei Ikosaeder gekoppelt),
  nicht f* - f6(C15) = 0,1043 - 0,1000 = 0,0043. Gleiche Ziffern, andere Groesse. Keine Verbindung ziehen.

## 8. Stand vor dem Dossier (07:24:23)

- Abrufe 8 von 8 verbraucht. Dossier folgt in DOSSIER.md.
- **B3 (07:29:11):** M6 (Abschn. 1) nennt "~33 Groessenordnungen" und "Omega_k ~ 1e30". Mit Vorfaktoren nachgerechnet
  (Streuung 0,377 rad je Kante, N1 ~ 2,6e184, sigma_R ~ 5e-92 l_P^-2): Omega_k ~ 6e29 gegen < 2e-3, also **rund 32**
  Groessenordnungen. Das Dossier fuehrt 32. ~~33~~ ist ueberholt (Groessenordnung unveraendert).
- **B4 (07:29:11):** DN-Begruendung im Dossier nachgeschaerft: Das l = 6-Verbot durch Eichinvarianz ist in R45 selbst [M].
  Abgrenzung zu DANZER ergaenzt.

## 9. Abschluss (07:29:11, date)

- DOSSIER.md geschrieben ab 07:24:23, letzte Aenderung 07:29:11. Abrufe 8 von 8. Keine Rechnung, kein Journal, kein Peerbus.
