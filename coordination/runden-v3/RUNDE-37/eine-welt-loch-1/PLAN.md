# EINE-WELT-LOCH-1: Plan (Code-Agent, Runde 41, explorativ nach v3)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 16:02:36 CEST; Plantext ab 16:18:39 CEST (date), vor jeder
  Rechnung. Zeitbox 150 min, also bis 18:32 CEST.
- Grundlage: KARTE.md (EW0 bis EW3; Wortlaut, Schwellen und Wahrscheinlichkeiten der Karte unveraendert).
- Werkzeug: TENSOR-EIS-PYRO-1, code/tp.py (sha256 419d7da6..., hier unveraendert als code/tp.py kopiert und nur
  importiert). Neuer Code: code/ew.py (allgemeiner Bloch-Baukasten fuer Regge-Netze), code/ew_auswertung.py (Urteile).
- Kennzeichen: [M] Mathematik (vorab ableitbar), [E] hier gerechnet, [P] Projektdatei, [F] eigene Festlegung,
  [H] Hypothese, [L] Literatur aus dem Gedaechtnis.
- Alle Rechnungen sind synthetische Gitterrechnungen, keine Messdaten.

## 1. Schreibtisch (vor jeder Rechnung)

### 1.1 Geometrie der Loecher [M]

- Wie TENSOR-EIS-PYRO-1: kubische Kante 1, fcc-Primitivvektoren a1 = (0,1,1)/2, a2 = (1,0,1)/2, a3 = (1,1,0)/2,
  r_0 = (1,1,1)/8, r_1 = (1,-1,-1)/8, r_2 = (-1,1,-1)/8, r_3 = (-1,-1,1)/8. Ecken P_a = R + r_a, Auf-Mitte U = R,
  Ab-Mitte D = R + 2 r_0, Kantenlaenge l_P = sqrt2/4.
- Je primitiver Zelle zwei Loecher (Stumpf-Tetraeder):
  - T1 mit Mitte C1 = R - 2 r_0. Seine vier Dreiecke teilt es mit den Auf-Tetraedern R + 2(r_a - r_0); seine 12 Ecken sind
    C1 + 2 r_a + r_b (a != b). Die 6 Kanten zwischen zwei Sechsecken sind Ab-Kanten.
  - T2 mit Mitte C2 = R + 4 r_0, gespiegelt: Dreiecke mit Ab-Tetraedern, Ecken C2 - 2 r_a - r_b.
  - Volumenprobe: 2 x 1/192 (Finns Tetraeder) + 2 x 23/192 (Loecher) = 1/4 = Zellvolumen.
- Sechsecke: je Zelle 4, Mitte H_a = C1 - r_a (Platz 16c), geteilt von T1 und dem T2 mit Mitte C1 - 2 r_a. Die
  Sechseckkanten wechseln Auf / Ab ab. Die Sechseckmitte ist ein Inversionszentrum, das Auf- und Ab-Kanten vertauscht.
- Folge fuer die Fuellung: Eine Zerlegung eines Sechsecks durch drei Diagonalen (Dreieck aus jeder zweiten Ecke)
  bricht diese Inversion und damit die Gleichberechtigung von Auf und Ab. Symmetrisch sind nur Zerlegungen mit der
  Sechseckmitte.
- Lage im Kopienbild von TENSOR-EIS-PYRO-1 [M]: C1 ist die Mitte eines Oktaeders der Kopie 1 und eines Gegentetraeders
  der Kopie 2, C2 umgekehrt. Die "Fuellzellen" von [F2] dort sitzen also genau in den Loechern.

### 1.2 Die zwei Fuellungen [F]

- **V (Standard, Karte):** Mittelpunkt C je Loch, verbunden mit seinen 12 Ecken; jedes Sechseck durch seine Mitte H in
  6 Dreiecke zerlegt; dazu die Kanten C-H. Zellen je Loch: 4 Kegel (C, Dreieck) und 24 Tetraeder (C, H, v_i, v_i+1).
  - Je Zelle: Ecken V = 10 (4 P, 2 C, 4 H), Kanten E = 68 (12 Finn, 24 C-Speichen, 24 H-Speichen, 8 C-H),
    Tetraeder T = 58 (2 Finn, 8 Kegel, 48 Sechsecktetraeder). Euler: 10 - 68 + 116 - 58 = 0.
