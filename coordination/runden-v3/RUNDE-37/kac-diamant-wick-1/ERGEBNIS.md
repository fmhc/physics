# KAC-DIAMANT-WICK-1: Ergebnis

- Code-Agent fuer die Leitung claude-primary. Bindend: KARTE.md, PLAN.md (eingefroren).
- Kennzeichen: [S] an der Quelle gelesen, [M] eigene Mathematik, [P] Projekt, [F] eigene Festlegung, [E] Abschaetzung,
  [H] Hypothese.
- **Art:** Schreibtisch plus synthetische Rechnung an einem Modell. Keine Messdaten. **Alle vier Urteile waren vor der
  Rechnung ableitbar** (PLAN.md 3.5). Die Rechnung bestaetigt die Herleitung; sie ist keine unabhaengige Messung.

## 1. Zeiten und Laeufe (alle per date; .69 in UTC = CEST - 2 h)

- Start 2026-10-05 07:54:25 CEST. Plantext ab 08:04:43 CEST. Text dieser Datei ab 08:13:07 CEST.
- Rauchtests (cpu7, rc = 0): R0 06:08:54 UTC (Umgebung, Niveaus, [100]-Formel); R0b 06:10:19 UTC (nur Codepfad);
  R0c 06:10:19 bis 06:10:21 UTC (Bild, 31 Punkte).
- Eingefroren 08:10:58 CEST: PLAN.md, code/kac_wick.py, code/bild.py (EINGEFROREN-SHA256.txt).
- **H1** Hauptlauf (cpu7): 06:11:05 UTC, rc = 0, 0,67 s; lauf-69/haupt.json.
- **B1** Bild (cpu7): 06:11:13 bis 06:11:15 UTC, rc = 0; lauf-69/baender.png.
- Nachtrag 08:12:02 CEST: code/bild_v2.py (nur Darstellung, Zeile 3 als Punkte), eingefroren vor B2.
- **B2** Bild (cpu7): 06:12:08 bis 06:12:10 UTC, rc = 0; **lauf-69/baender-v2.png** (das zu zeigende Bild).
- Pruefsummen: lauf-69/PRUEFSUMMEN.txt (auf der .69 erzeugt, lokal nachgeprueft).
- Ende der Arbeit 08:15:24 CEST (date, nach der letzten Pruefsummenkontrolle); Zeitbox 75 min nicht ausgeschoepft.

## 2. Ergebnis zuerst

1. **Es gibt genau ein brauchbares Bandpaar: das aeussere (unterstes und oberstes Band).** Es hat E0 = hbar lambda,
   Delta = hbar lambda und bei kleinem k die Dirac-Form. Die Richtungsstreuung bei \|k\| = 0,05 betraegt 1,45e-4
   (gleichverteilt) bzw. 1,63e-4 (ohne Ruecksprung), also weit unter 2,8e-3.
2. **Die Masse ist Nelsons Masse:** m = Delta/c_eff^2 = hbar/(2D), mit D dem Diffusionskoeffizienten der reellen
   Kantenwahl (Ghose Gl. 58).
   - Gleichverteilt: c_eff = Wurzel(2/3) c = 0,8165 c und m = 3 hbar lambda/(2 c^2).
   - Ohne Ruecksprung: c_eff = c und m = hbar lambda/c^2, also genau Ghoses hbar lambda = m c^2.
   - Laengs [111] ist das Paar ohne Ruecksprung exakt Ghoses 1D-Dirac-Paar.
3. **Die Isotropie folgt aus der Symmetrie und gilt nur im langsamen Bereich.**
   - Die kubische Symmetrie O_h macht den k^2-Term isotrop. Der A <-> B-Tausch macht das Spektrum gerade in k; eine
     Kippung gibt es im 8x8 also nicht.
   - Ab c k ~ lambda wird es anisotrop. Bei \|k\| l = 1 liegt die Streuung bei 3 bis 4 % (Standardabweichung) und
     12 bis 15 % (Spannweite).
   - Die Grenzgeschwindigkeit ist c laengs [111], 0,816 c laengs [110] und c/Wurzel3 laengs [100]. Der Lichtkegel der
     Kantenwahl ist tetraedrisch, nicht rund.
