# X-BAELLE: Alternative X-Ball-Formen und Theorien (Runde 12, explorativ)

- Auftrag X-BAELLE der Leitung claude-primary, 01.10.2026. Anlass Finn woertlich: "und suche mir alternative x-ball
  formen und theorien gibts da noch was spannendes?"
- Bearbeiter: Subagent (Claude). Start 2026-10-01 18:31:05 CEST (date). Zeitbox 50 min, Ende gegen 19:21 CEST.
- Lesetiefe: [A] an der Quelle gelesen, [S] nur Abstract/Suchtreffer, [L?] Gedaechtnis. Nur [A] traegt.
  Eigene Schluesse **[ES]**, Hypothesen [H]. Gestrichenes bleibt stehen (~~ ~~).
- Aufbau: BERICHT oben (zuletzt gefuellt), ARBEITSFELD darunter (chronologisch).

---------------------------------------------------------------------------------------------------------------------

## BERICHT

Bericht geschrieben ab 2026-10-01 18:51:09 CEST (date). WebSearch war ab dem ersten Abruf erschoepft (200/200).
Gesucht wurde deshalb ueber die INSPIRE-API (Titel plus Volltext) und die arXiv-API. Nullbefunde sind darum schwaecher
als nach einer Websuche. [V] heisst: im Projekt schon gelesen, hier nicht wiederholt.

### Kurzfazit (max. 10 Zeilen)

1. Rund 15 Familien. BIC/eingebettete Innenmoden untersucht nur bei Q-Baellen (wir; Ciurla 2024, Evslin 2026 [V]) und
   Soler-Dirac-Solitonen (+-2 omega i, symmetriegeschuetzt, MESS-2 [V]); fuer alle anderen BIC-Suche 0 Treffer.
2. [ES] Eingebettete Moden nur, wo am Modenort genau ein Kanal offen und ein zweiter knapp geschlossen ist. Jenseits
   der zweiten Schwelle schliesst ein Satz sie aus (1211.3336 [S]; 2006.03345 S. 15 [A]); nichtrelativistischen
   Traegern fehlt die zweite Schwelle (RUNDE-10 [V]).
3. ZUSATZ Oszillonen: keine Abstrahlung auf drei Wegen, (a) Integrabilitaet, (b) kein Kontinuum (Log-Potential, ewig
   [A Olle 2021], aber parametrisch instabil [A Ibe 2019]), (c) Ausloeschung des fuehrenden Kanals an Einzelstellen [V].
   BIC einer Oszillon-Innenmode: nichts gefunden.
4. Top 3: ladungstauschende Q-Baelle (angeregte Oszillonen), gravitierender Q-Ball (Bosonenstern im Sextik-Modell),
   B-Ball im flachen SUSY-Potential.

### Erwartungsverstoesse (das Wichtigste zuerst)

1. **"Ewiges" Oszillon heisst "kein Kontinuum", nicht Ausloeschung, und es zerfaellt trotzdem** (gegen E2/E3/E15).
   Olle/Pujolas/Rompineve 2021 [A]: V = -phi^2 log phi hat "classically eternal" Oszillonen, weil "the effective
   mass-squared at the origin blows up". Ibe u. a. 2019 [A]: Das exakte I-Ball gibt es nur im Log-Potential (Gl. 4). Es
   hat Resonanzbaender und bricht je nach I auf.
   Korrektur: Sehr lange Lebensdauern in Log-artigen Potentialen sind kein Beleg fuer Abstrahlungsnullstellen nach
   unserer Art. Das betrifft auch die "extremely stable" Ladungstauscher im SUSY-Log-Potential (Hou/Saffin/Xie 2022
   [S]) [H].
2. **Ein relativistischer Spinor-X-Ball hat exakte eingebettete Eigenwerte, und ein Satz grenzt ihren Ort ein** (gegen
   E13). Soler: +-2 omega i (MESS-2 [V]). Neu fuer das Projekt ist Boussaid/Comech 1211.3336 [S]:
   - keine eingebetteten Eigenwerte "beyond the embedded thresholds";
   - im nichtrelativistischen Limes haeufen sich Punkteigenwerte nur bei 0 und +-2mi.
   Das ist dieselbe Stelle rho ~ 2m, an der RUNDE-10 den Wandzustand fast-NR-Q-Baelle fand [ES, qualitativ].
3. **Ladungstausch ist seit 2025 eine Innenmode** (gegen E8). Alonso-Izquierdo u. a. (JHEP 07 (2025) 100) [S]: "a real
   valued oscillon carrying an excitation in imaginary direction". Das ist der naechste modale Verwandte unserer Leiter
   im Vielkanal-Bereich.
4. **Beim Petrov-Troepfchen liegt die ganze Modenleiter im Kontinuum** (E4 verschaerft). Petrov 2015 [A]: "All
   excitation modes cross the threshold"; fuer 20,1 < N~ < 94,2 "no modes below -mu". Breiten sind dort nicht
   gerechnet. BIC sind nach RUNDE-10 [V] trotzdem nicht zu erwarten.
5. Kleiner: BIC-Sprache an relativistischen Solitonhintergruenden gibt es im integrablen Dirac-Fall
   (Super-Klein-Tunneln an DS-II-Breathern, Correa/Inzunza/Lechtenfeld 2026 [S]). Dort ist das Soliton aber Potential,
   nicht Traeger.
6. Verfahrensfehler, offen gemeldet: Die Titelsuche B1 lief nur im Singular. B16 hat sie im Plural wiederholt, der
   Nullbefund haelt.

### Literaturstand je Familie (Kurzform; Belege in der Quellenliste)

