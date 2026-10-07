# ERGEBNIS LOG-NACHBAU (Runde 16)

- Code-Agent, frischer Kontext, eigener Code (stille.py; Folgelaeufe stille_n1.py und stille_n2.py).
- Start 2026-10-02 07:46:33 CEST, Bericht ab 08:20:45 CEST, um F3 ergaenzt bis 08:28:02 CEST (date). Uhrzeiten der .69 in UTC (CEST = UTC + 2).
- Status: explorativ (v3).
  - Die Rechnungen sind Messungen am eigenen Modellcode, keine Messdaten.
  - Alle Deutungen sind Hypothesen.

## 1 Ergebnis zuerst

1. **K1 und K2 bestanden.**
   - K1, Kontrollmodell:
     - Die stille Stelle liegt bei w^2 = 0,7976768, rho = 1,7446175 (Stufe 1) und 0,7976768 / 1,7446175 (Stufe 2).
     - Abstand zur bewiesenen Stelle (0,797677; 1,744618): 2e-7 in w^2, 5e-7 in rho.
     - Umlauf -1 auf beiden Stufen, groesster Sprung 0,361 rad, aufgeloest.
   - K2: Q und E stimmen zwischen den Stufen auf 6e-11 relativ ueberein.
2. **Blinde Suche im Log-Modell: genau ein Kandidat (eine Nullstelle von W).**
   - 57 Zeilen von 0,700 bis 0,980, beide Stufen.
   - Genau ein Vorzeichenwechsel von s: zwischen w^2 = 0,925 und 0,930 auf dem oberen Ast der geschlossenen Bedingung.
   - Der Zellen-Umlauf als zweiter Detektor findet dieselbe und keine weitere Zelle.
3. **Lage der Stelle:**
   - Stufe 1: w^2 = 0,9256098, rho = 1,8379959.
   - Stufe 2: w^2 = 0,9256099, rho = 1,8379961.
   - Die Stufen stimmen auf 8e-8 (w^2) und 1,2e-7 (rho) ueberein.
4. **Umlauf nach dem eingefrorenen Plan (6 Halbierungsrunden): -1 auf beiden Stufen, aber nicht aufgeloest.**
   - Der groesste Sprung bleibt 2,46 rad bei 76 Randpunkten.
   - Nach der eingefrorenen Regel gilt die Stelle damit **nicht als gefunden**.
   - Ursache: Auf diesem Ast ist die Abstrahlamplitude s sehr klein (1e-6 bis 1e-4), W ist stark anisotrop.
5. **Nachtraeglich (PLAN-NACHTRAG-1, eingefroren vor dem Lauf; ob er gilt, entscheidet die Leitung):**
   - F1 mit bis zu 24 statt 6 Halbierungsrunden, sonst unveraendert: Umlauf -1 auf beiden Stufen, groesster Sprung
     0,357 rad, 94 Punkte, aufgeloest.
   - F2 mit kleinerem Rechteck (Halbbreite 1e-4): ebenfalls -1, groesster Sprung 0,363 rad, aufgeloest.
   - K1 ist mit derselben Einstellung unveraendert.
   - F3 (PLAN-NACHTRAG-2): Die Randstreifen, die der Hauptlauf ausliess, wurden bis 1e-5 an die Fenstergrenzen abgetastet.
     Keine weitere Stelle.

## 2 Herleitung kurz (voll: HERLEITUNG.md)

- Profil:
  - f'' + (2/r) f' = (U'(f^2) - w^2) f.
  - Zweiseitiges Schiessen: aussen von r = 0, innen vom Yukawa-Schwanz A e^{-mu r}/r. Newton in (f0, A).
- Kanaele mit u = r a, v = r b:
  - u'' = [V - (w+rho)^2] u + g v, v'' = [V - (w-rho)^2] v + g u.
  - V = U' + f^2 U'', g = f^2 U''.
  - Im Fenster 1 - w < rho < 1 + w ist a offen (k^2 = (w+rho)^2 - 1) und b geschlossen
    (kappa^2 = 1 - (w-rho)^2).
- Regulaere Loesungen: Y_a mit (a(0), b(0)) = (1, 0), Y_b mit (0, 1). Sie spannen einen Lagrange-Raum der Wronski-Form auf.
- Z_d: die einzige Loesung ohne offene Welle mit abfallendem b-Kanal.
  - Stille Stelle <=> Z_d ist regulaer <=> G_a = G_b = 0 mit G_x = W[Y_x, Z_d] = -2 kappa (wachsender b-Anteil von Y_x).
  - Jede gemeinsame Nullstelle ist eine echte stille Stelle (Lagrange-Argument).
