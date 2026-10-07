# SUCH-1: Suchwoerter fuer unsere Themen – unter welchem Namen laeuft das in der Literatur?

- Auftrag: claude-primary, Runde 9, Karte SUCH-1 (Finn 07:55: "mach mal ein research zu suchworten die das beschreiben woran
  wir gerade arbeiten"). Bearbeiter: feldforscher (Anthropic-Agent), reine Literaturarbeit, keine Rechnung.
- Beginn: 2026-09-30 07:55:40 CEST (date). Ende: letzte Zeile (nach dem Schreiben mit date gemessen).
- Arbeitsdatei und Ergebnis zugleich (Feldregel 5). Gestrichenes bleibt stehen und ist als ~~gestrichen~~ markiert.
- Markierungen:
  - **[A]**: an der Quelle gelesen (arXiv-Abstract roh per curl/arXiv-API oder Volltext), ohne Zusammenfassungsmodell.
  - **[W]**: WebFetch-Auszug (Zusammenfassungsmodell dazwischen; Wortlaut nicht selbst geprueft).
  - **[S]**: nur Suchtreffer oder Suchmaschinen-Zusammenfassung.
  - **[V]**: in den Vorarbeiten gelesen, hier nicht erneut: RUNDE-06/resonanz3d/L4-BIC-LITERATUR.md und
    RUNDE-07/L4-BIC-FAMILIE-LITERATUR.md.
  - **[L?]**: aus dem Gedaechtnis, nicht an der Quelle geprueft.
  - **[ES]**: eigener Schluss.
- Vorarbeit: Themen 1 bis 3 sind in Runde 6 und 7 schon breit gesucht (Q-Baelle, Kinks, Oszillonen, NLS-Mathematik,
  Inagaki-Murakami 2609.15056, Ayala u. a. 2609.23217). Diese Datei sucht dort nur neue Namen und Nachbarfelder.

## BERICHT (Synthese begonnen 2026-09-30 08:10:11 CEST, date; das Abrufprotokoll mit allen Erwartungen steht darunter)

### 0 Kurzfazit (hoechstens 10 Zeilen)

1. **Stille Atmungsstellen:** Der Mechanismus hat zwei alte Namen: "accidental / single-resonance BIC" (eingebetteter
   Eigenwert) und, fuer die Phasenregel, **"nonradiating source / radiationless motion"** (Schott 1933: eine Kugelschale
   strahlt bei k R = n pi nicht [S]). Eine lineare BIC-Leiter bei Q-Baellen, Solitonen oder Troepfchen: keine Treffer gesehen.
2. **Beweis:** naechster Nachbar ist Yu & Lu 2025 (strenger Existenzbeweis einer BIC in drei gekoppelten Schroedinger-
   Gleichungen); rechnergestuetzt gibt es sonst nur Abwesenheitsbeweise und seit 19.09.2026 einen Optik-Fall.
3. **Drei Komponenten:** Der 120-Grad-Stern mit zwei Drehsinnen ist der frustrierte, zeitumkehrbrechende Zustand der
   Mehrband-Supraleiter; mit Paarterm cos(2 Delta theta) sind seit Mai 2026 alle Grundzustaende klassifiziert (Peng, Zhang,
   Hu [A]; ob ihr Modell sonst unserem gleicht, ist nicht geprueft).
   Fabry-Perot-BIC, polarizable vacuum). **Troepfchen:** Grundatmung in 1D immer gebunden, in 3D nur dickwandig eingebettet.

### 1 Erwartungsverstoesse (das Wichtigste zuerst; Einzelheiten im Abrufprotokoll)

1. **V1, Phasenregel = Schott-Bedingung.** Erwartet: Nebenbemerkung. Gefunden: eigene Literaturlinie (Schott 1933,
   Bohm & Weinstein 1948, Goedecke 1964 [S]; Rentzber, arXiv:2608.24171, Aug. 2026 [A]: Abstrahlung "vanishes exactly at the
   positive roots of j_2"). Unser delta-Schalen-Modell (M = g V_c(R) sin(qR)) ist diese Bedingung im Kanal l = 0 [ES]. Neu
   bleibt nur: Die Quelle ist selbst Eigenmode (BIC statt angetriebener Quelle), die Welle ist verzerrt (theta), und der
   Radius waechst mit omega (Haeufung ~1/n).
2. **V3, Troepfchen im falschen Regime.** Erwartet: direktes Laborgegenstueck. Gefunden: In 1D ist die Atmungsmode "always
   bound" (Tylutki u. a. 2020 [A]); in 3D ist der Monopol nur zwischen N ~ 20 und ~ 934 eingebettet (Petrov 2015 [A], obere
   Zahl [S]), also dickwandig, und an beiden Raendern geht die offene Wellenzahl gegen null. Folge [ES]: Die Grundatmung ist
   ein schwacher Kandidat fuer eine Leiter; hoehere radiale Obertoene sind besser. Das betrifft MESS-1 direkt.
3. **V2, cos(2 Delta theta)-Dreikomponenten-Modell 2026 durchgerechnet.** Peng, Zhang, Hu, arXiv:2605.28221 [A]: "8-fold
   degenerate frustrated state", Zeitumkehrbruch, "Higgs-Leggett mode ... softening near the phase boundaries". FA-1s Stern
   ist dort der homogene Grundfall.
4. **V4, strenger BIC-Existenzbeweis in Schroedinger-Systemen seit 2025.** Yu & Lu, arXiv:2504.19573 [A]. Erwartet hatte ich
   nur symmetriegeschuetzte Faelle und Ayala u. a. 2026 [V].
5. Kleiner: Cui, Xia, Yang 2023 (arXiv:2304.09708) [A] beweisen "no embedded eigenvalue" fuer radiale Grundzustaende eines
   *Klein-Gordon-Systems*, aber mit EINER Schwelle; das markiert die Regimegrenze zu uns (zwei Schwellen). Mein
   Fabry-Perot-Autor war falsch (Shabanov, nicht Shipman). Die Websuche war um 08:05 erschoepft (200 von 200).

### 2 Suchwortlisten, Treffer und Urteil je Thema

Legende der Datenbanken: arXiv-API (export.arxiv.org/api/query, Felder abs:, ti:, all:; getestet, siehe Protokoll),
arXiv-Kategorien, INSPIRE-HEP (Syntax `t "..." and date > 2024` [ES, Syntax nicht getestet]), Google Scholar
(`allintitle:`, Anfuehrungszeichen), APS/PhySH-Begriffe [ES, nicht gegen die PhySH-Liste geprueft]. Queries mit "(benutzt)"
sind in dieser Recherche gelaufen.

#### T1 Stille Atmungsstellen (deutsch: "stille Stellen", "Atmungs-BIC-Leiter")

- **Begriffe (12):**
  1. bound state in the continuum (BIC); accidental BIC; single-resonance / parameter-tuned BIC
  2. embedded eigenvalue; embedded eigenstate; embedded eigenvalue of the linearized operator
  3. **nonradiating source; radiationless motion** (Schott, Bohm-Weinstein, Goedecke, Devaney-Wolf)
  4. anapole; nonscattering state (nur zur Abgrenzung)
  5. Fabry-Perot BIC; interior phase quantization
  6. Friedrich-Wintgen BIC (zwei Resonanzen, ein Kanal; Abgrenzung)
  7. von Neumann-Wigner BIC (oszillierendes Potential; nicht unser Mechanismus)
  8. vanishing Fermi golden rule constant; zero-width resonance; Feshbach resonance
  9. topological charge of BIC; winding number; polarization vortex
  10. quasinormal mode of Q-balls; internal mode; half-bound / Feshbach-type quasinormal mode
  11. Nachbarn: form-factor zero / diffraction minimum (Kernphysik), Ramsauer-Townsend (Streunullstellen)
  12. thin-wall Q-ball (R ~ 1/(omega - omega_min), Grund fuer die 1/n-Haeufung)
- **Datenbanken und Queries:**
  - arXiv: physics.optics, nlin.PS, hep-th, math-ph, math.SP, math.AP.
  - arXiv-API (benutzt): `abs:"internal mode" AND abs:continuum AND (abs:soliton OR abs:oscillon OR abs:kink OR
    abs:"Q-ball" OR abs:bubble)`; `abs:"continuum" AND abs:"bound state" AND (abs:soliton OR abs:droplet OR abs:solitary)`.
  - INSPIRE: `t "Q-ball" and (t quasinormal or t "internal mode" or t resonance) and date > 2024`.
  - Scholar: `"nonradiating source" "spherical shell"`; `"radiationless" Schott "Bohm" "Weinstein"`;
    `"bound state in the continuum" "internal mode"`.
  - APS/PhySH: "Bound states in the continuum", "Solitons", "Resonances".
- **Treffer:**
  - Inagaki & Murakami 2026, arXiv:2609.15056 [V]: fuenf Abstrahlungsnullstellen der Innenmode einer kritischen Blase, aber
    nichtlinear (zweite Harmonische). Bezug: naechste Soliton-Leiter.
  - Rentzber 2026, arXiv:2608.24171 [A]: Strahlung einer Kugel exakt null an den Nullstellen von j_2 bzw. j_1. Bezug:
    Schott-Leiter lebt, als angetriebene Quelle.
  - Monticone, Sounas, Krasnok, Alu 2019, ACS Photonics 6, 3108 [S]: Anapol (nicht streuend, anregbar) ist kein
    eingebetteter Eigenzustand (nicht anregbar, Reziprozitaet). Bezug: Abgrenzung unserer Stelle vom Anapol.
  - Prudencio & Silveirinha 2021, arXiv:2111.00311 [A]: Monopol-BIC in 3D-Kugeln (ENZ); frueher nur bei fein abgestimmtem
    Radius. Bezug: l = 0-BIC in 3D gibt es in der Optik, mit Sondermaterial.
  - Zhen, Hsu, Lu, Stone, Soljacic 2014, PRL 113, 257401 [S]: BIC tragen erhaltene ganzzahlige Ladungen. Bezug: Umlauftest.
- **Urteil: teilweise bekannt.** Mechanismus bekannt als "accidental BIC" plus "nonradiating source (Schott-Leiter)".
  Q-Ball- oder Soliton-Innenmode mit exakter linearer Nullstellenleiter: keine Treffer gesehen (dritte Suchrunde nach R6, R7).
- **Die zwei Sonderfragen:**
  - *BIC-Leitern bei Solitonen oder Troepfchen?* Eine Leiter von Abstrahlungsnullstellen an einem Soliton gibt es, aber
    nichtlinear (Inagaki & Murakami [V]). Eine linear eingebettete Leiter an Solitonen oder Troepfchen: keine Treffer gesehen.
    Fuer Troepfchen spricht das Regime eher dagegen (V3).
  - *Sind Anapol- oder "nonradiating source"-Bedingungen dasselbe wie unsere Phasenregel?* **Nonradiating source: ja, auf
    Quellenebene** (delta-Schale -> sin(qR) = 0 ist Schotts Bedingung; die verzerrte Welle entspricht der
    Devaney-Wolf-Bedingung im Hintergrundpotential [ES, Devaney-Wolf nur L?]). **Anapol: nein im strengen Sinn.** Ein Anapol
    ist ein angetriebener, nicht streuender Zustand, kein Eigenmode [S]; unsere Stelle ist ein Eigenmode, der seine eigene
    nichtstrahlende Quelle ist. Messbarer Unterschied: siehe Unterscheidungspunkt U1.

