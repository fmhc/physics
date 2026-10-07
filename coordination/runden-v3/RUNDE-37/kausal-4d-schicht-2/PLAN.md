# KAUSAL-4D-SCHICHT-2: Plan (Code-Agent fuer die Leitung, Runde 39, explorativ nach v3)

- Start des Code-Agenten 2026-10-04 10:00:08 CEST (date). Plantext ab 10:17:40 CEST (date vor dem Schreiben).
- Karte: KARTE.md (Vorhersagen ab 09:59:10 CEST). Vorhersagen S2-0 bis S2-3 und ihre Schwellen unveraendert uebernommen
  (Abschnitt 7).
- Vor dem Plantext liefen nur Rauchlaeufe ohne Pol-, Erwartungs- oder Feldwerte von V-00 (Abschnitt 10).
- Code (code/):
  - kausal4d.py, kontinuum4d.py: unveraendert aus KAUSAL-WELLE-4D bzw. SCHICHT-1 (sha256 46311620... bzw. 4462504d...).
  - schicht2_feld.py: Teil B. Links, 1- und 2-Element-Intervalle aus einem GEMM; V-J, V-0, V-00 je Streuung.
  - schicht2_kont.py: Teil A. Pole, Argumentprinzip, Schalennullstelle ueber beide Blaetter, Erwartung, Linkzahlen.
  - schicht2_auswertung.py: Urteile, Bilder, auswertung.json.
- Kennzeichen:
  - [S] an der Quelle gelesen (hier aus zweiter Hand: SCHICHT-1, Dossier/Arbeitsfeld KAUSAL-4D-STABIL-L)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [M] eigene Mathematik; [H] Hypothese
  - [F] Festlegung dieses Plans (von der Karte offengelassen); [E] im Rauch gesehen

## 1. Varianten

- Sprungregel Phi = sum_n a_n L_n. L_n[y, x] = 1, wenn y vor x und das offene Intervall I(y, x) genau n Elemente
  enthaelt. Halt b = -m^2/rho in allen Varianten (Johnston (3.44)). a = sqrt(rho)/(2 pi sqrt 6).

  | Variante | a_0 (Links) | a_1 (1-Element) | a_2 (2-Element) | sigma | sum a_n Gamma(n + 3/2)/n! |
  |---|---|---|---|---|---|
  | V-J | a | 0 | 0 | +a | +a sqrt(pi)/2 |
  | V-0 | 2a | -2a | 0 | 0 | -a sqrt(pi)/2 |
  | V-00 | 3a | -7a | 4a | 0 | 0 |

- **Technik** wie SCHICHT-1: C (float32), je Block P = C[I0:I1, I0:J1] C[I0:J1, J0:J1]; Links bei C = 1 und P = 0,
  1-Element-Intervalle bei P = 1, 2-Element-Intervalle bei P = 2. Zaehler < N < 2^24, in float32 exakt.
- Rekursion psi = J - (m^2/rho) Phi^T psi, phi = (1/rho) Phi^T psi; Zuschauer (Palm) mit S = C Pm, Schicht n bei S = n.
- Gebiet D kausal konvex; alle Intervalle zwischen Punkten von D liegen in D, die Schichten sind also exakt [M, SCHICHT-1].

## 2. Bedingungen, Koeffizienten und Restformel [M]

**Grundlagen** (wie SCHICHT-1 PLAN 2, Gegenleser 1.1 bis 1.5 ohne Befund):
- mu_n(tau) = u^n/n! e^-u mit u = c tau^4, c = pi rho/24; f = sum a_n mu_n.
- k~_gen(Z) = (4 pi/Z) int tau^2 f K1(Z tau) dtau, Z^2 = |k|^2 - omega^2; K_P~ = k~_gen/(1 + m^2 k~_gen).
- Momente: S_p = int tau^p f dtau = sum_n a_n Gamma(n + (p + 1)/4)/(4 c^((p + 1)/4) n!).
  - p = 1: Gamma(n + 1/2); p = 3: Gamma(n + 1) = n! (also S_3 = sigma/(4c)); p = 5: Gamma(n + 3/2);
    p = 7: Gamma(n + 2) = (n + 1)!; p = 9: Gamma(n + 5/2).

