# ARBEITSFELD REGGE-HADRON-REF-L (feldforscher, eine Datei, wird vor jedem Schritt neu gelesen)

- Start 2026-10-05 04:42:20 CEST (date). Zeitbox 90 min, also Ende spaetestens ~06:12 CEST.
- Auftrag: Karte KARTE.md (RH1-RH5 unveraendert). Finn woertlich: "Check in einem subagents Alle Referenzen hier
  https://arxiv.org/pdf/2512.21805 und ordne das ein".
- Abrufbudget 45 (curl nur arxiv.org, export.arxiv.org, inspirehep.net/api, api.crossref.org), Websuche max. 3.
- Gestrichenes bleibt stehen (~~so~~), offene Fragen wandern sichtbar mit (Abschnitt O).

## Projektkontext (gelesen 04:42-04:43, nur gezielte Stellen)

- gluon-paar-l/DOSSIER.md: Finns rotierendes Paar = Glueball-Bild der Pomeron-Trajektorie (Meyer/Teper 2004);
  Gitter 2 pi sigma alpha' = 0,281(22) (MT) bzw. 0,372(20) (aus A&T 2020); PAAR-REGGE-1 (Paar mit fester Endmasse);
  R1-R4, O1 (kein Fit rotierender Strings mit Endmassen an Gitter-Glueballs gefunden), O2.
- CEMZ-MESS.md Z. 102, 215, 323: Eckner/Figueroa/Metayer/Tourkine 2512.17828: "infinitely many Regge trajectories
  ... forced to have a stringy spectrum".
- brief-astra-regge-20260912.md Z. 1-10: Regge-Trajektorie (rotierender QCD-String, J = alpha' M^2, alpha' ~ 0,9 GeV^-2)
  als "einzige Stelle" mit Messzahl.
- WARUM-SPIN-2.md Z. 248 ff.: Glied 7 = "nicht Spin 3 oder hoeher" (Weinberg 1964, Weinberg-Witten 1980), Nachtraege
  24.09., 30.09. (CEMZ nur bedingt), 01.10.

## Abrufprotokoll mit Erwartung vor dem Abruf (Regel 3)

### Buendel B1 (A1 PDF, A2 INSPIRE-Datensatz mit Referenzen)
- Erwartung geschrieben 2026-10-05 04:42:59 CEST (date), vor A1/A2:
  - A1: PDF ~23 Seiten, numerierte Referenzliste mit 100 bis 160 Eintraegen, ueberwiegend Zeitschrift+Band+Seite+Jahr,
    selten Titel (hep-ph-Stil); Geschichte (Regge 1959, Chew/Frautschi, Gribov, Veneziano), JPAC-Arbeiten zahlreich.
  - A2: INSPIRE hat den Datensatz mit geparster Referenzliste; 85 bis 95 % der Referenzen einem Datensatz zugeordnet,
    der Rest Buecher und alte Arbeiten.
- **Ausgang B1:**
  - A1 HTTP 200, 23 Seiten, sha256 9b69857a...; Text in quellen/A1-2512.21805v1{,-layout}.txt.
  - **Referenzliste: 238 Eintraege** (erwartet 100-160: Verstoss, mild). **Jede Referenz mit Titel, fast alle mit DOI**
    (erwartet "selten Titel": Verstoss). Das erleichtert die Pruefung: DOI und Titel lassen sich gegeneinander halten.
  - A2 HTTP 200, INSPIRE recid 3095817: 243 Eintraege = 238 + 5 Errata-Zeilen (Nr. 174, 179, 192, 196, 209 doppelt).
    224 von 238 Nummern einem Datensatz zugeordnet (94,1 %, in der Erwartung), 224 verschiedene recids.
  - Unzugeordnet (14): 5, 6, 10, 53, 55 (Buecher), 41 (unveroeffentlicht), 58 (Technischer Bericht), 9 (Watson 1918),
    16 (Abbe 1967), 24 (Fukutome 1957), 43 (Mandelstam, Ann. Phys.), 44 (Khuri PRL 1963), 100 (Cheng/Sharp 1963),
    101 (Frautschi/Kaus/Zachariasen 1964).
  - Neu: Der Artikel ist inzwischen erschienen: Encyclopedia of Particle Physics, Bd. 1 (2026) S. 681-704, Elsevier,
    DOI 10.1016/B978-0-443-26598-3.00042-0 (INSPIRE publication_info, parent_record 3204670); 6 Zitierungen.
    Affiliationen: Winney Bonn U., HISKP; Szczepaniak Indiana U./CEEM und Jefferson Lab (JPAC-Umfeld) [S INSPIRE].
  - Erstlesung der Liste (nur Gedaechtnis, noch zu pruefen [ES]): Nr. 43 "M. Mandelstam ... (1959)" mit DOI ...(62)...
    -> Initiale und Jahr verdaechtig; Nr. 30 Yukawa mit DOI der Nachdruck-Ausgabe PTPS 1 (1955); Nr. 59 JETP-Angabe mit
    DOI von Nucl. Phys. 40 (1963); Nr. 99 DOI ujpe66 (2021) zu einer Arbeit von 1977; Nr. 55 Jahr 2012 (Gribov-Buch?);
    Tippfehler in 43 ("extention"), 55 ("emnergies"), 75 ("Pomeranchuck", "NUCELON", "CORSS"), 101 ("te").