- Definitionen:
  - W = G_a + i G_b.
  - Geschlossene Bedingung G_b = 0: Quantisierung des geschlossenen Kanals.
  - s = G_a an deren Nullstellen. In erster Ordnung ist s = -Int g u_a v_d dr, das Ueberlappintegral der Goldenen Regel,
    also die Abstrahlamplitude des Zustands des geschlossenen Kanals in die offene Welle.
- Hypothese aus der Herleitung (nicht gerechnet): Die Jost-Determinante mit auslaufender Welle hat an einer stillen
  Stelle den Umlauf 0, weil die Breite Gamma >= 0 quadratisch verschwindet. Deshalb ist W hier ueber die
  Wronski-Paarungen gebildet.

## 3 Kontrollen

### K1 (Kontrollmodell, U = S - S^2 + S^3/2)

- 8 Zeilen w^2 = 0,780 bis 0,815, je eine Nullstelle von G_b im ganzen Fenster.
- s wechselt zwischen 0,795 (+5,8e-4) und 0,800 (-5,0e-4).
- Start aus beiden Detektoren bei (0,797703; 1,744621). Newton in 3 Schritten (letzter Schritt 4e-14), |W| am Punkt < 2e-15.

| Stufe | w^2 | rho | Abstand w^2 / rho zur bewiesenen Stelle | Umlauf | groesster Sprung | Randpunkte |
|---|---|---|---|---|---|---|
| 1 (h = 0,02) | 0,797676775 | 1,744617541 | 2,3e-7 / 4,6e-7 | -1 | 0,361 rad | 74 |
| 2 (h = 0,01) | 0,797676786 | 1,744617545 | 2,1e-7 / 4,6e-7 | -1 | 0,361 rad | 74 |

- Urteil nach der Regel der Karte: **K1 bestanden** (auf 1e-4, Umlauf +-1 auf zwei Stufen, aufgeloest).

### K2 (Log-Profile auf zwei Gittern)

- Gitter hp = 0,01 und 0,005, w^2 = 0,70; 0,74; ...; 0,98 (8 Werte).
- Groesste relative Abweichung: Q 6,0e-11, E 5,4e-11. Ueber alle 57 Zeilen der blinden Suche ebenso 6,0e-11 und 5,4e-11.
- Profile knotenfrei. f0 faellt von 2,465 (0,70) auf 0,585 (0,98).
- Halbwertsradius 2,69 bis 4,70. Am Aussenrand R = 130,8 ist f/f0 hoechstens 4e-10 (bei 0,98).
- Anschlusssprung des zweiseitigen Schiessens hoechstens 1,1e-15 relativ.
- Nebenbefund: Q hat zwischen 0,90 und 0,98 ein Minimum (Q = 330,9; 307,9; 354,3 bei 0,90; 0,94; 0,98).
- Urteil: **K2 bestanden** (1e-6 relativ).

## 4 Zeilen der blinden Suche (Log)

- Spalten:
  - w^2
  - Zahl der Nullstellen von G_b (Stufe 2 / Stufe 1)
  - rho der Nullstellen (Stufe 2)
  - Vorzeichen von s auf Stufe 2 und auf Stufe 1
  - s (Stufe 2)
  - groesste Abweichung der Nullstellen zwischen den Stufen
- Ast unten (ab 0,885): Nullstelle knapp ueber der unteren Abtastgrenze 1 - w + 0,002, s = +0,067 bis +0,103.
- Ast oben (alle Zeilen): s klein, Vorzeichenwechsel zwischen 0,925 und 0,930.

