# V-1-PRAEZISION: Ergebnis (Code-Agent, Runde 37, explorativ)

- Gerechnet vom Code-Agenten fuer die Leitung claude-primary auf der .69. Alle Laeufe ueber kleintest.sh, Spuren cpu3
  und cpu4, hoechstens zwei zugleich.
- Plan und Code eingefroren 2026-10-04 02:59:38 CEST (PLAN.md.eingefroren-20261004-025938,
  code/v1p.py.eingefroren-*, code/auswertung.py.eingefroren-*, sha256 in EINGEFROREN.sha256).
- Gewertete Laeufe 00:59:44 bis 01:11:29 UTC (02:59 bis 03:11 CEST), je Lauf 22 bis 82 s. Nach dem Einfrieren keine
  Code-Korrektur.
- Auswertung mechanisch mit code/auswertung.py (lauf-69/auswertung.json). Zusatz code/zusatz.py (beschreibend, nach dem
  Einfrieren geschrieben), Nachprobe L = 60/80 bei -1e-2.
- Geschrieben ab 2026-10-04 03:14:04 CEST (date).
- Kennzeichen: [M] Mathematik, [L] / [L?] Literatur aus dem Gedaechtnis (sicher / unsicher), [H] Hypothese, [F]
  Festlegung des Code-Agenten (vor dem Einfrieren).

## Ergebnis zuerst

1. **Das Leck ist jetzt bis 1e-49 aufgeloest, mit Reserve.**
   - Taylor-Reihen in Festkomma, 60 bzw. 40 Stellen, Kartenmodell (eps im Hintergrund und in den Schwankungen).
   - P(eps) reicht von 8,69e-17 (-1e-2) bis 1,55e-49 (-2e-3).
   - Zwei Genauigkeiten und zwei Schrittweiten stimmen in ln P auf mindestens 16 Stellen, zwei Gebietslaengen auf 12.
2. **Die einfache Formel mit 1/sqrt(abs(eps)) verfehlt die 1 % knapp: c = 6,149 statt 2 pi = 6,283 (q frei,
   PR1 nicht eingetroffen).**
   - Die Form selbst passt gut: Reste <= 0,022 in ln P ueber 75 Einheiten (PR3 eingetroffen).
3. **Mit der genauen Wellenzahl des Hauptkanals trifft der Polabstand pi auf 0,28 % (PR2 eingetroffen, knapp).**
   - Die gewertete Variante nimmt K_B, die Wellenzahl des neuen Aussenkanals B neu; Exponent ist dann -2 d K_B mit
     d = 3,1328, dazu q = -2,0.
   - Die Kartenformel woertlich gaebe -2,5 % (Festlegung im Plan, Vermerk unten).
   - Kanalweise, beschreibend: d = pi - 0,42 % (A neu) und -0,35 % (B neu), mit q = -1,7 bzw. -1,8. Der Schwanz des
     Hintergrunds selbst folgt exp(-d k0) mit d = pi + 0,21 %.
   - Der Faktor pi kommt damit an drei Groessen heraus, auf 0,2 bis 0,5 %.
4. **PR0 nicht eingetroffen, nur wegen des V-1-WEITER-Vergleichs.** P(-1e-2) = 8,687e-17 liegt 7,4 % unter dem gewerteten
   FD-Wert A (9,378e-17).
   - Gegen FD-Variante B (8,812e-17) sind es -1,4 %; A und B lagen schon in V-1-WEITER 6 % auseinander.
   - Im schwanzfreien Modell D trifft das Verfahren V-1-WEITER auf 1,8e-6.
   - Die Teile Genauigkeit (16 Stellen) und eps = +3e-3 (Leck 6,9e-115) sind klar bestanden.
5. **Bedeutung [H]:**
   - Das Leck ist im Exponenten verstanden: Polabstand pi mal doppelte Kanalwellenzahl, pro offenem neuen Kanal.
   - Die Kurzform exp(-2 pi/sqrt(abs(eps))) ist nur die fuehrende Naeherung. Im Bereich eps >= -1e-2 weicht der
     Hauptkanal B um 0,6 bis 3 % von 1/sqrt(abs(eps)) ab, das verschiebt c um 2 %.
   - Der Vorfaktor ist kein reines Potenzgesetz mit festem q: Je nach Exponentenform kommt q = -0,4 bis -2,0 heraus.
   - Fuer Papier I reicht die Aussage: Leck ~ abs(eps)^q exp(-2 pi K_kanal), K_kanal ~ 1/sqrt(abs(eps)).

