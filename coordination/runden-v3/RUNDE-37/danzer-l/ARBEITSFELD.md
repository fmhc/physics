# ARBEITSFELD DANZER-L (eine Arbeitsdatei, vor jedem Schritt neu lesen)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-05 04:18:35 CEST (date). Zeitbox 60 min, also bis 05:18:35.
- Regeln: keine Websuche; hoechstens 8 Abrufe (arXiv-API, arxiv.org abs/pdf, freie Verlagsseiten); Kopie in quellen/;
  lokal kein python/awk/perl, jq nur lesen; Versiegeltes nie oeffnen; nur in RUNDE-37/danzer-l/ schreiben; Zeiten per date.
- Kennzeichen: [S] an der Quelle gelesen (mit Abschnitt/Gleichung), [S Abstract], [L] Gedaechtnis, [M] von Hand,
  [ES] eigener Schluss, [H] Hypothese, [P] Projektdatei.
- Gestrichenes wird ~~durchgestrichen~~, nicht geloescht. Offene Rueckfragen stehen unten und wandern mit.
- Datei angelegt ab 2026-10-05 04:29:35 CEST (date).

## 0. Vorarbeit gelesen (04:18 bis 04:29)

- KARTE.md ganz. DZ1 85 %, DZ2 80 %, DZ3 75 %; Bedeutungen vorab. Nicht aendern.
- GEMEINSAMES-NETZ-v3 Abschn. 4, Weiche 3: Kristall (kubisch, TT-Spanne 6,3 %, abstimmbar auf 1e-5 bis 2e-7) oder
  Glas (im Mittel isotrop, Rauschen ~N^-1/2) [P].
- TT-ISO-1: Regge-Steifigkeit der affinen TT-Welle schon isotrop (1/4, Spanne <= 2,5e-8); die ganze Anisotropie sitzt
  in der effektiven Masse; Symmetriezaehlung der Leitung "9 gegen 4 Invarianten der Gradientenenergie"; die
  Dispersion hat volle m-3m-Form; skalare Regel zweiter Klasse (Spur-Eichdefekt konstant ~0,9) [P].
- TT-GRUND-1: keine natuerliche Massenregel (5,3 bis 8,1 %); isotrope Menge = schmales Tal (Kurve bei 1e-4), Boden
  faellt bis 7e-8; Selbstanzeige 7: Boden nicht von Dispersion zwischen |k| = 1e-3 und 2e-3 getrennt [P].
- LICHT-FINN-NETZ-1: Maxwell langwellig isotrop, a2 = -1/8 + S4/24 (kubisch, l = 4), keine Doppelbrechung bis (kl)^4;
  Dimensionsvergleich: "Das k^2-Glied ist ein Tensor 4. Stufe"; Wabe 2D isotrop durch Sechszaehligkeit [P].
- TETRAEDER-L: harte Tetraeder -> dodekagonaler Quasikristall (nicht ikosaedrisch); 600-Zelle auf S3; Fang/Irwin
  (arXiv:1511.07786, "contain only regular tetrahedra", ohne journal_ref); Elser-Sloane per cut-and-project
  (Baake/Gaehler 1998) [P, dort S Abstract].

## 1. Projektsuche (04:29:20, grep mit allen Ausschluessen)

- "Danzer": nur KARTE, RUNDE-45.md (Kartenzeile) und Kusner u. a. (12-Kugel-Problem, Danzer 1963, andere Sache).
- "ABCK": nichts. "Phason": nur eine Nebenbemerkung in dreieck-pumpe-l/ARBEITSFELD.md Z. 214. Keine Rechnung.
- Ikosaedrisch: Frustration (RUNDE-17), 600-Zelle (RUNDE-22), ICO-STAB (RUNDE-29, Cluster). Keine Tensor-/Isotropie-
  rechnung auf ikosaedrischem Netz. -> Karte ist nicht vorab aus Projektdateien beantwortet.

## 2. Schreibtisch [M] (vor jedem Abruf, 04:30 bis 04:3x)

### 2.1 Invarianten von I in D_l (Charaktertafel)

- Klassen von I (60): E; 15 C2 (pi); 20 C3 (2pi/3); 12 C5 (2pi/5); 12 C5^2 (4pi/5).
- chi_l(theta) = sin((2l+1)theta/2)/sin(theta/2):
  - chi_l(pi) = (-1)^l; chi_l(2pi/3) = 1, 0, -1 (l mod 3 = 0, 1, 2);
  - chi_l(2pi/5) + chi_l(4pi/5) = 2, 1, 0, -1, -2 (l mod 5 = 0..4), weil chi(2pi/5) = 1, tau, 0, -tau, -1 und
    chi(4pi/5) = 1, -1/tau, 0, 1/tau, -1 mit tau - 1/tau = 1.
