# DOPPLER-LAUFZEIT-L: Arbeitsfeld (feldforscher fuer claude-primary)

- Start 2026-10-05 08:44:24 CEST (date). Zeitbox 60 min (bis ~09:44), hoechstens 15 Netzabrufe.
- Bindend: KARTE.md (DL0 bis DL3 unveraendert). Gelesen 08:44 bis 08:50: KARTE.md ganz,
  teile-schranke-l/DOSSIER.md ganz, art-grenzen-20260921/UNGEPRUEFT.md Abschn. 1.1 bis 1.4.
- Feld-Regeln: eine Datei (diese), Erwartung mit date vor jedem Abruf, Gestrichenes bleibt stehen (~~...~~).
- Kennzeichen: [E] [M] [S] [L] [H] [P]; [ES] eigener Schluss. [M] = Rechnung von Hand, nicht gegengelesen.

## 0. Uebernommen aus Projektdateien [P]

- TEILE-SCHRANKE-L (DOSSIER Abschn. 2, 4, 7): kappa = -d ln nu/dL; schaerfste Wegschranke DES-Zeitdehnung,
  kappa < ~1,5e-28 /m (nur fuer Verlust OHNE Zeitstreckung); Laborstrecken rundweg-geregelt, blind; H0/c ~ 7,6e-27 /m.
- UNGEPRUEFT 1.2: Pioneer erledigt (Turyshev u. a. 2012, "no anomalous acceleration remains"), a_P = (8,74 +- 1,33)e-10 m/s^2.
- UNGEPRUEFT 1.1: Voyager 1 ohne Ranging (nur Doppler). 1.3: Cassini-Ephemeride Q2 (Hees 2014, Park 2026).

## 1. Schreibtisch vor jedem Abruf (08:51 bis 08:58)

### 1.1 Groessen [M, vorab ableitbar], H0 = 70 km/s/Mpc [L]
- H0 = 7e4 / 3,0857e22 = 2,27e-18 /s; H0/c = 7,57e-27 /m.
- Zweiwege-Doppler: y = Delta f/f = 2 kappa D (Hin- und Rueckweg je kappa D). Entspricht scheinbarer Radialgeschwindigkeit
  v_app = y c/2 = kappa c D. Bei kappa = H0/c: v_app = H0 D.
  - 1 AE (1,496e11 m): 0,34 um/s, y = 2,3e-15.
  - Jupiter/Juno (~5,2 AE, 7,8e11 m): 1,8 um/s, y = 1,2e-14.
  - Saturn/Cassini (1,3e12 m): 2,95 um/s, y = 2,0e-14.
  - New Horizons (~60 AE, ~9e12 m; Entfernung [L]): ~20 um/s, y ~ 1,4e-13.
- Konvention: "1e-14 relativ" heisst im Zweiwege-Doppler v = y c/2 = 1,5 um/s, nicht 3 um/s. DL1 schreibt "~1e-14 (~3 um/s)";
  das passt nur zur Einweg-Umrechnung v = y c. Kein Urteilsgrund, aber notiert (Faktor 2).
- Laufzeit-Diskrepanz: Delta r = kappa c D T. Saturn, 1 Jahr: 93 m; 1 AE, 1 Jahr: 10,7 m; NH, 1 Jahr: ~650 m.
- Innerhalb eines Passes (T_p = 8 h = 2,88e4 s), ohne jedes Bahnmodell: Saturn 8,5 cm; 1 AE 1,0 cm; NH ~0,6 m.

### 1.2 Drei Regime fuer "Frequenz aendert sich unterwegs" (Feldregel 1) [M, ES]
- **R1 muedes Licht im engen Sinn:** Traegerfrequenz sinkt um kappa je Meter, die Laufzeit der Modulation
  (Entfernungscode, Gruppenlaufzeit) bleibt D/c. Dann gilt die Identitaet "Doppler = Ableitung der Laufzeit" nicht mehr.
  Bei fester Strecke und fester Laufzeit muessen unterwegs Schwingungen verschwinden (Phase nicht erhalten): Rate
  2 kappa D f [M, vorab ableitbar]. Beobachtbar: Zweiwege-Doppler-Versatz y = 2 kappa D, Laufzeit unveraendert,
  also DRVID-Drift ("Differenced Range Versus Integrated Doppler") kappa c D, nicht dispersiv.
- **R2 zeitdehnender Verlust:** Alle Frequenzen samt Modulation werden gestaucht. Dann kommt auch der Entfernungscode
  gestreckt an, die gemessene Laufzeit waechst mit der Zeit, Doppler und Entfernung bleiben UNTEREINANDER konsistent.
  Nur die Bahndynamik (Kepler, Planeten-Ranging ueber Jahre) sieht es. Bei fester Strecke ist R2 von einer Ausdehnung
  des Lichtwegs nicht zu unterscheiden. Moderator R1 gegen R2 = derselbe wie G7 in TEILE-SCHRANKE-L (Zeitstreckung).
- **R3 zeitliche Drift:** y(t) = 2 a_t t, unabhaengig von D (Uhrbeschleunigung, Pioneer: a_t = a_P/c = 2,92e-18 /s).
- Pioneer gegen R1 [M]: Pioneer hatte kein Ranging (Doppler allein). Bei auswaerts fliegender Sonde ist D = D0 + v t:
  Der R1-Versatz kappa c D0 verschwindet in der Startgeschwindigkeit, uebrig bleibt eine Drift kappa c v, also eine
  scheinbare Beschleunigung nach aussen. Bei Hubble-Rate und v = 12 km/s: 2,7e-14 m/s^2, 3e4-mal kleiner als a_P und mit
  umgekehrtem Vorzeichen (Pioneer: Blauverschiebungsdrift, sonnenwaerts [L]). Pioneer begrenzt kappa nur ueber
  kappa < a_lim/(c v); bei a_lim ~ 1e-10 m/s^2 (angenommen, nicht gelesen) kappa < ~3e-23 /m ~ 4e3 H0/c.

