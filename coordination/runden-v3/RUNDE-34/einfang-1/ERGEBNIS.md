# EINFANG-1: Ergebnis (Code-Agent fuer claude-primary, Runde 34, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (CUDA, Quadro P4000, float64). Auswertung und
  Bild liefen auf der Spur cpu. Die .69-Uhr laeuft in UTC.
  - **Plan-Laeufe:** 9 Laeufe und 2 beschreibende Laeufe von 16:06:50 bis 16:12:42 UTC (18:06:50 bis 18:12:42 CEST).
    Erste Auswertung um 16:12:53 UTC.
  - **Nachtrag:** 4 Laeufe von 16:12:31 bis 16:16:21 UTC, nicht im Plan, nur beschreibend (Selbstanzeige 2).
  - **Endgueltige Auswertung** 16:16:30 UTC (gleiche Urteile wie die erste), Bild 16:16:31 UTC, Nachtragsbild
    16:17:37 UTC.
  - Alle rc = 0. Der laengste Lauf dauerte 217 s (h = 0,2; Grenze 600 s); keine Fortsetzung noetig.
- **Eingefroren** um 18:06:44 CEST, vor der ersten echten Rechnung:
  - PLAN.md.eingefroren-20261003-180644
  - code/einfang.py.eingefroren-20261003-180644 (sha256 beginnt mit 5ae493bf3e97b326)
  - code/laufplan.eingefroren-20261003-180644.tar (Spurskripte)
  - code/kegel_q.py unveraendert aus RUNDE-26 (sha256 beginnt mit 4de64b080729204c)
- **Rohdaten:** lauf-69/
  - Bahnen und Bilanzen je Lauf (ef-*.json, alle 2 Zeiteinheiten), Logs
  - auswertung.json mit den mechanischen Urteilen
  - bahnen.png (Plan-Laeufe); bahnen-schwelle.png (v = 0,01 eingefangen, v = 0,02, Siebener-Ecke; nachtraeglich)
  - Rauchlaeufe: rauch-69/. Felddumps gab es keine.
- Geschrieben ab 18:15:10 CEST (date).
- **Einheiten:** Modell M1 in 2D, Masse 1. Q = 200 heisst:
  - Ruheenergie 157,288 (Netz h = 0,3), R_half = 6,26
  - Bindung B = +1,445 (Fuenfer-Ecke) bzw. -1,337 (Siebener-Ecke) bei h = 0,3, R_c = R_half + 3 = 9,26
  - K = (gamma - 1) E_rest: 0,0314 / 0,197 / 0,791 bei v = 0,02 / 0,05 / 0,1

## Ergebnis zuerst

1. **Bei v = 0,02, 0,05 und 0,1 faengt die Fuenfer-Ecke den Ball nicht ein.**
   - Der Ball faellt in die Mulde, laeuft durch die Spitze und verlaesst sie auf dem Gegenstrahl.
   - Austrittsgeschwindigkeit 0,0148 / 0,0343 / 0,0586, also 74 / 69 / 59 % von v.
   - EF2 ist nicht eingetroffen. Beide Konvergenzproben (dt = 0,05 und h = 0,2) geben denselben Ausgang, v_aus auf
     0,6 % und den Verlust auf 1,1 %.
2. **Der Durchgang ist stark unelastisch.**
   - Verlust je Durchgang Delta K = 0,0143 / 0,041 / 0,104 / 0,520 bei v = 0,02 / 0,035 / 0,05 / 0,1, also 45 / 42 / 53 /
     66 % von K.
   - 92 bis 95 % davon bleiben als innere Anregung im Ball. Er atmet danach mit Periode ~28.
     - max |phi|^2 schwingt um +-0,6 / 0,9 / 1,3 / 2,6 % bei v = 0,02 / 0,035 / 0,05 / 0,1.
     - Unterhalb v = 0,02 bleibt es bei etwa +-0,5 %.
   - Abgestrahlt werden bei v = 0,02 bis 0,1 Energie 0,003 bis 0,096 und Ladung 0,003 bis 0,090 (der Ball hat
     Ladung 200).
