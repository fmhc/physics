# QUANT-1: Vorab-Rechnung des Rechen-Agenten (vor jeder Produktions-Ergebnisdatei)

- Geschrieben ab 2026-10-05 18:12:39 CEST (date). Erste Produktionsdatei (k8-l0) entsteht fruehestens 5 min nach 18:12:20 CEST.
- Quelle der Zahlen: q1.py frei (aus/frei-k8.json, frei-k6.json, frei-v4.json, .69, 16:10:48 bis 16:10:53 UTC): exaktes
  freies G0 = <|phi|^2> und Einschleifen-Tadpole [M, eigene Wick-Zaehlung, nicht gegengelesen].

## Umrechnung [M]

- Gitter: U_g(S) = m^2 S - lam S^2 + g6 S^3 mit g6 = lam^2/(2 m^2) (Papier-I-Form, beta = 1/2).
- phi = (m/sqrt(lam)) psi, x = y/m: S_E = (1/lam) S_QB[psi]. lam ist hbar in Q-Ball-Einheiten.
- Zahl der Quanten N = Q_QB/lam, Energie E = (m/lam) E_QB(Q_QB = lam N).
- Klassisch (q1.py klass, laeuft noch): E_QB/Q_QB = 1 bei Q_QB etwa 141 (om etwa 0,92). Fuer N <= 5 Quanten gibt es
  einen klassisch gebundenen Q-Ball also erst ab lam etwa 28 (N = 5) bzw. 70 (N = 2).

## Einschleifen-Erwartung (cubisch L = 8, T = 32, m = 0,5; G0 = 0,1456)

- Normalordnung des Sextik-Terms: 9 g6 G0 |phi|^4. Effektive Quartik lam_eff = lam - 9 g6 G0 = lam - 2,62 lam^2.
- Anziehend nur fuer lam < 0,38; groesste Anziehung lam_eff = 0,095 bei lam = 0,19.
- Kastenverschiebung 1. Ordnung (Q Quanten in Ruhe): dE_Q = -lam_eff Q(Q-1)/(4 m1^2 Vol) + Sextik-Dreikoerperterm.
  - lam = 0,25, L = 8: dE_2 = -5,5e-4, dE_3 = -1,7e-3, dE_5 = -5,5e-3 (L = 6: -1,3e-3 / -3,9e-3 / -1,3e-2).
  - lam = 1: lam_eff = -1,6 (abstossend), dE_2 = +3,7e-3 (L = 8).
- Gebundener Zweierzustand (nichtrelativistisch, Kontaktpotential auf dem kubischen Gitter, Watson-Integral 0,505):
  braucht lam_eff > etwa 8 m = 4. Das ist mit lam_eff <= 0,1 um den Faktor 40 verfehlt.
- Erwartung [M, grob]: keine echte Bindung fuer Q = 2, 3 bei m a = 0,5; bei schwacher Kopplung eine kleine
  anziehende Kastenverschiebung (skaliert wie 1/L^3, kein Bindungszustand), ab lam etwa 0,4 Abstossung.
- Einschleifen-Masse: lam = 0,1: m1 = 0,443; lam = 0,25: 0,388; lam = 1: 0,64 (Gitterenergie). Fuer lam >= 2
  versagt die Einschleifenrechnung (m1 > 1, Sextik dominiert); lam = 10 ist ohne Vorhersage.
- Q1 (Masse auf 20 %): bei lam = 0,1 erwartet -11 %, bei lam = 0,25 -22 % (knapp ausserhalb).
