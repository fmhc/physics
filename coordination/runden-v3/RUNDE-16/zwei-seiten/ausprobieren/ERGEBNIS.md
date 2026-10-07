# ERGEBNIS: Ausprobieren V1 bis V5 (Runde 16, "Zwei Seiten des Feldes")

- Code-Agent im Auftrag von claude-primary, Finn: "probier in einem subagent einfach mal aus die sachen".
- Zeitbox ab 08:16:11 CEST. Plan eingefroren 08:23:14 (PLAN.md.eingefroren-20261002-082314). Bericht geschrieben ab 08:50:38 CEST (date).
- Alle berichteten Zahlen stammen aus Laeufen auf der .69 (kleintest.sh, Spuren cpu und cpu2). Lokal liefen nur Rauchtests.
- Explorativ. Synthetische Rechnungen an Spielzeugmodellen, keine Messdaten.

## 1. Ergebnis zuerst

1. **Positivkontrollen bestanden (V1, V2).**
   - Federtetraeder: Spektrum (k/m) {0 x6, 1, 1, 2, 2, 2, 4} auf 2e-15.
   - Maxwell-Ring: N = 3 bis 6 sind fuer jedes m/M instabil. Ab N = 7 ist der Ring stabil unterhalb einer Grenze eps_c(N).
   - eps_c N^3 sinkt von 2,45 (N = 7) auf 2,30 (N = 64), Steigung -3,01. Das passt zu Maxwells 1/0,4352 = 2,298 [L?], dem sich der Wert von oben naehert, und zum Befund von Vanderbei/Kolemen (arXiv:astro-ph/0606510).
   - Der gyroskopische Stabilitaetscode fuer Variante R ist damit geprueft.
2. **Ticks (V4) sind ereignisgenau schrittweitenunabhaengig, naiv nicht.**
   - Ereignisgenau: 1226 Ticks in T = 200 bei jedem dt <= 0,1, Ereigniszeiten auf 4e-13 gleich. Erst bei dt = 0,2 fehlen 6 Ticks (0,5 %).
   - Naive Zustandsvergleiche verlieren Ereignisse etwa proportional zu dt: 13 % bei dt = 0,2, 0,5 % bei dt = 0,005.
3. **Federring (V3): Nicht die Rotation macht instabil, sondern die Vorspannung.**
   - Spannungsfrei gebaut (F0): stabil bis zum Durchgehen (R -> unendlich bei Omega -> sqrt K_N).
   - Mit gleichen Ruhelaengen (F1): ab N = 10 schon in Ruhe eingeknickt (2D; in 3D jedes N ausser 6). Rotation stabilisiert ab Omega_stab(N) = 0,38 (N = 10) bis 0,89 (N = 32).
   - Die Kartenvorhersage "ab kritischem Omega instabil" traf nicht ein.
4. **Diskretes sextisches Feld (V5): lokalisierte, phasenrotierende Moden existieren, aber nicht im Fenster (0,5; 1).**
   - Das Fenster ist [1/3 + O(J), 1 - O(J)], z. B. [0,475; 0,96] bei J = 0,05 und [0,59; 0,92] bei J = 0,1.
   - Ein Stabilitaetskriterium (Zahl negativer Richtungen plus Vorzeichen von dQ/domega) sagte an allen 3954 Punkten das Eigenwertergebnis richtig voraus.
   - Am Zentrum ("+1") gibt es nur fuer J N <= 0,55 bis 0,6 eine Mode.
5. **11 und 19 sind nirgends auffaellig.**
   - |z(11)| und |z(19)| bleiben in V3 und V5 unter 3 (groesster Betrag 2,3, bei S auf Rauschniveau). Der vorab festgelegte Test markierte nur andere N, und zwar Rauschboden oder Regimegrenzen.
   - Einzige scheinbare "11": Bei J = 0,05 ist N = 11 die letzte Ringgroesse mit Zentrumsmode. Das ist die Schwelle J N = 0,55, sie wandert mit J (N_max = 20, 15, 11, 9, 7 fuer J = 0,03 bis 0,08).

## 2. Je Versuch

### V1 Federtetraeder

