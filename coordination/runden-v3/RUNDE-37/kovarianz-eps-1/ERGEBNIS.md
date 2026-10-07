# KOVARIANZ-EPS-1: Ergebnis (Runde 42, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 17:04:46 CEST. Code bis etwa 17:24, vorab 15:24:56 bis 15:25:03 UTC, Kontrolle 15:25:09 bis
    15:25:54, Rauchlaeufe 15:25:54 bis 15:30:00 (blind), Codeprobe 15:31:25 bis 15:36:11 UTC (nur Struktur). VORAB.md ab
    17:33:33 CEST, PLAN.md ab 17:36:29 CEST.
  - Eingefroren 17:38:12 CEST: PLAN.md.eingefroren-20261004-173812, VORAB.md.eingefroren-20261004-173812, Code-Kopien
    *.eingefroren-20261004-173812, Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 15:38:27 bis 16:27:19 UTC (1 Kontrolle, 13 Messlaeufe, alle rc 0), Auswertung 16:27:25 bis 16:27:33 UTC
    (rc 0). Text ab 18:29:35 CEST.
- Code nach dem Einfrieren unveraendert: sha256 aller acht Dateien auf der .69 vor der Auswertung gleich den
  eingefrorenen (kovarianz_eps.py 5882e76d...). lauf-69/PRUEFSUMMEN.txt (.69, 30 Dateien) lokal nachgeprueft: 30 von 30.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu und cpu4).
  Euklidisch, eine Schleife, freies masseloses Skalarfeld (P1), synthetisch, keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [E] hier gerechnet, [ES] eigener Schluss, [F] Festlegung im Plan,
  [K] Kartenpunkt (vor dem Rechnen offengelegt), [H] Hypothese, [L] Literatur aus dem Gedaechtnis, [P] Projektdatei,
  [N] Nachtrag nach der Auswertung (nicht im Plan, beschreibend).
- **Konvention (wie KOVARIANZ-KUGEL-1):** y = Delta Gamma/sqrt(N), Delta Gamma = Gamma_QI(verformt) - Gamma_Q(rund),
  gepaart je Saat und N; b = Saatmittel des Mittels ueber N = 1000, 2000, 4000, SE aus 40 Saaten (0 bis 39). Gerader
  Anteil G(e) = (y(+e) + y(-e))/2, ungerader U(e) = (y(+e) - y(-e))/2. Einstein: y_E = beta_Q Delta S_1/(32 pi^2),
  N-unabhaengig, gerader Teil bei e = 0,05: -0,0137.
  - (a) = Neuvernetzung wie KOVARIANZ-KUGEL-1; (b) = mitgenommene Verbindungen (rundes Netz, Punkte verschoben, Laengen
    neu, Regel QI mit |V_g|).

## 1. Ergebnis zuerst

1. **Kernaussage: Ja, die Nicht-Glaette liegt an der Neuvernetzung (Regel PLAN Abschnitt 7: KE1 und KE2 nach Plan
   eingetroffen) [E].**
   - Mit Neuvernetzung (a) ist Delta Gamma bei +eps und -eps negativ. Das gilt fuer alle vier Werte, je mindestens 15 SE.
   - Der gerade Anteil von (a) waechst nur wie eps^1,31 +- 0,06 (0,025 auf 0,05), also nicht quadratisch.
   - Mit mitgenommenen Verbindungen (b) ist die Antwort quadratisch: Steigung 2,010 +- 0,022, ungerader Anteil 10 bis
     15 % des geraden.
2. **Aber (b) ist nicht Einstein [E].** G_b(0,05) = **+0,154 +- 0,002** gegen Einstein -0,0137: falsches Vorzeichen,
   Betrag das 11-Fache. Der gerade Anteil waechst von N = 1000 auf 4000 um 126 % (27 SE). KE3 und KE4 sind nicht
   eingetroffen.
   - Groesse, Vorzeichen und N-Abhaengigkeit treffen die vorab berechnete Scherprognose (VORAB Abschnitt 3).
   - Das feste Netz wird durch den massstreuen Transport geschert und gibt Delta Gamma = c N <tr H^2> mit c = 1/24.
   - Gemessen/vorhergesagt liegt in allen 21 Zellen (7 Amplituden, 3 N) zwischen 0,72 und 1,17, in 20 davon zwischen
     0,87 und 1,17 [N].
3. **(a) im Einzelnen [E].**
   - +eps antwortet staerker als -eps (b = -0,178 gegen -0,134 bei 0,025; -0,459 gegen -0,316 bei 0,05).
   - Der ungerade Anteil ist 14 bis 18 % des geraden.
   - Die Antwort waechst mit N: G_a(0,05) = -0,32 / -0,37 / -0,48 bei N = 1000 / 2000 / 4000.
   - Wo vergleichbar, ist (a) bitgleich mit KOVARIANZ-KUGEL-1 (120 von 120 bei -0,1; 90 von 90 im
     Amplituden-Nachtrag).
