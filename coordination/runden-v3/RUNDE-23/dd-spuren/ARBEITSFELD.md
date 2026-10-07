# ARBEITSFELD DD-SPUREN (Runde 23) - feldforscher

- Einzige Arbeitsdatei dieser Karte (Feldregel 5). Vor jedem Schritt neu lesen. Gestrichenes bleibt mit ~~ ~~ stehen.
- Agentenstart 2026-10-02 21:24:29 CEST (date). Strategie geschrieben ab 2026-10-02 21:25:55 CEST (date), vor dem
  ersten Abruf.
- Zeitbox 75 min ab Start, also bis 22:39 CEST (aus dem Start gerechnet, nicht geschaetzt).
- Marken: [S] gelesen, [L?] nur Abstract/Zitat, [H] eigene Schlussfolgerung, [E] Kopfrechnung
  (hbar c = 1,973e-7 eV m).
- Quellkopien: `quellen/` in diesem Ordner (nicht im Scratchpad).

## 0. Gelesene Projektquellen (nur zur Einordnung)

- KARTE.md (ganz): fuenf Fragen, E1-E4, Bedeutung.
- RUNDE-22/dunkel-zeit/ERGEBNIS.md und ARBEITSFELD.md: Langhoff arXiv:2610.01825 (dort "01.10.2026"),
  Lee/Randall/Riojas arXiv:2609.36234 (dort "28.09.2026"), Danielsson/Giri arXiv:2606.20942; MVV 2205.12293;
  GMOV 2209.09249; Law-Smith u. a. 2307.11048; Hardy/Sokolov/Stubbs 2510.18975; Anchordoqui/Antoniadis/Luest 2501.11690;
  Schwarz 2403.12899; Bedroya/Obied/Vafa/Wu 2507.03090; Braun u. a. 2606.19440; alpha = 8/3 fuer einen Kreis
  (Adelberger/Heckel/Nelson 2003); MVV-Laborgrenze "around 30 um".
- RUNDE-22/stelle-24m/ERGEBNIS.md: Lee 2020 |alpha| = 1 bei < 38,6 um; Venugopalan 2024/26 alpha ~ 1e6-1e7 bei 5-100 um;
  Murata u. a. 2605.18212 Uebersicht; Vorzeichen nur im Supplement.
- WARUM-SPIN-2.md, Nachtrag 2026-10-02 19:24:11 zu Glied 10: Stelle-Richtung schwach gemessen; Zwei-Term-Regime.
- **Auffaelligkeit vor dem Abruf:** Die KARTE nennt "Langhoff (28.09.2026)" und "Lee/Randall/Riojas (01.10.2026)";
  DUNKEL-ZEIT nennt die Daten umgekehrt (und die arXiv-Nummern 2609.* vs. 2610.* passen zu DUNKEL-ZEIT). Pruefung
  in Block A1 ueber die API-Felder published/updated.

## 1. Suchstrategie (vor dem ersten Abruf)

Kanaele: arXiv-API (export.arxiv.org/api/query, per curl fuer Wortlaut), arXiv-Volltexte (pdf -> pdftotext, html),
Semantic Scholar Graph-API (citations), INSPIRE-HEP-API (refersto, schnell bei hep-ph), OpenAlex (cited_by).
WebSearch ist erschoepft.

| Block | Frage | Ziel | Abfragen (geplant) |
|---|---|---|---|
| A | 1, Daten | Metadaten beider Preprints (Daten, Versionen, Kommentare, Autoren) und Volltexte | API id_list=2610.01825,2609.36234,2606.20942; PDF beider Arbeiten -> pdftotext; grep Annahmen, Schranken, "assume", "warp", "flat", "branching", "neutrino", "reheating", "Note added" |
| B | 2 | angreifbare Annahmen; Varianten, die entgehen | aus dem Volltext; dazu Danielsson/Giri (Blase), gewarpte Dark Dimension, andere DM (PBH, fuzzy DM, sterile Neutrinos, 5D-Schwarze-Loecher) |
| C | 3 | Reaktionen | Semantic Scholar citations fuer beide IDs; INSPIRE refersto:arxiv:...; arXiv all:"dark dimension" nach Datum (50); arXiv au:Vafa, au:Anchordoqui, au:Antoniadis, au:Lust/Luest, au:Gonzalo, au:Noble jeweils mit "dark dimension" nach Datum |
| D | 3 | juengste Schranken anderer Art mit Datum | arXiv-Abfragen "dark dimension" AND (neutron star / supernova / SN1987A / collider / CMB / BBN / neutrino oscillation / gamma); Hardy/Sokolov/Stubbs 2510.18975; Reig/Ruiz 2510.25832; Petretti 2411.03459 |
| E | 4 | Laborpruefbarkeit < 10 um, geplante Empfindlichkeit | arXiv "Casimir" AND "Yukawa" AND (isoelectronic OR "Casimir-less"); Chen u. a. 2016 (IUPUI); CANNEX; Stanford levitierte Kugeln (Venugopalan, Blakemore); Manley Mikro-Torsion 2406.13020; Geraci 2010 Projektion; Murata 2605.18212 Text |
| F | Gegensweep | Arbeiten, die den Schranken widersprechen oder Varianten retten | arXiv "warped" AND "dark dimension"; "dark dimension" AND (rescue OR evade OR loophole); "Kaluza-Klein graviton" AND decay AND threshold; Randall-Begleitarbeit (au:Randall nach Datum) |

Abgrenzung: keine Rechnung ausser Kopfrechnung; keine Laeufe; Zitate unter 15 Woertern.

## 2. Meine Vorab-Bilder (aus Gedaechtnis und DUNKEL-ZEIT, damit Verstoesse sichtbar werden)

- VB-1 (Langhoff, zu E2): Nahe der Schwelle sind Zerfaelle KK-Graviton -> leichteres KK-Graviton + Graviton d-Welle
  (Rate ~ p^5). Zweites Standbein: Freeze-in-KK-Gravitonen aus dem SM-Plasma bei T_RH >= ~6 MeV zerfallen in Photonen
  -> MeV-Gamma-Schranken -> R <~ 0,2 um. Angreifbar erwarte ich: (i) flache Geometrie, (ii) Photon-Verzweigungsverhaeltnis
  (zusaetzliche unsichtbare Kanaele, z. B. in Bulk-Neutrinos, wuerden die Gammaschranke schwaechen), (iii) Mindest-T_RH
  aus BBN, (iv) Brane-Kopplung (Standard-1/M_Pl).
- VB-2 (Lee/Randall/Riojas, zu E3): Die Unterdrueckung (q/m_n)^2 folgt aus 5D-Diffeomorphismusinvarianz (Ward-artig)
  und trifft jede Kaskade; Ziel ist das GMOV-DM-Szenario; die Existenz der Dimension wird nicht angegriffen; eine
  Begleitarbeit zu gewarpten Varianten ist angekuendigt.
