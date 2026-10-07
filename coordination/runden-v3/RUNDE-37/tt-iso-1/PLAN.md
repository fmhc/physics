# TT-ISO-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 43)

- Start 2026-10-04 21:53:38 CEST (date). Plantext ab 22:12:37 CEST (date), vor jedem TT-Wert neuer Gewichte.
- Bisher gesehen: nur alte Zahlen aus EINE-WELT-LOCH-1 (ERGEBNIS, kinetik.json) und im Rauchtest r1 bis r4 nur
  Laufzeiten und Schluessel (rauch-69/, Option --rauch). Kein TT-Wert mit neuen Gewichten.
- Kennzeichen: [M] eigene Mathematik bzw. Codelesung, [P] Projektdatei, [L] Gedaechtnis, [H] Hypothese, [F] Festlegung.
- Code: code/ew.py, ew_auswertung.py, nachtrag_kinetik.py, tp.py unveraendert kopiert (sha256 wie EINE-WELT-LOCH-1:
  fa7b6417..., 35cd9927..., fd0d17b9..., 419d7da6...). Neu: code/tti.py.

## 0. Rohdatenprobe (kinetik.json, per jq vor dem Plan)

- Oberste Schluessel: S, V, info, laufzeit_s, maxrss_MB, ohne. Je Netz: gitter (L, nk, traegheit_verteilung, w2_min)
  und klein (6 Eintraege: richtung, eps, A{1,2,3}_R{1,2}_w2_masselos_ueber_k2, ..._negativ, ..._kleinster_rest, Traegheiten
  A{1,2,3}_R1, _R2inv, _voll, A3_K_voll, B_phys). Traegheiten als neg/null-Zaehlungen (z. B. neg0_null0).
- Nur 3 Richtungen ([100], [110], [111]) x 2 eps, fuenf feste Varianten, keine Gewichtsabtastung [P].
- Spannen der festen Varianten (max/min - 1 ueber diese 6 Punkte, von Hand aus den Zahlen): V A1R1 6,34 %,
  A2R1 5,92 %, A3R2 3,18 %; S A1R1 2,68 %, A2R1 6,41 %, A3R2 0,30 % [P]. (Zahlen der Karte: 6,2 % ist
  (max - min)/Mittel, nicht max/min - 1; s. TB0.)
- Auffaellig: A3R2 V in [100] fast entartet (0,0051770 / 0,0052083), der Wert 0,0052083 = 1/192 kehrt in mehreren
  Varianten wieder [P].

## 1. Ableitbarkeitsprobe (Schreibtisch)

### 1.1 Punktgruppe des gefuellten Netzes [M, Codelesung ew.geometrie]

- V und S mit J = 1, g = 1: Raumgruppe Fd-3m, Punktgruppe O_h (m-3m). Jedes Loch (Stumpf-Tetraeder) ist um seine
  Mitte T_d-symmetrisch gefuellt (C mit 12 Speichen; Sechseck um H in 6 Kegel bzw. um die Achse C1-C2 in 6 Tetraeder
  zerlegt). Die Sechseckmitte ist Inversionszentrum (vertauscht T1 und T2, Auf und Ab). Das deckt sich mit
  EINE-WELT-LOCH-1, Abschnitt 3 [P].
- Gewichte je Code-Art: Ungleiche Gewichte fuer finn_auf/finn_ab oder T1/T2 brechen die Inversion; es bleibt F-43m,
  Punktgruppe T_d, **weiter kubisch**. Weil alle Operatoren im Ortsraum reell sind, gilt B(-k) = conj B(k) (ebenso A, M,
  c); das Spektrum ist gerade in k. Fuer gerade Funktionen von n sind T_d und O_h gleichwertig. Also hat omega^2(n)
  fuer **jede** Wahl der Gewichte je Art und je Kantenart die volle m-3m-Form [M].
