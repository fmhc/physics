# KAUSAL-4D-SCHICHT-1: Ergebnis (Code-Agent fuer die Leitung, Runde 38, explorativ)

- Gerechnet auf der .69 nur ueber kleintest.sh, Spuren cpu6 und p4000a, jeweils CPU mit einem Gewinde; die GPU der
  p4000a-Spur blieb unbenutzt. Hoechstens zwei Laeufe zugleich.
- **Zeiten** (date; .69 in UTC, CEST = UTC + 2):
  - Start 08:53:29 CEST.
  - Rauch 07:03:45 bis 07:11:20 UTC. Plantext ab 09:07:48 CEST.
  - **Eingefroren 09:12:55 CEST:**
    - PLAN.md.eingefroren-20261004-091255
    - code/*.eingefroren-20261004-091255
    - sha256 in code/pruefsummen-einfrieren.txt
  - Hauptlaeufe 07:13:03 bis 07:36:22 UTC: Pole, Erwartung, fuenf Feldlaeufe, Auswertung, alle rc = 0, kein
    Abbruch vor einer Saat. Dazu zwei Pfadproben der Auswertung (rc = 1, dann rc = 0; Selbstanzeige 1).
  - Text ab 09:38:20 CEST.
- **Hashes:**
  - Alle 24 Felddateien tragen die sha256 des eingefrorenen schicht_feld.py (5c71a057...).
  - pole.json und erwartung.json tragen die des eingefrorenen schicht_kont.py (ed11cf5a...).
  - Plan, kausal4d.py, kontinuum4d.py, schicht_feld.py und schicht_kont.py waren nach den Laeufen unveraendert (sha256
    um 09:37:22 CEST geprueft).
  - schicht_auswertung.py ist nach dem Einfrieren berichtigt worden: d0169832... -> 0cd08aab... (Selbstanzeige 1).
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier aus zweiter Hand: Dossier/Arbeitsfeld KAUSAL-4D-STABIL-L bzw. KAUSAL-WELLE-4D)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [E] hier gerechnet (synthetisch, keine Messdaten); [F] Festlegung des Plans

## 1. Ergebnis zuerst

1. **Die geaenderte Sprungregel V-0 drueckt das Anwachsen der Erwartung um eine Ordnung [E, M].**
   - V-0: Links 2a, 1-Element-Intervalle -2a.
   - Der Massenschalen-Pol liegt bei rho = 16 (k = 0) bei Im omega = 0,0147 statt 0,152 (V-J).
   - Er faellt von rho = 4 bis 16 um den Faktor 4,8: 0,070 / 0,032 / 0,0147.
   - Die Restformel 3 M^6/(16 rho omega) aus dem Dossier trifft auf 13 / 5 / 3 % (0,081 / 0,034 / 0,0151), mit
     wachsender Dichte besser.
   - **Abgestellt ist das Anwachsen nicht:** Ein kleiner Rest hoeherer Ordnung waechst weiter.
2. **V-M kehrt das Vorzeichen um [E, M].**
   - V-M: Links 3a, 1-Element-Intervalle -4a.
   - Auf dem physikalischen Blatt gibt es keinen Pol nahe der Massenschale. Er liegt auf dem zweiten Blatt bei
     Im omega = -0,149 (rho = 16), also Zerfall, fast so gross wie das Wachstum von V-J.
   - In abs(omega) < 10, Im omega > 0,05 gibt es fuer V-0 und V-M keine weitere Nullstelle, bei keiner Dichte, auch
     nicht fuer V-J.
3. **Die Felder folgen der jeweiligen Erwartung [E].**
   - Bei rho = 16 und 8 liegen alle drei Varianten an 18 von 18 Pruefpunkten innerhalb 3 SE ihrer eigenen Erwartung,
     also 108 von 108. Die groesste Abweichung ist 1,97 SE.
   - Zuwachs abs(E)/abs(Kontinuum) von t = 2,0 bis 3,2 bei rho = 16: V-J 1,247, V-0 1,064, V-M 0,867.
4. **Preis: mehr Rauschen [E].** Die relative Streuung je Saat bei rho = 16 betraegt 0,31 (V-J), 0,64 (V-0) und
   1,03 (V-M). V-0 rauscht also doppelt so stark wie V-J; bei allen drei faellt die Streuung mit rho.
5. **Urteile:** SH0, SH1, SH2 und SH3 eingetroffen. Kein Graubereich wurde beruehrt. Bei rho = 8 laege der Zuwachs von
   V-0 aber im Graubereich (1,115), bei rho = 4 waere SH2 gescheitert (1,20); geurteilt wird nach Plan nur bei rho = 16.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 09:12:55 CEST) durch code/schicht_auswertung.py; Werte in lauf-69/auswertung.json.
- Die Felder "vermerk" sind per jq nachgetragen.
- Ohne sie ist die Datei inhaltsgleich mit lauf-69/auswertung.maschine.json (sha256 der sortierten Ausgabe geprueft:
  fd62542a...).

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| SH0 | Saatmittel V-J trifft Johnstons Erwartung an >= 15 von 18 Punkten (3 SE) | 85 % | **eingetroffen** | 18 von 18 (rho = 16), max 1,97 SE; rho = 8 ebenfalls 18 von 18 |
| SH1 | Im omega(V-0, 16, k = 0) in [0; 0,05], Faktor >= 3 von rho 4 bis 16; V-M ohne Pol in Im omega > 0 nahe der Schale; keine weitere Nullstelle | 50 % | **eingetroffen** | 0,0147; Faktor 4,77; V-M N_S = 0 in allen 6 Faellen; weitere Nullstellen 0 in allen 12 Faellen |
| SH2 | Saatmittel V-0 trifft eigene Erwartung (>= 15 von 18); Zuwachs V-0 <= 1,10; V-M unter 1 | 50 % | **eingetroffen** | 18 von 18 (max 1,66 SE); Zuwachs V-0 1,064, V-M 0,867 (Maximum ueber beide Konfigurationen) |
| SH3 | [H] Streuung V-0 > V-J; Prognose 0,5 bis 1,0 | 55 % | **eingetroffen** | s_V0 = 0,636, s_VJ = 0,310 (Faktor 2,05) |

- **Scheiterregeln:** Keine ausgeloest. SH1: Im omega(V-0) = 0,0147 <= 0,075, V-M wechselt das Vorzeichen, keine weitere
  Nullstelle. SH2: 1,064 <= 1,15. SH3: weder unter 0,33 ("kein Preis") noch ueber 1,5 ("unbrauchbar").
- **Kartenwortlaut:** Die Normierung der Karte stimmt (PLAN 2), ich habe nichts berichtigt, nur Offenes festgelegt
  (PLAN 9). Die Urteile nach Wortlaut sind dieselben.
- **Andere Lesarten (beschreibend):**
  - SH2 bei rho = 8: Zuwachs V-0 1,115 / 1,100 (eta = 0 / 0,5), also Graubereich; V-M 0,894 / 0,902.
  - SH2 bei rho = 4 (nur Erwartung): V-0 1,200 / 1,177, also ueber der Scheiterschwelle; V-M 1,035 / 1,036, also
    nicht unter 1.
  - Die Dichte rho = 16 fuer SH2 stand vor jeder Rechnung im Plan [F]. Die Vorhersage traegt aber erst ab etwa
    rho = 16; das passt zum Gang m^6/rho.
  - SH0 und SH2(a) bei rho = 8: je 18 von 18.
- **Meine Vorab-Erwartung** (PLAN 9.3): SH0 ein (90 %), SH1 ein (35 %), SH2 ein (40 %), SH3 ein (55 %).
  - Die befuerchteten UV-Nullstellen (abs(Z) ~ 1,9) gibt es nicht. Meine Abschaetzung war die ungueltige
    Grossargument-Naeherung.
  - Mein Rauschschaetzer (s_V0 ~ 0,8, s_VM ~ 1,3) lag etwas zu hoch: 0,64 bzw. 1,03.
- **Bedeutung nach der Karte (vorab):**
  - Ausgeloest ist "SH1 und SH2 treffen ein: Das Anwachsen ist eine reparierbare Eigenschaft des Kerns. Die
    Ereignis-Seite bleibt in diesem Punkt offen. Naechster Schritt ist die Kausalmengen-Form von f(Box + m^2)."
  - Einschraenkungen dazu in Abschnitt 6.

## 3. Tabellen

### 3.1 Massenschalen-Nullstellen von 1 + m^2 k~_gen [E, M]

Newton nach Gitter, Zaehlung per Argumentprinzip (PLAN 4). Blatt I: physikalisch, Im omega > 0 heisst Wachstum. Blatt II:
Fortsetzung ueber den zeitartigen Schnitt, Im omega < 0 heisst Zerfall.

| rho | k | V-J (Blatt I) | V-0 (Blatt I) | V-M (Blatt II) |
|---|---|---|---|---|
| 4 | 0 | 1,0173 + 0,2458 i | 1,1225 + 0,0701 i | 1,4710 - 0,2796 i |
| 8 | 0 | 1,0422 + 0,1978 i | 1,0884 + 0,0322 i | 1,0597 - 0,2429 i |
| 16 | 0 | 1,0545 + 0,1523 i | 1,0606 + 0,0147 i | 1,0125 - 0,1490 i |
| 4 | p | 1,1376 + 0,2198 i | 1,2372 + 0,0636 i | 1,5579 - 0,2640 i |
| 8 | p | 1,1619 + 0,1774 i | 1,2066 + 0,0291 i | 1,1762 - 0,2189 i |
| 16 | p | 1,1743 + 0,1368 i | 1,1817 + 0,0132 i | 1,1367 - 0,1327 i |

- p = sinh 0,5 = 0,521. Die V-J-Pole sind dieselben wie in KAUSAL-WELLE-4D (bis 1e-14).
- **Schreibtisch gegen Rechnung (k = 0):**
  - V-J: (sqrt 6/4) m^4/(omega sqrt rho) gibt 0,306 / 0,217 / 0,153.
  - V-0: 3 M^6/(16 rho omega) gibt 0,081 / 0,034 / 0,0151 (Rechnung 0,070 / 0,032 / 0,0147).
  - V-M, erste Ordnung: -0,306 / -0,217 / -0,153 (Rechnung -0,280 / -0,243 / -0,149).
  - Bei rho = 4 liegt die V-M-Nullstelle mit Re omega = 1,47 weit von der Schale. Die Erwartung von V-M ist dort
    nicht durch einen einzelnen Pol beschrieben (Bild zuwachs_t.png, gepunktet rot).
- **Zaehlungen:**
  - N_A (abs(omega) < 10, Im omega > 0,05): V-J 2 (das Schalenpaar) in allen 6 Faellen. V-0 2 bei rho = 4 (Schalenpaar,
    Im 0,070 bzw. 0,064 > 0,05), sonst 0. V-M 0.
  - N_S (Re omega in [0,5; 2], Im omega in [0,002; 1]): V-J 1, V-0 1, V-M 0.
  - Weitere Nullstellen: 0 in allen 18 Faellen. Beide Aufloesungen geben dieselbe Zahl, und die Zahl der lokalisierten
    Nullstellen ist gleich der gezaehlten.
  - Groessenprobe: max abs(m^2 k~_gen) auf abs(omega) = 10 ist <= 0,013, auf abs(omega) = 20 <= 1,5e-4. Ausserhalb
    der Kontur gibt es also keine Nullstellen.
- Bild lauf-69/pole.png: links und Mitte die omega-Ebene, rechts Im omega gegen rho mit den Schreibtischformeln.
  - Die gepunktete V-J-Kurve rechts teilt durch M statt durch m (Selbstanzeige 5).

### 3.2 Pruefpunkte: Saatmittel, Erwartung und Kontinuum, 12 Saaten je Dichte [E, M]

Je Variante und Dichte die Spannweite ueber die 18 Pruefpunkte.

| Variante | rho | abs(Saatmittel)/abs(K) | abs(E)/abs(K) [M] | in 3 SE von E | groesste Abw. von E | in 3 SE von K |
|---|---|---|---|---|---|---|
| V-J | 16 | 1,20 bis 1,83 | 1,29 bis 1,63 | 18 | 1,97 SE | 0 (4,5 bis 9,5 SE) |
| V-0 | 16 | 1,00 bis 1,58 | 1,21 bis 1,29 | 18 | 1,66 SE | 17 |
| V-M | 16 | 0,57 bis 1,45 | 0,97 bis 1,16 | 18 | 1,83 SE | 18 |
| V-J | 8 | 1,24 bis 1,70 | 1,31 bis 1,74 | 18 | 1,29 SE | 0 |
| V-0 | 8 | 1,16 bis 1,53 | 1,30 bis 1,46 | 18 | 1,45 SE | 18 |
| V-M | 8 | 0,80 bis 1,64 | 1,17 bis 1,35 | 18 | 1,62 SE | 17 |

- K ist die gekappte direkte Faltung, wie KV1 in KAUSAL-WELLE-4D.
- **V-0 hat einen festen Abstand zum Kontinuum, waechst aber kaum:** abs(E)/abs(K) liegt bei rho = 16 an allen Punkten
  bei 1,21 bis 1,29. Re omega der Schale ist 1,061 statt 1, die Massenverschiebung M^2 = m^2/(1 - eps m^2) bleibt.
- Dass V-0 und V-M auch das Kontinuum "treffen" (17 bzw. 18 von 18), liegt an ihrem groesseren SE und dem kleineren
  Abstand. Das ist kein Beleg fuer Kontinuumsnaehe.
- Bild lauf-69/saatmittel_erwartung_kontinuum.png: Profil bei t = 3,2 und rho = 16, je Variante und Konfiguration.

### 3.3 Zuwachs [E, M]

Z = [abs(E)/abs(K)](t = 3,2) / [abs(E)/abs(K)](t = 2,0) an Lage A (Paketmitte), aus der Erwartung.

| rho | V-J eta 0 / 0,5 | V-0 eta 0 / 0,5 | V-M eta 0 / 0,5 |
|---|---|---|---|
| 4 | 1,334 / 1,323 | 1,200 / 1,177 | 1,035 / 1,036 |
| 8 | 1,298 / 1,277 | 1,115 / 1,100 | 0,894 / 0,902 |
| 16 | **1,247** / 1,224 | **1,064** / 1,055 | **0,856** / 0,867 |

- Bei V-J und eta = 0 reproduziert das den Kartenwert 1,25.
- Die Lagen B und C liegen innerhalb 0,04 daneben (auswertung.json, beschreibend.zuwachs_erwartung).
- **Aus den Saatmitteln** ist der Zuwachs nicht aussagekraeftig: Bei rho = 16 liegt er zwischen 0,48 und 1,59. Grund
  ist die Streuung je Saat von 30 bis 100 %. Mit 12 Saaten hat das Mittel ~10 bis 30 % Fehler, das Verhaeltnis zweier
  solcher Mittel mehr.
- Bild lauf-69/zuwachs_t.png:
  - links abs(E)/abs(Kontinuum) auf der Achse von t = 0,4 bis 4,0 (k-Raum-Bezug), mit den Saatmitteln bei rho = 16
  - rechts die Norm je Zeitscheibe

### 3.4 Streuung je Saat [E]

s ist das geometrische Mittel ueber die 18 Pruefpunkte von sd/abs(K); in Klammern bezogen auf abs(E_v).

| rho | V-J | V-0 | V-M |
|---|---|---|---|
| 8 | 0,417 (0,277) | 0,816 (0,589) | 1,326 (1,038) |
| 16 | **0,310** (0,214) | **0,636** (0,508) | **1,034** (0,964) |
| Steigung log s / log rho (8 -> 16) | -0,43 | -0,36 | -0,36 |

- KAUSAL-WELLE-4D hatte fuer V-J 0,366 / 0,327 mit anderen Saaten.
  - Die Steigung zwischen zwei Dichten mit je 12 Saaten ist grob: dort -0,16, hier -0,43.
- Je Punkt bei rho = 16: V-J 0,20 bis 0,38, V-0 0,40 bis 0,87, V-M 0,65 bis 1,40.
- Bild lauf-69/streuung_varianten.png.

### 3.5 Norm je Zeitscheibe gegen Kontinuum, R = Saatmittel(n)/n_c, G = R_4/R_1 [E]

| rho | Variante | R (eta = 0) in den vier Scheiben | G eta 0 / 0,5 | G je Saat Median (eta 0) |
|---|---|---|---|---|
| 16 | V-J | 2,21 / 2,49 / 2,81 / 3,36 | 1,52 / 1,55 | 1,58 |
| 16 | V-0 | 2,30 / 2,36 / 2,23 / 2,35 | 1,02 / 1,08 | 1,01 |
| 16 | V-M | 3,09 / 3,01 / 2,57 / 2,94 | 0,95 / 1,09 | 0,90 |
| 8 | V-J | 2,49 / 2,72 / 3,21 / 4,41 | 1,77 / 1,82 | 1,78 |
| 8 | V-0 | 3,07 / 3,03 / 3,09 / 3,59 | 1,17 / 1,24 | 1,16 |
| 8 | V-M | 4,88 / 4,51 / 4,59 / 5,77 | 1,18 / 1,31 | 1,25 |

- Die Norm enthaelt die Rauschleistung im ganzen Scheibenvolumen. Deshalb liegt R bei allen Varianten bei 2 bis 6, und
  bei V-M zeigt sie den Zerfall des Mittels nicht klar.
- Die Norm war keine Urteilsgroesse dieser Karte. Beim KV3-Massstab der Vorgaengerkarte (G <= 1,5) laege V-0 in allen
  vier Faellen darunter, V-J in keinem.

### 3.6 Linkzahlen [E, M]

| rho | N (Mittel) | L0/N +- SE | Erwartung | Abw. | L1/N +- SE | Erwartung | Abw. |
|---|---|---|---|---|---|---|---|
| 8 | 10 124 | 70,85 +- 0,18 | 71,147 | -1,67 SE | 30,00 +- 0,08 | 30,249 | **-3,08 SE** |
| 16 | 20 372 | 105,15 +- 0,23 | 105,370 | -0,97 SE | 46,37 +- 0,11 | 46,476 | -0,94 SE |

- Die Abweichung von L1/N bei rho = 8 ist auffaellig. L0 und L1 schwanken je Saat gemeinsam, beide liegen bei rho = 8
  tief.
  - Das Integral fuer L1 ist dieselbe Quadratur wie fuer L0, nur mit [1 - (1 + U) e^-U].
  - Bei rho = 16 trifft es.
  - Ich halte es fuer eine Schwankung, geprueft ist das nicht. Kein Urteil haengt daran.
- 1-Element-Intervalle sind 44 % der Links (rho = 16) bzw. 42 % (rho = 8).
- max abs(phi) je Variante: V-J 0,78, V-0 1,16, V-M 1,51. Alle 24 Saaten endlich.

## 4. Kontrollen

- **Codeprobe** (rho = 1,2, N = 1 478, L0 = 32 134, L1 = 11 369, Bloecke 256):
  - Links und 1-Element-Intervalle aus dem GEMM gleich dichtem C C (float64): ja. C gleich Koordinaten: ja.
  - Rekursion gegen dichte Loesung: <= 4,5e-16 (alle drei Varianten). Reihe <= 3,2e-16.
  - Zuschauer gegen eine Schleife, die die Elemente in I(y, p) explizit zaehlt: <= 6,5e-16.
- **Repro:** V-J mit der Saatfolge von KAUSAL-WELLE-4D (rho = 4, Saat 1).
  - N und L0 gleich, phi an den Zuschauern bitgleich (0,0), Normsummen 3e-17.
- **Kontinuum:** gekappte Faltung und Normen bitgleich mit KAUSAL-WELLE-4D (0,0); k-Raum 1,5e-16.
  - V-J-Erwartung bei rho = 4 / 8 / 16 gegen KAUSAL-WELLE-4D: <= 7,9e-16.
- **Argumentprinzip:**
  - Synthetische Probe 3 von 3 und 1 von 1.
  - Je Zaehlung zwei Aufloesungen (2 000 Punkte und Schranke 0,25 rad bzw. 4 000 und 0,12 rad), alle 36 gleich.
  - Lokalisierte Zahl gleich gezaehlter Zahl in allen 36 Faellen.
- **Zweites Blatt:** abs(g_I(x + i e) - g_II(x - i e)) = 3,0e-5 bis 4,9e-5 bei e = 1e-6 und 3,0e-7 bis 4,9e-7 bei
  e = 1e-8. Das skaliert linear mit e, die Fortsetzung ist also stetig.
- **Quadratur:**
  - Pole mit 256 statt 128 tau-Knoten: <= 6,3e-15. Bogen: <= 2,4e-15.
  - Erwartung mit 128 statt 64 Knoten (V-0, V-M bei rho = 4): <= 2,2e-12.
- **Erwartung:**
  - Gamma 0,8 gegen 1,4: <= 4,7e-14 in allen neun Faellen. Weil keine Nullstelle ueber 0,3 liegt, ist das die Regel
    aus PLAN 3.
  - rho = 10^6 gegen k-Raum an 54 Punkten: V-J 0,72 %, V-0 0,09 %, V-M 0,55 %. Alle drei Varianten haben also
    denselben Kontinuumsgrenzfall; das prueft die Normierung numerisch.
- **Monte Carlo gegen Formel:** 108 von 108 Punkten in 3 SE (drei Varianten, zwei Dichten). Das prueft Code und
  verallgemeinerte Erwartungsformel gegeneinander, auch fuer die 1-Element-Spruenge.
- **Laufzeit und Speicher:** rho = 16: 130 bis 137 s je Saat, Hoechststand 1,96 GB (getrusage), unter MemoryMax 4G.
  rho = 8: 21 bis 24 s. Gesamt ~40 min Rechenzeit (Summe der Laufdauern).

## 5. Latten (v3)

- **L1 (kann scheitern):** ja.
  - SH1 haette an UV-Nullstellen scheitern koennen; meine eigene Vorab-Erwartung war 35 %.
  - V-M haette auf Blatt I bleiben koennen.
  - SH2 scheitert bei rho = 4 (1,20) und laege bei rho = 8 im Graubereich (1,115). Die Schwelle ist also nicht trivial.
  - SH3 haette in beide Richtungen scheitern koennen; V-M liegt mit 1,03 schon ueber 1,0.
  - SH0 haette an Code- oder Formelfehlern scheitern koennen.
- **L2 (Gegenprobe):**
  - dichte Links und 1-Element-Intervalle, Koordinaten, dichte Loesung, Reihe, Zuschauerschleife; Repro bitgleich
  - Kontinuum bitgleich; V-J-Pole wie die Vorgaengerkarte
  - zwei Aufloesungen, synthetische Windung, Lokalisierung, Blattstetigkeit, zwei tau-Quadraturen, zwei Gamma,
    rho = 10^6 fuer alle Varianten
  - Monte Carlo gegen Formel fuer drei Varianten
  - Schreibtischformeln fuer V-0 und V-M gegen die Numerik
- **L3 (Numerik):** Code <= 6,5e-16; Pole <= 6e-15; Erwartung <= 5e-14 (Gamma), 2e-12 (Quadratur); Grenzfall
  rho = 10^6 <= 0,72 %.
- **L4 (schon bekannt):**
  - Johnstons Pfadsumme, a und b [S, KAUSAL-WELLE-4D]; Korrekturterm erster Ordnung bei Johnston 2014 [S, Dossier].
  - Alternierende Schichtkoeffizienten mit Summe 0 bei den 4D-BD-Operatoren (4, -36, 64, -32)/sqrt 6 [S, Dossier, ASS
    (2.12)]; allgemeine Sprungamplituden bei Shuman 2023 [S, Dossier].
  - Die Mehrschicht-Pfadsumme mit sigma = 0 als Abhilfe gegen das Anwachsen ist ein eigener Vorschlag des Dossiers. In
    dessen Recherche war sie nicht zu finden [L?].
- **L5 (Messbezug):** keiner (synthetisch, eine lineare Welle, Laufstrecke 2/m).
  - **Hochrechnung [M, ungeprueft, nur Modell]:** Der V-0-Rest je Eigenzeit ist (3/16) m^5 l^4 statt (sqrt 6/4) m^3 l^2.
  - Bei l = l_P waere das fuer einen Skalar mit Higgsmasse ~6e24 Weltalter je e-Faltung statt ~2,6 Jahre (Dossier),
    mit Top-Masse ~1e24 Weltalter.
  - Die Numerik stuetzt die Restformel nur bis rho = 16 (Abweichung 13 / 5 / 3 %, fallend).

## 6. Bedeutung

- **Gezeigt [E, M]:** Im Mittel steuert sigma = sum a_n das Vorzeichen des Massenschalen-Imaginaerteils, wie das Dossier
  vorhersagt.
  - sigma = +a waechst, sigma = 0 waechst nur mit einem Rest hoeherer Ordnung, sigma = -a zerfaellt.
  - Die Normierung haelt den Kontinuumsgrenzfall fest.
  - In abs(omega) < 10 entstehen keine neuen instabilen Nullstellen, anders als die alternierenden BD-Summen bei ASS
    (dort UV-Nullstellen an der Nichtlokalitaetsskala [S, Dossier]).
- **Einschraenkungen:**
  - **Kein vollstaendiges Abstellen:** V-0 waechst weiter, mit einer Rate ~m^6/rho statt ~m^4/sqrt(rho). Fuer
    physikalische Dichten ist das nach der Hochrechnung bedeutungslos (L5), bei rho = 16 sind es 0,015.
  - **V-M ist keine Loesung, sondern das Spiegelbild:** Das Mittel zerfaellt mit fast derselben Rate, mit der V-J waechst.
    Fuer schwere Skalare waere das ebenso unphysikalisch (Higgs-Mode ~2,6 Jahre Zerfallszeit nach Dossier-Rechnung) [H].
  - **Der feste Abstand bleibt:** Auch V-0 liegt bei rho = 16 um 21 bis 29 % ueber dem Kontinuum (Massenverschiebung).
    Die Abhilfe betrifft das Anwachsen, nicht die Naehe zum Kontinuum bei endlicher Dichte.
  - **Preis:** Die Streuung je Saat verdoppelt sich. Sie faellt mit rho, aber nur zwei Dichten.
  - Mittel gegen Einzelnetz: Die Einzelsaaten wachsen in der Norm bei V-0 kaum (G je Saat Median 1,01, rho = 16). Die
    Laufstrecke ist aber nur 2/m; Langzeit-Selbstmittelung bleibt offen [H].
- **Fuer die Karte:** "Das Anwachsen ist eine reparierbare Eigenschaft des Kerns" traegt im Mittel und bis auf einen
  Rest hoeherer Ordnung. Fuer die Ereignis-Seite heisst das: Johnstons 4D-Form ist kein Endpunkt; eine kleine
  Schichtsumme macht sie in diesem Punkt brauchbar [E, H].
- **Naechste Schritte [H]:**
  - Drei Schichten (a_0, a_1, a_2) mit Normierung, sum a_n = 0 und sum a_n Gamma(n + 3/2)/n! = 0. Dann faellt auch der
    m^6-Rest weg (Dossier, offene Frage 2). Pruefbar mit demselben Code (P == 2 aus demselben GEMM).
  - Die Kausalmengen-Form von f(Box + m^2) (Karte).
  - Mehr Dichten fuer die Streuungssteigung.

## 7. Selbstanzeigen

1. **Codefehler nach dem Einfrieren (schicht_auswertung.py):**
   - Ich hatte 35 Punkte je Konfiguration angenommen (18 + 17). Es sind 26: 9 Pruefpunkte und 17 Profilpunkte. Der
     Kopftext von kausal4d.pruefpunkte nennt die Form (NC, 18 + 17, 4); ich habe ihn uebernommen, statt die Form zu
     pruefen.
   - Die Pfadprobe (07:21:46 UTC, rc = 1) brach beim Vergleich mit KAUSAL-WELLE-4D ab. Falsch geschnitten waeren auch
     zwei Bilder.
   - Behoben um 09:22 CEST per sed und Edit: 35 -> NPP = pp.shape[1]. sha256 d0169832... -> 0cd08aab...; die
     eingefrorene Fassung liegt unveraendert daneben.
   - Die Urteile benutzen nur die ersten 9 Punkte; dieser Teil ist unveraendert.
2. **Pfadprobe mit Hauptdaten:**
   - Die zweite Pfadprobe (07:22:21 UTC) lief auf den Haupt-Teil-A-Daten und der Rauchsaat 91. Sie druckte dabei schon
     das SH1-Urteil (eingetroffen), das nur von Teil A abhaengt, und ich habe die Teil-A-Werte angesehen. Das war vor
     den Teil-B-Hauptdaten.
   - Plan und Regeln waren seit 09:12:55 CEST eingefroren. Die anderen Urteile der Probe (eine Saat, nan) zaehlen nicht.
3. **Vor dem Einfrieren gesehen** (PLAN 10):
   - V-J-Pole bei rho = 16 (bekannt aus KAUSAL-WELLE-4D) und die V-J-Erwartungskontrollen
   - die Pruefgroessen der Codeprobe
   - die Zaehler L1 (rho = 4: 95 815; rho = 16, Saat 91: 942 371)
   - Keine Werte von V-0 oder V-M.
4. **Lokal:** kein python, awk oder perl.
   - Benutzt habe ich jq, sed, grep, sha256sum, date, ssh und scp, sort nur mit LC_ALL=C.
   - Dazu Dateibefehle: cp, mv, mkdir, chmod, ls, cat, cut, head, tail, tr, uniq, wc.
   - Warteschleifen mit until/sleep. Ein direktes "sleep 45" hat das Werkzeug abgelehnt; es lief nicht.
   - Auf der .69 ausserhalb des Starters nur: date, uptime, nproc, free, ls, head, cat, mkdir, mv, sha256sum.
5. **Bild pole.png:** Die gepunktete "V-J erste Ordnung" rechts teilt durch omega = M statt m. Die Werte sind
   ~5 % kleiner als (sqrt 6/4) m^4/(m sqrt rho). Die Tabelle 3.1 nennt die richtigen Formelwerte.
6. **Spur p4000a:** nur als Lock fuer CPU-Rechnungen benutzt, wie im Plan. Die GPU war nicht im Spiel. Die
   Projektregel "Simulationen auf CUDA" ist fuer diese Kleintests durch die Spurwahl der Leitung abgedeckt, nicht durch
   mich geprueft.
7. **Geringere Trennschaerfe bei SH2(a):** V-0 rauscht doppelt so stark. Derselbe Test "in 3 SE" ist deshalb lockerer als
   bei SH0. Er traf aber auch das Kontinuum nicht ueberall (17 von 18) und hat so weniger Aussagekraft.
8. **Korrelation und kleine Statistik:** 12 Saaten je Dichte; alle Varianten, Konfigurationen und Punkte einer Saat
   teilen sich eine Streuung. Die 18 bzw. 108 Tests sind nicht unabhaengig.
9. **L1/N bei rho = 8 um -3,08 SE daneben** (Abschnitt 3.6), nicht geklaert.
10. **Ablage:** Meine Dateien liegen nur im Kartenordner und auf der .69 (runde38-kausal-schicht/). Das Werkzeug legt
    Ausgaben von Hintergrundbefehlen selbst unter /tmp/claude-1000/.../tasks/ ab; das habe ich nicht gewaehlt.
11. **Kein frischer Gegenleser** fuer Herleitung (zweites Blatt, Z^2 ln Z^2-Koeffizient), Code und Text.
12. **Zeitbox:** Start 08:53:29 CEST, Text ab 09:38:20 CEST, Abschluss 09:41:17 CEST (date), also rund 50 von 120 min.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-091255
- code/:
  - kausal4d.py, kontinuum4d.py (unveraendert aus KAUSAL-WELLE-4D)
  - schicht_feld.py, schicht_kont.py, schicht_auswertung.py (berichtigt, Selbstanzeige 1)
  - je *.eingefroren-20261004-091255; pruefsummen-einfrieren.txt
- lauf-69/:
  - feld-r{8,16}-s{1..12}.json/.npz
  - kont/ (pole.json, erwartung.json, erwartung.npz)
  - aw/ (Originalausgabe)
  - auswertung.json (mit Vermerken), auswertung.maschine.json
  - Logs: pole, erwartung, f16a bis f16d, f8, auswertung
- **Bilder** (lauf-69/):
  - pole.png: Nullstellen je Variante und Dichte (k = 0 und k = p), Im omega gegen rho mit Schreibtischformeln
  - saatmittel_erwartung_kontinuum.png: Saatmittel gegen Erwartung und Kontinuum je Variante (t = 3,2, rho = 16)
  - zuwachs_t.png: abs(E)/abs(Kontinuum) gegen t je Variante und Dichte, Norm je Zeitscheibe
  - streuung_varianten.png: relative Streuung je Punkt, Variante und Dichte
- rauch-69/: Probe, Repro, Zeitlauf, V-J-Pole und -Erwartung, Pfadproben der Auswertung (aw/; Urteile dort zaehlen nicht).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-kausal-schicht/ (code/, rauch/, lauf/).

## 9. Einfach gesagt

Auf dem zufaelligen Raumzeit-Netz wurde eine schwere Welle im Mittel mit der Zeit immer staerker, weil sie nach der
alten Regel nur zu direkten Nachbarpunkten springen durfte. Wir haben eine kleine Aenderung getestet: Die Welle springt
doppelt so stark zu direkten Nachbarn und mit umgekehrtem Vorzeichen zu Punkten, zwischen denen genau ein weiterer Punkt
liegt. Damit waechst sie bei unserem feinsten Netz rund zehnmal langsamer, und dieser Rest schrumpft mit feinerem Netz
schnell; mischt man etwas anders, klingt die Welle sogar ab statt zu wachsen. Ganz abgestellt ist das Anwachsen also
nicht, aber auf einen winzigen Rest gedrueckt; der Preis ist, dass ein einzelnes Netz etwa doppelt so stark rauscht.
Das ist eine Computerrechnung, keine Messung.
