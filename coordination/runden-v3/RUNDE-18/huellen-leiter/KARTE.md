# HUELLEN-LEITER: Wie viele stille Stellen hat der Q-Ball mit Huelle, und wie sind sie geordnet? (Runde 18)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 13:40:13 CEST (date), vor jeder Rechnung.
- Herkunft: Im Zweifeldmodell M2 sind die Huellen-Stellen jetzt von drei Rechnungen getragen.
  - STILLE-ZWEIFELD: 15 Stellen, omega^2 0,819 bis 1,159.
  - ZWEIFELD-NACHBAU: blind 9, post hoc.
  - HUELLEN-UHR: zwei im Zeitbereich, vorab gewertet.
- Offen: etwa 26 Kandidaten unter omega^2 ~ 0,82 sind unbearbeitet. Die Stellen liegen auf vier Kurven von
  chi-Schwingungen (Beobachtung ZWEIFELD-NACHBAU).
- Vergleich Einfeld-Modell M1: Dort bilden die stillen Stellen eine Leiter (in 3D blind bis n = 15).
- Explorativ (v3), Hypothesen [H].

## Frage und Vorgehen

- Vollstaendige Suche im ganzen Duennwand-Bereich mit Huelle, omega^2 von 0,74 (knapp ueber der Schranke 0,728) bis 1,40,
  in E1. Code und Messgroesse wie validiert (W2 = s + i m_a; STILLE-ZWEIFELD- bzw. ZWEIFELD-NACHBAU-Code), adaptive
  Verfeinerung bis aufgeloest.
- **Ordnen:**
  - Je Stelle die zugehoerige chi-Modenkurve k: Index der inneren chi-Schwingung des Hintergrunds bei rho, z. B. Zahl
    der Knoten der c-Komponente.
  - Je Kurve: omega^2-Lagen, Huellenradius R(omega^2), Abstaende.
- **Leiterfrage:**
  - Haeufen sich die Stellen gegen die Duennwand-Schranke (omega^2 -> 0,728, R -> unendlich)?
  - Ist der Abstand in R etwa konstant?
- **Kontrollen:**
  - K1: bewiesene M1-Stelle mit chi-Kopplung aus.
  - Zwei Gitterstufen je Fund.
  - Die 15 bekannten Stellen muessen wiedergefunden werden.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L1 | Alle 15 bekannten Stellen werden wiedergefunden (Lage auf 1e-6) | 90 % |
| L2 | Unter omega^2 = 0,819 liegen mindestens 10 weitere Stellen | 60 % |
| L3 | Auf jeder der vier chi-Kurven werden die Stellen zur Schranke hin dichter (Abstaende in omega^2 nehmen ab) | 70 % |
| L4 | Pro chi-Kurve sind die Abstaende im Huellenradius R ungefaehr konstant (Streuung < 25 %) | 50 % |
| L5 | Es gibt eine fuenfte oder weitere chi-Kurve mit Stellen bei kleinerem omega^2 | 45 % |

**Bedeutung (vorab):**
- Treffen L2 bis L4 ein: Die Huelle traegt eine eigene Leiter stiller Stellen, die zur duennen Wand hin unendlich viele
  Sprossen hat [H]. Mechanismus: Die Kopplung der chi-Mode an den offenen Kanal wechselt periodisch mit dem Radius das
  Vorzeichen.
- Treffen sie nicht ein: Die Stellen sind vereinzelt; dann den Mechanismus anders suchen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu, cpu2, cpu3 und cpu4, je <= 10 min.
- Plan vor dem ersten Lauf einfrieren; Nachtraege nur eingefroren. Zeitbox 120 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
