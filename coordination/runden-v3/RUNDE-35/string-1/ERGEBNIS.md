# STRING-1: Ergebnis (Code-Agent fuer claude-primary, Runde 35, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh, nur Spur cpu6, ein Lauf zugleich (1 Kern, MemoryMax 4G).
  - C-Kerne mit gcc -O2 auf der .69 uebersetzt, per ctypes geladen; Auswertung mit numpy/scipy/matplotlib. Die
    .69-Uhr laeuft in UTC; CEST = UTC + 2.
- **Rauchlaeufe** (rauch-69/): 19:19:07 bis 19:33:14 UTC (21:19 bis 21:33 CEST), in drei Teilen, alle offengelegt in
  PLAN.md Abschnitt 8.
- **Eingefroren** um 21:35:09 CEST (date). Die Pruefsummen stehen in code/PRUEFSUMMEN-eingefroren-20261003-213509.txt:
  - PLAN.md.eingefroren-20261003-213509: 4a958566
  - string_kern.c: 44ae6665
  - string_kern.so (auf der .69): 9aa1e7dd
  - string_mc.py: 0af56fa6
  - auswertung.py: 1f1f0a62
  - laeufe.sh: 2154a238
- **Hauptlaeufe** 19:35:09 bis 20:24:20 UTC (21:35:09 bis 22:24:20 CEST): 15 Laeufe und 2 Auswertungen, alle rc = 0.
  Alle 15 Ausgabedateien und beide Auswertungen melden genau die eingefrorenen Pruefsummen.
- **Nachtraeglich, nur beschreibend:** code/empfindlichkeit.py (sha256 97ea8a72, nicht eingefroren), 20:24:24 bis
  20:24:25 UTC. Es prueft die Fensterabhaengigkeit, den lokalen Exponenten und die Blockgroesse; siehe Selbstanzeige 4.
- **Rohdaten:** lauf-69/
  - je Lauf JSON, NPZ (Bloecke) und Log; kette.json (d = 1); gauss.json (Spinwellen-Referenz)
  - auswertung.json (mechanische Urteile), auswertung_zwischen.json (nach den S0-Laeufen, gleiche Urteile S0 bis S5)
  - empfindlichkeit.json (nachtraeglich)
  - Bild auswertung-F.png: F/T(r) je d und K mit Ausgleichen, d = 1 mit Paaren, S6
- Geschrieben ab 22:25:45 CEST (date); Zahlen aus lauf-69/auswertung.json und empfindlichkeit.json.

## 1. Ergebnis

1. **Aus "Punkte ergeben Striche" entstehen von selbst Strings, sobald Fluss teuer ist (K gross).**
   - d = 2, K = 2,5 (L = 128): F/T waechst linear mit 1/xi = 0,6795 (xi = 1,47 Gitterschritte).
     - Dazu kommt das Zittern mit a = 0,4955 +- 0,0022. Die Theorie [L, Ornstein-Zernike] sagt 1/2.
     - Der Wert ist robust: a = 0,494 bis 0,502 fuer jedes Fenster mit r >= 2 (L = 128); auf L = 64 a = 0,4980.
   - d = 3, K = 4,5 (L = 32): F/T waechst linear mit 1/xi = 1,853 (xi = 0,54).
     - Der Log-Anteil haengt am Fenster: a = 0,676 auf [2; 8], aber 0,537 auf L = 24 ([2; 6]).
     - Der lokale Exponent waechst von 0,17 (r = 2) auf 1,2 bis 1,4 (r = 7 bis 12). Der String ist hier sehr steif
       (Querschritt kostet e^-2,25 = 0,1) und kommt im Fenster erst ins Zittern.
     - Die String-Form beschreibt die Daten nur grob (chi^2 = 738 bei 4 Freiheitsgraden).
2. **Strings brechen, wenn ein neues Paar billiger ist.**
   - d = 1 exakt (J = 1, T = 0,5, mu = 3): Knick bei r_c = 10,47, Plateau F/T = 10,456.
     - Das ist bis auf 4e-5 der Wert 2 mu/T - 2 ln[(1 + e^-1)/(1 - e^-1)] = 12 - 1,544 = 10,456 [M] (der Rest
       stammt von Vakuumpaaren).
     - Die Paarladung darf auf beiden Seiten der festen Ladung sitzen. Die Karte (~11) und meine Plan-Handrechnung
       (11,08) zaehlten nur die Innenseite.
   - d = 3, K = 4,5, mu/T = 5,673 (2 mu/sigma = 5,99): F/T saettigt bei P = 9,667, ab r ~ 7 flach auf +-0,01.
     - Die Lagenentropie-Vorhersage P_pred = 2 mu/T - 2 ln chi_1 = 9,662 trifft auf 0,005.
     - Der Schnitt mit der String-Kurve liegt bei r_c = 4,57, also 0,76 * 2 mu/sigma: frueher als 2 mu/sigma, weil der
       String seinen Achsenabschnitt und Log-Anteil mitbringt.
