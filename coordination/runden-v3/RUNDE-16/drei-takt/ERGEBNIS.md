# ERGEBNIS drei-takt (Runde 16, Code-Agent)

- Zeitbox ab 2026-10-02 08:33:37 CEST (date). Plan eingefroren 08:47:17 CEST (PLAN.md.eingefroren-20261002-084717).
- Begonnen ab 2026-10-02 08:52:10 CEST (date), schrittweise gefuellt; letzte Aenderung siehe Dateiende.

## 1. Ergebnis zuerst

1. **H1 (zwei bearbeiten ein drittes: eine Zeitlang stabil): gestuetzt im Phasenmodell D2a.** Knapp ausserhalb der
   Rastung bleibt der Dritte jeweils eine Zeitlang gerastet, die Dauer waechst zur Grenze wie (Abstand)^(-1/2)
   (Steigung -0,5001; Adler-Formel auf 2e-9 getroffen). In der Gravitation (D1b) nur **teilweise**: endliche
   Lebensdauern oberhalb der Routh-Grenze, aber kein solches Gesetz; das Herausfallen beginnt schon unterhalb der Grenze.
2. **H2 (Einfluss im gleichen Takt stabilisiert): teilweise.** Im Phasenmodell (D2b) nur bei exakt gleichem Takt und
   passender Phase (in Phase rastet ein, gegenphasig nie, anderer Takt rastet nicht an A/B). In der Gravitation (D1a,
   D1d) wirkt derselbe Takt in beide Richtungen: er zerstoert Stabilitaet in breiten Resonanzzungen und schafft
   Stabilitaet jenseits der Routh-Grenze (D1a nur ein schmaler Streifen bis mu = 0,0458; D1d breite Fenster, am
   haeufigsten nahe der Eigenfrequenz).
3. **H3 (aeusserer Einfluss erzeugt Chaos im Dreiersystem): gestuetzt im Phasenmodell D3.** Drei Taktgeber mit
   aeusserem Takt: 38 von 40 nachgerechneten Kandidaten robust chaotisch (lambda_max bis 0,29); ohne Takt an 2000
   Punkten nie (max 0,0022). Zwei mit Takt: nie (max 0,0024). Vier ohne Takt: auch chaotisch (39 von 40 robust).
4. **Drei ist die kleinste Zahl, bei der ein aeusserer Takt Chaos moeglich macht**, aber nicht besonders: Es braucht
   mindestens drei unabhaengige Phasenunterschiede (Takt mitgezaehlt), das erfuellen auch vier ohne Takt. In der
   Gravitation (D1c) ist H3 **offen** (zu wenig Bahnen, kein klarer Anstieg).
5. **Leitfrage: ja, die Antwort haengt am Systemtyp.** Gedaempfte Phasenmodelle geben glatte, exakt pruefbare Antworten;
   im konservativen Dreikoerperproblem hilft und schadet derselbe Takt je nach Massenverhaeltnis und Frequenz.

## 2. Versuche

### D1a: Exzentrizitaet als Takt im Umlauftakt (linear, Floquet)

- Gleichungen wie Karte. Schreibtischpruefung: Hesse-Matrix bei L4 aus Omega = (x^2+y^2)/2 + (1-mu)/r1 + mu/r2 gibt
  3/4, 9/4, (3 sqrt3/4)(1-2mu); bei e = 0 folgt lambda^4 + lambda^2 + (27/4) mu(1-mu) = 0. Kein Konventionsunterschied.
  Zusatz (eigene Rechnung): Die Eigenwerte der Hesse-Matrix sind (3 +- sqrt(9 - beta))/2 mit beta = 27 mu(1-mu). Das ist
  die Form des "wesentlichen Teils" der elliptischen Lagrange-Loesung, deren Stabilitaet nur von beta und e abhaengt
  (Hu, Long, Sun, arXiv:1206.6162, nur Abstract gelesen). Dass das eingeschraenkte Problem genau dieser Teil ist, ist
  Gedaechtnis [L?].
- Numerik: RK4, n = 2000 und 4000 Schritte je 2 pi; Gitter A (121 x 121) und B (241 x 241); Bisektion (14 Schritte,
  n = 4000, Gitter A als Start).
- Kontrollen (e = 0): Bisektion mu_R = 0,0385209 (Intervall 3e-8; exakt 0,03852090). Multiplikatoren gleich
  exp(2 pi lambda_k) aus der Eigenwertgleichung auf <= 1,3e-12 (8 Werte von mu, n = 4000). Bei mu = 0,0285955 liegen zwei
  Multiplikatoren bei -1 (max|rho| - 1 = 4e-13). Zungenraender bei e = 0,005: 0,028314 und 0,028878, Mitte 0,028596
  (Spitze 0,0285955). det M - 1 <= 3,3e-10 auf allen Gittern.