### Buendel B2 (A3, A4: INSPIRE, 224 zugeordnete recids in zwei Abrufen, mit Abstracts)
- Erwartung geschrieben 2026-10-05 04:44:15 CEST (date), vor A3/A4:
  - Die Zuordnung von INSPIRE stimmt fuer >= 98 % (sie laeuft ueber die DOIs). Abgleich Autor/Zeitschrift/Band/Seite/Jahr:
    5 bis 15 kleine Fehler (Jahr Druck gegen online, Seitenbereich, Initialen, Tippfehler im Titel), 0 bis 2 sachliche
    Fehler (falsche Arbeit unter richtiger Angabe). Keine erfundene Referenz.
- **Ausgang B2** (eingetragen 2026-10-05 04:47:06 CEST):
  - A3/A4 (112 recids je Abruf, mit Abstracts): beide **HTTP 502** (Antwort zu gross oder zu langsam), verbraucht.
  - A5-A8 (56 recids je Abruf, ohne Abstracts): alle HTTP 200, 224/224 Datensaetze.
  - Maschineller Abgleich mit jq (quellen/R-vergleich.txt, R-*-map.json):
    - Autoren: alle Nachnamen des Datensatzes stehen in der Referenz, ausser Unicode-Formen (Fernández-Ramírez
      mit punktlosem i, 't Hooft mit Apostroph, Müller, Biró, Montaña). Echte Abweichungen: Nr. 210 "J. R. de Elvira"
      statt J. Ruiz de Elvira; Nr. 75 "Pomeranchuck". Autorenzahl: bei allen pruefbaren Eintraegen gleich.
    - Titel (Satzzeichen/Gross-Klein ignoriert): alle gleich ausser LaTeX/MathML-Schreibweisen; echte Abweichung nur
      Nr. 75 (Tippfehler "NUCELON", "CORSS"); dazu Nr. 101 "te" statt "the" (Sichtpruefung).
    - Band/Jahr/Seite: alle gleich; Nr. 184 nur als Preprint zitiert, inzwischen Phys. Rev. C 112 (2025) 015204;
      Nr. 40 russische Originalangabe (ZhETF 41, 1961), Datensatz fuehrt die Uebersetzung (JETP 14, 1962): beides richtig.
    - DOIs: alle gleich; Abweichungen nur Trennstrich-Verlust am Zeilenumbruch im Text (12, 66, 77, 78, 119, 132, 166,
      198, 216), im PDF selbst richtig. Offen: Nr. 179 (zwei DOIs im Datensatz; welcher gehoert zum Original?).
    - Angabe und DOI zeigen auf verschiedene Ausgaben derselben Arbeit: Nr. 30 (Yukawa 1935, DOI des Nachdrucks PTPS 1),
      Nr. 52 (Collins 1977, DOI der Neuauflage 2023), Nr. 59 (JETP 15, 1962, DOI von Nucl. Phys. 40, 1963),
      Nr. 99 (Ukr. Fiz. Zh. 1977, DOI des Nachdrucks Ukr. J. Phys. 66, 2021).
  - Erwartung "5 bis 15 kleine Fehler, 0-2 sachliche, keine erfundene": **bislang eingetroffen** fuer den
    zugeordneten Teil (224). Die Zuordnung von INSPIRE laeuft ueber DOIs; sie ist damit nicht unabhaengig von der
    Angabe im Artikel [ES]. Gegenprobe: Titel und Autoren des Datensatzes stimmen, also passt DOI zu Titel.

## Lesung des Artikels (Volltext, Abschnitte 1-6 ganz gelesen) und Kontextpruefung "passt das Zitat zur Stelle?"

- Alle 238 Nummern im Text gegen Titel gehalten (Titel stehen in jeder Referenz). Ueberwiegend passend. Auffaellig [ES]:
  - K1 Abschn. 3, S. 8: "very slowly rising cross sections ... also observed in elastic pp, pp-bar, K+-p scattering
    [68-71]". [68]-[70] sind Messungen 1961-1965 bei 3-22 GeV/c, [71] eine Analyse von Differenzen (1965). Der Anstieg
    der Wirkungsquerschnitte wurde erst ~1971-73 (Serpukhov, ISR) gesehen [Gedaechtnis, ES]. -> Abstracts pruefen.
  - K2 Abschn. 5.1, S. 13: "GlueX [171], CLAS12 [172], COMPASS [173]": [172] ist der CLAS-Detektor (2003), nicht CLAS12.
    Ebenso S. 14 "CLAS12 data in Refs. [185, 186]": [186] traegt "using the CLAS detector" im Titel. -> Abstracts.
  - K3 Fig. 9 (S. 13): "Blue curve is predictions from the Regge pole model in Ref. [63]" ([63] = Pion-Photoproduktion);
    der Text S. 14 ordnet die Vektormeson-Vorhersage aber [181] zu. -> innere Unstimmigkeit; Volltext [175] pruefen.
  - K4 S. 14: "eta(') [180], vector [181], tensor [182] ... GlueX data in Refs. [175, 183, 184] respectively": die
    Reihenfolge passt nicht ([175] = rho-SDME, [183] = eta-Strahlasymmetrie). Vertauschung, keine falsche Quelle.
  - K5 S. 14: "A similar methodology is also used in Ref. [63, 180] for pion photoproduction": [180] ist eta/eta'.
  - K6 S. 11: "numerical simulations on the lattice [163-168]": [166] (Greensite/Thorn, Gluonkettenmodell) ist ein
    Modell, keine Gittersimulation; [163]-[165] pruefen (Coulomb-Eichung, teils Gitter).
  - K7 S. 9: "The pomeron is now usually ascribed to gluonic exchanges [79]": [79] ist von 1964 (vor QCD,
    "vacuum trajectory in conventional field theory"). Anachronistisch, -> Abstract.
  - K8 Fig. 4 / [46]: Bildunterschrift "pi0 p -> rho0 p", Titel im Datensatz "pi+- p ---> rho n". -> Crossref-Titel.
  - K9 Fig. 5 rechts: "spectrum of light mesons as of 2018 in Ref. [63]" -> Volltext [63] auf Chew-Frautschi-Bild pruefen.
  - Tippfehler im Fliesstext (kein Referenzfehler): "Frautshi" (2x), "Pomerachuk", "Pomeranchuck pole", "t'Hooft",
    Gl. (33) Text "alpha(s) = alpha0 + alpha' t", "discussed in Ref. 3" (gemeint Abschn. 3, 2x).
- RH-relevante Fundstellen [S]:
  - RH3: Kein "graviton", kein "AdS", kein "BPST" im Text (grep folgt). Holographie nur als [157], [161].
  - RH5: Susskind [129, 130] Federkette; Fussnote 14 String-Theorie [131-133]; S. 12 "stringy flux tube dynamics
    of gluons (Fig. 8) which underlie the harmonic oscillator-like Regge trajectories"; S. 15 "string-like structure
    as a q q-bar state". Kein Nambu-Goto-Rechenweg, keine Formel alpha' = 1/(2 pi sigma), keine "Enden mit c".
  - Wortzaehlung im Haupttext (Z. 1-1031): graviton 0, AdS 0, BPST/Brower/Polchinski 0, Nambu 0, "speed of light" 0,
    soliton/Q-ball/Skyrm 0, "Regge calculus" 0, "string tension" 0 (nur "tension" in "intention"? -> 3 Treffer sind
    "attention"/"extension"-Woerter, gesichtet), glueball 1 (S. 9), holographic 1 ([161]).

### Buendel B3 (A9: INSPIRE-Abstracts fuer die Zitat-Stichprobe und K1-K9, ein Abruf mit ~36 recids)
- Erwartung geschrieben 2026-10-05 04:50:12 CEST (date), vor A9:
  - K1: Die Abstracts von [68]-[70] berichten konstante oder fallende Gesamtwirkungsquerschnitte zwischen 3 und
    22 GeV/c, keinen Anstieg (70 %). Dann traegt [68-71] die Aussage "slowly rising" nicht.
  - K2: [185] und [186] nennen CLAS (nicht CLAS12) im Abstract (85 %).
  - K7: [79] behandelt die Vakuumtrajektorie in einer Feldtheorie mit Vektormesonen/Fermionen, keine Gluonen (75 %).
  - Stichprobe: [78] nennt epsilon ~ 0,08 und alpha' = 0,25 (85 %); [162] nennt die Pomeron-Steigung aus Glueballs
    (90 %); [130] traegt das Bild "quarks ... chain of springs" (50 %, Woertlichkeit unsicher); [150] nennt
    alpha(t -> -inf) = -1 fuer q q-bar-Austausch (60 %); [144] zeigt eine effektive rho-Trajektorie bis -t ~ 6 GeV^2
    (60 %); [14] behandelt das Kastenpotential (50 %).
  - Ein Teil der alten Datensaetze hat bei INSPIRE keinen Abstract (Erwartung: ~30-50 % der Vor-1975-Arbeiten ohne).
- **Ausgang B3** (eingetragen 2026-10-05 04:52:31 CEST): A9 HTTP 200, 36/36 Datensaetze, 30 mit Abstract (6 ohne: [68], [71], [40], [79],
  [61], [113]). Datei quellen/A9-abstracts.txt.
  - **K1 bestaetigt (Verstoss gegen die Lesart des Artikels):** [69] Baker 1963: "sigma_t(K+p) is, within errors,
    constant ... sigma_t(K-p) decreases gradually from 28 mb at 4 BeV/c to 21.6 mb at 19 BeV/c" [S Abstract].
    [70] Galbraith 1965: "evidence ... for a small but significant decrease in sigma_T(pp) ... above 12 GeV/c"
    [S Abstract]. Die Quellen zeigen konstante oder fallende, nicht steigende Wirkungsquerschnitte. [68], [71] ohne
    Abstract. Zwei Regime: Daten bis ~22 GeV/c (1961-65) gegen ISR/Tevatron/LHC (Anstieg). Moderator: Energie.
    Die Quellen tragen die Pomeranchuk-Motivation (alpha(0) ~ 1), nicht das Wort "rising".
  - **K2 bestaetigt:** [172] beschreibt CLAS (2003); [185] "CEBAF Large Acceptance Spectrometer", 3,5-5,5 GeV;
    [186] "using the CLAS detector", 3,6-5,4 GeV [S Abstract]. "CLAS12" im Text ist ein falsches Etikett.
  - **K3 gestuetzt:** [181] "predictions for ... spin-density matrix elements in photoproduction of omega, rho0 and phi
    at E_gamma ~ 8.5 GeV" [S Abstract]; [63] behandelt FESR der Pion-Photoproduktion [S Abstract]. Fig. 9 nennt [63];
    passend waere [181] [ES]. Volltext [175] zur Bestaetigung (B4).
  - **K6 bestaetigt fuer [166]:** "We develop a picture of the QCD string as a chain of constituent gluons" (Modell);
    [163] "via numerical simulations" (Coulomb-Eichung), [164] "SU(2) Yang-Mills lattice simulation", [165] "SU(2)
    lattice gauge theory" [S Abstract]: passend.
  - **K8 nicht bestaetigt (Erwartung verletzt):** [46] "systematic study of pi+p->rho+p, pi-p->rho0n, pi-p->rho-p ...
    Structures of the isospin-zero and isospin-one contributions in the t-channel exchange are observed" [S Abstract].
    "pi0 p -> rho0 p" in Fig. 4 ist damit die Isospin-0-Kombination (omega-Austausch) [ES], kein Fehler.
  - **Neuer Befund (nicht erwartet), Z4:** [150] Brodsky/Tang/Thorn: "A fundamental prediction of perturbative QCD is
    that the Reggeon trajectories alpha_rho(t) and alpha_A2(t) ... must monotonically approach zero at large spacelike
    momentum transfers ... lim alpha_R(t) = 0" [S Abstract]. Der Artikel (S. 11) zitiert [149, 150] fuer
    "alpha_rho(t -> -inf) = -1". [150] traegt -1 nicht. Zwei Regime: Konstituenten-Austausch/Zaehlregeln (-1, so
    Blankenbecler u. a. [146], Erinnerung [L?]) gegen stoerungstheoretische Regge-Grenze (0). [149] pruefen (B4).
  - Stichprobe bestaetigt: [14] "square well" (passt), [162] "alpha(t)=0.93(24)+0.28(2) alpha'_R t ... similar to that
    of the pomeron", [144] rho-Trajektorie aus Triple-Regge bis -t 6-8 GeV^2, [106] FESR + "double counting ...
    interference model", [227] rho linear / sigma nichtlinear, [223] Saettigung ~ Deconfinement, [62] Regge-Pole an
    Ladungsaustausch, [1] Faktorisierung/Rapiditaetsluecke, [129] Oszillator-Green-Funktion.
  - [130] Susskind: Abstract "violin string or organ pipe"; das woertliche Zitat "chain of springs" steht nicht im
    Abstract -> sinngemaess getragen, Wortlaut ungeprueft.
  - [78] DL 1992: Abstract nur "Regge theory provides a very simple and economical description of all total cross
    sections" -> Zahlen 1.08/0.25 ungeprueft -> Volltext (B4).
  - Fuer das Programm wichtig: [157] Kruczenski u. a.: "rotating point-like massive particles connected by a flux
    string. The massive endpoints induce nonlinearities"; [161] Sonnenschein/Weissman: "non-linear Regge trajectories of
    a string with massive endpoints ... Glueballs" [S Abstract]. Das ist genau das PAAR-REGGE-1-Modell (Enden mit Masse).

### Buendel B4 (A10 Crossref DOI-Filter; A11 INSPIRE Buecher+[149]+[146]+BPST; A12-A14 arXiv-Volltexte; A15 Crossref Kapitel)
- Erwartung geschrieben 2026-10-05 04:52:31 CEST (date), vor A10-A15:
  - A10: Alle 10 DOIs ([9], [16], [24], [43], [44], [58], [100], [101], [179] x2) existieren bei Crossref (OSTI-DOI [58]
    vielleicht nicht, 40 %). [43]: Crossref zeigt S. Mandelstam, Ann. Phys. 19 (1962) 254 -> Initiale und Jahr falsch
    (80 %). [179]: 09420-1 ist das Original (647), 09594-8 das Erratum (915) -> PDF nennt die Erratum-DOI (60 %).
  - A11: INSPIRE kennt Donnachie u. a. "Pomeron physics and QCD" mit Jahr 2002 (70 %) und Gribov "Strong interactions
    of hadrons at high energies" mit Jahr 2009 (70 %); Newton/Nussenzveig/Sommerfeld teils nicht (50 %).
    [149] Collins/Kearney nennt -1 als Grenzwert (50 %). BPST 2007 existiert (95 %).
  - A12 [175]-Volltext: die Modellkurve stammt aus Mathieu u. a. 2018 = [181] (80 %).
  - A13 [63]-Volltext: enthaelt ein Chew-Frautschi-Bild der leichten Mesonen (55 %).
  - A14 DL 1992-Volltext: epsilon = 0,0808, alpha' = 0,25 GeV^-2 (85 %; alpha' ggf. aus DL 1984 uebernommen).
  - A15 Crossref Kapitel 10.1016/B978-0-443-26598-3.00042-0: existiert; Referenzliste hinterlegt (50 %), ggf. Zahl
    abweichend von 238.
  - Nachtrag Erwartung 2026-10-05 04:53:57 CEST (date), vor A16/A17 (Crossref-Buecher): Newton 2. Aufl. Springer 1982 existiert bei Crossref (80 %); Sommerfeld 'Partial Differential Equations in Physics', Academic Press 1949, bei Crossref (60 %).