#### T2 Rechnergestuetzter Beweis (deutsch: "Beweis eingebetteter Eigenwert")

- **Begriffe (11):** computer-assisted proof; validated numerics; rigorous numerics; numerically assisted proof; interval
  arithmetic; ball arithmetic (Arb, python-flint); Krawczyk operator; Newton-Kantorovich; radii polynomial; Jost solution /
  rigorous Evans function; absence (bzw. persistence) of embedded eigenvalues.
- **Datenbanken und Queries:** arXiv math.SP, math.AP, math.NA, math.DS. arXiv-API (benutzt): `abs:"embedded eigenvalue"
  AND (abs:soliton OR abs:computer OR abs:interval OR abs:solitary)`. Scholar: `"computer-assisted proof" "embedded
  eigenvalue"`; `"bound states in the continuum" existence "rigorous"`. zbMATH Open: Stichwort "embedded eigenvalue" [ES].
- **Treffer:**
  - Yu & Lu 2025, arXiv:2504.19573 [A]: strenger Existenzbeweis einer Friedrich-Wintgen-BIC in drei gekoppelten
    1D-Schroedinger-Gleichungen. Bezug: naechster Nachbar von BEWEIS-1 (analytisch, 1D, selbstadjungiert).
  - Marzuola & Simpson 2010, arXiv:1003.2474 [A]: "numerically assisted proof", dass die 3D-kubische NLS keine eingebetteten
    Eigenwerte hat. Bezug: gleiche Werkzeugklasse, umgekehrte Richtung.
  - Asad & Simpson 2011, arXiv:1101.2485 [V]: Abwesenheit, u. a. 3D kubisch-quintische NLS (unser NLS-Grenzfall).
  - Ayala, Blanco, Cakoni, Hovsepyan, Vogelius 2026, arXiv:2609.23217 [V]: rechnergestuetzter Beweis diskreter Frequenzen
    ohne Antwort (Optik, zweite Harmonische).
  - Cui, Xia, Yang 2023, arXiv:2304.09708 [A]: Klein-Gordon-System, radial, "no embedded eigenvalue"; eine Schwelle.
- **Urteil: teilweise bekannt.** Werkzeug und Nachbarsaetze existieren; ein rechnergestuetzter Existenzbeweis eines
  eingebetteten Eigenwerts in der Linearisierung eines Solitons: keine Treffer gesehen.

#### T3 Nichtlinearer Zerfall (deutsch: "Zerfall ueber die zweite Harmonische")

- **Begriffe (10):** nonlinear Fermi golden rule; radiation damping of internal modes; second-harmonic radiation;
  breather nonexistence / "beyond all orders" (Segur-Kruskal); quasi-breather; oscillon decay rate; embedded soliton;
  nonlinear bound state in the continuum (Vorsicht: meist Photonik-Strukturen); metastability when the FGR constant
  vanishes; Stokes constant / exponentially small splitting.
- **Datenbanken und Queries:** arXiv nlin.PS, math.AP, hep-th. arXiv-API: `abs:"internal mode" AND abs:"Fermi golden rule"`
  [ES, nicht gelaufen]; Scholar: `"radiation damping" "internal mode" soliton`; `"Fermi golden rule" vanishes metastable`.
- **Treffer:**
  - Soffer & Weinstein 1999, arXiv:chao-dyn/9807003 [V]: nichtlineare goldene Regel als generische Annahme.
  - Segur & Kruskal 1987, PRL 58, 747 [S]: keine echten kleinen Breather in phi^4, Abstrahlung jenseits aller Ordnungen.
  - Bizon & Romanczukiewicz 2026, arXiv:2603.18605 [V]: Strahlungsdaempfung der Innenmode, 1D quadratisches KG.
  - Inagaki & Murakami 2026 [V]: an ihrer nichtlinearen Nullstelle A ~ tau^(-1/4) statt tau^(-1/2).
- **Urteil: bekannt unter den Namen "nonlinear Fermi golden rule" / "radiation damping of internal modes".** Unsere Lage
  (lineare Breite null, Rest ueber die zweite Harmonische) ist das lineare Gegenstueck zu Inagaki & Murakami: teilweise
  bekannt.

#### T4 Zwei und drei Komponenten (deutsch: "Gesamtformel mehrkomponentig", "Farb-Stern")

- **Begriffe (12):** multicomponent / multi-field Q-balls; cored Q-ball; charge-swapping Q-balls; non-Abelian Q-balls;
  coherently coupled NLS / four-wave-mixing (phase-dependent) coupling; **second-order Josephson coupling** / pair
  tunneling; frustrated three-band superconductor; time-reversal symmetry breaking (BTRS, s + is); chirality (Dreiecks-XY,
  Kawamura [L?]); Leggett mode / Higgs-Leggett mode; gyroscopic stabilization, Krein signature, negative-energy mode,
  dissipation-induced instability (Thomson-Tait-Chetaev [L?]); vortex trimer.
- **Datenbanken und Queries:** arXiv cond-mat.supr-con, cond-mat.quant-gas, hep-th, nlin.PS. arXiv-API (benutzt):
  `abs:"Q-ball" AND (abs:multicomponent OR abs:"two-component" OR abs:"non-Abelian" OR abs:"charge-swapping" OR
  abs:"multi-field")`. Scholar: `"second-order Josephson" three-component frustrated`; `"time-reversal symmetry breaking"
  "three-band" chirality`.
- **Treffer:**
  - Peng, Zhang, Hu 2026, arXiv:2605.28221 [A]: Dreikomponenten-GL mit cos(2 Delta theta)-Kopplung, 8-fach entarteter
    frustrierter Zustand, Zeitumkehrbruch, Higgs-Leggett-Mode. Bezug: FA-1 ohne Ball.
  - arXiv:1107.0995 (2011) [S, Titel; Autoren Garaud, Carlstroem, Babaev L?]: topologische Solitonen in
    Dreiband-Supraleitern mit BTRS.
  - Lennon 2021, arXiv:2201.00024 [A]: Q-Baelle mit mehreren Ladungen, "cored Q-ball". Bezug: gemischter Ball, gefuellter Kern.
  - Kevrekidis, Pelinovsky, Saxena 2014, arXiv:1412.1522 [V]: Moden negativer Energie plus Kontinuum -> Instabilitaet.
    Bezug: FA-1-Befund an der Kontinuumsschwelle.
- **Urteil: teilweise bekannt.** Stern, Chiralitaet und Zeitumkehrbruch sind bekannt; der selbstgebundene Stern mit
  Kontinuum, Kreiselstabilitaet und zweiter BIC-Leiter im Gegentakt-Kanal: keine Treffer gesehen.

#### T5 Drehung (deutsch: "Wirbel, gefuellter Kern, innerer Rotor")

- **Begriffe (12):** spinning / rotating / vortex Q-balls; slowly rotating Q-balls; Q-vortex; massive-core vortex /
  filled-core vortex / coreless vortex; superconducting cosmic string (Witten) / vorton; domain wall of relative phase
  (Son-Stephanov); vortex molecule / confinement / string breaking; generalized (higher-order) Josephson term; half-quantized
  vortex; isospinning hopfions / Q-lumps / Q-kinks; internal ac Josephson effect / running phase; macroscopic quantum
  self-trapping.
- **Datenbanken und Queries:** arXiv cond-mat.quant-gas, hep-th, hep-ph. arXiv-API: `ti:"rotating Q-balls" OR
  ti:"generalized Josephson"` (benutzt). Scholar: `"vortices with massive cores"`; `"domain wall" "relative phase"
  vortex confinement`; `"isospinning" soliton`.
- **Treffer:**
  - Almumin, Heeck, Rajaraman, Verhaaren 2023, arXiv:2302.11589 [A]: langlebige, langsam rotierende Q-Baelle mit kleinem J.
    Bezug: SP-1 (langlebige m = +-1-Anregung).
  - Richaud, Penna, Mayol, Guilleumas 2020, arXiv:1908.06668 [A]: Wirbel einer Sorte beherbergen die andere als
    "massive cores". Bezug: ROT-1.
  - Chatterjee, Gudnason, Nitta 2019, arXiv:1912.02685 [A]: Josephson-Term hoeherer Ordnung, "angular domain walls".
    Bezug: ROT-3.
  - Tylutki, Pitaevskii, Recati, Stringari 2016, arXiv:1601.03695 [S] und Eto & Nitta 2012, arXiv:1201.0343 [S]:
    Einschluss von Wirbelpaaren bzw. -tripeln durch Waende, Quark-Analogie. Bezug: ROT-3, FA-1.
  - Smerzi, Fantoni, Giovanazzi, Shenoy 1997, cond-mat/9706221 [A]: ac-Josephson, Plasmaschwingung, Selbsteinfang.
    Bezug: ROT-2 (laufende relative Phase).
- **Urteil: bekannt unter Namen.** ROT-1 = massive-core vortex bzw. Witten-String; ROT-2 = interner ac-Josephson-Effekt
  mit pi-periodischem Potential [ES, aus Smerzi u. a. und dem cos(2 Delta theta)-Term]; ROT-3 = Son-Stephanov-Wand und
  Wirbelmolekuel. Die Q-Ball-Fassung mit cos(2 Delta theta):
  keine Treffer gesehen, sie ist aber ein kleiner Schritt.

#### T6 Kollektiv (deutsch: "dunkles Paar, stille Kette")

- **Begriffe (10):** subradiance; dark state (Dicke); collective BIC; Fabry-Perot BIC; BIC in arrays / chains of dielectric
  spheres; coupled-resonator optical waveguide (CROW); decoherence-free interaction (waveguide QED); coupled-mode theory;
  Q-ball interactions / charge transfer; charge-swapping Q-balls.
- **Datenbanken und Queries:** arXiv physics.optics, quant-ph, hep-th. Scholar: `"Fabry-Perot" "bound state in the
  continuum" distance`; `subradiance "finite separation" dark state`; `"arrays of dielectric spheres" "bound states in the
  continuum"`.
- **Treffer:**
  - Marinica, Borisov, Shabanov 2008, PRL 100, 183902 [S]: BIC zwischen zwei Resonatoren bei Fabry-Perot-Abstand.
  - Bulgakov & Maksimov 2018, arXiv:1805.08036 [A]: BIC in Kugelketten, Fano-Merkmale nahe der BIC.
  - Subradianz in 3D: endlicher Abstand, kein vollkommen dunkler Zustand (arXiv:2502.09851) [S].
  - Axenides, Komineas, Perivolaropoulos, Floratos 1999, hep-ph/9910388 [A]: zwei Q-Baelle schwingen mit der Differenz
    ihrer Innenfrequenzen. Bezug: Grundrauschen jeder KOLL-1-Messung.
- **Urteil: bekannt unter Namen** (Subradianz, Fabry-Perot-BIC, Ketten-BIC). Zwei Q-Baelle als dunkles Paar: keine Treffer
  gesehen. Exakt dunkel in 3D bei endlichem Abstand ist nicht zu erwarten [ES, siehe U6].

