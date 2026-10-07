# TENSOR-EIS-N: Ergebnis (Code-Agent fuer die Leitung, Runde 36, explorativ)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-03 23:24:33 CEST; Quelle gelesen vor 23:40:41 CEST (naechster date-Aufruf).
  - Plantext ab 23:55:41 CEST.
  - Rauchlaeufe 21:50:50 bis 22:00:46 UTC (PLAN Abschnitt 8).
  - Eingefroren 2026-10-04 00:01:30 CEST:
    - PLAN.md.eingefroren-20261004-000130 (sha256 ebdbaca4...);
    - code/tn.py (4952a92e...) und code/tn_auswertung.py (2d8a0dd0...), Kopien *.eingefroren-20261004-000130;
    - code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe 22:01:45 bis 22:07:22 UTC, alle rc = 0. Auswertung 22:07:31 bis 22:07:34 UTC.
  - Text ab 00:10:20 CEST.
  - Code nach dem Einfrieren unveraendert; die Pruefsummen auf der .69 und lokal stimmen ueberein.
- Alle Zahlen sind Gitterrechnungen auf der .69 (lauf-69/), keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (Gu/Wen 2009, arXiv:0907.1203v3, Seite bzw. Gleichung);
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher;
  - [H] Hypothese;
  - [M] vorab ableitbar (PLAN Abschnitt 3);
  - [E] hier gerechnet;
  - [F] Festlegung im Plan.
- **Einheiten:** J = g = 1, Massen m1 = m2 = 1, r in Gitterabstaenden; U < 0 heisst gebunden.

## 1. Ergebnis zuerst

1. **N-Typ: Gleiche Massen ziehen sich auf dem kubischen Gitter an, genau wie Newton [E, M].**
   - U(r) = -(g/2) m1 m2 G(r), mit G der Greenschen Funktion des Gitter-Laplace. Torus-korrigiert trifft das
     -1/(8 pi r) auf 2,0 % ab r = 4 und auf 0,41 % ab r = 8.
   - Exponenten 1,011 ([100]), 0,999 ([110]), 0,995 ([111]), Schale 1,001.
   - Der Wert ist ein **echtes Minimum** auf der Zwangsflaeche, kein Sattel. Die Richtung mit dem "falschen" Vorzeichen
     (konformer Modus) ist durch die Masse selbst festgelegt; sie ist nicht frei.
2. **L-Typ: keine Wechselwirkung, auch keine Abstossung [E, M].**
   - Torus-korrigiert gilt |U| < 1e-16 fuer alle 2 <= r <= 16.
   - Roh bleibt nur die Torus-Konstante -1/(2 L^3).
   - Der statische Kern ist eine Konstante (Kontaktglied). Gu/Wens Angabe "repulsive ... |x1 - x2|^-4" (S. 11) folgt aus
     Gl. 27 und 31 in dieser Fassung nicht.
   - **N0 ist damit nicht eingetroffen.** Die gemeinsamen Bausteine (inc, Skalarbedingung, Gitterlagen) sind gegen
     Gu/Wens N-Matrix auf S. 19 auf 1e-15 bestaetigt (Kontrolle K3), der L-Typ zusaetzlich exakt gegen seine
     Dispersion Gl. 30 (K4).
3. **N-Typ-Form: indefinit, aber nur ausserhalb der eichfreien Zwangsflaeche (N2 eingetroffen) [E, M].** Je q gibt es
   zwei negative Richtungen:
   - E-Spur (-1/2): zu 2/3 Eichrichtung (Gl. 23), zu 1/3 Verletzung von Gl. 13;
   - a-konformer Modus (-K^2): reine Verletzung von Gl. 21.
   - Auf der eichfreien Zwangsflaeche bleiben die beiden Helizitaet-2-Richtungen mit A = J und B = g K^2.
   - Ausnahme: Auf dem endlichen Torus ist die homogene Mode E = e delta (q = 0) eine physikalische negative Richtung.
