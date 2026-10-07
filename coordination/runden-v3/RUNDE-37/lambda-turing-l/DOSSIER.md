# LAMBDA-TURING-L: Dossier. Was sagen Lambda-Kalkuel, Church-Rosser und die Church-Turing-These ueber Finns Netz?

- feldforscher fuer Leitung claude-primary (Runde 48, Finns Auftrag vom 05.10.2026).
- **Zeiten (date):** Start 2026-10-05 10:48:34 CEST; Abrufe 10:52:30 bis 11:02:46; Dossier ab 11:08:16; Abgabe am Ende
  (Zeitbox-Zeile).
- **Abrufe: 20 von 20.** 12 Websuchen und 8 Seitenabrufe, numeriert A1-A13 und A15-A21 (die Nummer 14 ist nicht
  vergeben). Davon 1 ohne Inhalt (A21, HTTP 301, eigener Fehler). Der zweite Bulletin-Abruf war nicht noetig.
- Protokoll mit Erwartung vor jedem Abruf, Ergebnis und Verstossvermerk: ARBEITSFELD.md. Lokale Kopien in quellen/:
  - A1 (Bulletin, HTML und Text)
  - A6 (Nabutovsky/Ben-Av), A7 (Geroch/Hartle), A13 (Kruszewski/Mikolov): PDF und Text
  - A18 (Church/Rosser 1936, JSTOR-Scan ohne Textschicht, als Bild gelesen)
- **Kennzeichen:**
  - [S] an der Quelle gelesen (Seite bzw. Zeile; Seiten = PDF-Seiten per Seitenvorschub, bei A18 Zeitschriftenseiten);
    [S Abstract] nur Abstract gelesen;
  - **[S Treffer]** nur der Treffertext der Websuche (Suchmaschinen-Zusammenfassung), die Seite selbst nicht gelesen;
    schwaecher als [S Abstract]. Vor einer Verwendung in einem Vertrag an der Quelle lesen;
  - [S lokal] Projektkopie hier gelesen; [P] Projektbefund; [L] Gedaechtnis, ungeprueft; [M] Mathematik;
    [ES] eigener Schluss; [H] Hypothese.

## 1. Ergebnis zuerst

1. **Konfluenz und Kausalinvarianz sind verschiedene Dinge; fuer terminierende Systeme folgt keine aus der anderen** [S].
   - Gelesen ist das Bulletin, das im Projekt dreimal scheiterte (Piskunov 2020, ueber web.archive.org).
   - Fuer terminierende Systeme zeigt es mit einem Gegenbeispiel, dass Kausalinvarianz ohne Konfluenz moeglich ist.
     Damit gilt Gorards gesetzte Aussage "confluence is a necessary condition for causal invariance" dort nicht.
   - Die Aussage ist im Projekt als Befund gefuehrt; bei Gorard steht sie ohne Beweis [S lokal]. Fuer nicht
     terminierende Systeme ist Kausalinvarianz im Bulletin nicht definiert.
   - Zur Physik aeussert sich das Bulletin ausdruecklich nicht.
   - Fuer Finns Netz heisst das: gleiche Endzustaende und gleiche Ursachenstruktur getrennt pruefen.
2. **Berechenbarkeit bricht auch bei fester Topologie, aber erst in 4D** [S, S Treffer].
   - In 4D gibt es fuer eine bestimmte Mannigfaltigkeit keine berechenbare Schranke fuer die Zahl der Zuege zwischen
     Triangulierungen (Nabutovsky/Ben-Av 1992/93). Fuer S^4 war das 1992 offen; dass es heute noch offen ist, ist [L].
   - In 3D ist die Schranke berechenbar (Mijatovic fuer S^3; allgemein nach Burton, nur theoretisch).
   - Die Grenze liegt also zwischen 3D und 4D, nicht zwischen fester und wechselnder Topologie.
   - Geroch/Hartle sagen nur "indications" und nennen selbst Auswege.
3. **Ohne Wegwerfen ist die Reihenfolge fast gleichgueltig** [S].
   - Church/Rosser 1936 beweisen fuer Churchs Kalkuel, in dem nichts weggeworfen wird (lambda-I), mehr als Konfluenz
     (Theorem 2, S. 479): Hat ein Ausdruck eine Normalform, erreicht **jede** Reduktionsfolge sie in beschraenkt vielen
     Schritten.
   - Der Moderator ist das Loeschen von Information.
   - In Finns Netz loeschen der 4-1-Zug und die Projektion bei der Umklapp-Uebergabe (Lesart R) [P, ES].
