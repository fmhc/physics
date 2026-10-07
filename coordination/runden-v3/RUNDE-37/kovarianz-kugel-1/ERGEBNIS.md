# KOVARIANZ-KUGEL-1: Ergebnis (Runde 41, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 14:19:28 CEST. Schreibtisch bis etwa 14:45, code/kovarianz.py bis 14:50:45 CEST, Vorab-Lauf
    12:50:33 UTC, Kontrolle und Rauchlaeufe 12:50:55 bis 12:52:19 UTC, Codeprobe 12:53 bis 12:56 UTC, letzte
    Codeaenderung 14:56 CEST (nur Auswertung), Plantext ab 14:54 CEST.
  - Eingefroren 14:57:13 CEST: PLAN.md.eingefroren-20261004-145713, VORAB.md.eingefroren-20261004-145713, Code-Kopien
    *.eingefroren-20261004-145713, Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe 12:57:23 bis 13:40:14 UTC (1 Kontrolle, 17 Messlaeufe, alle rc 0), Auswertung 13:40:25 bis 13:40:27 UTC
    (rc 0). Nachtraege (nicht im Plan) 13:46:42 bis 13:51:49 und 13:55:39 bis 14:02:51 UTC. Text ab 15:53 CEST.
- Code nach dem Einfrieren unveraendert: sha256 von kovarianz.py (bed2c12a...) und der fuenf kopierten Dateien auf der
  .69 vor der Auswertung gleich den eingefrorenen. lauf-69/PRUEFSUMMEN.txt (.69, 38 Dateien) lokal nachgeprueft: 38 von
  38 gleich. Nachtraege: neue Dateien code/nachtrag_drehung.py (6e627eb0...) und code/nachtrag_amplitude.py
  (5bb7b693...), beide importieren kovarianz.py unveraendert; nachtrag-69/PRUEFSUMMEN.txt 12 von 12 gleich.
- Alle Zahlen sind Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, float64, Spuren cpu3, cpu4, cpu5).
  Euklidisch, eine Schleife, freies masseloses Skalarfeld (P1), synthetisch, keine Messdaten.
- **Kennzeichen:** [M] eigene Mathematik, [E] hier gerechnet, [ES] eigener Schluss, [F] Festlegung im Plan,
  [K] Kartenpunkt, [H] Hypothese, [L] Literatur aus dem Gedaechtnis, [N] Nachtrag nach der Auswertung (nicht im Plan).
- **Konvention:** y = (Gamma_X - Gamma_rund)/sqrt(N), gepaart je Saat und N; X = M (Moebius-Nullprobe), K (konform
  l = 2), E (gestauchte Kugel). Hauptregel QI (Sehnen der isometrischen Einbettung, je Simplex auf das g-Volumen
  skaliert; fuer die runde Kugel = Regel Q), Fassung roh, gegen Gamma_Q(rund). Nebenlesart CI (Sehnen, korr) gegen
  Gamma_C(rund, korr). b = Saatmittel des Mittels ueber N = 1000, 2000, 4000; SE aus 120 Saaten.
  Einstein-Vorhersage (VORAB.md): y = beta_Q Delta S_1/(32 pi^2), N-unabhaengig.

## 1. Ergebnis zuerst

1. **Das Vorzeichen ist Einsteins, der Betrag nicht [E].** Konform l = 2 (K): b = **-0,625 +- 0,008** (-82 SE, alle 120
   Saaten negativ), vorhergesagt -0,0554 +- 0,0018, also das **11,3-Fache**. Gestauchte Kugel (E): b = **-0,951 +-
   0,008** (-127 SE), vorhergesagt -0,0458 +- 0,0015, das **20,8-Fache**. Das Verhaeltnis E/K ist 1,52 statt 0,825.
2. **Die Antwort ist keine saubere zweite Ordnung [E].** Sie waechst mit N: y_K = -0,505 / -0,611 / -0,758 und
   y_E = -0,756 / -0,928 / -1,169 bei N = 1000 / 2000 / 4000 (SE je 0,013); die Werte liegen genau auf
   y = beta' + alpha sqrt(N) (von Hand: K alpha = -0,0080, beta' = -0,25; E -0,0131 und -0,34), Delta Gamma hat also in
   diesem Bereich einen mit N wachsenden Anteil. Und sie faellt mit der Amplitude etwa linear statt quadratisch
   (Nachtrag 2 [N]: halbe Amplitude etwa die Haelfte, Viertel etwa ein Fuenftel; Einstein verlangt ein Viertel bzw.
   ein Sechzehntel). Beides kann eine glatte lokale kovariante Wirkung Lambda V + B Int R + O(1) nicht.
