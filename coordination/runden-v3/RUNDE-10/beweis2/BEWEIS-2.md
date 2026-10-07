# BEWEIS-2: zwei weitere stille Stellen des 3D-Q-Balls, rechnergestuetzt, im linearen Modell

- Autor: Beweis-Agent der Leitung claude-primary (Claude, Haus Anthropic), derselbe wie BEWEIS-1. Auftrag: BRIEF.md
  (ab 12:05:26 CEST). Plan und Lemmata: BEWEIS-2-PLAN.md. Zeitverlauf: STAND.md.
- Beginn 2026-09-30 12:06:22 CEST; dieser Text ab 12:25:51 CEST (date).
- Grundlage: BEWEIS-1 (RUNDE-07/beweis/). Dort nur der von der Leitung erbetene Textabschnitt 7.2 in BEWEIS.md,
  ohne Neulauf und ohne Aenderung an zertifikat/.

## Ergebnis

- **T1 (l = 0, n = 2): bewiesen** (rechnergestuetzt, linear, Sektor l = 0). Gleicher Satzaufbau wie BEWEIS-1, derselbe
  Kern (byte-gleich), nur neue Startwerte. Beweislauf A und Wiederholung B bestanden.
- **T2 (l = 1, n = 1): bewiesen** (rechnergestuetzt, linear, Sektor l = 1, je m). Neuer Kernzweig fuer l = 1 (Start
  in alpha = A/r^2 mit Integralform, Zentrifugalterm, Riccati-Schwanz). Beweislauf A bestanden; T2 stuetzt sich
  allein auf T2-A.
  - Die Wiederholung B mit den vorab gewaehlten Parametern scheiterte in der c-Zeile des Krawczyk-Tests (Kasten in c zu
    schmal; Ursache der Profilblock, berichtigt in 4.5).
  - B2 mit exakt vergroessertem c-Radius bestand. B2 ist ein adaptiv gewaehlter Kasten, keine vorab festgelegte
    Wiederholung und kein unabhaengiger Code.
  - Frei-Test l = 1 und Kontrollen bestanden.
- n = 1, n = 2 sind Leiteretiketten aus dem Datenpaket, keine zertifizierte Knotenzahl.
- **Gelesen in zwei Haeusern** (Anthropic: T1 und T2 "traegt mit Auflagen"; OpenAI: T1 "traegt" im eingeschraenkten
  linearen radialen Sinn, T2 "traegt mit Auflagen"; nichts blockierend). Einarbeitung nur
  als Text in Abschnitt 8, ohne neuen Lauf, zertifikat/ unveraendert.
- Vertrauensannahmen wie BEWEIS-1: python-flint 0.9.0 / FLINT rechnet richtig. Kein zweites unabhaengiges Programm.
  Die Lesungen (Abschnitt 8) haben Lemmata, Code und Zahlen gegengelesen (Kopfrechnung, jq), aber keine ODE-, H_0-
  oder Krawczyk-Nachrechnung gemacht.
- Umgesetzt aus der Fremdlesung von BEWEIS-1 (Haus OpenAI; Nachricht der Leitung, eingearbeitet ab 12:16):
  - Auflage 1: 2 kappa0 > kappa_c steht im Gesamtflag M3.BESTANDEN.
  - Auflage 2: Einfachheit heisst hier nur geometrische Vielfachheit 1.
  - Auflage 3: "eingebettet" nur im operationalen Sinn.
  - Auflage 4: Y, DH_0(Z), Mk und die Untergrenzen von phibar und eta stehen im JSON.

## 1. Satz T1 (l = 0, Leiteretikett n = 2)

Bezeichnungen wie BEWEIS-1: U(S) = S - S^2 + S^3/2, N(f) = (1 - omega^2) f - 2 f^3 + (3/2) f^5,
V_pm = 1 - 4S + (9/2) S^2 - (omega pm rho)^2, C = -2S + 3S^2, S = f^2.

Z sei der Kasten z0 +- delta mit den exakten dyadischen Zahlen aus zertifikat/ZERT-T1-A-L32.json (Feld protokoll.Z
und export.delta). In Dezimalform (nach aussen gerundet):

| Groesse | untere Grenze | obere Grenze |
|---|---|---|
| a = f(0) | 1,064896026677023097387669985 | 1,064896026677023097395827310 |
| c | 36,91397776714791725575 | 36,91399461932547431920 |
| rho | 1,690356597328143456807519406 | 1,690356597328143456846998028 |
| omega | 0,827725138230207487803945082 | 0,827725138230207487831177773 |

Damit omega^2 in [0,6851289044582160933 +- 2,5e-20] und rho in [1,6903565973281434568 +- 4,7e-20] (Satz-Modus, LAUF-t1-satzA.log; Kugeln nach aussen gerundet).

**Satz T1.** Es gibt (a*, c*, rho*, omega*) in Z mit:
1. **Profil.** Die Loesung f von f'' + (2/r) f' = N(f), f(0) = a*, f'(0) = 0 (omega = omega*) existiert auf [0, oo), ist
   positiv, und r e^{kappa0 r} f(r) -> c*. phi = e^{i omega* t} f(|x|) ist ein positiver radialer Q-Ball der NLKG.
2. **Mode.** A'' = V_+ A + C B, B'' = V_- B + C A hat eine nichttriviale reelle Loesung Psi mit A(0) = B(0) = 0 und
   |A(r)| + |B(r)| <= K_J e^{-kappa_c r} fuer r >= L = 32, K_J <= 1 + 2,56e-15.
3. **Einfachheit (geometrisch).** Jede auf [L, oo) quadratintegrierbare Loesung dieses Systems bei festen
   (rho*, omega*) ist ein Vielfaches von Psi (Lemma E). Keine Aussage zu algebraischer Vielfachheit oder Stabilitaet.
4. **Folgerung.** a = A/r, b = B/r sind glatt und exponentiell abfallend; delta phi = e^{i omega* t}(a e^{i rho* t} +
   b e^{-i rho* t}) loest die linearisierte NLKG. Eingebettet im operationalen Sinn: k^2 = (omega* + rho*)^2 - 1
   >= 5,3407 (Kanal omega + rho offen), kappa_c^2 >= 0,25586 (Kanal omega - rho geschlossen).
5. **Korollar (Krein, Formel aus KREIN-1).** E_2 = 2 rho* [(omega* + rho*) ||a||^2 + (rho* - omega*) ||b||^2] > 0,
   weil rho - omega >= 0,8626 > 0 auf ganz Z. Die Formel ist in KREIN-1 hergeleitet und hier nicht neu geprueft; ein
   Stabilitaetssatz folgt daraus nicht.

Nicht behauptet: Eindeutigkeit in Z, wesentliches Spektrum des vollen Bueschels, nichtlineare Strahlungsfreiheit,
Eindeutigkeit des Profils unter allen positiven radialen Loesungen [L?].

## 2. Satz T2 (l = 1, Leiteretikett n = 1, Schwapp-Leiter)

Z sei der Kasten aus zertifikat/ZERT-T2-A-L36.json (protokoll.Z, export.delta; exakte Dyadiken). Nach aussen gerundet:

| Groesse | untere Grenze | obere Grenze |
|---|---|---|
| a = f(0) | 1,053524284176264539997729961 | 1,053524284176264540039943565 |
| c | 12,12363911265958500231 | 12,12363965981975312046 |
| rho | 1,826342030181069956187558772 | 1,826342030181069956296773986 |
| omega | 0,868617299955876559803915647 | 0,868617299955876559857955441 |

Damit omega^2 in [0,7544960137826372331 +- 7,8e-20] und rho in [1,826342030181069956 +- 3,0e-19] (Satz-Modus, LAUF-t2-satzA.log; Kugeln nach aussen gerundet).

