# ALT-1 (Runde 10): Alternativen fuer einen gebundenen Dreier mit Y-Knoten (Baryon-Vorbild)

- Bearbeiter: Anthropic-Code-Agent (Fable 5.1) fuer die Leitung claude-primary. Explorativ (v3). Nur Literatur und
  Handrechnung, keine Rechnung auf dem Rechner. Alles [H]: Vorbild, kein Proton, kein QCD, kein Eichfeld.
- Zeitkette (date, CEST): Beginn 11:57:55; Projektunterlagen bis 12:05; Vorab-Erwartungen 12:05:21 (A1) vor dem ersten
  externen Abruf; zweite Runde ab 12:09:47 (A1b); Bericht ab 12:19:00. Ende: siehe letzte Zeile.
- Belegstufen: [A] an der Quelle gelesen (Volltext, Stelle genannt), [A-W] nur Abstract an der Quelle, [S] nur
  Suchtreffer oder Erinnerung, [L?] nicht an der Quelle geprueft, [Hand] eigene Herleitung (Rechenweg im Arbeitsfeld),
  [P] Projektdatei, [ES] eigener Schluss, [H] Hypothese.
- Werkzeuge: WebSearch war erschoepft (200/200); alle Abrufe ueber arXiv-API (export.arxiv.org) und arXiv-Abstracts;
  drei Volltexte als PDF geladen und lokal mit pdftotext gelesen (nur IO, kein Interpreter).

## 0. Ergebnis in fuenf Punkten

1. **Das gesuchte Vorbild existiert in der Literatur, aber im Supraleiter:** Nitta, Eto, Fujimori, Ohashi, "Baryonic Bound
   State of Vortices in Multicomponent Superconductors", J. Phys. Soc. Jpn. 81, 084711 (2012), arXiv:1011.2552 [A, Volltext].
   Drei 1/3-quantisierte Wirbel, je einer je Komponente, mit linearer Josephson-Kopplung
   -gamma_ij |Psi_i||Psi_j| cos(theta_i - theta_j) und **Quartik je Komponente** (lambda_i/4)(|Psi_i|^2 - v_i^2)^2, bei
   **festgehaltenen** Wirbellagen: "the numerical solution indicates the Y-junction" (Abschn. 3, Abb. 2). Ohne Festhalten:
   "these vortices collapse to form a single integer vortex". Kein Vergleich E gegen Geometrie, eine Konfiguration.
   Die Eichung des Gesamt-U(1) ist fuer das Y nicht noetig: die relativen Phasen sind auch dort global (Abschn. 2).
2. **Bester Kandidat fuer unsere Formel: nicht der Rabi-Term, sondern die Quartik je Kanal** + c sum_a |psi_a|^4 mit
   **nachgestimmtem U** (S^2-Koeffizient b_0 = 1 + c/3, damit der gemischte Ball bei b = 1,167 bleibt) [ES, Hand A4].
   Grund: Y-1 scheiterte nicht an der Topologie (Y ist in der Z_2^2-Struktur erlaubt, PLAN 2.3 und A1), sondern am
   billigen entleerten Kern. Bei Nitta u. a. kostet das Entleeren (lambda/4) v^4 = 0,5 je Flaeche gegen Josephson-Energie
   gamma v^2 = 0,02: Faktor 25. Bei uns (g = 0,5): Kern 0,057 je Flaeche gegen Wand sigma_W = 0,41 je Laenge; die
   Abschirmung gewinnt [Hand]. Mit c allein (ohne Nachstimmen) sinkt S mit c, und das Verhaeltnis erreicht hoechstens ~1
   (Y-1 mit c = 0,4: Gegenwirbel an 11/12, passt). Mit c = 2 und b_0 = 1,667 liegt die Abschaetzung bei Faktor 2 bis 7
   zugunsten der Waende. **Preis:** der einkomponentige Q-Ball verschwindet (b_eff(N = 1) = b_0 - c < 0); U(3) bei g = 0
   geht verloren; der Grundzustand bei festem Q ist wieder vorab ableitbar (BERICHT-FARBEN C3), der Test misst deshalb
   die Netzform, nicht "wer gewinnt".
3. **Rabi-Term (Kandidat 1) nur als Zusatz, nicht als Traeger.** Bei g = 0 ist er beweisbar eine Basiswahl (KANDIDAT 2.3);
   die Literatur bestaetigt das: im U(N)-symmetrischen Fall ist der Dreier "an axisymmetric giant vortex ... a CP^{N-1}
   skyrmion" (Eto/Nitta 2013 [A], S. 2), also unser "Beutel". Mit g != 0 hebt er die Kernkosten linear (epsilon S/2 je
   Flaeche), ist aber durch die Vakuumschranke auf epsilon < 0,32 (g = 0,5) begrenzt [Hand]; das reicht nach der
   Abschaetzung gerade zum Gleichstand. Er wuerde ausserdem Z_2^{N-1}, die Fourier-Gitterregel und den Paartransfer
   (sin 2 Delta -> sin Delta) aendern. Als dritter Arm im Test sinnvoll, weil er der Wandtyp der Literatur ist.
4. **Kleinster Rechentest (Abschnitt 5, nicht gerechnet):** y1.py mit Parameter b_0 (drei Stellen) und optional epsilon
   (zwei Zeilen); g = 0,5, weiter Ring r < 4; Arm B: c = 2, b_0 = 1,667; Arm A: c = 1, b_0 = 1; Arm C: epsilon = 0,3.
   Geometrien: gleichseitig 9 und 12, kollinear 8, Meson 6/9/12. Etwa 15 Laeufe, je 3 bis 5 min P4000. Vorab: Arm B ohne
   Gegenwirbel in >= 4 von 5, Kopplungsdefizit auf den Steiner-Armen, E(12) - E(9) = 3 bis 5. **Scheiterregel:** Arm B mit
   Gegenwirbel in >= 2 von 3 Dreiern oder flaches Meson (Steigung 9 -> 12 < 0,3 x Steigung 6 -> 9) => "Quartik traegt
   das Y in dieser Formelfamilie nicht"; Waende auf den Kanten statt auf den Armen => "Dreieck", kein Scheitern.
5. **Einordnung nach Regel 1 (zwei Regime, drei Felder):** Kompakt gegen ausgedehnt, Moderator = Abstand gegen Wand-
   bzw. Kernbreite. Gitter-QCD: gefuelltes Dreieck bei kleinen, Y bei grossen Abstaenden (Bissey u. a. 2007 [A-W]; daher
   die Lager Takahashi/Y gegen Alexandrou/Delta). BEC: freie Trimere kompakt, "we cannot see domain walls" (Eto/Nitta 2012
   [A], S. 3); Y nur festgehalten (Nitta u. a. 2012). 3He-B: Doppelkernwirbel als Dreifachkern, gestreckt zwischen
   Haftstellen wird das Halbwirbel-plus-Wand-Bild gueltig (Rantanen 2025 [A-W]). Unser Y-1-"Beutel" ist das kompakte
   Regime; die Abschirmung ist der zusaetzliche, bei uns billige Ausweg. Alles bleibt Vorbild: kein Eichfeld, kein Spin 1/2,
   Drittelwindung ja, Drittelladung als Erhaltungsgroesse nein (Abschnitt 6).

## Einfach gesagt

Wir wollten wissen, ob jemand schon einmal drei Wirbel wie drei Quarks mit einem Y-foermigen Faden verbunden hat. Ja:
2012 in einem Modell fuer Supraleiter mit drei Komponenten, aber nur, wenn man die drei Wirbel festhaelt; laesst man sie
los, fallen sie zu einem einzigen Wirbel zusammen. Unser Modell hat den Faden nicht gezeigt, weil es fuer einen Wirbel
billiger ist, sein eigenes Feld aus der Umgebung zu verdraengen, als einen Faden zu spannen. Im Supraleiter-Modell ist
genau dieses Verdraengen sehr teuer. Der kleinste Umbau ist deshalb ein Term, der jedem Feld eine eigene Dichte
aufzwingt; ob das den Faden bringt, kann ein kurzer Rechenlauf zeigen.

---

## 1. Erwartungsverstoesse (das Wichtigste zuerst; Vorab in A1/A1b, Zyklen in A3)

1. **Ein gebundener Dreier mit Y-Knoten aus Wirbeln ist publiziert** (Nitta u. a. 2012, [A]). Vorab p = 0,3 dafuer, dass
   jemand festgehaltene Wirbel gerechnet hat; p = 0,6 dafuer, dass kein Y ohne Wirbel am Knoten vorkommt. Beides verfehlt.
   Korrigierte Erwartung: Der Y-Knoten dreier Einzelwaende (je Wirbel eine 2 pi-Komponentenwand, alle drei am Knoten)
   ist die bekannte Loesung; die Autoren begruenden ihn genau mit dem Argument, das PLAN 2.3 fuer unsere Waende fand
   (ein Dreieck liesse "a domain (membrane) with finite energy ... inside the triangle", Abschn. 3).
2. **Der Y-Traeger ist die Quartik je Komponente, nicht die Kopplungsart.** Erwartet hatte ich, dass die lineare Rabi-
   Kopplung der Schluessel ist. Gefunden: Bei Nitta u. a. ist gamma = 0,02 winzig gegen lambda = 2; die Waende sind breit
   (~8 Laengeneinheiten [Hand aus Gl. 12, 17]) und trotzdem sichtbar, weil das Entleeren eines Kerns 25-mal teurer ist
   als die Wandenergie je Flaeche. Das ist die Stanev/Tesanovic-Quartik aus BERICHT-FARBEN (Verstoss 3 dort).
3. **Das Einschluss-Papier ist 2018, nicht 2020, und benennt unseren N = 2-Befund vollstaendig:** Eto, Nitta, PRA 97,
   023613 (2018) [A]: "baryon" = Wirbelpaar in zwei Komponenten, "meson" = Wirbel plus Antiwirbel derselben Komponente;
   "baryon is static at the equilibrium and rotates once it deviates from the equilibrium, while a meson moves with
   constant velocity"; Stringbruch durch Paarbildung ab R_c ~ 21 R* (eta = 0,1). ROT-1 (Gleichgewichtsabstand ~2,5,
   Magnus-Kreisen), REGGE-1 und BAND-1 (Reissen bei 8 bis 14) sind damit "bekannt unter Namen". PRR 2, 033373 (2020) ist
   Eto, Ikeno, Nitta zu Stoessen solcher Molekuele ("swap a partner ... Feynman diagrams ... selection rule") [A-W].