**Reihe** [M; K1-Reihe L, DLMF 10.31.1]:
- K1(x) = 1/x + ln(x/2) I1(x) - (x/4) sum_j [psi(j + 1) + psi(j + 2)] (x^2/4)^j/(j! (j + 1)!),
  I1(x) = sum_j (x/2)^(2j + 1)/(j! (j + 1)!).
- Gliedweise: k~_gen = 4 pi S_1/Z^2 + R(Z^2) + L(Z^2) ln Z^2. R und L sind Potenzreihen in Z^2 mit reellen Koeffizienten.
  - L(Z^2) = sum_j L_j Z^(2j) mit L_j = pi S_(2j + 3)/(4^j j! (j + 1)!).
  - L_0 = (pi/(4c)) sigma und L_1 = (pi/(32 c^(3/2))) sum a_n Gamma(n + 3/2)/n!, wie SCHICHT-1.
  - Der Sprung ueber den Schnitt ist 2 pi i L(Z^2) = (4 pi^2 i/Z) int tau^2 f I1(Z tau) dtau, wie der Code (g_II).
- **Auf der Massenschale** (Z^2 = -M^2 - i0, ln Z^2 = ln M^2 - i pi) ist Im k~ = -pi L(-M^2). Den Rest bestimmt also
  die erste nichtverschwindende Zahl L_j.

**Drei Bedingungen** (x_n = a_n/a, n = 0, 1, 2):
- Normierung 4 pi S_1 = 1, also sum x_n Gamma(n + 1/2)/n! = sqrt(pi): x_0 + x_1/2 + 3 x_2/8 = 1.
- L_0 = 0 (sigma = 0): x_0 + x_1 + x_2 = 0.
- L_1 = 0 (naechste Ordnung): x_0/2 + 3 x_1/4 + 15 x_2/16 = 0, also 8 x_0 + 12 x_1 + 15 x_2 = 0.
- Determinante 3 - 7/2 + 3/2 = 1, also eindeutig: **x_2 = 4, x_1 = -7, x_0 = 3.**
- **V-00: a_0 = 3a, a_1 = -7a, a_2 = 4a.** Kern f = a (3 - 7u + 2u^2) e^-u = a (2u - 1)(u - 3) e^-u.
- **Pruefung gegen SCHICHT-1:**
  - V-0 (2, -2, 0): Normierung 2 - 1 = 1, sigma = 0, L_1-Summe 1 - 3/2 = -1/2. Das ist -a sqrt(pi)/2 wie dort.
  - V-00: Normierung 3 - 7/2 + 3/2 = 1, sigma = 0, L_1-Summe 3/2 - 21/4 + 15/4 = 0.

**V-00, naechste Groessen:**
- S_7 = a sum x_n (n + 1)/(4c^2) = a (3 - 14 + 12)/(4c^2) = a/(4c^2). Das ist derselbe Wert wie bei V-J.
- L_2 = pi S_7/192, also pi L_2 = pi^2 a/(768 c^2) = eps/(8 rho), mit eps = pi a/(4c) = sqrt 6/(2 pi sqrt rho).
- Konstante (sigma = 0): (pi/(8c)) sum a_n psi(n + 1) = (pi a/(8c)) [3 psi(1) - 7 psi(2) + 4 psi(3)] = -eps/2.
  - Damit M^2 = m^2/(1 - eps m^2/2); bei V-0 war es m^2/(1 - eps m^2).
  - Der feste Abstand zum Kontinuum halbiert sich also in fuehrender Ordnung (Amplitude ~ M^3/m^3, Gegenleser B9) [M].
- Reeller Z^2-Koeffizient: (pi/16) sum a_n M_5(n) psi(n + 3/2) = 1/(128 c) = 3/(16 pi rho).

**Restformel V-00 (vorab):**
- Mit Z^2 = -M^2 + delta folgt Im delta = -pi L_2 M^8 (1 + O(eps M^2)), also

  **Im omega(V-00) = pi L_2 M^8/(2 omega) = eps M^8/(16 rho omega) = sqrt 6 M^8/(32 pi rho^(3/2) omega).**

