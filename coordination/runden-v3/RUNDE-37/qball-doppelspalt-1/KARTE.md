# QBALL-DOPPELSPALT-1: Erzeugt ein klassischer 2D-Q-Ball am Doppel- bzw. Dreifachspalt eine strukturierte Ablenkungsstatistik, und folgt sie seiner inneren Uhr oder der Geometrie? (Runde 45/46, Finn-Auftrag Doppelspalt, Q-Ball nur als Teilchenmodell)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 05:35:29 CEST (date), vor jeder Rechnung.
- **Finn (05.10.):** "Wir brauchen alternative Ideen zum Doppelspaltexperiment"; Q-Baelle "Nur fürs Teilchenmodell".
- **Herkunft:** Kartenvorschlag aus DOPPELSPALT-L (RUNDE-37/doppelspalt-l/DOSSIER.md, Abschnitt 7). Frage, Aufbau, Vorhersagen V-Q1 bis V-Q4, Bedeutung, Budget, Konvergenzbindung und Abbruch sind **woertlich bindend**; die Wahrscheinlichkeiten setzt die Leitung. Zusaetze der Leitung sind markiert.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Frage (woertlich)

- Erzeugt ein klassischer 2D-Q-Ball des Projektmodells (beta = 1/2) am Doppel- bzw. Dreifachspalt eine strukturierte Ablenkungsstatistik?
- Wenn ja: Folgt die Struktur der inneren Phase (lambda_omega ~ 1/(gamma v)) oder der Geometrie?
- Wie gross ist I3?

## Pflicht vor dem Start (woertlich, dazu Zusatz)

- (a) arXiv:1508.06837 an der Quelle lesen: Was ist dort schon gerechnet? Erst danach den Plan schreiben. Ist der Kern dort schon gerechnet, zuerst an die Leitung melden.
- (b) Projekt-grep, von der Leitung um 05:35 erledigt: kein Q-Ball- bzw. Soliton-Spalt im Projekt. Treffer zu "Spaltung" betreffen Q-Ball-Zerfall in 1D (RUNDE-04/chemie-bio).
- (c) Den Ausgangszustand je Gitter pruefen: Q-Ball-Profil, Ruhetest ohne Spalt, Ladung und Energie erhalten.
- **[Zusatz Leitung] (d) Energiebilanz als Pflichtzeile (Gedaechtnis QBALL-DREIPOL):**
  - Vor den Laeufen aus der Projekt-Kurve E(Q) die Spaltkosten E(Q_1) + E(Q_2) - E(Q) fuer Stuecke von je >= 10 % Q berechnen.
  - Mit der kinetischen Energie bei v = 0,2 / 0,3 / 0,45 vergleichen.
  - Reicht sie nie, ist V-Q4 vorab entschieden ("verfehlt"). Das steht dann im Plan, nicht erst im Ergebnis.
- **[Zusatz Leitung] (e) Ableitbarkeit:**
  - V-Q1 ist nahezu ableitbar (Lokalitaet: Schwanz ~ e^(-kappa d') am fernen Spalt) und gilt als Kontrolle.
  - Bei V-Q2 ist nur die Skalierung ableitbar, falls die Struktur phasengetrieben ist. Ob es sie gibt, ist nicht ableitbar.
  - V-Q3 (Groesse von I3) und V-Q4 (nach (d)) sind nicht ableitbar.

## Aufbau (woertlich)

- 2D, h = 0,25, Gebiet ~128 x 64, dt ~0,05.
- Wand: Zusatzpotential V_w |phi|^2 mit V_w = 4, Dicke 2.
- Spaltbreite w = R; Abstaende d in {R; 1,5 R; 3 R; 2R + 4/kappa}.
- omega in {0,80; 0,90}; v in {0,2; 0,3; 0,45}; 41 Stossparameter.
- Beobachtet je Lauf:
  - Ausgangsklasse (reflektiert / ein Spalt / geteilt / geteilt und wiedervereint)
  - Ablenkwinkel des groessten Ladungsstuecks
  - Ladungsanteile
- **Linearer Kontrollarm:** Klein-Gordon-Wellenpaket gleicher Breite und gleicher Geometrie. Er liefert das Rand-kappa, gegen das der Q-Ball verglichen wird.

## Vorhersagen (woertlich; vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. (Leitung) |
|---|---|---|
| V-Q1 | Reichweite: Fuer d = 2R + 4/kappa ist das Histogramm der offenen Spalte gleich der Summe der Einzelspalt-Histogramme, \|I2\|/Summe < 0,05 (scheitert, wenn ein Fernmechanismus wirkt, z. B. Abstrahlung bei Beschleunigung als Pilotwelle) [Kontrolle, nahezu ableitbar] | 85 % |
| V-Q2 | Takt: Hat das Histogramm fuer d <= 1,5 R eine periodische Struktur, dann skaliert ihre Winkelperiode ueber v = 0,2 / 0,3 / 0,45 wie 1/(gamma v), innerhalb +-20 % (scheitert, wenn v-unabhaengig; "kein Muster" ist ebenfalls ein zaehlbarer Ausgang) | 35 % |
| V-Q3 | I3: Fuer d <= 1,5 R ist \|kappa\| >= 0,05 nach Abzug des Rand-kappa aus dem Kontrollarm (scheitert, wenn \|kappa\| < 0,05) | 55 % |
| V-Q4 | Ein-Klick: Fuer d <= R enden mindestens 20 % der durchgelassenen Laeufe mit zwei getrennten Stuecken von je >= 10 % von Q (scheitert, wenn der Ball fast immer einen Spalt waehlt oder sich vereint) | 40 % |

**Bedeutung (woertlich):**
- **V-Q2 bestanden:** Die Phase der inneren Uhr steuert die Ablenkung, aber mit lambda_omega ~ Q lambda_M. Das ist die falsche Laenge fuer Teilchen mit Q >> 1.
- **V-Q4 bestanden:** Das Ein-Klick-Problem ist im Modell sichtbar.
- **Beides zusammen:** Interferenz gehoert nicht zum klassischen Q-Ball, sondern zur quantisierten Schwerpunktbewegung. Das stuetzt Finns Weiche, Q-Baelle nur fuer die Teilchenstruktur zu verwenden.
- **V-Q2 gescheitert (v-unabhaengig):** Es gibt kein de-Broglie-artiges Verhalten des klassischen Balls.

## Budget, Konvergenz, Abbruch (woertlich)

- **Budget:** 2 x 4 x 3 x 41 = 984 Laeufe je Spaltkonfiguration, auf der GPU gebuendelt.
  - Kleintest zuerst mit 1 omega, 2 d, 2 v, 21 y (84 Laeufe) auf p4000 ueber kleintest.sh.
  - Dreifachspalt (7 Konfigurationen) erst nach bestandenem Ruhetest.
- **Konvergenzbindung:**
  - V-Q1 und V-Q3 werden nur gewertet, wenn sich |I2|/Summe bzw. kappa zwischen 41 und 81 Stossparametern UND zwischen h = 0,25 und h = 0,125 um weniger als 0,02 aendern.
  - Sonst ist der Ausgang "unentschieden", nicht "bestanden".
- **Abbruch:** Verliert der Ball im Ruhetest ohne Spalt mehr als 1 % Ladung, wird nicht weiter ausgewertet.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (GPU, CUDA). Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Passt das volle Programm nicht in die Zeitbox, gilt diese Reihenfolge:
  1. Ruhetest
  2. Kleintest
  3. Doppelspalt
  4. Dreifachspalt
  - Ein ehrlicher Teilbericht ist besser als keiner.
