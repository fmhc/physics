# PT-AUSGLEICH-L: Arbeitsfeld (feldforscher fuer die Leitung claude-primary)

- Start 2026-10-05 04:21:33 CEST (date). Zeitbox 50 min, also Ende spaetestens gegen 05:11.
- Karte gelesen (KARTE.md, bindend). PA1 bis PA3 und ihre Bedeutung werden nicht geaendert.
- Gelesen (nur lesen): spiegel-haelfte-1/KARTE.md, PLAN.md, ERGEBNIS.md, code/spiegel_haelfte.py (Kopf, fj_referenz,
  lauf_unordnung); RUNDE-42/NEGATIV-LESARTEN.md (N9); RUNDE-42/quellen-leitung/ABRUFE-1830.md; RUNDE-42.md
  Zeilen 651-683 (Ernte SPIEGEL-HAELFTE-1); RUNDE-44/GEMEINSAMES-NETZ-v3.md Luecke L5 (Zeile 80).
- Kennzeichen: [S] Quelle mit Abschnitt/Gleichung, [S Abstract], [L] aus dem Gedaechtnis, [M] von Hand gerechnet,
  [ES] eigener Schluss, [H] Hypothese, [P] Projektdatei.
- Abrufbudget: 5 (arXiv-API oder arxiv.org per WebFetch). Keine Websuche.

## 0. Was aus den Projektdateien feststeht [P]

- Modell: BCC, 4 Zustaende (Verschiebungsbasis a = 1..4, Sprung h_a), W = C_x S_+, C_x = e^{i alpha} P_2 + e^{i beta_x} P_2',
  alpha = 0, beta = pi (Gegentakt), beta_x je Knoten gleichverteilt in [beta - W/2, beta + W/2].
- P_2 = Gram-Projektor (1/2)<n_a|n_b> (Rang 2), P_2' = 1 - P_2. Kompression P_2 S_+ P_2 = FJ (Foster/Jacobson) einer
  Haendigkeit, 2' wirkt dort als vollkommene Senke (Teil A, A5).
- A8: Bei W = 2 pi ist der Unordnungsmittelwert der Amplitude exakt FJ.
- Gemessen (Modell): W = 0: w_2(100) = 0,9979, min 0,9897 (kohaerente Rueckkehr). W = 2 pi: w_2(100) = 0,717 gegen
  N_FJ = 0,496; kohaerent 0,4937, inkohaerent 0,2237; Rueckgabequote r = 0,44; f_gross 31 %.
- Zwischenwerte: w_2(100) = 0,9899 (pi/2), 0,934 (pi), 0,804 (3 pi/2). Schwache Unordnung: Zusatzverlust ~ W^2.
- ERGEBNIS "Teil A" (Folge fuer Teil B): Komplexe Konjugation mit diagonaler Eichung tauscht die Haelften [M des Code-Agenten].

## 1. Zwei-Regime-Vorannahme und Plan

- Regime U ("ungebrochen"): Spektrum der effektiven Dynamik der sichtbaren Haelfte unimodular und diagonalisierbar, dann
  gibt es eine positive Metrik eta, und die Dynamik ist pseudo-unitaer (Mostafazadeh) [L]. Erwartete Lage: W = 0.
- Regime G ("gebrochen" bzw. Senke): keine positive eta; Gewicht geht in eine Richtung. Erwartete Lage: W = 2 pi, FJ.
- Vermuteter Moderator: die Taktunordnung W der verborgenen Haelfte (spektrale Trennung der beiden Haelften), beim
  PT-Dimer das Verhaeltnis Gewinn/Verlust gamma zu Kopplung kappa.
- Plan: (a) Schreibtisch PT-Form, eta, Rueckfluss; (b) Literatur 2610.00774 (Scout-Abstract lokal, Volltext per Abruf),
  2601.03189 (Abstract liegt vor, Volltext per Abruf); (c) PT und Informationsrueckfluss (Kawabata/Ashida/Ueda [L]);
  (d) 24-Monats-Pruefung zur Front (PT-Quantenlaeufe mit Dirac/Weyl/Masse) per arXiv-API.

## 2. Abrufprotokoll (Erwartung vor jedem Abruf, Ausgang danach)

### L0 (lokal, kein Abruf) 2026-10-05 04:27:58 CEST: Scout-Abstract 2610.00774 aus canonical.json
- Erwartung: diskrete NLS auf einem Stern mit vier Kanten; Gewinn auf zwei, Verlust auf zwei Aesten; Vertex-Zustaende;
  Stabilitaetsfenster; Wirbel mit Ladung; Schaltkreis. Keine Aussage zu linearen Spektren im Abstract.
