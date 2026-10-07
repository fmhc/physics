# SKALAR-SEKTOR-L: Arbeitsfeld (feldforscher fuer claude-primary)

- Start 2026-10-05 08:29:12 CEST (date). Zeitbox 75 min, also bis 09:44:12 CEST. Hoechstens 15 Netzabrufe.
- Karte gelesen ~~08:29~~ nach 08:29:12 per date (KARTE.md, unveraendert). SS1 bis SS5 und Bedeutungen bleiben wie auf der Karte.
- Dieses Feld wird vor jedem Schritt neu gelesen. Gestrichenes bleibt stehen (~~so~~), offene Rueckfragen wandern mit.

## A. Projektbefunde (Lesen, vor der Literatur)

### A1 IMPULS-NETZ-1 (ERGEBNIS.md, Abschnitte 2, 4, 5, 6) [P]
- Impulsregel M^H p = J ist erster Klasse: d/dt(M^H p) = -kappa_g M^H B a = 0 wegen B M = 0; vertauscht mit dem skalaren Paar,
  weil c^H M = 0 (4.1). Die skalare Regel bleibt zweiter Klasse (TT-ISO-1, GAMMA-NETZ-L zitiert).
- Kopplung -nu^H J (Shift mal Impulsdichte, wie N_i H^i), widerspruchsfrei genau dann, wenn J' = -M^H sigma (4.1).
- Bewegungsenergie je Tetraeder ist eine DeWitt-Form G(X,Y) = X:Y - (1/2) trX trY (4.2) -- also lambda = 1 im
  DeWitt-Sinn (Horava-Sprache!) [ES, zu pruefen: der Spurkoeffizient 1/2 in 3D entspricht lambda = 1].
- Mitfuehrung (quer, gravitomagnetisch) einsteinsch auf 1,3e-5 mit J_iso (5.4).
- **Laengsanteil k^T Q k negativ** (-0,559 im Mittel, J_iso), anisotrop, Quer-Laengs-Kopplung bis 6,6 % (5.4): "deutet an, dass
  der Laengsimpuls die negative Spur-Richtung der DeWitt-Form erreicht" [ES dort].
- Kreisbahnen (kompakt, J_iso): G_rad/G = 1 + 0,004077 (0,6331 - Summe m_i^4), Bereich -0,15 % bis +0,12 % (5.2). Ohne V1-Kanal.
  J = 1: umgekehrter Gang (+0,33 % bis -0,16 %). V1 verschiebt phi-Quelle um bis 0,9 %.
- Doppelpulsar 1,3e-4 (Kramer u. a. 2021, PRX 11, 041050) [P aus PUMPE-NETZ-1]. Groesste Abweichung 12-mal darueber.
- 6: alpha_1, alpha_2 offen [H]. Vermutung: skalare Regel erster Klasse mit m' = -(Gitterdivergenz J).
- Lageabhaengigkeit (Summe m_i^4 der Bahnnormale) ist **Anisotropie gegen das Gitter**, also gegen Raumrichtungen im
  Netzsystem. Das ist kein Skalar-Monopol/Dipol im ueblichen Sinn, sondern eine Verletzung der Rotationsinvarianz
  (Achsen des Gitters). [ES] -> fuer SS3 wichtig: Was entspricht das in der Kontinuums-Sprache? Kubische Anisotropie
  (Summe m_i^4 ist die kubische Invariante 4. Stufe) hat in Horava/Khronon (isotrop) kein Gegenstueck. Pruefen.

### A2 TAKT-UMBENENNUNG-L (DOSSIER.md ~~gelesen 08:31~~ gelesen zwischen 08:29:27 und 08:37:12 per date, Abschn. 1-14) [P]
- Konvention: Kinetik K_ij K^ij - lambda K^2; Impulsbild pi.pi - c pi^2, c = lambda/(3 lambda - 1); c = 1/2 <-> lambda = 1.
- Fester Takt (N = 1) = lokal projizierbares Horava (BPS 2011, S. 8, woertlich). Projizierbar: Lapse faellt aus quadr.
  Wirkung (S. 12); stabil nur |lambda - 1| <~ 1e-61 (M* >~ 0,1 eV, Gl. 3.8, S. 13), dann stark gekoppelt unter ~1e13 cm (S. 18).
  Koyama/Arroja: Geist bei c_s^2 > 0, sonst Gradienteninstabilitaet. Zwei Lager (BPS/K-A perturbativ gegen Mukohyama
  nichtperturbativ, Vainshtein-artig offen).
- Gesund (lokaler Lapse): gamma = beta = 1, xi = 0 (BPS S. 33); |alpha1| < 1e-4, |alpha2| < 4e-7 (GSS 2018 nach Will);
  GW170817 |beta_ae| <~ 1e-15 (GSS S. 3). G_N = 1/(8 pi M^2 (1 - alpha/2)) (BPS Gl. 5.30).
- 1/2 = Passbedingung: H-dot ~ (X - 1) B Y D_i(N^2 D^i p) (Anderson 2007 Gl. 26). Vier Auswege: X = 1, B = 0 (kein R),
  Y = 0, oder bevorzugte Blaetterung (Impulsspur = 0). **Letzteres = maximales Slicing!** [ES, fuer Kette K1 unten]
- Lokale Kopien ohne Abrufbudget: takt-umbenennung-l/quellen/F5-1007.3503.txt (BPS 2011 Volltext), F6 (Mukohyama Review),

### A3 PACHNER-TAKT-1 (ERGEBNIS.md 1, 2, 5, 9 ~~gelesen 08:33~~ gelesen zwischen 08:29:27 und 08:37:12 per date) [P]
- Kommutator D zweier Nachbar-Zeltzuege: flach 1e-15; mit Welle D ~ eps^1 (Steigung 0,998), Wirkung ~ eps^2,00.
  D ~ (a/L)^2,25 (L/a = 4..32), lokale Steigung 2,48 -> 2,07; bedingter Grenzwert p -> 2 [M, bedingt] (D1 ~ k^2).
- Global gleiche Zeltstangen (G) heben die Spur nicht auf: D(G)/D(L) = 1,39..1,51.
- Euklidisch, linearisiert, ein Kantenpaar, keine Drift ueber viele Takte.