- **Ergebnis:** Eigenwerte der Hesse-Matrix (k = m = 1): 0 (6-fach, |mu| < 1e-15), 1, 1, 2, 2, 2, 4.
  - Groesste Abweichung von der Vorhersage: 1,8e-15 (analytisch), 2,0e-8 (finite Differenzen, h = 1e-4), 2,1e-10 (h = 1e-5).
  - Die sechs Nullmoden liegen ganz im Raum aus Translation und Rotation (Projektion 1,000; Rest < 1e-30).
- **Vorab gegen Ausgang:** {0 x6, 1, 1, 2, 2, 2, 4} (~95 %): eingetroffen.
- **Kontrollen:**
  - Nichtlineare Zeitentwicklung (Auslenkung 1e-4, T = 400): Spektrum der Kantenlaengen mit Spitzen bei omega = 0,99982; 1,41427; 2,00029 (Aufloesung 0,0157).
  - Energiefehler Velocity-Verlet: 7,9e-5 (dt = 0,01), 2,0e-5, 5,0e-6, 1,24e-6, 3,1e-7 (dt = 0,000625).
    - Faktor 4,0 je Halbierung, also proportional zu dt^2. Beschraenkt, ohne Drift.
    - Die Kartenschwelle 1e-6 erfuellt erst dt = 0,000625.
- **Abbildung:** aus/v1_tetra.png.

### V2 Maxwell-Ring mit Gravitation (Positivkontrolle)

- **Aufbau:**
  - N Massen m auf R = 1 um M = 1, G = 1, die Zentralmasse ist beweglich und sitzt im Schwerpunkt.
  - Omega^2 = 1 + (m/4M) sum 1/sin(pi j/N). Kraeftebilanz-Rest <= 8,5e-16.
  - Linearisierung im mitrotierenden System, Begleitmatrix [[0, I], [-M^-1 K_eff, -M^-1 G]].
- **Ergebnis:**
  - N = 3, 4, 5, 6: instabil fuer jedes m/M im Raster 1e-9 bis 1e-1 (81 Punkte).
    - max Re s bei 1e-6: 1,53e-3; 1,44e-3; 1,24e-3; 9,14e-4.
    - Bei 1e-4 jeweils das Zehnfache, also Wachstum proportional zu sqrt(m/M).
  - N >= 7: stabil unterhalb eps_c(N), darueber instabil. Fuer jedes N genau ein Umschlag, keine Fenster.
  - Grenzen und eps_c N^3:

| N | eps_c | eps_c N^3 |
|---|---|---|
| 7 | 7,150e-3 | 2,453 |
| 8 | 4,711e-3 | 2,412 |
| 11 | 1,779e-3 | 2,368 |
| 19 | 3,389e-4 | 2,325 |
| 32 | 7,045e-5 | 2,309 |
| 64 | 8,780e-6 | 2,301 |

  - Potenzfit log eps_c gegen log N:
    - Plan-Bereich N = 20..64 (aus dem abgebrochenen ersten Lauf, dessen eps_c-Werte bitgleich reproduziert sind): Steigung -3,008, Vorfaktor 2,375.
    - Teil 2 allein (N = 25..64): -3,006 und 2,359.
- **Triviale Eigenwerte** (benannt, ausgeklammert):
  - 0, 2-fach: Drehung und Partner aus der Radius/Omega-Familie.
  - +-i Omega, zusammen 6 bei m/M = 1e-4: Schwerpunkt (4, Jordan-Bloecke) und Kepler-Familie (2).
  - Ihr numerischer Realteil (Rauschboden) liegt bei <= 5e-8.
- **Vorab gegen Ausgang:**
  - "Stabil genau fuer N >= 7, wenn m/M klein genug" (~70 %): eingetroffen.
  - "Stabiles m/M schrumpft wie N^-3" (~60 %): eingetroffen. Der Vorfaktor naehert sich 2,298 von oben (2,301 bei N = 64).
  - Literatur ueber die arXiv-API, nur Abstracts: Vanderbei/Kolemen, astro-ph/0606510: "always unstable for 2<=n<=6 and for n > 6 they are stable provided that the central mass is massive enough".
  - Den Zahlenwert 0,4352 nennt das Abstract nicht, er bleibt [L?].
