# DOSSIER CSP-STRING-L: Superstrings ohne Teilchen mit kontinuierlichem Spin, und was das fuer die Glieder 7 und 10 heisst

- feldforscher fuer claude-primary, Runde 39 (Karte RUNDE-37/csp-string-l/KARTE.md). Beginn 2026-10-04 11:06:12 CEST,
  Dossier geschrieben ab 11:20:12 CEST (beides date). Arbeitsfeld mit allen Zwischenschritten: ARBEITSFELD.md.
- 9 von 10 Abrufen (einer davon leer), keine Websuche, kein python/awk/perl. Lokale Kopien und Hashes: quellen/SHA256SUMS.txt.
- Kennzeichen: [S] am Volltext selbst gelesen (Seite bzw. txt-Zeile), [Sa] nur Abstract selbst gelesen, [L?] Gedaechtnis,
  [ES] eigener Schluss, [H] Hypothese.

## Ergebnis zuerst (Kurzfazit)

1. **Papier [S]:** arXiv:2610.00745v1 (Alabbasi/Quevedo, 30.09.2026, unbegutachtet) rechnet in d = 10 (Lichtkegel, NSR) nach:
   T^i annihiliert alle masselosen Zustaende offener, geschlossener (IIA/IIB) und heterotischer Strings. Also keine CSP, perturbativ.
2. **Neu ist nur die Rechnung [S]:** Superstring-Fassung und Falsifikationslesung stehen schon bei Font/Quevedo/Theisen 2013
   (S. 2, S. 6). Ausnahmen laut Autoren: tensionslose Strings und nichtperturbative Effekte (S. 3, S. 13).
3. **E4:** Die CEMZ-Kopplung 7-10 bleibt (2610.00745 und FQT behandeln weder Kausalitaet noch CEMZ). "Getrennt" stimmt nicht: Im perturbativen
   String schliessen sich CSP und String aus. [H] Beide haengen an "endlich vielen Zustaenden je Massenstufe". Diese Annahme
   waehlt 2026 im maximal supersymmetrischen Gravitations-Bootstrap den String gegen eine Turm-Ecke mit allen Spins bei einer
   Masse ([S] 2607.14230). Wo sie faellt (tensionsloser String, Savvidy [Sa]), erscheinen CSP, und Spin 2 ist nicht mehr ausgezeichnet.
4. **Kompass [S]:** Der CSP-Zweig fuer das Graviton ist schwaecher als notiert. On-shell gibt es keine CSP-Graviton-Kopplung und
   keine CSP-Gravitonen (BDR 2025, S. 12). Gelockert verletzen CSP das Aequivalenzprinzip ab 1/rho. Die CSP-Gravitation ist nur linear.

## Erwartungen mit Ausgang und Fundstelle

| Nr | Erwartung (Kurzform) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | 2610.00745: perturbative Superstrings enthalten keine CSP | **eingetroffen**, genauer: gezeigt fuer alle masselosen Zustaende offener, geschlossener (IIA/IIB) und heterotischer NSR-Strings in d = 10, Lichtkegel, perturbativ | 2610.00745 Abstract; Abschn. 4-6, S. 6-12; Schluss S. 12 [S] |
| E2 | CSP-Graviton-Kopplung offen oder stark eingeschraenkt | **eingetroffen, schaerfer:** on-shell unmoeglich (BDR); gelockert moeglich, dann Verletzung des Aequivalenzprinzips oberhalb 1/rho; CSP-Graviton nur linear | BDR S. 12 (txt Z. 635-642), S. 26, S. 31-32 [S]; KST txt Z. 52-58, 834-837 [S] |
| E3 | CEMZ: neben Strings nur Tuerme massiver hoeherer Spins; CSP nicht behandelt | **Teil "CSP nicht behandelt" eingetroffen** (CEMZ-Volltext v1: "continuous" nur einmal, im Koordinatensinn, Z. 358). Teil 1 hier nicht neu geprueft; dazu passt: Im Bootstrap 2026 ist die Alternative zum String ein Einmassen-Turm aller Spins | lokale CEMZ-Kopie [S, grep]; 2607.14230 S. 4-5 [S] |
| E4 | CSP-Ausweg vom String-Ausweg getrennt; Kopplung 7-10 bleibt; ein weiterer, schlecht verstandener Zweig | **teilweise.** Kopplung 7-10 bleibt (eingetroffen). "Getrennt" **nicht eingetroffen**: gegenseitiger Ausschluss im perturbativen String und [H] gemeinsame Endlichkeitsannahme. "Schlecht verstanden" eingetroffen, praezisiert durch das On-shell-No-go | 2610.00745 S. 3 (Z. 128-129, 152-154), S. 12 (Z. 921-927); FQT S. 2; 2607.14230 S. 5; BDR S. 12 [S] |
| E5 | Argument wie FQT ueber Endlichkeit; Grenzen genannt; kein CEMZ | Methode **verletzt** (explizite Modenrechnung statt Endlichkeit); Grenzen und "kein CEMZ" eingetroffen; GSO kommt nicht vor | 2610.00745 S. 4-13 [S, grep] |
| E6 | Ergebnis nicht neu (FQT 2013) | **eingetroffen** | FQT S. 2, S. 5-6 [S] |
| E7 | keine nichtlineare CSP-Gravitation | nach Recherchestand **nicht belegt** (keine solche Arbeit in 24 Monaten per arXiv-API); kubische Vertices CSP-ganzzahliger Spin gibt es (Metsaev), on-shell-No-go dagegen (BDR) | A4-Liste [Sa]; Metsaev 2510.05011, 2505.02817 [Sa]; BDR [S] |
| E8 | "continuous spin" fehlt im CEMZ-Text | **eingetroffen** | lokale Kopie 1407.5597v1.txt [S, grep] |
| E9 | CSP-Graviton loest CEMZ nicht automatisch | **ungeprueft**: keine Arbeit gefunden, die CEMZ fuer CSP-Gravitonen untersucht. Nachbarbefund: BDR rechnen die gravitative Zeitverzoegerung fuer CSP als **Sonde** (nicht als Graviton); sie bleibt "always ... positive, and even finite" | BDR S. 26 (txt Z. 1557-1558) [S] |
| E10-E21 | Einzelerwartungen je Abruf | siehe ARBEITSFELD.md Abschn. 3-4; Verstoesse unten | - |

