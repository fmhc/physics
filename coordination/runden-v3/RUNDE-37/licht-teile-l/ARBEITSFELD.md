# LICHT-TEILE-L: Arbeitsfeld (eine Datei, vor jedem Schritt neu lesen; Gestrichenes bleibt stehen)

- feldforscher fuer die Leitung claude-primary. **Start 2026-10-05 05:29:15 CEST (date).** Zeitbox 50 min, also bis
  etwa 06:19 CEST. Hoechstens 8 Abrufe (A1 bis A8). Keine Websuche.
- Grundlage: KARTE.md (bindend, LT1 bis LT5 unveraendert).
- Kennzeichen: [S Abschn./Gl.], [S Abstract], [L], [L?], [M], [ES], [H], [P].

## 0. Gelesen (lokal, kein Abruf), 05:29 bis 05:33

- KARTE.md ganz.
- PAAR-LICHT-L DOSSIER Abschn. 1, 1a, 3, 4, 5 [P]: Photon als Bilinear zweier Weyl-Automaten (Bisio/D'Ariano/Perinotti
  2016); omega_gamma(k) = 2 omega_W(k/2), also Zerfall in zwei masselose Bausteine genau an der Schwelle; Bose-
  Saettigung (8 n) als offene eigene Rechnung; vier statt zwei Moden; Laengsanteil theta ~ 2k.
- DOPPELSPALT-L ARBEITSFELD [P]: Grangier/Roger/Aspect 1986 dort nur als [L] (G2, "nicht geprueft, nur benannt"),
  kein Abruf, keine g2-Zahl. Also nichts lokal wiederzuverwenden; A3 ist kein Doppelabruf.
- KUBISCH-ANKER-L DOSSIER Z. 131, 155 [P]: Photonzerfall-Schranken (HAWC, c00 > -1,1e-28) nur superluminal;
  begrenzen Finns Netz nicht.
- LICHT-FINN-NETZ-1 ERGEBNIS Abschn. 1 [P]: Maxwell auf Finns Netz: a2 = -1/12 bis -1/9 (subluminal), isotrop
  langwellig, keine Doppelbrechung bis (k l)^4.
- Projekt-grep (05:32, mit Pflicht-Ausschluessen): "Grangier" nur in doppelspalt-l, RUNDE-45.md, paper-aeh1011 und
  Scout-Cache; "photon splitting" nur im Scout-Cache (Mikroskopie, "computational photon splitting", ohne Belang) und
  kubisch-anker-l; "photon structure function" nur Scout-Cache und RUNDE-45.md. Kein Projekttext zu SPDC als
  Photonspaltung, Kernfeldspaltung, Strukturfunktion. Bestaetigt die Projektsuche der Karte.

## 1. Zwei Regime (Feldregel 1), vorab

- **Regime A (Quant):** Das Photon ist das unteilbare Quant eines Feldes. "Teile" gibt es nur als Quantenschwankung
  (virtuelle geladene Paare), sichtbar erst bei hohem Impulsuebertrag (Strukturfunktion). Spalten heisst: ein Photon
  verschwindet, zwei oder drei ganze, kleinere Photonen entstehen (nichtlineares Medium, Feld).
- **Regime B (Ansammlung):** Das Photon ist ein gebundener Haufen echter Teile, die mitlaufen. Dann muessten Teile bei
  genuegend Energie oder an einem Strahlteiler abtrennbar sein, und Energie koennte in Bruchteilen abgegeben werden.
- **[H] Vermuteter dritter Fall A' (Sammelschwingung):** Das Photon ist das Quant einer Sammelschwingung vieler Teile
  eines Mediums (Phonon-Analogie, Eis-Licht). Die Teile laufen nicht mit, die Erregung schon. Dann ist "aus vielen Teilen"
  und "unteilbar" kein Widerspruch. Moderator zwischen B und A': ob die Teile mit dem Photon mitlaufen.