3. **Die Umbenennung gibt fast null [E].** Moebius-Nullprobe (M): b = -0,0017 +- 0,0002, das sind 3 % der
   K-Vorhersage und 0,3 % der gemessenen K-Antwort, aber 8,9 SE von null; Ursache ist die Volumenzuordnung je Simplex
   (CI, ohne diese Zuordnung, ist exakt null: 1e-12). Nachtrag [N]: Auch mit Neuvernetzung (Punkte vorher massstreu
   verdreht, 53 bis 55 % neue Simplizes) bleiben Umbenennung und rundes Netz bei +0,03 +- 0,02. Die grosse K/E-Antwort
   kommt also nicht vom Neuvernetzen oder der Paarung, sondern von der echten Formaenderung.
4. **Urteile (Plan = Kartenwortlaut):** KV0 nicht eingetroffen (8,9 SE, Groesse 3 % des Signals); **KV1 eingetroffen**
   (-82 SE); KV2 nicht eingetroffen (E sinkt, -127 SE; das hatte die Vorab-Datei als Einstein-Erwartung festgehalten);
   KV3 nicht eingetroffen (Faktor 11 und 21).
5. **Bedeutung (Kartensatz, ausgeloest):** "Verfehlt sie (Nullkontrolle, Vorzeichen, Verhaeltnis), ist Schwerkraft aus
   Materie in 4D auf diesem Netz nicht Einstein." Verfehlt sind Nullkontrolle (knapp, im Wortlaut) und Verhaeltnis
   (deutlich); das Vorzeichen stimmt fuer beide Verformungen. **Einschraenkung meiner Lesart [ES]:** Wegen Punkt 2 misst
   die Groesse das Einstein-Glied nicht sauber; sie wird von einem nicht-quadratischen Effekt der Formaenderung
   beherrscht, dessen Ursache (Gitter, Konstruktion oder Codefehler im nicht-Moebius-Zweig) offen ist. Ein B fuer
   Formaenderungen ist daraus nicht ablesbar. Vorab-Einschraenkung: nur konform flache Verformungen; die Spin-2-Struktur
   (TT) ist mit dieser Vorschrift nicht baubar und ungemessen.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 6 durch kovarianz.py auswertung; Werte in lauf-69/auswertung.json.
**Tor bestanden:** 120 von 120 Saaten bei allen drei N gueltig (360 runde und 1080 verformte Netze, je zwei LU ok,
Transportrest <= 1,1e-16); 0 ausgeschlossen, 0 unvollstaendig. **K0:** Gamma_Q und Gamma_C rund in 240 von 240
Vergleichen bitgleich mit KUGEL-2 (Saaten 0 bis 39, groesste Abweichung 0,0).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Plan) | Kartenwortlaut | Kennzahlen (QI) |
|---|---|---|---|---|---|
| KV0 | Nullprobe: l = 1-Umbenennung innerhalb 2 SE um null | 60 % | **nicht eingetroffen** | **nicht eingetroffen** | b_M = -0,00166 +- 0,00019 (-8,9 SE); b_M/y_pred,K = 0,030; CI exakt null (1,3e-12 +- 1,3e-12) |
| KV1 | [H] konform l = 2: Gamma sinkt, >= 3 SE | 55 % | **eingetroffen** | **eingetroffen** | b_K = -0,6247 +- 0,0076 (-81,9 SE), 120/120 Saaten negativ; Vorhersage -0,0554 |
| KV2 | [H] spurfrei volumentreu (gestauchte Kugel): Gamma steigt, >= 3 SE | 45 % | **nicht eingetroffen** | **nicht eingetroffen** | b_E = -0,9508 +- 0,0075 (-126,6 SE), 120/120 negativ. Einstein-Lesart (Zusatzzeile, vorab): b_E <= -3 SE: **erfuellt** |
| KV3 | [H] beide innerhalb 30 % der Kontinuumsvorhersage | 25 % | **nicht eingetroffen** | **nicht eingetroffen** | b_K/y_pred = 11,27; b_E/y_pred = 20,78; beide weit ausserhalb 2 kombinierter SE (73 bzw. 118) |