## Erwartungsverstoesse (das Wichtigste zuerst)

**V1 (gross): Die String-Auswahl im Gravitations-Bootstrap haengt an derselben Endlichkeit, die CSP ausschliesst.**
Erwartet hatte ich, dass CSP und massiver Turm zwei getrennte Themen sind. Gefunden [S]: Berman, Caron-Huot, Chandra, Elvang,
Herderschee, Lin, Morales (arXiv:2607.14230v1) finden fuer N = 8-Supergravitation zwei Ecken. Ihre Voraussetzungen sind
schwach gekoppelte EFT in D = 4, Faktorisierung auf Baumniveau und die Bedingung "peculiar parity". Die eine Ecke ist der
Virasoro-Shapiro-String, die andere eine "Infinite Spin Tower"-Amplitude, die "states of every spin J = 0, 2, 4, ... at
the same mass m" austauscht (S. 4, Gl. 1.7). "Requiring that only finitely many spins appear at the mass gap removes all
IST amplitudes" (S. 5). Die IST ist der Virasoro-Shapiro-Ausdruck "with all zeta_k formally replaced by 1" (S. 24,
Gl. 5.14-5.15). Dasselbe sagen Huang/Wan/Wang/Zhou (arXiv:2610.02124v1 = Pool S3) [Sa]. Sie setzen dafuer maximale Supersymmetrie,
eine Skalarparitaet bei sechs Punkten sowie "explicit analytic and positive dispersive assumptions" voraus: "Finite-spin support at the lowest
massive pole is therefore an additional assumption required to select the Virasoro--Shapiro amplitude". Auch die
nichtstringigen UV-Amplituden von Huang/Remmen (2203.00696) haben "accumulation points in the form of infinite towers of
states on each mass pole" [Sa]. 2610.00745 verortet seinen Kern selbst in "forbidding an infinite spectrum of massless
particles" (S. 12, Z. 921-922) [S]. **Korrigierte Erwartung [H]:** Der CSP-Zweig und der String-Zweig von Glied 7 sind
ueber eine gemeinsame Voraussetzung gekoppelt: endlich viele Zustaende je Massenstufe.

**V2 (gross): Im einzigen String-Regime mit CSP gibt es keine Gravitation mehr.** Erwartet: tensionslose Strings als
blosse Ausnahme. Gefunden [Sa]: Savvidy (hep-th/0310085, IJMPA 19 (2004) 3171; von FQT als Ref. [9] zitiert): D = 13, alle
Teilchen masselos. "The ground state is infinitely degenerated and contains massless gauge fields of arbitrary large
integer spin." "The excitation levels realize CSR representations ... with an infinite number of helicities." Vermutung:
Diese Stufen sind Nullzustaende. Und "in this model there is no gravity". Mourad (hep-th/0410009) [Sa]: Seine
CSP-Stringwirkung ist "identical to the tensionless extrinsic curvature action proposed by Savvidy", mit kritischer
Dimension 28. **Folge [ES]:** Wo Strings CSP tragen, sind zugleich Glied 7 im Wortlaut (masselose Spins jeder Hoehe) und
die Endlichkeit verletzt, und das Spin-2-Feld hat keine besondere Rolle. Das stuetzt V1.

