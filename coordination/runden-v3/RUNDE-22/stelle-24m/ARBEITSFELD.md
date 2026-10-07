# ARBEITSFELD STELLE-24M (Literatur-Agent, Runde 22)

Einzige Arbeitsdatei dieser Karte (Feldregel 5). Vor jedem Schritt neu lesen. Gestrichenes bleibt stehen (~~so~~).
Marken: [S] gelesen (Volltext/Abbildung/Tabelle selbst gesehen), [L?] nur Abstract oder Zitat, [H] eigene Schlussfolgerung, [E] Kopfrechnung.

## 0. Start
- Start (date): 2026-10-02 19:03:39 CEST (erste date-Messung); Strategie geschrieben 2026-10-02 19:04:27 CEST
- Zeitbox 50 min, also Ende spaetestens ca. 50 min nach Start (Endzeit wird per date geprueft, nicht vorab eingetragen).
- Gelesen als Vorwissen: WARUM-SPIN-2.md, Nachtrag 27.09. und Berichtigung 29.09. (Lee u. a. 2020: |alpha| = 1, 95 % lambda < 38,6 um, Abstaende bis 52 um; Stelle-Form +1/3 / -4/3; 5,1 meV nur Einzel-Yukawa).

## 1. Suchstrategie (vor jedem Abruf geschrieben)

Ziel: alle Sub-mm-Tests des Abstandsgesetzes / Yukawa-Schranken, erschienen ab 2024-10-01, plus Arbeiten, die die
Zwei-Term-Stelle-Form oder quadratische Gravitation gegen Kurzabstandsdaten auswerten.

Kanaele (WebSearch erschoepft, nur WebFetch):
1. arXiv-API (export.arxiv.org/api/query), sortiert nach submittedDate absteigend, je Suchbegriff 30-50 Treffer:
   a. "inverse-square" AND submillimeter / sub-millimeter
   b. "short-range gravity" / "short-range" AND "Yukawa"
   c. "Yukawa" AND "torsion pendulum" / "torsion balance"
   d. "non-Newtonian gravity" AND micrometer / "non-Newtonian"
   e. "Casimir" AND "gravity" / "Casimir" AND "Yukawa" (Casimir-kompensierte Tests, IUPUI, CANNEX)
   f. "quadratic gravity" AND "Yukawa"; "Stelle" AND "Newtonian potential"; "higher-derivative gravity" AND "laboratory"
   g. Neutronen: "neutron" AND "fifth force" / "qBounce" / "Pendelloesung"; Atominterferometrie: "atom interferometer" AND "fifth force"
   h. Schwebende Mikrokugeln: "levitated" AND "Yukawa" / "micrometer scale" AND "new interactions"
2. OpenAlex (api.openalex.org/works?search=...&filter=from_publication_date:2024-10-01) als Zweitkanal fuer Zeitschriftenartikel ohne arXiv.
3. Semantic Scholar (api.semanticscholar.org/graph/v1/paper/search) als Drittkanal, falls 1 und 2 Luecken lassen.
4. Gruppen gezielt: Eot-Wash (Adelberger, Heckel, Lee), HUST/Wuhan (Tan, Shao, Luo), IUPUI (Decca), Stanford (Gratta, Kapitulnik), CANNEX (Sedmik), qBounce (Abele), Neutronenstreuung (Snow, Haddock, Heacock).
5. Volltexte bei arXiv (abs-Seite, dann HTML-Fassung arxiv.org/html/... oder PDF) fuer jede Kandidatin mit neuer Schranke; Schranke nur aus selbst gesehener Abbildung/Tabelle oder Textstelle mit Zahl, sonst [L?].
6. Gegensweep: gezielt nach neuen Rekordschranken suchen, die S2 kippen wuerden ("38.6", "improved constraints" "inverse-square law" "torsion" 2025/2026; "Eot-Wash" neu; HUST neu).

Abbruchkriterien: Zeitbox; je Kanal Stopp, wenn zwei aufeinanderfolgende Abfragen keine neue Kandidatin ab 10/2024 liefern.

## 2. Eigene Erwartungen des Agenten (vor dem ersten Abruf; die Leitungserwartungen S1-S3 stehen fest und werden nur gewertet)
- A1: Es gibt seit 10/2024 mindestens ein neues HUST- oder Mikrokugel-Ergebnis, aber keine neue Eot-Wash-Rekordschranke fuer |alpha| = 1.
- A2: Die 38,6-um-Schranke (Lee 2020) ist am 02.10.2026 noch der Rekord fuer |alpha| = 1; HUST 2020 lag bei ca. 48 um (aus Gedaechtnis, ungeprueft).
- A3: Zur Stelle-Form gibt es seit 10/2024 hoechstens Arbeiten, die "m2 > ~ meV" aus Eot-Wash zitieren, keine eigene Zwei-Term-Anpassung an Daten.

## 3. Abruf-Protokoll (Erwartung vor Abruf -> Ausgang)

### Block 1 (arXiv-API, vier Abfragen parallel), Erwartungen geschrieben 2026-10-02 19:04:35 CEST
- Q1 all:"inverse-square" AND all:submillimeter -> Erwartung: meist aeltere Arbeiten; 0-2 Treffer ab 10/2024 (ggf. HUST).
- Q2 all:"short-range gravity" -> Erwartung: Mischung Theorie/Experiment, einige neue, kaum mit neuer Schranke.
- Q3 all:Yukawa AND all:"torsion pendulum" -> Erwartung: HUST-Linie; moeglicherweise ein neues HUST-Ergebnis 2025.
- Q4 all:"non-Newtonian gravity" AND all:micrometer -> Erwartung: Casimir-basierte Schranken (Klimchitskaya/Mostepanenko), Wiederauswertungen, keine neue Messung unter 38,6 um bei alpha = 1.
#### Ausgang Block 1 (eingetragen 2026-10-02 19:05:30 CEST)
- Q1: nur 6 Treffer, juengster 2019 -> Phrase "inverse-square" greift in der API schlecht (Bindestrich). Erwartung "0-2 neue" formal bestaetigt, aber Kanal untauglich; Variante ohne Bindestrich noetig.
- Q2: 35 Treffer. Ab 10/2024 nur Vorschlaege/Methoden/Theorie, keine neue Messschranke:
  - 2605.00749 Zhong (QGEM-Vorschlag, 40-80 um), 2602.13829 Ren (Sensorvorschlag 0,1-10 um), 2511.08770 Boynewicz (Quantenreflexion, Vorschlag),
    2504.18389 Grinin (Fallenmethode), 2603.16026 Balfagon (Ringdown), 2507.00223 Bailey (Review SME).
  - 2601.05750 Zhu, "PPN analysis of quadratic gravity": Sonnensystem-Schranke m >~ 23 AU^-1 (laut Abstract-Zusammenfassung) -> Kandidat fuer Frage 3 (quadratische Gravitation gegen Daten, aber Sonnensystem, nicht Kurzabstand). [L?] Pruefen.
  - Erwartung bestaetigt (keine neue Schranke).