- **Bedeutung, wie vorab auf der Karte festgelegt:** "Verfehlt sie (Nullkontrolle, Vorzeichen, Verhaeltnis), ist
  Schwerkraft aus Materie in 4D auf diesem Netz nicht Einstein": **ausgeloest** ueber Verhaeltnis (KV3) und, im
  Wortlaut, Nullkontrolle (KV0). "Trifft die Vorhersage, ... Torus-Frage erledigt": nicht ausgeloest.
- **Zu KV2 [K1, vorab]:** Die gestauchte Kugel ist keine spurfreie Verformung, sondern konform (VORAB.md Abschnitt 1);
  Einstein sagt "sinkt". Der Kartenwortlaut ist verfehlt, wie es bei Einstein sein muss; der Betrag (Faktor 21) passt
  dagegen nicht zu Einstein.
- **Zu KV0:** Kein Wesentlichkeitsrabatt (Plan). Der Rest ist klein gegen alles andere hier: 3 % der Vorhersage fuer K.

**Agenten-Vorhersagen** (PLAN Abschnitt 10, vor den Hauptlaeufen)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (90 %) | Tor ohne Ausschluss | **eingetroffen** |
| A2 (90 %) | K0 bitgleich | **eingetroffen** (240/240) |
| A3 (45 %) | KV0 eingetroffen | nicht eingetroffen |
| A4 (70 %) | b_K < 0 | **eingetroffen** |
| A5 (45 %) | KV1 eingetroffen | **eingetroffen** |
| A6 (10 %) | KV2 (Karte) eingetroffen | nicht eingetroffen |
| A7 (70 %) | b_E < 0 | **eingetroffen** |
| A8 (15 %) | KV3 eingetroffen | nicht eingetroffen |

## 3. Tabellen

### 3.1 b je Verformung und Regel [E]

(Mittel ueber 120 Saaten des Mittels ueber N; Std je Saat; "neg" = Saaten mit negativem Mittel; Zweiparameterfit
y = b + d/sqrt(N) je Saat, beschreibend)

| X / Regel | b +- SE | Std je Saat | neg | y_pred (beta) | b/y_pred | Zweiparameter b; d |
|---|---|---|---|---|---|---|
| **M / QI** | **-0,00166 +- 0,00019** | 0,0020 | 87 | 0 | - | -0,0008 +- 0,0007; -0,036 +- 0,032 |
| M / CI | +1,3e-12 +- 1,3e-12 | 1,4e-11 | 65 | 0 | - | (exakt null, vorab ableitbar) |
| **K / QI** | **-0,6247 +- 0,0076** | 0,084 | 120 | -0,0554 +- 0,0018 | **11,27** | -0,990 +- 0,028; +15,7 +- 1,2 |
| K / CI | -0,4891 +- 0,0077 | 0,085 | 120 | -0,0500 +- 0,0018 | 9,78 | -0,778 +- 0,028; +12,4 +- 1,2 |
| **E / QI** | **-0,9508 +- 0,0075** | 0,082 | 120 | -0,0458 +- 0,0015 | **20,78** | -1,547 +- 0,028; +25,6 +- 1,2 |
| E / CI | -0,7470 +- 0,0076 | 0,083 | 120 | -0,0413 +- 0,0015 | 18,10 | -1,201 +- 0,028; +19,5 +- 1,2 |

- Verhaeltnis E/K (von Hand): QI 1,522, CI 1,527; Einstein 0,825.
- Der Zweiparameterfit (Modell der Vorgaengerkarten) passt nicht: d ist 11 bis 22 SE von null, und die Reste je N
  liegen bei 2 SE. Das Modell y = beta' + alpha sqrt(N) trifft alle drei N auf 0,001 (von Hand, Abschnitt 1).

### 3.2 y je N [E]

(Mittel +- SE ueber 120 Saaten; in Klammern Std je Saat)

| X / Regel | N = 1000 | 2000 | 4000 |
|---|---|---|---|
| M / QI | -0,00186 +- 0,00044 (0,0049) | -0,00186 +- 0,00028 (0,0031) | -0,00125 +- 0,00022 (0,0024) |
| K / QI | -0,505 +- 0,013 (0,145) | -0,611 +- 0,013 (0,143) | -0,758 +- 0,013 (0,145) |
| K / CI | -0,395 +- 0,013 | -0,477 +- 0,013 | -0,596 +- 0,013 |
| E / QI | -0,756 +- 0,013 (0,145) | -0,928 +- 0,014 (0,153) | -1,169 +- 0,013 (0,144) |
| E / CI | -0,600 +- 0,013 | -0,727 +- 0,014 | -0,915 +- 0,013 |

