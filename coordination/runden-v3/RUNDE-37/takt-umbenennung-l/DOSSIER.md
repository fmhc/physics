# TAKT-UMBENENNUNG-L: Dossier (feldforscher fuer die Leitung, Runde 41, Literaturkarte)

- Karte: KARTE.md (E1 bis E6, A1 bis A6, Fragen 1 bis 7). Start 2026-10-04 15:26:17 CEST, Text ab 15:50:47 CEST,
  Abgabe am Ende (date).
- Grundlage: 9 von 12 Abrufen. Davon 2 arXiv-API-Bloecke (12 bzw. 17 Abstracts), 6 Volltexte und 1 Bulletin-Versuch
  ohne Inhalt. Keine Websuche.
  - Dazu lokale Volltexte aus frueheren Karten, ohne Abrufbudget: Hoehn 2014, Will 2014, Guemruekcueoglu/Saravani/Sotiriou
    2018, Visser 2002, Wolfram TI und Gorard 2020.
- Vorhersage je Abruf, Protokoll, Verstoesse und Gestrichenes stehen in ARBEITSFELD.md. Lokale Kopien liegen in quellen/
  (PDF nach pdftotext geloescht, E-Mail-Adressen entfernt).
- **Kennzeichen:**
  - [S] an der Quelle gelesen (S. = PDF-Seite der Textkopie, per Seitenvorschub gezaehlt); [S Abstract];
    [S lokal] Projektkopie hier selbst gelesen; [S sek.] nur ueber eine gelesene Sekundaerquelle;
  - [P] Projektdatei; [L] Gedaechtnis; [L?] unsicher;
  - [M] eigene Mathematik; [ES] eigener Schluss; [H] Hypothese.
- **Konvention:**
  - Horava-Kinetik K_ij K^ij - lambda K^2, Einstein lambda = 1.
  - Unser c (Impulsbild pi.pi - c pi^2) ist c = lambda/(d lambda - 1); in d = 3 entspricht c = 1/2 dem Wert lambda = 1.

## 1. Kurzfazit (Ergebnis zuerst)

1. **Was die 1/2 ist:**
   - Sie ist die Passbedingung zwischen Bewegungsenergie und Kruemmungsenergie R. Gibt es einen R-Term und keine
     bevorzugte Zeitscheibe, bleibt die freie Zeitumbenennung je Ort (lokaler Lapse) nur mit ihr eine Eichung.
   - An der Quelle: Die Hamilton-Bedingung pflanzt sich nur fort, wenn eine von vier Moeglichkeiten gilt: DeWitt-Wert
     (X = 1, unsere 1/2), kein R-Term (Carroll), keine Kinetik (Galilei) oder eine bevorzugte Blaetterung
     (Anderson 2007, Gl. 26).
2. **HKT 1976** (nur ueber zwei Sekundaerquellen gelesen):
   - Annahmen: Weg-Unabhaengigkeit, Lokalitaet, nur die Raummetrik als Variable, Invertierbarkeit.
   - Folge: DeWitt-Kombination (die 1/2) und Potential Lambda - R. Die 1/2 ist Ergebnis, die Raumzeit-Einbettung Annahme.
3. **Globaler Takt** (auch "N = 1 fest") ist lokal das projizierbare Horava-Modell (BPS 2011, S. 8).
   - Es hat keine lokale Hamilton-Bedingung; die Schwerkraft muss im Shift sitzen.
   - Stabil ist es nur fuer |lambda - 1| <~ 1e-61 (bei M* >~ 0,1 eV) und dann unter ~1e13 cm stark gekoppelt.
4. **A2 ist zu stark:** Die 1/2 und die zweite Haelfte der Lichtablenkung sind in beide Richtungen unabhaengig.
   - Gesundes Horava: lambda != 1, trotzdem gamma = 1.
   - Brans-Dicke: volle Symmetrie, trotzdem gamma != 1.
   - E3b haelt nur bei lokalem Lapse.
5. **Gitter:** Regge ist linear um flach exakt, gekruemmt quadratisch im Fehlwinkel gebrochen. Nur die Zeitschritte zu
   verkleinern stellt nichts her (3D-Beispiel). Exakt geht es in 2+1 und im flachen 4D-Sektor.

## 2. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigste zuerst)

1. **E3b (gegen die Leitung) gilt nur in einem von zwei Regimen.**
   - Erwartet war: lambda != 1 aendert die statische Lichtablenkung nicht, weil K^2 statisch verschwindet.
   - **Lokaler Lapse (nicht projizierbar, gesund): eingetroffen.** "beta_PPN = gamma_PPN = 1, xi_PPN = 0" in der
     khronometrischen Theorie, weil die kugelsymmetrischen Loesungen mit Einstein-Aether uebereinstimmen (BPS 2011,
     S. 33) [S]. lambda ist dort frei: lambda' = (1 - beta)(lambda - 1) - beta (S. 32) mit der Schranke
     "alpha, beta, lambda' <~ 0.1" (S. 33) [S]; |lambda - 1| bis etwa 0,1 ist also mit gamma = 1 vertraeglich.
   - **Globaler Takt (projizierbar): verletzt.**
     - "the perturbation of the lapse phi drops out of the quadratic Lagrangian because of the projectability
       condition" (BPS S. 12, nach Gl. 3.1) [S].
     - Im statischen Ansatz N = 1 mit Shift beta(x) stehen ausdruecklich Terme (lambda - 1)[...] in Impulsbedingung und
       Feldgleichung (Mukohyama 2010, S. 14, Gl. 61) [S].
     - "For beta = 0 ... only a trivial solution" (S. 15) [S]: Ohne Shift gibt es dort keine Schwerkraft.
     - K = div(Shift) ist nicht null, also faellt der lambda K^2-Term statisch nicht weg [M].
   - Korrigierte Erwartung: E3b gilt fuer lokalen Lapse. Fuer globalen Takt steht lambda in den statischen Gleichungen.
     Ob es die Lichtablenkung aendert, ist nicht berechnet; das Fernfeld geht fuer lambda -> 1+0 stetig in Schwarzschild
     ueber (S. 15-16, 26-27) [S].
2. **"Raum-Netz mit aeusserer Uhr" ist in der Literatur genau benannt und quantitativ schlecht** (A1 war vorsichtiger).
   - Der Fall ist woertlich beschrieben: "restricting the lapse N to a fixed value, say N = 1. Then N drops out of the
     action. The only difference of the resulting theory from the projectable model is the absence of the integral
     Hamiltonian constraint, so locally the two theories are equivalent" (BPS S. 8) [S].
   - Projizierbar gilt: Mit M* >~ 0,1 eV verlangt Stabilitaet "|lambda - 1| <~ 1e-61" (Gl. 3.8, S. 13) [S]; dann
     "fails to provide adequate description of gravity within distances ~ 1e13 cm" (S. 18) [S].
3. **"Langwellig" ist nicht der richtige Moderator; nur die Zeitschritte zu verfeinern stellt die Symmetrie nicht her**
   (gegen A4, E2 und meine Vorhersage F8).
   - Im 3D-Beispiel mit kosmologischer Konstante: "gauge invariance is not being restored in this limit", Zeltstange
     gegen null bei festem Raumgitter, "almost degenerate simplices" (Bahr/Dittrich 2009, S. 11) [S].
   - Erst die Verfeinerung in Raum und Zeit zugleich hilft dort, zur ersten Ordnung in Lambda (ebd.).
   - Der Bruch geht "quadratically in the curvature" gegen null (S. 4) [S], bzw. "to an order quadratic in the deficit
     angle" (Bonzom/Dittrich 2013, S. 15) [S].
   - Korrigiert: Der Moderator heisst Fehlwinkel je Simplex, nicht Wellenlaenge allein.
4. **"Schwerkraft ist Taktgefaelle (h_00)" haengt an der Wahl der Zeitscheiben** (gegen A6 und E4, Teil 1).
   - "all information about the Newtonian potential can be included in the shift and the spatial metric. ... Even in
     general relativity, we can choose a gauge in which the lapse is space-independent at least locally, and in this
     gauge the Newtonian potential is encoded in the shift and the spatial metric" (Mukohyama 2010, S. 16) [S].
   - Invariant bleibt nur das Gefaelle zwischen ruhenden Uhren entlang der Killing-Zeit, g_00 = -(N^2 - N_i N^i) [M].
