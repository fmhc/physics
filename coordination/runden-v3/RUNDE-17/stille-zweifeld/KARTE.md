# STILLE-ZWEIFELD: Hat der Q-Ball im Zweifeldmodell stille Stellen? (Runde 17)

- Leitung: claude-primary. Karte, Herleitungsskizze und Vorhersagen geschrieben ab 2026-10-02 09:52:35 CEST (date), vor
  jeder Rechnung.
- Herkunft: BEUTEL-1 (Runde 16). In Codex' Zweifeldmodell M2 baut sich der Ball eine Huelle (chi -> 0 innen) und bleibt
  ein Tropfen.
- Schwerpunkt Q-Baelle: Ueberleben die stillen Stellen (Atmung ohne Abstrahlung), wenn ein zweites Feld mitspielt? Das
  ist die Frage QK-1 ("stille Stellen sind empfindlich gegen weitere offene Kanaele") in einem konkreten Modell.
- Explorativ (v3). Hypothesen [H].

## Modell M2 (wie BEUTEL-1)

L = |d psi|^2 + (1/2)(d chi)^2 - U(S, chi), mit
U = (1/4)(chi^2 - 1)^2 + (1 + chi^2) S - S^2 + S^3/2 und S = |psi|^2.
- Hintergrund: psi = f(r) e^{i omega t}, chi = g(r). Das sind die BEUTEL-1-Loesungen; der Code dort darf gelesen und
  benutzt werden.
- Vakuum: S = 0, chi = 1. Dort haben psi und chi die Masse^2 2, die Schwelle liegt also bei sqrt(2).

## Linearisierung l = 0 (Skizze der Leitung [ES]; vom Agenten selbst herleiten und pruefen)

Ansatz: psi = e^{i omega t} (f + a e^{i rho t} + b e^{-i rho t}) mit a, b reell; chi = g + c cos(rho t).

Mit
- U_S = 1 + g^2 - 2S + (3/2) S^2
- U_SS = -2 + 3S
- U_chichi = 3 g^2 - 1 + 2S
- gemischte Ableitung U_Schi = 2g

ergibt sich:

    [-Lap + U_S - (omega + rho)^2] a + U_SS f^2 (a + b) + g f c = 0
    [-Lap + U_S - (omega - rho)^2] b + U_SS f^2 (a + b) + g f c = 0
    [-Lap + U_chichi - rho^2] c + 4 g f (a + b) = 0

Kanaele im Unendlichen (f -> 0, g -> 1):
- a mit k_a^2 = (omega + rho)^2 - 2
- b mit k_b^2 = (omega - rho)^2 - 2
- c mit k_c^2 = rho^2 - 2

Ein Kanal ist offen, wenn k^2 > 0.

Bereiche (Q-Ball-Fenster 0,728 < omega^2 < 2):
- **E1, genau ein offener Kanal (a):** sqrt(2) - omega < rho < sqrt(2). Hier ist eine stille Stelle generisch moeglich
  (eine Bedingung, wie in M1).
- **E2, zwei offene Kanaele (a und c):** rho > sqrt(2). Eine stille Stelle braucht hier zwei Bedingungen zugleich und
  ist generisch nicht zu erwarten [L?, QK-1].
- **E0:** rho < sqrt(2) - omega, alle Kanaele zu. Dort gibt es gebundene Innenmoden, keine stillen Stellen im engeren
  Sinn.

## Vorgehen

- Verfahren wie LOG-NACHBAU (RUNDE-16/log-nachbau/: HERLEITUNG.md, stille.py duerfen gelesen und erweitert werden).
  Erweitert wird von 2 auf 3 Kanaele.
  - Regulaere Loesungen am Ursprung
  - Abklingen der geschlossenen Kanaele
  - Abstrahlamplitude im offenen Kanal
  - Vorzeichenwechsel und Umlaufzahl
  - Aufloesungsschwelle 0,4 rad. Rundenzahl adaptiv, bis aufgeloest, und im Plan vorab so festgelegt; siehe die Lehre
    aus LOG-NACHBAU.
- In E2: Abstrahlung in beide offenen Kanaele messen. Eine Stelle zaehlt nur, wenn beide Amplituden zugleich
  verschwinden (Minimum der Gesamtabstrahlung unter einer vorab festgelegten Schwelle, die vor dem Lauf an der Numerik
  geeicht wird).
- Gitter: omega^2 von 0,75 bis 1,95 in Zeilen von hoechstens 0,02. rho je Zeile in E1 und in E2 bis 3,0.
- **Kontrollen:**
  - K1: Mit abgeschalteter chi-Kopplung und U = S - S^2 + S^3/2 (M1) findet der eigene Code die bewiesene Stelle
    0,797677 / 1,744618 auf 1e-4, Umlauf -1 aufgeloest.
  - K2: Die M2-Profile treffen BEUTEL-1 (E/Q, Q) auf 1e-4.
  - K3: zwei Gitterstufen je Fund, Lagen auf 1e-4 gleich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S1 | In E1 gibt es mindestens eine stille Stelle (aufgeloester Umlauf +-1, zwei Stufen) | 45 % |
| S2 | In E2 gibt es keine Stelle, an der beide Abstrahlungen zugleich verschwinden | 90 % |
| S3 | Gibt es Stellen in E1, liegen sie auf dem Duennwand-Ast (omega^2 < 1,4), wo die Huelle chi(0) < 0,5 ausgebildet ist | 60 % |
| S4 | Die M1-Stelle hat in M2 keinen stetigen Nachfolger mit nur einem offenen Kanal (rho waere > sqrt(2)) | 75 % |

**Bedeutung (vorab):**
- Trifft S2 ein und S1 nicht: Ein zweites Feld mit offenem Kanal loescht die stillen Stellen. Die stillen Stellen
  waeren dann eine Besonderheit des Einfeld-Modells.
- Trifft S1 ein: Stille Stellen ueberleben, wenn die Huelle die Kanaele passend schliesst. Das waere ein neuer
  Mechanismus [H].

## Rahmen

- Code-Agent, eigener bzw. erweiterter Code. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4, je
  <= 10 min.
- Plan vor dem ersten Lauf einfrieren. Zeitbox 120 min.
