# KOVARIANZ-EPS-1: Ist die 4D-Antwort auf Verformung glatt in der Amplitude, und liegt die Anomalie am Neuvernetzen? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 17:04:02 CEST (date), vor jeder
  Rechnung.
- **Anlass:**
  - KOVARIANZ-KUGEL-1: Auf dem S^4-Netz ist die Antwort auf eine konforme l = 2-Verformung 11- bis 21-mal zu gross, sie
    waechst mit N und faellt etwa linear statt quadratisch mit der Amplitude.
  - KOVARIANZ-2D-GEGENPROBE (RUNDE-37/kovarianz-2d-gegenprobe/ERGEBNIS.md): Derselbe Codepfad (n-allgemein, mit n = 4
    bitgleich zu kovarianz.py) zeigt auf S^2 nichts davon (Schranke 0,6 bis 1,3 % der 4D-Groesse je Punkt). Der
    gemeinsame Code ist damit als Ursache ausgeschlossen.
  - Kandidaten nach dem Agenten:
    - laengenabhaengige 4D-Steifigkeit
    - 4D-Delaunay-Neuvernetzung (60 % neue Simplizes gegen 13 % in 2D)
    - Grobheit (Sehnenvolumen 20 % statt 0,6 % zu klein)
  - Vorschlag des Agenten: eps = +-0,025 in 4D. Bleibt das Vorzeichen bei beiden gleich, ist die Antwort in eps nicht
    glatt.
  - KOVARIANZ-KUGEL-1 hat neu vernetzt (PLAN Z. 25, S4: "Neu bauen [F]").
- **Ableitbarkeitsprobe [M]:**
  - Eine glatte, kovariante Wirkung gibt Delta Gamma gerade in eps, fuer kleine eps proportional eps^2. Ein Glied
    proportional abs(eps) oder ein gleiches Vorzeichen bei +eps und -eps ist mit Glaette unvertraeglich.
  - Neuvernetzung schaltet die Verbindungen sprunghaft um. Sie kann einen nicht glatten Anteil erzeugen, der mit der
    Zahl der Umschaltungen (also mit N) waechst.
  - Mitgenommene Verbindungen (nur die Laengen aendern sich) sind glatt in eps, solange kein Simplex entartet.
  - Ob die Anomalie damit verschwindet, ist nicht ableitbar.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [H] Hypothese.

## Auftrag (Code-Agent)

1. Lesen: KOVARIANZ-KUGEL-1 (ERGEBNIS, PLAN, VORAB, code, Nachtraege), KOVARIANZ-2D-GEGENPROBE (ERGEBNIS, Code). Code
   kopieren, nicht aendern.
2. **Zwei Bauweisen in 4D:**
   - (a) wie KOVARIANZ-KUGEL-1, mit Neuvernetzung
   - (b) mitgenommene Verbindungen: dasselbe runde Netz, nur die Punkte verschoben und die Laengen neu berechnet; die
     Zahl entarteter bzw. umgeklappter Simplizes zaehlen und melden
3. **Amplituden** eps = -0,1, -0,05, -0,025, +0,025, +0,05, +0,1 (konform l = 2); dazu die Moebius-Nullprobe. N = 1000,
   2000, 4000; gepaarte Saaten wie bisher.
4. **Messgroessen:** Delta Gamma(eps); gerader und ungerader Anteil (Delta(eps) + Delta(-eps))/2 bzw.
   (Delta(eps) - Delta(-eps))/2; Steigung in log abs(eps); N-Abhaengigkeit je Bauweise.
5. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KE0 | Kontrollen: Bauweise (a) reproduziert die KOVARIANZ-KUGEL-1-Werte bei eps = -0,1 im Rahmen der Fehler; Moebius-Nullprobe in (b) innerhalb 3 SE um null | 85 % |
| KE1 | [H] Bauweise (a): Bei +eps und -eps hat Delta Gamma dasselbe Vorzeichen (nicht glatt), mindestens bei eps = 0,025 und 0,05 | 60 % |
| KE2 | [H] Bauweise (b): Antwort glatt (gerader Anteil mit Steigung 1,7 bis 2,3 in log abs(eps); ungerader Anteil unter 20 % des geraden) | 55 % |
| KE3 | [H] Bauweise (b): Der gerade Anteil haengt nicht von N ab (Aenderung 1000 auf 4000 unter 15 % bzw. 2 SE) | 40 % |
| KE4 | [H] Bauweise (b): Der gerade Anteil trifft das Einstein-Vorzeichen und liegt innerhalb Faktor 3 der Kontinuumsvorhersage aus dem gemessenen B | 25 % |

**Bedeutung (vorab):**
- **KE1 und KE2 treffen ein:** Die 4D-Anomalie ist ein Neuvernetzungs-Effekt. Mit mitgenommenen Verbindungen ist die
  Antwort glatt; ob sie Einstein ist, sagen KE3 und KE4.
- **KE2 verfehlt:** Auch ohne Neuvernetzung ist die Antwort nicht glatt. Dann liegt es an der 4D-Steifigkeit bzw. an der
  Grobheit, und das 4D-Kugelnetz ist so nicht als Einstein lesbar.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh. Spuren cpu und cpu4 (frei seit KOVARIANZ-2D-GEGENPROBE). Je
  Lauf <= 10 min, 1 Thread. Zeitbox 150 min.
