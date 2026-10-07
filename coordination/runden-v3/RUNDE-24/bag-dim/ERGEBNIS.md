# BAG-DIM: Ergebnis (Code-Agent, Runde 24, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 00:32:46 CEST (date).
- Rauchlaeufe R1 bis R3 (Graphen und Q-Raster in keinem echten Lauf): .69, 22:45:25 bis 22:52:42 UTC.
- Plan eingefroren 2026-10-03 00:56:57 CEST (PLAN.md.eingefroren-20261003-005657), nach den Rauchlaeufen und vor jedem
  echten Lauf.
  - Code: code/bagdim.py, sha256 d6d4276511eae6d5ec99a1940cbef9a93a1d890223c362c1373ff2838c0fa53c
  - Auswertung: code/auswertung.py, sha256 76e1798043e4f23c39e96daa4e3bb6da312e2c382f3b603ca77236d0682eee19
  - Startskript: code/start_haupt.sh, sha256 e6802ca8d32a57fdb3c2a4901a7e0be4e9d795598e71098aee58060968f57643
  - Alle vor dem Einfrieren geschrieben, lokal = .69, schreibgeschuetzt.
- **Echte Laeufe:** .69, 22:57:02 bis 23:14:23 UTC; 20 Aufrufe ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4,
  cpu6), alle rc = 0, keiner ueber das Budget; kein Restlauf noetig.
- Auswertung mechanisch mit auswertung.py auf der .69 (kleintest.sh, cpu4, 23:14:33 bis 23:14:34 UTC), ueber
  lauf/haupt. Tabellen lokal mit jq aus lauf-69/.
- Ergebnis geschrieben ab 2026-10-03 01:10:02 CEST (date): zuerst Gliederung und Gitter-Teile, waehrend die letzten
  Sierpinski-Laeufe rechneten; die Zahlen der Auswertung ab 01:15:52 CEST. Ende in der letzten Zeile.
- Explorativ (v3). Deutungen [H, Modell FLS mit lam = g = 1, Graphen mit Knoten- und Kantengewicht 1].

## Ergebnis zuerst

1. **Auf dem 2D- und dem 3D-Gitter folgt der Beutel dem Beutelgesetz fast exakt.**
   - p am grossen Ende: 2D 0,6668 (Reff 43 bis 64), 3D 0,7507 (Reff 19,5 bis 26,4). BD1 und BD2 sind eingetroffen.
   - Auch der Vorfaktor des idealen Beutels stimmt.
     - 2D: E/(3,130 Q^(2/3)) - 1 = -3,6e-4 bei Reff 58
     - 3D: E/((4 pi/3) Q^(3/4)) - 1 = -1,1e-3 bei Reff 26
     - (4 pi/3) Q^(3/4) ist auch der Fuehrungsterm von Heeck und Sokhashvili (2023) fuer unsere Parameter [S; Umrechnung
       eigen].
   - Bei kleinen Beuteln liegt der oertliche Exponent ueber dem Grenzwert: 0,693 bei Reff 3,9 (2D), 0,777 bei Reff 4,4
     (3D). Er naehert sich ihm etwa wie 1/R^2.
2. **Auf dem Sierpinski-Dreieck misst der Beutel die spektrale Dimension, nicht die Hausdorff-Dimension.**
   - Mechanisch (Sekante ueber zwei volle Perioden am oberen Ende, k 18 bis 34): **p = 0,5903**. BD3 ist eingetroffen
     (0,577 +- 0,03 und naeher an 0,577 als an 0,613).
   - Der oberste Punkt zieht den Wert nach oben. Dort liegt der tiefste zentrale Beutel ueber der Plan-Grenze
     nB <= N/4, und die Regel nimmt einen Nebenast (Kontrollen). Die anderen 18 Zwei-Perioden-Sekanten liegen bei
     0,5735 bis 0,5792 (Mittel 0,5765).
   - E/Q^0,5772 schwingt log-periodisch zwischen 2,63 und 2,84, ohne Drift. Die Periode ist Faktor 3 sqrt5 = 6,708 in
     Q, also Faktor 2 im Radius. Die Minima je Periode: 2,6289 / 2,6359 / 2,6315 / 2,6305 (k = 5, 13, 21, 29).
   - E/Q^0,6131 (Hausdorff-Variante) faellt dagegen stetig von 2,36 auf 1,87.
   - Die Beutel rasten auf Teildreieck-Vereinigungen ein. nB = 29, 83, 245 sind genau zwei Teildreiecke der Stufen 2
     bis 4 am Mittelknoten; 743 und 2353 sind etwas mehr als zwei der Stufen 5 und 6 (731 bzw. 2189). Einmal je
     Periode springt der Beutel eine Stufe hoeher.
3. **Auf dem Zufallsgraphen entsteht gar kein Beutel.**
   - Jeder Beutelstart zerfliesst. Der tiefste Zustand ist eine ueber den ganzen Graphen verteilte Welle mit E knapp
     unter Q: E/Q = 0,9997 bei Q = 10, 0,901 bei Q = 3162.
   - p ueber die obere halbe Dekade: 0,933. BD4 ist damit eingetroffen.
   - Ab Q ~ 4e3 geht der ganze Graph in den Beutelzustand (chi = 0 ueberall, E -> N/4 = 2500).
4. **K0: BD0 ist nicht eingetroffen, wegen des 3D-Gitters.**
   - Plateaus: Sierpinski (Stufe 8) 1,307, 2D 1,949, 3D 2,833 (Schranke 2,85).
   - Der 3D-Fehlbetrag ist der Randterm der Spur auf dem offenen Gitter.
     - Die Spur des offenen Pfads ist n q(t) + 1/2 mit q(t) = e^(-2t) I_0(2t).
     - Das gibt d_s(t) ~ 3 (1 + 1/(8t))/(1 + sqrt(pi t)/n) mit n = 81.
     - Das ergibt 2,840 bei t = 10 und 2,723 bei t = 24; gemessen 2,842 und 2,724 [Rechnung von Hand].
   - Die Beutel sitzen im Inneren, weit weg vom Rand. BD1 bis BD4 beruehrt das nicht [H].