- Feinheit: Die Code-Arten sind nicht die feinsten Bahnen. Die sechs Kegel um ein Sechseck (V, 'sechs_T1') und die
  sechs Achsen-Tetraeder (S, 'achse') liegen auf Sechseckkanten, die abwechselnd an Dreiecke von T1 und von T2 grenzen;
  unter F-43m sind das je zwei Bahnen. Gewichte je Code-Art brechen also keine Symmetrie, sind aber groeber als moeglich
  [M]. Die Karte verlangt Arten nach dem Code; dabei bleibt es.
- Kontrolle im Lauf (Kontrolle d): omega^2/k^2 an den 48 Bildern einer allgemeinen Richtung, mit J = 1 und mit
  zufaelligen J und g (Saat 5); erwartet gleich bis auf Rundung.

### 1.2 Pruefung der Symmetriezaehlung der Leitung (Karte, [M, ungeprueft])

| Satz der Karte | Urteil | Begruendung [M] |
|---|---|---|
| spurfreie Polarisationen = Eg + T2g | **stimmt** | Sym2 spurfrei = 5 = Eg (2) + T2g (3) |
| jede kubische Bewegungsenergie wirkt nur ueber m_E, m_T; fuer die Tempi zaehlt nur m_E/m_T | **stimmt so nicht** | Das gilt fuer eine feste Form auf den 5 spurfreien Verzerrungen. Hier wirkt A auf alle 68 (V) bzw. 40 (S) Kanten, und die TT-Moden leben auf der Zwangsflaeche. Fuer R1 gilt exakt (S^+ A S)^-1 = S^+ (K - K N (N^+ K N)^-1 N^+ K) S mit K = A^-1 und N = Bild [M, c]: die TT-Masse ist die Lagrange-Form K, minimiert ueber Eichung und Regelrichtungen. Bei k -> 0 enthalten diese die von n abhaengigen Laengsrichtungen sym(n x xi) und eine Spur-Richtung. Kreuzterme mit dem Laengs- und Spuranteil gehen mit (m_E - m_T) bzw. mit dem entsprechenden Kreuzgewicht ein; die effektive TT-Masse ist eine rationale Funktion von n mit mehr als einem Verhaeltnis. Fuer R2 aehnlich (Euklidischer Vertreter statt Minimum). |
| Gradientenenergie: kubisch 9, isotrop 4 Invarianten | **Zahl stimmt** | Sym2(V) x Sym2(Sym2 V): (A1+E+T2) x (3A1+3E+T1+3T2) gibt 3+3+3 = 9; SO(3): (L0+L2) x (2L0+2L2+L4) gibt 4 |
| also mehrere Bedingungen, ein Verhaeltnis erfuellt generisch hoechstens eine | **fuer ein Verhaeltnis richtig, hier nicht anwendbar** | Die Bewegungsgewichte wirken gar nicht auf die Gradientenenergie (B und Zwangsflaeche haengen nicht von J ab). Und der Code hat 6 Arten in V (5 freie Verhaeltnisse), 5 in S (4); mit Fd-3m-Symmetrie 3 (2 Verhaeltnisse). |

- **Meine Zaehlung [M, mit H]:** Ist die Steifigkeit der TT-Welle isotrop (lineare Regge-Wirkung -> Einstein-Hilbert,
  Rocek/Williams [L] fuer das hyperkubische Netz; fuer dieses Netz [H]), dann verlangt Isotropie nur eine isotrope
  effektive TT-Masse. Dafuer reichen generisch zwei Bedingungen (gleiche E- und T2-Gewichte der reduzierten Lagrange-Form
  und des Kreuzterms mit der Spur-Richtung). Zwei oder mehr freie Verhaeltnisse koennen das generisch an isolierten
  Punkten erfuellen, ob im positiven Bereich und stabil, ist offen.
- **Folgerung:** Die Richtung von TB1 ("generisch nicht isotrop") folgt **nicht** aus der Symmetrie; die Begruendung
  der Karte traegt nur fuer ein einzelnes Verhaeltnis. TB1 und TB2 sind nicht vorab ableitbar. Gerechnet wird beides.
