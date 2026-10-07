# ARBEITSFELD DUNKEL-ZEIT (Runde 22) – feldforscher

- Einzige Arbeitsdatei dieser Karte (Feldregel 5). Vor jedem Schritt neu lesen. Gestrichenes bleibt mit ~~ ~~ stehen.
- Agentenstart 2026-10-02 20:37:37 CEST (date). Strategie geschrieben 2026-10-02 20:40:52 CEST (date), vor dem ersten Abruf.
- Zeitbox 90 min, also bis etwa 22:07 CEST (gerechnet aus dem Start, nicht geschaetzt).
- Marken: [S] gelesen, [L?] nur Abstract/Zitat, [H] eigene Schlussfolgerung, [E] Kopfrechnung.

## 0. Gelesene Projektquellen (lokal, nur zur Einordnung)

- KARTE.md (ganz, mit Nachtrag Frage 7)
- RUNDE-22/stelle-24m/ERGEBNIS.md: Lee 2020, |alpha| = 1 bei lambda < 38,6 um (95 %); |alpha| = 4/3 bei ~35-37 um,
  |alpha| = 1/3 bei ~55-58 um (Augenmass an Fig. 5); Venugopalan 2024/26 alpha ~ 1e6-1e7 bei 5-100 um; Murata 2026
  Uebersicht. Vorzeichen-Vorbehalt: Lee zeigt nur |alpha|.
- RUNDE-22.md: Codex-Uhr (stille Atmung = Dichte-Uhr, Periode 2 pi/rho = 3,6015; schwache Auslesung stoert nicht,
  starke resonante zerstoert die Regelmaessigkeit; keine Synchronisationsaussage); BILDUNG-1/2 (kleine Klumpen werden
  schnell Q-Baelle; grosse behalten Atmung; Verschmelzen behaelt Formschwingung; Bad stoesst Baelle an, v ~ 0,021).
- RUNDE-17.md, Stand Gesamtformel 02.10.: stille Atmung ist Uhr; Zweifeld psi/chi baut Huelle; Beutelgesetz E ~ Q^(3/4)
  ausgeschlossen.
- ZWEI-SEITEN v2.3: Leitidee Geometrie -> Feld -> Schnitte -> Moden -> (effektive Zeit); Ticks = Ereignisse der
  Kodimension 1; [H] d tau ~ nu_Delta dt; Grenze: aeussere Zeit t vorausgesetzt, Entstehung von Raumzeit nicht zeigbar.
  Abstract) [A dort]; m = hbar/(R c); Uhr = Umlauf mit c, geht im Feld langsamer (B.9).

## 1. Suchstrategie (vor dem ersten Abruf)

Kanaele: arXiv-API (export.arxiv.org/api/query), OpenAlex, Semantic Scholar (fiel bei STELLE-24M mit 429 aus; nur
als Ausweich), Volltexte arxiv.org/abs, /pdf, /html. WebSearch ist erschoepft.

Reihenfolge nach Gewicht fuer die Erwartungen:

| Block | Frage | Ziel | Abfragen (geplant) |
|---|---|---|---|
| A | 2 / D1 | Primaerquelle Montero/Vafa/Valenzuela 2022 (arXiv:2205.12293): Groesse R, Yukawa alpha, lambda, Bezug Dunkle Energie/Materie; Volltext | all:"dark dimension" AND all:Vafa; abs/2205.12293; Volltext-Stellen zu "inverse square", "Yukawa", "micron" |
| A' | 2 / D1 Gegensweep | neuere Schranken gegen die Dark Dimension (Neutronensterne, Supernova, Roentgen/Gamma fuer dunkle Gravitonen, Kosmologie, Kurzabstand), Uebersichten 2024-2026 | all:"dark dimension" AND (all:constraint OR all:bound OR all:neutron); sortiert nach Datum; Review "dark dimension" |
| B | 4 / D3 | Uebersicht ultraleichte Skalar-DM + Uhren; juengste Schranken (2024-2026) | all:"ultralight dark matter" AND all:"atomic clock"; all:"scalar dark matter" AND all:clock AND all:review |
| B' | 4 Gegensweep | universelle Kopplung: sehen Uhrvergleiche sie ueberhaupt? Pulsar-Timing (Khmelnitsky/Rubakov 2014) | all:"pulsar timing" AND all:"ultralight scalar"; all:universal AND all:coupling AND all:clock |
| C | 3 / D2 | Page/Wootters 1983, Moreva 2014 (Labor), Hoehn/Smith/Lock 2021, Quanten-Zeitdilatation (Smith/Ahmadi 2020), Connes/Rovelli 1994, Barbour; Uebersichten 2024-26; Pruefbarkeit | all:"Page-Wootters"; all:"quantum time dilation"; all:"thermal time hypothesis"; all:Barbour AND all:time |
| D | 1 / D4 | KK-Lesart der Q-Ball-Phase: Arbeiten zu Q-Baellen und Zusatzdimension; KK-Ladung = Impuls; Weak-Gravity-/No-global-symmetry-Bezug | all:"Q-ball" AND all:"Kaluza-Klein"; all:"Q-balls" AND all:"extra dimension"; all:"weak gravity conjecture" AND all:"Q-ball"; all:"global symmetries" AND all:"quantum gravity" |
| E | 5 | MIT-Beutel (Chodos 1974), Friedberg-Lee 1977, Casimir (Jaffe 2005), entropische Kraefte/Verlinde und Tests, CDT-Kosmokonstante nur kurz (Nachbarkarte!) | Metadaten per arXiv/OpenAlex; all:"emergent gravity" AND all:Verlinde AND all:test |
| F | 6 | Q-Ball-Wechselwirkung abhaengig von Phasendifferenz (Battye/Sutcliffe 2000, Axenides 2000, Bowcock/Foster/Sutcliffe 2009), Ladungstausch (Copeland/Saffin/Zhou 2014), Synchronisation von Solitonen | all:"Q-balls" AND all:phase AND all:interaction; all:"charge-swapping" |
| G | 7 | Van Raamsdonk 2010; Strings: Endpunkte mit c, Graviton im Spektrum; vDVZ; GW-Polarisationen (Eardley 1973; LIGO-Tests) | all:"building up spacetime" AND all:entanglement; all:"van Dam" OR vDVZ; all:"polarization" AND all:"gravitational waves" AND all:test |

Abgrenzung: Kein Ausbau zu CDT/Kausalmengen (Nachbarkarte GEOMETRIE-STAND). Zu Frage 5 nur ein Satz zur
Kosmokonstante in CDT mit einer Fundstelle.

## 2. Meine Vorab-Bilder (aus Gedaechtnis, ungeprueft, damit Verstoesse sichtbar werden)

- V-A (D1): MVV 2022 verbinden Lambda ~ 1e-122 mit der Abstandsvermutung; Turm leichter Zustaende m ~ Lambda^(1/4)
  /lambda; einzig konsistent: eine Zusatzdimension, R ~ 1-10 um, 5D-Planck-Skala ~ 1e9-1e10 GeV. Dunkle Materie:
  KK-Gravitonen ("dunkle Gravitonen", 2209.09249) oder primordiale Schwarze Loecher (2206.07071). Yukawa-Staerke fuer
  einen Kreis: alpha = 8/3 (massive KK-Gravitonen mit vDVZ-Faktor 4/3, je zwei Moden n = +-1), Reichweite = R.
  Erwartung: Das Papier nennt als Laborschranke ~30 um (aus Lee 2020), nicht 38,6 um.
- V-B (D3): Uhrschranken auf lineare Photonkopplung d_e erreichen 1e-4 bis 1e-6 (Gravitationsstaerke = 1) bei
  m ~ 1e-22 bis 1e-16 eV; Aequivalenzprinzip-Tests (MICROSCOPE) sind fuer lineare Kopplung oft staerker, Uhren fuer
  quadratische Kopplung konkurrenzfaehig.
