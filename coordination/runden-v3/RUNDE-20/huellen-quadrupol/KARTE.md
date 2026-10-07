# HUELLEN-QUADRUPOL: Stille Quadrupol-Stellen (l = 2) und ihr Versatz (Runde 20)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 17:07:29 CEST (date), vor jeder Rechnung.
- Herkunft: HUELLEN-DIPOL (Runde 19).
  - 19 stille Dipol-Stellen auf 5 Leitern, Abstand wie bei l = 0 (+1,7 bis 2,9 %).
  - Versatz nach aussen 0,34 bis 0,47 Abstaende.
  - Schreibtisch-Lesart der Leitung [H]: Phase der Innenwelle j_l ~ sin(kr - l pi/2), also Versatz ~ l/2 Abstaende.
- Explorativ (v3), Hypothesen [H].

## Vorgehen

- Wie HUELLEN-DIPOL, mit Zentrifugalterm l(l + 1)/r^2 = 6/r^2 und Regularitaet ~ r^2.
- **K1:** Der Code muss mit l = 1 drei bekannte Dipol-Stellen aus HUELLEN-DIPOL auf 1e-6 wiederfinden, und mit l = 0 drei
  bekannte Atmungsstellen aus Runde 18.
- **Suche:** M2, l = 2, omega^2 von 0,80 bis 1,40, Bereich E1, zwei Gitterstufen. Zaehlung wie im Vorlaeufer, Rechteck-Umlauf
  an allen Funden.
- **Versatz:** Je Kurve werden die l = 2-Sprossen R_2 mit den l = 0-Sprossen R_0 derselben Kurvenordnung verglichen (wie in
  HUELLEN-DIPOL, Kriterium von dort uebernehmen). Versatz v = (R_2 - R_0,unten)/Abstand, modulo 1, in [0, 1).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Q0 | K1 bestanden | 90 % |
| Q1 | Mindestens 5 stille Quadrupol-Stellen in E1 | 75 % |
| Q2 | Abstand in R je Kurve fast fest (Streuung < 10 %) und innerhalb +-5 % des l = 0-Abstands | 60 % |
| Q3 | Versatz v im Mittel zwischen 0,6 und 1,0 (Lesart ~ l/2 = 1,0 mit derselben Krummungskorrektur wie bei l = 1) | 50 % |

**Bedeutung (vorab):**
- Treffen Q1 bis Q3 ein: Eine Sprossenregel fuer alle l, R_n,l ~ (n + l/2 + konst) pi/k_innen [H].
- Trifft Q3 nicht ein: Der Versatz hat eine andere Ursache.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6, je <= 10 min.
- Plan vorab einfrieren. Zeitbox 120 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