- Ausgang: bestaetigt (eine Zeile). Akramov, Fayzullaev, Tojakhmadova, Akhmadjanov; nlin.PS; eingereicht 30.09.2026,
  Datum 02.10.2026; Vier-Kanten-Stern, DNLS, Wirbel mit fester Ladung, mit ausgeglichenem Gewinn und Verlust
  stromtragend, Stabilitaetsfenster, Schaltkreis. Kein Wort zu linearen Spektren oder Ausnahmepunkt im Abstract.
  Abweichung nur: Die Anordnung von Gewinn und Verlust nennt der Abstract nicht.

### F1 2026-10-05 04:28:26 CEST: arXiv 2610.00774 Volltext (arxiv.org/pdf/2610.00774)
- Erwartung: Stern mit vier Aesten, je Ast eine Kette; Gewinn i gamma auf zwei Aesten, Verlust auf zwei (PT = Spiegelung
  der Aeste plus Zeitumkehr). Lineares Spektrum reell unterhalb einer Schwelle gamma_c, die an der Kopplung zum
  Zentralknoten haengt (Ausnahmepunkt bei gamma = Kopplung oder einem Bruchteil davon). Eine Bedingung an die
  Ast-Kopplungen (abgestimmte Verzweigung) erwarte ich hier eher nicht; die Symmetrie der vier Aeste macht sie
  automatisch. Wirbel mit Ladung 1 (Phase 2 pi/4 je Ast); Strom durch den Knoten bei gamma > 0.
- Ausgang (PDF per WebFetch geladen, Werkzeug konnte es nicht lesen; Kopie quellen/F1-arXiv-2610.00774-abruf-20261005-0428.pdf,
  23 Seiten mit dem Read-Werkzeug gelesen, 04:28:49 bis 04:29:49):
  - **Abweichung 1 (Anordnung):** Gewinn und Verlust sitzen nicht astweise, sondern abwechselnd in jedem Ast (jeder Ast ist
    eine Kette von PT-Dimeren, Konotop-Modell); der Knoten ist ein Vierer-Block (Quadrimer), in dem Gewinnplaetze nur an
    Verlustplaetze koppeln (kappa_0) [S Abschn. 3.1, Gl. (19)-(23), Abb. 3]. Gewinn/Verlust gaussfoermig um den Knoten,
    gamma_n = gamma_0 exp(-n^2/sigma^2) [S Gl. (8)].
  - Bestaetigt (Schwelle an Kopplung): Kette: PT ungebrochen genau dann, wenn |kappa_0 - kappa_1| >= gamma [S Abschn. 2.1,
    Gl. (2), nach Konotop/Pelinovsky/Zezyulin EPL 2012]. Stern: nur numerisch; Schwelle bei sigma = 100 etwa 0,2 = |kappa_0 -
    kappa_1| (kappa_0 = 1, kappa_1 = 1,2), bei sigma = 2,5 etwa 0,43, bei sigma = 1,25 etwa 0,86 [S Abb. 4, abgelesen].
    Keine geschlossene Formel fuer den Stern.
  - Bestaetigt (keine Abstimmungsbedingung an die Aeste): Die vier Aeste sind gleich gebaut; eine Bedingung an die
    Ast-Kopplungen kommt nicht vor.
  - **Abweichung 2 (Kern, Mechanismus):** Am isolierten Knoten ist die lokale PT-Symmetrie fuer jedes gamma_0 != 0 gebrochen:
    "the block M_- eliminates the kappa_0 coupling, and the gain-loss sites decouple with eigenvalues +-gamma_0 for any
    gamma_0 != 0" [S Abschn. 3.4, nach Gl. (55), S. 15]; der antisymmetrische Zweig existiert nur bei gamma_0 = 0, weil "the
    two gain sites drive the hub in exactly opposite phase, so their net coupling to the loss sites cancels" [S Abschn. 3.2,
    Gl. (28)]. Wiederherstellung nur ueber die Kettenkopplung kappa_1 [S S. 15]. Lehre: **Wo die hermitesche Kopplung zwischen
    Gewinn- und Verlustseite in einem Kanal ausloescht, bricht jedes gamma > 0 die PT-Symmetrie.** Selbstanzeige: Dieselbe
    Struktur (Kopplung der Haelften bei k = 0 null) hatte ich vor F1 nur im Kopf, nicht hier notiert; sie zaehlt nicht als
    Vorhersage.
  - Wirbel: Windungszahl l = +-1 bei gamma_0 = 0 ist ein pi-Phasenmuster ohne Strom; mit gamma_0 != 0 wird er stromtragend,
    l = -1 bleibt [S Abschn. 4.1, Gl. (60)-(61)]. Stabil bei kappa_1 = 0 fuer mu in (2 kappa_0, 5,479 kappa_0) und
    (8,819 kappa_0, unendlich) [S Gl. (65)]; Stabilitaetskarte (kappa_1, gamma_0): stabil bei kleinem kappa_1 (< ~0,5) und
    gamma_0 (< ~0,45), Insel bei gamma_0 ~ 0,8 [S Abb. 7a]. Strom bei gamma_0 = 0,1 zwischen ~0,05 und 0,8 [S Abb. 7b].
  - Schaltkreis: ausdruecklich nur Skizze, "not a validated realization" (drei Gruende) [S Abschn. 5].
  - Fuer die Karte wichtig [ES]: Im ungebrochenen PT-Zustand fliesst ein stationaerer Strom von Gewinn zu Verlust; der
    "Ausgleich" ist ein Durchfluss, kein Hin und Zurueck.

