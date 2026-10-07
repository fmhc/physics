# ARBEITSFELD GRB-221009A (Feldforscher fuer claude-primary, Runde 34)

Einzige Arbeitsdatei dieser Karte (Feldregel 5). Vor jedem Schritt neu lesen. Gestrichenes bleibt stehen (~~so~~).
Marken: [S] an der Quelle gelesen (Volltext, Fundstelle), [A] nur Abstract/Metadaten, [L?] nicht gelesen (nur Zitat/Suchtreffer),
[H] eigene Schlussfolgerung/Hypothese, [E] eigene Kopfrechnung mit Formel.

## 0. Start
- Start (date): 2026-10-03 17:52:50 CEST (erste date-Messung). Zeitbox 60 min; Ende wird per date geprueft, nicht vorab eingetragen.
- Vorwissen gelesen: KARTE.md (C1-C4 fest, werden nicht geaendert), LORENTZ.md (Z. 63, Berichtigung Z. 492-501),
  BEOBACHTUNGSSPANNUNGEN.md (ganz), WARUM-SPIN-2.md (Glied 2, Glied 10, Rangliste).
- Werkzeuge: curl, jq, pdftotext, grep, sed -n; WebSearch/WebFetch. Kein python/perl/awk.

## 1. Eigene Erwartungen des Agenten zu Teilfragen (vor dem ersten Abruf, 2026-10-03 17:55; C1-C4 der Leitung bleiben unberuehrt)
- A1 (Photon, Absorption): Galanti/Roncadelli (G/R) nehmen das Carpet-3-Photon E = 300 (+43/-38) TeV bei T0 + ~4536 s; Absorption
  ueber CMB plus EBL (ein Standard-EBL-Modell, z. B. Saldana-Lopez 2021 oder Franceschini 2008); optische Tiefe bei z = 0,151 und
  300 TeV in der Groessenordnung 1e2 bis 1e3, also Ueberleben praktisch null.
- A2 (LIV-Form): reine Photon-LIV, subluminal, modifizierte Dispersion E^2 = p^2 - E^(n+2)/E_LIV^n mit n = 1, 2; Schwellenverschiebung
  der Paarbildung (Jacob/Piran-, Tavecchio/Bonnoli-Ansatz); keine Doppelbrechung, keine Elektron-LIV; die "<"-Schranken kommen aus der
  Forderung, dass das Photon (untere Energiegrenze ~262 TeV) mit ausreichender Wahrscheinlichkeit ankommt.
- A3 (ALP allein benachteiligt): Grund vermutlich, dass bei 300 TeV die Photon-Photon-Dispersion am CMB die ALP-Photon-Mischung in der
  Milchstrasse unterdrueckt (Dobrynina/Kartavtsev/Raffelt 2015), oder dass extreme Kopplungen noetig waeren.
- A4 (Carpet): volle Auswertung 2025 (Carpet-3-Gruppe, Baksan, Troitsky u. a.), ein Einzelereignis, Signifikanz nach Versuchszahl um
  3 sigma, Untergrund aus myonarmen Hadronschauern, Richtungsfehler 1,5 bis 2 Grad.
- A5 (LHAASO zur Zeit des Ereignisses): Die drei LHAASO-Arbeiten nennen KM2A-Photonen bis ~13 TeV im ersten Zeitfenster und geben keine
  ausdrueckliche obere Grenze ueber 100 TeV bei T0 + 4536 s an. [E] Eigene Ortsrechnung: Zenitwinkel der Quelle fuer LHAASO bei
  T0 + 4536 s etwa 45 Grad (bei T0 etwa 28 Grad, passt zu LHAASO 28,1 Grad), also wohl noch im KM2A-Sichtfeld.
- A6 (Schranken): G/R-LIV subluminal wie LHAASO-Laufzeit; Fenster n = 1 etwa 1e20 bis 1,22e21 GeV, n = 2 etwa 7e11 bis 2e13 GeV.
  H.E.S.S.-Mrk-501 (subluminal, Absorption) ist schwaecher (unter 1e20 GeV). Photonzerfall-Schranken (LHAASO 2021) gelten nur
  superluminal. [H] Moeglicher Schliesser: bei reiner Photon-LIV subluminal wird Vakuum-Cherenkov geladener Teilchen erlaubt
  ([E] Schwelle Elektron n = 1: p_th = (2 m_e^2 E_LIV)^(1/3), bei E_LIV = 1,2e21 GeV etwa 85 TeV; Krebsnebel braucht PeV-Elektronen).
  Erwartung: Das wird in der Literatur zum Carpet-Photon selten diskutiert.
- A7 (Gegenpositionen): seit 10/2024 mindestens eine Arbeit mit Zufall/galaktischer Quelle oder Hadron-Fehlkennung; dazu alternative
  neue Physik (sterile Neutrinos, UHECR-Sekundaere, ALP plus LIV).

## 2. Suchstrategie
1. G/R: arXiv abs + PDF v3 (pdftotext), Volltext; Fundstellen mit Gleichung/Seite.
2. Carpet: ATel #15669 (2022), Carpet-3-Volltext (2025?), ueber arXiv-API und Literaturliste von G/R.
3. LHAASO: arXiv:2306.06372 (Science 2023), arXiv:2310.08845 (Sci. Adv. 2023), arXiv:2402.06009 (PRL 2024); grep nach "4536",
   "Carpet", "100 TeV", "upper limit", "zenith".
4. Andere Schranken: H.E.S.S. Mrk 501 (ApJ 2019), LHAASO PRL 128, 051102 (2022), Vakuum-Cherenkov, Doppelbrechung (Polarisation).
5. 24-Monats-Fenster (ab 2024-10-01): arXiv-API "221009A" sortiert nach Datum; WebSearch "Carpet 300 TeV GRB 221009A".
6. Gegensweep am Ende.

## 3. Abruf-Protokoll (Erwartung vor Abruf -> Ausgang)

### Block 1, Erwartungen geschrieben 2026-10-03 17:56 CEST
- R1 arXiv-API id_list=2504.01830 -> Erwartung: zwei Autoren (Galanti, Roncadelli), v1 April 2025, v3 2026; Abstract wie Crossref.
- R2 PDF v3 (pdftotext) -> Erwartung: wie A1-A3; Schranken aus Ueberlebenswahrscheinlichkeit bei unterer Energiegrenze.
- R3 arXiv-API all:Carpet AND all:221009A -> Erwartung: 2-5 Treffer, darunter die volle Carpet-3-Auswertung 2025.
#### Ausgang Block 1 (eingetragen 2026-10-03 ~~~18:05~~ CEST; die Zeit war geschaetzt, date danach: 17:58:49)
- R1 bestaetigt: Galanti, Roncadelli; v1 2025-04-02, v3 2026-06-30 ("Accepted for publication in PRL", 26 S., 10 Abb., mit Supplement).
  Datei quellen/arxiv-2504.01830-meta.xml.
