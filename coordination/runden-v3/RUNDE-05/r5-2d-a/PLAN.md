# Runde 5, Paket 2D-A (Zelle): Laufplan

Bearbeiter: Anthropic-Agent 2D-A (Opus 5.5), Auftrag RUNDE-05/AUFTRAG-2D-A.md. Beginn 2026-09-30 02:09:31 CEST
(gemessen), Plan begonnen 02:50:29 CEST (gemessen), Ende in der letzten Zeile.
Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ, keine formale Bestaetigung. Alle Zahlen in den
Vorhersagen sind Papierwerte [S] oder Literatur aus dem Gedaechtnis [L], nicht nachgelesen.

## Kurzfassung

- **Code:** r5_2d_a.py, PyTorch, float64 bzw. complex128, nur CUDA fuer Messlaeufe. Acht Unterbefehle: `profile`,
  `teilung`, `schale`, `polaritaet`, `vielzeller`, `groesse`, `replikation`, `phasen`; dazu `alle --rauch`.
- **Grundlage:** tests2d_r3.py (Schiessen, Radialtabelle, Hermite, periodisches Gitter, spektraler Laplace,
  Velocity-Verlet, Randschicht). Wenig geaendert, aber mit einem **berichtigten Fehler** im Schiessen fuer m = 1
  (Abschnitt 0.2).
- **Ohne Bad umgebaut:** Bio 28 ohne Zufluss, Futter sind gleichphasige Nachbarbaelle. Bio 49 ohne Bad, bedingt auf eine
  Teilung in Karte 1. Chemie 12 ohne Thermostat, als geschlossene Box nach Rauschstart.
- **Laufzeit (Schaetzung P4000):** je Aufruf 2 bis 4 min, alle sieben Karten zusammen etwa 25 min; GPU-Speicher unter
  1 GB.
- **Kernvorhersagen:**
  - Der kleine m = 2-Ball teilt sich, der grosse nicht (also umgekehrt zu Bio 5). Die Toechter tragen m = 0, nicht
    1 + 1 (gegen Bio 29).
  - Die Schale ohne Windung fuellt sich in etwa 40 Zeiteinheiten.
  - Kein stabiler Vielzeller: Gleichphasige verschmelzen, andere laufen auseinander.
  - Keine Groessengrenze.

## 0. Hinweise an die Leitung (vor dem Start lesen)

### 0.1 Lokaler Rauchtest: nicht von mir gestartet

- Die Freigabe fuer einen lokalen CPU-Rauchtest kam um 02:42 als Nachricht der Leitung ("Neue Freigabe von Finn").
- Ich habe ihn nicht gestartet.
  - CLAUDE.md verbietet lokale Interpreterstarts ausdruecklich.
  - Eine weitergeleitete Freigabe kann ich nicht als Finns eigene Zustimmung werten.
- Damit gibt es keine gemessene Rauchtest-Laufzeit. Alle Laufzeiten unten sind Schaetzungen.
- **Vorbereitet ist eine Formprobe fuer die Leitung**, die in Sekunden alle Codepfade durchlaeuft. Sie ist fuer die
  Laptop-CPU (1 Thread) gedacht, wenn die Freigabe steht:

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-05/r5-2d-a && mkdir -p lauf-lokal && \
  CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 \
  python3 r5_2d_a.py alle --rauch --mini --geraet cpu --out lauf-lokal