**Satz T2.** Es gibt (a*, c*, rho*, omega*) in Z mit:
1. **Profil** wie Satz T1 (positiver radialer Q-Ball bei omega*, Schwanzamplitude c*).
2. **Mode.** Das System A'' = (V_+ + 2/r^2) A + C B, B'' = (V_- + 2/r^2) B + C A hat eine nichttriviale reelle Loesung
   Psi, die am Ursprung regulaer ist (A, B = O(r^2), Psi in span{R_1, R_2}), mit
   |A(r)| + |B(r)| <= K_J e^{-kappa_c r} fuer r >= L = 36, K_J <= 1,09656 (= 1 + 1/(kappa_c L) + (a1 + b1) eps,
   Lemma J-l1; Normierung e^{kappa_c r} B -> 1).
3. **Einfachheit (geometrisch).** Im Radialsektor (l, m) = (1, m) ist der Raum der auf [L, oo) quadratintegrierbaren
   Loesungen bei festen (rho*, omega*) eindimensional (Lemma E-l1). Keine Aussage zu algebraischer Vielfachheit oder
   Stabilitaet; die Entartung in m = -1, 0, 1 kommt aus der Kugelsymmetrie.
4. **Folgerung.** Y_1m bezeichnet eine **reelle** orthonormale Basis der Kugelflaechenfunktionen zu l = 1
   (proportional zu x/r, y/r, z/r). Fuer jedes m sind a Y_1m und b Y_1m mit a = A/r, b = B/r glatt und exponentiell
   abfallend (Lemma R-l1), und delta phi = e^{i omega* t}(a e^{i rho* t} + b e^{-i rho* t}) Y_1m loest die
   linearisierte NLKG. Bei komplexen Y_lm traegt das zweite Seitenband Y_lm*:
   delta phi = e^{i omega* t}(a Y_lm e^{i rho* t} + b Y_lm* e^{-i rho* t}) (BEWEIS-2-PLAN.md 4.1). Eingebettet
   im operationalen Sinn: k^2 >= 6,2628 (Kanal omega + rho offen), kappa_c^2 >= 0,08276 (Kanal omega - rho geschlossen).
   Die beiden Laborfrequenzen omega* +- rho* sind gezeigt; ueber ihr Verhaeltnis wird nichts behauptet
   (periodisch oder quasiperiodisch).
5. **Korollar (Krein, Formel aus KREIN-1).** E_2 > 0, weil rho - omega >= 0,9577 > 0 auf ganz Z. Die Formel fuer E_2
   ist in KREIN-1 hergeleitet und hier nicht neu geprueft; ein Stabilitaetssatz folgt daraus nicht.

Nicht behauptet: wie Satz T1; ausserdem nichts ueber andere l oder die Translationsmode (rho = 0).

## 3. Beweisstruktur

T1: wortgleich BEWEIS-1, Abschnitt 2 (Nullstellenproblem H = H_0 + E in z = (a, c, rho, omega); Lemma P und J fuer den
Schwanz; Lemma T0 und T fuer die Vorwaertsintegration mit 38 Komponenten im Kastenlauf; Brouwer-Krawczyk mit Stoerterm
(Lemma K); Lemma Pos, R, E, W). Die Bedingungen der Lemmata sind in Kugelarithmetik ueber ganz Z geprueft und
stehen im Gesamtflag M3.BESTANDEN (Tabelle 4.2), mit zwei Ausnahmen (berichtigt nach der Lesung, ab 13:15):
- 0 < h < R, N >= 1 und qfac > 1 standen fuer T1 nicht im Flag (die Pruefung kam erst in pruef-l1.py).
  - 0 < h < R ist nachtraeglich aus den Schrittprotokollen mit jq geprueft: alle 350, 362, 487 und 508 Schritte
    erfuellen es.
  - N >= 1 und qfac > 1 folgen aus dem Feld parameter mit dem Unterfeld kommandozeile (N = 64/48 bzw. 72/44,
    --q 3 bzw. 4). In den Schrittprotokollen stehen sie nicht (berichtigt nach der Lesung der letzten Schicht, L3).
- R < r_j (fuer alle Schritte mit r_j > 0; der erste Schritt bei r_j = 0 ist die Reihe um 0 nach Lemma T0) steht nicht
  in M3.BESTANDEN.
  - Das Protokoll fuehrt es als R_kleiner_rj_alle = true, gebildet als (R < r_j) oder r_j = 0.
  - Geprueft wird es vor jedem Schritt mit r_j > 0 in Kugelarithmetik (bewkern.py, apriori). Bei R >= r_j verwirft
    der Kern den Schrittversuch und nimmt ein kleineres R (bewkern.py, integrate). Erst bei R < 1/1000 bricht der Lauf
    ab. Schon die Schrittwahl gibt R <= r_j/2.
  - Kein angenommener Schritt hat R >= r_j (jq). Berichtigt nach der Lesung der letzten Schicht (L2, L3); vorher stand
    hier "bricht der Lauf ab" und "in keinem Flag".

T2: derselbe Aufbau, mit den l = 1-Fassungen (BEWEIS-2-PLAN.md 4):
1. **Nullstellenproblem.** H_0,1/2 wie T1 (Profil). H_0,3/4 = s3 W(J_0, R_i) mit den freien l = 1-Jost-Daten
   J_0 = (0, 1 + 1/(kc L), 0, -(kc + 1/L + 1/(kc L^2))). E_3, E_4 aus Lemma J-l1. H(z*) = 0 heisst nach Lemma W-l1:
   Die Jost-Loesung hat keinen Anteil an den singulaeren Loesungen ~ r^{-1}, ist also regulaer am Ursprung.
2. **Vorwaertsintegration.** Erster Schritt in alpha = A/r^2, beta = B/r^2 mit der Integralform (Lemma T0-l1), exakte
   Umrechnung bei h0, danach Lemma T-l1 mit 2/r^2 in P und Q (R < r_j geprueft).
3. **Schwanz** exakt mit Riccati-Funktionen (Lemma J-l1), Profilschwanz unveraendert (Lemma P).
4. **Brouwer-Krawczyk** (Lemma K), Positivitaet (Lemma Pos), Einfachheit (Lemma E-l1), Regularitaet (Lemma R-l1).
   Alle Bedingungen einschliesslich k L >= 1, kc L >= 1 und 0 < h < R im Gesamtflag (Tabelle 4.5). R < r_j gilt wie
   bei T1 fuer alle Schritte mit r_j > 0: Protokollwert R_kleiner_rj_alle, nicht in M3.BESTANDEN; bei einem Verstoss
   wird der Schrittversuch verworfen und R verkleinert.

## 4. Zertifikate

### 4.1 Laeufe T1 (.69, Spur cpu5, ein Kern, kleintest.sh; Zeiten gemessen)

| Lauf | Zweck | Parameter | Ergebnis | Laufzeit |
|---|---|---|---|---|
| t1-start | Startwert (float, nicht streng) | w2, rho aus A02 | a = 1,06490, c = 36,92 | 0,9 s |
| t1-newton | z0 (nicht streng) | Ls 12, 20, 28, 32; N = 48; q = 1/3; 256 bit | omega^2 = 0,685128904458216, rho = 1,690356597328143 | 410 s |
| ZERT-T1-A-L32 | **Beweislauf** | L = 32; Punkt N = 64, Kasten N = 48; q = 1/3; 256 bit; Faktor 8 | **bestanden** | 68,3 s |
| ZERT-T1-B-L36 | Wiederholung | L = 36; Punkt N = 72, Kasten N = 44; q = 1/4; 320 bit; Faktor 8; gleiches z0 | **bestanden** | 96,9 s |

### 4.2 Zahlen des Beweislaufs A (T1)

Rundung: Untergrenzen abgerundet, Obergrenzen aufgerundet; Quelle ZERT-T1-A-L32.json (protokoll, export).

