# MESS-3A (Neustart) - AFM-Baelle, Kanalstruktur, Plan Kanal-Test

Auftrag der Leitung claude-primary, RUNDE-11 nach v3, explorativ. Neustart nach Abbruch 13:30.
Start dieses Laufs: 2026-09-30 19:41:07 CEST (per date). Zeitbox 40 min.

## BERICHT

Bericht begonnen 2026-09-30 20:02:08 CEST (per date). Markierungen: [A] an der Quelle gelesen (Volltext per
pdftotext, grep/sed-Lesung), [S] nur Suchtreffer (arxiv.org/search ueber WebFetch-Zusammenfassung), [L?] Gedaechtnis,
[T] aus der Teildatei, [ES] eigener Schluss, [H] Hypothese. WebSearch war erschoepft (200 von 200), die arXiv-API
meldete "Rate exceeded"; die 24-Monats-Suche lief deshalb nur ueber arxiv.org/search.

### 1 Kurzfazit

1. **Einwand haelt, staerker als formuliert:** 2U/sin^2 theta = 1 identisch, also kein nichttopologischer Ball in
   keiner Dimension, in d = 1 nur Waende [ES]; seit 1983 als "specific degeneracy" bekannt (Bar'yakhtar/Ivanov) [A].
2. **Feld entlang der Achse hilft nicht:** nur Omega = omega + h (Nietz Gl. 5 [A]; B-I 1983 [A]).
3. **3D-Baelle traegt Anisotropie vierter Ordnung, konkav in sin^2 theta** (w_a = -K1 cos^2 - K2 cos^4, K2 > 0;
   kappa = -K2/(K1+2K2) < 0): Fenster Omega^2 in (1 + kappa, 1), dort U_Omega(pi/2) < 0. 3D stabil fuer
   omega_1 < omega < omega_* (B-I 1983 [A]), 3D gedaempft (Nietz 2010 [A]), 2D getrieben (Ovcharov 2023 [A]).
4. **Kanalstruktur wie bei uns:** offen 1 - Omega, geschlossen 1 + Omega [ES]; rho ~ m + omega ~ 2 m liegt am oberen
   AFMR-Zweig. Die woertliche Scheiterregel wird voraussichtlich von Innenraum-Volumenzustaenden bestanden.
5. Gemessen: kein praezedierender AFM-Ball, nur AFMR-Frequenzen und Spin-Flop-Felder.

### 2 Erwartungsverstoesse (das Wichtigste zuerst)

1. **Der Klassiker ist frei lesbar und enthaelt Einwand, Loesung und Stabilitaet** (gegen V0-E5 und Teildatei-E4:
   "bleibt [L?]"). Bar'yakhtar/Ivanov, JETP 58, 190 (1983), Archiv-PDF mit OCR:
   - reine sin^2-Anisotropie: Frequenz unabhaengig von der Amplitude, "degeneracy ... appears also in the properties
     of solitons and vanishes upon consideration of the more general form of the anisotropy energy";
   - 3D-kugelsymmetrische Solitonen mit zweitem Anisotropieparameter; N(omega) divergiert an beiden Fensterenden,
     "stable at omega_1 < omega < omega_* and unstable at omega_* < omega < omega_0" (Lyapunov-Methode);
   - 3He-A mit festem l: Leggett-Gleichungen "coincide literally" mit der AFM-Gleichung.
   Korrigierte Erwartung: Der Einwand ist 43 Jahre alt; neu waere bei uns nur die Innenmoden-Frage.
2. **Nicht das Feld nahe Spin-Flop und nicht DM oeffnen das Fenster** (gegen die Kandidatenliste der Leitung und
   teils gegen V0-E2).
   - Nietz setzt explizit K2 = 140 Oe neben K1 = 700 Oe, also kappa = -0,2. Das Feld tritt nur als omega + h auf [A].
   - In 2609.32059 verengt DM das Fenster ("suppress the Q-ball window through the same combination, D^2 + omega^2").
     Geoeffnet wird es dort durch den in n_z linearen Term h cos theta: "always built over the metastable,
     higher-energy polar background" [A].
   - Gemeinsamer Nenner [ES]: Ein AFM-Q-Ball ist immer eine praezedierende Blase einer zweiten, fast entarteten
     Phase. Das Fenster in Omega ist das Metastabilitaetsfenster der AF-Phase. Seine Breite 1 - sqrt(1 + kappa) ist
     gleich der Restluecke des unteren AFMR-Zweigs am Spin-Flop-Feld.
3. **Die woertliche Scheiterregel aus MESS-2 ist fuer den AFM fast vorentschieden** (Schreibtisch [ES], teils gegen
   die Annahme in MESS-2, sie trenne).
   - Im Duennwandball ist das Innere Spin-Flop-Phase. Ovcharov [A]: "gapless branch", Wellen unter omega_AFMR
     "localized inside the soliton".
   - Der nackte geschlossene Kanal hat dort Volumenzustaende ab rho ~ sqrt(|kappa|/2). Das liegt ueber der offenen
     Schwelle 1 - Omega <= |kappa|/2 + O(kappa^2), die Zustaende sind also eingebettet.
   - Die Regel wird deshalb voraussichtlich bestehen, ohne etwas ueber einen Wandzustand zu sagen (vgl. die
     "Volumenzustaende ohne Leiter" in R10). Die Karte fuehrt deshalb einen getrennt markierten Wandzustands-Test [H].
4. Kleiner: Nietz behauptet "stable precessing exitations at presence of dissipative member" (EBS-1). Das folgt aus
   seiner Naeherungsgleichung (7). Ungetrieben mit Gilbert-Daempfung sinkt die Energie bei omega != 0 monoton [L?].
   Ich halte die Aussage fuer fraglich [ES].
5. FeF2: keine Quelle gefunden (drei arXiv-Suchen leer). Die Zahlen bleiben [L?].

### 3 Literaturstand mit Quellen

- Reines Modell, Entartung: Bar'yakhtar/Ivanov 1983 [A]; Ovcharov u. a. 2023: "simple quadratic anisotropy (in the
  form -K1 Mz^2) does not provide nonlinear coupling between magnons in AFMs" [A].