- VB-3 (Reaktionen, zu E1): 1-4 Tage nach Einreichung keine Antwort; hoechstens Querzitate (Langhoff zitiert LRR).
  INSPIRE kennt 0-2 Zitate.
- VB-4 (Labor, zu E4): Beste Schranken bei 1-10 um liegen bei alpha ~ 1e4-1e10 (Casimir-less/IUPUI, Stanford Kragarm,
  levitierte Kugeln). Projektionen nennen hoechstens alpha ~ 1e2-1e3 bei ~10 um; keine Gravitationsstaerke unter
  10 um innerhalb von zwei Jahren.
- VB-5 (Danielsson/Giri): Dunkle Blase gibt schwaechere Gravitation bei um (fat graviton), keinen leichten KK-Turm
  freier Gravitonen auf der Wand -> Langhoffs Freeze-in-Argument greift dort vermutlich nicht direkt [H, ungeprueft].

## 3. Abrufprotokoll (Erwartung vor jedem Abruf, dann Ausgang)

(wird fortgeschrieben)

## 4. Erwartungsverstoesse (getrennt gefuehrt)

(wird fortgeschrieben)

## 5. Gegensweep

(am Ende jeder Phase)

## 6. Offene Rueckfragen (wandern mit)

- R1 (aus DUNKEL-ZEIT): Was meint Finn mit "Seiten einer Dimension"? Unbeantwortet, nicht Teil dieser Karte.
- R2: Vorzeichengetrennte Lee-2020-Schranken (Supplement, APS-Zugang) - aus STELLE-24M, hier nur relevant fuer die
  Blasen-Variante (schwaechere Gravitation).

## 7. Gestrichenes

(noch nichts)

### Block A1 (Erwartung geschrieben 2026-10-02 21:26:36 CEST)
- A1a API id_list=2610.01825,2609.36234,2606.20942 (curl, Wortlaut): Erwartung: 2609.36234 (LRR) published 28.09.2026,
  2610.01825 (Langhoff) published 01.10.2026 (also Kartendaten vertauscht); je v1; LRR-Kommentar nennt Seitenzahl,
  evtl. Begleitarbeit; Danielsson/Giri v1 06/2026.
- A1b Volltexte beider Preprints als PDF -> pdftotext (quellen/): Erwartung: wie VB-1/VB-2.
- Ausgang A1 (eingetragen 2026-10-02 21:28:14 CEST) [S, quellen/api-A1a.xml; quellen/Langhoff-2610.01825v1-raw.txt und -layout.txt]:
  - A1a bestaetigt: LRR 2609.36234v1 published 2026-09-28T20:28:38Z, "11 pages", hep-th, Autoren Vincent S. H. Lee,
    Lisa Randall, Marcos Riojas. Langhoff 2610.01825v1 published 2026-10-01T15:01:45Z, "4 pages, 1 figure", hep-ph,
    Einzelautor Kevin Langhoff (MIT, CTP). Danielsson/Giri 2606.20942v1 2026-06-18. **Die KARTE vertauscht die Daten**
    (Langhoff ist der 01.10., LRR der 28.09.). Je nur v1, keine Fassung nach Kritik.
  - A1b Langhoff-Volltext im Kern bestaetigt (VB-1), mit drei Feinheiten:
    - Die Null an der Schwelle sei "dynamical in origin", nicht Drehsymmetrie (Z. 246-251); Herleitung ueber
      Feldumdefinition h = e^H - 1, gueltig "for all momenta and any static warped extra dimension" (Z. 351-359).
      -> Die d-Wellen-Unterdrueckung selbst gilt auch gewarpt; nur die Kaskaden-Abschaetzung nimmt "weakly warped"
      (Gl. 26, Vollstaendigkeitsschranke g^2 <= 1 + O(Delta A)) und flaches Spektrum m_n = n m_KK an.
    - Kaskade gerechnet fuer delta n = 100 (GMOV-Benchmark) und R = 0,05-0,2 um: Massenverteilung verschiebt sich bis
      zur Gleichheit Materie/Strahlung um < 0,1 % (rechte Spalte Z. 227-230 layout, zusammenhaengend; also Langhoffs
      eigene Wahl, nicht GMOV-Wert).
    - Irreduzible Schranke: Freeze-in-Abundanz rho_h/rho_DM = 1,3e-6 (T_RH/5 MeV)^3 (m_KK/5 meV)^-1 fuer
      T_RH <~ 100 MeV, uebernommen aus Ref. [33] = Langhoff/Ramos/Reig 2607.27314 (eigene, ebenfalls 2026); Zerfall
      Gamma_gg = c_n^2 m^3/(80 pi M_P^2), Gesamtbreite 9/4 Gamma_gg (nur SM-Kanaele); Daten COMPTEL (inneres
      Milchstrassengebiet, Burkert-Halo J = 1,55), COMPTEL/EGRET isotrop; Kriterium Signal > Beobachtung + 2 sigma.
      Untere Schranke T_RH >= 5,96 MeV aus Barbieri u. a. PRL 135, 181003 (2025) (BBN, CMB+BAO, 95 %).
      Ergebnis: "a viable TRH exists only for R <~ 0.2 um, mKK >~ 1 eV" (Z. 565-566).
    - Vergleichsmassstab ist R ~ Lambda^(-1/4) (~88 um), nicht der MVV-Bereich 0,1-10 um: "almost three orders of
      magnitude smaller" (Abstract). [E] 88/0,2 ~ 440. MVV-Untergrenze 0,1 um (lambda ~ 1e-3) liegt unter 0,2 um.
    - Abb. 1: graue Torsionswaagen-Flaeche "(for a brane at a fixed point)", Projektion fuer MeV-Teleskope (Faktor 10,
      AMEGO-X, e-ASTROGAM).
    - Note Added: LRR "obtains the same threshold suppression"; unabhaengig, anderer Weg; Danksagung an LRR fuer
      Diskussionen. Das ist ein Querbezug, keine Antwort der DD-Urheber.

### Block A2 (Erwartung geschrieben 2026-10-02 21:28:20 CEST)
- A2 LRR-Volltext (quellen/LeeRandallRiojas-2609.36234v1-raw.txt; Abstract, Einleitung, Schluss, Stellen "warp",
  "scalar", "Dark Dimension", "rule out", "companion", "fifth force"): Erwartung (VB-2): Rate ~ q^5 universell aus
  5D-Diffeomorphismus; Ziel GMOV-Kaskade; Existenz der Dimension nicht angegriffen; Begleitarbeit gewarpt angekuendigt;
  Rettungsversuch "kleinere Anfangsmassen" scheitert an Fuenfter Kraft und Kick-Geschwindigkeit.
