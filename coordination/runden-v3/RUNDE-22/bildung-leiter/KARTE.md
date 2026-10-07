# BILDUNG-LEITER: Abklingen der stillen Mode an und neben der Sprosse, und welche Moden ein Klumpen anregt (Runde 22)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 20:14:48 CEST (date), vor jeder Rechnung. Grundlage: DENKNOTIZ.md daneben.
- Rohdatenprobe (Lehre R21/R22):
  - Breiten der stillen Mode bei n = 7 liegen nur im Frequenzbereich vor (RUNDE-12/leiter2d-praez).
  - Zeitbereichs-Abklingraten in 2D sind nicht gerechnet.
  - BILDUNG-2 hat S_max nur alle 10 Einheiten; die Spektren sind daraus nicht bestimmbar.
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min.

## Test

- **Radiale Zeitentwicklung** (l = 0) des Einfeldmodells M1 in 2D (U = S - S^2 + S^3/2), Absorber am Rand, zwei
  Gitter.
  - Hintergruende: exakte Familienprofile bei omega^2 = 0,529266 (Sprosse n = 7), 0,52905 und 0,52950 (je etwa 2,2e-4
    daneben) sowie 0,5310 (etwa zwischen n = 6 und 7; im Plan aus der Leiter festlegen).
- **Arm M (Mode):** Startstoerung = die stille Mode bzw. ihr Pol-Eigenvektor (rho ~ 1,556) aus dem Runde-12-Code mit
  kleiner Amplitude (linearer Bereich). Gemessen wird die Abklingrate der Modenamplitude (Projektion oder Fit von
  |Amplitude|(t)) bis T = 2000, gegen |Im rho| aus Runde 12.
- **Arm G (glatter Klumpen):** Gauss-Klumpen vom Typ (i) aus BILDUNG-1, gegen dieselben Familienpunkte. Zentraldichte alle
  0,5 Einheiten bis T = 2000.
  - Spektrum in Fenstern: gebundene Moden (rho < 1 - omega) gegen ueberschwellige.
  - Energieanteil in der stillen Mode (rho ~ 1,556).
- **K0:** Die exakte Familienloesung ohne Stoerung bleibt bis T = 2000 stationaer (Zentraldichte relativ < 1e-6).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L0 | K0 bestanden | 85 % |
| L1 | Arm M: Die gemessene Abklingrate trifft \|Im rho\| aus Runde 12 an den Punkten daneben (0,52905 und 0,52950) innerhalb Faktor 2; an der Sprosse liegt sie unter 1e-5 | 60 % |
| L2 | Arm M bei 0,5310 (zwischen den Sprossen): Abklingrate >= 3e-3 (H1 statt H2) | 55 % |
| L3 | Arm G: Das Spektrum wird von gebundenen Moden (rho < 1 - omega) beherrscht; der Energieanteil der stillen Mode bleibt unter 1 % | 70 % |

**Bedeutung (vorab):**
- L1 trifft ein: Die Zeitentwicklung bestaetigt die V-foermige Breite unabhaengig von der Frequenzrechnung (Gegenprobe L2
  der Leiter in 2D).
- L2 trifft ein: Zwischen den Sprossen klingt die Mode schnell ab (H1), und Naehe zur Sprosse bestimmt die Lebensdauer.
- L2 trifft nicht ein: H2, allgemein schwache Abstrahlung.
- L3 trifft ein: Glatte Klumpen regen die stille Mode kaum an. Ihr langes Nachschwingen ist gebundene Wand-Atmung (H3),
  keine Spur der Leiter.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu bis cpu4 bzw. cpu6, je <= 10 min.
- Plan vor der ersten Rechnung einfrieren. Zeitbox 90 min.