#### T7 Laborbezug (deutsch: "Troepfchen, fluessiges Licht, Kernatmung")

- **Begriffe (12):** quantum droplet; self-bound droplet; self-evaporation; particle emission threshold; breathing /
  monopole mode; Lee-Huang-Yang (LHY); extended Gross-Pitaevskii equation; Bose-Bose / dipolar droplet; liquid light;
  cubic-quintic NLS / flat-top soliton; isoscalar giant monopole resonance / escape width / continuum RPA; Q-ball analogue
  in BEC.
- **Datenbanken und Queries:** arXiv cond-mat.quant-gas, physics.optics, nucl-th. arXiv-API (benutzt): `all:"quantum
  droplet" AND all:breathing`; `abs:"self-evaporation" OR abs:"self-evaporating" OR abs:"particle emission threshold"`.
  Scholar: `"self-evaporation" droplet "breathing mode" width`; `"escape width" "monopole"`.
- **Treffer:**
  - Petrov 2015, arXiv:1506.08419 [A]: Selbstverdampfung; fuer 20,1 < N < 94,2 (reskaliert) liegen alle Moden ueber der
    Schwelle; der Monopol bleibt bis N ~ 934 eingebettet (obere Zahl nur [S]).
  - Tylutki, Astrakharchik, Malomed, Petrov 2020, arXiv:2003.05803 [A]: 1D, Atmungsmode "always bound"; andere Moden
    kreuzen der Reihe nach die Schwelle.
  - Flynn, Parisi, Billam, Parker 2022, arXiv:2209.04318 [A]: unbalancierte Troepfchen, mehrere gleichzeitig zerfallende
    Schwingungen.
  - Enqvist & Laine 2003, cond-mat/0304355 [A]: "perfect formal analogy" zwischen Q-Baellen und BEC-Solitonen.
  - GMR: escape width aus Kontinuums-RPA (arXiv:2201.04578) [S].
- **Urteil: teilweise bekannt** (Selbstverdampfung, Schwellen, Analogie). Emissionsbreite gegen N mit Nullstellen: keine
  Treffer gesehen. Regimewarnung V3.


- **Begriffe (12):** quadratic / Stelle / higher-derivative gravity; massive spin-2 ghost; Yukawa corrections -4/3 und
  +1/3; inverse-square-law test / short-range gravity / torsion balance (Eoet-Wash, HUST); Lee-Wick; fakeon / purely virtual
  particle; unstable ghost; PPN of quadratic gravity; **polarizable vacuum** (Dicke 1957, Puthoff 2002); refractive-index
  gravity / optical-mechanical analogy; Gordon metric / moving medium / Fresnel drag; frame-dragging / gravitomagnetism.
- **Datenbanken und Queries:** arXiv gr-qc, hep-th, hep-ex. INSPIRE: `t "quadratic gravity" and (t yukawa or t
  "short-range") and date > 2024`. Scholar: `"polarizable vacuum" "frame dragging"`; `"Stelle" "torsion balance"`.
- **Treffer:**
  - Zhu & Li 2026, arXiv:2601.05750 [A]: PPN der quadratischen Gravitation; "m_W > m_R/4" fuer anziehende Gravitation.
  - van Manen, Blankenstein, Mazumdar 2026, arXiv:2609.22501 [A]: Stelle-Gravitation in Verschraenkungstests,
    m_0 < 4^(1/3) m_2; Unterscheidung ab ~0,02 eV bei ~40 um.
  - Donoghue & Menezes 2019, arXiv:1908.02416 [A]: Geist als instabile Resonanz, nicht im asymptotischen Spektrum.
  - Anselmi & Piva 2017, arXiv:1703.04584 [A]: Neuformulierung von Lee-Wick (Grundlage der Fakeonen).
  - Puthoff 2002, Found. Phys. 32, 927 [S]; Ye 2009, arXiv:0903.3665 [A]: polarisierbares Vakuum.
  ART im schwachen Feld, und Frame-Dragging wurde in den fruehen, statischen Formulierungen "not addressed" [S]. Unser
  erster Ordnung gleich) ist damit die ausgerechnete Fassung einer bekannten Luecke. Eine Arbeit, die das fuer PV
  ausrechnet, habe ich nicht gesehen (nur eine Suche). Die ST-1-Talform (Teilaufhebung der zwei Yukawa-Terme): keine
  Treffer gesehen, ebenfalls nur eine Suche.

### 3 Die 10 besten Suchwoerter insgesamt

| # | Suchwort | deckt ab |
|---|---|---|
| 1 | "bound state in the continuum" + ("internal mode" OR soliton OR "Q-ball") | T1, T6 |
| 2 | "nonradiating source" / "radiationless motion" (Schott, Devaney-Wolf) | T1 (Phasenregel) |
| 3 | "embedded eigenvalue" + ("linearized" OR "computer-assisted proof") | T1, T2 |
| 4 | "Fermi golden rule" + (vanishing OR "radiation damping" OR "internal mode") | T1, T3 |
| 5 | "Friedrich-Wintgen" / "Fabry-Perot BIC" / "accidental BIC" | T1, T6 |
| 6 | "self-evaporation" + "quantum droplet" + "breathing mode" | T7 |
| 7 | "second-order Josephson" / "frustrated" + "time-reversal symmetry breaking" | T4 |
| 8 | "domain wall of relative phase" / "vortex molecule" / "vortex trimer" | T5, T4 |
| 9 | "massive-core vortex" / "spinning Q-balls" / "slowly rotating Q-balls" | T5 |
| 10 | "polarizable vacuum" + "quadratic gravity Yukawa" | T8 |

### 4 Regime und Moderatoren (Regel 1)

| Moderator | Regime A | Regime B | Folge fuer uns |
|---|---|---|---|
| angetrieben gegen Eigenmode | Anapol, nichtstrahlende Quelle: Quelle vorgegeben [S] | BIC: Quelle ist die Mode selbst [S] | gleiche Nullstellenbedingung, verschiedene Objekte |
| Kopplungsordnung | linear eingebettet (unser Pol) | nichtlinear (Inagaki-Murakami) [V] | zwei Leitern, nicht verwechseln |
| offene Kanaele | 1 Kanal: isolierte exakte Nullstellen entlang eines Parameters [V] | 2+: nur Minima, exakt erst mit zweitem Parameter [V] | Troepfchen: balanciert (Dichte- und Spinsektor entkoppelt) gegen unbalanciert (gemischt) [ES] |
| Geometrie | kompaktes endliches 3D-Objekt: keine echte BIC ohne Sondermaterial [S] | periodische Kette: BIC moeglich [A, Bulgakov-Maksimov] | Q-Ball ist weder kompakt noch Kette (Auslaeufer, zwei Kanaele) [ES] |
| relativistisch gegen NLS | NLKG: Mode bei Re rho ~ 1,58 bis 1,74, q = sqrt((omega + Re rho)^2 - 1) ~ 2,1 bis 2,4 bleibt gross [Hand, aus n = 1 und n = 9; die Angabe "q ~ 2,4" in V3 unten gilt nur fuer n = 1] | NLS-Troepfchen: Monopol nahe der Schwelle, q klein [A Petrov, ES] | Leiter bei Troepfchen eher in Obertoenen |
| Dimension | 1D: Atmungsmode gebunden (Tylutki [A]), keine eingebetteten Eigenwerte (Collot u. a. [V]) | 3D: eingebettet moeglich | 1D-Negativbefund V7 passt |
| Schwellenzahl | eine Schwelle: "no embedded eigenvalue" bewiesen (Cui u. a. [A]) | zwei Schwellen 1 - omega, 1 + omega | Unser Fall liegt ausserhalb dieses Satzes |

- **Regel 6 [ES]:** "Mode strahlt nicht" hat mindestens sieben Wege: Schwelle, Symmetrie, Integrabilitaet,
  Friedrich-Wintgen, akzidentelle lineare Ueberlapp-Null, nichtlineare Ueberlapp-Null, periodische Anordnung (Kette). Die
  gemeinsame Groesse ist die Projektion der Quelle auf die offenen Streuzustaende [V]. Diese Recherche fuegt fuer diese
  Groesse den Namen "nonradiating source" (Devaney-Wolf-Bedingung) hinzu.

### 5 Unterscheidungspunkte (Regel 2)

| # | Erklaerungspaar | wo sie messbar auseinanderlaufen [ES] |
|---|---|---|
| U1 | Anapol / angetriebene Quelle gegen BIC (Eigenmode) | Anregung von aussen: Eine einlaufende l = 0-Welle bei omega* regt die BIC nicht an. Das Fano-Merkmal im Streuquerschnitt wird zu omega* hin schmal und verschwindet. Ein Anapol bleibt anregbar. Test: Streuung am Q-Ball nahe 0,7977 |
| U2 | Einzelresonanz-Nullstelle gegen Friedrich-Wintgen mit breitem Partner (offene Innenwelle als Fabry-Perot-Mode) | FW verlangt einen Partnerpol, dessen Breite bei omega* maximal wird (Summe der Breiten etwa fest). R6 schloss nur Partner mit Gamma < 0,1 aus. Test: Polsuche bis Im ~ 1 |
| U3 | Schott-Formfaktor mit aeusserer Welle (q R) gegen verzerrte Innenwelle (k_c R) | dickwandige Seite (kleines n), wo k_c und q stark verschieden sind. R8: k_c-Fassung traf 8 von 8 blind; q-Fassung gab Abstaende 0,93 bis 1,02 pi (R7) |
| U4 | Troepfchen: Grundatmung gegen Obertoene | Grundatmung: hoechstens 0 bis 1 Nullstelle im Fenster N ~ 20 bis 934; Obertoene: Leiter in N im flachen Bereich |
| U5 | Troepfchen balanciert gegen unbalanciert | balanciert: exakte Nullstellen entlang N moeglich (ein Kanal je Sektor); unbalanciert: nur Minima entlang N, exakte Nullstelle braucht die Unbalance als zweiten Regler |
| U6 | KOLL-1: Weitergabe an der stillen Stelle gegen abseits | Abstandsgesetz: an der stillen Stelle nur Nahfeld ~ e^{-kappa_c d} (kappa_c ~ 0,52); abseits Strahlungskopplung ~ sin(q d)/(q d) mit Verlust. In 3D kein exakt dunkles Paar bei endlichem d |

### 6 Gegensweep-Befunde (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1, teilgeprueft: "Schotts Bedingung ist k R = n pi."** Belegt nur ueber eine Suchzusammenfassung ("2a = m c T", also
  k a = m pi) [S]. Die Dissertation von Gbur liess sich nicht laden (TLS-Fehler). Die Bessel-Nullstellen-Leiter selbst ist
  durch Rentzber 2026 [A] belegt. Status: plausibel, Primaerquelle Schott/Bohm-Weinstein nicht gelesen.