- V-B' (Gegensweep-Kandidat): Ein universell an alle Materie gekoppeltes Feld aendert keine dimensionslosen Verhaeltnisse,
  Uhrvergleiche waeren dafuer blind. Sichtbar nur ueber Gravitation (Pulsar-Timing, oszillierendes Potential).
- V-C (D2): Moreva u. a. 2014 zeigen Page-Wootters mit verschraenkten Photonen; Theorie ohne Raumzeit-Vorhersage; aber
  Quanten-Zeitdilatation (Smith/Ahmadi 2020) ist eine pruefbare Vorhersage fuer Uhren in Ueberlagerung.
- V-D (D4): Ein 5D-Feld auf dem Kreis mit Impuls n/R ergibt einen geladenen 4D-Mode; ein Q-Ball dieses Modes ist in 5D
  eine um den Kreis laufende Welle. Ernst genommen ist die U(1) dann geeicht (Graviphoton), mit Radion -> neue
  Elemente, also Modellaenderung statt Vorhersage. Literatur direkt zu "KK-Q-Ball" erwarte ich duenn.

## 3. Abrufprotokoll (Erwartung vor jedem Abruf, dann Ausgang)

(wird fortgeschrieben)

## 4. Erwartungsverstoesse (getrennt gefuehrt)

(wird fortgeschrieben)

## 5. Gegensweep

(am Ende jeder Phase)

## 6. Offene Rueckfragen (wandern mit)

- R1: Was meint Finn mit "Seiten einer Dimension"? Lesart hier: die zwei Richtungen bzw. Innen/Aussen einer kompakten
  Zusatzdimension; alternativ "zwei Seiten des Feldes" aus RUNDE-16 (dort selbst offen). Nicht entscheidbar ohne Finn.

## 7. Gestrichenes

(noch nichts)

### Block A1 (Erwartung geschrieben 2026-10-02 20:41:45 CEST)
- A1a arXiv-API all:"dark dimension" AND all:Vafa (nach Datum): Erwartung: MVV 2205.12293 plus 10-30 Folgearbeiten
  (dunkle Gravitonen, PBH, Neutrinos, Kosmologie), juengste 2025/26.
- A1b arXiv abs 2205.12293: Erwartung: Abstract nennt "micron", Zusammenhang mit Lambda, Species-Skala 1e9-1e10 GeV.
- Ausgang A1 (eingetragen 2026-10-02 20:42:46 CEST):
  - A1b bestaetigt [S Abstract]: MVV, JHEP 2023, 22; "length l ~ Lambda^(-1/4) ~ 10^(-6) m"; Species-Skala = hoeherdim.
    Planck-Skala; Neutrino-Turm; Higgs-vev-Spekulation; GZK. Zahl 1e9-1e10 GeV steht nicht im Abstract (offen).
  - A1a **Verstoss** (73 Treffer, viele 2026): mindestens zwei Arbeiten vom 28.09. und 01.10.2026 melden laut
    WebFetch-Zusammenfassung Ausschluesse: Lee/Randall/Riojas 2609.36234 ("ruling out existing Dark Dimension models"?),
    Langhoff 2610.01825 (KK-Gravitonen als DM ausgeschlossen? Radius ~3 Groessenordnungen kleiner?). Dazu Hardy/
    Sokolov/Stubbs 2510.18975 (Sternkuehlung), Anchordoqui/Antoniadis/Luest 2501.11690 (zwei Mikrometer-Dimensionen),
    Reig/Ruiz 2510.25832 (Protonzerfall), Petretti 2411.03459 (CMB). Zusammenfassungen sind Paraphrase des Abrufmodells,
    NICHT Wortlaut -> Abstracts selbst lesen (Block A2). Erwartung "nicht widerlegt" wackelt; Moderator-Vermutung
    (Feldregel 1): Geometrie (R ~ um) gegen Kosmologie-Zusatz (dunkle Gravitonen als DM, Zerfallskaskade).

### Block A2 (Erwartung geschrieben 2026-10-02 20:42:46 CEST)
- A2a Abstracts 2609.36234 und 2610.01825: Erwartung: Beide treffen das Szenario "dunkle Gravitonen als DM" (Kaskade
  bzw. Zerfaelle), nicht die Existenz einer um-Dimension; Kurzabstands-Vorhersage unberuehrt.
- A2b Abstract 2510.18975: Erwartung: Fuer eine Dimension (n = 1) ist die Supernova-Schranke schwach; Hauptaussage fuer
  n = 2.
- A2c MVV-Volltext (Stellen "inverse", "Yukawa", "30", "micron", "lambda"): Erwartung: Laborschranke ~30 um aus Lee 2020;
  Bereich R ~ 1-10 um; alpha nicht ausgeschrieben.