- Q3: nur 3 Treffer (2022, 2011, 2004) -> API-Phrase eng; Erwartung "neues HUST-Ergebnis" hier nicht gefunden, Kanal unvollstaendig.
- Q4: 2 Treffer (2021, 2019). Kanal unvollstaendig.
- Zwischenbefund: die arXiv-API-Phrasensuche liefert wenig; Zweitkanal OpenAlex jetzt vorziehen.
### Block 2 (arXiv-API Varianten + OpenAlex), Erwartungen geschrieben 2026-10-02 19:05:30 CEST
- Q5 arXiv all:"inverse square law" AND all:gravitational -> Erwartung: einige Treffer 2025/26, darunter evtl. ein HUST-Ergebnis.
- Q6 arXiv all:Casimir AND all:Yukawa -> Erwartung: Klimchitskaya/Mostepanenko-Neuauswertungen 2025, keine neue Schranke bei 30-40 um.
- Q7 OpenAlex search "inverse-square law submillimeter" ab 2024-10-01 -> Erwartung: 3-10 Treffer, ein bis zwei Messarbeiten (HUST/Eot-Wash).
- Q8 OpenAlex search "non-Newtonian gravity Yukawa constraints" ab 2024-10-01 -> Erwartung: Casimir-/Neutronen-Schranken unter 10 um, nichts unter 38,6 um bei alpha = 1.
#### Ausgang Block 2 (eingetragen 2026-10-02 19:06:37 CEST)
- Q5 (arXiv "inverse square law" + gravitational), neu ab 10/2024:
  - **2605.18212 Murata (2026-05-18), Review "Short-Range Tests of the Gravitational Inverse-Square Law"** -> muss gelesen werden (Stand der Rekorde 2026). [L?]
  - **2609.00317 Pszota (2026-08-31), "Ghost-free higher-gradient Newtonian gravity"**: laut API-Zusammenfassung "internal length below 4e-5 m; Yukawa amplitude sum rule alpha = -1". [L?]
    - ERWARTUNGSVERSTOSS-KANDIDAT fuer S3/A3: Summenregel alpha = -1 ist genau die Stelle-Summe (+1/3 - 4/3 = -1). Voller Zyklus noetig.
  - 2509.02801 Ewasiuk (Theorie, grosse dunkle Sektoren, nutzt Labortests) [L?]; Rest irrelevant.
- Q6 (arXiv Casimir + Yukawa), neu ab 10/2024: 2603.22413 Ma (lambda <~ 10 nm), 2511.19276 Klimchitskaya (1-2 nm), 2602.13829 Ren (Vorschlag); alle weit unter 38,6 um -> fuer Frage 2 irrelevant. Erwartung bestaetigt.
- Q7/Q8 (OpenAlex, freie Suche): 560 bzw. 570 Treffer, Zusammenfasser gab nur je 3 aus -> Kanal so untauglich. Ein Fund:
  - Fiorillo u. a. 2025, PRL, DOI 10.1103/tlqz-713s, "Leading bounds on micrometer to picometer fifth forces from neutron star cooling" [L?, nur Titel].
    - [H] Astrophysikalische Emissionsschranken gelten fuer Teilchenkopplungen weit ueber Gravitationsstaerke; bei alpha ~ 1 (Kopplung ~ m_n/M_Pl) erwartet keine Wirkung. Pruefen, ob sie bis 30-40 um reichen.
- Naechster Schritt: Murata-Review, Pszota, Zhu (2601.05750) lesen; OpenAlex mit title_and_abstract.search und select.
### Block 3, Erwartungen geschrieben 2026-10-02 19:06:37 CEST
- R1 arXiv abs 2605.18212 (Murata-Review) -> Erwartung: nennt Lee 2020 (38,6 um) weiter als Bestwert fuer |alpha| = 1; evtl. HUST 2020 (~48 um); keine neuere Rekordschranke.
- R2 arXiv abs 2609.00317 (Pszota) -> Erwartung: Theorie (Gradientenelastizitaet/Mindlin-artig), nutzt Lee 2020 als Datenschranke; nicht Stelle-Wirkung selbst, aber Zwei-Yukawa-Form mit Summe -1.
- R3 arXiv abs 2601.05750 (Zhu, PPN quadratische Gravitation) -> Erwartung: nur Sonnensystemschranken, Kurzabstandsdaten hoechstens erwaehnt.
- R4 OpenAlex filter title_and_abstract.search "inverse-square law" ab 2024-10-01 -> Erwartung: 10-30 Treffer, 0-2 neue Messungen.
#### Ausgang Block 3 (eingetragen 2026-10-02 19:07:58 CEST)
- R1 Murata, Fujiie, Suzuki, arXiv:2605.18212 (v1 18.05.2026, v2 08.09.2026, fuer AAPPS Bulletin): Abstract verspricht "comprehensive updates ... new experimental data from the past decade". [L?] -> Volltext noetig (Abbildungen/Tabelle zu 10-100 um).
- R2 Pszota, Van, arXiv:2609.00317 (31.08.2026), 4 Seiten, keine Abbildungen: Summenregel sum alpha_i = -1; "laboratory tests ... bound the largest internal length below 4e-5 m". [L?]
  - Teilverstoss gegen A3: Es GIBT eine neue Arbeit (08/2026), die eine Mehr-Yukawa-Form mit Summe -1 gegen Labortests auswertet; aber Newtonsche Gradiententheorie, nicht ausdruecklich Stelle (+1/3/-4/3). Volltext pruefen.
