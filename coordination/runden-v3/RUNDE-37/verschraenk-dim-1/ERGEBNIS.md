# VERSCHRAENK-DIM-1: Ergebnis (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:48:53 CEST (date); Ergebnis geschrieben ab
  19:16:11 CEST (date).
- Plan und Code eingefroren um 19:03:59 CEST (EINGEFROREN-SHA256.txt), vor jeder Rechnung zu S_D oder D*. Danach blieben
  Plan und Code unveraendert; der Hash von code/vd.py ist auf beiden Seiten gleich (lauf-69/PRUEFSUMMEN.txt).
- Kennzeichen: [E] gerechnet (.69), [M] von Hand (nicht gegengelesen), [L] Gedaechtnis ohne Abruf, [D] beschreibend,
  [H] Hypothese.

## 1. Ergebnis zuerst

1. **Je Randplatz gibt es kein Maximum [E].** S_D(m) faellt streng mit D, fuer alle drei Massen bis D = 200. Fuer
   grosses D gilt S_D ~ (1 + ln(16 w^2))/(16 w^2) mit w = m^2 + 2D, also etwa ln(D)/D^2: bei D = 24 auf 6 % genau,
   bei D = 100 auf 1,3 % genau.
2. **Gleichfoermigkeit [E]:** Fuer grosses D zaehlt nur noch die mittlere Querstoerung. S_D naehert sich dem Wert einer
   einzelnen Kette mit m_eff^2 = m^2 + 2(D - 1). Der Faktor dazwischen ist 1,19 bei D = 8, 1,057 bei D = 24 und 1,013
   bei D = 100. Ab D = 4 liegen m = 0,01 und 0,1 auf 0,5 % beieinander. m = 1 liegt bei D = 4 um 30 % und bei D = 24
   um 4 % tiefer.
3. **Bei fester Punktzahl N gibt es ein Maximum, aber nicht bei 3 [E].**
   - m = 0,1: D* = 3 (N = 10^3), 7 (10^6), 11 (10^9), 14 (10^12) und 98 (10^80).
   - Fuer N = 10^6 ist das nicht 3 oder 4, VD1 ist also nicht eingetroffen.
   - Die Maxima sind flach. Das 90-%-Band reicht fuer N = 10^6 von D = 5 bis 9, fuer 10^80 von 72 bis 140.
4. **Einfaches Gesetz, aber ableitbar [E, M]:** D* ~ 0,53 ln N - 0,5. Das ist VD2, eingetroffen nach beiden Lesarten,
   aber knapp und von der Lesart abhaengig (Abschn. 2).
   - Gleichwertig gesagt: Am Maximum hat der Wuerfel fuer jedes N nur etwa 5,6 bis 10 Plaetze je Kante.
   - Das folgt schon aus S_D ~ ln(D)/D^2 und stand vorab im Plan (Abschn. 2 dort). Es ist keine Entdeckung.
5. **Kontrollen bestanden [E]:**
   - Zerlegung gegen die direkte 2D- und 3D-Rechnung: bis 6e-11 genau.
   - Steigung fuer D = 1: -0,1662 (Ausgleich) bzw. -0,1661 (Sekante) gegen -1/6.
   - Die Halbketten-Formel aus der Eckentransfermatrix stimmt fuer M < 10,8 auf 10^-9 mit der Peschel-Rechnung.

## 2. Urteile

| Nr | Karte (Wahrsch.) | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| VD0 | Zerlegung < 1 %; Steigung -1/6 auf 5 %; S_D monoton (85 %) | **eingetroffen**: (a) max. 5,9e-11; (b) Ausgleich ueber 121 Stuetzstellen -0,16621 (0,27 % Abweichung); (c) streng fallend D = 1..24 | **eingetroffen**: (a) wie Plan; (b) Sekante 0,01 bis 0,1: -0,16610 (0,34 %); (c) wie Plan |
| VD1 | N = 10^6, m = 0,1: D* = 3 oder 4 (15 %) | **nicht eingetroffen**: D* = 7 (stetig 6,86; Bootstrap 400/400) | **nicht eingetroffen**: D* = 7 |
| VD2 | D*(N) linear in ln N, auf 10 % (50 %) | **eingetroffen, knapp**: m = 0,1, stetiges D*, affin: D* = -0,529 + 0,5367 ln N; groesste Abweichung 9,5 % (bei N = 10^3) | **eingetroffen**: ganzzahliges D*, je Masse affin; groesste Abweichung 7,0 % (m = 0,01), 7,0 % (0,1), 4,3 % (1) |

