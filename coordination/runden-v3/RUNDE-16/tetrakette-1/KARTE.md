# TETRAKETTE-1: Ist die Tetraederkette "11+1" bzw. "19+1" besonders? (Runde 16)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 09:34:03 CEST (date), vor jeder Codezeile.
- Auftrag Finn (02.10., woertlich): "mach weiter, rechne die tetraederkette 11+1 und 19+1".
- Anlass: Die Gegenlesung von v2 (U1) zeigte, dass bisher nur Ringvarianten gerechnet waren, nicht Variante T.
- Explorativ (v3). Die Leitung rechnet selbst auf der .69 (kleintest.sh, Spuren cpu, cpu2), mit eigenem Code.
- Codex' Code (tetra-chain/codex/) wird nicht gelesen; nur seine Ergebniszahlen dienen als Kontrolle eines anderen
  Hauses.

## Kette

- Regulaere Tetraeder mit Kante 1. Start ist ein regulaeres Tetraeder v0..v3.
- Jede neue Ecke v_n ist die Spiegelung von v_(n-4) an der Ebene durch v_(n-3), v_(n-2), v_(n-1). Das ist Codex'
  Rekonstruktion des Buendels und die Boerdijk-Coxeter-Helix [L?].
- Kanten: alle Paare mit |i - j| <= 3, also 3N - 6 Kanten bei N Ecken.
  - "11+1" = 12 Ecken, 9 Tetraeder, 30 Kanten.
  - "19+1" = 20 Ecken, 17 Tetraeder, 54 Kanten.
- Scan ueber N = 4 bis 33 Ecken, damit 12 und 20 Nachbarn auf beiden Seiten haben.

## Messgroessen

- **K0 Geometrie:**
  - Drehwinkel theta und Steighoehe je Ecke um die Helixachse; Achse aus der Schraubung v_i -> v_(i+1).
  - Fuer jedes N der kleinste Azimutabstand zweier Ecken, einmal modulo 360 Grad (gleiche Seite) und einmal modulo
    180 Grad (dieselbe Ebene durch die Achse, wichtig fuer Ticks einer drehenden Achsenebene).
- **K1 Mechanik:** spannungsfreie Federn an allen Kanten, m = k = 1.
  - Gemessen: Zahl der Nullmoden und kleinste positive Kreisfrequenz omega_1.
- **K2 Schnitte wie im Buendel:** zufaellige Ebenen durch den Eckenschwerpunkt, gleichverteilte Normalen,
  2 x 200 000 je N.
  - Mittel und Varianz von P, P(C > 1).
  - Identitaet P = T3 + 2 T4 + 2C in jeder Stichprobe.