- **Unterscheidungspunkte (vorab, Feldregel 2):**
  - Strahlteiler mit genau einem Photon: B mit trennbaren Teilen gibt Doppelklicks (g2(0) > 0, binomial), A und A'
    geben g2(0) = 0.
  - Energieabgabe: B erlaubt Bruchteile von h nu, A und A' nur ganze Vielfache (Photopeak, TES-Spektren).
  - Hohe Energie: B mit Bindungsskala Lambda gibt angeregte Photonen bzw. Formfaktor ab Q ~ Lambda; A gibt nur die
    bekannte QED/QCD-Strukturfunktion.
  - A gegen A': Der Unterschied liegt bei Wellenlaengen nahe der Teilgroesse (Gitterdispersion, Brillouin-Zone). Bei
    Laborenergien nicht unterscheidbar [ES].

## 2. Abrufe (Erwartung vor dem Abruf, Ausgang danach)

### A1 (Erwartung 05:33:11 CEST) arXiv-API ti:"photon splitting", neueste zuerst, bis 200 Treffer
- Erwartung: Darin Akhmadaliev u. a. (Budker-Institut, ROKK-1M an VEPP-4M), PRL 2002, "Experimental observation of
  high-energy photon splitting in atomic fields": markierte Photonen ~0,1 bis 0,5 GeV, Spaltung im Feld schwerer Kerne
  (BGO-Target [L?]) beobachtet, Rate stimmt mit der Theorie exakt in Z alpha (Coulomb-Korrekturen, Lee/Milstein)
  ueberein. Magnetar-Arbeiten (Baring/Harding; Hu/Baring/Wadiasingh): Spaltung nach Adler nur vorhergesagt bzw.
  indirekt (Spektralabbruch), nicht direkt gemessen. 24 Monate: Laser-Vorschlaege (Spaltung im starken Laserfeld),
  keine Labor-Beobachtung im Laserfeld. Kein Treffer mit "Spaltung in Nicht-Photonen".
- Bedeutung: LT2 traefe ein; Magnetar = nicht gemessen.

### A2 (Erwartung 05:33:11 CEST) arXiv-API abs:"three-photon" AND abs:"down-conversion", neueste zuerst, bis 100
- Erwartung: Chang u. a. 2020 (PRX, supraleitender Resonator, Mikrowellen, direkte Drei-Photonen-SPDC beobachtet);
  Huebel u. a. 2010 (Nature, Kaskade zweier SPDC, optische Tripletts, sehr kleine Raten); Faservorschlaege
  (Cavanna u. a.). 24 Monate: weitere Mikrowellen-Arbeiten, optisch direkt noch nicht beobachtet [L?].
- Bedeutung: LT1-Teil "Spaltung in drei beobachtet" traefe ein (Mikrowelle direkt, optisch kaskadiert).

### A3 (Erwartung 05:33:11 CEST) arXiv-API "background-free" AND "single photons", nach Relevanz, bis 50
- Erwartung: Schweickert u. a. 2018 (APL, Quantenpunkt, Zwei-Photonen-Anregung) g2(0) = (7,5 +- 1,6) x 1e-5 [L?].
  Weitere Quantenpunkt-Arbeiten mit g2(0) ~ 1e-4. 24 Monate: kein deutlich besserer Rekord als ~1e-5 [L?].
- Bedeutung: LT3 traefe ein (<= 1e-3 klar unterschritten).

### Ausgang A1 bis A3 (05:34:58 CEST, Eintrag 05:36:59 CEST)
- Alle drei Antworten der arXiv-API: 14 Byte, Text "Rate exceeded." (Kopien in quellen/A1-..., A2-..., A3-...).
  DOPPELSPALT-L hatte um 05:09:47 dieselbe Antwort (dort quellen/A1-arxiv-droplet-slit-...xml, 14 Byte) [P].
- **Zaehlung (konservativ, Kontrollen nicht nach Befund lockern):** A1 bis A3 zaehlen als verbrauchte Abrufe, obwohl sie
  nichts brachten. Rest: 5 (A4 bis A8). Die arXiv-API meide ich ab jetzt; Ausweg INSPIRE-API und arxiv.org/search
  (per curl als Kopie, wie DOPPELSPALT-L A4/A5 arxiv.org genutzt hat).
