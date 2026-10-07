# ERGEBNIS SCHWEBUNGSUHR-2 (Runde 23)

- Code-Agent im Auftrag der Leitung claude-primary. Geschrieben ab 2026-10-02 22:20:52 CEST (date).
- Plan eingefroren 22:06:35 CEST (PLAN.md.eingefroren-20261002-220635, schreibgeschuetzt; PLAN.md seither unveraendert,
  gleicher sha256).
- Laeufe auf der .69 ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6):
  - Aufrufe ab 22:06:41 CEST. Mehrere Aufrufe warteten bis knapp 3 min auf Spuren, die ein anderer Auftrag belegte.
  - Letzter Lauf fertig 22:14:27, Hilfsauswertung 22:14:36 bis 22:14:38 CEST.
  - Literatur erst danach.
- Explorativ (v3). Alles im Modell M1 in 1D, nur Phasenlage 0 (Kartenvorgabe). Deutungen sind Hypothesen [H].
- Urteile mechanisch aus hilfs/auswertung2.py nach den eingefrorenen Regeln (lauf-69/auswertung2.json).

## 1. Ergebnis zuerst

1. **Die Uhren laufen bei jedem Abstand auseinander, nie zusammen (T0 und T2 eingetroffen).**
   - Der groessere Ball gewinnt immer Ladung, der kleinere verliert genau so viel. Q_1 steigt bei D = 10 / 12 / 18 / 22
     um 0,925 / 0,230 / 0,0038 / 0,00033.
   - Delta omega am Ende liegt immer ueber dem freien Wert: r = +534 % (D = 8), +361 % (10), +109 % (12), +1,9 % (18),
     +0,18 % (22).
   - Bedeutung laut Karte: "Schwach gekoppelte Q-Ball-Uhren laufen auseinander statt zusammen ('reich wird reicher'
     ueber Ladungsfluss)" [H, 1D].
   - Der zweite Satz der Kartenbedeutung ("eine gemeinsame Zeit entsteht nur durch Verschmelzen") stuetzt sich auf die
     Vorkarte (D = 6,6 und 4,6). In diesem Raster endete kein Lauf verschmolzen.
2. **T1 formal nicht eingetroffen, und zwar knapp.**
   - r ist ueberall positiv und faellt streng mit D. Die Steigung von ln r gegen D ist aber -0,602. Sie liegt 0,008
     ausserhalb des vorhergesagten Bereichs [-1,22; -0,61].
   - In der Zweitlesart (letztes 50er-Gleitfenster statt Ende-Fenster) waere T1 eingetroffen (-0,725). Diese Lesart
     haengt an einer Momentaufnahme der Schwebung bei D = 22: Dort schwankt r im 50er-Fenster zwischen 0,0002 und
     0,0032.
   - Beobachtung [H]: Im schwachen Bereich ist die lokale Steigung -0,61 (14,6 nach 18, nicht gewertet) bzw. -0,59
     (18 nach 22). Das ist etwa -kappa, also einfacher Schwanzueberlapp, genau am Rand des vorhergesagten Bereichs.
3. **T3 nicht eingetroffen: Bei D = 8 sind die Baelle bei T = 3000 getrennt.**
   - Sie beruehren sich: Der Maximaabstand liegt ab t = 12 bis etwa t = 25 unter 1,5.
   - Danach fliegen zwei Baelle auseinander:
     - ein grosser mit Q ~ 4,85 und v ~ -0,06
     - ein kleiner mit Q ~ 1,45, v ~ +0,20 und Zentraldichte 0,13
   - Beide Kriterien (V1 der Vorkarte und das Dichtebild V2) sagen bei T "nicht verschmolzen".
   - Ob es ein kurzes Verschmelzen mit Spaltung war oder ein Abprallen, zeigen die gespeicherten Daten nicht.
