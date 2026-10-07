# EINFANG-2: Ergebnis (Code-Agent fuer claude-primary, Runde 34, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (CUDA, Quadro P4000, float64).
  - Auswertung und Bilder auf der Spur cpu4; cpu2 blieb auf Bitte der Leitung frei.
  - Die .69-Uhr laeuft in UTC; die CEST-Zeiten sind daraus umgerechnet.
- **Plan-Laeufe:** 8 Laeufe von 16:58:51 bis 17:26:02 UTC (18:58:51 bis 19:26:02 CEST), alle rc = 0.
  - Die Probe h = 0,2 lief in 3 Abschnitten, die Probe dt = 0,05 in 2. Nach je 500 s Wandzeit wurde der Zustand
    gespeichert und fortgesetzt. Alle anderen Laeufe brauchten einen Abschnitt; Grenze 600 s.
  - Fruehe Auswertung des fertigen Hauptlaufs um 17:04 UTC (Selbstanzeige 2).
  - Endgueltige Auswertung 17:26:13 bis 17:26:29 UTC, Bilder bis 17:27:11 UTC.
- **Nachtrag:** 2 Laeufe ab 17:29:46 UTC in einem eigenen Ordner. Sie standen nicht im Plan, sind nur beschreibend und
  gehen in kein Urteil ein (Selbstanzeige 3).
- **Eingefroren** um 18:58:44 CEST, vor der ersten echten Rechnung:
  - PLAN.md.eingefroren-20261003-185844
  - code/einfang2.py.eingefroren-20261003-185844 (sha256 beginnt mit 82c3fbd8460457ac; auf der .69 dieselbe Datei)
  - code/laufplan.eingefroren-20261003-185844.tar (Spurskripte, Auswertung)
  - code/kegel_q.py unveraendert aus RUNDE-26 (sha256 beginnt mit 4de64b080729204c)
- **Rohdaten** in lauf-69/:
  - Bahnen und Bilanzen je Lauf (ef2-*.json, alle 2 Zeiteinheiten), Logs
  - auswertung.json mit den mechanischen Urteilen
  - Bilder: bahn-<lauf>.png (Bahn in 3D, Abstand d(t), Bewegungsenergie K(t)) und kt-alle.png
  - Nachtrag: lauf-69/nachtrag/; Rauchlaeufe: rauch-69/
  - Die Felder (Zustandsdateien *.npz) blieben auf der .69 in /home/fmh/fmhc-physics-remote/runde34-einfang2/.
- Geschrieben ab 19:30:54 CEST (date).
- **Einheiten** wie EINFANG-1: Modell M1 in 2D, Masse 1, Q = 200.
  - Ruheenergie E_rest = 157,288 (h = 0,2985), R_halb = 6,26. Bindung an einer Fuenfer-Spitze B = +1,445 (KEGEL-Q).
  - K = (gamma - 1) E_rest: 0,197 bei v = 0,05; 0,791 bei v = 0,1.
  - Spitzenabstand 40 entlang einer Kante, 69,28 ueber zwei Flaechen; Ikosaederflaeche 13 856.

## Ergebnis zuerst

1. **Hauptlauf (v0 = 0,05, frontal): an der dritten Spitze eingefangen, nach zwei Durchgaengen.**
   - Durchgang 1 (Spitze 0, t = 308) wie in EINFANG-1: v 0,04997 -> 0,03449, also 0,690 v0. K faellt von 0,197 auf
     0,094 (-52 %).
   - Durchgang 2 (Spitze 10, t = 1996): K faellt von 0,094 auf 0,0067 (-93 %), danach v = 0,0092.
   - An Spitze 9 bleibt der Ball ab t = 4100 innerhalb 12,26.
     - Bis T = 8000 laeuft er 11-mal durch die Spitze und wendet 10-mal; die Wendeweite sinkt von 10,7 auf 7,9.
     - In der Verlaengerung bis t = 16 000 bleibt er gefangen: 56 Wenden, zuletzt bei etwa 7,3.
   - E2-1 und E2-2 sind eingetroffen.