- **G2, geprueft: "Troepfchen haben dieselbe Ein-Kanal-Struktur wie unser Ball."** Petrov [A]: Die Schwelle -mu trennt
  diskretes und kontinuierliches Spektrum; u-Kanal offen, v-Kanal geschlossen [ES]. Fuer zwei Komponenten koennen aber zwei
  offene Kanaele zusammenfallen (U5). Die Selbstverstaendlichkeit gilt also nur im balancierten Einfeld-Modell.
- **G3, geprueft (Gegenrichtung): "Solitonen haben keine eingebetteten Eigenwerte."** Gefunden: Cui, Xia, Yang 2023 [A]
  (Klein-Gordon-System, eine Schwelle), Marzuola & Simpson 2010 [A] (3D-kubische NLS), dazu [V] Collot, Germain, Pacherie
  2025 (1D) und Li & Yang 2026 (3D kubisch). Keiner dieser Saetze erfasst eine NLKG-Linearisierung mit zwei Schwellen.
  Nicht gefunden: ein Satz, der unseren Fall ausschliesst. Urteil: kein Widerspruch nach Recherchestand, kein "widerlegt".
- **G4, nicht geprueft:** Kato/Froese-Herbst ("keine Eigenwerte oberhalb aller Schwellen") als Stuetze fuer U2 und G3 [L?],
  wegen Suchgrenze.
- **G5, nicht geprueft:** Volltexte (ausser Petrov), russische und chinesische Literatur, Bezahlseiten (APS, Springer).
- **G6, nicht geprueft:** Q/Anti-Q-Vernichtung (Chem 14); Axenides u. a. und Battye & Sutcliffe erwaehnen sie im Abstract
  nicht [A].

### 7 Offene Fragen

1. Gibt es eine Q-Ball- oder Troepfchen-Arbeit, die Gamma(omega) bzw. Gamma(N) als Kurve zeigt (auch in Bosonstern-QNM)?
   Drei Suchrunden: nein; Abdeckung: englisch, arXiv-Abstracts.
2. U2: Ist die Phasenregel besser als Friedrich-Wintgen zwischen Wandzustand und offener Innenwelle zu lesen?
3. U4/U5 fuer MESS-1: Obertoene statt Grundatmung; balanciert statt unbalanciert.
4. Nicht gesucht wegen Grenze (B7.2 bis B7.6): Q/Anti-Q-Vernichtung; Kato/Froese-Herbst; Zibold u. a. 2010 (Kennung
   1008.3057 lieferte nichts); Fakeon-Laborsignaturen 2024-2026; rigorose Evans-Funktion (Barker & Zumbrun [L?]).
5. Beobachtung des Wirbeleinschlusses in kohaerent gekoppelten BEC: in einer Suche nicht gefunden, kein Urteil.
6. Mitteilung an Ya Yan Lu (Beweis), Inagaki & Murakami (Leiter) oder die Q-Ball-Gruppe Dorey/Romanczukiewicz/Shnir?
   Frage an die Leitung.

### 8 Kalibrierung

- **(a) Gemessen bzw. an der Quelle gelesen:** die [A]-Abstracts dieser Datei; Petrov 2015 Seite 3 im Volltext; die
  Projektzahlen aus RUNDE-07 bis RUNDE-09 (nicht von mir gerechnet).
- **(b) Nuetzlich verdichtet:** die Namenszuordnung je Thema; Schott-Bedingung = delta-Schalen-Modell; Troepfchen-Regime
  (V3); Ein- gegen Zwei-Kanal bei Troepfchen (U5); Abstandsgesetz fuer KOLL-1 (U6).
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** "Phasenregel = Schott" stuetzt sich auf ein Spielzeugmodell und eine
  Suchzusammenfassung; "Grundatmung schwacher Kandidat" ist ein Argument, keine Rechnung; "Q-Ball-BIC-Leiter nicht in der
  Literatur" ist eine Abwesenheitsaussage bei begrenzter Abdeckung.
- **Warnzeichen:** Meine Sicherheit, dass "alles schon einen Namen hat", stieg im Lauf der Suche, waehrend die Frage feiner
  wurde (was genau neu ist: Selbstkonsistenz, Haeufung, Q-Ball-Kontext). Einen Namen zu finden heisst nicht, dass das
  Ergebnis bekannt ist.

### 9 Quellenliste (neu in dieser Datei; [V]-Quellen siehe RUNDE-06/07)

- Almumin Y., Heeck J., Rajaraman A., Verhaaren C. B. (2023): Slowly rotating Q-balls. arXiv:2302.11589. https://arxiv.org/abs/2302.11589
- Anselmi D., Piva M. (2017): A new formulation of Lee-Wick quantum field theory. arXiv:1703.04584. https://arxiv.org/abs/1703.04584
- Axenides M., Komineas S., Perivolaropoulos L., Floratos M. (1999): Dynamics of Nontopological Solitons - Q Balls. hep-ph/9910388. https://arxiv.org/abs/hep-ph/9910388
- Battye R., Sutcliffe P. (2000): Q-ball Dynamics. hep-th/0003252. https://arxiv.org/abs/hep-th/0003252
- Bohm D., Weinstein M. (1948): The Self-Oscillations of a Charged Particle. Phys. Rev. 74, 1789 [S]. https://journals.aps.org/pr/abstract/10.1103/PhysRev.74.1789
- Brumelot C., Medina L. (2026): Existence of Ground State and Excited Spinning Q-Vortex Solitons on Finite Domains. arXiv:2602.07676. https://arxiv.org/abs/2602.07676
- Bulgakov E. N., Maksimov D. N. (2018): Optical response induced by bound states in the continuum in arrays of dielectric spheres. arXiv:1805.08036. https://arxiv.org/abs/1805.08036
- Chatterjee C., Gudnason S. B., Nitta M. (2019): Chemical bonds of two vortex species with a generalized Josephson term and arbitrary charges. arXiv:1912.02685. https://arxiv.org/abs/1912.02685
- Cui Y., Xia B., Yang K. (2023): Spectrum of linearized operator at ground states of a system of Klein-Gordon equations. arXiv:2304.09708. https://arxiv.org/abs/2304.09708
- DeVries B., Vassallo F., Verhaaren C. B. (2026): Understanding the Quantized Angular Momentum of Rotating Q-balls. arXiv:2602.15196. https://arxiv.org/abs/2602.15196
- Donoghue J. F., Menezes G. (2019): Unitarity, stability and loops of unstable ghosts. arXiv:1908.02416. https://arxiv.org/abs/1908.02416
- Enqvist K., Laine M. (2003): Q-ball dynamics from atomic Bose-Einstein condensates. cond-mat/0304355. https://arxiv.org/abs/cond-mat/0304355
- Eto M., Nitta M. (2012): Vortex trimer in three-component Bose-Einstein condensates. PRA 85, 053645; arXiv:1201.0343 [S]. https://arxiv.org/abs/1201.0343
- Flynn T. A., Parisi L., Billam T. P., Parker N. G. (2022): Quantum Droplets in Imbalanced Atomic Mixtures. arXiv:2209.04318. https://arxiv.org/abs/2209.04318
- Fort C., Modugno M. (2020): Self-evaporation dynamics of quantum droplets in a 41K-87Rb mixture. arXiv:2012.10347. https://arxiv.org/abs/2012.10347
- Garaud J., Carlstroem J., Babaev E. [Autoren L?] (2011): Topological solitons in three-band superconductors with broken time reversal symmetry. arXiv:1107.0995 [S]. https://arxiv.org/abs/1107.0995
- Gbur G.: Nonradiating Sources and the Inverse Source Problem (Dissertation) [S, nicht ladbar]. https://pages.charlotte.edu/greg-gbur/wp-content/uploads/sites/158/2012/11/thesis.pdf
- Lennon O. (2021): Q-balls with Multiple Charges and Cores. arXiv:2201.00024. https://arxiv.org/abs/2201.00024
- Marinica D. C., Borisov A. G., Shabanov S. V. (2008): Bound States in the Continuum in Photonics. PRL 100, 183902 [S]. https://www.researchgate.net/publication/51395082_Bound_States_in_the_Continuum_in_Photonics
- Marzuola J. L., Simpson G. (2010): Spectral Analysis for Matrix Hamiltonian Operators. arXiv:1003.2474. https://arxiv.org/abs/1003.2474
- Monticone F., Sounas D., Krasnok A., Alu A. (2019): Can a Nonradiating Mode Be Externally Excited? Nonscattering States versus Embedded Eigenstates. ACS Photonics 6, 3108 [S]. https://www.semanticscholar.org/paper/Can-a-Nonradiating-Mode-Be-Externally-Excited-Monticone-Sounas/47099c4d0fbf2942c8da5beb3098bee8b74abaf0
- Orignac E., De Palo S., Salasnich L., Citro R. (2024): Breathing mode of a quantum droplet in a quasi-one-dimensional dipolar Bose gas. arXiv:2401.03918. https://arxiv.org/abs/2401.03918
- Peng S.-Y., Zhang L.-F., Hu X. (2026): Three-component superconductivity: the effect of second-order Josephson couplings. arXiv:2605.28221. https://arxiv.org/abs/2605.28221
- Petrov D. S. (2015): Quantum Mechanical Stabilization of a Collapsing Bose-Bose Mixture. arXiv:1506.08419 (PRL 115, 155302 [L?]). https://arxiv.org/abs/1506.08419
- Prudencio F. R., Silveirinha M. G. (2021): Monopole Embedded Eigenstate in Nonlocal epsilon-Near Zero Nanostructures. arXiv:2111.00311. https://arxiv.org/abs/2111.00311
- Puthoff H. E. (2002): Polarizable-Vacuum (PV) Approach to General Relativity. Found. Phys. [S; Band 32, S. 927 L?]. https://link.springer.com/article/10.1023/A:1016011413407
- Rentzber N. (2026): Electromagnetic Radiation from a Neutralized Polarized Sphere with Two Conserved Currents for One Charge History. arXiv:2608.24171. https://arxiv.org/abs/2608.24171
- Richaud A., Penna V., Mayol R., Guilleumas M. (2020): Vortices with massive cores in a binary mixture of Bose-Einstein condensates. arXiv:1908.06668 (PRA 101, 013630 [S]). https://arxiv.org/abs/1908.06668
- Ritu, Rajat, Singh M., Gupta R. K., Gautam S. (2026): Spin and density excitations of one-dimensional self-bound Bose-Bose droplets. arXiv:2603.00987. https://arxiv.org/abs/2603.00987
- Segur H., Kruskal M. D. (1987): Nonexistence of small-amplitude breather solutions in phi^4 theory. PRL 58, 747 [S]. https://ui.adsabs.harvard.edu/abs/1987PhRvL..58..747S/abstract
- Smerzi A., Fantoni S., Giovanazzi S., Shenoy S. R. (1997): Quantum Coherent Atomic Tunneling between Two Trapped Bose-Einstein Condensates. cond-mat/9706221. https://arxiv.org/abs/cond-mat/9706221
- Son D. T., Stephanov M. A. [Autoren und PRA 65, 063621 L?] (2002): Domain walls of relative phase in two-component Bose-Einstein condensates. cond-mat/0103451 [S, Titel]. https://arxiv.org/abs/cond-mat/0103451
- Tylutki M., Astrakharchik G. E., Malomed B. A., Petrov D. S. (2020): Collective Excitations of a One-Dimensional Quantum Droplet. arXiv:2003.05803. https://arxiv.org/abs/2003.05803
- Tylutki M., Pitaevskii L. P., Recati A., Stringari S. (2016): Confinement and precession of vortex pairs in coherently coupled Bose-Einstein condensates. PRA 93, 043623; arXiv:1601.03695 [S]. https://arxiv.org/abs/1601.03695
- van Manen L. M., Blankenstein T., Mazumdar A. (2026): Gravitationally Induced Entanglement of Matter in Quadratic Curvature Gravity and Constraints on Ghost Mass. arXiv:2609.22501. https://arxiv.org/abs/2609.22501
- Ye X.-H. (2009): Polarizable vacuum analysis of the gravitational metric tensor. arXiv:0903.3665. https://arxiv.org/abs/0903.3665
- Yu X., Lu Y. Y. (2025): Existence of Friedrich-Wintgen bound states in the continuum: system of Schroedinger equations. arXiv:2504.19573. https://arxiv.org/abs/2504.19573
- Zhang N., Lu Y. Y. (2024): Perturbation theory for resonant states near a bound state in the continuum. arXiv:2408.08162. https://arxiv.org/abs/2408.08162
- Zhang X., Liu J., Xiao H., Chen X.-L., Zhang Y. (2026): Breathing mode of quantum droplets in dipolar quantum gases: A sum-rule analysis. arXiv:2606.29370. https://arxiv.org/abs/2606.29370
- Zhen B., Hsu C. W., Lu L., Stone A. D., Soljacic M. (2014): Topological Nature of Optical Bound States in the Continuum. PRL 113, 257401 [S]. https://link.aps.org/doi/10.1103/PhysRevLett.113.257401
- Zhu J., Li H. (2026): Parameterized Post-Newtonian Analysis of Quadratic Gravity and Solar System Constraints. arXiv:2601.05750. https://arxiv.org/abs/2601.05750
- Nur als Titel oder Suchtreffer [S]: arXiv:1306.2313, 1403.2132 (Dreiband-BTRS); 2112.14263, 1409.3232, 2101.06988
  (Mehrfeld-/charge-swapping Q-Baelle); 2306.00394 (kohaerent gekoppelte NLS); 1301.2923, 2405.10114 (isospinning);
  2609.32059 (Magnetic Q-balls); 2410.12317, 2111.02609, 1203.4896 (Skyrmionen/Vortonen im BEC); 2304.07255, 2407.17080
  (massive Wirbelkerne); 2502.09851 (Subradianz); 2010.15167 (Ketten-BIC); 2201.04578 (Riesenresonanzen);
  2512.05763, 2602.07762, 1605.02515 (liquid light); 2605.19913, 2512.23368, 2401.06589 (Polaritonen-Solitonen in BIC);
  2510.17789, 2512.24144 (Geister); Invent. Math. 2025, doi 10.1007/s00222-025-01327-y (kleine Breather); Found. Phys.,
  doi 10.1007/BF00708515 (keine strahlungsfreien Bewegungen relativistisch starrer Koerper); Nanotechnology 2019,
  doi 10.1088/1361-6528/ab02b0 (Anapole).