- Vorzeichen positiv, also Wachstum. Die Ordnung ist die dritte in m^2/sqrt(rho); V-J ist erste, V-0 zweite Ordnung.
- Reihe der Raten:
  - V-J: pi eps m^4/(2 omega)
  - V-0: (pi^2 eps^2/8) M^6/omega
  - V-00: (pi^2 eps^3/24) M^8/omega
  - V-0/V-J = (pi/4) eps M^2; V-00/V-0 = (eps/3) M^2.
- **Zahlen** (fuehrende Ordnung, m = 1):

  | rho | eps | M^2 (V-00) | Re omega ~ M (k = 0) | Im omega, k = 0 | Im omega, k = p |
  |---|---|---|---|---|---|
  | 4 | 0,19492 | 1,10799 | 1,0526 | 4,36e-3 | 3,91e-3 |
  | 8 | 0,13783 | 1,07402 | 1,0363 | 1,38e-3 | 1,24e-3 |
  | 16 | 0,09746 | 1,05123 | 1,0253 | 4,53e-4 | 4,04e-4 |

  - Faktor rho = 4 zu 16 (k = 0): 9,6. V-0: Formel 5,3 (0,0806/0,01514), Numerik SCHICHT-1 4,77.
- **Erwartete Korrekturen [M, grob]:**
  - naechster Logterm -0,083 M^2/sqrt(c): -13 % bei rho = 4, -6 % bei rho = 16
  - Ableitungsfaktor +2 % bzw. +0,4 %
  - Verschiebung der reellen Nullstelle: einige Prozent
  - Also liegt die Numerik voraussichtlich 10 bis 25 % unter der Formel bei rho = 4 und 5 bis 10 % bei rho = 16. Der
    Faktor 4 zu 16 sollte bei 8 bis 10 liegen.
- **Feinabstimmung (B4) [M]:** V-00 braucht zwei exakte Bedingungen.
  - Eine Abweichung delta-sigma bringt den Term erster Ordnung mit dem Gewicht delta-sigma/a zurueck.
  - Eine Abweichung delta_1 in sum x_n Gamma(n + 3/2)/n! bringt den m^6-Term mit dem Gewicht -2 delta_1/sqrt(pi)
    zurueck, gemessen am V-0-Rest.

**UV und weitere Nullstellen [M/H]:**
- Fuer abs(Z) >> c^(1/4) gilt k~ ~ 8 pi a_0/Z^4 = 24 pi a/Z^4. Das ist wie bei V-M in SCHICHT-1; V-M hatte keine weiteren
  Nullstellen.
- Auf der imaginaeren omega-Achse (reelles Z) dominiert im Integral der positive Bereich u < 1/2 mit grossem K1. Ich
  erwarte k~ > 0, also keine rein wachsenden Nullstellen [H, nicht gerechnet].
- Fuer andere Lagen bei rho = 4 (m^2/sqrt(c) = 1,38) bleibt es offen.

**Rauschen [H]:**
- Grobe Schaetzung mit unabhaengigen Beitraegen: s ~ sqrt(sum x_n^2 L_n/L_0).
- Mit L_1/L_0 = 0,440 und L_2/L_0 = 0,307 (Rauch, rho = 16) ergibt das 1 / 2,40 / 5,96 fuer V-J / V-0 / V-00.
- Auf SCHICHT-1 geeicht (s_V0/s_VJ = 2,05 statt 2,40) erwarte ich s_V00 ~ 1,6 (Spanne 1,2 bis 2,0), also etwa 2,5-mal
  s_V0.

## 3. Teil A: Pole, Zaehlung, Erwartung

- **Pole:** V-J, V-0 und V-00 bei rho = 4, 8, 16 und k = 0, p (p = sinh 0,5).
  - g_I = 1 + m^2 k~_gen mit Re Z > 0; g_II = g_I - m^2 D (zweites Blatt), alles wie SCHICHT-1, tau-Quadratur 128 Knoten.
  - Fortgesetzte Funktion F = g_I fuer Im omega > 0, g_II fuer Im omega <= 0; stetig ueber den zeitartigen Schnitt.
