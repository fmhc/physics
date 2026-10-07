# REGGE-KINETIK-L: Wie behandelt die Literatur die Bewegungsenergie (simpliziale Supermetrik), die Eich-Reduktion und das Umklappen im kanonischen Regge-Kalkuel? (Runde 48, Literatur zu HODGE-MASSE-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 09:34:14 CEST (date), vor jedem Abruf.
- **Anlass [P]:** Drei Projektbefunde zeigen auf die Bewegungsenergie bzw. die Eich-Reduktion:
  - Leckage (IMPULS-NETZ-1, SKALAR-SEKTOR-L)
  - TT-Anisotropie (TT-GLAS-2, unprojiziert 0,00 %)
  - Energiesprung beim Delaunay-Zug (TAKT-DYNAMIK-1)
  - HODGE-MASSE-1 rechnet das gerade. Diese Karte liefert die Literatur dazu, ohne zu rechnen.
- **Projektsuche (09:34, alle Dateitypen, Ausschluesse):**
  - Rocek/Williams 1981 (linearisiertes Regge gibt linearisierte ART) [P, GRAVITON-NETZ-L]
  - Hoehn 2014 (Pachner-Zuege als Zeitentwicklung) und Bahr/Dittrich (Symmetriebruch ausser nahe flach) [P, R41]
  - Die Bewegungsenergie je Tetraeder ist im Projektcode eine DeWitt-Form [P, IMPULS-NETZ-1].
  - Simpliziale Supermetrik, 3+1-Regge (Piran/Williams, Friedman/Jack) und die Behandlung der Eckverschiebungs-Eichung im Hamilton-Bild sind im Projekt nicht gelesen.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Fragen

1. **Simpliziale Supermetrik:** Was ist sie, wer hat sie eingefuehrt (Lund/Regge; Hartle/Miller/Williams 1997), welche Signatur hat sie, und ist sie volumengewichtet?
2. **3+1-Regge:** Wie behandeln Piran/Williams 1986, Friedman/Jack 1986 und Nachfolger Lapse und Shift je Ecke? Bleiben Impuls- und Hamilton-Bedingungen erhalten?
3. **Eich-Reduktion:** Gibt es in der Literatur eine ausdrueckliche (horizontale bzw. symplektische) Reduktion der Eckverschiebungs-Eichung im linearisierten Regge? Ist dort gezeigt, dass das Spektrum von der Eichflaeche unabhaengig ist?
4. **Umklappen:** Was sagt die kanonische simpliziale Gravitation mit sich aendernden Gittern (Dittrich/Hoehn 2012, 2013; Hoehn 2014) zur Erhaltung von Symplektik und Energie bei 2-3-, 3-2- und 1-4-Zuegen?
5. **TT-Isotropie:** Ist die Isotropie der langen Gravitonwellen auf unregelmaessigen Regge-Gittern irgendwo untersucht?

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:** Bei gleichmaessiger Verzerrungsrate ist die volumengewichtete DeWitt-Form auf jedem Netz der Kontinuumswert (HODGE-MASSE-1, HM0). Die Literaturfragen beruehren das nicht.
- **Nicht ableitbar:** alle fuenf Fragen, reiner Literaturstand.

## Vorhersagen (vor jedem Abruf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RK1 | [L?] Die simpliziale Supermetrik ist die volumengewichtete DeWitt-Metrik auf den Kantenlaengen; ihre negativen Richtungen haengen an konformen Moden, etwa eine je Ecke | 55 % |
| RK2 | [L?] Im 3+1-Regge bleiben Impuls- und Hamilton-Bedingungen nicht exakt erhalten bzw. brauchen Abaenderungen (Friedman/Jack: erhaltene Impulsbedingung) | 60 % |
| RK3 | [L?] Die kanonische simpliziale Gravitation mit sich aendernden Gittern erhaelt die Symplektik ueber Pachner-Zuege; 1-4-Zuege bringen neue Zwangsbedingungen bzw. Eichfreiheit | 65 % |
| RK4 | [H] Eine ausdrueckliche horizontale Reduktion der Eckverschiebungs-Eichung mit Nachweis der Eichflaechen-Unabhaengigkeit des Spektrums steht in der Literatur | 40 % |
| RK5 | [H] Die Isotropie langer Gravitonwellen auf unregelmaessigen Regge-Gittern ist untersucht | 35 % |

**Bedeutung (vorab):**
- **RK1 und RK4 treffen ein:** HODGE-MASSE-1 kann sich auf eine Standardform stuetzen. Abweichungen unseres Codes davon waeren dann zu berichtigen.
- **RK3 trifft ein:** Fuer Finns Umklappen gibt es einen Rahmen, der die Symplektik erhaelt. Der Energiesprung aus TAKT-DYNAMIK-1 waere dann ein Fehler unserer Zustandsabbildung, nicht des Umklappens.
- **RK5 verfehlt:** Die TT-Isotropie auf Zufallsnetzen ist ein eigener Projektbeitrag. Das gilt als Hypothese, bis eine Suche ueber 24 Monate leer bleibt.

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 15 Netzabrufe; WebSearch, arXiv, INSPIRE, OpenAlex, freie Verlagsseiten.
- Schreibt nur in RUNDE-37/regge-kinetik-l/.
- Literatur, keine Rechnung.