- n_l = [ (2l+1) + 15(-1)^l + 20 chi3 + 12 (chi5 + chi5^2) ] / 60:
  - l = 0: 60/60 = 1; l = 1: (3 - 15 + 0 + 12) = 0; l = 2: (5 + 15 - 20 + 0) = 0; l = 3: (7 - 15 + 20 - 12) = 0;
    l = 4: (9 + 15 + 0 - 24) = 0; l = 5: (11 - 15 - 20 + 24) = 0; l = 6: (13 + 15 + 20 + 12) = 60 -> 1;
    l = 7..9: 0; l = 10: 1; l = 11: 0; l = 12: 1; l = 13, 14: 0; l = 15: 1; l = 16: 1.
  - Passt zur Molien-Reihe von I: Harmonische Invarianten (1 + t^15)/((1 - t^6)(1 - t^10)); fuer I_h faellt l = 15
    weg (ungerades l ist unter Inversion ungerade): 1/((1 - t^6)(1 - t^10)) -> l = 0, 6, 10, 12, 16, 18, ...
- Gegenprobe kubisch O (24; E, 8 C3, 3 C2, 6 C4, 6 C2'): n_l = [(2l+1) + 8 chi3 + 9(-1)^l + 6 chi4]/24 mit
  chi4 = 1, 1, -1, -1 (l mod 4): l = 2: 0; l = 3: 0; l = 4: 1; l = 6: 1. Kubische Invarianten bei l = 0, 4, 6, 8, ...

### 2.2 Folge fuer Tensoren

- Ein Tensor der Stufe n zerfaellt unter SO(3) in D_l mit l <= n. Unter I gibt es fuer 1 <= l <= 5 keine Invariante.
  Also ist jeder I-invariante (erst recht I_h-invariante) Tensor bis Stufe 5 SO(3)-invariant, also isotrop. **Der
  Kern von DZ2 ist Mathematik und stimmt.** Stufe 6 hat ein l = 6-Stueck: dort beginnt die Ikosaeder-Struktur.
- Zaehlung je Tensorart (Raum der Tensoren mit den Symmetrien; D-Zerlegung, dann Invarianten SO(3) / O / I):
  - Elastizitaet bzw. TT-Masse M_ijkl (Paar ij, Paar kl, Tausch): Sym^2(D0 + D2) = 2 D0 + 2 D2 + D4
    -> SO(3): 2, O: 3, I: 2. **Ikosaedrisch = isotrop (2 Lame-Konstanten).**
  - Gradiententensor eines Spin-2-Felds K_(ij)(kl)(mn) mit Tausch (ij)<->(kl): (2 D0 + 2 D2 + D4) x (D0 + D2)
    = 4 D0 + 2 D1 + 7 D2 + 3 D3 + 4 D4 + D5 + D6 (126 = 4 + 6 + 35 + 21 + 36 + 11 + 13).
    -> SO(3): 4, O: 4 + 4 + 1 = 9, I: 4 + 1 = 5. **Die "9 gegen 4" der Leitung (TT-ISO-1) ist damit bestaetigt; unter
    I bleiben 5, also EINE ikosaedrische Zusatzinvariante (l = 6).** Das ist Stufe 6, nicht <= 5.
  - Das einzige D6-Stueck in diesem Raum ist der total symmetrische, spurfreie Tensor T (Sym^6 enthaelt D6 genau
    einmal, der K-Raum auch genau einmal). Eichprobe: E(k) = T(.,.,.,.,k,k); E(k)(k x xi + xi x k) = 2 T(.,.,xi,k,k,k)
    verschwindet nicht fuer alle k (sonst T(k,k,k,k,k,k) = 0, also T = 0). Da die Eichbedingung SO(3)-aequivariant ist,
    muss das D6-Stueck allein eichinvariant sein -> **lineare Diffeomorphismen-Invarianz verbietet die l = 6-Steifigkeit.**
  - Licht: Die eichinvarianten Groessen E und B sind Vektoren. Ordnung k^2: Tensor 2. Stufe; k^4-Glied (a2): T_ijkl
    d_k B_i d_l B_j, Stufe 4 -> unter I_h isotrop, auch die Doppelbrechung bei (kl)^4 faellt weg. Erste moegliche
    Anisotropie: k^6-Glied (Stufe 6, l = 6).
  - Phononen (Vektorfeld u ohne Eichung): Ordnung k^4 hat G_ijklmn (Stufe 6) -> l = 6-Anisotropie schon bei k^4.
  - TT-Moden mit eichinvarianter Steifigkeit: Ordnung k^2 isotrop (M Stufe 4, K nur Einstein-Form); Ordnung k^4:
    Kruemmung R_ij (Stufe 2) gibt R W R mit W Stufe 4 -> isotrop; aber die Bewegungsenergie mit Gradient
    d_m K_ij S d_n K_kl (Stufe 6) erlaubt l = 6 bei k^4 [M, vorlaeufig].
- **Vorbehalt [M/H]: Phasonen.** Ein Quasikristall hat zusaetzlich das Phasonfeld w (3 Komponenten im Senkrechtraum,
  Darstellung Gamma_3' = "T2", nicht der Vektor). Kopplung Phonon-Phason ueber das gemeinsame H (5-dim) in
  grad u (A + H) und grad w (G + H). Integriert man w statisch aus, entsteht ein Beitrag k^4/k^2 = k^2 mit einer
  rationalen Richtungsfunktion, die die Senkrechtraum-Struktur traegt (effektiv Stufe 6) -> l = 6-Anisotropie schon
  bei k^2 moeglich, wenn Phasonen mitlaufen. Ob der Koeffizient ungleich null ist, habe ich nicht gerechnet [H].

### 2.3 Erwartung vor den Abrufen (Gesamtbild)

- DZ2 Kern [M] stimmt (s. o.). Die Folgerung "TT-Tempo isotrop" braucht zusaetzlich: Steifigkeit eichinvariant
  (Regge: ja, TT-ISO-1 [P]) und keine mitlaufenden Phasonen. "Licht-a2 isotrop": ja.
- Literatur erwartet: Levine u. a. 1985 (zwei Phonon-, zwei Phason-Konstanten, eine Kopplung); Phasonen diffusiv
  (Lubensky/Ramaswamy/Toner 1985); Danzer 1989 Discrete Math. (vier Tetraeder A, B, C, K, Inflation tau).

## 3. Abrufe (Erwartung mit date VOR dem Abruf; Ausgang danach)

(folgt)

## 4. Erwartungsverstoesse (laufend)

(folgt)

## 5. Gestrichenes

(noch nichts)

## 6. Offene Rueckfragen (wandern mit)

- R1: Will Finn regulaere Tetraeder (Pyrochlor) oder genuegt "raumfuellend aus Tetraedern" (Danzer: vier
  unregelmaessige Sorten)? Ohne Antwort ist "Netz im Sinne Finns" nur bedingt beantwortbar.

### F1 arXiv-API: Danzer-Pflasterung (ABCK)
- **Erwartung (vor dem Abruf, 04:30:31 CEST, date):** 5 bis 20 Treffer, viele zu "Danzer sets" (andere Sache). Mindestens
  ein Abstract nennt Danzers ABCK-Pflasterung mit vier Tetraedern, ikosaedrischer Symmetrie und Inflation (Faktor tau);
  vermutlich auch: Eckenmenge ist eine Modellmenge (Schnitt aus 6D) und lokal gleichwertig (MLD) zu Socolar-Steinhardt.
- Abruf: erster curl-Versuch 04:30:31 ueber http ohne Weiterleitung -> leere Datei (wie bei TETRAEDER-L); zweiter
  Versuch 04:30:36 ueber https mit -L -> quellen/F1-api-danzer.xml (7 Treffer). Gezaehlt als ein Abruf, Selbstanzeige.
- **Ausgang F1: im Kern bestaetigt -> eine Zeile je Quelle.**
  - Al-Siyabi/Koca/Koca 2020 (arXiv:2003.13449, Symmetry 12, 1983): "Vertices of the Danzer's ABCK tetrahedra are
    determined as the fundamental weights of H3", Inflation als Projektion von D6-Gittervektoren "with coefficients from
    Fibonacci sequence"; "The tetrahedron K constitutes the fundamental region of the icosahedral group and generates
    the rhombic triacontahedron" [S Abstract].
  - Gaehler/Hunton/Kellendonk 2008 (arXiv:0809.4442, Z. Kristallogr. 223, 801): Danzer-Pflasterung ist eine kanonische
    Projektionspflasterung (Dimension 3, Kodimension 3), "in some sense, the simplest of all icosahedral tilings";
    Kohomologie mit Torsion [S Abstract]. 2012 (arXiv:1202.2240): Danzer, Ammann-Kramer, kanonische D6-Pflasterungen als
    die Hauptbeispiele ikosaedrischer Muster in R^3 [S Abstract].
  - Nicht im Abstract: "vier Prototile", "aperiodisch", Faktor tau woertlich, flaechengleich (face-to-face), Ecken-
    koordination. -> F2 (Volltext Al-Siyabi u. a.).
  - Nebenfund: Tsiokos 2026 (arXiv:2609.19214), stark aperiodisches 3D-Monotile, "every tiling is homochiral", Symmetrie-
    gruppe hoechstens Ordnung 24; nicht ikosaedrisch, fuer DZ ohne Belang [S Abstract].

### F2 arXiv-PDF 2003.13449 (Al-Siyabi/Koca/Koca 2020), Volltext
- **Erwartung (vor dem Abruf, 04:31:17 CEST, date):** Koordinaten der vier Tetraeder A, B, C, K mit Kanten laengs 2-, 3- und
  5-zaehliger Achsen; Inflation mit tau (A -> mehrere kleinere Kacheln); Kantenlaengen aus einer kleinen Menge; die
  Pflasterung flaechengleich (face-to-face) und mit Spiegelbildern der Kacheln. Keine Physik (Elastizitaet, Phasonen).
- Abruf F2: curl 04:31:17 bis 04:31:18 (date), quellen/F2-2003.13449.pdf, pdftotext -> F2-2003.13449.txt (913 Zeilen).
- **Ausgang F2: Erwartung im Kern bestaetigt, zwei Abweichungen.**
  - Inflation mit tau, Regeln woertlich (Abschn. 3, Ueberschriften Z. 541, 589, 628, 698): "tau K = B + K",
    "tau B = C + 4K + B1 + B2", "tau C = K1 + K2 + C1 + C2 + A", "tau A = 3B + 2C + 6K" [S].
  - Kantenlaengen (Abschn. 3, Z. 392-400): a = sqrt(2+tau)/2, b = sqrt(3)/2, 1 "and their multiples by tau and
    tau^-1, where a, b, 1 are the original edge lengths introduced by Danzer. However, the tetrahedron K has edge
    lengths also involving 1/2, tau/2, tau^-1/2" [S].
  - Spiegelbilder kommen vor: "If we call R1 K = K' as the mirror image of K", Triakontaeder = "60K + 60K'" (Z. 429,
    438) [S] -> die Pflasterung braucht beide Haendigkeiten; Punktgruppe I_h, nicht nur I [ES].
  - Abschn. 4 (Z. 859-860): "Faces of the Danzer tiles are all parallel to the faces of the rhombic triacontahedron; in
    other words, they are all orthogonal to the 2-fold axes" [S].
  - Einleitung (Z. 52-58): Socolar-Steinhardt-Kacheln lassen sich aus ABCK bauen (Danzer/Papadopolos/Talis 1993;
    Roth 1993) [S Zitat]; Original Danzer, Discrete Math. 76, 1-7 (1989) [S Zitat]; Substitutionsmatrix bei Baake/Grimm
    2013, S. 229-235 [S Zitat].
  - **Abweichung 1:** "face-to-face" steht nirgends. Belegt ist nur, dass Flaechen beim Einbau passend aufeinander
    gelegt werden (Z. 545-560). Ob die ganze Pflasterung ein simplizialer Komplex ist, bleibt offen.
  - **Abweichung 2:** Keine Koordinationszahlen, keine Eckenumgebungen. Kein regulaeres Tetraeder unter A, B, C, K
    (Flaechen mit Kanten a, tau a, tau b bzw. tau^-1 a, a, b; Z. 468-469) [S].
- Schreibtisch dazu [M]: Volumen aus den Regeln mit tau^3 = 2 tau + 1: V_B = 2 tau V_K, V_C = 2 tau V_K,
  V_A = 2 tau^2 V_K; Probe tau A: tau^3 * 2 tau^2 = 10 tau + 6 = 3*2tau + 2*2tau + 6 (stimmt). Die Regeln sind also mit
  dem linearen Faktor tau (Volumen tau^3) vertraeglich.

### F3 arXiv-API: Phasonen, Elastizitaet, Hydrodynamik ikosaedrischer Quasikristalle
- **Erwartung (vor dem Abruf, 04:32:21 CEST, date):** Abstracts nennen fuer ikosaedrische Quasikristalle zwei Phonon-Konstanten
  (isotrop), zwei Phason-Konstanten K1, K2 und eine Kopplung K3; Phasonen sind diffusiv (nicht ausbreitend), mit sehr
  langsamer Relaxation (Experiment: Minuten bis Stunden, Francoual u. a.); die EFT-Arbeit Baggioli/Landry 2020 taucht auf.
- Abruf F3: curl 04:32:21 bis 04:32:22 (date), quellen/F3-api-phason.xml (34 Treffer).
- **Ausgang F3: teils bestaetigt, ein Verstoss (voller Zyklus).**
  - Bestaetigt (je eine Zeile): drei Phason-Freiheitsgrade zusaetzlich zum Verschiebungsfeld (Bachteler/Trebin 1998,
    cond-mat/9802???, s. XML) [S Abstract]; Phonon-Phason-Kopplung "usually neglected", relativ "of order 1/10" fuer
    i-AlMn und i-(Al,Cu)Li (Zhu/Henley 1998, cond-mat/9812139) [S Abstract]; dritte Ordnung: "20 independent third-order
    elastic constants" mit Phason-Verzerrung (Ricker/Trebin, J. Phys. A 35, 6953 (2002)) [S Abstract]; Phason diffusiv
    bei langen Wellen, "diffusion-to-propagation crossover", weil Phason-Verschiebungen "symmetries of the system with no
    associated Noether currents" sind, "compatible with the EFT description only because of the presence of dissipation
    (finite temperature) and the lack of periodic order" (Baggioli/Landry, SciPost Phys. 9, 062 (2020)) [S Abstract].
  - Nicht im Abstract: "isotrope Phonon-Elastizitaet" woertlich. -> braucht eigene Quelle (F5).
  - **Verstoss V1:** Mendoza-Coto/Bonifacio/Piazza 2024 (arXiv:2407.21230), bosonische Quanten-Quasikristalle (ohne
    Dissipation, Phasonen als Goldstone-Moden mit konjugierter Dichte): dodekagonal und dekagonal "isotropic speed of
    sound"; oktagonal "the coupling between phononic and phasonic degrees of freedom leads in turn to hybridization ...
    and an anisotropic speed of sound" [S Abstract]. Erwartet hatte ich: Quasikristall-Symmetrie -> isotroper Schall,
    Phasonen nur als Zusatzmoden. Korrigierte Erwartung: **Isotropie bis Stufe 5 gilt fuer die Phonon-Tensoren; laufen
    Phasonen als Goldstone-Moden mit und koppeln, kann der Schall schon in fuehrender Ordnung richtungsabhaengig werden**
    (2D oktagonal gezeigt; in 2D macht 8-zaehlig den Tensor 4. Stufe isotrop [M], die Anisotropie kommt also allein aus
    der Kopplung). Das trifft meinen Vorbehalt aus 2.2 (Phasonen) und macht ihn von [H] zu "in 2D belegt, in 3D
    ikosaedrisch offen". -> voller Zyklus: Volltext F4.
  - Nebenfunde: K2 wechselt mit sinkender Temperatur das Vorzeichen, K2/K1 -> -0,7 nahe einer Phason-Instabilitaet
    (Mihalkovic/Henley 2002, cond-mat/0205271?) [S Abstract]; Coddens 2004/2006: "phason waves" seien unnoetig und
    "violate many physical principles" (Gegenposition) [S Abstract]; Surowka 2021 (PRB 103, 201119): ebene Quasikristall-
    Elastizitaet als duale Eichtheorie, Defekte als Fraktonen [S Abstract]; De Donno u. a. 2025 (PRR 6, 043285):
    mesoskalige Amplituden-Feldtheorie, dissipativ [S Abstract].
  - Zusatz aus F3 (ohne neuen Abruf): Ricker/Bachteler/Trebin 2001 (cond-mat/0111395, EPJB 23, 351): "Starting from the
    solution for elastic isotropy in phonon and phason spaces, corrections of higher order reflect the two-, three- and
    fivefold symmetry" [S Abstract]. Zuordnung der IDs: Bachteler/Trebin = cond-mat/9802201, Ricker/Trebin =
    cond-mat/0209401, Mihalkovic/Henley = cond-mat/0205271 (oben mit ? markiert, jetzt geprueft).

### F4 arXiv-PDF 2407.21230 (Mendoza-Coto/Bonifacio/Piazza), Volltext (voller Zyklus zu V1)
- **Erwartung (vor dem Abruf, 04:34:00 CEST, date):** Die oktagonale Anisotropie kommt aus einem Phonon-Phason-Kopplungsterm,
  den die 8-Zaehligkeit erlaubt; beim Dodekagon verschwindet die Kopplung aus Symmetrie, beim Dekagon in ihrem Modell
  ebenfalls oder erst hoeher. Winkelmuster cos(8 theta). Phasonen laufen als Goldstone-Moden mit eigener Geschwindigkeit.
  3D-ikosaedrisch wird nicht behandelt.
- Abruf F4: curl 04:34:00 bis 04:34:01 (date), quellen/F4-2407.21230.pdf -> .txt (831 Zeilen).
- **Ausgang F4 (voller Zyklus): Erwartung teils verletzt, Verstoss V1 geschaerft.**
  - Dodekagonal: "the absence of the coupling between phonons and phasons"; fuenf masselose Moden, isotrop (S. 3,
    linke Spalte, Z. 139-161) [S].
  - Dekagonal: Kopplung vorhanden, trotzdem "two groups of three and two modes, respectively, all with isotropic
    dispersion relations" (S. 3, rechte Spalte, Z. 139-148) [S]. **Meine Erwartung "Kopplung allein -> Anisotropie" ist
    damit falsch.**
  - Oktagonal: "the structure of the elasticity action characterized by an anisotropic phason contribution and a
    finite phonon-phason coupling produces anisotropic dispersion relations ... with propagation speed c_s that depend
    on the orientation of the momentum q when q -> 0"; ausserhalb der Symmetrieachsen hat jede Mode einen laengs- und
    einen quer-Anteil (Z. 148-162) [S]. Schluss: "due to the phonon-phason coupling, the octagonal QC structure develops
    an anisotropic speed of sound" (Z. 256-261) [S].
  - Modell: zweidimensional, bosonisch, ohne Dissipation; Phasonen sind masselose Moden ("five gapless extended low
    energy excitation modes", Z. 254-255) [S]. 3D-ikosaedrisch nicht behandelt (wie erwartet).
  - **Korrigierte Erwartung (protokolliert):** Anisotropie in fuehrender Ordnung braucht beides: eine Phason-
    Steifigkeit, die selbst richtungsabhaengig ist, UND eine Kopplung an die Phononen. [M/ES fuer 3D:] Ikosaedrisch ist
    die Phason-Steifigkeit (K1, K2) eine 3x3-Matrix im Senkrechtraum; ihre Invarianten sind Polynome in n; die
    Determinante ist vom Grad 6 und darf das l = 6-Stueck enthalten. Fuer K1 und K2 allgemein erwarte ich deshalb eine
    richtungsabhaengige Phason-Steifigkeit (wie oktagonal), fuer eine besondere Wahl (G- und H-Teil gleich steif) eine
    isotrope. Gerechnet ist das nicht [H]. Stuetze: Ricker/Bachteler/Trebin 2001 rechnen "starting from ... elastic
    isotropy in phonon and phason spaces" und bekommen Korrekturen hoeherer Ordnung mit 2-, 3- und 5-zaehliger Symmetrie
    [S Abstract, F3] -> Isotropie im Phason-Raum ist dort die nullte Naeherung, nicht die Regel.

### F5 freie Verlagsseite: Spoor/Maynard/Kortan 1995, PRL 75, 3462 (Abstract)
- **Erwartung (vor dem Abruf, 04:34:47 CEST, date):** Gemessen (Resonanz-Ultraschall): ikosaedrisches AlCuLi elastisch isotrop
  innerhalb der Messgenauigkeit (Groessenordnung 1e-3 oder besser); die kubische Naeherungsphase (R-Phase) messbar
  anisotrop. Das waere Kategorie (a), gemessen.
- Abruf F5: WebFetch 04:34:5x (nach date 04:34:47), Auszug in quellen/F5-spoor-1995-abstract-webfetch.md.
- **Ausgang F5: bestaetigt -> eine Zeile.** "the AlCuLi quasicrystal is isotropic within 0.07%, significantly more
  isotropic than any conventional crystal (by 10 standard deviations)"; "a closely related cubic phase of AlCuLi is
  slightly, but measurably, anisotropic" [S Abstract, WebFetch-Auszug]. Kategorie (a) gemessen; Genauigkeit 7e-4, nicht
  1e-15.

### F6 arXiv-API: Feldtheorie, Raumzeit, Lorentz auf Quasikristallen (auch 24-Monats-Pruefung, Regel 7)
- **Erwartung (vor dem Abruf, 04:35:17 CEST, date):** Wenige Arbeiten (unter 30). Erwartet: Boyle/Dickens/Flicker 2020
  (konforme Quasikristalle, Holografie), QGR-Gruppe (Amaral/Clawson/Irwin), vielleicht "Spacetime quasicrystals"
  (Boyle/Mygdalas, Quasikristalle im Minkowski-Raum mit diskreter Lorentz-Symmetrie) [L?]. Keine Arbeit, die
  Schwerewellen- oder Licht-Isotropie eines ikosaedrischen Raumnetzes gegen Messgrenzen rechnet.
- Abruf F6: curl 04:35:17 bis 04:35:18 (date), quellen/F6-api-raumzeit-qk.xml (24 Treffer, nach Datum sortiert,
  neuester 2026-01-12).
- **Ausgang F6: bestaetigt -> je eine Zeile; eine Datumskorrektur meiner [L?].**
  - Boyle/Mygdalas, "Spacetime Quasicrystals", arXiv:2601.07769 (2026): selbstaehnliche Quasikristalle "from Euclidean
    space to Minkowski spacetime", "the first examples of such Lorentzian quasicrystals"; Bezug zur Wirklichkeit
    ausdruecklich "(speculative)" [S Abstract]. Mein [L?] hatte 2022 vermutet; richtig ist Januar 2026.
  - Boyle/Dickens/Flicker 2020 (PRX 10, 011009): Diskretisierung konformer Feldtheorien auf "conformal quasicrystals",
    erhaelt "an infinite discrete subgroup of the global conformal group at the cost of lattice periodicity" [S Abstract].
  - Holographic Foliations (arXiv:2408.15316, 2024): Randgeometrie regulaerer hyperbolischer Pflasterungen ist eine
    selbstaehnliche Substitutionspflasterung; {3,5,3} gibt einen 2D-Rand-Quasikristall mit 5-zaehligen Punkten [S Abstract].
  - Amaral/Clawson/Irwin 2023 (arXiv:2306.01964): quasikristalline Spin-Schaeume (EPRL-Variante), 600-Zelle,
    Fermionen [S Abstract].
  - Randstaendig: f(Q)-Kosmologie mit "quasicrystalline topological phases" (Vacaru-Linie, 2410.03700, 1803.04810 u. a.),
    "Lorentz and gauge invariance of quantum space" (Ali u. a., IJMPA 38 (2023)) [S Abstract/Titel]; ohne Rechnung zur
    Isotropie eines Raumnetzes.
  - **Regel 7:** Eine Arbeit, die Licht- oder Schwerewellen-Isotropie eines ikosaedrischen Raumnetzes gegen Messgrenzen
    rechnet, fand diese Abfrage nicht: nach Recherchestand nicht belegt (nicht: "gibt es nicht").

### F7 arXiv-API (Gegensweep): lange Wellen, Bloch, Ausbreitung in Quasikristallen
- **Erwartung (vor dem Abruf, 04:36:38 CEST, date):** In 1D-Fibonacci-Ketten Cantor-Spektrum mit Luecken auf allen Skalen
  und "kritischen" Zustaenden; trotzdem bei langen Wellen eine wohldefinierte Schallgeschwindigkeit. In ikosaedrischen
  Legierungen (Neutronen) scharfe akustische Phononen bei kleinem q, Verbreiterung erst bei groesserem q. Kein Hinweis,
  dass langwelliger Schall in 3D gestoert waere.
- Abruf F7: curl 04:36:38 (date), quellen/F7-api-langwellig.xml (10 Treffer).
- **Ausgang F7: teils bestaetigt, teils nicht gefunden.**
  - Bestaetigt (gemessen, Neutronen): Verbreiterung akustischer Moden in Quasikristallen; Modell: bei kleinem q stoert
    der Schall fast dispersionslose optische Cluster-Moden ("Akhiezer"), bei groesserem q "strong hybridization of
    acoustic and optical modes ... can no longer be described as a single acoustic mode with a well defined wave vector"
    (de Boissieu/Currat/Francoual/Kats, cond-mat/0312163) [S Abstract]. Gegenposition: Coddens (cond-mat/0506600) [S
    Abstract]. Breitere Moden bei nicht-primitiver Zelle (Kats/Muratov, cond-mat/0502673) [S Abstract].
  - Elektronen: "another type of breakdown of the semi-classical Bloch-Boltzmann theory", anomale Quantendiffusion
    (cond-mat/0701639) [S Abstract].
  - Nicht gefunden: Cantor-Spektrum der Fibonacci-Kette (bleibt [L]).
  - [M, Nebenfund am Schreibtisch, angeregt durch die Fermion-Frage]: Der lineare Aufspaltungsterm a1 des Weyl-Operators
    auf Finns Diamant (LICHT-FINN-NETZ-1: a1 = +-(b/sqrt3)|q x n|, null laengs Achsen und Raumdiagonalen) hat die Form
    eines Tensors 3. Stufe d_ijk k_j k_k (T_d-Invariante |eps_ijk|, "xyz", l = 3). Unter I ist der einzige invariante
    Tensor 3. Stufe eps_ijk, und eps_ijk k_j k_k = 0. **Ein ikosaedrisches Netz verbietet diesen Term.** Bedingung: Der
    Fermion-Operator hat dort ueberhaupt einen Kegel bei k = 0 (offen, [H]).

### F8 arXiv-API (letzter Abruf): Richtungsabhaengigkeit der Phason-Steifigkeit, ikosaedrisch
- **Erwartung (vor dem Abruf, 04:37:37 CEST, date):** Abstracts nennen anisotrope diffuse Streuung um Bragg-Reflexe, deren Form
  vom Verhaeltnis K2/K1 der Phason-Konstanten abhaengt (de Boissieu u. a., Letoublon u. a., Jaric/Nelson); d. h. die
  Phason-Steifigkeit ist ikosaedrisch richtungsabhaengig, isotrop nur fuer K2 = 0.
- Abruf F8: curl 04:37:37 bis 04:37:38 (date), quellen/F8-api-phason-aniso.xml (4 Treffer). Damit 8 von 8 Abrufen.
- **Ausgang F8: Erwartung nicht getroffen (nicht gefunden, kein Widerspruch).** Die Arbeiten zur anisotropen diffusen
  Streuung (de Boissieu u. a.) sind nicht unter den Treffern. Gefunden: Newman/Henley 1995 (PRB 52, 6386):
  Zufallspflasterung der ikosaedrischen Phase, "the two fundamental elastic constants" (Phason), verknuepft mit
  "diffuse scattering wings near Bragg peaks" [S Abstract]; i-R-Cd: Reflexverbreiterung "dominated by frozen-in phason
  strain" (arXiv:1406.4522) [S Abstract, gemessen]; Jagannathan/Szallas 2013 (EPJB 86, 76): Phason-Flips als
  Geometrie-Fluktuationen erzeugen eine anisotrope Casimir-artige Kraft ~1/d [S Abstract].
- Kein Abruf mehr frei. Die Richtungsabhaengigkeit der ikosaedrischen Phason-Steifigkeit pruefe ich am Schreibtisch.

## 2.4 Schreibtisch nach den Abrufen [M]: Phason-Steifigkeit und Kopplung ikosaedrisch (04:38 bis 04:41)

- Konstruktion: sechs 5-zaehlige Achsen a_i (Parallelraum) und ihre Bilder b_i (Senkrechtraum, Galois tau -> -1/tau);
  6D-Orthogonalitaet gibt b_i.b_j = -a_i.a_j fuer i != j (Probe: a_A = (0,1,tau)/N, a_B = (0,-1,tau)/N gibt +1/sqrt5,
  die Bilder (0,1,-1/tau), (0,-1,-1/tau) geben -1/sqrt5).
- T1 x T2 = G + H. Die Matrizen E_i = a_i x b_i spannen genau H auf (Summe = 0, weil T1 x T2 keine Invariante hat);
  Gram-Matrix (6/5) I - (1/5) J, also Projektion P(X) = (5/6) sum_i E_i <E_i, X>.
- H-Teil der Phason-Steifigkeit fuer eine ebene Welle w e^{iqx}: B(n) = (5/6) sum_i (a_i.n)^2 b_i b_i^T.
  Kontrollen: tr B = 5/3 (G-Teil 4/3, Verhaeltnis 5:4 wie die Dimensionen).
  - laengs 5-zaehlig: Spektrum (1, 1/3, 1/3); laengs 3-zaehlig: (1/9, 7/9, 7/9); laengs 2-zaehlig: (0,127; 0,873; 0,667).
  - tr B^2 = 11/9 in allen drei Richtungen (wie verlangt: Grad 4, keine l = 4-Invariante); tr B^3 = 1,074 / 0,942 /
    0,963 -> **richtungsabhaengig (l = 6).** Die beiden Achsspektren sind genau die zwei Loesungen von tr = 5/3,
    tr^2 = 11/9 mit zweifachem Eigenwert.
  - Phason-Steifigkeit K_G (|q|^2 - B) + K_H B: **isotrop nur fuer K_G = K_H**, sonst l = 6-anisotrop.
- Kopplung: einziger Weg ueber H; Intertwiner a_i a_i^T <-> a_i x b_i (Schur): C = R sum_i (a_i^T eps a_i)(a_i^T grad w b_i),
  fuer ebene Wellen u^T X(q) w mit X(q) = sum_i (a_i.q)^2 a_i b_i^T.
  - Laengsanteil |X^T q^|^2 = |sum_i (a_i.q)^3 b_i|^2: 5-zaehlig 16/25 = 0,64; 2-zaehlig 0,160; 3-zaehlig 144/2025 =
    0,071; Kugelmittel 0,274 (Paarformel <(a.q)^3(a'.q)^3> = (9c + 6c^3)/105).
  - **Folge [M]: Werden Phasonen statisch mitrelaxiert oder laufen sie mit, wird der Laengsschall schon in fuehrender
    Ordnung l = 6-anisotrop, auch bei isotroper Phason-Steifigkeit (K_G = K_H).** Groesse ~ R^2/(K (lambda + 2 mu)) x
    O(1); mit Zhu/Henleys "of order 1/10" waeren das Promille bis Prozent [H, Abschaetzung].
  - Abgleich mit F4 (2D): dekagonal isotrop, oktagonal anisotrop. In 2D ist der Phason-Raum ein m = 3-Darstellungsraum;
    die Kopplungskorrektur bleibt dort ohne die oktagonale Zusatzkonstante isotrop. In 3D sitzt T2 in l = 3, deshalb reicht
    die Kopplung allein. Das ist eine Lesart, nicht an einer Quelle geprueft [ES].
- Warum Spoor u. a. trotzdem 0,07 % messen [ES]: Ultraschall ist viel schneller als die Phason-Relaxation (diffusiv,
  Baggioli/Landry; F3), die Phasonen sind eingefroren -> nur der Tensor 4. Stufe zaehlt -> isotrop. Unterscheidungspunkt:
  statische (relaxierte) gegen schnelle Elastizitaet.

## 4. Erwartungsverstoesse (Stand 04:43, wichtigste zuerst)

1. V1 Phasonen sind der Moderator der Isotropie, nicht nur Zusatzmoden (F3, F4, Schreibtisch 2.4).
2. V2 TT-Steifigkeit ist Stufe 6; die Stufe-5-Regel deckt sie nicht; Rettung nur ueber Eichinvarianz (Schreibtisch 2.2).
3. V3 Danzer: keine regulaeren Tetraeder, Spiegelbilder noetig, face-to-face nicht belegt (F2).
4. Klein: F4 dekagonal isotrop trotz Kopplung (meine Teil-Erwartung falsch); F8 nicht gefunden; F6 Datum 2026 statt 2022.

## 5. Gestrichenes

- ~~"Kopplung Phonon-Phason allein macht den Schall anisotrop" (allgemein)~~ -> in 2D dekagonal falsch (F4); fuer 3D
  ikosaedrisch am Schreibtisch neu begruendet (2.4), dort [M].
- ~~"Spacetime quasicrystals (Boyle/Mygdalas), etwa 2022" [L?]~~ -> arXiv:2601.07769, Januar 2026 (F6).

## 7. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | Gemessene Quasikristalle sind isotrop, also waere es ein Danzer-Raumnetz auch | ja (F5, F4, 2.4) | nur mit eingefrorenen Phasonen; laufen sie mit und koppeln, l = 6 in fuehrender Ordnung |
| G2 | Die Stufe-5-Regel deckt alle Groessen der Karte ab | ja (2.2) | nein: TT-Steifigkeit Stufe 6, Phason-Kopplung effektiv Stufe 6; Licht-a2 ja |
| G3 | Die Phason-Steifigkeit ist ikosaedrisch isotrop (wie die Phonon-Steifigkeit) | ja (2.4) | nein, ausser K_G = K_H; Spektren (1, 1/3, 1/3) gegen (1/9, 7/9, 7/9) |
| G4 | Danzer ist ein simplizialer Komplex (face-to-face), also Regge-tauglich | nein (kein Abruf frei) | offen; F2 belegt nur Flaechenanpassung beim Einbau |
| G5 | Lange Wellen sind auf Quasikristallen wohldefiniert | teils (F7) | Schall bei kleinem q ja (gemessen), Verbreiterung bei groesserem q; Elektronen: Bloch-Boltzmann bricht |
| G6 | Isotrop im Netz-Ruhesystem heisst isotrop | nein, [ES] | Ruhesystem bleibt wie beim Kristall; bewegte Beobachter sehen O(v)-Richtungsabhaengigkeit |
| G7 | Die Mittelung ueber eine Pflasterung traegt die I_h-Symmetrie der LI-Klasse | nein, [L] | nicht geprueft |

## 8. Abschluss

- DOSSIER.md geschrieben ab 04:43:47, Abgabe 2026-10-05 04:48:01 CEST (date). Keine weiteren Abrufe.
