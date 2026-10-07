# QBALL-LADUNG-1: Geladene Q-Baelle: Gibt es eine groesste Ladung? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:08:07 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn (Eingang vor 04:08:07): "Haben wir ein Teilchenmodell?" Antwort der Leitung: Baukasten, aber die Teile sind nicht verbunden.
    Erste Verbindung: Q-Baelle als elektrische Ladung im Pfeil-Eis.
  - FLUSS-1: Das Pfeil-Eis auf Tetraedern gibt im Grossen ein Coulomb-Feld, also eine U(1)-Eichtheorie [E/L].
  - Hier wird die Ladung des Q-Balls an dieses Feld gekoppelt, zunaechst im Kontinuum, kugelsymmetrisch.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Modell:** M1 (U(S) = S - S^2 + beta S^3, beta = 1/2, S = abs(phi)^2) mit Eichkopplung e an ein U(1)-Feld.
  - Statischer Ansatz phi = f(r) e^(i omega t), A_0(r), A_i = 0.
  - Mit Omega(r) = omega - e A_0(r) [M]:
    - f'' + (2/r) f' + Omega^2 f - U'(f^2) f = 0
    - A_0'' + (2/r) A_0' = -2 e Omega f^2 (Gauss: Ladungsdichte 2 e Omega f^2)
  - Ladung Q = int 2 Omega f^2 d^3x; Energie E = int [Omega^2 f^2 + f'^2 + U + A_0'^2/2] d^3x.
  - Rand: f'(0) = A_0'(0) = 0, f -> 0, A_0 -> e Q/(4 pi r).
  - Vorzeichen und Normierung vor der Rechnung pruefen und im Plan festlegen.
- **Erwartung [L?, nach Lee/Stein-Schabes/Watkins/Widrow 1989 "Gauged Q balls"]:** Die Coulomb-Abstossung im Ball waechst
  mit der Ladung staerker als die Bindung. Deshalb gibt es eine groesste Ladung Q_max(e).
- **Grobe Duennwand-Schaetzung [M]:**
  - Volumenenergie ~ omega_0 Q, Coulomb-Energie ~ e^2 Q^2/R mit R ~ Q^(1/3). Die Coulomb-Energie je Ladung waechst
    wie e^2 Q^(2/3).
  - Sie erreicht die Bindungsluecke m - omega_0 (m = 1, omega_0 = sqrt(1 - 1/(4 beta)) = 0,707) bei
    Q ~ ((m - omega_0)/e^2)^(3/2), also Q_max ~ e^-3.
- **Fuer Finns Bild:** Q-Baelle waeren dann elektrisch geladene Teilchen mit einer Obergrenze fuer ihre Ladung. Riesige
  geladene Klumpen zerreissen an ihrer eigenen Abstossung.

## Test (Code-Agent)

- **Radialer Loeser:** Schiessverfahren oder Relaxation fuer das gekoppelte System f, A_0.
  - Gegen den ungeeichten 3D-Loeser aus REGEL-1 (RUNDE-36/regel-1/code/regel.py, Abgleich mit RUNDE-02) bei e = 0
    pruefen.
- **e-Reihe:** e = 0,005; 0,01; 0,02; 0,05; 0,1; 0,2 (soweit machbar). Je e die Familie ueber omega bzw. Q abtasten: E(Q),
  E/Q, Q(omega), Ende der Familie.
- **Kleines e:** Coulomb-Zusatz Delta E(Q) = E_e(Q) - E_0(Q) bei festem Q.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QL0 | Kontrolle: e = 0 reproduziert den ungeeichten M1-Q-Ball (E und Q bei drei omega) auf 1e-6 relativ | 90 % |
| QL1 | Kleines e (0,005 bis 0,05), festes Q (zwei Werte): Delta E waechst wie e^2 (Steigung im log-log-Bild 2 +- 0,1) | 75 % |
| QL2 | Fuer e = 0,05; 0,1; 0,2 endet die Familie bei einer groessten Ladung Q_max; Q_max ~ e^-p mit p in [2,5; 3,5] | 55 % |
| QL3 | [H] Bei Q_max ist E/Q noch < 1: Der groesste geladene Q-Ball ist noch stabil gegen Zerfall in freie Teilchen | 50 % |

**Bedeutung (vorab):**
- **QL2 trifft ein:** Q-Baelle im Pfeil-Eis waeren geladene Teilchen mit einer groessten Ladung. Das ist die erste
  Verbindung zweier Bausteine (Teilchen und Elektrizitaet).
  - Ob die Grenze bei kleinen oder grossen Ladungen liegt, haengt an e. Ein Vergleich mit echten Teilchen ist damit noch
    nicht moeglich [H].
- **QL3 verfehlt:** Schon vor der Grenze zerfallen grosse geladene Baelle in freie Teilchen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh; Spuren nach freiem Platz (wird beim Start festgelegt);
  je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
- Spaeter, nicht hier: zwei geladene Baelle im Gitter-Pfeil-Eis (Abstossung bzw. Anziehung mit Vernichtung).

## Festlegungen vor der Rechnung (2026-10-04 04:15:42 CEST, Leitung)

- **Wer rechnet:** die Leitung selbst (alle drei Agentenplaetze belegt; Finn: "Weiter", Eingang vor diesem Eintrag). Spur p4000a als CPU-Lauf,
  ohne Codeagent, ohne Gegenleser des Codes (wird so vermerkt).
- **QL0-Bezug:** Tabelle RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_bericht.txt, Test 4 (3D radial, beta = 1/2).
  - omega^2 = 0,60: f0^2 = 1,088133, Q = 2,87318e3, E = 2,33259e3
  - omega^2 = 0,70: f0^2 = 1,135060, Q = 473,413, E = 428,641
  - omega^2 = 0,80: f0^2 = 1,044572, Q = 186,110, E = 181,912
  - Die Tabelle hat 6 bis 7 gueltige Stellen. Die Schwelle ist deshalb die halbe letzte gedruckte Stelle (relativ), aber
    mindestens 1e-6. Das ist eine Klarstellung der Kartenschwelle wegen der Druckgenauigkeit, vor jeder Rechnung.
- **Familienparameter:** Omega_0 = g(0) = omega - e A_0(0). Je e eine Folge von Omega_0^2 zwischen 0,98 und 0,505.
  omega = g(unendlich) folgt aus der Rechnung.
- **QL1:** Delta E bei Q = 300 und Q = 1000 (Interpolation von E(Q) auf dem Ast mit dQ/dOmega_0 < 0). Steigung aus
  e = 0,005; 0,01; 0,02; 0,05 per Ausgleich in log-log.
- **QL2:** Q_max = groesstes Q der berechneten Familie je e. "Endet" heisst: Q faellt danach wieder bzw. es gibt keine
  Loesung mehr. p aus dem Ausgleich ueber e = 0,05; 0,1; 0,2.
- **QL3:** E/Q am Punkt Q_max, fuer jedes der drei e.
- **Kontrolle (beschreibend):** dE/dQ gegen omega laengs der Familie.