- R3 Zhu, Li, arXiv:2601.05750 (EPJC 2026): quadratische Gravitation, Sonnensystem m_R, m_W >~ 23 AU^-1; Kurzabstand nur als Ausblick ("future tests ... laboratory-scale"). [L?] Erwartung bestaetigt (nicht Kurzabstand).
  - Nebenbefund [L?]: "to ensure that gravity remains attractive, m_W > m_R/4".
- R4 OpenAlex title_and_abstract: 2790 Treffer, ueberwiegend Zenodo-Rauschen; relevant nur Murata 2026 und Fiorillo 2025. Kanal fuer Vollstaendigkeit untauglich.
### Block 4, Erwartungen geschrieben 2026-10-02 19:07:58 CEST
- R5 arXiv HTML 2605.18212v2 (Murata-Volltext) -> Erwartung: Yukawa-Abbildung 1-1000 um zeigt Eot-Wash 2020 als staerkste Kurve um 30-50 um; neue Daten seit 2020 hauptsaechlich Casimir/Neutronen unter 10 um.
- R6 arXiv HTML/PDF 2609.00317 (Pszota-Volltext) -> Erwartung: 4e-5 m stammt aus Lee 2020 (38,6 um bei |alpha| = 1), ohne eigene Datenanpassung.
- R7 arXiv-API au:Adelberger OR au:Heckel (Eot-Wash), nach Datum -> Erwartung: keine neue ISL-Messung seit 10/2024.
- R8 arXiv-API au:Shao_C AND all:gravit* bzw. HUST-Linie -> Erwartung: evtl. eine neue HUST-ISL-Arbeit 2025/26 mit Schranke um 40-50 um.
#### Ausgang Block 4 (eingetragen 2026-10-02 19:09:43 CEST)
- R5 Murata-Review v2 (WebFetch-Auszug, noch nicht selbst geprueft): nennt Lee 2020 (UW, Mindestabstand 52 um) als juengstes UW-Ergebnis; neuere Zitate 2024-26 nur Atominterferometrie (Panda 2024, Nature 631, 515), Isotopieverschiebung (Door 2025 PRL 134, 063002; Wilzewski 2025 PRL 134, 233002), Yb-Spektroskopie (Ishiyama 2026). Keine Stelle-/Zwei-Term-Diskussion.
  - Auszug enthielt eine unklare Angabe ("HUST 2020 ... down to lambda ~ 210 um gap distance"), Fig. 3 -> selbst pruefen; Abbildung nur selbst gesehen werten.
  - Erwartung (Lee 2020 weiter Bestwert) vorlaeufig bestaetigt, aber [L?] bis Abbildung gesehen.
- R6 Pszota/Van (WebFetch-Auszug mit Zitaten): Gl. (11) phi = -GM/r (1 + sum alpha_i e^(-r/lambda_i)), sum alpha_i = -1, i = 1,2; Gl. (13) alpha_a = -a/(a-b) <= -1, alpha_b >= 0; Amplituden durch Reichweiten festgelegt.
  - Schranke: "exclude |alpha| = 1 for lambda > 38.6 um at 95 %" [Lee 2020], frueher 56 um [Kapner 2007] -> ell_1 <~ 4e-5 m. Also Einzel-Yukawa-Ablesung, keine gemeinsame Zwei-Term-Anpassung.
  - Stelle nur als Analogie erwaehnt, Koeffizienten 1/3, -4/3 nicht genannt (laut Auszug). -> Erwartung R6 bestaetigt; S3 im strengen Sinn weiter eingetroffen, aber Beinahe-Fall dokumentieren.
  - [E] Stelle-Amplituden in Pszota-Parametrisierung: alpha_a = -4/3 verlangt a = 4b, also lambda_a = 2 lambda_b; bei Stelle sind die Reichweiten dagegen frei und die Amplituden fest -> verschiedene Familien, nur Vorzeichenstruktur und Summe -1 gemeinsam.
- R7 Eot-Wash (au:Adelberger/Heckel_B): juengste ISL-Arbeit weiter Lee 2020 (2002.11761). Danach nur EP-/Dunkle-Materie-/Kalibrator-Arbeiten (2024: Ross EP Supraleiter; Smith/Hoyle Kurzreichweiten-EP 2405.10982, Mai 2024, vor Fenster). Erwartung bestaetigt.
- R8 HUST (au:Shao_Cheng-Gang/Tan_Wen-Hai/Luo_Pengshun): seit 10/2024 keine ISL-Messung auf arXiv; nur TDI/TianQin/LLR-EP. Erwartung "evtl. neues HUST-Ergebnis" NICHT eingetroffen (auf arXiv). Gegenpruefung ausserhalb arXiv noetig.
### Block 5 (Gruppen gezielt), Erwartungen geschrieben 2026-10-02 19:09:43 CEST
- R9 au:Gratta (Stanford, schwebende Mikrokugeln) -> Erwartung: evtl. ein neues Ergebnis 2025 bei 1-10 um, alpha >> 1 (nicht bei alpha = 1).
- R10 au:Decca (IUPUI) -> Erwartung: keine neue Messung seit 10/2024.
- R11 au:Sedmik (CANNEX) -> Erwartung: Apparate-/Statusarbeiten, evtl. erste Casimir-Messung; Schranken nur unter ~10 um.
- R12 au:Abele_H (qBounce) -> Erwartung: evtl. neue Gravitationsresonanz-Schranke; alpha riesig (~1e20) bei um.
#### Ausgang Block 5 (eingetragen 2026-10-02 19:10:24 CEST)
- R9 Gratta: **2412.13167 Venugopalan, Hardy, Kohn, Zhu, ..., Gratta (17.12.2024), "Optomechanical vector sensing of new forces at 6 micron separation"**: laut API-Zusammenfassung alpha < 1e7 bei lambda ~ 5 um, < 1e6 fuer lambda >= 10 um. [L?]
  - -> S1 eingetroffen (neues Kurzabstandsergebnis im Fenster). Erwartung R9 bestaetigt (alpha >> 1, kein Einfluss auf 38,6 um).