4. **Lesart [M, ES].**
   - In (a) ist der Erwartungswert exakt die Differenz zweier frischer Ensembles (verformte gegen runde Kugel). Die
     Umschaltspruenge der Paarung verschieben ihn nicht. "An der Neuvernetzung" heisst also: an den neu gebauten
     Delaunay-Netzen der verformten Kugel selbst, nicht an einem Paarungsartefakt.
   - Ohne Neuvernetzung tritt ein anderer, verstandener Gittereffekt an seine Stelle.
   - Keine der beiden Bauweisen misst auf diesem 4D-Netz Einsteins Glied: (a) ist nicht quadratisch und 28-mal zu gross
     (bei 0,05), (b) ist vom Scherterm beherrscht, der 11-mal groesser ist als Einstein und das andere Vorzeichen hat.
5. **KE0 nicht eingetroffen, wie vorab abgeleitet [K2].** Die Moebius-Nullprobe gibt in (b) b_M = -0,0019 +- 0,0003
   (-6,0 SE). Ursache ist die Volumenzuordnung je Simplex, in (a) und (b) dieselbe Zahl. Die Reproduktion (Teil 1) ist
   eingetroffen: 120 von 120 Werten bitgleich mit KOVARIANZ-KUGEL-1.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch kovarianz_eps.py auswertung; Werte in lauf-69/auswertung.json.
**Tore bestanden:** (a), (b) und D je 40 von 40 Saaten bei allen drei N gueltig. Das sind 120 runde, 600 (a)- und
1200 (b)-Netze (davon 240 D), jedes mit LU ok und Transportrest <= 1e-10. Ausgeschlossen 0, unvollstaendig 0.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| KE0 | (a) reproduziert KOVARIANZ-KUGEL-1 bei eps = -0,1; Moebius in (b) innerhalb 3 SE um null | 85 % | **nicht eingetroffen** | **nicht eingetroffen** | Teil 1 eingetroffen: 120/120 bitgleich (a K-0,1 und rund Q, Abweichung 0,0); b_a(-0,1) = -0,629 +- 0,015 (40 Saaten) gegen -0,625 +- 0,008 (120). Teil 2 nicht: b_M = -0,00187 +- 0,00031 (-6,0 SE), 0,3 % von b_a(-0,1) |
| KE1 | [H] (a): gleiches Vorzeichen bei +eps und -eps (nicht glatt), bei 0,025 und 0,05 | 60 % | **eingetroffen** | **eingetroffen** | b(+-0,025) = -0,178 +- 0,011 / -0,134 +- 0,009; b(+-0,05) = -0,459 +- 0,012 / -0,316 +- 0,013 (alle >= 15 SE, alle 40 Saaten negativ). Steigung des geraden Anteils 1,314 +- 0,058 (+2 SE = 1,43 < 1,7) |
| KE2 | [H] (b): glatt (gerader Anteil Steigung 1,7 bis 2,3; ungerader unter 20 % des geraden) | 55 % | **eingetroffen** | **eingetroffen** | Steigung 2,010 +- 0,022; U/G = 0,114 (0,025) und 0,145 (0,05); abs(U) + 2 SE < 0,2 abs(G) bei beiden |
| KE3 | [H] (b): gerader Anteil unabhaengig von N (1000 auf 4000 unter 15 % bzw. 2 SE) | 40 % | **nicht eingetroffen** | **nicht eingetroffen** | e = 0,05: G = 0,0974 +- 0,0036 -> 0,2203 +- 0,0029, Aenderung +0,123 +- 0,005 (+126 %, 26,9 SE). Zusatz e = 0,0125 / 0,025: +111 % / +123 %, ebenfalls nicht |
| KE4 | [H] (b): Einstein-Vorzeichen und innerhalb Faktor 3 der Vorhersage aus B | 25 % | **nicht eingetroffen** (falsches Vorzeichen, >= 3 SE) | **nicht eingetroffen** | G(0,05) = +0,1541 +- 0,0019 gegen y_E = -0,0137 +- 0,0004; Verhaeltnis -11,2 +- 0,4. Zusatz 0,0125 / 0,025: -9,6 / -11,1 |

- **Bedeutung, wie vorab auf der Karte festgelegt:** "KE1 und KE2 treffen ein: Die 4D-Anomalie ist ein
  Neuvernetzungs-Effekt. Mit mitgenommenen Verbindungen ist die Antwort glatt; ob sie Einstein ist, sagen KE3 und KE4":
  **ausgeloest**. KE3 und KE4 sagen: nicht Einstein. "KE2 verfehlt ...": nicht ausgeloest.
- **Kernaussage nach PLAN Abschnitt 7:** ja (KE1 und KE2 nach Plan eingetroffen), mit den dort vorab festgelegten
  Lesarten: nicht als Umschaltartefakt [M] und nicht als "(b) ist Einstein" [H, hier bestaetigt].
- **Zu KE1 [K1]:** Das Kartenurteil (gleiches Vorzeichen) waere auch bei glatter gerader Antwort eingetroffen. Der Plan
  hat deshalb zusaetzlich die Steigung des geraden Anteils verlangt; sie liegt mit 1,31 +- 0,06 klar unter 1,7.
- **Zu KE0 [K2]:** Teil 2 war vorab bestimmt (VORAB Abschnitt 4: erwartet -0,0017 +- 0,0003, etwa -5 SE). KE0 ist damit
  im Wortlaut verfehlt, ohne dass eine Kontrolle unerwartet angeschlagen hat. Kein Wesentlichkeitsrabatt.