2. **Der Einfang ist nicht konvergiert. Beide Proben sind bei T = 8000 nicht eingefangen.**
   - In allen drei Fassungen gleich:
     - Durchgang 1: v_nach/v0 = 0,690 / 0,690 / 0,691
     - grosser Verlust in Durchgang 2: K_nach/K_vor = 0,071 / 0,029 / 0,072
     - danach ist der Ball langsamer als die Einfangschwelle aus EINFANG-1 (v ~ 0,011): v = 0,0092 / 0,0059 / 0,0093
   - Was danach geschieht, haengt an dt und h:
     - dt = 0,05: Der Ball haelt an Spitze 9 nur kurz (eine Wende) und entkommt mit v = 0,0038. Bei T = 8000 ist er
       17 von ihr entfernt.
     - h = 0,2: Der Ball wendet schon an Spitze 10 und laeuft mit v = 0,0093 zur Spitze 0 zurueck. Bei T = 8000 ist er
       4,6 vor ihr.
3. **K faellt nicht stetig. E2-3 ist nicht eingetroffen.**
   - Gewertet sind 9 nahe Durchgaenge: 2 aus dem Hauptlauf, 7 aus dem Lauf mit v0 = 0,1.
   - Der mittlere Abfall betraegt 31 %; die Schwelle von 30 % ist knapp erfuellt.
   - Zwei Durchgaenge erhoehen K aber stark: x1,90 (v0 = 0,1, Spitze 10, t = 1210) und x1,70 (Spitze 1, t = 3042).
   - Dabei sinkt jeweils die innere Anregung (0,48 -> 0,20 bzw. 0,43 -> 0,18). Energie fliesst also aus der Atmung in
     die Bewegung zurueck [H].
   - Der Zuwachs an Spitze 10 ist im Nachtrag gegen dt und h stabil (1,898 / 1,911 / 1,902). Der an Spitze 1 betraegt
     mit dt = 0,05 sogar 2,22.
   - **v0 = 0,1:**
     - 7 Begegnungen, alle nahe Durchgaenge.
     - Voruebergehende Haftung an Spitze 10 von t = 4966 bis 6892 mit 2 Wenden; danach tritt der Ball mit K = 0,092
       wieder aus.
     - Bei T = 8000 ist er frei mit K = 0,018 (v = 0,015); kein Einfang.
4. **Stossparameter b = 3,13** (nur berichtet):
   - Die Bahn verlaesst die Spiegelebene und fuehrt an 6 verschiedenen Spitzen vorbei (d_min 0,11 bis 2,2).
   - K_nach/K_vor = 0,58 / 0,88 / 0,60 / 0,76 / 1,26 / 1,32.
   - Bei T = 8000 ist der Ball frei mit K = 0,077.
5. **Kontrollen:**
   - Auf dem Torus bleiben v (auf 3e-5) und Ladung (auf 2e-7) erhalten (E2-0).
   - Der ruhende Ball steht (Drift 8e-7).
   - Die Gesamtladung ist auf 2e-11 erhalten, die Energie auf 2e-3 (dt = 0,1) bzw. 6e-4 (dt = 0,05).
   - Die frontalen Laeufe bleiben auf der Spiegelebene (Hauptlauf 1e-9).

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang (mechanisch nach PLAN.md) |
|---|---|---|
| E2-0 | Torus, v0 = 0,05, T = 4000: Geschwindigkeit innerhalb 5 %, Ladung innerhalb 1 % (85 %) | **eingetroffen**: v(3800..4000)/v(20..220) - 1 = 3,2e-5; Q_ball(4000)/Q_ball(0) - 1 = -2,0e-7; v = 0,049968 (Soll 0,05) |
| E2-1 | Erster frontaler Durchgang (v0 = 0,05): Austritt mit 0,60 bis 0,80 v0 (80 %) | **eingetroffen**: v_nach/v0 = 0,690 (v_nach = 0,03449, v_vor = 0,04997). Proben: 0,690 (dt = 0,05), 0,691 (h = 0,2) |
| E2-2 | v0 = 0,05: Einfang an einer Spitze vor T_end = 8000 (55 %) | **eingetroffen, Vermerk "nicht konvergiert"**: Hauptlauf an Spitze 9 seit t_c = 4100, 10 Wenden. Beide Proben bei T = 8000 nicht eingefangen (Selbstanzeige 4) |
| E2-3 | K faellt im Mittel um >= 30 % je Durchgang; kein Durchgang erhoeht K um mehr als 10 % (60 %) | **nicht eingetroffen**: Mittel 0,306 (erfuellt), groesstes K_nach/K_vor = 1,898 > 1,10 (verletzt), 9 Durchgaenge. Mit den Proben statt des Hauptlaufs dasselbe Urteil (Mittel 0,337 bzw. 0,306; Hoechstwert 1,898) |

