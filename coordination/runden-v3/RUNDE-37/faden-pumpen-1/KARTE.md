# FADEN-PUMPEN-1: Kann ein dicker Faden in Finns Netz pumpen, und wie viele Dimensionen hat das Pumpen? (Runde 50, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 17:46:56 CEST (date), vor jeder Rechnung.
- **Finn, 05.10.:**
  - "ja wenn ein faden 3d wird und eine aussenflaeche bekommt bei einem durchmesser von 1 und dann der kantenlaenge (?)
    kann der faden auch dicker werden und pumpen? wievieldimensional pumpt es auf dem faden?"
  - "also ein string netz pipe... kann es sein das alle punkte in 3d bzw 4d auch 'rohre' sind oder/und eine richtung
    haben?"
- **Herkunft [P]:**
  - STRING-1: Fluss-Faeden entstehen bei teurem Fluss, zittern und reissen.
  - ROHR-1: Boerdijk-Coxeter-Helix, dichteste Rohrpackung bei D/a = 3 Wurzel 3 / 5, also Durchmesser etwa eine Kante.
  - ATEM-NETZ-1: atmende Punkte, Pyrochlor ordnet sich "2 + 2".
  - Q-Ball-Sektor (Papier I, stille Schwingung).
  - FADEN-DIM-2: raue Faeden treffen sich nur bis Raumdimension 3.
- **Modell:**
  - (a) Q-Schlauch: ein unendlich langer Q-Ball mit Ladung je Laenge, das Feld dreht sich innen wie exp(i omega t). Er
    gehoert zu unserem Modell, ist aber nicht topologisch.
  - (b) Gegenprobe: ein Wirbelfaden eines komplexen Felds mit Minimum bei abs(phi) ungleich 0. Er ist topologisch und
    als Standardfall bekannt.
  - Beide auf V bzw. einem feinen Gitter, Durchmesser etwa 1 bis 4 Kantenlaengen.
- **Ableitbarkeit:**
  - [M, L] Ein dicker Faden hat zwei Biegeformen quer zur Achse (duenner Faden, Nambu-Goto: D - 2 = 2). Dazu kommen
    Formen des Querschnitts: m = 0 Pumpen, m = 2 oval, und so weiter. Alle laufen als Wellen laengs des Fadens: 1 Raum
    plus Zeit. Mit allen Querschnittsformen lebt das Pumpen auf der Rohrflaeche: laengs, rundherum, Zeit.
  - [L] Beim Standard-Wirbel (b) sind die Biegeformen masselos; das Pumpen ist eine gebundene Form unter der Feldmasse.
  - [H] Fuer den Q-Schlauch (a) ist eine Perlenbildung moeglich (wie ein Wasserstrahl, Rayleigh-Plateau): Er pumpt
    sich in Q-Baelle auseinander.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| FP1 | (b) Wirbel: zwei Biegeformen mit omega -> 0 fuer k -> 0, Tempo laengs des Fadens = c auf 2 % | 85 % |
| FP2 | (a) Q-Schlauch: Die Pumpform (m = 0) waechst fuer lange Wellen an (Perlenbildung), bei k unter einer Schwelle von etwa 1/R | 60 % |
| FP3 | (a) Biegeformen des Q-Schlauchs laufen langsamer als c (Spannung kleiner als Energie je Laenge) | 60 % |
| FP4 | Bei Durchmesser um eine Kantenlaenge haftet der Faden am Gitter (kleine Luecke der Biegeform statt omega -> 0) | 50 % |

## Rahmen

- Code-Agent, ohne Einfrieren und ohne Leser (Finn: einfach machen). Spuren cpu2 bis cpu4 ueber kleintest.sh, je Lauf
  hoechstens 10 min.
- Code aus RUNDE-37/schwere-masse-v/code (Q-Baelle auf V) und kanon-transfer-1 bzw. uebergabe-konfluenz-1
  (Skalar auf den Ecken) nur kopieren.
- Synthetisch, keine Messdaten.
