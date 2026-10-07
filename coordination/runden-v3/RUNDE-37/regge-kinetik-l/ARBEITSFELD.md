# REGGE-KINETIK-L: Arbeitsfeld (feldforscher fuer claude-primary)

- Start 2026-10-05 09:35:24 CEST (date). Karte KARTE.md gelesen 09:35. Vorarbeiten gelesen bis 09:41:19 (date).
- Regel: Vor jedem Netzabruf Erwartung mit Zeit (date) hier; Gestrichenes bleibt stehen (~~...~~), offene Fragen wandern mit.
- Kennzeichen: [E] [M] [S] [L] [H] [P] [ES].

## 0. Was ich aus den Vorarbeiten mitnehme [P]

- Bewegungsenergie im Code (ew.py) wirkt auf Impulse: x' = A p / kappa_g (IMPULS-NETZ-1 4.2). Je Tetraeder
  A0_ef = (n_e.n_f)^2 - 1/2 = G(n_e n_e, n_f n_f), G(X,Y) = X:Y - 1/2 trX trY. Das ist die Impuls-DeWitt-Form in 3D
  (Koeffizient 1/(d-1) = 1/2, RUNDE-36 REGEL.md Z. 29). Gewicht J_t je Tetraeder (A1: J = 1; A2: J_t V_F/V_t).
- Eichung: Eckverschiebungen M, B M = 0 (flach exakt), M^H p erster Klasse. Skalare Regel c: Paar zweiter Klasse
  (delta R^(3) = 0 je Ecke plus c^H p = 0), GAMMA-NETZ-L ueber SKALAR-SEKTOR-L 4.
- R1: p senkrecht auf Bild [M, c] (euklidisch), q auf P = Komplement (TT-GLAS-2 Begriffe; IMPULS-NETZ-1 4.1).
- TT-GLAS-2: Spanne sitzt in der Bewegungsenergie; mit isotroper A3 bleibt ~Haelfte, "aus der Projektion auf P";
  unprojiziert 0,00 %. Projektionsanteil der affinen Welle 0,40 bis 0,53.
- TAKT-DYNAMIK-1: Delta V = 0 beim 2-3-Zug [M]; Sprung in der Bewegungsenergie 0,2 bis 0,46 % H0 je Zug; Lesart R
  verliert, Lesart P gewinnt; "Was fehlt: eine Regel, die die Energie am Zug erhaelt".
- SKALAR-SEKTOR-L 5.4: Ursache des Spur-Eichdefekts laut GAMMA-NETZ-L: Bewegungsenergie "gesetzt und nicht aus einer
  4D-Wirkung abgeleitet" [P].
- Projekt-grep 09:40 (Ausschluesse gesetzt): Lund/Regge, Hartle/Miller/Williams, Piran/Williams, Friedman/Jack
  im Projekt nicht gelesen (nur DeWitt-1/2 in RUNDE-36). Bestaetigt die Karte.

## 1. Schreibtisch vor dem Netz (Bausteine verketten)

### 1.1 Ist eine Hamilton-Reduktion mit M^H p = 0 schon horizontal? [M, vorab ableitbar]

- Lineares System H = 1/2 p^H A p + 1/2 q^H B q, A positiv definit, B M = 0, Impulsbedingung M^H p = 0.
- Physikalische Frequenzen: p'' = -B A p auf ker M^H; Bild B liegt in ker M^H (M^H B = 0). Keine Eichflaeche noetig.
- S orthonormale Basis von (Bild M)^perp = ker M^H. R1-artig: p = S y, q = S x. Dann
  S^H B A S = S^H B (S S^H + P_M) A S = (S^H B S)(S^H A S), weil B P_M = 0. Also gleiche Eigenwerte wie das
  eichfreie Problem. Die Wahl der q-Flaeche (euklidisch) aendert die Frequenzen nicht.
- Identitaet: (S^H A S)^-1 = S^H Q S mit Q = A^-1 - A^-1 M (M^H A^-1 M)^-1 M^H A^-1 (horizontale Geschwindigkeits-
  metrik). Beweis: (S^H Q S)(S^H A S) = S^H Q (1 - P_M) A S = S^H Q A S = S^H S - S^H A^-1 M (...) M^H S = 1,
  weil Q M = 0 und M^H S = 0.
- **Folge [ES]:** Bezueglich M ist die Hamilton-Reduktion mit Impulsbedingung automatisch die horizontale. Ein
  Eichflaechen-Artefakt kann nur aus dem Teil c kommen (zweite Klasse, B c != 0): Dort haengt das Ergebnis an der
  Partnerbedingung fuer q. Pruefen, wie R1 den c-Teil behandelt (Code lesen, nicht rechnen), erst nach der Literatur.
- Offen: Gilt das auch fuer R2 (TT-GLAS-2 (c))? Und behandelt R1 c mit derselben euklidischen Flaeche fuer p und q?

## 2. Erwartungen und Abrufe (je Abruf: Zeit, Erwartung, Ausgang)

### F1 (Erwartung 09:41:52): arXiv-API, Sammelabruf Abstracts (IDs aus dem Gedaechtnis [L], Titel pruefen)
- gr-qc/9609028 Hartle/Miller/Williams 1997: Lund-Regge-Supermetrik als diskretes DeWitt-Analogon auf Quadrat-
  Kantenlaengen; Signatur bei "dicken" Geometrien kleiner S^3-Triangulierungen Lorentz (eine negative Richtung),
  sonst mehr. Ob volumengewichtet: erwartet ja (Integral ueber flache Tetraeder), im Abstract vermutlich nicht.
- 1108.1974 Dittrich/Hoehn 2012: Evolving phase spaces, Pachner-Zuege, Vor-/Nachbedingungen; Symplektik bleibt auf
  dem reduzierten Raum erhalten; Eckverschiebung flach Eichung. Zur Energie: kein Wort (kein erhaltenes H).
- 1303.4294 Dittrich/Hoehn 2013: Klassen von Bedingungen; erste Klasse nur bei echter Symmetrie.
- 1411.5672 Hoehn 2015: linearisiertes kanonisches Regge mit Pachner-Zuegen; 1-4 bringt Lapse/Shift-Eichung
  (erste Klasse flach); Gravitonen-Zaehlung.
- 1109.2530 Hamber/Williams 2011: diskrete WDW-Gleichung mit Lund-Regge-Supermetrik, Formel im Volltext.
- 1407.6641 Hoehn 2014 (quadratische Wirkungen), 0912.1817 Dittrich/Hoehn 2010, gr-qc/9411008 Barrett u. a. 1997,
  gr-qc/0408006 Gentle 2002: Einordnung; Barrett u. a.: Sorkin-Schema, fast abhaengige Gleichungen je Ecke.