4. **Lineare Dynamik: keine exponentiell wachsenden Moden (N3 nicht eingetroffen), aber nur knapp [E, M].**
   - Physikalische Dynamik omega^2 = g J K^2 (Gl. 35).
   - Mit Gu/Wens Straftermen ist die Energie nach unten unbeschraenkt: Eine negative E-Richtung (Mischung aus
     Spur-Eichrichtung und Verletzung von Gl. 13) bleibt bei jedem q und jedem Strafgewicht. Trotzdem waechst nichts
     exponentiell.
   - Grund: Die negativen Richtungen sind an Eichrichtungen ohne Energie gekoppelt. Das gilt **nur bei genau 1/2** im
     Glied -1/2 (E^ii)^2. Schon lambda = 0,49 oder 0,51 gibt exponentielles Wachstum.
   - Was bleibt, ist polynomiales Wachstum (Jordankette der Laenge 4 statt 2 beim L-Typ). Verletzt man die
     Vektorbedingung, driftet die Massendichte R^ii linear in der Zeit.
5. **N4 (Pyrochlor) nicht gerechnet** [F5]: Die Quelle hat keine Fassung dafuer; die Zeitbox reichte nicht fuer eine
   eigene Modellbildung.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 00:01:30 CEST) durch code/tn_auswertung.py; alle Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| N0 | L-Typ stoesst gleiche Massen ab, Kraftexponent 4 +- 0,4 (nach Torus-Korrektur) | 70 % | **nicht eingetroffen** | Keine Wechselwirkung: max abs(U_inf) = 9,3e-17 fuer 2 <= r <= 16 (Schwelle 1e-12). Roh U(8,0,0) = -1,9073e-6 / -2,3842e-7 / -7,0643e-8 / -2,9802e-8 fuer L = 64/128/192/256, gleich -1/(2 L^3). c-Koeffizient der Anpassung -0,5000000 |
| N1 | N-Typ: stationaere Wechselwirkung gleicher Massen anziehend, Potential ~ 1/r (Exponent 1 +- 0,1) | 50 % | **eingetroffen** | U_inf < 0 ueberall (-0,02144 bis -0,00249); Kraft anziehend auf allen Strahlen; p = 1,011 / 0,999 / 0,995 / Schale 1,001. Minimum existiert (0 negative Tangentialeigenwerte, kleinster -7e-16 relativ) |
| N2 | N-Typ: Form indefinit, negative Richtungen ausserhalb der eichfreien Zwangsflaeche | 75 % | **eingetroffen** | An 100 % der q != 0: je ein negativer Eigenwert von A (-0,5) und B (-K^2). Auf ker Kv bzw. ker c: kleinster Eigenwert -3,9e-16 bzw. -6,8e-16 relativ; auf der eichfreien Flaeche A = 1,000, B/K^2 = 1,000. Vermerk: q = 0 [F6] |
| N3 | N-Typ: lineare Gitterdynamik hat wachsende (exponentielle) Moden | 55 % | **nicht eingetroffen** | P0 bis P6 und physikalisch: -Re(omega^2) <= 1,7e-8 und abs(Im(omega^2)) <= 1,7e-8 relativ (Schwelle 1e-6). Exakt an 12 rationalen Punkten fuer P0, P1, P3, P5: Null vierfach, alle uebrigen omega^2 reell und positiv (Beispielpunkt: x^4 (x - K^2)^2) |
| N4 | Pyrochlor: Vorzeichenregel gilt | 50 % | **nicht auswertbar** | nicht gerechnet [F5] |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "N0 und N1 treffen ein" ist nicht ausgeloest, nur N1.
  - "N2 und N3 treffen ein" ist nicht ausgeloest, nur N2.
  - "N1 verfehlt" ist nicht ausgeloest.
  - Die Lesart dazu steht in Abschnitt 7.
