# SCHWEBUNGSUHR-2: Laufen schwach gekoppelte Q-Ball-Uhren auseinander? Vorab gewertetes Abstandsraster (Runde 23)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 21:53:08 CEST (date), vor jedem Lauf.
- Herkunft: SCHWEBUNGSUHR (R23).
  - Bei D = 6,6 und 4,6 verschmelzen die Baelle; der groessere frisst den kleineren.
  - Nur der Zusatzlauf D = 14,6 (nicht gewertet) war schwach gekoppelt: Die Schwebung war ueber 3000 Einheiten auf 0,2 %
    stabil, aber 15 % schneller als der freie Taktunterschied. Anfangs flossen ~2 % Ladung vom kleinen zum grossen Ball, und
    die Takte rueckten auseinander.
  - Finns Frage nach "Zeit aus Bewegungsdifferenz": Entsteht durch Kopplung eine gemeinsame Zeit, oder laufen die Uhren
    auseinander?
- **Ableitbarkeitspruefung:** Bekannt ist nur der Punkt D = 14,6. Er wird nur berichtet, nicht gewertet. Vorzeichen und
  Abstandsgesetz fuer die anderen Abstaende sind nicht ablesbar.
- Explorativ (v3), Hypothesen [H]. Laeufe je <= 10 min.

## Test

- Code der Vorkarte (RUNDE-23/schwebungsuhr/code/schwebung1d.py), unveraendert bis auf den Abstand.
- omega_1^2 = 0,60 (groesserer Ball, Q_1 ~ 3,69), omega_2^2 = 0,65; ruhend, Phasenlage 0.
- Abstaende D = 8, 10, 12, 18, 22 (gewertet) und 14,6 (nur berichtet); T = 3000. Ein Gitter wie in der Vorkarte; bei D = 12
  zusaetzlich das zweite Gitter (L3).
- Messgroessen:
  - Q_1 und Q_2 Anfang/Ende
  - Delta omega(t) = omega_2 - omega_1 in Fenstern, gegen den freien Wert Delta omega_frei
  - Schwebungsfrequenz am Mittelpunkt
  - Schwerpunktabstand Anfang/Ende
  - Verschmelzen (dasselbe Kriterium wie die Vorkarte, und zusaetzlich ein Dichtebild-Pruefpunkt)

## Vorhersagen (vor jedem Lauf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| T0 | Fuer alle D >= 10 ohne Verschmelzen fliesst Ladung vom kleinen zum grossen Ball (Q_1 steigt bis T = 3000) | 75 % |
| T1 | r(D) = (Delta omega_Ende - Delta omega_frei)/Delta omega_frei ist positiv und faellt mit D etwa exponentiell. Steigung von ln r gegen D zwischen -1,22 und -0,61, also zwischen -2 kappa und -kappa (kappa ~ 0,61) | 50 % |
| T2 | Bei keinem D ruecken die Takte um 10 % oder mehr zusammen (keine Synchronisation) | 80 % |
| T3 | Bei D = 8 verschmelzen die Baelle bis T = 3000 | 55 % |

**Bedeutung (vorab):**
- T0 und T2 treffen ein: Schwach gekoppelte Q-Ball-Uhren laufen auseinander statt zusammen ("reich wird reicher" ueber
  Ladungsfluss). Eine gemeinsame Zeit entsteht in diesem Modell nur durch Verschmelzen [H, 1D].
- T1 trifft ein: Der Effekt ist ein Schwanz-Ueberlapp-Effekt (exponentiell im Abstand).
- T2 trifft nicht ein: Es gibt einen Abstandsbereich mit Synchronisation; Grund beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren), je <= 10 min.
- Plan vor dem ersten echten Lauf einfrieren. Zeitbox 60 min.
- Danach ein kurzer Literaturcheck im Volltext (arXiv per WebFetch): Ist das Auseinanderlaufen der Takte bzw. die
  Ladungsdrift zum groesseren Ball bekannt (z. B. Battye/Sutcliffe 2000, Axenides u. a. 2000, Bowcock/Foster/Sutcliffe 2009)?