3. **Ist Fluss billig (K klein), verteilt er sich.**
   - d = 2, K = 0,5: Logarithmus mit eta = 0,0767 +- 0,0017 (L = 128).
     - Die Spinwellen-Referenz auf demselben Torus gibt 0,0771; K/(2 pi) = 0,0796.
     - Der Torus drueckt den Wert um etwa 3 %; ein Wirbelbeitrag ist nicht sichtbar (Wurm gegen Referenz: -0,0004).
   - d = 3, K = 1,5: F/T saettigt (Q_sat = 0,059), Coulomb-Ausgleich mit C = 0,124 +- 0,007 (Referenz 0,130).
     - Der formale Vergleich ist trotzdem verfehlt: Die String-Form gewinnt nach AIC knapp (10,6 gegen 11,7). Sie tut
       das mit negativer Spannung 1/xi = -0,011 +- 0,002, ist also kein String.
     - Gegen die reine Gerade sigma r + c gewinnt Coulomb klar (AIC 11,7 gegen 94,9).
4. **Gegenprobe:** Wurm (Strommodell) und Villain-Winkelmodell stimmen in allen vier gerechneten Faellen innerhalb
   3 sigma. Gewertet sind d = 2, K = 2,5 (max |z| = 1,65) und d = 3, K = 1,5 (1,50); berichtet d = 2, K = 0,5 (2,20)
   und d = 3, K = 4,5 (1,16). Das Gauss-Gesetz war nach jedem Block an jedem Platz exakt erfuellt (0 Fehler).
5. **Bedeutung (nach Karte):** S1, S3 und S5 treffen ein (S3 mit Vermerk "nicht konvergiert"). Karte: "Die 'Punkte
   ergeben Striche'-Logik erzeugt von selbst Strings, sobald Fluss teuer ist. Sie zittern messbar (ln r) und brechen,
   wenn ein neues Paar billiger ist als ein langer String."
   - In d = 2 ist das Zittern quantitativ (a = 1/2).
   - In d = 3 ist es auf diesen Abstaenden nur im Entstehen; ob a asymptotisch 1 wird, bleibt offen [H].
   - S2 trifft ein; S4 formal nicht (siehe 3.). Karte: "Ist Fluss billig, verteilt er sich, und die Kraft wird
     Coulomb-artig." Die Saettigung und das C sind da. Verfehlt ist allein der Formvergleich gegen eine 3-Parameter-Kurve
     mit negativer Spannung, in einem von neun Fenstern (Selbstanzeige 4). Beschrieben, nicht umgedeutet: Das Urteil
     bleibt "nicht eingetroffen".
   - Alles ist synthetisch und weitgehend Lehrbuch (Gitter-Dualitaet, Ornstein-Zernike, String-Bruch) [L]. Es ist eine
     Vorfuehrung der Kraftgesetze am Modell, kein Messdatenbeleg.

