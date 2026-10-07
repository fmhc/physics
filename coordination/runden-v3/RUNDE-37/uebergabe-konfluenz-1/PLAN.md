# UEBERGABE-KONFLUENZ-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Start 2026-10-05 11:21:14 CEST (date). Plantext ab 2026-10-05 11:40:32 CEST (date), vor jeder Hauptrechnung.
  Zeitbox 120 min, also bis 13:21:14 CEST.
- Grundlage: KARTE.md (UK0 bis UK4, Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] vorab ableitbar (eigene Mathematik, nicht gegengelesen), [E] hier gerechnet, [P] Projektdatei,
  [F] eigene Festlegung, [H] Hypothese oder Lesart. Alles ist synthetische Gitterrechnung, keine Messdaten.
- Code: code/konfluenz.py (neu). Unveraendert kopiert aus RUNDE-37/hodge-masse-1/code und importiert: td.py
  (fbc02c48..., = TAKT-DYNAMIK-1 eingefroren), hm_td.py (c62c15ab..., HODGE-MASSE-1 eingefroren), tg.py (ec48a258...),
  uk.py (f52df743...), tu.py (6c5c3a95...), dazu deren Importe tp.py (419d7da6...), ew.py (fa7b6417...), mn.py
  (b36984d3...), tg_auswertung.py (88cbd2ce...). Die Originale sind unveraendert.

## 1. Netz und Konstruktion zweier gleichzeitig faelliger Zuege [F]

- **Netz:** Glas N = 128 (tg.zufallsnetz(128, s), TT-GLAS-1), Saaten s = 1 bis 4. Periodischer Kasten, Bloch-k = 0,
  Operatoren auf den Hintergrundlagen (Lesart H aus TAKT-DYNAMIK-1), Zwangsflaeche S = Komplement von Bild[M, c, 1_E]
  (td.Netz, R1).
- **Ueberlappungsarten** (Traeger eines Zugs = Doppelpyramide der Flaeche, 2 Tetraeder, 5 Ecken):
  - **T:** X und Y sind zwei Flaechen desselben Tetraeders (gemeinsames Tetraeder).
  - **K:** X und Y haben eine gemeinsame Flaechenkante, aber kein gemeinsames Tetraeder.
  - **D:** Die beiden Doppelpyramiden haben keine gemeinsame Ecke (disjunkte Traeger, Kontrolle UK0).
- **Kandidaten:** T: alle Flaechenpaare je Tetraeder; K: alle Flaechenpaare je Kante ohne gemeinsames Tetraeder;
  D: Paare unter den 40 Flaechen mit kleinstem Randabstand mu0 ohne gemeinsame Ecke. Nur Flaechen mit 5 verschiedenen
  Ecken. Sortiert nach max(mu0_X, mu0_Y) aufsteigend; hoechstens die ersten 80 je Art; eine Flaeche wird je Art und
  Saat hoechstens einmal benutzt.
- **Eckverschiebung ("kleine Eckverschiebung" der Karte):** Verschoben werden die Hintergrundlagen. Zwei Schemata:
  - (1) eine gemeinsame Ecke beider Doppelpyramiden (nur T, K): Gauss-Newton mit Mindestnorm fuer mu_X = mu_Y = -1e-3;
  - (2) je eine Ecke, die nur in der Doppelpyramide von X bzw. nur in der von Y liegt (T, K, D): je eine Gleichung
    mu = -1e-3.
  - Jede Einzelverschiebung hoechstens 0,1 x mittlere Kantenlaenge. Von allen Moeglichkeiten wird die mit der
    kleinsten Gesamtnorm genommen, die drei Pruefungen besteht:
    - genau X und Y sind verletzt (mu < -1e-9, wie tu.TOL_MU), alle anderen Flaechen nicht;
    - kein Tetraeder kehrt sein Vorzeichen um;
    - X und Y sind je fuer sich ausfuehrbar (2-3 nach tu.zug23_ok bzw. 3-2 nach tu.zug32_vorbereiten, Volumen > 1e-10
      des Mittels wie td.py).
- Je Art und Saat hoechstens **5 Faelle**; also hoechstens 60 Faelle. Weniger, wenn die Kandidaten nicht reichen
  (wird ausgewiesen).

## 2. Reihenfolge XY und YX [F]

- **XY:** Zug an X im verschobenen Ausgangsnetz, danach "umklappen bis Delaunay" auf dem Hintergrund:
  - verletzte Flaechen (mu < -1e-9), staerkste zuerst;
  - 2-3, wenn die Doppelpyramide konvex ist, sonst 3-2 ueber die Kante, hinter der d-e die Flaechenebene trifft (Grad 3);
  - nicht ausfuehrbar: naechste Flaeche;
  - Regel wie tu.reparatur; Ausfuehrung und Zugbeschreibung durch td.zug_ausfuehren (unveraendert).
