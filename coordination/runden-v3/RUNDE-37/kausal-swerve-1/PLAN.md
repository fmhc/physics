# KAUSAL-SWERVE-1: Plan (Code-Agent fuer die Leitung, Runde 37, explorativ nach v3)

- Start des Code-Agenten 04:35:13 CEST (date). Plan geschrieben ab 04:52:02 CEST (date), vor jedem Rauchlauf.
- Karte: KARTE.md. Die Vorhersagen KS0 bis KS3 und ihre Schwellen sind unveraendert uebernommen (Abschnitt 6).
- Code:
  - code/swerve.py: Laeufer, Linkzahl (KS0), Laeufer in einer unbegrenzten Streuung (Kontrolle)
  - code/auswertung.py: Urteile, Gegenproben, Bilder
- Kennzeichen:
  - [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese
  - [F] Festlegung dieses Plans (von der Karte offengelassen)
  - [S] Schreibtisch des Code-Agenten (vor jeder Rechnung)
  - [E] im Rauch gesehen

## 1. Hinweise zur Karte (vor jeder Rechnung)

### 1.1 Kartenfehler in KS0

- KS0 sagt: Zukunftslinks je Punkt **fern vom Rand** = ln N - 1,42 +- 0,15 bei N = 64 000.
- ln N - 1,42 ist aber das Mittel **ueber alle Punkte** des Diamanten (L/N aus KAUSAL-1). Punkte nahe dem oberen Rand
  haben wenige Zukunftslinks und ziehen das Mittel herunter.
- **[M] Zukunftslinks eines Punktes bei (u, v):** Erwartung = Integral von 0 bis c ueber (1 - (1 - t)^(N-1))/t dt mit
  c = (1 - u)(1 - v).
  - Fuer c N >> 1 ist das H_(N-1) + ln c = ln N + gamma_E + ln((1 - u)(1 - v)).
  - Das Mittel ueber den ganzen Diamanten gibt E[ln(1 - u)] = -1, also ln N + gamma_E - 2 = ln N - 1,42 (KAUSAL-1).
- **Fern vom Rand ist der Wert groesser.**
  - Zentrum u, v in [0,4; 0,6] (Zentrum wie KAUSAL-1): ln N + gamma_E - 1,400 = 10,244 bei N = 64 000.
  - Die Karte sagt 9,647. Abweichung +0,60, also das Vierfache der Toleranz.
  - Am Startpunkt der Laeufer (0,05; 0,05) waeren es ln N + 0,47.
- **Berichtigung [F]:** KS0 wird ueber **alle Punkte** des Diamanten geurteilt (L/N, wie KAUSAL-1). Sollwert ln N - 1,42 =
  9,647 und Toleranz 0,15 bleiben.
- **Urteil nach Kartenwortlaut** (Zentrumspunkte u, v in [0,4; 0,6]) wird daneben genannt.
  - Erwartung [S]: Wortlaut "nicht eingetroffen" (Mittel ~10,24), berichtigt "eingetroffen".
- Zusaetzlich beschreibend: Linkzahl an den besuchten Punkten der Laeufer gegen die Ortsformel H_(N-1) + ln c (nur c N >
  100).

### 1.2 tau_max wirkt kaum (kein Kartenfehler, Hinweis zur Begruendung)

- [M] Fuer jeden Link eines Punktes fern vom Rand ist X = N tau^2 exponentialverteilt mit Mittel 1, unabhaengig von seiner
  Rapiditaet. Die Linkdichte ist N e^(-N A) dA d eta mit A = du dv = tau^2 (KAUSAL-1).
- Damit faellt mit tau_max = 3/sqrt(N) nur der Anteil e^(-9) = 1,2e-4 der Links weg.
- Fast lichtartige Links sind lang in u oder v, aber nicht in der Eigenzeit. Der Schnitt entfernt sie nicht.
- Der Laeufer waehlt nach der Rapiditaet. Einen fast lichtartigen Link nimmt er nur, wenn seine eigene Rapiditaet schon gross
  ist.
- **Festlegung [F]:** tau_max = 3/sqrt(N) wie in der Karte. Die Laeufe zaehlen, wie viele Links der Schnitt entfernt.

### 1.3 Rand gegen Irrfahrt (Erwartung, kein Kartenfehler)

- Rechnung in Abschnitt 3: Die Streuung je Schritt ist sigma^2 = 1/4 [M]. Bei n = 50 ist die Breite also sqrt(12,5) =
  3,5 in der Rapiditaet.
- Der Diamant laesst vom Startpunkt aus nur etwa abs(eta) <= 4,4 (N = 64 000) bzw. 3,7 (N = 16 000) randfrei zu
  (Abschnitt 4).
- Ein grosser Teil der Laeufer erreicht n = 50 deshalb nicht im Inneren. Das ist der Randeffekt, den die Karte unter
  "KS2 verfehlt" nennt.

## 2. Laeuferregel

- **Netz** wie KAUSAL-1: N Punkte gleichverteilt in (u, v) in [0,1]^2. Links per laufendem Minimum, Funktion
  zukunftslinks() in swerve.py, Logik wie KAUSAL-1/code/kausal.py.
- **Startpunkt [F]:**
  - Ein eingefuegter Punkt bei (u, v) = (0,05; 0,05) plus N - 1 gleichverteilte Punkte.
  - Fuer eine Poisson-Streuung ist das die Palm-Verteilung: ein typischer Streupunkt an dieser Stelle [M].
  - Ein naechstgelegener Streupunkt waere ungeeignet, weil er die Umgebung leer bedingt.
  - Er liegt nahe der unteren Spitze, nicht auf den Raendern u = 0 oder v = 0.
- **Jeder Laeufer bekommt seine eigene Streuung [F]:**
  - Saat SeedSequence([20261004, 37, 1, N, Block, Index von eta_0, Laeufer]).
  - Damit sind alle Laeufer unabhaengig. Zusammenfliessende Laeufer in einer gemeinsamen Streuung sind ausgeschlossen.
- **Schritt:**
  - Alle Zukunftslinks des aktuellen Punktes berechnen; zulaessig sind die mit tau = sqrt(du dv) <= tau_max.
  - Den zulaessigen Link mit kleinstem abs(eta_link - eta) waehlen, eta_link = (1/2) ln(dv/du).
  - Dann eta := eta_link.
- **Ende des Laufs:** nach 100 Schritten oder wenn kein zulaessiger Link mehr da ist ("bis zum oberen Rand").
- Je Schritt werden notiert: eta, tau, Ort, Zahl aller und der zulaessigen Zukunftslinks und das Kennzeichen bulk-exakt
  (Abschnitt 4).

## 3. Schreibtisch des Code-Agenten [S], vor jeder Rechnung

- **Links eines Punktes in einer unbegrenzten Streuung [M]:**
  - Die Links sind die minimalen Punkte des Zukunftsquadranten, eine Treppe. Nach dv absteigend geordnet gilt
    b_(k+1) = b_k U_k und a_(k+1) = a_k + E_k/(N b_k), mit a = du, b = dv, U gleichverteilt und E exponentiell.
  - Daraus folgt: X_k = N a_k b_k ist exponentiell verteilt, und die Abstaende benachbarter Links in eta sind
    (1/2) Gamma(2, 1)-verteilt (Mittel 1, Varianz 1/2).
  - Die Treppe ist also regelmaessiger als ein Poisson-Prozess, mit 1 Link je Rapiditaetseinheit.
- **Ein Schritt [M]:**
  - Die Zukunft des neuen Punktes ist frisch. Die Vorgeschichte haengt nur von Punkten ausserhalb von J+(neuer Punkt) ab.
  - Die eigene Rapiditaet liegt deshalb an einer typischen Stelle der neuen Treppe, in einer groessengewichteten Luecke
    (Gamma(3, 1/2)).
  - Der Abstand zum naechsten Link ist gleichverteilt in [0, g/2]. Daraus folgt:
    - sigma^2 = E[Delta eta^2] = E[g^2]/12 = **1/4**
    - E[abs(Delta eta)] = 3/8
    - E[cosh Delta eta] = 4 (1/1,5^2 - 1/2,5^2) = **1,1378**
    - E[cosh 2 Delta eta] = 16/9
  - Delta eta ist symmetrisch (Spiegelung u <-> v) und haengt nicht von eta ab (Boost). Die Schritte sind unabhaengig.
- **Folgerungen in der unbegrenzten Streuung [M]:**
  - <eta_n - eta_0> = 0 und Var = n/4 fuer jedes eta_0. Das ist die Aussage von KS1 und KS2 ohne Rand.
  - <cosh eta_n> = cosh(eta_0) 1,1378^n. Das Netz heizt exponentiell: n = 5 gibt 1,91, n = 50 gibt 636 (eta_0 = 0).
  - Der Mittelwert ist aber schwer geschwaenzt: Var(cosh eta_50) ~ (16/9)^50/2 ~ 1e12. Ein Stichprobenmittel aus 1000
    Laeufern liegt bei n = 50 meist weit unter 636 und streut stark.
- **Erwartung im Diamanten [S/H]:**
  - Unter der Randregel (Abschnitt 4) sind die verbleibenden Laeufer auf abs(eta) <~ 4 beschraenkt.
  - Var waechst dann langsamer als n/4 und flacht ab.
  - Fuer eta_0 = +-1 liegt die Schranke einseitig naeher. Die verbleibenden Laeufer werden zur Rapiditaet 0 des
    Diamanten hin ausgelesen (Scheinreibung durch Auslese).
  - Grobe eigene Erwartung (keine Urteilsregel):
    - KS0 berichtigt eingetroffen (95 %)
    - KS1 nicht eingetroffen (65 %, wegen eta_0 = +-1)
    - KS2 nicht eingetroffen (70 %)
    - KS3 eingetroffen (80 %)
  - Gegenproben: eingefrorene Laeufer und Drift je Schritt im Inneren ohne Drift [M]; Schritte nach dem Randkontakt mit
    Drift zur 0 hin [H].

## 4. Randregel und Populationen [F]

- **Bulk-exakter Schritt:**
  - Gegeben sind der Zustand vor dem Schritt (Ort u, v; Rapiditaet eta) und der gewaehlte Abstand d = abs(eta_link - eta).
  - Der Schritt ist bulk-exakt, wenn tau_max e^(eta + d) <= 1 - v und tau_max e^(-eta + d) <= 1 - u.
  - [M] Dann liegt jeder zulaessige Link mit abs(eta' - eta) < d im Diamanten. Der gewaehlte Link ist auch in einer
    unbegrenzten Streuung ein Link (sein Intervall liegt im Diamanten). Der Schritt ist also derselbe wie ohne Rand.
  - Umgekehrt: Ist der Schritt im Diamanten nicht bulk-exakt, so ist er es auch in der unbegrenzten Streuung nicht. Die
    Regel haengt also nur vom Zustand und von abs(Delta eta) ab.
- **Hauptregel:** Ein Laeufer gilt bis zu seinem ersten nicht bulk-exakten Schritt T als "im Inneren".
  - Er zaehlt bei n genau dann, wenn die Schritte 1 bis n alle bulk-exakt waren (n < T).
  - "Kein zulaessiger Link" zaehlt als nicht bulk-exakt.
  - Das ist "nur Laeufer werten, die n Schritte sicher im Inneren bleiben".
- **Gegenproben ohne Urteilskraft:**
  - **Eingefroren:** Alle Laeufer zaehlen; ab T steht eta auf dem letzten Wert im Inneren.
    - [M] Die Abbruchregel ist symmetrisch in Delta eta. Diese Reihe ist deshalb ein Martingal: <eta_n - eta_0> = 0 ohne
      Auslese, fuer jedes n und eta_0 (bis auf O(1/N) durch festes N).
  - **Bis zum Rand:** Alle Laeufer, solange sie Schritte machen (ohne Randregel, Kartenwortlaut "bis zum oberen Rand").
  - **Drift je Schritt:**
    - Alle Schritte im Inneren (k < T), nach eta vor dem Schritt in Klassen der Breite 0,5 von -4 bis 4.
    - Je Klasse: <Delta eta>, SE und <Delta eta^2>.
    - Dazu die Ausgleichsgerade Delta eta = alpha + beta eta (Reibung hiesse beta < 0).
    - Dasselbe fuer die Schritte ab T (nach dem Randkontakt).
  - **Unbegrenzte Streuung** (bulk in swerve.py):
    - Je Schritt eine frische Poisson-Streuung im Ruhesystem des Laeufers, mit X = N tau^2 in [0, 9] (gleicher
      tau-Schnitt) und abs(eta) <= 8.
    - Fehlende Sperrpunkte ausserhalb betreffen nur Links nahe abs(eta) = 8.
    - Rapiditaeten addieren sich. Synthetisch, nur Vergleich ohne Rand.
  - **N = 16 000** mit derselben Regel.
  - **KS1 mit SE ueber die 4 Bloecke** statt ueber Laeufer.

## 5. Laeufe und Statistik [F]

- **N = 64 000 (Urteile) und N = 16 000 (Gegenprobe):**
  - Je 4 Bloecke (Block 1 bis 4)
  - je Block und eta_0 in {-1; 0; 1} B Laeufer
  - B steht nach der Zeitmessung im Rauch fest, vor dem Einfrieren (Abschnitt 8); Ziel war B = 300.
  - **Festgelegt nach dem Rauch: B = 1000**, also 4000 Laeufer je eta_0 und N.
    - Grund: Im Rauch bei N = 4000 waren bei n = 50 nur 0,3 bis 0,7 % der Laeufer noch im Inneren (Abschnitt 8).
    - Fuer die Mindestzahl 100 bei n = 50 braucht es mehr Laeufer.
    - Das ist eine Stichprobengroesse; Schwellen und Regeln bleiben.
- **Codeprobe Spiegelung** (swerve.py spiegel, N = 64 000, 20 Streuungen): u <-> v und eta_0 -> -eta_0 muss eta -> -eta
  geben, mit gleichen Kennzeichen. Nur Codepruefung, kein Urteil.
- **KS0:** N = 64 000, Saaten 1 bis 3 (eigene Streuungen, alle N Punkte gleichverteilt, ohne eingefuegten Punkt).
- **Unbegrenzte Streuung:** 1000 Laeufer je eta_0, Saat 1, je 100 Schritte.
- **Rechnen:**
  - Nur .69 ueber kleintest.sh, Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich, je Lauf < 10 min.
  - Zwischenstaende alle 100 Laeufer in die Ausgabedatei.
- **Standardfehler:**
  - SE = Standardabweichung ueber Laeufer / sqrt(Zahl), mit ddof = 1. Die Laeufer sind unabhaengig (eigene Streuungen).
  - Var mit ddof = 1.
- **Mindestzahl:** Ein Urteil braucht bei jedem benutzten n >= 100 Laeufer im Inneren je eta_0, sonst "nicht
  auswertbar".

## 6. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| KS0 | Kontrolle: Zukunftslinks je Punkt (fern vom Rand) = ln N - 1,42 +- 0,15 bei N = 64 000 | 85 % |
| KS1 | Keine Reibung: abs(<eta_n - eta_0>) <= 3 Standardfehler bei n = 50, fuer eta_0 = -1, 0, 1 | 75 % |
| KS2 | Irrfahrt: Var(eta_n - eta_0) linear in n (R^2 > 0,98 fuer n = 5 bis 50); die Steigung sigma^2 ist fuer eta_0 = -1, 0, 1 gleich innerhalb 15 % | 55 % |
| KS3 | Heizen: Fuer eta_0 = 0 steigt <cosh eta_n> mit n (bei n = 50 groesser als bei n = 5, ueber 3 Standardfehler) | 65 % |

- **KS0:**
  - **Berichtigt (Urteil):** Mittel der Zukunftslinks ueber alle N Punkte, je Saat; Mittel der 3 Saaten.
    "Eingetroffen", wenn abs(Mittel - (ln 64000 - 1,42)) <= 0,15. Alle Links ohne tau-Schnitt, wie KAUSAL-1.
  - **Kartenwortlaut (genannt):** Mittel ueber alle Zentrumspunkte u, v in (0,4; 0,6) der 3 Saaten, gleiche Schwelle.
- **KS1:**
  - Hauptregel, N = 64 000, n = 50, je eta_0: m = <eta_50 - eta_0>, SE wie Abschnitt 5.
  - "Eingetroffen", wenn abs(m) <= 3 SE fuer alle drei eta_0.
- **KS2:**
  - Hauptregel, N = 64 000. Je eta_0 Var_n fuer n = 5, 6, ..., 50 (46 Werte), gewoehnliche Ausgleichsgerade
    Var = a + b n (ungewichtet).
  - R^2 = 1 - Restquadratsumme / Gesamtquadratsumme.
  - "Eingetroffen", wenn R^2 > 0,98 fuer alle drei eta_0, alle b > 0 und max(b)/min(b) <= 1,15.
  - "Gleich innerhalb 15 %" lese ich als max/min <= 1,15 [F].
- **KS3:**
  - Hauptregel, N = 64 000, eta_0 = 0. D = <cosh eta_50> - <cosh eta_5>, SE_D = sqrt(SE_50^2 + SE_5^2). Das ist
    konservativ: die Population bei 50 ist eine Teilmenge der bei 5.
  - "Eingetroffen", wenn D > 3 SE_D.
- **Fuer KS1 bis KS3 gilt:**
  - "Nicht auswertbar", wenn bei einem benutzten n und eta_0 weniger als 100 Laeufer im Inneren sind.
  - Die Urteile rechnet code/auswertung.py mechanisch.
  - Die Gegenproben (Abschnitt 4, N = 16 000, unbegrenzte Streuung) werden mit denselben Regeln ausgewertet und
    berichtet. Sie aendern kein Urteil.
- **N [F]:** Die Karte nennt N = 16 000 und 64 000, legt aber nicht fest, wo KS1 bis KS3 geurteilt werden. Ich urteile bei
  N = 64 000:
  - Dort ist der Rand weiter weg.
  - KS0 steht ebenfalls bei 64 000.
  - N = 16 000 zeigt, wie der Randeffekt mit N schrumpft.

## 7. Bilder (lauf-69/)

- drift_n.png: <eta_n - eta_0> gegen n je eta_0
  - Hauptregel N = 64 000 mit SE-Band
  - Hauptregel N = 16 000
  - eingefroren
  - bis zum Rand
- var_n.png: Var gegen n je eta_0, beide N, mit unbegrenzter Streuung und n/4.
- cosh_n.png: <cosh eta_n> gegen n je eta_0 (log), mit unbegrenzter Streuung und 1,1378^n.
- kontrollen.png: Anteil im Inneren gegen n; Drift je Schritt gegen eta (innen und nach dem Randkontakt).

## 8. Rauch (vor dem Einfrieren; Ergebnisse folgen hier)

- **Zweck:** Laeuft der Code, Zeitbedarf je Laeufer und je Linkzahl-Lauf, tau-Schnitt, Pfadprobe der Auswertung.
- **Laeufe:**
  - laeufer N = 4000 und N = 2000, Block 91, B = 20 (fremde N, nicht in den Urteilen)
  - laeufer N = 64 000, Block 90, B = 2 (nur Zeitmessung; Block 90 geht nicht in die Urteile ein)
  - links N = 4000 und N = 16 000, Saat 90
  - bulk B = 20, Saat 91
  - auswertung.py auf dem Rauchordner mit N_haupt = 4000, N_neben = 2000
- Was ich dabei sehe, steht hier vor dem Einfrieren. Schwellen und Regeln aendern sich danach nicht.

### 8.1 Gesehen im Rauch [E] (02:54:00 bis 02:56:59 UTC, Ordner rauch-69/)

- **Rauch 1** (Laeufe wie oben, alle rc = 0):
  - Laufzeit: laeufer N = 64 000 mit 6 Laeufern 0,2 s. links N = 16 000 2,0 s; fuer N = 64 000 erwarte ich ~30 s
    (N^2).
  - links N = 4000, Saat 90:
    - alle Punkte 6,809 gegen ln N - 1,42 = 6,874 (exakt 6,874)
    - Zentrum 7,71 +- 0,19 gegen die Ortsformel 7,48
  - links N = 16 000, Saat 90:
    - alle 8,225 gegen exakt 8,258
    - Zentrum 8,93 gegen Ortsformel 8,85
  - Wie in KAUSAL-1 liegen die Mittel ueber alle Punkte etwas unter dem exakten Wert (-0,065 bzw. -0,033).
  - bulk (60 Laeufer x 100 Schritte):
    - sigma^2 = 0,2405, E abs(Delta eta) = 0,367, E cosh Delta eta = 1,131 (Schreibtisch 0,25 / 0,375 / 1,138)
    - 1,005 Links je Rapiditaetseinheit
  - In Rauch 1 bei N = 4000 (60 Laeufer) lag die mittlere Aenderung der Schritte im Inneren bei +0,040 +- 0,016. Das
    war mein Anlass fuer die Spiegelprobe und Rauch 2.
  - Die Bilder rendern; die Beschriftung "N = 64 000 / 16 000" ist dort fest und im Rauch falsch (4000 / 2000).
- **Spiegelprobe** (N = 4000, 40 Streuungen): eta + eta_gespiegelt <= 4,4e-16, Kennzeichen und Schrittzahlen alle
  gleich. Der Code behandelt u und v gleich.
- **Rauch 2** (N = 4000 und 2000, Block 92, B = 300; 3,7 s bzw. 2,7 s):
  - **Schritte im Inneren:**
    - N = 4000: <Delta eta> = -0,0010 +- 0,0040, beta = +0,0011 +- 0,0041 (13 455 Schritte)
    - N = 2000: +0,0026 +- 0,0046, beta = -0,0033 +- 0,0052
    - Die +0,040 aus Rauch 1 war also Zufall.
    - sigma^2 je Schritt im Inneren: 0,219 bzw. 0,211, kleiner als 1/4, wie erwartet durch die Abbruchregel.
  - **Schritte nach dem Randkontakt:** beta = -0,139 +- 0,005 (N = 4000) bzw. -0,179 +- 0,006 (N = 2000). Das ist die
    erwartete Rueckstellung zur Rapiditaet 0 des Diamanten [H bestaetigt im Rauch].
  - **Anteil im Inneren** (N = 4000):
    - n = 10: 0,57 bis 0,72; n = 20: 0,23 bis 0,31; n = 30: 0,07 bis 0,12; n = 50: 0,003 bis 0,007
    - Bei N = 2000 ist bei n = 50 keiner mehr im Inneren.
  - **Eingefroren** (N = 4000, n = 50): +0,10 +- 0,10 / -0,16 +- 0,11 / +0,03 +- 0,10 (eta_0 = -1 / 0 / 1).
  - **tau-Schnitt:** 15 von 187 717 Links (8e-5) an besuchten Punkten.
  - Linkzahl an besuchten Punkten gegen die Ortsformel: -0,015 +- 0,017. Mittleres tau sqrt(N) des gewaehlten Links:
    0,746.
  - Nicht angesehen: Mittelwerte und Varianzen der Hauptregel bei kleinen N. Angesehen habe ich nur:
    - kontrollen.png aus Rauch 1
    - aus Rauch 2 Anteil im Inneren, Eingefroren, Schritte, tau-Schnitt und Linkzahl
- **Folge fuer den Plan:** nur B = 1000 statt 300 (Abschnitt 5). Keine Schwelle und keine Regel geaendert.

## 9. Einfrieren und Hauptlaeufe

- Kopie PLAN.md.eingefroren-JJJJMMTT-HHMMSS (Zeit per date), Code-Kopien mit derselben Endung, sha256 in
  code/pruefsummen-einfrieren.txt.
- Danach aendern sich Plan und Urteilsregeln nicht. Code nur bei echten Fehlern, offengelegt im ERGEBNIS.
- **Hauptlaeufe** (Ordner lauf/ auf der .69, danach lauf-69/):
  - laeufer N = 64 000, Bloecke 1 bis 4, B = 1000
  - laeufer N = 16 000, Bloecke 1 bis 4, B = 1000
  - links N = 64 000, Saaten 1 bis 3
  - bulk 1000, Saat 1
  - spiegel N = 64 000, 20
  - dann auswertung.py lauf lauf (ohne N-Argumente)