4. **Der angekuendigte Dreikomponenten-Einschluss ist nicht erschienen.** Eto/Nitta 2018, S. 5: "As real QCD has SU(3)
   symmetry, our next step will be the confinement of 1/3 quantized vortices in three-component BECs, for which a baryon
   was constructed numerically in Ref. [30, 31]". Suche (arXiv-API, alle Jahre, drei Komponenten AND baryon/confinement
   AND vortex): nach 2013 kein Treffer. **Nach Recherchestand offen**, nicht widerlegt. Das ist die Luecke, in die ein
   Test unserer Art hineinrechnen wuerde, mit dem Unterschied, dass unsere Waende Z_2-Paare sind.
5. **Ein neues Dreikomponenten-Vorbild aus 3He-B (Okt. 2025):** Rantanen, arXiv:2510.19566 [A-W]: der Doppelkernwirbel
   "as a combination of three vortices, one in each component of the spin-triplet superfluid"; "stretched between pinning
   sites ... the HQV picture becomes more applicable when separation between subcores becomes large". Vorab: keine neue
   Arbeit mit festgehaltenem Dreier (p = 0,6). Verfehlt; das ist ein gestreckter, festgehaltener Mehrkern in einem
   realen Suprafluid, mit Regimewechsel kompakt -> Wand.
6. **Die Graphen der N-omere sind Kopplungsgraphen, keine Wandnetze:** "we identify vertices as vortices, and the edge
   connecting i-th and j-th vertices as the Rabi coupling omega_ij if it is nonzero" (Eto/Nitta 2013 [A], S. 2). N = 3:
   Dreieck und "rod" (Abb. 6). Kein wirbelfreier Knoten, wie erwartet, aber aus einem anderen Grund als erwartet.
7. Klein: Oda u. a. 1999 ist keine Z_3-Wess-Zumino-Loesung, sondern U(1) x U(1)'-SUSY mit drei Chiralfeldpaaren; die
   Knotenladung Y_k traegt negativ zur Masse bei [A-W]. Beim Boojum treffen drei Neutronenwirbel und spalten in drei
   Farbwirbel (3 -> 3), nicht 1 -> 3 [A-W]. In 24 Monaten null Treffer fuer "vortex trimer" und fuer "coherently coupled"
   AND vortex AND (confinement OR molecule OR "domain wall").

## 2. Literaturstand je Kandidat

### 2.1 Kandidat 1: lineare Rabi-/Josephson-Kopplung, cos(Delta) statt cos(2 Delta)

- Bekannt: Son/Stephanov 2002 [A in ROT-3]: Sine-Gordon-Wand der relativen Phase, metastabil, "vortex confinement".
  Kasamatsu/Tsubota/Ueda 2004 [A-W]: Wirbelmolekuel, Meronpaar; Anisotropie aus ungleichen Streulaengen. Eto/Nitta 2012
  [A]: Trimer, T_1 = sqrt(T_12^2 + T_31^2) (Gl. 10), A ~ 0,56 omega^-0,25 (Gl. 11, 0,01 <= omega <= 0,1), Relaxation mit
  fester Windung am Rand (Fn. 18), "we cannot see domain walls" (S. 3), Kollaps bei omega_12 = 0,5; nur "partonic",
  kein Quark-Wort (Grep, A5). Eto/Nitta 2013 [A]: N-omere, U(N)-Fall = CP^{N-1}-Skyrmion, "N - 1 domain walls are
  attached to the i-th vortex ... it must be connected to the boundary or to vortices winding around the other
  components" (S. 2). Tylutki u. a. 2016 [A-W]: "analogue of quark confinement and string breaking". Gallemi u. a. 2019
  [A-W]: zwei Zerfallswege der Wand (energetisch ueber Paar derselben Sorte bei kleinem Omega; Schlangeninstabilitaet
  bei grossem Omega). Eto/Nitta 2018 [A], Eto/Ikeno/Nitta 2020 [A-W]: Mesonen/Baryonen, Reaktionen.
- Y-Knoten: **ja, topologisch** (A1, Hand; Nitta u. a. 2012 im Supraleiter, [A]); **nein fuer freie Wirbel** (kompakt).
  Bedingungen: festgehaltene Enden, Abstand >> Wandbreite, Kernleerung teurer als Wand, Abstand < Reisslaenge.
- Kleinste Aenderung: + epsilon sum_{a<b} Re(psi_a^* psi_b) in L (Energie -(epsilon/2)(|Psi|^2 - S), Psi = sum psi_a;
  Kraft -(epsilon/2)(Psi - psi_a)). Nur zusammen mit g != 0 wirksam (KANDIDAT 2.3 [P]; bestaetigt durch den U(N)-Fall
  bei Eto/Nitta 2013 [A]).
- Was verloren ginge: Z_2^{N-1} (Delta = pi wird falsches Vakuum; die Ising-Linse aus ROT-1 wird gebunden), die
  Fourier-Gitterregel und das Verbot der Dreier-Linie (BERICHT-FARBEN 9.1), Paartransfer wird Einzeltransfer
  (Josephson-Strom ~ sin Delta), Vakuumschranke epsilon < 1 - b^2/2 = 0,32 bei b = 1,167 [Hand A4], bei g = 0 die
  ganze Kanalstruktur (Basiswahl mit Massenaufspaltung). Q_a sind schon bei g != 0 nicht erhalten.

### 2.2 Kandidat 2: Y-foermige Wandknoten in Modellen mit drei Vakua

- Bekannt: Gibbons/Townsend 1999 [A-W]: Wess-Zumino mit quartischem Superpotential, drei Waende an einem Knoten,
  1/4-SUSY-Schranke. Carroll/Hellerman/Trodden 1999 [A-W]: "domain wall junctions are 1/4-BPS states", BPS-Schranke,
  explizite Loesung im Sonderfall. Oda u. a. 1999 [A-W]: exakte Loesung, Knotenladung negativ. Banerjee, Digal, Shaw
  2026 [A-W]: Z_N-Waende in SU(N) mit Polyakov-Loop-Potential; SU(3): "the merger of two non-planar Z_3 domain walls
  ... proceeds via the creation of a vortex-antivortex pair in 2+1 dimensions"; "string junctions play a crucial role".
- Y-Knoten: ja, als Knoten dreier Waende zwischen drei Vakua. Unsere Formel hat bei N = 3 vier Vakua (Z_2^2) und
  erlaubt den Knoten W_1-W_2-W_3 (Zyklus (0,0) -> (pi,0) -> (pi,pi) -> (0,0)) ohne jede Aenderung [Hand, A1]; auch die
  sechs-Wand-Version aus PLAN 2.3. **Die Topologie war nie das Problem.**
- Kleinste Aenderung: keine noetig. Ein Z_3-Uhrterm (z. B. Re[(psi_a^* psi_b)^3]) waere sechster Ordnung und brachte
  nichts, was die Z_2^2-Struktur nicht schon hat.
- Verlust: entfaellt.

### 2.3 Kandidat 3: nichtabelsche Wirbel, Farbe-Flavour, "baryonische" Konfigurationen

- Bekannt: Auzzi u. a. 2003 [A-W]: nichtabelsche Flussroehren in N = 2 SQCD, Einschluss von Monopolen, keine
  Knoten/Baryonen im Abstract. Eto, Hirono, Nitta, Yasui 2014 [A-W]: Uebersicht, nichtabelsche Wirbel = "1/3 quantized
  superfluid vortices and color magnetic flux tubes". Cipriani/Vinci/Nitta 2012 [A-W]: "three neutron vortices join at a
  boojum and split into three color magnetic vortices" (3D, Grenzflaeche). Cipriani/Nitta 2013 [A-W]: "colorful" Gitter
  in Dreikomponenten-BEC unter Rotation. Nitta/Uchino/Vinci 2014 [A-W]: nichtabelsche Wirbel in Dreikomponenten-BEC mit
  masselosen Moden. Gudnason/Nitta 2025 [A-W]: chirale nichtabelsche Wirbelmolekuele in dichter QCD, "one or two domain
  walls", zwei Wirbel, kein Dreier.
- Y-Knoten: als Knoten von **Wirbellinien in 3D** (Boojum), nicht als 2D-Wandnetz. Die drei 1/3-Wirbel der CFL-Phase
  stossen sich in 2D ab [S, Nakano/Nitta/Matsuura 2008, nicht an der Quelle].
- Kleinste Aenderung: ein nichtabelsches Eichfeld; das ist keine kleine Aenderung. Einordnung nur.
- Verlust: das ganze bisherige Q-Ball-Programm (globale Symmetrie).

### 2.4 Kandidat 4: Skyrme-Baryonen (Soliton = Hadron)

- Bekannt: Skyrme 1961/62, Witten 1983 [L, nicht abgerufen]. Bruecke: der Trimer der Rabi-Kopplung ist im U(N)-Fall ein
  CP^{N-1}-Skyrmion (Eto/Nitta 2013 [A]); die "Partonen" sind die Nullstellen der Komponenten an Z_N-symmetrischen
  Punkten (Gl. 4). Neu (24 Monate): Hamada 2025 [A-W] "Baryons as linked vortices" (Verkettungszahl = Baryonzahl), Hamada
  2026 [A-W], Mameda 2026 [A-W] "Baryonic vortices in rotating nuclear matter".
- Y-Knoten: nein; das Baryon ist das ganze Soliton. Unser "Beutel" (Y-1: Loch mit S -> 0, P windet zweimal) ist das
  Gegenstueck: das kompakte Objekt als Ganzes.
- Kleinste Aenderung: keine; aber Deutung: ein kompakter Dreier ist kein Scheitern, sondern das Skyrme-Regime.
- Verlust: das Quarkbild (drei Konstituenten sind im Skyrme-Regime nicht mehr getrennt).

### 2.5 Kandidat 5: QCD-Y-Gesetz (nur Einordnung)

- Takahashi u. a. 2001 [A-W]: V_3Q = const + Coulomb + sigma_3Q L_min, "accuracy better than a few %", sigma_3Q ~
  sigma_QQbar. Takahashi/Suganuma u. a. 2002 [A-W]: > 300 Muster, drei Gitter, "support the Y-ansatz", Delta nur mit
  reduzierter Spannung als Naeherung. Alexandrou u. a. 2002 [A-W]: "support to the Delta ansatz". Bissey u. a. 2007
  [A-W]: kleine Abstaende "filled triangle", grosse "Y-shape flux-tube formation is observed. T-shaped paths ... relax
  towards a Y-shaped topology".
