# HUELLEN-DIPOL: Hat der Q-Ball mit Huelle auch stille Dipol-Schwingungen (l = 1)? (Runde 19)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 15:41:05 CEST (date), vor jeder Rechnung.
- Herkunft: Im Zweifeldmodell M2 sind bisher nur Atmungsmoden (l = 0) gerechnet.
  - 88 stille Stellen auf 10 Leitern, bis R = 39.
  - Im Zeitbereich vorab gewertet bestaetigt.
- Im Einfeld-Modell M1 ist die Dipol-Stelle l = 1, n = 1 rechnergestuetzt bewiesen: omega^2 = 0,7544960184,
  rho = 1,8263420673 (BEWEIS-2, RUNDE-10).
- Frage: Traegt die Huelle auch Dipol-Leitern?
- Explorativ (v3), Hypothesen [H].

## Vorgehen

- Linearisierung wie STILLE-ZWEIFELD bzw. HUELLEN-LEITER, mit Zentrifugalterm l(l + 1)/r^2 = 2/r^2 in allen drei Kanaelen.
  - Regularitaet am Ursprung ~ r^l.
  - Kanaele und Schwellen unveraendert (gegen 2).
  - Messgroesse und Zaehlung wie im Vorlaeufer (W = m_ac + i m_bc, Zellen-Umlauf, Rechteck-Stichproben).
- Triviale Moden (Translation, rho = 0) liegen ausserhalb von E1 und duerfen nicht gezaehlt werden. Das ist im Plan zu
  pruefen.
- **K1 (Kontrolle):** M1 (chi-Kopplung aus, U = S - S^2 + S^3/2, Schwelle 1), l = 1. Gesucht ist die bewiesene Stelle auf
  1e-6, Umlauf aufgeloest.
- **Suche:** M2, l = 1, omega^2 von 0,80 bis 1,40 (Huellenradius bis etwa 20 bis 25), Bereich E1, zwei Gitterstufen.
- **Ordnen:** nach chi-Kurven (l = 1-Moden der Huelle) mit Abstand in R; Vergleich mit l = 0 (HUELLEN-LEITER).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| D0 | K1 bestanden (bewiesene M1-Dipolstelle auf 1e-6) | 90 % |
| D1 | In M2 gibt es im Bereich E1 stille Dipol-Stellen (mindestens 5 im Fenster) | 75 % |
| D2 | Sie liegen auf chi-Kurven mit fast festem Abstand in R (Streuung < 15 %) | 60 % |
| D3 | Dieser Abstand liegt innerhalb +-15 % des l = 0-Abstands bei gleichem R (gleiche Innenwellenzahl) | 50 % |
| D4 | Die M1-Dipolstelle hat im Zweifeldmodell keinen Nachfolger mit nur einem offenen Kanal (rho = 1,83 > sqrt(2)) | 75 % |

**Bedeutung (vorab):**
- Treffen D1 und D2 ein: Die Huelle traegt auch Dipol-Leitern. Der Mechanismus ist nicht an l = 0 gebunden [H].
- D3 prueft, ob die Sprossenregel (halbe Innenwellenlaenge) fuer beide l dieselbe ist.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6 (cpu bis cpu4 belegt HUELLEN-LEITER-2), je <= 10 min.
- Plan vor dem ersten Lauf einfrieren; Nachtraege nur eingefroren. Zeitbox 120 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
