# ARBEITSFELD UNSCHAERFE-KANTE-L (feldforscher)

- Start: 2026-10-05 05:48:08 CEST (date). Zeitbox 50 min, mit Zusatzauftrag 65 min, also Ende spaetestens 06:53 CEST.
- Abrufbudget: 8, mit Zusatzauftrag 10 (Leitung 05:49).
- Karte KARTE.md gelesen (05:48). HU1 bis HU5 unveraendert uebernommen.
- Zusatzauftrag (Leitung 05:49, Finn woertlich "-13.6 eV Quantum+coulomb fuer Elektronen?"): eigener Abschnitt
  "Wasserstoff (-13,6 eV)" im DOSSIER mit vier Punkten (Eingabe/Ergebnis, Nelson/SED, 1S-2S und GUP-Schranken,
  Larmor-Absturz fuer unsere klassischen Modelle).

## Projektlektuere (05:48 bis 05:52, nur lesen)

- HILBERT.md Z. 89 bis 94 [P]: Tabelle "Nichtkommutierende Messgroessen": Feld und kanonischer Impuls kommutieren,
  keine Unschaerferelation, kein Nullpunktsbeitrag. Bestaetigt Karte.
- five-why report-source.md Z. 80 bis 92 [P]: H = c p sigma_z + Delta sigma_x, <v> = c cos(2 Delta t/hbar);
  Telegraph-Gegenmodell 65.536 Poisson-Pfade, <v> = c exp(-2 lambda t). Bestaetigt Karte.
- QCA-TETRA-1 "Ergebnis zuerst" [P]: Weyl-Automat auf BCC exakt unitaer, c = 1/sqrt(3); auf Finns Diamantnetz mit
  2 Zustaenden je Knoten KEIN isotroper unitaerer Automat (Defekt >= 0,394). Wichtig fuer Lesart (b).
- DOPPELSPALT-L Katalog Z. 116 [P]: Nelson/SED "Mehrzeitkorrelationen (Nelson) [L?]; SED: Probleme bei nichtlinearen
  Systemen [L?]"; Z. 170: QM gegen Nelson im Einteilchen-Doppelspalt empirisch nicht unterscheidbar [ES dort].
  viewpoint of a ..."; Academia-Liste nennt SPIE 2011/2013/2015 zu Unschaerferelation. Text lokal nicht vorhanden.
  (Unschaerfe)". In pdf-nachrechnung.md Z. 10 ist "Unschaerfe" eine BEWERTUNGSKLASSE ("Ergebnis stimmt, Herleitung
  ohne Treffer. Website Z. 304 bis 311: Welle-Teilchen-Dualitaet "classically understood according to Louis de
  Broglie" (qualitativ). Unschaerfe kommt auf der Website nicht vor [P].

## Abrufe (Erwartung vorher, Ausgang danach)

### A2 arXiv-API id_list GUP-Satz: 1203.6191, 1411.6410, 0810.5333, 1903.03346, 2305.16193 (HU3, Wasserstoff 3)
- Erwartung (2026-10-05 05:53:29 CEST): Gedaechtnis-IDs stimmen bis auf hoechstens eine. Hossenfelder: Diskretheit und minimale Laenge sind verschiedene Szenarien. Bawaj: beta0-Schranke um 1e33 oder tiefer. Das/Vagenas: Lamb-Verschiebung beta0 < 1e36, STM < 1e21. Bushev: beta0 um 1e6 bis 1e7. Bosso-Review: keine Zahl im Abstract; alle Schranken weit ueber 1 (HU3 tritt ein).
### A3 arXiv-API id_list Stochastik/Wasserstoff: 2208.14189, 1502.06856, 1506.06787, 1107.3101 (HU2, Wasserstoff 2/3)
- Erwartung (2026-10-05 05:53:29 CEST): Derakhshani/Bacciagaluppi 2022: Mehrzeit-Korrelationen der stochastischen Mechanik stimmen MIT Messmodell doch mit der QM ueberein (dann HU2 nur fuer die naive Lesart). Nieuwenhuizen/Liska 2015: SED-Wasserstoff ionisiert sich selbst. Parthey 2011: 1S-2S auf ~4e-15 relativ.
  darunter SPIE 8832 (2013) ZWEI Arbeiten mit Abstract: 883219 "The physical origins of the uncertainty theorem"
  (DOI 10.1117/12.2022656) und 88320H "The nature of the photon in the viewpoint of a generalized particle model"
  (DOI 10.1117/12.2022650). Abstract 883219 [S Abstract]: "the uncertainty is not a property of the physical world but
  rather a limitation of our knowledge about the actual state of a physical process. This view conforms to the quantum
  theory of Louis de Broglie and to Albert Einstein's interpretation." Kein Mechanismus (Radius, Bahn) im Abstract.
  HU4 im Wortlaut nicht belegt. SPIE 2011 und 2015 fehlen bei INSPIRE.
  Nebenbefund: unter demselben Namen 1976/77 DESY-Arbeiten (Compton-Streuung an H und D, Nucl. Phys. B 121); ob dieselbe
  Person, ist nicht geprueft [L?].
