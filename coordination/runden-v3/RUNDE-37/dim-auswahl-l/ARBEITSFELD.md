# ARBEITSFELD DIM-AUSWAHL-L (feldforscher, Runde 42)

- Agentenstart 2026-10-04 18:49:10 CEST (date). Zeitbox 75 min, also bis 20:04 CEST.
- Einzige Arbeitsdatei. Gestrichenes wird ~~gestrichen~~, nicht geloescht. Offene Rueckfragen stehen unten in Abschnitt R.
- Abrufzaehler: 0 von 10. Keine Websuche.

## 0. Projektstand gelesen (18:49 bis 18:53, nur lokale Dateien, kein Abruf)

- n-dimensionen-grundlagen-20260912.md [P]: Ehrenfest (1a), Tangherlini (1b), Derrick (4a), Zeeman-Knoten nur R^3 (4e),
  Huygens ungerade n >= 3 (5a), Rueckwirkung lokal nur D = 4 (5c), Polya d <= 2 (6a), Anyonen d = 2 (8c), Tegmark (9a),
  KK-Massenturm (9c).
- STRANG-ANKER-L DOSSIER [P]: GW170817 D = 4,02 +0,07/-0,10 (nicht kompakte Zusatzdim.), Newton bis 52 um, LHC M_D,
  Cassini, Photonmasse; Spitzen nur in 3+1 generisch (O'Callaghan 1005.3220 [S dort]).
- DD-SPUREN (R23) [P]: flache Dark Dimension nach Langhoff R <~ 0,2 um (unbegutachtet); KK-Graviton-Zerfall an der
  Schwelle ~ q^5 unterdrueckt (LRR, Langhoff).
- RUNDE-22 geometrie-stand [P, dort S]: EDT gleiche Gewichte d_h = unendlich, mit EH-Gewicht d_h = 2 (verzweigte
  Polymere) (AJL 2004 S. 2-3); CDT d_s = 4,02 +- 0,1 gross, 1,80 +- 0,25 klein (Extrapolation, AJL 2005 Gl. 14-15);
  Kausalmengen: Kleitman-Rothschild-Posets dominieren die Entropie (Surya 2019 S. 20); "Die Zahl 4 kommt aus den
  Bausteinen" [H dort]. Verstoss dort schon: d_s faellt nicht universell auf 2 (CDT ~3/2 Coumbe/Jurkiewicz; Kausalmengen
  steigend, Eichhorn/Mizera) [S Abstract dort].
- BAG-DIM (R24) [P]: Beutelexponent misst d_s, nicht d_H.
- WOLFRAM-SCAN-L (R41) [P]: keine Regel mit 3+1-Kausalgraph; Beispielregel raeumlich ~2,6-dimensional.
- Folge fuer das Budget: E3 und E4 sind weitgehend schon im Projekt; Abrufe gehen auf E1, E2, E6 und Frage 2/3.

## 1. Schreibtisch der Leitung, selbst geprueft (18:54, Kopf, [ES])

- S1 Schnittregel: Zwei Untermannigfaltigkeiten der Dimension a, b im n-dim. Raum schneiden sich generisch, wenn
  a + b >= n (Transversalitaet; Schnittdimension a + b - n). Weltflaechen von k-Gebilden haben a = b = k + 1, n = D_Raum + 1.
  -> 2(k+1) >= D_Raum + 1 <=> D_Raum <= 2k + 1. Punkte 1, Faeden 3, Membranen 5. RICHTIG.
  - Randfall D_Raum = 2k + 1: Schnitt nulldimensional (Punkte). "Treffen sich" heisst nicht "treffen sich schnell
    genug" (gegen die Hubble-Rate). Das ist Dynamik, nicht Zaehlung -> Literatur (Raten).
  - [ES] Zwei Regime fuer die Schnittregel: glatte (ballistische) Gebilde gegen Irrfahrt-Gebilde. Ein Faden als Irrfahrt
    hat raeumlich Hausdorff-Dim. 2 statt 1; dann zaehlt nicht k, sondern die fraktale Dimension. Punkte: ballistisch
    D_Raum <= 1, diffusiv treffen sich zwei Irrlaeufer dauernd nur bis d <= 2 (Polya auf die Differenz) [L].
    Moderator: Bewegungsart (ballistisch/diffusiv). Unterscheidungspunkt: D_Raum = 4 und 5 fuer Faeden.
- S2 Finns PU-Bild: Weitester Punkt einer Gitterzelle (Abstand a) ist die Zellmitte, Abstand (a/2) sqrt(D).
  Volle Ueberdeckung <=> r >= (a/2) sqrt(D) <=> D <= 4 (r/a)^2. RICHTIG.
  - Mittlere Ueberdeckung = V_D (r/a)^D. Bei r = a: V_12 = pi^6/720 ~ 1,335 >= 1, V_13 = 2^7 pi^6/13!! ~ 0,911 < 1
    -> "im Mittel bis 12" RICHTIG.
  - Aber: Beide Zahlen haengen an r = a. Bei r/a = sqrt(3)/2 voll genau bis 3 (tautologisch). Fuer grosses r/a
    (Stirling) D_voll = 4 (r/a)^2, D_Mittel ~ 2 pi e (r/a)^2 (minus Log-Korrektur) -> Verhaeltnis ~ pi e/2 ~ 4,3.
    [ES, Kopf, nicht gegengelesen] Robust ist hoechstens das Verhaeltnis "teilweise : voll" ~ 3 bis 4, nicht die
    Zahlen 4 und 12 selbst.
  - "Im Mittel >= 1" ist mittlere Mehrfachueberdeckung, keine Ueberdeckung; < 1 erzwingt Luecken, >= 1 nicht deren Fehlen.
  - [L] Verwandter strenger Begriff: Lebesgue-Ueberdeckungsdimension (dim <= n <=> jede offene Ueberdeckung hat eine
    Verfeinerung mit Ordnung <= n + 1). Dort zaehlt die Ueberlappungs-Ordnung, nicht der Radius.
