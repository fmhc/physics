# G1-10 Stille Atmung im gekruemmten Raum: Die Feld-Uhr bleibt still und spuert die Kruemmung erst in zweiter Ordnung

- Hypothese: Die erste stille Atmungsstelle des 3D-Balls (omega*^2 = 0,797677, beta = 1/2) bleibt im raeumlich
  gekruemmten hyperbolischen Raum H^3 (Kruemmungsradius R_c) still und verschiebt sich um +C/R_c^2 nach oben, und die
  Kruemmung wirkt dabei wie eine effektiv etwas hoehere Raumdimension d_eff = 3 + (2/3) <r^2>/R_c^2 [H].

- Grundlagen-Bezug [H]: Eine stille Feld-Atmung ist eine Uhr ohne Strahlungsdaempfung. Haengt ihr Gang nur ueber
  (R_Ball/R_c)^2 von der Kruemmung ab, entspricht das dem Muster, das das Uhrenpostulat der Allgemeinen
  Relativitaetstheorie fuer ausgedehnte Uhren erwartet (Gezeitenordnung). Hier gilt das nur fuer einen statischen, rein
  raeumlich gekruemmten Raum ohne Rotverschiebung. Die Zuordnung ist eine Hypothese, keine Aussage ueber Gravitation.

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Radialer Laplace auf H^3: f'' + (2/R_c) coth(r/R_c) f' = f'' + (2/r + 2r/(3 R_c^2) + ...) f'. Das ist der flache
    Operator in d = 3 + 2r^2/(3 R_c^2) Dimensionen, also mehr Volumen je Radius.
  - Mit chi = sigma f, sigma = R_c sinh(r/R_c): chi_tt - chi'' + chi/R_c^2 + U'(chi^2/sigma^2) chi = 0. Zwei Anteile:
    - (a) Massenterm 1/R_c^2: exakt das flache Modell mit beta' = 0,5 (1 + eps), eps = 1/R_c^2, und
      omega^2 = (1 + eps) x*(beta'). Mit der bekannten Leiter (erste Stelle 0,755738 / 0,797677 / 0,829984 bei
      beta = 0,45 / 0,50 / 0,55 [A]) folgt dx*/dbeta = 0,65 bis 0,84, also eine Verschiebung +C_A/R_c^2 mit
      C_A = 1,12 bis 1,22.
    - (b) sigma statt r in der Dichte: Vorzeichen offen.
  - Die Signatur der Abstrahlamplitude bleibt reell, weil der Raum statisch ist. Eine einzelne Nullstelle kann darum bei
    kleiner Stoerung nicht verschwinden, nur wandern.
  - Kanalkante: Freie Wellen haben in chi die Masse^2 1 + 1/R_c^2, also k^2 = (omega + nu)^2 - 1 - 1/R_c^2.

- Kleiner Test:
  - Code-Basis: RUNDE-07/bic2/bic2_v2.py (profil mit dim und beta, lin_aufbau, det/newton, Kontur fuer den Umlauf,
    signierte Amplitude wie in "kurve"). Neu (unter 1 h): Radialoperator mit coth-Term im Profil und im linearen
    Problem, Kanalmasse 1 + 1/R_c^2 in der Randbedingung.
  - Arme je R_c = 10, 20, 40, 80 und 1e4:
    - (B) voll H^3
    - (A) nur Massenterm (flacher Operator plus 1/R_c^2): Codekontrolle gegen die Abbildung auf beta'
    - (C) flach, gebrochene Dimension d = 3 + (2/3) <r^2>/R_c^2. <r^2> ist der ladungsgewichtete mittlere
      Radiusquadrat des flachen Profils bei 0,797677; es wird vor den Scans gerechnet und eingetragen.
  - Je Arm: Scan der signierten Amplitude in omega^2 = 0,78 bis 0,84, dann Feinverfahren, Pol-Minimum der Breite und
    Umlauf auf zwei Rechtecken.
  - Rechenort: .69 ueber kleintest.sh, Spuren cpu bis cpu4, je R_c ein Aufruf unter 10 min.