- **Ausgang F1 (09:42:08, Abrufe 2 von 15; F1a leer mitgezaehlt):**
  - HMW 1997 [S Abstract] **verletzt die Erwartung dreifach:**
    1. Die Lund-Regge-Metrik liefert laut Abstract den kuerzesten Abstand zwischen simplizialen Dreigeometrien
       unter allen Eichwahlen im Inneren der Simplizes (Regge-Eichfreiheit). Sie ist also selbst eine Minimierung
       ueber Eichwahl, aber ueber die Eichung **innerhalb** der Simplizes, nicht ueber Eckverschiebungen.
    2. Nahe flacher Metriken gibt es raumartige Richtungen, die zur Eichfreiheit der Kantenlaengen gehoeren:
       Die Eckverschiebungen sind dort **positive** Richtungen der Supermetrik.
    3. T^3 nahe flach: Entartungen, und einige negative Eigenwerte sind physikalisch (keine Diffeomorphismen).
       S^3 (Rand des 4-Simplex): genau eine zeitartige Richtung. Mindestens eine physikalische zeitartige Richtung immer.
    (Zitate hier nach 10:00:35 (date) in Umschreibungen umgewandelt, Urheberrechtsregel: hoechstens ein Zitat je Quelle; Inhalt gleich.)
    - Korrigierte Erwartung: Signatur nicht "eine negative Richtung je Ecke" aus Eichung; Zahl der negativen
      Richtungen auf T^3 im Volltext lesen (F2). Volumengewichtung im Volltext lesen.
  - Dittrich/Hoehn 2012 [S Abstract]: Pachner-Zuege als "canonical transformations on naturally extended phase
    spaces"; a priori freie Daten, spaeter durch Bedingungen fixiert. Wie erwartet, eine Zeile.
  - Dittrich/Hoehn 2013 [S Abstract]: Erhalt bzw. Nicht-Erhalt von Bedingungen und Symplektik wird dort eigens
    behandelt. **Teilverstoss:** Erhalt der Symplektik ist nicht bedingungslos. Wo genau: offen (Volltext, falls Budget).
  - Hoehn 2015 [S Abstract]: 1-4 erzeugt vier Lapse/Shift-Variablen und vier Eckverschiebungs-Generatoren; 2-3 erzeugt
    ein "Graviton"; 3-2 entfernt eines und liefert die einzige nichttriviale Bewegungsgleichung; 4-1 entfernt Lapse/
    Shift; "Pachner moves preserve the vertex displacement generators". Wie erwartet (Regime K, diskrete Zeit).
  - Dittrich/Hoehn 2010 [S Abstract]: linearisiertes Regge flach: lokale Bedingungen erster Klasse fuer beliebige
    triangulierte Cauchy-Flaechen; hoeher: Pseudo-Bedingungen. Wie erwartet.
  - Hoehn 2014 (quadratisch) [S Abstract]: auf zeitlich variierender Diskretisierung werden Bedingungen, Observablen,
    Symmetrien und reduzierte Phasenraeume regionsabhaengig. Wie erwartet.
  - Barrett u. a. 1997, Gentle 2002 [S Abstract]: Sorkin-Schema, Bianchi-Bezug; Gentle: Brill-Wellen in Regge
    entwickelt (Schwerewellen-Rechnung existiert, Isotropie nicht genannt). Hamber/Williams 2011: Formel nicht im Abstract.

### F2 (Erwartung 09:42:50): arXiv-PDF gr-qc/9609028 (HMW 1997 Volltext)
- Formel: G^{mn}(s) proportional zu -Summe_tau (1/V_tau) d^2(V_tau^2)/ds_m ds_n, also Summe ueber Tetraeder der
  DeWitt-Form mit Volumen (volumengewichtet), Lapse konstant je Tetraeder; Konstante 1/8 oder 1/16.
- Herleitung aus DeWitt mit Lapse/Shift innerhalb jedes Simplex; Minimierung ueber die innere Eichung.
- T^3 nahe flach: Zahl der negativen Richtungen etwa gleich der Ecken- oder Tetraederzahl; Eckverschiebungen
  positiv (schon aus F1), Entartungen aus flacher Geometrie.
