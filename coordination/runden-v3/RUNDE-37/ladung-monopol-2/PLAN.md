# LADUNG-MONOPOL-2: Plan (Code-Agent, Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 06:50:49 CEST, Plantext ab 07:14:49 CEST (date). Die .69
  laeuft in UTC (CEST = UTC + 2).
- Gelesen vor dem Plan: KARTE.md; LADUNG-MONOPOL-1 (PLAN, ERGEBNIS, code/); FLUSS-1 (KARTE, ERGEBNIS, code/gitter.py,
  code/gitter_fluss.py); Dossier LADUNG-MONOPOL-L Abschnitte 5 und 9.
- **Kennzeichen:** [M] eigene Mathematik (Schreibtisch), [F] Festlegung dieses Plans (von der Karte offen gelassen),
  [K] Kartenberichtigung, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese, [E] gerechnet (nur im
  Rauchlauf-Abschnitt 8).
- Alles ist eine synthetische Einteilchen-Gitterrechnung, keine Messdaten.

## 1. Konstruktion

### 1.1 Gitter [F]

- Koordinaten ganzzahlig in 1/8 der kubischen Zellkante, relativ zur Mitte des Monopol-Tetraeders (ein "oberer"
  Tetraeder; seine Ecken liegen bei -(1,1,1), -(1,-1,-1), -(-1,1,-1), -(-1,-1,1)). Alle Ecken haben ungerade
  Koordinaten. Kantenlaenge a = sqrt(8) (= sqrt(2)/4 Zellkanten, wie FLUSS-1 Netz A).
- Knoten: Pyrochlor-Ecken (fcc + Basis aus FLUSS-1/EIS-1). Kanten: alle Eckpaare im Abstand a (genau die
  Tetraederkanten, Grad 6 im Inneren).
- **Box [F]:** Wuerfel der Kante L Zellen, **zentriert auf die Monopolmitte** (|x_i| <= 4 L). So bleibt die Drehgruppe
  der Tetraedermitte exakt erhalten (die Karte sagt "nahe der Mitte"; ich lege den Monopol genau in die Mitte). Etwa
  16 L^3 Ecken (L = 4: 1024, L = 8: 8192).
- **L-Raster [F, "nach Laufzeit"]:** L in {4, 6, 8}. Halbe Boxbreite 5,7 bis 11,3 Kantenlaengen, vergleichbar mit
  LADUNG-MONOPOL-1 (L = 16 und 24: 8 bis 12). L = 3 (Halbbreite 4,2 a) waere kaum groesser als der Kernradius 3 a.
  Zeitprobe L = 8: 1,4 s je Punkt (Abschnitt 8).

### 1.2 Zellkomplex

- **Flaechen:** Dreiecke der Tetraeder (alle 3 Ecken in der Box) und Kagome-Sechsecke (alle 6 Ecken in der Box).
  - Sechsecke werden gefunden ueber Ecke i und zwei Nachbarn j, k aus verschiedenen Tetraedern unter 120 Grad; Mitte
    x_j + x_k - x_i, Normale vom Typ (+-1,+-1,+-1), die 6 Ecken sind Mitte + die 6 Nachbarvektoren senkrecht zur Normale.
  - Orientierung: Dreiecke nach aussen aus ihrem Tetraeder; Sechsecke entlang ihrer Normale (erste Komponente > 0).
- **Zellen:** Tetraeder (4 Ecken in der Box) und abgestumpfte Tetraeder (alle 8 Flaechen in der Box).
  - Lage der Nachbarzellen einer Flaeche [M]: Dreieck mit Schwerpunkt s und Aussennormale n (Typ (+-1,+-1,+-1)):
    Tetraeder bei s - n/3, Stumpftetraeder bei s + 5 n/3. Sechseck mit Mitte c: Stumpftetraeder bei c +- n.
  - Abstand Mitte-Ecke: Tetraeder sqrt3, Stumpftetraeder sqrt11 (Umkugel; Code prueft beides).
