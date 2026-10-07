# ISO-ATEM-1: Kann Finns Tetraeder-Netz in alle Richtungen gleich atmen? (Runde 42)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 18:53:36 CEST (date), vor jeder Rechnung.
- **Herkunft:** Kartenvorschlag aus DREIECK-PUMPE-L (RUNDE-37/dreieck-pumpe-l/DOSSIER.md, Abschnitt 6). Modell, Teile
  A bis C, Messgroessen, Vorhersagen IA1 bis IA3 sowie Scheitern/Bestehen von dort sind **bindend und woertlich**.
  Zusaetze der Leitung sind als **[Zusatz Leitung]** markiert.
- **Finn (04.10.):** "kann daraus ein in der mitte gleich fließendes netz aus vielen dreiecken werden und somit ein teil
  was pumpt?" (18:08 bis 18:10). Dazu die atmenden Punkte (ATEM-NETZ-1, RAUTE-ATEM-1).
- **Frage:** Gibt es fuer starre regulaere Tetraeder (Kante 1 PU, eckenteilend in Finns Topologie, Kugelgelenke) in der
  periodischen kubischen Zelle mit 8 Tetraedern eine endliche Bewegung, bei der die Zelle kubisch bleibt und schrumpft
  (F = lambda I, lambda < 1)?
- Kennzeichen: [M] Mathematik, [E] Rechnung, [L] Literatur, [L?], [S], [H].

## Ableitbarkeitsprobe [Zusatz Leitung, vor jeder Rechnung]

- **Schritt 0, Literatur zuerst:**
  - Das P2_13-Modell von beta-Cristobalit (Tetraeder um ihre <111>-Achsen gedreht, kubisch) koennte genau eine solche
    Schar sein [L?].
  - Pruefen (hoechstens 2 gezielte arXiv-Abrufe bzw. Kristallographie-Literatur): Ist die P2_13-Drehung eine stetige
    Schar starrer Tetraeder mit schrumpfender kubischer Zelle?
  - Wenn ja, sind IA2 und IA3 vorab ableitbar. Dann als Kontrolle fuehren und nur die Zahlen rechnen: Volumen gegen
    Kippwinkel, Beruehrwinkel, Si-O-Si-Winkel.
- Teil A (Gegendrehung um [001], tetragonal) und "in der primitiven Zelle nur tetragonal" sind laut Dossier vorab
  ableitbar.
- Nicht ableitbar ist Teil C: weitere isotrope Mechanismen ohne Symmetrieansatz.

## Vorhersagen (woertlich aus dem Dossier, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IA1 | Kontrolle: Teil A exakt; der Gamma-Ansatz erreicht F = lambda I nie (Rest > 1e-3 bei lambda = 0,97) | 95 % |
| IA2 | [H] Fuer lambda = 0,97 gibt es eine Loesung mit Rest < 1e-10, also isotropes Atmen in der kubischen Zelle | 60 % |
| IA3 | [H] Die Loesung aus IA2 hat P2_13-Symmetrie (je Tetraeder eine eigene <111>-Achse) | 50 % |

**Bedeutung (vorab):**
- **IA2 trifft ein:** Finns Netz hat einen Gleichtakt-Atemkanal ohne Energie, der in alle Richtungen gleich wirkt. Das
  ist ein Anschluss an ATEM-NETZ-1 (atmende Punkte, Volumenatmen = Spin 0).
- **IA2 verfehlt:** Das Netz atmet in dieser Zelle nur flach (tetragonal) oder ungleich.

## Dimensionsvergleich (AGENTS.md)

- In 2D (Kagome) gibt es genau eine gleichfoermige Atemverformung; in 3D sind es drei Maxwell-Moden (Rocklin u. a.
  2017, laut Dossier).
- Die Frage hier ist, ob eine davon isotrop ist.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8 und cpu9, sobald WEYL-LINEAR-1 sie freigibt; sonst cpu2 oder
  cpu3. Je Lauf <= 10 min, 1 Thread. Zeitbox 75 min.