- **YX:** dasselbe mit Y zuerst. Hoechstens 12 Zuege je Reihenfolge.
- Status je Reihenfolge: ok, stecken (verletzte Flaechen, kein Zug moeglich), max.
- **Endzerlegung gleich:** gleiche Menge der Tetraederschluessel (uk.tetra_schluessel) nach XY und YX. Nur Faelle mit
  gleicher Endzerlegung werden in den Sektoren verglichen.

## 3. Felder und Zustand [F]

- **Geometrie (q, p):** Fuer jede Form die TT-Mode des Ausgangsnetzes (td.tt_mode, unveraendert) mit TT-Amplitude
  A_q = 1e-3 (wie TAKT-DYNAMIK-1), als stehende Welle zur Phase 1 rad: x0 = sin(1) x_Mode,
  dx/dt = omega cos(1) x_Mode, y0 = A_red^-1 dx/dt. q heisst hier a = S x (Kantenwerte dl/l), p heisst S y.
  Die Uebergabe ist linear; relative Abstaende haengen von A_q nicht ab [M].
- **Skalar (phi, pi):** auf den Ecken, wie GRUNDGLEICHUNG-SKIZZE-v2 3.1 (reell, ohne Potential):
  - H_phi = 1/2 pi^T *0^-1 pi + 8/2 (d0 phi)^T *1 (d0 phi), *0 und *1 umkreisbasiert und vorzeichenbehaftet
    (tu.hodge unveraendert, *0 aus dessen Formel je Ecke nachgebildet, Kontrolle Summe *0 = V);
  - Anfang: phi_v = A cos(k1 . r_v + 0,3), pi_v = *0_v A |k1| sin(k1 . r_v + 0,3), Amplituden A = 0, 1e-3, 1e-2;
  - Testfeld ohne Rueckwirkung auf die Geometrie. Der Vorlagencode hat keine Kopplung Feld -> Geometrie.
