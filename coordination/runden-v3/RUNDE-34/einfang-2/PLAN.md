# EINFANG-2: Plan (Code-Agent fuer claude-primary, Runde 34)

- Geschrieben ab 2026-10-03 18:56:46 CEST (date). Wird vor der ersten echten Rechnung eingefroren:
  PLAN.md.eingefroren-<datum-uhrzeit>, code/einfang2.py.eingefroren-<datum-uhrzeit>, code/laufplan.eingefroren-<...>.tar.
- Karte: KARTE.md. E2-0 bis E2-3 und ihre Bedeutung bleiben unveraendert.
- Code:
  - code/einfang2.py (neu)
  - code/kegel_q.py: unveraenderte Kopie von RUNDE-26/kegel-q/code/kegel_q.py.eingefroren-20261003-043140 (sha256
    beginnt mit 4de64b080729204c)
- Rechnen nur auf der .69 ueber kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde34-einfang2/lauf/.
  - Spuren p4000a und p4000b (CUDA, float64); Auswertung und Bild auf cpu4.
  - Rauchlauf: 3,0 ms je Schritt bei nu = 134 (179 562 Knoten), 6,1 ms bei nu = 200.

## 1. Netz

- **Ikosaeder:** Kante a = 40, jede Flaeche in nu^2 gleichseitige Dreiecke zerlegt.
  - nu = 134, also h = 40/134 = 0,29851. nu muss gerade sein, damit die Kantenmitte ein Knoten ist; 134 ist das gerade
    nu mit h am naechsten an 0,3.
  - Knoten auf Ecken und Kanten einmalig (Index je Ecke, je Kante und Schritt, je Flaecheninneres).
  - Kotangens-Gewichte und Eckflaechen aus der Einbettung im R^3; die Flaechen sind eben.
  - Die Bewegung ist rein innerlich (Netzgraph).
- **Netzpruefung** je Lauf (im Rauchlauf a = 40 bestanden):
  - 10 nu^2 + 2 = 179 562 Knoten; 12 Knoten mit Grad 5, alle anderen Grad 6; Euler-Charakteristik 2
  - Winkeldefekt pi/3 nur an den 12 Spitzen (Rest < 3e-14)
  - alle Gewichte 1/sqrt 3 (auf 1e-13); Flaeche 5 sqrt 3 a^2 = 13 856,41
- **Torus (E2-0):** periodisches ebenes Dreiecksnetz N1 x N2 = 335 x 536 = 179 560 Knoten.
  - Gleiches h = 0,29851; Rechteck 100,0 x 138,6.
  - Flaeche N1 N2 sqrt(3)/2 h^2 = 13 856,41, genau die Ikosaederflaeche.
- **Feinere Probe:** nu = 200 (h = 0,2), 400 002 Knoten.

## 2. Modell und Zeitentwicklung

- Gleichung, Energie, Ladung wie EINFANG-1 (M1, beta = 1/2, Q = 200), aber **ohne Schwamm**: A_i phi_i'' = -(L phi)_i -
  A_i U'(|phi_i|^2) phi_i.
- Stoermer-Verlet, float64, dt = 0,1 (EINFANG-1: bei h = 0,3 stabil bis dt = 0,2).
- Verlet erhaelt die Ladung bis auf Rundung; die Energie schwankt (EINFANG-1: 1e-3 bis 2e-3 bei klingendem Ball).
- Ein schwacher globaler Schwamm als Vergleich (optional laut Auftrag) wird nicht gerechnet.

## 3. Start

- **Statischer Ball:** kegel_q.loese_ball auf einem ebenen Sechser-Flicken (Radius 30, Dirichlet), Q_lat = Q/gamma,
  zentriert auf einem Knoten.
  - Uebertragung auf das Zielnetz ueber Gitterkoordinaten. Die Umgebung der Kantenmitte (Radius < 20) ist eben und hat
    dasselbe Dreiecksgitter.
  - Uebertragen wird bis Radius R_trans = 19, ausserhalb ist das Feld 0.
  - Rauchlauf (a = 40, Q = 150, ruhend): Startenergie 1,9e-6 ueber E_lat, Ladungsrest 6e-7.
- **Ort:** Mitte der Kante (Spitze 0, B_0) mit B_0 = kleinster Nachbar von Spitze 0. Abstand zu beiden Endspitzen 20.
- **Boost** wie EINFANG-1: phi = f exp(i omega gamma v e.xi), phi' = [-v e.grad f - i omega gamma f] exp(...), grad f
  aus dem radialen Kontinuumsprofil.
  - Laborladung exakt Q = 200; keine Lorentz-Kontraktion.
  - Richtung e frontal auf Spitze 0, entlang der Kante.