- **Ableitbarkeit:**
  - E2-1 war laut Karte eine Kontrolle. Durchgang 1 hat dieselbe Ortsgeometrie wie EINFANG-1: Ankunft entlang einer
    Gitterrichtung, Austritt durch die Mitte der gegenueberliegenden Flaeche. Er trifft EINFANG-1 (0,0343) auf 0,6 %.
  - E2-2 und E2-3 waren offen.
- **E2-3 je Lauf** (beschreibend):
  - Hauptlauf: 2 Durchgaenge, Mittel 0,73
  - v0 = 0,1: 7 Durchgaenge, Mittel 0,19
  - Gesamt: geometrisches Mittel des Abfalls 0,55, also Faktor 0,45 je Durchgang

**Bedeutung (nach Karte):**
- E2-3 ist nicht eingetroffen. Damit gilt der Fall der Karte: "E2-3 trifft nicht ein (Rueckgabe aus der Atmung,
  Wiederaufnahme der Abstrahlung): Die Bremse ist schwaecher als gedacht. Beschreiben."
- **Beschreibung:**
  - **Kein fester Faktor:** Die Bremse wirkt nicht als fester Faktor je Durchgang. Ueber alle 20 auswertbaren
    Begegnungen der Plan-Laeufe (mit Proben und Stossparameter-Lauf) reicht K_nach/K_vor von 0,03 bis 1,90.
  - **Zurueck aus der Atmung:** Was ein Durchgang an Bewegung nimmt, geht vor allem in die innere Anregung (Atmung)
    des Balls. Ein spaeterer Durchgang kann es zurueckgeben. Das zeigen zwei Durchgaenge bei v0 = 0,1 (K steigt, die
    innere Anregung faellt um 0,28 bzw. 0,24) und zwei im Stossparameter-Lauf (x1,26, x1,32) [H].
  - **Haftung mit Wiederaustritt:** dreimal beobachtet. Bei v0 = 0,1 an Spitze 10 mit 2 Wenden, in den Proben
    dt = 0,05 (Spitze 9) und h = 0,2 (Spitze 10) mit je einer Wende.
  - **Abstrahlung:** Der Ball verliert laufend Ladung (Hauptlauf: Q_ball 200 -> 199,35 bis t = 8000, 198,95 bis
    16 000; v0 = 0,1: 198,2). Ob abgestrahlte Wellen den Ball auf der geschlossenen Flaeche spaeter wieder anstossen,
    ist nicht getrennt gemessen.
- **E2-2 trat ein, aber nicht konvergiert:**
  - Nach dem zweiten Durchgang ist der Ball in allen drei Fassungen unter v ~ 0,01. Er wendet danach mindestens einmal
    an einer Spitze: im Hauptlauf an Spitze 9 (gefangen), bei dt = 0,05 an Spitze 9 (wieder frei), bei h = 0,2 an
    Spitze 10 (wieder frei).
  - Ob er bleibt, entscheidet sich nahe der Schwelle und haengt hier an dt und h.
