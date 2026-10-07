# LEITER-3D-PRAEZ: Plan (Runde 13, explorativ)

- Code-Agent im Auftrag der Leitung claude-primary. Beginn 2026-10-01 19:08:31 CEST (date). Plan geschrieben ab
  19:22:44 CEST (date), nach den lokalen Rauchtests (Abschnitt 8), vor jedem .69-Lauf. Zeitbox 75 min (bis 20:23:31).
- Arbeitsordner lokal: coordination/runden-v3/RUNDE-13/leiter3d-praez/; .69: /home/fmh/fmhc-physics-remote/runde13-leiter3d-praez/.
- Markierungen: [K] Wortlaut der KARTE, [A] Auslegung/Festlegung des Code-Agenten (nicht von der Leitung),
  [L] Zusatz der Leitung im Auftrag (nicht in der Karte).

## 1. Regel, Kontrollen und Vorhersage (Wortlaut der KARTE, bindend, unveraendert)

### Positivkontrollen [K]

- K1: die bewiesene Stelle l = 0, n = 1 (omega^2 = 0,797677, rho = 1,744618) auf 1e-4, Umlauf +-1 auf beiden Stufen.
- K2: n = 6 mit dem neuen Verfahren bei 0,56940 +- 2e-4 (Vorzeichenwechsel, Umlauf aufgeloest).
- Verfehlt K1 oder K2: nicht auswertbar.

### Regel je Stelle n = 7 bis 10 [K]

- **Gesehen:** Aufgeloester Umlauf +-1 auf beiden Stufen und ein Vorzeichenwechsel von s zwischen benachbarten Zeilen. Die
  Lage liegt auf beiden Stufen innerhalb +-3e-4 (omega^2) der Polsuch-Lage oben und stimmt zwischen den Stufen auf 1e-4.
- **Nicht gesehen:** In +-1e-3 um die Polsuch-Lage kein Vorzeichenwechsel auf beiden Stufen, alle Rechtecke aufgeloest
  mit Umlauf 0, Kernwachstum am Kandidaten < 1e8.
- **Unentschieden:** alles andere, auch Kernwachstum > 1e8 oder ein nicht aufgeloestes Rechteck.
- Vorzeichen des Umlaufs: Die bisherige Regel sagt n gerade +1, n ungerade -1 (RUNDE-08). Das wird nur berichtet und ist
  keine Bedingung.

### Vorhersage der Leitung (vor jedem Lauf) [K]

- K1 und K2 bestehen: ~85 %.
- n = 7 und 8 gesehen: je ~70 %.
- n = 9 und 10 gesehen: je ~55 %.
- Wenn gesehen: Abstand zur Polsuch-Lage < 1e-4.

### Polsuch-Lagen "oben" (KARTE Z. 9 bis 13) [K]

| Stelle | Polsuch-Lage (Karte) | zum Vergleich DATENPAKET (abgeleitet) | Re rho am Polsuch-Minimum (Keim rho0) |
|---|---|---|---|
| n = 7 | ~0,5598 | 0,5598497 | 1,5897567 (bei 0,5598) |
| n = 8 | ~0,5526 | 0,5526199 | 1,5826358 (bei 0,5526) |
| n = 9 | ~0,5470 | 0,5469426 | 1,5772052 (bei 0,5470) |
| n = 10 | 0,5424 | 0,5424 (Formel, "interpoliert") | 1,57178 (rho_b 1,5723075 bei 0,5425 minus 5,3 * 1e-4) |

- [A] Massgeblich fuer die Regel sind die Kartenwerte 0,5598 / 0,5526 / 0,5470 / 0,5424. Die DATENPAKET-Werte werden nur
  berichtet.

## 2. Auslegung der Regel, festgelegt vor jedem Lauf [A]

- **Zielast:** je Zeile die Nullstelle von L(y_b), die rho_ref(x) = rho0 + Steigung * (x - x_Pol) am naechsten liegt,
  innerhalb +-0,02. "s" ist L(y_a) an dieser Nullstelle. "Vorzeichenwechsel zwischen benachbarten Zeilen" heisst
  s_i * s_(i+1) < 0 auf dem Zielast.
