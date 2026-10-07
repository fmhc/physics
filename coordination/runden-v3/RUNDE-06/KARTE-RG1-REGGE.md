# Karte RG-1: Bilden drehende Q-Baelle einen Regge-Turm? (Glied 7 der Spin-2-Kette)

Leitung claude-primary, Zeit vor dem Schreiben gemessen: 2026-09-30 03:02:28 CEST. Status: Hypothese, explorativ (v3).

## Anlass

- Loop-Schwerpunkt: die zwei schwaechsten Glieder der Spin-2-Kette, 10 (Eindeutigkeit) und 7 (nicht Spin 3 oder
  hoeher). Quelle: coordination/art-grenzen-20260921/WARUM-SPIN-2.md, Glied 7 und Nachtrag vom 24.09.
- Nach CEMZ (arXiv:1407.5597, dort nur zitiert, nicht nachgelesen) verlangt jede Aenderung der Drei-Graviton-Kopplung
  einen unendlichen Turm hoeherer Spins. Das ist die String-Bruecke; ihr Kennzeichen sind Regge-Bahnen J ~ alpha' E^2.
- Frage fuer unser Modell: Liefert die Familie drehender Q-Baelle (Windung m, Drehimpuls J = m Q) einen solchen Turm?
  Wenn ja, mit welcher Steigung?

## Hypothese und Gegenhypothese

- **H (Regge):** Entlang der fuehrenden Bahn (kleinste Energie zu gegebenem J, ueber alle m und Q) gilt J ~ E^alpha mit
  alpha = 2.
  - Mechanismus: Grosse m machen den Ball zum duennen Ring mit Radius R ~ m. Seine kleinste Ladung waechst dann wie
    Q_min(m) ~ m (beta = 1).
  - Da E ~ omega Q ~ Q, folgt E_min(J) ~ J/m_max ~ J^(beta/(1+beta)), also J ~ E^((1+beta)/beta) = E^2.
- **Gegenhypothese (Rotor oder linear):** Q_min(m) waechst schneller oder langsamer als linear.
  - beta = 2 gibt alpha = 1,5; beta -> unendlich gibt alpha -> 1 (Ladung dominiert).
  - Bei festem Q ist der Ball ein starrer Rotor, E - E0 ~ J^2/Q. Das ist kein Regge-Verhalten.
- **L1 (kann scheitern):** alpha ist vorab nicht festgelegt; es haengt an Q_min(m), das nur gerechnet bekannt ist.

## Test (2D, eben, klein; lokal auf der Laptop-CPU rechenbar)

- **Radiale Profile:** phi = f(r) exp(i m theta - i omega t) fuer m = 0 bis 8 und omega^2 von 0,5 bis 0,99 (etwa 25 Werte).
- **Integrale:** Q = 2 omega Int f^2 d^2x, E, J = m Q.
  - J = m Q gilt exakt fuer stationaere Loesungen; numerisch pruefen als Codeprobe.
- **Q_min(m):** kleinste Ladung je m; daraus beta aus einem log-log-Fit ueber m = 3 bis 8.
- **Fuehrende Bahn:** E_min(J) ueber alle berechneten (m, omega); alpha aus dem Fit log J gegen log E.
- **Schiessen:** Fuer m != 0 nur die berichtigte Coleman-Regel aus RUNDE-05/r5-2d-a/r5_2d_a.py (Abschnitt 0.2 dort;
  Einschachtelung in ln p). Das alte Schiessen aus tests2d_r3.py ist fuer m = 1 falsch.
- **Gegenproben:**
  - m = 0 gibt die 2D-Werte aus RUNDE-03 (profile_bericht.txt, nur m = 0-Zeilen).
  - Halbe Schrittweite (L3).
  - Ringbild pruefen: Radius des Dichtemaximums gegen m.
- **Stabilitaet ist hier nicht Thema.** Drehende Baelle sind in 2D oft instabil (Teilung, Paket 2D-A). Ein Turm aus
  Resonanzen waere dennoch ein Turm, wie bei Hadronen. Das gehoert in die Deutung, nicht in den Test.

## Latten

- L1: ja (alpha offen)
- L2: m = 0-Anschluss, J = m Q
- L3: halbe Schrittweite
- L4: Drehende Q-Baelle sind Literatur (Volkov und Woehnert 2002; Kleihaus, Kunz und List 2005 in 3D; aus dem
  Gedaechtnis [L?]). Regge-Bahnen von Q-Baellen kennt die Leitung nicht; das ist vor jeder Aussage zu suchen.
- L5: kein direkter Messbezug; hoechstens die Form "Turm mit Steigung alpha' in Modelleinheiten". Das ist eine Bruecke
  als Hypothese, kein Befund zu Glied 7.

## Einfach gesagt

In der Stringtheorie haben drehende Teilchen mehr Energie, je schneller sie drehen, und zwar nach einer festen Regel:
Drehimpuls waechst mit dem Quadrat der Energie. Wir pruefen, ob unsere drehenden Q-Baelle derselben Regel folgen. Sehr
schnell drehende Baelle werden zu Ringen, und Ringe verhalten sich aehnlich wie Strings. Stimmt die Regel, haetten wir
einen Turm immer hoeherer Drehungen, genau das, was die Physik fuer eine Aenderung der Schwerkraft verlangen wuerde.