- [H] Auf einer facettierten Kugel koennen Q-Baelle nach wenigen Durchgaengen an einer Spitze haengen bleiben.
  - Im Hauptlauf geschah das nach zwei Durchgaengen und hielt bis t = 16 000.
  - Bei v0 = 0,1 und mit Stossparameter geschah es bis T = 8000 nicht.
  - Der Satz der Karte "Auf einer facettierten Kugel sammeln sich Q-Baelle an den Spitzen, auch wenn sie mit Schwung
    starten" ist damit nicht gestuetzt, nur als moeglicher Ausgang gezeigt.
  - Im Mittel faellt K (geometrisch Faktor 0,45 je Durchgang), aber mit grosser Streuung und mit Rueckgaben.

## Tabelle der nahen Durchgaenge

- Je Begegnung mit einer Spitze (Abstand < 12) mit Mindestabstand d_min < 3.
- t = Zeit des Minimums; bei mehreren Durchgaengen in einer Begegnung das erste bzw. tiefste Minimum.
- K davor/danach aus der Sehnen-Geschwindigkeit der freien Strecke unmittelbar davor bzw. danach (Abstand zu allen
  Spitzen >= 12).

**Hauptlauf ik-v0.05** (dt = 0,1, h = 0,2985):

| Nr | t | Spitze | d_min | K davor | K danach | K_nach/K_vor | v davor | v danach | Bemerkung |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 308 | 0 | 0,11 | 0,1967 | 0,0936 | 0,476 | 0,04997 | 0,03449 | wie EINFANG-1 |
| 2 | 1996 | 10 | 0,11 | 0,0936 | 0,0067 | 0,071 | 0,03449 | 0,0092 | Ladungsverlust des Balls 0,16 (Durchgang 1: 0,025) |
| 3 | 4516 (tiefstes 6524) | 9 | 0,06 | 0,0067 | - | - | 0,0092 | - | eingefangen ab 4100: 11 Durchgaenge, 10 Wenden (10,7 / 9,4 / 8,5 / ... / 7,9) |

**Zusatzlauf ik-v0.1** (dt = 0,1):

| Nr | t | Spitze | d_min | K davor | K danach | K_nach/K_vor | v davor | v danach | Bemerkung |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 172 | 0 | 0,21 | 0,7906 | 0,2589 | 0,327 | 0,0999 | 0,0573 | EINFANG-1: 0,0586 |
| 2 | 1210 | 10 | 0,22 | 0,2589 | 0,4914 | **1,898** | 0,0573 | 0,0789 | innere Anregung 0,48 -> 0,20 |
| 3 | 1628 | 9 | 0,26 | 0,4914 | 0,1354 | 0,276 | 0,0789 | 0,0415 | |
| 4 | 3042 | 1 | 0,16 | 0,1354 | 0,2308 | **1,704** | 0,0415 | 0,0543 | innere Anregung 0,43 -> 0,18 |
| 5 | 3618 | 0 | 0,15 | 0,2308 | 0,1156 | 0,501 | 0,0543 | 0,0384 | |
| 6 | 5140 | 10 | 0,02 | 0,1156 | 0,0920 | 0,796 | 0,0384 | 0,0343 | Haftung 4966 bis 6892: 3 Durchgaenge, 2 Wenden (8,8 / 11,1), dann Austritt |
| 7 | 7550 | 9 | 0,05 | 0,0920 | 0,0178 | 0,194 | 0,0343 | 0,0151 | bei T = 8000 frei |

**Proben des Hauptlaufs** (Konvergenz):

