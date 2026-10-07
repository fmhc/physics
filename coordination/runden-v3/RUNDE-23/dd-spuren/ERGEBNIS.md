# ERGEBNIS DD-SPUREN (Runde 23): Die neuen Arbeiten gegen die Dark Dimension, ihre Spuren, Annahmen, Antworten und was pruefbar bleibt

- Literatur-Agent (feldforscher) im Auftrag von claude-primary.
  - Agentenstart 2026-10-02 21:24:29 CEST, Schreibbeginn dieses Berichts 21:41:36 CEST (beides date).
- Arbeitsdatei: `ARBEITSFELD.md` (gleicher Ordner). Sie enthaelt jede Erwartung vor dem Abruf, jeden Ausgang und alle
  Zeiten.
- Quellkopien in `quellen/`:
  - Volltexte (PDF und pdftotext): Langhoff 2610.01825, Lee/Randall/Riojas 2609.36234, Danielsson/Giri 2606.20942 und
    2511.21362, Anchordoqui u. a. 2411.07029, Langhoff/Ramos/Reig 2607.27314, GMOV 2209.09249, Obied u. a. 2311.05318,
    Manley u. a. 2406.13020, Baeza-Ballesteros u. a. 2106.08611, Adelberger u. a. hep-ph/0611223
  - Murata u. a. 2605.18212 als HTML-Text, dazu Abb. 3 und 4 als PNG
  - API-Antworten: arXiv (`api-*.xml`), Semantic Scholar (`s2-*.json`), INSPIRE (`inspire-*.json`), OpenAlex
    (`openalex-*.json`, `oa-*.json`)
- Marken:
  - [S] selbst gelesen: Volltext-Stelle oder Abstract im Wortlaut aus der API, jeweils angegeben
  - [L?] nur Titel, Metadaten oder Zitat
  - [H] eigene Schlussfolgerung
  - [E] Kopfrechnung mit hbar c = 1,973e-7 eV m
- Beide Hauptarbeiten sind **unbegutachtete Preprints** (je nur v1). Fehlanzeigen gelten nur nach Recherchestand.
- Datenkorrektur zur Karte: Lee/Randall/Riojas erschien am **28.09.2026**, Langhoff am **01.10.2026** (arXiv-API,
  Feld published). Die Karte nennt die Daten vertauscht.

---

## 1. Ergebnis zuerst (5 Punkte)

1. **Was die zwei Arbeiten zeigen.** Beide finden dieselbe Schwellenunterdrueckung. Ein KK-Graviton zerfaellt in zwei
   leichtere nur mit einer Rate proportional zu q^5 (q = Impuls der Zerfallsprodukte), nicht ~q wie in der
   Dark-Dimension-Literatur angenommen. Fuer die DD-Parameter macht das ~1e-24 aus [S].
   - Lee/Randall/Riojas (LRR) begruenden das allgemein und halten es auch mit Warp-Faktor fuer gueltig. Sie greifen nur
     die Dunkle-Materie-Kaskade an: "the suggestion by GMOV [8, 9] is ruled out by decays to the Standard Model" [S].
     Damit ist **E3 eingetroffen**.
   - Langhoff geht weiter: Auch wenn die Dunkle Materie etwas anderes ist, gilt fuer eine flache Dimension R <~ 0,2 um
     (m_KK >~ 1 eV). Grundlage: die unvermeidliche Freeze-in-Population, MeV-Gammadaten und T_RH >= 5,96 MeV [S].
   - Antworten gibt es noch keine. Die einzige Zitierung ist Langhoffs Querverweis auf LRR (Semantic Scholar,
     INSPIRE, arXiv, OpenAlex). **E1 ist eingetroffen**, bei einem Fenster von einem bzw. vier Tagen.
2. **E2 nur zur Haelfte.** Langhoffs Ausschluss haengt an Modellannahmen: flache oder schwach gewarpte Geometrie,
   Brane am Fixpunkt, keine weiteren Zerfallskanaele ausser 9/4 Gamma_gg [Lesart H], eigene unbegutachtete
   Freeze-in-Formel, T_RH-Untergrenze [S].
   - Der Warp-Faktor allein umgeht die Schwellenunterdrueckung aber nicht. Langhoffs Feldumdefinition gilt "for all
     momenta and any static warped extra dimension" [S]; LRR argumentieren ebenso.
   - Ausweichen ist nur ueber ein anderes Spektrum moeglich. Das kuendigt die noch nicht erschienene LRR-Begleitarbeit
     an: Warping "can rescue some parameter space", die Modelle seien aber "still severely constrained" [S].
   - Ganz ausserhalb der Annahmen liegt die dunkle Blase (Danielsson/Giri) [H].
3. **Die Spur ist aelter als die zwei Preprints.**
   - Die Aufhebungsphysik stand seit 2019-2021 in der Randall-Sundrum- und Summenregel-Literatur (Bonifacio/
     Hinterbichler; de Giorgi/Vogl). GMOV schaetzten die Turm-internen Raten 2022 ausdruecklich naiv ab
     ("expected again to be roughly given by (3.1)") [S].
   - Schon im Juli 2026 schrieben Langhoff/Ramos/Reig: "the simplest dark dimension dark matter model is excluded" [S].
   - 2024 gab es einen ersten Ausschlussanspruch gegen Mikrometer-Dimensionen (McKeen/Ng/Shamma, Delta N_eff). Die
     Gegenrede von Anchordoqui u. a. stuetzte sich auf schnelle Turm-interne Zerfaelle [S].
   - [H] Das ist genau der Mechanismus, den LRR und Langhoff jetzt fuer Gravitonen an der Schwelle unterdrueckt finden.
     Ob er auch Neutrino-Tuerme trifft, ist offen.
4. **Labor: E4 eingetroffen (streng), mit zwei Erwartungsverstoessen.**
   - Unter 10 um liegen die heutigen Schranken bei alpha ~ 1e4 (10 um) bis ~1e11-1e12 (0,2 um). Die DD erwartet
     alpha = 8/3 [S Abb., Augenmass; E].
   - Kein laufendes Projekt erreicht in zwei Jahren Gravitationsstaerke unter 10 um. Der DD-motivierte
     Mikro-Torsionsresonator (Manley u. a. 2024) kaeme erst kryogen bei 100 mK "potentially" auf ~10 um [S].
   - Verstoss: Ein Papiervorschlag (Mikro-Orbits, Baeza-Ballesteros/Donini/Nadal-Gisbert 2022) beansprucht alpha ~ 1
     schon bis lambda <~ 5-7 um. Gebaut ist er nach Recherchestand nicht [S].
   - Verstoss: Die Variante mit umgekehrtem Vorzeichen (dunkle Blase) ist mit vorhandenen Daten pruefbar.
     - Ihre Korrektur -(3/2)(L/r)^2 ist ein Potenzgesetz.
     - Eot-Wash begrenzte solche Terme schon 2007 auf |beta_3| <= 1,3e-4 (68 %) [S].
     - Daraus folgt L <~ 9 um [E]. Der Blasen-Wert 50 um (Danielsson/Panizo 2024) laege rund 30-fach darueber; der
       neuere Wert "L ~ 1e-5 m" liegt an der Grenze.
5. **Bedeutung gemaess Karte: Sie greift nur teilweise.**
   - Eingetroffen ist E3: Die DM-Begruendung ist, falls die Preprints halten, erledigt.
   - Der Kern ist aber nicht bloss "modellabhaengig unter Druck". Fuer eine flache Dimension trifft Langhoff gerade
     den Mikrometerbereich: Von MVVs 0,1-10 um bliebe nur das untere Ende 0,1-0,2 um. Auch die Casimir-Schaetzung
     7,4 um faellt heraus.
   - Im Mikrometerbereich ueberleben nur nicht-flache Realisierungen, und die Blase ist schon von Eot-Wash eingeengt
     [E].
   - E4 eingetroffen: Die flache DD ist im Labor auf absehbare Zeit unpruefbar. Der praktische Test ist die
     MeV-Gamma-Astronomie (Faktor 10 mit AMEGO-X bzw. e-ASTROGAM).
   - Fuer Glied 10 aendert sich nur die Einordnung [H]: Im zugaenglichen Fenster (5-60 um) bleiben die Stelle-Form
     (+1/3, -4/3) und die Blase (Potenzgesetz, schwaecher) als Muster. Die Vorzeichenfrage wird dadurch wichtiger.