- Ausgang A2 (eingetragen 2026-10-02 21:28:59 CEST) [S, quellen/LeeRandallRiojas-2609.36234v1-raw.txt]: im Kern bestaetigt (VB-2), mit
  drei Zusaetzen:
  - Ziel ist ausdruecklich das GMOV-DM-Szenario ("Cascading Graviton Dark Matter", CGDM): "the suggestion by GMOV
    [8, 9] is ruled out by decays to the Standard Model" (Z. ~153); Rate pro Kanal um (q/m_n)^4 kleiner; Kaskaden-
    Lebensdauer ~1e26 s statt 1e2-3 s (GMOV-Parameter m_KK ~ eV, delta n_max ~ 1e2, beta ~ 20); m(t) ~ t^(-2/3) statt
    t^(-2/7). Existenz der Dimension wird nicht angegriffen; keine R-Schranke.
  - Universalitaet: Skalar-induzierte KK-Verletzung und nichtminimale Kopplungen werden in einen Warp-Faktor bzw. per
    Weyl-Reskalierung absorbiert (App. A, B); Grund der Aufhebung: Gleichung des masselosen 5D-Gravitons.
    Hoehere Ableitungsoperatoren helfen nicht (App. E). Annahmen in App. F (nicht gelesen).
  - **Kleiner Verstoss:** Der Befund ist nicht neu erfunden, sondern entscheidet einen alten Streit: "resolving an
    ambiguity in the literature"; Giudice u. a. 2018 (1711.08437) fanden eine erhoehte Rate, "in disagreement with"
    de Giorgi/Vogl 2021 (2105.06794) und Bonifacio/Hinterbichler 2019 (1910.04767); weitere: Chivukula u. a. 2025
    (2411.02509, 2507.21218), Donini u. a. (2509.04580), Im/Jodlowski (2412.20913), de Giorgi/Marcoli/Silvetti 2026
    (2607.12012). Die q^5-Rate war fuer RS schon bekannt ("validating the result in [14]").
  - Rettungswege laut LRR: viel kleinere Anfangsmassen (dann Fuenfte Kraft und Kick-Geschwindigkeit); Begleitarbeit
    [24] "to appear": "warping can rescue some parameter space, but even so such models are still severely
    constrained" (alternatives RS-Szenario); KK-Tuerme von Skalaren "even less well motivated".
  - [H] Abweichung zwischen den beiden Kritiken: LRR setzen fuer GMOV m_KK ~ eV an, Langhoff m_KK ~ meV; beide kommen
    auf ~1e-24 Unterdrueckung (verschiedene Wege). PDF-Kopf LRR: "Dated: September 30, 2026", arXiv 28.09.

### Block C1 Reaktionen (Erwartung geschrieben 2026-10-02 21:29:10 CEST)
- C1a Semantic Scholar citations arXiv:2609.36234 und arXiv:2610.01825: Erwartung: LRR 0-1 Zitat (Langhoff), Langhoff 0;
  evtl. 404, weil noch nicht indiziert.
- C1b INSPIRE refersto:arxiv:2609.36234 und refersto:arxiv:2610.01825: Erwartung: LRR 1 (Langhoff), Langhoff 0.
- C1c arXiv-API all:"dark dimension" nach submittedDate absteigend (50): Erwartung: juengster Eintrag Langhoff 01.10.;
  keine Arbeit von Vafa/Montero/Valenzuela/Anchordoqui/Antoniadis/Luest/Gonzalo nach dem 28.09.
- Ausgang C1 (eingetragen 2026-10-02 21:30:00 CEST) [S, quellen/s2-cit-*.json, inspire-*.json, api-C1c-darkdim.xml]: bestaetigt.
  - Semantic Scholar: LRR 1 Zitat (Langhoff 2610.01825, 2026-10-01); Langhoff 0.
  - INSPIRE: LRR recid 3209110, citation_count 1 (Langhoff); Langhoff recid 3210654, 0; Danielsson/Giri recid 3170957,
    0. (Erster Versuch "refersto:arxiv:<id>" lieferte Fremdtreffer, also Syntax-Fehlschlag; mit recid korrekt.)
  - arXiv all:"dark dimension": 73 Treffer; juengster Langhoff (01.10.), davor LRR (28.09.), Stewart 2609.25230
    (21.09., Stasis und gekoppelter Dunkler Sektor), de Giorgi/Pasari 2609.10668 (09.09., Majorana-Neutrinos),
    Ahmed/Leontaris 2609.07138 (07.09.), Langhoff/Ramos/Reig 2607.27314 (29.07.), Anchordoqui/Antoniadis/Cunat
    2607.22442 (24.07.), Pourtsidou 2607.13910 (15.07., dunkle Gravitonen gegen Kosmologie-Daten). Juengste Arbeit der
    MVV-Urheber: Montero/Vafa/Valenzuela 2512.09052 (09.12.2025, Neutrinos, B-L). "Noble" = Neena T. Noble (Mitautorin
    2404.17334, Casimir-Korrekturen). Keine Antwort nach dem 28.09.
  - Grenze: Die API kennt nur bis zur Ankuendigung vom 01.10. abends (US-Ostzeit); Einreichungen vom 01.10. nach
    14 Uhr ET und vom 02.10. sind noch nicht oeffentlich [H aus arXiv-Ablauf, nicht geprueft].

### Block C2 Urheber und Begleitarbeit (Erwartung geschrieben 2026-10-02 21:30:00 CEST)
- C2a arXiv-API (au:Vafa OR au:Anchordoqui OR au:Antoniadis OR au:Obied OR au:Valenzuela_I OR au:Montero_M OR
  au:Gonzalo_E), nach Datum (25): Erwartung: keine Arbeit nach dem 28.09. zu KK-Zerfaellen; juengste Arbeiten zu
  anderen Themen.
- C2b au:Randall_L nach Datum (10): Erwartung: Begleitarbeit [24] noch nicht erschienen (LRR v1 sagt "to appear").
- C2c all:"Kaluza-Klein graviton" nach Datum (25): Erwartung: de Giorgi/Marcoli/Silvetti 2607.12012 und Chivukula u. a.
  unter den Treffern; keine Gegenrede zu LRR/Langhoff.
- Ausgang C2 (eingetragen 2026-10-02 21:30:36 CEST) [S Metadaten, quellen/api-C2*.xml]:
  - C2a bestaetigt: juengste Arbeiten der Urheber vor dem 28.09.: Baykara/Vafa 2609.20915 (17.09., IIB-Dualifold),
    Anchordoqui/Antoniadis/Bedroya 2608.11086 (11.08.), Anchordoqui/Bedroya/Luest/Tarazi 2608.00590 (01.08.),
    Anchordoqui/Antoniadis/Cunat 2607.22442 (24.07.). Keine Antwort.
  - C2b **Fehlschlag (Kanal)**: au:Randall_L trifft "Randall L. Rathbun" u. a., nicht Lisa Randall. Ersatz C2d.
  - C2c bestaetigt: KK-Graviton-Treffer ohne Gegenrede. Neu fuer Frage 3: Gross/Hooper 2407.07529 (KK-Graviton-
    Freeze-in und BBN, 2024), Cassem/Kumar 2607.02651 (Planck-Suche nach KK-Gravitonen und Radion, 02.07.2026),
    Luest/Masias 2609.16103 (Higuchi-Schranke, 14.09.2026), de Giorgi/Vogl 2208.03153 (warme DM aus gravitativem
    Freeze-in).