5. **Nebenbefunde.**
   - Auf endlichen Graphen mit Rand liegt ein Beutel in der Gitterecke bzw. abseits der Mitte tiefer als der Beutel am
     Mittelknoten: -20 % und -37 % (2D), -13 % und -16 % (Sierpinski).
   - Der Beutel am Mittelknoten ist dort ein oertliches Minimum.
   - Auf dem Sierpinski-Dreieck gibt es viele Nebentaeler (Starts enden bis 38 % hoeher). Auf den Gittern enden alle
     Beutelstarts in derselben Loesung.
   - dE/dQ = omega gilt auf hoechstens 9,2e-7 (relativ).

## Vorab gegen Ausgang

Mechanisch nach PLAN.md Abschnitt 5 (auswertung.py, lauf-69/auswertung/auswertung.json).

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang |
|---|---|---|---|
| BD0 | K0: d_s-Plateau Sierpinski 1,365 +- 0,08; Gitter 2 und 3 je +- 0,15 | 75 % | **nicht eingetroffen**: Sierpinski 1,307 (Schwankung 3,7 %, t = 431 bis 1771), 2D 1,949 (3,3 %), **3D 2,833** (6,8 %; Schranke 2,85) |
| BD1 | 2D: p am grossen Ende 2/3 +- 0,03 | 70 % | **eingetroffen**: 0,66683 (k 22 bis 26, Q 5,6e4 bis 1,78e5, Reff 43 bis 64); Abstand +1,6e-4 |
| BD2 | 3D: p am grossen Ende 3/4 +- 0,03 | 60 % | **eingetroffen**: 0,75069 (k 18 bis 22, Q 1,8e5 bis 5,6e5, Reff 19,5 bis 26,4); Abstand +6,9e-4 |
| BD3 | Sierpinski: p ueber volle Perioden 0,577 +- 0,03 und naeher an 0,577 als an 0,613 | 45 % | **eingetroffen**: 0,5903 (zwei Perioden, k 18 bis 34, Q 4345 bis 1,96e5, Rg 34 bis 100); Abstand +0,013 zu 0,577, -0,023 zu 0,613. Oberster Punkt auf einem Nebenast (Kontrollen) |
| BD4 | Zufallsgraph: p am grossen Ende > 0,85 | 55 % | **eingetroffen**: 0,933 (k 16 bis 20, Q 1000 bis 3162); dabei gibt es keinen Beutel (Punkt 3) |

- Beutelbereiche (zusammenhaengend, kompakter Beutel am Mittelknoten):
  - 2D: k 0 bis 26 (3,25 Dekaden, Reff 3,9 bis 63,8)
  - 3D: k 0 bis 22 (2,75 Dekaden, Reff 4,4 bis 26,4)
  - Sierpinski: k 0 bis 34 (3,51 Dekaden, Rg 4 bis 100)
  - Die Karte verlangt mindestens 1,5 Dekaden.
- Zufallsgraph: nicht fuellend von k = 0 bis 20 (Q 10 bis 3162); ab k = 21 ist der ganze Graph im Beutelzustand (dort
  konvergiert kein Start, siehe Kontrollen).

**Bedeutung (nach Karte):**
- BD1 bis BD3 treffen ein, also gilt die erste Zeile der Karte: "Die Masse-Ladungs-Beziehung eines Beutel-Teilchens
  misst die spektrale Dimension seines Raums, auch auf einem Fraktal [H, Modell FLS]. Ein solches Teilchen ist ein
  'Dimensionsmesser' fuer entstandene Graphen (Anschluss an URSUPPE und CDT)."
  - Auf dem Fraktal ist der Wert nach Plan 0,590. Ohne den Nebenast-Punkt liegen alle Zwei-Perioden-Sekanten naeher
    an 0,577 (0,5735 bis 0,5792).
  - [H] Entscheidend ist omega = sqrt(lambda_1) ~ R^(-d_w/2) im Beutel: die Laufdimension d_w = log5/log2 statt 1. Das
    Volumen allein (Hausdorff-Dimension) gaebe 0,613. Dieser Fall ist durch die Drift von E/Q^0,6131 klar
    ausgeschlossen.
- BD4 trifft ein: "Ohne endliche Dimension gibt es kein Beutelgesetz."
  - Der Ausgang geht weiter als die Karte: Es gibt dort gar keinen Beutel.
  - Auf einem 6-regulaeren Zufallsgraphen hat jede Kugel einen Dirichlet-Eigenwert von mindestens etwa
    6 - 2 sqrt5 = 1,53 (Baumschranke) [H, Kopfrechnung]. Ein Beutel haette also omega >= 1,24 und damit mehr Energie
    je Ladung als die freie Welle mit omega ~ 1.
  - Das "massige" Teilchen der Karte ist hier eine Welle ueber den ganzen Graphen (E ~ m Q mit m = 1).
- BD0 deckt die Karte mit keiner Bedeutungszeile ab. Beschreibung:
  - Das Messgeraet (Spur des Waermeleitungskerns, Plateau-Regel wie URSUPPE-1) trifft 2D und das Fraktal.
  - Auf dem offenen 81^3-Gitter liegt es 0,167 zu tief, also 0,017 jenseits der Schranke, wegen des Randanteils der Spur.
  - [H] Fuer entstandene Graphen mit Rand braucht der "Dimensionsmesser" eine Randkorrektur. Ein Beutel im Inneren
    braucht sie nicht.
- **Einschraenkungen:**
  - ein Modell (FLS, lam = g = 1, also m_chi = m_phi), Einheitsgewichte
  - endliche Graphen; 3D nur bis Reff 26 (Karte: grob 6 bis 60), 2D bis 64, Sierpinski bis Rg 100
  - Sierpinski: nur ein Mittelknoten-Typ (Seitenmitte), nur Stufe 9; viele Nebentaeler, vier Starts je Q
  - Zufallsgraph: ein N, eine Saat

## Tabellen