- **Pruefungen (Code, je L):**
  - Euler-Bilanz V - E + F - Z = 1 (offene, konvexe Box ist zusammenziehbar; bei b2 = 0 heisst das b1 = 0, also wird
    jeder Kreis des Graphen von Flaechen berandet und lsqr legt jede Wilson-Schleife fest).
  - Rand jeder Zelle geschlossen (Summe der orientierten Randkanten = 0); Ecken jeder Zelle auf der Umkugel, Zahl 4
    bzw. 12.
  - Inzidenz: jede Flaeche, deren Mitte mindestens eine Zellkante vom Boxrand entfernt liegt, liegt in genau zwei
    vollen Zellen. Kanten in 2 bis 4 Flaechen (innen 4: 2 Dreiecke + 2 Sechsecke).
  - Ebenheit der Sechsecke (groesster Abstand einer Ecke von der Mittelebene).
  - Zusammenhang, Grad hoechstens 6.

### 1.3 Fluss und Eichfeld

- Phi_f = Omega_f/2, Omega_f vorzeichenbehafteter Raumwinkel vom Monopol (Van Oosterom-Strackee wie LADUNG-MONOPOL-1).
  Sechsecke als feste Faecherflaeche (Schwerpunkt + 6 Dreiecke), fuer beide anliegenden Zellen dieselbe (die Flaeche
  ist eine einzige Zeile der Inzidenzmatrix).
- Pruefung (Karte): Auswaertssumme ueber jede volle Zelle <= 1e-12, Monopolzelle 2 pi +- 1e-12. Monopol-Dreiecke je
  pi/2.
- **Dirac-String [F]:** gieriger Weg durch volle Zellen vom Monopol-Tetraeder bis zu einer Randflaeche: in jeder Zelle
  die noch nicht benutzte Flaeche mit der groessten Projektion auf eine Richtung d. n_f = +1, wenn die Normale aus der
  verlassenen Zelle zeigt, sonst -1. F = Phi - 2 pi n ist dann in jeder vollen Zelle quellenfrei (Code: "schliessung").
  - Drei Richtungen: s1 = (1; 0,31; 0,17) (Hauptstring), s2 = (-0,23; 1; 0,41), s3 = (0,37; -0,53; -1); absichtlich
    schief, damit keine Gleichstaende auftreten.
- A aus rot A = F per lsqr (atol = btol = 1e-15, bis zu 3 Nachbesserungen), Rest max_f |(DA - F)_f| <= 1e-10.
- Hamilton: H = -sum (e^{i q A_ij} c_i^+ c_j + h.c.) - V0 sum_{4 Kernecken} n_i, q in {0, 1, 2}.

### 1.4 Symmetrie: magnetische Drehungen und Phasenwahl

- **[M, K1] Die unitaere Symmetrie ist nur die Drehgruppe T (Ordnung 12), nicht T_d.**
  - Eine Spiegelung kehrt jeden orientierten Raumwinkel um: P_sigma H P_sigma^-1 ist der Hamilton zur Ladung -q.
  - Spiegelungen und S4 sind nur zusammen mit komplexer Konjugation Symmetrien (antiunitaer).
  - Gerechnet wird darum mit der Doppelgruppe 2T (binaere Tetraedergruppe, Ordnung 24): Spinor-Darstellungen G4, G5,
    G6, alle 2-dimensional.
- **Operatoren:** U_R = D_g P_R wie LADUNG-MONOPOL-1, mit (P_R v)(x) = v(R^-1 x) und g aus g_i conj(g_j) = K_ij / K^R_ij
  (Breitensuche, dann Defekt auf allen Kanten <= 1e-10).
  - Rx, Ry: pi um x bzw. y durch die Tetraedermitte.
  - C3: 2 pi/3 um (1,1,1); die Achse geht durch die Kernecke -(1,1,1).
  - Antiunitaer: A = D_h P_sigma K mit sigma: x <-> y (Spiegelebene durch die (1,1,1)-Achse) und K komplexe
    Konjugation; h aus K_ij / (P_sigma K* P_sigma^T)_ij.
- **Kommutatorzeichen** wie LADUNG-MONOPOL-1: C = U_x U_y U_x^-1 U_y^-1, als Operator (Zufallsvektor) und als
  s = Tr(P C P)/m je Stufe. Herleitung s = (-1)^q wie dort [M]: Die Schleife der beiden pi-Drehungen umschliesst die
  halbe Kugel. Die Karte nennt das selbst ableitbar.