5. **Die 1/2 braucht die Kruemmungsenergie R** (gegen meine Vorhersage F4 und als Schaerfung von A1).
   - Die Fortpflanzung der Hamilton-Bedingung ist H-dot ~ (2/N)(X - 1) B Y D_i(N^2 D^i p) (Anderson 2007, Gl. 26,
     S. 13) [S].
   - Mit B = 0, also ohne R-Term, gibt es "strong or 'Carrollian' gravity options for both W = 1 and for W != 1"
     (S. 13) [S]; jedes c ist dann erlaubt.
   - Meine Rechnung M1 (ARBEITSFELD Abschn. 4) gibt denselben Stoerterm, ((d - 1) c - 1) mal Gradient der Impulsspur [M].
6. **Der gemeinsame Lichtkegel (A5) ist Literatur, aber mit Ausnahmen, und das Aequivalenzprinzip folgt nicht.**
   - Barbour/Foster/O Murchadha 2002: Ein Skalarfeld "must have the same characteristic speed as gravity" [S Abstract].
   - Anderson 2007 bestaetigt das fuer propagierende Felder ("enforcement of a universal null cone", S. 15) [S]. Er
     laesst aber nicht propagierende Carroll- und Galilei-Felder zu (S. 16) [S] und sagt: "it does not imply the
     equivalence principle" [S Abstract].
7. **Exakte diskrete Verformungsalgebra gibt es auch im homogen gekruemmten 4D-Sektor**, nicht nur im flachen
   (Bonzom/Dittrich 2013, Abstract und S. 15) [S]. Den Bruch verursacht die inhomogene Kruemmung.
8. **Loll 1998: Die raeumlichen Diffeo-Kommutatoren auf dem Hamilton-Gitter schliessen "in the limit of small lattice
   spacing"** [S Abstract]. Erwartet hatte ich "schliessen nicht". Das ist A4s "langwellig", aber nur fuer das Regime
   Raumgitter mit kontinuierlicher Zeit.
9. **Hamber/Williams 1997 widersprechen woertlich Bahr/Dittrich.**
   - Sie zeigen "exact local gauge invariance ... for arbitrarily triangulated background manifolds", "mostly the two
     dimensional case" [S Abstract].
   - Ungeloest; Moderator vermutlich die Dimension (2D-Regge-Einstein ist topologisch [L]).
10. Kleinere Verstoesse:
    - Verlindes Abstract beansprucht auch die Einstein-Gleichungen; E5 sagte nur "Newton".
    - HKTs Zeitumkehr war nur Hilfsannahme, "separately removed in (Kuchar, 1974)" (Anderson S. 9) [S].
    - Eine Gedaechtnis-ID war falsch (1003.5480).

## 3. Erwartungen E1 bis E6 mit Ausgang und Fundstelle

| Nr | Erwartung (kurz) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | HKT: Weg-Unabhaengigkeit + Lokalitaet + Ordnung legt Einsteins H samt lambda = 1 fest, bis auf G und Lambda | **eingetroffen, mit genauerer Annahmenliste** | Anderson 2007, S. 9 [S sek.]: "path-independence of the foliation" -> Algebra (12)-(14); "representation postulate"; Zeitumkehr "separately removed in (Kuchar, 1974)"; "The remaining assumption is locality"; Induktionsbeweis: "quadratic in p^ij ... in the DeWitt supermetric combination plus a (potential) piece"; Potential "A - R" ueber Lovelock; Restannahme "precisely 2 degrees of freedom per space point ... the only variables are among the 6 independent h_ij". Gomes/Shyam 2016, S. 5 [S sek.]: zusaetzlich "invertibility criteria between the momentum and the extrinsic curvature". Original (Annals Phys. 96, 88) nicht gelesen |
| E2 | Bahr/Dittrich, Dittrich: Eckverschiebung exakt nur flach; gekruemmt gebrochen; Bruch verschwindet im Kontinuums- bzw. langwelligen Grenzfall; perfekte Wirkungen stellen her | **im Kern eingetroffen; "langwellig" verletzt (Verstoss 3)** | Bahr/Dittrich 2009a, S. 2, 4, 11 [S]: "generically broken"; "approximate gauge invariance"; Eigenwerte "go to zero (quadratically in the curvature)"; Kontinuum: "our results will support this view" (also gestuetzt, nicht bewiesen); Zeitgrenzfall allein stellt nichts her. Dittrich 2008: "Generically ... approximate ones, however there are incidences in which the symmetries are exactly preserved" [S Abstract]. Bahr/Dittrich 2009b: perfekte Wirkung "in three dimensions with cosmological constant, and in four dimensions for one simplex" [S Abstract] |
| E3 | Horava projizierbar: keine lokale Hamilton-Bedingung, lambda frei, Skalar-Graviton; gesund: gamma = beta = 1, Abweichung in alpha1, alpha2 | **eingetroffen** | Mukohyama 2009: "the Hamiltonian constraint is not a local equation ... but an equation integrated over a whole space" [S Abstract]; BPS 2011, S. 12 (Skalarmodus, Lapse faellt heraus), S. 33 (gamma = beta = 1), S. 35 [S]; Schranken \|alpha1\| < 1e-4, \|alpha2\| < 4e-7 (Guemruekcueoglu u. a. 2018, S. 2, nach Will) [S lokal]; Koyama/Arroja: Geist bei c_s^2 > 0, sonst klein negativ, "casts doubt on the validity of the projectable version" [S Abstract] |
| E3b | Gegen die Leitung: A2 zu stark; lambda != 1 aendert die statische Ablenkung nicht; projizierbar -> Dunkle Materie als Integrationskonstante | **Schluss (A2 zu stark) eingetroffen; Begruendung nur bei lokalem Lapse (Verstoss 1)**; Dunkle-Materie-Teil eingetroffen | BPS S. 33 [S]; Mukohyama 2010, S. 14-16, Gl. (60)-(61) [S]; Mukohyama 2009 [S Abstract]: "a component which behaves like pressureless dust emerges as an 'integration constant'" |
| E4 | Newton aus g_00; Soldner = Haelfte; COW 1975; Compton-Uhr umstritten | **Soldner eingetroffen; g_00 eichabhaengig (Verstoss 4); COW nicht geprueft; Compton-Uhr eingetroffen** | Will 2014, S. 40 [S lokal]: Soldner und Einstein 1911 "yield only the '1/2' part"; "The first factor '1/2' holds in any metric theory, the second 'gamma/2' varies from theory to theory". Mukohyama 2010, S. 16 [S]. Wolf u. a. 2011: Compton-Phasendifferenz "actually zero in ... all metric theories", Deutung "unsound" [S Abstract]. COW [L] (Abele/Leeb 2012 nennt COW im Abstract nicht). Lan u. a. 2013 nicht geprueft |
| E5 | Jacobson 1995 volle Einstein-Gleichungen (Lambda als Integrationskonstante); Verlinde heuristisch Newton; Kritik Kobakhidze (Neutronen) | **Jacobson eingetroffen (Lambda-Teil nur [L]); Verlinde teilweise verletzt; Kobakhidze eingetroffen, praezisiert** | Jacobson 1995: "The Einstein equation is derived ... for all the local Rindler causal horizons"; "gravitational lensing by matter energy distorts the causal structure" [S Abstract]. Verlinde 2010: "A relativistic generalization ... directly leads to the Einstein equations" [S Abstract]. Kobakhidze 2011a: "ultra-cold neutrons in the gravitational field of Earth"; 2011b: "neutron interference experiments and experiments on gravitational bound states" [S Abstract] |
| E6 | Bulletin "Confluence and Causal Invariance": Kausalinvarianz = Unabhaengigkeit von der Reihenfolge, verbunden mit Kovarianz; HKT nicht zitiert | **am Bulletin nicht pruefbar** (dritter Fehlschlag: "Could not resolve host"); **an den lokalen Kerntexten eingetroffen** | Gorard 2020, S. 1 [S lokal]: Kausalinvarianz "is equivalent to a discrete version of general covariance, with changes to the updating order corresponding to discrete gauge transformations"; S. 9: "confluence is a necessary condition for ... causal invariance". Wolfram TI, S. 137 [S lokal]: "a notion of 'path independence' [55] - or what we will call 'causal invariance'", Ref. [55] = Church/Rosser 1936. grep "Hojman\|Kucha\|Teitelboim" in TI, Gorard 2020 (beide), Gorard 2011.12174: 0 Treffer |

## 4. Pruefung der Antworten A1 bis A6