## 2. Urteile (mechanisch nach dem eingefrorenen Plan; auch in lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Urteil | Werte (urteilendes L) | Kleineres L |
|---|---|---|---|---|
| S0 | Gauss-Gesetz exakt; d = 1 ohne Paare F = (J/2) r; Wurm = Winkelmodell innerhalb 3 sigma (90 %) | **eingetroffen** | Gauss-Fehler 0 in 8 Wurmlaeufen (je 51 Vollpruefungen); d = 1: max Abweichung 0,0; Villain max abs z = 1,65 (d = 2, K = 2,5, L = 64, 16 Abstaende) und 1,50 (d = 3, K = 1,5, L = 24, 6 Abstaende) | |
| S1 | d = 2, K = 2,5: String; AIC(String) < AIC(Log); a in [0,25; 0,75] (60 %) | **eingetroffen** | L = 128: AIC 11,5 gegen 1,98e7; a = 0,4955 +- 0,0022 | L = 64: a = 0,4980, gleiches Urteil |
| S2 | d = 2, K = 0,5: eta in [0,068; 0,092] (70 %) | **eingetroffen** | L = 128: eta = 0,0767 +- 0,0017 | L = 64: 0,0765 +- 0,0008 |
| S3 | d = 3, K = 4,5: String; AIC(String) < AIC(Coulomb); a in [0,6; 1,4] (55 %) | **eingetroffen**, Vermerk **nicht konvergiert** | L = 32: AIC 744 gegen 1,8e7; a = 0,676 +- 0,003 | L = 24: a = 0,537 +- 0,003, also nicht eingetroffen |
| S4 | d = 3, K = 1,5: saettigt; Coulomb besser als jeder lineare Ausgleich; C in [0,10; 0,36] (60 %) | **nicht eingetroffen**, Vermerk **nicht konvergiert** | L = 32: Q_sat = 0,059 (ja); AIC Coulomb 11,72, String 10,62, linear 94,95 (Coulomb nicht besser als String); C = 0,124 (ja) | L = 24: AIC 5,51 / 9,22 / 68,92, also eingetroffen |
| S5 | d = 1 mit Paaren: r_c in [10; 13] (85 %) | **eingetroffen** | r_c = 10,473 (Ast: Steigung 0,998, Abschnitt 0,004; Plateau 10,456) | |
| S6 | d = 3 mit Paaren (wahlweise): saettigt ab r_c (+-30 %) bei ~2 mu - T Lagenentropie (50 %) | **eingetroffen** | L = 24: Anstieg F(12) - F(9) = -0,002 (< 0,568); r_c = 4,57 gegen 5,99, Verhaeltnis 0,763 (Fenster 0,7 bis 1,3); P = 9,667 gegen P_pred = 9,662 | |

- **Ableitbarkeit:**
  - S5 und S0 (b) waren vorab ableitbar [M].
  - S2 folgte fast aus der Spinwellen-Referenz (PLAN.md Abschnitt 9).
  - S1, S3 und S6 waren nur durch die Rauchlaeufe angedeutet: S1 auf L = 64 (a = 0,490), S3 auf L = 24 (a = 0,547,
    also verfehlt), S6 auf L = 24 (Verhaeltnis 0,76). Die urteilenden Groessen 128 und 32 liefen erst nach dem
    Einfrieren.
  - S4 haette nach dem Rauchlauf auf L = 24 eingetroffen sein muessen; L = 32 kippt den Formvergleich.

## 3. Tabellen

**Ausgleiche** (Fenster r = 2..L/4 auf der Achse, gewichtet mit den Jackknife-Fehlern der Form y(r); Parameterfehler
Jackknife ueber 50 Bloecke; c umgerechnet auf normiertes F/T):

| d | K | L | Punkte | String: 1/xi | a | c | chi^2 | AIC String | AIC Log | AIC Coulomb | AIC linear |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2,5 | 128 | 31 | 0,67947 +- 0,00019 | 0,4955 +- 0,0022 | 0,345 | 5,5 | 11,5 | 1,98e7 | 8,57e7 | 62 106 |
| 2 | 2,5 | 64 | 15 | 0,67912 +- 0,00031 | 0,4980 +- 0,0018 | 0,342 | 14,0 | 20,0 | 6,25e6 | 2,75e7 | 64 360 |
| 3 | 4,5 | 32 | 7 | 1,85319 +- 0,00059 | 0,6760 +- 0,0026 | 0,171 | 738 | 744 | 4,26e6 | 1,78e7 | 29 929 |
| 3 | 4,5 | 24 | 5 | 1,89446 +- 0,00083 | 0,5365 +- 0,0028 | 0,190 | 223 | 229 | 1,71e6 | 6,91e6 | 10 945 |