- In absoluten Zahlen (beschreibend): Delta Gamma_K = -16, -27, -48 gegen vorhergesagt -1,75, -2,48, -3,51; je Punkt
  Delta Gamma/N = -0,0160, -0,0137, -0,0120 (K) und -0,0239, -0,0207, -0,0185 (E).
- Die Streuung je (Saat, N) ist in y-Einheiten konstant (0,14 bis 0,15), also waechst das Paarungsrauschen wie sqrt(N);
  die Paarung traegt trotz 60 % neuer Simplizes (volle Entkopplung gaebe etwa 0,24).

### 3.3 Netze [E]

| | N = 1000 | 2000 | 4000 |
|---|---|---|---|
| neue Simplizes K / E / M | 0,603 / 0,535 / 0 | 0,610 / 0,553 / 0 | 0,616 / 0,565 / 0 |
| M: Netz gleich dem runden (Netze) | 120 von 120 | 120 von 120 | 120 von 120 |
| M: Punkte gegen rund, max (relativ zu a) | 2,1e-13 | 1,1e-12 | 1,7e-11 |
| max abs(Summe V_g/N - 1) | 2,1e-4 | 6,3e-5 | 2,0e-5 |
| V_Sehnen/N (M = rund, K, E) | 0,8029 / 0,7995 / 0,8007 | 0,8576 / 0,8550 / 0,8562 | 0,8977 / 0,8957 / 0,8969 |
| Delta F = F_X - F_rund, Mittel (K / E) [jq, beschreibend] | -89,6 / -84,7 | -169,9 / -111,6 | -318,5 / -216,9 |
| F_rund, Mittel | 27 444 | 57 351 | 118 300 |
| Laufzeit je Saat (rund + drei Verformungen) | 5,5 s | 14,0 s | 40,9 s |

- Kleinster Gram-Eigenwert der Sehnen-Simplizes in allen 1080 verformten Netzen > 0 (min 2,8e-9 bei M, N = 1000):
  QI und CI sind ueberall einbettbar.

### 3.4 Nachtrag [N]: Nullproben mit Neuvernetzung (nicht im Plan, nach der Auswertung)

Grund: Die Kontrollen des Plans haben keinen Fall mit Neuvernetzung und bekannter Antwort. code/nachtrag_drehung.py
dreht vor dem Bau jede S^3-Faser um kappa theta (kappa = 0,5): massstreu, nicht isometrisch, also gleichverteilte
Punkte mit 53 bis 55 % neuen Simplizes. D-B: sigma = 0 (Erwartung exakt 0). D-A: dazu der Moebius-Transport wie M
(Erwartung wie M, etwa 0). Saaten 0 bis 39 (N = 1000, 2000) und 0 bis 9 (N = 4000); alle Netze gueltig.

| Probe | N = 1000 | 2000 | 4000 | gewichtet (von Hand) |
|---|---|---|---|---|
| D-B (sigma = 0), QI | +0,008 +- 0,028 | +0,047 +- 0,029 | +0,044 +- 0,046 | +0,029 +- 0,018 |
| D-A (Moebius), QI | +0,005 +- 0,028 | +0,045 +- 0,029 | +0,043 +- 0,046 | +0,028 +- 0,018 |
| D-B, CI korr | +0,007 +- 0,028 | +0,046 +- 0,029 | +0,044 +- 0,046 | |
| Delta F (D-B) | +1,9 | +57,1 | +56,6 | |

- Beide sind mit null vertraeglich (1,6 SE) und hoechstens etwa 0,065 (2 SE), also unter 11 % der K-Antwort. Die
  grosse Antwort von K und E entsteht nicht durch Neuvernetzen oder Paaren, sondern durch die nicht-Moebius-Form.
- Einschraenkung: Seeds und kappa nach der Auswertung gewaehlt; nur beschreibend.

### 3.5 Nachtrag 2 [N]: Amplitudenreihe (nicht im Plan, nach der Auswertung)