| Groesse | Hauptlauf (dt = 0,1, h = 0,2985) | dt = 0,05 | h = 0,2 (dt = 0,05) |
|---|---|---|---|
| v vor Durchgang 1 | 0,04997 | 0,04994 | 0,04998 |
| Durchgang 1: v_nach/v0; K_nach/K_vor | 0,690; 0,476 | 0,690; 0,476 | 0,691; 0,478 |
| Durchgang 2 (Spitze 10, t = 1996 / 1996 / 1992): K_nach/K_vor | 0,071 | 0,029 | 0,072 |
| v nach Durchgang 2 | 0,0092 (vorwaerts) | 0,0059 (vorwaerts) | 0,0093 (nach einer Wende rueckwaerts, Richtung Spitze 0) |
| danach | Spitze 9 ab 4130, gefangen bis 16 000 | Spitze 9 von 5238 bis 6688 (2 Durchgaenge, 1 Wende bei 9,0), K 0,0027 -> 0,0012, dann frei | Spitze 0 ab 7640, bei T = 8000 d = 4,6 |
| Begegnungen mit nahem Durchgang bis 8000 | 3 | 3 | 2 |
| Einfang bei T = 8000 | ja (Spitze 9) | nein (d = 17 von Spitze 9) | nein |
| Energie, max. Abweichung | 2,2e-3 | 5,8e-4 | 6,1e-4 |

**Stossparameter-Lauf ik-v0.05-b** (b = 3,13, nur berichtet):

| Nr | t | Spitze | d_min | K davor | K danach | K_nach/K_vor |
|---|---|---|---|---|---|---|
| 1 | 316 | 0 | 1,40 | 0,1967 | 0,1142 | 0,580 |
| 2 | 1166 | 5 | 2,22 | 0,1142 | 0,1001 | 0,877 |
| 3 | 2064 | 6 | 0,61 | 0,1001 | 0,0602 | 0,601 |
| 4 | 5508 | 3 | 1,10 | 0,0602 | 0,0459 | 0,762 |
| 5 | 6716 | 1 | 0,48 | 0,0459 | 0,0579 | 1,262 |
| 6 | 7748 | 2 | 0,11 | 0,0579 | 0,0767 | 1,324 |

- d_min ist der harmonische Abstand; nahe der Spitze ist er eine Reaktionskoordinate.
- Der seitliche erste Durchgang kostet weniger als der frontale (K-Verhaeltnis 0,58 gegen 0,48), wie die Karte
  erwartet.
- Alle sechs Begegnungen dieses Laufs waren nah (d_min < 3), obwohl die Bahn die Spiegelebene verlaesst. [H] Die
  Fuenfer-Spitzen lenken vorbeilaufende Baelle zu sich hin; geprueft ist das nicht.

**Freie Strecken des Hauptlaufs** (beschreibend):

| Strecke | v | K | Q_ball | innere Anregung | Atmung (halbe Spanne von max abs(phi)^2) |
|---|---|---|---|---|---|
| 20 bis 160 | 0,04997 | 0,1967 | 199,9996 | 3e-5 | 0,04 % |
| 494 bis 1806 | 0,03449 | 0,0936 | 199,9749 | 0,096 (EINFANG-1: 0,099) | 1,3 % (EINFANG-1: 1,3 %) |
| 2402 bis 4128 | 0,0092 | 0,0067 | 199,8110 | 0,131 | 2,1 % |

## Nachtrag (nicht im Plan, nur beschreibend)

- **Laeufe:** 17:29:46 bis 17:34:09 UTC, je ein Abschnitt (263 s), Ordner lauf-69/nachtrag/.
  - ik-v0.1-dt0.05: h = 0,2985, dt = 0,05, bis T = 4000, Spur p4000a
  - ik-v0.1-h0.2: h = 0,2, dt = 0,05, bis T = 2000, Spur p4000b
  - Eigene Auswertung (lauf-69/nachtrag/auswertung.json). Die Urteile dort sind leer, es zaehlen nur die Laufanalysen.
- **K_nach/K_vor bei v0 = 0,1:**