---

## 2. Erwartungsverstoesse (das eigentliche Ergebnis; wichtigster zuerst)

| Nr | Erwartung vorab (ARBEITSFELD Abschnitt 2 bzw. Karte) | Was stattdessen kam | Korrektur |
|---|---|---|---|
| V1 gross | VB-5 und Kartenbedeutung: Die DD-Varianten sind im Labor "vorerst unpruefbar"; die Blase liegt ausserhalb jeder Schranke | Adelberger/Heckel/Hoedl/Hoyle/Kapner/Upadhye, PRL 98, 131104 (2007): Potenzgesetz-Schranken, k = 3: \|beta_3\| <= 1,3e-4 (68 %). Den "fat graviton" testeten sie ebenfalls: "Our results require lg <= 98 um at 95% confidence" [S Volltext Z. 218-350]. Danielsson/Giri Gl. 23: V = -G M [1/rho - 3L^2/(2 rho^3) + ...] [S] | [E] beta_3 = -1,5 (L/1 mm)^2, daraus L <~ 9 um (68 %; bei 95 % grob ~13 um). Fuehrende Ordnung, Punktmassen, ohne Apparateantwort. D/G zitieren die Eot-Wash-Auswertung nicht (grep). Die Blase ist also keine laborferne Variante, sondern liegt an der Grenze heutiger Daten |
| V2 mittel | Kartenbedeutung: Der Kern (Dimension im um-Bereich) ist "nicht tot", nur die DM-Begruendung | Langhoff: "This excludes the existence of a flat dark dimension with R >~ 0.2 um" [S], ausdruecklich unabhaengig von der Natur der Dunklen Materie | Fuer flache bzw. schwach gewarpte Realisierungen ist gerade der um-Bereich betroffen. Es bleibt R <~ 0,2 um, falls die Arbeit haelt |
| V3 mittel | VB-1/Karte: Der Druck auf die DD kam mit zwei neuen Preprints | Langhoff/Ramos/Reig 2607.27314 (29.07.2026): "the simplest dark dimension dark matter model is excluded", Auswege nur per Handabstimmung: "no concrete construction achieving this has been proposed" [S Z. 60-69]. McKeen/Ng/Shamma 2406.05266 (2024): "These limits generically rule out micron-sized extra dimensions" [S Abstract] | Die zwei Preprints sind die dritte Welle: Delta N_eff 2024, Energieeinspeisung gegen Kick-Geschwindigkeit 07/2026, Schwellenunterdrueckung 09/10 2026 |
| V4 mittel | VB-2: Die q^5-Rate ist eine neue Rechnung | LRR: "resolving an ambiguity in the literature". Giudice u. a. 2018 fanden eine erhoehte Rate, "in disagreement with" de Giorgi/Vogl 2021 und Bonifacio/Hinterbichler 2019; das RS-Ergebnis war schon bekannt: "validating the result in [14]" [S] | Neu ist die Anwendung auf die DD-Kaskade, nicht die Amplitudenphysik. GMOV Gl. 3.2 nahm die Kanalrate "roughly given by (3.1)" an, nur mit Geschwindigkeits-Phasenraum [S] |
| V5 mittel | VB-4: Projektionen erreichen hoechstens alpha ~ 1e2-1e3 bei ~10 um | Baeza-Ballesteros/Donini/Nadal-Gisbert, EPJC 82, 154 (2022): Sensitivitaet fuer alpha ~ 1 bis "lambda <~ 5 um" ohne Untergruende, "<~ 7 um" mit ungunstigen; "compared with the present sensitivity, lambda <= 40 um" [S Z. 2862-2876] | Auf dem Papier gibt es Gravitationsstaerke unter 10 um. Die Folgearbeit 2312.13736 (12/2023) beginnt erst mit dem realistischen Aufbau (Luftreibung) [S Abstract]. E4 bleibt im strengen Sinn eingetroffen |
| V6 klein | E2 (Karte): Gewarpte Varianten umgehen Langhoff | Langhoff Gl. 25: Die Aufhebung gilt "for all momenta and any static warped extra dimension" [S]; LRR absorbieren Skalare und nichtminimale Kopplungen in den Warp-Faktor [S] | Warping hilft nur ueber ein anderes Spektrum bzw. andere Kopplungen. Die LRR-Begleitarbeit ist "to appear" |
| V7 klein | VB-5: Die Blase hat eine um-Dimension mit Yukawa-artiger Abschwaechung | Danielsson/Panizo 2311.14589: "a dark dimension of size 5 x 10^-5 m" [S Abstract]; D/G 2026: L ~ 1e-5 m, Korrektur als Potenzgesetz [S] | Die Blasenlaenge liegt 10-50 um, also im Torsionswaagen-Fenster |
| V8 klein | Kartendaten | API: LRR 28.09.2026, Langhoff 01.10.2026 | In der Karte vertauscht |
| V9 klein, Kanal | INSPIRE "refersto:arxiv:<id>" und arXiv "au:Randall_L" funktionieren | Fremdtreffer (2009er Arbeit bzw. andere Randalls) | Ersatz: INSPIRE ueber recid; au:Riojas |

**Selbstkorrekturen:** keine Streichungen noetig. Zwei Kanalsyntax-Fehlschlaege stehen in V9.

---

## 3. Antworten auf die Fragen

### Frage 1: Was genau zeigen die beiden neuen Arbeiten?

| | Lee/Randall/Riojas, arXiv:2609.36234v1 (28.09.2026, hep-th, 11 S.) | Langhoff, arXiv:2610.01825v1 (01.10.2026, hep-ph, 4 S., Einzelautor, MIT) |
|---|---|---|
| Mechanismus | Kubischer Vertex dreier KK-Gravitonen. Terme, in denen zwei Ableitungen miteinander kontrahiert sind, geben M ~ m_n; sie heben sich weg, weil die Klammer die Bewegungsgleichung des masselosen 5D-Gravitons ist (Gl. 3-4). Es bleiben Terme, die Impulse mit Polarisationen kontrahieren, also M ~ q [S] | An der Schwelle "pure d-wave", Gamma ~ p^5. Vertex als Doppelkopie des Yang-Mills-Vertex (Gl. 14-15); die Null an der Schwelle sei "dynamical in origin", nicht Drehsymmetrie. Herleitung ueber die Feldumdefinition h = e^H - 1 (Gl. 25) [S] |
| Annahmen | Zweiableitungs-Gravitation mit Skalaren; KK-Verletzung durch Skalare wird in einen Warp-Faktor absorbiert (App. A, B), nichtminimale Kopplungen per Weyl-Reskalierung. Hoehere Ableitungen helfen nicht (App. E). Fuer die Skalierung der Ueberlappungen (App. F): glatter Bulk-Hintergrund, m_n >> m_KK, Neumann-Rand; "brane localized curvature terms (e.g. DGP terms) may give model dependent corrections" [S] | 5D minimal gekoppelt, Intervall 0 <= y <= pi R, Brane am Fixpunkt, c_n = sqrt(L) psi_n(y_b). Kaskadenschaetzung fuer schwach gewarpt (Gl. 26) und flaches Spektrum m_n = n m_KK. Irreduzible Schranke: Abundanz aus Ref. [33] (Langhoff/Ramos/Reig 2026, unbegutachtet), gueltig fuer T_RH <~ 100 MeV; Gesamtbreite 9/4 Gamma_gg, ohne weitere (etwa unsichtbare) Kanaele [S; Lesart "ohne weitere" H] |
| Datenlage | keine eigenen Daten; GMOV-Parameter (m_KK ~ eV, delta n_max ~ 1e2, beta ~ 20) [S] | COMPTEL inneres Milchstrassengebiet (Burkert-Halo, J = 1,55), COMPTEL/EGRET isotrop; Kriterium Signal > Beobachtung + 2 sigma; T_RH >= 5,96 MeV aus Barbieri u. a., PRL 135, 181003 (2025) [S] |
| Rechnung | Unterdrueckung je Kanal (q/m_n)^4; Kaskaden-Lebensdauer ~1e26 s statt 1e2-3 s; m(t) ~ t^(-2/3) statt t^(-2/7) [S] | Verhaeltnis zu s-Welle ~ (Q/mu)^2 ~ 1e-24 fuer Q ~ m_KK ~ meV; Kaskade fuer delta n = 100 und R = 0,05-0,2 um: Massenverteilung verschiebt sich bis zur Gleichheit Materie/Strahlung um < 0,1 % [S] |
| Schranke | keine R-Schranke; "can be used to rule out existing Dark Dimension models" [S Abstract] | (a) KK-Gravitonen als DM in flacher DD ausgeschlossen; (b) "a viable TRH exists only for R <~ 0.2 um, mKK >~ 1 eV" [S] |
| Variante | flach als Spezialfall des allgemeinen Warps; Begleitarbeit zu RS angekuendigt | flach bzw. "approximately flat"; Abb. 1 mit Torsionswaagen-Streifen "(for a brane at a fixed point)" |
| DM-Kaskade | ja, nur sie | ja, und zusaetzlich die Dimension selbst ueber die irreduzible Population |
| Querbezug | Dank an Kevin Langhoff | "Note Added": LRR erhielten dieselbe Unterdrueckung; eigener Weg, unabhaengig; Dank fuer Diskussionen |