**V3 (gross): Fuer Gravitonen gibt es ein publiziertes On-shell-No-go.** Erwartet: "offen oder eingeschraenkt". Gefunden
[S]: Bellazzini/De Angelis/Romano (arXiv:2406.17017v3, JHEP 05 (2025) 166), S. 12: "No on-shell coupling of CSP to
(massless) gravitons is possible" und "CSPs have no on-shell three-point self-interactions, e.g. no CSP-like gravitons".
S. 31: "2-CSPs-1-graviton amplitudes" verschwinden. Das gilt unter Poincare-Invarianz, Kleingruppen-Kovarianz, Analytizitaet
und gutem Hochenergieverhalten. Mit gelockerter Faktorisierung (massives Graviton, dann Masse gegen null) verletzen CSP
"the equivalence principle at distances larger than the spin scale, while preserving causality" (S. 26, S. 32).
Kundu/Schuster/Toro (2503.03817v2) zitieren diese Arbeit nur als "complementary path" (txt Z. 35-37) und bleiben "limited
to leading order in Newton's gravitational constant" (Z. 52-58) [S]. **Folge fuer den Kompass:** Der CSP-Ausweg aus
Glied 7 stoesst fuer das Graviton an Glied 9 (Selbstkopplung). Fuer CSP als Materie stoesst er an Glied 3 (gleiches
Fallen).

**V4 (mittel): Die Falsifikationslesung steht seit 2013 da.** FQT S. 2: "if these states are detected experimentally, all
string theory constructions known so far would be ruled out" [S]. 2610.00745 wiederholt es (S. 3, Z. 128-129, 152-154).
Die Rahmung hat sich verschoben: 2013 gehoerten interagierende CSP-Feldtheorien "to the swampland" (FQT S. 3), 2026
"bypasses the swampland programme" (2610.00745 S. 3).

**V5 (mittel, Projektstand):** Fuer das Photon gibt es eine vorgeschlagene Grenze. Reilly/Russo/Schuster/Toro
(2505.15890v2) [Sa] leiten aus dem 21-cm-Uebergang Abweichungen "proportional rho^2 alpha^2/omega^2" ab, "suggesting
experimental constraints rho <~ 1 meV". Der 24.09.-Bericht kannte nur einen Beispielwert. Fuer das Graviton gibt es weiter
nur Empfindlichkeiten. Der Satz von 2610.00745, die Abwesenheit sei "an experimental result" (S. 12, Z. 921-924), ist
also Nichtnachweis, kein Befund.

**V6 (klein): Innerer Widerspruch in 2610.00745.** S. 4 (Z. 230, 233): Beide Beitraege verschwinden "separately" bzw.
"independently". S. 12 (Z. 928-929): "the explicit cancellation between bosonic and fermionic oscillator contributions ...
is what fixes T^i = 0". Nach den eigenen Abschnitten 4-5 hebt sich nichts auf. [ES] Das schwaecht die Behauptung
"distinctly stringy property" (S. 12, Z. 925).

**V7 (klein): Offener Theoriewiderspruch zur kubischen Ebene.** Metsaev (2510.05011v2, JHEP 03 (2026) 061) [Sa]: "All
parity-even cubic vertices for self-interacting continuous-spin fields ... are obtained". Dagegen BDR [S]: "no on-shell
three-point self-interactions". Vermutete Moderatoren: Funktionenraum (Distributionen bzw. Vektor-Superraum gegen
analytische Funktionen der Bispinoren), gleiche oder verschiedene rho der drei Beine, Lichtkegel- gegen komplexe
Kinematik. Nicht aufgeloest.

Bestaetigt, je eine Zeile: CEMZ ohne CSP (E8); Schuster/Toro: Helizitaetskorrespondenz, Weinberg-Witten nicht anwendbar
(1302.1577 [Sa]); Longo/Morinelli/Rehren: keine Lokalisierung unendlicher Spins in Doppelkegeln (1505.01759 [Sa]); KST
nur linear (E21).

## Literaturstand

- **Kernarbeit [S]:** Alabbasi, Quevedo 2026, arXiv:2610.00745v1. Kriterium: CSP haben sum_i (Pi^i)^2 != 0 (S. 4,
  Z. 195). Im Bezugssystem p^i = 0 reicht T^i|psi> = 0 (S. 4, Z. 220-221). NS-Sektor: Gl. 24-33 (S. 6-8), R-Sektor:
  Gl. 43-47 (S. 9-10), geschlossen und heterotisch inklusive Stromalgebra J^a_{-1}: Gl. 48-56 (S. 11-12). "Compactification-
  independent" wird behauptet (S. 3, Z. 152). Gerechnet ist nur d = 10 plus die heterotische innere Stromalgebra; GSO kommt
  im Text nicht vor. Turm-Bezug nur in Fn. 1 (S. 3) mit Duff/Pope/Stelle 1989 und Huang/Remmen 2022, **ohne CEMZ**. In der
  Danksagung (S. 13): "We counted with the assistance of Claude for checking our computations".
