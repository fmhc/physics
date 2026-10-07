# DEFEKT-NETZ-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 47)

- Start 2026-10-05 07:41:53 CEST (date). Plantext ab 08:02:27 CEST (date), vor jeder Hauptrechnung.
- Grundlage: KARTE.md, woertlich bindend (DN0 bis DN3, Bedeutung). Der Zusatz der Leitung ist ebenso verbindlich und
  bleibt hier getrennt gekennzeichnet ("Zusatz").
- Gelesen: KARTE; WELTKRISTALL-L DOSSIER Abschnitt 6; TT-ISO-1 ERGEBNIS, PLAN, code; TT-GLAS-1 ERGEBNIS, PLAN, code;
  DANZER-NAEHERUNG-1 ERGEBNIS Abschnitte 1, 2, 5 und PLAN Abschnitte 3 bis 5 (Definition Grundtempo); EINE-WELT-LOCH-1
  ERGEBNIS Abschnitte 1, 2, 4, 5 (Netz S); per jq zwei Rohwerte: TT-ISO-1 lauf-69/gitter-V-A1R1.json und
  gitter-S-A1R1.json, Schluessel spanne_J1.
- Vor diesem Plan liefen Rauchtests auf der .69 (Abschnitt 7). Gelesen habe ich davon nur Rueckgabewerte, Laufzeiten und
  Dateinamen, keine Werte.
- Kennzeichen: [M] Mathematik bzw. Codelesung, [P] Projektdatei, [S] Quelle, [F] Festlegung, [H] Hypothese,
  [L] Gedaechtnis. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 0. Lagen und Quelle [S]

- Quelle: NRL Crystal Lattice Structures (Mehl et al.), Spiegel www.atomic-scale-physics.de/lattice/struk/c15.html und
  .../a15.html, per WebFetch am 05.10. gegen 07:51 CEST gelesen. Vier Abrufe: zwei AFLOW-Adressen
  (aflow.org/prototype-encyclopedia/AB2_cF24_227_a_d[.C15].html) gaben 404, dann die zwei NRL-Seiten.
- **C15** (Cu2Mg, Fd-3m Nr. 227, cF24; Quelle dort: Wyckoff, Crystal Structures Vol. I, S. 365-367):
  - fcc-Translationen (0, 1/2, 1/2), (1/2, 0, 1/2), (1/2, 1/2, 0);
  - Mg 8a: (1/8, 1/8, 1/8), (7/8, 7/8, 7/8);
  - Cu 16d: (1/2, 1/2, 1/2), (1/2, 1/4, 1/4), (1/4, 1/2, 1/4), (1/4, 1/4, 1/2).
  - Je kubischer Zelle 8 Mg und 16 Cu = 24 Ecken.
- **A15** (Cr3Si, Pm-3n Nr. 223, cP8; Quelle dort: Nevitt):
  - Si 2a: (0, 0, 0), (1/2, 1/2, 1/2);
  - Cr 6c: (1/4, 1/2, 0), (3/4, 1/2, 0), (0, 1/4, 1/2), (0, 3/4, 1/2), (1/2, 0, 1/4), (1/2, 0, 3/4).
  - 8 Ecken je Zelle. Cr-Ketten laengs x (y = 1/2, z = 0), y und z.
- Ideallagen ohne freie Parameter. Kubische Kante a = 1. Absolutwerte von omega^2/k^2 skalieren wie a^3 (B ~ a,
  A dimensionslos, k ~ 1/a) und sind eine Festlegung; die Spanne ist skalenfrei [M].

## 1. Ableitbarkeits- und Rohdatenprobe (vor jeder Rechnung)

### 1.1 Das Netz S aus EINE-WELT-LOCH-1 ist C15 [M, P]

- ew.geometrie('S') (Codelesung): Ecken = Finns Pyrochlor R8/8 = (1,1,1)/8, (1,-1,-1)/8, (-1,1,-1)/8, (-1,-1,1)/8 und
  die Lochmitten C1 = -(1/4)(1,1,1), C2 = (1/2)(1,1,1), fcc mit kubischer Kante 1.
- Um (3/8, 3/8, 3/8) verschoben sind das genau die C15-Lagen der Quelle:
  - Cu: (1,1,1)/8 + 3/8 = (1/2, 1/2, 1/2); (1,-1,-1)/8 + 3/8 = (1/2, 1/4, 1/4); die anderen zwei ebenso.
  - Mg: C1 + 3/8 = (1/8, 1/8, 1/8); C2 + 3/8 = (7/8, 7/8, 7/8).