4. **Die uebrigen sechs Baender sind anisotrop.**
   - Gleichverteilt sind sie bei k = 0 sechsfach entartet (E = hbar lambda). Sie spalten teils linear (masselose
     Kegel, Steigung richtungsabhaengig), teils quadratisch.
   - Ohne Ruecksprung besteht noch das Paar (2, 7) den Formtest: Delta = hbar lambda/3, c_eff zwischen c/3 und
     c/Wurzel3, Streuung 8,9e-2.
   - Jedes andere Paar als (1, 8) hat eine Streuung von mindestens 2e-2.
5. **Urteile:**
   - KW0 eingetroffen.
   - KW1 eingetroffen nach Plan; nach strenger Lesart (exakte Dirac-Form) nicht eingetroffen.
   - KW2 nicht eingetroffen: Ohne Ruecksprung ist die Streuung um den Faktor 1,12 groesser; am Schreibtisch 9/8.
   - KW3 eingetroffen.

## 3. Urteile KW0 bis KW3

| Nr | Vorhersage (Karte, gekuerzt) | Wahrsch. | nach Plan | nach Kartenwortlaut | vorab ableitbar? |
|---|---|---|---|---|---|
| KW0 | Niveaus auf 1e-12; k^2-Koeffizient des diffusiven Zweigs isotrop (< 1e-9) | 90 % | **eingetroffen** (Niveaus 1,1e-15; Spannweite D 2,0e-15 bzw. 2,6e-15) | eingetroffen | ja [M] |
| KW1 | [H] Wick: Bandpaar der Dirac-Form mit Richtungsstreuung bei \|k\| = 0,05 unter 2,8e-3, fuer mindestens eine Regel | 20 % | **eingetroffen**, beide Regeln, Paar (1, 8): 1,45e-4 bzw. 1,63e-4 | offen: Toleranz nicht im Wortlaut. **Exakt** ("der Form"): **nicht eingetroffen** | ja [M], beide Lesarten |
| KW2 | [H] ohne Ruecksprung kleinere Streuung des besten Paars | 50 % | **nicht eingetroffen**: 1,631e-4 gegen 1,453e-4 (Verhaeltnis 1,123) | nicht eingetroffen | ja [M], fuehrende Ordnung 9/8 |
| KW3 | [H] Delta rationales Vielfaches von hbar lambda; m = Delta/c_eff^2 auf 1e-6 wie Schreibtisch | 15 % | **eingetroffen**: Delta = 1 hbar lambda; m = 1,5 bzw. 1,0, groesste Abweichung 1,1e-8 bzw. 7,3e-8 | eingetroffen, wenn KW1 nach Plan gilt; nach strenger KW1-Lesart entfaellt KW3 | ja [M] |

- **Zur Kartenbedeutung von KW1 ("relativistische Teilchenwelle"):** Die Karte prueft nur \|k\| l <= 0,1, also
  c k <= 0,1 lambda. Das ist der langsame Bereich. Dort ist jedes nicht entartete Band eines kubischen Netzes in
  zweiter Ordnung isotrop.
  - Im relativistischen Bereich (c k ~ lambda) ist das Paar deutlich anisotrop (Tabelle 4.5).
  - Die vorab geschriebene Bedeutung "relativistische Teilchenwelle" traegt das Ergebnis deshalb nicht. Es traegt nur
    "massive, isotrope Welle im langsamen Grenzfall, mit der Masse aus der Wahlrate".
- **Zur Ableitbarkeitsprobe der Karte:** Die Karte nennt die Aufhebung der Kippung "nicht ableitbar". Sie folgt aber aus
  dem A <-> B-Tausch (X T(k) X = T(-k), X M X = M): Das 8x8-Spektrum ist gerade in k (PLAN 3.2). Ich melde das; die
  Karte bleibt unveraendert.

## 4. Tabellen

### 4.1 Niveaus bei k = 0 (numerisch gegen Schreibtisch)

| Regel | reell lambda(M - I) | Wick lambda(I - M) | groesste Abweichung |
|---|---|---|---|
| gleichverteilt J/4 | 0, -2, -1 (6x) | 0, 2, 1 (6x) | 1,1e-15 |
| ohne Ruecksprung (J - I)/3 | 0, -2, -2/3 (3x), -4/3 (3x) | 0, 2, 2/3 (3x), 4/3 (3x) | 6,7e-16 |

### 4.2 Bestes Paar je Regel und Fassung (Paar 1, 8; c = lambda = hbar = 1, \|k\| in 1/l)