### Block D1 Schranken anderer Art (Erwartung geschrieben 2026-10-02 21:30:37 CEST)
- D1 API id_list (Wortlaut der Abstracts): 2407.07529 (Gross/Hooper), 2607.02651 (Cassem/Kumar), 2607.13910
  (Pourtsidou), 2609.25230 (Stewart), 2607.27314 (Langhoff/Ramos/Reig), 2601.00790 (Bai u. a.), 2509.05233 (KATRIN),
  2508.04274 (Eller u. a.), 2510.25832 (Reig/Ruiz), 2411.07029 (AAL Neutrino-Tuerme), 2512.09052 (MVV Neutrinos),
  2609.16103 (Luest/Masias). Erwartung: Gross/Hooper: BBN begrenzt Freeze-in-KK-Gravitonen stark (fuer n = 1 bei
  um-Radius schon eng); Pourtsidou: Kosmologie-Daten begrenzen dunkle Gravitonen, nicht ausgeschlossen; Neutrino-
  Arbeiten: R <~ wenige um aus Oszillationsdaten (Bulk-Neutrinos); Reig/Ruiz: Protonzerfall begrenzt M-Theorie-
  Intervall; MVV 2512.09052: Neutrinomassen; Stewart: kosmologische Stasis rettet/aendert DM-Bild; Langhoff/Ramos/
  Reig: Axiverse plus DD, Freeze-in-Formel.
- D2 au:Riojas nach Datum (10): Erwartung: nur LRR, Begleitarbeit noch nicht da.
- Ausgang D1 (eingetragen 2026-10-02 21:31:24 CEST) [S Abstracts, quellen/api-D1.xml]: teils bestaetigt, zwei **Verstoesse**:
  - **Verstoss (mittel): Der Druck auf die DD-Dunkle-Materie ist aelter als die zwei neuen Preprints.**
    Langhoff/Ramos/Reig 2607.27314 (29.07.2026): N Axion-Tuerme verduennen sichtbare Energieeinspeisung um N; "how dark
    dimension dark matter can avoid strong cosmological constraints which rule out the simplest models". Also galt die
    einfachste DD-DM schon im Juli als ausgeschlossen (welche Schranke genau: offen, Block D3). Dieselbe Arbeit liefert
    die Freeze-in-Formel, die Langhoff im Oktober nutzt; T_RH-Fenster 5 MeV bis O(1) GeV fuer DM aus Freeze-in.
  - **Verstoss (mittel): Es gab schon einmal einen Ausschlussanspruch gegen Mikrometer-Dimensionen samt Gegenrede.**
    Anchordoqui/Antoniadis/Luest/Penaló Castillo 2411.07029 (11.11.2024): "counterarguments to a recent claim
    suggesting that the bounds on Delta N_eff rule out micron-sized extra dimensions". Urheber der Behauptung: offen
    (Block D3).
  - Gross/Hooper 2407.07529 (2024): BBN; fuer n = 1 muss M_* > 2e13 GeV sein, "unless the temperature of the early
    universe was never greater than T ~ 2 TeV". [E/H] Die DD (M_5 ~ 1e9-1e10 GeV) entgeht dem nur ueber eine
    niedrige Hoechsttemperatur (GMOV: T_RH ~ GeV); dieselbe Stellschraube T_RH wie bei Langhoff.
  - Neutrinos: Eller/Ettengruber/Zander 2508.04274 (MINOS/MINOS+, KamLAND, Daya Bay): keine Signatur; Schranken auf
    den Radius je nach Bulk-Masse und Yukawa, "small couplings or negative bulk masses remain less constrained".
    Bai u. a. 2601.00790 (T2K, NOvA): "stringent exclusion limit" auf Modellparameter. Antoniadis u. a. 2509.05233:
    grosser Teil des Parameterraums in KATRIN-Reichweite. Montero/Vafa/Valenzuela 2512.09052: Vorhersage
    m_nu ~ m_KK ~ Lambda^(1/4) und sterile Neutrinos im keV-Bereich.
  - Reig/Ruiz 2510.25832 (JHEP 2026, 293): im Horava-Witten-Bild Protonzerfall -> R <~ 1e-28 m; trifft eine
    Stringeinbettung, nicht die DD allgemein.
  - Pourtsidou 2607.13910: aktualisierte CMB+BAO-Schranken auf zerfallende dunkle Gravitonen, Euclid/LSST koennten
    "confirm or rule out" [L?, Ergebnis-Zahlen nicht im Abstract].
  - Cassem/Kumar 2607.02651: Planck-NG-Suche im gewarpten 5D-Modell, kein Signal (max. 1,8 sigma) - inflationaere
    Skala, fuer die DD nicht direkt einschlaegig [H].
  - Stewart 2609.25230: Stasis; fuer die DD mit Fuenfte-Kraft-Schranken "capture into stasis in the future is
    excluded" fuer geometrische Potentialquellen - Randbefund.
  - Luest/Masias 2609.16103: Higuchi-Schranke haelt fuer Casimir-stabilisierten Kreis - kein Druck.

### Block D3 Vorlaeufer-Kritik (Erwartung geschrieben 2026-10-02 21:31:39 CEST)
- D3a Volltext AAL 2411.07029, grep "rule out", "Delta N", "claim": Erwartung: die Behauptung von 2024 stammt aus einer
  Arbeit zu thermalisierten Bulk-Neutrino-Tuermen (Delta N_eff > Schranke fuer R ~ um); AAL halten mit kleiner
  Mischung bzw. Zerfallskanaelen dagegen.
- D3b Volltext Langhoff/Ramos/Reig 2607.27314, grep "rule out", "simplest", "constraint", "cascade", "d-wave":
  Erwartung: Die einfachsten Modelle scheitern an CMB-Energieeinspeisung bzw. BBN durch zerfallende Turmzustaende;
  noch ohne d-Wellen-Argument (das kam erst im Oktober).