**Wie belastbar VD2 ist [D, M von Hand]:**
- Bei N = 10^12 stehen D = 14 und 15 fast gleich: S_tot(15)/S_tot(14) = 0,99996 bei m = 0,1 und 0,99991 bei m = 0,01.
  Im Bootstrap gewinnt D = 14 nur in 295 bzw. 375 von 400 Ziehungen.
- Mit D*(10^12) = 15 stiege die groesste Abweichung des ganzzahligen Fits fuer m = 0,01 und 0,1 auf 15,2 % (von Hand).
  Das Kartenwortlaut-Urteil waere dann "uneindeutig".
- Mit dem stetigen D* fuer m = 0,01 (nicht Teil der Urteile) liegt die groesste Abweichung bei 22 %. Grund: Bei
  N = 10^3 liegt das Maximum dort fast genau zwischen D = 2 und 3 (stetig 2,51).
- Die Abweichungen kommen fast nur vom kleinsten N. Die Steigung bestimmt vor allem der Punkt N = 10^80.
- Die Urteile bleiben wie gerechnet. Sie haengen aber an einem Gleichstand im Monte-Carlo-Rauschen und an der Lesart.

**Bedeutung (nach der vorab festgelegten Karte):**
- VD1 verfehlt: Das Maximum liegt hoeher. Verschraenkung allein waehlt keine 3 aus. D* = 3 ergibt sich nur bei etwa
  1000 Punkten (Kante L = 10) und m <= 0,1.
- VD2 eingetroffen: Es gibt eine einfache Formel fuer die "beste" Dimension. Sie ist aber aus dem Verduennungsgesetz
  S_D ~ ln(D)/D^2 ableitbar und war vorab so erwartet.

## 3. Tabelle S_D(m), D = 1 bis 24 [E]

Je Randplatz, in nats. D = 1 per Korrelationsmatrix (Peschel), D = 2, 3 mit Gauss-Legendre (gestuft), D >= 4 mit
Monte Carlo (2^22 Stichproben in 32 Bloecken). In Klammern der Fehler (D = 1: Laengenprobe; D = 2, 3: |fein - grob|;
D >= 4: Standardfehler der Blockmittel). Fuer D >= 2 kommt der Splinefehler von S_1 hinzu (bis 8e-9 relativ).

