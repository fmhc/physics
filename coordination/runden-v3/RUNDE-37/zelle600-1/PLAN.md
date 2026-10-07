# ZELLE600-1: Plan (Code-Agent fuer die Leitung claude-primary)

- **Auftrag (Finn, woertlich):** "Welche 600 Zelle? Bau die". Karte KARTE.md ist bindend, Z0 bis Z4 bleiben unveraendert.
- **Zeiten (date):** Start 2026-10-05 06:12:00 CEST. Dieser Plan ab 06:18:41 CEST, vor jeder Rechnung. Zeitbox bis 07:42 CEST.
- **Rechenort:** .69, Arbeitsordner /home/fmh/fmhc-physics-remote/zelle600-1/, Aufruf ueber
  /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spur cpu (Ausweich cpu2), ein Thread, je Lauf hoechstens 10 min.
  Ergebnisse als JSON nach RUNDE-37/zelle600-1/lauf-69/.
- **Lokal nur Darstellung:** zelle600.html (Canvas, ohne Module, ohne CDN, per file://), zelle600.png per headless Chrome mit GPU.
  Kein lokales python, awk, perl; jq nur lesend.
- **Kennzeichen:** [M] eigene Schreibtischrechnung, [E] gerechnet (.69), [L] Literatur aus dem Gedaechtnis, [P] Projektdatei, [H] Hypothese.
- **Projektsuche** (grep mit allen Ausschluessen nach "600-Zelle", "600-cell", "{3,3,5}", "Boerdijk"): Die 600-Zelle kommt
  nur als Stichwort vor (RUNDE-27 GEOMETRIE-XD: 7,36 Grad Luecke; RUNDE-34/TETRAEDER-ANALYSE.md: 30er-Ring der Tetrahelix,
  Drehung arccos(-2/3) je Tetraeder) [P]. Kein Projektlauf hat sie gebaut oder ihr Spektrum gerechnet.

## 1. Bau und Pruefungen Z0

- **Ecken:** genau das Rezept der Karte. 8 Permutationen von (+-1,0,0,0), 16 von (+-1/2)^4, 96 gerade Permutationen von
  1/2 (+-phi, +-1, +-1/phi, 0), Reihenfolge (a, b, c, d) = a + b i + c j + d k.
  - [M] Die geraden Permutationen dieser Grundfolge sind die ungeraden der Lehrbuchfolge (0, 1, 1/phi, phi). Das ist das
    Bild der Lehrbuch-2I unter i <-> j, einem Antiautomorphismus. Also auch eine Gruppe. Gepruefte Abgeschlossenheit
    (alle 14400 Produkte in der Menge, Einselement, Inverse) entscheidet das.
- **Kanten:** Paare mit Skalarprodukt phi/2 = cos 36 Grad, also Laenge 1/phi bei Radius 1.
  **Dreiecke, Tetraeder:** 3- und 4-Cliquen.
- **Pruefungen Z0** (alle vorab ableitbar, Kontrolle, keine Messung):
  - Zahlen 120 / 720 / 1200 / 600, Euler 120 - 720 + 1200 - 600 = 0.
  - 12 Nachbarn je Ecke, 5 Tetraeder je Kante, 20 je Ecke, jedes Dreieck in genau 2 Tetraedern.
  - Eckfigur = Ikosaeder (Link: 12 Ecken, 30 Kanten, 20 Dreiecke, Grad 5).
  - alle Kantenlaengen gleich, alle 600 Tetraeder regulaer (6 Kanten, Volumen l^3/(6 sqrt 2)).
- **Schalen um den Pol** (Ecke 1 = (1,0,0,0)), Schreibtisch [M]:
  - nach Winkel auf S^3: 0, 36, 60, 72, 90, 108, 120, 144, 180 Grad mit 1, 12, 20, 12, 30, 12, 20, 12, 1 Ecken
    (Konjugationsklassen von 2I);
  - nach Graphabstand: 1, 12, 32, 42, 32, 1;
  - Kreuztabelle. [M] Abstand 2 mischt 60 und 72 Grad mit 3 bzw. 1 gemeinsamen Nachbarn; der Graph ist also nicht
    abstandsregulaer. Die Rechnung prueft das.

## 2. Regge-Kruemmung Z3 (Schreibtisch vorab)

- [M] Diederwinkel des regulaeren Tetraeders arccos(1/3) = 70,5288 Grad. Fehlwinkel je Kante
  delta = 2 pi - 5 arccos(1/3) = 0,128388 rad = 7,3561 Grad.
- [M] Summe(l delta) = 720 * (1/phi) * 0,128388 R = 57,131 R. Kontinuum (1/2) Integral R dV = (1/2)(6/R^2)(2 pi^2 R^3)
  = 6 pi^2 R = 59,218 R. Verhaeltnis 0,9648, Abweichung -3,5 %.
- [M] Zweite Lesart: gleiches Volumen statt gleichem Umkreis. 600 flache Tetraeder haben 600 l^3/(6 sqrt 2) = 16,693 R^3,
  S^3 hat 2 pi^2 R^3 = 19,739 R^3, R_eff = 0,9457 R. Dann 6 pi^2 R_eff = 56,00 R, Regge +2,0 %.
- **Erwartung Z3:** erfuellt in beiden Lesarten (innerhalb 5 %). Vorab ableitbar, keine Messung.
- **Rechnung:** Diederwinkel aus den 4D-Koordinaten jedes Tetraeders an jeder Kante, je Kante die 5 Winkel summieren,
  delta je Kante (min, max), Summe(l delta), beide Vergleiche.

## 3. Spektrum Z1, Z2, Z4 (Schreibtisch vorab)

- [M] Der Kantengraph ist der Cayley-Graph von 2I mit der Konjugationsklasse C (Realteil phi/2, 12 Elemente).
  Eigenwerte daher lambda_rho = 12 chi_rho(c) / d_rho mit Vielfachheit d_rho^2, je irreduzibler Darstellung rho.
  - Die SU(2)-Darstellungen V_j (j = 0 bis 5/2, Dimension k+1 mit k = 2j) bleiben auf 2I irreduzibel:
    chi = sin((k+1) pi/5) / sin(pi/5), also
    lambda = 12, 6 phi = 9,708, 4 phi = 6,472, 3, 0, -2 mit Vielfachheiten 1, 4, 9, 16, 25, 36.
  - Uebrig 29 = 4 + 9 + 16: Galois-Partner 2' (-6/phi = -3,708), 3' (-4/phi = -2,472) und die 4 von A5 (-3).
  - Spur 0 und Spur A^2 = 1440 stimmen.
- **Z1 [M]:** fallend sortiert 12, 9,708, 6,472, 3, 0, -2, -2,472, -3, -3,708 mit 1, 4, 9, 16, 25, 36, 9, 16, 4.
  Erwartung: erfuellt, vorab ableitbar.
- **Z2 [M]:** Laplace L = 12 I - A steigend: 0, 2,292, 5,528, 9, 12, 14 | 14,472, 15, 15,708 mit
  1, 4, 9, 16, 25, 36 | 9, 16, 4. Erwartung: erfuellt, vorab ableitbar.
  - Abbruch nach n = 6: die Harmonischen vom Grad 6 (49) und 7 (64) falten sich auf 25 und 4 Dimensionen
    (3' + 4 bzw. 2'), weil 120 Ecken nur 120 Muster tragen.
- **Z4 [M]:** Verhaeltnis lambda_k / lambda_1 gegen k(k+2)/3:
  - k = 2: 2,412 gegen 2,667 (-9,5 %);
  - k = 3: 3,927 gegen 5 (-21,5 %).
  - Erwartung: **nicht erfuellt** (k = 3 liegt ausserhalb 10 %). Vorab ableitbar.
- **Rechnung:**
  - eigh von A und L (120 x 120), Eigenwerte auf 1e-8 buendeln, Vielfachheiten, Abstand zu den geschlossenen Formen.
  - Identitaetsprobe Harmonische: Polynome vom Grad <= k auf den Ecken, Rang je k (Erwartung
    1, 5, 14, 30, 55, 91, 116, 120 fuer k = 0 bis 7). Pruefen, dass ihr Spann fuer k <= 5 genau der Eigenraum der
    k+1 untersten Laplace-Niveaus ist (Restnorm), und wohin Grad 6 und 7 fallen.

## 4. 30er-Ring (Boerdijk-Coxeter-Helix)

- Lauf von einem geordneten Tetraeder (v0, v1, v2, v3): v_{i+4} = die Ecke gegenueber v_i ueber dem Dreieck
  (v_{i+1}, v_{i+2}, v_{i+3}). Erwartung [L, P RUNDE-34]: schliesst nach 30 Tetraedern, 30 verschiedene Ecken.
- Pruefen: Schluss, 30 verschiedene Tetraeder und Ecken; Rang der Ecken v0, v3, v6, ... (Grosskreis?).
- Zusatz, billig: Bahn des Rings unter Links- bzw. Rechtsmultiplikation mit 2I. Erwartung [L]: 20 disjunkte Ringe
  zerlegen alle 600 Tetraeder. Nur wenn gefunden, in der Ansicht waehlbar.

## 5. Ansicht

- zelle600.html, eine Datei, Canvas 2D ohne externe Skripte (laeuft per file:// und offline).
- Daten inline als JSON aus lauf-69/ansicht.json (jq -c ausgeben, mit Edit einfuegen, danach per diff gegen jq pruefen).
- Inhalt:
  - Stereographische Projektion vom Gegenpol, Pol in der Mitte.
  - Kanten als projizierte Grosskreisboegen.
  - Schieberegler xw, yw, zw, Maus- und Touch-Drehung, Zoom.
  - Ecken nach Schale gefaerbt (Winkel, umschaltbar auf Graphabstand), Legende mit Zahlen, Schalen ein- und ausblendbar.
  - Knopf "30er-Ring".
  - Kurztext fuer Finn und Niveau-Bild des Laplace-Spektrums neben n^2.
  - Hell und dunkel, Handy.
- PNG mit dem Chrome-Aufruf aus dem Auftrag, Sichtprobe per Read.

## 6. Abbruch und Grenzen

- Faellt die Gruppenpruefung oder Z0 aus, zuerst den Bau pruefen und nichts weiter deuten.
- Findet sich kein 30er-Ring, wird das so berichtet; der Knopf entfaellt.
- Alles ist Geometrie und Darstellungstheorie, keine Messdaten. Z0, Z1, Z2, Z3 und Z4 sind vorab ableitbar.
  Die Rechnung bestaetigt sie nur oder findet einen Baufehler.