## Urteile (mechanisch nach PLAN.md Abschnitt 6, lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Urteil | Werte |
|---|---|---|---|
| PR0 | Zwei Genauigkeiten in ln P auf 1e-6; -1e-2 trifft V-1-WEITER auf 5 %; +3e-3 Leck < 1e-60 | **nicht eingetroffen** | (a) ja: H und G gleich auf >= 16 Stellen; (b) nein: 8,6866e-17 gegen 9,3782e-17, -7,37 %; (c) ja: T_aus = 6,9e-115 (H), 2,1e-74 (G) |
| PR1 | Ausgleich q frei: c in 6,22 bis 6,35 | **nicht eingetroffen** | c = 6,1492, q = -0,389, sechs Punkte |
| PR2 | Mit genauem Kanal-k: d = pi auf 0,3 % | **eingetroffen** (knapp, Vermerk) | d = 3,13278, d/pi - 1 = -0,280 %, q = -2,005 (K = K_B) |
| PR3 | Reste des Ausgleichs mit q frei < 0,05 | **eingetroffen** | groesster Rest 0,0224 |

- **Vermerk PR0:**
  - Teil (b) haengt an der Referenzwahl [F, vor dem Einfrieren]: gewerteter V-1-WEITER-Wert A.
  - Die FD-Werte von V-1-WEITER enthalten randbedingte Schwanzwellen. Ende 47 gegen 90 aenderte dort P um 27 %, A gegen
    B um 6 %.
  - Mein Kartenhintergrund hat einen anderen, eindeutig festgelegten Schwanz (Plan Abschnitt 2). Der Vergleich prueft
    also auch die Schwanzwahl, nicht nur die Numerik.
  - Den numerischen Gleichwert zeigt Modell D (gleiches Modell in beiden Rechnungen): -1e-2 auf -1,8e-6, -1,5e-2
    (Rauchlauf r1) auf 1,9e-8.
- **Vermerk PR2:**
  - Das Urteil haengt an der Festlegung K = K_B (Plan Abschnitt 5, begruendet vor dem Einfrieren).
  - Andere k-Varianten, beschreibend (q frei):

| k-Variante | d/pi - 1 | q |
|---|---|---|
| Kartenformel woertlich | -2,54 % | +0,02 |
| Kartenformel mit berichtigtem Vorzeichen | -1,61 % | -0,88 |
| K_A | -2,17 % | -0,35 |

  - Die Marge ist klein (0,280 % gegen 0,3 %). Kanalweise liegen die Werte knapp ausserhalb: -0,35 % (B neu mit K_B),
    -0,42 % (A neu mit K_A).
  - Gesamt-P mit K_B ist eine Mischung zweier Exponenten. Die 0,28 % sind deshalb teils Mischungsglueck [H].
- **Vermerk PR1:** Der Kanal A neu allein ergibt mit 1/sqrt(abs(eps)) c = 6,259 (-0,38 %). Dort ist K_A ~ 1/sqrt(abs(eps)),
  weil mu_A = 0,18 klein ist.
  - Den Ausschlag gibt der Hauptkanal B neu: mu_B = -5,97, K_B liegt 0,6 % (-2e-3) bis 3,2 % (-1e-2) unter
    1/sqrt(abs(eps)).
- **Bedeutungszeile der Karte:** "PR1 und PR2 treffen ein" ist nicht ausgeloest.
  - Es greift "PR1 verfehlt ... Herleitung waere dann unvollstaendig".
  - Nach den Daten fehlt der Herleitung die genaue Kanalwellenzahl, keine naehere Singularitaet [H]. Der Polabstand pi
    selbst bestaetigt sich auf 0,2 bis 0,5 % (Zusatz).

## Tabelle P(eps): Kartenmodell, Hauptlauf H (200 bits, N = 64, Kh = 3,2, L = 70)

| eps | 1/sqrt(abs(eps)) | rho_z | P | ln P | Anteil B neu | K_B | K_A | Schwanz T |
|---|---|---|---|---|---|---|---|---|
| -1e-2 | 10,000 | 1,77349110030447 | 8,6866e-17 | -36,98216 | 87,4 % | 9,6761 | 10,0088 | 2,26e-13 |
| -7e-3 | 11,952 | 1,77347957609155 | 5,8802e-22 | -48,88529 | 82,8 % | 11,6884 | 11,9597 | 5,52e-16 |
| -5e-3 | 14,142 | 1,77347194891650 | 9,6406e-28 | -62,20640 | 78,7 % | 13,9228 | 14,1484 | 6,33e-19 |
| -4e-3 | 15,811 | 1,77346815181836 | 3,7211e-32 | -72,36869 | 76,2 % | 15,6168 | 15,8170 | 3,59e-21 |
| -3e-3 | 18,257 | 1,77346436562438 | 1,2356e-38 | -87,28668 | 73,2 % | 18,0902 | 18,2623 | 1,80e-24 |
| -2e-3 | 22,361 | 1,77346059026831 | 1,5486e-49 | -112,38934 | 69,4 % | 22,2252 | 22,3646 | 5,13e-30 |

