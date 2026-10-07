# Chem 8 Mitte: Ist der grosse Klumpen der ruhende Ball C? (Runde 11, Folgeschritt der Zufallskarte aus Runde 10)

- Leitung: claude-primary. Karte geschrieben ab 2026-09-30 19:36:17 CEST (date), vor jedem Lauf.
- Herkunft: RUNDE-10/chem8/KARTE.md, Entscheidung nach Vorab-Regel "weiter". Naechster Schritt dort: Klumpen mit Ort
  verfolgen, ob der grosse Klumpen (etwa 1,5 Q0) der ruhende Ball C ist.
- Bestand aus Runde 10 (dichtes v-Raster, T = 300 und 600, grob = fein):
  - bruecke bei dphi = pi: Fenster v = 0,12 bis 0,17 (bis 1,52 Q0). Bei T = 600 ist dort kein Klumpen mehr im
    Messbereich.
  - bruecke bei 3pi/4: Fenster v = 0,06 bis 0,12 (bis 1,56 Q0). Bei T = 600 bleibt fuer v >= 0,11 ein Klumpen von 1,26 bis
    1,51 Q0; fuer v < 0,11 hat er den Bereich verlassen.

## Test

- Code: chem8_mitte.py = Kopie von RUNDE-10/chem8/chem8_dicht.py (sha256 b49075c729dc1d0f...). Einzige Aenderung: eine
  weitere Messspalte, die Ladung im Mittelstueck |x| < 6, gemittelt wie der groesste Klumpen ueber die letzten 50
  Zeiteinheiten.
- Laeufe wie in Runde 10: v = 0,05 bis 0,25 (21 Werte), T = 300 und T = 600, grob und fein, Spur p4000b.

## Vorhersage (vor jedem Lauf)

- **V1 (3pi/4, v >= 0,11):** Der grosse Klumpen ruht in der Mitte. Ladung in |x| < 6 geteilt durch den groessten
  Klumpen ist mindestens 0,9, bei T = 300 und bei T = 600 (fein).
- **V2 (pi, v = 0,12 bis 0,17, T = 300):** Der grosse Klumpen liegt nicht in der Mitte; das Verhaeltnis ist unter 0,5.
  Grund: Er ist bis T = 600 aus dem Messbereich gewandert.
- **V3 (3pi/4, v = 0,06 bis 0,10, T = 300):** ebenfalls unter 0,5, aus demselben Grund.
- **V4 (Kontrolle):** Die Spalten der Klumpen stimmen mit Runde 10 ueberein (Code sonst unveraendert), Abweichung
  hoechstens 1e-12.

## Scheiterregel

- Verfehlt V1 an mehr als einem der Punkte v >= 0,11 bei 3pi/4, ist das Bild "der ruhende Ball C hat Ladung aufgenommen"
  fuer 3pi/4 falsch.
- Verfehlt V4, ist der Lauf nicht auswertbar.

## Ergebnis (Leitung, eingetragen 19:40:13; Laeufe .69 p4000b 19:36:54 bis 19:40:06, rc = 0)

Code chem8_mitte.py (sha256 d3c5ff2889384bef..., lokal = .69). Dateien: lauf-69/t300/katalyse.json (91d68bce...),
lauf-69/t600/katalyse.json (df644d0f...), LAUF-CHEM8M.log, kette.sh.

- **V4 (Kontrolle) getroffen:** Die Klumpenspalten stimmen mit Runde 10 bis 6,7e-16 (T = 300) bzw. 4,4e-16 (T = 600)
  ueberein.
- **V1 verfehlt, an allen Punkten:** Bei 3pi/4 und v >= 0,11 liegt im Mittelstueck |x| < 6 am Ende fast keine Ladung.
  - T = 300: 0,01 bis 0,16 Q0 bei einem groessten Klumpen von 1,26 bis 1,52 Q0; Verhaeltnis 0,01 bis 0,11 statt >= 0,9.
  - T = 600: 0 bis 0,01 Q0 bei 1,26 bis 1,51 Q0. Der grosse Klumpen ist bis T = 600 im Messbereich, aber nicht in der
    Mitte.
- V2 getroffen (pi, v = 0,12 bis 0,17: Mitte 0 bei T = 300). V3 getroffen (3pi/4, v = 0,06 bis 0,10: Mitte 0 bis 0,01).
- **Nach der Scheiterregel ist das Bild "der ruhende Ball C hat Ladung aufgenommen" fuer 3pi/4 falsch.** Der grosse Klumpen
  liegt ausserhalb der Mitte. Er ist also ein bewegter Ball oder ein aus der Mitte gestossener Klumpen; welcher, ist nicht
  gemessen.
- Einordnung: Gemessen ist eine Ladungsumverteilung im Dreierstoss. Katalyse im Sinn "C hilft A und B zu verschmelzen und
  bleibt selbst gleich" ist nicht gezeigt. Den paarweisen Ladungsuebertrag beschreibt die Literatur (Battye/Sutcliffe
  2000, nur Abstract gelesen).
