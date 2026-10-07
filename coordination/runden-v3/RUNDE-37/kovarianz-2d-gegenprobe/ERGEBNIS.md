# KOVARIANZ-2D-GEGENPROBE: Ergebnis (Runde 41, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 16:12:18 CEST. VORAB.md Abschnitte 1 bis 3 ab 16:31:53 CEST (vor jeder Rechnung), Abschnitt 4 ab
    16:34:52 CEST (nach dem vorab-Lauf, reine Quadratur). Plantext ab 16:39:34 CEST.
  - .69: vorab 14:34:15 bis 14:34:31, Kontrolle 14:34:48 bis 14:35:03, Rauchlaeufe 14:34:50 bis 14:35:48 (blind),
    Codeprobe 14:38 bis 14:39 UTC (nur Struktur gelesen).
  - Eingefroren 16:41:40 CEST: PLAN.md.eingefroren-20261004-164140, VORAB.md.eingefroren-20261004-164140, Code-Kopien
    *.eingefroren-20261004-164140, Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe: Kontrolle 14:41:46 bis 14:42:10 (cpu); N = 4000 14:42:10 bis 14:47:33 (cpu); N = 8000, Saaten 0 bis
    59, 14:47:33 bis 14:52:41 (cpu); N = 1000 Start 14:41:49 (wartete auf den Lock von cpu4), Ende 14:49:03; N = 2000
    14:49:03 bis 14:51:49; N = 8000, Saaten 60 bis 119, 14:51:49 bis 14:56:59 (cpu4). Alle rc 0. Auswertung 14:57:14
    bis 14:57:18 UTC (cpu, rc 0). Text ab 17:00:02 CEST.
- Code nach dem Einfrieren unveraendert: sha256 von kovarianz2d.py (4d83a55d...), kugel.py und kugel2.py auf der .69
  vor der Auswertung gleich den eingefrorenen. lauf-69/PRUEFSUMMEN.txt (.69, 14 Dateien) lokal nachgeprueft: 14 von 14.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu und cpu4).
  Euklidisch, eine Schleife, freies masseloses Skalarfeld (P1), synthetisch, keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [E] hier gerechnet, [ES] eigener Schluss, [F] Festlegung im Plan,
  [K] Kartenpunkt (vor dem Rechnen), [H] Hypothese, [L] Literatur aus dem Gedaechtnis, [N] Nachtrag nach der
  Auswertung (nicht im Plan).
- **Konvention:** Delta Gamma = Gamma_QI(verformt) - Gamma_Q(rund), Gamma = 1/2 log det' K (roh, wie kovarianz.py),
  gepaart je Saat und N. b = Saatmittel des Mittels ueber N = 1000, 2000, 4000; SE aus 120 Saaten. In 2D ist die
  Vorhersage fuer Delta Gamma selbst N-unabhaengig ([K5]); pred = kappa_GROB Delta Gamma_P (VORAB.md Abschnitt 4).

## 1. Ergebnis zuerst

1. **Ja, die Vorschrift ist in 2D sauber, soweit messbar [E].** Auf S^2 zeigt dieselbe Bauvorschrift keine Spur des
   4D-Musters. Konform l = 2, eps = -0,1: Delta Gamma = +0,041 +- 0,068 / -0,010 +- 0,091 / +0,169 +- 0,131 /
   -0,185 +- 0,171 bei N = 1000 / 2000 / 4000 / 8000. In 4D waren es bei gleicher Amplitude -16 / -27 / -48.
   - Kein Wachstum mit N: Aenderung von N = 1000 auf 4000 +0,13 +- 0,15 (0,9 SE); Steigung in N -1,8e-5 +- 2,5e-5 je
     Punkt (4D etwa -0,011).
   - Keine in abs(eps) lineare Antwort: Linearglied A1 je Punkt <= 0,0021 / 0,0013 / 0,0007 (2-SE-Schranke,
     N = 1000 / 4000 / 8000); 4D: 0,16 / 0,12.
   - Alle Schranken (2 SE) liegen bei 0,6 bis 1,3 % der 4D-Groesse.
2. **Derselbe Codepfad wie in 4D [E].** kovarianz2d.py mit n = 4 gibt kovarianz.py bitgleich wieder (live und gegen
   dessen Laufdatei, Abweichung 0,0; Kontrolle K4D). Transport, Huelle, Einbettungssehnen, Neuvernetzung, Paarung und
   Gamma-Auswertung sind also in 2D und 4D derselbe Code.