| Durchgang | Plan-Lauf (dt = 0,1, h = 0,2985) | dt = 0,05 | h = 0,2 |
|---|---|---|---|
| 1, Spitze 0 (t = 172) | 0,327 | 0,328 | 0,328 |
| 2, Spitze 10 (t = 1210) | **1,898** | **1,911** | **1,902** |
| 3, Spitze 9 (t = 1628) | 0,276 | 0,271 | 0,280 |
| 4, Spitze 1 (t = 3042 / 3044) | **1,704** | **2,220** | (T = 2000 erreicht) |
| 5, Spitze 0 (t = 3618 / 3564) | 0,501 | 0,404 | |

- Die innere Anregung faellt in Durchgang 2 in allen drei Fassungen gleich: von 0,481 / 0,480 / 0,480 auf 0,201 /
  0,198 / 0,198.
- **Lesart:**
  - Der K-Zuwachs an Spitze 10 ist gegen dt und h stabil (auf 0,7 %).
  - Der Zuwachs an Spitze 1 ist in der Groesse nicht konvergiert (1,70 gegen 2,22), liegt aber in beiden Fassungen
    ueber 1,10.
  - Das Scheitern von E2-3 haengt also nicht an der Numerik. Die Urteile bleiben unveraendert, denn der Nachtrag geht
    in keines ein.

## Kontrollen

- **Torus (E2-0)**, 335 x 536, gleiche Flaeche und gleiches h:
  - v = 0,0499680 (20..220) und 0,0499696 (3800..4000), Ladung im Ball -2,0e-7, Querdrift 2,5e-10.
  - Atmung 0,06 %; Energie auf 1,3e-4.
  - **Pruefung des Sehnenverfahrens:** Sehnen gegen Ausgleichsgerade von x(t): 0,0499680 gegen 0,0499679 bzw.
    0,0499696 gegen 0,0499692.
- **Ruhender Ball** (ik-v0, T = 1000, Kantenmitte):
  - Abstand zu Spitze 0 fest auf 8e-7, Richtung auf 1e-12.
  - E_ball auf 9e-7 und Q_ball auf 6e-7 relativ.
  - Atmung 0,06 % (Startabweichung durch den Zeitschritt, wie EINFANG-1).
- **Start:** Die Uebertragung des Flickenballs passt aufs Gitter (Rundungsfehler der Gitterkoordinaten 1e-13).
  - Laborladung 199,999998.
  - K_eff = 0,19672 gegen den Nennwert 0,19698 (-0,13 %, fehlende Lorentz-Kontraktion wie EINFANG-1).
  - Die gemessene Startgeschwindigkeit 0,04997 geht in die Urteile ein.
- **Netzpruefung** (jeder Lauf):
  - 179 562 Knoten (h = 0,2985) bzw. 400 002 (h = 0,2), also 10 nu^2 + 2
  - 12 Knoten mit Grad 5, alle anderen Grad 6; Euler 2; jede Kante in genau zwei Dreiecken
  - Winkeldefekt nur an den 12 Spitzen (Rest < 5e-14)
  - Gewichte 1/sqrt 3 auf 1e-13; Spitzenflaeche 5/6 der regulaeren Flaeche
  - Flaeche 13 856,41 (Soll 5 sqrt 3 a^2)
  - Torus: Euler 0, alle Grad 6, gleiche Flaeche
- **Erhaltung:**
  - Gesamtladung in allen Laeufen auf <= 1,8e-11.
  - Gesamtenergie (Verlet-Schwankung): 2,2e-3 (Hauptlauf), 3,1e-3 (v0 = 0,1), 2,0e-3 (Stossparameter), 5,8e-4
    (dt = 0,05), 6,1e-4 (h = 0,2), 1,2e-4 bzw. 1,3e-4 (ruhender Ball, Torus).
  - Ohne Schwamm bleibt die abgestrahlte Energie im Netz.