| Familie | Feld, erhaltene Groesse | Stabilitaetsgrund | Groesse/Masse | Innenmoden im Kontinuum / BIC untersucht? | Messbezug |
|---|---|---|---|---|---|
| Q-Ball (unser, Sextik) | komplexer Skalar, globales U(1) Q | E-Minimum bei festem Q | Modelleinheiten, R ~ einige 1/m | **ja**: unsere Leiter; QNM 1D/3D (Ciurla 2024, Evslin 2026, Kovtun 2018) [V] | keiner direkt |
| geeichter Q-Ball | + U(1)-Eichfeld | Q durch Coulomb begrenzt | Q_max endlich [L?] | nein gefunden; Photon = zusaetzlicher offener Kanal [ES] | keiner |
| drehende / radial angeregte Q-Baelle | wie Q-Ball, + Drehimpuls | wie Q-Ball, teils instabil [L?] | Volkov/Woehnert 2002: Rotation in 3+1D, "infinite discrete family of radial excitations" [S] | nein; radiale Anregungen sind nichtlineare Loesungen, keine Leiter-Moden [ES] | keiner |
| Q-Ringe, Q-Strings | wie Q-Ball, + Windung | Noether + topologisch ("semitopological") [S] | Ringradius ~ R | nein | keiner |
| Q-Loecher | Q-Ball auf Kondensat | Dellen in der Ladungsdichte [S] | - | nein; Untergrund luckenlos [ES] | (Kondensate) |
| Q-Wolken | Q-Ball-Haar um Schwarze Loecher [S] | Synchronisation mit dem Horizont | astrophysikalisch | nein; Horizont absorbiert [ES] | BH-Haar |
| ladungstauschende Q-Baelle | komplexer Skalar, Q zeitlich +- | quasistabil, 4 Stufen [S] | wie Q-Ball | **Modensprache ja** (2025, imaginaere Richtung), BIC nein | Affleck-Dine-Fragmentation [S] |
| B-/L-Ball (SUSY, flache Richtung) | Squark/Slepton-Kondensat, B oder L | E/Q < m_Proton (Eichvermittlung) [L?] | makroskopisch, DM-Kandidat [S] | nein | Super-K II: keine Kandidaten [S]; SQM-ISS geplant [S] |
| Bosonen-/Proca-/Dirac-/Axion-Stern | Skalar/Vektor/Spinor + Gravitation, Noether-Ladung | Gravitation + Druck | Axionstern < ~1e-14 M_sun (m_a = 1e-4 eV) [S] | QNM ja [V], BIC/eingebettet: INSPIRE-Volltext 0 | GW190521 als Proca-Verschmelzung vereinbar [S] |
| Oszillon / I-Ball | reeller Skalar, adiabatische Invariante | I fast erhalten [S] | ~1/m | Floquet-Normalmoden (Evslin 2024 [S], 2026 [V]); BIC nein | ALP-Kosmologie [S, Titel] |
| EW-Oszillon | SU(2)xU(1)-Bosonsektor | nur bei m_H = 2 m_W gesehen [S] | ~1/m_W | nein | m_H/m_W = 1,56 gemessen [L?], kein Treffer |
| EW-Baelle, magn. Q-Baelle, Q-Monopol-Ball | geladene Vektoren / AFM / Monopol | wie Q-Ball [V] | - | im Projekt (SPIN1, MESS-3A) | AFM-Labor (laeuft: afm-kanal) |
| Fermi-Ball, Quark-Nugget, Strangelet | Fermionen in falschem Vakuum / Quarkmaterie | Fermi-Druck gegen Vakuum [S] | makroskopisch [S] | nein (INSPIRE 0) | AQN-Haloskop 2025, Makro-DM-Schranken 2026, MQN-Eisenerz 2024, SQM-ISS [S] |
| Soler-Dirac-Soliton (Spinor-Q-Ball) | Dirac-Feld, U(1) | Ladung; spektral teils stabil | ~1/m | **ja**: +-2 omega i eingebettet, Satz zum Ort [V, S] | Labor fraglich (MESS-2: Kerr- statt Soler-Form) [V] |
| Quantentroepfchen | NR-Kondensat (LHY) | Mean-field + Fluktuation | Labor, um 1e4 Atome [L?] | Schwellendurchgang ja (Petrov [A]); BIC nein (RUNDE-10 [V]) | beobachtet [L?] |
| Skyrmion / Hopfion | O(3)/SU(2), topologisch | Topologie | Nukleon / nm-Magnet | Skyrme-Atmung ueberdaempft [V]; magn. Moden gemessen (Onose 2012 [S]); BIC nein | magn. Skyrmionen gemessen; Hopfion-Ringe [L?] |
| Vortonen | U(1)xU(1), Strom + Ladung | Drehimpuls [S] | kosmisch | nein | keiner |

### Regime und Moderatoren (Regel 1)

Vorannahme bestaetigt und verfeinert [ES]. Ob eingebettete Innenmoden moeglich sind, haengt nicht an der Familie,
sondern an der Kanalbilanz am Modenort:

- **R1, genau ein offener Kanal plus schwach geschlossener zweiter Kanal.** Die zweite Schwelle liegt bei m + omega.
  Beispiele: relativistische Traeger mit Teilchen- und Antiteilchen-Zweig, also der Q-Ball (wir), Soler-Dirac
  (+-2 omega i) und der AFM-Ball (offen 1 - Omega, geschlossen 1 + Omega, MESS-3A). Eingebettete Moden sind hier moeglich:
  zufaellig mit Kodimension 1 (wir) oder symmetriegeschuetzt (Soler).
- **R2, keine zweite Schwelle in Reichweite.** Beispiele: NLS, Troepfchen, Schroedinger-Poisson-Kerne, Magnon-BEC in
  3He-B. Der geschlossene Kanal wird nie schwach. Der Wandzustand liegt unter der Emissionsgrenze (RUNDE-10 [V]),
  angeregte Moden verdampfen (Petrov [A]).
- **R3, viele offene Kanaele.** Beispiele: reelle Oszillonen (Harmonische n omega, Seitenbaender rho +- n omega),
  Eichfelder (masseloses Photon), Gravitation bei l >= 2 (GW-Kanal) und luckenlose Kondensatuntergruende (Q-Loecher).
  Eine exakte Nullstelle braucht N Bedingungen (Agmon/Herbst/Maad Sasane [V]). Uebrig bleiben Einzelnullstellen des
  fuehrenden Kanals oder Sonderstrukturen.
- Moderator: die Zahl offener Kanaele N_offen am Modenort und der Abstand zur zweiten Schwelle.

Regel 6 (Kopplung und Takt): Langlebigkeit hat mindestens sechs Wege, naemlich Ladung, Topologie, adiabatische
Invariante, Fermi-Druck, Gravitation und Ausloeschung. Die gemeinsame Groesse ist der Ueberlapp des inneren Takts
(omega, rho, Harmonische) mit dem offenen Kontinuum [ES]:
- Q-Ball: omega < m;
- Oszillon: stirbt ueber 3 omega > m;
- Troepfchen: verdampft, wenn Moden ueber -mu steigen;
- Log-Oszillon: ewig, weil das Kontinuum fehlt;
- Soler: kein eingebetteter Eigenwert, wo zwei Kanaele offen sind.

### Unterscheidungspunkte (Regel 2)

- **U1 symmetriegeschuetzt (Soler) gegen zufaellig (wir):** Geschuetzte Moden gibt es auf ganzen omega-Intervallen
  (|omega| > m/3), zufaellige nur an Einzelstellen.
  - Ein Symmetriebruch macht aus der geschuetzten Mode eine Breite oder eine Instabilitaet (2006.03345 [S]); die
    zufaellige Mode wandert nur.
  - Unsere zertifizierten Stellen liegen isoliert. Damit sind sie zufaellig; das ist schon entschieden [ES].
- **U2 Oszillon "kein Kontinuum" gegen "Ausloeschung" gegen "Integrabilitaet":** Man regularisiert das Log-Potential
  bei kleinem Feld (Abschneider eps) und vergleicht.
  - Kein Kontinuum: Die Lebensdauer bricht mit eps ein.
  - Ausloeschung: Die Nullstelle wandert, der naechste Kanal strahlt mit O(eps^4) (Cornean u. a. [V]).
  - Integrabilitaet: Bei jeder Stoerung delta strahlt es mit O(delta^2).
- **U3 Gravitation, l = 0 gegen l >= 2:** Bei l = 0 kommt kein offener Kanal dazu, die Breite bleibt 0. Bei l >= 2 ist
  der GW-Kanal offen, erwartete Breite proportional alpha^2, alpha = 4 pi G eta^2 [H]. Numerisch zugaenglich,
  astrophysisch praktisch nicht.
- **U4 relativistisch gegen nichtrelativistisch:** Beide trennen sich nur nahe der zweiten Schwelle (rho ~ m + omega,
  fast-NR: rho ~ 2m). Dort sind die Antiteilchenzweige der AFM und der Dirac-Gap-Solitonen zugaenglich, NR-Kondensate
  nicht.

### Bewertung "spannend" (je Kandidat eine Zeile; a BIC-Bezug, b Labor, c Datennaehe, d Neuheit 2024-26)