- **Agenten-Vorhersagen** (PLAN Abschnitt 4):

  | Nr | Ergebnis |
  |---|---|
  | A1 | Kern eingetroffen: abs(U_inf) <= 9e-17; c = -0,5. Teilaussage "roh gleich -1/(2 L^3) auf 1e-12 relativ" **verfehlt**: tatsaechlich 2,4e-11 (L = 64) bis 2,6e-11 (L = 256) |
  | A2 | eingetroffen: 1,98 % (r >= 4), 0,41 % (r >= 8) |
  | A3 | eingetroffen: 0,995 bis 1,011 |
  | A4 | eingetroffen: Gewichte A-negativ 0 / 0,6667 / 0,3333, B-negativ 0 / 0 / 1,0000 |
  | A5 | eingetroffen: A_phys = 1, B_phys/K^2 = 1, omega^2/K^2 = 1 (je auf 2e-15) |
  | A6 | eingetroffen, soweit geprueft: an allen Punkten Null vierfach und uebrige Wurzeln positiv (N) bzw. ebenso (L); ausgeschrieben am Beispiel K = (3/5, -8/7, 1), N: x^6 - (6532/1225) x^5 + (10666756/1500625) x^4 = x^4 (x - K^2)^2; L: x^4 (x - K^6)^2; Jordan 4 (N) und 2 (L) |
  | A7 | eingetroffen: mit U = 1 waechst jedes lambda != 0,50 exponentiell, 0,50 nicht |
  | A8 | eingetroffen in der geaenderten Fassung (PLAN, vor dem Einfrieren): A 1,3e-15, B 4,3e-14; vertauscht 2,4 bzw. 38 |
  | A9 | eingetroffen |

## 3. Tabellen

### 3.1 Statik N-Typ, torus-korrigiert (Anpassung L = 128/192/256) [E]

| v | r | U_inf | -1/(8 pi r) | U_inf 8 pi r + 1, Vorzeichen umgekehrt | roh L = 256 gegen U_inf | Anpassung 64/128/256 gegen 128/192/256 |
|---|---|---|---|---|---|---|
| (2,0,0) | 2 | -0,021445 | -0,019894 | +7,8 % | -2,1 % | < 1e-6 |
| (4,0,0) | 4 | -0,010144 | -0,009947 | +1,98 % | -4,3 % | < 1e-6 |
| (8,0,0) | 8 | -0,004994 | -0,004974 | +0,41 % | -8,8 % | 8e-6 |
| (16,0,0) | 16 | -0,002489 | -0,002487 | +0,10 % | -17,7 % | 2,7e-4 |
| (3,3,0) | 4,24 | -0,009357 | -0,009378 | -0,22 % | -4,7 % | < 1e-6 |
| (8,8,0) | 11,31 | -0,003515 | -0,003517 | -0,05 % | -12,5 % | 1,3e-5 |
| (11,11,0) | 15,56 | -0,002557 | -0,002558 | -0,03 % | -17,2 % | 6,3e-5 |
| (3,3,3) | 5,20 | -0,007610 | -0,007657 | -0,62 % | -5,8 % | 1e-6 |
| (6,6,6) | 10,39 | -0,003823 | -0,003829 | -0,16 % | -11,5 % | 2,0e-5 |
| (9,9,9) | 15,59 | -0,002551 | -0,002552 | -0,07 % | -17,2 % | 1,5e-4 |

- Positiv in Spalte 5 heisst: staerker gebunden als im Kontinuum. Laengs [100] liegt das Gitter darueber, laengs [111]
  darunter: Das ist die bekannte kubische Anisotropie der Gitter-Greenfunktion [L], sie faellt wie r^-2.
- Ohne Torus-Korrektur ist die Anziehung bei L = 256 und r = 16 um 18 % zu schwach; bei L = 64 sind es 67 %.
- Selbstglied G(0) laeuft gegen -(1/2) mal das Watson-Integral 0,2527 [L]: -0,12460 / -0,12548 / -0,12578 / -0,12592
  fuer L = 64/128/192/256.
- Bild: lauf-69/bild-wechselwirkung.png (links N, rechts L).

### 3.2 Statik L-Typ [E]

- kappa_L(q) = 1/2 fuer jedes q != 0, also U = (g/2)(delta_r0 - 1/N).
  - Ortsraum L = 6 (K2): U = -0,0023148 = -1/432 fuer (1,0,0), (2,0,0) und (3,0,0) gleich.
  - Torus-korrigiert: abs(U_inf) <= 9,3e-17.
- Minimum existiert (H_L >= 0). Der stationaere Wert ist das Minimum; es ist **lokal** (nur das Selbstglied g/4 je
  Masse).