### 1.3 Unterscheidungspunkte (Feldregel 2), vorab
- R1 gegen Null: nicht-dispersive DRVID-Steigung proportional zu D. Groesste Empfindlichkeit bei grossem D, vielen
  Paessen und langen Boegen mit Ranging (NH, Cassini, Juno).
- R1 gegen Plasma: Plasma-DRVID ~ 1/f^2 (dispersiv), wechselt mit dem Sonnenwind; R1 nicht dispersiv, fest im Vorzeichen.
  Zweiband (X/Ka) trennt.
- R1 gegen Troposphaere: wirkt auf Phase und Gruppe gleich, keine DRVID [L].
- R1 gegen echte Bahnfehler: echte Bewegung wirkt auf Doppler und Laufzeit gleich und faellt in der DRVID heraus [M].
- R2 gegen echte Bahnaufweitung: R2 waechst mit D (Erde-Ziel), eine echte Aufweitung mit a (heliozentrisch).

### 1.4 Gegensweep, vorab benannt
- G1 (Auftrag): Schluckt die Bahnanpassung einen Doppler-Versatz? Erwartung: kurze Boegen (Juno-Perijove, Cassini-
  Vorbeifluege) ja, ueber den Anfangszustand; lange gemeinsame Doppler+Range-Fits mit gebundenen Range-Biases nein.
  Ephemeriden (DE, INPOP) passen Range-Normalpunkte (Laufzeit) an: fuer R1 blind, fuer R2 empfindlich.
- G2 (Auftrag): Konsistenzpruefungen gibt es als DRVID (Plasmakalibrierung, DSN 1970er); eine kappa-Schranke daraus
  erwarte ich nicht.
- G3 (selbstverstaendlich): Zweiwege-Doppler gilt als absolut, ohne Bias-Parameter. Drehende Sonden (Pioneer, Juno,
  NH im Spin-Modus) haben aber einen Spin-Versatz; wird dort ein Doppler-Bias geschaetzt, ist der Fit blind fuer R1.
- G4 (selbstverstaendlich): "Range = Laufzeit, unberuehrt" gilt nur in R1. Rate-Aiding mit dem Traeger koppelt R1 in
  die Range ein: v_app x Integrationszeit ~ 3e-6 m/s x 600 s ~ 2 mm, vernachlaessigbar [M].
- G5 (selbstverstaendlich): kappa haengt nicht von nu ab (8 bis 32 GHz gegen optisch). Fuer achromatisches z noetig,
  fuer Finns Teile-Bild nicht gesichert.
- G6 (selbstverstaendlich): Das DSN-Beobachtungsmodell rechnet Doppler als differenzierte Laufzeit (Moyer [L]). Eine
  Doppler-Laufzeit-Abweichung ist dort gar kein Parameter.

### 1.5 Abrufplan (hoechstens 15)
1. WebSearch: direkte Schranke (muedes Licht, Frequenzverlust, Doppler gegen Ranging, Sonnensystem).
2. WebSearch: DRVID nicht-dispersiv / "range-Doppler consistency".
3. WebSearch, 24 Monate (Regel 7): neue Tests 2024 bis 2026.
4. INSPIRE-Sammelabruf: Turyshev 2012, Anderson 2002, Kopeikin 2012, Carrera/Giulini 2010, Bertotti 2003.
5. Bertotti 2003 (Nature) fuer DL1; Ersatz Asmar 2005 bzw. Armstrong 2006.
6. DE440/INPOP: welche Datentypen (Range, Doppler)?
7. Genova 2018 (MESSENGER, Doppler und Range gemeinsam): Bias-Parameter?
8. Iess 2021 BepiColombo MORE: Empfindlichkeit, Range gegen Doppler.
9. bis 15. Reserve fuer Erwartungsverstoesse.

## 2. Abrufprotokoll mit Erwartung (Erwartung VOR dem Abruf, Zeit per date)

### A1 bis A3: Erwartung notiert 2026-10-05 08:52:44 CEST (date), vor dem Abruf
- **A1** WebSearch "tired light spacecraft Doppler ranging solar system test frequency loss proportional distance".
  Erwartung: keine Arbeit mit expliziter kappa-Schranke aus Sondendaten (~20 % fuer einen direkten Treffer). Treffer
  eher: Pioneer-Literatur (a_P ~ c H0), Kopeikin 2012 (Ephemeriden im expandierenden Universum), Randseiten zu muedem Licht.
- **A2** WebSearch "DRVID differenced range versus integrated Doppler nondispersive range Doppler consistency".
  Erwartung: JPL-TDA/IPN-Berichte der 1970er zur Plasmakalibrierung, eventuell Navigationsarbeiten zur
  Range-Doppler-Konsistenz (Transponderlaufzeit). Keine kappa-Schranke.
- **A3** WebSearch, 24 Monate: "2025 2026 spacecraft tracking test local cosmic expansion Hubble solar system Doppler range".
  Erwartung: Arbeiten zur lokalen Expansion ueber Ephemeriden oder LLR (Regime R2/Dynamik), keine zu R1 mit Sonden.

### A1 bis A3: Ausgang (eingetragen 2026-10-05 08:53:42 CEST, date). Werkzeugtexte = nur Wegweiser
- **A1 bestaetigt:** keine Sondenschranke fuer muedes Licht. Treffer: Lehrtexte, Randseiten, eine NTRS-Notiz 1971
  (19710002916, Inhalt unbekannt), gr-qc/0308010 und 1305.1950 (Inhalt unbekannt). Eine Zeile, weiter.
- **A2 bestaetigt:** DRVID gibt es seit 1961 als DSN-Verfahren (Plasma: Phase vor, Gruppe nach). Werkzeugtext: "DR minus
  ID" misst die Elektronensaeule "independently of spacecraft motion"; "DR plus ID" (DRPID) ist plasmafrei. Fuer R1 heisst
  das [ES]: muedes Licht wuerde in der DRVID als stetige, nicht-dispersive "Elektronenzunahme" erscheinen. Keine
  kappa-Schranke. Wegweiser: ipnpr 42-106/106A, NTRS 19950021345, 19770014187, 19740008873, 19920020125.
