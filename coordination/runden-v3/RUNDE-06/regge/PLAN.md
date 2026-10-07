# RG-1 Regge-Turm drehender Q-Baelle (2D): Laufplan

Bearbeiter: Anthropic-Agent RG-1 (Opus 5.5), Auftrag der Leitung zur Karte RUNDE-06/KARTE-RG1-REGGE.md. Beginn
2026-09-30 03:03:13 CEST (gemessen), Plan begonnen 03:32:04 CEST (gemessen), Ende in der letzten Zeile.
Status: Code fertig, lokaler Rauchtest gelaufen (Abschnitt 7). **Die Hauptlaeufe fehlen noch.** Explorativ (v3), keine
formale Bestaetigung. Die Zahlen des Rauchtests sind eine Vorschau; gerechnet wurde er auf dem Laptop.

## Kurzfassung

- **Code:** regge2d.py, numpy float64, CPU, ein Kern. Unterbefehle `tabelle`, `bahn` und `rauch`; Ausgaben bericht.txt
  und ergebnis.json nach --out. Das Schiessen fuer m != 0 ist die berichtigte Coleman-Regel aus r5_2d_a.py mit
  Einschachtelung in ln p.
- **Tabelle:** m = 0 bis 8, 25 Werte omega^2 von 0,52 bis 0,99, dazu die NLS-Grenze omega -> 1 je m. Zusammen 234 Zeilen.
- **Kernvorhersage (Schreibtisch):** Q(omega) faellt fuer jedes m monoton zu omega -> 1. Q_min liegt also am oberen Rand
  des Gitters. In 2D ist dort die kubische NLS kritisch: Q -> 2 N_T(m), E/Q -> 1.
  - Grosse m sind duenne Ringe mit Radius sqrt(2) m/sqrt(1 - omega^2) und festem Querschnitt. Daraus folgt
    Q_min ~ 43,5 m, also beta -> 1 und alpha -> 2.
  - Erwartet fuer m = 3 bis 8: beta = 0,99 und alpha = 2,01.
- **Einschraenkung zu L1:** alpha -> 2 laesst sich im Duennring-Grenzfall vorab ableiten. Scheitern kann der Test nur an
  drei Stellen: wenn Q_min nicht am Rand liegt, wenn die Ringe bei m = 3 bis 8 noch nicht duenn sind, oder an der
  Numerik. Das ist eine schwache L1 (Memory "vorab ableitbare Kennzahl").
- **Rauchtest:** m = 0, 1, 3, 8 bei drei omega^2-Werten, lokal in 28 s. Alle 16 Zeilen gueltig, R3-Anschluss und J = m Q
  bestanden.
  - Vorschau: beta = 0,988 und alpha = 2,012 (nur zwei Punkte, m = 3 und 8).
  - Q_lim(0) = 11,7009 ist die Townes-Norm.
- **Hauptlaeufe:** zwei Tabellen (h0 = 0,01 und 0,005) und eine Auswertung. Geschaetzt je 1 bis 3 min, sicher unter
  10 min. Aufrufe in Abschnitt 8.

## 1. Herleitung

### 1.1 Radialgleichung

- L = |phi_t|^2 - |grad phi|^2 - U(|phi|^2), U(S) = S - S^2 + S^3/2, also U'(S) = 1 - 2S + (3/2) S^2.
- Mit phi = f(r) e^{i m theta - i omega t}:
  - |phi_t|^2 = omega^2 f^2
  - |grad phi|^2 = f'^2 + m^2 f^2/r^2
  - Wirkungsdichte je Flaeche: omega^2 f^2 - f'^2 - m^2 f^2/r^2 - U(f^2)