**Agenten-Vorhersagen** (PLAN Abschnitt 10, vor den Hauptlaeufen)

| Nr | Vorhersage | Wahrsch. | Ergebnis |
|---|---|---|---|
| A1 | Tore ohne Ausschluss | 90 % | **eingetroffen** |
| A2 | KE0 Teil 1 eingetroffen | 97 % | **eingetroffen** |
| A3 | KE0 Teil 2 eingetroffen | 10 % | nicht eingetroffen |
| A4 | KE1 nach Karte | 75 % | **eingetroffen** (siehe Selbstanzeige 1) |
| A5 | KE1 nach Plan | 50 % | **eingetroffen** |
| A6 | KE2 nach Karte | 75 % | **eingetroffen** |
| A7 | KE2 nach Plan | 60 % | **eingetroffen** |
| A8 | KE3 | 15 % | nicht eingetroffen |
| A9 | KE4 nach Karte | 10 % | nicht eingetroffen |
| A10 | G_b(0,05) > 0 | 75 % | **eingetroffen** (+0,154) |
| A11 | y_D > 0 fuer beide kappa (Saatmittel) | 90 % | **eingetroffen** (+0,026 und +0,242; bei N = 1000 ist D0,25 -0,005 +- 0,006) |

## 3. Tabellen

### 3.1 Delta Gamma gegen eps und N je Bauweise [E]

y = Delta Gamma/sqrt(N), Mittel +- SE ueber 40 Saaten; in Klammern Delta Gamma selbst (Mittel). Letzte Spalten:
Saatmittel b des N-Mittels, Vorhersage.

**(a) Neuvernetzung**

| eps | N = 1000 | 2000 | 4000 | b | y_E (Einstein) |
|---|---|---|---|---|---|
| -0,1 | -0,538 +- 0,022 (-17,0) | -0,601 +- 0,025 (-26,9) | -0,749 +- 0,023 (-47,3) | -0,629 +- 0,015 | -0,0554 |
| -0,05 | -0,259 +- 0,022 (-8,2) | -0,300 +- 0,022 (-13,4) | -0,389 +- 0,019 (-24,6) | -0,316 +- 0,013 | -0,0140 |
| -0,025 | -0,107 +- 0,020 (-3,4) | -0,127 +- 0,015 (-5,7) | -0,168 +- 0,017 (-10,6) | -0,134 +- 0,009 | -0,0035 |
| +0,025 | -0,138 +- 0,021 (-4,4) | -0,183 +- 0,018 (-8,2) | -0,212 +- 0,018 (-13,4) | -0,178 +- 0,011 | -0,0034 |
| +0,05 | -0,376 +- 0,016 (-11,9) | -0,433 +- 0,021 (-19,4) | -0,567 +- 0,020 (-35,9) | -0,459 +- 0,012 | -0,0134 |
| +0,1 | nicht baubar | | | | |

- Alle 40 Saaten negativ bei jeder Amplitude. Std je Saat des N-Mittels 0,05 bis 0,09.
- In allen 90 gemeinsamen (Saat, N) (N = 1000 und 2000: Saaten 0 bis 39; N = 4000: Saaten 0 bis 9) sind K-0,05,
  K-0,025 und rund Q zeichengleich mit dem Amplituden-Nachtrag von KOVARIANZ-KUGEL-1 [N, jq-Vergleich,
  vergleich-amplituden-*.txt].

**(b) Mitgenommene Verbindungen** (Vorhersage = Scherprognose c = 1/24 plus Einstein, VORAB Abschnitt 3; Spalte
gemessen/vorhergesagt fuer b [N])

| eps | N = 1000 | 2000 | 4000 | b | Vorhersage b | gem./vorh. |
|---|---|---|---|---|---|---|
| -0,1 | +0,381 +- 0,009 (+12,1) | +0,569 +- 0,007 (+25,4) | +0,860 +- 0,006 (+54,4) | +0,603 +- 0,004 | +0,652 | 0,92 |
| -0,05 | +0,113 +- 0,004 (+3,6) | +0,165 +- 0,003 (+7,4) | +0,251 +- 0,003 (+15,9) | +0,177 +- 0,002 | +0,158 | 1,12 |
| -0,025 | +0,0277 +- 0,0019 (+0,88) | +0,0384 +- 0,0019 (+1,72) | +0,0618 +- 0,0014 (+3,91) | +0,0426 +- 0,0010 | +0,0381 | 1,12 |
| -0,0125 | +0,0063 +- 0,0008 (+0,20) | +0,0077 +- 0,0012 (+0,35) | +0,0136 +- 0,0010 (+0,86) | +0,0092 +- 0,0006 | +0,0093 | 0,99 |
| +0,0125 | +0,0053 +- 0,0007 (+0,17) | +0,0061 +- 0,0011 (+0,27) | +0,0110 +- 0,0012 (+0,69) | +0,0075 +- 0,0006 | +0,0089 | 0,84 |
| +0,025 | +0,0219 +- 0,0018 (+0,69) | +0,0308 +- 0,0020 (+1,38) | +0,0489 +- 0,0020 (+3,09) | +0,0339 +- 0,0012 | +0,0346 | 0,98 |
| +0,05 | +0,0812 +- 0,0040 (+2,57) | +0,1241 +- 0,0036 (+5,55) | +0,1898 +- 0,0037 (+12,0) | +0,1317 +- 0,0024 | +0,1308 | 1,01 |
| M | -0,0022 +- 0,0008 | -0,0017 +- 0,0005 | -0,0018 +- 0,0004 | -0,0019 +- 0,0003 | -0,0017 (KK-1) | |
| D0,25 | -0,005 +- 0,006 | +0,027 +- 0,006 | +0,054 +- 0,006 | +0,026 +- 0,004 | +0,097 | 0,26 |
| D0,5 | +0,104 +- 0,010 | +0,234 +- 0,009 | +0,387 +- 0,008 | +0,242 +- 0,005 | +0,383 | 0,63 |