- **Phasenwahl fuer C3 (Karte: offenlegen) [F, M]:**
  - g ist nur bis auf eine globale Phase bestimmt. Diese Mehrdeutigkeit vertauscht G4, G5 und G6 zyklisch (Tensor mit
    den 1-dim Darstellungen von T).
  - Die Phase von g an einer Fixecke der Drehung ist eichinvariant. Fixecken auf der C3-Achse liegen bei t (1,1,1),
    t = ..., -9, -1, 7, 15, ...
  - Kontinuum [M]: Im Nordeichmass ist J_z = -i d_phi - e g; daraus folgt U = e^{i theta e g} P_R am Nordpol und
    e^{-i theta e g} am Suedpol. Das Produkt der Phasen an zwei gegenueberliegenden Fixpunkten ist also 1.
  - **Festlegung:** Produkt der Phasen an den innersten Fixecken beiderseits (t = -1 und t = 7) gleich 1, dazu
    U_C3^3 = (-1)^q. Das ist eindeutig.
  - Erwartung [M]: g(t = -1) = e^{+i q pi/3} (Hand-Rechnung am K4, Abschnitt 2, mit der Kopplung e^{i q A_{i->j}} an
    c_i^+ c_j). Das Verhaeltnis g(-)/g(+) = e^{i q 2 pi/3} ist eichinvariant, also eine echte Pruefung.
- **Darstellung einer Stufe [F]:** Eigenwerte von V^+ U_C3 V (physikalische Phase).
  - q ungerade: G4 = {e^{i pi/3}, e^{-i pi/3}} (j = 1/2-artig), G5 = {-1, e^{i pi/3}}, G6 = {-1, e^{-i pi/3}}; G5 + G6 ist
    das j = 3/2-Quartett. Zerlegung aus den Zaehlungen (n4, n5, n6).
  - q gerade: A = {1}, E1 = {omega}, E2 = {omega^2}, T = {1, omega, omega^2}; T gegen A + E1 + E2 per |chi(Rx)| = 1
    gegen 3.
  - In der Sprache der Karte: G4 entspricht E_1/2 oder E_5/2 (beide werden in 2T zu G4), G5 + G6 entspricht F_3/2.
- **Vervollstaendigung** wie LADUNG-MONOPOL-1 (Abschluss jeder eigsh-Stufe unter Rx, Ry, C3 und zusaetzlich der
  antiunitaeren Operation, Rayleigh-Ritz, Residuum <= 1e-6). Symmetrie-Rest je Stufe ueber alle vier Operationen,
  Grenze 1e-6.

## 2. Schreibtisch vor jeder Rechnung: tiefer Topf (K4) [M]

- Fuer V0 -> unendlich sitzen die tiefsten Zustaende auf den 4 Kernecken (K4). Jedes Dreieck traegt den Fluss
  q Omega/2 = q pi/2 (Omega = 4 pi/4).
- Eichmass A_1j = 0, A_23 = A_34 = -phi, A_24 = +phi mit phi = q pi/2. Gerechnet von Hand:
  - q = 1: T^2 = 3 (die Zweischritt-Wege heben sich weg). Spektrum -sqrt3 (2), +sqrt3 (2).
  - q = 2: T + 1 ist eine Hadamard-Matrix. Spektrum -1 (3), +3 (1).
  - q = 0: -3 (1), +1 (3).
- **Darstellungen [M]:** P_C3 hat auf der unteren q = 1-Dublette die Eigenwerte {1, omega^2}. Mit g(-) = e^{i pi/3}
  wird daraus {e^{i pi/3}, e^{-i pi/3}}, also G4; die obere Dublette ist G5. Bei q = 2 ist das Triplett T, das Singulett
  E1.
