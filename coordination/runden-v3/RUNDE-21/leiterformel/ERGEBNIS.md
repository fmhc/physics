# ERGEBNIS LEITERFORMEL (Runde 21)

- Code-Agent. Start 2026-10-02 18:36:32 CEST (date). Plan eingefroren 18:44:29 CEST
  (PLAN.md.eingefroren-20261002-184429), vor der ersten Rechnung (K0-Lauf 16:46:52 UTC = 18:46:52 CEST). Kein Nachtrag.
  Bericht ab 18:53:43 CEST (date). Uhrzeiten der .69 in UTC (CEST = UTC + 2).
- Code: code/leiterformel.py (eigen; Befehle k0, stellen, ausw); code/stille3.py und code/huellen_leiter.py unveraendert
  aus RUNDE-18 (sha256 gleich). Grundlage: 156 stille Stellen (l = 0: 108, l = 1: 27, l = 2: 21), 137 Paare.
- Explorativ (v3), nachtraegliche Erklaerung vorhandener Daten. Alles modellintern (M2, linear, klassisch), keine
  Messdaten. Deutungen sind Hypothesen [H].

## 1 Ergebnis zuerst

1. **Die Phasenregel Delta Phi = pi traegt auf reifen Kurven, nicht kurz nach der Geburt einer Kurve.** Auf den
   Wandkurven k = 0 (l = 0, 1, 2, alle Paare mit R_n >= 10) und auf l = 0, k = 0 bis 2 (R_n >= 15) liegt jedes Paar
   innerhalb von 3 %; bei R ~ 40 trifft Delta Phi pi auf 0,07 bis 0,33 % (k = 0 bis 3). Alle 29 Fehlpaare von LF1 und LF2
   liegen auf inneren Kurven (k >= 1) unter den ersten vier Paaren nach der Geburt der Kurve.
2. **Formal: LF0, LF1, LF3 und LF4 eingetroffen, LF2 nicht.**
   - LF1: 68 von 85 Paaren = 80,0 %, genau auf der Schwelle. Ein Paar mehr ausserhalb haette LF1 kippen lassen; das
     knappste Paar innen liegt bei 2,98 % (k = 3, R_n = 19,94).
   - LF2: 20 von 32 = 62,5 % (ohne die gekennzeichnete Stelle l = 2 / R = 22,29: 19 von 31).
   - LF3: Delta Phi weicht im Mittel 2,7 % von pi ab, pi/k_innen 11,5 % vom gemessenen Abstand (l = 0, 98 Paare).
   - LF4: alle 137 Reste sind positiv (Delta Phi > pi).
3. **Bedeutung nach Karte: keine der beiden vorab festgelegten Bedeutungen ist ausgeloest.** "LF1 und LF2 treffen ein"
   gilt nicht (LF2 verfehlt), "LF1 trifft nicht ein" gilt auch nicht. Die Phasenbedingung ist damit als geschlossener
   Baustein fuer l = 0, 1, 2 nicht bestaetigt; sie gilt auf reifen Kurven, nicht auf jungen.
4. **Restabweichung:** immer positiv; auf jeder Kurve streng fallend mit R (Spearman -1 auf allen l = 0-Kurven k = 0
   bis 7); auf der Wandkurve l = 0 etwa wie 1/R^2 (0,079 bei R = 3,2; 0,0098 bei 10,6; 0,0029 bei 20,3; 0,0007 bei
   42,0). Bei gleichem R groesser fuer hoeheres k (juengere Kurve) und hoeheres l.
5. **[H, nachtraeglich, getrennt von der Wertung]** Auf der Wandkurve ist der Mehrrest von l = 1 und l = 2 gegenueber
   l = 0 der Abstandsterm der Nullstellen von j_l (McMahon): Verhaeltnis 0,99 bis 1,06 fuer R_n >= 11,7. Der l = 0-Rest
   auf reifen Kurven entspricht einem festen Radiusversatz a ~ 2,1 bis 2,5 (Phi = k_innen (R + a)). Beides ist
   Beschreibung, keine Vorhersage.

## 2 K0 im Detail

- Lauf zuerst und allein (r21lf-k0, 16:46:52 UTC, vor allen Stellen). Je Stelle: Anker = gespeichertes Runde-18-Profil
  Stufe 1 der naechsten Zeile mit omega^2 <= omega^2 der Stelle (.69, runde18-huellen-leiter/aus/prof-st1, nur gelesen),
  Profil an der Stelle mit stille3.Umgebung (Rechenweg HUELLEN-LEITER cmd_umlauf), S0 = f(0)^2, dann die Formel der
  Runde 18 woertlich (unterer Eigenwert lambda_- des a-b-Blocks, k_innen = sqrt(-lambda_-)).
- Kriterium (PLAN 4): abs(pi/k_innen - Kartenzahl) <= 0,01.

| Stelle | k | omega^2 / rho | S0 (Profil) | S0 (U_S = omega^2) | k_innen | pi/k_innen | Karte | Abweichung | R18 dreistellig | Abweichung | Rchi / R Liste | K0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R18 Nr 81 | 0 | 0,76524821 / 1,02705186 | 1,2032701074 | 1,2032701074 | 1,32663053 | 2,368099 | 2,37 | -0,0019 | 2,368 | +0,0001 | 37,184717 / 37,184719 | bestanden |
| R18 Nr 88 | 1 | 0,76405900 / 1,18834090 | 1,2025308674 | 1,2025308674 | 1,52209256 | 2,063996 | 2,07 | -0,0060 | 2,065 | -0,0010 | 38,398836 / 38,398836 | bestanden |

- **K0 bestanden (LF0 eingetroffen).** Bei R ~ 37 ist S0 aus dem Profil gleich der Wurzel von U_S(S0) = omega^2 auf
  10 Stellen. Die Zusatzkontrolle mit der Matrix der Kanalrechnung (stille3.Pot bei r = 0) gibt dasselbe k_innen auf
  8 Stellen.