- **A2 und A3 technisch gescheitert (05:53:39 und 05:53:45):** 0 Byte, weil export.arxiv.org per http mit 301 auf https
  umleitet und curl ohne -L nicht folgt (HEAD-Probe 05:54:08). Kein Inhalt erhalten; Wiederholung per https mit
  gleicher Erwartung. Zaehlung: Fehlversuche nicht als Abruf gezaehlt, Selbstanzeige im DOSSIER.
- A2-Wiederholung per https (05:54:21): arXiv antwortet "Rate exceeded" (HTTP 429, 14 Byte). Kein Inhalt. Kanalwechsel: A2 ueber INSPIRE-API (eprint-Abfrage), gleiche Erwartung wie oben. A3 spaeter erneut ueber arXiv. Stand 2026-10-05 05:54:56 CEST
- **Ausgang A2 (INSPIRE, 05:54:56, quellen/A2-inspire-gup-20261005-055456.json): bestaetigt, mit einem Teilverstoss.**
  Alle 5 IDs stimmen. Hossenfelder 2013 (Living Rev. Rel. 16): GUP und modifizierte Dispersion als zwei Modellklassen
  [S Abstract]. Bushev u. a. 2019 (PRD 100): beta0 < 5,2e6 (Saphir, 0,3 kg), Quarz-Schaetzung beta0 < 4e4 [S Abstract].
  Das/Vagenas 2008 (PRL 101): Lamb, Landau, STM; Abstract OHNE Zahlen (meine 1e36/1e21 bleiben [L?]). Bawaj 2015: Massen
  um die Planck-Masse (~22 Mikrogramm), "Previous limits ... substantially lowered", Zahl nicht im Abstract.
  Bosso u. a. 2023 (CQG 40): Liste von beta-Schranken nach Strenge sortiert, Schranken an zusammengesetzten Koerpern
  neu bewertet [S Abstract].
  **Teilverstoss:** Bushev nennt Atkinsons Pendeldaten (1936), die "could potentially lead to ... beta0 << 1", aber
  "the exact upper bound ... cannot be reliably established" [S Abstract]. Also: eine Schranke unter 1 ist behauptet
  moeglich, aber nicht belastbar. Erwartung korrigiert: HU3 gilt fuer die belastbaren Schranken; die Frage "beta < 1?"
  ist an der Front offen und haengt am Zusammengesetzt-Problem (Moderator: elementar gegen Schwerpunkt vieler Teilchen).
- A3-Wiederholung arXiv (05:55:30): wieder HTTP 429 "Rate exceeded", kein Inhalt. Kanalwechsel A3 auf INSPIRE (eprint-Abfrage), gleiche Erwartung. Stand 2026-10-05 05:55:39 CEST
- **Ausgang A3 (INSPIRE, 05:55:39, quellen/A3-inspire-stoch-h-20261005-055539.json): bestaetigt (eine Zeile).** Alle 4 IDs
  stimmen; Derakhshani/Bacciagaluppi: Mehrzeit-Korrelationen stimmen mit effektivem Kollaps, mehrere Teilchen dann
  nichtlokal; Nieuwenhuizen/Liska: SED-Wasserstoff ionisiert bei laengeren Zeiten, Relativistik aendert nichts,
  Punktladung vermutet als Ursache; Parthey: 2 466 061 413 187 035 (10) Hz, relativ 4,2e-15 [alle S Abstract].
  **Aber gegen die KARTE (HU2) ist das ein Verstoss:** "scheitert an Mehrzeit-Korrelationen" ist seit Blanchard u. a.
  1986 und D/B 2022 beantwortet; was bleibt, ist der Preis Nichtlokalitaet. Volle Analyse im DOSSIER, HU2.