### F2 2026-10-05 04:29:49 CEST: arXiv 2601.03189 Volltext (arxiv.org/pdf/2601.03189)
- Erwartung: kontinuierliche Schroedinger-Gleichung auf einem Stern-Graphen (drei oder mehr Kanten) mit periodischem
  PT-Potential V(x) = V_0 cos + i W_0 sin; gewichtete Vertex-Bedingungen alpha_1 psi_1 = alpha_2 psi_2 = ... und
  Sum (1/alpha_k) d psi_k = 0. Die "Bedingung" ist eine Summenregel an die Gewichte (Art 1/alpha_1^2 = Sum_k 1/alpha_k^2,
  wie bei Sobirov/Matrasulov 2010); sie macht den Stern auf eine Kette abbildbar. Mit Regel: Ausnahmepunkt wie in der
  Kette (Makris-Wert); ohne Regel: komplexe Eigenwerte schon unterhalb. Das wuerde PA3 fuer diese Arbeit stuetzen.
- Ausgang (PDF geladen, Werkzeug konnte es nicht lesen; Kopie quellen/F2-arXiv-2601.03189v2-abruf-20261005-0430.pdf,
  Fassung v2 vom 30.09.2026, Seiten 1-11 mit dem Read-Werkzeug gelesen bis 04:31:13):
  - Bestaetigt (Geometrie, Potential, Summenregel): Stern mit vier halbunendlichen Kanten; V(x) = V_0 (cos^2 x + i W_0 sin 2x)
    [S Gl. (2)]; "To preserve PT-symmetry in the system, such a graph must contain an even number of edges" [S Abschn. III].
    Vertex: gewichtete Stetigkeit und gewichtete Kirchhoff-Regel [S Gl. (14)]; globale PT verlangt
    alpha_j Psi_j(x,t) = alpha_-j Psi*_-j(-x,-t) [S Gl. (15)], daraus die Summenregel
    1/alpha_-1^2 + 1/alpha_-2^2 = 1/alpha_1^2 + 1/alpha_2^2 [S Gl. (16)]. Nichtlinear: 1/beta_-1 + 1/beta_-2 = 1/beta_1 + 1/beta_2
    [S Gl. (30)].
  - Bestaetigt (Mostafazadeh konkret): In 1D ist das Spektrum genau dann reell, wenn eine Aehnlichkeitstransformation
    S = diag(r^n) H hermitesch macht; das gilt fuer |W_0| <= 0,5 [S Abschn. II, Gl. (9)-(12)].
  - **Abweichung (Kern):** Mit erfuellter Summenregel liegt der Ausnahmepunkt auf dem Stern NICHT beim Kettenwert 0,5,
    sondern bei W_0 = 0,185 (V_0 = 6, N = 100): reell bei 0,15 und 0,185, komplex bei 0,19 [S Abb. 2-4, Text S. 7].
    Die Verzweigung senkt die Schwelle um etwa den Faktor 2,7.
  - Teilweise: Verletzte Summenregel (alpha_-j = 1, alpha_j = 2) zeigt komplexe Eigenwerte (Im ~ +-0,02 in schmalen
    k-Fenstern bei k ~ +-0,42) nur an EINEM Punkt, W_0 = 0,185 [S Abb. 5]. Dass Verletzung schon bei kleinem W_0 bricht,
    ist nicht gezeigt.
  - Nichtlinear: Solitonen stabil bei W_0 = 0,45, instabil bei 0,55; "the phase transition point shifts from 0.185 to 0.5,
    due to the cubic nonlinearity" [S S. 11]; kleine Abweichung von der Summenregel laesst das Soliton verschwinden [S S. 11].
  - [ES] Die "Abstimmung" ist hier die PT-Invarianz der Vertex-Bedingung selbst, also notwendig fuer PT, nicht hinreichend
    fuer reelles Spektrum.

## 3. Schreibtisch (ab 2026-10-05 04:32:46 CEST, von Hand, nicht gegengelesen)

Bezeichnungen wie im Code: U = C S_+, C = e^{i alpha} P_2 + e^{i beta_x} P_2', S_+(k) = diag(e^{-i k.h_a}), |h_a| = 1 Hop.
Bloecke bezueglich 2 + 2': A = e^{i alpha} P_2 S_+ P_2 (FJ), B_12 = e^{i alpha} P_2 S_+ P_2', B_21 = e^{i beta_x} P_2' S_+ P_2,
D = e^{i beta_x} P_2' S_+ P_2'. Unitaritaet: A^dag A + B_21^dag B_21 = 1 auf 2 [M].

