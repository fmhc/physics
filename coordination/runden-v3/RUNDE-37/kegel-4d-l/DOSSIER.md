# KEGEL-4D-L: Dossier (feldforscher fuer die Leitung claude-primary)

- **Auftrag:** Finn (05.10.), woertlich: "Bezouts Theorem und Keplers optics zu conic sections / circle, ellipse,
  parabola, hyperbola, nutze das für 4d ideen". Karte KARTE.md ist bindend; KB1 bis KB4 und ihre Bedeutung sind
  unveraendert.
- **Zeiten (date):** Start 2026-10-05 06:07:04 CEST. Abrufe 06:18:26 bis 06:24:12 CEST. Dieser Text ab 06:29:50 CEST.
- **Abrufe:** 8 von 8 (arXiv-API sieben Mal, dazu einmal arxiv.org per WebFetch). Ein leerer http-Fehlversuch um 06:18:19
  ist nicht gezaehlt. Das PDF, das WebFetch abgelegt hat, wurde mit dem Read-Werkzeug gelesen; das zaehlt nicht extra.
  Kopien liegen in quellen/, Protokoll mit Erwartung vor jedem Abruf in ARBEITSFELD.md.
- **Keine Rechenlaeufe.** Alle Zahlen sind Kopf- bzw. Schreibtischrechnung [M], nicht gegengelesen. Keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen, mit Seite bzw. Gleichung; [S Abstract] nur Abstract gelesen
  - [L] Lehrbuchwissen aus dem Gedaechtnis; [L?] Literatur aus dem Gedaechtnis, unsicher
  - [M] eigene Mathematik; [ES] eigener Schluss; [H] Hypothese; [P] Projektdatei

## 1. Ergebnis zuerst

1. **Alle fuenf Saatideen sind Literatur oder vorab ableitbar.** Fuer Finns Netz ergibt keine eine messbare neue
   Vorhersage. Die "vierte Dimension" ist ueberall eine Hilfsdimension und nicht die Raumzeit:
   - S1: der Abstand r als "zweite Zeit"
   - S2: der Impulsraum
   - S3: die Hopf-Faser
2. **S1 steht woertlich in der Literatur** (Meng 2012, arXiv:1111.2277) [S]:
   - Die Kepler-Bahn ist der Schnitt des Zukunftslichtkegels mit der Ebene a.x = 1, l.x = 0, mit a ~ (1, A). Der
     Lenz-Vektor A ist die "Geschwindigkeit" der Ebene, und e = |A|.
   - Jede Ellipse ist per Lorentz-Transformation einem Kreis gleich. Ellipsen und Parabeln bilden getrennte Bahnen der
     Lorentzgruppe (mit Skalierung R+); fuer Hyperbeln gibt es keine solche Wirkung.
   - Die Kegelzeit ist laut Meng eine **zweite Zeitdimension**. Ein Schub darin macht klassisch aus einer Kepler-Bahn
     eine Bahn mit Monopolladung.
3. **600-Zelle [M, drei Spurproben]:** Ihre untersten Graph-Laplace-Niveaus tragen genau die Wasserstoff-Schalen
   n = 1 bis 6, also 1, 4, 9, 16, 25 und 36 Zustaende (zusammen 91).
   - Danach kommen 29 "Galois-Spiegelzustaende" mit 9, 16 und 4 Zustaenden; eine Schale n = 7 gibt es nicht.
   - Die Abstaende der Niveaus passen nicht zum Kontinuum l(l + 2).
   - Eine Wasserstoff-Deutung des Spektrums findet sich in arXiv-Abstracts nicht, auch nicht in den letzten 24 Monaten.
     Das Ergebnis ist aber vorab ableitbar und damit keine Messung.
4. **Finns Diamant-Netz entspricht auf S^3 der 120-Zelle bzw. den 4-Fullerenen, nicht der 600-Zelle.**
   - Die 600-Zelle ist die 12-fach koordinierte Tetraeder-Dichtpackung.
   - In 4D schliessen fuenf 4-Simplexe je Dreieck hyperbolisch: Wabe {3,3,3,5}, deren Eckfigur die 600-Zelle ist
     [M, L?].
5. **Bezout gibt bei Gravitationslinsen nur fuer n <= 3 Punktmassen die scharfe Bildzahl n^2 + 1.**
   - Ab n = 4 gilt 5n - 5 (Rhie; Khavinson/Neumann) [S Abstract]. Die scharfe Grenze kommt aus der Funktionentheorie,
     nicht aus dem Grad der Gleichung.
   - Kartenvorschlag: **FOCK-SCHALEN-S3-1** (120-Zelle gegen 600-Zelle), ausdruecklich ohne Datenbezug.

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

**V1 (S1, Abruf A4/A6): Der Lichtkegel in S1 ist nicht die Raumzeit, sondern eine zweite Zeit. Und die Lorentzgruppe
verbindet Ellipse und Parabel nicht.**
- Erwartet: S1 ist eine anschauliche Bruecke "Keplers Stetigkeit = Lorentz-Schub" (Karte) und als eigene Rechnung neu
  aufgeschrieben [M].
- Gefunden in Meng 2012 (arXiv:1111.2277v2, J. Math. Phys. 53, 052901):
  - Zur Hebung [S S. 4, Gl. (2.11), (2.12)]: "the projection of the Minkowski space onto R^3 defines a diffeomorphism
    from the future light cone ... onto R^3_*". Die Bahn (2.3) ist "the intersection of the future light cone with the
    oriented plane" a.x = 1, l.x = 0, mit a = (1, A)/(L^2 - mu^2) und l = (mu, L)/sqrt(L^2 - mu^2).
  - Zur Energie [S Gl. (3.5)]: E = -a^2/(2 a0). Die Ellipse hat a^2 > 0, die Parabel a^2 = 0, die Hyperbel a^2 < 0
    [S Thm. 1 (5)].
  - Zum Kreis [S S. 7]: Im elliptischen Fall laesst sich (a, l) per Lorentz-Transformation auf A = 0 bringen, "so that
    the magnetic charge is zero and the orbit is a circle".
  - Zu den Bahnklassen [S S. 3]: SO+(1,3) x R+ wirkt transitiv auf die elliptischen und getrennt auf die parabolischen
    Bahnen; "there is no similar action on the oriented hyperbolic orbits".
  - Zur zweiten Zeit [S S. 7]: "The Jordan algebra approach to the Kepler problem requires a second temporal dimension,
    and the Lorentz transformations in this note refer to the one that mixes space with this second temporal
    dimension." Die Monopolladung mu ist "relative and becomes zero in a certain 'inertial' frame". Meng fragt offen:
    "Is this second temporal dimension more than just a mathematical artifact?"
- Korrigierte Erwartung [ES]:
  - S1 ist Literatur (Meng 2012, aufbauend auf arXiv:0911.2977).
  - "Keplers Stetigkeit ist ein Lorentz-Schub" gilt nur innerhalb der Ellipsen (Kreis -> Ellipse, e = v < 1).
  - Der Schritt ueber die Parabel ist ein Grenzuebergang v -> 1, also Keplers Brennpunkt im Unendlichen, und keine
    Symmetrie. Die Hyperbel ist der "ueberlichtschnelle" Sektor (zeitartige Schnittebene).
  - Die Kegelzeit ist der Abstand r, nicht Finns Takt.

