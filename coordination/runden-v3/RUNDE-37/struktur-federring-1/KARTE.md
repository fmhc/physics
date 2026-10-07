# STRUKTUR-FEDERRING-1: Was lehrt Finns Federring-Struktur (Rastung, freies Schwingen, begrenztes Ueberdrehen) fuer unsere Modelle? (Inspirations- und Schreibtischkarte, Runde 41)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 14:37:30 CEST (date).
- **Auftrag von Finn (04.10., Nachricht zwischen 14:31 und 14:37, woertlich):** "schau dir mal in einem subagent diese
  struktur an, es hat locking mechanismen aber wenn es in 3d frei schwebt schwingt es und kann über die locking ebenen
  hinaus drehen (nicht unendlich) [Bild] hol dir inspirationen daraus"
- **Bild:** RUNDE-37/struktur-federring-1/bild-finn-20261004.png (sha256 e44e1a90...). Beschreibung der Leitung [B, am
  Bild abgelesen, kann ungenau sein]: gruener 3D-Druck; drei konzentrische Ringe und eine Nabe; zwischen den Ringen
  Maeander- bzw. Serpentinenfedern; radiale Speichen mit Rastnasen bzw. Kerben an den Ringen; Kerben am Aussenrand.
- **Lesart der Leitung [H]:** Eine nachgiebige (compliant) Drehmechanik. Federn geben eine Rueckstellkraft (Parabel im
  Drehwinkel), Rastungen geben bevorzugte Winkel (periodische Mulden). Zusammen entsteht eine "Waschbrett"-Landschaft
  mit endlich vielen erreichbaren Mulden. Frei im Raum kommen Kippen und Biegen aus der Ebene dazu; das erlaubt mehr
  Drehung als in der Ebene, aber nicht beliebig viel.
- **Projekt-grep (Leitung):** "Guertel"/"belt trick" als Idee H3 GUERTEL-1 im Ideenpool (Seile mit Ausschlussvolumen,
  Entwirrungsenergie; nicht gerechnet), STRATEGIE-SPIN-20261004.md Weg 2; Treffer zu Rastung/Multistabilitaet in
  RUNDE-16/drei-takt und RUNDE-36/-38/-39 (zuerst lesen, nichts doppelt).
- Kennzeichen: [B] am Bild abgelesen, [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [S] an der Quelle gelesen,
  [ES] eigener Schluss, [H] Hypothese.

## Fragen

1. **Mechanik der Struktur:** Freiheitsgrade, Steifigkeiten (in der Ebene, aus der Ebene, Torsion), Rastzustaende,
   Schwingungsmoden; warum ist das Ueberdrehen frei im Raum groesser, aber begrenzt? Ein einfaches Modell
   (Energielandschaft aus Federn plus Rastung plus Kippen) als Schreibtischrechnung.
2. **Physikalische Gegenstuecke (je mit Kennzeichen):** mindestens pruefen
   - Waschbrett-Potential, Phasenspruenge (Kinks, Sinus-Gordon, Frenkel-Kontorova) als teilchenartige Anregungen
   - Phasen- bzw. Modenkopplung verschachtelter Oszillatoren (Synchronisation, Arnold-Zungen; Finns "synchrones Drehen")
   - Diracs Guertel- bzw. Tellertrick: ein an Federn angebundener Koerper, 360 gegen 720 Grad, Spin 1/2 (Idee H3)
   - Orientierungsordnung mit diskreten Rastungen (Uhrmodelle, Tetraeder-Orientierungen mit Gruppe T bzw. 2T,
     nichtabelsche Defekte; Idee H4 TETRA-RAHMEN-1)
   - Q-Baelle: innere Drehung mit Rastung (Ladungstausch, Phasenspruenge)
   - nachgiebige mehrstabile Mechanismen und mechanische Metamaterialien (Literatur)
3. **Inspiration fuer das Weltmodell:** Welche Idee aus der Struktur ist fuer unsere Kandidaten (Finns Tetraeder-Netz,
   K-AM mit Flip-Flop, Ereignis-Netz) neu und pruefbar? Ehrlich trennen: Analogie, die nur schoen ist, gegen Mechanismus,
   der etwas vorhersagt.
4. **Kartenvorschlag:** hoechstens zwei kleine Rechenkarten (<= 10 min je Lauf), die scheitern koennen, mit
   Ableitbarkeitsprobe. Beispiel zum Pruefen [H]: ein angebundener Rotor aus elastischen Federn mit Selbstausschluss,
   frei im Raum: Ist die Energielandschaft nach 360 Grad noch verdreht und nach 720 Grad entdrehbar (Guertel-Trick), und
   wie hoch ist die Sperre?

## Abgabe

- RUNDE-37/struktur-federring-1/BERICHT.md: Ergebnis zuerst; Mechanik der Struktur; Gegenstuecke mit Kennzeichen und
  Fundstellen; Inspirationen fuer das Weltmodell (Analogie gegen Mechanismus); Kartenvorschlaege mit Ableitbarkeitsprobe;
  "Einfach gesagt" (3 bis 5 Saetze, fuer Finn).

## Rahmen

- Schreibtisch und Literatur; keine Laeufe. Hoechstens 8 gezielte Abrufe, keine Websuche; Fundstellen nur aus selbst
  gelesenem Text, lokale Kopien im Kartenordner quellen/.
- Lokal kein python, awk oder perl. Zeitbox 60 min.

## Erweiterung (Leitung, gleiche Zeit): Drehungs-Cluster aus Finns vorheriger Nachricht

- Finn (Nachricht zwischen 14:29 und 14:31): "kann ein syncrones drehen in mehreren dimensionen mit verschiedenen
  dimensionen potential dings berechnung nice machen". Gekoppelt mit dieser Karte (Drehung, Rastung, Kopplung), deshalb
  hier statt in TETRAEDER-L: synchrone bzw. isokline Doppelrotation (Quaternionen, Hopf-Fasern, SU(2)), mehrkomponentige
  und ladungstauschende Q-Baelle ("charge-swapping", Copeland/Saffin/Zhou 2014 [L]), Projektbezug QB-BS-2D (drehender
  Knoten plus Q-Ball: nicht gebunden), SPIN-HOPF-L, Codex B.5 (C x S^2). Ableitbarkeitsprobe fuer eine moegliche
  Rechenkarte SYNCHRON-QBALL-1 (zwei Felder mit Doppelrotation bzw. Ladungstausch) gehoert in den Bericht.
- Budget damit: hoechstens 12 gezielte Abrufe, Zeitbox 90 min.

## Hinweis (Leitung, 2026-10-04 14:43)

- Diese Karte ist mit GUERTEL-1 zusammengelegt (RUNDE-37/guertel-1/KARTE.md); ein Agent bearbeitet beide.
