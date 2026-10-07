# TETRA-KETTE: Wie weit traegt eine Kette aus Knicklicht-Tetraedern die Spannung eines Defekts? (Runde 26)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben nach 2026-10-03 03:54:00 CEST (letzte date-Messung) und vor jeder Rechnung. Selbstanzeige: Zuerst stand hier "03:58", geschaetzt und in der Zukunft; berichtigt um 03:56:05 (date).
- **Herkunft:**
  - Finn, Runde 22: "koennen gekoppelte Tetraeder in 3D koppeln ueber Winkelspannung als Feldgroesse?"
  - Finn, Runde 24: Knicklicht-Tetraeder.
  - TETRA-STAB (RUNDE-24/tetra-stab/ERGEBNIS.md): Ein staerker geneigter Stab erzeugt in einem Tetraeder ein in sich
    geschlossenes Zug-Druck-Muster an allen Kontaktpunkten.
- **Frage:** Haengen viele Tetraeder flaechig aneinander, wie weit reicht dann die Spannung eines einzelnen Defekt-Stabs?
  Langreichweitig wie ein Feld, oder abgeschirmt?
- **Schreibtisch der Leitung [H]:**
  - Eine Kette flaechenverbundener Tetraeder (Boerdijk-Coxeter-Helix, "Tetrahelix") ist als Stabwerk mit Gelenken
    statisch bestimmt (3V - 6 Staebe), also ohne Eigenspannung.
  - Mit eingespannten Verbindern (Momente) ist sie unbestimmt. Ein lokaler Fehlwinkel erzeugt dann eine Eigenspannung, die
    sich selbst im Gleichgewicht haelt.
  - Nach dem Prinzip von Saint-Venant [L] klingt eine solche Last in einem schlanken Tragwerk exponentiell ab, mit einer
    Abklinglaenge von der Groesse des Querschnitts, hier etwa ein Tetraeder.
  - Erwartung: Die Winkelspannung ist in der Kette abgeschirmt, wie ein massives Feld (Yukawa), nicht weitreichend.
  - Gegenbild: Im elastischen Kontinuum (WINKELFELD-1) fiel eine 3D-Scharnierquelle wie ein Potenzgesetz ab (p ~ 2,4 bis
    2,7).

## Test

- **Modell wie TETRA-STAB** (RUNDE-24/tetra-stab/code/tetra_stab.py): von Natur aus gerade Staebe (B = 1, L = 1,
  Ks = 25600), Verbinder starr mit Lage und Drehung, keine Torsion. Energieformen (Biegung B/l0, Einspannung 2B/l0,
  Dehnung) wie dort.
- **Tetrahelix:**
  - M = 12 Tetraeder: 15 Ecken v_0 bis v_14, Staebe (i, i+1), (i, i+2), (i, i+3), zusammen 39.
  - Je vier aufeinanderfolgende Ecken bilden ein regulaeres Tetraeder mit Kante L.
  - Einspannrichtungen = gerade Kantenrichtungen (alpha = 0), damit ist der Bezugszustand spannungsfrei.
- **Defekt:** ein Stab im ersten Tetraeder, (v_0, v_1), an beiden Enden um alpha_d = 10 Grad zur Mitte seines Tetraeders
  geneigt, wie in TETRA-STAB.
- **Lagerung:** Der letzte Verbinder v_14 ist fest (Lage und Drehung); alles andere ist frei. Die Reaktion dort muss klein
  sein.
- **Messung:**
  - je Stabende Kraft und Moment
  - je Tetraeder k (Ecken v_k bis v_(k+3)) die groesste Momentbetrag-Aenderung und die groesste Kraft gegen den
    Bezugszustand
  - Verlauf ueber k und Abklingverhaeltnis je Tetraeder
- Diskretisierung N = 10 und 16 je Stab als Gitterprobe. Die Energie fuer alle Staebe gebuendelt (vektorisiert) rechnen,
  sonst wird es zu langsam.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TKe0 | Ohne Defekt spannungsfrei: alle |tau|, |F| L < 1e-8 B | 90 % |
| TKe1 | Das groesste Endmoment je Tetraeder faellt mit dem Abstand vom Defekt ueber mindestens sechs Tetraeder monoton | 70 % |
| TKe2 | Der Abfall ist exponentiell (log-linearer Fit ueber Tetraeder 2 bis 8 mit R^2 > 0,95), Verhaeltnis je Tetraeder zwischen 2 und 30 (Abklinglaenge 0,29 bis 1,44 Tetraeder) | 55 % |
| TKe3 | Die Axialkraft der Staebe wechselt entlang der Kette mindestens einmal das Vorzeichen | 50 % |

**Bedeutung (vorab):**
- TKe1 und TKe2 treffen ein: In einer Kette aus Knicklicht-Tetraedern ist die Winkelspannung eines Defekts abgeschirmt,
  mit einer Abklinglaenge um ein Tetraeder.
  - Gekoppelte Tetraeder "spueren" sich dann nur ueber Nachbarn, wie ein massives Feld [H].
  - Eine weitreichende Kopplung braucht etwas anderes, etwa eine Netto-Winkelladung in einer Flaeche wie in WINKELFELD-1.
- TKe2 trifft nicht ein, weil der Abfall langsamer ist (Potenzgesetz): Die Kette traegt die Spannung weit. Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min, 4 GB).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min.
