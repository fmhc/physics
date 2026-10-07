# G1-01 Gitter-Pinning duennwandiger Q-Baelle: Haelt das Rechengitter die Fronten fest?

- **Hypothese [H]:** Nahe omega^2 = 1/2 (duenne Wand, flaches Inneres) kann das Rechengitter die beiden Fronten eines
  Q-Balls festhalten. Dann gibt es bei fester Ladung mehrere stationaere Loesungen, eine Snaking-Leiter, die Stabilitaets-
  und Konkurrenzurteile verfaelscht.

- **Papier vorab [S] (eigene Rechnung, ungeprueft):**
  - Modell wie im Atlas: U(S) = S - S^2 + S^3/2, S = f^2, stationaer f'' = f (1 - 2 f^2 + 1,5 f^4 - omega^2).
  - 1D-Front am Maxwell-Punkt omega^2 = 1/2: f'^2 = (f^2/2)(1 - f^2)^2, also f^2 = 1/(1 + e^{-sqrt2 x}). Die naechste
    Singularitaet liegt bei x = i pi/sqrt2, Abstand d = pi/sqrt2 von der reellen Achse (wie beim phi^4-Kink).
  - Daraus Peierls-Nabarro-Energie E_PN ~ P(h) exp(-2 pi d/h) = P(h) exp(-sqrt2 pi^2/h) = P(h) exp(-13,96/h), P(h) ein
    Vorfaktor, potenzartig in 1/h: h = 1: 8,7e-7 P; h = 0,75: 8,3e-9 P; h = 0,5: 7,6e-13 P; h = 0,25: 6e-25 P.
  - 1D-Troepfchen aus zwei Fronten im Abstand L: omega^2 - 1/2 ~ e^{-sqrt2 L}. Snaking (omega^2(Q) nicht monoton) erst,
    wenn omega^2 - 1/2 unter die Pinningbreite faellt, etwa 3 E_PN/h.
  - Kontinuum geschlossen: b = sqrt(2 omega^2 - 1), Q_kont(omega) = 2 sqrt2 omega arcosh(1/b),
    E_kont = omega Q_kont + (1/sqrt2) [sqrt(1 - b^2) - b^2 arcosh(1/b)].
  - Folge: Bei h <= 0,25 liegt das Pinning unter der float64-Aufloesung; unsere Produktionsgitter (0,1 und feiner)
    waeren nicht betroffen.

- **Kleiner Test:**
  - Neuer 1D-Code (numpy, float64): Newton-Fortsetzung in Q fuer symmetrische Troepfchen auf dem Gitter mit Weite h,
    je zwei Zweige: gitterplatz-zentriert und bindungszentriert. Unbekannte f und omega, Nebenbedingung
    Q = 2 omega h Sum f^2. Q von 4 bis 34 (omega^2 - 1/2 bis etwa 1e-14), Dirichlet-Rand bei 42.
  - Hauptlauf: h = 1, 0,75, 0,5 und 0,25. Die Gitterweiten 1 und 0,75 kommen dazu, weil laut Papier nur dort und bei
    0,5 ein Pinning ueber der float64-Aufloesung liegt; ohne sie ist keine Breite gegen h messbar.
  - Gegenprobe (getrennter Lauf): h = 0,125 und 0,1 (0,1 = radiale Produktionsweite von r5a) und Vergleich mit dem
    geschlossenen Kontinuum.
  - Grob/fein: Fortsetzungsschritt dQ und dQ/2.
  - Messung:
    - A_E(h) = max |E_platz(Q) - E_bindung(Q)| fuer Q in [12, 30] (Energieabstand bei fester Ladung)
    - d_w(h) = max |omega^2_platz(Q) - omega^2_bindung(Q)| im selben Fenster
    - Zahl stationaerer Loesungen je Q: 2 (Platz, Bindung), wenn ihr Energieabstand ueber der Aufloesung liegt, sonst 1
    - Snaking: Zahl der Extrema von omega^2(Q) je Zweig und groesste Zahl von Loesungen eines Zweigs bei einem
      omega^2; Beginn Q_pin und Breite W(h) = omega^2(Q_pin) - 1/2
  - Rechenort: .69 Spur cpu (numpy, 1 Thread), unter 10 min je Aufruf.

- **Vorhersage vorab:**
  - V1: A_E faellt wie exp(-c/h); der Fit ueber h = 1, 0,75, 0,5 ergibt c zwischen 10 und 18 (Papier 13,96 plus
    Vorfaktor).
  - V2: A_E(0,5) liegt zwischen 1e-14 und 1e-8.
  - V3: Snaking (omega^2(Q) mit Extrema ueber dem Rauschen) tritt bei h = 1 auf, bei h = 0,25 und feiner nicht.
  - V4: Bei h = 0,25, 0,125 und 0,1 ist A_E unter 1e-12 (auf dem Raster nicht gesehen, obere Schranke).
  - **Scheitert, wenn** eines davon eintritt:
    - c ausserhalb 10 bis 18, oder A_E(0,5) ausserhalb 1e-14 bis 1e-8
    - Snaking oder A_E >= 1e-12 bei h <= 0,25 (dann traefe das Pinning auch unsere Produktionsgitter)
    - kein Snaking bei h = 1 bis Q = 34

- **Gegenprobe (Effekt muss verschwinden):** h = 0,125 und 0,1: omega^2(Q) monoton, A_E unter 1e-12, und omega^2_h(Q)
  naehert sich dem Kontinuum mit zweiter Ordnung: Fehlerverhaeltnis h = 0,25 zu 0,125 bei Q = 8 und 12 zwischen 3 und 5.

- **Plausibilitaetsschranke:**
  - fuer jede Loesung 1/2 - d_w(h) - 1e-14 <= omega^2 < 1 (unter 1/2 nur im Pinningband), omega < E/Q < 1,
    0 < max f^2 <= 1 + 1e-9
  - auf dem Gitter gilt dE/dQ = omega exakt; der zentrale Differenzenquotient entlang des Zweigs trifft omega auf 1e-4
    relativ

- **Latten erwartet:** L1 ja (Exponent, Groesse und die Grenze bei h = 0,25 koennen je scheitern); L2 h = 0,125 und 0,1
  mit Kontinuumsvergleich; L3 dQ gegen dQ/2, A_E auf 5 % gleich, Effekt mindestens fuenfmal die Aenderung; L4 ja
  (Peierls-Nabarro-Barrieren und homoklines Snaking auf Gittern sind Literatur [L, aus dem Gedaechtnis]); L5 nein
  (Numerik-Hygiene, keine Messung).

- **Einfach gesagt:** Ein Rechengitter ist wie ein Eierkarton: Die Kante eines grossen, flachen Q-Balls kann in einer
  Mulde haengen bleiben. Dann liefert der Rechner mehrere Loesungen, wo es eigentlich nur eine gibt. Nach der
  Papierrechnung ist dieser Effekt winzig und schrumpft mit feinerem Gitter extrem schnell, so dass unsere ueblichen
  Gitter nichts davon merken. Der Test misst die Mulden-Tiefe bei groben Gittern und prueft, ob sie so schnell
  verschwindet wie vorhergesagt.

- Vorhersage geschrieben: 2026-09-30 07:58:24 CEST