- **[K2] Ableitbarkeit:** Im tiefen Topf sind LP2 (2-fach) und LP3 (3-fach) vorab ableitbar, wie in LADUNG-MONOPOL-1.
- **[K1, M] Ein geschuetztes Quartett gibt es nicht:**
  - In 2T sind alle Spinor-Darstellungen 2-dimensional.
  - Die antiunitaere Operation sigma K bildet C3 auf C3^-1 ab und konjugiert dazu. Damit fuehrt sie jede der drei
    Spinor-Darstellungen in sich selbst ueber und klebt G5 nicht an G6.
  - Wigners Test ist fuer G4, G5 und G6 gleich (sie unterscheiden sich um eine 1-dim Darstellung, die sigma K festlaesst).
    Der K4 hat zwei einfache Dubletten, also Typ (a): keine zusaetzliche Entartung.
  - Folge: Bei q = 1 ist jede Stufe genau 2-fach. Ein Quartett entsteht nur durch Zufall (Kreuzung genau auf einem
    Rasterpunkt).
  - Die Kartenalternative "Quartett F_3/2 unten" ist damit symmetrisch ausgeschlossen. LP2 ist bis auf Zufall vorab
    ableitbar.
  - Echt offen ist: Ist die tiefste gebundene Dublette G4 (j = 1/2-artig) oder G5/G6 (abgespaltene Haelfte des
    j = 3/2-Quartetts)?
  - Ebenso bei q = 2: Stufen sind 3-fach (T) oder einfach (A, E1, E2). Das E-Paar von T_d zerfaellt.
- **Grenzen:** Wigner-Typ und "kein Quartett" sind meine Herleitung; die Rechnung prueft sie (Vervollstaendigung mit der
  antiunitaeren Operation, Stufenzahlen).

## 3. Raster und Messgroessen

- q in {0, 1, 2}, L in {4, 6, 8}, V0 in {0, 1, 2, 3, 4, 6, 8, 12} (Karte, wie LADUNG-MONOPOL-1). Hauptstring s1.
- **Spektrum:** eigsh(which = 'SA', tol = 0, ncv = 64, fester Startvektor), k = 16, berichtet die tiefsten 12; Stufen,
  die den 16. Eigenwert beruehren, gelten als "nicht voll" [F wie LADUNG-MONOPOL-1].
- **Stufe:** Kette mit relativem Abstand <= 1e-8 (Karte LADUNG-MONOPOL-1). Energie = Mittelwert.
- **Gebunden [F, K3]:** "Schwelle wie LADUNG-MONOPOL-1" heisst hier: E < -6 - 1e-3 und Gewicht in r <= 3 a mindestens
  0,9.
  - Die Bandkante des Pyrochlor-Netzes mit H = -Adjazenz ist -6 (Grad 6, gleichfoermiger Zustand) [M].
  - r wird in Kantenlaengen gemessen (in LADUNG-MONOPOL-1 war die Gitterkonstante die Kantenlaenge). Kein Platz liegt
    genau auf r = 3 a (r^2 ist 3 mod 8, 72 nicht).
  - Gewicht der Stufe = Tr(P Pi_{r <= 3a})/m.
- **Tiefste gebundene Stufe:** die tiefste volle Stufe mit dem Kriterium (wie LADUNG-MONOPOL-1); ob sie zugleich die
  tiefste Stufe ueberhaupt ist, wird berichtet.
- **Schwelle V0c je (L, q):** Rasterklammer, ohne Bindung bei 12 Verdoppelung bis 48; Bisektion auf Breite <= 1e-3;
  V0c = Mitte. Beschreibend daneben die reine Energieschwelle.
- **Gegenproben:**
  - String: s2 und s3 gegen s1 bei q = 0, 1, 2, allen L, V0 in {0, 4, 12}; max |dE| der tiefsten 12.
  - Dicht bei L = 4 (Karte: "bei kleinem L"): numpy eigvalsh an allen 8 Raster-V0 und allen q; Eigenwerte und
    Stufengroessen.
  - Zweitlauf L = 8: q = 1, 2, alle Raster-V0 ueber der Schwelle, anderer Startvektor, ncv = 96; dazu das obere
    Bisektionsende.
  - Kato: E_0(q) >= E_0(0) an allen Rasterpunkten.
  - K4-Schreibtisch im Code: Spektrum und Darstellungen der 4 x 4-Kernmatrix je q, gegen Abschnitt 2.
  - Operatoren: U_C3^3 = (-1)^q, Rx^2 und A^2 konstant, Fixecken-Phasen.