- Nitta u. a. 2012 uebernehmen genau diese Dichotomie: Y = "genuine three-body interaction", Delta = Summe von
  Zweikoerperkraeften (Abschn. 1, 5). Die statischen Quarks des Wilson-Loops entsprechen den festgehaltenen Wirbeln [ES].

### 2.6 Kandidat 6: 24 Monate (Regel 7)

- Anfragen (arXiv-API, submittedDate 2024-09-01 bis 2026-10-01): "vortex trimer(s)": 0. "coherently coupled" AND
  vortex AND (confinement OR molecule OR "domain wall"): 0. Rabi AND vort* AND BEC: 3 (keiner einschlaegig).
  "vortex molecule(s)"/"vortex dimer": 2 (Gavrilov 2025, Gudnason/Nitta 2025). fractional/half-quantum vortices AND
  (three-component OR multicomponent OR three-band): 3 (Rantanen 2025 einschlaegig; Hui 2026; Canfora 2025).
  three-component AND vort* AND (domain wall OR junction) AND (condensate OR superfluid OR superconductor): 2 (Zou 2025;
  Rantanen 2025). junction AND "domain wall" AND vort*: 1 (Banerjee u. a. 2026). baryon AND (condensate OR superfluid)
  AND vort*: 8 (Hamada 2025/2026, Mameda 2026, Nitta 2026 einschlaegig).
- Urteil: Ein festgehaltener Dreier mit Y-Knoten in einem Kondensat ist in den letzten 24 Monaten nicht gerechnet
  worden; der Dreikomponenten-Einschluss von Eto/Nitta ist nicht erschienen. "Nach Recherchestand nicht belegt", nicht
  widerlegt. Aktiv sind: Baryonen als verkettete Wirbel (Hamada, Mameda), Z_3-Wandknoten mit Paarbildung in 2+1
  (Banerjee u. a.), Mehrkernwirbel in 3He-B (Rantanen).

## 3. Regime und Moderatoren (Regel 1)

| Feld | kompaktes Regime | ausgedehntes Regime | Moderator | Quelle |
|---|---|---|---|---|
| Gitter-QCD, 3Q | gefuelltes Dreieck (Delta-artig) | Y-Flussroehren | Quarkabstand gegen Roehrenbreite | Bissey 2007 [A-W]; Lager Takahashi/Alexandrou |
| Rabi-BEC, N = 3 | Trimer A ~ 0,56 omega^-1/4, Waende unsichtbar, U(N): Skyrmion | Y nur festgehalten (Supraleiter-Modell) | Festhalten; Kernkosten/Wandkosten; omega | Eto/Nitta 2012, 2013 [A]; Nitta u. a. 2012 [A] |
| 3He-B | Dreifachkern | Halbwirbelpaar plus Wand | Abstand der Teilkerne (Haftstellen) | Rantanen 2025 [A-W] |
| unsere Formel (Y-1) | Beutel (a <= 9, l <= 5) | Abschirmung durch Gegenwirbel, keine Waende | Kernkosten (g/12) S^2 gegen sigma_W; Ringradius | Y-1 [P] |

- Gemeinsame Kopplungsgroesse (Regel 6) [ES]: kappa = Kosten je Flaeche, die eigene Komponente aus einem Kern zu
  entfernen, gegen sigma_W / w_W (Wandenergie je Flaeche). Drei Wege aendern dasselbe Verhaeltnis: Quartik je Kanal (c),
  Rabi-Term (epsilon), Ringradius (r_c). Bei Nitta u. a. ist kappa/(gamma v^2) = 25; bei uns kappa/sigma_W-Vergleich in
  A4: Abschirmung gewinnt bei c = 0 und c = 0,4 (beides beobachtet), Gleichstand bei c ~ 1 oder epsilon ~ 0,3, Waende bei
  c = 2 mit nachgestimmtem U. Die Abschaetzung ist grob: fuer N = 2 (K1) sagt sie Abschirmung voraus, wo keine war
  (Faktor >= 2,5 daneben, A5). Der Test muss deshalb die Abschirmung direkt messen.

## 4. Unterscheidungspunkte (Regel 2)

- **Y gegen Dreieck gegen Beutel** trennen sich nur in der Parameterregion: Armlaenge >= 3 w_W (w_W ~ 1,3 bei g = 0,5),
  kappa-Verhaeltnis > 1 (keine Abschirmung) und Armlaenge < Reisslaenge (BAND-1: 8 bis 14 bei N = 2). Also Arme 4 bis 8,
  gleichseitig a = 7 bis 14. Y-1 lag mit L_St = 10 bis 26 in dieser Region, aber mit kappa-Verhaeltnis < 1: die
  Abschirmung hat die Region leer gemacht. Ausserhalb (kompakt) fallen alle drei Gesetze zusammen, wie Y-1 fand.
- **Rabi gegen Quartik** trennen sich an der Wandform (2 pi-Kink mit gebundener Linse gegen zwei freie pi-Waende mit
  echter Vakuumlinse dazwischen) und am Kanalstrom (sin Delta gegen sin 2 Delta): messbar an der Kopplungsdefizit-Karte
  (eine Rippe gegen zwei) und an der Fourier-Linie omega_b - omega_a (bei Rabi erlaubt, bei uns verboten, BERICHT-FARBEN
  9.1). Beides braucht keinen neuen Lauf, nur die vorhandenen Diagnosen.
- **Eichfeld gegen kein Eichfeld** trennt sich nicht am Y, sondern an der Endlichkeit der Energie des ganzen (1,1,1)-Wirbels
  (Nitta u. a. 2012, Abschn. 2) und am Reissen: mit globaler Symmetrie ist die Reisslaenge die Skala des Paars (BAND-1),
  im Eichmodell die des Flussquants. Empirisch fuer uns unzugaenglich; wird hiermit als nicht unterscheidbar benannt.

## 5. Kleinster Rechentest mit Scheiterregel (nicht gerechnet; Vorschlag an die Leitung)

- **Code:** RUNDE-10/y1/y1.py, Kopie als alt1.py. Aenderungen (Schaetzung 30 bis 60 min):
  1. Parameter b_0 (S^2-Koeffizient von U) an drei Stellen: upot(s, b) wird von der Flussgleichung
     "1.0 + S*(1.5*S - 2.0)" (-> 1.0 + S*(1.5*S - 2*b_0)), von energie() (upot mit b_0) und von b_von(k)
     (b = b_0 + g(N-1)/(2N) - c/N) benutzt.
  2. Optional epsilon: in energie() "- (eps/2) * (|Psi|^2 - S)" mit Psi = psi.sum(1); in der Schleife
     "- (eps/2) * (Psi - psi)" zur Kraft. Radialer Ball dann mit Massenterm (1 - eps(N-1)/2) statt 1: eine weitere Stelle.
  3. Der weite Ring (kl_aus = 4) und alle Diagnosen (windung_um_wirbel, S_loch, knoten, Kopplungsdefizit, Kantenmitten)
     existieren.
- **Arme** (g = 0,5, Q = 3600, dx 0,3, 12000 Iterationen, Schwerpunktbindung wie Y-1):
  - B (Hauptarm): c = 2, b_0 = 1 + c/3 = 1,6667 (gemischter Ball b = 1,1667 wie Y-1). Vorab-Probe: b_eff(N = 1) = -0,33
    (kein Einzelball), b_eff(zwei Fuellkomponenten) = 0,79, Vakuum stabil (1 - b^2/2 = 0,32 > 0).
  - A (Vergleich): c = 1, b_0 = 1 (b = 0,833). Nach A4 Gleichstand; zeigt, ob das Nachstimmen noetig ist.
  - C (Literatur-Wandtyp): epsilon = 0,3, c = 0, b_0 = 1 (unter der Vakuumschranke 0,32).
  - Geometrien je Arm: gleichseitig 9, gleichseitig 12, kollinear 8, Meson d = 6 / 9 / 12; Saat neutral und Y.
  - Umfang: 3 Arme x 6 Laeufe x 2 Saaten = 36 Laeufe, gebuendelt wie Y-1 (Stapel je Arm); nach Y-1 (225 s je Stapel von
    12) etwa 30 bis 45 min P4000 gesamt.
- **Vorab-Erwartungen fuer Arm B** (binden, bevor gerechnet wird): (i) keine Gegenwirbel (eigene Windung um jeden Wirbel
  bei r = 2,5 und 4,5 gleich 1) in >= 4 von 5 Nicht-Meson-Laeufen; (ii) Kopplungsdefizit-Rippe innerhalb 1,5 der
  Steiner-Arme, Knoten (arg-P-Windung 2) innerhalb 1,5 von J; (iii) E(gleich 12) - E(gleich 9) = 3 bis 5 (2 sigma_W bis
  2 sigma_Rand mal 5,2); (iv) Meson linear bis 12 mit Steigung 0,6 bis 1,0; (v) E(kollinear 8) - E(gleich 9) < 1
  (Y: +0,3; Dreieck: +2,0 bei sigma = 0,82). Fuer Arm A: (i) verfehlt in >= 2 von 5. Fuer Arm C: eine Rippe je Arm statt
  zwei.
- **Scheiterregel (vorab, Wortlaut gilt):**
  - "Quartik traegt das Y nicht": Arm B zeigt Gegenwirbel in >= 2 der 3 Dreier-Geometrien **oder** das Meson ist flach
    (Steigung 9 -> 12 < 0,3 x Steigung 6 -> 9).
  - "Dreieck": keine Gegenwirbel, aber Rippe an den Kantenmitten (n_a/S < 0,1 an >= 2 Kantenmitten) und nicht auf den
    Armen. Kein Scheitern, anderes Vorbild.
  - "Y": (i), (ii) erfuellt und (iii) innerhalb 3 bis 5. Alles andere: "weder noch", wie Y-1.
  - Nicht auswertbar: dE1000 > 0,02 oder Schub > 30 (Ball weggeglitten) in einem der drei Dreier.