- Zellen von S je primitiver Zelle: 2 Finn-Tetraeder (Cu4), 8 Kegel (Mg Cu3), 24 Achsen-Tetraeder (Mg2 Cu2, sechs um
  jede Achse C1-C2 durch ein Sechseck). Das sind 34 = 136/4 Tetraeder, 40 = 160/4 Kanten, 6 = 24/4 Ecken. Genau das sind
  die FK-Tetraeder von C15 (Zaehlung der Leitung: 136 Tetraeder, 160 Kanten) [M].
- **Folge:** Ist die Delaunay-Zerlegung von C15 die FK-Zerlegung (keine Gleichstaende, 1.2), dann ist das C15-Netz
  dieser Karte dasselbe Netz wie S. Dasselbe Modell (A1R1, J = 1, Eck-Eichung, skalare Regel) und dieselbe Spannenmessung
  (13 Richtungen x 2 Zweige x 2 |k|) gaben in TT-ISO-1 fuer S: **s(S) = 0,026847167 = 2,6847 %** [P,
  lauf-69/gitter-S-A1R1.json, spanne_J1].
- **Damit sind DN1 (2,68 % < 6,34 %) und DN3 (2,68 % < 3 %) vorab aus Projektdaten ableitbar: eingetroffen**, sofern
  die Identitaet S = C15 im Lauf L0 besteht. Die C15-Rechnung ist dann eine Reproduktion, keine Messung.
- Ebenso schon vorhanden fuer S, also fuer C15 [P, EINE-WELT-LOCH-1 Abschnitte 2, 4]: 2 masselose TT-Moden an 46
  Punkten (TT-Anteil 1,000, linear), 14 Moden mit Luecke (kleinster Wert 5,82), nichts waechst; an 4 095 Gitter-k
  (L = 16) stabil; omega^2/k^2 in [100] 0,21130 / 0,21698, in [111] 0,21509.
- Die Ableitbarkeitsprobe der Leitung ("DN1 bis DN3 sind nicht ableitbar") trifft fuer DN1 und DN3 also nicht zu. Der
  Projekt-grep des Dossiers suchte Namen (C15, MgCu2, Laves), nicht die Struktur.
- **Nicht ableitbar und neu ist nur A15**, also s(A15) und damit DN2. Mein Projekt-grep 07:55 (Weaire, Cr3Si, MgCu2,
  Laves, alle *.md und *.py unter coordination, Ausschluesse wie vorgeschrieben): keine A15-Netzrechnung.

### 1.2 DN0 ist vorab ableitbar [M]

- Zaehlung der Leitung (Karte): C15 160 Kanten, davon 16 mit 6 Tetraedern (Mg-Mg), 136 Tetraeder, q = 5,1, f6 = 10 %;
  A15 54 Kanten, davon 6 Kettenkanten, 46 Tetraeder, q = 46/9, f6 = 1/9.
- Gleichstaende, Schreibtischrechnung an den Umkugeln der FK-Tetraeder (in Einheiten a):
  - C15 Mg2Cu2: Mitte 0,128 neben der Sechseckmitte, R = 0,251; naechster fremder Punkt im Abstand 0,376.
  - C15 MgCu3: R = 0,238; Gegenecke im Abstand 0,411. Cu4: R = 0,217; naechstes Mg im Abstand 0,433.
  - A15 Cr4-Disphenoid (zwei Kettenstuecke): R = 0,354; naechster fremder Punkt 0,559.
  - A15 Si Cr3 mit Kettenkante: R = 0,349; naechster fremder Punkt etwa 0,60. Si Cr3 gleichseitig: R = 0,361; naechster
    etwa 0,505.
  - Erwartung: keine Gleichstaende, Delaunay = FK. Geprueft habe ich nur diese Typen, nicht alle Punkte.
- Grundtempo: Kubische Symmetrie macht jeden Tensor 2. Stufe isotrop, also auch das skalare Grundtempo [M]. Kontrolle.

### 1.3 Nicht ableitbar

- s(A15) und damit DN2. Kubisch bleibt ein freier l = 4-Anteil. A15 hat 2 von 8 Ecken mit Ikosaeder-Umgebung (Z12),
  C15 16 von 24.