- Ausgang A2 (eingetragen 2026-10-02 20:44:13 CEST):
  - A2c MVV-Volltext [S, quellen/MVV-2205.12293.txt, pdftotext]: l ~ lambda Lambda^(-1/4) ~ 1 um, lambda ~ 1e-1 bis
    1e-3 (Z. 67-68); Labor: "verified down to the scales around 30 um", daraus m >~ 6,6 meV (Gl. 3.2, Ref. [32] = Lee
    2020); Lambda^(1/4) = 2,31 meV bzw. Lambda^(-1/4) ~ 88 um; Neutronenstern-Heizung (Hannestad/Raffelt): eine Dimension
    l < 44 um, zwei Dimensionen l < 1,6e-4 um -> nur n = 1 bleibt; Casimir: lambda_Casimir = 5e-5, l ~ 7,42 um
    (Gl. 3.7); Bereich l ~ 0,1-10 um (Gl. 3.8); 5D-Planck ~ 1e9-1e10 GeV; Test: "factor of 10 - 100 improvement" der
    Torsionswaage. Yukawa-alpha nicht genannt. -> Erwartung im Kern bestaetigt; kleine Abweichung: Bereich reicht bis
    0,1 um (D1 sagt 1-10 um).
  - A2b Hardy/Sokolov/Stubbs [S Abstract]: "For 1 extra dimension, the bounds are weaker than those from laboratory
    searches." -> bestaetigt.
  - A2a teils bestaetigt, teils **Verstoss**: Langhoff 2610.01825 [S Abstract, Wortlaut]: intra-Turm-Zerfaelle nahe der
    Schwelle "pure d-wave", Gamma ~ p^5 statt p; "In a flat dark dimension this excludes KK gravitons as a dark matter
    candidate"; dazu Reheating-Schranke -> Radius "almost three orders of magnitude smaller" als R ~ Lambda^(-1/4).
    Das trifft nicht nur die DM-Lesart, sondern ueber Freeze-in auch R selbst (falls andere DM). Lee/Randall/Riojas
    2609.36234: nur Paraphrase des Abrufmodells [L?] (Unterdrueckung (q/m_n)^2, q^5-Rate, "constrains existing Dark
    Dimension theories"). Wortlaut noetig -> curl auf die API.

### Block A3 (Erwartung geschrieben 2026-10-02 20:44:13 CEST)
- A3a curl arXiv-API id_list=2609.36234,2610.01825,2501.11690: Erwartung: Lee/Randall/Riojas sagen woertlich, dass die
  DM-Kaskade der dunklen Gravitonen nicht schnell genug ist; keine Aussage zur Kurzabstandsgravitation. 2501.11690:
  zwei Dimensionen um-Groesse, gegen MVV-Argument (n >= 2 ausgeschlossen) -> eigene Spannung.
- A3b Langhoff-Volltext: Erwartung: R-Obergrenze bei ~0,1 um (lambda ~ 1e-3), abhaengig von Reheating-Temperatur und
  KK-Zahl-Verletzung; Annahme flache Dimension.
- Ausgang A3 (eingetragen 2026-10-02 20:45:12 CEST), alle [S] (API-Wortlaut quellen/api-A3a.xml; Langhoff-Volltext pdftotext):
  - Lee/Randall/Riojas 2609.36234 (28.09.2026): Zerfallsamplitude um (q/m_n)^2 unterdrueckt, Rate ~ q^5, universell
    "even with scalar-induced KK violation"; Wortlaut: "can be used to rule out existing Dark Dimension models, because
    the rapid cascade that was needed to evade constraints is severely suppressed". -> Erwartung (nur DM-Kaskade)
    bestaetigt im Kern.
  - **Verstoss (gross)**, Langhoff 2610.01825 (01.10.2026, 4 S., Einzelautor, unbegutachtet): "This excludes the
    existence of a flat dark dimension with R >~ 0.2 um (Fig. 1)"; unabhaengig von der DM-Frage: "any viable dark
    dimension ... R <~ 0.2 um, or m_KK >~ 1 eV". Annahmen: (annaehernd) flache Dimension, Freeze-in ueber Gl. (1),
    T_RH >= 5,96 MeV (BBN, CMB+BAO), MeV-Gamma-Schranken. Note Added: Ref. [20] = Lee/Randall/Riojas, unabhaengig.
    Abb. 1: graues Band = Torsionswaage "(for a brane at a fixed point)". Folge [H]: Ein Signal bei 1-10 um waere dann
    ausgeschlossen; Kurzabstandsgravitation koennte die verbleibende Dark Dimension (<= 0,2 um) mit Gravitationsstaerke
    nicht erreichen.
  - 2501.11690 (Anchordoqui/Antoniadis/Luest 2025, Fortsch. Phys.): zwei um-Dimensionen nur ohne Isometrien (KK-Impuls
    verletzt) und mit feinabgestimmter Reheating-Temperatur [S Abstract]. -> bestaetigt (eigene Spannung zu MVV n = 1).
  - Moderator (Feldregel 1): DM-Lesart (Kaskade) gegen Geometrie (R); Langhoff verbindet beide ueber das
    unvermeidliche Freeze-in. Zweiter Moderator: flach gegen gewarpt (Lee/Randall/Riojas behaupten Universalitaet).

### Block A4 (Erwartung geschrieben 2026-10-02 20:45:12 CEST)
- A4 API id_list 2002.11761 (Lee 2020), hep-ph/0611184 (Kapner 2007), hep-ph/0307284 (Adelberger/Heckel/Nelson 2003):
  Erwartung: Kapner nennt "R* <= 44 um" fuer eine Zusatzdimension mit alpha = 8n/3 (n = 1 -> 8/3); Lee 2020 nennt eine
  Zahl fuer die groesste Zusatzdimension (~30 um). Adelberger 2003: alpha = 8n/3 fuer n-Torus.
- Ausgang A4 (eingetragen 2026-10-02 20:46:00 CEST) [S]:
  - Lee 2020 Abstract: nur "gravitational-strength Yukawa ... ranges < 38.6 um"; keine Zusatzdimensionszahl im Abstract.
  - Kapner 2007 Abstract: "|alpha| <= 1 down to ... 56 um" und "an extra dimension must have a size R <= 44 um".
  - Adelberger/Heckel/Nelson 2003 (Volltext, quellen/Adelberger-2003.txt Z. 742-752): flacher n-Torus: tiefster KK-Mode
    Multiplizitaet 2n, "giving alpha = 8n/3 and lambda = R*"; Faktor 4/3, weil massives Spin 2 fuenf Polarisationen hat
    und der longitudinale Mode nicht entkoppelt (direkt fuer Frage 7). Groesste Einzeldimension: alpha = 8/3.
  - **Kleiner Verstoss:** MVV schreiben die n=1-Zahl "l < 44 um" der Neutronenstern-Heizung zu (Ref. [33] = PDG 2020,
    [34] = Hannestad/Raffelt). 44 um ist aber genau Kapners Laborschranke; Hardy u. a. 2025: fuer n = 1 sind
    Sternschranken schwaecher als Labor. [H] MVV verwechseln dort Labor- und Sternschranke; folgenlos fuer ihr Argument.
  - [E] Fuer alpha = 8/3 liegt die Lee-2020-Grenze unter der fuer 4/3 (~35-37 um) -> MVVs "around 30 um" plausibel.

### Block A5 Gegensweep D1 (Erwartung geschrieben 2026-10-02 20:46:00 CEST)
- A5 API id_list 2404.10068 (Branchina u. a.), 2507.03090 (Bedroya/Obied/Vafa/Wu), 2403.12899 (Schwarz):
  Erwartung: Branchina kritisiert die Casimir-/EFT-Grundlage (Lambda nicht natuerlich aus Turm); Bedroya: DESI-artige
  zeitabhaengige Dunkle Energie im Szenario; Schwarz: skeptisch zur Stringeinbettung. Keine Messschranke.
- Ausgang A5 (eingetragen 2026-10-02 20:46:16 CEST) [S Abstracts]: bestaetigt, mit Zusatz: Schwarz 2024 nennt "roughly 1 -- 10 microns" und
  zeigt eine zweite Einbettung: Intervall mit Branen an beiden Enden -> "a parallel 4d spacetime microns away from us"
  (direkter Bezug zu Finns "Seiten einer Dimension" [H]). Bedroya/Obied/Vafa/Wu (v3 05/2026): Radius laeuft mit einem
  Skalar phi, Dunkle Energie und DM-Masse aendern sich gekoppelt; Anpassung an DESI DR2 + SN; c' ~ 0,05 +- 0,01 unter
  Fuenfte-Kraft-Grenze c' <~ 0,2. Branchina u. a. (IJGMMP 2024): UV-empfindliche Terme in rho, Streit offen.

### Block B1 (Erwartung geschrieben 2026-10-02 20:46:16 CEST)
- B1 arXiv-API all:"ultralight dark matter" AND all:clock (nach Datum, 40) und all:"scalar dark matter" AND
  all:"atomic clocks" AND all:review: Erwartung: Uebersichten (Antypas u. a. 2022; ggf. neuere 2024-26), juengste
  Messungen mit optischen Uhren/hochgeladenen Ionen/Th-229; Kopplung d_e ~ 1e-4 bis 1e-6 bei 1e-22 bis 1e-16 eV.
- Ausgang B1 (eingetragen 2026-10-02 20:46:48 CEST) [S Abstracts, quellen/api-B1*.xml]: bestaetigt, staerker als erwartet:
  - Filzinger u. a., PRL 130, 253001 (2023): Yb+ E3/E2 und E3/Sr; d_e fuer 1e-24 bis 1e-17 eV um "more than an order
    of magnitude" verbessert.
  - Arakawa u. a. 2602.16804 (02/2026, JILA, Th-229-Kernuhr): staerkste Schranken 1e-21 bis 1e-19 eV; Wortlaut
    "effective interaction scales exceeding 10^6 times the Planck scale".
  - Sherrill u. a., NJP 25, 093012 (2023): Sr/Yb+/Cs, Minuten bis ein Tag.
  - Smarra u. a., PRD 110, 043033 (2024, EPTA): "universal conformal coupling" -> Modulation der Pulsarfrequenz;
    Schranken auch fuer Brans-Dicke/Damour-Esposito-Farese mit Masse. -> stuetzt V-B': universelle Kopplung braucht
    den Gravitations-/Pulsar-Kanal [H bis Beleg fuer "Uhrverhaeltnisse blind"].
  - Weitere Treffer: Th-229-Uebersicht 2606.26600; EPTA DR2 2411.02915; NANOGrav 15 J "New Physics" 2306.16219; PTA
    quadratische Kopplung 2510.13945; Uhren im Orbit 2601.16259; Theorie aus Quantengravitation 2510.23808.

### Block B2 und C1 (Erwartung geschrieben 2026-10-02 20:46:48 CEST)
- B2 API id_list 1009.5514 (Uzan, Living Rev.), hep-th/0208093 (Duff): Erwartung: Beide sagen, nur dimensionslose
  Konstanten sind messbar -> Uhrvergleiche sehen nur Verhaeltnisse.
- C1 API all:"Page-Wootters" (nach Datum, 40) plus id_list 1310.4691 (Moreva 2014): Erwartung: viele Theoriearbeiten
  2024-26, wenige Experimente (Moreva 2014/2017, evtl. Qubit-Plattformen); Uebersicht vorhanden.
- Ausgang B2/C1 (eingetragen 2026-10-02 20:47:08 CEST) [S Abstracts]:
  - Duff hep-th/0208093: Zeitvariation dimensionsbehafteter Konstanten "has no operational meaning"; Dirac-Zitat zu
    dimensionslosen Groessen. Uzan LRR 2011: variierende Konstante = fast masseloses Feld, verletzt Universalitaet des
    freien Falls; Schranken aus Uhren, Oklo, Pulsaren usw. -> B2 bestaetigt.
  - Moreva u. a., PRA 89, 052122 (2014): Page-Wootters mit Polarisation zweier Photonen; innerer Beobachter sieht
    Entwicklung, aeusserer beweist Stillstand. -> bestaetigt.
  - Page-Wootters: 50 arXiv-Treffer, fast nur Theorie; juengste 2026: 2608.27650 (topologische Windungs-Auslesung einer
    PW-Uhr), 2608.09601 (Zeitdilatation im PW-Formalismus), 2604.21805 (Uhren-Mehrdeutigkeit), 2608.16732; 2304.01263
    (Gravitationspotential und Zeitdilatation aus globaler Quantenuhr); 2409.06479 (periodische Uhren).

### Block C2 (Erwartung geschrieben 2026-10-02 20:47:08 CEST)
- C2 API id_list 2608.27650, 2304.01263, 2409.06479, 1904.12390 (Smith/Ahmadi), 2604.21805: Erwartung: Windungs-
  Auslesung ist ein Theorie-/Simulationsvorschlag; 2304.01263 leitet Zeitdilatation formal her, ohne neue Messgroesse;
  Smith/Ahmadi sagen "quantum time dilation" als pruefbaren Effekt voraus (kein Messnachweis); Uhrenmehrdeutigkeit =
  Deutungsproblem.
- Ausgang C2 (eingetragen 2026-10-02 20:47:38 CEST) [S Abstracts, quellen/api-C2.xml]:
  - Smith/Ahmadi, Nat. Commun. 11, 5360 (2020): Quantenkorrektur zur Zeitdilatation bei Ueberlagerung von Impulspaketen,
    "has the potential to be observed in experiment" -> bestaetigt (Vorhersage, kein Nachweis im Abstract).
  - Singh/Friedrich 2304.01263 (Found. Phys. angenommen, v2 10/2025): aus Wheeler-DeWitt-artiger Kopplung von
    Masse-Energie an Koordinatenzeit folgen Zeitdilatation (Schwarzschild, fuehrende Ordnung) und Newton-Wechselwirkung;
    Quantenkorrekturen nur "suggesting". -> bestaetigt (formal, keine Messgroesse).
  - Stoica 2604.21805: Uhren-Mehrdeutigkeit ist staerker als gedacht (erfasst auch Bewegungsgesetze); Loesung nur durch
    physikalische Bedeutung der Operatoren -> Deutungsproblem, bestaetigt.
  - Zaravashan u. a. 2608.27650: Photonik-Vorschlag, topologische Windung einer PW-Uhr messen -> Vorschlag, bestaetigt.
  - **Verstoss (mittel, fuer Frage 6 wichtig):** Chataignier/Hoehn/Lock/Mele, NJP 28, 034504 (2026), periodische Uhren:
    relationale Observablen relativ zu periodischer Uhr nur invariant, wenn die Groesse selbst periodisch ist; "counting
    winding numbers does not lead to invariant observables"; ein periodisch laufendes System kann bezueglich einer
    aperiodischen Uhr monoton laufen. Folge [H]: Q-Ball-Phase und Schwebung sind periodische Uhren; ohne aeussere Zeit
    liefert ihr Windungszaehler keine invariante Zeit -> Test in Frage 6 muss das trennen (aeussere Zeit t vorhanden).

### Block C3 (Erwartung geschrieben 2026-10-02 20:47:38 CEST)
- C3a API all:"quantum time dilation" (nach Datum): Erwartung: nur Theorie und Vorschlaege (Ionen, Atome), kein Nachweis
  bis 10/2026.
- C3b API id_list gr-qc/9406019 (Connes/Rovelli), 1005.2985 (Rovelli/Smerlak), 0903.3489 (Barbour): Erwartung: thermische
  Zeit reproduziert Tolman-Ehrenfest/Unruh, keine neue Vorhersage; Barbour: Zeit als Abstraktion aus Veraenderung,
  Deutung.
- Ausgang C3 (eingetragen 2026-10-02 20:47:58 CEST) [S Abstracts]: bestaetigt. "quantum time dilation": 8 Treffer, 2019-2024, nur Theorie und
  Vorschlaege (u. a. 2004.10810 "A new test of relativistic quantum theory", 2006.10084 Atomspektren); kein Nachweis
  nach Recherchestand. Connes/Rovelli CQG 11, 2899 (1994): Zeitfluss aus thermischem Zustand (Tomita-Takesaki), Bezug
  Unruh/Hawking. Rovelli/Smerlak CQG 28, 075007 (2011): Temperatur = Rate der thermischen Zeit gegen Eigenzeit,
  leitet bekannten Tolman-Ehrenfest-Effekt her. Barbour 0903.3489: Dauer "redundant", Uhren entstehen aus zeitlosem
  Gesetz der Veraenderung.

### Block D1 (Erwartung geschrieben 2026-10-02 20:47:58 CEST)
- D1a API all:"Q-ball" AND all:"Kaluza-Klein"; D1b all:"Q-balls" AND all:"extra dimension"; D1c all:"weak gravity
  conjecture" AND all:Q-ball; D1d all:"Q-balls" AND all:"global symmetry" AND all:gravity: Erwartung: wenige (<10)
  Treffer je Abfrage; Q-Baelle auf Branen/RS, KK-Q-Baelle als 5D-Konstruktion; kaum etwas, das die Phase als Bewegung
  in einer Zusatzdimension deutet; WGC/Q-Ball 0-3 Treffer.
- Ausgang D1 (eingetragen 2026-10-02 20:49:05 CEST) [S Abstracts, quellen/api-D1.xml]: Trefferzahl wie erwartet duenn (4/8/1/0/2), aber
  **Verstoss (mittel)** im Inhalt: Die KK-Lesart der Q-Ball-Ladung steht ausdruecklich in der Literatur:
  - Demir, PLB 495, 357 (2000): kompakte Mannigfaltigkeit induziert kontinuierliche 4D-Symmetrien -> stabile Q-Baelle;
    "mass per unit charge ... bounded by the size of the extra dimensions"; KK-Niveaus des Higgs bilden Q-Ball; DM-Kandidat.
  - Abel/Kehagias, JHEP 11 (2015) 096 "Q-branes": Q-Baelle im Bulk "carry Kaluza-Klein charge and possess a
    corresponding Kaluza-Klein tower of states just as normal particles".
  - Herdeiro/Radu 2503.15069 (2025): Q-Ball/Bosonstern x S^1 (Groesse L): uniforme Bosonstrings haben bei kritischem L
    einen statischen Nullmode -> Gregory-Laflamme-Instabilitaet fuer groesseres L; dazu lokalisierte 5D-Bosonsterne.
  - Brihaye/Herdeiro/Radu JHEP 10 (2022) 153 (Q-Haar in D = 5); Krippendorf/Muia/Quevedo JHEP 08 (2018) 070 (Moduli-
    Sterne, Q-Baelle aus offenen String-Moduli). WGC+Q-Ball: nur 1907.04982 (Schwarze Loecher in Q-Wolken), ungelesen.
  - Folge [H]: D4 haengt am Regime: Lesart als Feldraum-Umbenennung -> keine neue Vorhersage; Lesart als echte
    Zusatzdimension -> neue Aussagen (KK-Turm angeregter Q-Baelle, E/Q < 1/R, GL-Instabilitaet ab kritischem L), aber
    als Modellaenderung, nicht als Vorhersage des jetzigen Modells.

### Block E1 (Erwartung geschrieben 2026-10-02 20:49:05 CEST)
- E1 API id_list gr-qc/9805018 (Overduin/Wesson), hep-th/0503158 (Jaffe), 1001.0785 (Verlinde 2011), 1611.02269
  (Verlinde 2017), 1612.03034 (Brouwer 2017), 2106.11677 (Brouwer 2021), 0712.2485 (Ambjorn u. a. 2008): Erwartung:
  KK-Uebersicht nennt Impuls in 5. Dimension = Ladung; Jaffe: Casimir ohne Nullpunktsenergie als relativistische
  van-der-Waals-Kraft; Verlinde: Gravitation entropisch; Brouwer 2017 vertraeglich, 2021 (KiDS-1000) mit Spannungen fuer
  EG; Ambjorn 2008: de-Sitter-Form aus CDT bei festem Volumen.
- Ausgang E1 (eingetragen 2026-10-02 20:49:27 CEST) [S Abstracts, quellen/api-E1.xml]: im Kern bestaetigt.
  - Jaffe PRD 72, 021301 (2005): Casimir-Kraefte "can be computed without reference to zero point energies"; Kraft
    verschwindet fuer alpha -> 0.
  - Verlinde JHEP 04 (2011) 029: Gravitation als entropische Kraft bei emergentem Raum; auch Traegheit entropisch.
    Verlinde SciPost 2, 016 (2017): zusaetzliche "dunkle" elastische Kraft aus Entropieverdraengung, Skala a0 = c H0.
  - Brouwer u. a. MNRAS 466, 2547 (2017): EG ohne freie Parameter passt zu Linsenprofilen. Brouwer u. a. A&A 650, A113
    (2021, KiDS-1000): RAR passt zu MOND/EG, aber >= 6 sigma Unterschied frueh/spaet-Typ bei gleicher Sternmasse, den
    Theorien mit eigenschaftsunabhaengiger Modifikation nicht erklaeren koennen (Gas-Halos als Ausweg).
  - Ambjorn/Goerlich/Jurkiewicz/Loll PRL 100, 091304 (2008): CDT-Universum mit hoher Genauigkeit de Sitter, 17-28
    Planck-Laengen. Rolle der Kosmokonstante im Abstract nicht genannt -> offen (Nachbarkarte).
  - Overduin/Wesson Phys. Rep. 283, 303 (1997): Uebersicht; keine der drei KK-Varianten beobachtungsseitig ausgeschlossen
    (Stand 1997).

### Block F1 (Erwartung geschrieben 2026-10-02 20:49:27 CEST)
- F1 API all:"Q-balls" AND all:phase AND all:interaction; all:"charge-swapping"; all:"Q-ball" AND all:synchroniz*;
  id_list hep-th/0002171? (Battye/Sutcliffe Q-ball dynamics, Kennung ungewiss), 1409.3232? (Copeland/Saffin/Zhou):
  Erwartung: Kraft zwischen Q-Baellen haengt von der Phasendifferenz ab (in Phase anziehend, gegenphasig abstossend);
  bei verschiedenem omega oszilliert sie mit Delta omega; Ladungstausch bei Stoessen; Synchronisation durch Hintergrund
  kaum untersucht.
- Ausgang F1 (eingetragen 2026-10-02 20:50:25 CEST) [S Abstracts, quellen/api-F1.xml]: bestaetigt, mit zwei unerwarteten Funden:
  - Bowcock/Foster/Sutcliffe J. Phys. A 42, 085403 (2009, 1+1D): Kraft "attractive or repulsive depending upon their
    relative internal phase". Battye/Sutcliffe NPB 590, 329 (2000): Ladungstransfer, Spaltung, erklaert ueber die
    zeitabhaengigen Phasen. Kinach/Choptuik PRD 110, 075033 (2024): geeichte Q-Baelle 3D, Stoesse haengen u. a. von
    relativer Phase und Ladung ab.
  - **Unerwartet (positiv):** Copeland/Saffin/Zhou PRL 113, 231603 (2014): Ladungstausch-Q-Baelle, in einem Verbund
    tauschen + und - Ladung "at a frequency lower than the natural frequency of an individual Q-ball" -> eine langsame
    Uhr aus Ueberlagerung schneller Phasen existiert schon (quasistabil; Xie/Saffin/Zhou JHEP 07 (2021) 062: vier
    Stadien, Lebensdauern kartiert).
  - **Unerwartet (positiv):** Gleiser/Howell hep-ph/0209176 (2003): synchronisiertes Entstehen von Oszillonen, angetrieben
    von resonanten parametrischen Schwingungen des Nullmodes; nur im geschlossenen System, nicht mit Waermebad.
    -> ein gemeinsames Hintergrund-Feld (Nullmode) synchronisiert schon in der Literatur, allerdings die Entstehung,
    nicht die Takte fertiger Baelle.

### Block G1 (Erwartung geschrieben 2026-10-02 20:50:25 CEST)
- G1a API id_list 1005.3035 (Van Raamsdonk), 1105.3735 (Hinterbichler), 1709.09660 (GW170814), 2112.06861 (GWTC-3
  Tests): Erwartung: VR: Verschraenkung trennen -> Raum zerfaellt; Hinterbichler: vDVZ, 5 Polarisationen massiv;
  GW170814: Tensor bevorzugt gegen reine Skalar/Vektor; GWTC-3: keine Abweichung.
- G1b API all:"open string" AND all:"speed of light" AND all:endpoints: Erwartung: Arbeiten zu rotierenden Strings
  (Regge), Endpunkte masseloser Enden mit c.
- Ausgang G1 (eingetragen 2026-10-02 20:51:24 CEST) [S]:
  - Van Raamsdonk GRG 42, 2323 (2010): Entflechten zweier Regionen -> sie "pulling apart and pinching off" -> bestaetigt.
  - Hinterbichler RMP 84, 671 (2012): vDVZ-Unstetigkeit, Aufloesung durch Vainshtein; massive Gravitonen auch aus
    Zusatzdimensionen/Branen -> bestaetigt.
  - GW170814 PRL 119, 141101 (2017): erstmals Polarisationstest mit drei Detektoren. GWTC-3-Tests PRD 112, 084080 (2025):
    keine Nicht-GR-Polarisationsmoden; m_g <= 2,42e-23 eV (90 %) -> bestaetigt.
  - G1b Suche "speed of light"+endpoints+rotating: 0 Treffer (Kanal untauglich). Ersatz: Tong, Lectures on String Theory
    (0908.0333), Volltext [S, quellen/Tong-0908.0333.txt]: Z. 2566 Neumann-Rand: "the end point of the string moves at
    the speed of light"; Z. 2213 masseloses Spin-2-Teilchen im geschlossenen String; Feynman/Weinberg -> ART.

### Block H1 Gegensweep-Pruefung (Erwartung geschrieben 2026-10-02 20:51:24 CEST)
- H1a API all:"dark dimension" AND (all:torsion OR all:"inverse square" OR all:"short-range"): Erwartung: 0-5 Treffer,
  eher Vorschlaege/Projektionen als Messungen.
- H1b API id_list 2609.22501 (van Manen u. a.): Erwartung: Projektion bis ~20 meV (lambda ~ 10 um), nennt Dark Dimension
  als Motivation.
- H1c MVV-Text zu Radion (Z. ~495-510): Erwartung: Radion muss schwer sein oder entkoppelt, sonst Fuenfte Kraft.
- Ausgang H1 (eingetragen 2026-10-02 20:51:54 CEST) [S]:
  - H1a bestaetigt: 4 Treffer, keine Kurzabstandsmessung oder -projektion fuer die Dark Dimension; 2606.19440 (Braun/
    Cicoli/Milioli/Valandro, Moduli-Stabilisierung ADD/Dark Dimension), 2609.25230, 2507.03090, 2402.00981.
  - H1b **kleiner Verstoss**: 2609.22501 ist keine Kurzabstands-Projektion fuer die Dark Dimension, sondern
    gravitationsinduzierte Verschraenkung in Stelle-Gravitation; "spin modes as low as 0.0197 eV become distinguishable
    ... at a distance d ~ 40 um"; Nebenbedingung m0 < 4^(1/3) m2. Fuer diese Karte nur Randnotiz.
  - H1c bestaetigt (MVV Z. 500-506): Radion muss schwer sein oder entkoppelt, "to avoid trouble with fifth-force
    constraints [32]" -> Kurzabstands-Signal der Dark Dimension = KK-Graviton-Yukawa (alpha = 8/3, lambda = R) plus
    ggf. Radion-Skalar; Letzteres modellabhaengig.

### Block H2 (Erwartung geschrieben 2026-10-02 20:51:54 CEST)
- H2a API id_list 1309.5888 (Khmelnitsky/Rubakov): Erwartung: ULDM erzeugt rein gravitativ ein mit 2m oszillierendes
  Potential, sichtbar im Pulsar-Timing (universeller "Takt" ohne Kopplung).
- H2b Crossref DOIs 10.1103/PhysRevD.9.3471 (Chodos u. a.), 10.1103/PhysRevD.15.1694 (Friedberg/Lee),
  10.1103/PhysRevD.27.2885 (Page/Wootters): Erwartung: Metadaten stimmen (Titel, Jahr).
- Ausgang H2 (eingetragen 2026-10-02 20:55:00 CEST) [S]: Khmelnitsky/Rubakov JCAP 02 (2014) 019: oszillierender Druck -> Potentialschwingung
  ~1e-15, nHz, PTA/SKA -> bestaetigt. Crossref: Chodos/Jaffe/Johnson/Thorn/Weisskopf "New extended model of hadrons"
  (PRD 9, 3471, 1974); Friedberg/Lee "Fermion-field nontopological solitons" (PRD 15, 1694, 1977) und "... II. Models
  for hadrons" (PRD 16, 1096, 1977); Page/Wootters "Evolution without evolution: Dynamics described by stationary
  observables" (PRD 27, 2885, 1983) -> Metadaten bestaetigt.
- Zwischenstand Zeit: 20:54:25 (date) -> Restbudget erlaubt Vertiefung (Block I).

### Block I1 Vertiefung (Erwartung geschrieben 2026-10-02 20:55:00 CEST)
- I1a Lee/Randall/Riojas Volltext (grep "Dark Dimension", "rule", "R", "um"): Erwartung: Sie rechnen das Gonzalo-
  Montero-Obied-Vafa-Szenario nach und zeigen, dass die Kaskade zu langsam ist; keine eigene R-Schranke.
- I1b API id_list 2307.11048 (Law-Smith/Obied/Prabhu/Vafa): Erwartung: Roentgen/Gamma-Schranken auf zerfallende
  dunkle Gravitonen, Szenario damals noch vertraeglich.
- I1c Demir 2000 Volltext: Erwartung: Ladung = KK-Zahl, Q-Ball-Ansatz mit e^(i n y/R), Bedingung E/Q < 1/R.
- I1d API Suche "two-time physics" (Bars) und all:Stueckelberg AND all:"invariant evolution parameter": Erwartung:
  Bars-Arbeiten seit 1998 ohne Messbestaetigung; Horwitz-Stueckelberg mit Zeitparameter tau, Vorschlaege fuer
  Interferenz in der Zeit.
- Ausgang I1a (eingetragen 2026-10-02 20:55:29 CEST) [S Volltext quellen/LeeRandallRiojas-2609.36234v1.txt Z. 405-440]: bestaetigt. Fuer die
  GMOV-Parameter (m_KK ~ eV, delta n_max ~ 1e2) waere die Kaskaden-Lebensdauer ~1e26 s statt 1e2-3 s; Rettungsversuch
  mit viel kleineren Anfangsmassen traefe "KK-mode-mediated fifth forces" und Kick-Geschwindigkeit; Begleitarbeit zu
  gewarpter Alternative angekuendigt. Keine eigene R-Schranke. ~~Neu: Das DM-Szenario nutzte m_KK ~ eV; Langhoff Z. 230:
  Benchmark von Ref. [9] "R = 0.05-0.2 um" -> die DM-Variante lag schon unter 1 um (Pruefung I1e).~~
  [gestrichen ~~20:58~~ (Uhrzeit von Hand geschaetzt, berichtigt: Streichung lag zwischen 20:55:29 und 20:56:13 nach date), siehe Ausgang I1e: Langhoff-Satz im Lesefluss (pdftotext ohne -layout) nennt "the benchmark of
  Ref. [9], and R = 0.05-0.2 um" nebeneinander; GMOV brauchen laut Langhoff "T_RH ~ GeV [9] for m_KK ~ meV". Die
  Lesart "Benchmark lag unter 1 um" war ein Spaltensalat-Fehlschluss.]
- I1e API id_list 2209.09249 (GMOV), 2307.11048 (Law-Smith u. a.) (Erwartung geschrieben 2026-10-02 20:55:29 CEST): Erwartung: GMOV nennen
  m_KK ~ 1-100 eV bzw. R ~ 0,01-1 um fuer DM; Law-Smith: Roentgen/Gamma-Schranken noch vertraeglich.
- Ausgang I1e (eingetragen 2026-10-02 20:56:13 CEST) [S Abstracts quellen/api-I1e.xml]: **Verstoss (klein bis mittel):**
  - GMOV (JHEP 11 (2023) 109): dunkle Gravitonen als "unavoidable dark matter candidate", erzeugt bei T ~ 4 GeV,
    Masse heute 1-100 keV; keine R-Zahl im Abstract.
  - Law-Smith/Obied/Prabhu/Vafa (2307.11048 v3, 01/2024): Schranken aus CMB-Verzerrung u. a. vertraeglich; Vorhersage
    DM-Masse heute "a few hundred keV" und "effective size of the extra dimension is around 1 - 30 um".
  - Folge [H]: Die DM-Variante zielte auf 1-30 um, oberes Ende direkt an der Torsionswaagen-Grenze (~30 um fuer
    alpha = 8/3). Genau diese Variante trifft der neue Ausschlussanspruch (Langhoff: R <~ 0,2 um).
- **Verfahrensvermerk ~~20:58~~ (geschaetzt; berichtigt: gleicher Eintrag wie Ausgang I1e, date 20:56:13):** In einem Bash-Aufruf stand unnoetig "python3 --version" (Ausgabe verworfen, keine
  Rechnung). Das verletzt die Regel "kein python lokal" dem Wortlaut nach; nicht wiederholt.
- I1c/I1d jetzt (Erwartungen siehe Block I1, unveraendert; Abruf ab 2026-10-02 20:56:13 CEST)
- Ausgang I1c (eingetragen 2026-10-02 20:56:44 CEST) [S Volltext quellen/Demir-raw.txt]: bestaetigt und erweitert (zu V2):
  - Gl. (5): U(1)_KK "generated by translations along S^1": phi_n -> phi_n e^(i n alpha).
  - Gl. (8): Q-Ball: "the scalars phi_n rotate in the internal space with velocities proportional to their U(1)_KK
    charge", phi_n = varphi_n e^(i n omega t). Gl. (7): M_n^2(omega) = m^2 + (1 - omega^2 R^2) m_n^2.
  - Bei flachem Potential "M_Q ~ Q^(3/4) rather than Q" -> dasselbe Gesetz wie unser Beutelgesetz E ~ Q^(3/4) (R17).
  - Stabilitaet: Masse je Ladung "bounded by the inverse compactification radius"; damals 1e-4 eV <~ 1/R.
  - Fuer reelles Bulk-Feld koppeln Niveaus mit Summe n = 0 (phi_n phi_k phi_-(n+k)) -> Q-Ball aus Niveau 1 zieht
    Niveaus 2, 3 ... mit (Obertoene 2 omega, 3 omega) [H aus Gl. 4/5]; unser Ein-Feld-Modell hat keine.
  - [E] Phasengeschwindigkeit entlang y: n omega / (n/R) = omega R, fuer alle Niveaus gleich; gebunden heisst
- Ausgang I1d (eingetragen 2026-10-02 20:57:16 CEST) [S Abstracts quellen/api-I1d.xml]: bestaetigt. Bars, "Two-Time Physics" (hep-th/9809034)
  und PRD 62, 046007 (2000): d+2 Dimensionen (zwei Zeiten), Eichsymmetrien liefern viele 1T-Theorien als "Schatten";
  als Beleg nur versteckte Symmetrien vorgeschlagen. Stueckelberg/Horwitz: 6 Treffer, duenn. "extra time dimension"
  + emergent: 0.

### Block J1 Gegensweep Regel 7 (Erwartung geschrieben 2026-10-02 20:57:16 CEST)
- J1 OpenAlex ab 2024-10-01: search "quantum time dilation" experiment; search "Page-Wootters" experiment: Erwartung:
  keine Beobachtung der Quanten-Zeitdilatation; hoechstens weitere Illustrationen (Photonen, Qubits, NMR) von PW.
- Ausgang J1 (eingetragen 2026-10-02 20:57:52 CEST): im Kern bestaetigt, ein Fund mit Gewicht:
  - OpenAlex "quantum time dilation experiment" ab 10/2024: 5066 Treffer (Rauschen); einschlaegig nur Uebersicht RMP 97,
    015003 (2025) [L? Titel], "Single electron relativistic clock interferometer" (2024) [L? Titel] und
  - ~~Martinez-Lahuerta? (Autoren nicht abgerufen)~~ [berichtigt: Sorci/Foo/Leibfried/Sanner/Pikovski laut API, quellen/api-autoren.xml] "Quantum signatures of proper time in optical ion clocks", PRL 136,
    163602 (2026), arXiv:2509.09573 [S Abstract]: "all measurements of time dilation so far can be explained
    effectively" mit klassischer Eigenzeit; Ionenuhren mit gequetschter Bewegung koennten Quanten-Eigenzeit pruefen,
    "within reach". -> bestaetigt "kein Nachweis", aber Pruefbarkeit naeher als erwartet.
  - OpenAlex "Page-Wootters experiment": 620 Treffer; Zenodo-Protokoll (Ultrametrizitaet, Randbereich, nicht gewertet);
    "Parallel-in-time quantum simulation via Page and Wootters quantum time" (arXiv:2308.12944, 2025 publiziert) =
    rechentechnische Nutzung; keine neue Laborpruefung der Zeitentstehung gefunden (nach Recherchestand).

### Block J2 (Erwartung geschrieben 2026-10-02 20:57:52 CEST)
- J2 CDT-Uebersicht arXiv:1203.3591 (Ambjorn/Goerlich/Jurkiewicz/Loll, Phys. Rep. 519, 127), grep "cosmological
  constant", "fixed", "volume": Erwartung: Simulation bei festem 4-Volumen, nackte Kosmokonstante auf kritischen Wert
  abgestimmt; de-Sitter-Profil aus effektiver Minisuperraum-Wirkung mit Lagrange-Multiplikator fuer das Volumen.
  Nur Kurznotiz (Nachbarkarte).
- Ausgang J2 (eingetragen 2026-10-02 20:58:07 CEST) [S Volltext quellen/CDT-review-raw.txt]: bestaetigt. Z. 5214: "the bare cosmological
  constant kappa4 is tuned to its (pseudo)critical value in the simulations"; Z. 5990-5997: Gesamtvolumen praktisch fest,
  Zusammenhang ueber Ableitung nach der Kosmokonstante, "put in by hand"; Z. 6255: Euklidischer de Sitter "(a four-sphere,
  the maximally symmetric space for positive cosmological constant)"; Z. 8609-8610: "four-volume is the variable
  conjugate to the cosmological constant". -> Kosmokonstante tritt als Volumen-Gegenspieler auf (festes Volumen
  gleichwertig zu Lambda > 0 als Lagrange-Multiplikator) [H aus S].

