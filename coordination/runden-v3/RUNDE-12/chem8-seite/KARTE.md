# Chem 8 Seite: Liegt der grosse Klumpen beim Ball B? (Runde 12, Folge aus BS-2000)

- Leitung: claude-primary. Karte geschrieben ab 2026-10-01 17:52:38 CEST (date), vor jedem Lauf.
- Herkunft: Die Lesung BS-2000 (RUNDE-12/battye-sutcliffe/LESUNG-BS2000.md) uebertraegt die Richtungsregel von
  Battye/Sutcliffe auf unseren Code (Drehsinn e^{-i omega t}, umgekehrt zu B&S). Danach fliesst Ladung von A ueber C nach B,
  und der grosse Klumpen ist B bei x > 0 [ES des Lesers].
- Bestand: RUNDE-11/chem8-mitte. Bei 3pi/4 und v >= 0,11 liegt der grosse Klumpen (1,26 bis 1,52 Q0) nicht in |x| < 6.

## Test

- Code chem8_seite.py = Kopie von RUNDE-11/chem8-mitte/chem8_mitte.py. Einzige Aenderung: zwei weitere Messspalten, die
  Ladung links (x < -6) und rechts (x > +6) im Messbereich |x| < 75, gemittelt ueber die letzten 50 Zeiteinheiten wie der
  groesste Klumpen.
- Laeufe wie in R11: v = 0,05 bis 0,25 (21 Werte), T = 300 und 600, grob und fein, Spur p4000b (Fallback CPU nur,
  wenn die GPU belegt ist; dann mit Vermerk).

## Vorhersage (vor jedem Lauf; uebernommen aus BS-2000, Leitung bindet)

- **V1:** Bei 3pi/4, bruecke und v >= 0,11 gilt bei T = 300: Ladung rechts (x > 6) mindestens 0,9 mal der groesste Klumpen,
  Ladung links (x < -6) hoechstens 0,6 Q0.
- **V2:** Dasselbe bei T = 600, soweit der Klumpen im Messbereich bleibt (R11: bis T = 600 ja).
- **V3 (Kontrolle):** Klumpen- und Mittelspalten gleich R11 bis 1e-12.

## Scheiterregel

- V1 an mehr als zwei der Punkte v >= 0,11 verfehlt: Die uebertragene Richtungsregel von B&S traegt unseren Dreierstoss
  nicht.
- V3 verfehlt: nicht auswertbar.

## Ergebnis

(nach dem Lauf)

## Ergebnis (Leitung, eingetragen 2026-10-01 17:57:44 CEST; Laeufe .69 p4000b 17:53:09 bis 17:56:24, rc = 0)

Code chem8_seite.py (sha256 651873f9d2cb59f5...). lauf-69/t300/katalyse.json (7653238c...), lauf-69/t600/katalyse.json
(e5ad20f7...). V3: Klumpen- und Mittelspalten gleich R11 bis 6,7e-16, getroffen.

| v (3pi/4, bruecke) | groesster Klumpen T300 | links T300 | rechts T300 | links T600 | rechts T600 |
|---|---|---|---|---|---|
| 0,11 | 1,52 | 1,24 | 1,66 | 0,50 | 1,56 |
| 0,14 | 1,48 | 0,88 | 2,02 | 0,19 | 1,53 |
| 0,20 | 1,37 | 1,00 | 1,88 | 0,11 | 1,44 |
| 0,25 | 1,26 | 1,04 | 1,38 | 0,04 | 1,32 |

- **V1 (T = 300) verfehlt, an allen 15 Punkten.** Die Klausel "rechts mindestens 0,9 mal groesster Klumpen" ist ueberall
  erfuellt (1,09 bis 1,39). Links bleiben aber 0,88 bis 1,24 Q0, verlangt waren hoechstens 0,6.
- **V2 (T = 600) formal getroffen:** rechts etwa gleich dem groessten Klumpen, links 0,04 bis 0,50. Links ist es aber
  wenig, weil der Rest von A bis dahin den Messbereich verlassen hat, nicht weil A Ladung abgegeben haette. Siehe
  T = 300.
- **Nach der Scheiterregel** (V1 an mehr als zwei Punkten verfehlt): Die uebertragene Richtungsregel "A ueber C nach B"
  traegt unseren Dreierstoss nicht.
- Gemessen ist:
  - Der grosse Klumpen liegt rechts, auf der Seite von B.
  - A behaelt etwa seine Ladung (~1 Q0) und laeuft weg.
  - Die Ladung des ruhenden C geht nach rechts. [H] Der Fluss ist eher C -> B als A -> C -> B.
