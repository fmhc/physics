# Runde 9, Literaturkarte ROT-3: Drehung im Feld (Wirbel mit gefuelltem Kern, innerer Rotor, Bruchwirbel mit Waenden)

Papier-Agent (Anthropic, Opus 5.5), Auftrag von claude-primary (RUNDE-09.md, Nachtrag 07:42:41). Nur Papier: keine lokale
Rechnung, keine Interpreter; Rechnungen von Hand, Formeln im Text. Explorativ (v3), keine formale Bestaetigung. Keine
Aenderung an fremden Dateien, kein git, keine Journaleintraege.

- Beginn: 2026-09-30 07:41:58 CEST (date)
- Ende: 2026-09-30 08:11:53 CEST (date, nach dem letzten inhaltlichen Schreiben gemessen). Das Websuch-Budget der Sitzung
  war danach erschoepft (Block 16).

Lesetiefe: **[A]** an der Quelle gelesen, **[A-W]** ueber das Abrufwerkzeug gelesen (Zusammenfassung eines Hilfsmodells),
**[S]** nur Suchtreffer, **[L?]** Gedaechtnis, ungeprueft, **[P]** Projektdatei, **[ES]** eigener Schluss bzw.
Schreibtischrechnung, **[H]** Hypothese.

Status: ARBEITSDATEI (Feldregel 5). Der Bericht kommt oben hinzu, das Arbeitsfeld bleibt unten. Gestrichenes bleibt
~~gestrichen~~. Offene Rueckfragen stehen in Abschnitt ~~W5~~ W8 und wandern mit.

Bericht geschrieben ab 2026-09-30 08:07:08 CEST (date).

---

## Kurzfazit (fuer die Leitung, fuenf Punkte)

1. **(a) Wirbel mit gefuelltem Kern: bekannt** in BEC, NLS, Supraleitern und Bosonensternen (Halbwirbel, Skyrmion als
   Meronpaar, Vorton, l = 0 + l = 1-Stern); **teilweise** fuer Q-Baelle; **neu** (nach Recherchestand) mit unserem
   phasenempfindlichen Term. Der Term erzwingt eine m = 2-Verformung. Die stetige Fortsetzung von g = 0 ist ein
   **mitdrehendes** Muster mit Omega = omega_1 - omega_2, weil der Kern bei g = 0 eine kleinere Frequenz braucht [ES, G1];
   ob es bei groesserem g auch einen ruhenden Zweig gibt, ist offen (O1).
2. **(b) innerer Rotor: teilweise.** Laufende Phase, Oszillonen aus angeregten phi^6-Q-Baellen und "charge-swapping"
   sind bekannt. Einen stationaeren reinen Rotor gibt es nicht [ES]. In erster Ordnung in g strahlt er nicht, solange
   Omega_r < (2/3)(1 - omega); der mitdrehende Wirbel strahlt in erster Ordnung erst, wenn 2 omega_1 - omega_2 > 1 [ES].
3. **(c) Bruchwirbel mit Waenden: bekannt** fuer Rabi-Kopplung, samt ausdruecklichem QCD-Vergleich (Son und Stephanov
   [A]), und im Experiment fuer Mehrband-Supraleiter und Spin-1-BEC; **teilweise** fuer die zweite Ordnung. Bei uns sind
   es **Ising-artige pi-Waende**, je zwei an jedem (1,0)-Wirbel. Eine reine Phasenwand nach Son und Stephanov ist bei uns
   ein Sattel, kein Minimum [ES, V1-Nachtrag].
4. (a), (b) und (c) sind vermutlich **eine Familie** mit stetigem J/Q zwischen 0 und 1 [H]: Moderator R/delta fuer
   Textur gegen Waende, Omega gegen die Massenschwelle fuer die Abstrahlung.
5. **Test:** T1 im 2D-Querschnitt misst Musterdrehzahl, Wandkontrast P2 und n_z/S an den Stufen; T2 radial misst die
   Rotorschwelle. Jeder Lauf dauert Minuten, zusammen unter 1 h Spurzeit [ES, nicht gemessen] (W6).

## Erwartungsverstoesse (das Wichtigste zuerst; voller Zyklus in W3)

1. **V1: Die Son-Stephanov-Wand ist in unserem Modell keine stabile Wand.** Erwartet: ihre 2 pi-Phasenwand als Vorlage
   fuer (c). Gelesen [A]: Die Wand ist nur metastabil, solange sie breiter ist als die Spin-Heilungslaenge
   xi_A ~ (g/delta g)^{1/2} xi_B (Gl. 2.21, 3.5, 3.6).
   - Unser U(S) ist U(2)-symmetrisch, also ist delta g = 0 bei g = 0. ~~Das Regime ist leer.~~
   - Berichtigt beim Gegenlesen (eingetragen bis 08:09:30 laut date, siehe V1-Nachtrag):
     - Bei g != 0 liefert g J Phasen- **und** Konzentrationssteifigkeit von gleicher Ordnung. Kein Parameter macht die
       Wand breiter als xi_A.
     - Die reine Phasenwand ist ein Sattel: Dreht man ihren Kreis auf der Pseudospin-Kugel um die x-Achse zum Pol, sinkt
       die Anisotropie-Energie bei gleichen Gradientenkosten [ES].
   - Stattdessen: Die Kopplung ist eine zweiachsige Pseudospin-Anisotropie. In der Basis psi_+- = (psi_1 +- psi_2)/sqrt 2
     wird sie zu einer **Entmischung** plus Rest zweiter Ordnung. Unsere Waende sind Ising-artige pi-Waende, und in der
     Wandmitte ist eine Komponente null.
2. **V5: Oszillierende Selbsterhaltung ist frisch belegt, fuer ein Feld.** Erwartet: Zerfall drehender Sterne. Gefunden
   (Zhou u. a., arXiv 2609.06954, Sept. 2026 [A-W]): quasiperiodisches Pendeln zwischen Ring- und Zwillingssternform,
   beschrieben durch einen Drei-Moden-Hamiltonian; abstossende Selbstwechselwirkung verlaengert die Lebensdauer.
   - Fuer uns [H]: ein Pendeln zwischen Textur (a) und Zwei-Wand-Form (c), messbar als P2(t).
3. **V2: Bruchwirbel mit Skyrmion-Textur sind gemessen, aber im Supraleiter.** Erwartet: Spinor-BEC. Gefunden:
   Rastertunnelmikroskopie an KFe2As2 (Science 393, 80-84, 2026 [S]): Ganzzahlige Wirbel spalten in Bruchwirbel, die
   sich zu Ketten mit CP^2-Skyrmion-Invariante ordnen. (a) und (c) treten dort zusammen auf.
4. **V3: Stabile 3D-Skyrmionen brauchen Entmischung** (Battye, Cooper, Sutcliffe 2002 [S]). Genau diese erzeugt unser
   g > 0 in der +- Basis (V1). Das ist ein Hinweis fuer Frage 4, kein Beleg.
5. **V6: Z_2-Waende ohne Rabi-Term, mit zwei Wandtypen und eingeschlossenen Halbwirbel-Molekuelen** (Gavrilov 2025
   [A-W]). Das passt zu unseren zwei entarteten pi-Wandtypen (n_z = +-S in der Mitte) [ES].
6. **V4: m = 1 ist im nichtrelativistischen Grenzfall unabhaengig von der Selbstwechselwirkung instabil** (Siemonsen und
   East 2021 [S]). Unser dickwandiger Bereich (omega -> 1) ist dieser Grenzfall. Ein Stabilitaetsfenster, falls es eines
   gibt, liegt eher im Duennwandbereich.
7. Klein:
   - E28: Battye und Cotterill 2021 rechnen im geeichten, nicht im globalen Modell.
   - E29: Die Arbeit zur zweiten Ordnung von 2026 behandelt im Abstract keine Waende.
   - E56: Beim Halbwirbel von Zezyulin ist die Kernkomponente schwaecher gebunden; sein Modell ist nicht U(2).
   - E58: arXiv 2511.16210 behandelt drehende 2D-Q-Baelle, keine Q-lumps.
   - E60: Die Polarisationsarbeit von 2025 ist im Abstract nur Oszillon-Genese.
8. Verfahren: Zwei Zeitangaben habe ich zuerst geschaetzt statt gemessen (Block 1 "07:52", W1 "07:48 bis 07:55"). Beide
   sind gestrichen und durch date-Werte ersetzt.

## Literaturstand mit Quellen (Lesetiefe in Klammern; Details im Arbeitsfeld)

**Frage 1, gefuellter Kern, Stabilitaet:**
- Einkomponentige drehende Q-Baelle:
  - Volkov und Woehnert 2002 [A] konstruieren sie in 3+1 und 2+1, mit J = N Q und einer Potentialklasse wie unserer
    (kubisch plus quintisch in der Feldgleichung). **Keine Stabilitaetsaussage.** Sie betonen, dass ein J != 0-Anfangszustand
    sonst "most probably immediately radiated away" wird.
  - Kleihaus, Kunz, List 2005 [A, S. 1 bis 3, 17]: Existenzbereich und J = n Q. Stabil heisst dort nur "lower branch,
    when their mass is smaller than the mass of Q free bosons", und das fuer kugelsymmetrische Baelle; drehende Baelle
    werden nicht dynamisch geprueft. Ihr Potential entspricht beta = 0,275 in unserer beta-Familie, unseres hat beta = 0,5
    [ES]; bei beta = 0,5 sind drehende Q-Baelle in den gelesenen Arbeiten nicht gerechnet.
  - Dynamische Stabilitaet flacher drehender Q-Baelle: nach Recherchestand nicht belegt.
  - Hinweise nur indirekt:
    - m = 1-Bosonensterne sind nichtachsensymmetrisch instabil, Selbstwechselwirkung loescht das nur in Teilbereichen
      (Siemonsen und East 2021 [S]).
    - Ring und Zwillingsstern pendeln (Zhou u. a. 2026 [A-W]).
    - Kubisch-quintisches bimodales NLS mit Vierwellenmischung, 3D-Lichtkugeln: s = 1 ist stabil oberhalb einer
      Energieschwelle, etwa 25 % des Existenzbereichs (Mihalache u. a. 2003 [A-W]).
- Gefuellter Kern bzw. zwei Komponenten:
  - Sanchis-Gual u. a. 2021 [S]: Ein l = 0-Stern eines zweiten Felds "with a different frequency" stabilisiert den
    drehenden Stern.
  - Zezyulin 2026 [A-W]: Halbwirbel (Windung nur in einer Komponente) sind im kubisch-quintischen NLS in der
    Doppel-Flachspitzen-Form stabil, sonst spaltet der Kern ("solitary wave billiard").
  - Kasamatsu, Tsubota, Ueda 2004 [S]: Das Wirbelmolekuel ist eine nichtachsensymmetrische Pseudospin-Textur, "a pair of
    merons".
  - Metlitski und Zhitnitsky 2004 [S]: Vortonen im BEC sind durch Kondensation im Kern auch in Ruhe stabil.
  - Lemperiere und Shellard 2003 [S]: globale Vortonen meist instabil, dicke kleine bleiben.
- In Q-Baellen mit phasenempfindlicher Kopplung: nichts gefunden (24-Monats-Suche eingeschlossen).

**Frage 2, Bruchwirbel und Waende:**
- Son und Stephanov 2002 [A, S. 2, 7 bis 12]:
  - 2 pi-Wand, "not topologically stable", Zerfall ueber Loecher.
  - Wirbel als Wandrand; "vortex confinement", "very similar to that of quark confinement".
  - Umeinander kreisende Wirbelpaare als "high-spin meson states".
- Tanaka 2002 und Babaev 2002 [S]: Phasensoliton bzw. Bruchfluss-Wirbel in Zweiband-Supraleitern.
- Tylutki u. a. 2016 [S]: Seilreissen als QCD-Analogon. arXiv 1906.06237 [S]: Zerfall der Wand in eingeschlossene
  Wirbelpaare.
- Zweite Ordnung und Z_2:
  - Garaud und Babaev 2014 [S]: s+is-Waende, Bruchwirbel als Knoten zwischen Waenden.
  - Peng, Zhang, Hu 2026 [A-W]: Grundzustaende bei zweiter Ordnung.
  - Kang, Seo, Takeuchi, Shin 2019 [S]: Waende mit Halbquantenwirbeln im Spin-1-BEC, gemessen.
  - Yu und Blakie 2021 [A-W]: Wand mit Dunkelsoliton-Profil der Magnetisierung, stabil gegen die Schlangeninstabilitaet.
  - Gavrilov 2025 [A-W]: Z_2-Domaenen, zwei Wandtypen.
  - Gilles u. a. 2017 [S]: Polarisations-Domaenenwaende in Fasern, gemessen.
  - Science 2026 [S]: Bruchwirbel mit CP^2-Skyrmion in KFe2As2.
- Was sich bei cos(2 Delta theta) aendert: W5.1 [ES].