- **Ausgang B4** (eingetragen 2026-10-05 04:54:55 CEST):
  - A10 Crossref (HTTP 200, 10/10 DOIs gefunden, auch OSTI [58]): [9], [16], [24], [44], [101] stimmen (101: Tippfehler
    "te"). **[43]: Crossref "S Mandelstam | An extension of the Regge formula | Annals of Physics 19 (1962) 254-261"** ->
    PDF hat "M. Mandelstam", "extention", "(1959)": drei kleine Fehler, Arbeit eindeutig. [58]: Crossref "MAXIMAL
    ANALYTICITY OF THE SECOND DEGREE", PDF "MAXIMUM": Titel leicht falsch. [100]: "Numerical Solution" (PDF
    "Solutions"): unerheblich. **[179]: 09594-8 ist laut Crossref das "Erratum to: ...", 09420-1 das Original** ->
    PDF nennt fuer EPJC 81, 647 die Erratum-DOI (Erwartung 60 %, eingetroffen).
  - A11 INSPIRE (HTTP 200): [53] Datensatz 604987, Autoren in derselben Reihenfolge wie im PDF (Donnachie S., Dosch,
    Nachtmann, Landshoff), Reihe Camb. Monogr. 19 (2002), Impressum Cambridge University Press 2004-12-02 -> Angabe
    "Vol. 19, CUP, 2004" deckt sich mit INSPIRE (Erwartung "2002" verletzt, mild). [55] Datensatz 2180771: Ausgaben 2009
    und Neuauflage 2022 (CUP), keine 2012 -> Jahr unbestaetigt, Tippfehler "emnergies". [6] Nussenzveig: Academic
    Press 1972, Math. Sci. Eng. 95 [S]. [5] Newton: INSPIRE-Datensatz ohne Angaben; A18 Crossref: Springer 1982,
    DOI 10.1007/978-3-642-88128-2 [S]. [10] Sommerfeld: A17 Crossref: Academic Press/Elsevier 1949, Buchkapitel
    (DOI-Praefix 10.1016/b978-0-12-654658-3) [S].
  - **[149] Collins/Kearney: "Reggeized version of the constituent interchange model (CIM), which predicts that
    alpha(t) -> -1 as t -> -inf"** [S Abstract]: traegt die -1. [146] BBGS: "trajectories are found to approach negative
    constants for large negative momentum transfer" [S Abstract]. -> Z4 bestaetigt: -1 gehoert zum CIM-Regime,
    [150] (pQCD: 0) ist an dieser Zahl falsch angehaengt.
  - BPST: Brower/Polchinski/Strassler/Tan, "The Pomeron and gauge/string duality", JHEP 12 (2007) 005,
    hep-th/0603115, 496 Zitierungen [S INSPIRE]; im Artikel nicht zitiert. Abstract: "a soft Pomeron Regge pole for
    the tensor glueball ... curved-space string-theory to describe simultaneously both the BFKL regime and the classic
    Regge regime".
  - Q-Baelle: Volkov/Woehnert, "Spinning Q balls", PRD 66 (2002) 085003, hep-th/0205157 [S INSPIRE, Abstract]:
    "first explicit example of spinning solitons in 3+1 dimensional Minkowski space" + "infinite discrete family of
    radial excitations". Drehimpuls-Masse-Beziehung steht nicht im Abstract.
  - **A12 GlueX [175] Volltext: "blue dashed curves show Regge theory predictions from JPAC ... [17]" (Z. 702),
    [17] = Mathieu u. a., Vector Meson Photoproduction with a Linearly Polarized Beam (Z. 1106) = [181] des Artikels.**
    -> K3 bestaetigt: Fig. 9 nennt [63] statt [181] [S].
  - A13 [63] Volltext: "FIG. 4. Chew-Frautschi plot for natural and unnatural par[ity exchanges]" (Z. 632) -> Fig. 5
    rechts korrekt zugeordnet (Erwartung 55 %, eingetroffen).
  - A14 DL 1992 Volltext: "epsilon = 0.0808, eta = 0.4525" (Z. 66-68); "Our s^epsilon is an effective power, with epsilon
    a little less than alpha(0) - 1" (Z. 102-103); "The line is alpha(t) = 0.44 + 0.93t" fuer rho, omega, f, a (Z. 230).
    alpha'_P = 0,25 steht nicht in [78] (Herkunft DL 1983/84 [L?]); [76-78] gemeinsam zitiert -> passt.
  - **A15 Crossref Kapitel (Elsevier 2026, S. 681-704): 238 Referenzen hinterlegt; [43] (1959, "extention"),
    [75] ("Pomeranchuck", "NUCELON", "corss"), [184] (nur arXiv), [55] (2012) stehen unveraendert in der
    Verlagsfassung** [S Crossref]. [179] dort mit Original-DOI, aber "doi-asserted-by: crossref" (von Crossref
    zugeordnet, nicht vom Verlag) -> keine Aussage ueber eine Verlagskorrektur.
  - A16 HTTP 400 (ungueltiges select-Feld, Bedienfehler), verbraucht; A18 Wiederholung HTTP 200.
  - Selbstzitate: 24 von 238 Referenzen mit Szczepaniak oder Winney als Autor (10 %), 12 davon JPAC-Kollaboration;
    Schwerpunkt Abschnitt 5. Jahrzehnte (zugeordnete, mit Jahr): 1960er 79, 1970er 46, 1950er 18, 2020er 32.