- **S (kantenaermer, zweite Variante):** wie V, aber ohne Sechseckmitte; stattdessen die Achse C1-C2 durch die
  Sechseckmitte, und die Doppelpyramide ueber dem Sechseck in 6 Tetraeder (C1, C2, v_i, v_i+1) zerlegt.
  - Je Zelle: V = 6, E = 40 (12 Finn, 24 C-Speichen, 4 Achsen), T = 34. Euler: 6 - 40 + 68 - 34 = 0.
- Beide sind Triangulierungen des Raums mit voller Wuerfelsymmetrie (Fd-3m). Die neuen Kanten verbinden Ecken
  verschiedener Tetraeder nur ueber die Lochmitten (es gibt keine Diagonale P-P).
- Volumina (V): Finn 4/768, Kegel 5/768, Sechsecktetraeder 3/768. (S): Achsentetraeder 6/768. (Berichtigt vor 16:26:26 CEST (date direkt danach)
  nach der Volumenkontrolle im Rauchlauf r2: vorher stand "Kegel 20/768", Rechenfehler; die Summe 192/768 je Zelle
  gilt nur mit 5/768.)

### 1.3 Bauweise B1 auf dem gefuellten Netz [F, M]

- **Uebertragung [F]:**
  - Kantenwerte = Kantendehnungen a_e = delta l_e / l_e auf allen Kanten (Finn und neu).
  - Eichfreiheit an den Mitten aller Tetraeder, Finns und der neuen ("neue Simplizes entsprechend").
  - Jede Ecke folgt dem Mittel der Mitten der Tetraeder, zu denen sie gehoert. Ohne Fuellung ist das genau B1
    (jede Ecke P gehoert zu einem Auf- und einem Ab-Tetraeder).
- **Folge [M]:** Mit Fuellung gehoert P zu 32 (V) bzw. 20 (S) Tetraedern. Die Abbildung Mitten -> Ecken ist bei k = 0
  surjektiv: Ihre Transponierte ist injektiv, denn aus "Summe der y_v ueber jeden Tetraeder = 0" folgt mit Finns
  Tetraeder und den vier Kegeln eines Lochs y(P_a) = y(C) fuer alle a, also y = 0; die H folgen aus den
  Sechsecktetraedern.
  - Dann ist das Bild der B1-Eichung gleich dem Bild aller Eckverschiebungen: **Auf dem gefuellten Netz fallen B1 und A
    zusammen**; die Eichung ist die gewoehnliche Regge-Eichung (3 je Ecke).
  - Fuer k != 0 wird die Gleichheit der Bilder numerisch geprueft (Rang von M_B1, M_A und [M_B1, M_A]).
  - Damit gibt es nur noch **eine** Eichgruppe; das Entkopplungsargument von TENSOR-EIS-PYRO-1 (jede Ecke in genau zwei
    Tetraedern) entfaellt.
- **Kruemmung [F]:** linearisierter Regge-Kalkuel auf der Triangulierung selbst (alle Tetraeder),
  B_ef = l_e l_f Summe_t d theta_t,e / d l_f (komplexer Schritt und C^+ wie tp.py baue_zelle), also B = -l d eps/d l l.
  Dann gilt B M = 0 exakt (flache Einbettung) und B = B^dagger (Schlaefli). Keine Fuellzellen mehr noetig.
- **Skalare Regel [F]:** je Ecke v: Summe_{e an v} l_e eps_e (linearisierte Skalarkruemmung). Ohne Fuellung (alle Staebe
  gleich lang) ist das bis auf den Faktor LBAR die Regel von tp.py.