- **A3 VERSTOSS (voller Zyklus):** Erwartet nur Ephemeriden/LLR zur lokalen Expansion. Gefunden ein eigener
  Literaturstrang genau zur Hubble-Signatur im Sonden-Doppler:
  - gr-qc/0605078 "On Doppler tracking in cosmological spacetimes" (Inhalt erst zu lesen);
  - 1011.1944 "The Measurement of the Hubble Constant H_0 in the Solar System". Werkzeugtext (nicht Quelle!): der kosmische
    Rotverschiebungsterm bleibe im Rueckweg-Doppler "coherently conserved", wenn die Rundlaufzeit eine Schwelle der
    Frequenznormal-Stabilitaet uebersteigt; nicht modelliert erzeuge er Doppler-Reste wie eine "anomalous force", in langen
    Boegen gross;
  - 1207.3873 Kopeikin 2012; 1407.6667; 1306.0374; 1311.4912; 2109.03280 (2021); **2602.09141 (2026, im 24-Monats-Fenster,
    Titel unbekannt)**.
  - Korrigierte Erwartung: Die Frage "sieht der Sonden-Doppler eine Frequenzverschiebung ~ H0 x Lichtlaufzeit?" ist in
    der Kosmologie-Literatur gestellt, als Frage nach R2/R3 (Ausdehnung), nicht nach R1. Zu klaeren: Wer sagt Effekt
    erster Ordnung in H0 voraus, wer nur H0^2? Steht irgendwo eine gemessene Schranke?

### A4: Erwartung notiert 2026-10-05 08:53:54 CEST (date), vor dem Abruf
- export.arxiv.org/api/query, id_list = gr-qc/0605078, 1011.1944, 1207.3873, 2109.03280, 2602.09141, 1204.2507,
  gr-qc/0104064 (Abstracts, Datei nach quellen/).
- Erwartung je Arbeit:
  - gr-qc/0605078 (vermutlich Carrera/Giulini 2006): Effekt der Expansion auf Doppler-Tracking vernachlaessigbar
    (hoehere Ordnung in H0), keine Pioneer-Erklaerung.
  - 1011.1944: behauptet einen Effekt erster Ordnung (~H0 x Rundlaufzeit), messbar; Minderheitsposition; keine Messung.
  - 1207.3873 Kopeikin 2012: Effekt erster Ordnung auf die Lichtausbreitung in konformen Koordinaten, Bezug Pioneer.
  - 2109.03280: lokale Experimente nur O(H0^2).
  - 2602.09141: unbekannt; 50 % dass es eine Pioneer-/Expansions-Arbeit ohne Messschranke ist.
  - 1204.2507 Turyshev 2012: thermischer Rueckstoss, keine Zahl fuer die Restschranke im Abstract.
  - gr-qc/0104064 Anderson 2002: a_P = (8,74 +- 1,33)e-8 cm/s^2; Uhr-Lesart vermutlich nicht im Abstract.

### A4: Ausgang (eingetragen 2026-10-05 08:55:14 CEST, date). Quelle: quellen/A4-arxiv-batch-20261005-085410.xml [S Abstract]
- 7 von 7 Eintraegen. Je Arbeit:
  - **1011.1944, Allen Joel Anderson 2010 (ohne Journal-Angabe, nur v1): VERSTOSS.** Erwartet "keine Messung". Abstract:
    bestimmt "with available published data" H0 = (2,59 +- 0,05)e-18 /s = 79,8 +- 1,7 km/s/Mpc aus Sonden-Doppler. Der
    kosmische Rotverschiebungsterm bleibe im Zweiwege-Doppler erhalten; in einer Bahn "determined by line of sight Doppler
    alone" erzeuge er Reste wie eine "anomalous force". Welche Daten, welches Vorzeichen, R1 oder R3: im Abstract nicht
    gesagt. -> voller Zyklus (A5, Volltext).
    - Vorab-Rechnung dazu [M]: 2,59e-18 /s x c = 7,8e-10 m/s^2. Das liegt bei a_P = 8,74e-10 m/s^2 (Anderson u. a. 2002).
      Verdacht: Die "Messung" ist die Pioneer-Anomalie, gelesen als H0. Dann ist es Regime R3 (Drift ~ t), nicht R1
      (Versatz ~ D). Und Pioneer ist thermisch erklaert (Turyshev 2012). Zu pruefen in A5.
  - **1207.3873 Kopeikin 2012 (PRD 86, 064004): teilweise wie erwartet.** Die Bewegungsgleichungen von Teilchen und Licht
    haben verschiedene Zeitargumente, Differenz proportional zu H; den Lichtlaufzeit-Gleichungen der Navigationszentren
    "for fitting range and Doppler-tracking" fehlten Terme ~H. Das ist eine Behauptung ueber die LAUFZEIT (R2-artig),
    nicht ueber einen reinen Frequenzverlust. Pioneer steht nicht im Abstract. Die Atomzeit sei unberuehrt.
  - **gr-qc/0605078 Carrera/Giulini 2006 (CQG 23, 7483): leichter Verstoss.** Erwartet "hoehere Ordnung in H0". Gefunden:
    Die kosmologische Korrektur an der per Zweiwege-Doppler bestimmten Beschleunigung ist "linear in the Hubble
    constant", aber "negligible in typical applications within the Solar System". Groesse nicht im Abstract.
    Vermutung [ES]: Term ~ H0 v. Das waere dieselbe Groessenordnung wie die R1-Drift bei Hubble-Rate (H0 v, 1.2). -> A6.
  - **2109.03280 Spengler/Belenchia/Raetzel/Braun (CQG 39, 055005, 2022):** McVittie und Kottler; Frequenzverschiebung
    eines Resonators und Lichtsignale zwischen lokalen Beobachtern; "clarify some of the statements made in the literature".
    Keine Zahl im Abstract.
  - **2602.09141 McQuinn u. a. 2026 (NIAC-Bericht): wie erwartet nicht einschlaegig.** FRB-Laufzeiten mit Sonden im
    aeusseren Sonnensystem (Cosmic Positioning System). Fuer Regel 7: kein neuer Sondentest von R1 im Fenster.
  - **1204.2507 Turyshev u. a. 2012: bestaetigt.** "no anomalous acceleration remains"; keine Restschranke im Abstract.
  - **gr-qc/0104064 Anderson u. a. 2002: bestaetigt.** a_P = (8,74 +- 1,33)e-8 cm/s^2; Abstract nennt "radio Doppler and
    ranging data from distant spacecraft" (fuer die Vorarbeiten; Pioneer selbst: Doppler, siehe Negativliste-Pruefung).

