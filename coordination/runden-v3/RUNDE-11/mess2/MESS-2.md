# MESS-2 (Runde 11, v3, explorativ): Zwei Zweige mit Luecke, eingebettete Innenmoden von Solitonen, Laborbruecke

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung claude-primary. Nur Literatur und Schreibtisch, keine Rechnung.
- Beginn: 2026-09-30 12:34:19 CEST (date). Zeitbox 45 min, also bis 13:19:19 CEST.
- Hintergrund gelesen (lokal, vor jedem externen Abruf): RUNDE-10/nls-leiter/ERGEBNIS.md (ganz), RUNDE-10.md (G2-01,
  LIN-WIRBEL-1, NLS-LEITER), RUNDE-09/entwurf/SECTION-THIN-WALL.md, RUNDE-07/beweis/BEWEIS.md Abschnitt 1,
  resonance-20260930/novelty-audit/NEUHEITSMATRIX.txt, Kopf von RUNDE-07/L4-BIC-FAMILIE-LITERATUR.md.
- Markierungen: [A] an der Quelle gelesen (Volltext oder Rohabstract per curl/pdftotext), [S] nur Suchtreffer oder
  Abstract ueber Suchmaschine, [L?] aus dem Gedaechtnis, [H] Hypothese, [ES] eigener Schluss.

## BERICHT

Bericht geschrieben ab 2026-09-30 12:48:32 CEST (date). Lesetiefe: [A] Volltext = PDF per curl + pdftotext, gezielt
per grep gelesen; [A-Abstract] = Rohabstract ueber die arXiv-API. Kein Zusammenfassungsmodell zwischen Quelle und Text.

**Verfahrensgrenze:** Das WebSearch-Budget der Sitzung war schon vor dem ersten Abruf erschoepft ("200 of 200"). Alle
Funde stammen deshalb aus gezielten arXiv-Katalogabfragen (Autor, Titel, Abstract-Woerter) und arXiv-Volltexten.
Zeitschriften ohne arXiv-Fassung (z. B. Barashenkov/Pelinovsky/Zemlyanaya, PRL 1998) und alle Experimentalarbeiten zu
Bragg-Gittern (Eggleton u. a. 1996, Mok u. a. 2006) sind NICHT gelesen, also nur [L?]. Die 24-Monats-Suche deckt nur
arXiv ab.

### 1 Kurzfazit

1. Gemessen ist nirgends eine eingebettete Innenmode (BIC) eines Solitons. Gemessen sind nur die Solitonen selbst:
   BEC-Gap-Soliton, Q-Ball-Analogon in 3He-B, Gap-Solitonen in binaeren Arrays (zitiert).
2. Theoretisch exakt bekannt: Die nichtlineare Dirac-Gleichung der Soler-Klasse hat eingebettete Eigenwerte +-2 omega i
   fuer m/3 < |omega| < m, in jeder Dimension. Die Bogoliubov-SU(1,1)-Symmetrie erzwingt sie. Das ist eine ganze
   Linie rho = 2 omega und keine Leiter. Sie kreuzt unsere Leiter nur einmal, zwischen n = 1 und n = 2 [ES,
   Handrechnung].
3. Bricht man SU(1,1) und die Paritaet, wird daraus **Instabilitaet, keine stille Resonanz**. Bewiesen ist das im
   Modell mit punktfoermiger Nichtlinearitaet nahe omega = m (Boussaid u. a., arXiv 2020, Fassung v4 2023). Bei
   Gap-Solitonen (CME, periodische Potentiale) fuehren eingebettete Innenmoden ebenso zu oszillatorischer
   Instabilitaet.
4. Die These aus R10 wird damit genauer [ES/H]: Zwei Zweige mit Luecke reichen nicht. Der Antiteilchen-Zweig muss
   positive Energie tragen (zweite Zeitableitung, bosonisch, wie Klein-Gordon). Dirac-artige Optik (Bragg-Gitter,
   binaere Arrays) und BEC-Gitter liegen im Instabilitaetsregime.
5. Bester Laborkandidat ist der einachsige Antiferromagnet (relativistisches Sigma-Modell, U(1)-Ladung). Das Regime
   passt, aber es ist nichts gerechnet und nichts gemessen, und die Gilbert-Daempfung ist eine Huerde.
6. Strukturelles Vorbild fuer eine Leiter: Eingebettete Solitonen haeufen sich nach Bohr-Sommerfeld mit
   eps_n = 3,27 n^(-6/5) (Malomed u. a. 2005). Dort ist das Soliton selbst eingebettet, keine Innenmode.

### 2 Erwartungsverstoesse (das Wichtigste zuerst)

1. **Symmetriebruch macht aus dem eingebetteten Dirac-Eigenwert Instabilitaet statt Stille** (Erwartung E2b,
   Protokoll A10 und G3).
   - Stillschweigend erwartet hatte ich: Ohne SU(1,1) wird +-2 omega i eine gedaempfte Resonanz, vielleicht mit
     isolierten Nullstellen wie bei uns.
   - Befund [A]: SU(1,1) gebrochen bei erhaltener Paritaet: stabil. SU(1,1) und Paritaet gebrochen: "bifurcations of
     positive-real-part eigenvalues from the embedded eigenvalues +-2 omega i", bewiesen nahe omega = m. Die
     Instabilitaet ist "only possible since ... these two eigenvalues are embedded" (Boussaid, Cacciapuoti, Carlone,
     Comech u. a. 2023, arXiv:2006.03345v4).
   - Korrigiertes Bild [ES]: Im Hamiltonschen Fall fuehrt eine eingebettete Mode nur dann zu Wachstum, wenn ihre
     Krein-Signatur der des Kontinuums entgegengesetzt ist. Das allgemeine Prinzip habe ich aus dem Gedaechtnis und
     hier an keiner Quelle gelesen [L?].
     - Klassisches Dirac-Feld: Der Zweig negativer Frequenz hat negative Energie [L?].
     - Klein-Gordon: Der Antiteilchen-Kanal traegt positiv bei. KREIN-1 (RUNDE-10.md) bestimmte
       E_2 = 2 rho[(omega + rho)||a||^2 + (rho - omega)||b||^2] > 0 an allen acht Stellen.
     - Das Wort "Krein" steht NICHT in der Quelle (grep leer). Diese Lesart ist meine.
2. **Gap-Solitonen haben eingebettete Innenmoden, aber als Instabilitaet** (A9).
   - Erwartet: keine eingebetteten Moden beschrieben.
   - Befund: Innenmoden entstehen aus den Bandkanten. Wenn sie mit den Baendern des "inverted spectrum" ueberlappen,
     "complex eigenvalues give rise to oscillatory instabilities" (Pelinovsky, Sukhorukov, Kivshar 2004,
     [A-Abstract]).
   - In der CME kollidiert ein Paar "with the continuous spectrum and emerge[s] as a quartet of complex eigenvalues"
     (Chugunova, Pelinovsky 2005, [A]).
   - Zusammen mit Verstoss 1 ergibt das den Moderator M3 (Abschnitt 4).
3. **Leitern isolierter stiller Punkte gibt es schon, fuer eingebettete Solitonen, per Bohr-Sommerfeld** (A2, V1).
   - Erwartet: gleiche Zaehlung, anderer Gegenstand; der Mechanismus eher eine Stokes-Konstante.
   - Befund [A]: "at certain discrete values of the frequency, the amplitude of these tails can exactly vanish".
     Die "Bohr-Sommerfeld (BS) quantization rule ... selects a discrete spectrum", eps_n = 3,27 n^(-6/5) (Gl. 37).
     Das ist eine Phasenbedingung mit Haeufung am kritischen Punkt, strukturell wie unsere
     1/(omega_n^2 - omega_c^2) ~ b_inf (n + theta).
   - Folge fuer das Paper [ES]: Die Haeufung als Idee ist nicht neu. Neu bliebe die Leiter einer linearen Innenmode.