- **Spiegelsymmetrie der frontalen Laeufe** (Abstand der 3D-Lage von der Ebene durch Startkante und Mittelpunkt, nur
  in Karten von Spitzen auf der Ebene: 0, 1, 9, 10):
  - Hauptlauf 1,2e-9, dt = 0,05 1,6e-9, h = 0,2 2,6e-5, v0 = 0,1 5,3e-5, ruhender Ball 2e-11.
  - Alle Karten zusammen: bis 0,02 bzw. 0,04. Das ist der Kartenfehler des harmonischen Schwerpunkts bei Spitzen
    neben der Ebene (Selbstanzeige 7).
- Die Bahn folgt der Schreibtischrechnung: Spitzen 0 -> 10 -> 9 -> 1 -> 0, abwechselnd ueber zwei Flaechen (69,3) und
  entlang einer Kante (40). Der Lauf mit v0 = 0,1 hat die geschlossene Runde einmal ganz durchlaufen.

## Latten (v3)

- **L1: ja.**
  - E2-3 konnte scheitern und ist gescheitert.
  - E2-2 konnte scheitern; es ist im Hauptlauf eingetroffen und in beiden Proben nicht.
  - E2-0 und E2-1 konnten scheitern.
- **L2: ja.**
  - Zwei Proben des Hauptlaufs (dt, h). Sie stimmen fuer Durchgang 1 und den Verlust in Durchgang 2 und widersprechen
    beim Einfang; das ist ein Befund.
  - Torus, ruhender Ball, Spiegelsymmetrie, Ladungserhaltung.
  - Nachtrag fuer den Lauf mit v0 = 0,1.
- **L3: teilweise.**
  - Durchgang 1 ist auf 0,3 % konvergiert (v_nach).
  - Der Verlust in Durchgang 2 betraegt in allen Fassungen 93 bis 97 % von K.
  - Der K-Zuwachs bei v0 = 0,1 an Spitze 10 ist auf 0,7 % konvergiert (Nachtrag).
  - Der Ausgang danach ist nicht konvergiert. Der Ball ist dann so langsam (K 0,003 bis 0,007), dass die Verlet-
    Schwankung der Energie (6e-4 bis 2e-3) und Gitterunterschiede gegen K nicht mehr klein sind.
- **L4: teilweise.**
  - Bekannt ist [L?, aus dem Gedaechtnis, nicht nachgelesen]:
    - Solitonen und Kinks tauschen beim Stoss mit Stoerstellen oder miteinander Energie mit inneren Moden. Es gibt
      Einfang, Wiederaustritt nach mehreren Pendeln (Resonanzfenster) und Rueckgabe gespeicherter Energie.
    - Quellen: Campbell, Schonfeld und Wingate 1983 (phi^4-Kink-Antikink); Fei, Kivshar und Vazquez 1992 (Kink an
      Stoerstelle); Goodman, Holmes und Weinstein 2004 (NLS-Soliton an Delta-Defekt).
  - Die Haftung mit Wiederaustritt (v0 = 0,1 an Spitze 10, Proben dt = 0,05 und h = 0,2) und die K-Zuwaechse passen
    dazu [H].
  - Fuer 2D-Q-Baelle auf einer Flaeche mit vielen Kegelspitzen wurde nicht gesucht.
- **L5: nein.**
  - Moegliche Analogien [H]: Defekte in Kristallgittern (Disklinationen), Teilchen auf facettierten Kapseln oder
    Fullerenen, Haftung von Wirbeln an Fehlstellen.
  - Kein Messbezug.

## Selbstanzeigen

1. **Rauchlauf vor dem Einfrieren** (a = 25, Q = 150, v = 0,1) zeigte ein Austrittsverhaeltnis von 0,64 im ersten
   Durchgang. Offengelegt im Plan, Abschnitt 10.
2. **Fruehe Auswertung** des fertigen Hauptlaufs um 17:04 UTC, waehrend die anderen Laeufe rechneten.
   - Danach wurde nichts an Plan, Code oder Laufliste geaendert.
   - Die endgueltige Auswertung lief mit demselben Code ueber alle Laeufe.