- [E] Einordnung der Zahlen:
  - Lambda^(1/4) = 2,31 meV entspricht R ~ 85-88 um; 0,2 um liegt rund 440-mal darunter. Langhoffs "almost three
    orders of magnitude" bezieht sich auf diesen naiven Wert, nicht auf MVVs Bereich 0,1-10 um (Gl. 3.8 dort).
  - Langhoffs m_KK >~ 1 eV entspricht R <~ 0,2 um, also lambda <~ 2e-3 in MVVs Schreibweise.
- [H] Kleine Unstimmigkeit zwischen den Kritiken: LRR setzen fuer GMOV m_KK ~ eV an, Langhoff m_KK ~ meV. Beide landen
  auf demselben Faktor ~1e-24, aber auf verschiedenen Wegen.
- [H] Die zwei Herleitungen sind nicht voellig unabhaengig: Beide Seiten danken einander fuer Diskussionen.

### Frage 2: Welche Annahmen sind angreifbar, welche Varianten entgehen?

**Langhoffs irreduzible Schranke** (die staerkere Aussage):
- **Geometrie, flach oder schwach gewarpt:**
  - Die Schwellennull selbst gilt fuer jeden statischen Warp [S, Gl. 25].
  - Angreifbar ist nur der Rest: das gleichmaessige Spektrum m_n = n m_KK, die Kopplungen c_n an der Brane und die
    Vollstaendigkeitsschranke g^2 <= 1 + O(Delta A).
  - Ein stark gewarpter Hals mit "redshifted KK tower" existiert als Konstruktion (Blumenhagen/Brinkmann/Makridou
    2208.01057) [S Abstract]. Ob er Langhoff entgeht, ist ungerechnet [H].
- **Freeze-in-Formel:**
  - Sie stammt aus Langhoffs eigener, unbegutachteter Arbeit 2607.27314 [S].
  - Ein unabhaengiger Abgleich, etwa mit Gross/Hooper 2407.07529 (KK-Freeze-in und BBN), fehlt [H].
- **T_RH-Untergrenze 5,96 MeV:**
  - Die Grenze stammt aus der juengsten, laut Abstract strengsten Analyse (Barbieri u. a. 2025) [S Abstract].
  - [E, grob] Die Abundanz geht wie T_RH^3 R. Eine um 20 % tiefere Untergrenze verschiebt die R-Grenze etwa um den
    Faktor 2. Das ist robust in der Groessenordnung, nicht im Faktor.
- **Keine weiteren Zerfallskanaele (Gesamtbreite 9/4 Gamma_gg) [H-Lesart]:**
  - Zusaetzliche unsichtbare Kanaele wuerden den Photonfluss verduennen.
  - Langhoff/Ramos/Reig zeigen genau das fuer N Axion-Tuerme ("diluted by a factor of N") [S Abstract].
  - [H] Dort verteilen sich die Tuerme aber durch Fragmentation um, also wieder durch Turm-interne Zerfaelle. Ob die
    Schwellenunterdrueckung auch diesen Ausweg trifft, ist offen.
- **Brane am Fixpunkt, Standard-Kopplung:**
  - [E] psi_n^2(0)/psi_0^2 = 2, also alpha = 8/3 und lambda = R.
  - An einem allgemeinen Ort waere die Kopplung 2 cos^2(n y_b/R) <= 2.
  - Brane-Kruemmungsterme (DGP) nennen LRR selbst als modellabhaengige Korrektur ihrer Skalierung [S App. F].

**LRR:**
- Gezielt ist nur die Kaskade; die Unterdrueckung "applies regardless of how chi_nml scales" [S App. F].
- Rettungswege laut LRR:
  - viel kleinere Anfangsmassen; dann treffen Fuenfte Kraft und Kick-Geschwindigkeit
  - Warping (Begleitarbeit, nicht erschienen)
  - KK-Tuerme von Skalaren, "even less well motivated" [S]

**Varianten, die den Schranken entgehen (nach Recherchestand):**
1. **Flache DD mit R <~ 0,2 um:**
   - MVVs unteres Ende (lambda ~ 1e-3) ueberlebt, aber ohne KK-Gravitonen als DM.
   - Im Labor ist sie unsichtbar (Frage 4).
2. **Dunkle Blase** (Danielsson/Giri 2606.20942; 2511.21362, PRD 113, 126010):
   - Kein kompakter Kreis; 4D-Gravitation ist "stronger than the five dimensional one", umgekehrt wie bei KK und RS [S].
   - Langhoffs Herleitung trifft sie nicht [H].
   - Sie hat aber ihre eigene Laborschranke (V1).
3. **Stark gewarpte Hals-Varianten:** ungerechnet; LRR kuendigen "rescue some parameter space" an [S].
4. **DD mit anderer Dunkler Materie** (primordiale bzw. 5D-Schwarze Loecher, z. B. Anchordoqui/Bedroya/Luest
   2506.14874 [L? Titel]):
   - Sie entgeht der Kaskadenkritik.
   - Langhoffs irreduzible Schranke R <~ 0,2 um gilt nach seiner Aussage trotzdem [S].

### Frage 3: Reaktionen und juengster Stand der uebrigen Schranken

**Reaktionen (Stand 02.10.2026, ~21:40 CEST):**
- Semantic Scholar: LRR hat 1 Zitat (Langhoff), Langhoff 0 [S, quellen/s2-cit-*.json].
- INSPIRE: LRR (recid 3209110) citation_count 1, Langhoff (recid 3210654) 0, Danielsson/Giri (3170957) 0
  [S, quellen/inspire-*.json].
- arXiv all:"dark dimension" (73 Treffer, nach Datum): juengster Eintrag Langhoff [S].
- Juengste Arbeiten der Urheber, alle vor dem 28.09. und ohne Bezug zu KK-Zerfaellen:
  - Baykara/Vafa 2609.20915 (17.09.)
  - Anchordoqui/Antoniadis/Bedroya 2608.11086 (11.08.)
  - Anchordoqui/Bedroya/Luest/Tarazi 2608.00590 (01.08.)
  - Montero/Vafa/Valenzuela 2512.09052 (09.12.2025)
- OpenAlex-Volltextsuche "dark dimension" ab 01.09.2026: 38 Treffer, keine Antwort.
- **Fazit:** keine Antwort der Urheber, kein Kommentar. Das ist negative Evidenz aus einem Fenster von 1-4 Tagen.
- Muster frueherer Wellen [S]:
  - McKeen/Ng/Shamma 06/2024 (Delta N_eff) beanspruchten einen Ausschluss.
  - Anchordoqui/Antoniadis/Luest/Penaló Castillo antworteten nach rund fuenf Monaten (2411.07029, 11/2024): "deceptive
    conclusion", "not generic but rather model dependent".
  - [H] Eine Antwort auf LRR/Langhoff waere demnach eher in Wochen bis Monaten zu erwarten.

**Uebrige Schranken mit Datum:**