- S3 V_D: V_D/V_(D-2) = 2 pi/D -> waechst je Paritaetsklasse bis D < 2 pi. Kontinuierliches Maximum bei
  psi(D/2 + 1) = ln pi, D ~ 5,257 [L, bekannter Wert]; ganzzahlig V_5 = 8 pi^2/15 ~ 5,264 > V_6 = pi^3/6 ~ 5,168.
  RICHTIG. Aber [ES]: V_D ist nicht skalenfrei; fuer Radius r liegt das Maximum von V_D r^D bei ~ 2 pi r^2. Das
  Maximum bei 5,26 ist eine Aussage ueber die Einheitskugel, keine Dimensionsauswahl ohne festgelegtes r/a.
  (Dieselbe Funktion wie S2 bei r = a.)

## 2. Abrufe (Erwartung vor dem Abruf, Ausgang danach)

### A1 (Erwartung geschrieben 2026-10-04 18:54:24 CEST, vor dem Abruf): arXiv-API id_list, 27 IDs aus dem Gedaechtnis

Ziel: Abstracts fuer E1, E2, E6, Frage 2/3 in einem Abruf. IDs [L], bis zur Pruefung unsicher.
Erwartung je ID (ein Satz):
- hep-th/0005212 ABE: p-Branen lassen hoechstens 2p+1 Raumdimensionen gross werden; Hierarchie 3 gross, bis 5 mittel (E2).
- hep-th/9511075 Sakellariadou: Numerik bestaetigt, dass Windungen nur in <= 3 Raumdim. vernichten (E1 numerisch).
- hep-th/0510022 Battefeld/Watson: Uebersicht Stringgas, offene Probleme (Dilaton, Moduli, Raten).
- 0808.0746 Brandenberger: Stringgas-Uebersicht, 3 grosse Dim. "BV" als Ergebnis plus Strukturbildung.
- hep-th/0409162 Danos/Frey/Mazumdar: Windungs-Vernichtungsraten zu klein bzw. Ausfrieren; Mechanismus fragil.
- hep-th/0409121 Easther/Greene/Jackson/Kabat: Windungen vernichten in expandierendem Raum nicht vollstaendig.
- hep-th/0211124 EGJK: Branengas in M-Theorie, spaete Zeit; Isotropie bzw. kein Auswahleffekt.
- hep-th/0501163 Durrer/Kunz/Sakellariadou: Branengas erklaert 3+1 nicht ohne Zusatzannahmen.
- 0908.0955 Greene/Kabat/Marnerides: dynamische Dekompaktifizierung, 3 grosse Dim. mit Zusatzbedingung.
- hep-th/0506053 Karch/Randall: In AdS ueberleben 3- und 7-Branen die Verduennung -> 3+1 bevorzugt.
- 1108.1540 Kim/Nishimura/Tsuchiya: Lorentzsches IKKT, 3 von 9 Raumrichtungen expandieren spontan.
- 1108.1293 Nishimura/Okubo/Sugino: euklidisches IKKT (GEM), SO(10) -> SO(3).
- 2002.07410 Anagnostopoulos u. a.: Complex Langevin bestaetigt SO(10) -> SO(3).
- 1904.05914 Aoki u. a.: Die expandierende 3D-Struktur ist Pauli-Matrix-artig, also singulaer.
- hep-th/9602022 Vafa: F-Theorie, 12D-Formulierung mit zwei Hilfsrichtungen (Torus = Axion-Dilaton).
- 1508.01458 Berera u. a.: Geknotete Flussroehren stabilisieren genau 3 Raumdimensionen.
- hep-th/0303031 Giddings: 4D-Vakua sind gegen Dekompaktifizierung instabil.
- 0904.3115 Carroll/Johnson/Randall: dS hoeherer Dimension kompaktifiziert dynamisch, Uebergaenge zwischen Dimensionszahlen.
- 0912.4082 Blanco-Pillado/Schwartz-Perlov/Vilenkin: transdimensionales Tunneln in der Landschaft.
- 1004.4567 Schwartz-Perlov/Vilenkin: Mass ueber Dimensionszahlen, Ergebnis massabhaengig.
- 1003.0236 Graham/Harnik/Rajendran: beobachtbare Anisotropie eines hoeherdimensionalen Elternvakuums.
- 1108.0119 Brown/Dahlen: Dekompaktifizierung als schnellster Zerfall, alle Vakua besiedelt.
- 1705.05417 Carlip: d_s -> 2 in vielen Ansaetzen (E4).
- 1003.5914 Anchordoqui u. a.: "verschwindende Dimensionen", bei hoher Energie 2D bzw. 1D, planare LHC-Ereignisse.
- 1102.3434 Mureika/Stojkovic: primordiale GW als Test verschwindender Dimensionen.
- 1709.00064 Loomis/Carlip: EH-Wirkung unterdrueckt nicht-mannigfaltigkeitsartige Kausalmengen.
- 1502.01843 Gonzalez-Ayala u. a.: thermodynamisches Argument fuer 3+1.
Gesamterwartung: 3 bis 5 IDs falsch (Quote STRANG-ANKER-L 2/21).

