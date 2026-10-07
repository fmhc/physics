# TETRAKETTE-1: Ergebnis (Leitung, geschrieben ab 2026-10-02 09:40:49 CEST)

Karte: KARTE.md (09:34:03, Nachtrag Bisektionsboden vor dem Lauf). Gerechnet von der Leitung auf der .69 (kleintest.sh,
cpu und cpu2), Laeufe 09:37:21 bis 09:39:46, alle rc = 0.
- Code: code/tetrakette.py, mit Kernfunktionen aus STABIL-6-8-12.
- Daten: aus/.

## Ergebnis zuerst

1. **In den Stabilitaetsgroessen sind 12 ("11+1") und 20 ("19+1") Ecken nicht besonders.** Gemessen wurden:
   - Federsteifigkeit
   - Feldklumpen
   - Lennard-Jones-Bindung
   - Schnittstatistik

   20 ist in keiner Groesse markiert. 12 ist in vier von sieben Groessen markiert, aber nie allein, sondern stets mit
   dem ganzen Kurzkettenbereich (8 bis 14). Dort dominieren die Kettenenden. Die vorab festgelegte Streuung kam aus dem
   glatten Langkettenbereich und war fuer kurze Ketten untauglich (Selbstanzeige).
2. **Besonders an der 12 ist die Geometrie:**
   - Die Helix dreht je Ecke um genau arccos(-2/3) = 131,8103 Grad (gerechnet auf 1e-13).
   - 11 Schritte sind fast genau 4 Umlaeufe (Kettenbruch 4/11). Darum liegen bei 12 Ecken erstmals zwei Ecken fast auf
     derselben Seite, 9,9 Grad versetzt; vorher waren es mindestens 25,5 Grad. Besser wird es erst bei 31 Ecken (5,7
     Grad).
   - Fuer 20 Ecken gibt es die Naeherung 7/19 (15,6 Grad); sie ist schlechter als 4/11 und bringt keinen Sprung.
3. **Nachtraegliche Beobachtung [H, post hoc]:** Die zwei tiefsten Biegeschwingungen fallen fast zusammen bei 9, 12
   und 15/16 Ecken (Verhaeltnis 0,99 / 0,97 / 0,98). Das sind genau die Laengen, ab denen neue Fast-Ausrichtungen moeglich
   werden (k = 8, 11, 15). Die Geometrie hinterlaesst also eine schwache mechanische Spur. Die 12 ist dabei nicht
   einmalig.
4. **Kontrollen:** Codex wurde zweimal von einem anderen Haus reproduziert.
   - Kleinste Federfrequenz 0,300563645588 / 0,134921087613 fuer 12 / 20 Ecken, auf 1e-12.
   - Mittleres P = 10,216 / 12,648 gegen Codex' exakte Zellwerte 10,2187 / 12,6444.
   - Die Zaehlregel P = T3 + 2T4 + 2C gilt in allen 2 x 200 000 x 30 Stichproben.
5. **Unter Lennard-Jones bleibt die Kette fuer alle N = 4 bis 33 ein lokales Minimum.** Sie liegt aber weit ueber dem
   kompakten Cluster, 6,2 bei N = 12 und 19,3 bei N = 20. Frei bewegliche, sich anziehende Teilchen wuerden sich also
   zu einem Ikosaeder-Haufen zusammenballen, nicht zur Kette.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| K0-1 | theta, Steighoehe, Radius auf 1e-9 (95 %) | **eingetroffen**: theta = 131,81031489577862 Grad = arccos(-2/3), Steighoehe 0,316227766 = 1/sqrt(10), Radius 0,519615242 = 3 sqrt(3)/10 (Streuung 3e-15) |
| K0-2 | Azimutabstand springt bei N = 12 auf 9,9 Grad, erst bei 31 weiter, bei 20 kein Sprung (95 %) | **eingetroffen**: N 4-8: 35,43 Grad; 9-11: 25,52; 12-30: 9,91; ab 31: 5,69. Modulo 180 Grad: Spruenge bei 5 (12,76), **12 (9,91)** und 16 (2,85) |
| K1-1 | Codex' omega_1 auf 1e-6, 6 Nullmoden (95 %) | **eingetroffen** auf 1e-12; 6 Nullmoden fuer alle N |
| K1-2 | log omega_1 glatt, 12 und 20 unauffaellig (90 %); Steigung -> etwa -2 (70 %) | **nicht eingetroffen** fuer 12: markiert mit 8-11, z = -7,9 / +13,9 / +4,4 / -9,0 / **+4,7** fuer N = 8..12. 20 unauffaellig (z = 0,6). Steigung -1,78 (N 20-27) bzw. -1,86 (27-33), naehert sich -2: **eingetroffen** |
| K2-1 | P(12) = 10,219 +- 0,01, P(20) = 12,644 +- 0,015 (90 %) | **eingetroffen**: 10,2163 und 12,6482 |
| K2-2 | Zaehlidentitaet in allen Stichproben (99 %) | **eingetroffen**: 0 Verletzungen |
| K2-3 | Mittel, Varianz, P(C > 1) glatt, 12 und 20 unauffaellig (80 %) | **eingetroffen** fuer 12 und 20 (z = 1,2 / -1,0 im Mittel). Einzige Markierung: N = 10 im Mittel (z = -3,2) |
| K3 | J_max (Mitte) ab N >= 10 auf 1 % konstant, 12 und 20 unauffaellig (85 %) | **nicht eingetroffen**: J_max(Mitte) waechst von 0,0350 (N = 10) auf 0,04284 und ist erst ab N ~ 16 auf 1 % konstant. Es wechselt gerade/ungerade, markiert sind 8-14 und 16. 20 unauffaellig. J_max(Ende) ist ab N = 12 konstant (0,039351) |
| K4-1 | Helix bleibt LJ-Minimum fuer alle N (75 %) | **eingetroffen**, siehe Selbstanzeige zur Hesse-Schrittweite. Kleinster positiver Eigenwert 0,148 bei N = 33 |
| K4-2 | Abstand zum globalen Minimum waechst; D2(E_kette) ohne Gipfel bei 12 und 20 (90 %) | **eingetroffen**: Abstand 0 (N = 4, 5), 0,41 (6), 0,97 (7), 6,16 (12), 19,27 (20), 28,15 (25). D2 faellt monoton ohne Gipfel; formal markiert ist 9-16 (Kurzkettenbereich) |
| Gesamt | 12 und 20 in K1-K4 nicht besonders, besonders nur die Geometrie (80 %) | **im Kern eingetroffen, formal nicht**: 20 nirgends markiert; 12 nur im Verbund 8-14. Dazu die nachtraegliche mechanische Spur der Geometrie (Punkt 3) |