- **Ausgang F2 (gelesen bis 09:46:06; Abruf 3 von 15), HMW 1997 Volltext [S, Seiten = PDF-Seiten]:**
  - Kontinuum (S. 4, Gl. 2.1, 2.2): (k', k) = Int d^3x N(x) G^abcd k'_ab k_cd mit
    G^abcd = 1/2 h^(1/2) [h^ac h^bd + h^ad h^bc - 2 h^ab h^cd]; Signatur je Punkt (-,+,+,+,+,+). Mit N = 1 gerechnet.
  - Horizontal (S. 5, Gl. 2.3 bis 2.5): vertikal = D_(a xi_b); horizontal = orthogonal dazu; Konvention: das Minimum
    der Abstaende waehlen, Eichbedingung D^b (k_ab - h_ab k^c_c) = 0. Konstante konforme Verschiebung ist horizontal und negativ.
  - Lund-Regge (S. 7, Gl. 3.4, 3.5): Regge-Eichung dh_ab konstant je Tetraeder; G_mn dt^m dt^n =
    Summe_tau V(tau) {dh_ab dh^ab - (dh^a_a)^2}. Also **volumengewichtet, Geschwindigkeitsseite, Spurkoeffizient 1**.
    dh aus Quadrat-Kantenlaengen: h_ab = 1/2 (t_0a + t_0b - t_ab) (3.6, 3.7).
  - Geschlossen (S. 8, Gl. 3.13): G_mn = - Summe_tau (1/V) d^2 V^2 / dt^m dt^n; (S. 9, Gl. 3.14):
    G_mn = -2 [d^2 V_TOT/dt^m dt^n + Summe_tau (1/V) dV/dt^m dV/dt^n].
  - S. 9/10: extremal nur gegen Umeichungen im Inneren der Tetraeder; "not exactly 'horizontal' in the sense of
    the continuum" (S. 10), Grund: simpliziale Diffeomorphismen (Eckverschiebungen).
  - S. 10/11 (3.19 bis 3.23): konforme Richtung immer zeitartig (G t t = -6 V_TOT); orthogonal zu jeder Eichrichtung;
    G = G~ - 4 Summe (1/V) dV dV mit G~ >= 0, also mindestens n1 - n3 raumartige Richtungen. [ES] Damit hoechstens
    n3 negative Richtungen, und sie liegen im Spann der Tetraedervolumen-Gradienten.
  - S. 11/12 (3.30): Eckverschiebungs-Moden: Vorzeichen allgemein offen; S. 18 bis 20: auf dem T^3-Gitter positiv in
    Sonderfaellen (einzelne Ecke: dS^2 = 8 dr^2), Eigenwert 1/2 = Diffeomorphismus bis eps^3, 6n - 4 davon.
  - S. 14: Rand des 4-Simplex (S^3): (-,+,...,+) ueberall (102 160 Punkte, Seitenverhaeltnis bis 10:1).
  - S. 21: T^3 3x3x3 (27 Ecken, 189 Kanten, 162 Tetraeder), flach und nahe flach: 176 positive, 13 negative;
    keine der 13 ist Diffeomorphismus, also 13 horizontale negative Richtungen; nahe flach Signaturwechsel und Null-
    Eigenwerte. S. 22 Abb. 4: 33 Gitter bis 6x6x7 (252 Ecken), 10 % Zufallsstoerung: negativ/positiv 0,074 bis 0,123.
    600-Zelle (vorlaeufig): 628 positiv, 92 negativ.
  - S. 22/23: Zukunft: naeherungsweise Begriffe von vertikal und horizontal im simplizialen Konfigurationsraum
    definieren; 3 n0 naeherungsweise Diffeomorphismen ueber einen Shift-Vektor je Ecke (Miller 1986; Kheyfets/Miller/
    Wheeler 1988).
  - **Erwartungsverstoesse F2:**
    - V-a: Die Standard-Form ist eine **Geschwindigkeits**-Metrik (Summe V {dh:dh - (tr dh)^2}). Unser Code legt eine
      lokale DeWitt-Form auf die **Impulse** (Spurkoeffizient 1/2). Je Tetraeder sind beide zueinander invers; die Summe
      ueber geteilte Kanten aber nicht: inv(Summe V G_v) != Summe (1/V) G_p. [ES]
    - V-b: Negative Richtungen: nicht "eine je Ecke", sondern auf T^3 13 bei 27 Ecken (0,48 je Ecke), 92 bei 120 Ecken
      (600-Zelle, vorlaeufig), 1 bei 5 Ecken (S^3). Schranke: hoechstens n3 (Tetraederzahl). Sie haengen an
      Volumenaenderungen der Tetraeder (3.23), nicht an Ecken.
    - V-c: Die Autoren selbst nennen die Lund-Regge-Metrik nicht horizontal gegen Eckverschiebungen und die horizontale
      Reduktion eine offene Aufgabe (1997). Zaehlt fuer RK4 (Gegenrichtung).
- **Neue Kette [ES, vorab ableitbar, nicht gerechnet]:** Bei der Lund-Regge-Form (Geschwindigkeitsseite) ist der
  Mittelwert der Verzerrungsrate ueber die Doppelpyramide in beiden Zerlegungen gleich (Randintegral ueber dieselben
  6 Aussenflaechen der P1-Geschwindigkeit). Der Energiesprung beim 2-3-Zug ist dann nur die Differenz der Schwankungs-
  anteile; null, wenn die Eckgeschwindigkeiten auf der Doppelpyramide affin sind. Bei kl ~ 1,5 (TAKT-DYNAMIK-1) ist das
  keine kleine Groesse. Gegen HM4 (< 1e-4 H0) spricht das eher [H].
- **Weitere Kette [ES]:** Lund-Regge-Form = DeWitt-L2-Masse der Regge-Finite-Elemente niedrigster Ordnung (stueckweise
  konstante Metrik). Pruefen, ob es Konvergenz-/Spektralaussagen fuer linearisiertes Regge auf unstrukturierten Netzen
  gibt (Christiansen 2011?). Waere fuer RK5 ein Baustein.

### F3 (Erwartung 09:46:33): OpenAlex, Werke 1986 mit "Regge calculus" im Titel, mit Abstract
- Piran/Williams 1986 (PRD 33, 1622): 3+1-Regge mit Lapse- und Shift-Kanten ("struts") je Ecke; Gleichungen der
  Struts = Analoga von Hamilton-/Impulsbedingung; frei waehlbar; Erhaltung nicht exakt.
- Friedman/Jack 1986 (JMP 27, 2973): stetige Zeit, Lund-Regge-Supermetrik als Bewegungsenergie; Titel sagt "with
  conserved momentum and Hamiltonian constraints": erhalten nur mit besonderer Wahl bzw. Abaenderung (z. B. Shift
  oder Lapse je Tetraeder statt je Ecke). Abstracts in OpenAlex evtl. fehlend.
- **Ausgang F3 (09:46:53; Abruf 4 von 15), Abstracts aus OpenAlex (abstract_inverted_index, mit jq zusammengesetzt) [S Abstract]:**
  - Piran/Williams 1986: 3+1-Regge-Wirkung fuer allgemeine Raumzeiten nach Lund/Regge, erster und zweiter Ordnung;
    Anfangswertproblem ueber konforme Transformationen; zwei Modelluniversen. Lapse/Shift-Behandlung nicht im Abstract.
  - Friedman/Jack 1986 (JMP 27, 2973; DOI 10.1063/1.527224): Einstein-Wirkung fuer stueckweise flache Dreimetriken
    gibt die Lund-Regge-Wirkung. "the constraints are not conserved if the lapse and shift are chosen a priori"
    (Gegensatz zum Kontinuum). Mit Shift != 0 und nicht konstanter Lapse bleiben sie erhalten; Hamilton-Formalismus
    ueber Bergmann-Dirac oder durch algebraisches Loesen der Bedingungen nach Lapse und Shift je
    Drei-Simplex. Bei Shift = 0: Summe freier relativistischer Teilchen (eins je Tetraeder), gekoppelt ueber
    gemeinsame Koordinaten (Kantenlaengen).
  - **Erwartungsverstoss V-d:** Lapse und Shift sitzen bei FJ **je Drei-Simplex**, nicht je Ecke; die Erhaltung der
    Bedingungen wird erkauft, indem Lapse/Shift aus den Bedingungen bestimmt werden (Multiplikatoren festgelegt, also
    der Sache nach zweite Klasse [ES]). Korrigierte Erwartung: Im Regime "stetige Zeit, Lund-Regge" gibt es keine
    erste Klasse fuer die Hamilton-Bedingung; das passt zu unserem Paar zweiter Klasse (GAMMA-NETZ-L [P]) und zum
    Spur-Eichdefekt (TT-ISO-1 [P]) als Eigenschaft des Regimes, nicht nur unseres Codes [ES].
  - RK2 nach Abstract: "nicht exakt erhalten bzw. brauchen Abaenderungen" trifft (FJ wortgleich in der Sache).
  - Williams 1986 ~~(CQG 3, 1045?)~~ (CQG 3, DOI 10.1088/0264-9381/3/5/015; Seitenzahl geraten, gestrichen): Lorentz-Quanten-Regge, inverser Propagator, ADM-Variablen ~ Regge-Variablen.
    Porter 1987: eigener 3+1-Ansatz. Je eine Zeile.

