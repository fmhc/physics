# AETHER-UHR-1: Merkt eine Uhr aus zwei Wellensorten, dass sie sich durchs Netz bewegt? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 23:39:12 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn ~23:28 "Weiter experimentieren gedanklich"; Gedankenexperiment GE1 (RUNDE-36/GEDANKENEXPERIMENTE.md).
  - ZUFALLSNETZ-1: Querwellen richtungsfrei, Laengswelle ~1,7-mal schneller.
  - NETZ-C-1: Kinks verkuerzen sich mit der Netzgeschwindigkeit.
  - Dossier: Die Engstelle ist ein gemeinsamer Lichtkegel fuer alle Anregungen.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Aufbau** (1+1D, zwei Felder):
  - Feld A: unser M1, komplex, Grenzgeschwindigkeit c_A = 1. Ein grosser 1D-Q-Ball ist ein "Beutel" mit zwei Waenden;
    seine Laenge ist das Lineal. Seine innere Phase e^(i omega t) ist die A-Uhr.
  - Feld B: reell, Grenzgeschwindigkeit c_B, Masse m_B aussen. Die Kopplung -g abs(A)^2 B^2 senkt die B-Masse im
    Beutel, also hat B dort gebundene Hohlraummoden. Das ist die B-Uhr (Frequenz Omega_B).
  - Langsame Beschleunigung des Beutels auf v ueber ein schwaches Feld auf die A-Ladung (wie QBALL-GITTER-1, aber feines
    Gitter, kontinuumsnah). B ist neutral und wird nur mitgetragen.
- **Kinematik** [M, Lorentz-Aether]:
  - Der Beutel verkuerzt sich mit gamma_A (Laenge L/gamma_A).
  - Die A-Uhr geht mit 1/gamma_A.
  - Eine Hohlraummode mit Wellengeschwindigkeit c_B in einem mit v bewegten Hohlraum der Laenge L' hat die Frequenz
    ~ (c_B/L') (1 - v^2/c_B^2).
  - Also Omega_B(v)/Omega_B(0) ~ gamma_A/gamma_B^2. Das Verhaeltnis der Uhren ist
    R(v) = Omega_B/omega_A ~ gamma_A^2/gamma_B^2 ~ 1 + v^2 (1/c_A^2 - 1/c_B^2).
- **Folge:**
  - c_B = c_A: R(v) ist konstant. Ein Beobachter im Beutel merkt seine Bewegung nicht (Relativitaet).
  - c_B ungleich c_A: R(v) aendert sich mit v^2. Ein Uhrenvergleich zeigt die Bewegung gegen das Netz (wie
    Hughes-Drever- bzw. Kennedy-Thorndike-Versuche) [L].
- **Messbezug** [L]: Uhrenvergleiche begrenzen solche Unterschiede der Grenzgeschwindigkeit zwischen Sektoren auf etwa
  1e-17 bis 1e-20 (Standardmodell-Erweiterung, Datentabellen Kostelecky/Russell).
  - Mit der Bewegung gegen den Mikrowellenhintergrund verlangt das abs(1 - c_A^2/c_B^2) < ~1e-11 bis 1e-14.

## Test (Code-Agent)

- 1D, kontinuumsnahes Gitter (h <= 0,05), Felder A (M1, beta = 1/2) und B (c_B, m_B, g), Code-Basis RUNDE-35/qball-gitter-1/.
- Grosser Beutel (duennwandiger 1D-Q-Ball, Laenge >= 20). B in der untersten gebundenen Mode, kleine Amplitude (keine
  merkliche Rueckwirkung; pruefen).
- Drei Faelle: c_B = 1,00 (Kontrolle), 1,15 (elastisches Minimum) und 1,70 (Zufallsnetz). Je Endgeschwindigkeit
  v = 0,2, 0,4, 0,6.
- Gemessen:
  - Beutellaenge
  - omega_A aus der Phase im Beutelinneren
  - Omega_B aus der B-Schwingung im Beutel
  - R(v)/R(0)
- Beschleunigung langsam genug, dass die Mode adiabatisch folgt (pruefen: Wiederholung mit halber Beschleunigung).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| U0 | Kontrolle c_B = 1: R(v)/R(0) = 1 innerhalb 1e-3 fuer v bis 0,6; Beutellaenge ~ 1/gamma innerhalb 1 % | 80 % |
| U1 | c_B = 1,15: R(v)/R(0) - 1 = v^2 (1 - 1/c_B^2) innerhalb 20 % (Sollwerte 0,0098 / 0,039 / 0,088 bei v = 0,2 / 0,4 / 0,6) | 65 % |
| U2 | c_B = 1,70: dasselbe Gesetz innerhalb 20 % (Sollwerte 0,026 / 0,105 / 0,235) | 60 % |
| U3 | Die Beutellaenge verkuerzt sich mit gamma_A, nicht mit gamma_B (in allen Faellen innerhalb 1 %) | 75 % |

**Bedeutung (vorab):**
- U0 bis U3 treffen ein: Eine Welt aus einem Netz mit zwei Wellengeschwindigkeiten verraet ihre Bewegung durch
  Uhrenvergleiche, mit genau dem berechneten v^2-Gesetz.
  - Die gemessenen Grenzen verlangen, dass alle Sektoren auf 11 bis 14 Stellen dieselbe Grenzgeschwindigkeit haben.
  - Fuer Finns Netz heisst das: Licht und Materie muessen ueber dieselbe Wellensorte laufen.
- U1 verfehlt: Rueckwirkung oder Nichtadiabatik verfaelschen die einfache Kinematik; beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (nicht cpu, cpu2, cpu5, cpu6, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