**K0: spektrale Dimension** (Spur des Waermeleitungskerns, Plateau-Regel von URSUPPE-1: Fenster [t, 4t] mit kleinster
relativer Schwankung, P(t) > 2 c/N, t >= 0,5)

| Graph | N | Verfahren | Plateau d_s | Fenster t | Schwankung | Soll (Karte) | im Soll |
|---|---|---|---|---|---|---|---|
| Sierpinski Stufe 8 | 9843 | eigvalsh, 218 s | 1,307 | 431 bis 1771 | 3,7 % | 1,365 +- 0,08 | ja |
| 2D-Gitter 241^2 | 58081 | Produktformel | 1,949 | 9,8 bis 40,4 | 3,3 % | 2 +- 0,15 | ja |
| 3D-Gitter 81^3 | 531441 | Produktformel | 2,833 | 5,4 bis 22,0 | 6,8 % | 3 +- 0,15 | **nein** |
| Zufall 6-regulaer, N = 1e4 | 10000 | eigvalsh, 233 s | (7,13) | 0,82 bis 3,38 | 58 % (kein Plateau) | nur berichtet | - |

- Sierpinski: d_s(t) schwingt fuer t = 4 bis 330 zwischen 1,29 und 1,41, mit einer Periode von etwa Faktor 5 in t
  (Zeit mal 5 = Laenge mal 2). Das Fenster der Regel liegt spaet, wo d_s leicht absinkt.
- 3D: gemessen d_s(t) = 2,969 / 2,901 / 2,842 / 2,724 bei t = 4,3 / 6,6 / 10,1 / 24,0. Die Randformel 3 (1 + 1/(8t))/(1 + sqrt(pi
  t)/81) gibt 2,955 / 2,895 / 2,840 / 2,723 [Rechnung von Hand, nachtraeglich]. Der Term 1 + 1/(8t) ist die Naeherung
  des Gitteranteils fuer grosses t; bei t = 4 ist sie noch 0,014 zu klein.
- 2D: Dieselbe Formel mit Faktor 2 und n = 241 gibt bei t = 24 1,940; gemessen 1,941.

**Ideale Beutel zum Vergleich** (Karte, B = 1/4): 2D E = 3 pi B R^2 mit Q = 2 pi B R^3/j_0, also E = 3,130 Q^(2/3); 3D E =
(4 pi/3) Q^(3/4) mit Q = R^4. Nachtraeglich, ohne Wertung:

| Gitter | Reff | E/(c Q^p) - 1 | (p_omega - p_unendlich) R^2 |
|---|---|---|---|
| 2D | 10,5 / 21,5 / 43,2 / 57,8 | -4,5e-3 / -1,3e-3 / -5,1e-4 / -3,6e-4 | 0,35 / 0,32 / 0,41 / 0,46 |
| 3D | 8,9 / 16,7 / 26,4 | -9,1e-3 / -2,6e-3 / -1,1e-3 | 0,43 / 0,36 / 0,35 |

- Die Korrektur zum oertlichen Exponenten faellt also etwa wie 1/R^2, nicht wie 1/R. [H] Eine positive Wandspannung
  allein gaebe 1/R und p unter dem Grenzwert. Hier liegt p darueber; wahrscheinlich hebt das Hineinlecken von f in die
  Wand (groesserer wirksamer Radius) den Wandterm bei m_chi = m_phi fast auf. Nicht getrennt geprueft.

**2D-Gitter (g2:241)**, Raster Q = 100 x 10^(k/8). p (bis k+1) = Sekante zum naechsten k; p_omega = Q omega/E.

| k | Q | E | p (bis k+1) | p_omega | nB | Reff | Start |
|---|---|---|---|---|---|---|---|
| 0 | 100,00 | 65,54887 | 0,6891 | 0,6927 | 49 | 3,9 | frisch_x0.667 |
| 1 | 133,35 | 79,92868 | 0,6834 | 0,6859 | 69 | 4,7 | fort |
| 2 | 177,83 | 97,30372 | 0,6793 | 0,6812 | 89 | 5,3 | frisch |
| 3 | 237,14 | 118,3159 | 0,6763 | 0,6777 | 109 | 5,9 | frisch |
| 4 | 316,23 | 143,7423 | 0,6741 | 0,6751 | 145 | 6,8 | fort |
| 5 | 421,70 | 174,5209 | 0,6724 | 0,6732 | 177 | 7,5 | frisch |
| 6 | 562,34 | 211,7877 | 0,6712 | 0,6717 | 221 | 8,4 | fort |
| 7 | 749,89 | 256,9185 | 0,6702 | 0,6706 | 277 | 9,4 | fort |
| 8 | 1000,0 | 311,5798 | 0,6694 | 0,6698 | 349 | 10,5 | frisch_x0.667 |
| 9 | 1333,5 | 377,7900 | 0,6689 | 0,6691 | 421 | 11,6 | fort |
| 10 | 1778,3 | 457,9942 | 0,6684 | 0,6686 | 517 | 12,8 | fort |
| 11 | 2371,4 | 555,1554 | 0,6681 | 0,6683 | 649 | 14,4 | frisch |
| 12 | 3162,3 | 672,8613 | 0,6678 | 0,6679 | 793 | 15,9 | fort |
| 13 | 4217,0 | 815,4608 | 0,6676 | 0,6677 | 973 | 17,6 | fort |
| 14 | 5623,4 | 988,2204 | 0,6674 | 0,6675 | 1201 | 19,6 | frisch |
| 15 | 7498,9 | 1197,522 | 0,6673 | 0,6674 | 1457 | 21,5 | fort |
| 16 | 10000,0 | 1451,096 | 0,6672 | 0,6672 | 1781 | 23,8 | frisch_x1.5 |
| 17 | 13335 | 1758,312 | 0,6671 | 0,6672 | 2177 | 26,3 | frisch |
| 18 | 17783 | 2130,515 | 0,6670 | 0,6671 | 2653 | 29,1 | fort |
| 19 | 23714 | 2581,455 | 0,6670 | 0,6670 | 3241 | 32,1 | frisch |
| 20 | 31623 | 3127,790 | 0,6669 | 0,6670 | 3945 | 35,4 | frisch |
| 21 | 42170 | 3789,699 | 0,6669 | 0,6669 | 4817 | 39,2 | fort |
| 22 | 56234 | 4591,631 | 0,6669 | 0,6669 | 5853 | 43,2 | fort |
| 23 | 74989 | 5563,209 | 0,6668 | 0,6668 | 7129 | 47,6 | frisch |
| 24 | 100000 | 6740,318 | 0,6668 | 0,6668 | 8677 | 52,6 | fort |
| 25 | 133352 | 8166,437 | 0,6668 | 0,6668 | 10509 | 57,8 | fort |
| 26 | 177828 | 9894,241 |  | 0,6668 | 12801 | 63,8 | frisch |