3. **Den Polyakov-Betrag selbst misst dieser Test nicht [E, K3].** Das Signal (-0,0052 bei eps = -0,1, -0,081 bei
   -0,4) liegt weit unter dem Paarungsrauschen (Std je Saat 0,2 bis 5,8). Bei eps = -0,4 ist b = -0,081 +- 0,143 gegen
   die Vorhersage -0,087, also 0,92 +- 1,64. Das ist im Rauschen vertraeglich mit Polyakov, mit null und mit dem
   Mehrfachen; kein Beleg fuer den Betrag.
4. **Urteile:** KG0 eingetroffen. KG1 nicht auswertbar (Signal unter 3 SE). KG2 eingetroffen. KG3 nach Plan nicht
   entschieden; nach Kartenwortlaut (Punktschaetzer) eingetroffen, aber als Zufallstreffer im Rauschen (Abschnitt 2).
5. **Folge fuer KOVARIANZ-KUGEL-1 [ES]:**
   - Die 4D-Anomalie entsteht nicht im dimensionsunabhaengigen Teil von Vorschrift und Code.
   - Sie muss an etwas haengen, worin sich 4D von 2D unterscheidet. Kandidaten: die Laengenabhaengigkeit der
     4D-Steifigkeit (K vom Grad 2, also Groesse und Form jedes Simplex), das 4D-Delaunay-Netz (60 % statt 13 % neue
     Simplizes) und die Grobheit (Sehnenvolumen 20 % zu klein statt 0,6 %). Welcher davon, trennt dieser Test nicht.
   - Der Kartenzweig "KG1 und KG2 treffen ein" ist formal nicht ausgeloest, weil KG1 nicht auswertbar ist.
   - Das 4D-Ergebnis ist damit kein Codefehler im gemeinsamen Teil. Ob es Physik dieses 4D-Netzes oder ein 4D-eigener
     Konstruktionseffekt ist, bleibt offen (Abschnitt 6).

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch kovarianz2d.py auswertung; Werte in lauf-69/auswertung.json.
**Tor bestanden:** 120 von 120 Saaten bei N = 1000, 2000, 4000 gueltig, dazu 120 von 120 bei N = 8000. Das sind 480 runde
und 3360 verformte Netze, jedes mit Huellenpruefungen, Gauss-Bonnet <= 2,5e-12, zwei LU ok und Transportrest
<= 1,1e-16. Ausgeschlossen 0, unvollstaendig 0.
**K0:** Gamma_C rund in 80 von 80 Vergleichen bitgleich mit INDUZIERT-KUGEL-1 (n = 2, N = 4000, Saaten 0 bis 79,
groesste Abweichung 0,0).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen (G_QI) |
|---|---|---|---|---|---|
| KG0 | Moebius-Nullprobe innerhalb 3 SE um null oder kleiner als 5 % des l = 2-Signals | 70 % | **eingetroffen** | **eingetroffen** | b_M = -1,7e-12 +- 1,7e-12 (-1,0 SE); vorab entschieden [K2]. Nebenlesart Gamma_M (QI): +0,00089 +- 0,00087 (1,0 SE), mit Planregel eingetroffen |
| KG1 | [H] l = 2 quadratisch (Steigung ln abs(Delta Gamma) gegen ln eps zwischen 1,8 und 2,2) | 55 % | **nicht auswertbar** | **nicht auswertbar** | b = +0,067 +- 0,057 / +0,087 +- 0,102 / -0,081 +- 0,143 bei eps = -0,1 / -0,2 / -0,4: kein b >= 3 SE, Vorzeichenwechsel. Polyakov-Steigung 1,977 |
| KG2 | [H] l = 2 unabhaengig von N (Aenderung 1000 -> 4000 innerhalb 2 SE bzw. unter 10 %) | 50 % | **eingetroffen** | **eingetroffen** | eps = -0,1: +0,041 +- 0,068 -> +0,169 +- 0,131, Aenderung +0,128 +- 0,147 (0,87 SE) |
| KG3 | [H] Betrag trifft Polyakov innerhalb 30 % | 40 % | **nicht entschieden** | **eingetroffen** (Zufallstreffer) | eps = -0,4: b = -0,081 +- 0,143, pred = -0,087 +- 0,006; r = 0,92 +- 1,64, 2-SE-Intervall [-2,4; 4,2]. Zu kappa = 1: 0,99 |

- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "KG1 und KG2 treffen ein: Die Vorschrift ist in 2D sauber ...": **nicht ausgeloest**, weil KG1 nicht auswertbar ist.
  - "KG1 oder KG2 verfehlt: ...": **nicht ausgeloest**.
  - Nach PLAN Abschnitt 7 berichte ich in diesem Fall die Schranken (Abschnitt 3) gegen die 4D-Groesse, getrennt vom
    Kartenurteil.
- **Zu KG1 (Pflichtvermerk):** nicht auswertbar heisst hier: Die Antwort ist bei allen drei Amplituden mit null
  vertraeglich. Eine Steigung laesst sich nicht bestimmen. Die vorab befuerchtete Lage [K3] ist eingetreten.
- **Zu KG3 (Pflichtvermerk):** Das Karten-"eingetroffen" ist ein Punktschaetzer mit SE_r = 1,64. Das 2-SE-Intervall
  umfasst null und das Vierfache der Vorhersage. Nicht zitierfaehig als Bestaetigung von Polyakov.
- **Zu KG0 [K2]:** fuer Gamma vorab entschieden (Netz und Sehnen sind fuer M exakte Bilder, M netzgleich in 480 von 480
  Netzen). Es ist eine Codekontrolle, kein Test.

**Agenten-Vorhersagen** (PLAN Abschnitt 10, vor den Hauptlaeufen)

| Nr | Vorhersage | Wahrsch. | Ergebnis |
|---|---|---|---|
| A1 | Tor ohne Ausschluss | 95 % | **eingetroffen** |
| A2 | K0 bitgleich | 95 % | **eingetroffen** (80/80) |
| A3 | KG0 (Plan) eingetroffen | 99 % | **eingetroffen** |
| A4 | KG0-Nebenlesart Gamma_M eingetroffen | 35 % | **eingetroffen** |
| A5 | KG1 nicht auswertbar | 80 % | **eingetroffen** |
| A6 | KG2 eingetroffen | 85 % | **eingetroffen** |
| A7 | KG3 nach Plan nicht entschieden | 90 % | **eingetroffen** |
| A8 | kein 4D-artiger Anteil (abs(b(K-0.1)) <= 0,3 und abs(D) <= 0,5) | 80 % | **eingetroffen** (0,067; 0,128) |

## 3. Skalierung mit N und Amplitude [E]

### 3.1 Delta Gamma je Verformung und N (Mittel +- SE ueber 120 Saaten; Std je Saat in Klammern)

| X | N = 1000 | 2000 | 4000 | 8000 | b (1000 bis 4000) | pred |
|---|---|---|---|---|---|---|
| M | 0 (Rundung 6e-10) | 0 | 0 | 0 | -1,7e-12 +- 1,7e-12 | 0 |
| K-0.025 | +0,013 +- 0,018 (0,20) | +0,012 +- 0,023 | +0,032 +- 0,035 | -0,028 +- 0,047 (0,52) | +0,019 +- 0,015 | -0,00036 |
| K-0.05 | +0,024 +- 0,036 (0,39) | +0,017 +- 0,046 | +0,066 +- 0,069 | -0,085 +- 0,090 (0,99) | +0,036 +- 0,029 | -0,0014 |
| **K-0.1** | **+0,041 +- 0,068 (0,74)** | **-0,010 +- 0,091 (0,99)** | **+0,169 +- 0,131 (1,43)** | **-0,185 +- 0,171 (1,87)** | **+0,067 +- 0,057** | -0,0056 |
| K-0.2 | -0,017 +- 0,115 (1,26) | -0,043 +- 0,167 | +0,320 +- 0,227 | -0,448 +- 0,313 (3,43) | +0,087 +- 0,102 | -0,022 |
| K-0.4 | -0,246 +- 0,177 (1,94) | -0,269 +- 0,264 | +0,274 +- 0,333 | -0,971 +- 0,526 (5,76) | -0,081 +- 0,143 | -0,087 |
| K+0.05 | -0,031 +- 0,037 (0,41) | -0,001 +- 0,046 | -0,041 +- 0,068 | +0,051 +- 0,090 | -0,024 +- 0,031 | -0,0014 |