- **Kontrollen:**
  - Methode A (analytisch, volles System), Methode B (heliozentrisch, finite Differenzen) und A in 3D: gleiche Einstufung in allen 28 Tabellenfaellen, auch bei tol 1e-5 und 1e-7.
  - B an der Grenze: 0,99 eps_c stabil (max Re <= 6,7e-10), 1,01 eps_c instabil (max Re etwa 0,036). 3D bei 0,99 eps_c stabil.
  - Hesse-Matrix gegen finite Differenzen: 1,2e-10 relativ.
  - Nichtlineare Zeitentwicklung, m/M = 1e-4, T = 3000, rtol 1e-10 und 1e-12:
    - N = 6 waechst mit 0,009134, die Linearisierung sagt 0,009127 (0,08 %). Der Ring zerfaellt (Formabweichung 1,4).
    - N = 8 bleibt beschraenkt: Formabweichung <= 8e-6 bei Start 1,3e-7, ohne exponentielles Wachstum. Deutung, ungeprueft: Die Verstaerkung um etwa 1/sqrt(m/M) passt zu den langsamen Driftmoden.
    - Energie- und Drehimpulsfehler: 1,8e-9 bzw. 9e-10 (rtol 1e-10), 1,1e-11 bzw. 5e-12 (rtol 1e-12).
- **Abbildung:** aus/v2_maxwell.png.

### V3 Federring N + 1

- **Aufbau:** Massen 1, k_Speiche = k_Ring = 1, R(Omega) aus der Kraeftebilanz (Rest <= 1e-14).
  - F0: Ruhelaengen L_s = 1, L_r = 2 sin(pi/N), spannungsfrei in Ruhe.
  - F1: L_s = L_r = 1. Fuer N > 6 ist der Ring dann gestaucht, fuer N < 6 sind die Speichen gestaucht.
- **Ergebnis F0:** fuer alle N = 4..32 spektral stabil auf dem ganzen Raster Omega = 0 bis 0,999 sqrt(K_N), in 2D und 3D.
  - Groesster Realteil 6e-8 bzw. 9e-8, das ist der Rauschboden.
  - Bei Omega -> sqrt(K_N) waechst R ueber alle Grenzen (Durchgehen), ohne vorherige Instabilitaet.
  - Weichste Frequenz bei Omega = 0,6: glatt fallend von 0,65 (N = 4) auf 0,16 (N = 32).
- **Ergebnis F1:**
  - In 2D sind N = 4..9 ueberall stabil.
  - N >= 10 ist in Ruhe eingeknickt (gestauchter Ring). Rotation stabilisiert ab Omega_stab: 0,382 (N = 10), 0,503 (11), 0,587 (12), 0,793 (19), 0,890 (32), monoton.
  - In 3D ist jedes N ausser N = 6 in Ruhe instabil. Deutung, nicht an Eigenvektoren geprueft: Bei N < 6 knickt die Mitte aus (Speichen gestaucht), bei N > 6 der Ring. Bei Omega = 0,9 ist alles stabil.
  - N = 6 ist der einzige spannungsfreie F1-Fall (Sechseck: Seite = Radius).
- **Vorab gegen Ausgang:**
  - "Ab einem kritischen Omega werden Ringe instabil" (~70 %): nicht eingetroffen. F0 bleibt stabil bis zum Durchgehen. F1 zeigt das Gegenteil: in Ruhe instabil, durch Rotation stabilisiert. Die vorab gewaehlte Kennzahl Omega_c ist deshalb entartet (F0: nie; F1: 0 oder undefiniert).
  - "Kein N auffaellig, 11 und 19 nicht ueber 3 sigma" (~85 %): fuer 11 und 19 eingetroffen.
    - omega_soft(0,6): z(11) = 0,22 und z(19) = 0,14 (F0); 1,52 und 0,84 (F1). Omega_stab (nachtraeglich): z(19) = -0,31.
    - Der vorab festgelegte Test auf S(N) = max Re markierte N = 10, 17, 25 (F0) und N = 9, 10, 12 (F1).
    - Bei F0 ist S reines Rauschen um 1e-8. Bei F1 liegen die markierten N an Regimegrenzen: Umschlag stabil/instabil zwischen N = 9 und 10 bei Omega = 0,3 und zwischen 12 und 13 bei Omega = 0,6.
    - Keine dieser Marken ist eine N-Eigenschaft. Selbstanzeige: S ist als Kennzahl fuer diesen Test ungeeignet.
- **Kontrollen:**
  - Methode B (Hesse-Matrix per finiter Differenzen, Abweichung <= 1e-10, tol 1e-4) stuft in allen 174 Faellen gleich ein wie A.
  - 2D gegen 3D getrennt berichtet.
  - Keine Zeitentwicklung gerechnet.