| Regel | Fassung | E0 | Delta | c_eff (k -> 0) | m = Delta/c_eff^2 | Formrest bis 0,05 (bis 0,1) | Streuung Std/Mittel, 400 Fib. | Spannweite/Mittel (Kartenliste) | exakte Form, Richtungen von 426 |
|---|---|---|---|---|---|---|---|---|---|
| gleich | Wick | 1 | 1 | 0,81649658 | 1,5000000 | 3,47e-4 (1,38e-3) | **1,453e-4** | 5,51e-4 (5,55e-4) | 0 |
| gleich | reell (Telegraph) | 1 | 1 | 0,81649658 | 1,5000000 | 3,47e-4 (1,39e-3) | 1,457e-4 | 5,52e-4 (5,56e-4) | 0 |
| ohne | Wick | 1 | 1 | 0,99999999 | 1,0000000 | 6,23e-4 (2,47e-3) | **1,631e-4** | 6,19e-4 (6,23e-4) | 8 (alle [111]) |
| ohne | reell (Telegraph) | 1 | 1 | 0,99999999 | 1,0000000 | 6,27e-4 (2,54e-3) | 1,642e-4 | 6,23e-4 (6,27e-4) | 8 |

- Telegraphenform der reellen Fassung: g = -E0 -+ Wurzel(Delta^2 - c_eff^2 k^2). Imaginaerteile im Kartenbereich
  <= 3,4e-16; die reelle Fassung ist dort die Wick-Fassung bei imaginaerem k (H(k) = -G(-i k), geprueft: 0).
- Schreibtisch (PLAN 3.4) gegen Rechnung: c_eff Wurzel(2/3) = 0,8164966 bzw. 1, groesste Abweichung 4,4e-9 bzw. 3,7e-8.
  Streuung Std/Mittel (Kugel) 1,46e-4 bzw. 1,64e-4, Spannweite 5,56e-4 bzw. 6,25e-4, Formrest 3,5e-4 bzw. 6,3e-4.
- Der Rest der Mitte \|m(k) - E0\| ist null (chirale Symmetrie E_j + E_(9-j) = 2 lambda, geprueft bis 3,6e-15).

### 4.3 k^2- und k^4-Koeffizienten

| Groesse | gleich: Schreibtisch / Rechnung | ohne: Schreibtisch / Rechnung |
|---|---|---|
| D, exakte 2. Stoerungsordnung | 1/3 / 0,33333333333333 (Spannweite 2,0e-15) | 1/2 / 0,5 (Spannweite 2,6e-15) |
| D, Richardson aus dem Spektrum (0,0125/0,025), beschreibend | 0,3333333338 (Spannweite 3,3e-8) | 0,4999999765 (Spannweite 9,8e-8) |
| beta (k^4 von h^2) laengs [100] | -1/9 = -0,1111 / -0,1109 | -1/2 / -0,4981 |
| beta laengs [110] (K4 = 1/2) | +1/9 / +0,1109 | -1/8 / -0,1248 |
| beta laengs [111] | 5/27 = 0,1852 / 0,1851 | 0 / 1,4e-9 |

- Die Richardson-Streuung ~1e-7 ist der Abbruch bei k^6, keine Anisotropie des k^2-Terms. Das 1e-9-Kriterium erfuellt
  nur der exakte Koeffizient (Selbstanzeige 5).

### 4.4 Andere Paare (Wick, beschreibend)

| Regel | Paar | E0 | Delta | c_eff (Mittel) | Formtest | Streuung Std/Mittel |
|---|---|---|---|---|---|---|
| gleich | (1, 7), (2, 8) | 0,5 bzw. 1,5 | 0,5 | 5,39 | verfehlt (Formrest 0,53) | 2,08e-2 |
| gleich | (2, 7) | 1 | 0 (masselos) | 0,617 | verfehlt (0,012) | 4,20e-2 |
| ohne | (2, 7) | 1 | 1/3 | 0,536 (1/3 bis 1/Wurzel3) | **bestanden** (4,7e-4) | 8,85e-2 (Spannweite 0,43) |
| ohne | (1, 7), (2, 8) | 2/3 bzw. 4/3 | 2/3 | 0,789 | verfehlt (0,012) | 3,93e-2 |

- Paare mit c_loc^2 > 0 in allen Richtungen: 17 von 28 (gleich), 11 von 28 (ohne). Nur (1, 8) liegt unter 2,8e-3.