**3D-Gitter (g3:81)**, Raster Q = 1000 x 10^(k/8).

| k | Q | E | p (bis k+1) | p_omega | nB | Reff | Start |
|---|---|---|---|---|---|---|---|
| 0 | 1000,0 | 716,2047 | 0,7740 | 0,7767 | 365 | 4,4 | frisch |
| 1 | 1333,5 | 894,9222 | 0,7694 | 0,7715 | 461 | 4,8 | fort |
| 2 | 1778,3 | 1116,774 | 0,7658 | 0,7675 | 619 | 5,3 | fort |
| 3 | 2371,4 | 1392,173 | 0,7629 | 0,7643 | 799 | 5,8 | fort |
| 4 | 3162,3 | 1734,047 | 0,7606 | 0,7617 | 1021 | 6,2 | fort |
| 5 | 4217,0 | 2158,427 | 0,7587 | 0,7596 | 1357 | 6,9 | fort |
| 6 | 5623,4 | 2685,219 | 0,7572 | 0,7579 | 1791 | 7,5 | fort |
| 7 | 7498,9 | 3339,103 | 0,7560 | 0,7565 | 2301 | 8,2 | frisch |
| 8 | 10000 | 4150,733 | 0,7549 | 0,7554 | 2945 | 8,9 | fort |
| 9 | 13335 | 5158,132 | 0,7541 | 0,7545 | 3791 | 9,7 | fort |
| 10 | 17783 | 6408,483 | 0,7534 | 0,7537 | 4777 | 10,4 | frisch_x0.667 |
| 11 | 23714 | 7960,349 | 0,7528 | 0,7531 | 6043 | 11,3 | fort |
| 12 | 31623 | 9886,404 | 0,7524 | 0,7526 | 7809 | 12,3 | frisch |
| 13 | 42170 | 12276,83 | 0,7520 | 0,7522 | 9771 | 13,3 | fort |
| 14 | 56234 | 15243,55 | 0,7517 | 0,7518 | 12269 | 14,3 | fort |
| 15 | 74989 | 18925,43 | 0,7514 | 0,7515 | 15515 | 15,5 | fort |
| 16 | 100000 | 23494,84 | 0,7512 | 0,7513 | 19597 | 16,7 | frisch |
| 17 | 133352 | 29165,64 | 0,7510 | 0,7511 | 24765 | 18,1 | fort |
| 18 | 177828 | 36203,28 | 0,7509 | 0,7509 | 31103 | 19,5 | fort |
| 19 | 237137 | 44937,11 | 0,7507 | 0,7508 | 38953 | 21,0 | fort |
| 20 | 316228 | 55775,89 | 0,7506 | 0,7507 | 48885 | 22,7 | frisch |
| 21 | 421697 | 69226,83 | 0,7505 | 0,7506 | 61445 | 24,5 | frisch_x1.5 |
| 22 | 562341 | 85919,41 |  | 0,7505 | 76789 | 26,4 | fort |

**Sierpinski-Dreieck (sg:9)**, Raster Q = 60 x (3 sqrt5)^(k/8); 8 Schritte = eine Periode. Rg = groesster Graphabstand
eines Beutelknotens vom Mittelknoten.