- Lesart [M]:
  - Die Energie (g/2) R^2 ist von vierter Ordnung in den Ableitungen, die Bedingung R^ii = rho von zweiter. Der Kern
    k^4/k^4 ist deshalb konstant.
  - Beim N-Typ ist die Energie a R von zweiter Ordnung: Kern k^4/k^2 im Nenner, also 1/k^2, also 1/r.
  - Das Vorzeichen kommt von B in der durch die Masse festgelegten Richtung T: positiv beim L-Typ, negativ beim N-Typ.

### 3.3 Definitheit und Dynamik (BZ-Gitter L = 32, 32 767 Punkte q != 0) [E]

| Satz | U_v / U_s | Anteil q mit negativem Eigenwert A / B | max -Re(omega^2) rel. | max abs(Im(omega^2)) rel. | exponentiell wachsend |
|---|---|---|---|---|---|
| P0 (N) | 0 / 0 | 100 % / 100 % | 1,7e-8 | 1,7e-8 | nein |
| P1 (N, Gu/Wen U ~ J ~ g) | 1 / 1 | 100 % / 0,62 % | 7,6e-9 | 6,1e-9 | nein |
| P2 (N) | 0,1 / 0,1 | 100 % / 35,9 % | 1,1e-8 | 1,0e-8 | nein |
| P3 (N) | 10 / 10 | 100 % / 0,018 % | 2,8e-9 | 2,4e-9 | nein |
| P4 (N) | 100 / 100 | 100 % / 0 % (auf dem Gitter) | 1,3e-9 | 3,7e-10 | nein |
| P5 (N) | 1 / 0,01 | 100 % / 100 % | 9,2e-9 | 1,1e-8 | nein |
| P6 (N) | 0,01 / 1 | 100 % / 0,62 % | 1,3e-8 | 1,1e-8 | nein |
| L0 (L) | 0 / 0 | 0 / 0 | 4e-16 | 2e-16 | nein |
| L1 (L) | 1 / 1 | 0 / 0 | 1e-16 | 8e-17 | nein |

- "rel." heisst relativ zu |A| |B|. Die Restwerte um 1e-8 sind Rundung an Jordanbloecken (Groesse 2 in A B,
  Rundung ~ Wurzel aus eps).
  - In absoluten Wachstumsraten sehen sie bei grossen Straftermen nach etwas aus (bis 0,057 bei P4).
  - Die exakte Rechnung zeigt dort omega^2 = 0.
- **B mit Strafterm** ist negativ fuer K^2 < g/(2 U_s), also bei kleinem q. Bei P4 liegt das unter dem kleinsten
  Gitter-q (Anteil 0), nicht aber im unendlichen Gitter [M].
- **A mit Strafterm** ist an jedem q negativ, fuer jedes U_v: det des (T, L)-Blocks = -J^2/2 [M]. Die Gitterzaehlung
  (100 %) bestaetigt das.
- **Nullmoden je q:** vier (N, L), bei P3/P4 an wenigen q zwei. Das sind numerisch gerundete Werte nahe Null, die Kette
  bleibt (exakt: Rang von D^k = 9, 6, 5, 4, 4, ...).
- **Lambda-Abtastung** (beschreibend, Bild lauf-69/bild-spektrum.png rechts):

  | lambda | mit U = 1: groesste Rate, Anteil wachsender q | ohne Strafterme |
  |---|---|---|
  | 0,40 | 0,158; 0,6 % (kleines K) | 1,549; 100 % |
  | 0,45 | 0,111; 0,6 % | 1,095; 100 % |
  | 0,49 | 0,050; 0,6 % | 0,490; 100 % |
  | **0,50** | **0 (Rundung)** | **0** |
  | 0,51 | 2,35; 99,4 % | 0 |
  | 0,55 | 5,25; 99,4 % | 0 |
  | 0,60 | 7,43; 99,4 % | 0 |

  - Ohne Strafterme ist lambda > 1/2 linear stabil. Dann liegt aber eine negative Richtung auf der Zwangsflaeche: Die
    Energie ist dort negativ, und das System ist nur scheinbar ruhig. Ein Geist-Modus, Lesart [H].
  - Exakt bestaetigt: lambda = 0,45 und 0,55 mit U = 1 haben an rationalen Punkten negative omega^2.