| d | K | L | Log: eta | chi^2 Log | Coulomb: C | chi^2 Coulomb | String: 1/xi, a | chi^2 String | linear sigma | AIC Log / Coulomb / String / linear | Q_sat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 0,5 | 128 | 0,0767 +- 0,0017 | 32,9 | 0,551 | 1869 | -0,0006, 0,084 | 17,7 | 0,0053 | 36,9 / 1873 / 23,7 / 1639 | 0,113 |
| 2 | 0,5 | 64 | 0,0765 +- 0,0008 | 24,4 | 0,401 | 1994 | -0,0010, 0,084 | 6,3 | 0,0096 | 28,4 / 1998 / 12,3 / 2144 | 0,129 |
| 3 | 1,5 | 32 | 0,0303 +- 0,0019 | 39,9 | 0,1237 +- 0,0073 | 7,72 | -0,0114 +- 0,0015, 0,082 +- 0,007 | 4,62 | 0,0061 | 43,9 / 11,72 / 10,62 / 94,9 | 0,059 |
| 3 | 1,5 | 24 | 0,0387 +- 0,0015 | 16,4 | 0,1287 +- 0,0048 | 1,51 | -0,0089, 0,071 | 3,22 | 0,0101 | 20,4 / 5,51 / 9,22 / 68,9 | 0,051 |

**Spinwellen-Referenz** (Gitter-Greenfunktion auf demselben Torus, ohne Wirbel, gleiches Fenster):

| d | K | L | eta | C | Q_sat |
|---|---|---|---|---|---|
| 2 | 0,5 | 128 / 64 | 0,0771 / 0,0767 | | 0,103 / 0,129 |
| 3 | 1,5 | 32 / 24 | | 0,1303 / 0,1314 | 0,046 / 0,066 |

**F/T auf der Achse (Auszug, normiert; Fehler 0,0003 bis 0,005):**

| r | 1 | 2 | 4 | 8 | 16 | 32 |
|---|---|---|---|---|---|---|
| d = 2, K = 2,5, L = 128 | 1,0886 | 2,0481 | 3,7484 | 6,8114 | 12,5888 | 23,8038 |
| d = 2, K = 0,5, L = 128 | 0,1223 | 0,1778 | 0,2349 | 0,2878 | 0,3416 | 0,3867 |
| d = 3, K = 4,5, L = 32 | 2,2016 | 4,3542 | 8,5148 | 16,3919 | 30,6334 | |
| d = 3, K = 1,5, L = 32 | 0,2547 | 0,3186 | 0,3549 | 0,3650 | 0,3715 | |

**Wurm gegen Winkelmodell** (G(r) = Z(r)/Z(0) gegen <cos(theta_0 - theta_r)>, gleiches L, r = 1..L/4):

| Fall | gewertet | r | G Wurm (Beispiele) | G Villain | max abs z | Villain: Durchgaenge, Annahme |
|---|---|---|---|---|---|---|
| d = 2, K = 2,5, L = 64 | ja (S0) | 1..16 | 0,33678; 0,02357 (r = 4); 0,00110 (r = 8) | 0,33692; 0,02366; 0,00124 (+-0,00012) | 1,65 | 50 x 1061, 0,62 |
| d = 3, K = 1,5, L = 24 | ja (S0) | 1..6 | 0,7798; 0,7056 (r = 4); 0,6971 (r = 6) | 0,7774; 0,7039; 0,6969 | 1,50 | 50 x 331, 0,49 |
| d = 2, K = 0,5, L = 64 | nein (berichtet) | 1..16 | | | 2,20 (alle z > 0: Normierung des Wurms) | 50 x 1067, 0,51 |
| d = 3, K = 4,5, L = 24 | nein (berichtet) | 1..6 | | | 1,16 | 50 x 311, 0,81 |

- Villain-Abschnitt m = -3..3: Abweichung gegen m = -12..12 ist 0, Schranke <= 2,8e-23 (K = 4,5).

**r_c:**

| Fall | Ast | Plateau | r_c | Vorhersage | Verhaeltnis |
|---|---|---|---|---|---|
| d = 1 exakt (S5) | Gerade durch r = 1..6: 0,998 r + 0,004 | F/T(60) = 10,4562 (Aenderung 40 -> 60: 2e-13) | 10,473 | 2 mu/sigma = 12; mit beidseitiger Lagenentropie 10,456 | 0,87 bzw. 1,002 |
| d = 3, K = 4,5, L = 24 (S6) | String ohne Paare: 1,8945 r + 0,5365 ln r + 0,190 | Mittel F_h/T(9..12) = 9,667 | 4,572 | 2 mu/sigma = 2 * 5,673 * 0,5279 = 5,989 | 0,763 |

**S6, F_h/T mit Paaren (L = 24) gegen das Zwei-Zustands-Bild -ln(e^-F_0 + e^-P)** (nachtraeglich, beschreibend):