- **Lage eines Wechsels:** lineare Interpolation von s zwischen den beiden Zeilen (omega*^2), ebenso rho*.
- **Umlauf +-1:** Rechteck aufgeloest (groesster Phasensprung < 0,4 rad) und |abs(Umlauf) - 1| < 0,1. Umlauf 0:
  |Umlauf| < 0,1.
- **Kernwachstum am Kandidaten:** das groessere Kernwachstum (Feld "wachstum" aus direkt_m, max ueber U, V, U', V' bei
  r_m durch Startbetrag bei r = h, beide regulaeren Loesungen) an den Zielast-Nullstellen der beiden Zeilen um den
  Wechsel; ohne Wechsel an den beiden Zeilen um die Polsuch-Lage. **Fenstermaximum:** groesstes Kernwachstum ueber alle
  Abtastpunkte des ganzen rho-Fensters aller Zeilen (Lauf).
- **"auch Kernwachstum > 1e8 oder ein nicht aufgeloestes Rechteck"** lese ich als Bedingung fuer alle Ausgaenge (strenge
  Lesart, wie RUNDE-08: "Ab einem Kernwachstum ueber ~1e8 gilt der Lauf als nicht entscheidbar"):
  - "gesehen" verlangt zusaetzlich Kernwachstum am Kandidaten <= 1e8 auf beiden Stufen und dass alle gerechneten
    Rechtecke der Stelle aufgeloest sind.
  - Die mildere Lesart (nur die zwei woertlichen Bedingungen) wird zusaetzlich berichtet, entscheidet aber nicht.
  - Offene Frage an die Leitung: welche Lesart gemeint ist.
- **"Nicht gesehen" ohne Wechsel:** Dann gibt es kein Rechteck "um einen Wechsel". Ich lege je Stufe ein Rechteck um die
  Polsuch-Lage (alle 9 Zeilen, rho-Mitte = Zielast interpoliert bei x_Pol). "Alle Rechtecke" sind dann diese beiden.
- **Vollstaendigkeit:** Eine Stelle ist nur auswertbar, wenn beide Stufen alle 9 Profile haben; sonst unentschieden.
- **K1 bestanden:** auf beiden Stufen ein Wechsel auf dem Zielast mit |omega*^2 - 0,797677| <= 1e-4 und
  |rho* - 1,744618| <= 1e-4, Rechteck aufgeloest, Umlauf +-1.
- **K2 bestanden:** auf beiden Stufen ein Wechsel mit |omega*^2 - 0,56940| <= 2e-4, Rechteck aufgeloest, Umlauf +-1
  (strenger als der Wortlaut "Umlauf aufgeloest": ich verlange auch +-1).
- Umsetzung: Kommando `regel` in bic2_3d_praez.py; es liest die praez.json beider Stufen und gibt den Ausgang aus.

## 3. Code

- bic2_3d_praez.py = Kopie von RUNDE-07/bic2/bic2.py (sha256 ee1ef6d226e8ec2c262e40a6d0e1b571a2a6fe40d334831f8e4ccb0856df12ce),
  Aenderungen mit "PRAEZ3D" markiert, Diff in bic2_3d_praez.diff. Physik unveraendert (Profile, Gleichungen,
  direkt_m-Rechnung, Pluecker-Newton, lin_multi mit r_m = Median R_halb und R aus f_rand).
- Aenderungen:
  1. direkt_m gibt zusaetzlich "la_terme" aus (groesster Einzelterm von Omega(y_a, z2) mal |nz|), nur Auswertung.
  2. Kommando `praez` (Abschnitt 4), Kommando `regel` (Abschnitt 2), neue Argumente.
- Ohne die neuen Kommandos verhaelt sich der Code wie bic2.py.

## 4. Verfahren je Stelle und Stufe (ein Aufruf `praez`)