- **Vorlaeufer [S]:** Font, Quevedo, Theisen 2013, arXiv:1302.4771 (Fortsch. Phys. 62 (2014) 975 laut KST Ref. [26]).
  Kernargument ist ein Multiplett-Argument: "if the massive representations do not carry a continuous label the massless
  states should not carry it either" (S. 2). Die Rechnung T^i|j> = 0 ist ausdruecklich "a consistency check" (S. 5).
  Tensionsloser Grenzfall "even if true it does not correspond to the standard string constructions" (S. 3).
- **CSP-Gravitation:** Kundu/Schuster/Toro 2503.03817v2 (laut 2610.00745 Ref. [10] erschienen als PRD 113 (2026) 076017)
  [S], nur linear. Bellazzini/De Angelis/Romano 2025 [S]: On-shell-No-go, gelockerte Fassung mit Verletzung des
  Aequivalenzprinzips. Metsaev 2025/2026 [Sa]: kubische Vertices; in 2505.02817 "complete for the dimensions of space-time
  greater than four". Basile/Bekaert/Figueroa/Skvortsov 2606.28245 [Sa]: "CSP amplitudes can be understood as the
  infinite-spin limit of amplitudes of massive particles". Dazu BDR Fn. 29 [S]: SU(2) "contracts to CSPs ISO(2) for m -> 0
  and j -> infinity with mj held fixed".
- **Feldtheorie ohne Strings [Sa]:** Longo/Morinelli/Rehren (CMP 345 (2016) 587): "local fields generating them from the
  vacuum state cannot exist". In einer wechselwirkenden Theorie mit zyklischem Vakuum fuer Doppelkegel-Algebren gibt es
  keine unendlichen Spins. Voraussetzung ist die Bisognano-Wichmann-Eigenschaft; ohne sie gibt es ein Gegenbeispiel "with
  continuous particle degeneracy".
- **24-Monats-Suche (Regel 7)**, arXiv-API statt Websuche, 80 Treffer bis 2024-09-18: Ausser 2610.00745 keine Arbeit zu CSP
  in Strings endlicher Spannung. Keine nichtlineare CSP-Gravitation. "Nicht gefunden" ist ohne Websuche schwaecher.

## Regime und Moderatoren (Regel 1)

| Regime | Voraussetzung | Spektrum | Graviton | Beleg |
|---|---|---|---|---|
| S: Strings mit Spannung, perturbativ | endlich viele Zustaende je Stufe | rho = 0 fuer alle masselosen Zustaende; unendlicher massiver Turm; im Bootstrap: Virasoro-Shapiro | Helizitaet 2, CEMZ-Bruecke zu Glied 7/10 | 2610.00745, FQT [S]; 2607.14230 [S] |
| T: tensionslose Strings (Savvidy, Mourad) | Spannung 0, Grundzustand unendlich entartet | masselose Spins jeder Hoehe; CSR auf Anregungsstufen (vermutlich Nullzustaende); D = 13 bzw. 28 | "no gravity" (Savvidy) | hep-th/0310085, hep-th/0410009 [Sa] |
| B: Bootstrap ohne Endlichkeit | unendlich viele Spins bei einer Masse bzw. Haeufungspunkte | IST-Ecke, Huang/Remmen-Amplituden | Einstein bei niedriger Energie | 2607.14230 [S]; 2610.02124, 2203.00696 [Sa] |
| C: CSP-Gravitation | Helizitaet nicht lorentzinvariant (rho_g > 0) | ein Teilchen mit allen Helizitaeten | linear gekoppelt; on-shell nicht selbstkoppelnd (BDR) | KST, BDR [S] |

- **Moderatoren:** Stringspannung; Endlichkeit der Entartung je Massenstufe [H]; perturbativ gegen nichtperturbativ;
  strenge gegen gelockerte On-shell-Faktorisierung und Analytizitaet (BDR gegen KST und Metsaev).
- **Regel 6 [H]:** Zu "kein CSP" fuehren mindestens drei Wege: (1) Oszillatoralgebra perturbativer Strings, (2) Lokalitaet
  in beschraenkten Gebieten (Longo/Morinelli/Rehren), (3) endlich viele Zustaende je Impuls (Wigner/Weinberg-Lesart in
  FQT S. 2). Der String ist also nicht "die Ursache", sondern ein Fall der gemeinsamen Groesse "Zahl der Zustaende je
  Stufe bzw. Lokalisierbarkeit". **[ES] Vorbehalt:** Fuer die masselose Stufe ist der Schluss "endlich -> rho = 0"
  fast trivial, denn eine CSP-Darstellung ist bei festem Impuls unendlichdimensional. Nicht trivial ist nur die Verbindung
  "endlich auf den massiven Stufen <-> rho = 0 auf der masselosen". Dafuer gibt es nur das Multiplett-Argument (FQT) und
  die Kontraktion m -> 0, j -> unendlich (BDR Fn. 29; Basile u. a.).