| Groesse | Wert |
|---|---|
| khat (fest) | 2540974827025 * 2^-40 ~ 2,3110 |
| Schritte Punkt / Kasten | 350 / 362; R < r_j in allen Schritten mit r_j > 0 (R_kleiner_rj_alle); Fehlversuche 209 / 216 |
| erster Schritt | Punkt: R = 13/64, h0 = 13/128 nach 7 Verkleinerungen, Rest <= 1,9e-38; Kasten: R = 41/256, h0 = 41/512 nach 8 Verkleinerungen, Rest <= 2,3e-28 |
| groesster Schrittrest | Punkt <= 6,9e-29, Kasten <= 1,4e-14 |
| H_0(z0) | [+- 1,1e-6], [+- 6,3e-7], [+- 4,6e-23], [+- 1,8e-22] |
| delta (a, c, rho, omega) | ~ 4,08e-21; ~ 8,43e-6; ~ 1,97e-20; ~ 1,36e-20 (exakt dyadisch in export.delta) |
| eps_1 .. eps_4 | <= 1,975e-14; <= 2,278e-14; <= 2,919e-22; <= 7,067e-22 |
| Lemma P (i) | f* <= 1,8354e-8 < 1,8537e-8 <= phibar (phibar_unten im JSON) |
| Lemma P (ii) | K m^3 <= 1,9747e-14 < 3,9492e-14 <= eta (eta_unten im JSON) |
| Lemma P (iii), (iv) | Lambda <= 1,605e-15 < 1; c - eta >= 36,9139777 |
| Lemma J | Q <= 1,801e-15, mu <= 0,98847, eps <= 1,781e-15, K_J - 1 <= 2,56e-15 |
| Kanaele ueber Z | k^2 >= 5,340735, kappa_c^2 >= 0,255866, rho - (1 - omega) >= 1,518081, (1 + omega) - rho >= 0,137368 |
| Weitere Bedingungen ueber Z (Gesamtflag) | 2 kappa0 - kappa_c >= 0,616434; 2 omega^2 - 1 >= 0,370257; rho > omega; 4 - 6 kappa0^2 > 0 |
| Krawczyk | Kr strikt im Innern; Innenabstand >= 0,8742 delta je Koordinate; gewichtete Zeilensumme <= 7,6098e-4; ungewichtet <= 4,973e9 |
| Breite von D relativ zu mid | <= 7,4e-5 |
| M1 (Profil bei omega0) | bestanden: a in [1,064896026677023097392 +- 5,5e-22], c in [36,91399 +- 4,9e-6], Zeilensumme <= 2,1e-6 |
| Positivitaet | L_p = 7,837646484375, danach |f| < thr mit thr >= 0,42706 |

Lauf B (L = 36, 320 bit), soweit abweichend: delta ~ 1,06e-23; 1,51e-13; 1,05e-22; 8,26e-23; eps_1..4 <= 1,753e-16;
2,016e-16; 3,280e-25; 7,940e-25; K_J - 1 <= 2,3e-17; Zeilensumme <= 0,08452; Innenabstand >= 0,7904 delta (c), sonst
>= 0,87498 delta; L_p = 7,89227294921875.

### 4.3 Empfindlichkeitskontrolle (nicht streng)

| Lauf | rho + delta/4 | rho + delta | rho + 4 delta | Vorab erwartet |
|---|---|---|---|---|
| T1-A | besteht | verfehlt | verfehlt | so erwartet |
| T1-B | besteht | **besteht** | verfehlt | delta sollte verfehlen: **Erwartung verfehlt** |

Grund fuer B: Dort ist delta = 8 (|Y H_0(z0)| + |Y| eps) vom Newton-Abstand bestimmt. z0 stammt aus dem Newton bei
L = 32, N = 48; die Nullstelle der genaueren B-Abbildung liegt etwa 0,11 delta_rho ueber z0 (Kr_rho in
1,69035659732814345682727 +- 1,9e-24; z0_rho = 1,690356597328143456827258717..., die Mitte der Z-Grenzen, berichtigt
nach der Lesung ab 13:15; Abstand 1,13e-23 = 0,108 delta_rho, Kr-Radius 0,017 delta_rho). Kr ist also nicht um z0
zentriert,
und die Verschiebung um + delta behaelt die Nullstelle im verschobenen Kasten. Das zeigt eine Grenze dieser Kontrolle
(sie setzt Kr um z0 voraus), keine Luecke des Beweises: die Strenge liegt allein in den Lemmata und der Kugelrechnung.

### 4.4 Laeufe T2

| Lauf | Zweck | Parameter | Ergebnis | Laufzeit |
|---|---|---|---|---|
| t2-frei | Frei-Test l = 1 (f = 0) | L = 40, N = 64, q = 1/3, 256 bit | **bestanden**: A_1, A_1', B_2, B_2' = Riccati-Werte (relativ <= 4,3e-37), B_1 und A_2 enthalten 0 | 3,4 s |
| t2-start | Startwert (float) | w2, rho aus C01 | a = 1,05352, c = 12,12 | < 1 s |
| t2-newton | z0 (nicht streng) | Ls 12, 20, 28, 36; N = 48; q = 1/3; 256 bit | omega^2 = 0,754496013782637, rho = 1,826342030181070 | 374 s |
| ZERT-T2-A-L36 | **Beweislauf** | L = 36; N = 64/48; q = 1/3; 256 bit; Faktor 8 | **bestanden** | 63,6 s |
| ZERT-T2-B-L40 | Wiederholung, vorab gewaehlt | L = 40; N = 72/44; q = 1/4; 320 bit; Faktor 8 | **nicht bestanden** (c-Zeile, 4.5) | 96 s |
| ZERT-T2-B2-L40 | Wiederholung mit c-Radius mal 2^17 | wie B, dazu --dcexp 17 | **bestanden** | 95,9 s |
| t2-kontrolle | T1 A-priori gegen Rekursion (mit 2/r^2), T2 Differenzenquotienten | L = 36 | T1: Mittelpunkte gleich bis <= 5,2e-77 bzw. exakt; T2: relativ <= 7,8e-14 | 79 s |

### 4.5 Zahlen des Beweislaufs A (T2)

Quelle ZERT-T2-A-L36.json; Rundung wie 4.2.