- **Abbildung:** aus/v3_federring.png.

### V4 Ticks ereignisgenau

- **Aufbau:**
  - Tetraeder A dreht um z (omega_A = 1).
  - Tetraeder B dreht um (1, 2, 2)/3 (omega_B = sqrt 2), sein Mittelpunkt pendelt (0,3 sin 0,618 t).
  - 68 Paare: 32 Ecke-Flaeche, 36 Kante-Kante. T = 200.
- **Ergebnis ereignisgenau:**
  - 1226 Ticks (229 Ecke-Flaeche, 997 Kante-Kante), nu = 6,13 je Zeiteinheit.
  - Gleich fuer dt = 0,1; 0,05; 0,02; 0,01; 0,005 und die Referenz 0,001. Ereigniszeiten gegen die Referenz <= 3,7e-13.
  - Bei dt = 0,2: 1220, sechs Kante-Kante-Ticks fehlen (zwei Vorzeichenwechsel in einem Schritt).
  - Von 4254 Vorzeichenwechseln bestehen 1226 den Innen-Test.
- **Ergebnis naiv** (Summe |B_k Delta B_k+1| ueber 48 Kante-Flaeche-Paare; Soll ohne Verluste 3 N_EF + 4 N_KK = 4675):
  - 4055 (dt = 0,2), 4337 (0,1), 4493 (0,05), 4581 (0,02), 4625 (0,01), 4651 (0,005), 4673 (0,001).
  - Der Fehlbetrag waechst etwa proportional zu dt: Zwei Ereignisse am selben Paar in einem Schritt heben sich auf.
  - "Schritte mit Wechsel": 691 bis 1223 statt 1226.
- **Vorab gegen Ausgang:**
  - "Ereignisgenau gleich fuer alle dt" (~95 %): in der feinen Reihe (0,02 / 0,01 / 0,005) eingetroffen, in der groben (0,2 / 0,1 / 0,05) nicht (1220 gegen 1226).
  - "Naiv dt-abhaengig oder verpasst Ereignisse" (~70 %): eingetroffen, beides.
- **Kontrollen:**
  - Rate bei T = 400: 6,09; bei T = 200: 6,13.
  - Fuenf Stoerungen des Mittelpunkts um 1e-3: 1222 bis 1228 Ticks.
- **Abbildung:** aus/v4_ticks.png.

### V5 Diskretes sextisches Feld auf dem Rad-Graphen

- **Aufbau:**
  - Ring aus N Knoten plus Zentrum, J gleich auf allen Kanten, V'(s) = 1 - 2 s + 1,5 s^2.
  - Newton mit Fortsetzung in J ab der exakten Anti-Kontinuum-Loesung (12 Schritte).
  - Stabilitaet im mitrotierenden Phasenbild bei fester Ladung.
  - Raster: omega^2 = 0,300..0,995 (Schritt 0,005), N = 8..21, J = 0,05 / 0,1 / 0,2.
- **Ergebnis Ringmode** (kleiner Zweig s < 2/3 bzw. grosser Zweig):
  - Kontrolle J = 1e-4: Fenster [0,334; 0,999], erwartet [1/3, 1). Das Minimum von V'(s) ist 1/3 bei s = 2/3.
  - J = 0,05: klein [0,475; 0,945 bis 0,960], stabil bis 0,93 bis 0,95. Gross [0,475; 0,775 bis 0,79], stabil.
  - J = 0,1: klein [0,59; 0,885 bis 0,925], stabil bis 0,87 bis 0,90. Gross [0,59; 0,705 bis 0,74], stabil.
  - J = 0,2: klein [0,655 bis 0,72; 0,75 bis 0,84], stabiler Anteil 83 bis 95 %. Gross fast verschwunden, instabil.
  - Instabil wird jeweils das obere Fensterende: reelles Paar, dQ/domega > 0 (Abbildung, linke Tafel: Minimum von Q).
- **Ergebnis Zentrumsmode:**
  - Nur bei J = 0,05 und N <= 11, das Fenster schrumpft: N = 8 [0,68; 0,835], N = 11 [0,76; 0,795].
  - Nachtrag v5b, groesstes N mit Zentrumsmode: N_max = 20, 15, 11, 9, 7 fuer J = 0,03 / 0,04 / 0,05 / 0,06 / 0,08. Also J N_max = 0,54 bis 0,60.