- R2 (PDF v3, sha256 0bb13ef9..., quellen/galanti-roncadelli-2504.01830v3.pdf/.txt), gelesen [S]:
  - Photon: Carpet-3 volle Auswertung ueber EINEN TAG (nicht 4536 s), Einzelereignis E = 300 (+43/-38) TeV; Zufallskoinzidenz-
    Wahrscheinlichkeit "about 9e-3", Fehlkennung als Hadron "about 3e-4" (S. 1, nach [11] = Dzhappuev et al., PRD 111, 102005 (2025)).
    "close to the limit of the field of view of the LHAASO experiment", HAWC unter dem Horizont (S. 1, [11], [12]).
  - Rechnung: N_gamma = Integral 262-343 TeV ueber P(E)*F_em(E) mal Flaeche ~60 m^2 mal ein Tag (Gl. 1, S. 2); F_em = Carpet-Extra-
    polation des LHAASO-Spektrums (Fig. 7 von [11]); Standard N(CP) ~ 1e-96 (S. 2); CMB dominiert bei 300 TeV.
  - ALP: N(ALP) <~ O(1e-4) (S. 2) bzw. ~1e-5 (Suppl. S. 22) gegen Poisson-Forderung N >= 0,0513 (95 %, Gehrels) -> zwei Groessen-
    ordnungen zu wenig. Grund u. a. schwache Mischung oberhalb E_H durch QED und CMB-Dispersion (Suppl. Gl. 33) -> A3 bestaetigt.
  - LIV: Gl. (5) p^2 = E^2 (1 + xi_n E^n/E_LIV,n^n), xi = +1 subluminal; nur subluminal, n = 1, 2; reine Photon-(und ALP-)LIV,
    begruendet mit Liouville-String/D-Brane (S. 3); Energie-Impuls-Erhaltung ausdruecklich angenommen (Suppl. S. 23 unten).
    Schranken Gl. (7), (8) aus N(E_LIV) >= 0,0513; Fehler = Systematik der Carpet-Normierung (S. 4). -> A2 bestaetigt.
  - ERWARTUNGSVERSTOSS-KANDIDAT (A6): G/R diskutieren selbst Fremdschranken (Suppl. S. 22-23): Laufzeit LHAASO 1,22e20 / 7,32e11 GeV;
    Breit-Wheeler (Lang u. a. 2019) 1,21e20 / 2,38e12 GeV; GZK-Photonen (Galaverni/Sigl 5,08e33 / 2,49e22; Lang u. a. O(1e29)/O(1e19))
    -> von G/R fuer nicht anwendbar erklaert, weil LIV die Bethe-Heitler-Paarbildung in der Luft unterdrueckt; Satunin 2021 (Tibet
    diffus) E_LIV,2 > 1,7e13 GeV -> von G/R verworfen ("effectively disappears"). Doppelbrechung n = 1: E_LIV,1 > 3,6e34 GeV ->
    nur in D-Brane-Modellen ohne Doppelbrechung umgangen (S. 4). Vakuum-Cherenkov: kein Wort (grep "Cherenkov" nur Detektorname).
  - Neue Gegen-/Nebenpositionen: Ofengeim/Piran PRD 112, 083055 (2025): n = 2, E_LIV,2 = 1,59e12 GeV erklaert die Verspaetung >1 h;
    Kalashev u. a. PRD 112, 023022 (2025): Protonstrahl (Standardphysik); Neutronstrahl in [11] selbst (Dermer/Atoyan-Idee).
  - [H] Selbstkonsistenz: G/R geben fuer 300 TeV im ALP+LIV-Fall eine Bethe-Heitler-Weglaenge O(1-10) km an (Suppl. S. 24),
    Standard ~0,4 km auf Meereshoehe [E: 47 g/cm^2 / 1,2e-3 g/cm^3]. Dann waere der Luftschauer selbst veraendert, die Carpet-Energie
    und die Photon/Hadron-Trennung beruhen aber auf Standard-Schauern. Pruefen, ob jemand das diskutiert.
- R3 noch offen (naechster Block).

### Block 2, Erwartungen geschrieben 2026-10-03 17:59 CEST (date 17:58:49 unmittelbar davor)
- R3 arXiv-API all:Carpet AND all:221009A -> Erwartung: 2-5 Treffer, darunter Carpet-3 PRD 111, 102005 (2025).
- R4 Carpet-3-Volltext -> Erwartung: Einzelereignis; 9e-3 ist die Zufalls-Koinzidenz (post-trial ~2,4-2,6 sigma), 3e-4 Hadron-
  Fehlkennung; Richtungsabstand ~1,8 Grad; LHAASO-Sichtfeld-Satz mit Zenitwinkel; Energieaufloesung ~15 %.
- R5 LHAASO PRL 133, 071501 (arXiv:2402.06009) Volltext -> Erwartung: subluminal 10 E_Pl / 6e-8 E_Pl; zusaetzlich superluminal
  aehnliche Werte; Zahlen im Text 1,0e20 bzw. 6,9e11 GeV (Runde-7-Agent) oder 1,22e20 / 7,32e11 GeV (G/R).
- R6 LHAASO Sci. Adv. 2023 (arXiv:2310.08845) -> Erwartung: KM2A-Fenster 230-900 s, kein Wort zu Carpet oder T0 + 4536 s.
#### Ausgang Block 2, R3/R4 (eingetragen nach date 18:0x; genaue Zeit unten im naechsten Kopf)
- R3 arXiv-Suche (quellen/arxiv-q-carpet-221009A.xml): 15 Treffer, davon im 24-Monats-Fenster (ab 10/2024): 2502.02425 (Carpet-3,
  PRD 111, 102005), 2502.03453 (Galanti u. a., 3 S.), 2504.01830 (G/R), 2508.07153 (Ofengeim/Piran, PRD 112, 083055),
  2508.08984 (Song/Ma, PLB 870, 139959: "evidence for Lorentz violation"), 2510.07234 (Satunin/Troitsky, JETP Lett. 123, 73 (2026)),
  2510.23113 (Qin u. a., ApJ angenommen: ALP+LIV), 2608.21266 (Wang/Song/Li/Zhu/Ma, PRD 114, 063023 (2026): TeV-Photonen aus
  PeV-Neutrinos). Erwartung "2-5 Treffer" uebertroffen: das Ereignis hat eine eigene kleine Literatur.