### A5 und A6: Erwartung notiert 2026-10-05 08:55:32 CEST (date), vor dem Abruf
- **A5** arxiv.org/pdf/1011.1944 (A. J. Anderson 2010, Volltext). Erwartung: Der H0-Wert stammt aus der Pioneer-Anomalie
  (80 %), also Regime R3 (Drift), umgedeutet als "Cosmic Redshift"; keine Entfernungsdaten, kein Vergleich Doppler
  gegen Laufzeit; kein Gutachterverfahren erkennbar.
- **A6** arxiv.org/pdf/gr-qc/0605078 (Carrera/Giulini 2006, Volltext). Erwartung: Formel fuer die per Zweiwege-Doppler
  bestimmte Beschleunigung mit kosmologischem Term ~ H0 v (oder H0 mal Radialgeschwindigkeit), Groesse ~1e-14 m/s^2 oder
  kleiner, "negligible" gegen a_P; kein Versatz ~ H0 D (kein R1-Term) bei gebundenen Beobachtern.

### A5 und A6: Ausgang (eingetragen 2026-10-05 08:57:27 CEST, date)
- **A5 bestaetigt** (quellen/A5-arxiv-1011.1944-20261005-085543.pdf und .txt; 25 Seiten; arXiv-Hauptkategorie
  physics.space-ph; Einzelautor Allen Joel Anderson, NICHT John D. Anderson):
  - Equ. 2 (S. 2): "- Delta f/f = t x H0", t = Rundlaufzeit. Das ist genau R1 mit kappa = H0/c [S, Lesart ES].
  - Daten: Pioneer 10, 1987 bis 1999, "approximately 40 to 90 AU", Werte aus Anderson u. a. 2002 (sein "paper (4)"),
    darunter a_P = (7,77 +- 0,16)e-8 cm/s^2 (zitiert von S. 34 dort). 7,77e-10/c = 2,59e-18 /s [M] = sein H0. Also: die
    "Messung" ist a_P/c.
  - Der Schritt von R1 (Versatz ~ Rundlaufzeit) zur Pioneer-Drift wird im "Gedanken"-Experiment behauptet, nicht
    gerechnet: Der Term sei "not dependent on the distance to the spacecraft" und erscheine als "constant positive frequency
    shift (that is reverse sign)". Keine Entfernungsdaten (Pioneer hatte nur Doppler; er schreibt selbst "navigation was
    performed using only line of sight Doppler").
  - Brauchbar fuer G1 (aus einer nicht begutachteten Quelle): Er schreibt, das Bahnprogramm koenne den Effekt ueber
    Strahlungsdruck und andere freie Parameter "easily absorb".
- **A6 bestaetigt** (quellen/A6-arxiv-gr-qc-0605078-20261005-085545.pdf und .txt; CQG 23, 7483):
  - Gl. (27)/(36): Im Zweiwege-Doppler steht ein kosmologischer Zusatzterm "Hcβ k" = H v. "the sometimes alleged Hc
    acceleration term [7] is actually suppressed by a factor β" (S. 7/8). Er zeigt "in outer direction and hence opposite
    to the Pioneer anomalous acceleration". Gegen die speziell-relativistische Korrektur ~1e-7, "negligible".
  - Deckt sich mit meiner Rechnung 1.2 fuer R1 bei Hubble-Rate: scheinbare Zusatzbeschleunigung H0 v nach aussen,
    2,7e-14 m/s^2 bei 12 km/s [M]. Damit ist die Rechnung von A. J. Anderson (H0 c = a_P) schon 2006, vier Jahre vorher,
    in begutachteter Form entkraeftet [S + ES].
  - Neu fuer die Deutung [ES]: Im Zweiwege-Doppler hat "Expansion bis in den Lichtweg" (FLRW-Beobachter) dieselbe
    Drift-Form wie R1 bei Hubble-Rate. Doppler allein trennt beides nicht; die Laufzeit trennt (R1: keine Laufzeitaenderung).

### A7: Erwartung notiert 2026-10-05 08:57:44 CEST (date), vor dem Abruf
- api.openalex.org/works?filter=doi:10.1038/nature01997|10.1029/2004RS003101|10.12942/lrr-2006-1 (Bertotti/Iess/Tortora
  2003; Asmar u. a. 2005 Radio Science; Armstrong 2006 Living Review). Fuer DL1.
- Erwartung: Bertotti-Abstract ohne Rauschzahl (nur gamma = 1 + (2,1 +- 2,3)e-5). Asmar 2005 nennt fuer Cassini
  (Ka-Band, Troposphaerenkalibrierung) eine Allan-Abweichung um 3e-15 bis 1e-14 bei 1000 s (Gedaechtnis, unsicher).
  Armstrong-Abstract allgemein ohne Zahl. Moegliche Luecke: OpenAlex fuehrt fuer Nature-Artikel oft kein Abstract.