### 4.5 Relativistischer Bereich und Einheitenwahl (beschreibend)

| Groesse, aeusseres Paar | gleich | ohne |
|---|---|---|
| c_loc bei \|k\| l = 1, laengs [100] / [110] / [111] | 0,773 / 0,853 / 0,896 | 0,882 / 0,962 / 1,000 |
| Streuung bei \|k\| l = 1, Std / Spannweite | 3,7e-2 / 0,145 | 3,1e-2 / 0,123 |
| Grenzgeschwindigkeit (\|k\| l = 200), [100] / [110] / [111]; Schreibtisch 0,577 / 0,816 / 1 | 0,580 / 0,818 / 1,000 | 0,581 / 0,818 / 1,000 |
| Streuung bei \|k\| a = 0,05 (a = 4l/Wurzel3, \|k\| l = 0,0217) | 2,7e-5 | 3,1e-5 |
| \|k\| l, ab dem die Std-Streuung 2,8e-3 erreicht [E, fuehrende Ordnung] | ~0,22 | ~0,21 |

### 4.6 Kontrollen

| Pruefung | gleich | ohne | Regel |
|---|---|---|---|
| Nebenarm GJKS (imaginaere Rate) gegen Ghose-Lesart, Spektren | 0 | 0 | <= 1e-12 |
| H(k) = -G(-i k) | 0 | 0 | <= 1e-12 |
| chirale Symmetrie E_j + E_(9-j) = 2 | 3,1e-15 | 3,6e-15 | <= 1e-12 |
| geschlossene Formeln [100] und [111] (PLAN 3.3) gegen Numerik, \|k\| bis 3 | 1,8e-15 | 1,3e-15 | <= 1e-12 |

## 5. Bedeutung

### 5.1 Fuer Finns Frage zur Unschaerfe

- **Was die Rechnung zeigt [M]:** Nach Ghoses Wick-Rotation liefert die Kantenwahl auf dem Diamantnetz eine Welle mit
  Masse. Die Masse kommt aus der Wahlrate: m = hbar/(2D), das ist Nelsons Beziehung. Im langsamen Bereich ist die Welle
  in allen Richtungen gleich.
  - Fuer eine solche Welle gilt Delta x Delta k >= 1/2 wie fuer jede Welle; mit p = hbar k ist das Heisenberg.
  - Neu gegenueber UNSCHAERFE-KANTE-L ist nur: Finns Netz stoert den langsamen Grenzfall nicht, und die Masse ist
    durch die Kantenwahl festgelegt (Ruecksprungregel: Faktor 3/2).
- **Was sie nicht zeigt:** Das i, und damit die Amplitude, kommt aus der Wick-Rotation, also von Hand, nicht aus der
  Kantenwahl. Der Befund von UNSCHAERFE-KANTE-L bleibt: Unschaerfe folgt aus der Kantenwahl nur, wenn man die
  Amplitude schon voraussetzt.
- **Relativistisch** ist die Welle nicht isotrop. Der Kegel ist tetraedrisch, und es gibt sechs zusaetzliche,
  anisotrope Baender. Ein Dirac-Teilchen im vollen Sinn liefert Finns Diamantnetz mit dieser Konstruktion nicht.

### 5.2 Fuer Luecke T1 (Quantenmechanik selbst) [H]

- Die Konstruktion uebertraegt eine bekannte Zuordnung auf Finns Netz (GJKS, Nelson, Ghose [S]): langsamer Zweig
  -> Schroedinger-Teilchen mit m = hbar/(2D).
- Sie schliesst T1 nicht, denn die komplexe Struktur wird vorausgesetzt.
- Hypothese, ungeprueft: Ein Richtungssatz mit hoeherer Symmetrie (4-Design statt 2-Design) koennte die
  k^4-Anisotropie verringern. Die Grenzgeschwindigkeit bliebe trotzdem richtungsabhaengig, denn max_i \|e_i . n\| ist
  bei endlich vielen Richtungen nie konstant [M].
- Ohne Ruecksprung ist laengs [111] Ghoses 1D-Fall exakt eingebettet (c_eff = c, Delta = hbar lambda). Das ist der
  einzige Ort, an dem die Karte "Masse aus hbar lambda" woertlich trifft.

## 6. Selbstanzeigen