- D2 au:Riojas nach Datum: Erwartung siehe Block D1.
- Ausgang D3/D2 (eingetragen 2026-10-02 21:32:24 CEST) [S Volltexte quellen/AAL-2411.07029v1-raw.txt, LanghoffRamosReig-2607.27314v1-raw.txt;
  quellen/api-D2-riojas.xml]:
  - D3a bestaetigt, mit Zusatz: Die Behauptung stammt von McKeen/Ng/Shamma, PRD 110, 083507 (2024), arXiv:2406.05266
    (Bulk-Neutrinos, Delta N_eff "generically rule out micron-sized extra dimensions", so AAL Z. 51-56). AAL nennen das
    "deceptive", "not generic but rather model dependent"; Hauptgegenargument: Die Annahmen erlaubten keine
    "intra-tower neutrino decays" ("dark-to-dark"), die "usually dominates" (Z. 58-63); KK-Verletzung "very small:
    delta n ~ 0.2" (Z. ~528). **[H] Spur:** Die Verteidigung von 2024 stuetzt sich auf genau die Art schneller
    Turm-interner Zerfaelle, die LRR und Langhoff jetzt fuer Gravitonen an der Schwelle unterdrueckt finden. Ob das fuer
    Neutrino-Tuerme ebenso gilt, ist nach Recherchestand offen.
  - D3b bestaetigt: Langhoff/Ramos/Reig (07/2026), Z. 60-69: Spannung zu warm vs. zu viel Energieeinspeisung;
    "the simplest dark dimension dark matter model is excluded"; Ausweg nur durch Handabstimmung [16, 17], "no
    concrete construction achieving this has been proposed". Noch s-Wellen-Bild ("Such decays naturally outpace decays
    to the SM"). Fuenfte Kraft: "fifth force bounds exclude Delta m_KK <~ 5 meV" (Abb. 1); "improving bounds on
    Delta m_KK by a factor of 6 ... would already exclude most models with N < 10^4" (Z. 1284-1287).
    [E] 5 meV <-> 39 um; Faktor 6 <-> ~7 um.
  - D2 bestaetigt: au:Riojas juengster Eintrag ist LRR (28.09.); Begleitarbeit [24] nach Recherchestand nicht auf arXiv.

### Block B1 Varianten (Erwartung geschrieben 2026-10-02 21:32:24 CEST)
- B1a Danielsson/Giri 2606.20942 Volltext (grep "micron", "fat graviton", "Kaluza", "tower", "KK", "Newton",
  "weaken", "experiment"): Erwartung (VB-5): Gravitation auf der Blasenwand induziert; bei um wird sie schwaecher
  ("fat graviton"); kein leichter KK-Turm frei beweglicher Gravitonen, daher greift Langhoffs Freeze-in nicht direkt;
  Vorhersage zum Labor qualitativ.
- B1b arXiv all:"dark dimension" AND all:warped (und all:"warped dark dimension"): Erwartung: 0-3 Treffer; keine
  Arbeit nach dem 28.09.
- Ausgang B1 (eingetragen 2026-10-02 21:33:22 CEST) [S Volltext quellen/DanielssonGiri-2606.20942v1-raw.txt; S Abstracts quellen/api-B1*.xml]:
  - B1a im Kern bestaetigt, mit **Verstoss (mittel) bei der Laenge und der Form**:
    - Potential (Gl. 23, Z. ~700-706): V = -G4 M4 [1/rho - 3L^2/(2 rho^3) + ...]; Abschwaechung als Potenzgesetz, nicht
      als Yukawa; "L ~ 10^-5 m" (AdS5-Laenge), Gravitation "effectively shuts itself off" darunter.
    - Vierdimensionale Gravitation ist staerker als die fuenfdimensionale, "inverting the usual hierarchy found in
      standard Kaluza-Klein compactifications or RS-type setups" (Z. 1080-1083); 4D-Gravitation braucht gemischte
      Randbedingungen in AdS. Kein kompakter Kreis mit KK-Turm im Sinn von Langhoff [H].
    - Danielsson/Panizo 2311.14589 (PRD 109, 026003, 2024): "a dark dimension of size 5 x 10^-5 m", Stringskala 11 TeV.
      Danielsson/Giri 2511.21362 (PRD 113, 126010, 2026): Gravitation "weaker rather than stronger" bei ~1e-5 m;
      "explicit predictions of measurable deviations using table top experiments"; Kruemmung Omega_c ~ 5e-4.
    - [E, nur fuehrende Ordnung, ohne Apparateantwort] relative Abschwaechung 1,5 (L/rho)^2: L = 10 um, rho = 52 um
      -> ~5,5 %; rho = 100 um -> 1,5 %; rho = 1 mm -> 1,5e-4. Ein Potenzgesetz reicht weiter als ein Yukawa-Term;
      Eot-Wash-Daten (52 um - mm) koennten diese Variante schon stark pruefen. Ob D/G das selbst gegen Lee 2020 halten:
      Block B2.
  - B1b bestaetigt: 4 Treffer "dark dimension" + warped: LRR, Bernal u. a. 2601.02982, Fadafan/Cacciapaglia
    2312.08456, Blumenhagen/Brinkmann/Makridou 2208.01057 "The Dark Dimension in a Warped Throat" (2022). Nichts nach
    dem 28.09. ausser LRR.

### Block B2 (Erwartung geschrieben 2026-10-02 21:33:22 CEST)
- B2 Volltext Danielsson/Giri 2511.21362 (grep "Adelberger", "Lee", "Washington", "torsion", "excluded", "bound",
  "experiment"): Erwartung: Sie vergleichen mit Eot-Wash nur qualitativ und nennen L als frei (~1-10 um); keine
  vollstaendige Auswertung mit Apparateantwort.
- B2b API Abstract 2208.01057 (Blumenhagen u. a.): Erwartung: gewarpter Hals mit Mikrometer-Laenge, Stringkonstruktion,
  keine Kaskadenaussage.
- Ausgang B2 (eingetragen 2026-10-02 21:33:52 CEST) [S Volltext quellen/DanielssonGiri-2511.21362v2-raw.txt]: bestaetigt. Keine Nennung von
  Adelberger, Lee, Kapner, Eot-Wash oder Torsionswaage (grep). Nur: Laborgrenzen liegen "of precisely this order of
  magnitude", Verweis auf die Uebersicht Murata/Tanaka [8] (Z. 116-132). L ~ 1e-5 m ist eine Groessenordnung aus
  N ~ 1e60 (Z. 111-113). [H] Eine quantitative Auswertung der Potenzgesetz-Abschwaechung gegen Torsionswaagen-Daten
  fand ich nicht (nach Recherchestand).

### Block E1 Labor (Erwartung geschrieben 2026-10-02 21:33:52 CEST)
- E1a Murata/Fujiie/Suzuki 2605.18212 (arXiv-HTML, grep "Casimir", "future", "IUPUI", "Stanford", "levitat",
  "project", "sensitiv", "micro"): Erwartung (VB-4): unter 10 um stammen die besten Schranken aus Casimir-
  (IUPUI 2016) und Mikrokugel-/Kragarm-Versuchen, alpha >~ 1e4 bei 10 um, >~ 1e8 bei 1 um; geplante Versuche
  versprechen 1-2 Groessenordnungen; keiner erreicht alpha ~ 1 unter 10 um.