| Nr | Antwort der Leitung (kurz) | Urteil | Begruendung (Fundstellen) |
|---|---|---|---|
| A1 | 1/2 = Bedingung, dass die freie Zeitumbenennung je Ort respektiert wird; Raum-Netz mit aeusserer Uhr gibt 1/5 [M, ungeprueft] | **haelt im Kern, zu knapp** | Kern richtig: Anderson Gl. (26) [S]; M1 [M]; Gomes/Shyam Gl. (69): GR-Kinetik "pi^ij pi_ij - 1/(D-2) pi^2" [S], also c = 1/(d - 1). Es fehlt "zusammen mit R": Ohne R-Term waere jedes c erlaubt (Carroll, Anderson S. 13). Die 1/5 ist arithmetisch richtig [M, nachgerechnet], die Zuordnung c = lambda/(3 lambda - 1) jetzt dreifach belegt (AGSW 2013 [S ueber CDT-HORAVA-L]; Anderson Gl. 20-21: X = 2W/(3W - 1), X/2 = c [S]; Gomes/Shyam Gl. 69 [S]). Die 1/5 haengt an den Annahmen (gleichverteilte Kanten, eigene Kanten-Kinetik). Staerker als die 1/5 ist der Literaturbefund: Ein Netz mit fester Uhr ist lokal projizierbar (BPS S. 8) |
| A2 | Hamilton-Bedingung kruemmt zugleich den Raum durch Energie = zweite Haelfte der Lichtablenkung; "beide Haelften haben dieselbe Wurzel" | **zu stark** (als allgemeine Aussage falsch, in GR richtig) | In GR, statisch und linear, liefert die Hamilton-Bedingung die Raumkruemmung, also den gamma-Teil [L]; die Aufteilung "1/2 aus dem Aequivalenzprinzip, gamma/2 aus der Raumkruemmung" steht bei Will 2014, S. 40 [S lokal]. Aber: gesundes Horava hat lambda != 1 und gamma = 1 (BPS S. 33 [S]); Brans-Dicke hat volle Diffeo-Invarianz [L] und gamma = (1 + omega)/(2 + omega) (Will Tab. 3, S. 34 [S lokal]). HKT schliessen Brans-Dicke nur ueber "nur Metrik" aus (Anderson S. 9 [S]). Gemeinsam ist beiden Haelften die **lokale** Hamilton-Bedingung, nicht die 1/2 |
| A3 | HKT 1976: Weg-Unabhaengigkeit legt Einsteins H samt 1/2 fest [L] | **haelt**; Kennzeichen auf [S sek.] heben, Annahmen nennen | Anderson S. 9; Gomes/Shyam S. 5 [S sek.]. "Weg-Unabhaengigkeit allein" reicht nicht: Lokalitaet, nur Metrik (2 Freiheitsgrade), Invertierbarkeit und Lovelock (fuer das Potential) gehoeren dazu; die Signatur steckt im Vorzeichen der Algebra (Anderson S. 9) |
| A4 | Auf Gittern gilt die Symmetrie nur naeherungsweise, bei langen Wellen (Bahr/Dittrich) [L?] | **zu stark bzw. unscharf** | 4D-Regge: linear um flach exakt fuer jede Wellenlaenge (Hoehn 2014, S. 1 [S lokal]; Dittrich/Hoehn 2010 [S Abstract]); gekruemmt gebrochen, quadratisch im Fehlwinkel (Bahr/Dittrich S. 4; Bonzom/Dittrich S. 15 [S]); Zeit allein verfeinern hilft nicht (Bahr/Dittrich S. 11, 3D-Beispiel mit Lambda [S]); exakt in 2+1 und im flachen bzw. homogen gekruemmten 4D-Sektor (Bonzom/Dittrich [S]). "Nur langwellig" stimmt fuer unser Hamilton-Gitter auf Finns Netz (TENSOR-EIS-PYRO-1 [P]) und fuer Lolls raeumliche Kommutatoren [S Abstract], nicht fuer Regge allgemein. Das kubische Gitter ist linear exakt [P] |
| A5 | Vermutlich teilen alle Felder, die an dieselbe Geometrie koppeln, dann denselben Lichtkegel [H] | **haelt, ist aber Literatur statt Vermutung, mit zwei Einschraenkungen** | BFO 2002 [S Abstract]; Anderson 2007, S. 15-16 [S]: gemeinsamer Kegel fuer propagierende Felder; nicht propagierende Carroll- und Galilei-Felder vertraeglich; Aequivalenzprinzip folgt nicht [S Abstract]. Ohne exakte lokale Umbenennung (Horava) koennen Tensor-, Skalar- und Lichttempo verschieden sein (Guemruekcueoglu u. a. 2018, Gl. 4 und Abschn. III: Lorentz-Verletzung im Materiesektor braucht einen eigenen Unterdrueckungsmechanismus [S lokal]) |
| A6 | Alltagsschwerkraft fast ganz Takt-Effekt (h_00, COW 1975); reiner Takt-Effekt = Soldner-Wert [L] | **haelt im Kern; "Takt-Effekt" ist eichabhaengig; COW ungeprueft** | Soldner: Will S. 40 [S lokal]. h_00: richtig in statischer Eichung [L]; mit ortsunabhaengigem Lapse steckt dasselbe Feld im Shift (Mukohyama S. 16 [S]); bei globalem Takt ist das sogar Pflicht (BPS S. 12 [S]). COW [L] |

**Wortlaut-Vorschlaege** (je ein Ersatz fuer die Chat-Antwort; Fundstellen wie in der Tabelle):

- **A1:** "Die 1/2 ist die Bedingung, dass die freie Zeitumbenennung je Ort mit Einsteins Kruemmungsenergie zusammenpasst
  (Anderson 2007, Gl. 26). Ohne Kruemmungsterm waere jede Zahl erlaubt, mit bevorzugter Zeitscheibe ebenfalls. Ein
  Raum-Netz mit fester aeusserer Uhr ist in der Literatur das projizierbare Horava-Modell (Blas/Pujolas/Sibiryakov 2011,
  S. 8). Unsere Kanten-Abschaetzung gibt dort 1/5 [M, Annahmen: gleichverteilte Kanten, eigene Kanten-Bewegungsenergie]."
- **A2:** "In Einsteins Theorie kruemmt dieselbe Hamilton-Bedingung den Raum durch Energie; das gibt die zweite Haelfte der
  Lichtablenkung (Will 2014, S. 40). Zwingend verbunden sind die 1/2 und diese zweite Haelfte aber nicht:
  - Eine Theorie mit bevorzugter Zeit und lambda != 1 hat die volle Ablenkung (BPS 2011, S. 33).
  - Eine mit voller Umbenennung plus Zusatzskalar (Brans-Dicke) hat sie nicht (Will 2014, Tab. 3).
  - Gemeinsam ist nur, dass die Hamilton-Bedingung an jedem Ort gelten muss. Bei nur globalem Takt fehlt das (Mukohyama
    2009), und lambda steht dann auch in den statischen Gleichungen (Mukohyama 2010, Gl. 61)."
- **A3:** "Hojman/Kuchar/Teitelboim 1976 (nach Anderson 2007 und Gomes/Shyam 2016; Original nicht gelesen) fordern
  - dass die Entwicklung nicht vom Weg durch die Zwischenflaechen abhaengt,
  - dazu Lokalitaet und nur die Raummetrik als Variable.
  Daraus folgt Einsteins Hamilton-Funktion mit der DeWitt-Kombination (unsere 1/2) bis auf G und Lambda. Die Einbettung
  in eine Raumzeit und ihre Signatur sind dabei vorausgesetzt."
- **A4:** "Auf Gittern ist die Symmetrie je nach Bauweise linear exakt (Regge um flach, kubisches Gitter) oder nur
  langwellig (Finns Netz, TENSOR-EIS-PYRO-1). Mit Kruemmung bricht sie in 4D-Regge, quadratisch im Fehlwinkel
  (Bahr/Dittrich 2009). Zurueck kommt sie erst, wenn Raum und Zeit zugleich feiner werden; feinere Zeitschritte allein
  reichen nicht (gezeigt in ihrem 3D-Beispiel mit Lambda). Exakt bleibt sie in 2+1 Dimensionen und im flachen 4D-Fall
  (Bonzom/Dittrich 2013)."
- **A5:** "Ist die Zeitumbenennung je Ort exakt, muss jedes Feld, das sich ausbreitet und an dieselbe Raummetrik koppelt,
  den Lichtkegel der Schwerkraft teilen (Barbour/Foster/O Murchadha 2002; Anderson 2007, S. 15-16). Felder, die sich
  nicht ausbreiten, sind ausgenommen; das Aequivalenzprinzip folgt daraus nicht. Mit bevorzugter Zeit duerfen die Tempi
  verschieden sein."