- **Bewegungsenergie [F]:** woertlich [F3] je Tetraeder, jetzt fuer alle Tetraeder: (1/2)[E^ij E^ij - (1/2)(E^ii)^2] mit
  E^ij = Summe_{e in t} E_e n_e n_e, also A = Summe_t P_t^dagger A0_t P_t, A0_t,ef = (n_e . n_f)^2 - 1/2, J = 1 fuer jeden
  Tetraeder. Gewicht: Die Stabilitaet (EW1 gegen EW3) kann an dieser Wahl haengen; die Zahl masseloser Moden nicht,
  solange A auf dem physikalischen Raum regulaer ist.
- **Ohne Fuellung (Kontrolle EW0):** derselbe Baukasten mit den zwei Kopien von TENSOR-EIS-PYRO-1: Ecken = Mitten der
  anderen Sorte, Staebe = verdoppelte Finn-Kanten, Regge-Zellen = Tetraeder-Oktaeder-Wabe, Bewegungsenergie nur auf
  Finns Tetraedern, skalare Regel je Mitte. Die Zellen werden allgemein aus Eckkoordinaten gebaut, nicht aus tp.py
  uebernommen.

### 1.4 Zaehlung je Zelle (ableitbar; im Code als Kontrolle) [M]

| Netz | Kanten E | Ecken V | Eichrang 3V | eichinvariant E - 3V | skalare Regeln V | physikalisch E - 4V |
|---|---|---|---|---|---|---|
| ohne Fuellung (B1, zwei Kopien) | 12 | 2 (Mitten) | 6 | 6 | 2 | 4 |
| V | 68 | 10 | 30 | 38 | 10 | 28 |
| S | 40 | 6 | 18 | 22 | 6 | 16 |

- Flache Richtungen von B bei k = 0 (Erwartung): Eichbild bei k = 0 (3V - 3) plus 6 gleichfoermige Dehnungen, also
  33 (V) bzw. 21 (S); bei kleinem k auf dem eichfreien Raum 3 Eigenwerte ~ k^2 (TT, TT, Spur), alle uebrigen ~ 1.
  Begruendung: Regge-flach heisst einbettbar, also Eckverschiebung oder gleichfoermige Dehnung.

### 1.5 Was vorab folgt und was nicht

- **Vorab [M, unter 1.3]:** Eine Eichgruppe und eine flache Einbettung lassen langwellig hoechstens ein glattes
  Metrikfeld zu, also hoechstens zwei masselose TT-Moden. **EW2 (vier) ist damit vorab fast ausgeschlossen**, sofern die
  Rang- und Kernproben aus 1.3 und 1.4 halten. Das ist eine Folge meiner Uebertragung [F]; eine Uebertragung mit zwei
  getrennten Eichgruppen (Ecken P nur an Finns Mitten) waere mit einem Regge-Potential auf dem gefuellten Netz nicht
  konsistent: Es ist auch unter allen Verschiebungen von P invariant, und die 6 Nicht-B1-Verschiebungen je Zelle waeren
  Nullmoden ohne Eichung.
- **Nicht vorab:** ob die Skalarregel den Spurmodus entfernt, ob die 26 (V) bzw. 14 (S) uebrigen Moden eine positive
  Luecke haben oder wachsen (Vorzeichen von A und B auf dem physikalischen Raum), das Tempo und seine
  Richtungsabhaengigkeit, der TT-Anteil.

## 2. Rechnung (code/ew.py)

- Gitter wie tp.py (fcc, BZ-Gitter L = 16 ohne k = 0, also 4 095 k). Bloch-Konvention: Amplitude einer Ecke bzw. Kante
  mit der Phase e^{i k . T} ihrer Gitterverschiebung T. Kanten aus den Tetraedern automatisch erzeugt und kanonisch
  benannt (Anfangsecke, Endecke, Gittervektor).