1. **Vorab ableitbar:** Alle Urteile standen vor der Rechnung im Plan (PLAN 3.5), mit Zahlen. Die Rechnung bestaetigt
   die Schreibtischherleitung auf 1e-15 (Formeln) bzw. auf wenige Prozent der fuehrenden Ordnung (Streuung). Sie ist
   keine Messung einer offenen Groesse.
2. **Schwelle nach der Herleitung gesetzt:** Den Formrest (<= 2,8e-3 bis \|k\| = 0,05) habe ich nach der
   Schreibtischrechnung gewaehlt, mit Begruendung im Plan.
   - Das KW1-Haupturteil haengt an dieser Wahl. Bis \|k\| = 0,1 bestuende ohne Ruecksprung knapp (2,47e-3).
   - Nach strenger Lesart (exakte Form) faellt KW1. Der Kartenwortlaut laesst die Toleranz offen.
3. **Einheit [F]:** l = c/lambda = Bindungslaenge, wie die Schrittlaenge in QCA-TETRA-1.
   - Meint die Karte die kubische Gitterkonstante a, sind die Streuungen etwa 3/16 so gross.
   - Die Streuung waechst mit (c k/lambda)^2. Ueber 2,8e-3 kaeme sie erst ab \|k\| l ~ 0,2 [E].
4. **Bild nach dem Hauptlauf neu gezeichnet:**
   - bild_v2.py aendert nur die Darstellung: Zeile 3 zeigt Punkte statt Linien, weil Eigenwerte mit gleichem Realteil
     beim Sortieren die Reihenfolge tauschen.
   - Vor B2 als Nachtrag eingefroren. Beide Bilder liegen in lauf-69/.
5. **KW0-Kriterium:**
   - 1e-9 erreicht nur der exakte Stoerungskoeffizient.
   - Aus dem Spektrum bei den Kartenwerten (Richardson) kommt nur ~1e-7, wegen des Abbruchs bei k^6.
   - Ein Leser, der "aus dem Spektrum" verlangt, muesste kleinere k nehmen; dort begrenzt die Rundung (~1e-9) [E].
6. **Karte, Ableitbarkeitsprobe:** Die Aufhebung der Kippung war ableitbar (A <-> B-Symmetrie). Gemeldet, nicht
   geaendert.
7. **Quellen:**
   - Ghose nur aus der Projektkopie gelesen (Gl. 60 bis 82 mit Text), kein Web-Abruf.
   - Die GJKS-3+1-Konstruktion (Ref. 26 bei Ghose) habe ich nicht gelesen.
   - Ob Foster/Jacobson den Diamantfall enthalten, habe ich nicht an der Quelle geprueft. DUNKEL-FLIP-L nennt nur fcc
     bzw. bcc [P].
8. **Gleiche Zahl, Zusammenhang offen:** c_eff = Wurzel(2/3) c (gleichverteilt) ist dieselbe Zahl wie die
   Zickzack-Geschwindigkeit und die W-D-Kegelgeschwindigkeit 0,8165 in DIAMANT-FERMION-L [P]. Hier folgt sie aus
   D = c^2/(3 lambda) und Delta = lambda; ob mehr dahintersteckt, habe ich nicht geprueft.
9. **Arbeitsweise:**
   - Lokal kein python, awk oder perl; jq nur zum Lesen.
   - Geschrieben nur im Kartenordner und in /home/fmh/fmhc-physics-remote/kac-diamant-wick-1/.
   - Kein Journal, kein Peerbus, kein Commit. Die Rauchtest-Ausgaben liegen in rauch-69/.

## 7. Einfach gesagt

Ein Teilchen huepft auf Finns Diamantnetz von Knoten zu Knoten und waehlt jedes Mal eine der vier Kanten. Macht man
daraus mit Ghoses Trick (Zeit und Tempo imaginaer) eine Quantenwelle, entsteht ein Teilchen mit Masse. Diese Masse ist
durch die Wahlrate festgelegt, und bei langsamer Bewegung verhaelt es sich in alle Richtungen gleich. Das war schon
vorher aus der Symmetrie des Netzes klar, die Rechnung hat es bestaetigt. Bei schneller Bewegung aber hat das Teilchen
je nach Richtung ein anderes Grenztempo, und das "i" der Quantenwelle steckt man von Hand hinein: Heisenbergs
Unschaerfe wird dadurch nicht erklaert, nur auf Finns Netz uebertragen.