- **Driftbeispiel** (q = (0,3; 0,2; 0,1), reine Verletzung der Vektorbedingung, Q_E = 0,0767 fest):

  | t | c.a (N, P0) | abs(a) (N, P0) | c.a (L, L0) | abs(a) (L, L0) |
  |---|---|---|---|---|
  | 0 | 0 | 0 | 0 | 0 |
  | 10 | 0,139 | 3,12 | -4e-18 | 0,190 |
  | 50 | 0,696 | 148 | -2e-17 | 0,950 |

  - N-Typ: Die Skalarbedingung (Massendichte) waechst linear. abs(a) waechst polynomial; die lokale Steigung in
    log-log ist 1,9 zwischen t = 10 und 20 und 2,8 zwischen 20 und 50, also gegen t^3 (Kettenlaenge 4).
  - L-Typ: c.a bleibt null, abs(a) waechst linear (reine Eichdrift).

## 4. Kontrollen

- **K1, Operatoridentitaeten** (L = 32, alle q):
  - d_i R^ij = 0: 5e-15;
  - inc G15 und c G15: 1e-14;
  - Kv G23 ([S, V] = 0, S. 14): 7e-15;
  - C G23: 4e-15;
  - c + G23: 2e-15;
  - inc symmetrisch: 0;
  - Raenge 3 und 3;
  - Physikalische Raeume der E- und der a-Seite gleich (kleinster Kosinus 1 - 1e-15).
- **K2, Ortsraum L = 6** (Stencils per np.roll, Lagen per assert geprueft):
  - statisch N 1,5e-16, L 2,7e-15 gegen den Fourierweg;
  - Zwangsresiduen <= 9e-15;
  - Spektrum A B: P0 4,9e-8, P1 1,2e-6 absolut bei max omega^2 = 12 (Schwelle 1e-6 relativ: erfuellt).
- **K3, Gu/Wen S. 19** (200 zufaellige q, k = q + (pi, pi, pi)):
  - A = 2 D^-1 X D^-1 auf 1,3e-15, B = 2 D Y D auf 4,3e-14 mit s = (1, 1, 1) und strukturgleicher Zuordnung
    (phi-Strafterm = Vektorbedingung).
  - Vertauschte Zuordnung: 2,4 bzw. 38.
  - Der Nachbau ist also genau Gu/Wens quadratisches N-Gittermodell, und die Beschriftung U1/U2 auf S. 19 ist gegenueber
    Gl. 39/62 vertauscht [S + E].
  - Signaturen A/X (5, 0, 1), B/Y (2, 3, 1).
- **K4, Dispersion:**
  - N physikalisch omega^2/K^2 = 1 (Gl. 35);
  - L exakt x^4 (x - K^6)^2 (Gl. 30).
- **K5, Statik:**
  - Zwangsresiduum <= 2e-15 (N), <= 5e-14 (L);
  - kappa gegen kappa' (Formel ohne KKT, L = 64): 3e-15 (N), 7e-14 (L);
  - Spiegel- und Vertauschungssymmetrie <= 6e-17;
  - Mittelwert von G null (<= 4e-21).
- **K6, Torus:** Abstand der Anpassungen 64/128/256 gegen 128/192/256 hoechstens 2,7e-4 relativ (N, r = 16).
- **Latten:**
  - L1 (kann scheitern): Alle Ausgaenge waren vorab ableitbar [M, PLAN Abschnitt 3]. Scheitern konnte nur die
    Rekonstruktion oder der Schreibtisch. Echte Tests dafuer waren K2, K3 und die exakte Rechnung.
  - L2 (Gegenprobe): Ortsraum gegen Fourier, KKT gegen B^+, Gleitkomma gegen exakt, zwei Torus-Anpassungen.
  - L3 (Numerik): 1e-15 bis 1e-14; Torus 2,7e-4.
  - L4 (schon bekannt): N-Anziehung bei Gu/Wen [S] und in der linearisierten ART [L]; das negative Vorzeichen des
    konformen Modus [L].
    - Neu: Der L-Typ hat statisch keine Wechselwirkung, gegen Gu/Wen S. 11.
    - Neu: Die lineare Stabilitaet des N-Gitters haengt an der exakten 1/2.
  - L5 (Messbezug): keiner.

## 5. Selbstanzeigen