Grund: Eine glatte, unter SO(5) symmetrische Erwartung E[Gamma](eps) hat bei eps = 0 keine erste Ableitung; jede echte
Formantwort muss fuer kleine Amplituden quadratisch fallen. code/nachtrag_amplitude.py (gleiche Vorschrift, kovarianz.py
unveraendert importiert): K mit eps = -0,05 und -0,025, E mit lam = e^(-0,25); Saaten 0 bis 39 (N = 1000, 2000) und 0 bis 9
(N = 4000); alle Netze gueltig. Vergleich mit den Hauptlaeufen auf denselben Saaten.

| Verformung | Vorhersage y (Einstein) | N = 1000 | 2000 | 4000 | Verhaeltnis zur vollen Amplitude (gemessen; Einstein) |
|---|---|---|---|---|---|
| K, eps = -0,1 (Hauptlauf, dieselben Saaten) | -0,0554 | -0,538 | -0,601 | -0,737 | 1 |
| K, eps = -0,05 | -0,0140 | -0,259 +- 0,022 | -0,300 +- 0,022 | -0,410 +- 0,041 | 0,48 / 0,50 / 0,56; Einstein 0,252 |
| K, eps = -0,025 | -0,0035 | -0,107 +- 0,020 | -0,127 +- 0,015 | -0,197 +- 0,038 | 0,20 / 0,21 / 0,27; Einstein 0,063 |
| E, lam = e^(-0,5) (Hauptlauf) | -0,0458 | -0,754 | -0,923 | -1,167 | 1 |
| E, lam = e^(-0,25) | -0,0127 | -0,331 +- 0,018 | -0,384 +- 0,022 | -0,488 +- 0,027 | 0,44 / 0,42 / 0,42; Einstein 0,277 |

- Neue Simplizes: K 0,40 bis 0,42 (eps = -0,05), 0,23 bis 0,25 (-0,025); E 0,36 bis 0,39.
- **Die Antwort faellt etwa linear mit der Amplitude, nicht quadratisch** (bei halber Amplitude etwa die Haelfte, bei
  einem Viertel etwa ein Fuenftel). Bei eps = -0,025 ist sie 31-mal so gross wie Einsteins Vorhersage. Eine glatte
  symmetrische Erwartung kann das bei kleinen Amplituden nicht; der Effekt ist also entweder nicht analytisch in der
  Verformung (Gittereffekt) oder ein Fehler der Konstruktion bzw. des Codes im nicht-Moebius-Zweig [ES, H].
- Einschraenkung: nach der Auswertung entworfen, nur beschreibend; Amplituden und Saaten von mir gewaehlt.

## 4. Kontrollen

- **Tor und K0:** Abschnitt 2.
- **Kontrolllauf lauf-69/kontrolle.json (12:57:23 bis 12:57:38 UTC, cpu3, rc 0), alle Schwellen erfuellt, Werte gleich dem
  Kontrolllauf vor dem Einfrieren:**
  - C1 (sigma = 0): 0 neue Simplizes; Gamma_QI - Gamma_Q = -6,8e-13; CI korr - C korr = -1,6e-12 (Schwelle 1e-8).
  - C2 (Moebius): Transport gegen die exakte Moebius-Abbildung 4,3e-14; Netz gleich; Punkte gleich 4,0e-14;
    CI korr - C korr 2,3e-12.
  - C3 (N = 400, Saat 990): duenne LU gegen dichte Eigenwerte und slogdet <= 6,3e-13, Gamma_M gegen verallgemeinerte
    Eigenwerte <= 1,1e-13, fuer M, K, E.
  - C4 (Negativprobe, N = 1000): konforme Sehnen ohne Einbettung sind fuer K (27) und E (26) nicht einbettbar, fuer M
    (0) schon; Grund fuer die Regel QI.
- **Vorab-Proben (vorab.json):** Delta S_M = -5,7e-14; Ellipsoid aus der konformen Karte gegen Gauss-Gleichung 2,3e-13;
  eingebettetes Profil gegen Ellipse 1,3e-14; Volumennormierung 1 +- 2,4e-15; l = 2-Koeffizient 1082,35 gegen 1082,84
  (dritte Ordnung); l = 1-Koeffizient 0,001 (gegen 0).
- **In jedem Netz:** Transportrest <= 1,1e-16; Huellenpruefungen (Euler 2, Facetten gepaart, leere Kappen, Normalen);
  LU ok fuer QI und CI.

