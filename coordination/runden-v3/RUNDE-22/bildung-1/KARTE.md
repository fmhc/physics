# BILDUNG-1: Wird ein einzelner Klumpen von selbst zum Q-Ball? (Runde 22)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 19:01:37 CEST (date), vor jedem Lauf.
- Herkunft:
  - KF-5 (R6, R20): Tropfen aus der 2D-Geburt verschmelzen, bevor sie abrunden; nie "auf".
  - KF-EICH (R21): Der Klassifikator sagt bei exakten Q-Baellen sicher "auf" (48 von 48). "Auf" heisst aber nur, dass Q
    zu omega passt.
  - Offene Frage der Stufe 5 (bildungsfaehig): Laeuft ein **einzelner**, nicht passender Klumpen ohne Verschmelzen auf
    die Familie zu?
- Ableitbarkeitspruefung vor den Vorhersagen (Lehre R21): Einzelne Klumpen wurden im Projekt fuer M1 in 2D nicht
  gerechnet; die Ausgaenge sind aus vorhandenen Dateien nicht ablesbar.
- Explorativ (v3), Hypothesen [H]. Minibudget: Laeufe je hoechstens 10 min.

## Test

- Modell M1 (sextisch), 2D, Integrator und Klassifikator aus RUNDE-06/kf5 (kf5_geburt.py), unveraendert importiert, wie
  in KF-EICH (RUNDE-21/kf-eich/kf_eich.py als Vorbild).
- Anfangszustand: ein Gauss-Klumpen psi = A exp(-r^2/(2 s^2)), psi_t = i w0 psi. Q und Breite sind festgelegt gegen den
  Familienball bei omega^2 = 0,60 (Q_F, Radius R_F aus familie_2d_m0.json):
  - (i) Q = Q_F, s so, dass der Ladungsradius gleich R_F ist, w0 = omega_F
  - (ii) Q = Q_F, s 30 % groesser
  - (iii) Q = Q_F, s 30 % kleiner
  - in (ii) und (iii) A und w0 so, dass Q = Q_F und w0 = omega_F (A folgt)
- Box so gross, dass bis T = 1000 keine Ladung den Absorberrand erreicht, sonst Box vergroessern und dokumentieren.
  Beide Gitter wie in Runde 6.
- **K0:** Ein exakter Familienball im selben Aufbau bleibt bis T = 200 "auf" und "rund".
- Klassifikation zu T = 100, 250, 500, 1000; dazu Q im Ball (Anteil der Anfangsladung), omega, E/Q, Rundheit.

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B0 | K0 bestanden | 90 % |
| B1 | (i) ist bei T = 500 "auf" und "rund", auf beiden Gittern | 65 % |
| B2 | (ii) und (iii) sind bei T = 1000 beide "auf" und "rund", auf beiden Gittern | 50 % |
| B3 | In allen drei Faellen behaelt der Ball bei T = 1000 mindestens 80 % der Anfangsladung | 60 % |

**Bedeutung (vorab):**
- B1 und B2 treffen ein: Einzelne Klumpen laufen auf die Familie zu. M1 ist in 2D fuer isolierte Klumpen
  bildungsfaehig (Stufe 5, im Modell) [H]. Das "nie auf" in KF-5 lag dann am Verschmelzen bzw. an der Zeit.
- B1 trifft nicht ein: Auch ein einzelner, gut passender Klumpen erreicht die Familie bis T = 500 nicht. Stufe 5 ist
  fraglich; Grund beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (bei Belegung p4000b), je <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 75 min.