### F4 (Erwartung ~~09:47:57~~ geschaetzt, gestrichen; date direkt nach dem Schreiben: 09:47:54): arXiv-API-Suche linearisiertes Regge / Regge-Elemente x (random, irregular, unstructured, isotropy, eigenvalues, graviton, waves)
- Treffer: Christiansen ("On the linearization of Regge calculus", Spektralkonvergenz auf allgemeinen Netzen, 3D),
  Gawlik/Neunteufel/Li zu Regge-Elementen und Kruemmung (2020 bis 2025), Dittrich u. a. Gravitonen auf
  hyperkubischen Gittern (Flaechen-Regge, effektive Spinschaum). Ausdrueckliche Isotropie-Studie langer Gravitonen
  auf unregelmaessigen Regge-Netzen: keine (RK5 eher verfehlt bzw. nur indirekt ueber Konvergenz).
- **Ausgang F4 (09:47:55; Abruf 5 von 15): Fehlschlag im Suchdesign.** 16 Treffer, alle Hadronen-Regge-Theorie
  (Regge-Trajektorien, Holographie). Die Phrasensuche griff nicht. Kein Inhaltsbefund; RK5 bleibt offen.
  Lehre: Wortsuche mit "calculus"/"simplicial" statt Phrase.

### F5 (Erwartung, Zeit = date-Zeile direkt davor im Protokoll ABRUFE F5): arXiv-API Wortsuche Regge AND calculus AND (linearized|weak) AND (graviton|random|irregular|isotrop*|dispersion|wave*)
- Erwartung wie F4: Christiansen 2011 (falls auf arXiv), Barrett/Williams-Konvergenz (falls), Dittrich u. a.
  Gravitonen auf hyperkubischen Gittern, Hamber/Williams; keine ausdrueckliche Isotropie-Studie auf Zufallsnetzen.
- **Ausgang F5 (09:48:40; Abruf 6 von 15):** 4 Treffer. Hoehn 2015 (schon F1); Asante/Dittrich/Haggard 2018
  (linearisiertes Regge um flachen euklidischen Volltorus, Randgravitonen, Kontinuumsgrenze lokal) [S Abstract];
  Gentle 2002 (Brill-Wellen); Zumbusch 2009 (FE/DG/FD-Zeitschritte, DG "related to Regge calculus", Apples-with-
  Apples-Tests) [S Abstract]. Keine Arbeit zur Richtungsabhaengigkeit langer Gravitonen auf unregelmaessigen Netzen.
  Wie erwartet (eine Zeile). Arxiv-Abdeckung fuer 1980er (Christ/Friedberg/Lee, Feinberg u. a.) fehlt naturgemaess.

### F6 (Erwartung; ~~09:49~~ vorab eingetragen, gestrichen; date direkt nach dem Schreiben: 09:49:08): arXiv-PDF 1303.4294v3 (Dittrich/Hoehn 2013), Stellen zu "symplectic" per pdftotext + grep
- Erwartung: Symplektik bleibt nur auf den Bedingungsflaechen (Vor-/Nach-Bedingungen) modulo Eichrichtungen erhalten;
  auf dem ganzen erweiterten Phasenraum nicht (Dimension wechselt). Energie: kein Begriff, ausser bei
  translationsinvarianten Systemen.
- **Ausgang F6 (09:49:17; Abruf 7 von 15), Dittrich/Hoehn 2013 Volltext [S, Zeilen der pdftotext-Datei, S. = PDF-Seite]:**
  - Satz 3.1 (~~S. 12~~ S. 13, per pdftotext je Seite berichtigt): Die globale Zeitentwicklung H_n: C_n^- -> C_{n+1}^+ ist **kein** symplektischer, sondern ein
    prae-symplektischer Abbildung: (iota_n^-)^* omega_n = H_n^* (iota_{n+1}^+)^* omega_{n+1}.
  - ~~S. 12~~ S. 13 Fussnote 7: Vor- und Nachbedingungen bilden je eine Menge erster Klasse; das zurueckgezogene omega hat je
    Bedingung eine Nullrichtung.
  - Z. 1281 f.: 1-3 (3D) sowie 1-4 und 2-3 (4D Regge) sind Typ I (neue Variablen, keine alten entfernt).
    Z. 1355 f.: 3-1 (3D) sowie 3-2 und 4-1 (4D) sind Typ II (alte Variablen entfernt).
  - Satz 4.1 (S. 25): Impulsaktualisierung h_k erhaelt die Symplektik eingeschraenkt auf die Nachbedingungsflaechen;
    fuer Typ II/III nur auf C_k^+ geschnitten mit der partiellen Vorbedingungsflaeche K_k^-. Folge: Typ II/III
    senken den Rang der Symplektik um zwei je unabhaengiger, nicht zweitklassiger Vorbedingung (S. 40, Abschn.
    5.4.3); Zahl der Nachbedingungen bleibt oder waechst. (~~S. 40~~ S. 41 berichtigt.)
  - Fussnote 13: Der 2-2-Zug in 3D-Regge (Typ III) hat keine nichttrivialen Vorbedingungen.
  - Schluss (~~S. 40 f.~~ S. 41): Eich-erzeugende Bedingungen sind zugleich Vor- und Nachbedingungen, also erster Klasse; es
    gibt aber auch Bedingungen erster Klasse, die "in contrast to the continuum" keine Symmetrie erzeugen.
  - **Teilverstoss V-e (gegen RK3 und meine F6-Erwartung nur im Detail):** Erhalt der Symplektik gilt fuer 1-4 und 2-3,
    fuer 3-2 und 4-1 im Allgemeinen nicht (Rangverlust). Energie kommt im Rahmen nicht vor.
  - **Kette [ES]:** TAKT-DYNAMIK-1 hatte beim 3-2-Zug einen Fehlwinkel auf der wegfallenden Kante (TD0 verfehlt). Im
    4D-Rahmen liefert genau der 3-2-Zug die einzige Bewegungsgleichung (Hoehn 2015 Abstract) als Vorbedingung; ist sie
    nicht erfuellt, geht ein Freiheitsgrad samt Energie verloren. Der Verlust beim 3-2-Zug ist also im Rahmen
    angelegt, nicht nur unser Codefehler. Beim 2-3-Zug (Typ I) entsteht eine a priori freie neue Kante; wir legen sie
    auf Flachheit fest, der Rahmen nicht.