| Art | Arbeit | Datum | Ergebnis fuer die DD (n = 1) | Marke |
|---|---|---|---|---|
| Kurzabstand | Lee, Adelberger, Cook, Fleischer, Heckel, PRL 124, 101101 | 02/2020 | \|alpha\| = 1 bei lambda < 38,6 um; fuer alpha = 8/3 nennen MVV "around 30 um" | [S, aus STELLE-24M/DUNKEL-ZEIT] |
| Kurzabstand | Kapner u. a., PRL 98, 021101 | 11/2006 | R <= 44 um | [S Abstract, DUNKEL-ZEIT] |
| Kurzabstand | Venugopalan u. a., Sci. Rep. 16, 5180 | 12/2024 (2026) | alpha ~ 1e6-1e7 bei 5-10 um | [S, STELLE-24M] |
| Kurzabstand | Blakemore u. a., PRD 104, 061101 | 02/2021 | \|alpha\| >~ 1e8 fuer lambda > 10 um ausgeschlossen, Vorzeichen getrennt | [S Abstract] |
| Potenzgesetz / fat graviton | Adelberger, Heckel, Hoedl, Hoyle, Kapner, Upadhye, PRL 98, 131104 | 11/2006 (2007) | \|beta_3\| <= 1,3e-4 (68 %); l_g <= 98 um (95 %) | [S Volltext] |
| Sterne / SN 1987A | Hardy, Sokolov, Stubbs, 2510.18975 | 10/2025 | "For 1 extra dimension, the bounds are weaker than those from laboratory searches"; Zerfallsschranken schwaecher als Kuehlung bei "typically assumed" KK-Verletzung | [S Abstract] |
| BBN, KK-Freeze-in | Gross, Hooper, 2407.07529 | 07/2024 | n = 1: M_* > 2e13 GeV, "unless the temperature ... was never greater than T ~ 2 TeV"; die DD (T_RH ~ GeV) entgeht nur ueber die Temperatur | [S Abstract; H] |
| Reheating-Untergrenze | Barbieri u. a., 2501.01369; PRL 135, 181003 | 01/2025 | T_RH > 5,96 MeV (95 %) | [S Abstract] |
| MeV-Gamma | Langhoff, 2610.01825 | 10/2026 | R <~ 0,2 um (flach) | [S] |
| DM-Kaskade | Lee/Randall/Riojas, 2609.36234 | 09/2026 | GMOV-DM ausgeschlossen | [S] |
| Energieeinspeisung gegen Kick | Langhoff/Ramos/Reig, 2607.27314 | 07/2026 | einfachste DD-DM ausgeschlossen; Fuenfte Kraft schliesst Delta m_KK <~ 5 meV aus | [S] |
| Kosmologie, dunkle Gravitonen | Pourtsidou, 2607.13910 | 07/2026 | aktualisierte CMB+BAO-Schranken, Euclid/LSST koennten "confirm or rule out" | [L? Zahlen nicht im Abstract] |
| Delta N_eff, Bulk-Neutrinos | McKeen/Ng/Shamma, PRD 110, 083507 | 06/2024 | "generically rule out micron-sized extra dimensions", Ausweg niedriges T_RH | [S Abstract] |
| Gegenrede dazu | Anchordoqui/Antoniadis/Luest/Penaló Castillo, 2411.07029 | 11/2024 | modellabhaengig; Turm-interne Zerfaelle; delta n ~ 0,2 | [S Volltext] |
| Neutrino-Oszillation | Eller/Ettengruber/Zander, 2508.04274 | 08/2025 | MINOS/MINOS+, KamLAND, Daya Bay: keine Signatur; Radius-Schranken je nach Bulk-Masse und Yukawa | [S Abstract] |
| Neutrino-Oszillation | Bai u. a., 2601.00790 | 01/2026 | T2K, NOvA: "stringent exclusion limit" auf Modellparameter | [S Abstract] |
| Beta-Zerfall | Antoniadis/Chatrabhuti/Isono, 2509.05233 | 09/2025 | grosser Teil des Parameterraums in KATRIN-Reichweite (Projektion) | [S Abstract] |
| Protonzerfall | Reig/Ruiz, 2510.25832; JHEP 2026, 293 | 10/2025 | in der Horava-Witten-Einbettung R <~ 1e-28 m; trifft diese Stringeinbettung, nicht die DD allgemein | [S Abstract] |
| Massive Spin-2 aus ALP-Suchen | Gue/d'Enterria, 2605.00549; JHEP 09 (2026) 220 | 05/2026 | ALP-Suchen setzen "not ... stronger bounds" als Fuenfte-Kraft-Tests | [S Abstract] |
| Collider | - | - | 5D-Planck-Skala ~1e9-1e10 GeV (MVV), weit jenseits der LHC; die LHC-KK-Schranken (de Giorgi u. a. 2607.12012) gelten TeV-Tuermen | [H] |

### Frage 4: Was bleibt im Labor pruefbar, und wann?

- **Erwartetes Signal:**
  - Flache DD mit Brane am Fixpunkt: Yukawa mit alpha = +8/3, lambda = R. Gravitation wird darunter staerker
    (Adelberger/Heckel/Nelson 2003; GS2 [E]).
  - Ein leichter Radion gaebe eine zusaetzliche skalare Kraft. MVV verlangen, dass er schwer oder entkoppelt ist
    (aus DUNKEL-ZEIT).
  - Blase: -(3/2)(L/r)^2, Gravitation schwaecher, Potenzgesetz [S].
- **Wo die DD laege:**
  - MVV 0,1-10 um, Casimir-Schaetzung 7,4 um
  - DM-Variante (Law-Smith u. a.) 1-30 um
  - nach Langhoff R <~ 0,2 um
  - Blase L ~ 10-50 um
- **Heutige Grenze fuer alpha > 0** (Murata/Fujiie/Suzuki 2605.18212v2, Abb. 3 und 4; Ablesung nach Augenmass auf
  Log-Achsen) [S Abb.]:
  - lambda = 10 um: alpha ~ 1e4; 1 um: ~1e8-1e9; 0,2 um: ~1e11-1e12; 0,1 um: ~1e12-1e13
  - alpha = 1 erst ab ~40 um ("Washington 2020")
  - Murata: unter 1 um sind Casimir-Versuche "the practical limit for mechanical gravity tests" [S]
- **[E] Abstand zur Erwartung alpha = 8/3:** bei 7,4 um rund 3-4 Groessenordnungen, bei 1 um ~8, bei 0,2 um ~11.
- **Laufende und angekuendigte Projekte** (keines mit Zeitplan fuer alpha ~ 1 unter 10 um):

| Projekt | Status | Reichweite | Marke |
|---|---|---|---|
| Mikro-Torsionsresonatoren (Manley, Condos, Schlamminger, Pratt, Wilson, Terrano; PRD 110, 122005; ausdruecklich mit der DD begruendet) | Vorschlag, Prototyp gefertigt | Raumtemperatur: neue Flaeche fuer 3 um <~ lambda <~ 36 um; \|alpha\| = 1 erst kryogen bei 100 mK "potentially" bei lambda_min ~ 10 um, s0 ~ 25 um | [S Volltext] |
| Mikro-Orbits (Baeza-Ballesteros/Donini/Nadal-Gisbert, EPJC 82, 154) | Papierstudie; 2023 erst Luftreibung untersucht | alpha ~ 1 bis lambda <~ 5-7 um (Fall 1) bzw. 10-20 um (Fall 2) | [S Volltext] |
| Meissner-levitierte Mikrokugel (Ren u. a. 2602.13829) | Vorschlag | 0,1-10 um, ~1e-19 N/sqrt(Hz) bei mK; keine alpha-Zahl im Abstract | [S Abstract] |
| Optisch levitierte Kugeln (Stanford: Blakemore 2021, Venugopalan 2024/26) | gemessen | 1e8 bzw. 1e6-1e7 | [S Abstract; STELLE-24M] |
| Quantenreflexion (Boynewicz/Sackett 2511.08770) | Vorschlag | "approaching" makroskopische Versuche | [S Abstract] |
| MeV-Teleskope (AMEGO-X, e-ASTROGAM) | Missionskonzepte | Faktor 10 im Fluss verschiebt Langhoffs T_RH-Grenze (Abb. 1, "projected") | [S Langhoff] |

- Langhoff/Ramos/Reig: Schon eine Verbesserung der Fuenfte-Kraft-Schranke um den Faktor 6 in Delta m_KK "would
  already exclude most models with N < 10^4" (Axiverse-Variante) [S].
  - [E] 5 meV entspricht 39 um, Faktor 6 also ~7 um. Hier ist ein Labor-Fortschritt im Bereich 5-10 um direkt
    entscheidend.