- Die Abweichung 0,001 zu 2,065 (Nr 88) ist nicht aufgeklaert; die Runde-18-Zahl war eine Schreibtischrechnung.
- Wiederholt mit Fassung 2 des Codes (r21lf-k0-v2, Programmfehler siehe Abschnitt 6): Zahlen bitgleich.

## 3 Tabelle je Paar

- Paar = zwei in R aufeinanderfolgende Stellen derselben Kurve (gleiches l, k). R aus der Stellenliste (Stufe 1).
  Gemessener Abstand = R_n+1 - R_n. pi/k_innen (Mittel) = (pi/k_n + pi/k_n+1)/2. Delta Phi = k_innen(R_n+1) R_n+1 -
  k_innen(R_n) R_n. Restabweichung = Delta Phi / pi - 1.
- Lueckenregel (PLAN 3): Alle 137 Paare sind gezaehlt. Der Umlauf wechselt in allen 137, kein Abstand ist groesser als
  das 1,5-fache des Kurvenmedians. Keine doppelten Stellen.
- Merker "chi0": Die Formel setzt chi = 0 im Inneren voraus; an 6 Stellen mit R < 7 ist chi(0) > 1e-3. Diese Paare liegen
  ausserhalb der LF1- und LF2-Mengen.
- Gekennzeichnet: Stelle l = 2, k = 2, R = 22,29 (SPROSSEN-L1L2 Satz B, formal nicht angenommen, in deren Nachtrag 1 als
  stille Stelle belegt: Rang 2, sigma2/sigma1 4,6e-12, Rechteck-Umlauf +1 aufgeloest auf beiden Stufen).

