# LICHT-FINN-NETZ-1: Nachtrag Phase gegen Gruppe (gekennzeichneter Nachtrag, beschreibend)

- **Anlass:** Zusatz der Leitung (22:1x CEST) nach einer Pruefnotiz von Codex (ROOT-REVIEW-2003.txt, nicht von mir
  gelesen). Der Nachtrag aendert keine Urteilsregel und beruehrt LF0 bis LF2 nicht. Plan, Code und Ergebnis der Karte
  bleiben eingefroren und unveraendert (PLAN.md.eingefroren-20261004-215914, code/licht_netz.py.eingefroren-...).
- **Zeiten (date):** Nachtrag-Plan ab 22:10:00 CEST, nach dem Hauptlauf und nach dem ersten Entwurf von ERGEBNIS.md.
- Kennzeichen wie im ERGEBNIS: [E] gerechnet, [M] eigene Mathematik, [S] an der Quelle gelesen, [P] Projektdatei,
  [K] Kopfrechnung.

## N0. Plan des Nachtrags (vor dem Nachtrag-Lauf geschrieben)

- **Frage 1:** Gelten a2, a4 fuer omega/k (Phase) oder fuer domega/dk (Gruppe)?
- **Frage 2:** Schranke in der Konvention der Quelle (LHAASO, lokal RUNDE-34/grb-221009a/quellen/
  lhaaso-2402.06009.txt), mit Fundstelle.
- **Frage 3:** Hat WEYL-LINEAR-1 bei l < 5,9e-28 m Phase und Gruppe richtig zugeordnet? Faktor, falls nicht.
- **Rechnung:** neues Skript code/nachtrag_gruppe.py. Es liest lauf-69/ergebnis.json (eingefroren erzeugt) und
  rechnet je Zweig auf Finns Netz:
  - die Gruppenkoeffizienten g1 = 2 a1, g2 = 3 a2, g4 = 5 a4 (Mittel, min, max ueber die 26 Richtungen);
  - die Schranke auf zwei Wegen: ueber Gl. (1) (Phase) und ueber Gl. (2) (Gruppe, Faktor (n+1)/2 = 3/2). Beide muessen
    gleich sein;
  - zur Pruefung die zwei falschen Zuordnungen (Faktor sqrt3 nach oben bzw. unten);
  - die WEYL-LINEAR-1-Zahl mit kappa = 0,117.
- **Festlegung [F, Nachtrag]:** abs(a2) < 1e-6 gilt als null (Grover laengs der Achsen); dort gibt es keine Schranke.
  Superluminale Werte (n = 2: 7,0e11 GeV) braucht es nur bei a2 > 0; das kommt nicht vor.
- **Erwartung:** gleiche Zahlen wie im ERGEBNIS (Abschnitt 4), relativ auf ~1e-15. Kein Urteil.
- Lauf: N1 auf cpu11 ueber kleintest.sh, <= 600 s, 1 Thread. Einfrieren von Skript und diesem Abschnitt vorher
  (NACHTRAG-EINGEFROREN-SHA256.txt).

## N1. Ergebnis des Nachtrags (Text ab 22:11:00 CEST)

- **Zeiten:** Nachtrag-Skript und Abschnitt N0 eingefroren 22:10:30 CEST (NACHTRAG-EINGEFROREN-SHA256.txt, auf der .69
  dieselben Pruefsummen). Syntaxpruefung 20:10:23 UTC, Lauf N1 (cpu11) 20:10:38 UTC, rc = 0.
- **Frage 1: a1, a2, a4 sind Phasenkoeffizienten [E, Code].** licht_netz.py fittet omega/k (Funktion fit: y = om/kk)
  zu omega/k = c (1 + a1 k + a2 k^2 + ...). Das Gruppentempo ist domega/dk = c (1 + 2 a1 k + 3 a2 k^2 + 4 a3 k^3 +
  5 a4 k^4 + ...). Alle Tabellen im ERGEBNIS (Abschnitte 1 bis 3) nennen Phasenkoeffizienten.
- **Gruppenkoeffizienten [E, N1], 26 Richtungen:**

| Zweig | g2 = 3 a2: Mittel (min bis max) | g4 = 5 a4: Mittel (min bis max) | g1 = 2 a1: max abs |
|---|---|---|---|
| M-D Maxwell (beide Pol.) | -0,3045 (-0,3333 bis -0,2500) | +0,0228 (+0,0104 bis +0,0319) | 0 (<= 2e-12) |
| S-D, S-P Skalar | -0,1170 (-0,1458 bis -0,0625) | -0,0040 (-0,0173 bis +0,0026) | 0 (<= 4e-9) |
| W-D Weyl (lo, hi) | -0,3910 (-0,5000 bis -0,2500) | +0,0273 (+0,0104 bis +0,0417) | 0,7071 |
| Q-W Weyl-Automat | -0,277 (-1,095 bis -0,045) | -0,021 (-0,203 bis +0,781) | 2,270 |
| Q-G Grover | -0,0545 (-0,0833 bis 0) | -0,0103 (-0,0266 bis 0) | 0 (<= 2,2e-11) |

