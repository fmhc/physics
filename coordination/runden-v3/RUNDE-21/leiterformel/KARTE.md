# LEITERFORMEL: Erklaert die Phasenbedingung der Innenwelle alle Sprossenabstaende fuer l = 0, 1, 2? (Runde 21)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 18:36:07 CEST (date), vor jeder Rechnung dieser Karte.
- Herkunft:
  - Runde 18, Schreibtisch [H]: Delta R ~ pi/k_innen, k_innen aus dem a-b-Block mit S0 und omega an der Stelle.
    Wandkurve k = 0: 2,37 gegen gemessen 2,41; k = 1: 2,07 gegen 2,11.
  - SPROSSEN-VORAB (R20) und SPROSSEN-L1L2 (R21): Die Abstaende schrumpfen langsam nach aussen; die Regel mit
    schrumpfendem Abstand trifft 2,6-mal genauer.
  - Ziel: ein geschlossener Baustein der Gesamtformel. Eine Sprosse je Phasenzuwachs pi der Innenwelle [H].
- **Ueberlegung der Leitung (Schreibtisch, vor der Rechnung):** Zwischen zwei Sprossen aendert sich nicht nur R, sondern
  auch omega(R) und damit k_innen. Die Bedingung sollte deshalb fuer die Phase Phi(R) = k_innen(R) R gelten, nicht fuer
  pi/k allein: Phi(R_n+1) - Phi(R_n) = pi. Bei l >= 1 kommt asymptotisch ein fester Versatz -l pi/2 hinzu, der in der
  Differenz herausfaellt.
- Explorativ (v3), Hypothesen [H]. Nachtraegliche Erklaerung vorhandener Daten (Latte L4), keine neue Vorhersage von
  Lagen.

## Test

- Grundlage: alle bekannten stillen Stellen samt (omega^2, rho, R, Kurve) fuer
  - l = 0: RUNDE-18/huellen-leiter, RUNDE-19/huellen-leiter-3, RUNDE-20/sprossen-vorab
  - l = 1: RUNDE-19/huellen-dipol, RUNDE-21/sprossen-l1l2
  - l = 2: RUNDE-20/huellen-quadrupol, RUNDE-21/sprossen-l1l2
- k_innen an jeder Stelle aus dem a-b-Block wie in Runde 18 (Code dort nachlesen, unveraendert uebernehmen): S0 =
  Inneramplitude des Hintergrunds, omega, rho der Stelle.
- **K0:** Die Runde-18-Zahlen (2,37 fuer k = 0, 2,07 fuer k = 1 an denselben Stellen) werden mit der eigenen Umsetzung
  wiedergefunden, auf 0,01.
- Je Paar benachbarter Sprossen auf derselben Kurve: Delta Phi = k_innen(R_n+1) R_n+1 - k_innen(R_n) R_n und
  Delta Phi / pi. Zusaetzlich zum Vergleich pi/k_innen (Mittel beider Stellen) gegen den gemessenen Abstand.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LF0 | K0 bestanden | 85 % |
| LF1 | l = 0, Paare mit R_n >= 15: Delta Phi / pi = 1 auf +-3 % bei mindestens 80 % der Paare | 50 % |
| LF2 | l = 1 und l = 2 (alle Paare mit R_n >= 10): ebenso bei mindestens 70 % der Paare | 40 % |
| LF3 | Delta Phi trifft pi besser als pi/k_innen den Abstand (kleinere mittlere relative Abweichung, l = 0) | 60 % |
| LF4 | Die Restabweichung hat bei mindestens 80 % der Paare dasselbe Vorzeichen (systematisch, z. B. eine Wandphase) | 65 % |

**Bedeutung (vorab):**
- LF1 und LF2 treffen ein: Die Leitern fuer l = 0, 1, 2 folgen einer Phasenbedingung der Innenwelle [H, im Modell].
  Das waere ein geschlossener Baustein der Gesamtformel.
- LF1 trifft nicht ein: Das Halbwellenbild ist nur qualitativ; die Restabweichung wird beschrieben.

## Rahmen

- Code-Agent. Kleine Rechnungen (Hintergrund S0 an den Stellen, k_innen) nur auf der .69 ueber kleintest.sh, Spuren cpu
  bis cpu4 und cpu6, je <= 10 min.
- Plan vor der ersten Rechnung einfrieren. Zeitbox 75 min.