3. **Eingefangen wird erst unterhalb v ~ 0,011** (beschreibend und Nachtrag).
   - Bei v = 0,01 kehrt der Ball nach dem ersten Durchgang bei x = 10,8 um. Bis t = 3200 pendelt er weiter in der
     Mulde: fuenf Durchgaenge, Umkehrpunkte 10,8 / -9,0 / 8,6 / -8,6.
   - Mit dt = 0,05 (Nachtrag) ebenso: erste Umkehr bei 10,78. Die spaeteren Umkehrpunkte weichen ab (-9,7 / 8,9 / -8,5).
   - Bei v = 0,0125 / 0,015 / 0,0175 laeuft er durch, mit v_aus = 0,0057 / 0,0094 / 0,0120.
   - Der Verlust hat bei kleinem v einen Boden: 0,009 / 0,0097 / 0,0108 / 0,0127 / 0,0143 bei v = 0,01 / 0,0125 /
     0,015 / 0,0175 / 0,02.
   - K = 0,0079 / 0,0123 / 0,0177 / 0,0241 / 0,0314 faellt wie v^2 unter diesen Boden. Die Schwelle K = Verlust liegt
     bei v ~ 0,011.
4. **Siebener-Ecke: zurueckgeworfen vor der Spitze (EF3), praktisch elastisch.**
   - v_aus/v_ein = 0,9994, Delta K = 2,3e-4 (0,1 % von K), keine Atmung.
   - Umkehr im Abstand 6,21 von der Spitze. Das statische Potential aus KEGEL-Q liegt dort zwischen 0,189 und 0,204
     (zwei Interpolationen), K = 0,197.
5. **Kontrollen:**
   - Auf dem ebenen Netz laeuft der Ball mit v = 0,04997 ungebremst (EF0).
   - Der ruhende Ball steht (Drift 1e-4).
   - Energiebilanz mit Schwamm auf <= 2e-3 (dt = 0,1) bzw. 2,6e-4 (dt = 0,05); Ladungsbilanz auf 4e-12 (Rundung).
   - Der Ball bleibt auf der Spiegelachse (|Im W| <= 5e-10).

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang (mechanisch nach PLAN.md) |
|---|---|---|
| EF0 | Ohne Defekt, v = 0,05: Geschwindigkeit nach t = 400 auf 5 %, Ladung auf 1 % erhalten (85 %) | **eingetroffen**: v(350..450)/v(20..120) - 1 = -1,5e-5; Q_ball(400)/Q_ball(0) - 1 = -2,1e-7. Gemessen v = 0,04997 (Soll 0,05) |
| EF1 | Fuenfer-Ecke, v = 0,1 und 0,05: kein Einfang (70 %) | **eingetroffen**: beide "durchgelaufen", Austritt bei t = 294 bzw. 516, v_aus = 0,0586 bzw. 0,0343 |
| EF2 | Fuenfer-Ecke, v = 0,02: Einfang (40 %) | **nicht eingetroffen**: "durchgelaufen", Austritt bei t = 1046, v_aus = 0,0148. Verlust 0,0143 < K = 0,0314. Konvergenzproben gleicher Ausgang (dt = 0,05: v_aus = 0,01468; h = 0,2: 0,01473) |
| EF3 | Siebener-Ecke, v = 0,05: zurueckgeworfen (90 %) | **eingetroffen**: "zurueckgeworfen", x bleibt < 0, naechste Annaeherung 6,21 an die Spitze, Rueckweg mit v = 0,04994 |

- **Ableitbarkeit:**
  - EF3 folgt nach der Karte aus Energieerhaltung und KEGEL-Q. Geprueft wurde, ob die Dynamik das traegt (sie tut es
    praktisch verlustfrei).
  - EF1 war nach der Karte nahezu ableitbar; tatsaechlich sind die Verluste nicht klein, sondern 53 bis 66 % von K.
  - EF2 war offen und ist gescheitert.