- (b) ist in fast allen Saaten positiv (je Amplitude 0 bis 2 von 40 negativ). Std je Saat des N-Mittels 0,004 bis
  0,027, bei gleicher Amplitude 3,5- bis 9-mal kleiner als in (a): Ohne Neuvernetzung bleibt die Paarung fast
  vollstaendig.
- Je Zelle (von Hand [N]): gemessen/vorhergesagt 0,72 bis 1,17. Effektives c = (G_b - y_E,gerade)/(sqrt(N)
  <tr H^2>_gerade) aus dem geraden Anteil: 0,043 / 0,043 / 0,045 (e = 0,05, N = 1000 / 2000 / 4000), 0,044 / 0,041 /
  0,045 (0,025), 0,041 / 0,034 / 0,040 (0,0125); Schaetzung vorab 1/24 = 0,042, Schranken 0 bis 0,0625.

### 3.2 Gerade und ungerade Anteile, Steigungen [E]

| Bauweise, e | G (N-Mittel) | U | U/G | G je N (1000 / 2000 / 4000) | y_E gerade |
|---|---|---|---|---|---|
| (a) 0,025 | -0,1557 +- 0,0089 | -0,0218 +- 0,0044 | 0,14 | -0,123 / -0,155 / -0,190 | -0,0034 |
| (a) 0,05 | -0,3872 +- 0,0106 | -0,0714 +- 0,0064 | 0,18 | -0,318 / -0,367 / -0,478 | -0,0137 |
| (b) 0,0125 | +0,0083 +- 0,0006 | -0,0009 +- 0,0002 | -0,11 | +0,0058 / +0,0069 / +0,0123 | -0,0009 |
| (b) 0,025 | +0,0383 +- 0,0010 | -0,0044 +- 0,0005 | -0,11 | +0,0248 / +0,0346 / +0,0554 | -0,0034 |
| (b) 0,05 | +0,1541 +- 0,0019 | -0,0224 +- 0,0010 | -0,15 | +0,0974 / +0,1447 / +0,2203 | -0,0137 |

| Steigung (ln abs(G) gegen ln e, Jackknife-SE) | Wert | Einstein / Scherung (vorab) |
|---|---|---|
| (a) gerader Anteil, 0,025 bis 0,05 (KE1) | **1,314 +- 0,058** | 1,991 / 1,989 |
| (b) gerader Anteil, 0,025 bis 0,05 (KE2) | **2,010 +- 0,022** | 1,991 / 1,989 |
| (b) gerader Anteil, 0,0125 bis 0,05 (Zusatz) | 2,105 +- 0,041 | |
| (a) einseitig, eps = -0,025 / -0,05 / -0,1 | 1,116 +- 0,042 | |
| (b) einseitig, eps = -0,025 / -0,05 / -0,1 | 1,911 +- 0,014 | |

- (a): Der ungerade Anteil ist negativ (+eps staerker) und waechst von 0,025 auf 0,05 um den Faktor 3,3; eine glatte
  Entwicklung verlangte dafuer eps^3 (Faktor 8). Der gerade Anteil waechst um 2,5 statt 4. Beides passt nicht zur
  Kleinsignal-Entwicklung, die fuer den Erwartungswert von (a) gelten muss (VORAB Abschnitt 2) [ES].
- (b): U/G ist bei 0,0125 / 0,025 / 0,05 etwa -0,11 / -0,11 / -0,15 (+eps schwaecher als -eps). Die Scherprognose
  allein gibt -0,02 / -0,04 / -0,09, also dasselbe Vorzeichen, aber weniger. Ein glatter ungerader Anteil faellt in U/G
  linear mit eps; bei 0,0125 waere etwa -0,06 zu erwarten, gemessen -0,105 +- 0,030 (1,6 SE). Nicht aufgeloest [N].

### 3.3 Netze [E]