4. **Zwei Regime** [H fuer die Deutung]:
   - Bei D <= 12 fliessen 8 bis 52 % der Ladung des kleinen Balls zum grossen. Danach stossen sich die Baelle ab und
     fliegen auseinander (v_rel 0,10 bis 0,33); der Ladungsstand friert ein.
   - Bei D >= 18 bleiben die Baelle fast liegen, und die Ladung pendelt im Schwebungstakt.
   - Bei D = 22 pendelt Q_1 zwischen seinem Startwert (3,162139 gegen 3,162136) und Startwert + 6,6e-4. Unter den
     Startwert faellt es nie.
   - Das passt zu einem phasengetriebenen Austausch, dessen Vorzeichen an der Startphase haengt.
   - [H, ungeprueft]: Mit Phasenlage pi koennte der grosse Ball im Mittel verlieren, dann wuerden die Takte
     zusammenruecken. Gerechnet ist nur Phasenlage 0.
5. **Kontrollen und Literatur:**
   - D = 14,6 reproduziert den Vorkartenlauf Z2 bitgleich (Analyse und Meta ohne Zeitfelder).
   - Zweites Gitter bei D = 12: r = 1,0854 (dx 0,1) gegen 1,0861 (dx 0,05), alle Urteile gleich (L3).
   - Literatur (L4):
     - Bekannt [S]: phasengetriebener Ladungstransfer mit gegenlaeufiger Taktaenderung; der Verlierer fliegt schneller;
       Schwebung mit der Differenzfrequenz; langsame Drift auseinander; Kraft ~ cos(Phase) e^(-Schwanzrate * Abstand).
     - Ein gemessenes Abstandsgesetz r(D) des Taktauseinanderlaufens fand ich nicht [L?].

## 2. Tabelle je D (T = 3000, Phasenlage 0, omega^2 = 0,60 / 0,65)

Messweise:
- Q Anfang = Q(t = 0) (erste Messung); Q Ende = Mittel ueber [2602,7; 3000].
- Delta omega Anfang/Ende = Phasenfits der Vorkarte ueber [50; 447,3] bzw. [2602,7; 3000].
- r = (Delta omega_Ende - Delta omega_frei)/Delta omega_frei, mit Delta omega_frei = 0,0316331 (dx 0,1) bzw. 0,0316301
  (dx 0,05).
- Schwebung = dominante Pencil-Frequenz der Mittelpunktsdichte ueber [50; 3000].
- Abstand = d(0) / Schwerpunktabstand dX Anfang / dX Ende.
- Verschmolzen bei T:
  - V1 = Median des Maximaabstands ueber [2900; 3000] < 1,5.
  - V2 = Dichtebild bei t = 3000 mit hoechstens einem Maximum > 0,1 oder den zwei groessten < 1,5 auseinander.

| D | dx | verschmolzen V1 / V2 | Q_1 Anf. / Ende | Q_2 Anf. / Ende | Delta omega Anf. / Ende | r(D) | Schwebung | Abstand d(0) / dX A / dX E |
|---|---|---|---|---|---|---|---|---|
| 8 | 0,1 | nein (766) / nein (2 Max., 779) | 3,4405 / 4,8501 | 3,0048 / 1,4519 | 0,20039 / 0,20058 | +5,3408 | (2,244, nicht deutbar) | 7,91 / 69,5 / 738,2 |
| 10 | 0,1 | nein (972) / nein (2 Max., 988) | 3,2736 / 4,1987 | 2,8436 / 1,9058 | 0,14578 / 0,14578 | +3,6085 | (0,236, nicht deutbar) | 9,97 / 77,7 / 922,1 |
| 12 | 0,1 | nein (291) / nein (2 Max., 296,5) | 3,2026 / 3,4323 | 2,7881 / 2,5584 | 0,066166 / 0,065968 | +1,0854 | 0,06665 | 11,99 / 28,5 / 276,9 |
| 12 | 0,05 | nein (291) / nein (2 Max., 296,5) | 3,2030 / 3,4331 | 2,7891 / 2,5589 | 0,066183 / 0,065984 | +1,0861 | 0,06668 | 11,99 / 28,5 / 277,0 |
| 14,6 (nur berichtet) | 0,1 | nein (37,75) / nein (2 Max., 38,0) | 3,1724 / 3,2023 | 2,7655 / 2,7356 | 0,036412 / 0,036328 | +0,14841 | 0,03622 | 14,60 / 15,3 / 36,5 |
| 18 | 0,1 | nein (19,6) / nein (2 Max., 19,5) | 3,16363 / 3,16747 | 2,75929 / 2,75545 | 0,032237 / 0,032228 | +0,018822 | 0,03195 | 18,00 / 17,96 / 19,46 |
| 22 | 0,1 | nein (22,0) / nein (2 Max., 22,0) | 3,162136 / 3,162468 | 2,758301 / 2,757970 | 0,031687 / 0,031689 | +0,0017815 | 0,03164 | 22,00 / 22,00 / 22,01 |