- **Vergleich mit 4D (KOVARIANZ-KUGEL-1, K, eps = -0,1):** Delta Gamma = -16 / -27 / -48 bei N = 1000 / 2000 / 4000,
  je Punkt -0,016 / -0,014 / -0,012. In 2D: je Punkt +4e-5 / -5e-6 / +4e-5 / -2e-5 (N = 1000 bis 8000). In der 4D-Groesse
  y = Delta Gamma/sqrt(N): 2D +0,0013 / -0,0002 / +0,0027 / -0,0021 gegen 4D -0,505 / -0,611 / -0,758.
- **Wachstum mit N** (gewichteter Ausgleich b = beta + alpha N ueber alle vier N, beschreibend): alpha je Punkt
  -3,5e-6 +- 6,7e-6 (-0,025), -1,0e-5 +- 1,3e-5 (-0,05), -1,8e-5 +- 2,5e-5 (-0,1), -2,6e-5 +- 4,4e-5 (-0,2),
  -3,4e-5 +- 7,1e-5 (-0,4), +8,3e-6 +- 1,3e-5 (+0,05). Alle innerhalb 1 SE von null. 4D bei -0,1: etwa -0,011 je Punkt
  (von Hand aus -16 und -48).
- **KG2-Zusatzzeilen** (Aenderung 1000 -> 4000 in SE): 0,49 / 0,54 / 0,87 / 1,33 / 1,38 / -0,13 (eps = -0,025 bis
  -0,4, +0,05); 1000 -> 8000: -0,80 / -1,12 / -1,23 / -1,29 / -1,31 / +0,83. Alle "eingetroffen". Die Vorzeichen sind
  ueber die Amplituden gleich, weil dieselben Punkte eingehen (Rauschen korreliert).
- Std je Saat waechst wie sqrt(N) und etwa linear mit abs(eps): bei eps = -0,1 etwa 0,023 sqrt(N), also rund
  0,23 abs(eps) sqrt(N). Das liegt im vorab geschaetzten Bereich (VORAB S6: 0,1 bis 1).

### 3.2 Amplitude [E]

- **Linear- und Quadratglied** (b(eps) = A1 abs(eps) + A2 eps^2 ueber die fuenf negativen Amplituden, je Saat,
  beschreibend): A1 = +1,00 +- 0,68, A2 = -3,0 +- 1,2 (Polyakov aus denselben Ausgleich: -0,003 und -0,50).
  - Je N: A1 = +0,57 +- 0,76 / +0,23 +- 1,04 / +2,20 +- 1,54 / -1,84 +- 1,94. Je Punkt also hoechstens 0,0021 /
    0,0012 / 0,0013 / 0,0007 (2 SE).
  - 4D-Linearglied je Punkt: 0,016/0,1 = 0,16 (N = 1000) bzw. 0,12 (N = 4000).
  - A1 und A2 sind wegen fast kollinearer Spalten stark gegenlaeufig korreliert; einzeln 1,5 bzw. 2,4 SE von null,
    gegen Polyakov 1,5 bzw. 2,0 SE. Kein Befund.
- **Steigungen (beschreibend):** ueber die drei kleinsten Amplituden 0,91 +- 0,22, paarweise 0,93 / 0,89 / 0,37; ueber
  E_FIT und alle fuenf nicht definiert (Vorzeichenwechsel).
  - Diese Steigung um 1 ist **kein** lineares Signal. Alle drei b liegen unter 1,5 SE, und ihr gemeinsames Rauschen
    ist ungerade in eps.
  - Zerlegung bei abs(eps) = 0,05: ungerader Teil (b(-0,05) - b(+0,05))/2 = +0,030, gerader Teil +0,006.
  - Ein in eps ungerades Rauschen gibt fuer jede Rauschziehung Steigung 1. Deshalb verlangt die KG1-Regel 3 SE.
- **Gegenvorzeichen:** b(+0,05) = -0,024 +- 0,031, b(-0,05) = +0,036 +- 0,029: entgegengesetzt, beide mit null
  vertraeglich. Ein 4D-artiger Anteil in abs(eps) haette fuer beide Vorzeichen dasselbe Vorzeichen.