| Groesse | Wert |
|---|---|
| khat (fest) | 2751593698811 * 2^-40 ~ 2,5026 |
| Schritte Punkt / Kasten | 319 / 338; 0 < h < R in allen Schritten (Gesamtflag); R < r_j in allen Schritten mit r_j > 0 (Protokollwert R_kleiner_rj_alle; ein Verstoss verwirft den Schrittversuch); Fehlversuche 183 / 203 |
| erster Schritt (T0-l1, Integralform in alpha, beta) | Punkt und Kasten: R = 13/32, h0 = 13/64 nach 4 Verkleinerungen, 3 Inflationsrunden; Rest <= 8,3e-39 bzw. <= 2,0e-28 |
| groesster Schrittrest | Punkt <= 9,7e-30, Kasten <= 8,4e-17 |
| H_0(z0) | [+- 3,42e-8], [+- 1,80e-8], [+- 1,44e-24], [+- 6,61e-24] |
| delta (a, c, rho, omega) | ~ 2,11e-20; ~ 2,74e-7; ~ 5,46e-20; ~ 2,70e-20 |
| eps_1 .. eps_4 | <= 8,992e-16; <= 9,160e-16; <= 3,434e-21; <= 1,146e-20 |
| Lemma P (i), (ii) | f* <= 6,0346e-9 < 6,0948e-9 <= phibar; K m^3 <= 8,9915e-16 < 1,7982e-15 <= eta |
| Lemma P (iii), (iv) | Lambda <= 2,225e-16 < 1; c - eta >= 12,1236391 |
| Lemma J-l1 | a1 <= 0,39965, a2 <= 1,00007, b0 <= 1,09656, b1 <= 1,90582, b2 <= 1,10122; mu <= 1,90582; Q <= 2,205e-16; eps <= 2,418e-16; E_A <= 9,663e-17, E_B <= 4,608e-16, E_A' <= 2,418e-16, E_B' <= 2,663e-16; K_J <= 1,09656 |
| Kanaele ueber Z | k^2 >= 6,262805, kappa_c^2 >= 0,082763, rho - (1 - omega) >= 1,694959, (1 + omega) - rho >= 0,042275 |
| Weitere Bedingungen (Gesamtflag) | 2 kappa0 - kappa_c >= 0,703280; 2 omega^2 - 1 >= 0,508992; rho > omega; 4 - 6 kappa0^2 > 0; k L >= 90, kappa_c L >= 10,35 |
| Krawczyk | Kr strikt innen, Innenabstand >= 0,8734 delta; gewichtete Zeilensumme <= 1,5402e-3; ungewichtet <= 9,641e6 |
| Breite von D relativ zu mid | <= 1,4e-3 (Zeilen H_0,3/4, Spalte a); sonst <= 4,6e-5 |
| M1 / M2 | M1 bestanden (Zeilensumme <= 3,3e-7); F_1 in [+- 1,1e-16], F_2 in [+- 3,7e-16] |
| Positivitaet | L_p = 7,31658935546875, danach |f| < thr mit thr >= 0,36984 |

Lauf B2 (L = 40, 320 bit, c-Radius mal 2^17), soweit abweichend: delta ~ 1,75e-21; 9,03e-10; 4,51e-21; 2,23e-21;
eps_1..4 <= 1,384e-17; 1,406e-17; 1,381e-23; 4,608e-23; K_J <= 1,08691; Zeilensumme <= 1,877e-3; Innenabstand
>= 0,8731 delta; L_p = 7,7659912109375; 445 / 472 Schritte. Der B2-Kasten liegt im A-Kasten (Grenzen verglichen).

**Warum B scheiterte (vorab gewaehlte Parameter). Berichtigt nach der Lesung (Befund A1, ab 13:15); die erste Fassung
nannte die l = 1-Zeilen 3 und 4 als Ursache, das war falsch.**
- Bei 320 bit und N = 72 ist H_0(z0) sehr genau bekannt (Breite von H_0,1 <= 2,3e-18). Der Kastenfaktor 8 auf
  |Y H_0(z0)| + |Y| eps gab delta_c = 6,9e-15, bei delta_a = 1,75e-21 und delta_om = 2,23e-21.
- Die c-Zeile von |I - Y D| hat in den Spalten a und om die Radien 7,54e7 und 7,07e7. Sie entstehen fast ganz aus den
  **Profilzeilen** H_0,1/2, nicht aus den l = 1-Zeilen 3 und 4. Nachgerechnet mit jq aus export.Y und export.DH0_Z von
  ZERT-T2-B-L40.json (Werte in double):
  - Die c-Zeile von Y ist (-0,4748; 1,0091; -149,0; 32,51).
  - Die Profilzeilen von D haben in Spalte a die Radien 3,97e7 und 5,60e7, relativ 4,0e-10 und 1,2e-9. Das ergibt
    0,4748 * 3,97e7 + 1,0091 * 5,60e7 = 7,54e7.
  - Die Zeilen 3 und 4 haben in Spalte a die Radien 1,23e-3 und 4,09e-3. Sie tragen nur
    149,0 * 1,23e-3 + 32,51 * 4,09e-3 = 0,32 bei.
  - Spalte om: 0,4748 * 4,25e7 + 1,0091 * 5,01e7 = 7,07e7; die Zeilen 3 und 4 geben 0,25.
- Gewichtet: 7,54e7 * 1,75e-21 / 6,89e-15 = 19,1 plus 7,07e7 * 2,23e-21 / 6,89e-15 = 22,9, zusammen 42,0 > 1
  (protokoll.zeilensumme_gewichtet 41,9986).
- **Beleg: Auch M1 scheiterte in T2-B**, das reine 2x2-Profilproblem in (a, c) ohne die Zeilen 3 und 4, mit
  Zeilensumme 19,10 (M1.rowsum, M1.BESTANDEN = false). Das stand bisher nur in STAND.md. In B2 ist M1.rowsum =
  1,457e-4 = 19,10 / 2^17.
- Der Mechanismus ist derselbe wie bei l = 0: Bei 320 bit wird delta_c sehr klein, die absoluten Breiten der
  Profilzeilen schrumpfen nicht im gleichen Mass. T1-B lag schon nahe an derselben Grenze (Zeilensumme 0,0845, davon
  0,0342 aus dem Profilblock, M1.rowsum).
- Der Kasten war in c zu schmal. Der Fehlschlag erklaert sich damit vollstaendig ohne einen Fehler in Code oder Lemma
  (42,0 = 19,1 + 22,9 aus den Profilzeilen, M1 scheitert mit 19,10, B2 besteht allein mit delta_c mal 2^17). Einen
  allgemeinen Ausschluss von Fehlern gibt das nicht her; es gibt kein zweites Programm (berichtigt nach L5).
- B2 vergroessert nur delta_c exakt um 2^17. Lemma K gilt fuer jeden Kasten (Z bleibt ein konvexer dyadischer Quader
  um z0; DH_0, eps und alle Bedingungen werden ueber genau dieses Z neu ausgewertet). B2 ist ein **adaptiv nach dem
  Fehlschlag gewaehlter Kasten**, keine vorab festgelegte oder urspruenglich bestandene Wiederholung und kein
  unabhaengiger Code. Die Wahl ist in STAND.md mit Stempel 12:36:54 vermerkt, einem Selbststempel (siehe 6).
- **Die l = 1-Breite** (Zeilen 3 und 4 von D, Spalte a, relativ 1,3e-3 bis 1,6e-3; in B mit 1,64e-3 und 1,54e-3 sogar
  groesser als in A mit 1,34e-3 und 1,26e-3, obwohl delta_a in B zwoelfmal kleiner ist; berichtigt nach L5)
  hat mit dem Scheitern von B nichts zu tun. In T2-A und B2 bestimmt sie die groesste Zeilensumme, und zwar ueber die
  a-Zeile: Deren Y-Eintraege fuer die Zeilen 3 und 4 sind (-0,443; 0,0967).
  - T2-A: 7,70e-4 + 6,02e-4 * (2,702e-20 / 2,111e-20) = 1,540e-3.
  - B2: 9,38e-4 + 7,34e-4 * 1,2785 = 1,877e-3.
  - Das ist weit unter 1. Fuer die Strenge ist die Breite harmlos: Eine zu breite Huelle erschwert den Test nur, und
    die Punkt-Jacobi-Matrix liegt in der Kastenhuelle.
- **Woher die l = 1-Breite kommt, ist offen** (Befund A5). Moegliche Ursachen:
  - Einwickeln in den vielen kleinen Schritten nahe r = 0, wo 2/r^2 gross ist.
  - Das Produkt f * phi_a in den Quellen: f ist im Kastenlauf bei L relativ 2872 (T2-A) breit.
    - Hinweis: Von A nach B aendert sich die relative Breite von f bei L in beiden Saetzen in dieselbe Richtung wie
      die D-Breite. T2: f 2872 -> 14558 bei D 1,34e-3 -> 1,64e-3; T1: f 26282 -> 9595 bei D fallend um den Faktor 29.
    - Kandidat 2 ist damit nicht widerlegt; ob er die l = 1-Breite erklaert, bleibt offen. (Berichtigt nach der
      Nachpruefung, R1; die Fassung von 19:49 zog hier einen zu starken Schluss.)
  - Beides ist ungeprueft. Vor weiteren Laeufen mit l >= 1 oder groesserem L klaeren, etwa mit Breiten je Schritt
    oder einem Kastenlauf mit kleinerem delta_a.