## Selbstanzeigen

- **Das Kriterium "auffaellig" war fuer kurze Ketten untauglich.**
  - sigma stammt aus N = 8..29; der glatte Langkettenbereich drueckt es klein, und die Endeffekte bei kurzen Ketten
    werden markiert.
  - v2.1 selbst empfiehlt, Regimegrenzen vorher auszuschliessen; das habe ich nicht getan.
  - Ein faires Mass waere z. B. der Vergleich nur mit den unmittelbaren Nachbarn nach Abzug eines Endterms ~ 1/N. Das
    waere jetzt post hoc und ist nicht gemacht.
- **Hesse-Matrix unter LJ mit h = 1e-4:** Sie zeigt bei allen N 1 bis 3 "negative" Eigenwerte um -5e-6.
  - Das sind die 6 Starrkoerper-Nullmoden mit Differenzenfehler: negativ + null = 6 in beiden Schrittweiten. Bei
    h = 1e-5 sinkt der Wert auf ~ -5e-8, also wie h^2.
  - Die vorab gesetzte Schwelle 1e-6 war fuer h = 1e-4 zu eng. Die Wertung stuetzt sich auf h = 1e-5 und die
    h^2-Skalierung.
- **Unnoetiger Interpreterstart:** Waehrend des Laufs habe ich auf der .69 einmal python ausserhalb von kleintest
  gestartet, als wirkungsloses print(). Es hat nichts gerechnet.
- Codex' Code wurde nicht gelesen, nur seine Zahlen (TETRA-RECON-1, TETRA-FOLLOWUP).
- Literatur: Die Helixwerte waren vorab [L?] und sind jetzt nachgerechnet. Das ist keine Quellenlesung.

## Pruefsummen und Zeiten

- Code tetrakette.py: 785ba071.
- schnell.json: 52d61fd8.
- schnitte-31.json: ca6746f9.
- schnitte-32.json: 7d0d6a35.
- auswertung.json: f9b7366f.
- Laufzeiten: schnell 137 s, Schnitte je 3,7 s, Auswertung < 1 s.

## Einfach gesagt

Wir haben die Kette aus Tetraedern mit 12 und mit 20 Ecken nachgebaut und mit allen ihren Nachbarlaengen verglichen:
Wie steif sie ist, wie gut sie Feldklumpen haelt, wie fest sie unter Anziehung zusammenhaelt und wie oft eine Ebene sie
schneidet. Dabei ist die 12 nicht stabiler als 11 oder 13 und die 20 nicht stabiler als 19 oder 21. Besonders an der 12
ist nur etwas Geometrisches: Die Kette dreht sich wie eine Wendeltreppe, und nach 11 Stufen steht man fast genau ueber
dem Anfang. Das passiert vorher nie so genau.

## Berichtigung (Leitung, 2026-10-02 10:00:38 CEST, nach der dritten frischen Lesung von v2.2, Auflage G1)

- Der Satz "In den Stabilitaetsgroessen sind 12 und 20 Ecken nicht besonders" (Ergebnis zuerst, Punkt 1) ist fuer 12 zu
  stark. Fuer 20 gilt er.
- Fuer 12 ist richtig: Die vorab festgelegte Vorhersage K1-2 und das Gesamt-Urteil sind formal nicht eingetroffen. Der
  Test markiert 12 in vier von sieben Groessen, kann 12 aber nicht von seinen kurzen Nachbarn trennen.
- Die Erklaerung "Endeffekte" ist nicht geprueft; ein fairer Vergleich mit abgezogenem Endterm fehlt.
- **Fuer 12 also: mit diesem Test nicht entscheidbar.**
- Nachtraeglich [post hoc, beschreibend]: In keiner der markierten Groessen ist 12 der staerkste Ausreisser des Bereichs
  8-14.
  - log omega_1: 9 (+13,9), 11 (-9,0), 8 (-7,9) gegen 12 (+4,7)
  - J_max: 8 (-102), 9 (+84), 11 (+69) gegen 12 (-11)
  - E/N und D2 fallen monoton