### 10 Einfach gesagt

Wir haben nachgeschaut, unter welchen Namen andere Forscher an denselben Dingen arbeiten. Fast jedes unserer Themen hat
schon einen Namen: Die "stillen Stellen" heissen in der Optik "gebundene Zustaende im Kontinuum", und unsere Regel, wann ein
Ball nicht strahlt, ist im Kern eine fast hundert Jahre alte Regel fuer schwingende Kugelschalen. Nicht gefunden haben wir
jemanden, der eine ganze Leiter solcher stillen Stellen bei einem Q-Ball oder einem Atomtroepfchen gezeigt hat. Fuer den
geplanten Labortest mit Troepfchen haben wir eine Warnung gefunden: Deren einfachste Atemschwingung liegt meist im falschen
Bereich, bessere Kandidaten sind die hoeheren Schwingungen.

## ABRUFPROTOKOLL (Erwartung vor jedem Abruf, Zeit per date)

### Block B1 (Erwartungen notiert zwischen 2026-09-30 07:55:40 CEST (date) und dem ersten Abruf um 07:56 (mtime der ersten API-Antwort); die zuerst hier stehende Zeit "07:57" war geschaetzt und ist berichtigt)

- B1.1 Suche "anapole" gegen "bound state in the continuum" / nonscattering gegen embedded eigenstate.
  Erwartung: Es gibt eine Arbeit (vermutlich Monticone, Sounas, Krasnok, Alu 2019), die ausdruecklich trennt: Anapol =
  angeregter, nicht streuender Zustand (Quelle mit verschwindender Fernfeldamplitude), kein Eigenzustand; BIC = Eigenzustand.
- B1.2 Suche "nonradiating source" Kugelschale kR = n pi (Schott, Bohm-Weinstein 1948, Goedecke 1964, Devaney-Wolf 1973).
  Erwartung: Die klassische Bedingung einer strahlungsfreien pulsierenden Kugelschale ist j0(kR) = 0, also kR = n pi, mit
  einer diskreten Leiter strahlungsfreier Frequenzen. Das waere die Born-/Quellen-Version unserer Phasenregel.
- B1.3 Suche Quantentroepfchen, Atmungsmode im Kontinuum, Selbstverdampfung, Breite gegen N.
  Erwartung: Petrov 2015 (Selbstverdampfung), Baillie/Wilson/Blakie 2017 (dipolar), 1D-Arbeiten (Tylutki u. a. 2020);
  eine Breite der Atmungsmode gegen N mit Nullstellen ist NICHT berichtet.
- B1.4 Suche BIC/eingebetteter Eigenwert bei Solitonen oder Troepfchen, letzte 24 Monate.
  Erwartung: nichts ueber die Vorarbeit hinaus (kein Q-Ball- oder Troepfchen-Pol mit Breite null).
- B1.5 Suche Fabry-Perot-BIC und Phasenbedingung (Marinica, Borisov, Shipman 2008).
  Erwartung: BIC zwischen zwei Resonatoren, wenn die Umlaufphase ein Vielfaches von 2 pi ist; Leiter in der Abstandsvariable.

### Block B1, Ausgang (eingetragen 2026-09-30 07:57:47 CEST, date; die zuerst hier stehende Zeit "07:59" war geschaetzt und ist berichtigt)

- B1.1 **bestaetigt** (eine Zeile): Monticone, Sounas, Krasnok, Alu 2019, ACS Photonics 6, 3108 [S] trennen "nonscattering
  states" (Anapol, kein Eigenmode, von aussen anregbar) von "embedded eigenstates"/BIC (Eigenmode, wegen Reziprozitaet von
  aussen nicht anregbar). Nebenfund [A]: Prudencio & Silveirinha, arXiv:2111.00311 (2021): "monopole-type" eingebettete
  Eigenzustaende in 3D-Kugeln (ENZ-Kern-Schale); bisher "only when the size of the resonator is delicately tuned".
- B1.2 **bestaetigt, aber groesser als erwartet** -> voller Zyklus, siehe V1 unten: Schott 1933 / Bohm & Weinstein 1948
  (Phys. Rev. 74, 1789) [S]: starre Ladungsschale strahlt nicht, wenn 2a = m c T, also k a = m pi. Dazu ganz frisch [A]:
  Rentzber, arXiv:2608.24171 (25.08.2026): Strahlung einer Kugel "proportional to j_2(kR)", "vanishes exactly at the
  positive roots of j_2"; nackte Kugel "silent at the roots of j_1". Die Kugelschalen-Leiter k R = Nullstellen von j_l ist
  also Lehrbuch plus aktuelle Literatur. Gegensweep-Nebenfund [S]: "Absence of radiationless motions of relativistically
  rigid classical electron" (Found. Phys., link.springer.com/article/10.1007/BF00708515).
- B1.3 **bestaetigt** (eine Zeile, noch ohne Volltext): Flynn, Parisi, Billam, Parker, arXiv:2209.04318 [A]: Atmungsmode
  unbalancierter Troepfchen emittiert Teilchen, "intricate superposition of multiple simultaneously decaying collective
  oscillations"; keine Nullstellen der Breite im Abstract. Petrov-Schwellen N ~ 94,2 und 933,7 (reskaliert) nur [S].
- B1.4 laeuft in B2 weiter (arXiv-API funktioniert per https; http liefert 0 Byte).
- B1.5 nicht abgerufen (verschoben nach Block B5, Kollektiv).

#### V1 (Erwartungsverstoss, voller Zyklus): Die Phasenregel hat einen 90 Jahre alten Namen