- **Schreibtisch zur frontalen Bahn:**
  - Die Ebene durch die Startkante und den Mittelpunkt ist eine Spiegelebene des Netzes. Sie enthaelt 4 Spitzen
    (0, B_0 und deren Gegenspitzen); eine frontale Bahn bleibt in ihr.
  - Hinter Spitze 0 geht sie durch die Mitte der gegenueberliegenden Flaeche und ueber eine Kantenmitte (Abstand 20 zu
    deren Endspitzen) zur naechsten Spitze. Danach laeuft sie eine Kante entlang.
  - Der Spitzenabstand wechselt also zwischen 69,28 = sqrt(3) a und 40. Jede Spitze wird frontal getroffen.
- **Stossparameter-Lauf:** Richtung um alpha = asin(b/20) gedreht, b = 3,13 (= R_halb/2). Die Gerade verfehlt
  Spitze 0 um b.
- **Torus:** Ball am Knoten (N1/2, N2/2), Richtung +x (Gitterrichtung).

## 4. Messgroessen (Methoden vorab festgelegt)

1. **Ort und Abstand auf dem Ikosaeder:** harmonischer Schwerpunkt je Spitzenkarte, Definition wie KEGEL-Q und
   EINFANG-1.
   - **Karte k:** Abwicklung der 5 Sternflaechen und der 5 Flaechen des zweiten Rings um Spitze k (die Haelfte der
     Oberflaeche). Kegelkoordinaten (r, theta), theta mit Periode 5 pi/3.
   - **Schwerpunkt:** W_k = Sum rho w_k / Sum rho ueber die Kartenknoten mit w_k = r^(6/5) exp(i (6/5) theta).
     rho = Ladungsdichte auf den Ecken mit |phi|^2 > 0,01, wie EINFANG-1 "x".
   - Die Karte gilt nur bei voller Abdeckung: |Sum_Karte rho / Sum rho - 1| <= 1e-6.
   - **Abstand zur Spitze k:** d_k = |W_k|^(5/6), geodaetisch ueber die Abwicklung. Exakt fuer runde Baelle, die die
     Spitze nicht ueberdecken (Mittelwerteigenschaft); nahe der Spitze ist d_k eine Reaktionskoordinate wie x in
     EINFANG-1. Richtung theta_k = arg(W_k)/(6/5).
   - **Naechste Spitze:** kleinstes d_k unter den abgedeckten Karten.
     - Der Ballkern (|phi|^2 > 0,01) hat einen Radius von etwa 9,4.
     - Der Abstand zur naechsten Spitze ist hoechstens 23,1; die Karte reicht ueberall mindestens 40 weit.
     - Daher deckt die Karte der naechsten Spitze den Ball immer ab.
   - Die Lage in 3D (nur Bild und Symmetriepruefung) folgt aus der Rueckabbildung der Karte der naechsten Spitze.
2. **Geschwindigkeit und K (Sehnenverfahren):**
   - Zwischen Diagnosepunkten im Abstand 5 (10 Zeiteinheiten) wird die geodaetische Sehne in der Karte der
     naechsten Spitze gemessen (Kegelabstand der beiden Orte).
   - Bogenlaenge s(t) = Summe der Sehnen; v = Steigung der Ausgleichsgeraden s(t) ueber eine freie Strecke.
   - K = (gamma(v) - 1) E_rest(Q_ball), E_rest(Q) = E_lat + omega (Q - 200) wie EINFANG-1. Q_ball ist das Mittel ueber
     die Strecke.
   - **Q_ball und E_ball:** geodaetische Scheibe mit Radius 15 um den Ball (Kegelabstand in der Karte der naechsten
     Spitze).
   - **Pruefung des Verfahrens:**
     - Torus: v ueber Sehnen gegen die Steigung von x(t).
     - Ikosaeder: v der Startstrecke gegen v0.
     - Rauchlauf Torus (Q = 150, v = 0,15): Sehnen 0,1497640, Gerade 0,1497641.
3. **Torus:** Schwerpunkt mit denselben Gewichten im Mindestbild um den Knoten mit groesstem |phi|^2, stetig
   fortgesetzt; Sehnen euklidisch. Q_ball in der Scheibe mit Radius 15.
4. **Diagnose** alle 2 Zeiteinheiten. Dazu E_tot, Q_tot, max |phi|^2 (Atmung) und |phi|^2 an der naechsten Spitze.

## 5. Begriffe (mechanisch)

- **Freie Strecke:** maximale Folge von Diagnosepunkten, deren Abstand zur naechsten Spitze >= 12 ist.
  - Das entspricht dem Fenster |x| >= 12 in EINFANG-1 (Restpotential < 2e-4).
  - Die Startstrecke zaehlt erst ab t = 20.
  - Eine freie Strecke wird nur mit mindestens 10 Punkten gewertet.