- **Ableitbarkeits- und Sichtprobe:** Die Netzform und die Abschirmung stehen in keiner vorhandenen Datei; der
  Grundzustand bei festem Q mit c ist vorab ableitbar (C3) und ist keine Kennzahl. Die Handabschaetzung A4 ist um
  einen Faktor >= 2,5 unsicher (N = 2-Probe), also kann der Test in beide Richtungen ausgehen.

## 6. Gegensweep (Regel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

1. **"Y-Knoten = Baryon-Vorbild"** (ungeprueft uebernommen aus der Karte). Bissey u. a. zeigen: bei kleinen Abstaenden ist
   das Baryon ein gefuelltes Dreieck. Y-1s Beutel ist also nicht "kein Baryon", sondern das kompakte Regime. Was fehlt,
   ist der Uebergang zum ausgedehnten Regime, den die Abschirmung verhindert. **Geprueft** an der Y-1-Tabelle: alle
   Beutel liegen bei L_St <= 15,6, alle abgeschirmten Zustaende darueber oder mit einem kurzen Paar.
2. **"Die Handabschaetzung kappa gegen sigma_W erklaert Y-1"** (eigene Rechnung, A4). **Geprueft** gegen K1 (N = 2,
   ROT-1 paar): dort sagt sie Abschirmung voraus (3,1 gegen 7,8), K1 zeigt den leeren Schlitz ohne Gegenwirbel bis
   d = 9,5. Die Abschaetzung ist also mindestens um den Faktor 2,5 zu pessimistisch; die Zahlen in Abschnitt 5 sind
   Groessenordnungen, keine Vorhersagen mit Fehlerbalken.
3. **"KANDIDAT 2.3 (Rabi = Basiswahl bei g = 0) gilt auch mit Wirbeln"** (uebernommen). **Geprueft** an Eto/Nitta 2013:
   fuer g = g-tilde (U(N)-symmetrische Wechselwirkung) gibt es kein Molekuel, sondern "an axisymmetric giant vortex"
   (S. 2) und "the total energy density is universally axisymmetric" (Eto/Nitta 2012, S. 4). Bestaetigt. Folge: unser
   Kern-gefuellter Wirbel bei g = 0 (ROT-1) ist der CP^1-Skyrmion-Fall, nicht ein Molekuel.
4. **"Eto/Nitta 2012 hat keine Quark-Analogie"** (Y-1-Agent). **Geprueft** per Grep in beiden Volltexten: 2012 nur
   "partonic" (zwei Zeilen), 2013 kein Quark/Baryon/QCD/confinement. Die Analogie steht bei Nitta u. a. 2012 und
   Eto/Nitta 2018. Der Y-1-Agent hatte recht, aber das falsche Papier fuer die Frage.
5. **"Festhalten (Klammer) ist ein Artefakt."** Nicht so: Die statischen Quarks des Wilson-Loops (Takahashi) und die
   "fixed positions" bei Nitta u. a. sind dasselbe Festhalten. Das Vorbild ist ehrlicher als gedacht: es ist ein Vorbild
   fuer das **statische Dreiquark-Potential**, nicht fuer ein freies Baryon. Frei kollabiert es in allen bekannten
   Modellen (Nitta u. a. 2012: "collapse to form a single integer vortex"; Eto/Nitta 2012: kompakt; Y-1: Beutel).
   Ungeprueft bleibt, wie Nitta u. a. genau festhalten (Windung an den Punkten oder Phasenfeld); der Text sagt nur
   "we have fixed the positions of the three vortices".
6. **"Kein Eichfeld = kein Y."** Falsch: Bei Nitta u. a. sind die relativen Phasen global; das Eichfeld macht nur den
   Gesamtwirbel endlich. Der Gegensweep-Punkt der Karte trifft nicht das Y, sondern "Einschluss" als Begriff, Spin 1/2 und
   die Drittelladung: die 1/3-Windung ist da (Nitta u. a. Gl. 4: jeder Wirbel traegt 1/3 der Eichdrehung), eine erhaltene
   Drittelladung nicht, weil Q_a bei g != 0 nicht erhalten ist (KANDIDAT 4.3).

## 7. Kalibrierung

- (a) Gemessen (Literatur, numerisch, an der Quelle): Y bei festgehaltenen 1/3-Wirbeln im Dreikomponenten-Supraleiter,
  eine Konfiguration [A]; kompakte Trimere im BEC mit A ~ omega^-1/4 [A]; Stringbruch mit R_c ~ 21 R* [A]; Gitter-QCD:
  Y bei grossen, gefuelltes Dreieck bei kleinen Abstaenden [A-W].
- (b) Nuetzlich verdichtet: die Kopplungsgroesse kappa gegen sigma_W/w_W (Abschnitt 3) und die Zwei-Regime-Tabelle. Beides
  [ES]; die Zahlen in A4 sind Duennwand-Handrechnungen mit bekanntem Faktor-2,5-Fehler.
- (c) Gewachsene Gewissheit ohne neue Evidenz: "Der c-Term wird das Y tragen." Dafuer gibt es keine Rechnung in unserer
  Formel; Y-1 mit c = 0,4 zeigte weiter Abschirmung. Meine Sicherheit ist im Lauf der Recherche gestiegen, waehrend die
  Frage feiner wurde (von "welcher Term" zu "welches Verhaeltnis"); das ist das Warnzeichen aus der Kalibrierregel.
  Deshalb die Scheiterregel in Abschnitt 5 und der Vergleichsarm A.

## 8. Offene Fragen

- Wie halten Nitta u. a. 2012 die Wirbel fest, und wie gross ist ihr Dreieck gegen die Wandbreite (~8)? Abb. 2 ist nur
  als Bild vorhanden; eine Zahl steht nicht im Text.
- Warum versagt die kappa-Abschaetzung bei N = 2 (K1)? Vermutung [H]: der Gegenwirbel braucht bei N = 2 einen Kern, der
  mit einer einzigen Fuellkomponente teurer ist; bei N = 3 teilen sich zwei Fuellkomponenten den Kern mit freier
  relativer Phase. Nicht gerechnet.
- Ist der Dreikomponenten-Einschluss (Eto/Nitta 2018, "next step") irgendwo erschienen, was die arXiv-API nicht findet
  (Konferenzband, andere Schlagworte)? Nach Recherchestand nein.
- Gilt die Reisslaenge 8 bis 14 (BAND-1, N = 2) auch fuer Arm B? Mit c = 2 aendern sich Paarenergie und Spannung; der
  Meson-Arm im Test misst das mit.
- Was ist der Y-Knoten energetisch bei Z_2-Waenden: sechs Waende an einem Punkt oder zwei Dreier-Knoten (W_1, W_2, W_3)
  dicht beieinander? Beide sind topologisch erlaubt (A1); die Kopplungsdefizit-Karte des Tests zeigt es.

## 9. Quellenliste (Autor, Jahr, Titel, Fundstelle, URL; Lesetiefe)

- Nitta, M.; Eto, M.; Fujimori, T.; Ohashi, K. (2012): Baryonic Bound State of Vortices in Multicomponent Superconductors.
  J. Phys. Soc. Jpn. 81, 084711. https://arxiv.org/abs/1011.2552 [A, Volltext Abschn. 1 bis 5]
- Eto, M.; Nitta, M. (2012): Vortex trimer in three-component Bose-Einstein condensates. PRA 85, 053645.
  https://arxiv.org/abs/1201.0343 [A, Volltext S. 1 bis 4, Fn. 18, 19]
- Eto, M.; Nitta, M. (2013): Vortex graphs as N-omers and CP^{N-1} Skyrmions in N-component Bose-Einstein condensates.
  EPL 103, 60006. https://arxiv.org/abs/1303.6048 [A, Volltext S. 1 bis 5]
- Eto, M.; Nitta, M. (2018): Confinement of Half-quantized Vortices in Coherently Coupled Bose-Einstein Condensates:
  Simulating Quark Confinement in QCD. PRA 97, 023613. https://arxiv.org/abs/1702.04892 [A, Volltext Abstract, S. 2, 5,
  Anhang A, Referenzen 21, 23, 30, 31]
- Eto, M.; Ikeno, K.; Nitta, M. (2020): Collision dynamics and reactions of fractional vortex molecules in coherently
  coupled Bose-Einstein condensates. Phys. Rev. Research 2, 033373. https://arxiv.org/abs/1912.09014 [A-W]
- Nitta, M.; Eto, M.; Cipriani, M. (2014): Vortex molecules in Bose-Einstein condensates. J. Low Temp. Phys. 175, 177.
  https://arxiv.org/abs/1307.4312 [A-W]
- Cipriani, M.; Nitta, M. (2013): Vortex lattices in three-component Bose-Einstein condensates under rotation: simulating
  colorful vortex lattices in a color superconductor. PRA 88, 013634. https://arxiv.org/abs/1304.4375 [A-W]
- Cipriani, M.; Vinci, W.; Nitta, M. (2012): Colorful boojums at the interface of a color superconductor. PRD 86, 121704.
  https://arxiv.org/abs/1208.5704 [A-W]
- Nitta, M.; Uchino, S.; Vinci, W. (2014): Quantum Exact Non-Abelian Vortices in Non-relativistic Theories. JHEP 1409, 098.
  https://arxiv.org/abs/1311.5408 [A-W]
- Eto, M.; Hirono, Y.; Nitta, M.; Yasui, S. (2014): Vortices and Other Topological Solitons in Dense Quark Matter. PTEP
  2014, 012D01. https://arxiv.org/abs/1308.1535 [A-W]
- Gudnason, S. B.; Nitta, M. (2025): Chiral non-Abelian vortex molecules in dense QCD. PRD 111, 074013.
  https://arxiv.org/abs/2501.18464 [A-W]
- Kasamatsu, K.; Tsubota, M.; Ueda, M. (2004): Vortex molecules in coherently coupled two-component Bose-Einstein
  condensates. PRL 93, 250406. https://arxiv.org/abs/cond-mat/0406150 [A-W]
- Tylutki, M.; Pitaevskii, L. P.; Recati, A.; Stringari, S. (2016): Confinement and precession of vortex pairs in
  coherently coupled Bose-Einstein condensates. PRA 93, 043623. https://arxiv.org/abs/1601.03695 [A-W]
- Gallemi, A.; Pitaevskii, L. P.; Stringari, S.; Recati, A. (2019): Decay of the relative phase domain wall into confined
  vortex pairs: the case of a coherently coupled bosonic mixture. PRA 100, 023607. https://arxiv.org/abs/1906.06237 [A-W]
