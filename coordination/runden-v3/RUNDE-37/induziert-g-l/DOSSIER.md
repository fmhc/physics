# INDUZIERT-G-L: Dossier (Literaturkarte, Runde 39, feldforscher)

- Fuer die Leitung claude-primary. Start 2026-10-04 10:07:06 CEST, Text ab 10:31:16 CEST (date).
- 11 von 15 Abrufen (curl, lokale Kopien in quellen/, pdftotext; ein leerer Erstversuch mitgezaehlt). Keine Websuche,
  kein WebFetch, kein python/awk/perl, keine Laeufe. Fundstellen nur aus den lokalen Kopien (Datei, Seite, Zeile).
- Arbeitsdatei mit Vorhersagen vor jedem Abruf und Protokoll: ARBEITSFELD.md.
- **Kennzeichen:** [S] an der lokalen Kopie gelesen; [L] Gedaechtnis; [L?] unsicher; [ES] eigener Schluss;
  [H] Hypothese. Zusaetzlich: [M] eigene Rechnung auf dem Papier (nicht gegengelesen, Unterfall von [ES]); [E] im
  Projekt gerechnet (aus den ERGEBNIS-Dateien uebernommen, hier nicht neu gerechnet).

## 1. Ergebnis zuerst

1. **Das Vorzeichen der induzierten Newton-Konstante ist bei freien Feldern eine Eigenschaft des Reglers, keine der
   Materie allein.** Das Einstein-Glied steht vor kappa^2, also einer Potenzdivergenz. Sein Koeffizient ist
   (1/6 - xi) mal ein "Reglermoment", und das ist nur fuer Regler fest positiv, die eine Funktion des Operators mit
   nichtnegativem Gewicht sind (Eigenzeit). Universell sind nur die Log-Glieder: in 2D die Anomalie, in 4D R^2 und
   Weyl^2. [S Visser 2002; M]
2. **Daraus folgt die Lesart unserer Befunde [ES]:** 2D trifft Polyakov, weil dort nach "Zahl = Volumen" nur das
   universelle Log-Glied uebrig bleibt (Int sqrt(g) R ist topologisch). 4D verfehlt Einsteins Vorzeichen, weil dort
   ein Gitterglied Lambda^2 Int sqrt(g) R uebrig bleibt, dessen Vorzeichen der P1-Delaunay-Regler setzt. Kein
   Satz verbietet ein negatives G fuer diesen Regler.
3. **Die Leitungs-Hypothese "xi_eff > 1/6" haelt im langwelligen Sinn nicht [ES, M]:** Die P1-Steifigkeit hat
   Zeilensumme null (K 1 = 0). Das verbietet ein xi R phi^2 auf jeder Skala, xi_IR = 0. Unsere 2D-Zahl bestaetigt das
   (1,075 P heisst xi_IR = -0,013 +- 0,012). Das 4D-Vorzeichen kommt aus dem UV-Teil (Laengenregel, Netzform, Mass).
4. **Zweites Regime aus der Literatur [S]:** Wenn die Materie im UV asymptotisch frei ist, ist G_ind endlich und
   reglerfrei; fuer QCD kommt es positiv heraus (Donoghue/Menezes 2018). Getrennte Punkte tragen dort, wie bei uns
   auf dem festen Netz, mit dem Anti-Einstein-Vorzeichen bei; positiv macht es der UV-Teil.
5. **Vorschlag:** Karte INDUZIERT-KUGEL-1. Poisson-Punkte auf S^4 (und S^2 als Kontrolle) messen das Vorzeichen des
   induzierten Regge-Glieds an einem exakt kovarianten Ensemble ueber das sqrt(N)-Glied von log det. Rauscharm,
   <= 10 min je Lauf, kann in drei Richtungen scheitern (Abschnitt 8).

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

1. **Zwei Regime statt einer Regel (A6).** Erwartet war "nur der Log-Teil ist universell" (E2).
   - Donoghue/Menezes rechnen G_ind fuer QCD endlich und ohne Regler, mit Gitter-Glueballdaten als Eingabe: "this
     procedure determines that the induced G is positive" (quellen/donoghue-menezes-1712.04468.txt, S. 2, Z. 74) [S].
   - Euklidische Adler-Zee-Formel: 1/(16 pi G_ind) = -(1/96) Int d^4y y^2 <T{Tbar(y) Tbar(0)}> (Gl. 16, S. 3) [S].
     Der euklidische Korrelator ist bei getrennten Punkten positiv (Reflexionspositivitaet [L]). Getrennte Punkte
     tragen also negativ zu 1/G bei; D/M: "Because the glueball contribution is negative" (S. 7, Z. 493) [S]. Das
     positive Ergebnis kommt aus dem UV-Teil, und der "may change sign depending on the values assigned for x0"
     (S. 6, Z. 388) [S].
   - Moderator [ES]: das UV-Verhalten der Spur T. Verschwindet sie logarithmisch (asymptotisch frei), ist G_ind
     endlich und das Vorzeichen dynamisch. Bleibt sie kanonisch (freie Felder, unser P1-Skalar), ist G_ind
     potenzdivergent und das Vorzeichen gehoert dem Regler.
   - Strukturgleichheit mit uns [ES, M]: INDUZIERT-1 schreibt die Hesse-Matrix als 1/2 Tr(G K2) - 1/2 Tr(G K1 G K1). Die
     Blase ist der verbundene Korrelator; ihr k^2-Anteil aus getrennten Punkten ist +(1/8) Int y^2 psi > 0, also steif,
     anti-Einstein, wie D/Ms Glueball-Teil. Die Konvexitaet des festen Netzes (ERGEBNIS-4D, Selbstanzeige 5) heisst
     in dieser Sprache: Auf festem Netz gewinnt der Kontaktteil immer. Einsteins Vorzeichen kann nur aus dem
     UV-/Kontaktteil kommen, also aus dem, was der Regler festlegt.