- Folge fuer die Planung: Themen buendeln. INSPIRE fuer alles Hochenergie-Nahe in einer Anfrage (Spaltung im Kern- und
  Magnetfeld, Strukturfunktion, Kompositheit), arxiv.org/search fuer Quantenoptik (Drei-Photonen-SPDC, g2-Rekord) und
  Spin-Eis.

## 3. Zusatzbefund der Leitung (eingegangen waehrend 05:36, eingetragen 05:36:59 CEST)

- Quelle: gegenlesen-r45/GEGENLESEN.md Abschn. 4.2, V-1 (gelesen: nur 4.2 und Teil-A-Tabelle). In Abschn. 4 und 5 des
  Dossiers einbeziehen. Karte, Erwartungen, Budget unveraendert.
- Aussage (woertlich): "Licht aus Paaren zweier Fermionen kann im Breitband hoechstens n = 1/8 je Polarisation tragen
  (unpolarisiert; 1/4 bei einer Linearpolarisation); gemessene Rayleigh-Jeans-Spektren (n >> 1) passen nicht dazu."
- Vorbehalt (woertlich, muss mitstehen): "[M], einmal frisch gegengelesen; gilt fuer den Bau aus zwei Vernichtern mit
  Verschmierung nach Bisio Gl. (20), auch mit gefuelltem See. Offen: Dichtebau c^+ c mit Dirac-See (Jordan,
  Bosonisierung) und Verduennung ueber N innere Zustaende (8 n/N). Literaturpruefung unvollstaendig."
- Verboten: Gegenlesen Abschn. 4.1 (A-1 bis A-7), also keine "10^90"-Entwarnung, keine Bose-Test-Schranke, kein
  "widerlegt". Abschn. 4.1 habe ich nicht gelesen.
- Auftrag daraus: Welche Bedingung legt das einem Teile-Bild auf (bosonische Teile, viele innere Zustaende, Dichtebau)?
  Zahl fuer n >> 1 mit Quelle oder [L].
- Vorueberlegung [M, Planck-Formel n = 1/(e^x - 1), x = h nu/(k T)]: CMB T = 2,725 K [L] gibt k T/h = 56,8 GHz; bei
  1 GHz n = 56, bei 3 GHz n = 18, bei 60 GHz n = 0,53 [M]. Raumtemperatur 300 K bei 1 GHz: n ~ 6250 [M].
  Rubens/Kurlbaum 1900 (51 um, ~1500 K [L?]): x ~ 0,19, n ~ 5 [M]. FIRAS misst 60 bis 600 GHz, also gerade NICHT
  die Seite n >> 1 [L]; dafuer ARCADE 2 (3 bis 90 GHz) [L] und Bodenmessungen um 1 GHz [L?].

### A4 (Erwartung 05:36:59 CEST) INSPIRE-API, eine Anfrage: Titel "photon splitting" ODER "photon structure function"
### ODER "composite photon(s)" ODER "photon compositeness" ODER "size of the photon"; neueste zuerst, bis 1000
- Erwartung:
  - Spaltung: Adler 1971 (Ann. Phys.), Akhmadaliev u. a. 2002 PRL (Kernfeld, beobachtet, Theorie mit
    Coulomb-Korrekturen stimmt), Lee/Milstein-Theorie; Magnetare (Baring/Harding 1997 bis 2001; Hu/Baring u. a. 2019
    bis 2023) nur Vorhersage bzw. indirekt. 24 Monate: Laserfeld-Vorschlaege, keine Beobachtung.
  - Strukturfunktion: LEP-Messungen (OPAL, L3, DELPHI, ALEPH) und PETRA/TRISTAN, Uebersicht Nisius 2000 (Phys. Rep.):
    F2^gamma gemessen etwa Q^2 ~ 0,1 bis ~800 GeV^2 [L?], steigt mit ln Q^2 (punktfoermiger Anteil) - also "Teile"
    nur als Quantenschwankung. Auch die QED-Strukturfunktion (Leptonpaare) gemessen.
  - Kompositheit: fast nur Theorie (Neutrinotheorie, emergente Photonen, Bjorken), KEINE eigene experimentelle
    Kompositheits-Schranke fuer das Photon. Indirekt nur LEP e+e- -> gamma gamma (QED-Abschneideskala Lambda ~ 0,4 TeV
    [L?]). Damit traefe LT4 ("> ~1 TeV, < ~1e-19 m") nur abgeschwaecht ein (Skala eher 0,4 TeV, ~5e-19 m) [L?].