| k | Q | E | p (bis k+1) | p_omega | nB | Rg | E/Q^0,5772 | E/Q^0,6131 | Start |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 60,000 | 29,08538 | 0,6750 | 0,6559 | 29 | 4 | 2,7373 | 2,3631 | frisch_x0.667 |
| 1 | 76,116 | 34,15259 | 0,5603 | 0,6933 | 29 | 4 | 2,8018 | 2,3982 | fort |
| 2 | 96,561 | 39,02287 | 0,4414 | 0,4160 | 83 | 8 | 2,7906 | 2,3683 | frisch_x1.5 |
| 3 | 122,50 | 43,34367 | 0,4935 | 0,4672 | 83 | 8 | 2,7018 | 2,2735 | frisch |
| 4 | 155,40 | 48,74369 | 0,5460 | 0,5199 | 83 | 8 | 2,6486 | 2,2097 | fort |
| 5 | 197,14 | 55,50465 | 0,5965 | 0,5717 | 83 | 8 | 2,6289 | 2,1747 | fort |
| 6 | 250,10 | 63,96793 | 0,6426 | 0,6205 | 83 | 8 | 2,6410 | 2,1661 | frisch_x0.667 |
| 7 | 317,27 | 74,53557 | 0,6811 | 0,6635 | 91 | 9 | 2,6825 | 2,1814 | frisch |
| 8 | 402,49 | 87,64741 | 0,7109 | 0,6970 | 95 | 10 | 2,7496 | 2,2170 | frisch_x0.667 |
| 9 | 510,60 | 103,7999 | 0,4383 | 0,7246 | 103 | 10 | 2,8385 | 2,2692 | fort |
| 10 | 647,75 | 115,2088 | 0,4680 | 0,4407 | 245 | 16 | 2,7463 | 2,1768 | frisch_x1.5 |
| 11 | 821,74 | 128,7766 | 0,5212 | 0,4950 | 245 | 16 | 2,6758 | 2,1029 | frisch_x1.5 |
| 12 | 1042,5 | 145,7768 | 0,5701 | 0,5466 | 253 | 17 | 2,6404 | 2,0574 | fort |
| 13 | 1322,5 | 166,9533 | 0,6150 | 0,5929 | 257 | 18 | 2,6359 | 2,0364 | frisch_x1.5 |
| 14 | 1677,7 | 193,2595 | 0,6150 | 0,6366 | 265 | 18 | 2,6597 | 2,0374 | frisch |
| 15 | 2128,3 | 223,7124 | 0,6688 | 0,6439 | 301 | 20 | 2,6838 | 2,0383 | frisch |
| 16 | 2700,0 | 262,2969 | 0,6978 | 0,6932 | 301 | 20 | 2,7429 | 2,0655 | fort |
| 17 | 3425,2 | 309,6697 | 0,4691 | 0,6522 | 409 | 24 | 2,8228 | 2,1076 | frisch |
| 18 | 4345,3 | 346,2305 | 0,4676 | 0,4512 | 743 | 34 | 2,7511 | 2,0366 | frisch_x1.5 |
| 19 | 5512,4 | 386,9755 | 0,5100 | 0,4815 | 787 | 36 | 2,6803 | 1,9673 | frisch |
| 20 | 6993,1 | 436,9017 | 0,5671 | 0,5387 | 787 | 36 | 2,6378 | 1,9196 | fort |
| 21 | 8871,4 | 500,0162 | 0,5901 | 0,5953 | 787 | 36 | 2,6315 | 1,8988 | frisch |
| 22 | 11254 | 575,3801 | 0,6283 | 0,6010 | 895 | 40 | 2,6396 | 1,8884 | frisch |
| 23 | 14277 | 668,1496 | 0,6801 | 0,6549 | 895 | 40 | 2,6719 | 1,8952 | fort |
| 24 | 18112 | 785,4924 | 0,7001 | 0,7043 | 911 | 41 | 2,7381 | 1,9257 | fort |
| 25 | 22977 | 927,8478 | 0,4715 | 0,6619 | 1235 | 49 | 2,8193 | 1,9659 | frisch |
| 26 | 29149 | 1037,997 | 0,4572 | 0,4281 | 2353 | 72 | 2,7493 | 1,9008 | frisch_x1.5 |
| 27 | 36978 | 1157,262 | 0,5156 | 0,4864 | 2353 | 72 | 2,6719 | 1,8316 | fort |
| 28 | 46911 | 1308,297 | 0,5732 | 0,5447 | 2353 | 72 | 2,6330 | 1,7896 | fort |
| 29 | 59511 | 1499,453 | 0,5910 | 0,6012 | 2369 | 73 | 2,6305 | 1,7727 | fort |
| 30 | 75496 | 1725,842 | 0,6327 | 0,6061 | 2693 | 81 | 2,6391 | 1,7634 | frisch |
| 31 | 95775 | 2006,204 | 0,6761 | 0,6587 | 2717 | 82 | 2,6742 | 1,7716 | fort |
| 32 | 121500 | 2356,307 | 0,6995 | 0,7002 | 2789 | 84 | 2,7379 | 1,7984 | fort |
| 33 | 154135 | 2782,965 | 0,6845 | 0,6588 | 3761 | 100 | 2,8187 | 1,8357 | frisch |
| 34 | 195537 | 3275,181 |  | 0,7095 | 3761 | 100 | 2,8916 | 1,8672 | fort |

Gleitende Sekanten im Beutelbereich (nur berichtet):

- Zwei Perioden (k_oben: p):
  - 16: 0,5777; 17: 0,5792; 18: 0,5735; 19: 0,5751; 20: 0,5761; 21: 0,5775; 22: 0,5771; 23: 0,5762; 24: 0,5761
  - 25: 0,5754; 26: 0,5775; 27: 0,5768; 28: 0,5765; 29: 0,5767; 30: 0,5752; 31: 0,5763; 32: 0,5767; 33: 0,5768
  - 34: 0,5903 (gewertet)
- Eine Periode (k_oben: p):
  - 8: 0,5796; 9: 0,5840; 10: 0,5688; 11: 0,5721; 12: 0,5756; 13: 0,5786; 14: 0,5809; 15: 0,5775; 16: 0,5759
  - 17: 0,5743; 18: 0,5781; 19: 0,5781; 20: 0,5767; 21: 0,5763; 22: 0,5732; 23: 0,5749; 24: 0,5763; 25: 0,5765
  - 26: 0,5769; 27: 0,5755; 28: 0,5762; 29: 0,5770; 30: 0,5771; 31: 0,5777; 32: 0,5772; 33: 0,5771; 34: 0,6037
- Ohne den obersten Punkt (k = 34): zwei Perioden 0,5735 bis 0,5792 (18 Werte, Mittel 0,5765), eine Periode 0,5688 bis
  0,5840 (26 Werte, Mittel 0,5766).
- Nachtraeglich: Die Minima von E/Q^0,5772 je Periode (k = 5 und 29, drei Perioden) geben p = 0,5773, die Maxima vor
  dem Sprung (k = 9 und 33) 0,5760.

**Zufallsgraph (zr:10000:6:1)**, Raster Q = 10 x 10^(k/8). Gewaehlt: tiefster konvergierter Start ueberhaupt. nB = 0
heisst: kein Knoten mit chi < 0,5.