## 2. Bau [F]

- **Zellen:** kubische Zelle (C15 24 Ecken, A15 8 Ecken). Kontrolle (beschreibend): Superzelle 2 x 2 x 2 (192 bzw. 64
  Ecken); die masselosen Werte an [100], [110], [111] muessen gleich sein (Bloch-Probe, <= 1e-6 relativ).
- **Delaunay** wie TT-GLAS-1 (tg.zufallsnetz): 27 Kopien, scipy.spatial.Delaunay mit Standardoptionen, je Tetraeder die
  Kopie mit Schwerpunkt in der Zelle.
  - Eigene Funktion in dn.py, weil tg.zufallsnetz Zufallspunkte erzeugt. Gleicher Weg.
  - Zuordnung zur Zelle mit generischer Verschiebung (0,01234; 0,02345; 0,03456), weil Schwerpunkte im Kristall sonst
    genau auf dem Zellrand liegen koennen [F].
- **FK (kristallographisch):** alle 4-Cliquen des Nachbargraphen. Abstand < 0,52 a (C15) bzw. < 0,66 a (A15).
  - Proben: keine Paarabstaende in +-0,03 a um die Schwelle; Koordination Z12/Z16 (C15) bzw. Z12/Z14 (A15).
- **Gleichstands-Zaehlung (Zusatz 1):** je Tetraeder die Zahl der Punkte aller 27 Kopien
  - auf der Umkugel: | |P - C|/R - 1 | <= 1e-9;
  - innen: < -1e-9.
  - Gleichstand = 5 oder mehr Punkte auf einer Umkugel. Dazu die kleinste relative Marge der uebrigen Punkte.
  - Gezaehlt fuer Delaunay und FK. Die Kugeln liegen ganz im Kopienbereich (wird geprueft).
- **Regel Bauweg (Zusatz 2, Fehlerzweig von DN0):**
  - Gleichstaende (Delaunay) = 0: Delaunay, wie die Karte sagt.
  - Sonst: FK-Tetraeder, kein Zitter.
  - L0 schreibt den Bauweg in dn0.json; die TT-Laeufe lesen ihn dort.
- **Netzproben (L0):** Volumensumme = Zellvolumen; jedes Dreieck in genau 2 Tetraedern; Euler V - E + F - T = 0;
  Diedersumme je Kante 2 pi; kleinstes Volumen; Delaunay = FK (Schluesselmengen); C15 = S (1.1, Zellen von S
  verschoben und mit den fcc-Translationen in die kubische Zelle gebracht, Schluesselmengen).
- **Symmetriekontrolle (Zusatz 3; vorab ableitbar, nur Kontrolle):**
  - (a) Operationen der Lagen: alle (R, t), R aus den 48 kubischen Punktoperationen, t im 1/8-Raster, die die Lagen samt
    Typ erhalten. Erwartet: 192 bei C15 (48 x 4 fcc), 48 bei A15.
  - (b) Unter wie vielen dieser Operationen ist die Tetraedermenge nicht invariant? Erwartet 0.
  - (c) Grundtempo: skalarer Graph-Laplace mit Einheitsgewichten (wie DANZER S), c^2 = kleinster Eigenwert / k^2, an den
    13 Richtungen. Richardson aus |k| = 1e-3 und 2e-3. Spanne (max c - min c)/Mittel c < 1e-6: isotrop. Dazu 48 Bilder
    einer allgemeinen Richtung (beschreibend).
  - (d) TT: omega^2/k^2 an den 48 Bildern einer allgemeinen Richtung gleich auf <= 1e-6.

## 3. Messgroesse [F]

- **Modell:** tg.modell und tg.punkt unveraendert, also das Hamilton-Netz von EINE-WELT-LOCH-1:
  - Regge-Steifigkeit B, Eck-Eichung M, skalare Regel c_v = -B w_v;
  - Bewegungsenergie A0 = (n_e . n_f)^2 - 1/2 je Tetraeder mit J = 1;
  - Reduktion R1.
  - Klassen wie TT-GLAS-1: masselos |omega^2| <= 30 eps^2; Luecke >= 100 eps^2; wachsend Re < -1e-12 s oder
    |Im| > 1e-12 s (s = groesstes |omega^2|).