- Eigene Pruefung (Frage 1) [ES]:
  - Derrick (2 - d) G = d (1 - Omega^2) V ist richtig. In d = 1 folgt aus T'^2 = (1 - Omega^2) sin^2 T nur die Wand
    0 -> pi. Die Teildatei [T] kommt unabhaengig zum selben Schluss.
  - Mit Feld nur Omega = omega + h. Das gilt nach dem Larmor-Satz auch im Zweiuntergitter-Landau-Lifshitz-Modell,
    solange es um z symmetrisch ist.
- 3D existent und teils stabil: B-I 1983 [A] (konservativ, Lyapunov, dN/domega); Nietz 2010 [A] (Zweiuntergitter mit
  K1, K2, Gl. 5 kugelsymmetrisch, Daempfung Q = 0,02; keine Linearisierung, kein "Q-ball"). 2D: Ovcharov 2023 [A]
  (Film, Nanokontakt, Spinstrom, Haematit mit Ru/Rh; 213/192 GHz).
- Neuere Arbeiten (24 Monate, nur arXiv, [S]): nichts zu praezedierenden AFM-Baellen; einzig 2609.32059 (1D, chiral,
  [A] lokal). Eingebettete Innenmoden praezedierender AFM-Solitonen: nach Recherchestand nicht belegt.
- Material [A]: MnF2 mu0 H_A = 0,82 T, mu0 H_E = 47,05 T, H_SF ~ 9,4 T (Vaidya u. a. 2020); Cr2O3 Spin-Flop ~ 6 T,
  AFMR 170 GHz (Seki u. a. 2015); Haematit: K2-Form "reported to describe magnetic anisotropies in hematite", alpha =
  1,1e-5 (Ovcharov, zitiert).

### 4 Regime und Moderatoren

- Entartet (kappa = 0, reines Sigma-Modell; MnF2/Cr2O3 in fuehrender Ordnung) gegen quartisch (kappa < 0; Haematit,
  Nietz, B-I). Moderator: relative Anisotropie vierter Ordnung. Die Quellen widersprechen sich nicht; sie
  stichproben verschiedene kappa.
- Konservativ (B-I, Nietz Gl. 5) gegen getrieben-dissipativ (Ovcharov). Moderator: Daempfung gegen Spinstrom.
- In der Familie: Duennwandast (Spin-Flop-Innenraum, stabil nach B-I) gegen Dickwandast (Omega -> 1, kubisch-NLS-
  artig, instabil nach B-I). Moderator Omega. Fuer die Leiter zaehlt vermutlich nur der Duennwandast [H].
- Zweiuntergitter-Korrekturen [ES, unbelegt]: kappa_eff ~ -H_A/H_E (MnF2 ~ -0,017), vom Vorzeichen her wie K2.
  Gleiche Ordnung wie andere vernachlaessigte Terme, also nicht tragfaehig.

### 5 Unterscheidungspunkte

- Entartet gegen quartisch: Restluecke des unteren AFMR-Zweigs am Spin-Flop-Feld. Entartet sagt 0 vorher, quartisch
  (1 - sqrt(1 + kappa)) omega_0 [ES]; zugleich die Fensterbreite. Zweiter Weg: Frequenzverschiebung grosser
  Praezessionskegel, Omega^2 = 1 + 2 kappa sin^2 theta; messbar erst bei Kegelwinkeln nahe 90 Grad.
- AFM wie KG (eingebetteter Wandzustand bei rho ~ 1 + Omega) gegen AFM wie NLS (keiner): trennt sich im
  Duennwandast; am Dickwandende laufen beide zusammen. Genau das misst die Karte (Abschnitt R, Punkt 9).
- Konservative Existenz gegen Nietz' gedaempftes Gleichgewicht: dE/dt < 0 bei omega != 0 ohne Antrieb (LLG) [L?].

### 6 Gegensweep-Befunde

- Geprueft: DM als Kandidat -> nein, verengt (2609.32059 [A]). "Nichttopologisch" -> ja (B-I: Stabilitaet "not by
  the presence of a topological charge" [A]).
- Nicht geprueft: exakte U(1)-Symmetrie in echten Kristallen (Anisotropie in der Ebene, DM in Haematit); Daempfung
  gegen Resonanzschmalheit (MnF2-Linienbreiten nicht gelesen); Gueltigkeit des Sigma-Modells im Innenraum und fuer
  kleine Baelle; kappa_eff aus Zweiuntergitter-Korrekturen.

### 7 Kalibrierung

- (a) Gemessen: AFMR-Frequenzen und Spin-Flop-Felder (Seki, Vaidya). Kein praezedierender AFM-Ball, keine Innenmode.
- (b) Nuetzlich verdichtet: Larmor plus Coleman ergibt Fenster = Metastabilitaetsfenster = Restluecke; Zwei-Kanal-
  Struktur mit cos-Theta-Coriolis-Term; Laborzuordnung geschlossen = oberer AFMR-Zweig. Alles [ES], ungegengelesen.
- (c) Gewachsene Gewissheit ohne neue Evidenz: "AFM ist der Laborkandidat" wurde im Lauf fester, waehrend die
  Bedingungen enger wurden (kappa < 0 noetig, Wandzustand unbekannt, Daempfung, U(1)-Bruch). **Warnzeichen.**

### 8 Offene Fragen

- O1 Bindet die Wand einen Zustand des geschlossenen Kanals nahe 1 + Omega (Karte R)?
- O2 Wie gross ist kappa in MnF2, Cr2O3 und Haematit? Mit Quelle belegt ist die K2-Form nur fuer Haematit.
  Gemessene Restluecke am Spin-Flop?
- O3 Stoert die Anisotropie in der Ebene die Ladungserhaltung (Lebensdauer des Balls)?
- O4 Nietz' Formel "h < 1 - k2/k1 ~ 0,8944": fehlt die Wurzel nur in der Textextraktion?

### 9 Laborbezug (Frage 5; Zahlen mit Quelle, Umrechnungen [ES, Handrechnung])

| Material | Beleg | omega_0 = m | rho ~ 2 m (mitdrehend) | Laborkomponenten nahe Spin-Flop |
|---|---|---|---|---|
| Cr2O3 | Spin-Flop ~ 6 T, AFMR 170 GHz [A Seki] | 0,17 THz | ~0,34 THz | geschl. ~ omega_0 + gamma H ~ 0,34 THz |
| MnF2 | H_A 0,82 T, H_E 47,05 T, H_SF ~ 9,4 T [A Vaidya] | ~0,25 THz [ES] | ~0,5 THz | ~0,5 THz |
| Haematit (dotiert, Modell) | 213/192 GHz, kappa ~ -0,19 [A Ovcharov + ES] | 0,213 THz | ~0,43 THz | Spin-Flop nicht belegt; bei H = 0 Ball 192-213 GHz, geschl. ~ 0,21 THz, offen ~ 0,6 THz [ES] |
| FeF2 | keine Quelle gefunden | [L?] ~1,6 THz | [L?] | [L?] |

- Kappa ist nur fuer das Haematit-Modell belegt. Bei MnF2 und Cr2O3 ist ohne K2 das Fenster (Restluecke) unbekannt.

### 10 Quellenliste

- Bar'yakhtar, I. V.; Ivanov, B. A. (1983): Dynamic solitons in a uniaxial antiferromagnet. Sov. Phys. JETP 58, 190.
  http://www.jetp.ras.ru/cgi-bin/dn/e_058_01_0190.pdf [A], sha256 82a66207...
- Nietz, V. V. (2010): Precessing equilibrium and overcritical solitons at a spin-flop phase transition.
  https://arxiv.org/abs/1005.2049 [A], sha256 2d51c6fc...
- Ovcharov, R. V.; Hamdi, M.; Ivanov, B. A.; Akerman, J.; Khymyn, R. (2023): Antiferromagnetic droplet soliton driven by
  spin current. https://arxiv.org/abs/2311.18583 [A], sha256 f2ac9b9f...
- Balseyro Sebastian, Ohashi, Nitta (2026): Magnetic Q-balls. https://arxiv.org/abs/2609.32059 [A, grep, Kopie
  MESS-2], sha256 f0e9bcd5...