| D | m = 0,01 | m = 0,1 | m = 1 |
|---|---|---|---|
| 1 | 0,767549 (3e-12) | 0,385080 (1e-13) | 0,0559004 (5e-15) |
| 2 | 0,0766221 (3e-13) | 0,0695007 (3e-13) | 0,0254186 (2e-14) |
| 3 | 0,0242550 (1e-14) | 0,0238673 (5e-15) | 0,0136605 (2e-16) |
| 4 | 1,19383e-2 (8,8e-6) | 1,18738e-2 (8,6e-6) | 8,3473e-3 (3,8e-6) |
| 5 | 7,2224e-3 (3,9e-6) | 7,2006e-3 (3,8e-6) | 5,6069e-3 (2,2e-6) |
| 6 | 4,8976e-3 (2,4e-6) | 4,8871e-3 (2,4e-6) | 4,0293e-3 (1,5e-6) |
| 7 | 3,5655e-3 (1,5e-6) | 3,5595e-3 (1,5e-6) | 3,0413e-3 (1,0e-6) |
| 8 | 2,7262e-3 (9,0e-7) | 2,7224e-3 (9,0e-7) | 2,3831e-3 (6,9e-7) |
| 9 | 2,1589e-3 (6,4e-7) | 2,1563e-3 (6,4e-7) | 1,9210e-3 (5,2e-7) |
| 10 | 1,7562e-3 (5,0e-7) | 1,7543e-3 (5,0e-7) | 1,5839e-3 (4,2e-7) |
| 11 | 1,4594e-3 (3,9e-7) | 1,4580e-3 (3,9e-7) | 1,3303e-3 (3,3e-7) |
| 12 | 1,2335e-3 (3,1e-7) | 1,2325e-3 (3,1e-7) | 1,1341e-3 (2,7e-7) |
| 13 | 1,0577e-3 (2,5e-7) | 1,0568e-3 (2,5e-7) | 9,7937e-4 (2,2e-7) |
| 14 | 9,1771e-4 (2,0e-7) | 9,1705e-4 (2,0e-7) | 8,5488e-4 (1,8e-7) |
| 15 | 8,0449e-4 (1,7e-7) | 8,0396e-4 (1,7e-7) | 7,5324e-4 (1,5e-7) |
| 16 | 7,1141e-4 (1,4e-7) | 7,1097e-4 (1,4e-7) | 6,6904e-4 (1,2e-7) |
| 17 | 6,3398e-4 (1,2e-7) | 6,3362e-4 (1,2e-7) | 5,9852e-4 (1,1e-7) |
| 18 | 5,6879e-4 (1,0e-7) | 5,6848e-4 (1,0e-7) | 5,3881e-4 (9,4e-8) |
| 19 | 5,1343e-4 (9,4e-8) | 5,1316e-4 (9,4e-8) | 4,8783e-4 (8,6e-8) |
| 20 | 4,6597e-4 (7,9e-8) | 4,6574e-4 (7,9e-8) | 4,4392e-4 (7,3e-8) |
| 21 | 4,2494e-4 (6,4e-8) | 4,2474e-4 (6,4e-8) | 4,0581e-4 (5,9e-8) |
| 22 | 3,8924e-4 (5,9e-8) | 3,8907e-4 (5,9e-8) | 3,7254e-4 (5,5e-8) |
| 23 | 3,5794e-4 (5,1e-8) | 3,5779e-4 (5,1e-8) | 3,4326e-4 (4,7e-8) |
| 24 | 3,3037e-4 (4,3e-8) | 3,3024e-4 (4,3e-8) | 3,1739e-4 (4,0e-8) |

- Weiter bis D = 200 in lauf-69/auswertung.json. Beispiele (m = 0,1): S_50 = 8,333e-5, S_100 = 2,2752e-5,
  S_200 = 6,1955e-6.
- Verhaeltnis zur Grossmassen-Naeherung (m = 0,1) [E]: 4,82 (D = 1), 2,73 (2), 1,87 (3), 1,54 (4), 1,20 (8), 1,089 (16),
  1,058 (24), 1,027 (50), 1,013 (100) und 1,007 (200).

## 4. D*(N, m) [E]

- D* ist das ganzzahlige Maximum von S_tot(D) = N^((D-1)/D) S_D(m) ueber D = 1..200. Am Rand lag keines.
- "stetig" ist der Scheitel der Parabel durch D* - 1, D*, D* + 1.
- r(-1) und r(+1) sind S_tot(D* -+ 1)/S_tot(D*).
- Band: alle D mit S_tot >= 0,9 S_tot(D*).
- L ist die Kantenlaenge N^(1/D*).
- Boot: Anteil von 400 Bootstrap-Ziehungen mit demselben D*.