- **Frage 2: Konvention der Quelle [S, gelesen 22:08 CEST]:** lhaaso-2402.06009.txt
  - Gl. (1), Z. ~165 bis 172 (zweispaltige Textfassung, Formel zerrissen): E^2 ~ p^2 c^2 [1 - sum_n s (E/E_QG,n)^n];
    "where E and p are the energy and momentum of a photon, s = +-1 is the 'sign' of the LIV effect"
    (Z. 171/172 und 131).
  - Gl. (2), Z. 141 bis 147: "the photon group velocity is then given by" v(E) = dE/dp ~ c [1 - s (n+1)/2
    (E/E_QG,n)^n].
  - Gl. (3), Z. 154 bis 158: Laufzeitversatz mit demselben Faktor (n+1)/2.
  - Grenzen: Z. 466 bis 471 ("E_QG,2 > 6.9 x 10^11 GeV (E_QG,2 > 7.0 x 10^11 GeV) for a subluminal (superluminal)
    LIV effect"; linear 1,0e20 bzw. 1,1e20 GeV); Tabelle Z. 446.
  - **Zuordnung [M]:**
    - Aus Gl. (1) folgt das Phasentempo E/p = c [1 - (s/2)(E/E_QG,n)^n], aus Gl. (2) das Gruppentempo mit (n+1)/2,
      bei n = 2 also 3/2.
    - Netz und Quelle passen auf beiden Wegen zusammen:
      - Phase a2 gegen -(s/2): l = hbar c / (E_QG,2 sqrt(2 abs(a2)))
      - Gruppe 3 a2 gegen -s (3/2): l = hbar c sqrt((3/2)/(3 abs(a2))) / E_QG,2, dasselbe
  - **Gerechnet [E, N1]:** Beide Wege geben je Zweig dieselbe Zahl (relativ <= 2,6e-16) und dieselben Werte wie das
    eingefrorene ERGEBNIS. Die Schranken im ERGEBNIS sind also schon in der Konvention der Quelle gerechnet:
    - M-D: konservativ 7,0e-28 m (Achsen), Mittel 6,3e-28 m, streng 6,1e-28 m
    - S-D/S-P: 1,4e-27 / 1,0e-27 / 9,2e-28 m
    - W-D: 7,0e-28 / 5,6e-28 / 5,0e-28 m, linear 2,8e-36 m (a1 < 0, 1,0e20 GeV) bzw. 2,5e-36 m (a1 > 0, 1,1e20 GeV)
    - Q-W: 1,7e-27 / 6,7e-28 / 3,3e-28 m, linear 8,7e-37 bzw. 7,9e-37 m
    - Q-G: laengs der 6 Achsen keine Schranke (a2 = 0); ohne die Achsen konservativ 1,4e-27 m, Mittel 1,5e-27 m,
      streng 1,2e-27 m
  - Wer den Phasenkoeffizienten a2 direkt gegen (3/2)(E/E_QG,2)^2 setzte (Phase als Gruppe gelesen), bekaeme l um
    sqrt3 zu gross (M-D konservativ 1,2e-27 m). Umgekehrt, wer 3 a2 gegen (1/2)(E/E_QG,2)^2 setzte, bekaeme l um sqrt3
    zu klein (4,0e-28 m). Beides steht nur zur Pruefung in nachtrag-gruppe.json.
- **Frage 3: WEYL-LINEAR-1, l < 5,9e-28 m [P, E]:**
  - kappa = 0,117 stammt aus STRICH-NETZ-1. Dort ist v = E_zentrum / k (strichnetz.py Z. 787), also das
    **Phasentempo** v = 1 - kappa k^2.
  - WEYL-LINEAR-1 rechnet das Gruppentempo 1 - 3 kappa k^2 und setzt es gegen (3/2)(E/E_QG,2)^2 (WEYL-LINEAR-1 PLAN
    Abschnitt 2, ERGEBNIS 3.1). Daraus folgt l = hbar c / (E_QG,2 sqrt(2 kappa)).
  - **Die Zuordnung ist richtig, Faktor 1.** N1 rechnet 5,912e-28 m auf beiden Wegen.
  - Waere kappa als Gruppenkoeffizient gelesen worden, kaeme 1,024e-27 m heraus (Faktor sqrt3).
  - Vorbehalt: Die Laengeneinheit dort ist n^(-1/3) des Zufallsnetzes, hier die Tetraederkante; die Zahlen sind
    deshalb nicht direkt vergleichbar.
- **Nicht geprueft:** die Martynenko-Zahl des Dossiers (2,4e14 GeV) und ihre Konvention; Codex' Pruefnotiz selbst habe
  ich nicht gelesen.

## N2. Selbstanzeigen zum Nachtrag

1. Nachtrag nach Sicht auf alle Ergebnisse geschrieben und gerechnet; er ist beschreibend und aendert kein Urteil.
2. Neues Skript code/nachtrag_gruppe.py (eingefrorener Code unveraendert). Syntaxpruefung und Lauf N1 ueber
   kleintest.sh (cpu11).
3. Schwelle abs(a2) < 1e-6 fuer "null" erst im Nachtrag festgelegt (vor N1). Im eingefrorenen Code fehlte sie; dort
   stand fuer Q-G die Rausch-Schranke 3,1e-23 m.
4. Die Quelle ist eine zweispaltige Textfassung. Gl. (1) ist dort zerrissen; ich habe sie aus den Bruchstuecken
   ("E ~ p c 1 - s", "2 2", "X", "n=1", "EQG,n") und dem Satz in Z. 171/172 gelesen [S, mit diesem Vorbehalt].