- **Spanne wie TT-ISO-1 fuer V:** 13 Richtungen tti.richtungen13 ([100], [110], [111], [210], [211], [221], [310], [311],
  [320], [321], [322], [331], [332]), |k| = 1e-3 und 2e-3, je die zwei masselosen Werte omega^2/k^2.
  s = max/min - 1 ueber die 52 Werte.
- **Kontrollen:** derselbe Code auf Finns V (tg.netz_V) muss s(V) = 0,0633881 (TT-ISO-1) auf <= 1e-5 relativ geben.
  Ebenso S gegen 0,026847167 (beschreibend).
- **Regulaer (Plan):** an allen 26 Punkten
  - genau 2 masselose Moden, beide positiv;
  - 0 wachsend, 0 unklar;
  - reduzierte Bewegungsmatrix positiv definit, reduzierte Lagematrix ohne negative Richtung;
  - TT-Anteil >= 0,99 an [100], [110], [111] (|k| = 1e-3, beide Moden);
  - linear: omega^2/k^2 bei 2e-3 gegen 1e-3 auf <= 1e-2.
- **Stabilitaet bei kleinem k:** an den 26 Punkten (Regel). Beschreibend dazu die Klassen an 48 Bildern, 23
  ew-Richtungen, 91 Keil-Richtungen und 73 Pfad-Richtungen. Beschreibend ausserdem das Gitter L = 8 der kubischen Zelle
  (511 k), wie TT-ISO-1.
- **Zahl masseloser TT-Moden:** je Punkt gezaehlt.
- **Beschreibend:**
  - Spanne an den 23 ew-Richtungen und an 91 Richtungen im Keil (dichter);
  - Zerlegung: Richtungsspanne der Zweigmittel, groesste Aufspaltung der Polarisationen;
  - affine Regge-Steifigkeit (tg.affin, 13 Wuerfelachsen, |k| = 1e-2);
  - Superzelle 2 x 2 x 2 (Abschnitt 2).
- **Bild:** omega^2/k^2 beider Zweige relativ zum Mittel je Netz laengs [100] -> [110] -> [111] -> [100] (73 Richtungen,
  |k| = 1e-3), C15, A15 und V in einem Bild, auf der .69 erzeugt.

## 4. Urteilsregeln (mechanisch, dn.py auswertung)

- **DN0** (Plan = Kartenwortlaut), je Kristall an der Delaunay-Zerlegung. Eingetroffen, wenn fuer C15 und A15 alles gilt:
  - (a) "nur Tetraeder": 0 Tetraeder mit 5 oder mehr Punkten auf der Umkugel; 0 Punkte innen; kleinstes Volumen
    > 1e-9 des Mittels; Volumensumme auf 1e-12; jedes Dreieck in genau 2 Tetraedern; kein von Qhull ausgelassener
    Punkt.
  - (b) Jede Kante liegt in 5 oder 6 Tetraedern.
  - (c) |q - 5,1| <= 1e-9 (C15) bzw. |q - 46/9| <= 1e-9 (A15), q = 6T/E.
  - (d) C15: Die 6er-Kanten bilden das Diamantnetz der Mg: nur Mg-Mg; Grad 4 an jedem Mg; Menge = alle naechsten
    Mg-Mg-Paare; Vektoren (1/4)(+-1, +-1, +-1) mit Tetraederwinkeln; zwei sich abwechselnde Untergitter.
  - Sonst verfehlt.
- **DN1:**
  - Nach Plan: s(C15) < s(V) aus demselben Lauf; Kontrolle V bestanden und C15 regulaer, sonst nicht entscheidbar.
  - Nach Kartenwortlaut: s(C15) < 0,0634.
- **DN2:** nach Plan s(C15) < s(A15), beide regulaer (sonst nicht entscheidbar); nach Kartenwortlaut s(C15) < s(A15).
- **DN3:** nach Plan s(C15) < 0,03, C15 regulaer (sonst nicht entscheidbar); nach Kartenwortlaut s(C15) < 0,03.
- **Bauweg:** DN1 bis DN3 nehmen das Netz nach der Regel in Abschnitt 2. Bei Bau FK steht das an jedem Urteil.
- **Vorab-Vermerk:** Gilt C15 = S (L0), sind DN1 und DN3 vorab ableitbar (1.1). Das steht dann an beiden Urteilen.