### Block K1 Frage 7 vertiefen (Erwartung geschrieben 2026-10-02 20:58:33 CEST)
- K1 API all:"spherical" AND all:"resonant" AND all:"gravitational" AND (all:polarization OR all:monopole): Erwartung:
  Arbeiten zu Kugeldetektoren (Lobo 1995; Bianchi/Coccia u. a. 1996): fuenf Quadrupolmoden (l = 2) sprechen auf
  Tensor-Polarisationen an, Monopol (l = 0) auf skalare Atmung; 5 + 1 = 6 = Eardley-Zahl; l = 1 koppelt nicht.
- Ausgang K1 (eingetragen 2026-10-02 20:59:24 CEST): **bestaetigt, mit Literaturbeleg statt [H]:** Bianchi/Coccia/Colacino/Fafone/Fucito,
  CQG 13, 2865 (1996) [S Volltext quellen/Bianchi-raw.txt Z. 658-663, 719-721, 992-996]: "in any metric theory of
  gravity only the l = 0, 2 spheroidal modes of the sphere can be excited"; "five plus one independent spheroidal
  modes"; sechs Polarisationszustaende (NP: Psi2, Phi22, Re/Im Psi4, Re/Im Psi3) "uniquely determined by monitoring
  the six lowest spheroidal modes"; Toroidalmoden nicht anregbar (Veto). Coccia/Gasperini/Ungarelli PRD 65, 067101
  (2002): skalare Strahlung koppelt an den Monopol (l = 0) [S Abstract].
  - [E/H] Zuordnung bei Welle entlang z: Psi4 (ART, + und x) <-> l = 2, m = +-2 (Dehnen x, Quetschen y, z unveraendert,
    Hauptachsen (1, -1, 0)); Zigarre<->Pfannkuchen ist (1, -1/2, -1/2) = 3/4 (1, -1, 0) + 1/4 (1, 1, -2); der zweite
    Anteil ist m = 0 entlang z, also skalar-longitudinal (in der ART nicht vorhanden).