- Numerische Gegenproben: n = 2000 gegen 4000 und eigvals gegen charakteristisches Polynom weichen nur in der Spalte
  mu = 0 ab (A: 42 bzw. 121, B: 80 bzw. 237 Punkte; alle bei mu = 0). Dort ist der Grenzfall entartet (vierfacher
  Multiplikator 1 mit Jordan-Block, max|rho| - 1 ~ 1e-6 aus Rundung); mu = 0 wird nicht gewertet. tol 1e-6 gegen 1e-4:
  A 0, B 4 Punkte. Gitter A gegen B an 14641 gemeinsamen Punkten: 0 Abweichungen.
- Querkontrolle D1d bei Omega = 1 gegen D1a (erste Ordnung in e): Zungenraender D1d(eps 0,02) 0,02751/0,02976 gegen
  D1a(e 0,02) 0,027473/0,029730; eps 0,04: 0,02649/0,03101 gegen 0,026364/0,030875 (Unterschied O(e^2)).
- Ergebnis (Bisektion, n = 4000; Gitter B bestaetigt auf 0,00025):

| e | Zunge links | Zunge rechts | rechte Stabilitaetsgrenze | stabil oberhalb mu_R |
|---|---|---|---|---|
| 0 | - | - | 0,038521 | nein |
| 0,06 | 0,025269 | 0,032030 | 0,038811 | 0,038521 bis 0,038811 |
| 0,1 | 0,023126 | 0,034364 | 0,039329 | bis 0,039329 |
| 0,2 | 0,018077 | 0,040280 | 0,041816 | 0,040280 bis 0,041816 |
| 0,24 | 0,016199 | 0,042647 | 0,043321 | 0,042647 bis 0,043321 |
| 0,28 | 0,014410 | 0,044994 | 0,045144 | 0,044994 bis 0,045144 |
| 0,3 | 0,013550 | - | - | nein (alles mu > 0,01355 instabil) |

- Gitter B: stabile Punkte mit mu > mu_R und e > 0: 378 (n = 2000 und 4000 gleich), e von 0,055 bis 0,2925, groesstes
  stabiles mu 0,04575 bei e = 0,2925. Das ist 1,8 % der Flaeche oberhalb mu_R. Unterhalb mu_R (mu > 0) sind bei e > 0
  59 % der Punkte instabil, die bei e = 0 alle stabil sind.
- Lesart: Der Umlauftakt (Exzentrizitaet) zerstoert die Stabilitaet in einer breiten Zunge ab mu = 0,0286 (dort ist die
  langsame Librationsfrequenz 1/2, also Parametererregung 2 s2 = 1) und schafft zugleich einen schmalen stabilen
  Streifen oberhalb der Routh-Grenze, bis mu = 0,0458 bei e ~ 0,29. Abbildung: abb/d1a_karte.png.

### D2: zwei Schrittmacher und ein Dritter (Phasenmodell)

- D2a (H1, ohne Takt, 42 Punkte, K = 0,5 und 1, Abstand |Delta| - 2K = 1e-4 bis 1): gemessene Rastdauer (Zeit zwischen
  Phasenspruengen) gegen Adler 2 pi/sqrt(Delta^2 - 4K^2): groesste relative Abweichung 2,4e-9 (Kontrolle 1 %
  bestanden). Steigung im log-log fuer die fuenf kleinsten Abstaende: -0,50007 (K = 0,5) und -0,50004 (K = 1).
  Beispiele K = 0,5: Abstand 1e-4 -> 444,28 Zeiteinheiten (20 Spruenge), 1e-3 -> 140,46, 0,1 -> 13,71.
- D2b (H2, K = 0,5, Delta = 1,1, also 0,1 ausserhalb der Rastung; Takt Omega = 1 wie A und B):
  - Karte (psi, F), 72 x 51 Punkte: gerastet (kein voller Phasensprung in 2000 Zeiteinheiten nach 500 Einschwingen)
    stimmt an 100 % der Punkte mit der Zeigerformel |2K + F e^{i psi}| > |Delta| ueberein (auch ausserhalb eines
    Randstreifens 0,01: 100 %).
  - psi = 0 (in Phase): Rastung ab F = 0,1 = |Delta| - 2K. psi = pi (gegenphasig): bei keinem F bis 0,5 gerastet.
    32 % der Karte gerastet.
  - Karte (Omega, F), psi = 0, Omega 0 bis 2 in Schritten 0,02: C rastet an A/B nur bei Omega = 1,00 (41 Punkte,
    alle F >= 0,1; 0,8 % der Karte). Bei anderem Takt zieht der Takt C auf seine eigene Frequenz (26 % der Karte
    "rastet am Takt"), sonst Drift.
- Lesart: Ein aeusserer Takt hilft genau dann, wenn er den gleichen Takt UND die passende Phase hat; die Antriebe
  addieren sich wie Zeiger. Gegenphasig schadet derselbe Takt. Abbildung: abb/d2_karten.png.