2. **Vissers absolutes Vorzeichen widerspricht dem Standardergebnis, woertlich gelesen (A1).**
   - Visser setzt das Einstein-Glied als "-R/(16 pi G)" an (Gl. 19) und erhaelt 1/G ~ -(1/2 pi) str[k1] kappa^2 mit
     der Forderung "str[k1] ~ -1" (Gl. 29, S. 7, Z. 389) [S]. Nach seiner Tabelle 1 (S. 9, Z. 498 bis 512) haben minimale
     Skalare k1 = 1/6 und Dirac-Fermionen in der Superspur +1/3, Vektoren -2/3 [S]. Woertlich wuerden also Skalare und
     Fermionen G negativ machen.
   - Meine Euklid-Rechnung [M]: W = 1/2 ln det(-Box + m^2) enthaelt -(kappa^2/(192 pi^2)) Int sqrt(g) R; mit
     I_E = -(1/(16 pi G)) Int sqrt(g) R folgt 1/(16 pi G_ind) = +kappa^2/(192 pi^2). Anker ueber Entropie [M]: Die
     Kegelmethode gibt S = -4 pi a1 A fuer W ⊃ a1 Int sqrt(g) R; positive Verschraenkungsentropie verlangt a1 < 0, also
     G > 0. Jacobsons "hbar a1 in place of (1/16 pi G)" (quellen/jacobson-gr-qc-9404039.txt, S. 4, Z. 158) ist
     vorzeichenlos gemeint.
   - Lesart: Konventionsfrage in Vissers Gl. (19). **Relativvorzeichen sind davon frei:** minimaler Skalar und Dirac
     gleich, Vektor entgegengesetzt, konformer Skalar null. Das [M] in ERGEBNIS-4D (c = -Lambda^2/(32 pi^2) fuer den
     minimalen Skalar) ist richtig.
3. **"xi_eff > 1/6" ist im langwelligen Sinn ausgeschlossen (eigener Schluss, kein Abruf).** Siehe Ergebnis 3 und
   Abschnitt 6.2. Erwartet hatte die Karte eine bestimmbare effektive Kruemmungskopplung (E4).
4. **Jacobsons Fussnote 1 ist zu optimistisch (A2, A8).** "If the cutoff breaks general covariance ... Still, for
   background metrics that are slowly varying on the scale of the cutoff, the generally covariant terms should
   dominate" (Jacobson 1994, S. 4, Z. 160 ff.) [S]. INDUZIERT-1 fand das Gegenteil (Streuung von c2 78 %). Collins u. a.
   2004: Ein Planck-skaliges Ruhesystem gibt "Lorentz violation at the percent level ... unless the bare parameters of
   the theory are unnaturally strongly fine-tuned" (quellen/api-A8.xml, Abstract) [S]. Nicht kovariante Glieder sind
   von derselben Ordnung Lambda^2 wie das Einstein-Glied [ES].
5. **Vissers eigener Text zeigt einen Vorzeichenwechsel eines Potenzglieds zwischen zwei Reglern (A1, Nebenfund).**
   Eigenzeit: Lambda = -(1/(32 pi^2)) str[kappa^4/2 - ...] (Gl. 20, S. 5), fuer ein Boson also negativ. Fussnote c (S. 8,
   Z. 455 bis 467): Nullpunktsumme mit Impulsschnitt +kappa^4/4, laut Visser "precisely yields the one-loop shift" [S].
   Die Log-Glieder stimmen ueberein (wenn man dort ln kappa liest), das kappa^4-Glied hat entgegengesetztes Vorzeichen
   [M]. Beleg dafuer, dass Potenzglieder mit dem Regler das Vorzeichen wechseln koennen, Log-Glieder nicht.
6. **Die Trefferlage ist duenn (A4b, A7).** Nur 4 Treffer fuer "induced gravity"/Sakharov mit Gitterwoertern, davon
   einer einschlaegig. Die Kernaussage "keine 4D-Vorzeichenrechnung" gilt nach Recherchestand; Grenze: nur Abstracts.

## 3. Erwartungen E1 bis E5 mit Ausgang