- **Zeilen:** 9 Zeilen omega^2 = x_Pol + (k - 4) * 2,5e-4, k = 0 .. 8, also x_Pol +- 1e-3. Alle 9 Profile in einem
  Stapel (lin_multi: gemeinsames R und r_m).
- **rho-Abtastung je Zeile:**
  - grob: 400 Punkte gleichabstaendig im ganzen Fenster [1 - omega + 0,002, 1 + omega - 0,002] (Abstand ~3,7e-3);
  - dicht: 401 Punkte in rho_ref(x) +- 0,02 (Abstand 1e-4).
- **Direkte Nullstellensuche von L(y_b)** (wie AFM-KANAL-2, KARTE: "oder direkte Nullstellensuche"): jede
  Vorzeichenklammer von L(y_b) auf dieser Abtastung wird mit Illinois verfeinert (alle Klammern aller Zeilen in einem
  Stapel), bis die Klammer < 1e-13 * max(1, rho) ist, hoechstens 80 Schritte. s = L(y_a) wird exakt an der letzten
  Stelle gerechnet (keine Interpolation), dazu Rest L(y_b), Kernwachstum, Ausloeschung = la_terme / |s|.
- **Paarung:** Nullstellen benachbarter Zeilen werden gepaart (wechselseitig naechste, gleiche Richtung von dL(y_b)/drho,
  Abstand < 0,03); Wechsel von s auf anderen Aesten werden berichtet. Der Zielast wird zusaetzlich auf Paarung geprueft
  ("ast_konsistent").
- **Rechteck um jeden Wechsel des Zielasts** zwischen Zeile i und i + 1: omega^2-Seiten = Zeilen max(0, i - 3) bis
  min(8, i + 4); rho-Mitte rho*; halbe Hoehe drho = max(0,01; 2 |d rho_b/d omega^2| * halbe Breite), hoechstens 0,03;
  60 Punkte je rho-Seite, dann bis zu 30 Halbierungsrunden auf den rho-Seiten (Schwelle 0,3 rad wie bic2).
  Aufgeloest: groesster Phasensprung < 0,4 rad. Dazu Umlauf aus der Kreuzungszaehlung als Gegenprobe (nicht
  entscheidend). Ohne Wechsel: ein Rechteck um die Polsuch-Lage (Abschnitt 2).
- **Zusatz (nicht Regel):** Pluecker-Pole am Zielast (newton_m, Start rho_b - 1e-5 i), nur wenn die Zeit reicht.
- **Zwischenspeichern:** praez.json und praez_bericht.txt nach den Profilen, der Abtastung, den Nullstellen, den Aesten,
  jedem Rechteck und den Polen.

## 5. Gitterstufen

- **h = 0,04 und h/2 = 0,02** (lineare ODE; Profile auf h/2 = 0,02 bzw. 0,01; f_rand nach FRAND: 1e-8 bzw. 1e-6).
- Begruendung [A]: Laufzeit. Ein Profil kostet auf der .69 bei h = 0,02 etwa 18 s (RUNDE-12, 2D). Bei h = 0,01 kaemen
  9 Profile allein auf ~320 s, ein Aufruf naehme mehr als die 10-min-Grenze. h = 0,02 ist die Stufe der Polsuche
  (DATENPAKET) und damit direkt vergleichbar; h = 0,04 ist die grobere Stufe. Grenze: Eine Stufe h = 0,01 fehlt.

## 6. Laufliste (.69, nur Spuren cpu und cpu2 [L]; je Aufruf --budget 500, RuntimeMaxSec 600)

| Phase | Spur cpu | Spur cpu2 |
|---|---|---|
| 1 Kontrollen | k2-h002 (~6 min), dann k1-h004 (~2 min) | k1-h002 (~4 min), dann k2-h004 (~3 min) |
| Gate | regel-k1, regel-k2 (je Sekunden); nur wenn beide "bestanden": weiter | - |
| 2 Stellen | n7-h002, n8-h004, n9-h002, n10-h004 (~6 + 3 + 7 + 4 min) | n7-h004, n8-h002, n9-h004, n10-h002 (~3 + 6 + 4 + 7 min) |
| Auswertung | regel-n7, regel-n8, regel-n9, regel-n10 | - |