- **zaehlung (V und S, ohne Fuellung zum Vergleich):** E, V, T; Rang von M_A (Eckverschiebungen) und M_B1 (Mitten aller
  Tetraeder) und [M_A, M_B1] auf dem Gitter L = 8 und an 300 Zufalls-k (Schwelle 1e-9 relativ), bei k = 0; Rang der
  Skalarregeln modulo Bild M; Zahl flacher Eigenwerte von B (< 1e-10 relativ) bei k = 0; bei |k| = 1e-4 (23 Richtungen)
  die drei kleinsten Eigenwerte von B auf dem eichfreien Raum geteilt durch k^2 und der naechste; Kontrollen B
  hermitesch, B M, c M.
- **kontrolle (EW0):** ohne Fuellung, allgemeiner Baukasten:
  - Spektrum auf dem Gitter L = 16 und bei kleinem k wie tp.py spektrum_modell (23 Richtungen: [100], [110], [111] und
    20 Zufallsrichtungen aus default_rng(3), |k| = 1e-3 und 2e-3).
  - Vergleich mit TENSOR-EIS-PYRO-1 (ref/spektrum-tensor-eis-pyro-1.json, sha256 3c86c372...): positive Moden je k
    (pyro1 + pyro2) gegen meine Zahl je k; omega^2/k^2 je Richtung (4 Werte, sortiert) gegen die vier Werte von pyro1
    und pyro2.
  - Zusatz: Operatoren gegen tp.ops_pyro an 20 Zufalls-k (Spektren von B, A, Rang M, Bildwinkel).
- **spektrum (V und S):** physikalischer Raum S_phys = Komplement von Bild M_A + span c (SVD mit Rangschwelle 1e-9),
  omega^2 = Eigenwerte von (S^dagger A S)(S^dagger B S) wie tp.py.
  - Gitter L = 16: je k Zahl positiver, negativer, komplexer und naher Null-Werte (Schwelle 1e-9 relativ zu
    max|eig A_phys| max|eig B_phys| wie tp.py), Traegheit von A_phys und B_phys.
  - Kleines k: 23 Richtungen wie oben, |k| = eps in {1e-3, 2e-3}; alle omega^2; je Mode grobe Metrik H durch kleinste
    Quadrate a = (n_e^T H n_e e^{i k . m_e})_e + M xi (m_e Kantenmitte, Eichanteil xi frei), Restanteil, TT-Anteil wie
    tp.py tt_anteil. Die Eichspalten nehmen die Relativverschiebungen der Untergitter auf; der TT-Anteil ist unter
    glatter Eichung sym(k x xi) invariant. (Vor dem Einfrieren ergaenzt zwischen 16:26:26 und 16:29:10 CEST (date), ohne Kenntnis von Ergebnissen mit
    Fuellung: Ohne die Eichspalten haette die Projektion auf das Komplement des Eichbilds den Tensor je nach
    Wuerfel-Darstellung verschieden gestaucht und den TT-Anteil echter TT-Moden kuenstlich gesenkt.)
  - Beschreibend: Spur-Eichdefekt |(1 - P_M) A c_v| / |A c_v| (max, Median), freie Dynamik ohne Zwang (Eigenwerte von
    A B), Spektrum ohne Skalarregel (Komplement nur von Bild M).

## 3. Urteilsregeln (mechanisch in code/ew_auswertung.py)

**Klassen je Mode an einem Punkt (Richtung d, eps), s = max_j |omega^2_j| an diesem Punkt:**
- wachsend: Re omega^2 < -1e-9 s oder |Im omega^2| > 1e-9 s;
- masselos: nicht wachsend und |omega^2| <= 1e3 eps^2;
- Luecke: nicht wachsend, Re omega^2 >= 1e-4 s und Re omega^2 >= 2e3 eps^2;
- unklar: alles andere.
- (Vor dem Einfrieren geaendert zwischen 16:26:26 und 16:29:10 CEST (date), ohne Kenntnis von Ergebnissen mit Fuellung: vorher 1e-3 s und 1e4 eps^2.
  Grund: Eine echte, aber weiche Luecke unter 0,04 waere bei eps = 2e-3 "unklar" geworden. Dafuer neu die Bedingung,
  dass die Luecke nicht mit k waechst, siehe EW1 Punkt 3.)