| Nr | Erwartung (Karte) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | G_ind fuer Skalare ~ (1/6 - xi) Lambda^2, Umkehr fuer xi > 1/6 | **eingetroffen** fuer Form und Kipppunkt. Absolutes Vorzeichen bei Visser konventionsabhaengig (Verstoss 2), ueber Euklid-Rechnung und Entropie-Positivitaet verankert. Frolov/Fursaev nur als Abstract gelesen ("determined by the masses of the heavy constituents"), xi dort nicht geprueft | Visser 2002, Gl. (3) S. 2, Gl. (14) S. 4, Gl. (21) S. 5, Tabelle 1 S. 9 ("Scalar (generic) ... 1/6 - xi", "Scalar (conformal) ... 0") [S]; FFZ 1996 Abstract [S] |
| E2 | Vorzeichen bzw. Wert reglerabhaengig, nur Log-Teil universell | **eingetroffen, mit Erweiterung** um ein zweites Regime (Verstoss 1) | Visser Fussnote a S. 3 (Zeta bzw. dim. Reg. "hiding some of the interesting terms"), Gl. (20) gegen Fussnote c, Gl. (36) S. 8 und (43) S. 10: 1/G = -(1/2 pi) str[k1 m^2 ln(m^2/mu^2)], Vorzeichen vom Spektrum [S]; Donoghue/Menezes Gl. (16) S. 3, S. 2, 6, 7, 8 [S] |
| E3 | Gitter- bzw. Simplex-Rechnungen, die Vorzeichen bzw. Reglerabhaengigkeit diskutieren | **teilweise.** Es gibt Simplex-Rechnungen, aber keine 4D-Vorzeichenrechnung von G_ind aus einem Gitter-Skalar (nach Recherchestand nicht belegt) | Hamber/Liu 1996: 2D-Anomalie auf Regge-Gittern "with the correct coefficient", Tadpole "necessary on the lattice for canceling unwanted terms" (S. 28) [S]. Raasakka 2025 (v2 13.08.2026): 2D-Lorentz, "G_eff ... ~ 0.015", Fussnote 5 "do not have any immediate physical significance", 4D nur Ausblick (S. 7 bis 9) [S]. Hamber/Williams 1993: 4D-Skalar in dynamischer Regge-Gravitation, "effects of matter are rather small" (Abstract) [S] |
| E4 | Diskrete Laplace auf gekruemmten Simplexkomplexen haben eine bestimmbare effektive Kruemmungskopplung | **nicht belegt** (A7: 4 Treffer, keiner einschlaegig). Eigener Schluss: K 1 = 0 erzwingt xi_IR = 0; der Rest ist keine Kopplung, sondern Reglermoment | quellen/api-A7.xml; Abschnitt 6.2 [ES, M] |
| E5 | Dirac: Vorzeichen ebenfalls positiv, weniger reglerempfindlich | **erster Teil eingetroffen** (relativ: Dirac wie minimaler Skalar, doppeltes Gewicht). **Zweiter Teil nicht belegt.** Dirac hat kein freies xi (R/4 aus dem Quadrat fest), das Reglermoment wirkt aber gleich; auf Gittern kommen Doppler hinzu [L] | Visser Tabelle 1: Dirac k1 = -1/3, mit Fermion-Minus in str also +1/3 [S] |

## 4. Literaturstand (kurz)

- **Kontinuum, Waermeleitung [S Visser 2002]:** S_g = S_g0 + (1/(32 pi^2)) Str{[a0] kappa^4/2 + [a1] kappa^2 +
  [a2] ln(kappa^2/m^2)} + UV-endlich (Gl. 11). a1 = k1 R - m^2 (Gl. 14). Vier Lesarten (Sakharov: Ein-Schleifen-
  Dominanz mit Abschneiden; Pauli: Endlichkeit; Frolov/Fursaev: Berechenbarkeit; Renormierung). In den endlichen
  Lesarten verschwindet der Regler, und 1/G haengt am Spektrum ueber str[k1 m^2 ln m^2].
- **Adler-Zee [S Donoghue/Menezes 2018]:** G_ind aus dem Spur-Korrelator, endlich fuer asymptotisch freie Theorien,
  QCD positiv, frueher auch Krasnikov/Pivovarov positiv (S. 8).
- **Entropie [S Jacobson 1994]:** Verschraenkungsentropie und 1/G_ren werden von denselben Fluktuationen
  renormiert, "in proportion to their contribution" (S. 5, Z. 174) [S]; Bedingung: kovarianter Regler (Fussnote 1).
  Solodukhin 2011 betont das "puzzling behavior ... due to fields which non-minimally couple to gravity" (Abstract) [S].
- **Simplex/Gitter [S]:** Hamber/Liu 1996 (2D-Anomalie richtig, Tadpole als Gitter-Diagramm noetig); Raasakka 2025
  (2D-Lorentz, Zahl ohne physikalische Bedeutung, 4D offen); Collins u. a. 2004 (nicht kovariante Regler ->
  unterdrueckungsfreie Verletzung, Feinabstimmung).
- **24-Monats-Pruefung (Regel 7):** Im Fenster nur Raasakka 2025/2026 gefunden (A4b, A5 nach Datum sortiert). Kein
  "widerlegt" in diesem Dossier.