- **Begegnung:** maximale Folge mit Abstand < 12. Sie gehoert immer zu genau einer Spitze, weil Spitzen 40 auseinander
  liegen.
- **Naher Durchgang (Karte: Mindestabstand < 3):** Begegnung mit d_min < 3.
  - K davor = K der freien Strecke unmittelbar davor; K danach = K der freien Strecke unmittelbar danach.
  - Pendelt der Ball innerhalb einer Begegnung mehrfach durch die Spitze, werden die Minima < 3 gezaehlt (Hysterese 2).
    Die Begegnung bleibt ein Eintrag.
- **Wende:** Maximum von d (Abstand zu derselben Spitze) mit Hysterese 2. d steigt vorher um mindestens 2 und faellt
  danach um mindestens 2.
- **Einfang (Karte: "Der Ball bleibt bis T_end innerhalb R_halb + 6 = 12,3 um dieselbe Spitze und wendet dort mindestens
  zweimal"):**
  - Am Laufende (T = 8000) liegt der Ball innerhalb R_halb + 6 = 12,2551 der naechsten Spitze, durchgehend seit einem
    Zeitpunkt t_c.
  - In [t_c, 8000] gibt es mindestens zwei Wenden bezueglich dieser Spitze.

## 6. Laeufe

| Name | Rolle | Netz | v0 | b | dt | T | Spur |
|---|---|---|---|---|---|---|---|
| ik-v0.05 | Hauptlauf (E2-1, E2-2, E2-3) | nu = 134 | 0,05 | 0 | 0,1 | 8000 | p4000a |
| ik-v0.1 | Zusatzlauf (E2-3) | nu = 134 | 0,1 | 0 | 0,1 | 8000 | p4000a |
| torus-v0.05 | E2-0 | Torus | 0,05 | - | 0,1 | 4000 | p4000a |
| ik-v0 | Kontrolle: ruhender Ball | nu = 134 | 0 | 0 | 0,1 | 1000 | p4000a |
| ik-v0.05-lang | Verlaengerung des Hauptlaufs aus seinem Endzustand bis T = 16 000, nur berichtet | nu = 134 | 0,05 | 0 | 0,1 | 16 000 | p4000a |
| ik-v0.05-b | Stossparameter, nur berichtet | nu = 134 | 0,05 | 3,13 | 0,1 | 8000 | p4000a |
| ik-v0.05-h0.2 | Probe h | nu = 200 | 0,05 | 0 | 0,05 | 8000 | p4000b |
| ik-v0.05-dt0.05 | Probe dt | nu = 134 | 0,05 | 0 | 0,05 | 8000 | p4000b |

- **Abschnitte:** Wandzeit 500 s je Aufruf.
  - Danach werden Felder, Zeitableitungen, Zeit und Aufzeichnung gespeichert und mit --fortsetzen weitergerechnet
    (hoechstens 4 Fortsetzungen).
  - Am Laufende wird der Zustand immer gespeichert (fuer die Verlaengerung).
- **Frist:** Laeufe, die bis 20:15 CEST nicht fertig sind, gehen mit dem erreichten T ein.
  - Erreicht der Hauptlauf T = 8000 nicht, ist E2-2 nicht entscheidbar.
  - Fehlt ein Lauf ganz, ist die zugehoerige Vorhersage nicht entscheidbar.

## 7. Urteile (Wortlaut der Karte, dann die mechanische Fassung)

- **E2-0** (Karte: "Kontrolle Torus, v0 = 0,05, T = 4000: Geschwindigkeit innerhalb 5 %, Ladung innerhalb 1 % erhalten",
  85 %):
  - Eingetroffen, wenn |v(3800..4000)/v(20..220) - 1| < 0,05 und |Q_ball(4000)/Q_ball(0) - 1| < 0,01.
  - v(a..b) = Sehnen-Steigung ueber die Diagnosepunkte in [a, b].
- **E2-1** (Karte: "Ikosaeder, erster frontaler Durchgang (v0 = 0,05): Austrittsgeschwindigkeit 0,60 bis 0,80 v0, wie
  EINFANG-1 (0,69)", 80 %):
  - Die erste Begegnung des Hauptlaufs muss ein naher Durchgang sein (d_min < 3).
  - Eingetroffen, wenn 0,60 <= v_nach/0,05 <= 0,80. v_nach = Sehnen-Geschwindigkeit der freien Strecke danach.
  - Kein Austritt (keine freie Strecke danach bis T = 8000) oder erste Begegnung kein naher Durchgang: nicht
    eingetroffen.
  - Berichtet wird auch v_nach/v_vor.
- **E2-2** (Karte: "Ikosaeder, v0 = 0,05: Einfang an einer Spitze vor T_end = 8000", 55 %):
  - Eingetroffen, wenn der Hauptlauf bei T = 8000 "eingefangen" ist (Abschnitt 5). Sonst nicht eingetroffen.
  - Erreicht der Lauf T = 8000 nicht: nicht entscheidbar.
- **E2-3** (Karte: "Ueber alle nahen Durchgaenge faellt K im Mittel um >= 30 % je Durchgang; kein Durchgang erhoeht K um
  mehr als 10 %", 60 %):
  - Gewertet werden alle nahen Durchgaenge mit t_min <= 8000 in ik-v0.05 und ik-v0.1, die K davor und K danach haben.
  - Eingetroffen, wenn das arithmetische Mittel von 1 - K_nach/K_vor >= 0,30 ist und jedes K_nach/K_vor <= 1,10.
  - Nicht entscheidbar bei weniger als 2 solchen Durchgaengen.
  - Durchgaenge ohne K danach (Einfang, Laufende) und der Stossparameter-Lauf (Karte: nur berichtet) werden aufgefuehrt,
    gehen aber nicht ein.
  - Berichtet werden auch das geometrische Mittel und die Werte je Lauf.
- **Konvergenz:** Die Proben dt = 0,05 und h = 0,2 werden mit denselben Regeln bewertet (bei E2-3 die Probe statt
  ik-v0.05).
  - Weicht ein Urteil ab, erhaelt es den Vermerk "nicht konvergiert". Das Urteil selbst kommt aus dem Hauptlauf.
  - Verglichen wird auch die Zahl der nahen Durchgaenge bis zum gemeinsamen Ende.

## 8. Beschreibend (nicht gewertet)

- Tabelle aller Begegnungen: t, Spitze, d_min, K davor und danach, Wenden, Atmung, innere Anregung
  E_ball - E_rest(Q_ball) - K.
- Verlaengerung bis T = 16 000, Stossparameter-Lauf, ruhender Ball.
- Bilder: Bahn in 3D, d(t) und K(t) je Lauf (lauf-69/bahn-*.png), K(t) aller Ikosaeder-Laeufe (lauf-69/kt-alle.png).

## 9. Kontrollen

- Netzpruefung je Lauf (Abschnitt 1).
- Energie und Ladung des Gesamtnetzes: max |E_tot(t) - E_tot(0)| und max |Q_tot(t) - Q_tot(0)|.
- **Ruhender Ball:** Drift von d und theta, E_ball, Q_ball.
- **Spiegelsymmetrie der frontalen Laeufe:** Abstand der 3D-Lage von der Spiegelebene durch Startkante und Mittelpunkt.
  - Gewertet nur dort, wo die naechste Spitze auf der Ebene liegt.
  - In Karten anderer Spitzen ist der harmonische Schwerpunkt nicht durch die Symmetrie gebunden. Im Rauchlauf
    (a = 25, Q = 150) war die Abweichung dort 0,044 gegen 5e-12 auf der Ebene; das ist ein Kartenfehler, kein
    Symmetriebruch.
- Torus: Sehnen gegen Gerade, Querdrift.

## 10. Rauchlaeufe vor dem Einfrieren (offengelegt; ihre Parameter kommen in keinem echten Lauf vor)

- **rauch-ik25:** Ikosaeder a = 25 (nu = 84), Q = 150, v = 0,1, T = 700.
  - Erster Durchgang durch Spitze 0 bei t = 100 (d_min 0,32), freie Strecke mit v = 0,0639, zweiter frontaler
    Durchgang bei Spitze 10 (t = 656).
  - **Damit war die Tendenz eines E2-1-artigen Verhaeltnisses (0,64 bei v = 0,1, Q = 150) vor dem Einfrieren sichtbar
    (Selbstanzeige).**
  - Wegen R_trans = 11,5 (a/2 - 1) hatte dieser Start 0,036 Energie zu viel. Bei a = 40 ist R_trans = 19.
- **rauch-torus:** Torus 168 x 194 (h = 25/84), Q = 150, v = 0,15, T = 240. v = 0,14976 (Sehnen und Gerade gleich),
  Querdrift 7e-14.
- **rauch-ik40ruh:** a = 40 (nu = 134), Q = 150, v = 0, T = 100.
  - Ort fest (d = 20 auf 1e-7), E_tot auf 1e-4, Atmung 0,04 %.
  - 3,0 ms je Schritt.
- **rauch-ik200:** a = 40 (nu = 200), Q = 150, v = 0, T = 10; 6,1 ms je Schritt.
- **Auswertung und Bild auf den Rauchdaten** (Spuren cpu und cpu4) als Pipeline-Probe.