- Beschreibende Kontrolle dazu (Kontrolle e): Steifigkeit der affinen TT-Welle a_e = (n_e^T h n_e) e^{i k.m_e},
  K(n) = a^+ B a / k^2 auf TT(n), an 13 Richtungen (V, S, ohne). Ist sie isotrop, liegt die ganze Anisotropie in der
  Masse.

### 1.3 Weitere Ableitungen vorab [M]

- **A2R1 ist dieselbe Familie wie A1R1:** A2 = A1 mit J_t -> J_t V_F/V_t (V: Kegel 4/5, Sechseck 4/3; S: Kegel 4/5,
  Achse 4/6). Mit freien J ist A2R1 ein verschobenes Gitter von A1R1. Die kleinste Spanne muss bis auf Randeffekte des
  Bereichs gleich sein. Gerechnet wird A2R1 trotzdem (Karte); der Vergleich ist eine Kontrolle.
- **Skaleninvarianz:** Gemeinsame Skalierung aller J aendert omega^2 um einen Faktor, die Spanne nicht. Deshalb ist eine
  Art Referenz (finn_auf = 1), die uebrigen laufen frei. Ebenso fuer g (Referenz pyro = 1; c_v -> lambda c_v aendert
  die Zwangsflaeche nicht).
- **TB0 nach Kartenwortlaut** ist teilweise vorab entschieden: Mit der Kartendefinition max/min - 1 gibt der Hauptlauf
  0,12643/0,11889 - 1 = 6,34 %, nicht 6,2 % auf 1e-3; die 6,2 % sind (max - min)/Mittel [P]. Gerechnet wird beides.

## 2. Messgroesse und Verfahren [F]

- **Richtungen (13):** [100], [110], [111], [210], [211], [221], [310], [311], [320], [321], [322], [331], [332]
  (alle im irreduziblen Keil; wegen 1.1 genuegt der Keil). Zusaetzlich fuer die Bestwahlen beschreibend die 23
  Richtungen von ew.richtungen() (Hauptlauf).
- **|k|:** 1e-3 und 2e-3; 26 k-Punkte.
- **omega^2:** Zwangsflaeche wie ew (S = Komplement von Bild [M, c_g]); B_red = S^+ B S = L L^+ (Cholesky);
  1/omega^2 = Eigenwerte von Z = L^-1 A_red^-1 L^-+ (A1R1, A2R1: A_red = S^+ A S; A3R2: Z = L^-1 (S^+ K S) L^-+).
  Die zwei betragsgroessten Eigenwerte von Z sind die masselosen Moden (gut konditioniert, statt kleiner Eigenwerte).
- **Spanne(J, g)** = max/min - 1 ueber alle 52 Werte omega^2/k^2 (13 Richtungen x 2 Zweige x 2 |k|).
- **Gueltig nach Plan:** an allen 26 k-Punkten B_red positiv definit, die zwei masselosen Werte positiv, Luecke
  |ev_3|/|ev_2| < 1e-2 (masselos klar getrennt), und keine negative Mode an diesen 26 Punkten (Traegheit von Z).
  **Gueltig nach Wortlaut:** wie Plan, aber negative Moden an den 26 Punkten erlaubt (nur Gitter).
- **Gewichte J:** je Code-Art. V: finn_ab, finn_auf (Referenz), kegel_T1, kegel_T2, sechs_T1, sechs_T2;
  S: achse, finn_ab, finn_auf (Referenz), kegel_T1, kegel_T2. J_t = 10^x_t, x_t in [-2, 2] (je Gewicht 1e-2 bis 1e2
  relativ zur Referenz).
- **Gitter (TB1):** 9 Punkte je Achse (halbe Dekade), V 9^5 = 59 049, S 9^4 = 6 561 Gewichtssaetze je Paarung.
  Die Fd-3m-symmetrische Teilmenge (finn_ab = 1, T1 = T2) wird getrennt ausgewiesen.
- **Verfeinerung (TB1):** Nelder-Mead in x (Kasten [-2, 2]) aus den 4 besten Gitterpunkten (Plan-gueltig), Schritt 0,25,
  dann Neustart mit 0,05; Zielgroesse Spanne (ungueltig = 1e3). Ebenso im symmetrischen Unterraum (2 Verhaeltnisse:
  Kegel, Sechseck bzw. Achse). Maxit 250/200 je Phase (Faktor --nmfaktor 0,67 im Lauf, s. 5).