**V2 (S5, Schreibtisch, KB3): Die 600-Zelle traegt nicht nur 1, 4, 9 und 16, sondern genau sechs Schalen. Darueber
gibt es nur noch Bruchstuecke.**
- Erwartet (Karte): Die Entartungen 1, 4, 9, 16 gelten, "solange die H4-Symmetrie die SO(4)-Multipletts nicht spaltet"
  (55 %).
- Gefunden [M]: Die Niveaus haben die Vielfachheiten 1, 4, 9, 16, 25 und 36, dann 9, 16 und 4.
  - Zur Rechnung: Die 120 Ecken bilden die binaere Ikosaedergruppe 2I. Die 12 Nachbarn eines Punkts sind eine
    Konjugationsklasse, der Graph ist also ein normaler Cayley-Graph.
  - Jede irreduzible Darstellung rho gibt den Eigenwert 12 chi_rho(c)/d_rho mit Vielfachheit d_rho^2.
  - SU(2)-Darstellungen V_j bleiben unter 2I irreduzibel fuer j <= 5/2; das gibt die sechs Schalen. Die drei
    "gestrichenen" Darstellungen 2', 3' und 4' liefern die Spiegelzustaende.
  - Bei j = 3 zerfaellt V_3 = 3' + 4'. Ab der Schale n = 7 spaltet H4 also wirklich, und zwar in 9 + 24 + 16.
  - Im 120-dimensionalen Raum ist dann nur fuer Bruchstuecke Platz: wahrscheinlich 9 und 16 aus n = 7 und 4 aus n = 8
    [M, vorlaeufig].