- **Reicht die geplante Empfindlichkeit?** [H]
  - Fuer die flache DD nach Langhoff (<= 0,2 um): nein, um rund 11 Groessenordnungen.
  - Fuer MVVs Casimir-Wert 7,4 um (falls Langhoff faellt): nur der Mikro-Orbit-Vorschlag kaeme auf dem Papier hin.
  - Fuer die Blase: schon die Daten von 2007 reichen bis L ~ 9 um [E]. Eine eigene Auswertung mit Lee-2020-Daten und
    Apparateantwort wuerde das schaerfen.

### Frage 5: Was bedeutet das fuer uns?

- **Glied 10 der Spin-2-Kette** (Kurzabstand, Stelle-Form, Vorzeichen) [H]:
  - Kein neuer Messbefund. Die Einordnung vom 02.10. (Nachtrag 19:24:11) bleibt stehen.
  - Neu ist die Landkarte der Muster im zugaenglichen Fenster 5-60 um:
    - flache DD: ein Yukawa-Term, +8/3, staerker. Faellt dort heraus, falls Langhoff haelt.
    - Stelle: zwei Yukawa-Terme, +1/3 und -4/3, Summe -1, Vorzeichenwechsel moeglich (STELLE-24M, Regime B).
    - Blase: ein Potenzgesetz, schwaecher, mit langem Auslaeufer; durch Eot-Wash-Potenzgesetzschranken schon eingeengt
      [E].
  - Damit wird die Vorzeichen- und Formauswertung (Yukawa gegen Potenzgesetz) wichtiger als jede Einzelkurve fuer
    |alpha|.
  - Die Glieder 2 und 5 mit dem Faktor-3-Befund beruehrt das nicht.
- **Finns "dunkle Dimension fuer Zusammenhalt und Zeit"** [H, getrennt gefuehrt]:
  - Zusammenhalt: In der flachen DD waere Gravitation unter R staerker. Genau diese Variante ist unter Druck und
    wirkte, wenn ueberhaupt, nur unter 0,2 um.
  - In der Blase wird Gravitation auf kleinen Skalen schwaecher, sie "schaltet ab". Das ist das Gegenteil von
    Zusammenhalt.
  - Die neue Literatur stuetzt "Zusammenhalt durch eine dunkle Dimension" im Mikrometerbereich also nicht.
  - Zeit: Die DD-Arbeiten dieser Karte sagen nichts zur Zeit; es gilt DUNKEL-ZEIT (Uhren messen nur Verhaeltnisse).
  - Am staerksten getroffen ist der Teil "dunkel" im Sinn von Dunkler Materie.

---

## 4. Tabelle E1 bis E4

| Nr | Erwartung (Leitung) | Ausgang | Beleg |
|---|---|---|---|
| E1 (85 %) | Auf keine der beiden neuen Arbeiten gibt es schon eine veroeffentlichte Antwort oder Widerlegung | **eingetroffen** | Semantic Scholar: LRR 1 Zitat (Langhoff), Langhoff 0; INSPIRE dasselbe; arXiv "dark dimension" juengster Eintrag Langhoff; Urheber zuletzt vor dem 28.09.; OpenAlex ab 01.09.: keine Antwort [S]. Fenster 1 bzw. 4 Tage |
| E2 (60 %) | Langhoffs Ausschluss haengt an einer Modellannahme (flach bzw. Produktionskanal), die verzerrte Varianten umgehen koennen | **teils eingetroffen** | Modellannahmen ja: flach bzw. schwach gewarpt, Fixpunkt-Brane, keine weiteren Zerfallskanaele [Lesart H], eigene Freeze-in-Formel, T_RH >= 5,96 MeV [S]. Der Produktionskanal ist aber irreduzibel (Brane-Kopplung Gl. 1). Die Schwellenunterdrueckung gilt fuer jeden statischen Warp (Gl. 25), Warping allein umgeht sie nicht. Umgehen nur ueber anderes Spektrum (LRR-Begleitarbeit, nicht erschienen) oder ausserhalb des Rahmens (Blase) |
| E3 (60 %) | LRR greifen die DM-Kaskade an, nicht die Existenz der Zusatzdimension | **eingetroffen** | "the suggestion by GMOV [8, 9] is ruled out by decays to the Standard Model"; keine R-Schranke; ob irgendeine Kaskaden-DM funktioniert, "remains open" [S] |
| E4 (70 %) | Kein laufendes oder angekuendigtes Experiment erreicht in zwei Jahren Gravitationsstaerke unter 10 um | **eingetroffen (streng)** | Manley u. a.: \|alpha\| = 1 bestenfalls kryogen bei ~10 um, ohne Zeitplan [S]. Heutige Grenzen 1e4 (10 um) bis 1e12 (0,2 um) [S Abb.]. Einschraenkung: Der Papiervorschlag Mikro-Orbits beansprucht alpha ~ 1 bis 5-7 um; ein Bau ist nicht belegt [S] |

---

## 5. Zeitleiste der Dark-Dimension-Literatur 2022 bis heute

Datum = arXiv-Erstfassung (published) laut API, wo nicht anders vermerkt.

| Datum | Arbeit | Kern | Marke |
|---|---|---|---|
| 24.05.2022 | Montero/Vafa/Valenzuela, 2205.12293 (JHEP 2023, 22) | eine Dimension, l ~ 0,1-10 um, Casimir 7,4 um, 5D-Planck ~1e9-1e10 GeV | [S, DUNKEL-ZEIT] |
| 01.08.2022 | Blumenhagen/Brinkmann/Makridou, 2208.01057 | gewarpter Hals realisiert m ~ Lambda^(1/4) | [S Abstract] |
| 19.09.2022 | Gonzalo/Montero/Obied/Vafa, 2209.09249 (JHEP 11 (2023) 109) | dunkle Gravitonen als DM, Kaskade mit naiver Rate (Gl. 3.2) | [S Volltext] |
| 20.07.2023 | Law-Smith/Obied/Prabhu/Vafa, 2307.11048 (JHEP 06 (2024) 047) | Astro-Schranken vertraeglich, R ~ 1-30 um | [S Abstract, DUNKEL-ZEIT] |
| 09.11.2023 | Obied/Dvorkin/Gonzalo/Vafa, 2311.05318 (PRD 109, 063540) | Kick-Geschwindigkeit, Zerfaelle | [S Stellen] |
| 24.11.2023 | Danielsson/Panizo, 2311.14589 (PRD 109, 026003) | Blase: Dimension 5e-5 m, Stringskala 11 TeV | [S Abstract] |
| 01.02.2024 | Vafa, 2402.00981 | Uebersicht, "consistent with ... inverse square law" | [S, DUNKEL-ZEIT] |
| 19.03.2024 | Schwarz, 2403.12899 | Kommentare, Intervall mit zwei Branen | [S, DUNKEL-ZEIT] |
| 07.06.2024 | McKeen/Ng/Shamma, 2406.05266 (PRD 110, 083507) | Delta N_eff: um-Dimensionen "generically" ausgeschlossen | [S Abstract] |
| 06/2024 | Manley u. a., 2406.13020 (PRD 110, 122005) | Mikro-Torsion, DD-motiviert, Projektion | [S Volltext] |
| 10.07.2024 | Gross/Hooper, 2407.07529 | BBN gegen KK-Freeze-in | [S Abstract] |
| 11.11.2024 | Anchordoqui/Antoniadis/Luest/Penaló Castillo, 2411.07029 | Gegenrede zu McKeen u. a. | [S Volltext] |
| 17.12.2024 | Venugopalan u. a., 2412.13167 (Sci. Rep. 16, 5180 (2026)) | 6-um-Abstand, alpha ~ 1e6-1e7 | [S, STELLE-24M] |
| 02.01.2025 | Barbieri u. a., 2501.01369 (PRL 135, 181003) | T_RH > 5,96 MeV | [S Abstract] |
| 20.01.2025 | Anchordoqui/Antoniadis/Luest, 2501.11690 | zwei um-Dimensionen, nur mit Feinabstimmung | [S, DUNKEL-ZEIT] |
| 03.07.2025 | Bedroya/Obied/Vafa/Wu, 2507.03090 | laufender Radius, DESI | [S, DUNKEL-ZEIT] |
| 06.08.2025 | Eller/Ettengruber/Zander, 2508.04274 | Neutrino-Oszillationen, Radius-Schranken | [S Abstract] |
| 05.09.2025 | Antoniadis/Chatrabhuti/Isono, 2509.05233 | KATRIN-Reichweite | [S Abstract] |
| 21.10.2025 | Hardy/Sokolov/Stubbs, 2510.18975 | Sternkuehlung; n = 1 schwaecher als Labor | [S Abstract] |
| 29.10.2025 | Reig/Ruiz, 2510.25832 (JHEP 2026, 293) | Protonzerfall gegen Horava-Witten-Intervall | [S Abstract] |
| 11/2025 | Danielsson/Giri, 2511.21362 (PRD 113, 126010) | Blase: Gravitation schwaecher bei ~1e-5 m | [S Abstract und Volltext] |
| 09.12.2025 | Montero/Vafa/Valenzuela, 2512.09052 | B-L, Neutrinos, m_nu ~ m_KK | [S Abstract] |
| 02.01.2026 | Bai u. a., 2601.00790 | T2K/NOvA-Schranken | [S Abstract] |
| 01.05.2026 | Gue/d'Enterria, 2605.00549 (JHEP 09 (2026) 220) | ALP-Umrechnung, nicht staerker als Fuenfte Kraft | [S Abstract] |
| 18.05.2026 | Murata/Fujiie/Suzuki, 2605.18212 (v2 09/2026) | Uebersicht Kurzabstand | [S Text, Abb.] |
| 18.06.2026 | Danielsson/Giri, 2606.20942 | Blase = DD plus fat graviton | [S Volltext] |
| 15.07.2026 | Pourtsidou, 2607.13910 | CMB+BAO fuer dunkle Gravitonen | [L?] |
| 29.07.2026 | Langhoff/Ramos/Reig, 2607.27314 | einfachste DD-DM ausgeschlossen; Axiverse-Ausweg | [S Volltext-Stellen] |
| 21.09.2026 | Stewart, 2609.25230 | Stasis, Randbefund | [S Abstract] |
| 28.09.2026 | Lee/Randall/Riojas, 2609.36234 | universelle q^5-Rate, GMOV-DM ausgeschlossen | [S Volltext] |
| 01.10.2026 | Langhoff, 2610.01825 | d-Welle; flache DD nur mit R <~ 0,2 um | [S Volltext] |