- Erwartung war: "Born-/Quellenversion unserer Phasenregel existiert als Nebenbemerkung".
- Befund: Sie ist ein eigenes, benanntes Forschungsthema mit Stammbaum: Schott 1933 (radiationless orbits) [S], Bohm & Weinstein
  1948 (Selbstschwingungen ohne Strahlung, als Teilchenmodell: Myon als angeregtes Elektron) [S], Goedecke 1964 ("classically
  radiationless motions") [S], Devaney & Wolf 1973 ("nonradiating sources") [L?], Gbur (Dissertation "Nonradiating sources and
  the inverse source problem") [S], Anapol-Literatur (Uebersicht Nanotechnology 2019, doi 10.1088/1361-6528/ab02b0) [S],
  Rentzber 2026 [A]. Suchwort: **nonradiating source / radiationless motion**. (Markierungen nachgetragen zwischen
  08:07:58 und 08:08:33 CEST, date davor und danach; vorher fehlten sie hier. Die zuerst eingetragene Zeit "08:09" war
  geschaetzt und ist berichtigt.)
- Unser Spielzeugmodell (delta-Schale, M = g V_c(R) sin(qR), Nullstellen bei qR = n pi; THEORIE-ATMUNGS-NULLSTELLEN.md
  Abschn. 4.1 Punkt 6) ist **woertlich Schotts Bedingung fuer eine Kugelschale im Kanal l = 0** [ES].
- Korrigierte Erwartung: Neu kann nur sein, (i) dass die Quelle nicht vorgegeben ist, sondern der geschlossene Kanal
  selbstkonsistent die Quelle bildet (Eigenmode statt angetriebene Quelle: BIC statt Anapol), (ii) die Verzerrung durch den
  Ball (theta ~ 0,83 statt 0) und (iii) die Haeufung ~1/n, weil der Radius selbst mit omega waechst.

### Block B2 (Erwartungen notiert 2026-09-30 07:58:19 CEST, vor den Abrufen)

- B2.1 arXiv-API: "quantum droplet" UND "breathing", neueste 40. Erwartung: mehrere Arbeiten 2024-2026 zu Atmungsmoden (1D,
  2D, dipolar, Falle); keine meldet eine an diskreten N verschwindende Emissionsbreite.
- B2.2 arXiv-API: "embedded eigenvalue(s)" UND (soliton | "computer-assisted" | "interval"). Erwartung: Mathematik zur
  Abwesenheit (NLS), eventuell Ayala u. a. 2026 [V]; kein Existenzbeweis fuer die Linearisierung eines Solitons.
- B2.3 Websuche "computer-assisted proof" existence "embedded eigenvalue" / "resonance" "interval arithmetic".
  Erwartung: nur Ayala 2026 [V] und Asad-Simpson 2011 [V]; eventuell rigorose Evans-Funktion (Barker, Zumbrun).
- B2.4 Websuche kubisch-quintische NLS, innere Moden flacher Solitonen, "liquid light". Erwartung: Pelinovsky, Kivshar,
  Afanasjev 1998 (innere Moden), Michinel u. a. 2006 (liquid light); keine BIC-Leiter.
- B2.5 arXiv-API: "bound state(s) in the continuum" UND (soliton | droplet | condensate | "nonlinear Schr"). Erwartung:
  photonische BIC mit Nichtlinearitaet und BEC im Gitter; keine Innenmoden-BIC eines selbstgebundenen Objekts.

### Block B2, Ausgang (eingetragen 2026-09-30 07:59:21 CEST)

- B2.1 **bestaetigt**: 30 Treffer 2020-2026 zu Troepfchen-Atmungsmoden (u. a. Orignac, De Palo, Salasnich, Citro,
  arXiv:2401.03918 [A]: 1D-dipolar, Atmungsfrequenz ~ 1/N, "stability of the quantum droplet against the particles emission"
  bei flachem Profil; Zhang u. a. arXiv:2606.29370 [A]: Summenregeln, nur Frequenzen). Keine Arbeit mit Emissionsbreite gegen N
  im Titel oder in den gelesenen Abstracts.
- B2.2 **bestaetigt, mit Gegensweep-Gewinn**: Kein Existenzbeweis eines eingebetteten Eigenwerts an einem Soliton. Dafuer drei
  Abwesenheitssaetze, einer davon neu fuer uns:
  - Marzuola & Simpson 2010, arXiv:1003.2474 [A]: "By a numerically assisted proof, we show that there are no embedded
    eigenvalues for the three dimensional cubic equation" (Matrix-Hamilton-Operatoren um NLS-Solitonen).
  - **Cui, Xia, Yang 2023, arXiv:2304.09708 [A]:** Linearisierung an Grundzustaenden eines *Systems von Klein-Gordon-
    Gleichungen*, radial: "no embedded eigenvalue in the essential spectrum". Das klingt wie unser Fall, ist es nach
    Abstract aber nicht: dort EINE Schwelle ('1', "bottom of the essential spectrum"), statische Grundzustaende; bei uns
    zwei Schwellen 1 - omega und 1 + omega (zeitperiodischer Ball, Hamilton-Matrix) [ES]. Volltext nicht gelesen.
  - Asad & Simpson 2011 [V] (u. a. 3D kubisch-quintische NLS, also unser nichtrelativistischer Grenzfall).
- B2.3 **bestaetigt**: Websuche findet rechnergestuetzte Beweise fuer Eigenwerte UNTER dem wesentlichen Spektrum
  (sciencedirect S0377042700004817 [S]) und fuer Abwesenheit (oben), keinen fuer Existenz IM Kontinuum ausser Ayala u. a.
  2026 [V] (Optik, Frequenzen ohne Antwort). Suchwoerter, die hier greifen: "computer-assisted proof", "validated
  numerics", "rigorous numerics", "numerically assisted proof", "interval arithmetic", "Newton-Kantorovich", "radii
  polynomial". [ES]
- B2.4 **bestaetigt**: "liquid light" / kubisch-quintisch ist aktiv (u. a. arXiv:2512.05763 "Double-flat-top half-vortices
  and self-bound solitary wave billiards", arXiv:2602.07762 "Phase-controlled ... coalescent collisions", arXiv:1605.02515
  "Coherent cavitation in the liquid of light") [S, nur Titel]; keine Innenmoden-BIC in Titeln oder Suchzusammenfassung.
- B2.5 **bestaetigt**: Treffer sind Polaritonen-Solitonen IN photonischen BIC-Strukturen (arXiv:2605.19913, 2512.23368,
  2401.06589) [S, Titel]: dort ist die BIC die lineare Mode der Struktur, nicht eine Innenmode eines selbstgebundenen
  Objekts. Name-Falle fuer Suchen: "soliton" + "BIC" liefert fast nur dieses Feld.

### Block B3 (Erwartungen notiert 2026-09-30 07:59:40 CEST, vor den Abrufen)

- B3.1 Websuche Dreiband-Supraleiter, frustrierte Josephson-Kopplung, Zeitumkehrbruch, Chiralitaet. Erwartung: bekannt
  (Stanev & Tesanovic 2010; Carlstroem, Garaud, Babaev 2011): bei gleicher abstossender Kopplung 120-Grad-Phasen, zwei
  entartete chirale Zustaende (Z2), "s + is"; das ist unser FA-1-Stern ohne Q-Ball-Huelle.
- B3.2 Websuche "vortex trimer" drei Komponenten, Einschluss von Bruchwirbeln durch Domaenenwaende (Son & Stephanov 2002;
  Kasamatsu, Tsubota, Ueda 2004; Eto & Nitta). Erwartung: bekannt, mit ausdruecklicher Quark-/Baryon-Analogie.
- B3.3 arXiv-API "Q-ball" UND (multicomponent | two-component | non-Abelian | SU(3) | "charge-swapping"). Erwartung: einige
  Arbeiten (Safian, Coleman, Axenides 1988 nicht in arXiv; Copeland, Saffin, Zhou 2014 "charge-swapping Q-balls"); keine
  zu Innenmoden-BIC im Mehrkomponentenball.
- B3.4 Websuche kohaerente Kopplung / Vierwellenmischterm in gekoppelten NLS (doppelbrechende Faser), Potential
  cos(2 Delta phi). Erwartung: Lehrbuch (Menyuk; Akhmediev & Ankiewicz); phasengekoppelte Vektorsolitonen.
- B3.5 Websuche rotierende Q-Baelle / Wirbel-Q-Baelle, Stabilitaet. Erwartung: Volkov & Woehnert 2002, Kleihaus, Kunz, List
  2005; J = n Q; neuere Stabilitaetsarbeiten 2023-2026.

### Block B3, Ausgang (eingetragen 2026-09-30 08:01:08 CEST)

- B3.1 **bestaetigt**: frustrierte Dreiband-Supraleiter, Chiralitaet +1/-1 (zyklische Ordnung der Phasen), 2 pi/3 im
  symmetrischen Fall: Garaud, Carlstroem, Babaev arXiv:1107.0995; arXiv:1306.2313; arXiv:1403.2132 [S, Titel/Suchtext].
  **Dazu Verstoss V2 (siehe unten):** Peng, Zhang, Hu, arXiv:2605.28221 (27.05.2026) [A].
- B3.2 **bestaetigt**: Eto & Nitta, "Vortex trimer in three-component Bose-Einstein condensates", PRA 85, 053645 (2012),
  arXiv:1201.0343 [S]: drei Bruchwirbel, durch Domaenenwaende der relativen Phasen gebunden, ausdrueckliche
  Quark-Einschluss-Analogie [S]. Zusaetzlich [A]: Chatterjee, Gudnason, Nitta, arXiv:1912.02685 (JHEP 04 (2020) 109):
  "higher-order generalization of the Josephson term"; "global vortices have angular domain walls".
- B3.3 **bestaetigt**: Mehrfeld-Q-Baelle existieren als Thema (Lennon arXiv:2201.00024 [A]: "a cored Q-ball", mehrere
  Stabilisierungssymmetrien; arXiv:2112.14263 Multi-Field Q-balls; Copeland, Saffin, Zhou arXiv:1409.3232 "Charge-Swapping
  Q-balls" und arXiv:2101.06988 Lebensdauern [Titel]). Keine Innenmoden-BIC im Mehrkomponentenball.
- B3.4 **bestaetigt**: "coherently coupled NLS" mit phasenabhaengigem Vierwellenmischterm (doppelbrechende Faser); Einteilung
  in "coherently coupled" und "incoherently coupled solitons" [S]. Der Paarterm g J_12 psi_1^2 psi_2^* ist dort Standard.
- B3.5 **bestaetigt, mit Treffer fuer SP-1**: Almumin, Heeck, Rajaraman, Verhaaren, arXiv:2302.11589 [A] "Slowly rotating
  Q-balls": "classically long-lived metastable rotating Q-balls with small angular momentum, even for large charge". Dazu
  DeVries, Vassallo, Verhaaren arXiv:2602.15196 [A] (Herleitung von J = n Q) und Brumelot & Medina arXiv:2602.07676 [A]
  (Existenz "spinning Q-vortex solitons").

#### V2 (Erwartungsverstoss, voller Zyklus): Drei Komponenten mit Paarterm cos(2 Delta theta) sind seit Mai 2026 durchgerechnet

- Erwartung war: Frustration nur mit gewoehnlicher Josephson-Kopplung cos(Delta theta) (Dreiband-Supraleiter).
- Befund [A]: Peng, Zhang, Hu, arXiv:2605.28221: dreikomponentiges Ginzburg-Landau-Modell mit "second-order Josephson-type
  couplings" (also cos(2 Delta theta), unser Paarterm), vollstaendiger Satz der Grundzustaende: "an 8-fold degenerate
  frustrated state and four 4-fold degenerate non-frustrated phase-locked states"; vier davon brechen die Zeitumkehr;
  "a Higgs-Leggett mode unique to the frustrated region, accompanied by mode softening near the phase boundaries".
- Bezug zu FA-1 [ES]: Der 120-Grad-Stern mit zwei Drehsinnen ist in der homogenen Version dieses Problems der frustrierte,
  zeitumkehrbrechende Zustand. Neu bei uns bleibt: selbstgebundener Ball mit Kontinuum (Abstrahlung, Kreiselstabilitaet
  nahe der Kontinuumsschwelle), nicht der Phasenstern selbst. FA-1s Befund "instabil, wo die Mode negativer Energie die
  Kontinuumsschwelle kreuzt" ist das Gegenstueck zur dortigen "mode softening near the phase boundaries" (Hypothese, nicht
  geprueft).
- Korrigierte Erwartung: Fuer den inneren Phasenraum (FA-1, ROT-2, ROT-3) ist die Mehrband-Supraleiter- und
  Mehrkomponenten-BEC-Literatur der Hauptvorlaeufer. Suchwoerter: "second-order Josephson coupling", "frustrated
  multicomponent", "BTRS", "Leggett mode", "chirality".

### Block B4 (Erwartungen notiert 2026-09-30 08:01:08 CEST, vor den Abrufen)

- B4.1 Websuche Son & Stephanov, Domaenenwand der relativen Phase, Einschluss von Wirbelpaaren, Experimente 2024-2026.
  Erwartung: Theorie bekannt (Son & Stephanov 2002; Kasamatsu, Tsubota, Ueda 2004; Tylutki u. a. 2016); eine direkte
  Beobachtung des Einschlusses vermute ich (maessig sicher) noch nicht.
- B4.2 Websuche Wirbel mit gefuelltem Kern / coreless vortex, zweikomponentig, auch fuer Q-Baelle. Erwartung: BEC-Klassiker
  (Matthews u. a. 1999, JILA; coreless vortex im Spinor-BEC 2003); fuer Q-Baelle vermutlich nur "twisted"/"cored" Varianten.
- B4.3 Websuche "Q-Hopfion" / isospinning Hopf solitons. Erwartung: "isospinning Hopf solitons" (Battye & Haberichter 2013)
  und "Q-lumps" (Leese 1991) existieren; der Name "Q-Hopfion" eher nicht.
- B4.4 Websuche Zwei-Resonator-BIC / Subradianz zweier Strahler in 3D. Erwartung: Fabry-Perot-BIC bekannt; zwei
  Punktstrahler in 3D werden nie ganz dunkel (Gamma_- = Gamma (1 - sin kd / kd)).
- B4.5 Websuche Riesen-Monopolresonanz, escape width, Kontinuums-RPA. Erwartung: bekannt; keine Nullstellen der escape width.

### Block B4, Ausgang (eingetragen 2026-09-30 08:01:54 CEST)

- B4.1 **bestaetigt**: Son & Stephanov, cond-mat/0103451 (PRA 65, 063621, 2002) "Domain walls of relative phase in
  two-component Bose-Einstein condensates" [S]; Tylutki, Pitaevskii, Recati, Stringari, arXiv:1601.03695 (PRA 93, 043623,
  2016) [S]: Wirbelpaar durch Wand gebunden; bei staerkerer Rabi-Kopplung zerfaellt die Wand in Stuecke mit neuen
  Wirbelpaaren, "analogous to quark confinement and string breaking" [S-Zusammenfassung]. Eine Beobachtung im Experiment habe
  ich in diesem Durchgang nicht gefunden (nur eine Suche; kein Urteil).