- R10 Decca: seit 10/2024 nur eine Nicht-Physik-Arbeit (2510.13365). Bestaetigt.
- R11 Sedmik/CANNEX: juengste 2403.10998 (Maerz 2024, Design-Review), keine Messung im Fenster. Bestaetigt.
- R12 Abele: seit 10/2024 nur NUCLEUS-/CRAB-Arbeiten, kein qBounce-Ergebnis auf arXiv. Bestaetigt (keine neue GRS-Schranke gefunden).
### Block 6, Erwartungen geschrieben 2026-10-02 19:10:24 CEST
- R13 arXiv abs 2412.13167 (Venugopalan) -> Erwartung: Schranke alpha ~ 1e6-1e7 bei 5-10 um, 95 %, Abstand 6 um; Journal evtl. PRL/PRD 2025.
- R14 Semantic Scholar "gravitational inverse-square law test" 2024-2026 -> Erwartung: findet Murata, Venugopalan; evtl. eine nicht-arXiv-HUST-Arbeit.
- R15 arXiv all:neutron AND all:Yukawa (Datum) -> Erwartung: 0-2 neue Neutronenschranken im Fenster, alle bei lambda < 1 um bzw. alpha >> 1.
- R16 arXiv all:inverse AND all:square AND all:torsion (Datum) -> Erwartung: keine neue Torsionsmessung im Fenster.
#### Ausgang Block 6 (eingetragen 2026-10-02 19:11:20 CEST)
- R13 Venugopalan u. a. 2024/2026: Sci. Rep. 16, 5180 (2026), DOI 10.1038/s41598-026-35656-6, arXiv:2412.13167 (v2 11.04.2026). Abstract [L?]: "upper limit ... 10^7 at ... lambda ~ 5 um and close to 10^6 for lambda >~ 10 um"; Konfidenzniveau im Abstract nicht genannt. Erwartung bestaetigt, Journal war nicht PRL/PRD sondern Sci. Rep. (unerheblich).
- R14 Semantic Scholar: HTTP 429 (Fehlschlag). Ersatzkanal Crossref.
- R15 Neutronen: seit 10/2024 keine neue Neutronen-Yukawa-Schranke auf arXiv in dieser Abfrage (juengste: Heacock 2021, 20 pm-10 nm). Bestaetigt.
- R16 Torsion + inverse square: keine neue Torsionsmessung im Fenster; juengste Manley 2406.13020 (Vorschlag, Juni 2024). Bestaetigt.
  - Nebenbefund: die HUST-ISL-Arbeiten 2016/2020 erscheinen in KEINER der arXiv-Abfragen -> HUST publiziert womoeglich ohne arXiv; Journal-Kanal (Crossref) noetig. Das ist eine Luecke der bisherigen Suche.
### Block 7 (Journal-Kanal Crossref + Frage 3), Erwartungen geschrieben 2026-10-02 19:11:20 CEST
- R17 Crossref query "inverse-square law submillimeter torsion" ab 2024-10-01 -> Erwartung: keine neue HUST-/UW-Messung in PRL/PRD; evtl. CPL/Chinese Physics B.
- R18 Crossref query "non-Newtonian gravity micrometer Yukawa constraint" ab 2024-10-01 -> Erwartung: Casimir-/Mikrokugel-Arbeiten, Venugopalan, nichts unter 38,6 um bei alpha = 1.
- R19 arXiv all:"quadratic gravity" AND all:Yukawa (Datum) -> Erwartung: 1-3 Theorie-Arbeiten im Fenster, zitieren Eot-Wash nur pauschal (m2 >~ meV).
- R20 arXiv all:Stelle AND all:Newtonian AND all:potential (Datum) -> Erwartung: Theoriearbeiten zum Potential (Singularitaetsfreiheit), keine Datenanpassung.
#### Ausgang Block 7 (eingetragen 2026-10-02 19:12:19 CEST)
- R17 Crossref (inverse-square/submillimeter/torsion): kein neuer ISL-Messartikel im Fenster; nur Methodik (Xu 2026, EPJ Plus, "Thermal lag effect in torsion pendulum", DOI 10.1140/epjp/s13360-026-07827-x [L?, nur Titel]). Erwartung bestaetigt.
- R18 Crossref (non-Newtonian/Yukawa/micrometer), neu und zu pruefen:
  - **PRD 2026-09-30, DOI 10.1103/tsc9-s1dv, "Probing Yukawa gravity with modulated Newtonian cancellation in the torsion bar type detector"** (Autor in Crossref leer) [L?, nur Titel].
  - **Amaral u. a., PRD 2026-01-27, DOI 10.1103/pqrs-bpgj, "Magnetic levitation as a new probe of non-Newtonian gravity"** [L?, nur Titel].
  - Park u. a. PRD 2026 (Cassini, Sonnensystem), Zhu/Li EPJC 2026 (s. R3) -> nicht Kurzabstand.