4. **3He-B-Q-Ball ist ein Zwei-Feld-Mechanismus** (A6).
   - Erwartet: einfaches NLS.
   - Befund [A-Abstract]: "the neutral field provides the potential for the charged one", also
     Friedberg-Lee-Sirlin-artig. Ob die Magnonen dort einen oder zwei Zweige haben, ist offen.
5. **Verfahren:** Das Suchbudget war vor dem ersten Abruf leer. Ich habe auf arXiv-Katalogabfragen umgestellt. Das
   schwaecht jede "nicht gefunden"-Aussage.

### 3 Literaturstand je Kandidat, Fragen (a) bis (e)

Bezug: unser Fenster 1 - omega < rho < 1 + omega; Leiter bei rho ~ 1,6 bis 1,75 m, omega ~ 0,75 bis 0,9 m.

**K1 Faser-Bragg-Gitter (Kopplungsmodengleichungen, CME; massives Thirring-Modell als integrabler Sonderfall)**
- (a) Ja. Das Kontinuum der CME-Linearisierung hat zwei Aeste, "|Im(lambda)| > 1 - omega and |Im(lambda)| > 1 +
  omega". Das ist genau unser Kanalbild (Chugunova, Pelinovsky 2005, [A]).
- (b) Innenmoden sind bekannt. Sie entstehen durch Randverzweigung [A].
  - Nur Selbstphasenmodulation (a1 = 1, Fig. 1): komplexe Quartette ab omega ~ -0,18, -0,54 und nahe -1.
  - Mittelwertfreie Kerr-Modulation (a3 = 1, Fig. 2): Quartett zwischen omega ~ 0,45 und 0,15.
  - In unserem Bereich omega ~ 0,75 bis 0,9 meldet die Quelle fuer beide Faelle keine komplexen Eigenwerte.
  - Die Faser-Standardform mit Kreuzphasenmodulation (a2 ungleich 0) ist dort nicht gerechnet.
  - Das integrable MTM hat "no non-zero eigenvalues of L".
  - Eingebettete Eigenwerte oder stille Stellen: nicht berichtet.
- (c) Gap-Solitonen sind beobachtet (Eggleton u. a. 1996; Mok u. a. 2006, Slow Light) [L?, nicht gelesen].
  Innenmoden: keine Messung gefunden (nur arXiv).
- (d) Unser omega/m ~ 0,75 bis 0,9 entspricht Omega/kappa nahe der oberen Lueckenkante. Dort ist der Gap-Soliton "close
  to a small-amplitude sech-soliton" [A], also NLS-artig, und nach R10 ohne Wandzustand [H].
  - Die Zahlenwerte sind modellabhaengig. Uebertragbar ist nur das Fenster (kappa - Omega, kappa + Omega).
  - Regime: Dirac-artig (erste Zeitableitung) -> Instabilitaet statt Stille [H].
- (e) Siehe T2. Bragg-Gitter nicht als erster Pruefstand.

**K2 Nichtlineare Dirac-Gleichung (Soler = massives Gross-Neveu in 1D; Dirac-Klein-Gordon)**
- (a) Ja. Wesentliches Spektrum iR ohne (-i(1 - omega), i(1 - omega)), Schwellen +-(1 - omega) und +-(1 + omega)
  (Berkolaiko, Comech, arXiv:0910.0917, Lemma 6.1, [A]).
- (b) Ja, exakt.
  - +-2 omega i sind L2-Eigenwerte "with any nonlinearity g(s) and in any dimension n >= 1", "embedded eigenvalues
    as long as |omega| > m/3" (ebd., Bemerkung 6.2, [A]).
  - Ursache sind die Zwei-Frequenz-Loesungen und die "Bogoliubov SU(1,1) symmetry"; Vielfachheit mindestens N/2
    (Boussaid, Comech, arXiv:1711.05654, Korollar 3.2, [A]).
  - Pseudoskalare Kopplung bricht SU(1,1) (ebd., Bemerkung 3.6, [A]); ebenso fehlt sie im Dirac-Maxwell-System
    (arXiv:2006.03345, [A]).
  - 3D-Radialreduktion: Soler (3+1)D, Dez. 2024 (arXiv:2412.21170, [A-Abstract], Volltext nur per grep: kein
    "embedded").
  - Zusammenhang mit unserem Wandzustand [ES]: nicht dasselbe Objekt.
    - Die Dirac-Linie ist rho = 2 omega; unsere Leiter liegt bei rho ~ omega + c(eps).
    - Abstand von Hand: n = 1: rho* - 2 omega* = -0,042; n = 2: +0,035. Die Linien kreuzen sich einmal.
    - Das Dirac-Objekt entspricht eher dem Rotationsmoden-Kanal unseres Zweikomponenten-Balls
      (SECTION-THIN-WALL 5.5.6).
    - Bei U(2)-Symmetrie (g = 0) loest chi = eps f e^{-i omega t} die linearisierte zweite Komponente exakt, denn dort
      gibt es keine u-v-Kopplung. Der geschlossene Kanal ist dann entkoppelt und fuer alle omega eingebettet, wie
      +-2 omega i [H, nicht nachgerechnet].
- (c) Nicht gemessen. Eine Laborrealisierung der Soler-Nichtlinearitaet habe ich nicht gefunden. arXiv:2501.04027
  (Dez. 2024) schlaegt Zwei-Frequenz-Moden als Dunkle-Materie-Speicher vor, also Theorie [A-Abstract].
- (d) Das Fenster m/3 < omega < m enthaelt unser omega vollstaendig.
- (e) Siehe T2.

**K3 Binaere Wellenleiter-Arrays**
- (a) Ja, in der Kontinuumsgrenze.
  - Die NDE lautet i dz Psi = -i kappa alpha d_xi Psi + sigma beta Psi - gamma G mit G = (|Psi1|^2 Psi1,
    |Psi2|^2 Psi2). Die Masse ist die Verstimmung sigma.
  - Die Nichtlinearitaet "violates Lorentz invariance" (Tran, Longhi, Biancalana 2013/14, arXiv:1305.1055, [A]).
  - Folgerung [ES]: Kerr-Form statt Soler-Form, also kein SU(1,1)-Schutz.
- (b) Nicht untersucht; die Stabilitaet ist ausdruecklich auf spaeter verschoben [A].
- (c) Diskrete Gap-Solitonen im binaeren Array beobachtet (Morandotti u. a., Opt. Lett. 29, 2890 (2004); zitiert in
  1305.1055, Primaerquelle nicht gelesen). Innenmoden: nichts gefunden.
- (d) Dirac-artig, also Instabilitaetsregime [H].
- (e) Wie K1.

**K4 BEC-Gap-Solitonen in optischen Gittern**
- (a) Mehr als zwei Baender. In der Bogoliubov-Linearisierung gibt es "invertierte" Lochbaender.
- (b) Innenmoden kommen aus allen Bandkanten gleicher Polaritaet. Ueberlappen sie mit invertierten Baendern, folgt
  oszillatorische Instabilitaet (Pelinovsky, Sukhorukov, Kivshar 2004, PRE 70, 036618, [A-Abstract]).
- (c) Erste Beobachtung "bright gap solitons ... with repulsive interaction" (Eiermann u. a. 2004, PRL 92, 230401,
  [A-Abstract]). Innenmoden nicht gemessen (nicht gefunden).
- (d) NLS-artig (erste Zeitableitung); nach R10 und M3 kein Leiterkandidat [H].
- (e) Nicht empfohlen.