- R4 Carpet-3 Volltext (quellen/carpet3-2502.02425v1.pdf, sha256 dd45c334...) [S]:
  - Tab. I (S. 3): 09.10.2022 14:32:35 UT, T - T0 = 4536 s, Zenit 26,5 Grad, RA 289,5, Dec +18,4, Abstand 1,8 Grad; Ne = 36400;
    n_mu(175 m^2) = 0; n_mu(410 m^2) = 3; E = 300 (+43/-38) TeV (Photonannahme, Ne-E-Fit an Gamma-MC, S. 4).
  - Richtungsaufloesung 4,7 Grad (90 % CL) (S. 3) -> ERWARTUNGSVERSTOSS gegen A4 (erwartet 1,5-2 Grad; der Fehlerkreis ist
    gut doppelt so gross).
  - Myonzahl allein: Anteil Hadronschauer mit n_mu <= 3 = 0,127 (S. 4): "it is not that rare". Nur das neuronale Netz (MC-trainiert,
    QGSJET-II-04/FLUKA, Vorhersage 0,927 bei Schwelle 0,71) gibt 3e-4 (S. 5). ERWARTUNGSVERSTOSS-KANDIDAT: Die 3e-4 haengen
    ganz an einem MC-trainierten Klassifikator; die Myonzahl allein sagt 13 %.
  - Zufallskoinzidenz 9,0e-3 = 6 gleich photonartige Ereignisse in 667 Tagen im 4,7-Grad-Kreis (S. 5), also ein Tag als Fenster;
    [E] einseitig etwa 2,4 sigma. Mit Myonzahl-Kriterium 2 Ereignisse/667 Tage -> 3,0e-3 (S. 3); Telegramm 2022: pre-trial 1,2e-4
    (4536 s, strengere Schnitte, ohne 410-m^2-Detektor). Galaktische Quelle 3HWC J1928+178 (evtl. LHAASO J1929+1745) 2,5 Grad
    vom Ereignis; diffuse galaktische Emission > 100 TeV (b ~ 4 Grad) als moeglicher Untergrund genannt (S. 3).
  - LHAASO: "considerably larger zenith angle at LHAASO, close to the limit of the field of view ... LHAASO did not report on the
    GRB 221009A observations beyond 2000 s post trigger" (S. 6, Abb. 6). HAWC: unter dem Horizont.
  - Fluenz > 100 TeV F ~ (1,1 +- 0,9)e-3 erg/cm^2 (68 %) aus einem Ereignis, effektive Flaeche ~ 1,6e6 cm^2 x 0,38 (S. 5-6).
  - Erklaerung in Standardphysik: Neutronenstrahl-"Echo" (Dzhatdoev [100], Dermer/Atoyan) als moeglich genannt (S. 6-7).
  - [E] Groessenvergleich: KM2A ~1,3 km^2 gegen Carpet-3 ~60 m^2 effektiv, Faktor ~2e4. Ein echter Fluss, der Carpet ~1 Ereignis
    gibt, haette KM2A im Sichtfeld Tausende Ereignisse > 100 TeV gegeben. Die Frage "war die Quelle im KM2A-Sichtfeld?" ist damit
    der eigentliche Unterscheidungspunkt fuer C1.

### Block 3, Erwartungen geschrieben 2026-10-03 18:01 CEST (date 18:00:32 davor)
- R7 Satunin/Troitsky 2510.07234 (JETP Lett. 2026) -> Erwartung: gemeinsamer Fit LHAASO + Carpet-3; LIV-Bereich, der Carpet erklaert,
  kollidiert fuer n = 2 mit Satunins eigenen Luftschauer-Schranken (Bethe-Heitler), n = 1 nur in schmalem Fenster; ALP allein schwach.
- R8 Song/Ma 2508.08984 -> Erwartung: LIV-"Evidenz" mit n = 1 nahe 1e20-1e21 GeV, Bezug auf die Ma-Gruppen-Zahl 3,6e17 GeV
  (Lichtgeschwindigkeitsvariation), die mit LHAASO > 1e20 GeV unvereinbar waere.
- R9 Ofengeim/Piran 2508.07153 -> Erwartung: n = 2 mit E_LIV,2 ~ 1,6e12 GeV erklaert Durchsichtigkeit UND ~4300 s Verspaetung;
  [E] Laufzeit n = 2, z = 0,151: Dt ~ 1,5 (E/E_LIV)^2 (1/H0) * 0,165 ~ 3900 s bei 300 TeV und 1,59e12 GeV.
#### Ausgang Block 3, R7 (eingetragen 2026-10-03 nach 18:01; Zeit im naechsten Kopf gemessen)
- R7 Satunin/Troitsky, arXiv:2510.07234v2 = JETP Lett. 123, 73 (2026) (quellen/satunin-troitsky-2510.07234v2.pdf, sha256 8324a246...) [S]:
  - Gemeinsamer Fluenz-Fit WCDA + KM2A + Carpet-3 (26 Punkte; Carpet-Bin Poisson mit Untergrund 0,003 Ereignissen; EBL Saldana-
    Lopez 2021 plus CMB) (S. 2-3).
  - LIV n = 2 subluminal: flaches Minimum bei E_LIV,2 ~ 4e12 GeV, Dchi^2 = 12,99 gegen Standard; LIV aendert nur den 300-TeV-Punkt
    (Abb. 4). ALP: Bestwert m = 5,16e-7 eV, g = 6e-11 GeV^-1, Dchi^2 = 30,48 -> "ALP scenario provides a clearly superior
    description" (S. 3-5). ERWARTUNGSVERSTOSS gegen G/R-Lesart: ALP allein ist hier NICHT benachteiligt, sondern bevorzugt -
    allerdings mit g = 6e-11 (nahe CAST), ausserhalb des G/R-Bereichs g = 3-5e-12, in Spannung mit Weisser-Zwerg-Polarisation.
    -> Zwei Regime, Moderator = zugelassener ALP-Parameterbereich (MWD-Schranke ja/nein).
  - Fremdschranken (S. 5): Satunin 2021 (EPJC 81, 750) aus Luftschauern galaktischer VHE-Quellen E_LIV,2 > 1,7e13 GeV;
    Martynenko, Rubtsov, Satunin, Sharofeev, Troitsky, PRD 111, 063010 (2025): keine anomalen Photon-Unterschauer in Hadron-
    Schauern -> E_LIV,2 > 2,4e14 GeV (Annahme: keine Hadron-LIV). n = 1: Myers-Pospelov-EFT erzwingt Doppelbrechung; GRB 061122
    (INTEGRAL/IBIS) E_LIV,1 > 1,8e34 GeV -> E_LIV,1 ~ 3e20 GeV "ruled out ... by 14 orders of magnitude".
  - Selbstkonsistenz (S. 5-6): bei solchen E_LIV,2 "the very air shower detected by Carpet would start deeper in the atmosphere and
    develop in a non-standard way" -> mein [H] aus Block 1 ist von Carpet-Mitgliedern selbst ausgesprochen.
  - LHAASO: "recorded 4536 s after the GRB trigger, when the source was leaving the LHAASO field of view" (S. 2).
  - Vorzeichenkonvention umgekehrt zu G/R: s_n = +1 superluminal, -1 subluminal (Gl. 1); G/R xi = +1 subluminal. Inhaltlich beide
    subluminal.
  - ERWARTUNGSVERSTOSS (C2, A6): Das n = 2-Fenster von G/R (7,32e11 bis 2,03e13 GeV) ist durch eine 2025er Schranke (2,4e14 GeV)
    um gut eine Groessenordnung geschlossen, sofern Hadronen keine LIV haben; G/R zitieren diese Arbeit nicht (grep folgt).