### A4 INSPIRE, 24-Monats-Suche GUP-Schranken (de > 2024-10-05) (HU3, Regel 7)
- Erwartung (2026-10-05 05:56:10 CEST): 10 bis 40 Treffer; keiner setzt belastbar beta0 < 1 fuer ein elementares Teilchen; beste belastbare Schranken weiter >= 1e4 (Oszillatoren, mit Zusammengesetzt-Vorbehalt); hoechstens einzelne Arbeiten behaupten beta0 < 1 aus Spezialsystemen (dann Teilverstoss, mit Vorbehalt lesen).
- **Ausgang A4 (INSPIRE, 05:56:11, quellen/A4-inspire-gup24-20261005-055610.json): bestaetigt, mit Einheitenfalle.** Nur 5
  Treffer (Titelsuche eng). Al Ghifari u. a. 2025 (GRG 57): "upper bound of beta = 1.5e-7" aus Kernmaterie und
  Neutronensternen [S Abstract]; Einheit im Abstract NICHT genannt. Als dimensionsloses beta0 gelesen waere das bei
  Kernenergien (E/E_Pl)^2 ~ 1e-38 rund 30 Groessenordnungen jenseits jeder Empfindlichkeit, also ist beta hier
  dimensionsbehaftet [ES, Gegenlese-Frage "messen die zwei Zahlen dasselbe?"]. Paliathanasis 2026: kosmologisch,
  beta systematisch negativ, LCDM im 95-%-Intervall [S Abstract]. Valero 2025 (CQG 43): Compton-Schranken an eine
  Skala Lambda, Zahl nicht im Abstract. Kein belastbares beta0 < 1 im Fenster gefunden.
### A5 INSPIRE, Klassiker per Zeitschriftenstelle: Gaveau/Jacobson/Kac/Schulman PRL 53, 419 (1984); Grabert/Haenggi/Talkner PRA 19, 2440 (1979); Nelson Phys. Rev. 150, 1079 (1966) (HU1, HU2, Lesart a/b)
- Erwartung (2026-10-05 05:56:51 CEST): INSPIRE hat GJKS 1984 mit Abstract (Dirac in 1+1 D als analytische Fortsetzung des Telegraphenprozesses, Flip-Rate imaginaer); Nelson 1966 vorhanden (D = hbar/2m), evtl. ohne Abstract; GHT 1979 eher nicht in INSPIRE. Fuerth 1933 nicht abfragbar.
- **Ausgang A5 (INSPIRE, 05:56:51, quellen/A5-inspire-klassiker-20261005-055651.json): bestaetigt (eine Zeile).** GJKS 1984:
  "Poisson processes whose real version gives rise to the telegrapher's equation and which when analytically continued
  produce the Dirac equation" [S Abstract]. Nelson 1966: Diffusion hbar/2m "and no friction", Newton F = ma, fuehrt auf
  Schroedinger, Deutung "entirely classical", "within a limited framework, the two theories are equivalent" [S Abstract].
  GHT 1979 nicht in INSPIRE (wie erwartet); bleibt [L?] bzw. ueber D/B 2022 nur als "long-standing criticism" belegt.
### A6 arXiv-API (sonst INSPIRE), 24-Monats-Suche: stochastische Mechanik / Nelson / SED-Wasserstoff (HU2, Wasserstoff 2, Regel 7)
- Erwartung (2026-10-05 05:58:07 CEST): 5 bis 25 Treffer; Nelson-Linie aktiv (Kuipers u. a., Bacciagaluppi, Derakhshani), Tenor: SM reproduziert QM inkl. Mehrzeit mit effektivem Kollaps, Preis Nichtlokalitaet; SED-Wasserstoff weiter ungeloest (Selbstionisation), hoechstens Teilerfolge mit Strahlungsreaktion oder Ausdehnung des Elektrons.
- A6 arXiv (05:58:07): wieder 429, kein Inhalt. Kanalwechsel A6 auf INSPIRE-Freitext, gleiche Erwartung. Stand 2026-10-05 05:58:17 CEST
- **Ausgang A6 (INSPIRE, 05:58:17, quellen/A6-inspire-stoch24-20261005-055817.json, 31 Treffer): ERWARTUNGSVERSTOSS.**
  - Ghose, arXiv 2609.29248 (24.09.2026!), "The Uncertainty Principle, Uncertainty Relations, and Underlying
    Trajectories: Feynman, Nelson, Bohm, and Persistent Kac-Dirac Dynamics" [S Abstract]: trennt Unschaerfe-RELATIONEN
    (statistische Folgen der QM) vom Unschaerfe-PRINZIP (ontologische Zusatzbehauptung); Kac-Dynamik = Bahnen endlicher
    Geschwindigkeit, diffusiver Grenzfall Wiener, nach Wick-Rotation Dirac; "experimentally established uncertainty
    relations are compatible with markedly different underlying path structures". Das ist fast woertlich Finns Frage,
    elf Tage alt. Erwartet hatte ich die Nelson-Linie allgemein, nicht diese Punktlandung.
  - Ghose, arXiv 2604.03214: Nelson braucht (i) Diffusionsskala = hbar und (ii) die Eindeutigkeitsbedingung der
    Wellenfunktion als Zusatz (Wallstrom-Punkt) [S Abstract]; schlaegt eine Abstandsskala fuer Grenzen der
    Bell-Korrelationen vor.
  - Yordanov, arXiv 2412.19918 (Phys. Scr. 101): Wasserstoff aus Brownscher Bewegung plus stochastischer optimaler
    Steuerung; Bahnsimulationen konvergieren auf Born-Verteilungen und QM-Energiemittel; L_z = m hbar erst nach
    auferlegter Eindeutigkeit der Phase [S Abstract].
  - Lynd, arXiv 2504.08669: Geschwindigkeitsfeld aus Potential UND Gesamtenergie (Energie also Eingabe) [S Abstract].
  - SED-Wasserstoff: im Fenster kein Treffer (nur Cetto/de la Pena zu Spin-Statistik in SED). Korrektur: "weiter
    ungeloest" ist nach Fensterlage nur "kein neuer Beleg", nicht "bestaetigt ungeloest".