| k | Q | E | E/Q | p (bis k+1) | p_omega | nB | chi(Mittelknoten) | Start |
|---|---|---|---|---|---|---|---|---|
| 0 | 10,000 | 9,997499 | 0,9997 | 0,9997 | 0,9997 | 0 | 0,999 | frisch |
| 1 | 13,335 | 13,33077 | 0,9997 | 0,9996 | 0,9997 | 0 | 0,999 | flach |
| 2 | 17,783 | 17,77488 | 0,9996 | 0,9995 | 0,9996 | 0 | 0,999 | frisch |
| 3 | 23,714 | 23,69966 | 0,9994 | 0,9993 | 0,9994 | 0 | 0,999 | frisch |
| 4 | 31,623 | 31,59774 | 0,9992 | 0,9991 | 0,9992 | 0 | 0,998 | flach |
| 5 | 42,170 | 42,12510 | 0,9989 | 0,9988 | 0,9989 | 0 | 0,998 | fort |
| 6 | 56,234 | 56,15485 | 0,9986 | 0,9984 | 0,9986 | 0 | 0,997 | flach |
| 7 | 74,989 | 74,84830 | 0,9981 | 0,9978 | 0,9981 | 0 | 0,996 | frisch |
| 8 | 100,000 | 99,74874 | 0,9975 | 0,9971 | 0,9975 | 0 | 0,995 | frisch_x0.667 |
| 9 | 133,35 | 132,9046 | 0,9966 | 0,9961 | 0,9966 | 0 | 0,993 | frisch |
| 10 | 177,83 | 177,0302 | 0,9955 | 0,9947 | 0,9955 | 0 | 0,991 | fort |
| 11 | 237,14 | 235,7144 | 0,9940 | 0,9929 | 0,9939 | 0 | 0,988 | fort |
| 12 | 316,23 | 313,6869 | 0,9920 | 0,9904 | 0,9918 | 0 | 0,984 | fort |
| 13 | 421,70 | 417,1529 | 0,9892 | 0,9870 | 0,9889 | 0 | 0,978 | fort |
| 14 | 562,34 | 554,1998 | 0,9855 | 0,9822 | 0,9849 | 0 | 0,971 | frisch |
| 15 | 749,89 | 735,2646 | 0,9805 | 0,9755 | 0,9793 | 0 | 0,960 | flach |
| 16 | 1000,00 | 973,6056 | 0,9736 | 0,9658 | 0,9713 | 0 | 0,946 | fort |
| 17 | 1333,5 | 1285,618 | 0,9641 | 0,9513 | 0,9596 | 0 | 0,925 | frisch |
| 18 | 1778,3 | 1690,537 | 0,9507 | 0,9281 | 0,9416 | 0 | 0,895 | flach |
| 19 | 2371,4 | 2208,176 | 0,9312 | 0,8856 | 0,9117 | 0 | 0,849 | frisch |
| 20 | 3162,3 | 2849,231 | 0,9010 |  | 0,8506 | 0 | 0,766 | fort |
| 21 | 4217,0 | - | - | - | - | - | - | kein konvergierter Start |
| 22 | 5623,4 | - | - | - | - | - | - | kein konvergierter Start |
| 23 | 7498,9 | - | - | - | - | - | - | kein konvergierter Start |
| 24 | 10000,0 | - | - | - | - | - | - | kein konvergierter Start |

## Kontrollen

- **dE/dQ = omega** (Plan): an zehn Punkten (2D k 8, 16, 24; 3D k 8, 16; Sierpinski k 12, 24, 32; Zufall k 8, 16).
  - |rel| <= 9,2e-7 (Sierpinski k = 32), sonst <= 1,4e-7.
  - **Bestanden** (Schranke 1e-4).
- **Beutelbild 2D (K0, zweiter Teil)** bei k = 26 (Q = 1,78e5, Reff 63,8):
  - chi am Mittelknoten ~1e-105
  - Wand (chi 0,1 bis 0,9 entlang +x) zwischen x = 62,1 und 65,9, also **3,78 Gitterschritte**
  - f faellt von 13,5 (x = 40) auf 0,5 an der Wandmitte und ist ab x = 70 unter 0,005
  - **Bestanden** (Schranken chi(0) < 0,05 und Wand <= 6). Bei k = 14 (Reff 19,6) ist die Wand ebenso schmal (~3,9).
- **Bauproben:**
  - Sierpinski Stufe 8: N = 9843 = (3^9 + 3)/2, 19683 = 3^9 Kanten, drei Ecken mit Grad 2, sonst Grad 4. Stufe 9:
    N = 29526, 59049 Kanten.
  - Gitter: Produktformel gegen eigvalsh von g2:12 und g3:8 aus demselben Code: 8,0e-15 und 4,1e-14.
  - Zufallsgraph: Grad 6 ueberall, 30000 Kanten, zusammenhaengend; Exzentrizitaet des Mittelknotens 7.
- **Konvergenz:**
  - 2D 64 von 64 Starts konvergiert, 3D 29 von 29, Sierpinski 136 von 136, Zufall 66 von 75.
  - Die neun nicht konvergierten sind alle Starts bei k = 21 bis 24 auf dem Zufallsgraphen. Dort ist der ganze Graph im
    Beutelzustand; E sinkt gegen N/4 ohne echtes Minimum, max|grad| ~1e-3.
- **Nebentaeler:**
  - 2D und 3D: Alle Beutelstarts (fort, frisch, 1,5 R0, R0/1,5) enden in derselben Energie (Abstand <= 5e-14
    relativ).
  - Sierpinski: Die Starts enden in verschiedenen oertlichen Minima, bis 38 % hoeher (k = 31).
    - Gewaehlt war 26-mal fort oder frisch und 9-mal ein Start mit 1,5 R0 oder R0/1,5 (k = 0, 2, 6, 8, 10, 11, 13, 18,
      26).
    - Ob der gewaehlte Beutel das tiefste zentrale Minimum ist, bleibt offen (vier Starts je k).
- **Tiefere Zustaende abseits der Mitte** (flache Starts, nur berichtet):
  - 2D k = 4 und 12: ein Beutel in einer Gitterecke (nB 121 bzw. 526), 20 % bzw. 37 % tiefer als der zentrale.
  - Sierpinski k = 8 und 16: ein Beutel abseits der Mitte, 13 % bzw. 16 % tiefer. Der naechste Beutelknoten liegt 159
    bzw. 235 Schritte vom Mittelknoten; die Ecken A und B liegen 256 entfernt.
  - [H] Der offene Rand wirkt wie ein Spiegel: gleiches lambda_1 bei kleinerem Volumen. Der zentrale Beutel ist auf
    diesen endlichen Graphen ein oertliches Minimum, kein globales.
