# KOVARIANZ-2D-GEGENPROBE: Gibt dieselbe Verformungs-Vorschrift auf der 2D-Kugel die bekannte Polyakov-Antwort, oder waechst sie mit N? (Runde 41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 16:11:27 CEST (date), vor jeder
  Rechnung. Ordner angelegt 16:09:59.
- **Anlass, KOVARIANZ-KUGEL-1 (RUNDE-37/kovarianz-kugel-1/ERGEBNIS.md):**
  - Auf dem S^4-Netz reagiert Gamma auf konforme Verformungen mit Einsteins Vorzeichen, aber 11- bis 21-mal zu stark.
  - Die Antwort waechst mit N (-0,51 / -0,61 / -0,76 bei N = 1000 / 2000 / 4000) und faellt etwa linear statt quadratisch
    mit der Amplitude.
  - Die Moebius-Nullprobe ist -0,0017 +- 0,0002 (8,9 SE, aus der Volumenzuordnung je Simplex).
  - Der Agent empfiehlt vor jeder Deutung eine 2D-Gegenprobe mit derselben Vorschrift.
- **Warum 2D trennt [L, M]:**
  - Auf S^2 ist das Einstein-Glied topologisch (Gauss-Bonnet); es antwortet auf keine Verformung.
  - Die Antwort von Gamma = ln det des Laplace-Operators auf eine konforme Verformung sigma ist die Polyakov-Wirkung:
    endlich, unabhaengig von N, fuer kleine Amplitude quadratisch.
  - Das Projekt hat den 2D-Polyakov-Koeffizienten schon gemessen: 1,075 P +- 0,071 P bzw. 0,92 P (INDUZIERT-DICHTE-2D
    und -GROB, Torus) [P].
  - Waechst die Antwort auf S^2 mit N oder faellt sie linear mit der Amplitude, liegt der Fehler in der Vorschrift bzw.
    im Code und nicht in der 4D-Physik.
- **Ableitbarkeitsprobe:**
  - Die Polyakov-Antwort fuer die gewaehlte Verformung ist vorab rechenbar und gehoert als Zahl mit Fehler in VORAB.md;
    dabei sind der Flaecheninhalt (fest oder nicht) und die Nullmode zu beachten.
  - Nicht ableitbar ist, ob die Huellen-Vorschrift samt Volumenzuordnung in 2D sauber skaliert. Das ist die Frage.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Lesen:**
   - RUNDE-37/kovarianz-kugel-1/ (ERGEBNIS, PLAN, VORAB, code/kovarianz.py, kugel2.py)
   - RUNDE-37/induziert-dichte-2d/ERGEBNIS.md und die GROB-Karte (Polyakov auf dem Torus)
   - RUNDE-37/induziert-kugel-1/ (Kugel-Bau)
2. **Bau:**
   - dieselbe Vorschrift in 2 statt 4 Dimensionen:
     - Punkte nach Flaeche auf S^2
     - Huellen- bzw. Delaunay-Netz
     - Laengenregel und Volumenzuordnung je Simplex wie in kovarianz.py
     - Verformung durch dieselbe Art fester glatter Abbildung
   - Verformungen: Moebius-Nullprobe (l = 1), konform l = 2, Amplitudenreihe (mindestens drei Amplituden), N = 1000,
     2000, 4000 und, wenn moeglich, 8000.
   - Variante ohne Volumenzuordnung je Simplex als Diagnose, beschreibend.
3. **VORAB.md:** Polyakov-Vorhersage je Verformung und Amplitude mit dem Projekt-Koeffizienten.
4. **Plan, Rauchlauf, Einfrieren wie ueblich.**

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KG0 | Moebius-Nullprobe innerhalb 3 SE um null oder kleiner als 5 % des l = 2-Signals | 70 % |
| KG1 | [H] Konform l = 2: Antwort quadratisch in der Amplitude (Steigung von ln abs(Delta Gamma) gegen ln Amplitude zwischen 1,8 und 2,2) | 55 % |
| KG2 | [H] Konform l = 2: Antwort unabhaengig von N (Aenderung von N = 1000 auf 4000 innerhalb 2 SE bzw. unter 10 %) | 50 % |
| KG3 | [H] Betrag trifft die Polyakov-Vorhersage innerhalb 30 % | 40 % |

**Bedeutung (vorab):**
- **KG1 und KG2 treffen ein:** Die Vorschrift ist in 2D sauber. Die Anomalie in 4D (Wachstum mit N, lineare Amplitude)
  ist dann 4D- bzw. gitterspezifisch, und KOVARIANZ-KUGEL-1 gilt: auf diesem 4D-Netz nicht Einstein.
- **KG1 oder KG2 verfehlt:** Die Vorschrift oder der Code erzeugt die Anomalie auch dort, wo die Physik sie verbietet.
  Dann ist das 4D-Ergebnis nicht als Physik lesbar; der Bau muss vor jeder Deutung berichtigt werden.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh. Spuren cpu (frei seit GUERTEL-1) und cpu4 (geteilt mit
  EINE-WELT-LOCH-1; der Lock regelt die Reihenfolge). Je Lauf <= 10 min, 1 Thread. Zeitbox 120 min.