- **Regionen:**
  - **A:** abs(omega) < 10, Im omega > 0,05, wie SCHICHT-1 (Kartenwortlaut S2-3).
  - **S:** Re omega in [0,5; 2,0], Im omega in [0,002; 1,0], wie SCHICHT-1.
  - **S0 [F, neu]:** Re omega in [0,5; 2,0], Im omega in [1e-5; 0,002]. Rechteck, Zaehlung auf g_I mit denselben zwei
    Aufloesungen. Lokalisierung: Newton auf F ab x + 0,001 i, x = 0,5 bis 2,0 in Schritten von 0,05.
  - S und S0 zusammen heissen "nahe der Massenschale". Nullstellen mit 0 < Im omega < 1e-5 sieht die Zaehlung nicht.
- **Zaehlung:** Windungszahl adaptiv, zwei Aufloesungen (2 000 Startpunkte und 0,25 rad; 4 000 und 0,12 rad). "Stabil"
  heisst: beide aufgeloest und gleich. Lokalisierte Zahl gegen gezaehlte Zahl je Region.
- **Schalennullstelle [F, neu]:**
  - Definition: die Newton-Nullstelle von F ab omega_0 + 0,001 i, omega_0 = sqrt(k^2 + m^2).
  - Gueltig bei Residuum < 1e-9, Re omega > k und abs(omega - omega_0) < 0,6.
  - Blatt I bei Im omega > 0 (Wachstum), Blatt II bei Im omega < 0 (Zerfall).
  - **Konsistenz:**
    - Der Gegenstart omega_0 - 0,02 i trifft dieselbe Nullstelle (1e-8).
    - Bei Im >= 0,002 ist sie eine der lokalisierten S-Nullstellen und N_S >= 1.
    - Bei 1e-5 <= Im < 0,002 ist sie eine der lokalisierten S0-Nullstellen und N_S0 >= 1.
    - Bei 0 < Im < 1e-5: Vermerk "unter der Zaehlaufloesung".
  - **Warum neu:** Nach der Restformel liegt V-00 bei rho = 8 und 16 unter Im omega = 0,002, also ausserhalb von S.
    - Die Regel aus SCHICHT-1 faende dort N_S = 0 und suchte auf Blatt II. Newton auf g_II verlaesst dabei die untere
      Halbebene, das gibt kein gueltiges Ergebnis.
    - Die alte Regel wird trotzdem mitgerechnet ("schale_regel_schicht1"). Fuer V-J und V-0 muessen beide Regeln
      dieselbe Nullstelle liefern.
- **Weitere Nullstellen:** N_weitere = N_A - 2, wenn die Schalennullstelle auf Blatt I liegt und Im > 0,05 hat (Paar
  omega_s, -conj(omega_s)); sonst N_weitere = N_A.
- **Proben** (ohne Urteilskraft):
  - synthetische Windung in A, S und S0, dazu eine polartige Stelle auf der Achse bei 0,52 wie der Lichtkegelpunkt bei k = p
  - Blattstetigkeit (e = 1e-6 und 1e-8)
  - Momentprobe S_1 bis S_9 numerisch gegen die Gamma-Formeln
  - Sprungprobe D(i y) gegen die Reihe, y = 0,05 / 0,1 / 0,2
  - tau 128 gegen 256 Knoten an der Schalennullstelle und auf dem Bogen
  - Groessenprobe max abs(m^2 k~) auf abs(omega) = 10 und 20
- **Erwartung E[phi_v]** wie SCHICHT-1:
  - Linie Im omega = Gamma_1 = max(0,8; groesstes Im omega aller Blatt-I-Nullstellen bei k = 0 + 0,5), Gegenprobe
    Gamma_2 = Gamma_1 + 0,6.
  - rho = 4, 8, 16 und 10^6 (Grenzfall gegen den k-Raum, nur Gamma_1)
  - 9 Pruefpunkte und 17 Profilpunkte je Konfiguration, dazu 19 Achsenpunkte
  - tau-Quadratur 64 gegen 128 Knoten fuer V-0 und V-00 bei rho = 4
  - Erwartete Schichtzahlen L0/N, L1/N und L2/N fuer D bei rho = 16 (beschreibend).