- **Nachtrag [N]** (nach der Auswertung, jq, nicht im Plan): Die gepaarte Summe Delta Gamma(+0,05) + Delta Gamma(-0,05)
  ist -0,006 +- 0,017 / +0,017 +- 0,023 / +0,025 +- 0,032 / -0,034 +- 0,049 (N = 1000 / 2000 / 4000 / 8000); Polyakov:
  -0,0027. Die Summe senkt das Rauschen nur um etwa den Faktor 2; es gibt also auch geraden Rauschanteil.

### 3.3 Netze [E]

| | N = 1000 | 8000 |
|---|---|---|
| neue Dreiecke K-0.025 / -0.05 / -0.1 / -0.2 / -0.4 / +0.05 | 0,035 / 0,067 / 0,127 / 0,226 / 0,321 / 0,070 | 0,035 / 0,069 / 0,130 / 0,226 / 0,320 / 0,070 |
| M: Netz gleich dem runden; Punkte gegen rund (relativ zu a) | 120 von 120; 1,3e-13 | 120 von 120; 2,0e-13 |
| max abs(Summe V_g/N - 1) | <= 9,6e-7 | <= 6,2e-10 |
| V_Sehnen/N (Sehnendreiecke gegen Kugelflaeche) | 0,9940 (M) bis 0,9928 (K-0.4) | 0,9992 bis 0,9991 |
| Laufzeit je Saat (rund und sieben Verformungen) | 0,67 s | 5,07 s |

- Zum Vergleich 4D bei eps = -0,1: 60 % neue Simplizes, V_Sehnen/N = 0,80 (N = 1000).

## 4. Diagnose-Variante und Nebenlesarten [E]

- **Ohne Volumenzuordnung je Simplex (CI):** Gamma_CI = Gamma_QI in allen 3360 verformten Netzen auf hoechstens 1,1e-9
  (Rundung bei Gamma bis etwa 5600), rund Q = C auf 1,7e-10. Wie vorab abgeleitet [K1]: In 2D sieht Gamma die
  Volumenzuordnung nicht. G_CI-Tabelle daher gleich 3.1.
- **Gamma_M** (Massenmatrix; sieht die Volumenzuordnung). Lesart GM_QI mit Volumenzuordnung, GM_CI_korr ohne
  Volumenzuordnung, mit globaler Korrektur:
  - b(GM_QI) = +0,056 +- 0,083 / +0,055 +- 0,128 / +0,092 +- 0,162 / +0,138 +- 0,226 / -0,027 +- 0,300 / +0,021 +- 0,118
    (eps = -0,025 bis -0,4, +0,05), alle mit null vertraeglich.
  - GM_CI_korr weicht davon um 0,001 (eps = -0,025) bis 0,20 (eps = -0,4) ab, jeweils innerhalb der SE.
  - Bei N = 8000 liegen mehrere Amplituden bei -1,7 bis -2,0 SE (z. B. K-0.05: -0,64 +- 0,32); dieselben Punkte gehen in
    alle Amplituden ein. Ich lese das als eine korrelierte Schwankung, kein Befund.
- **Moebius-Rest in Gamma_M** (Volumenzuordnung allein, 2D-Gegenstueck des 4D-Rests -0,0017):
  - je N +0,0037 +- 0,0014 / -0,0026 +- 0,0013 / +0,0016 +- 0,0013 / +0,0028 +- 0,0012, gemittelt +0,0009 +- 0,0009.
  - Hoechstens 4e-6 je Punkt. Die Werte je N streuen etwas mehr als ihre SE (chi^2 etwa 14 bei 3 FG, von Hand, beschreibend).
  - CI korr ist exakt null (Moebius-Bilder).

## 5. Kontrollen [E]

- **Kontrolllauf lauf-69/kontrolle.json** (eingefrorener Code, 14:41:46 bis 14:42:10 UTC, cpu, rc 0). Alle Schwellen
  erfuellt, Werte gleich dem Kontrolllauf vor dem Einfrieren:
  - C1 (sigma = 0): 0 neue Dreiecke; Gamma_QI - Gamma_Q = 1,1e-13; Gamma_CI - Gamma_C = 0,0.
  - C2 (Moebius): Transport gegen die exakte Abbildung 1,4e-14; Netz gleich; Punkte gleich 2,1e-14; Gamma QI und CI
    gegen rund 0,0.
  - C3 (N = 400): LU gegen dichte Eigenwerte und slogdet <= 4,0e-13, Gamma_M gegen verallgemeinerte Eigenwerte <= 2,8e-13
    (M, K-0.1, K-0.4).
  - C5: Gamma_QI - Gamma_CI = 0,0 fuer alle sieben Verformungen.
  - **K4D:** n = 4, Saat 0, N = 1000. Rund Q/C, M und K, QI/CI, Gamma und Gamma_M sind gegen kovarianz.py (live) und
    gegen dessen Laufdatei bitgleich (Abweichung 0,0).