### F7 (Erwartung, geschrieben vor dem Abruf; date folgt): arXiv-PDF 1411.5672v2 (Hoehn 2015), grep nach gauge fixing, horizontal, independent, spectrum, frequency, dispersion, a priori free
- Erwartung: Abelsche Algebra der Eckverschiebungs-Generatoren (erste Klasse, flach), eichinvariante "lattice
  gravitons" als Dirac-Observablen = symplektische Reduktion in diskreter Zeit. Kein Frequenzspektrum, kein
  Nachweis der Eichflaechen-Unabhaengigkeit eines Spektrums, kein "horizontal". Neue Kante beim 2-3-Zug a priori frei.
- **Ausgang F7 (09:50:23; Abruf 8 von 15), Hoehn 2015 Volltext [S, S. = PDF-Seite, Z. = Zeile der .txt]:**
  - ~~S. 14~~ S. 15 (Abschn. 8): Gitter-"Gravitonen" = eichinvariante Kruemmungs-Freiheitsgrade; Bezug zum Kontinuum dort
    ausdruecklich ungeklaert; Dynamik durch die Zuege, waehrend im Kontinuum eine quadratische globale Hamilton-
    Funktion die Gravitonen treibt. Barretts Fundamentalsatz des linearisierten Regge-Kalkuels: Laengenstoerungen
    modulo Eckverschiebungen = linearisierte Fehlwinkel mit Bianchi-Identitaeten (topologisch trivial).
  - Z. 1117 ff., 1237 ff.: Zaehlung 1-4: +4 Eichmoden; 2-3: +1 Graviton; 3-2: -1; 4-1: -4. Der Fehlwinkel um das
    neue Bulk-Dreieck des 2-3-Zugs ist a priori frei.
  - Abschn. 11.2 (S. 22): linearisierter 2-3-Zug: alte Laengen bleiben (y_{k+1} = y_k), Eckverschiebungs-Generatoren
    bleiben erhalten (11.3); alte Graviton-Impulse werden aktualisiert pi_{k+1} = pi_k + S y; Impuls des neuen
    Gravitons durch die Nachbedingung pi_new = S y (11.4) festgelegt (dort als Verfeinerungs-Konsistenzbedingung gedeutet).
  - Wie erwartet, eine Zeile: Es gibt eine symplektische (Dirac-)Reduktion der Eckverschiebungs-Eichung in diskreter
    Zeit, aber kein Spektrum, keine Eichflaechen-Pruefung und kein "horizontal".
  - **Kette fuer TAKT-DYNAMIK-1 [ES]:** Die Zustandsabbildung der Literatur am 2-3-Zug ist weder "Raten stetig" (R) noch
    "Impulse stetig" (P), sondern Impulsaktualisierung durch die Hamilton-Hauptfunktion des aufgeklebten Simplex
    (Erzeugende erster Art, daher (prae-)symplektisch). Unser stetiges Zeit-Regime hat dafuer kein Gegenstueck in der
    gelesenen Literatur.

### F8 Gegensweep (Erwartung vor dem Abruf, date folgt): arXiv-API, eingereicht 2024-10-01 bis 2026-10-05, (simplicial|Regge|triangulation) AND (canonical|Hamiltonian|symplectic|Pachner) AND gravity
- Erwartung: wenige Treffer (Flaechen-Regge/effektive Spinschaum, Regge-Finite-Elemente, CDT-Zeit). Keine Arbeit, die fuer
  3+1-Regge mit stetiger Zeit und wechselnder Triangulierung Energie- oder Symplektik-Verletzung zeigt; hoechstens
  Wiederholung der Dittrich/Hoehn-Aussagen in diskreter Zeit.
- **Ausgang F8 (09:51:25; Abruf 9 von 15):** 7 Treffer (2025-04 bis 2026-06): Bruno/Colafranceschi/Mele/Rovelli 2026
  (Kontinuumslimes von Spinschaum, axiomatisch; starke Konvergenz -> topologisch) [S Abstract]; Gamboa/Tapia-Arellano
  2026 (zwei, IR-Gravitation, Regge-Teitelboim-Ladung); Elizaga Navascues 2025 (Regge-Wheeler-Gleichungen, LQC);
  DT in 2D; Spinschaum mit kosmologischer Konstante; Regulaere sphaerische Loesungen. **Keiner** zeigt Energie- oder
  Symplektik-Verletzung fuer 3+1-Regge bzw. kanonische simpliziale Gravitation bei wechselnden Gittern. Wie erwartet.
  Grenze: Suchwoerter im Abstract; "piecewise flat" oder "lattice gravity" ohne die Woerter fallen heraus.

### F9 (Erwartung vor dem Abruf, date folgt): WebSearch "Regge calculus random lattice graviton isotropy continuum limit Friedberg Lee"
- Erwartung: Treffer zu Christ/Friedberg/Lee (Zufallsgitter, Isotropie fuer Skalare/Eichfelder), Friedberg/Lee 1984
  und Feinberg/Friedberg/Lee/Ren 1984 (Regge auf Zufallsgittern nahe Kontinuum, statische Wirkung), Hamber-Arbeiten.
  Keine Studie zur Richtungsabhaengigkeit der Ausbreitung langer Gravitonen auf unregelmaessigen Netzen.
- **Ausgang F9 (Abruf 10 von 15; Zaehlung F1a, F1 bis F9):** Nur Trefferliste. Die Such-Zusammenfassung behauptet sinngemaess, Gittergravitation
  naehere sich dem Kontinuum unabhaengig davon, ob das Gitter regelmaessig ist, Abweichung als Reihe in l^2.
  Klingt nach Feinberg/Friedberg/Lee/Ren 1984; **nicht als Quelle verwendbar**, Primaerquelle in F10 pruefen.
  Kein Treffer zur Richtungsabhaengigkeit von Gravitonen. Teil-Ueberraschung: Konvergenz auf unregelmaessigen Gittern als Aussage.

