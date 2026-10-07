# KAUSAL-4D-SCHICHT-2: Ergebnis (Code-Agent fuer die Leitung, Runde 39, explorativ)

- Gerechnet auf der .69 nur ueber kleintest.sh, Spuren cpu6 und p4000a, jeweils CPU mit einem Gewinde; die GPU der
  p4000a-Spur blieb unbenutzt. Hoechstens zwei Laeufe zugleich.
- **Zeiten** (date; .69 in UTC, CEST = UTC + 2):
  - Start 10:00:08 CEST. Rauch 08:12:33 bis 08:16:34 UTC. Plantext ab 10:17:40 CEST.
  - **Eingefroren 10:19:56 CEST:** PLAN.md.eingefroren-20261004-101956, code/*.eingefroren-20261004-101956, sha256 in
    code/pruefsummen-einfrieren.txt.
  - Hauptlaeufe 08:20:02 bis 08:47:39 UTC, alle rc = 0, kein Abbruch vor einer Saat:
    - drei Pollaeufe, Erwartung, vier Feldlaeufe, Auswertung
    - dazu eine Pfadprobe der Auswertung auf drei Saaten (08:40:48 UTC) und eine Zusatzprobe nach dem Befund (08:32:31
      UTC, Selbstanzeige 1)
  - Text ab 10:50:55 CEST.
- **Hashes:**
  - Alle 12 Felddateien tragen die sha256 des eingefrorenen schicht2_feld.py (99ced10d...).
  - Die drei Poldateien und erwartung.json tragen die des eingefrorenen schicht2_kont.py (7b05d976...).
  - auswertung.json traegt die des eingefrorenen schicht2_auswertung.py (c5627157...).
  - Plan und alle fuenf Codedateien waren nach den Laeufen unveraendert (sha256sum -c um 10:47 CEST, lokal und auf der .69).
  - **Nach dem Einfrieren wurde kein eingefrorener Code geaendert.** Neu ist nur code/zusatz_lokalisierung.py (63b09f7b...),
    eine getrennte Probe ohne Urteilskraft.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier aus zweiter Hand: SCHICHT-1 mit Gegenlesen, Dossier/Arbeitsfeld KAUSAL-4D-STABIL-L)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [E] hier gerechnet (synthetisch, keine Messdaten); [F] Festlegung des Plans

## 1. Ergebnis zuerst

1. **Die dritte Schicht stellt auch die naechste Ordnung ab, im Mittel [E, M].**
   - Aus Normierung, sigma = 0 und dem Verschwinden der naechsten Ordnung folgt eindeutig V-00 = (3, -7, 4) a.
   - Der Massenschalen-Pol liegt bei rho = 16 (k = 0) bei Im omega = 4,36e-4. Bei V-0 waren es 0,0147, bei V-J 0,152.
   - Von rho = 4 bis 16 faellt er um den Faktor 9,69 (V-0: 4,77). In rho ist die Steigung -1,6 (V-0 -1,13, V-J -0,35).
     Jede Schicht senkt den Exponenten also um etwa 1/2.
   - **Die Restformel vorab, eps M^8/(16 rho omega), trifft auf 3 bis 4 % bei allen drei Dichten.**
2. **Keine neuen Nullstellen, kleinerer fester Abstand [E].**
   - In abs(omega) < 10 und Im omega > 0,05 hat V-00 bei keiner Dichte eine Nullstelle (S2-3).
   - Die Erwartung liegt an den Pruefpunkten nur 10 bis 12 % ueber dem Kontinuum (V-0: 21 bis 29 %). Vorab hatte ich aus
     M^2 = m^2/(1 - eps m^2/2) etwa die Haelfte erwartet (~8 %).
3. **Der Preis ist Rauschen, und es waechst mit jeder Ordnung und mit der Laufzeit [E].**
   - Relative Streuung je Saat bei rho = 16: 0,31 (V-J), 0,64 (V-0), 1,61 (V-00), also die Faktoren 2,05 und 2,53 je
     Ordnung. Vorab geschaetzt hatte ich 1,6.
   - Bei V-00 ist die Streuung eines Einzelnetzes groesser als das Signal (sd/abs(E) = 1,45).
   - Sie waechst mit der Zeit: sd/abs(E) 1,15 / 1,47 / 1,81 bei t = 2,0 / 2,6 / 3,2. Bei V-0 sind es 0,47 / 0,48 / 0,59.
     Die Norm je Saat waechst um 1,4 bis 1,6, das Mittel bleibt flach.
4. **Urteile:** S2-0, S2-2 und S2-3 eingetroffen. **S2-1 ist nach dem eingefrorenen Plan "nicht auswertbar"**:
   - Bei rho = 4 hat die aus SCHICHT-1 uebernommene Gittersuche die gezaehlte Nullstelle nicht lokalisiert. Sie liegt nur
     0,0022 ueber dem unteren Rand der Region S.
   - Die Werte selbst erfuellen beide Teile (4,36e-4 < 0,004; 9,69 > 4,77). Eine Zusatzprobe nach dem Befund bestaetigt
     die Nullstelle. Das zaehlt nicht als Urteil (Selbstanzeige 1).
5. **Bedeutung [E, H]:** Im Mittel laesst sich das Anwachsen Ordnung fuer Ordnung abstellen.
   - Jede Ordnung kostet eine exakte Bedingung (Feinabstimmung, B4) und etwa den Faktor 2,5 im Rauschen.
   - Bei V-00 beherrscht das wachsende Rauschen das Einzelnetz. Die Grenze des Schemas setzt also das zweite Moment,
     nicht mehr das Mittel [H].

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 10:19:56 CEST) durch code/schicht2_auswertung.py; Werte in lauf-69/auswertung.json.
- Die Felder "vermerk" und bei S2-1 "werte_beschreibend_ohne_urteilskraft" sind per jq nachgetragen.
- Ohne sie ist die Datei inhaltsgleich mit lauf-69/auswertung.maschine.json (sha256 der sortierten Ausgabe geprueft:
  41bf1de0...).

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| S2-0 | V-0 gibt den SCHICHT-1-Pol wieder (0,0147 bei rho = 16, k = 0, auf 1e-3) | 90 % | **eingetroffen** | 1,060585 + 0,014701 i; Abstand zum Kartenwert 9,7e-7, zum SCHICHT-1-Wert 5e-18 |
| S2-1 | [H] V-00: Pol bei rho = 16 mit Im omega < 0,004 (oder keiner nahe der Schale), faellt von rho = 4 bis 16 schneller als V-0 | 45 % | **nicht auswertbar** | Gitterlokalisierung bei rho = 4 gescheitert (PLAN 7.2). Werte ohne Urteilskraft: 4,36e-4; Faktor 9,69 gegen 4,77 |
| S2-2 | [H] Streuung je Saat bei V-00 groesser als bei V-0 (0,636) | 70 % | **eingetroffen** | s_V00 = 1,609, s_V0 = 0,636 (Faktor 2,53) |
| S2-3 | Keine weitere Nullstelle mit Im omega > 0,05 bei abs(omega) < 10 fuer V-00 | 60 % | **eingetroffen** | N_A = 0 in allen sechs Faellen (rho = 4, 8, 16; k = 0, p), alle stabil |

- **S2-1 im Einzelnen** (PLAN 7.2):
  - Die Zaehlungen sind stabil. Bei V-00, rho = 4, k = 0 zaehlt das Argumentprinzip in S genau eine Nullstelle.
    Lokalisiert werden null. Damit sind "lokalisiert = gezaehlt" und die Konsistenz der Schalennullstelle verletzt;
    beides steht in 7.2 als Grund fuer "nicht auswertbar".
  - **Ursache:** Die Gittersuche aus SCHICHT-1 nimmt die Randzeilen nicht als Kandidaten. In S beginnt das Gitter bei
    Im = 0,002 in Schritten von 0,01.
    - Die Schalennullstelle liegt bei 1,064164 + 0,004223 i, naeher an der Randzeile 0,002 als an der Zeile 0,012.
    - Das Minimum von abs(g) liegt deshalb auf dem Rand und wird verworfen.
    - Bei V-J und V-0 (Im >= 0,0132) trat das nicht auf. Dasselbe gilt fuer k = p (Im 0,0038), das nur beschreibend ist.
  - **Werte** (aus derselben Rechnung, ohne Urteilskraft):
    - (a) Im(V-00, 16, 0) = 4,360e-4 < 0,004, Blatt I. In S0 gezaehlt (1) und lokalisiert (1); in S keine Nullstelle.
    - (b) F_00 = 0,0042228/0,00043596 = 9,686 > F_0 = 0,070136/0,014701 = 4,771.
  - **Zusatzprobe nach dem Befund** (lauf-69/kont/zusatz-lokalisierung.json):
    - Im Rechteck [0,914; 1,214] x [0,002; 0,05] um die Schalennullstelle liegt genau eine Nullstelle (stabil). S hat
      insgesamt genau eine.
    - Newton auf g_I (statt F) ab der Schalennullstelle bleibt dort (6e-17).
    - Die gezaehlte S-Nullstelle ist also die Schalennullstelle.
  - **Nach Kartenwortlaut** (nur die Werte, ohne die Konsistenzregeln des Plans) waere S2-1 eingetroffen. Massgeblich ist
    das Urteil nach dem eingefrorenen Plan: nicht auswertbar.
- **Kartenwortlaut sonst:** Die Karte enthielt keinen Fehler (PLAN 9). S0 und die Schalennullstelle ueber beide Blaetter
  sind Ergaenzungen, A und S sind unveraendert. Fuer S2-0, S2-2 und S2-3 sind die Urteile nach Wortlaut dieselben.
- **Meine Vorab-Erwartung** (PLAN 6): S2-0 ein (99 %), S2-1 ein (80 %), S2-2 ein (85 %, Schaetzung 1,6), S2-3 ein (65 %).
  - Die Korrekturen zur Restformel hatte ich mit 10 bis 25 % bei rho = 4 zu gross geschaetzt; es sind 3 %.
  - Das Rauschen traf ich (1,609).
  - Die Grenze der Gittersuche nahe dem Rand von S habe ich nicht vorhergesehen, obwohl mein Plan V-00 bei rho = 4 genau
    dort erwartete (4,4e-3).
- **Bedeutung nach der Karte (vorab):** Formal ist keine der beiden Zeilen ausgeloest, weil S2-1 nicht auswertbar ist.
  - Die Werte stuetzen "S2-1 trifft ein: Das Anwachsen laesst sich Ordnung fuer Ordnung abstellen, mit je einer exakten
    Bedingung an die Schichtgewichte".
  - Mit S2-2 ist der Preis "mehr Rauschen je abgestellter Ordnung" eingetroffen. Wie weit man gehen kann, beschraenkt
    das Rauschen schon bei V-00 (Abschnitt 6).

## 3. Tabellen

### 3.1 Massenschalen-Nullstellen von 1 + m^2 k~_gen [E, M]

Newton auf der fortgesetzten Funktion F, Zaehlung per Argumentprinzip (PLAN 3). Alle 18 liegen auf Blatt I (Wachstum).

| rho | k | V-J | V-0 | V-00 |
|---|---|---|---|---|
| 4 | 0 | 1,01726 + 0,24579 i | 1,12246 + 0,070136 i | 1,06416 + 0,0042228 i |
| 8 | 0 | 1,04216 + 0,19776 i | 1,08838 + 0,032213 i | 1,04158 + 0,0013248 i |
| 16 | 0 | 1,05453 + 0,15232 i | 1,06059 + 0,014701 i | 1,02771 + 0,00043596 i |
| 4 | p | 1,13765 + 0,21978 i | 1,23717 + 0,063633 i | 1,18490 + 0,0037925 i |
| 8 | p | 1,16189 + 0,17738 i | 1,20662 + 0,029056 i | 1,16466 + 0,0011848 i |
| 16 | p | 1,17434 + 0,13678 i | 1,18167 + 0,013195 i | 1,15227 + 0,00038884 i |

- p = sinh 0,5 = 0,521. V-J und V-0 sind dieselben wie in SCHICHT-1, nach neuer und alter Regel (Abstand <= 5e-16).
- **Verhaeltnis Numerik/Schreibtisch** (erste nichtverschwindende Ordnung, PLAN 2), k = 0, rho = 4 / 8 / 16:
  - V-J (sqrt 6/4) m^4/(omega sqrt rho): 0,803 / 0,913 / 0,995
  - V-0 3 M^6/(16 rho omega): 0,870 / 0,949 / 0,971
  - **V-00 eps M^8/(16 rho omega): 0,968 / 0,958 / 0,961**
  - Bei k = p fuer V-00: 0,970 / 0,959 / 0,962.
- **Abfall mit rho** (k = 0):

  | Variante | Faktor 4 zu 16 | Steigung log Im/log rho, 4 zu 8 | 8 zu 16 | asymptotisch [M] |
  |---|---|---|---|---|
  | V-J | 1,61 | -0,31 | -0,38 | -1/2 |
  | V-0 | 4,77 | -1,12 | -1,13 | -1 |
  | V-00 | 9,69 | -1,67 | -1,60 | -3/2 |

  - Die Abweichung von der Asymptotik kommt aus den M-Faktoren: M^2 = m^2/(1 - eps m^2/2) faellt mit rho.
- **Re omega:** V-00 liegt bei 1,064 / 1,042 / 1,028 (k = 0), V-0 bei 1,122 / 1,088 / 1,061. Die Verschiebung ist also
  etwa halbiert, wie die Konstante -eps/2 statt -eps vorhersagt.
- **V-00 gegen V-0 bei rho = 16:** Im omega ist 34-mal kleiner (Formel: (eps/3) M^2, also 33-mal), gegen V-J 349-mal.
- Bild lauf-69/pole.png:
  - oben die omega-Ebene bei k = 0 und k = p
  - unten links die Schalennullstellen bei k = 0 in symlog-Lupe, mit den Grenzen 0,004 (S2-1) und 0,002 (S/S0)
  - unten rechts abs(Im omega) gegen rho, log-log, mit den Schreibtischformeln

### 3.2 Zaehlungen [E]

| Variante | N_A (alle 6 Faelle) | N_S | N_S0 | weitere | stabil | lokalisiert = gezaehlt |
|---|---|---|---|---|---|---|
| V-J | 2 (Schalenpaar) | 1 | 0 | 0 | 18/18 | 18/18 |
| V-0 | 2 bei rho = 4 (Schalenpaar), sonst 0 | 1 | 0 | 0 | 18/18 | 18/18 |
| V-00 | 0 | 1 bei rho = 4, sonst 0 | 0 bei rho = 4, sonst 1 | 0 | 18/18 | 16/18 (S bei rho = 4, k = 0 und p: 0 statt 1) |

- Zaehlungen: Variante mal 3 Dichten mal 2 k mal 3 Regionen.
- Groessenprobe: max abs(m^2 k~) auf abs(omega) = 10 ist bei V-00 0,0066 / 0,011 / 0,021 (rho = 4 / 8 / 16), auf
  abs(omega) = 20 <= 2,1e-4. Ausserhalb der Kontur gibt es also keine Nullstellen.
- B7 gilt weiter: Nullstellen mit 0 < Im omega <= 0,05 ausserhalb von S und S0 (Re omega ausserhalb [0,5; 2]) sieht keine
  Zaehlung.

### 3.3 Pruefpunkte: Saatmittel, Erwartung und Kontinuum, rho = 16, 12 Saaten [E, M]

Je Variante die Spannweite ueber die 18 Pruefpunkte; dieselben Streuungen fuer alle Varianten.

| Variante | abs(Saatmittel)/abs(K) | abs(E)/abs(K) [M] | in 3 SE von E | groesste Abw. von E | in 3 SE von K |
|---|---|---|---|---|---|
| V-J | 1,20 bis 1,83 | 1,29 bis 1,63 | 18 | 1,97 SE | 0 |
| V-0 | 1,00 bis 1,58 | 1,21 bis 1,29 | 18 | 1,66 SE | 17 |
| V-00 | 0,50 bis 1,54 | 1,10 bis 1,12 | 18 | 1,61 SE | 18 |

- K ist die gekappte direkte Faltung. Die Zeilen V-J und V-0 sind dieselben wie in SCHICHT-1 (bitgleiche Felder).
- **Monte Carlo gegen Formel:** 54 von 54 Punkten in 3 SE der eigenen Erwartung. Das prueft Code und verallgemeinerte
  Erwartungsformel auch fuer die 2-Element-Spruenge.
- **Fester Abstand:** abs(E)/abs(K) liegt bei V-00 an allen Punkten bei 1,10 bis 1,12 und ist in t flach (1,097 / 1,116 /
  1,113 bei t = 2,0 / 2,6 / 3,2). Vorab erwartet hatte ich ~M^3/m^3 = 1,08 plus wenig Wachstum (PLAN 2).
- Dass V-00 das Kontinuum an 18 von 18 Punkten "trifft", liegt vor allem am grossen SE und ist kein Beleg fuer
  Kontinuumsnaehe des Einzelnetzes.
- Bild lauf-69/saatmittel_erwartung_kontinuum.png: Profil bei t = 3,2, je Variante und Konfiguration.

### 3.4 Streuung je Saat [E]

s ist das geometrische Mittel von sd/abs(K) ueber die 18 Pruefpunkte; daneben je Zeitpunkt (6 Punkte) und bezogen auf
abs(E_v).

| Variante | s (rho = 16) | s gegen abs(E) | sd/abs(K) bei t = 2,0 / 2,6 / 3,2 | sd/abs(E) bei t = 2,0 / 2,6 / 3,2 |
|---|---|---|---|---|
| V-J | **0,310** | 0,214 | 0,277 / 0,299 / 0,359 | 0,212 / 0,208 / 0,223 |
| V-0 | **0,636** | 0,508 | 0,563 / 0,605 / 0,756 | 0,465 / 0,478 / 0,589 |
| V-00 | **1,609** | 1,451 | 1,261 / 1,637 / 2,018 | 1,148 / 1,468 / 1,813 |

- Faktor je Ordnung: V-0/V-J = 2,05, V-00/V-0 = 2,53, V-00/V-J = 5,19.
- **Schaetzung vorab** (PLAN 2): s ~ sqrt(sum x_n^2 L_n/L_0), geeicht an V-0, gab 1,6. Getroffen: 1,609.
- **Zeitgang:** Bei V-J waechst das Rauschen mit dem Mittel (sd/abs(E) flach). Bei V-00 waechst es schneller als das
  Mittel: sd/abs(E) steigt um den Faktor 1,58 von t = 2,0 bis 3,2, bei V-0 um 1,27.
- Je Punkt bei V-00 0,96 bis 2,35. Bild lauf-69/streuung_varianten.png (die Achsenbeschriftung links ist abgeschnitten).

### 3.5 Norm je Zeitscheibe gegen Kontinuum, R = Saatmittel(n)/n_c, G = R_4/R_1 [E, beschreibend]

| Variante | R (eta = 0) in den vier Scheiben | G eta 0 / 0,5 | G je Saat Median eta 0 / 0,5 |
|---|---|---|---|
| V-J | 2,21 / 2,49 / 2,81 / 3,36 | 1,52 / 1,55 | 1,58 / 1,64 |
| V-0 | 2,30 / 2,36 / 2,23 / 2,35 | 1,02 / 1,07 | 1,01 / 1,08 |
| V-00 | 5,66 / 6,21 / 6,05 / 8,27 | 1,46 / 1,69 | 1,42 / 1,64 |

- Die Norm enthaelt die Rauschleistung im ganzen Scheibenvolumen. Bei V-00 ist sie grob zu ~80 % Rauschen (R ~ 6 gegen
  abs(E)^2/abs(K)^2 ~ 1,2).
- **Das Einzelnetz waechst in der Norm bei V-00 wieder etwa so stark wie bei V-J**, obwohl das Mittel praktisch nicht
  mehr waechst. Ursache ist das wachsende Rauschen, nicht der Pol [E; Deutung H].

### 3.6 Zuwachs [E, beschreibend; nach B2 kein Polmass]

Z = [abs(E)/abs(K)](t = 3,2)/[abs(E)/abs(K)](t = 2,0) an Lage A, aus der Erwartung.

| rho | V-J eta 0 / 0,5 | V-0 eta 0 / 0,5 | V-00 eta 0 / 0,5 |
|---|---|---|---|
| 4 | 1,334 / 1,323 | 1,200 / 1,177 | 1,044 / 1,035 |
| 8 | 1,298 / 1,277 | 1,115 / 1,100 | 1,022 / 1,016 |
| 16 | 1,247 / 1,224 | 1,064 / 1,055 | 1,014 / 1,011 |

- Vom Pol allein erwartet man bei V-00 ln Z = 1,2 Im omega = 5e-4 (rho = 16); gemessen ist 0,0143. Der Fensterzuwachs
  stammt also fast ganz aus anderen Anteilen (Schnitt, Einschwingen), wie B2 fuer V-0 fand.
- Sein Gang mit rho ist flacher als der des Pols (ln Z: 0,043 / 0,022 / 0,014).
- Aus den Saatmitteln ist der Zuwachs bei V-00 sinnlos (1,52 bzw. 0,79), weil die Streuung je Saat ueber 100 % liegt.
- Bild lauf-69/zuwachs_t.png: links abs(E)/abs(Kontinuum) auf der Achse fuer t = 0,4 bis 4,0, rechts die Norm.

### 3.7 Schichtzahlen, rho = 16 [E, M]

| Groesse | Mittel +- SE (12 Saaten) | Erwartung [M] | Abw. |
|---|---|---|---|
| L0/N | 105,15 +- 0,23 | 105,370 | -0,97 SE |
| L1/N | 46,37 +- 0,11 | 46,476 | -0,94 SE |
| L2/N | 32,33 +- 0,08 | 32,404 | -0,94 SE |

- 2-Element-Intervalle sind 31 % der Links, 1-Element-Intervalle 44 %.
- max abs(phi): V-J 0,77, V-0 1,16, V-00 1,70. Alle 12 Saaten endlich.

## 4. Kontrollen

- **Codeprobe** (rho = 1,2, N = 1 511, L0 = 33 120, L1 = 12 289, L2 = 7 535, Bloecke 256):
  - drei Schichten aus dem GEMM gleich dichtem C C (float64): ja, ja, ja; C gleich Koordinaten: ja
  - Rekursion gegen dichte Loesung <= 4,6e-16, Reihe <= 5,5e-16 (alle drei Varianten)
  - Zuschauer gegen eine Schleife, die die Elemente in I(y, p) explizit zaehlt: <= 4,1e-15
- **Repro gegen SCHICHT-1:** V-J und V-0 auf allen 12 Hauptsaaten und auf der Rauchsaat 91 bitgleich (phi an den
  Zuschauern und Normsummen). Damit sind auch s_VJ = 0,310 und s_V0 = 0,636 dieselben.
- **Argumentprinzip:**
  - synthetische Probe A 3/3, S 1/1, S0 1/1 (mit polartiger Stelle bei 0,52 auf der Achse), S ohne Nullstelle 0/0
  - alle 54 Zaehlungen stabil (zwei Aufloesungen gleich)
  - lokalisiert gleich gezaehlt in 52 von 54; die zwei Ausnahmen in 3.2 und Abschnitt 2
- **Schalennullstelle:** Gegenstart omega_0 - 0,02 i trifft in allen 18 Faellen dieselbe Nullstelle (<= 2,3e-16). Bei
  V-J und V-0 ist sie gleich der Nullstelle nach der alten Regel.
- **Zweites Blatt:** abs(g_I(x + i e) - g_II(x - i e)) <= 4,9e-5 bei e = 1e-6 und <= 4,9e-7 bei e = 1e-8, linear in e.
- **Moment- und Sprungprobe:** 4 pi S_1 = 1 auf 7e-15. Bei V-00 S_3 und S_5 auf Rundungsniveau null, S_7 = a/(4c^2) wie
  analytisch (<= 4,4e-13 bezogen auf das Betragsintegral). D(i y) geteilt durch den Term y^4 geht gegen 1 (0,99971 bei
  y = 0,05).
- **Quadratur:**
  - Schalennullstelle mit 256 statt 128 tau-Knoten <= 3,1e-15; Bogen <= 2,4e-15
  - Erwartung mit 128 statt 64 Knoten (V-0, V-00 bei rho = 4) <= 1,7e-12
- **Erwartung:**
  - Gamma 0,8 gegen 1,4 <= 3,8e-14 in allen neun Faellen
  - rho = 10^6 gegen den k-Raum: V-J 0,72 %, V-0 0,093 %, V-00 0,046 %. Alle drei haben denselben Kontinuumsgrenzfall;
    das prueft die Normierung numerisch.
- **Zusatzprobe nach dem Befund** (ohne Urteilskraft): siehe Abschnitt 2.
- **Laufzeit und Speicher:** 129 bis 141 s je Saat (rho = 16), Hoechststand 2,04 GB unter MemoryMax 4G. Pollaeufe 183 bis
  229 s, Erwartung 264 s.

## 5. Latten (v3)

- **L1 (kann scheitern):** ja.
  - S2-1 haette scheitern koennen: Vorzeichen, weitere Nullstellen nahe der Schale oder ein langsamerer Abfall.
  - S2-3: Die Koeffizienten von V-00 sind groesser und wechseln zweimal das Vorzeichen; meine Vorab-Erwartung war 65 %.
  - S2-2 haette an Ausloeschungen scheitern koennen.
  - Die Restformel war vorab mit Zahlen angegeben (PLAN 2) und haette daneben liegen koennen.
- **L2 (Gegenprobe):**
  - dichte Schichten, Koordinaten, dichte Loesung, Reihe, Zuschauerschleife
  - Repro bitgleich auf 13 Saaten
  - zwei Aufloesungen, synthetische Windung, Lokalisierung, Gegenstart, alte gegen neue Regel, Blattstetigkeit
  - Moment- und Sprungprobe, zwei tau-Quadraturen, zwei Gamma, rho = 10^6
  - Monte Carlo gegen Formel (54 Punkte), Schreibtischformel gegen Numerik
- **L3 (Numerik):** Code <= 4,1e-15; Pole <= 3,1e-15; Momente <= 4,4e-13; Erwartung <= 3,8e-14 (Gamma) bzw. 1,7e-12
  (Quadratur); Grenzfall rho = 10^6 <= 0,72 %.
- **L4 (schon bekannt):**
  - Johnstons Pfadsumme, a und b [S, ueber KAUSAL-WELLE-4D].
  - Schichtsummen mit wechselnden Vorzeichen und Summe 0 bei den BD-Operatoren, 4D: (1, -9, 16, -8) mal 4/sqrt 6
    [S, Surya 2019 laut Gegenlesen SCHICHT-1]; Bedingungen an die Koeffizienten fuer den IR-Grenzfall bei ASS [S, nur
    Abstract laut Gegenlesen].
  - Momentbedingungen Ordnung fuer Ordnung sind dort das Werkzeug fuer den Grenzfall des Operators [L?].
  - Fuer Johnstons Propagator-Pfadsumme, um das Anwachsen an der Massenschale abzustellen, ist so etwas nach Lesestand
    nicht gefunden (wie SCHICHT-1, B10); selbst gesucht habe ich nicht.
- **L5 (Messbezug):** keiner (synthetisch, eine lineare Welle, Laufstrecke 2/m).
  - Hochrechnung [M, ungeprueft]: Der V-00-Rest je Eigenzeit ist (sqrt 6/(32 pi)) m^7 l^6. Fuer einen Higgs-schweren Skalar
    bei l = l_P waeren das ~4e59 Weltalter je e-Faltung (V-0: ~6e24).
  - Fuer das Mittel war V-0 also schon mehr als genug. Physikalisch zaehlen hier die Feinabstimmung und das Rauschen.

## 6. Bedeutung

- **Gezeigt [E, M]:**
  - Im Mittel steuern die Momente L_j das Anwachsen. Jede verschwindende Momentbedingung hebt den Rest um eine Ordnung in
    m^2/sqrt(rho).
  - V-J, V-0 und V-00 folgen den Formeln pi eps m^4/(2 omega), (pi^2 eps^2/8) M^6/omega und (pi^2 eps^3/24) M^8/omega.
    Bei rho = 16 treffen die Formeln auf 0,5 %, 3 % und 4 %.
  - Mit der Ordnung faellt auch der feste Abstand zum Kontinuum: 21 bis 29 % bei V-0, 10 bis 12 % bei V-00.
- **Einschraenkungen:**
  - **Feinabstimmung (B4):** V-00 braucht zwei exakte Bedingungen. Eine Restabweichung delta-sigma bringt den Term erster
    Ordnung zurueck, eine Abweichung in sum a_n Gamma(n + 3/2)/n! den m^6-Term [M].
  - **Rauschen:** Die Streuung je Saat waechst je Ordnung um 2,05 und 2,53.
    - Bei V-00 ist sie groesser als das Signal und waechst mit der Laufzeit schneller als das Mittel.
    - In der Norm waechst das Einzelnetz bei V-00 wieder um 1,4 bis 1,6, etwa so wie V-J.
  - **[H] Deutung:** Die Momentbedingungen wirken auf den Erwartungskern sum a_n mu_n. Die Varianz haengt an Quadraten der
    Amplituden und an Paaren von Pfaden; diese Bedingungen erreichen sie nicht. Moeglicherweise hat das zweite Moment
    eigene wachsende Moden. Dann setzt es die Grenze des Schemas. Geprueft ist das nicht.
  - Nur rho = 16 fuer die Felder, Laufstrecke 2/m, zwoelf Saaten.
- **Naechste Ordnung [M, H]:**
  - Vier Schichten mit Normierung und L_0 = L_1 = L_2 = 0 ergeben eindeutig (4, -16, 20, -8) a. Am Schreibtisch
    nachgerechnet: Normierung 4 - 8 + 7,5 - 2,5 = 1; Summe 0; 16 x_0 + 24 x_1 + 30 x_2 + 35 x_3 = 64 - 384 + 600 - 280 = 0;
    sum x_n (n + 1) = 4 - 32 + 60 - 32 = 0.
  - Nach derselben groben Schaetzung waere das Rauschen nochmals ~2,7-mal groesser, s ~ 4 [H]. L3/L0 ist dafuer nur
    geschaetzt (0,23).
- **Fuer die Karte:** "Ordnung fuer Ordnung abstellbar" traegt im Mittel, auch fuer die zweite Ordnung.
  - Der Preis waechst je Ordnung und mit der Zeit. Er begrenzt das Schema schon bei V-00, nicht erst spaeter.
  - Die Ereignis-Seite gewinnt durch V-00 gegenueber V-0 fuer das Mittel nichts Messbares (L5). Das Einzelnetz wird aber
    unruhiger.
- **Naechste Schritte [H]:**
  - Varianzkern und seine Pole (zweites Moment) am Schreibtisch, dann im Feld bei mehreren Laufstrecken.
  - Mehr Dichten fuer die Rauschsteigung.
  - Die Kausalmengen-Form von f(Box + m^2) aus SCHICHT-1 bleibt offen.

## 7. Selbstanzeigen

1. **S2-1 nicht auswertbar durch einen Planungsfehler:**
   - Ich habe die Gittersuche fuer S unveraendert aus SCHICHT-1 uebernommen, obwohl mein eigener Plan V-00 bei rho = 4
     genau knapp ueber dem Rand von S erwartete (4,4e-3).
   - Die Suche verwirft Minima auf den Randzeilen. Zugleich habe ich "lokalisiert = gezaehlt" und die Konsistenz zur
     Urteilsbedingung gemacht.
   - Den eingefrorenen Code und die Regeln habe ich nicht geaendert.
   - **Zusatzprobe nach dem Befund:** Danach habe ich code/zusatz_lokalisierung.py neu geschrieben (nicht eingefroren) und
     einmal laufen lassen (cpu6, 08:32:31 bis 08:33:24 UTC).
     - Ihr Teil "Gitter ab Im = 0,001" war ebenfalls ungeeignet: Die Nullstelle lag wieder naeher an der Randzeile, die
       Liste blieb leer.
     - Tragend sind nur die Rechteckzaehlung (1, stabil) und Newton auf g_I.
   - Ich hatte die Werte vor dem Schreiben der Probe gesehen. Sie aendert kein Urteil.
2. **Vor dem Einfrieren gesehen** (PLAN 10):
   - V-J-Pole bei rho = 16 (bekannt); die Pruefgroessen der Codeprobe; Repro und Zeiten der Rauchsaat
   - die Moment- und Sprungprobe des V-00-Kerns (analytische Identitaeten, keine Polwerte)
   - die Zaehler L2 (rho = 1,2: 7 535; rho = 16, Saat 91: 657 207). Den Wert L2/L0 = 0,307 habe ich fuer die
     Rauschschaetzung im Plan benutzt.
   - Keine Pol-, Erwartungs- oder Feldwerte von V-00 oder V-0.
3. **Pfadprobe:** Die Pfadprobe der Auswertung (Saaten 1 bis 3, 08:40:48 UTC) druckte schon alle vier Urteile. Plan und
   Regeln waren da eingefroren; ihre Urteile zaehlen nicht. Sie lief fehlerfrei.
4. **Lokal:** kein python, awk oder perl.
   - Benutzt habe ich jq, sed, grep, sha256sum, date, ssh und scp, sort nur mit LC_ALL=C; dazu cp, mv, mkdir, ls, cat,
     cut, head, tail, uniq.
   - Warteschleifen mit until/sleep. Ein direktes "sleep 100" hat das Werkzeug abgelehnt; es lief nicht.
   - Auf der .69 ausserhalb des Starters nur: date, uptime, ls, cat, grep, mkdir, mv, ln -s (Ordner der Pfadprobe),
     sha256sum.
5. **Spur p4000a:** nur als Lock fuer CPU-Rechnungen benutzt, wie im Plan. Die Projektregel "Simulationen auf CUDA" ist
   fuer diese Kleintests durch die Spurwahl der Leitung abgedeckt, nicht durch mich geprueft.
6. **Leerlauf:** Zwischen 10:39:22 und 10:40:41 CEST stand p4000a, weil ich Feld 10 bis 12 spaet gestartet habe. Folgen
   fuer die Regeln hat das nicht.
7. **Dieselben Saaten wie SCHICHT-1:** Das war gewollt (PLAN 4) und gibt bitgleiche Repro. Dafuer ist s_V0 = 0,636 keine
   unabhaengige Wiederholung. S2-2 vergleicht gepaart auf denselben Netzen.
8. **Korrelation und kleine Statistik:** zwoelf Saaten. Alle Varianten und Punkte einer Saat teilen sich eine Streuung;
   die 54 Tests sind nicht unabhaengig.
9. **Nicht geplante Beobachtung:** Der Zeitgang der Streuung (3.4) und die Norm (3.5) waren keine Urteilsgroessen. Die
   Deutung "zweites Moment" ist eine Hypothese.
10. **Meine Korrekturschaetzung** zur Restformel (PLAN 2: 10 bis 25 % bei rho = 4) war zu gross; es sind 3 bis 4 %.
11. **Bild streuung_varianten.png:** Die Beschriftung der y-Achse ist links abgeschnitten.
12. **Ablage:** Meine Dateien liegen nur im Kartenordner und auf der .69 (runde39-kausal-schicht2/). Das Werkzeug legt
    Ausgaben von Hintergrundbefehlen selbst unter /tmp/claude-1000/.../tasks/ ab; das habe ich nicht gewaehlt.
13. **Kein frischer Gegenleser** fuer Herleitung (Momentreihe L_j, Restformel, (4, -16, 20, -8)), Code und Text.
14. **Zeitbox:** Start 10:00:08 CEST, Text ab 10:50:55 CEST, Abschluss 10:54:08 CEST (date), also rund 54 von 120 min.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-101956
- code/:
  - kausal4d.py, kontinuum4d.py (unveraendert aus KAUSAL-WELLE-4D)
  - schicht2_feld.py, schicht2_kont.py, schicht2_auswertung.py, je *.eingefroren-20261004-101956
  - pruefsummen-einfrieren.txt
  - zusatz_lokalisierung.py (nach dem Befund, nicht eingefroren)
- lauf-69/:
  - feld-r16-s{1..12}.json/.npz
  - kont/ (pole-VJ.json, pole-V0.json, pole-V00.json, erwartung.json, erwartung.npz, zusatz-lokalisierung.json)
  - aw/ (Originalausgabe der Auswertung)
  - auswertung.json (mit Vermerken), auswertung.maschine.json
  - Logs: pole-VJ, pole-V0, pole-V00, erwartung, f16a bis f16d, auswertung, zusatz
- **Bilder** (lauf-69/):
  - pole.png: Nullstellen je Variante und Dichte (k = 0 und p), Lupe an der Schale, Im omega gegen rho mit Formeln
  - streuung_varianten.png: relative Streuung je Pruefpunkt und Variante
  - saatmittel_erwartung_kontinuum.png: Saatmittel gegen Erwartung und Kontinuum je Variante (t = 3,2)
  - zuwachs_t.png: abs(E)/abs(Kontinuum) gegen t je Variante und Dichte, Norm je Zeitscheibe
- rauch-69/: Codeprobe, Repro, Moment- und Sprungprobe, V-J-Pole, Pfadprobe der Auswertung (aw-pfad/; Urteile dort zaehlen
  nicht).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde39-kausal-schicht2/ (code/, rauch/, lauf/).

## 9. Einfach gesagt

Auf dem zufaelligen Raumzeit-Netz waechst eine schwere Welle im Mittel langsam an. Mit einer dritten Sorte von Spruengen,
zu Punkten, zwischen denen genau zwei andere Punkte liegen, und genau abgestimmten Gewichten haben wir auch den Rest des
Anwachsens noch einmal rund 30-fach gedrueckt; bei unserem feinsten Netz waechst die Welle im Mittel jetzt etwa 350-mal
langsamer als nach der urspruenglichen Regel, und die Rechnung auf dem Papier hat das auf wenige Prozent vorhergesagt.
Der Preis ist hoch: Ein einzelnes Netz rauscht jetzt etwa fuenfmal so stark wie mit der urspruenglichen Regel, das
Rauschen ist groesser als die Welle selbst und wird mit der Zeit staerker. Man kann das Anwachsen also Schritt fuer
Schritt abstellen, aber jeder Schritt braucht eine exakte Feinabstimmung und macht das einzelne Netz unruhiger. Das ist
eine Computerrechnung, keine Messung.