#### A1 Ausgang (gelesen 18:54:43 bis 18:56:15 [date beim Eintrag], Kopie quellen/A1-api-idlist.xml, Auszug quellen/A1-abstracts.txt)

- Abrufzaehler 1 von 10. Alle 27 IDs richtig (erwartet 3 bis 5 falsch) -> kleiner Kanal-Verstoss, sonst nichts.
- Bestaetigt (eine Zeile je): ABE (hep-th/0005212) "string winding modes will only allow four space-time dimensions to
  become large", p > 1 "may lead to a hierarchy" (Zahlen der Hierarchie NICHT im Abstract) | Sakellariadou 1995:
  "long winding strings decay only if the space dimensionality ... is equal to 3" (niedrige Energiedichte) |
  Karch/Randall: "dominated by 3-branes and 7-branes" | Carlip 2017: "effectively two dimensional" | Loomis/Carlip:
  "most causal sets are not at all manifold-like" | Kim/Nishimura/Tsuchiya: "three out of nine spatial directions start
  to expand" | Nishimura/Okubo/Sugino: "free energy takes the minimum value at d = 3" (GEM 3. Ordnung, 2 <= d <= 7) |
  Anagnostopoulos u. a. 2020: CLM "SO(3) symmetric vacuum" (mit Deformation) | Berera u. a.: Knotennetz "topologically
  stable only in three space dimensions" | Giddings 2003 | Carroll/Johnson/Randall | Blanco-Pillado u. a. |
  Brown/Dahlen | Graham/Harnik/Rajendran | Anchordoqui u. a. | Mureika/Stojkovic | Vafa F-Theorie "12 dimensional".
- **VERSTOSS V-A (gross, E1):** Easther/Greene/Jackson/Kabat 2004 (hep-th/0409121): Bei Gleichverteilung ueber Zustaende
  (Dilaton und Volumen fest) "although dynamical evolution can indeed lead to three large spatial dimensions, such an
  outcome is not statistically favored". Danos/Frey/Mazumdar 2004 (hep-th/0409162): "the interaction rates of strings
  are negligible, so the common assumption of thermal equilibrium cannot apply". Rettung Greene/Kabat/Marnerides 2009
  (0908.0955): starke exponentielle Unterdrueckung fuer d > 3 im Stossparameterbild, gueltig "if wound strings are heavy
  ... and diluted"; aber "for any number of dimensions the universe generically stays trapped in the Hagedorn regime";
  nur nach Fluktuation in ein Strahlungsregime frieren Rest-Windungen in d > 3 aus und vernichten in d = 3.
  -> Korrektur der Erwartung: E1 gilt als Zaehlargument; dynamisch zwei (drei) Regime. Moderator: Anfangsmass und
  Regime (dichtes Gleichgewichtsgas / verduennte schwere Windungen nach Hagedorn-Austritt / Gleichverteilung).
  Volltext EGJK 2004 noetig: Dort steht die einzige Wahrscheinlichkeitsverteilung ueber die Zahl grosser Dimensionen,
  die ich bisher sehe (Frage 3).
- **VERSTOSS V-B (gross, Frage 2):** Giddings 2003 (hep-th/0303031): Positive Vakuumenergie "generically implies
  catastrophic instability of our four-dimensional world. The most generic instability is a decompactification
  transition". Umgekehrte Lebensdauer-Hierarchie zu Finns Bild: Nicht die vielen Dimensionen sind kurzlebig, die
  Kompaktifizierung auf 3+1 ist metastabil. Battefeld/Watson 2005: "at late-times it is not possible to stabilize the
  extra dimensions by a gas of massive string winding modes" (braucht Zustaende erhoehter Symmetrie).
- **VERSTOSS V-C (mittel):** Aoki u. a. 2019 (1904.05914): Der expandierende 3D-Teil im Lorentz-IKKT ist "essentially
  by the Pauli matrices", Ursache eine Naeherung e^(iS_b) -> e^(beta S_b). Der Lorentz-Befund "3 von 9" ist damit
  naeherungsabhaengig; der euklidische (GEM + CLM) ist der belastbarere. 24-Monats-Stand noetig.
- **VERSTOSS V-D (mittel, Frage 2):** Anchordoqui u. a. 2010: Dimensionszahl haengt von der Laengenskala ab, kurz
  niedriger, mittel 3, gross "effectively higher dimensional". Eine Hierarchie nach Skala statt nach Lebensdauer.
  Test: 2+1 hat keine GW-Freiheitsgrade -> Grenzfrequenz (Mureika/Stojkovic). Stand nach 2011 unbekannt.
- Durrer/Kunz/Sakellariadou 2005: Antwort ist Branenwelt, "left with D3-branes embedded in a (9+1)-dimensional bulk";
  "3" heisst dort "Dimension unserer Brane", nicht "Zahl grosser Dimensionen". Zwei Bedeutungen von "drei" -> Regime.