- R19 arXiv "quadratic gravity" + Yukawa: 4 Arbeiten im Fenster (Peng 2605.02955, da Rocha 2601.22268, Bhattacharyya 2508.02785, Hurtado 2506.15123), laut Abstract keine Laborauswertung. Erwartung bestaetigt (sogar ohne pauschales Eot-Wash-Zitat im Abstract).
- R20 arXiv Stelle + Newtonian + potential: nur 1 Treffer (Modesto 2012) -> Abfrage untauglich (Fehlschlag), nicht als Fehlanzeige werten.
### Block 8 (Gegensweep Rekordschranken), Erwartungen geschrieben 2026-10-02 19:12:19 CEST
- R21 Crossref-Metadaten 10.1103/tsc9-s1dv -> Erwartung: TOBA-Vorschlag/Analyse, Reichweite cm bis m, keine Sub-mm-Messung.
- R22 Crossref-Metadaten 10.1103/pqrs-bpgj -> Erwartung: Vorschlag (supraleitende Levitation), projizierte Empfindlichkeit, keine Messung.
- R23 arXiv au:Hoyle_C (Humboldt) -> Erwartung: keine neue ISL-Schranke im Fenster.
- R24 arXiv all:levitated AND all:Yukawa (Datum) -> Erwartung: Vorschlaege und Venugopalan; nichts bei alpha ~ 1.
#### Ausgang Block 8 (eingetragen 2026-10-02 19:13:06 CEST)
- R21 PRD 10.1103/tsc9-s1dv: Crossref ohne Autoren, ohne Abstract, ohne arXiv-Bezug -> offen; arXiv-Titelsuche noetig.
- R22 Amaral, Fuchs, Ulbricht, Tunnell, PRD 113, L021101 (27.01.2026), arXiv:2506.17385: MORRIS, Vorschlag; projiziert alpha <~ 1e-5 bei mm-Reichweiten [L?, Crossref-Abstract]. Erwartung bestaetigt (Vorschlag, keine Messung).
- R23 Hoyle: keine ISL-Arbeit im Fenster (juengste Smith/Hoyle 2405.10982, Mai 2024, EP-Test bis 1 cm). Bestaetigt.
- R24 levitated + Yukawa: im Fenster nur Venugopalan (Messung, alpha ~ 1e6-1e7), Amaral (Vorschlag), Ren (Vorschlag), Chowdhury 2410.21718 (Vorschlag). Bestaetigt.
### Block 9, Erwartungen geschrieben 2026-10-02 19:13:06 CEST
- R25 arXiv ti:"torsion bar" AND all:Yukawa -> Erwartung: TOBA-Arbeit (Japan), Reichweite cm-m; Messung oder Vorschlag unklar.
- R26 OpenAlex title_and_abstract.search:"inverse-square law" torsion ab 2024-10-01 -> Erwartung: keine neue Sub-mm-Messung (HUST-Gegenpruefung ausserhalb arXiv).
- R27 Lee 2020 PDF (arXiv:2002.11761) lokal im Kartenordner, Abb. 5 selbst ansehen -> Erwartung: |alpha| = 1 bei 38,6 um; |alpha| = 4/3 bei ~40-42 um (Kurve faellt steil); Vorzeichen: Schranke fuer |alpha|, beide Vorzeichen.
- R28 Murata-Review HTML: Abbildungsliste per curl|grep -> Erwartung: eine Yukawa-Abbildung 1 um - 1 m mit Eot-Wash 2020 als Grenzkurve bei 10-100 um.
#### Ausgang Block 9 (eingetragen 2026-10-02 19:13:53 CEST)
- R25 PRD 10.1103/tsc9-s1dv ~~= arXiv:2604.11167~~ vermutlich = arXiv:2604.11167 (Titel fast gleich: "torsion bar type detector" vs. "CHRONOS Detector"; Identitaet [H], beim Gegenlesen 19:23 praezisiert), Inoue, Huang, Kumar, Tanabe u. a., "Probing Yukawa Gravity with Modulated Newtonian Cancellation in the CHRONOS Detector": Empfindlichkeitsstudie, bestes |alpha| = 2,4e-5 bei lambda = 8 m [L?, API-Abstract]. Erwartung bestaetigt (cm-m-Bereich, keine Sub-mm-Messung).
- R26 OpenAlex "inverse-square law" + torsion: 102 Treffer, Seite 1 fast nur Zenodo-Rauschen; einzig relevant Manley u. a., PRD 110, 122005 (20.12.2024), Journalfassung des Vorschlags 2406.13020. Keine HUST-Messung gefunden. Bestaetigt (mit Kanalvorbehalt).
- R27 Lee 2020 PDF geladen nach quellen/lee2020-arXiv-2002.11761.pdf (856 030 Byte, 5 Seiten).
- R28 Murata-Review: Abbildungen Fig. 1 alpha-lambda-fullscale-2025, Fig. 3 alpha-lambda-shortscale-2025, Fig. 4 alpha-lambda-microscale-2025, Fig. 7 UW, Fig. 8 HUST, Fig. 9 Decca. Erwartung (Yukawa-Abbildung vorhanden) bestaetigt; Inhalt folgt.
#### R28 Murata-Review Fig. 3, selbst angesehen (eingetragen 2026-10-02 19:14:28 CEST) [S]
- Datei quellen/murata2026-fig3-alpha-lambda-shortscale-2025.png (aus arXiv-HTML 2605.18212v2). Achse "alpha (alpha > 0)", lambda 1e-6 bis 1e2 m.
- Bildunterschrift (Textauszug per curl|sed): "dark shaded area shows the improved constraints obtained over the last decade"; neue Kurven: Washington 2020 [Lee 2020], HUST 2016/2020/2021, Vienna 2021 (Westphal, Nature 591), Rikkyo 2015/2017, Atom (Panda 2024, Nature 631).
- Abgelesen (grob, Augenmass auf log-Achsen): Die Grenzkurve schneidet alpha = 1 bei lambda ~ 3,5-4e-5 m, getragen von "Washington 2020"; keine juengere Kurve im Bereich 10-100 um. Bei lambda = 1e-5 m liegt die Grenze grob bei alpha ~ 1e3 (Augenmass).
- Venugopalan 2024/2026 (alpha ~ 1e6 bei >= 10 um) ist NICHT eingezeichnet; nach Augenmass waere es dort ~3 Groessenordnungen schwaecher als die Grenzkurve [H].
- Abbildung zeigt nur alpha > 0. Stelle-Spin-2-Term hat alpha < 0 -> Vorzeichenfrage offen (Gegensweep-Punkt).
- Weitere Textstelle: HUST-Mikrometer-Torsionswaage gibt im Potenzgesetz-Fall n = 2 "Lambda < 11 um" (andere Parametrisierung, nicht |alpha| = 1-Yukawa).
- Zitierte HUST-Arbeiten: Tan 2016 PRL 116, 131101; Tan 2020 PRL 124, 051301; Ke 2021 PRL 126, 211101 (Zentimeterbereich). Keine HUST-Arbeit nach 2021 zitiert.
- -> Erwartung R5/R28 bestaetigt: Lee 2020 ist im Review von 09/2026 die Grenzkurve bei alpha = 1.
#### R27 Lee 2020, PDF S. 4-5 selbst gelesen (eingetragen 2026-10-02 19:15:13 CEST) [S]
- Fig. 5 unten: "corresponding 95% confidence upper limits on |alpha|" (Bildunterschrift).
- S. 5: "2 sigma constraints on |alpha| (constraints on +alpha and -alpha are given in Supplemental Material [27])".
  - ERWARTUNGSVERSTOSS (zu R27 "beide Vorzeichen in einer Kurve"): Die Hauptabbildung zeigt |alpha|; getrennte Schranken fuer +alpha und -alpha stehen nur im Supplement. Fuer Stelle (+1/3 und -4/3) ist genau diese Trennung noetig.
