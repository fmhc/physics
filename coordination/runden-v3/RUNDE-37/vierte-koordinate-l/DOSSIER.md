# VIERTE-KOORDINATE-L: Dossier (feldforscher fuer die Leitung claude-primary, Runde 49, Finns Fragen)

## 1. Kopf

- **Auftrag:** Finn, 05.10.2026, woertlich (aus KARTE.md):
  - "Aber warum keine mehr Dimensionen wenn Teile sich in 3d noch nicht direkt zu Dreiecken zusammen gesetzt haben, eine temporäre 4. Dimension wäre doch da ggf sinnvolle oder?" (Eingang vor 11:54:35)
  - "Oder eine Drehdimension dann quasi mit Spin" (Eingang vor 12:01:29)
  - Karte KARTE.md bindend; VK1 bis VK6 und ihre Bedeutung unveraendert.
- **Zeiten (alle per date, CEST, 2026-10-05):**
  - Start 2026-10-05 12:02:37.
  - Erste Erwartung vor einem Netzabruf 12:11:57; Ausgang des letzten Abrufs (Nr. 20) 12:26:47.
  - Dossier-Text ab 12:30:30; Kopf zusammengesetzt 12:37:39.
  - Abgabe: letzte Zeile dieser Datei.
- **Abrufe: 20 von 20** (21 Netzaufrufe, siehe Selbstanzeige 2):
  - 7 WebSearch (Abrufe 1, 3, 9, 11, 12, 17, 18);
  - 1 WebFetch (Abruf 2, mit Umleitung);
  - 12 curl: arXiv-API 6 (Abrufe 4 leer, 5, 10, 13, 15, 19), INSPIRE-API 5 (6, 7, 14, 16, 20), PDF 1 (8).
  - Kopien in quellen/ (Dateiname mit Abrufzeit).
- **Ohne Abrufzaehlung lokal gelesen:** Kleman/Friedel 2008, Tarjus u. a. 2005, Will 2014 (Projektkopien), KEGEL-4D-L A1, Projektdateien (P-1 bis P-8 im Arbeitsfeld).
- **Kennzeichen:**
  - [S] an der Quelle gelesen, mit Abschnitt, Gleichung oder Seite; [S lokal] Projektkopie gelesen.
  - [S Abstract] nur Abstract; [S Gliederung] Inhaltsverzeichnis gelesen; [S Treffer] nur Suchtreffer bzw. Trefferzusammenfassung (sekundaer).
  - [L] Gedaechtnis, [L?] unsicher; [P] Projektbefund mit Fundstelle.
  - [M] Schreibtisch-Mathematik (Kopf, ohne zweiten Leser; M1 bis M7 im Arbeitsfeld); [ES] eigener Schluss; [H] Hypothese.
- **Art:** Literatur und Schreibtisch. Keine Rechnung, keine Messdaten, keine Messdatenbestaetigung.
- **Arbeitsfeld:** ARBEITSFELD.md, mit allen Erwartungen vor jedem Abruf, Ausgaengen, M1 bis M7, Gegensweep (G1 bis G6) und offenen Rueckfragen.

## 2. Ergebnis zuerst

1. **Finns "voruebergehende vierte Dimension" gibt es in der Literatur, und zwar dreifach; fuer Umklappzuege ist die
   genaueste Form die Hebehoehe.**
   - Delaunay in 3D = Projektion der unteren Huelle der auf (x, |x|^2 - w) gehobenen Punkte in R^4. Ein 2-3-Zug ist
     der Augenblick, in dem die fuenf gehobenen Punkte in einer Hyperebene liegen; der gehobene 4-Simplex hat dann
     4-Volumen null [M; Erickson/Lin 2020 S Abstract; Brown 1979 S Treffer].
   - Im 4D-Regge-Kalkuel ist die vierte Richtung eines 2-3-Zugs die Zeit: Pachner-Zuege sind dort Zeitschritte
     (Dittrich/Hoehn, Hoehn 2015) [P HODGE-L]. Als Kruemmung ist sie die S^3 der 600-Zelle [P; Sadoc/Mosseri S
     Gliederung].
   - Browns Kugel-Hebung fuehrt auf genau diese S^3: Hebe-Kugel, 600-Zellen-Kugel und Drehgruppe SU(2) sind dieselbe
     3-Sphaere [M].
2. **Die Hebehoehe ist eine Spannungsfunktion, keine neue Koordinate [S Abstract, S, M].**
   - Maxwell/Cremona: Eine Hebung ist gleichwertig mit einer positiven Eigenspannung und einem orthogonalen Dual
     (Potenzdiagramm). In der Ebene sind alle drei gleich "gewichtete Delaunay" (Erickson/Lin 2020). Auf flachen Tori,
     also bei periodischen Netzen wie Finns, gilt die Gleichwertigkeit nur eingeschraenkt.
   - Die Hoehe ist nur bis auf affine Funktionen bestimmt [M1]. Auf die Regge-Wirkung wirkt sie bei festen Kantenlaengen
     gar nicht [M2]; sie wirkt ueber den Hodge-Stern der Materie und ueber die Wahl der Zerlegung (de Goes u. a. 2014,
     Gl. 13 und Abschn. 2.4 [S]).
   - Gueltige Gewichte werden im Kontinuum konstant (de Goes u. a. 2014, Abschn. 4.2 [S]). Ohne Zusatzannahme ist die
     Hoehe also eine Gitterfreiheit, kein langreichweitiges Feld [ES].
3. **Eine dynamische Hebehoehe als Feld in diskreter Gravitation fand ich nicht (VK5 nicht eingetroffen, nach
   Recherchestand, mit 24-Monats-Suche).**
   - Nahtreffer [S Treffer bzw. S Abstract]: Laguerre-Gewichte als Unbekannte der Rekonstruktion des fruehen Universums
     bzw. einer Euler-Stroemung; Kaehler-Moduli mit Kammern topologisch verschiedener Raeume und Topologieaenderung an
     den Waenden (Aspinwall/Greene/Morrison 1994, Witten 1993). Dass diese Kammern regulaere Triangulierungen sind und
     die Kaehler-Parameter deren Hoehen, ist [L].
   - Waere die Hoehe ein universell gekoppeltes Feld, haengt die Schranke an ihrer Reichweite: lang -> Cassini
     |gamma - 1| ~ 2e-5; kurz -> keine Abweichung vom 1/r^2-Gesetz zwischen einigen 10 nm und 10 mm; gitterskalig ->
     LHAASO E_QG,1 > 10 E_Pl. MICROSCOPE (eta ~ 1e-15) greift nur bei Zusammensetzungsabhaengigkeit [S; M7].
4. **Eine Drehdimension gibt Ladung; Spin gibt sie erst, wenn sie an die Raumdrehungen gekoppelt ist (VK3
   eingetroffen; fuer bosonische Felder [M], Mechanismus [S Abstract]).**
   - Im Monopolfeld werden Isospinor-Freiheitsgrade zu Spin (Jackiw/Rebbi 1976). Bosonen mit halbzahligem Isospin
     geben gebundene Fermionen (Hasenfratz/'t Hooft 1976). Die Spin-Statistik-Verbindung bleibt erhalten (Goldhaber
     1976) [S Abstract].
   - Auf S^3 = SU(2) gilt [M6]: Ein halber Umlauf laengs der Hopf-Faser ist eine volle 2-pi-Drehung des Rahmens. Der
     60-dimensionale Raum der ungeraden Funktionen auf den 120 Ecken der 600-Zelle traegt nur spinorielle Darstellungen
     von 2I.
   - Das zaehlt als Spin aber nur, wenn Raumdrehungen einseitig auf die S^3 wirken (Rahmen, Kreisel). Bei Drehung um
     einen Punkt der S^3 (Konjugation) entstehen nur ganze Spins.
5. **VK1, VK2 eingetroffen; VK4 im Kern eingetroffen; VK6 teilweise eingetroffen.**
   - Begutachtet ist die Spinor-Struktur der 600-Zelle: Dechant 2013 [S Abstract]; Kleman/Friedel 2008, wo die
     Defektalgebra des {3,3,5}-Kristalls SU(2) mit dem Element -1 braucht [S lokal].
   - Ein begutachtetes Gittermodell mit Spin-1/2-Freiheitsgraden auf der 600-Zelle fand ich nicht. Der einzige formale
     Treffer (Fermionen im quasikristallinen Spinschaum, 2023) ist nicht als begutachtet festgestellt und stammt aus dem
     E8/H4-Umfeld.

## 3. Urteile VK1 bis VK6

