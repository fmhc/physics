# AETHER-UHR-1: Ergebnis (Code-Agent fuer die Leitung, Runde 36, explorativ)

- Gerechnet auf der .69 ueber kleintest.sh, nur Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich.
- **Ablauf** (Zeiten per date):
  - Start 2026-10-03 23:40:10 CEST. Code ab 23:53.
  - Rauch 1 bis 3: 21:56:41 bis 22:02:37 UTC.
  - Plan ab 00:01:49 CEST. Eingefroren 00:06:16 CEST: PLAN.md.eingefroren-20261004-000616,
    code/*.eingefroren-20261004-000616, sha256 in code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe und Proben 22:06:21 bis 22:40:48 UTC, alle rc = 0, alle Status "fertig".
  - Auswertung 22:40:59 bis 22:41:01 UTC, Bilder bis 22:41:04 UTC.
  - Zwischenauswertungen: 22:13:58 UTC (H-100) und 22:23:46 UTC (H-*, R0, G-115); Selbstanzeige 6.
  - Text ab 00:24:15 CEST.
- **Hashes:**
  - Alle zehn Laeufe tragen die sha256 des eingefrorenen aether.py (8ea2cd3d...), die Auswertung die von auswertung.py
    (fb15f7ab...).
  - Plan und Code wurden nach dem Einfrieren nicht geaendert.
- **Daten:**
  - lauf-69/: je Lauf .json (Kopf), .log und .npz (Zeitreihen, Profile, Momentaufnahmen)
  - lauf-69/auswertung.json: Urteile, alle Plateauwerte, Sollkurven
  - Bilder: lauf-69/R_gegen_v.png, R_rest_gegen_K.png, laenge_gegen_v.png
  - rauch-69/: Rauchlaeufe und Zwischenauswertungen
  - Checkpoints der Gitterproben liegen nur auf der .69 (/home/fmh/fmhc-physics-remote/runde36-aether/lauf/).
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [E] hier gerechnet (synthetisch, keine Messdatenbestaetigung), [F] von mir vor dem Einfrieren festgelegt.

## 1. Ergebnis

1. **Kontrolle c_B = 1: Die Uhren im Beutel merken die Bewegung nicht [E].**
   - R(v)/R(0) - 1 = -2,0e-6 / -7,1e-6 / +1,5e-5 bei v = 0,2 / 0,4 / 0,6 (Schwelle 1e-3).
   - Der Beutel verkuerzt sich mit 1/gamma auf 5e-5 genau. Die A-Uhr geht mit 1/gamma auf 1,6e-5, die B-Uhr auf 9e-6.
2. **Bei c_B ungleich 1 verraet der Uhrenvergleich die Bewegung durchs Netz [E].**
   - R(v)/R(0) - 1 = 0,0092 / 0,042 / 0,124 (c_B = 1,15) und 0,024 / 0,111 / 0,323 (c_B = 1,70).
   - Das folgt der vorab ableitbaren Kinematik K(v) aus dem Ruheprofil [M] auf hoechstens 6e-5 absolut. Mit halbem
     Gitterabstand sind es 1,3e-5 (etwa h^2-Gang). Die halbe Beschleunigung aendert ihn um hoechstens 4e-6.
   - Die B-Mode folgt dem beschleunigten Beutel also adiabatisch. Rueckwirkung und Gitter verschieben R/R0 - 1 um weniger
     als 6e-5.
3. **U1 und U2 sind nicht eingetroffen, weil die Sollwerte der Karte nur die fuehrende Ordnung sind [M, E].**
   - Bei v = 0,6 liegt der Effekt 41 % (c_B = 1,15) bzw. 37 % (c_B = 1,70) ueber v^2 (1 - 1/c_B^2), also ausserhalb von
     20 %. Bei v = 0,2 und 0,4 liegt er innerhalb (-5 bis -7 %, +6 bis +8 %).
   - Das stand vor der Rechnung fest (PLAN.md Abschnitt 7): Schon der harte Hohlraum der Karte gibt
     R/R0 = gamma_A^2/gamma_B^2, also gamma_A^2 = 1,56-mal den Kartenwert bei v = 0,6.
   - Rueckwirkung (Verformung 3,5e-7) und Nichtadiabatik (Adiabatik-Probe: Aenderung <= 4e-6) sind nicht die Ursache.
4. **Der Beutel verkuerzt sich mit gamma_A, nicht mit gamma_B (U3) [E].**
   - In allen neun Faellen gilt abs(L(v) gamma_A/L(0) - 1) <= 4,6e-5.
   - Mit gamma_B waeren es bis -6,2 % (c_B = 1,15) bzw. -14,5 % (c_B = 1,70).
5. **Gesetz fuer kleine v [M, E]:**
   - R/R0 - 1 ~ ((1 + f)/2) v^2 (1 - c_A^2/c_B^2). Dabei ist f der Gradientenanteil der Hohlraummode, hier 0,80 bis
     0,83, also (1 + f)/2 = 0,90 bis 0,91.
   - Das v^2-Gesetz der Karte gilt damit bis auf einen Bauartfaktor der B-Uhr zwischen 1/2 (Mode mit Masse) und 1 (harter
     masseloser Hohlraum).
   - Im Netzbild [H]: Zwei Wellensorten mit verschiedener Grenzgeschwindigkeit machen die Bewegung gegen das Netz
     messbar. Nur eine gemeinsame Grenzgeschwindigkeit macht sie unsichtbar.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 00:06:16 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json.
Hauptlauf, Adiabatik-Probe und Gitterprobe geben dieselben Urteile; es gibt keine Vermerke. K2 ist erfuellt.

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte (Hauptlauf; v = 0,2 / 0,4 / 0,6) |
|---|---|---|---|---|
| U0 | c_B = 1: R(v)/R(0) = 1 innerhalb 1e-3; L ~ 1/gamma innerhalb 1 % | 80 % | **eingetroffen** | R/R0 - 1 = -2,0e-6 / -7,1e-6 / +1,5e-5; L gamma/L0 - 1 = +6,7e-8 / -5,4e-6 / -4,6e-5 |
| U1 | c_B = 1,15: R/R0 - 1 = v^2 (1 - 1/c_B^2) innerhalb 20 % | 65 % | **nicht eingetroffen** | 0,009247 / 0,04219 / 0,1241 gegen 0,009754 / 0,03901 / 0,08776: -5,2 % / +8,2 % / **+41,4 %** |
| U2 | c_B = 1,70: dasselbe Gesetz innerhalb 20 % | 60 % | **nicht eingetroffen** | 0,02443 / 0,1110 / 0,3233 gegen 0,02616 / 0,1046 / 0,2354: -6,6 % / +6,1 % / **+37,4 %** |
| U3 | L verkuerzt sich mit gamma_A, nicht mit gamma_B (alle Faelle, 1 %) | 75 % | **eingetroffen** | max abs(L gamma_A/L0 - 1) = 4,6e-5 (alle drei c_B; L haengt nicht von c_B ab, Unterschied < 1e-8 relativ) |

- **Bedeutung, wie vorab festgelegt:**
  - "U0 bis U3 treffen ein" ist nicht ausgeloest.
  - "U1 verfehlt" ist formal ausgeloest, aber nicht aus dem vorab genannten Grund. Die Karte nannte "Rueckwirkung oder
    Nichtadiabatik verfaelschen die einfache Kinematik". Beides ist hier ausgeschlossen:
    - Rueckwirkungsprobe: Verformung 3,5e-7.
    - Adiabatik-Probe: R/R0 - 1 aendert sich um hoechstens 4e-6.
    - Die Rechnung folgt der vollstaendigen Kinematik K(v) auf hoechstens 2,7e-4 relativ.
  - Verfehlt wird nur die Reihenentwicklung der Karte. Ihre eigene Formel gamma_A^2/gamma_B^2 hat bei v = 0,6 den
    Faktor 1/(1 - v^2) = 1,5625 mehr. Die weichen Waende (f ~ 0,8) holen davon etwas zurueck.
  - Der Kern der ersten Bedeutung bleibt: Ein Netz mit zwei Wellengeschwindigkeiten verraet seine Bewegung durch
    Uhrenvergleiche, fuer kleine v mit dem v^2-Gesetz bis auf den Bauartfaktor (1 + f)/2.

## 3. Tabellen

### 3.1 Ruhewerte (Hauptlaeufe, h = 0,05)

| Groesse | c_B = 1,00 | c_B = 1,15 | c_B = 1,70 |
|---|---|---|---|
| Omega_B(0) | 0,150787 | 0,169203 | 0,232240 |
| lambda_1 / lambda_2 / lambda_3 (B-Moden, m_B^2 = 1) | 0,02274 / 0,08920 / 0,19502 | 0,02863 / 0,11222 / 0,24486 | 0,05394 / 0,21019 / 0,45259 |
| Gradientenanteil f der Grundmode | 0,8272 | 0,8215 | 0,7962 |
| R(0) = Omega_B/omega_A | 0,213245 | 0,239289 | 0,328437 |

- Beutel (fuer alle gleich): Halbwertsbreite der Ladungsdichte L0 = 21,00006, omega_A(0) = 0,7071068
  (omega^2 - 1/2 = 2,5e-13).
- Energie M0 = 21,7071, Ladung Q0 = 29,6985, Newton-Rest 1,6e-13, B-Amplitude 1e-3.
- Feld E_k = 5,97e-4 / 6,79e-4 / 9,17e-4 (Adiabatik-Probe halb). Hoechste Eigenbeschleunigung 1,25e-3.

### 3.2 Uhren und Lineal je Plateau (Hauptlaeufe)

- Gemessene Schnelle 0,199993 / 0,399973 / 0,599913 in allen drei Laeufen.
- gamma_A = 1,020619 / 1,091076 / 1,249898.

| c_B | v | L(v) | omega_A | Omega_B | Omega_B(v)/Omega_B(0) | Omega_B gamma_B/Omega_B(0) - 1 | R/R0 - 1 | Karte v^2(1 - 1/c_B^2) | K(v) [M] | harter Hohlraum [M] |
|---|---|---|---|---|---|---|---|---|---|---|
| 1,00 | 0,2 | 20,57581 | 0,692821 | 0,147740 | 0,97980 | -2,0e-6 | -2,0e-6 | 0 | 0 | 0 |
| 1,00 | 0,4 | 19,24702 | 0,648081 | 0,138199 | 0,91652 | -8,8e-6 | -7,1e-6 | 0 | 0 | 0 |
| 1,00 | 0,6 | 16,80065 | 0,565723 | 0,120639 | 0,80006 | -1,1e-6 | +1,5e-5 | 0 | 0 | 0 |
| 1,15 | 0,2 | 20,57581 | 0,692821 | 0,167318 | 0,98886 | +0,42 % | 0,0092471 | 0,0097536 | 0,0092486 | 0,0101600 |
| 1,15 | 0,4 | 19,24702 | 0,648081 | 0,161622 | 0,95520 | +1,88 % | 0,0421946 | 0,0390118 | 0,0421988 | 0,0464414 |
| 1,15 | 0,6 | 16,80065 | 0,565723 | 0,152166 | 0,89931 | +5,41 % | 0,1240626 | 0,0877627 | 0,1240337 | 0,1371068 |
| 1,70 | 0,2 | 20,57581 | 0,692821 | 0,233107 | 1,00373 | +1,08 % | 0,0244291 | 0,0261574 | 0,0244298 | 0,0272472 |
| 1,70 | 0,4 | 19,24702 | 0,648081 | 0,236484 | 1,01827 | +4,77 % | 0,1110137 | 0,1046227 | 0,1110124 | 0,1245476 |
| 1,70 | 0,6 | 16,80065 | 0,565723 | 0,245880 | 1,05873 | +13,15 % | 0,3233250 | 0,2353640 | 0,3232685 | 0,3676961 |

- Die A-Uhr geht in allen Laeufen mit 1/gamma_A, unabhaengig von c_B.
- **Die B-Uhr geht nicht mit 1/gamma_B [E, M]:**
  - Ihr Topf ist im B-Ruhesystem um gamma_B/gamma_A gestaucht, ihre Eigenfrequenz steigt also.
  - Bei c_B = 1,70 ueberwiegt das: Die B-Uhr tickt im bewegten Beutel sogar in Laborzeit schneller als in Ruhe (+5,9 %
    bei v = 0,6).
- Kartenabweichung (R/R0 - 1)/Karte - 1: c_B = 1,15: -5,19 / +8,16 / +41,36 %; c_B = 1,70: -6,61 / +6,11 / +37,37 %.
- **Fuer kleine v** geht K/Karte gegen (1 + f)/2 = 0,911 (c_B = 1,15) bzw. 0,898 (c_B = 1,70) [M].
  - Bei v = 0,2 sind es 0,948 und 0,934.
  - Der harte Hohlraum gaebe 1/(1 - v^2) = 1,042 / 1,190 / 1,5625.

### 3.3 Proben: R/R0 - 1 und L gamma_A/L0 - 1

- H = Hauptlauf (h = 0,05, T_r = 500); A = Adiabatik-Probe (T_r = 1000, halbes Feld); G = Gitterprobe (h = 0,025,
  dt = 0,005).
- Schnelle bei G: 0,199998 / 0,399993 / 0,599978.

| c_B | v | R/R0 - 1: H | A | G | K(v) bei G [M] | L-Rest: H | A | G |
|---|---|---|---|---|---|---|---|---|
| 1,00 | 0,2 | -2,0e-6 | -2,0e-6 | -5e-7 | 0 | +6,7e-8 | +2,0e-7 | +6,6e-8 |
| 1,00 | 0,4 | -7,1e-6 | -4,9e-6 | -3,9e-6 | 0 | -5,4e-6 | -4,5e-6 | -2,1e-6 |
| 1,00 | 0,6 | +1,5e-5 | +1,9e-5 | -2e-7 | 0 | -4,6e-5 | -4,5e-5 | -1,3e-5 |
| 1,15 | 0,2 | 0,0092471 | 0,0092471 | 0,0092487 | 0,0092491 | wie oben | | |
| 1,15 | 0,4 | 0,0421946 | 0,0421964 | 0,0422013 | 0,0422039 | | | |
| 1,15 | 0,6 | 0,1240626 | 0,1240667 | 0,1240796 | 0,1240758 | | | |
| 1,70 | 0,2 | 0,0244291 | 0,0244291 | 0,0244309 | 0,0244311 | | | |
| 1,70 | 0,4 | 0,1110137 | 0,1110144 | 0,1110253 | 0,1110255 | | | |
| 1,70 | 0,6 | 0,3233250 | 0,3233266 | 0,3233895 | 0,3233763 | | | |

- Die Beutellaenge haengt nicht von c_B ab (Unterschiede < 1e-8 relativ). Die L-Reste der Zeilen 1,15 und 1,70 sind deshalb
  dieselben wie bei 1,00.
- **Abweichung von K(v) bei v = 0,6** (R_rest_gegen_K.png):
  - H: 1,5e-5 / 2,9e-5 / 5,6e-5 (c_B = 1,00 / 1,15 / 1,70)
  - A: 1,9e-5 / 3,3e-5 / 5,8e-5
  - G: -2e-7 / 3,8e-6 / 1,3e-5
  - Der Rest ist also ein Gittereffekt (er faellt bei halbem h um den Faktor 4 bis 8, bei c_B = 1 auf -2e-7), kein Adiabatikfehler.

## 4. Kontrollen

- **K1 Uhrwahl (c_B = 1) [F]:**
  - max abs(omega_A gamma_A/omega_A(0) - 1) und abs(Omega_B gamma_B/Omega_B(0) - 1): 1,6e-5 (H), 1,6e-5 (A), 4,3e-6 (G).
    Schwelle 1e-3: erfuellt.
  - Die Phase des eichkovarianten Felds am mitbewegten Mittelpunkt ist also die Eigenzeit-Uhr.
  - Die reine Zeitableitung am festen Ort gaebe omega gamma_A = 0,884 statt 0,566 bei v = 0,6 [M], also den
    Dopplerbeitrag.
- **K2 Rueckwirkung:**
  - Profil S bei t = 480 mit b = 1e-3 gegen b = 0: max abs(S_b - S_0)/max S_0 = 3,6e-7 / 3,5e-7 / 3,4e-7 (c_B = 1,00 / 1,15
    / 1,70). Schwelle 1e-3: erfuellt.
  - Aenderung von L(0) -1,5e-7, von omega_A(0) <= 1,4e-8.
- **Zusatz Z-K (kein Kartenurteil) [F]:** abs(R/R0 - 1 - K) <= 0,05 abs(K) + 2e-4 in allen sechs Laeufen mit
  c_B ungleich 1 erfuellt. Groesste Abweichung absolut 5,8e-5 (A-170, v = 0,6), relativ 2,7e-4 (A-115, v = 0,6).
- **Bilanzen** (ganzer Lauf, inklusive Feldarbeit):
  - Energie <= 7,7e-10 M0 bei h = 0,05 und <= 4,8e-11 M0 bei h = 0,025.
  - Ladung <= 9,1e-14 Q0.
  - Feldarbeit 5,4263; Schwamm- und Fensterabfluss <= 8,5e-11.
  - Der Beutel strahlt also nichts Messbares ab.
- **Zweite Messgroessen:**
  - B im Mittelpunkt allein statt Fenstermittel: R/R0 - 1 gleich auf <= 5e-8.
  - Halbwertsbreite von |A|^2 statt der Ladungsdichte: L-Rest <= 6,4e-5.
- **Ruhe der Plateaus:**
  - Fit-Rest der B-Schwingung <= 6,6e-4 der Amplitude (A: <= 1,3e-4).
  - Schwankung der Beutellaenge <= 7e-4 absolut (4e-5 relativ).
  - Rest der Ortsgeraden <= 2e-4.
  - Der Rest der Phasengeraden betraegt <= 3,2e-4 rad.
- **Laufzeiten:** H 227 s, A 326 s, G 690 s in zwei Wandzeit-Abschnitten, R0 32 s.
- **Latten (v3):**
  - L1 kann scheitern: U0 und U3 nur numerisch (Rauch 2 mit kurzen Rampen gab bei c_B = 1 noch -6e-3). U1 und U2
    konnten bei v = 0,6 nicht bestehen (Selbstanzeige 4). Die eigentliche Pruefung der Dynamik ist Z-K; sie haette
    scheitern koennen.
  - L2 Gegenprobe: Kontrolle c_B = 1, Adiabatik-Probe, Gitterprobe, Rueckwirkungsprobe, zweite Messgroessen.
  - L3 Numerik: Bilanzen 1e-9 bzw. 1e-13, h^2-Gang des Rests.
  - L4 schon bekannt:
    - Lorentz' Satz der korrespondierenden Zustaende: Ist alles aus einer Wellensorte gebaut, ist die Bewegung gegen den
      Aether unsichtbar [L].
    - Kennedy-Thorndike-Versuch (1932): Lichtlaufzeit gegen Uhr bei wechselnder Geschwindigkeit [L].
    - Test-Theorie nach Robertson, Mansouri und Sexl [L].
    - Verschiedene Hoechstgeschwindigkeiten je Teilchensorte: Coleman und Glashow, spaete 1990er [L?].
    - Zweikomponenten-Kondensate mit zwei Schallgeschwindigkeiten als Analogmodell (Liberati, Visser, Weinfurtner, um
      2006) [L?].
    - Das Ergebnis ist also bekannte Kinematik in einem neuen Zweifeldmodell.
  - L5 Messbezug, nur ueber die Karte [L]:
    - Uhrenvergleiche begrenzen Unterschiede der Grenzgeschwindigkeit zwischen Sektoren auf 1e-17 bis 1e-20.
    - Mit v ~ 1,2e-3 gegen den Mikrowellenhintergrund verlangt das abs(1 - c_A^2/c_B^2) < ~1e-11 bis 1e-14.
    - Der Bauartfaktor (1 + f)/2 zwischen 1/2 und 1 aendert die Groessenordnung nicht [M].
    - Moderne Kennedy-Thorndike-Versuche (Resonator gegen Atomuhr) messen genau diesen v^2-Gang [L?, Zahlen nicht
      nachgeschlagen].

## 5. Selbstanzeigen

1. **Rauch 1, Fehler in der Kontinuumsformel:** In der Halbwertsbreite stand (2 + D)/D statt (1 + 2D)/D. Der Beutel war
   20,0 statt 21 lang. Vor Rauch 2 berichtigt, im Plan offengelegt.
2. **Vor dem Einfrieren gesehen (Rauch 2, PLAN.md Abschnitt 8):**
   - der U2-Wert bei v = 0,6 (+36 % gegen die Karte, K(v) auf 0,6 % getroffen)
   - die Abweichungen der Kontrolle (-6e-3 bei kurzen Rampen)
   - T_r = 500 und T_p = 480 habe ich danach gewaehlt (Protokoll, keine Schwelle). Schwellen und Regeln der Karte
     blieben unveraendert.
3. **Nach Rauch 2, vor dem Einfrieren:** Regel "Probe nicht gerechnet: Haupturteil bleibt mit Vermerk" in auswertung.py
   und im Plan ergaenzt. Sie kam nicht zum Tragen: alle Proben liefen.
4. **Ausgang von U1/U2 vorab ableitbar [M]:**
   - Die Sollwerte der Karte sind die fuehrende Ordnung. Selbst ein idealer harter Hohlraum verfehlt bei v = 0,6 um
     +56 %.
   - "nicht eingetroffen" spricht also nicht gegen die Aether-Kinematik, sondern gegen die Naeherung der Karte bei
     v = 0,6. Das stand im Plan, bevor ein Hauptlauf rechnete.
   - Auch U0 und U3 folgen aus der Lorentz-Invarianz von A (und von allem bei c_B = 1). Gerechnet wurde also nur, ob
     Dynamik und Numerik der Kinematik folgen (Z-K).
5. **Bauartwahl der B-Uhr [F]:**
   - g = m_B^2 = 1 (innen masselos) war vor jeder Rechnung festgelegt, begruendet mit der masselosen Hohlraummode der
     Karte.
   - Die weichen Waende des A-Beutels geben trotzdem f = 0,80 bis 0,83 statt 1. Ein anderer Topf gaebe einen anderen
     Faktor (1 + f)/2.
   - Dass U1/U2 bei v = 0,2 und 0,4 innerhalb 20 % liegen, haengt daran mit: Der harte Hohlraum laege bei v = 0,4 mit
     +19,0 % knapp innerhalb, dieser Topf liegt bei +6 bis +8 %.
6. **Zwischenauswertungen** um 22:13:58 UTC (H-100) und 22:23:46 UTC (H-*, R0, G-115):
   - mit dem eingefrorenen auswertung.py, auf cpu3 zwischen zwei Laeufen (Lock), also nie als dritter Lauf
   - Zweck: Fehlersuche und frueher Textbeginn
   - Danach wurde nichts geaendert.
7. **Fortsetzung nach Wandzeit-Abbruch:** Die Gitterproben liefen in zwei Abschnitten. Bitgleiche Fortsetzung habe ich
   nur in Rauch 3 geprueft (gleiche Endwerte auf alle Stellen), nicht an den Hauptlaeufen.
8. **U3 "nicht mit gamma_B":**
   - Bei c_B = 1,15 und v = 0,2 laege auch eine gamma_B-Verkuerzung innerhalb 1 % (-0,50 %).
   - Die Unterscheidung traegt bei c_B = 1,15 erst ab v = 0,4 (-2,2 % und -6,2 %), bei c_B = 1,70 ueberall (-1,3 %,
     -5,7 %, -14,5 %).
9. **Messgroessen [F]:**
   - Die Uhrwahl (Phase von e^(-i a x) A am mitbewegten Mittelpunkt) und das B-Fenster (Radius 5, cos^2) sind von mir.
   - In einem geboosteten Fenster koennen ungerade Moden ins Mittel einstreuen. Der Mittelpunkt allein gab aber dieselben
     Werte R/R0 - 1 auf 5e-8.
10. **Gittertraegheit:** Die erreichte Schnelle liegt bei h = 0,05 um 9e-5 unter dem Ziel 0,6, bei h = 0,025 um 2e-5.
    Alle Sollwerte sind deshalb am gemessenen v ausgewertet.
11. **Kein Messbezug (L5) aus eigener Rechnung:** synthetisch, 1+1D, ein Beutel, eine Kopplung. Die Uebertragung auf
    Finns 3D-Netz (Laengs- gegen Querwellen) ist [H].
12. **Zeitbox:** Start 23:40:10 CEST, Text ab 00:24:15 CEST, Abschluss 00:51:08 CEST (innerhalb von 150 min).

## 6. Einfach gesagt

Wir haben im Rechner einen langen Beutel aus Feld A gebaut, in dem eine zweite Wellensorte B hin- und herschwingt, und
ihn auf 20, 40 und 60 Prozent der Lichtgeschwindigkeit beschleunigt. Sind beide Wellensorten gleich schnell,
gehen die zwei Uhren im Beutel bei jeder Geschwindigkeit gleich (auf 0,002 Prozent): Wer im Beutel sitzt, merkt nicht,
dass er durchs Netz fliegt. Ist die B-Welle 1,15- oder 1,7-mal schneller, laeuft die B-Uhr bei 60 Prozent um 12 bzw. 32
Prozent vor, und die Bewegung durchs Netz verraet sich. Die Karte hatte das mit einer Naeherungsformel fuer kleine
Geschwindigkeiten geschaetzt; bei 60 Prozent ist der echte Effekt gut ein Drittel groesser, genau wie die vollstaendige
Formel es vorhersagt. Fuer Finns Netz heisst das: Weil echte Uhrenvergleiche keinen solchen Gang zeigen, muessen Licht und
Materie ueber dieselbe Wellensorte laufen.