### Buendel B5 (W1: eine Websuche fuer [41] Froissart, La Jolla 1961, unveroeffentlicht)
- Erwartung geschrieben 2026-10-05 04:54:55 CEST (date), vor W1: Die Zitierform 'M. Froissart, Report to the La Jolla Conference on Theory of Weak and Strong Interactions (1961), unpublished' ist in Lehrbuechern/Uebersichten gebraeuchlich (80 %); ein Text des Berichts ist nicht auffindbar (85 %).
- Ausgang W1 2026-10-05 04:55:13 CEST: Websuche 1 von 3; Treffer-Zusammenfassung nennt 'M. Froissart ... report to the La Jolla Conference on the Theory of Weak and Strong Interactions, La Jolla, 1961 (unpublished)', Quelle u. a. arXiv hep-ph/0005257. Erwartung eingetroffen. Gegenprobe am Volltext (A19), Erwartung: Zitierform dort woertlich (75 %).
- **Ausgang A19** (Martin 2000, hep-ph/0005257, HTTP 200): Z. 58-61 "our meeting at the La Jolla Conference in 1961 ...
  Marcel Froissart gave a talk on his famous Froissart bound [2]", [2] = Phys. Rev. 123 (1961) 1053 (= [37] des
  Artikels). **Erwartung verletzt:** die Zitierform "Report ... (unpublished)" steht dort nicht; die Konferenz und
  Froissarts Vortrag sind belegt [S]. [41] bleibt "nicht pruefbar (unveroeffentlicht)"; der Inhalt (Fortsetzung in l)
  ist an keiner Primaerquelle geprueft.

## Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- G1: Ich habe die INSPIRE-Rohzeilen (raw_refs) als "PDF-Text" behandelt. Sind sie mit dem PDF identisch? -> lokal pruefen.
- G2: Ich habe v1 als einzige Fassung angenommen. Gibt es eine v2 auf arXiv mit Korrekturen? -> A20 arXiv-API.
- G3: Dass "DOI stimmt + Titel stimmt" auch "Jahr/Band stimmen" bedeutet: per jq abgeglichen (B2), erledigt.
- G4: Dass meine Einteilung klein/sachlich stabil ist: zwei Zaehlweisen (streng/milde) im Dossier.
- G5: Dass Abbildungsunterschriften nur bei Fig. 4, 5, 9 heikel sind: uebrige Bildquellen an Titel/Abstract gehalten
  (Fig. 1 [1], 3 [42], 6 [123], 7 [144], 8 [168], 10 [179], 11 [202], 13 [230], 14 [238]/[227]) -> passend nach Titel.
- G6: Dass die Q-Ball-Literatur keine Drehimpuls-Masse-Beziehung nennt (nur Abstract gelesen) -> A21 Volltext.
### Buendel B6 (A20 arXiv-API 2512.21805; A21 Volltext Volkov/Woehnert hep-th/0205157)
- Erwartung geschrieben 2026-10-05 04:55:56 CEST (date), vor A20/A21: A20: nur v1, journal_ref evtl. nachgetragen (60 %). A21: Volkov/Woehnert nennen J = n Q (Drehimpuls proportional zur Ladung, ganzzahliges n) (70 %); keine Regge-artige Beziehung J ~ M^2 (85 %).
- **Ausgang B6:** A20 (HTTP 200): nur v1 (25.12.2025), Kommentar "Commissioned article for the 'Encyclopedia of Particle
  Physics'. 23 pages, 14 figures", kein journal_ref auf arXiv (Erwartung "journal_ref nachgetragen" verletzt, mild;
  die Verlagsfassung kennt nur INSPIRE/Crossref). A21 (HTTP 200): Volkov/Woehnert Gl. (30) "J = ... = NQ" und Schluss
  Z. 911-912: "The angular momentum of these solutions is quantized, J = NQ, the energy increases (but not very rapidly)
  with the angular momentum" [S] (Erwartung eingetroffen). G1 erledigt: raw_refs = PDF-Text (5 Stichproben gleich).