| w^2 | Nullst. St2/St1 | rho (St2) | s St2 | s St1 | s (St2) | max d rho |
|---|---|---|---|---|---|---|
| 0,7 | 1/1 | 1,55654 | + | + | 0,001048146 | 1,3402945420182277e-10 |
| 0,705 | 1/1 | 1,56244 | + | + | 0,001023291 | 1,349869105382595e-10 |
| 0,71 | 1/1 | 1,56833 | + | + | 0,000997946 | 1,3588685732202066e-10 |
| 0,715 | 1/1 | 1,57421 | + | + | 0,000972137 | 1,3672418752719295e-10 |
| 0,72 | 1/1 | 1,58009 | + | + | 0,000945892 | 1,374989011537764e-10 |
| 0,725 | 1/1 | 1,58598 | + | + | 0,00091924 | 1,3820722344348724e-10 |
| 0,73 | 1/1 | 1,59186 | + | + | 0,000892211 | 1,3884604577185655e-10 |
| 0,735 | 1/1 | 1,59774 | + | + | 0,000864836 | 1,3941381382664986e-10 |
| 0,74 | 1/1 | 1,60362 | + | + | 0,000837148 | 1,3990608671576865e-10 |
| 0,745 | 1/1 | 1,60951 | + | + | 0,00080918 | 1,4032042194855876e-10 |
| 0,75 | 1/1 | 1,61539 | + | + | 0,000780967 | 1,406534888559463e-10 |
| 0,755 | 1/1 | 1,62129 | + | + | 0,000752544 | 1,4090328903648697e-10 |
| 0,76 | 1/1 | 1,62718 | + | + | 0,00072395 | 1,4106560364268717e-10 |
| 0,765 | 1/1 | 1,63308 | + | + | 0,000695222 | 1,4113710200547303e-10 |
| 0,77 | 1/1 | 1,63899 | + | + | 0,0006664 | 1,4111445345577067e-10 |
| 0,775 | 1/1 | 1,64491 | + | + | 0,000637526 | 1,4099565959213578e-10 |
| 0,78 | 1/1 | 1,65084 | + | + | 0,000608641 | 1,4077472521023537e-10 |
| 0,785 | 1/1 | 1,65678 | + | + | 0,00057979 | 1,4044920781941528e-10 |
| 0,79 | 1/1 | 1,66273 | + | + | 0,000551017 | 1,4001666492902132e-10 |
| 0,795 | 1/1 | 1,66869 | + | + | 0,00052237 | 1,39472655646955e-10 |
| 0,8 | 1/1 | 1,67467 | + | + | 0,000493896 | 1,3881118476888332e-10 |
| 0,805 | 1/1 | 1,68067 | + | + | 0,000465645 | 1,3803158616099154e-10 |
| 0,81 | 1/1 | 1,68668 | + | + | 0,000437667 | 1,371265323513171e-10 |
| 0,815 | 1/1 | 1,69271 | + | + | 0,000410015 | 1,3609513516144034e-10 |
| 0,82 | 1/1 | 1,69877 | + | + | 0,000382742 | 1,349309552978184e-10 |
| 0,825 | 1/1 | 1,70485 | + | + | 0,000355904 | 1,3363110618058727e-10 |
| 0,83 | 1/1 | 1,71096 | + | + | 0,000329555 | 1,321898146500189e-10 |
| 0,835 | 1/1 | 1,7171 | + | + | 0,000303755 | 1,3060419412624924e-10 |
| 0,84 | 1/1 | 1,72326 | + | + | 0,000278561 | 1,2886824940494535e-10 |
| 0,845 | 1/1 | 1,72947 | + | + | 0,000254033 | 1,2697820572782348e-10 |
| 0,85 | 1/1 | 1,73571 | + | + | 0,000230232 | 1,24930066291995e-10 |
| 0,855 | 1/1 | 1,74199 | + | + | 0,00020722 | 1,2271761384852198e-10 |
| 0,86 | 1/1 | 1,74831 | + | + | 0,000185058 | 1,2033662954991087e-10 |
| 0,865 | 1/1 | 1,75468 | + | + | 0,000163808 | 1,1778289454866808e-10 |
| 0,87 | 1/1 | 1,76111 | + | + | 0,000143534 | 1,1505152386348527e-10 |
| 0,875 | 1/1 | 1,76759 | + | + | 0,000124295 | 1,1213763251305409e-10 |
| 0,88 | 1/1 | 1,77414 | + | + | 0,000106155 | 1,0903633551606617e-10 |
| 0,885 | 2/2 | 0,06264; 1,78075 | ++ | ++ | 0,067226536; 8,917e-05 | 1,0574341402502796e-10 |
| 0,89 | 2/2 | 0,06144; 1,78744 | ++ | ++ | 0,068662788; 7,3398e-05 | 1,0225575941547049e-10 |
| 0,895 | 2/2 | 0,06017; 1,79421 | ++ | ++ | 0,070134995; 5,8893e-05 | 9,856870875069035e-11 |
| 0,9 | 2/2 | 0,05884; 1,80107 | ++ | ++ | 0,071644896; 4,5702e-05 | 9,46775990939841e-11 |
| 0,905 | 2/2 | 0,05742; 1,80803 | ++ | ++ | 0,073194373; 3,387e-05 | 9,057998795469757e-11 |
| 0,91 | 2/2 | 0,05593; 1,81509 | ++ | ++ | 0,074785471; 2,343e-05 | 8,627543124362091e-11 |
| 0,915 | 2/2 | 0,05435; 1,82228 | ++ | ++ | 0,076420414; 1,4408e-05 | 8,176059829168025e-11 |
| 0,92 | 2/2 | 0,05267; 1,8296 | ++ | ++ | 0,078101628; 6,817e-06 | 7,703748750031991e-11 |
| 0,925 | 2/2 | 0,05089; 1,83707 | ++ | ++ | 0,079831761; 6,55e-07 | 7,210609886953989e-11 |
| 0,93 | 2/2 | 0,04899; 1,84471 | +- | +- | 0,081613712; -4,1e-06 | 6,697220555906824e-11 |
| 0,935 | 2/2 | 0,04698; 1,85254 | +- | +- | 0,083450656; -7,492e-06 | 6,164246890705272e-11 |
| 0,94 | 2/2 | 0,04483; 1,86058 | +- | +- | 0,085346074; -9,593e-06 | 5,6128435232949414e-11 |
| 0,945 | 2/2 | 0,04254; 1,86886 | +- | +- | 0,087303784; -1,0508e-05 | 5,0449866506596663e-11 |
| 0,95 | 2/2 | 0,04009; 1,87743 | +- | +- | 0,089327967; -1,0383e-05 | 4,462807901006727e-11 |
| 0,955 | 2/2 | 0,03746; 1,88631 | +- | +- | 0,091423184; -9,402e-06 | 3,870104237080341e-11 |
| 0,96 | 2/2 | 0,03463; 1,89557 | +- | +- | 0,093594371; -7,798e-06 | 3,2718272535703363e-11 |
| 0,965 | 2/2 | 0,03157; 1,90529 | +- | +- | 0,095846788; -5,847e-06 | 2,6750157644528372e-11 |
| 0,97 | 2/2 | 0,02826; 1,91554 | +- | +- | 0,09818588; -3,85e-06 | 2,089550754647007e-11 |
| 0,975 | 2/2 | 0,02465; 1,92644 | +- | +- | 0,10061694; -2,111e-06 | 1,529509852105093e-11 |
| 0,98 | 2/2 | 0,02071; 1,93816 | +- | +- | 0,103144395; -8,68e-07 | 1,014166528534588e-11 |