| r | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 12 |
|---|---|---|---|---|---|---|---|---|
| gemessen | 2,220 +- 0,008 | 4,364 +- 0,013 | 6,428 +- 0,017 | 8,252 +- 0,017 | 9,321 +- 0,012 | 9,616 +- 0,009 | 9,669 | 9,668 |
| Zwei Zustaende | 2,201 | 4,348 | 6,417 | 8,243 | 9,317 | 9,611 | 9,666 | 9,667 |

**Laeufe:**

| Lauf | Versuche | Blockgroesse | Anteil geschlossen | max abs n | <n^2> je Kante |
|---|---|---|---|---|---|
| Wurm d = 2, K = 2,5, L = 128 / 64 (b = 0,7) | 7,21e9 / 7,23e9 | 1,44e8 | 8,9e-4 / 2,6e-3 | 3 | 0,036 / 0,038 |
| Wurm d = 2, K = 0,5, L = 128 / 64 | 8,23e9 / 8,32e9 | 1,65e8 | 9,1e-5 / 3,5e-4 | 6 | 1,0001 / 1,0010 |
| Wurm d = 3, K = 4,5, L = 32 / 24 (b = 1,9) | 8,18e9 / 8,23e9 | 1,64e8 | 1,8e-3 / 3,3e-3 | 2 | 0,0013 / 0,0015 |
| Wurm d = 3, K = 1,5, L = 32 / 24 | 7,55e9 / 7,65e9 | 1,52e8 | 4,4e-5 / 1,0e-4 | 4 | 0,4411 / 0,4406 |
| Wurm mit Paaren d = 3, K = 4,5, L = 24 | 2,43e9 Kantenzuege, 2,43e9 Sprungversuche (9,5e8 angenommen) | 9,7e7 | | | |

- Je Lauf 50 Bloecke nach einem Einlauf von 8,4e8 bis 9,7e8 Schritten (Wurm mit Paaren 5,7e8); 3,5e7 bis
  4,0e7 Schritte/s (Wurm mit Paaren 2,4e7).

## 4. Kontrollen

- **Gauss-Gesetz (S0 a):** Vollpruefung an allen V Plaetzen nach dem Einlauf und nach jedem der 50 Bloecke, in allen
  8 Wurm-Hauptlaeufen: 0 Fehler. Ebenso im Wurm mit Paaren (div n = q + delta_M - delta_I): 0 Fehler.
- **d = 1 (S0 b):** ohne Paare max |F/T - (K/2) r| = 0,0 (r = 0..60). Kette N = 600 statt 400: 5e-14; Flussabschnitt
  +-16 statt +-8: 0. Uebertragungsmatrix gegen Abzaehlung aller Ladungsbelegungen (N = 6): 7,9e-16 (Rauchlauf).
- **Wurm gegen exakt (Rauchlauf):**
  - Ring d = 1, L = 8 gegen die Windungssumme: |z| <= 1,4.
  - Wurm mit Paaren gegen die exakte Spur mit Paarbildung: |z| <= 0,93.
  - Bias gegen ohne Bias: |z| <= 0,64.
- **Feldfaktor:** Villain mit Platzfaktor (1 + 2z cos theta) gegen die exakte Paarbildung (Ring): |z| <= 0,88. Die
  Herleitung h = 2 exp(-mu/T) der Karte stimmt in erster Ordnung; exakt ist 1 + 2z cos theta (PLAN.md Abschnitt 5).
- **Spinwellen-Grenzfall:** F/T(1) = 0,1223 bis 0,1241 (d = 2, K = 0,5) bzw. 0,2487 bis 0,2547 (d = 3, K = 1,5).
  Exakt in der Gauss-Naeherung ist K/(2d): 0,125 bzw. 0,25; die Abweichungen liegen in der Normierungsunsicherheit
  (+-0,002 bis 0,003).
  - <n^2> je Kante = 1,0001 (d = 2, K = 0,5); Gauss-Wert fuer divergenzfreie Felder (d - 1)/(d K) = 1 [M].
  - d = 3, K = 1,5: 0,4411 gegen 0,444. Die Ganzzahligkeit (Wirbelschleifen im Dualen) senkt den Wert etwas.
- **Blockgroesse** (nachtraeglich): Fehler mit 25 zusammengelegten Bloecken gegen 50 im Mittel 0,94 bis 1,16. Die
  Bloecke sind also laenger als die Autokorrelation.