- **K3 Feldklumpen** (Gleichung wie V5/S6, V' = 1 - 2S + 1,5 S^2):
  - Grosser Ast, omega^2 = 0,8, je an einer mittleren Ecke und an Ecke 0.
  - J_max mit Lokalisierungskriterium: Anteil am Startknoten >= 0,5, 200 Fortsetzungsschritte.
- **K4 Lennard-Jones:**
  - Kette mit Kante 2^(1/6) lokal relaxieren. Bleibt sie ein lokales Minimum (Hesse-Matrix ohne negative Richtung
    ausser den 6 Nullmoden)? Wie weit weicht sie von der Ausgangsform ab?
  - Energie E_kette(N), Abstand zum globalen Minimum aus STABIL-6-8-12 (N <= 25), D2 von E_kette.

**Kriterium "auffaellig" (vorab):**
- Fuer jede stetige Groesse X(N): Residuum r(N) = X(N) - p(N), wobei p ein quadratischer Fit ueber N-4..N+4 ohne N
  selbst ist.
- sigma = robuste Streuung (1,4826 x MAD) aller Residuen fuer N = 8..29.
- Auffaellig heisst |r|/sigma > 3.
- Geprueft fuer:
  - log omega_1
  - mittleres P, Var P, P(C > 1)
  - J_max (Mitte)
  - E_kette/N und D2(E_kette)
- Berichtet werden alle markierten N, nicht nur 12 und 20.

## Schreibtisch der Leitung (vorab, mit [L?] fuer die Helixwerte)

- Fuer die Boerdijk-Coxeter-Helix gilt [L?]:
  - Drehwinkel je Ecke theta = arccos(-2/3) = 131,8103 Grad
  - Steighoehe 1/sqrt(10) = 0,3162
  - Radius 3 sqrt(3)/10 = 0,5196
- theta/360 = 0,366139 hat den Kettenbruch [0; 2, 1, 2, 1, 2, ...] mit den Naeherungen 1/3, 3/8, **4/11**, 11/30.
  Die Naeherungsbrueche dazwischen sind 7/19 usw.
- Daraus folgt der Azimutversatz nach k Schritten:

  | k | Versatz zur naechsten vollen Drehung |
  |---|---|
  | 3 | 35,4 Grad |
  | 8 | 25,5 Grad |
  | **11** | **9,9 Grad (vier Umlaeufe)** |
  | **19** | **15,6 Grad (sieben Umlaeufe)** |
  | 22 | 19,8 Grad |
  | 30 | 5,7 Grad |

  Modulo 180 Grad: k = 4 ergibt 12,8, k = 11 ergibt 9,9, k = 15 ergibt 2,85 Grad.
- **Folgerung [ES]:** N = 12 ("11+1") ist die kleinste Kette, in der zwei Ecken fast auf derselben Seite liegen; erst
  bei N = 31 wird das besser. Das ist eine Eigenschaft der Helix-Geometrie (Zahlentheorie von arccos(-2/3)), keine
  Stabilitaet. Fuer N = 20 ("19+1") gibt es die Ausrichtung k = 19 (15,6 Grad), aber k = 11 bleibt besser.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K0-1 | theta = arccos(-2/3), Steighoehe 1/sqrt(10), Radius 3 sqrt(3)/10 auf 1e-9 | 95 % |
| K0-2 | Kleinster Azimutabstand (mod 360) springt bei N = 12 von 25,5 auf 9,9 Grad und erst bei N = 31 weiter (5,7). Bei N = 20 kein Sprung | 95 % |
| K1-1 | Kontrolle Codex: omega_1(12) = 0,300564, omega_1(20) = 0,134921 auf 1e-6; 6 Nullmoden fuer alle N | 95 % |
| K1-2 | log omega_1 glatt, 12 und 20 nicht auffaellig; Steigung d ln omega_1 / d ln N -> etwa -2 (Biegung) bei grossem N | 90 % / 70 % |
| K2-1 | Kontrolle Codex: mittleres P(12) = 10,219 +- 0,01, P(20) = 12,644 +- 0,015 | 90 % |
| K2-2 | P = T3 + 2 T4 + 2C in allen Stichproben (offene Kette) | 99 % |
| K2-3 | Mittel, Varianz und P(C > 1) glatt in N, 12 und 20 nicht auffaellig | 80 % |
| K3 | J_max (Mitte) ab N >= 10 auf 1 % konstant, 12 und 20 nicht auffaellig | 85 % |
| K4-1 | Die Helix bleibt unter Lennard-Jones fuer alle N ein lokales Minimum | 75 % |
| K4-2 | Ab N = 7 liegt sie deutlich ueber dem globalen Minimum, mit wachsendem Abstand; D2(E_kette) ohne Gipfel bei 12, 20 | 90 % |
| Gesamt | In den Stabilitaetsgroessen K1 bis K4 sind 12 und 20 nicht besonders. Besonders ist nur die Geometrie in K0 (11 Schritte ~ 4 Umlaeufe) | 80 % |

## Rahmen

- Code: tetrakette-1/code/tetrakette.py, von der Leitung geschrieben. Kernfunktionen aus stabil.py und stabil_s6.py
  (STABIL-6-8-12) werden uebernommen.
- Laeufe ueber kleintest.sh, je <= 10 min, ein Thread.
- Kontrollen:
  - Codex-Zahlen (K1-1, K2-1)
  - zwei MC-Seeds in K2
  - Zaehlidentitaet K2-2
  - Hesse-Matrix ueber zwei Schrittweiten in K4

## Nachtrag vor dem ersten Lauf (2026-10-02 09:37:15 CEST)

- Fuer J_max (Mitte) bekommt sigma einen Boden von 1e-6, weil die Bisektion nur auf etwa 6e-8 genau ist. Ohne Boden
  koennte reines Bisektionsrauschen ein N markieren. Fuer alle anderen Groessen bleibt es bei der robusten Streuung.