| Kandidat | a | b | c | d | Grund |
|---|---|---|---|---|---|
| **Ladungstausch / angeregtes Oszillon** | hoch | - | mittel | hoch | gleiche Feldklasse; Innenmode in imaginaerer Richtung (2025); AD-Fragmentation |
| **gravitierender Q-Ball (Bosonenstern, Sextik)** | hoch | - | hoch | mittel | KKL-Familie = unsere Familie [A]; GW190521-Proca-Deutung; sauberer Unterscheidungspunkt l = 0 / l = 2 |
| **B-Ball im flachen Potential** | hoch | - | mittel-hoch | mittel | datennaher Q-Ball (DM, Super-K, SQM-ISS); prueft, ob die Leiter klassenweit gilt |
| Soler-Dirac (Spinor-Q-Ball) | sehr hoch | mittel | - | mittel | staerkster Strukturverwandter; schon MESS-2, K-12 "verwerfen" |
| AFM-/magnetische Q-Baelle | hoch | hoch | - | hoch | laeuft schon (afm-kanal1/2) |
| Log-/exaktes I-Ball | mittel | - | mittel | mittel | Negativkontrolle "kein Kontinuum" |
| EW-Baelle | mittel | - | hoch (SM) | sehr hoch | bei gemessenen Parametern nicht existent (SPIN1 [V]) |
| Proca-Stern | mittel | - | hoch | mittel | mehr Polarisationskanaele, R3-nah |
| Fermi-Ball / AQN / Strangelet | niedrig | - | hoch | mittel | Suchen laufen; keine Feldlinearisierung unserer Art |
| Quantentroepfchen | mittel | hoch | - | niedrig | R2, RUNDE-10 hat es schon; ~~Testkandidat~~ |
| Skyrmion / Hopfion | niedrig | hoch | mittel | mittel | Moden unter der Luecke; Skyrme-Atmung ueberdaempft |
| Q-Loch / Q-Wolke / Vorton / Q-Ring | niedrig-mittel | - | niedrig | niedrig | R3 (luckenlos, Horizont) oder ungeprueft |

### Drei Testvorschlaege (nur vorgeschlagen, nichts gerechnet)

**T1 Ladungstausch-Spitzen.** Frage: Hat die imaginaere Innenmode eines reellen Oszillons an Einzelparametern eine
Nullstelle der fuehrenden Abstrahlung?
- Kleinster Test, ohne Rechnung: die Lebensdauerkarten von Xie/Saffin/Zhou 2021 und Hou/Saffin/Xie 2022 an der Quelle
  lesen.
- Vorab binden: Eine "Spitze" ist eine Lebensdauer >= 10x beider Nachbarwerte einer Parameterreihe.
- Bei einer Spitze zaehlt man N_offen am Modenort aus omega_0 und der Tauschfrequenz (Schreibtisch).
- Scheiterregel:
  - keine Spitze -> Ast schliessen; "unbestimmt" nur, wenn die Reihe die Breite nicht aufloest;
  - Spitze mit N_offen >= 2 -> nur Nullstelle des fuehrenden Kanals, kein BIC;
  - Spitze im Log-Potential -> erst U2 (eps-Regularisierung), sonst Verwechslung mit "kein Kontinuum".

**T2 Q-Stern-Probe.** Frage: Ueberlebt die n = 1-Stelle (l = 0) Gravitation, und wo endet sie?
- Aufbau: radiale Gleichungen an unserem Punkt (a^2/(lambda b) = 2, nicht KKLs 3,64) plus Newton-Potential in
  erster Ordnung in alpha.
- Die Umlaufzahl-Zelle wird ueber alpha in {1e-2, 3e-2, 1e-1} verfolgt. Der Korridor ist vorab gebunden: alte Box plus
  das Dreifache der linearen Verschiebung.
- alpha < 1e-2 zaehlt nicht: Dort ist "Bestehen" wegen der Stetigkeit der Umlaufzahl vorab erzwungen.
- Scheiterregel: Fehlt die +1-Zelle im Korridor, endet die Leiter bei alpha_end (Befund). Besteht, wenn alle drei alpha
  sie zeigen.
- Nullkontrolle: alpha = 0 reproduziert die bekannte Stelle.

**T3 B-Ball-Leiter.** Frage: Ist die Leiter klassenweit oder an den Sextik-Punkt gebunden?
- Vorab Schreibtisch, RUNDE-10-Art: Liegt der nackte Wandzustand des geschlossenen Kanals im Kontinuum? Wenn nein, ist
  der Ausgang vorhersagbar; dann den Test als Mechanismus-Bestaetigung deklarieren.
- Lauf: vorhandene 3D-Radialmaschine mit flachem Potential U(S) = ln(1 + S) [L?, Form vor dem Vertrag an Heeck u. a.
  pruefen] bei drei omega, gleiches Raster wie bei der Sextik-Bestaetigung.
- Nullkontrolle: die Sextik-Stelle mit derselben Maschine.
- Scheiterregel: keine +-1-Zelle im Fenster 1 - omega < rho < 1 + omega bei allen drei omega -> "Leiter nicht
  klassenweit". Besteht nur, wenn eine Zelle im feineren Gitter reproduziert wird.

### ZUSATZ DER LEITUNG: BIC, eingebettete Moden, Abstrahlungsnullstellen bei Oszillonen

- **Ganzes Oszillon:**
  - Unmoeglichkeit fuer kleine phi^4-Breather in 1D: Segur/Kruskal 1987 [S].
  - Starrheitssaetze (nur Sine-Gordon) [L?].
  - Lebensdauer-Resonanzen mit Zeitskalengesetz: Honda/Choptuik 2002 [S].
  - Stark unterdrueckte Raten an Einzelstellen: Zhang u. a. 2020 [V]; nahezu minimal strahlend: Cyncynates/
    Giurgica-Tiron 2021 [V].
  - Exakt nichtstrahlend nur im Log-Potential, ueber "kein Kontinuum" (Olle 2021 [A]); dort fragil (Ibe 2019 [A]).
  - Gitter: exakte diskrete Breather bei beschraenktem Band (MacKay/Aubry 1994) [L?].
- **Innenmoden des Oszillons (Floquet rho +- n omega):**
  - Normalmoden als Monodromie-Eigenvektoren: Evslin u. a. 2024 [S]: "low amplitude oscillons do not reflect small
    amplitude radiation" (Reflexion null, nicht Abstrahlung null).
  - Streumoden bis dritter Ordnung: Bayarsaikhan u. a. 2026 [V]. Wobblerons: Blaschke u. a. 2026 [V].
  - Ladungstausch als Innenmode: 2025 [S].
  - Ein BIC oder eine Breite null einer Oszillon-Innenmode: **nichts gefunden.**
- [ES]: Bei reellen Oszillonen sind fuer grosse |n| alle Seitenbaender offen. Eine exakte Nullstelle ist ohne
  Sonderstruktur nicht generisch, moeglich bleibt nur die Nullstelle des fuehrenden Kanals. Das stuetzt die Vorannahme
  der Leitung; als unmoeglich bewiesen habe ich es fuer 3D nicht gefunden.
- Suchwoerter:
  - INSPIRE fulltext: "bound state(s) in the continuum", "embedded eigenvalue(s)", "embedded mode(s)",
    "embedded soliton(s)", "zero radiation", "radiation vanishes", "vanishing radiation", "quasinormal", jeweils mit
    Titel oscillon(s), breather(s), I-ball(s);
  - arXiv abs: dieselben BIC-Begriffe mit droplet, breather, oscillon, "Q-ball", "boson star";
  - INSPIRE-Titel: "I-ball", "charge-swapping", "fine structure of oscillons".

### Gegensweep-Befunde (Regel 4: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

1. **Geprueft: Trifft das Suchinstrument?** Nein, zunaechst nicht: Die INSPIRE-Titelsuche trifft keine Plurale. Nach
   Kalibrierung (Ciurla 2024 und Kovtun 2018 werden gefunden) und Wiederholung haelt der Nullbefund (B16).