| l | k | R_n | R_n+1 | gemessener Abstand | pi/k_innen (Mittel) | Delta Phi / pi | Restabweichung | gezaehlt | Merker |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 3,207 | 5,758 | 2,5506 | 2,1395 | 1,0785 | +0,0785 | ja | chi0 = 7,4e-02 |
| 0 | 0 | 5,758 | 8,210 | 2,4519 | 2,2238 | 1,0297 | +0,0297 | ja | chi0 = 6,1e-03 |
| 0 | 0 | 8,210 | 10,640 | 2,4306 | 2,2653 | 1,0157 | +0,0157 | ja | - |
| 0 | 0 | 10,640 | 13,062 | 2,4222 | 2,2913 | 1,0098 | +0,0098 | ja | - |
| 0 | 0 | 13,062 | 15,480 | 2,4178 | 2,3094 | 1,0067 | +0,0067 | ja | - |
| 0 | 0 | 15,480 | 17,895 | 2,4153 | 2,3226 | 1,0049 | +0,0049 | ja | - |
| 0 | 0 | 17,895 | 20,309 | 2,4136 | 2,3326 | 1,0037 | +0,0037 | ja | - |
| 0 | 0 | 20,309 | 22,721 | 2,4124 | 2,3406 | 1,0029 | +0,0029 | ja | - |
| 0 | 0 | 22,721 | 25,133 | 2,4117 | 2,3470 | 1,0023 | +0,0023 | ja | - |
| 0 | 0 | 25,133 | 27,544 | 2,4111 | 2,3524 | 1,0019 | +0,0019 | ja | - |
| 0 | 0 | 27,544 | 29,955 | 2,4106 | 2,3568 | 1,0016 | +0,0016 | ja | - |
| 0 | 0 | 29,955 | 32,365 | 2,4103 | 2,3606 | 1,0014 | +0,0014 | ja | - |
| 0 | 0 | 32,365 | 34,775 | 2,4100 | 2,3639 | 1,0012 | +0,0012 | ja | - |
| 0 | 0 | 34,775 | 37,185 | 2,4097 | 2,3668 | 1,0010 | +0,0010 | ja | - |
| 0 | 0 | 37,185 | 39,594 | 2,4095 | 2,3693 | 1,0009 | +0,0009 | ja | - |
| 0 | 0 | 39,594 | 42,004 | 2,4094 | 2,3715 | 1,0008 | +0,0008 | ja | - |
| 0 | 0 | 42,004 | 44,413 | 2,4093 | 2,3735 | 1,0007 | +0,0007 | ja | - |
| 0 | 1 | 5,917 | 8,398 | 2,4807 | 1,8386 | 1,1581 | +0,1581 | ja | chi0 = 5,2e-03 |
| 0 | 1 | 8,398 | 10,678 | 2,2798 | 1,9104 | 1,0550 | +0,0550 | ja | - |
| 0 | 1 | 10,678 | 12,886 | 2,2083 | 1,9535 | 1,0280 | +0,0280 | ja | - |
| 0 | 1 | 12,886 | 15,059 | 2,1727 | 1,9813 | 1,0169 | +0,0169 | ja | - |
| 0 | 1 | 15,059 | 17,211 | 2,1523 | 2,0005 | 1,0113 | +0,0113 | ja | - |
| 0 | 1 | 17,211 | 19,351 | 2,1394 | 2,0145 | 1,0081 | +0,0081 | ja | - |
| 0 | 1 | 19,351 | 21,481 | 2,1308 | 2,0251 | 1,0060 | +0,0060 | ja | - |
| 0 | 1 | 21,481 | 23,606 | 2,1247 | 2,0335 | 1,0047 | +0,0047 | ja | - |
| 0 | 1 | 23,606 | 25,726 | 2,1203 | 2,0401 | 1,0037 | +0,0037 | ja | - |
| 0 | 1 | 25,726 | 27,843 | 2,1170 | 2,0456 | 1,0031 | +0,0031 | ja | - |
| 0 | 1 | 27,843 | 29,958 | 2,1144 | 2,0502 | 1,0026 | +0,0026 | ja | - |
| 0 | 1 | 29,958 | 32,070 | 2,1124 | 2,0541 | 1,0022 | +0,0022 | ja | - |
| 0 | 1 | 32,070 | 34,181 | 2,1108 | 2,0574 | 1,0018 | +0,0018 | ja | - |
| 0 | 1 | 34,181 | 36,290 | 2,1095 | 2,0603 | 1,0016 | +0,0016 | ja | - |
| 0 | 1 | 36,290 | 38,399 | 2,1084 | 2,0628 | 1,0014 | +0,0014 | ja | - |
| 0 | 1 | 38,399 | 40,506 | 2,1075 | 2,0650 | 1,0012 | +0,0012 | ja | - |
| 0 | 1 | 40,506 | 42,613 | 2,1068 | 2,0670 | 1,0011 | +0,0011 | ja | - |
| 0 | 1 | 42,613 | 44,719 | 2,1061 | 2,0688 | 1,0010 | +0,0010 | ja | - |
| 0 | 2 | 9,250 | 11,812 | 2,5618 | 1,8085 | 1,1825 | +0,1825 | ja | - |
| 0 | 2 | 11,812 | 14,185 | 2,3730 | 1,8714 | 1,0718 | +0,0718 | ja | - |
| 0 | 2 | 14,185 | 16,472 | 2,2865 | 1,9164 | 1,0381 | +0,0381 | ja | - |
| 0 | 2 | 16,472 | 18,709 | 2,2371 | 1,9485 | 1,0234 | +0,0234 | ja | - |
| 0 | 2 | 18,709 | 20,914 | 2,2055 | 1,9720 | 1,0158 | +0,0158 | ja | - |
| 0 | 2 | 20,914 | 23,098 | 2,1838 | 1,9899 | 1,0113 | +0,0113 | ja | - |
| 0 | 2 | 23,098 | 25,266 | 2,1682 | 2,0037 | 1,0084 | +0,0084 | ja | - |
| 0 | 2 | 25,266 | 27,423 | 2,1567 | 2,0148 | 1,0065 | +0,0065 | ja | - |
| 0 | 2 | 27,423 | 29,571 | 2,1478 | 2,0237 | 1,0052 | +0,0052 | ja | - |
| 0 | 2 | 29,571 | 31,712 | 2,1409 | 2,0311 | 1,0042 | +0,0042 | ja | - |
| 0 | 2 | 31,712 | 33,847 | 2,1354 | 2,0373 | 1,0035 | +0,0035 | ja | - |
| 0 | 2 | 33,847 | 35,978 | 2,1310 | 2,0425 | 1,0029 | +0,0029 | ja | - |
| 0 | 2 | 35,978 | 38,105 | 2,1273 | 2,0470 | 1,0025 | +0,0025 | ja | - |
| 0 | 2 | 38,105 | 40,229 | 2,1242 | 2,0509 | 1,0021 | +0,0021 | ja | - |
| 0 | 2 | 40,229 | 42,351 | 2,1217 | 2,0543 | 1,0019 | +0,0019 | ja | - |
| 0 | 2 | 42,351 | 44,471 | 2,1195 | 2,0573 | 1,0016 | +0,0016 | ja | - |
| 0 | 3 | 12,564 | 15,163 | 2,5997 | 1,7881 | 1,2054 | +0,2054 | ja | - |
| 0 | 3 | 15,163 | 17,599 | 2,4353 | 1,8413 | 1,0858 | +0,0858 | ja | - |
| 0 | 3 | 17,599 | 19,945 | 2,3457 | 1,8845 | 1,0473 | +0,0473 | ja | - |
| 0 | 3 | 19,945 | 22,235 | 2,2904 | 1,9176 | 1,0298 | +0,0298 | ja | - |
| 0 | 3 | 22,235 | 24,488 | 2,2528 | 1,9432 | 1,0204 | +0,0204 | ja | - |
| 0 | 3 | 24,488 | 26,714 | 2,2257 | 1,9633 | 1,0147 | +0,0147 | ja | - |
| 0 | 3 | 26,714 | 28,919 | 2,2055 | 1,9796 | 1,0111 | +0,0111 | ja | - |
| 0 | 3 | 28,919 | 31,109 | 2,1898 | 1,9928 | 1,0086 | +0,0086 | ja | - |
| 0 | 3 | 31,109 | 33,286 | 2,1774 | 2,0037 | 1,0069 | +0,0069 | ja | - |
| 0 | 3 | 33,286 | 35,454 | 2,1674 | 2,0129 | 1,0056 | +0,0056 | ja | - |
| 0 | 3 | 35,454 | 37,613 | 2,1593 | 2,0207 | 1,0046 | +0,0046 | ja | - |
| 0 | 3 | 37,613 | 39,765 | 2,1526 | 2,0273 | 1,0039 | +0,0039 | ja | - |
| 0 | 3 | 39,765 | 41,912 | 2,1469 | 2,0331 | 1,0033 | +0,0033 | ja | - |
| 0 | 3 | 41,912 | 44,054 | 2,1421 | 2,0381 | 1,0028 | +0,0028 | ja | - |
| 0 | 4 | 18,494 | 20,972 | 2,4781 | 1,8188 | 1,0974 | +0,0974 | ja | - |
| 0 | 4 | 20,972 | 23,363 | 2,3907 | 1,8591 | 1,0551 | +0,0551 | ja | - |
| 0 | 4 | 23,363 | 25,696 | 2,3333 | 1,8915 | 1,0354 | +0,0354 | ja | - |
| 0 | 4 | 25,696 | 27,989 | 2,2927 | 1,9177 | 1,0246 | +0,0246 | ja | - |
| 0 | 4 | 27,989 | 30,251 | 2,2624 | 1,9390 | 1,0180 | +0,0180 | ja | - |
| 0 | 4 | 30,251 | 32,490 | 2,2391 | 1,9566 | 1,0137 | +0,0137 | ja | - |
| 0 | 4 | 32,490 | 34,711 | 2,2206 | 1,9713 | 1,0107 | +0,0107 | ja | - |
| 0 | 4 | 34,711 | 36,917 | 2,2057 | 1,9836 | 1,0086 | +0,0086 | ja | - |
| 0 | 4 | 36,917 | 39,110 | 2,1934 | 1,9942 | 1,0070 | +0,0070 | ja | - |
| 0 | 4 | 39,110 | 41,293 | 2,1832 | 2,0032 | 1,0058 | +0,0058 | ja | - |
| 0 | 5 | 21,816 | 24,324 | 2,5083 | 1,8017 | 1,1079 | +0,1079 | ja | - |
| 0 | 5 | 24,324 | 26,750 | 2,4254 | 1,8387 | 1,0619 | +0,0619 | ja | - |
| 0 | 5 | 26,750 | 29,118 | 2,3681 | 1,8699 | 1,0404 | +0,0404 | ja | - |
| 0 | 5 | 29,118 | 31,444 | 2,3262 | 1,8958 | 1,0284 | +0,0284 | ja | - |
| 0 | 5 | 31,444 | 33,738 | 2,2941 | 1,9175 | 1,0210 | +0,0210 | ja | - |
| 0 | 5 | 33,738 | 36,007 | 2,2689 | 1,9358 | 1,0161 | +0,0161 | ja | - |
| 0 | 5 | 36,007 | 38,256 | 2,2485 | 1,9514 | 1,0127 | +0,0127 | ja | - |
| 0 | 5 | 38,256 | 40,487 | 2,2317 | 1,9647 | 1,0102 | +0,0102 | ja | - |
| 0 | 5 | 40,487 | 42,705 | 2,2177 | 1,9762 | 1,0084 | +0,0084 | ja | - |
| 0 | 6 | 25,134 | 27,665 | 2,5305 | 1,7883 | 1,1190 | +0,1190 | ja | - |
| 0 | 6 | 27,665 | 30,118 | 2,4528 | 1,8223 | 1,0680 | +0,0680 | ja | - |
| 0 | 6 | 30,118 | 32,514 | 2,3967 | 1,8519 | 1,0448 | +0,0448 | ja | - |
| 0 | 6 | 32,514 | 34,869 | 2,3545 | 1,8772 | 1,0318 | +0,0318 | ja | - |
| 0 | 6 | 34,869 | 37,190 | 2,3216 | 1,8988 | 1,0237 | +0,0237 | ja | - |
| 0 | 6 | 37,190 | 39,485 | 2,2952 | 1,9173 | 1,0183 | +0,0183 | ja | - |
| 0 | 6 | 39,485 | 41,759 | 2,2735 | 1,9333 | 1,0145 | +0,0145 | ja | - |
| 0 | 7 | 28,450 | 30,998 | 2,5483 | 1,7778 | 1,1334 | +0,1334 | ja | - |
| 0 | 7 | 30,998 | 33,473 | 2,4746 | 1,8087 | 1,0736 | +0,0736 | ja | - |
| 0 | 7 | 33,473 | 35,893 | 2,4204 | 1,8368 | 1,0488 | +0,0488 | ja | - |
| 0 | 7 | 35,893 | 38,272 | 2,3786 | 1,8612 | 1,0349 | +0,0349 | ja | - |
| 0 | 7 | 38,272 | 40,617 | 2,3454 | 1,8824 | 1,0262 | +0,0262 | ja | - |
| 0 | 7 | 40,617 | 42,935 | 2,3184 | 1,9009 | 1,0203 | +0,0203 | ja | - |
| 0 | 8 | 34,327 | 36,819 | 2,4923 | 1,7974 | 1,0794 | +0,0794 | ja | - |
| 1 | 0 | 4,085 | 6,745 | 2,6599 | 2,1045 | 1,0875 | +0,0875 | ja | chi0 = 3,2e-02 |
| 1 | 0 | 6,745 | 9,254 | 2,5086 | 2,2085 | 1,0334 | +0,0334 | ja | chi0 = 2,2e-03 |
| 1 | 0 | 9,254 | 11,717 | 2,4633 | 2,2575 | 1,0183 | +0,0183 | ja | - |
| 1 | 0 | 11,717 | 14,161 | 2,4434 | 2,2867 | 1,0117 | +0,0117 | ja | - |
| 1 | 0 | 14,161 | 16,593 | 2,4328 | 2,3063 | 1,0082 | +0,0082 | ja | - |
| 1 | 0 | 16,593 | 19,020 | 2,4265 | 2,3204 | 1,0061 | +0,0061 | ja | - |
| 1 | 0 | 19,020 | 21,442 | 2,4223 | 2,3310 | 1,0047 | +0,0047 | ja | - |
| 1 | 0 | 21,442 | 23,862 | 2,4194 | 2,3393 | 1,0037 | +0,0037 | ja | - |
| 1 | 1 | 8,976 | 11,351 | 2,3756 | 1,8696 | 1,0839 | +0,0839 | ja | - |
| 1 | 1 | 11,351 | 13,622 | 2,2702 | 1,9225 | 1,0406 | +0,0406 | ja | - |
| 1 | 1 | 13,622 | 15,839 | 2,2170 | 1,9575 | 1,0240 | +0,0240 | ja | - |
| 1 | 1 | 15,839 | 18,024 | 2,1856 | 1,9817 | 1,0158 | +0,0158 | ja | - |
| 1 | 1 | 18,024 | 20,190 | 2,1655 | 1,9993 | 1,0112 | +0,0112 | ja | - |
| 1 | 1 | 20,190 | 22,341 | 2,1517 | 2,0126 | 1,0083 | +0,0083 | ja | - |
| 1 | 2 | 12,281 | 14,745 | 2,4640 | 1,8323 | 1,1080 | +0,1080 | ja | - |
| 1 | 2 | 14,745 | 17,094 | 2,3487 | 1,8833 | 1,0539 | +0,0539 | ja | - |
| 1 | 2 | 17,094 | 19,378 | 2,2840 | 1,9207 | 1,0322 | +0,0322 | ja | - |
| 1 | 2 | 19,378 | 21,621 | 2,2428 | 1,9486 | 1,0214 | +0,0214 | ja | - |
| 1 | 2 | 21,621 | 23,835 | 2,2143 | 1,9699 | 1,0151 | +0,0151 | ja | - |
| 1 | 3 | 15,584 | 18,100 | 2,5155 | 1,8075 | 1,1260 | +0,1260 | ja | - |
| 1 | 3 | 18,100 | 20,503 | 2,4036 | 1,8540 | 1,0648 | +0,0648 | ja | - |
| 1 | 3 | 20,503 | 22,839 | 2,3353 | 1,8908 | 1,0395 | +0,0395 | ja | - |
| 2 | 0 | 4,798 | 7,593 | 2,7950 | 2,0507 | 1,1075 | +0,1075 | ja | chi0 = 1,6e-02 |
| 2 | 0 | 7,593 | 10,180 | 2,5871 | 2,1769 | 1,0429 | +0,0429 | ja | - |
| 2 | 0 | 10,180 | 12,694 | 2,5133 | 2,2375 | 1,0243 | +0,0243 | ja | - |
| 2 | 0 | 12,694 | 15,172 | 2,4779 | 2,2729 | 1,0160 | +0,0160 | ja | - |
| 2 | 0 | 15,172 | 17,630 | 2,4581 | 2,2962 | 1,0114 | +0,0114 | ja | - |
| 2 | 0 | 17,630 | 20,075 | 2,4458 | 2,3127 | 1,0086 | +0,0086 | ja | - |
| 2 | 0 | 20,075 | 22,513 | 2,4376 | 2,3249 | 1,0067 | +0,0067 | ja | - |
| 2 | 1 | 9,498 | 11,968 | 2,4697 | 1,8310 | 1,1192 | +0,1192 | ja | - |
| 2 | 1 | 11,968 | 14,301 | 2,3337 | 1,8912 | 1,0556 | +0,0556 | ja | - |
| 2 | 1 | 14,301 | 16,565 | 2,2638 | 1,9324 | 1,0324 | +0,0324 | ja | - |
| 2 | 1 | 16,565 | 18,787 | 2,2219 | 1,9613 | 1,0213 | +0,0213 | ja | - |
| 2 | 1 | 18,787 | 20,981 | 2,1944 | 1,9825 | 1,0151 | +0,0151 | ja | - |
| 2 | 1 | 20,981 | 23,157 | 2,1754 | 1,9986 | 1,0113 | +0,0113 | ja | - |
| 2 | 2 | 12,715 | 15,268 | 2,5535 | 1,7977 | 1,1570 | +0,1570 | ja | - |
| 2 | 2 | 15,268 | 17,680 | 2,4113 | 1,8520 | 1,0731 | +0,0731 | ja | - |
| 2 | 2 | 17,680 | 20,011 | 2,3316 | 1,8938 | 1,0426 | +0,0426 | ja | - |
| 2 | 2 | 20,011 | 22,292 | 2,2809 | 1,9255 | 1,0279 | +0,0279 | ja | gekennzeichnete Stelle R = 22,29 |