- B4.2 nicht abgerufen (in B5 verschoben).
- B4.3 **bestaetigt**: Der Literaturname ist "isospinning hopfions" (arXiv:1301.2923) bzw. "isospinning CP^2 solitons"
  (arXiv:2405.10114); die Familie heisst Q-kinks, Q-lumps [S]. Frisch: "Magnetic Q-balls", arXiv:2609.32059 (25.09.2026)
  [Titel]. "Q-Hopfion" ist kein gebraeuchlicher Suchbegriff.
- B4.4 **bestaetigt**: Subradianz-Literatur: in 3D und bei endlichem Abstand kein vollkommen dunkler Zustand; Anteil
  sin(kR)/(kR) in der kollektiven Rate [S]. Vollkommen dunkel nur in 1D-Wellenleitern (Abstand n lambda/2) oder in
  periodischen Ketten (siehe B5).
- B4.5 **bestaetigt**: GMR = "breathing mode"; Breite = "escape width" (Kontinuums-RPA) plus "spreading width" [S,
  arXiv:2201.04578 "Theoretical Methods for Giant Resonances"]. Keine Nullstellen der escape width gesehen.

### Block B5 (Erwartungen notiert 2026-09-30 08:01:54 CEST, vor den Abrufen)

- B5.1 Websuche BIC in Ketten/Gittern dielektrischer Kugeln (Bulgakov & Sadreev; Bulgakov & Maksimov 2017) und
  Unmoeglichkeit echter BIC in endlichen 3D-Objekten (Rellich; Silveirinha 2014; Monticone & Alu 2014). Erwartung: beides
  bekannt: unendliche periodische Ketten ja, endliche kompakte Objekte aus gewoehnlichem Material nein.
- B5.2 Websuche quadratische Gravitation, zwei Yukawa-Terme (-4/3, +1/3), Torsionswaagen-Grenzen, 2024-2026. Erwartung:
  Grenzen auf die Spin-2-Masse aus Eoet-Wash (Groessenordnung meV), eventuell eine neue Arbeit mit beiden Termen zugleich.
- B5.3 Websuche Gravitation als Brechungsindex / polarisierbares Vakuum (Dicke 1957, Puthoff 2002), Kritik und
  Frame-Dragging. Erwartung: PV-Modell reproduziert 1PN, Kritik an Starkfeld/Rotation/Gravitationswellen; Mitfuehrung ueber
  Gordon-Metrik bewegter Medien.
- B5.4 Websuche Wirbel mit gefuelltem Kern, zweikomponentig (BEC, Q-Ball). Erwartung: Matthews u. a. 1999; "coreless
  vortex"; fuer Q-Baelle wenige Treffer.
- B5.5 arXiv-API "self-evaporation" (Troepfchen). Erwartung: Petrov 2015 und eine Handvoll Folgearbeiten; keine
  Nullstellen der Verdampfungsrate gegen N.

### Block B5, Ausgang (eingetragen 2026-09-30 08:03:41 CEST)

- B5.1 **bestaetigt**: BIC in periodischen Ketten dielektrischer Kugeln (Bulgakov & Sadreev; arXiv:1805.08036 "Optical
  response induced by bound states in the continuum in arrays of dielectric spheres"; arXiv:2010.15167 "Observation of an
  accidental bound state in the continuum in a chain of dielectric disks") [S, Titel]. Nichtexistenzsatz fuer kompakte
  endliche Strukturen mit gewoehnlichem Material (Ausnahmen epsilon = 0, +-unendlich) [S, Hsu u. a. 2016 via Suche; [V] fuer
  den Review selbst].
- B5.2 **bestaetigt**: Stelle-Potential 1 - 4/3 e^{-m2 r} + 1/3 e^{-m0 r} ist Standard; Torsionswaagen geben eine
  Spin-2-Masse ueber ~4 meV [S-Zusammenfassung, Quelle unklar]. Neu im Suchfenster [Titel]: arXiv:2601.05750 (PPN-Analyse
  quadratischer Gravitation, Sonnensystem), arXiv:2609.22501 (gravitativ erzeugte Verschraenkung, Grenzen auf die
  Geistmasse), arXiv:2510.17789 (Geister und Gravitationswellen), arXiv:2512.24144 (Spin-2, Lee-Wick-Geister, GUP).
  927) bzw. Brechungsindex-/"pseudo-metric"-Gravitation; im schwachen Feld wie ART; "gravitational radiation and
  frame-dragging effects were not addressed in early formulations confined to ... static sources" [S, Wikipedia-Zusammenfassung].
- B5.4 **teilweise**: Suche lieferte Skyrmionen und Vortonen im Zwei-Komponenten-BEC (arXiv:2410.12317, 2111.02609,
  1203.4896: "vortex loops ... with one component trapped inside their cores") [S]. Fuer Q-Baelle nur Lennon "cored
  Q-ball" (B3.3). Nachsuche mit Witten-Strings und "massive cores" in B6.
- B5.5 **bestaetigt, aber mit Regime-Befund** -> V3 unten. Petrov 2015 (arXiv:1506.08419) [A], Fort & Modugno 2020
  (arXiv:2012.10347) [A, Abstract], Tylutki, Astrakharchik, Malomed, Petrov 2020 (arXiv:2003.05803) [A], Ritu u. a. 2026
  (arXiv:2603.00987) [A]: keine Nullstellen der Emissionsbreite.

#### V3 (Erwartungsverstoss, voller Zyklus): Bei Troepfchen liegt die Atmungsmode im falschen Regime fuer eine Leiter

- Erwartung war: Troepfchen sind das direkte Laborgegenstueck; ihre Atmungsmode liegt fuer kleine N im Kontinuum, die
  Leiter muesste zur flachen (duennwandigen) Seite hin auftreten.
- Befund 1D [A]: Tylutki u. a. 2020: "A notable exception is the breathing mode which we find to be always bound." Die
  anderen Moden sind "plane-wave Bogoliubov phonons ... reflected by edges of the droplet" und kreuzen mit sinkendem gamma
  "sequentially" die Emissionsschwelle. In 1D gibt es also keine eingebettete Atmungsmode.
- Befund 3D [A]: Petrov 2015, S. 3: "All excitation modes cross the threshold for sufficiently small N. Only the monopole
  mode reenters at N ~ 20.1"; "in the interval 20.1 < N < 94.2 there are no modes below -mu". Oberhalb faellt der Monopol
  bei N ~ 934 unter die Schwelle (Zahl nur [S], nicht in Petrovs Text gefunden).