- Gonzalez-Ayala u. a. 2015: Minimum der Helmholtz-Energie je Hypervolumen der Hohlraumstrahlung waehlt n = 3.
  [ES] Verdacht wie bei V_D: T^(n+1) vergleicht verschiedene Einheiten; das Minimum ueber n muesste an T in einer
  gewaehlten Einheit haengen. Volltext pruefen, falls Budget.
- Schwartz-Perlov/Vilenkin 2010: Mass fuer transdimensionales Multiversum; naive Verallgemeinerung widerspricht der
  Beobachtung, "volume factor cutoff" als Ausweg. Verteilung ueber D im Abstract nicht genannt.

### A2 (Erwartung geschrieben vor dem Abruf, Zeit siehe date-Zeile darunter): arXiv-API-Suche, 24 Monate (04.10.2024 bis 04.10.2026)

- Anfrage: abs "string gas" | "Brandenberger-Vafa" | "three large" | "dimensionality of space" | "dimensionality of
  spacetime" | "number of spatial dimensions" | "transdimensional" | "IKKT" | "type IIB matrix model" | "vanishing
  dimensions", submittedDate 202410040000 bis 202610042359, nach Datum, max 100.
- A2-E1: Stringgas: wenige neue Arbeiten (Brandenberger u. a.), keine neue Widerlegung oder Bestaetigung des
  BV-Mechanismus.
- A2-E2: IKKT-Gruppe (Nishimura u. a.) meldet Lorentz-Simulationen mit glatter (3+1)-Expansion ohne Pauli-Artefakt,
  unbegutachtet.
- A2-E3: keine neue Arbeit mit expliziter Wahrscheinlichkeitsverteilung ueber die Zahl grosser Dimensionen.
- A2-E4: "vanishing dimensions": nichts Neues.

#### A2 Ausgang (Abrufzaehler 2 von 10)

- Anfrage zu breit: 3314 Treffer ("three large", "number of spatial dimensions", "dimensionality of space" treffen
  Fremdes). Die 100 neuesten decken nur 17.09. bis 01.10.2026 ab. Fuer den 24-Monats-Zweck fast leer [Selbstanzeige].
- Nebenbefund: IKKT ist aktiv, 2609.40183 "Lie Algebra Saddles in the IKKT Matrix Model and Criteria for the Emergence
  of Time" (30.09.2026), 2609.35963 "Type IIB supergravity solutions for polarized IKKT" (28.09.2026) [S Titel].
- Erwartungen A2-E1 bis E4 gehen unveraendert an A3 weiter.

### A3 (Erwartung vor dem Abruf, date-Zeile oben): enge 24-Monats-Suche

- Anfrage: abs "string gas cosmology" | "Brandenberger-Vafa" | "three large spatial dimensions" | "three large
  dimensions" | "transdimensional" | "vanishing dimensions" | (abs IKKT UND abs expanding) | ti "dimensionality of
  spacetime" | ti "why three", submittedDate 202410040000 bis 202610042359, max 100.
- Erwartungen wie A2-E1 bis A2-E4; dazu A3-E5: weniger als 60 Treffer.

#### A3 Ausgang (Abrufzaehler 3 von 10, konservativ gezaehlt)

- arXiv antwortete 503 (HTML, 126 Byte), keine Eintraege. Leer. Moegliche Ursache: verschachtelte Klammer oder Last.

### A4 (Erwartung vor dem Abruf, date-Zeile oben): dieselbe enge Suche ohne verschachtelte Klammer

- abs:"IKKT matrix model" statt (abs IKKT UND abs expanding); sonst wie A3. Erwartungen A2-E1 bis E4 und A3-E5.

#### A4 Ausgang (Abrufzaehler 4 von 10)

- Wieder 503, leer. export.arxiv.org verweigert seit ~18:57. 24-Monats-Suche spaeter hoechstens ein weiterer Versuch.
  Bis dahin gilt fuer alles Neuere: "nach Recherchestand nicht geprueft", kein "widerlegt".

### A5 (Erwartung vor dem Abruf, date-Zeile oben): Volltext Easther/Greene/Jackson/Kabat 2004, hep-th/0409121v1 (arxiv.org/pdf)

- A5-E: Bei Gleichverteilung ueber Anfangszustaende (Dilaton, Volumen fest) gibt es eine Verteilung ueber die Zahl
  grosser Dimensionen; genau 3 grosse ist selten (Prozentbereich); haeufiger wachsen alle oder keine, oder Windungen
  frieren in mehr Richtungen aus. Ursache: Anfangsmass bzw. fehlendes Gleichgewicht.

#### A5 Ausgang (Abrufzaehler 5 von 10; Kopie quellen/A5-EGJK-hep-th-0409121v1.pdf/.txt; Abb. 3 und 4 per Read angesehen)