- **Oberster Sierpinski-Punkt (k = 34):**
  - Der tiefste zentrale Beutel (Start 1,5 R0: E = 3240,35, nB = 8023) liegt ueber N/4 = 7381. Nach Plan zaehlt er
    nicht als kompakt.
  - Gewaehlt wurde darum der Fortsetzungsast (E = 3275,18, nB = 3761). Er ist noch nicht auf die naechste Stufe
    gesprungen.
  - E/Q^0,5772 = 2,892, gegen 2,746 / 2,751 / 2,749 an den gleichen Phasenpunkten k = 10, 18, 26. Der Punkt liegt also
    um etwa 5 % zu hoch. Allein er hebt die gewertete Zwei-Perioden-Sekante von ~0,577 auf 0,590.
- **Groesse gegen Graph:** In allen gewaehlten Beuteln gilt Rs + 10 <= d_rand und nB <= N/4. Die groessten: 2D
  nB = 12801 von N/4 = 14520; 3D 76789 von 132860; Sierpinski 3761 von 7381.

## Latten (v3)

- **L1 (kann scheitern): ja.**
  - Fuenf Vorhersagen mit Zahlengrenzen vor jeder Rechnung.
  - BD0 ist gescheitert. BD3 trennte zwei Kandidaten, die nur 0,036 auseinanderliegen.
- **L2 (Gegenprobe): ja.**
  - Der Zufallsgraph ist die Gegenprobe ohne Dimension: kein Beutel, p nahe 1.
  - Die Hausdorff-Variante (0,613) scheidet nicht nur ueber die Sekante aus. E/Q^0,6131 faellt ueber vier Perioden
    stetig (2,36 auf 1,87), E/Q^0,5772 nicht.
  - Gegenproben der Numerik: zweite und dritte Starts je Q, flache Starts, dE/dQ = omega, Bauproben, K0.
- **L3 (Numerik): ja, teilweise.**
  - dE/dQ = omega auf 9,2e-7. Auf den Gittern enden alle Beutelstarts in derselben Energie.
  - Offen:
    - Sierpinski: viele Nebentaeler, nur vier Starts je Q; der oberste Punkt liegt auf einem Nebenast
      (Stufe 9 ist dort zu klein, siehe Kontrollen)
    - 3D nur bis Reff 26
    - Konvergenz der Graphgroesse nicht eigens geprueft (nur Randabstand >= 10 und nB <= N/4)
- **L4 (schon bekannt): teilweise.**
  - [S] Heeck und Sokhashvili, "Revisiting the Friedberg-Lee-Sirlin soliton model", arXiv:2303.09566, an der Quelle
    gelesen (S. 1 bis 9):
    - Gl. (45): E = 2^(7/4) pi eta^(1/4) m_phi/(3 sqrt d) Q^(3/4) (1 + O(Q^(-1/4))) im Duennwand-Grenzfall, 3D.
    - S. 8: "From the above E proportional to Q^(3/4) expression - which matches the expectation for Q-balls in flat
      potentials".
    - Eigene Umrechnung unseres Modells: chi_HS = sqrt2 chi, d^2 = 1/2, g^2 = 1/2, chi_vac^2 = 2, also m_phi = m_chi = 1,
      eta = 1. Damit ist der Vorfaktor 4 pi/3, unser idealer 3D-Beutel.
    - Ihr Korrekturterm (-0,75 Q^(-1/4) relativ, hergeleitet fuer grosses eta) ist hier etwa 24-mal zu gross: -2,7e-2
      gegen gemessen -1,1e-3 bei Q = 5,6e5.
  - [S, nur Abstract gelesen] Qiu, arXiv:1206.1381 (2012): Eigenwert-Zaehlfunktion auf einem Gebiet im
    Sierpinski-Dreieck "rho(x) = g(log x) x^(log 3/log 5) + O(...)". Das ist d_s/2 = log3/log5 mit periodischem g,
    also die log-Periodik, die wir in E(Q) sehen.
  - [L?] nicht an der Quelle gelesen:
    - Friedberg, Lee und Sirlin, Phys. Rev. D 13, 2739 (1976)
    - Rammal und Toulouse (1983), d_s = 2 log3/log5
    - Kigami und Lapidus, Commun. Math. Phys. 158, 93 (1993), Weyl-Gesetz auf p.c.f.-Fraktalen
  - Beutel- oder Q-Ball-Solitonen auf Fraktalen mit E ~ Q^(d_s/(d_s+1)): nicht gefunden. Gesucht nur ueber die
    arXiv-Schnittstelle (vier Abfragen); das Websuch-Kontingent war erschoepft.
- **L5 (Messbezug): nein.**
  - [H] Bezug hoechstens zu Simulationen entstehender Geometrie (URSUPPE, CDT). Dort misst man d_s ueber Diffusion; ein
    Beutel-Teilchen waere eine "physikalische" Sonde fuer d_s im Inneren.

## Selbstanzeigen

- **Rauchlaeufe vor dem Einfrieren** (Graphen und Raster in keinem echten Lauf; im Plan offengelegt):
  - R3 lief die ganze Kette mit sg:7, g2:81, g3:41 und zr:2000.
  - Dabei gesehen: Zwei-Perioden-Sekante 0,577 (sg:7), 0,674 (2D), 0,762 (3D) und 0,914 (Zufall).
  - Die Vorhersagen der Karte standen vorher fest und sind unveraendert.
  - Die Auswerteregeln standen als Code fest, bevor R3 lief. R1 und R2 waren da schon gesehen (oertliche p_omega in
    2D, 3D und auf dem Fraktal).
- **Code nach R1 geaendert** (vor dem Einfrieren):
  - Die Fortsetzung lief in R1 nie (Variable nie gesetzt).
  - Wahlregel "zentral" neu, weil flache Starts in Randbeutel fielen.
  - Randabstand auf Gittern euklidisch statt Manhattan.
  - Neue Optionen --ohne-frisch, --flach-k, --pruef-k alle.
