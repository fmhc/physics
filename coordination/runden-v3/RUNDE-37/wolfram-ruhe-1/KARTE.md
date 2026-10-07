# WOLFRAM-RUHE-1: Verschwindet das versteckte Ruhesystem eines Wolfram-Kausalgraphen im Grossen? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 17:22:24 CEST (date), vor jeder
  Rechnung.
- **Herkunft:** Kartenvorschlag K1 aus WOLFRAM-SCAN-L (RUNDE-37/wolfram-scan-l/DOSSIER.md, Abschnitt Unterscheidungspunkte
  U1, Z. 108). Bezug: Finns Weiche, festes Netz mit Ruhesystem (A) gegen Ereignisnetz (B).
- **Stand:**
  - Wolfram-Kausalgraphen haben im Kleinen beschraenkte Valenz, also ein Ruhesystem (Seite A) [M, Agent; S Gorard A34].
  - Gorard rettet die Lorentz-Invarianz nur durch Vergroeberung.
  - Bombelli/Henson/Sorkin (2006) [L]: Ein lokal endliches Netz mit beschraenkter Valenz kann nicht im Kleinen
    Lorentz-invariant verteilt sein. Das ist vorab bekannt.
- **Messgroesse (gegen Boost):**
  - Fuer Intervalle [p, q] im Kausalgraphen: N = Zahl der Ereignisse dazwischen, L = laengste Kette, r = L / (2 sqrt N).
  - Bestimmt wird r als Funktion der "Schraegstellung" eta des Intervalls gegen die Aktualisierungs-Blaetterung
    (Generationsschritte als Zeit; Schraegstellung ueber das Verhaeltnis der Nullrichtungen).
  - Kontrollen [M, L]:
    - Poisson-Streuung in 1+1: r -> 1 fuer jedes eta (Lorentz-invariant; Brightwell/Gregory)
    - regelmaessiges Nullgitter: r = cosh(eta) (Ruhesystem sichtbar)
- **Ableitbarkeitsprobe:**
  - Beide Kontrollen sind ableitbar.
  - Fuer den Wolfram-Graphen ist r(eta) nicht ableitbar. Ob das Ruhesystem im Grossen verschwindet, hat niemand gemessen
    (WOLFRAM-SCAN-L: "nirgends gemessen").
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Literatur, [S] Quelle, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Regel:** die lorentzartige 2D-Regel R2 aus der Technical Introduction (S. 284; lokale Kopie in
   RUNDE-37/wolfram-scan-l/quellen/, Seitenkarte SEITENKARTE.md) nachbauen. Ersetzungsregel, Aktualisierungsreihenfolge
   und Kausalgraph wie dort definiert.
   - Pruefen, ob der Kausalgraph von der Reihenfolge abhaengt (Kausalinvarianz).
   - Pruefen, ob das Netz wie 1+1 waechst (Kegelvolumen ~ t^2). Sonst abbrechen und melden.
2. **Messung:** r(eta) fuer Intervalle mit N = 50 bis 2000 bei mehreren eta, mit Fehlern; dazu beide Kontrollen mit
   denselben Programmen.
3. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WR0 | Kontrollen: Poisson r innerhalb 5 % von 1 und ohne eta-Trend; Nullgitter r = cosh(eta) auf 2 % | 85 % |
| WR1 | Der R2-Kausalgraph waechst wie 1+1 (Kegelvolumen-Exponent 1,8 bis 2,2) | 55 % |
| WR2 | [H] Wenn WR1: r(eta) steigt mit eta mindestens halb so stark wie cosh(eta) (Ruhesystem sichtbar), auch bei den groessten N | 60 % |

**Bedeutung (vorab):**
- **WR2 trifft ein:** Wolframs Netz behaelt sein Ruhesystem auch im Grossen, wie ein festes Gitter. Fuer Finns Weiche
  steht es dann neben K-A (Seite A) und braucht dieselbe Abstimmung fuer ein gemeinsames Tempo.
- **WR2 verfehlt:** Das Ruhesystem verschwindet im Grossen; Gorards Lesart haelt in 1+1 [H].

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und cpu7 (frei seit STRICH-NETZ-1). Je Lauf
  <= 10 min, 1 Thread. Zeitbox 150 min.