- S. 5: "any gravitational-strength Yukawa interaction must have lambda < 38.6 um"; daraus "dilaton [28] or heavy graviton [3] mass ... greater than 5.1 meV".
  - ERWARTUNGSVERSTOSS (Herkunft der 5,1 meV): Die 5,1-meV-Umrechnung steht schon bei Lee u. a. selbst, fuer Dilaton bzw. "heavy graviton" (Ref. [3] Aoki/Mukohyama, PRD 94, 024001, 2016, Bigravitation), nicht fuer Stelle. Unser Nachtrag 27.09. hat sie also nachgerechnet, nicht erfunden; die Berichtigung 29.09. bleibt richtig, weil Lee den Einzel-Yukawa-Fall meint.
- Abgelesen (Augenmass, PDF-Seitenbild klein): Grenzkurve Eot-Wash 2020 bei |alpha| = 10 grob lambda ~ 2,5e-5 m, bei |alpha| = 1 bei 3,86e-5 m. Fuer |alpha| = 4/3 (0,125 Dekaden ueber 1) grob 36-37 um [E, Interpolation]; ~~fuer |alpha| = 1/3 grob 4-5e-5 m [E, unsicher].~~ (gestrichen 19:21, ersetzt durch die Ablesung an fig5b1.pdf unten: ~55-58 um)
- Naechster Schritt: Original-Abbildung aus arXiv-Quellpaket (e-print) und Supplement (+/-alpha) versuchen.
### Block 10, Erwartungen geschrieben 2026-10-02 19:15:13 CEST
- R29 arXiv e-print 2002.11761 (Quellpaket) -> Erwartung: enthaelt Fig. 5 als PDF/EPS, evtl. Supplement-Tabelle (+alpha/-alpha); wenn Supplement fehlt, bleibt Vorzeichenfrage [L?].
- R30 APS-Supplement PRL 124, 101101 -> Erwartung: Abruf blockiert (403/Cloudflare).
#### R29 Lee 2020 Quellpaket (eingetragen 2026-10-02 19:16:27 CEST) [S]
- e-print enthaelt fig5b1.pdf und FB_ISL_pdf.tex, aber KEIN Supplement (Verweis "See Supplemental Material at XXXX"). Erwartung teilweise verletzt (Supplement fehlt) -> Vorzeichenfrage bleibt [L?].
- tex Z. 43: V(r) = V_N(r) [1 + alpha exp(-r/lambda)] -> gleiche Normierung wie Stelle-Form (Vorfaktoren direkt als alpha lesbar).
- tex Z. 150: Einzel-Yukawa-Anpassung fuer 66 lambda-Werte zwischen 5 um und 9 mm; keine Zwei-Term-Anpassung.
- fig5b1.pdf selbst angesehen (gross). Pixel-Achsen: Dekade x ~ 300 px (1e-5 bei x ~ 500), Dekade y ~ 81 px (|alpha| = 1 bei y ~ 597).
  - |alpha| = 1: Grenze bei x ~ 676 = 38,6 um (stimmt mit Text). 
  - |alpha| = 4/3 (y ~ 587): Grenze bei x ~ 664-669 -> lambda ~ 35-37 um [E, Augenmass]; m >~ 1,973e-7 / 3,6e-5 ~ 5,3-5,6 meV [E].
  - |alpha| = 1/3 (y ~ 635, liegt auf der unteren "radion"-Linie der Abbildung): gruene Flaeche (Gewinn 2020) endet dort bei x ~ 727 -> lambda ~ 55-58 um [E, Augenmass]; m >~ 1,973e-7 / 5,7e-5 ~ 3,4-3,6 meV [E].
  - Korrektur der eigenen Vorab-Schaetzung "1/3 bei ~45 um" -> tatsaechlich ~57 um (Kurve flacht unter |alpha| = 1 stark ab).
- [H] Zwei Regime fuer die Stelle-Form delta(r) = (1/3) e^(-m0 r) - (4/3) e^(-m2 r):
  - Regime A, m0 >= m2: Spin-2-Term ueberwiegt bei jedem r, kein Vorzeichenwechsel; effektiv ein negativer Yukawa mit |alpha| zwischen 1 und 4/3 -> m2 >~ 5,1-5,6 meV, vorbehaltlich der -alpha-Schranke im Supplement.
  - Regime B, m0 < m2: Vorzeichenwechsel bei r* = ln 4 / (m2 - m0); teilweise Aufhebung; keine Einzelkurven-Ablesung zulaessig, gemeinsame Auswertung mit Apparateantwort noetig.
  - Grenzfaelle: m0 -> unendlich: m2 >~ ~5,5 meV; m2 -> unendlich: m0 >~ ~3,5 meV; m0 = m2: alpha = -1 -> 5,1 meV (wieder -alpha-Vorbehalt).