### Ausgang A4 (Abruf 05:37:31 CEST, ausgewertet bis 05:39:00 CEST)
- Kopie: quellen/A4-inspire-splitting-structure-composite-20261005-053731.json (625 kB, 281 Treffer = alle).
- **Spaltung im Kernfeld (LT2):** Akhmadaliev u. a., PRL 89 (2002) 061802, hep-ex/0111084 [S Abstract]: markierter
  Photonenstrahl ROKK-1M an VEPP-4M, 120 bis 450 MeV, 1,6e9 Photonen auf BGO, "About 400 candidates", "consistent with
  the cross section calculated exactly in an atomic field. The predictions obtained in the Born approximation
  significantly differ". -> bestaetigt (eine Zeile).
  - **Verstoss V-A (klein):** Schon Jarlskog u. a., PRD 8 (1973) 3813 (DESY, 1 bis 7 GeV, Cu/Ag/Au/U): "The
    photon-splitting process has been experimentally detected ... Estimates of the cross section are given" [S Abstract].
    Silagadze 2020 (arXiv:2009.03039) nennt dagegen das Budker-Team 1995 "for the first time" [S Abstract]. Korrektur
    der Erwartung: "erstmals" ist strittig; die erste Messung mit Querschnitt gegen exakte Theorie ist Budker
    (1995 vorlaeufig, 2002 endgueltig).
- **Spaltung in drei an einem freien Elektron:** Loetstedt/Jentschura, PRL 108 (2012) 233201, arXiv:1205.0317: "a
  photon splits into three after the collision with a free electron (triple Compton effect)"; "our calculation is in
  agreement with the only available measurement of the differential cross section" [S Abstract].
  - **Verstoss V-B:** Ich hatte Drei-Photonen-Spaltung nur ueber SPDC erwartet. Es gibt einen zweiten, gemessenen Weg
    (Gammaquanten an ruhenden Elektronen), Messung selbst nicht gelesen, Autor/Jahr unbekannt.
- **Magnetfeld/Magnetar:** wie erwartet nicht direkt gemessen. Hu u. a. MNRAS 486 (2019) 3327: "no emission yet
  detected above around 1 MeV"; Spaltung und Paarbildung "expected to be active ... possibly accounting for the
  paucity of gamma-rays" [S Abstract]. Indirekt und modellabhaengig: PSR B1509-58, Abbruch bei E_c = 81 +- 20 MeV,
  "interpreted in the framework of polar cap models as a signature of the exotic photon splitting process" (Pilia u. a.
  2010, arXiv:1009.1636) [S Abstract]. Adler 1971 (811 Zitate) und Bialynicka-Birula 1970 als Theorie [S Titel].
  -> bestaetigt.
- **24 Monate (Spaltung):** In INSPIRE-Titeln seit 2023 keine Arbeit zur Spaltung im Laserfeld oder im Magnetar;
  letzter Titel Ngo 2023 (Mikrosaeulen, offenbar Strahlteilung) [S Titel]. Urteil: Laserfeld- und Magnetar-Spaltung
  "nach Recherchestand nicht direkt beobachtet" (Feldregel 7: kein "ausgeschlossen").
