# GERAHMTER-FADEN-1: Kommen 2-pi-Vorzeichen und Austauschvorzeichen am Fadenende aus derselben Regel, wenn das Rahmenfeld die Faeden rahmt? (Runde 50, Ziel Schritt b, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 19:03:43 CEST (date), vor jeder Rechnung.
- **Herkunft:** Vorschlag aus GERAHMTER-FADEN-L (DOSSIER.md, Abschnitt 10), von der Leitung uebernommen. Wortlaut,
  Modelle und Erwartungen stammen aus dem Dossier; die Wahrscheinlichkeiten sind die des Dossiers.
- **Projektsuche der Leitung** (19:03, mit Sperrausschluessen):
  - Hebungsbuchhaltung, kurzer Lift, Knotenkonvention, w2: nur IDEEN-SPIN-ZEIT I1 (kurzer Lift) und das Dossier.
  - Vorlagen: TWIST-PYRO-1 und TWIST-SPIN-1 (Code), Z2-SCHUTZ-1/-2 (Rahmenfeld).
- **Frage:** Kommen auf Finns Diamantnetz das 2-pi-Vorzeichen am Fadenende und das Austauschvorzeichen aus derselben
  Regel, wenn die Fadenoperatoren mit dem Rahmenfeld statt mit einer festen Projektion gerahmt werden?

## Modell

- Exakt rechnen, GF(2)/Z4 wie TWIST-PYRO-1/-SPIN-1, Rahmen als klassischer Hintergrund.
- Netz: Diamant n = 2, 3 (Code aus TWIST-PYRO-1/-SPIN-1); Pyrochlor-Kanten optional.
- Rahmenklassen:
  - R0 gleichfoermig (q_i = 1)
  - R1 glatt zufaellig mit groesstem Bindungswinkel theta_max in {15, 30, 45, 60} Grad
  - R2 Kern um 360 Grad verdreht (kleine Kugel wie Z2-SCHUTZ)
- Varianten:
  - A feste Projektion (Kontrolle)
  - B Levin/Wen, Lesart S, mit knotenweiser Richtung n_i = q_i z q_i^-1
  - C wie A, dazu das Kopplungsgesetz (Fluss von a je kleinster Schleife = Hebungsvorzeichen des Rahmens) und die
    Hebungsbuchhaltung im Fadenoperator
- Messgroessen:
  - M1 Vertraeglichkeit: antivertauschende Paare in B bei R1, je theta_max.
  - M2 Austausch: T-Kreuzungs-Vorzeichen in allen Tripeln.
  - M3 Spin: Vorzeichen eines Zustands mit einem Ende am Knoten i unter einer oertlichen 2-pi-Drehung von q_i (drei
    Achsen, darunter n_i), relativ zum Zustand ohne Ende.
  - M4 Punktgruppe: (C2)^2 am Einzelende unter T, Rahmen per Konjugation (R0) mitgedreht.

## Erwartungen (vor jeder Rechnung)

| Nr | Vorhersage | Art | Wahrsch. |
|---|---|---|---|
| GFR0 | Kontrolle: A gibt TWIST-PYRO-1/-SPIN-1 bitgleich wieder (0 antivertauschende Paare, -1 in allen Tripeln, (C2)^2 = +1) | vorab [P] | 90 % |
| GFR1 | [H] B ist bei R1 mit theta_max <= 30 Grad vertraeglich (0 Paare), bei 60 Grad nicht (> 0 Paare) | offen | 45 % |
| GFR2 | [H] B liefert in M3 kein achsenunabhaengiges -1 (ueberall +1 oder achsenabhaengig) | Skizze, scheiterfaehig | 70 % |
| GFR3 | C liefert in M3 -1 mit Ende und +1 ohne, fuer alle drei Achsen; M2 in C gleich A | Skizze [M] | 75 % |
| GFR4 | M4 bei R0: (C2)^2 = +1 in A, B und C (geordneter Rahmen = feste Rahmung) | Skizze [M] | 70 % |

- Vorab ableitbar: GFR0 ganz; GFR3 und GFR4 als Skizze. Echt offen und in beide Richtungen scheiterfaehig: GFR1 und
  GFR2.
- **Bedeutung (vorab, aus dem Dossier):**
  - GFR2 und GFR3 treffen ein: Der Spin kommt nur aus der Hebungsbuchhaltung, die Statistik aus dem Twist. Das sind zwei
    getrennte Regeln. Folgekarte GERAHMTER-FADEN-2 mit Quantenrotor (j <= 1/2) je Knoten; die Huepfer transportieren den
    Rahmen.
  - GFR2 scheitert: Die knotenweise Levin/Wen-Rahmung traegt selbst Spin.
- **Kontrollen:** ohne Ende; Achse = n_i (B muss +1 geben); 4-pi-Drehung gibt +1; Gegenprobe G1 aus TWIST-PYRO-1.

## Rahmen

- Code-Agent ohne Einfrieren und Leser (Finn: einfach machen).
- Spuren cpu8 bis cpu10 ueber kleintest.sh, je Lauf hoechstens 10 min; df vor jedem Lauf.
- Synthetisch, keine Messdaten.