- **Stabilitaetskriterium:**
  - Vorhersage "stabil, wenn K_u keine negative Richtung hat oder genau eine mit dQ/domega < 0".
  - Sie traf an allen 3954 Punkten. Drei Einzelpunkte sind oszillatorisch statt reell (J = 0,05, grosser Zweig, N = 14, 18, 20, omega^2 = 0,945, eine Loesung mit zwei negativen Richtungen).
  - Auf dem grossen Zweig ist dQ/domega > 0 und trotzdem stabil, weil dort K_u positiv ist. Ein reines "dQ/domega < 0" waere falsch.
- **Vorab gegen Ausgang:**
  - "Lokalisierte Moden fuer omega^2 im Fenster (0,5; 1) bei kleiner J" (~80 %): teilweise.
    - Die Moden existieren, die Grenzen sind aber 1/3 + O(J) und 1 - O(J).
    - Die Kontinuumszahl omega_min^2 = 1/2 (Minimum von V/s) ist keine Grenze des diskreten Problems. Bei J = 0,05 liegt die untere Kante zufaellig nahe 0,5.
  - "Kein N ist besonders" (~85 %): eingetroffen.
    - Im vorab festgelegten Test hatten 11 und 19 bei N = 8..21 keine volle Nachbarschaft (Selbstanzeige). Einzige Marke dort: N = 14, grosser Zweig, J = 0,05 (eine Fortsetzungsluecke).
    - Nachtrag v5b (N = 4..26, festes omega^2, stetige Kennzahlen Q, PR, kleinste innere Frequenz, Zentrumsamplitude): max |z| <= 1,29, relative Abweichungen <= 1,4 %, kein N markiert. |z(11)|, |z(19)| <= 0,28 bei J = 0,05 und 0,1.
- **Kontrollen:**
  - dQ/domega analytisch gegen finite Differenzen: Median der Abweichung 1e-4 bis 7e-3.
  - Fortsetzung gegen Neustart: <= 1,2e-10.
  - Zeitentwicklung (N = 11, 12; J = 0,1; T = 500; Stoerung 1e-6):
    - Stabile Moden (omega^2 = 0,7 klein; 0,6 gross) bleiben innerhalb 2e-7.
    - Die instabile Mode omega^2 = 0,9 (max Re = 0,038 bzw. 0,034) erreicht bei t = 100 3,6e-6 bzw. 6,3e-6 (erwartet etwa 4e-6) und bis T = 500 0,32 bzw. 0,057.
    - Energie- und Ladungsfehler <= 3e-9 (rtol 1e-10) bzw. <= 2e-11 (rtol 1e-12).
- **Abbildung:** aus/v5_feld.png (rechte Tafel aus v5b).

## 3. Was fuer Finns Arbeitsmodell traegt und was nicht

**Traegt:**

- Variante R (§6, §7): Die gyroskopische Stabilitaetsrechnung im mitrotierenden System reproduziert Maxwell und die Literatur. Neue Ringrechnungen koennen darauf aufsetzen.
- §4 (Fassung v2): Ticks ueber Orientierungsdeterminanten mit Nullstellensuche sind eine wohldefinierte, schrittweitenunabhaengige Zaehlung. Die Definition aus v1 (Zaehler pro Delta t) ist es nicht.
- §7, "Rotation kann stabilisieren": Im Federring F1 stabilisiert die Rotation tatsaechlich, durch Zug statt Stauchung.
- §2 und §9: Auf dem Rad-Graphen gibt es Q-Ball-artige, phasenrotierende lokalisierte Moden. Das Kriterium "stabil bei fester Ladung" mit Zaehlung der negativen Richtungen funktioniert diskret ohne Ausnahme.

**Traegt nicht oder bleibt offen:**

- Sonderrolle von 11 oder 19: in keinem Versuch. Wo eine Schwelle auf 11 fiel (Zentrumsmode bei J = 0,05), ist sie eine stetige J-N-Schwelle.
- "Ab kritischem Omega instabil": nicht gefunden. Stabilitaet haengt am Spannungszustand (Ruhelaengen), N wirkt nur ueber die Geometrie.
- Kontinuumsfenster (1/2; 1): Es uebertraegt sich nicht auf ein grobes Gitter. Die Bruecke aus §9a (stille Stelle, a -> 0) bleibt der eigentliche Test und wurde hier nicht gerechnet.
- Tickrate als Uhr: nu = 6,1 ist eine Eigenschaft der gewaehlten Bewegung. Ein Zusammenhang mit Energiedichte oder Eigenzeit wurde nicht geprueft [H bleibt H].
- Das "+1"-Zentrum ist fuer lokalisierte Feldmoden der unguenstigste Ort: Es koppelt an alle N Ringknoten.