## 4 LF0 bis LF4

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| LF0 | K0 bestanden (85 %) | **eingetroffen** | pi/k_innen = 2,3681 (Karte 2,37) und 2,0640 (Karte 2,07); Abweichung -0,0019 und -0,0060, Grenze 0,01 |
| LF1 | l = 0, Paare mit R_n >= 15: Delta Phi / pi = 1 auf +-3 % bei mindestens 80 % der Paare (50 %) | **eingetroffen (ohne Puffer)** | 68 von 85 = 80,0 %. Ausserhalb (17): k = 3: 15,16 / 17,60; k = 4: 18,49 / 20,97 / 23,36; k = 5: 21,82 / 24,32 / 26,75; k = 6: 25,13 / 27,66 / 30,12 / 32,51; k = 7: 28,45 / 31,00 / 33,47 / 35,89; k = 8: 34,33 (Reste 0,032 bis 0,133). Knapp innen: k = 3 / 19,94 (0,0298), k = 5 / 29,12 (0,0284), k = 7 / 38,27 (0,0262). k = 0, 1, 2: alle 39 Paare innen |
| LF2 | l = 1 und 2, alle Paare mit R_n >= 10: ebenso bei mindestens 70 % (40 %) | **nicht eingetroffen** | 20 von 32 = 62,5 %; ohne die gekennzeichnete Stelle 19 von 31 = 61,3 %. Je l: l = 1 11 von 18, l = 2 9 von 14. Ausserhalb (12): l = 1, k = 1: 11,35; k = 2: 12,28 / 14,75 / 17,09; k = 3: 15,58 / 18,10 / 20,50; l = 2, k = 1: 11,97 / 14,30; k = 2: 12,72 / 15,27 / 17,68 (Reste 0,032 bis 0,157). Wandkurven k = 0: alle 10 Paare innen |
| LF3 | Delta Phi trifft pi besser als pi/k_innen den Abstand (l = 0) (60 %) | **eingetroffen** | Mittel abs(Rest) 0,0268 gegen Mittel abs((pi/k_innen)/Abstand - 1) 0,1148 (98 Paare); R_n >= 15: 0,0203 gegen 0,1086. pi/k_innen ist in allen 98 Paaren kuerzer als der Abstand (-1,5 % bis -31 %) |
| LF4 | Restabweichung bei mindestens 80 % der Paare mit demselben Vorzeichen (65 %) | **eingetroffen** | 137 von 137 positiv; ebenso je l (98 / 22 / 17) und in den LF1- und LF2-Mengen |

