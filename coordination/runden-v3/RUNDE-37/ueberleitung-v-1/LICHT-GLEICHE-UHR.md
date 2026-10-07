# LICHT-GLEICHE-UHR: Licht und Schwerewellen auf V mit derselben Uhr (Folgeauftrag zu UEBERLEITUNG-V-1, ohne Karte)

- Auftrag der Leitung (Finn: "einfach machen und ausprobieren"): kein Plan-Einfrieren, keine Vorhersagen, kein frischer Leser.
- Start 16:12:03 CEST, Text ab 16:23:39 CEST (date). Laeufe 14:17:24 bis 14:22:00 UTC auf der .69, nur cpu5 und cpu6, 9 Starts
  (kontrolle, dec, w4d fein 2x, aw, diag, w4d grob 2x, aw2), alle rc 0, laengster 24,8 s. Synthetisch, linear um flach.
- Code: licht/licht.py (Laeufe kontrolle, dec, w4d fein, aw mit Stand licht.py.lauf1, sha 08b7437f; w4d grob und aw2 mit
  Stand licht.py, sha 81685008), licht/diag_w4d.py; unveraendert importiert uv.py und hi.py samt Abhaengigkeiten.
  Ergebnisse in licht/lauf-69/ (aw2.json = Endstand).

## Uhr und Einheiten

- **Schwerewellen (Nachtrag nt3 von UEBERLEITUNG-V-1):** omega ist konjugiert zur Zeit T der Ecken, T = h (n_t + hb). Die
  Zeltstange hat die 4D-Laenge h je Schritt. Also ist T die **Eigenzeit der Zeltstangen**, Hintergrund-Lapse N = 1 in T
  (Koordinatenzeit = Eigenzeit). Der Lapse ist n = relative Laengenaenderung der Zeltstange, Bedingung C = -c/2.
  Laengeneinheit: kubische Kante a = 1 von V. "Tempo 1" = Lichtkegel der 4D-Metrik in diesen Einheiten.
- Die Setzung N0 = Wurzel 8 der Grundgleichung v2.5 kommt hier nicht vor (N0 = 1); sie multipliziert alle Tempi gleich.
- **Licht W4D (Hauptweg):** 4D-Maxwell auf **demselben** Zeltnetz V mal Zeit (Whitney-1-Formen, F je 4-Simplex konstant,
  S = Summe Vol |F|^2 / 2). Gleiche 3+1-Zerlegung wie die Schwerkraft: Schichtkanten a, Zeltstangen phi = A_T,
  Diagonal-Reste per Schur, Grenze h -> 0. Die Uhr ist damit nicht gesetzt, sie kommt aus denselben Zeltstangen.
- **Licht DEC (zweiter Weg, Code aus HOEHE-ISOTROP-1, Kammermitte):** 3+1-Form *1 A'' = -d1^T *2 d1 A mit Lapse 1 in T.
  Hier ist die gleiche Uhr eine Setzung (Lapse des Lichts = Lapse der Zeltstangen), nicht abgeleitet.
- Warum beide: W4D beantwortet "dieselbe Uhr" ohne Setzung, DEC ist der Lichtoperator des Projekts.

## Ergebnis (kl -> 0 durch Anpassung omega^2/k^2 = mu/(kl)^2 + w0 + w2 (kl)^2 + w4 (kl)^4 ueber kl = 0,005 bis 0,1; 13 Richtungen x 2 Zweige; c = Wurzel w0; b = w2/(2 w0) = relative Tempoaenderung je (kl)^2)

| Groesse | Schwerewelle (2 masselose Moden) | Licht DEC | Licht W4D |
|---|---|---|---|
| c bei kl -> 0 (min bis max) | 0,99999999992 bis 1,00000000006 | 0,99999999992 bis 1,00000000012 | 0,99999984 bis 1,00000015 |
| c_Licht / c_Schwerewelle | - | 0,99999999992 bis 1,00000000015 | 0,99999984 bis 1,00000015 |
| Isotropie: Spanne von c | 1,4e-10 | 2,0e-10 | 3,0e-7 |
| b, Bereich ueber Richtungen und Zweige (Mittel) | -0,0207 bis -0,0113 (-0,0180) | -0,0180 bis -0,0120 (-0,0160) | -0,0191 bis -0,0162 (-0,0181) |
| Doppelbrechung, max abs(b_1 - b_2) | 0,0057 ([100]) | 0,00082 | 0,00080 |
| Tempounterschied zur Schwerewelle bei gleichem kl, b_L - b_GW je Richtung (Zweigmittel) | - | +0,0018 bis +0,0022 | -0,0022 bis +0,0009 |
| Scheinmasse mu (Kontrolle, soll 0 sein) | abs <= 2e-14 | abs <= 2,1e-14 | -4,7e-10 bis -9,8e-11 |