## 4. Teil B: Felder

- Gebiet D, Quelle (sigma = 1, eta = 0 und 0,5, Kappe R_S = 3,5), Pruefpunkte, Profil, Zeitscheiben und Normmessung
  unveraendert aus kausal4d.py.
- **Saaten [F]:** rho = 16, Saaten 1 bis 12, SeedSequence([20261004, 38, 141, 16000, s]). Das sind dieselben Streuungen
  wie in SCHICHT-1.
  - V-J und V-0 muessen deshalb bitgleich mit SCHICHT-1 herauskommen (Kontrolle des neuen Codes).
  - S2-2 vergleicht V-00 auf genau den Streuungen, auf denen s_V0 = 0,636 gemessen wurde.
  - Eine neue Saatfolge haette eine unabhaengige Wiederholung von V-0 gebracht. Die Bitgleichheit als Codeprobe wiegt
    fuer diese Karte mehr.
- Je Saat eine Streuung, darauf alle drei Varianten und beide Konfigurationen.
- Laeufe: vier Bloecke zu drei Saaten, Zeitgrenze 540 s je Lauf. Fehlende Saaten folgen in weiteren Laeufen mit
  denselben Nummern.

## 5. Statistik und Groessen (wie SCHICHT-1)

- Saatmittel, SE_c = sqrt(var Re + var Im)/sqrt(n), ddof = 1.
- **Relative Streuung** je Pruefpunkt sd/abs(K) mit K = gekappte direkte Faltung.
  - s_v = geometrisches Mittel ueber die 18 Pruefpunkte (9 je Konfiguration), bei rho = 16.
- Beschreibend:
  - Saatmittel gegen eigene Erwartung (3 SE) und gegen das Kontinuum
  - abs(E)/abs(K)
  - Zuwachs [abs(E)/abs(K)](t = 3,2)/[...](t = 2,0) an Lage A. Er ist nach B2 kein reines Polmass und traegt kein Urteil.
  - Norm je Zeitscheibe, Schichtzahlen, max abs(phi)

## 6. Schreibtisch-Erwartung je Vorhersage (vor jeder Rechnung von V-00)

- S2-0: eingetroffen, 99 %. Gleicher Rechenweg wie SCHICHT-1, im Rauch fuer V-J bitgleich.
- S2-1: eingetroffen, 80 %.
  - Erwartet: 4,5e-4 (Formel), numerisch etwa 4,1e-4 bis 4,5e-4 bei rho = 16; Faktor 8 bis 10 gegen 4,77.
  - Risiko: weitere Blatt-I-Nullstellen nahe der Schale mit Im >= 0,004, oder instabile Zaehlung im duennen Streifen.
- S2-2: eingetroffen, 85 %. Schaetzung s_V00 ~ 1,6 gegen 0,636.
- S2-3: eingetroffen, 65 %. Die UV-Amplitude ist wie bei V-M, die Kernform aber anders (zwei Vorzeichenwechsel).

## 7. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| S2-0 | Kontrolle: V-0 gibt den Pol aus SCHICHT-1 wieder (Im omega = 0,0147 bei rho = 16, k = 0, auf 1e-3) | 90 % |
| S2-1 | [H] V-00: Massenschalen-Pol bei rho = 16 mit Im omega < 0,004 (oder kein Pol mit Im omega > 0 nahe der Massenschale), und der Wert faellt von rho = 4 bis 16 schneller als bei V-0 | 45 % |
| S2-2 | [H] Preis: Die relative Streuung je Saat ist bei V-00 groesser als bei V-0 (0,636 bei rho = 16) | 70 % |
| S2-3 | Keine weitere Nullstelle mit Im omega > 0,05 bei abs(omega) < 10 fuer V-00 | 60 % |

- Die Karte nennt keine Scheiterregeln und keinen Graubereich.
- "eingetroffen" heisst: Jeder Teil des Wortlauts gilt (Regeln unten). Sonst "nicht eingetroffen", ausser in den
  genannten Faellen "nicht auswertbar".