- **Zwei Groessen:** d = 2 stimmt zwischen L = 64 und 128 in 1/xi auf 4e-4 und in a auf 0,003. d = 3, K = 4,5 nicht:
  a = 0,537 gegen 0,676, weil das Fenster mitwaechst (lokaler Exponent steigt mit r). F/T selbst stimmt zwischen
  L = 24 und 32 bei gleichem r auf 0,001 (z. B. r = 8: 16,3915 gegen 16,3919).
- **S6, Zwei-Zustands-Bild** (Tabelle oben): Das Bild "String oder gebrochen" erklaert die gemessene Kurve auf
  +-0,01 ab r = 3. Bei r = 1 bis 2 liegt die Messung 0,02 hoeher (1,3 bis 2,4 sigma), vermutlich aus der
  Normierung durch Z_h(0) mit nur 6,8e4 Zaehlern [H].
- **Latten (v3):**
  - L1 ja: S3 auf L = 24 und S4 auf L = 32 sind gescheitert, die Regeln konnten also scheitern.
  - L2 ja: Winkelmodell gegen Wurm, exakte Spuren, Spinwellen-Referenz, zwei Groessen.
  - L3 ja: Gauss-Gesetz, Abschnitte, Blockgroesse.
  - L4 ja: Dualitaet Strom/Villain [L: Jose, Kadanoff, Kirkpatrick, Nelson 1977; Savit 1980], Wurm
    [L: Prokof'ev/Svistunov 2001], Ornstein-Zernike-Vorfaktor [L], String-Bruch [L?: Bali u. a. 2005];
    Uebergangslagen [L?, nicht nachgelesen].
  - L5 nein: kein Messbezug.

## 5. Selbstanzeigen

1. **Rauchlaeufe auf Hauptgroessen.** Die Bias-Proben liefen auf L = 64 (d = 2) und L = 24 (d = 3), also auf den
   kleineren Hauptgroessen, mit anderen Seeds und 60 s statt 240 s. Ich habe sie vor dem Einfrieren gelesen und im Plan
   offengelegt. Sie zeigten S1 (a = 0,490) und S3 (a = 0,547, verfehlt) auf diesen L vorab, ebenso S6 (Verhaeltnis
   0,76). Fenster, Formen, AIC und Regeln standen im Planentwurf, bevor ich diese Ausgaben las (Entwurf 21:26 CEST),
   die Kleingitter-Rauchlaeufe (L = 32, 16) hatte ich vorher gesehen. Die urteilenden Groessen 128 und 32 liefen nur
   nach dem Einfrieren.
2. **Nach den Rauchlaeufen geaendert (vor dem Einfrieren):**
   - Bias-Norm Euklid -> Maximum (Effizienz, kein Erwartungswert).
   - S6 vom Winkelmodell auf den Wurm mit Ladungszuegen, weil das Winkelmodell den Knick bei G ~ e^-10 nicht aufloest.
     Der Code dafuer (wurm_paare_laufe, gauss_pruefen_q, s6 in auswertung.py) entstand erst nach den ersten
     Rauchlaeufen und wurde vor dem Einfrieren gegen exakte Spuren geprueft.
   - mu/T fuer S6 aus dem Rauchlauf (so verlangt die Karte).
   - Keine Schwelle der Karte geaendert, kein Code nach dem Einfrieren geaendert.
3. **Handrechnung im Plan war falsch (S5):** PLAN.md Abschnitt 9 sagt Plateau 11,08 und r_c ~ 11,1. Richtig ist
   10,456: Die Paarladung kann auch auf der Aussenseite der festen Ladung sitzen. Die Karte ("~11") hat dieselbe
   Luecke. Das Urteil S5 haengt nicht daran (10,47 liegt im Intervall).
4. **Nachtraegliche Empfindlichkeit** (empfindlichkeit.py, nicht eingefroren, aendert kein Urteil):
   - **S4:** Von neun Fenstern (r_min 1 bis 4, r_max 4 bis 12) auf L = 32 ist das eingefrorene [2; 8] das einzige, in
     dem die String-Form nach AIC gewinnt (um 1,1). In den anderen acht gewinnt Coulomb (um 0,7 bis 58,5). Die
     String-Form hat in allen Fenstern 1/xi < 0. C liegt je nach Fenster bei 0,089 bis 0,134.
   - Ich hatte das Risiko im Schreibtisch gesehen (Gitterkorrekturen bei r = 2 gegen eine 3-Parameter-Form) und im
     Plan nur als "nicht vorab entschieden" vermerkt. Eine Bedingung 1/xi >= 0 fuer "linear" habe ich nicht
     festgelegt. Mit ihr (nachtraeglich) waere die String-Form der Log-Ausgleich (AIC 43,9), und Coulomb gewaenne.
   - **S3:** a haengt stark am Fenster. Auf L = 32: [2; 8] gibt 0,676, [3; 8] 0,855, [4; 8] 0,995, [2; 12] 0,846.
     Der lokale Exponent aus drei Nachbarpunkten: 0,17 / 0,39 / 0,63 / 0,88 / 1,04 / 1,17 / 1,32 / 1,26 / 1,33 / 1,36 /
     1,21 fuer r = 2..12. Das Urteil "eingetroffen" haengt also an der Gittergroesse (Vermerk) und am Fenster.
   - **S1** ist robust: a = 0,494 bis 0,502 (L = 128) bzw. 0,490 bis 0,526 (L = 64) fuer alle Fenster mit
     r_min >= 2. Der lokale Exponent liegt fuer r = 3 bis 10 bei 0,38 bis 0,58.
   - **S2** ist robust: eta = 0,069 bis 0,081 in allen Fenstern, also im Intervall.
5. **Saettigungsmass schwaecher als im Plan behauptet.** Der Plan schrieb, ein Logarithmus gebe Q_sat ~ 0,4 bis 0,7.
   Gemessen ist Q_sat = 0,11 bis 0,13 fuer d = 2, K = 0,5 (Referenz 0,10 bis 0,13; den Rauchwert auf L = 32 hatte ich
   falsch abgelesen). Q_sat < 0,2 trennt auf diesen Tori also nur "saettigt/waechst logarithmisch" von "linear", nicht
   Coulomb von Logarithmus. Fuer S4 aendert das nichts (Q_sat = 0,059 erfuellt, verfehlt ist der Formvergleich).
6. **S2 ohne Formvergleich.** Fuer d = 2, K = 0,5 hat die String-Form ein kleineres AIC als die Log-Form (23,7 gegen
   36,9), mit 1/xi = -0,0006. Sie faengt die Torus-Kruemmung ein. Die Karte verlangt fuer S2 nur eta; ich habe keinen
   Formvergleich hinzugefuegt.
7. **S0-Vergleiche:** Gewertet sind nur d = 2, K = 2,5 und d = 3, K = 1,5. Die beiden Zusatzvergleiche (max |z| 2,20
   und 1,16) bestehen ebenfalls. Der Vergleich d = 2, K = 0,5 hat alle z > 0, also eine gemeinsame Verschiebung durch
   die Wurm-Normierung (Z(0) mit 2,9e6 Zaehlern).
8. **Wortlaut "F = (J/2) r":** geprueft als F/T = (K/2) r mit K = J/T = 2, also F/T = r.
9. **Uhrzeiten:** Laufzeiten aus den .69-Logs (UTC), CEST umgerechnet; alle anderen Zeiten per date.
10. **Zeitbox:** Beginn 21:02:53 CEST; Hauptlaeufe fertig 22:24:20; dieser Bericht ab 22:25:45.

## 6. Einfach gesagt

Finn fragte, ob aus "Punkte ergeben Striche" von selbst wackelnde Strings werden, die reissen, wenn sie zu lang werden.
Wir haben Fluss auf den Kanten eines Gitters gerechnet: Kostet jedes Stueck Fluss viel Energie, bleibt der Fluss
zwischen zwei Ladungen in einem duennen Schlauch, und die Energie waechst wie bei einem gespannten Gummiband gleichmaessig
mit dem Abstand. Der Schlauch zittert dabei seitlich; in der Flaeche genau so stark, wie die Theorie es sagt, im Raum
faengt das Zittern auf den gerechneten Abstaenden erst an. Duerfen neue Ladungspaare entstehen, reisst der String, sobald
ein neues Paar billiger ist als das lange Stueck: in der Kette bei etwa 10,5 Schritten, im Raum schon bei etwa 4,6, und
danach bleibt die Energie konstant. Ist Fluss billig, verteilt er sich wie bei elektrischen Ladungen; nur der strenge
Kurvenvergleich im Raum ging knapp an eine Kurve ohne echte Spannung verloren, und alles ist ein Modell, keine Messung.