### A7 INSPIRE-Freitext: Unschaerfe aus Zusatzdimension (Lesart d), neueste zuerst, 100 Treffer
- Erwartung (2026-10-05 05:59:16 CEST): wenige direkte Treffer; Wesson-Linie (5D, Space-Time-Matter) mit "uncertainty principle from 5D" o. ae.; Dolce (kompakte Zeit, Elementarzyklen); sonst GUP in Extradimensionen (Unschaerfe MODIFIZIERT, nicht ERKLAERT). Kein Treffer, der Heisenberg aus Kantenwahl in einer verborgenen Richtung herleitet.
### A8 INSPIRE: LHAASO Lorentz-Verletzung GRB 221009A (Lesart c, Gitter-Dispersion statt GUP)
- Erwartung (2026-10-05 05:59:16 CEST): LHAASO 2024 (PRL): E_QG,1 > ~1e20 GeV (~10 E_Pl, subluminal linear), E_QG,2 > ~1e11-1e12 GeV; also lineare Gitterkorrekturen bei Planck-Masche ausgeschlossen, quadratische frei.
- **Ausgang A7 (INSPIRE, 05:59:22, quellen/A7-inspire-dim-20261005-055922.json, 97 Treffer, meist Rauschen durch
  "Heisenberg"): ERWARTUNGSVERSTOSS.** Jalalzadeh 2023 (Annals Phys. 452, arXiv 2303.11104) [S Abstract]: Teilchen auf
  der Brane schwingt LAENGS DER ZUSATZDIMENSION; Stabilitaet gibt Bohr-Sommerfeld; "motion along the extra dimension
  allows us to formulate a geometrical version of the uncertainty principle"; Bewegung in der Zusatzrichtung "identical
  to the time-independent Schroedinger equation"; Highlights: hbar aus anderen Konstanten berechenbar, Tunneln als
  Spruenge in der Zusatzdimension. Das ist Lesart (d) fast woertlich, erwartet hatte ich "kein Treffer".
  Weitere: Magpantay 2011 (1108.0750): klassische Bulk-Bewegung MODIFIZIERT Heisenberg zeitabhaengig; Lake u. a. 2023
  (Front. Astron. Space Sci. 10): dimensionsabhaengige Unschaerfe nur bei grossen Zusatzdimensionen, bei Planck-
  Kompaktifizierung keine Abweichung; Mu/Wu/Yang 2009 (Chin. Phys. Lett. 28): minimale Laenge = Kompaktifizierungs-
  radius. Wesson, Dolce: kein Treffer in dieser Abfrage. Im 24-Monats-Fenster kein (d)-Treffer dieser Art.
- **Ausgang A8 (INSPIRE, 05:59:28, quellen/A8-inspire-liv-20261005-055928.json): bestaetigt (eine Zeile).** LHAASO 2024
  (PRL 133, 071501, arXiv 2402.06009): E_QG,1 > 10 E_Pl (linear), E_QG,2 > 6e-8 E_Pl (quadratisch), 95 % [S Abstract].