| | N = 1000 | 2000 | 4000 |
|---|---|---|---|
| (a) neue Simplizes bei +-0,025 / +-0,05 / -0,1 | 0,23 / 0,39 / 0,60 | 0,24 / 0,40 / 0,61 | 0,24 / 0,41 / 0,62 |
| (b) umgeklappt je Netz bei -0,1 (Mittel, max; Netze ohne) | 0,7, 3; 21 von 40 | 1,4, 4; 8 | 1,8, 8; 1 |
| (b) umgeklappt bei -0,05 | 0,03, 1; 39 | 0,08, 1; 37 | 0,05, 1; 38 |
| (b) umgeklappt bei abs(eps) <= 0,025 und +0,05 | 0 | 0 bis 1 (1 Netz, bei +0,05) | 0 bis 1 (0 bis 2 Netze je Amplitude) |
| (b) D0,25 / D0,5 umgeklappt (Mittel) | 10 / 40 | 16 / 62 | 22 / 90 |
| (b) staerkste Quetschung V_Sehnen(b)/V_Sehnen(rund), +-0,025 | 0,66 / 0,87 | 0,44 / 0,86 | 0,47 / 0,88 |
| (b) entartete Sehnen-Simplizes | 0 | 0 | 0 |

- Signierte Summe V_g/N in (b) bei allen Netzen 1 auf <= 2,3e-4 (die Kugelsimplizes ueberdecken die Kugel mit Grad 1),
  die Betragssumme im Mittel hoechstens 1,0004.

### 3.4 Scherkontrolle D [E, beschreibend]

- D0,5: c_Scher = y_D/(sqrt(N) <tr H^2>_D) = 0,017 / 0,027 / 0,031 (N = 1000 / 2000 / 4000); D0,25: -0,003 / 0,012 /
  0,017. Beide liegen unter 1/24 und wachsen mit N.
- Die Faserdrehung kalibriert den Scherterm des K-Transports also **nicht**. Bereinigt man G_b(0,05) mit D0,5
  (G_b - 0,412 y_D0,5), bleibt +0,055 / +0,048 / +0,061 statt -0,0137. Moegliche Gruende [H]: In D klappen im Mittel
  10 bis 90 Simplizes je Netz um (hoechstens 111; im K-Transport bei abs(eps) <= 0,05 fast keine), und die Scherung von
  D ist eine Gleitung quer zur Faser, deren Betrag ueber die Faser stark schwankt (g = kappa rho sin theta).
- Fuer die Urteile spielt D keine Rolle (Zusatz [K5]).

## 4. Was das bedeutet [ES, H]

- **Was gezeigt ist [E]:**
  - Mit Neuvernetzung (a) bleibt das Vorzeichen bei +eps und -eps negativ. Der gerade Anteil waechst zwischen 0,025 und
    0,05 nur wie eps^1,3, und es gibt einen deutlichen ungeraden Anteil (+eps staerker). Die Antwort waechst mit N
    (Delta Gamma etwa wie N^0,8).
  - Mit mitgenommenen Verbindungen (b), auf denselben Punkten und mit derselben Laengenregel, ist die Antwort glatt und
    quadratisch (Steigung 2,01 +- 0,02). Sie ist aber positiv und waechst wie N.
  - Groesse, Vorzeichen und N-Gang von (b) stimmen mit der vorab geschaetzten Scherantwort des festen Netzes ueberein:
    gemessen/vorhergesagt je Zelle 0,72 bis 1,17, meist innerhalb 10 bis 15 %; c = 1/24 ohne freie Konstante, zulaessig
    waren 0 bis 1/16.
- **Was ich daraus schliesse [ES]:**
  - Die Nicht-Glaette von KOVARIANZ-KUGEL-1 entsteht nur, wenn das Netz fuer die verformte Kugel neu gebaut wird. Ohne
    Neuvernetzung ist die Antwort glatt. In diesem Sinn liegt die Anomalie an der Neuvernetzung.
  - Sie ist kein Paarungsartefakt [M, VORAB Abschnitt 2]. Der Erwartungswert von (a) ist exakt der Unterschied zweier
    frischer Ensembles, und die Umschaltspruenge der Paarung verschieben ihn nicht. Die Anomalie ist eine Eigenschaft
    der frisch gebauten 4D-Delaunay-Netze der verformten Kugel (Huelle in der konformen Karte, Regel QI) bei dieser
    Grobheit.
  - Der Erwartungswert von (a) ist nach VORAB Abschnitt 2 glatt in eps, mit verschwindender erster Ableitung. Die
    gemessenen Steigungen (1,3 gerade, etwa 1,7 ungerade) heissen dann: Der Bereich 0,025 bis 0,05 liegt ausserhalb der
    Kleinsignal-Entwicklung. Ein quadratischer Bereich, falls es ihn gibt, liegt unter 0,025 [ES]. Mit den
    Umschaltungen selbst hat das nichts zu tun.
  - Mitgenommene Verbindungen liefern keine saubere Einstein-Referenz. Das feste Netz ist im runden Mass isotrop, nicht
    im verformten. Die Scherung erzeugt einen extensiven, nicht kovarianten Term. Er ist etwa elfmal so gross wie das
    Einstein-Glied und hat das andere Vorzeichen. Das Einstein-Glied ist daneben nicht messbar: c ist nur geschaetzt,
    und die D-Kalibrierung traegt nicht (Abschnitt 3.4).
  - **Folge fuer die 4D-Kugel [ES]:** Keine der beiden Bauweisen misst auf diesem Netz Einsteins Glied.
    - Die Neuvernetzung ist als kovariante Vorschrift gebaut (Netz aus der konformen Struktur, Dichte 1 in g), aber im
      gemessenen Amplitudenbereich nicht quadratisch und etwa 28-mal zu gross.
    - Das mitgenommene Netz ist glatt, aber nicht kovariant.
    - Die Aussage von KOVARIANZ-KUGEL-1 ("auf diesem Netz nicht Einstein") bleibt stehen. Ihre Ursache ist jetzt enger
      eingegrenzt: Sie liegt in der neu gebauten Netzgeometrie, nicht im gemeinsamen Code (2D-Gegenprobe) und nicht in
      der Paarung.
