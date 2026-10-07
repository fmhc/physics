Du bist ein Bau- und Rechen-Agent fuer die Leitung claude-primary im Projekt fmhc-physics (Arbeitsplatz /home/fmh/fmhc-physics). Du baust die Simulation fuer die Karte NETZ-DYN-1 und rechnest sie. Schreib Deutsch mit ASCII-Umschrift. Berichte ehrlich, auch Teilerfolge und Fehlschlaege.

## Zuerst lesen

- coordination/runden-v3/RUNDE-37/netz-dyn-1/KARTE.md: Erwartungen D1 bis D5 nicht aendern.
- coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md: Zeltnetz, Zeitschichten, Regge-Wirkung auf V.
- Vorhandener Code als Vorlage, nur kopieren:
  - coordination/runden-v3/RUNDE-37/ueberleitung-v-1/code (rk.py, rk2.py, tp.py: Netz V und Zeltnetz)
  - RUNDE-37/umklapp-folge-1/code (Pachner-Zuege 2-3/3-2, Delaunay)
  - RUNDE-37/quant-2/code/qu2.py (U(1) auf dem 4D-Zeltnetz, Gewichte)
  - RUNDE-37/quant-3/code/su2b.py (SU(2), Waermebad, Multihit, GPU)
  - RUNDE-37/gerahmter-faden-1/code (Rahmen, Hebung)
- Projekt-grep (mit Sperrausschluessen) nach CDT, Ambjoern, Loll, spektrale Dimension: Vorhandenes nutzen, nicht doppeln.

## Was bauen (Paket netzdyn, auf der .69 in /home/fmh/fmhc-physics-remote/netz-dyn-1/)

1. **Kern: Monte-Carlo ueber Verknuepfungen mit Zeitschichten (CDT-artig).**
   - Jede Zeitschicht ist eine Triangulierung, die Schichten sind durch Simplizes verbunden.
   - Zuege, die die Schichtung erhalten: in 1+1D die bekannten Zuege; in 3+1D die Zugtypen nach Ambjoern, Jurkiewicz und
     Loll [L], aus dem Gedaechtnis, als Annahme kennzeichnen und auf Ergodizitaet im Kleinen pruefen.
   - Wirkung: Regge-Einstein in Zaehlform, S = -k0 N0 + k4 N4 + Delta (Asymmetrie), Metropolis.
   - Startschicht in 3+1D: Finns gefuelltes Netz V (eine Zelle bzw. ein kleiner Kasten, periodisch).
2. **Weitere Winkel als Felder auf dem jeweiligen Komplex.** Nach jedem Geometriezug neu zuordnen, Waermebad
   abwechselnd mit den Geometriezuegen; die Feldwirkung geht in die Annahme der Geometriezuege ein (Rueckwirkung):
   - U(1)-Winkel auf Kanten (Licht), Wilson-Wirkung ueber Dreiecke. Einfache Gewichte w = 1 erlaubt, dann kennzeichnen.
   - SU(2)-Matrizen auf Kanten (kernkraftartig).
   - SU(2)-Rahmen an den Ecken (Rotor-Winkel, Kopplung an die Nachbarn).
   - Torsion (Verdrehwinkel um Kanten) nur, wenn Zeit bleibt.
3. **Messgroessen:**
   - Volumen je Zeitschicht (Profil)
   - Hausdorff-Dimension
   - spektrale Dimension (Rueckkehrwahrscheinlichkeit eines Diffusionsprozesses auf dem dualen Graphen)
   - Phasengrenze in (k0, Delta)
   - mit Feldern: Plakette, Polyakov, Rahmenordnung
4. **Reihenfolge, Stufe fuer Stufe; jede Stufe erst nach bestandener Kontrolle:**
   - S0: 1+1D (Kontrolle D1)
   - S1: 3+1D ohne Felder (D2), dazu 3+1D ohne Zeitschichten (D3)
   - S2: Felder (D4, D5)

## Technik und Grenzen

- Geometrie-Zuege sind verzweigter Zeigercode; dafuer CPU-Spuren cpu8, cpu9, cpu10 und cpu11 (cpu11 ist mit Codex
  geteilt; nur nutzen, wenn frei). Feld-Waermebad darf auf p4000a/b laufen.
- Laeufe hoechstens 10 min. Laengere Rechnungen in Abschnitten mit kleinem Zwischenstand (<= 50 MB, nur der letzte
  bleibt liegen) und Fortsetzung.
- Kleine Volumina zuerst (N4 einige Tausend). Ehrlich sagen, wenn die Volumina fuer D2 zu klein sind.
- Zeitrahmen etwa 150 min.

## Abgabe

- coordination/runden-v3/RUNDE-37/netz-dyn-1/ERGEBNIS.md (Aufbau, Kontrollen, Tabellen, Abgleich D1 bis D5,
  Grenzen) und code/ (lokale Kopie des Pakets) mit Pruefsummen.

## Nachtrag der Leitung (vor dem Start): Superpunkte messen

- Gradverteilung der Ecken je Phase. Ecken mit Grad > 5-faches Mittel als "Superpunkte" zaehlen, ihre Lebensdauer in Sweeps.
- Um jeden Superpunkt: U(1)-Windung der Kantenwinkel (Ladung) und Windung des Ecken-Rahmens (Spin-Vorzeichen). Erwartungen D6 und D7 in der Karte.