Zusatzgroessen je D (r je Drittel = Phasenfits der Vorkarte):
- Gleitend = Spanne von r im 50er-Fenster ueber den ganzen Lauf.
- r letzt = letztes 50er-Fenster [2950; 3000] (Zweitlesart).
- Zeitdehnung = Anteil von omega/gamma an r, berichtet, nicht korrigiert.
- Interferenz = Q_innen(0) - Q_1,frei - Q_2,frei.

| D | r je Drittel | r gleitend min / max | r letzt | Zeitdehnung | v1 / v2 Ende | Q_1 halbe Spanne Ende | Interferenz t = 0 | Q_innen 0 / T |
|---|---|---|---|---|---|---|---|---|
| 8 | 5,3402 / 5,3412 / 5,3411 | -1,66 / 5,43 | 5,3317 | -0,512 | -0,064 / +0,196 | 0,018 | +0,525 | 6,445 / 6,281 |
| 10 | 3,6085 / 3,6085 / 3,6085 | 2,76 / 4,07 | 3,6056 | -0,513 | -0,112 / +0,219 | 2e-4 | +0,197 | 6,117 / 6,104 |
| 12 (0,1) | 1,0865 / 1,0854 / 1,0854 | 0,445 / 1,542 | 1,0853 | -0,0174 | -0,043 / +0,055 | < 1e-6 | +0,071 | 5,99072 / 5,99069 |
| 12 (0,05) | 1,0872 / 1,0861 / 1,0861 | 0,445 / 1,542 | 1,0861 | -0,0174 | -0,043 / +0,055 | < 1e-6 | +0,071 | 5,99208 / 5,99205 |
| 14,6 | 0,1493 / 0,1484 / 0,1484 | 0,051 / 0,309 | 0,1484 | -7e-5 | -0,0039 / +0,0045 | < 1e-6 | +0,0178 | 5,9379 / 5,9379 |
| 18 | 0,01933 / 0,01927 / 0,01914 | 0,0021 / 0,0368 | 0,01964 | -5e-7 | -0,0004 / +0,0005 | 0,0016 | +0,0028 | 5,92292 / 5,92292 |
| 22 | 0,00171 / 0,00172 / 0,00171 | 0,0002 / 0,0032 | 0,00022 | < 1e-9 | ~0 / ~0 | 0,00033 | +0,0003 | 5,92044 / 5,92044 |

Lesehilfe:
- **Ladung:** Q_1 + Q_2 bleibt bei D >= 12 auf 1e-5 erhalten. dQ_1 = -dQ_2 bis auf 3e-5; die Ladung fliesst also
  wirklich vom kleinen zum grossen Ball.
  - D = 8 verliert 2,5 % der Gesamtladung durch Abstrahlung, D = 10 0,2 %.
- **Schwebung bei D <= 12:** Sobald die Baelle auseinandergeflogen sind, liegt am Mittelpunkt kein Ueberlapp mehr. Die
  Pencil-Frequenzen der spaeteren Drittel (1,2 bis 2,7) sind dann Rauschen.
  - Bei D = 12 ist nur das erste Drittel deutbar: 0,0666 gegen Delta omega_Ende = 0,0660.
  - Bei D >= 14,6 trifft die Schwebung Delta omega_Ende auf 0,15 bis 0,9 % (Wert ueber [50; T]; spaetere Drittel bis auf 0,15 %).
- **D = 8 im Zeitverlauf:**
  - Maximaabstand d: 7,9 (t = 0), 5,7 (t = 10), 0,8 (t = 14 bis 20), 1,0 bis 3,4 (t = 22 bis 50), dann ein Sprung
    auf 13,1 (t = 52).
  - Bilder |psi|^2: ab t = 100 ein grosser Klumpen (Zentraldichte 0,80 bis 0,83, Integral |psi|^2 ~ 3,3) und ein kleiner
    (0,13 bis 0,14, Integral ~ 0,73).
  - Der kleine Klumpen ist ein echter Ball: Ruhefrequenz ~ 0,937, also omega^2 ~ 0,88. Dazu gehoert Q ~ 1,43, passend zu
    Q_2 = 1,45.