- D2c (explorativ; omega_A = 0,8, omega_B = 1,2, omega_C = 1,1, K = 0,15; Omega 0,5 bis 1,5, F 0 bis 0,5): Schon
  ohne Takt rastet C an B (mittlere Frequenz 1,2003, Lyapunov-Exponent der C-Phase -0,077), weil omega_C naeher an
  omega_B liegt (|1,1 - 1,2| < K). Mit Takt: 94 % der Karte phasenstabil; C laeuft mit B in 33 %, mit dem Takt in 30 %,
  mit A in 4,8 %, in der Mitte (1,0) in 2,3 %, sonst 29 %. Die Frage "hilft ein Takt" ist mit diesen Parametern
  schlecht gestellt (C war schon gefangen); Selbstanzeige in Abschnitt 4.

### D1b: Lebensdauer oberhalb der Routh-Grenze (kreisfoermig, nichtlinear)

- 15 Werte mu von 0,0386 bis 0,05, Auslenkung 0,005 und 0,02, je 64 Richtungen, Startgeschwindigkeit null im
  mitrotierenden System, RK4 400 Schritte je Umlauf, bis 1000 Umlaeufe; Ende bei Abstand zu L4 > 0,5 oder r2 < 0,05
  (r2 < 0,05 kam nie vor).
- Kontrollen: Jacobi-Konstante relativ fuer alle bis zum Ende gebundenen Teilchen <= 2,1e-11 (Grenze 1e-9), Median
  ueber alle Teilchen <= 2e-11. Stichprobe mit dt/2 (mu 0,0386, 0,039, 0,042; 16 Richtungen): siehe Abschnitt 4.
- Kontrolle unterhalb mu_R (PLAN-NACHTRAG-3, nach dem Hauptlauf beschlossen): gleiches Protokoll bei mu = 0,030,
  0,035, 0,038.

| mu | Auslenkung | Anteil nach 1000 Umlaeufen in der 0,5-Kugel | Median-Lebensdauer (Umlaeufe) | lineare Anwachszeit (Umlaeufe) |
|---|---|---|---|---|
| 0,030 (stabil) | 0,005 | 100 % | > 1000 | - |
| 0,030 (stabil) | 0,02 | 20 % | 3,5 | - |
| 0,035 (stabil) | 0,005 | 100 % | > 1000 | - |
| 0,035 (stabil) | 0,02 | 17 % | 1,8 | - |
| 0,038 (stabil) | 0,005 | 64 % | > 1000 | - |
| 0,038 (stabil) | 0,02 | 13 % | 1,4 | - |
| 0,0386 | 0,005 | 61 % | > 1000 | 46 |
| 0,0386 | 0,02 | 13 % | 1,4 | 32 |
| 0,0390 | 0,005 | 50 % | > 1000 (Grenzfall) | 19 |
| 0,0393 | 0,005 | 41 % | 87 | 14 |
| 0,0396 | 0,005 | 31 % | 9,1 | 12 |
| 0,0400 | 0,005 | 19 % | 5,9 | 10 |
| 0,0405 | 0,005 | 0 % | 3,3 | 9 |
| 0,0420 | 0,005 | 0 % | 3,2 | 7 |
| 0,0500 | 0,005 | 0 % | 2,3 | 4 |
| 0,0405 bis 0,05 | 0,02 | 0 % | 1,3 bis 1,2 | 6 bis 2 |

- Fit log(Median) gegen log(mu - mu_R) ueber die mu, bei denen alle entkommen (0,0405 bis 0,05, 8 Punkte):
  Steigung -0,24 (Auslenkung 0,005) und -0,06 (0,02), nicht -1/2.
- Die gebundenen Teilchen sind nicht "nahe" L4: groesste Auslenkung im Median 0,31 bis 0,36, hoechstens 0,46 bis 0,50
  (Start 0,005). Schon unterhalb mu_R (mu = 0,030) waechst die Auslenkung 0,005 auf im Median 0,16.
- Lesart: Mit dem Kriterium der Karte misst D1b das nichtlineare Herausfallen aus einem Gebiet, das mit mu stetig
  schrumpft, nicht die lineare Instabilitaet. Bei Auslenkung 0,02 fallen auch linear stabile Faelle (mu = 0,030) zu
  80 % nach wenigen Umlaeufen heraus. Bei 0,005 steigt der Anteil der Entkommenen stetig durch mu_R hindurch
  (36 % bei 0,038, 39 % bei 0,0386, 50 % bei 0,039, 81 % bei 0,040, 100 % ab 0,0405). Abbildung: abb/d1b_lebensdauer.png.

### D1d: Takt mit frei waehlbarem Omega (e = 0, linear, Floquet)

