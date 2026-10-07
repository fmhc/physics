# BILDUNG-3D: Werden kugelsymmetrische Klumpen in 3D von selbst zu Q-Baellen? (Runde 23)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 21:48:09 CEST (date), vor jedem Lauf.
- Herkunft:
  - BILDUNG-1 (R22): In 2D werden einzelne kleine Gauss-Klumpen in 50 bis 200 Einheiten Q-Baelle; ein grosser Klumpen
    behaelt eine gebundene Wand-Atmung (BILDUNG-2, BILDUNG-LEITER).
  - PAPIER-SCHNITT PS-8: Bildung nur als 2D-Befund fuehren.
  - Das Papier (Anhang "Exploratory concentration") nennt einen echten Bildungstest als offene Aufgabe. Es hat nur eine
    Nicht-Verduennungs-Schranke (E < Q) und einen gezirpten Radiallauf bis T = 32.
- Ableitbarkeitspruefung (Rohdatenprobe):
  - In 3D wurden radiale Laeufe nur mit Ball- bzw. BIC-Startprofilen gerechnet (Codex QBALL-CLOCK, R18 HUELLEN-UHR,
    M2), nicht mit Gauss-Klumpen in M1.
  - Der gezirpte Lauf des Papiers endet bei T = 32.
  - Die Ausgaenge sind nicht ablesbar.
- Explorativ (v3), Hypothesen [H]. Nur kugelsymmetrisch (l = 0); nichtradiale Instabilitaeten sind nicht erfasst.

## Test

- Modell M1 (U = S - S^2 + S^3/2), radial 3D (Laplace psi_rr + 2 psi_r/r, bei r = 0: 6 (psi_1 - psi_0)/dr^2), Leapfrog mit
  Absorberrand. Vorbild ist zeit2d_v2.py (RUNDE-22/bildung-leiter/code/) mit dem exakten Startschritt.
- Familie M1 in 3D: Profile fuer omega^2 von 0,52 bis 0,90 (Schritt 0,01) mit Q_F(omega), E_F(omega), rms-Radius.
- Klumpen psi = A exp(-r^2/(2 s^2)), psi_t = -i w0 psi:
  - (i) Q = Q_F bei omega^2 = 0,60, rms-Radius gleich dem des Familienballs, w0 = omega_F
  - (ii) Breite +30 %, (iii) Breite -30 % (je mit Q = Q_F, w0 = omega_F)
  - (iv) "gross": wie (i), aber gegen den Familienball bei omega^2 = 0,55
- **K0:** Ein exakter Familienball bleibt bis T = 1000 stationaer (Zentraldichte relativ < 1e-8).
- **"auf"** zu T = 250, 500, 1000:
  - |Q_Ball - Q_F(omega_mess)|/Q_F < 10 %. Dabei ist omega_mess die Phasendrehung am Zentrum ueber ein Fenster von 50
    Einheiten, Q_Ball die Ladung innerhalb r < r_sd.
  - Dazu werden berichtet: E/Q gegen die Familie, Atmungsamplitude (Spanne der Zentraldichte im Fenster) und
    Ladungsanteil.
- Zwei Gitter (dr = 0,04 und 0,02); gewertet wird mit dr = 0,02.

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B3D-0 | K0 bestanden | 90 % |
| B3D-1 | (i) ist bei T = 500 "auf" | 60 % |
| B3D-2 | (ii) und (iii) sind bei T = 1000 beide "auf" | 45 % |
| B3D-3 | (iv) ist bei T = 1000 nicht "auf", weil er weiter deutlich atmet (Spanne der Zentraldichte > 5 %) | 55 % |

**Bedeutung (vorab):**
- B3D-1 und B3D-2 treffen ein: M1 ist auch in 3D fuer einzelne kugelsymmetrische Klumpen bildungsfaehig (Stufe 5 im
  Modell, nur l = 0) [H].
- B3D-1 trifft nicht ein: 3D verhaelt sich anders als 2D; Grund beschreiben.
- B3D-3 trifft ein: Wie in 2D behalten grosse Klumpen eine langlebige Atmung.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren), je <= 10 min.
- Plan vor dem ersten echten Lauf einfrieren (Rauchlauf vorher erlaubt). Zeitbox 90 min.