- **Bedeutung (Karte, woertlich):** Ausgeloest waere "Die Leitern fuer l = 0, 1, 2 folgen einer Phasenbedingung der
  Innenwelle [H, im Modell]. Das waere ein geschlossener Baustein der Gesamtformel." nur mit LF1 und LF2; LF2 ist nicht
  eingetroffen. "Das Halbwellenbild ist nur qualitativ; die Restabweichung wird beschrieben." gilt nur, wenn LF1 nicht
  eintrifft; LF1 ist eingetroffen. Fuer diese Kombination ist keine Bedeutung vorab festgelegt. Die Restabweichung ist in
  Abschnitt 5 beschrieben.
- **Empfindlichkeit von LF1 (nur berichtet, Wertung unveraendert):** Mit R_n >= 14 statt 15 kaeme k = 2 / 14,19 (0,038)
  hinzu: 68 von 86 = 79,1 %, nicht eingetroffen. Mit R_n >= 16: 66 von 82 = 80,5 %. Rechenunsicherheit des Rests: R der
  Liste gegen Rchi <= 8,2e-6, S0-Variante <= 9e-8 (R_n >= 10); der knappste Abstand zur 3-%-Grenze (2e-4) ist davon
  nicht beruehrt.

## 5 Restabweichung

### Beschreibung (PLAN 6, vorab festgelegt)