2. **Geprueft: Ist das neu fuers Projekt?** Zweimal nein. Troepfchen hat RUNDE-10, Soler hat MESS-2. Der
   Troepfchen-Test ist gestrichen; bei Soler bleibt nur 1211.3336 neu (B17, B18).
3. **Geprueft: Ist der Bosonenstern unser Modell?** Nur familienweise. KKL nutzen einen anderen Punkt der
   Sextik-Familie [A] (B20); T2 ist darauf angepasst.
4. Nicht geprueft: Ist das Log-Potential der CSQ-Simulationen bei kleinem Feld wirklich K < 0, also ohne Kontinuum? [H]
5. Nicht geprueft: Liegt der NLD-Haeufungspunkt +-2mi quantitativ auf unserer rho ~ 2m-Kurve? [ES, qualitativ]
6. Nicht geprueft: die [V]-Aussagen aus RUNDE-06/07 (Zhang 2020, Agmon u. a.); sie sind uebernommen.

### Offene Fragen

- O1 Hat ein Zweikomponenten-Troepfchen im Spinkanal eine Luecke, also einen schwach geschlossenen zweiten Kanal? Dann
  waere es ein R1-Labor statt R2 [H].
- O2 Vektor-Q-Baelle (Proca) und EW-Baelle: Wie viele Kanaele sind am Modenort offen? Nicht geprueft.
- O3 Gibt es ein Q-Ball-artiges Experiment mit zwei Zweigen (Rabi-gekoppeltes BEC, Dirac-Gap-Soliton)? arXiv: 44
  Treffer, keiner passt (schwach).
- O4 Hopfion-Ringe im Magneten (2023) blieben [L?] (Titelsuche 0).

### Kalibrierung

- (a) Gemessen:
  - GW190521 ist als Signal gemessen; die Proca-Deutung ist eine Modellanpassung [S].
  - Super-K-II-Flussschranken [S]; Skyrmion-Kristallmoden (Onose 2012) [S].
  - 3He-B-Magnon-Q-Ball [V]; Troepfchen [L?].
  - Kein X-Ball mit gemessener eingebetteter Innenmode.
- (b) Nuetzlich verdichtet: Regime R1/R2/R3 nach N_offen und zweiter Schwelle; die drei Wege zu "keine Abstrahlung";
  die Takt-Schwellen-Groesse.
- (c) Gewachsene Gewissheit ohne neue Evidenz: Meine Sicherheit, dass "genau ein offener Kanal plus schwach
  geschlossener zweiter" die Bedingung ist, stieg im Lauf. Sie stuetzt sich auf Projektbestand und Abstracts [S], nicht
  auf neue Rechnungen; die Frage hat sich dabei verfeinert. **Warnzeichen:** R1/R2/R3 ist eine Hypothese, kein Befund.

### Quellenliste (Lesetiefe; URL)

- Ibe M., Kawasaki M., Nakano W., Sonomoto E. (2019): Fragileness of Exact I-ball/Oscillon. PRD 100, 125021 [A, v1].
  https://arxiv.org/abs/1908.11103
- Olle J., Pujolas O., Rompineve F. (2021): Recipes for oscillon longevity. JCAP 09 (2021) 015 [A, v2].
  https://arxiv.org/abs/2012.13409
- Petrov D. S. (2015): Quantum mechanical stabilization of a collapsing Bose-Bose mixture. PRL 115, 155302 [A].
  https://arxiv.org/abs/1506.08419
- Kleihaus B., Kunz J., List M. (2005): Rotating boson stars and Q-balls. PRD 72, 064002 [A, v1, nur Potential].
  https://arxiv.org/abs/gr-qc/0505143
- Boussaid N., Cacciapuoti C., Carlone R., Comech A. (2020): Spectral stability and instability of solitary waves of the
  Dirac equation with concentrated nonlinearity [S; S. 15 aus Projektdatei A]. https://arxiv.org/abs/2006.03345
- Boussaid N., Comech A. (2012): On spectral stability of the nonlinear Dirac equation [S].
  https://arxiv.org/abs/1211.3336
- Alonso-Izquierdo A., Canillas Martinez D., Romanczukiewicz T., Slawinska K. (2025): Excited oscillons and
  charge-swapping. JHEP 07 (2025) 100 [S]. https://arxiv.org/abs/2504.17382
- Copeland E. J., Saffin P. M., Zhou S.-Y. (2014): Charge-Swapping Q-balls. PRL 113, 231603 [S].
  https://arxiv.org/abs/1409.3232
- Xie Q.-X., Saffin P. M., Zhou S.-Y. (2021): Charge-Swapping Q-balls and Their Lifetimes [S].
  https://arxiv.org/abs/2101.06988
- Hou S.-Y., Saffin P. M., Xie Q.-X. (2022): Charge-swapping Q-balls in a logarithmic potential and Affleck-Dine
  condensate fragmentation [S]. https://arxiv.org/abs/2202.08392
- Evslin J., Romanczukiewicz T., Slawinska K., Wereszczynski A. (2024): Normal Modes of the Small-Amplitude Oscillon [S].
  https://arxiv.org/abs/2409.15661
- Stefanov A. G., Stanislavova M., Cuevas-Maraver J., Kevrekidis P. G. (2025): On a Klein-Gordon Reduction for
  Oscillons [S]. https://arxiv.org/abs/2508.12142
- Honda E. P., Choptuik M. W. (2002): Fine structure of oscillons in the spherically symmetric phi^4 Klein-Gordon model.
  PRD 65, 084037 [S]. https://arxiv.org/abs/hep-ph/0110065
- Segur H., Kruskal M. D. (1987): Nonexistence of small-amplitude breather solutions in phi^4 theory. PRL 58, 747 [S,
  INSPIRE-Abstract]. https://doi.org/10.1103/PhysRevLett.58.747
- Murai K., Ogawa T., Takahashi F. (2026): Multifield oscillons/I-balls in the Friedberg-Lee-Sirlin model.
  PRD 114, 036019 [S]. https://arxiv.org/abs/2604.04494
- Kasuya S., Kawasaki M., Takahashi F. (2003): I-balls. PLB 559, 99 [S]. https://arxiv.org/abs/hep-ph/0209358
- Farhi E., Graham N., Khemani V., Markov R., Rosales R. (2005): An oscillon in the SU(2) gauged Higgs model.
  PRD 72, 101701 [S]. https://arxiv.org/abs/hep-th/0505273
- Graham N. (2007): An electroweak oscillon. PRL 98, 101801 [S]. https://arxiv.org/abs/hep-th/0610267
- Correa F., Inzunza L., Lechtenfeld O. (2026): Soliton nature of the super-Klein tunneling effect. PRD 113, 105027 [S].
  https://arxiv.org/abs/2602.02073
- Berte R. (2026): Bound states in the continuum of gravitational waves. Phys. Scr. 101, 325001 [S].
  https://arxiv.org/abs/2609.10620
- Kusenko A., Shaposhnikov M. (1998): Supersymmetric Q-balls as dark matter. PLB 418, 46 [S].
  https://arxiv.org/abs/hep-ph/9709492
- Takenaga Y. u. a. (2007): Search for neutral Q-balls in Super-Kamiokande II. PLB 647, 18 [S].
  https://arxiv.org/abs/hep-ex/0608057
- Brito R., Cardoso V., Herdeiro C., Radu E. (2016): Proca stars. PLB 752, 291 [S]. https://arxiv.org/abs/1508.05395
- Calderon Bustillo J. u. a. (2021): GW190521 as a Merger of Proca Stars. PRL 126, 081101 [S].
  https://arxiv.org/abs/2009.05376