- Projektbezug Q-Baelle (grep, gelesen hagedorn-1/KARTE.md Z. 5-14): RG-1 (RUNDE-06) "Die fuehrende Bahn drehender
  Q-Baelle folgt J ~ E^2 wie bei Strings. Das folgt aber schon aus der Ringform (Radius ~ m, Ladung ~ m)."
  HAGEDORN-1/-2 (Runde 37/38) pruefen, ob der Ringturm wie ein String zaehlt. -> Q-Ball-Frage ist im Projekt schon
  gestellt; der Artikel und seine Quellen tragen dazu nichts bei.

### Buendel B7 (A22: INSPIRE-Abstracts zur Relevanzbewertung: [140], [143], [167], [222], [80], [169], [97], [142], [195], [176], [64], [65])
- Erwartung geschrieben 2026-10-05 04:58:08 CEST (date), vor A22: [140] Veneziano 1976 nennt die topologische Entwicklung mit Pomeron als Zylinder bzw. geschlossenem String (55 %); [143] Rossi/Veneziano nennen die String-Verzweigung (junction) fuer Baryonen (80 %); [167] Y-foermige Flussroehre im Baryon (70 %); [222] saettigende Trajektorie (75 %); [64]/[65] Reggeon als Summe ueber den Turm (60 %).
- **Ausgang B7** (A22 HTTP 200, 12/12): [143] "For N colour = 3, the baryon resembles a Y shaped string" [S Abstract];
  [167] "T-shape paths are observed to relax towards a Y-shape topology as opposed to a Delta shape ... flux tube radius
  ... 0.38(3) fm ... The node connecting the flux tubes is 25% larger at 0.47(2) fm" [S Abstract]; [64] Van Hove: "if
  particles and resonances occur in infinite Regge recurrence series, the well-known contradiction between Regge pole and
  single particle exchange models ... can be avoided"; [65] Durand: s^alpha(0) "by summing ... an infinite set of
  single-particle exchanges"; [97] Childers: "infinitely rising trajectories ... consistent ... only if the trajectories
  behave, to within logarithmic factors, as sqrt(s) ... the imaginary part must increase more rapidly than the real part";
  [142] 't Hooft 2D: "interactions resemble those of the quantized dual string ... nearly straight 'Regge trajectory'";
  [140] Veneziano 1976: "necessity for quarkless (purely gluonic) bound states ... bare pomeron" (Zylinder/geschlossener
  String nicht im Abstract: Erwartung nur teilweise); [222] analytisches Trajektorienmodell (Schwelle + Asymptotik).