## Unterscheidungspunkte (Regel 2)

- **U1 (CSP-Graviton gegen Helizitaet-2-Graviton):** Abweichung O(rho_g/omega) bei GW-Frequenzen nahe rho_g.
  Empfindlichkeit ~1e-14 eV (Bodendetektoren) bzw. ~1e-24 eV (Pulsar-Timing), Projektstand 24.09. Keine Schranke. Im
  Prinzip zugaenglich, Antwortfunktion fuer Pulsar-Timing fehlt weiter.
- **U2 (perturbative Strings gegen CSP in der Natur):** irgendein masseloses Teilchen mit rho > 0. **Einseitig:** Ein
  positiver Befund wuerde laut FQT/2610.00745 alle perturbativen Stringkonstruktionen ausschliessen. Ein Nullbefund stuetzt
  Strings nicht, denn Lokalitaet (Weg 2) sagt dasselbe voraus. Photon heute: vorgeschlagene Grenze rho <~ 1 meV.
- **U3 (String gegen IST-Ecke):** Zahl der Spins an der ersten Massenstufe. Liegt an der Stringskala, praktisch
  unzugaenglich.
- **U4 (Regime S gegen T):** Spannung gegen null. Unzugaenglich. [ES] Da Regime T nach Savvidy keine Gravitation hat,
  liegt die beobachtete Welt (mit Gravitation) nicht in diesem Modell. Das gilt nur fuer Savvidys Wirkung.
- **U5 (BDR gegen Metsaev):** Funktionenraum der Dreipunktamplitude. Rein mathematisch, empirisch nicht unterscheidbar.

## Projektbezug (Hypothesen, nicht kleingeredet)

- **[H] Kompass, Glieder 7 und 10:** Die CEMZ-Kopplung (massiver Turm <-> geaenderte Drei-Graviton-Kopplung) bleibt
  unveraendert und so bedingt wie in den Berichtigungen vom 30.09. und 01.10. Neu ist eine **Ausschlusskante** zwischen den
  zwei Auswegen aus Glied 7: massiver Turm/String (Regime S) gegen CSP (Regime C). Beide haengen an einer Annahme, die in
  der Zehnerkette nicht steht: **endlich viele Zustaende je Massenstufe bzw. Impuls**. Vorschlag an die Leitung: Diese
  Annahme neben "feste Helizitaet" (WARUM-SPIN-2.md, Nachtrag 24.09., Z. 538) als Querannahme zu Glied 7 fuehren. Sie scheitert, wenn eine
  Theorie mit endlicher Entartung je Stufe CSP-Austausch zeigt oder wenn die IST-Ecke mit CSP nichts zu tun hat (Karte
  unten).
- **[H] CSP-Zweig kostet andere Glieder:** fuer das Graviton Glied 9 (keine On-shell-Selbstkopplung, BDR S. 12), fuer
  CSP-Materie Glied 3 (Helizitaeten fallen verschieden, BDR S. 26). Glied 3 ist das am besten gemessene Glied der Rangliste
  (eta ~ 1e-15). Der "vierte Ausweg mit Messfolge" vom 24.09. ist damit schwaecher als dort beschrieben.
- **[H] "Strings als Pfeilfaeden":** Ein CSP-Feld ist in der Feldtheorie gerade an einem halb-unendlichen raumartigen
  Strahl lokalisiert ("string-localized", Mund/Schroer/Yngvason, von FQT als Ref. [7] genannt) und nie in einem
  beschraenkten Gebiet (Longo/Morinelli/Rehren). Ein gerichteter Faden von einem Punkt ins Unendliche ist formal genau
  dieses Gebiet. Pruefbare Folge: Sind Finns Pfeilfaeden endlich oder geschlossen, schliesst Longo/Morinelli/Rehren
  unendliche Spins aus (unter Bisognano-Wichmann). Nur halb-unendliche Faeden lassen CSP-artige Inhalte zu. Diese
  Hypothese kann an der Geometrie der Faeden scheitern.