---

## 6. Regime, Unterscheidungspunkte, Kopplung, Gegensweep, Kalibrierung, offene Fragen

### 6.1 Regime und Moderatoren (Feldregel 1)

- **GMOV gegen LRR/Langhoff (Zerfallsrate):**
  - Kein Lagerstreit, sondern zwei kinematische Regime. Moderator ist Q/mu, die freiwerdende Energie relativ zur
    reduzierten Masse.
  - Fern der Schwelle (Q ~ m) liegt die naive Skala nicht grob daneben. Nahe der Schwelle (Q << mu) gilt die
    d-Wellen-Rate.
  - Das DD-DM-Szenario liegt per Konstruktion im Schwellenregime, denn es braucht kalte Dunkle Materie (Langhoff
    Einleitung) [S/H].
- **Hardy u. a. 2025 gegen Langhoff 2026 (wie stark Zerfaelle begrenzen):** Moderator ist die Geschwindigkeit der
  Kaskade. Bei schneller Kaskade sind Zerfallsschranken schwaecher als die Kuehlung, ohne Kaskade bleibt die
  Population schwer und zerfaellt sichtbar [S/H].
- **McKeen u. a. gegen Anchordoqui u. a. (Delta N_eff):** Moderatoren sind die Rate Turm-interner Zerfaelle und T_RH
  [S].
- **Flache DD gegen Blase:** Moderator ist die Realisierung, also kompaktes Intervall mit Brane gegen AdS5-Blase mit
  induzierter Gravitation. Das Vorzeichen und die Form der Abweichung kippen [S].

### 6.2 Unterscheidungspunkte (Feldregel 2)

- **Flache DD gegen keine Zusatzdimension:**
  - Unterscheidet bei r <~ R mit alpha = 8/3. Nach Langhoff ist das <= 0,2 um und im Labor um ~11 Groessenordnungen
    unzugaenglich [E].
  - Zugaenglich ist stattdessen die MeV-Gamma-Linienstruktur der irreduziblen Population: Photonen bei E = m_n/2 [S].
- **Naive Rate (GMOV) gegen q^5 (LRR/Langhoff):**
  - Theoretisch entscheidet die Amplitudenrechnung; zwei Rechnungen und die Summenregel-Literatur stimmen ueberein.
  - Empirisch trennen die Massenentwicklung der DM (m ~ t^(-2/3) gegen t^(-2/7)) und die Kick-Geschwindigkeiten,
    pruefbar ueber Strukturbildung (Euclid/LSST, Pourtsidou) [S/H].
- **Flache DD gegen Blase:**
  - Yukawa +8/3 bei lambda = R (staerker, kurz) gegen -(3/2)(L/r)^2 (schwaecher, langer Auslaeufer).
  - Torsionswaagen bei 50 um bis mm sehen den Auslaeufer der Blase, aber nicht den Yukawa-Term einer 0,2-um-Dimension
    [E/H]. Die Daten dafuer existieren seit 2007.
- **Stelle gegen DD gegen Blase (Glied 10):** Unterscheiden lassen sie sich nur durch eine Auswertung, die Vorzeichen
  und Form trennt. Lee 2020 zeigt im Haupttext nur |alpha| (STELLE-24M).

### 6.3 Kopplung und Takt vor Bauteil (Feldregel 6)

- "Die DD-Dunkle-Materie scheitert" hat mindestens drei Wege:
  - Delta N_eff aus Bulk-Neutrinos (2024)
  - Energieeinspeisung gegen Kick-Geschwindigkeit (07/2026)
  - Schwellenunterdrueckung der Kaskade (09/10 2026)
- [H] Die gemeinsame Groesse ist kein Bauteil, sondern die Besetzung des Turms: die Zahl zugaenglicher Moden
  N ~ T_RH R (bei GMOV ~1e11; Langhoff Z. 45) und deren Umverteilungsrate.
  - Gross/Hooper (T_max < 2 TeV), McKeen u. a. (Ausweg niedriges T_RH) und Langhoff (Boden T_RH >= 5,96 MeV) drehen
    alle an derselben Stellschraube T_RH.
  - Die kosmologische Lebensfaehigkeit der DD haengt daher an einem Fenster in T_RH, nicht an einem einzelnen Effekt.

### 6.4 Gegensweep-Befunde (Feldregel 4)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | Geprueft? | Ergebnis |
|---|---|---|---|
| GS1 | Die Kartendaten stimmen | ja (API) | vertauscht |
| GS2 | alpha = 8/3 gilt fuer Langhoffs Fixpunkt-Brane | ja [E] | psi_n^2(0)/psi_0^2 = 2, also 8/3 und lambda = R |
| GS3 | Die Blase ist mit heutigen Daten vereinbar, weil niemand das Gegenteil schreibt | **ja (Adelberger 2007, Volltext)** | L <~ 9 um (68 %) [E]; fat graviton l_g <= 98 um (95 %) [S]. Groesster Befund dieses Laufs |
| GS4 | Reaktionen erscheinen auf arXiv | teils (S2, INSPIRE, OpenAlex) | keine; Blogs, Vortraege und soziale Medien nicht abgedeckt |
| GS5 | Langhoffs Freeze-in-Formel ist unabhaengig geprueft | nein | eigene unbegutachtete Arbeit; ein Abgleich mit Gross/Hooper fehlt |
| GS6 | MVVs l und Langhoffs R sind dieselbe Groesse | [H] | nur Groessenordnung; Faktoren 2 pi aendern die Aussage nicht |
| GS7 | Gewarpte Varianten umgehen die Schwellenunterdrueckung | ja (Gl. 25; LRR App. A/B) | nein, nur ueber ein anderes Spektrum |
| GS8 | Die T_RH-Untergrenze ist robust | teils | 5,96 MeV (95 %); [E] 20 % tiefer verschiebt die R-Grenze um etwa Faktor 2 |

### 6.5 Kalibrierung