- **VERSTOSS V-E (gross, Frage 3, gegen A5-E im Kern):** Es gibt eine Verteilung, aber sie "pendelt" nicht ein. Sie ist
  eine wandernde Glocke, deren Lage der Anfangswert der Kopplung (Dilaton phi) setzt.
  - Abb. 4 (S. 26, je 10^3 Laeufe, V = 4,0 (2 pi sqrt(alpha'))^9, phi-Punkt = -1) [S Abb., Augenmass]:
    phi = -1,0: alle bei 9 grossen Dimensionen; -1,5: Gipfel 7 (4 bis 9); -2,0: Gipfel 5 (2 bis 8); -2,5: Gipfel 2
    (0 bis 4); -3,0: Gipfel 0; -3,5: fast nur 0.
  - Text Z. 821-823: "for a rather narrow range of phi three dimensions is the favored outcome, the distribution of
    final dimensionality is not very sharply peaked".
  - Schluss Z. 835-844: "all or nothing" — viele gewickelte Strings frieren aus und halten alle Dimensionen klein, wenige
    vernichten sich und "all dimensions decompactify"; 3 nur bei feinabgestimmten Anfangswerten.
  - Ursache Z. 846-848: "due to the rolling dilaton the string annihilation cross section becomes weaker".
  - Z. 887-895: drei Deutungen (andere Dynamik; Mass (32) falsch; 3 nicht bevorzugt, dann anthropisch).
  - Z. 81-84: Sakellariadou bestaetigte die Zaehlung 2+2 = 3+1 "in a static background" (Regime statisch!).
  - Mass Z. 646-656: Liouville-Mass Omega ~ d^9 lambda d^9 lambda-Punkt d phi d phi-Punkt e^(-10 phi) e^S; Entropie
    maximal bei phi -> -unendlich (schwache Kopplung). [ES] Das Mass selbst zieht in das Regime "alles bleibt klein".
- Korrektur der Erwartung: nicht "3 selten", sondern "jede Zahl 0 bis 9 moeglich, Lage durch einen stetigen
  Anfangsparameter gesetzt, Breite etwa +-1 bis 2". Fuer Finns Frage heisst das: In diesem Modell gibt es keinen
  Attraktor bei 3 bis 4; die Zaehlregel (Schnitt) ist statisch richtig, die Dynamik waehlt nicht.
- Regime fuer E1: statisch (Sakellariadou: nur 3 zerfallen) / dynamisch mit rollendem Dilaton (EGJK: nicht bevorzugt) /
  verduennt-schwer nach Hagedorn-Austritt (GKM 2009: wirkt). Unterscheidungspunkt: Anfangskopplung und Dichte der
  Windungen.

### A6 (Erwartung vor dem Abruf, date-Zeile oben): Volltext Greene/Kabat/Marnerides 2009, 0908.0955v2

- A6-E: Rate fuer Windungs-Vernichtung im Stossparameterbild ~ exp(-b^2/...) bzw. Potenz der Laenge mit Exponent, der
  bei d = 3 umschlaegt; Bedingung "schwer und verduennt"; Hagedorn-Falle fuer jedes d; in d > 3 Ausfrieren. Zahl fuer
  die Unterdrueckung (z. B. ~ (l_s/R)^(d-3)) als Unterscheidungspunkt fuer eine Netz-Karte.

#### A6 Ausgang (Abrufzaehler 6 von 10; Kopie quellen/A6-GKM-0908.0955v2.pdf/.txt)

- A6-E im Kern eingetroffen, eine Zeile: Stossparameter b in den D - 4 Querrichtungen, Im A(s,b) ~ exp(-b^2/(4 Y alpha'))
  (Gl. 5), Dicke Delta x^2 = 4 alpha' log(R^2/alpha') (Z. 290-292); bei D = 4 gibt es keine Querrichtung.
- Neu und wichtig [S]:
  - Gueltigkeit Z. 666-676 (berichtigt 19:05, vorher falsch "680-690"): Strings muessen "semiclassical one-dimensional objects" sein, Laenge >> Quantendicke,
    Dicke << Querausdehnung; "in the Hagedorn phase strings have a significant spread in all directions and the
    classical picture fails".
  - Ergebnisse Z. 628-645: Fuer alle d bleibt Hagedorn-Gleichgewicht; viele Anfangswerte "remain forever trapped";
    grosses Volumen mit <W> -> 0 in der Hagedorn-Phase -> Dekompaktifizierung "for any d"; fuer d > 3 ausserhalb
    Hagedorn "few cases (of order 1%)". d = 3: auch in der Strahlungsphase vernichten lange Strings.
  - Aufbau Z. 672 (berichtigt 19:05, vorher falsch "682-684"): "simple isotropic setup", d gleich grosse Richtungen (d = 3 ... 9). [ES] GKM zeigen die
    d-Abhaengigkeit der Vernichtung, nicht die Auswahl von 3 aus 9 in einem anisotropen Torus (das tat EGJK 2004 mit
    "alles oder nichts"). Beide Befunde widersprechen sich nicht: zwei Regime (isotrop-verduennt gegen anisotrop mit
    rollendem Dilaton).
  - Hierarchie Z. 96-105 (ueber Easther u. a. 2002 und Folgearbeit): Anfangszustaende mit "3 dimensions unwrapped, some
    number of dimensions partially wrapped and some fully wrapped" -> "a hierarchy among dimensions is established";
    mit Fluessen "suppressing the growth of 3 out of the 6 unwrapped dimensions". Das ist Finns "3 gross, einige
    teilweise" in der Literatur, aber AUS GEWAEHLTEN ANFANGSZUSTAENDEN.
- [ES, Regel 6] Drei Wege zu "3" (glatte Weltflaechen 2+2 >= d+1; Knotennetz nur in R^3 (Berera u. a.); Irrfahrt-
  Strings: zwei Brownsche Pfade schneiden sich in R^d genau fuer d <= 3 [L, Dvoretzky/Erdoes/Kakutani]) teilen eine
  Groesse: Verschlingung/Schnitt von 1-dimensionalen Gebilden braucht Kodimension 2 (p + q = n - 1, Alexander-
  Dualitaet [L]). Die "3" kommt aus k = 1 (Faeden), nicht aus Statistik. Mit Membranen waere es 5.

### A7 (Erwartung vor dem Abruf, date-Zeile oben): Volltext Alexander/Brandenberger/Easson 2000, hep-th/0005212v2

- A7-E: Regel "p-Branen lassen hoechstens 2p+1 Raumdimensionen gross werden"; Membranen (p = 2) -> 5, Strings -> 3;
  Hierarchie 3 groesste, dann 2 mittlere, Rest klein; als Vermutung, ohne Dynamikrechnung.

#### A7 Ausgang (Abrufzaehler 7 von 10; Kopie quellen/A7-ABE-hep-th-0005212v2.pdf/.txt)

- A7-E eingetroffen [S, S. 4, txt Z. 274-290]: "the winding modes of p-branes can interact in at most 2p + 1 large
  spatial dimensions"; 2-Branen "will only allow 5 spatial dimensions to become large"; darin "1-brane winding modes
  will only allow a T^3 subspace"; "there will be 2 extra spatial dimensions which are larger than the remaining ones".
  Welche 5: "determined by thermal fluctuations".
- Vorbehalte an derselben Stelle [S]: Skalen nicht natuerlich trennbar ("it appears difficult to produce the mm scale");
  Kausalitaet: mindestens 1 Windungsmode je Hubble-Volumen bleibt; Branen mit p >= 2 wirken in 4D als Domaenenwaende,
  "even one-branes will overclose the Universe" -> Inflation oder anderer Ausweg noetig.
- Fuer Frage 2: Die Literatur-Hierarchie ist 3 gross / 2 mittel / 4 klein (Summe 9 Raumdim.), also 3, 5, 9 —
  nicht 3 bis 4 und 12.

### A8 (Erwartung vor dem Abruf, date-Zeile oben): Volltext Carroll/Johnson/Randall 2009, 0904.3115v2

- A8-E: Nukleationsraten aus dS_D in Vakua mit p grossen und q kompakten Richtungen; Raten haengen exponentiell von
  der Dimension ab (Euklidische Wirkung); keine normierte Wahrscheinlichkeitsverteilung ueber D, Ergebnis
  massabhaengig; "4" nicht ausgezeichnet.

#### A8 Ausgang (Abrufzaehler 8 von 10; Kopie quellen/A8-CJR-0904.3115v2.pdf/.txt; Abb. 16 per Read angesehen)

- **VERSTOSS V-F (gross, Frage 3; gegen A8-E "4 nicht ausgezeichnet", "keine Verteilung"):**
  - Es gibt eine scharfe Verteilung: P_i/P_j ~ exp[-S_dS^(D) (alpha_i - alpha_j)] (Gl. 94, Z. 1950-1955), "vacua with
    the largest possible values of alpha are exponentially favored" (unter einem bestimmten Volumenmass).
  - alpha = S_inst/S_dS (Gl. 79), fuer kleine Ladung Gl. 84 = Verhaeltnis von Einheitssphaeren-Volumina mal
    Dimensionsfaktoren. Z. 1642-1647: alpha "peaks at a value of p specified by the total dimensionality. This is due to
    the relative volumes of the unit spheres"; D = 8: p = 2, "four non-compact dimensions", ist am groessten; D = 7:
    p = 1 und 2 gleich; D = 9: p = 2 und 3 gleich; "alpha is in general larger when the total dimensionality is
    increased".
  - Abb. 16 (S. 26) [S Abb., Augenmass]: D = 6 Gipfel p = 1; D = 7 p = 1/2; D = 8 p = 2; D = 9 p = 2/3;
    D = 10 Gipfel p = 3 (~0,805), also 5 nicht kompakte Dimensionen. Unterschiede in alpha ~ 0,005 bis 0,08; mal
    |S_dS| riesig -> exponentiell scharf.
  - Vorbehalte [S]: Spielzeugmodell Einstein-Maxwell mit q-Form-Fluss auf S^q (Abstract); "the comparison of nucleation
    rates between solutions is complicated", fuer jedes p gibt es ein Q mit gleicher Rate (Z. 1765-1768); Mass
    "inherently ambiguous" (Z. 2000-2004).
- Korrektur: Eine scharfe Wahrscheinlichkeitsverteilung ueber die Zahl grosser Dimensionen existiert in mindestens einem
  Modell. Ihr Gipfel wandert mit der Gesamtdimension D (wie das V_D-Maximum mit r). "4" ist nur fuer D = 8 der Gipfel,
  fuer D = 10 eher 5.
- [ES] Bezug zum Schreibtisch S3: Hier ist das Sphaerenvolumen-Argument physikalisch sauber, weil alpha ein
  dimensionsloses Verhaeltnis zweier Wirkungen ist (kein r/a-Problem). Die Lage des Gipfels haengt dann an D, nicht
  an einer Einheit.

### A9 (Erwartung vor dem Abruf, date-Zeile oben): 24-Monats-Suche, zweiter Versuch, gleiche Anfrage wie A4

- Erwartungen A2-E1 bis E4 und A3-E5 unveraendert.

#### A9 Ausgang (Abrufzaehler 9 von 10)

- Dritter 503, leer. Verdacht: ti-Felder bzw. Stoppwort "why" in der Phrasensuche (A2 ohne ti-Felder lief).

### A10 (Erwartung vor dem Abruf, date-Zeile oben): letzte 24-Monats-Suche, nur abs-Felder wie in A2

- Anfrage: abs "string gas" | "Brandenberger-Vafa" | "three large spatial" | "transdimensional" | "vanishing
  dimensions" | IKKT, submittedDate 202410040000 bis 202610042359, max 150.
- A10-E1: Stringgas 2024-2026: wenige Arbeiten, keine neue robuste Auswahl von 3 und keine Widerlegung.
- A10-E2: IKKT: mehrere Arbeiten zur Entstehung von (3+1) im Lorentz-Modell (Nishimura u. a.), unbegutachtet.
- A10-E3: "transdimensional" und "vanishing dimensions": hoechstens vereinzelt.
- Bei erneutem 503: 24-Monats-Pruefung gilt als gescheitert; Urteile dann nur "nach gelesenem Stand", 2024-2026 offen.

#### A10 Ausgang (Abrufzaehler 10 von 10, Budget erschoepft; Kopie quellen/A10-api-24m-abs.xml, Auszug A10-abstracts.txt)

- 57 Treffer (04.10.2024 bis 04.10.2026), davon ~20 fachfremd ("transdimensional" in MCMC und Festkoerpern).
- A10-E1 eingetroffen: Stringgas nur 2603.19334 (T-Dualitaet waehlt eine disformale Metrik, keine Dimensionsauswahl)
  und 2512.22694 (Spezies-Skala/TCC; "In scenarios such as string gas cosmology ... the spacetime background remains
  completely regular") [S Abstract]. Keine neue Arbeit zur Auswahl von 3 durch Windungen, keine Widerlegung.
- A10-E2 nur teilweise: Keine neue grosse Lorentz-Simulation mit glatter 3+1-Expansion in der Trefferliste. Statt dessen
  analytische Arbeiten, die auf 4 bzw. so(1,3) zeigen [S Abstract, alle unbegutachtet]:
  - 2605.03611v3 (05.05.2026): SUSY-Ward-Identitaeten; in 10D erzwingt ein 5-Form-Term Konstanz; die 4D-Clifford-Algebra
    bietet "a unique exit through Hodge duality"; "the emergence of a four-dimensional Euclidean space-time is a
    prerequisite" fuer nichttriviale Hintergruende (fuehrende Ordnung, euklidisch, selbstdual).
  - 2609.40183v1 (30.09.2026): Lie-Algebra-Sattel; Casimir-Hindernis erklaert, warum Fuzzy-Sphaeren und expandierende
    Loesungen Massenterme oder IR-Regulatoren brauchen; halbeinfache Sattel "first appear in six dimensions and reach
    every signature only from twelve"; einziger nichttrivialer halbeinfacher Teil Lorentz-Sattel ist so(1,3).
    [ES] Hier erscheint eine 12, aber als Schwelle der Matrixzahl fuer alle Signaturen, nicht als "teilweise
    existierende Dimensionen". Namensgleichheit, kein Beleg fuer Finns 12.
  - 2512.03161v2 (02.12.2025): euklidischer IKKT-Sattel nur fuer N -> unendlich, eindeutig so(1,3), 4D-Raum mit
    SU(2)-Isometrie (Taub-NUT-artig).
  - 2608.29688v1 (30.08.2026): N = 5, "ordered 3+6 spectral separation" als rahmenabhaengige Diagnose, "not an
    intrinsic observable".
- A10-E3 eingetroffen: "vanishing dimensions" 0 Treffer; "transdimensional" physikalisch 0 relevante.
- Grenze: Anfrage ohne "IIB matrix model" ohne IKKT im Abstract; Arbeiten, die nur so heissen, fehlen evtl.

## 3. Gegensweep (ab 19:05): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 GEPRUEFT: "Drei" hat in der Literatur drei Bedeutungen, ich hatte stillschweigend "Zahl grosser Raumrichtungen"
  angenommen. (a) Zahl grosser Richtungen (BV, EGJK, GKM, IKKT); (b) Dimension der Brane, auf der wir leben, in einem
  9+1-Volumen (Durrer/Kunz/Sakellariadou "D3-branes embedded in a (9+1)-dimensional bulk"; Karch/Randall "3-branes and
  7-branes") [S Abstract]; (c) skalenabhaengige effektive Dimension (Anchordoqui u. a.; CDT d_s; Carlip) [S Abstract,
  P]. Folge: Finns "3 bis 4 stabil" passt je nach Bedeutung anders. Neuer Moderator: Bedeutung von "Dimension".
- G2 GEPRUEFT: BV braucht eine Raumtopologie mit nicht zusammenziehbaren Schleifen (Torus), sonst gibt es keine
  Windungen. ABE Z. 11 und 62 ("existence of one-cycles in all spatial directions"), Z. 415 (Calabi-Yau-Dreifaltigkeiten:
  "one cycles are absent") [S]; GKM Z. 106-118: Ausweg "pseudo-wound" Strings auf Orbifolds, "persist for many Hubble
  times" [S, sekundaer]. Die Auswahl von 3 ist also an eine Topologie-Annahme gebunden, nicht nur an die Zaehlung.
- G3 GEPRUEFT (Kopf): Finns PU-Zahlen haengen nicht nur an r = a, sondern auch am hyperkubischen Gitter. Die
  Ueberdeckungsradien anderer Gitter (z. B. A_D^*) sind kleiner [L]; fuer ein Tetraeder- oder Zufallsnetz aendern sich
  4 und 12. [ES]
- G4 NICHT GEPRUEFT: Zahl der Zeitrichtungen = 1 als gegeben genommen. Tegmark (n, m) [P]; 2609.40183 stellt
  "criteria for the emergence of time" auf [S Abstract]. Offen.
- G5 NICHT GEPRUEFT: Zwei Brownsche Pfade schneiden sich in R^d genau fuer d <= 3 (Dvoretzky/Erdoes/Kakutani 1950) [L].
  Traegt den Regime-Vorschlag (Irrfahrt-Strings); ohne Abruf nicht verifiziert.
- G6 GEPRUEFT (Projekt-grep): Kein frueherer Netz-Test "Faeden treffen und vernichten sich bei einstellbarer
  Dimension". RUNDE-10 "d = 6 vernichtet" ist ein Startabstand, kein Dimensionswert (Fehltreffer). Parallelkarten
  derselben Runde: DIM-LEITER-QBALL-1 (Q-Ball-Stabilitaet ueber D), VERSCHRAENK-DIM-1 (Verschraenkungsmaximum ueber D)
  -> Kartenvorschlag darf diese nicht doppeln.
- G7 GEPRUEFT (Projekt): GW170817 D = 4,02 gilt nur fuer nicht kompakte Zusatzdimensionen (STRANG-ANKER-L, 1801.08160
  [S Abstract dort]). Kompakte Richtungen unter ~30 um sind durch Newton-Tests nicht ausgeschlossen [P, MESSLAGE].
  Gemessen ist also "keine grosse Zusatzrichtung mit Leckage", nicht "genau drei".

## 4. Regime und Unterscheidungspunkte (Stand 19:06)

- R1 BV-Zaehlung: statisch (Sakellariadou: nur d = 3 zerfallen) / isotrop-verduennt nach Hagedorn (GKM: d = 3 vernichtet,
  d > 3 ~1 % Dekompaktifizierung) / anisotroper 9-Torus mit rollendem Dilaton und Gleichverteilungsmass (EGJK: alles oder
  nichts, Glocke wandert mit phi). Moderator: Anfangskopplung, Dichte, Mass. Unterscheidungspunkt: anisotroper Torus mit
  festgehaltenem Dilaton (dann muesste die Glocke bei 3 stehen bleiben, wenn die Zaehlung allein waehlt).
- R2 Glatte gegen raue Faeden: GKM Z. 666-676: klassisches Bild nur bei Laenge >> Dicke; Hagedorn-Strings "spread in all
  directions". Unterscheidungspunkt im Netz: Verhaeltnis Fadendicke/Torusweite in D_Raum = 4 und 5.
- R3 Landschaft: Gipfel der Keimbildungsrate (CJR) wandert mit Gesamt-D (8 -> 4D, 10 -> 5D). Unterscheidungspunkt: D = 10
  oder 11 mit realistischem Flussgehalt; nach Recherchestand nicht gerechnet.
- R4 IKKT: euklidisch SO(3) (GEM 3. Ordnung + CLM mit Deformation) / Lorentz 3 von 9 (Pauli-Artefakt der Naeherung) /
  2025-2026 analytisch so(1,3) bzw. 4D euklidisch. Unterscheidungspunkt: Lorentz-Simulation mit exaktem e^(iS_b) bei
  grossem N; nach Recherchestand nicht vorhanden.

## 5. Berichtigungen (19:07)

- A10-Eintrag "alle unbegutachtet" ist ~~alle unbegutachtet~~ falsch: 2605.03611v3 (Muramatsu) traegt laut arXiv-Feld
  journal_ref "Nucl. Phys. B 1030 (2026) 117610". Die uebrigen IKKT-Treffer (Liao 2609.40183; Liao/Maeta 2512.03161;
  Muramatsu 2608.29688; Chou/Nishimura/Wang 2507.18472) ohne journal_ref.
- Autoren 1502.01843: Gonzalez-Ayala und Angulo-Brown (zwei, nicht drei wie aus dem Gedaechtnis).
- Autoren aus der API (A1-api-idlist.xml) fuer alle zitierten IDs abgeglichen.

## R. Offene Rueckfragen an die Leitung (wandern mit)

- R1: Soll FADEN-DIM-1 (Vorschlag Frage 5) gegen DIM-LEITER-QBALL-1 und VERSCHRAENK-DIM-1 abgestimmt werden (gleiche D-Leiter
  2 bis 6, gleiche Netzgroessen)?
- R2: Volltexte Gonzalez-Ayala/Angulo-Brown 2015 (Einheitenfrage) und Vafa 1996 (Hilfsrichtungen der 12) nicht gelesen;
  Budget erschoepft.

## 6. Abschluss

- DOSSIER.md geschrieben ab 19:09:56 CEST, zwei Zeilenverweise darin um 19:13 berichtigt (ABE Z. 272-281, GKM Z. 628-647).
- Abschlusseintrag um 19:13:12 CEST (date). Abrufe 10 von 10, Websuche 0.