## 5. Regime und Moderatoren

| Regime | Was G_ind festlegt | Vorzeichen | Moderator | Beispiel |
|---|---|---|---|---|
| R-a: freies Feld, kovarianter Regler mit f >= 0 | (1/6 - xi) mal Reglermoment m_f > 0 | positiv fuer xi < 1/6, Fermionen gleich, Vektoren entgegen | xi, Feldinhalt | Eigenzeit [M]; Visser Tab. 1 |
| R-b: freies Feld, Regler mit Vorzeichenwechsel (Pauli-Villars, Kompensation) | str[k1 m^2 ln m^2] | vom Spektrum | Massen und Gewichte der Reglerfelder | Visser Gl. (36), (43) [S] |
| R-c: Gitter-Regler (unser Fall) | Gittersumme; enthaelt Operatorform, Laengenregel, Mass, Netzensemble | nicht festgelegt | O(h^2 R)-Anteile des Gitteroperators [ES] | INDUZIERT-DICHTE-4D |
| R-d: UV-endliche, asymptotisch freie Materie | Adler-Zee, Spur-Korrelator | dynamisch, QCD positiv | UV-Verhalten der Spur | Donoghue/Menezes [S] |
| Log-Glieder (2D-Anomalie, 4D R^2/Weyl^2, m^2 ln m^2) | Waermeleitungskoeffizienten | universell | keiner | Visser Gl. (22), (23) [S]; Hamber/Liu [S]; unser 2D |

- **Moderator unserer 2D/4D-Spannung [ES]:** die Dimension, weil sie entscheidet, ob das kovariante
  Zwei-Ableitungs-Glied Int sqrt(g) R ein Log-Glied (2D, topologisch, Koeffizient universell) oder ein Potenzglied
  (4D, Lambda^2, Koeffizient Gitterzahl) ist.

## 6. Deutung unserer Befunde

### 6.1 2D: Polyakov getroffen

- **Messung [E, aus ERGEBNIS-GROB]:** Dichte-Ensemble c(0) = 1,075 P +- 0,071 P; festes Netz +0,159.
- **Lesart [ES]:** Das feste Netz traegt nicht kovariante Glieder in grad log rho (Dichte wandert mit der Mode). Mit
  "Zahl = Volumen" verschwinden sie. Das einzige kovariante lokale Zwei-Ableitungs-Glied ist topologisch. Uebrig bleibt
  der universelle Anomalie-Anteil. Das ist das Muster, das Hamber/Liu 1996 auf Regge-Gittern fuer den universellen
  Anteil fanden ("correct coefficient", Tadpole hebt Gitterglieder weg) [S], und das INDUZIERT-1 Teil A2 (lambda =
  0,996) auf dem festen Netz ueber die Winkelstruktur freilegte.
- **Was die 2D-Zahl misst [M]:** den langwelligen Wert von (1 - 6 xi), also xi_IR = (1 - 1,075)/6 = -0,013 +- 0,012
  (mit k^6-Glied 0,91 P +- 0,19 P: +0,015 +- 0,032). Vertraeglich mit dem exakten Wert 0 (6.2). Vorbehalt [M]: Fuer
  xi ungleich 0 kommt in 2D zum lokalen (1 - 6 xi)-Teil ein nichtlokaler Teil der Ordnung xi^2 hinzu, der vom IR
  abhaengt; fuer kleine xi vernachlaessigbar. Die Zahl sagt nichts ueber das 4D-Reglermoment.

### 6.2 Warum xi_IR = 0 [ES, M]

- Fuer phi = konstant gilt K phi = 0 exakt (Verschiebungssymmetrie). Im Kontinuum gibt (-Box + xi R) 1 = xi R. Ein
  Potentialglied ist also auf jedem Netz und jeder Skala verboten.
- Der Massenkoeffizient m^2 ln m^2 im R-Glied ist universell -(1/6 - xi)/(32 pi^2) (aus Visser Gl. 21 abgelesen [S];
  Vorzeichenkonvention wie 2.2). Ein P1-Skalar hat dort 1/6.
- Gitterkorrekturen der Art h^2 R Box im Operator wirken in der Waermeleitung wie h^2 R mal a0 und geben ~ h^2 kappa^4
  ~ kappa^2 zum R-Glied, also in derselben Ordnung wie a1 [M]. Dasselbe gilt fuer die Laengenregel und fuer das Mass
  (det' K gegen det'(M^-1 K): log det M ist lokal und haengt in O(h^2 R) von der Kruemmung ab) [ES]. Ein "xi_eff" im
  UV-Sinn ist deshalb keine Kopplung, sondern die Summe dieser Gitteranteile.

### 6.3 4D: Einstein-Vorzeichen verfehlt

- **Messung [E, aus ERGEBNIS-4D]:** c = +0,111 +- 0,045 (rho = 1), -0,017 +- 0,045 (rho = 0,5); festes Netz +0,171 bzw.
  +0,118; geo+ +0,371.