### Block K2 (Erwartung geschrieben 2026-10-02 20:59:24 CEST)
- K2 API id_list 2606.20942 (Danielsson/Giri), 2606.19440 (Braun u. a.), 2402.00981 (Vafa 2024): Erwartung: Dunkle Blase
  = 4D-Welt als Blasenwand in 5D-AdS, Dunkle Energie aus Bulk; Braun: Radion-/Moduli-Stabilisierung moeglich mit
  Aufwand; Vafa 2024: Vereinheitlichung Dunkle Energie/Materie ueber Dark Dimension.
- Ausgang K2 (eingetragen 2026-10-02 20:59:38 CEST) [S Abstracts quellen/api-K2.xml]: **Verstoss (mittel, Vorzeichen):**
  - Danielsson/Giri 2606.20942 (06/2026): Dunkle-Blase-Modell (Lambda > 0 aus Instabilitaeten) sagt eine Dark Dimension
    um-Groesse voraus, aber "a weakening of gravity at distances of order the dark-dimension scale, leading to a fading
    of the gravitational force at micron distances" (Sundrums "fat graviton"); dazu Stringskala ~ zig TeV, positive
    raeumliche Kruemmung. -> In der flachen Variante wird Gravitation unter R STAERKER (KK-Moden, alpha = +8/3), in der
    Blasen-Variante SCHWAECHER. Moderator: Realisierung (flacher Bulk mit Brane gegen Blase in AdS5). Bezug STELLE-24M:
    Lee 2020 zeigt nur |alpha|; das Vorzeichen waere hier entscheidend.
  - Vafa 2402.00981 (Uebersicht 2024): "consistent with the cosmological bounds as well as the Newton's inverse square
    law"; Axion- und sterile Neutrino-Massen 1-10 meV.
  - Braun/Cicoli/Milioli/Valandro 2606.19440: Moduli-Stabilisierung fuer eine grosse Dimension im LVS moeglich, "some
    degree of tuning" fuer Lambda; Fuenfte-Kraft-Schranken analysiert.