- **D = 22, Q_1 im Ende-Fenster:** zwischen 3,162139 und 3,162798, bei Q_1(0) = 3,162136. Die Ladung pendelt also nur
  oberhalb des Startwerts; ihr Mittel liegt eine Amplitude darueber.
- **Gleitendes r bei D = 22:** Im Abstand von 100 Einheiten abgetastet springt es zwischen ~0,0007 und ~0,0027 hin und
  her (Schwebungsperiode ~199) und naehert sich 0,0017. Das letzte Fenster traf zufaellig einen Tiefpunkt (0,0002).

## 3. T0 bis T3

Alle Urteile gelten auf beiden Gittern gleich (Neurechnung mit S12f statt S12). Die Verfolgungspruefung bestand ueberall:
p1(T) und p2(T) liegen je hoechstens 1,0 von einem Bildmaximum > 0,1 entfernt.

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| T0 | Fuer alle D >= 10 ohne Verschmelzen fliesst Ladung vom kleinen zum grossen Ball (Q_1 steigt bis T = 3000) | 75 % | **eingetroffen** | Q_1,Ende - Q_1(0) = +0,925 / +0,230 / +0,00384 / +0,00033 (D = 10 / 12 / 18 / 22). Q_2 jeweils gleich viel tiefer. Kein D verschmolzen |
| T1 | r(D) positiv, faellt etwa exponentiell, Steigung von ln r gegen D in [-1,22; -0,61] | 50 % | **nicht eingetroffen** (knapp) | Alle r > 0 und streng fallend (erfuellt). Steigung -0,6021, also 0,008 zu flach. Zweitlesart (letztes 50er-Fenster): -0,7250, eingetroffen |
| T2 | Bei keinem D ruecken die Takte um 10 % oder mehr zusammen | 80 % | **eingetroffen** | Alle r > 0; kleinstes r = +0,0018 (D = 22). Die woertliche Lesart mit verschmolzenen D ergibt dasselbe, da keines verschmolz |
| T3 | Bei D = 8 verschmelzen die Baelle bis T = 3000 | 55 % | **nicht eingetroffen** | V1: Median d ueber [2900; 3000] = 766 (> 1,5); V2: zwei Maxima > 0,1 (0,80 und 0,13), 779 auseinander. Beruehrung mit d < 1,5 von t = 12 bis etwa 25, danach Trennung |

**Fit fuer T1** (Kleinste Quadrate, ln r gegen D, Punkte = gewertete D ohne Verschmelzen, dx 0,1):

| D | 8 | 10 | 12 | 18 | 22 |
|---|---|---|---|---|---|
| r | 5,3408 | 3,6085 | 1,0854 | 0,018822 | 0,0017815 |
| Residuum ln r | -0,485 | +0,327 | +0,330 | -0,112 | -0,061 |

- Steigung -0,6021, Achsenabschnitt 6,977. Mit S12f statt S12: -0,6021.
- Lokale Steigungen:
  - 8 nach 10: -0,196 (Saettigung im starken Bereich)
  - 10 nach 12: -0,601
  - 12 nach 18: -0,676
  - 18 nach 22: -0,589
  - Mit dem nicht gewerteten Punkt 14,6: 12 nach 14,6: -0,765; 14,6 nach 18: -0,607.
- Zweitlesart: Steigung -0,7250, Residuen -0,81 / +0,25 / +0,50 / +0,84 / -0,78. Sie haengt an r_letzt(22) = 0,00022,
  einem Tiefpunkt der Schwebungsmodulation.
- Empfindlichkeit (keine Regel, nur berichtet):
  - Mit korrigierter Zeitdehnung (r + 0,512 / 0,513 / 0,017 bei D = 8 / 10 / 12): -0,6103.
  - Ohne D = 8: -0,642.
  - Das formale Urteil liegt also innerhalb dieser Unsicherheiten auf der Grenze.