- Projekt-grep (Ausschluesse gesetzt): "2512.21805" nur Leitungsdateien (ARBEITSFELD-claude-primary, RUNDE-45, events,
  bus); "1812.01619" (HISH) 0 Literaturtreffer (nur Zahlenfolgen in breather-JSON); "Weissman"/"Sonnenschein" nur die
  Mesonen-Arbeit 2014 (regge-anschluss-20260912, gluon-paar-l "nur fuer Mesonen", paar-regge-1 [L]);
  "BPST" im Projekt = BPST-Instanton (formen-stabilitaet-20260909), NICHT Brower/Polchinski/Strassler/Tan ->
  Namensgleichheit, im Dossier ausschreiben; "hep-th/0603115" nur Scout-Cache. PAAR-REGGE-1 ist gerechnet
  (ERGEBNIS.md: "scheitert am festen Intercept"; Sonnenschein/Weissman-Randbedingung [L] ungeprueft).
- Erwartung geschrieben 2026-10-05 05:00:19 CEST (date), vor A23 (INSPIRE: Regge 1961 'General relativity without coordinates'): Nuovo Cim. 19 (1961) 558-571 (85 %); im Artikel nicht zitiert (grep: 0).
- Ausgang A23 (HTTP 200): Regge, "General relativity without coordinates", Nuovo Cim. 19 (1961) 558-571,
  DOI 10.1007/BF02733251, 1057 Zitierungen [S INSPIRE]; im Artikel 0 Treffer -> Regge-Kalkuel nicht zitiert (RH4).