- K1-Zeilen (Kontrollmodell), gleiche Spalten:

| w^2 | Nullst. St2/St1 | rho (St2) | s St2 | s St1 | s (St2) | max d rho |
|---|---|---|---|---|---|---|
| 0,78 | 1/1 | 1,73851 | + | + | 0,003975347 | 4,2369663333374774e-11 |
| 0,785 | 1/1 | 1,74031 | + | + | 0,002835566 | 5,4406923410965646e-11 |
| 0,79 | 1/1 | 1,74205 | + | + | 0,001698572 | 6,496914117803954e-11 |
| 0,795 | 1/1 | 1,74373 | + | + | 0,00058281 | 7,381539823825278e-11 |
| 0,8 | 1/1 | 1,74538 | - | - | -0,000495272 | 8,074585444717286e-11 |
| 0,805 | 1/1 | 1,74698 | - | - | -0,001521284 | 8,560685493819165e-11 |
| 0,81 | 1/1 | 1,74857 | - | - | -0,00248291 | 8,828671127503185e-11 |
| 0,815 | 1/1 | 1,75013 | - | - | -0,003369893 | 8,872880208343759e-11 |

### Kandidat und Umlauf (Log)

| Lauf | Stufe | w^2 | rho | Umlauf (roh) | groesster Sprung | Punkte / Runden | aufgeloest |
|---|---|---|---|---|---|---|---|
| Hauptlauf (6 Runden) | 1 | 0,925609811 | 1,837995942 | -1 (-1,0000) | 2,459 rad | 76 / 6 | nein |
| Hauptlauf (6 Runden) | 2 | 0,925609892 | 1,837996066 | -1 (-1,0000) | 2,459 rad | 76 / 6 | nein |
| F1 nachtraeglich (24 Runden) | 1 | wie oben | wie oben | -1 (-1,0000) | 0,357 rad | 94 / 10 | ja |
| F1 nachtraeglich (24 Runden) | 2 | wie oben | wie oben | -1 (-1,0000) | 0,357 rad | 94 / 10 | ja |
| F2 nachtraeglich (Halbbreite 1e-4) | 1 | wie oben | wie oben | -1 (-1,0000) | 0,363 rad | 96 / 10 | ja |
| F2 nachtraeglich (Halbbreite 1e-4) | 2 | wie oben | wie oben | -1 (-1,0000) | 0,363 rad | 96 / 10 | ja |