| m | N | D* | stetig | r(-1) | r(+1) | 90-%-Band | L | Boot |
|---|---|---|---|---|---|---|---|---|
| 0,01 | 10^3 | 3 | 2,51 | 0,9990 | 0,8753 | 2-3 | 10,0 | 400 |
| 0,01 | 10^6 | 7 | 6,85 | 0,9886 | 0,9786 | 5-9 | 7,20 | 400 |
| 0,01 | 10^9 | 11 | 10,73 | 0,9967 | 0,9889 | 8-15 | 6,58 | 400 |
| 0,01 | 10^12 | 14 | 14,49 | 0,9902 | 0,99991 | 11-20 | 7,20 | 375 |
| 0,01 | 10^80 | 98 | 98,29 | 0,99985 | 0,99996 | 72-140 | 6,55 | 400 |
| 0,1 | 10^3 | 3 | 2,90 | 0,9208 | 0,8847 | 2-3 | 10,0 | 400 |
| 0,1 | 10^6 | 7 | 6,86 | 0,9881 | 0,9788 | 5-9 | 7,20 | 400 |
| 0,1 | 10^9 | 11 | 10,74 | 0,9966 | 0,9890 | 8-15 | 6,58 | 400 |
| 0,1 | 10^12 | 14 | 14,50 | 0,9901 | 0,99996 | 11-20 | 7,20 | 295 |
| 0,1 | 10^80 | 98 | 98,30 | 0,99985 | 0,99996 | 72-140 | 6,55 | 400 |
| 1 | 10^3 | 4 | 4,11 | 0,9203 | 0,9488 | 3-5 | 5,62 | 400 |
| 1 | 10^6 | 8 | 7,61 | 0,9972 | 0,9766 | 6-10 | 5,62 | 400 |
| 1 | 10^9 | 11 | 11,35 | 0,9862 | 0,9975 | 9-16 | 6,58 | 400 |
| 1 | 10^12 | 15 | 15,09 | 0,9950 | 0,9966 | 11-21 | 6,31 | 400 |
| 1 | 10^80 | 99 | 98,80 | 0,99994 | 0,99986 | 72-140 | 6,43 | 400 |

**Affine Fits D* = a + b ln N [E]:**

| m | ganzzahlig | groesste Abw. | stetig | groesste Abw. | nur b ln N (ganzzahlig) |
|---|---|---|---|---|---|
| 0,01 | -0,483 + 0,5346 ln N | 7,0 % | -0,653 + 0,5375 ln N | 22 % | b = 0,531 |
| 0,1 | -0,483 + 0,5346 ln N | 7,0 % | -0,529 + 0,5367 ln N | 9,5 % | b = 0,531 |
| 1 | 0,249 + 0,5360 ln N | 4,3 % | 0,308 + 0,5347 ln N | 2,7 % | b = 0,538 |

- Die Karte schaetzt D* ~ (ln N)/2. Die gerechnete Steigung ist 0,535, rund 7 % mehr.
  - Bei N = 10^80 liegt D* 6 % ueber (ln N)/2 = 92,1.
  - Bei N = 10^3 liegt es darunter (3 gegen 3,45).
- Das passt zu meiner Korrektur F2 im Plan, (ln N)/2 / (1 - 1/ln(64 D*^2)): fuer N = 10^80 ergibt sie rund 99,6,
  gerechnet sind 98,3.

## 5. Bild

BILD-verschraenk-dim-1.png (gleich lauf-69/verschraenk-dim-1.png). Drei Felder:
- links: S_D(m) fuer D = 1..24, logarithmisch, mit der Grossmassen-Naeherung;
- Mitte: S_tot(D)/S_tot(D*) fuer die fuenf N bei m = 0,1;
- rechts: D* gegen ln N mit dem stetigen Fit (m = 0,1) und der Kartenschaetzung (ln N)/2.

## Kontrollen und Vorbehalte (zu Abschn. 1 bis 4)

**Kontrollen [E]:**

| Kontrolle | Erwartung (Plan) | Ergebnis |
|---|---|---|
| Zerlegung gegen direkte Rechnung, 2D (48 x 32) und 3D (24 x 10 x 10), drei Massen | < 1 % | max. 5,9e-11, bestanden |
| Laengenprobe S_1 (1,5 ell) | < 1e-8 | max. 2,9e-8 bei M = 31,6, sonst <= 6,2e-9; verfehlt an 1 von 22 Gitterpunkten (Rundung, absolut 3e-14 bei S ~ 1e-6); die drei Kartenmassen <= 4e-12 |
| Splineprobe (42 Mittelpunkte) | < 1e-6 | max. 7,7e-9, bestanden |
| CTM-Formel gegen Peschel | < 1e-8 | M < 10,8: < 1e-9. An 18 von 421 Stuetzstellen (M >= 18) bis 4,4e-8 (absolut <= 7,5e-12), also verfehlt. Dort ist S ~ 1e-6; die Rundung der Peschel-Rechnung liegt in derselben Groesse wie die Aenderung in der Laengenprobe. |
| Monte Carlo gegen Gauss-Legendre, D = 2, 3 | z <= 3 | z zwischen -1,17 und -0,06, bestanden (alle sechs negativ; sie teilen dieselben Zufallszahlen und sind nicht unabhaengig) |
| quad gegen Gauss-Legendre, D = 2 | < 1e-6 | max. 1,7e-11, bestanden |