### 4.6 Empfindlichkeitskontrolle T2 (nicht streng)

| Lauf | rho + delta/4 | rho + delta | rho + 4 delta | Vorab erwartet |
|---|---|---|---|---|
| T2-A | besteht | verfehlt | verfehlt | so erwartet (4.8 im Plan) |
| T2-B | verfehlt (c) | verfehlt (c) | verfehlt (c, rho) | Lauf insgesamt gescheitert |
| T2-B2 | besteht | besteht | verfehlt | Vorab 12:36:54: delta/4 besteht, 4 delta verfehlt, delta offen; so eingetreten |

### 4.7 Reihenfolge Vorab gegen Ergebnis (mtime und Logzeiten)

- **Vorab-Zeilen (Uhrzeit per date im Text):**
  - T1: 12:11:22, vor Startwert (10:12:13 UTC) und Newton (10:12:20 UTC).
  - T2: 12:22:22, vor Startwert und Newton (10:24:10 UTC).
  - B2: 12:36:54 in STAND.md, vor Lauf B2 (10:37:00 UTC).
- **Frei-Test l = 1:** Um 12:21:45 in die Warteschlange gestellt, also vor Abschnitt 4 des Plans (12:22:22). Er lief
  wegen des Locks erst 12:23:00 bis 12:23:04 (Logzeile start 12:21:50 ist die Wartezeit vor flock, Laufzeit 3,4 s),
  also nach Abschnitt 4. Er ist eine Kontrolle, kein Beweislauf.
- **mtime:** Die Datei BEWEIS-2-PLAN.md wurde danach noch ergaenzt (Abschnitt 5), ihre mtime belegt die Reihenfolge
  deshalb nicht allein. Massgeblich sind die gestempelten Zeilen und die Logzeiten.

## 5. Unterschiede zu BEWEIS-1 (Code und Lemma)

Zeilennummern der Enddateien in zertifikat/ (aus `diff`, 12:27, fuer pruef-l1.py nach der letzten Aenderung 12:40 erneuert).

### 5.1 T1: pruef-v2.py (BEWEIS-1) -> pruef-l0.py; Kern bewkern.py byte-gleich (a8a7ec6f...)

| pruef-l0.py Zeilen | Aenderung | Grund / Lemma |
|---|---|---|
| 1-3 | Kopfkommentar | - |
| 134 | tail_E gibt zusaetzlich die Untergrenzen von phibar und eta aus | Fremdlesung Auflage 4 (Lemma P, Tabelle) |
| 226-227, 257, 261 | Optionen --w2, --rho; Modus start liest sie statt fester Werte | Startwerte T1 |
| 268-269 | Quellenvermerk in z_start.json | - |
| 413-414 | sha256-Schluessel = wirkliche Dateinamen | Auflage L6 aus BEWEIS-1 |
| 490-494 | Gesamtflag enthaelt 2 kappa0 > kappa_c, rho > omega, 4 - 6 kappa0^2 > 0 | Fremdlesung Auflage 1 (Lemma E); Korollar Krein; Lemma Pos |
| 570-571 | protokoll.lemma_P_untergrenzen | Fremdlesung Auflage 4 |
| 601-618 | export: Y, DH_0(Z), Mk, H_0(z0), eps, delta, Kr exakt (Mantisse, Exponent) | Fremdlesung Auflage 4 |

Kein Lemma aendert sich fuer T1; die Zahlen haengen nur ueber die geprueften Bedingungen von (omega, rho) ab.

### 5.2 T2: bewkern.py -> bewkern_l1.py

| bewkern_l1.py Zeilen | Aenderung | Lemma |
|---|---|---|
| 1-7 | Kopfkommentar mit Liste der l1-Aenderungen | - |
| 63, 65-66 | Par(..., l): l und cent = l(l+1) | 4.1 |
| 177, 185-192 | lin_M_series(..., w): cent (w*w)_n in P und Q, Fehler bei fehlendem w | T-l1 (4.3) |
| 283-356 | neu: lin_series0_l1 (Reihe (n+2)(n+5) y_{n+2} = F_n mit Jet-Quellen) und voc_aus_alpha (Umrechnung bei h0) | T0-l1 (4.2) |
| 380, 385-391 | M_complex(..., WD): cent WD^2 in P und Q | T-l1 (4.3) |
| 498-528 | apriori: erster Schritt fuer l = 1 in Integralform alpha(0) + (Dt^2/10) F, (Dt/5) F; sonst M_complex mit WD | T0-l1, T-l1 |
| 597-599, 617-622, 625-628, 633-634 | step: erster Schritt l = 1 ueber lin_series0_l1 und Umrechnung; lin_M_series mit w fuer r_j > 0 | T0-l1, T-l1 |
| 651-657 | initial_state: l = 1: alpha(0) = 1 (R_1), beta(0) = 1 (R_2) | T0-l1 |

Fuer l = 0 fuehrt bewkern_l1.py dieselben Operationen aus wie bewkern.py (alle Zusaetze haengen an par.l). T1 wurde
trotzdem mit dem unveraenderten bewkern.py gerechnet.

### 5.3 T2: pruef-l0.py -> pruef-l1.py