- Alle Urteile rechnet code/schicht2_auswertung.py mechanisch.

### 7.1 S2-0 [F]

- Massgeblich: Im omega der Schalennullstelle von V-0 bei rho = 16, k = 0 (Abschnitt 3).
- **eingetroffen**, wenn abs(Im omega - 0,0147) <= 1e-3 (absolut, Kartenwert). Beschreibend dazu: Abstand zum genauen
  SCHICHT-1-Wert 0,014700968 absolut und relativ, und die Nullstelle nach der alten Regel.
- **nicht auswertbar**, wenn die Schalennullstelle nicht bestimmbar oder nicht konsistent ist oder die S-Zaehlung nicht
  stabil ist.

### 7.2 S2-1 [F]

- Massgeblich ist k = 0 (wie SH1 in SCHICHT-1); k = p nur beschreibend.
- **(a)** Die Schalennullstelle von V-00 bei rho = 16 hat Im omega < 0,004.
  - Auf Blatt II (Im < 0) gilt (a), das ist der Fall "kein Pol mit Im omega > 0 nahe der Massenschale".
  - Zusaetzlich muessen alle lokalisierten Nullstellen in S und S0 (V-00, rho = 16, k = 0) Im omega < 0,004 haben.
- **(b)** Der Wert faellt von rho = 4 bis 16 schneller als bei V-0.
  - F_0 = Im(V-0, 4)/Im(V-0, 16), aus diesem Lauf (Erwartung 4,77).
  - Liegt V-00 bei rho = 4 und 16 auf Blatt I: F_00 = Im(V-00, 4)/Im(V-00, 16), und (b) heisst F_00 > F_0.
  - Liegt V-00 bei rho = 4 auf Blatt I und bei rho = 16 auf Blatt II: (b) gilt (Vorzeichenwechsel).
  - Liegt V-00 schon bei rho = 4 auf Blatt II: (b) ist nicht anwendbar, Urteil "nicht auswertbar" mit Vermerk.
- **eingetroffen**, wenn (a) und (b) gelten; sonst "nicht eingetroffen".
- **nicht auswertbar**, wenn
  - eine der Zaehlungen A, S, S0 fuer V-00 (rho = 4, 16, k = 0) oder S fuer V-0 (rho = 4, 16, k = 0) nicht stabil ist,
  - die lokalisierte Zahl in S oder S0 fuer V-00 (rho = 4, 16, k = 0) nicht der gezaehlten entspricht,
  - eine der vier Schalennullstellen (V-00 und V-0, rho = 4 und 16, k = 0) nicht bestimmbar oder nicht konsistent ist,
  - oder V-0 nicht auf Blatt I liegt.

### 7.3 S2-2 [F]

- s_V00 und s_V0 bei rho = 16 auf denselben 12 Saaten (Abschnitt 5).
- **eingetroffen**, wenn s_V00 > s_V0.
- **nicht auswertbar** bei weniger als 12 Saaten oder nicht endlichen Werten.
- Beschreibend: s_VJ, die Verhaeltnisse, s bezogen auf abs(E_v), je Punkt.

### 7.4 S2-3 [F]

- N_weitere(V-00) = 0 bei rho = 4, 8 und 16 sowie k = 0 und p (sechs Faelle, wie SH1 (d) in SCHICHT-1).
- **eingetroffen**, wenn alle sechs null sind; **nicht eingetroffen**, wenn einer groesser null ist.
- **nicht auswertbar**, wenn eine A-Zaehlung nicht stabil ist oder N_weitere < 0 herauskommt.
- Beschreibend: lokalisierte Nullstellen in A, Groessenprobe auf dem Bogen; V-J und V-0 nur beschreibend.

## 8. Kontrollen (ohne Urteilskraft)

- **Codeprobe** (rho = 1,2, Bloecke 256):
  - drei Schichten aus dem GEMM gegen dichtes C C (float64); C gegen Koordinaten
  - Rekursion je Variante gegen dichte Loesung und Reihe
  - Zuschauer je Variante gegen eine Schleife, die die Elemente in I(y, p) explizit zaehlt