- **[H] Netze (Tetraedernetz, TENSOR-EIS):** Gitter mit endlich vielen Freiheitsgraden je Platz liegen von selbst im Regime
  "endlich je Stufe". Ein dort entstehendes Spin-2 sollte feste Helizitaet haben. Das passt zu TENSOR-EIS-N ("nur
  Helizitaet 2 mit positiver Energie" auf der Zwangsflaeche, RUNDE-36.md Ernte). Einschraenkung: Ohne Lorentz-Boosts ist
  rho auf dem Gitter gar nicht definiert. Die Aussage ist deshalb nur eine Erwartung fuer den Kontinuumsgrenzfall.
- **[H] HAGEDORN-1/2:** Q-Ball-Ringe mit Spannung gehoeren, wenn sie stringartig sind, zu Regime S und lassen kein CSP
  erwarten. Ein Bezug zu Glied 7 ergaebe sich erst bei unendlicher Entartung je Stufe. Davon zeigt HAGEDORN-1 nichts.

## Kartenvorschlag (kann scheitern)

**IST-KONTRAKTION-L (Schreibtisch, zuerst Ableitbarkeitsprobe):** Ist die "Infinite Spin Tower"-Ecke des
Gravitations-Bootstraps (2607.14230 Gl. 1.7/5.14) im Grenzfall m -> 0, J -> unendlich mit mJ fest ein CSP-Austausch
(BDR, Basile u. a.)?
- **Erster Schritt:** Pruefen, ob Basile/Bekaert/Figueroa/Skvortsov (2606.28245, Volltext) das fuer Einmassen-Tuerme schon
  zeigen. Wenn ja, ist die Karte reine Literatur, kein neuer Befund.
- **Scheiterregel, vorab:** Die Kopplungshypothese V1 ("CSP und String-Auswahl haengen an derselben Endlichkeit") wird
  gestaerkt, wenn der Grenzfall der IST-Residuen die Helizitaetsstruktur einer CSP-Austauschamplitude mit endlichem rho
  ergibt. Sie faellt, wenn der Grenzfall verschwindet, divergiert oder nur endlich viele Helizitaeten liefert. Ist der
  Grenzfall nicht wohldefiniert, ist die Karte ergebnislos und so zu melden.

## Gegensweep-Befunde (Regel 4)

1. Projekt-grep der Leitung: Der Treffer in RUNDE-23/bildung-3d/PLAN.md ist ein Falschtreffer ("scipy CubicSpline", Z. 111).
   **Geprueft.**
2. "String" heisst Stringtheorie: **geprueft, nein.** CSP-Felder sind feldtheoretisch "string-localized". Ebenso ist
   "infinite spin" in der A4-Liste oft der klassische Drehimpulsgrenzfall (z. B. 2506.23974) oder das n-Koerper-Problem.
3. 2610.00745 ist die geltende Fassung: **geprueft** (Stempel v1, 30 Sep 2026, ueber /pdf/ geladen).
4. Ein CSP-Graviton vertraegt sich mit dem On-shell-No-go: **geprueft (A9), nein.** KST gehen auf BDR nur als
   "complementary path" ein.
5. Die Modenrechnung von 2610.00745 stimmt: **nicht geprueft.** Gemildert durch das Endlichkeitsargument [ES] und FQT S. 5.
6. "Abwesenheit in der Natur ist gemessen": **geprueft, nein** (V5).

## Kalibrierung

- **(a) Gemessen:** nichts zu CSP-Gravitonen. Fuer das Photon eine vorgeschlagene Grenze rho <~ 1 meV, ohne Datenanpassung
  im Abstract. Dass perturbative Strings keine CSP enthalten, ist eine Rechnung, keine Messung.
- **(b) Nuetzlich verdichtet:** die Regime S, T, B und C; die Ausschlusskante CSP <-> perturbativer String; die
  Endlichkeitsannahme als gemeinsame Groesse [H]; die Kosten des CSP-Zweigs an den Gliedern 9 und 3.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - in 2610.00745: "an experimental result" (S. 12), "compactification-independent" (S. 3, nur teilweise gerechnet),
    "distinctly stringy" (S. 12, gegen die eigenen Abschnitte 4-5);
  - im Projekt: "CSP als vierter Ausweg mit Messfolge" (seit 24.09.). Das ist ohne Bezug auf das On-shell-No-go weitergetragen
    worden.
- **Warnzeichen:** Meine Sicherheit, dass CSP und String ueber die Endlichkeit gekoppelt sind, stieg waehrend der Recherche.
  Zugleich zerfiel die Frage in vier Regime. Ausserdem ist der masselose Teil dieser Kopplung fast eine Tautologie. Belastbar
  ist nur: Endlichkeit ist im Bootstrap eine Annahme, und wo sie in Strings faellt, erscheinen CSP. Die Verbindung zwischen
  massiven Stufen und rho = 0 ist heuristisch.

## Offene Fragen

1. Gilt das On-shell-No-go von BDR auch gegen die lineare CSP-Graviton-Kopplung von KST? Oder umgeht deren Strom-Formalismus
   die Analytizitaetsannahme? Keine der zwei Arbeiten beantwortet das.
2. BDR gegen Metsaev: Gibt es kubische Selbstkopplungen von CSP oder nicht? Welcher Funktionenraum ist physikalisch?
3. Ist die IST-Ecke ein Grenzfall von CSP-Austausch? (Karte oben.)
4. Gilt "keine CSP" fuer allgemeine Kompaktifizierungen (beliebige innere CFT), fuer D-Bran-Sektoren und nach der
   GSO-Projektion? 2610.00745 behauptet es, rechnet es aber nur teilweise.
5. Gibt es eine Datenschranke (nicht nur eine Empfindlichkeit) fuer rho_g? Und eine Pulsar-Timing-Antwortfunktion (F-7 vom
   24.09.)?
6. Ist 2505.15890 (Photon, rho <~ 1 meV) eine Datenanpassung oder eine Abschaetzung? Nur das Abstract ist gelesen.

## Selbstanzeigen

- Im Arbeitsfeld standen zuerst fuenf falsche Zeilennummern zu 2610.00745. Ich habe sie um 11:13 an der Quelle berichtigt
  und gestrichen, nicht geloescht.
- Zweimal stand zuerst eine geschaetzte Zeit im Arbeitsfeld: 11:19 statt 11:17:59 und 11:26 statt 11:24:00 (date). Beide sind
  gestrichen und berichtigt. Ebenso zwei BDR-Zeilenangaben: Das Zitat zur Zeitverzoegerung steht in Z. 1557-1558, die Passage
  in Z. 1554-1558.
- In einem Befehl stand der Tippfehler "awk2=0 head -0". Das ist eine Variablenzuweisung, kein awk-Aufruf.
- Abruf A3 lieferte ueber http 0 Byte. Er ist trotzdem als Abruf gezaehlt.
- Die Modenrechnung von 2610.00745 habe ich nicht nachgerechnet.
- Unabhaengigkeit: Die Autoren liessen ihre Rechnung von Claude pruefen, und diese Lesung stammt ebenfalls von einem
  Claude-Modell. Sie ist also nicht hausfremd.
- Nur am Abstract gelesen: Metsaev (2), Mourad (2), Savvidy, Huang/Remmen, Huang u. a. 2610.02124, Basile u. a.,
  Longo/Morinelli/Rehren, Reilly/Russo/Schuster/Toro 21 cm, Schuster/Toro 1302.1577. Die BDR-Seitenzahlen sind aus den
  Seitenmarken der pdftotext-Ausgabe erschlossen.
- Keine Websuche, nur die arXiv-API. "Nicht gefunden" ist entsprechend schwach.

## Quellenliste (Abrufstand 2026-10-04, Zeiten per date)

- Alabbasi, A.; Quevedo, F. (2026): Absence of Continuous Spin Particles in Superstring Theory. arXiv:2610.00745v1,
  https://arxiv.org/abs/2610.00745. Abgerufen 11:09:53, quellen/2610.00745.pdf, sha256 95166197...6a5250. [S, ganz]
- Font, A.; Quevedo, F.; Theisen, S. (2013/2014): A Comment on Continuous Spin Representations of the Poincare Group and
  Perturbative String Theory. arXiv:1302.4771, Fortsch. Phys. 62 (2014) 975, https://arxiv.org/abs/1302.4771. Abgerufen
  11:13:18, sha256 c74db148...4e4300. [S, ganz]
- Bellazzini, B.; De Angelis, S.; Romano, M. (2024/2025): Continuous-Spin Particles, On Shell. arXiv:2406.17017v3, JHEP 05
  (2025) 166, https://arxiv.org/abs/2406.17017. Abgerufen 11:16:24, sha256 130de128...04dfb51c. [S, Teile]
- Berman, J.; Caron-Huot, S.; Chandra, A. V.; Elvang, H.; Herderschee, A.; Lin, L. L.; Morales, R. (2026): Gravitational
  Effective Theories with Maximal Supersymmetry and a Peculiar Parity. arXiv:2607.14230v1,
  https://arxiv.org/abs/2607.14230. Abgerufen 11:16:16, sha256 d7a89495...c335efa5. [S, Teile]
- Kundu, S.; Schuster, P.; Toro, N. (2025/2026): First look at continuous spin gravity: Time delay signatures.
  arXiv:2503.03817v2, PRD 113 (2026) 076017 (laut 2610.00745 Ref. [10]), https://arxiv.org/abs/2503.03817. Abgerufen
  11:18:17, sha256 a2d7a61b...c2ee591. [S, Teile]
- Huang, Y.-t.; Wan, S.-L.; Wang, Z.-H.; Zhou, S.-Y. (2026): Infrared Consistency and the Uniqueness of String Amplitudes.
  arXiv:2610.02124v1, https://arxiv.org/abs/2610.02124. Abstract aus A4 (11:14:23). [Sa]
- Shao, L.-Q.; Vichi, A. (2026): Analytic Boundaries of Infinite-Spin-Tower Amplitudes from Hidden Zero. arXiv:2607.27300v2,
  https://arxiv.org/abs/2607.27300. Abstract aus A4. [Sa]
- Reilly, A.; Russo, A.; Schuster, P.; Toro, N. (2025): Hydrogen 21 cm Constraints on the Photon's Spin Scale.
  arXiv:2505.15890v2, https://arxiv.org/abs/2505.15890. Abstract aus A4. [Sa]
- Metsaev, R. R. (2025): Interacting massive/massless continuous-spin fields and integer-spin fields. arXiv:2505.02817v3,
  https://arxiv.org/abs/2505.02817. Abstract aus A4. [Sa]
- Metsaev, R. R. (2025/2026): Lorentz covariant on-shell cubic vertices for continuous-spin fields and integer-spin fields.
  arXiv:2510.05011v2, JHEP 03 (2026) 061 (laut 2610.00745 Ref. [16]), https://arxiv.org/abs/2510.05011. Abstract aus A3
  (11:13:30, sha256 423032e1...82b776068). [Sa]
- Basile, T.; Bekaert, X.; Figueroa, F.; Skvortsov, E. (2026): Spinor-helicity formalism for continuous-spin particles.
  arXiv:2606.28245v1, https://arxiv.org/abs/2606.28245. Abstract aus A3. [Sa]
- Schuster, P.; Toro, N. (2013): On the Theory of Continuous-Spin Particles: Helicity Correspondence in Radiation and
  Forces. arXiv:1302.1577v2, JHEP 09 (2013) 105, https://arxiv.org/abs/1302.1577. Abstract aus A3. [Sa]
- Longo, R.; Morinelli, V.; Rehren, K.-H. (2015/2016): Where Infinite Spin Particles Are Localizable. arXiv:1505.01759v3,
  CMP 345 (2016) 587, https://arxiv.org/abs/1505.01759. Abstract aus A3. [Sa]
- Mourad, J. (2005): Continuous spin particles from a string theory. arXiv:hep-th/0504118v1,
  https://arxiv.org/abs/hep-th/0504118. Abstract aus A3. [Sa]
- Mourad, J. (2004): Continuous spin and tensionless strings. arXiv:hep-th/0410009v3, https://arxiv.org/abs/hep-th/0410009.
  Abstract aus A5 (11:16:10, sha256 eb43a477...297a5dc8). [Sa]
- Savvidy, G. (2003/2004): Tensionless strings: physical Fock space and higher spin fields. arXiv:hep-th/0310085v2, IJMPA 19
  (2004) 3171, https://arxiv.org/abs/hep-th/0310085. Abstract aus A5. [Sa]
- Huang, Y.-t.; Remmen, G. N. (2022): UV-Complete Gravity Amplitudes and the Triple Product. arXiv:2203.00696v2, PRD 106,
  L021902, https://arxiv.org/abs/2203.00696. Abstract aus A5. [Sa]
- Camanho, Edelstein, Maldacena, Zhiboedov (2014/2016), arXiv:1407.5597. Nur lokale Codex-Kopie
  art-grenzen-20260921/cemz-gegenpruefung-codex-quellen/1407.5597v1.txt per grep. [S, grep]
- Nur zitiert, nicht gelesen: Mund/Schroer/Yngvason 2004 (math-ph/0402043, laut FQT Ref. [7]); Duff/Pope/Stelle 1989
  (laut 2610.00745 Ref. [21]).
- Arbeitsmaterial: arXiv-API-Suche quellen/search-A4.xml (11:14:23, sha256 186a885f...225bbe1f).

## Einfach gesagt

Eine neue Arbeit rechnet nach, dass die uebliche Stringtheorie keine Teilchen mit "kontinuierlichem Spin" kennt. Das sind
exotische masselose Teilchen, die alle Drehrichtungen zugleich in sich tragen. Fuer unseren Kompass heisst das: Die zwei
Notausgaenge aus der Regel "keine Kraftteilchen mit Spin 3 oder mehr" schliessen sich gegenseitig aus. Entweder ein
String mit unendlich vielen schweren Teilchen, oder so ein exotisches Teilchen, nicht beides. Beide Notausgaenge haengen
an derselben Frage: Gibt es auf jeder Energiestufe nur endlich viele Zustaende? Und der exotische Ausgang ist fuer die
Schwerkraft wackliger als gedacht, denn nach einer Arbeit von 2025 kann so ein Teilchen nach strengen Regeln gar nicht
richtig an Gravitonen ankoppeln.