| Nr | Vorhersage (Karte, woertlich) | Wahrsch. | Urteil | Beleg mit Fundstelle |
|---|---|---|---|---|
| VK1 | Kontrolle [M, L]: Die 120 Ecken der 600-Zelle sind die binaere Ikosaedergruppe 2I (Ordnung 120) in SU(2) = S^3 (Einheitsquaternionen, "Icosians") | 95 % | **eingetroffen** | Dechant 2013, Acta Cryst. A69, 592 [S Abstract, lokal KEGEL-4D-L A1]: "The spinors arising from the Platonic Solids can thus in turn be interpreted as vertices in four-dimensional space, giving a simple construction of ... the 600-cell". Ewha-Arbeit "Binary icosahedral group and 600 cell" (Symmetry, Aug. 2018) [S Treffer, Abrufe 3, 18]: 2I als Teilmenge der Quaternionen ueber die Spin-Abbildung von SO(3), gleich den Ecken der 600-Zelle. Treffertext Abruf 18: "icosians, which are quaternion coordinates of the 120 elements of the binary icosahedral group 2I" [S Treffer]. Baez 2018 [S Abstract lokal]: Icosians, 600-Zelle, Poincare-Sphaere. Ordnung 120 [M]. |
| VK2 | [L] Sadoc/Mosseri beschreiben dichte Tetraederpackungen ueber die 600-Zelle auf S^3 und ihre Hopf-Faserung; Disklinationen entstehen beim "Abflachen" | 75 % | **eingetroffen** (Gliederungs- und Trefferebene; Buchtext nicht gelesen) | Cambridge-Kapitelseite [S Gliederung, Abruf 2]: Kap. 2 "Ideal models", Kap. 4 "Decurving and disclinations", Anh. A2 "Quaternions and related groups", A3 "Hopf fibration", A5 "Polytope {3, 3, 5}". Anfang A3 woertlich: "A space can be considered as a fibre bundle if there is a sub-space (the fibre) which can be reproduced by a displacement so that any point of the space is on a fibre, and only one." Sadoc 2001, EPJ E [S Treffer, Abruf 1]: {3,3,5} als Vorlage dichter Strukturen, groessere Strukturen ueber Disklinationen, "discretised version of the Hopf fibration". Kleman/Friedel 2008, Abschn. VI.A.4, S. 39 [S lokal]: Dekurvierung der {3,3,5} durch Disklinationen negativer Staerke (nach Kleman/Sadoc 1979). WELTKRISTALL-L V4 [P] hatte auf arXiv keinen solchen Sadoc/Mosseri-Abstract gefunden; die Zuschreibung ist jetzt ueber die Buchgliederung belegt. |
| VK3 | [L] Ein innerer Raum SU(2) (Kaluza-Klein) liefert Eichladungen bzw. Isospin, keinen Raumzeit-Spin. Spin 1/2 aus Bosonen braucht eine zusaetzliche Kopplung an die Raumdrehungen, etwa einen Monopol (Jackiw/Rebbi, Hasenfratz/'t Hooft 1976) | 70 % | **eingetroffen** (Satz 2 an den Abstracts; Satz 1 ueber einen Abstract und [M]) | Jackiw/Rebbi, PRL 36, 1116 [S Abstract, Abruf 6]: "isospinor degrees of freedom are converted into spin degrees of freedom in the field of a magnetic monopole". Hasenfratz/'t Hooft, PRL 36, 1119 [S Abstract]: Isospin ganz bzw. halbzahlig -> Gesamtdrehimpuls ganz bzw. halbzahlig; "we can obtain fermions this way in a theory that started off with bosons only". Goldhaber, PRL 36, 1122 [S Abstract]: Spin-Statistik bleibt. Satz 1: Witten 1981, NPB 186, 412 [S Abstract, Abruf 7]: sieben kompakte Dimensionen geben eine Eichgruppe SU(3) x SU(2) x U(1), "but the proper fermion quantum numbers are difficult to achieve"; dass innere Bewegung Ladung und nicht 4D-Spin traegt, ist [M] (KK-Moden tragen Darstellungen der Isometriegruppe; der 4D-Spin stammt aus der 4D-Lorentzgruppe). |
| VK4 | [L] Die Delaunay-Hebeabbildung und gewichtete Delaunay mit Hoehen \|x\|^2 - w stehen so in der Literatur; Potenzdiagramm-Duale geben gewichtete Hodge-Sterne in DEC | 85 % | **im Kern eingetroffen**; die Formel \|x\|^2 - w selbst habe ich an keiner Quelle gesehen (nur [M] aus dem Potenzabstand) | Erickson/Lin 2020 [S Abstract, Abruf 10]: "the well-known correspondence between convex hulls and weighted Delaunay triangulations"; kohaerent (gewichteter Delaunay-Graph) ist in der Ebene gleich "the projection of the 1-skeleton of the lower convex hull of points in R^3". Brown 1979 [S Treffer, Abruf 17]: konvexe Huellen plus Inversion, auch hoehere Dimensionen. de Goes u. a. 2014 [S, Abruf 8]: Def. 6 und Gl. (1) (duale Ecke = Umkreismitte - 1/2 grad w), Prop. 1 (orthogonales Dual), Gl. (2) d_ij = (l_ij^2 + w_i - w_j)/(2 l_ij), Abschn. 2.4 ("power distance", Potenzdiagramm, Aurenhammer 1987), Gl. (10) und (13) (gewichteter Stern *1 = l*/l). **Einschraenkung:** de Goes ist 2D (Dreiecksflaechen), und die Hebung kommt dort nicht vor. 3D-Hodge-Sterne: HKV 2013, Glickenstein 2011 [P HODGE-L]. |
| VK5 | [H] Mindestens eine Arbeit behandelt eine dynamische Hebehoehe bzw. Eckgewichte als physikalisches Feld in diskreter Gravitation oder emergenter Geometrie | 25 % | **nicht eingetroffen** (nach Recherchestand, mit 24-Monats-Suche). Ein Nahtreffer haengt an einer [L]-Zuordnung (s. rechts) | Abrufe 11 und 13 (Fenster 2024-10 bis 2026-10, 3 Treffer, alle hep-th): keine Arbeit in Regge, DT, CDT oder Spinschaum mit dynamischen Eckgewichten. Nahtreffer: (i) Laguerre-Zellen in der Rekonstruktion des fruehen Universums ("Each Laguerre cell corresponds to the matter that lumped to form one of the galaxy clusters", Levy/Mohayaee/von Hausegger, 2012.09074) und in der Euler-Stroemung ("pressure force" zu den Schwerpunkten der Laguerre-Zellen, Gallouet/Merigot, 1605.00568) [S Treffer, Abruf 12]: Newton bzw. Stroemung, keine diskrete Gravitation. (ii) Aspinwall/Greene/Morrison 1994 [S Abstract, Abruf 14]: Kaehler-Moduliraum aus "adjacent domains ... (complexified) Kahler cones of topologically distinct manifolds", getrennt durch Waende; "Spacetime topology change in string theory ... is realized by ... deformation by a truly marginal operator". Witten 1993 [S Abstract]: Phasen, Topologieaenderung. Dass die Kammern regulaere Triangulierungen und die Kaehler-Parameter deren Hoehen sind, ist [L]; MacFadden/Sheridan 2025 [S Abstract] stuetzt nur "Kaehler-Moduli <-> Triangulierungen bzw. Faecher". Waere das an der Quelle belegt, hiesse das Urteil "teilweise" (Hoehen als Felder, aber fuer den inneren Raum, nicht fuer ein Raumnetz). (iii) Das Membran-Hoehenfeld (Seung/Nelson) ist [P] und eine Einbettungshoehe, keine Hebehoehe. |
| VK6 | [H] Mindestens eine begutachtete Arbeit verbindet Spin 1/2 bzw. Spinoren mit der 600-Zelle oder ihrer Hopf-Faserung in einem Gitter- oder Festkoerpermodell | 45 % | **teilweise eingetroffen**: Spinor-Struktur ja, Spin-1/2-Freiheitsgrade im Gitter nein. Bei strenger Lesart ("Spin-1/2-Teilchen im Gittermodell"): nicht eingetroffen | Kleman/Friedel 2008 (RMP 80, 61), Abschn. VII.E.1, Gl. (88), (89), S. 52 [S lokal]: Disvektionen der {3,3,5} sind Elemente von Q = SU(2); an Knoten gilt h1 h2 h3 = {+-1}; "hQ and -hQ represent the same rotation in SO(3), but they do not represent the same transvection in SU(2) ... a fundamental necessity to introduce the quaternion {-1}". Das ist die Doppelueberlagerung in einem Festkoerper-Defektmodell, aber kein Spin 1/2. Dechant 2013 (Acta Cryst. A) [S Abstract lokal]: Spinoren = Ecken der 600-Zelle, Kristallographie-Zeitschrift, aber kein Gittermodell. Nicht gewertet bzw. passt nicht [S Abstract, Abrufe 5, 19]: Amaral/Clawson/Irwin 2023 (2306.01964, gr-qc): Fermionen in quasikristallinem Spinschaum mit 600-Zelle; Begutachtung nicht festgestellt, E8/H4-Umfeld -> Randarbeit. Konstantinidis 2022: klassische Spins auf der 600-Zelle. Waegell/Aravind 2010: Kochen-Specker mit 600-Zellen-Richtungen, kein Gitter. Taubes/Wu 2026: Spinoren mit Polytop-Singularitaeten, Mathematik. 24 Monate (Abrufe 15, 18, 19): kein Gittermodell mit Spin 1/2. |

**Bedeutung nach der Karte, angewandt:**
- **VK1 und VK2 eingetroffen:** Die Lesart der Karte gilt. Die gekruemmte Kugel, auf der Finns Tetraeder lueckenlos
  passen, ist zugleich der Raum der Spin-Drehungen; beide Ideen Finns treffen sich mathematisch.
  - Zusatz [M4]: Auch die Hebehoehe fuehrt auf diese Kugel (Brown).
  - Wie vorab vermerkt, ist damit nicht gezeigt, dass das Netz das physikalisch nutzt.
- **VK3 eingetroffen:** Die Lesart gilt. Eine Drehdimension allein gibt Ladung, Spin 1/2 braucht die Kopplung an die
  Raumdrehungen und SU(2) statt SO(3).
  - Finns Rahmenfeld in GUERTEL-FINN-NETZ-1 ist schon so gekoppelt [P].
  - GEN-04 H2 (Ladung + Monopol) steht jetzt auf [S Abstract] statt auf [L].
- **VK5 verfehlt:** Die Lesart "dynamische Hebehoehe als Feld waere neu [H]" gilt nur eingeschraenkt.
  - Neu waere es nach Recherchestand fuer ein Raumnetz, nicht fuer den inneren Raum (Kaehler-Moduli, [L]).
  - Zwei Befunde schraenken das Feld ein. Erstens werden gueltige Gewichte im Kontinuum konstant (de Goes [S]); ein
    langreichweitiges Hoehenfeld muesste die Dual-Metrik-Bedingung verlassen. Zweitens wirkt die Hoehe nicht auf die
    Regge-Wirkung [M2], koppelt also nur ueber die Materie.
  - Vor einer Fuenfte-Kraft-Karte ist zu klaeren, ob V ueberhaupt eine Hoehe hat (Kartenvorschlag 6.1).
- **VK6 teilweise:** Literaturanschluss fuer einen Spin-Strang ueber die 600-Zelle besteht auf der Ebene der SU(2)-Struktur
  (Kleman/Friedel, Dechant), nicht auf der Ebene "Spin-1/2-Teilchen im Gitter".

## 4. Antworten auf die Fragen der Karte

### 4.1 Arm A: Hoehe

**Frage A1: Genaue Aussage der Hebeabbildung (Brown 1979; Edelsbrunner/Seidel 1986)**
- [M] Delaunay(P) in R^3 ist die Projektion der unteren Facetten von conv{(p, |p|^2)} in R^4. Eine Umkugel ist genau
  dann leer, wenn die Hyperebene durch die vier gehobenen Punkte keinen anderen gehobenen Punkt unter sich hat.
- **Gewichtet [M aus S]:** de Goes u. a. 2014, Abschn. 2.4 [S], nennen den Potenzabstand ("power distance"), also
  |y - p|^2 - w_p. Daraus folgt die Hoehe |p|^2 - w_p [M]. Fuer die Ebene steht die Gleichwertigkeit "gewichtete
  Delaunay = untere Huelle" bei Erickson/Lin 2020 [S Abstract].
- **Kugelvariante:** Brown 1979 benutzt "convex hulls and the inversion transform", auch fuer hoehere Dimensionen
  [S Treffer]. [M4]: Stereographisch R^3 -> S^3 gehen Kugeln in Schnitte der S^3 mit Hyperebenen ueber; leere Kugel
  heisst Stuetzhyperebene. Also ist Delaunay(P) = Randkomplex von conv(sigma^-1(P)) ohne die Polseite. Die Kombinatorik
  ist invariant unter den projektiven Abbildungen, die S^3 erhalten (Moebiusgruppe SO(4,1)).
- **Umklappzug [M3]:** Die Insphaeren-Determinante det[p_i, |p_i|^2 - w_i, 1] (5 x 5) ist das orientierte Volumen des
  gehobenen 4-Simplex.
  - Beim 2-3-Zug ist sie null: Die fuenf Punkte liegen auf einer Kugel.
  - Davor und danach hat sie entgegengesetztes Vorzeichen.
  - **Die "vierte Ausdehnung" ist im Hebebild also genau im Augenblick des Zugs null.**
- **Edelsbrunner/Seidel 1986:** nicht abgerufen [L].
- **Grenze:** Nicht jede 3D-Zerlegung ist regulaer (Joe; LAMBDA-TURING-L [P, dort S Treffer]). Eine nicht-regulaere
  Zerlegung hat keine Hebehoehe.
  - Finns V ist nicht Delaunay: 12 von 116 Flaechen je Zelle verletzen die Leere-Kugel-Bedingung (HODGE-L 1a [P]).
  - Ob V mit Gewichten regulaer ist, ist offen (Gegensweep G2, Kartenvorschlag 6.1).

**Frage A2: Regulaere Zerlegungen mit dynamischen Gewichten; Potenzdiagramm-Duale; DEC (de Goes, Memari, Mullen,
Desbrun)**
- **de Goes u. a. 2014 [S]:**
  - "a gradient vector is unchanged if one adds a constant to all weights; thus, weights add |V|-1 degrees of freedom"
    (Abschn. 2.3).
  - "any weighted triangulation can be converted to a weighted Delaunay triangulation through a series of edge flips to
    enforce positive dual lengths [Aurenhammer 1987]" (Abschn. 2.4).
  - Def. 8 "dual metric": |w_i - w_j| <= l_ij^2. Abschn. 4.2: "the validity of dual metrics (Eq. (8)) implies that the
    weights become constant in the limit. As a consequence, Delta^w tends to the same operator in the limit".
  - Abschn. 4.3: Die Gewichte naehern eine "divergence-free metric"; die erweiterte Metrik ist die stueckweise
    euklidische "additively perturbed by a divergence-free matrix associated to the weights". Mullen u. a. 2011 (HOT)
    waehlen die Gewichte als Minimierer eines Hodge-Stern-Fehlers.
- **[M1] Affine Eichfreiheit:** h -> h + a.x + b laesst die untere Huelle kombinatorisch gleich. Das Potenzdiagramm
  verschiebt sich um a/2; duale Laengen und *1 bleiben gleich.
  - Im flachen R^3 hat die Hoehe 4 Eichrichtungen, auf dem Torus nur die Konstante (de Goes: |V| - 1).
  - [ES] In 2D ist eine symmetrische divergenzfreie Matrix die Kofaktor-Hesse-Matrix einer Airy-Spannungsfunktion. Das
    passt zu Maxwell/Cremona (A3): Wirksam ist die "Kruemmung" der Hoehe, nicht ihr affiner Teil.
- **Kinetische Datenstrukturen mit zeitabhaengigen Gewichten:** nicht gezielt geprueft (Negativliste).

**Frage A3: Gewichte als physikalisches Feld?**
- **Diskrete Gravitation:** keine Arbeit gefunden (Abrufe 11, 13). McDonald/Miller 2008 [S Treffer; P HODGE-L] nutzen
  Voronoi- und Delaunay-Zellen mit festen Umkreisdualen.
- **Mechanik: Hoehe = Spannungsfunktion** [S Treffer Abruf 9; S Abstract Abruf 10]:
  - Maxwell 1864 und Cremona verbinden eigengespannte ebene Stabwerke mit stueckweise linearen Hebungen.
  - Erickson/Lin 2020: In der Ebene sind positives Gleichgewicht, Reziprozitaet und Kohaerenz gleichwertig.
  - "On any flat torus, reciprocal and coherent embeddings are equivalent, and every reciprocal embedding is in positive
    equilibrium, but not every positive equilibrium embedding is reciprocal"; es bleibt nur affine Aequivalenz.
  - Karpenkov/Mohammadi/Mueller/Schulze 2023: Fuer d-Komplexe in d Dimensionen gibt es Verallgemeinerungen (Rybnikov),
    fuer Stabwerke in d >= 3 fehlten sie bisher ("differential liftings").
- **Optimaler Transport:** Laguerre-Gewichte als Unbekannte, Kosmologie und Stroemung [S Treffer Abruf 12].
- **Stringtheorie:** Kaehler-Kammern und Topologieaenderung [S Abstract Abruf 14]; Hoehen-Zuordnung [L].
- **Projektbezug [P]:** Eigenspannungen des Pyrochlor-Stabnetzes (EIS-1: 12 L^2 gerade <110>-Linien); "Kruemmung wird
  Spannung" (KRUEMMUNG-SPANNUNG-SPIN-L). Die Bruecke Hebung <-> Eigenspannung fehlt im Projekt (grep "Cremona": 0).

**Frage A4: Welche Messgroessen begrenzen eine universell gekoppelte Hoehe?**
- **Kopplungsweg [M2, ES]:** Die Regge-Wirkung Summe l_e delta_e haengt bei fester Zerlegung nur an den Kantenlaengen.
  - Die Hoehe wirkt ueber den Hodge-Stern aller Materiefelder (de Goes Gl. 13 [S]) und ueber Umklappzuege.
  - Wenn alle Materiefelder denselben Stern sehen, ist das eine universelle Kopplung an die kinetischen Terme.
- **Zwei Regime, Moderator Zusammensetzung (Regel 1):**
  - (i) Zusammensetzungsabhaengig, z. B. wenn Bindungsenergien die Gewichte verschieden sehen: MICROSCOPE eta(Ti, Pt) =
    [-1,5 +- 2,3 (stat) +- 1,5 (syst)] x 10^-15 bei 1 sigma (Touboul u. a. 2022 [S Abstract]). Eoet-Wash-WEP
    2 x 10^-13 (Will 2014, S. 8 [S lokal]).
  - (ii) Universell: Eta-Tests sehen nichts. Dann entscheidet die Reichweite.
    - Lang: Cassini gamma - 1 = (2,1 +- 2,3) x 10^-5; Skalar-Tensor-Theorien brauchen omega > 40 000 (Will 2014, S. 43
      [S lokal]).
    - Kurz: "No deviations from the inverse square law have been found to date at distances between tens of nanometers
      and 10 mm" (Will 2014, S. 24 [S lokal]). Eoet-Wash 2020: alpha = 1 fuer lambda > 38,6 um ausgeschlossen
      [P dunkle-dimension-check].
    - Gitterskalig (de Goes: Gewichte im Kontinuum konstant): nur Dispersion. LHAASO: E_QG,1 > 10 E_Pl (linear),
      E_QG,2 > 6 x 10^-8 E_Pl (quadratisch) (Cao u. a. 2024 [S Abstract]).
- **Unterscheidungspunkt (Regel 2):** Masse bzw. Reichweite des Hoehenfelds.
  - Am Netz: Eine dynamische, langreichweitige Hoehe muesste eine dritte masselose langwellige Mode neben den zwei
    TT-Moden bringen. Das gefuellte Netz hat bisher genau zwei (EINE-WELT-LOCH-1, zitiert in SKALAR-SEKTOR-L [P]).
  - Ohne dritte Mode ist die Hoehe eine Gitterfreiheit [ES].

### 4.2 Arm B: Drehdimension

**Frage B1: Kaluza-Klein mit innerem SU(2) bzw. S^3; "spin from isospin"**
- **Ladung, nicht Spin:** Witten 1981 [S Abstract]: Die Eichgruppe kommt aus den kompakten Dimensionen, die richtigen
  Fermion-Quantenzahlen sind schwer zu erreichen.
  - [M] Ohne Hintergrund ist die Symmetrie G_Raum x G_innen. J = L + S vertauscht mit dem inneren T, und eine
    2-pi-Raumdrehung wirkt nicht auf innere Koordinaten. Bosonische Felder geben dann ganzzahliges J.
- **Spin aus Isospin:** Ein Igel bzw. Monopol bricht auf die Diagonale; erhalten ist J = L + S + T (Jackiw/Rebbi,
  Hasenfratz/'t Hooft [S Abstract]).
- **KK-Monopol:**
  - Sorkin 1983 [S Abstract]: Taub-NUT plus -dt^2 ist eine statische 5D-Vakuumloesung, "regular five-geometry", aus 4D
    singulaer.
  - Gross/Perry 1983 [S Abstract]: Die Monopole erfuellen die Dirac-Quantisierung.
  - [ES/L] Die fuenfte Dimension (ein Kreis, also eine Drehdimension) liegt dort als Hopf-Faser ueber S^2. Zusammen
    mit Goldhaber kann ein KK-geladenes Teilchen am KK-Monopol halbzahligen Drehimpuls tragen. Das stand so in keinem
    gelesenen Abstract.
  - **Gross/Perry, unerwartet:** "they exert no newtonian force on slowly moving test particles, thus they have zero
    gravitational mass", erklaert durch "the violation of Birkhoff's theorem in Kaluza-Klein theories"; nach den Autoren
    "consistent with the principle of equivalence" [S Abstract].

**Frage B2: Starrer Kreisel bzw. Rahmenfeld, SO(3) gegen SU(2)**
- [P] Der starre Rotor hat einen ganz- und einen halbzahligen Sektor (Giulini 2009, S. 26, in KRUEMMUNG-SPANNUNG-SPIN-L).
  Jede Zelle mit eigenem Rahmen ist ein solcher Rotor. Der Guertel-Trick gelingt auf Finns Netz mit SU(2), nicht mit
  SO(2) (GUERTEL-FINN-NETZ-1).
- [M6] Peter-Weyl: Funktionen auf S^3 zerfallen in (j, j) unter SU(2)_L x SU(2)_R.
  - Unter der Diagonalen (Drehung um einen Punkt der S^3) gibt es nur ganze Spins.
  - Unter der einseitigen Wirkung (Rahmen) gibt es halbzahlige.
- Bernard-Bernardet/Apffel 2024 (2411.15059) [S Abstract]: ein Handgeraet, "to discuss the origin of spin-1/2 from
  rotations group representation, without relying on the quantum mechanics framework". Bloch-Kugel, Hopf-Faserung und
  Berry-Phase sind am Geraet sichtbar.

**Frage B3: Hopf-Faserung und Spin; Monopol-Kugelfunktionen**
- Urbantke ("The Hopf fibration - seven times in physics") ist nicht abgerufen (Budget) [L].
- **[M6] Faser-Halbumlauf = volle Rahmendrehung:**
  - Mit x -> x e^(i theta) laengs der Faser dreht sich der Rahmen R_x um den Basispunkt um 2 theta.
  - theta = pi ist also eine 2-pi-Rahmendrehung und zugleich x -> -x.
  - Auf der 600-Zelle ist -1 = c^5 mit c = exp(q pi/5) der Erzeuger der Zehneck-Faser.
- **Folgen [M]:**
  - Ungerade Funktionen auf den 120 Ecken haben ungerade Faserladung s.
  - Sie bilden einen 60-dimensionalen Raum mit nur treuen Darstellungen von 2I (2, 2', 4', 6, Vielfachheit = Dimension:
    4 + 4 + 16 + 36 = 60). Die geraden tragen 1, 3, 3', 4, 5 (1 + 9 + 9 + 16 + 25 = 60).
  - Das ist die diskrete Form der Monopol-Kugelfunktionen mit halbzahliger Ladung q, j >= |q| (Wu/Yang [L]).
- **Bekannt [P]:** WELTKRISTALL-L D2: Der Sektor s = 0 ist das Ikosaeder; die Grade 1, 3, 5 tragen dort nichts.

**Frage B4: Sadoc/Mosseri und Nachfolger: Spinor-Bezug?**
- **Buchgliederung [S]:** Anh. A2 "Quaternions and related groups", A3 "Hopf fibration". Ein Spinor-Kapitel ist nicht
  sichtbar.
- **Qubits und Hopf-Faserungen:** Mosseri/Dandoloff 2001 [P WELTKRISTALL-L F3, dort S Abstract], ohne Gitter.
- **Frustrationstheorie:**
  - Nelson/Widom bzw. Sethna, nach Tarjus u. a. 2005, S. 14 und S. 19-20 [S lokal]: Der Ordnungsparameter Q_l mit
    l = 12 ist "minimally coupled" an einen eingefrorenen nichtabelschen Eichhintergrund. Die Kruemmung der kovarianten
    Ableitung ist "precisely equal to that of the reference 4-D sphere"; Konfigurationen entstehen durch "Rollen" der
    {3,3,5}.
  - **Die "Drehung in die vierte Richtung" ist dort ein SO(4)-Eichfeld der Frustration mit ganzzahligem
    Ordnungsparameter, kein Spin.**
- **Kleman/Friedel 2008:**
  - VI.B.1, S. 40 [S lokal]: "Letting M (S3, say) roll without glide upon E3 ... The closure failure can be described as
    a disclination."
  - VI.B.2: Die {3,3,5} wird ausdruecklich nach Regge (1961) trianguliert.
  - VII.E.1: SU(2) mit dem Element -1 (VK6).

**Frage B5: Herkunft der Arbeiten (Quellenkritik)**
- **Randarbeit, nicht gewertet:** Gray/Dennis/Kauffman 2026 (2604.00255, math.GR, ohne journal_ref) [S Abstract]. Der
  Abstract beruft sich auf "perennial philosophy" und schreibt "The 600-cell is made from 120 copies of a dodecahedron";
  das ist die 120-Zelle.
- **Begutachtung nicht festgestellt, nur Nahtreffer:** Amaral/Clawson/Irwin 2023 (2306.01964, gr-qc), E8/H4-Umfeld
  (Quantum Gravity Research [L]). gr-qc ist eine Kernkategorie; nach dem Auftrag waere die Arbeit wertbar, nicht aber als
  "begutachtet" im Sinn von VK6.
- **Gewertet:** Dechant 2013 (Acta Cryst. A), Dechant 2021 (Adv. Appl. Clifford Alg.), Kleman/Friedel 2008 (RMP),
  Waegell/Aravind 2010 (J. Phys. A), Serafin u. a. 2021 (Nat. Commun.), Taubes/Wu 2026 (math.DG, Mathematik).
  Konstantinidis 2022 (cond-mat.str-el): journal_ref fehlt, klassische Spins.

### 4.3 Gegensweep der Karte

**Argumente gegen eine "temporaere" Extradimension**
1. **Lorentz-Tests:** LHAASO GRB 221009A: E_QG,1 > 10 E_Pl, E_QG,2 > 6 x 10^-8 E_Pl (Cao u. a. 2024, PRL 133, 071501
   [S Abstract]).
   - Im Fenster auch Yang/Bi 2024 (JCAP 04, 060): E_QG,1 > 14,7 (6,5) x 10^19 GeV subluminal (superluminal)
     [S Abstract].
   - Satunin/Troitsky 2025: Lorentz-Verletzung erklaert Carpet-3 nur mit Parametern, "excluded by other constraints"
     [S Abstract].
   - Eine Planck-Gitter-Dispersion linear in E ist damit ausgeschlossen [ES].
2. **KK-Moden und 1/r^2:** universelle Extradimensionen hbar c/R > ~1 TeV (LHC) und Eoet-Wash 2020 [P
   dunkle-dimension-check]. Will 2014, S. 24 [S lokal]: grosse Extradimensionen gaeben 1/R^(2+n) kurzreichweitig; nicht
   gesehen.
3. **KK-Monopole mit verschwindender schwerer Masse** (Gross/Perry [S Abstract]): Eine Drehdimension mit Monopol bringt
   Objekte mit unueblicher Gravitation.
4. **Kausalitaet:** Abkuerzungen durch eine Zusatzrichtung (Signale schneller als in der 3D-Schicht) [L, Chung/Freese
   2000; Csaki/Erlich/Grojean 2001]. Nicht geprueft.
5. **Die Dimension waehlt sich nicht aus den Bausteinen** (AJL 2004, S. 2 [P GEOMETRIE-STAND]); EDT ohne Kausalregel
   entartet [P].
- **Einschraenkung [ES]:** Diese Schranken treffen eine physikalische Zusatzrichtung, in der sich etwas bewegt.
  - Die Hebehoehe ist keine solche Richtung: Beim Zug hat sie keine Ausdehnung [M3], und sie ist nur eine Eichklasse
    modulo affiner Funktionen [M1].
  - Fuer sie gelten die Feldschranken aus A4.

**24-Monats-Suche (Oktober 2024 bis Oktober 2026)**
- **Arm A** (Abruf 13, arXiv-API, 6 Phrasen, 5 Kategorien): 3 Treffer, alle hep-th (Scattering Facet; regulaere
  Triangulierungen fuer Calabi-Yau-Raeume). Keine dynamischen Gewichte als Feld.
- **Arm B:**
  - Abruf 15: 1 Treffer, das Spinor-Handgeraet 2024; Recall fraglich (Selbstanzeige).
  - Abrufe 3, 5, 18, 19: Taubes/Wu 2026 (Mathematik), Mereon 2026 (Randarbeit). Kein Gittermodell mit Spin 1/2.
- **Lorentz-Tests** (Abruf 20): LHAASO 2024, Yang/Bi 2024, Satunin/Troitsky 2025.
- **Urteil:** Kein "widerlegt". VK5 und VK6 stehen auf "nach Recherchestand".

## 5. Einordnung fuer Finns Netz [ES/H]

### 5.1 Wo es eine vierte Richtung genau gibt

| Lesart | Was die vierte Richtung ist | "Temporaer"? | Physikalischer Gehalt | Stand |
|---|---|---|---|---|
| Zeit im 4-Simplex | Ein 2-3-Zug in der 3D-Schicht = Ankleben eines 4-Simplex; Pachner-Zuege als Zeitschritte (Hoehn 2015: 1-4 erzeugt Lapse/Shift, 2-3 ein Graviton, 3-2 die einzige nichttriviale Bewegungsgleichung) | Ja, als duenner 4D-Zeitschritt mit endlichem 4-Volumen | Hoch: Das ist ART auf dem Netz | [P] HODGE-L, PACHNER-TAKT-1 |
| Hebehoehe (regulaere Zerlegung) | Hoehe h_v = \|x_v\|^2 - w_v; Delaunay = untere Huelle in R^4 | Ja: Beim Zug liegt der gehobene 4-Simplex flach (Volumen null) [M3] | Spannungsfunktion (Maxwell/Cremona); keine Wirkung auf Regge; wirkt ueber Materie-Hodge-Stern und Zerlegungswahl [M2]; im Kontinuum konstant (de Goes) | neu fuers Projekt (Literatur) |
| Gekruemmte S^3 (600-Zelle) | Einbettung des gekruemmten Idealraums; im flachen Raum Disklinationen bzw. SO(4)-Eichhintergrund | Beim "Abflachen" bleibt sie als Defektnetz bzw. Frustration | Glas- und Kristallstruktur (Nelson, Sadoc/Mosseri, Kleman/Friedel) | [P] WELTKRISTALL-L; hier S Gliederung, S lokal |
| Drehdimension als innerer Raum | Kreis (Ladung) bzw. S^3 (Isospin-artige Ladungen) | Kompakt, nicht temporaer | Ladung; Spin erst mit Monopol bzw. Igel (JR, HtH) | GEN-04 H2 [P]; jetzt S Abstract |
| Drehdimension als Rahmenraum | SU(2)-Orientierung je Zelle bzw. Knoten | Nein | Spin-Sektor moeglich (Rotor, Guertel-Trick) | [P] GUERTEL-FINN-NETZ-1 |

### 5.2 Eine Kugel, drei Rollen [M]
- **Dieselbe 3-Sphaere:** Browns Kugel-Hebung (M4), die 600-Zelle (M5: Randkomplex der konvexen Huelle ihrer 120 Ecken
  = sphaerische Delaunay-Zerlegung) und SU(2).
  - **Hebe-Richtung und Kruemmungs-Richtung sind bis auf eine projektive Abbildung dieselbe Konstruktion** (Gegensweep
    G4).
  - Delaunay-Zuege sind deshalb moebiusinvariant (SO(4,1)), bis auf die Buchfuehrung des Pols. Das ist die konforme
    Gruppe des R^3 und die Isometriegruppe des 4D-de-Sitter-Raums [M; Deutung ES].
- **[M] Brown-Hebung als Feld:** Liest man den gehobenen Punkt sigma^-1(x) als Einheitsquaternion, ist die Abbildung
  R^3 u {inf} -> S^3 ein Homoeomorphismus. Als SU(2)-Feld ist das eine Textur vom Grad 1 mit Profil
  f(r) = 2 arctan(R/r).
  - [L/H] Das ist die Form eines Skyrmions mit B = 1.
  - Ob ein solcher Zustand fermionisch quantisiert werden darf, haengt an der Dynamik (Finkelstein/Rubinstein; GEN-04
    H4 [P]).
  - Ein Spin-1/2-Beleg ist das nicht.

### 5.3 Wann ist eine Drehdimension Spin und nicht Ladung?
- **Kriterium [M, S]:** Spin, wenn Raumdrehungen auf die Drehdimension wirken, und zwar einseitig. Das geht auf drei
  Wegen:
  1. Die Drehdimension ist selbst der Orientierungsraum (Rahmen, Kreisel; GUERTEL [P]).
  2. Ein Hintergrund verriegelt innere und Raumdrehung (Monopol bzw. Igel; JR, HtH [S Abstract]).
  3. Die Drehdimension ist eine Hopf-Faser ueber der Raumkugel; die Faserladung wird dann Drehimpuls (Goldhaber;
     KK-Monopol [S Abstract + ES]).
  - Regel 6: Alle drei koppeln an dieselbe Groesse, die Wirkung der 2-pi-Raumdrehung auf den inneren Freiheitsgrad.
    Das ist die Kopplungsgroesse, nicht ein bestimmtes Bauteil [ES].
- **Unterscheidungspunkt (Regel 2):** Vorzeichen eines Zustands unter einer 2-pi-Raumdrehung.
  - Innen ungekoppelt: +1 fuer bosonische Felder [M].
  - Gekoppelt: (-1)^(2T) (JR/HtH).
  - Auf der 600-Zelle: Paritaet unter x -> -x, also unter dem Faser-Halbumlauf [M6].
  - Am Modell ist das messbar, in der Natur nicht direkt (Ladung-Monopol-Komposite sind nicht beobachtet [L]).
- **Zweiter Moderator:** S^3 als Ort (Konjugation, nur ganze Spins) gegen S^3 als Orientierungsraum (einseitig,
  halbzahlig) [M6].
  - Finns Netz mit Rahmenfeld ist schon im zweiten Fall [P].
  - Die 600-Zelle als Ort ist im ersten Fall.
  - **Fuer Spin braucht Finns Netz die S^3 also nicht als Raum, sondern als Werteraum der Rahmen (SU(2))** (Gegensweep
    G3). Die 600-Zelle waere dann hoechstens eine diskrete Auswahl dieser Werte (2I) [ES].

### 5.4 Was im Projekt bekannt ist, was neu waere
- **Bekannt [P]:**
  - Pachner = Zeitschritt; Glickenstein (Eckvariation = Laplace mit *1); HKV-Delaunay-Stern; V nicht Delaunay.
  - Hopf-Faserung der 600-Zelle, Fock-Kugel, s = 0-Sektor; starrer Rotor, Guertel-Trick, FR; Ladung + Monopol ([L]
    in GEN-04).
  - Seung/Nelson-Beulen; Eigenspannungen (EIS-1); KK-Schranken, Eoet-Wash 2020, Dunkle Dimension; Poincare-Sphaere
    als [H]-Bruecke.
- **Neu fuers Projekt (Literatur, nicht neu fuer die Welt):**
  - Maxwell/Cremona und Hebung = Spannung, mit Torus-Einschraenkung; Gewichte im Kontinuum konstant (de Goes).
  - Sadoc/Mosseri-Gliederung; Nelson/Widom-Eichhintergrund als Lesart der "Drehung in die vierte Richtung";
    Kleman/Friedel-SU(2) mit -1.
  - JR/HtH/Goldhaber, Witten 1981, Sorkin, Gross/Perry an den Abstracts; AGM/Witten (Kaehler-Kammern).
  - MICROSCOPE 2022, LHAASO 2024; Dechant (Spinoren = 600-Zelle).
- **Neu fuer die Welt, nach Recherchestand [H]:**
  - Eine dynamische Hebehoehe als Feld eines Raumnetzes, mit Umklappzuegen an den Kammerwaenden. Das waere das
    Raumnetz-Gegenstueck der Kaehler-Kammern [L-Zuordnung].
  - Die Lesart "Brown-Hebung = Grad-1-Textur auf Finns Netz".
  - Ein Hopf-Faser-Hamiltonian auf der 600-Zelle, dessen Frustration Spinor-Multipletts waehlt (Kartenvorschlag 6.2).
  - Jeweils mit grossem vorab ableitbarem Anteil.

## 6. Kartenvorschlaege (zwei)

### 6.1 REGULAER-V-1: Hat Finns Netz V eine Hebehoehe, und wie viel Spielraum hat sie?
- **Frage:** Gibt es Eckgewichte w, mit denen V die gewichtete Delaunay-Zerlegung seiner Ecken ist (regulaer)?
  - Falls ja: Dimension und Breite der Gewichtskammer modulo Konstante, und welche Umklappzuege an den Waenden liegen.
  - Wie stark aendert sich innerhalb der Kammer der Materie-Hodge-Stern *1, gemessen an der langwelligen
    Laplace-Anisotropie (l = 4)?
- **Methode:** Lineares Programm auf einer periodischen Superzelle.
  - Je innerer Dreiecksflaeche eine gewichtete Insphaeren-Ungleichung (M3, linear in w) mit Marge t; t wird maximiert.
  - Lokal regulaer an jeder Flaeche heisst global regulaer: Die Hebung ist eine stueckweise lineare Funktion auf ganz
    R^3, lokale Konvexitaet genuegt [M]. Danach Stichproben in der Kammer, gewichteter Stern wie in de Goes Gl. (13),
    3D-Gegenstueck nach Glickenstein.
- **Ableitbarkeitsprobe:**
  - **Vorab ableitbar:**
    - w = konstant ist unzulaessig (12 von 116 Flaechen je Zelle, HODGE-L 1a [P]).
    - Die Regge-Wirkung haengt nicht an w [M2]; die Konstante ist Eichrichtung (de Goes [S]); lineare Anteile sind auf
      dem Torus nicht periodisch [M1].
  - **Nicht ableitbar:** ob ein nichtkonstantes w existiert; Kammerbreite; Wandzuege; Wirkung auf die
    *1-Anisotropie.
  - **Schreibtischrechnung vor Freigabe:** die Bahnen von Fd-3m auf den Ecken von V zaehlen. Mit bahnweise konstanten
    Gewichten bleiben nur wenige Unbekannte; ist das LP dann von Hand loesbar, wird RV2 vorab entschieden.
- **Vorhersagen (Entwurf):**

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| RV0 | Kontrolle: Bei w = 0 meldet das LP genau die 12 verletzten Flaechen je Zelle aus HODGE-L 1a. Eine Delaunay-Zerlegung zufaelliger Punkte ist bei w = 0 zulaessig. Ein bekannt nicht-regulaeres Beispiel (2D "mother of all examples" [L], als Prisma in 3D) ist unzulaessig | Kontrolle | 85 % |
| RV1 | V ist regulaer (t_max > 0) | [H] | 55 % |
| RV2 | Falls regulaer: bahnweise konstante (Fd-3m-symmetrische) Gewichte genuegen | [H] | 60 % |
| RV3 | Innerhalb der Kammer aendert sich die langwellige l = 4-Anisotropie des gewichteten Laplace um weniger als 10 % ihres Werts in der Kammermitte | [H] | 50 % |

- **Bedeutung (vorab):**
  - **RV1 trifft ein:** Finns "vierte Richtung beim Zusammensetzen" gibt es fuer V als Hebehoehe, mit messbarem
    Spielraum. Dynamische Gewichte koppeln dann nur an Materie [M2], und die Pruefung als universeller Skalar (A4) wird
    sinnvoll.
  - **RV1 scheitert:** V hat keine Hebung. Die vierte Richtung gibt es fuer V dann nur als Zeit (Regge) oder als
    S^3-Kruemmung.
- **Kontrolle:** RV0, und das Ergebnis darf nicht von der Superzellengroesse (L = 1, 2) abhaengen.
- **Aufwand:** klein (LP), Kleintest-Spur der .69. Synthetisch, keine Messdatenbestaetigung.

### 6.2 FASER-SPIN-600-1: Waehlt eine frustrierte Drehdimension Spinor-Zustaende?
- **Frage:** Auf der 600-Zelle (120 Ecken; je Ecke 2 Kanten laengs der eigenen Hopf-Faser, 10 zu den Nachbarfasern
  [P WELTKRISTALL-L D3]) gelte H = -t_b Summe_Basis - t_f Summe_Faser mit t_f < 0, also frustriert laengs der Faser.
  - Bei welchem Verhaeltnis r = t_b/|t_f| ist der Grundzustand ungerade unter x -> -x? Ungerade heisst
    Faser-Halbumlauf = 2-pi-Rahmendrehung (M6), also spinoriell unter 2I.
  - Welche treue 2I-Darstellung traegt der Grundzustand?
- **Ableitbarkeitsprobe:**
  - **Vorab ableitbar [M]:**
    - t_f > 0, t_b > 0: Grundzustand konstant, also gerade (Perron-Frobenius). Bei t_b = 0 zerfaellt der Graph in
      12 Zehnecke; der Grundzustand ist dann je Faser konstant (s = 0), ebenfalls gerade.
    - t_b = 0, t_f < 0: Jedes Zehneck ist einzeln; Grundzustand s = 5 (ungerade), 12-fach entartet.
    - Ungerade heisst treu, mit Vielfachheiten 60/60 (M6). Der s = 0-Sektor ist 2 x Ikosaeder-Laplace [P].
    - Ungefaehre Grenze: E_5 < E_0 genau dann, wenn r < 4/(10 - lambda_5), wobei lambda_5 der groesste
      Basis-Eigenwert im Sektor s = 5 ist. Ein Wechsel in den Sektor s = 4 kann frueher kommen.
  - **Nicht ableitbar ohne Rechnung:** die Sektor-Eigenwerte lambda_s (12 x 12-Bloecke mit Phasen), also r* und das
    Grund-Multiplett.
  - **Warnung:** Mit der Charaktertafel von 2I sind die 12 x 12-Bloecke im Prinzip von Hand loesbar. Vor der Freigabe
    eine Schreibtischrechnung machen. Ist r* dann bekannt, ist die Karte vorab ableitbar und entfaellt (Projektregel
    "Vertraege muessen scheitern und bestehen koennen").
- **Vorhersagen (Entwurf):**

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| FS0 | Kontrolle: Bei t_b = t_f = 1 gibt der Laplace 12 - A im Sektor s = 0 genau 2 x Ikosaeder-Laplace (0; 5,528; 12; 14,472) auf 1e-12; die Sektordimensionen summieren sich zu 120; ungerade Sektoren tragen nur treue Darstellungen; die Grenzfaelle t_b = 0 und t_f > 0 kommen wie abgeleitet heraus | Kontrolle | 90 % |
| FS1 | 0,1 < r* < 1 | [H] | 50 % |
| FS2 | Fuer kleines r ist das Grund-Multiplett 6-dimensional, wie j = 5/2 im Kontinuum (Faserladung 5 <-> Monopolladung 5/2) | [H] | 40 % |

- **Bedeutung (vorab):**
  - **FS1 und FS2 treffen ein:** Eine Drehdimension mit Frustration waehlt von selbst Spinor-Multipletts. Spin 1/2 im
    engen Sinn (Dublett) kommt aber nicht heraus, sondern ein hoeherer halbzahliger Drehimpuls.
  - **FS1 scheitert:** Die Frustration muss feiner abgestimmt sein.
- **Kontrolle:** Kontinuumsvergleich mit Monopol-Kugelfunktionen (j >= |q| [L, vorher an der Quelle lesen]);
  2I-Charaktere aus einer Tabelle [L, vorher an der Quelle lesen].
- **Aufwand:** 120 x 120, Kleintest. Synthetisch; zeigt einen Mechanismus, nicht die Natur.

## 7. Erwartungsverstoesse, Negativliste, Selbstanzeigen

### 7.1 Erwartungsverstoesse (das eigentliche Ergebnis; wichtigste zuerst)

| Nr | Erwartet | Gefunden | Quelle |
|---|---|---|---|
| E1 | Die Hebeabbildung ist ein Rechentrick der Geometrie | Sie ist Mechanik: Hebung = positive Eigenspannung = orthogonales Dual = gewichtete Delaunay (eben). Auf flachen Tori nur eingeschraenkt; fuer Stabwerke in d >= 3 bis 2023 offen | Abrufe 9, 10 [S Treffer, S Abstract] |
| E2 | de Goes 2014 enthaelt die Hebung und traegt VK4 ganz | 2D, keine Hebung im Text. Dafuer: Gewichte werden im Kontinuum konstant; sie wirken als divergenzfreie Stoerung der Metrik | Abruf 8 [S] Abschn. 4.2, 4.3 |
| E3 | Hebehoehen als Felder gibt es in der Physik nicht | In der Stringtheorie haben Kaehler-Moduliraeume Kammern topologisch verschiedener Raeume mit Topologieaenderung an den Waenden; dass das Hoehen regulaerer Triangulierungen sind, ist [L] | Abrufe 13, 14 [S Abstract] |
| E4 | Die "Drehung in die vierte Richtung" hat in der Frustrationstheorie mit Spin zu tun | Sie ist ein eingefrorener SO(4)-Eichhintergrund; Ordnungsparameter ganzzahlig (l = 12) | Tarjus u. a. 2005, S. 14, 19-20 [S lokal] |
| E5 | In Festkoerpermodellen der 600-Zelle spielt SU(2) gegen SO(3) keine Rolle | Kleman/Friedel brauchen SU(2) und das Element -1 fuer die Knotenregel der Disvektionen | KF 2008 VII.E.1, Gl. (89) [S lokal] |
| E6 | KK-Monopole sind nur Monopole | Gross/Perry: verschwindende schwere Masse (Birkhoff verletzt) | Abruf 7 [S Abstract] |
| E7 | 24-Monats-Suche zu Arm B gibt einige Treffer | 1 Treffer (Recall fraglich); im weiteren Fenster eine Randarbeit mit Sachfehler (600- und 120-Zelle verwechselt) | Abrufe 5, 15 |
| E8 (klein) | Die 600-Zellen-Spinmodelle sind quantenmechanisch | Konstantinidis 2022: klassische Spins | Abruf 19 [S Abstract] |

**Korrigierte Erwartungen:**
- Die Hebehoehe ist eine Spannungs- bzw. Gitterfreiheit.
- Eine Drehdimension ist Ladung oder Frustrations-Eichfeld, solange sie nicht an Raumdrehungen gekoppelt ist.

### 7.2 Negativliste (nicht behaupten)
- **Nicht:** "Die Hebehoehe ist eine neue Raumdimension." Sie ist eine Eichklasse modulo affiner Funktionen [M1], beim
  Zug ohne Ausdehnung [M3], in Regge ohne Wirkung [M2].
- **Nicht:** "Die 600-Zelle liefert Spin 1/2." Sie liefert die SU(2)-Struktur; Spin braucht die einseitige Kopplung
  (5.3).
- **Nicht:** "Eine Drehdimension gibt Spin." Ohne Verriegelung gibt sie Ladung (VK3).
- **Nicht:** "VK5 bzw. VK6 widerlegt." Es gilt nur "nach Recherchestand nicht belegt" bzw. "teilweise".
- **Nicht:** "Pachner-Zuege als Zeit sind neu." Das ist [P] (Dittrich/Hoehn).
- **Nicht:** "Membran-Beulen als Gegenstueck ist neu." Das ist [P] (Seung/Nelson in KRUEMMUNG-SPANNUNG-SPIN-L).
- **Nicht:** Mereon 2026 oder den Spinschaum von 2023 als Beleg anfuehren.
- **Nicht:** "LHAASO schliesst jede temporaere Extradimension aus." Ausgeschlossen ist eine lineare Dispersion unterhalb
  von 10 E_Pl.
- **Nicht:** "Kaehler-Moduli sind Hoehen regulaerer Triangulierungen" als [S] fuehren. Das ist [L].
- **Nicht:** "Universelle Kopplung wird von MICROSCOPE begrenzt." Eta-Tests messen Zusammensetzungsabhaengigkeit.

### 7.3 Selbstanzeigen
1. **Startzeit:** Die Startzeit im Kopf stammt aus der Ausgabe des ersten date-Aufrufs und wurde im Arbeitsfeld von Hand
   uebernommen (gemessen, aber getippt). Alle anderen Zeitzeilen per $T; der Kopf dieses Dossiers zieht sie per grep aus
   dem Arbeitsfeld.
2. **Zaehlung:** 20 Abrufe gezaehlt, 21 Netzaufrufe.
   - Abruf 2 besteht aus zwei WebFetch-Aufrufen: Der erste gab nur die 301-Umleitung zurueck, ohne Inhalt.
   - Abruf 4 war leer (http ohne -L) und ist mitgezaehlt.
3. **[S Treffer]** heisst Suchmaschinen-Zusammenfassung, also sekundaer. Betroffen: Sadoc 2001, Brown 1979, die
   Ewha-Arbeit 2018, Levy u. a., Gallouet/Merigot, Maxwell/Cremona-Saetze aus Abruf 9.
   - Autorennamen der Ewha-Arbeit [L?].
   - Den Titel von Sadoc 2001 habe ich nicht gesehen.
4. **Ohne Abrufzaehlung lokal gelesen:** Kleman/Friedel, Tarjus u. a., Will 2014, KEGEL-4D-L A1 (Abfrage aus
   KEGEL-4D-L, nicht von mir; Zeit im Dateinamen).
5. **Werkzeuge:** pdftotext lokal (IO) fuer de Goes; jq nur lesend.
6. **Recall:** Die Arm-B-Abfrage (Abruf 15) gab nur 1 Treffer; nicht wiederholt (Budget). Die Phrase "Laguerre cells"
   trifft "Laguerre cell" in Abruf 13 vermutlich nicht.
7. **Nur Abstracts gelesen:** JR, HtH, Goldhaber, Witten, Sorkin, Gross/Perry, AGM, MICROSCOPE, LHAASO. Urbantke und
   Edelsbrunner/Seidel nicht gelesen.
8. **[M]-Punkte M1 bis M7** sind Kopfrechnung ohne zweiten Leser; die 2I-Darstellungsdimensionen sind [L].
9. **VK6 "teilweise"** haengt an der Lesart von Kleman/Friedels SU(2)-Defekten und Dechants Rotoren als "Spinoren".
   Streng gelesen waere VK6 nicht eingetroffen.
10. **VK5** ist streng geurteilt; mit belegter Kaehler-Zuordnung waere es "teilweise".

### 7.4 Kalibrierung
- **(a) Gemessen:** nichts Neues. Zitiert sind fremde Messzahlen (MICROSCOPE, LHAASO, Cassini, Eoet-Wash).
- **(b) Nuetzlich verdichtet:**
  - fuenf Lesarten der vierten Richtung (5.1);
  - Hebung = Spannung;
  - eine Kugel, drei Rollen (5.2);
  - Spin-gegen-Ladung-Kriterium mit dem Unterscheidungspunkt "Vorzeichen bei 2 pi = Faser-Halbumlauf" (5.3).
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Kaehler-Moduli = Hoehen" [L];
  - "Brown-Hebung = Skyrmion-Textur" ([M] nur fuer den Grad, [H] fuer die Physik);
  - "Hoehe = Gitterfreiheit" (de Goes ist 2D und setzt Def. 8 voraus).
- **Warnzeichen:** Meine Sicherheit "Hebehoehe = Spannungsfunktion" stieg stark. Sie stuetzt sich auf einen Abstract
  (Erickson/Lin) und Trefferzusammenfassungen. Die 3D-Fassung (Rybnikov) ist nur erwaehnt, nicht gelesen.

### 7.5 Offene Fragen
1. **An Finn:** Meint "temporaer" waehrend eines Umklappzugs (Hebebild) oder als Zeitschritt (Regge/CDT)?
2. **Ist V regulaer?** (6.1)
3. **Kaehler-Kammern = regulaere Triangulierungen** (GKZ-Sekundaerfaecher): an der Quelle lesen, bevor VK5 neu geurteilt
   wird.
4. **Begutachtung** von Amaral/Clawson/Irwin 2023 und Konstantinidis 2022 feststellen.
5. **Rybnikov 1999 und Karpenkov u. a. 2023 im Volltext:** Welche Spannungen (auf Dreiecksflaechen?) entsprechen in 3D
   einer Hebung nach R^4?
6. **Kausalitaet** einer Zusatzrichtung (Chung/Freese) nicht geprueft.

## 8. Einfach gesagt

Finns Idee einer "voruebergehenden vierten Dimension" gibt es wirklich, sogar in drei Formen. Man kann jeden Punkt des
Netzes in eine vierte Richtung anheben; ein Umklappzug passiert genau dann, wenn fuenf angehobene Punkte auf einer
gemeinsamen flachen Ebene liegen, und diese Anhebung entspricht in der Mechanik einer Spannung im Netz. Physiker benutzen
dieselben Umklappzuege ausserdem als Zeitschritte, und die gekruemmte Kugel der 600-Zelle ist zugleich der Raum aller
Drehungen. Eine "Drehdimension" gibt fuer sich allein eine Ladung, keinen Spin; halben Spin bekommt man erst, wenn das
Drehen dort an das Drehen im Raum gekoppelt ist, so wie beim Guertel-Trick, den Finns Netz schon kann. Als naechster
kleiner Test lohnt sich die Frage, ob Finns Netz V ueberhaupt so anhebbar ist; wenn nicht, gibt es fuer V diese vierte
Richtung nur als Zeit.

## 9. Quellenliste

**Abgerufen (quellen/, Abrufzeit im Dateinamen bzw. im Arbeitsfeld):**
- Sadoc, J.-F.; Mosseri, R. (1999): Geometrical Frustration. Cambridge University Press. Kapitelseite "Hopf fibration":
  https://www.cambridge.org/core/books/abs/geometrical-frustration/hopf-fibration/410D6B45DCC58B9439532E75F6475B0C
  [S Gliederung, Anfang A3] (Abruf 2).
- Sadoc, J.-F. (2001): Eur. Phys. J. E, Artikel e01035, https://epje.epj.org/articles/epje/abs/2001/09/e01035/e01035.html
  [S Treffer] (Abruf 1); Titel [L?] "Helices and helix packings derived from the {3,3,5} polytope".
- Ewha-Arbeit (Choi/Lee [L?]) (2018): Binary icosahedral group and 600 cell. Symmetry (Aug. 2018).
  https://pure.ewha.ac.kr/en/publications/binary-icosahedral-group-and-600-cell/ ;
  https://doaj.org/article/163b15fee29443aa9c9b619e4241421c [S Treffer] (Abrufe 3, 18).
- Taubes, C.; Wu, Y. (2026): Homogeneous Z/2-Harmonic Forms and Spinors on R^4 from Regular 4-Polytopes.
  https://arxiv.org/abs/2604.20840 [S Abstract] (Abruf 5).
- Gray, R. W.; Dennis, L.; Kauffman, L. H. (2026): The Mereon System, the 600-Cell, and the Exceptional Algebras E6, E7,
  E8. https://arxiv.org/abs/2604.00255 [S Abstract], Randarbeit (Abruf 5).
- Serafin, F.; Lu, J.; Kotov, N.; Sun, K.; Mao, X. (2021): Frustrated Self-Assembly of Non-Euclidean Crystals of
  Nanoparticles. Nat. Commun. 12, 4925. https://arxiv.org/abs/2010.03087 [S Abstract] (Abruf 5).
- Jackiw, R.; Rebbi, C. (1976): Spin from Isospin in a Gauge Theory. Phys. Rev. Lett. 36, 1116.
  https://doi.org/10.1103/PhysRevLett.36.1116 [S Abstract, INSPIRE] (Abruf 6).
- Hasenfratz, P.; 't Hooft, G. (1976): A Fermion-Boson Puzzle in a Gauge Theory. Phys. Rev. Lett. 36, 1119.
  https://doi.org/10.1103/PhysRevLett.36.1119 [S Abstract] (Abruf 6).
- Goldhaber, A. S. (1976): Spin and Statistics Connection for Charge-Monopole Composites. Phys. Rev. Lett. 36, 1122.
  https://doi.org/10.1103/PhysRevLett.36.1122 [S Abstract] (Abruf 6).
- Witten, E. (1981): Search for a Realistic Kaluza-Klein Theory. Nucl. Phys. B 186, 412. Ueber INSPIRE
  (https://inspirehep.net, Suche "j Nucl.Phys.B,186,412") [S Abstract] (Abruf 7).
- Sorkin, R. D. (1983): Kaluza-Klein Monopole. Phys. Rev. Lett. 51, 87. https://doi.org/10.1103/PhysRevLett.51.87
  [S Abstract] (Abruf 7).
- Gross, D. J.; Perry, M. J. (1983): Magnetic Monopoles in Kaluza-Klein Theories. Nucl. Phys. B 226, 29. Ueber
  INSPIRE (Suche "j Nucl.Phys.B,226,29") [S Abstract] (Abruf 7).
- de Goes, F.; Memari, P.; Mullen, P.; Desbrun, M. (2014): Weighted Triangulations for Geometry Processing. ACM Trans.
  Graph. 33(3). http://www.geometry.caltech.edu/pubs/dGMMD14.pdf [S] Def. 6, 8, Prop. 1, Gl. (1), (2), (10), (13),
  Abschn. 2.3, 2.4, 3.2, 4.2, 4.3 (Abruf 8).
- Erickson, J.; Lin, P. (2020): A Toroidal Maxwell-Cremona-Delaunay Correspondence. https://arxiv.org/abs/2003.10057
  [S Abstract] (Abruf 10).
- Karpenkov, O.; Mohammadi, F.; Mueller, C.; Schulze, B. (2023): A differential approach to Maxwell-Cremona liftings.
  https://arxiv.org/abs/2312.09891 [S Abstract] (Abruf 10).
- Rote, G.; Santos, F.; Streinu, I.: Pseudo-Triangulations - a Survey. https://arxiv.org/abs/math/0612672 [S Treffer]
  (Abruf 9).
- Brown, K. Q. (1979): Voronoi diagrams from convex hulls. Inf. Process. Lett. 9(5), 223-228.
  https://doi.org/10.1016/0020-0190(79)90056-5 ; Volltext https://math.wustl.edu/~victor/classes/pmf/KQBrown.pdf
  [S Treffer, nicht gelesen] (Abruf 17).
- Levy, B.; Mohayaee, R.; von Hausegger, S. (2021): A fast semi-discrete optimal transport algorithm for a unique
  reconstruction of the early Universe. https://arxiv.org/abs/2012.09074 [S Treffer] (Abruf 12).
- Gallouet, T. O.; Merigot, Q.: A Lagrangian scheme a la Brenier for the incompressible Euler equations.
  https://arxiv.org/abs/1605.00568 [S Treffer] (Abruf 12).
- McDonald, J. R.; Miller, W. A. (2008): https://arxiv.org/abs/0804.0279 [S Treffer; P HODGE-L] (Abruf 11).
- Rios-Sanchez, J.; Rodrigo, G. (2026): https://arxiv.org/abs/2609.18668; MacFadden, N. (2026):
  https://arxiv.org/abs/2605.27770; MacFadden, N.; Sheridan, E. (2025): Calabi-Yau Threefolds from Vex Triangulations,
  https://arxiv.org/abs/2512.14817. Alle [S Abstract] (Abruf 13).
- Aspinwall, P. S.; Greene, B. R.; Morrison, D. R. (1994): Calabi-Yau moduli space, mirror manifolds and space-time
  topology change in string theory. Nucl. Phys. B 416, 414. https://arxiv.org/abs/hep-th/9309097 [S Abstract; arXiv-Nr.
  L] (Abruf 14).
- Witten, E. (1993): Phases of N=2 theories in two dimensions. Nucl. Phys. B 403, 159.
  https://arxiv.org/abs/hep-th/9301042 [S Abstract; arXiv-Nr. L] (Abruf 14).
- Bernard-Bernardet, S.; Apffel, B. (2024): The spinorial ball (II): a manipulable qubit at human scale.
  https://arxiv.org/abs/2411.15059 [S Abstract] (Abruf 15).
- Touboul, P. u. a. (2022): MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle. Phys. Rev. Lett.
  129, 121102. https://doi.org/10.1103/PhysRevLett.129.121102 [S Abstract] (Abruf 16).
- Konstantinidis, N. P. (2022): Classical magnetization of a four-dimensional Platonic solid.
  https://arxiv.org/abs/2207.11077 [S Abstract] (Abruf 19).
- Waegell, M.; Aravind, P. K. (2010): Critical noncolorings of the 600-cell proving the Bell-Kochen-Specker theorem.
  J. Phys. A 43, 105304. https://arxiv.org/abs/0911.2289 [S Abstract] (Abruf 19).
- Amaral, M.; Clawson, R.; Irwin, K. (2023): Quasicrystalline Spin Foam with Matter: Definitions and Examples.
  https://arxiv.org/abs/2306.01964 [S Abstract], Begutachtung nicht festgestellt (Abruf 19).
- Cao, Z. u. a. (LHAASO) (2024): Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB
  221009A. Phys. Rev. Lett. 133, 071501. https://arxiv.org/abs/2402.06009 [S Abstract] (Abruf 20).
- Yang, Y.-M.; Bi, X.-J. u. a. (2024): JCAP 04, 060. https://arxiv.org/abs/2312.09079 [S Abstract] (Abruf 20).
- Satunin, P. S.; Troitsky, S. V. (2025): JETP Lett. 123, 73. https://arxiv.org/abs/2510.07234 [S Abstract] (Abruf 20).

**Lokal gelesen (Projektkopien, ohne Abrufzaehlung):**
- Kleman, M.; Friedel, J. (2008): Disclinations, dislocations and continuous defects: a reappraisal. Rev. Mod. Phys. 80,
  61. https://arxiv.org/abs/0704.3055 [S lokal] VI.A.4 (S. 39), VI.B.1-2 (S. 40), VII.E.1 Gl. (88)-(89) (S. 52).
  Datei RUNDE-22/geometrie-stand/hilfs/kleman-friedel-0704.3055.txt
- Tarjus, G.; Kivelson, S. A.; Nussinov, Z.; Viot, P. (2005): The frustration-based approach of supercooled liquids and
  the glass transition. J. Phys.: Condens. Matter 17, R1143. https://arxiv.org/abs/cond-mat/0509127 [S lokal] S. 14,
  19-20. Datei RUNDE-17/quellen-frustration/hilfs/p4-cm0509127.txt
- Will, C. M. (2014): The Confrontation between General Relativity and Experiment. https://arxiv.org/abs/1403.7377
- KEGEL-4D-L A1 (arXiv all:"600-cell", 41 Eintraege, Datei RUNDE-37/kegel-4d-l/quellen/A1-arxiv-600cell-*.xml): Dechant, P.-P. (2013), Acta Cryst. A69, 592,
  https://arxiv.org/abs/1307.6768; Dechant, P.-P. (2021), Adv. Appl. Clifford Alg. 31, 57,
  https://arxiv.org/abs/2103.07817; Baez, J. C. (2018), LMS Newsletter 476, 18-23, https://arxiv.org/abs/1712.06436.
  [S Abstract lokal]
- Projekt [P]: WELTKRISTALL-L, KRUEMMUNG-SPANNUNG-SPIN-L, GUERTEL-FINN-NETZ-1, GEN-04-SPIN-HALB, URSUPPE-1,
  GEOMETRIE-STAND, HODGE-L, LAMBDA-TURING-L, SKALAR-SEKTOR-L, EIS-1, dunkle-dimension-check.md.

**Nur Gedaechtnis [L]:** Edelsbrunner/Seidel 1986; Aurenhammer 1987 (nur ueber de Goes zitiert); Rybnikov 1999;
Urbantke 2003; Wu/Yang-Monopol-Kugelfunktionen; Finkelstein/Rubinstein 1968; Chung/Freese 2000; Csaki/Erlich/Grojean
2001; GKZ-Sekundaerfaecher; 2I-Darstellungsdimensionen; Skyrmion-Profil 2 arctan(R/r) als bekannter Ansatz.

---
Abgabe (date): 2026-10-05 12:39:43 CEST