- 6 x 61 x 981 = 359046 Punkte (mu, eps, Omega), RK4 mit h <= 0,01 in t (mindestens 400 Schritte je Periode) und mit
  doppelter Schrittzahl: 0 Abweichungen in der Einstufung, groesster Unterschied in max|rho| 8,5e-7; det M - 1 <= 2,7e-8.
- Unterhalb mu_R (mu = 0,01; 0,02; 0,035), Eigenfrequenzen s1/s2 = 0,963/0,268; 0,918/0,396; 0,805/0,593:
  - Zungen bei 2 s_k/n (n = 1, 2, 3) und bei der Differenz (s1 - s2)/n. Beispiel mu = 0,01, eps = 0,05: max|rho| 1,15 bei
    2 s1, 1,16 bei 2 s2, 1,29 bei s1 - s2, 1,07 bei (s1 - s2)/2; bei der Summe s1 + s2 stabil (1,0). Ebenso mu = 0,02
    (s1 - s2: 1,67; s1 + s2: 1,0). Bei mu = 0,035 verschmelzen die Zungen bei eps = 0,05 (1,08 bis 1,76), die Summe ist
    dort nicht trennbar. Das passt zur vorab notierten Krein-Erwartung (entgegengesetzte Signaturen).
  - "Gleicher Takt" Omega = s_k (Zunge zweiter Ordnung): schmal instabil ab eps ~ 0,1 (mu = 0,01: Omega = 0,97,
    max|rho| 1,022; mu = 0,02: 0,93). Haupttakt Omega = 2 s_k breit instabil.
  - Schneller Takt Omega > 3: bei keinem eps instabil. Anteil instabiler Omega bei eps = 0,3: 18 bis 21 %.
- Oberhalb mu_R (mu = 0,039; 0,040; 0,042; bei eps = 0 alles instabil): ein Takt macht L4 in breiten Bereichen stabil.

| mu | kleinstes eps, das stabilisiert (bei Omega) | Anteil stabil bei eps = 0,1 / 0,3 | stabil je Omega-Band (alle eps > 0): 0,2-0,6 / 0,6-0,8 / 0,8-1,2 / 1,2-1,6 / 1,6-3 / 3-10 |
|---|---|---|---|
| 0,039 | 0,01 (1,33) | 20 % / 67 % | 19 / 49 / 30 / 0,9 / 57 / 29 % |
| 0,040 | 0,025 (0,20 bis 0,25) | 10 % / 30 % | 15 / 41 / 23 / 0,1 / 43 / 7,5 % |
| 0,042 | 0,035 (0,21 bis 0,22) | 3,8 % / 14 % | 11 / 31 / 16 / 0 / 28 / 0,9 % |

  - Stabile Fenster bei eps = 0,1, mu = 0,040: Omega 0,45-0,54, 0,56-0,60, 0,63-0,75, 0,79-1,09, 1,83-2,24; bei eps = 0,3:
    2,23-5,17. Der Realteil der Eigenfrequenz liegt nahe 1/sqrt2 = 0,707; das Band um 2 x 0,707 (1,2-1,6) stabilisiert
    fast nie.
- Lesart: Unterhalb der Grenze schadet der Takt in Resonanzzungen (auch beim "gleichen Takt" Omega = s_k, schwach).
  Oberhalb der Grenze hilft ein Takt nahe der Eigenfrequenz (0,6-0,8) am haeufigsten, ein schneller Takt (Omega > 3)
  nur bei mu knapp ueber mu_R. Abbildung: abb/d1d_zungen.png.

### D3: Chaos, zwei gegen drei (Kuramoto-Sakaguchi mit Takt)

- Stichproben (RK4 dt 0,02, Einschwingen 500, Messung 2000; Parameter wie PLAN):

| Fall | Punkte | lambda_max groesster Wert | > 0,005 | > 0,01 | > 0,05 | nachgerechnet | robust (alle drei Varianten ueber Schwelle) |
|---|---|---|---|---|---|---|---|
| N = 2 mit Takt | 2000 | 0,0024 | 0 | 0 | 0 | - | - (nichts ueber 0,005) |
| N = 3 ohne Takt | 2000 | 0,0022 | 0 | 0 | 0 | - | - (nichts ueber 0,005) |
| N = 3 mit Takt | 2000 | 0,290 | 103 | 97 | 65 | 40 groesste | 38 von 40 (alle 38 auch > 0,05) |
| N = 4 ohne Takt | 1000 | 0,157 | 49 | 43 | 14 | 40 groesste | 39 von 40 (14 auch > 0,05) |