- Seki, S. u. a. (2015): Thermal generation of spin current in an antiferromagnet. https://arxiv.org/abs/1508.02555
  [A, grep], sha256 7ff6c012...
- Vaidya, P. u. a. (2020): Sub-Terahertz Spin-Pumping from an Insulating Antiferromagnet.
  https://arxiv.org/abs/2005.01203 [A, grep], sha256 7f0334c6...
- Kosevich, Ivanov, Kovalev (1990): Magnetic Solitons. Phys. Rep. 194, 117 [nur als Zitat in 2311.18583].
- Foner (1963), Phys. Rev. 130, 183 [nur als Zitat bei Nietz].

---

## ARBEITSFELD

### V0 - Vorab-Erwartungen, 2026-09-30 19:41:07 CEST (per date)

Geschrieben, BEVOR ich die Teildatei MESS-3A.abgebrochen-1330.md, die Texte in quellen/ oder die
Hintergrunddateien RUNDE-10/RUNDE-11 gelesen habe. Grundlage nur der Auftragstext und Gedaechtnis [L?].

- E1 (Einwand, Sigma-Modell): Der Einwand haelt fuer das reine einachsige AFM-Sigma-Modell. Er ist
  sogar staerker: U(theta) = (1/2) sin^2 theta ist genau der Grenzfall, in dem 2U/sin^2 theta konstant
  ist. Das Coleman-Kriterium (Q-Ball, wenn min 2U/sin^2 < m^2) ist dann nie erfuellt, auch nicht in
  d = 1: dort gibt es nur praezedierende Domaenenwaende (theta laeuft 0 -> pi), keine lokalisierten
  nichttopologischen Loesungen. Erwarte in d = 1 nur Wand und (planar, ohne Praezession)
  Sine-Gordon-Breather.
- E2 (Feld entlang der leichten Achse): Im Sigma-Modell ist das Feld entlang z eine reine
  Larmor-Verschiebung omega -> omega - gamma H; Derrick bleibt mit (1 - (omega - omega_H)^2). Das Feld
  allein hilft im Sigma-Modell nicht. Erwarte: Es hilft erst jenseits des Sigma-Modells, ueber die
  Korrekturen der Ordnung H_A/H_E, die den Spin-Flop erster Ordnung machen (effektiver Term
  b sin^4 theta mit b < 0). Dann existieren 3D-Baelle als praezedierende Spin-Flop-Blasen in einem
  schmalen Fenster der Breite ~ gamma (H_c - H_sf) ~ gamma H_sf H_A/(2 H_E) unter dem unteren Magnonzweig.
- E3 (welcher Term macht U_omega negativ): (a) vierte Ordnung Anisotropie mit K2 < 0;
  (b) effektiver Quartterm nahe Spin-Flop (Zweiuntergitter-Modell, nicht Sigma-Modell);
  (c) Ferrimagnet/Unkompensation (Berry-Term erster Ordnung, U_omega(pi) = -2 s omega < 0, wie FM-Magnon-
  Tropfen); (d) DM-Kopplung aendert die Derrick-Skalierung (Gradient erster Ordnung), wirkt aber bei
  radialsymmetrischer Konfiguration mit ortsunabhaengiger Phase nicht (DM-Energie ist dann Randterm) [ES].
- E4 (Nietz 2010, arXiv:1005.2049): Erwarte numerische Loesungen der Zweiuntergitter-Landau-Lifshitz-
  Gleichungen, kugelsymmetrisch in 3D, Kern mit Spin-Flop-artiger Struktur, praezedierend mit
  Frequenz nahe gamma H; Stabilitaet nicht streng untersucht; kein Q-Ball-Bezug im Text; vermutlich
  im Umfeld von Nietz' "precessing ball solitons" beim Phasenuebergang im Ferromagneten.
- E5 (Klassiker KIK 1990): Erwarte, dass Kosevich/Ivanov/Kovalev feststellen, dass im Sigma-Modell des
  einachsigen AFM nichttopologische praezedierende Solitonen in 2D/3D fehlen und in 2D nur topologische
  (Skyrmion-artige) praezedierende Solitonen existieren. Nur [L?], nicht tragend.
- E6 (neuere Arbeiten 2024-2026): Erwarte wenig direkt Passendes; eher STT-getriebene (dissipative)
  AFM-Tropfen, Ferrimagnet-Tropfen, AFM-Skyrmionen, Oszillonen. Konservative 3D-AFM-Q-Baelle
  erwarte ich hoechstens vereinzelt. "Magnetic Q-balls" (arXiv:2609.32059) laut Auftrag 1D.