- Son, D. T.; Stephanov, M. A. (2002): Domain walls of relative phase in two-component Bose-Einstein condensates. PRA 65,
  063621. https://arxiv.org/abs/cond-mat/0103451 [A in ROT-3, hier nicht erneut abgerufen]
- Rantanen, R. (2025): Triple-core structure of the double-core vortex in superfluid 3He-B. arXiv:2510.19566.
  https://arxiv.org/abs/2510.19566 [A-W]
- Gavrilov, S. S. (2025): Phase domain walls in coherently driven Bose-Einstein condensates. arXiv:2505.09553.
  https://arxiv.org/abs/2505.09553 [A-W in ROT-3; hier nur Suchtreffer]
- Carroll, S. M.; Hellerman, S.; Trodden, M. (2000): Domain Wall Junctions are 1/4-BPS States. PRD 61, 065001.
  https://arxiv.org/abs/hep-th/9905217 [A-W]
- Gibbons, G. W.; Townsend, P. K. (1999): A Bogomol'nyi equation for intersecting domain walls. PRL 83, 1727.
  https://arxiv.org/abs/hep-th/9905196 [A-W]
- Oda, H.; Ito, K.; Naganuma, M.; Sakai, N. (1999): An Exact Solution of BPS Domain Wall Junction. PLB 471, 140.
  https://arxiv.org/abs/hep-th/9910095 [A-W]
- Banerjee, S.; Digal, S.; Shaw, S. (2026): Dynamics of (Z_N) Domain Walls in SU(N) Gauge Theories. arXiv:2606.22532.
  https://arxiv.org/abs/2606.22532 [A-W]
- Auzzi, R.; Bolognesi, S.; Evslin, J.; Konishi, K.; Yung, A. (2003): Nonabelian Superconductors: Vortices and
  Confinement in N = 2 SQCD. NPB 673, 187. https://arxiv.org/abs/hep-th/0307287 [A-W]
- Takahashi, T. T.; Matsufuru, H.; Nemoto, Y.; Suganuma, H. (2001): Three-Quark Potential in SU(3) Lattice QCD. PRL 86,
  18. https://arxiv.org/abs/hep-lat/0006005 [A-W]
- Takahashi, T. T.; Suganuma, H.; Nemoto, Y.; Matsufuru, H. (2002): Detailed Analysis of the Three Quark Potential in
  SU(3) Lattice QCD. PRD 65, 114509. https://arxiv.org/abs/hep-lat/0204011 [A-W]
- Alexandrou, C.; de Forcrand, Ph.; Tsapalis, A. (2002): The static three-quark SU(3) and four-quark SU(4) potentials.
  PRD 65, 054503. https://arxiv.org/abs/hep-lat/0107006 [A-W]
- Bissey, F.; Cao, F.-G.; Kitson, A. R.; Signal, A. I.; Leinweber, D. B.; Lasscock, B. G.; Williams, A. G. (2007): Gluon
  flux-tube distribution and linear confinement in baryons. PRD 76, 114512. https://arxiv.org/abs/hep-lat/0606016 [A-W]
- Hamada, Y. (2025): Baryons as linked vortices in QCD matter with isospin asymmetry. arXiv:2509.20844.
  https://arxiv.org/abs/2509.20844 [A-W, nur Suchzusammenfassung]
- Hamada, Y. (2026): QCD phase diagram in a magnetic field with baryon and isospin chemical potentials. arXiv:2602.11762.
  https://arxiv.org/abs/2602.11762 [S]
- Mameda, K. (2026): Baryonic vortices in rotating nuclear matter. arXiv:2603.29325. https://arxiv.org/abs/2603.29325 [S]
- Nitta, M. (2026): Emergent Conformal Symmetry on Superfluid Vortices in Two-Color QCD and Pseudoreal Gauge Theories.
  arXiv:2609.12080. https://arxiv.org/abs/2609.12080 [S]
- Nakano, E.; Nitta, M.; Matsuura, T. (2008): Non-Abelian strings in high density QCD. PRD 78, 045002 [S, nicht abgerufen]
- Skyrme, T. H. R. (1961/62); Witten, E. (1983) [L, nicht abgerufen]
- Projektdateien [P]: RUNDE-10/y1/ERGEBNIS.md, PLAN.md, y1.py; RUNDE-09/rot1/ERGEBNIS.md, REGGE-1.md, BAND-1.md;
  RUNDE-09/PAPIER-ROT3.md; RUNDE-09/SUCHWORTE.md; farben-20260927/BERICHT-FARBEN.md; gesamtformel-20260921/KANDIDAT.md.

---

# Arbeitsfeld

## A0. Ausgangslage aus den Projektdateien [P] (gelesen 11:58 bis 12:05)

- Y-1 ERGEBNIS.md: N = 3, cos 2 Delta, g = 0,5 / 0,2: keine Waende. Kompakte Dreier teilen sich ein Loch ("Beutel"),
  groessere werden durch Gegenwirbel im entleerten Kern abgeschirmt. Kernkosten bei N = 3 nur (g/12) S^2 je Flaeche
  (N = 2: (g/4) S^2). Meson reisst zwischen d = 9 und 12. Mit + c sum |psi_a|^4 (c = 0,4) haelt der Beutel bis a = 12;
  sieben intakte Beutel passen eher zu Y (RMS 0,29 gegen 0,41), nicht belastbar. C1: Gegenwirbel an 11/12 auch mit c.
- Y-1 PLAN 2.3 [Hand]: In der Z_2^2-Struktur ist ein Dreieck mit einer Wand je Kante unmoeglich; billigstes Netz ist
  das Y aus drei Doppelbaendern (2 W_a je Wirbel). Das Wandbild war numerisch falsch (Kern statt Wand).
- Y-1 PLAN 2.4: g = 0,5: b = 1,1667, sigma_W = 0,411, 2 sigma_Rand = 0,962; tau_2 Arbeitswert 0,6 +- 0,2.
- Y-1 PLAN 2.6, Eto und Nitta 2012 [A durch den Y-1-Agenten]: Rabi-Kopplung erster Ordnung; je Bruchwirbel eine
  zusammengeklebte Wand T_1 = sqrt(T_12^2 + T_31^2); Z_3-Fall: gleichseitiges Dreieck der Groesse ~0,56 omega^-1/4,
  so dicht, dass man die Waende nicht sieht; freie Relaxation; kein Y-gegen-Dreieck-Vergleich; keine Quark-Analogie.
- ROT-1 / BAND-1 / REGGE-1: N = 2 Band mit konstanter Kraft (frei ~1,6, statisch ~1,0), Ising-Waende, Regge nein
  (Magnus), Reisslaenge 8 bis 14 durch Paarbildung; K1: leerer Schlitz bis d = 9,5 ohne Gegenwirbel; paardyn d_0 = 3
  bleibt bei 2,4 bis 2,6 (Gleichgewichtsabstand).
- BERICHT-FARBEN W6: kein Eichfeld, kein Einschluss, kein Spin 1/2, kein SU(3)-Singulett eines Koerpers; 4.3: + c sum
  |psi_a|^4 ist die kleinste Erweiterung fuer einen gleichseitigen Dreier-Grundzustand; W4: Dreikoerperterm
  Re[(psi_1 psi_2 psi_3)^k] bricht U(1) und ist verworfen; Verstoss 3: Stanev/Tesanovic-Quartik je Band fehlt uns.
- KANDIDAT 2.3 [P]: Ein hermitescher quadratischer Mischterm -psi^dagger K psi ist bei U = U(S) und g = 0 **beweisbar
  nur eine Basiswahl** (konstante unitaere Drehung diagonalisiert alles). Das trifft Kandidat 1 (Rabi-Term) direkt:
  ohne g != 0 gibt es damit keine Waende und keinen Einschluss. Das deckt sich mit Son und Stephanov (ROT-3 W3 V1):
  die Wand braucht delta g != 0, also eine U(2)-brechende Wechselwirkung.
- ROT-3 PAPIER [P]: Son/Stephanov 2002 [A]: Wand metastabil, "vortex confinement ... very similar to that of quark
  confinement"; Kasamatsu/Tsubota/Ueda 2004 [S]; Tylutki u. a. 2016 [S]: Stringbruch als QCD-Analogon; PRR 2, 033373
  (2020) [S, nur Nummer]; Chatterjee/Gudnason/Nitta 2019 [A]: Josephson-Term hoeherer Ordnung, "angular domain walls".
- y1.py (gelesen 1904 bis 2135): Kopplungskraft -g psi^*(P - psi^2); c-Term als + 2 c s_a psi in der Kraft und + c Q4 in
  der Energie; U'(S) fest als 1 + S(1,5 S - 2); b_von(k) = 1 + g(N-1)/(2N) - c/N nur fuer den radialen Startball;
  Klammer als Phasenring 0,5 < r < kl_aus; Schwerpunktbindung per Fourier-Verschiebung.

## A1. Vorab-Erwartungen (12:05:21 CEST, vor jedem externen Abruf; Regel 3)