- **Repro:** V-J und V-0 auf allen 12 Hauptsaaten gegen die SCHICHT-1-Dateien (bitgleich verlangt).
- **Teil A:**
  - synthetische Windung; zwei Aufloesungen; lokalisiert gegen gezaehlt; Blattstetigkeit
  - Moment- und Sprungprobe; tau 128 gegen 256 Knoten; Gamma-Gegenprobe; 64 gegen 128 Knoten (Erwartung)
  - rho = 10^6 gegen den k-Raum fuer alle drei Varianten
  - V-J und V-0: neue Regel gleich alter Regel und gleich SCHICHT-1
- **Teil B:** L0/N, L1/N und L2/N gegen die Integrale (beschreibend); Saatmittel gegen eigene Erwartung (3 SE,
  beschreibend); Endlichkeit; max abs(phi).

## 9. Hinweise zur Karte (vor dem Einfrieren)

1. **Kartenfehler: keinen gefunden.**
   - Die drei Bedingungen ergeben eindeutig (3, -7, 4) a.
   - Die Zahlen 0,0147 (S2-0) und 0,636 (S2-2) stimmen mit SCHICHT-1 (0,014701 bzw. 0,636).
   - Die Restformel 3 M^6/(16 rho omega) im Anlass ist die von SCHICHT-1.
   - Die Urteile nach Kartenwortlaut sind deshalb dieselben wie nach diesem Plan.
   - **Eine Stelle braucht eine Ergaenzung, keine Berichtigung:** "Nullstellenzaehlung wie in SCHICHT-1" sieht
     Nullstellen nur ab Im omega = 0,002. Nach der Restformel liegt V-00 bei rho = 8 und 16 darunter.
     - Woertlich mit der alten Zaehlung waere V-00 bei rho = 16 "kein Pol mit Im omega > 0 nahe der Massenschale".
       Damit gaelte S2-1 (a), aber der Abfall (b) waere nicht bestimmbar.
     - Deshalb ergaenze ich S0 und die Schalennullstelle ueber F (Abschnitt 3). A und S bleiben unveraendert.
2. **Offen gelassen und festgelegt [F]:**
   - S0, die Definition der Schalennullstelle und ihre Konsistenzpruefung
   - k = 0 fuer S2-0 und S2-1; S2-0 absolut 1e-3 gegen 0,0147
   - S2-1: Lesart von (a) mit allen Nullstellen nahe der Schale; F_0 aus diesem Lauf; Sonderfaelle der Blaetter
   - S2-2: Dichte 16, dieselbe Saatfolge wie SCHICHT-1
   - S2-3: drei Dichten und k = 0, p; Definition von N_weitere
   - "nicht auswertbar"-Faelle
3. **Gegenleser-Befunde aus SCHICHT-1:**
   - B2: Der Zuwachs ist hier nur beschreibend. Das Urteil zum Anwachsen ruht auf den Polen.
   - B5 (V-M klingt erst ab rho = 8 ab): V-M kommt in dieser Karte nicht vor.
   - B4 (Feinabstimmung): Je abgestellte Ordnung kommt eine exakte Bedingung hinzu (Abschnitt 2).
   - B7: Die Zaehlung in A sieht Nullstellen mit Im <= 0,05 ausserhalb von S und S0 nicht. Das gilt hier ebenso und
     steht so im ERGEBNIS.

## 10. Rauch (vor dem Plantext und vor dem Einfrieren)

Ordner rauch-69/ (Logs; Kopien aus /home/fmh/fmhc-physics-remote/runde39-kausal-schicht2/rauch/); .69-Zeiten in UTC, alle
rc = 0.

- **Codeprobe** (cpu6, 08:12:33 bis 08:13:55 UTC, rho = 1,2, N = 1 511, L0 = 33 120, L1 = 12 289, L2 = 7 535):
  - Schichten 0, 1, 2 aus dem GEMM gleich dichtem C C: ja, ja, ja. C gleich Koordinaten: ja.
  - Rekursion gegen dichte Loesung: 4,6e-16 / 3,8e-16 / 4,1e-16 (V-J / V-0 / V-00). Reihe <= 5,5e-16.
  - Zuschauer gegen Schleife: <= 4,1e-15.
  - Gesehen habe ich nur diese Pruefgroessen.