- **Vorab-Proben:** Polyakov(M) 8,9e-16; kleines eps gegen -8/15 relativ 1,9e-4; M-Profil 4,6e-15; Flaeche 3e-15.
- **In jedem Netz:** Transportrest <= 1,1e-16; Huellenpruefungen; Gauss-Bonnet <= 2,5e-12; LU ok fuer QI und CI;
  kleinster Gram-Eigenwert der Sehnendreiecke > 0 in allen Netzen (min 1,8e-8 bei N = 8000).

**Latten (v3):**
- **L1 (kann scheitern):** ja. KG2 haette bei einem mit N wachsenden Anteil scheitern muessen (Trennschaerfe etwa 0,4
  gegen erwartet -32 beim 4D-Muster). KG1 haette bei einem linearen Anteil "nicht eingetroffen" ergeben. KG0 war fuer
  Gamma vorab entschieden [K2].
- **L2 (Gegenprobe):** zwei Laengenregeln, zwei Masse (Gamma, Gamma_M), sechs Amplituden mit Gegenvorzeichen, vier N,
  120 Saaten; bitgleiche Reproduktion von KUGEL-1 (K0) und von kovarianz.py (K4D).
- **L3 (Numerik):** log det etwa 1e-12 absolut; SE(b) 0,015 bis 0,14.
- **L4 (schon bekannt):** Polyakov-Alvarez- und OPS-Formel, Onofri-Ungleichung [L]; Kotangens-Laplace haengt nur von
  Winkeln ab [L, M]; Polyakov auf dem Torus im Projekt gemessen (INDUZIERT-DICHTE-2D, -GROB) [P]. Eine Rechnung dieser
  Art auf S^2 kenne ich nicht; nicht gesucht [L?].
- **L5 (Messbezug):** keiner (2D euklidisch, synthetisch).

## 6. Folgerung fuer KOVARIANZ-KUGEL-1 [ES, H]

- **Was ausgeschlossen ist:**
  - Ein Fehler in den Teilen, die 2D und 4D teilen. Das sind Transport (Umordnung in theta), Huelle in der konformen
    Karte, Einbettungssehnen, Neuvernetzung, Paarung, Gamma-Auswertung und Moebius-Nullprobe.
  - Diese Teile sind nachweislich derselbe Code (K4D bitgleich) und erzeugen in 2D keinen mit N wachsenden und keinen
    in abs(eps) linearen Anteil, auf 0,6 bis 1,3 % der 4D-Groesse je Punkt (2-SE-Schranken).
  - Ein reines Paarungs- oder Neuvernetzungsartefakt dieser Art ist damit ebenfalls unwahrscheinlich: In 2D werden
    bis zu 32 % der Dreiecke neu gebaut, ohne Spur.
- **Was nur 4D hat** (die Gegenprobe kann es nicht pruefen):
  - (a) Die P1-Steifigkeit ist in 4D vom Grad 2 in den Laengen. Groesse und Form jedes Simplex (Regel QI wie CI) gehen in
    Gamma ein; in 2D nur die Winkel [K1].
  - (b) 4D-Delaunay-Netze: keine Energie-Minimalitaet wie in 2D (Rippa [L]); Gamma springt beim Kippen. In 2D ist der
    Delaunay-Kotangens-Laplace stetig [L, M]. Dazu kippen in 4D 60 % der Simplizes, in 2D 13 %.
  - (c) Grobheit: In 4D fehlen den Sehnensimplizes 20 % Volumen, in 2D 0,6 %. h^2 R ~ 1 bis 2 gegen h^2 K0 <= 0,025 [K4].
- **Schreibtisch-Schluss (VORAB S5):**
  - Eine kovariante Konstruktion mit glatter Abhaengigkeit gibt eine quadratische Antwort ohne N-Wachstum; das sieht
    man hier in 2D (im Rahmen des Rauschens).
  - Das 4D-Muster verlangt dort also einen nicht kovarianten oder nicht glatten Anteil, der an (a) bis (c) haengt.
