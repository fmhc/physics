# INDUZIERT-KUGEL-1: Welches Vorzeichen hat die induzierte Schwerkraft eines Gitter-Skalars auf einem exakt kovarianten 4D-Zufallsnetz? (Runde 39)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 10:39:11 CEST (date), vor jeder
  Rechnung. Vorlage: Abschnitt 8 von RUNDE-37/induziert-g-l/DOSSIER.md (Vorschlag des feldforschers); Aufbau, Messgroesse
  und Vorhersagen KU0 bis KU4 von dort uebernommen, Wahrscheinlichkeiten und Bedeutungssaetze von der Leitung.
- **Anlass:**
  - INDUZIERT-DICHTE-4D: Mit "Zahl = Volumen" auf dem 4D-Torus hat die konforme Mode die Steifigkeit c = +0,111 +- 0,045
    (Dichte 1) bzw. -0,017 +- 0,045 (Dichte 0,5). Das ist nicht Einsteins Vorzeichen.
  - INDUZIERT-G-L: Bei freien Feldern setzt der Regler das Vorzeichen von G_ind; kein Satz verbietet ein negatives G fuer
    ein P1-Delaunay-Netz. Offen ist, ob das Torus-Vorzeichen eine Eigenschaft des kovarianten Reglers ist oder ein
    Artefakt der Torus-Konstruktion (Delaunay in Koordinaten, Laengenregel sp, Dichteskalierung 1,7 SE daneben).
- **Projekt-grep (Leitung, vor dieser Karte):** keine S^4-Rechnung im Projekt; nur Fehltreffer (Potenzen S^4 in der
  Q-Ball-Familie, 4-Kugel als Quellgebiet in kausal4d.py).
- Kennzeichen: [M] Mathematik, [ES] eigener Schluss, [H] Hypothese.

## Aufbau (aus dem Dossier, Abschnitt 8.2)

- **4D:** N Poisson-Punkte, gleichverteilt auf S^4 vom Radius a mit (8 pi^2/3) a^4 = N (Dichte 1). Konvexe Huelle in
  R^5 = sphaerisches Delaunay (Qhull). P1-Steifigkeit wie in INDUZIERT-1 bzw. INDUZIERT-DICHTE-4D (Gram-Formel; Code in
  RUNDE-37/induziert-dichte-4d/code/ wiederverwenden).
  - Regel C (Sehne): Kantenlaengen = Sehnen; jedes Simplex echt euklidisch.
  - Regel S (sp-Analog): je Simplex alle Laengen mit e^(sigma_T) skalieren, e^(4 sigma_T) = Jacobi-Faktor der
    Radialprojektion am Schwerpunkt.
  - Gamma = 1/2 log det' K, dazu Gamma_M = 1/2 log det'(M^-1 K).
- **Referenz:** flacher 4D-Torus gleicher Dichte und gleichen N (dichte4d.py, Grundnetz bei s = 0).
- **2D-Kontrolle:** S^2 (Huelle in R^3) gegen T^2 (zufall2d.py), gleiche N.
- **N:** 4D 1000, 2000, 4000, 8000; 2D 4000, 16000, 64000; je 4 bis 6 Saaten. Der Rauchlauf misst Zeit und
  Saatstreuung; reicht die Streuung nicht, mehr Saaten statt neuer Groessen.

## Messgroesse und Schreibtisch (aus dem Dossier, Abschnitt 8.3; vor dem Einfrieren pruefen)

- Modell [M]: Gamma_S(N) - Gamma_T(N) = beta sqrt(N) + gamma ln N + delta + O(N^(-1/2)).
- Im kovarianten Ensemble: Int sqrt(g) R auf S^4 = 32 pi^2 a^2 = 61,6 sqrt(N) bei Dichte 1, also beta = 61,6 B = 10,26 c.
  Die Leitung hat 61,6 und c = 6 B (konforme Mode: Int sqrt(g) R ~ 6 Int (grad sigma)^2) am Schreibtisch nachgerechnet.
- **Vorzeichen-Lesart:** beta > 0 heisst B > 0, also negatives G_ind (anti-Einstein, wie der Torus). beta < 0 heisst
  Einsteins Vorzeichen.
- **Vorab ableitbar, keine Messung:** Volumenglied der Polytop-Konvention (K in 4D vom Grad 2 in den Laengen: Gamma
  aendert sich exakt um (N - 1)/4 ln(V_Kugel/V_Polytop)); beide Fassungen (roh, berichtigt) berichten. In 2D ist K
  skaleninvariant: kein Volumenglied, kein sqrt(N)-Glied, also beta_2D = 0.
- Erwartete Werte [M]: H-kov (Torus-c ist kovariantes B, Regel S ~ sp): beta = +1,14 +- 0,46. H-Kont (Kontinuum mit
  Eigenzeit-Regler): beta ~ -0,58, nur das Vorzeichen belastbar.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KU0 | 2D-Kontrolle: abs(beta_2D) <= 2 SE und <= 0,05 | 75 % |
| KU1 | [H] 4D, Regel S: beta > 0 mit >= 3 SE (negatives Gitter-G, wie auf dem Torus) | 50 % |
| KU2 | [H] 4D: beta(Regel S) liegt innerhalb 2 SE von 10,26 c_Torus = +1,14 +- 0,46 | 35 % |
| KU3 | [H] 4D: beta(Regel C) und beta(Regel S) haben verschiedenes Vorzeichen | 30 % |
| KU4 | [H] Mass: beta aus Gamma und aus Gamma_M unterscheidet sich um mehr als 2 SE | 50 % |

**Bedeutung (vorab):**
- **KU0 verfehlt:** Die Kugel-Konstruktion erzeugt in 2D ein Artefakt. Karte stoppen, Ursache suchen; keine 4D-Lesart.
- **KU1 trifft ein:** Auch ein exakt kovariantes P1-Netz gibt in 4D das falsche Vorzeichen. Fuer Ue1 in 4D braucht es
  dann eine andere Zutat (Kompensationsfelder, wechselwirkende Materie, andere Netzregel).
- **KU1 verfehlt durch beta < 0 mit >= 3 SE:** Das Torus-Vorzeichen kam aus nicht kovarianten Anteilen; ein kovariantes
  Netz kann Einsteins Vorzeichen geben. Ue1 waere in 4D wieder offen, mit S^4 als Bauplan [H].
- **KU3 trifft ein:** Das Vorzeichen haengt an der Laengenregel, also an einer Wahl des Netzes, nicht an der Materie.
- **KU4 trifft ein:** Das Mass (wie man Punkte gewichtet) bestimmt das Vorzeichen mit.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3, cpu4 und cpu5; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren (wie INDUZIERT-DICHTE-4D). Rauchlauf zuerst.
- Zeitbox 150 min.