### A7: Ausgang (quellen/A7-openalex-doppler-noise-20261005-085759.json; Abstracts per jq aus dem Wortindex gelesen)
- **Teilweise Verstoss (fuer DL1):**
  - Bertotti/Iess/Tortora 2003: OpenAlex ohne Abstract (Luecke wie vorhergesagt). Die Rauschzahl ist an Bertotti NICHT gelesen.
  - Asmar u. a. 2005, Radio Sci. (doi 10.1029/2004RS003101) [S Abstract]: "most sensitive current experiments achieve
    fractional frequency fluctuation noise of about 3 x 10^-15 at 1000-s integration time", "better than 1 micron per
    second". Also ~3-mal besser als DL1 (~1e-14). Cassini wird im Abstract NICHT namentlich genannt.
  - Armstrong 2006 (LRR 9, 1) [S Abstract]: Konvention 2 Delta v/c = Delta nu/nu0 (Zweiwege). Bestaetigt meine
    Konventionsnotiz 1.1: 1e-14 entspricht 1,5 um/s, nicht 3 um/s. Keine Zahl im Abstract.
- Korrigierte Erwartung/Einordnung [ES]: Fuer einen KONSTANTEN Versatz ist die 1000-s-Allan-Abweichung die falsche
  Guete. Massgeblich ist die Stabilitaet des Frequenznormals ueber die Rundlaufzeit (Saturn ~2,6 h) und systematische
  Versaetze zwischen Paessen. Bei Hubble-Rate ist das Signal y = 2e-14 (Saturn) bzw. 2,3e-15 (1 AE); die Kurzzeit-
  Rauschzahl 3e-15 bei 1000 s liegt darunter bzw. gleichauf [M].