**Latten (v3):**
- **L1 (kann scheitern):** ja. Das Vorzeichen haette positiv sein koennen (KV1), die Nullprobe haette gross sein koennen,
  der Betrag haette die Vorhersage treffen koennen (KV3); nichts davon stand vorab fest. Nur die CI-Nullprobe war vorab
  ableitbar (exakt null) und ist als Kontrolle gefuehrt.
- **L2 (Gegenprobe):** zwei Laengenregeln (QI, CI), drei Verformungen, drei N, 120 Saaten, bitgleiche Reproduktion des
  runden Netzes (K0), Ellipsoid-Vorhersage auf zwei unabhaengigen Wegen, Nachtrag mit Neuvernetzung.
- **L3 (Numerik):** log det etwa 1e-12 absolut (C1 bis C3); SE(b) 0,0075 (K, E) und 0,0002 (M).
- **L4 (schon bekannt):** zweite Variation von Int R auf Einstein-Raeumen und TT-Spektrum auf S^4 (Besse 4.55/4.60,
  Christensen-Duff) [L]; konforme Flachheit O(4)-symmetrischer Metriken [M]; Poisson-Delaunay auf der Kugel als Huelle
  [L]. Eine Gitterrechnung dieser Art kenne ich nicht; nicht gesucht [L?].
- **L5 (Messbezug):** keiner (4D euklidisch, synthetisch).

## 5. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **[K1] KV2 misst keine spurfreie Verformung:** bestaetigt; E verhaelt sich wie K (beide sinken), wie vorab fuer
  Einstein berechnet, aber 21-mal staerker.
- **[K2] KV3 mit den Einstein-Vorhersagen beider Verformungen:** so geurteilt; auch mit jeder anderen Vorzeichenwahl
  waere der Betrag (Faktor 11 bzw. 21) ausserhalb von 30 %.
- **[K3] Nullprobe teilweise vorab entschieden:** Netz und Sehnen waren fuer M exakt Moebius-Bilder (120 von 120 Netzen
  gleich); gemessen wurde nur die Volumenzuordnung je Simplex: -0,0017. Der Nachtrag ergaenzt den Fall mit Neuvernetzung.
- **[K4] Neu bauen:** Rauschpreis kleiner als befuerchtet (Std je Saat 0,083 statt geschaetzt 0,14).
- **[K5] Regel QI:** ueberall einbettbar; die Nebenlesart CI gibt dieselben Aussagen (Faktor 9,8 und 18,1).
- **[K6] einseitig, eps = -0,1:** Ein Vorzeichen; dritte Ordnung in der Vorhersage enthalten (exakte Quadratur).
- **[K7] Konstantenfit:** Modellannahme verworfen (Abschnitt 3.1); das Urteil haengt daran nicht, weil jedes N einzeln
  dasselbe zeigt (y_K zwischen -0,51 und -0,76, also 9- bis 14-mal die Vorhersage).

## 6. Selbstanzeigen

1. **Vor dem Einfrieren gesehen:** keine Gamma-Werte oder Mittel der verformten Netze. Gesehen habe ich: die
   Vorab-Vorhersagen (Kontinuum), Kontrollabweichungen (C1 bis C4, Groessenordnung 1e-12), blinde Streuungen aus 2 bis 3
   Rauchsaaten, Kippanteile, Volumen, Zeiten, Gueltigkeit und von der Codeprobe nur die Struktur (jq keys).
   probe-aw.log und probe-aw2.log enthalten die Probe-Urteile; ich habe sie nicht gelesen.
2. **Codeaenderungen vor dem Einfrieren:** Rundungsschranke der Profilpruefung (nach dem Vorab-Lauf, der -2e-16 an den
   Polen zeigte) und die Unterscheidung "unvollstaendig" im Tor (nach der Codeprobe). Beide ohne Kenntnis von Messwerten.
3. **Nach dem Einfrieren:** kovarianz.py unveraendert (Pruefsumme vor der Auswertung). Beide Nachtraege
   (nachtrag_drehung.py mit kappa, Saaten, N; nachtrag_amplitude.py mit den Amplituden) sind **nach** dem Lesen der
   Ergebnisse entworfen, nicht eingefroren und nur beschreibend.
4. **Beschreibend nach der Auswertung, nicht im Plan:** Delta F (jq), das Modell beta' + alpha sqrt(N) und die
   gewichteten Mittel des Nachtrags (von Hand), Verhaeltnis E/K.