- **Fuer die Karte KOVARIANZ-KUGEL-1:**
  - Die 4D-Zahlen sind kein Codefehler im gemeinsamen Teil.
  - Ob "auf diesem 4D-Netz nicht Einstein" Physik des Netzes ist oder ein 4D-eigener Konstruktionseffekt (zum Beispiel
    der Laengen- und Volumenregel in einer laengenabhaengigen Steifigkeit), entscheidet diese Gegenprobe nicht.
  - Vor einer Deutung als Physik sollte ein 4D-eigener Effekt ausgeschlossen werden.
- **Naechste Schritte [H]:**
  - (1) **4D mit Gegenvorzeichen** (eps = +0,025 ist in 4D einbettbar, eps = -0,025 vorhanden), dieselben Saaten:
    - glatte Antwort: Delta Gamma(+eps) etwa gleich Delta Gamma(-eps);
    - ungerader Anteil erster Ordnung: entgegengesetzte Vorzeichen;
    - nicht glatter Anteil in abs(eps): gleiches Vorzeichen bei linearer Skalierung.
    - Das ist die billigste scharfe Probe auf die 4D-Ursache.
  - (2) **S^3-Gegenprobe:** Steifigkeit vom Grad 1, 3D-Delaunay ohne Minimalitaet, Grobheit einstellbar. Dafuer muesste
    kugel.py um n = 3 erweitert werden; kovarianz2d.py ist schon allgemein in n.
  - (3) **4D mit kleineren Amplituden** (eps = -0,01, -0,005; Vorschlag aus KOVARIANZ-KUGEL-1).

## 7. Kartenpunkte (vor dem Rechnen offengelegt) und was daraus wurde

- **[K1] Volumenzuordnung wirkt in 2D nicht auf Gamma:** bestaetigt (Gamma_QI = Gamma_CI auf 1e-9 in 3360 Netzen).
  Die Diagnose-Variante war fuer Gamma leer. Nur Gamma_M sieht die Zuordnung; dort keine Auffaelligkeit.
- **[K2] KG0 fuer Gamma vorab entschieden:** so eingetreten (-1,7e-12).
- **[K3] KG1 und KG3 voraussichtlich nicht entscheidbar:** so eingetreten (KG1 nicht auswertbar, KG3 nach Plan nicht
  entschieden).
- **[K4] Grobheit:** bleibt die wichtigste Grenze der Gegenprobe (Abschnitt 6 (c)).
- **[K5] Delta Gamma statt Delta Gamma/sqrt(N):** so geurteilt; y wird zum Vergleich mitberichtet.
- **[K6] KG3 gegen kappa_GROB:** so geurteilt; Verhaeltnis zu kappa = 1: 0,99 (ebenso im Rauschen).
- **[K7] 120 Saaten:** reichten fuer die Anomaliefrage mit grossem Abstand; fuer KG3 waeren etwa 10^4 noetig.

## 8. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:**
   - Keine Gamma-Werte oder Mittel verformter Netze.
   - Gesehen: Kontinuumsvorhersagen, Kontrollabweichungen (<= 4e-13, K4D bitgleich), blinde Streuungen (10 bzw. 4
     Rauchsaaten), Kippanteile, Zeiten und Gueltigkeit.
   - C5 zeigte Gamma_M(QI) - Gamma_M(CI) im selben Netz (etwa -2,3); das ist keine Antwort auf die Verformung.
   - Von der Codeprobe nur die Struktur (jq keys). Ihre Werte und Urteile habe ich nicht gelesen.
2. **Codeaenderungen:** Nach Kontrolle und Rauchlauf, vor dem Einfrieren, nur in der Auswertung: A1/A2-Ausgleich, KG2
   mit allgemeinen Haupt-N und Zusatzzeile bis N = 8000, Parameter fuer die Codeprobe. Ohne Kenntnis von Messwerten; der
   Messteil blieb unveraendert. Die Kontrolle mit eingefrorenem Code gab dieselben Werte.
3. **E_FIT und EPS_KG3** standen vor dem Rauchlauf im Code (meine Schaetzung); der Rauchlauf hat sie nur ueber das
   Rauschen bestaetigt. Der Plan sagt das ausdruecklich (nach einer Berichtigung des Plantexts vor dem Einfrieren).