- **TB2 (Regelgewicht):** g je Kantenart, c_v = - B w_v^g mit (w_v^g)_e = g(e) an v (g = 1 ist ew). V: pyro (Referenz),
  c_speiche, ch, h_speiche; S: pyro (Referenz), achse, c_speiche. g = 10^y, y in [-2, 2]. Gitter 5 Punkte je Achse
  (V 125, S 25) bei J = TB1-Bestwahl, dann gemeinsamer Nelder-Mead ueber (x, y) aus den 2 besten g-Gitterpunkten und aus
  g = 1, Schritt 0,25 dann 0,05.
- **Bestwahl-Pruefung** (TB1 alle Arten, TB1 symmetrisch, TB2), je Paarung und Netz:
  - Spanne an den 13 und an den 23 ew-Richtungen;
  - TT-Anteil der zwei masselosen Moden an [100], [110], [111] (|k| = 1e-3; ew.tensor_fit, tp.tt_anteil), dazu
    omega^2 per eig(A_red B_red) wie ew als Gegenrechnung;
  - Stabilitaet: alle 511 k des Gitters L = 8 (ohne k = 0), Zahl der k mit Re omega^2 < -1e-9 s oder |Im| > 1e-9 s
    (s = groesstes |omega^2| an diesem k), dazu Zahl der k mit B_red bzw. A_red (K_red) nicht positiv definit.
- **Netze:** V Hauptergebnis; S beschreibend mit demselben Ablauf.

## 3. Kontrollen (Lauf "kontrolle", vor den Abtastungen)

- a) J = 1, g = 1: drei Paarungen, V und S, an [100], [110], [111] x 2 eps gegen kinetik.json (relative Abweichung).
- b) V A1R1, J = 1, 23 ew-Richtungen: [100]-Werte, Spanne in beiden Definitionen.
- c) ohne Fuellung, A1R1, 13 Richtungen x 2 eps: alle vier masselosen Werte gegen 0,25.
- d) Symmetrie, 48 Bilder (1.1).
- e) Steifigkeit der affinen TT-Welle (1.2), beschreibend.
- Die Gleichheit von c_gew mit g = 1 und ew.ops (c) ist im Code bitgleich angelegt (gleiche Rechenschritte); geprueft
  wird sie ueber a).

## 4. Vorhersagen und Urteilsregeln (Karte unveraendert; Regeln hier vor jeder Rechnung)

| Nr | Karte | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| TB0 | A1-R1 (V) gibt in [100] wieder 0,1189 / 0,1264 und die Spanne 6,2 % auf 1e-3 relativ; ohne Fuellung (R1) isotrop 0,25 (90 %) | **eingetroffen**, wenn alle: (i) [100] (eps 1e-3) beide Werte auf <= 1e-3 relativ an 0,11889 / 0,12643; (ii) Spanne (max - min)/Mittel an den 23 ew-Richtungen in [6,15; 6,25) %; (iii) ohne: alle Werte an 13 Richtungen x 2 eps mit \|w - 0,25\| <= 2,5e-4; (iv) Nachtragsvarianten A2R1 und A3R2 (V, S) an den 6 Punkten auf <= 1e-3 relativ. Sonst verfehlt. | wie Plan, aber (ii) mit der Kartendefinition max/min - 1: \|Spanne - 6,2 %\| <= 1e-3 x 6,2 %. Nach 1.3 vorab: verfehlt (6,34 %). |
| TB1 | [H] ueber alle Bewegungsgewichte im Plan-Bereich bleibt die kleinste TT-Spanne in V bei jeder der drei Paarungen ueber 1 % (70 %) | **eingetroffen**, wenn fuer jede Paarung (A1R1, A2R1, A3R2) in V die kleinste Plan-gueltige Spanne (Gitter und Verfeinerung, alle Code-Arten frei) > 1 % ist; **verfehlt**, wenn bei mindestens einer <= 1 %. Ohne Plan-gueltigen Punkt bei einer Paarung: nicht entscheidbar. | wie Plan, aber Minimum ueber Plan-gueltige Verfeinerung und Wortlaut-gueltige Gitterpunkte (negative Moden an den 26 Punkten erlaubt). |
| TB2 | [H] mit zusaetzlich freiem Gewicht der skalaren Regel sinkt die kleinste Spanne in V unter 0,1 %, ohne negative Mode an den 511 k (20 %) | **eingetroffen**, wenn bei mindestens einer Paarung in V die TB2-Bestwahl Spanne < 0,1 % hat und an den 511 k keine Mode mit Re omega^2 < 0 oder komplexem omega^2. Sonst verfehlt. Fehlt der TB2-Lauf: nicht entscheidbar. | eingetroffen, wenn die ueber alle Paarungen kleinste TB2-Spanne in V < 0,1 % ist und genau diese Wahl an den 511 k keine negative Mode hat. |