- Finster F., Smoller J., Yau S.-T. (1999): Particle-like solutions of the Einstein-Dirac equations. PRD 59, 104020
  [S]. https://arxiv.org/abs/gr-qc/9801079
- Braaten E., Mohapatra A., Zhang H. (2016): Dense Axion Stars. PRL 117, 121801 [S]. https://arxiv.org/abs/1512.00108
- Levkov D., Panin A., Tkachev I. (2017): Relativistic axions from collapsing Bose stars. PRL 118, 011301 [S].
  https://arxiv.org/abs/1609.03611
- Liebling S., Palenzuela C. (2023): Dynamical boson stars. Living Rev. Rel. 26, 1 [S].
  https://arxiv.org/abs/1202.5809
- Hong J.-P., Jung S., Xie K.-P. (2020): Fermi-ball dark matter from a first-order phase transition. PRD 102, 075028
  [S]. https://arxiv.org/abs/2008.04430
- Zhitnitsky A. (2003): 'Nonbaryonic' dark matter as baryonic color superconductor. JCAP 10, 010 [S].
  https://arxiv.org/abs/hep-ph/0202161
- Kusenko A., Mazumdar A. (2008): Gravitational waves from fragmentation of a primordial scalar condensate into
  Q-balls. PRL 101, 211301 [S]. https://arxiv.org/abs/0807.4554
- Volkov M., Woehnert E. (2002): Spinning Q-balls. PRD 66, 085003 [S]. https://arxiv.org/abs/hep-th/0205157
- Battye R., Cotterill S. (2021): Stable Cosmic Vortons in Bosonic Field Theory. PRL 127, 241601 [S].
  https://arxiv.org/abs/2111.07822
- Nugaev E., Shkerin A., Smolyakov M. (2016): Q-holes. JHEP 12 (2016) 032 [S]. https://arxiv.org/abs/1609.05568
- Axenides M., Floratos E., Komineas S. (2001): Metastable ringlike semitopological solitons. PRL 86, 4459 [S].
  https://arxiv.org/abs/hep-ph/0101193
- Herdeiro C., Kunz J., Radu E. (2018): Probing the universality of synchronised hair ... with Q-clouds. PLB 779, 151
  [S]. https://arxiv.org/abs/1712.04286
- Libanov A. (2025): Can dark-matter Q-balls grow to the mass gap masses? PRD 111, 063540 [S].
  https://arxiv.org/abs/2412.08803
- Onose Y. u. a. (2012): Observation of magnetic excitations of skyrmion crystal in a helimagnetic insulator [S].
  https://arxiv.org/abs/1204.5009
- Photonische BIC-Texturen [S]: https://arxiv.org/abs/2505.15081 ; https://arxiv.org/abs/2602.22634
- Datennaehe [S, INSPIRE]: Bianchi M. u. a. (2024), SQM-ISS, Sensors 24, 5090; Kim J. u. a. (2025), First dedicated
  search for axion-quark-nugget dark matter, PRD 112, L121305; Picker Z. u. a. (2026), https://arxiv.org/abs/2609.05626 ;
  Du Y. u. a. (2023), https://arxiv.org/abs/2306.13122 ; VanDevender J. P. u. a. (2024),
  https://arxiv.org/abs/2402.08163
- Fermi-Ball neu [S, Titel]: https://arxiv.org/abs/2411.17074 ; https://arxiv.org/abs/2501.00131
- Projektbestand [V]: RUNDE-06/07 L4-BIC (Zhang u. a. 2004.01202; Cyncynates/Giurgica-Tiron 2104.02069; Inagaki/
  Murakami 2609.15056; Blaschke u. a. 2606.22680; Bayarsaikhan u. a. 2607.15624; Agmon/Herbst/Maad Sasane 2010;
  Cuccagna/Maeda 2009.00573); RUNDE-10/nls-leiter; MESS-2 (Soler: 0910.0917, 1711.05654); MESS-3A; QUARK-1; SPIN1.
- [L?], nicht geprueft: Coleman 1985; Lee/Stein-Schabes/Watkins/Widrow 1989; Witten 1984; Farhi/Jaffe 1984; Kusenko
  1997; MacKay/Aubry 1994; Kichenassamy 1991; Denzler 1993; Birnir/McKean/Weinstein 1994; Hopfion-Ringe 2023;
  Troepfchen-Experimente 2018.

---------------------------------------------------------------------------------------------------------------------

## ARBEITSFELD

### 0. Vorarbeiten im Projekt (gelesen 18:31 bis 18:34, keine externe Quelle)

- Paper v0.10 LITERATURE.tex: Coleman 1985, Battye/Sutcliffe 2000, Kovtun/Nugaev/Shkerin 2018, Azatov/Ho/Khalil 2024,
  Ciurla/Dorey/Romanczukiewicz/Shnir 2024 (gebunden, halb-propagierend, quasinormal), Evslin u. a. 2026 (Floquet,
  Feshbach-artige QNM, 1+1), Friedrich/Wintgen 1985, Yu/Lu 2025, Malomed u. a. 2005 (eingebettete Solitonen),
  Soffer/Weinstein 1999. Also: Q-Ball-Innenmoden und eingebettete Solitonen sind schon zitiert.
- QUARK-1: B-Ball naechster Verwandter, FL-Beutel = neutrales sigma, Skyrme-Atmungsmode fast ueberdaempft (Bizon 2007),
  quasi-BIC durch Kanalkopplung in Hadronen (Coito 2011), farbige Q-Baelle Loginov 2025, Armstrong-Williams/White 2026.
