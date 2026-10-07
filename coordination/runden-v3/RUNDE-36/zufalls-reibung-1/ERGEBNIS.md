# ZUFALLS-REIBUNG-1: Ergebnis (Code-Agent fuer die Leitung, Runde 36, explorativ)

- Gerechnet auf der .69 ueber kleintest.sh, nur Spuren cpu und cpu6, hoechstens zwei Laeufe zugleich.
- **Ablauf** (Zeiten per date; .69 in UTC, CEST = UTC + 2):
  - Start 01:03:19 CEST.
  - Rauch 1: 23:23:07 bis 23:23:20 UTC. Rauch 2: 23:26:13 bis 23:27:35 UTC. Rauch 3: 23:29:58 bis 23:33:10 UTC.
  - Plan ab 01:30:09 CEST. Eingefroren 01:34:41 CEST: PLAN.md.eingefroren-20261004-013441,
    code/*.eingefroren-20261004-013441, sha256 in code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe und Proben 23:34:48 bis 23:45:51 UTC: 40 Laeufe, alle rc = 0 und Status "fertig".
  - Auswertung 23:50:13 bis 23:50:20 UTC. Beschreibung (nach dem Einfrieren, Selbstanzeige 9) 23:51:32 bis 23:51:34 UTC.
  - Text ab 01:52:29 CEST.
- **Hashes:**
  - Alle Laeufe tragen die sha256 des eingefrorenen reibung.py (d573dac1...), die Auswertung die von auswertung.py
    (e31ac1bd...).
  - Plan und Code wurden nach dem Einfrieren nicht geaendert.
- **Daten:**
  - lauf-69/: je Lauf .json (Kopf), .npz (Zeitreihen), .log
  - lauf-69/auswertung.json: Urteile, Zellen, Proben, Gegenproben
  - lauf-69/beschreibung.json: Teilfenster, nur beschreibend
  - Bilder: lauf-69/v_t.png, vc_t.png, ladung_t.png, reibung_sigma_v.png
  - rauch-69/: Rauchlaeufe; rauch-69/aw3/ ist die Probe des Auswertepfads
- Kennzeichen:
  - [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese
  - [E] hier gerechnet (synthetisch, keine Messdatenbestaetigung), [F] von mir vor dem Einfrieren festgelegt

## 1. Ergebnis

1. **Das ungeordnete Netz bremst den Ball, etwa mit dem Quadrat der Unordnung [E].**
   - Ohne Unordnung haelt der Ball seine Schnelle auf 3e-6.
   - Mit Unordnung strahlt er Ladung ab und wird langsamer. Die Reibungsrate (Hauptmass r_B) waechst mit sigma^p:
     - p = 2,03 bei v = 0,2 und 1,85 bei v = 0,5
     - p = 2,31 bei v = 0,3 (Z1-Zelle). Dort knapp ausserhalb von 2 +- 0,3, mit Saat C 2,22.
   - Die Abweichung bei v = 0,3 kommt aus sigma = 0,04: Dort faellt der Ball im Messfenster von 0,28 auf 0,22, und die
     Rate steigt mit fallender Schnelle.
2. **Die v-Abhaengigkeit hat keine Schwelle nach oben, sondern einen Gipfel bei v ~ 0,2 [E].**

   | v | r_B bei sigma = 0,01 | r_B bei sigma = 0,04 |
   |---|---|---|
   | 0,1 | 1,6e-6 | Ball gefangen |
   | 0,2 | 2,0e-5 | 3,3e-4 |
   | 0,3 | 1,1e-5 | 2,6e-4 |
   | 0,5 | 2,9e-6 | 3,8e-5 |

   - Schnelle Baelle verlieren zwar viel Ladung, behalten aber ihre Schnelle besser.
3. **Langsame Baelle gleiten nicht, sie bleiben haengen [E].**
   - Bei v = 0,1 und sigma = 0,04 kehrt der Ball in allen drei Saaten um und pendelt zwischen Bergen der
     Landschaftsenergie (Schnelle zwischen -0,13 und +0,13).
   - Bei sigma = 0,02 kehrt er in Saat A um.
   - Damit ist Z2 nach der Regel "gefangen" nicht auswertbar.
4. **Ladungs- und Impulsverlust haengen fest zusammen (Z3 eingetroffen) [E].**
   - dQ/dP liegt zwischen 0,60 und 1,37 (Faktor 2,26). Es haengt kaum von sigma ab (je v hoechstens 14 %), aber von v.
   - Das folgt der vorab notierten Ballbild-Formel dP/dQ = gamma (v omega + |p|) (PLAN Abschnitt 7) in Groesse und Gang.
5. **Urteile:** Z0 nicht eingetroffen, Z1 nicht eingetroffen (nicht robust), Z2 nicht auswertbar, Z3 eingetroffen.
   - Z0 scheitert nur an der Ladung bei v = 0,5 (2,9e-8 gegen 1e-8). Vermutlich ist das Restabstrahlung meines
     Boost-Starts [H]; Rauch 3 hatte es angezeigt, im Plan offengelegt.
   - Die Schnelle haelt bei allen v auf <= 2,7e-6.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 01:34:41 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| Z0 | sigma = 0: Schnelle relativ < 1e-4, Ladungsverlust < 1e-8 | 90 % | **nicht eingetroffen** (robust) | Schnelle 1,3e-6 / 1,7e-6 / 2,2e-6 / 2,7e-6; Ladungsverlust 1,4e-9 / 3,4e-9 / 6,4e-10 / **2,88e-8** (v = 0,1 / 0,2 / 0,3 / 0,5) |
| Z1 | v = 0,3: Reibung ~ sigma^p, p = 2 +- 0,3 | 65 % | **nicht eingetroffen** (nicht robust) | r_B = 1,07e-5 / 4,65e-5 / 2,62e-4; p = 2,307 (Fehler 0,04); Paare 2,12 und 2,49; Saat C statt B: p = 2,220 |
| Z2 | sigma = 0,04: r(0,5) >= 10 r(0,1) | 55 % | **nicht auswertbar** (robust) | v = 0,1 gefangen (Saat A, B und C); r(0,5) = 3,75e-5 +- 0,06e-5 |
| Z3 | dQ/dP ueber v und sigma innerhalb Faktor 3 konstant | 40 % | **eingetroffen** (robust) | 10 Zellen, dQ/dP = 0,60 bis 1,37, max/min = 2,26 (dt/2: 2,26; Saat C: 2,27) |

- **Bedeutung, wie vorab festgelegt:**
  - "Z1 und Z2 treffen ein" ist nicht ausgeloest.
  - "Z2 verfehlt (Reibung kaum von v abhaengig)" ist formal ebenfalls nicht ausgeloest, Z2 ist nicht auswertbar.
- **Beschreibend:**
  - Langsame Materie spuert die Unordnung sehr wohl. Bei sigma = 0,04 wird sie gefangen; bei sigma = 0,01 ist
    r(0,5)/r(0,1) = 1,75, also keine Zehnfach-Stufe.
  - Der Kartensatz "Auch langsame Materie spuert die Unordnung" beschreibt die Rechnung besser als "erst bei hoher
    Geschwindigkeit merklich". Ausgeloest ist er nach den Regeln nicht.
  - Zum Ruhesystem des Netzes [H]: Die Reibung ist fuer jede Schnelle > 0 messbar (ausser beim Fangen). Ein
    ungeordnetes, zeitlich festes Netz waere also ueber Reibung als Ruhesystem erkennbar.

## 3. Tabellen

### 3.1 Zellen (Saatmittel A, B; Messfenster [400, 1400]; Raten je Zeiteinheit)

- Messgrenze G = max(sigma = 0-Rauschen, 2 SE). Das sigma = 0-Rauschen von r_B ist <= 5e-10, die Grenze kommt also
  ueberall aus 2 SE.
- r_B: Hauptmass, ln(gamma_c v_c) mit gamma_c = gamma(v) + V/M(Q).
- r_A: Karte woertlich, ln(gamma v) aus v(t).
- r_C: aus E und Q.

| v | sigma | r_B (SE) | Saaten A / B | r_A (SE) | r_C | r_Q/Q0 | r_P | dQ/dP | v im Fenster (A / B) | Ladung verloren im Fenster |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,1 | 0,01 | 1,64e-6 (4,1e-7) | 2,4e-6 / 0,9e-6 | unter Grenze (2,6e-5 +- 4,0e-5) | 1,9e-6 | 9,1e-8 | 3,7e-7 | 0,60 | 0,093 / 0,093 | 0,01 % |
| 0,1 | 0,02 | gefangen (A) | 6,7e-6 / 4,1e-6 | gefangen | gefangen | - | - | - | 0,055 / 0,084 | 0,04 / 0,03 % |
| 0,1 | 0,04 | gefangen (A, B) | - | gefangen | gefangen | - | - | - | 0,002 / 0,005 | 0,19 / 0,28 % |
| 0,2 | 0,01 | 1,99e-5 (6,0e-7) | 2,3e-5 / 1,6e-5 | 1,6e-5 (7,5e-6) | 1,8e-5 | 4,1e-6 | 1,08e-5 | 0,93 | 0,197 / 0,195 | 0,48 / 0,35 % |
| 0,2 | 0,02 | 8,06e-5 (2,9e-6) | 9,3e-5 / 6,8e-5 | 7,0e-5 (1,7e-5) | 8,0e-5 | 1,63e-5 | 4,10e-5 | 0,97 | 0,188 / 0,184 | 1,9 / 1,4 % |
| 0,2 | 0,04 | 3,32e-4 (1,4e-5) | 3,7e-4 / 3,0e-4 | 4,2e-4 (9,5e-5) | 3,1e-4 | 4,48e-5 | 1,28e-4 | 0,85 | 0,148 / 0,146 | 5,2 / 3,7 % |
| 0,3 | 0,01 | 1,07e-5 (5,6e-7) | 1,02e-5 / 1,12e-5 | unter Grenze (6,3e-6 +- 3,2e-6) | 1,1e-5 | 6,2e-6 | 1,15e-5 | 1,31 | 0,297 / 0,297 | 0,58 / 0,66 % |
| 0,3 | 0,02 | 4,65e-5 (1,9e-6) | 4,40e-5 / 4,91e-5 | 3,7e-5 (6,5e-6) | 4,8e-5 | 2,49e-5 | 4,70e-5 | 1,30 | 0,289 / 0,287 | 2,4 / 2,6 % |
| 0,3 | 0,04 | 2,62e-4 (7,5e-6) | 2,40e-4 / 2,84e-4 | 2,2e-4 (1,8e-5) | 2,5e-4 | 1,03e-4 | 1,99e-4 | 1,26 | 0,255 / 0,246 | 9,7 / 10,9 % |
| 0,5 | 0,01 | 2,88e-6 (1,4e-7) | 2,6e-6 / 3,1e-6 | 4,3e-6 (5,6e-7) | 2,4e-6 | 4,9e-6 | 9,5e-6 | 1,25 | 0,499 / 0,499 | 0,48 / 0,50 % |
| 0,5 | 0,02 | 1,04e-5 (3,1e-7) | 9,6e-6 / 1,12e-5 | 1,3e-5 (1,1e-6) | 9,5e-6 | 1,93e-5 | 3,62e-5 | 1,30 | 0,497 / 0,496 | 1,9 / 2,0 % |
| 0,5 | 0,04 | 3,75e-5 (6,2e-7) | 3,4e-5 / 4,1e-5 | 4,3e-5 (2,0e-6) | 3,6e-5 | 7,34e-5 | 1,31e-4 | 1,37 | 0,489 / 0,488 | 7,1 / 7,5 % |

- **Potenz in sigma je v** (drei Punkte; bei gleichen Abstaenden in ln sigma ist die Ausgleichssteigung
  (ln r_3 - ln r_1)/ln 4):
  - v = 0,2: 2,03; v = 0,3: 2,31; v = 0,5: 1,85
  - Teilfenster (beschreibung.json): [400, 900] gibt 2,08 / 2,20 / 1,89, [900, 1400] gibt 1,94 / 2,34 / 1,85.
  - Nur bei v = 0,3 steigt die Potenz von Paar zu Paar (2,08 auf 2,32 bzw. 2,09 auf 2,60). Dort bremst sigma = 0,04 den
    Ball am staerksten ab (Schnelle 0,28 auf 0,22), und die Rate ist bei v = 0,2 hoeher als bei 0,3.
- **Saatstreuung:** Saat C bei v = 0,3 gibt 1,38e-5 / 5,88e-5 / 2,81e-4, gegen das Saatmittel A/B +29 / +26 / +7 %.
  Die blockrobusten Fehler (5 %) unterschaetzen also die Streuung zwischen Landschaften (Selbstanzeige 5).

### 3.2 Gefangene Baelle (v = 0,1)

- **sigma = 0,04:**
  - Saat A und B kehren vor t = 400 um.
  - Saat C kehrt im Fenster um; die mittlere Schnelle dort ist -0,10, er laeuft also ueberwiegend rueckwaerts.
  - Alle drei pendeln zwischen zwei Bergen der Landschaft (v_t.png, Feld oben links).
  - Mit der Kontinuums-Abschaetzung (PLAN Abschnitt 7, [M]):
    - Streuung der Landschaftsenergie 0,19 sigma = 7,6e-3
    - Bewegungsenergie (gamma - 1) M = 0,0116
    - Ein Berg von 1,5 Standardabweichungen reicht zum Umkehren.
- **sigma = 0,02:** Saat A kehrt bei t ~ 1250 um, Saat B nicht (mittlere Schnelle 0,084).
- **Auch gefangen verliert der Ball Ladung:** r_Q/Q0 = 1,6e-6 bis 2,8e-6 bei sigma = 0,04. Das ist mehr als frei bei
  sigma = 0,01, weniger als bei v >= 0,2.

### 3.3 Ladung gegen Impuls (Z3) und das Ballbild [M, H]

| v | dQ/dP gemessen (sigma = 0,01 / 0,02 / 0,04) | Ballbild vorab (PLAN 7): dP/dQ -> dQ/dP |
|---|---|---|
| 0,1 | 0,60 / - / - | 1,7 -> 0,6 |
| 0,2 | 0,93 / 0,97 / 0,85 | 1,0 -> 1,0 |
| 0,3 | 1,31 / 1,30 / 1,26 | 0,8 -> 1,25 |
| 0,5 | 1,25 / 1,30 / 1,37 | 0,7 -> 1,4 |

- Die Ballbild-Zahlen stehen in PLAN Abschnitt 7 (Schreibtisch, vor den Hauptlaeufen; aus Rauch 2 kannte ich 1,16 bis
  1,39 bei v = 0,3 und 0,5).
- Lesart [H]:
  - Je abgestrahlter Ladung braucht der Ball bei fester Schnelle die Energie gamma omega, abgegeben wird W >= 1.
  - Die Differenz zahlt die Bewegung. Deshalb ist dQ/dP fast unabhaengig von sigma und faellt bei kleinem v.
- Der Feldimpuls P_win (unbereinigt, auswertung.json rPw) gibt bei sigma = 0,04 und v >= 0,3 dieselben Verlustraten auf
  <= 6 %, sonst bis 40 %; bei v = 0,1 ist er von der Landschaft ueberdeckt.

### 3.4 Abstrahlung gegen die grobe Bornsche Schaetzung (PLAN Abschnitt 7)

- **Ladungsverlust bei sigma = 0,04:** Bei v = 0,5 ist r_Q = 1,79e-4 je Zeit, meine Nebenrechnung ~2,3e-4 ([M, grob];
  vor den Hauptlaeufen gerechnet, im Plan nur als Reibungsraten und Unterdrueckung notiert).
  - Bei v = 0,1 (sigma = 0,01) sind es 2,2e-7 gemessen gegen ~1e-8 geschaetzt, also 20-mal mehr. Die Schwelle der
    Schaetzung ist dort zu streng [H: weitere Kanaele, etwa innere Moden des Balls oder Gitter-Ballform statt
    sech-Naeherung; nicht geprueft].
- **Reibungsraten bei sigma = 0,04:** geschaetzt 3e-5 (0,2), 5e-5 (0,3), 3e-5 (0,5), gemessen 3,3e-4, 2,6e-4, 3,8e-5.
  - Bei v = 0,5 stimmt die Schaetzung, bei 0,3 und 0,2 liegt die Rechnung 5- bzw. 11-mal hoeher.
  - Den Gipfel bei v ~ 0,2 hatte die Schaetzung nicht.

## 4. Kontrollen

- **Z0-Pfad (sigma = 0, Fenster [400, 1400]):**
  - Schnelle konstant auf <= 2,7e-6 relativ.
  - Ladungsverlust 1,4e-9 / 3,4e-9 / 6,4e-10 / 2,9e-8.
  - Mit dt = 0,01 identisch auf 4 Stellen (2,8825e-8 gegen 2,8826e-8): kein Zeitschritteffekt.
  - Der Verlust bei v = 0,5 ist vermutlich die langsam mitlaufende Restabstrahlung des Boost-Starts [H].
    - Startenergie E_win/(gamma M0) - 1 = -8e-5 bei v = 0,5 und -1,7e-6 bei v = 0,1.
    - Rauch 1 zeigte das Einschwingen bis t ~ 300 (5e-7 Q0 insgesamt).
- **sigma = 0-Rauschen der Raten:** r_B <= 5e-10, r_Q <= 7,5e-11 (Q-Einheiten je Zeit). Das ist 3 bis 4
  Groessenordnungen unter allen Raten bei sigma > 0.
- **Bilanzen** (ganzer Lauf, mit Einschaltarbeit und Schwamm):
  - Energie <= 1,1e-9 M0 (dt = 0,02), <= 4,8e-11 (dt = 0,01)
  - Ladung <= 4,6e-14 Q0
- **Unordnung:** min(1 + sigma eta) = 0,839 / 0,839 / 0,856 bei sigma = 0,04 (Saat A / B / C); die Massenluecke bleibt
  > 0.
- **dt-Probe (7 Laeufe):** Alle Raten bei sigma > 0 aendern sich um <= 1e-6 relativ, z. B. r_B(0,3; 0,04; A) =
  2,404675e-4 gegen 2,404676e-4. Urteile gleich.
- **Saat-Probe (Saat C statt B):** Z0, Z2, Z3 gleich; Z1 kippt zu "eingetroffen" (p = 2,220). Daher "nicht robust".
- **Gegenproben:**
  - r_A (Karte woertlich) hat 2- bis 100-mal groessere Fehler als r_B (am groessten bei v = 0,1).
    - Abweichung von r_B in Fehlern von r_A: v = 0,2 innerhalb 1, v = 0,3 bei -1,4 bis -2,2 (r_A 15 bis 40 % tiefer).
    - Bei v = 0,5 liegt r_A in allen drei Zellen um +2,5 Fehler hoeher (15 bis 50 %).
    - Vermutung [H]: Das ist der geschwindigkeitsabhaengige Landschaftsrest ~ gamma^3 v^2 (PLAN 4.2), den r_B nicht
      bereinigt. Die Bereinigung ist dort also unvollstaendig, in welche Richtung sie r_B verschiebt, ist nicht
      geprueft.
    - Z1 waere mit r_A nicht auswertbar (sigma = 0,01 unter der Messgrenze), Z3 eingetroffen. Gipfel bei v ~ 0,2 und
      Fangen zeigen sich auch in r_A.
  - r_C (aus E und Q) liegt in allen gemessenen Zellen innerhalb 20 % von r_B. Damit waere Z1 eingetroffen (p = 2,23),
    Z3 ebenfalls.
- **Familie M(Q):** alle Q_win lagen im Bereich der Familie (omega^2 = 0,66 bis 0,94); Newton-Reste <= 4e-14.
- **Latten (v3):**
  - L1 kann scheitern: ja. Z0 und Z1 sind gescheitert, Z1 knapp und nicht robust. Z2 blieb wegen der Fangregel offen. Z3
    haette scheitern koennen (Faktor 3).
  - L2 Gegenprobe:
    - halber Zeitschritt, dritte Saat
    - woertliche Kartengroesse r_A und Energiegroesse r_C
    - Feldimpuls neben P_c
  - L3 Numerik: Bilanzen, dt/2 auf 1e-6, sigma = 0-Kontrolle.
  - L4 schon bekannt:
    - Solitonen in ungeordneten Medien strahlen ab, werden gebremst oder gefangen; Uebersicht Gredeskul/Kivshar,
      Physics Reports um 1992 [L?].
    - Fuer die NLS gibt es Rechnungen zur Abstrahlung eines Solitons an zufaelligen Stoerungen (Garnier, Bronski, spaete
      1990er) [L?].
    - Impulsdiffusion ("swerves") in Kausalmengen: Dowker/Henson/Sorkin 2004 [L].
    - Neu ist hier nur die Zahl fuer M1 und die Form der v-Abhaengigkeit mit Gipfel und Fangen.
  - L5 Messbezug: keiner aus eigener Rechnung (synthetisch, 1D, ein omega).

## 5. Selbstanzeigen

1. **Rauch 1, Z0-Werte gesehen, Messbeginn und Fenster danach gewaehlt** (PLAN Abschnitt 8):
   - Mit T_A = 250 und R1/R2 = 10/16 lag der Ladungsverlust bei 6,5e-8 (v = 0,5) und 1,5e-8 (v = 0,1).
   - Danach T_A = 400 und R1/R2 = 14/20. Die Schwellen 1e-4 und 1e-8 blieben.
   - Der breitere Rand verschob den Restverlust bei v = 0,5 nur in die Messzeit (Rauch 3: 1,3e-8, Hauptlauf 2,9e-8).
     Mit R2 = 16 war Q_win ab t = 300 auf 1e-11 gleich.
   - Ich habe nach Rauch 3 bewusst nicht ein zweites Mal verschoben. Z0 scheitert damit an meiner Festlegung; ein
     schmaleres Fenster haette vermutlich bestanden [H].
2. **Rauch 2, Z1-, Z2- und Z3-nahe Werte gesehen** (Saat 1, Fenster [400, 1800]):
   - p = 2,25 (Zweipunkt), v = 0,1 gefangen, dQ/dP = 1,16 bis 1,39.
   - Danach festgelegt:
     - Messfenster [400, 1400]
     - Regel "gefangen"
     - Hauptmass r_B statt r_A
     - Bloecke 100 statt 200
   - Die Regel "gefangen" macht Z2 "nicht auswertbar" statt "nicht eingetroffen". Ohne sie gaebe r_B bei v = 0,1 einen
     Wert aus der Landschaft (Rauch: 1,25e-4, Teilfenster 3,5e-5 bis 2,7e-4), nicht aus Reibung.
3. **Hauptmass r_B ist nicht die woertliche Kartengroesse.**
   - Es bereinigt gamma um die umkehrbare Landschaftsenergie V/M (Energiesatz erster Ordnung).
   - Mit der woertlichen Groesse r_A waere Z1 nicht auswertbar (sigma = 0,01 unter der Messgrenze), mit r_C eingetroffen.
4. **Z1 liegt auf der Kante.**
   - p = 2,307 gegen die Grenze 2,3. Die Saatstreuung (C statt B: 2,220) ist groesser als der Abstand zur Grenze.
   - Die Potenz bei v = 0,3 ist durch das Abbremsen bei sigma = 0,04 nach oben verschoben; bei v = 0,2 und 0,5, wo die
     Schnelle weniger faellt bzw. die Rate flacher in v ist, liegt sie bei 2,03 und 1,85. Das ist beschreibend, nicht
     Teil der Regel.
5. **Fehlerbalken:**
   - Der blockrobuste Fehler (zehn Bloecke) unterschaetzt die Streuung zwischen Landschaften: Saat C weicht bei v = 0,3
     um bis zu 30 % ab, der Fehler sagt 5 %.
   - Bei v = 0,1 ist die Korrelationszeit (~60) zudem mit der Blocklaenge (100) vergleichbar.
   - Die Messgrenzen sind also eher zu eng. Fuer die Urteile zaehlt das bei Z1 (Kante), nicht bei Z0, Z2 oder Z3.
6. **Einschalten in der Zeit:**
   - Der Ball bekommt beim Einschalten eine zufaellige Energie (Arbeit W = -7e-3 bis +2e-3). Er reibt sich ausserdem
     schon vor T_A.
   - Seine Schnelle bei T_A weicht deshalb von v0 ab (z. B. 0,279 statt 0,3 bei sigma = 0,04). Die Tabellen nennen die
     Schnelle im Fenster.
7. **Gemeinsame Zufallszahlen:** Alle sigma und v einer Saat sehen dieselbe Landschaft. Zellen derselben Saat sind
   korreliert; das Saatmittel stuetzt sich auf zwei Saaten.
8. **Kleine Code-Maengel ohne Einfluss auf Urteile** (nicht berichtigt, Code eingefroren):
   - In den Bildern steht die Messbeginn-Linie bei t = 250 statt 400.
   - In auswertung.json heissen die bei Z3 ausgeschlossenen Zellen (v = 0,1; 0,02 und 0,04) "fehlt"; sie sind
     "gefangen".
9. **Nach dem Einfrieren:** code/beschreibung.py (sha256 83fbece1..., 23:51:32 UTC, Spur cpu) liefert nur beschreibende
   Zahlen, keine Urteile.
   - Teilfenster-Raten und Potenzen (Abschnitt 3.1)
   - Einschaltarbeit, Orte
10. **Bornsche Schaetzung grob** (freie Wellen, sech-artige Ballform, ohne Ballpotential). Sie war als Schreibtisch
    gedacht und trifft v = 0,5, nicht v = 0,1 bis 0,3.
11. **Kein Messbezug (L5):** synthetisch, 1D, ein omega, eine Gitterweite.
    - Die Uebertragung auf kosmische Strahlung und Finns 3D-Netz ist [H].
    - Die Karte rechnete fuer die Uebertragung mit einer Schwelle. Gerechnet ist eine Reibung, die bei v = 0,5 wieder
      faellt, aber nicht verschwindet.
12. **Zeitbox:** Start 01:03:19, Text ab 01:52:29, Abschluss 01:57:39 CEST (date), innerhalb von 120 min.

## 6. Einfach gesagt

Wir haben unser Modellteilchen, einen Q-Ball, mit verschiedenen Geschwindigkeiten durch eine Kette geschickt, deren
Maschen zufaellig etwas schwerer oder leichter sind, so wie Finns Netz, wenn es Schaum statt Kristall ist. Ohne Unordnung
fliegt der Ball ungebremst weiter; mit Unordnung strahlt er Wellen ab, verliert Ladung und wird langsamer, und zwar etwa
viermal so stark, wenn die Unordnung doppelt so gross ist. Am staerksten gebremst werden mittelschnelle Baelle; ganz
langsame gleiten nicht reibungsfrei, sondern bleiben bei starker Unordnung zwischen den Unebenheiten haengen, und schnelle
verlieren zwar Ladung, behalten aber ihre Geschwindigkeit besser. Ein ungeordnetes Netz bremst Materie also bei jeder
Geschwindigkeit, nicht erst bei hoher. Wenn echte Teilchen fast verlustfrei durchs All fliegen, muss Finns Netz deshalb
sehr glatt sein.