- **(a) Gemessen:**
  - Kurzabstand: Lee 2020, Kapner 2007, Adelberger 2007 (Potenzgesetz, fat graviton), Blakemore 2021, Venugopalan
    2024/26
  - COMPTEL/EGRET-Spektren (von Langhoff genutzt)
  - BBN/CMB/BAO-Analyse fuer T_RH
  - Neutrino-Oszillationsdaten ohne Signatur
- **(b) Nuetzlich verdichtet:**
  - Langhoffs R <~ 0,2 um (Theorie plus Daten, unbegutachtet)
  - LRRs q^5-Rate
  - meine Grenze L <~ 9 um fuer die Blase [E]
  - Ablesungen der alpha-Grenzen aus Murata Abb. 3/4 (Augenmass)
  - Regime-Lesart Q/mu
- **(c) Nur gewachsene Gewissheit:**
  - "Die DD-Dunkle-Materie ist erledigt." Das stuetzt sich auf zwei unbegutachtete Preprints, 1 und 4 Tage alt, ohne
    Antwort. Dafuer spricht die Summenregel-Literatur seit 2019; die Urheber haben aber noch nicht geantwortet.
  - "Keine Antwort" ist negative Evidenz aus einem sehr kurzen Fenster.
- **Warnzeichen:**
  - Meine Sicherheit, dass die Blase schon eingeengt ist, stieg aus einer einzigen Kopfrechnung, ohne Apparateantwort
    und ohne Veroeffentlichung, die das so auswertet.
  - Zugleich zerfiel die Frage in flach, schwach gewarpt, stark gewarpt und Blase, jeweils mit oder ohne DM, und in
    drei Vorzeichenmuster.
  - Die Antwort auf E1-E4 ist sicherer geworden, die Antwort auf "wo und mit welchem Vorzeichen laege das Signal"
    unschaerfer.

### 6.6 Offene Fragen

1. Haelt Langhoffs irreduzible Schranke?
   - Unabhaengig zu pruefen sind die Freeze-in-Formel (2607.27314) und die Gamma-Auswertung.
   - Abzuwarten ist eine Antwort von Vafa, Montero, Obied, Gonzalo bzw. Anchordoqui, Antoniadis, Luest.
   - Vorschlag: den Scout auf "dark dimension" und auf Zitate von 2609.36234/2610.01825 ansetzen.
2. Die LRR-Begleitarbeit zu RS ("to appear"): Welche Parameter rettet Warping?
3. Trifft die Schwellenunterdrueckung auch
   - die Turm-internen Neutrino-Zerfaelle, auf die sich die Gegenrede gegen McKeen u. a. stuetzt?
   - die Fragmentation zwischen Axion-Tuermen im Axiverse-Ausweg?
4. Blase gegen Eot-Wash: eine Anpassung von -(3/2)(L/r)^2 mit Apparateantwort an die Daten von Lee 2020. Das ist ein
   Rechenauftrag, keine Literaturfrage, und nach Recherchestand nirgends veroeffentlicht.
5. Vorzeichengetrennte Lee-2020-Schranken (Supplement, APS-Zugang), offen aus STELLE-24M (R2).
6. Rueckfrage R1 aus DUNKEL-ZEIT ("Seiten einer Dimension") bleibt offen; nicht Teil dieser Karte.

---

## 7. Suchprotokoll und Grenzen

Zeiten nach date (CEST, 02.10.2026). Je Block stehen Erwartung, Abruf und Ausgang einzeln in `ARBEITSFELD.md`.

| Block | Erwartung geschrieben | Abfragen | Ergebnis / Fehlschlag |
|---|---|---|---|
| A1 | 21:26:36 | arXiv-API id_list (3); PDFs Langhoff, LRR, D/G -> pdftotext | Daten der Karte vertauscht |
| A2 | 21:28:20 | LRR-Volltext (Einleitung, Abschnitt III, Diskussion, Literatur) | - |
| C1 | 21:29:10 | Semantic Scholar citations (2); INSPIRE (2 + recid 3); arXiv "dark dimension" (60) | INSPIRE "refersto:arxiv:" Fehlschlag (Fremdtreffer), mit recid korrekt |
| C2 | 21:30:00 | arXiv Urheber-Autoren (25); au:Randall_L; "Kaluza-Klein graviton" (25) | au:Randall_L Fehlschlag (andere Randalls) |
| D1 | 21:30:37 | API 12 Abstracts (Schranken) | - |
| D3/D2 | 21:31:39 | Volltexte AAL 2411.07029, LRRe 2607.27314; au:Riojas | Begleitarbeit nicht auf arXiv |
| B1 | 21:32:24 | D/G-Volltext 2606.20942; "dark dimension"+warped; Abstracts 2511.21362, 2311.14589 | - |
| B2 | 21:33:22 | Volltext 2511.21362 (grep) | keine Eot-Wash-Auswertung bei D/G |
| E1 | 21:33:52 | Murata-HTML, Abb. 3 und 4 | - |
| E2 | 21:34:35 | Abstracts Manley, Blumenhagen; arXiv levitated+Yukawa, Casimir+Yukawa+Projektion, short-range; 6 Abstracts; Volltexte Manley, Baeza-Ballesteros | Phrase "short-range" stark verrauscht (Himmelsmechanik, Turbulenz) |
| F1 | 21:36:28 | Volltexte GMOV, ODGV (grep); Abstracts Barbieri, Giudice, Bonifacio, de Giorgi/Vogl, Chivukula, McKeen | - |
| GS3/GS4 | 21:37:34 | Adelberger 2007 (Abstract, Volltext); OpenAlex Volltextsuche ab 01.09.2026 (2 Seiten), 2 Einzelsaetze | OpenAlex-Einzelabruf mit select-Feldern leer, ohne select korrekt |
| D4 | 21:39:05 | arXiv ti:"graviton-like"; Hardy-Abstract | - |
| F2 | 21:39:27 | 4 Abstracts (LRR-Literatur [17-20]) | - |
| Meta | 21:42:18 (Ausgabe des date-Aufrufs im selben Befehl) | Autoren Adelberger 2007, Murata; Metadaten fuer die Zeitleiste | - |

Die Spalte nennt die Erwartungszeit der Bloecke, abgeschrieben aus dem ARBEITSFELD. Eine erste Fassung dieser
Tabelle enthielt sieben falsch uebertragene Zeiten und zwei nicht gemessene Werte bei D4; sie sind hier gegen das
ARBEITSFELD berichtigt.

**Grenzen:**
- WebSearch war erschoepft. Genutzt habe ich arXiv-API, arXiv-Volltexte, Semantic Scholar, INSPIRE und OpenAlex.
- Die arXiv-API kennt nur, was bis zur Ankuendigung am 01.10. abends (US-Ostzeit) erschienen ist. Einreichungen vom
  01.10. nach 14 Uhr ET und vom 02.10. sind nicht sichtbar [H aus dem arXiv-Ablauf, nicht geprueft].
- Volltexte habe ich ueber pdftotext gelesen, bei zweispaltigem Satz mit Gegenprobe im -layout-Text.
- Nicht gelesen:
  - LRR App. B-E im Einzelnen
  - Langhoffs Abb. 1 als Bild
  - Pourtsidou 2607.13910 im Volltext (Zahlen offen)
  - Barbieri u. a. im Volltext (Kanalabhaengigkeit der T_RH-Grenze offen)
- Die alpha-Werte aus Murata Abb. 3/4 sind Augenmass-Ablesungen auf Log-Achsen, nur Groessenordnungen.
- Die Grenze L <~ 9 um fuer die Blase ist Kopfrechnung in fuehrender Ordnung (Punktmassen, rho >> L), ohne
  Apparateantwort, aus einer 68-%-Schranke von 2007.
- Keine Rechnung ausser Kopfrechnung, kein Code, kein python.

---

## 8. Quellenliste

Hauptarbeiten (unbegutachtete Preprints):
- Lee, Randall, Riojas (2026): A Universal Kaluza-Klein Graviton Cascade Rate. https://arxiv.org/abs/2609.36234
- Langhoff (2026): Near Threshold Kaluza-Klein Graviton Decays and the Dark Dimension. https://arxiv.org/abs/2610.01825

