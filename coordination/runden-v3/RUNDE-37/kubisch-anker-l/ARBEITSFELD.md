# KUBISCH-ANKER-L: Arbeitsfeld (feldforscher, eine Datei, vor jedem Schritt neu lesen)

- Start 2026-10-04 22:16:21 CEST (date). Zeitbox bis 23:16 CEST. Hoechstens 8 Abrufe, keine Websuche.
- Karte KARTE.md gelesen (bindend, KA1 bis KA3 unveraendert). Gelesen (nur lesen): licht-finn-netz-1/ERGEBNIS.md
  (ganz), NACHTRAG-PHASE-GRUPPE.md (ganz), strang-anker-l/DOSSIER.md (ganz), licht-gleich-l/DOSSIER.md (ganz).
- Kennzeichen: [S] an der Quelle gelesen (Zeile/Abschnitt), [S Abstract], [S-lokal] lokale Kopie eines frueheren
  Agenten, selbst gelesen, [P] Projektdatei, [L] Gedaechtnis, [M] Handrechnung, [ES] eigener Schluss, [H] Hypothese.
- Gestrichenes bleibt stehen (~~so~~), offene Rueckfragen stehen in Abschnitt 9 und wandern mit.

## 0. Lokale Vorarbeit (keine Abrufe) 22:19 bis 22:21

- find nach lokalen Kopien von Kostelecky/Mewes, Data Tables, 0905.0031, 0801.0287, 0809.2846, 1301.5367, 1704.05984,
  1210.1847: **keine** (nur fremde russell_*-Dateien in RUNDE-04/wellen). Also kein SME-Photonen-Text im Projekt.
- grep in RUNDE-34/grb-221009a/quellen (LHAASO 2402.06009, Martynenko 2412.08349v2 und 2608.05106v1, Satunin/Troitsky
  2510.07234v2, JLM): "anisotrop", "direction", "SME", "Kosteleck", "sky" -> keine Richtungsanalyse; nur
  Literaturverweise auf Kostelecky/Russell und JLM Z. 327 "(e) Anisotropy effects" (Laborbewegung) [S-lokal].
- **Martynenko u. a. 2608.05106v1 (5. Aug. 2026, lokal) [S-lokal]:**
  - Z. 131-151: Konvention L_gamma = (s2/M^2) F_ij d^2 F^ij, Gl. (4) E^2 = k^2 - k^4/M_LIV^2 (subluminal). Das ist
    dieselbe Form wie LHAASO Gl. (1) mit n = 2 -> M_LIV = E_QG,2 [M].
  - Z. 692-712: Liste subluminaler Photon-Schranken (95 %): Tibet-ASgamma Crab 1,4e12 GeV; Tibet diffus galaktische
    Scheibe 1,7e13 GeV; TeV-Ausbreitung 2,4e12 GeV; Myonengehalt (Ref. 29) 2,4e14 GeV; eigene Toy-Analyse Auger-Xmax
    M_LIV > 1,5e21 GeV, laut Abstract Z. 21-24 ausdruecklich "should not be interpreted as a detector-level
    experimental limit" und kompositionsabhaengig.
  - Z. 176-209: harter Vakuum-Cherenkov bei Lorentz-invarianten Elektronen, Schwelle Gl. (7) E_e > (2 m_e M^2)^(1/3).
    **Rueckfrage R1 [M]:** Meine Kinematik (kollinear, e -> e + gamma, omega = k - k^3/(2M^2)) gibt
    k^2 p p' = m_e^2 M^2, also Schwelle p = (27/4)^(1/4) sqrt(m_e M) ~ 1,6 sqrt(m_e M), nicht (m_e M^2)^(1/3).
    Nicht geklaert; fuer den Gegensweep wichtig (siehe 7).

## 1. Schreibtisch vor jedem Abruf [M, ungeprueft]

### 1.1 Zerlegung von Finns Muster

- a2(n) = -1/8 + S4/24, S4 = n_x^4 + n_y^4 + n_z^4 in [1/3, 1]. Achsen S4 = 1 -> -1/12; Flaechendiagonalen 1/2 ->
  -5/48; Raumdiagonalen 1/3 -> -1/9. Kugelmittel <S4> = 3 <n_x^4> = 3/5 -> <a2> = -1/10. (Stimmt mit Karte.)
- Mit x = sin t cos f, y = sin t sin f, z = cos t: x^4 + y^4 = sin^4 t (3/4 + cos(4f)/4). Also
  S4 - 3/5 = (2/5) P4(cos t) + (1/4) sin^4 t cos 4f.
- Mit Y40 = (3/(2 sqrt pi)) P4 und Y44 + Y4,-4 = (3/8) sqrt(35/(2 pi)) sin^4 t cos 4f (Condon-Shortley):
  **S4 - 3/5 = (4 sqrt(pi)/15) [Y40 + sqrt(5/14) (Y44 + Y4,-4)]** (z = Wuerfelachse). sqrt(5/14) ist das bekannte
  Verhaeltnis der kubischen Harmonischen [L]. Proben: z-Achse 2/5 (beide Seiten), Raumdiagonale -4/15 (beide Seiten).
- **a2(n) = -1/10 + (sqrt(pi)/90) [Y40 + sqrt(5/14)(Y44 + Y4,-4)]**, nur l = 0 und l = 4 (l = 2 verbietet die kubische
  Symmetrie, ungerade l die Inversion).
- Reiner l = 4-Anteil von a2: +1/60 (Achsen), -1/240 (Flaechendiag.), -1/90 (Raumdiag.); Kugel-RMS
  (1/24) sqrt(16/525) = 0,00727. Verhaeltnis zum l = 0-Anteil (0,1): Spitze 1/6, RMS 0,073.
  Probe RMS: <S4^2> = 3<x^8> + 6<x^4 y^4> = 3/9 + 6/105 = 41/105; minus 9/25 -> 16/525 = 0,03048 (= 192 pi/1575/(4 pi)).

### 1.2 Erwartete SME-Form (vor F2 aus dem Gedaechtnis [L], wird an der Quelle geprueft)

- [L] Kostelecky/Mewes 2009: omega = (1 - s0 +- sqrt(s1^2 + s2^2 + s3^2)) p, s0 = sum_djm omega^(d-4) Y_jm(n) c^(d)_(I)jm,
  isotrop c-ring = c_00/sqrt(4 pi). Nicht doppelbrechend = nur s0. d = 6: j = 0 bis 4, 25 Koeffizienten.