## 4. Laufzeiten, sha256, Selbstanzeigen, Grenzen

**Laeufe auf der .69** (Service-Laufzeit laut systemd; Start/Ende UTC):

| Lauf | Spur | Ende (UTC) | Laufzeit | Status |
|---|---|---|---|---|
| v1_tetra.py | cpu | 06:30:31 | 2 min 54 s | ok |
| v2_maxwell.py | cpu2 | 06:37:38 | 10 min 0 s | **abgebrochen (Zeitlimit), kein JSON** |
| v4_ticks.py | cpu | 06:33:31 | 2 min 7 s | ok |
| v3_federring.py | cpu | 06:43:31 | 10 min 0 s | **abgebrochen (Zeitlimit), kein JSON** |
| v5_feld.py | cpu2 | 06:40:59 | 3 min 21 s | ok |
| v2b_maxwell.py teil1 | cpu | 06:44:02 | 31 s | ok |
| v2b_maxwell.py teil2 | cpu | 06:46:21 | 2 min 19 s | ok |
| v2b_maxwell.py zeit | cpu2 | 06:47:01 | 6 min 2 s | ok |
| v3b_federring.py F1 | cpu | 06:47:35 | 1 min 15 s | ok |
| v5b_feld.py (Nachtrag) | cpu2 | 06:47:33 | 32 s | ok |
| v3b_federring.py F0 | cpu2 | 06:48:41 | 1 min 8 s | ok |
| plot.py (zweimal, Beschriftung berichtigt) | cpu | 06:49:23 | 6 s | ok |

Logs: aus/logs/. Laufordner auf der .69: /home/fmh/fmhc-physics-remote/runde16-ausprobieren/.

**sha256** (Code wie gelaufen, plot.py in der berichtigten Fassung):

```
e636a5570cf63a1718a1776d34cb970168885258a81b27f3e36c6d687d41499c  code/v1_tetra.py
529c5b790abd9d9649a0f100eb450275fa878afb9b768e55b97ba7aa5e4a65b1  code/v2_maxwell.py
021ce07627af9019841d51f636b3d6544b1f5f91aacf80a758a39501b82f5889  code/v2b_maxwell.py
621a3652557dfe772f20d84de4af23bb20395119e60018b25e519532a17002a3  code/v3_federring.py
987f3d31d95426bae69dda415656910b772035567791d5efa52b2e2c620b63e5  code/v3b_federring.py
29bca8368cc3621a4c7bcc3b26484d6d75e51c4b8ae4ac694b2729c501b932a5  code/v4_ticks.py
85b2cc60614e46b9fdd7b2cb83ff074059780de0af64a61d5a5d54db8a3d912c  code/v5_feld.py
d4a39bda4506bf7d65f3121db67f2b53a6921f157702e9b5326c5732a885d097  code/v5b_feld.py
4a13a58716bf683d1fafbe0c6b598838eeb563237ed5ba1b6ac2a0e24d5fdeec  code/plot.py
cdf1bc3f7530ab7afabf712e7992ad5cb8f027c8a421839b218b7b426336ce58  aus/v1_tetra.json
0ad2126ae1fa166a08d1e90232e6f6cac02430545367bd8ba0df0a216bc5eda1  aus/v2b_teil1.json
b24b073ea4444099c56b6fe11d590b249f3cd2e77170e3db952c194c807e4984  aus/v2b_teil2.json
de1bbb2d12408239b3e95055e1682c6b4d7817aad8d14fd137a504aef646a3fc  aus/v2b_zeit.json
0597ed3fbd2619ba91cea26a4bc500758fe904ddd64db6b5021c1a8d8c2dadce  aus/v3b_F0.json
fcb5a3538fe696ddbf47a6097be20b9c42d342e331a5a65c0a8f4dbbcd761994  aus/v3b_F1.json
32989ecc7d209c4db065176e8d63ed6dfc04f33a936925ec7e55c37f2bcf76a9  aus/v4_ticks.json
7d1ef12b9898bf4fd23f1fdcc228db4dec7a2de0175ec40be51718e8d348d8db  aus/v5_feld.json
155ba5a5bbb06a67b5b438570349e40ea86210a3bfa85d38876958acdce7c9bc  aus/v5b_feld.json
1c88b74f8da45508ab1449c51439c0b663b958b504468f4c9a61efdfa0b2e909  PLAN.md.eingefroren-20261002-082314
```