3. **Nachtrag ausserhalb des Plans** (nach Sicht auf die Auswertung beschlossen):
   - v0 = 0,1 mit dt = 0,05 (bis T = 4000) und mit h = 0,2 (bis T = 2000).
   - Anlass: Die Durchgaenge, an denen E2-3 scheitert, liegen im Lauf mit v0 = 0,1, und der Plan sah fuer diesen Lauf
     keine Probe vor.
   - Eigenes Skript (code/laufplan/spur-nachtrag.sh, nicht im eingefrorenen tar), eigener Ordner, kein Einfluss auf
     die Urteile.
4. **Der Vermerk-Text** in auswertung.json nennt nur die Probe h = 0,2, weil die Schleife den Text ueberschreibt.
   Tatsaechlich haben beide Proben ein anderes E2-2-Urteil (siehe urteile.E2-2.proben).
5. **E2-3 haengt an Durchgaengen des Laufs mit v0 = 0,1.** Fuer diesen Lauf sah der Plan keine Probe vor (siehe
   Nachtrag). Die Lesart der Karte, Hauptlauf und v0 = 0,1 zusammen zu werten, steht im Plan; der Stossparameter-Lauf
   ist laut Karte nur berichtet.
6. **Festlegungen im Plan, nicht aus der Karte:**
   - Wende mit Hysterese 2; freie Strecke ab Abstand 12; Abdeckung 1e-6; Sehnen ueber 10 Zeiteinheiten
   - Einfanggrenze R_halb + 6 = 12,2551 statt gerundet 12,3
   - Alle Festlegungen standen vor der Rechnung fest.
7. **Kartenfehler:**
   - Der harmonische Schwerpunkt ist exakt nur fuer runde Baelle. In Karten von Spitzen neben der Spiegelebene weicht
     die Lage um bis zu 0,02 (Hauptlauf) bzw. 0,04 (v0 = 0,1) ab.
   - Das stoert die Sehnen nur wenig; es aendert keinen Durchgang.
8. **Bei kleinen Geschwindigkeiten** (v <= 0,006) schwankt die lokale Geschwindigkeit ueber 40 Zeiteinheiten um bis
   zu 25 %, weil der Schwerpunkt mit der Atmung wackelt.
   - Die Streckenwerte sind Ausgleichsgeraden ueber 650 bis 2450 Punkte; ihre Unsicherheit ist dort trotzdem groesser
     als bei schnellen Strecken.
9. **Energieschwankung bei dt = 0,1** (2,2e-3) ist ein Drittel von K nach Durchgang 2 (0,0067). Das passt dazu, dass
   die Probe dt = 0,05 dort abweicht.
10. **Deutungen sind nachtraeglich und nicht vorhergesagt [H]:** Rueckgabe aus der Atmung, Haftung mit Wiederaustritt,
    Empfindlichkeit nahe der Schwelle.
11. Ein schwacher globaler Schwamm als Vergleich (im Auftrag optional) wurde nicht gerechnet.
12. **Uhrzeiten** stammen aus den Logs der .69 (UTC); CEST ist umgerechnet.

## Einfach gesagt

Wir haben einen Q-Ball, einen Feldklumpen wie ein Tropfen, ueber die Oberflaeche eines Zwanzigflaechners rollen
lassen, die nur an ihren 12 Ecken Mulden hat. An der ersten Ecke verliert er wie im Vorversuch die Haelfte seiner
Bewegungsenergie, an der zweiten sogar 93 %, und im Hauptlauf bleibt er dann an der dritten Ecke haengen und pendelt
dort. Mit kleinerem Zeitschritt oder feinerem Netz verliert er genauso viel, bleibt danach aber nicht oder nur kurz
haengen; das "gefangen" ist also nicht sicher. Ausserdem bremst nicht jede Ecke: Den schnelleren Ball haben zwei
Ecken sogar wieder beschleunigt, weil sein Zittern zurueck in Bewegung ging. Die Ecken bremsen also im Mittel, aber
sehr unregelmaessig.