- **A6:** "Fuer langsame Koerper bestimmt in der ueblichen statischen Beschreibung fast nur der Gang der Uhren (h_00) die
  Schwerkraft [L]. Das ist aber eine Wahl der Zeitscheiben: Laeuft die Uhr ueberall gleich, steckt dasselbe Feld im
  'fliessenden Raum' (Shift) (Mukohyama 2010, S. 16). Ein reiner Uhren-Effekt gibt nur die Soldner-Haelfte der
  Lichtablenkung, die zweite Haelfte kommt aus der Raumkruemmung (Will 2014, S. 40). COW 1975 [L]."

## 5. Antworten auf die Fragen 1 bis 7

**Frage 1: Was zeigt HKT, unter welchen Annahmen? Folgt die 1/2 aus der Weg-Unabhaengigkeit allein?**
- **Annahmen** [S sek.: Anderson 2007, S. 9; Gomes/Shyam 2016, S. 5]:
  - Weg-Unabhaengigkeit der Blaetterung zwischen Anfangs- und Endflaeche; daraus folgt die Verformungsalgebra
    (Teitelboim 1973), Anderson Gl. (12)-(14).
  - Darstellungspostulat: Die Bedingungen schliessen wie die Verformungen.
  - Lokalitaet.
  - Nur die 6 Komponenten h_ij als Variablen (2 Freiheitsgrade).
  - Invertierbarkeit Impuls <-> extrinsische Kruemmung.
  - Die Zeitumkehr war Hilfsannahme und ist seit Kuchar 1974 entbehrlich.
- **Ergebnis:**
  - Ultralokal in p.
  - Quadratisch in DeWitt-Kombination plus ein Potential, das ueber Lovelock zu Lambda - R wird.
  - Mit umgekehrtem Vorzeichen in (14) ergibt sich euklidische GR.
- **Folgt die 1/2 aus der Weg-Unabhaengigkeit allein? Nein.** [M + S]
  - Im Mechanismus kommt sie aus der Klammer {Kinetik(x), Potential(y)}. Der Stoerterm ist ((d - 1) c - 1)(d_i pi)
    d^i delta (M1), bei Anderson (X - 1) B Y D_i(N^2 D^i p) (Gl. 26).
  - Sie verlangt also die Weg-Unabhaengigkeit **und** einen Kruemmungsterm R im Potential.
  - Ohne R (B = 0) ist jedes c vertraeglich (Carroll); mit bevorzugter Blaetterung (Impulsspur = 0) ebenso (Anderson
    S. 13).
- Gomes/Shyam verallgemeinern: Alle Ableitungs-Erweiterungen der Kinetik (quadratisch in pi) machen die Bedingung zweiter
  Klasse, "we do not require a specific Poisson bracket algebra" [S Abstract]. Es reicht also "die Umbenennung ist eine
  Eichung" (erste Klasse) statt der vollen Algebra.
- Ob ein rein ultralokales lambda != 1 in ihrer Klasse liegt, steht im gelesenen Text nicht ausdruecklich; den
  Ausschluss gibt M1.

**Frage 2: Wie stark bricht die Regge- bzw. Pachner-Entwicklung die Umbenennung? Passt TENSOR-EIS-PYRO-1?**
- **Regime G-a, Regge in Raum und Zeit:**
  - Flache Loesungen haben 4 Eckverschiebungen je Ecke als exakte Eichung (Bahr/Dittrich S. 4 [S]).
  - Linear um flach exakt, mit abelscher Algebra der Generatoren, "as close as one comes to a consistent hypersurface
    deformation algebra" (Hoehn S. 8 [S lokal]).
  - Gekruemmt gebrochen, kleinste Hesse-Eigenwerte ~ Kruemmung^2 (Bahr/Dittrich S. 4). Statt Bedingungen entstehen
    "pseudo constraints", der Lapse wird bestimmt statt frei (S. 2).
  - Zurueck kommt die Symmetrie erst bei Verfeinerung in Raum und Zeit, gezeigt im 3D-Beispiel mit Lambda (S. 11).
- **Regime G-b, Raumgitter mit kontinuierlicher Zeit (Hamilton-Gitter):**
  - Die diskretisierte Algebra erster Klasse wird zweiter Klasse (Hoehn S. 4 [S lokal], zu Piran/Williams,
    Friedman/Jack, Loll).
  - Raeumliche Kommutatoren schliessen nur fuer Gitterweite -> 0 (Loll 1998 [S Abstract]).
- **Passt TENSOR-EIS-PYRO-1? Ja, zu Regime G-b** [ES]:
  - kontinuierliche Zeit;
  - strenge Regeln (Zwang) noetig, also zweiter Klasse;
  - Spur-Eichdefekt nur fuer k -> 0 null, linear oder quadratisch je Richtung [P].
  - Dass das kubische Gitter linear exakt ist [P], zeigt: In G-b ist der lineare Defekt eine Frage der Bauweise, kein
    Naturgesetz.
- Die Weg-Unabhaengigkeit **innerhalb einer festen 4D-Triangulierung** ist automatisch: Die kanonische Fassung
  "exactly reproduces the dynamics and (broken) symmetries of the covariant formalism" (Dittrich/Hoehn 2010 [S
  Abstract]). Offen ist nur die Unabhaengigkeit von der Triangulierung bzw. vom gewaehlten lokalen Lapse.

**Frage 3: Globaler gegen lokalen Takt bei Horava; rechnet REGEL.md Abschn. 8 richtig?**
- **Projizierbar (globaler Takt), alles [S]:**
  - Der Lapse faellt aus der quadratischen Wirkung (BPS S. 12).
  - Die Hamilton-Bedingung gilt nur integriert, und ein Staub-Anteil erscheint als Integrationskonstante (Mukohyama 2009).
  - Skalar-Graviton: Geist bei c_s^2 > 0, sonst instabil (Koyama/Arroja). Stabil nur fuer |lambda - 1| <~ 1e-61, dann
    stark gekoppelt unter ~1e13 cm (BPS S. 13, 18).
  - Statisch sitzt die Schwerkraft im Shift, und lambda steht in den Gleichungen (Mukohyama 2010, Gl. 61).
  - Es gibt zwei Lager:
    - Mukohyama: nichtperturbative Stetigkeit fuer lambda -> 1+0; er fragt selbst nach einem Vainshtein-Effekt (S. 26).
    - BPS und Koyama/Arroja: perturbativ stark gekoppelt.
    - Moderator: perturbativ gegen nichtperturbativ.
- **Gesund, lokaler Lapse N(x):**
  - gamma = beta = 1, xi = 0 (BPS S. 33).
  - alpha1, alpha2 ungleich null, Schranken \|alpha1\| < 1e-4, \|alpha2\| < 4e-7 (Guemruekcueoglu u. a. S. 2).
  - GW170817 gibt \|beta_ae\| <~ 1e-15 (S. 3) [S lokal].
  - G_N = 1/(8 pi M^2 (1 - alpha/2)) (BPS Gl. 5.30, S. 32) [S].
- **REGEL.md Abschn. 8** [M, nachgerechnet]:
  - Das Richtungsmittel gibt (2 tr hdot^2 + (tr hdot)^2)/15, also lambda = -1/2.
  - (1 - lambda P)(1 - c P) = 1 mit P^2 = 3P gibt c = lambda/(3 lambda - 1) = 1/5. Richtig.
  - Fuer lambda = -1/2 ist (lambda - 1)/(3 lambda - 1) = 3/5 > 0, also omega^2 = -(3/5) xi k^2: Gradienten-Instabilitaet,
    kein Geist. Das passt zu LAMBDA-1 [P] und zu Koyama/Arroja (c_s^2 < 0) [M].
  - Die Rechnung ist eine Abschaetzung unter Annahmen, keine Messung.

**Frage 4:** siehe Abschnitt 4 (A1 bis A6).

**Frage 5: Takt als Schwerkraft und die Ausgleichs-Ansaetze; wer liefert Takt und Raum im Verhaeltnis 1:1?**
- **Sakharov:** ja, aber eingesetzt.
  - "Assume you are given a Lorentzian manifold"; die Ein-Schleifen-Wirkung enthaelt dann sqrt(-g)(c0 + c1 R + c2 R^2)
    (Visser 2002, S. 1-2) [S lokal].
  - Das 1:1 kommt aus der vorausgesetzten Kovarianz von Geometrie und Regularisierung. Auf unseren Netzen muss man es
    pruefen (KOVARIANZ-KUGEL-1 [P]).
- **Jacobson 1995:** ja.
  - Die Forderung gilt "for all the local Rindler causal horizons", und "lensing by matter energy" verformt die
    Kausalstruktur [S Abstract].
  - [M] Wenn S_ab k^a k^b = 0 fuer alle Nullvektoren k gilt, dann ist S_ab = f g_ab. Nullrichtungen tasten Zeit- und
    Raumteil zugleich ab, also steckt das 1:1 im Lichtkegel der Eingabe.