1. **Vorab ableitbar:**
   - Die Urteile N0 bis N3 standen als Erwartung im Plan (Abschnitt 3), mit Zahlen (Abschnitt 4).
   - Die Rechnung prueft die Rekonstruktion und die Herleitung; sie entdeckt nichts, was der Schreibtisch nicht sagt.
2. **Gu/Wens r^-4 beim L-Typ:**
   - Ich habe die naechstliegende eindeutige Fassung gerechnet: statischer stationaerer Wert unter exakten Bedingungen
     [F2].
   - Gu/Wen geben keine Herleitung. Es ist moeglich, dass sie mit "force" etwas anderes meinen, etwa das r^-3-Feld
     R^ij ~ d_i d_j (1/r) einer Einzelmasse multipliziert mit der zweiten Masse [H], oder eine Quantenkorrektur [L?].
   - Fuer eine klassische statische Kraft ist das Ergebnis eindeutig null.
   - Dossier V4 und Karte uebernehmen "L stoesst ab (~ r^-4)" [S] als Zitat einer unbelegten Angabe.
3. **Rauchlaeufe** (offengelegt in PLAN Abschnitt 8):
   - rauch1: Importfehler.
   - rauch2: gesehen habe ich G(0) und Zwangsresiduen, keine U(r).
   - rauch3: Startfehler durch `cd ... && ... &`. Die cpu6-Kette lief im Heimatordner ohne Rechnung an; derselbe Fehler
     wie bei LAST-1. Danach richtig gestartet. Kontrollen K2/K3 per jq gelesen, sonst nur rc und Dateinamen.
   - rauch4: nur der neue Matrixvergleich.
4. **Aenderung nach rauch3, vor dem Einfrieren:**
   - Neu ist der direkte Matrixvergleich in K3, mit neuer Fassung von A8. Grund: Der urspruengliche Eigenwertvergleich
     haengt nicht von U_v, U_s ab und ist durch Jordan-Rundung begrenzt (1e-7 statt 1e-10).
   - Das ist eine Kontrolle; keine Urteilsschwelle wurde geaendert.
5. **A1 teilweise verfehlt:** Die Teilaussage "roh = -1/(2 L^3) auf 1e-12" stimmt nur auf 2,6e-11 (Rundung der
   L-Typ-KKT-Loesung, Residuen bis 5e-14). Fuer N0 ohne Belang.
6. **Festlegungen mit Gewicht:**
   - [F6] q = 0 (homogene Torusmode, E = e delta, physikalisch negativ) zaehlt fuer N2 nicht. Wer sie mitzaehlt, muss
     den Klammerteil von N2 als verfehlt lesen.
   - [F7] Nur exponentielles Wachstum zaehlt fuer N3. Unter der Lesung "jede unbeschraenkte Loesung" waere N3
     eingetroffen: Jordankette 4, Massendichte driftet bei verletzter Vektorbedingung. Dann waeren aber auch der L-Typ
     (Kette 2) und Maxwell in Zeiteichung [L] "instabil".
   - [F1] Unversetzte Gittervariablen; durch K3 als gleichwertig zu Gu/Wens versetzten Variablen bestaetigt.
7. **Nicht gerechnet:**
   - Statik des Strafterm-Modells (dort gibt es kein Minimum; der stationaere Wert je q, (U_s/2) g/(g - 2 U_s K^2)
     |rho|^2, hat einen Pol bei K^2 = g/(2 U_s)) [M], nur Schreibtisch;
   - N4;
   - Nichtlineare und Quanteneffekte (Gu/Wens Grund fuer "not reliable").
8. **Quelle:** Ein gezielter Abruf (PDF). Die WebFetch-Zusammenfassung war leer; gelesen habe ich die gespeicherte PDF
   mit dem Read-Werkzeug, S. 1-3 und 9-24. Nicht gelesen: S. 4-8 und die Literaturliste.
9. **Zeitbox:** Start 23:24:33, Text ab 00:10:20 CEST, innerhalb von 150 min.

## 6. Bedeutung fuer das Dossier und die Vorzeichenregel [M, H]