- Start: Detektor 1 und 2 bei (0,925688; 1,838125).
- Newton in 3 Schritten (1,3e-4; 2,3e-7; 4,2e-11). |W| am Punkt: 3e-16 bei Randwerten bis 3,3e-3.
- Am Rand des 1e-3-Rechtecks faellt |W| bis 1,8e-6 (Hauptlauf) bzw. 6,9e-7 (F1). Das zeigt die Anisotropie.
- Umlaufrichtung: gegen den Uhrzeigersinn in der Ebene (x = w^2, y = rho), W = G_a + i G_b. Kontrollstelle und Log-Stelle
  haben dasselbe Vorzeichen (-1).
- Urteil nach der eingefrorenen Regel:
  - Kandidat lokalisiert, Lagen der Stufen auf 1e-4 gleich, Umlauf -1 auf beiden Stufen.
  - **Nicht aufgeloest, also nach dem eingefrorenen Plan nicht gefunden.**
- Nach Nachtrag 1 (nachtraeglich): aufgeloest auf beiden Stufen, damit "gefunden" im Sinn der Kartenregel. Ob F1 gilt,
  entscheidet die Leitung.

### F3: Randstreifen (nachtraeglich, PLAN-NACHTRAG-2, eingefroren 08:24:20 CEST vor dem Lauf)

- Abgetastet: 57 Zeilen, beide Stufen, je 101 Punkte in rho.
  - unten: 1 - w + 1e-5 bis 1 - w + 0,0025
  - oben: 1 + w - 0,0025 bis 1 + w - 1e-5
- Nullstellen von G_b im unteren Streifen nur bei w^2 = 0,875 (rho = 0,0648440, s = +0,0645) und 0,880 (rho = 0,0637697,
  s = +0,0658). Beide Stufen gleich auf 1e-10.
- Das ist der Anfang des unteren Astes. Er tritt zwischen 0,870 und 0,875 an der unteren Fenstergrenze ein und ist ab 0,885
  in der Hauptabtastung, s ebenfalls positiv.
- Oberer Streifen: keine Nullstelle in keiner Zeile.
- Beide Detektoren finden in den Streifen keinen Kandidaten. Isotropiefehler hoechstens 1,3e-8.
- Damit gibt es im ganzen Fenster (bis 1e-5 an die Grenzen) auf beiden Aesten genau einen Vorzeichenwechsel von s, den
  bei w^2 = 0,92561.

## 5 Laufzeiten und Hashes

### Laeufe (.69, kleintest.sh; Zeiten UTC aus den Logs, Dauer = Service runtime)

| Lauf | Spur | Start (UTC) | Dauer |
|---|---|---|---|
| L0 Rauchtest lokal (System-python3, hp = 0,04) | Laptop | 08:07:08 CEST | 1 s |
| K1-Zeilen Stufe 1 | cpu3 | 06:08:22 | 9,1 s |
| K1-Zeilen Stufe 2 | cpu4 | 06:08:22 | 18,4 s |
| K1-Kandidaten Stufe 1 | cpu3 | 06:08:31 | 28,6 s |
| K1-Kandidaten Stufe 2 | cpu4 | 06:08:40 | 48,3 s |
| K2 | cpu3 | 06:09:37 | 47,9 s |
| Blind Zeilen 0,700-0,845 Stufe 1 | cpu3 | 06:10:25 | 26,5 s |
| Blind Zeilen 0,850-0,980 Stufe 1 | cpu3 | 06:10:52 | 53,8 s |
| Blind Kandidaten Stufe 1 | cpu3 | 06:11:46 | 54,6 s |
| Blind Zeilen 0,700-0,845 Stufe 2 | cpu4 | 06:09:37 | 50,9 s |
| Blind Zeilen 0,850-0,980 Stufe 2 | cpu4 | 06:10:28 | 107,0 s |
| Blind Kandidaten Stufe 2 | cpu4 | 06:12:16 | 93,1 s |
| F1 Log Stufe 1 / K1 Stufe 1 / F2 Log Stufe 1 (nachtraeglich) | cpu3 | 06:15:37 | 57,3 / 12,8 / 56,2 s |
| F1 Log Stufe 2 / K1 Stufe 2 / F2 Log Stufe 2 (nachtraeglich) | cpu4 | 06:15:37 | 99,2 / 21,4 / 100,5 s |
| F3 Streifen Stufe 1: unten A/B/Kand, oben A/B/Kand (nachtraeglich) | cpu3 | 06:24:20 | 13,9 / 28,0 / 0,2 / 13,9 / 26,2 / 0,2 s |
| F3 Streifen Stufe 2: unten A/B/Kand, oben A/B/Kand (nachtraeglich) | cpu4 | 06:24:20 | 23,3 / 51,6 / 0,2 / 23,3 / 47,8 / 0,2 s |