- **Umrechnung [M]:** In einem kovarianten Ensemble ist c = 6 B mit Gamma ⊃ B Int sqrt(g) R. Also B = +0,0185 +- 0,0075:
  ein negatives induziertes G fuer diesen Regler, falls das Dichte-Ensemble kovariant genug ist.
- **Literatur-Lesart [ES, gestuetzt auf S]:** Das widerspricht keinem Satz. Positiv ist B nur fuer Regler der Klasse
  R-a. Ein P1-Delaunay-Gitter ist R-c. Die starke Abhaengigkeit von der Laengenregel (sp gegen geo+) ist die erwartete
  Form der Reglerabhaengigkeit: Die Regel aendert den O(h^2 R)-Teil des Operators, und genau der speist das
  Lambda^2-Glied (6.2).
- **Festes Netz:** immer anti-Einstein (Konvexitaet). In der Sprache von Abschnitt 2.1: Kontakt schlaegt Blase. Das
  passt zum Positivitaetsargument bei D/M: Der Teil aus getrennten Punkten ist anti-Einstein.
- **Zweifel an der Kovarianz [ES]:** c(0,5) liegt 1,7 SE unter c(1)/sqrt(2). Das kann Rauschen sein oder ein nicht
  kovarianter Anteil (Delaunay in Koordinaten, Regel sp; ERGEBNIS-4D [K6] nur erste Ordnung). Dann waere c nicht 6 B.
  Die Karte in Abschnitt 8 trennt das.
- **Fuer Finns Weiche [H]:** Ein freier Gitter-Skalar kann in 4D das Vorzeichen von G nicht "aus sich" festlegen;
  das bleibt eine Wahl des Reglers (Laengenregel, Mass, Netz). Feste Wege laut Literatur: (i) Kompensation bzw.
  Pauli-Villars-artige Felder (R-b), (ii) UV-endliche, wechselwirkende Materie (R-d), (iii) Feinabstimmung. Die
  Tensorform (c0s/c2 = -2) waere in einem kovarianten Ensemble dagegen erzwungen, unabhaengig vom Vorzeichen
  (INDUZIERT-1, Bedeutung; [H]).

## 7. Unterscheidungspunkte

| Erklaerungspaar | Wo sie auseinanderlaufen | Zugang |
|---|---|---|
| (a) 4D-Vorzeichen ist Eigenschaft des kovarianten P1-Reglers gegen (b) es ist ein nicht kovariantes Artefakt der Torus-Konstruktion (Delaunay in Koordinaten, sp) | exakt kovariantes Ensemble mit O(1)-Kruemmung: S^4. (a) sagt beta > 0 und beta ~ 10,3 c voraus, (b) beta < 0 oder unabhaengig von c | Karte A, <= 10 min je Lauf |
| (a) xi_IR = 0 gegen (b) xi_IR = xi_eff ungleich 0 | 2D-Anomaliezahl (schon gemessen, spricht fuer a) oder 4D m^2 ln m^2-Glied (braucht 1/L << m << 1/h; im 4D-Torus 24 x 6,5^3 kein Fenster) | 2D erledigt; 4D unzugaenglich bei unseren N |
| (a) Vorzeichen fest durch Laengenregel gegen (b) durch Netzensemble allein | dieselben S^4-Netze mit zwei Laengenregeln (Sehne gegen simplexweise Skalierung) | Karte A, Zusatz |
| (a) Jacobson-Gleichheit S_ent = A/(4G) gilt auf dem Gitter gegen (b) gilt nicht | Gitter mit G_ind < 0 und positiver Flaechengesetz-Entropie. (a) verlangt dann einen Widerspruch | Karte B (nur Skizze, Abschnitt 8.4) |
| R-c (Regler) gegen R-d (dynamisch) fuer eine kuenftige Materiewahl | wechselwirkende, asymptotisch freie Materie auf dem Netz | nicht in Reichweite kleiner Laeufe |

## 8. Vorschlag: Rechenkarte INDUZIERT-KUGEL-1 [H]

### 8.1 Frage

Welches Vorzeichen hat das induzierte Regge-Glied eines P1-Skalars auf einem exakt kovarianten Zufallsnetz in 4D, und
haengt es von der Laengenregel ab?

### 8.2 Aufbau

- **4D:** N Poisson-Punkte (feste Zahl, gleichverteilt) auf S^4 vom Radius a mit (8 pi^2/3) a^4 = N (Dichte 1).
  Konvexe Huelle in R^5 = spherisches Delaunay (Qhull). P1-Steifigkeit wie in INDUZIERT-1 (Gram-Formel).
  - Regel C (Sehne): Kantenlaengen = Sehnen; jedes Simplex ist ein echtes euklidisches Simplex, immer einbettbar.
  - Regel S (sp-Analog): je Simplex alle Laengen mit einem Faktor e^(sigma_T), e^(4 sigma_T) = Radialprojektions-
    Jacobi-Faktor am Schwerpunkt (deckt das Simplex auf die Kugel ab). Immer einbettbar.
  - Gamma = 1/2 log det' K, zusaetzlich Gamma_M = 1/2 log det'(M^-1 K) (exakte Beziehung aus INDUZIERT-1 K1).