- **Vorzeichen:** In allen 137 Paaren ist Delta Phi > pi.
- **Abhaengigkeit von R:** Auf jeder l = 0-Kurve faellt der Rest streng mit R (Spearman -1,0 auf k = 0 bis 7). Gepoolt
  ueber die Kurven: Spearman -0,50 (l = 0, n = 98), -0,47 (l = 1, n = 22), -0,65 (l = 2, n = 17); das Poolen mischt
  verschieden alte Kurven.
  - Wandkurve l = 0, k = 0: 0,0785 (R_n = 3,2), 0,0297 (5,8), 0,0157 (8,2), 0,0098 (10,6), 0,0067 (13,1), 0,0049 (15,5),
    0,0029 (20,3), 0,0019 (25,1), 0,0014 (30,0), 0,0010 (34,8), 0,0007 (42,0). Bei doppeltem R faellt der Rest auf etwa
    ein Viertel (Faktor 3,6 bis 3,7 von 10,6 auf 21 und von 20 auf 40).
- **Abhaengigkeit von k (l = 0):** Mittel je Kurve 0,0096 / 0,0171 / 0,0239 / 0,0322 / 0,0276 / 0,0341 / 0,0457 / 0,0562
  (k = 0 bis 7). Bei gleichem R steigt der Rest mit k, z. B. R_n ~ 38: k = 0: 0,0009; 1: 0,0012; 2: 0,0021; 3: 0,0039;
  4: 0,0070; 5: 0,0102; 6: 0,0183; 7: 0,0262.
  - Deutlicher als k selbst ordnet das Alter der Kurve: erstes Paar nach der Geburt 0,079 bis 0,205, zweites 0,030 bis
    0,086, drittes 0,016 bis 0,049 (l = 0). Jede Kurve beginnt mit einem grossen Rest, der dann schnell faellt.
- **Abhaengigkeit von l:** Bei gleichem k und aehnlichem R groesser fuer hoeheres l, z. B. Wandkurve bei R ~ 15: l = 0:
  0,0049 (R_n = 15,5), l = 1: 0,0082 (14,2), l = 2: 0,0114 (15,2). Mittel je l: 0,027 / 0,037 / 0,045.
- **pi/k_innen gegen Abstand:** Die einfache Halbwellenregel liegt in allen l = 0-Paaren zu kurz, auf der Wandkurve um
  1,5 bis 16 %, auf jungen Kurven bis 31 %. Grund in der Rechnung: k_innen faellt laengs jeder Kurve (omega^2 und rho
  sinken), der Term R Delta k gehoert zur Phase; Delta Phi enthaelt ihn.
- **Kontrolle S0:** Mit S0 aus der Wurzel von U_S(S0) = omega^2 statt aus dem Profil aendert sich der Rest um hoechstens
  9e-8 (R_n >= 10) bzw. 0,0072 (kleinste R).

### Eigene Deutung [H], nachtraeglich, getrennt (keine Wertung)

- **l-Anteil auf der Wandkurve = Nullstellenabstand von j_l [H].** Fuer die Nullstellen von j_l gilt
  z_n ~ beta_n - l(l+1)/(2 beta_n) (McMahon), der Abstand ist also um l(l+1)/(2 pi) (1/Phi_n - 1/Phi_n+1) groesser als
  pi. Der Mehrrest von l = 1, 2 gegenueber l = 0 auf k = 0 (l = 0-Rest linear in R_n interpoliert, hilfs/mcmahon-k0.jq):

| l | R_n | Rest | Rest l = 0 (interpoliert) | Mehrrest | McMahon-Term | Verhaeltnis |
|---|---|---|---|---|---|---|
| 1 | 4,09 | 0,0875 | 0,0617 | 0,0258 | 0,0177 | 1,46 |
| 1 | 6,75 | 0,0334 | 0,0241 | 0,0093 | 0,0082 | 1,14 |
| 1 | 9,25 | 0,0183 | 0,0132 | 0,0051 | 0,0049 | 1,05 |
| 1 | 11,72 | 0,0117 | 0,0084 | 0,0033 | 0,0032 | 1,02 |
| 1 | 14,16 | 0,0082 | 0,0059 | 0,0023 | 0,0023 | 1,00 |
| 1 | 16,59 | 0,0061 | 0,0043 | 0,0017 | 0,0017 | 1,00 |
| 1 | 19,02 | 0,0047 | 0,0033 | 0,0013 | 0,0014 | 0,99 |
| 1 | 21,44 | 0,0037 | 0,0026 | 0,0011 | 0,0011 | 0,99 |
| 2 | 4,80 | 0,1075 | 0,0481 | 0,0594 | 0,0388 | 1,53 |
| 2 | 7,59 | 0,0429 | 0,0193 | 0,0236 | 0,0194 | 1,22 |
| 2 | 10,18 | 0,0243 | 0,0109 | 0,0134 | 0,0121 | 1,11 |
| 2 | 12,69 | 0,0160 | 0,0072 | 0,0088 | 0,0083 | 1,06 |
| 2 | 15,17 | 0,0114 | 0,0051 | 0,0063 | 0,0061 | 1,04 |
| 2 | 17,63 | 0,0086 | 0,0038 | 0,0047 | 0,0046 | 1,02 |
| 2 | 20,08 | 0,0067 | 0,0030 | 0,0037 | 0,0037 | 1,02 |

  - Lesart [H]: Der l-Versatz -l pi/2 der Karte faellt in der Differenz heraus, sein 1/Phi-Nachlauf nicht. Auf der
    Wandkurve erklaert dieser Nachlauf den l-Anteil fast vollstaendig; die lineare Interpolation des l = 0-Rests
    ueberschaetzt dabei wegen der Kruemmung leicht. Fuer innere Kurven ist der Vergleich nach Rang nicht Gleiches mit
    Gleichem (HUELLEN-QUADRUPOL: l = 2, Rang k liegt nahe l = 0, Rang k + 1); nicht gerechnet.