- Eine masselose Mode heisst **masselose TT-Mode**, wenn Re omega^2 > 1e-9 s (positiv), TT-Anteil >= 0,99 und, nach
  Sortierung der masselosen Moden beider eps, |omega^2(2e-3)/(4 omega^2(1e-3)) - 1| <= 0,01 (linear).

**EW0** (Kontrolle ohne Fuellung): eingetroffen genau dann, wenn
1. an allen 4 095 Gitter-k die Zahl positiver Moden gleich der Summe pyro1 + pyro2 von TENSOR-EIS-PYRO-1 ist, und
2. fuer alle 23 Richtungen und beide eps max |omega^2/k^2 (neu) - omega^2/k^2 (alt)| <= 1e-8 (je vier Werte sortiert).
- Nach Plan = nach Kartenwortlaut.

**EW1** (Standard V): eingetroffen genau dann, wenn an allen 46 Punkten (23 Richtungen x 2 eps)
1. keine Mode wachsend oder unklar ist,
2. genau 2 Moden masselos sind und beide masselose TT-Moden sind,
3. alle uebrigen 26 Moden in der Klasse Luecke liegen und die Luecke konstant ist: kleinster Luecke-Wert bei eps = 2e-3
   geteilt durch den bei 1e-3 liegt je Richtung in [0,5; 2].
- Nach Plan = nach Kartenwortlaut ("eichinvariante Moden" = Moden auf der Zwangsflaeche wie TE2 in TENSOR-EIS-PYRO-1).

**EW2** (V): eingetroffen genau dann, wenn an allen 46 Punkten genau 4 masselose TT-Moden vorliegen. Nach Plan = nach
Kartenwortlaut.

**EW3** (V):
- **Nach Plan:** eingetroffen, wenn an mindestens einem der 46 Punkte eine Mode wachsend ist (Re < 0 oder komplex).
- **Nach Kartenwortlaut** ("omega^2 < 0 bei kleinem k"): eingetroffen, wenn an mindestens einem Punkt Re omega^2 < -1e-9 s
  fuer eine Mode gilt.

- Variante S wird mit denselben Regeln ausgewertet, aber nur beschreibend (kein Kartenurteil).
- Bricht ein Lauf ab oder ist A_phys an einem Punkt singulaer (Konditionszahl > 1e12), gilt das betroffene Urteil als
  "nicht entscheidbar".

## 4. Agenten-Vorhersagen (vorab; gehen in kein Kartenurteil ein)

| Nr | Vorhersage |
|---|---|
| Z1 | Rang M_A = Rang M_B1 = Rang [M_A, M_B1] = 30 (V) bzw. 18 (S) an allen k != 0; 27 bzw. 15 bei k = 0 |
| Z2 | Flache Eigenwerte von B bei k = 0: 33 (V), 21 (S); bei kleinem k genau 3 Eigenwerte ~ k^2 auf dem eichfreien Raum |
| Z3 | Physikalische Dimension 28 (V), 16 (S), 4 (ohne Fuellung) an allen Gitter-k |
| Z4 | EW0 eingetroffen, Tempo-Abweichung <= 1e-10 |
| V1 | Langwellig genau 2 masselose Moden (V und S), TT-Anteil >= 0,99 |
| V2 | Wachstum bei kleinem k (EW3 nach Plan) in V: 60 %; in S: 60 % |
| V3 | Tempo der masselosen Moden richtungsabhaengig (Spanne > 1 %) in V: 60 % |

## 5. Laeufe auf der .69 (kleintest.sh, Spuren cpu3, cpu4, sonst cpu5 und cpu)

| Lauf | Aufruf |
|---|---|
| ZA | ew.py zaehlung --out lauf/zaehlung.json |
| KO | ew.py kontrolle --ref ref/spektrum-tensor-eis-pyro-1.json --out lauf/kontrolle.json |
| SV | ew.py spektrum --fuellung V --L 16 --out lauf/spektrum-V.json |
| SS | ew.py spektrum --fuellung S --L 16 --out lauf/spektrum-S.json |
| AW | ew_auswertung.py --lauf lauf --out lauf/auswertung.json |