- **Licht (A, E):** nicht gerechnet. Der Vorlagencode (td.py, hm_td.py) hat keinen Lichtsektor (Auftrag: "Licht nur,
  wenn der Vorlagencode es hat"). Damit entfaellt auch der Gauss-Rest im Sinne von d0^T E (Abschnitt 6).

## 4. Uebergabe ueber einen Zug (wie im Vorlagencode) [F, P]

- **Geometrie:** td.abbilden unveraendert (TAKT-DYNAMIK-1, PLAN 4):
  - **Lesart R:** gemeinsame Kanten behalten a und da/dt; 2-3: neue Kante a_de = j . a_9, da_de/dt = j . da_9/dt
    (j = Linearisierung der flachen Laenge der Doppelpyramide); 3-2: wegfallende Kante gestrichen; dann
    x' = S'^T a', dx'/dt = S'^T da'/dt (orthogonale Projektion), y' = A'_red^-1 dx'/dt.
  - **Lesart P:** a wie R; p = S y; 2-3: p'_de = 0 (Null-Fortsetzung); 3-2: p' = p + J^T p_PQ auf den 9 Kanten;
    y' = S'^T p'.
- **Skalar:** Die Ecken bleiben bei 2-3 und 3-2 dieselben. phi' = phi.
  - **Lesart R:** Raten stetig: dphi/dt = pi / *0 bleibt, also pi' = *0' pi / *0.
  - **Lesart P:** pi' = pi.
- **Inverser Zug** (fuer die Zeitumkehr): 2-3 <-> 3-2 mit vertauschten alten und neuen Tetraedern und denselben 9
  Kanten der flachen Doppelpyramide; td.abbilden unveraendert.

## 5. Formen der Bewegungsenergie [F, P]

- **Form A:** A1 (J = 1, td.Netz) und A2 (Kartenformel aus HODGE-MASSE-1, hm_td.NetzHM mit KIN = A2, R1).
  GRUNDGLEICHUNG-SKIZZE-v2 2.2 nennt A2 die Projektvariante der Form A.
- **Form B:** A2L (Lagrange-additive volumengewichtete DeWitt-Form, Lund-Regge-artig, hm_td KIN = A2L, R1).
  **Startbar** heisst: A_red ist im verschobenen Ausgangsnetz des Falls positiv definit (Cholesky gelingt), wie td.lauf
  es verlangt. Nicht startbar: nur n_A_neg wird notiert, kein Zustand.
- V_ref (A2, A2L) = Kastenvolumen / Tetraederzahl des Ausgangsnetzes, fest ueber alle Zuege des Falls.

## 6. Messgroessen [F]

- **Delta_s** je Sektor s in {q, p, phi, pi}: relativ ||u_XY - u_YX|| / max(||u_XY||, ||u_YX||), dazu absolut
  ||u_XY - u_YX||. q = S x und p = S y im Kantenraum der Endzerlegung (unabhaengig von der Basis S).
- **Delta_Feld** = max(Delta_phi, Delta_pi) (relativ bzw. absolut). Die Karte nennt die Felder getrennt von der
  Geometrie (Bau: "mit und ohne Felder (Skalar-Amplitude 0, 1e-3, 1e-2)"); Delta_Feld meint hier also den Skalar.
- **Delta_H** = |H_XY - H_YX| / H_XY, getrennt Geometrie (Form, Lesart), Skalar (Lesart, Amplitude) und gesamt
  (H_geo + H_phi je Amplitude).
- **Gauss-Rest:** Ohne Lichtsektor gibt es kein d0^T E. Ersatzgroesse (beschreibend): Zwangsrest vor der Projektion
  je Zug, ||a' - S' S'^T a'|| / ||a'|| (proj_rest_a aus td.abbilden), Summe ueber die Zugfolge. Nach der Projektion
  ist der Zwang konstruktionsbedingt erfuellt.
- **Zeitumkehr (statisch):** Endzustand von XY (bzw. YX), Impulse umgekehrt (y -> -y, pi -> -pi), die inversen Zuege in
  umgekehrter Reihenfolge mit derselben Lesart, Impulse wieder umgekehrt; Abstand zum Anfangszustand je Sektor
  (relativ). Die dynamische Probe (Bahn rueckwaerts mit Ereignissuche) ist nicht gerechnet: Hier loest die
  Hintergrundverschiebung die Zuege aus, nicht die Welle.
- **Haeufigkeit (beschreibend):** In den vorhandenen TAKT-DYNAMIK-1-Laeufen td-glas-N128-s1..s4-A1e-3-b.json (h = 0,5)
  und ...-b-h025.json (h = 0,25), Lesart R, auf der .69: Zahl der Zeitschritte n mit mindestens zwei
  Delaunay-Ereignissen (ausgefuehrt oder nicht) bzw. mindestens zwei ausgefuehrten Zuegen; Anteil an allen Schritten und
  an den Schritten mit Ereignis; dazu Zuege, nach denen sofort eine Flaeche verletzt war (dort gesperrt).

## 7. Urteilsregeln (mechanisch, code/konfluenz.py auswertung)

- Gewertet werden Faelle mit gleicher Endzerlegung. "BODEN" = 1e-12 (Schwelle der Karte fuer "exakt" aus UK0).
- **UK0** (Plan = Wortlaut): eingetroffen, wenn (i) in allen D-Faellen alle Delta (q, p fuer A1 und A2, R und P;
  phi, pi fuer A = 1e-3 und 1e-2, R und P) < 1e-12 sind und (ii) in allen Faellen (D, T, K) die Endzerlegung von XY und
  YX gleich ist (Status "stecken" oder "max" zaehlt als nicht gleich). Sonst verfehlt. Ohne D-Fall: (ii) verfehlt ->
  verfehlt, sonst nicht entscheidbar.
- **UK1:** Lesart R, A = 1e-3, Arten T und K getrennt.
  - Plan: Median ueber die Faelle einer Art von Delta_Feld (relativ) > 1e-6 fuer mindestens eine Art -> eingetroffen.
  - Wortlaut: dasselbe mit dem Maximum statt dem Median (irgendein Fall).
  - Kein T- und kein K-Fall: nicht entscheidbar.
- **UK2:** T und K zusammen, Lesarten R und P zusammen; je (Fall, Lesart) Steigung
  log10(Delta_Feld,abs(1e-2) / Delta_Feld,abs(1e-3)).
  - Plan: nur Paare mit Delta_Feld (relativ) > 1e-12 bei beiden Amplituden (Signal ueber Rundung). Median in
    [0,9; 1,1] -> eingetroffen; kein solches Paar -> nicht entscheidbar; sonst verfehlt.
  - Wortlaut: alle Paare mit Delta_Feld,abs > 0 bei beiden Amplituden, sonst wie Plan. Hinweis [M]: Rundungsfehler
    einer linearen Abbildung skalieren selbst linear mit der Amplitude; der Wortlaut kann also an Rundung eintreffen.
- **UK3:** A = 1e-3, T und K zusammen; m_R, m_P = Mediane von Delta_Feld (relativ) in Lesart R bzw. P.
  - Plan: beide <= 1e-12 -> nicht entscheidbar; nur m_P <= 1e-12 -> eingetroffen; nur m_R <= 1e-12 -> verfehlt;
    sonst m_R / m_P >= 10 -> eingetroffen, sonst verfehlt.
  - Wortlaut: ohne Boden; m_P > 0: m_R / m_P >= 10 -> eingetroffen, sonst verfehlt; m_P = 0: m_R > 0 -> eingetroffen,
    beide 0 -> nicht entscheidbar.
- **UK4:** Form B (A2L) nicht startbar in allen T- und K-Faellen -> nicht entscheidbar (Kartenwortlaut). Sonst, ueber die
  startbaren T- und K-Faelle, Lesart R, r = Delta_p(A2L) / Delta_p(Form A):
  - Plan: Median von r gegen A2 > 2 oder < 1/2 -> eingetroffen, sonst verfehlt;
  - Wortlaut: dasselbe gegen A1 und gegen A2 (beide Varianten der Form A).
- Fehlen Faelle, werden die vorhandenen gewertet und die Zahl vermerkt.

## 8. Ableitbarkeitsprobe (vor dem Einfrieren) [M, nicht gegengelesen]

- **Skalar auf den Ecken: vorab ableitbar, dass Delta_Feld = 0 bis auf Rundung.**
  - 2-3- und 3-2-Zuege behalten alle Ecken (uk.py: "auf festen Ecken"). phi wird je Ecke uebernommen, pi in Lesart P
    ebenfalls, in Lesart R mit dem Faktor *0'_v / *0_v.
  - Diagonale Abbildungen vertauschen. Nach beiden Zuegen ist pi_R = *0_End / *0_Anfang x pi in jeder Reihenfolge,
    sobald die Endzerlegung gleich ist.
  - Folgen: UK1 vorab verfehlt. UK2 nach Plan vorab nicht entscheidbar (kein Signal), nach Wortlaut moeglicherweise an
    Rundung eingetroffen. UK3 nach Plan vorab nicht entscheidbar. Die Zeitumkehr des Skalars ist vorab exakt
    (R: Faktor und Kehrwert; P: Identitaet).
  - Das ist Ableitbarkeitsprobe (c) der Karte. Die Karte nennt "Groesse von Delta_Feld je Ueberlappungsart" nicht
    ableitbar; fuer einen Eckenskalar ohne Rueckwirkung ist sie es doch.
  - Was die Rechnung hier noch prueft: Umsetzung (Rundung) und dass die Endzerlegung gleich ist.
  - Eine Reihenfolgespur in den Feldern braeuchte (a) Felder auf Kanten oder Zellen (Licht A_e, E^e; Zellfelder) oder
    (b) Rueckwirkung (Materie in der skalaren Regel). Beides steht nicht im Vorlagencode.
- **Geometrie, Lesart R, reine 2-3-Folgen:**
  - Aus der Schreibtischpruefung von TAKT-DYNAMIK-1 (PLAN 4) folgen J M = M', J 1_E = 1_E' und c'^T J a = c^T a.
  - Mit c' orthogonal zu M' (B M = 0) und zu 1_E' (B 1_E = 0) entfernt die Projektion nach einem 2-3-Zug nur Anteile
    in Bild[M', 1_E']. Der naechste Zug bildet diese wieder in Eichung und Streckung ab, und die letzte Projektion
    loescht sie.
  - Also gilt am Ende P_End J_2 J_1 a in beiden Reihenfolgen. Fuer D (J vertauschen) folgt Delta_q = Delta_p = 0 bis auf
    Rundung.
  - Fuer T und K haengt der Abstand daran, ob die flachen Fortsetzungen der neuen Kanten ueber verschiedene
    Doppelpyramiden gleich ausfallen. Das stimmt fuer flache (Eich-)Anteile exakt, fuer die gekruemmte Welle nicht.
    Erwartet: Delta > 0 von der Ordnung des Fehlwinkelgehalts; die Groesse ist nicht ableitbar.
- **Nicht ableitbar (offen):**
  - Geometrie mit 3-2-Zuegen in Lesart R: Die Projektion entfernt dort auch einen Anteil entlang c' (TAKT-DYNAMIK-1 PLAN
    4.3). Die Koeffizienten kommen aus einer globalen Kleinste-Quadrate-Loesung. Ob disjunkte 3-2-Zuege dann noch
    exakt vertauschen, folgt daraus nicht.
  - Lesart P: Die Null-Fortsetzung des Impulses erfuellt c'^T Z p = 0 nicht allgemein; die Projektion kann dann
    nichtoertlich wirken. Auch D-Faelle koennen in P > 1e-12 ergeben. Das wuerde UK0 nach Regel verfehlen lassen.
  - die Groesse von Delta_q, Delta_p je Art, Lesart und Form;
  - die Zeitumkehr der Geometrie bei Folgen mit 3-2. Bei reinen 2-3-Folgen in R ist sie exakt [M]: R J = 1 auf den
    alten Kanten, Eichanteile werden geloescht. Ein 3-2 mit Rueckweg 2-3 ersetzt a_PQ durch die flache Fortsetzung
    und verliert den nichtflachen Anteil delta.