- **Strukturfunktion (LT5):** 196 Titel. Erste Messung PLUTO (PETRA), PLB 107 (1981) 168: 1 < Q^2 < 15 GeV^2, "The
  pointlike component of the photon is found to be dominant" [S Abstract]. JADE 1984: Q^2 10 bis 220 GeV^2 [S Titel].
  TPC/2gamma 1986: 0,2 < Q^2 < 7 GeV^2 [S Titel]. OPAL PLB 411 (1997) 387: Q^2 1,86 bis 135, Steigung
  (1/alpha) dF2/dlnQ^2 = 0,10 +0,05 -0,03 [S Abstract]. L3 PLB 447 (1999) 147: "linear growth with ln Q^2" [S Abstract].
  Nisius 2009 (arXiv:0907.2782): QED- und hadronische Strukturfunktion gemessen [S Abstract]. -> bestaetigt.
  - **Verstoss V-C (Deutung, wichtig fuer Finn):** Berger 2014 (arXiv:1404.3551): "the increase of the structure
    function with x ... and its rise with log Q**2, both characteristics beeing dramatically different from hadronic
    structure functions"; Datenstrom "ended naturally around 2005" [S Abstract]. Ich hatte "Teile" als hadronartig
    erwartet. Die Daten sagen: Die Teile des Photons sind keine festen, gebundenen Bausteine (dann waere F2 bei grossem
    x klein und skalierte), sondern entstehen beim Hinsehen durch punktfoermige Aufspaltung gamma -> q qbar; je feiner
    die Aufloesung, desto mehr. Das ist ein Unterscheidungspunkt Regime A gegen B [ES].
  - 24 Monate: Jang u. a., J. Korean Phys. Soc. 88 (2026) 1325, arXiv:2512.00889: Lambda_QCD aus F2^gamma, mit VMD
    fuer den nichtperturbativen Teil [S Abstract]. Keine neue Messung.
- **Kompositheit (LT4):** In INSPIRE nur Theorie und Streit, keine experimentelle Kompositheits-Schranke im Titel.
  Perkins, J. Mod. Phys. 5 (2014) 2089 (arXiv:1503.00661): "composite photon theory" (Neutrino plus Antineutrino),
  "impossible to rule out", Pryce-Einwaende "invalid or irrelevant" [S Abstract]; Perkins 2025 (J. Mod. Phys. 16, 1409):
  Antiphoton als dunkle Materie [S Abstract]; Low, MPLA 31 (2016) 1675002: Gegenargumente aus kosmologischer
  Strahlungsdichte, Verteilung der dunklen Materie und C-Symmetrie [S Abstract]. Etim 1972 "size of the photon"
  (Skalierungsbild) [S Abstract].
  - **Verstoss V-D (vorlaeufig):** Ich hatte wenigstens indirekte Kompositheitsgrenzen erwartet. Unter diesen
    Titeln: keine. Ob LEP e+e- -> gamma gamma eine Photon-Skala liefert, ist offen -> A8 (Reserve) dafuer.

### A5, A6, A7 (Erwartungen 2026-10-05 05:39:52 CEST) arxiv.org/search per curl (Kopie), je eine Anfrage
- **A5** "three-photon" "down-conversion", alle Felder, neueste zuerst, bis 100, mit Abstracts.
  - Erwartung: Chang u. a. 2020 (PRX, supraleitende parametrische Kavitaet, Mikrowellen): erste direkte
    Drei-Photonen-SPDC. Huebel u. a. 2010 (Nature): optische Tripletts nur ueber Kaskade zweier SPDC-Stufen, wenige
    Ereignisse je Stunde [L?]. Faser- bzw. chi(3)-Vorschlaege. 24 Monate: weitere Mikrowellen- bzw. Theoriearbeiten;
    direkte optische Drei-Photonen-SPDC noch nicht beobachtet (60 %).
  - Bedeutung: LT1 ("Spaltung in drei beobachtet") traefe ein, aber nur im Mikrowellenbereich direkt.