## 5. Agenten-Vorhersagen (vor der Rechnung; kein Urteil)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | DN0 eingetroffen (keine Gleichstaende, Delaunay = FK in beiden Kristallen) | 90 % |
| A2 | Delaunay(C15) = S; s(C15) = 2,6847 % auf 1e-6 relativ | 90 % |
| A3 | A15 regulaer (2 masselose TT-Moden, stabil an den 26 Punkten und an den 511 k) | 75 % |
| A4 | s(A15) > s(C15), also DN2 eingetroffen | 55 % |
| A5 | s(A15) < s(V) | 50 % |

## 6. Laeufe (.69, kleintest.sh, Spuren cpu3 und cpu4, 1 Thread, <= 600 s)

- Arbeitsordner /home/fmh/fmhc-physics-remote/defekt-netz-1/ (code/ eingefroren, lauf/, rauch/).
- TAKT-UMKLAPP-1 laeuft auf cpu8 bis cpu10 (PLAN dort, Zusatz der Leitung). cpu3 und cpu4 waren um 07:51 CEST frei
  (kein Eintrag in /proc/locks). Vor jedem Start pruefe ich den Lock und belege keine Spur doppelt.
- Reihenfolge, DN0 zuerst:

| Lauf | Spur | Aufruf (code/dn.py ...) | erwartet |
|---|---|---|---|
| L0 | cpu3 | dn0 --out lauf/dn0.json | ~ 20 s |
| L1 | cpu3 | tt --netz C15 --dn0 lauf/dn0.json --out lauf/tt-C15.json | ~ 40 s |
| L2 | cpu4 | tt --netz A15 --dn0 lauf/dn0.json --out lauf/tt-A15.json (nach L0) | ~ 10 s |
| L3 | cpu4 | tt --netz V --out lauf/tt-V.json | ~ 5 s |
| L4 | cpu4 | tt --netz S --out lauf/tt-S.json | ~ 5 s |
| L5 | cpu3 | auswertung --dn0 lauf/dn0.json --tt lauf/tt-C15.json lauf/tt-A15.json lauf/tt-V.json lauf/tt-S.json --out lauf/auswertung.json | < 5 s |
| L6 | cpu3 | bild --tt lauf/tt-C15.json lauf/tt-A15.json lauf/tt-V.json --out lauf/bild-defekt-netz.json (PNG daneben) | < 5 s |
| L7 | cpu4 | dn0 --out lauf/dn0-wdh.json (Wiederholung, beschreibend; Vergleich ohne argv und Zeiten) | ~ 20 s |

- Schluss: kein neuer Lauf nach 09:25 CEST. Faellt ein Lauf aus, steht das im Ergebnis. Eine Codeaenderung danach ist
  eine Selbstanzeige mit neuer eingefrorener Fassung.

## 7. Rauchtests vor dem Einfrieren (.69 in UTC)

- r1 (cpu3, 05:59:51 bis 06:00:13): dn0 --rauch, 20,8 s, rc 0. Nur Schluessel.
- r2 (cpu4, erster Versuch 05:59:51): falsches Arbeitsverzeichnis meiner ssh-Zeile, Python fand code/dn.py nicht,
  rc 2. Wiederholt 06:00:24 bis 06:01:02: tt C15 --bauweg delaunay --rauch, 36,9 s, rc 0.
- r3 (cpu3, 06:00:24 bis 06:00:31): tt A15 --bauweg fk --rauch, 5,8 s, rc 0 (prueft den FK-Weg).
- r4 bis r10 (cpu3 und cpu4, 06:01:19 bis 06:02:06): die ganze Kette **ohne --rauch** nach rauch/v-*.json (dn0, tt
  C15, A15, V, S, auswertung, bild). Zweck: Absturzprobe von auswertung und bild vor dem Einfrieren. Laufzeiten 15,2;
  23,8; 3,0; 2,9; 2,0; 0,0; 0,9 s, alle rc 0. Gelesen: nur Rueckgabewerte, Laufzeiten und die Dateiliste. Werte und Bild
  habe ich nicht angesehen. Die Hauptlaeufe rechnen dasselbe deterministisch nach (Selbstanzeige im Ergebnis).
- Code seit r1 unveraendert (sha256 von code/dn.py auf der .69 und lokal gleich: 0cd5d13e...). Die Option --bauweg (nur
  fuer Rauchtests ohne dn0.json) war schon vor r1 eingebaut.