S1 Kopplung der Haelften bei langen Wellen [M]: P_2 P_2' = 0 und S_+(k) = 1 - i diag(k.h_a) + O(k^2), also
   B_12(k) = -i e^{i alpha} P_2 diag(k.h_a) P_2' + O(k^2) = O(|k|). Bei k = 0 sind die Haelften entkoppelt.

S2 FJ-Verlust ist diffusiv [M]: A(k) = f + g.sigma mit f = (1/4) Sum_a e^{i k.h_a} = 1 - |k|^2/6 + ..., g = (i/3) k + O(k^2)
   (Sum_a h_a = 0, Sum_a h_a h_a^T = (4/3) 1). Eigenwerte 1 - |k|^2/6 +- (i/3)|k|: Tempo 1/3,
   |lambda|^2 = 1 - (2/9)|k|^2. A ist bis O(k^2) normal (g parallel zu reellem Vektor): FJ = unitaerer Weyl-Schritt mal
   Daempfung e^{-|k|^2/9} je Schritt. Gauss-Paket (|psi(k)|^2 ~ exp(-2 sigma^2 k^2)):
   N_FJ(t) ~ (1 + t/(9 sigma^2))^{-3/2}, also Potenzgesetz t^{-3/2}, kein exponentieller Zerfall.
   Gegen R2 [P] bei t = 100: sigma = 3/4/5/6/8 gibt 0,299/0,453/0,576/0,668/0,787 gegen gemessen 0,357/0,496/0,605/0,687/0,795.
   Passt fuer breite Pakete auf 1 %, fuer schmale ueberschaetzt die Naeherung den Verlust (hoehere Ordnungen in k).

S3 Keine positive Metrik fuer FJ [M]: Fuer k != 0 liegen beide Eigenwerte von A(k) im Einheitskreis. Gaebe es eta > 0 mit
   A^dag eta A = eta, folgte fuer den Eigenvektor v: (|lambda|^2 - 1) v^dag eta v = 0, also v^dag eta v = 0. Widerspruch.
   FJ ist nicht pseudo-unitaer und hat keine Paarung lambda <-> 1/lambda* (nur Verlust, kein Gewinn). Ein "passives PT"
   (Guo 2009 [L]) braucht gleichmaessigen Verlust auf einer Seite; FJ verliert k-abhaengig in denselben zwei Komponenten.

S4 PT-Form mit Gewinn und Verlust zwischen den Haelften [M]:
   - Ansatz U_gamma = G C S_+ (oder symmetrisch), G = e^{-gamma} P_2 + e^{+gamma} P_2' (sichtbar verliert, verborgen gewinnt).
   - (a) Bei k = 0 ist S_+ = 1, also U_gamma(0) = e^{i alpha - gamma} P_2 + e^{i beta + gamma} P_2': Betraege e^{-+gamma},
     gebrochen fuer jedes gamma > 0.
   - (b) Die Haelften tauschende antiunitaere Abbildung Theta (D K bzw. D P K; ERGEBNIS: "Komplexe Konjugation mit diagonaler
     Eichung tauscht die Haelften") erfuellt Theta U Theta^-1 = U^-1 nur fuer alpha = beta (bei k = 0 folgt
     e^{-i alpha} P_2' + e^{-i beta} P_2 = e^{-i alpha} P_2 + e^{-i beta} P_2'). Fuer alpha = 0, beta = pi gilt stattdessen
     Theta U Theta^-1 = -U (Teilchen-Loch-Typ, Paare E <-> pi - E), keine Realitaet. Fuer alpha = beta ist C ein Skalar,
     U = e^{i alpha} S_+ sind vier ballistische Laeufer; die Weyl-Kegel sind dann keine eigenen unitaeren Baender.
   - (c) Dimer-Naeherung um k = 0: E = +-sqrt(v_c^2 |k|^2 - gamma^2), Ausnahmekugel |k_EP| = gamma/v_c (v_c Steigung von S1;
     Konstante nicht gerechnet [H]). Innen (lange Wellen, dort lebt das Weyl-Teilchen) gebrochen.
   - Gleiche Struktur wie F1 (2610.00774, S. 15): Wo die hermitesche Kopplung zwischen Gewinn- und Verlustseite ausloescht,
     bricht jedes gamma.
   - Folge: Ein PT-Ausgleich zwischen sichtbarer und verborgener Haelfte macht das langwellige Umklappen nicht verlustfrei.