**Bedeutung gemaess Karte:**
- **T0 und T2 treffen ein:** "Schwach gekoppelte Q-Ball-Uhren laufen auseinander statt zusammen ('reich wird reicher'
  ueber Ladungsfluss)" [H, 1D, nur Phasenlage 0].
  - Der Nachsatz "Eine gemeinsame Zeit entsteht nur durch Verschmelzen" ist hier nicht neu geprueft. Kein Lauf endete
    verschmolzen; Verschmelzen kennen wir aus der Vorkarte (D = 6,6; 4,6).
- **T1 trifft formal nicht ein.** Die Kartenbedeutung "Schwanz-Ueberlapp-Effekt" ist damit nicht nach Regel belegt.
  Die Zahlen zeigen einen exponentiellen Abfall mit einer Steigung genau am flachen Rand (-kappa) des vorhergesagten
  Bereichs.
- **T2 trifft ein:** Kein Abstandsbereich mit Synchronisation.

## 4. Literaturcheck (L4)

Nach den Laeufen abgerufen, ab etwa 22:17 CEST.
- arxiv.org/pdf konnte WebFetch nicht lesen. Gelesen wurden daher die ar5iv-HTML-Fassungen des Volltexts, ueber
  Auszuege des WebFetch-Werkzeugs.
- Die Zitate stammen aus diesen Auszuegen und sind nicht Zeile fuer Zeile am PDF geprueft.

- **Battye, Sutcliffe, "Q-ball dynamics", hep-th/0003252, Nucl. Phys. B 590 (2000) 329, Abschnitt 3 (1D):**
  - Mechanisches Modell mit Rotationswinkeln, Gl. (3.8): "the sum of the rotation frequencies θ̇1+θ̇2 is conserved" und
    "the first Q-ball will have a higher frequency than the second Q-ball and, since we know that the charge of a Q-ball
    decreases with increasing frequency, then this corresponds to the charge of the first Q-ball decreasing and the
    charge of the second Q-ball increasing." [S]
    - Das ist phasengetriebener Ladungstransfer mit gegenlaeufiger Taktaenderung, wie bei uns.
    - Die Richtung folgt dort aus der Phasenlage. Das passt zu meiner Hypothese, dass das Vorzeichen an der Startphase
      haengt [H].
  - Fig. 9 (gleiche Ladungen, Phasendifferenz pi/9): "the novel process of charge transfer where the soliton in the left
    hand half plane loses charge to the one in the right hand half plane" und "Clearly the one which has lost charge is
    moving faster than the other." [S]
    - Das passt zu D = 8 bis 12: Der kleine, verlierende Ball fliegt schneller weg.
  - Gleiche Ladung, Phase 0: "The two Q-balls slowly attract and coalesce to form one larger Q-ball ... the charge
    deficit being carried away by the fission of two additional Q-balls." [S] Das entspricht C1/C2 der Vorkarte.
- **Axenides, Komineas, Perivolaropoulos, Floratos, hep-ph/9910388, Phys. Rev. D 61 (2000) 085006, Abschnitt III:**
  - "the system generically performs breather type oscillations with frequency equal to the difference of the internal
    qball frequencies" [S].
  - "the system slowly drifted to larger qball separations with a rate dependent on the parameter values" [S]. Das passt
    zu D = 14,6 und 18.
  - Ladungstransfer und eine Verschiebung der Schwebung gegen die freie Differenz berichtet der Auszug nicht [L?].
- **Bowcock, Foster, Sutcliffe, arXiv:0809.3895, J. Phys. A 42 (2009) 085403:**
  - Abschnitt 4: F = -16 cos(θ) ω'^4 e^(-2aω') mit "For two in-phase Q-balls, θ=0 and hence F<0, so there is an
    attractive force ..." [S]. Die Kraft faellt exponentiell mit Abstand mal Schwanzrate, also Einfach-Ueberlapp.
  - Abschnitt 5, integrabel: "the two Q-balls emerge at exactly the point in the breather cycle at which the individual
    charges are identical to the incoming charges".
  - Abschnitt 5, nicht integrabel: "This leads to a significant difference between initial and final charges in
    non-integrable models, and results in the charge exchange phenomenon." [S]