### Block 4, Erwartungen geschrieben 2026-10-03 18:01:30 CEST (date 18:01:23 davor)
- R10 Martynenko u. a. PRD 111, 063010 (2025) -> Erwartung: n = 2 subluminale Photon-LIV; Grundlage: in Hadronschauern entstehen
  Photonen ueber pi0 mit sehr hohen Energien, deren Unterschauer bei LIV verspaetet waeren; Daten: Auger/Yakutsk/Telescope Array
  X_max oder Myonzahl; Schranke 2,4e14 GeV wie zitiert; Annahme "keine Hadron-LIV" ausdruecklich.
- R11 LHAASO PRL 133, 071501 (arXiv:2402.06009) Volltext -> Erwartung wie R5.
#### Ausgang Block 4, R10 (eingetragen nach date 18:01:23; naechster Kopf mit gemessener Zeit)
- R10a Martynenko, Rubtsov, Satunin, Sharofeev, Troitsky, arXiv:2412.08349v2 = PRD 111, 063010 (2025) (quellen/martynenko-2412.08349v2.pdf,
  sha256 044eb2d7...) [S]: n = 2, subluminale Photon-LIV als EFT (Dim. 6, Gl. 4-6), Elektronen LI; Auger-Myonzahl (z-Skala) schliesst
  M_LIV <= 2,4e14 GeV aus (95 %, S. 6, Abb. 3); bester LIV-Wert M_LIV = 1,9e16 GeV koennte das Myonraetsel erklaeren (S. 6-7).
  Erwartung bestaetigt (Annahme "keine Hadron-/Elektron-LIV" ausdruecklich). Zusatzfund: Abschnitt II C nennt Vakuum-Cherenkov
  fuer LI-Elektronen bei subluminalen Photonen, Schwelle (2 m_e M^2)^(1/3), und vernachlaessigt ihn unter 1e17 eV.
- R10b Martynenko u. a., arXiv:2608.05106v1 (05.08.2026, "to be submitted to PRD", ungeprueft begutachtet) (quellen/martynenko-
  2608.05106v1.pdf, sha256 38b1b32b...) [S]: n = 2 subluminal; Auger-X_max-Verteilungen, "toy analysis": M_LIV > 1,5e21 GeV (95 %),
  ausdruecklich "should not be interpreted as a detector-level experimental limit", zusammensetzungsabhaengig (Abstract, Gl. 38, S. 10).
  Listet bestehende Schranken: Tibet-Krebsnebel 1,4e12; Tibet diffus 1,7e13; TeV-Ausbreitung 2,4e12; Myonzahl 2,4e14 GeV (S. 10).
  ERWARTUNGSVERSTOSS (A6/C2): eine weitere, um 8 Groessenordnungen staerkere (aber vorlaeufige) n = 2-Schranke aus 08/2026.