**Bedeutung (nach Karte, Fall "EF2 trifft nicht ein"):**
- Karte: "Die Haftung ist bei diesen Geschwindigkeiten rein statisch. Einfang braucht dann zusaetzliche Reibung.
  Beschreiben, wie gross der Verlust je Durchgang war."
- **Verlust je Durchgang:** 42 bis 66 % von K zwischen v = 0,02 und 0,1 (kleinster Anteil bei v ~ 0,02 bis 0,035;
  Tabelle unten). Er geht fast ganz in Atmung des Balls, nur zu 5 bis 8 % netto in Abstrahlung.
- **Einschraenkungen dieser Lesart:**
  - "Rein statisch" stimmt nur fuer den Ausgang. Der Durchgang selbst ist stark unelastisch; der Verlust waechst bei
    groesserem v etwa wie K mit.
  - Unterhalb v ~ 0,011 faengt die Fuenfer-Ecke den Ball doch ein (beschreibend bzw. Nachtrag, nicht gewertet). EF2 lag
    also nur um einen Faktor ~2 in v neben der Schwelle.
  - [H] Auf einer Dreieckskugel mit 12 Spitzen wuerden langsame Q-Baelle (v < ~0,011 bei Q = 200) an Spitzen haengen
    bleiben. Schnellere verlieren an jeder Spitze 42 bis 79 % von K, bis sie unter die Schwelle fallen.
    - Gemessen ist das nur fuer 0,0125 <= v <= 0,1 und Stossparameter 0.
    - Die Atmungsenergie, die sie mitnehmen, kann bei spaeteren Durchgaengen wieder in Bewegung zurueckfliessen (siehe
      die gleich hohen Umkehrpunkte 8,62 und 8,61 bei v = 0,01).

## Tabelle je Lauf

- Austrittsgeschwindigkeit v_aus: Steigung von |x|(t) fuer |x| >= 12 nach dem Austritt.
- Verlust Delta K = K_ein - K_aus mit K = (gamma - 1) E_rest(Q_ball); in Klammern Delta K/K_ein.
- **Innere Anregung** = E_ball - E_rest(Q_ball) - K nach dem Durchgang (davor <= 4e-5).
- Delta Q_ball: Ladungsverlust des Balls zwischen den Geschwindigkeitsfenstern (Ballscheibe Radius 15).
- **Atmung** = halbe Spanne von max |phi|^2 nach dem Durchgang; vorher 0,04 %.