- **Grenzen:** eine Schleife, freies masseloses Skalarfeld, euklidisch, N bis 4000, nur konforme l = 2-Verformungen um
  eine Achse, abs(eps) <= 0,05 symmetrisch (+0,1 nicht baubar), 40 Saaten. Die Scherprognose ist eine
  Ebene-Wellen-Schaetzung [H]; ihre Uebereinstimmung ist ein Befund, keine Herleitung fuer das Zufallsnetz.
- **Naechste Schritte [H]:**
  - (1) (a) bei kleineren Amplituden (0,0125, 0,00625) mit vielen Saaten: Wo beginnt der quadratische Bereich, und wie
    haengt er von N ab? Das Rauschen je Saat ist in (a) etwa 0,05 bis 0,09 (aus dem Neuvernetzen), in (b) nur etwa
    0,004; fuer (a) braucht es dort also viele Saaten.
  - (2) Ein festes Netz ohne Scherung: Punkte nicht verschieben, Laengen direkt aus g = e^(2 sigma) g0 (rein konform,
    also scherfrei). Dann gilt "Zahl = Volumen" nicht mehr; der Dichteterm muesste getrennt bestimmt werden. Ohne
    Scherterm koennte ein festes Netz zur Einstein-Referenz werden.
  - (3) Die Ursache in (a) direkt: Gamma frischer Netze auf der verformten Kugel gegen eine Kugel mit derselben
    Kruemmung, aber anderer Punktdichte-Verteilung in der konformen Karte. Das trennt "Delaunay bezueglich der konformen
    Karte" von "Kruemmung".

## 5. Kontrollen [E]

- **Kontrolllauf lauf-69/kontrolle.json** (eingefrorener Code, 15:38:27 bis 15:39:16 UTC, cpu, rc 0): alle Schwellen
  erfuellt, Zeilen C1 bis C7 zeichengleich mit dem Kontrolllauf vor dem Einfrieren:
  - C1 (sigma = 0): (a) und (b) gleich Gamma_Q(rund) auf 6,8e-13; 0 neue, 0 umgeklappte Simplizes.
  - C2 (Moebius): (a) netzgleich; (a) - (b) = -4,1e-12.
  - C3 (Codepfad, Saat 0, N = 1000): rund Q, (a) K-0,1 und (a) K+0,05 bitgleich mit kovarianz2d.py (live); rund Q und
    (a) K-0,1 bitgleich mit der Laufdatei von KOVARIANZ-KUGEL-1.
  - C4 (LU gegen dicht, (b), N = 400): <= 2,8e-13 fuer K-0,1 (1 umgeklappt), K+0,05 (0) und D0,5 (27).
  - C5 (Negativprobe Umklappen): 3 von 3 vertauschten Simplizes erkannt, V_g < 0 bei 3.
  - C6: eps = +0,1 nicht baubar (profil_min = -0,114).
  - C7 (Umklappen, Saat 991): K-0,1 je 1 (N = 1000, 2000), sonst 0; D0,25 8 und 9; D0,5 38 und 63.
- **KE0 Teil 1 im Lauf:** 120 von 120 (Saat, N) bitgleich mit KOVARIANZ-KUGEL-1, fuer Gamma_Q(rund) und fuer (a) bei
  eps = -0,1 (Abweichung 0,0).
- **Vorab-Proben (vorab.json):** Delta S/eps^2 bei eps = 0,001: 1082,35 gegen 1082,84; <tr H^2>/eps^2 = 32,86 gegen
  32,91 (erste Ordnung); Moebius <tr H^2> = 5e-13 (Isometrie).
- **In jedem Netz:** Transportrest <= 1e-10; (a) Huellenpruefungen; LU ok in allen 1800 verformten und 120 runden
  Netzen.

**Latten (v3):**
- **L1 (kann scheitern):** ja.
  - (a) haette bei +eps das Vorzeichen wechseln koennen, und sein gerader Anteil haette quadratisch sein koennen.
  - (b) haette durch Umklappen nicht glatt sein koennen, oder Einstein treffen koennen.
  - Die Scherprognose (c = 1/24 aus 0 bis 1/16) haette um ein Mehrfaches daneben liegen koennen.
  - Vorab entschieden war nur KE0 Teil 2 [K2]; Teil 1 ist eine Codepruefung.
- **L2 (Gegenprobe):** zwei Bauweisen auf denselben Punkten, sieben Amplituden mit beiden Vorzeichen, drei N, 40 Saaten,
  bitgleiche Reproduktion (120/120), zwei Scherkontrollen, Umklappzaehlung.