### A8: Erwartung notiert 2026-10-05 08:59:09 CEST (date), vor dem Abruf
- descanso.jpl.nasa.gov/monograph/series1/Descanso1_all.pdf (Thornton/Border 2000, "Radiometric Tracking Techniques for
  Deep-Space Navigation"; Adresse aus Gedaechtnis, kann leer sein). Fuer G1, G2, G6.
- Erwartung: DRVID als Plasmakalibrierung (Gruppenverzoegerung gegen Phasenvorlauf); Range mit Stationslaufzeit-
  Kalibrierung, systematische Fehler ~m; in der Bahnbestimmung werden Range-Biases je Pass oder Bogen geschaetzt,
  Zweiwege-Doppler ohne Bias-Parameter; Doppler wird als Phasen- bzw. Laufzeitdifferenz modelliert. Kein Wort zu
  muedem Licht. Wenn Range-Biases je Pass frei sind, kann Range einen Doppler-Versatz nur ueber die Steigung im Pass
  herausdruecken (Saturn bei Hubble-Rate: 8,5 cm in 8 h, unter dem Range-Rauschen) [M].

### A8: Ausgang (quellen/A8-descanso1-thornton-border-20261005-085919.pdf und .txt; 94 Seiten)
- **Weitgehend bestaetigt, ein Zusatz:**
  - Tab. 3-3 (S. 33/35 der Monographie, X-Band, Stand 2000) [S]: Doppler-Zufallsfehler 0,03 mm/s bei 60 s; Range 60 cm;
    "Instrument bias (range)" 2 m; "Instrument stability @ 8 h" 1e-14; Stationsuhr Stabilitaet bei 1000 s 1e-15,
    Rate 5e-14. Plasma bei 180 Grad SEP: Drift ueber 8 h 15 cm (X).
  - Text S. 21 [S]: "several days of continuous, biased range data with an accuracy of 1 m have the same angular
    information as a comparable track of Doppler with an accuracy of 0.1 mm/s"; Range und Doppler gemeinsam koennen
    "poorly modeled spacecraft accelerations" aufdecken.
  - Abschn. 3.6 (S. 35/36) [S]: Unmodellierte Kraefte werden vom Schaetzer in schwach bestimmte Parameter gedrueckt
    (Beispiel: 5 m Range-Stoerung -> 1000 km Querlage); "solving for the orbit parameters from Doppler and range data
    alone can be highly risky".
  - DRVID nur als Literaturhinweis (MacDoran 1970, SPS 37-62), kein eigener Text.
- Folgerung fuer G1 [ES auf S]: Ein unmodellierter R1-Versatz wuerde nicht zwingend in den Resten stehen bleiben. Der
  Schaetzer verschiebt ihn in schwach bestimmte Groessen (Querlage, Strahlungsdruck, Anfangsgeschwindigkeit). Range
  "zwingt" ihn nur heraus, wenn der Bias der Range gebunden ist und die Boegen lang sind.
- Rechnung [M]: Bei Hubble-Rate ist y(Saturn) = 2e-14 nur das Doppelte der "Instrument stability @ 8 h" (1e-14),
  y(1 AE) = 2,3e-15 ein Viertel davon. Je Pass ist R1 bei Hubble-Rate also hoechstens knapp sichtbar; nur die Mittelung
  ueber viele Paesse oder ein Laufzeitvergleich ueber Monate hilft.

### A9: Erwartung notiert 2026-10-05 09:00:21 CEST (date), vor dem Abruf
- ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf (Park/Folkner/Williams/Boggs 2021, AJ 161, 105; Adresse aus Gedaechtnis).
- Erwartung: Datentabelle mit Range (Radar, Sonden-Range-Normalpunkte Mars, MESSENGER, Venus Express, Juno, Cassini),
  VLBA/VLBI-Winkeln, optischen Daten; Doppler nicht als Ephemeriden-Datentyp; kein Parameter fuer Doppler-gegen-Range.
  Folge: DE ist fuer R1 blind, fuer R2 empfindlich (Laufzeiten ueber Jahrzehnte).

### A9: Ausgang (quellen/A9-jpl-de440-20261005-090029.pdf und .txt; AJ 161:105, 15 S.)
- **Bestaetigt, mit zwei Zusaetzen** [S, Abschn. 5, S. 10/11]:
  - "For spacecraft in orbit about the planet, the Doppler measurements are typically used to estimate the position of
    the spacecraft with respect to the planet's center of mass and then range and VLBI measurements are used to estimate
    the orbit of the planet."
  - Doppler wird als Aenderung der Laufzeit gelesen ("Doppler measurements change in range much more accurately");
    beide Messungen beruhen auf der Phase (Traeger bzw. Modulation). Das bestaetigt G6 an einer Primaerquelle.
  - Zusatz 1: Die Stationskalibrierung je Pass ist allen Range-Punkten eines Passes gemeinsam, deshalb "only one range
    point per tracking pass was used". Die Steigung innerhalb eines Passes (DRVID-Information) geht nicht in DE440 ein.
  - Zusatz 2, Reste: Cassini-Range 2004 bis 2018, 147 Punkte, rms ~3 m; Juno-Range 2016 bis 2020, 15 Punkte, rms ~13 m;
    MESSENGER ~0,7 m; MGS/ODY/MRO ~0,7 m; MEX ~2 m; VEX ~8 m; LLR ~1,3 cm (neu).
- Folgerung [ES]: Die Ephemeride ist fuer R1 (Frequenzversatz bei unveraenderter Laufzeit) praktisch blind, weil die
  Planetenbahn aus Laufzeiten kommt. R1 wirkt nur auf die planetenbezogene Sondenbahn. Fuer R2 (Laufzeit waechst mit)
  ist sie empfindlich: Bei Hubble-Rate waeren das bei Saturn ~93 m je Jahr, ~1,3 km ueber 14 Jahre [M], gegen 3 m rms.
  Wie viel davon die Bahnelemente schlucken, ist ohne Fit nicht ableitbar. Also keine Zahl, nur Groessenordnung.

### A10, A11, A12: Erwartung notiert 2026-10-05 09:01:46 CEST (date), vor dem Abruf (drei Suchen parallel)
- **A10** (Regel 7, gezielt) WebSearch "tired light photon energy loss constraint solar system spacecraft radio tracking
  2025 2026". Erwartung: keine neue Sondenschranke; hoechstens Kosmologie-Arbeiten zu muedem Licht (CCC+TL u. ae.).
- **A11** WebSearch "PDS radio science raw data ODF TNF Cassini Juno two-way Doppler range archive". Erwartung: PDS-
  Atmospheres-Seiten (Cassini, Juno) bzw. PDS-Geosciences (MESSENGER) mit ODF/TNF, die Doppler UND Range enthalten.
- **A12** (G3) WebSearch "Juno spin Doppler bias radio science gravity spacecraft rotation correction". Erwartung:
  Der Spin-Beitrag wird aus der bekannten Drehrate korrigiert, kein freier Doppler-Bias (55 %); sonst freier Bias je Bogen.

### A10 bis A12: Ausgang (Werkzeugtexte = nur Wegweiser)
- **A10 leichter VERSTOSS:** Keine neue Sondenschranke im 24-Monats-Fenster (wie erwartet). Unerwartet: Ein weiterer
  Text (Werkzeugtext, Quelle vermutlich astro-ph/0701132 oder 0707.3351) deutet die Pioneer-Frequenzverschiebung unter
  "tiring photon hypothesis" als "direct manifestation of the Hubble law inside the solar system". Also gibt es
  mindestens zwei Stimmen, die Pioneer als NACHWEIS von muedem Licht im Sonnensystem lesen (A. J. Anderson 2010 und
  diese). Korrigierte Erwartung: Der Sonnensystem-Fall ist in der Randliteratur als Nachweis behauptet, nicht als
  Schranke gefuehrt. Pruefen an der Quelle -> A13.
- **A11 bestaetigt:** ODF ("range, Doppler and frequency ramps", ODE-Hilfeseite MESSENGER RSS EDR) im PDS fuer MESSENGER
  (pds-geosciences.wustl.edu/MESSENGER/mess-v_h-rss-1-edr-rawdata-v1/, SIS-PDF), Mars Odyssey (ody-m-rss-1-raw-v1),
  Dawn (sbnarchive.psi.edu), Juno (atmos.nmsu.edu/data_and_services/atmospheres_data/JUNO/gravity.html, PDS4). Nicht
  an der Quelle geprueft -> A14 fuer Juno.
- **A12 nicht entschieden:** Werkzeugtext: Juno dreht mit 2 U/min; Spin-Signatur in Open-Loop-Daten wird kompensiert.
  Ob ein freier Doppler-Bias geschaetzt wird, sagt kein Treffer. Wegweiser arXiv:1411.1613 (Juno-Radio-Science-Modelle),
  1302.6920 (Inhalt unbekannt). -> Abstracts in A13 mitnehmen.

### A13: Erwartung notiert (Zeit siehe date-Ausgabe im Abrufbefehl; vor dem Abruf geschrieben)
- export.arxiv.org/api/query, id_list = astro-ph/0701132, 0707.3351, 1411.1613, 1302.6920.
- Erwartung: astro-ph/0701132 ist die Quelle des A10-Satzes (60 %): muedes Licht erklaert Pioneer, keine
  Entfernungsdaten. 0707.3351: Uebersicht zu muedem Licht, Pioneer vielleicht erwaehnt. 1411.1613: Juno-Modelle, kein
  Wort zu freiem Doppler-Bias im Abstract (70 %). 1302.6920: unbekannt.
- **A13 LEER:** export.arxiv.org antwortete nicht (curl Zeitueberschreitung nach 60 s, 0 Byte, keine Datei). Zaehlt mit.
  Die Quelle des A10-Satzes bleibt ungeprueft (Negativliste). G3 bleibt nicht entschieden.

### A14: Erwartung notiert vor dem Abruf (Zeit: date-Ausgabe oben in diesem Befehl)
- atmos.nmsu.edu/data_and_services/atmospheres_data/JUNO/gravity.html (Juno-Schwerefeld-Archiv, PDS4).
- Erwartung: Liste je Perijove mit TNF, ODF und RSR (Open-Loop); ODF enthalten Doppler und, wo gemessen, Range (70 %,
  dass "range" auf der Seite steht). Frei herunterladbar ohne Anmeldung.
- **A14 LEER:** atmos.nmsu.edu setzte die Verbindung zurueck (curl rc 56, keine Datei). Zaehlt mit. Juno-Datensatz
  bleibt ungeprueft.

### Zwischenrechnung vor A15 (Schreibtisch) [M]: Reicht ein oeffentlicher Datensatz fuer die DRVID-Probe je Pass?
- Steigungsfehler je Pass: sigma ~ sigma_r sqrt(12) / (T sqrt(N)). X-Band: sigma_r 0,6 m (Thornton/Border Tab. 3-3),
  ein Punkt je 10 min, T = 8 h, N = 48: sigma ~ 1e-5 m/s je Pass. Plasma bei X allein: Drift ~15 cm in 8 h (Tab. 3-3,
  180 Grad SEP) -> ~5e-6 m/s je Pass, Vorzeichen wechselnd.
- Signal bei Hubble-Rate: 0,34 um/s (1 AE), 1,8 um/s (Juno), 2,95 um/s (Saturn).
- Folge: Bei 1 bis 1,5 AE (Mars, MESSENGER) braucht man einige tausend Paesse, um die Hubble-Rate knapp zu erreichen;
  bei Saturn reichen ~100 Paesse fuer 3 sigma. Unter die Hubble-Rate (0,1 H0/c) kommt die Probe je Pass nur mit
  Cassini/Juno und ~1000 Paessen oder mit Ka-Band-Ranging im cm-Bereich (BepiColombo MORE; Zugang nicht geprueft).
- Staerker ist der Weg ueber die Bahn (Planetenumlaufer): Die Planetenbahn kommt aus Laufzeiten (DE440, A9), die mittlere
  Sichtlinien-Geschwindigkeit eines gebundenen Umlaufers ist durch die Planetenbahn festgelegt. R1 gaebe einen mittleren
  Doppler-Rest +kappa c D, der mit der Erde-Planet-Entfernung ueber die synodische Periode schwankt. Ob Bogen-Parameter
  (Strahlungsdruck, Bogen-Anfangszustand, Planetengeschwindigkeit) ihn schlucken, ist nicht ableitbar.

### A15: Erwartung notiert vor dem Abruf (Zeit: date-Ausgabe oben in diesem Befehl). Letzter Abruf.
- pds-geosciences.wustl.edu/ody/ody-m-rss-1-raw-v1/odrs_0275/catalog/dataset.cat (Mars Odyssey Radio-Science-Rohdaten).
- Erwartung: Die Katalogdatei nennt ODF/TNF mit Zweiwege-Doppler UND Range sowie Rampen, Zeitraum ab 2001, frei
  zugaenglich. Ohne Range waere der Datensatz fuer die DRVID-Probe wertlos (30 %).

### A15: Ausgang (quellen/A15-pds-ody-rss-raw-dataset-20261005-090524.cat; 852 Zeilen)
- **Bestaetigt, mit Bonus** [S, Katalogtext]: DATA_SET_ID "ODY-M-RSS-1-RAW-V1.0", 2001 Mars Odyssey Radio Science,
  START_TIME 2002-01-01, STOP_TIME 2019-01-31. ATDF-Felder: "Range", "High- or low-rate Doppler", "Differential Range vs
  Integrated Doppler (DRVID)", "Allan deviation". ODF-Felder: "Two-way Doppler (Hertz)", "Two-way total count phase
  (cycles)", Range (PRA/SRA in range units, RE in ns). ODF-Produktion endete April 2017; danach TNF. "Typical users ...
  analyze range and Doppler measurements ... to reconstruct the spacecraft trajectory."
- Bonus: Die DRVID ist im Archiv ein eigenes Feld (ATDF, Fruehphase) und aus ODF/TNF (Range plus Zaehlphase) direkt
  bildbar. Damit ist die modellfreie R1-Probe je Pass mit oeffentlichen Daten moeglich, ohne Bahnbestimmung.

### Projekt-grep 09:07:39 (Pflicht-Ausschluesse, ohne diesen Ordner)
- "DRVID|differenced range|integrated doppler": keine Treffer im Projekt.
- "Carrera|Kopeikin|1011.1944|Allen Joel": Kopeikin nur zur Gravitationsgeschwindigkeit (strang-anker-l, Goldhaber/Nieto);
  Giulini-Treffer betreffen Spin-Themen (Dateinamen). Der Doppler-H-Strang ist im Projekt neu.

## 3. Gegensweep am Ende der Recherche (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- **GS1: "Unter der Hubble-Rate" ist die richtige Messlatte.** NICHT selbstverstaendlich. Fuer ein UNIVERSELLES kappa ohne
  Zeitstreckung (R1) liegt die DES-Schranke aus TEILE-SCHRANKE-L schon bei ~0,02 H0/c (~1,5e-28 /m) [P]. Ein
  Sonnensystem-Test bei ~H0/c bringt dafuer nichts Neues. Er zaehlt nur fuer (a) ein kappa, das vom Medium bzw. der
  Umgebung abhaengt (Dichte, Feld, kurze Strecken), (b) ein kappa, das von der Frequenz abhaengt (Radio gegen optisch),
  (c) R2, falls man die Ephemeriden als Laufzeittest liest. Geprueft am Schreibtisch [M, P]; Quelle: TEILE-SCHRANKE-L
  Abschn. 2 Punkt 3.
  - Zahl dazu [M, Werte L]: mittlere Baryonendichte heute ~2,7e-7 /cm^3 (Omega_b 0,049, rho_crit 9,2e-27 kg/m^3),
    Sonnenwind bei 1 AE ~5 /cm^3, Verhaeltnis ~2e7. Bei kappa proportional zur Dichte: DES-Schranke je Dichte
    uebertragen gibt im interplanetaren Raum nur kappa < ~3e-21 /m ~ 4e5 H0/c. Fuer einen dichteabhaengigen Verlust ist
    der Sondentest also um Groessenordnungen empfindlicher als DES. Dann zaehlt aber zuerst die Luft (Dichte ~2,5e19 /cm^3
    auf ~8 km): ein solcher Verlust fiele bodennah auf, wo die Praezisionsstrecken rundweg-geregelt und blind sind
    (TEILE-SCHRANKE-L V1).
- **GS2: kappa ist frequenzunabhaengig.** Nicht geprueft. Fuer achromatisches z noetig; ein Vergleich Radio- gegen
  optische Rotverschiebung derselben Quellen (HI 21 cm gegen optisch) wuerde es begrenzen [L], nicht abgerufen.
- **GS3: Zweiwege-Doppler hat keinen freien Bias.** Teilweise geprueft: DE440 und Thornton/Border nennen keinen
  Doppler-Bias; Drehende Sonden (Juno 2 U/min, Pioneer) haben einen Spin-Beitrag; ob dort ein freier Bias geschaetzt
  wird, blieb offen (A12 Werkzeugtext, A13 leer). Bei Dreiwege-Doppler gibt die Uhrenrate zwischen Stationen
  5e-14 (Thornton/Border Tab. 3-3) einen Versatz in der Groesse des Hubble-Signals bei Saturn [S, M].
- **GS4: Die Laufzeit (Range) ist von R1 unberuehrt.** Geprueft am Schreibtisch [M]: gilt nur, wenn die Modulation nicht
  mitgestaucht wird (R1). Wird die ganze Signalform gestaucht (R2), wandert die Range mit und Doppler gegen Range sieht
  nichts. Kopplung ueber Rate-Aiding ~mm, vernachlaessigbar.
- **GS5: Doppler wird im Modell als Laufzeitaenderung gerechnet.** Geprueft an der Quelle (DE440 Abschn. 5) [S].
  Das ist genau die Identitaet, die R1 bricht; deshalb gibt es im Standardmodell keinen Parameter dafuer.
- **GS6: Der R1-Versatz hat ein festes Vorzeichen** (Rotverschiebung, scheinbares Entfernen). Geprueft ueber A6 [S]:
  Der H-lineare Term zeigt "in outer direction", Pioneer entgegengesetzt.

## 4. Kalibrierung (a/b/c)
- (a) gemessen [S]: Asmar 2005 (3e-15 bei 1000 s); Thornton/Border Tab. 3-3; DE440-Reste (Cassini 3 m, Juno 13 m,
  MESSENGER 0,7 m) und Datentypen; Pioneer a_P (Anderson 2002); Odyssey-Archivfelder.
- (b) verdichtet [M, ES]: drei Regime R1/R2/R3; v_app = kappa c D; DRVID als R1-Observable; Empfindlichkeitsschaetzungen;
  Ephemeride R1-blind; Pioneer-Grenze ~5e3 H0/c; Dichte-Uebertragung GS1.
- (c) gewachsene Gewissheit ohne neue Evidenz: "Niemand hat R1 im Sonnensystem begrenzt." Die Sicherheit stieg nach
  A3/A10 (zwei Suchen, keine Arbeit), beruht aber auf Werkzeugtexten von Suchmaschinen und auf 2 leeren Abrufen
  (A13, A14). Warnzeichen. Ebenso: "Bahnfits schlucken den Versatz" stuetzt sich auf ein allgemeines Beispiel
  (Thornton/Border 3.6) und eine nicht begutachtete Quelle (A. J. Anderson), nicht auf einen Test mit eingebautem kappa.

## 5. Berichtigungen und Fundstellen vor dem Dossier
- Pioneer-Grenze (1.2): dort a_lim ~1e-10 m/s^2 angenommen -> ~4e3 H0/c. Mit a_lim = 1,33e-10 m/s^2 (Unsicherheit von
  a_P laut Anderson 2002, Abstract) -> 3,7e-23 /m ~ 5e3 H0/c [M]. Beide nur Groessenordnung; im Dossier "~4e3 bis 5e3".
- Seiten (aus Seitenumbruechen der .txt-Dateien): A5 Equ. 2 und "easily absorb" S. 3; Gedanken-Experiment S. 6;
  "constant positive frequency shift" S. 7; Zitat a_P = 7,77e-8 cm/s^2 S. 8; "only line of sight Doppler" S. 9.
  A6 Gl. (27) und "suppressed by a factor β" S. 7; "outer direction" und McVittie-Satz S. 8; Gl. (36) und Schluss S. 9.
  A9 Abschn. 5 S. 10 bis 11; Tab. 4 S. 10; Abb. 9 (Juno) S. 12; Abb. 11 (Cassini) S. 13.
  A8 nach Kopfzeilen: "biased range"-Satz S. 20; Tab. 3-3 S. 33 f.; Abschn.-3.6-Beispiel S. 35 f.
- Ableitbarkeitsprobe zum Kartenvorschlag: Projekt-grep 09:07:39 ohne DRVID-Treffer; Signal und Fehler je Pass
  ableitbar [M]; die gemessene nicht-dispersive DRVID-Steigung nicht.

## 6. Abschluss
- Dossier geschrieben ab 09:11:52, Zitatpruefung (hoechstens ein Zitat je Quelle) und Rueckwaertslesen ~~09:13 bis 09:20~~ [geschaetzt, gestrichen; berichtigt:] zwischen 09:11:52 und 09:17:12 (gemessene Grenzen; dazwischen date 09:16:15).
- Endzeit (date): 2026-10-05 09:17:12 CEST. Abrufe 15 von 15 (A13, A14 leer).
- Selbstanzeige: In dieser Abschlusszeile standen zuerst geschaetzte Zeiten (09:13, 09:20; 09:20 lag sogar nach der Endzeit). Gestrichen und durch gemessene Grenzen ersetzt (date 09:17:20).