| Lauf | v | Defekt | Ausgang | v_aus | Verlust Delta K | Innere Anregung | Delta E_ball | Ladungsverlust Delta Q_ball | Atmung |
|---|---|---|---|---|---|---|---|---|---|
| f5-v0.1 | 0,1 | Fuenfer | durchgelaufen | 0,0586 | 0,520 (66 %) | 0,492 | 0,096 | 0,090 | +-2,6 % |
| f5-v0.05 | 0,05 | Fuenfer | durchgelaufen | 0,0343 | 0,104 (53 %) | 0,099 | 0,018 | 0,017 | +-1,3 % |
| f5-v0.035 (beschr.) | 0,035 | Fuenfer | durchgelaufen | 0,0265 | 0,041 (42 %) | 0,039 | 0,0072 | 0,0069 | +-0,9 % |
| f5-v0.02 | 0,02 | Fuenfer | durchgelaufen | 0,0148 | 0,0143 (45 %) | 0,0134 | 0,0030 | 0,0029 | +-0,6 % |
| f5-v0.02-dt0.05 | 0,02 | Fuenfer | durchgelaufen | 0,0147 | 0,0144 (46 %) | 0,0136 | 0,0031 | 0,0030 | +-0,6 % |
| f5-v0.02-h0.2 | 0,02 | Fuenfer | durchgelaufen | 0,0147 | 0,0144 (46 %) | 0,0135 | 0,0031 | 0,0030 | +-0,6 % |
| f5-v0.0175 (Nachtrag, d0 = 16) | 0,0175 | Fuenfer | durchgelaufen | 0,0120 | 0,0127 (53 %) | 0,0118 | 0,0030 | 0,0029 | +-0,5 % |
| f5-v0.015 (Nachtrag, d0 = 16) | 0,015 | Fuenfer | durchgelaufen | 0,0094 | 0,0108 (61 %) | 0,0101 | 0,0026 | 0,0025 | +-0,5 % |
| f5-v0.0125 (Nachtrag, d0 = 16) | 0,0125 | Fuenfer | durchgelaufen | 0,0057 | 0,0097 (79 %) | 0,0090 | 0,0025 | 0,0024 | +-0,5 % |
| f5-v0.01 (beschr., d0 = 16) | 0,01 | Fuenfer | **eingefangen** (Umkehr bei 10,77; Etikett siehe Selbstanzeige 3) | - | ~0,0090 im 1. Durchgang (114 %) | - | - | - | +-1,5 % (ganzer Lauf) |
| f5-v0.01-dt0.05 (Nachtrag) | 0,01 | Fuenfer | **eingefangen** (Umkehr bei 10,78) | - | ~0,0090 im 1. Durchgang | - | - | - | +-1,0 % (ganzer Lauf) |
| s7-v0.05 | 0,05 | Siebener | zurueckgeworfen | 0,0499 | 0,00023 (0,1 %) | 0,00026 | 1e-5 | 6e-6 | keine |
| e6-v0.05 | 0,05 | keiner | durchgelaufen | 0,0500 | -3e-6 | 3e-5 | 1e-5 | 5e-6 | keine |

- **Bei v = 0,01** kommt der Verlust des ersten Durchgangs aus dem Umkehrpunkt: K_ein - V(10,77) = 0,0079 + 0,0011.
  V(d) ist das statische Potential aus KEGEL-Q (h = 0,3), interpoliert zwischen d = 9,6 und 10,8.
  - Die Umkehrpunkte danach liegen bei -9,02 / 8,62 / -8,61, also V = -0,014 / -0,025 / -0,026.
  - Der Verlust je Durchgang ist dann 0,013 / 0,011 / unter 0,001 (Interpolation des Potentials auf etwa 2 %). Er
    schwankt also stark; zwischen dem dritten und vierten Umkehrpunkt fliesst Atmungsenergie praktisch vollstaendig in
    Bewegung zurueck.
  - Die Umkehrpunkt-Energien zaehlen nur Bewegung plus Lage, nicht die Atmung.
- Abgestrahlte Energie bis Laufende (Schwamm plus unterwegs): 0,0038 (v = 0,02), 0,021 (0,05), 0,129 (0,1); bei v = 0,01
  0,041 ueber fuenf Durchgaenge.

## Kontrollen

- **Ruhender Ball** (e6-v0, Q = 200, T = 300): Ort fest auf 9,8e-5, E_ball auf 9e-7 und Q_ball auf 3e-7 relativ.
  - max |phi|^2 schwankt um 0,06 %. Das ist die Startabweichung durch den Zeitschritt.
- **Ohne Schwamm** (e6-v0.05-ohne, T = 300): Energie erhalten auf 1,3e-4 (bei E = 157,5), Ladung exakt (Verlet erhaelt
  die U(1)-Ladung).
- **Energiebilanz mit Schwamm**, max |E_tot + E_damp - E_tot(0)|:
  - 1,2e-4 bis 1,5e-4 ohne Durchgang (eben, Siebener-Ecke)
  - 1e-3 bis 2e-3 an der Fuenfer-Ecke bei dt = 0,1 (der klingende Ball verstaerkt die Verlet-Schwankung)
  - 2,6e-4 bei dt = 0,05 und bei h = 0,2
  - Ladungsbilanz in allen Laeufen auf <= 3,6e-12 (Rundung).