- Alles in einem einmaligen Starter start.sh (per nohup von Hand, kein Dienst). Gemeinsame Argumente und Keime dort:
  - K1: --x0 0.797677 --rho0 1.744618 --rho-steig 0.4049; K2: --x0 0.56940 --rho0 1.5991684 --rho-steig 2.8
  - n = 7: 0.5598 / 1.5897567 / 3.3; n = 8: 0.5526 / 1.5826358 / 3.9; n = 9: 0.5470 / 1.5772052 / 4.6;
    n = 10: 0.5424 / 1.57178 / 5.3 (Steigungen aus den Polsuch-Tripeln; nur Mitte des dichten Fensters).
- Geschaetzte Gesamtdauer: Phase 1 ~9 min, Phase 2 ~20 min.
- Faellt ein Aufruf aus (rc != 0, Zeit): die Stelle ist unentschieden bzw. "nicht gerechnet"; kein Nachlauf ohne
  eingefrorenen Nachtrag.

## 7. Eigene Vorhersagen des Code-Agenten (vor jedem .69-Lauf; nach den lokalen Rauchtests, siehe 8) [A]

- K1 und K2 bestehen: 0,85.
- n = 7 gesehen: 0,85. **Nicht blind:** Der Rauchtest (3 Zeilen, h = 0,04) zeigte schon einen Wechsel bei 0,559848 mit
  aufgeloestem Umlauf -1 und Kernwachstum am Kandidaten 2,3e5.
- n = 8 gesehen: 0,75; n = 9: 0,6; n = 10: 0,45. Hauptrisiko: Kernwachstum am Kandidaten waechst mit r_m (n = 7: r_m
  ~12, Kernwachstum 2,3e5; Schaetzung e^(1,15 * Delta r_m)): n = 8 ~2e6, n = 9 ~1e7, n = 10 ~7e7, also nahe 1e8. Nach
  der strengen Lesart (Abschnitt 2) wird n = 10 dann leicht unentschieden.
- Wenn gesehen: Abstand zur DATENPAKET-Lage < 3e-5; zur Kartenlage < 1e-4 (ausser n = 10: < 1e-4 zu 0,5424, Erwartung
  0,54238 +- 3e-5 aus u-Schritt 2,30).
- Umlauf: n gerade +1, n ungerade -1 (wie K1 -1, n = 7 im Rauchtest -1): 0,8.

## 8. Rauchtests (lokal, System-python3 mit torch 2.10, 1 Thread, nice 19, timeout 118 s; ungueltig fuer die Regel)

- rauch1 (K1, h = 0,08, 3 Zeilen, 60 + 21 rho-Punkte): 20,0 s, rc = 0. Wechsel bei 0,79767368 / 1,74461649, Umlauf -1,
  aufgeloest (0,293 rad).
- rauch2 (n = 7, h = 0,04, 3 Zeilen, 100 + 41 rho-Punkte): 51,0 s, rc = 0. Profile je 6,9 s, Nullstellensuche 16 s
  (22 Schritte), Rechteck 14 s (19 Runden). Wechsel bei 0,55984822 / 1,58991995, Umlauf -1, aufgeloest (0,298 rad),
  Kernwachstum am Kandidaten 2,29e5, Fenstermaximum 1,43e7, Ausloeschung 6,5e6.
- Regel-Kommando zweimal auf diesen Dateien (gleiche Datei fuer beide Stufen): laeuft, Ausgaben plausibel.
- Hochrechnung .69 (etwa 1,3-mal langsamer als lokal, aus RUNDE-12: 18 s je Profil bei h = 0,02): Aufruf h = 0,04
  ~3 min, h = 0,02 ~6 min. Budget 500 s mit Reserve 150 s nach den Profilen; Pole entfallen bei Zeitnot.