- **Selbstanzeige (2026-10-05 05:02:54 CEST):** Im Listenbefehl kurz davor stand versehentlich `awk 'NR%1==0'` in einer Pipe (nach
  `head -0` wirkungslos, keine Ausgabe verwendet). Das verletzt "lokal kein awk". Ab hier nur jq/grep/sed/cut.

## Zwischenstand der Zaehlung (vor dem Dossier)
- 238 Referenzen. Existenz bestaetigt: 237 (224 INSPIRE, 8 Crossref-DOI, 5 Buecher INSPIRE/Crossref). Nicht pruefbar: 1
  ([41], unveroeffentlicht; Konferenz belegt). Nicht gefunden/erfunden: 0.
- Kleine bibliografische Fehler: 9 ([43], [55], [58], [75], [100], [101], [179], [184], [210]).
- OK mit Hinweis (Angabe und DOI zu verschiedenen Ausgaben/Impressum): [30], [52], [53], [59], [99] (+[5] Impressum).
- Kontext, streng sachlich (Quelle traegt die zitierte Aussage nicht): 4 Referenzstellen: [63] in Fig. 9, [69], [70]
  ("rising"), [150] (-1).
- Kontext, kleiner Fehler (Etikett/Teilpassung): 5: [172], [185], [186] ("CLAS12"), [166] ("lattice"), [180]
  ("pion photoproduction"). Dazu Reihenfolge "respectively" ([175]/[183]) vertauscht.
- Kontext fraglich, nicht pruefbar (kein Abstract): [68], [71] (gleicher Satz "rising"), [79] (anachronistisch).

## Abschluss (2026-10-05 05:14:20 CEST, date)
- DOSSIER.md geschrieben ab 05:06:44, Rueckwaertsdurchgang bis 2026-10-05 05:14:20 CEST.
- **Berichtigungen beim Gegenlesen (Zwischenstand oben bleibt stehen):**
  - ~~"Selbstzitate ... 12 davon JPAC"~~ -> **13** (Labels 1, 63, 170, 179, 181, 182, 187, 188, 193, 200, 201, 204, 230).
  - Abstracts gelesen fuer **44** Referenzen (nicht 47); Volltexte aus der Liste **3** ([63], [78], [175]), dazu 2
    ausserhalb (Martin 2000, Volkov/Woehnert).
  - Stichprobe neu getrennt: Verdachtsteil (K1, K2, K3, K6, K8, K9 = Z2, Z13, Z11, Z10, Z14, Z12): 4 von 6 bestaetigt;
    neutraler Teil (14): 1 Fehler (Z7, [150]). ~~"5 von 6" / "0 von 14"~~ war falsch zugeordnet.
  - Verlagsfassung: nur [43], [55], [75], [184] als unveraendert belegt; [58], [100], [101], [210] dort nicht pruefbar.
- Abrufe 23/45 (3 fehlgeschlagen), Websuche 1/3. Offene Rueckfragen: O1-O7 im Dossier Abschn. 8.2 (wandern mit).