### F10 (Erwartung vor dem Abruf, date folgt): INSPIRE-API, Titel "lattice gravity near the continuum limit" (Feinberg/Friedberg/Lee/Ren 1984)
- Erwartung: Abstract vorhanden oder nicht; falls vorhanden: Regge-Wirkung auf (Zufalls-)Gittern naehert Einstein-
  Hilbert mit Korrekturen O(l^2), unabhaengig von Regelmaessigkeit, statisch/euklidisch; keine Ausbreitungs-Isotropie.
- **Ausgang F10 (09:52:19; Abruf 11 von 15), Feinberg/Friedberg/Lee/Ren 1984, Nucl. Phys. B 245, 343 [S Abstract, INSPIRE]:**
  - Gilt fuer "any lattice, regular or irregular": Gittergravitation (Regge) naehert sich fuer l -> 0 dem
    Kontinuum (unter allgemeinen Randbedingungen); Abweichung je Gitter als Potenzreihe in l^2; Beispiele, darunter
    der Graviton-Propagator; erfuellt alle Invarianzen der ART plus eine neue Transformationsklasse.
  - **Erwartungsverstoss V-f (stark):** Erwartet war "keine Studie". Im kovarianten 4D-Regime ist die Kontinuums-
    naeherung auf unregelmaessigen Gittern als Satz behauptet, mit Korrekturen O(l^2), also Isotropie langer Wellen bis
    auf (kl)^2. Unser Netz zeigt dagegen langwellig O(1)-Anisotropie (V 6 %, Glas N = 128 15 % [P]).
  - Zwei Regime [ES]: (i) kovariant/4D, Bewegungsanteil aus der 4D-Wirkung: Abweichung O(l^2); (ii) unser 3+1-Netz mit
    gesetzter Bewegungsenergie: O(1). Moderator: Herkunft der Bewegungsenergie. Passt dazu, dass die affine
    Steifigkeit (Regge-Potential) bei uns isotrop ist (1 +- 1,7e-5, TT-GLAS-2 [P]).
  - Vorsicht: Abstract spricht von Wirkung/Propagator; ob die Bewegungs-Gleichungen punktweise konsistent sind, ist eine
    eigene Frage (Brewin-Einwand, aus dem Gedaechtnis [L]). Gegenlager in F11 pruefen (Regel 1).

### F11 (Erwartung vor dem Abruf, date folgt): arXiv-API (au:Brewin OR au:Christiansen) AND ti:Regge
- Brewin (um 2000): Regge-Gleichungen punktweise keine konsistente Naeherung der Einstein-Gleichungen; Brewin/Gentle:
  Konvergenz nur im integralen/schwachen Sinn. Christiansen ("On the linearization of Regge calculus", falls auf
  arXiv): linearisiertes 3D-Regge = Finite-Elemente-Form, Spektralnaehe auf allgemeinen Netzen.
- **Ausgang F11 (09:53:06; Abruf 12 von 15) [S Abstract]:**
  - Brewin (gr-qc/9502043, GRG 32, 897, 2000): Residuen der Regge-Gleichungen auf Einstein-Loesungen trennen auf
    generischen Gittern Loesungen nicht von Nicht-Loesungen; entweder inkonsistent oder Residuen-Kriterium falsch.
  - Brewin/Gentle (gr-qc/0006017, CQG 18, 517, 2001): Kasner direkt simplizial geloest; oszillierende Abweichung
    versoehnt die Lager; "solutions of Regge calculus are, in general, expected to be second order accurate".
  - Christiansen (1106.4266, 2011): linearisiertes 3D-Regge um euklidische Metrik = curl^T curl; die Eigenpaare
    "converge to their continuous counterparts", als nichtkonforme FEM, mit diskretem Komplex und kommutierenden
    Interpolatoren (also ohne Eichflaeche; die Eichung ist der Kern im Komplex).
  - Christiansen/Hu/Lin 2023 (Regge-Komplex, Kohomologie), Christiansen/Lin 2026 "Regge metrics with enhanced trace"
    (Spur-Operator surjektiv auf stetige Funktionen; Anwendungen ART angedeutet) = die HODGE-L-Spur-Varianten [P].
  - **Zwei-Regime-Befund (Regel 1) [ES]:** Kein echter Widerspruch FFLR gegen Brewin: Moderator ist das Kriterium
    (Wirkung/Loesung/Spektrum konvergieren mit O(l^2); punktweise Residuen der Gleichungen nicht). Fuer unsere Frage
    zaehlt das Spektrum: Christiansen zeigt Spektralkonvergenz fuer den Potentialteil (curl^T curl) auf allgemeinen
    Netzen. **Erwartungsverstoss V-g:** Das ist naeher an RK5 und RK4 als erwartet (Spektrum ohne Eichflaeche).
  - Unterscheidungspunkt [ES]: Bei konsistenter Masse (volumengewichtet, Geschwindigkeitsseite) und Regge-Steifigkeit
    erwartet man langwellig Isotropie bis O((kl)^2); unser Netz zeigt O(1) bei kl -> 0. Wo beide Erklaerungen
    ("Massenform" gegen "Zufallsnetz an sich") auseinanderlaufen: Spanne gegen kl bei festem Netz. ~~Massenform-
    Ursache sagt: Spanne bleibt bei kl -> 0 endlich; FEM-Erwartung sagt: Spanne ~ (kl)^2 mit konsistenter Masse.~~
    (gestrichen, Etiketten missverstaendlich; berichtigt in Abschnitt 5, Unterscheidungspunkt 1: gemessen wird MIT
    Lund-Regge-Masse; H_A "Massenform" sagt dann Spanne -> 0 wie (kl)^2, H_B "Netz an sich" sagt endliche Spanne.)
    TT-GLAS-2 misst bei |k| = 1e-2 (Linearitaet <= 6,3e-5 [P]) mit der jetzigen Impulsseiten-Form eine endliche
    Spanne; das trennt H_A und H_B noch nicht.

## 3. Code gelesen (lokal, kein Netzabruf, nicht ausgefuehrt): takt-dynamik-1/code/ew.py (~~09:55~~ geschaetzt, gestrichen; zwischen 09:54:24 und 09:56:15 per date)