- **Konvergenz** (f5-v0.02):

  | Probe | v_aus | Delta K | Austritt |
  |---|---|---|---|
  | h = 0,3, dt = 0,1 | 0,014767 | 0,014281 | t = 1046 |
  | h = 0,3, dt = 0,05 | 0,014681 | 0,014443 | t = 1048 |
  | h = 0,2, dt = 0,05 | 0,014729 | 0,014380 | t = 1046 |

  - Die Unterschiede (0,6 % in v_aus, 1,1 % im Verlust) sind klein gegen den Abstand zur Schwelle (K_aus = 0,017 > 0).
  - Der Zeitschritt wirkt staerker als die Gitterweite.
- **Siebener-Ecke gegen Statik:** Die Umkehr liegt bei d = 6,21 (x_S, Definition von KEGEL-Q).
  - Das statische Potential auf dem 1,2-Raster gibt dort 0,204 (linear interpoliert, obere Schranke, weil V konvex
    ist) bzw. 0,189 (exponentiell interpoliert, untere Schranke, weil ln V dort konkav ist). K_ein = 0,197 liegt
    dazwischen.
  - Die Statik von KEGEL-Q traegt also die Dynamik am abstossenden Defekt.
- **Mitlaufende Kontrollen:**
  - Spiegelsymmetrie: |Im W| <= 5e-10 in allen Laeufen.
  - Start: Laborladung exakt 200; K_eff = E(0) - E_rest liegt 0,1 bis 0,2 % unter (gamma - 1) E_rest (fehlende
    Lorentz-Kontraktion).
  - Startstrahlung (Zeitschritt und Boost) bis zum Eintritt: 3e-5 bis 6e-5, bei v = 0,1 2e-4.
- **Netzpruefung** je Lauf: genau eine Spitze vom Grad 5 bzw. 7, Defekt +-pi/3, Euler-Charakteristik 1
  (120 876 / 145 051 / 169 226 Ecken fuer n = 5 / 6 / 7 bei h = 0,3; 272 056 fuer n = 5 bei h = 0,2).

## Latten (v3)

- **L1: ja.** EF2 konnte scheitern und ist gescheitert. EF0, EF1 und EF3 konnten scheitern (EF1 haette bei Verlusten
  ueber K ebenfalls scheitern koennen).
- **L2: ja.**
  - Zwei Konvergenzproben mit demselben Ausgang.
  - Siebener-Umkehrpunkt gegen das statische Potential.
  - Energiebilanz mit gezaehltem Schwammverlust.
  - Ebene Kontrolle, Lauf ohne Schwamm, ruhender Ball.
- **L3: ja.** CFL-Probe, Energieerhaltung, v_aus auf 0,6 % und Verlust auf 1,1 % zwischen dt und h; Ladung exakt.
- **L4: teilweise.**
  - Einfang eines Solitons durch einen anziehenden Defekt unterhalb einer kritischen Geschwindigkeit ist in 1D bekannt.
    Oberhalb laeuft es mit verringerter Geschwindigkeit durch; Energie geht in Defekt- bzw. innere Moden und Strahlung,
    mit Resonanzfenstern. [L?, aus dem Gedaechtnis, nicht nachgelesen: Fei, Kivshar und Vazquez 1992 (Sinus-Gordon-Kink
    an Stoerstelle); Goodman, Holmes und Weinstein 2004, Physica D (NLS-Soliton an Delta-Defekt); Cao und Malomed 1995]
  - Fuer einen 2D-Q-Ball an einer Kegelspitze (Kruemmungsdefekt) ist die Dynamik hier gerechnet. Ob sie bekannt ist,
    wurde nicht gesucht.
- **L5: nein.** Moegliche Analogien [H]: Tropfen oder Solitonen auf Kegeln und facettierten Flaechen, Haftung von
  Wirbeln oder Skyrmionen an Defekten. Kein Messbezug.

## Selbstanzeigen

1. **Rauchlauf vor dem Einfrieren** (n = 6, h = 0,35, Q = 150, v = 0,15) zeigte die Tendenz von EF0: v = 0,1497,
   Ladung erhalten. Offengelegt im Plan, Abschnitt 7.