- P = Flussanteil in A neu + B neu (aussen) bei Einfall mit Fluss 1 im alten Innenkanal e1, an der Nullstelle rho_z von
  E. Volle Stellen in lauf-69/K_H_*.json.
- P_neu_innen = P_neu_aus an allen sechs Punkten auf 15 Stellen (wie in V-1-WEITER bei -1e-2) [Beobachtung].
- Schwanz T: Amplitude der Mode e^{i k0 x} des Hintergrunds bei x = +70; k0 = 10,012 ... 22,366.
- Vergleich mit V-1-WEITER (FD, Ende 90): rho_z weicht um -7,4e-13 (-1e-2), +1,0e-12 (-7e-3), -2,7e-13 (-3e-3) ab.
- Bei -7e-3 hatte V-1-WEITER (Zusatz Z) 2,61e-21, das ist 4,4-fach ueber dem jetzigen Wert. Der dortige Verdacht auf
  ein Hintergrund-Artefakt bestaetigt sich.
- Die Hochrechnung von V-1-WEITER fuer -3e-3 (1e-39, Modell D) liegt 5,7-fach unter Modell D jetzt (5,74e-39) und
  12-fach unter dem Kartenmodell.

## Ausgleich (sechs aufgeloeste Punkte, ungewichtet in ln P)

| Form | Ergebnis | groesster Rest |
|---|---|---|
| F1: a + q ln abs(eps) - c/sqrt(abs(eps)) | c = 6,1492 (-2,13 %), q = -0,389, a = 22,706 | 0,0224 |
| F0: q = 0 | c = 6,0991 (-2,93 %) | 0,0415 |
| FK: a + q ln abs(eps) - 2 d K_B | d = 3,13278 (-0,280 %), q = -2,005 | 0,0063 |
| FK, q = 0 | d = 3,0053 (-4,34 %) | 0,184 |

- Reste F1 (von -1e-2 nach -2e-3): +0,014, -0,022, -0,008, +0,007, +0,019, -0,010.
  - Dasselbe Vorzeichenmuster zeigen alle Ausgleiche, auch die kanalweisen und Modell D, mit 0,002 bis 0,025.
  - Ursache offen [H]: denkbar sind Korrekturen hoeherer Ordnung im Vorfaktor oder eine schwache Schwebung.
- Ortliche Steigungen d ln P/d(1/sqrt(abs(eps))) zwischen Nachbarn: -6,097, -6,083, -6,088, -6,099, -6,118. Sie sind
  fast konstant, ein q aus ln abs(eps) ist in diesem Fenster schwach bestimmt.
- Bild: lauf-69/bild_lnP.svg.
  - Oben ln P gegen 1/sqrt(abs(eps)) mit F1: Kartenmodell gefuellt, Modell D offen.
  - Unten die Reste von F1 (Kreuz) und FK (Kreis).

## Kontrollen

- **Genauigkeit (H 200 bits gegen G 133 bits):** ln P an allen sechs Punkten in float64 identisch. Die vollen
  Zeichenketten weichen hoechstens in der 17. Stelle ab (-2e-3: 5e-17 relativ). rho_z gleich auf mindestens 30
  Stellen, also bis unter die Klammerbreite.
- **Schrittweite (S, Kh = 2,2 statt 3,2, 1,45-fach mehr Schritte):** ln P identisch auf alle 20 ausgegebenen Stellen.
- **Gebiet:**
  - L = 85 gegen 70 bei -2e-3: 7,3e-13 relativ in ln P, 8e-11 in P (Lauf R).
  - Nachprobe bei -1e-2 (nach der Auswertung, beschreibend): L = 60, 70, 80 geben ln P gleich auf 6,6e-18 relativ,
    obwohl der wachsende Anteil des Hintergrunds bei L = 80 schon 6,6e-6 erreicht.
- **Flussbilanz:**
  - H und S: abs(T + R - 1) <= 6,9e-57; G: <= 2e-37.
  - Taylor-Rest (letzte Koeffizienten) <= 1,5e-52.