- Alle Aufrufe mit rc 0, keiner ueber 2 min.

### sha256

- Code und Starter:
  - stille.py `79450100a433b6d2e1f2997595aa4f2390ec78944fa799968728d4adfd8c1842` (Hauptlaeufe; auf der .69 gleich)
  - stille_n1.py `0de6f0d26044f977adbbf82d422d810d16890439ef89f8e8cea92f4a2327c873` (nur F1/F2; auf der .69 gleich)
  - kette-k1.sh `4e5e87092687675e9aeb233a115bc987aa725195d4f345a960aed8e16913a5f2`
  - kette-blind.sh `9097d5dd05283965a3ea73b23a7155c4687e8b6cdcd5afcf92f8dab91511d6ac`
  - kette-n1.sh `48222d89825a109bd8cb70645f16872f7baf159430f4c837178ebd9526d83a62`
  - stille_n2.py `d0a554a4c78f11ecd1d76b6643dfdeb8d3630e390e070bc70e85473d9f910b73` (nur F3; auf der .69 gleich)
  - kette-n2.sh `8b9feb807828aefd2c67fed74bfc10b19a3bcb03c68750ad99fc43a916756903`
- Herleitung und Plaene:
  - HERLEITUNG.md `7c9252978ecdffaa6f222d743557d46a7f623ec86b412fa23455f844e481991f`
  - PLAN.md.eingefroren-20261002-080809 `0eafe1688f0dcb3e7b65d02fb8e32930f316dc2e6435248cd88cc322347f34aa` (gleich PLAN.md)
  - PLAN-NACHTRAG-1.md.eingefroren-20261002-081537 `fdaf7dd1ae7f1caa47afe63a2efb945cf1f970a424b7ab32d656833e0bcba34c`
  - PLAN-NACHTRAG-2.md.eingefroren-20261002-082420 `f297f6d6db987956e34e23da784248b504a9c661b3894eb4086d8022ac60ad0e`