**K5 Magnonen**
- Antiferromagnet:
  - Die Dynamik ist "naturally second order in time and is therefore closely related to relativistic nonlinear sigma
    models" (Balseyro Sebastian, Ohashi, Nitta 2026, "Magnetic Q-balls", arXiv:2609.32059, [A]).
  - Das Q-Ball-Fenster ist symmetrisch in omega und kann durch DM-Kopplung plus Zeeman-Feld ganz geschlossen werden
    [A-Abstract].
  - Die Spektralannahmen sind "not prove[d]" [A].
  - "precessing ball solitons" im einachsigen AFM am Spin-Flop (Nietz 2010, arXiv:1005.2049, [A-Abstract]).
  - Klassiker (Kosevich, Ivanov, Kovalev 1990, Phys. Rep.) nur [L?].
- 3He-B: Magnon-Q-Ball beobachtet, "Persistent Signal" im NMR (Bunkov, Volovik 2007, PRL 98, 265302, [A-Abstract]),
  mit Zwei-Feld-Mechanismus.
- Ferromagnetische Magnon-Tropfen (Spin-Torque, 2013) [L?]: Berry-Phasen-Dynamik, erste Ordnung, NLS-artig.
- (a) Im AFM ja: zwei Polarisationen als Teilchen/Antiteilchen mit Luecke, KG-Regime [A fuer "zweite Ordnung", sonst
  L?]. Im Ferromagneten und in 3He-B: eher nein [H].
- (b) Eingebettete Innenmoden praezedierender Solitonen: nichts gefunden (nur arXiv).
- (c) Nicht gemessen. Die Quelle nennt Gilbert-Daempfung als Huerde; die Realisierung brauche "sufficiently weak
  damping" oder Spin-Torque-Antrieb [A].
- (d) Mit einer AFMR-Frequenz im Bereich 0,1 bis 1 THz [L?] laegen die Stoerkomponenten bei omega + rho ~ 2,4 bis 2,6 m
  (offen, abgestrahlt) und |omega - rho| ~ 0,85 m (gebunden), also im THz-Bereich [Handrechnung]. Ob grosse AFM-Solitonen eine Duennwand mit gebundenem
  Antiteilchen-Zustand haben, ist unbekannt [offen].
- (e) T1, bester Kandidat.

**K6 Eingebettete Solitonen (Abgrenzung)**
- Dort liegt die Frequenz des Solitons selbst im Kontinuum; an diskreten Werten verschwinden die Schwaenze
  (Malomed, Wagenknecht, Champneys, Pearce 2005, arXiv:nlin/0505012, [A]).
- Bei uns ist das Soliton nicht eingebettet (omega < m); eingebettet ist eine lineare Mode.
- Gemeinsam: Kodimension 1, Bohr-Sommerfeld-Leiter, Haeufung an einem kritischen Punkt.
- Verwandt: eingebettete Solitonen in mikrowellengekoppelten Zweikomponenten-BEC mit SOC, "chiefly stable" (Fan, Chen,
  Li, Malomed 2020, PRA 101, 013607, arXiv:1912.10992, [A-Abstract]).
- Yang/Malomed/Kaup 1999 und Champneys u. a. 2001 nicht gelesen [L?].
- **Wortfallen** (Abgrenzung, [A-Abstract]):
  - "Embedded eigenvalue" im integrablen MTM meint den Kaup-Newell-Lax-Operator, nicht die Linearisierung (Han, He,
    Pelinovsky 2024, arXiv:2406.06715).
  - "Soliton at a BIC" bei Polaritonen meint ein Kondensat auf einem photonischen BIC (Septembre u. a. 2024,
    arXiv:2401.06589; ebenso 2512.23368, 2605.19913).

### 4 Regime und Moderatoren

- **M1 Symmetrie:** Regime S (symmetriegeschuetzt) gegen Regime P (Phasenbedingung).
  - S: Der geschlossene Kanal ist exakt entkoppelt, der Eigenwert eingebettet auf ganzen Intervallen (Dirac +-2 omega i;
    vermutlich unser Zweikomponenten-Ball bei g = 0 [H]).
  - P: Die Kopplung g(omega) ist ungleich 0 und hat isolierte Nullstellen (unsere Leiter; Bohr-Sommerfeld-Leiter
    eingebetteter Solitonen).
  - Moderator: SU(1,1), Paritaet, U(2).
- **M2 Relativistisch gegen nichtrelativistisch** (R10): Der Wandzustand lebt bei rho ~ 2 m. Das NLS schneidet diesen
  Bereich ab; die Dirac-Gleichung hat ihn noch. Dort heissen +-2 mi "embedded thresholds" (1711.05654, [A]).
- **M3 Krein-Signatur des Zustands im geschlossenen Kanal relativ zum offenen Kontinuum** [ES, aus drei
  Quellengruppen plus KREIN-1]:
  - Gleiches Vorzeichen (bosonisch, zweite Zeitableitung: KG, AFM-Sigma-Modell): gedaempfte Resonanz; stille Stellen
    sind BIC.
  - Entgegengesetzt (erste Zeitableitung: Dirac, CME, Bogoliubov-Loch im NLS): oszillatorische Instabilitaet. Stille
    Stellen gaebe es hoechstens als isolierte Nullstellen der Wachstumsrate, also als Stabilitaetspunkte in einem
    instabilen Band [H].
- **Kopplung vor Bauteil (Regel 6):** Es gibt drei Wege zu "keine Abstrahlung":
  - Symmetrie-Entkopplung (Dirac, U(2))
  - Phasenbedingung eines Zustands (unsere Leiter, Bohr-Sommerfeld)
  - Friedrich-Wintgen (zwei Resonanzen)
  Die gemeinsame Groesse ist die Kopplung g(omega) des Zustands im geschlossenen Kanal an das offene Kontinuum.
  |g|^2 ist je nach M3 Zerfalls- oder Wachstumsrate [ES].

### 5 Unterscheidungspunkte

- **U1 S gegen P:** Gamma(omega) (bzw. Re lambda) ist auf einem Intervall identisch 0 (S) oder hat isolierte
  Doppelnullstellen Gamma ~ C(omega^2 - omega*^2)^2 (P).
  - Trennend ist der Grenzfall schwachen Symmetriebruchs eps -> 0.
  - Ist unsere Zweikomponenten-Leiter das gebrochene Bild einer geschuetzten Linie, muessen ihre Nullstellen fuer
    g -> 0 in eine durchgehende Nulllinie uebergehen [H].
- **U2 KG-Regime gegen Dirac-Regime:** Vorzeichen der Frequenzverschiebung neben der Stelle, also Abklingen gegen
  Wachsen.
  - Trennbar am klarsten bei omega -> m: Dort ist die Dirac-Instabilitaet bewiesen [A], und der KG-Wandzustand bleibt
    nach R10 gebunden (beta = 1 bis 4, nur der nackte Zustand).
- **U3 Unsere Leiter gegen die Leiter eingebetteter Solitonen:** Haeufungsexponent -1 (Duennwandmodell) gegen -6/5
  (Gl. 37 in nlin/0505012).
  - Trennbar erst bei grossem n (n >= 5, wo das Duennwandmodell 4e-5 trifft). Bei n = 1 bis 3 ununterscheidbar
    [ES].
- **U4 Dirac-Linie gegen unsere Leiter:** rho = 2 omega exakt gegen rho ~ omega + c.
  - Trennbar an jeder Stelle ausser nahe omega ~ c ~ 0,80 bis 0,84. Bei n = 1 und n = 2 betraegt der Abstand 0,04, also
    schon getrennt.