- **L3 (Numerik):** log det etwa 1e-13 absolut (C4); SE(G) 0,0006 bis 0,002 in (b), 0,009 bis 0,011 in (a).
- **L4 (schon bekannt):** Ein festes Gitter mit verzerrter Metrik hat einen nicht kovarianten Vakuumterm (anisotroper
  Schnitt) [L, allgemein bekannt aus der Gitterfeldtheorie]; Delaunay ist in 2D energieminimal (Rippa), in 4D nicht
  [L]. Eine Rechnung dieser Art auf S^4 kenne ich nicht; nicht gesucht [L?]. Die Scherschaetzung stand schon in
  KOVARIANZ-KUGEL-1 PLAN S4 ("etwa 1,4 N eps^2") [P].
- **L5 (Messbezug):** keiner (4D euklidisch, synthetisch).

## 6. Kartenpunkte (vor dem Rechnen offengelegt) und was daraus wurde

- **[K1] KE1 "gleiches Vorzeichen" zeigt allein keine Nicht-Glaette:** Der Plan hat die Steigung dazugenommen. Sie
  liegt bei 1,31 +- 0,06, also klar unter 1,7. Karte und Plan stimmen ueberein.
- **[K2] KE0 Teil 2 vorab bestimmt:** so eingetreten (-0,0019 +- 0,0003; vorab -0,0017, etwa -5 SE).
- **[K3] KE3 und KE4 bei e = 0,05 und in y:** Die Zusatzzeilen bei 0,0125 und 0,025 geben dasselbe Urteil. In
  Delta Gamma statt y waere das N-Wachstum noch groesser (Faktor 4,5 statt 2,3).
- **[K4] eps = +0,1 nicht baubar:** Die Karten-Steigung ist eine Zweipunktsteigung. Die Dreipunktsteigung von (b) mit
  0,0125 gibt 2,11 +- 0,04.
- **[K5] Zusaetze:** +-0,0125 bestaetigt die Glaette von (b). Die Scherkontrolle D kalibriert nicht (Abschnitt 3.4).
- **[K6] Umklappen in (b):** bei abs(eps) <= 0,05 hoechstens 1 Simplex in wenigen Netzen, bei -0,1 bis 8 von 118 000.
  Fuer KE2 ohne Gewicht.
- **[K7] Scherprognose:** bestaetigt; sie war eine Hypothese des Agenten, keine Kartenaussage.

## 7. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:**
   - Keine Mittel verformter Netze aus Rauchlaeufen (blind, per jq geprueft: kein Feld gamma oder gamma_M). Gesehen:
     Kontinuumsvorhersagen, Kontrollabweichungen, Umklappzahlen, blinde Streuungen (2 bis 3 Saaten), Zeiten, Gueltigkeit,
     von der Codeprobe nur die Struktur (jq keys, Torzaehlungen).
   - **Aber:** Kontrolle C3 druckt absolute Gamma-Werte fuer Saat 0, N = 1000: rund Q 1258,022, (a) K-0,1 1244,509 (aus
     KOVARIANZ-KUGEL-1 bekannt) und (a) K+0,05 1249,617. Daraus folgt fuer diese eine Saat Delta Gamma_a(+0,05) = -8,4
     (y = -0,27), also dasselbe Vorzeichen wie bei -eps.
   - Ich habe dieses Kontrollprotokoll vor dem Einfrieren gelesen; die Agenten-Vorhersagen A4 und A5 entstanden danach.
     Die Urteilsregeln standen schon vorher im Code (17:24 CEST).
2. **Codeaenderung nach Kontrolle und Rauchlauf, vor dem Einfrieren:**
   - Nur der Vergleichswert der Scherprobe (48 mal 96/140 statt 48/140). Grund: mein Rechenfehler beim S^4-Mittel von
     sin^4 (halbe sin^7-Integration); der Code hatte richtig gerechnet.
   - Vor dem Einfrieren ausserdem eine unsaubere Kruemmungsformel in VORAB.md berichtigt.
3. **Fremder Ordner:**
   - Ein Probe-Auswertungsaufruf mit vertauschten Argumenten hat um 15:35:09 UTC die Datei
     /home/fmh/fmhc-physics-remote/runde41-kovarianz-kugel/lauf.tmp angelegt (meine Probe-Ausgabe; Abbruch beim
     Umbenennen auf den Ordner lauf/, rc 1).
   - Ich habe sie um 15:35:30 UTC in meinen Ordner verschoben (rauch/probe/probe-aw-irrlauf-lauf.tmp, Inhalt ungelesen).
   - lauf/ von KOVARIANZ-KUGEL-1 ist unveraendert: 38 von 38 Pruefsummen gleich. Geaendert ist nur der Zeitstempel des
     Ordners runde41-kovarianz-kugel/.
4. **Weitere Fehlversuche:**
   - Der erste Start von rauch-a lief wegen eines cd-Fehlers im Befehl nicht an (keine Datei erzeugt, geprueft).
   - Die zweite Probe-Auswertung fand keine Dateien (Namensmuster); Kopien in rauch/probe2/.