- Nachrechnung (code/d3_nach.py, PLAN-NACHTRAG-1): Varianten dt/2, doppelte Messzeit (beide mit den urspruenglichen
  Anfangswerten) und andere Anfangswerte. Code-Pruefung: lambda(T) im Nachrechenlauf gibt die Stichprobe exakt wieder
  (Abweichung 0,0). Bester Punkt N = 3 mit Takt: 0,290 / dt/2 0,289 / 2T 0,286 / andere AB 0,306. Bester Punkt N = 4
  ohne Takt: 0,157 / 0,168 / 0,167 / 0,169. Median |dt/2 - Stichprobe| 0,012 (N = 3) und 0,0035 (N = 4).
- Die zwei Faelle, in denen nach der Theorie kein Chaos moeglich ist (Fluss auf einem 2-Torus), bleiben an allen
  4000 Punkten unter 0,0025: Kontrolle des Codes bestanden. Regulaere Bahnen liegen erwartungsgemaess knapp ueber
  null (ln(T)/T ~ 0,004).
- Abweichung: N = 4 ohne Takt nur 1000 statt 2000 Punkte (zweiter Aufruf, Seed 22, aus Zeitgruenden nicht gerechnet;
  NACHTRAG-1 sieht das vor). Bei mehr als 40 Treffern wurden nur die 40 groessten nachgerechnet (97 bzw. 43 Treffer).
- Lesart: Drei Taktgeber ohne aeusseren Takt und zwei mit Takt koennen nicht chaotisch werden; drei mit Takt (und vier
  ohne Takt) werden robust chaotisch: bestaetigt an mindestens 1,9 % (38 von 2000) bzw. 3,9 % (39 von 1000) der
  Parameterpunkte; Kandidaten gab es an 4,9 % bzw. 4,3 %. Abbildung: abb/d3_lyapunov.png.

### D1c: Chaos nahe L4 im elliptischen Problem (nur Zusatz, wenig Bahnen)

- 4 x 4 Paare (mu, e), je 8 Bahnen (Auslenkung 0,005 und 0,02, 4 Richtungen), 1000 Umlaeufe, Abbruch bei r1 oder
  r2 < 0,05 oder Abstand > 3. Referenz fuer regulaere Bahnen ln(T)/T = 0,0014 (je Bogenmass f).
- Gebundene Bahnen, mittlere endliche Lyapunov-Zahl fuer e = 0 / 0,05 / 0,1 / 0,2:
  mu = 0,001: 0,00075 / 0,0011 / 0,0027 / 0,0010 (gebunden 6/5/5/4 von 8); mu = 0,01: 0,00061 / 0,00061 / 0,00050 /
  0,00072 (6/6/5/3); mu = 0,02: 0,00091 / 0,0018 / 0,00091 / - (5/4/2/0); mu = 0,03: 0,0011 / - / - / - (4/0/0/0).
  Groesster Einzelwert 0,0097 (mu 0,001, e 0,1, Auslenkung 0,02).
- Lesart: e vergroessert vor allem den Anteil der Bahnen, die das Gebiet verlassen (bei mu = 0,03 alle ab e = 0,05,
  passend zur Zunge in D1a). Die Lyapunov-Zahl der gebundenen Bahnen bleibt meist auf dem Niveau regulaerer Bahnen;
  ein klarer Anstieg im Mittel ist mit 8 Bahnen je Paar nicht zu sehen.

### Vorab gegen Ausgang (alle Vorhersagen der Karte)