- E7 (Kanalstruktur): Wegen U(1)-Symmetrie um z und zweiter Zeitordnung gibt es wie beim komplexen
  Klein-Gordon-Q-Ball zwei Kanaele mit Schwellen rho = m - omega (offen) und rho = m + omega (geschlossen).
  Im Zweiuntergitter-Modell sind das die beiden AFMR-Zweige omega_(+/-) = gamma (H_c +/- H). rho ~ m + omega
  entspricht im Labor dem oberen Magnonzweig; ob die Wand dort bindet, ist offen (muss gerechnet werden).
  Erwarte: da der Q-Ball im AFM immer im Bereich omega/m nahe 1 lebt (schmales Fenster), ist der
  Ball schwach nichtlinear ausser nahe Spin-Flop; die Bindung im geschlossenen Kanal ist fraglich.
- E8 (Labor): MnF2 H_sf ~ 9,3 T, AFMR ~ 0,26 THz; FeF2 H_sf ~ 41-42 T, AFMR ~ 1,6 THz; Cr2O3 H_sf ~ 6 T,
  AFMR ~ 0,16-0,17 THz [alles L?, muss belegt werden]. rho ~ m + omega laege im Bereich des oberen Zweigs,
  also ~ 0,2-0,5 THz (MnF2, Cr2O3) bzw. > 1,5 THz (FeF2).
- E9 (Teildatei): Erwarte, dass der abgebrochene Lauf Nietz gelesen hat und die Derrick-Rechnung
  bestaetigt; 1508.02555, 2005.01203, 2311.18583 kenne ich nicht - Erwartung je Quelle vor dem Lesen.

### V0b - Hintergrund gelesen, Nachtrag Erwartungen, 2026-09-30 19:43:09 CEST (per date)

Gelesen (lokal, noch VOR Teildatei und quellen/): RUNDE-10/nls-leiter/ERGEBNIS.md Abschnitte 0 und 3; MESS-2.md Bericht
(Kurzfazit, K5, T1) und Zeilen 440-526; RUNDE-11.md Abschnitt MESS-2 mit Nachtrag 13:14:37 und Abschnitte
Unterbrechung/Fortsetzung. Nichts davon aendert E1-E9. Zusaetzlich vorab, als eigene Handrechnung [ES, nicht geprueft]:

- E10 (Larmor exakt): Auch im vollen Zweiuntergitter-Landau-Lifshitz-Modell mit Achse und Feld entlang z ist eine
  Praezession mit omega in Feld H dasselbe wie ein statischer Zustand im Feld H' = H -/+ omega/gamma (Larmor-Satz).
  Praezedierende Baelle = statische kritische Keime (Blasen) im Feld H'. Die gibt es in d >= 2 nur, wenn im Feld H'
  eine Phase tiefer liegt als die AF-Phase, also H_sf < H' < H_c (metastabiles Fenster des Spin-Flops erster
  Ordnung). Fensterbreite gamma (H_c - H_sf) ~ gamma H_sf H_A / (2 H_E): fuer MnF2 grob 2 GHz [L?-Zahlen].
- E11 (Kanalgleichungen, Sigma-Modell): In den Tangentialkoordinaten u = delta theta, v = sin(Theta) delta phi im
  mitdrehenden System lauten die linearen Gleichungen
  u_tt - lap u + [U''(Theta) - omega^2 cos 2Theta] u - 2 omega cos(Theta) v_t = 0,
  v_tt - lap v + [lap(sin Theta)/sin Theta] v + 2 omega cos(Theta) u_t = 0.
  Kreisbasis w = u + i v ist der geschlossene Kanal (Schwelle rho = 1 + omega), w~ = u - i v der offene (rho = 1 - omega);
  Kopplung (V_u - V_v)/2, die im Vakuum verschwindet. Anders als beim KG-Q-Ball steht im Diagonalterm 2 omega rho
  cos(Theta) statt 2 omega rho: die Kugelgeometrie gibt dem geschlossenen Kanal einen zusaetzlichen anziehenden Topf
  -2 omega rho (1 - cos Theta). Erwartung: Die Scheiterregel greift beim AFM eher NICHT, weil die offene Schwelle
  1 - omega im AFM-Fenster (omega nahe 1) winzig ist; entscheidend ist dann, ob ueberhaupt ein gebundener Zustand
  unter 1 + omega existiert.

### T0 - Teildatei gelesen (ungepruefte Vorarbeit), Abgleich mit V0

Kennzeichnung ab hier: **[T]** = steht in MESS-3A.abgebrochen-1330.md, von mir noch nicht an der Quelle geprueft.
- [T] D1 (Derrick, d = 1 nur Wand, Coleman 2W/|psi|^2 = 1, Larmor mit Feld, Zusatzterme i-iv) deckt sich mit meinen
  vorab geschriebenen E1-E3 und E10. Unabhaengig ist das nicht in jeder Hinsicht (gleiches Modellhaus), aber zeitlich
  vorab getrennt: meine V0 entstand ohne Kenntnis der Teildatei.
- [T] Nietz 1005.2049: Zweiuntergitter-Energie mit K1 und NEGATIVEM Term vierter Ordnung, 3D kugelsymmetrisch,
  Frequenz und Feld nur als Summe omega + h; EBS/overcritical PBS; keine Linearisierung; kein "Q-ball". -> pruefen.
- [T] 2311.18583 (Ovcharov/Hamdi/Ivanov/Akerman/Khymyn 2023): woertliches Zitat "simple quadratic anisotropy ... does
  not provide nonlinear coupling between magnons in AFMs"; Vorschlag hoeherer Anisotropie nach KIK 1990 und
  Bar'yakhtar/Ivanov 1983 (JETP 58, 190); Fenster omega_c < omega < omega_AFMR; Innenraum als Spin-Flop-Hohlraum. -> pruefen.
- Sha256-Abgleich Teildatei gegen meine Rechnung (sha256sum 19:43): 1005.2049.pdf 2d51c6fc4855e8cd... = gleich;
  2311.18583.pdf f2ac9b9f4b1b71bb... = gleich. 1508.02555 und 2005.01203 stehen in der Teildatei nicht (nach 13:26
  geladen, nicht mehr protokolliert).