### 6 Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1 geprueft:** Dass unsere Moden positive Krein-Signatur haben. Bestaetigt, KREIN-1 in RUNDE-10.md.
- **G2 geprueft:** Dass das CME-Kanalbild dem unseren gleicht. Bestaetigt, math/0504442 Z. 510-512 [A].
- **G3 geprueft:** Ob die Dirac-Quelle die Instabilitaet selbst der Krein-Signatur zuschreibt. Nein, "Krein" kommt
  nicht vor. M3 bleibt mein Schluss [ES].
- **G4 nicht geprueft:** Die Experimente Eggleton 1996, Mok 2006, Morandotti 2004 und die AFM-Klassiker. Alle [L?] bzw.
  zitiert.
- **G5 nicht geprueft:** Dass unsere Zahlen (rho ~ 1,6 bis 1,75 m) auf andere Modelle uebertragbar sind. Das sind sie
  nicht; nur das Fenster ist modellunabhaengig.
- **G6 widerlegt als Selbstverstaendlichkeit:** "Zwei Zweige mit Luecke" (R10) war das Suchkriterium. Es ist notwendig,
  nicht hinreichend (M3).

### 7 Kalibrierung

- **(a) Gemessen:**
  - Gap-Solitonen im BEC [A-Abstract]
  - Gap-Solitonen in Bragg-Gittern und binaeren Arrays ([L?] bzw. zitiert)
  - Q-Ball-Analogon in 3He-B [A-Abstract]
  Eine eingebettete Innenmode eines Solitons ist nirgends gemessen.
- **(b) Verdichtet:**
  - +-2 omega i eingebettet fuer |omega| > m/3 [A]
  - Symmetriebruch -> Instabilitaet [A]
  - Gap-Innenmoden im Kontinuum -> Instabilitaet [A]
  - Bohr-Sommerfeld-Leiter eingebetteter Solitonen [A]
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - "AFM ist der beste Kandidat" folgt aus dem Ausschluss der anderen plus einem Regime-Argument. Eine Quelle ueber
    AFM-Innenmoden gibt es nicht.
  - Meine Sicherheit in M3 stieg ueber drei Quellen. Zwei davon (Chugunova/Pelinovsky; Pelinovsky/Sukhorukov/Kivshar)
    teilen einen Mitautor und den Rahmen, und keine spricht Krein aus.

### 8 Offene Fragen und Testvorschlaege (nicht gerechnet)

- **T1 (kleinste Rechnung, labornah, bester Kandidat): nackter geschlossener Kanal im einachsigen AFM.**
  - Aufbau: O(3)-Sigma-Modell mit leichter Achse, 3D radial, Familie praezedierender Solitonen. Bestimmt wird der
    tiefste Eigenwert des geschlossenen Kanals bei Kopplung 0, wie der "kanal"-Test in nls2.py.
  - **Scheiterregel (vorab):** Liegt dieser Zustand auf zwei Gitterstufen fuer die ganze Familie nicht im offenen
    Kontinuum (m - omega < rho_c < m + omega verfehlt), ist der AFM als Leiterkandidat verworfen. Das entspraeche dem
    NLS-Befund aus R10.
  - Nur wenn er eingebettet ist, folgt die W-Gitter-Suche wie in R10.
- **T2 (Regimeprobe, eigenes Modell):** Zweikomponenten-Ball bei g -> 0 (U(2)-Grenzfall).
  - Vorhersage [H]: Der gegenlaeufige Kanal ist bei g = 0 fuer alle omega eingebettet (Regime S). Bei kleinem g
    bleiben isolierte Nullstellen, die sich fuer g -> 0 zu einer Linie verdichten.
  - **Scheiterregel:** Hat der gegenlaeufige Kanal schon bei g = 0 eine Breite ungleich 0 (Gamma > 1e-8 an drei
    omega-Werten, zwei Gitterstufen), ist die Dirac-Analogie (M1) fuer unser Modell falsch.
- **O1** Gibt es KG-Laborsysteme mit U(1) und positiver Energie ausser dem AFM (z. B. Gitter isotroper
  2D-Oszillatoren, phi = x + iy) [H]?
- **O2** Liefern Dirac-artige Systeme Leitern von Stabilitaetspunkten (Nullstellen der Wachstumsrate)? Pruefbar in der
  CME (Glasfaser, SPM:XPM = 1:2) oder in der Soler-Gleichung mit pseudoskalarem Zusatz.
- **O3** Barashenkov/Pelinovsky/Zemlyanaya 1998 und alle Zeitschriften ohne arXiv-Fassung sind nicht durchsucht.

### 9 Quellenliste (alle unter quellen/ mit sha256 in F1; Lesetiefe in Klammern)

- Berkolaiko, Comech (2009/2012): On spectral stability of solitary waves of nonlinear Dirac equation on a line.
  https://arxiv.org/abs/0910.0917 [A]
- Boussaid, Comech (2017/2018): Spectral stability of bi-frequency solitary waves in Soler and Dirac-Klein-Gordon
  models. https://arxiv.org/abs/1711.05654 [A]
- Boussaid, Cacciapuoti, Carlone, Comech u. a. (2020, v4 2023): Spectral stability and instability of solitary waves of
  the Dirac equation with concentrated nonlinearity. https://arxiv.org/abs/2006.03345 [A]
- Boussaid, Comech, Kulkarni (Dez. 2024): On spectral stability of one- and bi-frequency solitary waves in Soler model
  in (3+1)D. https://arxiv.org/abs/2412.21170 [A-Abstract, Volltext nur grep]
- Comech, Kulkarni, Boussaid, Cuevas-Maraver (Dez. 2024): Stable bi-frequency spinor modes as Dark Matter candidates.
  https://arxiv.org/abs/2501.04027 [A-Abstract]
- Chugunova, Pelinovsky (2005): Block-diagonalization of the linearized coupled-mode system.
  https://arxiv.org/abs/math/0504442 [A]
- Pelinovsky, Sukhorukov, Kivshar (2004): Bifurcations and stability of gap solitons in periodic potentials, PRE 70,
  036618. https://arxiv.org/abs/nlin/0405019 [A-Abstract]
- Tran, Longhi, Biancalana (2013/2014): Optical analogue of relativistic Dirac solitons in binary waveguide arrays.
  https://arxiv.org/abs/1305.1055 [A]
- Eiermann u. a. (2004): Bright gap solitons of atoms with repulsive interaction, PRL 92, 230401.
  https://arxiv.org/abs/cond-mat/0402178 [A-Abstract]
- Malomed, Wagenknecht, Champneys, Pearce (2005): Accumulation of embedded solitons in systems with quadratic
  nonlinearity. https://arxiv.org/abs/nlin/0505012 [A]
- Fan, Chen, Li, Malomed (2019/2020): Gap and embedded solitons in microwave-coupled binary condensates, PRA 101,
  013607. https://arxiv.org/abs/1912.10992 [A-Abstract]
- Han, He, Pelinovsky (2024): Algebraic solitons in the massive Thirring model. https://arxiv.org/abs/2406.06715
  [A-Abstract]
- Septembre u. a. (2024): Soliton formation in an exciton-polariton condensate at a bound state in the continuum.
  https://arxiv.org/abs/2401.06589 [A-Abstract]
- Balseyro Sebastian, Ohashi, Nitta (2026): Magnetic Q-balls. https://arxiv.org/abs/2609.32059 [A, grep-Lesung]
- Nietz (2010): Precessing equilibrium and overcritical solitons at a spin-flop transition.
  https://arxiv.org/abs/1005.2049 [A-Abstract]
- Bunkov, Volovik (2007): Magnon condensation into Q-ball in 3He-B, PRL 98, 265302.
  https://arxiv.org/abs/cond-mat/0703183 [A-Abstract]