- **Empfindlichkeit auf rho:** P(rho_z + 1e-8)/P(rho_z) - 1 = -1,5e-6 (-1e-2) bis -9e-7 (-2e-3). Die Klammer um rho_z
  ist <= 1,4e-27 breit.
- **eps = +3e-3 (Hintergrund f0, Plan Abschnitt 2):**
  - rho_z = 1,7735094593488634 (H und G gleich auf 39 Stellen).
  - T_aus(rho_z) = 6,9e-115 (H) bzw. 2,1e-74 (G).
  - Neue offene Kanaele gibt es dort nicht.
- **Gleichwert zu V-1-WEITER (Modell D, gleiche Definition):**
  - -1e-2: P = 4,747966e-17 gegen 4,747975e-17 (float64), -1,8e-6; rho_z gleich auf 1e-16.
  - -1,5e-2 (Rauchlauf r1, 100 bits): 1,9e-8.
- **Aufloesung (Plan Abschnitt 4):** Alle sechs Punkte sind aufgeloest.

## Zusatz (beschreibend, kein Urteil; code/zusatz.py, lauf-69/zusatz.json)

- **Kanalweise mit eigenem K (q frei):**

| Modell | Kanal | d | d/pi - 1 | q | groesster Rest |
|---|---|---|---|---|---|
| Karte | A neu (K_A) | 3,12840 | -0,42 % | -1,73 | 0,0045 |
| Karte | B neu (K_B) | 3,13058 | -0,35 % | -1,83 | 0,0056 |
| D (f0) | A neu | 3,12637 | -0,48 % | -1,65 | 0,0046 |
| D (f0) | B neu | 3,12169 | -0,63 % | -1,57 | 0,0075 |

  - Der Anteil von A neu waechst von 12,6 % (-1e-2) auf 30,6 % (-2e-3). Das passt zu exp(-2 pi (K_A - K_B)) mit fast
    festem Vorfaktorverhaeltnis.
- **Hintergrund-Schwanz (Kartenmodell):**
  - ln T = a + q ln abs(eps) - d k0 ergibt d = 3,14812 (+0,21 %), q = -0,35, groesster Rest 0,0006.
  - T e^{pi k0} = 10,3 ... 16,8.
  - Das ist eine zweite, unabhaengige Bestaetigung des Polabstands pi, hier fuer den nichtlinearen Hintergrund
    (Nanopteron) [L?].
- **Modell D (f0-Hintergrund, eps nur in den Schwankungen):**
  - P = 4,748e-17, 3,023e-22, 4,731e-28, 1,780e-32, 5,743e-39, 6,967e-50 (-1e-2 bis -2e-3).
  - F1: c = 6,1301, q = -0,122, groesster Rest 0,025.
  - Kartenmodell durch D: 1,83 (-1e-2) bis 2,22 (-2e-3), langsam wachsend.
  - Der eps-Anteil im Hintergrund aendert also den Vorfaktor um einen Faktor ~2, kaum den Exponenten.

## Latten (v3)

- **L1 (kann scheitern):** ja. PR0 und PR1 sind gescheitert, PR2 nur knapp bestanden.
- **L2 (Gegenprobe):** teilweise.
  - Anderer Integrator und anderes Zahlformat als V-1-WEITER, Gleichwert im Modell D auf 1,8e-6.
  - Polabstand pi an drei Groessen.
  - Kein zweites Haus.
- **L3 (Numerik):** ja. Zwei Genauigkeiten, zwei Schrittweiten, drei Gebietslaengen, Flussbilanz 1e-57, eps > 0 auf
  1e-115.
- **L4 (schon bekannt):** ja, im Prinzip.
  - Jenseits aller Ordnungen kleine Abstrahlung mit Faktor exp(-Polabstand mal Wellenzahl) ist Lehrbuchstoff:
    Pomeau/Ramani/Grammaticos zur KdV 5. Ordnung; Boyd, "Weakly Nonlocal Solitary Waves and Beyond-All-Orders
    Asymptotics" (1998) [L?].
  - Fuer die Q-Ball-Wand und die kanalweise Form nicht gesucht.
- **L5 (Messbezug):** nein. Rein modellintern.

## Selbstanzeigen