### Block L1 Gegensweep (Erwartung geschrieben 2026-10-02 21:00:07 CEST)
- Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe? Kandidat L1: Das Feld, das in der etablierten
  Physik den Uhrengang setzt, ist das Gravitationspotential (g_00). API id_list 2109.12238 (Bothwell u. a.): Erwartung:
  Rotverschiebung ueber eine mm-grosse Atomprobe aufgeloest (Nature 2022).
- Ausgang L1 (eingetragen 2026-10-02 21:01:38 CEST) [S Abstract]: bestaetigt. Bothwell u. a., Nature 602, 420 (2022): Rotverschiebung
  innerhalb einer mm-Probe Sr, Unsicherheit 7,6e-21. -> Das "Feld fuer die Zeit" der etablierten Physik ist das
  Gravitationspotential; Uhren messen es heute auf mm-Hoehe.

## 5. Gegensweep (zusammengefasst, eingetragen 2026-10-02 21:01:38 CEST)

Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | Geprueft? | Ergebnis |
|---|---|---|---|
| GS1 | Die Dark Dimension waere an der |alpha| = 1-Grenze (38,6 um) zu messen | ja (Adelberger 2003, MVV, Kapner) | alpha = 8/3 fuer einen Kreis; Grenze ~30 um (MVV), 44 um (Kapner 2007) |
| GS2 | Das Kurzabstandssignal ist nur der KK-Graviton-Yukawa | ja (MVV Z. 500-506; Danielsson/Giri) | Radion muss schwer/entkoppelt sein; Blasen-Variante sagt SCHWAECHERE Gravitation bei um |
| GS3 | Atomuhren sehen jedes "Takt-Feld" | ja (Duff; Smarra; Khmelnitsky/Rubakov) | universelle Kopplung fuer Uhrverhaeltnisse unsichtbar; nur ueber Pulsare/Gravitation |
| GS4 | Die Phase eines einzelnen Q-Balls ist eine beobachtbare Uhr | Literatur indirekt (Bowcock: nur relative Phase wirkt); [H] | Dichte eines exakten Q-Balls ist stationaer; die Phasenuhr wird erst relativ zu einem zweiten Ball sichtbar |
| GS5 | WebFetch-Zusammenfassungen = Abstract-Wortlaut | ja (curl auf die API) | Lee/Randall/Riojas: Abrufmodell paraphrasierte; Wortlaut nachgezogen |
| GS6 | Das Feld, das den Uhrengang setzt, muesste neu sein | ja (Bothwell 2022) | Gravitationspotential leistet das schon, gemessen auf mm |
| GS7 | Uhrschranken gelten fuer jedes Feld | nein | Annahme: Feld = lokale Dunkle Materie (Amplitude aus rho_DM); fuer ein Nicht-DM-Feld gelten sie so nicht [H, ungeprueft] |
| GS8 | Langhoffs Ausschluss gilt fuer jede Dark-Dimension-Variante | teils | Annahme flach; Lee/Randall/Riojas behaupten Universalitaet auch mit Warp; Gegenrede im arXiv bis 01.10. nicht gefunden |