- Euler-Lagrange fuer das Radialfunktional Int r dr [...]:
  - -d/dr(-2 r f') = r [2 omega^2 f - 2 m^2 f/r^2 - 2 f U'(f^2)]
  - daraus (r f')'/r - m^2 f/r^2 = (U'(f^2) - omega^2) f
  - **f'' + f'/r - m^2 f/r^2 = a f - 2 f^3 + (3/2) f^5**, mit a = 1 - omega^2. Die Gleichung der Karte stimmt.
- Teilchenbild: f'' + f'/r = -Phi'(f) + m^2 f/r^2 mit Phi = (omega^2 S - U(S))/2.
  - Phi hat bei f = 0 ein Maximum (Phi = 0), bei f_tal ein Tal und bei f_top eine Kuppe.
  - S_tal,top = (2 -+ sqrt(6 omega^2 - 2))/3.
  - Q-Baelle gibt es fuer Phi(f_top) > 0, also 1/2 < omega^2 < 1.
- Coleman-Regel: Ueberschuss ist f > f_top oder f < 0, Unterschuss ist Umkehr im Tal (f' > 0 bei f < f_tal nach dem
  Fallen).
  - Fuer m >= 1 steigt der Ring von 0 auf, kehrt unter f_top um und muss genau bei 0 ankommen.
  - Zu kleines p: Die Reibung f'/r ueberwiegt den Zentrifugalterm (bei grossem Ringradius R wie T/R gegen m^2 n/R^3),
    die Bahn kommt nicht zurueck, also Unterschuss.
  - Zu grosses p: Die Bahn laeuft durch null oder ueber die Kuppe.

### 1.2 Ladung, Energie, Drehimpuls

- Ladungsdichte rho = 2 Im(phi conj(phi_t)) = 2 omega f^2, also **Q = 2 omega Int f^2 d^2x**.
- Energiedichte |phi_t|^2 + |grad phi|^2 + U, also **E = Int [omega^2 f^2 + f'^2 + m^2 f^2/r^2 + U(f^2)] d^2x**.
- Impulsdichte p_i = -2 Re(conj(phi_t) d_i phi). Drehimpulsdichte x p_y - y p_x = -2 Re(conj(phi_t) d_theta phi).
  - Mit d_theta phi = i m phi und conj(phi_t) = i omega conj(phi) wird daraus 2 omega m f^2.
  - Also **J = m Q** (fuer jede stationaere Loesung, unabhaengig vom Profil).

### 1.3 Identitaeten als Gegenproben

- **Virial (Derrick, 2D):** Gradient- und Zentrifugalterm sind in 2D skaleninvariant, also Int U d^2x = omega^2 Int f^2
  d^2x. Das gilt fuer jedes m. Spalte "Virialrest".
- **EL-Identitaet:** Gleichung mal f integriert gibt G = omega^2 N - Int S U'(S) (G = Gradient plus Zentrifugalanteil).
  Spalte "EL-Rest".
- **dE = omega dQ** entlang jeder Familie (Nebenprobe, Trapez zwischen Nachbarzeilen, grob).

### 1.4 NLS-Grenze omega -> 1 (in 2D kritisch)

- Mit f = sqrt(a) g(sqrt(a) r): g'' + g'/rho - m^2 g/rho^2 = g - 2 g^3 + (3/2) a g^5.
- Fuer a -> 0 bleibt die kubische NLS. In 2D ist sie kritisch:
  - N = Int f^2 d^2x = Int g^2 d^2rho haengt nicht von a ab.
  - Also Q -> 2 N_T(m), endlich.
- Townes-Werte (Pohozaev): Int g^4 = N_T und G_T = N_T. Daraus E - Q = O(a^2), also E/Q -> 1.
- **L4-Anker:** N_T(0) = 11,701/2 = 5,8505 (Townes-Norm 2 pi x 1,8623 in der Normierung R - R^3 [L]), also
  Q_lim(0) = 11,701.
- **Richtung:** Der Quintikterm wirkt defokussierend und hebt N an; nach den R3/R5-Zahlen ist dN/da gross. Deshalb faellt
  Q = 2 sqrt(1 - a) N(a) zum Rand omega -> 1 hin, fuer alle m.
  - Q_min(m) = inf Q = 2 N_T(m) wird nicht angenommen. Im Gitter liegt Q_min bei omega^2 = 0,99 (Randminimum).

### 1.5 Duennring-Asymptotik fuer grosse m (Schreibtisch [S])

- Ansatz g = A sech((rho - R)/w), dann das Funktional Int rho drho [g'^2 + m^2 g^2/rho^2 + g^2 - g^4] extremal in A, w, R:
  - A^2 = K, w = 1/sqrt(K), K = 1 + m^2/R^2
  - Bedingung d/dR: K = 3 m^2/R^2, also **R = sqrt(2) m** (skaliert) und K = 3/2
  - **N_T(m) = 2 pi R x 2 sqrt(K) = 4 sqrt(3) pi m = 21,77 m**, also **Q_lim(m) = 43,53 m**
- Ungeskaliert: Ringradius R = sqrt(2) m/sqrt(1 - omega^2), Dicke etwa 1/sqrt(K a), Dicke/R etwa 1/m.
  - Das ist ein duenner Ring, wie die Karte vermutet.
- Allgemein gilt fuer duenne Ringe bei jedem festen a: Querschnitt und m^2/R^2 = T/n haengen nur von a ab.
  - Also Q(m, a)/m -> q(a) und E(m, a)/m -> e(a), unabhaengig von m.
  - Damit Q_min ~ m **exakt im Grenzfall grosser m**, also beta -> 1.
- Duennwand-Seite (omega^2 -> 1/2, Formel aus RUNDE-05, PLAN.md Karte 2):
  - Loch R_h aus sigma R_h + P R_h^2 = S m^2, Aussenrand R_a aus P R_a^2 - sigma R_a - S m^2 = 0
  - Breite R_a - R_h = sigma/P, fuer grosse m R ~ m sqrt(S/P)
  - Auch dort Ringradius ~ m und Q ~ m. Der Rauchtest bestaetigt die Formel bei omega^2 = 0,52, m = 8: R_innen 48,4 gegen
    48,8 und R_aussen 66,1 gegen 66,3.

### 1.6 Folgerung fuer die fuehrende Bahn

- Zu festem J ist die Energie am kleinsten beim groessten m mit m Q_min(m) <= J (E etwa Q = J/m).
- Die Ecken der Bahn sind (E_min(m), J = m Q_min(m)) mit E_min etwa Q_min ~ m^beta.
  - Daraus **alpha = d ln J/d ln E = 1 + 1/beta**; beta -> 1 gibt alpha -> 2 und J etwa E^2/43,5.
  - Die Regge-Steigung in Modelleinheiten ist alpha' = J/E^2 etwa 1/43,5 = 0,023.
  - Das ist die Kinematik eines rotierenden Rings mit fester Ladung je Laenge.
- **Die Huelle E_min(J) ist ein Saegezahn und nicht monoton:**
  - Zwischen den Ecken m und m+1 liegt die Familie m mit E etwa J/m.
  - Bei J = (m+1) Q_min(m+1) springt E_min nach unten auf E_min(m+1).
  - Deshalb ist die primaere alpha-Zahl die Eckenzahl. Die Huellenfits E_min(J) (Karte) und J_max(E) (Chew-Frautschi)
    sind Nebenzahlen.

## 2. Numerik (Festlegungen vor dem Lauf)

- **Schiessen** wie r5_2d_a.py (RK4, Coleman-Regel fuer alle m, m = 0 linear in p, m >= 1 in ln p). Abweichungen im
  Kopf von regge2d.py:
  - Einschachtelung mit 15 Kandidaten je Zeile und Runde, bis die Klammer 8 ulp breit ist.
  - ln-p-Klammer -150 bis 5 (bei m = 8, omega^2 = 0,99 ist ln p etwa -42).
  - Schrittweite je Zeile h = h0 min(3, max(1, 0,3/sqrt a)); fuer omega^2 <= 0,9 und NLS h = h0.
  - Start bei r0 = 2m h fuer m >= 1 (m = 0: r0 = h wie R3/R5).
  - Schiessbereich bis r_cap = r0 + 60 + 30/kappa + 6 m/kappa.
- **Rauschboden:** Liegt ein Unterschuss oberhalb eines Ueberschusses, zaehlt das bis 1e-9 (relativ) als Rauschboden der
  Integration; die Klammer gilt dann als geschlossen. Darueber wird die Zeile "nicht monoton" und ungueltig.
- **Schwanz:** ab f < 1e-3 f_max (wie R3/R5). Weiter geht es mit der linearen Gleichung (Loesung K_m(sqrt(a) r)),
  rueckwaerts gerechnet bis r_cut + 30/kappa.
  - Ausgegeben werden Sprung von f'/f am Schnitt und die Spreizung der beiden Klammerbahnen dort.
- **Integrale:** Simpson auf dem Schiessgitter, Radien aus S = f^2:
  - R_max: Parabel durch das Maximum
  - R_innen, R_aussen: Halbwertsradien
  - r_mittel = Int r S / Int S
- **Gueltig:** Klammer geschlossen, Mitte-Bahn erreicht die Schwanzschwelle ohne Klassifikation, Einschachtelung monoton.
  Keine Loesung wird vermerkt, nicht geraten.
  - In die Fits gehen nur gueltige Zeilen mit |Virialrest| <= 1e-5.
- **Codeprobe J = m Q** (15 Zeilen: alle m bei 0,80, dazu m = 1, 4, 8 bei 0,55 und 0,95):
  - Hermite-Interpolation der Radialtabelle auf ein kartesisches Gitter, dx = min(0,25, Skala/10), N <= 1024,
    periodische Box bis f < 1e-8 f_max
  - spektrale Ableitungen; J = 2 omega Int Im(conj(psi)(x d_y - y d_x) psi) direkt aus dem Feld
  - dazu Q, E und der Rest der 2D-Feldgleichung -lap psi + (U' - omega^2) psi. Der kennt kein m^2/r^2 und prueft
    damit auch die Herleitung.

## 3. Vorhersagen

**Zeitfolge, offen gelegt (Zeiten gemessen):**
- Die Schreibtischrechnung (1.4 bis 1.6) entstand vor dem ersten Rauchtest, also zwischen dem Beginn 03:03:13 und dem
  Rauchteststart 03:27:53. Niedergeschrieben ist sie erst danach (Plan ab 03:32:04).
- Der Rauchtest zeigte m = 0, 1, 3 und 8 bei omega^2 = 0,52, 0,80 und 0,99 sowie die NLS-Grenze.
- Die Spalte "Stand" nennt je Zeile, was vorher feststand und was ich nach dem Rauchtest gebildet oder geaendert habe.
  Blind sind nur m = 2 und 4 bis 7, das volle omega-Raster, die Huellen und der Ringexponent bei omega^2 = 0,55 bis 0,95.

| Groesse | Karte (H) | meine Erwartung | Begruendung | Stand |
|---|---|---|---|---|
| Lage von Q_min(m) | nicht festgelegt | am oberen Rand omega^2 = 0,99 fuer alle m, Q faellt monoton mit omega^2 (p = 0,9) | 1.4: kritische NLS, Quintik hebt N | vor dem Rauchtest; fuer m = 2, 4 bis 7 blind |
| beta (Gitter, m = 3..8) | 1 | 0,99 (0,95 bis 1,02), p = 0,8 | Q_lim = 43,5 m + kleine Korrektur (N_T(1) etwa 24,1, N_T(2) etwa 44,4 [L?], also leicht unter linear) | vor dem Rauchtest; Vorschau 0,988 gesehen |
| alpha (Ecken, m = 3..8) | 2 | 2,01 (1,97 bis 2,05), p = 0,8 | alpha = 1 + 1/beta, E/Q = 1 - O(a^2) | vor dem Rauchtest; Vorschau 2,012 gesehen |
| Q_lim(0) | - | 11,70 +- 0,01 (Townes), p = 0,97 | L4 | vor dem Rauchtest; 11,7009 gesehen |
| Q_lim(m)/m, m = 8 | - | 43,5 bis 44 | 1.5 | vor dem Rauchtest; 43,62 gesehen |
| R_max sqrt(a)/m bei 0,99 | Ring R ~ m | sqrt(2) +- 10 % fuer m >= 3 | 1.5 | vor dem Rauchtest; 1,447 und 1,423 gesehen |
| Ringexponent gamma (ln R_max gegen ln m, m = 3..8) | 1 | vor dem Rauchtest: 1 bei 0,99, gegen 2 zur Duennwand hin (Loch ~ m^2/sigma). **Nach dem Rauchtest geaendert:** Mit dem Druckterm P wird auch dort R ~ m sqrt(S/P); erwartet 0,85 bis 1,0 bei jedem omega^2 | 1.5 | geaendert, nachdem 0,52 gesehen war (gamma 0,84 aus m = 3 und 8) |
| Dicke/R_max | "duenn" | etwa 1,02/m, bei m = 8 also 0,13 | 1.5 (FWHM von sech^2) | vor dem Rauchtest; 0,127 gesehen |
| Huelle E_min(J) | glatt J ~ E^2 | Saegezahn, 4 bis 5 Abwaertsspruenge (p = 0,85); Fit alpha_Huelle 1,9 bis 2,5 | 1.6 | Saegezahn vor dem Rauchtest, Spannen danach; blind (der Rauchtest hat nur m = 3 und 8) |
| Chew-Frautschi J_max(E) | - | alpha_CF 1,95 bis 2,3 | 1.6 | blind |
| Rotorprobe (fester Q) | E - E0 ~ J^2/Q heisst Exponent 2 | Exponent unter 1,5 (p = 0,7), kein starrer Rotor | Loch und Radius wachsen mit m | nach dem Rauchtest gebildet (Vorschau 0,86 aus m = 1, 3, 8) |
| gueltige Zeilen | - | alle 234 (p = 0,85) | Plateau hoechstens etwa 17,5 lang (1.5), also in float64 aufloesbar | nach dem Rauchtest (16 von 16) |
| R3-Anschluss (h0 = 0,01) | Gegenprobe | p gleich bis 1e-12, Q und E bis 1e-6 | gleiche diskrete Abbildung; Simpson statt Riemann | vor dem Rauchtest. **Knapp verfehlt:** dE/E = 4,0e-6 bei 0,80 (L2-Grenze 1e-4 bestanden) |
| J/(mQ) - 1 auf dem Gitter | exakt | unter 1e-6 | spektral, glattes Feld | vor dem Rauchtest; 4e-16 gesehen |
| L3 (h0 halbiert) | - | d alpha, d beta unter 1e-4 | RK4 O(h^4) | vor dem Rauchtest; 3e-11 gesehen (0,02 gegen 0,01) |

## 4. Auswertung (Definitionen, Unterbefehl `bahn`, auch am Ende von `tabelle`)

- **Q_min(m):** kleinstes Q der gueltigen Zeilen je m. Dazu Lage (Rand oder innen) und ob Q mit omega^2 monoton faellt.
  Q_lim(m) = 2 N_T(m) aus den NLS-Zeilen ist das Infimum.
- **beta:** Steigung ln Q_min gegen ln m ueber m = 3 bis 8 (kleinste Quadrate), dazu beta_lim aus Q_lim, lokale Steigungen
  und Standardfehler.
- **Fuehrende Bahn, primaer:** Ecken (E_min(m), J = m Q an derselben Zeile), m = 1 bis 8. alpha = Steigung ln J gegen ln E
  ueber m = 3 bis 8. Dazu alpha_lim (NLS-Ecken) und alpha' = J/E^2 je Ecke.
- **Fuehrende Bahn, Nebenzahlen:**
  - E_min(J) auf 400 log-Punkten zwischen den Ecken m = 3 und m = 8 (lineare Interpolation in ln-ln je Familie, Minimum
    ueber m); alpha_Huelle = 1/Steigung(ln E gegen ln J), mit Zahl der Abwaertsspruenge.
  - J_max(E) entsprechend, alpha_CF = Steigung.
- **Ringbild:** R_max(m), r_mittel(m), Dicke/R_max, R_max sqrt(a)/m bei omega^2 = 0,55 / 0,70 / 0,80 / 0,90 / 0,95 / 0,99,
  Exponent gamma ueber m = 3 bis 8; NLS: rho_max/m gegen sqrt(2).
- **Rotorprobe (Nebenprobe):** E_m(Q) bei Q = 300 und 1000 (Interpolation in ln Q), Exponent von E_m - E_0 gegen m.
- **L2:** m = 0 gegen R3; Codeprobe J = m Q; Virial- und EL-Rest; dE = omega dQ (grob).
- **L3:** `bahn --l3`: gleiche Auswertung der h0/2-Tabelle; Differenzen von alpha, beta, alpha_lim, beta_lim und
  max |dQ/Q|, |dE/E|.

## 5. Urteilsregeln (vorab)

- **alpha:**
  - "H getragen", wenn |alpha - 2| <= 0,1
  - "Gegenhypothese getragen", wenn alpha <= 1,6 (entspricht beta >= 1,67)
  - sonst "Zwischenwert"
- **beta:** "Ring-Mechanismus getragen", wenn |beta - 1| <= 0,1.
- **L2 bestanden:**
  - R3 (bei h = 0,01): |dp| <= 1e-9, |dQ/Q| und |dE/E| <= 1e-4, |dS_max| <= 1e-5, |dR_halb| <= 2e-3
  - Gitter: |J/(mQ) - 1|, |Q_g/Q - 1| und |E_g/E - 1| je <= 1e-4
- **L3 bestanden:** |d alpha|, |d beta| <= 0,01 und max |dQ/Q|, |dE/E| in den Fitzeilen <= 1e-5. Der Effekt, der H von der
  Gegenhypothese trennt, ist |alpha - 1,5| = 0,5, also 50-mal groesser.
- Das Urteil "H getragen" heisst nur: Die Q-Ball-Ringe in 2D folgen J ~ E^2. Ueber Glied 7 der Spin-2-Kette sagt es
  nichts (L5).

## 6. Latten

| Latte | Stand |
|---|---|
| L1 kann scheitern | **schwach.** alpha -> 2 folgt im Duennring-Grenzfall vorab (1.5, 1.6). Scheitern koennte der Test an drei Stellen: Q_min innen statt am Rand, m = 3 bis 8 noch nicht asymptotisch, Numerik. Neu waeren nur die Korrekturen bei endlichem m und die Huellenform. |
| L2 Gegenprobe | m = 0 gegen R3 (fuenf Zeilen), J = m Q direkt aus dem Feld, Q und E auf dem Gitter, Rest der 2D-Feldgleichung, Virial- und EL-Rest, Townes-Norm Q_lim(0) = 11,701. |
| L3 Numerik | halbe Schrittweite (h0 = 0,01 gegen 0,005); dazu Rauschboden, Schwanzsprung und Spreizung je Zeile. |
| L4 schon bekannt | teilweise, Abschnitt 9. Drehende Q-Baelle mit J = n Q und Ringform in 2+1D sind Literatur. Eine E(J)-Potenz fuer drehende 2+1D-Q-Baelle gibt es fuer ein anderes Modell: signum-Gordon, E ~ J^(1/5), also J ~ E^5. Regge-Bahnen von Q-Baellen oder Boson-Sternen habe ich nicht gefunden. Die Duennring-Asymptotik der NLS-Wirbel ist vermutlich bekannt; eine Quelle habe ich nicht geoeffnet. |
| L5 Messbezug | keiner. Hoechstens die Form "Turm mit Steigung alpha' = 0,023 in Modelleinheiten". Eine Bruecke zur String-Seite waere Hypothese, kein Befund zu Glied 7. |

## 7. Lokaler Rauchtest (Vorschau, gerechnet auf dem Laptop)

- **Aufruf** (Freigabe Finn 30.09. 02:42, laut Memory feedback-lokale-pruefung-ohne-python.md: CPU, 1 Thread, nice 19,
  120 s):

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/regge && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 \
  MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 regge2d.py rauch --out lauf-lokal/rauch
```

- **Zwei Laeufe:**
  - 03:27:53 bis 03:28:17: Dabei wurden die NLS-Zeilen m = 3 und 8 bei h0 = 0,01 als "nicht monoton" verworfen. Die
    Ursache war eine Vertauschung um 2e-14 in ln p, also Rauschboden, kein Befund. Danach kam die Rauschboden-Regel
    (Abschnitt 2) dazu.
  - Ebenfalls danach: Der p-Vergleich mit R3 zaehlt nur bei h = 0,01.
  - Zweiter Lauf 03:30:13 bis 03:30:41 (27,9 s): Ausgaben in lauf-lokal/rauch/, Protokoll in lauf-lokal/rauch.log.
- **Ergebnisse (m = 0, 1, 3, 8; omega^2 = 0,52 / 0,80 / 0,99; NLS; h0 = 0,02 und 0,01):**
  - 16 von 16 Zeilen gueltig. Virial- bzw. Pohozaev-Rest unter 1e-8, bei 0,80 und 0,99 unter 1e-11. Schwanzsprung bei
    0,52 bis 3e-3 (Genauigkeitsgrenze der Duennwand), sonst 1e-6.
  - **R3-Anschluss bestanden:**
    - omega^2 = 0,52: dp = 0, dQ/Q = -3,7e-8
    - omega^2 = 0,80: dp = 1,6e-15, dQ/Q = 1,1e-6, dE/E = 4,0e-6; vermutlich wegen der Riemann-Summe in R3 (Fehler
      O(h^2) bei r = 0), nicht geprueft
  - **J = m Q auf dem Gitter:** |J/(mQ) - 1| = 4e-16, Q und E auf dem Gitter bis 4e-10, Rest der 2D-Feldgleichung 9e-8.
  - **NLS-Grenze:**
    - Q_lim = 11,7009 / 48,2984 / 132,4234 / 348,9414 fuer m = 0 / 1 / 3 / 8
    - Townes 11,701 getroffen; Q_lim/m bei m = 8: 43,62 (Duennring 43,53)
  - **Q(0,99)** = 11,823 / 48,653 / 133,370 / 351,434, jeweils etwa 1,007 Q_lim. Q faellt monoton mit omega^2; Q_min liegt
    am Rand.
  - **Vorschau-Fits aus zwei Punkten (m = 3, 8):** beta = 0,9878, alpha = 2,0123, alpha_lim = 2,0123.
  - **Ringbild bei 0,99:** R_max sqrt(a)/m = 1,447 (m = 3) und 1,423 (m = 8) gegen sqrt(2); Dicke/R = 0,33 und 0,127.
  - **L3 (0,02 gegen 0,01):** d alpha = 3e-11, max |dQ/Q| in den Fitzeilen 7e-8.
- **Formprobe der Unterbefehle `tabelle` und `bahn`** (03:36:25 bis etwa 03:36:45, gleiche lokale Grenzen; m = 0, 3, 8,
  omega^2 = 0,80 und 0,99, h0 = 0,02 und 0,01; Ausgaben lauf-lokal/form/):
  - alle drei Aufrufe mit rc = 0
  - JSON-Hin- und Rueckweg und L3-Vergleich laufen; Zahlen wie im Rauchtest
  - Die Huellenzahlen dort sind ohne Aussage, weil je Familie nur zwei omega^2-Werte vorliegen.
- **Zeitprobe:**
  - erste Schiessrunde der vollen Tabelle 2,2 s
  - obere Schranke fuers Schiessen: h0 = 0,01 etwa 1 min, h0 = 0,005 etwa 2 min
  - Profile und Gitterprobe zusammen etwa 1 min

## 8. Aufrufe fuer die Hauptlaeufe (Leitung; je hoechstens 10 min, ein Kern)

- **Variante Laptop** (Nachtrag 03:00 im Memory: die Leitung rechnet kleine Laeufe bis 10 min lokal):

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/regge && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 600 python3 regge2d.py tabelle --h 0.01 --out lauf-lokal/h001
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/regge && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 600 python3 regge2d.py tabelle --h 0.005 --out lauf-lokal/h0005
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/regge && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 regge2d.py bahn --tabelle lauf-lokal/h001/ergebnis.json --l3 lauf-lokal/h0005/ergebnis.json --out lauf-lokal/bahn
```

- **Variante .69, CPU-Spuren:** vorher regge2d.py nach /home/fmh/fmhc-physics-remote/runde6-regge/ kopieren. Das Programm
  braucht nur numpy und schreibt nur nach --out. Die beiden Tabellen koennen parallel auf cpu und cpu2 laufen.

```
cd /home/fmh/fmhc-physics-remote/runde6-regge && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu rg1-h001 regge2d.py tabelle --h 0.01 --out ausgabe/h001
cd /home/fmh/fmhc-physics-remote/runde6-regge && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 rg1-h0005 regge2d.py tabelle --h 0.005 --out ausgabe/h0005
cd /home/fmh/fmhc-physics-remote/runde6-regge && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu rg1-bahn regge2d.py bahn --tabelle ausgabe/h001/ergebnis.json --l3 ausgabe/h0005/ergebnis.json --out ausgabe/bahn
```

- **Laufzeit (Schaetzung aus der Zeitprobe):**
  - tabelle h0 = 0,01: 1 bis 3 min
  - tabelle h0 = 0,005: 2 bis 4 min
  - bahn: unter 10 s
- **Speicher:** unter 0,5 GB. Am meisten brauchen die Gitterprobe (N = 1024, etwa 200 MB) und die Bahnspeicher
  (etwa 60 MB bei h0 = 0,005).
- **Die Ausgaben lesen:**
  - bahn/bericht.txt ab "Q_min(m)"
  - die Urteilszeile am Ende
  - L2 (R3, Gitter) und L3
  - dazu in tabelle/bericht.txt die Zeilen mit "NEIN"

## 9. L4: Literatur (Websuche zwischen 03:15:17 und 03:22:27, gemessen)

- **Geoeffnet (Abstract):** H. Arodz, J. Karkowski, Z. Swierczynski, "Spinning Q-balls in the complex signum-Gordon
  model", Phys. Rev. D 80, 067702 (2009), https://arxiv.org/abs/0907.2801.
  - 2+1D, kompakte Q-Baelle; fast alle drehenden Loesungen sind Ringe endlicher Breite.
  - "In the limit of large angular momentum M_z their energy is proportional to |M_z|^(1/5)", also J ~ E^5 in jenem
    (V-foermigen) Modell.
  - Die E(J)-Potenz drehender Q-Baelle ist damit fuer ein anderes Potential Literatur, mit ganz anderem Exponenten.
  - Welche Familie dort gemeint ist (festes n oder Minimum ueber n), habe ich im Abstract nicht gesehen.
- **Geoeffnet (Abstract):** T. A. Davydova, A. I. Yakimenko, "Stable multiple-charged localized optical vortices in
  cubic-quintic nonlinear media" (2003), https://arxiv.org/abs/physics/0308079.
  - 2D kubisch-quintische NLS, also die omega -> 1-Seite unseres Modells.
  - Stabile Wirbel mit mehrfacher Ladung oberhalb kritischer Leistungen. Zur m-Abhaengigkeit der Norm steht nichts im
    Abstract.
- **Suchtreffer, nicht geoeffnet [S]:**
  - "Angularly excited and interacting boson stars and Q-balls" (arXiv:0812.3968)
  - "Rotating boson stars in 2+1 dimensions" (Phys. Lett. B, 2004, sciencedirect.com/science/article/pii/S0370269304003880)
  - "Q-vortices, Q-walls and coupled Q-balls" (arXiv:1101.5366)
  - "Slowly rotating Q-balls" (Eur. Phys. J. C, 2024)
  - "Understanding the quantized angular momentum of rotating Q-balls" (JHEP 08 (2026) 108)
  - "Spinning Q-ball superradiance in 3+1D" (arXiv:2402.03193)
  - "Square vortex solitons with a large angular momentum" (arXiv:nlin/0407034)
  - Laut Suchtext: "all known solutions for rotating boson star configurations have the property that the total angular
    momentum increases proportionally to the mass of the star", also J ~ M bei Boson-Sternen [S, Zitat ungeprueft].
- **Aus dem Gedaechtnis [L?]:**
  - Volkov und Woehnert 2002 (drehende Q-Baelle, J = n Q)
  - Kleihaus, Kunz und List 2005 (3D)
  - Townes-Norm 11,70
  - Normen der NLS-Wirbel N(1) etwa 48,3, N(2) etwa 88,8 in der Normierung R - R^3
- **Nicht gefunden:** eine Arbeit, die Regge-Bahnen (J gegen E^2 der leichtesten Zustaende je Spin) fuer Q-Baelle oder
  Boson-Sterne ausweist. Vier Suchen, keine Treffer dazu. Das heisst nicht, dass es keine gibt.

## 10. Grenzen

- **2D statt 3D.** Die Kette zielt auf 3+1D. In 3D werden drehende Q-Baelle mit grossem m zu Tori. Deren Querschnitt ist
  ein 2D-Ball; in der NLS-Grenze ist dieser Querschnitt kritisch, die Ringbalance also entartet. Ob dort Q ~ m und
  alpha = 2 gelten, folgt nicht aus diesem Test (Hypothese).
- **Q_min am Gitterrand:** Das Gitter endet bei omega^2 = 0,99, das Infimum liegt bei omega -> 1. Beide werden
  ausgegeben; primaer zaehlt nach der Karte das Gitter.
- **Klassische Ladung:** J = m Q ist stetig. Ein "Turm" diskreter Zustaende entsteht erst mit ganzzahligem Q (Quantisierung),
  die hier nicht vorkommt. Die Ecken je m sind die naechste klassische Entsprechung.
- **Stabilitaet ist nicht Thema** (Karte). Viele dieser Ringe sind in 2D instabil (R5, Paket 2D-A).
- **Duennwandrand:** Bei omega^2 = 0,52 steht die Einschachtelung am Genauigkeitsrand von float64 (Plateau etwa 17,5 lang).
  Die Integrale sind dennoch gut (Virialrest 1e-9), der Schwanzsprung liegt bei 1e-3.
- **Die Huellenfits haengen am Saegezahn** und sind deshalb nur Nebenzahlen.

## Einfach gesagt

Wir rechnen fuer drehende Q-Baelle in einer flachen 2D-Welt aus, wie ihre Energie mit dem Drehimpuls waechst. Schnell
drehende Baelle werden zu duennen Ringen, und ein Ring mit m Drehungen ist ungefaehr m-mal so gross und traegt m-mal so viel
Ladung. Daraus folgt schon auf dem Papier: Der Drehimpuls waechst mit dem Quadrat der Energie, genau die Regel der Strings.
Der kleine Test auf dem Laptop bestaetigt das mit 2,01 statt 2. Weil die Regel aber schon aus der Ringform folgt, ist sie
kein Hinweis auf neue Physik, sondern ein Rechenergebnis fuer Ringe. Die grossen Laeufe pruefen noch alle Zwischenwerte und
die Rechengenauigkeit.

Ende der Bearbeitung: 2026-09-30 03:37:16 CEST (gemessen mit date). Beginn 2026-09-30 03:03:13 CEST.