- **Verlinde 2010:**
  - Newton entsteht aus Entropie und Gleichverteilung. Relativistisch nutzt er die Komar-Masse mit dem
    Rotverschiebungsfaktor e^phi (RUNDE-35 graviton-netz-l, Abschn. 5.2, dort [S]). Das ist eine Takt-Groesse entlang
    der Killing-Zeit.
  - Der Abstract beansprucht die vollen Einstein-Gleichungen [S Abstract]; woher der Raumteil kommt, habe ich nicht
    gelesen [L?].
  - Kritik: Kobakhidze 2011 mit Neutronen-Bindungszustaenden und -Interferenz [S Abstract].
- **[ES] Keiner der drei gewinnt das 1:1 aus einem reinen Takt.** Wer es hat, setzt den lokalen Lichtkegel
  (Lorentz-Kovarianz) voraus. Das ist dieselbe Groesse, die bei Anderson den gemeinsamen Kegel erzwingt (Regel 6,
  Abschn. 6).

**Frage 6: Wolframs Kausalinvarianz gegen HKTs Weg-Unabhaengigkeit: dasselbe, verwandt oder verschieden?**
- **Verwandt, nicht dasselbe** [ES aus S lokal]:
  - Beide verlangen, dass das Ergebnis nicht von der Reihenfolge lokaler Fortschritte abhaengt.
  - Wolfram: gleicher Kausalgraph fuer jede Aktualisierungsreihenfolge (Gorard S. 1). Kausalinvarianz entspricht damit
    der Einbettbarkeit: eine Raumzeit fuer alle Blaetterungen.