4. **Umkehrbare oertliche Graphdynamik erhaelt die Eckenzahl** [S Abstract, A17; der Wortlaut "almost
   vertex-preserving" nur S Treffer, A12].
   - Das zeigen Arrighi u. a. (causal graph dynamics, Fassung v4 vom Juli 2026). Lokale Erzeugung und Vernichtung von
     Ecken gelingt dort nur in drei gelockerten Rahmen.
   - Das ist genau Finns 1-4/4-1-Frage unter Umkehrbarkeit, mit ausdruecklichem Bezug auf diskrete Quantengravitation.
5. **Finns Netz ist mit reellen Kantenlaengen keine Gandy-Maschine, gerundet wahrscheinlich schon** [ES aus S Treffer].
   - Auf dem exakt symmetrischen Netz fallen zwei Probleme zusammen [ES, M; L fuer den Nulltest]:
     - Nicht-Konfluenz: kosphaerische Oktaeder, Delaunay nicht eindeutig.
     - Nicht-Entscheidbarkeit: Gleichheitstest reeller Zahlen.
   - Die Verbindung "Verformungsalgebra = Konfluenz" fand ich in der Literatur nicht (zwei Suchen); sie bleibt [H].

## 2. Urteile LT1 bis LT7 (gegen den unveraenderten Wortlaut der Karte)

| Nr | Vorhersage (woertlich) | Wahrsch. | Urteil | Beleg mit Fundstelle |
|---|---|---|---|---|
| LT1 | [L] Kontrolle: Church/Rosser 1936: Beta-Reduktion im ungetypten Lambda-Kalkuel ist konfluent. Die Normalform ist eindeutig, falls es sie gibt; der Kalkuel ist nicht stark normalisierend. | 90 % | **teilweise eingetroffen** | Satz 1: Theorem 1, S. 479: "If A conv B, there is a conversion from A to B in which no expansion precedes any reduction" [S]; bewiesen fuer Churchs Kalkuel mit der Bedingung, dass x in R frei vorkommt (lambda-I); der lambda-K-Fall ist die "third kind of conversion" (S. 481, Fortsetzung S. 482 nicht in der Kopie) [S]. Satz 2: Corollary 2, S. 479: "its normal form is unique (to within applications of Rule I)" [S], also bis auf Umbenennung. Satz 3 steht dort nicht. Stattdessen Theorem 2, S. 479: "any sequence of reductions starting from A will lead to B ... after at most m reductions". "Nicht stark normalisierend" gilt nur fuer Terme ohne Normalform [L] |
| LT2 | [L] Gandy 1980 beweist: Jede diskrete, deterministische Maschine, die seine Prinzipien I bis IV erfuellt (darunter oertliche Kausalitaet mit begrenzter Ausbreitung), berechnet nur Turing-berechenbare Funktionen. | 85 % | **eingetroffen** (nur ueber Treffertexte; Original nicht gelesen) | "From these four principles, Gandy proves that what can be calculated by a device satisfying Principles I-IV is computable"; Prinzip IV abstrahiert "a lower bound on the linear dimensions of every atomic part" und "an upper bound (the velocity of light) on the speed of propagation of changes"; Prinzip III "unique reassembly" [S Treffer, A5]. Copeland/Shagrir 2007: ideale physikalische Maschinen ausserhalb der Gandy-Klasse, die Nicht-Turing-Funktionen berechnen [S Treffer] |
| LT3 | [L] Geroch/Hartle 1986: Weil 4-Mannigfaltigkeiten nicht algorithmisch klassifizierbar sind (Markov 1958), kann eine Summe ueber 4D-Topologien in der Quantengravitation nicht berechenbar sein. Bei fester Topologie entfaellt dieses Argument. | 75 % | **teilweise eingetroffen** (Satz 1 abgeschwaecht ja, Satz 2 nein) | Satz 1: Engpass ist "the elimination of duplications ... whether two simplicial 4-manifolds are topologically identical is undecidable" (GH, S. 16) [S]. GH schwaechen selbst ab: "All this is not to say that quantum gravity will admit measurable numbers that are not computable" (S. 16) [S], Grenzwerte koennen berechenbar sein, Ausweg "duplications ... not to be excluded" (S. 17) [S], Folge "merely an inconvenience" (S. 18) [S]. Eingetroffen also nur in der Lesart "kann moeglicherweise nicht berechenbar sein". Satz 2 nicht eingetroffen: Nabutovsky/Ben-Av, Prop. 1 (S. 3) und Prop. 2 (S. 5) [S]: fuer die nicht erkennbare S0 (4-Sphaere mit 46 angehaengten Henkeln vom Index 2) keine "computationally ergodic" Zugmenge, s(N) nicht rekursiv; woertlich: "we discuss a Markov process for one fixed topological type ... essentially different from the result of Geroch and Hartle" (S. 6) [S] |
| LT4 | [L] In 3D kann der Lawson-Umklapp-Algorithmus aus einer beliebigen Zerlegung vor Delaunay stecken bleiben (Joe), in 2D nicht. Die Pachner-Graphen von 3D-Zerlegungen sind zusammenhaengend, mit berechenbarer Schranke fuer S^3 (Mijatovic). | 65 % | **eingetroffen** (Treffer-Ebene) | Joe um 1990: "one cannot, in general, monotonically flip from any triangulation to the Delaunay triangulation, but the incremental algorithm works"; 2D: "every triangulation can be monotonically transformed" [S Treffer, A8; Santos math/0601746, Edelsbrunner/Muecke math/9410208]. Mijatovic: weniger als a t^2 2^(b t^2) Pachner-Zuege, a <= 6e6, b < 5e4 [S Treffer, A9]. Burton (1110.6080): fuer jede 3-Mannigfaltigkeit "a theoretical computable function that bounds the distance of two triangulations in the Pachner graph" [S Treffer]. Praezisierung: "stecken bleiben" heisst "monoton nicht erreichbar" |
| LT5 | [L?] Das Wolfram-Bulletin unterscheidet Konfluenz (gleiche Endzustaende) von Kausalinvarianz (isomorphe Kausalgraphen) und verbindet nur Letztere mit allgemeiner Kovarianz. | 60 % | **teilweise eingetroffen** (Teil 1 ja und staerker, Teil 2 nein) | Piskunov, 16.11.2020 [S, A1]. Definitionen: "causal invariant if and only if the causal graphs for singleway evolutions with any possible event ordering functions are isomorphic"; "confluent if and only if any pair of partial singleway evolutions ... can be continued ... to reach isomorphic final states". Dazu: "neither of them implies the other" (fuer terminierende Systeme; nur fuer solche ist Kausalinvarianz dort definiert). Teil 2: "We will not make any comments in this note about the physics claims made above." Den Bezug zu "relativistic invariance" stellt nur das zitierte Glossar her |
| LT6 | [H] Mindestens eine Arbeit verbindet die Hyperflaechen-Verformungsalgebra (Dirac, HKT) ausdruecklich mit Konfluenz bzw. Kausalinvarianz eines Ersetzungssystems. | 40 % | **nicht eingetroffen** (nach Recherchestand nicht belegt; kein "gibt es nicht") | Zwei Suchen (A4, A19) [S Treffer]: Treffer nur getrennt, Wolfram-Texte (Kausalinvarianz als diskrete Kovarianz, ohne HKT) und Bonzom/Dittrich 1304.5983 (Verformungsalgebra, ohne Konfluenz). Lokale greps: HKT in Wolfram-Kerntexten 0 Treffer [P]; Bulletin ohne Physik [S]; Gorard ohne HKT [S lokal]. Die Suchmaschinen-Zusammenfassung "connects path independence ... to confluence" ist keine Quelle |
| LT7 | [L] In Lambda- bzw. Programm-Suppen entstehen ohne Vorgabe selbsterhaltende Organisationen (Fontana/Buss 1994) bzw. Selbstreplikatoren (Aguera y Arcas u. a. 2024). Eine umkehrbare, energieerhaltende Variante mit demselben Befund ist nicht bekannt. | 55 % | **eingetroffen**, mit zwei Einschraenkungen | Fontana/Buss: Ebene 0 Selbstberechner "quickly emerged", Ebene 1 abgeschlossene Mengen, Ebene 2 Verbuende [S Treffer; S lokal sekundaer: Kruszewski/Mikolov, Textkopie Z. 59-66 und 108-118, S. 1-3]. Aguera y Arcas u. a.: "self-replicators tend to arise", "with and without background random mutations"; aber "a counterexample of a minimalistic programming language where self-replicators are possible, but so far have not been observed to arise" [S Abstract]. Satz 2 nach Recherchestand: Naechster Fall ist Combinatory Chemistry, massenerhaltend mit spontaner Selbstvermehrung, aber mit einseitigen Reduktionen und ohne Energie (S. 3, Gl. 1-4) [S]. Umkehrbare Graphdynamik (Arrighi u. a.) ist ohne Entstehungsbefund [S Abstract] |

**Bedeutung (Abgleich mit der vorab geschriebenen Bedeutung der Karte):**
- LT2 eingetroffen: Die Einordnung "mit endlicher Genauigkeit eine Gandy-Maschine" haelt [ES]. Mit reellen Laengen gilt
  sie nicht (Abschnitt 4).
- LT3 nur teilweise: Der vorab notierte Satz "Solange die Zuege die Topologie nicht aendern, gilt das Argument nicht"
  ist so nicht haltbar. Richtig ist: Fuer 3D-Raumscheiben gibt es kein solches Hindernis. Fuer Summen ueber
  4D-Geschichten gibt es eines, auch bei fester Topologie (Nabutovsky/Ben-Av).
- LT4 und LT6: "Konfluenz = Ersetzungssprache fuer die Weg-Unabhaengigkeit" bleibt [H] ohne Literaturbeleg. Der Test
  "Form A gegen Form B" ist in Kartenvorschlag K1 eingebaut.
- LT7: Lambda-Suppen sind ein Muster fuer Entstehen, aber nur mit Wegwerfen bzw. aeusserem Fluss. Siehe Abschnitt 4.4.

## 3. Antworten auf die Fragen 1 bis 6

**Frage 1: Church-Rosser, genaue Aussage und Uebertrag**
- Original [S, Church/Rosser 1936]:
  - Theorem 1 (S. 479): Konversion als "Tal" (erst reduzieren, dann expandieren).
  - Corollary 2: Normalform eindeutig bis auf Regel I (Umbenennung gebundener Variablen).
  - Theorem 2: Normalisierbare Ausdruecke erreichen die Normalform auf jedem Reduktionsweg in hoechstens m Schritten.
- Kalkuel [S]: Churchs lambda-I ("x a free symbol of R", S. 481). Die Erweiterung auf delta-Regeln steht S. 480-481;
  lambda-K ist die "third kind" (S. 481, Rest nicht gelesen).
- Abstrakte Form [S lokal, Gorard 2020, S. 8-12]:
  - Definition 7/8: Konfluenz = Church-Rosser fuer Objekte.
  - Schwaechere Formen (lokal, semi) und staerkere (Diamant, stark): Gl. 9-12.
  - Hinweis auf das "critical pair lemma".
- Graphen und Zerlegungen:
  - Piskunov [S]: Konfluenz ueber "isomorphic final states"; Kausalinvarianz ueber isomorphe Kausalgraphen; unabhaengig.
  - "confluent up to isomorphism" fuer Hypergraph-Dominanzregeln (wolfram-scan-l/quellen/A49) [S lokal, Abstract].
- [ES] Im Graphfall heisst Church-Rosser immer "modulo Isomorphie", so wie im Original "modulo Regel I".

**Frage 2: Umklappzuege als Ersetzungssystem**
- 2D: Lawson erreicht Delaunay von jeder Triangulierung aus monoton [S Treffer].
- 3D: Monotones Umklappen von beliebigem Start kann scheitern (Joe); inkrementell klappt es [S Treffer].
  - Ob der Umklappgraph einer festen Punktmenge in 3D zusammenhaengt, ist nach meinem Wissen offen; in hoeheren
    Dimensionen gibt es unzusammenhaengende Beispiele (Santos) [L].
- Pachner-Graphen:
  - S^3: Schranke a t^2 2^(b t^2) (Mijatovic) [S Treffer].
  - Jede 3-Mannigfaltigkeit: berechenbare Schranke nur theoretisch (Burton) [S Treffer].
  - 4D: fuer S0 keine berechenbare Schranke, S^4 offen (Stand der Quelle 1992; Nabutovsky/Ben-Av S. 3-4) [S].
  - Praxis-Gegenpol: "Absence of barriers in dynamical triangulation" (hep-lat/9411070), nur Titel [S Treffer].
- Kinetisches Delaunay in 3D: nicht abgerufen. [L] In allgemeiner Lage aendert sich die Delaunay-Zerlegung bewegter
  Punkte nur durch 2-3- und 3-2-Zuege, wenn 5 Punkte kosphaerisch werden. 1-4/4-1 kommen nicht vor, weil alle Punkte
  Ecken bleiben; auf dem Torus gibt es keine Huellen-Ereignisse [ES].

**Frage 3: Konfluenz, Kausalinvarianz, Weg-Unabhaengigkeit**
- Bulletin gelesen (E6 geschlossen) [S]:
  - Gegenbeispiel "konfluent, nicht kausalinvariant": {{1},{1,2}} -> {{1,2},{2}}.
  - Gegenbeispiel "kausalinvariant, nicht konfluent": {{1,2},{2,1}} -> {{1}}.
  - "the 'CausalInvariantQ' property of MultiwaySystem checks for confluence despite its name".
  - Kausalinvarianz ist nur fuer terminierende Systeme definiert; die Verallgemeinerung ist offen (#487).
- Gorard 2020 [S lokal, S. 9-12]: Die Notwendigkeit wird nur gesetzt ("We can formalize this notion by stating that
  ..."), spaeter heisst es "Having shown that ...". Ein Beweis steht nicht da.
- HKT-Weg-Unabhaengigkeit: "two different foliations connecting the same pair of hypersurfaces ... yield the same
  evolution map" (Treffertext zu Bonzom/Dittrich 1304.5983) [S Treffer].
- Ausdrueckliche Bruecke Dirac/HKT zu Church-Rosser: nicht gefunden (LT6).
- [ES] Zuordnung:
  - HKT vergleicht Daten auf **derselben** Endflaeche, ist also der Konfluenz der Zustaende naeher als der
    Kausalinvarianz.
  - Genauer ist es ein beschrifteter Diamant: dieselben Zuege in anderer Reihenfolge.
  - [L] Spurmonoid-Begriff: unabhaengige Zuege vertauschen exakt; abhaengige mit einer Strukturfunktion.

**Frage 4: Physikalische Church-Turing-These**
- Gandy 1980: siehe LT2 [S Treffer]. Arrighi/Dowek (1102.1612) fassen Gandys Postulate als "homogeneity of space and
  time, bounded density and velocity of information" [S Treffer].
- Deutsch 1985: nicht abgerufen [L].
- Pour-El/Richards gegen Weihrauch/Zhong [S Treffer, A20]:
  - berechenbare, stetige Anfangsdaten "with however a non-computable gradient" geben eine nicht berechenbare Loesung;
  - das gilt in der Supremumsnorm; in der Energienorm bzw. in Sobolev-Raeumen ist die Loesung berechenbar.
  - Moderator: Norm bzw. Glattheit.
- Geroch/Hartle 1986 und Nabutovsky/Ben-Av 1993: siehe LT3 [S].
- 2024 bis 2026:
  - arXiv 2604.00182 (April 2026 nach der Nummer; der Treffertext sagt faelschlich 2025): Quanteneffekte vereiteln
    Beschleunigungsschemata; "strengthens the physical Church-Turing thesis at the level of computability" [S Treffer].
  - Arrighi/Durbec/Emmanuel 1805.10330, v4 vom 10.07.2026 [S Abstract].
  - Eine Arbeit zu Konfluenz bzw. Gandy fuer Regge- oder Pachner-Netze fand ich nicht.
- Tao 2016 und Cardona u. a. 2021: nicht abgerufen [L].
  - Die RAUM-GAS-L-Quellen zum Navier-Stokes-Blow-up (F17, F20) nennen weder Tao noch Turing-Vollstaendigkeit (grep 0);
    F20 nennt den rechnergestuetzten Blow-up von Chen/Hou [P].
  - Ein Bezug des RAUM-GAS-L-Blow-ups zum "Fluessigkeitscomputer" ist damit nicht belegt.

**Frage 5: Lambda-Chemie und Entstehen**
- Aufbau AlChemy: Lambda-Ausdruecke werden durch Anwendung verbunden und ausgewertet; Zufallsentnahme haelt die
  Population begrenzt [S Treffer].
- Ebenen: 0 Selbstberechner, 1 abgeschlossene Organisationen, 2 Verbuende [S Treffer; S lokal sekundaer].
- Nachfolger:
  - "Return to AlChemy" (2408.12137, 2024) und "Prebiotic Functional Programs" (2509.03534, 2025) [S Treffer, nur Titel].
  - Kruszewski/Mikolov 2020 (2003.07916) [S]: Kombinatorlogik; Reduktionen erhalten die Zahl der Kombinatoren; S
    braucht eine zweite Kopie seines dritten Arguments aus der Umgebung; einseitig; nur Kondensation/Spaltung
    gegenlaeufig.
  - Aguera y Arcas u. a. 2024 [S Abstract]: siehe LT7.
- Umkehrbare Varianten:
  - Kausale Graphdynamik: Umkehrbarkeit erzwingt (fast) gleiche Eckenzahl; Erzeugung/Vernichtung nur in drei
    gelockerten Rahmen [S Abstract, A17; S Treffer, A12].
  - "Toffoli gates solve the tetrahedron equations" (2405.16477) [P, TETRAEDER-L, dort S Abstract]: umkehrbare
    Gatter und Tetraedergleichung, ohne Entstehungsbefund.
  - Margolus bzw. Billardkugel-Rechner: [L], nicht abgerufen.

**Frage 6: Gegensweep (Literatur)**
- "Church-Turing sagt fuer die Physik nichts Pruefbares":
  - Geroch/Hartle halten ihr Kriterium fuer pruefbarer als "Eleganz", aber eine Verletzung waere "merely an
    inconvenience" (S. 17-18) [S].
  - Pour-El/Richards: Die Antwort haengt an der Norm [S Treffer].
  - Copeland/Shagrir: Gandys Klasse erschoepft die idealen physikalischen Maschinen nicht [S Treffer].
- Kritik an "Kausalinvarianz = Kovarianz":
  - Die schaerfste gelesene Kritik kommt aus Wolfram Research selbst (Bulletin) [S]; Aaronson 2002 steht schon in
    WOLFRAM-SCAN-L [P].
  - Ein Podcast-Titel "Causal invariance versus confluence with Jonathan Gorard" ist ungelesen [S Treffer, nur Titel].
- 24-Monats-Suche (A11): siehe Frage 4. Kein "widerlegt" vergeben.

## 4. Einordnung fuer Finns Netz [ES/H, Belege wie markiert]

### 4.1 Ist das Netz eine Gandy-Maschine?
- **Mit reellen Kantenlaengen: nein** [ES].
  - Gandy-Zustaende sind aus Teilen beschraenkter Groesse eindeutig zusammengesetzt [S Treffer].
  - Arrighi/Dowek nennen beschraenkte Informationsdichte als Postulat [S Treffer].
  - Eine reelle Zahl je Kante traegt unbeschraenkt viel Information.
- **Gerundet (endlich viele Symbole je Kante): wahrscheinlich ja** [ES].
  - Oertliche Kausalitaet: Zuege und Zeltstangen wirken auf beschraenkte Nachbarschaften.
  - Das Netz ist aus Tetraedern eindeutig zusammensetzbar.
  - Dann gilt Gandys Satz: nicht mehr als ein Turing-Rechner.
  - Ob man die exakte Bahn beliebig genau nachrechnen kann, haengt an der Glattheit (Pour-El/Richards: Supremumsnorm
    gegen Energienorm) [S Treffer].
- **Schwachstelle sind die Umklapp-Entscheidungen** [ES; L fuer die Saetze der berechenbaren Analysis].
  - Ob 5 Punkte kosphaerisch sind, ist ein Gleichheitstest reeller Zahlen. Der ist nicht entscheidbar, und
    berechenbare Funktionen sind stetig [L]. Ein Umklappzug ist eine unstetige Entscheidung.
  - In allgemeiner Lage stoert das nicht. Auf dem exakt symmetrischen Netz (Tetraeder-Oktaeder-Wabe) liegt aber jedes
    Oktaeder genau auf der Entartung [M].

### 4.2 Was heisst Church-Rosser fuer Umklapp- und Zeltzuege und fuer die Weg-Unabhaengigkeit?
- **Umklappzuege**, drei Regime [ES]:
  - (i) **Kinetisch** (Start Delaunay, kleine Schritte, allgemeine Lage): Die Normalform ist die eindeutige
    Delaunay-Zerlegung, also konfluent trivial [M].
  - (ii) **Grosse Schritte bzw. Start fern von Delaunay, 3D**: Monotones Umklappen kann ohne Delaunay-Ziel enden
    (Joe [S Treffer]). Normalformen sind dann nicht eindeutig.
  - (iii) **Exakt symmetrisch**: Die 6 Oktaederecken liegen auf einer Kugel, jede der 3 Diagonalen ist Delaunay [M].
    Konfluenz gilt nur modulo Diagonalwahl. Genau das ist der Flip-Flop aus PACHNER-TAKT-1 [P].
- **Zeltzuege**:
  - PACHNER-TAKT-1 hat die staerkste Form gemessen, den Ein-Schritt-Diamanten AB gegen BA [P]: flach 1e-15, gekruemmt
    D ~ eps^1 (a/L)^2,25.
  - Beide Reihenfolgen haben dieselben 111 Randkanten. D vergleicht Randimpulse bei gleichen Randlaengen, also zwei
    Hamilton-Funktionen derselben Randdaten [P]. D ist damit eichinvariant: Es misst Triangulierungsabhaengigkeit,
    keine verbliebene Eichung [ES].
  - Konfluenz ueber laengere Wege ist nicht getestet.
- **Weg-Unabhaengigkeit (erste Klasse)** [H, Analogie, in der Literatur nicht gefunden]:
  - Im Kontinuum vertauschen zwei oertliche Zeitzuege bis auf eine raeumliche Verschiebung (Dirac-Algebra mit
    Strukturfunktion).
  - Das entspricht "Church-Rosser modulo Umbenennung", wie Church/Rosser modulo Regel I.
  - Im Regge-Netz sind die Zeltzuege 4D-Verschiebungen der Ecken. Sie vertauschen flach exakt (abelsch, Hoehn [P]),
    mit Kruemmung nicht [P].
  - Kartenvorschlag K2 prueft, ob der Defekt genau ein 4D-Pachner-Defekt ist.
- **Bulletin-Lehre** [S, ES]:
  - Fuer Finns Netz muessen "gleiche Enddaten" (Konfluenz) und "gleiche Ursachenstruktur" (Kausalinvarianz) getrennt
    definiert werden. Das Netz terminiert nie; die Bulletin-Definition greift deshalb nicht direkt.

### 4.3 Was folgt fuer Topologieaenderung?
- Pachner-Zuege aendern die Topologie nicht [M, GRUNDGLEICHUNG-SKIZZE-v2 Abschn. 6].
- **3D-Raumscheiben** [S Treffer, Burton; ES]:
  - Welche Topologie vorliegt, ist entscheidbar; zwischen Triangulierungen derselben 3-Mannigfaltigkeit gibt es eine
    berechenbare Zugschranke.
  - Eine deterministische Entwicklung einer 3D-Scheibe, auch mit Topologiewechsel durch eine zusaetzliche Zugart (Geonen,
    Finns Spin-Frage), laeuft damit **nicht** in Markovs Hindernis.
- **4D-Summen** (Quantenfassung, Summe ueber Geschichten) [S]:
  - Bei fester, nicht erkennbarer Topologie greift Nabutovsky/Ben-Av; fuer S^4 ist es offen.
  - Ob T^4 bzw. T^3 x I erkennbar sind, habe ich nicht gesucht (offen).
- **Kurz** [ES]: Nicht die Topologieaenderung ist das Risiko, sondern der Schritt von 3D-Zustaenden zu Summen ueber
  4D-Triangulierungen.

### 4.4 Was koennen Lambda-Suppen beitragen, und wo bricht der Vergleich?
- **Beitrag:** Aus einfachen Regeln ohne Fitness entstehen Selbstberechner, abgeschlossene Organisationen und
  Replikatoren [S Treffer, S Abstract]. Das gilt auch massenerhaltend (Combinatory Chemistry) [S].
- **Bruch 1, Umkehrbarkeit:**
  - Alle gelesenen Suppen werfen weg: Reduktion ist einseitig, AlChemy entnimmt zufaellig [S, S Treffer].
  - Normalformen und Replikatoren sind Anziehungspunkte, und Anziehungspunkte braucht man nur ohne Volumenerhaltung im
    Phasenraum. Ein hamiltonsches Netz hat keine Attraktoren (Liouville) [L/M].
  - Umkehrbare Graphdynamik erhaelt zudem die Eckenzahl [S Abstract]. Ein umkehrbares Finn-Netz mit 1-4/4-1 braucht
    deshalb einen der gelockerten Rahmen von Arrighi u. a. (Inhalt nicht gelesen, R1).
- **Bruch 2, Energie:** AlChemy hat keine Energie; Combinatory Chemistry erhaelt Atome, nicht Energie [S].
- **Folge** [ES/H]: Im umkehrbaren, energieerhaltenden Netz waere die Entsprechung einer "selbsterhaltenden
  Organisation" eine erhaltene bzw. topologisch geschuetzte Struktur. Die Q-Baelle des Projekts sind das naechste
  Gegenstueck, kein Autokatalysezyklus.
- **Gegensweep-Befund G1** [P]: Das Projektnetz ist nur zwischen den Zuegen hamiltonsch.
  - TAKT-DYNAMIK-1: Lesart R verliert ueber 10 Perioden 2,4 bis 12,7 %, Lesart P gewinnt 15 bis 20 % (A = 1e-3).
  - Arm a ohne Zug driftet hoechstens 2e-8.
  - Lesart R streicht die wegfallende Kante und projiziert auf die neue Zwangsflaeche. Das ist ein Loeschschritt, das K
    des Netzes [ES].

### 4.5 Was ist im Projekt bekannt, was waere neu?
- **Bekannt [P]:** HKT-Weg-Unabhaengigkeit, PACHNER-TAKT-1-Kommutator, Gorards Kovarianzbehauptung, Wolfram-Valenz,
  Energiespruenge je Zug, Pachner-Zuege erhalten die Topologie.
- **Neu fuers Projekt [S]:**
  - Bulletin (Unabhaengigkeit, keine Physik).
  - Nabutovsky/Ben-Av (feste Topologie, 4D).
  - Church/Rosser Theorem 2 (ohne Wegwerfen ist die Reihenfolge fuer das Anhalten gleichgueltig).
  - Umkehrbare kausale Graphdynamik (Eckenzahl).
  - Combinatory Chemistry (Massenerhaltung).
  - Aguera-y-Arcas-Gegenbeispiel.
- **Neu als Hypothese [H], in den Suchen nicht gefunden:**
  - "Dirac-Algebra = Church-Rosser modulo raeumlicher Umbenennung".
  - "4-1-Zug und Lesart-R-Projektion als Loeschschritte (K)".
  - "Auf dem symmetrischen Netz fallen Nicht-Konfluenz und Nicht-Entscheidbarkeit zusammen".
  - "Nicht gefunden" heisst nicht "neu".

## 5. Kartenvorschlaege (hoechstens 2)

### K1 UEBERGABE-KONFLUENZ-1: Haengt der Zustand nach zwei faelligen Umklappzuegen von ihrer Reihenfolge ab, mit Feldern, in Form A gegen Form B?

- **Frage:** Zwei im selben Zeitschritt faellige 2-3- bzw. 3-2-Zuege X und Y mit ueberlappendem Traeger (gemeinsames
  Tetraeder bzw. gemeinsame Kante), Uebergabe in der Reihenfolge XY gegen YX:
  - Gleichen sich die Endzustaende (q, p, phi, pi, A, E)?
  - Getrennt nach Lesart R (Projektion) und P sowie nach Bewegungsform A (impulsseitig je Zelle) und B (Lund-Regge,
    GRUNDGLEICHUNG-SKIZZE-v2 Abschn. 2.3).
- **Warum ueber PACHNER-TAKT-1 hinaus:** Dort gab es nur Zeltzuege und reine Geometrie. Hier geht es um Umklappzuege,
  Felder bzw. Materie und den Loeschschritt.
  - Im Projekt ist die Reihenfolge der Uebergabe nicht getestet: grep "Reihenfolge|vertausch|kommut" in TAKT-DYNAMIK-1,
    HODGE-MASSE-1 und UMKLAPP-1 ohne Treffer zur Sache [P].
  - Im Code entscheidet bei endlichem Zeitschritt h eine Implementierungsreihenfolge, sobald mehrere Flaechen
    gleichzeitig nicht lokal Delaunay sind [ES].
- **Bau:**
  - Vorhandener Code aus TAKT-DYNAMIK-1 bzw. HODGE-MASSE-1, Glas-Netz.
  - Zwei benachbarte Flaechen durch kleine Eckverschiebung gleichzeitig nicht lokal Delaunay machen.
  - Uebergabe XY und YX, je mit und ohne Felder (Skalar-Amplitude 0, 1e-3, 1e-2).
  - Messgroessen: Delta_s = Abstand der Endzustaende je Sektor, relativ; Delta_H = |H_XY - H_YX| / H; Gauss-Rest.
  - Dazu: Anteil der Zeitschritte mit mindestens zwei faelligen Zuegen in einem vorhandenen Lauf (h = 0,5 gegen 0,25).
- **Ableitbarkeitsprobe:**
  - Vorab ableitbar [M]:
    - (a) Disjunkte Traeger vertauschen exakt.
    - (b) In allgemeiner Lage ist die kombinatorische Endzerlegung nach "umklappen bis Delaunay" in beiden
      Reihenfolgen dieselbe (eindeutige Delaunay-Zerlegung). Die Geometrie-Kombinatorik ist also nur Kontrolle.
    - (c) Ist die Uebergabe je Zug linear und invertierbar auf ihrem Traeger und vertauschen die beiden Abbildungen,
      dann ist Delta = 0. Ob sie vertauschen, folgt aus dem Code nicht ohne Rechnung.
  - Nicht ableitbar: Groesse und Skalierung von Delta_Feld mit Amplitude und Ueberlappungsart; ob R (Projektion) eine
    groessere Reihenfolgespur hinterlaesst als P; Unterschied Form A gegen B; Haeufigkeit doppelter Ereignisse je h.
  - Projekt-grep: siehe oben, keine Rechnung dazu.
  - Kann scheitern: ja, beide Richtungen.
- **Vorhersagen-Entwurf** (vor jeder Rechnung neu setzen, Leitung entscheidet):
  - UK0 (Kontrolle): disjunkte Zuege Delta < 1e-12; ohne Felder kombinatorisch gleiche Endzerlegung (90 %).
  - UK1: Lesart R, Felder 1e-3: Delta_Feld > 1e-6 relativ (60 %).
  - UK2: Delta_Feld waechst linear mit der Feldamplitude, Steigung 0,9 bis 1,1 (55 %).
  - UK3: Lesart R hat eine mindestens 10-mal groessere Reihenfolgespur als P (35 %).
  - UK4: Form A und Form B unterscheiden sich in Delta_p um mehr als Faktor 2 (40 %).
- **Kontrolle:** UK0; ausserdem Zeitumkehr-Probe: Laeuft die Bahn nach dem Zugpaar mit umgekehrten Impulsen zurueck,
  muss sie die Zuege in umgekehrter Reihenfolge wieder aufheben. Weicht sie ab, ist die Uebergabe nicht umkehrbar,
  unabhaengig von der Reihenfolge.
- **Laufzeit:** [ungemessene Schaetzung] Sekunden bis wenige Minuten, Kleintest-Spur.

### K2 ZELT-PACHNER-BRUECKE-1: Ist der Zeltzug-Kommutator aus PACHNER-TAKT-1 ein 4D-Pachner-Defekt?

- **Frage:** Welche 4D-Pachner-Zuege verbinden die Schichten AB und BA (Innenkante A'B gegen AB')? Ist D gleich der
  Aenderung der linearisierten Regge-Hamilton-Funktion unter genau diesen Zuegen?
  - Wenn ja, ist auf Finns Netz "Weg-Unabhaengigkeit der Zeltzuege" (HKT, Konfluenz) dasselbe wie die Invarianz unter
    diesen Zuegen (Dittrichs Triangulierungsunabhaengigkeit).
- **Bau:**
  - Kombinatorik der je 48 Simplizes (vorhandene Daten bzw. Code): Differenzmenge der Simplizes.
  - Grad der Kante A'B (Zahl der 4-Simplizes um sie).
  - Kuerzeste Zugfolge AB -> BA.
  - Fuer jeden Zug der Folge der Defekt der Hamilton-Funktion mit denselben gekruemmten Randdaten (eps = 1e-3,
    L/a = 4 bis 32); Vergleich der Summe mit D.
- **Ableitbarkeitsprobe:**
  - Vorab ableitbar [M]:
    - (a) Ein 3-3-Zug laesst die Kantenmenge seiner 6 Ecken unveraendert, er tauscht nur ein inneres Dreieck. AB und BA
      unterscheiden sich in einer Kante, also ist **kein einzelner 3-3-Zug** die Verbindung; noetig sind mindestens ein
      2-4- und ein 4-2-Zug.
    - (b) Unter 5-1 und 4-2 ist die Regge-Wirkung invariant [P, TETRAEDER-L nach Dittrich/Kaminski/Steinhaus, dort
      S Abstract]. Bestuende die Folge nur aus 2-4 und 4-2 mit lauter Loesungen, waere D = 0. Das widerspricht
      D ~ eps [P]. Also enthaelt die Folge entweder einen 3-3-Zug, oder die Invarianzaussage gilt hier nicht.
    - Beides ist bedingt auf die Lesart der DKS-Aussage, die ich nicht an der Quelle gelesen habe.
  - Nicht ableitbar: der Grad von A'B, die Folge selbst, ob D quantitativ gleich der Summe der Einzeldefekte ist, und der
    a/L-Exponent des Einzeldefekts.
  - Projekt-grep: PACHNER-TAKT-1 hat die Folge nicht bestimmt ("welche Pachner-Zuege AB und BA verbinden, habe ich nicht
    bestimmt") [P].
  - Kann scheitern: ja, beide Richtungen.
- **Vorhersagen-Entwurf:**
  - ZP0 (Kontrolle): flache Randdaten, Defekt jedes Zugs < 1e-13 relativ (90 %).
  - ZP1 (bedingt vorab ableitbar, siehe (b); eigentlich eine Pruefung der DKS-Lesart, keine Messung): Die kuerzeste
    Folge enthaelt mindestens einen 3-3-Zug (75 %).
  - ZP2: D gleich der Summe der Einzeldefekte auf 1 % (45 %).
  - ZP3: Der Einzeldefekt faellt im Bereich L/a = 4 bis 32 mit einem Exponenten 2,0 bis 2,5 (55 %).
- **Kontrolle:** isolierter 4-2-Zug mit Loesung: Defekt 0 (Gegenprobe zur DKS-Aussage); Lapse-Varianten L und G aus
  PACHNER-TAKT-1 muessen dieselbe Folge ergeben.
- **Laufzeit:** [ungemessene Schaetzung] Kombinatorik Sekunden; Defekte wie PACHNER-TAKT-1 (dort Minuten).
- **Kopplung:** Teilt Code und Netz mit PACHNER-TAKT-1, also ein Agent.

## 6. Regime, Moderatoren und Unterscheidungspunkte (Regel 1 und 2)

| Paar | Moderator | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|---|
| Konfluenz gegen Kausalinvarianz | Zustaende gegen Kausalgraphen | Piskunovs zwei terminierende Beispiele [S] | symbolisch ja; fuer Finns Netz erst nach eigener Definition (nicht terminierend) |
| Geroch/Hartle gegen Nabutovsky/Ben-Av | Summe ueber Topologien gegen feste, nicht erkennbare Topologie; Dimension | 4D, M0 = S0: keine berechenbare Zugschranke [S]; S^4 offen | mathematisch entschieden fuer S0; in 3D laufen sie nicht auseinander (beide unkritisch) |
| lambda-I gegen lambda-K | Wegwerfen erlaubt? | Ausdruck mit wegwerfbarem, nicht terminierendem Argument; im Netz ein 4-1-Zug ueber nicht reiner Eichung [H] | im Kalkuel ja; im Netz in silico (K1, Lesart R) |
| Pour-El/Richards gegen Weihrauch/Zhong | Norm bzw. Glattheit | Anfangsdaten mit nicht berechenbarem Gradienten [S Treffer] | **empirisch nicht unterscheidbar** (verlangt unendlich feine Daten) |
| Gandy-berechenbar gegen analog (Copeland/Shagrir) | endliche gegen unbeschraenkte Informationsdichte | nur bei unendlicher Genauigkeit | **empirisch nicht unterscheidbar** |
| Kinetisches gegen beliebiges Umklappen | Schrittweite h, Abstand zur Entartung | grosse h, Start fern von Delaunay, exakt symmetrisches Netz | ja, in silico (K1) |
| Theorie-Schranke gegen Praxis | Netzgroesse N | sehr grosse N (Schranke nicht rekursiv) [S]; kleine N ohne Barrieren (Titel hep-lat/9411070) | praktisch nicht |
| Reihenfolgespur Gitterartefakt gegen physikalisch | a/L | Kruemmungslaenge nahe der Zellgroesse | in der Natur nicht; in silico ja (PACHNER-TAKT-1, K2) |

**Regel 6 (Kopplung vor Bauteil):**
- Zu "die Reihenfolge veraendert das Ergebnis" fuehren mindestens vier Wege:
  - Kruemmung (PACHNER-TAKT-1) [P];
  - Loeschen (lambda-K, 4-1, Projektion) [S, P];
  - entartete Normalform (kosphaerische Oktaeder; Joe) [M, S Treffer];
  - ueberlappende Treffer (Piskunov) [S].
- Gemeinsame Groesse [ES]: Ueberlappung der Traeger zweier Zuege mal nicht vertauschende Aenderung der gemeinsamen
  Daten. Zuege mit disjunktem Traeger vertauschen in allen vier Faellen exakt.
- Messbar ist das als Abhaengigkeitsrelation plus Defekt je kritischem Paar ("critical pair lemma", Gorard S. 12 [S lokal];
  Knuth-Bendix [L]).

## 7. Erwartungsverstoesse, Negativliste, Selbstanzeigen

### 7.1 Erwartungsverstoesse (wichtigste zuerst; Protokoll in ARBEITSFELD.md)

1. **Bulletin (A1):**
   - Konfluenz und Kausalinvarianz sind fuer terminierende Systeme unabhaengig (Gegenbeispiele in beide Richtungen);
     "CausalInvariantQ" prueft Konfluenz; keine Physikaussage.
   - Das trifft den **Projektstand** (TAKT-UMBENENNUNG-L und WOLFRAM-SCAN-L fuehrten Gorards Notwendigkeit als Befund).
     Bei Gorard ist sie gesetzt, nicht bewiesen.
2. **Nabutovsky/Ben-Av (A6):** Nichtberechenbarkeit bei fester Topologie in 4D (S0; S^4 offen), ausdruecklich "essentially
   different" von Geroch/Hartle. LT3 Satz 2 und die vorab notierte Bedeutung fallen. Der Moderator ist die Dimension bzw.
   die Erkennbarkeit, nicht der Topologiewechsel.
3. **Church/Rosser Theorem 2 (A18):** Ohne Wegwerfen (lambda-I) erreicht jede Reduktionsfolge eine vorhandene
   Normalform in beschraenkt vielen Schritten. LT1 Satz 3 ist so an der Quelle nicht belegt. Neuer Moderator:
   Loeschen von Information.
4. **Umkehrbare kausale Graphdynamik (A12, A17):** Ein ganzes Programm behandelt Finns Frage "umkehrbar plus
   Ecken-Erzeugung/-Vernichtung", mit Bezug zu diskreter Quantengravitation und Fassung v4 vom Juli 2026.
5. **Gegensweep G1 (Projekt):** Die Netzdynamik ist nur zwischen den Zuegen umkehrbar und energieerhaltend. Die
   Karten-Aussage "[M] Unsere Netzdynamik ist hamiltonsch, also umkehrbar" gilt fuer den Code mit Zuegen nicht.
6. **Geroch/Hartle (A7):** viel vorsichtiger als LT3. Der Engpass sitzt in einer Rechenvorschrift (Doppelte
   streichen); sie nennen zwei Auswege und nennen die Folge "merely an inconvenience".
7. **Aguera y Arcas u. a. (A15):** "tend to arise" und ein Gegenbeispiel-Substrat; das Substrat ist ein Moderator.
8. **24 Monate (A11):** Gefunden ist eine Arbeit von 2026, die die physikalische Church-Turing-These aus QFT und
   Quantengravitation **staerkt** (2604.00182, nur Treffer). Erwartet hatte ich "nichts Pruefbares".
9. **Combinatory Chemistry (A10/A13):** Massenerhaltung mit spontaner Selbstvermehrung liegt naeher an LT7 Satz 2 als
   erwartet, ist aber nicht umkehrbar.

### 7.2 Negativliste (nach diesen Befunden NICHT sagen)

- "Konfluenz ist notwendig fuer Kausalinvarianz" bzw. "Kausalinvarianz = Konfluenz".
- "Das Wolfram-Bulletin verbindet Kausalinvarianz mit Kovarianz."
- "Bei fester Topologie gibt es kein Berechenbarkeitsproblem." Erlaubt: "In 3D nicht; in 4D fuer manche
  Mannigfaltigkeiten doch."
- "Geroch/Hartle haben gezeigt, dass Quantengravitation nicht berechenbar ist."
- "Church/Rosser zeigen, dass der Lambda-Kalkuel nicht stark normalisierend ist."
- "Finns Netz ist eine Gandy-Maschine." Erlaubt: "gerundet wahrscheinlich ja".
- "Finns Netzdynamik ist umkehrbar bzw. energieerhaltend." Erlaubt: "zwischen den Zuegen".
- "Es gibt keine Arbeit, die Verformungsalgebra und Konfluenz verbindet." Erlaubt: "in zwei Suchen nicht gefunden".
- "Dirac-Algebra = Church-Rosser modulo Umbenennung ist neu." Erlaubt: "Hypothese, nicht gefunden".
- "In jeder Programm-Suppe entstehen Selbstreplikatoren."
- "Umkehrbare Graphdynamik kann keine Ecken erzeugen." Erlaubt: "nur in gelockerten Rahmen".
- "In 3D bleibt Delaunay-Umklappen stecken." Erlaubt: "monotones Umklappen von beliebigem Start kann scheitern,
  inkrementell nicht".
- "PACHNER-TAKT-1 zeigt fehlende Konfluenz." Erlaubt: "zeigt einen Ein-Schritt-Diamant-Defekt; Konfluenz ueber laengere
  Wege nicht getestet".
- "D aus PACHNER-TAKT-1 ist ein Eichartefakt."
- Jede [S Treffer]-Aussage als [S] zitieren.

### 7.3 Selbstanzeigen

1. **Geschaetzte Zeiten:** Im ARBEITSFELD standen dreimal geschaetzte Uhrzeiten ("10:5x", "10:53", "10:56"). Sie sind
   durch gemessene ersetzt und dort als SELBSTANZEIGE markiert.
2. **Abruf 20 ohne Inhalt** durch eigenen Fehler (http statt https, curl ohne -L, HTTP 301). Gezaehlt, nicht
   wiederholt.
3. **Nummernsprung:** keine Nummer 14. Gezaehlt sind 20 Abrufe.
4. **Viele Aussagen nur [S Treffer]** (Suchmaschinen-Zusammenfassungen): Gandy, Copeland/Shagrir, Joe, Mijatovic,
   Burton, Pour-El/Richards, Weihrauch/Zhong, Fontana/Buss, 2604.00182, Arrighi 2016/2018 (Teile). Nach der Projektregel
   vor jedem Vertrag an der Quelle lesen.
5. **Nicht an der Quelle:**
   - Gandy 1980, Deutsch 1985, Tao 2016, Cardona u. a. 2021, Margolus, DKS 2014 (nur ueber TETRAEDER-L).
   - Church/Rosser S. 482 (fehlt in der Kopie).
6. **Church/Rosser:** JSTOR-Scan, als Bild ueber das Read-Werkzeug gelesen (keine OCR). Lokale Kopie nur zur eigenen
   Pruefung; JSTOR-Bedingungen: "personal, non-commercial use".
7. **Kein frischer Leser**; nur eigener Rueckwaertsdurchgang.
8. **Werkzeuge lokal:** curl, pdftotext, grep, sed, head, wc, tr, cut, ls, mkdir, file, cat mit gequotetem Heredoc, date.
   Kein python, awk oder perl. Keine Rechnung.
9. **Versiegeltes:** Projekt-greps mit den vorgeschriebenen Ausschluessen; keine solche Datei geoeffnet.

## 8. Anhang: Kalibrierung, Gegensweep, offene Fragen, Quellen

### 8.1 Kalibrierung
- **(a) Gemessen bzw. bewiesen:**
  - Saetze an der Quelle: Church/Rosser Theorem 1 und 2; Nabutovsky/Ben-Av Prop. 1 und 2; Piskunovs Gegenbeispiele
    (symbolisch, mit Code im Bulletin).
  - Projektzahlen [P]: D ~ eps (a/L)^2,25; Energiespruenge je Zug.
  - Keine Messdaten.
- **(b) Nuetzlich verdichtet [ES]:**
  - Moderator "Wegwerfen" (lambda-I gegen K).
  - "Grenze 3D gegen 4D statt fester gegen wechselnder Topologie".
  - "D ist eichinvariant, misst Triangulierungsabhaengigkeit".
  - Vier Wege zur Reihenfolgeabhaengigkeit mit gemeinsamer Groesse "Traegerueberlappung".
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Dirac-Algebra = Church-Rosser modulo Umbenennung" (Analogie, zwei Suchen ohne Fund).
  - "4-1 = K" (Bild, nicht gerechnet).
  - "symmetrisches Netz = Nicht-Konfluenz plus Nicht-Entscheidbarkeit" (Nulltest-Satz nur [L]).
- **Warnzeichen:** Meine Sicherheit, dass Konfluenz die richtige Sprache fuer HKT ist, stieg mit jedem passenden
  Fund. Zugleich zerfiel die Frage in drei verschiedene Begriffe: Zustands-Konfluenz, Kausalinvarianz und
  beschrifteter Diamant. Belegt ist nur, dass die ersten beiden verschieden sind.

### 8.2 Gegensweep (Regel 4; Tabelle G1 bis G7 in ARBEITSFELD.md Abschn. 3)

| Selbstverstaendlichkeit | geprueft? | Ergebnis |
|---|---|---|
| G1 Netzdynamik umkehrbar | ja [P] | nur zwischen Zuegen; Lesart R loescht |
| G2 Delaunay hat eine eindeutige Normalform | ja [M] | nicht auf dem symmetrischen Netz (Oktaeder kosphaerisch) |
| G3 Kausalinvarianz ist fuer Finns Netz definiert | ja [S] | nur fuer terminierende Systeme definiert |
| G4 Church-Rosser ist der richtige Begriff fuer HKT | teils [ES] | genauer: beschrifteter Diamant bzw. Teilkommutation |
| G5 D koennte Eichung sein | ja [P/ES] | nein, gleiche Randdaten, eichinvariant |
| G6 Flip-Entscheidung berechenbar | nein [L] | Nulltest auf Reellen; offen |
| G7 Gandy fuer reellwertige Netze | Treffer | beschraenkte Informationsdichte verlangt |

### 8.3 Offene Fragen
1. Welche drei gelockerten Rahmen erlauben umkehrbare Ecken-Erzeugung (Arrighi u. a.)? Passt einer zu 1-4/4-1 mit
   Regge-Eichung?
2. Welche Pachner-Folge verbindet AB und BA, und ist D ihr Defekt? (K2)
3. Ist die Umklapp-Uebergabe reihenfolgeunabhaengig, mit Feldern, in Form A und B? (K1)
4. Sind T^4 bzw. T^3 x I algorithmisch erkennbar (Bedeutung fuer 4D-Summen auf Finns Torus)?
5. Gibt es eine Konfluenz- bzw. Kausalinvarianz-Definition fuer nicht terminierende, reellwertige Netze (Bulletin #487)?
6. Raeumt Gorard die Unabhaengigkeit inzwischen ein (Podcast-Titel)?

### 8.4 Quellenliste (Abrufe 2026-10-05, CEST per date; Volltexte in quellen/)

| Nr | Autor, Jahr, Titel | URL | Lesestand |
|---|---|---|---|
| A1 | Piskunov, M. (16.11.2020): Confluence and Causal Invariance (Wolfram Physics Bulletin), Archiv-Schnappschuss 24.10.2021 | https://web.archive.org/web/20211024021917/https://www.wolframphysics.org/bulletins/2020/11/confluence-and-causal-invariance/ | [S] voll, 10:52:30 |
| A2, A6 | Nabutovsky, A.; Ben-Av, R. (1993): Noncomputability arising in dynamical triangulation model of four-dimensional quantum gravity. Commun. Math. Phys. 157, 93-98; arXiv hep-lat/9208014 | https://arxiv.org/abs/hep-lat/9208014 | [S] voll, 10:55:35 |
| A3, A7 | Geroch, R.; Hartle, J. B. (1986): Computability and physical theories. Found. Phys. 16, 533-550; arXiv:1806.09237 | https://arxiv.org/abs/1806.09237 | [S] Abschn. I, III, IV (S. 1-2, 10-18), 10:55:37 |
| A18 | Church, A.; Rosser, J. B. (1936): Some properties of conversion. Trans. AMS 39(3), 472-482 | https://www.cs.cmu.edu/~crary/819-f09/ChurchRosser36.pdf | [S] S. 472-473, 475-481, 11:00:09 |
| A13 | Kruszewski, G.; Mikolov, T. (2020): Combinatory Chemistry: Towards a Simple Model of Emergent Evolution, arXiv:2003.07916v2 | https://arxiv.org/abs/2003.07916 | [S] S. 2-3, 10:58:38 |
| A15 | Aguera y Arcas, B.; Alakuijala, J.; Evans, J.; Laurie, B.; Mordvintsev, A.; Niklasson, E.; Randazzo, E.; Versari, L. (2024): Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction, arXiv:2406.19108 | https://arxiv.org/abs/2406.19108 | [S Abstract] |
| A17 | Arrighi, P.; Durbec, A.; Emmanuel, A. (2018, v4 10.07.2026): Size-varying reversible causal graph dynamics, arXiv:1805.10330 | https://arxiv.org/abs/1805.10330 | [S Abstract] |
| A12 | Arrighi, P.; Martiel, S.; Perdrix, S.: Reversible Causal Graph Dynamics, arXiv:1502.04368; Arrighi, P.; Dowek, G.: Causal graph dynamics, arXiv:1202.1098; "Reversibility vs local creation/destruction" (HAL 01800661) | https://arxiv.org/abs/1502.04368 | [S Treffer] |
| A5 | Gandy, R. (1980): Church's thesis and principles for mechanisms (Kleene Symposium); Copeland, B. J.; Shagrir, O. (2007): Physical computation: How general are Gandy's principles for mechanisms? (Minds and Machines) | https://oronshagrir.huji.ac.il/publications/physical-computation-how-general-are-gandys-principles-mechanisms | [S Treffer] |
| A8 | Santos, F.: Geometric bistellar flips (arXiv math/0601746); Edelsbrunner, H.; Muecke, E.: Three-dimensional alpha shapes (arXiv math/9410208); darin Joe 1989/1991 | https://arxiv.org/abs/math/0601746 | [S Treffer] |
| A9 | Mijatovic, A. (2003): Simplifying triangulations of S^3. Pacific J. Math. 208; Burton, B. A.: Simplification paths in the Pachner graphs (arXiv 1110.6080) | https://arxiv.org/abs/math/0008107 ; https://arxiv.org/abs/1110.6080 | [S Treffer] |
| A10, A16 | Fontana, W.; Buss, L. W. (1994) (AlChemy) ueber: "Self-Organization in Computation & Chemistry: Return to AlChemy" (arXiv 2408.12137); "Prebiotic Functional Programs" (arXiv 2509.03534); Kruszewski/Mikolov 2021 (arXiv 2103.08245) | https://arxiv.org/abs/2408.12137 | [S Treffer]; Fontana/Buss nicht selbst gelesen |
| A11 | (Autoren nicht gesehen) (2026): Limits to Computational Acceleration Imposed by Quantum Field Theory and Quantum Gravity, arXiv:2604.00182; Arrighi, P.; Dowek, G.: The physical Church-Turing thesis and the principles of quantum theory, arXiv:1102.1612 | https://arxiv.org/abs/2604.00182 | [S Treffer] |
| A20 | Pour-El, M. B.; Richards, J. I. (1981): The wave equation with computable initial data such that its unique solution is not computable; Weihrauch, K.; Zhong, N. (2002): Is wave propagation computable or can wave computers beat the Turing machine? | https://bibbase.org/network/publication/pourel-richards-thewaveequationwithcomputableinitialdatasuchthatitsuniquesolutionisnotcomputable-1981 | [S Treffer] |
| A4, A19 | Suchen Verformungsalgebra x Konfluenz (Treffer u. a. Bonzom/Dittrich arXiv:1304.5983; Gorard arXiv:2004.14810, 2011.12174; Podcast "Causal invariance versus confluence with Jonathan Gorard") | - | [S Treffer] |
| A21 | arXiv-API-Abfrage Berechenbarkeit x Quantengravitation | http://export.arxiv.org/api/query | HTTP 301, kein Inhalt |
| lokal | Gorard, J. (2020): Some Relativistic and Gravitational Properties of the Wolfram Model (wolfram-scan-l/quellen/A35) | https://arxiv.org/abs/2004.14810 | [S lokal] S. 7-12 |
| Projekt | TAKT-UMBENENNUNG-L, PACHNER-TAKT-1, WOLFRAM-SCAN-L, TETRAEDER-L, RUNDE-22 geometrie-stand, GRUNDGLEICHUNG-SKIZZE-v2, RAUM-GAS-L (Quellen F17, F20), TAKT-DYNAMIK-1, HODGE-MASSE-1 | lokal | [P] |

## 9. Einfach gesagt

Der Lambda-Kalkuel ist eine Rechenregel. Der Satz von Church und Rosser sagt: Egal in welcher Reihenfolge man
vereinfacht, man kommt zum selben Ergebnis, und wenn nie etwas weggeworfen wird, haengt nicht einmal das Anhalten von
der Reihenfolge ab. Fuer Finns Netz heisst die Frage dann: Ist es egal, welche Ecke zuerst tickt oder welcher Tetraeder
zuerst umklappt? Bisher gilt: auf flachem Netz ja, mit Kruemmung nur ungefaehr, und auf dem perfekt symmetrischen Netz
gibt es mehrere gleich gute Ergebnisse. Ein solches Netz kann auch nicht mehr berechnen als ein normaler Computer,
solange man die Laengen rundet; schwierig wird es erst, wenn man ueber alle moeglichen vierdimensionalen Netze
summieren will, und das fuer manche Raeume sogar ohne Topologiewechsel.

## Zeitbox

- Start 10:48:34 CEST, Abrufe 10:52:30 bis 11:02:46, Dossier ab 11:08:16 CEST (date).
- Abgabe 2026-10-05 11:14:46 CEST (date), nach eigenem Rueckwaertsdurchgang; innerhalb der 90 min. Kein frischer Leser.