- **l = 0-Rest als fester Radiusversatz [H].** Setzt man Delta(k_innen (R + a)) = pi, folgt je Paar
  a = pi Rest / (-Delta k_innen) (hilfs/versatz-a.jq). Laengs jeder Kurve laeuft a gegen einen fast festen Wert:
  k = 0: 3,07 -> 2,13; k = 1: 5,9 -> 2,50; k = 2: 8,2 -> 2,46; k = 3: 11,4 -> 2,53; k = 4: 7,3 -> 2,79; k = 5: 8,8 -> 3,07;
  k = 6: 10,6 -> 3,65; k = 7: 13,2 -> 4,26 (erstes -> letztes Paar). Auf reifen Kurven (k = 0 bis 3 bei R ~ 40; k = 4 bis 7 fallen am Ende der Daten noch) ist a ~ 2,1 bis 2,5, also ein
  Bezugspunkt der Innenwelle etwa 2 Laengeneinheiten ausserhalb des Huellenradius chi = 1/2. Nahe der Geburt einer
  Kurve passt kein fester Versatz; dort wirkt nach dieser Lesart noch etwas anderes, vermutlich die Form des jungen
  chi-Zustands nahe der Schwelle rho = sqrt2.
- **Kandidat fuer den Baustein [H, nicht gewertet, keine Vorhersage]:** Phase(R_n) = k_innen (R_n + a) - l pi/2 -
  l(l+1)/(2 k_innen (R_n + a)) = n pi + konst, mit a ~ 2,1 bis 2,5, auf reifen Kurven. Pruefbar waere er nur mit vorab
  festgelegtem a an neuen Stellen.

## 6 Latten, Grenzen, Selbstanzeigen, Laufzeiten, sha256

### Latten L1 bis L5

- Die Definitionen der Latten L1 bis L5 stehen nicht in meinen freigegebenen Quellen; ich gebe sie nicht aus dem
  Gedaechtnis wieder. Die Karte ordnet diesen Lauf der Latte L4 zu: nachtraegliche Erklaerung vorhandener Daten.
- Was der Lauf liefert: eine vorab festgelegte, rechnerisch geschlossene Wertung einer Erklaerung (LF1 bis LF4) an 137
  bekannten Paaren. Was er nicht liefert: keine neue Lagevorhersage, keine neue Stelle, keine zweite Gitterstufe fuer S0,
  keine Fremdpruefung, keine Messdaten.

### Grenzen

- **LF1 ohne Puffer:** 80,0 % bei Schwelle 80 %. Der formale Ausgang haengt an der Grenze R_n >= 15 (bei 14 waere er
  umgekehrt) und an einem Paar mit Rest 0,0298.
- **Nachtraeglich:** Alle Stellen waren bekannt, die Karte und die Vorhersagen entstanden nach Sicht der Sprossenlagen.
  Die [H]-Teile (McMahon-Vergleich auf k = 0, Radiusversatz a) sind nach dem Ergebnis gerechnet.
- **Formel der Runde 18:** setzt im Inneren chi = 0 und U_S = omega^2 voraus. Bei R < 7 gilt das nur grob (chi(0) bis
  0,074, S0 weicht bis 0,015 von der Wurzel ab); diese Paare liegen ausserhalb der LF1-/LF2-Mengen.
- **R der Liste:** Runde 18, DIPOL und QUADRUPOL geben R aus der Halbierung (Abstand zu Rchi am Profil der Stelle
  <= 8,2e-6), die Newton-Quellen auf <= 7,4e-11. Auf den Rest wirkt das hoechstens ~1e-5.
- **Nur Stufe 1** fuer S0; die Hintergruende beider Stufen unterscheiden sich nach Runde 18 um ~1e-10 (dQ/Q).
- **Lueckenlosigkeit** jenseits der vollstaendigen Suchen (l = 0: R > 39; l = 1, 2: R > 19,4) nur ueber Umlaufwechsel und
  Abstand geprueft, wie in den Vorlaeufern.
- **Eine Stimme**, keine Fremdpruefung. Modell M2, linear, klassisch, modellintern.

### Selbstanzeigen

- **Programmfehler in Fassung 1** (code/leiterformel.py 12a11d64...): Das Ausgabefeld "k" (Kurvenindex) wurde mit dem
  Wert von k_innen ueberschrieben. Die K0-Zahlen waren davon nicht betroffen (pi/k aus dem Funktionswert, Log mit dem
  Eingabeindex). Der Stellenlauf der Fassung 1 (r21lf-stellen) wurde verworfen, bevor ich ihn ausgewertet habe. Behoben
  nur durch Umbenennen des Felds in "k_innen" (Fassung 2, 7e2dac14...; diff: 7 Zeilen, nur Feldname), dann K0 und alle
  Stellen neu (r21lf-k0-v2, r21lf-stellen-v2). Die Ausgaben der Fassung 1 liegen ungenutzt als aus/k0.json und
  aus/stellen-0-156.json, die Fassung 1 als hilfs/leiterformel-fassung1-12a11d64.py.txt. Gegenprobe mit jq: Phi und S0
  aller 156 Stellen und pi/k_innen von K0 sind in beiden Fassungen bitgleich.
- **Lesen ausserhalb der Freigabe:** RUNDE-18/huellen-leiter/KARTE.md (im selben Befehl wie die PLAN-Dateien).
  Ordnerlisten (nur Namen) der fuenf Vorlaeuferordner (zeigten hilfs/, logs/, KARTE, FREMDSTIMME u. a.; nicht geoeffnet)
  und von RUNDE-18 aus/laeufe, aus/prof. Nichts aus Sperrbereichen.
- **.69:** Einmal die Eintraege von /home/fmh/fmhc-physics-remote/ gezaehlt (`ls | grep -c .`, nur die Zahl, keine
  Namen angezeigt), um vor dem Anlegen meines Ordners den Pfad zu pruefen. Sonst ausserhalb meines Ordners nur
  runde18-huellen-leiter/aus/prof-st1 gelistet und gelesen (Ankerprofile). Angelegt nur
  /home/fmh/fmhc-physics-remote/runde21-leiterformel/. py_compile direkt mit dem venv-Python, danach rm -rf
  code/__pycache__ in meinem Ordner. Keine Prozesse beendet, kleintest.sh nicht gelesen.