- Korrigierte Erwartung: Die Schalen sind exakt und vorab ableitbar, also keine Messung. Die Karten-Bedingung ("solange
  H4 nicht spaltet") stimmt. Sie greift genau ab n = 7, und dort endet zugleich der Platz im endlichen Netz.

**V3 (S5, Projektlage): Die 600-Zelle ist nicht Finns Netz.**
- Erwartet (Karte S5): "Die 600-Zelle als Finns 4D-Tetraeder-Netz".
- Gefunden:
  - Finns Netz ist Diamant (4 Kanten je Knoten) bzw. Pyrochlor (LICHT-FINN-NETZ-1, Einheiten-Zeile) [P].
  - Die 600-Zelle ist 12-fach koordiniert (Tetraeder-Dichtpackung, Metallglas-Vorbild). Das Diamant-Gegenstueck auf
    S^3 ist die 120-Zelle {5,3,3} mit 600 Ecken, Grad 4, Tetraeder-Eckfigur und Fuenferringen [M; L? Sadoc/Mosseri,
    a-Si].
  - Dazu gibt es eine ganze Familie: die sphaerischen "4-Fullerene" mit Fuenf- und Sechseck-Flaechen (Deza/Shtogrin
    1999, math/9906035) [S Abstract].

**V4 (S3, Abruf A3/A4): Die KS-Literatur spricht von "MIC-Kepler" und "Dyon", nicht von "monopole". Ungerade Sektoren
tragen halben Spin.**
- Erwartet: Treffer zu "Kustaanheimo AND monopole".
- Gefunden: 0 Treffer (A3). Unter "MICZ/MIC-Kepler" waren es 46 (A4).
  - Mardoyan/Petrosyan 2006 (quant-ph/0604127) [S Abstract]: Das verallgemeinerte MIC-Kepler-System und der
    4D-Singulaer-Oszillator sind dual, ueber eine verallgemeinerte KS-Transformation.
  - Nersessian 2000 (math-ph/0010049, Einzelautor laut Abrufdaten) [S Abstract]: Fuer die Bohlin-Abbildung (2D, auf
    Sphaere und Pseudosphaere) gilt: "the odd states yield the Coulomb system on pseudosphere in the presence of magnetic
    flux tube generating half spin". Mit KS ergibt sich die pseudosphaerische Fassung des MIC-Kepler-Problems.
- Bedeutung [ES]: Der bosonische Oszillator enthaelt in seinem ungeraden Sektor ein Kepler-Problem mit halbzahligem
  Drehimpuls.
  - Woertlich belegt ist das nur fuer 2D (Bohlin). Fuer KS (4D -> 3D) stuetzt es sich auf meine Zaehlung (Faserladung
    s = 1/2) [M] und auf MIC-Kepler [S Abstract].
  - Das ist derselbe Mechanismus wie Ladung plus Monopol (Goldhaber), den das Projekt schon kennt (LADUNG-MONOPOL-L) [P],
    hier mit einer 4D-Herkunft.

**V5 (S4, Abruf A2): Der Grad der Linsengleichung (Bezout) ist nur bis n = 3 scharf.**
- Erwartet (Karte S4): "Zaehlgrenzen aus dem Grad der Linsengleichung".
- Gefunden [S Abstract]:
  - Rhie 2001 (astro-ph/0103463): "the equation for n-tuple lenses suggests that the maximum number of images ...
    increases as n^2+1"; n = 1, 2 und 3 erreichen 2, 5 und 10. Sie vermutet 5(n - 1).
  - Khavinson/Neumann (math/0401188): hoechstens 5n - 5 Nullstellen, damit ist Rhies Vermutung bewiesen. Die Scharfheit
    zeigt Rhie 2003 (astro-ph/0305166).
  - Bei n = 4 stehen 17 gegen 15, bei n = 10 stehen 101 gegen 45 [M].
- Meine Schreibtisch-Erwartung (06:16) hatte das vorweggenommen. Verletzt ist nur der Kartenwortlaut.

**V6 (4D, Schreibtisch): Das Vorzeichen der Kruemmung kippt von 3D nach 4D.**
- Erwartet: Ein 4D-Tetraeder-Netz ist "wie die 600-Zelle", also positiv gekruemmt.
- Gefunden [M, L?]:
  - Fuenf Tetraeder um eine Kante lassen 7,36 Grad Luecke; sie schliessen auf S^3 (600-Zelle) [P GEOMETRIE-XD].
  - Fuenf 4-Simplexe um ein Dreieck ueberlappen um 17,6 Grad [P GEOMETRIE-XD, Zeile d = 4]. Sie schliessen in H^4 als
    regulaere Wabe {3,3,3,5} [L? Coxeter].
  - Deren Eckfigur ist die 600-Zelle: 120 Kanten und 600 Simplexe an jeder Ecke.
  - Die 600-Zelle ist also die "Kugel um eine Ecke" eines negativ gekruemmten 4D-Simplexnetzes.

## 3. Urteile KB1 bis KB4

| Nr | Erwartung (Karte) | Urteil | Beleg |
|---|---|---|---|
| KB1 (95 %) | e = v, Gegenlesen bestaetigt | **eingetroffen, mit Praezisierung** | Siehe die Punkte unter der Tabelle. |
| KB2 (80 %) | Kepler 1604: Begriff "Brennpunkt" und Stetigkeitsprinzip | **nicht entschieden** | A8 (arXiv) ergab 0 Treffer. Bleibt [L?]. Ein Abruf einer Sekundaerquelle (z. B. Field 1986, Stud. Hist. Phil. Sci. 17, 449 [L?]) war im Budget nicht mehr moeglich. |
| KB3 (55 %) | 600-Zelle: unterste Entartungen 1, 4, 9, 16 | **eingetroffen, staerker als erwartet** | Siehe die Punkte unter der Tabelle. |
| KB4 (75 %) | hoechstens 5n - 5 Bilder; Rhie-Vermutung, bewiesen von Khavinson/Neumann 2006 | **eingetroffen** | [S Abstract math/0401188]: "no more than 5n - 5 complex zeros ... settles a conjecture of S. H. Rhie". Scharf nach Rhie 2003 (Kommentar v2 und astro-ph/0305166). Gilt fuer n > 1. |

- **Beleg KB1:**
  - Schreibtisch [M]: Auf dem Kegel gilt r = t = a + v x. Das ist die Brennpunkt-Leitlinien-Form mit e = v und dem
    Brennpunkt in der Kegelspitze, in Polarform r = a/(1 - v cos phi): die Kepler-Bahn.
  - Literatur: [S Meng, Gl. (2.11), (2.12)] mit mu = 0 ergibt v = A und e = |A| [S Gl. (2.5)].
  - **e = v gilt fuer die Projektion auf die Ruhe-Ebene (x, y)**, die Kepler-Bahn. In der schraegen Ebene selbst,
    euklidisch gemessen, ist e' = v sqrt(2/(1 + v^2)) [M, Dandelin]. Mit der von Minkowski induzierten Metrik ist der
    Schnitt fuer v < 1 ein Kreis [M].
- **Beleg KB3:**
  - Schreibtisch [M]: Die Vielfachheiten sind 1, 4, 9, 16, 25, 36, dann 9, 16, 4.
  - Spurproben: A ergibt 0, A^2 ergibt 1440 (Soll 1440), A^3 ergibt 7199,97 (Soll 6 x 1200 Dreiecke = 7200).
  - Literatur: Eine Wasserstoff-Deutung fand sich nicht (A1: 41 Abstracts zu "600-cell", 6 davon im 24-Monats-Fenster).
  - Vorab ableitbar, also keine Messung.

Bedeutung (nach der vorab festgelegten Lesart der Karte):
- **KB1:** Die anschauliche Bruecke gibt es. Sie fuehrt aber in eine Hilfs-Raumzeit (zweite Zeit), nicht in die
  physikalische, und ist keine neue Physik (V1).
- **KB3:** Ein 4D-geschlossenes Tetraeder-Netz traegt das Wasserstoff-Muster bis n = 6 von selbst. Die Karte sagt: "Ein
  kleiner Test lohnt nur, wenn das nicht schon in der Literatur steht". In arXiv-Abstracts steht es nicht. Fuer die
  600-Zelle ist es aber vollstaendig ableitbar (V2), ein Test waere nur eine Kontrolle. Offen und nicht ableitbar ist
  die 120-Zelle, also Finns Diamant (Kartenvorschlag).

## 4. S1 bis S5: was traegt die Literatur, was ist Rechnung, was Hypothese

### S1 Kegel, bewegte Ebene, e = v
- **[S] Meng 2012:**
  - Gl. (2.3): r - A.r = L^2 - mu^2.
  - Gl. (2.11), (2.12): Lichtkegel-Schnitt, siehe V1.
  - Gl. (3.5): E = -a^2/(2 a0).
  - Satz 2: Lorentz-Transitivitaet auf den elliptischen und den parabolischen Bahnen.
  - S. 7: Ellipse ist Lorentz-aequivalent zum Kreis; die zweite Zeit; die Monopolladung ist relativ.
  - Quelle der 4D-Sicht ist Meng, arXiv:0911.2977 (nicht abgerufen).
- **[M]** Die Rechnung der Karte stimmt. Halbachsen der Projektion: A = a/(1 - v^2) und B = a/sqrt(1 - v^2). Die Mitte
  liegt bei x0 = a v/(1 - v^2), ein Brennpunkt in der Kegelspitze.
- **[L]** Runge-Lenz: A.r = L^2 - m k r. Der Abstand ist also affin im Ort; das ist der ganze Inhalt von S1.
- **[L?]** Kepler 1604 (Ad Vitellionem Paralipomena, Kap. 4): "focus", stetige Folge der Kegelschnitte, Parabel mit
  einem Brennpunkt im Unendlichen. Nicht an einer Quelle geprueft (KB2).
- **[ES]** Keplers Stetigkeit (Kreis, Ellipse, Parabel, Hyperbel) ist in Mengs Bild:
  - Kreis zu Ellipse: ein Schub mit v < 1
  - Parabel: der Grenzfall v -> 1, die lichtartige Ebene
  - Hyperbel: eine zeitartige Ebene, fuer die es keinen Schub gibt
  - Die Parabel ist "der Lichtschnitt", wie die Karte sagt, aber in der Hilfs-Raumzeit.

### S2 Fock 1935
- **[L]** Fock 1935 (Z. Phys. 98, 145):
  - Der Impulsraum wird stereographisch auf S^3 projiziert, mit Radius p0 = sqrt(-2 m E).
  - Gebundene Zustaende sind S^3-Kugelfunktionen vom Grad n - 1, mit Entartung n^2 und Symmetrie SO(4) (Drehimpuls plus
    Runge-Lenz, Pauli 1926).
  - E > 0 fuehrt auf das Hyperboloid mit SO(3,1), E = 0 auf E(3) (Bander/Itzykson 1966).
  - Nicht abgerufen.
- **[S]** Meng, Thm. 1 (5): Das Vorzeichen der Energie bestimmt den Kegelschnitt (Ellipse, Parabel, Hyperbel). Das
  stuetzt die Dreiteilung, die die Karte SO(4), Grenzfall und SO(3,1) zuordnet.
- **[S Abstract] Ballesteros u. a. 2008 (0803.3430):** Bertrand-Raumzeiten (nach Perlick 1992). Geschlossene Bahnen
  gibt es nur mit Kepler- oder Oszillatorpotential, auch auf gekruemmten 3-Raeumen.
- **[S Abstract] 2601.13028 (Jan. 2026):** MICZ-Analoga auf S^3 und dem zweischaligen Hyperboloid; Spektren mit zwei
  Quantenzahlen. Kepler auf gekruemmten Raeumen ist aktuelle Forschung.
- **[L?]** Schroedinger 1940: Wasserstoff auf einer S^3 vom Radius R hat E_n = -1/(2 n^2) + (n^2 - 1)/(2 R^2) (atomare
  Einheiten), die Entartung n^2 bleibt (Higgs 1979, Leemon 1979). Nicht geprueft.
- **[ES]** Focks S^3 ist der Impulsraum. "Wasserstoff auf Finns Netz" im Ortsraum ist darum eine Analogie, keine
  Identitaet.

### S3 Kustaanheimo/Stiefel
- **[L]** KS 1965 (J. Reine Angew. Math. 218, 204):
  - Die Abbildung R^4 -> R^3 ist die Hopf-Abbildung.
  - Das 3D-Kepler-Problem bei fester Energie wird zum 4D-Oszillator mit U(1)-Nebenbedingung und fiktiver Zeit dt/r.
  - In 2D leisten das Levi-Civita bzw. Bohlin mit z -> z^2.
- **[S Abstract]** Die Dualitaet: Mardoyan/Petrosyan 2006 (quant-ph/0604127) und Lavrenov 2019 (1908.03572,
  ND-Oszillator gegen (n+1)D-MICZ, verallgemeinerte KS). Der halbe Spin aus ungeraden Zustaenden (2D, Bohlin):
  Nersessian 2000 (math-ph/0010049).
- **[M]** Zaehlung im Oszillator in C^2:
  - n_a und n_b seien die Gesamtzahlen der rechts- bzw. linksdrehenden Quanten (je zwei Moden), die Faserladung
    s = (n_a - n_b)/2. Zu festem (n_a, n_b) gibt es (n_a + 1)(n_b + 1) Zustaende.
  - Mit n_a = n - 1 + s und n_b = n - 1 - s ist die Entartung (n + s)(n - s) = n^2 - s^2.
  - s = 0 gibt Wasserstoff (n^2).
  - s = 1/2 gibt halbzahlige n und die Entartungen 2, 6, 12, ...
- **[H]** Die Q-Ball-Phase als Hopf-Faser: Waere die innere U(1) des Q-Balls die Faser, erschiene ein geladener Ball in
  3D als Dyon (MICZ).
  - Unterscheidungspunkt: s ungleich 0 aendert die Entartung zu n^2 - s^2 und erlaubt halbzahlige Bahndrehimpulse.
  - Wasserstoff zeigt s = 0 [L].

### S4 Bezout
- **[S Abstract]** Rhie 2001, Rhie 2003, Khavinson/Neumann (siehe V5, KB4). Negative Bilder uebersteigen positive um
  n - 1 (Rhie 2003).
- **[M]** Vier Lichtkegel in 3+1D (Positionsbestimmung aus vier Signalen):
  - Bezout erlaubt 2^4 = 16 Schnittpunkte.
  - Die Differenzen der Kegelgleichungen sind aber linear, also bleibt eine Gerade mal eine Quadrik: hoechstens 2 reelle
    Ereignisse.
  - [L?] Das ist das bekannte Zweideutigkeitsproblem der Positionsbestimmung (Abel/Chaffee 1991; Coll u. a.).
- **[L?]** Alhazens Spiegelproblem fuehrt auf eine Gleichung 4. Grades (Neumann 1998). Nicht geprueft.
- **[ES]** Bezout liefert obere Schranken. Die scharfen Zahlen kommen aus Zusatzstruktur:
  - Bei den Lichtkegeln ist es der gemeinsame quadratische Teil (die Metrik).
  - Bei den Linsen ist es die Harmonizitaet (Fatou-Argument nach Khavinson/Swiatek).

### S5 600-Zelle
- **[M]** Spektrum (Adjazenz bzw. Laplace L = 12 - A):

  | Darst. | d | Adjazenz | Laplace | Vielfachheit | Wasserstoff |
  |---|---|---|---|---|---|
  | 1 | 1 | 12 | 0 | 1 | n = 1 |
  | 2 | 2 | 6 phi = 9,708 | 2,292 | 4 | n = 2 |
  | 3 | 3 | 4 phi = 6,472 | 5,528 | 9 | n = 3 |
  | 4 | 4 | 3 | 9 | 16 | n = 4 |
  | 5 | 5 | 0 | 12 | 25 | n = 5 |
  | 6 | 6 | -2 | 14 | 36 | n = 6 |
  | 3' | 3 | 4 phi' = -2,472 | 14,472 | 9 | Spiegel |
  | 4' | 4 | -3 | 15 | 16 | Spiegel |
  | 2' | 2 | 6 phi' = -3,708 | 15,708 | 4 | Spiegel |

  - phi = 1,618 und phi' = -0,618.
  - Auf 3 skaliert ist das untere Spektrum 0 : 3 : 7,24 : 11,78 : 15,71 : 18,33, gegen l(l + 2) = 0 : 3 : 8 : 15 : 24 :
    35.
  - Lesart der Spiegelniveaus [M, vorlaeufig]:
    - Die Darstellungen 3', 4' und 2' kommen in den S^3-Kugelfunktionen erst ab Grad 6 bzw. 7 vor. Charakterprobe:
      V_3 = 3' + 4' und V_7/2 = 2' + 6 unter 2I.
    - Die Spiegelniveaus sind also wahrscheinlich Bruchstuecke der Schalen n = 7 (9 + 16 von 49) und n = 8 (4 von 64).
    - Der 24-dimensionale Rest der Schale n = 7 (3' x 4' plus Tausch) hat auf den Ecken keinen Platz.
    - Ob die Bruchstuecke wirklich aus Grad 6 und 7 stammen oder erst aus hoeheren Graden, habe ich nicht geprueft.
- **[S Abstract]** Cohn/Kumar 2006 (math/0607446): Die 600-Zelle minimiert die Energie fuer alle vollstaendig monotonen
  Potentiale. [L?] Ihre Ecken bilden ein sphaerisches 11-Design. Das erklaert, warum die Kugelfunktionen bis Grad 5 auf
  den 120 Punkten orthogonal bleiben.
- **[S Abstract] 2604.12971 (April 2026):** Laves-Netz (3 Kanten je Ecke) auf S^3 als Teilnetz der 600-Zelle. Netze auf
  S^3 sind aktuell, Spektren dort nicht.
- **[S Abstract] 2011.04120:** Regge-FLRW-Universum aus verfeinerten 600-Zellen, das abwechselnd expandiert und
  kontrahiert.
- **[S Abstract] math/9906035:** 4-Fullerene, die Verfeinerungsleiter fuer Diamant-artige Netze auf S^3.
- **[H]** Die Wasserstoff-Lesart braucht Focks Impulsraum (siehe S2).

## 5. Regime, Moderatoren, Unterscheidungspunkte

**Zwei Regime (Regel 1):**
- **A, Umbenennung bekannter Physik:** S1 bis S4 vollstaendig (Meng, Fock, KS/MICZ, Rhie/Khavinson-Neumann), S5 als
  Gruppentheorie.
- **B, neue Vorhersage fuer Finns Netz:** Dazu muesste entweder
  - die Hilfsdimension physikalisch sein, oder
  - die Netzstruktur (Diskretheit, Kopplungszahl, S^3-Schliessung) in eine Kenngroesse eingehen.
- **Vermuteter Moderator:** der Status der vierten Koordinate (Hilfsgroesse oder Raumzeit), dazu der Massstab k l bzw.
  l/r.

**Kopplung vor Bauteil (Regel 6):**
- Die n^2-Entartung und die geschlossenen Kegelschnitte entstehen auf vier verschiedenen Wegen:
  - Runge-Lenz (Pauli)
  - Fock-S^3 (Impulsraum)
  - KS-Oszillator (Hopf-Faser)
  - Meng-Lichtkegel (zweite Zeit)
- Keines dieser Bauteile ist die Ursache. Die gemeinsame Groesse ist die dynamische Gruppe SO(4,2) des exakten
  1/r-Potentials [L?, Barut/Kleinert 1967; Malkin/Man'ko 1965].
- Fuer Finns Netz zaehlt darum allein, ob das Fernfeld exakt 1/r ist [ES].

**Unterscheidungspunkte (Regel 2):**

| Paar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| S1: Hilfszeit gegen physikalische zweite Zeit | Klassisch macht ein Schub in Mengs zweiter Zeit aus mu = 0 eine Bahn mit Monopolladung mu ungleich 0 (stetig). Wasserstoff haette dann halbzahlige Bahndrehimpulse und n^2 - mu^2 Zustaende. Quantenmechanisch ist mu gequantelt (Dirac) [L], der stetige Schub kann dort also keine Symmetrie sein [ES]. | ja, und **entschieden**: 1s existiert, n^2-Entartung, also mu = 0 im Laborsystem. Eine physikalische zweite Zeit braeuchte ein ausgezeichnetes System [ES]. |
| S2/S5: kontinuierliche Fock-S^3 gegen Netz-S^3 im Impulsraum | 120 Punkte geben nur 6 Schalen, n = 7 fehlt | ja, **trivial entschieden**: Rydberg-Zustaende mit n weit ueber 7 [L]. Fuer ein Ortsraum-Netz erst bei Wellenlaenge ~ Netzradius. |
| S3: Faserladung s = 0 gegen s ungleich 0 | Entartung n^2 - s^2, halbzahlige Drehimpulse | ja, **entschieden**: s = 0 [L]. |
| S4: Bezout-Grad gegen scharfe Schranke | Linsen aus n >= 4 Punktmassen (17 gegen 15) | praktisch nein: Mikrolinsen-Bilder sind nicht aufgeloest [L?] |
| Netz gegen Kontinuum (exaktes 1/r) | Gitterkorrektur ~ (l/r)^2 mit kubischer Winkelform. Sie bricht SO(4) zuerst bei n = 3: 3d spaltet in 2 + 3 (e_g + t_2g, "Kristallfeld des Vakuums") [M] | nein: Groesse etwa 13,6 eV x (l/a0)^2, also etwa 2e-33 eV bei l = 7e-28 m und darunter fuer kleinere l [P LICHT-FINN-NETZ-1; M; H, dass das Netz das Coulombfeld traegt] |

## 6. 4D-Ideen fuer Finns Programm

| Idee | Bezug | Ableitbarkeitsprobe | kleiner Test (<= 10 min) | Datenbezug |
|---|---|---|---|---|
| **I1 Zweite Zeit:** Kepler-Bahnen als Lichtkegel-Schnitte in einer 4D-Hilfsraumzeit mit x0 = r; ein Schub darin macht aus Kepler ein MICZ-Problem (Monopol) | Licht, Wasserstoff, Monopol (LADUNG-MONOPOL-L, QBALL-MONOPOL-1), Zwei-Zeiten-Physik (Bars, RUNDE-22/dunkel-zeit) [P] | vollstaendig ableitbar bzw. Literatur (Meng Gl. (2.11), (3.5), Satz 2). Nichts Netzspezifisches. | Schreibtisch: Schub entlang L auf (a, l) einer Kepler-Bahn, mu' und E' ueber Gl. (3.2) ablesen. Prueft nur Meng nach. | Wasserstoff verlangt mu = 0 im Laborsystem. Offen bleibt Mengs Frage, ob die zweite Zeit mehr ist als ein Artefakt. |
| **I2 Fock-Schalen auf S^3-Netzen:** Wie weit tragen Finns Netze, auf S^3 geschlossen, das Schalenmuster n^2? | Netz, Wasserstoff (UNSCHAERFE-KANTE-L laeuft parallel), GEOMETRIE-XD | 600-Zelle: vollstaendig ableitbar [M]. 120-Zelle: nur teilweise; das 11-Design sichert die harmonischen Anteile, nicht Reihenfolge und Mischung. Kantengraph = 120-Zelle (gleiche Laplace-Niveaus) plus flaches Band [M]. | 120 x 120, 600 x 600 und 1200 x 1200 Eigenwerte auf der .69 (Sekunden) | keiner im Ortsraum. Im Impulsraum gelesen trivial widerlegt (Rydberg). |
| **I3 Hopf-Faser als vierte Richtung:** 3D-Coulomb = 4D-Oszillator; die Faserladung erscheint als Monopol, der ungerade Sektor als halber Spin | Q-Ball-Phase, Spin 1/2, Ladung plus Monopol [P] | vollstaendig ableitbar (Zaehlung n^2 - s^2 [M]; Nersessian 2000, Mardoyan/Petrosyan 2006 [S Abstract]) | keiner noetig, Zaehlung von Hand erledigt | Wasserstoff: s = 0 |
| **I4 Bezout-Zaehlung von Lichtkegeln und Linsen:** wie viele Ereignisse bzw. Bilder hoechstens; Netz-Kegel mit a2-Verformung | Licht, Netz | Linsen: Literatur (5n - 5). Lichtkegel: [M] hoechstens 2. Netz-Kegel: Bezout-Grenze waechst (Quartik), reelle Zusatzloesungen erst bei k l ~ 1 [H] | reelle Schnittpunkte von 4 verformten Kegeln zaehlen, ueber k l = 0,01 bis 1 | Positionsbestimmung (2 Loesungen) [L?]; Mikrolinsen mit 3 Linsen gibt es [L?], Bildzahl nicht aufgeloest |
| **I5 4-Simplex-Netz mit der 600-Zelle als Eckfigur:** fuenf 4-Simplexe je Dreieck schliessen hyperbolisch ({3,3,3,5}), vier je Dreieck sphaerisch ({3,3,3,4}) | PACHNER-TAKT-1, CDT, GEOMETRIE-XD (Zeile d = 4) [P] | Winkel ableitbar [M] (75,52 Grad; Ueberschuss 17,6 Grad bei 5); Existenz und Eckfigur [L? Coxeter] | Schreibtisch: Defizit je Dreieck fuer n = 4 und 5, Kruemmungsradius von {3,3,3,5} in Kanteneinheiten | schwach [H]: Ein euklidisches de-Sitter-Universum (Lambda > 0, S^4) braucht im Mittel weniger als 4,77 Simplexe je Dreieck; reine Fuenferpackung gaebe das falsche Vorzeichen |
| **I6 Netz-Lichtkegel, schraeg geschnitten:** Abweichung von e = v durch das kubische Muster | Licht (LICHT-FINN-NETZ-1: a2 laengs der Achsen -1/12, laengs der Raumdiagonalen -1/9) [P] | vollstaendig aus a2 ableitbar, Ordnung (k l)^2 [M] | Schnitt der Gruppengeschwindigkeitsflaeche mit t = a + v x bei k l = 0,1 und 0,3 | nur die bekannte LHAASO-Schranke [P], nichts Neues |

- Nicht aufgenommen, weil Projektbestand [P]: Keplers Abstandsgesetz des Lichts (1/r^2) fuehrt ueber Gauss, Ehrenfest
  und Tangherlini zu "stabile Bahnen und Atome nur in D = 3". Das steht in n-dimensionen-grundlagen-20260912.md und
  DIM-AUSWAHL-L.

## 7. Kartenvorschlag (einer): FOCK-SCHALEN-S3-1

**Frage:** Tragen Finns Netze, auf S^3 geschlossen, das Wasserstoff-Schalenmuster 1, 4, 9, 16, ... in den untersten
Graph-Laplace-Niveaus? Bis zu welcher Schale reicht es, und haengt es von der Kopplungszahl ab?
- 600-Zelle: Tetraeder-Dichtpackung, 12 Kanten je Ecke
- 120-Zelle: Diamant-Gegenstueck, 4 Kanten je Ecke
- Kantengraph der 120-Zelle: Pyrochlor-Gegenstueck, 6 Kanten je Ecke

**Ableitbarkeitsprobe (vorab):**
- 600-Zelle: vollstaendig ableitbar (Abschnitt 4, S5) [M]. Im Test nur Kontrolle.
- Kantengraph der 120-Zelle:
  - Laplace-Niveaus wie bei der 120-Zelle: L_L = 6 - (lambda + 2) = 4 - lambda = L_G.
  - Dazu ein flaches Band bei L = 8 mit Vielfachheit m - n = 600, weil die 120-Zelle Fuenferringe hat und nicht
    bipartit ist [M]. Kontrolle.
- 120-Zelle:
  - Vorab bekannt: Ihre Ecken bilden eine H4-Bahn, also [L?] ein 11-Design. Die Kugelfunktionen vom Grad <= 5 bleiben auf
    den 600 Punkten linear unabhaengig.
  - Nicht vorab bekannt: ob diese Anteile Eigenraeume sind und ob sie die untersten sind. Die Permutationsdarstellung
    auf 600 Punkten enthaelt manche Typen doppelt (Stabilisator der Ordnung 24), fuer Grad 3 nach meiner Zaehlung
    zweimal [M, ungeprueft].
  - Die Rechnung ist darum keine reine Wiederholung.
- Projekt-grep (alle Dateitypen, mit den Pflicht-Ausschluessen, 06:14 bis 06:30):
  - "120-Zelle"/"120-cell": nur eine Dualitaetszeile in RUNDE-17/quellen-frustration/DOSSIER.md (Z. 145) und
    Quellenkopien.
  - "4-Fulleren", "Deza", "{3,3,3,5}": 0 Treffer.
  - "Graph-Laplace" bzw. "Laplace-Spektrum" zusammen mit der 600-Zelle: 0 Treffer.
  - "Fock" nur als Fock-Raum (Karte). Ein Treffer "R120-Zellen" (RUNDE-16) meint etwas anderes.

**Vorhersagen (vor jeder Rechnung; FS1 und FS2 koennen scheitern, FS0, FS3 und FS4 sind Kontrollen der
Schreibtischrechnung):**

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| FS0 | 600-Zelle: Laplace-Niveaus 0; 12 - 6 phi; 12 - 4 phi; 9; 12; 14; 12 - 4 phi'; 15; 12 - 6 phi' mit Vielfachheiten 1, 4, 9, 16, 25, 36, 9, 16, 4 (Toleranz 1e-9) | Kontrolle [M] | 97 % |
| FS1 | 120-Zelle: Die sechs untersten verschiedenen Niveaus haben die Vielfachheiten 1, 4, 9, 16, 25, 36, in dieser Reihenfolge | [H] | 50 % |
| FS2 | 120-Zelle: lambda_2/lambda_1 (die ersten beiden von null verschiedenen) liegt naeher an 8/3 als bei der 600-Zelle: Abstand zu 8/3 kleiner als 0,255, also im offenen Intervall (2,412; 2,922) | [H] | 60 % |
| FS3 | Kantengraph: Laplace-Niveaus unterhalb 8 gleich denen der 120-Zelle (1e-9), flaches Band bei 8 mit Vielfachheit 600 | Kontrolle [M] | 95 % |
| FS4 | 120-Zelle: Unter den untersten 140 Zustaenden gibt es kein 49-faches Niveau. Grund [M]: Unter 2I gilt V_3 = 3' + 4', also zerfaellt der Grad-6-Raum unter H4 in 9 + 24 + 16. Ein 49-faches Niveau braeuchte eine zufaellige Entartung. | Kontrolle [M] | 95 % |

**Bedeutung je Ausgang:**
- **FS1 trifft ein:**
  - Das Schalenmuster ist eine Eigenschaft der H4-Schliessung von S^3, nicht der Kopplungszahl.
  - Finns Diamant traegt auf S^3 die Wasserstoff-Schalen bis n = 6.
  - Das ist anschaulich, ohne Datenbezug.
- **FS1 trifft nicht ein:** Die Kopplungszahl entscheidet, und die 600-Zelle ist ein Sonderfall (normaler
  Cayley-Graph). Der Satz "Finns Netz traegt das Wasserstoff-Muster" gilt fuer das Diamant-Gegenstueck dann nicht.
- **FS2** misst, wie schnell ein S^3-Netz das Kontinuum erreicht, als Vorstufe einer Leiter ueber groessere
  4-Fullerene.
- **FS0, FS3 oder FS4 scheitern:** Meine Schreibtischrechnung ist falsch. Dann ist KB3 neu zu urteilen.

**Test:**
- Ecken der 120-Zelle als die 600 Einheitsquaternionen in den ueblichen Koordinaten (Permutationen mit phi). Die Kanten
  verbinden naechste Nachbarn.
- Dichte Diagonalisierung (600 x 600 und 1200 x 1200), 1 Thread.
- .69, kleintest.sh, p4000 bzw. cpu, unter 1 min.
- Mit Plan- und Code-Einfrieren nach Projektbrauch.

**Datenbezug:** keiner. Nach der Neuausrichtung vom 22.09. ist das ein modellinterner Geometrie-Strang. Die Leitung
entscheidet, ob er in v3 als kleiner Test laufen darf.

## 8. Gegensweep (Regel 4)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- **G1, geprueft:**
  - Die 12 Nachbarn einer Ecke der 600-Zelle bilden eine Konjugationsklasse von 2I: Realteil phi/2, Klassengroessen
    1, 1, 30, 20, 20, 12, 12, 12, 12.
  - Nur deshalb gilt die Charakterformel. Dazu kommen drei Spurproben (Abschnitt 3). Bestanden.
- **G2, geprueft (Projektdatei):** Finns Netz ist Diamant/Pyrochlor, nicht die 600-Zelle. Daraus folgt V3 und die Wahl
  des Kartenvorschlags.
- **G3, geprueft (Projekt-grep):**
  - Ehrenfest, Tangherlini, Bertrand und Tegmark sind Projektbestand (n-dimensionen-grundlagen-20260912.md,
    DIM-AUSWAHL-L).
  - Bars' Zwei-Zeiten-Physik ebenso (RUNDE-22/dunkel-zeit, Abruf I1d).
  - Keplers Abstandsgesetz habe ich deshalb nicht als neue Idee gefuehrt. Mengs zweite Zeit dockt an Bars an; ob es
    dieselbe ist, ist offen.
- **G4, nicht geprueft:** Focks S^3 liegt im Impulsraum. "Wasserstoff auf der 600-Zelle" vermischt Ort und Impuls.
  Das steht hier aus dem Gedaechtnis [L].
- **G5, nicht geprueft:** Wasserstoff hat mit Spin 2 n^2 Zustaende; alle n^2-Vergleiche hier sind spinlos.
- **G6, teilweise geprueft:** Die Nullergebnisse A3 und A8 sind wohl Wortwahl, nicht Syntax: A5 mit AND und Klammern
  lieferte einen Treffer. Ganz ausgeschlossen ist ein Suchfehler nicht.

## 9. Kalibrierung

- **(a) Gemessen bzw. an der Quelle gelesen:**
  - Mengs Gleichungen (2.3), (2.5), (2.8), (2.11), (2.12), (3.5), Satz 2 und S. 7 [S].
  - Die Abstracts von Rhie 2001/2003, Khavinson/Neumann, Mardoyan/Petrosyan, Nersessian, Lavrenov, Mardoyan/Nersessian,
    Ballesteros u. a., MacKay/Salour, Deza/Shtogrin, Cohn/Kumar, Niu/Kamien und Tsuda/Fujiwara.
  - Gemessen im Sinn von Rechenlaeufen: nichts.
- **(b) Nuetzlich verdichtet:**
  - das 600-Zellen-Spektrum mit drei Spurproben [M]
  - die Lesart "vierte Dimension = Hilfsdimension" als Moderator [ES]
  - SO(4,2) bzw. exaktes 1/r als gemeinsame Kopplungsgroesse [ES, L?]
  - die Zuordnung Diamant -> 120-Zelle [M]
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - KB2 (Kepler 1604)
  - {3,3,3,5} mit der 600-Zelle als Eckfigur
  - Schroedingers S^3-Formel
  - Barut/Kleinert
  - das 11-Design
  - die Lesart der Spiegelniveaus als Bruchstuecke der Schalen n = 7 und 8
  - Alles das steht hier ohne Quelle bzw. ohne volle Rechnung.
- **Warnzeichen:** Waehrend der Recherche stieg meine Sicherheit, dass alles "nur Umbenennung" ist. Zugleich loeste sich
  die Frage feiner auf: Meng nennt die zweite Zeit ausdruecklich eine offene Frage. "Umbenennung" ist darum fuer S1 ein
  Urteil ueber die heutige Datenlage (mu = 0), keine Widerlegung.

## 10. Offene Fragen

1. Meint Finn mit "4D-Tetraeder-Netz" die 600-Zelle (Dichtpackung), die 120-Zelle (Diamant auf S^3) oder ein Netz aus
   4-Simplexen (Pachner/CDT, I5)? (Rueckfrage an die Leitung)
2. Ist Mengs zweite Zeit dieselbe wie die zweite Zeit in Bars' 2T-Physik [P RUNDE-22]? Nicht geprueft.
3. KB2: Kepler 1604, Sekundaerquelle noch nicht gelesen.
4. Ist das Graph-Spektrum der 600-Zelle in Tabellen distanzregulaerer Graphen verzeichnet (Brouwer/Cohen/Neumaier 1989)
   [L?]? Damit waere FS0 zitierbar statt nur gerechnet.
5. Gibt es eine Verfeinerungsleiter (4-Fullerene), auf der die Spiegelzustaende nach oben wandern und das Kontinuum
   l(l + 2) erreicht wird?

## 11. Selbstanzeigen

- Einen leeren http-Abruf (06:18:19, 0 Byte) habe ich wiederholt und nicht als Abruf gezaehlt.
- A2 lief als arXiv-API-Abruf mit drei IDs statt, wie in der Erwartung notiert, per WebFetch auf arxiv.org/abs. Das
  ergab mehr Inhalt bei gleicher Abrufzahl; die Methode habe ich nach der Erwartung geaendert.
- WebFetch konnte das PDF zu A6 nicht lesen. Die vom Werkzeug abgelegte Datei habe ich nach quellen/ kopiert und mit dem
  Read-Werkzeug gelesen. Der Dateiname enthaelt die Kopierzeit.
- Alle Zahlen sind Kopfrechnung ohne Gegenlesen. Die Spurproben pruefen das 600-Zellen-Spektrum, nicht die
  Wasserstoff-Deutung.
- Die Zaehlung "Grad 3 doppelt" in der 600-Punkt-Darstellung der 120-Zelle ist eine ungepruefte Ueberschlagsrechnung.
- KB2 ist nicht entschieden. Ich habe es nicht als eingetroffen gewertet, obwohl ich es fuer richtig halte.
- Zuschreibungsfehler, berichtigt vor Abgabe: In der ersten Fassung (und im ARBEITSFELD) stand "Nersessian/Pogosyan
  2000" aus dem Gedaechtnis. Laut Abrufdaten ist math-ph/0010049 von A. Nersessian allein. Ebenso habe ich vor Abgabe
  einen geratenen Autorennamen fuer 1406.5866 durch die Namen aus den Abrufdaten ersetzt (MacKay/Salour).
- Die "halber Spin"-Aussage aus Nersessian 2000 gilt woertlich fuer die 2D-Bohlin-Abbildung; die 3D/KS-Fassung ist
  meine Zaehlung (V4).
- In UNSCHAERFE-KANTE-L habe ich nur die Karte gelesen und dort nichts geschrieben.

## 12. Quellenliste

Abrufe:
- A1 (06:18:26) arXiv-API all:"600-cell", 41 Treffer: quellen/A1-arxiv-600cell-20261005-061826.xml
- A2 (06:19:38) arXiv-API id_list math/0401188, astro-ph/0305166, astro-ph/0103463: quellen/A2-arxiv-linsen-20261005-061938.xml
- A3 (06:19:53) arXiv-API Kustaanheimo AND monopole, 0 Treffer: quellen/A3-arxiv-ks-monopol-20261005-061953.xml
- A4 (06:20:12) arXiv-API MICZ OR "MIC-Kepler", 46 Treffer: quellen/A4-arxiv-micz-20261005-062012.xml
- A5 (06:21:40) arXiv-API au:Meng AND Kepler AND (...), 1 Treffer: quellen/A5-arxiv-meng-kepler-20261005-062140.xml
- A6 (06:22) arxiv.org/pdf/1111.2277 per WebFetch, PDF-Kopie: quellen/A6-arxiv-1111.2277-pdf-abgerufen-20261005-0622-kopie-20261005-062214.pdf
- A7 (06:23:47) arXiv-API all:"120-cell", 24 Treffer: quellen/A7-arxiv-120cell-20261005-062347.xml
- A8 (06:24:12) arXiv-API Kepler AND (Paralipomena OR ...), 0 Treffer: quellen/A8-arxiv-kepler-1604-20261005-062412.xml

Zitierte Arbeiten (Autor, Jahr, Titel, URL):
- G. Meng (2012), Lorentz Group and Oriented MICZ-Kepler Orbits, J. Math. Phys. 53, 052901,
  https://arxiv.org/abs/1111.2277 [S]
- G. W. Meng (2009), Euclidean Jordan Algebras, Hidden Actions, and J-Kepler Problems, https://arxiv.org/abs/0911.2977
  [zitiert in Meng 2012, nicht gelesen]
- D. Khavinson, G. Neumann (2004/2006), On the number of zeros of certain rational harmonic functions,
  https://arxiv.org/abs/math/0401188 [S Abstract]
- S. H. Rhie (2001), Can a gravitational quadruple lens produce 17 images?, https://arxiv.org/abs/astro-ph/0103463
  [S Abstract]
- S. H. Rhie (2003), n-point gravitational lenses with 5(n-1) images, https://arxiv.org/abs/astro-ph/0305166
  [S Abstract]
- L. G. Mardoyan, M. G. Petrosyan (2006/2007), 4D singular oscillator and generalized MIC-Kepler system, Phys. Atom.
  Nucl. 70, 572, https://arxiv.org/abs/quant-ph/0604127 [S Abstract]
- A. Nersessian (2000/2002), How to relate the oscillator and Coulomb systems on spheres and pseudospheres?, Phys. Atom.
  Nucl. 65, 1070, https://arxiv.org/abs/math-ph/0010049 [S Abstract; laut Abrufdaten Einzelautor]
- A. Lavrenov (2019), Generalized KS transformations, ND singular oscillator and generalized MICZ-Kepler system,
  https://arxiv.org/abs/1908.03572 [S Abstract]
- L. Mardoyan, A. Nersessian (2026), Generalized MICZ-Kepler systems on three-dimensional sphere and hyperboloid,
  https://arxiv.org/abs/2601.13028 [S Abstract]
- A. Ballesteros, A. Enciso, F. J. Herranz, O. Ragnisco (2008), Bertrand spacetimes as Kepler/oscillator potentials,
  https://arxiv.org/abs/0803.3430 [S Abstract]
- N. J. MacKay, S. Salour (2014), Kepler unbound: some elegant curiosities of classical mechanics,
  https://arxiv.org/abs/1406.5866 [S Abstract]
- R. Montgomery (2013), MICZ-Kepler = dynamics on the cone over the rotation group, https://arxiv.org/abs/1305.1063
  [S Abstract, im Abruf A4 mitgekommen, nur Titel und Abstract]
- H. Cohn, A. Kumar (2006), Universally optimal distribution of points on spheres, https://arxiv.org/abs/math/0607446
  [S Abstract]
- L. Niu, R. D. Kamien (2026), Variations on the Three-Sphere: Laves' Labyrinth Lopped,
  https://arxiv.org/abs/2604.12971 [S Abstract]
- R. Tsuda, T. Fujiwara (2020), Oscillating 4-Polytopal Universe in Regge Calculus, https://arxiv.org/abs/2011.04120
  [S Abstract]
- M. Deza, M. I. Shtogrin (1999), Three, four and five-dimensional fullerenes, https://arxiv.org/abs/math/9906035
  [S Abstract]
- N. P. Konstantinidis (2022), Classical magnetization of a four-dimensional Platonic solid,
  https://arxiv.org/abs/2207.11077 [S Abstract]
- R. V. Moody, J. Morita (2017), Discretization of SU(2) and the Orthogonal Group Using Icosahedral Symmetries and the
  Golden Numbers, https://arxiv.org/abs/1705.04910 [S Abstract]
- Aus dem Gedaechtnis, nicht abgerufen:
  - V. Fock 1935, Z. Phys. 98, 145 [L]
  - M. Bander, C. Itzykson 1966, Rev. Mod. Phys. 38, 330/346 [L]
  - P. Kustaanheimo, E. Stiefel 1965, J. Reine Angew. Math. 218, 204 [L]
  - J. Kepler 1604, Ad Vitellionem Paralipomena [L?]
  - J. V. Field 1986, Stud. Hist. Phil. Sci. 17, 449 [L?]
  - E. Schroedinger 1940, Proc. R. Irish Acad. 46, 9 [L?]
  - P. W. Higgs 1979, J. Phys. A 12, 309 [L?]
  - H. I. Leemon 1979, J. Phys. A 12, 489 [L?]
  - A. O. Barut, H. Kleinert 1967, Phys. Rev. 156, 1541 [L?]
  - H. S. M. Coxeter, Regular Polytopes [L?]
  - J.-F. Sadoc, R. Mosseri, Geometrical Frustration 1999 [L?, im Projekt zitiert]
  - Abel/Chaffee 1991 [L?]
  - Coll u. a. [L?]
  - Neumann 1998 [L?]

Projektdateien [P]:
- RUNDE-27/GEOMETRIE-XD.md
- RUNDE-37/licht-finn-netz-1/ERGEBNIS.md
- RUNDE-37/dim-leiter-qball-1/ERGEBNIS.md
- RUNDE-37/pachner-takt-1/ERGEBNIS.md
- RUNDE-37/unschaerfe-kante-l/KARTE.md
- RUNDE-37/ladung-monopol-l/DOSSIER.md
- RUNDE-37/qball-monopol-1/ERGEBNIS.md
- RUNDE-37/dim-auswahl-l
- RUNDE-22/dunkel-zeit
- RUNDE-17/quellen-frustration/DOSSIER.md

## 13. Einfach gesagt

Kepler sah, dass Kreis, Ellipse, Parabel und Hyperbel eine Familie sind. Man bekommt sie, wenn man eine schraege Ebene
durch einen Kegel legt, und zwar umso schraeger, je gestreckter die Bahn ist. Ein Mathematiker hat 2012 gezeigt, dass genau
das die Planetenbahnen beschreibt, wenn man den Abstand zur Sonne wie eine zweite Zeit behandelt. Das ist eine schoene
Umrechnung, aber keine neue Physik, und diese "vierte Richtung" ist nicht unsere Raumzeit. Spannend fuer Finns Netz ist
eine Rechnung zur 600-Zelle, einem 4D-Koerper aus Tetraedern. Ihre Schwingungen haben genau die Stufen 1, 4, 9, 16, 25
und 36 wie die Schalen im Wasserstoffatom, und ein kleiner Test soll klaeren, ob Finns Diamant-Netz auf der 4D-Kugel das
auch kann.