5. **Schreibtischfehler:** In VORAB.md standen die Kruemmungen fuer K zuerst fuer eps = -0,08; vor dem Einfrieren auf
   eps = -0,1 berichtigt (1,42 / 0,64 R0). Meine Rauschschaetzung (S8) war zu pessimistisch.
6. **ssh-Verbindungen:** hoechstens drei Spurketten und eine kurze Abfrage zugleich.
7. **Auf der .69 ausserhalb des Starters:** mkdir, mv, sha256sum, grep, cat, tail, wc, date, uptime, /usr/bin/jq (Struktur,
   blinde Streuung, Netzdaten ohne Gamma vor der Auswertung). Kein Python ausserhalb des Starters.
8. **Lokal:** kein python, awk oder perl. Benutzt: jq (Lesen; Mittel, Std und Delta F fuer den Nachtrag und die
   Netztabelle), sed (ein Ersatz im Code vor dem Einfrieren), grep, sha256sum, date, ssh, scp, cp, mv, mkdir, ls, cat,
   cut, head, tail, wc und sleep in Warteschleifen. Nichts geloescht.
9. **Scratchpad:** nichts hineingeschrieben. Die Werkzeugumgebung legt fuer Hintergrundbefehle eigene Ausgabedateien
   unter /tmp/claude-1000/.../tasks/ an (nur Rueckgabecodes und Laufmeldungen).
10. **Zeitbox:** Start 14:19:28 CEST, Text fertig 16:05:32 CEST (date), also rund 112 min von 150.

## 7. Bedeutung

- **Was gezeigt ist [E]:**
  - Auf Poisson-Delaunay-Netzen der S^4 (N = 1000 bis 4000, 120 Saaten) sinkt Gamma bei einer echten Formaenderung
    der Kugel (konform l = 2 und gestaucht), in jeder Saat, mit Einsteins Vorzeichen.
  - Der Betrag ist 11- bzw. 21-mal groesser, als das am runden Netz gemessene B sagt, das Verhaeltnis der beiden
    Verformungen ist 1,52 statt 0,825, die Antwort waechst mit N schneller als sqrt(N) und faellt mit der Amplitude
    etwa linear statt quadratisch (Nachtrag 2).
  - Eine reine Umbenennung (Moebius) gibt fast null (3 % des erwarteten Signals), auch mit Neuvernetzung (Nachtrag).
- **Was ich daraus schliesse [ES]:**
  - Das runde B beschreibt die Antwort dieses Netzes auf Formaenderungen nicht. Die induzierte Wirkung ist auf diesem
    Netz kein "Lambda V + B Int R + O(1)": Es gibt einen viel groesseren, formabhaengigen Anteil, der in N = 1000 bis 4000
    wie N waechst. Damit ist "Schwerkraft aus Materie in 4D auf diesem Netz" im Sinn der Karte nicht Einstein.
  - Die Nullproben sprechen gegen einen Fehler im Transport, in der Paarung oder in der Huelle (sie haetten bei
    Neuvernetzung angeschlagen). Ein Fehler, der nur bei nicht-Moebius-sigma wirkt, ist nicht ausgeschlossen: Keine
    Kontrolle hat einen nicht-Moebius-Fall mit bekannter Gitterantwort [H].
  - Nach meiner Schreibtischrechnung (lokal, erste Ordnung) sollte eine kovariante Konstruktion keinen mit N wachsenden
    Anteil haben, und nach Symmetrie und Glattheit muss die Erwartung fuer kleine Amplituden quadratisch fallen; die
    Daten widersprechen beidem (Abschnitte 3.2 und 3.5). Moegliche Quellen [H]: (a) Die Gitterwirkung haengt bei
    h^2 R ~ 1 bis 2 stark nichtlinear von der Form ab, so dass schon eps = 0,025 jenseits der zweiten Ordnung liegt;
    (b) die Konstruktion ist fuer nicht-Moebius-sigma nicht kovariant in einer Weise, die ich nicht sehe (Huelle in der
    konformen Karte, Aussensehnen der Einbettung, Volumenzuordnung); (c) ein Codefehler im nicht-Moebius-Zweig.
  - Folge fuer die Karte: Das Kartenurteil "nicht Einstein" ist mechanisch ausgeloest; inhaltlich ist der Test in dieser
    Form noch keine Messung der Tensorstruktur, sondern zeigt, dass die Messgroesse von einem unverstandenen, nicht
    quadratischen Effekt beherrscht wird. Vor einer Meldung an Finn sollte (c) ausgeschlossen werden.
  - Fuer den Torus-Widerspruch: Dort war die Antwort positiv und klein, hier negativ und gross. Beide sind keine
    Einstein-Antwort mit dem runden B; die Torus-Frage ist damit nicht erledigt, sondern verschaerft.