- **UK4 [P]:** Nach HODGE-MASSE-1 hat A2L mit R1 im Kasten 28 bis 46 negative Richtungen. Erwartet: nicht startbar,
  also UK4 nach Kartenwortlaut "nicht entscheidbar".
- **Lesart P und Form:** In Lesart P geht A_red nicht in die Uebergabe ein. Unterschiede zwischen A1 und A2 kommen
  dort nur aus der Anfangsmode [M].

## 9. Laeufe auf der .69 (kleintest.sh, Spuren p4000a und p4000b, <= 600 s je Aufruf)

- Arbeitsordner /home/fmh/fmhc-physics-remote/uebergabe-konfluenz-1/ (code/ eingefroren, lauf/).
- Kette (code/kette.sh, einmal je Spur per ssh gestartet, kein Dienst, kein Timer):
  - p4000a: lauf Saat 1, dann Saat 3;
  - p4000b: lauf Saat 2, dann Saat 4. Sperrt kleintest.sh p4000b (WM-1-MB laeuft), laufen 2 und 4 nach 1 und 3 auf
    p4000a.
  - Danach auf p4000a: haeufigkeit (TAKT-DYNAMIK-1-Laeufe, nur lesen), auswertung, tabellen, Pruefsummen.
- Schaetzung aus den Rauchtests: etwa 8 s je Fall, also 2 bis 3 min je Saat.
- Schlusszeit: nach 13:00 CEST (11:00 UTC) startet kein neuer Aufruf.

