# LEITER-2D: naechste Sprossen der 2D-Leiter blind vorhersagen und rechnen (Runde 11)

- Leitung: claude-primary. Karte geschrieben ab 2026-09-30 12:35:34 CEST (date), vor jedem Lauf.
- Herkunft: Ideen-Evolution G2-10 (Ernte: "Leiter in 2D auf dem Raster gesehen ... nächste Sprosse unter 0,535 blind
  vorhersagen"). Gerechnet sind dort n = 1 bis 5 (leiter-2, verfeinert, L3 bestanden). Die Werte n >= 6 liegen unter
  dem damaligen Raster (0,535 bis 0,699) und sind nicht gerechnet.

## Bekannt (GEN-02/G2-10/lauf-69-kopie/lauf-69/leiter-2/leiter.json)

| n | omega^2 | eps = omega^2 - 1/2 | 1/eps | Schritt in 1/eps | rho |
|---|---|---|---|---|---|
| 1 | 0,6536181 | 0,1536181 | 6,50965 | | 1,61008 |
| 2 | 0,5903511 | 0,0903511 | 11,06794 | 4,558 | 1,60186 |
| 3 | 0,5637612 | 0,0637612 | 15,68350 | 4,616 | 1,58588 |
| 4 | 0,5492521 | 0,0492521 | 20,30371 | 4,620 | 1,57462 |
| 5 | 0,5401206 | 0,0401206 | 24,92483 | 4,621 | 1,56670 |

- Duennwandgrenze omega_c^2 = min U/S = 1 - 1/(4 beta) = 1/2 bei beta = 1/2, in jeder Dimension.
- Duennwandradius R ~ (d - 1)/eps: In 2D braucht eine zusaetzliche halbe Welle den doppelten Schritt in 1/eps wie in
  3D. Gemessen: 3D-Grenzschritt etwa 2,305 (RUNDE-09), 2D 4,62; Verhaeltnis 0,499.

## Vorhersage (vor jedem Lauf, Zeit siehe Kopf)

Regel: gleicher Schritt in 1/eps wie zuletzt, 4,621 (die Schritte konvergieren: 4,558, 4,616, 4,620, 4,621).

- **V1 Lagen:**
  - n = 6: 1/eps = 29,546, omega^2 = 0,53385 +- 0,0001
  - n = 7: 1/eps = 34,167, omega^2 = 0,52927 +- 0,0002
  - n = 8: 1/eps = 38,788, omega^2 = 0,52578 +- 0,0003
  - Die Baender entsprechen einer Unsicherheit des Schritts von +-0,03 bis +-0,1, erweitert um die Verfeinerungsgenauigkeit.
- **V2:** Die gemessenen Schritte n5 -> n6 und n6 -> n7 liegen in [4,59; 4,65].
- **V3:** rho faellt weiter und langsamer: rho_6 = 1,5612 +- 0,003, rho_7 = 1,5573 +- 0,004.
- **V4:** An jeder gefundenen Stelle ist |Gamma| unter 1e-6 (unter der Aufloesung, nur obere Schranke).

## Scheiterregel

- **Verfehlt:** Auf dem Raster 0,523 bis 0,537 (Schritt 0,002) liegt keine Stelle innerhalb +-0,0005 von 0,53385 oder
  von 0,52927.
- Liegen Stellen dort, aber ausserhalb der Baender von V1: V1 verfehlt, die Leiter selbst ist gesehen.
- Gar keine Stelle im Bereich: "auf dem Raster nicht gesehen". Dann ist erst die Verfeinerung zu pruefen, bevor etwas
  geschlossen wird.

## Test

- Code: bic2_2d.py aus G2-10 (unveraendert; Kopie nach runde11-leiter2d/ auf der .69, sha256 vorher und nachher).
- Aufrufe `kurve --dim 2 --beta 0.5 --h 0.02 --n-wechsel-fein 2`, Raster 0,002, benachbarte Stuecke teilen einen
  Randwert:
  - a: 0,533, 0,535, 0,537
  - b: 0,527, 0,529, 0,531, 0,533
  - c: 0,523, 0,525, 0,527
- Spuren cpu, cpu2, cpu6 (je ein Kern), je Aufruf unter 10 min (G2-10: 7 Werte in 348 s).
- Danach `leiter` nur zur Auswertung, falls noetig; L3 (h = 0,01) je gefundene Stelle als zweiter Schritt.

## Ergebnis, erster Teil (Leitung, eingetragen 12:39:59; Laeufe .69 12:36:05 bis 12:38:49, alle rc = 0)

- **n = 6 gefunden:** Vorzeichenwechsel von s zwischen 0,533 und 0,535, verfeinert (4 Stufen) auf
  omega^2* = 0,5338453, rho* = 1,560885, Pol-Imaginaerteil 5,0e-9 (unter der Aufloesung, nur obere Schranke). Lauf a,
  160,9 s.
  - V1 fuer n = 6: getroffen (vorhergesagt 0,53385 +- 0,0001; Abstand 4,7e-6).
  - V2: Schritt n5 -> n6 in 1/eps = 29,5463 - 24,9248 = 4,6215, getroffen ([4,59; 4,65]).
  - V3 fuer n = 6: getroffen (vorhergesagt 1,5612 +- 0,003; gemessen 1,56089).
  - V4 fuer n = 6: getroffen.
- **n = 7 und n = 8 auf dem Raster 0,002 nicht gesehen** (Laeufe b und c, 84,5 s und 71,7 s): Auf dem verfolgten Ast
  bleibt s von 0,523 bis 0,533 negativ (-6e-5 bis -3,9e-4).
  - Auffaellig: Der Kernzuwachs steigt von 1,2e5 (Lauf a) auf 2,9e6 (Lauf b). Die Box ist R = 32,4 statt 30,1, r_m = 12,0
    statt 9,9. Die Pol-Breiten springen zwischen Nachbarpunkten (2,3e-4 bis 6,6e-3).
  - Nach der Scheiterregel: nicht "verfehlt" (eine Stelle liegt im Band von n = 6). Fuer n = 7 und n = 8 gilt erst die
    Verfeinerung.
- **Verfeinerung, festgelegt vor dem Lauf (12:39:59):**
  - d: 0,5285, 0,5290, 0,5295, 0,5300 bei h = 0,02
  - e: dieselben Werte bei h = 0,01
  - f: 0,5255, 0,5260 bei h = 0,02 (n = 8)
  - Gilt als gesehen, wenn s auf dem Ast das Vorzeichen wechselt und die Verfeinerung konvergiert wie bei n = 6.

## Ergebnis, zweiter Teil (Leitung, eingetragen 12:43:33; Laeufe d, e, f 12:40:14 bis 12:42:58, alle rc = 0)

Dateien lokal: lauf-69/{a..f}/kurve.json (sha256 a cab9e096..., b 825725af..., c d5082a39..., d 2c99a0e1..., e 6d488c04...,
f f8ab6f3b...), LAUF-L2D-*.log, start.sh, start2.sh. Code bic2_2d.py unveraendert (e5f035c994922d35).

- **d (h = 0,02) und e (h = 0,01), 0,5285 bis 0,5300 in Schritten 0,0005:** kein Vorzeichenwechsel von s.
  - s = -7,0e-5 / -8,8e-5 / -1,13e-4 / -1,41e-4, monoton. Beide Schrittweiten stimmen auf 3 bis 4 Stellen ueberein,
    die Diskretisierung ist also nicht die Ursache.
  - Die Polbreite hat auf dem Raster ein Minimum bei 0,5295 (1,75e-4; bei 0,5290 2,34e-4; an den Raendern 1,6e-3 bis
    2,0e-3), wird aber nicht klein wie bei n = 6 (5e-9).
- **f (0,5255, 0,5260):** kein Vorzeichenwechsel (s = -3,1e-5, -5,9e-5; Polbreite 4,2e-4, 2,5e-4).
- Zusammen mit a bis c: Auf dem einzigen Ast (ein Kandidat je omega^2) bleibt s von 0,523 bis 0,5338 negativ. Unterhalb
  von n = 6 ist auf dem Raster **keine weitere stille Stelle gesehen**. Die Leiter der Stellen mit s-Wechsel endet auf
  diesem Raster bei n = 6.
- Kernzuwachs 1,2e5 (a) bis 1,8e7 (f): Er waechst zur Duennwandgrenze hin (etwa e^{kappa R}). Das ist ein moeglicher
  Genauigkeitsverlust, den dieser Code nicht selbst prueft. Die Uebereinstimmung h = 0,02 gegen 0,01 schliesst ihn nicht
  aus.

## Vorhersage gegen Ausgang

| Vorab | Ausgang |
|---|---|
| V1 n = 6 bei 0,53385 +- 0,0001 | getroffen (0,5338453) |
| V1 n = 7 bei 0,52927 +- 0,0002 | nicht gesehen (Raster 0,0005 und 0,002, h = 0,02 und 0,01); kleinste Polbreite 1,75e-4 bei 0,5295 |
| V1 n = 8 bei 0,52578 +- 0,0003 | nicht gesehen (Raster 0,0005 und 0,002) |
| V2 Schritt n5 -> n6 in [4,59; 4,65] | getroffen (4,6215); n6 -> n7 entfaellt |
| V3 rho_6 = 1,5612 +- 0,003 | getroffen (1,56089) |
| V4 Polbreite < 1e-6 | getroffen fuer n = 6 |

- Scheiterregel: nicht "verfehlt", denn n = 6 liegt im Band.
- **Befund [H, Modell]:** In 2D sind n = 1 bis 6 stille Stellen. Bei n = 7 und 8 bleibt nur eine schmale Resonanz mit
  endlicher kleinster Breite (auf dem Raster etwa 2e-4) uebrig, kein Nulldurchgang.
  - Anders als in 3D, wo die Leiter bis n = 15 blind getroffen wurde.
  - Zwei Lesarten, nicht entschieden: (a) Die 2D-Leiter bricht ab und geht in Quasi-BIC ueber. (b) Der Code verliert an
    der Duennwandgrenze Genauigkeit (Kernzuwachs bis 1,8e7).
  - Unterscheidungstest: dieselben omega^2 mit hoeherer Rechengenauigkeit (Kugelarithmetik wie im Beweiskern oder
    mpmath) oder mit anderem Anschlussradius r_m. Bleibt s negativ und die Breite endlich, gilt (a).