**Frage 3, innerer Rotor:**
- Laufende Phase und Selbsteinfang im Josephson-Kontext [S, Sammeltreffer; Smerzi u. a. 1997 nur L?].
- Charge-swapping Q-balls (Copeland, Saffin, Zhou 2014 [S]).
- Oszillonen aus angeregten Q-Baellen im komplexen phi^6 (Blaschke u. a. 2025 [A-W]).
- Abstrahlung eines Relativphasen-Rotors in einem relativistischen Q-Ball: nach Recherchestand nicht behandelt. Schwellen
  [ES] in W5.2.

**Frage 4, Q-Hopfionen:**
- Q-lumps (Leese 1991 [S]; Sutcliffe 2023 [A-W]): 2+1, CP^1 mit Potential, drehend, Bogomolny.
- Isospinnende Hopfionen nur mit Skyrme-Term (Harland u. a. 2013 [S]).
- "Q-Hopfion" ohne Skyrme-Term: nach Recherchestand nicht belegt.
- [ES]: Bei g != 0 fehlt die erhaltene Isoladung, die der Q-lump-Mechanismus braucht. Im Q-Ball gibt es ohnehin keine
  strenge Hopf-Ladung (S -> 0 aussen); das passt zur Entscheidung vom 23.09.

## Regime und Moderatoren

| Streitpunkt | Moderator | Regime 1 | Regime 2 |
|---|---|---|---|
| (a) Textur gegen (c) Waende | R/delta, delta ~ 1/sqrt(\|g\| J S_0) [ES, ohne Vorfaktor] | R/delta <~ 1: fast runde Textur, m = 2-Anteil ~ g | R/delta >= 3: zwei pi-Stufen |
| Phasenwand gegen Ising-Wand | Konzentrationssteifigkeit delta g gegen Phasensteifigkeit (V1) | delta g > 0 unabhaengig, Wand breiter als xi_A: Sine-Gordon (Son-Stephanov) | unser Modell: beide Steifigkeiten aus g J, fest gekoppelt; Phasenwand ist Sattel, Minimum Ising ueber den Pol [ES] |
| Stabilitaet drehender Baelle | dick- gegen duennwandig (nichtrelativistische Naehe, V4) | omega -> 1: m = 1 eher instabil | duennwandig: Fenster moeglich (NLS-Analoga) |
| 3D-Texturen stabil? | Mischbarkeit in der passenden Basis (V3) | mischbar: bei BCS 2002 nicht als stabil gemeldet [L?, Abstract nennt nur das Entmischungsregime] | entmischend: stabile Skyrmionen (BCS 2002 [S]) |
| Rotor ruhig? | Omega_r gegen (2/3)(1 - omega) | darunter: Verlust nur in hoeherer Ordnung | darueber: Abstrahlung erster Ordnung |
| Mitdrehender Wirbel strahlt? | 2 omega_1 - omega_2 gegen 1 | < 1: gebunden | > 1: m = 2-Welle in psi_2 |

## Unterscheidungspunkte (Feldregel 2)

- (a) gegen (c): P2 = O(g) linear gegen P2 > 0,5 mit Plateaus. Trennbar erst bei R/delta >= 3, also am duennwandigen
  Ball mit g ~ 0,5. Bei R/delta <~ 1 empirisch nicht unterscheidbar.
- Ising gegen Phasenwand: n_z/S in der Stufenmitte, +-1 gegen 0. Scharf, in T1 direkt ablesbar.
- (a/c) gegen (b): J/Q ist exakt erhalten. (b) hat J = 0, der gefuellte Wirbel 0 < J/Q < 1. Immer trennbar.
- Mitdrehen (G1) gegen ruhendes Muster: Omega_pat = omega_1 - omega_2 gegen 0; am schaerfsten bei kleinem g.
- Rotor gegen Pendel: Energie ueber der Separatrix; die Verlustrate springt bei Omega_r = (2/3)(1 - omega) (T2).

## Gegensweep-Befunde (W4)

- G1 (geprueft): Der gefuellte Wirbel ist bei g = 0 **zwei-frequent** (omega_2 < omega_1, Variationsargument, gestuetzt
  durch zwei Quellen). Bei g != 0 folgt daraus das Mitdrehen. Das ist der wichtigste Befund der Karte.
- G2 (geprueft): J/Q ist fuer den gefuellten Wirbel nicht quantisiert. Der Vergleich "stabiler als der einkomponentige
  Wirbel" vergleicht verschiedene Sektoren.
- G3 (geprueft): Beide Wandwege kosten gleich viel Gradientenenergie, W1.1 haelt.
- G4 bis G6 nicht geprueft: Uebertragbarkeit aus nichtrelativistischen Systemen; Wand im inhomogenen Ball; die
  Abschnitte 5 und 6 von KANDIDAT nicht gelesen.

## Offene Fragen

O1 bis O8 in W8. Die wichtigsten:
- O1: Gibt es einen ruhenden Zweig?
- O2: Wandspannung mit Vorfaktor.
- O4: Pendeln (a) <-> (c)?
- O8: Ist der einkomponentige drehende Ball unseres U(S) im Duennwandbereich stabil?

## Quellenliste (URL wie abgerufen; Lesetiefe)

- Son, D. T.; Stephanov, M. A. (2002): Domain walls of relative phase in two-component Bose-Einstein condensates. PRA 65,
  063621. https://arxiv.org/abs/cond-mat/0103451 [A]
- Volkov, M. S.; Woehnert, E. (2002): Spinning Q-balls. PRD 66, 085003. https://arxiv.org/abs/hep-th/0205157 [A]
- Kleihaus, B.; Kunz, J.; List, M. (2005): Rotating boson stars and Q-balls. PRD 72, 064002.
  https://arxiv.org/abs/gr-qc/0505143 [A, S. 1 bis 3, 17]
- Shnir, Ya. (2011): Q-vortices, Q-walls and coupled Q-balls. J. Phys. A 44, 425202. https://arxiv.org/abs/1101.5366
  [A, S. 1 bis 2]
- Sanchis-Gual, N.; Di Giovanni, F.; Herdeiro, C.; Radu, E.; Font, J. A. (2021): Multifield, multifrequency bosonic stars
  and a stabilization mechanism. PRL 126, 241105. https://arxiv.org/abs/2103.12136 [S]
- Siemonsen, N.; East, W. E. (2021): Stability of rotating scalar boson stars with nonlinear interactions. PRD 103,
  044022. https://arxiv.org/abs/2011.08247 [S]
- Zhou, K.-D.; Bao, S.-S.; Deng, J.; Zhang, H. (2026): The Dynamical Instability of Rotating Boson Stars. arXiv
  2609.06954. https://arxiv.org/abs/2609.06954 [A-W]
- Almumin, Y.; Heeck, J.; Rajaraman, A.; Verhaaren, C. B. (2024): Slowly rotating Q-balls. EPJC 84, 364.
  https://arxiv.org/abs/2302.11589 [S]
- DeVries, B.; Vassallo, F.; Verhaaren, C. B. (2026): Understanding the quantized angular momentum of rotating Q-balls.
  JHEP 08(2026)108. https://arxiv.org/abs/2602.15196 [A-W]
- Chen, Q.; Andersson, L.; Li, L. (2025): Stability analysis for Q-balls with spectral method. JHEP 02(2026)078.
  https://arxiv.org/abs/2509.18656 [A-W]
- Galushkina, Y.; Kim, E.; Nugaev, E.; Shnir, Ya. (2025): Generalized models for spinning field lumps on plane. JHEP
  04(2026)136. https://arxiv.org/abs/2511.16210 [A-W]
- Mihalache, D.; Mazilu, D.; Towers, I.; Malomed, B. A.; Lederer, F. (2003): Stable spatiotemporal spinning solitons in a
  bimodal cubic-quintic medium. PRE 67, 056608. https://journals.aps.org/pre/abstract/10.1103/PhysRevE.67.056608 [A-W];
  2D-Fassung J. Opt. A 4, 615 (2002) nur als Titel [S].
- Zezyulin, D. A. (2026): Double-flat-top half-vortices and self-bound solitary wave billiards. PRA 113, 013501.
  https://arxiv.org/abs/2512.05763 [A-W]
- Kasamatsu, K.; Tsubota, M.; Ueda, M. (2004): Vortex molecules in coherently coupled two-component Bose-Einstein
  condensates. PRL 93, 250406. https://link.aps.org/doi/10.1103/PhysRevLett.93.250406 [S]
- Tylutki, M.; Pitaevskii, L. P.; Recati, A.; Stringari, S. (2016): Confinement and precession of vortex pairs in
  coherently coupled Bose-Einstein condensates. PRA 93, 043623. https://arxiv.org/abs/1601.03695 [S]
- (Autoren nicht gesehen) (2019): Decay of the relative phase domain wall into confined vortex pairs: the case of a
  coherently coupled bosonic mixture. https://arxiv.org/abs/1906.06237 [S]
- Tanaka, Y. (2002): Soliton in two-band superconductor. PRL 88, 017002.
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.88.017002 [S]
- Babaev, E. (2002): Vortices with fractional flux in two-gap superconductors and in extended Faddeev model. PRL 89,
  067001. Nur Suchtreffer-Zitat, keine eigene URL abgerufen [S]
- Garaud, J.; Babaev, E. (2014): Domain walls and their experimental signatures in s+is superconductors. PRL 112,
  017003. https://www.idpoisson.fr/garaud/research/3CGL-BTRS-detection.html [S]
- Peng, S.-Y.; Zhang, L.-F.; Hu, X. (2026): Three-component superconductivity: the effect of second-order Josephson
  couplings (Titel laut Treffer gekuerzt). https://arxiv.org/abs/2605.28221 [A-W]
- (Autoren nicht gesehen) (2026): Observation of quantum vortex core fractionalization and skyrmion formation in a
  superconductor. Science 393, 80-84. https://www.science.org/doi/10.1126/science.ads0189 [S; Seite 403, Inhalt aus
  PubMed- und SJTU-Treffern]
- (Autoren nicht gesehen) (2023): Superconducting vortices carrying a temperature-dependent fraction of the flux quantum.
  Science. https://www.science.org/doi/10.1126/science.abp9979 [S]
- Kang, S.; Seo, S. W.; Takeuchi, H.; Shin, Y. (2019): Observation of wall-vortex composite defects in a spinor
  Bose-Einstein condensate. PRL 122, 095301. https://arxiv.org/abs/1812.08955 [S]
- Yu, X.; Blakie, P. B. (2021): Dark-soliton-like magnetic domain walls in a two-dimensional ferromagnetic superfluid. PRR
  3, 023043. https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.3.023043 [A-W]
- Gavrilov, S. S. (2025, rev. 2026): Phase domain walls in coherently driven Bose-Einstein condensates.
  https://arxiv.org/abs/2505.09553 [A-W]
- Gilles, M.; Bony, P.-Y.; Garnier, J.; Picozzi, A.; Guasoni, M.; Fatome, J. (2017): Polarization domain walls in
  optical fibres as topological bits for data transmission. Nature Photonics 11, 102.
  https://www.nature.com/articles/nphoton.2016.262 [S]
- Battye, R. A.; Cooper, N. R.; Sutcliffe, P. M. (2002): Stable Skyrmions in two-component Bose-Einstein condensates. PRL
  88, 080401. https://arxiv.org/abs/cond-mat/0109448 [S]
- Metlitski, M. A.; Zhitnitsky, A. R. (2004): Vortex rings in two component Bose-Einstein condensates. JHEP 06 (2004)
  017. https://arxiv.org/abs/cond-mat/0307559 [S]
- Lemperiere, Y.; Shellard, E. P. S. (2003): Vorton existence and stability. PRL 91, 141601.
  https://arxiv.org/abs/hep-ph/0305156 [S]
- Battye, R. A.; Cotterill, S. J. (2021): Stable cosmic vortons in bosonic field theory. PRL 127, 241601.
  https://arxiv.org/abs/2111.07822 [A-W]
- Leese, R. A. (1991): Q-lumps and their interactions. Nucl. Phys. B 366, 283.
  https://www.osti.gov/etdeweb/biblio/7302395 [S]
- Sutcliffe, P. (2023): Q-lump scattering. https://arxiv.org/abs/2304.05521 [A-W]
- Harland, D.; Jaeykkae, J.; Shnir, Ya.; Speight, M. (2013): Isospinning hopfions. https://arxiv.org/abs/1301.2923 [S]
- Copeland, E. J.; Saffin, P. M.; Zhou, S.-Y. (2014): Charge-swapping Q-balls. https://arxiv.org/abs/1409.3232 [S]
- Blaschke, F.; Romanczukiewicz, T.; Slawinska, K.; Wereszczynski, A. (2025): Q-ball polarization - a smooth path to
  oscillons. PLB (2025). https://arxiv.org/abs/2502.20519 [A-W]