- [E] Eigene Kinematik (zu pruefen, Frage statt Befund): fuer LI-Elektron und Photon E^2 = k^2 - k^4/M^2 ergibt kollineare Emission
  m^2 M^2 = x^2 (1-x) p^4, Minimum bei x = 2/3: p_th = (27/4)^(1/4) sqrt(m_e M) ~ 1,6 sqrt(m_e M), bei M = 2e13 GeV ~ 160 TeV.
  Das liegt weit unter der in Martynenko u. a. genannten Schwelle (2 m_e M^2)^(1/3) ~ 7e16 eV (dort: "Elektron kommt fast zum
  Stillstand", x -> 1). Falls meine Rechnung stimmt, waeren PeV-Elektronen (Krebsnebel, LHAASO 1,1 PeV) bei G/R-Werten
  instabil. n = 1 analog: p_th = (4 m_e^2 E_LIV)^(1/3) ~ 110 TeV bei 1,22e21 GeV. -> offene Frage an die Leitung, nicht als Befund.

### Block 5, Erwartungen geschrieben 2026-10-03 18:04 CEST (date 18:03:38 davor)
- R11 LHAASO PRL 133, 071501 (arXiv:2402.06009) -> Erwartung: subluminal E_QG,1 > 10 E_Pl, E_QG,2 > 6e-8 E_Pl (95 %), dazu
  superluminal-Werte; Zahlen im Text 1e20/6,9e11 oder 1,22e20/7,32e11 GeV; Daten nur WCDA bis ~7 TeV im fruehen Fenster.
- R12 LHAASO Sci. Adv. 9, eadj2778 (arXiv:2310.08845) -> Erwartung: KM2A 230-900 s, Zenitwinkel 28 Grad; kein Wort zu Carpet;
  keine obere Grenze > 100 TeV spaeter als 2000 s.
- R13 LHAASO Science 380, adg9328 (arXiv:2306.06372) -> Erwartung: WCDA-Fenster bis ~3000 s, Quelle bis ~6000 s im Sichtfeld.
#### Ausgang Block 5 (eingetragen nach date 18:03:38; Kopf des naechsten Blocks mit gemessener Zeit)
- R11 LHAASO PRL 133, 071501 (quellen/lhaaso-2402.06009.pdf, sha256 fea2278e..., Fassung "Dated: February 17, 2026") [S]:
  Abstract "E_QG,1 > 10 times of the Planck energy", "E_QG,2 > 6 x 10^-8 E_Pl" (95 %). Text (Summary S. 6, Tab. I): subluminal
  E_QG,1 > 1,0e20 GeV, E_QG,2 > 6,9e11 GeV (ML/MINOS); superluminal 1,1e20 / 7,0e11 GeV; CCF schwaecher (0,6e20 / 4,7e11);
  "ML calibrated" 1,1e20 / 7,2e11. Daten: WCDA 0,2-7 TeV, Segmente 232-400 s. -> Die Leitungsangabe Z. 499-500 (1,0e20 und 6,9e11,
  subluminal) ist jetzt an der Quelle gelesen [S]. "10 E_Pl" ist gerundet: 1,0e20 GeV = 8,2 E_Pl [E]. G/R setzen 1,22e20 und
  7,32e11 GeV (= gerundete Abstractwerte mal E_Pl); die Fensterunterkante ist an der Quelle also 1,0e20 GeV, nicht 1,22e20.
  Erwartung bestaetigt (beide Richtungen angegeben, fast gleich). Zusatz: "remained within LHAASO's field of view for the next
  6000 seconds" (S. 2).
- R12 LHAASO Sci. Adv. 9, eadj2778 (quellen/lhaaso-2310.08845.pdf, v2, sha256 7dde47f2...) [S]:
  - S. 2-3: Sichtfeld Zenit < 50 Grad; Quelle "left the FOV at T0 +6000s"; Zenit 28 Grad bei T0, 31,5 Grad bei T0 + 1000 s;
    Abschn. 4.1: 28,8 / 31,2 / 35,1 Grad bei T0 + 230 / 900 / 2000 s; KM2A-Tastgrad 100 %; effektive Flaeche ~900 000 m^2 ab ~20 TeV.
  - S. 4, woertlich: "Gamma-ray events with energy above 100 TeV were searched for during a long period from T0 to T0 +6000s;
    however, no event was detected."
  - GROESSTER ERWARTUNGSVERSTOSS (C1, A5): LHAASO-KM2A hat das Carpet-Zeitfenster (T0 + 4536 s) abgedeckt, die Quelle war im
    Sichtfeld ([E] Zenit ~45 Grad, eigene Ortsrechnung; Interpolation 35,1 Grad bei 2000 s -> 50 Grad bei 6000 s gibt ~44,5 Grad),
    und es gab NULL Ereignisse > 100 TeV. Carpet-3 schreibt "LHAASO did not report on the GRB 221009A observations beyond 2000 s"
    (S. 6) und "close to the limit of the field of view"; G/R uebernehmen das (S. 1); Satunin/Troitsky: "leaving the LHAASO field of
    view" (S. 2). grep "6000|searched for" in allen drei Texten: kein Treffer. Keine der drei Arbeiten setzt sich mit der
    KM2A-Nullsuche auseinander.
  - [E] Groessenordnung: KM2A bei ~45 Grad etwa 0,8 x 9e5 m^2 ~ 7e5 m^2 gegen Carpet-3 ~61 m^2 (1,6e6 cm^2 x 0,38): R ~ 1e4.
    Fuer einen echten Fluss zur selben Zeit: P(Carpet 1, KM2A 0) <= max_mu mu e^(-mu(1+R)) = 1/(e(1+R)) ~ 3e-5. Untergrund-
    hypothese (Carpet-3 selbst): 9e-3 je Tag (oder 3e-3 mit Myon-Kriterium). Verhaeltnis ~100 bis 300 zugunsten Untergrund,
    ohne Priors. Vorbehalte: LIV-veraenderte Schauer koennten bei KM2A anders rekonstruiert werden; KM2A-Flaeche bei 45 Grad und
    300 TeV nur geschaetzt.
- R13 LHAASO Science 380 (quellen/lhaaso-2306.06372.pdf, sha256 39d193bd...) [S]: "observed by LHAASO for about 6000 s before
  moving out of the field of view" (S. 2, Z. 75-77). Bestaetigt R12.

### Block 6 (24-Monats-Fenster, Gegenpositionen), Erwartungen geschrieben 2026-10-03 18:05:40 CEST (date 18:05:28 davor)
- R14 Abstracts der Kandidaten (Song/Ma, Ofengeim/Piran, Galanti u. a. 2502.03453, Qin u. a., Wang u. a. 2608.21266) -> Erwartung:
  alle nehmen das Carpet-Photon als echt; keine nutzt die KM2A-Nullsuche; Song/Ma n = 1 mit E_LIV ~ 1e20-1e21 GeV.
- R15 WebSearch/arXiv nach Kritik ("Carpet" + "KM2A" bzw. "non-detection", "chance coincidence", "Galactic") -> Erwartung: hoechstens
  eine Arbeit, die die KM2A-Nullsuche gegen Carpet wendet; C3 (Leitung 70 %) daher eher knapp.
#### Ausgang Block 6, R14 (eingetragen nach date 18:05:28)
- Song/Ma, PLB 870, 139959 (2025) [A]: subluminal, E_LV ~ 3e17 GeV (n = 1) -> [E] um Faktor ~300 unter der LHAASO-Laufzeitschranke
  1,0e20 GeV (subluminal); innerhalb der G/R-Oberschranke, aber unterhalb der LHAASO-Unterkante. Erwartung bestaetigt.
- Ofengeim/Piran, PRD 112, 083055 (2025) [A]: "If the association ... is real"; n = 1 "appears to be incompatible with the constraints
  set by analyzing the TeV afterglow of this GRB"; n = 2 subluminal E_LIV2 = 1,30 (+0,56/-0,35)e-7 E_Pl (95,4 %) [E: 1,59e12 GeV]
  erklaert Durchsichtigkeit und Verspaetung; Annahme: Photon gehoert zum LHAASO-Nachleuchten. -> TEILVERSTOSS: O/P halten n = 1
  fuer unvereinbar, G/R fuer offen (1e20-1,22e21). Moderator vermutlich: O/P verlangen zusaetzlich die Verspaetung (n = 1 braucht
  dafuer [E] E_LIV,1 ~ 5e18 GeV, von LHAASO ausgeschlossen), G/R nur die Durchsichtigkeit.
- Qin u. a., ApJ (2026), 10.3847/1538-4357/ae4c4d [A]: ALP g = 1,685e-10 GeV^-1 (ueber der CAST-Grenze 0,58-0,66e-10) plus LIV n = 2.
- Wang u. a., PRD 114, 063023 (2026) [A]: betrifft Vorlaeufer-TeV-Photonen, nicht das Carpet-Ereignis.
- R15 WebSearch nicht moeglich (Sitzungsbudget 200/200 erschoepft, Meldung 18:0x). Ersatz: OpenAlex "cites:W4410437820"
  (Carpet-3, 14 Zitate; quellen/openalex-cites-carpet3.json). Neue Kandidaten: "Is there new physics beyond 30 TeV in the BOAT?"
  (Phys. Dark Univ. 2026, 10.1016/j.dark.2026.102389); "Multi-TeV Gamma Rays from GRB 221009A: Challenges ..." (Galaxies 13, 95,
  2025); "Probes for String-Inspired Foam, Lorentz, and CPT Violations" (Symmetry 17, 974, 2025).
- Neue Kandidaten [A] (quellen/arxiv-q-gegen.xml):
  - Rescic, Recabarren Vergara, Doro, Terzic, arXiv:2511.15542 = Phys. Dark Univ. (2026) 102389: LHAASO-Nichtnachweise ueber ~30 TeV
    enthielten "excesses", vereinbar mit n = 2 subluminaler LIV -> andere Lesart derselben LHAASO-Daten (neue Physik, kein Carpet-Bezug
    im Abstract).
  - C. Li, arXiv:2509.00552 = PLB 869, 139823 (2025): im String-Schaum-Modell koennen Luftschauer trotz subluminaler Photonen
    unveraendert bleiben, "naturally escapes the shower formation constraints". -> ZWEI REGIME: (I) modifizierte Dispersion mit
    Energie-Impuls-Erhaltung (EFT/Phaenomenologie): Schwellen UND Schauer veraendert; (II) String-Schaum: Laufzeit ja, Schauer nein.
    [H] G/R rechnen ausdruecklich in (I) (Energie-Impuls-Erhaltung, Suppl. S. 23; Bethe-Heitler-Unterdrueckung als Ausweg vor GZK-
    Photonen, Suppl. S. 23-24) und berufen sich fuer die Doppelbrechung auf D-Branen (II). Das ist eine innere Spannung.
  - Li/Ma, Symmetry 17, 974 (2025): Uebersicht String-Schaum, behauptet Vereinbarkeit mit LHAASO-PeV-Photonen.
  - Abdalla, Galaxies 13, 95 (2025): Uebersicht (Voids, Kaskaden, LIV, ALP), nur LHAASO bis ~13 TeV im Abstract.
- Kalashev u. a. PRD 112, 023022 (2025): arXiv-Suche au:Kalashev traf nur CTAO-LST (ApJL 988, L42); Protonstrahl-Arbeit nur ueber
  G/R-Darstellung bekannt [L?].

### Block 7, Erwartungen geschrieben 2026-10-03 18:07 CEST (date 18:06:57 davor)
- R16 Ofengeim/Piran Volltext (2508.07153v3) -> Erwartung: sie setzen T_emit ~ T0 + 230 s; n = 1 scheitert an LHAASO-Laufzeit;
  zur KM2A-Nullsuche kein Wort (wie Carpet/G/R).
- R17 arXiv-API abs:"vacuum Cherenkov" AND subluminal AND photon -> Erwartung: wenige Arbeiten; keine bezieht die harte VCR-Schwelle
  auf das Carpet-Photon.
#### Ausgang Block 7, R16 (eingetragen nach date 18:06:57)
- Ofengeim/Piran, arXiv:2508.07153v3 = PRD 112, 083055 (2025) (quellen/ofengeim-piran-2508.07153v3.pdf, sha256 d785a586...) [S]:
  - S. 5: Wenn das Photon zum LHAASO-Nachleuchten gehoert, sind n = 1-Schwelle und LHAASO-Laufzeit "in strong contradiction",
    vereinbar nur bei 0,1 % Glaubwuerdigkeit; S. 7: "if one sets n = 1, the latter probability is ~0.1% ... much smaller than 0.9%,
    the possibility of a spurious association is favored." -> GEGENPOSITION im Fenster (fuer n = 1: Zufall wahrscheinlicher als LIV).
  - S. 7: Kommt das Photon NICHT aus dem Nachleuchten ("new astrophysics" noetig), dann n = 1 nicht ausgeschlossen: 9 E_Pl <~ E_LIV1
    <~ 25 E_Pl [E: 1,1e20 bis 3,05e20 GeV]; Z. 232: "For n = 1 it implies E_LIV1 <~ 3 x 10^20 GeV ~ 25 E_Pl [17]".
  - n = 2: E_LIV2 = 1,30 (+0,56/-0,35)e-7 E_Pl (95,4 %); "consistent with existing limits" [29, 30, 32] -> zitieren Satunin 2019
    (EPJC 79, 1011), aber NICHT Satunin 2021 (1,7e13) und NICHT Martynenko 2025 (2,4e14); Satunin/Troitsky werten genau diesen Bereich
    als ausgeschlossen.
  - Schluss S. 8: "one should hesitate accepting LIV before discarding other possible explanations and just on the basis of a single
    event." Anhang A: Neutronenstrahl-Modell sagt starke Neutrinoemission voraus, IceCube-Grenzen dagegen.
  - Zur KM2A-Nullsuche > 100 TeV: kein Treffer (grep KM2A/6000/searched). Erwartung bestaetigt.
  - ERWARTUNGSVERSTOSS-KANDIDAT: O/P nennen fuer n = 1 als Oberkante ~3e20 GeV (25 E_Pl) unter Verweis auf [17], G/R v3 nennen
    1,22e21 GeV. Pruefen: stand in G/R v1 ein anderer Wert?
- G/R v1 (quellen/galanti-roncadelli-2504.01830v1.pdf, sha256 78570c83...) [S]: Abstract "we derive the first evidence for LIV";
  Text S. 2 (Z. 179-180): "N_gamma^LIV ~ 1 for E_LIV ~ 3.0 x 10^20 GeV". -> Versionsgeschichte: v1 Punktwert bei N = 1 und
  "first evidence"; v3/PRL Oberschranke bei N >= 0,0513 (Poisson 95 %) und "compatible with specific LIV frameworks",
  "potential first indication". Die Fensterbreite haengt also an der Statistikvorschrift: N = 1 -> ~1e20 bis 3e20 GeV
  (Faktor 3); N >= 0,05 -> 1e20 bis 1,22e21 GeV (Faktor 12). O/P und Satunin/Troitsky zitieren noch den v1-Wert 3e20.

### Block 8, Erwartung geschrieben 2026-10-03 ~~18:10~~ CEST (geschaetzt, falsch; date direkt nach dem Abruf: 18:08:26)
- R17 arXiv-API abs:"vacuum Cherenkov" AND abs:subluminal -> Erwartung: wenige Arbeiten; keine bezieht harte VCR auf das Carpet-Photon.
#### Ausgang Block 8, R17 (eingetragen nach date 18:08:26)
- Li/Ma, arXiv:2505.06121v2 = JHEP 10 (2025) 216 [A]: Fehlender Vakuum-Cherenkov ultrahochenergetischer Elektronen (LHAASO-Krebsnebel)
  schraenkt "generic models" mit LIV ein (fruehere Arbeiten PLB 829 (2022) 137034; PLB 835 (2022) 137536; PRD 108 (2023) 063006);
  im phaenomenologischen Ansatz seien die Raten so gross, dass Schwellenanalysen gerechtfertigt sind; in D-Branen-Schaummodellen
  wuerden diese Schranken "naturally evaded". -> ERWARTUNG A6-Zusatz teilweise verletzt: die VCR-Frage ist in der Literatur
  vorhanden (nicht auf Carpet bezogen). Bestaetigt die Zwei-Regime-Struktur: (I) phaenomenologische Dispersion mit Energie-
  Impuls-Erhaltung -> Doppelbrechung (EFT, n = 1), Luftschauer (n = 2), Elektron-VCR (Krebsnebel) greifen; (II) String-Schaum ->
  laut Li/Ma bzw. Li ausweichbar. Ob (II) die fuer die Durchsichtigkeit noetige Schwellenverschiebung ueberhaupt liefert, zeigen
  G/R nicht: sie rechnen die Schwelle in (I). [H]

## 4. Gegensweep (Regel 4), begonnen 2026-10-03 nach 18:08:26
Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
1. Richtungsabstand 1,8 Grad zwischen Carpet-Ereignis und GRB: von Carpet uebernommen. -> PRUEFEN (unten).
2. Gleiche Normierung der LIV-Skalen in G/R, LHAASO, Satunin, Martynenko (Faktor (1+n)/2, E_Pl = 1,22e19 GeV): -> GEPRUEFT an den
   Gleichungen: G/R Gl. 5 p^2 = E^2(1 + xi E^n/E^n_LIV) <=> Satunin Gl. 1 mit s = -1 <=> Martynenko Gl. 4 (n = 2); LHAASO Gl. 1-2
   E^2 ~ p^2[1 - s (p/E_QG)^n] mit Laufzeitfaktor (1+n)/2; E_Pl = 1,22e19 GeV (LHAASO S. 1). Gruppengeschwindigkeit in allen:
   v = 1 - (n+1)/2 (E/E_*)^n. Skalen direkt vergleichbar. [E]
3. Dass das intrinsische Spektrum als ungebrochenes Potenzgesetz bis 300 TeV reicht: nur angenommen. Carpet-3 selbst: oberhalb
   10 TeV setzt Klein-Nishina ein, "another mechanism is needed" fuer > 100 TeV (S. 6); Satunin/Troitsky: jede konkave Form
   machte den Carpet-Punkt "difficult to reproduce even in the absence of absorption" (S. 3). -> Jede Kruemmung senkt N_gamma und
   damit die G/R-Oberschranke; das Fenster schrumpft. [H], nicht nachgerechnet.
4. Dass "LIV nur fuer Photonen (und ALPs)" konsistent ist mit pi0-Zerfall und Hadronen: G/R-D-Brane-Bild (geladene Bausteine
   offene Strings) -> Martynenko-Annahme "keine Hadron-LIV" passt zu G/R selbst. Nicht weiter geprueft.
- Gegensweep-Pruefung zu Punkt 1 (GEPRUEFT): GRB-Position Swift-XRT RA 288,2643, Dec +19,7712 (GCN 32632, Dichiara u. a., quellen/
  gcn-32632.json) [S]; Carpet-Ereignis RA 289,5, Dec 18,4 (Carpet-3 Tab. I) [S]. [E] Abstand: dDec = 1,3712 Grad, dRA cos(Dec) =
  1,2357 x 0,94503 = 1,1678 Grad -> 1,80 Grad. Bestaetigt, kein Verstoss.
- Zusatzpruefung LHAASO-Zenit [E]: Breite 29,36 N, Laenge 100,14 O; Stundenwinkel bei T0 ~29,5 Grad (aus GMST-Naeherung), Modell
  reproduziert LHAASO: T0 -> 28,4 (LHAASO 28,1), T0 + 2000 s -> 35,6 (35,1), T0 + 6000 s -> 50,1 (Austritt bei 50). Bei T0 + 4536 s:
  44,8 Grad, also im Sichtfeld (< 50 Grad). Carpet: 26,5 Grad (Tab. I).
- Kalibrierungs-Warnung: Meine Sicherheit, dass das Ereignis eher Untergrund ist, stieg im Lauf der Recherche (R12). Sie beruht auf
  einer eigenen Abschaetzung [E] (Flaechenverhaeltnis, Poisson), nicht auf einer publizierten Analyse. Keine der gelesenen Arbeiten
  rechnet die KM2A-Nullsuche gegen das Carpet-Ereignis. -> im Dossier als [E]/[H] ausweisen.

## 5. Unterscheidungspunkte (Regel 2), Entwurf
- Photon von GRB vs. Untergrund: KM2A-Zaehlrate bei T0 + 4536 s (zugaenglich, gemessen: 0 Ereignisse > 100 TeV); Schauer-Alter/
  Tiefe des Carpet-Ereignisses (bei LIV tiefer Start; Carpet-Daten im Prinzip vorhanden, nicht veroeffentlicht).
- LIV (I) vs. ALP: ALP erzeugt Strukturen bei 5-10 TeV (KM2A-Delle, Satunin/Troitsky Abb. 4), LIV nur am CMB-Teil >~100 TeV; LIV n = 2
  erzeugt Stunden-Verspaetung, ALP keine.
- LIV (I) vs. LIV (II, String-Schaum): Luftschauer > 100 TeV und PeV-Elektronen im Krebsnebel (VCR); (I) sagt veraenderte bzw.
  fehlende PeV-Photonschauer voraus, (II) nicht. LHAASO sieht PeV-Photonen (Krebsnebel 1,1 PeV) [L?, nicht in dieser Runde gelesen].
- n = 1 vs. n = 2: Energieabhaengigkeit der Verspaetung; braucht mehrere Photonen > 100 TeV (mit einem Ereignis unzugaenglich).

### Block 9, Erwartung geschrieben 2026-10-03 18:10:40 CEST (date 18:10:27 davor)
- R18 LHAASO Krebsnebel PeV (Science 373, 425, 2021; arXiv:2111.06545) Abstract -> Erwartung: Photonen bis 1,1 PeV, Elektronen
  >~ 2 PeV im Nebel noetig.
#### Ausgang Block 9, R18 (eingetragen nach date 18:10:27)
- LHAASO, Science 373, 425 (2021), arXiv:2111.06545 [A]: Spektrum bis 1,1 PeV, "presence of a PeV electron accelerator", aber "we do
  not exclude a non-negligible contribution of PeV protons". -> Die PeV-Elektronen sind gefolgert, nicht gemessen; das VCR-Argument
  (Abschn. Block 4, [E]) bleibt eine Frage.

## 6. Dossier
- Dossier wird jetzt geschrieben (DOSSIER.md); Zeit per date im Dossierkopf.
- REGELVERSTOSS (eigener, gemeldet): Um 18:11:55 habe ich in einem Anzeige-Befehl versehentlich `awk 'NR>1'` aufgerufen (nur zum
  Weglassen der Kopfzeile einer Dateiliste). Die Auftragsregel "lokal kein python3, perl oder awk" ist damit einmal verletzt; kein
  Rechenergebnis haengt daran. Ab jetzt nur ls/grep/sed -n.

## 7. Rueckwaertslesung (Gegenlesen in beide Richtungen), nach dem Schreiben von DOSSIER.md
- Seitenzahlen per Formfeed-Zeilen der pdftotext-Ausgaben nachgeprueft. Berichtigt (alte Eintraege oben bleiben stehen):
  - G/R v3: Supplement-Fremdschranken stehen auf S. 21-23 (nicht ~~22-24~~); N(ALP) ~1e-5 auf S. 21 (nicht ~~22~~); Weglaenge
    O(1-10) km und Energie-Impuls-Erhaltung auf S. 23 (nicht ~~24~~ bzw. ~~"23 unten"~~); Gl. 33 auf S. 14 (nicht ~~11~~).
  - G/R v1: "N ~ 1 for E_LIV ~ 3.0e20 GeV" auf S. 3 (nicht ~~S. 2~~).
  - LHAASO PRL: "remained within LHAASO's field of view for the next 6000 seconds" auf S. 3 (nicht ~~S. 2~~).
  - LHAASO Science 380: Sichtfeld-Satz auf S. 3 (nicht ~~S. 2~~).
  - Satunin/Troitsky: "leaving the LHAASO field of view" auf S. 3 (nicht ~~S. 2~~).
  - Ofengeim/Piran: "spurious association is favored" und 9-25 E_Pl auf S. 6 (nicht ~~S. 7~~); n = 2-Ergebnis S. 8 und Abstract.
- DOSSIER.md entsprechend berichtigt (22 Zeilen; Vorfassung als Kopie im Sitzungs-Scratchpad, nicht im Projekt).
- Zahlen im Dossier gegen die Quellen gegengelesen: Fensterfaktoren 10/12,2/29,4, Abstaende 12 (2,4e14/2,03e13), ~13 (Doppelbrechung),
  ~8 (Martynenko 2026), R ~ 5e3-1e4 und 1/(e(1+R)) = 3,7e-5 bis 7,4e-5 - konsistent.

### Block 10 (Restzeit fuer offene Frage 3), Erwartung geschrieben 2026-10-03 18:17:20 CEST (date 18:17:09 davor)
- R19 Jacobson/Liberati/Mattingly, PRD 67, 124011 (2003), arXiv:hep-ph/0209264, Abschnitt Vakuum-Cherenkov -> Erwartung: fuer
  Photon-LIV xi < 0 und LI-Elektron (eta = 0) ist harte Photonemission oberhalb p_th ~ (m^2 M/|xi|)^(1/3) (n = 1) erlaubt, also
  dieselbe Skalierung wie meine Rechnung (m^2 statt m), nicht (m M^2)^(1/3).
#### Ausgang Block 10, R19 (eingetragen nach date 18:17:09)
- Jacobson/Liberati/Mattingly, PRD 67, 124011 (2003), arXiv:hep-ph/0209264 (quellen/jlm-hep-ph-0209264.pdf, sha256 726d61cd...) [S]:
  Abschn. III B (S. 9-10): Dispersion E^2 = p^2 + m^2 + eta p^n/M^(n-2) (Elektron), omega^2 = k^2 + xi k^n/M^(n-2) (Photon); JLM-n = 3
  entspricht unserem n = 1, JLM-n = 4 unserem n = 2. Fuer xi < eta <= 0 (Fall b, harte Photonemission):
  - Gl. (21): p_th = [-4 m^2 (xi + eta)/(xi - eta)^2]^(1/3); mit eta = 0: p_th = (4 m^2 M/|xi|)^(1/3) = (4 m_e^2 E_LIV,1)^(1/3),
    Photonanteil x = 1/2. -> meine Rechnung bestaetigt.
  - Gl. (27)-(29) (JLM-n = 4): mit eta = 0 ist tau = -2, F = 4 lambda/27 [E], also p_th^4 = (27/4) m^2 E_LIV,2^2, x = 2/3.
    -> meine Rechnung bestaetigt. Die Formel (2 m_e M^2)^(1/3) bei Martynenko u. a. ist nicht die Minimalschwelle (offen, ob dort
    eine andere Endkonfiguration gemeint ist).
  - Rate oberhalb der Schwelle fuer JLM-n > 2: dE/dt ~ alpha E^2, Zerfallsstrecke ~100/E (S. 9) -> Elektronen ueber der Schwelle
    existieren praktisch nicht.
  - S. 10: Elektronen von ~100 TeV in SN1006/Krebsnebel aus Synchrotron-Roentgen plus Magnetfeld gefolgert.
- [E] Folgerung im Rechenrahmen I (nur Photon-LIV, Energie-Impuls-Erhaltung, LI-Elektronen) = G/R-Rahmen:
  - n = 1: 100-TeV-Elektronen -> E_LIV,1 > (1e5)^3/(4 x 2,611e-7) = 9,6e20 GeV; PeV-Elektronen (Krebsnebel, falls leptonisch)
    -> > 9,6e23 GeV. G/R-Oberkante 1,22e21 GeV: Restfenster 9,6e20 bis 1,22e21 bzw. geschlossen.
  - n = 2: 100-TeV-Elektronen -> E_LIV,2 > (1e5)^2/(2,598 x 5,11e-4) = 7,5e12 GeV; PeV-Elektronen -> > 7,5e14 GeV. G/R-Oberkante
    2,03e13 GeV: Restfenster 7,5e12 bis 2,03e13 bzw. geschlossen.
  - Keine Arbeit gefunden, die das auf Carpet anwendet; Li/Ma (JHEP 2025) [A] nennen Krebsnebel-VCR-Schranken fuer "generic models".

## 8. Abschluss
- DOSSIER.md nach Block 10 ergaenzt (Kurzfazit Punkt 2, C2-Zeile, Schranken-Tabelle zwei Zeilen VCR [E], Fensterbilanz, Regime-
  Zeile I, Unterscheidungspunkt I/II, offene Frage 3 teilweise beantwortet und gestrichen-markiert, Quellenliste JLM).
- Titel von Erwartungsverstoss 3 entschaerft: ~~"G/R benutzen das Argument, das sie widerlegt"~~ -> "G/R stuetzen ihren Ausweg auf
  denselben Effekt, auf dem die schliessenden Schranken beruhen" (kein "widerlegt" ohne eigene Pruefung, Regel 7).
- Offene Rueckfragen wandern mit: Dossier Abschn. 12, Fragen 1, 2, 3(a-c), 4, 5, 6.
