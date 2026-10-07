# TENSOR-EIS-0: Ziehen sich gleichartige Ladungen in einem Tensor-Eis an? (Runde 35)

- Leitung claude-primary. Karte und Schreibtisch geschrieben ab 2026-10-03 21:36:44 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finns Tetraederbild: Kraefte in den Staeben als Weg zur Schwerkraft (RUNDE-34/tetra-konzept/WEITERGEDACHT.md,
    Abschnitt 3).
  - Schreibtisch QBALL-EIS (RUNDE-35/SCHREIBTISCH-QBALL-EIS-LAPSE.md): Eine Pfeil-Erhaltungsregel gibt nur Elektrostatik
    (Gleichnamige stossen sich ab).
  - Quelle fuer die Tensorfassung auf Finns Gitter, an der Arbeit gelesen: Yan/Benton/Jaubert/Shannon, PRL 124, 127203
    (2020), arXiv:1902.10934 (RUNDE-35.md).
  - Schleife seit 21:32: "TENSOR-EIS als Weg zur Schwerkraft".
- Kennzeichen: [M] Mathematik (hier vorab abgeleitet, also Pruefung der Rechnung, kein harter Test), [L] Literatur,
  [S] an der Quelle gelesen, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Gausssche Coulomb-Phase** [M]: freie Energie F = (K/2) int E^2 mit Nebenbedingung (Gauss-Gesetz) fuer die Ladungen;
  K ist die entropische Steifigkeit (~ T).
  - Fuer gegebene Ladungen ist F[rho] das Minimum ueber E (laengsgerichteter Teil). Der quergerichtete Teil schwankt frei
    und haengt nicht von rho ab.
- **Vektorladung** (Yan u. a., Gl. 2 und 3 [S]): E symmetrisch und spurfrei, d_i E_ij = rho_j.
  - Laengslösung im Fourierraum: E = (i/q^2)[-(q rho^T + rho q^T) + (q.rho)/(2 q^2) q q^T + (q.rho)/2 * Eins].
  - Spur und Gauss-Gesetz erfuellt; orthogonal zu allen quergerichteten spurfreien Tensoren.
  - Daraus |E|^2 = (2/q^2)(rho^2 - (q_dach.rho)^2/4), also F = K sum_q rho_i^* (1/q^2)(delta_ij - q_dach_i q_dach_j/4) rho_j.
  - Ortsraum mit FT[q_i q_j/q^4] = (delta_ij - r_dach_i r_dach_j)/(8 pi r):
    G_ij(r) = (1/(4 pi r)) [(7/8) delta_ij + (1/8) r_dach_i r_dach_j].
  - **Zwei gleiche (parallele) Vektorladungen p:** U(r, theta) = (2 K p^2/(4 pi r)) [7/8 + (1/8) cos^2 theta] > 0. Sie
    stossen sich in jeder Richtung ab, laengs p um den Faktor 8/7 staerker als quer.
  - Antiparallele Ladungen ziehen sich an; senkrechte haengen vom Winkel ab.
- **Skalarladung** (Pretko-Fraktonen [L]): d_i d_j E_ij = rho.
  - Laengslösung E_ij ~ q_i q_j rho/q^4, also F ~ K sum rho^2/q^4, und im Ortsraum G(r) = -r/(8 pi) + const.
  - Ungleiche Ladungen: linear wachsende Energie (Einschluss, wie ein String, konstante Kraft). Gleiche Ladungen: konstante
    Abstossung.
- **Folgerung** [H]: In der einfachen (Gaussschen) Tensor-Coulomb-Phase ziehen sich gleichartige Ladungen nicht an, weder
  bei Pfeilen noch bei Tensoren. Eine schwerkraftartige Anziehung muesste aus etwas anderem kommen:
  - Dynamik der Fraktonen ("Mach", Pretko 2017 [L?])
  - Kopplung an die Energie ueber die Geometrie (h_00; LAPSE-0)
- **Bekannte Kontrolle** [S, Yan u. a. Gl. 17 und Fig. 1]: Die Korrelation <E_xy(q) E_xy(-q)> der Vektortheorie zeigt
  in der [hk0]-Ebene einen vierzaehligen Pinch-Punkt, in [0kl] einen zweizaehligen.

## Test (Code-Agent, klein)

- Periodisches kubisches Gitter, L = 64 (und 32 zur Kontrolle). Gitterableitungen ueber 2 sin(q/2).
- Mindestnorm-Loesung E fuer gegebene Ladungen per FFT, ohne Nutzung der Schreibtischformel:
  - lineares Ausgleichsproblem je q mit symmetrischen spurfreien Tensoren als Unbekannten
  - kleinste Norm per Pseudoinverse
- F fuer zwei Ladungen in Abstaenden r = 2 bis 16 und mindestens 12 Richtungen (theta zwischen p und r).
  - Vektorladungen parallel, antiparallel und senkrecht.
  - Skalarladungen gleich und ungleich, gesamt neutral bzw. mit Hintergrund.
- Querkorrelation (Projektor auf quergerichtete spurfreie Tensoren) in [hk0] und [0kl] als Bild.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| T0 | Kontrolle: Gauss-Gesetz und Spurfreiheit der Loesung auf 1e-10; das Gitter-F trifft fuer r >= 4 die Kontinuumsformel innerhalb 3 % (L = 64) | 85 % |
| T1 | Parallele Vektorladungen: Wechselwirkung U > 0 fuer alle gemessenen r >= 2 und alle Richtungen (Abstossung ueberall) | 90 % |
| T2 | Anisotropie U(theta = 0)/U(theta = 90 Grad) bei r = 8 gleich 8/7 = 1,143 innerhalb 3 % | 80 % |
| T3 | Ungleiche Skalarladungen: U(r) - U(4) waechst linear; Steigung zwischen r = 8 und 16 aendert sich um weniger als 10 % | 75 % |
| T4 | Bekannte Kontrolle: vierzaehliger Pinch-Punkt in [hk0], zweizaehliger in [0kl] (Bildvergleich mit Fig. 1b/c) | 85 % |

**Bedeutung (vorab):**
- T1 bis T3 treffen ein: Auch ein Tensor-Eis auf Finns Gitter gibt keine Schwerkraft im einfachen Sinn. Gleichartige
  Ladungen stossen sich ab (Vektor) oder werden konstant auseinandergedrueckt (Skalar), ungleiche sind wie ueber einen
  String gebunden (Skalar).
  - Der Weg "Kraefte in den Staeben -> Schwerkraft" braucht dann eine zusaetzliche Zutat (Energiekopplung ueber
    Geometrie oder Fraktonendynamik).
- T1 verfehlt: Es gibt Richtungen mit Anziehung zwischen gleichen Ladungen. Das waere fuer Finns Bild wichtig; dann
  Kopplung und Gitterursache genau beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu oder p4000a (nicht cpu2, cpu3, cpu4, cpu5, cpu6,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 75 min.

## Berichtigungsvermerk (2026-10-03 22:39:20 CEST)

- Diese Datei hat der frische Gegenleser geprueft: RUNDE-35/GEGENLESEN-R35.md. Gueltige Fassung der betroffenen Stellen: RUNDE-35.md, Abschnitt "Berichtigung nach GEGENLESEN-R35". Der urspruengliche Text bleibt zur Nachvollziehbarkeit stehen.