| Nr | Vorhersage (Leitung, vorab) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| K | Kontrollen D1 bei e = 0 auf 1e-4; D2 trifft Adler auf 1 % | 98 % | eingetroffen | mu_R auf 1e-8, Multiplikatoren auf 1,3e-12, Zungenspitze 0,028596, Jacobi <= 2,8e-11, Adler 2,4e-9 |
| D1a-1 | e > 0 macht stabile Faelle instabil (Zunge ab 0,0286) | 95 % | eingetroffen | Zunge bei e = 0,1: 0,0231 bis 0,0344; 59 % der Flaeche unter mu_R bei e > 0 instabil |
| D1a-2 | e > 0 macht irgendwo oberhalb mu_R stabil | 35 % | eingetroffen | 378 Gitterpunkte, e 0,055 bis 0,29, bis mu = 0,04575 (1,8 % der Flaeche) |
| D1d-1 | Zungen bei 2 omega_k/n und omega_s +- omega_l; gleicher Takt destabilisiert | 90 % | eingetroffen (Kombination nur als Differenz) | Zungen bei 2 s_k/n und (s1 - s2)/n; bei s1 + s2 keine (mu 0,01; 0,02); Omega = s_k schwach instabil ab eps ~ 0,1 |
| D1d-2 | Stabilisierung oberhalb mu_R, wenn, dann schnell (Kapitza), nicht der gleiche Takt | 60 % | nicht eingetroffen | haeufigste Fenster bei Omega 0,6-0,8 (31-49 %) und 1,6-3 (28-57 %); Omega > 3 nur 1-29 %; kleinstes eps bei Omega 1,33 bzw. 0,2 |
| D1b-1 | Lebensdauer endlich, ~ (mu - mu_R)^(-1/2) | 55 % | nicht eingetroffen | Steigungen -0,24 und -0,06; Kriterium misst nichtlineares Herausfallen (Kontrolle unter mu_R) |
| D1b-2 | Knapp oberhalb mu_R bleiben Teilchen 1000 Umlaeufe gefangen | 35 % | eingetroffen (Vorbehalt: ebenso unter mu_R, Auslenkungen bis 0,5) | Auslenkung 0,005: 50-61 % bei mu <= 0,039 (aber Auslenkungen bis 0,5; unter mu_R bei 0,038 ebenso 64 %); Auslenkung 0,02: 11-13 % |
| D1c | e erhoeht die Chaoszahl nahe L4 im Mittel | 85 % | offen | kein klarer Anstieg bei gebundenen Bahnen; e erhoeht das Entkommen; 8 Bahnen je Paar |
| D2a | Rastdauer ~ (abs(Delta) - 2K)^(-1/2) | 99 % | eingetroffen | Steigung -0,50007 / -0,50004 |
| D2b | psi = 0 rastet ein, psi = pi rastet aus | 97 % | eingetroffen | Rastung ab F = 0,1 bei psi = 0; bei psi = pi nie; Zeigerformel an 100 % der Punkte |
| D3-1 | N = 2 mit Takt, N = 3 ohne Takt: nirgends robust > 0,005 | 97 % | eingetroffen | max 0,0024 bzw. 0,0022 an je 2000 Punkten |
| D3-2 | N = 3 mit Takt: mindestens ein robuster Punkt > 0,01 | 70 % | eingetroffen | 38 von 40 robust, bis 0,29 |
| D3-3 | N = 4 ohne Takt: robuste Punkte > 0,01 | 75 % | eingetroffen | 39 von 40 robust, bis 0,17 (1000 Punkte) |

## 3. Was das fuer Finns Hypothese heisst

- **"Zwei bearbeiten ein drittes, eine Zeitlang stabil":** Stimmt im Taktgeber-Bild genau so, wie Finn es sagt: knapp
  jenseits der Grenze haelt der Dritte eine Weile mit und springt dann, und die Haltezeit waechst zur Grenze hin
  (Adler-Gesetz, exakt). Bei Gravitation (zwei Hauptkoerper, ein Trojaner) gibt es ebenfalls endliche Haltezeiten,
  aber sie folgen keinem einfachen Gesetz; ob ein Koerper bleibt, haengt stark von der Startauslenkung ab, und schon
  unterhalb der Routh-Grenze fallen Koerper mit groesserer Auslenkung heraus.
- **"Aeussere Einfluesse im gleichen Takt koennen positiv wirken":** Stimmt unter Bedingungen. Bei Taktgebern: nur
  derselbe Takt und dieselbe Phase; dieselbe Frequenz gegenphasig verschlechtert. Bei Gravitation: Der Umlauftakt
  (Exzentrizitaet) stabilisiert jenseits der Routh-Grenze nur einen schmalen Streifen, zerstoert aber eine breite Zone
  darunter; ein frei gewaehlter Takt stabilisiert jenseits der Grenze in breiten Fenstern, am haeufigsten nahe der
  Eigenfrequenz, waehrend derselbe Takt unterhalb der Grenze (schwach) destabilisiert. "Gleicher Takt hilft" ist also
  keine allgemeine Regel, sondern haengt an Phase und daran, auf welcher Seite der Grenze das System liegt.
- **"Im Dreiersystem koennen aeussere Einfluesse mehr Chaos verursachen":** Stimmt in den Phasenmodellen genau: drei
  mit Takt chaotisch, drei ohne und zwei mit Takt nicht. Der Grund ist geometrisch (Zahl der unabhaengigen
  Phasenunterschiede), deshalb ist auch vier ohne Takt chaotisch. Fuer die Gravitation ist das hier offen.
- Kein "widerlegt": Alles gilt nur fuer die gerechneten Modelle (lineares und kreisfoermiges eingeschraenktes
  Dreikoerperproblem, ein Spielzeugmodell mit pulsierendem Potential, Phasenoszillatoren ohne Rueckwirkung auf A und B).
  Bis zu einer Messbezug-Pruefung bleibt alles Hypothese [H].

## 4. Laufzeiten, sha256, Selbstanzeigen, Grenzen

- Laeufe auf der .69 (kleintest.sh, Spuren cpu3/cpu4; Uhr der .69 in UTC, Laufzeit = systemd-Dienstzeit):