- Abgleich Phasentempo 1 - s0 gegen 1 + a2 (k l)^2 (hbar = c = 1): sum_jm Y_jm c^(6)_(I)jm = -a2(n) l^2.
  - c^(6)_(I)00 = (sqrt(pi)/5) l^2 = 0,3545 l^2; c-ring^(6)_(I) = l^2/10.
  - Netzrahmen: c^(6)_(I)40 = -(sqrt(pi)/90) l^2 = -0,01969 l^2; c^(6)_(I)4,+-4 = -0,01177 l^2; sonst null.
  - Drehinvariante Norm des j = 4-Teils N4 = (sqrt(pi)/90) sqrt(12/7) l^2 = 0,02579 l^2; N4/c00 = 0,0727; c40/c00 = -1/18.
  - Gerade j -> egal, ob n die Flug- oder die Quellrichtung ist.
- LHAASO in dieser Form: Phasentempo 1 - (1/2)(E/E_QG,2)^2 -> c-ring = 1/(2 E_QG,2^2) < 1/(2 (6,9e11)^2) =
  1,05e-24 GeV^-2 (Sichtlinie GRB 221009A); c00 < 3,72e-24 GeV^-2. Probe: l^2 < 1,05e-24 * 12 GeV^-2 -> l < 3,55e-12
  GeV^-1 * 1,973e-16 m GeV = 7,0e-28 m, wie ERGEBNIS Abschn. 4.

### 1.3 Was eine l = 4-Schranke fuer l bringen kann [M]

- Gleiche Empfindlichkeit X je Sichtlinie angenommen: isotroper Weg mit kleinstem abs(a2) = 1/12: l^2 < 12 X.
- Nur Richtungsunterschiede (l = 4 allein): groesste Differenz zweier Richtungen 1/12 gegen 1/9 = 1/36; aus zwei
  Sichtlinien mit je X bestenfalls l^2 < 2 X * 36 = 72 X -> l-Schranke mindestens sqrt(6) = 2,4-mal schwaecher, und das
  nur, wenn zwei Quellen zufaellig laengs Achse und Raumdiagonale liegen.