### Block M1 (Erwartung geschrieben 2026-10-02 21:01:50 CEST)
- M1 Abel/Kehagias "Q-branes" Volltext (grep KK charge, tower, graviphoton, gauge): Erwartung: Q-Ball im Bulk mit
  Impuls n/R entlang der Zusatzdimension -> Masse sqrt(M_Q^2 + n^2/R^2) als Turm; Graviphoton nicht behandelt.
- Ausgang M1 (eingetragen 2026-10-02 21:02:07 CEST) [S Volltext quellen/AbelKehagias-raw.txt Z. 58-90, 495-522]: teils **Verstoss (klein)**:
  - 5D-U(1)-Modell mit kompakter Dimension: Q-Baelle tragen globale Ladung Q UND KK-Impuls P5 = Q p + n/R (Turm);
    E^2(P5) = E^2(0) + P5^2; "the large Q-ball is blind to the compactness of the extra dimension".
  - Scherk-Schwarz-Phase p mit phi(x, y + 2 pi R) = e^(ip) phi: "non-integer momentum per unit charge" -> die innere
    Phase windet sich entlang der Zusatzdimension; Impuls proportional zur Ladung.
  - Graviphoton nicht gefunden (nicht behandelt, nach grep).
  - Folge [H]: Es gibt ZWEI KK-Lesarten: Demir (Ladung = KK-Zahl) und Abel/Kehagias (eigene Ladung, ueber Verdrillung
    an den Impuls gekoppelt). Beide sind Modellerweiterungen; fuer das jetzige Modell ohne kompakte Richtung folgt nichts.

