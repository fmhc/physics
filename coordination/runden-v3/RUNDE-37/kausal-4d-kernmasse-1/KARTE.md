# KAUSAL-4D-KERNMASSE-1: Laeuft massive Materie in 3+1 auf der Kausalmenge stabil, wenn die Masse im nichtlokalen Kern sitzt? (Runde 41)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 14:18:14 CEST (date), vor jeder Rechnung. Anforderungen aus
  WELTMODELL-REVIEW-1 (REVIEW.md, Abschnitt 5, Rangliste Punkt 3); Wahrscheinlichkeiten von der Leitung.
- **Anlass:**
  - KAUSAL-WELLE-4D, KAUSAL-4D-SCHICHT-1/-2: Johnstons Pfadsumme baut die Masse ausserhalb des nichtlokalen Kerns ein,
    und ihr Mittel waechst in 3+1 fuer massive Felder an; Sprungregeln druecken das nur mit exakter Feinabstimmung je
    Ordnung, bei steigendem Einzelnetz-Rauschen.
  - KAUSAL-4D-STABIL-L (DOSSIER Z. 38 und 251): Ort der Masse ausserhalb oder innerhalb der nichtlokalen Funktion ist der
    Unterscheidungspunkt.
  - Fuer den Weltmodell-Kandidaten K-B (Ereignis-Netz) ist stabile massive Materie in 3+1 eine Grundbedingung.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Literatur, [H] Hypothese.

## Anforderungen (aus dem Review)

- Die Masse sitzt im nichtlokalen Kern, nicht ausserhalb (KAUSAL-4D-STABIL-L Punkt 3). Bauweise im Plan aus Dossier und
  Literatur begruenden.
- Messgroessen: Pol des Mittels (Im omega, Nullstellenzaehlung wie in SCHICHT-1/-2) und relative Einzelnetz-Streuung gegen
  die Dichte (rho = 4, 8, 16).
- **Ableitbarkeitsprobe:** Das Mittel ist vorab rechenbar und gehoert in die Vorab-Datei (wie die Restformel in SCHICHT-2).
  Das Einzelnetz-Rauschen ist nicht ableitbar; nur dafuer lohnt die Rechnung.
- Vorab festlegen, was als Baufehler und was als Befund zaehlt (die Literatur kennt keine stabile 4D-Familie, ein
  Fehlschlag kann am Bau liegen).
- Code aus RUNDE-37/kausal-4d-schicht-2/code/ wiederverwenden.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KM0 | Kontrolle: Mit der Masse ausserhalb (V-J) werden die Pole von SCHICHT-2 bitgleich wiedergefunden | 90 % |
| KM1 | [H] Mittel mit der Masse im Kern: kein Pol mit Im omega > 0 nahe der Massenschale bei rho = 4, 8, 16 (Vorab-Datei sagt, ob das ableitbar ist) | 50 % |
| KM2 | [H] Relative Einzelnetz-Streuung faellt mit der Dichte (Steigung in log rho <= -0,2) | 55 % |

**Bedeutung (vorab):** KM1 und KM2 treffen ein: K-B traegt massive Materie in 3+1 ohne Feinabstimmung der Schichten.
KM1 verfehlt: Auch mit der Masse im Kern waechst das Mittel; K-B braucht dann einen anderen Weg fuer massive Materie.
KM2 verfehlt: Das Mittel ist stabil, aber das einzelne Netz rauscht zu stark; dann ist die Glaettungsskala Pflicht.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und cpu7; je <= 10 min.
- Plan und Vorab-Datei vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 150 min.