### Block 11, Erwartungen geschrieben 2026-10-02 19:16:27 CEST
- R30 APS-Supplement PRL 124, 101101 -> Erwartung: blockiert (403).
- R31 arXiv HTML 2412.13167v2 (Venugopalan) -> Erwartung: 95 % CL; alpha ~ 1e6 bei 10-30 um; Abbildung zeigt sie oberhalb Eot-Wash/IUPUI-Grenze.
- R32 arXiv abs Fiorillo u. a. (Neutronenstern-Kuehlung) -> Erwartung: Reichweite pm bis ~1 um, nur fuer alpha >> 1; irrelevant bei 30-60 um und alpha ~ 1.
- R33 arXiv all:"quadratic gravity" AND all:laboratory (Datum) -> Erwartung: keine Fenster-Arbeit mit eigener Zwei-Term-Auswertung.
#### Ausgang Block 11 (eingetragen 2026-10-02 19:17:09 CEST)
- R30 APS-Supplement: HTTP 401 (Fehlschlag, wie erwartet). +alpha/-alpha-Schranken von Lee 2020 nach Recherchestand nicht eingesehen.
- R31 Venugopalan, Volltext-HTML 2412.13167v2 (WebFetch-Auszug mit Zitaten): "95% confidence level limit on alpha for each sign" (Wilks); lambda 1-100 um; Abstand ~6 um; Verbesserung "factor of ~50 over previous results" fuer lambda > 10 um bezieht sich auf fruehere Ergebnisse derselben Technik; Fig. 4 zeigt Lee 2020, Chen 2016 u. a. als bereits ausgeschlossen. [S Textstellen; Abbildung nicht selbst gesehen]. Erwartung bestaetigt.
- R32 Fiorillo, Lella, O'Hare, Vitagliano, arXiv:2506.19906 = PRL 135, 211003 (2025): Reichweite 1e-6 bis 1e-12 m, Skalare m_phi eV-MeV, g_N <~ 5e-14 [L?, Abstract].
  - [E] alpha = g_N^2/(4 pi) / (m_N/M_Pl)^2 ~ (2e-28)/(5,9e-39) ~ 3e10 -> weit ueber alpha = 1 und unter 1 um. Irrelevant fuer Frage 2. Erwartung bestaetigt.
  - Nebenfund: Fiorillo u. a. arXiv:2605.24094 (Mai 2026), muonische fuenfte Kraefte -> irrelevant.
- R33 "quadratic gravity" + laboratory: im Fenster nur Zhu/Li (Sonnensystem) und Liu/Quintin/Afshordi 2510.18733 (Kosmologie). Bestaetigt.
### Block 12 (Gegenprobe S3), Erwartungen geschrieben 2026-10-02 19:17:09 CEST
- R34 arXiv all:Stelle AND all:Yukawa (Datum) -> Erwartung: wenige Arbeiten; im Fenster hoechstens Theorie ohne Datenanpassung.
- R35 arXiv all:"Lee-Wick" AND all:gravity AND all:potential (Datum) -> Erwartung: Theorie zu Potentialen; evtl. eine Arbeit, die Eot-Wash-Schranke auf Massen umrechnet (Einzel-Yukawa).
- R36 arXiv all:"higher-derivative" AND all:Yukawa AND all:gravity (Datum) -> Erwartung: wie R35.
#### Ausgang Block 12 (eingetragen 2026-10-02 19:17:44 CEST)
- R34 Stelle + Yukawa: nur Fluid-Arbeiten (Namensgleichheit "Stell"); Abfrage untauglich, keine Fehlanzeige daraus.
- R35 Lee-Wick + gravity + potential: im Fenster einzig Pszota/Van 2026 mit Laborvergleich; sonst Theorie ohne Daten. Bestaetigt.
- R36 higher-derivative + Yukawa + gravity: im Fenster Ewasiuk/Profumo 2509.02801 (grosse dunkle Sektoren, nutzt Fuenfte-Kraft-Daten, nicht Stelle) [L?]; sonst nichts. Bestaetigt.
### Block 13, Erwartungen geschrieben 2026-10-02 19:17:44 CEST
- R37 Pszota-HTML per curl|grep (Wortlaut selbst) -> Erwartung: Saetze mit 38.6, Stelle, sum rule wie im WebFetch-Auszug.
- R38 arXiv abs 2603.16026 (Balfagon, Ringdown/Spektraldichte) -> Erwartung: Theorie, Sub-mm nur als Bemerkung, keine Zwei-Term-Auswertung.
#### Ausgang Block 13 (eingetragen 2026-10-02 19:18:30 CEST)
- R37 Pszota/Van 2609.00317v1, Wortlaut selbst per curl|sed gelesen [S]:
  - Gl. (11) phi = -GM/r (1 + sum alpha_i e^(-r/lambda_i)), sum alpha_i = -1, "equivalent to regularity at the origin"; Gl. (13) alpha_a <= -1, alpha_b >= 0; "amplitudes are therefore fixed by the ranges".
  - "Torsion-balance experiments exclude |alpha| = 1 for lambda > 38.6 um at 95% confidence [11]" -> Gl. (14) ell_1 <~ 4e-5 m. Einzel-Yukawa-Ablesung, keine eigene Datenanpassung.
  - Stelle nur als Beispiel fuer Vakuuminstabilitaet zitiert (Stelle 1977, PRD 16, 953). Koeffizienten 1/3, -4/3 kommen nicht vor.
  - Zusatz [S]: statisches Potential aus Einteilchenaustausch mit nichtnegativer Spektraldichte "cannot change sign"; Vorzeichenwechsel braucht Lee-Wick-Pole.
  - [E] In der Pszota-Familie entsteht das Stelle-Muster (-4/3, +1/3) nur bei lambda_a = 2 lambda_b, also m0 = 2 m2 (Regime A, kein Vorzeichenwechsel).
  - [H] Passt zu Regime B: Stelles Spin-2-Geist hat negative Norm, damit ist der Vorzeichenwechsel bei m0 < m2 erlaubt.