4. **VORAB.md Abschnitt 4** entstand nach dem vorab-Lauf, wie in KOVARIANZ-KUGEL-1; das ist reine Quadratur, keine
   Gitterzahl. Abschnitte 1 bis 3 standen vor jeder Rechnung.
5. **Nach der Auswertung, nicht im Plan:**
   - Nachtrag [N] gepaarte Summe +-0,05 (jq).
   - Pruefung Gamma_QI = Gamma_CI ueber alle Netze (jq).
   - Zerlegung ungerade/gerade, chi^2 der Moebius-Gamma_M-Werte, 4D-Vergleichsgroessen je Punkt (von Hand).
6. **Beschreibende Steigung "klein3" (0,91):** von mir vorab als Zusatz festgelegt, liest sich aber irrefuehrend
   (Abschnitt 3.2). Ich habe sie nicht als Befund gefuehrt.
7. **ssh-Verbindungen:** hoechstens zwei Spurketten und zwei kurze Abfragen zugleich. Mein N = 1000-Lauf wartete etwa
   5 min auf den Lock von cpu4; fremde Units habe ich nur gelistet (systemctl --user list-units), nicht angefasst.
8. **Auf der .69 ausserhalb des Starters:** mkdir, mv, sha256sum, grep, ls, cat, tail, cut, tr, date, uptime,
   systemctl --user list-units (lesen). Kein Python ausserhalb des Starters.
9. **Lokal:** kein python, awk oder perl. Benutzt: jq, sed (Textberichtigungen in ERGEBNIS.md), grep, sha256sum, date,
   ssh, scp, cp, mv (nur auf der .69),
   mkdir, ls, cat, wc, cut und sleep in until-Warteschleifen. Nichts geloescht.
10. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
    unter /tmp/claude-1000/.../tasks/ an (nur Rueckgabecodes und Laufmeldungen).
11. **Zeitbox:** Start 16:12:18 CEST, Text fertig 2026-10-04 17:03:13 CEST (date), also rund 59 min von 120.

## 9. Dateien

- KARTE.md (Leitung), VORAB.md, VORAB.md.eingefroren-20261004-164140, PLAN.md, PLAN.md.eingefroren-20261004-164140,
  EINGEFROREN-SHA256.txt.
- code/:
  - kovarianz2d.py (neu, n allgemein) mit Kopie *.eingefroren-20261004-164140.
  - Unveraendert kopiert, je mit eingefrorener Kopie: kugel.py, kugel2.py, dichte4d.py, induziert.py, zufall2d.py,
    kovarianz.py (nur fuer K4D).
- rauch-69/:
  - vorab.json/.log, kontrolle.json/.log (Code vor der Auswertungsaenderung), rauch-a.json/.log, rauch-b.json/.log
    (blind).
  - probe/probe-aw.json (Codeprobe; nur Struktur gelesen).
- lauf-69/:
  - kontrolle.json/.log; messung-N1000-s0, -N2000-s0, -N4000-s0, -N8000-s0, -N8000-s60 (.json/.log).
  - auswertung.json/.log (Tor, K0, Messgroessen, Steigungen, Zusatz A1/A2, Netze, Urteile, Vorab).
  - PRUEFSUMMEN.txt (.69, 14 Dateien, lokal geprueft).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde41-kovarianz-2d/ (code/, rauch/, lauf/).

## 10. Einfach gesagt

- Im vierdimensionalen Netz hatte eine verbeulte Kugel eine viel zu starke Reaktion gezeigt, die mit der Zahl der
  Punkte wuchs. Das darf eine saubere Rechnung nicht.
- Wir haben genau dieselbe Bauanleitung, mit nachweislich demselben Programmcode, auf eine gewoehnliche Kugeloberflaeche
  angewendet. Dort ist die richtige Antwort aus der Lehrbuchphysik bekannt und sehr klein.
- Dort ist von einer solchen Reaktion nichts zu sehen: Sie waechst nicht mit der Punktzahl und ist mindestens
  siebzigmal kleiner als der Effekt, den wir in vier Dimensionen gesehen haben.
- Der allgemeine Teil der Anleitung und des Codes ist also nicht schuld. Die Ursache steckt in etwas, das es nur in vier
  Dimensionen gibt, oder in der Grobheit des 4D-Netzes.
- Die winzige Lehrbuchantwort selbst geht auf der Kugel im Zufallsrauschen unter; ihre genaue Groesse konnten wir
  deshalb nicht pruefen.