## 10. Agenten-Erwartungen (vorab; gehen in kein Urteil ein)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E1 | Endzerlegung XY = YX in allen Faellen mit Status ok/ok | 90 % |
| E2 | Skalar: Delta_Feld <= 1e-13 in allen Faellen und Lesarten | 90 % |
| E3 | Geometrie D, Lesart R: Delta_q, Delta_p < 1e-12 in allen D-Faellen nur mit 2-3-Zuegen | 80 % |
| E4 | Geometrie T und K, Lesart R: Median Delta_q > 1e-6 | 60 % |
| E5 | A2L nicht startbar in allen Faellen | 85 % |

## 11. Rauchtests vor diesem Plantext (.69 in UTC)

- r1 (09:37:25 bis 09:37:52, p4000a, Saat 1, --rauch, 1 Fall je Art): rc = 0, 27,4 s. Gelesen: Laufzeit, Fallzeiten
  (6,8 bis 9,1 s), Zahl angenommener Faelle je Art (1 / 1 / 1), Schluessel. Keine Abstaende, Status oder
  Endzerlegungen.
- r2 (09:38:27 bis 09:39:06, p4000a, Rauchsaat 901, 1 Fall je Art, volle Ausgabe in rauch/): rc = 0. Nicht gelesen.
- r3 und r5 (auswertung auf rauch/), r4 (haeufigkeit auf den TAKT-DYNAMIK-1-Laeufen), r6 (tabellen): rc = 0.
  Gelesen: nur rc, die Schluessel der Urteile, die Zahl der Haeufigkeitszeilen (8) und die Zeilenzahl der Tabelle.
- Nach r1 geaendert: N_FAELLE 3 -> 5, Testoption --faelle; nach r4 die Modi tabellen und zusammenfassung (nur
  Darstellung); nach r6 ein Schutz: Form A1 bzw. A2 ohne positiv definites A_red im Ausgangsnetz wird wie nicht
  startbar behandelt statt abzubrechen. Regeln (Abschnitte 1 bis 8) danach nicht geaendert.
- r7 (09:42:50 bis 09:43:15, p4000a, Saat 1, --rauch, Stand zum Einfrieren): rc = 0, 24,9 s. Gelesen: Laufzeit und
  angenommene Faelle je Art (1 / 1 / 1).