- **A6** "background-free" "single photons", nach Relevanz, bis 50.
  - Erwartung: Schweickert u. a. 2018 (APL, Quantenpunkt, Zwei-Photonen-Anregung): g2(0) = (7,5 +- 1,6) x 1e-5. Andere
    Quellen ~1e-4. 24 Monate: kein Wert deutlich unter 1e-5 (60 %).
  - Bedeutung: LT3 traefe ein (g2(0) << 1, Rekord <= 1e-3 weit unterschritten).
- **A7** "emergent photon" "spin ice", neueste zuerst, bis 50.
  - Erwartung: Quanten-Spin-Eis-Kandidaten Ce2Zr2O7, Ce2Sn2O7, Ce2Hf2O7, Pr2Hf2O7; Neutronen-Hinweise auf
    Spinonen und emergente Eichfelder, "evidence"-Arbeiten 2024 bis 2026, aber kein eindeutiger Nachweis des emergenten
    Photons (70 %). Emergentes Lichttempo winzig gegen c (Groessenordnung 1e2 bis 1e3 m/s [L?]).
  - Bedeutung: Finns "Licht als Sammelschwingung vieler Teile" hat ein Laborgegenstueck, ob es gemessen ist, ist offen.

### Ausgang A5 (05:39:52 CEST) und Neuplanung (Eintrag 2026-10-05 05:41:31 CEST)
- A5: arxiv.org/search per curl -> 14 Byte "Rate exceeded." (Kopie quellen/A5-...html). Zaehlt als Abruf 5. Rest: 3.
  DOPPELSPALT-L kam um 05:11 per WebFetch an die Suchseite [P]. Also: arxiv.org nur noch per WebFetch (Ausgabe als
  Zusammenfassung, Kopie des WebFetch-Texts nach quellen/), INSPIRE per curl.
- **Lokal statt Abruf (kein Abruf):** Pace/Morampudi/Moessner/Laumann, arXiv:2009.04499 (dyon-statistik-l/quellen,
  Text) [S-lokal]:
  - Z. 349-351: Kandidaten Tb2Ti2O7, Yb2Ti2O7, Pr2Sn2O7, Pr2Zr2O7; a ~ 10 Angstroem; g ~ 1 ueV.
  - Z. 355-357: "the emergent photon travels a hundred million times slower than the speed of light and the emergent
    fine structure constant is ten times larger".
  - Z. 360-363: "The experimental effort ... largely been focused on finding evidence for the existence of a linearly
    dispersing transverse photon and fractionalized gapped spinons".
  - Folge: A7 (Spin-Eis) entfaellt als Abruf. Stand nur 2020/2021; neuere Lage nicht abgerufen (Selbstanzeige).
- **Neue Reihenfolge der letzten 3 Abrufe:** A6 g2-Rekord (LT3), A7 Drei-Photonen-SPDC (LT1), A8 INSPIRE LEP
  e+e- -> gamma gamma (LT4).

### A6 (Erwartung siehe oben, unveraendert) WebFetch arxiv.org/search "background-free" "single photons", Relevanz, 50
### A7 (Erwartung = alte A5, unveraendert) WebFetch arxiv.org/search Titel "three-photon" "down-conversion", neueste, 50
### A8 (Erwartung) INSPIRE: Titel (QED und LEP) oder "QED cut-off", meistzitiert, bis 60
- Erwartung: OPAL, L3, DELPHI, ALEPH "Tests of QED ... e+e- -> gamma gamma(gamma)": Abschneideparameter
  Lambda+- ~ 0,3 bis 0,4 TeV (95 % CL), dazu Schranken fuer angeregte Elektronen und Kontaktwechselwirkungen
  (Lambda ~ 0,8 bis 1 TeV) [L?]. Das testet den e-e-gamma-Vertex, nicht gezielt eine Photongroesse.
- Bedeutung: LT4 ("> ~1 TeV, < ~1e-19 m") traefe nur abgeschwaecht ein: direkte Photon-Groesse nicht begrenzt;
  indirekt ~0,4 TeV (~5e-19 m).