- **Referenz:** flacher 4D-Torus gleicher Dichte und gleichen N (dichte4d.py, Grundnetz bei s = 0, Regel egal).
- **2D-Kontrolle:** S^2 (Huelle in R^3) gegen T^2 mit zufall2d.py, gleiche N.
- **N:** 4D 1000, 2000, 4000, 8000; 2D 4000, 16 000, 64 000; je 4 bis 6 Saaten. Rauchlauf misst Zeit und Saatstreuung.

### 8.3 Messgroesse und Schreibtischrechnung (was ist vorab ableitbar?)

- **Modell [M]:** Gamma_S(N) - Gamma_T(N) = beta sqrt(N) + gamma ln N + delta + O(N^(-1/2)).
  - Begruendung: Im kovarianten Ensemble sind nur lokale Glieder Int sqrt(g) (proportional N, faellt in der Differenz
    weg) und B Int sqrt(g) R moeglich. Auf S^4 ist Int sqrt(g) R = 32 pi^2 a^2 = 61,6 sqrt(N) bei Dichte 1, also
    **beta = 61,6 B = 10,26 c**.
  - gamma ist universell (Euler- und R^2-Glieder, Groessenordnung 1) und bei dem Rauschen nicht messbar; es stoert nicht.
- **Vorab ableitbar, also KEINE Messung:**
  - Das Volumenglied der Polytop-Konvention: K ist in 4D homogen vom Grad 2 in den Laengen. Skaliert man das Polytop auf
    das Kugelvolumen, aendert sich Gamma exakt um (N - 1)/4 ln(V_Kugel/V_Polytop). Je Netz exakt berechenbar; beide
    Fassungen (roh, berichtigt) berichten, wie das dy in ERGEBNIS-4D.
  - Der extensive Teil alpha N: aus vorhandenen Torus-Daten (Gamma(0)/N, rho = 1) schaetzbar; nur Referenz.
  - In 2D ist K skaleninvariant (Grad 0): kein Volumenglied, und kein kovariantes Glied waechst wie sqrt(N).
    **Vorhersage 2D: beta_2D = 0.** Universell waere -(1/6) ln N in der Differenz S^2 minus T^2 [M, ungeprueft]; bei
    einer Saatstreuung von ~0,04 sqrt(N) je Netz (geschaetzt aus -GROB) nicht messbar.
- **Erwartete Werte je Hypothese [M]:**
  - H-kov (Torus-c ist kovariantes B, Regel S ~ sp): beta = +1,14 +- 0,46.
  - H-Kont (Kontinuum mit Eigenzeit, Lambda aus Modenzahl, Lambda^2 ~ 17,8 bei Dichte 1): beta ~ -0,58; nur das
    Vorzeichen ist belastbar.
- **Rauschen [ES, ungeprueft]:** aus den Torus-Zweitdifferenzen ~0,15 sqrt(N) je Netz, also SE(beta) ~ 0,2 je
  Saatpaar. Mit 4 bis 6 Saaten bei 3 bis 4 N: SE(beta) ~ 0,05 bis 0,1. Das trennt +1,1 von -0,6 klar. Ist die Streuung
  unabhaengiger Netze groesser (moeglich, Gegensweep 4), braucht es mehr Saaten; der Rauchlauf entscheidet.
- **Ableitbarkeitsprobe:** beta ist aus vorhandenen Daten nicht ableitbar (keine S^4-Netze; der Bezug zum Torus-c gilt
  nur unter H-kov, die getestet wird). Projekt-grep (10:35, runden-v3, "S^4", "4-sphere", "four-sphere"; dazu
  Dateien mit "log det" und "Kugel"/"sphere"): nur Fehltreffer (eps^4, cos^4, "Umkugel" in den INDUZIERT-Plaenen).
  Keine S^4-Rechnung im Projekt. Vor dem Einfrieren der Karte trotzdem noch einmal pruefen.

### 8.4 Vorhersagen (fuer die Karte; Wahrscheinlichkeiten setzt die Leitung)

| Nr | Vorhersage | kann scheitern, weil |
|---|---|---|
| KU0 | 2D: abs(beta_2D) <= 2 SE und <= 0,05 | ein sqrt(N)-Glied in 2D zeigte ein Artefakt der Kugel-Konstruktion; dann Karte stoppen |
| KU1 | 4D, Regel S: beta > 0 mit >= 3 SE (Gitter-G negativ, wie Torus) | beta < 0 hiesse: Das Torus-Vorzeichen kam aus nicht kovarianten Anteilen, und fuer ein kovariantes P1-Ensemble ist Einsteins Vorzeichen moeglich; Ue1 in 4D bliebe offen [H] |
| KU2 | 4D: beta(Regel S) innerhalb 2 SE von 10,26 c_Torus = +1,14 +- 0,46 | Abweichung hiesse: das Torus-c ist nicht 6 B |
| KU3 | 4D: beta(Regel C) und beta(Regel S) haben verschiedenes Vorzeichen | gleiches Vorzeichen hiesse: das Vorzeichen ist robust gegen die Laengenregel |
| KU4 | Gamma gegen Gamma_M (Mass): beta aendert sich um mehr als 2 SE | keine Aenderung hiesse: das Mass ist fuer das Vorzeichen egal |