- Ausgaben (Ordner laeufe/):
  - k1-kand-st1.json `d87ece0b66a51c97e415e29e178044c90fd27055fee3fdd086aba6c4219af9d7`
  - k1-kand-st2.json `15ed957705662b33360ea5064bbd8c0c2540c7ba8e7e2c896a45318be2119732`
  - k2.json `b0472971f3ce5a8afdd4d0d333ed42961ca388800b64506a71856111465e07cc`
  - blind-kand-st1.json `ae3b2a1e1800d7fe035a87a0b94b3d27732532ab3e90bfa5dc3b4a2e59a2f887`
  - blind-kand-st2.json `bd3108bd41b38646b8732114ee5e28f2ea64bbcdf0d52d5f17810277f08d2980`
  - f1-log-st1.json `bf122a1fe0e5875465f46535bf732461d596d174bbdd08370fa816df3900aa34`
  - f1-log-st2.json `819cc4c567a89db290ed4b8977b7f0a7bbda50ef2b432131e930f5a122bbd5f7`
  - f2-log-st1.json `fb9f7efa6cbf6b07b4aa6192819d067ba891bcfaba85c361d1cd92cb6454eb0b`
  - f2-log-st2.json `7ecb08ec7d31d49884d0622779574cda1bc3eb3267e280cd0032330f64cdd98e`
  - f1-k1-st1.json `f6b711ebdffd7e1bb63ab4a873844016307769718828a90b7fbf585d7ee2b595`
  - f1-k1-st2.json `9258907f78c479f9d3a72369badd15b7fc9f452d1085a3c4156a9f544cf9e133`
  - Zeilendateien (je Ordner verkettet in Namensfolge):
    - aus-k1-st1 `2f9ef677c95588024e0d64db4924a802a50b64b3df7e91682459d476c0a796aa`
    - aus-k1-st2 `49355d4976e58d4baed9ca660afa4f513c8ac0fe640ec236f299137c8930fd1d`
    - aus-blind-st1 `f375ee2adbf1f38f61de6c98d1f6baeff5c15f338a7834462ca739c4938cb8a3`
    - aus-blind-st2 `c4f0e3abdc554b3c486d73514c2d58b2339e95323770aaccd5e9458a6d6bec1e`
    - aus-streifen-unten-st1 `662a834bb43ea137e0f85def4c6ee46a5a0a41ab961159417461b44d84b84854`
    - aus-streifen-unten-st2 `a78d84d0a65d001d2ebce114986461ee83691eb2304e9fc4faa44f4b31b2fb8f`
    - aus-streifen-oben-st1 `832474b1f54c32e6596aa8a04976a191773348bbd057c044db1a885951291a87`
    - aus-streifen-oben-st2 `3978706c04cf0691bc7248eac0b8d35b3ba5229dfe9c19352a53381cbcd00f9a`
  - Streifen-Kandidaten:
    - streifen-unten-kand-st1.json `25180a4a195a1823fe57368d0e988569470029e5707cc4749e31668c0e7fb5a6`
    - streifen-unten-kand-st2.json `2a4e58985ae1028362419bbf2f7cd751a52f1db4486ccc78031c324f38a74d19`
    - streifen-oben-kand-st1.json `4fc69e8d0d3ab29ee886c4cf55b8352fa431786e5588995ecaf29fb380224349`
    - streifen-oben-kand-st2.json `459b235d8c107932bec21e7d47a0d5142bb45237cffe2647ad88ab12d4d88f39`

## 6 Selbstanzeigen

- **Unabhaengigkeit, gelesen:**
  - KARTE.md
  - kleintest.sh (per ssh cat, nur Aufrufweise)
  - Dateinamen der ersten 50 Eintraege von /home/fmh/fmhc-physics-remote/
  - die mir mitgegebenen Kontexte (CLAUDE.md, Gedaechtnis-Index)
  - Keiner davon enthaelt Lage oder Ergebnis zum Log-Potential.
- **Unabhaengigkeit, nicht gelesen:**
  - keinen Code der Linien bic2, afm_bic, bball, qstern
  - nichts aus RUNDE-13/, RUNDE-13.md, RUNDE-16.md, RUNDE-12/x-baelle/X-BAELLE.md
  - keine Journal-Eintraege, auch nicht AGENTS.md und RESEARCH_JOURNAL.md (Projektregel "Lies AGENTS.md ...", hier wegen
    der Lesesperren bewusst nicht befolgt)
  - VORHERSAGE.sha256 nur aufgelistet, nicht geoeffnet
- **Vorfall Scratchpad (wichtig):**
  - Um 08:15:46 CEST habe ich zwei Hilfsdateien (z1.txt, z2.txt, jq-Auszuege meiner Zeilen) in das Verzeichnis
    geschrieben, das meine Umgebung als "eigenen Scratchpad" nennt
    (/tmp/claude-1000/-home-fmh-fmhc-physics/76c41c65-.../scratchpad). Das ls danach zeigte: Es ist der Scratchpad der
    Leitung.
  - Dabei habe ich die Dateinamen gesehen, unter anderem bic2_v2.py, bic2_v3.py, log-nachbau-vorhersage.txt,
    ARBEITSFELD-L4-BIC.md, journal-runde-v3-13/14/15.json, qb_rechteck.py.
  - Geoeffnet habe ich keine dieser Dateien.
  - Der Vorfall lag nach dem Ende aller Hauptlaeufe (06:13:49 UTC) und nach dem Einfrieren und Start von Nachtrag 1
    (08:15:37 CEST). Er konnte Code und Ergebnisse nicht beeinflussen.
  - Meine zwei Dateien habe ich sofort nach hilfs/ in den Kartenordner verschoben.
  - **Falls die Leitung dort eigene z1.txt oder z2.txt hatte, sind sie ueberschrieben.** Ob es sie vorher gab, kann ich
    nicht feststellen.
  - Danach nur noch Hilfsdateien im Kartenordner.