### Ausgang A6, A7, A8 (Eintrag 2026-10-05 05:47:04 CEST)
- **A6** (WebFetch ~05:41:40, Kopie quellen/A6-...txt, 17 Treffer): Schweickert u. a., arXiv:1712.06937, "On-demand
  generation of background-free single photons from a solid-state source": "g^(2)(0)=(7.5\pm1.6)\times10^{-5}"
  [S Abstract via WebFetch]. Wei u. a. 2014 (arXiv:1405.1991): "two-photon emission probability of 0.3%". Kein
  kleinerer Wert in den 17 Treffern (bis Jan 2026). -> LT3 bestaetigt (eine Zeile). Selbstanzeige: enge Suche, ein
  neuerer Rekord unter anderem Stichwort ist nicht ausgeschlossen.
- **A7** (WebFetch ~05:41:40, Kopie quellen/A7-...txt, 6 Treffer im Titel):
  - Jarvis-Frain u. a., Okt. 2025, arXiv:2510.05405: "Observation of Genuine Tripartite Non-Gaussian Entanglement from a
    Superconducting Three-Photon Spontaneous Parametric Down-Conversion Source"; "superconducting parametric cavity";
    "maximum violation of the bound by 23 standard deviations" [S Abstract via WebFetch]. -> direkte Drei-Photonen-
    Spaltung im Mikrowellenbereich, 24-Monats-Fenster, bestaetigt.
  - Optisch: Borshchevskaya u. a. 2015 (arXiv:1508.03291) nur Theorie fuer Volumenkristalle; Borrero Landazabal u. a.
    Sep. 2026 (arXiv:2609.03542) "Heralded one-, two- and three-photon states" in PPKTP-Wellenleiter, laut
    Zusammenfassung ohne Angabe direkt/kaskadiert [S Titel]. Urteil: direkte optische Drei-Photonen-SPDC "nach
    Recherchestand nicht beobachtet".
  - Kleiner Verstoss: Chang u. a. 2020 (meine [L?]-Erstbeobachtung) erscheint in der Titelsuche nicht. Ungeklaert
    (anderer Titelwortlaut oder Suchindex). Beleg fuer die Mikrowellen-Spaltung bleibt Jarvis-Frain 2025 [S Titel].
- **A8** (INSPIRE 05:42:57, Kopie quellen/A8-...json, 142 Treffer, 80 geladen):
  - hep-ph/0111302 (2001, Autoren nicht im Abruf), "Putting non point-like behavior of fundamental particles to test":
    L3, e+e- -> gamma gamma bei 91 und 209 GeV, 1991 bis 2001, globaler Fit: "contact interaction energy scale
    parameter Lambda > 1.6 TeV, which restricts the characteristic QED size of the interaction region to
    R_e < 1.2 x 10^-17 cm" [S Abstract]. Also 1,2e-19 m.
  - L3, PLB 353 (1995) 136: Lambda > 602 GeV, m_e* > 146 GeV, Lambda+ > 149 GeV, Lambda- > 143 GeV (Z-Pol) [S Abstract].
  - DELPHI, EPJC 37 (2004) 405: 161 bis 208 GeV, 656,4 pb^-1, "confirming the validity of QED at the highest energies
    ever attained in electron-positron collisions" [S Abstract].
  - **Verstoss V-E (gegen meine A8-Erwartung, nicht gegen LT4):** Ich erwartete ~0,4 TeV (QED-Abschneideparameter).
    Die schaerfste Zahl ist der Kontaktparameter 1,6 TeV, ausdruecklich als Groesse gedeutet (1,2e-19 m). LT4s Zahl
    stimmt damit. Aber: Es ist die Groesse des Wechselwirkungsbereichs e-e-gamma (die Quelle schreibt R_e), keine
    eigene Photonschranke. Korrigierte Erwartung: Teile des Photons waeren unterhalb ~1e-19 m gebunden, sonst saehe
    man sie in e+e- -> gamma gamma; eine nur dem Photon zugeordnete Schranke habe ich nicht gefunden.
