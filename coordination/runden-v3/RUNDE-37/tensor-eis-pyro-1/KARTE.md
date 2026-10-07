# TENSOR-EIS-PYRO-1: Traegt Finns Tetraeder-Netz ein Tensor-Eis mit Gravitonen und Newton-Anziehung? (Runde 40)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 11:37:55 CEST (date), vor jeder
  Rechnung.
- **Anlass:**
  - TENSOR-EIS-N (RUNDE-36/tensor-eis-n/, kubisches Gitter nach Gu/Wen): Der N-Typ zieht gleiche Massen wie Newton an
    (U = -1/(8 pi r) auf 0,4 % ab r = 8), nur Helizitaet 2 bleibt mit positiver Energie; stabil nur mit strengen Regeln und
    exaktem Faktor 1/2 (Hořava lambda = 1, LAMBDA-1). Die Pyrochlor-Fassung (N4) wurde nicht gerechnet: "eigene
    Modellbildung" (PLAN [F5]).
  - Ueberleitung Ue2 (RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md): Ein Tetraeder hat 6 Kanten, ein symmetrischer 3D-Tensor 6
    Komponenten; die Paarprodukte der Tetraederrichtungen spannen die symmetrischen Tensoren auf. Tensor-Eis saesse also
    natuerlich auf den Kanten von Finns Tetraedern.
  - Finns Bild (RUNDE-34/tetra-konzept/ANALYSE.md): Einheiten fliessen "dadurch oder daran entlang".
- **Ableitbarkeitsprobe der Leitung (Schreibtisch, vor der Karte) [M, ungeprueft]:**
  - Pyrochlor-Netz je kubischer Elementarzelle des fcc-Gitters: 4 Ecken, 2 Tetraeder, 12 Kanten.
  - Platzierung A (Eichfreiheit xi an den Ecken, Kantenwert = Kantendehnung, wie linearisierter Regge): 12 Kanten gegen
    12 Eichfreiheitsgrade; das Pyrochlor-Stabnetz ist isostatisch (Maxwell, im Projekt bekannt: RUNDE-34/35). Dann
    bleiben eichinvariante Kantenkombinationen nur als Eigenspannungszustaende, vermutlich nur auf Linien im k-Raum: keine
    Gravitonen im Volumen [H].
  - Platzierung B (xi an den Tetraedermitten = Diamantplaetze, 6 je Zelle): 12 - 6 = 6 eichinvariante Groessen je Zelle,
    3 je Tetraeder wie im Kontinuum (6 - 3); mit der skalaren Regel blieben 2 Helizitaeten [H].
  - Diese Zaehlung ist der erste Schritt der Karte und kann sie schon am Schreibtisch beenden.
- **Projekt-grep:** TENSOR-EIS-0, TENSOR-EIS-N, LAMBDA-1, REGEL-1 (kubisch); GRAVITON-NETZ-L (Gu/Wen, Xu, Pretko);
  Pyrochlor-Stabnetz isostatisch (RUNDE-34/35, NETZ-C-1). Kein Tensor-Eis auf Pyrochlor gerechnet.
- Kennzeichen: [M] Mathematik, [L] Literatur, [H] Hypothese.

## Test (Code-Agent; Schreibtisch zuerst)

- **Schritt 1 (Schreibtisch, dann exakte Zaehlung im Code):** Fuer A und B den Rang des Eichoperators (diskretes
  symmetrisiertes Gradient) im k-Raum zaehlen; eichinvariante Moden je k; Linien oder Volumen? Calladine-Index
  pruefen. Steht fest, dass eine Platzierung keine Volumen-Gravitonen hat, wird sie nicht weiter gebaut.
- **Schritt 2 (nur fuer eine tragende Platzierung):** N-Typ-Modell nach Gu/Wen (Gl. 32 bzw. Nachbau in
  RUNDE-36/tensor-eis-n/code/tn.py) auf Finns Netz uebertragen: Vektorregel (Gauss je Eichplatz), skalare Regel
  (linearisierte Hamilton-Bedingung), Energie mit dem Spurglied -1/2. Begruendung jeder Gitterwahl im Plan.
- **Messgroessen:**
  - Spektrum im k-Raum: Zahl und Helizitaet der positiven Moden auf der eichfreien Zwangsflaeche, Tempo je Richtung.
  - statisches Potential zweier Punktmassen (Verletzung der skalaren Regel), Exponent und Richtungsstreuung, Torus
    korrigiert wie in TENSOR-EIS-N.
- **Kontrolle:** Der kubische Nachbau aus TENSOR-EIS-N laeuft mit demselben neuen Code und trifft dort -1/(8 pi r).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TE0 | Kontrolle: kubischer Nachbau trifft U = -1/(8 pi r) auf 1 % ab r = 8 | 85 % |
| TE1 | [H] Platzierung A (Ecken) hat keine eichinvarianten Volumenmoden (nur Linien oder Punkte im k-Raum) | 65 % |
| TE2 | [H] Platzierung B (Tetraedermitten) traegt auf der Zwangsflaeche genau zwei positive Moden mit Helizitaet +-2 und linearer Dispersion | 40 % |
| TE3 | [H] Newton-Anziehung auf Finns Netz: Exponent 1 +- 0,02 ab r = 4 und Richtungsstreuung des Vorfaktors <= 3 % | 30 % |

**Bedeutung (vorab):**
- **TE1 trifft ein:** Kantendehnungen auf dem Eck-Netz sind fast nur Eichung; die Regge-Lesart von Finns Netz (Kanten =
  Laengen) traegt dort keine Gravitonen.
- **TE2 und TE3 treffen ein:** Finns Netz traegt ein Tensor-Eis mit Gravitonen und Newton-Anziehung, wenn die
  Eichfreiheit in den Tetraedermitten sitzt (Lesart "dadurch") [H].
- **TE2 verfehlt:** Auf Finns Netz braucht Tensor-Eis eine andere Verteilung der Freiheitsgrade als "ein Wert je Kante".

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (CPU-Skripte erlaubt); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 150 min.