5. **Nach der Auswertung, nicht im Plan [N]:**
   - Spalte gemessen/vorhergesagt und Vorhersagen je Zelle; effektives c je Zelle.
   - Bereinigung mit D0,5 als Zahl je N (aus auswertung.json); Bemerkung zum ungeraden Anteil von (b).
   - N^0,8 und Faktor 28 (von Hand).
   - Zeichenvergleich (jq) der (a)-Werte bei -0,05 und -0,025 mit dem Amplituden-Nachtrag von KOVARIANZ-KUGEL-1 (90 von
     90 gleich); die beiden Listen liegen als vergleich-amplituden-*.txt im Kartenordner (zuerst in lauf-69/ angelegt,
     dann verschoben; die Pruefsummen von lauf-69/ danach erneut 30 von 30).
6. **Nach dem Einfrieren:** Code unveraendert (Pruefsummen vor der Auswertung). Waehrend der Laeufe habe ich nur
   Start/Ende, Gueltigkeit, Umklappzahlen und Zeiten aus den Protokollen gelesen (die Protokolle enthalten keine
   Gamma-Werte). Messwerte habe ich erst in auswertung.json gesehen.
7. **ssh-Verbindungen:**
   - Meist zwei Spurketten und eine Abfrage; hoechstens vier zugleich (etwa 16:04 bis 16:20 UTC: zwei Ketten, zwei
     Warteschleifen), nicht darueber.
   - Zwei Startbefehle in der Rauchphase hielten ihre Verbindung bis zum Laufende offen (Hintergrundjob hinter "&&").
8. **Auf der .69 ausserhalb des Starters:**
   - mkdir, mv, cp, sha256sum, grep, tail, cat, cut, tr, ls, wc, sort, date, sleep (Warteschleifen), nohup (Start der
     Codeprobe), uptime, nproc, free.
   - systemctl --user list-units (nur lesen).
   - /usr/bin/jq (nur Struktur und Torzaehlungen der Probe).
   - Kein Python ausserhalb des Starters.
9. **Lokal:**
   - Kein python, awk oder perl.
   - Benutzt: jq (Lesen, Auszugsfilter auswertung-tabellen.jq, Zeichenvergleich), sha256sum, cmp, comm, sort, date, ssh,
     scp, cp, mv, mkdir, ls, cat, cut, head, tail, wc, grep, Warteschleife mit sleep.
   - Nichts geloescht.
10. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
    unter /tmp/claude-1000/.../tasks/ an (nur Endzeilen und Rueckgabecodes).
11. **Zeitbox:** Start 17:04:46 CEST, Text fertig 2026-10-04 18:38:04 CEST (date), also rund 103 min von 150.

## 8. Dateien

- KARTE.md (Leitung), VORAB.md, VORAB.md.eingefroren-20261004-173812, PLAN.md, PLAN.md.eingefroren-20261004-173812,
  EINGEFROREN-SHA256.txt, auswertung-tabellen.jq (Lesefilter fuer die Tabellen), vergleich-amplituden-hier.txt und
  vergleich-amplituden-nachtrag-kk1.txt (Zeichenvergleich, Abschnitt 3.1).
- code/:
  - kovarianz_eps.py (neu) mit Kopie *.eingefroren-20261004-173812.
  - Unveraendert kopiert, je mit eingefrorener Kopie: kovarianz2d.py, kugel.py, kugel2.py, kovarianz.py, dichte4d.py,
    induziert.py, zufall2d.py.
- rauch-69/:
  - vorab.json/.log, kontrolle.json/.log (vor dem Einfrieren), rauch-a.json/.log, rauch-b.json/.log (blind).
  - probe/ (Codeprobe: probe-1, probe-2, Irrlauf-Datei), probe2/ (Probe-Auswertung, nur Struktur gelesen),
    probe-aw-tor0.json/.log (Fehlversuch ohne Daten).
- lauf-69/:
  - kontrolle.json/.log; messung-N<N>-s<saat0>.json/.log (13 Laeufe); auswertung.json/.log (Tore, KE0-Reproduktion,
    Messgroessen, gerade/ungerade Anteile, Steigungen, Scherkontrolle, Urteile, Vorab).
  - PRUEFSUMMEN.txt (.69, 30 Dateien, lokal geprueft).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde42-kovarianz-eps/ (code/, rauch/, lauf/).

## 9. Einfach gesagt

- Auf der vierdimensionalen Punktkugel war die Reaktion auf eine Verbeulung viel zu gross, und sie wuchs nicht wie
  erwartet mit der Staerke der Beule.
- Wir haben dieselbe Beule auf zwei Arten gebaut: einmal das Netz zwischen den Punkten neu geknuepft, einmal das alte
  Netz behalten und nur die Punkte verschoben.
- Mit neu geknuepftem Netz bleibt die seltsame Reaktion: Beule nach innen und Beule nach aussen geben beide dasselbe
  Vorzeichen, und die Reaktion waechst kaum schneller als linear statt quadratisch.
- Mit dem alten Netz ist die Reaktion dagegen sauber quadratisch. Sie hat aber das falsche Vorzeichen und ist elfmal zu
  gross, weil ein festes Netz beim Verziehen geschert wird; genau das hatten wir vorher ausgerechnet.
- Die Ungereimtheit haengt also am Neuknuepfen des Netzes; eine saubere Einstein-Schwerkraft liefert auf diesem Netz
  aber keine der beiden Bauarten.