- E1b API Abstracts: 2406.13020 (Manley u. a.), 2412.13167 (Venugopalan), 2208.01057 (Blumenhagen u. a.):
  Erwartung: Manley projiziert Gravitationsstaerke erst um 25 um; Venugopalan wie STELLE-24M.
- Ausgang E1a (eingetragen 2026-10-02 21:34:35 CEST) [S Text quellen/Murata-2605.18212v2.txt; S Abb. quellen/Murata-fig3-shortscale.png,
  Murata-fig4-microscale.png, Ablesung nach Augenmass auf Log-Achsen]: bestaetigt.
  - Bereiche: 10 nm-1 um Casimir, "strongest limits set by Decca et al."; 1 um-1 mm Torsionswaagen UW und HUST;
    UW-Mindestabstand 52 um, HUST 210 um. "at the 10 um scale, the Stanford group's result was the sole experimental
    effort until the latest UW result". Neue Ansaetze (Vienna, Rikkyo, Berkeley-Atominterferometrie u. a.) "do not
    yet establish the most stringent limits". Unter 1 um: "Casimir-type measurements the practical limit for
    mechanical gravity tests".
  - Ablesung Abb. 3/4 (nur alpha > 0): Grenze bei lambda = 10 um ~ 1e4; bei 1 um ~ 1e8-1e9; bei 0,2 um ~ 1e11-1e12;
    bei 0,1 um ~ 1e12-1e13. alpha = 1 erst bei ~ 4e-5 m ("Washington 2020").
  - [E] Abstand zur DD-Erwartung alpha = 8/3: bei 7,4 um (MVV-Casimir) ~3-4 Groessenordnungen, bei 1 um ~8, bei
    0,2 um (Langhoff-Grenze) ~11.

### Block E2 Projektionen (Erwartung geschrieben 2026-10-02 21:34:35 CEST)
- E2a API Abstracts 2406.13020 (Manley u. a.), 2208.01057 (Blumenhagen u. a.): Erwartung: Manley projiziert
  Verbesserung bei ~25 um, nicht alpha ~ 1 unter 10 um; Blumenhagen: Stringkonstruktion ohne Labor-Zahl.
- E2b arXiv-Suchen nach Projektionen (nach Datum): all:levitated AND all:Yukawa; all:"inverse-square" AND
  all:(proposal OR projected); all:"Casimir" AND all:"Yukawa" AND all:"isoelectronic". Erwartung: Projektionen
  verbessern um 1-3 Groessenordnungen; keine nennt alpha <~ 1 bei lambda <~ 10 um innerhalb von zwei Jahren.
- Ausgang E2 (eingetragen 2026-10-02 21:36:28 CEST) [S Abstracts quellen/api-E2*.xml; S Volltext-Stellen quellen/Manley-2406.13020v3-raw.txt,
  BaezaBallesteros-2106.08611v2-raw.txt]: teils bestaetigt, ein **Verstoss (mittel)**:
  - Manley/Condos/Schlamminger/Pratt/Wilson/Terrano, PRD 110, 122005 (2024), arXiv:2406.13020 - ausdruecklich mit der
    DD begruendet ("predicted to arise between 1-10 um"). Projektion: Raumtemperatur neue Flaeche fuer 3 um <~ lambda
    <~ 36 um; |alpha| = 1 erreicht ein Kryo-Versuch bei 100 mK "potentially" bei lambda_min ~ 10 um mit s0 ~ 25 um;
    Prototyp gefertigt. Kein Zeitplan. -> bestaetigt (nicht unter 10 um).
  - **Verstoss gegen VB-4:** Baeza-Ballesteros/Donini/Nadal-Gisbert, EPJC 82, 154 (2022), arXiv:2106.08611
    (Mikro-Orbit, "Satellit" ~1e-9 g um "Planet" ~1e-5 g, Praezession): Empfindlichkeit fuer alpha ~ 1 bis
    "lambda <~ 5 um" ohne Untergruende, "lambda <~ 7 um" mit ungunstigen Untergruenden (Fall 1); Fall 2 10-20 um;
    "compared with the present sensitivity, lambda <= 40 um" (Z. 2862-2876). Folgearbeit 2312.13736 (12/2023) beginnt
    erst mit realistischem Aufbau (Luftreibung). -> Auf dem Papier erreicht ein Vorschlag Gravitationsstaerke unter
    10 um; gebaut ist er nach Recherchestand nicht.
  - Gemessen: Blakemore u. a., PRD 104, 061101 (2021), levitierte Mikrokugel, |alpha| >~ 1e8 fuer lambda > 10 um
    ausgeschlossen, Vorzeichen getrennt; Venugopalan 2024/26 ~1e6-1e7 (aus STELLE-24M).
  - Vorschlaege ohne alpha-Zahl im Abstract: Ren u. a. 2602.13829 (Meissner-levitierte Kugel, 0,1-10 um, ~1e-19 N/
    sqrt(Hz) bei mK); Boynewicz/Sackett 2511.08770 (Quantenreflexion); Zhong/Sui/Yang 2605.00749 (Verschraenkung, KK-
    Spektren, d = 40-80 um, Theorie).
  - Blumenhagen/Brinkmann/Makridou 2208.01057: stark gewarpter Hals realisiert m ~ Lambda^(1/4) mit "redshifted KK
    tower"; Laengenangabe l ~ 1e-6 m; keine Laborzahl. Gewarpte DD existiert also seit 2022 als Konstruktion.

### Block F1 Gegensweep: Annahmen der Verteidiger und Robustheit (Erwartung geschrieben 2026-10-02 21:36:28 CEST)
- F1a GMOV 2209.09249 und Obied/Dvorkin/Gonzalo/Vafa 2311.05318 Volltext, grep "s-wave", "threshold", "phase space",
  "p-wave", "momentum", "Mohapatra": Erwartung: Rate pro Kanal ~ m_n (bzw. Mohapatra-Abschaetzung), kein Hinweis auf
  Schwellenunterdrueckung; keine Absicherung gegen q^5.
- F1b API Abstract Barbieri u. a. 2501.01369 (T_RH-Untergrenze): Erwartung: 5,96 MeV gilt fuer einen bestimmten
  Zerfallskanal des Reheaton (hadronisch/strahlend); andere Kanaele ~4-5 MeV.
- F1c API Abstracts Giudice u. a. 1711.08437, Bonifacio/Hinterbichler 1910.04767, de Giorgi/Vogl 2105.06794,
  Chivukula u. a. 2411.02509: Erwartung: Giudice: Klockwerk/linearer Dilaton mit KK-Graviton-Zerfaellen; Bonifacio/
  Hinterbichler: Summenregeln aus Geometrie, die Wachstum aufheben; de Giorgi/Vogl: RS-Zerfaelle.
