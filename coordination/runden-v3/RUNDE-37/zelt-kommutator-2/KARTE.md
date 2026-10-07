# ZELT-KOMMUTATOR-2: Ist der Zeltzug-Kommutator aus PACHNER-TAKT-1 ein 4D-Pachner-Defekt, und haengt die unimodulare Uhr weniger von der Reihenfolge ab als die Randimpulse? (Runde 49, zwei gekoppelte Vorschlaege)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 12:57:50 CEST (date), vor jeder Rechnung.
- **Herkunft (zwei Vorschlaege, ein Agent, weil Code und Netz geteilt):**
  - Teil A: K2 ZELT-PACHNER-BRUECKE-1 aus LAMBDA-TURING-L (RUNDE-37/lambda-turing-l/DOSSIER.md, Abschnitt 5), Vorhersagen woertlich (ZP0 bis ZP3).
  - Teil B: K2 UNIMODULAR-KOMMUTATOR-1 aus GIELEN-RIED-TIEF-L (RUNDE-37/gielen-ried-tief-l/DOSSIER.md, Abschnitt 7), Vorhersagen woertlich, umbenannt von UK1 bis UK4 in UT1 bis UT4 (UK ist in UEBERGABE-KONFLUENZ-1 vergeben).
  - Finns Fragen: Church-Rosser bzw. Reihenfolge ("In der Reihenfolge der Sache?") und der Takt als Uhr ("Check das Tetraeder netz Artikel Ding direkt intensiv").
- **Projektbefunde [P]:**
  - PACHNER-TAKT-1 / TAKT-KOMMUTATOR-1 (RUNDE-42): Zwei Zeltzuege an Nachbarecken vertauschen flach (1e-15); mit Kruemmung bleibt D ~ eps^0,998 (a/L)^2,25 (Randimpulse bei gleichen Randlaengen). Welche Pachner-Zuege AB und BA verbinden, ist dort nicht bestimmt; das 4-Volumen ist nur als Realisierbarkeit ausgewertet.
  - LAMBDA-TURING-L: D ist eichinvariant und misst Triangulierungsabhaengigkeit.
  - GIELEN-RIED-TIEF-L: Unimodulare Zeit dT = Summe_sigma V_sigma (Gl. 36 der Arbeit); Finns Takt kann sie als globaler Zaehler sein; Kuchar: T kennzeichnet nur Klassen von Flaechen gleichen 4-Volumens.
  - TETRAEDER-L (nach Dittrich/Kaminski/Steinhaus, dort nur Abstract): Regge-Wirkung invariant unter 5-1 und 4-2.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (aus den Dossiers, von der Leitung uebernommen)

- **Teil A [M]:**
  - Ein 3-3-Zug laesst die Kantenmenge seiner 6 Ecken unveraendert. AB und BA unterscheiden sich in einer Kante; also ist kein einzelner 3-3-Zug die Verbindung, noetig sind mindestens ein 2-4- und ein 4-2-Zug.
  - Bestuende die Folge nur aus 2-4 und 4-2 mit lauter Loesungen, waere D = 0 (DKS-Invarianz, Lesart nicht an der Quelle geprueft). Das widerspricht D ~ eps. Also enthaelt die Folge einen 3-3-Zug, oder die Invarianzaussage gilt hier nicht.
- **Teil B [M]:**
  - Bei eps = 0 ist D_T = 0 exakt (dieselbe flache Region).
  - Eine innere Eckverschiebung aendert das Gesamtvolumen in erster Ordnung nicht; D_T ist eichfest.
  - Auf der Loesung gilt V_gesamt = -dS/dLambda. D_T ist also die Lambda-Ableitung des Unterschieds der Hamilton-Jacobi-Funktionen von AB und BA und damit allgemein erster Ordnung in eps, ausser eine Symmetrie hebt es auf.
- **Nicht ableitbar:** Grad der Kante A'B, die Zugfolge selbst, ob D gleich der Summe der Einzeldefekte ist, die a/L-Exponenten von Einzeldefekt und D_T.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ZP0 | Kontrolle: flache Randdaten, Defekt jedes Zugs < 1e-13 relativ | 90 % |
| ZP1 | (bedingt vorab ableitbar; Pruefung der DKS-Lesart) Die kuerzeste Folge AB -> BA enthaelt mindestens einen 3-3-Zug | 75 % |
| ZP2 | [H] D gleich der Summe der Einzeldefekte auf 1 % | 45 % |
| ZP3 | [H] Der Einzeldefekt faellt im Bereich L/a = 4 bis 32 mit einem Exponenten 2,0 bis 2,5 | 55 % |
| UT1 | [H] D_T faellt mit (a/L)^q, q >= 2,75 (schneller als D): Die Uhr ist reihenfolgefester als die Impulse | 40 % |
| UT2 | [H] 1,75 <= q < 2,75 (wie D): Die Uhr erbt die gebrochene Eichung | 45 % |
| UT3 | [H] q < 1,75 | 15 % |
| UT4 | [H] D_T ist linear in eps (Verhaeltnis der Werte bei eps = 1e-3 und 1e-4 zwischen 9 und 11) | 75 % |

**Bedeutung (vorab):**
- **ZP1 und ZP2:** Auf Finns Netz ist "Weg-Unabhaengigkeit der Zeltzuege" (Church-Rosser, HKT) dasselbe wie die Invarianz unter einer bestimmten 4D-Pachner-Folge (Triangulierungsunabhaengigkeit).
- **UT1:** stuetzt Gielen/Rieds Satz, die Randzeit bleibe im Diskreten diffeomorphismeninvariant; Finns Takt als globale unimodulare Uhr waere reihenfolgefester als die Geometrie.
- **UT2:** Kuchars Flaechen gleicher Klasse sind diskret physikalisch verschieden; die Uhr traegt denselben Fehler wie die Impulse.

## Kontrollen

- eps = 0: D_T <= 1e-13; DeltaT stimmt mit dem analytischen Schichtvolumen ueberein; die bekannten Werte von D aus PACHNER-TAKT-1 werden reproduziert.
- isolierter 4-2-Zug mit Loesung: Defekt 0 (Gegenprobe zur DKS-Lesart).
- Lapse-Varianten L und G aus PACHNER-TAKT-1 muessen dieselbe Folge ergeben.

## Rahmen

- Code-Agent. Code aus RUNDE-37/pachner-takt-1/code (pt.py) kopieren, dort nichts aendern; eingefrorenen Code nur kopiert erweitern (Skript nie in place aendern).
- Laeufe fuer L/a = 4, 8, 16, 32, beide Takte L und G, eps = 1e-3 und 1e-4.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch (euklidisch, linearisiert), keine Messdatenbestaetigung.