- b je Richtung (Zweig 1 / Zweig 2), Auszug aus aw2.json:

| Richtung | Schwerewelle | Licht DEC | Licht W4D |
|---|---|---|---|
| [100] | -0,0170 / -0,0114 | -0,0121 / -0,0121 | -0,0163 / -0,0163 |
| [110] | -0,0206 / -0,0163 | -0,0169 / -0,0161 | -0,0188 / -0,0180 |
| [111] | -0,0199 / -0,0199 | -0,0180 / -0,0180 | -0,0190 / -0,0191 |
| [321] | -0,0203 / -0,0166 | -0,0167 / -0,0162 | -0,0187 / -0,0181 |

- Zusatzzeilen (beschreibend, nach Sicht gewaehlt):
  - W4D wurde zuerst mit h = 2^-8 bis 2^-14 gerechnet wie die Schwerkraft. Rundung (waechst wie 1/h^2) erzeugte dort
    eine Scheinmasse mu bis 9,1e-8 und ohne Massenterm c = 1,00038 bis 1,00092.
  - Endstand daher h = 2^-4 bis 2^-10 (quartisch, Licht hat keine Nulldurchgaenge im Gitterrest) mit Massenterm.
  - Ohne Massenterm gibt dieselbe Folge c = 0,9999953 bis 0,9999991.
  - Bei Schwerewelle und DEC verschieben sich die c-Bereiche mit oder ohne Massenterm um <= 1e-10.
- Kontrollen: Whitney exakt fuer lineares A auf <= 3,6e-13; Laurent-Form gegen Bloch-Summe <= 2,5e-16; 4D-Eichnullvektoren
  <= 1,4e-17 (h = 1 und 2^-14). Der Grenz-Eichvektor (d0 chi, i omega chi) ist Nullvektor bis O(h) (Diagnose diag_w4d.py).
  W4D: an allen 78 k zwei Photonen mit Luecke < 0,006, keine wachsende Mode, Masse K positiv definit.
- [K] GW170817 (abs(dv/v) < 1e-15, f ~ 100 Hz, k ~ 2,1e-6 1/m): Mit abs(b_L - b_GW) ~ 0,002 folgt kl < 7e-7, also mittlere
  Kantenlaenge l < 0,34 m. Das ist keine harte Grenze an das Netz.

## Konstruktion oder Ergebnis?

- Die Gleichheit bei kl -> 0 folgt aus dem Aufbau: Beide Sektoren sind Diskretisierungen euklidisch invarianter Wirkungen
  auf derselben 4D-Metrik, und beide geben gleichmaessige Felder exakt wieder. Deshalb laufen beide langwellig mit dem c
  dieser Metrik.
  - Licht: Whitney exakt (oben) bzw. die DEC-Identitaeten, Summe *2 A^2 n n^T = Vol I.
  - Schwerkraft: Regge-Kontinuumsgrenze auf V, REGIME-K-2 und Nachtrag.
- Echt gerechnet ist:
  - Auf V verdirbt nichts diese Gleichheit; es entsteht keine Gitterkonstante, die die Tempi verschiebt, bis 1,5e-7 (W4D)
    bzw. 1,5e-10 (DEC).
  - Die Schwerkraft braucht dafuer h unter den Nulldurchgaengen des Gitterrests (bei kleinem k knapp unter 2^-8).
  - Bei endlichem kl unterscheiden sich die Tempi um etwa 0,002 (kl)^2.

## Einfach gesagt

Wir haben Licht und Schwerewellen auf Finns gefuelltem Netz mit derselben Uhr laufen lassen: der Laenge der Zeltstangen,
mit denen jede Ecke in der Zeit nach oben springt. Fuer sehr lange Wellen sind beide gleich schnell, auf zehn Stellen genau
beim Licht nach Projektcode und auf sieben Stellen beim Licht, das wir selbst im 4D-Zeltnetz gebaut haben. Das ist so
gebaut und keine Ueberraschung; neu ist nur, dass das Netz nichts daran verdirbt und dass sich die Tempi bei kurzen Wellen
um etwa zwei Tausendstel mal (Kantenlaenge mal Wellenzahl) zum Quadrat unterscheiden.

---
Abgabe: 2026-10-05 16:23:39 CEST (date).