- **Vorzeichenregel verfeinert [M]:** Wird eine Quelle als Zwangsbedingung c.a = rho auf ein Feld mit Energie 1/2 a.B.a
  gesetzt, ist die statische Energie 1/2 rho^2/(c B^-1 c).
  - Das Vorzeichen bestimmt B in der von der Quelle festgelegten Richtung.
  - Die Reichweite bestimmt der Unterschied der Ableitungsordnungen:
    - Maxwell 2 - 0: Coulomb;
    - N-Typ 4 - 2: Newton;
    - L-Typ 4 - 4: Kontakt.
  - "Positiv definit gibt Abstossung" (Dossier V4, Gegenleser 3.2) gilt nur, wenn die Energie weniger Ableitungen hat
    als die Bedingung im Quadrat.
- **Dossier V4 berichtigen:** Statt "L stoesst ab (~ r^-4), N zieht an" gilt nach Nachbau: "L ohne statische
  Fernwirkung, N zieht an wie -m1 m2/(8 pi r)". Die Angabe r^-4 bleibt Zitat ohne Herleitung.
- **Zur Kartenfrage Q3 (beschraenkt?):**
  - Mit exakten Zwangsbedingungen ist der N-Typ auf dem Gitter stabil und nach unten beschraenkt (bis auf die homogene
    Torusmode).
  - Mit Straftermen (Gu/Wens Gittermodell, quadratisch) ist er nach unten unbeschraenkt, aber linear nicht exponentiell
    instabil, und nur dank der exakten 1/2.
  - Nichtlinear koennte Energie in die unbeschraenkten Richtungen fliessen [H]. Das passt zu Gu/Wens "not reliable".
- **Fuer Finns Netz [H]:**
  - Die gesuchte Zutat ist nicht nur ein Minuszeichen. Es braucht drei Dinge:
    1. eine zweite, **strenge** Regel je Knoten (skalar), deren Verletzung die Masse ist und die den konformen Modus
       festlegt;
    2. ein Spurglied mit **genau** abgestimmtem Gewicht (Eichsymmetrie Gl. 23);
    3. eine strenge Vektorregel, sonst driftet die Masse.
  - Weiche Regeln (Energiestrafen) reichen nicht: Die negative E-Richtung bleibt bei jeder Strafstaerke.
  - Die Masse bleibt eine Defektladung mit Vorzeichen (ungleiche stossen sich ab, Gu/Wen S. 12 [S]), nicht die Energie.
    Universalitaet ist damit nicht gezeigt (Dossier Q5).

## 7. Einfach gesagt

Wir haben zwei Netzmodelle von Gu und Wen nachgerechnet, in denen eine "Masse" eine Stelle ist, an der eine Netzregel
verletzt wird. Im ersten Modell, in dem alle Energien positiv sind, spueren sich zwei solche Massen ueber das Netz gar
nicht, anders als die Autoren schreiben, die eine Abstossung angeben. Im zweiten Modell hat ein Energieglied ein
"falsches" Minuszeichen, und dann ziehen sich gleiche Massen genau wie bei Newton mit 1/r an. Das Minuszeichen macht
das Netz nicht kaputt, solange die Netzregeln streng gelten: Die gefaehrliche Richtung ist genau die, die von der Masse
festgelegt wird, so wie in Einsteins Theorie. Fuer Finns Netz heisst das: Schwerkraft braucht eine zweite, strenge
Regel an jedem Knoten und ein genau abgestimmtes Minus-Glied; schon kleine Abweichungen davon machen das Netz instabil.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-000130
- code/:
  - tn.py: Rechnung (Statik, Spektrum, Kontrollen);
  - tn_auswertung.py: Urteile und Bilder;
  - beide mit eingefrorenen Kopien;
  - pruefsummen-einfrieren.txt.
- lauf-69/:
  - auswertung.json (Urteile, Tabellen, Kontrollen);
  - statik-64/-128-192/-256 (.json/.npz, Oktant-Wuerfel U je L);
  - spektrum.json, kontrolle.json, Logs;
  - Bilder bild-wechselwirkung.png und bild-spektrum.png.
- rauch-69/: rauch1/rauch2, r3 (Kette kleiner Groessen), r4 (Matrixvergleich).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde36-tensorn/ (code/, rauch/, lauf/).
- Quelle: PDF arXiv:0907.1203v3, lokal nur im Werkzeugspeicher der Sitzung (nicht ins Projekt kopiert).