- **Groessen nach R2 geaendert:** 2D von 181^2 auf 241^2 (Regel nB <= N/4); flache Starts nur bei kleinem Q.
- **Schwaeche der eingefrorenen Regeln auf dem Fraktal (erst nach den Laeufen bemerkt):**
  - Die Grenze nB <= N/4 sollte nur "fuellende" Zustaende ausschliessen. Auf Stufe 9 schliesst sie bei k = 34 den
    tiefsten zentralen Beutel aus. Die Wahlregel nimmt dann einen Nebenast.
  - Die gewertete BD3-Zahl (0,5903) haengt an diesem einen Punkt. Das Urteil haengt nicht daran: Alle anderen
    Zwei-Perioden-Sekanten (0,5735 bis 0,5792) erfuellen BD3 ebenfalls.
  - Besser waere gewesen: Stufe 10 fuer das obere Ende oder Q-Raster nur bis k = 33. Nicht nachgerechnet; Plan und
    Code bleiben unveraendert.
- **Ergebnis-Entwurf waehrend der Laeufe:** Gliederung und Gitter-Teile entstanden ab 01:10 CEST, als die letzten
  Sierpinski-Laeufe noch rechneten. Deren Zwischenstaende (Logzeilen) waren dabei sichtbar. Gewertet ist nur die
  Auswertung von 23:14:34 UTC.
- **Erster Start von R1:** Vier von fuenf Zeilen liefen nicht (Shell-Variablen im Hintergrund-Teilausdruck; "Permission
  denied" beim Log). Neu gestartet ueber ein Startskript; die Spektrums-Kette des ersten Versuchs lief und ist Teil
  von R1.
- **Startskript mit Hintergrund-Ketten** (code/start_haupt.sh): einmal per nohup gestartet, je Spur nacheinander; kein
  Dienst, kein Timer, kein Hook. Die ssh-Sitzung des Starts blieb haengen (Hintergrundprozess hielt sie). Sie lief
  lokal im Hintergrund weiter; die Laeufe waren davon unberuehrt.
- **Geteilte Spuren:** Waehrend der Laeufe nutzte ein anderer Auftrag (r24wb) dieselben Spuren. SGd und D3p2 warteten
  deshalb etwa 1,7 bis 2,8 min auf die Sperre (Unit-Name gegen Prozessalter).
- **Literatur** ab kurz nach 22:59:07 UTC (letzte Zustandsabfrage davor): nach dem Einfrieren und nach dem Start aller
  Laeufe, aber waehrend die meisten Beutel-Laeufe noch rechneten. Plan und Code waren da fest.
  - Heeck und Sokhashvili als PDF gelesen; Qiu und Malomed (2412.01097, Eckensolitonen auf SG-Wellenleitern, nicht
    verwendet) nur im Abstract.
  - Nur ueber arxiv.org und export.arxiv.org (eine Abfrage scheiterte an 429/503).
- **K0 3D:** Die Randformel ist eine Rechnung von Hand nach dem Ergebnis, keine Rechnung auf der .69 und kein Teil des
  Plans.
- **Sierpinski-K0 auf Stufe 8, Beutel auf Stufe 9** (Stufe 9 passt nicht dicht in 4 GB); im Plan festgelegt.
- **Lokal kein Interpreter.** Lokal benutzt: jq, sha256sum, rsync, ssh, scp, cp, chmod, mkdir, grep, sed, awk, date
  und das Lese-Werkzeug fuer das PDF. bash -n nur auf der .69.
- **Speicher:** Nicht systematisch gemessen. RSS-Stichproben per ps: 0,72 GB (g3:81), 1,1 GB (eigvalsh N = 1e4).
  MemoryMax 4G wurde nie ueberschritten (alle rc = 0).
- **Sonst:**
  - nur Spuren cpu, cpu2, cpu3, cpu4 und cpu6; nicht cpu5, keine GPU; jeder Lauf unter 10 min
  - kein git, kein Peerbus, kein Journal, keine Unteragenten, keine Aenderung an Karten oder anderen Runden
  - Auf der .69 wurde nichts in place ueberschrieben (neue Namen; bagdim.py und auswertung.py als Kopien der
    getesteten .rauch3-Fassungen)

## Ablage

- lokal: code/ (bagdim.py, auswertung.py, start_haupt.sh, bagdim.py.rauch1 = Fassung von R1)
- PLAN.md und PLAN.md.eingefroren-20261003-005657 (sha256 805b476745e6b18c31269d1dff18d8c8d58e41c8f0c90c2b37007049dcabf23b)
- lauf-69/:
  - rauch/, rauch2/, rauch3/ (Rauchlaeufe; rauch3/auswertung_rauch3.json = Probelauf der Auswertung)
  - haupt/ (alle echten Laeufe: s_*.json Spektren, b_*.json Beutel, je .log)
  - auswertung/ (auswertung.json, auswertung.log; gewertet)
- .69: /home/fmh/fmhc-physics-remote/runde24-bag-dim/ (code/, lauf/; identisch)

## Einfach gesagt

Wir haben ein Teilchen gebaut, das wie eine Seifenblase funktioniert: Innen sitzt eine Ladung, und jedes Stueck Platz in
der Blase kostet etwas Energie. Wie schwer die Blase mit wachsender Ladung wird, haengt davon ab, wie viel Platz der Raum
um sie herum bietet, also von seiner Dimension. Auf flachen Gittern in 2D und 3D folgt die Blase sehr genau der Regel,
die man fuer 2 und 3 Dimensionen erwartet. Auf dem Sierpinski-Dreieck, einem Fraktal voller Loecher, zeigt sie die
Dimension, die angibt, wie schnell sich Waerme ausbreitet (1,37), und nicht die, die angibt, wie viele Punkte
hineinpassen (1,58). Auf einem Zufallsnetz ohne Dimension bildet sich gar keine Blase; die Ladung verteilt sich ueber
das ganze Netz.

---
Letzte Aenderung dieser Datei: 2026-10-03 01:20:08 CEST (date). Zeitbox 120 min ab 00:32:46 CEST eingehalten.