| Lauf | Inhalt | Ende (UTC) | rc | Laufzeit |
|---|---|---|---|---|
| 01 | D1a Gitter A + Bisektion + Kontrollen | 06:48:45 | 0 | 1 min 13 s |
| 02 | D1a Gitter B | 06:51:10 | 0 | 3 min 37 s |
| 03 | D3 N = 4 ohne Takt, P = 2000 | 06:58:45 | 1 | 10 min (abgebrochen, keine Ausgabe) |
| 04 | D3 N = 3 mit Takt | 06:59:58 | 0 | 8 min 48 s |
| 06 | D1d Faktor 1 | 07:01:20 | 0 | 2 min 35 s |
| 05a | Auswertung D1a + Querkontrolle D1d | 07:02:34 | 0 | 1 min 14 s |
| 08 | D1b Hauptlauf | 07:04:34 | 0 | 2 min 0 s |
| 07 | D2 komplett | 07:09:59 | 1 | 10 min (abgebrochen, keine Ausgabe) |
| 03 | D3 N = 2 mit Takt | 07:11:37 | 0 | 7 min 3 s |
| 09 | D1b dt/2 | 07:12:57 | 0 | 2 min 59 s |
| 03b | D3 N = 4 ohne Takt, P = 1000, Seed 21 | 07:17:34 | 0 | 5 min 57 s |
| 06b | D1d doppelte Schrittzahl | 07:18:00 | 0 | 5 min 3 s |
| 07b | D2a + D2b | 07:23:17 | 0 | 5 min 43 s |
| 08b | D1b Kontrolle unter mu_R | 07:25:13 | 0 | 1 min 56 s |
| 04 | D3 N = 3 ohne Takt | 07:27:01 | 0 | 9 min 0 s |
| 05 | D3 Nachrechnen B, C | 07:28:23 | 0 | 3 min 10 s |
| 06c | Auswertung D1d | 07:28:24 | 0 | 0,4 s |
| 07c | D2c | 07:31:36 | 0 | 4 min 36 s |
| 10 | D1c | 07:32:30 | 0 | 3 min 51 s |
| 11 | Auswertung D1b + Abbildungen | 07:32:38 | 0 | 8 s |
| 05 | D3 Nachrechnen A (dt/2) | 07:34:07 | 0 | 2 min 31 s |