- Weitere nur als Treffer gesehen [S]: arXiv 2402.03193 (Spinning Q-ball Superradiance in 3+1D), arXiv 2312.01139
  (Quantum corrected Q-ball dynamics: nichtdrehende 2+1-Baelle stabil), arXiv 2405.06591 (Perturbations of Q-balls),
  arXiv 2602.05001 und 2605.04441 (Rabi-gekoppelte Solitonen 2026), arXiv 1012.2989 (Rabi-Josephson), arXiv 2608.26782
  (Phasensolitonen 2026), JHEP 06(2026)126, arXiv 2504.13509, JHEP 12(2025)154.
- Projektdateien [P]: coordination/gesamtformel-20260921/KANDIDAT.md (0, 2.2, 3.2);
  coordination/runden-v3/RUNDE-08/gf-bic/ERGEBNIS.md; coordination/runden-v3/RUNDE-09.md (Nachtrag 07:42:41).

---

# ARBEITSFELD

## W0. Modell, wie ich es lese [P]

- KANDIDAT.md 0, 2.2, 3.2 [P]: L = sum_a (|d_t psi_a|^2 - |grad psi_a|^2) - U(S) + g J Re[(psi_1^* psi_2)^2], flaches
  R^3 x R, Masse 1 (U'(0) = 1). Bewegungsgleichung d_t^2 psi_1 - lap psi_1 + U'(S) psi_1 - g J psi_1^* psi_2^2 = 0.
- Restgruppe bei g != 0: U(1)_global x Z_2 (psi_2 -> -psi_2), Tausch 1 <-> 2, Konjugation C. **Keine** getrennten
  Kanalphasen, also sind Q_1 und Q_2 einzeln nicht erhalten, nur Q = Q_1 + Q_2 [P, KANDIDAT 3.2, 4.3].
- GF-BIC (RUNDE-08/gf-bic/ERGEBNIS.md) [P]: gemischter Ball psi_1 = psi_2 (g > 0) bzw. psi_2 = +-i psi_1 (g < 0);
  symmetrischer Sektor exakt N = 1 mit beta_eff; antisymmetrischer Sektor linear stabil; Pseudo-Goldstone-Mode der
  Komponentendrehung nu_0 = 0,069 / 0,131 / 0,218 (M1 / M2 / M3).
- RUNDE-09.md [P]: ROT-1 (2D-Querschnitt, weil der Kopplungsterm bei Windung nur in psi_1 wie cos(2 phi) variiert) und
  ROT-2 (innerer Rotor) laufen seit 07:45:42 parallel.

## W1. Schreibtischvorarbeit vor jedem Abruf (geschrieben zwischen 07:47:55 und 07:48:44 laut den date-Zeilen davor und danach; die zuerst eingetragene Spanne ~~07:48 bis 07:55~~ war geschaetzt) [ES]

### W1.1 Pseudospin-Form des Kopplungsterms [ES]

- Mit psi_a = f_a e^{i theta_a}, Delta theta = theta_2 - theta_1 und dem Pseudospin
  n_x + i n_y = 2 psi_1^* psi_2, n_z = |psi_1|^2 - |psi_2|^2 gilt |n| = S und

      Re[(psi_1^* psi_2)^2] = f_1^2 f_2^2 cos(2 Delta theta) = (n_x^2 - n_y^2)/4 .

- Die Potentialdichte ist also V = U(S) - (g J/4)(n_x^2 - n_y^2): eine **zweiachsige Anisotropie** des Pseudospins,
  keine Zeeman-artige (lineare) Kopplung wie bei Rabi/Josephson (die waere Omega n_x).
  - g > 0: leichte Achse x (psi_1 = +-psi_2), schwere Achse y (Delta theta = +-pi/2), mittlere Achse z (reine Komponente).
  - g < 0: leichte und schwere Achse tauschen.
- Mit n = S (sin a cos b, sin a sin b, cos a): Delta V = (g J S^2/4)(1 - sin^2 a cos 2b) gegenueber dem Minimum.
  - Barriere ueber den Pol (reine Komponente, eine Komponente wird null): g J S^2/4.
  - Barriere ueber den Aequator (Drehung der relativen Phase um pi/2): g J S^2/2, **doppelt so hoch**.
  - Die Gradientenkosten beider Wege sind auf der Pseudospin-Kugel gleich (je ein Halbkreis).
- **Folge [ES]:** Eine Wand zwischen psi_1 = psi_2 und psi_1 = -psi_2 (n_x = +S -> -S) laeuft bei freien Amplituden
  bevorzugt ueber den Pol, also als **Ising-artige Wand** (eine Komponente geht durch null und wechselt das Vorzeichen),
  nicht als Sine-Gordon-Knick der relativen Phase. Die Phase springt dort um pi, wo die Amplitude verschwindet.
  - Zu pruefen: Welche Literatur kennt diesen Wandtyp bei Kopplung zweiter Ordnung (Pruefpunkt fuer Frage 2).

### W1.2 Topologie der Waende [ES]

- Vakuum des gemischten Zustands bei g > 0: {sqrt(S/2) e^{i chi} (1, +-1)}, zwei **getrennte** Kreise (psi_2 -> -psi_2
  ist gebrochen). Also pi_0 = Z_2: die pi-Wand ist **topologisch stabil**, solange beide Komponenten da sind.
  - Bei Rabi-Kopplung cos(Delta theta) ist das Vakuum ein Kreis; die 2 pi-Wand ist nur metastabil (Erwartung zu Son und
    Stephanov, siehe W2).
- Weil psi_1 und psi_2 einzeln eindeutig sind, windet Delta theta um jeden Punkt um 2 pi (n_2 - n_1). Eine einzelne
  pi-Wand kann also **nicht** an einem Wirbel enden; ein (1,0)-Wirbel traegt genau zwei pi-Waende (oder eine gerade Zahl).
  Enden koennen die Waende nur dort, wo der gemischte Zustand verschwindet, also am Rand des Q-Balls.
- Halbierte Wirbel (Windung pi in einer Komponente) gibt es im Modell nicht, weil nichts psi_2 -> -psi_2 mit einer
  Raumdrehung verklebt (anders als bei Spinor-Kondensaten mit Halbquantenwirbeln). "Halb" ist hier die **Wand**, nicht
  der Wirbel.

### W1.3 Achsensymmetrie [ES]

- Mit psi_1 = f(r) e^{i m_1 phi}, psi_2 = h(r) e^{i m_2 phi} ist (psi_1^* psi_2)^2 proportional zu e^{2 i (m_2 - m_1) phi}.
- Achsensymmetrisch (stationaer, exakt) geht es bei g != 0 also nur mit m_1 = m_2: dann ist nichts gefuellt (beide
  Komponenten haben dieselbe Nullstelle), und der symmetrische Fall ist der einkomponentige drehende Q-Ball mit beta_eff.
- Gefuellter Kern (m_1 = 1, m_2 = 0) erzwingt eine **m = 2-Modulation** (cos 2 phi). Das deckt sich mit RUNDE-09.md
  (ROT-1 laeuft deshalb im 2D-Querschnitt) [P]. Hypothese (a) als achsensymmetrisches Objekt gibt es exakt nur bei g = 0.

### W1.4 Kein stationaerer innerer Rotor mit zwei Frequenzen [ES]

- Stationaer heisst psi_a(t) = e^{-i omega t} F_a(x) bis auf eine Symmetrie. Bei g != 0 ist die einzige kontinuierliche
  innere Symmetrie die globale Phase. Getrennte Frequenzen omega_1 != omega_2 machen den Kopplungsterm zeitabhaengig
  (Faktor e^{2 i (omega_1 - omega_2) t}); das ist keine Loesung der Form stationaer.
- **Ausnahme [ES]:** Raumdrehung ist eine Symmetrie. Ein starr rotierendes Muster
  psi_a(t, r, phi) = e^{-i omega t} F_a(r, phi - Omega t) ist zulaessig. Fuer F_1 ~ e^{i phi}, F_2 ~ e^0 heisst das
  omega_1 = omega + Omega, omega_2 = omega: die relative Phase dreht dann **in der Zeit** und **im Raum** zugleich.
  - [H] Damit sind (a), (b), (c) womoeglich keine drei Objekte, sondern drei Lagen einer Groesse, der Musterdrehzahl Omega
    gegen die Verankerung durch g J S: Omega = 0 und starke Kopplung -> ruhende Waende (c); Omega gross oder g klein ->
    fast achsensymmetrische Textur (a), die mitdreht; (b) ist der Grenzfall ohne Raumwindung.
  - Stoerpunkt dieser Lesart: Ein starr drehendes m = 2-Muster erzeugt im Laborsystem Frequenzen omega + 2 k Omega. Es
    strahlt, sobald omega + 2 k Omega > 1 fuer einen Anteil mit merklicher Fourier-Amplitude. Scharfe Waende (Breite delta)
    haben Harmonische bis k ~ R/delta. [ES, Groessenordnung, nicht gerechnet]

### W1.5 Zwei-Regime-Vorannahme [H]

- Moderator fuer (a) gegen (c): Wandbreite delta ~ 1/sqrt(|g| J S_0) gegen Ballradius R.
  - R << delta: Textur bleibt fast rund (a), die m = 2-Modulation ist eine kleine Stoerung ~ g.
  - R >> delta: die Windung der relativen Phase sammelt sich in zwei pi-Waenden (c).
  - Duennwand-Baelle (omega^2 -> 1/2, S_0 -> 1, R gross; R_halb ~ 12 bei 0,551 laut GF-BIC R9.1) liegen eher im
    Wandregime, kleine Baelle nahe omega^2 ~ 0,8 eher im Texturregime. Zahlen: delta ~ 1/sqrt(0,2) ~ 2,2 bei g = 0,2 [ES,
    ohne Vorfaktor].
- Moderator fuer (b): Drehzahl Omega der relativen Phase gegen die Pendelfrequenz nu_0 (Pseudo-Goldstone, GF-BIC 2.4) und
  gegen den Abstand 1 - omega zur Massenschwelle.

## W2. Erwartungsprotokoll (Feldregel 3)

Format: Nr., Zeit (date) der Erwartung, Erwartung in einem Satz, Ausgang (bestaetigt -> eine Zeile; verletzt -> W3).

### Block 1 (Erwartungen notiert 07:48:44)

- E1 Volkov und Woehnert 2002 "Spinning Q-balls": konstruieren drehende Q-Baelle in 3+1 mit J = n Q (quantisiert), sagen
  zur Stabilitaet nichts Belastbares (hoechstens Vermutung).
- E2 Kleihaus, Kunz, List 2005 "Rotating boson stars and Q-balls": achsensymmetrische drehende Q-Baelle gerader und
  ungerader Paritaet, J = n Q; Stabilitaet nur ueber E < m Q bzw. Katastrophenbild, keine nichtachsensymmetrische Pruefung.
- E3 Sanchis-Gual u. a. 2021 PRL "Multifield, multifrequency bosonic stars": l = 0 plus l = 1 stabilisiert den drehenden
  Stern, wenn der l = 0-Anteil gross genug ist (Kopplung nur ueber Gravitation).
- E4 Stabilitaet einkomponentiger drehender Q-Baelle (Suche): Zerfall durch nichtachsensymmetrische Moden (Aufspaltung),
  im Duennwandbereich teils stabil; im kubisch-quintischen NLS sind m = 1-Wirbelsolitonen oberhalb einer Leistungsschwelle
  stabil (Malomed, Mihalache u. a.).
- E5 Son und Stephanov 2002: Rabi-Kopplung cos(Delta theta), Sine-Gordon-Wand der relativen Phase, metastabil (Zerfall ueber
  Wirbelschleifen-Loecher), Bruchwirbel an Waenden, Einschluss-Analogie erwaehnt.
- E6 Bimodales kubisch-quintisches Modell mit Vierwellenmischung (Mihalache, Malomed u. a., um 2002 bis 2005): es gibt eine
  Arbeit zu stabilen drehenden Solitonen mit genau unserem Term (u^* v)^2 + c.c.
- Ausgang Block 1 (Suchtreffer; eingetragen 07:49:28 per date; die zuerst eingetippte Zeit "07:52" war geschaetzt und
  ist ~~07:52~~ gestrichen):
  - E1 [S] bestaetigt, soweit sichtbar: erste drehende Q-Baelle in 3+1 und 2+1, dazu radiale Anregungen; Stabilitaet im
    Suchtreffer nicht erwaehnt. Abstract noch lesen (E10).
  - E2 [S] bestaetigt: achsensymmetrisch, Existenzbereich.
  - E3 [S] bestaetigt: "adding a sufficiently large fundamental l = 0 bosonic star of another field, with a different
    frequency" stabilisiert. Achtung: **andere Frequenz**, Kopplung nur ueber Gravitation (U(1) x U(1)); das ist bei uns
    fuer g != 0 verboten (W1.4).
  - E5 [S] teilweise: 2 pi-Waende bei kleiner Kopplung bestaetigt; Metastabilitaet und Einschluss noch lesen (E8).
  - E6 [S] bestaetigt: Mihalache, Mazilu, Towers, Malomed, Lederer 2002/2003, bimodales kubisch-quintisches Modell mit
    Vierwellenmischung ("phase-sensitive nonlinear coupling"). Inhalt noch lesen (E9).
  - E4 [S] offen, neue Treffer: "Q-vortices, Q-walls and coupled Q-balls" (arXiv 1101.5366), "Slowly rotating Q-balls"
    (EPJC 2024), "Stability analysis for Q-balls with spectral method" (arXiv 2509.18656, JHEP 02(2026)078).

### Block 2 (Erwartungen notiert, Zeit siehe date-Zeile davor)

- E7 arXiv 1101.5366 "Q-vortices, Q-walls and coupled Q-balls": zweikomponentige Q-Baelle mit Kopplung ueber |phi_1|^2
  |phi_2|^2 (phasenblind), (1,0) heisst Windung in einer Komponente; Q-Wirbel instabil in einem Grenzfall.
- E8 Son und Stephanov (Volltext): Wand metastabil, Zerfall ueber Loecher mit Wirbelrand; Bruchwirbel (Windung nur in einer
  Komponente) haengen an einer Wand; Einschluss-Vergleich mit QCD im Text.
- E9 Mihalache u. a. PRE 67, 056608: mit Vierwellenmischung gibt es stabile drehende Solitonen nur, wenn beide Komponenten
  dieselbe Windung tragen (sonst bricht die Achsensymmetrie wie in W1.3).
- E10 Volkov und Woehnert (Abstract): keine Stabilitaetsaussage ausser Energie-Ladungs-Argument.
- E11 arXiv 2509.18656: Spektralmethode fuer lineare Stabilitaet einkomponentiger Q-Baelle, nicht drehend.
- E12 "Slowly rotating Q-balls" (Almumin u. a. 2024): kleine Drehimpulse ohne Quantisierung J = n Q, metastabil.
- Ausgang Block 2 (Abstracts, [A-W]):
  - E7 offen: Shnir 2011 (J. Phys. A 44, 425202), Abstract nennt "coupled non-topological 2-Q-ball solutions ... with an
    independent phase" und ein zweites Modell "two Q-balls minimally interacting via a coupling term". Kopplungsform und
    Stabilitaet stehen nicht im Abstract -> Volltext (E14).
  - E8 teilweise bestaetigt [A-W, Abstract]: 2 pi-Waende, "the wall tension determines the force between certain pairs of
    vortices at large distances", Zerfall "exponentially suppressed". **QCD oder Einschluss nicht im Abstract.** Volltext (E13).
  - E9 offen: Mihalache u. a. 2003: s = 1 stabil "only if their energy exceeds a certain critical value", ~25 % des
    Existenzbereichs; s >= 2 instabil. Gleiche oder entgegengesetzte Windung nicht im Abstract (E15).
    - Nachtrag beim Gegenlesen: Das Abrufwerkzeug schrieb "s>2", der spaetere Suchtreffer "s>=2". Widerspruechlich, an der
      Quelle nicht geklaert; in den Bericht geht nur die s = 1-Aussage.
  - E10 bestaetigt: Volkov und Woehnert sagen im Abstract nichts zur Stabilitaet.

### Block 3 (Erwartungen, Zeit siehe date-Zeile davor)

- E13 Son und Stephanov, Volltext: das Wort "confinement" kommt vor (lineares Potential zwischen einem Wirbel der einen und
  einem Antiwirbel der anderen Komponente), aber kein ausgearbeiteter QCD-Vergleich.
- E14 Shnir 2011, Volltext: das "minimal" gekoppelte Modell ist phasenblind (|phi_1|^2 |phi_2|^2); Stabilitaet der
  Q-Wirbel nur ueber Energie-Ladungs-Kurven, keine Zeitentwicklung.
- E15 Mihalache u. a. 2002/2003, Volltext: beide Komponenten tragen dieselbe Windung s (sonst keine Achsensymmetrie mit
  FWM); Stabilitaet aus linearer Analyse plus Simulation.
- E16 Almumin u. a. 2024 "Slowly rotating Q-balls": Drehimpuls ohne J = n Q ueber nichtachsensymmetrische oder
  angeregte Anteile, metastabil.
- E17 arXiv 2509.18656: nur nichtdrehende Q-Baelle, Spektralmethode.
- Ausgang Block 3, Teil 1:
  - **E13 verletzt (V1, siehe W3):** Son und Stephanov [A, arXiv cond-mat/0103451v2, S. 2, 7, 8, 10 bis 12 gelesen]
    ziehen den QCD-Vergleich ausdruecklich und weiter als erwartet (Hadronen, konstante Kraft, "high-spin meson states"
    als umeinander kreisende Wirbelpaare, dreidimensionale kompakte QED). Der entscheidende Befund liegt aber woanders:
    ihre Wand lebt nur in einem Regime, das es in unserem Modell nicht gibt (W3, V1).
  - E16 [S] bestaetigt: Almumin, Heeck, Rajaraman, Verhaaren, EPJC 84, 364 (2024): "classically long-lived metastable
    rotating Q-balls with small angular momentum, even for large charge".
  - E17 [A-W, Abstract] bestaetigt: Chen, Andersson, Li (arXiv 2509.18656, JHEP 02(2026)078): nur nichtdrehende Q-Baelle
    (Grund- und angeregte Zustaende), angeregte instabil auch gegen nichtkugelsymmetrische Stoerungen.
  - Neu im Suchtreffer (noch nicht gelesen): "Understanding the quantized angular momentum of rotating Q-balls", JHEP
    08(2026)108 -> E19.

## W3. Erwartungsverstoesse, voller Zyklus

### V1 (aus E13): Son-Stephanov-Waende brauchen eine Spin-Steifigkeit, die unser Modell nicht hat

- Gelesen [A]: Die 2 pi-Wand ist eine Sine-Gordon-Loesung der Phasen bei "eingefrorenen" Amplituden (Gl. 3.1 bis 3.3,
  Breite k^{-1}, k^2 = (m Omega/hbar) n/sqrt(n_1 n_2)). Sie ist "not topologically stable and can 'unwind'", ueber
  Konfigurationen mit n_1 = 0 oder n_2 = 0 (S. 8). Metastabil nur fuer Omega < Omega_c ~ Omega_0, also solange die Wand
  breiter ist als die laengere Heilungslaenge xi_A ~ (g/delta g)^{1/2} xi_B (Gl. 2.21, 3.5, 3.6); fuer n_1 = n_2 ist
  Omega_c/Omega_0 = 1/3 (Anhang A). Einschluss: phi_1- und phi_2-Wirbel durch eine Wand verbunden, Kraft konstant
  (S. 11 f.).
- Gegen unser Modell [ES]: delta g = g_11 - g_12 misst die Steifigkeit gegen Konzentrationsaenderung. Unser U(S) haengt
  nur von S ab (KANDIDAT 3.2: volle U(2) bei g = 0), also ist delta g = 0 exakt und xi_A unendlich. Das
  Son-Stephanov-Regime (Wand breiter als xi_A) ist **leer**. Die Amplituden sind nie eingefroren; die einzige
  Steifigkeit fuer Phase **und** Konzentration liefert der Kopplungsterm selbst (W1.1).
- **V1-Nachtrag beim Gegenlesen (bis 08:09:30, date):** "Regime leer" war zu stark formuliert. Bei g != 0 erzeugt der
  Kopplungsterm selbst eine Konzentrationssteifigkeit (bei gesperrter Phase wirkt er wie -g J |psi_1|^2 |psi_2|^2), und
  zwar von derselben Ordnung wie die Phasensteifigkeit. Wandbreite und xi_A sind deshalb fest gekoppelt; kein Parameter
  trennt sie. Die schaerfere Aussage [ES]: Alle Grosskreise durch +-x auf der Pseudospin-Kugel haben die Laenge pi (gleiche
  Gradientenkosten). Die Anisotropie-Energie ist auf dem Kreis durch y maximal und auf dem Kreis durch z minimal. Die reine
  Phasenwand (Kreis durch y) ist also ein Sattel gegen die Drehung des Wandkreises um die x-Achse; die Minima sind die
  beiden Ising-Waende ueber +z bzw. -z.
- Korrigierte Erwartung: Die richtige Literaturklasse fuer unsere Waende ist nicht die Sine-Gordon-Phasenwand, sondern die
  **Ising-artige (magnetische) Wand** eines Pseudospins mit leichter Achse, wie bei entmischenden Zweikomponenten-Systemen
  oder "ferromagnetischen" kohaerent gekoppelten Supraflüssigkeiten.
- Schreibtisch-Probe dazu [ES]: Die unitaere Basisdrehung psi_+- = (psi_1 +- psi_2)/sqrt 2 laesst den kinetischen Teil und
  U(S) unveraendert. In ihr wird der Kopplungsterm zu
  (g J/4)[(|psi_+|^2 - |psi_-|^2)^2 - 4 (Im psi_-^* psi_+)^2].
  - Der erste Teil ist eine reine Dichte-Wechselwirkung, die bei g > 0 **Entmischung** von psi_+ und psi_- belohnt.
  - Der zweite ist ein Rest zweiter Ordnung, der die relative Phase von psi_+ und psi_- auf 0 oder pi zieht.
  - Unsere pi-Waende (psi_1 = psi_2 gegen psi_1 = -psi_2) sind also **Entmischungswaende zwischen psi_+- Domaenen**; in der
    Wandmitte ist eine der urspruenglichen Komponenten rein (passt zu W1.1).
  - Der gefuellte Wirbel (a), psi_1 = f e^{i phi}, psi_2 = h, wird in der +- Basis zu psi_+- = (f e^{i phi} +- h)/sqrt 2:
    je ein **versetzter** Wirbel in psi_+ (bei phi = pi, f = h) und in psi_- (bei phi = 0, f = h). Das ist das bekannte Bild
    "Skyrmion = Wirbelmolekuel / Meronpaar" (Literatur noch pruefen, E22).

## W2 (Fortsetzung). Block 4 (Erwartungen, Zeit siehe date-Zeile davor)

- E18 Mihalache u. a. (Volltext/arXiv): mit Vierwellenmischung tragen beide Komponenten dieselbe Windung; Stabilitaet ab
  einer Energieschwelle.
- E19 JHEP 08(2026)108 "Understanding the quantized angular momentum of rotating Q-balls": erklaert J = n Q aus
  Achsensymmetrie und Eindeutigkeit; nichtachsensymmetrische Zustaende brechen die Quantisierung.
- E20 Kopplung zweiter Ordnung cos(2 Delta theta): Literatur zu s+is-Supraleitern (Garaud, Babaev) mit Z_2-Waenden und
  Bruchwirbeln an Waenden; nichts im Q-Ball-Kontext.
- E21 Tanaka 2002 und Babaev 2002: Phasensoliton zwischen Baendern, Bruchwirbel durch Phasensoliton gebunden.
- E22 Kernloser Wirbel bzw. Skyrmion = Wirbelmolekuel (Meronpaar) in kohaerent gekoppelten BEC (Kasamatsu, Tsubota,
  Ueda 2004/2005).
- E23 Vortons: Battye und Cotterill 2021 finden stabile Vortons im globalen U(1) x U(1)-Modell; Garaud, Radu, Volkov 2013
  im geeichten.
- E24 Leese 1991 Q-lumps: Drehung im Isoraum stabilisiert Lumps im O(3)-Sigma-Modell mit Potential gegen Kollaps.
- E25 Innere Josephson-Schwingung in Solitonen: langlebig, strahlt erst in hoeherer Ordnung; keine stationaere Loesung.
- Ausgang Block 4, Suchtreffer (Teil 1):
  - E19 [S] offen: DeVries, Vassallo, Verhaaren, JHEP 08(2026)108; leiten die Feldform drehender Q-Baelle her und geben
    "a method for computing their characteristic angular velocity". Abstract lesen (E26).
  - E20 [S] bestaetigt: zweite Ordnung "-eta_jk n_j n_k cos(2 theta_kj)" in Mehrband-Supraleitern; s+is mit Z_2-Waenden,
    "closed domain walls bind fractional vortices"; an Waenden spalten ganzzahlige Wirbel in Bruchwirbel. Neu und frisch:
    arXiv 2605.28221 (Mai 2026, dreikomponentig, zweite Ordnung), arXiv 2407.20132 (NJP, Bruchwirbel und Waende s+is),
    PRR 7, L012010 (2025).
  - E23 [S] teilweise: Battye und Cotterill PRL 127, 241601 (2021) "stable to axial and nonaxial perturbations"; ob global
    oder geeicht, klaert das Abstract (E28).
  - E24 [S] teilweise: Leese 1991 Nucl. Phys. B 366, 283: O(3)-Sigma-Modell 2+1 mit Potential, Q-lumps tragen
    topologische **und** Noether-Ladung; Stabilisierung gegen Kollaps nicht im Suchtreffer.
  - E18 [S] offen: 2D-Fassung J. Opt. A 4, 615 (2002); dazu Desyatnikov u. a. PRE 71, 026615 (2005) "hidden and explicit
    vorticity".
- Block 5 (Erwartungen):
  - E26 JHEP 08(2026)108: Omega = d E/d J bzw. omega/n; keine Aussage zu mehreren Komponenten.
  - E27 arXiv 2512.05763 "Double-flat-top half-vortices": zweikomponentig kubisch-quintisch, eine Komponente mit Windung,
    die andere ohne (Halbwirbel), flache Spitzen; stabil in einem Bereich; Kopplung phasenblind.
  - E28 Battye und Cotterill: globales U(1) x U(1)-Modell (kein Eichfeld), stabil nur in einem Parameterfenster.
  - E29 arXiv 2605.28221: zweite Ordnung macht in dreikomponentigen Supraleitern neue Wand- und Bruchwirbeltypen.
- Ausgang Block 5:
  - E27 [A-W, Abstract] bestaetigt: Zezyulin, PRA 113, 013501 (2026), arXiv 2512.05763: bimodal kubisch-quintisch, XPM
    (phasenblind), anziehend; "half-vortices ... carry different topological charges: zero for one component and nonzero
    for the other"; es gibt "dynamically stable stationary states"; instabile spalten den zentralen Wirbelkern in Fragmente
    ("solitary wave billiard"). Das ist die nichtrelativistische Form von (a) bei g = 0.
  - E28 verletzt (klein): Battye und Cotterill (arXiv 2111.07822) arbeiten laut Abstract im **geeichten** U(1) x U(1)
    ("stable to axial and, more importantly, non-axial perturbations"). Folge: kein direkter Beleg fuer das globale
    Modell ohne Eichfeld; unser Modell hat kein Eichfeld (KANDIDAT 3.2). Korrigierte Erwartung: Vorton-Stabilitaet im
    globalen Fall getrennt suchen (E33).
  - E29 teilweise verletzt (klein): Peng, Zhang, Hu (arXiv 2605.28221, Mai 2026) behandeln Grundzustaende und
    Higgs-Leggett-Moden bei Kopplung zweiter Ordnung (drei Komponenten, Kagome-PDW, Flussquant phi_0/3), aber im Abstract
    keine Waende und keine Bruchwirbel.
  - E26 offen: Springer verlangt Anmeldung; arXiv-Fassung suchen.
- Block 6 (Erwartungen):
  - E30 DeVries, Vassallo, Verhaaren (arXiv): Winkelgeschwindigkeit Omega = omega/n fuer psi ~ e^{i(n phi - omega t)}.
  - E31 Garaud und Babaev PRL 2014 (s+is): Z_2-Waende zwischen s+is und s-is, Bruchwirbel an Waende gebunden,
    Messsignatur ueber Magnetfeld der Wand.
  - E32 Kasamatsu, Tsubota, Ueda PRL 93, 250406 (2004): Rabi-Kopplung bindet Bruchwirbel zu Molekuelen, deren Abstand mit
    Omega schrumpft; Meronpaar-Bild.
  - E33 Vortons im globalen U(1) x U(1): Lemperiere und Shellard 2003 finden sie instabil oder nur knapp.
  - E34 Innere Josephson-Schwingung in Solitonen (Rabi-gekoppelt): Literatur zeigt Schwingung zwischen Komponenten; bei
    nichtlinearer Kopplung Selbsteinfang; Abstrahlung selten behandelt.
- Ausgang Block 6 (Suchtreffer [S]):
  - E30 offen: arXiv 2602.15196 (DeVries, Vassallo, Verhaaren; JHEP 08(2026)108) rechnet drehende Solitonen **in 2D**,
    analytische Naeherungen plus Numerik, "characteristic angular velocity". Abstract lesen (E35).
  - E31 bestaetigt: Garaud und Babaev PRL 112, 017003 (2014): Bruchwirbel als "junction point between two different domain
    walls"; bei ungleicher Wandspannung wirkt eine Kraft proportional zur Differenz. Neu: Science ads0189 "Observation of
    quantum vortex core fractionalization and skyrmion ..." (E36), Iguchi u. a. Science abp9979 (2023, Bruchwirbel mit
    temperaturabhaengigem Fluss), arXiv 2602.17399 (1/3-Wirbel in Kagome, 2026).
  - E32 bestaetigt: Kasamatsu, Tsubota, Ueda PRL 93, 250406 (2004): Wirbel je Komponente, verbunden durch eine Wand der
    relativen Phase = "vortex molecule", "nonaxisymmetric (pseudo)spin texture with a pair of merons". Die Anisotropie
    kommt dort aus ungleichen Streulaengen.
  - E33 bestaetigt: Lemperiere und Shellard PRL 91, 141601 (2003), globales U(1) x U(1): "Most vorton configurations are
    unstable and break in pieces when perturbed", duenne nicht, "thick vortons with small radius preserve their form".
  - E34 bestaetigt: laufende Phase und Selbsteinfang in gefangenen Kondensaten gut bekannt; Abstrahlung ins Kontinuum
    kommt in den Treffern nicht vor. Neu und frisch: arXiv 2602.05001 (2026, Rabi-getriebene Atmer), arXiv 2605.04441
    (2026, Dunkel-Hell-Solitonen mit Rabi- und Spin-Bahn-Kopplung).