- **Antwort fuer L4:**
  - Bekannt [S]:
    - Ladungsdrift zwischen 1D-Q-Baellen mit gegenlaeufiger Taktaenderung
    - der Verlierer fliegt schneller
    - Schwebung mit der Differenzfrequenz
    - langsame Drift auseinander
    - exponentielle, phasenabhaengige Kraft
  - Nicht gefunden [L?]:
    - ein gemessenes Abstandsgesetz r(D) des Taktauseinanderlaufens
    - die Aussage, dass beim ruhenden Start mit Phase 0 stets der groessere Ball gewinnt
  - Unser Taktauseinanderlaufen ist damit eine modellspezifische Zahlenreihe zu einem bekannten Mechanismus [H].

## 5. Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Latten** (Zuordnung nach meiner Lesart; runden-v3/README.md liegt ausserhalb meiner Leseerlaubnis):
- L1, Lauf und Reproduktion: erreicht. Sieben Laeufe mit rc = 0; D = 14,6 bitgleich zu Z2 der Vorkarte.
- L2, Kontrollen: erreicht. Freie Werte aus K1 bis K4 der Vorkarte; Ladungserhaltung bei D >= 12 auf 1e-5;
  Verfolgungspruefung bestanden.
- L3, zweites Gitter bei D = 12: erreicht. r 1,0854 / 1,0861, dQ_1 0,2297 / 0,2301, Urteile gleich.
- L4: siehe Abschnitt 4.
- L5, Bezug zu Messdaten: nicht erreicht (reine 1D-Modellrechnung).

**Grenzen:**
- Nur 1D, nur M1, nur omega^2 = 0,60 / 0,65, ruhender Start und nur Phasenlage 0.
  - Das Vorzeichen des Ladungsflusses und damit von r kann an der Startphase haengen [H]; siehe Punkt 4 in Abschnitt 1.
  - In der Vorkarte (Z1, D = 6,6, Phasenlage pi) rueckten die Takte zusammen.
- Der Start ist eine Ueberlagerung. Die Interferenzladung bei t = 0 betraegt +8,9 % der Summe bei D = 8, +3,3 % bei 10,
  +1,2 % bei 12 und hoechstens 0,3 % ab 14,6.
- Die Zeitdehnung ist nicht korrigiert, wie geplant. Bei D = 8 und 10 senkt sie das gemessene Delta omega um 0,51
  Delta omega_frei; ab D = 14,6 ist sie kleiner als 1e-4.