- Faellt SV an der 600-s-Grenze: L = 12 (vorab festgelegt); die Urteile haengen nur an den 46 Punkten bei kleinem k.

## 6. Rauchlaeufe vor dem Einfrieren (.69-Zeiten in UTC, CEST = UTC + 2)

- **r1** (ew.py 630f8c2b..., ew_auswertung.py ca0945a7...):
  - kontrolle (cpu3, 14:25:06 bis 14:25:10 UTC, rc 0, 4,0 s, 45 MB). Gelesen (EW0, erlaubt): positive Moden je k an
    allen 4 095 k gleich (Verteilung 2: 3 k, 4: 4 092 k, alt wie neu), Tempo-Abweichung max 4,3e-10; Gegenprobe gegen
    tp.ops_pyro: Spektren von B 1,5e-15, A 1,3e-15, omega^2 1,5e-15 relativ.
  - zaehlung klein (Lz = 4, 20 Zufalls-k; cpu4, 14:25:07 bis 14:25:11 UTC, rc 0). Gelesen nur: E, V, T wie 1.4
    (68/10/58, 40/6/34, 12/2/6); D symmetrisch <= 6,4e-16; l^T D <= 1,1e-15; Diedersumme je Kante 2 pi auf <= 1,8e-15;
    Volumensumme 0,25; Volumina 3/4/5 (V) bzw. 4/5/6 (S) mal 1/768; Kantenlaengen; B hermitesch, B M, c M <= 2,2e-15.
    Eine RuntimeWarning (0/0) in der Kontrollzeile k = 0 des Netzes ohne Fuellung (dort ist M bei k = 0 null).
  - spektrum V und S mit L = 4 (cpu3/cpu4, je rc 0; 7,5 s / 3,3 s; 63 / 49 MB): nur Zeiten, Speicher, Schluessel.
  - Auswertung auf r1: rc 0, nur Schluessel; Konsolenausgabe nicht gelesen.
- **Aenderungen nach r1**, ohne Kenntnis von Ergebnissen mit Fuellung: Tensor-Fit mit Eichspalten (Abschnitt 2),
  Lueckenschwellen und Konstanzbedingung (Abschnitt 3), Volumen-Tippfehler (1.2).
- **r2** (ew.py fa7b6417..., ew_auswertung.py 35cd9927...; cpu3, ab 14:29 UTC): ganze Kette klein (kontrolle,
  zaehlung Lz = 2, spektrum V und S mit L = 2, Auswertung), alle rc 0, keine Fehlermeldung. Gelesen: EW0 wieder gleich
  (Moden gleich, Tempo 4,3e-10), Schluessel der Auswertung.
- Laufzeit Hauptlaeufe geschaetzt aus r1 (L^3-Skalierung): SV etwa 50 s, SS etwa 20 s, ZA unter 60 s.
- Keine Schwelle und keine Urteilsregel wurde nach einem Befund mit Fuellung geaendert (es gab keinen gelesenen).
- **Leseregel (vor dem ersten Rauchlauf festgelegt, zwischen 16:21:40 und 16:24:59 CEST nach date):** Im Rauchlauf lese ich nur Rueckgabewerte, Zeiten,
  Speicher, JSON-Schluessel, die EW0-Kontrolle (ohne Fuellung) und die technischen Identitaeten der Netze mit Fuellung
  (Zellzahl, D symmetrisch, l^T D = 0, Diedersumme 2 pi, Volumensumme, B hermitesch, B M, c M). Keine Raenge,
  flachen Eigenwerte, Modenzahlen, omega^2, TT-Anteile oder Urteile mit Fuellung. Die Konsolenausgabe der Auswertung
  (sie nennt Urteile) geht im Rauchlauf in eine Datei, die ich nicht lese.
