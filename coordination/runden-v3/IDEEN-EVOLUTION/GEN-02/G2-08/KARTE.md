# G2-08 Q-Ball-Prisma: Eine Stufe im Brechungsfeld sortiert Q-Baelle nach ihrer inneren Frequenz, wenn das Feld nur als Optik wirkt

- Hypothese: Ein 1D-Q-Ball ueberquert eine glatte Stufe im Brechungsfeld wie ein Teilchen, dessen Ruheenergie um
  Delta M = R M Phi2 springt; wirkt das Feld nur auf den Gradiententerm (Optik, Variante A), haengt R = 4G/E von der
  inneren Frequenz omega ab, und die Stufe wirft langsame Baelle mit kleinem omega zurueck, waehrend sie gleich schnelle
  mit grossem omega durchlaesst; als volle Metrik (Variante C) behandelt sie alle Baelle gleich [H].

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Code-Basis RUNDE-01/qg1/qg1.py: L = A(x)|psi_t|^2 - B(x)|psi_x|^2 - C(x) U(S), U = S - S^2 + S^3/2, d = 1;
    A = 1 + a Phi, B = 1 + b Phi, C = 1 + c Phi. Variante A (Optik, B = c^2): (a, b, c) = (0, 4, 0). Variante C (volle
    Metrik): (-2, 2, 0). Dort ist Phi = g x/2 (linearer Gradient); hier statt dessen eine Stufe
    Phi(x) = Phi2 (1 + tanh((x - x_s)/w))/2 mit Phi2 = 0,01 und w = 1.
  - In einem Gebiet mit konstantem Phi ist die Physik die alte, umskaliert: x'' = x/sqrt(B), t'' = t/sqrt(A), Wirkung mal
    sqrt(AB). Bei fester Ladung Q folgt die Ruheenergie im Gebiet hinter der Stufe geschlossen:
    M2 = sqrt(B) E(Q/sqrt(AB)), mit der Familie E(Q) des freien Balls.
    - Variante C: M2/M1 = sqrt(1 + 2 Phi2) (1 + 2 Phi2^2 omega Q/E); ueber die drei omega gleich bis auf 3e-5 in M2/M1,
      also 0,1 % in v_cl.
    - Variante A: M2 - M1 = (sqrt(1 + 4 Phi2) - 1)(E - omega Q) = (sqrt(1 + 4 Phi2) - 1) 2G (1D-Virial: E - omega Q = 2G,
      G = Int f'^2); in erster Ordnung Delta M/M = R_A Phi2 mit R_A = 4G/E.
  - Bekannte Werte eines frueheren Fall-Laufs im linearen Gradienten (gleicher Code, fein): R_A = 0,3216 / 0,2227 / 0,0694
    bei omega^2 = 0,55 / 0,70 / 0,90; R_C = 0,9971 bei allen drei.
  - Teilchenschwelle (Energieerhaltung, Ball ohne innere Anregung, vgl. Stufen im Massenterm: dort Reflexion unter und
    Durchgang ueber der Schwelle auf 2 %): gamma_cl = M2/M1, v_cl = sqrt(1 - (M1/M2)^2).
    - Variante C: v_cl = 0,141 fuer alle drei omega.
    - Variante A: v_cl = 0,0796 / 0,0663 / 0,0371 (omega^2 = 0,55 / 0,70 / 0,90), also v_cl,A/v_cl,C = 0,56 / 0,47 /
      0,26, etwa sqrt(R_A). Die zweite Ordnung (Kruemmung von E(Q)) verschiebt den Wert bei 0,90 um bis zu 2 %.
  - **Bindend** sind die Schwellen, die der Code vor der Entwicklung exakt aus der geschossenen Familie rechnet (M2 wie
    oben, ohne erste Ordnung). Die Handwerte sind Groessenordnungen.

- Kleiner Test:
  - Code: Kopie von qg1.py; Phi(x) als Stufe (eine Zeile); Start bei x0 = -20 mit Lorentz-Boost v zur Stufe bei x_s = 0;
    Schwamm und Profilschiessen wie qg1; Box so lang, dass der langsamste Ball die Stufe um 40 Einheiten passieren kann
    (T bis 2000 bei v = 0,035, sonst 600). Neuer Code unter 45 min.
  - Laeufe:
    - Schwellenpaare: je Variante (A, C) und omega^2 (0,55 / 0,70 / 0,90) v = 0,95 und 1,05 mal Codeschwelle: 12 Laeufe
    - Prisma: gemeinsame Geschwindigkeit v_P1 = Mittel der A-Codeschwellen von 0,70 und 0,90 (Hand etwa 0,052) und
      v_P2 = Mittel der A-Codeschwellen von 0,55 und 0,70 (Hand etwa 0,073); je fuer alle drei omega in A und in C:
      12 Laeufe
    - Gegenproben: drei Laeufe (unten)
  - Rechenort: .69 ueber kleintest.sh, p4000a (grob); p4000b fein fuer die vier Schwellenlaeufe bei omega^2 = 0,70;
    geschaetzt 3 bis 6 min.
  - Messgroessen: q_durch, q_zurueck, q_stufe (Ladung in |x - x_s| < 6 am Ende), q_frei (Rest); Ausgang durch,
    reflektiert oder haengt nach der Mehrheitsladung; Endgeschwindigkeit v2; Schwankung von max|psi| nach dem Durchgang.

- Vorhersage vorab:
  - V1 (Universalitaet C): Alle sechs C-Schwellenpaare sind reflektiert bei 0,95 und durch bei 1,05 der Codeschwelle; die
    drei C-Codeschwellen stimmen untereinander auf 2 %.
  - V2 (Optik A): Alle sechs A-Schwellenpaare sind reflektiert bei 0,95 und durch bei 1,05 der Codeschwelle. Die
    Codeschwellen selbst sind vorab aus der Familie ableitbar und keine Messung; gemessen wird nur, ob der Ball an ihnen
    als Teilchen umschlaegt.
  - V3 (Prisma): bei v_P1 in A: omega^2 = 0,55 und 0,70 reflektiert, 0,90 durch; bei v_P2 in A: 0,55 reflektiert, 0,70 und
    0,90 durch. In C bei beiden Geschwindigkeiten alle drei reflektiert.
  - V4: Durchgelaufene Baelle behalten mindestens 97 % ihrer Ladung; max|psi| schwankt danach um weniger als 2 %.
  - **Scheitert, wenn** eines davon eintritt:
    - mehr als einer der 12 Schwellenlaeufe hat den falschen Ausgang
    - in A ist die Sortierung an einer der sechs Prisma-Stellen falsch, oder in C tritt eine Sortierung auf
    - die drei C-Codeschwellen weichen untereinander um mehr als 2 % ab, oder ein Ball spaltet (mehr als 10 % der Ladung
      auf beiden Seiten)
  - Nicht entscheidbar, wenn die Plausibilitaetsschranke reisst.

- Gegenprobe:
  - Phi2 = 0 (keine Stufe), omega^2 = 0,70, Variante A, v = v_P1: durch, v2 = v auf 1e-3.
  - Variante C: Die omega-Abhaengigkeit der Schwelle muss verschwinden (V1).
  - Umgekehrte Stufe Phi2 = -0,01, Variante A, omega^2 = 0,55, v = v_P1: durch, v2 > v (anziehend).

- Plausibilitaetsschranke:
  - Ladung (rho = 2 A Im(psi conj psi_t)) bis zum Schwamm auf 1e-6 erhalten; Killing-Energie (statisches Feld) auf 1e-5
  - q_durch + q_zurueck + q_stufe + q_frei = 1 +- 1e-3, jeder Anteil zwischen 0 und 1
  - |v2| unter der lokalen Lichtgeschwindigkeit sqrt(B/A)

- Latten erwartet:
  - L1 ja: Schwellen, Sortierung und Universalitaet koennen je einzeln scheitern.
  - L2: keine Stufe, Variante C, umgekehrte Stufe.
  - L3: dx/2 und dt/2 geben dieselben Ausgaenge; Codeschwellen auf 1 %.
  - L4 teilweise: Brechung von Materiewellen nach dem Impulsverhaeltnis (Neutronenoptik) [L?]; Solitonzentren folgen im
    aeusseren Potential dem klassischen Hamiltonfluss (arXiv 2609.25648, nicht an der Quelle gelesen) [L?]. Eine Stufe,
    die nur auf die Gradientenenergie wirkt und dadurch nach innerer Frequenz sortiert, kenne ich nicht [H].
  - L5 Messbezug nur als Argument: Ein solches Prisma waere eine Zusammensetzungsabhaengigkeit der Groesse 1;
    Eoetvoes-Experimente schliessen sie bis etwa 1e-15 aus (MICROSCOPE, Zahl nicht an der Quelle gelesen) [L?]. Kein
    neuer Messvergleich.

- Einfach gesagt: Ein Q-Ball, der auf eine Stufe im Brechungsfeld trifft, verhaelt sich wie eine Kugel vor einer
  Schwelle: Ist er zu langsam, rollt er zurueck. Wirkt das Feld wie in der Optik nur auf den Rand des Balls, ist die
  Schwelle fuer jeden Ball anders hoch, je nachdem, wie schnell er innerlich schwingt. Dann trennt die Stufe die Baelle wie
  ein Glasprisma die Farben: Bei gleicher Geschwindigkeit kommen manche durch und andere nicht. Wirkt das Feld dagegen wie
  Einsteins Raumzeit auf alles gleich, kommen alle gleich schnellen Baelle zusammen durch oder keiner.

- Karte geschrieben: 2026-09-30 10:56:55 CEST
- Vorhersage geschrieben: 2026-09-30 11:16:14 CEST