- Logs: hilfs/logs/*.log. sha256 vollstaendig in hilfs/sha256-code.txt, hilfs/sha256-aus.txt (33 Ergebnisdateien),
  hilfs/sha256-abb-plan.txt (Abbildungen und eingefrorene Plaene). Code lokal und auf der .69 gleich (Vergleich der
  sha256 um 09:35:33). Wichtigste:
  - a4cea3be1e7a6fcd6dd3835c3417e0ead41bb54678ec1a86d98beb6ce82225a0 code/d1a_floquet.py
  - 6e4fe00381a5618fedf5f09b654af339bc37603cf40e3dbc0134000864e1bfcf code/d1b_lebensdauer.py
  - f489d4e7b8e8185623fd9ddb9521a89a764d97f4149af9f9bd368c20033183ca code/d1d_takt.py
  - 79025e70042ded29000d7b8b0656be9128d36df1125d889bb36d9695df06c3e8 code/d2_phasen_teile.py
  - e3bba7faefb34732a9ce3ca94e37afd8498d5246213adaa3106a39cab81c81b1 code/d3_kuramoto.py
  - c1c6bc33dd64fefaef20d1a454d101f32072ea80cb2bbaa4dadc2cbab0c9ad1d code/d3_nach.py
  - 757becb2fbda84052a721d7fed28a869444bd01005a6a365e0c39cfa1e18fd3b aus/d1a/d1a_B.json
  - 8a9a998190ecd152410f1e278116e28fe3810026872e86cddaf772d2d316309d aus/d1b/d1b_haupt.json
  - bda8eacf917933eae5dfd15542edba5490626940344ed33d36acc5e0ee1ed956 aus/d1d/d1d_0.0100_0.0200_0.0350_0.0390_0.0400_0.0420_f1.json
  - 576acd7a3eee090a4f8626e894a169f05e7e93bbd0ee99127604b1e038595d5f aus/d2/d2_voll_ab.json
  - 9bef103d36bf21ac2915dac10a1615b1233ac9092a484189e6d63a32f4d67e84 aus/d3/d3_N3_takt1_P2000_s13.json
  - 2a4a471d3efddabc3d905c4ea6193c91983c54e4a6c84345fc026cc35b8b8807 aus/d3/nach_A.json
  - ac38d0d71851713b4fb34909ce2f843642cd65326e83a7673c27a6bde6e7c3e5 aus/d3/nach_BC.json
- Weitere Kontrollen: D1b dt/2 gegen dt fuer 96 Teilchen: Status (gebunden/entkommen) an allen 96 gleich, Median der
  relativen Lebensdauer-Abweichung <= 5e-4, mindestens 89 % der Paare unter 1 %. D1d Faktor 1 gegen 2: 0 von 359046
  Punkten verschieden.

### Selbstanzeigen

1. Laufzeit unterschaetzt: Lauf 3 (D3 N = 4, P = 2000) und Lauf 7 (D2 komplett) liefen in die 600-s-Grenze, ohne
   Ausgabe; 20 min Spurzeit verloren. Folge: NACHTRAG-1 (N = 4 nur 1000 statt 2000 Punkte, nur die 40 groessten Treffer
   nachgerechnet) und NACHTRAG-2 (D2 in zwei Aufrufen).
2. Lokal python ausserhalb von Rauchtests: einmal ein python3-Textersatz zum Aufteilen von main() in d2_phasen_teile.py
   (keine Rechnung), dazu dreimal python3 -m py_compile als Syntaxpruefung. Beides ist nach dem Auftrag nicht erlaubt.
3. Fehler im ersten Nachrechen-Entwurf (d3_kuramoto.py nachrechnen: Varianten dt/2 und 2T mit neuen statt den
   urspruenglichen Anfangswerten). Vor jedem Lauf erkannt und in d3_nach.py behoben; der alte Modus lief nur lokal im
   Rauchtest.
4. D1b-Kontrolle unterhalb mu_R fehlte im Plan; nach Kenntnis des Hauptlaufs als NACHTRAG-3 ergaenzt. Sie aendert die
   Lesart von D1b (Kriterium misst nichtlineares Herausfallen), nicht die Zahlen des Hauptlaufs.
5. D2c-Parameter schlecht gewaehlt: C war schon ohne Takt an B gerastet, die Frage "hilft ein Takt" ist damit kaum
   beantwortbar.
6. D1c nur 8 Bahnen je Paar und Abbruchkriterium vor dem Einfrieren geaendert (statt 0,5-Kugel: r1, r2 < 0,05 oder
   Abstand > 3, Begruendung im PLAN).
7. Literatur: nur die Abstracts von arXiv:1206.6162 (X. Hu, Y. Long, S. Sun) und arXiv:1308.4745 (X. Hu, Y. Ou,
   P. Wang) ueber die arXiv-API gelesen (08:47 bis 08:48 CEST, Antworten in hilfs/arxiv*.xml). 1206.6162 sagt: drei
   Kurven im (beta, e)-Rechteck, zwei -1-Entartungskurven und die rechte Einhuellende, nur dort aendert sich das
   Stabilitaetsmuster; das passt qualitativ zu D1a (zwei Zungenraender, eine rechte Grenze), Zahlen nennt der Abstract
   nicht. Die Danby-Karte und die Einordnung "eingeschraenktes Problem = wesentlicher Teil" sind Gedaechtnis [L?];
   die Zahlen hier sind eigene Rechnung, nicht mit einer Quelle verglichen.
8. ERGEBNIS.md wurde ab 08:52 schrittweise geschrieben, waehrend Laeufe noch liefen; die Vorhersagen standen vorher in
   der Karte und wurden nicht geaendert.

### Grenzen

- D1a und D1d sind linear: Sie sagen nichts ueber nichtlineare Stabilitaet. Die Spalte mu = 0 ist entartet und nicht
  gewertet.
- D1d ist ein Spielzeugmodell: Die ganze U-Hesse-Matrix (einschliesslich Zentrifugalanteil) pulsiert, die
  Coriolis-Terme nicht. Eine Lesart, bei der nur die Gravitation pulsiert, gaebe andere Fenster.
- D1b haengt am Kriterium der Karte (0,5-Kugel) und an der Startgeschwindigkeit null; andere Startbedingungen koennen
  andere Lebensdauern geben.
- D2 ohne Rueckwirkung von C auf A und B; D3 mit endlicher Messzeit (regulaere Bahnen bis ~0,004) und Stichproben von
  1000 bis 2000 Punkten.
- Kein Messbezug (L5): Alles sind Modellrechnungen; Bezug zu Trojanern oder Taktgebern in der Natur waere eine eigene
  Karte.

## 5. Einfach gesagt

Wenn zwei Taktgeber einen dritten mitziehen, haelt der dritte eine Zeitlang mit, auch wenn er eigentlich etwas zu
schnell ist, und zwar umso laenger, je naeher er an der Grenze ist. Ein Stoss von aussen im gleichen Rhythmus hilft
nur, wenn er auch im gleichen Moment kommt; kommt er genau versetzt, stoert er. Bei Planeten und Trojanern kann
derselbe Rhythmus je nach Massen sowohl stabilisieren als auch zerstoeren. Und Chaos entsteht bei Taktgebern erst,
wenn mindestens vier Rhythmen zusammenspielen: drei Teile plus ein aeusserer Takt reichen dafuer, zwei Teile plus Takt
nicht.

---
Letzte Aenderung: 2026-10-02 09:38:08 CEST (date). Zeitbox eingehalten (Start 08:33:37).