Dark Dimension und Varianten:
- Montero, Vafa, Valenzuela (2022/23): The Dark Dimension and the Swampland, JHEP 2023, 22. https://arxiv.org/abs/2205.12293
- Gonzalo, Montero, Obied, Vafa (2022/23): Dark Dimension Gravitons as Dark Matter, JHEP 11 (2023) 109. https://arxiv.org/abs/2209.09249
- Law-Smith, Obied, Prabhu, Vafa (2023/24): Astrophysical Constraints on Decaying Dark Gravitons, JHEP 06 (2024) 047. https://arxiv.org/abs/2307.11048
- Obied, Dvorkin, Gonzalo, Vafa (2023/24): Dark Dimension and Decaying Dark Matter Gravitons, PRD 109, 063540. https://arxiv.org/abs/2311.05318
- Langhoff, Ramos, Reig (2026): The Dark Dimension meets the Axiverse. https://arxiv.org/abs/2607.27314
- Blumenhagen, Brinkmann, Makridou (2022): The Dark Dimension in a Warped Throat. https://arxiv.org/abs/2208.01057
- Danielsson, Giri (2026): Dark bubbles, dark dimensions and fat gravitons. https://arxiv.org/abs/2606.20942
- Danielsson, Giri (2025/26): Weak gravity at micron scales from dark bubble cosmology and its cosmological consequences, PRD 113, 126010. https://arxiv.org/abs/2511.21362
- Danielsson, Panizo (2023/24): Experimental tests of dark bubble cosmology, PRD 109, 026003. https://arxiv.org/abs/2311.14589
- Montero, Vafa, Valenzuela (2025): Neutrinos, B-L Symmetry and the Dark Dimension. https://arxiv.org/abs/2512.09052
- Stewart (2026): Cosmological stasis and the coupled dark sector of the Dark Dimension. https://arxiv.org/abs/2609.25230
- Luest, Masias (2026): A LooKK at the Higuchi Bound. https://arxiv.org/abs/2609.16103

Schranken und Gegenrede:
- McKeen, Ng, Shamma (2024): Signatures of Bulk Neutrinos in the Early Universe, PRD 110, 083507. https://arxiv.org/abs/2406.05266
- Anchordoqui, Antoniadis, Luest, Penaló Castillo (2024): Cosmological Constraints on Dark Neutrino Towers. https://arxiv.org/abs/2411.07029
- Gross, Hooper (2024): Kaluza-Klein Graviton Freeze-In and Big Bang Nucleosynthesis. https://arxiv.org/abs/2407.07529
- Barbieri, Brinckmann, Gariazzo, Lattanzi, Pastor, Pisanti (2025): Current constraints on cosmological scenarios with very low reheating temperatures, PRL 135, 181003. https://arxiv.org/abs/2501.01369
- Hardy, Sokolov, Stubbs (2025): Stellar cooling limits on KK gravitons and dark dimensions. https://arxiv.org/abs/2510.18975
- Eller, Ettengruber, Zander (2025): A neutrino data analysis of extra-dimensional theories with massive bulk fields. https://arxiv.org/abs/2508.04274
- Bai u. a. (2026): Dark Dimension Right-handed Neutrinos Confronted with Long-Baseline Oscillation Experiments. https://arxiv.org/abs/2601.00790
- Antoniadis, Chatrabhuti, Isono (2025): Searching for a Dark Dimension Right-handed Neutrino in KATRIN. https://arxiv.org/abs/2509.05233
- Reig, Ruiz (2025/26): The dark dimension, proton decay, and the length of the M-theory interval, JHEP 2026, 293. https://arxiv.org/abs/2510.25832
- Pourtsidou (2026): Testing string theory with combined cosmological probes: a case study for dark matter gravitons. https://arxiv.org/abs/2607.13910
- Gue, d'Enterria (2026): Bounds on massive graviton-like particles from searches for axion-like particles coupling to photons, JHEP 09 (2026) 220. https://arxiv.org/abs/2605.00549
- Cassem, Kumar (2026): First Search for Kaluza-Klein Gravitons and Radion Using Planck Data. https://arxiv.org/abs/2607.02651

Amplituden-Vorgeschichte:
- Giudice, Kats, McCullough, Torre, Urbano (2018): Clockwork / Linear Dilaton: Structure and Phenomenology, JHEP 06 (2018) 009. https://arxiv.org/abs/1711.08437
- Bonifacio, Hinterbichler (2019): Unitarization from Geometry, JHEP 12, 165 (Angabe laut LRR-Literaturliste). https://arxiv.org/abs/1910.04767
- de Giorgi, Vogl (2021): Dark matter interacting via a massive spin-2 mediator in warped extra-dimensions, JHEP 11 (2021) 036. https://arxiv.org/abs/2105.06794
- Chivukula u. a. (2025): Limits on Kaluza-Klein Portal Dark Matter Models, PRD 111, 075030. https://arxiv.org/abs/2411.02509

Kurzabstand und Labor:
- Lee, Adelberger, Cook, Fleischer, Heckel (2020): New Test of the Gravitational 1/r^2 Law at Separations down to 52 um, PRL 124, 101101. https://arxiv.org/abs/2002.11761
- Kapner u. a. (2007): Tests of the Gravitational Inverse-Square Law below the Dark-Energy Length Scale, PRL 98, 021101. https://arxiv.org/abs/hep-ph/0611184
- Adelberger, Heckel, Hoedl, Hoyle, Kapner, Upadhye (2007): Particle Physics Implications of a Recent Test of the Gravitational Inverse-Square Law, PRL 98, 131104. https://arxiv.org/abs/hep-ph/0611223
- Murata, Fujiie, Suzuki (2026): Short-Range Tests of the Gravitational Inverse-Square Law. https://arxiv.org/abs/2605.18212
- Manley, Condos, Schlamminger, Pratt, Wilson, Terrano (2024): Microscale torsion resonators for short-range gravity experiments, PRD 110, 122005. https://arxiv.org/abs/2406.13020
- Baeza-Ballesteros, Donini, Nadal-Gisbert (2021/22): Dynamical measurements of deviations from Newton's 1/r^2 law, EPJC 82, 154. https://arxiv.org/abs/2106.08611
- Baeza-Ballesteros, Donini, Molina-Terriza u. a. (2023): Towards a realistic setup for a dynamical measurement of deviations from Newton's 1/r^2 law. https://arxiv.org/abs/2312.13736
- Blakemore, Fieguth, Kawasaki u. a. (2021): Search for non-Newtonian interactions at micrometer scale with a levitated test mass, PRD 104, 061101. https://arxiv.org/abs/2102.06848
- Venugopalan, Hardy, Kohn u. a. (2024/26): Optomechanical vector sensing of new forces at 6 micron separation, Sci. Rep. 16, 5180. https://arxiv.org/abs/2412.13167
- Ren, Xu, Broer u. a. (2026): Field-Tunable Meissner-Levitated Ferromagnetic Microsphere Sensor for Cryogenic Casimir and Short-Range Gravity Tests. https://arxiv.org/abs/2602.13829
- Boynewicz, Sackett (2025): Probing short-range gravity using quantum reflection. https://arxiv.org/abs/2511.08770

Projekt (nur Einordnung): KARTE.md; RUNDE-22/dunkel-zeit/ERGEBNIS.md und ARBEITSFELD.md; RUNDE-22/stelle-24m/ERGEBNIS.md;
art-grenzen-20260921/WARUM-SPIN-2.md (Nachtrag 2026-10-02 19:24:11).

---

## 9. Einfach gesagt

Eine bekannte Idee sagt eine versteckte Raumrichtung voraus, etwa ein Tausendstel Millimeter gross, und daraus sollte
auch die unsichtbare Dunkle Materie stammen. Zwei neue, noch ungepruefte Rechnungen zeigen diese Woche: Die Teilchen,
die dafuer zerfallen muessten, zerfallen viel zu langsam, und deshalb funktioniert die Dunkle-Materie-Erklaerung nicht.
Eine der beiden Arbeiten geht weiter: Wenn die versteckte Richtung flach ist, muss sie mindestens fuenfmal kleiner sein
als ein Tausendstel Millimeter, und so fein kann im Labor auf Jahre niemand messen. Geantwortet haben die Erfinder der
Idee noch nicht, die Arbeiten sind erst wenige Tage alt. Eine Spielart mit umgekehrter Wirkung, bei der die Schwerkraft
auf kleinen Abstaenden schwaecher wird, laesst sich dagegen schon mit alten Messungen pruefen, und nach meiner
Ueberschlagsrechnung wird es fuer sie dort bereits eng.