S5 Metrik im kohaerenten Regime (W = 0) [M]:
   - Baender von U(k): orthonormal u_j, Eigenwerte lambda_j (|lambda_j| = 1). alpha-Baender j = 1, 2 (nahe e^{i alpha}),
     sichtbare Teile a_j = P_2 u_j, R = [a_1 a_2] (2 x 2, bei k = 0 unitaer, nahe k = 0 invertierbar).
   - Fuer Zustaende in den alpha-Baendern gilt psi_2(t) = R Lambda^t R^-1 psi_2(0) = M^t psi_2(0).
   - M ist pseudo-unitaer: M^dag eta M = eta mit eta = (R R^dag)^-1 = (P_2 Pi_alpha P_2)^-1 >= 1.
   - Und psi_2^dag eta psi_2 = |c|^2 = ||psi_2||^2 + ||psi_2'||^2. **Die eta-Norm ist sichtbares plus verborgenes Gewicht.**
   - Das ist Mostafazadehs Aequivalenz [L] in konkreter Form: rho = sqrt(eta) bildet auf die unitaere Banddynamik ab.
   - eta - 1 = O(k^2). Gemessen bei W = 0: 1 - w_2(100) = 0,2 %, min w_2 = 0,9897 [P].
   - Grenze: eta existiert, solange R invertierbar ist und die alpha-Baender spektral von den beta-Baendern getrennt sind.