1. **Rauchlauf r3 (Kartenhintergrund bei +2e-3):**
   - Er blieb haengen: Die schnelle instabile Richtung e^{x/sqrt(eps)} liess die Festkomma-Zahlen ueberlaufen.
   - Ich habe ihn nach ~3 min gestoppt (eigene Unit, systemctl --user stop).
   - Folge, vor dem Einfrieren im Plan festgelegt: Die Kontrolle +3e-3 laeuft mit dem f0-Hintergrund. Ein
     Kartenhintergrund fuer eps > 0 in hoher Genauigkeit fehlt.
2. **PR2 nicht mit der Kartenformel ausgewertet:**
   - Gewertet ist K_B (Plan Abschnitt 5) statt der Formel der Karte.
   - Gruende: Die Formel hat ein Vorzeichen, das nicht zu omega^2 = 1 + k^2 + eps k^4 passt. Ausserdem setzt sie rho
     statt der Kanalfrequenz rho + om ein.
   - Woertlich gaebe sie -2,54 %, also "nicht eingetroffen".
   - Die Wahl stand vor dem Einfrieren fest. Sie stuetzt sich auf V-1-WEITER-Daten (Kanalanteile), nicht auf eigene
     Laeufe.
3. **Vorab-Auswertung:**
   - Um 03:07 bis 03:08 CEST liefen zusatz.py und auswertung.py, als die Kartenlaeufe fertig waren, Modell D und
     Kontrollen aber noch nicht (lauf-69/vorab/).
   - Ich kannte PR1 bis PR3 also vor den Kontrollen.
   - Danach wurde nichts an Code, Plan oder Regeln geaendert. Das Endergebnis ist mit der Vorab-Datei identisch, bis
     auf die damals fehlenden Teile.
4. **Nach dem Einfrieren hinzugekommen:**
   - zusatz.py (nur beschreibend)
   - die Nachprobe L = 60/80 bei -1e-2 (lauf-69/nach/)
5. **Bild:** Der Plan nannte F1 und FK im oberen Teil. Gezeichnet ist oben nur F1; FK erscheint nur ueber seine Reste
   (unten).
6. **Schwanzwahl ist Modellwahl [F]:**
   - Wie stark P von ihr abhaengt (etwa gegen einen zweiseitigen Schwanz), habe ich nicht gemessen.
   - Gemessen ist nur der Abstand zu Modell D (Faktor 1,8 bis 2,2), der auch den glatten eps-Anteil des Hintergrunds
     enthaelt.
7. **Eigene Rechenpanne beim Schreiben:**
   - Im ersten Entwurf dieser Datei stand, die Vorabschaetzung des Plans (Amplitude ~1e-25 bei -2e-3) habe um Faktor
     2,5 daneben gelegen.
   - Das war falsch gerechnet. Gemessen sind 1,08e-25 (B neu), die Schaetzung traf.
   - Beim Gegenlesen berichtigt, ebenso vier weitere Zahlen: oertliche Steigung -6,118 statt -6,105, K_B-Abstand
     3,2 statt 3,3 %, P_innen = P_aus auf 15 statt 16 Stellen, Gebietsprobe 12 statt 16 Stellen.

## Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-025938, EINGEFROREN.sha256
- code/:
  - v1p.py: Rechnung
  - auswertung.py: Urteile und Bild
  - zusatz.py: beschreibend
  - kette_a.sh, kette_b.sh: Laufketten
  - umgebung.py: Umgebungsprobe
- lauf-69/:
  - K_{H,G,S,R}_*.json/.log: Kartenmodell
  - D_{H,G}_*.json/.log: Modell D und eps = +3e-3
  - auswertung.json, zusatz.json, bild_lnP.svg
  - nach/: Nachprobe L = 60/80
  - vorab/: Vorab-Auswertung
- rauch-69/: r1 bis r4

## Einfach gesagt

Die Wand eines Q-Balls ist bei einer bestimmten Schwingung "still" und laesst dort keine Welle durch. Wirkt der Raum wie
ein feines Gitter, entsteht ein Schlupfloch fuer sehr kurze Wellen, und die Wand wird ein winziges bisschen undicht.
Dieses Leck haben wir jetzt mit 60 Stellen Genauigkeit nachgerechnet, bis hinunter zu Werten wie 10 hoch minus 49, und
alle Gegenproben stimmen auf viele Stellen ueberein. Die einfache Formel mit dem Faktor 2 pi passt nur auf etwa 2 %, weil
sie fuer den Hauptkanal des Lecks eine etwas zu grobe Wellenlaenge benutzt. Nimmt man die genaue Wellenlaenge dieses
Kanals, stimmt der Faktor pi, der aus der Form der Wand kommt, auf etwa 0,3 bis 0,5 %.