- Ueber Koeffizientenschranken B4 je c_4m (beliebige Ausrichtung): N4 <= 3 max abs(c'_4m) -> l^2 < 3 B4/0,02579 = 116 B4;
  isotrop l^2 < 2,82 B00. Der l = 4-Weg gewinnt nur bei B4 < 0,024 B00.
- **Erwartung daraus [ES]:** KA2 im Kern (Netzschranke ueber l = 4 schwaecher als 7e-28 m) ist fast ableitbar. Offen ist nur,
  ob die Literatur B4 viel schaerfer als B00 hat (dann Verstoss).
- **KA3 [ES]:** Trennen heisst: ein gemessenes, nicht verschwindendes quadratisches Signal in mehreren Richtungen. Solange
  nur Schranken (Nullresultate) vorliegen, sind "kubisch" und "isotrop" beide nur begrenzt, nicht getrennt. Verstoss
  waere nur ein veroeffentlichter Richtungsbefund (ein Signal) oder eine Analyse, die eine feste Kopplung l = 4 an l = 0
  ausnutzt.

## 2. Abrufplan (hoechstens 8)

| Nr | Ziel | Zweck |
|---|---|---|
| F1 | arXiv-API: anisotrop + Lorentz + Laufzeit/Dispersion, neueste zuerst | KA1, 24-Monats-Pflicht (Feldregel 7) |
| F2 | Kostelecky/Mewes 2009, arXiv 0905.0031 (pdf) | Parametrisierung an der Quelle, d = 6, Zahl der Quellen |
| F3 | Kostelecky/Russell Data Tables, neueste Fassung 0801.0287 (pdf) | KA1/KA2: veroeffentlichte c^(6)_(I)jm-Schranken |
| F4 | arXiv-API id_list mit bekannten IDs (Kostelecky/Mewes 2008 0809.2846, Wei u. a. 1704.05984, Beane/Davoudi/Savage 1210.1847, ...) | Abstracts in einem Abruf |
| F5-F8 | je nach Verstoss: Mehrrichtungs-Analyse im Volltext; Gegensweep Gitter/kubisch; Vakuum-Cherenkov subluminal d = 6 | |

## 3. Abrufe (Erwartung vor dem Abruf, Ausgang danach)

### F1 arXiv-API (Erwartung geschrieben 22:22:16 CEST)

- Anfrage: (abs:anisotropic OR abs:anisotropy OR abs:"direction-dependent") AND abs:Lorentz AND (abs:"time delay" OR
  abs:"time of flight" OR abs:"vacuum dispersion" OR abs:"spectral lag" OR abs:"time lag"), neueste zuerst, 80 Treffer.
- **Erwartung:** Treffer Wei u. a. 2017 (GRB 160625B, Sichtlinien-Schranke fuer d = 6 im SME) und Kostelecky/Mewes
  2008/2009; dazu wenige Arbeiten 2018 bis 2026 mit Sichtlinien-Schranken einzelner GRB (auch GRB 221009A). **Keine**
  Arbeit, die alle 25 c^(6)_(I)jm oder gezielt den j = 4-Teil aus vielen Richtungen getrennt begrenzt (70 %). In den
  letzten 24 Monaten 0 bis 3 einschlaegige Treffer.
- **Ausgang F1 (22:22:24 abgerufen, quellen/F1-arxiv-api-anisotrop-laufzeit.xml, 26 kB, 11 Treffer gesamt):**
  - Erwartet und getroffen: Wei u. a. 2017, 1704.05984 [S Abstract]: "direction-dependent dispersion constraints ... on
    nonbirefringent Lorentz-violating effects", GRB 160625B, "two-sided constraints on a variety of isotropic and
    anisotropic coefficients", eine Quelle, eine Sichtlinie. Kostelecky/Mewes 2008, 0809.2846 [S Abstract]:
    "Direction-dependent dispersion constraints are obtained on operators of dimension 6 and 8 using gamma-ray bursts and
    the blazar Markarian 501"; letzter Satz "No evidence appears for isotropic Lorentz violation, while some support at
    one sigma is found for anisotropic violation" (Bezug unklar: steht direkt nach dem WMAP-Satz, d = 3?) -> R2.
  - **Verstoss (teilweise): Mehrrichtungs-Analyse existiert.** Wei, J.-N.; Liu, Z.-K.; Wei, J.-J.; Zhang, B.-B.; Wu, X.-F.
    (2022), 2210.03897, Universe 8, 519 [S Abstract]: "spectral-lag transition features of 32 GRBs ... constraints on a
    variety of isotropic and anisotropic Lorentz-violating coefficients with mass dimension d=6 and 8. While our
    dispersion constraints are not competitive with existing bounds, they have the promise to complement the full
    coefficient space." 32 Quellen > 25 Koeffizienten -> moeglich, dass alle 25 c^(6)_(I)jm gemeinsam begrenzt sind.
    Ob der j = 4-Teil getrennt begrenzt ist und wie scharf: nur im Volltext -> F2.
  - Weitere Treffer ohne Belang fuer d = 6/Richtung: 2004.07661 (Lifshitz, GRB 090510, isotrop), 1907.06514 (Kislat,
    Polarimetrie, Uebersicht: "Observing multiple sources covering the entire sky allows the extraction of constraints
    on anisotropy"), GW-Tempo, Hořava, Aequivalenzprinzip.
  - **24-Monats-Pruefung (Feldregel 7):** juengster Treffer 2022-10; Okt. 2024 bis Okt. 2026 **null** Treffer fuer diese
    Wortwahl. Vorlaeufig "nach Recherchestand nichts Neueres", Wortwahl-Grenze -> spaeter zweite Anfrage mit
    "Standard-Model Extension"/"coefficients" pruefen (R3).
  - Erwartung korrigiert: Es gibt eine Mehrrichtungs-Arbeit (32 GRB), aber nach eigener Aussage nicht konkurrenzfaehig.

### F2 Volltext Wei, J.-N. u. a. 2022, arXiv 2210.03897 (Erwartung geschrieben 22:23)

- **Erwartung:** Sie nutzen die Kostelecky/Mewes-Laufzeitformel mit sum_jm Y_jm(n) c^(d)_(I)jm. Daten sind
  Fermi/GBM-Spektralverzoegerungen bei keV bis MeV; daher sind die d = 6-Schranken etwa 1e-12 GeV^-2 (+-2
  Groessenordnungen), rund 10 bis 12 Groessenordnungen schwaecher als LHAASO (1e-24 GeV^-2). Form: je GRB eine
  Sichtlinien-Schranke und vermutlich Einzelkoeffizienten-Schranken ("one at a time"); gemeinsamer Fit aller 25
  Koeffizienten 50 %. Ein Richtungsbefund (Signal) 10 %.
- **Ausgang F2 (22:23:18 abgerufen, quellen/F2-wei-2210.03897v1.pdf/.txt, 6 Seiten laut file, Text 2603 Zeilen):**
  - Getroffen: Formel s0 = sum p^(d-4) Y_jm(n) c^(d)_(I)jm, "n is the direction of the source" (Z. 160, 180 [S]);
    Gruppentempo dv_g = -sum (d-3) E^(d-4) Y_jm(n) c^(d)_(I)jm (Z. 209 [S]), also Faktor 3 bei d = 6 wie LHAASO 3/2
    gegen 1/2; Laufzeit Gl. (4) (Z. 223-240 [S]); isotroper Grenzfall Y00 = 1/sqrt(4 pi) (Z. 255-262 [S]).
    Groessenordnung d = 6: Sichtlinien-Kombinationen ~1e-11 bis 1e-13 GeV^-2 (Tabelle 2, Z. 600-1030, Layout
    zerrissen [S]); GRB 130427A 4,69e-14 GeV^-2 (Z. 2328-2334 [S]); Prior +-1e-10 GeV^-2 (Z. 548-549 [S]).
    Je GRB **eine** Sichtlinien-Kombination (Z. 2346-2350 [S]).
  - **Verstoss 1 (gross): kein gemeinsamer Fit.** Einleitung Z. 138-141: "We combine these limits with previous results
    in order to fully constrain the nonbirefringent ... coefficients with d = 6 and 8." Diskussion Z. 2346-2350: "For each
    GRB, we derive a limit on one direction-specific combination ... Thus, it is not feasible to conduct a global fit on
    the LIV parameters by taking into account all GRBs ... in the vacuum anisotropic model." Die volle Zerlegung ist also
    angekuendigt, aber nicht ausgefuehrt. Keine getrennten Schranken fuer j = 4.
  - **Verstoss 2 (gross): nominelle Richtungssignale.** Z. 2278-2304: 5 von 32 GRB (131231A, 160625B, 190114C, 200829A,
    210619B) "incompatible with zero at the 4.7 sigma, 12.3 sigma, 5.0 sigma, 6.1 sigma, and 5.2 sigma"; AIC verwirft
    "no LIV" mit 1e-6 bis 1e-34. Deutung der Autoren: "cannot be due to Lorentz-violating effects, as this would
    contradict with previous upper limits and must therefore be of intrinsic astrophysical origin"; die Schranken
    dieser fuenf seien "artificial upper limits".
  - Grundsatz an der Quelle (Z. 114-117 [S]): "at least (d - 1)^2 sources distributed evenly in the sky are needed to
    fully constrain the anisotropic ... coefficient space for a given d", die isotrope Einschraenkung "disregards
    d(d - 2) possible effects from anisotropic violations" (d = 6: 25 bzw. 24).
  - Zusammenfassung Z. 2368-2372 [S]: "For the case of d = 6, our constraints are not competitive with existing bounds".
  - Fruehere Sichtlinien-Schranken d = 6 laut Z. 119-125 [S]: GRB 021206 (Boggs u. a. 2004), GRB 080916C, "four bright
    GRBs" (Ref. 19 = Vasileiou u. a. 2013, Z. 2462 [S]), GRB 160625B, GRB 190114C; Zusammenstellung in Ref. 1 = Data
    Tables (Z. 2433, 2368 [S]).
  - [ES, Feldregel 1] Zwei Regime fuer die fuenf "Signale": keV-MeV-Spektralverzoegerung (Quellmodell SBPL dominiert,
    Signale 1e-11 bis 1e-13 GeV^-2) gegen GeV-TeV-Laufzeit (LHAASO-Sichtlinie < 1e-24 GeV^-2). Moderator: Photonenergie
    und Quellmodell. Fuer Finns Netz eindeutig [M]: Sein Richtungsverhaeltnis ist hoechstens 4/3 (1/9 zu 1/12); ein
    Signal von 1e-13 in einer Richtung neben < 1e-24 in einer anderen ist mit dem Muster unvereinbar. Die fuenf
    "Signale" koennen also keine Netzsignale sein, gleich wie das Netz ausgerichtet ist.
  - Erwartung korrigiert: Groessenordnung getroffen; "gemeinsamer Fit 50 %" -> nicht ausgefuehrt; "Signal 10 %" -> es gibt
    nominelle Signale, von den Autoren selbst verworfen.

### F3 Data Tables, Kostelecky/Russell, arXiv 0801.0287 neueste Fassung (Erwartung geschrieben 22:24)

- **Erwartung:** Die Photon-Tabelle fuer d >= 5 fuehrt fuer d = 6 (c^(6)_(I)) eine isotrope Schranke (c-ring) aus
  Laufzeit (GRB 090510/Vasileiou bzw. LHAASO 221009A, ~1e-23 bis 1e-24 GeV^-2), vielleicht schaerfer aus Luftschauern
  (Tibet/Crab, Myonen; bis ~1e-29 GeV^-2), dazu eine Liste von Sichtlinien-Kombinationen je Quelle (10 bis 40 Quellen) und
  **keine** getrennten Schranken fuer die neun c^(6)_(I)4m (75 %). Falls doch Einzelschranken fuer j = 4: dann "one at a
  time" aus einer Quelle, nicht aus einer Mehrrichtungs-Zerlegung.
- **Ausgang F3 (22:24:43 abgerufen; quellen/F3-datatables-0801.0287.pdf/.txt = v19, "January 2026 update", Literatur
  bis 31.12.2025, 198 Seiten; Layout-Auszug S. 62 und 63-69 als F3-datatables-D22-layout-*.txt):**
  - Legende Z. 276-279 [S]: Sternchen hinter der Quelle = "Results deduced on theoretical grounds" (abgeleitet, keine
    direkte Messung der Kollaboration).
  - **Verstoss 3 (gross, KA1 getroffen, aber anders): Es gibt zwei vollstaendige Zerlegungen aller 25 c^(6)_(I)jm aus
    vielen Richtungen**, Tabelle D22 Teil 1 und 4 (S. 62, 66 [S]):
    - Guerrero, M.; Campoy-Ordaz, A.; Potting, R.; Gaug, M. (2025), PRD 112, 104002, arXiv 2508.02883 [217]*
      ("Astrophysical dispersion"): c00 = (-0,5 +- 1,5)e-15; c40 = (-0,7 +- 0,7)e-15; Re c41 (-0,2 +- 0,2); Im c41
      (-0,3 +- 0,4); Re c42 (0,1 +- 0,4); Im c42 (0,0 +- 0,5); Re c43 (-0,2 +- 0,2); Im c43 (-0,2 +- 0,2); Re c44
      (0,1 +- 0,3); Im c44 (0,0 +- 0,4), alles e-15 GeV^-2. Vertrauensniveau steht nicht in der Tabelle (R5).
      **Innerhalb der 24 Monate** (Feldregel 7): F1 hat sie nicht gefunden (Wortwahl).
    - Kislat, F.; Krawczynski, H. (2015), PRD 92, 045016, arXiv 1505.02669 [225]: alle 25 als Intervalle, c00 (-2,705
      bis 3,925)e-14; c40 (-2,313 bis 2,739)e-14; Re c41 (-9,021 bis 11,31)e-15; Im c41 (-2,953 bis 3,904)e-14; Re c42
      (-4,650 bis 6,846)e-15; Im c42 (-2,489 bis 1,961)e-14; Re c43 (-7,276 bis 10,14)e-15; Im c43 (-1,246 bis
      1,343)e-14; Re c44 (-3,919 bis 2,923)e-14; Im c44 (-1,801 bis 1,427)e-14 GeV^-2.
  - Sichtlinien-Kombinationen (Teil 2, 3, 5 [S]): 32 GRB [218] 1e-11 bis 1e-15; Wei 2017 (83,1 Grad, 308 Grad)
    (-2,8 bis 34)e-16; Vasileiou 2013 [227] vier GRB, GRB 090510 (117, 334) (-0,31 bis 0,16)e-20, c00 (-1,1 bis
    0,57)e-20; Vasileiou 2010 [228] < 3,9e-22; Fermi 080916C [229] < 3,2e-20; H.E.S.S. PKS 2155-304 [230]
    abs < 7,4e-22, abs(c00) < 2,6e-21; **MAGIC Mrk 501 [231],[18]* (50,2; 253): 3 +1/-2 e-22, c00 10 +4/-7 e-22
    (nicht null)**; Boggs GRB 021206 [232] < 1e-16; Du u. a. 2021 GRB 190114C [222]* (116,9; 54,5): 5,05 +1,72/-1,25
    e-13 (nicht null); Agrawal u. a. 2021 [221]* "sum Y(b n) c" = 10^(-14,2 +- 0,1) GeV^-2 (Wert, keine Schranke).
  - **Staerkste Richtungswerte: HAWC 2020 [190]** (PRL 124, 131101, arXiv 1911.08070): abs(c00) < 12,4e-31;
    Sichtlinien abs(...) < 3,5e-31 (103,45; 276,41), < 4,93e-31 (83,75; 286,95), < 20,1e-31 (67,96; 83,6),
    < 50,3e-31 (53,26; 304,94) GeV^-2. Photon decay [223]* c00 > -1,1e-28 (einseitig, superluminal). Rubtsov/Satunin/
    Sibiryakov 2017 [224]* c00 < 4e-23 (einseitig, subluminal; = E_QG,2 > 2,1e11 GeV [M]). Laserinterferometrie [166]
    abs(c4m) < 1,3e-2 bis 2,4e-4 GeV^-2 (Labor, schwach).
  - Zusammenfassung S3 (Z. 2335-2360 [S]): fuer d = 6 nur isotrop c00 "10^-30 GeV^-2" (maximal two-sided); keine
    anisotrope d = 6-Zeile. -> wohl HAWC (abs(c00) < 1,24e-30).
  - **Verstoss 4 (mittel): LHAASO 221009A (PRL 133, 071501) und die Luftschauer-Schranken (Martynenko u. a.) stehen
    nicht in den Tabellen v19** (grep "LHAASO", "221009", "071501", "Martynenko" leer [S]).
  - **Rueckfrage R4 (entscheidend fuer Finns Netz):** Gilt HAWC nur fuer superluminales Licht (Photonzerfall,
    Photonspaltung [L])? Die Tabelle schreibt Betraege abs(...) <. Finns Netz ist in allen Richtungen subluminal; dann
    zaehlen die 1e-31-Werte fuer das Netz nicht. Falls doch beidseitig: Netz-l < ~4e-31 m [M], 1700-mal schaerfer
    als LHAASO. -> F4.
  - Teil 6/7: doppelbrechende d = 6-Koeffizienten k(E), k(B): Spektropolarimetrie ~8e-18, GRB-Polarisation
    (K/M 2013 [207]*) 1e-31 bis 1e-32 GeV^-2; CMB k(E)20,30,40 = +-(11 +4/-5)e-10 [19]* (nicht null, alte Daten).
  - Erwartung korrigiert: "keine Einzelschranken fuer j = 4 (75 %)" verfehlt: Es gibt sie aus zwei globalen Zerlegungen,
    aber 9 bis 10 Groessenordnungen schwaecher als die besten Sichtlinien (1e-22) und 15 schwaecher als HAWC.
  - [ES, Feldregel 6] Warum die Zerlegung so schwach ist: 25 Koeffizienten brauchen >= 25 Richtungen; die meisten
    Richtungen deckt nur keV-MeV-Material ab; die gemeinsame Loesung erbt die schwaechsten Richtungen.

### F4 arXiv-API id_list (Erwartung geschrieben 22:3x, Zeit siehe date-Zeile davor)

- IDs: 2508.02883 (Guerrero u. a. 2025), 1505.02669 (Kislat/Krawczynski 2015), 1911.08070 (HAWC 2020), 2102.11248
  (Agrawal u. a. 2021), 1210.1847 (Beane/Davoudi/Savage), 0905.0031 (Kostelecky/Mewes 2009).
- **Erwartung:** HAWC: nur superluminal (Photonzerfall/-spaltung), also fuer das Netz ohne Belang (80 %). Guerrero 2025:
  globale Zerlegung aus veroeffentlichten Laufzeitdaten vieler Quellen, nennt die Zahl der Quellen (>= 25). Kislat/
  Krawczynski 2015: erste vollstaendige Zerlegung der 25 Koeffizienten aus GRB/AGN-Laufzeiten. Agrawal 2021: nominell
  bevorzugtes LIV-Modell bei keV-MeV, mit Vorbehalt Quellverzoegerung (60 %). Beane u. a.: kubisches Gitter, Gitterweite
  um 1e-12 fm aus GZK, kubisches Muster in den Ankunftsrichtungen der hoechstenergetischen kosmischen Strahlung (80 %).
- **Ausgang F4 (22:29:09 abgerufen, quellen/F4-arxiv-api-idlist.xml, 6 Eintraege), alles im Rahmen der Erwartung, je
  eine Zeile:**
  - HAWC 1911.08070 [S Abstract]: "Superluminal LIV enables the decay of photons at high energy"; >= 4 Quellen ueber
    100 TeV; staerkste Grenze 2,2e31 eV (n = 1). Nur superluminal genannt. **R4 geloest (mit Vorbehalt [L] fuer n = 2):**
    Die 1e-31-Betragswerte der Tabellen begrenzen fuer Finns subluminales Netz nichts.
  - Guerrero u. a. 2508.02883 [S Abstract]: wandelt veroeffentlichte E_QG,2-Schranken in c^(6)_(I)jm um, "standardize
    them by accounting for systematics, applying missing prefactors, and transforming results into two-sided Gaussian
    uncertainties", verbessert die Einzelkoeffizienten "by about an order of magnitude". Welche Quellen (LHAASO?) und
    welches Niveau: nur im Volltext (R5) -> F5.
  - Kislat/Krawczynski 1505.02669 [S Abstract]: "constraints on all 25 real coefficients ... d=6", Fermi-LAT, 25 AGN,
    plus veroeffentlichte Grenzen; "the first set of constraints on these coefficients ... whereas previous measurements
    were only able to constrain linear combinations".
  - Agrawal u. a. 2102.11248 [S Abstract]: 37 GRB, 91 Messungen; konstante Eigenverzoegerung plus Streuung: "do not find
    any evidence for LIV"; GRB-abhaengige Eigenparameter: "decisive evidence"; "none of the models ... provide a good
    fit ... still missing Physics in the model for intrinsic spectral lags". Moderator = Quellmodell (Feldregel 1).
  - Beane/Davoudi/Savage 1210.1847 [S Abstract]: kubisches Raumzeitgitter (Wilson-Fermionen), staerkste Schranke
    b^-1 >~ 1e11 GeV aus dem Abbruch des Spektrums der kosmischen Strahlung; Test: "rotational symmetry breaking" in den
    Ankunftsrichtungen der hoechstenergetischen kosmischen Strahlung. [M] b < ~2e-27 m.
  - Kostelecky/Mewes 0905.0031 [S Abstract]: Zerlegung in spinbehaftete Kugelflaechenfunktionen, isotroper und nicht
    doppelbrechender Grenzfall, GRB-Dispersion d = 4 bis 9. Formel selbst an F2 Z. 160-209 gelesen.

### F5 Volltext Guerrero u. a. 2025, arXiv 2508.02883 (Erwartung geschrieben 22:30)

- **Erwartung:** 20 bis 40 Laufzeitergebnisse (GRB 090510, GRB 221009A/LHAASO, Mrk 501, PKS 2155-304, Crab-Pulsar),
  je in eine Sichtlinien-Kombination mit Gauss-Fehler umgerechnet, dann lineare Ausgleichsrechnung fuer 25
  Koeffizienten; Fehler ~1e-15 GeV^-2, weil viele Richtungen nur schwach abgedeckt sind; Fehler als 1 sigma. LHAASO
  enthalten 70 %. Keine Aussage, dass die Daten Anisotropie bevorzugen (85 %).
- **Ausgang F5 (22:30:07 abgerufen; quellen/F5-guerrero-2508.02883v1.pdf/.txt/-layout.txt):** im Kern getroffen,
  zwei Einzelheiten neu.
  - Getroffen: LHAASO 221009A ist enthalten (Z. 583-588, 1011-1012 [S]: "GRB 221009A stands out for providing the most
    stringent bound to date, it remains an isolated event"); dazu Crab-Pulsar, Mrk 421, PG 1553+113, Mrk 501,
    PKS 2155-304, GRB 090510/080916C/090902B/090926A, 190114C, 160625B, 021206, 24 AGN aus Kislat/Krawczynski. Einseitige
    95-%-Grenzen in zweiseitige Gauss-Intervalle umgerechnet (Z. 998-1008 [S]).
  - Tabelle II (Layout Z. 760-816 [S]): Erwartungswert, Standardabweichung, 95-%-Grenzen (e-15 GeV^-2): c00 -0,5 / 1,5 /
    [-3,4; 2,4]; c40 -0,7 / 0,7 / [-2,0; 0,6]; Re c41 [-0,7; 0,2]; Im c41 [-1,0; 0,4]; Re c42 [-0,7; 1,0]; Im c42
    [-1,0; 1,0]; Re c43 [-0,6; 0,2]; Im c43 [-0,6; 0,1]; Re c44 [-0,5; 0,7]; Im c44 [-0,9; 0,9]. -> Die Data-Tables-Zahlen
    sind Erwartungswert +- 1 Standardabweichung (R5 geloest).
  - Tabelle III (Layout Z. 840-870 [S]): gedrehte Kombinationen y1 bis y25 (e-22 GeV^-2): y1 = -9,6e-5 +- 3,5e-3, also
    sigma 3,5e-25 GeV^-2 (beste Richtung); y25 = -4,1e6 +- 2,9e7, also sigma 2,9e-15 GeV^-2.
  - **Neu (bestaetigt mein [ES] aus F3 an der Quelle):** Z. 2020-2027 "the improvement in the least sensitive measurement
    in the sample of the best 25, which determines the order of magnitude of the bounds on all coefficients"; Z. 2028-2031
    "a set of fourteen additional competitive bounds from very-high-energy or ultra-high-energy gamma-ray observatories
    could improve sensitivity to all c(I)jm by another five orders of magnitude!"
  - **Neu:** Z. 1999-2005 LHAASO-Vorbehalt der Autoren: Eigenverzoegerungen nicht beruecksichtigt; "nature has conspired
    to compensate for a LIV-induced effect" sei nicht ausgeschlossen. Z. 2013-2016: "none of the most sensitive analyses
    have incorporated a statistical treatment of intrinsic time delays".
  - Keine Aussage, dass die Daten Anisotropie bevorzugen (gesucht: "anisotrop", "isotropic" Z. 442 nur Formalismus) [S].

### R1 geklaert an lokaler Quelle (kein Abruf) 22:32

- JLM 2003 lokal (RUNDE-34/.../jlm-hep-ph-0209264.txt) Z. 438-447 Gl. (14), Z. 488-492 Gl. (15) [S-lokal]:
  m^2/p^n = -xi w (1-w)^(n-2) + eta (w + ... + w^(n-1)), w = q/p. Lorentz-invariante Elektronen (eta = 0), subluminales
  Licht (xi < 0), n = 4: m^2 M^2/p^4 = abs(xi) w (1-w)^2, Maximum bei w = 1/3 (Wert 4/27) -> **p_th = (27/4)^(1/4)
  sqrt(m_e M/abs(xi)^(1/2))**, genau meine Rechnung aus Abschnitt 0 [M]. Martynenko Gl. (7) (2 m_e M^2)^(1/3) passt dazu
  nicht; ihre Gl. (9) folgt konsistent aus (7), also kein Lesefehler meinerseits. Offen bleibt, ob dort eine andere
  Groesse gemeint ist (R1 bleibt als Frage stehen, nicht als Befund).
- JLM Z. 498-500 [S-lokal]: "there is no threshold if eta <= xi <= 0", "no threshold in the case of equal negative
  parameters". Und Z. 455-458: Energieverlust dE/dt ~ alpha E^2 oberhalb der Schwelle; die Schwelle muss ueber der
  hoechsten beobachteten Energie geladener Teilchen liegen.
- [M] Finns Netz an der LHAASO-Grenze (M = 6,9e11 GeV), Elektronen Lorentz-invariant: p_th = 1,61 sqrt(5,11e-4 *
  6,9e11) GeV = 1,61 * 1,88e4 GeV = 3,0e4 GeV = 30 TeV. Elektronen oberhalb davon gibt es [L: H.E.S.S.-Elektronenspektrum
  bis ~40 TeV; Crab-IC bis 1 PeV verlangt PeV-Elektronen]. Fuer p_th > 2 PeV: M > (2e6/1,61)^2/5,11e-4 GeV = 3,0e15 GeV
  -> l < 7,0e-28 m * 6,9e11/3,0e15 = 1,6e-31 m (~1e4 l_P). **Bedingt** auf Lorentz-invariante Elektronen [H].
  Sind die Elektronen mindestens so subluminal wie das Licht (eta <= xi < 0), entfaellt die Schranke ganz.
  [ES, Feldregel 6] Die Stellgroesse ist die Differenz der Sektoren, nicht das Photon allein.

### F6 arXiv-API, 24-Monats-Fenster (Feldregel 7), andere Wortwahl (Erwartung geschrieben 22:33)

- Anfrage: (abs:anisotropic OR abs:anisotropy OR abs:"direction-dependent" OR abs:"Standard-Model Extension" OR abs:SME)
  AND abs:Lorentz AND (abs:photon OR abs:photons OR abs:"gamma-ray" OR abs:"gamma rays"), eingereicht 2024-10-01 bis
  2026-10-04, neueste zuerst, bis 100.
- **Erwartung:** Guerrero u. a. 2025 erscheint (Positivkontrolle). Dazu 0 bis 3 Arbeiten zu richtungsabhaengiger
  d = 6-Dispersion (z. B. LHAASO- oder CTAO-Mehrquellen-Studie), **keine** mit einem Richtungssignal, keine, die ein
  kubisches Muster mit fester l = 4/l = 0-Kopplung testet (85 %).
- **Ausgang F6 (22:33:15 abgerufen; quellen/F6-arxiv-api-24monate.xml, 19 Treffer):** Erwartung getroffen.
  - Positivkontrolle: Guerrero u. a. 2508.02883 erscheint.
  - Einschlaegig neu: Xiao, Z.; Song, H.; Ma, B.-Q. (2026), arXiv 2602.01243 [S Abstract]: 14 GRB-Photonen im GeV-Band,
    nur **isotrop** c^(d)_(I)00, d = 6, 8, 10; "our analysis indicates a preference for subluminal LV effects";
    95 % glaubwuerdig abs(c^(6)_(I)00) <= 7,75e-20 GeV^-2. [M] Fuer Finns Netz verlangt LHAASO c00 = (sqrt(pi)/5) l^2 <
    0,3545 * 12 * 1,05e-24 = 4,5e-24 GeV^-2; ein Wert um 1e-20 waere damit um 4 Groessenordnungen unvereinbar.
  - Sonst ohne Belang (Wurmloecher, Torsion, CMB-SME, Bumblebee, klassische Lagrange-Funktionen, Metamaterial).
  - **Feldregel 7 erfuellt:** Okt. 2024 bis Okt. 2026 keine Richtungsdetektion, kein Test eines kubischen Musters mit
    fester l = 4/l = 0-Kopplung. Urteil zu KA3 also "nach Recherchestand nicht trennbar", mit Wortwahl-Grenze.

### F7 arXiv-API Gegensweep: Gitter-Raumzeit mit kubischer Symmetrie (Erwartung geschrieben 22:33)

- Anfrage: ("cubic lattice" OR "spacetime lattice" OR "space-time lattice" OR "discrete spacetime" OR "discrete
  space-time" OR "cubic symmetry" OR "lattice spacing") AND ("Lorentz violation" OR "Lorentz invariance" OR "Lorentz
  symmetry") AND (photon OR photons OR "gamma-ray" OR "cosmic ray(s)" OR dispersion), nach Relevanz, 60.
- **Erwartung:** Beane/Davoudi/Savage und wenige Folgearbeiten (Gitter-Dispersion, kosmische Strahlung, Abbruch des
  Spektrums). **Keine** Arbeit, die ein kubisches Muster in Photonen-Laufzeiten aus mehreren Richtungen gegen
  isotrop prueft (80 %). Vielleicht ein Satz der Art "ein festes Gitter erzeugt O(1)-Lorentzverletzung in Dimension 4
  ueber Schleifen" (Collins u. a. 2004, Polchinski) als staerkstes Gegenargument.
- **Ausgang F7 (22:33:56 abgerufen; quellen/F7-arxiv-api-gitter-kubisch.xml, nur 4 Treffer):**
  - Erwartung "kein Photonen-Laufzeittest eines kubischen Musters" getroffen. Beane u. a. fehlt (Abstract ohne
    "Lorentz"), Anfrage also zu eng (Selbstanzeige).
  - **Verstoss 5 (klein, Gegensweep):** Brun, T. A.; Mlodinow, L. (2019), PRD 99, 015012, arXiv 1802.03911 [S Abstract]:
    Richtungsabhaengige Dispersion eines 3D-Quantenlaufs auf dem kubisch-raumzentrierten Gitter (Dirac im Kontinuum)
    gibt "a surprisingly large phase shift between the two arms of an asymmetrical interferometer"; "This method could
    be employed to test any model that predicts a direction-dependent dispersion relation"; ein Neutronen-
    Interferometer "could put strong bounds on the size of the lattice spacing", skaliert evtl. bis zur Planck-Laenge.
    Also: Ein Labortest fuer kubische Richtungsabhaengigkeit existiert, aber fuer massive Fermionen, nicht fuer Licht.
  - Sonst: Calcagni 2017 (multifraktal, GW-Tempo), Iorio u. a. 2018 (Graphen als Analogon), Philpott 2010 (Kausalmengen:
    Diffusion statt Richtungsmuster) [S Abstract].

### F8 arXiv-API: Vakuum-Cherenkov bei quadratischer (subluminaler) Photon-Dispersion (Erwartung geschrieben 22:35)

- Anfrage: ("vacuum Cherenkov" OR "vacuum Cerenkov" OR "Cherenkov radiation in vacuum") AND (subluminal OR quadratic OR
  "dimension-six" OR "dimension six") AND (photon OR photons OR electron OR electrons), nach Relevanz, 40.
- **Erwartung:** Die Literatur behandelt vor allem superluminale Elektronen (Crab: M_e > 2e16 GeV, wie Martynenko
  Gl. (10) [S-lokal]). Eine ausdrueckliche Schranke fuer subluminales Licht der Dimension 6 mit Lorentz-invarianten
  Elektronen aus Crab-/Elektronendaten: gefunden 40 %, nicht gefunden 60 %.
- **Ausgang F8 (22:34:38 abgerufen; quellen/F8-arxiv-api-vakuum-cherenkov.xml, 2 Treffer):** zwischen den beiden
  Erwartungsarmen.
  - Li, C.; Ma, B.-Q. (2025), JHEP 10 (2025) 216, arXiv 2505.06121 [S Abstract]: Schranken aus dem Fehlen von
    Vakuum-Cherenkov ultrahochenergetischer Elektronen im Crab (LHAASO) seien in PLB 829 (2022) 137034, PLB 835 (2022)
    137536, PRD 108 (2023) 063006 hergeleitet; "the rates of this vacuum process are substantial such that one is
    justified in deriving bounds ... from simple threshold analysis"; in D-Schaum-Modellen mit subluminalem Licht werden
    sie umgangen: Elektronen strahlen dort "not ... despite moving faster than photons". -> Den Satz gibt es in der
    Literatur, die Zahl fuer quadratisches subluminales Licht habe ich nicht gelesen (O2).
  - Schreck 2017, 1702.03171 [S Abstract]: Vakuum-Cherenkov fuer Lorentz-verletzende Fermionen (minimales SME), nicht
    unser Fall.
- **Abrufe: 8 von 8 verbraucht. Ab hier nur lokale Dateien.**

## 4. Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | geprueft? | Ausgang |
|---|---|---|---|
| G1 | Finns Maxwell-Netz ist in jeder Richtung subluminal | ja [P] | ERGEBNIS Z. 92: a2 = -1/12 bis -1/9, alle < 0. Darum zaehlen HAWC und Photonzerfall (nur superluminal) nicht |
| G2 | LHAASO-E_QG,2 und SME-Koeffizient haengen ueber 1/(2 E^2) zusammen | ja [S] | Guerrero Gl. (28) Z. 353 (Layout): s+-/(2 E_QG,d-4^(d-4)) -> sum Y_jm c^(d)_(I)jm; Gruppentempo mit (d - 3) (Gl. 25) wie Wei 2022 Z. 209. Meine Umrechnung 1,05e-24 GeV^-2 stimmt |
| G3 | Kubische Symmetrie verbietet Doppelbrechung bei k^2 | ja, per Rechnung [M], Physik [L] | Nein: In kubischen Kristallen gibt es k^2-Doppelbrechung laengs [110] (CaF2 bei 157 nm, Burnett u. a. 2001 [L]). Bei Finns Netz fehlt sie numerisch (~1e-10 [P]). Mit l = 7e-28 m waere der Rest <= 1e-10 * 1,26e-23 = 1,3e-33 GeV^-2, unter den d = 6-Doppelbrechungswerten 1e-31 bis 1e-32 (D22 Teil 7 [S]). Also heute nicht bindend, aber eine Netz-Eigenschaft, keine Symmetriefolge |
| G4 | Die (k l)^2-Entwicklung gilt bei TeV | ja [M] | k l = 1e4 GeV * 3,55e-12 GeV^-1 = 3,5e-8; a4-Glied relativ ~1e-15 |
| G5 | Die Projektanker LHAASO und Martynenko stehen in der SME-Sammlung | ja [S] | Nein, beide fehlen in Data Tables v19 (Verstoss 4) |
| G6 | Netz ruht im Sonnensystem-Rahmen | nein | Bewegung ~1,2e-3 c gegen die Hintergrundstrahlung [L] mischt ungerade j mit relativ ~1e-3 ein [ES]; fuer Groessenordnungen ohne Belang |
| G7 | Die Elektronen des Netzes sind Lorentz-invariant (oder gleich langsam) | nein [H] | entscheidet ueber Vakuum-Cherenkov (R1, O2): l < ~1,6e-31 m oder gar nichts |

## 5. Rechnungen nach den Abrufen [M, von Hand, ungeprueft]

- **l = 4 allein, Guerrero 2025 (95-%-Intervalle je Koeffizient, Kasten):** groesster Betrag je Koeffizient (e-15):
  c40 2,0; Re/Im c41 0,7/1,0; Re/Im c42 1,0/1,0; Re/Im c43 0,6/0,6; Re/Im c44 0,7/0,9.
  N4^2 = c40^2 + 2 sum_(m=1..4)(Re^2 + Im^2) <= 4,0 + 2 * 5,51 = 15,02 -> N4 <= 3,88e-15 GeV^-2.
  Finn: N4 = 0,025785 l^2 -> l^2 < 1,503e-13 GeV^-2 -> l < 3,88e-7 GeV^-1 = **7,7e-23 m**. Der Kasten ist grosszuegig (alle
  neun zugleich am Rand; jede Ausrichtung, die in den Kasten passt, hat kleineres N4) -> gueltige, schwache Schranke.
- Gleiche Daten, isotroper Weg: c00 < 2,4e-15 -> l^2 < 2,4e-15/0,35449 = 6,77e-15 -> l < 1,6e-23 m.
- Kislat/Krawczynski 2015 (Intervalle laut Tabelle, Niveau nicht gelesen): N4 <= 9,84e-14 -> l < 3,9e-22 m.
- Vergleich LHAASO-Sichtlinie (Netz-Weg, konservativ 1/12): 7,0e-28 m. Der l = 4-Weg ist rund 1e5-mal schwaecher.
- **Allrichtungs-Satz fuer das Netz [M]:** Sichtlinien-Koeffizient C(n) = abs(a2(n)) l^2 liegt zwischen l^2/12 und l^2/9.
  Eine Sichtlinien-Schranke X gilt damit in jeder Richtung als <= (4/3) X. LHAASO: C(n) <= 1,4e-24 GeV^-2 ueberall.
  Nominelle Signale: MAGIC Mrk 501 3e-22 (Faktor ~200 darueber), Agrawal 6,3e-15, GBM-GRB 1e-15 bis 1e-11 (9 bis 13
  Groessenordnungen) -> im Netzmodell unvereinbar mit LHAASO.
- **Verhaeltnis l = 4 zu l = 0 als Kennung [M aus P-Formeln ERGEBNIS Z. 107-110]:** c40/c00 im Netzrahmen: Maxwell auf
  Finns Netz -1/18; Skalar Diamant -4/27; Grover -1/3; Wuerfel Z3 (Skalar, Yee) +2/9. Vorzeichen: Finns Netz hat die
  Achsen am schnellsten, der Wuerfel am langsamsten.
- **Trennung kubisch gegen isotrop [M, grob]:** Relativer l = 4-Anteil RMS 0,0727 (Spitze +1/6, Tal -1/9). N Quellen in
  zufaelligen Richtungen mit relativem Fehler s je Quelle: Delta chi^2 ~ 0,00529 N/s^2; fuer ~3 sigma plus drei
  Winkel (Delta chi^2 ~ 12): N ~ 2270 s^2 -> s = 10 %: ~23 Quellen; s = 5 %: ~6; s = 20 %: ~90. Jede Quelle braucht dafuer
  einen Nachweis (nicht nur eine Schranke) mit ~10 sigma.
- **Vakuum-Cherenkov [M nach JLM Gl. (15) S-lokal]:** p_th = (27/4)^(1/4) sqrt(m_e M) = 1,61 sqrt(m_e M); an der LHAASO-
  Grenze 30 TeV; mit 2-PeV-Elektronen [L] M > 3,0e15 GeV, l < 1,6e-31 m; mit 40-TeV-Elektronen [L] nur M > 1,2e12 GeV,
  l < 4,0e-28 m. Nur bei Lorentz-invarianten (oder weniger subluminalen) Elektronen.

## 9. Offene Rueckfragen (wandern mit)

- R1 Martynenko Gl. (7) gegen JLM Gl. (15): JLM und meine Rechnung stimmen ueberein (1,61 sqrt(m_e M)); Martynenko gibt
  (2 m_e M^2)^(1/3). **offen** (nicht geklaert, ob dort etwas anderes gemeint ist).
- R2 Kostelecky/Mewes 2008 "some support at one sigma ... for anisotropic violation": zu welchem d? **offen** (Volltext
  nicht abgerufen; Data Tables D22 Teil 5 zeigt fuer Mrk 501 einen von null verschiedenen d = 6-Wert 3 +1/-2 e-22 ueber
  [231], [18]*; Zusammenhang [H]).
- R3 Zweite 24-Monats-Anfrage: **erledigt** (F6).
- R4 HAWC nur superluminal: **erledigt** laut Abstract; die Betragsschreibweise der Tabellen bleibt eine Vereinfachung [ES].
- R5 Niveau der Data-Tables-Zahlen: **erledigt** (Erwartungswert +- 1 Standardabweichung; 95-%-Grenzen in Guerrero
  Tab. II).
- O2 Zahl der Crab-Vakuum-Cherenkov-Schranke fuer quadratisch subluminales Licht (Li/Ma 2022, 2023): **offen**.

## 10. Berichtigungen (nichts geloescht)

- Zeitangaben der Erwartungen nachgeprueft an den date-Ausgaben derselben Befehle: F4-Erwartung geschrieben **22:29:09**
  (im Kopf steht faelschlich "22:3x"); F8-Erwartung geschrieben **22:34:38** (im Kopf steht gerundet "22:35"). Die
  Reihenfolge Erwartung vor Abruf gilt in allen acht Faellen (Anhaengen und curl im selben Befehl, Anhaengen zuerst).
- Abschnitt 0, R1 "Nicht geklaert" ist durch Abschnitt "R1 geklaert an lokaler Quelle" und Abschnitt 9 ueberholt
  (Rechnung bestaetigt, Widerspruch zu Martynenko Gl. (7) offen).
- Dossier ab 22:39 (date folgt in DOSSIER.md).
- Zeilennummern nachgeprueft (grep -n, ~~22:44~~ vor 22:42:02 laut date): Guerrero LHAASO-Vorbehalt Z. 1999-2008 (oben "1999-2005"), "none of the
  most sensitive analyses" Z. 2014, "expand the sample ... different distances and of different origins" Z. 2008-2010;
  Wei 2022 "(d - 1)^2 sources distributed evenly" Z. 113-114, "not feasible" Z. 2349. Im Dossier entsprechend.
- Dossier fertig, letzte Aenderung vor 22:42:52 CEST (date). Danach keine Abrufe mehr.
- Berichtigung zu F3 ("Erwartung korrigiert"): Dort steht "9 bis 10 Groessenordnungen schwaecher als die besten
  Sichtlinien (1e-22) und 15 schwaecher als HAWC". Richtig [M]: j = 4-Grenzen (0,6 bis 2,0)e-15 gegen 1e-22 (H.E.S.S.,
  Vasileiou) sind ~7 Groessenordnungen, gegen LHAASO 1,05e-24 ~9, gegen HAWC 3,5e-31 ~15 bis 16. Im Dossier gilt "rund 9"
  (gegen LHAASO).