2. **Nachtrag ausserhalb des Plans:**
   - Nach Sicht auf den beschreibenden Lauf f5-v0.01 (Einfang) habe ich vier weitere Laeufe beschlossen und gerechnet:
     v = 0,0125, 0,015, 0,0175 (d0 = 16) und v = 0,01 mit dt = 0,05.
   - Sie sind nur beschreibend, gehen in kein Urteil ein und stehen getrennt im Skript code/laufplan/spur-nachtrag.sh.
   - Ebenso nachtraeglich: die Umkehrpunkt-Verluste bei v = 0,01 (mit jq aus den Bahnen gelesen, Potential von Hand
     interpoliert) und die Atmungsspannen (jq).
   - code/laufplan/spur-beschreibend.sh entstand erst nach dem Einfrieren (18:08 CEST). Es fuehrt genau die zwei im
     Plan genannten beschreibenden Laeufe aus (f5-v0.035, f5-v0.01) und steht nicht im eingefrorenen tar.
3. **Die Einfang-Definition der Karte (R_c = R_half + 3) ist zu eng.**
   - Bei v = 0,01 kehrte der Ball erst bei x = 10,77 > R_c = 9,26 um. Dort ist das statische Potential noch 1,1e-3,
     also 14 % von K.
   - Das mechanische Etikett von f5-v0.01 in auswertung.json lautet deshalb "durchgelaufen", obwohl der Ball gebunden
     bleibt.
   - Die gewerteten Laeufe (v >= 0,02) betrifft das nicht: Sie erreichten |x| = 24 mit konstanter Geschwindigkeit.
4. **Energiebilanz bei dt = 0,1** nur auf 1e-3 bis 2e-3, bei v = 0,02 also 7 % des Verlusts.
   - Der Verlust selbst kommt aus den Geschwindigkeiten und ist mit dt = 0,05 (Bilanz 2,6e-4) auf 1,1 % bestaetigt.
5. **Innere Anregung ist ein Rest** (E_ball - E_rest - K) und haengt an v_aus. Unabhaengig gestuetzt ist sie nur
   qualitativ durch die Atmung (max |phi|^2) und die ebene Kontrolle ohne Verlust.
6. **Deutungen sind nachtraeglich und nicht vorhergesagt [H]:** Atmung mit Boden (~0,5 %) und Anstieg mit v, Boden
   des Verlusts bei kleinem v, Rueckfluss der Atmungsenergie.
   - Die Einfangschwelle v ~ 0,011 ist aus fuenf Laeufen interpoliert (0,01 gefangen, 0,0125 frei), nicht gerechnet.
   - Gefangen heisst hier: bis t = 3200 gebunden (fuenf bzw. vier Durchgaenge), nicht fuer immer.
7. **Start ohne Lorentz-Kontraktion**, d_X f aus dem Kontinuumsprofil. K_eff liegt 0,1 bis 0,2 % unter dem
   Nennwert; die Urteile nutzen das gemessene v_ein.
8. **Uhrzeiten:** Die Laufzeiten stammen aus den Logs der .69 (UTC); die Zeiten in CEST sind daraus umgerechnet.

## Einfach gesagt

Wir haben einen Q-Ball, einen Feldklumpen wie ein Wassertropfen, langsam auf eine Netzspitze zurollen lassen, an der er
im Stillstand haengen bliebe. Er faellt in die Mulde, wird schneller, rollt durch und klettert auf der anderen Seite
wieder heraus; dabei verliert er etwa die Haelfte seiner Bewegungsenergie, fast alles an ein Zittern seiner Form, kaum
etwas an abgestrahlte Wellen. Bei den Tempi der Vorhersage (0,02 und schneller) reicht das nicht zum Festhalten; erst
bei noch langsameren Baellen (unter etwa 0,011) bleibt er in der Mulde gefangen und pendelt hin und her. An der
umgekehrten Stelle mit sieben Dreiecken prallt er wie an einem Huegel ab, fast ohne Verlust.