S6 Rueckfluss: Amplitude gegen Gewicht [M, P]:
   - Bei W = 2 pi ist <psi_2> exakt FJ (A8).
   - Der Rueckfluss steckt ganz in den Schwankungen: inkohaerent 0,2237 gegen w_2 - N_FJ = 0,221 [P].
   - Eine eta-Norm der gemittelten sichtbaren Amplitude (quadratische Form in <psi_2>) sieht ihn nicht; fuer FJ gibt es ohnehin
     kein eta > 0 (S3).
   - In einer einzelnen Welt ist die Gesamtdynamik unitaer (eta = 1 auf 2 + 2'); dort ist der Rueckfluss echtes Gewicht.
     Keine Umschreibung laesst ihn verschwinden.

S7 Zwei Regime [ES]:
   - Regime U (kohaerent, W klein): sichtbare Dynamik pseudo-unitaer (S5), Rueckkehr kohaerent, fast vollstaendig.
   - Regime G (W = 2 pi): Senke auf Amplitudenebene (FJ), 44 % inkohaerenter Rueckfluss auf Gewichtsebene, kein eta.
   - Moderator: die vom verborgenen Takt aufgesammelte Dephasierung, ~ W^2 t (Born; Verhaeltnis 4,58 gegen 4 [P]). Dazu
     [H] die spektrale Trennung der sichtbaren und der verborgenen Quasienergie-Baender.
   - Unterscheidungspunkt im Modell: Phasenlage des Rueckflusses.
     - Kohaerent: Ueberlapp mit dem Bandzustand, f_gross klein.
     - Inkohaerent: weiss in k. f_gross 0,11 % (W = 0), 2,9 % (pi), 15 % (3 pi/2), 31 % (2 pi) [P].
     - Getrennt ab W ~ pi.
   - In der PT-Form (S4): Ausnahmekugel |k| = gamma/v_c. Getrennt wird bei den langen Wellen, also genau dort, wo die
     Niedrigenergie-Physik lebt.

S8 Masse (L5) [L, M]:
   - Eine Dirac-Masse koppelt die beiden Haendigkeiten bei derselben Quasienergie. Im Modell sitzen sie bei alpha (2) und
     beta (2'); fuer beta - alpha = pi hybridisieren sie bei k = 0 nicht, es gibt keine Masse.
   - Der unitaere Dirac-Automat (D'Ariano/Perinotti 2014 [L, P]) mischt die Haelften je Schritt mit fester Amplitude m
     (n^2 + m^2 = 1). Das ist "Masse ohne Verlust" durch einen kohaerenten, unitaeren Teil-Umklapp.
   - PT-Variante (Dimer mit Kopplung m und Gewinn/Verlust gamma): E(k = 0) = +-sqrt(m^2 - gamma^2). Reelle Masse fuer gamma < m,
     masselos am Ausnahmepunkt. Erinnerung [L]: nicht-hermitescher gamma_5-Massenterm (Bender u. a.; Alexandre/Bender/
     Millington) mit m_phys^2 = m^2 - mu^2.

## 2b. Abrufprotokoll, Fortsetzung

### F3 2026-10-05 04:33:22 CEST: arXiv-API, drei Titel in einer Abfrage
- Abfrage: ti:"information retrieval and criticality" OR ti:"extension of gauge theories" OR (ti:"no-signaling" AND ti:PT).
- Erwartung:
  - (1) Kawabata/Ashida/Ueda 2017: ungebrochen -> Information fliesst hin und zurueck, vollstaendige Wiedergewinnung;
    gebrochen -> Fluss in eine Richtung; am Ausnahmepunkt kritisches Verhalten (Potenzgesetz).
  - (2) Alexandre/Bender/Millington: Dirac-Feld mit nicht-hermiteschem Massenterm m + mu gamma_5, physikalische Masse
    m^2 - mu^2, ungebrochen fuer |mu| < m; Folgen fuer Neutrinos.
  - (3) Lee/Hsieh/Flammia/Lee 2014: lokale PT-Entwicklung an einem Teil eines verschraenkten Paars erlaubt Signale,
    verletzt also das No-signaling-Prinzip.
- Bedeutung: (1) stuetzt S7 (Rueckfluss = ungebrochen), (2) stuetzt S8, (3) begrenzt "Ausgleich als neue Physik".
- Ausgang F3 (Kopie quellen/F3-arxiv-api-drei-titel-abruf-20261005-0433.md):
  - (1) bestaetigt, plus Zusatz:
    - "complete information retrieval ... in the PT-unbroken phase, whereas no information can be retrieved in the
      PT-broken phase"; Uebergang = reversibel/irreversibel-Kritikalitaet mit Potenzgesetzen [S Abstract 1705.04628].
    - **Zusatz, nicht erwartet:** "by embedding a PT-symmetric system into a larger Hilbert space so that the entire system
      obeys unitary dynamics, we reveal that behind the information retrieval lies a hidden entangled partner protected by
      PT symmetry".
    - Analyse: Finns "verborgene Haelfte" hat in der Literatur ein genaues Gegenstueck (unitaere Einbettung mit verborgenem
      Partner). Unsere Richtung ist umgekehrt (unitaer gegeben, PT-Lesart gesucht); im ungebrochenen Bereich treffen sich
      beide ueber eta (S5).
    - W = 0 liegt auf der reversiblen Seite, FJ auf der irreversiblen. W = 2 pi passt in keines der beiden Bilder
      (Amplitude: keine Rueckkehr; Gewicht: 44 % ohne Phase) [ES].
  - (2) **Erwartung verletzt im Kern:**
    - "Gauge invariance is restored when the Hermitian and anti-Hermitian masses are of equal magnitude, and the theory
      reduces to that of a single massless Weyl fermion" [S Abstract 1509.01203].
    - Mit Eichfeld ist der PT-Massenterm also nur am Ausnahmepunkt eichinvariant, und dort ist die Masse null.
    - Die Formel m^2 - mu^2 steht nicht im Abstract (bleibt [L]).
    - Neutrinos: Die Yukawa-Fassung "can explain the smallness of the light-neutrino masses" [S Abstract].
    - Analyse: Fuer L5 ("Masse ohne Verlust") ist der PT-Ausgleich der Chiralitaeten kein Massenerzeuger. In der
      eichinvarianten Fassung loescht er die Masse aus (ein Weyl-Teilchen, wie FJ auf einer Haelfte). Nur ueber Yukawa
      bleibt eine kleine Masse [S Abstract; Mechanismus nicht gelesen].
  - (3) bestaetigt: Lokale PT-Symmetrie verletzt das No-signaling-Prinzip; globale PT "is known to reduce to standard
    quantum mechanics"; "either a trivial extension or likely false as a fundamental theory" [S Abstract 1312.3395].
    - Gegenstimmen im selben Treffer: Japaridze/Pokhrel/Wang 2017 (mit PT-Skalarprodukt bleibt No-signaling gewahrt) und
      Kumari/Sen 2020, 2022 ("can be removed by using a CPT inner product").
    - **Zwei Regime mit Moderator:** Das verwendete Skalarprodukt entscheidet. Mit Dirac-Skalarprodukt gibt es Signale, also
      neue, aber relativitaetswidrige Physik. Mit eta/CPT-Skalarprodukt gibt es keine Signale, dann ist es Standard-QM
      [ES].

### F4 2026-10-05 04:35:22 CEST: arXiv-API, 24-Monats-Pruefung (Regel 7) zu PT/nicht-hermiteschen Quantenlaeufen mit Dirac/Weyl/Masse
- Abfrage: (abs:"PT-symmetric" OR abs:"non-Hermitian") AND (abs:"quantum walk" OR abs:"cellular automaton") AND
  (abs:Dirac OR abs:Weyl OR abs:mass), submittedDate 05.10.2024 bis 05.10.2026, neueste zuerst, 15 Treffer.
- Erwartung: einige Arbeiten zu Ausnahmepunkten, Haut-Effekt und Topologie in nicht-hermiteschen Dirac-Laeufen
  (Photonik). Keine Arbeit, die eine Masse ohne Verlust ueber einen PT-Ausgleich mit verborgener Haelfte oder Takt
  gewinnt. Kein Bezug auf Foster/Jacobson.
- Bedeutung: Findet sich eine solche Arbeit, ist S4/S8 an ihr zu pruefen, bevor irgendetwas als "nicht moeglich" gilt.
- Ausgang F4 (Kopie quellen/F4-arxiv-api-24monate-pt-quantenlauf-abruf-20261005-0435.md):
  - **Abweichung:** Es gab nur einen Treffer statt einiger, und er passt vermutlich nur ueber "center-of-mass".
    Yang/Sun/Hong/Yang 2026 (2606.27043): photonischer offener Quantenlauf, Phasenrauschen (Dephasierung) und
    Gewinn-Verlust-Ungleichgewicht getrennt einstellbar, stetiger Uebergang kohaerent <-> inkohaerent, "a crossover from
    coherence-enhanced to decoherence-enhanced transport" [S Abstract, teils sinngemaess].
  - Analyse: Inhaltlich ist das naeher an unserer Frage als erwartet. Die Arbeit hat genau die zwei Stellgroessen der Karte,
    Dephasierung (unser W) und nicht-hermiteschen Gewinn/Verlust (unser gamma), und zeigt den Uebergang im Experiment.
  - Masse ohne Verlust ueber PT-Ausgleich mit verborgener Haelfte: in dieser Abfrage nicht gefunden. Urteil "nach
    Recherchestand nicht belegt", nicht "widerlegt"; die Abfrage ist eng (Selbstanzeige).

### F5 2026-10-05 04:36:07 CEST: arXiv-API, 24-Monats-Pruefung (Regel 7) zu nicht-hermiteschen bzw. PT-Massentermen
- Abfrage: (abs:"non-Hermitian" OR abs:"PT-symmetric" OR abs:"pseudo-Hermitian") AND (abs:"neutrino mass" OR abs:"Dirac mass"
  OR abs:"mass term" OR abs:"fermion mass"), submittedDate 05.10.2024 bis 05.10.2026, neueste zuerst, 15 Treffer.
- Erwartung: einige Arbeiten (Alexandre, Millington, Mavromatos u. a.) zu nicht-hermiteschen Dirac-/Neutrinomassen mit
  m^2 - mu^2 und Aequivalenz zu hermitescher Theorie unterhalb des Ausnahmepunkts; vielleicht ein Mechanismus fuer kleine
  Neutrinomassen nahe dem Ausnahmepunkt. Keine Gitter-/Takt-Herleitung einer Masse ohne Verlust.
- Bedeutung: Prueft, ob S8 und F3(2) ("PT-Ausgleich der Chiralitaeten ist kein Massenerzeuger") an der Front ueberholt ist.
- Ausgang F5 (Kopie quellen/F5-arxiv-api-24monate-nh-masse-abruf-20261005-0436.md):
  - **Abweichung:** 9 Treffer, keine Alexandre/Millington-artige Arbeit zu nicht-hermiteschen Neutrinomassen in 24 Monaten.
    Stattdessen:
    - Die "imaginaere Dirac-Masse" ist in photonischen Zeitkristallen der Mechanismus einer Impulsluecke (k-gap) mit
      wachsenden und zerfallenden Moden (2510.08995, 2609.08181) [S Abstract].
    - PT-symmetrischer imaginaerer Massenterm in DS-II-Dirac-Modellen (2602.02073) [S Abstract].
    - Nicht-hermitesche Fermion-Massenmatrix mit komplex konjugierten Polen (2606.08143) [S Abstract].
    - PT-QM fuer GUP-Neutrinooszillationen (2506.07588) [S Abstract].
  - Analyse: Die k-gap-Lesart passt zu S4(c). Ein Gewinn/Verlust ohne ausgleichende Kopplung bei kleinen k wirkt wie eine
    imaginaere Masse: Ein Bereich langer Wellen waechst oder zerfaellt [ES]. Eine Gitter- oder Takt-Herleitung einer
    Masse ohne Verlust ueber einen PT-Ausgleich ist nach Recherchestand nicht belegt.
- Abrufbudget verbraucht: 5 von 5 (F1 bis F5). L0 war lokal.

## 4. Gegensweep (ab 04:38, "Was war so selbstverstaendlich, dass ich es nicht geprueft habe?")

1. Existenz der Haelften tauschenden antiunitaeren Abbildung Theta (S4b stuetzt sich auf ERGEBNIS, Satz des Code-Agenten).
   **Geprueft [M]:**
   - P_2' = 1 - P_2 hat dieselben Betraege wie P_2.
   - Fuer drei verschiedene a, b, c gilt <a|P_2'|b><b|P_2'|c><c|P_2'|a> = (-1)^3 B = -B mit
     B = <a|P_2|b><b|P_2|c><c|P_2|a> = +-i/(24 sqrt 3) (PLAN A3). Das ist rein imaginaer, also -B = B*.
   - P_2* hat die Betraege von P_2 und die Invariante B*. Damit sind P_2' und P_2* durch eine diagonale Eichung D verwandt
     (alle Nebenbetraege != 0, Bargmann-Invarianten gleich), also P_2' = D P_2* D^dag und Theta = D K.
   - Ausserdem: S4(a) braucht Theta gar nicht. Der Bruch bei k = 0 folgt allein aus S_+(0) = 1.
2. Einheiten von k und sigma (Hop) in S2: geprueft gegen R2 (sigma = 8: 0,787 gegen 0,795). Die Konvention passt.
3. Nicht geprueft: Haengt die Rueckgabequote r = 0,44 an der Paketbreite sigma = 4? Nur sigma = 4 ist gerechnet. S6 und S7
   stuetzen sich auf diese eine Zahl.
4. Nicht geprueft: Die PT-Definition fuer Zeitschritt-Laeufe (Theta U Theta^-1 = U^-1, Mochizuki/Kim/Obuse 2016 [L]) habe
   ich aus dem Gedaechtnis verwendet. Die beiden Gitterarbeiten (F1, F2) sind Hamilton-Systeme mit kontinuierlicher Zeit.
5. Nicht geprueft: ob die arXiv-API Phrasen mit Bindestrich ("PT-symmetric", "non-Hermitian") zuverlaessig findet. F4 hatte
   nur einen Treffer. Das kann an der Abfrage liegen.
6. Nicht geprueft: dass die Konstante v_c der Ausnahmekugel (S4c) endlich und nicht null ist. Gezeigt ist nur die lineare
   Ordnung von B_12. Nimmt die Kopplung in manchen Richtungen erst quadratisch zu, waere der gebrochene Bereich dort groesser.

## 5. Nachtraege (ab 04:39:43)

- Gegensweep Punkt 6 **geprueft [M]:**
  - Aus P_2 K P_2' = 0 (K = diag(k.h_a) hermitesch) folgt [K, P_2'] = 0, also (K_aa - K_bb)(P_2')_ab = 0.
  - Alle Nebenelemente von P_2' haben den Betrag 1/sqrt 12 != 0. Daraus folgt K ~ 1, mit Sum_a h_a = 0 also k.h_a = 0 fuer
    alle a, also k = 0.
  - Die lineare Kopplung ist daher fuer jede Richtung ungleich null; ihr Minimum ueber die Richtungen ist positiv
    (kompakte Kugel), also v_c > 0.
- S4(d) neu [M, erste Ordnung]:
  - Fuer alpha != beta gibt es keinen PT-Schutz. Stoerung erster Ordnung in gamma fuer ein nicht entartetes Band j mit
    sichtbarem Gewicht w_j: delta ln|lambda_j| = -gamma (2 w_j - 1).
  - Unimodular bleibt also nur, wo w_j = 1/2 ist (Mass null). Die PT-Form des Projekt-Laufs (alpha = 0, beta = pi) bricht
    damit generisch auf der ganzen Brillouin-Zone, nicht nur bei kleinen k.
  - Nicht gerechnet: entartete Stellen, hoehere Ordnungen.
- Projekt-grep (Loschmidt, Spurabstand, Kawabata, pseudo-herm, pseudo-unit, PT-AUSGLEICH): keine Karte zu
  Informationsrueckfluss oder Unterscheidbarkeit im Modell der verborgenen Haelfte; PT-AUSGLEICH nur in RUNDE-45.md (Start).
- Kartenvorschlag (hoechstens einer): RUECKFLUSS-INFO-1, siehe DOSSIER Abschnitt 6.
- **S4(c) berichtigt (ab 04:42; der alte Text bleibt oben stehen und gilt als gestrichen):**
  - Die "Ausnahmekugel |k_EP| = gamma/v_c" war eine Zwei-Niveau-Naeherung. Fuer alpha = beta ist U = e^{i alpha} S_+(k)
    diagonal in der Verschiebungsbasis. Eigenvektoren |a>, alle mit sichtbarem Gewicht w = <a|P_2|a> = 1/2. Damit ist die
    erste Ordnung ueberall null, PT-geschuetzt.
  - Entartet ist es dort, wo k.h_a = k.h_b mod 2 pi (sechs Ebenenscharen, k = 0 auf allen). Im entarteten 2 x 2-Block ist
    Gamma = P_2 - P_2' rein nebendiagonal mit Betrag 2|(P_2)_ab| = 1/sqrt 3. Die Verschiebungen von ln|lambda| sind
    +-gamma/sqrt 3, also gebrochen.
  - Der gebrochene Bereich sind Streifen der Breite ~ gamma um diese Ebenen, keine Kugel [M, entartete Stoerungsrechnung
    erster Ordnung, nicht gegengelesen].
  - Die Aussage "lange Wellen gebrochen" bleibt (k = 0 liegt auf allen Ebenen).

## 6. Abschluss

- DOSSIER.md geschrieben ab 04:41:05, Textende 04:43:48 CEST (date).
- Offene Rueckfragen, die mitwandern:
  - (i) Haengt r = 0,44 an sigma?
  - (ii) Wie ist S4(c, d) numerisch an U_gamma(k) zu pruefen? Das ist mit Stoerungsrechnung weitgehend ableitbar, daher
    keine Karte.
  - (iii) Formel m^2 - mu^2 nur [L].
  - (iv) Woertlichkeit F3 bis F5 nicht gegen das Original geprueft.
