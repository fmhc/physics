# ARBEITSFELD DUNKEL-FLIP-L (feldforscher, Runde 42)

- Einzige Arbeitsdatei dieser Karte. Vor jedem Schritt neu lesen. Gestrichenes bleibt stehen (~~so~~), offene
  Rueckfragen wandern im Abschnitt 6 mit.
- Start 2026-10-04 17:02:06 CEST (date). Zeitbox 75 min. Karte KARTE.md vollstaendig gelesen 17:02.
- Datei angelegt nach Lesen der Vorarbeit und Projekt-grep, vor dem ersten Abruf (date 17:06:31 vor dem Anlegen).
- Marken wie in der Karte: [S] an der Quelle gelesen, [S Abstract], [P] Projektdatei, [L] Gedaechtnis, [L?] unsicher,
  [ES] eigener Schluss, [H] Hypothese, [E] Kopfrechnung.
- Regeln: keine Websuche; hoechstens 12 Abrufe mit lokaler Kopie in quellen/; lokal nur curl, pdftotext, grep, sed, jq,
  date; nichts Versiegeltes oeffnen; nur in diesem Ordner schreiben.

## 0. Erwartungen der Leitung (Karte, vor jedem Abruf festgelegt)

E1 Zitterbewegung (ZB) 2mc^2/hbar, Amplitude ~ halbe Compton-Laenge, frei nicht beobachtet, Simulatoren (Gerritsma 2010).
E2 Feynman-Schachbrett 1+1 mit i eps m je Umkehr = Dirac-Propagator; 3+1 nicht einfach (Jacobson/Schulman 1984).
E3 Grassmann-Richtungen zaehlen -1 (Parisi/Sourlas 1979, Dimensionsreduktion d -> d-2).
E4 Spiegelwelt nur ueber Schwerkraft und schwache Mischung verbunden; n-n'- und o-Ps-Suchen ohne Befund.
E5 RS1: zwei Branen entgegengesetzter Spannung; unsere Welt auf der Brane mit negativer Spannung.
E6 Negative Masse laeuft mit positiver davon (Bondi 1957); Farnes 2018 umstritten.
E7 Dirac-See in der QFT umgedeutet; messbar nur Vakuumeffekte (Vakuumpolarisation, Casimir), kein See selbst.

## 1. Vorarbeit aus dem Projekt (ohne Abruf; Marke [P], dort mit eigener Marke gefuehrt)

- **Dark Dimension** (RUNDE-22/dunkel-zeit, RUNDE-23/dd-spuren):
  - MVV 2205.12293: eine Dimension l ~ 0,1-10 um, Casimir-Schaetzung 7,4 um [P, dort S Volltext].
  - Status strittig: Langhoff 2610.01825 (01.10.2026) R <~ 0,2 um fuer flache DD; Lee/Randall/Riojas 2609.36234
    (28.09.2026) gegen die DM-Kaskade [P, dort S Volltext]. Unbegutachtet.
  - Dunkle Blase (Danielsson/Giri): Schwerkraft wird bei um schwaecher; Potenzterm -(3/2)(L/r)^2 [P, dort S].
- **Kurzabstand** (RUNDE-22/stelle-24m, RUNDE-23/dd-spuren, RUNDE-23/blase-ew):
  - Lee u. a. 2020 (Eot-Wash): |alpha| = 1 bei lambda < 38,6 um, 95 % [P, S].
  - KK-Torus: alpha = 8n/3, lambda = R (Adelberger/Heckel/Nelson 2003) [P, S]; DD-Grenze ~30 um bei alpha = 8/3.
  - Unter 10 um: alpha ~ 1e4 (10 um) bis ~1e11-1e12 (0,2 um) [P, S Abb. Augenmass]; Venugopalan u. a. 2026 alpha < 1e7
    bei 5 um, ~1e6 ab 10 um [P, S].
  - Eot-Wash 2007 Potenzterm k = 3: |beta_3| <= 1,3e-4 (68 %), Blase L <= 9,3 um [P, E blind nachgerechnet].
  - Kein laufendes Projekt erreicht in zwei Jahren Gravitationsstaerke unter 10 um [P]; Mikro-Torsionsresonator
    (Manley 2024) kryogen "potentially" ~10 um [P, S].
  - Cline/Jeon/Moore hep-ph/0311312: Geister mit Lorentz-erhaltendem Abschneider "completely excluded", sonst
    Abschneider < 3 MeV [P, dort S Abstract].
  - Bondi 1957 nur ueber Sekundaerquelle (Wikipedia, arXiv:1408.2451) [P, dort L?].
- **Casimir ohne Nullpunktsenergie:** Jaffe, PRD 72, 021301 (2005): "can be computed without reference to zero point
  energies" [P, dort S Abstract] -> direkt relevant fuer E7.
- **Zitterbewegung im Projekt:**
  - SCHACHBRETT-KAUSAL-1: reine R-Quelle wechselt mit Kreisfrequenz 1,98 ~ 2m; Feynmans ungenormtes Schachbrett weicht
    erster Ordnung ab (0,0295 bei eps = 0,01; Faktor sqrt(1 + m^2 eps^2) je Schritt) [P, E]. Jacobson/Schulman 1984
    dort nur als Zitat bei Johnston [P, S nur als Zitat].
  - Hestenes, "Reading the Electron Clock", arXiv:0802.3227 (Channeling, 80,87 MeV/c) [P, Notiz
    dashboard-overview-20260909/snapshot/review-2026-09-06/next-tests/channeling_transit_note.md].
  - Gravity-Audit 09.09.: "Zitterbewegung beweist die Zweiteilchenstruktur nicht" (Interferenz beider
    Energievorzeichen) [P].
  - LIT-BIC-QBALL (R34): photonische ZB in binaeren Wellenleitern (Longhi 2010) [P, S Abstract]; Dreisow-Messung nicht
    gefunden [P].
- **Gegentakt und Spiegel im Netz:**
  - QCA-WINDUNG-1: W3 = 0 in allen 53 Projekt-Automaten (vektorartig); Grad-1-Kontrolle: ungepaarter Weyl-Punkt im
    Gegentakt (Quasienergie pi) [P, E].
  - CHIRAL-L: Doppler als Spiegelpartner; Spiegel unter derselben SU(2) x U(1) hoechstens TeV-Masse [P, dort L];
    SMG = Spiegel durch starke Kopplung entfernen, umstritten [P, S Abstract].
- **Spiegelwelt (Lee/Yang, KOP, Foot, Berezhiani):** im Projekt nirgends bearbeitet; einzig Oikonomou 2609.29495
  ("complex" = mehrkomponentig, Spiegel-DM) als Randnotiz in gesamtmodell-20260927/RECHERCHE-20260927.md Z. 120 [P].
- **Grassmann / negative Dimension / Parisi-Sourlas:** grep-Treffer nur in Fremdzusammenhang (induziert-dirac-2d,
  spin-kausal-l: Grassmann-Integration fuer Fermionen) [P]; Parisi/Sourlas nicht bearbeitet.
- **Randall/Sundrum:** nur DD-Zusammenhang (Lee/Randall/Riojas; Warp-Faktor) [P]; RS1-Spannungsvorzeichen nicht
  gelesen.