## 6. Schreibphase
- ERGEBNIS.md Schreibbeginn: 2026-10-02 21:02:07 CEST (date).
- Verfahrensvermerk (2026-10-02 21:02:53 CEST, date): Zwei Uhrzeiten (20:58) waren von Hand geschaetzt statt gemessen; oben gestrichen und berichtigt.
- Autorenabgleich (2026-10-02 21:06:40 CEST, date): quellen/api-autoren.xml; geratener Autorname in J1 gestrichen und berichtigt.
- Autorenabgleich 2609.22501 (2026-10-02 21:10:41 CEST, date) fuer die Quellenliste.
- Rueckwaerts-Gegenlesen ERGEBNIS.md (2026-10-02 21:11:28 CEST, date): Zahlen und Fundstellen gegen quellen/ geprueft; eine Gleichungsangabe berichtigt (MVV Gl. 3.6-3.7 statt 3.5-3.7); Quellenzeile 2609.22501 mit Autoren aus der API ersetzt.

## 7. Abschluss
- ERGEBNIS.md fertig: 2026-10-02 21:11:44 CEST (date). Zeitbox (bis ~22:07) eingehalten.
- Offene Rueckfragen wandern mit: R1 (Finns "Seiten einer Dimension"); Beobachtung arXiv "dark dimension" auf Gegenrede
  zu Langhoff und Lee/Randall/Riojas; vorzeichengetrennte Lee-2020-Schranken (aus STELLE-24M).
