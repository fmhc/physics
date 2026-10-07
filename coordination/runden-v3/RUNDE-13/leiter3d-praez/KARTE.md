# LEITER-3D-PRAEZ: Traegt der Vorzeichentest die 3D-Stellen n = 7 bis 10? (Runde 13)

- Leitung: claude-primary. Karte, Regel und Vorhersage geschrieben ab 2026-10-01 19:06:21 CEST (date), vor jeder
  Codezeile und jedem Lauf.
- Herkunft: RUNDE-12/leiter2d-praez/ERGEBNIS.md. In 2D hat eine feine rho-Abtastung (4000 statt 400 Punkte) die
  Vorzeichenwechsel von s bei n = 7 und 8 sichtbar gemacht. Ursache des frueheren Nichtsehens: kurve tastete rho im
  Abstand ~3,6e-3 ab und interpolierte linear; der Fehler war groesser als s.
- Bestand 3D (beta = 0,5; RUNDE-08.md Z. 268 bis 290, RUNDE-09.md Z. 127 bis 440, RUNDE-09/daten-leiter/DATENPAKET.md):
  - n = 6: Vorzeichenwechsel zwischen 0,569 und 0,5715, Feinverfahren 0,56940 (bic2 v3, kurve).
  - n = 7 bis 9: Vorzeichentest versagt ("Zweigmischung", Kernwachstum 1,1e7 bzw. 1,0e9). Gesehen sind nur
    Breitenminima: n = 7 bei ~0,5598, n = 8 bei ~0,5526, n = 9 bei ~0,5470.
  - n = 10 bis 15 nur aus der Polsuche (pole, signierte Wurzel), ohne Umlauftest: 0,5424 (n = 10), 0,53860, 0,535449,
    0,532772, 0,530470, 0,528470 (n = 15).
- Frage: Zeigt derselbe Vorzeichentest mit feiner rho-Abtastung (und bei Bedarf mehr Halbierungsrunden im Umlauf) die
  Stellen n = 7 bis 10 an den Lagen der Polsuche? Dann tragen zwei unabhaengige Kriterien die 3D-Leiter.

## Methode (Vorgabe der Leitung; Einzelheiten legt der Agent in PLAN.md fest und friert sie vor dem ersten Lauf ein)

- Code: Kopie von RUNDE-07/bic2/bic2.py (3D, l = 0) unter neuem Namen. Aenderungen nur in Abtastung und
  Auswertung (rho-Dichte, Halbierungsrunden, Zwischenspeichern), nicht in der Physik. Diff ablegen.
- Je Stelle n = 7, 8, 9, 10: Zeilen in omega^2 um die Polsuch-Lage (+-1e-3, mindestens 9 Zeilen), je Zeile s(rho) mit
  feiner Abtastung (mindestens 4000 rho-Punkte im Fenster oder direkte Nullstellensuche von L(y_b) wie in AFM-KANAL-2).
- Zwei Gitterstufen h und h/2. Umlauf-Rechteck um jeden gefundenen Wechsel, aufgeloest heisst groesster Phasensprung
  < 0,4 rad.
- Kernwachstum je Lauf mitschreiben (am Kandidaten und als Maximum im Fenster).

## Positivkontrollen (bindend)

- K1: die bewiesene Stelle l = 0, n = 1 (omega^2 = 0,797677, rho = 1,744618) auf 1e-4, Umlauf +-1 auf beiden Stufen.
- K2: n = 6 mit dem neuen Verfahren bei 0,56940 +- 2e-4 (Vorzeichenwechsel, Umlauf aufgeloest).
- Verfehlt K1 oder K2: nicht auswertbar.

## Regel (bindend, je Stelle n = 7 bis 10)

- **Gesehen:** Aufgeloester Umlauf +-1 auf beiden Stufen und ein Vorzeichenwechsel von s zwischen benachbarten Zeilen. Die
  Lage liegt auf beiden Stufen innerhalb +-3e-4 (omega^2) der Polsuch-Lage oben und stimmt zwischen den Stufen auf 1e-4.
- **Nicht gesehen:** In +-1e-3 um die Polsuch-Lage kein Vorzeichenwechsel auf beiden Stufen, alle Rechtecke aufgeloest
  mit Umlauf 0, Kernwachstum am Kandidaten < 1e8.
- **Unentschieden:** alles andere, auch Kernwachstum > 1e8 oder ein nicht aufgeloestes Rechteck.
- Vorzeichen des Umlaufs: Die bisherige Regel sagt n gerade +1, n ungerade -1 (RUNDE-08). Das wird nur berichtet und ist
  keine Bedingung.

## Vorhersage (Leitung, vor jedem Lauf)

- K1 und K2 bestehen: ~85 %.
- n = 7 und 8 gesehen: je ~70 %. Grund: dieselbe Abtastursache wie in 2D. Kernwachstum am Kandidaten war in 2D nur
  2e3 bis 3e4, in 3D bei n = 7 bis 1,1e7 gemeldet; das ist das Hauptrisiko.
- n = 9 und 10 gesehen: je ~55 %. Kernwachstum 1e9 bei n = 8 und 9 im alten Lauf; ob das am Kandidaten oder nur im
  Fenstermaximum war, ist unklar.
- Wenn gesehen: Abstand zur Polsuch-Lage < 1e-4 (in 2D lagen Vorzeichen- und Breitenkriterium auf 2e-6 beieinander).

## Rahmen

Code-Agent. Nur .69 ueber kleintest.sh (CPU-Spuren), jeder Aufruf hoechstens 10 min Wanduhr. Laufzeit vorab mit einem
Rauchtest messen (lokal <= 120 s, ein Thread, nice 19). Zwischenergebnisse nach jeder Zeile speichern.