- Die Werte ab M >= 18 spielen erst ab etwa D = 130 eine Rolle. An den gefundenen Maxima (D <= 99) liegen die
  S_1-Fehler unter 1e-8 relativ, weit unter dem Monte-Carlo-Fehler (~1e-4).
- **CTM-Formel [M, durch Rechnung gestuetzt]:** S_1(M) = Summe_j s((2j + 1) eps) mit s(x) = x/(e^x - 1) - ln(1 - e^-x)
  und eps = pi K(k')/K(k), k = ((sqrt(M^2 + 4) - M)/2)^2. Sie gilt bis zur Rechengenauigkeit. Den Modul hatte ich vorab
  vermutet; die Struktur kenne ich nur aus dem Gedaechtnis [L]. Folge: S_1(M) ~ (1/6) ln(1/M) mit Konstante fast 0
  [M, von Hand]: S_1(0,01) - (1/6) ln 100 = 2,0e-5; S_1(0,1) - (1/6) ln 10 = 1,3e-3.
- **Direkte Rechnung je Randplatz gegen das unendliche Gitter [D, Verhaeltnisse von Hand]:**
  - m = 1: 3e-10 (2D) und 2e-5 (3D).
  - m = 0,1: 0,23 % (2D) und 3,8 % (3D).
  - m = 0,01: 0,48 % (2D) und 5,5 % (3D).
  - Die Abweichungen bei kleiner Masse kommen von den kleinen Gittern (Lq = 32 in 2D, 10 in 3D, gegen die Korrelationslaenge
    1/m). Bei m = 1 bestaetigt die direkte 3D-Rechnung die ganze Kette (S_1-Gitter, Spline, Integration) auf 2e-5.

**Vorbehalte [M]:**
- **F3 aus dem Plan wird wichtig.** Am Maximum ist die Kante nur L = 5,6 bis 10. In einem offenen Wuerfel mit so
  wenigen Plaetzen je Kante liegen bei grossem D fast alle Randplaetze an Kanten und Ecken. S_tot nach Karte ist
  "Dichte im unendlichen Gitter mal Flaeche", also die Torus-Lesart. Das Maximum ist eine Eigenschaft dieser
  Definition, keine gerechnete Aussage ueber endliche offene Wuerfel.
- **Die Kopplungsnormierung aendert das Bild nicht.**
  - Eine Kopplung J je Glied wirkt wie die Masse m/sqrt(J), denn K = J (m^2/J + Laplace) und ein fester Faktor in K
    aendert X P nicht.
  - Bei jeder festen Kopplung gilt also dasselbe Abklingen ~ ln(D)/D^2. Eine mit D fallende Kopplung macht es nur
    steiler.
  - Der Grund: Jeder Platz teilt seine Steifigkeit auf 2D Nachbarn auf.
- **Ableitbarkeit:**
  - VD0 (b) und (c) standen vorab fest; (c) gilt nach Plan Abschn. 1 sogar Stichprobe fuer Stichprobe.
  - Das Gesetz von VD2 war aus der Grossmassen-Naeherung ableitbar; der Ausgang war vorab erwartet (Plan Abschn. 2).
  - Neu aus der Rechnung sind nur die genauen Zahlen: S_D-Tabelle, ganzzahlige D*, Schaerfe, Massenabhaengigkeit und
    die Kante am Maximum, L* ~ 5,6 bis 10.

## 6. Selbstanzeigen

1. **Python-Start ausserhalb des Starters:** Auf der .69 habe ich einmal
   `python -c "import numpy, scipy, matplotlib; print(...)"` direkt aufgerufen (16:55:34 UTC, Versionspruefung), nicht
   ueber kleintest.sh. Keine Rechnung, aber ein Interpreterstart neben dem Starter.
2. **Nebenrechnungen per jq auf der .69, ausserhalb von kleintest.sh:** relative Abweichung CTM gegen Peschel je
   Stuetzstelle, Zaehlung der Stellen ueber 1e-9 und 1e-8, kleinstes betroffenes M. Das ist eine kleine Rechnung, keine
   Simulation.
3. **Denkfehler im eingefrorenen Plan:**
   - Plan Abschn. 2 sagt, die Grossmassen-Naeherung gebe "eher zu kleines D*". Die Richtung ist falsch.
   - Die Naeherung unterschaetzt S_D bei kleinem D. Das wahre S_D faellt also steiler, und das schiebt D* nach unten.
   - Meine Handwerte lagen fuer m = 0,1 um 1 bis 2 zu hoch: 4 statt 3, 8 statt 7, 12 statt 11, 15 bis 16 statt 14,
     100 statt 98. Fuer N = 10^3 lag der wahre Wert ausserhalb meiner Spanne "4 (bis 5)".
4. **Vorab-Erwartungen verfehlt (Kontrollen und Vorbehalte):** Laengenprobe an 1 Punkt, CTM-Gegenprobe an 18
   Punkten. Beides liegt an
   der Rundung bei S ~ 1e-6 und ist nicht Teil der Urteile.
5. **Handrechnungen ohne eingefrorenen Code [M]:**
   - die Verhaeltnisse direkte Rechnung gegen unendliches Gitter (Kontrollen und Vorbehalte);
   - die Empfindlichkeit von VD2 bei D*(10^12) = 15 (15,2 %, Abschn. 2);
   - die Nachpruefung der Urteile von VD1 (ln S_tot = 6,1918; 6,2036; 6,1823 bei D = 6, 7, 8) und VD2 (Fit fuer
     m = 0,1 nachgerechnet).
   Alles im Kopf, nicht auf dem Laptop gerechnet.
6. **Dateien ausserhalb der Arbeitsordner, vom Werkzeug angelegt:** Die Hintergrund-Aufrufe (Laufwarten) haben ihre
   Ausgaben selbsttaetig unter /tmp/claude-1000/-home-fmh-fmhc-physics/<Sitzung>/tasks/ abgelegt. Das ist der
   Sitzungsordner der Leitung neben dem Scratchpad. Inhalt: nur Laufprotokolle.
7. **Rauchtest:** Er schrieb Dateien mit Werten aus Kleinstgroessen nach /home/fmh/fmhc-physics-remote/verschraenk-dim-1/rauch/.
   Ich habe nur seine Laufzeiten angesehen, nicht die Werte.
8. **Sonst:** keine Literaturabrufe (0 von 2), kein Projekt-grep, keine verbotenen Pfade, nur die Spuren cpu und cpu2,
   jeder Lauf unter 10 min (laengster: sd mit 7 min 8 s), kein pkill/pgrep, keine Hooks.

**Laeufe [E]** (UTC, .69, kleintest.sh, 1 Thread, alle rc = 0):

| Lauf | Spur | Zeit |
|---|---|---|
| rauch | cpu | 17:03:14 bis 17:03:53 |
| s1 | cpu | 17:04:03 bis 17:05:08 |
| direkt | cpu2 | 17:04:06 bis 17:04:33 |
| sd | cpu | 17:05:13 bis 17:12:21 |
| auswertung | cpu2 | 17:12:28 bis 17:12:31 |
| bild | cpu2 | 17:12:31 bis 17:12:41 |

## 7. Einfach gesagt

Wir haben ausgerechnet, wie stark die zwei Haelften eines Gitters aus Federn quantenmechanisch miteinander verbunden
sind, wenn das Gitter 1, 2, 3 bis 200 Dimensionen hat. Je Punkt auf der Schnittflaeche wird die Verbindung mit jeder
Dimension schwaecher, weil sich jeder Punkt auf immer mehr Nachbarn verteilen muss. Gibt man aber die Gesamtzahl der
Punkte vor, dann waechst mit der Dimension die Schnittflaeche, und es gibt eine beste Dimension. Diese beste Dimension
ist 3 nur bei etwa tausend Punkten; bei einer Million Punkten ist sie 7, bei 10^80 Punkten etwa 98. Verschraenkung allein
erklaert also nicht, warum unsere Welt drei Raumdimensionen hat.

- Abgabe: 2026-10-04 19:21:10 CEST (date), nach der letzten Aenderung an dieser Datei.