- Ausgang F1 (eingetragen 2026-10-02 21:37:34 CEST) [S Volltext-Stellen quellen/GMOV-2209.09249-raw.txt, ODGV-2311.05318-raw.txt; S Abstracts
  quellen/api-F1bc.xml]:
  - F1a bestaetigt: GMOV Z. 470-487: Turm-interne Zerfaelle "is expected again to be roughly given by (3.1)" (die
    SM-Zerfallsformel ~ m^3/M_P^2), Phasenraum nur ueber die Geschwindigkeit (m_KK delta n/m)^(1/2) "since the decay is
    almost at threshold" -> Gl. 3.2 Gamma ~ beta^2 delta n^(3/2) m^(7/2)/(M_P^2 m_KK^(1/2)). Keine Amplituden-
    unterdrueckung beruecksichtigt. ODGV (2311.05318): "epsilon ~ m_KK ~ meV, while m ~ 100 keV"; Kick-Geschwindigkeit
    aus der Kinematik.
  - F1b teils: Barbieri u. a. 2501.01369: "T_RH > 5.96 MeV" (95 %), BBN + CMB + Galaxiensurveys, Prior-Abhaengigkeit
    geprueft; Kanalabhaengigkeit nicht im Abstract [L?] -> Erwartung nicht pruefbar ohne Volltext.
  - F1c bestaetigt: Bonifacio/Hinterbichler 1910.04767: Summenregeln fuer KK-Massen und kubische Kopplungen erzwingen
    "nontrivial cancellations"; de Giorgi/Vogl 2105.06794: Wachstum "is unphysical and cancels once the full field
    content ... is taken into account"; Chivukula u. a. 2411.02509: "intricate cancellation". Giudice u. a.
    1711.08437: Kaskaden angeregter Gravitonen im linearen Dilaton. -> [H] Die Aufhebungs-Physik stand seit 2019-2021
    in der RS-/Summenregel-Literatur; die DD-DM-Arbeiten 2022-2024 nutzten sie nicht.
  - McKeen/Ng/Shamma 2406.05266 (PRD 110, 083507): "These limits generically rule out micron-sized extra dimensions";
    Ausweg dort: niedrige Reheating-Temperatur. -> Dieselbe Stellschraube T_RH wie bei Langhoff; Langhoff schliesst
    sie von unten mit T_RH >= 5,96 MeV.

## 5. Gegensweep Phase 1 (geschrieben 2026-10-02 21:37:34 CEST): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | Pruefen? |
|---|---|---|
| GS1 | Die Daten der Karte stimmen | geprueft (A1): vertauscht |
| GS2 | alpha = 8/3 gilt auch fuer Langhoffs Intervall mit Brane am Fixpunkt | [E] Kopfrechnung: psi_n^2(0)/psi_0^2 = 2 -> 2 x 4/3 = 8/3, lambda = R; an einem allgemeinen Punkt 2 cos^2(n y_b/R) <= 2 |
| GS3 | Die Blasen-Variante ist mit heutigen Daten vereinbar, weil niemand das Gegenteil schreibt | PRUEFEN: Eot-Wash-Schranken fuer Potenzgesetz-Abweichungen (Adelberger u. a. 2007, hep-ph/0611223) |
| GS4 | Reaktionen erscheinen auf arXiv | teils: Semantic Scholar/INSPIRE fangen jede zitierende Arbeit; Blogs, Vortraege, soziale Medien nicht abgedeckt; OpenAlex-Gegenprobe |
| GS5 | Langhoffs Freeze-in-Formel ist unabhaengig geprueft | nein: stammt aus seiner eigenen unbegutachteten Arbeit 2607.27314; Gross/Hooper 2024 rechnen aehnliches fuer BBN, nicht verglichen |
| GS6 | "R" bei MVV und bei Langhoff ist dieselbe Groesse | [H]: Langhoff R = 1/m_KK; MVV l ~ lambda Lambda^(-1/4) nur Groessenordnung; Faktoren 2 pi moeglich, fuer Groessenordnungsaussagen folgenlos |

- GS3 Erwartung: Adelberger u. a. 2007 nennen Schranken fuer Potenzgesetz-Terme beta_k (1 mm/r)^(k-1), k = 2-5,
  fuer k = 3 etwa |beta_3| <~ 1e-4 -> Blase mit L ~ 10 um an der Grenze, mit L ~ 50 um klar ausgeschlossen [E].
- GS4 Erwartung: OpenAlex search "dark dimension" ab 2026-09-01: nur arXiv-Spiegel der bekannten Preprints.
- Ausgang GS3/GS4 (eingetragen 2026-10-02 21:39:05 CEST):
  - **GS3 Verstoss (gross, eigener Befund [E]):** Adelberger u. a., PRL 98, 131104 (2007), arXiv:hep-ph/0611223
    [S Volltext quellen/Adelberger-2007-raw.txt Z. 218-298, 310-350]: Eot-Wash hat Sundrums "fat graviton" schon 2007
    getestet: "Our results require l_g <= 98 um at 95% confidence" (Modell F ~ (1 - exp(-0,914 r/l_g))^3 / r^2);
    Potenzgesetz-Schranken V = -G Ma Mb/r beta_k (1 mm/r)^(k-1), 68 %: |beta_3| <= 1,3e-4 (k = 3).
    Danielsson/Giri Gl. 23 (layout Z. 376-383 bestaetigt): relative Korrektur -(3/2)(L/rho)^2, also beta_3 =
    -1,5 (L/1 mm)^2. [E] |beta_3| <= 1,3e-4 -> L <= sqrt(8,7e-5) mm ~ 9 um (68 %, fuehrende Ordnung, Punktmassen-
    Entwicklung fuer rho >> L). Danielsson/Panizo-Wert 50 um -> beta_3 ~ -3,8e-3, rund 30-fach ueber der Schranke;
    "L ~ 1e-5 m" liegt an der Grenze. Weder D/G 2511.21362 noch 2606.20942 zitieren diese Eot-Wash-Auswertung (grep).
    -> Die Variante mit anderem Vorzeichen ist mit vorhandenen Daten pruefbar und im oberen Teil ihres Bereichs
    schon unter Druck (nach Kopfrechnung, nicht veroeffentlicht).
  - GS4 bestaetigt: OpenAlex Volltextsuche "dark dimension" ab 01.09.2026: 38 Treffer, keine Antwort auf LRR/Langhoff
    (Langhoff noch nicht indiziert). Neu fuer Frage 3: "Bounds on massive graviton-like particles from searches for
    axion-like particles coupling to photons", JHEP 09 (2026) 220, 21.09.2026 [L? Titel]. Randtreffer ohne Gewicht:
    ResearchGate-Text "Smectic-A Supersolid Multiverse ... Schwarz's Dark Dimension" (unbegutachtet, nicht gewertet).