| pruef-l1.py Zeilen | Aenderung | Lemma |
|---|---|---|
| 1-6 | Kopfkommentar | - |
| 19, 21 | import bewkern_l1, ELL = 1 | - |
| 68 | evalH: Par mit l = 1 | - |
| 74-76, 79-80 | H_0,3/4 = s3 (j0 B_i' + j1 B_i), j0 = 1 + 1/(kc L), j1 = kc + 1/L + 1/(kc L^2) | W-l1 (4.5), J-l1 (J_0) |
| 87-90, 96-99 | DH_0 Zeilen 3, 4 mit d j0/d kc = -1/(kc^2 L), d j1/d kc = 1 - 1/(kc L)^2 | Zusatz J |
| 125-126, 130-141 | tail_E: Kernschranken a1, a2, b0, b1, b2, mu = max(a1, b1), eps = b0 (e^{mu Q} - 1)/mu, E_A.. E_B' | J-l1 (4.4) |
| 156-158 | K_J = b0 + E_A + E_B, Konstanten und Lemma_J_l1_ok im Protokoll | J-l1 |
| 250 | Option --dcexp (c-Kastenradius exakt mal 2^dcexp; nur Lauf T2-B2) | K (Kastenwahl) |
| 256-261, 270-290 | Frei-Test l = 1 mit R_1 = 3 j(kr)/k^2, R_2 = 3 i(kc r)/kc^2 | T0-l1, T-l1 |
| 448-449, 489-493 | dcexp im Parameterblock; delta_c mal 2^dcexp | K |
| 537-540 | Gesamtflag enthaelt k L >= 1, kc L >= 1, 0 < h < R in jedem Schritt, N >= 1, qfac > 1 | J-l1, T (Hinweis der Fremdlesung) |
| 623-625 | protokoll.lemma_J mit den l1-Konstanten | - |
| 690, 698, 705 | Kontrollmodus: Par mit l = 1, Reihe mit w, Huelle mit WD | Kontrolle |

### 5.4 Lemmata: was sich fuer l = 1 aendert (Wortlaut in BEWEIS-2-PLAN.md 4)

| Lemma BEWEIS-1 | T2 |
|---|---|
| T0 (Start, Gewicht 2/r, Faktor (n+2)(n+3)) | T0-l1: alpha = A/r^2, beta = B/r^2, Gewicht 4/r, Integralgewichte 1/10 und 1/5, Faktor (n+2)(n+5); Umrechnung bei h0 |
| T (Taylor-Schritt, R < r_j) | T-l1: zusaetzlich 2/r^2 in P, Q; dieselbe Pruefung R < r_j |
| J (Kerne sin, e^{-kappa_c}) | J-l1: Riccati-Kerne, Konstanten a1, a2, b0, b1, b2; J_0 mit 1 + 1/(kc L) und -(kc + 1/L + 1/(kc L^2)); braucht k L, kc L >= 1 |
| W (W(Psi, R_i) = Psi_i(0)) | W-l1: W(Psi, R_i) = Koeffizient der singulaeren Loesung r^{-1}; Nullstelle von H = Regularitaet bei 0 |
| E (Wronski-Komplement) | E-l1: gleich mit j, y; geometrische Vielfachheit 1 je (1, m); Translationsmode bei rho = 0 stoert nicht |
| R (Regularitaet) | R-l1: alpha, beta gerade analytisch, a Y_1m = alpha(|x|) (r Y_1m) glatt |
| P, Pos, K, Zusatz S, Zusatz J | unveraendert (Profil l = 0; Krawczyk; Stetigkeit; Jets) |

## 6. Luecken und Vorbehalte

1. **Gelesen in zwei Haeusern** (Anthropic: LESUNG-BEWEIS-2.md; OpenAI: resonance-20260930/beweis2-fremdlesung/),
   Urteile: Anthropic T1 und T2 "traegt mit Auflagen", OpenAI T1 "traegt", T2 "traegt mit Auflagen"; nichts
   blockierend; Einarbeitung in Abschnitt 8. Lemma T0-l1 und J-l1 wurden dort
   nachgerechnet und gegen den Code gelesen. Der Frei-Test l = 1 und die Kontrollen pruefen die Umsetzung, nicht die
   Lemmata.
2. **Softwarevertrauen:** python-flint 0.9.0 / FLINT, dieselben Bibliotheken wie BEWEIS-1 (Hashes in 7).
3. **Kein zweites unabhaengiges Programm.** Beide Lesungen von BEWEIS-2 haben keine ODE-, H_0-, DH_0- oder
   Krawczyk-Nachrechnung gemacht. Die exakten Exporte machen die Krawczyk-Algebra nachpruefbar, ersetzen aber nicht
   die Pruefung ihrer ODE-Herkunft. Offen.
4. Eindeutigkeit von (rho*, omega*) in Z nicht gezeigt; Eindeutigkeit des Profils unter allen positiven radialen
   Loesungen [L?].
5. **Reichweite:**
   - Einfachheit heisst geometrische Vielfachheit 1 je radialem Winkelkanal.
   - Das dreifache l = 1-Multiplett (m = -1, 0, 1) bleibt bestehen.
   - Keine algebraische Einfachheit, keine Jordan-Freiheit, keine lineare oder nichtlineare Stabilitaet.
   - Eingebettet heisst operational. Es gibt keine Aussage zur Realisierung des vollen Bueschels und zu dessen
     wesentlichem Spektrum.
   - Die Leiteretiketten n = 1, n = 2 sind die Zuordnung aus dem Datenpaket, keine zertifizierte Knotenzahl. Aus einem
     Etikett folgt nichts ueber die Vollstaendigkeit der Leiter.
   - Das Krein-Korollar benutzt die Formel aus KREIN-1 und ist kein Stabilitaetssatz.
6. **T2-B scheiterte** mit den vorab gewaehlten Parametern (Kasten in c zu schmal, Profilblock, siehe 4.5).
   - B2 ist ein nach dem Fehlschlag adaptiv gewaehlter Kasten. Das aendert an der Strenge nichts (Lemma K gilt fuer
     jeden Kasten).
   - Die Forderung "zwei Zertifizierungen je Ziel" ist fuer T2 nur nachtraeglich erfuellt; T2 stuetzt sich allein auf
     T2-A.
   - Die Schrittprotokolle von B und B2 sind bitgleich, weil c nicht in die Integration eingeht.
7. **Empfindlichkeitskontrolle:** In T1-B und T2-B2 besteht auch die Verschiebung um delta.
   - Kr liegt dort nicht um z0, sondern um die Nullstelle, etwa 0,11 delta daneben.
   - Die Kontrolle ist nicht streng und in dieser Form nur aussagekraeftig, wenn der Kr-Radius den Newton-Abstand
     ueberwiegt.
   - Die Negativkontrolle des Auftrags (delta/4 besteht, 4 delta verfehlt) erfuellen alle Laeufe ausser dem
     gescheiterten T2-B. Verfehlt wurde nur meine strengere Zusatzerwartung "delta verfehlt" (T1-B).
8. **Codefassungen und Vorab-Stempel:**
   - Die Newton-Laeufe (nicht streng) liefen mit Vorfassungen der Treiber, die nicht beiliegen. "Unterschied nur in
     zert()" ist deshalb nicht pruefbar; fuer die Strenge ohne Belang.
   - Die Beweislaeufe tragen die sha256 der jeweils laufenden Fassung. Die Fassung von T2-A und T2-B liegt als
     pruef-l1-c1f85f81.py bei.
   - Die vollstaendige Zeilenliste stand nicht vor jedem Beweislauf im Plan (BEWEIS-2-PLAN.md 5.1).
   - Die Vorab-Stempel (12:11:22, 12:22:22, 12:36:54) sind **nur Selbststempel**. Plan und STAND haben mtimes nach
     allen Ergebnisdateien; die Pflicht "vorab heisst: vor der Ergebnisdatei, mtime pruefen" ist damit nicht erfuellt.
   - Fuer kuenftige Beweise (Befund A4): den Planstand vor jedem Beweislauf per sha256 einfrieren, etwa als
     STAND-Zeile mit Plan-Hash vor dem Lauf oder als gestempelte Kopie.
9. **Die l = 1-Breite** der D-Zeilen H_0,3/4 (Spalte a, relativ 1,3e-3 bis 1,6e-3; sie schrumpft nicht mit dem Kasten,
   in B ist sie sogar groesser als in A) ist in ihrer
   Herkunft offen (Befund A5). Sie stoert den Beweis nicht und bestimmt in A und B2 die groesste Zeilensumme
   (<= 1,9e-3). Bei laengerem L oder hoeherem l kann sie begrenzen; vor solchen Laeufen klaeren.
10. **Code-Hinweise der Fremdlesung** (ohne Codeaenderung, wegen der Hashkette):
    - bewkern_l1.py prueft nicht, dass l in {0, 1} liegt ("if par.l" setzt l = 1 voraus). Bei einer Erweiterung auf
      l >= 2 ist eine Bereichspruefung noetig.
    - Die uebernommenen Kommentare "A'(0) = 1" gelten nur fuer den l = 0-Zweig.
    - Die Logkopfzeile "L 40" in LAUF-t2-zertA-L36.log und LAUF-t2-kontrolle.log gibt args.L aus; benutzt wird
      L = 36 aus z0-t2.json. Das ist ohne Wirkung.

## 7. Dateien (zertifikat/, 37 Dateien in SHA256SUMS.txt; lokal und auf der .69 gleich, sha256sum -c 12:41:38)

- **Code:**
  - bewkern.py a8a7ec6ff96792265bd7ac8cca1504ea7c46f9e10e6d60f655c7d2e07717219d (= BEWEIS-1, fuer T1)
  - bewkern_l1.py 24b3dc8d91180459e765b260af79f83b14f47716cb48cd90378d709687b79841 (T2)
  - pruef-l0.py 7713f6367b82110f54a3847c49c6abafc3e6e869ccff3b18a3326af329a02a3e (T1-A, T1-B)
  - pruef-l1-c1f85f81.py c1f85f817147901a489c298a9157a1df72edb1ef3f7b3e5317f58493832d7bf4 (T2-A, T2-B; im JSON unter dem
    Namen pruef-l1.py)
  - pruef-l1.py eecfb3cddd92e17906eb321b127b74c6b98a959536c8f4a62e936584e24ab69a (Endfassung, T2-B2; dazu nur --dcexp)
- **Startpunkte:** z0-t1.json 24953077...c430c, z0-t2.json 1ec05051...96df3 (dazu z_start-t1/t2.json, float).
- **Zertifikate:**
  - ZERT-T1-A-L32.json 97e13cb196318114d4ad1dba5311ad52a4881aaa14ef38ed66d98fe02d065177 (T1 massgeblich)
  - ZERT-T1-B-L36.json 3248483821e68366d359a0043194467338c1e36ca6e906d7b36ed06bdf9b3cd3
  - ZERT-T2-A-L36.json 764ef9e992a9a89d346f5af42839607948ed017b6322201c4850d785129dc399 (T2 massgeblich)
  - ZERT-T2-B-L40.json 7485eaa2aa123807f61377cd29531458bbf81238e40476234cfba8dc58a6cedd (gescheitert)
  - ZERT-T2-B2-L40.json 533e64bb03f60feee924e9fe765a79a1b97c9d95de3f9c15c26a7a4c94fd3d8d
  - Dazu je Lauf *-SCHRITTE-KASTEN.json und *-SCHRITTE-PUNKT.json. Die Zertifikate enthalten parameter,
    Kommandozeile, sha256 von Code, z0, Interpreter und FLINT-Bibliotheken, protokoll und export.
- **Logs:**
  - LAUF-t1-start, -newton, -zertA-L32, -zertB-L36, -satzA
  - LAUF-t2-frei, -start, -newton, -zertA-L36, -zertB-L40, -zertB2-L40, -kontrolle, -satzA
- **Software:** Python 3.12.3 (e50d468e...), pyflint.abi3.so 1f7ef1f5..., libflint 871a4132..., libgmp 33d24e67...,
  libmpfr c4dfcfc7... (gleich BEWEIS-1).
- **Nachrechnen** auf der .69 im Ordner /home/fmh/fmhc-physics-remote/runde10-beweis2/ ueber kleintest.sh, Spur cpu5:
  - `pruef-l0.py zert --z z0-t1.json --N 64 --Nbox 48 --q 3 --kfak 8 --out ZERT-T1-A-L32.json`
  - `pruef-l1.py zert --z z0-t2.json --N 64 --Nbox 48 --q 3 --kfak 8 --out ZERT-T2-A-L36.json`
  - B-Laeufe mit `--Lz 36|40 --prec 320 --N 72 --Nbox 44 --q 4`, B2 zusaetzlich `--dcexp 17`.
  - **Reproduktion mit den historischen Hashes** (Auflage A3 der Fremdlesung): Fuer T2-A und T2-B die archivierte
    Fassung pruef-l1-c1f85f81.py in einem eigenen Ordner unter dem damaligen Namen pruef-l1.py ablegen (neben
    bewkern_l1.py und z0-t2.json). Nur dann steht im neuen JSON derselbe Treiber-Hash c1f85f81.... Die Endfassung
    pruef-l1.py ohne --dcexp rechnet denselben Weg, traegt aber einen anderen Hash (eecfb3cd...).

## 8. Einarbeitung der Lesungen (ab 2026-09-30 13:13:45 CEST, date; nur Text)

- Quellen: LESUNG-BEWEIS-2.md (Haus Anthropic, frischer Leser, 12:45:34 bis 13:12:08, Befunde F1 bis F9, Auflagen A1
  bis A6) und resonance-20260930/beweis2-fremdlesung/ (Haus OpenAI: GESAMT-REVIEW.txt mit ORIGIN-L1.txt, TAIL-L1.txt,
  CERTIFICATES.txt; Auflagen A1 bis A4 und ein Codehinweis). Urteile: Anthropic T1 und T2 traegt mit Auflagen; OpenAI
  T1 traegt, T2 traegt mit Auflagen; nichts blockierend,
  keine Neuberechnung noetig.
- Kein neuer Lauf, keine Aenderung an zertifikat/ (sha256sum -c am Ende, siehe STAND.md). Alte Fassungen gesichert als
  BEWEIS-2.md.bak-20260930-1313, BEWEIS-2-PLAN.md.bak-20260930-1313, STAND.md.bak-20260930-1313.

| Befund | Stelle | Aenderung |
|---|---|---|
| Anthropic A1 / F1, F2: Ursache des Scheiterns von T2-B falsch; M1-Fehlschlag nicht genannt | 4.5 "Warum B scheiterte"; STAND.md | Berichtigt: Die c-Zeile kommt aus den Profilzeilen H_0,1/2 (0,4748 * 3,97e7 + 1,0091 * 5,60e7 = 7,54e7), die l = 1-Zeilen geben nur 0,32. M1 scheiterte ebenso (19,10). Die Zahlen habe ich mit jq aus export.Y, export.DH0_Z, export.Mk, M1 selbst nachgeprueft. Die l = 1-Breite ist der a-Zeile in A und B2 zugeordnet. STAND.md hat eine neue Berichtigungszeile, die alte bleibt stehen. |
| Anthropic A2 / F6: z0_rho falsch abgeschrieben | 4.3 | Jetzt 1,690356597328143456827258717... (Mitte der Z-Grenzen), Abstand 0,108 delta statt "etwa 0,10". |
| Anthropic A3 / F7: "alle Voraussetzungen im Gesamtflag" fuer T1 zu weit; R < r_j in keinem Flag | 3 (T1 und T2), 4.5 Schrittzeile | T1: 0 < h < R, N >= 1, qfac > 1 nachtraeglich aus den Schrittprotokollen geprueft; R < r_j durch Abbruch erzwungen (T1 und T2). Ueberholt durch L2, L3 (unten): N, qfac stehen in parameter, R < r_j gilt fuer r_j > 0, ein Verstoss verwirft nur den Schrittversuch. |
| Anthropic A4 / F3, F4: Vorab-Stempel nur Selbststempel; Plan nicht vor jedem Lauf eingefroren | 6 Punkt 8 | Offen gesagt; fuer kuenftige Beweise Plan-Hash vor jedem Beweislauf in STAND.md oder gestempelte Kopie. |
| Anthropic A5 / F8: Herkunft der l = 1-Breite | 4.5, 6 Punkt 9 | Als offene Frage gefuehrt, mit zwei ungeprueften Kandidaten; vor Laeufen mit l >= 1 oder groesserem L klaeren. |
| Anthropic A6 / F9 (optional): "BIC = regulaer bei 0"; "a- und omega-Spalte bis 1,6e-3"; T1-rho-Obergrenze eine Einheit zu grosszuegig; Logkopf "L 40" | 5.4, 4.5, 1, 6 Punkt 10; Plan 4.5 | "Nullstelle von H = Regularitaet bei 0"; Spaltenangabe in der neuen 4.5 genau (Spalte a relativ 1,3e-3 bis 1,6e-3); Obergrenze jetzt ...846998028; Logkopf als wirkungslos vermerkt (Log bleibt unveraendert). |
| Anthropic F5: B2 nicht vorab festgelegt | Ergebnis, 4.5, 6 Punkt 6 | Deutlicher: T2 stuetzt sich allein auf T2-A; "zwei Zertifizierungen je Ziel" fuer T2 nur nachtraeglich. |
| OpenAI A1: Winkelharmonik-Basis | Satz T2 Punkt 4; Plan 4.1 | Y_1m als reelle orthonormale Basis definiert; fuer komplexe Y_lm traegt das zweite Seitenband Y_lm*, mit Begruendung im Plan. |
| OpenAI A2: Ableitungskern | Plan 4.4 | K_B' := (d_r - kc) K_B = e^{kc r} (d_r G_B) e^{-kc s} erklaert; Schranke b2 und Code unveraendert (der Codekommentar in pruef-l1.py bleibt wegen der Hashkette). |
| OpenAI A3: Reproduktion mit historischem Hash | 7 Nachrechnen | Anleitung: pruef-l1-c1f85f81.py unter dem Namen pruef-l1.py in eigenem Ordner verwenden. |
| OpenAI A4: n-Etiketten; Krein-Korollar | Ergebnis, Saetze T1 und T2 Punkt 5, 6 Punkt 5 | n als Leiterzuordnung, keine zertifizierte Knotenzahl; Krein-Korollar nutzt die Formel aus KREIN-1, kein Stabilitaetssatz. |
| OpenAI Grenzen wie gelesen | 6 Punkt 5 | Geometrische radiale Einfachheit je Winkelkanal, dreifaches l = 1-Multiplett, keine algebraische Einfachheit, keine Stabilitaet, eingebettet nur operational. |
| OpenAI Codehinweis: Bereichspruefung l, alte Kommentare A'(0) = 1 | 6 Punkt 10 | Vermerkt, keine Codeaenderung (Hashkette). |
| (eigene Aenderung 13:15, nachgetragen nach L4) Abschnitt Ergebnis | Ergebnis | Die Lesungen sind genannt; B2 ist als adaptiv gewaehlter Kasten gekennzeichnet; T2 stuetzt sich allein auf T2-A; n ist Leiteretikett; der Satz "noch nicht gegengelesen" ist ersetzt. |
| (eigene Aenderung 13:15, nachgetragen nach L4) Einfach gesagt | Einfach gesagt | Um 13:15 kam der Satz ueber die Lesungen hinzu ("nur Beschreibungsfehler gefunden, die jetzt berichtigt sind"). Er ging zu weit und ist ab 19:49 ersetzt, siehe L4. |

**Lesung der letzten Schicht** (LESUNG-LETZTE-SCHICHT-BEWEIS-2.md, frischer Leser, Haus Anthropic, 19:35:19 bis
19:48:21). Urteil: traegt mit Auflagen, nichts blockierend, 58 von 58 neuen oder geaenderten Zahlen richtig.
Eingearbeitet ab 2026-09-30 19:49:12 CEST, nur Text; alte Fassungen als *.bak-20260930-1949.

| Befund | Stelle | Aenderung |
|---|---|---|
| L1 (Befund 1; OpenAI A4 war nur teilweise umgesetzt): Ordnungswoerter und Knotenaussage | Ueberschriften 1 und 2; Einfach gesagt; Plan 2 | "Leiteretikett n = 2" bzw. "Leiteretikett n = 1, Schwapp-Leiter" statt "erste Schwapp-Stelle"; Einfach gesagt: "eine weitere Atmungsschwingung und eine Schwappschwingung", Nummern ausdruecklich keine gezaehlte Reihenfolge; Plan: "n = 2 ist das Leiteretikett ..., keine zertifizierte Knotenzahl" statt "hat mehr Knoten". Damit ist OpenAI A4 vollstaendig umgesetzt. |
| L2 (Befund 2): "R < r_j in allen Schritten" zu weit; "in keinem Flag" ungenau | 3 (T1, T2 Punkt 4); 4.2 und 4.5 Schrittzeilen | Auf Schritte mit r_j > 0 beschraenkt (der erste Schritt bei r_j = 0 ist die Reihe um 0); Protokollwert R_kleiner_rj_alle genannt, nur nicht in M3.BESTANDEN. |
| L3 (Befunde 3, 4): Quelle fuer N, qfac; Mechanismus bei R >= r_j | 3 (T1, T2 Punkt 4); 4.5 Schrittzeile | N >= 1 und qfac > 1 aus parameter und kommandozeile; bei R >= r_j wird der Schrittversuch verworfen und R verkleinert, erst bei R < 1/1000 bricht der Lauf ab; R <= r_j/2 schon durch die Schrittwahl. |
| L4 (Befund 5): Einfach gesagt zu weit, "linear" fehlte | Einfach gesagt; diese Tabelle; STAND.md | Neu gefasst: "im linearen Modell" ergaenzt, offene Punkte (zweites Programm, l = 1-Breite, Plan-Einfrieren) ausdruecklich als offen genannt statt "berichtigt". Die Aenderungen von 13:15 an Ergebnis und Einfach gesagt sind oben nachgetragen. |
| L5 (Befunde 6, 7, 8, optional) | 4.5; 6 Punkt 9; Ergebnis, 6 Punkt 1, 8 | Richtung der l = 1-Breite berichtigt (in B groesser als in A); "Ein Fehler in Code oder Lemma liegt nicht vor" auf "erklaert sich ohne Fehler; kein allgemeiner Ausschluss" begrenzt; OpenAI-Urteil je Satz zitiert (T1 traegt, T2 traegt mit Auflagen). |
| Hinweis (Befund 9, keine Auflage): Gegenfall zu Kandidat 2 | 4.5 | Aufgenommen: Bei T1-A ist f bei L noch breiter (26282), die l = 0-D-Breite schrumpft trotzdem um den Faktor 29; ein breites f allein erklaert die l = 1-Breite nicht. |
| Nachpruefung 19:49 (NACHPRUEFUNG-1949-BEWEIS-2.md), R1 und R2 sowie Punkt 4, ab 20:00:13 | 4.5; Einfach gesagt; 3 (T1) | R1: Befund-9-Zeile in 4.5 als Hinweis statt Schluss (f und D-Breite aendern sich von A nach B in beiden Saetzen gleichsinnig, Kandidat 2 nicht widerlegt); die Zeile oben (Hinweis Befund 9) ist damit ueberholt. R2: Einfach gesagt nennt den OpenAI-Codehinweis als offen und schraenkt "berichtigt" auf den Text ein. Punkt 4: "Datenpaket" statt "Datensammlung"; kommandozeile als Unterfeld von parameter. |

Offen nach der Einarbeitung:
- ein zweites unabhaengiges Programm
- die Herkunft der l = 1-Breite
- ein Plan-Einfrieren per Hash, erst fuer kuenftige Beweise

## Einfach gesagt

Ein Q-Ball kann in besonderen Faellen schwingen, ohne Wellen nach aussen abzugeben, jedenfalls in der vereinfachten
linearen Rechnung (kleine Schwingungen). Nach BEWEIS-1 sind jetzt zwei weitere solche Schwingungen mit derselben
garantierten Rechenweise im linearen Modell bewiesen: eine weitere Atmungsschwingung und eine Schwappschwingung, bei der
der Ball hin und her kippt. Ihre Nummern stammen aus dem Datenpaket und sind keine gezaehlte Reihenfolge. Fuer das
Schwappen musste der Rechenkern neu lernen, wie die Schwingung am Ballmittelpunkt anfaengt und wie sie weit draussen
auslaeuft; ein Test ohne Ball hat das auf 37 Stellen bestaetigt. Ein Wiederholungslauf scheiterte zuerst, weil ein
Suchkasten zu eng gewaehlt war, und bestand mit einem weiteren Kasten. Leser aus zwei Haeusern haben Rechenweg und
Programm geprueft; die gefundenen Beschreibungsfehler sind im Text berichtigt, die veralteten Kommentare im
Programmcode bleiben wegen der Pruefsummen der Rechnung stehen. Offen bleiben ein zweites, unabhaengiges Programm, die
Herkunft einer auffaelligen Rechenbreite beim Schwappen, ein nachpruefbares Festschreiben des Plans vor jedem Lauf und
zwei Hinweise zum Programmcode (eine Pruefung des erlaubten Drehimpulses l und die veralteten Kommentare zu
A'(0) = 1), die ohne Codeaenderung bleiben, damit die Pruefsummen gueltig bleiben.
