# KAUSAL-4D-STABIL-L: Dossier (Feldforscher fuer die Leitung, Runde 38)

- Start 2026-10-04 08:11:06 CEST, Text ab 08:45:17 CEST (date). Arbeitsfeld: ARBEITSFELD.md (alle Zwischenstaende,
  Abrufprotokoll mit Vorhersagen, Gestrichenes).
- 12 WebFetch-Abrufe von 15 (einer davon Fehlschlag), keine Websuche. Keine Rechnung auf der .69; lokal kein python,
  awk oder perl. PDFs hat das Abrufwerkzeug selbst unter ~/.claude/projects/.../tool-results/ abgelegt; gelesen habe ich
  sie als Seitenbild oder mit pdftotext auf stdout. Ich habe keine Datei im Scratchpad angelegt.
- Kennzeichen: [S] an der Quelle gelesen; [L] Gedaechtnis; [L?] unsicher; [ES] eigener Schluss bzw. eigene Rechnung;
  [H] Hypothese. Alles ist Theorie, Literatur oder synthetische Rechnung; nichts davon ist eine Messung.

## 1. Ergebnis zuerst

**Kurzfazit (10 Zeilen):**

- Traegt der Einwand? **Teilweise: gegen Johnstons unveraenderte 4D-Form ja, gegen das Ereignis-Netz an sich nein.**
- Die Polformel stimmt und ist fuer m^2/sqrt(rho) -> 0 asymptotisch exakt. Johnston 2014 hat denselben Term schon,
  nur nicht aufsummiert. Die Rate je Eigenzeit ist 0,61 m^3 l^2, die Hochrechnung stimmt.
- Die vorgeschlagenen Abhilfen tragen nicht: Reelle a, b helfen nicht, Glaettung beschleunigt um (l_k/l)^2.
- Ursache ist der Massenterm ausserhalb des Kerns. Masselos ist das Mittel stabil; BD mit naiver Masse zerfaellt
  mit gleicher Rate. Die Literatur legt die Masse ins Argument; die Kausalmengen-Form ist offen.
- Bekannt ist nur eine andere 4D-Instabilitaet (BD, UV, masselos); eine stabile 4D-Familie ist nicht gefunden.
- Einzelnetze wachsen kurzzeitig wie das Mittel. Fuer einen Higgs-Skalar waeren es ~2,6 Jahre je e-Faltung [ES/H].

**Einzelheiten:**

1. **Die Rechnung stimmt [ES, S].** Ich komme unabhaengig auf Im omega = (sqrt 6/4) m^4/(omega sqrt rho). Johnstons
   eigene Korrekturterme von 2014 stimmen damit Term fuer Term ueberein. Er hat sie aber nur als formale Reihe
   geschrieben und nicht zum Anwachsen aufsummiert. Fuer m^2/sqrt(rho) -> 0 ist die Formel asymptotisch exakt.
   - Je Eigenzeit ist die Rate lorentzinvariant (sqrt 6/4) m^3 l^2 mit l = rho^(-1/4).
   - Elektron ~3e6 Weltalter, Top ~1 Jahr: beide Zahlen stimmen.
2. **Haerter [ES]:**
   - Die zwei Abhilfen aus ERGEBNIS Abschnitt 8 tragen nicht. Reelle Sprung- und Haltamplituden koennen das Anwachsen
     nicht beseitigen.
   - Glaetten mit einer Nichtlokalitaetsskala l_k (Sorkin) beschleunigt es um (l_k/l)^2.
   - Fuer einen Skalar mit Higgsmasse waere die e-Faltungszeit ~2,6 Jahre, also ~5e9 e-Faltungen ueber das Weltalter.
     Das gilt nur, wenn das Mittel die wirksame Dynamik ist [ES/H].
3. **Enger [ES, S]:** Das Anwachsen ist kein Fehler des Ereignis-Netzes an sich. Es ist eine Eigenschaft davon, wie
   Johnstons 4D-Pfadsumme die Masse einbaut, naemlich ausserhalb des nichtlokalen Kerns.
   - Masselos ist Johnstons Mittel stabil.
   - Mit dem Benincasa-Dowker-Operator (BD) gilt exakt B~ = Z^4 k~ (Johnston 2010). Damit zerfaellt ein massiver
     BD-Skalar mit derselben Rate, mit der Johnstons Mittel waechst.
   - Die Literatur legt die Masse ins Argument, f(box + m^2) (Belenchia, Benincasa, Liberati 2015). Wie man das auf
     der Kausalmenge baut, ist dort ausdruecklich offen.