- Block 7 (Erwartungen):
  - E35 arXiv 2602.15196: psi ~ F(r) e^{i(n phi - omega t)}, Omega = omega/n oder Omega = d E/d J; einkomponentig.
  - E36 Science ads0189: Experiment an einem Spinor-Kondensat (Spin 1), Wirbelkern spaltet in Halbquantenwirbel, die
    als Skyrmion-Paar gebunden bleiben.
  - E37 Zweikomponentige Q-Baelle mit verschiedenen Frequenzen bei phasenempfindlicher Kopplung: keine stationaeren
    Loesungen; nur phasenblinde Modelle (Friedberg-Lee-Sirlin, Bosonensterne) haben Mehrfrequenzloesungen.
  - E38 Hopfionen ohne Skyrme-Term: durch Drehung im Isoraum nicht stabil, weil Derrick in 3D den Kollaps zulaesst; es
    gibt dazu hoechstens verstreute Arbeiten.
- Ausgang Block 7:
  - E35 [A-W, Abstract] offen gelassen: Winkelgeschwindigkeit im Abstract nur benannt ("a method for computing their
    characteristic angular velocity"), 2D, einkomponentig. Stabilitaet nicht im Abstract. Kein Volltext gelesen.
  - E36 nicht lesbar (HTTP 403) -> ueber Suche (E39a).
  - E37 [S] nicht belegt, nicht widerlegt: Treffer behandeln phasenabhaengige **Kraefte** zwischen getrennten Q-Baellen
    (Q-ball Dynamics, hep-th/0003252; Shnir 2011 mit omega_1, omega_2 an verschiedenen Orten), nicht einen gemischten Ball
    mit phasenempfindlicher Kopplung. Neu, im Fenster: "Perturbations of Q-balls: from spectral structure to radiation
    pressure" (arXiv 2405.06591, 2024).
  - E38 [S] bestaetigt: "Isospinning hopfions" (Harland, Jaeykkae, Shnir, Speight, arXiv 1301.2923) im
    Faddeev-Skyrme-Modell, also **mit** Skyrme-Term; Potentiale stabilisieren isospinnende Hopfionen. "Q-Hopfion" oder
    "Q-knot" ohne Skyrme-Term: kein Treffer.
- Block 8 (Erwartungen):
  - E39a Science ads0189 (ueber Suche): Spin-1-BEC, Kernfraktionierung zu Halbquantenwirbeln, Skyrmion-Bindung.
  - E39 Battye, Cooper, Sutcliffe PRL 88, 080401 (2002): 3D-Skyrmion im zweikomponentigen BEC ist durch den Strom der
    Kernkomponente stabil (wie ein Vorton), ohne Skyrme-Term.
  - E40 Q-Baelle mit Flavour-Oszillation (Ladungsaustausch zwischen zwei Feldern): eine Arbeit zu "charge-swapping"
    (Copeland, Saffin, Zhou 2014) passt nur lose; keine zum inneren Rotor mit cos(2 Delta theta).
  - E41 Experimente 2024 bis 2026 zu Wirbelmolekuelen bzw. Einschluss in kohaerent gekoppelten BEC: eher keine direkte
    Beobachtung, aber Wandexperimente der Trento-Gruppe (falsches Vakuum, magnetische Waende).
- Ausgang Block 8:
  - **E39a verletzt (V2, siehe W3):** Science 393, 80-84 (2026) ist **kein** Spinor-BEC, sondern Rastertunnelmikroskopie
    am Mehrband-Supraleiter KFe2As2 [S, mehrere Treffer: Science-Seite, PubMed 42166558, SJTU-Vortrag].
  - **E39 verletzt (V3):** Battye, Cooper, Sutcliffe PRL 88, 080401 (2002) [S, Abstract]: stabile Skyrmionen (Q = 1, 2) in
    zweikomponentigen BEC "in the regime of phase separation" (volle 3D-Simulation). Die Bedingung ist **Entmischung**,
    nicht der Kernstrom allein.
  - E40 [S] bestaetigt (lose): charge-swapping Q-balls (Copeland, Saffin, Zhou, arXiv 1409.3232; Lebensdauern arXiv
    2101.06988); neu im Fenster: "Q-ball polarization - a smooth path to oscillons" (arXiv 2502.20519, PLB 2025) und
    "Excited oscillons and charge-swapping" (arXiv 2504.17382, 2025): Real- und Imaginaerteil schwingen mit leicht
    verschiedenen Frequenzen, die Phasendifferenz laeuft langsam. Das ist strukturell ein innerer Rotor, aber in **einem**
    komplexen Feld.
  - E41 bestaetigt: kein Experiment zu Wirbelmolekuelen gefunden. Theorie: Tylutki, Pitaevskii, Recati, Stringari PRA 93,
    043623 (2016): mit wachsender Rabi-Kopplung zerfaellt die Wand in Stuecke, die neue Wirbelpaare verbinden, "the analog
    of quark confinement and string breaking in quantum chromodynamics" [S]. Dazu PRR 2, 033373 (2020) und arXiv
    2207.05893 (Pendel-Dynamik eines Wirbelmolekuels).
- Block 9 (Erwartungen):
  - E42 Volkov und Woehnert, Volltext: Stabilitaet nur qualitativ (Vergleich E gegen m Q), keine Zeitentwicklung.
  - E43 Kleihaus, Kunz, List 2005, Volltext: dito, Stabilitaet nur ueber E < m Q.
  - E44 Dynamische Stabilitaet drehender Q-Baelle in 2+1 (Suche): Zerfall in zwei Baelle fuer die meisten omega, eventuell
    stabil im Duennwandbereich.
- Ausgang Block 9:
  - E42 bestaetigt, sogar schwaecher als erwartet [A, hep-th/0205157v3, S. 1 bis 3, 16 bis 19 gelesen]: Volkov und
    Woehnert machen **keine** Stabilitaetsaussage. Sie betonen, dass ein Anfangszustand mit J != 0 "will be most probably
    immediately radiated away" (S. 2), deshalb zaehlt nur Stationaritaet. Ergebnis: J = N Q (Q-Wirbel je Laenge und 3+1),
    Potential mit kubischer und quintischer Nichtlinearitaet in der Feldgleichung (S. 16), gleiche Klasse wie unser U(S).
    Bei Q = 410 steigt E von 307,29 (N = 0) auf 378,36 (N = 1, P = +) und 442,24 (N = 1, P = -) (Tabelle II, S. 18).
  - E43 [A-W, Abstract] bestaetigt: Kleihaus, Kunz, List: keine Stabilitaetsaussage im Abstract.
  - E44 [S] nicht belegt: kein Treffer mit einer dynamischen Stabilitaetspruefung einkomponentiger drehender Q-Baelle im
    flachen Raum. Nebenbei: "Spinning Q-ball Superradiance in 3+1D" (arXiv 2402.03193, 2024); "Quantum corrected Q-ball
    dynamics" (arXiv 2312.01139): nichtdrehende 2+1-Baelle im ganzen Frequenzbereich stabil.
- Block 10 (Erwartungen):
  - E45 Siemonsen und East 2021 (drehende skalare Bosonensterne mit Selbstwechselwirkung): solitonische (sextische)
    Potentiale stabilisieren drehende Sterne in einem Bereich; ohne Selbstwechselwirkung Balken-Instabilitaet
    (Sanchis-Gual u. a. 2019).
  - E46 Mihalache u. a. J. Opt. A 4, 615 (2002): 2D, Vierwellenmischung, drehende Solitonen mit gleicher Windung in beiden
    Komponenten stabil oberhalb einer Energieschwelle.
  - E47 Tanaka 2002 und Babaev 2002: Phasensoliton in Zweiband-Supraleitern, Bruchwirbel gebunden (Babaev auch
    Faddeev-Modell-Bezug).
- Ausgang Block 10:
  - E45 teilweise bestaetigt, mit einer Einschraenkung, die ich nicht erwartet hatte (V4, W3): Siemonsen und East PRD
    103, 044022 (2021), arXiv 2011.08247 [S, Abstract laut Suchtreffer]: m = 1-Ministerne haben eine nichtachsensymmetrische
    Instabilitaet im ganzen Parameterraum; "any boson star with m = 1 sufficiently far into the non-relativistic regime will
    be unstable independent of nonlinear scalar self-interactions"; nichtlineare Wechselwirkung "can quench the
    non-axisymmetric instability in some regions", auf beiden Aesten. Frisch im Fenster: arXiv 2609.06954 "The Dynamical
    Instability of Rotating Boson Stars" (Sept. 2026) und arXiv 2609.30021 "Stability and Formation of Solitonic Boson
    Stars" (Sept. 2026) -> E48.
  - E46 nicht gelesen: der Suchtreffer gab wieder das Abstract der 3D-Arbeit (PRE 67, 056608). Die Windungsfrage bleibt
    an der Quelle offen; aus W1.3 folgt [ES], dass bei (u^* v)^2 nur gleiche Windung achsensymmetrisch sein kann.
  - E47 [S] bestaetigt: Tanaka PRL 88, 017002 (2002): relative Phase dreht von 0 auf 2 pi, bei kleiner Zwischenband-Kopplung;
    Babaev PRL 89, 067001 (2002) vorhanden. Frisch: arXiv 2608.26782 (Aug. 2026, Stabilisierung von Phasensolitonen).
- Block 11 (Erwartungen):
  - E48 arXiv 2609.06954: Instabilitaet drehender Bosonensterne ist eine m = 2- bzw. Aufspaltungsmode; Mechanismus ueber
    Korotation oder Ergoregion.
  - E49 Q-lumps (arXiv 2304.05521, Q-lump scattering): Q-lumps sind stabil, die Drehung im Isoraum fixiert die Groesse.
  - E50 Metlitski und Zhitnitsky 2004: Wirbelringe im zweikomponentigen BEC durch Kernstrom der zweiten Komponente
    stabilisiert.
  - E52 Kang, Seo, Kim, Shin PRL 122, 095301 (2019): Wand-Wirbel-Verbund im Spin-1-BEC; Halbquantenwirbel an Waenden.
- Ausgang Block 11:
  - **E48 verletzt (V5, W3):** Zhou, Bao, Deng, Zhang, arXiv 2609.06954 (7. Sept. 2026) [A-W, Abstract]:
    Gross-Pitaevskii-Poisson mit Kontaktwechselwirkung; der drehende Stern zerfaellt nicht einfach, sondern zeigt im
    fruehen nichtlinearen Stadium "a quasiperiodic conversion between ring-like and twin-star-like density configurations";
    ein Drei-Moden-Hamiltonian erklaert das; abstossende Selbstwechselwirkung verlaengert die Lebensdauer deutlich.
  - E49 teilweise: Sutcliffe 2023 (arXiv 2304.05521): "Q-lumps are spinning planar topological solitons with stationary
    solutions that satisfy first-order Bogomolny equations"; zur Rolle der Drehung gegen Kollaps nichts im Abstract.
    Die Aussage "Drehung stabilisiert gegen Kollaps" bleibt [L?].
  - E50 [S] bestaetigt: Metlitski und Zhitnitsky JHEP 06 (2004) 017 (cond-mat/0307559): Vortonen im zweikomponentigen
    BEC "can be stable even if they are at rest", durch Kondensation der zweiten Komponente im Kern.
  - E52 [S] bestaetigt, Autorenname berichtigt: Kang, Seo, **Takeuchi**, Shin PRL 122, 095301 (2019) (nicht "Kim"):
    Spin-Domaenenwaende, begrenzt von Halbquantenwirbeln, im antiferromagnetischen Spin-1-BEC, aus Z_2-Brechung nach einem
    Quench; Aufspaltung ueber Schlangeninstabilitaet.
- Block 12 (Erwartungen):
  - E53 arXiv 2505.09553 "Phase domain walls in coherently driven BEC" (2025): Sine-Gordon-Waende der relativen Phase bei
    Rabi-Treiben, Zerfall ueber Wirbelpaare.
  - E54 PRR 3, 023043 (2021) "Dark-soliton-like magnetic domain walls": im ferromagnetischen Regime einer kohaerent
    gekoppelten Mischung sind die Waende Ising-artig (eine Komponente geht durch null), passend zu W1.1.
  - E14 Shnir 2011 Volltext (gespeichertes PDF, S. 1 bis 3): Kopplung der 2-Q-Baelle phasenblind.
- Ausgang Block 12:
  - **E53 verletzt (V6, W3):** Gavrilov, arXiv 2505.09553 (Mai 2025, rev. Feb. 2026) [A-W, Abstract]: kohaerent
    getriebenes zweikomponentiges Polaritonfluid. Die Waende kommen **nicht** aus einem Rabi-Term, sondern aus spontaner
    Z_2-Brechung der Spinsymmetrie ("opposite-phase domains"), es gibt "confined half-vortex molecules" und **zwei**
    topologische Wandtypen, einer wie magnetische Solitonen (mit Spinpolarisation), einer monopolartig mit Vorzugsrichtung.
  - E54 im Bau bestaetigt, im System nicht: Yu und Blakie PRR 3, 023043 (2021) [A-W, Abstract] ist Spin 1
    (ferromagnetisch), nicht Spin 1/2. Die Wand hat ein Dunkelsoliton-Profil **der Magnetisierung** bei nicht
    verschwindender Gesamtdichte, "stable against the snake instability" im Quasi-2D. Das ist genau der Wandbau aus W1.1
    (Pseudospin ueber den Pol, S bleibt endlich).
  - E14 [A, S. 1 bis 2] teilweise: Shnir 2011 nutzt fuer gekoppelte 2-Q-Baelle das Modell von Brihaye und Hartmann
    ("spinning and non-spinning solutions"); "twisted" Q-Baelle nur, wenn beide Bestandteile Kopien derselben
    Konfiguration sind. Die Kopplungsform (vermutlich |phi_1|^2 |phi_2|^2) habe ich nicht an der Quelle gesehen [L?].
- Block 13 (Erwartungen):
  - E55 Polarisations-Domaenenwaende (Haelterman und Sheppard 1994; Faserexperiment Gilles u. a. 2017): Waende zwischen
    links und rechts zirkular polarisierten Domaenen in isotropen Kerr-Medien, der Vierwellen-Mischterm ist dort Teil
    der Physik.
  - E56 Zezyulin (Volltext): die beiden Komponenten des Halbwirbels haben verschiedene Ausbreitungskonstanten
    (Frequenzen), die Kernkomponente die kleinere Energie je Teilchen.
  - E57 24-Monats-Suche "two-component Q-ball vortex / filled core / phase-sensitive coupling" (2024 bis 2026): nichts
    direkt zu unserem Kopplungsterm.
- Ausgang Block 13:
  - E55 [S] bestaetigt im Kern: Gilles, Bony, Garnier, Picozzi, Guasoni, Fatome, Nature Photonics 11, 102 (2017):
    erste direkte Beobachtung von Polarisations-Domaenenwaenden ("polarization knots") in normal dispersiven Fasern, mehr
    als 20 Jahre nach Haelterman und Sheppard. Dass die Domaenen gegenlaeufig zirkular polarisiert sind, steht nicht im
    Treffer [L?].
  - E56 teilweise verletzt (klein): Zezyulin [A-W, Volltext html]: kein Vierwellen-Mischterm (XPM beta = 2, alpha = 0);
    die Komponenten haben **verschiedene Ausbreitungskonstanten** b_1 != b_2 (bestaetigt), aber die Kernkomponente liegt
    knapp unter der Grenze, ist also **schwaecher** gebunden (nicht staerker wie erwartet). Grund: sein Modell ist nicht
    U(2)-symmetrisch (beta = 2 != 1), die Komponenten sehen verschiedene Potentiale. Stabilitaet: "the double-flat-top shape
    enhances the stability of half-vortex solutions, which lose stability as they depart from the double-flat-top regime".
  - E57 bestaetigt: kein Treffer zu Q-Baellen mit gefuelltem Wirbelkern bei phasenempfindlicher Kopplung (2024 bis 2026).
    Im Fenster, nicht direkt passend: arXiv 2511.16210 (JHEP 04(2026)136, drehende Feldklumpen in der Ebene), JHEP
    06(2026)126 (kompakte Q-Baelle in CP^N-Skyrme-Faddeev), arXiv 2504.13509, JHEP 12(2025)154.
- Block 14 (Erwartungen):
  - E58 arXiv 2511.16210: verallgemeinert Q-lumps (Sigma-Modell mit Potential) auf weitere Zielraeume; Drehung fixiert
    die Groesse.
  - E59 Kopplung zweiter Ordnung ("pair tunneling", (psi_1^* psi_2)^2) in zweikomponentigen BEC: wenige Arbeiten, eher
    im Doppelmulden-Josephson-Kontext, keine zu Waenden oder Halbwirbeln.
- Ausgang Block 14:
  - E58 verletzt (klein): Galushkina, Kim, Nugaev, Shnir, arXiv 2511.16210 (JHEP 04(2026)136) [A-W, Abstract] sind keine
    Q-lumps, sondern **drehende nichttopologische Solitonen in der Ebene** mit nach unten beschraenkten Potentialen;
    "kinematical stability, which is unachievable in the previously studied model with negative quartic self-interaction".
    Das betrifft Frage 1 (einkomponentige drehende 2D-Baelle), nicht Frage 4. Was "kinematisch" genau heisst, steht nicht im
    Abstract [L?: vermutlich Energie-Ladungs-Kriterium, keine Zeitentwicklung].
  - E59 bestaetigt: Treffer nur zur Rabi-Kopplung erster Ordnung (Son-Stephanov, Tylutki u. a., Calderaro u. a.); dazu
    "Split vortices in optically coupled BEC" (Rabi, Entmischungsregime: Wirbel in zwei Haelften mit Waenden). Zur Kopplung
    zweiter Ordnung in BEC: nichts gefunden.
- Block 15 (Erwartungen):
  - E60 arXiv 2502.20519 "Q-ball polarization": Polarisation = Amplituden- und Phasenverhaeltnis von Real- und Imaginaerteil;
    polarisierte Q-Baelle sind zeitperiodisch und gehen stetig in Oszillonen ueber; sie strahlen langsam.
  - E61 24-Monats-Suche "string breaking / confinement vortex coherently coupled condensate 2025 2026": Theorie ja,
    Experiment nein.
- Ausgang Block 15:
  - E60 teilweise verletzt: Blaschke, Romanczukiewicz, Slawinska, Wereszczynski, arXiv 2502.20519 (PLB 2025) [A-W,
    Abstract]: "in the complex phi^6 theory the oscillon, together with its spectral structure and the amplitude modulation,
    arises from the exited Q-ball carrying the bound and the quasi-normal modes". Kein Wort zur Polarisation im Abstract;
    wichtig ist: **dieselbe Modellklasse (komplexes phi^6)**, angeregte Q-Baelle mit gebundenen und quasinormalen Moden
    gehen stetig in Oszillonen ueber.
  - E61 bestaetigt: nur Theorie. Tylutki u. a. 2016 (Seilreissen als QCD-Analogon) und arXiv 1906.06237 (Zerfall der
    Wand in eingeschlossene Wirbelpaare: bei kleiner Kopplung ueber ein Wirbel-Antiwirbel-Paar, oberhalb einer kritischen
    Rabi-Frequenz ueber die Schlangeninstabilitaet). Kein Experiment gefunden.

## W3 (Fortsetzung). Weitere Erwartungsverstoesse, voller Zyklus

### V2 (aus E39a): Kernfraktionierung mit Skyrmion ist 2026 gemessen, aber im Supraleiter

- Gefunden [S, drei unabhaengige Treffer]: Science 393, 80-84 (2026), Rastertunnelmikroskopie an der K-terminierten
  Oberflaeche von KFe2As2: ganzzahlige Wirbel spalten in mehrere Bruchwirbel, die sich in Ketten mit einer
  CP^2-Skyrmion-Invariante ordnen ("chiral skyrmion"). Dazu Iguchi u. a. Science (2023, abp9979): Bruchwirbel mit
  temperaturabhaengigem Flussanteil.
- Folge: Die Kombination "Bruchwirbel plus Skyrmion-Textur", also (a) und (c) zusammen, ist gemessen, und zwar in einem
  Mehrband-Supraleiter (Eichfeld, drei Komponenten, frustrierte Josephson-Kopplung erster Ordnung). Das stuetzt [H], dass
  (a) und (c) zwei Lagen eines Objekts sind; die Uebertragung auf unser Modell ist nur qualitativ.
- Korrigierte Erwartung: Direkte Messungen zu Bruchwirbeln stehen eher in der Supraleiter- und Spinor-Literatur als bei
  kalten Rabi-gekoppelten Mischungen (dort nach Recherchestand nur Theorie).

### V3 (aus E39): Stabile 3D-Skyrmionen brauchen Entmischung, und die liefert unser g in der +- Basis

- Gefunden [S, Abstract]: Battye, Cooper, Sutcliffe 2002: stabile Skyrmionen (Q = 1, 2) "in the regime of phase
  separation", volle 3D-Simulation.
- Gegen V1 [ES]: In der Basis psi_+- ist unser Kopplungsterm eine Entmischungs-Wechselwirkung plus Rest zweiter Ordnung.
  Das Stabilitaetsregime von BCS 2002 ist also genau das, was g != 0 in der gedrehten Basis erzeugt.
- Einschraenkungen: BCS rechnen im Fallenpotential mit Hintergrunddichte; unser Q-Ball ist selbstgebunden; der Rest
  zweiter Ordnung fehlt dort; bei g != 0 ist die relative Ladung nicht erhalten.
- Korrigierte Erwartung: Fuer Frage 4 ist der Moderator Mischbarkeit (in der richtigen Basis), nicht der Kernstrom allein.

### V4 (aus E45): m = 1 ist im nichtrelativistischen Grenzfall unabhaengig von der Selbstwechselwirkung instabil

- Gefunden [S]: Siemonsen und East 2021: nichtachsensymmetrische Instabilitaet der m = 1-Sterne im ganzen Parameterraum
  der Ministerne; weit im nichtrelativistischen Bereich instabil "independent of nonlinear scalar self-interactions";
  Selbstwechselwirkung loescht sie nur in Teilbereichen.
- Folge [ES]: Der duennwandige Bereich unseres Modells (omega^2 -> 1/2) ist nicht der nichtrelativistische; der
  dickwandige (omega -> 1) ist es. Einkomponentige drehende Baelle nahe omega -> 1 sind nach dieser Literatur eher
  instabil; ein Fenster im Duennwandbereich ist moeglich (dazu passen Mihalache u. a. 2003, s = 1 stabil oberhalb einer
  Energieschwelle, ~25 % des Existenzbereichs, und Zezyulin 2026, Flachspitzen stabilisieren Halbwirbel).
- Korrigierte Erwartung: Die Frage "stabiler als der einkomponentige Wirbel" hat in der Literatur Datenpunkte in beide
  Richtungen und haengt am Regime (dick- gegen duennwandig). Sie ist nur per Test zu klaeren.

### V5 (aus E48): Drehende Sterne zerfallen nicht einfach, sie pendeln zwischen Ring und Zwillingsstern

- Gefunden [A-W, Abstract]: Zhou, Bao, Deng, Zhang (arXiv 2609.06954, 7. Sept. 2026): quasiperiodische Umwandlung
  "between ring-like and twin-star-like density configurations", Drei-Moden-Hamiltonian, abstossende
  Selbstwechselwirkung verlaengert die Lebensdauer.
- Folge: Das ist ein Literaturbeispiel fuer genau das, was Finn "oszillierend selbst stabilisieren" nennt, aber in einem
  Feld: ein Drei-Moden-Austausch statt Zerfall.
- [H] fuer unser Modell: Der gefuellte Wirbel bei g != 0 traegt eine erzwungene m = 2-Mode (W1.3). Moeglich ist ein
  quasiperiodisches Pendeln zwischen runder Textur (a) und Zwei-Wand-Form (c). Messbar als Schwingung des Wandkontrasts
  P2(t) (W6).

### V6 (aus E53): Z_2-Waende mit zwei Typen und eingeschlossenen Halbwirbel-Molekuelen, ohne Rabi-Term

- Gefunden [A-W, Abstract]: Gavrilov (arXiv 2505.09553): gegenphasige Domaenen aus spontaner Z_2-Brechung, "confined
  half-vortex molecules", zwei topologische Wandtypen, einer "similar to 'magnetic' solitons" mit Spinpolarisation, deren
  Vorzeichen von der Bewegungsrichtung abhaengt.
- Gegen W1.1 [ES]: Unsere pi-Wand laeuft ueber einen Pol, n_z = +S oder n_z = -S in der Wandmitte (psi_2 oder psi_1 geht
  durch null). Das sind **zwei entartete Wandtypen**, gespiegelt durch den Tausch 1 <-> 2, mit entgegengesetzter
  "Polarisation" n_z. Das passt zum ersten Wandtyp bei Gavrilov.
- Korrigierte Erwartung: Z_2-Domaenen der relativen Phase ohne lineare Kopplung sind bekannt (Polaritonen 2025, Spin 1 2019,
  s+is 2014, Fasern 2017). Neu fuer uns bleibt nur die Einbettung in einen selbstgebundenen relativistischen Q-Ball.

## W4. Gegensweep (ab 08:04; Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

- **G1 (geprueft, Schreibtisch plus zwei Quellen): "Der gefuellte Wirbel ist ein stationaeres Objekt mit einer
  Frequenz."** Falsch fuer g = 0, und das hat Folgen fuer g != 0.
  - Bei g = 0 sehen beide Komponenten dasselbe Potential U'(S), also (-lap + U'(S)) psi_a = omega_a^2 psi_a. Der knotenlose
    m = 0-Kern h ist Grundzustand dieses Operators; der m = 1-Anteil f hat wegen f^2/r^2 > 0 einen **echt groesseren**
    Eigenwert (f ist als Probefunktion im m = 0-Sektor zulaessig). Also omega_2^2 < omega_1^2 [ES, streng unter den
    Annahmen: stationaer, h knotenlos, U nur von S abhaengig].
  - Quellen, die das stuetzen: Sanchis-Gual u. a. 2021 stabilisieren "with a different frequency" [S]; Zezyulin 2026 hat
    b_1 != b_2 [A-W] (dort mit umgekehrter Reihenfolge, weil sein Modell nicht U(2)-symmetrisch ist).
  - Bei g != 0 sind zwei Frequenzen verboten (W1.4), ausser das Muster dreht starr mit Omega = omega_1 - omega_2 (m = 1).
    Im mitdrehenden System haben dann beide Komponenten die Frequenz omega_2, und der Kopplungsterm e^{-2 i phi'} steht
    still. **Die stetige Fortsetzung des gefuellten Wirbels zu kleinem g ist also ein starr drehendes m = 2-Muster**
    [ES]. Ob bei groesserem g ein ruhender Zweig (Omega = 0) existiert, ist offen [H].
  - Folge fuer die Hypothesen: (a) und (b) sind nicht getrennt. An jedem festen Ort dreht die relative Phase in der Zeit
    mit Omega, weil das Muster im Raum dreht.
- **G2 (geprueft, Schreibtisch): "J/Q ist quantisiert, J = n Q."** Gilt nur achsensymmetrisch (Volkov und Woehnert [A];
  DeVries u. a. 2026 leiten die Quantisierung her [A-W]). Beim gefuellten Wirbel ist J = Q_1 (bei g = 0), also
  0 < J/Q < 1 stetig. Bei g != 0 ist J erhalten, Q_1 nicht; J/Q bleibt eine freie Familienvariable [ES].
  - Folge: Die Frage "stabiler als der einkomponentige Wirbel-Q-Ball?" vergleicht Objekte in verschiedenen Sektoren.
    Bei 0 < J/Q < 1 gibt es keinen achsensymmetrischen einkomponentigen Wirbel. Die Konkurrenz sind dort der langsam
    drehende Ball (Almumin u. a. 2024), ein Ball mit umlaufendem Begleiter und der Zwillingsstern (V5).
- **G3 (geprueft, Schreibtisch): "Die Gradientenkosten beider Wandwege sind gleich."** Mit psi_1 = psi_2 = sqrt(S/2) e^{-+i
  Delta theta/2} ist |grad psi|^2 = S (grad Delta theta)^2/4; mit reellem psi_1 = sqrt S cos(a/2), psi_2 = sqrt S sin(a/2)
  ist es S (grad a)^2/4. Beide Wege sind Halbkreise der Laenge pi. W1.1 haelt [ES].
- G4 (nicht geprueft): Uebertragbarkeit nichtrelativistischer Befunde (BEC, NLS, Polaritonen, Supraleiter) auf den
  relativistischen Q-Ball. Unterschiede: Massenschwelle 1 fuer Abstrahlung, Gegenlaeufer-Kanal bei 2 omega (GF-BIC), kein
  Hintergrundkondensat, kein Eichfeld. Der NLS-Grenzfall ist omega -> 1 (dickwandig), der duennwandige Bereich liegt
  nicht in seiner Naehe.
- G5 (nicht geprueft): Wand im inhomogenen Ball. W1.1 gilt fuer festes S; im Q-Ball faellt S nach aussen ab, die
  Wandbreite delta ~ 1/sqrt(|g| J S) waechst dort, und die Waende enden am Rand. Einschluss ist deshalb nur bis zur
  Ballgroesse R testbar (kein Grenzfall grosser Abstaende).
- G6 (nicht geprueft): Dass die Leitungsformel J = 1 und N = 2 meint und keine weiteren Terme in KANDIDAT stehen, die
  Waende beeinflussen (Abschnitt 5 und 6 von KANDIDAT nicht gelesen).

## W5. Schreibtischantworten je Frage [ES], nach den Quellen

### W5.1 Frage 2: Was aendert cos(2 Delta theta) gegenueber cos(Delta theta)?

1. Wand: aus der metastabilen 2 pi-Sine-Gordon-Wand (Son und Stephanov [A]) wird eine **pi-Wand**. Sie trennt zwei
   verschiedene Vakua (Z_2) und ist im gemischten Bereich topologisch stabil (W1.2).
2. Bau: Weil unser U(S) keine Konzentrationssteifigkeit hat (delta g = 0, V1), laeuft die Wand ueber einen Pol, ist also
   Ising-artig. Es gibt zwei entartete Typen (n_z = +S oder -S in der Mitte, V6). Messgroesse: n_z/S in der Wandmitte,
   +-1 fuer Ising, 0 fuer eine reine Phasenwand.
3. Jeder (1,0)-Wirbel traegt **zwei** pi-Straenge (2 pi relative Windung = zwei pi-Waende). Sie koennen sich trennen;
   der Winkel zwischen ihnen ist frei.
4. Ein einzelner pi-Strang kann im Inneren nicht enden (keine Halbwirbel, weil psi_a eindeutig sind), also nicht allein
   reissen. Ein Doppelstrang kann an einem (1,0)/(0,1)-Paar enden; "Seilreissen" durch Paarerzeugung bleibt moeglich.
5. Kraft zwischen (1,0) und (0,1) auf Abstaenden > delta: konstant, gleich der doppelten pi-Wandspannung 2 sigma_pi
   (sigma_pi nicht gerechnet). Im Q-Ball nur bis zum Radius R pruefbar (G5).
6. Vorzeichen: g > 0 Waende zwischen Delta theta = 0 und pi; g < 0 zwischen +pi/2 und -pi/2. Der Fall g < 0 entspricht
   strukturell der s+is-Z_2-Wand (Zeitumkehr gebrochen; Garaud und Babaev 2014 [S]).
7. "Halbe Bruchwirbel" gibt es im Modell nicht. Halb ist die Wand, nicht der Wirbel (W1.2).
- Literaturlage dazu: pi-Waende bzw. Z_2-Waende der relativen Phase ohne lineare Kopplung sind bekannt (s+is 2014,
  Spin 1 2019 gemessen, Fasern 2017 gemessen, Polaritonen 2025); in Q-Baellen nach Recherchestand nicht behandelt.

### W5.2 Frage 3: innerer Rotor

- Stationaer nur als mitdrehendes Muster (G1). Ein reiner Rotor ohne Raumwindung (J = 0) ist nicht stationaer, auch bei
  g = 0 nicht: zwei knotenlose Komponenten im selben Potential U'(S) haben denselben Eigenwert, also dieselbe Frequenz
  (Argument aus G1). Der reine Rotor ist ein Schwebungs- bzw. Anregungszustand, verwandt mit den angeregten Q-Baellen,
  die im komplexen phi^6 stetig in Oszillonen uebergehen (Blaschke u. a. 2025 [A-W]).
- Frequenzbuchhaltung erster Ordnung in g [ES]: Mit omega_1 = omega + delta, omega_2 = omega - delta (relative Drehrate
  Omega_r = 2 delta) treibt der Term g J psi_1^2 psi_2^* die Komponente 2 bei omega + 3 delta, der Term g J psi_1^* psi_2^2
  die Komponente 1 bei omega - 3 delta. Strahlung ins Kontinuum erst, wenn omega + 3 delta > 1, also
  **Omega_r > (2/3)(1 - omega)**. Hoehere Harmonische omega + (2k + 1) delta oeffnen spaeter, mit hoeherer Potenz von g.
  - Zahlen: omega^2 = 0,6 -> Omega_r < 0,15 ruhig in erster Ordnung; omega^2 = 0,8 -> Omega_r < 0,071.
  - Zum Vergleich die Pendelfrequenz der Pseudo-Goldstone-Mode (GF-BIC 2.4 [P]): 0,069 / 0,131 / 0,218.
  - An den gemischten Baellen M1 / M2 / M3 (omega^2 = 0,7557 / 0,5774 / 0,5663) liegt die Rotorschwelle (2/3)(1 - omega)
    bei 0,087 / 0,160 / 0,165 [ES, von Hand]. Die Kontinuumskante fuer kleine Librationen ist 1 - omega = 0,131 / 0,240 /
    0,247 (GF-BIC 2.4 nennt dieselben Kanten). Der Rotor oeffnet den Kanal also frueher als die Libration, weil sein
    Seitenband bei omega + (3/2) Omega_r liegt, das der Libration bei omega + nu.
  - Oberhalb der Separatrix ist jede Drehrate moeglich (nahe der Separatrix gegen null). Ein ruhiges Fenster
    0 < Omega_r < (2/3)(1 - omega) existiert also [ES].
- Mitdrehender gefuellter Wirbel (J != 0): erste Ordnung treibt psi_2 im m = 2-Kanal bei 2 omega_1 - omega_2 =
  omega_1 + Omega. Abstrahlung erster Ordnung genau dann, wenn **2 omega_1 - omega_2 > 1** [ES].

### W5.3 Frage 4: Q-Hopfionen, Q-lumps, Vortonen

- Q-lumps (Leese 1991, Sutcliffe 2023 [S/A-W]): CP^1 mit Potential in 2+1, topologische plus Noether-Ladung, stationaer
  drehend, Bogomolny-Gleichungen erster Ordnung. Die Drehung braucht eine **erhaltene Isospin-U(1)** [L?].
- Unser Modell: Bei g = 0 gibt U(2) diese Ladung (Q_1 - Q_2 erhalten). Bei g != 0 ist die Pseudospin-Anisotropie
  zweiachsig, es bleibt **keine** kontinuierliche Pseudospin-Symmetrie, also keine erhaltene Isoladung. Der
  Q-lump-Mechanismus steht bei g != 0 nicht zur Verfuegung [ES].
- Isospinnende Hopfionen gibt es nur mit Skyrme-Term (Harland u. a. 2013 [S]); "Q-Hopfion" ohne Skyrme-Term: nach
  Recherchestand nicht belegt (keine Arbeit gefunden, 24-Monats-Suche eingeschlossen).
- Naechste belegte Objekte: Vortonen im globalen U(1) x U(1) (Lemperiere und Shellard 2003: meist instabil, dicke kleine
  bleiben [S]); Vortonen im BEC in Ruhe stabil (Metlitski und Zhitnitsky 2004 [S]); 3D-Skyrmionen stabil bei Entmischung
  (Battye, Cooper, Sutcliffe 2002 [S]) -> V3.
- Topologischer Schutz: Im Q-Ball faellt S nach aussen auf null, die Pseudospin-Abbildung ist dort nicht definiert. Eine
  strenge Hopf-Ladung gibt es nicht; das passt zur Entscheidung vom 23.09. (Konfigurationsraum zusammenziehbar,
  bosonisch) [P, Memory "Spin 1/2 nicht moeglich"]. Q-Hopfionen koennten hier hoechstens langlebig sein.

## W6. Testvorschlag (Frage 5)

### T1: mitdrehender gefuellter Wirbel im 2D-Querschnitt (entscheidet a gegen c und prueft G1)

- Anfangsdaten: exakte g = 0-Loesung mit zwei Frequenzen (f mit m = 1 bei omega_1, knotenloser Kern h bei omega_2 <
  omega_1), aus zwei gekoppelten radialen ODEs (Schiessen). Zwei Baelle: klein (omega_1^2 ~ 0,8, R ~ delta) und
  duennwandig (omega_1^2 ~ 0,6, R >> delta); Fuellung Q_2/Q ~ 0,3.
- Danach g langsam einschalten (Rampe ueber t ~ 50, langsam gegen Omega und nu_0), g_end = 0,02 / 0,05 / 0,1 / 0,2 / 0,5,
  dazu g = 0 und g -> -g als Kontrolle. Laufzeit T ~ 2000. Relativistische Gleichung aus KANDIDAT 2.2 auf dem 2D-Gitter mit
  Schwamm.
- Messgroessen:
  1. Musterdrehzahl Omega_pat aus der Phase des m = 2-Fourierkoeffizienten von |psi_1|^2 (bzw. n_x^2 - n_y^2)
  2. Wandkontrast P2(t) = int f_1^2 f_2^2 cos(2 Delta theta) / int f_1^2 f_2^2 (rahmenunabhaengig; bei g = 0 exakt 0)
  3. n_z/S in der Mitte jeder Phasenstufe (Ising +-1 gegen Phasenwand 0)
  4. J/Q (erhalten, Kontrolle) und Q_1/Q (nicht erhalten)
  5. Fluss in psi_2, m = 2-Kanal, bei 2 omega_1 - omega_2 durch einen Kreis vor dem Schwamm
- Vorab [H]:
  - Texturregime (R/delta <~ 1 oder g <= 0,05): P2 = O(g), linear; Omega_pat = omega_1 - omega_2 auf +-10 %.
  - Wandregime (R/delta >= 3, etwa g = 0,5 am duennwandigen Ball): P2 > 0,5, zwei pi-Stufen mit |n_z|/S > 0,8 in der Mitte.
  - Abstrahlung erster Ordnung nur, wenn 2 omega_1 - omega_2 > 1.
- **Scheitert, wenn:**
  - (a) bei g = 0,02 und 0,05 die m = 2-Amplitude nicht linear in g skaliert (A_2/g um mehr als Faktor 1,5 verschieden)
    oder das Muster nicht mit omega_1 - omega_2 +- 10 % dreht (dann ist G1 falsch oder der Wirbel zerfaellt);
  - (c) bei R/delta >= 3 der Kontrast P2 unter 0,5 bleibt (keine Plateaus) oder die Stufen reine Phasenwaende sind
    (|n_z|/S < 0,3 in der Mitte, dann ist V1/W1.1 falsch);
  - die Abstrahlung bei 2 omega_1 - omega_2 < 1 nicht mindestens zwei Groessenordnungen kleiner ist als knapp oberhalb.
- Nebenbefund, frei: quasiperiodisches Pendeln von P2(t) zwischen (a)- und (c)-Form (V5).

### T2: reiner Rotor, radial (entscheidet b)

- Kugelsymmetrisch (l = 0 fuer beide Komponenten), also ein 1D-Radialcode. Start: gemischter Ball (psi_1 = psi_2, g > 0,
  symmetrischer Sektor exakt beta_eff), dann Frequenzversatz omega +- delta ueber die Anfangsgeschwindigkeit.
- Messgroessen: Delta theta(t) ladungsgewichtet, Zahl der pi-Durchlaeufe, Energie der Relativmode, abgestrahlte Energie
  je Umlauf.
- Vorab [H]: unterhalb Omega_r = (2/3)(1 - omega) Verlust je Umlauf mindestens hundertfach kleiner als knapp darueber.
- **Scheitert, wenn** die Verlustrate beim Ueberschreiten von (2/3)(1 - omega) keinen Sprung zeigt, oder wenn der Rotor
  unterhalb der Schwelle binnen zehn Umlaeufen in Libration faellt.

### Kosten [ES, nicht gemessen]

- T1: 2D, etwa 512^2 Punkte (dx ~ 0,15), dt ~ 0,05, T ~ 2000, vier reelle Felder: pro Lauf Groessenordnung 1 bis 5 min
  auf einer P4000-Spur (Doppelgenauigkeit; die Zeit wird von der Startlatenz der Kernel bestimmt, nicht von den Flops).
  Etwa 12 Laeufe, also unter 1 h Spurzeit. Anfangsdaten per radialem Schiessen: Sekunden.
- T2: 1D radial, Sekunden bis wenige Minuten je Lauf; 10 Werte von delta x 2 Werte von g: Minuten.
- Beide passen in die Kleintest-Spur (<= 10 min je Lauf), Vorab-Datei vor dem Start.

## W7. Kalibrierung

- (a) Gemessen (Experiment, laut Quelle): Bruchwirbel mit CP^2-Skyrmion-Ketten in KFe2As2 (Science 2026 [S]);
  Bruchwirbel mit temperaturabhaengigem Fluss (Science 2023 [S]); Polarisations-Domaenenwaende in Fasern (Nature Photonics
  2017 [S]); Wand-Wirbel-Verbund mit Halbquantenwirbeln im Spin-1-BEC (PRL 2019 [S]). Im eigenen Modell gemessen, also
  gerechnet: nur GF-BIC [P] (Pseudo-Goldstone-Frequenzen, Instabilitaet des einkomponentigen Balls).
- (b) Nuetzlich verdichtet [ES]: zweiachsige Pseudospin-Anisotropie (W1.1); +- Basis = entmischende Mischung (V1);
  zwei Frequenzen -> Mitdrehen (G1); J/Q stetig (G2); Strahlungsschwellen 2 omega_1 - omega_2 > 1 und Omega_r > (2/3)(1 -
  omega) (W5.2); Son-Stephanov-Regime leer (V1); kein Q-lump-Mechanismus bei g != 0 (W5.3).
- (c) Gewachsene Gewissheit ohne neue Evidenz:
  - "(a), (b) und (c) sind eine Familie": im Lauf der Arbeit sicherer geworden, gestuetzt nur auf Schreibtischargumente und
    Analogien (V2, V5). Im Modell nicht gerechnet.
  - "Duennwandige Baelle liegen im Wandregime": ohne Vorfaktor in delta, ohne gerechnete Wandspannung.
  - "Unterhalb der Schwelle ist die Abstrahlung klein": Standardargument; die Amplituden der Harmonischen sind nicht
    gerechnet.
  - Uebertragung aus BEC, NLS, Polaritonen und Supraleitern (G4).
- **Warnzeichen:** Meine Sicherheit stieg, waehrend die Frage feiner wurde (von "gibt es (c)?" zu "welcher Wandtyp, wie
  viele Straenge"). Das Feinere ist fast ganz Schreibtisch.

## W8. Offene Fragen (wandern mit)

- O1 Gibt es bei groesserem g einen ruhenden Zweig (Omega = 0) des gefuellten Wirbels, oder bleibt er immer mitdrehend?
- O2 Wandspannung sigma_pi und Breite delta mit Vorfaktor fuer unser U(S) (1D-Rechnung, billig).
- O3 Amplitude der Abstrahlung des mitdrehenden Musters in den m = 2-Kanal von psi_2 (erste Ordnung, wie GF-BIC 3.1).
- O4 Zeigt der gefuellte Wirbel das quasiperiodische Pendeln Ring <-> Zwillingsform (V5) als (a) <-> (c)?
- O5 Mihalache u. a. 2002/2003 an der Quelle: welche Windungspaare mit Vierwellenmischung (nicht gelesen).
- O6 Leese 1991 an der Quelle: Stabilisierung der Q-lumps durch die Isodrehung (nicht gelesen, [L?]).
- O7 Kopplungsform bei Brihaye und Hartmann (Shnir 2011, Abschnitt III nicht gelesen).
- O8 Ist der einkomponentige drehende Ball unseres U(S) im Duennwandbereich dynamisch stabil (ohne psi_2)? In der
  Literatur fuer flache Q-Baelle nach Recherchestand nicht belegt; Hinweise nur aus Bosonensternen und NLS (V4).

## W9. Nachlese nach dem ersten Berichtsstand (ab 08:10:22, date)

- Block 16 (Erwartungen):
  - E62 Kleihaus, Kunz, List 2005, Volltext: Stabilitaet nur als E < m Q (gegen Zerfall in freie Teilchen), keine
    dynamische Pruefung drehender Q-Baelle.
  - E63 Axenides, Komineas, Perivolaropoulos, Floratos 2000 (2D-Q-Ball-Dynamik): Stoesse und Stabilitaet nichtdrehender
    Baelle; drehende Baelle hoechstens als Stossprodukt, keine Stabilitaetspruefung.
- Ausgang Block 16:
  - E62 bestaetigt [A, gr-qc/0505143v1, S. 1 bis 3 und 17 gelesen]: Die einzige Stabilitaetsaussage betrifft
    kugelsymmetrische Baelle: "Q-balls are stable along the lower branch, when their mass is smaller than the mass of Q free
    bosons" (S. 1). Drehende Baelle: "J = nQ", Frequenzabhaengigkeit "analogous to the non-rotating Q-balls" (S. 17), keine
    dynamische Pruefung. Potential (3): U = lambda phi^2 (phi^4 - a phi^2 + b) mit lambda = 1, a = 2, b = 1,1 (bzw. 1).
    - Umrechnung auf unsere beta-Familie [ES, von Hand]: Mit S = phi^2, Masse^2 = lambda b und Feldskala c = b/a folgt
      U -> s - s^2 + (b/a^2) s^3, also beta = b/a^2 = 0,275 (bzw. 0,25, entartet). Unser Modell hat beta = 0,5. Drehende
      Q-Baelle bei beta = 0,5 sind in den gelesenen Arbeiten nicht gerechnet.
  - E63 nicht geprueft: Das Websuch-Budget der Sitzung ist erschoepft (Meldung 200 von 200). Axenides u. a. 2000 bleibt
    [L?].