- **Bild (beschreibend):** feines Raster V0 = 0 bis 12 in Schritten von 0,25 bei L = 6, alle q; Form = Entartung,
  Farbe = Darstellung; Ringe = tiefste Stufe bei L = 8 auf dem Kartenraster mit "m Darstellung".

## 4. Vorhersagen der Karte (unveraendert uebernommen)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LP0 | Kontrolle: q = 0 tiefste gebundene Stufe einfach; Fluss durch jede Zelle <= 1e-12 ausser der Monopolzelle (2 pi); Spektrum unabhaengig von der String-Richtung auf 1e-10 | 90 % |
| LP1 | Kontrolle: q = 1: Kommutatorzeichen -1 auf allen Stufen, jede Stufe gerade entartet; q = 2: +1 | 90 % |
| LP2 | [H] q = 1, groesstes L, jedes V0 ueber der Schwelle: tiefste gebundene Stufe genau 2-fach (Dublett), nicht 4-fach (Quartett F_3/2) | 60 % |
| LP3 | [H] q = 2, gleiche Bedingungen: tiefste gebundene Stufe genau 3-fach (Triplett) | 55 % |
| LP4 | Tief gebundene Eigenwerte bei den zwei groessten L auf 1e-6 gleich | 80 % |

## 5. Urteilsregeln (mechanisch, code/auswertung.py)

- **Gueltigkeit (alle LP) [F]:** Euler = 1, Zellraender 0, Umkugel und Eckenzahl, Inzidenz innen vollstaendig,
  zusammenhaengend, Grad <= 6, lsqr-Rest <= 1e-10 und Schliessung <= 1e-12 fuer alle drei Strings und alle L,
  Drehdefekte <= 1e-10. Scheitert eines, sind alle LP "nicht auswertbar".
- **LP0:** eingetroffen, wenn alle drei Teile gelten:
  - (a) q = 0: An allen (L, V0) mit gebundener Stufe ist die tiefste gebundene Stufe einfach; mindestens ein Punkt,
    sonst nicht auswertbar.
  - (b) Fluss: Auswaertssumme <= 1e-12 in jeder vollen Zelle ausser der Monopolzelle, dort 2 pi +- 1e-12, alle L.
  - (c) String: max |dE| <= 1e-10 an allen Punkten aus Abschnitt 3, bei q = 0, 1, 2 [F, K4: bei q = 0 ist die Probe
    trivial, weil es kein Feld gibt]. Nach Kartenwortlaut (nur q = 0) wird getrennt berichtet.
  - Symmetrie-Rest voller Stufen <= 1e-6, sonst nicht auswertbar.
- **LP1:** eingetroffen, wenn bei q = 1 an allen (L, V0) Operator-c = -1 (Rest <= 1e-8) und s = -1 auf jeder vollen
  Stufe gelten (|s + 1| <= 1e-8) und jede volle Stufe gerade ist, und bei q = 2 Operator-c = +1 und s = +1 auf jeder
  vollen Stufe.
- **LP2:**
  - Punkte: q = 1, L = 8, alle Raster-V0 > V0c(1, L = 8) [F: "jedes V0" = Kartenraster].
  - Eingetroffen, wenn an jedem Punkt die tiefste gebundene Stufe genau 2-fach ist.
  - Nicht eingetroffen, wenn sie an einem Punkt eine andere Groesse hat.
  - Nicht auswertbar, wenn es keinen Punkt gibt, an einem Punkt keine gebundene Stufe vorliegt, der Symmetrie-Rest
    > 1e-6 ist oder der Zweitlauf Groesse oder Energie (relativ 1e-9) nicht bestaetigt.
  - Berichtet wird zusaetzlich die Darstellung (G4/G5/G6) je Punkt und am oberen Bisektionsende; sie geht nicht ins
    Urteil (die Karte urteilt nur nach der Entartung).