- **Lokal:** nur jq, grep, sed, cut, tr, cp, mkdir, ls, cat, head, tail, wc, diff, chmod, sha256sum, rsync, ssh, date, dazu
  bash fuer hilfs/baue-eingabe.sh und echo. Ein gequoteter Heredoc fuer hilfs/versatz-a.jq. Kein python, awk oder bc.
- **Nachtraegliche Rechnungen mit jq** (hilfs/mcmahon-k0.jq, hilfs/versatz-a.jq): nach dem Ergebnis, nur fuer [H].
- Nichts in den Scratchpad geschrieben. Kein git, kein Peerbus, keine Unteragenten, keine Literatur.

### Laufzeiten (.69, kleintest.sh; Service runtime; UTC)

| Lauf | Spur | Start | Ende | Dauer | rc | gewertet |
|---|---|---|---|---|---|---|
| r21lf-k0 (Fassung 1) | cpu | 16:46:52 | 16:46:53 | 1,2 s | 0 | K0 zuerst, Zahlen = Fassung 2 |
| r21lf-stellen (Fassung 1) | cpu | 16:47:04 | 16:47:52 | 48,4 s | 0 | nein (Programmfehler) |
| r21lf-k0-v2 | cpu | 16:48:27 | 16:48:28 | 1,1 s | 0 | ja |
| r21lf-stellen-v2 (156 Stellen) | cpu | 16:48:32 | 16:49:21 | 48,4 s | 0 | ja |
| r21lf-ausw | cpu2 | 16:50:32 | 16:50:34 | 2,2 s | 0 | ja |

- Zusammen 101 s Spurzeit, dazu zweimal py_compile direkt (unter 1 s). Kein Lauf nahe der 600-s-Grenze.

### sha256

Code (lokal = .69):

```
7e2dac1462768c030e8ec29bc590ce1695f6555f8fb0becdfd2f9d2d82fa9576  code/leiterformel.py (Fassung 2, gewertet)
12a11d6432cef4134aa80b9979c1e68181dbf1f9fb54e2a8594b5abcc8e4b231  code/leiterformel.py Fassung 1 (= hilfs/leiterformel-fassung1-12a11d64.py.txt)
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py (Runde 18, unveraendert)
68c0a1fb9195550e4d93384304ba506c78e3239fbe9cd8a95e5571fa4e6bc45b  code/huellen_leiter.py (Runde 18, unveraendert)
```

Plan:

```
b2a9c0b3c7f772da0d2c709f89966aa3ce094eb57bc50e72cc79204bed7c542e  PLAN.md.eingefroren-20261002-184429 (PLAN.md gleich)
```

Ausgaben (lokal = .69):

```
8fee06efcc12a582489e9623ac579005f727223743c9f7bad7f769b6184dd7bd  aus/k0-v2.json
a818f55db2536c27d4c6d0ae6f4d63fd3a7c8ee1b88755e28e072807ed3a78fb  aus/stellen-v2-0-156.json
73f667ab0c1bc4f8a6986136e46550881fe42abab25125895883aaddf9a0ff62  aus/auswertung.json
7bd0b4f935e2b9dd5e3048543d10eb276984124fb7f8a01e2579ddaacf53fb08  aus/paare-tabelle.md
306e14820161a464bf95047d1eeb63c28a912089e48336a0b9f0509e96693d26  aus/k0.json (Fassung 1, ungenutzt)
b23996d0610019cc8e4f879a9ae5d76df88907be311bcb0c443f311fee41437b  aus/stellen-0-156.json (Fassung 1, verworfen)
```

Hilfsdateien:

```
fe94ec8547148eb5d4369f2924a1278e084ae9bcb6832d74cbf782673358a908  hilfs/stellen-eingabe.json (lokal = .69)
3840a2d18b6c8087f7548e99a52f54b6b60acc08baef5b721f10e64c22396c87  hilfs/baue-eingabe.sh
42f1f22c2f716471726962f86b697427163a663f364a4a594dfce211ec08c3c8  hilfs/mcmahon-k0.jq
7c5c914c709e88a137019b84a43ab08759be376abbc40d82c8df33142cb1cf6b  hilfs/mcmahon-k0-ausgabe.json
b50101958003e75acf9d6b9bd1b2b20dd5ce60bed5cb53ceb1f8bdfcac2fcaaf  hilfs/versatz-a.jq
228060195bdb062618e4eeb667ad3e8978545d8e852a0e4f476ebda594209bb2  hilfs/versatz-a-ausgabe.json
```

- Logs lokal unter logs/ (ssh-Ausgabe der kleintest-Aufrufe).

## 7 Einfach gesagt

Die stillen Stellen eines grossen Q-Balls liegen auf Leitern. Die Idee war: Im Inneren des Balls laeuft eine Welle, und
jedes Mal, wenn bis zur Wand eine halbe Welle mehr hineinpasst, kommt eine neue Sprosse. Wir haben das an 137
Sprossenpaaren nachgerechnet, dabei aber beruecksichtigt, dass sich die Welle von Sprosse zu Sprosse leicht aendert.
Auf eingespielten Leitern stimmt die Regel sehr gut, bei grossen Baellen auf ein paar Promille, viel besser als die
alte Faustregel mit festem Abstand. Auf ganz jungen Leitern, kurz nachdem sie entstanden sind, liegt sie bis zu 20 %
daneben, und zwar immer in dieselbe Richtung. Nach den vorher festgelegten Regeln ist die Regel deshalb fuer die Atmung
gerade noch bestanden, fuer Kippen und Verformen nicht. Nachtraeglich sieht man zwei einfache Korrekturen, die viel
vom Rest erklaeren: eine kleine Verschiebung des Bezugspunkts an der Wand und, fuer Kippen und Verformen, die bekannte
Form kugelfoermiger Wellen; das ist aber noch nicht vorab getestet.