- **Kosmische Doppelbrechung:** grep-Treffer in RUNDE-34/grb-221009a und RUNDE-35/36 (Lorentz-Verletzung im
  Photonsektor, GRB-Polarisation) [P]; CMB-Wert beta nicht im Projekt (noch pruefen per grep "Minami|Komatsu").
- **Dirac-See:** nur Randnotizen (SPIN-ZUFALLSNETZ-1, Z. 296; 2609.24159 Titel) [P].

## 2. Abrufplan (Budget 12) und Vorhersage je Abruf

Leitidee: Ein id_list-Abruf der arXiv-API holt viele Abstracts auf einmal (Bestaetigungen kosten so wenig). Suchabrufe
sortiert nach Datum fuer den 24-Monats-Stand je messnahem Thema. Volltext nur dort, wo Zahlen fehlen oder eine
Erwartung verletzt wird.

| Nr | Abruf | Vorhersage vorab (ein Satz) |
|---|---|---|
| F1 | API id_list: 0909.0674, hep-ph/9905221, hep-th/9911055, 1712.07962, hep-ph/0606202, hep-ph/0507031, 1401.3965, hep-ex/0609059, 2011.11254, 2205.13962, 1912.01617, hep-th/0505265, 2009.11046, 2111.05543, 1807.07906, 0807.2838 | Die meisten IDs treffen; Gerritsma nennt ZB im Ion, Badertscher Br(o-Ps->unsichtbar) < 4,2e-7, Minami/Komatsu beta ~ 0,35 Grad, Kaplan/Sundrum eine Geisterkopie des SM; 3 bis 5 IDs sind falsch (Gedaechtnis) |
| F2 | API-Suche Zitterbewegung, nach Datum | Viele Simulator- und Festkoerperarbeiten (Ionen, BEC, Photonik, Polaritonen, Graphen), keine direkte Beobachtung am freien Elektron |
| F3 | API-Suche Spiegelneutron (n-n'), nach Datum | Neue PSI/ORNL/ESS-Ergebnisse oder Vorschlaege; Schranken tau_nn' >~ 350-450 s ohne B'-Feld; kein Signal |
| F4 | API-Suche unsichtbarer o-Ps-Zerfall / Spiegelphoton-Mischung, nach Datum | Kaum neue Messungen seit 2007; Vorschlaege (ETH/PSI) mit Ziel 1e-8 bis 1e-9 |
| F5 | API-Suche kosmische Doppelbrechung, nach Datum | beta ~ 0,2-0,35 Grad bei 2-4 sigma, Kalibrierung der Polarisationswinkel als Hauptstreitpunkt; ACT/SPT/Planck-Kombinationen |
| F6 | API-Suche Parisi-Sourlas / Dimensionsreduktion, nach Datum | Dimensionsreduktion gilt nahe d = 6, bricht unter d ~ 4-5 zusammen (Kaviraj/Rychkov/Trevisani; Fytas u. a.) |
| F7 | API-Suche Antimaterie-Schwerkraft (ALPHA-g, AEgIS, GBAR) bzw. negative Masse, nach Datum | ALPHA-g 2023: Antiwasserstoff faellt nach unten, a ~ 0,75 g +- 0,2; Abstossung ausgeschlossen |
| F8 | Reserve: RS1-Volltext oder Garriga/Tanaka, falls F1 E5 nicht klaert | RS1 nennt die sichtbare Brane mit negativer Spannung |
| F9-F12 | Reserve fuer Verstoesse und Gegensweep | - |

## 3. Abrufprotokoll

(wird je Abruf ergaenzt: Zeit, Datei, Ausgang gegen Vorhersage)

## 4. Erwartungsverstoesse (laufend)

## 5. Gestrichenes

## 6. Offene Rueckfragen

## 7. Gegensweep

### Protokoll (Fortsetzung von Abschnitt 3; chronologisch angehaengt)

- **F1a** 17:07:51: curl ohne -L auf http://export.arxiv.org -> 0 Byte (keine Weiterleitung gefolgt). Zaehlt als Abruf
  ohne Inhalt (1 von 12).
- **F1b** 17:07:58: https mit -L, Datei quellen/F1-api-idlist.xml (40982 Byte, 16 Eintraege). Abruf 2 von 12.
  - Vorhersage "3 bis 5 IDs falsch" -> **verletzt (klein, Methode):** alle 16 IDs treffen (Titel geprueft).
  - Bestaetigt (je eine Zeile):
    - Gerritsma 0909.0674: ein Ion simuliert 1D-Dirac; ZB "for different initial superpositions of positive and
      negative energy spinor states"; ZB und Klein "would be difficult to observe in real particles" [S Abstract].
    - Badertscher hep-ex/0609059: Br(o-Ps -> unsichtbar) < 4,2e-7 (90 %), "photon mirror-photon mixing strength
      eps <= 1.55e-7 (90% C.L.)" [S Abstract].
    - Minami/Komatsu 2011.11254: beta = 0,35 +- 0,14 Grad (68 %), 2,4 sigma [S Abstract].
    - Eskilt/Komatsu 2205.13962: beta = 0,342 +0,094/-0,091 Grad, 3,6 sigma, keine Frequenzabhaengigkeit [S Abstract].
    - Kaviraj/Rychkov/Trevisani 1912.01617: PS-Vermutung "reduce in two less spatial dimensions"; "known to fail in
      some simple cases, but there is no consensus on why" [S Abstract].
    - Okun hep-ph/0606202: Spiegelteilchen "to restore the symmetry between left and right" [S Abstract].
    - Foot 1401.3965: exakte Kopie des SM, einzige neue Kopplung Photon-Spiegelphoton-Mischung eps; DM verlangt
      "eps ~ 10^-9" [S Abstract].
    - Farnes 1712.07962: negative Massen plus Erzeugung, Halos "not cuspy", "simple sign error" [S Abstract].
  - **Verletzt bzw. ueber die Vorhersage hinaus (voller Zyklus, Abschnitt 4):** V1 Garriga/Tanaka, V2 Kaplan/Sundrum,
    V3 n-n'-Anomalien, V4 Foot-eps gegen Laborgrenze.

### Abschnitt 4, laufend (Erwartungsverstoesse)

- **V1 (gross) Garriga/Tanaka hep-th/9911055 [S Abstract], PRL 84, 2778 (2000):**
  - Wortlaut: "In the case of two branes of opposite tension, linearized Brans-Dicke (BD) gravity is recovered on either
    wall"; "For the wall of negative tension, the BD parameter is always negative but greater than -3/2";
    "shadow matter from the other wall gravitates upon us"; "light deflection from shadow matter is 25 % weaker than
    from ordinary matter"; Linsenmasse von Schattenmaterie "would be underestimated".
  - Gegen E5: Die Karte sagt nur "unsere Welt auf der Brane mit negativer Spannung". Die Quelle sagt: Ohne
    Zusatzmechanismus ist die Schwerkraft auf der negativen Brane Brans-Dicke mit omega in (-3/2, 0). [L] Cassini
    verlangt omega > ~4e4; also braucht RS1 eine Radion-Stabilisierung (Goldberger/Wise [L]). Welche Brane die
    sichtbare ist, sagt keiner der zwei Abstracts -> Volltext RS1 noetig (Abruf F7 geplant).
  - Fuer Finn: "Schwerkraft auf der Rueckseite" ist hier woertlich: Materie auf der anderen Brane zieht uns an. Messbar
    wird das als Verhaeltnis Linsenmasse/dynamische Masse (Schattenmaterie lenkt Licht 25 % schwaecher ab). [ES]
    Das ist ein Unterscheidungspunkt zu gewoehnlicher dunkler Materie.
- **V2 (gross) Kaplan/Sundrum hep-th/0505265 [S Abstract], JHEP 0607:042 (2006):**
  - Wortlaut: Symmetrie "Energy -> - Energy", die Materiebeitraege zur kosmologischen Konstante unterdrueckt; "a 'ghost'
    copy of the Standard Model"; "naturalness requires General Relativity to break down at short distances with
    testable consequences"; mit Lorentz-Verletzung ist "the decay of flat spacetime by ghost production" langsam genug.
  - Gegen die Zuordnung der Leitung (RUNDE-41, Antwort 15:09: negative Parallelwelt = Spiegelwelt bzw. negative
    Brane): Die woertlich passendste Literatur zu Finns "kompletter negativer Parallelwelt, die das Gleichgewicht
    herstellt" ist eine Kopie des SM mit **negativer Energie**, nicht die Spiegelwelt (die hat positive Energie). [ES]
  - Messnah: (a) Kurzabstands-Schwerkraft (Bruchstelle der ART; Laenge im Volltext pruefen, Abruf F8 geplant);
    (b) Vakuumzerfall in Geister, begrenzt durch Cline/Jeon/Moore (Abschneider < 3 MeV) [P].
- **V3 (mittel) n-n'-Lage gegen E4 "ohne Befund":**
  - Abel u. a. 2009.11046 [S Abstract]: Nachanalysen frueherer UCN-Speicherexperimente "yielded statistically
    significant anomalous signals" (bei B' != 0); die PSI-Suche fand "no evidence"; tau_nn' > 352 s bei B' = 0, > 6 s
    fuer 0,4 bis 25,7 uT (95 %).
  - Broussard u. a. 2111.05543 [S Abstract]: 6,6-T-Suche am SNS "excludes this explanation" der Lebensdauer-Anomalie
    (Berezhiani 1807.07906: Massenaufspaltung ~1e-7 eV).
  - Korrektur: E4 haelt fuer die Spitzen-Suchen, aber es gab gemeldete Anomalien; Stand 2024-26 offen -> F3.
- **V4 (mittel) Foot-eps gegen Laborgrenze:** Foot braucht eps ~ 1e-9, o-Ps-Labor 2007 gibt eps <= 1,55e-7. [E] Faktor
  ~150. "Ohne Befund" heisst hier nicht "geprueft": Das DM-relevante eps liegt zwei Groessenordnungen unter der
  Laborreichweite von 2007. Neuer Stand -> F4.

- **F2** 17:09:14: arXiv-API all:zitterbewegung, nach Datum absteigend, 40 Eintraege (2024-03 bis 2026-09), Datei
  quellen/F2-api-zitterbewegung.xml. Abruf 3 von 12.
  - Vorhersage bestaetigt (eine Zeile): Simulatoren ja, freies Elektron nein. Guo/Xu/Gu 2511.21142: ZB "has long
    remained unobservable in free electrons due to its sub-Compton scale" [S Abstract].
  - Simulatoren mit Messung, neu seit 2024 [S Abstract]: Exziton-Polaritonen bei Raumtemperatur (Wen u. a., PRL 133,
    116903 (2024), 2405.19791); 2D-massives Dirac in Schaltkreis-QED, "rotational Zitterbewegung" (Kang u. a.
    2609.16628, 15.09.2026); photonische AdS2-Raumzeit (Himmel u. a. 2606.09501, 08.06.2026).
  - **V5 (mittel, positiv) Himmel u. a. 2606.09501 [S Abstract]:** Wellenleiter emulieren Dirac in gekruemmter
    AdS2-Raumzeit; gemessen: langsame Geodaetenschwingung plus schnelle ZB "arising from relativistic
    particle--antiparticle interference"; "the Zitterbewegung frequency exhibits a distinct joint dependence on mass
    and curvature". Erwartet hatte ich nur flache Simulatoren. Fuer Finn: Zittern und Kruemmung sind im Analog-Labor
    gekoppelt gemessen (Analogie, keine Schwerkraft).
  - **V6 (gross fuer K-AM) Wang/Ho/Chang 2609.09779 [S Abstract]:** In Dirac-Zellularautomaten kann "the rigid coupling
    between spatial and temporal resolutions ... introduce artificial phase-matching symmetries on finite grids that
    suppress interference phenomena such as Zitterbewegung". Gegen meine stille Annahme "Flip-Flop-Takt = ZB im
    Automaten": Im starren Takt kann die ZB auf endlichen Gittern kuenstlich unterdrueckt sein. [ES] Unsere QCA haben
    genau diese starre Kopplung (ein Schritt = eine Zelle). SCHACHBRETT-KAUSAL-1 sah ZB auf der Kausalmenge und im
    Kontinuum, nicht auf einem festen Gitter [P].
  - **V7 (mittel) Shen/Lu/Zhu, PRA 113, 043314 (2026), 2605.05608 [S Abstract]:** Im getriebenen SSH-Modell zeigt der
    Schwerpunkt "multi-frequency Zitterbewegung oscillations, whose spectral composition and phase are directly tied to
    the system's Floquet band structure"; Bandinversionen an topologischen Uebergaengen hinterlassen Signaturen. [ES]
    Die ZB ist damit ein Messfuehler fuer die Takt-Topologie (W3, Gegentakt) - aber fuer freie Automaten analytisch
    ableitbar ("analytically describe").
  - Aussenseiter: Rax 2405.17317, 2503.09465, 2403.07703 [S Abstract]: Erdschwere koppelt Strangeness-Oszillation an
    die ZB der Quarks; "This coupling is responsible for the observed CP violations"; Amplitude "linear with respect to
    the strength of gravity". Einzelautor, keine Zeitschrift in der API. Nach Recherchestand keine unabhaengige
    Pruefung gefunden (kein Urteil "widerlegt"). [ES] Unterscheidungspunkt: CP-Verletzung muesste mit der lokalen
    Schwerebeschleunigung skalieren.

- **F3** 17:10:10: arXiv-API "mirror neutron(s)", nach Datum, 35 Eintraege (2019-02 bis 2026-08), Datei
  quellen/F3-api-mirrorneutron.xml. Abruf 4 von 12.
  - Vorhersage "kein Signal" bestaetigt; "tau_nn' >~ 350-450 s" nur fuer B' = 0 (Abel 2021: > 352 s) [S Abstract].
  - Neu und entscheidend fuer V3 [S Abstract]:
    - Ayres u. a. (mit Berezhiani) 2602.23487, 26.02.2026: eigene PSI-Apparatur, B von 5 bis 109 uT, "No evidence of
      anomalous neutron losses"; "The parameter space, previously claimed for potential signals, has been excluded to
      99.98 %". -> V3 aufgeloest: Die gemeldeten Anomalien sind 2026 ausgeschlossen. E4 fuer n-n' damit
      eingetroffen, schaerfer als erwartet.
    - Ayres u. a. 2608.12173, 12.08.2026: nicht entartete n und n' (Massenabstand 0,3-22 peV), B 5-360 uT:
      tau_nn' >~ 20 s; teils staerker als die Neutronenstern-Kuehlschranke.
    - McKeen/Pospelov/Raj, PRL 127, 061805 (2021), 2105.09951: Heizung des kaeltesten Neutronensterns (PSR
      J2144-3933, < 40 000 K) begrenzt die n-n'-Mischung fuer Massenabstaende "19 orders of magnitude larger" als im
      Labor. Gegenrede Goldman/Mohapatra/Nussinov, EPJC 82, 945 (2022): Millildung der Spiegelteilchen kann die
      Schranke lockern. Kerbikov 2603.11930 (2026): Dekohaerenz im Stern unterdrueckt die Oszillation.
    - Mohanmurthy u. a. 2201.04191: nEDM-Daten, tau_nn'/sqrt|cos beta| > 5,7 s fuer 0,36-1,01 uT'.
    - Vorschlag Neutroneninterferometrie (Capolupo u. a. 2503.02479): geometrische Phase.
  - **Regime (Regel 1) [ES]:** Massengleich (Delta m = 0, Labor mit B'-Scan) gegen nicht entartet (Delta m bis
    peV im Labor, weit groesser nur im Neutronenstern). Die Schranken sampeln verschiedene Delta-m-Bereiche; der
    Moderator ist Delta m (dazu das unbekannte Spiegel-Magnetfeld B').

- **F4** 17:10:34: arXiv-API (positronium UND invisible) ODER "mirror photon" ODER "mirror dark matter", nach Datum, 35
  Eintraege (2021-02 bis 2026-09), Datei quellen/F4-api-positronium-mirror.xml. Abruf 5 von 12.
  - Vorhersage "kaum neue o-Ps-Messungen" bestaetigt: keine neue o-Ps-Schranke im Fenster; nur Geraetebau [S Abstract]:
    KAPAE Phase II (Jeong u. a. 2609.10259, 09.09.2026; Untergrund-Rate < ~3e-4 Hz) und J-PET-Machbarkeit
    (Medrala-Sowa u. a. 2410.00164, 2024). Badertscher 2007 bleibt nach Recherchestand die Laborgrenze (eps <= 1,55e-7).
    Einschraenkung: Das Fenster beginnt 2021-02; aeltere Nachfolger (2008-2020) sind damit nicht abgedeckt.
  - **V8 (gross) Direktsuche schlaegt o-Ps um Groessenordnungen:**
    - Raza 2409.01486 [S Abstract]: CDEX-10 "eps < 2 x 10^-10 for mirror nuclear dark matter in the 10--56 GeV mass
      range"; Projektion CDEX-300 eps < 3,75e-11 (bei Spiegel-Halotemperatur < 0,3 keV). Einzelautor, nicht in einer
      Zeitschrift laut API.
    - LZ (Akerib u. a., PRL 137, 101803 (2026), 2511.17350) [S Abstract]: "the most stringent constraints to date on
      ... mirror dark matter"; Zahl im Abstract nicht genannt.
    - Gegen Foot (eps ~ 1e-9 fuer DM) [E]: CDEX-10 liegt Faktor ~5 darunter. Foot-Spiegel-DM ist damit unter Druck,
      modellabhaengig (Halotemperatur, Zusammensetzung). Feldregel 7: nicht "widerlegt"; "nach Recherchestand unter
      Druck".
    - Korrektur von V4: Das DM-relevante eps wird heute nicht im o-Ps-Labor, sondern in Xenon-/Germanium-Detektoren
      geprueft.
  - Nebenbefund Projekt: Mandal/Shankaranarayanan 2502.00821 [S Abstract]: millionstel geladene Q-Baelle als DM, mit
    o-Ps-Grenze Q < 3,4e-5. Fuer K-AM nur Randnotiz.

- **F5** 17:11:04: arXiv-API "cosmic birefringence", nach Datum, 45 Eintraege (2025-03 bis 2026-09), Datei
  quellen/F5-api-birefringence.xml. Abruf 6 von 12.
  - Vorhersage "beta ~ 0,2-0,35 Grad bei 2-4 sigma, Kalibrierung strittig": **teils verletzt (klein):** die
    Kombination ist staerker als 4 sigma.
    - ACT DR6 (Diego-Palazuelos, Komatsu u. a. 2509.13654, PRD angenommen): beta = 0,215 +- 0,074 Grad, 2,9 sigma;
      "systematics ... not understood" [S Abstract].
    - Eskilt 2608.06480 (06.08.2026): Planck PR4 + ACT DR6 gemeinsam beta = 0,277 +- 0,057 Grad, 4,8 sigma; mit
      Staubschutz 3,5 sigma; beta = 0 verlangte, dass Staubmodell und Instrumentenprior zugleich versagen [S Abstract].
    - Lonappan/Keating, ApJL 1009, L12 (2026), 2609.09149: blinder Differenztest bestaetigt das Kalibriermuster;
      "rather than an independent-data confirmation"; beta = 0,37 +- 0,12 Grad [S Abstract].
    - BICEP/Keck XXI (2603.06812): skalenabhaengiges beta(l) mit Null vertraeglich, Fehler < 0,15 Grad [S Abstract].
    - Battye/Jackson/Browne (PRL im Druck, 2607.02664): Radioquellen mu_beta = 0,2 +- 1,0 Grad; ~0,1 Grad mit ~1e5
      Quellen moeglich [S Abstract].
    - LiteBIRD-Prognose (de la Hoz u. a. 2503.22322): 0,3 Grad mit 5 bis 13 sigma [S Abstract].
    - Kalibrierung: SO-Drahtgitter 0,08 Grad; LAT 0,10, Planck 0,17 Grad ueber Kreuzkalibrierung (Rigouzzo u. a.
      2606.11300); "standard self-calibration approaches assume vanishing isotropic cosmic birefringence" [S Abstract].
  - **Regime (Regel 1) [ES]:** Moderator ist die Winkelkalibrierung: Analysen mit Vordergrund-Kalibrierung (MK-Art)
    finden beta ~ 0,2-0,35 Grad; Selbstkalibrierung setzt beta = 0 voraus und kann es nicht sehen. Unterscheidungspunkt:
    absolute Hardware-Kalibrierung besser als ~0,1 Grad (SO-Drahtgitter, POLOCALC) oder Radioquellen mit ~1e5
    Objekten.
  - Bezug Finn [ES]: beta != 0 hiesse, der kosmische Hintergrund bevorzugt eine Drehrichtung (Paritaet im dunklen Sektor
    gebrochen). Eine exakte Spiegelsymmetrie der Gesetze verbietet das nicht (spontan gebrochener Hintergrund); ein
    direkter Test der Spiegelwelt ist es also nicht.

- **F6** 17:11:36: arXiv-API "Parisi-Sourlas" ODER (dimensional reduction UND random field), nach Datum, 30 Eintraege
  (2020-05 bis 2026-08), Datei quellen/F6-api-parisisourlas.xml. Abruf 7 von 12.
  - Vorhersage "DR gilt nahe d = 6, bricht unter d ~ 4-5" bestaetigt, mit Zahl [S Abstract]:
    - Tarjus/Tissier/Balog, SciPost Phys. 19, 001 (2025), 2411.11147: SUSY und DR brechen unter d_DR(N); fuer das RFIM
      "around 5.11 +- 0.09" (nichtperturbative FRG); nicht in eps = 6 - d sichtbar.
    - Kaviraj/Rychkov/Trevisani 2009.10087: zwei Stoerungen werden relevant unter "d_c ~ 4.2 - 4.7"; KRT, PRL 129,
      045701 (2022): RF-phi^3 behaelt SUSY, RF-phi^4 nicht unter d = 5 ("new relevant SUSY-breaking interactions").
    - Rychkov 2303.09654: RFIM verliert SUSY und DR "somewhere between 4 and 5 dimensions", verzweigte Polymere
      behalten sie "in any d".
    - Le Floch/Patashuri/Trevisani, SciPost Phys. 21, 039 (2026): neuer Beweis der DR ueber Q-Kohomologie und
      Lokalisierung.
  - **V9 (mittel, positiv, fuer K-AM) Gorsky/Kazakov/Levkovich-Maslyuk/Mishnyakov 2210.07176 [S Abstract]:**
    "matrix-forest theorem and the Parisi-Sourlas trick" -> "massive spinless fermions on dynamical planar graphs",
    "a lattice version of 2d quantum gravity"; Fluss zwischen "c=-2 (large trees regime) and c=0 (small trees regime)".
    [ES] Hier ist die "Negativdimension" ein Fermion auf einem dynamischen Netz, und ihr Beitrag ist negativ
    (c = -2). Das ist die naechste Literatur zu "Flip-Flop in einer Negativdimension auf einem Netz", und sie ist exakt
    loesbar, aber in 2D.
  - **Regime (Regel 1) [ES]:** Moderator Dimension d (und Wechselwirkungsart): oberhalb d_DR ~ 5,1 zaehlen zwei
    Grassmann-Richtungen exakt wie -2; darunter nicht. Fuer d = 3 (Labor, verduennte Antiferromagneten [L]) gilt die
    Aufhebung nicht.

- **F7** 17:12:15: RS1-Volltext hep-ph/9905221v1 (9 S.), quellen/F7-RS1-hep-ph-9905221.pdf und .txt (pdftotext
  -layout). Abruf 8 von 12.
  - Vorhersage "sichtbare Brane mit negativer Spannung" bestaetigt (eine Zeile): Gl. (11) "Vhid = -Vvis = 24M^3 k,
    Lambda = -24M^3 k^2" (txt Z. 185); Vvis ist die "vacuum energy" der sichtbaren Brane (Z. 121, 126); die
    SM-Felder sitzen auf ihr (Z. 258-261, 282) [S]. Das Wort "tension" steht nicht im Text; RS sagen "vacuum energy".
  - Dazu [S]: "The compactification radius rc is effectively an arbitrary integration constant" (Z. 199-200), also
    ohne Stabilisierung. Zusammen mit V1 (Garriga/Tanaka) [ES]: Ohne Stabilisierung (Goldberger/Wise [L]) gibt die
    negative Brane Brans-Dicke mit omega in (-3/2, 0), unvereinbar mit Cassini (omega > ~4e4 [L]).

- **F8** 17:12:35: Kaplan/Sundrum hep-th/0505265v2 Volltext (18 S.), quellen/F8-KaplanSundrum-hep-th-0505265.pdf und
  .txt. Abruf 9 von 12.
  - Vorhersage (aus V2): Bruchstelle der ART bei der Dunkle-Energie-Laenge, Geister-Zerfall durch Lorentz-Verletzung
    gebremst -> **bestaetigt, mit Zahlen; dazu ein Verstoss (V10).**
  - Zahlen [S]:
    - "naturalness implies mu <~ 2 x 10^-3 eV" (Gl. 16); "1/mu ~ 100 microns"; "A more refined estimate ... gives a
      minimal breakdown length of 30 microns [2]" (Ref. 2 = Sundrum, PRD 69, 044014 (2004)); damals "probed gravity
      down to 200 microns" (txt Z. 272-278).
    - Vorbehalt: Koppelt die Abschneide-Physik nicht an SM-Materie, dann Vorhersage "1/mu ~ 1/(10MeV) ~ 10 fm"
      (Gl. 18, Z. 330-346).
    - Vakuumzerfall in Photonen und Geister ~2e-92 je cm^3 und 10 Gyr bei mu = 2e-3 eV (Gl. 28); im
      Hoehenstrahlungs-Untergrund sichtbar erst ab mu >~ MeV (Z. 461-464).
    - Gravitative Lorentz-Verletzung ist Pflicht; induzierte Tempo-Verschiebung sichtbarer Materie <~ 1e-60
      (Z. 627-636).
  - **V10 (gross) Bondi steht hier an einer Primaerquelle, als Folge der Geisterkopie** (KS Abschn. 6, Z. 486-525) [S]:
    "if a ghost particle is brought near the Earth it will fall towards the ground"; "A ghost mass and a visible mass
    will be repelled from each other, however, if the ghost mass dominates"; "The gravitational force between two
    ghosts is also repulsive"; bei m1 = -m2 "the matter-ghost system spontaneously accelerates"; Abstrahlung
    "speeds them up". Gegen Finns "Tuch auf der Rueckseite zieht an": Eine negative Welt, die Energie ausgleicht,
    stoesst ab, statt anzuziehen. [ES]
  - **Messnah, aus dem Projekt dazu (lokale Kopie, kein Abruf):** Adelberger u. a., PRL 98, 131104 (2007),
    dd-spuren/quellen/Adelberger-2007-raw.txt Z. 220-283 [S lokal]: Sundrums "fat graviton" (die Abschneide-Physik
    dieses Szenarios) "Sundrum argues that naturalness requires lg >= 20 um. Our results require lg <= 98 um at 95%
    confidence." Lee 2020 nennt Sundrum 2004 nur fuer die Dunkle-Energie-Laenge ~85 um (lee2020-eprint
    FB_ISL_pdf.tex Z. 38), ohne Fat-Graviton-Anpassung (grep "fat": kein Treffer) [S lokal].
    - [ES] Fenster fuer die Geisterkopie: 20 um <= lg <= 98 um (Stand 2007). Juengere Daten (Lee 2020, Yukawa bis
      38,6 um) sind nach Recherchestand nicht auf diese Form ausgewertet. Unstimmigkeit klein: KS nennen 30 um,
      Adelberger zitiert 20 um, beide aus Sundrum 2004.

- **F9** 17:14:08: arXiv-API abs:Farnes ODER (ti:"negative mass" UND abs:cosmology), nach Relevanz, 17 Eintraege,
  Datei quellen/F9-api-farnes-negmass.xml. Abruf 10 von 12.
  - Vorhersage (E6 "umstritten") bestaetigt, schaerfer [S Abstract]:
    - Socas-Navarro, A&A 626, A5 (2019), 1902.08287: Halo-Form und -Dichte "incorrect"; Halos muessten leichter sein
      als die Baryonen; "a large-scale version of the `runaway' effect, which would result in all galaxies moving in
      random directions at nearly the speed of light".
    - Stepanian, MPLA 34, 1975002 (2019), 1903.06037: widerspricht "both the essence of the General Relativity and the
      available observational data".
    - Najera u. a., A&A 651, L13 (2021), 2105.11041: Feinabstimmung noetig.
    - Im 24-Monats-Fenster keine Verteidigung von Farnes in diesem Abruf (Feldregel 7: "nach Recherchestand nicht
      gestuetzt", nicht "widerlegt").
  - Neu und passend zu Finns "Ausgleich" [S Abstract]:
    - Manfredi/Rouet/Miller (2601.22910, 30.01.2026): Kosmos mit "equal amounts of positive and negative Bondi masses";
      gemischte Konfigurationen "always unstable"; Beschleunigung durch "stable positive/negative mass pairs"
      (Bondi-Paare). Vorlaeufer Dirac-Milne-Universum (Manfredi u. a., PRD 98, 023514 (2018)).
    - Luminet (Inference 8(4), Sept. 2026; 2609.26834): Sakharov-Zwillingsuniversen, Janus, Bimetrik; "no-go results
      for positive- and negative-mass sectors"; "a substantial burden of mathematical and observational proof".
    - Takahashi/Asada (ApJL 2013; 1303.1301): SDSS-Linsensuche, kompakte negative Massen n < 1e-8 (1e-4) h^3 Mpc^-3
      fuer |M| > 1e15 (1e12) Sonnenmassen, |Omega| < 1e-4 im Galaxienbereich. Messnahe Schranke.
  - [ES] Dirac-Milne setzt negative Schwermasse der Antimaterie voraus; ALPHA-g 2023 sah Antiwasserstoff fallen
    (Nature 621, 716; im Projekt [P] grid-time-field-review-20260907/motion-energy-gravity.md Z. 48-53 und
    literatur-20260922/... Z. 182 "auf 25 % beantwortet"). Volltext ALPHA-g hier nicht gelesen.

## 7. Gegensweep (Phase 1, ab 17:14:56): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 "Spiegelwelt = exakte Kopie mit gleichen Massen und gleicher Temperatur." Geprueft ohne Abruf (Abstracts aus F3/F4):
  - Beauchesne/Kats (JHEP; 2109.03279) [S Abstract]: Die Kosmologie des Mirror Twin Higgs "requires the breaking of
    the Z2 symmetry" (offen: explizit oder nicht); Probleme N_eff und Spiegelatom-Anteil.
  - Chacko/Curtin/Geller u. a. (2104.02074) [S Abstract]: Spiegel-DM als Teilkomponente, Spiegelfermionen
    "sub-nano-charged" durch kinetische Mischung; Halo oder Scheibe (dissipativ).
  - Ausgang: Die exakte Kopie ist nicht der Arbeitsstand. Aktiv ist der weich gebrochene Spiegel (Twin Higgs), mit
    LHC-Bezug (Higgs-Kopplungen [L]) und kosmologischem N_eff-Druck. **Erwartungsverstoss V11 (mittel) gegen E4:**
    "nur ueber Schwerkraft und schwache Mischung" gilt fuer Foot; beim Twin Higgs koppelt zusaetzlich das Higgs-Portal
    [L, Abstract 2104.02074 nennt nur kinetische Mischung].
- G2 "Negativ heisst raeumlich daneben (Brane) oder energetisch negativ." Nicht geprueft war die zeitliche Lesart:
  Universum vor dem Urknall als CPT-Spiegel (Boyle/Finn/Turok [L]) bzw. Sakharovs Zwillingsuniversum (Luminet 2026
  [S Abstract, F9]). Pruefung per F10.
- G3 "Der Dirac-See ist nicht messbar." Im Festkoerper ist der See woertlich das gefuellte Valenzband; Klein-Tunneln
  und Schwinger-artige Paarbildung in Graphen [L]. Ungeprueft (kein Abruf mehr frei), als [L] markieren.
- G4 "ZB ist eine echte Bewegung des Elektrons." Mit dem Foldy-Wouthuysen- bzw. Newton-Wigner-Ort verschwindet sie
  fuer freie Teilchen; ihre messbare Spur in Atomen ist der Darwin-Term [L]. Lokal nur Stichprobe: F2 enthaelt eine
  Arbeit zur Frage "Dirac or the Foldy-Wouthuysen density" (2501.06518, Z. 678 der XML) [S Abstract, nur Fragestellung].

- **F10** 17:15:15: arXiv-API id_list 1803.08928, gr-qc/0602076, hep-ph/0506256, hep-ph/0312335, 1610.01142; Datei
  quellen/F10-api-idlist-gegensweep.xml (5 Eintraege, alle IDs treffen). Abruf 11 von 12.
  - Vorhersage: BFT sagen masseloses leichtestes Neutrino und keine primordialen Wellen voraus; tHN bilden E -> -E
    komplex ab; Twin Higgs schuetzt die Higgs-Masse; Berezhiani T' < T; Foster/Jacobson 4D-Schachbrett mit Spin.
  - Bestaetigt [S Abstract]:
    - Boyle/Finn/Turok, PRL 121, 251301 (2018): "the universe after the big bang is the CPT image of the universe before
      it"; "a universe/anti-universe pair"; stabiles rechtshaendiges Neutrino als DM, "4.8 x 10^8 GeV"; Vorhersagen:
      Majorana-Neutrinos (0nubb), "the lightest neutrino is massless", "no primordial long-wavelength gravitational
      waves". -> G2 geprueft: Die zeitliche Lesart der "negativen Parallelwelt" ist Literatur mit drei messnahen
      Vorhersagen.
    - 't Hooft/Nobbenhuis, CQG 23, 3819 (2006): ohne Rand- und Hermitezitaetsbedingungen "as many negative as positive
      energy states, which are related by transformations to complex space"; loest das Lambda-Problem "not directly".
      [ES] Das ist Finns "invertierte Dimensionsebene" am woertlichsten.
    - Chacko/Goh/Harnik, PRL 96, 231802 (2006): Spiegel-SM schuetzt die schwache Skala "up to scales of order 5 - 10
      TeV"; ohne neue leichte SM-geladene Teilchen.
    - Berezhiani, IJMPA 19, 3775 (2004): "nucleosynthesis bounds demand that the mirror world should have a smaller
      temperature"; Spiegelbaryonen als dominante DM moeglich.
  - **V12 (gross, gegen E2 und fuer K-AM) Foster/Jacobson 1610.01142 "Spin on a 4D Feynman Checkerboard" [S Abstract]:**
    Weyl-Gleichung "on a time-diagonal, hypercubic spacetime lattice with null faces"; Schrittamplitude rechtshaendig
    = Spinprojektor in Schrittrichtung, linkshaendig der orthogonale; Pfadamplitude i^(+-T) 3^(-B/2) 2^(-N);
    **"Fermion doubling does not occur in this discrete scheme."**; "A Dirac mass m introduces the amplitude i eps m to
    flip chirality in any given time step eps".
    - Gegen E2 ("3+1 nicht einfach"): Es gibt eine 4D-Fassung mit Spin, ohne Verdopplung, und der Faktor i eps m wirkt
      dort als Chiralitaets-Flip je Zeitschritt.
    - Gegen CHIRAL-L/QCA-WINDUNG-1 (Verdopplung als Regel auf unseren Netzen) [ES]: Wie das ohne Widerspruch zu
      Nielsen/Ninomiya geht, sagt der Abstract nicht. Vermutung [H]: Produkte von Projektoren sind nicht unitaer
      (Faktoren 2^(-N), 3^(-B/2)), und NN setzt Unitaritaet bzw. Hermitezitaet voraus. Volltext noetig -> F11.

- **F11** 17:15:58: Foster/Jacobson 1610.01142v1 Volltext, quellen/F11-FosterJacobson-1610.01142.pdf und .txt
  (pdftotext meldete einen xref-Fehler und rekonstruierte; Text vollstaendig lesbar, 869 Zeilen). **Abruf 12 von 12;
  Budget erschoepft.**
  - Vorhersage (V12): Doppler-Freiheit durch Nicht-Unitaritaet -> **bestaetigt, mit zwei Zusaetzen.** [S, Zeilen der
    txt]:
    - 1+1 nach Feynman: Pfadamplitude "(i eps m)^R", R = Zahl der Richtungsumkehrungen (Z. 60-66). -> E2-Teil 1 an
      einer Primaerquelle bestaetigt (Feynman/Hibbs selbst nicht gelesen).
    - Gitter: Hyperwuerfel mit Zeit auf der Diagonale, Schrittgeschwindigkeit 3c; raeumlich fcc; ein Schritt fuehrt vom
      Mittelpunkt eines Tetraeders zu seinen vier Ecken; nach vier Schritten ist das Gitter wieder dasselbe
      (Z. 92-170).
    - Reelle Frequenzen nur exakt wie im Kontinuum, aber nur entlang vier Nullrichtungen; alle anderen Moden gedaempft,
      groesster unphysikalischer Eigenwert 1/sqrt(3) je Schritt (Z. 238-321).
    - NN-Umgehung: "the lack of a local action is our proposed explanation for how the fermion doubling is evaded"
      (Z. 326-332).
    - Masse: "an amplitude i eps m to swap chiralities at each step" (Z. 594-595). **Zusatz 1 (fuer K-AM gross):** In
      der eleganten Fassung "Adopt now a spatial, body-centered cubic (bcc) lattice"; "The eight steps from each lattice
      point to the corners of the surrounding cube can be grouped into two tetrahedral sets of four. Call them the R
      steps and the L steps"; L nimmt "the opposite steps with the same spin" (Z. 612-623). [ES] Das ist woertlich
      Finns Flip-Flop zwischen Auf- und Ab-Tetraeder, und die Literatur nennt ihn: Dirac-Masse.
    - **Zusatz 2:** "our scheme has a serious flaw: the discrete propagator is not unitarity"; Norm halbiert sich je
      Schritt aus einem Punkt; dagegen "one can write a unitary discrete evolution rule on a body centered cubic lattice
      whose continuum limit is the Weyl equation", Ref. [11] (Z. 727-741). [ES] Unitaer (unsere QCA, Ref. [11]) heisst
      Doppler, also Spiegelpartner bzw. Gegentakt (CHIRAL-L, QCA-WINDUNG-1 [P]); nicht unitaer (FJ) heisst keine
      Doppler, aber Normverlust. Zusammen: **Spiegel oder Verlust.**
    - Anwendung auf chirale Eichtheorien: "makes any directly useful application in its present form seem unlikely"
      (Z. 718-726).

## 7b. Gegensweep Phase 2 (nach dem letzten Abruf, ab 17:17)

- G5 "Die Kurzabstands-Schranken gelten fuer das Vorzeichen, das die Negativseite braucht." Geprueft im Projekt
  (STELLE-24M V1 [P]): Lee 2020 zeigt nur |alpha|, +alpha/-alpha getrennt nur im nicht abrufbaren Supplement. Die
  Geisterkopie (Fat Graviton) und die dunkle Blase **schwaechen** die Schwerkraft; fuer beide gibt es eigene Formen
  (Adelberger 2007: Fat Graviton lg <= 98 um; Potenzterm k = 3, Blase L <= 9,3 um) [P]. Ausgang: Die Yukawa-Zahl
  38,6 um darf man nicht ungeprueft auf die Geisterkopie uebertragen.
  Bewegung des Raums mit Fluchtgeschwindigkeit (FLUSS-ZITTER-1 [P]); dort reines Chaos ohne Fluss durch EHT
  ausgeschlossen (+84 % Schatten) [P]. Ausgang: zwei verschiedene Zittern, nicht verwechseln.
- G7 "Bondi 1957 ist die Quelle fuer das Davonlaufen." Bondi selbst nicht gelesen. Primaer gelesen ist dieselbe
  Mechanik bei Kaplan/Sundrum Abschn. 6 [S] und das Davonlaufen als kosmologisches Problem bei Socas-Navarro
  [S Abstract]. Ausgang: E6 inhaltlich an Primaerquellen belegt, Bondi selbst [L].
- G8 "Die n-n'-Schranken gelten fuer jede Spiegelwelt." Nein: sie setzen nahezu gleiche Massen (Delta m bis peV) und ein
  bestimmtes Spiegel-Magnetfeld B' voraus (F3 [S Abstract]). Fuer stark gebrochene Spiegel (Twin Higgs) gelten sie
  nicht direkt [ES].
- Nicht geprueft (Budget): ALPHA-g-Zahl an der Quelle; LZ-Zahl fuer Spiegel-DM (nur "most stringent"); Graphen-Analoga
  des Dirac-Sees; neuere o-Ps-Schranken vor 2021; Antworten auf Langhoff/LRR nach dem 02.10.

## 8. Nach dem Budget: Projektabgleich (ohne Abruf)

- **Selbstanzeige:** Foster/Jacobson war im Projekt schon bekannt. RUNDE-39.md Z. 60-63 (SPIN-KAUSAL-L):
  "3+1-Weyl-Schachbrett mit Spin auf tetraedrischen Lichtschritten, ohne Doppler, nicht unitaer; fuer die Masse BCC";
  dazu [H, nicht gegengelesen]: Die Einbahn-Regel aus QCA-DIAMANT-4 Teil B (v = 1/3) sei deren unitaere Erweiterung.
  Mein Projekt-grep vor den Abrufen suchte "zitterbewegung, Grassmann, Randall, Bondi, mirror ..." und nicht
  "Foster/checkerboard"; F10/F11 haben das teils doppelt geholt. Neu gegenueber RUNDE-39 sind nur die Volltextstellen
  (NN-Umgehung durch fehlende lokale Wirkung, Normhalbierung, Ref. [11] Bialynicki-Birula PRD 49, 6920 (1994),
  hep-th/9304070, als unitaere BCC-Regel).
- **QCA-DIAMANT-4 ERGEBNIS (Teil B, BCC, 4 Zustaende, Gruppe T) [P]:**
  - Treffer haben die Form W(k) = C S_+-(k) (Muenze mal Einbahn-Verschiebung entlang der vier Tetraeder-Richtungen);
    T:2+2' und T:2+2'' haben "zwei Weyl-Kegel, projektiv", v = 1/3; "in jedem der 73 Treffer haben die beiden
    Weyl-Kegel entgegengesetztes Vorzeichen. Sie liegen bei verschiedenen Eigenphasen von W(0) (auf 2 und auf 2')";
    Doppler an H, P, P' (je zwei Weyl-Kegel entgegengesetzter Chiralitaet); T:2+2 ohne Loesung (D_min 4/45).
  - Spurformel: auf Komponente 2 gilt <a|P_2|a> = 1/2, |<a|P_2|b>|^2 = 1/12 -> v = 1/3 [P, M].
  - [ES] Normiert sind das Ueberlappungen 1/3 = |<n_i|n_j>|^2 der vier FJ-Tetraeder-Spinoren; das passt zur
    RUNDE-39-Lesart (FJ = Kompression der Einbahn-Regel auf Komponente 2) und zu FJ "step speed ... three times the
    speed of light" (F11 Z. 92-95). Nicht gegengelesen.
  - **[ES] Damit "Spiegel oder Verlust" an Projektdaten:** In der unitaeren Fassung sitzt der Partner entgegengesetzter
    Chiralitaet in der Nachbarkomponente 2' und bei einer anderen Taktphase (Eigenphase von W(0)); in FJ (nur
    Komponente 2, nicht unitaer) fehlt er, dafuer geht Norm verloren.
  - [M, Skizze, nicht gegengelesen] 2 und 2' sind inaequivalente Darstellungen; nach Schur gibt es keinen
    T-symmetrischen konstanten Kopplungsterm zwischen ihnen. Ein Dirac-Massenterm (Finns Flip-Flop zwischen den beiden
    Haelften) waere dann nur mit Symmetriebruch oder in 2+2 moeglich, und 2+2 hat in Teil B keine Loesung [P].
    Gegen QCA-DIRAC-T-1 pruefen (Leitung).

## 9. Kartenwahl und eigene Herleitung (nach date 17:25:26)

- **[M, nicht gegengelesen] FJ = Kompression der Einbahn-Regel auf Komponente 2.** Mit den vier FJ-Spinoren |n_a>
  (Spin entlang der Tetraeder-Richtung n_a) sei V = (1/sqrt2) Sum_a |n_a><a| : C^4 -> C^2.
  - V V^+ = (1/2) Sum_a |n_a><n_a| = 1, weil Sum_a n_a = 0. V^+ V ist ein Projektor vom Rang 2 mit <a|V^+V|a> = 1/2 und
    |<a|V^+V|b>|^2 = (1/4)(1 + n_a.n_b)/2 = 1/12. Das sind genau die Werte, die QCA-DIAMANT-4 fuer P_2 meldet [P].
  - V S_+(k) V^+ = (1/2) Sum_a e^{i k.h_a} P_a = FJ-A(theta) mit theta_a = k.h_a (FJ Gl. 15, F11 Z. 260-262).
  - Die Muenze ist im Kommutanten, auf 2 nur eine Phase [P]; also P_2 W P_2 = e^{i alpha} V^+ A V.
  - Folge: FJ iteriert die Kompression, d. h. die Haelfte 2' wirkt als vollkommene Senke. In der unitaeren Regel
    fliesst die Amplitude von 2 nach 2' und zurueck; dort sitzt der Partner entgegengesetzter Chiralitaet bei der
    Eigenphase beta von W(0). Mit beta = pi saesse er im Gegentakt.
  - Die Vereinigung der vier zeitversetzten fcc-Gitter von FJ ist ein bcc-Gitter, die Schritte sind dessen T+-Satz
    [M, Kopfrechnung]; passt zu QCA-DIAMANT-4 Teil B (bcc, S_+).
- **Kartenwahl:**
  - ~~GEISTER-FENSTER-1 (Neufit der Eot-Wash-Daten 2020 fuer Sundrums fat graviton)~~ gestrichen (Eintrag 17:27:16, date) als
    Vorschlag: Die grobe Kopfrechnung [E, roh] gibt ~60 um (gleiche Abweichung wie die Yukawa-Grenze am kleinsten
    Abstand 52 um); dieselbe Methode gibt fuer 2007 75 um statt veroeffentlichter 98 um (Faktor 1,3). Hochgerechnet
    ~80 um. Der qualitative Ausgang "Fenster 20 bis ~80 um bleibt offen" ist damit fast vorab ableitbar, und die
    Rechnung braucht Apparateantwort und Daten, die nicht offen liegen (Lee-2020-Supplement HTTP 401 laut STELLE-24M).
    Bleibt als offene Frage.
  - Gewaehlt: SPIEGEL-HAELFTE-1 (Teil A Schreibtisch und Gegenleser, Teil B kleiner Lauf mit Unordnung im Takt der
    verborgenen Haelfte). Ableitbarkeitsprobe im DOSSIER.
- **Kalibrierungs-Warnung:** Meine Sicherheit, dass Finns Flip-Flop "die Dirac-Masse ist", ist im Lauf gestiegen, ohne
  neue Messdaten. Es ist eine genaue Zuordnung im Modell (FJ, QCA-DIRAC-T-1), keine Aussage ueber die Natur.

## 6. Offene Rueckfragen (Stand Abgabe)

- An Finn: Was heisst "negativ"? (a) negative Energie (Geisterkopie: stoesst ab, gleicht Vakuumenergie aus),
  (b) gespiegelte Haendigkeit (Spiegelwelt: zieht an, dunkle Materie), (c) Gegentakt (Phase pi im Netz),
  (d) zeitgespiegelt (CPT-Universum vor dem Urknall). Je Lesart andere Tests.
- An die Leitung: Teil A der Karte (FJ = Kompression) frisch gegenlesen lassen, bevor er in den Weichenstand geht.

## 10. Abgabe

- DOSSIER.md geschrieben ab 17:27:32 (date). Rueckwaertsdurchgang: Zahlen gegen die Abstracts bzw. Volltextzeilen
  geprueft; berichtigt: Speichervolumen 1,47 m^3 gehoert zu 2111.02794 (nicht 2602.23487); BICEP/Keck "Fehler
  < 0,15 Grad"; absolute Saetze im Ergebnis und in "Einfach gesagt" abgeschwaecht ("hier gelesene", "in den
  geprueften Bereichen", "entspricht", "noch nicht gegengelesen"); Betragsstriche in Tabellen durch abs() ersetzt.
- Nummern der Verstoesse im DOSSIER nach Gewicht neu vergeben (Zuordnung dort in Abschnitt 2).
- Abgabezeit (date): 17:33:42