- **Schluss [ES]:** Die Atmungsmode ist nur im dickwandigen Fenster (N ~ 20 bis ~ 934) eingebettet, und an BEIDEN Raendern
  des Fensters geht die offene Wellenzahl q gegen null (unten weicher Monopol, oben Schwellendurchgang). Die Phase q R, die
  bei uns die Leiter erzeugt, bleibt dort klein. Beim Q-Ball dagegen bleibt q ~ 2,4 (relativistische Mode, Re rho ~ 1,6 bis
  1,7) und R waechst ~ 1/epsilon. **Fuer MESS-1 ist die unterste Atmungsmode deshalb ein schwacher Kandidat (0 oder 1
  Nullstelle zu erwarten); die hoeheren radialen Obertoene (stehende Schallwellen im flachen Kern, Tylutkis "phonons
  reflected by edges") sind die bessere Stelle fuer eine Leiter.** Hypothese, nicht gerechnet.
- Korrigierte Erwartung: Die Uebertragung auf Troepfchen braucht den Obertonsektor und die Abhaengigkeit von N, nicht die
  Grundatmung.

### Block B6 (Erwartungen notiert 2026-09-30 08:03:41 CEST, vor den Abrufen)

- B6.1 arXiv-API Abstracts 2601.05750, 2609.22501, 0903.3665 (Stelle-PPN, Geistmasse, PV-Metrik). Erwartung: PPN-Arbeit
  findet gamma = 1 plus Yukawa-Korrekturen; Geistmassen-Grenzen im meV-Bereich; PV-Arbeit: exponentielle Metrik, 1PN gleich.
- B6.2 Websuche Nichtexistenz von Breathern (Segur & Kruskal 1987), Persistenz nichtlinearer BIC. Erwartung: Breather zerfallen
  ueber die zweite/dritte Harmonische jenseits aller Ordnungen (exponentiell klein); "nonlinear BIC" in Photonik existiert nur,
  wenn Harmonische unter der Lichtlinie liegen.
- B6.3 Websuche Wirbel mit massivem Kern / Witten-supraleitende Strings (Kondensat im Kern). Erwartung: Richaud u. a. 2020
  (massive cores) und Witten 1985 als Namen fuer ROT-1.
- B6.4 Websuche Fabry-Perot-BIC, zwei Resonatoren, Abstand (nachgeholt B1.5). Erwartung: Marinica, Borisov, Shipman 2008.
- B6.5 Websuche topologische Ladung von BIC (Zhen u. a. 2014), abwechselnde Vorzeichen. Erwartung: bekannt, BIC = Wirbel
  des Fernfeldvektors mit ganzzahliger Ladung.

### Block B6, Ausgang (eingetragen 2026-09-30 08:05:35 CEST)

- B6.1 **bestaetigt**: Zhu & Li, arXiv:2601.05750 [A]: quadratische Gravitation bis 2PN, "gamma(r) = 1 when m_R = m_W",
  "to ensure that gravity remains attractive, we have m_W > m_R/4", Sonnensystem nur m >~ 23 AU^-1. Van Manen, Blankenstein,
  Mazumdar, arXiv:2609.22501 (18.09.2026) [A]: Stelle-Gravitation in gravitativ erzeugter Verschraenkung, "m_0 < 4^(1/3) m_2"
  aus stabiler Oszillatorbeschreibung; "spin modes as low as 0.0197 eV become distinguishable ... at d ~ 40 um". Bezug
  ST-1 [ES]: Das Tal lambda0/lambda2 ~ 1,63 bis 1,70 heisst m_0/m_2 ~ 0,6, vereinbar mit beiden Bedingungen. Ye 2009,
  arXiv:0903.3665 [A]: PV-Deutung der Metrik als "variable dielectric tensor of vacuum".
- B6.2 **bestaetigt**: Segur & Kruskal 1987, PRL 58, 747 [S]: keine echten kleinen Breather in phi^4, Abstrahlung "beyond all
  orders"; rigorose Neufassung ueber exponentiell kleine homokline Aufspaltung, Invent. Math. 2025,
  doi 10.1007/s00222-025-01327-y [S]. Unser Fall ist das andere Regime: Zerfall algebraisch ueber die zweite Harmonische
  (nichtlineare goldene Regel), nicht jenseits aller Ordnungen [ES, gestuetzt auf [V] Soffer-Weinstein, Cuccagna-Maeda].
- B6.3 **bestaetigt**: Richaud u. a., "Vortices with massive cores in a binary mixture of Bose-Einstein condensates",
  arXiv:1908.06668 (PRA 101, 013630, 2020) [S]; Folgearbeiten arXiv:2304.07255, arXiv:2407.17080 ("Massive-vortex
  realization of a Bosonic Josephson Junction", PRR 6, 043197, 2024) [S]; Witten 1985 "superconducting cosmic strings" (Feld
  kondensiert im Kern) [S]. ROT-1 laeuft unter diesen Namen.
- B6.4 **bestaetigt mit Namensfehler in meiner Erwartung**: Die Fabry-Perot-BIC-Arbeit ist Marinica, Borisov, **Shabanov**
  2008, PRL 100, 183902 [S], nicht "Shipman". Dazu **Verstoss V4** (unten): Yu & Lu 2025.
- B6.5 **bestaetigt**: Zhen, Hsu, Lu, Stone, Soljacic 2014, PRL 113, 257401 [S]: BIC sind Wirbelzentren der
  Fernfeldpolarisation mit erhaltener, quantisierter Ladung. Unser Umlauftest (+-1) ist das Gegenstueck im Parameterraum
  (rho, omega^2) [ES].
- Zusatz: Battye & Sutcliffe 2000, hep-th/0003252 [A, Abstract]: Q-Ball-Dynamik in 1 bis 3 Dimensionen, "charge transfer and
  Q-ball fission"; Q/Anti-Q-Vernichtung steht nicht im Abstract (Chem-14-Vermerk [L?] bleibt offen).

#### V4 (Erwartungsverstoss, voller Zyklus): Existenzbeweise fuer nicht symmetriegeschuetzte BIC in Schroedinger-Systemen gibt es seit 2025

- Erwartung war: Existenzbeweise gibt es nur fuer symmetriegeschuetzte BIC und (seit 19.09.2026) rechnergestuetzt fuer die
  Optik (Ayala u. a. [V]).
- Befund [A]: Yu & Lu, arXiv:2504.19573 (28.04.2025): "we give a rigorous justification for the existence of BICs in the
  original system of three 1D Schroedinger equations" (Friedrich-Wintgen-Modell 1985). Sie schreiben auch: "The existence of
  BICs ... has only been established for some relatively simple cases such as BICs protected by symmetry."
- Bezug zu BEWEIS-1 [ES]: Das ist der naechste mathematische Nachbar: gekoppelte Schroedinger-Kanaele, ein offener Kanal,
  akzidentelle BIC, strenger Existenzbeweis. BEWEIS-1 unterscheidet sich durch (i) rechnergestuetzt statt analytisch,
  (ii) radial 3D statt 1D, (iii) Hamilton-Matrix (nicht selbstadjungiert, zwei Schwellen) aus der Linearisierung eines
  Solitons, (iv) Einzelresonanz statt zwei interferierender Resonanzen. Pflichtzitat fuer jede Beweis-Mitteilung.
- Korrigierte Erwartung: Die Gruppe Ya Yan Lu (City University Hong Kong) ist fuer BEWEIS-1 der erste Ansprechpartner
  in der Mathematik der BIC (auch Zhang & Lu, arXiv:2408.08162: Stoerungstheorie nahe einer BIC, "super-BICs").

### Block B7, Gegensweep und Restluecken (Erwartungen notiert 2026-09-30 08:05:35 CEST, vor den Abrufen)

- B7.1 arXiv-API "internal mode" UND continuum UND (soliton | oscillon | kink | Q-ball), neueste. Erwartung: nichts, was eine
  lineare Breiten-Nullstelle an einer Innenmode meldet (nach R7-Stand), eventuell Folgearbeiten zu Inagaki-Murakami.
- B7.2 Websuche Q-Ball/Anti-Q-Ball-Stoss, Vernichtung. Erwartung: Vernichtung zu Strahlung bzw. Oszillonen ist beschrieben
  (Axenides u. a. 2000 oder Battye & Sutcliffe 2000 im Volltext).
- B7.3 Websuche Kato-Satz / Froese-Herbst: keine Eigenwerte oberhalb aller Schwellen. Erwartung: bekannt; eingebettete
  Eigenwerte zwischen Schwellen (Mehrkanal) erlaubt.
- B7.4 Websuche bosonischer Josephson-Kontakt, laufende Phase, "macroscopic quantum self-trapping", innerer Josephson-Effekt
  (fuer ROT-2). Erwartung: Smerzi u. a. 1997, Albiez u. a. 2005, Zibold u. a. 2010.
- B7.5 Websuche Fakeonen/Lee-Wick: Laborsignaturen 2024-2026. Erwartung: nur Streuung/Kosmologie; im Labor unerreichbar
  (bestaetigt ST-2).
- B7.6 Websuche rigorose Evans-Funktion / validated numerics fuer Eigenwertprobleme auf der Halbachse (Jost). Erwartung:
  Barker & Zumbrun (numerischer Stabilitaetsbeweis), keine eingebetteten Eigenwerte.

### Block B7, Ausgang (eingetragen 2026-09-30 08:06:29 CEST)

- **Werkzeuggrenze:** Um 08:05 meldete die Websuche "used its web search budget (200 of 200)". B7.2 bis B7.6 sind deshalb
  NICHT gesucht. Ich suche danach nicht ueber Umwege weiter (keine neuen Stichwortabfragen), sondern lese nur noch schon
  bekannte Quellen per Kennung nach (arXiv id_list, WebFetch einer bekannten URL). Die offenen Punkte stehen als [L?] im
  Abschnitt "Offene Fragen".
- B7.1 **bestaetigt** (Abfrage lief vor der Grenze): In den letzten 24 Monaten nur Inagaki & Murakami arXiv:2609.15056 [V]
  und Bizon & Romanczukiewicz arXiv:2603.18605 [V] zu Innenmoden im Kontinuum; nichts Neues seit R7.
- B7.2 bis B7.6: nicht abgerufen (Grenze). Siehe [L?]-Pruefung per Kennung unten (B8).

### Block B8, Nachlesen per Kennung (Erwartungen notiert vor dem Abruf)

- B8.1 arXiv id_list mit aus dem Gedaechtnis vermuteten Kennungen: hep-ph/9910388 (Axenides u. a., Q-Ball-Dynamik),
  1908.02416 (Donoghue & Menezes, instabile Geister), 1703.04584 (Anselmi, Fakeonen), cond-mat/9706221 (Smerzi u. a.,
  Josephson/MQST), 1008.3057 (Zibold u. a., Rabi-Josephson). Erwartung: mindestens eine Kennung ist falsch; die richtigen
  bestaetigen die [L?]-Angaben.
- B8.2 WebFetch Gbur-Dissertation (bekannte URL aus B1.2) zu Schott / Bohm-Weinstein / kR = n pi (Gegensweep G1).
  Erwartung: Schott 1933 und Bohm-Weinstein 1948 werden als erste Beispiele nichtstrahlender Quellen genannt, mit einer
  Bedingung der Form 2a = m c T (also ka = m pi).

### Block B8, Ausgang (eingetragen 2026-09-30 08:08:33 CEST; die B8-Erwartungen wurden mit dem B7-Ausgang um 08:06:29 CEST geschrieben, vor den Abrufen)

- B8.1 **teilweise bestaetigt**: vier von fuenf Kennungen stimmen [A]:
  - hep-ph/9910388: Axenides, Komineas, Perivolaropoulos, Floratos, "Dynamics of Nontopological Solitons - Q Balls": zwei
    Q-Baelle zeigen "breather type oscillations with frequency equal to the difference of the internal qball frequencies";
    Streuung um 90 Grad. Q/Anti-Q-Vernichtung nicht im Abstract.
  - 1908.02416: Donoghue & Menezes, "Unitarity, stability and loops of unstable ghosts": der Geist ist eine instabile
    Resonanz, "does not appear in the asymptotic spectrum".
  - 1703.04584: Anselmi & Piva, "A new formulation of Lee-Wick quantum field theory" (nichtanalytische Wick-Rotation; die
    Fakeon-Idee baut darauf auf; das Wort "fakeon" steht nicht im Abstract).
  - cond-mat/9706221: Smerzi, Fantoni, Giovanazzi, Shenoy, Josephson-Tunneln zwischen zwei BEC: "ac Josephson effect and
    plasma oscillations" plus "macroscopic quantum self-trapping".
  - 1008.3057 (Zibold u. a.): keine Antwort unter dieser Kennung; Angabe bleibt [L?].
  - Nachgelesen ausserdem [A]: Bulgakov & Maksimov arXiv:1805.08036 (BIC in Kugelketten, Fano-Merkmale nahe der BIC);
    Richaud, Penna, Mayol, Guilleumas arXiv:1908.06668 ("vortices in one species host the atoms of the other species, which
    thus play the role of massive cores"); **Enqvist & Laine cond-mat/0304355: "perfect formal analogy" zwischen Q-Baellen
    und Solitonen in BEC mit anziehender Wechselwirkung** (Laborbezug fuer Thema 7, 2003).
- B8.2 **nicht moeglich**: WebFetch und curl scheitern am TLS-Zertifikat der Gbur-Seite ("unable to verify the first
  certificate", curl exit 60). Ich umgehe die Zertifikatspruefung nicht. Schott / Bohm-Weinstein bleiben [S]; die
  Bessel-Nullstellen-Leiter selbst ist durch Rentzber 2026 [A] belegt.


### Abschluss

- Verfahrensvermerk: Drei Zeitangaben waren zuerst geschaetzt (B1-Kopf "07:57", B1-Ausgang "07:59", V1-Nachtrag "08:09"); alle drei sind in der Datei berichtigt und als berichtigt markiert. Kein python, kein awk; Werkzeuge: curl (arXiv-API), sed, grep, tr, pdftotext (Petrov-PDF), Websuche bis zur Grenze.
- Ende: 2026-09-30 08:14:45 CEST (date, nach dem letzten Schreiben gemessen).