- **Lokale Interpreterstarts:**
  - L0 (1 s, geplant).
  - Zwei nicht in den Nachtraegen genannte Syntaxtests "python3 -m py_compile stille_n1.py" und "... stille_n2.py"
    (timeout 60, nice 19, je unter 1 s).
- **Abweichungen vom Plan:**
  - Die blinden Zeilen liefen je Stufe in zwei Aufrufen (30 + 27 Zeilen). Das war nach Plan Abschnitt 5 erlaubt.
  - Der Plan nannte fuer R "~34" bei 0,70. Tatsaechlich ist R das Blockmaximum, so geplant: 36,6 im ersten Block,
    130,8 bei 0,98.
- Die geplanten 6 Halbierungsrunden reichten fuer die Log-Stelle nicht. Das ist ein Planungsfehler meinerseits: Die
  Rundenzahl war an K1 gemessen, wo 2 Runden genuegten. Das Kriterium (Sprung < 0,4 rad) habe ich nicht veraendert.
- Nicht benutzt: git, Peerbus, Unteragenten, Dienste, Timer, Hooks, pkill. Status der Laeufe nur ueber Logzeilen.

## 7 Grenzen

- **Randstreifen:**
  - Die Hauptabtastung laesst an beiden Fenstergrenzen je 0,002 in rho aus.
  - Erst der nachtraegliche F3 deckt die Streifen bis 1e-5 ab. Ohne F3 waeren Stellen dort nicht ausgeschlossen.
  - Die letzten 1e-5 an den Schwellen (k -> 0 bzw. kappa -> 0) sind nicht abgetastet.
- **Doppelte Nullstellen und Faltungen:** Eine doppelte Nullstelle von G_b, die in einer Zeile nur beruehrt, und
  Faltungen zwischen zwei Zeilen findet Detektor 1 nicht. Detektor 2 (Zellen-Umlauf aus Eckwerten) ist grob und kann
  bei schneller Phasendrehung zwischen Ecken irren.
- **Fenstergrenzen in w^2:** Ein zweiter Vorzeichenwechsel des oberen Astes jenseits von 0,98 ist moeglich (s geht bei
  0,98 wieder gegen 0: -8,7e-7). Er liegt ausserhalb des Fensters und ist nicht geprueft.
- **Unterschiedliche Verfahren der Stufen:** Die Stufen unterscheiden sich nur im Schritt, nicht im Verfahren. Beide
  nutzen RK4 und denselben Code. Ein Verfahrensfehler, der beide gleich trifft, bliebe unentdeckt. K1 deckt das nur fuer
  das Kontrollmodell ab.
- **Definition von W:** W ist hier ueber die Wronski-Paarungen definiert. Eine andere zulaessige Wahl (anderer Grundsatz
  der regulaeren Loesungen) verschiebt die Kurven G_b = 0, nicht aber die Stellen. Das Vorzeichen des Umlaufs haengt von
  der Konvention ab.
- **Jost-Determinante:** Die Aussage "Umlauf 0" ist nur hergeleitet, nicht gerechnet.
- **Nachtrag:**
  - F1/F2/F3 sind nachtraeglich, also Diagnose.
  - F1/F2 zeigen nur, dass die Unaufloesung an der Randaufteilung lag.
  - F3 zeigt nur, dass in den Randstreifen kein weiterer Vorzeichenwechsel liegt.

## 8 Einfach gesagt

- Ein Q-Ball kann "atmen", also groesser und kleiner schwingen. Normalerweise strahlt er dabei Wellen ab und verliert
  Energie.
- Gesucht waren Einstellungen, bei denen das Atmen keine Welle nach aussen schickt, sogenannte stille Stellen.
- Mein selbst geschriebenes Programm findet die schon bekannte Stelle im Testmodell sehr genau wieder.
- Im Log-Modell findet es genau eine Stelle, bei w^2 = 0,92561 und rho = 1,83800, auf beiden Rechengenauigkeiten
  gleich.
- Die Pruefung "die Phase dreht sich einmal herum" war mit der vorher festgelegten Punktzahl zu grob. Erst ein
  nachtraeglich festgelegter, feinerer Durchlauf zeigt die Drehung sauber. Ob dieser zaehlt, entscheidet die Leitung.