- **Laufzeit [ES]:** Huelle in R^5 nur mit N Punkten (keine Saumkopien), LU wie ERGEBNIS-4D (N = 5000: ~6 s,
  10 000: ~40 s). Ein Lauf = ein N, beide Regeln, 4 bis 6 Saaten, S^4 und T^4: unter 10 min bis N = 8000.
- **Karte B (Skizze, nicht fuer jetzt):** Flaechengesetz der Verschraenkungsentropie eines Gitter-Skalars gegen
  1/(4 G_ind) aus Karte A, auf derselben Netzklasse. Braucht eine raeumliche 3D-Scheibe (Hamilton-Bild) und ist kein
  10-Minuten-Lauf.

## 9. Gegensweep-Befunde

- Projektsuche zuerst (grep "sakharov\|induziert\|visser"): keine lokale Kopie einer Quelle zur induzierten
  Gravitation; alle bisherigen Nennungen [L]. Gefunden: Raasakka 2025 in RUNDE-22 (dort nur Abstract) -> A3.
- Selbstverstaendlich angenommen und geprueft:
  1. "Minimaler Skalar gibt positives G": geprueft; gilt fuer R-a, Visser woertlich dagegen (Verstoss 2).
  2. INDUZIERT-1s Collins-Zitat: am Abstract bestaetigt (A8).
- Selbstverstaendlich angenommen, nicht abschliessend geprueft:
  3. Dass das Torus-c das kovariante B ist (c = 6 B): Hinweis dagegen aus der Dichteskalierung (1,7 SE). Karte A.
  4. Rauschen ~0,15 sqrt(N) je Netz auf S^4: aus korrelierten Torus-Netzen geschaetzt.
  5. Dass die Laengenregel Reglermerkmal ist und kein Fehler: begruendet, nicht an Literatur geprueft.
  6. Dass das Mass (det' K ohne M) neutral ist: nein, es traegt in O(h^2 R) zum R-Glied bei (6.2) [ES]; neu als
     Vorhersage KU4.

## 10. Kalibrierung

- **(a) Gemessen (Projekt):** 2D 1,075 P +- 0,071 P; 4D c = +0,111 +- 0,045 und -0,017 +- 0,045; feste Netze positiv.
- **(b) Nuetzlich verdichtet:** "Potenzglieder gehoeren dem Regler, Log-Glieder sind universell" [S Visser, M];
  "getrennte Punkte tragen anti-Einstein bei" [S D/M Gl. 16 plus Positivitaet]; "K 1 = 0 heisst xi_IR = 0" [M];
  Zwei-Regime-Tabelle (Abschnitt 5) [ES].
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):** Meine Sicherheit, dass das 4D-Vorzeichen "nur
  Regler" ist, stieg beim Schreiben, waehrend die Frage feiner wurde (Kovarianz des Torus-Ensembles, Mass,
  Laengenregel). Belegt ist nur: Kein Satz erzwingt ein positives G fuer Gitter-Regler. Dass unser Wert ein kovariantes
  B ist, ist nicht belegt. Ebenso ist die Gleichsetzung "Blase = Adler-Zee-Korrelator" eine Analogie [ES], keine
  Herleitung.

## 11. Offene Fragen

- R1: Vissers Konvention in Gl. (19) (fuer uns ohne Folgen).
- R2: Gibt es Gitterrechnungen, die Verschraenkungs-Flaechengesetz und 1/G_ind auf demselben Gitter vergleichen?
  (nicht gesucht)
- R3: Laesst sich das Reglermoment der P1-Delaunay-Diskretisierung analytisch angeben (Spektraldichte gegen Weyl-
  Gesetz, O(h^2 R)-Korrekturen)? (offen)
- R4: Frolov/Fursaev: explizite Formel mit xi_s im Volltext nicht gelesen (nur Abstract).
- R5: Ob Khuri 1982 o. ae. zum Vorzeichen in asymptotisch freien Theorien widerspricht: D/M zitieren es nicht; nicht
  gesucht.

## 12. Quellenliste (Abrufstand 2026-10-04, 10:17 bis 10:28 CEST; lokale Kopien in quellen/)

1. M. Visser (2002), "Sakharov's induced gravity: a modern perspective", Mod. Phys. Lett. A 17, 977.
   https://arxiv.org/abs/gr-qc/0204062 (v1, Volltext; visser-gr-qc-0204062.txt) [S]
2. T. Jacobson (1994), "Black Hole Entropy and Induced Gravity". https://arxiv.org/abs/gr-qc/9404039 (v1, Volltext)
   [S]
3. M. Raasakka (2025/2026), "Emergence of gravity from quantum field theory in triangulated spacetime and the QFT
   vector model", Phys. Scr. 101, 335301 (2026). https://arxiv.org/abs/2505.07102 (v2 vom 13.08.2026, Volltext) [S]
4. J. F. Donoghue, G. Menezes (2018), "Inducing the Einstein action in QCD-like theories".
   https://arxiv.org/abs/1712.04468 (v3, Volltext) [S]