- **Die Unterschiede:**
  - Wolframs "path independence" ist Church-Rosser-Konfluenz aus dem Umschreiben (TI S. 137, Ref. [55]); das gleiche Wort
    ist Zufall.
  - HKTs Algebra hat eine Strukturfunktion g^ij, also die Raummetrik (Gomes/Shyam S. 2: "this Poisson algebra strictly
    speaking isn't a lie algebra because the structure functions depend on the canonical variables"). Kausalinvarianz
    ist rein kombinatorisch und kennt keine Metrik.
  - HKT legen die 1/2 erst zusammen mit "nur Metrik", Lokalitaet und R fest. Gorard gewinnt die Einstein-Gleichungen
    anders, aus Dimensionserhaltung (WOLFRAM-SCAN-L [P]).
  - HKT werden in den gelesenen Wolfram-Kerntexten nicht zitiert (grep 0).
- **Unterscheidungspunkt** [H]: Eine kausalinvariante Regel, deren effektive Kontinuumsdynamik lambda != 1 oder einen
  Zusatzskalar hat. HKT verbieten das, wenn die Theorie lokal ist und nur die Metrik hat; Kausalinvarianz verbietet es
  nicht. Nicht gerechnet, in keiner gelesenen Quelle.

**Frage 7: Lokale Takte mit Weg-Unabhaengigkeit auf einem Tetraeder-Netz (Pachner-Zuege als lokale Takte)?**
- **Bekannt** [S]:
  - Pachner- bzw. Zeltzuege sind die lokale, "multi-fingered" Zeit des kanonischen Regge (Dittrich/Hoehn 2012 [S
    Abstract]; Bonzom/Dittrich S. 1).
  - Der 1-4-Zug erzeugt "four 'lapse and shift' variables and four conjugate vertex displacement generators", der 2-3-Zug
    ein Graviton (Hoehn S. 1 [S lokal]). Der lokale Takt ist also die Eckverschiebung am neuen Punkt.
  - Exakte Weg-Unabhaengigkeit, also eine diskrete Verformungsalgebra, gibt es in 2+1 (Lambda = 0) und im flachen bzw.
    homogen gekruemmten 4D-Sektor (Bonzom/Dittrich).
  - Linear um flach ist sie exakt (Hoehn). Allgemein in 4D bricht sie, quadratisch im Fehlwinkel; der Lapse wird dann
    von der Kruemmung bestimmt (Bahr/Dittrich S. 2, 4).
  - **Auswege:** perfekte bzw. vergroeberte Wirkungen (bisher 3D mit Lambda, 4D ein Simplex), nichtlokale
    Diskretisierungen, zylindrische Konsistenz (Bonzom/Dittrich S. 15).
  - Fuer das linearisierte 4D-Regge gibt es nach Dittrich/Kaminski/Steinhaus 2014 kein lokales invariantes Mass (ueber
    TETRAEDER-L [S Abstract]).
  - Wohin die Bedingung gehoert (an die Ecken oder an die Zellen), muss man waehlen; das ist nicht beliebig (Bonzom/
    Dittrich S. 24).
- **Fuer Finns Netz** [ES]:
  - In TENSOR-EIS-PYRO-1 (B1) sitzen die Regge-Ecken an den Tetraedermitten [P]. Der "Takt je Einzelteil" waere also die
    Eckverschiebung (Zeltstange) an jeder Tetraedermitte.
  - Mit Kruemmung ist er nicht mehr frei, sondern schwach festgelegt. Das ist die Gitter-Fassung von "jedes Teil hat
    seinen eigenen Takt", und er wird umso freier, je flacher das Netz im Kleinen ist.
- Kartenvorschlag: Abschnitt 8.

## 6. Regime und Moderatoren (Regel 1)

| Regime-Paar | Moderator | Belege |
|---|---|---|
| R1 globaler Takt gegen lokaler Lapse | Ob N nur von t oder von (t, x) abhaengt; also ob die Hamilton-Bedingung je Ort gilt | BPS S. 8, 12, 33; Mukohyama 2009, 2010 [S] |
| R2 Kontinuum gegen Gitter (G-a Regge in Raum und Zeit, G-b Raumgitter mit kontinuierlicher Zeit) | Fehlwinkel je Simplex (Bruch ~ Fehlwinkel^2); ob auch die Zeit diskret ist; Bauweise des Gitters | Bahr/Dittrich S. 2, 4, 11; Hoehn S. 1, 4, 8; Loll 1998; TENSOR-EIS-PYRO-1 [P] |
| R3 2+1 gegen 3+1 | topologisch (keine lokalen Freiheitsgrade) gegen propagierend | Bonzom/Dittrich S. 15 [S] |
| R4 nur Metrik gegen Zusatzfelder | HKTs 2-Freiheitsgrade-Annahme; entscheidet, ob gamma an der Symmetrie haengt | Anderson S. 9; Will Tab. 3 [S] |
| R5 projizierbar: zwei Lager | perturbativ (stark gekoppelt, BPS, Koyama/Arroja) gegen nichtperturbativ (Stetigkeit, Mukohyama) | BPS S. 18; Mukohyama S. 15, 26 [S] |
| R6 Hamber/Williams gegen Bahr/Dittrich | Dimension (2D topologisch) bzw. Begriff der Eichtransformation [H] | beide [S Abstract]; Volltext Hamber/Williams nicht gelesen |

**Regel 6 (Kopplung vor Bauteil):**
- **Zur 1/2 fuehren mindestens vier Wege** [S]:
  - HKT-Algebra mit nur Metrik;
  - Weinbergs Lorentz-invariantes masseloses Spin 2 (Gomes/Shyam S. 5);
  - Fortpflanzung der quadratischen Bedingung im 3-Raum-Ansatz (BFO; Anderson Gl. 26);
  - 4D-Regge (REGGE-4D-1: -2 = -1/c [P]).
- [ES] Die gemeinsame Groesse ist der **lokale Lichtkegel**, also das Passverhaeltnis von Zeit- zu Raumableitungen an
  jedem Ort. Bei Anderson ist der Stoerterm ein Produkt aus Kinetik- (Y) und Kruemmungskoeffizient (B) und verschwindet
  nur bei Passung (X = 1). Die 1/2 ist die Kopplungsbedingung zwischen dem Takt-Teil und dem Raum-Teil, kein Bauteil.
- **Zu gamma = 1 fuehren drei Wege:** GR, gesundes Horava mit lambda != 1, Einstein-Aether [S].
  - Gebrochen wird gamma durch einen Zusatzskalar, an den die Materie koppelt (Brans-Dicke).
  - Die gemeinsame Groesse ist, an welche Metrik die Materie koppelt und ob ein statischer Zusatzskalar existiert [ES].

## 7. Unterscheidungspunkte (Regel 2)

| Paar | Wo beide passen | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|---|
| U1 E3b lokal gegen global | lambda = 1 (beide GR) | Statisches Feld einer Masse bei lambda != 1. Lokaler Lapse: gamma = 1 (BPS). Globaler Takt: lambda in Gl. (61), Feld im Shift | Natur: nein, projizierbar verlangt \|lambda - 1\| <~ 1e-61 (BPS S. 13). In silico: ja, Netz mit lambda_eff = -1/2 einmal mit festem und einmal mit freiem lokalem Lapse |
| U2 "Symmetrie gibt gamma = 1" gegen "nur Metrik noetig" | GR | Zusatzskalar mit endlichem omega_BD: gamma != 1 bei voller Symmetrie | Ja: Lichtablenkung und Laufzeit; (1 + gamma)/2 = 0,99992 +- 0,00023 aus VLBI (Will S. 41); Cassini: (1 + gamma)/2 "within at most 0.0012 percent of unity", Skalar-Tensor "must have omega > 40,000" (Will S. 43) [S lokal] |
| U3 Gitter G-a gegen G-b | k -> 0 | Spur-Eichdefekt bei endlichem k auf demselben Netz: G-a (Zeit diskret, Regge) linear exakt, G-b (Finns Netz B1) O(k) | Ja, in silico (TENSOR-EIS-PYRO-1 hat G-b; G-a fehlt) |
| U4 Kausalinvarianz gegen HKT | GR-artige Regeln | kausalinvariante Regel mit effektivem lambda != 1 | unklar, nicht gerechnet [H] |
| U5 Jacobson gegen Verlinde | Newton | Raumteil (gamma) ohne Zusatzannahme: Jacobson ueber Nullrichtungen ja; Verlinde statisch nur Komar/Takt [L?] | nur im Formalismus, nicht empirisch (klassisch gleiche Gleichungen) |
| U6 Mukohyama gegen BPS (projizierbar) | lineare Theorie um flach | nichtlinearer Bereich unter ~1e13 cm: Vainshtein-artige Rettung oder Verlust der Vorhersagbarkeit | nach Recherchestand offen |

## 8. Kartenvorschlag (einer): TAKT-KOMMUTATOR-1 (Schreibtisch, dann Kleintest)

- **Frage:** Kommutieren zwei lokale Takte auf Finns Netz? Konkret: Ergeben zwei Zeltzuege an benachbarten Ecken A und B
  in der Reihenfolge AB dasselbe wie in BA, bei frei gewaehlten lokalen Zeltstangen (Lapse) N_A, N_B? Das ist HKTs
  Weg-Unabhaengigkeit auf dem Gitter, also der diskrete Kommutator {H(A), H(B)}.
- **Bau:**
  - Raumscheibe = eine B1-Kopie von Finns Netz, also die Tetraeder-Oktaeder-Wabe (fcc). Die Oktaeder werden mit einer
    festen Diagonale trianguliert, symmetrisch und vorab festgelegt (vgl. EINE-WELT-LOCH-1).
  - Euklidisches 3+1-Regge wie bei Hoehn; ein Zeltzug je Ecke (Tetraedermitte).
  - Hintergrund: flach plus eine Gravitationswelle der Amplitude eps und Wellenlaenge L.
  - Messgroesse: D = Abstand der eichinvarianten Enddaten (Fehlwinkel und Laengen der Endflaeche nach Eichfixierung)
    zwischen AB und BA, ueber eps = 0,01 bis 0,1 und L/a = 4 bis 16.
  - Dazu die kleinsten Hesse-Eigenwerte je Ecke (Kriterium von Bahr/Dittrich).
- **Pflichtvariante lokal gegen global:**
  - (L) N_A, N_B frei;
  - (G) N_A = N_B fest (globaler Takt), die lokalen Lapse-Gleichungen ersetzt durch ihre Summe.
- **Ableitbarkeitsprobe:**
  1. eps -> 0: D = 0 exakt, weil die Eckverschiebung um flach eine Eichung ist (Hoehn S. 1; Bahr/Dittrich S. 4). Das ist
     eine **Kontrolle, keine Messung**.
  2. Exponent in eps: D ~ eps^2 ist vorab ableitbar ("quadratically in the curvature", Bahr/Dittrich S. 4;
     Bonzom/Dittrich S. 15). Auch Variante (G) ist linear ableitbar: Ein Staub-artiger Zusatzanteil wie bei
     projizierbarem Horava (Mukohyama 2009 [S Abstract]; BPS S. 8), bei lambda = 1 ohne Ausbreitung
     (omega^2 ~ (lambda - 1), LAMBDA-1 [P]; [M]). Also auch nur Kontrolle.
  3. **Nicht ableitbar:** Vorfaktor und Exponent in L/a auf dieser Geometrie, ob D fuer die Auf- und die Ab-Kopie gleich
     ist, und ob sich D ueber viele Takte aufsummiert (Drift) oder mittelt.
     - Die gelesene Literatur rechnet nur kleine Konfigurationen (Bahr/Dittrich: wenige Simplizes) und keine
       periodischen Netze (nach Recherchestand; ohne Websuche).
     - Vorab-Vermutung [H]: D ~ eps^2 (a/L)^4, weil der Fehlwinkel ~ eps (a/L)^2 ist und der Bruch ~ Fehlwinkel^2.
  4. Projekt-grep: keine Zug- bzw. Zeltzug-Rechnung im Projekt; "tent move" steht nur in der Hoehn-Kopie, und
     TETRAEDER-L meldet "keine Rechnung mit Zugfolgen" [P].
  5. **Kann scheitern, in drei Richtungen:**
     - D ~ eps bei kleinem eps: Fehler im Bau, oder das Netz ist keine echte Triangulierung.
     - Exponent in L/a >= 4: Der lokale Takt ist langwellig frei; das stuetzt den Wortlaut A4.
     - Exponent klein oder D faellt nicht mit L: Die Reihenfolge der Takte hinterlaesst eine Spur auf grossen Skalen;
       Finns Einzeltakt waere dann physikalisch sichtbar.
- **Bezug:** Die Karte ergaenzt PACHNER-TAKT-1 (TETRAEDER-L K1, Gravitonen je Zugfolge). Beide teilen Code und Netz, also
  ein Agent (Kopplung).
- **Laufzeit** [ungemessene Schaetzung]: Je Zeltzug ein Newton-Loeser mit wenigen Dutzend Unbekannten; der Scan
  (5 eps x 3 L x 2 Reihenfolgen x 2 Varianten) dauert Minuten auf der Kleintest-Spur. Der Netzbau (Triangulierung der
  Oktaeder, periodische Wellen-Anfangsdaten) ist der eigentliche Aufwand und gehoert vorab in einen Schreibtisch-Plan.

## 9. Gegensweep-Befunde (Regel 4; ganze Liste in ARBEITSFELD.md Abschn. 7b)

**Was war so selbstverstaendlich, dass ich es nicht geprueft hatte?**
- Geprueft und gehalten:
  - "HKT sagen 'path independence'": Anderson S. 9.
  - "c = lambda/(3 lambda - 1)": dritte Quelle, Anderson Gl. 20-21.
  - "Izumi/Mukohyama behandeln die projizierbare Fassung": Mukohyama-Review S. 26-27, hier im Gegensweep nachgelesen.
    Nebenbefund: Lager-Gegensatz R5.
- Geprueft und gefallen (Abschn. 2, Verstoesse 3 und 4; Frage 6):
  - "Takt-Effekt = h_00" ist eichabhaengig.
  - "Langwellig reicht" stimmt nicht, wenn nur die Zeit verfeinert wird.
  - "Wolframs path independence = HKT" ist nur Namensgleichheit.
- Nicht geprueft:
  - COW 1975 (bleibt [L]);
  - Brans-Dicke erfuellt die Verformungsalgebra ([L], passt zu Anderson S. 9);
  - Hamber/Williams gegen Bahr/Dittrich (offen);
  - was Finn mit "pro Einzelteil" meint (R1). Zwei physikalisch verschiedene Lesarten:
    - Eigenzeit je Teilchen: in GR schon vorhanden und physikalisch; eine Compton-"Uhr" fuer sich ist keine
      beobachtbare Uhr (Wolf u. a.).
    - Lapse je Ort: Eichung, frei umstellbar.
- **Gegen die Leitung:**
  - A2 zu stark; A4 unscharf.
  - E3b (die Gegenposition der Karte selbst) gilt nur bei lokalem Lapse.
  - A1 und A5 sind staerker belegt, als die Leitung angab ([M, ungeprueft] bzw. [H] -> Literatur).

## 10. Kalibrierung

- **(a) Gemessen:**
  - (1 + gamma)/2 = 0,99992 +- 0,00023 (VLBI, Will S. 41) und Cassini mit hoechstens 0,0012 % Abweichung (Will S. 43);
  - \|alpha1\| < 1e-4, \|alpha2\| < 4e-7;
  - GW170817-Schranke auf c_T;
  - Neutronen-Bindungszustaende im Schwerefeld (nur ueber Kobakhidze-Abstracts).
  - Alles andere sind Theorie und Rechnung.
- **(b) Nuetzlich verdichtet [ES]:**
  - "die 1/2 ist die Passbedingung Kinetik zu R bei lokaler Umbenennung";
  - "Netz mit fester Uhr = projizierbar";
  - "Moderator Fehlwinkel je Simplex, nicht Zeitschritt";
  - Andersons vier Faktoren = unsere vier Projektfaelle;
  - "1/2 und gamma unabhaengig, gemeinsam nur die lokale Hamilton-Bedingung".
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "bei globalem Takt aendert lambda != 1 die Lichtablenkung". Belegt ist nur lambda in den statischen Gleichungen; die
    Ablenkung ist nicht berechnet, und das Fernfeld geht fuer lambda -> 1 in Schwarzschild ueber.
  - "Finns Einzeltakt = gebrochene Lapse-Eichung im Regge-Netz" (meine Lesart).
  - "TENSOR-EIS-PYRO-1 = Regime G-b" (meine Zuordnung).
- **Warnzeichen:** Meine Sicherheit in "E3b gilt nur lokal" stieg von einer eigenen Rechnung (M2) auf zwei Quellen. Zugleich
  zerfiel die Frage in "lambda steht in den statischen Gleichungen" (belegt) und "die Lichtablenkung aendert sich"
  (unbelegt). Belastbar ist nur der erste Teil.

## 11. Offene Fragen

1. Aendert lambda != 1 bei globalem Takt die Lichtablenkung messbar, und wie (Loesung von Mukohyama Gl. 61 fuer
   endliches lambda)?
2. Hamber/Williams (exakte Eichinvarianz fuer beliebige Hintergruende, vor allem 2D) gegen Bahr/Dittrich (generisch
   gebrochen in 4D): nur Dimension oder ein anderer Begriff von Eichung?
3. Gibt es eine kausalinvariante Wolfram-Regel mit effektivem lambda != 1 (U4)? Das Bulletin "Confluence and Causal
   Invariance" bleibt ungelesen (Host nicht aufloesbar).
4. Woher nimmt Verlinde den Raumteil der Einstein-Gleichungen (Volltext Abschn. 5 nicht gelesen)?
5. R1 an Finn: Meint "dark tick pro Einzelteil" einen Takt je Teilchen (Materie-Eigenzeit) oder je Netzort (Lapse)?
6. Ist die Gradienten-Instabilitaet bei unserem lambda_eff = -1/2 auf dem Gitter dieselbe wie im projizierbaren Horava
   (LAMBDA-1 [P] sagt ja fuer das lineare Modell)? Sie tritt nur auf, wenn das Netz einen Kruemmungsterm hat.

## 12. Selbstanzeigen

1. **Vorhersage F4 nach dem Abruf eingetragen:**
   - Der Wortlaut stand vor dem Abruf im Edit-Aufruf (15:38:24). Der Edit schlug wegen eines Gross-/Kleinschreibfehlers
     im Suchtext fehl; der Abruf lief parallel (15:38:34).
   - Eingetragen wurde derselbe Wortlaut danach. Ab F5 lief alles strikt nacheinander.
2. **Falsche Gedaechtnis-ID** in F2: 1003.5480 ist nicht Jacobsons Horava-Aether-Papier, sondern "Truthful Fair
   Division"; als Teil eines Blockabrufs verbraucht.
3. **F3 ohne Inhalt** (DNS-Fehler), als Abruf gezaehlt. E6 deshalb nur an Ersatzquellen geprueft.
4. **HKT-Original nicht gelesen** (Annals of Physics, nicht auf arXiv; nur arXiv und Bulletin erlaubt). Alle
   HKT-Aussagen sind [S sek.] ueber Anderson 2007 und Gomes/Shyam 2016.
5. **Seitenzahlen** sind PDF-Seiten der Textkopien, per Seitenvorschub gezaehlt; sie koennen von gedruckten Seitenzahlen
   abweichen.
   - BPS Gl. (3.1) ist in der Textkopie unsauber; ich zitiere nur den (lambda - 1)-Faktor und den Satz zum Lapse.
   - Die Normierung von G_abcd in Gomes/Shyam Gl. (2) ist in der Kopie unklar und wird nicht verwendet.
6. **Werkzeuge:** curl, pdftotext, grep, sed, date, dazu head, wc, ls, tr, cut, mkdir, rm (Anzeige und Dateiverwaltung im
   Kartenordner). Kein python, awk oder perl. Keine Websuche, keine Rechnung ausser Schreibtisch [M].
7. **Personendaten:** PDFs geloescht, E-Mail-Adressen in den Textkopien durch "[E-Mail entfernt]" ersetzt (3 Stellen).
   Die API-XML enthalten Autorennamen und Institute (bibliographisch); belassen.
8. **Versiegeltes:** Projekt-grep mit Ausschluss von *VERSIEGELT*, T8-SOLL-*, *ks-1*/*KS-1*/*ks1*, vertraege-20260925,
   ks-1-dk-lauf(e), secrets und Geheimnis-Mustern; keine solche Datei geoeffnet.
9. **Regel 7:** Keine 24-Monats-Suche moeglich (Websuche gesperrt; arXiv-API nur nach ID). Kein "widerlegt" vergeben.
   A2 heisst "zu stark", gestuetzt auf etablierte Gegenbeispiele (BPS 2011, Will 2014), nicht auf Front-Literatur.
10. **Lesetiefe:**
    - Volltexte nur abschnittsweise per grep und sed: Gomes/Shyam S. 1-5, 22, 25; BPS S. 8, 12-13, 18, 24, 32-35;
      Mukohyama S. 14-16, 26-27; Anderson S. 9, 11-16; Bahr/Dittrich S. 1-4, 11, 15; Bonzom/Dittrich S. 1-2, 15, 23-24.
    - Der Rest sind Abstracts.
11. **Kein frischer Leser** hat dieses Dossier gegengelesen.

## 13. Quellenliste mit Abrufstand

Abrufe 2026-10-04, Zeiten CEST per date. "lokal" heisst Kopie aus einer frueheren Karte, hier gelesen, ohne Abrufbudget.

| Autor, Jahr, Titel | URL | Abruf / Lesestand |
|---|---|---|
| Anderson, E. (2007): On the recovery of geometrodynamics from two different sets of first principles. Stud. Hist. Phil. Mod. Phys. 38, 15 | https://arxiv.org/abs/gr-qc/0511070 | F1 15:35:17 Abstract; F7 15:42:57 Volltext (S. 9, 11-16) |
| Bahr, B.; Dittrich, B. (2009a): (Broken) Gauge Symmetries and Constraints in Regge Calculus. CQG 26, 225011 | https://arxiv.org/abs/0905.1670 | F1 Abstract; F8 15:44:19 Volltext (S. 1-4, 11, 15) |
| Bahr, B.; Dittrich, B. (2009b): Improved and Perfect Actions in Discrete Gravity. PRD 80, 124030 | https://arxiv.org/abs/0907.4323 | F1 Abstract |
| Barbour, J.; Foster, B. Z.; O Murchadha, N. (2002): Relativity without relativity. CQG 19, 3217 | https://arxiv.org/abs/gr-qc/0012089 | F1 Abstract |
| Blas, D.; Pujolas, O.; Sibiryakov, S. (2010): A healthy extension of Horava gravity. PRL 104, 181302 | https://arxiv.org/abs/0909.3525 | F2 15:36:39 Abstract |
| Blas, D.; Pujolas, O.; Sibiryakov, S. (2011): Models of non-relativistic quantum gravity: the good, the bad and the healthy. JHEP 1104:018 | https://arxiv.org/abs/1007.3503 | F2 Abstract; F5 15:40:25 Volltext (S. 8, 12-13, 18, 24, 32-35) |
| Blas, D.; Sanctuary, H. (2011): Gravitational Radiation in Horava Gravity. PRD 84, 064004 | https://arxiv.org/abs/1105.5149 | F2 Abstract |
| Bonzom, V.; Dittrich, B. (2013): Dirac's discrete hypersurface deformation algebras. CQG 30, 205013 | https://arxiv.org/abs/1304.5983 | F1 Abstract; F9 15:45:10 Volltext (S. 1-2, 15, 23-24) |
| Dittrich, B. (2008/09): Diffeomorphism symmetry in quantum gravity models. Adv. Sci. Lett. 2, 121 | https://arxiv.org/abs/0810.3594 | F1 Abstract |
| Dittrich, B.; Freidel, L.; Speziale, S. (2007): Linearized dynamics from the 4-simplex Regge action. PRD 76, 104020 | https://arxiv.org/abs/0707.4513 | F1 Abstract |
| Dittrich, B.; Hoehn, P. A. (2010): From covariant to canonical formulations of discrete gravity. CQG 27, 155001 | https://arxiv.org/abs/0912.1817 | F1 Abstract |
| Dittrich, B.; Hoehn, P. A. (2012): Canonical simplicial gravity. CQG 29, 115009 | https://arxiv.org/abs/1108.1974 | nur ueber TETRAEDER-L [S Abstract dort] |
| Foster, B. Z.; Jacobson, T. (2006): Post-Newtonian parameters and constraints on Einstein-aether theory. PRD 73, 064015 | https://arxiv.org/abs/gr-qc/0509083 | F2 Abstract |
| Giulini, D. (2015): Dynamical and Hamiltonian formulation of General Relativity | https://arxiv.org/abs/1505.01403 | F1 Abstract (ohne Befund) |
| Gomes, H.; Shyam, V. (2016): Extending the rigidity of general relativity. J. Math. Phys. 57, 112503 | https://arxiv.org/abs/1608.08236 | F1 Abstract; F4 15:38:34 Volltext (S. 1-5, 22, 25) |
| Guemruekcueoglu, A. E.; Saravani, M.; Sotiriou, T. P. (2018): Horava Gravity after GW170817 (arXiv v2, Feb. 2018; Zeitschrift nicht gelesen) | https://arxiv.org/abs/1711.08845 | lokal RUNDE-37/licht-gleich-l/quellen/arxiv-1711.08845.txt (S. 1-3) |
| Hamber, H. W.; Williams, R. M. (1997): Gauge Invariance in Simplicial Gravity. NPB 487, 345 | https://arxiv.org/abs/hep-th/9607153 | F1 Abstract |
| Hoehn, P. A. (2014): Canonical linearized Regge Calculus: counting lattice gravitons with Pachner moves | https://arxiv.org/abs/1411.5672 | lokal RUNDE-37/tetraeder-l/quellen/F13-1411.5672.txt (S. 1-2, 4, 8 und Literaturliste) |
| Hojman, S. A.; Kuchar, K.; Teitelboim, C. (1976): Geometrodynamics Regained. Annals Phys. 96, 88 | (nicht auf arXiv) | nicht gelesen; [S sek.] ueber Anderson 2007 und Gomes/Shyam 2016 |
| Horava, P. (2009): Quantum Gravity at a Lifshitz Point. PRD 79, 084008 | https://arxiv.org/abs/0901.3775 | F2 Abstract |
| Izumi, K.; Mukohyama, S. (2010): Stellar center is dynamical in Horava-Lifshitz gravity. PRD 81, 044008 | https://arxiv.org/abs/0911.1814 | F2 Abstract; Einordnung ueber Mukohyama 2010, S. 26-27 |
| Jacobson, T. (1995): Thermodynamics of Spacetime: The Einstein Equation of State. PRL 75, 1260 | https://arxiv.org/abs/gr-qc/9504004 | F2 Abstract |
| Kobakhidze, A. (2011a): Gravity is not an entropic force. PRD 83, 021502 | https://arxiv.org/abs/1009.5414 | F2 Abstract |
| Kobakhidze, A. (2011b): Once more: gravity is not an entropic force | https://arxiv.org/abs/1108.4161 | F2 Abstract |
| Koyama, K.; Arroja, F. (2010): Pathological behaviour of the scalar graviton in Horava-Lifshitz gravity. JHEP 1003:061 | https://arxiv.org/abs/0910.1998 | F2 Abstract |
| Loll, R. (1998): On the diffeomorphism commutators of lattice quantum gravity. CQG 15, 799 | https://arxiv.org/abs/gr-qc/9708025 | F1 Abstract |
| Mukohyama, S. (2009): Dark matter as integration constant in Horava-Lifshitz gravity. PRD 80, 064005 | https://arxiv.org/abs/0905.3563 | F2 Abstract |
| Mukohyama, S. (2010): Horava-Lifshitz Cosmology: A Review. CQG 27, 223101 | https://arxiv.org/abs/1007.5199 | F2 Abstract; F6 15:41:36 Volltext (S. 14-16, 26-27) |
| Sotiriou, T. P.; Visser, M.; Weinfurtner, S. (2009): Quantum gravity without Lorentz invariance. JHEP 0910:033 | https://arxiv.org/abs/0905.2798 | F2 Abstract |
| Abele, H.; Leeb, H. (2012): Gravitation and quantum interference experiments with neutrons. NJP 14, 055010 | https://arxiv.org/abs/1207.2953 | F2 Abstract (COW nicht genannt) |
| Verlinde, E. (2011): On the Origin of Gravity and the Laws of Newton. JHEP 1104:029 | https://arxiv.org/abs/1001.0785 | F2 Abstract; Volltextstellen ueber RUNDE-35 graviton-netz-l [S dort] |
| Visser, M. (2002): Sakharov's induced gravity: a modern perspective. Mod. Phys. Lett. A (laut Kopie "to appear") | https://arxiv.org/abs/gr-qc/0204062 | lokal RUNDE-37/induziert-g-l/quellen/visser-gr-qc-0204062.txt (S. 1-2) |
| Wolf, P. u. a. (2011): Does an atom interferometer test the gravitational redshift at the Compton frequency? CQG 28, 145017 | https://arxiv.org/abs/1012.1194 | F2 Abstract |
| Wolfram, S. (2020): A Class of Models with the Potential to Represent Fundamental Physics (Technical Introduction) | https://www.wolframphysics.org/technical-introduction/ | lokal RUNDE-37/wolfram-scan-l/quellen/A4 (S. 137, Literaturliste) |
| Gorard, J. (2020): Some Relativistic and Gravitational Properties of the Wolfram Model | https://www.wolframcloud.com/obj/wolframphysics/Documents/some-relativistic-and-gravitational-properties-of-the-wolfram-model.pdf | lokal wolfram-scan-l/quellen/A35 (S. 1, 9, 12-15) |
| Piskunov, M. (2020): Confluence and Causal Invariance (Bulletin) | https://bulletins.wolframphysics.org/2020/11/confluence-and-causal-invariance/ | F3 15:37:59: "Could not resolve host", kein Inhalt |
| Projekt: RUNDE-36/REGEL.md; RUNDE-36/lambda-1; RUNDE-37/cdt-horava-l/DOSSIER.md; RUNDE-37/tetraeder-l/DOSSIER.md; RUNDE-37/tensor-eis-pyro-1/ERGEBNIS.md; RUNDE-37/wolfram-scan-l/DOSSIER.md; RUNDE-37/wolfram-kev-scan/ERGEBNIS.md; RUNDE-41.md; RUNDE-22/geometrie-stand/ERGEBNIS.md; RUNDE-35/graviton-netz-l/ARBEITSFELD.md | lokal | gelesen |
| Rohdaten | quellen/F1-api-hkt-regge.xml, F2-api-horava-ppn-ausgleich.xml, F4 bis F9 (.txt) | - |

## 14. Einfach gesagt

Die 1/2 fehlt uns nicht, weil eine Kraft fehlt. Sie ist die Bedingung dafuer, dass jeder Ort seine eigene Uhr frei vor-
oder zurueckstellen darf, ohne dass sich physikalisch etwas aendert. Das klappt nur, wenn Bewegungsenergie und
Raumkruemmung genau in diesem Verhaeltnis zueinander passen. Ein Netz mit nur einem gemeinsamen Takt fuer alle ist in der
Forschung gut bekannt: Dort fehlt diese Freiheit, es entsteht ein zusaetzlicher, wackliger Modus, und die Schwerkraft muss
als "fliessender Raum" statt als Gefaelle der Uhren auftreten. Finns "Takt je Einzelteil" ist also die richtige Zutat,
aber er muss frei umstellbar sein; auf Tetraeder-Netzen geht das exakt nur in Sonderfaellen und sonst nur ungefaehr, umso
besser, je glatter das Netz im Kleinen ist. Die zweite Haelfte der Lichtablenkung haengt dagegen nicht zwingend an der
1/2: Es gibt Theorien mit falscher 1/2 und voller Ablenkung und umgekehrt.

## Zeitbox

- Start 15:26:17, Abrufe 15:35:17 bis 15:45:10, Text ab 15:50:47 CEST, Abgabe 2026-10-04 15:58:53 CEST (alles date); innerhalb der 75 min.