**Selbstanzeigen:**

1. Laufzeit unterschaetzt: Die ersten .69-Laeufe von V2 und V3 liefen in das 600-s-Limit von kleintest.sh und schrieben kein JSON.
   - Ursache: BLAS-Threads gegen CPUQuota 100 %, etwa 20-fach langsamer.
   - Wiederholt als v2b/v3b mit einem Thread, aufgeteilt, sonst gleicher Code. Die eps_c-Werte des abgebrochenen Laufs sind bitgleich reproduziert.
2. V5-Rauchtest, erste Fassung mit zwei Fehlern, behoben vor dem .69-Lauf:
   - Newton fiel auf die Nullloesung.
   - Das Stabilitaetskriterium ignorierte die Zahl der negativen Richtungen.
3. Vorab-Test fuer V5 schlecht geplant: N = 8..21 gab 11 und 19 keine volle Nachbarschaft. Der Nachtrag v5b entstand nach Sicht der V5-Ergebnisse und ist nicht eingefroren.
4. V3: Die vorab gewaehlten Kennzahlen Omega_c und S(N) erwiesen sich als entartet bzw. rauschdominiert. Omega_stab und das 3D-Raster sind nachtraeglich.
5. Planabweichungen (alle in PLAN.md, Nachtrag):
   - V1: mehr dt-Werte.
   - V2: Methode B ohne Drehpaar eingestuft (FD-Rauschboden 1e-5); Fit-Bereich in v2b 25..64 statt 20..64. Der Plan-Bereich ist aus dem Log des abgebrochenen Laufs belegt.
6. Lokal liefen 15 Rauchtests (je <= 34 s, nice 19, ein Thread). Einige lieferten schon Physikzahlen; berichtet sind nur .69-Zahlen.
7. Auf der .69 liegt zusaetzlich code/plot2.py, eine Kopie der berichtigten plot.py fuer den zweiten Plot-Aufruf.

**Grenzen:**

- V2: nur ebene Kreis-Relativgleichgewichte gleicher Massen. 3D nur an den Tabellenpunkten und bei 0,99 eps_c. Maxwells Vorfaktor [L?].
- V3: nur k_s = k_r, Einheitsmassen, zwei Ruhelaengenwahlen; keine Zeitentwicklung; keine Krein-Signaturen ausgegeben.
- V4: eine Bewegung, ein Seed. Die Ereignissuche setzt hoechstens einen Vorzeichenwechsel je Schritt voraus. nu gilt nur fuer diese Bewegung.
- V5:
  - J gleich und Geometrie fest; die Kopplung J(|x|) aus v2 §2 ist nicht eingebaut.
  - omega^2-Raster 0,005, also Fenstergrenzen auf +-0,005.
  - Die Fortsetzung in J kann Aeste an Falten verfehlen (J = 0,2, N = 20 bei omega^2 = 0,74).
  - Stabil heisst spektral stabil bei fester Ladung. Zeitentwicklung nur fuer sechs Faelle bis T = 500.

## 5. Einfach gesagt

Wir haben fuenf kleine Rechenversuche gemacht. Der Pruefstein klappt: Wie Maxwell 1859 findet unser Programm, dass ein Ring aus Monden um einen Planeten erst ab sieben Monden stabil sein kann, und nur wenn die Monde sehr leicht sind. "Ticks", also die Augenblicke, in denen eine Ecke oder Kante durch den anderen Koerper stoesst, kann man exakt zaehlen, wenn man jeden Zeitpunkt genau ausrechnet; wer nur Schnappschuesse vergleicht, verliert Ereignisse. Auf dem Rad-Netz gibt es kleine stabile Feldklumpen wie Mini-Q-Baelle, aber fast nur auf dem Ring, die Nabe haelt bei vielen Speichen keinen. Die Zahlen 11 und 19 waren in keinem Versuch etwas Besonderes.