- T3 haengt an der Zustandslesart "verschmolzen bei T" (Plan). In einer Prozesslesart ("bis T irgendwann
  verschmolzen") waere T3 wegen d < 1,5 ab t = 12 eingetroffen. Diese Lesart ist keine Regel.
- V2 nutzt Bilder alle 100 Einheiten. Die Beruehrung bei D = 8 (t = 12 bis 50) liegt zwischen zwei Bildern.
- T3 haengt auch an der vorab festgelegten V2-Schwelle 0,1. Der kleine Ball bei D = 8 hat bei T im Bild die Zentraldichte
  0,129. Bei einer Schwelle ueber 0,129 haette V2 "verschmolzen" gemeldet (Q ~ 1,45, also ein echter Ball, kein Splitter).
- T1 liegt auf der Bereichsgrenze; Empfindlichkeiten siehe Abschnitt 3.

**Selbstanzeigen:**
1. **Hintergrund-Ausgabedateien:** Fuer Hintergrundaufrufe und einen Monitor legte das Werkzeug unter
   /tmp/claude-1000/.../tasks/ Ausgabedateien an. Sie enthalten nur Log-Endzeilen und Zeitstempel. Ich habe dort nichts
   selbst geschrieben, sie entstanden aber durch meine Aufrufe.
2. **WebFetch-PDFs:** WebFetch auf arxiv.org/pdf hat drei PDFs unter ~/.claude/projects/.../tool-results/ gespeichert
   (Werkzeugverhalten). Ich habe sie nicht geoeffnet, sondern bin auf ar5iv ausgewichen.
3. **Syntaxpruefung:** Der erste Test auf der .69 lief per python -c mit py_compile(cfile=/dev/null) statt wie
   vorgegeben. Er scheiterte folgenlos. Danach habe ich wie vorgeschrieben python -m py_compile benutzt; das legte
   hilfs/__pycache__ im eigenen .69-Ordner an.
4. **Fremde Unitnamen:** Um den Laufstart abzulesen, habe ich auf der .69 `systemctl --user list-units
   "fmhc-physics-klein*"` aufgerufen. Dabei wurden auch Unitnamen eines anderen Auftrags sichtbar. Fremde Ordner habe ich
   nicht gelistet.
5. **Rauchlauf:** Er gehoert nicht zu den Kartenlaeufen. Er liegt nur auf der .69 unter rauch/ und wurde nicht
   kopiert.

**Laufzeiten** (Service runtime je Aufruf):
- dx 0,1: S08 91 s, S10 94 s, S12 92 s, S18 92 s, S22 87 s, S146 87 s.
- dx 0,05: S12f 222 s.
- Hilfsauswertung 1,7 s.
- Rauchlauf 19 s plus 0,5 s Hilfsauswertung.
- Wartezeit auf belegte Spuren bis knapp 3 min (S08, S10, S12 je etwa 2,8 min; S22, S146 je etwa 2 min).

**sha256:**
- Code der Vorkarte schwebung1d.py: bd0fd1b7ff5db656f8504d14a695b3a46e84c3a8a9051b3c57b113b368862c45 (lokal und auf
  der .69 gleich)
- hilfs/auswertung2.py: 1594ec42f21d36dfffcfaa18f9e486ed47ff6fd0e7efc31366dc14721e6e3c32 (lokal und auf der .69
  gleich)
- PLAN.md.eingefroren-20261002-220635: 5107a7c3e03a2d0f7b72b9d465bfe1011033db128caa82d77c2822d81bc75296 (= PLAN.md)
- lauf-69/S08.json 43adea6394fd4873c70266742149d9a32c9e2ad003d2c252b19ffbc4250c54ba
- lauf-69/S10.json c218fdf29ed16ecf2c4f8289de5a373e4f9b2f0c356733f27a85236bad9396e7
- lauf-69/S12.json 689568b7f7bb14d7116bcf8ba02f3b9d601cce48248527f2b03806a7454d1eac
- lauf-69/S12f.json 1fc7891c7156dea7edf033dceaa9a39375811adaea4261689ccec0eb4269e5db
- lauf-69/S146.json e5a4dc9b294d98e90583b617b40866e3457042972c208576e72baaa8ba34fdf2
- lauf-69/S18.json cd46835ceff5e6c3e11819f4f749fd35fa82263818267fdcc5726baf44478cca
- lauf-69/S22.json ec6796e6915a06c0387814082b27a52bcd07580488b14b75b9bdfcc27e97db1c
- lauf-69/auswertung2.json ea94f53338acbd654c8574536732f0699b2a7c0eb8a35a2b48e9707a72615625

Die JSON-Hashes stimmen lokal und auf der .69 ueberein (Praefixvergleich). Rohdaten liegen in lauf-69/*.roh.npz, Logs in
lauf-69/*.log und lauf-69/auswertung2.log.

## 6. Einfach gesagt

Zwei Wellenpakete, die je in ihrem eigenen Takt kreisen, sind wie zwei Uhren. Wir wollten wissen, ob sie sich
gegenseitig angleichen. Das tun sie bei keinem Abstand. Immer zieht der groessere dem kleineren etwas "Ladung" ab. Der
groessere wird dadurch langsamer, der kleinere schneller, und die Uhren laufen weiter auseinander. Liegen sie nah
beieinander, ist das ein grosser Raub: Danach stossen sie sich ab und fliegen davon. Liegen sie weit auseinander, ist der
Effekt winzig und wird pro vier Laengeneinheiten etwa zehnmal kleiner. Das ist fast genau so steil, wie wir vorhergesagt
hatten, aber eben um ein Haar zu flach fuer die Vorhersage. Wichtig ist eine Einschraenkung: Wir haben die Uhren nur "im
Gleichtakt" gestartet. Ob es bei einem anderen Start andersherum laeuft, ist noch offen.
