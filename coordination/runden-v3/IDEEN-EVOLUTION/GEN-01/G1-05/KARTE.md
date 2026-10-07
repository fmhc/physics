# G1-05 Sattel-Knoten statt Kante: die Bremsschwelle im Kondensat als Solitonen-Abloesung

- **Hypothese:** Die Geschwindigkeit u_c, ab der ein stroemendes stabiles chi-Kondensat einen ruhenden Q-Ball bremst,
  ist die Stelle, an der die stationaere Umstroemung seiner Delle in einem Sattel-Knoten verschwindet (nichtlineare
  kritische Geschwindigkeit, kleiner als c_s); darueber loest der Ball periodisch graue (dunkle) Solitonen ab, deren Rate
  von null an etwa wie (u - u_SN)^(1/2) steigt, darunter geht die spaete Kraft gegen null.
- **Papier vorab [S]:** Hydraulische Grenze (Delle breit gegen die Heillaenge): 1 + M^2/2 = (3/2) M^(2/3) + beta mit
  beta = lam S_max/(2 g4 C0). Das gibt M = u/c_s = 0,30 (C0 = 0,1), 0,49 (C0 = 0,2), 0,58 (C0 = 0,3). Fuer ein schwaches
  Hindernis gilt M -> 1. Die Ballbreite liegt bei 1,6 / 2,2 / 2,8 Heillaengen, u_SN also dazwischen. Nahe eines
  Sattel-Knotens wachsen Zeiten wie |u - u_SN|^(-1/2); ein kurzes Messfenster sieht daher keine scharfe Kante.
- **Kleiner Test:**
  - (a) Stationaere Umstroemung, neuer Code (hoechstens 45 min), Laptop-CPU oder .69 cpu, Sekunden:
    - Ballprofil S(x) fest (omega^2 = 0,7, geschlossenes 1D-Profil wie in RUNDE-06/medium1d/medium1d.py); Rueckwirkung
      des Mediums auf den Ball vernachlaessigt (lam = 0,1).
    - Ansatz chi = a(x) exp(i(theta(x) - Omega t)), a^2 theta' = J, a'' = [mc2 + 2 g4 a^2 + lam S(x) - Omega^2 + J^2/a^4] a;
      weit weg a^2 = C0, theta' = K, Omega^2 - K^2 = mc2 + 2 g4 C0, u = K/Omega (Lorentz-Medium wie im Code).
    - Symmetrische Loesung (a'(0) = 0) per Schiessen vom stromauf liegenden Fixpunkt ab x = -60; u in Schritten von
      0,005 c_s erhoehen, bis die Loesung verschwindet: u_SN. Fuer C0 = 0,1 / 0,2 / 0,3 (g4 = 0,5, mc2 = 1).
    - Zwei Schrittweiten (L3); Kontrollen: lam = 0,01 gibt u_SN/c_s >= 0,9; ein auf das Vierfache gestrecktes S naehert
      sich der hydraulischen Zahl auf 0,05.
  - (b) Lauf erst nach (a), .69 p4000a, geschaetzt 5 bis 9 min (sonst in zwei Aufrufe teilen):
    - RUNDE-06/medium1d/medium1d.py, Unterbefehl landau, unveraendert bis auf T = 1500 statt 570 und Box 1600 statt 600
      (Schall kehrt vor T nicht zurueck).
    - C0 = 0,2 (neu, c_s = 0,2774) bei u/c_s = u_SN/c_s + (-0,15 / -0,05 / +0,05 / +0,15 / +0,30); dazu C0 = 0,1 bei
      u_SN +- 0,05 c_s. Zusammen 7 Laeufe, grob und fein.
    - Neu ausgegeben: Solitonzaehler (Durchgaenge eines Dichteminimums C < 0,6 C0 an der Sonde x = +40 stromab im
      Ballsystem, mit Zeiten), spaete Kraft F_spaet auf [1200, 1500], Kraft je 100er-Fenster.
- **Vorhersage vorab:**
  - V1 (a gegen die vorhandene Messung; Regel vor der Rechnung): u_SN/c_s liegt fuer C0 = 0,1 in [0,33; 0,53] und fuer
    C0 = 0,3 in [0,54; 0,77] (gemessene Klammern 0,38 bis 0,48 und 0,59 bis 0,72, je +- 0,05), und stets zwischen der
    hydraulischen Zahl und 1.
  - V2 (b, blind, C0 = 0,2): bei u <= u_SN - 0,05 c_s kein Soliton und F_spaet < F_MIN = 2e-6; bei u >= u_SN + 0,05 c_s
    mindestens ein Soliton im Fenster [370, 1500] und F_spaet > F_MIN.
  - V3: Abloeserate Gamma bei +0,05 / +0,15 / +0,30 c_s steigend; aus log Gamma gegen log(u - u_SN) Exponent 0,5 +- 0,2
    (nur mit mindestens zwei Solitonen je Punkt, sonst "nicht entscheidbar").
  - **Scheitert, wenn** V1 fuer eine der beiden Dichten verfehlt ist, oder Solitonen schon bei u <= u_SN - 0,05 c_s
    auftreten, oder bei u >= u_SN + 0,05 c_s keine, oder F_spaet unter u_SN - 0,05 c_s ueber F_MIN bleibt, ohne im
    Fenster abzufallen (dann bremst ein zweiter Kanal, den der Sattel-Knoten nicht erklaert).
- **Gegenprobe (Effekt muss verschwinden):** lam = 0 bei C0 = 0,2 und u = u_SN + 0,15 c_s: kein Soliton, F = 0 exakt;
  u = 0: kein Soliton, |F| < 1e-10.
- **Plausibilitaetsschranke:** hydraulisch <= u_SN <= c_s; Mediumladung Q_chi auf 1e-6 relativ erhalten; Solitonen mit
  Minimaldichte > 0 und Geschwindigkeit relativ zum Medium < c_s; mittlere Kraft >= 0 in Stroemungsrichtung.
- **Latten erwartet:** L1 ja; L2 lam = 0 und u = 0; L3 zwei Schrittweiten (a), grob gegen fein (b); L4 teilweise
  (kritische Geschwindigkeit mit Sattel-Knoten und Solitonen-Abloesung ist fuer 1D-NLS-Stroemung bekannt; fuer einen
  Q-Ball als Hindernis in einem relativistischen Kondensat nicht gefunden); L5 teilweise (Kondensat-Experiment mit
  breiter, durchlaessiger Barriere: stationaer, dann dunkle Solitonen, dann wieder ruhig; dort setzt es bei etwa
  Mach 0,1 bis 0,14 ein, die 1D-Hydraulik gaebe dort etwa 0,43 [S]; unser 1D-Modell prueft nur die 1D-Zahl).
- **Einfach gesagt:** Ein Ball in einem stroemenden Kondensat wird erst ab einer bestimmten Stroemung gebremst, und
  diese Grenze liegt unter der Schallgeschwindigkeit. Wir vermuten: Genau dort kann das Kondensat nicht mehr ruhig um
  die Delle des Balls fliessen und reisst stattdessen immer wieder kleine Dichteloecher ab, die davonschwimmen. Wir
  rechnen die Grenze zuerst auf dem Papier aus und pruefen sie dann mit einer neuen Dichte im Computer. Zaehlt der
  Solitonzaehler erst oberhalb der Grenze, stimmt das Bild.
- Karte geschrieben: 2026-09-30 07:38:50 CEST
- Vorhersage geschrieben: 2026-09-30 07:52:18 CEST