- R38 Balfagon 2603.16026 (physics.gen-ph): nichtlokale Kerne, Ringdown; Sub-mm nur als "most promising path" [L?]. Erwartung bestaetigt; nicht Stelle.
## 4. Gegensweep (Phase 1), geschrieben 2026-10-02 19:18:30 CEST
Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- G1: Atominterferometrie im Fenster nie gezielt abgefragt (nur Panda 2024, vor dem Fenster). -> PRUEFEN (R39).
- G2: Dass 38,6 um auch fuer negatives alpha gilt (Stelle-Spin-2-Term ist negativ). Lee zeigt |alpha|; +/-alpha nur im Supplement (401). -> bleibt offen.
- G3: Dass HUST nicht ausserhalb arXiv/Crossref-Stichwort (z. B. Chinese Physics Letters) neu gemessen hat. -> PRUEFEN (R40, Crossref "torsion pendulum Yukawa").
- G4: Dass die Stelle-Vorfaktoren in derselben Normierung stehen wie die alpha der Experimente. Lee tex Z. 43: V = V_N (1 + alpha e^(-r/lambda)) [S]; Stelle-Form aus der Karte (Lue u. a. 2015, Gl. 4.7) hier nicht neu gelesen.
- G5: Dass "Gravitationsstaerke" bei Lee |alpha| = 1 (und nicht |alpha| >= 1) meint: tex Z. 33 "gravitational-strength Yukawa interactions to ranges < 38.6 um" [S]. Erledigt.
### Block 14 (Gegensweep-Pruefungen), Erwartungen geschrieben 2026-10-02 19:18:30 CEST
- R39 arXiv all:"atom interferometer" AND all:"fifth force" (Datum) -> Erwartung: Arbeiten im Fenster, aber Reichweiten mm-m bzw. alpha >> 1 unter 100 um.
- R40 Crossref "torsion pendulum Yukawa submillimeter" ab 2024-10-01 -> Erwartung: keine neue HUST-Messung.
#### Ausgang Block 14 (eingetragen 2026-10-02 19:19:18 CEST)
- R39 (G1 geprueft) Atominterferometrie im Fenster: nur Vorschlaege/Theorie (Banks u. a. 2511.09750 abgeschirmte Skalare, Langbasis; Millington/Udemba 2606.28423 Symmetron; Horchani 2511.21576; Hu u. a. 2503.24087). Keine Messung mit Sub-mm-Yukawa-Schranke. Erwartung bestaetigt.
- R40 (G3 geprueft) Crossref Torsionspendel: im Fenster nur Methodik (Manley u. a. Phys. Rev. Applied 2026, DOI 10.1103/mnrd-3bm2, nanofabrizierte Aufhaengungen; Okuma u. a. PRD 111, 082006 (2025), Kreuzkorrelation; Xu EPJ Plus 2026; Raumfahrt-Inertialsensoren). Keine neue HUST- oder UW-ISL-Messung. Erwartung bestaetigt.
### Block 15 (letzte Gegenprobe S2), Erwartungen geschrieben 2026-10-02 19:19:18 CEST
- R41 INSPIRE-HEP Titelsuche "inverse square law" ab 2024-10 -> Erwartung: Murata-Review, keine neue Rekordmessung.
- R42 Eot-Wash-Gruppenseite (npl.washington.edu/eotwash) -> Erwartung: juengste Kurzabstandsveroeffentlichung Lee 2020; evtl. Hinweis auf laufendes Nachfolgeexperiment ohne Ergebnis.
#### Ausgang Block 15 (eingetragen 2026-10-02 19:20:30 CEST)
- R41 INSPIRE-HEP, Titel "inverse square law", ab 2024-10-01: genau 1 Treffer (Murata u. a. 2605.18212). Bestaetigt.
- R42 Eot-Wash-Publikationsseite: juengstes Kurzabstandsergebnis weiter Lee 2020; danach Instrumente (Ross 2021 RSI; Fleischer 2022 RSI, kryogene Torsionswaage) und EP/Dunkle Materie (2024/2025). Bestaetigt [L?, Seitenauszug].

## 5. Zwischenstand vor dem Schreiben (eingetragen 2026-10-02 19:20:30 CEST)
- S1 eingetroffen (Venugopalan 2024/2026). S2 eingetroffen (nichts unter 38,6 um, geschweige 30 um). S3 eingetroffen im strengen Sinn; Beinahe-Fall Pszota/Van 2026 (Zwei-Term-Form mit Summe -1, Einzel-Yukawa-Ablesung, nicht Stelle-Koeffizienten); Zhu/Li 2026 quadratische Gravitation nur Sonnensystem.
- Kalibrierung: Gewissheit fuer S2 ist im Lauf gestiegen, waehrend die eigentliche Frage (Massenschranke Stelle) feiner zerfiel: zwei Massen, zwei Regime, Vorzeichenvorbehalt. Warnzeichen -> in den Bericht.
- [E] Zhu/Li 23 AU^-1: 23 / 1,496e11 m ~ 1,5e-10 m^-1 -> m ~ 1,5e-10 * 1,973e-7 eV ~ 3e-17 eV; Laborschranke (~5 meV) ist ~14 Groessenordnungen staerker.
- [E] Pszota ell_1 <~ 4e-5 m entspricht 1,973e-7 / 4e-5 ~ 4,9 meV.

## 6. Abschluss (eingetragen 2026-10-02 19:23:20 CEST)
- ERGEBNIS.md geschrieben ab 19:20:51 CEST (date), danach rueckwaerts gegengelesen: zwei Praezisierungen (PRD-TOBA-Identitaet nur [H]; Kanalzahl "fuenf + Uebersicht" statt "sieben"), ein Zusatz (Ewasiuk/Profumo bei S3).
- quellen/lee2020-eprint/eprint.bin nach dem Entpacken entfernt; behalten: fig5b1.pdf, FB_ISL_pdf.tex, lee2020-arXiv-2002.11761.pdf, murata2026-fig3-*.png, murata2026-fig8-HUST.png.
- Offene Rueckfragen wandern mit (ERGEBNIS 6.4): +/-alpha-Supplement Lee 2020; Zwei-Term-Auswertung Regime B; Eot-Wash-Nachfolgeexperiment; van Manen 2026 ungeprueft.