- Vorhersage vorab:
  - V1 Stille bleibt: Fuer R_c = 20, 40 und 80 wechselt die signierte Amplitude im Scan das Vorzeichen, der Umlauf ist
    aufgeloest -1 (wie flach), und die kleinste Breite am Punkt liegt unter 1e-6.
  - V2 Verschiebung (B): Delta(R_c) = omega*^2(R_c) - 0,797677 ist positiv und faellt wie R_c^-q mit q = 2,0 +- 0,3
    (aus 20, 40 und 80); C = Delta R_c^2 liegt zwischen 0,2 und 3,0.
  - V3 Codekontrolle (A): C_A zwischen 1,12 und 1,22, und (A) trifft (1 + eps) x*(beta') auf 2e-4. Das ist ableitbar und
    kein Befund.
  - V4 Kruemmung wie Dimension [H]: Delta_B und Delta_C haben dasselbe Vorzeichen und weichen fuer R_c = 20, 40 und 80
    hoechstens 40 % voneinander ab.
  - R_c = 10: Nur Bericht (Ballradius etwa 3, nicht mehr kleine Kruemmung); vorhergesagt ist nur, dass die Stelle im
    Scanbereich bleibt.
  - **Scheitert, wenn** eines davon eintritt:
    - V1 verfehlt fuer ein R_c >= 20: kein Vorzeichenwechsel im Scan, oder Umlauf 0 auf einem aufgeloesten Rechteck, das
      die Stelle enthaelt
    - Delta_B negativ, q ausserhalb 1,6 bis 2,4 oder C ausserhalb 0,1 bis 5
    - Delta_B und Delta_C mit verschiedenem Vorzeichen oder mehr als 40 % auseinander
  - Nicht entscheidbar, wenn die Gegenprobe R_c = 1e4 oder die Codekontrolle (A) reisst.

- Gegenprobe: R_c = 1e4 muss den flachen Ball wiedergeben: omega*^2 = 0,797677 +- 2e-6, signierte Amplitude wie flach auf
  1e-6. Dort muss jeder Kruemmungseffekt verschwinden.

- Plausibilitaetsschranke:
  - An jedem Pol Im nu <= 0 (abklingend), also Breite >= 0.
  - Am Pol ist der Kanal offen: (omega + Re nu)^2 - 1 - 1/R_c^2 > 0.
  - Das Profil faellt wie e^{-sqrt(1 + 1/R_c^2 - omega^2) r}/sinh(r/R_c) ab.
  - Die Ladung Q(0,7977) des H^3-Balls liegt fuer R_c >= 20 hoechstens 10 % neben der flachen (faengt Fehler im
    Schiessen ab).

- Latten erwartet:
  - L1 ja: Vorzeichen, Exponent, Groesse und die Gleichsetzung mit der Dimension koennen je scheitern.
  - L2: R_c = 1e4 und Arm (A).
  - L3: halbe Schrittweite im Radius und groesserer Rand R_max; Stelle auf 1e-5, C auf 10 %.
  - L4 teilweise: Q-Baelle und Bosonensterne in Anti-de-Sitter- und hyperbolischen Raeumen sind Literatur [L, aus dem
    Gedaechtnis, nicht nachgelesen]. Stille Atmungsstellen im gekruemmten Raum kenne ich nicht [H].
  - L5 nein: Modellaussage, keine Messung.

- Einfach gesagt: Ein atmender Q-Ball hat besondere Atemfrequenzen, bei denen er gar keine Wellen abstrahlt; er ist dann
  eine fast perfekte kleine Uhr. Wir fragen, was mit dieser Uhr passiert, wenn der Raum selbst gekruemmt ist, wie es die
  Allgemeine Relativitaetstheorie erlaubt. Vorhersage: Die Uhr bleibt still, aber ihre besondere Frequenz rutscht ein
  kleines Stueck nach oben, und zwar mit dem Kehrwert des Quadrats des Kruemmungsradius. Ausserdem soll die Kruemmung so
  wirken, als haette der Raum ein kleines bisschen mehr als drei Dimensionen. Rutscht die Frequenz nach unten,
  verschwindet die Stille, oder passt der Dimensionsvergleich nicht, ist die Idee falsch.

- Karte geschrieben: 2026-09-30 07:44:45 CEST

- Vorhersage geschrieben: 2026-09-30 07:58:24 CEST