4. **Literaturlage [S]:**
   - Eine 4D-Instabilitaet ist bekannt, aber eine andere: die BD- bzw. GCB-Operatoren sind schon masselos instabil,
     an der Nichtlokalitaetsskala (Aslanbeigi, Saravani, Sorkin 2014).
   - Eine stabile 4D-Familie wurde nicht gefunden (ASS 2014; Surya 2019 "open question"). Nach Recherchestand gibt es
     auch bis heute keine (24-Monats-Abfrage, mit Luecke).
   - Das Anwachsen von Johnstons 4D-Mittel ist nach Recherchestand nirgends beschrieben.

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | betrifft | Verstoss | Fundstelle |
|---|---|---|---|
| V1 | E3 und ERGEBNIS Abschn. 8 | **Glaettung hilft nicht, sie schadet.** Das geglaettete Mittel ist dieselbe Formel mit rho_k < rho statt rho (ASS S. 10). Fuer Johnstons Linkkern heisst das Im omega ~ 1/sqrt(rho_k), also Faktor (l_k/l)^2 schneller. Mit l_k = 1e-19 m (LHC-Grenze) waere ein Skalar mit Elektronenmasse in ~3e-8 s e-fach gewachsen. **Reelle a, b helfen ebenfalls nicht:** Die Polbedingung wird k0~(Z) = -1/M^2 mit reellem M^2, der Imaginaerteil -pi eps M^4 bleibt. | [ES] Arbeitsfeld 2b; [S] ASS 2014 S. 9-10 |
| V2 | E3 | **Glaettung macht 4D-Operatoren nicht nachweislich stabil.** ASS fanden keine stabile Wahl: "we have not been able to find any choice that would make [it] stable". Surya 2019: "still an open question". In den letzten 24 Monaten nach Recherchestand nichts Gegenteiliges. | [S] ASS 2014 S. 17; Surya 2019 lokal Z. 7403-7409; A6, A12 |
| V3 | nicht erwartet | **Johnstons Mittel und der BD-Operator sind exakt verknuepft:** box^2 K_R = B-quer (Johnston 2010, (A.62); 2014, (111)), also B~(Z) = Z^4 k~(Z). Ich habe das gegen ASS (2.17) in zwei UV-Ordnungen nachgeprueft. In der IR-Ordnung steht derselbe Term p^4 ln p^2, aber mit entgegengesetztem Vorzeichen: BD + naive Masse **zerfaellt** mit Im omega = -(sqrt 6/4) m^4/(omega sqrt rho), Johnston **waechst** mit +(sqrt 6/4) m^4/(omega sqrt rho). | [S] Johnston 2010 Anhang A.3.2; 2014 (109)-(112); ASS (2.17); [ES] Vorzeichen |
| V4 | E2 | **Die bekannte 4D-Instabilitaet hat ein anderes Regime.** Bei ASS liegt die instabile Nullstelle bei Z = rho^(-1/2) p.p ~ 3,8 - 25,4 i, also ohne Masse und an der Nichtlokalitaetsskala. Bei k = 0 ist das omega ~ rho^(1/4) (3,3 + 3,8 i) [ES]. Unseres ist IR, nur massiv, mit Rate ~ m^3 l^2. | [S] ASS S. 8 Abb. 3a; [ES] |
| V5 | E3 | **Die Literatur-Abhilfe fuer den Massenterm** ist, die Masse ins Argument zu legen. Die naive Form "does not admit plane wave solutions ... with k^2 = -m^2", deshalb f(box + m^2). Auf der Kausalmenge: "It remains an interesting open issue". Die BBL-Abhilfe fuer die UV-Moden (Wheeler-Propagator) hilft bei uns nicht: Unser wachsender Pol ist das Teilchen selbst. | [S] BBL 2015 Abschn. 3, Fussnote 10, Abschn. 6; [ES] |
| V6 | E4 | Johnston 2014 hat die Korrektur erster Ordnung bereits. A1 in (100) ist bitgleich mit meinem eps [ln(Z^2/sqrt c) + C']. Er behandelt sie als formale Reihe; in (102) steht der saekulare Term box G_m * box G_m. Von Anwachsen ist keine Rede. E4 bleibt im Wortlaut wahr. Neu sind nur die Aufsummierung und die Folgerung. | [S] Johnston 2014 S. 15, (95)-(102) |
| V7 | E5 | **Fuer Johnstons Propagator ist das Mittel wohl die relevante Groesse.** Johnston berichtet fallende Varianz mit rho ("cancellations of random fluctuations"). Im 4D-Lauf ist das Anwachsen je Saat (Median G 1,69 bis 2,09) so gross wie das des Mittels (1,63 bis 1,98). E5 hoffte das Gegenteil. Ueber Zeiten ~1/Gamma ist das nicht gezeigt. | [S] Johnston 2014 Schluss; 2010 S. 46; [E] ERGEBNIS Tab. 3.3 |

## 3. Teil 1: Gegenpruefung am Schreibtisch

### 3.1 Nachrechnung (Einzelschritte im Arbeitsfeld, Abschnitt 2)

- **Erwartungswert [ES]:**
  - Die offenen Intervalle entlang einer Kette sind paarweise disjunkt. Die Leer-Wahrscheinlichkeit faktorisiert
    deshalb exakt, und die Mecke-Formel gibt E[#Pfade] = rho^(n-1) mu^(*n).
  - Daraus folgt K_P~ = a mu~/(1 - a b rho mu~), mit b = -m^2/rho also k~/(1 + m^2 k~). Gleich Johnston 2010 (3.45)
    [S].
- **Fouriertransformierte [ES, S]:** Bei omega = i Omega und k = 0 ergibt das innere Integral
  int sinh^2(chi) e^(-z cosh chi) dchi = K1(z)/z. Daraus folgt k~ = (4 pi a/Z) int tau^2 e^(-c tau^4) K1(Z tau) dtau,
  c = pi rho/24.
  - Das ist ASS (3.7) mit D = 4 (dort nach Dominguez/Trione 1979).
  - Zweig nach ASS (3.10): zukunftsgerichtet heisst Z^2 - i0.
  - Der Code (amu, F_rho) rechnet genau so.
- **Polformel [ES]:**
  - Aus K1(x) = 1/x + (x/2) ln(x/2) + (x/4)(2 gamma - 1) + ... folgt
    k~ = 1/Z^2 + eps [ln(Z^2/sqrt c) + C'] + O(eps Z^2/sqrt c), mit eps = sqrt 6/(2 pi sqrt rho) und
    C' = (3/2) gamma - 1 - 2 ln 2.
  - Johnston 2014 (100) hat denselben Ausdruck: (3/(2 pi sqrt 6)) [3 gamma - 2 - ln(2 pi rho/(3 s^2))]/sqrt(rho) mit
    s = Z^2. Ausmultipliziert identisch [S].
  - Die Nullstelle von 1 + m^2 k~ bei Z^2 = -m^2 + delta liefert delta = m^4 eps [ln(m^2/sqrt c) - i pi + C'].
  - Daraus Im omega = pi m^4 eps/(2 omega0) = (sqrt 6/4) m^4/(omega0 sqrt rho), bei omega0 = sqrt(k^2 + m^2).
  - Im delta < 0, also liegt die Nullstelle auf dem physikalischen Blatt: echtes Anwachsen, kein Resonanzpol.
- **Lorentz-Probe [ES]:** omega0 = gamma m gibt die Ruherate geteilt durch gamma. Je Eigenzeit gilt also
  (sqrt 6/4) m^3 l^2. Das passt dazu, dass Poisson-Streuung in der Verteilung lorentzinvariant ist.
- **Masselos [ES]:** K_P~ = k~ hat keinen Nenner. Der Kern ist beschraenkt und retardiert, also ist k~ in
  Im omega > 0 analytisch. Ohne Masse gibt es keine Pole und kein Anwachsen. Im ASS-Kriterium (3.30) heisst das:
  g_J = -1/k~ hat keine Nullstelle.
- **Gegenprobe am Lauf [ES]:** Die Norm waechst wie e^(2 Gamma Delta t), mit Delta t = 1,5:
  - rho = 16: 1,58 gegen gemessen G = 1,63 / 1,68
  - rho = 4: 2,09 gegen 1,87 / 1,98

### 3.2 Hochrechnung

- **Gueltigkeit fuer m^2/sqrt(rho) -> 0 [ES]:**
  - Die Reihe in Z^2/sqrt(c) konvergiert; jede Ordnung bringt einen Faktor m^2/sqrt(rho) (mit Log).
  - Relativer Fehler: O((m^2/sqrt rho) ln(sqrt rho/m^2)). Bei Planckdichte sind das ~1e-45 (Elektron) bzw. ~1e-34
    (Top).
  - Weitere Nullstellen gibt es dort nicht: Fuer |Z| >> c^(1/4) gilt k~ ~ 8 pi a/Z^4, sonst k~ ~ 1/Z^2. Deshalb ist
    |m^2 k~| << 1 ueberall ausser an der Massenschale. Das ist eine Groessenordnungsrechnung, nicht streng.
- **Einsetzen omega ~ m:** fuer ruhende Teilchen richtig (k = 0, omega0 = m). Damit gilt
  Gamma = 0,612 (m c^2/hbar)(m/m_P)^2. Die Einheiten stimmen (1/s).
- **Zahlen (Kopfrechnung) [ES]:**

  | Teilchen (als freier Skalar) | e-Faltungszeit bei l = l_P |
  |---|---|
  | Elektron 0,511 MeV | 1,2e24 s, rund 2,8e6 Weltalter |
  | Myon | 1,4e17 s, rund 0,3 Weltalter |
  | Tau | rund 0,9 Mio. Jahre |
  | W / Z | rund 10 / 7 Jahre |
  | Higgs 125,1 GeV | rund 2,6 Jahre |
  | Top 172,7 GeV | 3,1e7 s, rund 1 Jahr |

- **Grenzen der Hochrechnung [ES]:**
  - Sie gilt fuer einen freien Skalar mit Johnstons unveraenderten Amplituden. Elektron, Myon und Top sind Fermionen;
    fuer sie gibt es keinen 4D-Johnston-Kern. Das einzige elementare Skalarfeld ist das Higgs.
  - **l = l_P ist eine Annahme:** Surya 2019 setzt l_c = l_P ausdruecklich gleich [S]. Mit reduzierter Plancklaenge
    ist die Rate 25-mal groesser.
  - **Higgs-Folgerung [ES/H]:** Woertlich genommen haette die linearisierte Higgs-Dynamik um das Vakuum wachsende Moden.
    Vertraeglich mit dem Weltalter waere das nur fuer l < ~1,4e-5 l_P. Die Folgerung haengt an drei ungeprueften
    Annahmen: Das Mittel ist die wirksame Dynamik, das Feld ist frei, und QFT-Effekte (SJ-Zustand, Wechselwirkung)
    aendern nichts.
  - Ein echtes Top zerfaellt in 5e-25 s; das Anwachsen ist dafuer bedeutungslos. Die Hochrechnung ist eine Aussage
    ueber das Feld, nicht ueber das Teilchen.

### 3.3 Physikalische Lesart: Mittel oder Einzelrealisierung

- **Was die Literatur sagt [S]:**
  - ASS Fussnote 3: "Which behavior is relevant physically?" Fuer den BD-Operator wachsen die Fluktuationen einer
    einzelnen Streuung mit rho. Ausweg dort: eine Nichtlokalitaetsskala, damit die Mittelung in jeder einzelnen
    Kausalmenge stattfindet. Danach rechnen ASS und BBL nur mit dem gemittelten Kontinuumsoperator.
  - Fuer Johnstons Propagator dagegen faellt die Varianz mit rho (Johnston 2010 S. 46 in 1+1; 2014 Schluss: "leading
    to cancellations of random fluctuations").
- **Unser Lauf [E, aus ERGEBNIS]:** Das Rauschen faellt auch in 4D (rho^(-0,16)). Das Wachstum je Saat ist nicht
  kleiner als das des Mittels.
- **Lesart [ES/H]:**
  - E[phi] ist das kohaerente Feld eines Zufallsmediums, mit Dyson-Form 1/(Z^2 + m^2 + Sigma) und
    Sigma = -eps Z^4 [ln(Z^2/sqrt c) + C'].
  - In gewoehnlichen Zufallsmedien daempft Im Sigma, weil Energie in den diffusen Anteil streut. Johnstons Gewichte
    haben keinen Erhaltungssatz, der dieses Vorzeichen erzwingt.
  - Jensen: E|phi|^2 >= |E phi|^2. Waechst das Mittel, waechst die mittlere Leistung mindestens mit 2 Gamma.
  - Eine typische Einzelrealisierung kann langsamer wachsen (geglueht gegen gequencht). Die Korrektur je Schwingung
    stammt aber aus der mittleren Linkdichte nahe am Lichtkegel, also aus sehr vielen Elementen.
  - **[H] Eine Einzelrealisierung waechst vermutlich mit derselben Rate.** Gezeigt ist das nur fuer 2/m Laufstrecke.

### 3.4 Wo ich nicht folgen kann bzw. nichts geprueft habe

- L-a: Johnston 2008 (3.13) bis (3.15) habe ich nicht selbst gelesen; ich stuetze mich auf die Doktorarbeit (3.45),
  (3.57) und auf eine eigene Herleitung.
- L-b: Die zweite Ordnung ist nur skizziert. Die numerischen Pole bei rho = 16 (1,0545 + 0,1523 i) treffe ich mit
  erster Ordnung nur im Imaginaerteil (0,153). Im Realteil liegt die erste Ordnung bei 1,092; erst mit zweiter Ordnung
  komme ich naeherungsweise heran (rund 1,06 + 0,16 i). **Die 1-%-Uebereinstimmung bei rho = 16 ist teils Zufall.**
  Bei rho = 4 bzw. 8 liegt die erste Ordnung 25 % bzw. 9 % ueber der Numerik. Fuer die Hochrechnung spielt das keine
  Rolle.
- L-c: pol_k (Newton mit Differenzenquotient) habe ich nicht nachgerechnet.
- L-d: Ob das Mittel die wirksame Dynamik ist, ist eine Modellfrage (3.3).
- L-e: Die Vorzeichen der BD-Spektraldichte jenseits der IR-Ordnung habe ich nicht geprueft. BBL: in 4D "not positive
  definite".

## 4. Teil 2: Literatur

### 4.1 Erwartungen mit Ausgang

| Nr | Erwartung | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | Polformel 1. Ordnung richtig; ~ m^3 l_P^2 | **eingetroffen** | 3.1, 3.2; [S] Johnston 2014 (100), (101); ASS (3.7), (3.10) |
| E2 | 4D-Instabilitaet bekannt (ASS) | **teilweise**: im Wortlaut ja, in der Sache ein anderes Regime (V4) | [S] ASS Abstract, S. 8, 16-17; Surya 2019; BBL 2015 Abstract |
| E3 | Glaettung macht stabil, Preis l_k >> l_P | **nicht eingetroffen** (V1, V2, V5) | [S] ASS S. 17; Surya 2019; [ES] 2b |
| E4 | Fuer Johnstons Pfadsumme nicht beschrieben | **eingetroffen**, nach Recherchestand; Korrekturterme selbst bekannt (V6) | [S] Johnston 2010 S. 48; 2014; Shuman 2023; Hinrichsen/Kastrati 2026; A6, A12 |
| E5 | Mittel nicht die ganze Physik; Literatur meist Mittel | **teilweise** (V7) | [S] ASS Fn. 3, S. 10; Johnston 2014 Schluss |

### 4.2 Bekannte Instabilitaeten und Anwachsen (mit Bedingungen) [S]

- **4D-BD- bzw. GCB-Operatoren (ASS 2014):**
  - Kriterium (3.30): keine Nullstelle von g~(Z) fuer Z != 0. Der minimale 4D-Operator hat genau zwei instabile
    Nullstellen (S. 16-17).
  - Andere Koeffizienten aendern deren Zahl, aber "we have not been able to find any choice that would make [it]
    stable".
  - Der 2D-Operator ist bewiesen stabil (S. 6).
  - ASS raten, statt ebener Wellen das Spaetzeitverhalten von G_R zu pruefen (S. 18). Genau das hat KAUSAL-WELLE-4D
    getan.
- **Fussnote 7 (ASS):** Eine Instabilitaet mit kosmologischer Wachstumszeit waere "irrelevant physically"; einen
  solchen 4D-Operator fanden sie nicht.
  - Johnstons Mittel ist so ein Fall, aber nur fuer leichte Felder [ES]. Fuer Felder ab etwa Myonmasse liegt die
    Wachstumszeit unter dem Weltalter.
- **Nichtlokale QFT (BBL 2015):** "the unstable modes of the non-local d'Alembertian are propagated via the so called
  Wheeler propagator". In 4D ist die Hamiltonfunktion nicht positiv definit; "potential issues with the quantum theory
  remain".
- **Fluktuationen:**
  - Fuer den BD-Operator wachsen sie mit rho (Sorkin 2007, wiedergegeben in ASS Fn. 3, Johnston 2010 S. 80,
    BBL Einleitung, PDF-S. 3).
  - Fuer Johnstons Propagator fallen sie (Johnston 2010, 2014).
- **Weitere 4D-Maengel der Pfadsumme (Johnston 2010 S. 69-71):**
  - Auf R x T^3 sterben die Links in der fernen Zukunft aus.
  - In gekruemmter Raumzeit gibt es keine "tails"; "the 3+1 dimensional model would require modification".
- **Johnstons Pfadsumme bei endlicher Dichte:** Die Korrekturterme stehen in Johnston 2014. Von Instabilitaet oder
  Anwachsen ist nirgends die Rede, auch nicht bei Shuman 2023 und Hinrichsen/Kastrati 2026 (1+1). Fuer diese Aussage
  gilt "nach Recherchestand nicht belegt", nicht "widerlegt".

### 4.3 Abhilfen

| Abhilfe | Quelle | Wirkung auf unser Anwachsen | Kennz. |
|---|---|---|---|
| Glaetten mit Nichtlokalitaetsskala l_k (Sorkin; ASS Anhang D; Dowker/Glaser) | ASS S. 9-10; Surya (36), (37) | daempft Fluktuationen; **beschleunigt das Anwachsen um (l_k/l)^2** | [S] / [ES] |
| a, b bei endlicher Dichte reell anpassen | ERGEBNIS Abschn. 8 | **unmoeglich**: verschiebt nur Re omega | [ES] |
| Masse ins Argument, f(box + m^2) | BBL 2015 Abschn. 3 | reelle Massenschale (Verzweigungspunkt dort), kein Anwachsen; Kausalmengen-Form offen (BBL Fn. 10) | [S] / [ES] |
| Wheeler-Propagator bzw. Konturwahl (Barnaby/Kamran) | BBL 2015 Abschn. 6, Fn. 18 | hilft gegen komplexe Zusatzmoden, **nicht** gegen unseren Pol: Der ist das Teilchen selbst | [S] / [ES] |
| Mehrschicht-Spruenge mit sigma = sum a_n = 0 (z. B. Links 2a, 1-Element-Intervalle -2a) | eigener Vorschlag; Rahmen bei Shuman 2023 ("average jump amplitudes") und ASS (3.14a) | erster Imaginaerteil faellt weg; Rest Gamma_Ruhe ~ (3/16) m^5 l^4 (bei rho = 16 ~0,015 statt 0,152); Preis vermutlich mehr Rauschen | [ES] / [H] |
| Vorzeichen umkehren (sigma < 0) | eigener Vorschlag | Zerfall statt Wachstum, gleiche Groesse | [ES] |
| Lokaler d'Alembert-Operator (Boguna/Krioukov 2025) | arXiv 2506.18745, nur Abstract | Stabilitaet und Masse nicht geprueft | [S Abstract] / [L?] |

- **Herleitung zur Mehrschicht-Abhilfe [ES]:**
  - Fuer Spruenge entlang n-Element-Intervallen faktorisiert der Erwartungswert weiter, denn die Intervalle sind
    disjunkt.
  - Wegen int tau^3 mu_n dtau = 1/(4c) fuer jedes n ist der ln Z^2-Koeffizient (pi/(4c)) sum a_n.
  - Normierung: sum a_n Gamma(n + 1/2)/n! = sqrt(c)/pi.
  - Die 4D-BD-Koeffizienten (4, -36, 64, -32)/sqrt 6 haben ebenfalls Summe 0 [S ASS (2.12)].

### 4.4 Beobachtungsschranken

- **Auf die Nichtlokalitaetsskala BD-artiger Theorien [S, Belenchia u. a. 2016]:**
  - LHC 8 TeV: "lk <= 10^-19 m"
  - Optomechanik im Grundzustand: "lk < 2 x 10^-15 m"
  - Erste Schaetzungen aus Ref. [26] dort (thermische kohaerente Zustaende, schlimmster Fall): 2e-22 m bis 1e-29 m;
    "best forecast falls short by roughly six orders" von l_P.
- **Higgs:** de Brito/Eichhorn/Fausten 2023 [S, nur Abstract]: Die nichtlokalen Aenderungen ziehen den Landau-Pol an
  die Nichtlokalitaetsskala heran. Sie bezweifeln, dass sich Nichtlokalitaets- und Diskretheitsskala trennen lassen.
- **Swerves:** Kaloper/Mattingly 2006 begrenzen Swerves (nach Surya 2019 [S lokal]). Die Arbeit selbst habe ich nicht
  gelesen. Sie betrifft Punktteilchen, nicht Wellen.
- **Auf Johnston-artiges Massenschalen-Anwachsen:** keine Literaturschranke gefunden. Eigene Konsistenzabschaetzung
  [ES/H]:
  - Mit Higgs-Skalar und Weltalter ergibt sich l < ~1,4e-5 l_P, falls das Mittel die Dynamik ist.
  - Mit Glaettung l_k = 1e-19 m waere selbst ein Elektronmassen-Skalar nach ~3e-8 s e-fach gewachsen.
  - Kurz: Johnstons Form mit geglaettetem Kern ist mit jeder l_k >> l_P unvertraeglich.

## 5. Regime und Moderatoren

| | Johnstons Mittel (Links, Masse ueber geometrische Reihe) | BD/GCB-Mittel, masselos | BD-Mittel + naive Masse | BBL f(box + m^2) |
|---|---|---|---|---|
| masselos | stabil (k~ analytisch) [ES] | **instabil**, Nullstellen bei abs(p.p) ~ 25 sqrt(rho) [S ASS] | wie links | wie links |
| Massenschale | **Wachstum** (sqrt 6/4) m^4/(omega sqrt rho) [ES, S Johnston 2014] | - | **Zerfall**, gleicher Betrag [ES aus S] | reell, Verzweigungspunkt [S BBL] |
| Rate bei rho -> inf | -> 0 wie rho^(-1/2) | -> unendlich wie rho^(1/4) | -> 0 | 0 |
| Rauschen Einzelnetz | faellt mit rho [S Johnston; E] | waechst mit rho ohne Glaettung [S] | wie links | Kausalmengen-Form offen |

- **Moderatoren (Regel 1):**
  - Masse: Johnstons Instabilitaet gibt es nur massiv, die BD-Instabilitaet auch masselos.
  - Bauart: geometrische Reihe im Linkkern gegen alternierende Schichtsumme.
  - Ort der Masse: ausserhalb oder innerhalb der nichtlokalen Funktion.
- **Kopplungsgroesse (Regel 6) [ES]:** Zur Verschiebung der Massenschale fuehren drei Wege: Johnstons Reihe, BD plus
  naive Masse, und geglaettete Kerne plus naive Masse. Alle haengen an derselben Groesse.
  - Diese Groesse ist der Sprung (Imaginaerteil) des masselosen nichtlokalen Kerns ueber den zukunftsgerichteten
    zeitartigen Schnitt bei p^2 = -m^2, also die Spektraldichte des Kontinuumsanteils.
  - Ist sie negativ (Johnston: Spektraldichte -eps, also sigma = sum a_n > 0), waechst die Welle. Ist sie positiv
    (BD; Pfadsumme mit sigma < 0), zerfaellt sie. Ist sie null (sigma = 0), bleibt nur ein Rest hoeherer Ordnung.
  - Der einzelne Baustein (Links, Schichten, Glaettung) entscheidet nur ueber Vorzeichen und Groesse.

## 6. Unterscheidungspunkte (Regel 2)

- **Mittel gegen Einzelrealisierung:** Die Unterscheidung braucht t >~ 1/Gamma in einer grossen Einzelstreuung. Bei
  rho ~ 1 bis 2 und m = 1 sind das ~10/m Laufstrecke. Das verlangt N >> 2e4, mit heutigem Code praktisch
  unzugaenglich. Erreichbar ist nur der Kurzzeitvergleich, und der zeigt keinen Unterschied (V7).
- **Johnston-IR gegen BD-UV:** schon getrennt. Masselos (Johnston stabil, BD instabil) und im Gang mit rho
  (rho^(-1/2) gegen rho^(1/4)).
- **Mechanismus "Vorzeichen von sigma":** trennbar in einer kleinen Rechnung, Vorschlag in Abschnitt 8. Bei
  sigma = +a / 0 / -a lauten die Vorhersagen Wachstum / fast nichts / Zerfall.
- **Glaettung hilft gegen Glaettung schadet:** Fuer das Mittel ist das durch die Formel entschieden (schadet). Fuer das
  Rauschen gilt das Gegenteil. Beides zusammen ist ein echter Zielkonflikt, keine offene Frage.

## 7. Bedeutung fuer Ueberleitung 3 und Finns Weiche

- **Ue3:** Der Ueberleitungssatz sagt: "Teilchen muessen ueber viele Punkte mitteln, um nicht zu zittern". Das traegt
  in 3+1 weiter, denn das Rauschen faellt.
  - Hinzu kommt ein neuer Knackpunkt: **Mitteln reicht nicht; wie die Masse eingebaut wird, entscheidet ueber
    Stabilitaet** [ES].
  - Mit Johnstons unveraenderter 4D-Form ist Ue3 fuer schwere Skalare bei l ~ l_P nicht haltbar, falls das Mittel die
    Dynamik ist [ES/H]. Gegen das Ereignis-Netz an sich spricht das nicht.
- **Finns Weiche, Zweig (B):**
  - Der Befund trifft eine Konstruktion, nicht den Zweig.
  - Er zeigt aber ein Muster: Keine bekannte 4D-Skalardynamik auf Kausalmengen erfuellt zugleich drei Bedingungen,
    naemlich (i) aus der Kausalmenge abgeleitet, (ii) masselos stabil und (iii) ohne Massenschalen-Verschiebung.
    - Johnston: (i) und (ii) ja, (iii) nein.
    - BD: (i) ja, (ii) nein, (iii) Zerfall.
    - BBL: (iii) ja, (ii) nur ueber Wheeler-Quantisierung, (i) offen.
  - (B) in 3+1 ist damit "offen, mit bekannten Problemen", nicht "traegt".
- **Vorschlag fuer WEICHE-STAND, Zeile Wellen, Spalte (B):** "3+1: im Mittel wie Johnstons Erwartung; diese waechst fuer
  massive Felder mit 0,61 m^3 l^2 je Eigenzeit und ist masselos stabil (KAUSAL-WELLE-4D, KAUSAL-4D-STABIL-L)."
- **Gegenseite:** Fuer (A) und (C) ist nichts Vergleichbares gerechnet. Der Befund stuetzt (A) oder (C) also nicht,
  er belastet nur (B) in Johnstons Form.

## 8. Vorschlag Rechenkarte: KAUSAL-4D-SCHICHT-1 (kann scheitern; je Lauf <= 10 min auf der .69)

- **Frage:** Steuert sigma = sum a_n das Anwachsen wie vorhergesagt, und was kostet die Abhilfe an Rauschen?
- **Drei Varianten auf derselben Streuung:**
  - V-J: Johnston, Links mit a.
  - V-0: Links 2a, 1-Element-Intervalle -2a, also sigma = 0.
  - V-M: Links 3a, 1-Element-Intervalle -4a, also sigma = -a.
  - In allen drei Varianten b = -m^2/rho und dieselbe Normierung (sum a_n Gamma(n + 1/2)/n! gleich wie bei Johnston).
- **Technik:**
  - L1 = C und (C C == 1) faellt aus demselben GEMM-Produkt ab, das schon fuer die Links laeuft (Zaehler in float32
    exakt).
  - Rekursion psi = J - (m^2/rho) Phi^T psi, phi = (1/rho) Phi^T psi.
  - Gebiet D ist kausal konvex, deshalb sind auch die 1-Element-Intervalle exakt.
- **Teil A (Kontinuum, ein Lauf, < 10 min):**
  - Pole von 1 + m^2 k~_gen bei rho = 4, 8, 16 und k = 0, p.
  - Erwartung E[phi] an den 18 Pruefpunkten fuer alle drei Varianten (kontinuum4d.py mit mu_n statt mu_0).
  - Zusaetzlich das Argumentprinzip wie ASS (3.33), um weitere Nullstellen in der oberen Halbebene zu zaehlen.
- **Teil B (Felder):**
  - rho = 16 mit 12 Saaten (je ~150 s, also 4 Laeufe zu je 3 Saaten) und rho = 8 mit 12 Saaten (ein Lauf).
  - Messung wie KAUSAL-WELLE-4D, je Variante als eigene Spalte.
- **Vorab-Erwartungen (Schreibtisch, [ES], vor jeder Rechnung):**
  - KS0 (Kontrolle): Das Saatmittel von V-J trifft Johnstons Erwartung an >= 15 von 18 Punkten in 3 SE.
  - KS1: Im omega(V-0, rho = 16, k = 0) liegt in [0; 0,05] (Schaetzung 0,015 aus (3/16) M^6/(omega rho) mit
    M^2 = m^2/(1 - eps m^2)).
    - Gang mit rho: von 4 bis 16 faellt der Wert mindestens um den Faktor 3; Schaetzung 0,08 / 0,034 / 0,015.
    - V-M: kein Pol mit Im omega > 0 nahe der Massenschale; die Erwartung faellt gegen das Kontinuum ab.
  - KS2: Das Saatmittel von V-0 trifft seine eigene Erwartung an >= 15 von 18 Punkten. Der Zuwachs
    abs(E phi)/abs(Kontinuum) von t = 2,0 bis 3,2 liegt bei <= 1,10 (V-J: 1,25), bei V-M unter 1.
  - KS3 [H, Preis]: Die relative Streuung je Saat ist bei V-0 groesser als bei V-J (0,33 bei rho = 16); Prognose 0,5
    bis 1,0.
- **Scheitern:**
  - KS1 scheitert, wenn Im omega(V-0) > 0,075 ist, wenn V-M nicht das Vorzeichen wechselt, oder wenn eine weitere
    Nullstelle mit Im omega > 0,05 bei abs(omega) < 10 auftritt.
  - KS2 scheitert bei Zuwachs > 1,15.
  - KS3 ist in beide Richtungen informativ: unter 0,33 heisst "kein Preis", ueber 1,5 heisst "unbrauchbar".
- **Bedeutung:**
  - Bestehen KS1 und KS2, ist das Anwachsen eine reparierbare Kerneigenschaft. Ue3 bleibt in diesem Punkt offen, und
    als naechster Schritt folgt die Kausalmengen-Form von f(box + m^2).
  - Scheitert KS1, hat die 4D-Pfadsumme keine einfache Reparatur, und (B) braucht eine andere Massenkopplung.
- **Grenzen:** Bei rho <= 16 ist m^2/sqrt(rho) >= 0,25. Die Asymptotik ist dort nur grob, deshalb sind die Schwellen
  weit gesetzt. Die Laufstrecke bleibt 2/m.

## 9. Gegensweep-Befunde (Regel 4)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **Projekt hatte das Thema schon (geprueft):**
   - Suryas Living Review liegt seit Runde 22 als Text im Projekt
     (RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt). Er nennt die ASS-Instabilitaet in 4D (Z. 7403) und die
     "critical instabilities" von BBL (Z. 9065).
   - Der grep ueber aslanbeigi, saravani, benincasa, nichtlokal und nonlocal gibt 109 Dateien; fast alle sind
     Code-Variablen oder Rohdaten. Inhaltlich zaehlen nur Surya, UEBERLEITUNGEN-EMERGENZ (nur [L]-Verweise) und
     RUNDE-38.md Z. 105 ("Kein Benincasa-Dowker-Vergleich").
   - Mit KAUSAL-WELLE verknuepft hatte den Review niemand.
2. **Planckdichte (geprueft):** Surya 2019 setzt l_c = l_P ausdruecklich als Annahme. Mit reduzierter Plancklaenge
   ist die Rate 25-mal groesser (Top ~2 Wochen, Higgs ~5 Wochen, Elektron ~1e5 Weltalter).
3. **WebFetch-Zusammenfassungen (geprueft, Methodenbefund):**
   - Bei Hinrichsen/Kastrati 2026 behauptete der Zusammenfasser Pole, Daempfung und Wachstumsinstabilitaeten. Im Text
     steht davon nichts.
   - Alle [S] dieses Dossiers stammen aus lokal gelesenem Text bzw. Seitenbildern. Ausnahme sind Abstracts aus der
     arXiv-API; sie sind als "nur Abstract" markiert.
4. **Zeitkonvention im Code (geprueft):** exp(-i omega t) auf einer Linie ueber allen Singularitaeten. Im omega > 0
   bedeutet also Wachstum.
5. **Einzelsaat gegen Mittel (geprueft):** ERGEBNIS Tab. 3.3, siehe V7.
6. **Vollstaendigkeit der 24-Monats-Abfrage (geprueft, Luecke):**
   - Die arXiv-Abfrage A6 fand 1510.04656 und 1701.07212 nicht, obwohl beide einschlaegig sind.
   - Die INSPIRE-Abfrage A5 schlug fehl: 25 113 fachfremde Treffer, die refersto-Syntax griff nicht.
   - "Nach Recherchestand nicht belegt" gilt deshalb mit dieser Luecke.
7. **Nicht geprueft:**
   - ob der Higgs-Schluss eine QFT-Behandlung uebersteht (Selbstwechselwirkung, SJ-Zustand)
   - ob es ein 4D-Dirac-Analogon gibt
   - ob Dowker/Surya/X 2017 (1701.07212, gekruemmte Raumzeit) etwas zur endlichen Dichte sagt

## 10. Kalibrierung

- **(a) An der Quelle gelesen oder gerechnet:**
  - Johnstons Korrekturterm erster Ordnung [S]; die Identitaet box^2 K_R = B-quer [S], von mir in drei Ordnungen
    gegengeprueft [ES].
  - ASS: 4D-BD instabil, numerisch, "strong evidence"; keine stabile Wahl gefunden [S]. BBL: Massenterm ins
    Argument [S]. Schranken auf l_k [S].
  - Synthetisch gerechnet (nicht gemessen): Die Saatmittel folgen Johnstons Erwartung; G je Saat ~ G des Mittels [E,
    ERGEBNIS].
- **(b) Nuetzlich verdichtet [ES]:**
  - Rate je Eigenzeit (sqrt 6/4) m^3 l^2
  - sigma = sum a_n als Kopplungsgroesse; "Glaettung schadet dem Mittel"
  - Vorzeichengegensatz Johnston gegen BD
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - Die Higgs-Folgerung und das Urteil "unvertraeglich" stuetzen sich auf die Annahme "Mittel = wirksame Dynamik".
    Gestuetzt ist diese Annahme nur kurzzeitig (2/m) und indirekt (fallende Varianz).
  - **Warnzeichen:** Meine Sicherheit, dass der Einwand traegt, ist gewachsen, waehrend sich die Frage in Regime
    zerlegt hat: Masse innen oder aussen, Vorzeichen von sigma, Mittel oder Einzelnetz. Getragen ist der Einwand nur
    gegen Johnstons unveraenderte Form.

## 11. Offene Fragen

1. Waechst eine einzelne Streuung ueber t ~ 1/Gamma wie das Mittel (gequencht gegen geglueht)?
2. Wie sieht f(box + m^2) als Pfadsumme auf der Kausalmenge aus (BBL Fn. 10)? Ist sigma = 0 mit einer weiteren
   Schicht (Rest ~ m^6) ein Weg dorthin?
3. Gibt es eine stabile 4D-Familie (ASS, Surya)? Die 24-Monats-Abfrage hat eine Luecke.
4. Uebersteht die Higgs-Folgerung Wechselwirkung und eine QFT-Behandlung (SJ-Zustand)?
5. Vorzeichen der 4D-BD-Spektraldichte jenseits der IR-Ordnung (BBL: "not positive definite"). Fuer schwere Felder bei
   kleiner Dichte zaehlt das.

## 12. Quellenliste (Abrufstand 2026-10-04, Zeiten aus dem Abrufprotokoll)

- S. Aslanbeigi, M. Saravani, R. D. Sorkin, "Generalized Causal Set d'Alembertians", JHEP 06 (2014) 024,
  arXiv:1403.1622v1. https://arxiv.org/abs/1403.1622 (PDF abgerufen 08:21; gelesen S. 1-21, Seitenbilder) [S]
- S. Johnston, "Quantum Fields on Causal Sets", Doktorarbeit, Imperial College London 2010, arXiv:1010.5514.
  https://arxiv.org/abs/1010.5514 (PDF 08:24-08:30; gelesen 3.7, 3.8, S. 69-71, 80, Anhang A.3.2) [S]
- S. Johnston, "Correction terms for propagators and d'Alembertians due to spacetime discreteness",
  arXiv:1411.2614v2 (2015; laut PDF eingereicht bei Class. Quantum Grav.). https://arxiv.org/abs/1411.2614
  (08:30-08:33; gelesen Abstract, Abschn. 4.3-6, S. 15-16 als Bild) [S]
- S. Johnston, "Particle propagators on discrete spacetime", CQG 25 (2008) 202001, arXiv:0806.3083. Hier nicht selbst
  abgerufen; [S] durch den Code-Agenten (KAUSAL-WELLE-4D, PLAN Abschn. 1).
- A. Belenchia, D. M. T. Benincasa, S. Liberati, "Nonlocal Scalar Quantum Field Theory from Causal Sets", JHEP 03 (2015)
  036, arXiv:1411.6513. https://arxiv.org/abs/1411.6513 (08:30-08:33; gelesen Abstract, Abschn. 3, 6, Fussnoten 7,
  10, 16-18) [S]
- A. Belenchia, D. M. T. Benincasa, S. Liberati, F. Marin, F. Marino, A. Ortolan, "Tests of Quantum Gravity induced
  non-locality via opto-mechanical quantum oscillators", PRL 116 (2016) 161303, arXiv:1512.02083.
  https://arxiv.org/abs/1512.02083 (08:33-08:38; gelesen Abschnitt "Present constraints and forecasts") [S]
- S. Surya, "The causal set approach to quantum gravity", arXiv:1903.11544 (Living Reviews in Relativity 2019 [L]).
  Lokale Textfassung im Projekt, RUNDE-22/geometrie-stand/hilfs/surya-1903.11544.txt, gelesen 08:11-08:17
  (Z. 7318-7420, 7496-7530, 7940-8085, 9060-9080, 9168-9185, Literaturliste) [S]
- R. D. Sorkin, "Does Locality Fail at Intermediate Length-Scales", gr-qc/0703099, in D. Oriti (Hrsg.), Approaches to
  Quantum Gravity, CUP 2009, S. 26-43. Abstract woertlich ueber die arXiv-API (08:40-08:42) [S Abstract]
- F. Dowker, L. Glaser, "Causal set d'Alembertians for various dimensions", CQG 30 (2013) 195016, arXiv:1305.2588.
  Abstract ueber die arXiv-API (08:40-08:42) [S Abstract]
- S. Shuman, "Path Sums for Propagators in Causal Sets", arXiv:2307.08864v2 (2023). https://arxiv.org/abs/2307.08864
  (08:33-08:38; gelesen Abstract, Schluss, grep) [S]
- H. Hinrichsen, A. Kastrati, "Link-based causal set propagators in 1+1 dimensions", arXiv:2604.24812v1 (2026).
  https://arxiv.org/abs/2604.24812 (08:38-08:40; gelesen Abstract, Einleitung, Abschn. V, grep) [S]
- Nur Abstract ueber die arXiv-API (08:33-08:38) [S Abstract]:
  - A. Kastrati, arXiv:2608.18753 (2026)
  - M. Boguna, D. Krioukov, "Local d'Alembertian for causal sets", arXiv:2506.18745 (2025)
  - G. P. de Brito, A. Eichhorn, L. Fausten, "Towards a bound on the Higgs mass in causal set quantum gravity",
    arXiv:2305.07595 (2023)
  - J. Y. L. Jones, Y. K. Yazdi, arXiv:2606.00311 (2026)
  - M. Saravani, arXiv:1801.02582 (2018)
  - A. Belenchia, arXiv:1512.08485 (2015)
- Abfragen:
  - arXiv-API, abs "causal set" mit propagator, Alembertian, nonlocal oder non-local, 40 neueste (A6)
  - arXiv-API, all "causal set" mit stability, unstable, instability oder instabilities (A12)
  - INSPIRE refersto (A5, Fehlschlag)
- Lokal (Projekt): KAUSAL-WELLE-4D (ERGEBNIS, PLAN, code/kontinuum4d.py, lauf-69/kont/kontinuum.json),
  KAUSAL-WELLE-1/ERGEBNIS.md, RUNDE-38/WEICHE-STAND-20261004.md, RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md.

## 13. Einfach gesagt

Wir haben nachgerechnet, ob die Welle auf dem zufaelligen Raumzeit-Netz im Mittel wirklich langsam immer staerker wird,
und ja: Die Rechnung stimmt, und der Erfinder der Methode hatte den entscheidenden Korrekturterm 2014 schon berechnet,
ohne daraus das Anwachsen zu folgern. Das Anwachsen kommt nicht vom Netz selbst, sondern davon, wie die Masse eingebaut
wird; ohne Masse ist alles stabil, und bei einer verwandten Methode verkehrt sich der Effekt sogar in langsames
Abklingen. Fuer leichte Teilchen ist der Effekt winzig; fuer ein Feld so schwer wie das Higgs waeren es nur Jahre, was
nicht zu unserem 13,8 Milliarden Jahre alten Weltall passt, falls das Mittel wirklich die Wirklichkeit beschreibt. Das
bekannte "Glaetten" macht es sogar schlimmer; eine kleine Rechnung kann pruefen, ob eine geaenderte Sprungregel das
Anwachsen abstellt. Alles ist Rechnung und Literatur, keine Messung.