- Zusatz (geht in kein Urteil ein): S beschreibend; symmetrischer Unterraum beschreibend; Steifigkeitsprobe beschreibend.
- Agenten-Erwartung (vor der Rechnung, nicht urteilsrelevant) [H]: Nach 1.2 halte ich Isotropie mit freien J fuer
  moeglich. TB1 trifft ein: 40 %. TB2 trifft ein (unter 0,1 %, stabil): 35 %.

## 5. Laeufe, Laufzeit, Abbruchregeln

- **Rauchtests (vor dem Einfrieren, nur Schluessel und Laufzeiten):** r1 Gitter V A1R1 mit 3 Punkten je Achse: 243
  Saetze in 1,44 s (5,9 ms je Satz); r3 Gitter V A3R2: 2,9 ms je Satz; r2 Verfeinerung V A1R1 (Faktor 0,04, L = 2):
  12 ms je TB1-Auswertung, 114 ms je TB2-Auswertung (neue Zwangsflaeche); r4 Kontrolle 7,5 s.
- **Schaetzung:** Gitter V A1R1 und A2R1 je ~350 s, V A3R2 ~170 s, S je ~20 bis 40 s; Verfeinerung V mit
  --nmfaktor 0,67 ~250 s, S ~150 s; Kontrolle ~10 s. Zusammen ~35 min Rechenzeit auf 2 Spuren, ~20 min Wandzeit.
- **Spuren:** cpu3: kontrolle, V-A1R1 (Gitter, Verfeinerung), S-A1R1, S-A2R1; cpu5: V-A3R2, V-A2R1, S-A3R2. Je Lauf
  ueber kleintest.sh (<= 600 s, 1 Thread). Einmalige Laufkette je Spur (lauf-69/kette-*.sh), kein Dienst.
- **Abbruchregeln:**
  - Kein neuer Lauf nach SCHLUSS = 2026-10-04 23:00:00 CEST (21:00:00 UTC); die Kette prueft das vor jedem Lauf.
  - Die Optimierung bricht zeitgesteuert ab (Prozessstart + 150 s TB1, + 200 s symmetrisch, + 470 s TB2) und liefert
    den bis dahin besten Wert; gezaehlt in zeitabbruch_nm. Ein Zeitabbruch heisst: Minimum nicht konvergiert; das
    Urteil nimmt den erreichten Wert (fuer TB1 "> 1 %" damit nur vorlaeufig, fuer TB2 "< 0,1 %" unberuehrt).
  - Scheitert ein Gitterlauf an der Laufzeitgrenze, wird er nicht wiederholt; das Urteil fuer diese Paarung ist
    "nicht entscheidbar" (keine Nachbesserung im Plan).
  - Scheitert eine Verfeinerung, urteilt TB1 fuer diese Paarung nur mit dem Gitter (gekennzeichnet), TB2 ist dann nicht
    entscheidbar.
- **Auswertung:** mechanisch aus den JSON-Dateien des eingefrorenen tti.py (jq zum Lesen; keine lokale Rechnung);
  Quotienten fuer den Bericht liefert tti.py selbst.