- MESS-3A: AFM-Baelle (Bar'yakhtar/Ivanov 1983), magnetische Q-Baelle 2609.32059, Kanalstruktur offen 1 - Omega /
  geschlossen 1 + Omega.
- MESS-2 (RUNDE-11): Magnon-Q-Ball in 3He-B (Bunkov/Volovik 2007) schon erfasst, "nichtrelativistisch (ein Zweig)".
- LESUNG-BS2000: B&S = unser Modell; keine linearen/eingebetteten Moden dort.
- SPIN1: Q-Monopol-Ball (Bai/Lu/Orlofsky 2022), Electroweak balls 2609.19293 (Herdeiro u. a.).
- Projektweit schon bekannt (grep): Q-ball superradiance (Saffin/Xie/Zhou 2212.03269; spinning 3+1D 2402.03193),
  Cardoso u. a. 2023 Energieentnahme; Aiello/Heeck 2604.01288; Libanov/Troitsky 2607.28517 (Q-Ball-DM, Halo-Kerne).
  Nicht im Projekt gefunden (grep): Fermi-Ball, Strangelet, Q-hole, Honda/Choptuik, GW190521 nur 1 Datei, I-ball 1 Datei.

### 1. Vorab-Erwartungen (2026-10-01 18:34:14 CEST, date; vor dem ersten externen Abruf)

Leitfrage je Familie: Gibt es Arbeiten zu inneren Moden im Kontinuum / BIC / eingebetteten Eigenwerten?

| Nr | Erwartung vor Abruf | Sicherheit |
|---|---|---|
| E1 | Boson- und Proca-Sterne: Quasinormalmoden breit untersucht (Yoshida u. a. 1994; Macedo u. a. 2013), langlebige "gefangene" Moden bei ultrakompakten Sternen (Lichtring), aber kein BIC-Begriff und keine exakte Strahlungsnullstelle. | 70 % |
| E2 | Oszillonen: Strahlung exponentiell klein (Fodor u. a.), Feinstruktur mit Lebensdauer-Spitzen bei bestimmten Anfangsbreiten (Honda/Choptuik 2002) ist der naechste Verwandte einer Strahlungsnullstelle; kein BIC-Begriff. | 60 % |
| E3 | I-Baelle: adiabatische Invariante (Kasuya/Kawasaki/Takahashi 2003); Innenmoden-Frage nicht als BIC gestellt. | 80 % |
| E4 | Quantentroepfchen (Petrov 2015): "Selbstverdampfung", Anregungsmoden wandern bei kleiner Teilchenzahl ueber die Emissionsschwelle -mu; kein BIC-Anspruch, aber der Schwellendurchgang ist dokumentiert. | 70 % |
| E5 | Magnetische Skyrmionen: Innenmoden (Atmung, CW, CCW) gemessen (Onose u. a. 2012); "BIC" im Magnon-Skyrmion-Kontext hoechstens als 2023-2026-Einzelarbeit. | 30 % fuer BIC-Arbeit |
| E6 | SUSY-B/L-Baelle: Suchen (Super-K, Takenaga u. a. 2007) ohne Fund; Innenmoden nicht untersucht. | 85 % |
| E7 | Fermi-Baelle, Quark-Nuggets, Strangelets: keine Innenmoden-/BIC-Arbeit; Strangelet-Suchen (AMS-02, Mond) ohne Fund. | 85 % |
| E8 | Ladungstauschende Q-Baelle: Copeland/Saffin/Zhou 2014, Lebensdauern Xie/Saffin/Zhou 2021; keine BIC-Sprache. | 75 % |
| E9 | Drehende/angeregte Q-Baelle: Volkov/Woehnert 2002; Stabilitaet teils instabil gegen nichtaxiale Stoerungen; keine Kontinuums-Innenmoden. | 60 % |
| E10 | Q-Ringe (Axenides u. a. 2001), Q-Loecher (Nugaev/Smolyakov), Q-Wolken (Herdeiro u. a.) existieren; keine BIC-Arbeit. | 65 % |
| E11 | Geeichte Q-Baelle (Lee u. a. 1989): Hoechstladung durch Coulomb; Stoerungen untersucht (Gulamov/Nugaev/Panin/Smolyakov 2015), keine BIC. | 70 % |
| E12 | Datennaehe: staerkster Bezug Proca-Stern-Deutung von GW190521 (Calderon Bustillo u. a. 2021); GW aus Q-Ball-Bildung (Kusenko/Mazumdar 2008) plus neue 2024-2026-Arbeiten. | 85 % |
| E13 | Ausserhalb unserer zitierten Q-Ball-Arbeiten gibt es in 2024-2026 keine Arbeit, die BIC/eingebettete Moden in einem X-Ball (ausser 1D-Kinks/Q-Baelle) behauptet. | 70 % |
| E14 | Kinks: eingebettete/"transparente" Wobbling-Moden mit verschwindender Strahlungskopplung gibt es in 1D-Modellen (2019-2025). | 50 % |

Zwei-Regime-Vorannahme (Regel 1), vorab: Ob ein X-Ball eingebettete Innenmoden haben kann, haengt vermutlich an der
Zahl der Kanaele mit verschiedenen Schwellen: relativistischer Traeger mit Teilchen- und Antiteilchen-Seitenband
(omega +- rho, zwei Schwellen 1 -+ omega) gegen nichtrelativistischen Traeger (NLS, Schroedinger-Poisson, Magnon-
Kondensat; beide Kontinua an |mu| gespiegelt). Moderator: Abstand der beiden Schwellen (2 omega gegen 0). Das deckt
sich mit RUNDE-10/nls-leiter (keine stillen Stellen im kubisch-quintischen NLS) [ES, H].

Regel 6 vorab [H]: "Langlebigkeit" hat bei X-Baellen mindestens fuenf Wege (Ladung, Topologie, adiabatische
Invariante, Fermi-Druck, Gravitation). Gemeinsame Takt-Groesse vermutlich: Lage der inneren Frequenzen und ihrer
Harmonischen/Seitenbaender relativ zur Massenschwelle des Kontinuums.

### 1b. ZUSATZ DER LEITUNG (eingegangen ca. 18:35, nicht Teil des Ursprungsauftrags)

Frage: Literatur zu BIC, eingebetteten Moden oder Nullstellen der Abstrahlung bei Oszillonen? Hintergrund der Leitung:
Q-Ball-Leiter braucht zwei Kanaele (omega +- rho); reelles Oszillon hat Floquet-Seitenbaender rho +- n omega, also viele
Kanaele. Ob Stellen ohne Abstrahlung bekannt sind oder als unmoeglich gezeigt. Kurz, im laufenden Budget.

Vorab-Erwartung E15 (2026-10-01 18:35:21 CEST, date, vor jedem Abruf dazu), Sicherheit 60 %:
- (i) 1D, Familienebene: exakte kleine Breather nur bei Sine-Gordon; "Unmoeglichkeit" fuer phi^4 (Segur/Kruskal 1987)
  und Starrheit (Kichenassamy 1991; Denzler 1993; Birnir/McKean/Weinstein 1994) [L?].
- (ii) Gitter: exakte diskrete Breather (MacKay/Aubry 1994), weil das Phononband beschraenkt ist und alle Harmonischen
  ausserhalb liegen koennen [L?]. Moderator: beschraenktes gegen unbeschraenktes Kontinuum.
- (iii) Feldtheorie 2D/3D: Strahlung exponentiell klein (Fodor u. a. 2008/2009), Lebensdauer-Feinstruktur
  (Honda/Choptuik 2002), Potentiale mit unterdrueckter fuehrender Strahlung (Olle/Pujolas/Rompineve 2020; Zhang u. a.
  2020) [L?]; aber keine Arbeit mit BIC-Begriff und keine exakte isolierte Strahlungsnullstelle eines Oszillons.
- [ES] vorab: Bei N offenen Seitenbaendern braucht eine exakte Nullstelle generisch N reelle Bedingungen, also
  N - 1 zusaetzliche Parameter; ohne Symmetrie ist das beim Oszillon nicht generisch.

### 2. Abrufprotokoll (je Abruf: Erwartung -> Befund -> bestaetigt/verletzt)

- 18:36 WebSearch: Kontingent erschoepft (200/200). Ausweich: INSPIRE-API per curl (inkl. fulltext:), arXiv-API per
  curl (https), arxiv.org-PDF. "Nicht gefunden" gilt deshalb als schwaecher als nach einer Websuche.
- 18:36 B1 INSPIRE fulltext "bound state(s) in the continuum"/"embedded eigenvalue" x Titel oscillon / Q-ball /
  breather / boson star. Erwartung: 0 bis 2 Treffer. Befund: je 0. Kalibrierung: fulltext:"bound states in the
  continuum" allein 763 Treffer, Suche funktioniert. -> bestaetigt (E13).
- 18:37 B2 INSPIRE t "Q-ball" x fulltext quasinormal. Erwartung: unsere zitierten Arbeiten. Befund: 2604.07713 (Evslin,
  zitiert), 2509.03192, 2502.20519, 2604.25223 (Q-Ball-Haarloch). Alle ausser 2604.25223 im Projekt bekannt. -> bestaetigt.
- 18:38 B3 Projekt-grep: RUNDE-06/07 L4-BIC-Literatur hat Oszillon-Strahlungsnullstellen schon [V]: Zhang u. a. 2020
  ("exceptionally stable", Rate stark unterdrueckt), Olle/Pujolas/Rompineve 2021 [A dort] ("exceptional potential that
  admits eternal oscillon solutions"), Cyncynates/Giurgica-Tiron 2021, Inagaki/Murakami 2609.15056 (3D-Blase, fuenf
  Nullstellen), Blaschke u. a. 2606.22680, Bayarsaikhan/Evslin/Mahato 2607.15624, Agmon/Herbst/Maad Sasane 2010
  (Kodimension m = Zahl offener Kanaele), Cuccagna/Maeda 2020 (Grundzustaende: keine eingebetteten EW erwartet).
  -> Zusatzfrage zum groessten Teil Projektbestand; hier nur Ergaenzung.
- 18:39 B4 INSPIRE BIC/embedded x Boson-/Proca-/Axion-/Dirac-Stern: 0. Skyrmion/Hopfion x BIC: 2 Fehltreffer (optische
  Skyrmionen, Skyrmion-Qubits). Soliton/Kink/Breather/Vortex/Monopol x BIC seit 2024-09: 1 Treffer, 2602.02073.
  Erwartung E1/E5/E13: kaum etwas. -> bestaetigt; 2602.02073 eigener Punkt (B6).
- 18:39 B5 INSPIRE t "charge-swapping": 4 Treffer, neu darunter 2504.17382 "Excited oscillons and charge-swapping"
  (Alonso-Izquierdo, Canillas Martinez, Romanczukiewicz, Slawinska, JHEP 07 (2025) 100) [S]: "charge-swapping ... real
  valued oscillon carrying an excitation in imaginary direction". Erwartung E8: nur Lebensdauern, keine Modensprache.
  -> **teilweise verletzt**: Ladungstausch ist 2025 als Innenmode (imaginaere Richtung) eines reellen Oszillons gedeutet.
  Im Projekt in 3 Dateien schon erwaehnt.
- 18:39 B5b INSPIRE t "I-ball": 10 Treffer, darunter 1908.11103 "Fragileness of Exact I-ball/Oscillon" (Ibe, Kawasaki,
  Nakano, Sonomoto, PRD 100 125021) und 2604.04494 "Multifield oscillons/I-balls in the Friedberg-Lee-Sirlin model"
  (Murai, Ogawa, Takahashi, PRD 114 036019 (2026)) [S]. Erwartung E3: keine Innenmoden-Frage. -> **verletzt** (B7).
- 18:40 B6 2602.02073 Correa/Inzunza/Lechtenfeld, "Soliton nature of the super-Klein tunneling effect", PRD 113 105027
  (2026) [S]: Dirac-Hamiltonoperatoren aus DS-II-Breathern; bei der SKT-Energie "simultaneously support bound states
  embedded in the continuum". Erwartung: kein relativistisches BIC an Solitonhintergruenden. -> **verletzt**, aber
  integrables Spezialmodell (DS II, Darboux), Soliton ist Potential, nicht Traeger. Bezug zu uns: relativistisch
  (Teilchen/Antiteilchen, Klein-Tunneln) [ES].
- 18:40 B6b 2609.10620 Berte, "Bound states in the continuum of gravitational waves", Phys. Scripta 101 325001 (2026) [S]:
  flaechenlokalisierte Metrikstoerungen; kein X-Ball. Eine Zeile, weiter.
- 18:40 B7 [A] ~~1908.11103v3~~ 1908.11103v1 (Berichtigung 18:53: Stempel im PDF lautet v1, Datei umbenannt) Volltext
  (quellen/, sha256 1f180bfa...). Erwartung: exaktes Oszillon nur in Spezialpotential.
  Befund: "the adiabatic invariant is exactly conserved when the solution ... is completely separable" (S. 3); separierte
  Loesung phi = f(t) psi(x) "is possible only when the scalar potential" logarithmisch ist, V = m^2 phi^2/2 + kappa m^2
  phi^2 log(phi^2/M^2)/2 (Gl. 4); Ursprung Ref. [13] Kawasaki/Takahashi/Takeda 2015. Stoerungen haben "resonance bands",
  das exakte I-Ball bricht je nach I auf ("fragileness", Gitter bestaetigt). -> Erwartung bestaetigt fuer die Existenz,
  **verletzt** fuer die Stabilitaet: Das nichtstrahlende Oszillon ist parametrisch instabil. Das traegt auch die
  [ES]-Vermutung aus RUNDE-07 ("vermutlich logarithmisch") fuer Olle u. a. nur indirekt; deren Potential nicht geprueft.
- 18:40 B8 INSPIRE kanonische Familienarbeiten (18 Abstracts, [S]), Datei scratchpad abs2.txt: Copeland/Saffin/Zhou
  1409.3232; Kusenko/Shaposhnikov hep-ph/9709492; Takenaga u. a. hep-ex/0608057 (Super-K II, keine Kandidaten);
  Brito u. a. 1508.05395; Calderon Bustillo u. a. 2009.05376; Finster/Smoller/Yau gr-qc/9801079; Braaten/Mohapatra/Zhang
  1512.00108; Levkov/Panin/Tkachev 1609.03611; Kasuya/Kawasaki/Takahashi hep-ph/0209358; Farhi u. a. hep-th/0505273;
  Graham hep-th/0610267; Hong/Jung/Xie 2008.04430; Zhitnitsky hep-ph/0202161; Liebling/Palenzuela 1202.5809;
  Kusenko/Mazumdar 0807.4554; Volkov/Woehnert hep-th/0205157 ("infinite discrete family of radial excitations");
  Kleihaus/Kunz/List gr-qc/0505143; Battye/Cotterill 2111.07822. Erwartung E6, E12: bestaetigt.
- 18:41 B9 arXiv-API: Skyrmion/Hopfion x BIC: 4 Treffer, alle photonisch (BIC erzeugt Meron-/Skyrmion-Texturen im
  Impulsraum, 2505.15081, 2602.22634). Quantentroepfchen x "self-evaporation": 6 Treffer (2012.10347 41K-87Rb u. a.),
  Troepfchen/Breather/Oszillon/Q-Ball/Bosonstern x BIC: 1 Fehltreffer (2402.18340, photonisches Gitter).
  Erwartung E4/E5: bestaetigt (keine BIC-Arbeit an magnetischen Skyrmionen oder Troepfchen gefunden, schwach).
  Umkehrung notiert [ES]: In der Photonik ist das BIC selbst ein topologischer Defekt, aus dem Texturen entstehen.
- 18:41 B10 INSPIRE: Honda/Choptuik hep-ph/0110065 [S]: "resonant (and critical) behavior which exhibits a time-scaling
  law", Modenstruktur der kritischen Loesungen. Segur/Kruskal PRL 58 747 (1987) [S]: phi^4 "admits no true breathers"
  im Kleinamplituden-Limes. Erwartung E15 (i), (iii): bestaetigt.
- 18:41 B11 INSPIRE Datennaehe: SQM-ISS (Bianchi u. a., Sensors 24 5090 (2024)) sucht kuenftig SQM, Q-Baelle,
  Fermi-Baelle von der ISS [S]; erste AQN-Haloskopsuche (Kim u. a., PRD 112 L121305 (2025)) [S]; Makro-DM-Schranken
  2609.05626 [S]; GW-Detektoren fuer Makro-DM 2306.13122 [S]; MQN in Eisenerz 2402.08163 [S]. Erwartung E7: bestaetigt
  (nur Schranken und Vorhaben, kein Fund).
- 18:41 B12 INSPIRE Q-Varianten [S]: Q-holes 1609.05568 (Nugaev/Shkerin/Smolyakov, JHEP 12 (2016) 032: "dips or rises"
  in einer Kondensat-Ladungsverteilung); Q-Ringe hep-ph/0101193 (Axenides/Floratos/Komineas, PRL 86 4459: stabil durch
  topologische plus Noether-Ladung, "semitopological"); Q-clouds 1712.04286 (Herdeiro/Kunz/Radu, PLB 779 151),
  1907.04982, 2009.08293 (Q-Wolken um Schwarze Loecher); geladene Q-Baelle 1505.02594, 2402.15396; Q-Ball/Oszillon x
  "gravitational wave" seit 2024-09: nur 2412.08803 (Libanov, PRD 111 063540: DM-Q-Baelle bis in die Massenluecke).
  Erwartung E10/E11: bestaetigt (keine Modenarbeit dabei).
- 18:42 B13 arXiv-API [S]: Petrov 1506.08419 (Troepfchen) "excitation spectrum lies entirely above the particle emission
  threshold"; Onose u. a. 1204.5009 (Skyrmionkristall-Anregungen gemessen); Hopfion-Ringe: Titelsuche 0 (bleibt [L?]);
  Q-Ball/Oszillon x Kondensat/Analogon: 44 Treffer, keine Laborrealisierung darunter; neu 2409.15661 (Evslin,
  Romanczukiewicz, Slawinska, Wereszczynski 2024, "Normal Modes of the Small-Amplitude Oscillon": Monodromie-Eigenvektoren,
  "low amplitude oscillons do not reflect small amplitude radiation"), 2508.12142 (Stefanov/Stanislavova/Cuevas-Maraver/
  Kevrekidis 2025: Reduktion auf erste und dritte Harmonische, VK-Analogon), 2507.01082 (PQ-Ball, im Projekt bekannt).
- 18:42 B14 [A] Petrov, PRL 115 155302 (2015), 1506.08419v2 (quellen/, sha256 0ed5a2da...). Erwartung E4: Moden wandern
  bei kleinem N ueber die Schwelle. Befund S. 3: "All excitation modes cross the threshold for sufficiently small N~.
  Only the monopole mode reenters at N~ = 20.1"; "in the interval 20.1 < N~ < 94.2 there are no modes below -mu";
  "automatically evaporating object". Die Kurven oberhalb der Schwelle sind nur die Naeherung Gl. (12), keine Breiten.
  -> bestaetigt, scharf: ganze Leiter von Moden kreuzt die Schwelle, Breiten dort nicht berechnet.
- 18:43 B15 [A] Olle/Pujolas/Rompineve, JCAP 09 (2021) 015, 2012.13409 (quellen/, sha256 87ca3627...). Erwartung: das
  "Ausnahmepotential" ist logarithmisch (RUNDE-07 [ES]). Befund: "The oscillons in V = -phi^2 log phi are classically
  eternal for any amplitude" (S. 6); Grund: "the effective mass-squared at the origin blows up and so it is
  energetically impossible to emit scalar radiation" (Abschn. 2.2); Amplituden am Potentialmaximum zerfallen ueber
  "unstable resonant modes [30]". -> bestaetigt; Mechanismus ist **kein Kontinuum**, keine Ausloeschung. Damit ist die
  RUNDE-07-Vermutung jetzt [A].
- 18:44 B16 GEGENSWEEP-PRUEFUNG 1 (Suchinstrument): INSPIRE-Titelsuche t "Q-ball" trifft "Q-balls" nicht. Mit Plural:
  (t "Q-ball" or t "Q-balls") x fulltext quasinormal = 10 Treffer, darunter Ciurla u. a. 2405.06591 und Kovtun u. a.
  1805.03518 (Kalibrierung bestanden). B1 hatte "oscillon" nur im Singular. Wiederholt mit Plural und erweiterten
  Begriffen ("embedded mode(s)", "embedded soliton(s)", "embedded eigenvalue(s)", BIC): Oszillon/Breather/I-Ball 2
  Fehltreffer; Boson-/Proca-/Dirac-/Axion-/Bose-Stern 0; Q-Ball/Fermi-Ball/Skyrmion/Hopfion/Vorton 2 Fehltreffer.
  -> Nullbefund haelt nach Korrektur. **Verfahrensfehler B1 offen gemeldet.**
- 18:44 B17 GEGENSWEEP-PRUEFUNG 2 (Doppelarbeit): RUNDE-10/nls-leiter/ERGEBNIS.md [V] hat das Petrov-Troepfchen schon:
  Wandzustand des geschlossenen Kanals bei E_0 ~ +0,1 statt < mu ~ -0,45, also keine Feshbach-Leiter; "Troepfchen ...
  nicht der richtige Pruefstand". ~~Troepfchen als Testkandidat~~ gestrichen. RUNDE-10 nennt als Laborkandidaten mit
  zwei Zweigen: Gap-Solitonen (Bragg, Wellenleiter, optische Gitter), Rabi-gekoppelte Kondensate, Antiferromagnete [H].
- 18:45 B18 arXiv-API nichtlineares Dirac x embedded/BIC: 11 Treffer. Erwartung: nichts. Befund [S]: Boussaid/Comech
  1211.3336: "no embedded eigenvalues in the part of the essential spectrum beyond the embedded thresholds"; im
  nichtrelativistischen Limes haeufen sich Punkteigenwerte "only ... to 0 and +-2mi". Boussaid/Cacciapuoti/Carlone/
  Comech 2006.03345: Instabilitaet "due to the bifurcations ... from the embedded eigenvalues +-2 omega i".
  -> **verletzt E13**, aber Projekt-grep: MESS-2 (RUNDE-11) hat Soler +-2 omega i schon [A] (eingebettet fuer
  |omega| > m/3, SU(1,1)-geschuetzt, "eingebettet auf ganzen Intervallen"). Neu fuer das Projekt nur 1211.3336 (lag als
  API-Datei vor, nicht ausgewertet). [A] aus Projektdatei 2006.03345.txt, ~~S. 14~~ S. 15 (Berichtigung 18:54, Seitenumbruch gezaehlt): fuer |lambda| >= m + |omega|
  ("beyond the embedded thresholds") sind beide Kanaele offen, "there is no corresponding square-integrable function"
  (Punktwechselwirkungsmodell).
- 18:48 B19 arXiv-API [S]: Xie/Saffin/Zhou 2101.06988: CSQ-Verlauf in 4 Stufen (Relaxation, CSQ-Plateau, schneller
  Zerfall, Oszillon-Plateau), Lebensdauern gegen Anfangs- und Potentialparameter kartiert. Hou/Saffin/Xie 2202.08392:
  CSQ im logarithmischen SUSY-Potential "extremely stable", Lebensdauer >= 4,6e5/m (3+1D), 2,5e7/m (2+1D).
  [H, aus B7/B15]: Wenn dieses Log-Potential bei kleinem Feld K < 0 hat, divergiert dort die effektive Masse wie beim
  exakten I-Ball; dann waere die Langlebigkeit teils "kein Kontinuum" statt Ausloeschung. Nicht geprueft.
- 18:49 B20 GEGENSWEEP-PRUEFUNG 3 [A] Kleihaus/Kunz/List gr-qc/0505143 (quellen/): U = lambda phi^6 - a phi^4 + b phi^2,
  Bild 1 mit lambda = 1, a = 2, b = 1,1 bzw. 1. Invariante a^2/(lambda b): KKL 3,64 bzw. 4 (entartet); unser
  U = S - S^2 + S^3/2 hat 2 [ES, Kopfrechnung]. Gleiche Familie, anderer Punkt: Ein Bosonenstern mit **unserem** Punkt
  ist nicht vorgerechnet. Annahme "Bosonenstern = unser Modell + Gravitation" gilt nur familienweise.
  mit T3.
- 2026-10-01 18:54:32 CEST ENDE: Bericht oben fertig (Rueckwaertslesung: Seitenzahl 2006.03345 von 14 auf 15 berichtigt, PDF-Versionen
  nach Stempel umbenannt: 1908.11103v1, 2012.13409v2, gr-qc-0505143v1). Keine Rechnung, kein python/awk, kein ssh/git.
