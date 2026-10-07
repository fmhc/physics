# BEUTEL-1: Baut sich der Q-Ball eine Huelle, und ist er dann Tropfen oder Beutel? (Runde 16)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 08:50:32 CEST (date), vor jeder Rechnung.
- Anlass: Finn, 02.10.: "q-balls und hadronenhüllen ist das das gleiche vice versa"; danach "prüfen alles ... weiter
  prüfen und rechnen".
- Chat-Antwort der Leitung (RUNDE-16.md): gleiche Familie, nicht dasselbe. Unser Einfeld-Ball ist bei grosser Ladung
  ein Tropfen (E ~ Q). Ein Beutel gehorcht E ~ Q^(3/4).
- Diese Karte prueft die Aussage selbst und rechnet sie im Zweifeldmodell nach, das Codex am 02.10. vorgeschlagen hat
  (RUNDE-16/two-sides-review/codex/ARBEITSMODELL-V2.md). Dessen zweites Feld chi kann eine Huelle bilden.
- Explorativ nach v3; Hypothesen [H], Literatur aus dem Gedaechtnis [L?].

## Modelle (Kontinuum, 3D, kugelsymmetrisch)

In allen Modellen gilt S = |psi|^2 und psi = f(r) e^{i omega t}; chi = g(r) ist statisch.

- **M1 (Projektmodell, ein Feld):**
  - Lagrangedichte |d psi|^2 - U(S) mit U = S - S^2 + S^3/2. Masse 1.
  - Fenster 1/2 < omega^2 < 1.
- **M2 (Codex-Zweifeldmodell):**
  - Lagrangedichte |d psi|^2 + (1/2)(d chi)^2 - U(S, chi), mit
    U = (1/4)(chi^2 - 1)^2 + (1 + chi^2) S - S^2 + S^3/2 = (1/4)(chi^2 - 1 + 2S)^2 + (1/2) S (S - 2)^2.
  - Vakuum S = 0, chi = 1. Dort hat psi die Masse^2 2 und chi die Masse^2 2.
  - Im Inneren, bei chi = 0, sieht psi genau U(S) aus M1 plus die Konstante 1/4. Das ist eine "Beutelkonstante"
    B = 1/4 [ES].
- **M3 (Kontrolle, Friedberg-Lee-Sirlin-artig):**
  - U = (1/4)(chi^2 - 1)^2 + 2 chi^2 S, ohne Selbstwechselwirkung von psi.
  - Innen (chi = 0) ist psi masselos. Ein Beutel mit B = 1/4 ist dort zu erwarten.

Gleichungen (M2; fuer M1 entfaellt chi, fuer M3 aendert sich U):

    f'' + (2/r) f' = (U_S(f^2, g) - omega^2) f
    g'' + (2/r) g' = U_chi(f^2, g)

Randbedingungen: f'(0) = g'(0) = 0, f -> 0, g -> 1 fuer r -> unendlich, f > 0 ohne Knoten.

Groessen:
- Q = 2 omega Integral f^2 d^3x
- E = Integral [omega^2 f^2 + f'^2 + (1/2) g'^2 + U] d^3x
- Huellenanteil h = Integral [(1/2) g'^2 + (1/4)(g^2 - 1)^2] d^3x / E
- lokaler Exponent p(Q) = d ln E / d ln Q
- S(0) und chi(0)

## Schreibtischrechnung der Leitung (vorab)

- **M1, duenne Wand (omega^2 -> 1/2):**
  - min_S U/S liegt bei S = 1 und ist 1/2. Das gibt E/Q -> 1/sqrt(2) = 0,7071 und Innendichte S(0) -> 1.
  - Ein Tropfen mit Saettigungsdichte, also E ~ Q.
- **M2:**
  - Lokal minimiert chi bei S >= 1/2 auf chi = 0, bei S < 1/2 auf chi^2 = 1 - 2S.
  - Fuer S >= 1/2 ist min U/S = min [1/(4S) + 1 - S + S^2/2]. Das Minimum liegt bei 4S^3 - 4S^2 - 1 = 0, also
    S ~ 1,180, und hat den Wert omega_0^2 ~ 0,7281.
  - Duenne Wand: E/Q -> 0,853, S(0) -> 1,18, chi(0) -> 0.
  - Huellenanteil innen: 0,25 / (2 omega_0^2 S) ~ 0,146.
- **M3:**
  - Innen ist psi frei und masselos, also eine Hohlraummode mit omega ~ pi/R.
  - E = pi Q/R + (4 pi/3) R^3 B, minimiert ueber R. Das gibt E = (4 pi/3)(4B)^(1/4) Q^(3/4) = 4,19 Q^(3/4) und
    Huellenanteil 1/4.
  - Gueltig nur fuer pi/R < sqrt(2), also R > 2,2 bzw. Q > ~24. Die Wanddicke ~ 1/sqrt(2) gibt Korrekturen der Ordnung
    1/R.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B1 | M1: E/Q -> 0,7071 und S(0) -> 1 auf dem Duennwand-Ast (auf 1 %) | 95 % |
| B2 | M1: keine Q^(3/4)-Strecke (p in 0,75 +- 0,05 ueber einen Faktor 3 in Q) | 95 % |
| B3 | M2: Huelle bildet sich: chi(0) < 0,1 bei grossem Q; chi(0) > 0,8 nahe omega^2 -> 2 | 85 % |
| B4 | M2: Duennwand-Grenze E/Q -> 0,853 +- 0,01, S(0) -> 1,18 +- 0,02 | 75 % |
| B5 | M2: Huellenanteil bei grossem Q -> 0,15 +- 0,02, nicht 1/4 | 70 % |
| B6 | M2: keine Q^(3/4)-Strecke (Kriterium wie B2) | 80 % |
| B7 | M3 (Kontrolle): p -> 0,75 +- 0,03, Huellenanteil -> 0,25 +- 0,03, E/Q^(3/4) -> 4,19 auf 15 % beim groessten Q (>= 1000) | 70 % |

**Bedeutung fuer Finns Frage (vorab festgelegt):**
- Gelten B3 bis B6: Der Ball baut sich im Zweifeldmodell eine eigene Huelle (Friedberg-Lee-Struktur), bleibt aber ein
  Tropfen und wird kein Beutel. Die Huelle allein macht ihn nicht zum Hadron-Analogon.
- Gilt B7: Beutelverhalten kommt von einem freien Inhalt in der Huelle, nicht von der Huelle selbst.
- Scheitert B3 (keine Huelle): Die Bruecke Q-Ball / Huelle traegt in diesem Modell nicht.

## Kontrollen

- Zwei Gitter (Schrittweite und Radius) je Modell; Q und E auf 1e-4 relativ gleich.
- M1: bekannte Werte aus dem Projekt nur zum Abgleich am Ende, nicht als Startwerte. Das ist kein Blindtest; der Code
  wird selbst geschrieben.
- Virialprobe je Loesung (Derrick, 3D): Integral f'^2 + (1/2) g'^2 = 3 Integral [omega^2 f^2 - U]. Relativer Fehler
  < 1e-3.
- dE/dQ = omega entlang des Astes (bekannte Q-Ball-Beziehung [L?]); als Kontrolle numerisch pruefen.

## Rahmen

- Code-Agent, eigener Code (numpy/scipy).
- Nur .69 ueber kleintest.sh, Spur cpu6; jeder Aufruf hoechstens 10 min.
- Lokal nur Rauchtests (<= 120 s).
- Plan vor dem ersten Lauf einfrieren. Zeitbox 75 min.