| Nr. | Quelle (geplanter Abruf) | Erwartung | p |
|---|---|---|---|
| E1 | Eto, Nitta 2013, "Vortex graphs as N-omers and CP^{N-1} skyrmions", EPL (arXiv-Nummer erst ermitteln) | Wirbel = Knoten, Sine-Gordon-Waende = Kanten; N = 3: Dreieck-Graph; Gesamtkonfiguration = CP^{N-1}-Skyrmion; **kein** Y-Knoten ohne Wirbel am Knoten; keine Quark-/Baryon-Analogie | 0,6 |
| E2 | Eto, Nitta, PRR 2, 033373 (2020), "Confinement of half-quantized vortices ... simulating quark confinement" | zwei Komponenten, Rabi; lineares Potential, Stringbruch durch Paarbildung; Begriffe "meson" und "baryon" fuer Wirbel-Antiwirbel bzw. Wirbel-Wirbel-Molekuele; **kein** Dreier, kein Y | 0,5 |
| E3 | Cipriani, Nitta 2013, PRA 88, 013634, "colorful vortex lattices" (drei Komponenten, Rotation) | Gitter aus Wirbel-Trimeren; Analogie zu nichtabelschen CFL-Wirbeln; keine Y-Aussage | 0,7 |
| E4 | Carroll, Hellerman, Trodden 1999 (hep-th/9905217) und/oder Gibbons, Townsend 1999 | Z_3-Wess-Zumino-Modell mit drei Vakua; Y-Knoten dreier Waende ist 1/4-BPS; 120 Grad bei gleichen Spannungen; Knotenenergie endlich (Vorzeichen unsicher) | 0,8 |
| E5 | Takahashi u. a. 2001 (hep-lat/0006005) und Alexandrou u. a. 2002 (hep-lat/0107006) | Takahashi: Y-Gesetz, sigma_3q ~ sigma_qqbar; Alexandrou: Delta bei kleinen Abstaenden; **zwei Regime, Moderator Abstand** (Bissey u. a. 2007: Y bei grossen Abstaenden) | 0,7 |
| E6 | Nichtabelsche Wirbel / "baryonische" Knoten (Cipriani, Vinci, Nitta 2012 "colorful boojums"; Auzzi u. a. 2003) | Boojum: drei Farbwirbel (r, g, b) treffen sich in einem Knoten zu einem U(1)_B-Wirbel, also ein Y **von Wirbellinien in 3D**, kein Wandnetz in 2D; in 2D stossen sich die drei nichtabelschen Wirbel ab (kein gebundener Dreier) | 0,6 |
| E7 | 24-Monats-Suche (arXiv-API, WebSearch falls verfuegbar): vortex trimer / three-component Rabi / Y-junction domain wall / baryon vortex | einige neue Arbeiten zu Rabi-gekoppelten Wirbelmolekuelen (Dynamik, Gitter), **keine** mit festgehaltenem Dreier und Energie gegen Geometrie, **keine** mit Y-Knoten als Ergebnis | 0,6 |
| E8 | WebSearch verfuegbar? | erschoepft (Hinweis der Leitung) | 0,6 |

Eigene Vorab-Herleitung [Hand, vor den Abrufen] zur Topologie im rein Rabi-gekoppelten N = 3-Modell:
- Vakuum: alle relativen Phasen 0 (ein Punkt). Jede Wand ist ein 2 pi-Sprung **einer** Komponentenphase theta_a (ein
  Sprung nur in Delta_12 liesse Delta_13, Delta_23 bei pi, also kein Vakuum). Wandtypen: T_1, T_2, T_3.
- Wirbel A (1,0,0) sendet genau eine T_1-Wand aus. Sie kann an einem Antiwirbel der Komponente 1 enden oder an einem
  Knoten J, an dem T_1, T_2, T_3 zusammentreffen: Umlauf um J gibt fuer jede relative Phase +2 pi - 2 pi = 0. **Der
  Y-Knoten ist topologisch erlaubt.** Ein Dreieck mit einer Wand je Kante ist dagegen unmoeglich (Umlauf um B
  kreuzte eine T_1-Wand und gaebe n_1 = 1). Dieselbe Struktur wie in Y-1 PLAN 2.3 fuer unsere Z_2^2-Waende.
- Duennwandig, gleiche Spannungen: E_Y = T_1 L_St, E_Dreieck nicht als Einzelwandnetz moeglich. Y ist also die
  Vorhersage fuer festgehaltene, weit getrennte Wirbel, falls die Wand nicht vorher durch Paarbildung reisst
  (Son/Stephanov: Wand metastabil; Y-1: Abschirmung im billigen Kern).
- Erwartung fuer E1/E2 daraus: Die Literatur zeigt kompakte Dreiecke, weil sie freie Wirbel relaxiert; ein Y-Netz
  taucht nur bei festgehaltenen Enden auf. Ob jemand das gerechnet hat: p = 0,3.
- Nachtrag beim Lesen von Nitta u. a. 2012 (A3.1): Genau diese Herleitung steht dort als Argument fuer das Y
  (Abschn. 3: die Josephson-Energie entlang der radialen Pfade nimmt am Zentrum den Wert (1/2) gamma |Psi_i||Psi_j| an,
  ein Kantennetz liesse eine Membran mit endlicher Energie im Dreieck). Bestaetigt, nicht neu.

## A2. Abrufprotokoll (je Abruf: Erwartung bestaetigt -> eine Zeile; verletzt -> voller Zyklus in A3)

### A2.1 Erste Abrufrunde (eingetragen bis 12:09:47)

- E8 **bestaetigt**: WebSearch erschoepft (200/200). Weiter nur arXiv-API und arXiv-Abstracts per WebFetch.
- E1 **bestaetigt im Abstract** [A-W]: Eto, Nitta, EPL 103, 60006 (2013), arXiv:1303.6048: "Stable vortex N-omers ...
  classify all possible N-omers in terms of the mathematical graph theory and numerically construct all graphs for
  N = 2, 3, 4 ... N-omers are well described as CP(N-1) skyrmions when inter-component and intra-component couplings
  are U(N) symmetric ... size dependence on the Rabi coupling." Volltext noetig (Knoten ohne Wirbel? N = 3-Graphen?).
- E2 **verletzt** (A3.3): Das Einschluss-Papier ist Eto, Nitta, **PRA 97, 023613 (2018)**, arXiv:1702.04892, nicht
  PRR 2, 033373 (2020). Abstract [A-W]: "simulates certain aspects of the confinement in SU(2) QCD in 2+1 space-time
  dimensions"; Zirkulation <-> Baryonzahl, relative Phase <-> duale Gluonen; nur Singulett-Zustaende stabil als
  gebundene Paare ("baryons and mesons"); lineares Potential; jenseits eines kritischen Abstands Paarbildung.
- E3 **bestaetigt** [A-W]: Cipriani, Nitta, PRA 88, 013634 (2013), arXiv:1304.4375: drei Bruchwirbelsorten, dreieckige
  "colorful" Gitter geordneter Bruchwirbel; in anderen Parameterbereichen Phasentrennung. Keine Y-Aussage im Abstract.
- E6 **bestaetigt mit Nuance** [A-W]: Cipriani, Vinci, Nitta, PRD 86, 121704 (2012), arXiv:1208.5704 (Wortlaut in E16).
- E4 **teilweise bestaetigt** [A-W]: Carroll, Hellerman, Trodden, PRD 61, 065001 (2000), hep-th/9905217: "multiple
  discrete vacua ... segments of domain walls meeting at one-dimensional junctions ... preserving one quarter of the
  supersymmetry ... BPS bound ... construct a solution explicitly in a special case." Z_3 und Vorzeichen der
  Knotenenergie stehen nicht im Abstract.
- E5 **bestaetigt, zwei Lager** [A-W]: Takahashi, Matsufuru, Nemoto, Suganuma, PRL 86, 18 (2001), hep-lat/0006005:
  V_3Q = const + Coulomb (zwei Koerper) + sigma_3Q L_min, "with accuracy better than a few %", sigma_3Q ~ sigma_QQbar,
  A_3Q ~ A_QQbar/2, Gitter 12^3 x 24, beta = 5,7. Alexandrou, de Forcrand, Tsapalis, PRD 65, 054503 (2002),
  hep-lat/0107006: "consistent with a sum of two-body potentials, possibly with a weak many-body component ... support
  to the Delta ansatz". Moderator (Abstand) im Abstract nicht genannt.
- E7 **teilweise verletzt**: arXiv-API, 2024-09-01 bis 2026-10-01:
  - "vortex trimer(s)" in Titel oder Abstract: **0 Treffer**.
  - "coherently coupled" AND vortex AND (confinement OR molecule OR "domain wall"): **0 Treffer**.
  - junction AND "domain wall" AND vort*: 1 Treffer: Banerjee u. a., arXiv:2606.22532 (Juni 2026).
  - baryon AND (condensate OR superfluid) AND vort*: 8 Treffer, davon einschlaegig: Hamada, arXiv:2509.20844 (Sept.
    2025) "Baryons as linked vortices in QCD matter with isospin asymmetry" (Verkettungszahl = Baryonzahl); Hamada,
    arXiv:2602.11762 (Feb. 2026); Mameda, arXiv:2603.29325 (Maerz 2026); Nitta, arXiv:2609.12080 (Sept. 2026).
    **Keiner** davon: drei Wirbel mit Y-Knoten. Die Klasse "Baryon = topologische Wirbelstruktur (Verkettung)" ist
    aktiv; sie gehoert zu Kandidat 4 (Soliton = Hadron), nicht zu "drei Quarks".

### A1b. Vorab-Erwartungen fuer die zweite Runde (12:09:47, vor dem Abruf)

| Nr. | Abruf | Erwartung | p |
|---|---|---|---|
| E9 | Volltext arXiv:1303.6048 (N-omer) | Graphen: Knoten = Wirbel, Kanten = Waende; Sine-Gordon-Kink je Komponentenphase; N = 3: nur Dreieck oder Kette ("Stab"); **kein wirbelfreier Knoten**; U(N)-Fall = CP^2-Lump mit gefuelltem Kern; Groesse ~ omega^-1/4 | 0,6 |
| E10 | Volltext arXiv:1702.04892 (Einschluss 2018) | "baryon" = zwei Wirbel verschiedener Komponenten (1,0)+(0,1), "meson" = Wirbel + Antiwirbel derselben Komponente; SU(2) heisst: Baryon = zwei Quarks; Ausblick auf N Komponenten = SU(N) mit N-Wirbel-Baryonen; Stringbruch numerisch gezeigt; kein Y (bei SU(2) gibt es keins) | 0,6 |
| E11 | jr-Suche PRR 2, 033373 (2020) | ein Nitta-Papier zu Wirbelmolekuel-Dynamik oder Sine-Gordon-Kinks auf Wirbeln; nicht der Einschluss-Aufsatz | 0,5 |
| E12 | Bissey u. a. 2007 (hep-lat/0606016) und Takahashi, Suganuma 2002 (hep-lat/0204011) | Bissey: Y-Form bei grossen Abstaenden, Delta-artig bei kleinen; Takahashi 2002: Y bestaetigt mit ~300 Konfigurationen; Moderator = Abstand gegenueber Flussroehrenbreite | 0,7 |
| E13 | Oda, Ito, Naganuma, Sakai 1999 (hep-th/9910095) | exakte Loesung eines Z_3-Knotens im Wess-Zumino-Modell; Knotenenergie **negativ** | 0,6 |
| E14 | breitere 24-Monats-Suchen: Rabi AND vortex AND BEC; "vortex molecule(s)"; "fractional vortices" AND (three-component OR multicomponent) AND "domain wall" | 3 bis 15 Treffer, Dynamik/Gitter/Spin-Bahn; keiner mit festgehaltenem Dreier und E gegen Geometrie; keiner mit Y | 0,6 |
| E15 | Abstract 1601.03695 (Tylutki u. a. 2016) | lineares Potential, Praezession; bei grossem Omega zerfaellt die Wand in Stuecke mit neuen Wirbelpaaren: "analog of ... string breaking" | 0,8 |
| E16 | Abstract 1208.5704 im Wortlaut | ein U(1)_B-Wirbel (drei Neutronenwirbel?) spaltet an der Grenzflaeche in drei Farbwirbel | 0,6 |
| E17 | Abstract 2606.22532 | Z_N-Waende in SU(N) mit Stringknoten; Feldtheorie in 3+1; keine Kondensatanwendung | 0,7 |