### A9 arxiv.org Volltext Ghose 2609.29248 (HU1 Fuerth, Lesart a/b, Kac)
- Erwartung (2026-10-05 06:00:13 CEST): Text zitiert Fuerth 1933 mit einer Diffusions-Unschaerfe (50 %); Kac-Prozess gibt im diffusiven Grenzfall D = hbar/2m nur bei gewaehltem Takt; Dirac nur nach Wick-Rotation (also Amplitude, nicht reeller Zufall); kein neuer Messvorschlag.
### A10 arxiv.org Volltext Das/Vagenas 0810.5333 (Wasserstoff-GUP-Schranke)
- Erwartung (2026-10-05 06:00:13 CEST): Lamb-Verschiebung beta0 < 1e36, Landau-Niveaus < 1e50, STM < 1e21.
- **Ausgang A9 (arxiv.org, 06:00:18, quellen/A9-ghose-2609.29248-20261005-060017.pdf/.txt): Teilverstoss.**
  - Bestaetigt: Kac-Skalierung D = v^2/(2 lambda) (Gl. 54), mit D = hbar/2m (Gl. 58/59) und hbar lambda = m c^2
    (Gl. 76) [S]; also die Telegraph-Zeile der Karte stimmt woertlich. Dirac in 1+1 D erst nach Wick-Rotation
    t -> i t, v -> -i v (Gl. 66 bis 77) [S]; "These two routes should not be conflated. The diffusion limit is a limit
    of the real stochastic process, whereas the Kac-Dirac relation involves analytic continuation from a real
    probability dynamics to a complex amplitude dynamics" (Abschn. 8) [S].
  - Verstoss gegen meine 50-%-Erwartung: Fuerth 1933 wird NICHT zitiert (grep ohne Treffer). HU1-Fuerth-Teil bleibt [L?].
  - Neu: Wallstrom 1994 (Gl. 35): Nelson leitet die Quantisierungsbedingung "closed integral grad S dx = n h" nicht
    her, sie wird aufgesetzt [S Abschn. 4]; Derakhshani 2015 (arXiv 1510.06391) schlaegt Zitterbewegung als Antwort
    vor [S Ref. 18, nicht gelesen]. Abbott/Wise 1981: Feynman-Pfade skalieren brownsch, Dx ~ eps^(1/2) (Gl. 4 bis 6,
    Ref. 7) [S].
  - Kein Messvorschlag; Ghose sagt selbst, die Unschaerferelationen waehlen zwischen den Bahnbildern NICHT aus
    (Abschn. 7) [S].
- **Ausgang A10 (arxiv.org, 06:00:24, quellen/A10-dasvagenas-0810.5333-...pdf/.txt): bestaetigt (eine Zeile).** Lamb:
  beta0 < 1e36 (Gl. 13, Lamb-Genauigkeit 1e-12), relative Korrektur ~0,47e-48 beta0 (Gl. 12); Landau beta0 < 1e50
  (Gl. 22); STM beta0 < 1e21 (Gl. 34); elektroschwache Skala beta0 <= 1e34 [S].
- Abrufbilanz: 10 von 10 genutzt (A1 bis A10). Dazu 5 technische Fehlversuche ohne Inhalt (2x http-301, 3x arXiv-API
  429), nicht gezaehlt, Selbstanzeige.

## Gegensweep (nach den Abrufen, nur lokal)

- G1 geprueft: Vorgabe "Delta x Delta k >= 1/2 fuer jede Welle auf dem Netz" gilt auf dem Gitter nur fuer k << pi/l;
  exakt Delta x * Delta(sin kl/l) >= (1/2)|<cos kl>| [M].
- G2 geprueft: "Unschaerfe" in pdf-nachrechnung.md ist eine Bewertungsklasse, nicht Heisenberg (falscher Freund).
- G3 geprueft: Finns Netz = Pyrochlor (Tetraeder an den Ecken), Diamant = Tetraedermitten [P licht-finn-netz-1/PLAN.md
  Z. 30]. Rueckfrage an Finn: welche Kante (4 oder 6)?
- G4 geprueft (06:04): Scout-Cache enthielt Ghose 2609.29248 ab 25.09.; classification-cache.json: "topics":{},
  "checked":"2026-09-28".
- G8 geprueft (06:11): Nachgrep "checkerboard|Schachbrett|Foster/Jacobson" fand DUNKEL-FLIP-L (Foster/Jacobson,
  3+1-Schachbrett, Masse als Flip i eps m, nicht unitaer) und SCHACHBRETT-KAUSAL-1 (1+1 auf Kausalmenge, ZB 2m).
  Kartenvorschlag daraufhin eingeengt (Diamantfall), nicht verworfen. Zitierstellen nachgezogen: G5 in
  Codex-Mediator RUNDE-35.md Z. 277; Wallstrom bei Ghose Abschn. 4.1.

- DOSSIER.md geschrieben ab 06:07:39, Korrekturen bis 2026-10-05 06:14:46 CEST. Ende der Feldarbeit.