- ops() Z. 202 ff.: A = Summe ueber Zellen A0[i,j] (Impulsseite, x' = A p), B = Regge-Hesse; M = Eckverschiebung;
  c_v^H a = -Summe_{e an v} (B a)_e (crow), also c^H q = 0 ist "delta R^(3) = 0 je Ecke" und c^H p = 0 dieselbe
  Zeile auf den Impulsen.
- phys_basis_rr Z. 253: S = Orthonormalbasis des Komplements von Bild[M, c] (SVD). spektrum_punkt Z. 311 ff.:
  A_red = S^H A S, B_red = S^H B S, omega^2 = eig(A_red B_red). Daneben "ohne Skalarregel" (nur M).
- **Schreibtisch [M, vorab ableitbar, Voraussetzungen B M = 0 und c^H M = 0, laut IMPULS-NETZ-1 8,7e-16 bzw. 1,6e-15 [P]]:**
  - Das Paar (c^H q, c^H p) ist zweiter Klasse mit Klammer c^H c. Dirac-Klammer: {q, p}_D = P_c = 1 - c (c^H c)^-1 c^H
    (euklidisch, weil beide Bedingungen dieselben Spalten c benutzen). Auf q = S x, p = S y ergibt das genau
    x' = A_red y, y' = -B_red x. **R1 ist die korrekte Dirac-Reduktion des c-Paars**, keine willkuerliche Projektion.
  - M erster Klasse: p'' = -P_c B (P_c A p + M nu) = -P_c B P_c A p (B M = 0). Mit P_c = S S^H + P_M (weil Bild M
    senkrecht auf c) und S^H B P_M = 0 folgt S^H B P_c A S = B_red A_red. Also sind die R1-Frequenzen die eichinvarianten
    Frequenzen; **keine Abhaengigkeit von der Eichflaeche fuer M** (die euklidische q-Flaeche ist folgenlos).
  - Zusatz (Identitaet aus 1.1): (S^H A S)^-1 = S^H Q S, Q = horizontale Geschwindigkeitsmetrik bzgl. Bild[M, c].
  - **Folge fuer HODGE-MASSE-1 [ES]:** HM1-Teil "mit R1 weichen sie um mehr als 1e-4 ab" ist vorab nicht zu erwarten
    (Identitaet); eine zweite Eichflaeche fuer M muss dieselben omega^2 bis Rundung geben. Die TT-GLAS-2-
    "Projektionsanisotropie" ist dann kein Reduktionsartefakt, sondern die physikalische (reduzierte) Bewegungsenergie
    der gewaehlten Form auf dem Zufallsnetz (nichtaffine Relaxation der Geschwindigkeit, Stichprobenrauschen ~ N^-1/2,
    passt zu Exponent -0,55 [P]) [H].
- **Zweite Folge [M]:** A2 (J_t -> J_t V_F/V_t auf der Impulsseite) ist je Tetraeder genau das Inverse des Lund-Regge-
  Elements (Rechnung: M_tau = V T^-T G_v T^-1, M_tau^-1 = (1/V) [G_p(n_e n_e, n_f n_f)] mit G_p = G_v^-1, 3D: Spur-
  koeffizient 1/2). Global gilt aber A2 = Summe M_tau^-1 != (Summe M_tau)^-1 = Lund-Regge. **HM0 ("volumengewichtete
  DeWitt-Form bei gleichmaessiger Rate = Kontinuumswert auf 1e-12") ist nur fuer die Geschwindigkeitsseite (Lund-Regge)
  eine Identitaet**; fuer A2 auf der Impulsseite muesste die Elementzerlegung des gleichmaessigen Impulstensors in
  Kantenimpulse an geteilten Kanten uebereinstimmen, was sie im Allgemeinen nicht tut [M]. Warnung an die Leitung.

### F12 (Erwartung vor dem Abruf, date folgt): WebSearch "Lund-Regge supermetric horizontal simplicial diffeomorphisms vertex displacement superspace"
- Erwartung: HMW 1997 und Zitierende (Hamber/Williams 2011, Hamber/Toriumi/Williams 2012, evtl. Bromley/Hartle/Miller);
  keine ausdrueckliche horizontale Reduktion der Eckverschiebungen mit Spektrum-Nachweis, auch nicht in 2024 bis 2026.
- **Ausgang F12 (Abruf 13 von 15):** Trefferliste: HMW 1997, Williams 1997 "Recent Progress in Regge Calculus"
  (gr-qc/9702006), Hamber/Williams "Gauge Invariance in Simplicial Gravity" (hep-th/9607153; nur Titel gesehen, nicht
  gelesen). Keine Arbeit mit horizontaler Reduktion der Eckverschiebungen und Spektrum-Nachweis. Wie erwartet, eine Zeile.

### F13 (Erwartung vor dem Abruf, date folgt): arXiv-API 2024-10-01 bis 2026-10-05, (Regge|simplicial) AND (graviton(s)|supermetric|superspace|isotropy) AND (gravity|gravitational)
- Erwartung: einige Flaechen-Regge-/Spinschaum-Gravitonarbeiten (hyperkubisch), evtl. Regge-FE; nichts zur
  Isotropie auf Zufallsnetzen und nichts zur horizontalen Reduktion. Dient als 24-Monats-Pruefung fuer RK4 und RK5.
- **Ausgang F13 (09:57:03; Abruf 14 von 15):** 11 Treffer, 10 aus Streuamplituden ("Regge limit"); einschlaegig nur
  Khatsymovsky 2026 (2601.02181): korrekte Stoerungsreihe in diskreter Gravitation fuer Graviton-Schleifen zum
  Newton-Potential [S Abstract]. Nichts zu RK4 oder RK5 in 24 Monaten. Wie erwartet, eine Zeile.

### Gegensweep-Zwischenstand (Regel 4), ~~09:58~~ (vorab eingetragen, gestrichen; date nach dem Schreiben 09:57:48)
- Selbstverstaendlich und nicht geprueft: (1) dass Christiansens Spektralkonvergenz auf allgemeinen (unregelmaessigen)
  Netzen gilt und welche Masse sie benutzt; (2) dass FFLRs "lattice gravity" das Regge-Funktional ist; (3) dass die
  F4-Fehlsuche nichts Einschlaegiges verdeckt; (4) dass HODGE-MASSE-1s "A2" die Impulsseite meint; (5) dass "Lapse je
  Drei-Simplex" bei FJ auch fuer Piran/Williams gilt.
- Geprueft wird (1) mit dem letzten Abruf F14 (Christiansen 2011 Volltext), weil die Ketten fuer RK4/RK5 und HM daran
  haengen. (4) ist eine Rueckfrage an die Leitung (kein Abruf noetig). (2), (3), (5) bleiben offen.

### F14 (Erwartung vor dem Abruf, date folgt): arXiv-PDF 1106.4266 (Christiansen 2011), grep nach mesh/shape regular/quasi-uniform/L2/inner product/eigen/gauge/kernel
- Erwartung: Familie formregulaerer (shape-regular) Simplexnetze, sonst beliebig (unstrukturiert erlaubt); Masse = L2-
  Skalarprodukt (Frobenius) auf stueckweise konstanten Metriken, nicht DeWitt; Kern (Eichung) ueber Komplex und
  kommutierende Interpolatoren, keine Eichfixierung.
- **Ausgang F14 (09:57:48; Abruf 15 von 15), Christiansen 2011 Volltext [S, S. = PDF-Seite per pdftotext je Seite]:**
  - S. 15, Gl. (88) bis (91): Eigenproblem a(u, v) = lambda <u, v>; W = Kern von a; **V = {u : <u, w> = 0 fuer alle w in W}**,
    X = V (+) W, P = orthogonale Projektion auf V. Also eine ausdrueckliche massen-orthogonale ("horizontale")
    Zerlegung gegen den Kern, ohne Eichflaeche. Masse = kanonisches L2-Skalarprodukt auf symmetrischen Matrixfeldern
    (~~S. 18~~ S. 19, per Seitenextraktion berichtigt: O = L2(S) (x) S), nicht DeWitt.
  - S. 20: quasi-uniforme Folge simplizialer Netze T_h des 3-Torus, h -> 0. S. 22, Satz 4.7: Das linearisierte
    Regge-Kalkuel ist ein konvergentes Verfahren fuer die Eigenpaare des Saint-Venant-Operators.
  - Einleitung (Z. 145 ff.): Operator mit unendlichem Kern und Eigenwerten beider Vorzeichen; ein Vorzeichen gehoert zu
    Moden, die im Kontinuum durch Bedingungen ausgeschlossen sind.
  - **Erwartungsverstoss V-h (gegen RK4-Erwartung "nicht in der Literatur"):** Die horizontale Zerlegung steht dort
    ausdruecklich (statisch, L2-Masse, quasi-uniforme Netze); eine Eichflaeche kommt gar nicht vor. Gegen RK4 bleibt:
    kein Hamilton-Bild, keine DeWitt-Masse, kein ausdruecklicher Eichflaechen-Vergleich.
  - Fuer RK5 [ES]: Spektralkonvergenz auf quasi-uniformen unstrukturierten Netzen heisst: lange Wellen werden isotrop
    (statisches Operator-Regime, konsistente L2-Masse). Kein ausdruecklicher Richtungsvergleich.

## 4. Gegensweep (Regel 4), Abschluss ~~10:00~~ (vorab eingetragen, gestrichen; date nach dem Schreiben 10:00:21)

- Geprueft: (1) Christiansens Netzannahme und Masse: quasi-uniform; L2 (Frobenius), nicht DeWitt (F14). Folge: Die
  Konvergenzaussage traegt fuer eine Frobenius-Masse; fuer die indefinite DeWitt-Masse ist sie dort nicht bewiesen.
- Offen geblieben: (2) ob FFLRs "lattice gravity" das Regge-Funktional ist (nur Abstract; Friedberg/Lee 1984 leiten
  Regges Wirkung her [L]); (3) ob die F4-Fehlsuche Einschlaegiges verdeckt (F5 und F13 decken teilweise ab);
  (4) welche Seite HODGE-MASSE-1 mit "A2" meint (Rueckfrage); (5) Lapse-Lage bei Piran/Williams (nur Abstract).
- Gegensweep-Suche "Verletzung von Energie oder Symplektik bei wechselnden Gittern": gefunden in diskreter Zeit
  (Dittrich/Hoehn 2013, Typ-II-Zuege senken den Rang; F6) und fuer Bedingungen in stetiger Zeit (FJ 1986: nicht
  erhalten bei a priori Lapse/Shift; F3). 24 Monate (F8, F13): nichts Neues. Stetige Zeit mit Umklappen: keine Arbeit.

## 5. Regime, Unterscheidungspunkte, Urteilsentwurf (~~10:00~~ gestrichen; date nach dem Schreiben 10:00:21)

- Regime H (stetige Zeit, 3+1): Lund/Regge, Piran/Williams, Friedman/Jack, HMW, Hamber/Williams 2011, unser Netz.
  Regime K (diskrete Zeit bzw. 4D/Pfadintegral): Dittrich/Hoehn, Hoehn, FFLR, Rocek/Williams, Christiansen (statisch).
- Gilt in beiden: keine exakte erste Klasse fuer die Hamilton-Bedingung ausser flach-linear (FJ fuer H; DH 2010 fuer K).
  Nur in K belegt: Symplektik ueber Zuege (eingeschraenkt), Spektralkonvergenz/Isotropie. Nur in H belegt: Supermetrik.
- Unterscheidungspunkt 1 (H_A Massenform gegen H_B Zufallsnetz an sich): TT-Spanne gegen kl bei festem Netz, gerechnet
  MIT Lund-Regge-Masse (Geschwindigkeitsseite). H_A: Spanne -> 0 wie (kl)^2. H_B: endliche Spanne bei kl -> 0.
  Mit der jetzigen Impulsseiten-Form sagen beide eine endliche Spanne voraus; dort sind sie nicht trennbar.
- Unterscheidungspunkt 2 (Energiesprung aus Gewichten J gegen aus Zustandsabbildung): Sprung je Zug gegen kl.
  Lund-Regge + kinematische neue Rate: Sprung ~ Schwankungsenergie der Doppelpyramide ~ (kl)^2-unterdrueckt. A1:
  Sprung ~ Anteil der Zellen, unabhaengig von kl. Bei kl ~ 1,5 (TAKT-DYNAMIK-1) nicht trennbar.
- Unterscheidungspunkt 3 (Seite der Supermetrik): gleichmaessige Rate auf unregelmaessigem Netz: Lund-Regge gibt den
  Kontinuumswert exakt (Identitaet), die Impulsseite (A2) nicht. Das ist HM0.
- Urteilsentwurf: RK1 teilweise; RK2 eingetroffen; RK3 teilweise; RK4 teilweise (Christiansen-Zerlegung) bzw. nach
  Wortlaut "mit Nachweis der Eichflaechen-Unabhaengigkeit" nicht erfuellt; RK5 teilweise (implizit ueber Konvergenz).

## 6. Abschluss

- DOSSIER.md geschrieben ab 10:03:28 (date); Abgabezeile dort: 2026-10-05 10:09:30 CEST (date).
- Offene Rueckfrage an die Leitung (wandert mit): Meint HODGE-MASSE-1 mit "A2" die Impulsseite? Davon haengt HM0 ab.