- **LP3:** wie LP2 mit q = 2 und genau 3-fach; Darstellung (T oder anderes) berichtet.
- **LP4 [F]:**
  - "Tief gebunden" = volle Stufe, gebunden nach dem Kartenkriterium und mit Bindung -6 - E >= 1 (eine Huepfeinheit).
  - Verglichen werden bei L = 8 alle solchen Stufen an allen Raster-(q, V0) mit der Stufe gleichen Index bei L = 6.
  - Eingetroffen, wenn ueberall die Groesse gleich ist und |dE| <= 1e-6. Nicht auswertbar ohne solche Stufe.
  - Beschreibend daneben der Vergleich aller gebundenen Stufen (wie LM5).

## 6. Kartenberichtigungen und Anmerkungen (vor dem Einfrieren)

- **K1 (Symmetriegruppe):** Mit Monopol ist T_d keine unitaere Symmetrie, nur T (Abschnitt 1.4).
  - E_1/2 und E_5/2 sind dann nicht verschieden (beide G4).
  - F_3/2 zerfaellt in G5 + G6, die nicht zusammengehalten werden (Abschnitt 2).
  - Die Kartenalternative "Quartett unten" kann als geschuetzte Stufe nicht auftreten; LP2 ist dadurch bis auf eine
    zufaellige Kreuzung vorab ableitbar.
  - Urteil nach Kartenwortlaut bleibt: genau 2-fach.
- **K2 (Charakter der 120-Grad-Drehung):** Auch in der Doppelgruppe von T_d haben E_1/2 und E_5/2 denselben
  C3-Charakter (+1) [L, Koster-Tafel]; nur S4 trennt sie. Die Karte koennte sie also auch ohne Monopol per C3 nicht
  trennen. Ich ordne per C3-Eigenwerten mit der Phasenwahl aus 1.4 in 2T ein.
- **K3 (Sechsecke):** Die Karte sagt "Sechsecke sind nicht eben". Die Kagome-Sechsecke liegen in den Kagome-Ebenen und
  sind eben (Rauchlauf: Abstand 0). Die Faecherflaeche wird trotzdem benutzt; sie ist hier mit der ebenen Flaeche
  identisch.
- **K4 (String bei q = 0 trivial):** mitgeprueft bei q = 1, 2 (Abschnitt 5).
- **K5 (Kartenwortlaut "Schwelle wie LADUNG-MONOPOL-1"):** uebertragen als r <= 3 Kantenlaengen, Bandkante -6
  (Abschnitt 3).
- **K6 (Ableitbarkeit):** s = (-1)^q (Karte), Entartung im tiefen Topf (Abschnitt 2) und "kein Quartett"
  (Symmetrie) sind vorab ableitbar. Offen sind die Schwellennaehe, die Darstellung der tiefsten Dublette, die
  Schwellen und die Groessenkonvergenz.
- **Nach Kartenwortlaut:** Weicht ein Urteil der Plan-Lesart davon ab, wird es in ERGEBNIS.md getrennt genannt.

## 7. Ablauf

- .69, Ordner /home/fmh/fmhc-physics-remote/runde38-ladung-monopol2/ (code/, rauch/, lauf/), nur ueber kleintest.sh,
  Spur p4000a. CPU-scipy (eigsh) wie im Auftrag; die GPU der Spur bleibt ungenutzt.
- Einfrieren: PLAN.md.eingefroren-JJJJMMTT-HHMMSS, Code-Kopien, EINGEFROREN-SHA256.txt.
- Hauptlaeufe:
  - gitter-a (L = 4, 6; dicht bei 4)
  - gitter-b (L = 8)
  - schwelle-46 (L = 4, 6) und schwelle-8 (L = 8, mit Zweitlauf)
  - scan (L = 6)
  - auswertung (Urteile, auswertung.json, Bild)
- Abbruchregel: Laeuft ein Teil nach zwei ernsthaften Versuchen nicht, gilt er als "nicht gerechnet" mit Grund.

## 8. Rauchlauf-Befunde (vor dem Einfrieren offengelegt)

- **rauch1:** 05:12:09 bis 05:12:34 UTC, rc = 0. L = 4, q = 0, 1, 2, V0 = 0, 4, 12, dazu dicht, Strings und eine
  Zeitprobe L = 8 (q = 1, V0 = 4). Code danach nur geaendert: dichte Gegenprobe an festes L (--dicht 4, sonst waere sie
  bei L = 8 gelaufen) und Etikett "E1+E2" fuer 2-fache q = 0-Stufen (vorher "gemischt").