- **Grenzen:** eine Schleife, freies masseloses Skalarfeld, euklidisch, feste Punktzahl; nur konform flache
  (rotationssymmetrische) Verformungen, je ein Vorzeichen; im Plan je eine Amplitude (Nachtrag: drei fuer K, zwei fuer
  E); N bis 4000; TT-Sektor ungemessen.
- **Naechste Schritte [H]:**
  - (a) 2D-Gegenstueck mit derselben Vorschrift (S^2 gegen verformte S^2, gleiche Transport-, Huellen- und
    Laengenfunktionen): Dort ist Int R topologisch und K skaleninvariant; jede Antwort, die mit N waechst oder linear in
    der Amplitude ist, waere ein Konstruktions- oder Codefehler. Das ist die billigste Fehlerprobe fuer (c).
  - (b) Ein nicht-Moebius-Fall mit unabhaengig gebautem Netz: Punkte per Verwerfungsstichprobe statt Transport, Laengen
    auf einem zweiten Weg; gleiche Erwartung, anderer Code.
  - (c) Kleinere Amplituden (eps = -0,01, -0,005) mit vielen Saaten: Wo beginnt der quadratische Bereich, falls es ihn
    gibt?
  - (d) N = 8000 fuer wenige Saaten, um den wachsenden Anteil zu bestaetigen oder als Uebergang zu erkennen.

## 8. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-145713, VORAB.md, VORAB.md.eingefroren-20261004-145713,
  EINGEFROREN-SHA256.txt.
- code/: kovarianz.py (Verformungen, Transport, Huelle, Regeln QI/CI, Kontrollen, Messung, Auswertung); unveraendert
  kopiert kugel.py, kugel2.py, dichte4d.py, induziert.py, zufall2d.py; je mit Kopie *.eingefroren-20261004-145713;
  nachtrag_drehung.py und nachtrag_amplitude.py (Nachtraege, nicht eingefroren).
- rauch-69/: vorab.json/.log, kontrolle.json/.log, rauch-a/-b (blind) .json/.log, probe/ und probe-*.log (Codeprobe;
  Werte ungelesen).
- lauf-69/: kontrolle.json/.log; messung-N<N>-s<saat0>.json/.log (17 Laeufe); auswertung.json (Tor, K0, Messgroessen,
  Netze, Urteile, Vorab), auswertung.log; PRUEFSUMMEN.txt (.69, 38 Dateien, lokal geprueft).
- nachtrag-69/: drehung-*.json/.log und amplitude-*.json/.log (je 3 Laeufe), PRUEFSUMMEN.txt (12 Dateien, lokal
  geprueft).
- Auf der .69: /home/fmh/fmhc-physics-remote/runde41-kovarianz-kugel/ (code/, rauch/, lauf/, nachtrag/).

## 9. Einfach gesagt

Auf einer vierdimensionalen Kugel aus Zufallspunkten hatte das Zittern eines Materiefelds die Kugel so versteift, wie
es Einsteins Schwerkraft verlangt. Jetzt haben wir die Kugel verbeult und gestaucht und gemessen, ob die Versteifung
sich genau so aendert, wie Einsteins Formel mit der gemessenen Staerke es vorhersagt. Die Richtung stimmt, aber die
Aenderung ist 11- bis 21-mal zu gross, und sie waechst mit der Zahl der Punkte schneller, als Einstein erlaubt. Ein
blosses Umbenennen der Punkte aendert dagegen fast nichts, die Messung reagiert also wirklich auf die Form. Merkwuerdig
ist, dass eine halb so starke Beule etwa die halbe statt ein Viertel der Wirkung hat; so verhaelt sich keine glatte
Schwerkraft. Formal ist damit die Schwerkraft aus Materie auf diesem Netz nicht Einsteins Schwerkraft; ob das am Netz
selbst oder an einer noch unentdeckten Schwaeche unserer Konstruktion liegt, muss zuerst eine billige
zweidimensionale Gegenprobe klaeren.