### Block D4 (Erwartung geschrieben 2026-10-02 21:39:05 CEST)
- D4 arXiv-API ti:"massive graviton-like" sowie id_list 2510.18975 (Hardy u. a.): Erwartung: JHEP-Arbeit setzt
  ALP-Photon-Schranken (Sterne, Helioskope, Roentgen) auf massive Spin-2-Teilchen um und nennt KK-Gravitonen der DD
  als Anwendung; Hardy: n = 1 schwaecher als Labor, SN 1987A eingeschlossen.
- Ausgang D4 (eingetragen 2026-10-02 21:39:27 CEST) [S Abstracts quellen/api-D4*.xml]: teils bestaetigt.
  - Gue/d'Enterria, arXiv:2605.00549, JHEP 09 (2026) 220: ALP-Photon-Schranken auf massive Spin-2-Teilchen umgerechnet;
    "current ALP searches do not set stronger bounds on massive spin-2 particles than fifth-force tests"; Zukunft stark
    nur fuer m_G <~ 1e-8 eV. -> fuer DD-KK-Massen (~eV) keine neue Schranke [H].
  - Hardy/Sokolov/Stubbs 2510.18975 (v2): staerkste Grenze SN 1987A (Pion-Prozess); n = 1 "weaker than those from
    laboratory searches"; Zerfallsschranken "less stringent than the cooling bounds if there is KK number violation at
    the level typically assumed in the dark dimension scenario". [H] Spur: Ohne schnelle Kaskade (LRR/Langhoff) bleibt
    die Freeze-in-Population schwer und zerfaellt sichtbar; genau diese Zerfallsschranke macht Langhoff stark.

### Block F2 Vorlaeufer der Schwellenunterdrueckung (Erwartung geschrieben 2026-10-02 21:39:27 CEST)
- F2 API id_list 2507.21218 (Chivukula u. a. 2025), 2509.04580 (Donini/Folgado/Munoz-Ovalle), 2412.20913 (Im/Jodlowski),
  2607.12012 (de Giorgi u. a.): Erwartung: RS-/gewarpte KK-Graviton-Phaenomenologie; keine wendet die
  Schwellenunterdrueckung vor dem 28.09.2026 auf die DD an.
- Ausgang F2 (eingetragen 2026-10-02 21:41:36 CEST) [S Abstracts quellen/api-F2.xml]: bestaetigt. Chivukula u. a. 2507.21218 (Radion-
  Portal-DM), Im/Jodlowski 2412.20913 (Potenzgesetz-Warp, Collider), de Giorgi/Marcoli/Silvetti 2607.12012 (LHC,
  KK-Turm), Donini/Folgado/Munoz-Ovalle 2509.04580 (Drei-Bran-RS): RS-/Collider-Phaenomenologie; keine wendet die
  Schwellenunterdrueckung vor dem 28.09.2026 auf die DD an (nach Abstracts).

## 5b. Gegensweep Phase 2 (Recherche-Ende), Zusammenfassung

| Nr | Selbstverstaendlichkeit | Geprueft? | Ergebnis |
|---|---|---|---|
| GS1 | Kartendaten stimmen | ja (API) | vertauscht: LRR 28.09., Langhoff 01.10. |
| GS2 | alpha = 8/3 gilt fuer Langhoffs Fixpunkt-Brane | ja [E] | psi_n^2(0)/psi_0^2 = 2 -> 8/3, lambda = R |
| GS3 | Blasen-Variante mit heutigen Daten vereinbar | ja (Adelberger 2007 Volltext) | Potenzgesetz-Schranke -> L <~ 9 um (68 %) [E]; fat graviton l_g <= 98 um (95 %) |
| GS4 | Reaktionen nur auf arXiv | teils (S2, INSPIRE, OpenAlex) | keine Antwort; Blogs/Vortraege nicht abgedeckt |
| GS5 | Langhoffs Freeze-in-Formel unabhaengig geprueft | nein | eigene unbegutachtete Arbeit 2607.27314; nicht gegen Gross/Hooper verglichen |
| GS6 | MVV-l = Langhoff-R | [H] | nur Groessenordnung; Faktoren 2 pi folgenlos fuer die Aussage |
| GS7 | "Gewarpte Varianten umgehen" (E2) | ja (Langhoff Gl. 25, LRR App. A/B) | Schwellenunterdrueckung gilt fuer jeden statischen Warp; Umgehen nur ueber anderes Spektrum (LRR-Begleitarbeit, nicht erschienen) |
| GS8 | T_RH-Untergrenze robust | teils | 5,96 MeV (Barbieri 2025, 95 %); [E] Abundanz ~ T_RH^3 R: 20 % tiefere Untergrenze -> R-Grenze etwa Faktor 2 weiter |
## 6. Schreibphase
- ERGEBNIS.md Schreibbeginn: 2026-10-02 21:41:36 CEST (date).
- Verfahrensvermerk (2026-10-02 21:48:08 CEST, date): Die erste Fassung der Suchprotokoll-Tabelle in ERGEBNIS.md hatte sieben falsch
  uebertragene Erwartungszeiten (A2, C1, D3/D2, E1, E2, F1, F2) und zwei nicht gemessene Werte bei D4 (21:38:39,
  21:39:43). Gegen die Zeilen dieses ARBEITSFELDs berichtigt; der Fehler ist in ERGEBNIS.md Abschnitt 7 vermerkt.
- Rueckwaerts-Gegenlesen (2026-10-02 21:48:08 CEST): Zahlen, Daten und Zitate in ERGEBNIS.md gegen quellen/ geprueft. Berichtigt:
  "nur SM-Zerfallskanaele" ist Lesart [H] der Gesamtbreite 9/4 Gamma_gg (Langhoff sagt das nicht woertlich);
  Bonifacio/Hinterbichler-Fundstelle ohne geratene Jahreszahl der Zeitschrift.
- Meta-Abruf Autoren/Metadaten: date-Ausgabe 21:42:18 im selben Befehl (quellen/api-meta-final.xml).

## 7. Abschluss
- ERGEBNIS.md fertig: 2026-10-02 21:48:24 CEST (date). Zeitbox (bis 22:39) eingehalten.
- Offene Rueckfragen wandern mit: R1 (Finns "Seiten einer Dimension"); R2 (Lee-2020-Supplement, Vorzeichen);
  neu R3: Blase gegen Eot-Wash mit Apparateantwort (Rechenauftrag); R4: LRR-Begleitarbeit und Antwort der Urheber
  beobachten (Scout); R5: trifft die Schwellenunterdrueckung auch Neutrino-Tuerme und Axion-Fragmentation?
