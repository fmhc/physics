# EINE-WELT-LOCH-1: Werden aus den zwei Graviton-Welten eine, wenn man die Loecher von Finns Netz fuellt? (Runde 41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 16:01:47 CEST (date), vor jeder
  Rechnung.
- **Herkunft:**
  - Kartenvorschlag K2 aus TETRAEDER-L (RUNDE-37/tetraeder-l/DOSSIER.md, Abschnitt Kartenvorschlaege).
  - Finns Wunsch (04.10., nach 14:20), K-A "um das doppelte" zu erleichtern.
- **Anlass:**
  - TENSOR-EIS-PYRO-1 (Bauweise B1: Eichfreiheit an den Tetraedermitten, Kanten als Laengen) gab Gravitonen, aber
    doppelt: zwei Welten ohne gegenseitige Anziehung, die 1/2 nur langwellig.
  - TETRAEDER-L [M, Agent]: Im Pyrochlor gehoert jede Kante genau einem Tetraeder, also Werte auf Kanten koppeln Auf und
    Ab nie.
  - Kanten durch die Loecher (Stumpf-Tetraeder) verbinden Ecken verschiedener Tetraeder und koppeln Auf und Ab.
- **Ableitbarkeitsprobe (Leitung, nach TETRAEDER-L):**
  - Die Zahl der eichinvarianten Variablen je Zelle ist ableitbar (E - 4V bzw. E - 3V; Pyrochlor-Zelle mit 4 Ecken,
    12 Kanten, 2 Tetraedern, 2 Stumpf-Tetraedern [M, Agent]).
  - Nicht ableitbar ist, wie viele davon masselos bleiben, mit welchem Tempo und ob das Netz stabil bleibt.
  - Projekt-grep (TETRAEDER-L): keine Rechnung mit gefuellten Loechern.
  - Kein Vorab-Ergebnis in den Rohdaten von TENSOR-EIS-PYRO-1 (dort nur Pyrochlor ohne Fuellung).
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Lesen:**
   - TENSOR-EIS-PYRO-1 vollstaendig (ERGEBNIS, PLAN, code/tp.py, tp_auswertung.py)
   - TETRAEDER-L DOSSIER (K2, "Warum zwei Welten", Frage 3)
   - RUNDE-36/REGEL.md (1/2-Regel)
   - RUNDE-37/takt-umbenennung-l/DOSSIER.md (Abschnitt 4, A4: Gitter und Symmetrie)
2. **Schreibtisch im PLAN:**
   - Fuellung der Loecher vorab symmetrisch festlegen, sonst ist die Wuerfelsymmetrie gebrochen. Standard: ein
     Mittelpunkt je Stumpf-Tetraeder, verbunden mit seinen 12 Ecken; die Sechseckflaechen symmetrisch zerlegen. Eine
     zweite, kantenaermere Variante darf dazu.
   - Die Bauweise B1 sinngemaess auf das gefuellte Netz uebertragen und das begruenden. Kanten sind Laengen, Eichfreiheit
     an den Tetraedermitten; neue Simplizes entsprechend.
   - Variablen und Eichrang je Zelle zaehlen (ableitbar, Kontrolle).
3. **Rechnung wie in TENSOR-EIS-PYRO-1:**
   - langwellige Moden mit omega^2 > 0 und TT-Anteil, Luecke der Zusatzmoden, Tempo
   - Kontrolle: ohne Fuellung die Zahlen von TENSOR-EIS-PYRO-1 wiederfinden
4. **Plan, Rauchlauf, Einfrieren wie ueblich.**

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| EW0 | Kontrolle: Ohne Fuellung reproduziert der Code die Modenzahlen und Tempi von TENSOR-EIS-PYRO-1 (Modenzahlen gleich, Tempi auf 1e-8) | 90 % |
| EW1 | [H] Mit gefuellten Loechern gibt es langwellig genau zwei masselose TT-Moden (eine Welt); alle uebrigen eichinvarianten Moden haben eine Luecke | 35 % |
| EW2 | [H] Mit gefuellten Loechern bleiben vier masselose TT-Moden (weiter zwei Welten) | 30 % |
| EW3 | [H] Mit gefuellten Loechern wird das Netz instabil (omega^2 < 0 bei kleinem k) | 25 % |

**Bedeutung (vorab):**
- **EW1 trifft ein:** Finns Netz bekommt durch Striche durch die Loecher eine einzige Schwerkraft-Welt. Naechste Frage:
  Gilt dann die 1/2 auch kurzwellig?
- **EW2:** Die Loecher koppeln die Welten nicht genug; der Weg zu einer Welt fuehrt dann ueber den Takt
  (PACHNER-TAKT-1) oder eine andere Fuellung.
- **EW3:** Die Fuellung braucht zusaetzliche Regeln (Steifigkeit oder Eichung an weiteren Stellen).

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh. Spuren cpu5 und cpu, geteilt mit KOVARIANZ-KUGEL-1 bzw.
  GUERTEL-1; der Lock regelt die Reihenfolge. Ab dem Ende von KOVARIANZ-KUGEL-1 auch cpu3 und cpu4.
- Je Lauf <= 10 min, 1 Thread. Zeitbox 150 min.