- **Kontrollen [E]:**
  - L = 4: 1024 Ecken, 2712 Kanten, 1708 Dreiecke, 688 Sechsecke, 427 Tetraeder, 280 Stumpftetraeder. Euler 1,
    Zellraender 0, Umkugel ok, Inzidenz innen 384 von 384, Sechsecke eben (0,0).
  - Fluss: Zellen <= 6e-16, Monopolzelle 2 pi auf 9e-16, Monopol-Dreiecke pi/2 auf 2e-16. lsqr-Rest 1,3e-14
    (77 Iterationen), alle drei Strings (je 7 Flaechen).
  - Defekte <= 2e-13. Kommutator +1, -1, +1 (q = 0, 1, 2), Rest <= 7e-14. U_C3^3 = (-1)^q. A^2 = +1.
  - Fixecken-Phasen q = 1: +60 Grad (t = -9, -1), -60 Grad (t = 7, 15); Verhaeltnis 120 Grad, wie in 1.4 erwartet.
    q = 2: +-120 Grad.
  - K4 im Code: q = 1: -sqrt3 (2, G4), +sqrt3 (2, G5); q = 2: -1 (3, T), +3 (1, E1); q = 0: -3 (1, A), +1 (3, T). Genau
    wie Abschnitt 2.
  - Dicht gegen eigsh <= 6e-14, Stufengroessen gleich an 9 von 9 Punkten. String-Differenzen <= 2,1e-14.
  - Zeit: L = 4 je Punkt 0,15 s, dicht 0,8 s; L = 8: Gitteraufbau 9,9 s, lsqr 149 Iterationen, eigsh 1,4 s je Punkt.
- **Gesehen, was die Urteile vorwegnimmt (Selbstanzeige; daran wurde nichts geaendert):**
  - L = 4, V0 = 4: tiefste Stufe q = 0 einfach bei -7,613 (Gewicht 0,998); q = 1 G4-Dublette bei -6,563 (0,987);
    q = 2 Triplett T bei -6,048 (0,921), alle gebunden.
  - L = 4, V0 = 12: q = 1 G4 bei -13,988, darueber G5 bei -10,630; q = 2 T bei -13,273, darueber E1 bei -9,426.
  - L = 4, V0 = 0: q = 1 alle Stufen 2-fach; die zweite und dritte (G6 bei -5,5115 und G5 bei -5,5111) liegen nah
    beieinander, aber getrennt. q = 2: das Paar E1/E2 ist ebenfalls getrennt (-5,4626 und -5,4647).
  - Die Schwellen bei L = 4 liegen damit fuer alle q unter 4; ihre Lage kenne ich nicht.
- **Nicht geaendert:** Vorhersagen, Schwellen, Urteilsregeln.

## 9. Agenten-Vorhersagen (nach rauch1, vor den Hauptlaeufen; Rauchlauf-Wissen offengelegt)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | LP2 eingetroffen; die tiefste gebundene q = 1-Stufe ist an allen Punkten und am oberen Bisektionsende G4 | 85 % |
| A2 | LP3 eingetroffen; die tiefste gebundene q = 2-Stufe ist an allen Punkten und am oberen Bisektionsende T | 85 % |
| A3 | L = 8: V0c(0) in [1,5; 2,6], V0c(1) in [2,4; 3,6], V0c(2) in [3,3; 4,3]; Reihenfolge V0c(0) < V0c(1) < V0c(2) | 55 % |
| A4 | LP4 eingetroffen; der Vergleich aller gebundenen Stufen (wie LM5) scheitert an mindestens einer schwellennahen Stufe (dE > 1e-6) | 60 % |
| A5 | Keine 4-fache Stufe bei q = 1 und keine 2-fache bei q = 2 an irgendeinem Rasterpunkt (alle L); Wigner-Typ (a) wie in Abschnitt 2 | 85 % |
| A6 | Kato: E_0(q) >= E_0(0) an allen Rasterpunkten | 97 % |
