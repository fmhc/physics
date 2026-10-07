# QBALL-DREIPOL-3: Ab welcher Ladung gibt es den Dreifarben-Tropfen in 3D, ist er dort ein Minimum, und folgt die Schwelle einer Duennwand-Formel ueber die Dimension? (Runde 43, Fast Lane)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 19:06:56 CEST (date), vor jeder Rechnung.
- **Herkunft:** QBALL-DREIPOL-2 (RUNDE-37/qball-dreipol-2/ERGEBNIS.md).
  - Bei g4 = -0,1 entmischen sich drei Farben zu einem festen Dreifarben-Tropfen.
  - 2D: vorhanden bei Q1 = 60, lokales Minimum.
  - 3D: bei Q1 = 2500 (erzwungen, Start schon unter dem Mischball) und Q1 = 800 (3,32 unter dem Mischball, nicht
    erzwungen); bei Q1 = 200 und 400 verschmelzen die Pole.
  - Ob das 3D-Dreieck ohne Symmetriezwang stabil ist, ist nicht geprueft.
- **Finn:** Q-Baelle als 3 Pole "auf 3d/4d"; zusammengesetzte Formel ueber Dimensionen (18:33 bis 18:36).
- **Regel Dimensionsvergleich (AGENTS.md):** 2D und 3D getrennt; ein Ergebnis aus 2D gilt nicht ungeprueft in 3D.
- Kennzeichen: [M] Mathematik, [E] Rechnung, [L] Literatur, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung; nach den Lehren aus QBALL-DREIPOL-1 und -2)

- **Pflicht vor jedem Lauf:** E_start gegen E_Mischball und gegen E_Tropfen pruefen. Ein Lauf, dessen Start schon unter
  einem der Ausgaenge liegt, ist erzwungen und zaehlt nur als Kontrolle.
- **Vorab ableitbar [M, Duennwand]:** Der Tropfen hat innere Grenzflaechen (Kosten ~ sigma R^(D-1)) und gewinnt
  Volumenenergie aus der Entmischung (~ Delta R^D). Er gewinnt also oberhalb eines Schwellradius R* ~ sigma/Delta; die
  Schwellladung waechst wie R*^D mit der Dimension. Das ist nur eine Groessenordnung; Vorfaktoren sind nicht ableitbar.
- **Nicht ableitbar:**
  - die Schwellladung Q1*(3D) und Q1*(2D)
  - ob der 3D-Tropfen ausserhalb des symmetrischen Unterraums ein Minimum ist
  - ob R* in 2D und 3D (in Einheiten des Einpol-Radius) gleich ist

## Auftrag (Code-Agent)

1. Code aus qball-dreipol-2/code/ kopieren (dort nichts aendern).
2. **Teil A, Schwelle:**
   - 3D: Bisektion in Q1 zwischen 400 und 800 (g4 = -0,1), Fluss bei festen Ladungen vom beruehrenden Dreieck.
   - 2D: dieselbe Bisektion nach unten ab Q1 = 60.
   - Je Schritt E_start, E_Mischball und E_Tropfen protokollieren.
3. **Teil B, Stabilitaet 3D:** bei Q1 = 800 sechs Stoerungen ausserhalb des Unterraums (wie DP1:
   2 Verschiebungen, 2 Ladungsverschiebungen +-5 % ohne Sektorwechsel, 2 Phasenversaetze); Rueckkehr pruefen.
4. **Teil C, Formel:** Schwellradius R* (Tropfenradius an der Schwelle, in Einheiten des Einpol-Radius gleicher Ladung)
   in 2D und 3D.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| DR0 | Kontrollen: Q1 = 800 (3D) gibt den Tropfen 3,32 +- 0,1 unter dem Mischball; Q1 = 400 verschmilzt; 2D-Tropfen bei Q1 = 60 wie DREIPOL-2 | 85 % |
| DR1 | [H] Der 3D-Tropfen bei Q1 = 800 ist ein lokales Minimum: alle 6 Stoerungen kehren zurueck (Endabstand < 2 % R, Energie gleich auf 1e-3) | 55 % |
| DR2 | [H, M Duennwand] R* ist in 2D und 3D gleich auf 30 % (eine dimensionsuebergreifende Schwellformel) | 40 % |

**Bedeutung (vorab):**
- **DR1 trifft ein:** In 3D gibt es oberhalb einer Schwellladung einen stabilen Dreifarben-Tropfen. Er ist kein Einschluss
  (einzelne Pole stabil, U(1)^3).
- **DR2 trifft ein:** Die Schwelle folgt einer einfachen Duennwand-Formel ueber die Dimension; die Schwellladung waechst
  dann wie R*^D [H].
- **DR2 verfehlt:** Die Schwelle haengt nicht einfach an einem Radius; dicke Waende zaehlen mit.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (frei seit QBALL-DREIPOL-2). Je Lauf <= 10 min.
  Zeitbox 90 min.
