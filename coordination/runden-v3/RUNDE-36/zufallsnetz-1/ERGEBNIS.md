# ZUFALLSNETZ-1: Ergebnis (Code-Agent fuer die Leitung, Runde 36, explorativ)

- Gerechnet auf der .69 ueber kleintest.sh, nur Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich.
- Ablauf (Zeiten per date):
  - Start 22:52:03 CEST. Plan ab 23:12:49 CEST.
  - Rauch 21:09:11 bis 21:16:57 UTC und 21:17:15 bis 21:25:06 UTC (Saat 9 und Auswertetest; PLAN Abschnitt 6).
  - Eingefroren 23:25:46 CEST: PLAN.md.eingefroren-20261003-232546, code/*.eingefroren-20261003-232546, sha256 in
    code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe 21:25:51 bis 21:33:06 UTC, Auswertung bis 21:33:17 UTC, alle rc = 0.
  - Text ab 23:35:30 CEST.
- Alle Laeufe tragen die sha256 des eingefrorenen Skripts (zufallsnetz.py 28e04e2c..., auswertung.py 287054c7...).
  Nach dem Einfrieren wurde kein Code geaendert.
- Daten:
  - lauf-69/: je Netz .json und .log, fcc.json, kontrolle_N4000_s1_k1.json, auswertung.json (Urteile), drei Bilder
  - rauch-69/: Rauchlaeufe
- Code: code/zufallsnetz.py, code/auswertung.py, code/laeufe.sh (eingefroren); code/rauch.sh nur fuer den Rauch.
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [E] hier gerechnet, [F] von mir vor dem Einfrieren festgelegt.

## 1. Ergebnis

1. **Ein ungeordnetes Tetraedernetz ist ohne Feinabstimmung fast richtungsfrei, und der Rest schwindet mit der
   Groesse [E].**
   - Delaunay-Netz aus Zufallspunkten, Federn auf allen Kanten, k = 1, nach nichtaffiner Relaxation:
     - Die Querwellen schwanken mit der Richtung um 0,95 % (N = 4000), 0,43 % (N = 16000) und 0,28 % (N = 64000),
       je Mittel ueber zwei Saaten.
     - Die groesste Doppelbrechung betraegt bei N = 64000 0,30 % und 0,37 %.
   - Der Rest faellt wie N^(-0,43), passend zu einem Rauschen, das sich wegmittelt (erwartet N^(-1/2), [H]).
   - Zum Vergleich das fcc-Netz aus NETZ-C-1: 41 % und 22 % Schwankung, 41 % Doppelbrechung laengs [110].
2. **Die Laengswelle bleibt deutlich schneller, aber anders als die Karte erwartete [E].**
   - c_l/c_q = 1,681 (k = 1, N = 64000, beide Saaten). Das liegt unter dem affinen Wert sqrt 3 = 1,732.
   - Grund: Die Relaxation senkt hier den Kompressionsmodul staerker (K/K_affin = 0,687) als den Schermodul
     (G/G_affin = 0,767). Die Schreibtischannahme der Karte war umgekehrt.
   - Mit k = 1/l relaxieren beide etwa gleich (0,829 und 0,817), also c_l/c_q = 1,739.
3. **Kein Netz hat hier eine einzige Geschwindigkeit fuer alle drei Wellen [E, M].**
   - Die zwei Querwellen werden gleich und richtungsfrei.
   - Die Laengswelle bleibt 1,68-mal (k = 1) bzw. 1,74-mal (k = 1/l) so schnell. Das passt zum Satz aus
     GEGENLESEN-R35 4b.
4. **Vorhersagen:**
   - eingetroffen: Z0, Z1, Z2, Z4
   - nicht eingetroffen: Z3 (c_l/c_q = 1,681 statt 1,75 bis 2,2)
5. **Kontrollen [E]:** Die Born-Probe ist eine davon unabhaengige Kontrolle.
   - Die dynamische Matrix bei kleinem Wellenvektor trifft die Christoffel-Geschwindigkeiten aus dem relaxierten
     Tensor auf 2e-8. Der Rest skaliert wie k^2.
   - Damit ist auch der weiche Kompressionsmodul (Punkt 2) bestaetigt.
   - Ohne Relaxation laege die Laengswelle 18 % hoeher.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 23:25:46 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| Z0 | fcc trifft NETZ-C-1 auf 1e-6; Grad 15,5 +- 0,1; affin C12 = C44 auf 1 % | 85 % | **eingetroffen** | fcc: groesste Abweichung 3,5e-8 (Rest von \|k\| = 1e-3 in NETZ-C-1; gegen die geschlossenen Formen 2e-16). Grad 15,512 / 15,564 / 15,537 / 15,542 / 15,536 / 15,529. Affin \|lambda/mu - 1\| <= 7e-16 in allen zwoelf Tensoren (Lesart [F], siehe Selbstanzeige 1) |
| Z1 | N = 64000: Querwellen-Schwankung < 3 % und Doppelbrechung < 3 %, beide Saaten | 70 % | **eingetroffen** | Saat 1: S_T 0,272 %, D 0,304 %. Saat 2: S_T 0,298 %, D 0,368 % |
| Z2 | Schwankung ~ N^(-p), p in [0,35; 0,65] | 60 % | **eingetroffen** | Saatmittel S_T 0,952 % / 0,427 % / 0,285 %; p = 0,435. Residuen in ln: +0,07 / -0,13 / +0,07 |
| Z3 | c_l/c_q in [1,75; 2,2] (k = 1, N = 64000) | 65 % | **nicht eingetroffen** | 1,6815 (Saat 1), 1,6812 (Saat 2); isotrope Projektion 1,6815 / 1,6812 |
| Z4 | G/G_affin in [0,5; 0,9] (k = 1) | 60 % | **eingetroffen** | 0,762 / 0,769 / 0,765 / 0,766 / 0,767 / 0,766 (N = 4000, 16000, 64000; je Saat 1 / 2) |

- **Bedeutung, wie vorab festgelegt:**
  - "Z1 und Z2 treffen ein" ist ausgeloest: Ein ungeordnetes Tetraedernetz ist ohne Feinabstimmung richtungsfrei.
    - Es gibt eine Quergeschwindigkeit fuer beide Polarisationen, in alle Richtungen, bis auf ein Rauschen, das mit
      der Groesse verschwindet.
    - Fuer Finns Bild ist das der natuerliche Weg zu einer einzigen "Lichtgeschwindigkeit" der Querwellen.
  - Uebrig bleiben:
    - die Laengswelle, 1,68-mal so schnell (Z3 nicht eingetroffen, aber in der anderen Richtung als erwartet)
    - das bevorzugte Ruhesystem des Netzes
  - "Z1 verfehlt" ist nicht ausgeloest.

## 3. Tabellen [E]

- **Einheiten:** Punktdichte 1 (mittlerer Abstand 1), Masse 1 je Knoten, k = 1 (k1) oder k = 1/l (kl).
  Geschwindigkeiten in diesen Einheiten.
- **Bezeichnungen:**
  - S_1, S_2, S_3: Richtungsschwankung max/min - 1 von Ast 1 (langsame Querwelle), Ast 2 (schnelle Querwelle),
    Ast 3 (Laengswelle) ueber 403 Richtungen
  - S_T = max(S_1, S_2); D = groesste Doppelbrechung c2/c1 - 1

### Tabelle 1: Netze (Pruefungen je Netz; k1 und kl haben dieselbe Kantenliste, sha256 gleich)

| N | Saat | Kanten | mittlerer Grad | Tetraeder je Punkt | Grad min..max | Umkugel-Abstand zum Rand | CG-Iterationen k1 / kl | Dauer k1 |
|---|---|---|---|---|---|---|---|---|
| 4000 | 1 | 31024 | 15,512 | 6,756 | 6..29 | >= 2,32 | 96 / 110 | 1,6 s |
| 4000 | 2 | 31127 | 15,564 | 6,782 | 6..28 | >= 2,42 | 95 / 110 | 1,5 s |
| 16000 | 1 | 124297 | 15,537 | 6,769 | 6..30 | >= 2,37 | 135 / 155 | 7,1 s |
| 16000 | 2 | 124338 | 15,542 | 6,771 | 6..33 | >= 2,41 | 135 / 155 | 7,3 s |
| 64000 | 1 | 497167 | 15,536 | 6,768 | 4..31 | >= 2,28 | 198 / 233 | 37 s |
| 64000 | 2 | 496919 | 15,529 | 6,764 | 5..33 | >= 2,43 | 199 / 238 | 38 s |

- Literatur [L]: Tetraeder je Punkt 24 pi^2/35 = 6,768, mittlerer Grad 15,535.
- In allen Netzen erfuellt:
  - Euler E = N + T
  - jede Randkante von beiden Enden gefunden
  - kein Punkt ausgelassen, keine Selbstkante
  - alle Umkugeln im Rand m = 5

### Tabelle 2: Elastische Groessen (isotrope Projektion, Voigt-Mittel)

| N | Saat | Feder | lambda | mu = G | K | G/G_affin | K/K_affin | c1 / c2 / c3 (Richtungsmittel) | c_l/c_q | affin c_l/c_q |
|---|---|---|---|---|---|---|---|---|---|---|
| 4000 | 1 | k1 | 0,5954 | 0,7254 | 1,0790 | 0,7619 | 0,6799 | 0,8498 / 0,8536 / 1,4305 | 1,6796 | 1,7321 |
| 4000 | 2 | k1 | 0,6055 | 0,7299 | 1,0921 | 0,7685 | 0,6900 | 0,8510 / 0,8575 / 1,4371 | 1,6823 | 1,7322 |
| 16000 | 1 | k1 | 0,6015 | 0,7278 | 1,0868 | 0,7650 | 0,6854 | 0,8521 / 0,8541 / 1,4343 | 1,6812 | 1,7321 |
| 16000 | 2 | k1 | 0,6008 | 0,7279 | 1,0860 | 0,7656 | 0,6854 | 0,8514 / 0,8548 / 1,4341 | 1,6809 | 1,7321 |
| 64000 | 1 | k1 | 0,6026 | 0,7283 | 1,0881 | 0,7668 | 0,6874 | 0,8526 / 0,8542 / 1,4350 | 1,6815 | 1,7321 |
| 64000 | 2 | k1 | 0,6009 | 0,7271 | 1,0856 | 0,7665 | 0,6867 | 0,8517 / 0,8536 / 1,4335 | 1,6812 | 1,7321 |
| 4000 | 1 | kl | 0,5532 | 0,5422 | 0,9147 | 0,8152 | 0,8251 | 0,7347 / 0,7380 / 1,2797 | 1,7379 | 1,7321 |
| 4000 | 2 | kl | 0,5584 | 0,5469 | 0,9230 | 0,8199 | 0,8304 | 0,7372 / 0,7417 / 1,2854 | 1,7383 | 1,7321 |
| 16000 | 1 | kl | 0,5574 | 0,5439 | 0,9200 | 0,8165 | 0,8286 | 0,7367 / 0,7383 / 1,2827 | 1,7392 | 1,7321 |
| 16000 | 2 | kl | 0,5553 | 0,5434 | 0,9176 | 0,8159 | 0,8267 | 0,7359 / 0,7383 / 1,2814 | 1,7384 | 1,7321 |
| 64000 | 1 | kl | 0,5568 | 0,5441 | 0,9195 | 0,8174 | 0,8288 | 0,7370 / 0,7381 / 1,2825 | 1,7388 | 1,7321 |
| 64000 | 2 | kl | 0,5558 | 0,5432 | 0,9179 | 0,8168 | 0,8282 | 0,7364 / 0,7377 / 1,2815 | 1,7387 | 1,7321 |

- **Affin (k1, N = 64000, Saat 1):** lambda = mu = 0,9498, K = 1,5829; c1 / c2 / c3 = 0,9736 / 0,9755 / 1,6880.
- **Querdehnzahl** nu = (3K - 2G)/(2(3K + G)):
  - k1: 0,226; kl: 0,253; affin 0,25 (Cauchy)
  - aus Tabelle 2 nachgerechnet [M]
- **Selbstmittelnd:** G/G_affin und c_l/c_q aendern sich zwischen den Groessen und Saaten erst in der dritten
  Stelle.

### Tabelle 3: Richtungsabhaengigkeit nach der Relaxation (in %)

| N | Saat | Feder | S_1 / S_2 / S_3 | S_T | D | RMS c1 / c2 / c3 (Std/Mittel) | affin S_1 / S_2 / S_3 | affin D |
|---|---|---|---|---|---|---|---|---|
| 4000 | 1 | k1 | 0,649 / 0,917 / 1,056 | 0,917 | 0,941 | 0,146 / 0,199 / 0,259 | 0,715 / 0,595 / 0,824 | 0,885 |
| 4000 | 2 | k1 | 0,786 / 0,987 / 2,319 | 0,987 | 1,371 | 0,203 / 0,264 / 0,590 | 0,957 / 1,372 / 2,232 | 1,615 |
| 16000 | 1 | k1 | 0,293 / 0,300 / 0,760 | 0,300 | 0,519 | 0,084 / 0,078 / 0,199 | 0,355 / 0,423 / 0,668 | 0,525 |
| 16000 | 2 | k1 | 0,475 / 0,555 / 1,314 | 0,555 | 0,704 | 0,115 / 0,132 / 0,315 | 0,626 / 0,902 / 1,673 | 1,060 |
| 64000 | 1 | k1 | 0,272 / 0,221 / 0,606 | 0,272 | 0,304 | 0,063 / 0,051 / 0,147 | 0,272 / 0,262 / 0,639 | 0,354 |
| 64000 | 2 | k1 | 0,298 / 0,179 / 0,612 | 0,298 | 0,368 | 0,077 / 0,042 / 0,171 | 0,250 / 0,303 / 0,710 | 0,414 |
| 4000 | 1 | kl | 0,726 / 0,692 / 0,925 | 0,726 | 0,986 | 0,187 / 0,156 / 0,255 | 0,658 / 0,610 / 0,699 | 0,861 |
| 4000 | 2 | kl | 0,851 / 0,903 / 1,740 | 0,903 | 1,131 | 0,212 / 0,211 / 0,446 | 1,013 / 1,226 / 1,631 | 1,380 |
| 16000 | 1 | kl | 0,274 / 0,319 / 0,538 | 0,319 | 0,501 | 0,068 / 0,080 / 0,140 | 0,306 / 0,355 / 0,474 | 0,422 |
| 16000 | 2 | kl | 0,386 / 0,525 / 1,080 | 0,525 | 0,616 | 0,095 / 0,130 / 0,256 | 0,519 / 0,644 / 1,169 | 0,759 |
| 64000 | 1 | kl | 0,239 / 0,171 / 0,475 | 0,239 | 0,256 | 0,055 / 0,039 / 0,116 | 0,212 / 0,200 / 0,521 | 0,268 |
| 64000 | 2 | kl | 0,205 / 0,239 / 0,513 | 0,239 | 0,311 | 0,049 / 0,060 / 0,132 | 0,182 / 0,288 / 0,514 | 0,354 |

- **Relaxation und Anisotropie:** Die Relaxation verstaerkt die Restanisotropie nicht. Sie ist nach der Relaxation
  etwa so gross wie im affinen Tensor, meist etwas kleiner.
- **Laengswelle:** Sie schwankt etwa doppelt so stark wie die Querwellen (0,61 % bei N = 64000), relativ zu ihrer
  Geschwindigkeit.
- **Exponenten** (Information, keine Urteile; ungewichtete Ausgleichsgerade ueber drei Groessen):

  | Groesse | k1 Saat 1 | k1 Saat 2 | k1 Saatmittel | kl Saatmittel |
  |---|---|---|---|---|
  | S_T | 0,439 | 0,431 | **0,435** | 0,443 |
  | D | 0,407 | 0,475 | 0,446 | 0,475 |
  | S_1 / S_2 / S_3 (Saatmittel) | | | 0,333 / 0,562 / 0,368 | 0,457 / 0,490 / 0,358 |

  - Von N = 4000 nach 16000 faellt S_T (Saatmittel, k1) wie N^(-0,58), von 16000 nach 64000 wie N^(-0,29).
  - Mit zwei Saaten ist das im Rauschen: Saat 2 liegt bei N = 16000 fast doppelt so hoch wie Saat 1.

### Bilder (lauf-69/)

- geschwindigkeitsflaechen.png: Abweichung der drei Geschwindigkeiten vom Richtungsmittel und Doppelbrechung ueber
  die ganze Kugel (Karte theta, phi), N = 4000 und N = 64000, Saat 1, k = 1, gleiche Farbskala je Spalte.
- schwankung_gegen_n.png: S_T, D und S_3 gegen N, doppelt logarithmisch, Einzelsaaten, Saatmittel, Ausgleichsgerade,
  Bezugssteigung -1/2, Z1-Schwelle.
- schnitt_xy_fcc_gegen_zufall.png: Geschwindigkeiten in der xy-Ebene fuer fcc mit Zentralfedern und das
  Zufallsnetz N = 64000, je durch die mittlere Querwelle geteilt.

## 4. Kontrollen

- **fcc-Gegenprobe (Z0 a):** gleicher Code, 256 Knoten, 1536 Kanten.
  - Affiner gleich relaxierter Tensor: Die Knotenkraefte sind null (|f| <= 3e-14) [M].
  - C11 = 1,414214, C12 = C44 = 0,707107 wie geschlossen [M].
  - Gegen NETZ-C-1 (alle 403 Richtungen, drei Aeste): groesste Abweichung 3,5e-8 in [110] Ast 3. Das ist der Rest
    des endlichen |k| = 1e-3 dort. Gegen die geschlossenen Formen 2e-16.
- **Loeser (Kontrolllauf N = 4000, Saat 1, k1):**
  - Direktloeser (splu, Knoten 0 fest) gegen CG mit 1e-10: Tensor gleich auf 4e-16.
  - CG mit rtol 1e-6 / 1e-8 / 1e-12: Tensor auf 1,8e-12 / 4e-16 / 6e-16 (Energieform). Die Kurzform liegt bei 2e-8 /
    8e-11 / 1e-14, ihr Fehler ist wie erwartet linear.
  - In allen Hauptlaeufen: Residuen < 1e-10, Abstand Energieform zu Kurzform <= 2,1e-12, Asymmetrie der Kurzform
    <= 1,6e-12, alle sechs Eigenwerte von C_V positiv (kleinster 0,72 bei k1, 0,54 bei kl).
- **Born-Probe langer Wellen (unabhaengig vom Relaxationscode):**
  - Werte bei |k| = 1e-3 x 2 pi/L in [100], [110], [111] und Richtung 203:
    - quer -1,6e-8 bis -1,7e-8
    - laengs -3,8e-8 bis -4,1e-8
  - Bei 2e-3 ([100]): -6,5e-8 / -6,7e-8 / -1,6e-7, also das Vierfache.
  - Die Abweichung ist damit Dispersion O(k^2). Hochgerechnet auf k -> 0 ((4 r(k) - r(2k))/3) bleibt in [100] weniger
    als 1e-9.
  - Der affine Tensor laege bei den Querwellen 14 % und bei der Laengswelle 18 % daneben.
  - Die Probe bestaetigt also die nichtaffine Relaxation und den weichen Kompressionsmodul.
- **Richtungsproben:** 20000 Fibonacci-Richtungen und Nelder-Mead-Verfeinerung der Extrema aendern S_T und D um
  hoechstens 0,04 Prozentpunkte. Kein Urteil dreht sich (Z1: 0,31 % und 0,37 % gegen 3 %).
- **Netzgleichheit:** k1 und kl je Netz mit gleicher sha256 der Kantenliste. Kontrolllauf und Hauptlauf
  N = 4000/Saat 1 ebenso (5ba128fe...).

## 5. Selbstanzeigen

1. **Lesart von "C12 = C44" (Z0 c) [F]:**
   - Ich habe die Cauchy-Beziehung lambda = mu der isotropen Projektion geurteilt. Fuer Zentralfedern gilt sie
     identisch [M]; geprueft wird damit nur der Code.
   - Die woertliche Komponentenlesart C1122 = C2323 haette Z0 scheitern lassen: N = 4000, Saat 2: -2,08 % (k1) und
     -2,01 % (kl).
   - Die anderen Netze liegen dort unter 0,36 %. Die Abweichung ist die Restanisotropie, wie im Plan geschaetzt
     (~1 % bei N = 4000).
   - Diese Lesart war vor dem Einfrieren festgelegt (PLAN Abschnitt 3), ist aber eine Zusatzvorgabe von mir.
2. **Weitere Festlegungen [F] (alle im Plan vor dem Einfrieren):**
   - S_T = max(S_1, S_2)
   - D = groesstes c2/c1 - 1
   - c_l/c_q aus Richtungsmitteln
   - G aus der Voigt-Projektion
   - Z1 und Z2 nur fuer k1
   - Z2 als Fit an das arithmetische Saatmittel
   - Z4 ueber alle sechs k1-Netze
   - Keine dieser Wahlen ist knapp:
     - Z1 liegt um den Faktor 8 unter der Schwelle.
     - Z3 liegt auch in der isotropen Projektion und fuer kl unter 1,75.
     - Z4 haelt in allen Netzen (0,762 bis 0,769), auch fuer kl (0,815 bis 0,820).
     - Z2: Einzelsaaten 0,439 und 0,431, beide im Fenster.
3. **Z0 ist weitgehend vorab ableitbar:**
   - Teil c [M].
   - Teil b ist Literatur [L]; der Rauch zeigte ihn schon (Saat 9: 15,5545 und 15,5440).
   - Teil a sah ich im Rauch (3,5e-8). Er prueft nur den affinen Teil; die Relaxation pruefen Born-Probe und
     Direktloeser.
4. **Gesehen vor dem Einfrieren** (PLAN Abschnitt 6):
   - Netzpruefungen, Grade, CG-Zeiten, fcc-Abweichung, Born-Abweichungen fuer Saat 9
   - keine Tensoren und keine Urteilsgroessen
   - Den Auswertetest (N = 500 bis 2000) habe ich nur auf Rueckgabewert und Schluessel geprueft.
5. **Codeaenderungen:**
   - vor dem Einfrieren: Born-Probe von sieben auf fuenf Punkte, Zwischenspeicher; ein Versuch mit eigener
     Faktorisierung war langsamer und wurde zurueckgenommen
   - nach dem Einfrieren: keine
6. **Schreibtisch der Karte:**
   - Die Erwartung "Relaxation senkt den Schermodul staerker als den Kompressionsmodul, also c_l/c_q > sqrt 3" trifft
     fuer diese Netze nicht zu.
   - Bei k = 1 relaxiert der Kompressionsmodul staerker. Eine Deutung [H]:
     - Bei gleichmaessiger Dehnung zieht jede Feder mit k l eps, also lange Kanten staerker.
     - Ein Knoten, der nicht im Schwerpunkt seiner Nachbarn sitzt, wird deshalb schon bei reiner Dehnung verschoben.
     - Bei k = 1/l ziehen alle Federn gleich stark (eps); dann relaxieren K und G gleich.
   - Geprueft habe ich diese Deutung nicht.
7. **Rauschen in Z2:**
   - Nur zwei Saaten je Groesse. Saat 2 liegt bei N = 16000 fast doppelt so hoch wie Saat 1.
   - p = 0,435 ist mit 0,5 vertraeglich, aber nicht genau bestimmt (grob +-0,1, PLAN Abschnitt 5 [H]).
8. **Was die N-Abhaengigkeit bedeutet [H]:**
   - Gemessen ist die Anisotropie des Tensors einer periodischen Probe aus N Knoten.
   - Ein unendliches Zufallsnetz ist im Mittel exakt isotrop. Der Rest beschreibt, wie ungleich ein Ausschnitt aus
     N Knoten ist.
   - Fuer eine Welle, die viel laenger als die Masche ist, wirkt er eher als Streuung und Dispersion denn als feste
     Richtungsabhaengigkeit.
   - Eine Hochrechnung auf die Lichtgrenze 1e-17 [L, Herrmann u. a. 2009] mit N^(-1/2) ab 0,285 % bei N = 64000 gibt
     ~5e33 Knoten, also (1,7e11)^3. Bei Planck-Masche waere das ein Wuerfel von ~3e-24 m.
   - Das ist nur eine Groessenordnungsrechnung [H].
9. **Ruhesystem:** Ein raeumliches Zufallsnetz ist im Mittel drehinvariant, aber nicht boostinvariant [M].
   - Anders als die Poisson-Streuung in der Raumzeit bei Bombelli/Henson/Sorkin [L] waehlt es ein Ruhesystem.
   - Das bleibt ungeprueft offen, wie in der Karte.
10. **Richtungsmenge:** R403 enthaelt die Wuerfelachsen [100], [110], [111]. Fuer ein Zufallsnetz haben sie keine
    Sonderrolle. Ich habe sie wegen der fcc-Gegenprobe behalten.
11. **"Poisson-Punkte"** sind hier N gleichverteilte Punkte (Binomialprozess, feste Punktzahl) [F].
12. **Startbefehl Rauch 1:** Die ssh-Sitzung kehrte erst nach Rauchende zurueck (Befehlskette im Hintergrund). Ohne
    Wirkung auf die Laeufe. Hauptlaeufe mit getrenntem nohup.
13. **Zeitbox:** Start 22:52, Text ab 23:35 CEST; innerhalb von 120 min.

## 6. Einfach gesagt

Finns Bild ist ein Netz aus Tetraedern, durch das Wellen laufen wie Licht. In einem ordentlich gebauten
Kristallnetz haengt die Geschwindigkeit stark von der Richtung ab, beim fcc-Netz um bis zu 41 %. In einem zufaellig
gewuerfelten Tetraedernetz ohne jede Feineinstellung sind die beiden Querwellen dagegen in alle Richtungen fast
gleich schnell: Bei 64 000 Knoten bleiben nur 0,3 %, und je groesser das Netz, desto kleiner wird dieser Rest. Fuer
die Querwellen, die Wellensorte, die dem Licht entspricht, entsteht so von selbst eine einzige Geschwindigkeit. Eine
einzige Geschwindigkeit fuer alle Wellen gibt es aber nicht: Die Laengswelle laeuft immer etwa 1,7-mal so schnell,
und das Netz selbst ruht in einem bestimmten Bezugssystem.