### A4 TAKT-UMKLAPP-1 Abschn. 2 (~~gelesen 08:34~~ gelesen zwischen 08:33:43 und 08:37:12 per date) [P]
- "Finns Takt-Operator" P = -W^H B W = 8 d0^H *1 d0 (umkreisbasierter Hodge-Laplace auf Ecken), exakt je Tetraeder.
  W = Eck-Skalierung. P ist also der konforme Block der Regge-Steifigkeit (Glickenstein). Takt instabil, sobald P indefinit.
- Lesart [ES]: Der "Takt" ist die Eckvariable des skalaren Sektors (Lapse bzw. Eck-Skalierung mu); P ist der Operator
  der Takt-Gleichung (GAMMA-NETZ-L: (d_i d_j - delta_ij Lap) N = 0 im Kontinuum; statisch a = -(kappa'/kappa_g) W mu).

### A5 GAMMA-NETZ-L, EINE-WELT-LOCH-1 (grep, ~~gelesen 08:35~~ gelesen zwischen 08:29:27 und 08:37:12 per date) [P]
- Skalare Regel je Ecke v: c_v = -B w_v, c_v.a = Summe_{e an v} l_e delta eps_e = eckweise linearisierte Skalarkruemmung
  delta R^(3) (GAMMA-NETZ-L 1.1; EINE-WELT-LOCH-1 Z. 99-100).
- Paar zweiter Klasse: auf a Hamilton-Bedingung (ohne Quelle), auf p c^H p = 0 = im Kontinuum d_i d_j pi_ij - Lap pi = 0,
  mit Impulsbedingung tr pi = 0: **maximales Slicing** (GAMMA-NETZ-L Z. 104-111). Zweiter Klasse, weil A c_v nicht in
  Bild M (Spur-Eichdefekt Median 0,91 flach, L = 16). "Weder reine Hamilton-Bedingung noch reine Eichfixierung".
- "ohne Quelle, ohne Takt": In ew.py steht kein Lapse-Multiplikator in der Dynamik (GAMMA-NETZ-L 1.1).
- Regime-Tabelle GAMMA-NETZ-L 6.1: H (Hamilton-Gitter, ew.py, zweiter Klasse) / K (kov. 4D-Regge, Zeltstange = exakte
  Eichung flach) / Q (Quanten-Regge) / P (globaler Takt, projizierbar).
- EINE-WELT-LOCH-1: V-Fuellung: langwellig genau 2 masselose Moden, reine TT (TT-Anteil 1,000); 26 Zusatzmoden mit
  Luecke (omega^2 >= 3,43). B hat bei kleinem k so viele negative Richtungen wie Ecken (konformer Modus), nach den
  Regeln keine.
- **Folge [ES]: Auf der Zwangsflaeche gibt es KEINEN masselosen Skalar.** Ein "Zusatzskalar", der strahlt, existiert im
  Netz langwellig nicht. Die Leckage muss also in die zwei TT-Moden gehen (falsche Kopplung), nicht in einen dritten Kanal.

### A6 GEMEINSAMES-NETZ-v3 (~~gelesen 08:32~~ gelesen zwischen 08:29:27 und 08:37:12 per date) [P]
- L1: offen; skalare Regel auf dem gefuellten Netz auch langwellig nicht erster Klasse: Spur-Eichdefekt zwischen
  |k| = 0,1 und 0,001 konstant (Median 0,90; isotrop abgestimmte Gewichte 0,76 bis 0,84); ohne Fuellung -> 0 mit |k|
  (linear Achsen, quadratisch Flaechendiagonalen) (TT-ISO-1, TENSOR-EIS-PYRO-1).
- L8: Verstecktes Ruhesystem; Licht-Schranken l < 7,0e-28 m bzw. 6,1e-28 m (LICHT-FINN-NETZ-1); alpha1, alpha2 nicht
  untersucht (GAMMA-NETZ-L O5).
- Takt-Zeile: Flip-Flop nur mit mitrueckenden Ecken; 1/2 Passbedingung; Raum-Netz mit aeusserer Uhr 1/5 [M].

### A7 Codex-Ideation 2 (~~gelesen 08:36~~ gelesen zwischen 08:33:43 und 08:37:12 per date) [P, nur gelesen]
- Rang 1: Gegenseitigkeit (gemischte Ableitungen gleich), Integrabilitaetstest. Karte: im Vektor-Sektor durch
  IMPULS-NETZ-1 erfuellt (-nu^H J).
- Rang 8: Bindungsenergie: Quellenmonopol und traege Schwerpunktsantwort zweier Praeparationen desselben Verbunds;
  "Spaeter Aequivalenzprinzip; hier keine neue numerische Messschranke".

## B. Ketten (Bausteine verkettet)

- **K1 (Einordnung des Netz-Skalarsektors) [ES aus P + S]:** GAMMA-NETZ-L: Paar = (delta R^(3) = 0 je Ecke) + (tr pi = 0,
  maximales Slicing), zweiter Klasse. Anderson Gl. 26: Ohne Passung (X != 1) erhaelt sich H nur mit Impulsspur = 0,
  also genau mit diesem Paar. => Das Netz entspricht im Kontinuum dem **nicht projizierbaren Horava ohne a_i-Terme
  (lambda-R-Modell) mit K = 0 als Folgebedingung**, nicht dem projizierbaren und nicht der gesunden Erweiterung.
  Zu pruefen an der Quelle: Was sagt die Literatur zum lambda-R-Modell (Freiheitsgrade, Aequivalenz zu ART im
  maximalen Slicing)? [Erwartung: Bellorin/Restuccia; Loll/Pires 2014: 2 Freiheitsgrade, ART-aequivalent]
- **K2 (Kein masseloser Zusatzskalar im Netz) [ES aus P]:** EINE-WELT-LOCH-1: langwellig nur 2 masselose reine TT-Moden,
  alles andere gegappt. IMPULS-NETZ-1 5.2: "nur TT-Anteil" isotrop auf 1,8e-6; der Gang liegt im nn-Teil der Kopplung.
  => Die Leckage ist keine Abstrahlung eines Zusatzskalars, sondern eine falsche (kubisch anisotrope) Kopplung der
  Materiespannung an die TT-Moden ueber nicht-TT-Anteile von e_j = (1 - P_c) A p_j. Betrifft SS3.
- **K3 (Kubische Anisotropie hat kein Horava-Gegenstueck) [M]:** G_rad/G - 1 = 0,004077 (0,6331 - Summe m_i^4).
  Richtungsmittel <Summe m_i^4> = 3 <m_z^4> = 3/5 => isotroper Teil +0,004077 x 0,0331 = +1,35e-4; Rest ist reine
  l = 4-Anisotropie (kubische Harmonische). Horava/Khronon/Aether sind im Vorzugssystem isotrop; ihre Strahlungsformeln
  haengen nicht von der Bahnlage gegen Achsen ab. => Nur der isotrope Teil (1,35e-4, knapp an 1,3e-4!) ist einem
  Skalar-Term zuordenbar, der anisotrope (bis -1,5e-3/+1,2e-3) nicht.
- **K4 (PACHNER-TAKT-1 fuer Daten unerheblich) [ES]:** D ~ eps (a/L)^~2 verschwindet mit a/L -> 0. Fuer a ~ l_P und
  L ~ GW-Wellenlaenge des Doppelpulsars (P_b = 2,45 h -> P_GW ~ 1,2 h -> lambda ~ 1,3e12 m): (a/L)^2 ~ 1e-94.
  Dagegen ist die IMPULS-NETZ-1-Leckage langwellig konstant (5.1 "Gang mit kl ... langwellig konstant"). Zwei Regime:
  K (4D-Regge, Zeltstangen) wird asymptotisch erster Klasse; H (ew.py, gefuellt) bleibt langwellig zweiter Klasse.
- **K5 (Kopplungsgroesse, Regel 6) [H]:** Vier Wege zur Leckage: nn-Kopplung (haengt an Bewegungsgewichten, J = 1 kehrt
  den Gang um), V1 (Kontinuums- statt Gittererhaltung), Quer-Laengs-Kopplung 6,6 % (im Kontinuum null), Spur-Eichdefekt
  0,90 langwellig konstant. Gemeinsame Groesse: die langwellige Bewegungsenergie A_eff des gefuellten Netzes (effektive
  DeWitt-Form) und ob A c_v in Bild M liegt. Nicht die Klasse der Regel an sich.

## C. Erwartungen vor Abruf und Ergebnis (Regel 3)

Lokale Lesungen (kein Netzabruf, Erwartung trotzdem vorab):
- **LL1 08:38:03 GSS 2018 lokal (1711.08845):** Erwartung: Nach GW170817 beta <~ 1e-15; mit alpha1/alpha2 (Sonnensystem)
  folgt alpha <~ 1e-5 bzw. alpha ~ 0; lambda bleibt nur kosmologisch (BBN) begrenzt, |lambda - 1| <~ 0,1. Bei
  alpha = beta = 0 Skalartempo unendlich (instantan). Binaerpulsar-Schranken muessen neu gerechnet werden.
- **LL2 08:38:03 BPS 2011 lokal (1007.3503):** Erwartung: gesunde Erweiterung: N(t,x), a_i-Term; Skalar mit
  c_s^2 ~ (lambda - 1)/alpha-artig; alpha1 = 4(alpha - 2 beta)/(beta - 1), alpha2 = ... ; Zwangsbedingungen
  zweiter Klasse steht dort evtl. nicht (eher bei Donnelly/Jacobson 2011, Kluson 2010).
- **LL3 08:38:03 Will 2014 lokal:** Erwartung: Tabelle der PPN-Schranken: alpha1 < 1e-4 (LLR) und 4e-5 (PSR J1738),
  alpha2 < 4e-7 (Sonnenspin) und 2e-9 (Pulsare), Nordtvedt eta < 4,4e-4 bzw. ~1e-4 (LLR), GW-Abschnitt ohne GW170817.
- **LL1 Ergebnis (08:39):** bestaetigt, eine Zeile: GSS 2018 Gl. (11) |alpha1| < 1e-4, |alpha2| < 4e-7 (nach Will);
  Gl. (13) -3e-15 <= c_T - 1 <= 7e-16 -> |beta| <~ 1e-15 (14); BBN Gl. (10) |(alpha + 3 gamma + beta)/(2 + 3 gamma + beta)|
  < 1/8; c_S^2 = (2 - alpha)(gamma + beta)/(alpha (1 - beta)(2 + 3 gamma + beta)) (4); "speed of the scalar polarisation
  remains virtually unconstrained"; lambda = (1 + gamma)/(1 - beta), eta = alpha/(1 - beta) (3). **Teil-Verstoss:**
  Binaerpulsar-Schranken dort nur fuer die alpha = 2 beta-Ebene (Ref. [35]), "no longer well motivated"; der GR-Limes
  "is not smooth". Projizierbar: "renormalizable beyond power-counting", aber "infrared viability issues [16-22]".
- **LL2 Ergebnis (~~08:40~~ nach 08:39:16 per date):** BPS 2011 S. 35: gesundes Modell: H = dS/dN und pi_N = 0 "form a second class pair"; Lapse ist
  dort kein Lagrange-Multiplikator; "instantaneous interactions" (Abschn. 5.3). Das urspruengliche nicht projizierbare
  Modell (ohne a_i) nennt BPS pathologisch (Refs. [21, 22, 12, 23, 24], darunter Henneaux u. a. 2010). Bestaetigt.

Netzabrufe:
- **F1 08:39:16 Loll/Pires 2014 (arXiv:1407.1259, Abstract):** Erwartung: lambda-R-Modell (nicht projizierbar, nur
  K_ij K^ij - lambda K^2 + R) hat zwei lokale Freiheitsgrade wie ART; Folgebedingung pi = 0 (maximales Slicing);
  klassisch aequivalent zu ART in dieser Eichung; lambda physikalisch ohne Folge.
- **F2 08:39:16 Franchini/Herrero-Valea/Barausse 2021 (arXiv:2103.00929, Abstract):** Erwartung: Fuer alpha = beta = 0
  sind ART-Loesungen mit maximaler Blaetterung (K = 0) auch Loesungen der khronometrischen Theorie; daher Doppelsterne
  und Schwarze Loecher wie in der ART.
- **F3 08:39:16 Barausse 2019 (arXiv:1907.05958, Abstract):** Erwartung: Neutronenstern-Empfindlichkeiten verschwinden im
  nach GW170817 erlaubten Bereich (alpha = beta = 0) -> keine Dipolstrahlung, Binaerpulsar-Schranken erfuellt.
- **F1 Ergebnis (08:40:22): bestaetigt.** Loll/Pires 2014 Abstract: "all non-projectable lambda-R models are equivalent to
  general relativity in the asymptotically flat case" (nach Bellorin/Restuccia); geschlossene Raeume: tertiaere Bedingung
  allgemeiner. Giulini/Kiefer (kosmologisch) gehoert in den projizierbaren Sektor.
- **F3 Ergebnis (08:40:22): bestaetigt.** Barausse 2019: Empfindlichkeiten "vanish identically" fuer alpha = beta = 0,
  lambda beliebig; keine SEP-Verletzung (konservativ und in GW-Fluessen) in fuehrender PN-Ordnung; Pulsare und
  Interferometer "unlikely to further constrain lambda". 0 <= lambda <~ 0,01-0,1.
- **F2 Ergebnis (08:40:22): VERSTOSS.** Erwartet: ART-Loesungen mit K = 0 sind Loesungen. Abstract sagt: "a canonical
  constraint analysis shows that the class ... (alpha = beta = 0 and lambda != 0) cannot be equivalent to General
  Relativity, even in vacuum", aber Sonnensystem, Binaerpulsare und GW-Erzeugung zeigen "perfect agreement". Dazu:
  regulaere Schwarze Loecher verlangen alpha = beta = 0 exakt.
  - **Widerspruch zu F1** (Bellorin/Restuccia: aequivalent). Regel 1: zwei Regime? Moderator-Kandidaten:
    (a) Aequivalenz der Loesungsmengen in fester Blaetterung (K = 0) gegen Gleichheit der Theorien samt Khronon-
    Anfangsdaten; (b) Randbedingungen (asymptotisch flach gegen allgemein); (c) Vakuum gegen mit Materie;
    (d) Stueckelberg-Formulierung (Khronon als Feld) gegen Einheitseichung (lambda-R).
  - Korrigierte Erwartung: "Ununterscheidbar in den gerechneten Tests (PN-Ordnung), aber nicht dieselbe Theorie."
  - Naechster Schritt: Volltext F2 an der Stelle der kanonischen Analyse lesen (F4).
- **F4 08:40:45 Franchini u. a. 2021 Volltext (arXiv PDF 2103.00929), nach "canonical", "maximal", "K = 0",
  "Bellorin", "instantaneous", "degrees of freedom":** Erwartung: Sie zeigen, dass die alpha = beta = 0-Theorie einen
  zusaetzlichen (instantanen) Skalar-Freiheitsgrad bzw. eine Bedingung K = 0 als Folge hat; ART-Loesungen mit
  maximalem Slicing loesen die Theorie; Unterschied zeigt sich erst innerhalb von Horizonten (universeller Horizont) oder
  bei Randbedingungen. Moderator: Lapse-Randbedingung bzw. Existenz einer K = 0-Blaetterung.
- **F4 Ergebnis (08:41:04; Text quellen/F4-2103.00929.txt): Erwartung im Kern bestaetigt, Moderator gefunden.**
  - S. 2 [S]: mHG := alpha = beta = 0, lambda != 0. "all non-cosmological observables that have been computed in Horava
    gravity reduce to their GR counterparts in the mHG case": 1PN exakt ART, GW mit c, Sterne und Schwarze Loecher
    (ruhend und langsam bewegt) mit ART-Geometrie; Khronon nicht trivial, "does not backreact on the geometry".
  - S. 2: Nach GW170817 |beta| <~ 1e-15; mit Sonnensystem |alpha| <~ 1e-7 (lambda frei) oder |alpha| <~ 0,25e-4 mit
    lambda ~ alpha/(1 - 2 alpha); BBN lambda <~ 0,1; lambda >= 0 gegen Geister. (Hier lambda = Abweichung von 1.)
  - S. 2: Zwei Lager: Loll/Pires 2014 und Bellorin/Restuccia 2012 (aequivalent, Vakuum, asymptotisch flach) gegen
    Henneaux/Kleinschmidt/Lucena Gomez 2010 (tertiaere Bedingung geloest: nicht aequivalent, ausser N = 0).
    Volle Aequivalenz ausgeschlossen wegen anderer kosmologischer Expansion.
  - S. 7 [S]: dT H ~ lambda (...) dR K: H = 0 ist in mHG nicht von selbst eine Zwangsbedingung; Regularitaet gibt
    K = k(T); asymptotisch flache oder auslaufende Randbedingungen geben K = 0 fuer alle Zeiten; dann "identical to
    the GR ones, written in the maximal slicing gauge K = 0". Die Blaetterung ist dort physikalisch (Khronon =
    Zeitkoordinate); Grenzscheibe r = 3 G_N M/2 = universeller Horizont.
  - S. 10: "the khronon does not couple directly to matter ... at tree level"; Khronon stark gekoppelt um Minkowski,
    RW und statische Schwarze Loecher. Tests: Kosmologie und nicht asymptotisch flache Raumzeiten.
  - **Moderator (Regel 1):** Randbedingung (asymptotisch flach/auslaufend -> K = 0 -> ART) gegen kosmologisch (K != 0,
    lambda wirkt: G_C != G_N). Die zwei Lager streiten ueber die volle Theorie, nicht ueber die gerechneten Observablen.
- **Kette K6 [ES aus P + S]:** Das Netz-Paar ist (delta R^(3) = 0, tr pi = 0) [P GAMMA-NETZ-L] = lambda-R mit K = 0
  [S F1, F4]; ew.py hat keinen a_i-Term (kein Lapse in der Dynamik) -> eta = alpha = 0; TT-Tempo isotrop als c gesetzt
  -> beta = 0 relativ zu c_TT. **Das Kontinuums-Gegenstueck des Netzes ist also mHG**, und mHG sagt fuer Doppelsterne
  ART voraus (Barausse 2019: keine Dipolstrahlung; Franchini 2021). => Die IMPULS-NETZ-1-Leckage ist KEINE Folge
  des Vorzugssystems bzw. der zweiten Klasse an sich, sondern ein Gittereffekt (Bewegungsenergie A, V1-Quelle).
  Vorbehalt: beta = 0 nur relativ zum TT-Tempo; gegen Licht ist c_T/c_gamma im Netz nicht festgelegt.
- **F5 08:42:11 WebSearch (24-Monats-Front, Regel 7): "minimal Horava gravity" / khronometric constraints 2025:**
  Erwartung: Neuere Arbeiten (2024-2026) bestaetigen mHG als einzige lebensfaehige Ecke; Schranken auf lambda aus
  Kosmologie (CMB/BBN) um 0,01 bis 0,1; Arbeiten zu Kollaps/Quasinormalmoden; keine Arbeit, die mHG in Doppelsternen
  von der ART trennt.
- **F6 08:42:11 WebSearch (24-Monats-Front): projizierbares Horava im Infraroten 2024/2025:** Erwartung:
  Renormierbarkeit/asymptotische Freiheit (Barvinsky, Sibiryakov u. a.) in 3+1 ist UV-Arbeit; das IR-Problem
  (lambda -> 1, starke Kopplung bzw. Skalar-Instabilitaet) bleibt ungeloest; keine phaenomenologische Rettung.
- **F5/F6 Ergebnis (vor 08:42:41):** nur Trefferlisten (keine Quelle). Neu in 24 Monaten: arXiv:2508.03106 (mHG-
  Viabilitaet, J. Phys. A 2025), arXiv:2604.09400 (IR-Instabilitaet projizierbar "zaehmen", April 2026), arXiv:2411.13574
  (RG-Fluss projizierbar, lambda -> 1+0 im IR). Moegliche Verstoesse gegen SS1 (Rettung des projizierbaren Falls?) und
  gegen K6 (mHG doch nicht lebensfaehig?). Beide an der Quelle lesen.
- **F7 08:42:41 arXiv:2508.03106 Abstract ("On the viability of minimal Horava gravity"):** Erwartung: mHG bleibt
  lebensfaehig, aber mit einem Vorbehalt (starke Kopplung des Khronons um flachen Raum oder instantaner Modus bzw.
  Anfangswertproblem schlecht gestellt); evtl. Befund, dass mHG nicht wohlgestellt ist (Verstoss gegen K6 moeglich).
- **F8 08:42:41 arXiv:2604.09400 Abstract (projizierbar, IR-Instabilitaet):** Erwartung: Die Gradienteninstabilitaet
  des Skalars wird durch Zeit- bzw. Raumabhaengigkeit (Hintergrund, Kosmologie) gezaehmt, nur in Teilbereichen; keine
  allgemeine Rettung; Doppelpulsar/Sonnensystem nicht behandelt.
- **F9 08:42:41 arXiv:2411.13574 Abstract (RG-Fluss projizierbar):** Erwartung: Fluss von asymptotisch freiem UV-Punkt
  zu lambda -> 1+0 im IR; dort starke Kopplung des Skalars; Phaenomenologie im IR offen.
- **F8 Ergebnis (vor 08:44:00): bestaetigt.** Mukohyama/Radkovski/Sibiryakov 2026: Minkowski IR-instabil im
  projizierbaren 3+1-Fall; Rettung nur, wenn Zeitentwicklung (Hubble, Jeans) die Instabilitaet verdeckt; statische
  Endzustaende ausgeschlossen. Stuetzt SS1 (Stand April 2026), mit offenem Rettungsweg "verdeckt durch Expansion".
- **F9 Ergebnis: im Kern bestaetigt, eine Zeile.** RG-Fluss mit Fixpunkten; G verschwindet im UV und IR; schwache
  Kopplung verlangt Hierarchie zwischen LV-Skala und Planck-Masse. Zum IR-Skalar nichts im Abstract.
- **F7 Ergebnis (vor 08:44:00): VERSTOSS (staerker als erwartet).** Jacobson/Pulakkat 2025 (J. Phys. A 58, 315404):
  - mHG hat hamiltonsch einen pathologischen Modus, "unstable at high frequencies and strongly coupled at low
    frequencies". Abhilfe: Blaetter **konstanter mittlerer Kruemmung** (m2Hg).
  - m2Hg, zwei Regime: (i) mittlere Kruemmung zeitunabhaengig: "equivalent to a particular foliation of GR with nonzero
    cosmological constant"; (ii) zeitabhaengig: Lapse elliptisch, unendliches Tempo, nichtlokal anders als ART;
    Staubschalen-Kollaps: danach instantaner Kugelmodus mit unbestimmter Entwicklung, "failure of the Cauchy problem".
  - Korrigierte Erwartung: mHG ist ohne Zusatzbedingung NICHT sauber lebensfaehig (gegen Franchini 2021 und Barausse
    2019, die nur PN-Observablen rechneten). Moderator (Regel 1): perturbativ/PN-Observablen (wie ART) gegen
    hamiltonsche Vollanalyse (Zusatzmodus, Cauchy-Problem).
  - **Kette K7 [ES aus P + S]:** Unser Netz setzt mit c^H p = 0 je Ecke genau K = 0 (GAMMA-NETZ-L), also eine
    Blaetterung konstanter (null) mittlerer Kruemmung, zeitunabhaengig = Regime (i) von m2Hg mit k = 0. Damit ist die
    von Hand gesetzte zweite Klasse **genau die Zusatzbedingung, die Jacobson/Pulakkat zur Rettung von mHG verlangen**.
    Ob Regime (i) mit k = 0 ART ohne Lambda ist: aus dem Abstract nicht ablesbar ("nonzero cosmological constant").
    Offene Rueckfrage Q2 (unten).
  - Achtung Kalibrierung: Meine Sicherheit, dass das Netz "im Kontinuum ART im maximalen Slicing" ist, steigt, waehrend
    die Literatur gerade sagt: es kommt auf Randbedingungen, Kosmologie und Kollaps an. Warnzeichen notiert.
- **LL3 Ergebnis (08:45, Will 2014 lokal): teilweise Verstoss, Zahlen.** Table 4 (S. ~44 der Textkopie, Z. 2402-2416):
  alpha1 1e-4 (LLR) und 7e-5 (PSR J1738+0333); alpha2 2e-9 (Millisekundenpulsare, Spinpraezession; nicht 4e-7!);
  Nordtvedt: beta - 1 < 2,3e-4 "eta_N = 4 beta - gamma - 3 assumed"; LLR: WEP-Verletzung massiver Koerper ~1,4e-13
  (S. 47); E_g/m Erde 4,6e-10 (S. 46). eta_N = 4 beta - gamma - 3 - (10/3) xi - alpha1 + (2/3) alpha2 - ... (Gl. 66).
  - Zwei Regime fuer alpha2: schwaches Feld (Sonnenspin, 4e-7, GSS 2018) gegen starkes Feld (Pulsare, 2e-9, Will).
    Moderator: Kompaktheit bzw. Empfindlichkeit des Koerpers.
  - PPN g_0i (Will Z. 1669) [S]: g_0i = -(1/2)(4 gamma + 3 + alpha1 - alpha2 + zeta1 - 2 xi) V_i
    - (1/2)(1 + alpha2 - zeta1 + 2 xi) W_i - (1/2)(alpha1 - 2 alpha2) w_i U - alpha2 w^j U_ij.
  - **Kette K8 [M + P]:** V - W ist ein Gradient (chi_,0j = V_j - W_j, [L, TEGP]); quer gilt V^T = W^T, also
    g_0i^T = -(1/2)(4 gamma + 4 + alpha1) V^T, ART -4 V^T. Mitfuehrung relativ zu ART: R = (4 gamma + 4 + alpha1)/8.
    Mit gamma = 1 (GAMMA-NETZ-L: gamma = 2 kappa'/kappa_g = 1 bei einem Hamilton [P]) folgt alpha1_eff = 8 (R - 1).
    IMPULS-NETZ-1 5.4 [P]: J_iso, kl = 0,01: R - 1 = 7,4e-6 (Mittel), bis 1,32e-5 (200 Richtungen); waechst ~ (kl)^2;
    Aufloesungsgrenze ~3e-6. => alpha1_eff ~ 6e-5 bis 1,1e-4 bei kl = 0,01, langwellig fallend, unter ~2,4e-5
    nicht aufgeloest. J = 1: R bis 0,975/1,036 -> |alpha1_eff| bis ~0,29: durch LLR (1e-4) klar ausgeschlossen.
    Vorbehalt [H]: alpha1 ist auch ein Effekt der Bewegung w gegen das Vorzugssystem; gerechnet ist nur w = 0, und die
    Zuordnung setzt c_Licht = c_TT voraus.
- **F10 08:45:42 WebSearch "lunar laser ranging Nordtvedt parameter eta 2021 2024 Biskupek Mueller":** Erwartung:
  neuere LLR-Auswertung (Hofmann/Mueller 2018 oder Biskupek u. a. 2021) gibt eta_N mit Fehler ~1e-4 bis ~5e-5,
  mit null vertraeglich.
- **F11 08:45:42 arXiv:2005.01388 Abstract (Voisin u. a. 2020, Dreifachsystem PSR J0337+1715):** Erwartung:
  |Delta| < ~2e-6 (95 %) fuer den Unterschied der Fallbeschleunigung Neutronenstern gegen Weissen Zwerg; das ist die
  Starkfeld-Nordtvedt-Schranke, viel schaerfer als LLR fuer kompakte Koerper.
- **F11 Ergebnis (vor 08:46:23): bestaetigt.** Delta = (+0,5 +- 1,8)e-6 (95 %), omega_BD > 140 000.
- **F10 Ergebnis (vor 08:46:23):** nur Trefferliste; keine Primaerzahl. Neu: arXiv:2609.15303 (Sept. 2026). -> F12.
- **F12 08:46:29 arXiv:2609.15303 Abstract (LLR, Ephemeriden):** Erwartung: eta_N bzw. Delta(m_G/m_I) aus LLR mit
  Fehler um 1e-4 (eta) bzw. ~1e-13 (Delta); Ergebnis haengt etwas an der Ephemeride; mit null vertraeglich.
- **F13 08:46:29 WebSearch Gegensweep "anisotropic gravitational radiation damping binary pulsar orientation
  Lorentz violation constraint":** Erwartung: keine direkte Schranke auf eine bahnlagen-abhaengige (l = 4) Abstrahlung;
  SME-Pulsartests (Shao u. a.) betreffen die konservative Bahndynamik mit s^munu (l <= 2).
- **F14 08:46:29 arXiv-PDF 2508.03106 (Jacobson/Pulakkat), Stellen "maximal", "K = 0", "asymptotically flat",
  "cosmological constant", "second class":** Erwartung: Regime (i) mit k = 0 ist ART im maximalen Slicing (Lambda = 0)
  bei asymptotisch flachen Randbedingungen; "nonzero cosmological constant" betrifft k != 0 bzw. geschlossene Raeume.
  Zwangsbedingungen: CMC-Bedingung plus H bilden ein Paar zweiter Klasse.
- **F12 Ergebnis (vor 08:46:54): bestaetigt.** Ke u. a. 2026: Delta(m_g/m_i)_EM = (0,900 +- 3,183)e-14 (EPM21) usw.,
  alle mit null vertraeglich. [M] eta_N = Delta/((E_g/m)_Mond - (E_g/m)_Erde), Differenz ~ -4,4e-10 (Will S. 46:
  4,6e-10 Erde, 0,2e-10 Mond) -> sigma(eta_N) ~ 3,2e-14/4,4e-10 ~ 7e-5. "~1e-4" der Karte passt.
- **F13 Ergebnis: Erwartung bestaetigt (nur Trefferliste).** Keine Schranke auf eine bahnlagen-abhaengige (l = 4)
  Abstrahlung gefunden; SME-Pulsartests betreffen konservative Bahn und GWEP (Shao u. a. 2019, kubische
  Kruemmungskopplungen). Nach Recherchestand nicht belegt, dass es eine solche Schranke gibt.
- **F14 Ergebnis (08:46:54, quellen/F14-2508.03106.txt): bestaetigt und geschaerft, Q2 geloest.**
  - S. 12 [S]: Fall (A) K_,i = 0: "the Hamiltonian constraint H is first class"; Fall (B): H "second class without a
    'partner' constraint" -> Halbmodus (halbzahlige Freiheitsgrade), erster Ordnung in der Zeit, "unstable at high
    frequencies and strongly coupled at low frequencies".
  - S. 13 [S]: kompakte Raeume ohne Rand -> K_,i = 0; asymptotisch flach -> K = 0, "nothing but general relativity
    expressed in maximal slicing gauge" (nach Bellorin/Restuccia [10]). K = K(T) vorgeben eliminiert den Halbmodus und
    "gauge fixes the time reparametrization symmetry"; Freiheitsgrade wie ART ("minimally modified model").
  - S. 3: Pathologie nur bei allgemeinen (nicht asymptotisch flachen, kosmologischen) Randbedingungen.
  - **K7 bestaetigt:** Netz-Paar (delta R = 0, tr pi = 0) = Hamilton-Bedingung + Eichfixierung K = 0 = m2Hg mit K = 0 =
    ART im maximalen Slicing (fuer das exakte Kontinuum). Die zweite Klasse ist dort eine Eichfixierung, kein Defekt.
    Der Netzdefekt ist ein anderer: A c_v nicht in Bild M (Spur-Eichdefekt 0,90 langwellig), d. h. schon die Gitter-H
    ist nicht erster Klasse (Fall-B-artig?). [H] Ob das Netz einen Halbmodus traegt: EINE-WELT-LOCH-1 zaehlt nach den
    Regeln nur 2 masselose TT-Moden und 26 gegappte; ein Halbmodus waere erster Ordnung in der Zeit; nicht geprueft.
- **F15 08:48:20 arXiv:2112.06795 Abstract (Kramer u. a. 2021, Doppelpulsar):** Erwartung: Pdot_b stimmt mit ART auf
  1,3e-4 (95 %) ueberein; dazu Schranken auf Dipolstrahlung bzw. Skalar-Tensor; sieben PK-Parameter.

## D. Erwartungsverstoesse (Stand ~~08:52~~ 08:52:19 per date nach dem Schreiben, wichtigste zuerst)

1. **F7 Jacobson/Pulakkat 2025:** mHG (die nach den Daten einzig lebensfaehige Horava-Ecke) hat hamiltonsch einen
   Halbmodus (hochfrequent instabil, niederfrequent stark gekoppelt); lebensfaehig nur mit Blaettern konstanter
   mittlerer Kruemmung (m2Hg). Erwartet war "lebensfaehig mit Vorbehalt". Korrigiert: lebensfaehig nur mit der
   CMC-Zusatzbedingung; asymptotisch flach dann ART im maximalen Slicing. Das ist genau die Netz-Impulshaelfte
   c^H p = 0 (K7).
2. **F2 Franchini u. a. 2021:** "cannot be equivalent to GR, even in vacuum" gegen F1 (Bellorin/Restuccia: aequivalent).
   Moderator gefunden (F4): Randbedingungen (asymptotisch flach -> K = 0 -> ART) gegen kosmologisch; die beobachteten
   Groessen (Sonnensystem, Pulsare, GW-Erzeugung) sind in beiden Lesarten wie ART.
3. **K2 (Projektkette):** Im Netz gibt es langwellig keinen masselosen Zusatzskalar (EINE-WELT-LOCH-1). Die Leckage ist
   eine Fehlkopplung an die zwei TT-Moden, kubisch anisotrop (l = 4), kein Strahlungsterm eines Skalars. Erwartet
   (Karte SS3, 45 %) war die Zuordnung zum Zusatzskalar.
4. **LL3 Will 2014:** alpha2-Schranke 2e-9 (Pulsare) statt 4e-7; alpha1 7e-5 (PSR J1738) und 1e-4 (LLR), nicht ~1e-5.
5. **Gegensweep G1 (unten):** Fuer das Netz als Ganzes ist nicht der Doppelpulsar die schaerfste Schranke, sondern
   GW170817 (c_T auf 1e-15) gegen die TT-Restanisotropie 1,1e-5 (J_iso) bzw. 2,2e-7 (alle Arten frei).

## E. Regime-Trennung (Kontinuum vs. Gitter)

- Kontinuum (Horava, Khronon, Aether): isotrop im Vorzugssystem; Klassen: projizierbar (nur globales H), nicht
  projizierbar ohne a_i (lambda-R; H zweiter Klasse, Halbmodus bei allgemeinem Rand; mit CMC/K = 0 = ART-Eichung),
  gesund (H und pi_N zweiter Klasse, 1 Zusatzskalar), Khronon kovariant (Stueckelberg, volle Diffeo-Invarianz).
- Gitter: Regime K (4D-Regge, Zeltstangen): Takt flach exakte Eichung, Kommutator ~ eps (a/L)^~2 -> Kontinuum
  erster Klasse. Regime H (ew.py, gefuellt): Paar zweiter Klasse von Hand (H + K = 0), Gitter-H selbst nicht erster
  Klasse (A c_v nicht in Bild M; 0,90 langwellig konstant), kubisch anisotrop.
- Uebertragung je Aussage: (i) "zweite Klasse = Zusatzskalar" gilt im Kontinuum nur ohne Partnerbedingung (Fall B);
  das Netz hat einen Partner (K = 0) -> nicht uebertragbar. (ii) Isotrope Strahlungsformeln -> fuer die l = 4-Leckage
  nicht uebertragbar. (iii) alpha1 aus der queren Mitfuehrung: uebertragbar unter gamma = 1 und c_Licht = c_TT [H].
  (iv) mHG-Ergebnisse (keine Dipolstrahlung) gelten fuer das Netz nur, wenn sein langwelliger Grenzfall isotrop und
  die Gitter-H erster Klasse ist; beides ist auf dem gefuellten Netz nicht erfuellt.

## F. Unterscheidungspunkte

- Global (projizierbar) gegen je Ort/Eichwahl: Minkowski selbst (IR-instabil, Mukohyama u. a. 2026); Daten:
  Sonnensystem und Doppelsterne liegen im stark gekoppelten Bereich (BPS: unter ~1e13 cm). Zugaenglich: ja.
- m2Hg mit K = 0 (Takt physikalisch je Ort, maximales Slicing) gegen ART (Takt Eichwahl): asymptotisch flach identisch
  (J/P S. 13). Auseinander laufen sie nur (a) kosmologisch: K(T) != 0, lambda wirkt, G_C/G_N (BBN: lambda <~ 0,1);
  (b) im Kollaps: Grenzscheibe r = 3 G M/2 = universeller Horizont, Cauchy-Problem nach Punktkollaps der Schale
  (J/P). (a) zugaenglich (BBN, Kosmologie), (b) nur innerhalb des Ereignishorizonts, praktisch unzugaenglich.
- Gitter Regime K gegen H: Leckage langwellig konstant (H) gegen ~ (a/L)^2 (K). Zugaenglich ueber den Doppelpulsar,
  sofern die Zuordnung G_rad/G_N <-> Pdot_b gilt (setzt ART-artige konservative PK-Parameter voraus, nicht gerechnet).
- Leckage aus Fehlkopplung (K2) gegen Zusatzskalar: Bahnlagenabhaengigkeit (l = 4) gegen isotrop; Dipol (nur Skalar)
  gegen keiner. Daten: mehrere Doppelsterne gleicher Genauigkeit mit bekannter Bahnlage; derzeit nur einer auf 1e-4.

## G. Gegensweep (Regel 4), ~~08:52~~ 08:52:19 (date nach dem Schreiben)

Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- G1 **"Der Doppelpulsar ist die schaerfste Schranke fuers Netz."** Geprueft (lokal): GW170817 verlangt
  |c_T - c_Licht| < ~1e-15 (GSS Gl. 13 [S]); die TT-Tempi des Netzes streuen langwellig um 1,1e-5 (J_iso) bzw.
  2,2e-7 (alle Arten frei) (GEMEINSAMES-NETZ-v3 [P]), und c_Licht ist ein eigener Operator (LICHT-FINN-NETZ-1).
  Fuer das Netz als Ganzes ist also GW170817 schaerfer (Faktor 1e8 bis 1e10), allerdings im Tensor-, nicht im
  Skalarsektor. Gefallen.
- G2 **"G_rad/G_N - 1 ist direkt die Doppelpulsar-Groesse."** Nicht vollstaendig geprueft: Kramer 2021 vergleicht Pdot_b
  mit der ART-Vorhersage aus Massen, die aus anderen PK-Parametern (omega-dot, Shapiro) folgen. Deren Netzwerte sind
  nicht gerechnet. Bleibt [H].
- G3 **"Die Gitterweite ist mikroskopisch, also verschwinden (a/L)^2-Effekte."** Geprueft (lokal): L8 gibt l < 7,0e-28 m
  (LICHT-FINN-NETZ-1 [P]) -> (a/L)^2 < ~3e-79 fuer L ~ 1,3e12 m. Gehalten.
- G4 **"R1-Reduktion = Dirac-Dynamik des Paars."** Am Schreibtisch [M]: Fuer lineare Bedingungen a, p senkrecht auf
  denselben Raum U = Bild[M, c] ist die induzierte symplektische Form auf U^perp x U^perp kanonisch; das ist die
  Dirac-Klammer. Gehalten (Kontinuumsaussage zur Lapse-Gleichung damit implizit erfuellt).
- G5 **"Takt = Lapse."** Geprueft (lokal): MATERIE-NETZ-1: "Newtons Takt mit Einsteins Vorzeichen", Takt je Ecke,
  Operator -W^H B W [P]. Gehalten. Andere Lesart (Finn: Takt als Phase des Knotens, GEMEINSAMES-NETZ-v3) waere ein
  eigenes Feld = Khronon (Stueckelberg); dann ist erste Klasse auch mit physikalischem Takt moeglich (GSS Gl. 2).

## H. Offene Rueckfragen (wandern mit)
- Q1 (~~08:30~~ 08:29:27 per date): Ist die Summe-m_i^4-Abhaengigkeit ein Skalarsektor-Effekt? **Beantwortet ~~08:52~~ 08:52:19 (date) (K2):** Sie sitzt im
  nn-Anteil der Kopplung an die TT-Moden (Kopplungsvektor e_j), nicht in einem eigenen Skalarmodus. Rest offen: ob
  V1 auf der Bahn mitspielt (Bahnen ohne V1 gerechnet).
- Q2 (~~08:44~~ nach 08:44:00 per date): Ist m2Hg-Regime (i) mit k = 0 ART ohne Lambda? **Beantwortet ~~08:47~~ nach 08:46:54 per date (F14):** ja, asymptotisch flach
  "nothing but general relativity expressed in maximal slicing gauge".
- Q3 (neu): Hat das gefuellte Netz einen Halbmodus (erster Ordnung in der Zeit), wie Fall B? Nicht geprueft.
- Q4 (neu): Wie gross ist lambda_eff (bzw. c_eff) der langwelligen Bewegungsenergie des gefuellten Netzes? Nur
  kosmologisch relevant (K != 0). Nicht gerechnet.
- Q5 (neu, fuer Finn): Meint Finn mit Takt die Lapse (Uhrengang je Ecke) oder ein eigenes Phasenfeld je Knoten?

## I. Abschluss

- DOSSIER.md geschrieben ab 08:54:35, fertig 2026-10-05 08:59:36 CEST (date). Rueckwaertsdurchgang: Zahlen gegen ARBEITSFELD und Quellen geprueft; ein Satz berichtigt ("mehr als 70 Groessenordnungen" -> "(a/L)^2 < 3e-79, mehr als 60 unter 1e-15"); Zitate auf hoechstens eines je Quelle gekuerzt.
- Personendaten: eine E-Mail-Adresse in quellen/F14-2508.03106.txt durch "[E-Mail entfernt]" ersetzt (08:59:45, date).

## Vermerk der Leitung (05.10.2026, 11:11:57 CEST, date; nach V1-AUFHEBUNG-1)

- Die Angabe "rund 12-mal (bzw. 11-mal) ueber dem Doppelpulsar" galt fuer Kreisbahnen ohne den Energiekanal V1, also fuer eine unvollstaendige Quelle (nur Spannung und Impuls).
- Mit vollstaendiger Quelle (V1 + Spannung + Impuls J), unabhaengig nachgerechnet (V1-AUFHEBUNG-1, VA0):
  - auf V mit J_iso: groesste Abweichung abs(G - 1) = 1,5e-5, rund 9-mal unter 1,3e-4; Lagen-Spanne 1,8e-5
  - am exakt TT-isotropen Punkt aus SKALAR-MISCH-1: Spanne 1,5e-7 bei kl = 0,01, Rest ~(kl)^2, fuer kl -> 0 mit null vertraeglich (VA1)
- Gilt nur fuer synthetische Kreisbahnen auf V im Grenzfall k -> 0. Die Gewichte bleiben eine Abstimmung. "Finns Netz besteht den Doppelpulsar" bleibt unbelegt (Negativliste).
- Quelle: RUNDE-37/v1-aufhebung-1/ERGEBNIS.md, Abschnitte 2 und 5.1. Der Text oben bleibt unveraendert; Sicherung *.bak-vermerk-v1a.