5. H. W. Hamber, S. Liu (1996), "Feynman Rules for Simplicial Gravity". https://arxiv.org/abs/hep-th/9603016 (v2,
   Volltext; Textfolge im pdftotext verwuerfelt) [S]
6. J. Collins, A. Perez, D. Sudarsky, L. Urrutia, H. Vucetich (2004), "Lorentz invariance and quantum gravity: an
   additional fine-tuning problem?" https://arxiv.org/abs/gr-qc/0403053 (nur Abstract, api-A8.xml) [S]
7. S. N. Solodukhin (2011), "Entanglement entropy of black holes", Living Rev. Rel. https://arxiv.org/abs/1104.3712
   (nur Abstract, api-A8.xml) [S]
8. V. P. Frolov, D. V. Fursaev, A. I. Zelnikov (1996), "Statistical Origin of Black Hole Entropy in Induced
   Gravity". https://arxiv.org/abs/hep-th/9607104 (nur Abstract, api-A8.xml) [S]
9. H. W. Hamber, R. M. Williams (1993), "Simplicial Gravity Coupled to Scalar Matter",
   https://arxiv.org/abs/hep-th/9308099; H. W. Hamber (1993), "Scalar Fields Coupled to Four-Dimensional Lattice
   Gravity", https://arxiv.org/abs/hep-th/9310152; H. W. Hamber, R. M. Williams (1996), "Gauge Invariance in Simplicial
   Gravity", https://arxiv.org/abs/hep-th/9607153 (alle nur Abstract, api-A9.xml) [S]
10. D. Sexty, C. Wetterich (2012), "Emergent gravity in two dimensions", https://arxiv.org/abs/1208.2168 (Abstract,
    api-A5.xml; kein G-Vorzeichen) [S]
11. arXiv-API-Abfragen A4b, A5, A7, A9 (Treffermengen und Abstracts in quellen/api-*.xml).
- Nur [L] genannt, nicht abgerufen: Sakharov 1967; Gibbons/Hawking/Perry 1978; Adler 1982; Zee 1981; Susskind/Uglum
  1994; Kabat 1995; Cheeger 1983; Kenyon 2000; Reflexionspositivitaet (Osterwalder/Schrader).

## 13. Selbstanzeigen

- Statt WebFetch habe ich curl mit lokaler Kopie benutzt (Regel "Fundstellen nur aus selbst gelesenem Text"). Jeder
  curl-Aufruf ist als Abruf gezaehlt, der leere Erstversuch A4 eingeschlossen: 11 von 15.
- Lokale Kopien (PDF und Text) liegen im Kartenordner quellen/, nicht im Scratchpad.
- Verwendete Werkzeuge: curl, pdftotext, grep, sed, cut, tr, paste, wc, ls, file, mkdir, date. Kein python, awk, perl.
- Die Euklid-Rechnungen [M] in 2.2, 5 und 6.2 sowie die Schreibtischzahlen in 8.3 sind nicht gegengelesen.
- Eine eigene Zeile im ARBEITSFELD (2D-Blase) habe ich nach 10:31 gestrichen und begruendet; sie steht dort mit ~~.
- Die Projektsuche (grep ueber coordination/runden-v3 und coordination/*.md, Sperrpfade und -namen ausgeschlossen) hat
  Dateiinhalte durchsucht; angezeigt wurden nur Dateinamen und Trefferzeilen zu sakharov/induziert/visser. Eine
  Trefferzeile stammt aus ARBEITSFELD-claude-primary.md (Q-Ball-Notiz, ohne Bezug). KS-1-Inhalte habe ich nicht gesehen.
- Seitenangaben zu Donoghue/Menezes nach dem ersten Entwurf berichtigt (S. 6 und 7 statt 7 und 8; Formfeed-Zaehlung).
- Zeitbox: Start 10:07:06, Dossier ab 10:31:16 CEST; Abgabezeit in der Schlussmeldung.

## 14. Einfach gesagt

Ob das Zittern der Materie die Raumzeit so versteift, wie es Einsteins Schwerkraft verlangt, haengt in vier Dimensionen
nicht nur von der Materie ab, sondern davon, wie man die allerkleinsten Abstaende behandelt, also vom Netz selbst. In
zwei Dimensionen gibt es dagegen eine Zahl, die jedes vernuenftige Netz richtig liefern muss, und genau die haben wir
getroffen. Deshalb ist unser 4D-Ergebnis mit dem falschen Vorzeichen kein Rechenfehler, sondern eine Eigenschaft
unseres Netzes, die kein Naturgesetz verbietet. Die Literatur zeigt, dass ein festes Vorzeichen erst entsteht, wenn
die Materie selbst bei kleinsten Abstaenden zahm wird, wie die Gluonen in Atomkernen. Als naechsten kleinen Test
schlage ich vor, das Vorzeichen auf einer vierdimensionalen Kugel zu messen, wo das Netz keine Vorzugsrichtung hat
und die Antwort deutlich aus dem Rauschen herausragen sollte.