- Nur [L?]:
  - Eggleton u. a. 1996 (PRL, Bragg grating solitons)
  - Mok u. a. 2006 (Nature Physics, slow-light gap solitons)
  - Morandotti u. a. 2004 (Opt. Lett. 29, 2890, zitiert in 1305.1055)
  - Barashenkov/Pelinovsky/Zemlyanaya 1998 (PRL)
  - Yang/Malomed/Kaup 1999; Champneys u. a. 2001
  - Kosevich/Ivanov/Kovalev 1990 (Phys. Rep.)
- Nur Titel aus der Katalogliste [S]: 2512.23368, 2605.19913, 2412.00838, 2603.28544, 2404.08218, 2410.12467,
  2509.03627.

---

## ARBEITSFELD

### F0 Vorab-Erwartungen (geschrieben 2026-09-30 12:37:42 CEST laut date, VOR jedem externen Abruf)

Bezugsrahmen (aus den Hintergrunddateien): Unser Fenster "ein Kanal offen, einer zu" ist 1 - omega < rho < 1 + omega.
Die Leiter liegt bei rho ~ omega + c(eps), c ~ 0,80 bis 0,84 (nackter Wandzustand c_w = 0,7993 bei beta = 1/2). Der
geschlossene Kanal omega - rho ~ -omega ist der Antiteilchen-Zweig.

Eigene Vorueberlegung vor der Suche [ES]: Die Linie rho = 2 omega (Dirac-Eigenwert +-2 omega i, falls es ihn gibt)
kreuzt unsere Leiter nur einmal: n = 1 hat rho* - 2 omega* = 1,7446 - 1,7863 = -0,042, n = 2 hat
1,6904 - 2 x 0,8277 = +0,035. Eine Identitaet beider Objekte ist damit schon rechnerisch unwahrscheinlich.

| Nr | Erwartung (je ein Satz) | Sicherheit |
|---|---|---|
| E0 | Kein Laborsystem hat eine gemessene eingebettete Innenmode (BIC) eines Solitons; gemessen sind hoechstens die Solitonen selbst. | ~90 % |
| E1a | Faser-Bragg-Gitter (Kopplungsmodengleichungen, CME): zwei Zweige +-sqrt(kappa^2 + k^2) mit Luecke; das Kanalfenster kappa - Omega < lambda < kappa + Omega hat genau unsere Struktur. | ~85 % |
| E1b | Innere Moden der Gap-Solitonen sind theoretisch bekannt (Barashenkov/Pelinovsky/Zemlyanaya 1998: Innenmoden, oszillatorische Instabilitaet); eingebettete Eigenwerte als isolierte stille Stellen oder Leiter sind dort NICHT beschrieben. | ~65 % |
| E1c | Innenmoden von Bragg-Gap-Solitonen sind nicht gemessen (Eggleton u. a. 1996, Mok u. a. 2006 messen Ausbreitung, Verzoegerung, Kompression). | ~90 % |
| E2a | Nichtlineare Dirac-Gleichung (Soler/Gross-Neveu): Linearisierung hat exakte Eigenwerte +-2 omega i, eingebettet fuer omega > m/3, erzwungen durch eine SU(1,1)-Symmetrie (Zwei-Frequenz-Wellen, Boussaid/Comech); sie existieren auf einem ganzen Intervall, nicht an isolierten Punkten. | ~75 % |
| E2b | Eine Leiter isolierter eingebetteter Eigenwerte ist fuer NLD nicht beschrieben; Zusammenhang zu unserem Wandzustand: keiner im Sinne einer Identitaet, eher Analogie zum Rotationsmoden-Kanal (SECTION-THIN-WALL 5.5.6). | ~80 % |
| E2c | NLD-Solitonen mit Innenmoden sind nicht gemessen. | ~95 % |
| E3 | Binaere Wellenleiter-Arrays: Kontinuumsgrenze ist eine NLD mit Kerr-artiger (nicht Soler-artiger) Nichtlinearitaet; Dirac-Solitonen dort theoretisch (Tran/Longhi/Biancalana 2014), gemessen sind diskrete Gap-Solitonen in binaeren Arrays (Morandotti u. a. 2004), Innenmoden nicht. | ~70 % |
| E4 | BEC-Gap-Solitonen (Eiermann u. a. 2004): gemessen als Soliton mit wenigen hundert Atomen; mehr als zwei Baender, Innenmoden nicht gemessen, eingebettete Moden nicht beschrieben. | ~85 % |
| E5a | Antiferromagnet mit leichter Achse: Lorentz-artiges Sigma-Modell mit Luecke; beide Magnonpolarisationen spielen Teilchen/Antiteilchen; praezedierende Solitonen (Ivanov, Kosevich) sind Q-Ball-artig. | ~75 % |
| E5b | Eingebettete Innenmoden praezedierender AFM-Solitonen: nicht beschrieben; gemessen: keine praezedierenden AFM-Solitonen, wohl aber ferromagnetische Magnon-Tropfen (Spin-Torque, 2013), die aber NLS-artig (ein Zweig) sind. | ~80 % |
| E6 | Eingebettete Solitonen (Yang/Malomed/Kaup 1999; Champneys u. a. 2001): das Soliton selbst liegt im Kontinuum, an isolierten Parameterwerten; gleiche Zaehlung (Kodimension 1), anderer Gegenstand. | ~90 % |
| E7 | 24-Monats-Suche (2024 bis 2026): keine neue Arbeit mit BIC-Innenmode eines Solitons in einem Zwei-Zweig-System. | ~70 % |

Zwei-Regime-Vorannahme [H]: Regime S (symmetriegeschuetzte Einbettung, ganze Intervalle, z. B. NLD +-2 omega i) und
Regime P (Phasen-/Interferenzbedingung, isolierte Punkte, Leiter; unser Q-Ball). Vermuteter Moderator: eine
Zusatzsymmetrie, die den Zustand des geschlossenen Kanals vom offenen entkoppelt. Zweiter Moderator: relativistisch
(zwei Zweige) gegen nichtrelativistisch (Teilchen plus Loch).

### F1 Abrufprotokoll (Erwartung vor jedem Abruf, dann Befund)

- B1-B4 Erwartungen (vor Abruf; date beim Anhaengen: 12:38:21):
  - B1 Suche Boussaid/Comech Zwei-Frequenz-Wellen: Treffer ~2017/2018 (arXiv), +-2 omega i aus SU(1,1), eingebettet fuer omega > m/3.
  - B2 Suche Barashenkov/Pelinovsky/Zemlyanaya 1998: PRL, Innenmoden und oszillatorische Instabilitaet der CME-Gap-Solitonen, keine Leiter.
  - B3 Suche "embedded eigenvalue" + Kopplungsmodengleichungen: eher nichts Einschlaegiges (~50 %), sonst Chugunova/Pelinovsky 2006.
  - B4 Suche praezedierende AFM-Solitonen Innenmoden: Ivanov/Kosevich/Sheka; keine eingebetteten Moden.
- B1-B4 **nicht ausgefuehrt**: WebSearch-Budget der Sitzung erschoepft (Meldung "200 of 200 WebSearch calls"). Ersatzweg:
  gezielte Katalogabfragen bei arXiv (export.arxiv.org/api, Autor/Titel, roh per curl) und PDFs per curl + pdftotext.
  Folge fuer die Belegstufe: Die 24-Monats-Suche kann nur arXiv abdecken (keine Zeitschriften ohne arXiv-Fassung,
  keine Konferenzbaende). Das steht als Grenze im Bericht.