- **Repro und Zeit** (p4000a, 08:12:35 bis 08:15:01 UTC, rho = 16, Saat 91, Tag 141, gegen
  SCHICHT-1 rauch/feld/feld-r16-s91.npz):
  - N = 20 385, L0 = 2 140 832, L1 = 942 371 wie SCHICHT-1; dazu L2 = 657 207.
  - V-J und V-0: phi an den Zuschauern und Normsummen bitgleich (Abweichung 0,0).
  - Links 128,2 s, gesamt 142,7 s je Saat, 1,85 GB.
  - Die Ausgabe enthielt keine V-00-Werte.
- **Moment-, Sprung- und Windungsprobe** (cpu6, 08:15:03 bis 08:15:06 UTC; keine Pole):
  - 4 pi S_1 = 1 auf 7e-15 fuer alle Varianten und Dichten.
  - V-00: S_3 und S_5 auf Rundungsniveau null (<= 7e-15), S_7 wie analytisch.
  - Groesste Abweichung bezogen auf das Betragsintegral 4,4e-13.
  - Sprung D(i y) geteilt durch den ersten nichtverschwindenden Term (VJ: j = 0, V0: j = 1, V00: j = 2) bei
    y = 0,05 / 0,1 / 0,2: V-00 0,99971 / 0,99885 / 0,99542, also gegen 1.
  - Synthetische Windung: A 3/3, S 1/1, S0 1/1 (stabil), S ohne S0-Nullstelle 0/0.
- **Pole nur V-J, rho = 16** (cpu6, 08:15:29 bis 08:16:34 UTC):
  - k = 0: 1,0545310671831383 + 0,152322098799016 i nach neuer und alter Regel, bitgleich mit SCHICHT-1.
  - k = p: 1,17434 + 0,13678 i, ebenso.
  - N_A = 2, N_S = 1, N_S0 = 0; alle Zaehlungen stabil; lokalisiert = gezaehlt; konsistent.
  - 256 Knoten: <= 3,1e-15. Blattstetigkeit 3,3e-5 (e = 1e-6) bzw. 3,3e-7 (e = 1e-8).
  - 32 s je Fall.
- **Nicht gerechnet vor dem Einfrieren:** Pole, Erwartung oder Felder von V-00 und V-0.
  - Ausnahme: die Codeprobe, die keine Feldwerte zeigt.
  - Die Pole und Erwartung von V-0 kenne ich aus SCHICHT-1.
  - schicht2_auswertung.py ist vor dem Einfrieren nicht gelaufen.

## 11. Laeufe nach dem Einfrieren

- **cpu6:** pole V0 (rho 4, 8, 16), dann pole VJ, dann erwartung (alle drei Poldateien), dann feld 16 Saaten 7 bis 9.
- **p4000a:** pole V00, dann feld 16 Saaten 1 bis 3, dann 4 bis 6, dann 10 bis 12.
- Danach schicht2_auswertung.py auf lauf/ (12 Saaten).
  - Eine Pfadprobe der Auswertung darf vorher auf den ersten drei Saaten laufen (n_soll = 3). Ihre Urteile zaehlen
    nicht. Bricht sie ab, ist das ein Codefehler; die Behebung wird offengelegt.
- Hoechstens zwei Laeufe zugleich, je ssh-Aufruf ein Starteraufruf. Die Spur p4000a nutze ich nur als Lock; gerechnet
  wird auf der CPU mit einem Gewinde (wie SCHICHT-1), die GPU bleibt unbenutzt.

## 12. Einfrieren

- Kopie PLAN.md.eingefroren-JJJJMMTT-HHMMSS (Zeit per date), Code-Kopien mit derselben Endung, sha256 in
  code/pruefsummen-einfrieren.txt.
- Danach aendern sich Plan und Urteilsregeln nicht. Code nur bei echten Fehlern, offengelegt im ERGEBNIS.