- Was die Teildatei NICHT hat: Kanalstruktur (Frage 3), Rechenkarte (Frage 4), Laborzahlen mit Quelle (Frage 5),
  24-Monats-Suche. Meine E10 (exakter Larmor im Zweiuntergitter-Modell) und E11 (Kanalgleichungen) sind dort nicht.

### F1 - Abrufprotokoll (Erwartung vor jedem Abruf; bestaetigt = eine Zeile)
- Q0 (zwischen 19:43:52 und 19:46:11, per date eingegrenzt) Textpruefung der Quellen in quellen/: pdftotext -layout der vier PDFs erneut erzeugt (Scratchpad), sha256
  identisch mit den gespeicherten .txt (1005.2049 83c733f5..., 1508.02555 e2b0a07b..., 2005.01203 8bab17a1...,
  2311.18583 57b1fc57...). PDF-sha256: 1005.2049 2d51c6fc..., 1508.02555 7ff6c012..., 2005.01203 7f0334c6...,
  2311.18583 f2ac9b9f.... arXiv-Stempel im Text vorhanden (z. B. "arXiv:1508.02555v1 ... 11 Aug 2015",
  "arXiv:2311.18583v1 ... 30 Nov 2023"). Damit sind die .txt treue Auszuege der PDFs.
- N1 (vor 19:46:11) Nietz 2010, 1005.2049 [A]. Erwartung E4 + [T]. Befund: bestaetigt, mit Detail:
  - Energie Gl. (1): Zweiuntergitter (l, m), Anisotropie + K1/2 (m_perp^2 + l_perp^2) - K2/4 (m_perp^2 + l_perp^2)^2,
    Feld H_z; Bewegung Gl. (2)-(3) mit Daempfung Gamma. Gl. (5), kugelsymmetrisch 3D (Term 2/r):
    q'' + (2/r) q' + q q'^2/(1 - q^2) = q (1 - q^2)(1 - (omega + h)^2 - 2 (k2/k1) q^2), q = |l_perp| = sin theta.
  - Handabgleich [ES]: Mit q = sin theta ist das exakt die Profilgleichung des Sigma-Modells mit
    U = (1/2)(sin^2 theta + kappa sin^4 theta), kappa = -k2/k1, Omega = omega + h. Feld und Frequenz nur als Summe
    (Larmor, E10 bestaetigt). Nietz: K1 = 700 Oe, K2 = 140 Oe (kappa = -0,2), B = 4,9e6 Oe, Q = 0,02, "typical for
    antiferromagnetic crystals", Quelle [4] = Foner, Phys. Rev. 130, 183 (1963). Ob K2 aus Foner stammt, sagt der
    Text nicht.
  - Existenz: h < 1 "equilibrium PBS" (EBS-1 praezedierend, EBS-2 omega = 0 fuer h* ~ 0,996 < h < 1); h > 1 bzw.
    h < "1 - k2/k1 ~ 0,8944" (Rueckflop) "overcritical PBS". 0,8944 = sqrt(0,8): vermutlich fehlt in der
    Textextraktion ein Wurzelzeichen [ES, nicht am Bild geprueft]. Q-Ball-Fenster in Omega: Omega^2 in (1 + kappa, 1)
    = (0,8; 1); das ist genau das Metastabilitaetsfenster der AF-Phase [ES].
  - "Q-ball", "Coleman", Linearisierung, Innenmoden: nicht im Text (grep leer).
  - **Kleiner Verstoss gegen E2:** Nietz braucht keinen Zweiuntergitter-Korrekturterm ~H_A/H_E; er setzt K2 explizit.
    Das Feld nahe Spin-Flop ist bei ihm nur Rahmen (Larmor), nicht die Ursache. Die Ursache ist K2 < 0 im Sinn
    der Konkavitaet in sin^2 theta.
  - Zweifel [ES]: "stable precessing excitations at presence of dissipative member" (EBS-1, omega -> 0,0058) stammt
    aus der Naeherungsgleichung (7). Mit Gilbert-Daempfung und ohne Antrieb nimmt die Energie bei omega != 0
    monoton ab (Lyapunov-Eigenschaft von LLG [L?]); ein ungetriebener, gedaempfter, stationaer praezedierender
    Zustand widerspraeche dem. Fuer unsere Frage unerheblich (konservative Existenz folgt aus Gl. 5).
- N2 (vor 19:46:11) Ovcharov/Hamdi/Ivanov/Akerman/Khymyn, arXiv:2311.18583 (2023) [A]. Erwartung [T]. Bestaetigt woertlich:
  "Contrary to ferromagnets, simple quadratic anisotropy (in the form -K1 Mz^2) does not provide nonlinear coupling
  between magnons in AFMs. It was proposed in Refs. 31 and 32 to employ higher-order terms in the anisotropy energy
  density as w_a = -K1 cos^2 theta - K2 cos^4 theta, K1, K2 > 0 (1) to stabilize droplets". Ref. 31 = Kosevich/
  Ivanov/Kovalev, Phys. Rep. 194, 117-238 (1990); Ref. 32 = Bar'yakhtar/Ivanov, JETP 58, 190 (1983); Ref. 33 =
  Galkina/Ivanov (Ueberblick). Fenster omega_c < omega < omega_AFMR, omega_c^2 = (omega_AFMR^2 + omega_SF^2)/2;
  Profilgleichung mit (1/r)-Term, also 2D-Film; "in this central area theta ~ pi/2 ... local region of a spin-flop
  state, for which the magnon spectrum has a gapless branch. Thus, for omega < omega_AFMR these SWs are localized
  inside the soliton, and they can propagate outside it only at omega > omega_AFMR". Beispiel 213/192 GHz (Ru/Rh-
  dotiertes Haematit); "predicted theoretically a long time ago31-33 in the case of zero damping". Handabgleich
  [ES]: -K2 cos^4 = const + 2K2 s - K2 s^2 (s = sin^2), also kappa = -K2/(K1 + 2K2), 1 + kappa = (omega_c/
  omega_AFMR)^2: dieselbe Coleman-Grenze wie bei Nietz.