- K1-K6 Erwartungen (vor Abruf der arXiv-Katalogabfragen; date beim Anhaengen oben in der Befehlsausgabe):
  - K1 au:Comech + Zwei-Frequenz/bi-frequency: Arbeit Boussaid/Comech mit SU(1,1) und +-2 omega i (wie E2a).
  - K2 au:Berkolaiko + au:Comech: 1D-NLD-Spektralstabilitaet, Eigenwerte +-2 omega i fuer alle omega, Schwellen +-(m +- omega).
  - K3 au:Barashenkov + Gap-Solitonen: PRL 1998 und/oder Folgearbeit 2000 mit Innenmoden, keine eingebetteten Eigenwerte.
  - K4 au:Chugunova + au:Pelinovsky: Block-Diagonalisierung der CME; hoechstens Randbemerkung zu eingebetteten Eigenwerten.
  - K5 au:Longhi + au:Biancalana + Dirac: Tran/Longhi/Biancalana 2014, Dirac-Solitonen im binaeren Array, keine Innenmoden-Analyse.
  - K6 Balseyro Sebastian/Ohashi/Nitta 2609.32059 "Magnetic Q-balls": 1D chirale Magnete, AFM mit zweiter Zeitableitung, keine Innenmoden-BIC.
- K1 Befund: Treffer wie erwartet (1711.05654 Boussaid/Comech; dazu 2412.21170 "Soler (3+1)D" und 2501.04027 "Dark
  Matter", beide Dez. 2024, also im 24-Monats-Fenster). Rohabstract 1711.05654 [A]: "relation of +-2 omega i eigenvalues
  ... Bogoliubov SU(1,1) symmetry, and the existence of bi-frequency solitary waves". Bestaetigt E2a im Kern; Intervall
  und Einbettungsgrenze m/3 noch nicht an der Quelle gesehen.
- K2 Befund: 0910.0917 Berkolaiko/Comech (1D, Soler = massives Gross-Neveu), Abstract [A]: numerisch spektral stabil,
  "explicit expressions for several of the eigenfunctions". Bestaetigt.
- K3 Befund: kein Treffer fuer au:Barashenkov AND ti:gap (Arbeit 1998 vermutlich ohne arXiv-Fassung oder anders betitelt).
- P1-P3 Erwartungen (vor Volltextabruf):
  - P1 1711.05654 Volltext: +-2 omega i fuer alle omega in (0, m), eingebettet fuer omega > m/3 (wesentliches Spektrum
    ab |Im lambda| >= m - omega); Ursache Symmetrie, also ganze Intervalle.
  - P2 2412.21170 Volltext: 3D-Radialreduktion; +-2 omega i in einem Drehimpulssektor; keine weiteren eingebetteten
    Eigenwerte als Befund benannt.
  - P3 0910.0917 Volltext: 1D; +-2 omega i explizit; Schwellen +-(m - omega), +-(m + omega).
- P1 Befund 1711.05654 [A] (quellen/1711.05654.pdf, sha256 8f188db4...): +-2 omega i sind Eigenwerte der Linearisierung
  "of geometric multiplicity (at least) N/2" (Korollar 3.2), Beweis ueber exakte Zwei-Frequenz-Loesungen; Ursache
  "Bogoliubov SU(1,1) symmetry"; im nichtrelativistischen Grenzfall heissen +-2mi dort "embedded thresholds". Bemerkung
  3.6: mit pseudoskalarer Kopplung ist SU(1,1) "no longer present". **Bestaetigt E2a**, und liefert den Schalter
  (Symmetriebruch) fuer den Unterscheidungspunkt.
- P3 Befund 0910.0917 [A] (sha256 9a84cd59...): Lemma 6.1: sigma_ess = iR ohne (-i(1-omega), i(1-omega)); zwei
  Komponenten des wesentlichen Spektrums mit Schwellen +-(1 - omega) und +-(1 + omega) ("flat"/"sharp"), also genau unser
  Kanalbild. Bemerkung 6.2: +-2 omega i sind L2-Eigenwerte "with any nonlinearity g(s) and in any dimension n >= 1"
  (Soler-Klasse g(psi-bar psi)); "embedded eigenvalues as long as |omega| > m/3". **Bestaetigt E2a vollstaendig.**
- P2 Befund 2412.21170 [A, nur grep]: keine Stelle "embedded" im Text gefunden (grep leer); Erwartung "keine weiteren
  eingebetteten Eigenwerte benannt" nicht verletzt, aber nur per grep geprueft.
- Eigener Schluss nach P1/P3 [ES]: Im Zweikomponenten-Modell mit U(2)-Symmetrie (g = 0) loest chi = eps f e^{-i omega t}
  die fuer die zweite Komponente linearisierte Gleichung exakt (dort keine U''-Kopplung zwischen u und v), also
  entkoppelter geschlossener Kanal = eingebettet fuer alle omega, wie Dirac +-2 omega i. Bei g ungleich 0 wird daraus die
  Formfaktor-Leiter aus SECTION-THIN-WALL 5.5.6. Das ist die Bruecke zwischen Regime S und Regime P [H].
- K7-K9 Erwartungen (vor Abruf):
  - K7 au:Lakoba + Dirac: numerische Stabilitaet 1D-NLD mit verschiedenen kubischen Nichtlinearitaeten (Soler, Thirring,
    gemischt); vermutlich oszillatorische Instabilitaeten, zum Schicksal von +-2 omega i ohne SU(1,1) hoechstens Randnotiz.
  - K8 au:Chugunova + au:Pelinovsky: CME-Block-Diagonalisierung; eingebettete Eigenwerte hoechstens am Rand.
  - K9 au:Longhi + au:Biancalana: Tran/Longhi/Biancalana 2014; Kerr-artige NLD, keine Innenmoden-Analyse.
- K8/P4 Befund math/0504442 Chugunova/Pelinovsky [A] (sha256 7e2eca9c...): CME-Linearisierung = 4x4-Dirac-System mit
  indefiniter Metrik. Innenmoden (rein imaginaere Eigenwerte) entstehen durch Randverzweigungen ("edge bifurcation");
  bei omega ~ -0,18, -0,54 und nahe -1 kollidiert ein Paar "with the continuous spectrum and emerge as a quartet of
  complex eigenvalues" (oszillatorische Instabilitaet); integrables MTM: "no non-zero eigenvalues of L exist". Keine
  eingebetteten Eigenwerte berichtet. **Bestaetigt E1b.** Neu fuer mich: Der Eintritt ins Kontinuum fuehrt dort zu
  Instabilitaet (Krein-Kollision mit dem Kontinuum), nicht zu einer Resonanz -> Krein-Vorzeichen als Moderator [H].
- K9/P5 Befund 1305.1055 Tran/Longhi/Biancalana [A] (sha256 dcaa9772...): NDE (7) mit G = (|Psi1|^2 Psi1, |Psi2|^2 Psi2),
  Masse = Verstimmung sigma der Unterlinien; "violates Lorentz invariance"; Stabilitaet ausdruecklich auf spaeter
  verschoben; diskrete Gap-Solitonen im binaeren Array experimentell beobachtet (ihr Zitat [24] Morandotti u. a., Opt.
  Lett. 29, 2890 (2004); Primaerquelle nicht gelesen). **Bestaetigt E3.** [ES] Kerr-artige NDE hat keine SU(1,1), also
  kein geschuetztes +-2 omega i.
- K10-K15 Erwartungen (vor Abruf):
  - K10 id 2609.32059 (Magnetic Q-balls): 1D chirale Magnete; AFM-Fall Lorentz-artig; keine Innenmoden-BIC.
  - K11 arXiv abs:"Q-ball" + antiferromagnet/magnon, 2024-2026: wenige Treffer; keine eingebetteten Innenmoden.
  - K12 au:Malomed + ti:embedded (Yang/Malomed/Kaup; Champneys u. a.): Definition "Soliton im Kontinuum, isolierte
    Parameterwerte, halbstabil".
  - K13 24-Monats-Abfrage abs:"bound state in the continuum" AND abs:soliton bzw. "embedded eigenvalue": nur
    lineare Photonik oder Kinks; keine Innenmode eines Solitons in Zwei-Zweig-System.
  - K14 au:Bunkov + au:Volovik + Q-ball: Magnon-Q-Ball in 3He-B, nichtrelativistisch (ein Zweig), Anregungsniveaus der
    Falle gemessen, keine eingebetteten Moden.
  - K15 au:Eiermann + gap: cond-mat 2004, Gap-Soliton ~250 Atome, keine Innenmoden.
- K11-K15 Befunde (Kataloglisten, nur Titel [S]): K11 ausser 2609.32059 kein AFM-Q-Ball-Treffer 2024-2026 unter dem
  Wort "Q-ball". K12 unerwartet: "Accumulation of embedded solitons in systems with quadratic nonlinearity"
  (nlin/0505012) und "Gap and embedded solitons in microwave-coupled binary condensates" (1912.10992). K13a: nur
  Polariton-Solitonen AUF einem photonischen BIC (2401.06589, 2512.23368, 2605.19913), also Wortkollision, nicht BIC
  eines Solitons. K13b unerwartet: MTM-Arbeiten 2024-2026 mit "embedded eigenvalue" im Abstract (2406.06715,
  2412.00838, 2603.28544). K14: cond-mat/0703183. K15: cond-mat/0402178.
- A1-A7 Erwartungen (vor Abruf der Rohabstracts):
  - A1 2609.32059: wie K10.
  - A2 nlin/0505012: eingebettete Solitonen an isolierten Parameterwerten, die sich zu einem Grenzwert haeufen
    (Leiter-Analogon, aber fuer das Soliton selbst).
  - A3 1912.10992: Mikrowellen-(Rabi-)Kopplung gibt Luecke; eingebettete Solitonen = Soliton im Kontinuum; keine Innenmoden.
  - A4 2406.06715: "embedded eigenvalue" meint den Lax-Operator (Streuproblem) des MTM, nicht die Linearisierung.
  - A5 2401.06589: Polariton-Kondensat auf photonischem BIC; Soliton ist nicht Traeger einer BIC-Innenmode.
  - A6 cond-mat/0703183: Magnon-Q-Ball in 3He-B, nichtrelativistisch; Anregungsniveaus gemessen.
  - A7 cond-mat/0402178: ~250 Atome, repulsiv, Gap-Soliton an der Bandkante; keine Innenmoden.
- A1-A7 Befunde (Rohabstracts per arXiv-API [A-Abstract]):
  - A1 2609.32059 bestaetigt: 1D chirale Magnete, AFM-Fall mit zweiter Zeitableitung, Frequenzfenster "symmetric and
    can be completely closed"; keine Innenmoden im Abstract.
  - **A2 VERLETZT (Ausmass):** nlin/0505012 (Malomed/Wagenknecht/Champneys/Pearce 2005): WKB-Naeherung "yields an
    asymptotic formula for the distribution of discrete values of eps at which the ESs exist", Skalenindex -6/5, die
    Familien "emerge from a critical point" mit vierfacher Null-Eigenwert. Das ist eine Leiter isolierter stiller Punkte
    mit WKB-Phasenquantisierung und Haeufung an einem kritischen Punkt, also dieselbe Struktur wie unsere Leiter,
    nur fuer das Soliton selbst. Erwartet hatte ich "gleiche Zaehlung, anderer Gegenstand"; die Parallele reicht bis
    zum Haeufungsgesetz. -> Volltext pruefen (V1).
  - A3 1912.10992 bestaetigt: Zweikomponenten-BEC mit SOC, Zeeman und Mikrowelle; "gap and embedded solitons (those
    overlapping with the continuous spectrum)", "chiefly stable". Soliton eingebettet, nicht Innenmode.
  - A4 2406.06715 bestaetigt: "simple embedded eigenvalue in the Kaup-Newell spectral problem" = Lax-Operator.
    Wortfalle: "embedded eigenvalue" im integrablen MTM ist kein eingebetteter Eigenwert der Linearisierung.
  - A5 2401.06589 bestaetigt: Polariton-Kondensat auf photonischem BIC; Soliton ist nicht Traeger einer BIC-Mode.
  - A6 cond-mat/0703183 teilweise verletzt: Q-Ball in 3He-B experimentell ("Persistent Signal"), aber als
    Zwei-Feld-Mechanismus ("interaction between the charged and neutral fields, where the neutral field provides the
    potential"), also Friedberg-Lee-Sirlin-artig, nicht einfaches NLS. Ob die Magnonen dort ein oder zwei Zweige haben,
    sagt das Abstract nicht [offen].
  - A7 cond-mat/0402178 bestaetigt: erste Beobachtung, Gap-Soliton an der Bandkante, repulsiv; keine Innenmoden.
- V1 Erwartung (vor Volltext nlin/0505012): Index -6/5 beschreibt eps_n ~ n^(-6/5) oder aehnlich; Mechanismus:
  Nullstelle des Strahlungs-Stokes-Koeffizienten (jenseits aller Ordnungen), nicht Phasenbedingung einer Innenwelle.
- K16 Erwartung: arXiv abs:"precessional soliton" / "magnon droplet" + antiferromagnet: wenige Treffer, keine eingebetteten Innenmoden.
- **V1 VERLETZT:** nlin/0505012 Volltext [A] (sha256 32420500...): Mechanismus ist ausdruecklich eine
  Bohr-Sommerfeld-Quantisierung ("we can apply the Bohr-Sommerfeld (BS) quantization rule ... which selects a discrete
  spectrum of values of eps"), Ergebnis eps_n = 3,27 n^(-6/5) (Gl. 37); "at certain discrete values of the frequency, the
  amplitude of these tails can exactly vanish". Also Phasenbedingung, nicht Stokes-Konstante. Korrigierte Erwartung:
  Unsere Leiter (eps_n ~ 1/(n + theta), Index -1) hat ein strukturelles Vorbild in der Haeufung eingebetteter
  Solitonen (Index -6/5). Unterschied: dort das Soliton selbst, hier eine lineare Mode; dort Normalform der
  Typ-I-Frequenzverdopplung (chi-2), hier Wandzustand im Antiteilchen-Kanal.
- K16/K17 Erwartungen (vor Abruf): K16 wie oben. K17 abs:"gap soliton" AND abs:"internal mode": theoretische Arbeiten
  (CME, BEC-Gitter), keine Messung.
- K16/K17 Befund: je ein Treffer (1005.2049 AFM am Spin-Flop; nlin/0405019 Gap-Solitonen in periodischen Potentialen).
  Die klassische AFM-Literatur zu praezedierenden Solitonen (Kosevich/Ivanov/Kovalev) liegt vor arXiv, hier nur [L?].
  Erwartung A8 (1005.2049): praezedierende Solitonen im AFM nahe Spin-Flop, keine BIC-Innenmoden. A9 (nlin/0405019):
  Innenmoden aus den Bandkanten, keine eingebetteten.
- A8 1005.2049 (Nietz 2010) bestaetigt: "precessing ball solitons" im einachsigen AFM am Spin-Flop, keine Innenmoden.
- **A9 teilweise VERLETZT (Richtung):** nlin/0405019 (Pelinovsky/Sukhorukov/Kivshar 2004, PRE 70, 036618) [A-Abstract]:
  Gap-Solitonen haben Innenmoden aus den Bandkanten; "when they overlap" mit den Baendern des invertierten Spektrums,
  "complex eigenvalues give rise to oscillatory instabilities". Erwartet: "keine eingebetteten". Befund: Eingebettet
  werden sie dort sehr wohl, aber in den Zweig entgegengesetzter Krein-Signatur, und dann instabil statt still.
  Zusammen mit Chugunova/Pelinovsky: Bei Gap-Solitonen ist das Standardschicksal einer eingebetteten Innenmode die
  oszillatorische Instabilitaet. Korrigierte Erwartung: Ob eine eingebettete Mode strahlt (Resonanz, stille Stellen
  moeglich) oder instabil wird, entscheidet die Krein-Signatur relativ zum Kontinuum -> Moderator M3.
- K18-K20 Erwartungen (24-Monats-Suche, nur arXiv): K18 abs:"embedded eigenvalue" AND abs:Dirac: nur Mathematik
  (Spektraltheorie), keine Leiter. K19 abs:"bound state in the continuum" AND (Q-ball/oscillon/kink): Kink-Arbeiten
  (Evslin u. a.), keine Q-Ball-Leiter. K20 abs:"gap soliton" AND abs:Bragg, neueste: keine Innenmoden-Messung.
- K18-K20 Befunde (Titel [S]): K18 nur Spektraltheorie linearer Dirac-Operatoren 2024/2025 (2404.08218, 2410.12467,
  2509.03627) und 2006.03345 (Dirac mit punktfoermiger Nichtlinearitaet, 2020). K19: seit 2024 kein arXiv-Abstract mit
  "bound state in the continuum" und Q-ball/oscillon/kink/solitary wave (einziger Treffer 2022). K20: seit 2023 keine
  Bragg-Gap-Soliton-Arbeit unter diesen Woertern. Erwartungen K18-K20 bestaetigt (nur arXiv, nur Abstract-Woerter).
- Gegensweep-Pruefung G1 (lokal): RUNDE-10.md KREIN-1: alle acht stillen Moden positive Krein-Signatur, "Neben den
  Stellen werden die Moden zu abklingenden Resonanzen, nie zu wachsenden". Passt zu M3.
- Gegensweep-Pruefung G2 (Quelle): math/0504442 Z. 510-512 [A]: CME-Kontinuum "|Im(lambda)| > 1 - omega and
  |Im(lambda)| > 1 + omega". Kanalbild der CME = unseres (bestaetigt).
- A10 Erwartung (vor Abruf 2006.03345-Abstract): punktfoermige NLD, +-2 omega i, Stabilitaetsgrenzen; keine Leiter.
- **A10 VERLETZT (Kern):** 2006.03345 [A-Abstract] (NLD mit punktfoermiger Soler-Nichtlinearitaet): Ein Bruch von
  SU(1,1) bei erhaltener Paritaet erhaelt die Spektralstabilitaet; ein Bruch von SU(1,1) UND Paritaet "destroys the
  stability of weakly relativistic solitary waves", durch "bifurcations of positive-real-part eigenvalues from the
  embedded eigenvalues +-2 omega i". Erwartet hatte ich (E2b, stillschweigend): ohne Symmetrie wird aus +-2 omega i eine
  gedaempfte Resonanz mit moeglichen isolierten Nullstellen wie bei uns. Befund: Dort wird sie INSTABIL.
  Voller Analysezyklus:
  - Deutung [ES]: Instabilitaet aus einem eingebetteten Eigenwert gibt es im Hamiltonschen Fall nur bei
    entgegengesetzter Krein-Signatur zum Kontinuum. Bei Dirac hat der Zweig negativer Frequenz negative Energie
    (Beitrag (nu - omega)|c|^2 < 0); bei Klein-Gordon traegt der Antiteilchen-Kanal positiv bei
    (KREIN-1: E_2 = 2 rho[(omega + rho)||a||^2 + (rho - omega)||b||^2] > 0).
  - ~~Drei unabhaengige Quellen~~ Drei Quellen (Berichtigung beim Berichtschreiben: nicht unabhaengig, zwei teilen den
    Mitautor Pelinovsky und den CME-Rahmen) zeigen dasselbe Muster fuer Dirac-artige Systeme (erste Zeitableitung): 2006.03345
    (NLD), math/0504442 (CME, komplexe Quartette nach Kontinuumskollision), nlin/0405019 (Gap-Solitonen,
    "overlap" mit invertiertem Spektrum -> oszillatorische Instabilitaet).
  - Korrigierte Erwartung: Dirac-artige Laborsysteme (Bragg-Gitter, binaere Arrays, BEC-Gap-Solitonen in
    CME-Naeherung) liegen im Regime "eingebettete Innenmode -> oszillatorische Instabilitaet"; unsere Leiter kann dort
    hoechstens als Folge isolierter Stabilitaetspunkte (Wachstumsrate ~ |g|^2 mit Nullstellen) auftreten [H]. Das
    KG-Regime (zweite Zeitableitung, positive Energie) braucht ein Laborsystem mit Lorentz-artiger Dynamik:
    Antiferromagnet [H].
- V2 Erwartung (vor Volltext 2609.32059): AFM-Modell Lorentz-artig (zweite Zeitableitung), Q-Ball-Fenster
  symmetrisch in omega, keine Linearisierung um den Q-Ball, keine Innenmoden.
- V2 Befund 2609.32059 Volltext [A, grep-Lesung] (sha256 f0e9bcd5...): AFM-Dynamik "naturally second order in time
  and is therefore closely related to relativistic nonlinear sigma models" (Z. 62), "as in a relativistic nonlinear
  sigma model on S^2" (Z. 168); Spektralannahmen "We do not prove" (Z. 830); Gilbert-Daempfung "breaks the
  conservation of the corresponding charge", Realisierung braucht schwache Daempfung oder Spin-Torque-Antrieb
  (Z. 1543-1546). Bestaetigt V2 (keine Innenmoden-Analyse). Traegt den KG-Charakter des AFM [A].
- Rechenprobe von Hand (keine Werkzeuge) fuer F0: omega*(n=1) = 0,89313, 2 omega* = 1,78626, rho* - 2 omega* = -0,0417;
  omega*(n=2) = sqrt(0,6851) = 0,82771, 2 omega* = 1,65542, rho* - 2 omega* = +0,0350.
- Recherche geschlossen; ab hier Bericht oben.
- Nachtrag G3 (Gegensweep, vor Abruf): Erwartung an 2006.03345 Volltext: Das Wort "Krein" kommt vor und die
  Instabilitaet wird der Signatur von +-2 omega i relativ zum Kontinuum zugeschrieben (~50 %).
- G3 Befund 2006.03345 Volltext [A] (Boussaid, Cacciapuoti, Carlone, Comech u. a.; sha256 3d613322...): Das Wort
  "Krein" kommt NICHT vor (grep leer); Erwartung (~50 %) nicht eingetreten. Die Quelle begruendet die Instabilitaet so:
  Die +-2 omega i sind einfach; isoliert (|omega| < m/3) koennten sie die imaginaere Achse nicht verlassen; "only
  possible since in the unperturbed case these two eigenvalues are embedded"; Instabilitaet bewiesen fuer "weakly
  relativistic solitary waves (when omega < m is close enough to m)". Ausserdem: "The SU(1,1) symmetry is absent for
  the physically relevant Dirac-Maxwell system". Folge: Meine Krein-Lesart (Moderator M3) bleibt [ES], von der Quelle
  nicht ausgesprochen; die Quelle stuetzt nur "eingebettet + Symmetriebruch -> Instabilitaet (nahe omega = m)".

---
Ende: 2026-09-30 12:51:55 CEST (date, nach dem Schreiben des Berichts gemessen; innerhalb der Zeitbox bis 13:19:19).
Quellen-PDFs und Texte in quellen/, Pruefsummen in quellen/SHA256SUMS.txt; arXiv-API-Antworten als quellen/api-*.xml.
Regelvermerk: keine lokale Rechnung, kein python/awk/ssh/git/Peerbus, keine Unteragenten; nur curl (arXiv), pdftotext,
grep, sed, tr, paste, sha256sum.