- **Budget: 8 von 8 Abrufen verbraucht** (A1, A2, A3, A5 leer durch Ratenlimit; A4, A6, A7, A8 mit Inhalt).
  Weitere Fragen nur noch lokal oder als [L].

## 4. Gegensweep (Feldregel 4), 05:47: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1 [GEPRUEFT, Schreibtisch M]: "Der Photoeffekt zeigt, dass Licht Energie nur als Ganzes abgibt."**
  - Rechnung: klassisches Feld E0 cos(omega t), Atom quantisiert, Stoerung H' = e E0 x cos(omega t). Erste Ordnung:
    c_f(t) ~ (e^{i(omega_fi - omega) t} - 1)/(omega_fi - omega), also Uebergang nur bei E_f = E_i + hbar omega;
    Rate Gamma = (2 pi/hbar) |<f|e E0 x/2|i>|^2 rho(E_i + hbar omega).
  - Folge: E_kin = hbar omega - W, Rate proportional zur Intensitaet, keine Einschaltverzoegerung. Alles ohne
    Lichtquanten; das hbar kommt vom Elektron. So zeigten es Lamb und Scully 1969 [L].
  - **Befund: Erwartung verletzt.** Der Photoeffekt allein unterscheidet A nicht von einem klassischen, teilbaren Feld.
    Er prueft also eine "Teilansammlung" nicht. Trennscharf sind (i) g2(0) < 1 mit Einzelphotonen (A6) und (ii)
    Energieerhaltung in jedem einzelnen Ereignis (Bothe/Geiger und Compton/Simon 1925 gegen Bohr/Kramers/Slater [L]).
- **G2 [nur benannt]: "g2(0) ~ 0 heisst: keine Teile."** Ein Detektor klickt erst ab einer Schwelle. Teile mit einem
  winzigen Energieanteil eps fallen bei g2 nicht auf. Begrenzen koennen das nur energieaufloesende Messungen: Mossbauer-
  Resonanz (eps < Gamma/E ~ 3e-13 fuer Fe-57 [L, M]), Rainville u. a. 2005 (Gammaenergie aus Wellenlaenge gegen
  Delta m c^2, 4e-7 [P neue-theorie/gitter-checkliste.json, L]), TES-Spektren [L]. -> Kartenvorschlag.
- **G3 [nur benannt]: "Teile, die unterwegs abgegeben werden, saehe man nicht."** Doch: Energieverlust auf der Strecke
  waere "muedes Licht" (Rotverschiebung ohne Zeitdehnung). Gemessen ist die Zeitdehnung (1+z) an Supernova-Lichtkurven
  [L]. Nicht abgerufen.
- **G4 [nur benannt]: "Die Strukturfunktion misst Teile des Photons."** Sie misst ein fast reelles Zielphoton mit einer
  stark virtuellen Sonde. Die "Teile" haengen von der Aufloesung Q^2 ab. Das ist mit V-C vereinbar und spricht fuer
  Quantenschwankung statt Bausteine [ES].
- **G5 [nur benannt]: "Der g2-Rekord ist 7,5e-5."** A6 war eine enge Stichwortsuche. Ein neuerer Rekord unter anderem
  Wortlaut ist moeglich.

## 5. Abschluss (2026-10-05 05:51:23 CEST)
- DOSSIER.md geschrieben ab 05:48:23 CEST (date), danach eine Ergaenzung in Abschn. 1 Punkt 4 ("reine Energie" als
  Eigenschaft, [ES]) und diese Zeile. Kein weiterer Abruf (8 von 8 verbraucht).
- Offene Rueckfragen, die mitwandern: (1) Stand Spin-Eis-Photon 2024 bis 2026 nicht abgerufen; (2) Zwei-Photonen-SPDC
  und Grangier 1986 nur [L]; (3) eigene Photon-Kompositheitsschranke nicht gefunden; (4) V-1-Auswege (Runde 46,
  Warteschlange Punkt 5); (5) Kartenvorschlag TEILE-SCHRANKE-L (Luecke G2).
