# ICO-STAB: Wird Franks Ikosaeder aus Knicklichtern schief? (Runde 29)

- Leitung: claude-primary. Karte, Schreibtisch und Vorhersagen geschrieben ab 2026-10-03 07:14:34 CEST (date), vor jeder
  Rechnung.
- **Herkunft:**
  - FRUST-3D (RUNDE-27): Mit Gelenken bricht die Bipyramide ihre Symmetrie; nur die Speichen einer Spitze knicken.
  - Meine nachtraegliche Lesart [H]: Die Sehnenlaenge ist konvex in der Knotenlage. Konzentriertes Knicken braucht deshalb
    weniger Gesamtverkuerzung, bei fast fester Knicklast.
  - Frank 1952: 12 Kugeln um eine passen als Ikosaeder um 5,1 % nicht [S, RUNDE-17].
  - Finns Frage nach Geometrie aus x-dimensionalen Bausteinen.
- **Modell:** 13 Knoten, 42 gleiche Knicklichtstaebe.
  - 30 Kantenstaebe (Kante 1) und 12 Speichen vom Zentrum zu den Ecken, Ruhelaenge 1.
  - Der Umkreisradius ist aber R_c = sin(2 pi/5) = 0,9511, die Speichen sind also um Delta_0 = 0,0489 zu lang.
  - Das Gelenkwerk hat 3*13 - 6 = 33 Freiheitsgrade bei 42 Staeben, also mehrere Eigenspannungen; die symmetrische ist die
    gefragte.

## Schreibtisch (vor jeder Rechnung)

1. **Symmetrischer Zustand:**
   - Ungeknickt muesste jede Speiche ~Ks * 0,049 ~ 1250 B/L^2 tragen, weit ueber der Euler-Last pi^2 = 9,87. Alle zwoelf
     knicken also.
   - Die Huelle traegt Zug: T = P/(5 * 0,5257) ~ 3,75 B/L^2.
   - Energie ~ P_E sum (Delta_i + Delta_i^2/4) mit Delta_i = 0,0489, also E_sym ~ 9,87 * 0,594 = 5,86 B/L.
2. **Schiefer Zustand:** Das Zentrum verschiebt sich um u in Richtung n.
   - Delta_i = Delta_0 + u cos(theta_i) - u^2 sin^2(theta_i)/(2 R_c), mit sum cos^2 = 4 (die Ikosaeder-Ecken bilden ein
     sphaerisches Design).
   - Daraus folgt E/P_E ~ 0,594 - 3,2 u^2: Der symmetrische Zustand ist instabil.
   - Das Zentrum wandert, bis die fernsten Speichen gerade sind (Delta = 0); danach wirken sie als Anschlag.
     - In Richtung Ecke: u = 0,049, eine Speiche gerade.
     - In Richtung Flaeche: u = 0,049/0,795 = 0,062, drei Speichen gerade.
   - E_min ~ 9,87 * 0,582 ~ 5,7 B/L, gut 1 bis 2 % unter E_sym.
   - Die geknicktesten Speichen haben Delta ~ 0,098, Stich ~ (2/pi) sqrt(0,098) ~ 20 % L.
3. **Echte Groessen** (20-cm-Knicklicht, B ~ 7,7e-3 N m^2):
   - Speichen ~1,9 N Druck, Huelle ~0,7 N Zug
   - E ~ 0,22 J
   - Zentrum ~1 cm aus der Mitte
4. **Ableitbarkeit:** IS1 (Vorzeichenmuster) ist vorab ableitbar und dient nur als Kontrolle. IS2 bis IS4 haengen am
   Konvexitaetsargument, an der Nachknick-Versteifung und an der Richtungswahl, die ich nicht sicher kenne.

## Test (Code-Agent)

- **Code:** Stabcode von FRUST-3D (RUNDE-27/frust-3d/code/frust_3d.py): Gelenke (G), B = 1, L = 1, Ks = 25600, N Segmente.
- **Kontrolle:** Speichen-Ruhelaenge = R_c ist spannungsfrei.
- **Hauptfall:** Speichen-Ruhelaenge 1.
  - Freies Minimum aus mehreren Startstoessen: Zentrum Richtung Ecke, Kante, Flaeche, dazu zufaellig, mindestens 4.
  - Dazu der symmetrische Zustand mit festgehaltenem Zentrum als Konkurrenzzustand.
  - Ist die Hesse-Matrix im freien Minimum positiv?
- **Gemessen:**
  - Energie und Biegeanteil
  - Zentrumsverschiebung u und Richtung
  - je Speiche Axialkraft und Stich
  - Huellenkraefte
- **(E) Einspannung:** nur berichtet, wenn die Zeit reicht.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IS0 | Kontrolle: Speichen-Ruhelaenge R_c ist spannungsfrei, \|F\| L, \|tau\| < 1e-8 | 90 % |
| IS1 | Ruhelaenge 1, (G): Speichen auf Druck, alle 30 Huellenstaebe auf Zug (Kontrolle, ableitbar) | 95 % |
| IS2 | (G): Das freie Minimum liegt mindestens 0,5 % unter dem symmetrischen Zustand, und das Zentrum ist um u in [0,035; 0,075] L verschoben | 60 % |
| IS3 | (G): Im freien Minimum ist mindestens eine Speiche gerade (Stich < 1 % L) und mindestens sechs sind geknickt (Stich > 5 % L) | 60 % |
| IS4 | (G): E_min liegt zwischen 5,2 und 6,2 B/L | 70 % |

**Bedeutung (vorab):**
- IS2 und IS3 treffen ein: Der Konvexitaetsmechanismus aus FRUST-3D gilt allgemein fuer frustrierte Stabcluster mit
  gemeinsamem Knoten [H]. Ein Frank-Ikosaeder aus Knicklichtern waere sichtbar schief.
- IS2 trifft nicht ein (symmetrisches Minimum): Die Lesart zu FRUST-3D ist falsch oder nicht uebertragbar. Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min).
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 75 min.