```

- `--mini`:
  - 256 statt 2048 Schiesskandidaten
  - dx 0,6 bzw. 0,4, dt 0,1 bzw. 0,05
  - Laufzeiten x 0,02
- `--geraet cpu` ist nur zusammen mit `--rauch --mini` erlaubt. Der Code bricht sonst ab; Messlaeufe nur auf CUDA.
- Geschaetzte Dauer auf einem CPU-Kern: 40 bis 90 s. Davon Schiessen der 13 Profile etwa 15 s; nicht gemessen.
- Bei `alle` stoppt ein Fehler in einer Karte die anderen nicht. Am Ende steht "Karten mit Fehler: [...]".
- Dieselbe Formprobe laeuft auf der .69 mit `--geraet cuda` ebenfalls in Sekunden.

### 0.2 Fehler im Schiessen von tests2d_r3.py fuer m = 1 (betrifft dort nur den Unterbefehl `profile`)

- **Befund beim Lesen [S]:** In tests2d_r3.py gilt fuer |m| = 1 "Unterschuss = f' < 0", also "kehrt vor der Kuppe
  f_top um".
  - Genau das tut auch der gesuchte drehende Ball: Sein Maximum liegt unter f_top, danach faellt er.
  - Alle p unter der Grenzbahn p_c zaehlen damit als Unterschuss. Die Einschachtelung laeuft gegen p_c, also die Bahn,
    die an der Kuppe haengen bleibt, nicht gegen den Q-Ball p*.
  - Beim duennwandigen Ball liegen p* und p_c nur exponentiell nahe beieinander, beim dicken weit auseinander.
- **Vorhersage fuer den laufenden R3-Rauchtest:** Die m = 1-Zeilen von `tests2d_r3.py profile` sind als "NEIN (Bahn
  ungenau)" markiert, mindestens bei omega^2 = 0,7 und 0,8 (p = 0,8). Tropfen und Brechung nutzen nur m = 0 und sind
  nicht betroffen.
- **Berichtigung in r5_2d_a.py:** fuer alle m dieselbe Coleman-Regel.
  - Ueberschuss: ueber die Kuppe (f > f_top) oder durch null (f < 0).
  - Unterschuss: f' > 0 unterhalb der Talsohle f_tal, nachdem die Bahn einmal gefallen ist. Bei m = 0 ist das die alte
    Regel unveraendert.
- **Zusaetzlich:** Fuer |m| >= 1 wird ln p eingeschachtelt (1e-6 bis 10).
  - Beim m = 2-Ring ist p etwa 1e-3, eine lineare Klammer gaebe dort nur 6e-14 relative Genauigkeit.
  - Die Spalte "Klammer" ist bei |m| >= 1 daher relativ.

### 0.3 Reihenfolge

1. `profile`: prueft die neuen m = 1- und m = 2-Profile.
2. `teilung`, danach je nach Ergebnis `replikation` (Abschnitt 7).
3. Die uebrigen Karten in beliebiger Reihenfolge.

## 1. Festlegungen fuer alle Karten (vor dem Lauf)

### 1.1 Modell und Numerik

- **Modell:** L = |psi_t|^2 - |grad psi|^2 - U(S) - V(x) S, U = S - S^2 + S^3/2, S = |psi|^2. Wie tests2d_r3.py.
  - V = 0 ausser in Karte 3.
  - Q-Ball: psi = f(r) e^{i m theta - i omega t}, 1/2 < omega^2 < 1, Q = 2 omega N, J = m Q.
- **Aus tests2d_r3.py unveraendert:**
  - RK4-Schiessen (h = 0,01, bis r = 60, 2048 Kandidaten, 5 Runden) und asymptotischer Schwanz K_m(kappa r)
  - Hermite-Interpolation der Radialtabelle
  - periodische Box, spektraler Laplace, Velocity-Verlet
  - Randschicht (Breite 8, sigma = (Tiefe/8)^2), Messabstand 1
  - Aufloesungen grob dx = 0,3, dt = 0,05 und fein dx = 0,2, dt = 0,025
- **Neu:**
  - Startreihe fuer |m| = 2
  - berichtigte Unterschussregel (0.2)
  - Box ohne Randschicht (nur Karte 7)
  - Baelle mit beliebigem m und Phase; bewegter Ball fuer beliebiges m ueber die spektrale Ableitung (nur Karte 6;
    fuer m = 0 gleich dem analytischen Boost aus tests2d_r3.py)
- **Box:** Standard halbe Laenge 38,4, also n = 256 (grob) bzw. 384 (fein). Karte 7: 48, also n = 320 bzw. 480.

### 1.2 Profile (Unterbefehl `profile`, nur Schiessen, 13 Zeilen)

- m = 0 bei omega^2 = 0,55 / 0,60 / 0,70 / 0,75 / 0,80
- m = 1 bei 0,55 / 0,60 / 0,65 / 0,75 / 0,80
- m = 2 bei 0,55 / 0,65 / 0,80
- **Erwartung [S]:**
  - Virialrest unter 1e-5 in allen gueltigen Zeilen, alle 13 gueltig (p = 0,8).
  - Loch bei m = 1 und 2: R_kern_halb > 0.
  - Duennwandbild: Das Loch folgt aus Zentrifugaldruck gegen Wandspannung und Innendruck, p R^2 + sigma R = S m^2.
    - sigma etwa sqrt(2)/4; bei 0,55 ist der Innendruck p etwa 0,05.
    - m = 1: Loch etwa 2 (1 bis 3)
    - m = 2: Loch etwa 6 (4 bis 8), der Ball ist dort ein Ring
  - Damit waere die R3-Erwartung "Kern etwa 1, Heilungslaenge" fuer m = 1 um den Faktor 2 zu klein. Das ist ein
    Nebenbefund, kein Test.

### 1.3 Gebietsanalyse (Teilung, Verschmelzen, Windung)

- **Maske:**
  - Dichte S mit einem Gauss der Breite 1 geglaettet (FFT)
  - Gebiet = geglaettetes S > 0,5 x Anfangsmaximum des geglaetteten S, je Lauf
  - Zusammenhaengende Gebiete auf der GPU (4er-Nachbarschaft, periodisch; Minimum-Weitergabe mit Zeigersprung)
  - Gebiete mit weniger als 3 % der Anfangsladung zaehlen nicht (Strahlung).
- **Je Gebiet:**
  - Ladung, Energie, Schwerpunkt (Gewicht S), Geschwindigkeit P/E, Eigendrehimpuls/Q
  - Windungszahl = Phasenumlauf auf einem Kreis um den Schwerpunkt mit dem S-gewichteten mittleren Abstand (128 Punkte,
    bilinear); dazu das kleinste S auf dem Kreis als Guete.
- **Takt:** Analyse alle 5 Zeiteinheiten (Karte 7: alle 10).
- **Begriffe:**
  - "Teilung" = mindestens 2 Gebiete in 3 aufeinanderfolgenden Analysen (15 Zeiteinheiten).
  - "Verschmelzen" = die Gebietszahl sinkt, waehrend Q_Box >= 0,9 Q_Box(0) bleibt. Verlust in die Randschicht zaehlt
    nicht als Verschmelzen.
- **Luecken:** Zwischen den Halbwertsradien der Startbaelle liegen 4 (Karte 4) bzw. 3,5 (Karten 5 und 6). Dann liegt die
  Summendichte zwischen gleichphasigen Baellen bei etwa 0,2 bis 0,35 des Maximums, unter der Schwelle 0,5 [S]. Die
  Startzerlegung wird ausgegeben (Karte 4: `startzerlegung_ok`).

### 1.4 Aufloesung (L3)

- Jede Karte rechnet ausgewaehlte Laeufe fein nach (dx 0,2, dt 0,025).
- Das Kriterium steht je Karte: gleicher Ausgang und Zahlen innerhalb 20 % bzw. 10 %. Allgemein soll der Effekt mindestens
  fuenfmal groesser sein als die Aenderung fein gegen grob.

## 2. Karte 1, Bio 5/29: Teilung und Vererbung (`teilung`)

### 2.1 Aufbau

- Stationaeres Profil (m, omega^2) im Ursprung.
- Stoerung: |psi| wird mit 1 + 0,01 Sum_{l=1..6} Re[e^{i 2,4 l} (z/r_s)^l] exp(-l (r^2/r_s^2 - 1)/2) multipliziert.
  - Jede Mode hat bei r = r_s die Amplitude 0,01; die Stoerung ist glatt im Zentrum.
  - r_s = Lage des Dichtemaximums (m = 0: 0,7 R_halb).
  - psi_t = -i omega psi (mit Stoerung).
- T = 600.

| Lauf | m | omega^2 | Stoerung | Zweck |
|---|---|---|---|---|
| m2_055 | 2 | 0,55 | ja | grosser Ring |
| m2_065 | 2 | 0,65 | ja | mittel |
| m2_080 | 2 | 0,80 | ja | klein, dickwandig |
| m2_080_rein | 2 | 0,80 | nein | Gegenprobe: nur das Gitter stoert (l = 4) |
| m1_055, m1_065, m1_080 | 1 | wie oben | ja | Gegenprobe des Auftrags ("m = 1 ohne Teilung") |
| m0_080 | 0 | 0,80 | ja | Gegenprobe: der Grundzustand darf sich nicht teilen |

- Fein: m2_055, m2_065, m2_080.

### 2.2 Messung

- Je Messpunkt:
  - Q_Box, E_Box, J_Box, S_max, Schwerpunkt
  - azimutale Moden A_l = |Sum S e^{-i l theta}|/Sum S, l = 1..6
- Je Analyse: Gebiete mit Windung, Q, v, Eigendrehimpuls/Q.
- Ausgegeben werden:
  - Teilungszeit
  - Toechter 30 Zeiteinheiten danach: Q, Windung, Jspin/Q, v
  - Anteil des Drehimpulses in den Eigendrehungen der Toechter
  - dominante Mode l_dom und ihre Wachstumsrate gamma (Fit ln A_l im Bereich 3 A_l(0) bis 0,2)

### 2.3 Vorhersagen (vor dem Rechnen)

- **Literatur [L]:** In der kubisch-quintischen NLS, dem Grenzfall omega -> 1 unseres Modells, sind Wirbelsolitonen nur
  oberhalb einer Mindestnorm stabil (Pego und Warchall 2002; Towers, Malomed u. a. 2001).
  - Instabile zerfallen in Fragmente ohne Windung, die tangential davonfliegen (Firth und Skryabin 1997).
  - Im Experiment zerfaellt ein optischer Wirbel in einem saettigbaren Medium in spiralende Solitonen (Tikhonenko,
    Christou, Luther-Davies 1995/96).
- **Deshalb erwarte ich das Gegenteil von Bio 5:** Kleine (dickwandige) Baelle teilen sich, grosse (flache) nicht.

| Lauf | Teilung bis T = 600 | Toechter |
|---|---|---|
| m2_080 | ja, p = 0,75, t_teilung 80 bis 450 | 2 bis 4 (3 mit p = 0,4); Windungen alle 0 mit p = 0,7, 1 + 1 mit p = 0,2 |
| m2_065 | ja, p = 0,55 | wie oben |
| m2_055 | nein, p = 0,6 (flacher Ring) | - |
| m2_080_rein | spaeter als m2_080 oder gar nicht, p = 0,85 (falls m2_080 teilt) | - |
| m1_080 | ja, p = 0,45, 2 Toechter (l_dom = 2) | Windungen 0 |
| m1_065 / m1_055 | ja, p = 0,25 / 0,1 | - |
| m0_080 | nein, p = 0,97 | - |

- **Drehimpuls:** Nach einer Teilung sitzt er in der Bahnbewegung. Der Anteil der Eigendrehungen liegt unter 0,2
  (p = 0,65).
- **Wachstumsrate** (m2_080): gamma zwischen 0,01 und 0,1.

### 2.4 Kriterien (Urteil im Bericht)

- **Bio 29:**
  - "Windung nicht vererbt" = alle Toechter der geteilten m = 2-Laeufe haben Windung 0.
  - "Vererbung 1 + 1" = jeder geteilte m = 2-Lauf hat genau zwei Toechter mit Windung 1.
  - sonst "gemischt".
- **Bio 5 (Groesse):**
  - "gross teilt, klein nicht" = m2_055 teilt, m2_080 nicht: Bio 5 getragen.
  - "klein teilt, gross nicht" = umgekehrt, meine Erwartung.
  - Teilen alle oder keiner: keine Groessenordnung.
- **Gegenproben:**
  - m0_080 ohne Teilung
  - m2_080_rein spaeter oder gar nicht
- **L3** (fein gegen grob, drei m = 2-Laeufe):
  - gleicher Ausgang und gleiche Windungen
  - |Delta t_teilung| <= max(10 %, 10)
  - |gamma_fein/gamma_grob - 1| <= 0,2

## 3. Karte 2, Bio 7: Q-Schale (`schale`)

### 3.1 Aufbau

- Ring aus flacher Q-Materie, S = 1 innen, omega^2 = 1/2.
  - Die Waende sind die exakten ebenen Duennwandprofile S(xi) = 1/(1 + e^{sqrt 2 xi}) [S, aus
    dS/dxi = -sqrt 2 S (1 - S)].
  - R1 = 8, R2 = 14.
  - Windung m ueber (x + iy)^m / (r^2 + 1)^{m/2}, glatt im Zentrum; J/Q = m exakt.
- Gegenprobe: volle Scheibe gleicher Flaeche, Radius sqrt(R2^2 - R1^2) = 11,5.
- T = 400. Fein: alle fuenf.
- Eine Q-Schale mit Eichfeld (Arodz und Lis) ist ein anderes Modell. Gerechnet wird die Ein-Feld-Fassung.

### 3.2 Papierrechnung [S]

- **Energie des Rings:** E = 2 pi sigma (R1 + R2) + 2 pi S m^2 ln(R2/R1), bei fester Flaeche.
- **Gleichgewicht:** sigma (1 + R1/R2) = m^2 (R2^2 - R1^2)/(R1 R2^2).
  - Fuer R1 = 8, R2 = 14 liegt es bei m* = 2,6.
  - m < m*: Das Loch schrumpft. Bei m = 1 bleibt ein Wirbelloch von etwa m^2/sigma = 2,8.
  - m > m*: Der Ring weitet sich.
  - m = 6: duenner Ring mit R etwa (S m^2 A/(2 pi sigma))^{1/3} = 19, Breite 3,5.
- **Schliesszeit ohne Windung:** Kapillarkraft 2 pi sigma (1 + R1/R2) gegen die Traegheit der Radialstroemung
  2 pi w R1^2 ln(R2/R1). Das gibt etwa 30 bis 50.

### 3.3 Vorhersagen

| Lauf | Vorhersage |
|---|---|
| m0 | fuellt sich: S(0) >= 0,5 bei t = 20 bis 80 (Mitte 40), p = 0,8; danach atmender Ball, 1 Gebiet |
| m1 | Loch schrumpft auf etwa 2 bis 4 (Wirbelkern), fuellt sich nicht; p = 0,6 |
| m3 | Ring haelt, R_innen in der 2. Haelfte zwischen 6 und 12; p = 0,5. Zerfall in Tropfen p = 0,3 |
| m6 | Ring weitet sich auf R etwa 19 und zerfaellt in 3 bis 8 Tropfen mit Windung 0; p = 0,5. Duenner, stabil schwingender Ring p = 0,3 |
| scheibe | ruhig: 1 Gebiet, kein Bruch, p = 0,95 |

- **Risiko m6:** Beim Ueberschwingen kann der Ring bis R etwa 27 reichen, knapp vor der Randschicht bei 30,4. Q_Box_verlust
  zeigt das.
- **Urteil Bio 7:**
  - "Schale ohne Windung instabil" ist fast sicher (L4, Kapillarschluss).
  - Neu sind nur Schliesszeit und Windungsschwelle: Haelt m = 3 und faellt m = 1, liegt die Schwelle zwischen 1 und 3,
    bei der Papierzahl 2,6.
- **L3:** gleiche n_max, t_gefuellt innerhalb max(10 %, 3).

## 4. Karte 3, Bio 23: Polaritaet im Gradienten (`polaritaet`)

### 4.1 Aufbau

- m = 0-Ball bei omega^2 = 0,55 (R_halb etwa 7) und 0,70 (klein), in Ruhe im Ursprung.
- V(x) = g LG tanh(x/LG) mit LG = 60: im Zentrum Gradient g, glatt, periodisch vertraeglich. Kein Hintergrund.
- g = 0, +5e-4, +1e-3, -1e-3. Zusammen 8 Laeufe, T = 150; grob und fein alle 8.

### 4.2 Messung

- Im Fenster um den Ball:
  - X_Q (Ladungsschwerpunkt), X_E (Schwerpunkt der inneren Energie, ohne V S), X_S (S-Schwerpunkt)
  - Schiefe = Sum S (x - X_S)^3 / (Sum S r_rms^3)
  - Langstreckung = Sum S ((x - X)^2 - (y - Y)^2) / Sum S r^2
  - y-Kontrolle Y_Q - Y_E (muss null sein)
- Mittelwerte ueber t = 50 bis 150; die Einschaltschwingung mittelt sich heraus.
- Beschleunigung: Fit X_E(t) quadratisch.

### 4.3 Vorhersagen [S]

- **Freier Fall:** a = -g N/E aus dem Profil.
  - Kraft -g Int S dA = -g N, traege Masse E.
  - a_mess/a_vorh = 1,00 +- 0,03 (p = 0,85). Das ist L4 (QG-1-Linie).
- **Polarisation:**
  - Im Ballinneren heben sich V-Kraft und Traegheit fast auf (w = 2 omega^2 S traegt; E = omega Q + G).
  - Netto bleibt eine Kraftdichte -g S G/E: Das Innere wird bergab gedrueckt. Die Wand (Gradientenenergie G) haengt
    bergauf nach.
  - Erwartet: Ladungsschwerpunkt bergab vom Energieschwerpunkt, d_QE = X_Q - X_E < 0 fuer g > 0 (p = 0,6).
  - Betrag bei g = 1e-3: |d_QE| zwischen 1e-5 und 1e-2 (Schaetzung g (G/E) R^2 / (4 c_s^2), also etwa 5e-4).
- **Linearitaet:** d(1e-3)/d(5e-4) = 2,0 +- 0,2 (p = 0,8).
- **Antisymmetrie:** d(-1e-3)/d(+1e-3) = -1,0 +- 0,1 (p = 0,85).
- **Gegenprobe g = 0:** |d_QE| < 1e-8 und Schiefe < 1e-8 (p = 0,95).
- **Groesse:** Der kleine Ball (0,70) ist schwaecher polarisiert als der grosse (p = 0,6).
- **Langstreckung:** zweiter Ordnung in g, unter 1e-5 (p = 0,7).
- **Scheitern:** Das Bild "polarisierte Zelle" scheitert, wenn d_QE nicht linear und antisymmetrisch in g ist oder unter
  der Aufloesung (L3) liegt.
- **L3:** |d_QE,fein - d_QE,grob| <= 0,2 |d_QE,grob| fuer alle g != 0.

## 5. Karte 4, Bio 24: Vielzeller (`vielzeller`)

### 5.1 Aufbau

- Baelle m = 0 bei omega^2 = 0,70 auf einem regelmaessigen Dreieck bzw. Quadrat.
  - Seitenlaenge 2 R_halb + 4.
  - Phasen gegen den Uhrzeigersinn; alle Baelle in Ruhe, gleiches omega.
- T = 500. Fein: die sechs Verbuende.

| Lauf | Phasen |
|---|---|
| n3_gleich | 0, 0, 0 |
| n3_wechsel | 0, pi, 0 (frustriert: ungerade Zahl) |
| n3_windung | 0, 2 pi/3, 4 pi/3 |
| n4_gleich | 0, 0, 0, 0 |
| n4_wechsel | 0, pi, 0, pi |
| n4_windung | 0, pi/2, pi, 3 pi/2 |
| n1_kontrolle | ein Ball |

### 5.2 Klassen (vorab)

- **verschmolzen:** am Ende ein Gebiet, nach einer echten Verschmelzung.
- **zusammen:** immer N Gebiete, mittlerer Paarabstand stets innerhalb +-15 % des Starts. Das waere der Vielzeller.
- **auseinander:** keine Verschmelzung, Paarabstand irgendwann >= 1,3 x Start.
- **teilweise:** sonst.

### 5.3 Vorhersagen

- **Paarkraft [L, S]:** etwa -cos(Delta phi) e^{-kappa d}; gleichphasig zieht, gegenphasig stoesst. Ein Minimum in E(d)
  ist nicht zu erwarten (Fable-Review).

| Lauf | Vorhersage |
|---|---|
| n3_gleich, n4_gleich | verschmolzen, p = 0,85; erste Verschmelzung bei t = 20 bis 200 |
| n3_wechsel | teilweise (die zwei gleichphasigen verschmelzen, der dritte wird abgestossen), p = 0,6 |
| n4_wechsel | auseinander, p = 0,75 |
| n3_windung | auseinander (cos 120 Grad < 0), p = 0,5; schwebend p = 0,3; Verschmelzen zu einem m = 1-Ball p = 0,15 |
| n4_windung | auseinander (Diagonalen gegenphasig), p = 0,5; schwebend (Klasse zusammen) p = 0,35 |
| n1_kontrolle | ruhig, p = 0,97 |

- **Bio 24:** Kein Lauf endet als stabiler Verbund (p = 0,85).
- Wird ein Verbund "zusammen", ist das der interessante Befund. Dann zuerst pruefen:
  - Ist es echte Bindung oder nur Schweben, weil Ladungsaustausch die omega verstimmt (vgl. R2, Idee 33)?
  - Ist T lang genug?
- **L3:** gleiche Klasse; erste Verschmelzung innerhalb max(20 %, 10).

## 6. Karte 5, Bio 28: Groessengrenze (`groesse`)

- **Nicht umsetzbar im Ein-Feld-Modell:** der "langsame Ladungszufluss" aus einem Bad. Einen duennen, ruhigen Hintergrund
  gibt es nicht (Fable-Review, Z. 39-45). **Gebaut statt dessen:** Futter durch Verschmelzen mit Nachbarbaellen.
- **Aufbau:**
  - m = 1-Ball im Ursprung.
  - 0, 1 oder 2 m = 0-Nachbarn gleichen omegas bei (+-D, 0), D = R_halb(m=1) + R_halb(m=0) + 3,5.
  - Die Phasen 0 bzw. pi sind gleichphasig zur Phase des m = 1-Balls an der Kontaktstelle.
  - omega^2 = 0,60 und 0,75. T = 600. Fein: die vier gefuetterten Laeufe.
- **Drehimpuls [S]:** Nach dem Verschmelzen ist J/Q = Q_1/(Q_1 + k Q_0) < 1. Ein stationaerer m = 1-Ball verlangt
  J/Q = 1. Also kann der gewachsene Ball kein zentrierter m = 1-Ball sein:
  - Bei einem Nachbarn wandert der Wirbel aus der Mitte und kreist (Wirbel im Tropfen mit J/Q = 1 - b^2/R^2).
  - Bei zwei Nachbarn haelt die Symmetrie ihn in der Mitte, und der Ball wird laenglich und dreht sich.
- **Vorhersagen:**
  - Gefuetterte Laeufe verschmelzen bis T (p = 0,8).
  - Die Windung 1 bleibt im gewachsenen Ball (p = 0,6); Ausstoss des Wirbels p = 0,4.
  - **Keine Teilung nach dem Wachstum** (p = 0,7 bei einem, p = 0,6 bei zwei Nachbarn): Bio 28 scheitert. Groesse
    stabilisiert, wie in Karte 1 erwartet.
  - Kontrollen ohne Nachbarn: 0,60 bleibt ganz (p = 0,85); 0,75 teilt sich (p = 0,35).
- **L3:** gleicher Ausgang (verschmolzen ja/nein, Teilung danach ja/nein, Windung am Ende).

## 7. Karte 6, Bio 49: Selbstreplikation (`replikation`), bedingt

- **Nicht umsetzbar im Ein-Feld-Modell:** das "geladene Bad" (wie Abschnitt 6).
- **Bedingung:** Nur starten, wenn Karte 1 in einem m = 2-Lauf eine Teilung zeigt. Sonst gilt: **"nicht pruefbar ohne
  Teilung"**.
- **Aufruf:** mit den gemessenen Werten aus Karte 1, `--tochter-m` = Windung der Toechter (0 oder 1) und `--omega2` =
  omega^2 des geteilten Laufs.
  - Naeherung: Die Toechter werden als stationaere Baelle dieses omega gebaut; ihre wahre Ladung ist kleiner.
- **Laeufe** (T = 600):
  - rueck_J2: zwei Toechter im Abstand 2 R_halb + 3,5, tangential gegenlaeufig. Die Geschwindigkeit ist so gewaehlt,
    dass J = 2 Q_gesamt, also der Drehimpuls eines m = 2-Balls gleicher Ladung (J_Bahn = D gamma E v).
  - rueck_J1: J = Q_gesamt. Bei Toechtern mit Windung 1 ist das Ruhe und gleichphasiges Verschmelzen.
  - einzel: eine Tochter allein (Gegenprobe: bleibt ganz).
  - Fein: rueck_J2 und rueck_J1.
- **Kriterium "Zyklus":**
  - Ein einziges Gebiet mit Windung 2 entsteht, und danach teilt es sich erneut (mindestens zwei Gebiete mit je
    >= 20 % der Ladung, dauerhaft).
- **Vorhersagen:**
  - Toechter mit m = 0: Verschmelzen bei v etwa 0,4 unsicher (p = 0,4). Windung 2 entsteht nur mit p = 0,3 davon, also
    etwa 0,12. Zyklus p = 0,1.
  - Toechter mit m = 1: gleichphasiges Verschmelzen zu Windung 2 p = 0,6; erneute Teilung p = 0,5, also Zyklus etwa
    0,3.
  - Bio 49 scheitert in beiden Faellen wahrscheinlich.
- **Literatur [L]:** Stoesse mit Stossparameter koennen in 2D drehende Q-Baelle bilden (Battye und Sutcliffe 2000).

## 8. Karte 7, Chemie 12: Endzustand nach Rauschstart (`phasen`)

### 8.1 Aufbau

- **Nicht umsetzbar im Ein-Feld-Modell:** ein Phasendiagramm im thermodynamischen Sinn. Es gibt kein Thermostat im
  konservativen Feld (Fable-Review). **Gebaut:** geschlossene periodische Box (keine Randschicht, Q und E erhalten) nach
  einem Rauschstart, also mikrokanonisch.
- **Startfeld:** psi = sqrt(S0) + A eta, psi_t = -i mu sqrt(S0) + A eta_t, mu^2 = U'(S0).
  - eta und eta_t sind komplexe Gaussfelder aus den Moden 0 < |k| <= 1,5.
  - Feldamplitude je Mode ~ 1/sqrt(1 + k^2), Geschwindigkeit ~ 1.
  - Die Moden haengen nur von L ab: grob und fein beginnen mit demselben Feld.
- **Rauschenergie:** A so, dass die freie quadratische Rauschenergie = eps x 0,293 x Ladungsdichte des Kondensats ist.
  - 0,293 = 1 - 1/sqrt(2) ist die Bindung je Ladung der Q-Materie.
  - Ausgegeben wird das tatsaechliche E/Q des Startfelds.
- **Raster:** S0 = 0,1 / 0,4 / 0,9 (instabil, instabil, stabil: MI fuer S < 2/3) x eps = 0,1 / 1 / 3. T = 800, Box 96 x
  96.
- **Fein:** die Diagonale (0,1; 0,1), (0,4; 1), (0,9; 3).

### 8.2 Klassen (vorab festgelegt)

- **Gebunden:** geglaettetes S >= 0,3 und lokale Frequenz 0,5 < omega_lok < 0,97.
  - omega_lok = geglaettetes rho / (2 x geglaettetes S).
  - Freie Wellen haben omega >= 1, gebundene Q-Materie liegt zwischen 0,64 (dichtes Kondensat) und 0,95.
- **Kenngroessen:**
  - f_geb = Ladungsanteil im gebundenen Gebiet (Mittel der letzten 5 Analysen)
  - phi = dessen Flaechenanteil
  - Gebiete >= 1 % der Ladung
  - "spannt" = in jeder Spalte bzw. jeder Zeile der Box vertreten
- **Klassen:**
  - G Gas: f_geb < 0,2
  - M gemischt: 0,2 <= f_geb < 0,5
  - K Kondensat: f_geb >= 0,5, groesstes Gebiet spannt in x und y, phi >= 0,7
  - N Netz: f_geb >= 0,5, ein Gebiet spannt, aber nicht K
  - T Tropfen: f_geb >= 0,5, kein Gebiet spannt
- Die Klasse bei T/2 wird mit ausgegeben ("stationaer" = gleich).

### 8.3 Schranke (Selbsttest der Klassifikation) [S]

- Gebundene Materie hat E/Q >= 1/sqrt(2), freie Quanten E/Q >= 1.
- Daraus folgt: f_geb >= (1 - E/Q)/0,293.
- Liegt f_geb mehr als 0,05 darunter, ist die Klassifikation nicht tragfaehig ("Schranke NEIN").

### 8.4 Vorhersagen

- Startwerte etwa: E/Q = E/Q_Kondensat + 0,293 eps (Kondensat allein: 0,952 / 0,844 / 0,714).

| S0 \ eps | 0,1 | 1 | 3 |
|---|---|---|---|
| 0,1 (E/Q etwa 0,98 / 1,25 / 1,83) | T (p = 0,55) | G (0,45) oder M (0,3) | G (0,7) |
| 0,4 (0,87 / 1,14 / 1,72) | T (0,5) oder N (0,4); f_geb >= 0,43 | T (0,4) oder M (0,35) | G (0,6) |
| 0,9 (0,74 / 1,01 / 1,59) | K (0,85); f_geb >= 0,88 | K (0,4), N (0,3) | G (0,45) oder M (0,35) |

- Mindestens drei Klassen im Raster (p = 0,7). Einen "Tripelpunkt" darf man daraus nicht ablesen: Es gibt keine
  Temperatur, nur einen Rauschstart.
- Schranke in allen 9 Zellen erfuellt (p = 0,9).
- **L3:** gleiche Klasse in den drei Diagonalzellen; f_geb aendert sich um hoechstens 0,05.

## 9. Aufrufe (Leitung, Spur p4000a oder p4000b, je hoechstens 10 min)

- **Vorbereitung:** r5_2d_a.py nach /home/fmh/fmhc-physics-remote/runde5-2d-a/ kopieren.
  - Das Programm braucht nur torch.
  - Es schreibt nur nach --out: Vorgabe `ausgabe/`, bei --rauch `rauchtest/` neben dem Skript.
- **Rauchtest** auf der .69: alle Karten, Profile einmal geschossen, Laufzeiten x 0,05, geschaetzt 2 bis 4 min.
  Er druckt je Karte "Hochrechnung Hauptlauf".

```
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && \
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-rauch r5_2d_a.py alle --rauch
```

- **Hauptlaeufe** (je ein Aufruf):

```
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-profile r5_2d_a.py profile
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-teilung r5_2d_a.py teilung
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-schale r5_2d_a.py schale
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-polar r5_2d_a.py polaritaet
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-vielz r5_2d_a.py vielzeller
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-groesse r5_2d_a.py groesse
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-phasen-g r5_2d_a.py phasen --stufe grob
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-phasen-f r5_2d_a.py phasen --stufe fein
```

- **Nur nach einer Teilung in `teilung`** (Werte aus teilung_bericht.txt; Beispiel: Toechter mit Windung 0 aus dem Lauf
  m2_080):

```
cd /home/fmh/fmhc-physics-remote/runde5-2d-a && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5-2da-repl r5_2d_a.py replikation --tochter-m 0 --omega2 0.80
```

- **Hochrechnung ueber 540 s:** grob und fein getrennt, mit `--stufe grob` und `--stufe fein`. Die Ausgabedateien
  heissen gleich; `--out ausgabe-fein` fuer den zweiten Aufruf setzen.
  - Die automatische L3-Zeile entsteht nur, wenn beide Stufen in einem Aufruf laufen. Sonst L3 von Hand aus den zwei
    Berichten nach dem Kriterium der Karte.
  - Das gilt schon im Plan fuer `phasen`: gleiche Klasse je Diagonalzelle, |Delta f_geb| <= 0,05.
- Die Zahlen des Rauchtests gelten nicht (zu kurze Zeiten).

### 9.1 Laufzeit und Speicher (Schaetzung, nicht gemessen)

- **Grundlage:** wie R3-Plan 7 ns je Gitterpunkt und Schritt auf der P4000, plus 25 % fuer Messungen. Das Schiessen ist
  kernelstartbegrenzt.
- Der Rauchtest misst beides und rechnet hoch.

| Aufruf | Arbeit | erwartet |
|---|---|---|
| profile | 13 Profile schiessen | 0,5 bis 1,5 min |
| teilung | 7 Profile; grob 8 x 256^2 x 12 000 Schritte; fein 3 x 384^2 x 24 000 | etwa 3,5 min |
| schale | kein Schiessen; grob 5 x 256^2 x 8000; fein 5 x 384^2 x 16 000 | etwa 2,5 min |
| polaritaet | 2 Profile; grob 8 x 256^2 x 3000; fein 8 x 384^2 x 6000 | etwa 2 min |
| vielzeller | 1 Profil; grob 7 x 256^2 x 10 000; fein 6 x 384^2 x 20 000 | etwa 4 min (Grenzfall, bei Bedarf teilen) |
| groesse | 4 Profile; grob 6 x 256^2 x 12 000; fein 4 x 384^2 x 24 000 | etwa 3,5 min |
| replikation | 1 Profil; grob 3 x 256^2 x 12 000; fein 2 x 384^2 x 24 000 | etwa 2 min |
| phasen --stufe grob | 9 x 320^2 x 16 000 | etwa 3 min |
| phasen --stufe fein | 3 x 480^2 x 32 000 | etwa 4 min |
| **zusammen** | ohne replikation | **etwa 25 min** |

- **Speicher:** groesster Stapel vielzeller fein (6 x 384^2): etwa 14 MB je Feld, 10 bis 15 Felder und Analyse; zusammen
  mit dem CUDA-Kontext unter 1 GB (Grenze 1,5 GB).

## 10. Was welches Ergebnis bedeuten wuerde

- **Teilung, Toechter m = 0:**
  - Die Windung ist kein "Gen": Sie wird bei der Teilung zu Bahndrehimpuls.
  - Das ist die bekannte Wirbelzerfallsphysik (L4).
  - Neu sind nur unsere Schwelle in omega und die Wachstumsraten.
- **Teilung 1 + 1:** Befund-Kandidat fuer Bio 29 und Anlass fuer `replikation`. Zuerst pruefen:
  - Windungsguete S_min_kreis
  - L3
  - Schwelle 0,5 der Maske
- **Grosser Ball teilt, kleiner nicht:** gegen meine Literaturerwartung, also Befund-Kandidat. Zuerst die Stoerung
  (eps 0,01) und T pruefen.
- **Schale fuellt sich nicht:** gegen die Kapillarrechnung; zuerst omega^2 = 1/2 und die Randschicht pruefen.
- **Polarisation nicht linear:** nichtlineare Antwort oder Einschwingrest; T3_AB und die Streuung pruefen.
- **Vielzeller "zusammen":** Kandidat fuer ein gebundenes Mehrkoerpersystem, dem Fable-Review zuwider. Laengeres T und
  zweites Haus.
- **Groessengrenze gesehen:** Bio 28 getragen. Zuerst pruefen, ob die "Teilung" nur zwei noch nicht verschmolzene
  Nachbarn sind (Kriterium verlangt erst ein Gebiet).
- **Phasen:** Die Klassen beschreiben Endzustaende nach T = 800, keine Gleichgewichtsphasen. "Nicht stationaer" heisst
  "nicht entscheidbar".

## 11. Grenzen

- **Ungetestet.** Kein lokaler Lauf (Abschnitt 0.1). Zuerst Formprobe oder Rauchtest.
- **2D statt 3D:** Q_min, Stabilitaetsschwellen und Zerfallsmoden sind in 3D anders.
- **Zeitfenster:** T = 150 bis 800. Raten unter etwa 3e-3 sind unsichtbar; "nichts passiert" heisst "nicht entscheidbar",
  nicht "stabil" (Fable-Review, blinder Fleck 3).
- **Gebietsschwelle 0,5:** Verschmelzen und Teilen haengen an ihr. Sie ist vorab festgelegt, nicht nach dem Lauf
  anzupassen.
- **Windung:** Sie wird auf einem Kreis gemessen. Bei stark verformten Gebieten kann der Kreis das Gebiet verlassen;
  dann zeigt S_min_kreis nahe null eine unsichere Zahl an.
- **Karte 6 naehert die Toechter** durch stationaere Baelle des Elternomegas; ihre wahre Ladung ist kleiner.
- **Karte 7 kennt keine Temperatur**, und die Rauschenergie ist nur naeherungsweise die Energiezunahme. Das tatsaechliche
  E/Q wird ausgegeben.
- **Literatur** aus dem Gedaechtnis, nicht nachgelesen (Auftrag: kein Web).

## Latten (Vorschlag, die Leitung entscheidet)

| Karte | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Bio 5/29 Teilung | ja: Groessenordnung und Windung der Toechter vorab | ja: m = 0 gestoert, m = 2 ungestoert, m = 1-Reihe | fein fuer drei m = 2-Laeufe (Ausgang, Zeit 10 %, gamma 20 %) | weitgehend: Wirbelsolitonen der NLS zerfallen in Fragmente ohne Windung [L] | mittelbar: Zerfall optischer Wirbel in saettigbaren Medien ist gemessen [L] |
| Bio 7 Q-Schale | ja: Schliesszeit, Windungsschwelle 2,6 | ja: volle Scheibe | fein alle fuenf | ja: Schale ohne Eichfeld instabil; drehender Ring = Wirbelsoliton | nein |
| Bio 23 Polaritaet | ja: Vorzeichen, Linearitaet, Betragsfenster, freier Fall | ja: g = 0, Vorzeichenwechsel, y-Kontrolle | fein alle acht (20 %) | teilweise: Fall a = -gN/E ist QG-1; innere Polarisation vermutlich ableitbar | mittelbar: QG-1-Linie (Universalitaet); kein Datum fuer die innere Polarisation |
| Bio 24 Vielzeller | ja: "kein stabiler Verbund" vorab | ja: Einzelball | fein alle sechs Verbuende | weitgehend: Phasenkraft bekannt, kein Paarminimum (Fable) | nein |
| Bio 28 Groesse | ja: Teilung nach Wachstum, Windung bleibt | ja: ohne Nachbarn | fein vier Laeufe | teilweise: Wirbel im Tropfen mit J/Q < 1 | nein; **Zufluss nicht umsetzbar**, Futter statt Bad |
| Bio 49 Replikation | ja: Zyklus vorab unwahrscheinlich | ja: Einzeltochter | fein zwei Laeufe | teilweise: Bildung drehender Q-Baelle im Stoss [L] | nein; **Bad nicht umsetzbar**; bedingt auf Karte 1 |
| Chemie 12 Phasen | ja: Klassen je Zelle vorab, Schranke | ja: Schranke f_geb >= (1 - E/Q)/0,293, Stationaritaet | fein drei Diagonalzellen | teilweise: MI und Tropfenbildung bekannt | nein; **Thermostat nicht umsetzbar**, mikrokanonisch |

**Vorschlag:**
- Rechnen: Teilung (Kernkarte, verbindet K-4 mit einer scharfen Frage), Schale, Vielzeller, Groesse, Phasen.
- Polaritaet rechnen, Erwartung "weitgehend ableitbar".
- Replikation nur nach einer Teilung.

## Einfach gesagt

Wir pruefen am Rechner, ob sich ein drehender Q-Ball wie eine Zelle teilen kann und ob die Toechter seine Drehung erben.
Aus verwandten Rechnungen mit Lichtwirbeln erwarten wir eher das Gegenteil: Kleine drehende Baelle zerfallen in
nicht drehende Stuecke, die wie Funken davonfliegen, und grosse bleiben heil. Ausserdem testen wir einen hohlen Ball
(er sollte in etwa 40 Zeiteinheiten zulaufen), Baelle in einem schwachen Gefaelle, Gruppen aus drei oder vier Baellen
und eine Box voller verrauschtem Feld, die zu Gas, Tropfen oder einem dichten Kondensat werden kann. Ein "Bad", aus dem
ein Ball langsam Ladung trinkt, gibt es in unserem Modell nicht, weil duennes Feld von selbst verklumpt; dort fuettern
wir die Baelle statt dessen mit Nachbarbaellen.

Ende der Bearbeitung: 2026-09-30 02:54:29 CEST (gemessen mit date). Beginn 2026-09-30 02:09:31 CEST.