### A2.2 Zweite und dritte Abrufrunde (eingetragen ab 12:19)

- E9 **bestaetigt mit anderem Grund** [A]: Kanten sind **Rabi-Kopplungen**, nicht Waende ("we identify vertices as
  vortices, and the edge connecting i-th and j-th vertices as the Rabi coupling omega_ij if it is nonzero", S. 2).
  N = 3: Dreieck (omega alle 0,1) und "rod" (omega_23 = 0), Abb. 6. "For g = g-tilde, an axisymmetric giant vortex appears
  ... interpreted as a CP^{N-1} skyrmion. On the other hand, for g > g-tilde, there appear N fractional vortices ...
  connected by domain walls" (S. 2). "N - 1 domain walls are attached to the i-th vortex ... it must be connected to the
  boundary or to vortices winding around the other components" (S. 2). Imaginaerzeit mit fester Windung und
  konstanter Dichte am Rand (S. 1). Kein Quark/Baryon/QCD-Wort (Grep, A5). Groesse faellt mit omega (Abb. 2).
- E10 **teilweise verletzt** [A]: Baryon = "a pair of vortices in each component", Meson = "a pair of a vortex and an
  antivortex in the same component" (Abstract); "baryon is static at the equilibrium and rotates once it deviates ...
  while a meson moves with constant velocity"; Gleichgewicht R_0 = 2,8 R* (Abb. 6, u = 2 u_12 = 1, eta = 0,01), R_0
  faellt mit eta (Abb. 5); R_c ~ 21 R* (eta = 0,1); Sine-Gordon-Wand T_SG = 8 v^2 sqrt(m omega/hbar); Imaginaerzeit,
  dann Realzeit. Verletzt: der Ausblick nennt ausdruecklich "the confinement of 1/3 quantized vortices in three-component
  BECs, for which a baryon was constructed numerically in Ref. [30, 31]" (S. 5); [30] = Eto/Nitta PRA 85 (2012) und
  EPL 103 (2013), [31] = Nitta/Eto/Cipriani JLTP 175 (2013). Anhang B: Baryonen und Mesonen in bosonischer SU(2)-QCD.
- E11 **verletzt** (kleiner Zyklus): PRR 2, 033373 (2020) = Eto, Ikeno, Nitta, "Collision dynamics and reactions of
  fractional vortex molecules in coherently coupled BECs", arXiv:1912.09014 [A-W]: "'hadrons' either of mesonic type
  ... or of baryonic type ... Mesonic molecules move straight with a constant velocity while baryonic molecules rotate
  ... swap a partner in collisions ... Feynman diagrams ... selection rule". Korrigierte Erwartung: die Nitta-Gruppe hat
  die Zweikomponenten-Reaktionen 2020 abgeschlossen; danach kein Dreikomponenten-Einschluss (A2.3).
- E12 **bestaetigt** [A-W]: Bissey u. a. 2007: "at large separations, Y-shape flux-tube formation is observed. T-shaped
  paths are observed to relax towards a Y-shaped topology"; keine leere Delta-Verteilung, sondern "an expulsion of
  gluon-field fluctuations in the shape of a filled triangle" bei kleinen Abstaenden, Gitterabstand 0,123 fm.
  Takahashi u. a. 2002: "more than 300 different patterns", 12^3 x 24 (beta 5,7) und 16^3 x 32 (beta 5,8; 6,0), "all these
  fit analyses support the Y-ansatz", Delta nur als Naeherung mit reduzierter Spannung.
- E13 **teilweise verletzt** [A-W]: Oda u. a.: "N = 1 supersymmetric U(1) x U(1)' gauge theory with three pairs of chiral
  superfields ... the new central charge Y_k gives a negative contribution to the mass of the domain wall junction
  whereas Z_k gives a dominant positive contribution." Kein Z_3-Wess-Zumino; Vorzeichen wie erwartet.
- E14 **teilweise verletzt** [A-W]: Rabi AND vort* AND BEC: 3 Treffer (Yukalov 2025 Uebersicht; Syu 2025 analoge
  Schwarze Loecher; Wang 2024 adiabatischer Transfer), keiner einschlaegig. "vortex molecule(s)": Gavrilov 2025
  (bekannt) und **Gudnason/Nitta 2025** (chirale nichtabelsche Wirbelmolekuele, "one or two domain walls", zwei Wirbel).
  fractional/half-quantum AND multicomponent: **Rantanen 2025** (3He-B Dreifachkern; "stretched between pinning sites ...
  the HQV picture becomes more applicable when separation between subcores becomes large"), Hui 2026 (Quanten-Hall,
  Einschluss von Bruchladungen), Canfora 2025 (BPS-Spinor-GP). Zusatzsuche three-component AND vort* AND (domain wall
  OR junction): Zou 2025 (Kagome, 4e), Rantanen 2025.
- E15 **bestaetigt** [A-W]: "the increase of the Rabi coupling results in the disintegration of the domain wall into
  smaller pieces, connecting vortices of new-created vortex pairs ... the analogue of quark confinement and string
  breaking in quantum chromodynamics."
- E16 **berichtigt** [A-W]: "three neutron vortices join at a boojum and split into three color magnetic vortices which
  host confined color-magnetic monopoles when strange quark mass is taken into account." Also 3 -> 3, nicht 1 -> 3.
- E17 **bestaetigt** [A-W]: 2+1 und 3+1; "In SU(3) gauge theory, the merger of two non-planar Z_3 domain walls into a
  single wall proceeds via the creation of a vortex-antivortex pair in 2+1 dimensions."
- Kasamatsu/Tsubota/Ueda 2004 [A-W, cond-mat/0406150]: "connected by a domain wall of the relative phase, constituting a
  'vortex molecule' ... nonaxisymmetric (pseudo)spin texture with a pair of merons ... anisotropy ... caused by the
  difference in the scattering lengths."
- Gibbons/Townsend 1999 [A-W]: "the Wess-Zumino model with quartic superpotential admits static solutions in which three
  domain walls intersect at a junction ... configurations saturating [the bound] preserve 1/4 supersymmetry."
- Gallemi u. a. 2019 [A-W, 1906.06237]: zwei Zerfallswege (klein Omega: energetisch, Paar derselben Sorte; gross Omega:
  Schlangeninstabilitaet mit negativer effektiver Masse), Natrium-Mischungen.
- Auzzi u. a. 2003 [A-W]: nichtabelsche Flussroehren, Einschluss von Monopolen, keine Knoten/Baryonen im Abstract.
- Nitta/Eto/Cipriani JLTP 2014 [A-W, 1307.4312]: Trimere, N-omere, Graphen; Gitter mit Rabi; "Abrikosov lattices are
  robust in three-component BECs". Kein Y-Wort im Abstract.

### A2.3 Ungeplanter Hauptbefund (Suche au:Nitta AND three-component AND confinement/baryon AND vortex, alle Jahre)

- Treffer: Nitta/Uchino/Vinci 2014 [A-W]; Eto/Hirono/Nitta/Yasui 2014 [A-W]; **Nitta, Eto, Fujimori, Ohashi 2010/2012,
  arXiv:1011.2552, JPSJ 81, 084711** [A-W, dann Volltext A]. Gegenprobe ohne Autorenfilter (three-component OR
  multicomponent) AND (BEC OR condensate OR superconductor) AND (baryon OR "quark confinement" OR 1/3-quantized) AND
  vort*: nur Haber 2018 (Dissertation, allgemein) und Nitta 2010. Y-junction/Steiner AND vort* AND condensate: Nitta 2010
  und Lin 2026 (Gluonenknoten, keine Wirbel). Damit: **nach 2013 kein Dreier-Baryon aus Wirbeln in Kondensat oder
  Supraleiter** (arXiv-API; Konferenzbaende nicht erfasst).

## A3. Erwartungsverstoesse, volle Zyklen

### A3.1 Nitta u. a. 2012 [A, Volltext]: Y-Knoten bei festgehaltenen 1/3-Wirbeln

- Modell (Gl. 1, 2): GL mit U(1)-Eichfeld, (lambda_i/4)(|Psi_i|^2 - v_i^2)^2 je Komponente, Josephson
  -gamma_ij |Psi_i||Psi_j| cos(theta_i - theta_j), gamma_ij > 0 (Eisenpniktide; gamma < 0 waere frustriert).
- Topologie (Gl. 4, 5): (1,0,0) = (1/3)(1,1,1) + (1/3)(1,0,-1) - (1/3)(-1,1,0): jeder Wirbel traegt 1/3 der Eichdrehung
  (Fluss Phi_0/3) plus globale relative Drehungen; "the fractional vortices correspond to global ungauged symmetries and
  hence they have a logarithmically divergent energy, even in the absence of the Josephson terms" (S. 3); der
  (1,1,1)-Wirbel ist endlich (Abrikosov).
- Y-Argument (Abschn. 3): Josephson-Energie entlang jedes radialen Pfads gamma_ij|Psi_i||Psi_j| cos((4 pi/3) f(r)),
  am Zentrum (1/2) gamma_ij |Psi_i||Psi_j| != 0; ein Kantennetz liesse "a domain (membrane) with finite energy ... inside
  the triangle. The sine-Gordon kinks should bend to form the Y-junction." Numerik: Relaxation, hbar = c = 2m = 2e = v =
  lambda/2 = 1, gamma = 0,02, Box +-15; "we have fixed the positions of the three vortices"; ohne Festhalten "these
  vortices collapse to form a single integer vortex".
- Wandspannung (Gl. 12, 17, 20): T^(1) = 8 sqrt(K^(1) Gamma^(1)), K^(1) = hbar^2 (v_2^2 + v_3^2)/(12 m), Gamma^(1) =
  2(eta_2^2 + eta_3^2), also die Quadratsumme wie bei Eto/Nitta 2012 Gl. 10; symmetrisch T_dw = 8 hbar v^2 sqrt(2 gamma/(3m)).
  Wandbreite ~ 4 sqrt(K/Gamma) = 4 sqrt((1/3)/0,08) ~ 8 [Hand] bei ihren Parametern; Kernkosten (lambda/4) v^4 = 0,5 je
  Flaeche gegen Josephson gamma v^2 = 0,02 je Flaeche.
- Ein-/Entschluss (Abschn. 4): Wandentropie k_B ln(2 pi)/xi je Laenge; T_crit = xi T_dw/(k_B ln 2 pi); wie Goryo u. a.
- Schluss (Abschn. 5): Y = "genuine three-body interaction"; Dualitaet Polyakov/Shifman-Unsal (Quarks <-> Wirbel,
  elektrischer Fluss <-> Sine-Gordon-Wand); Vermutung: Y-Knoten des QCD-Baryons per Dualitaet zu Dreiband-Supraleitern;
  mehr Baender -> Tetra-, Pentaquarks.
- Korrigierte Erwartung: Der Y-Knoten aus Wirbelwaenden ist seit 2010 bekannt und wird von derselben Gruppe als
  Baryon-Vorbild gefuehrt; offen ist nur die Uebertragung auf globale Modelle mit U(S)-Potential (unseres, BEC) und die
  Energie gegen Geometrie.

### A3.2 Rantanen 2025 [A-W]: Dreifachkern in 3He-B, gestreckt zwischen Haftstellen

- Abstract: "an alternative representation of the vortex as a combination of three vortices, one in each component of
  the spin-triplet superfluid ... a double-core vortex stretched between pinning sites ... the HQV picture becomes more
  applicable when separation between subcores becomes large." Bindung dort aus Gradienten- und Dipolenergie des
  3 x 3-Ordnungsparameters, kein Rabi-Term. Fuer uns: drittes Feld mit demselben Regimewechsel (A-Tabelle, Abschn. 3).

### A3.3 Eto/Nitta 2018 und Eto/Ikeno/Nitta 2020: unser N = 2 ist "bekannt unter Namen"

- ROT-1 paardyn (Omega d konstant, Drehsinn gegen die Windung), REGGE-1 (Magnus, kein Regge), BAND-1 (Reissen bei 8 bis
  14 durch Paarbildung), Y-1 Meson (flach ab 12) entsprechen: "baryon ... rotates once it deviates from the equilibrium",
  "meson moves with constant velocity", "broken, thus creating other baryons or mesons in the middle when ... separated
  by more than some critical distance" (2018, Abstract); Reaktionen mit Partnertausch (2020). Unterschied: dort
  Sine-Gordon-2 pi-Wand, bei uns zwei Ising-pi-Waende mit Linse; dort GP mit u_12, bei uns U(S) plus cos 2 Delta.
  Fuer die Journal-Einordnung von ROT-1/BAND-1 (L4) sind das die Referenzen.

## A4. Handrechnungen (Duennwand, g = 0,5, Zahlen aus Y-1 PLAN 2.4; alles [Hand], grob)

- Groessen: b = 1 + g/3 - c/3 + (b_0 - 1); S ~ b; sigma_W(S) = 0,411 (S/1,1667)^{3/2}; w_W ~ 1/sqrt(g S) = 1,31 bei S = 1,1667.
- Kosten je Flaeche, die eigene Komponente aus einem Kern zu entfernen (N = 3, Fuellung durch zwei Komponenten je S/2):
  kappa = (g/12) S^2 [cos-2Delta-Verlust] + c S^2 (1/2 - 1/3) = c S^2/6 [Quartik] + epsilon (S - S/2) = epsilon S/2 [Rabi;
  voll: 3 epsilon (S/3) = epsilon S, entleert: epsilon sqrt(S/2) sqrt(S/2) = epsilon S/2].
- Vergleich: Abschirmung (Scheibe Radius r_c, Gegenwirbel am Ringrand) gegen zwei W-Waende der Laenge L_a (Arm zum
  Knoten, L_a ~ L_St/3): pi r_c^2 kappa gegen 2 sigma_W L_a. Gegenwirbelkern und Knotenenergie vernachlaessigt.

| Fall | b, S^2 | kappa | sigma_W | r_c = 2,5: Scheibe gegen Waende (L_a = 5,2) | r_c = 4,5 | Beobachtung |
|---|---|---|---|---|---|---|
| c = 0, eps = 0 | 1,167; 1,361 | 0,057 | 0,411 | 1,1 gegen 4,3: Abschirmung | 3,6 gegen 4,3: knapp | Y-1: Abschirmung; weiter Ring: gleich 9/12 intakt, 15 nicht |
| c = 0,4 | 1,033; 1,067 | 0,044 + 0,071 = 0,116 | 0,342 | 2,3 gegen 3,6: Abschirmung | 7,4 gegen 3,6: Waende | Y-1 C1: Gegenwirbel 11/12 (Ring 2) |
| c = 1, b_0 = 1 | 0,833; 0,694 | 0,029 + 0,116 = 0,145 | 0,248 | 2,8 gegen 2,6: Gleichstand | 9,2 gegen 2,6: Waende | nicht gerechnet |
| c = 2, b_0 = 1,667 | 1,167; 1,361 | 0,057 + 0,454 = 0,51 | 0,411 | 10,0 gegen 4,3: Waende (2,3x) | 32 gegen 4,3: Waende (7x) | nicht gerechnet |
| eps = 0,3, c = 0 | 1,167; 1,361 | 0,057 + 0,175 = 0,232 | 0,411 | 4,5 gegen 4,3: Gleichstand | 14,8 gegen 4,3: Waende | nicht gerechnet |
| N = 2, K1 (g/4) | 1,125; 1,266 | 0,158 | Schlitz 0,97/L, Linse 0,82/L | 3,1 gegen 7,8 (d = 9,5): Abschirmung | - | **K1: Schlitz intakt, kein Gegenwirbel** -> Abschaetzung falsch (>= 2,5x) |

- c-Deckel ohne Nachstimmen: kappa_c = c S^2/6 mit S = 1 + g/3 - c/3; Maximum bei c = 1 + g/3 = 1,167 (Ableitung
  (1+g/3-c/3)^2 - (2c/3)(1+g/3-c/3) = 0), Wert 1,167 x 0,605/6 = 0,118. Zusammen mit dem g-Anteil hoechstens ~0,14, waehrend
  sigma_W mit S^{3/2} faellt: das Verhaeltnis erreicht ~1, nicht mehr.
- Nachstimmen: b_0 = 1 + c/3 haelt b(N = 3) = 1,167. Dann b_eff(N = 1) = b_0 - c = 1 - 2c/3: fuer c > 1,5 kein Einzelball
  (U/S = 1 + |b_eff| S + S^2/2 > 1). b_eff(zwei Komponenten, gleiche Dichte) = b_0 + g/4 - c/2 = 0,79 bei c = 2.
- Vakuumschranke Rabi: U_eff/S = (1 - eps) - b S + S^2/2, Minimum 1 - eps - b^2/2 = 0,319 - eps; eps < 0,32, sonst liegt
  das homogene Kondensat unter dem Vakuum (Analogon KANDIDAT 5.2).
- Y-Vorhersage Arm B: Steigung je L_St zwischen 2 sigma_W = 0,82 (Kanal) und 2 sigma_Rand = 0,96 (Schlitz), tau_2-
  Arbeitswert 0,6: E(12) - E(9) = 0,6 ... 0,96 x 5,196 = 3,1 ... 5,0. Kollinear 8 (L_St = 16) gegen gleichseitig 9 (15,59):
  Y +0,25 ... +0,39; Dreieck (P/2 16 gegen 13,5): +1,5 ... +2,4.

## A5. Gegensweep-Pruefungen (durchgefuehrt)

- Grep der Volltexte (pdftotext-Ausgaben im Scratchpad) auf quark|baryon|parton|confine|QCD: Trimer 2012 zwei Zeilen
  ("partonic"), N-omer 2013 null Zeilen. Y-1-Agent bestaetigt.
- kappa-Abschaetzung gegen K1 (N = 2): siehe A4-Tabelle, Widerspruch, Faktor >= 2,5.
- KANDIDAT 2.3 gegen Eto/Nitta 2013 und 2012 (U(N)-Fall): bestaetigt (axialsymmetrischer Riesenwirbel).
- Y-1-Tabelle: alle Beutel bei L_St <= 15,6 (gleichseitig 6, 9; kollinear 5; mit c bis gleichseitig 12 und kollinear 6,5);
  abgeschirmte Zustaende ab L_St >= 12 (gestreckt 9 hat einen Schlitz plus Abschirmung). Der Uebergang kompakt ->
  abgeschirmt liegt bei Armen von ~4 bis 5, also 3 bis 4 Wandbreiten.

## A6. Verfahren, Grenzen, Verstoesse

- Keine Rechnung, kein python/awk lokal; pdftotext fuer drei PDFs (IO). Keine gesperrten Pfade geoeffnet. Kein git, kein
  Journal.
- Grenzen: WebSearch nicht verfuegbar; arXiv-API-Phrasensuche kann Treffer verfehlen (acht Anfragen fuer 24 Monate,
  vier ohne Zeitfenster); INSPIRE nicht befragt; Abb. 2 von Nitta u. a. nur als Bild, Dreiecksgroesse unbekannt;
  Son/Stephanov nicht erneut gelesen (ROT-3 [A] uebernommen).
- Erwartungen gebunden vor Abruf: A1 (12:05:21), A1b (12:09:47). Die dritte Runde (Rantanen, Gudnason, Gibbons/Townsend,
  Kasamatsu, Trimer-PDF, Auzzi, Nitta-2012-PDF, JLTP) hatte keine eigene Tabelle; ihre Erwartungen standen nur in A1/A1b
  sinngemaess (E4, E6, E14). Selbstanzeige: fuer den Hauptbefund (Nitta u. a. 2012) gab es keine explizite Vorab-Zeile;
  die naechste Zeile war A1 "Ob jemand das gerechnet hat: p = 0,3".

- Ende (date): 2026-09-30 12:27:32 CEST. Bericht und Arbeitsfeld in einer Datei; nichts gerechnet, nichts gestrichen.
