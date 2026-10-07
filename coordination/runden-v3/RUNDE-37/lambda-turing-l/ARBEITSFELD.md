# LAMBDA-TURING-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu lesen)

- feldforscher fuer Leitung claude-primary. Start 2026-10-05 10:48:34 CEST (date). Zeitbox 90 min, Abrufbudget 20.
- Kennzeichen: [S] an der Quelle gelesen (Fundstelle), [S Abstract], [S lokal] Projektkopie hier gelesen,
  [L] Gedaechtnis ungeprueft, [P] Projektbefund, [M] Mathematik, [ES] Schreibtisch, [H] Hypothese.
- Gestrichenes wird ~~durchgestrichen~~, nicht geloescht. Offene Rueckfragen stehen in Abschnitt 6 und wandern mit.

## 0. Gelesene Projektdateien (ohne Abrufbudget)

- KARTE.md (LT1 bis LT7, Fragen 1 bis 6) vollstaendig.
- takt-umbenennung-l/DOSSIER.md vollstaendig: HKT [S sek.], E6 (Bulletin) dreimal nicht abrufbar; Gorard 2020 S. 9
  "confluence is a necessary condition for ... causal invariance" [S lokal dort]; TI S. 137 "path independence" mit
  Ref. [55] Church/Rosser 1936; grep HKT in Wolfram-Texten 0 Treffer.
- pachner-takt-1/ERGEBNIS.md vollstaendig: Kommutator D zweier Zeltzuege; flach 1e-15; gekruemmt D ~ eps^1
  (Steigung 0,998), (a/L)^2,25; Wirkungsdifferenz ~ eps^2; globaler Takt hebt nichts auf (D(G)/D(L) 1,39 bis 1,51).
  Reiner Diagonal-Flip-Flop auf festen Ecken unmoeglich [M]; Oktaederdiagonalen im fcc-Netz.
- wolfram-scan-l/DOSSIER.md vollstaendig: Bulletin 404 bzw. Host unbekannt; Valenz beschraenkt; Lorentz nur vergroebert.
- RUNDE-22/geometrie-stand/ERGEBNIS.md, Stellen zu Unentscheidbarkeit: nur [L?] (Cubitt/Perez-Garcia/Wolf 2015;
  Bausch u. a. 2018/20), EV7 "Dimension kein Moderator".
- RUNDE-48/GRUNDGLEICHUNG-SKIZZE-v2.md: 2.3 (Form A linear in N, Form B nicht linear in N, nur bei globalem Takt);
  4 (ungefixtes Eichmodell, Algebra offen); 6 (Pachner-Zuege aendern Topologie nicht [M]).
- raum-gas-l/DOSSIER.md Z. 50-100: NS-Blow-up mit Kraft (OpenAI-Manuskript 08.09.2026), Folgearbeiten Clay (C)/(D).
- Projekt-grep (mit Ausschluessen) nach Gandy, Geroch, Nabutovsky, Pour-El, Fontana, AlChemy, Aguera, Margolus,
  Lawson, Mijatovic, Church-Turing: **0 Treffer in Projekt-Markdown** ausser Wolfram-Kopien und Hartle (andere Arbeiten:
  Hartle/Miller/Williams 1997, Hartle-Hawking). Lokale Gorard-Kopie A35 hat einen eigenen Abschnitt 2.2 "Abstract
  Rewriting, the Church-Rosser Property and Causal Invariance" (Z. 346 ff.) -> lokal lesen, ohne Budget.

## 1. Abrufplan (20 hoechstens; nach Informationsgehalt)

| Prioritaet | Ziel | Grund |
|---|---|---|
| 1 | LT5 Bulletin: web.archive.org, dann eine Suche nach Spiegel | dreimal gescheitert; hoechstens 2 Abrufe |
| 2 | LT3 Geroch/Hartle; Nabutovsky/Ben-Av (CMP, Project Euclid frei?) | moeglicher Verstoss "feste Topologie" |
| 3 | LT6 Suche Verformungsalgebra + Konfluenz/Kausalinvarianz | 40 %, Front |
| 4 | LT7 Suche umkehrbare/massenerhaltende Kunstchemie; Aguera y Arcas 2024 | 55 % |
| 5 | LT2 Gandy-Prinzipien + Kritik (Copeland/Shagrir 2007?) | Einordnung Gandy-Maschine |
| 6 | LT4 Joe 1989/1991, Mijatovic 2003, kinetisches Delaunay | Ersetzungssystem Umklappen |
| 7 | 24-Monats-Suche physikalische Church-Turing-These / Quantengravitation | Regel 7 |
| 8 | Pour-El/Richards gegen Weihrauch/Zhong | Regime-Beispiel (Norm) |
| 9 | LT1 Kontrolle (SEP Lambda-Kalkuel) | 90 %, nur eine Zeile, falls bestaetigt |
| Rest | Verstoesse nachverfolgen | Budget auf Verstoesse |

## 2. Abrufprotokoll (Erwartung vor Abruf, Ergebnis, Verstoss ja/nein)

### L0 (lokal, ohne Budget): Gorard 2020 "Some Relativistic and Gravitational Properties", Abschn. 2.2
- Erwartung vor L0 (geschrieben vor dem Lesen um 10:52:08, date): Gorard definiert Konfluenz (Church-Rosser) als Zusammenfuehrbarkeit von
  Zustaenden, Kausalinvarianz als Isomorphie der Kausalgraphen ueber alle Aktualisierungsreihenfolgen, und behauptet
  "Konfluenz notwendig fuer Kausalinvarianz" (so im Projekt zitiert, S. 9). Keine Erwaehnung der Verformungsalgebra.
- Ergebnis L0 (10:52:08, A35 Z. 336-640): **bestaetigt**, eine Zeile: Def. 7/8 Konfluenz = Church-Rosser fuer Objekte
  (Zustaende); Def. 9 Kausalinvarianz = Kausalgraphen aller Reihenfolgen "all, eventually, isomorphic"; "confluence is a
  necessary condition" wird **gesetzt** ("We can formalize this notion by stating that ..."), danach "Having shown that
  ..."; ein Beweis steht im Abschnitt nicht [S lokal, S. 9-12]. Schwaechungen (lokal, semi) und Staerkungen (Diamant,
  stark) Gl. 9-12; Church/Rosser 1936 als Beweis der globalen Konfluenz der Beta-Reduktion zitiert (S. 12, Ref. [20]).
  Nebenbefund [ES]: Konfluenz ist eine Aussage ueber Zustaende, Kausalinvarianz ueber Kausalgraphen; die Notwendigkeit
  ist im gelesenen Text nicht bewiesen -> genau das ist die Pruefstelle fuer das Bulletin (LT5).

