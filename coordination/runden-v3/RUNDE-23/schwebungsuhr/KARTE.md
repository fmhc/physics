# SCHWEBUNGSUHR: Ist die Schwebung zweier Q-Baelle eine Uhr, und ziehen sich ihre Takte zusammen? (Runde 23)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 21:22:37 CEST (date), vor jedem Lauf und jedem Literaturabruf.
- Herkunft:
  - Finn 20:35: "ein mechanismus der in den teilen drin ist und die zeit entstehen laesst durch bewegungsdifferenz"
  - DUNKEL-ZEIT (R22): Die Phase eines einzelnen Q-Balls ist unbeobachtbar; erst die Schwebung zweier Baelle ist eine
    Uhr.
  - GEOMETRIE-STAND (R22): Ein Tick gehoert zur Atmungsmode bzw. zur Auslesung.
- Ableitbarkeitspruefung (Rohdatenprobe): Zwei Q-Baelle mit verschiedenem omega wurden im Projekt nicht gemeinsam
  zeitentwickelt. Codex' CLOCK-PAIR (R17) nutzte ein anderes Modell (Zweispinor-Hamilton). Die Ausgaenge sind nicht
  ablesbar.
  - Fuer schwach ueberlappende Schwaenze folgt die Schwebung mit |omega_1 - omega_2| aus der Ueberlagerung. Neu ist nur,
    was die nichtlineare Wechselwirkung daraus macht (Drift, Einrasten, Ladungsfluss).
- Explorativ (v3), Hypothesen [H]. Laeufe je <= 10 min.

## Test

- Modell M1 (U = S - S^2 + S^3/2), **1D** (schnell), Leapfrog mit Absorberrand.
- Zwei exakte 1D-Q-Baelle mit omega_1^2 = 0,60 und omega_2^2 = 0,65, ruhend, Mittenabstand D so, dass sich die Schwaenze
  schwach ueberlappen. D legt der Plan vorab fest; Vorschlag: Zentraldichte des Nachbarballs am eigenen Zentrum ~1e-3.
- Dazu der Abstand D' = D - 2 (staerkere Kopplung) und die Kontrolle omega_1 = omega_2 (gleiche Takte, Phasenlage 0
  und pi).
- Zeit bis T = 3000, zwei Gitter.
- Messgroessen:
  - Dichte am Mittelpunkt zwischen den Baellen (Schwebungsfrequenz per Matrix-Pencil in Fenstern)
  - Ladungen Q_1(t), Q_2(t) (Integral je Halbraum)
  - Schwerpunkte
  - die momentanen Frequenzen omega_1(t), omega_2(t) aus der Phase am jeweiligen Zentrum

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S0 | Kontrolle gleiche Takte, Phasenlage 0: Die Baelle ziehen sich an und verschmelzen bis T = 3000; Phasenlage pi: sie stossen sich ab | 70 % |
| S1 | Abstand D: Die Mittelpunktsdichte schwingt mit \|omega_1 - omega_2\| auf 1 %, in allen drei Zeitdritteln | 70 % |
| S2 | Abstand D: Netto-Ladungsfluss bis T = 3000 < 5 % von Q_1 (kein Auffressen); der Ladungsaustausch pendelt im Schwebungstakt | 50 % |
| S3 | Abstand D: Die Takte rasten nicht ein; \|omega_1 - omega_2\| aendert sich bis T = 3000 um < 10 % | 75 % |
| S4 | Abstand D' (staerker gekoppelt): \|omega_1 - omega_2\| aendert sich um >= 10 % (Ziehen bzw. Ansaetze zum Einrasten oder Auffressen) | 45 % |

**Bedeutung (vorab):**
- S1 und S3 treffen ein: Zwei Q-Baelle mit verschiedenem Takt bilden eine stabile Schwebungsuhr ohne
  Selbstsynchronisation; der Tick sitzt im Ueberlappgebiet zwischen ihnen [H, im Modell].
- S3 trifft nicht ein (Einrasten): Zwei Baelle gleichen ihre Zeit an, eine gemeinsame Zeit entsteht durch Kopplung [H].
- S2 trifft nicht ein: Der groessere frisst den kleineren; die Uhr laeuft ab.
- Literaturabgleich erst nach dem Lauf (Q-Ball-Wechselwirkung und Ladungstausch, z. B. Axenides u. a., Battye/Sutcliffe,
  Copeland/Saffin/Zhou) als L4-Latte.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren), je <= 10 min.
- Plan vor dem ersten echten Lauf einfrieren (Rauchlauf vorher erlaubt). Zeitbox 90 min.