- N3 (vor 19:46:11) Seki u. a. 2015, arXiv:1508.02555 [A, grep]. Erwartung: Materialarbeit, Spin-Flop-Feld. Bestaetigt:
  Cr2O3, H || [001] "larger than Hc ~ 6 T causes a spin-flop transition" (T = 40 K); "antiferromagnetic resonance
  frequency 170 GHz (= nu+-(0))".
- N4 (vor 19:46:11) Vaidya u. a. 2020, arXiv:2005.01203 (Science 2020) [A, grep]. Erwartung: MnF2 sub-THz. Bestaetigt:
  MnF2, omega_res = gamma mu0 sqrt(H_A(2H_E + H_A)) +- gamma mu0 H (H < H_SF), H_SF = sqrt(2 H_E H_A);
  Fit mu0 H_A = 0,82 T, mu0 H_E = 47,05 T; "spin-flop (SF) transition (at mu0 H_SF ~9.4 T)"; Messungen bei 240 und
  395 GHz.
- Erwartungen vor den Web-Abrufen (19:46:17 per date):
  - W1 (24-Monats-Suche AFM-Q-Ball/-Tropfen 2024-2026): wenige Treffer; Folgearbeiten zu Ovcharov 2023 (Haematit,
    dissipativ, 2D), eventuell Ferrimagnet- oder Altermagnet-Tropfen; kein konservativer 3D-AFM-Q-Ball mit
    Linearisierung/Innenmoden.
  - W2 (Bar'yakhtar/Ivanov 1983, JETP 58, 190, Archiv jetp.ras.ru): Volltext zugaenglich; zeigt, dass
    praezedierende Solitonen im einachsigen AFM erst mit Anisotropie vierter Ordnung (oder in 1D) existieren.
  - W3 (FeF2): H_sf ~ 41-42 T, AFMR ~ 1,5-1,6 THz (52-53 cm^-1).
  - W4 (Haematit unterhalb Morin, K2): K2-Term belegt (Morrish), AFMR ~ 0,2 THz, Spin-Flop ~ 6-7 T.
- W-S1 (nach 19:46:31) WebSearch: Kontingent erschoepft ("200 of 200"), keine Suche ausgefuehrt. arXiv-API per curl:
  "Rate exceeded." (api-M2.xml, api-M3.xml je 14 Byte, nur diese Meldung; api-M1.xml nicht angelegt). Ausweg:
  WebFetch auf arxiv.org/search (sortiert nach Datum) und jetp.ras.ru.
- W1a (WebFetch arxiv.org/search "antiferromagnetic droplet soliton", Abstract-Suche, neueste zuerst) [S, ueber
  Zusammenfassungsmodell]: nur 3 Treffer: 2609.32059 (Magnetic Q-balls, 25.09.2026, quasi-1D chiral, AFM und FM, DMI
  + leichte Achse), 2311.18583 (2023, oben), 2008.00475 (Spinor-BEC, fremd). Erwartung W1 bestaetigt, eine Zeile.
- W2 (WebFetch jetp.ras.ru, dann curl PDF) **Bar'yakhtar/Ivanov 1983, "Dynamic solitons in a uniaxial
  antiferromagnet", Sov. Phys. JETP 58 (1), 190-197** [A, OCR-Text der Archiv-PDF, grep/sed-Lesung].
  quellen/baryakhtar-ivanov-1983-jetp58-190.pdf sha256 82a662078f084fb8..., .txt 84ae6ccd45b098a8....
  Erwartung W2 bestaetigt, aber mit mehr Gehalt als erwartet (voller Zyklus):
  - Woertlich: "If we choose the anisotropy energy in the simplest form beta(l_x^2 + l_y^2)/2 = (beta/2) sin^2 theta,
    as is usually done in uniaxial magnetics, we then obtain the result that the frequency of the nonlinear wave of
    arbitrary amplitude does not depend on the value of the amplitude ... a specific degeneracy of the AFM as a
    nonlinear system ... This degeneracy appears also in the properties of solitons and vanishes upon consideration
    of the more general form of the anisotropy energy." -> Das ist der Einwand der Leitung, 1983 formuliert.
  - Feld: Mit Phi = phi - gHt sind die Gleichungen Lorentz-invariant; "at H != 0, it is essential to assume that the
    AFM is uniaxial and that w_a does not depend on phi" -> Larmor-Aussage (E10) belegt [A].
  - Modell: Anisotropie mit zwei Parametern (beta, b bzw. omega_0, omega_1), b > 0 macht den Spin-Flop erster Ordnung
    ("H_c determines the field of the first-order transition"); OCR der Gleichungen (9), (11) unleserlich, die
    Lesart w_a = (beta/2) sin^2 - (b/4) sin^4 ist mein Schluss aus dem Kontext [ES].
  - 3D kugelsymmetrische Solitonen existieren; N(omega) -> unendlich fuer omega -> omega_1 (Duennwand) und
    omega -> omega_0 (Dickwand), dN/domega wechselt bei omega_* das Vorzeichen: "the soliton is stable at
    omega_1 < omega < omega_* and unstable at omega_* < omega < omega_0" (Lyapunov-Methode). "Thus the
    three-dimensional solitons in AFM are stable over a wide range of frequencies". 1D: "stable at all achievable
    values of omega".
  - Schluss des Papiers: 3He-A mit festem l: Leggett-Gleichungen "coincide literally with the equation for the
    antiferromagnetism vector" -> Bruecke zu den 3He-Q-Baellen (MESS-2) [A].
  - Linearisierung/Innenmoden oberhalb der Luecke: nicht behandelt (nur Stabilitaet ueber N(omega)).
- W1b (WebFetch arxiv.org/search "antiferromagnet soliton precession", Abstract, neueste zuerst) [S]: kein Treffer
  2024-2026; neuester 2311.18583. W1c ("Q-ball magnon") [S]: nur 3He-Arbeiten (2007-2017) und 1103.3148; kein AFM.
  Erwartung W1 bestaetigt, eine Zeile. Urteil fuer "3D-AFM-Q-Ball mit Linearisierung/Innenmoden": nach Recherchestand
  (nur arXiv-Suche ueber Zusammenfassungsmodell) nicht belegt - nicht "gibt es nicht".
- W3 (FeF2) [S]: arxiv.org/search "FeF2 spin-flop" 0 Treffer, "FeF2 antiferromagnetic resonance" 1 fremder Treffer,
  "FeF2 magnon terahertz" 0 Treffer. **Erwartung W3 nicht pruefbar**: FeF2-Zahlen bleiben [L?], tragen nichts.
- G-Pruefung (20:00:09) 2609.32059 lokal (mess2/quellen, sha256 f0e9bcd59fce4e6d = MESS-2-Eintrag) [A, grep]:
  V(theta) = (m^2/2) sin^2 theta + h cos theta (Gl. II.6); DM senkt nur die effektive Achse, delta = m^2 - D^2;
  "the DM coupling and the rotation frequency suppress the Q-ball window through the same combination, D^2 + omega^2";
  "for h != 0, the antiferromagnetic polar Q-ball is always built over the metastable, higher-energy polar
  background"; 3D nur ueber "rotating helical reduction" auf 1D (Anhang A). **Erwartungsverstoss gegen die
  Kandidatenliste der Leitung:** DM oeffnet das Fenster nicht, es verengt es; das Fenster oeffnet der in n_z lineare
  Term h cos theta. In einem kompensierten AFM koppelt ein homogenes Feld nicht linear an n (Symmetrie n -> -n);
  ein solcher Term braucht Unkompensation (Ferrimagnet) oder ein gestaffeltes Feld [ES, nicht an Quelle geprueft].

### K - Kanalstruktur (Frage 3), Schreibtisch [ES], nicht gegengelesen

- Modell, das 3D-Baelle traegt (B-I 1983, Nietz 2010, Ovcharov 2023 in 2D): Sigma-Modell mit
  U = (1/2)(s + kappa s^2), s = sin^2 theta, -1 < kappa < 0; Einheiten omega_0 = 1, c = 1; Feld entlang z nur ueber
  Omega = omega + h. Existenz (Coleman): Omega^2 in (1 + kappa, 1). U_Omega(pi/2) = (1/2)(1 - Omega^2 + kappa) < 0 genau
  in diesem Fenster. Statischer Spezialfall omega = 0: thermodynamischer Spin-Flop bei h_sf = sqrt(1 + kappa)
  (Nietz: 0,8944 = sqrt(0,8)); Restluecke des unteren AFMR-Zweigs dort 1 - sqrt(1 + kappa) = Fensterbreite in Omega.
- Linearisierung im mitdrehenden System (u = delta theta, v = sin Theta delta phi, Zeitfaktor e^{-i rho t}):
  V_u = U''(Theta) - Omega^2 cos 2Theta,  V_v = cot(Theta) U'(Theta) - Omega^2 cos^2 Theta - Theta'^2,
  geschlossen (w = u + i v):  [-lap + (V_u+V_v)/2 + 2 Omega rho cos Theta - rho^2] w + C w~ = 0,
  offen (w~ = u - i v):       [-lap + (V_u+V_v)/2 - 2 Omega rho cos Theta - rho^2] w~ + C w = 0,  C = (V_u - V_v)/2.
  Vakuum: (V_u+V_v)/2 -> 1 - Omega^2, C -> 0; Schwellen rho = 1 + Omega (geschlossen) und 1 - Omega (offen).
  **Ja, dieselbe Zwei-Kanal-Struktur wie bei uns** (U(1) um z, zweite Zeitordnung). Unterschied zum KG-Q-Ball: Faktor
  cos Theta am Coriolis-Term, also Zusatztopf -2 Omega rho (1 - cos Theta) im geschlossenen Kanal.
- Laborzuordnung (Nietz-Konvention, Laborfrequenz = mitdrehende - h): geschlossene Komponente Omega - rho ~ -1 ->
  Labor |.| = 1 + h = oberer AFMR-Zweig omega_0 + gamma H; offene Komponente Omega + rho ~ 3 -> Labor ~ 3 - h.
- rho ~ m + omega: Die geschlossene Schwelle liegt bei 1 + Omega ~ 1,9 bis 2 (Omega im Fenster 0,89 bis 1 fuer
  kappa = -0,2). Ein Wandzustand dort ist der Baustein aus R10 (KG: rho_c ~ 2 m). Die offene Schwelle 1 - Omega ist
  <= 0,106 (kappa = -0,2) bzw. <= 0,009 (kappa = -0,017): fast jeder gebundene Zustand des geschlossenen Kanals ist
  eingebettet. Erreichbar ja; ob die Wand dort bindet, ist ungerechnet.
- **Schreibtischrechnung zur Scheiterregel (Pflicht, Vertrag darf nicht selbsterfuellend sein):** Duennwand-Innenraum
  Theta = pi/2 (Spin-Flop-Phase): cos Theta = 0, V_v = 0, V_u = Omega^2 - 1 - 2 kappa, also naktes Innenpotential
  (Omega^2 - 1 - 2kappa)/2 - rho^2 >= |kappa|/2 - rho^2. Volumenzustaende beginnen bei rho ~ sqrt(|kappa|/2)
  (0,32 bzw. 0,09) und damit UEBER der offenen Schwelle (0,106 bzw. 0,009): eingebettet. Das passt zu Ovcharov [A]
  ("gapless branch" im Innern, Wellen unter omega_AFMR "localized inside the soliton"). Folge: Die woertliche Regel
  wird fuer duennwandige Baelle voraussichtlich NICHT greifen, weil Volumenzustaende sie bestehen lassen - wie die
  "Volumenzustaende ohne Leiter" der dicken NLS-Solitonen in R10. Offen bleibt nur, ob ein Wandzustand unter
  1 - Omega der tiefste ist (die Wand hat einen Topf ~ (kappa - Theta'^2)/2 < 0). Vorhersage: Regel greift nicht,
  ~80 %; Informationswert gering. Deshalb in der Karte ein zweiter, getrennt markierter Wandzustands-Test [H].

### R - Rechenkarte AFM-KANAL-1 fuer einen Code-Agenten (Frage 4; NICHT gerechnet)

1. Modell: L = (1/2)(d_t n)^2 - (1/2)|grad n|^2 - U, U = (1/2)(s + kappa s^2), s = 1 - n_z^2; 3D radial, l = 0.
   Quellenbindung: Profilgleichung = Nietz Gl. (5) mit q = sin Theta, kappa = -k2/k1 [A]; Anisotropieform = Ovcharov
   Gl. (1) mit kappa = -K2/(K1 + 2K2) [A + ES]. Feld nur ueber Omega (Larmor, B-I 1983 [A]).
2. Profil: Theta'' + (2/r) Theta' = sin Theta cos Theta [1 - Omega^2 + 2 kappa sin^2 Theta], Theta'(0) = 0,
   Theta(inf) = 0; Schiessen auf Theta(0) in (0, pi/2] oder Newton-Relaxation. Ladung N = Omega int sin^2 Theta d^3x;
   dN/dOmega < 0 markiert den stabilen Ast (B-I: stabil fuer omega_1 < omega < omega_*).
3. Kanaele: Formeln aus Abschnitt K. Pflicht vor jeder Zahl: Formeln selbst neu herleiten (L bis zur 2. Ordnung
   entwickeln) und die Leitungsfassung hier nur als Vergleich nehmen.
4. Kopplung aus: C = 0. Nackter geschlossener Kanal: H_c(rho) = -d^2/dr^2 + W(r; rho), u = r w, Dirichlet bei 0
   und R_max, W = (V_u+V_v)/2 + 2 Omega rho cos Theta - rho^2 (symmetrisch tridiagonal). Gesucht: alle rho_c in
   (0, 1 + Omega) mit lambda_k(rho_c) = 0 (Raster in rho, dann Bisektion), fuer die untersten k <= 5.
   Eingebettet, wenn 1 - Omega < rho_c < 1 + Omega. Zu jedem Zustand Wandanteil F_w = Gewicht in |r - R_w| < 2 delta
   (R_w: Theta = Theta(0)/2, delta: Wandbreite); Wand, wenn F_w > 0,5.
5. Kontrollen: (K0) kappa = 0: Profil-Loeser muss "keine Loesung" melden. (K1) Theta = 0: kein gebundener Zustand,
   Kante 1 - (rho - Omega)^2. (K2) Positivkontrolle: KG-Q-Ball-Kanal aus nls2.py (E = 0,706 bei omega^2 = 0,7977)
   im selben Codepfad. (K3) Formelprobe mit Kopplung an: Phasenmode v = sin Theta loest [-lap + V_v] v = 0 (l = 0),
   Translationsmode u = Theta' loest [-lap + 2/r^2 + V_u] u = 0 (l = 1); Residuum < 1e-6 auf beiden Gittern.
6. Familie: kappa in {-0,017 (MnF2-artig, nur [ES]), -0,05, -0,10, -0,19 (Ovcharov 213/192 GHz), -0,20 (Nietz)};
   Omega^2 = 1 + kappa + f |kappa|, f in {0,1; 0,2; 0,35; 0,5; 0,7; 0,85; 0,95} (7 Werte, 35 Profile).
   R_max = max(3 R_w, R_w + 25/sqrt(1 - Omega^2)); Mitglieder mit R_max > 3000 vorab ausgeschlossen und benannt.
7. Gitter: h = 0,02 und h = 0,01 (radial, wie R10). Aufwand [Schaetzung]: Code 1-2 h Agentenzeit; Rechnung
   tridiagonal O(N) je Eigenwert, <= 10 min je Gitterstufe auf der Kleintest-Spur (.69, kleintest.sh).
8. **Scheiterregel (woertlich aus MESS-2):** "Liegt der tiefste Zustand des geschlossenen Kanals auf zwei Gitterstufen
   fuer die ganze Familie nicht im offenen Kontinuum, ist der Kandidat verworfen."
9. **Zusatz der Feldforschung, getrennt markiert [H], nicht Teil der Leitungsregel:** Dieselbe Pruefung fuer den
   tiefsten WANDzustand (F_w > 0,5). Grund: Abschnitt K, die woertliche Regel wird voraussichtlich von
   Volumenzustaenden des Spin-Flop-Innenraums bestanden. Liegt auf zwei Gitterstufen fuer die ganze Familie kein
   Wandzustand im offenen Kontinuum, ist der AFM als Leiterkandidat im Sinn von R10 verworfen, auch wenn Regel 8
   besteht. Nur wenn ein eingebetteter Wandzustand existiert, folgt die W-Gitter-Suche mit Kopplung wie in R10.
10. Vorab-Vorhersage (vor jeder Rechnung): Regel 8 besteht (~80 %); Wandzustand nahe rho ~ 1 + Omega im
    Duennwandast eingebettet (~55 %); Dickwandende (Omega -> 1) verhaelt sich NLS-artig (~70 %).

### G - Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 **geprueft:** "DM-Kopplung ist ein Kandidatenterm" (Leitung, Teildatei iv). 2609.32059 [A, grep]: DM verengt
  das Fenster (delta - omega^2); geoeffnet wird es durch h cos theta ueber metastabilem Pol. Befund oben.
- G2 **geprueft:** "Die Baelle sind nichttopologisch". B-I 1983, Schlusssatz [A]: Stabilitaet "determined not by the
  presence of a topological charge". Bestaetigt.
- G3 nicht geprueft: exakte U(1)-Symmetrie um die Achse. Reale Kristalle haben Anisotropie in der Ebene (tetragonal
  MnF2, trigonal Cr2O3/Haematit) und Haematit DM. Beides bricht oder verformt die Ladungserhaltung; ungerechnet.
- G4 nicht geprueft: Daempfung gegen Schmalheit. Haematit alpha = 1,1e-5 nur als Zitat in Ovcharov (Ref. 50);
  MnF2-Linienbreite (Kotthaus/Jaccarino, zitiert bei Vaidya) nicht gelesen.
- G5 nicht geprueft: Gilt das Sigma-Modell (zweite Ordnung) noch im Spin-Flop-Innenraum mit m ~ H/H_E und fuer kleine
  Baelle (Quantisierung, B-I: N ganzzahlig)? Ebenso mein Schluss kappa_eff ~ -H_A/H_E aus dem Zweiuntergitter-Modell
  (E10): an keiner Quelle belegt.

### Ende

- Lauf beendet 2026-09-30 20:03:42 CEST (per date). Neue Dateien in quellen/: baryakhtar-ivanov-1983-jetp58-190.pdf (sha256 82a662078f084fb8), .txt (sha256 84ae6ccd45b098a8). Teildatei unveraendert (sha256 cb74d0d5d33167f4).