### A1: Bulletin ueber web.archive.org (1. von hoechstens 2 Bulletin-Abrufen)
- Erwartung vor Abruf 1 (geschrieben vor dem Abruf um 10:52:30, date; SELBSTANZEIGE: hier stand zuerst die geschaetzte Zeit "10:53"): Es gibt einen Archiv-Schnappschuss 2020/21 (60 %). Inhalt dann: Piskunov trennt
  Konfluenz (Zustaende zusammenfuehrbar) von Kausalinvarianz (Kausalgraphen isomorph) und zeigt mit Beispielen, dass
  **keine** die andere impliziert. Das wuerde Gorards gesetzte Notwendigkeit (L0) brechen. Kovarianz nur ueber
  Kausalinvarianz.
- Ergebnis A1 (10:52:30, curl mit Browser-UA, HTTP 200, Schnappschuss 2021-10-24; quellen/A1-bulletin-archiv.txt):
  **E6 nach drei Fehlschlaegen gelesen.** Piskunov, M. (16.11.2020), Z. 36-120 der Textkopie [S]:
  - Definitionen: "causal invariant if and only if the causal graphs for singleway evolutions with any possible event
    ordering functions are isomorphic"; "only meaningful for terminating systems"; "confluent if and only if any pair of
    partial singleway evolutions starting from a particular state can be continued in such a way as to reach isomorphic
    final states".
  - Kernsatz: "causal invariance is not equivalent to confluence, neither of them implies the other".
  - Gegenbeispiel 1 (konfluent, nicht kausalinvariant): {{1},{1,2}} -> {{1,2},{2}}; Reihenfolgen "OldestEdge" gegen
    "NewestEdge" geben nicht isomorphe Kausalgraphen.
  - Gegenbeispiel 2 (kausalinvariant, nicht konfluent): {{1,2},{2,1}} -> {{1}}; zwei Ereignisse, Kausalgraph je ein
    Knoten ohne Kante, Endzustaende {{1},{1}} gegen {{1},{2}} nicht isomorph.
  - Werkzeugbefund: "the "CausalInvariantQ" property of MultiwaySystem checks for confluence despite its name".
  - Physik: "We will not make any comments in this note about the physics claims made above."
  - Offen laut Bulletin: Definition der Kausalinvarianz fuer nicht terminierende Modelle (#487); Kausalmengen-
    Wachstumsmodelle als Klasse, in der Graph- und Zustandsisomorphie per Konstruktion zusammenfallen.
- **Verstoss: ja (stark, gegen Projektstand).** Meine Erwartung "keine impliziert die andere" traf ein; verletzt ist der
  Projektstand: TAKT-UMBENENNUNG-L und WOLFRAM-SCAN-L fuehren Gorards "confluence is a necessary condition" als Befund.
  Das Bulletin (Wolfram Research selbst) widerlegt es fuer terminierende Systeme mit einem Gegenbeispiel; fuer nicht
  terminierende ist Kausalinvarianz dort nicht einmal definiert. Und: Das Bulletin verbindet **keine** der beiden
  Eigenschaften mit Kovarianz (gegen LT5, zweiter Teil).
  - Korrigierte Erwartung: Fuer Finns Netz muss man Konfluenz (gleiche Endzustaende) und Kausalinvarianz (gleiche
    Kausalstruktur) getrennt pruefen; die eine folgt nicht aus der anderen.
  - [ES] HKTs Weg-Unabhaengigkeit vergleicht Enddaten auf derselben Endflaeche, ist also der Konfluenz (Zustaende)
    naeher als der Kausalinvarianz (Graphen). PACHNER-TAKT-1 hat mit AB gegen BA die staerkste Form gemessen
    (Diamant-Eigenschaft, je ein Schritt), nicht Konfluenz allgemein.
  - Moderator (Regel 1): terminierend gegen nicht terminierend; Gorards Aussage ist asymptotisch ("eventually"), das
    Bulletin terminierend. Gorards "Notwendigkeit" ist aber nirgends bewiesen (L0), also keine Gegenposition mit Beleg.
- Bulletin-Budget: 1 von 2 verbraucht, Ziel erreicht; kein zweiter Bulletin-Abruf.

### A2 bis A5 (parallel; Erwartungen vor dem Start geschrieben, Suchen fertig vor 10:54:58, date; SELBSTANZEIGE: hier stand zuerst die geschaetzte Zeit "10:56")
- **Erwartung vor Abruf 2** (Suche Nabutovsky/Ben-Av 1993): Abstract sagt: Fuer eine gegebene kompakte 4-Mannigfaltigkeit M
  (also bei **fester** Topologie) gibt es keinen Algorithmus, der alle Triangulierungen mit <= N Simplizes aufzaehlt;
  dazu rekursionstheoretische Grenzen fuer Naeherungen der DT-Summe. Das wuerde LT3 Satz 2 brechen (60 %).
- **Erwartung vor Abruf 3** (Suche Geroch/Hartle 1986): Sie diskutieren die Summe ueber 4-Geometrien, Markovs
  Unentscheidbarkeit, fuehren "messbare" (nicht berechenbare, aber naeherungsweise bestimmbare) Zahlen ein; Schluss:
  eine Theorie kann annehmbar sein, auch wenn ihre Vorhersagen nicht berechenbar sind (LT3 "kann nicht berechenbar
  sein" dann zu stark, 50 %).
- **Erwartung vor Abruf 4** (Suche Verformungsalgebra + Konfluenz/Kausalinvarianz): keine Arbeit, die Dirac/HKT
  ausdruecklich mit Church-Rosser bzw. Kausalinvarianz eines Ersetzungssystems verbindet (60 %); hoechstens
  Gorard-Formeln "discrete general covariance" ohne HKT.
- **Erwartung vor Abruf 5** (Suche Gandy-Prinzipien + Kritik): Gandys Satz: Maschinen nach Prinzipien I-IV (Form der
  Beschreibung, begrenzte Hierarchie, eindeutige Wiederzusammensetzung, oertliche Kausalitaet) berechnen nur
  Turing-berechenbare Funktionen; diskrete Zustaende (erblich endliche Mengen) vorausgesetzt; Kritik (Copeland/Shagrir
  2007): Prinzipien zu eng fuer allgemeine Physik.
- Ergebnis A2 (Suche, nur Treffertext [S Treffer]): Titel, CMP 157, 93-98, arXiv hep-lat/9208014. Treffertext: kein
  Algorithmus, der "for any given N and a given compact four-dimensional manifold M" alle Triangulierungen von M mit
  hoechstens N Simplizes konstruiert; dazu rekursionstheoretische Grenzen fuer Naeherungen. **Quantoren unklar**
  (fuer jedes M? fuer ein bestimmtes M? fuer S^4?). Nebenfund: "Absence of barriers in dynamical triangulation"
  (hep-lat/9411070) als moegliche Gegenposition (Regel 1: Theorie gegen numerische Praxis). -> Volltext noetig (A6).
  Verstoss: vorerst nein, Quantoren offen.
- Ergebnis A3 (Suche [S Treffer]): Geroch/Hartle, Found. Phys. 16, 533-550 (1986), arXiv:1806.09237. "physically
  measurable numbers predicted by the theory are computable"; Quantengravitation geschlossener Kosmologien als
  Funktional ueber Geometrien auf kompakten 4-Mannigfaltigkeiten; "indications that there may exist no such
  algorithms". **Vorsichtiger als LT3** ("indications", "may"). "Messbare Zahlen" stehen im Treffertext nicht. -> A7.
- Ergebnis A4 (Suche [S Treffer]): keine Arbeit, die die Verformungsalgebra ausdruecklich mit Konfluenz bzw.
  Kausalinvarianz verbindet; Treffer nur Wolfram-Texte (2011.12174, 2303.07282, ZX 2010.02752) und Bonzom/Dittrich
  1304.5983 getrennt. Ein Treffertext setzt "Causal invariance (confluence)" gleich (Quelle unklar, vermutlich
  Sekundaertext). Erwartung bestaetigt (eine Zeile). Eine Suche reicht fuer "nicht belegt", nicht fuer "gibt es nicht".
- Ergebnis A5 (Suche [S Treffer]): Prinzip III "unique reassembly", Prinzip IV "local causality": "F(x) is assembled
  from bounded (and possibly overlapping) parts of x"; IV abstrahiert laut Gandy zwei Voraussetzungen: "a lower bound
  on the linear dimensions of every atomic part of the device and ... an upper bound (the velocity of light) on the
  speed of propagation of changes". Copeland/Shagrir (2007): "interesting examples of (ideal) physical machines that
  fall outside the class of Gandy machines and compute functions that are not Turing-machine computable". Erwartung
  bestaetigt (eine Zeile). Neu fuer die Einordnung [ES]: Prinzip III/IV verlangen Teile **beschraenkter Groesse** und
  einen **festen Mindestmassstab**; Finns Netz mit reellen Kantenlaengen ist ohne Rundung keine Gandy-Maschine.
- Lokale Pruefung (ohne Budget, 10:54:58): wolfram-scan-l/quellen/A49 nennt "confluent up to isomorphism" (Hypergraph-
  Dominanzregeln) und "associativity as a confluence property"; nichts zur Verformungsalgebra.

### A6, A7 (Volltexte, Erwartungen geschrieben 10:55:13 date, vor dem Abruf)
- **Erwartung vor Abruf 6** (Nabutovsky/Ben-Av Volltext hep-lat/9208014): Der Satz gilt fuer **bestimmte** kompakte
  4-Mannigfaltigkeiten M (solche mit unentscheidbarem Erkennungsproblem, ueber Markov), nicht nachweislich fuer S^4;
  Beweisweg ueber nicht berechenbar wachsende Zahl von Zuegen ("barriers") zwischen Triangulierungen. Damit faellt
  LT3 Satz 2 ("bei fester Topologie entfaellt das Argument") fuer manche M, offen fuer S^4 und T^4 (55 %).
- **Erwartung vor Abruf 7** (Geroch/Hartle Volltext 1806.09237): Argument ueber Markov: 4-Mannigfaltigkeiten nicht
  aufzaehlbar bzw. nicht klassifizierbar; Summe ueber Topologien daher vermutlich nicht berechenbar; sie schlagen eine
  Ersatzbedingung vor (Vorhersagen naeherungsweise aus Messungen bestimmbar); fixe Topologie behandeln sie nicht
  eigens (50 %).
- Ergebnis A6 (10:55:35, curl arXiv-PDF, pdftotext; quellen/A6-...txt): Nabutovsky/Ben-Av, arXiv hep-lat/9208014v1
  (18.08.1992), S. 1-6 [S]:
  - Begriff "computational ergodicity": rekursive Funktion r mit hoechstens r(N) Zuegen zwischen je zwei
    Triangulierungen mit <= N Simplizes (S. 2-3).
  - Proposition 1: Fuer eine algorithmisch nicht erkennbare PL-Mannigfaltigkeit M0 gibt es **keine** endliche Zugmenge
    mit dieser Eigenschaft (S. 3). Beispiel nach Markov/Fomenko: S0 = 4-Sphaere mit 46 angehaengten Henkeln vom Index 2.
    Fuer S^4 offen: "if S^4 cannot be effectively recognized ..., then there is no computationally ergodic finite set
    of elementary moves on the set of triangulations of S^4" (S. 4).
  - Ergodizitaet selbst bleibt: die DT-Zuege sind ergodisch ([GV]); gebrochen ist nur die berechenbare Schranke.
  - Proposition 2: s(N) (Zahl der Triangulierungen von M0 mit <= N Simplizes) ist nicht rekursiv; ebenso die
    Zustandssumme (2) im Grenzfall Delta lambda_4 = unendlich (S. 5).
  - Erwartung: Rechenzeit fuer Integrale auf Genauigkeit eps waechst "non-recursively fast with [1/eps]" (S. 4),
    "if the integrated function is of a special form this can be not the case".
  - **Woertlich zu LT3:** "In this paper we discuss a Markov process for one fixed topological type of manifolds. Thus,
    the absence of computability discussed in the present paper is essentially different from the result of Geroch
    and Hartle." (S. 6)
- **Verstoss: ja (stark).** LT3 Satz 2 und die Vorab-Bedeutung ("Solange die Zuege die Topologie nicht aendern, gilt
  das Argument nicht") gelten nur fuer Geroch/Hartles eigenes Argument. Bei fester Topologie gibt es ein zweites,
  anderes Hindernis: Die Zuege verbinden alles, aber nicht in berechenbar beschraenkter Zahl. Moderator: Erkennbarkeit
  der Mannigfaltigkeit, damit die Dimension (S^n, n >= 5 nicht erkennbar nach Novikov, S. 3; 4D: S0 nicht, S^4 offen;
  3D: zu pruefen, LT4/Mijatovic).
- Ergebnis A7 (10:55:37, curl arXiv-PDF; quellen/A7-...txt): Geroch/Hartle, arXiv:1806.09237 (Neusatz 2018 des
  Aufsatzes von 1986), Abschn. III-IV, S. 15-18 [S]:
  - "Measurable": Zahl w, fuer die es endliche Anweisungen an einen Techniker gibt, die eine rationale Zahl innerhalb
    eps von w liefern (Analogrechnung); jede berechenbare Zahl ist messbar (S. 10-13, Z. 353-456 der Kopie; Seiten per Seitenvorschub gezaehlt).
  - Regge-Lesart der Summe: feste simpliziale 4-Mannigfaltigkeit mit n Ecken, ueber Kantenlaengen integrieren, dann
    ueber alle Mannigfaltigkeiten mit n Ecken summieren, n -> unendlich (S. 15-16).
  - Engpass ist die **Beseitigung von Doppelzaehlungen**: "whether two simplicial 4-manifolds are topologically
    identical is undecidable" (S. 16); "whether a simplicial complex is a manifold is decidable in dimension four, but
    undecidable in higher dimensions" ("It appears likely", S. 16).
  - Abschwaechung: "All this is not to say that quantum gravity will admit measurable numbers that are not computable";
    Grenzwert kann berechenbar sein; Ausweg "duplications of 4-manifolds are not to be excluded in the sums" (S. 16-17).
  - Schluss: "a serious candidate for a physical theory for whose application there is no algorithm" (S. 17); Folgen
    "merely an inconvenience - far from a disaster for physics" (S. 18).
- **Verstoss: ja (mittel).** Erwartung "Markov -> nicht klassifizierbar -> Summe vermutlich nicht berechenbar" traf
  nur abgeschwaecht ein: Das Hindernis sitzt in **einer** Rechenvorschrift (Doppelte streichen), nicht in der Summe;
  GH nennen selbst zwei Auswege. LT3 Satz 1 in der Lesart "kann nicht berechenbar sein = ist moeglicherweise nicht
  berechenbar" eingetroffen, in der Lesart "kann nicht berechenbar sein = ist sicher nicht berechenbar" nicht.
  - [ES] Ironie fuer LT3: GHs eigenes Argument (Duplikate erkennen) greift bei fester, nicht erkennbarer Topologie
    ebenfalls, denn auch dort muss man Triangulierungen von M0 aufzaehlen (NB/BA Prop. 2 ist genau das).

### A8 bis A11 (parallel; Erwartungen hier vor dem Start geschrieben, Zeit oben per date)
- **Erwartung vor Abruf 8** (Suche Joe 1989/1991, Lawson, 3D-Umklappen): Eine Quelle sagt: In 2D erreicht Lawsons
  Umklappen von jeder Triangulierung aus Delaunay; in 3D kann Umklappen von einer beliebigen Triangulierung aus
  stecken bleiben (Joe 1989); inkrementelles Einfuegen mit Umklappen erreicht Delaunay immer (Joe 1991; Edelsbrunner/
  Shah 1996 fuer regulaere Triangulierungen). Bestaetigt LT4 Teil 1.
- **Erwartung vor Abruf 9** (Suche Mijatovic S^3, Pachner-Schranken, Erkennbarkeit in 3D): Mijatovic 2003 gibt eine
  explizite (also berechenbare) Schranke fuer die Zahl der Pachner-Zuege zwischen zwei Triangulierungen der S^3,
  exponentiell in n^2; Folgearbeiten fuer weitere Klassen; 3-Mannigfaltigkeiten allgemein ueber Geometrisierung
  entscheidbar. Bestaetigt LT4 Teil 2 und zeigt: In 3D greift Nabutovsky/Ben-Av nicht.
- **Erwartung vor Abruf 10** (Suche umkehrbare bzw. massenerhaltende Kunstchemie): Kruszewski/Mikolov (2020/22)
  "combinatory chemistry" mit Massenerhaltung (Atome erhalten) und spontanen autokatalytischen bzw. sich selbst
  erhaltenden Strukturen; Reduktion nicht umkehrbar, keine Energieerhaltung. Dann LT7 Satz 2 teilweise getroffen
  (massenerhaltend ja, umkehrbar nein).
- **Erwartung vor Abruf 11** (24-Monats-Suche physikalische Church-Turing-These / Quantengravitation): wenige Arbeiten;
  wahrscheinlich Faizal/Krauss/Shabir/Marino 2025 ("undecidability ... theory of everything", keine algorithmische
  Weltformel, keine Simulation) mit Kritik; dazu Arbeiten zur Unentscheidbarkeit in Gitter-Quantensystemen. Keine
  Arbeit, die die physikalische These fuer diskrete Raumzeit pruefbar macht.
- Ergebnis A8 (Suche [S Treffer]; Quellen laut Trefferliste Santos, arXiv math/0601746, und Edelsbrunner/Muecke,
  arXiv math/9410208): Joe hat um 1990 die (2,3)- und (3,2)-Zuege eingefuehrt; "one cannot, in general, monotonically
  flip from any triangulation to the Delaunay triangulation, but the incremental algorithm works"; in 2D (Lawson)
  "every triangulation can be monotonically transformed in the Delaunay triangulation". Erwartung bestaetigt (eine
  Zeile). Praezisierung: "monoton" (nur verbessernde Zuege) ist die Bedingung, unter der 3D stecken bleiben kann.
- Ergebnis A9 (Suche [S Treffer]; Mijatovic-Abstractseite nms.kcl.ac.uk und arXiv math/0008107; Burton, arXiv
  1110.6080): S^3 mit t Tetraedern -> Standardtriangulierung in weniger als a t^2 2^(b t^2) Pachner-Zuegen,
  a <= 6e6, b < 5e4; daraus neuer Erkennungsalgorithmus. Burton: Weil man fuer 3-Mannigfaltigkeiten entscheiden kann,
  ob zwei Triangulierungen dieselbe Mannigfaltigkeit sind, gibt es "a theoretical computable function that bounds
  the distance of two triangulations in the Pachner graph", "purely theoretical at present". Erwartung bestaetigt.
  Folge [ES]: In 3D gilt die berechenbare Ergodizitaet, die Nabutovsky/Ben-Av in 4D fuer S0 ausschliessen. -> Die
  Grenze verlaeuft zwischen 3D und 4D (Moderator Dimension), nicht zwischen fester und wechselnder Topologie.
  Wortlaut Burton noch nicht an der Quelle (A19 geplant).
- Ergebnis A10 (Suche [S Treffer]; arXiv 2003.07916, ALIFE 2020): Combinatory Chemistry hat "conservation laws
  replicating natural resource constraints", entstehen ohne Eingriff autopoietische Strukturen, wachsende Ketten und
  "patterns able to reproduce themselves, duplicating their number at each generation", mit Stoffwechsel.
  **Verstoss: teilweise.** Massenerhaltung mit spontaner Selbstvermehrung ist belegt (Treffer); ob die Reaktionen
  umkehrbar sind und ob es eine Energie gibt, steht im Treffer nicht. -> Volltext (A13).
- Ergebnis A11 (24-Monats-Suche [S Treffer]): arXiv 2604.00182 "Limits to Computational Acceleration Imposed by
  Quantum Field Theory and Quantum Gravity" (April 2026): Quanteneffekte vereiteln Beschleunigungsschemata
  (Malament-Hogarth), Schranken aus Energieskalen, "strengthens the physical Church-Turing thesis at the level of
  computability", Bezug zu Entropieschranken und Swampland. Faizal u. a. 2025 tauchte nicht auf. Dazu Arrighi/Dowek
  (arXiv 1102.1612): Gandy-Postulate "homogeneity of space and time, bounded density and velocity of information".
  **Verstoss: ja (klein):** Erwartet war "keine Arbeit macht die These fuer Quantengravitation pruefbar"; gefunden ist
  eine Arbeit 2026, die sie aus QFT+QG **staerkt** (Treffer, nicht gelesen). Neuer Strang durch Arrighi/Dowek:
  "causal graph dynamics" (Graphdynamik mit wechselnder Topologie, Gandy-artig) [L] -> A12.

### A12, A13, A15, A16 (Erwartungen vor dem Start; Zeit oben per date)
- **Erwartung vor Abruf 12** (Suche umkehrbare causal graph dynamics, Arrighi u. a.): Arrighi/Dowek 2012/13 zeigen
  fuer kausale, verschiebungsinvariante Graphdynamiken mit beschraenkter Geschwindigkeit eine Lokalitaets-(Gandy-)
  Darstellung; Arrighi/Martiel/Perdrix 2016: **umkehrbare** kausale Graphdynamiken erhalten die Eckenzahl
  (keine Erzeugung/Vernichtung von Ecken); spaetere Arbeit: mit geeigneter Benennung doch moeglich (50 %).
- **Erwartung vor Abruf 13** (Volltext Combinatory Chemistry 2003.07916): Reduktionsreaktionen sind einseitig (nicht
  umkehrbar), nur Kondensation/Spaltung sind gegenlaeufig; erhalten wird die Atomzahl, keine Energie (65 %).
- **Erwartung vor Abruf 15** (Abstract Aguera y Arcas u. a. 2024, arXiv 2406.19108): Selbstreplikatoren entstehen
  spontan in einer Ursuppe aus BFF-Programmen ohne Fitnessfunktion, auch ohne Hintergrundmutation; Uebergang mit
  Komplexitaetssprung; weitere Sprachen (Forth, Z80). Bestaetigt LT7 Satz 1 zweite Haelfte (80 %).
- **Erwartung vor Abruf 16** (Suche Fontana/Buss 1994 AlChemy): Lambda-Ausdruecke kollidieren (Anwendung + Normalform);
  Ebene 0 Selbstkopierer, Ebene 1 selbsterhaltende Organisationen (algebraisch abgeschlossen), Ebene 2 Verbuende; die
  Organisationen entstehen, wenn Kopierer unterdrueckt werden. Bestaetigt LT7 Satz 1 erste Haelfte (80 %).
- Hinweis Zaehlung: Die Nummer 14 ist nicht vergeben (Sprung beim Schreiben). Bisher 15 Abrufe: A1-A13, A15, A16.
- Ergebnis A12 (Suche [S Treffer]; arXiv 1502.04368 "Reversible Causal Graph Dynamics", 1202.1098 "Causal graph
  dynamics", 1805.10330 "Size-varying reversible causal graph dynamics", HAL 01800661 "Reversibility vs local
  creation/destruction"): Kausale Graphdynamiken = Zellularautomaten auf beschraenkt-gradigen, zeitlich veraenderlichen
  Graphen; "Invertible CGD are almost vertex-preserving"; die Frage, ob umkehrbare Nachbardynamik die Netzgroesse
  aendern darf, sei "settled negatively in three different ways", lokale Erzeugung/Vernichtung gelinge "in three
  relaxed settings whose equivalence is proven"; umkehrbare CGD als Schaltkreise endlicher Tiefe aus lokalen
  umkehrbaren Gattern.
  **Verstoss: ja (stark, unerwartet relevant).** Erwartet war "erhalten die Eckenzahl" (eingetroffen); nicht erwartet
  war, dass es ein ganzes Programm gibt, das genau Finns Frage "umkehrbare oertliche Netzdynamik mit Ecken-Erzeugung
  (1-4) und -Vernichtung (4-1)" formal behandelt, mit Gandy-artigen Darstellungssaetzen. -> Abstract lesen (A17).
- Ergebnis A13 (10:58:38, curl arXiv-PDF; quellen/A13-...txt, S. 3, Gl. 1-4) [S]: Reduktionsreaktionen
  "α(If)β -> αfβ [+I]", "α(Kfg)β -> αfβ [+g + K]", "α(Sfgx)β [+x] -> α(fx(gx))β [+S]" sind einseitig; nur
  "x + y <-> xy" (Kondensation/Spaltung) ist gegenlaeufig; "each of these reduction rules preserves the total number of
  combinators in the multiset"; "computation takes precedence" (Reduktion sofort, als autokatalysiert gedeutet). Keine
  Energie. Erwartung bestaetigt (eine Zeile): massenerhaltend ja, umkehrbar nein, energieerhaltend nein.
- Ergebnis A15 (WebFetch arXiv-Abstract 2406.19108v2) [S Abstract]: Aguera y Arcas, Alakuijala, Evans, Laurie,
  Mordvintsev, Niklasson, Randazzo, Versari (27.06.2024, rev. 02.08.2024): "when random, non self-replicating programs
  are placed in an environment lacking any explicit fitness landscape, self-replicators tend to arise", "with and
  without background random mutations", mehrere Sprachen und Befehlssaetze; **"a counterexample of a minimalistic
  programming language where self-replicators are possible, but so far have not been observed to arise"**. Nichts zu
  Umkehrbarkeit, Energie, Erhaltung. **Verstoss: ja (klein):** "tend to" und ein Gegenbeispiel-Substrat; das Substrat
  ist ein Moderator. LT7 Satz 1 nur mit dieser Einschraenkung.
- Ergebnis A16 (Suche [S Treffer]; dazu lokal A13 S. 2 [S lokal, sekundaer]): AlChemy: Paare von Lambda-Ausdruecken
  werden durch Anwendung verbunden und ausgewertet, Population durch Zufallsentnahme begrenzt; Ebene 0: sich selbst
  berechnende Ausdruecke ("quickly emerged"); Ebene 1: Mengen, in denen jeder Ausdruck von anderen derselben Menge
  berechnet wird; Ebene 2: Verbuende von Ebene-1-Organisationen. Nachfolger: "Return to AlChemy" (arXiv 2408.12137,
  2024), "Prebiotic Functional Programs: Endogenous Selection in an Artificial Chemistry" (arXiv 2509.03534, 2025,
  im 24-Monats-Fenster), Kruszewski/Mikolov 2021 (arXiv 2103.08245). Erwartung bestaetigt (eine Zeile); dass L1 erst bei
  unterdrueckten Kopierern entsteht, steht im Treffer nicht (offen, [L]).

### A17 bis A20 (Erwartungen vor dem Start; Zeit oben per date)
- **Erwartung vor Abruf 17** (Abstract arXiv 1805.10330, Arrighi u. a.): Drei negative Antworten (umkehrbar + kausal
  -> Eckenzahl erhalten); drei gelockerte Rahmen, die Erzeugung/Vernichtung erlauben: (i) unendlich viele "schlafende"
  Ecken bzw. Vorrat, (ii) Ecken mit Namen aus einer Namensalgebra, (iii) nicht deterministische bzw. quantenartige
  Variante; Aequivalenz bewiesen (50 %).
- **Erwartung vor Abruf 18** (Church/Rosser 1936, Original-PDF): Satz 1: Sind A und B konvertierbar, gibt es C, auf das
  beide reduzieren; Korollar: Normalform eindeutig bis auf Umbenennung gebundener Variablen. Bewiesen fuer Churchs
  lambda-I-Kalkuel (Variable muss im Rumpf vorkommen), nicht fuer den vollen lambda-K-Kalkuel; "nicht stark
  normalisierend" steht dort nicht (55 %).
- **Erwartung vor Abruf 19** (zweite Suche LT6: Pfad-Unabhaengigkeit/Dirac-Algebra + Church-Rosser): wieder keine
  ausdrueckliche Arbeit (65 %).
- **Erwartung vor Abruf 20** (Suche Pour-El/Richards gegen Weihrauch/Zhong): Pour-El/Richards 1981: berechenbare
  Anfangsdaten, nicht berechenbare Loesung der 3D-Wellengleichung, in der Supremumsnorm; Weihrauch/Zhong 2002: in
  passenden (Sobolev-/Energie-) Raeumen ist der Loeser berechenbar; Moderator Norm bzw. Glattheit (70 %).
- Ergebnis A17 (WebFetch arXiv-Abstract 1805.10330) [S Abstract]: Arrighi, Durbec, Emmanuel, "Size-varying reversible
  causal graph dynamics", v1 25.05.2018, **v4 10.07.2026**: "being the principal carriers of information, nodes cannot
  be destroyed without jeopardising bijectivity"; "The question has been settled negatively -- for three different
  reasons. Yet, in this paper we do obtain reversible local node creation/destruction -- in three relaxed settings,
  whose equivalence we prove"; Motivation u. a. "basic formalisms towards discrete quantum gravity". Die drei Gruende
  und die drei Rahmen stehen nicht im Abstract (meine Erwartung dazu: nicht pruefbar). Kern bestaetigt (eine Zeile).
- Ergebnis A18 (11:00:09, curl CMU-PDF, JSTOR-Scan ohne Textschicht; per Read-Werkzeug als Bild gelesen, S. 472-481;
  S. 482 fehlt in der Kopie) [S]:
  - S. 472: Konversion nach "Church's Rules I, II, III" (I Umbenennung gebundener Variablen, II Kontraktion, III
    Expansion), Regeln nach Church 1932 in Kleenes Fassung 1934.
  - S. 473: "if A conv B, there is a conversion from A to B which is a valley" (Berg-Tal-Bild).
  - S. 475 Lemma 1: endliche Entwicklungen, Ergebnis eindeutig bis auf Regel I.
  - S. 479 **Theorem 1:** "If A conv B, there is a conversion from A to B in which no expansion precedes any reduction."
    **Corollary 2:** "If A has a normal form, its normal form is unique (to within applications of Rule I)."
    **Theorem 2:** "If B is a normal form of A, then there is a number m such that any sequence of reductions starting
    from A will lead to B (to within applications of Rule I) after at most m reductions."
  - S. 480 Korollar: Hat eine Formel eine Normalform, so jeder wohlgeformte Teil. Abschn. 2: weitere Konversionen
    (delta-Regeln IV, V), Saetze 1 und 2 gelten dort entsprechend (S. 481).
  - S. 481 unten: "a third kind of conversion, namely the conversion that results if we modify Kleene's definitions
    ... by omitting the requirement that x be a free symbol of R" = der lambda-K-Kalkuel (Wegwerfen erlaubt); die
    Fortsetzung (S. 482) fehlt in der Kopie.
- **Verstoss: ja (mittel, gegen LT1 Teil 3).** Erwartung (55 %) "lambda-I, 'nicht stark normalisierend' steht nicht
  da" traf ein; darueber hinaus steht dort das **Gegenstueck**: In Churchs Kalkuel (Variable muss im Rumpf vorkommen,
  also nichts wird weggeworfen) fuehrt **jede** Reduktionsfolge eines normalisierbaren Terms in beschraenkt vielen
  Schritten zur Normalform (Theorem 2). Die Reihenfolge ist dort also nicht einmal fuer das Anhalten wichtig. Dass
  der Kalkuel nicht stark normalisierend ist, gilt nur fuer Terme ganz ohne Normalform [L, z. B. (lambda x.xx)(lambda x.xx)];
  dass in lambda-K die Reihenfolge ueber das Anhalten entscheiden kann, ist [L] (S. 482 nicht gelesen).
  - Moderator (Regel 1) [ES]: **Wegwerfen** (Loeschen von Information, K-Kombinator) gegen **Nicht-Wegwerfen** (lambda-I).
    Ohne Wegwerfen ist die Ordnung bis aufs Anhalten gleichgueltig; mit Wegwerfen nicht.
  - Bezug Finn [H]: Der 4-1-Zug vernichtet eine Ecke samt ihrer 4 Lapse-/Shift-Groessen; das ist das K des Netzes.
    Er wirft nur dann keine Information weg, wenn diese Groessen reine Eichung sind (linear um flach exakt, Hoehn [P]);
    mit Kruemmung sind sie schwach bestimmt (Bahr/Dittrich [P]) und der 4-1-Zug wuerde Physik loeschen.
- Lokal (ohne Budget): RAUM-GAS-L-Quellen (F17, F20) nennen Tao 2016 bzw. Turing-Vollstaendigkeit nicht (grep 0);
  F20 nennt Chen/Hou (rechnergestuetzter Blow-up). Tao 2016 und Cardona u. a. 2021 bleiben [L].
- Abrufstand: 17 (A1-A13, A15-A18). Rest 3.
- Ergebnis A19 (Suche [S Treffer]): wieder **keine** Arbeit, die die Verformungsalgebra ausdruecklich mit Church-
  Rosser/Konfluenz verbindet. Treffer: Bonzom/Dittrich 1304.5983 (Weg-Unabhaengigkeit: "two different foliations
  connecting the same pair of hypersurfaces ... yield the same evolution map"), Dittrich/Hoehn 1303.4294, Gorard
  2004.14810 (Kausalinvarianz als diskrete Kovarianz), Bulletin, ein Podcast "Causal invariance versus confluence with
  Jonathan Gorard" (The Last Theory; Datum und Inhalt nicht gesehen). Die Zusammenfassung der Suchmaschine ("The research
  connects path independence in canonical gravity to confluence ...") ist **keine Quelle**, sondern ihre eigene
  Verknuepfung; nicht verwendet. Erwartung bestaetigt (eine Zeile). LT6 nach zwei Suchen: nicht belegt.
- Ergebnis A20 (Suche [S Treffer]; FOM-Liste 2000, sapientia.ualg.pt, Wikipedia-Buchartikel): Pour-El/Richards:
  "computable and continuous initial conditions ... (with however a non-computable gradient) that lead to a continuous
  but not computable solution"; "depends upon using the 'Uniform Norm' ... if the 'Energy norm' is used, then computable
  initial data always evolve into computable functions"; in "Sobolev space settings, the solution is computable
  uniformly in the initial data". Erwartung bestaetigt (eine Zeile). Moderator Norm/Glattheit belegt (Treffer).

### A21 (letzter Abruf; Nummer 21 wegen des Sprungs, gezaehlt Abruf 20)
- **Erwartung vor Abruf 20** (arXiv-API, Abfrage computability/undecidab/Church-Turing UND quantum gravity/spacetime/
  triangulation, neueste zuerst): 5 bis 15 Treffer im Fenster Okt. 2024 bis Okt. 2026; darunter 2604.00182; Rest
  vor allem Spektralluecke/Gittermodelle, Quanten-Komplexitaet in AdS/CFT, philosophische Arbeiten; keine Arbeit zu
  Konfluenz oder Gandy fuer Regge/Pachner-Netze.
- Ergebnis A21 = **Abruf 20** (11:02:46): HTTP 301 ohne Inhalt (eigener Fehler: http statt https, curl ohne -L).
  Gezaehlt; **nicht wiederholt** (Budget 20 erreicht). Die 24-Monats-Pflicht ist durch A11 erfuellt; kein "widerlegt"
  vergeben. Abrufbudget damit **erschoepft (20 von 20)**.

## 3. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | "Finns Netzdynamik ist hamiltonsch, also umkehrbar" (Karte, Ableitbarkeitsprobe [M]) | **ja, lokal [P]** | Nur zwischen den Zuegen. TAKT-DYNAMIK-1/HODGE-MASSE-1: Arm a ohne Zug Drift <= 2e-8; mit Zuegen verliert Lesart R 2,4 bis 12,7 % in 10 Perioden (A = 1e-3), Lesart P gewinnt 15 bis 20 %; je 2-3-Zug im Mittel 1,2e-3 bis 3,9e-3 (A2R1). Lesart R: "wegfallende Kante gestrichen, dann Projektion auf die neue Zwangsflaeche" (TAKT-DYNAMIK-1 Z. 11-12) = Loeschen von Information [ES]. **Verstoss** gegen die Karte |
| G2 | "Delaunay-Umklappen hat eine eindeutige Normalform" | **ja [M]** | Nicht auf Finns symmetrischem Netz: Die 6 Ecken eines regulaeren Oktaeders liegen auf einer Kugel (±1,0,0), (0,±1,0), (0,0,±1); jede der 3 Diagonalen gibt eine Delaunay-Triangulierung. Normalform nur modulo Diagonalwahl; genau dort sitzt der Flip-Flop aus PACHNER-TAKT-1 [P] |
| G3 | "Konfluenz/Kausalinvarianz sind fuer Finns Netz definiert" | **ja [S]** | Das Bulletin definiert Kausalinvarianz nur fuer terminierende Systeme; Verallgemeinerung offen (#487). Finns Netz terminiert nie. Uebertrag braucht eine eigene Definition |
| G4 | "Church-Rosser ist der richtige Begriff fuer HKTs Weg-Unabhaengigkeit" | teils, am Schreibtisch [M/ES] | HKT verlangt gleiche Daten auf **derselben** Endflaeche, also gleiche Zuege in anderer Reihenfolge (beschrifteter Diamant, Vertauschen unabhaengiger Zuege), nicht nur "irgendwann wieder zusammen". Der passende Rahmen ist Teilkommutation (unabhaengige Zuege vertauschen exakt, abhaengige mit Strukturfunktion) [ES; Spurmonoid-Begriff aus Gedaechtnis, L] |
| G5 | "D aus PACHNER-TAKT-1 koennte Eichung sein (Konfluenz modulo Eichung)" | ja, am Projekttext [P/ES] | AB und BA haben dieselben 111 Randkanten; D vergleicht Randimpulse bei gleichen Randlaengen, also zwei Hamilton-Funktionen derselben Randdaten. Das ist eichinvariant: D misst Triangulierungsabhaengigkeit, keine verbliebene Eichung [ES] |
| G6 | "Exakte Flip-Entscheidung ist berechenbar" | nein (nur L) | In berechenbarer Analysis ist Gleichheit reeller Zahlen nicht entscheidbar und berechenbare Funktionen sind stetig [L]; die Delaunay-Entscheidung im entarteten (kosphaerischen) Fall ist ein solcher Nulltest. Auf dem symmetrischen Netz faellt damit Nicht-Konfluenz (G2) mit Nicht-Entscheidbarkeit zusammen [ES, H] |
| G7 | "Gandy gilt fuer reellwertige Netze" | nur Treffer | Arrighi/Dowek: Gandy-Postulate enthalten "bounded density ... of information" [S Treffer]; reelle Kantenlaengen verletzen das ohne Rundung [ES] |

- Mindestens einer geprueft: G1 (Projektdateien), G2 (Mathematik), G3 (Quelle), G5 (Projekttext).

## 4. Regel 6 (Kopplung vor Bauteil): "Reihenfolge veraendert das Ergebnis" hat mindestens vier Wege

1. Kruemmung im Zeltzug-Kommutator (PACHNER-TAKT-1 [P]).
2. Loeschen von Information: lambda-K statt lambda-I (Church/Rosser S. 479, 481 [S]); 4-1-Zug; Projektion in Lesart R [P].
3. Entartete Normalform: kosphaerische Oktaeder (G2 [M]); in 3D monotones Umklappen ohne Delaunay-Ziel (Joe [S Treffer]).
4. Ueberlappende Treffer (Piskunovs Gegenbeispiele [S]).
- Gemeinsame Groesse [ES]: die **Ueberlappung der Traeger** zweier Zuege (gemeinsame Kanten bzw. Ausdruecke) mal der
  **nicht vertauschenden Aenderung der gemeinsamen Daten**. Unabhaengige Zuege (disjunkte Traeger) vertauschen in allen
  vier Faellen exakt. Messbar als Abhaengigkeitsrelation plus Defekt je kritischem Paar (Knuth-Bendix-Sprache [L];
  "critical pair lemma" bei Gorard S. 12 [S lokal]).

## 5. Regime und Unterscheidungspunkte (Regel 1 und 2), Kurzfassung fuer das Dossier

| Paar | Moderator | wo sie auseinanderlaufen | zugaenglich? |
|---|---|---|---|
| Konfluenz gegen Kausalinvarianz | Zustaende gegen Kausalgraphen | Piskunovs zwei terminierende Beispiele | ja, symbolisch; fuer Finns Netz erst nach eigener Definition (G3) |
| Geroch/Hartle gegen Nabutovsky/Ben-Av | Summe ueber Topologien gegen feste, nicht erkennbare Topologie; Dimension | 4D mit M0 = S0: GH-Argument (Topologiesumme) greift nicht als Summe, NB/BA schon | mathematisch bewiesen fuer S0; S^4 offen; 3D beide unkritisch |
| lambda-I gegen lambda-K | Loeschen erlaubt? | Term mit wegwerfbarem, nicht terminierendem Argument | ja, im Kalkuel; im Netz: 4-1-Zug mit nicht reiner Eichung |
| Pour-El/Richards gegen Weihrauch/Zhong | Norm bzw. Glattheit | Anfangsdaten mit nicht berechenbarem Gradienten | in der Natur nicht unterscheidbar (unendliche Glattheitsanforderung) |
| Gandy-berechenbar gegen analog | endliche gegen unbeschraenkte Informationsdichte | nur bei unendlicher Genauigkeit | empirisch nicht unterscheidbar |
| Kinetisches gegen beliebiges Umklappen | Schrittweite, Abstand zur Entartung | grosse Schritte bzw. Start fern von Delaunay; exakt symmetrisches Netz | ja, in silico |
| Theorie-Schranke gegen Praxis (NB/BA gegen "Absence of barriers") | Netzgroesse N | sehr grosse N | praktisch nicht (Schranken nicht rekursiv) |

## 6. Offene Rueckfragen (wandern mit)

- R1: Die drei Gruende und die drei gelockerten Rahmen bei Arrighi u. a. (nur Abstract gelesen).
- R2: Welche 4D-Pachner-Zuege verbinden AB und BA aus PACHNER-TAKT-1 (dort nicht bestimmt)? -> Kartenvorschlag K2.
- R3: Ist T^4 bzw. T^3 x I algorithmisch erkennbar? [nicht gesucht]
- R4: Gandy 1980, Deutsch 1985, Tao 2016, Cardona u. a. 2021 nicht an der Quelle gelesen.
- R5: Podcast "Causal invariance versus confluence with Jonathan Gorard": Datum, Inhalt (raeumt Gorard die Unabhaengigkeit ein?).

## 7. Abschluss

- DOSSIER.md geschrieben ab 11:08:16; Rueckwaertsdurchgang: Abrufzahl-Satz, Bulletin-Reichweite (terminierend), S^4-Stand (1992), Gorard-Seite (S. 12 statt 11), Arrighi-Kennzeichen, Gandy "wahrscheinlich", Einfach-gesagt-Schlusssatz berichtigt.
- quellen/A21-...xml ist leer (HTTP 301), als Beleg des Fehlabrufs belassen.
- Abgabe 2026-10-05 11:14:46 CEST (date).
