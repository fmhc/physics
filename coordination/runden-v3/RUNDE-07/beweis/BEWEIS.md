# BEWEIS-1 (M4): Strahlungsfreie Atmungsmode des 3D-Q-Balls im linearen Modell

- Autor: Beweis-Agent (Claude, Haus Anthropic). Auftrag: RUNDE-07/beweis/BRIEF.md. Plan und Lemmata:
  BEWEIS-PLAN.md (mit Einarbeitung der Lesung LESUNG-PLAN.md). Zeitverlauf: STAND.md.
- Beginn 2026-09-30 05:35:09 CEST, dieser Text ab 07:04:51 CEST (date). Nach der Code-Lesung LESUNG-CODE.md
  ueberarbeitet ab 08:04:40 CEST (date); Einarbeitung: Abschnitt 7.

## Ergebnis

**Bewiesen (rechnergestuetzt, im linearen Modell, Sektor l = 0).** Die Kette ist vollstaendig streng:
- analytische Schwanzlemmata mit Beweis im Text (Lemma P, J),
- Kugelarithmetik mit 256 bzw. 320 bit fuer jeden Rechenschritt,
- strenge Cauchy-Restglieder fuer jeden Taylor-Schritt,
- Brouwer-Krawczyk-Test mit Stoerterm.

Stand der Pruefung und Vertrauensannahmen (Abschnitt 5):
- Code und Zertifikat wurden frisch gegengelesen (LESUNG-CODE.md, 30.09., Leser aus dem Haus Anthropic).
  Urteil: traegt mit Auflagen (Code-Lesung W1, K1-K8); alle eingearbeitet (Abschnitt 7). Es fehlen weiterhin eine Lesung aus
  einem fremden Haus und ein zweites unabhaengiges Programm.
- python-flint 0.9.0 / FLINT rechnet richtig (Vertrauensannahme).

## 1. Satz

Bezeichnungen: U(S) = S - S^2 + S^3/2, N(f) = (1 - omega^2) f - 2 f^3 + (3/2) f^5, V_pm = U'(S) + U''(S) S - (omega pm rho)^2
= 1 - 4S + (9/2) S^2 - (omega pm rho)^2, C = U''(S) S = -2S + 3S^2, S = f^2.

Z sei der Kasten z0 +- delta mit den exakten dyadischen Zahlen aus zertifikat/ZERT-A2-L40.json (Feld protokoll.Z; gleich in ZERT-A-L40.json).
In Dezimalform (die Grenzen sind exakte Dyadiken; die Dezimalstellen sind nach aussen gerundet):

| Groesse | untere Grenze | obere Grenze |
|---|---|---|
| a = f(0) | 1,024235506571665864903719568 | 1,024235506571665864903976115 |
| c | 7,518251887708654655 | 7,518253935068731844 |
| rho | 1,744617544837398735780754587 | 1,744617544837398735781671831 |
| omega | 0,893127531269675502073897354 | 0,893127531269675502074377802 |

Damit gilt omega^2 in [0,797676787111865191750 +- 4,8e-22] und rho in [1,744617544837398735781 +- 6,8e-22] (Kugelschreibweise, nach aussen gerundet).

**Satz.** Es gibt (a*, c*, rho*, omega*) in Z mit folgenden Eigenschaften.

1. **Profil.** Die Loesung f des Anfangswertproblems f'' + (2/r) f' = N(f), f(0) = a*, f'(0) = 0 (mit omega = omega*)
   existiert auf [0, oo), ist positiv, und r e^{kappa0 r} f(r) -> c* (kappa0 = sqrt(1 - omega*^2), in
   [0,44980352698498797815 +- 1,4e-21]). phi = e^{i omega* t} f(|x|) ist ein positiver radialer Q-Ball der NLKG
   phi_tt - Laplace phi + U'(|phi|^2) phi = 0. Ob es der einzige positive radiale ist, wird nicht behauptet [L?].
2. **Mode.** Das System A'' = V_+ A + C B, B'' = V_- B + C A (mit f, omega*, rho*) hat eine nichttriviale reelle Loesung
   Psi = (A, B) mit A(0) = B(0) = 0. Fuer r >= L = 40 gilt |A(r)| + |B(r)| <= K_J e^{-kappa_c r}
   (Normierung e^{kappa_c r} B(r) -> 1). Dabei ist K_J <= 1 + 7,57e-17 (protokoll.K_J_minus_1_obere_schranke) und kappa_c = sqrt(1 - (omega* - rho*)^2)
   in [0,52437081993036044928 +- 5,5e-21].
3. **Einfachheit.** Jede Loesung dieses Systems, die auf [L, oo) quadratintegrierbar ist, ist ein Vielfaches von Psi
   (Lemma E). Der Raum der L^2-Loesungen mit A(0) = B(0) = 0 ist also eindimensional.
4. **Folgerung.** a(x) = A(|x|)/|x| und b(x) = B(|x|)/|x| sind glatte, exponentiell abfallende radiale Funktionen (in
   jedem H^s(R^3)).
   - delta phi(t, x) = e^{i omega* t} (a(x) e^{i rho* t} + b(x) e^{-i rho* t}) loest die um phi linearisierte NLKG.
   - Im mitrotierenden Rahmen (Faktor e^{i omega* t} abgespalten) ist die Stoerung 2 pi/rho*-periodisch. delta phi
     selbst ist quasiperiodisch mit den Frequenzen omega* + rho* und omega* - rho*.
   - **Eingebettet** heisst hier operational: rho* liegt im Kontinuum des freien Bueschels (S = 0), denn
     (omega* + rho*)^2 - 1 = k^2 >= 5,9576. Der Kanal omega* + rho* ist offen, der Kanal omega* - rho* geschlossen
     (kappa_c^2 >= 0,27496).
   - Also 1 - omega* < rho* < 1 + omega*, mit Abstaenden >= 1,6377 nach unten und >= 0,14850 nach oben.
   - Es gibt eine nichttriviale L^2-Loesung ohne Abstrahlung: ein gebundener Zustand im Kontinuum der
     Linearisierung.

**Nicht behauptet:**
- Eindeutigkeit von (rho*, omega*) in Z und die Nichtexistenz weiterer Nullstellen in Z.
- Aussagen ueber das wesentliche Spektrum des vollen Bueschels (Weyl-Satz nicht an der Quelle geprueft).
- Aussagen fuer l > 0.
- Nichtlineare Strahlungsfreiheit. Codex zeigt Abstrahlung der endlichen Anregung in der zweiten Harmonischen,
  Fluss ~ epsilon^4 (bic-proof/). Der Satz ist ausdruecklich ein Satz ueber die lineare Gleichung.

Zweite Zertifizierung mit anderen Parametern (Lauf B2, Zahlen gleich B: L = 44, 320 bit, anderes Gitter, andere Ordnung;
derselbe Code, also kein zweites Programm) liefert einen noch
engeren Kasten im Innern von Z:
- rho in [1,744617544837398735781213 +- 3,9e-25],
- omega^2 in [0,797676787111865191750045 +- 6,5e-25],
- a in [1,024235506571665864903848 +- 4,1e-25].

## 2. Beweis (Struktur; Lemmata mit Beweisen in BEWEIS-PLAN.md, Abschnitt 4)

1. **Nullstellenproblem** (BEWEIS-PLAN 3). H(z) = H_0(z) + E(z) auf Z, z = (a, c, rho, omega).
   - H_0 besteht aus zwei Profil-Anschlussbedingungen bei L und zwei Wronski-Formen W(J_0, R_i) der regulaeren
     Loesungen mit den freien Jost-Daten J_0 = (0, 1, 0, -kappa_c).
   - E enthaelt die Schwanzkorrekturen.
   - H(z*) = 0 liefert: globales Profil (Anschluss in Wert und Ableitung), Jost-Loesung Psi mit
     W(Psi, R_i) = Psi_i(0) = 0 (Lemma W), also Psi(0) = 0.
2. **Schwanz** (Lemma P, Lemma J). Die Bedingungen gelten auf ganz Z, in Kugelarithmetik ueber Z geprueft
   (Tabelle 3.2). E ist stetig auf Z (Stetigkeitsbeweis ausgeschrieben in BEWEIS-PLAN, Lemma P/J, Zusatz S).
   |E_i| <= eps_i mit den Werten aus Tabelle 3.2.
3. **Vorwaertsintegration** (Lemma T0 am Ursprung, Lemma T fuer r > 0).
   - H_0(z0) wird streng eingeschlossen (Punktlauf).
   - DH_0 wird ueber ganz Z eingeschlossen (Kastenlauf mit den 38 gekoppelten Komponenten aus Profil,
     Profilvariationen, R_1, R_2 und deren Ableitungen nach a, rho, omega; Liste in BEWEIS-PLAN, Lemma T, Zusatz J).
   - Jeder Schritt prueft vorab R < r_j in Kugelarithmetik. Er gilt nur, wenn der Einschlusstest
     Y0 + Dt F(Dt, B) in B (acb_contains) wahr ist.
4. **Brouwer-Krawczyk** (Lemma K). Kr = z0 - Y H_0(z0) + (I - Y DH_0(Z))(Z - z0) + |Y| [-eps, eps] liegt in Z.
   - Innenabstand >= 0,87499 delta je Koordinate.
   - Invertierbarkeit: kastengewichtete Zeilensumme max_i sum_j |I - Y D|_ij delta_j / delta_i <= 5,7e-9 < 1 (Maximum exakter oberer Zeilenschranken).
     Die ungewichtete Zeilensumme ist <= 27253: Die Unbekannten sind sehr verschieden skaliert, darum gehoert die
     Gewichtung in Lemma K. Mit der Perron-Frobenius-Schranke folgt rho(|I - Y D|) < 1.
   - Also hat T(z) = z - Y H(z) einen Fixpunkt z* in Z, und H(z*) = 0.
5. **Positivitaet** (Lemma Pos): f > 0 auf [0; 7,0475] aus den A-priori-Huellen, danach bis L |f| < thr <= sqrt(S_-)
   mit thr >= 0,33208949 (Zertifikat, Feld schwelle; das ist die gepruefte Bedingung), tatsaechlich |f| <= 0,093
   (Schrittprotokoll A2) und Minimumprinzip; ab L nach Lemma P.
6. **Regularitaet, Abfall, Einfachheit, Kontinuum** (Lemma R, J, E; Kanalzahlen Tabelle 3.2). QED.

## 3. Zertifikat

### 3.1 Laeufe (alle auf der .69, Spur cpu5, ein Kern, ueber kleintest.sh; Zeiten gemessen)

| Lauf | Zweck | Parameter | Ergebnis | Laufzeit |
|---|---|---|---|---|
| newton3 | Startpunkt z0 (nicht streng) | L = 12, 20, 30, 40; N = 48; q = 1/3; 256 bit | quadratische Konvergenz, z0.json | 297 s |
| ZERT-A2-L40 | **Beweislauf** M1-M3 (massgeblich) | L = 40; Punkt N = 64, Kasten N = 48; q = h/R = 1/3; 256 bit; Faktor 8 | **bestanden** | 113,1 s |
| ZERT-B2-L44 | unabhaengige Wiederholung | L = 44; Punkt N = 72, Kasten N = 44; q = 1/4; 320 bit; Faktor 8 | **bestanden** | 123,2 s |
| kontr2 | T1 Konsistenz A-priori/Rekursion, T2 Differenzenquotienten | L = 40 | T1: Mittelpunkte gleich bis <= 3,5e-77 (M, Mp) bzw. exakt gleich (g', Y', Jets), Schranken <= 5,4e-8 allein aus den Radiensummen; T2 rel. <= 2e-14 | 95,9 s |
| frei3 | Frei-Test (f = 0, geschlossene Loesungen) | L = 40 | alle 25 Stellen gleich | 3,8 s |
| in A2 und B2 | Empfindlichkeitskontrolle: Kastenmitte rho + delta/4, + delta, + 4 delta (D, eps vom Originalkasten) | wie A2, B2 | delta/4 besteht, delta und 4 delta verfehlen (rho-Komponente); so vorab im Code festgelegt | in A2, B2 |

- A2 und B2 rechnen mit unveraendertem Kern (bewkern.py) und der Treiberfassung pruef-v2.py; sie tragen Laufparameter
  und sha256 im JSON. Alle mit A und B gemeinsamen Felder mit gleicher Ausgabegenauigkeit sind gleich (jq-Vergleich
  zwischen 08:14:21 und 08:15:49, u. a. delta, Kr, eps, M1, M2, Z, Kanaele, Innenabstaende, D-Breiten, Schrittzahlen);
  die Kasten-Schrittprotokolle sind bitgleich (gleiche sha256). Sechs Felder werden jetzt mit 20 statt 8 bzw. 10
  Stellen ausgegeben und sind deshalb als Text verschieden (lemma_info, protokoll.lemma_P, protokoll.lemma_J,
  protokoll.eps_1_bis_4, beide Zeilensummen); die alten Werte sind Rundungen derselben Zahlen.
- Die Empfindlichkeitskontrolle zeigt, wo der Test kippt (Kr hat Radius etwa delta/8, Kippunkt etwa 7/8 delta). Sie
  zeigt Empfindlichkeit, nicht Strenge; die Strenge liegt allein in den Lemmata und der Kugelrechnung.
- Laufzeiten von A2 und B2 hoeher als bei A und B (50,6 s, 69,9 s). Die drei zusaetzlichen Punktlaeufe der
  Empfindlichkeitskontrolle kosten in A2 etwa 25 s, das Hashen 0,2 s. Den Rest machen langsamere Kernlaeufe bei
  gleichen Ergebnissen aus, also die Umgebung (Last auf der .69), keine andere Rechnung:
  - A2 gegen A: Punkt 13,6 s gegen 6,9 s, Jacobi am Punkt 33,5 s gegen 18,4 s, Kasten 41,0 s gegen 18,3 s.
  - B2 gegen B: 16,7 s, 48,3 s, 24,2 s gegen 11,0 s, 23,4 s, 24,0 s.
- Frueher und ueberholt: ZERT-1, ZERT-2, ZERT-3 (Zwischenfassungen des Treibers) sowie ZERT-A-L40 und ZERT-B-L44
  (Treiber pruef.py, ohne Parameter und Hashes im JSON). Sie liefern dieselben Kastenradien und Einschluesse und
  bleiben unveraendert als Verlauf liegen.

### 3.2 Zahlen des Beweislaufs A2 (L = 40), Pflichtangaben der Plan-Lesung (B1)

Rundungsregel fuer diese Tabelle (Auflage K1 der Code-Lesung): Untergrenzen sind abgerundet, Obergrenzen
aufgerundet; "~" steht bei Groessen ohne Schrankenrolle. Quelle aller Werte: zertifikat/ZERT-A2-L40.json (Feld
protokoll, 20 Stellen) und LAUF-zertA2-L40.log.

| Groesse | Wert |
|---|---|
| khat (fest, dyadisch) | 2683731777057 * 2^-40 ~ 2,4408398 |
| s1, s3 (feste dyadische Skalen; ihr genauer Wert ist unerheblich) | 2732420236147253 * 2^-20; 1249525116156041501441206294031155549638271840599013 * 2^-200 |
| Schritte Punkt / Kasten | 324 / 328; R in [49/4096; 3583/4096] = [0,011962890625; 0,874755859375], h in [0,00396728515625; 0,29156494140625]; alle R < r_j (r_j > 0) |
| erster Schritt (Reihe um 0) | Startversuch R0 = 1, nach sieben Verkleinerungen (R -> dyf(4/5 R, 8): 1, 51/64, 163/256, 65/128, 13/32, 83/256, 33/128, 13/64) angenommen: R = 13/64, h0 = 13/128, q = 1/2; Ordnung 2N = 128 (Punkt) bzw. 96 (Kasten); Inflationsrunden 4 bzw. 10; Rest <= 4,9e-39 bzw. <= 1,1e-27. Die Reihe um 0 traegt bis r = 13/128, danach Lemma T. Im Schrittprotokoll steht fuer Schritt 0 fehlversuche = 0, weil bewkern.integrate nfail erst ab r_j > 0 setzt; die sieben Verkleinerungen folgen aus der Schleifenlogik und stehen als Nachbildung in protokoll.erster_schritt_*.verkleinerungen (folge_trifft_R_angenommen = true). Die Summen der Fehlversuche (184 Punkt, 186 Kasten) enthalten sie nicht. Der Kern bleibt dafuer unveraendert (Hashkette). |
| groesster Schrittrest | Punkt <= 3,5e-30, Kasten <= 7,8e-13 (Kasten N = 48, breite Parameter) |
| H_0(z0) | [+- 1,3e-7], [+- 6,1e-8], [+- 9,9e-26], [+- 3,8e-25] |
| delta (a, c, rho, omega) | ~ 1,2827e-22; ~ 1,0237e-6; ~ 4,5862e-22; ~ 2,4022e-22 (exakt dyadisch in protokoll.Z) |
| eps_1 .. eps_4 | <= 1,5467e-16; <= 1,4301e-16; <= 2,3122e-26; <= 2,3101e-26 |
| Lemma P (i) | f* <= 2,8852e-9 < 2,9140e-9 <= phibar |
| Lemma P (ii) | K m^3 <= 1,5467e-16 < 3,0932e-16 <= eta |
| Lemma P (iii) | Lambda <= 6,172e-17 < 1 |
| Lemma P (iv) | c - eta >= 7,5182518 > 0 |
| Lemma P Konstanten | K <= 3,640e-19, m <= 7,518254 |
| Lemma J | Q <= 5,552e-17, mu <= 0,95353, eps <= 5,294e-17, E_A <= 2,275e-17, E_B <= 5,294e-17, E_A' <= 6,872e-17, E_B' <= 8,328e-17, K_J - 1 <= 7,57e-17 (protokoll.K_J_minus_1_obere_schranke) |
| Kanaele ueber Z | k^2 >= 5,957699, kappa_c^2 >= 0,274964, rho - (1 - omega) >= 1,637745, (1 + omega) - rho >= 0,148509 |
| Weitere Bedingungen ueber Z | 2 kappa0 - kappa_c >= 0,375236 (Lemma E), 2 omega^2 - 1 >= 0,595353 |
| Krawczyk | Kr strikt im Innern von Z; Innenabstand >= 0,87499 delta je Koordinate; gewichtete Zeilensumme <= 5,6813e-9; ungewichtet <= 27253 |
| Breite von D = DH_0(Z) relativ zu mid | <= 1,92e-9 (protokoll.D_relbreite) |
| M1 (Profil bei omega0, 2x2) | bestanden: a in [1,024235506571665864904 +- 2,2e-22], c in [7,518253 +- 2,2e-7], gewichtete Zeilensumme <= 1,8e-12 |
| M2 (F(rho0, omega0)) | Psi_n-Normierung: F_1 in [+- 1,2e-14], F_2 in [+- 1,2e-13] (entspricht |Psi(0)| <= 1e-22 bei Normierung e^{kappa_c r} B -> 1) |
| Positivitaet | L_p = 7,04754638671875 (exakt); danach bis L |f| < thr <= sqrt(S_-) mit thr >= 0,33208949 (Feld schwelle; gepruefte Bedingung), tatsaechlich |f| <= 0,093 (Schrittprotokoll); Lauf B2: L_p = 7,3560791015625, danach |f| <= 0,085 |

Lauf B2 (L = 44, 320 bit), soweit abweichend:
- erster Schritt ebenfalls R = 13/64, h0 = 13/128; Ordnung 144 bzw. 88; Rest <= 7,4e-44 bzw. <= 2,8e-25;
- eps_1 .. eps_4 <= 3,4980e-18; 3,2264e-18; 6,7951e-29; 6,7892e-29; K_J - 1 <= 1,72e-18;
- gewichtete Zeilensumme <= 2,6010e-7; Innenabstand >= 0,87499 delta.

### 3.3 Budget (Plan-Lesung W1)

Der Vorwaertsschuss verstaerkt Profilfehler in der Zeile H_0,1 etwa um L e^{2 kappa0 L} (etwa 1e17 bei L = 40).
Gemessen:
- Lauf A2 (q = 1/3, N = 64): Breite von H_0,1(z0) <= 1,3e-7. Sie geht fast nur in die c-Richtung
  (dH_0,1/dc = -1, dH_0,1/da ~ -2,1e15), daher delta_c ~ 1e-6, delta_a ~ 1,3e-22.
- Lauf B2 (q = 1/4, N = 72, 320 bit): Breite <= 6,7e-18, delta_c ~ 1,2e-15.
- In beiden Laeufen schliesst das Budget mit Innenabstand >= 0,87499 delta. Der Kastenfaktor 8 ist vorab gesetzt.
- q = 1/3 und 1/4 lagen vor der Lesung fest (06:43 bzw. 06:54). Die Lesung schaetzt fuer q = 1/2 ein Scheitern; das ist nicht erprobt.
- z0 ist mit 200 bis 197 Nachkommabits exakt dyadisch gespeichert (Plan-Lesung K6: mindestens 120).

## 4. Dateien (zertifikat/, sha256 in zertifikat/SHA256SUMS.txt)

- Code: bewkern.py (Kern: Lemma T, T0, Rekursionen, A-priori-Huelle; seit 07:02 unveraendert) und pruef-v2.py
  (Treiber fuer A2/B2: Newton, Lemma P/J, Krawczyk, Protokoll, Kontrollen; heisst auf der .69 pruef.py). Die
  aeltere Treiberfassung pruef.py (erzeugte A und B) bleibt unveraendert liegen.
- Achtung Namensgleichheit: Im Feld sha256 von ZERT-A2/B2 sind die Schluessel 'bewkern.py' und 'pruef.py' fest im Code
  gesetzt (pruef-v2.py Zeile 406). 'pruef.py' bezeichnet dort den laufenden Treiber, also lokal pruef-v2.py
  (sha256 922eb191...). Gemeint ist nicht die lokale aeltere pruef.py (4c58d569...). Zum Abgleich den Hash vergleichen,
  nicht den Namen.
- Startpunkt: z0.json (Zaehler und Exponent je Koordinate).
- Zertifikate (massgeblich): ZERT-A2-L40.json, ZERT-B2-L44.json. Sie enthalten Laufparameter (Feld parameter,
  inkl. Kommandozeile) und die volle sha256 von Code, z0.json, Interpreter und FLINT-Bibliotheken (Feld sha256,
  zur Laufzeit gelesen). Dazu Schrittprotokolle *-SCHRITTE-KASTEN.json und *-SCHRITTE-PUNKT.json (je Schritt
  r_j, R, h, Inflationsrunden, Fehlversuche, Rest, reelle Huelle von f, relative Breiten).
- Logs: LAUF-zertA2-L40.log, LAUF-zertB2-L44.log, LAUF-satzA2.log, LAUF-satzB2.log, LAUF-kontr2.log,
  LAUF-frei3.log, LAUF-newton3.log.
- sha256 (auf der .69 und lokal gleich, geprueft 08:15:49; vollstaendige Liste in SHA256SUMS.txt, `sha256sum -c` ohne
  Fehler, 38 Dateien):
  - bewkern.py a8a7ec6ff96792265bd7ac8cca1504ea7c46f9e10e6d60f655c7d2e07717219d
  - pruef-v2.py 922eb191b47e5f6fa257bc0809d3081a57d424d4d60c04002c9083086c84ee2b
  - z0.json bc8a9352238f99736b2f8a2202bf64e052bcd6b4a7e41db5d0339e8e68be69d7
  - ZERT-A2-L40.json 7fd55b3f494333fb86ce8ea4152a6c7908462df1fa3b403ae2d172e6053d0798
  - ZERT-B2-L44.json 9891e3fa4fe645643c777ff42980da7e417fb94081a7907867b3289038208929
  - ZERT-A2-L40-SCHRITTE-KASTEN.json b1ac8353b3147a25533bf1e314dc0b8e69bf2561b2d66f746734698e442e717d (gleich A)
  - ZERT-A2-L40-SCHRITTE-PUNKT.json baed13e91e48d9e128136fdc18f598150e74073590e70679feabbdde7a92e188
  - ZERT-B2-L44-SCHRITTE-KASTEN.json 71bbd6d29f73a8bf7dc878f30183444a4ebbe3bd09f2ba118b931008f2c3f731 (gleich B)
  - ZERT-B2-L44-SCHRITTE-PUNKT.json 02b181dcde836e3846b8156ce5efd3a0d76fda60c4bb3c38287643a8a737efd3
- Nachrechnen: auf der .69 im Ordner mit bewkern.py, pruef.py (= pruef-v2.py) und z0.json
  `kleintest.sh cpu5 A2 pruef.py zert --z z0.json --N 64 --Nbox 48 --q 3 --kfak 8 --out ZERT-A2-L40.json` und
  `kleintest.sh cpu5 B2 pruef.py zert --z z0.json --Lz 44 --prec 320 --N 72 --Nbox 44 --q 4 --kfak 8 --out ZERT-B2-L44.json`.
- Software (volle sha256, aus ZERT-A2-L40.json, Feld sha256): Python 3.12.3, /usr/bin/python3.12
  e50d468e8b0adfb05733f5b87b3cff34829c4a8c1aea50c865aa8bdfe4bb150f; python-flint 0.9.0: pyflint.abi3.so
  1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138, libflint-6839011d.so.24.0.0
  871a4132fd1e9f3638391b2208e07088f8e3e72a10e41d45f58b150a60c2a1a9, libgmp-e0c82b6b.so.10.5.0
  33d24e675b10f8b1ab93a8ad3fa2ed5012e1b0d89dcdb97273877c6c6b9450d8, libmpfr-be332c05.so.6.2.2
  c4dfcfc7c5c7ab71d427e15f2f9fae4ace88592a81d4596a918dcc02eadfc6e3.
- Keine float64-Operation liegt in der strengen Kette. Float liefert nur Startwerte, den Vorkonditionierer Y, die
  Skalen s1, s3, khat und die Gitterwahl; alle werden als exakte Dyadiken eingelesen.
- Zeilensummen (Lemma K) seit pruef-v2.py als Maximum exakter oberer Zeilenschranken (vorher Python-max ueber
  Kugeln; ohne Folge, die Zahlen sind gleich geblieben).

### 4.1 Code-Landkarte fuer die Gegenlesung (Zeilen der Enddateien in zertifikat/)

| Lemma / Baustein | Code |
|---|---|
| Lemma T0 (Start bei 0): Reihe und Integralform | bewkern.py prof_series0 (126), var_series0 (156), apriori Zweig first (380-381, 390-393), step (463-464, 479-481) |
| Lemma T: A-priori-Huelle, Pruefung R < r_j, Einschlusstest | bewkern.py apriori (350-438), contains_all (277), inflate_acb (271) |
| Lemma T: Cauchy-Rest, Auswertung | bewkern.py step (456-501): tailfac = q^N/(1-q), acb_beta (284), horner/horner_mat (442-453) |
| Profil-Rekursion fuer r_j > 0 (2/r als Reihe) | bewkern.py prof_series (102) |
| Offener Kanal in Variation der Konstanten, lineares System | bewkern.py trig_series (69), lin_M_series (168), M_complex (289), lin_recursion (235) |
| Jets (Zusatz J) | bewkern.py var_series (144), lin_Mp_series (191), Mp_complex (304), lin_recursion Zweig Mps |
| Gitter exakt dyadisch, Schrittsteuerung | bewkern.py integrate (540), dyf (527), fr_arb (533) |
| H_0 und DH_0 | pruef-v2.py evalH (57) |
| Lemma P und J (Schranken eps_1..4) | pruef-v2.py tail_E (88) |
| Lemma K (Krawczyk-Brouwer), M1, M2, Empfindlichkeitskontrolle, Protokoll | pruef-v2.py zert (393), zeilenschranke (330) |
| Erster Schritt, Versuchsfolge (Protokoll) | pruef-v2.py erster_schritt (358) |
| Lemma Pos | pruef-v2.py positivity (374) |
| Kontrollen T1, T2 | pruef-v2.py kontrolle (602) |

Nicht Teil der strengen Kette: shoot_float, start_a, c_from_float (float-Startwerte), der Newton-Modus, relw
(Protokoll), consts (Skalen), erster_schritt und sha256_datei (Protokoll).

## 5. Lueckenliste und Vorbehalte

1. **Gegenlesung:** Code und Zertifikat frisch gegengelesen (LESUNG-CODE.md, 30.09.). Urteil: traegt mit Auflagen
   (Code-Lesung W1, K1-K8); alle eingearbeitet (Abschnitt 7). Es fehlen weiterhin eine Lesung aus einem fremden Haus (nicht
   Anthropic) und ein zweites unabhaengiges Programm (Punkt 3).
2. **Softwarevertrauen**: python-flint 0.9.0 / FLINT (Kugelarithmetik, acb_contains, Polynomprodukte).
3. **Kein zweites unabhaengiges Programm.** Codex' Parallelplan (bic-proof/analytic/CONTINUUM-MEMBERSHIP.txt)
   waere es, wenn Codex getrennt rechnet (Entscheidung der Leitung).
4. Eindeutigkeit des Profils unter allen positiven radialen Loesungen [L?] (Kandidaten: Killip-Oh-Pocovnicu-Visan
   2017, Serrin-Tang 2000; Skalierung f(x) = lambda g(mu x), lambda^2 = 4/3, mu^2 = 8/3 fuehrt auf
   Laplace g - w g + g^3 - g^5 = 0, w = 3 kappa0^2/8 = 0,0759 in (0, 3/16)). Nicht tragend.
5. Eindeutigkeit von (rho*, omega*) in Z nicht gezeigt (E nur stetig, keine C^1-Schranke).
6. Nur l = 0; keine Aussage zum wesentlichen Spektrum des vollen Bueschels.
7. Nichtlineare Theorie ausdruecklich ausgeschlossen (Codex: Abstrahlung ~ epsilon^4).

## 7. Einarbeitung der Code-Lesung LESUNG-CODE.md (07:14:03 bis 08:03:32)

| Befund | Aenderung | Stelle |
|---|---|---|
| W1 erster Schritt falsch angegeben | Richtig: Startversuch R0 = 1, angenommen nach sieben Verkleinerungen R = 13/64, h0 = 13/128, q = 1/2, Ordnung 2N, Inflationsrunden 4 (Punkt) bzw. 10 (Kasten), Reste <= 4,9e-39 bzw. <= 1,1e-27 (A2), <= 7,4e-44 bzw. <= 2,8e-25 (B2); Versuchsfolge im Protokoll nachgebildet (folge_trifft_R_angenommen = true) | BEWEIS.md 3.2; BEWEIS-PLAN.md 6; ZERT-A2/B2 protokoll.erster_schritt_* |
| K1 drei Untergrenzen aufgerundet | Abgerundet: kappa_c^2 >= 0,274964, (1 + omega) - rho >= 0,148509, 2 omega^2 - 1 >= 0,595353. Beim eigenen Gegenlesen ebenso berichtigt: c - eta >= 7,5182518 (war 7,5182519), Obergrenzen eps, Lemma-J-Werte, Lambda, K, H_0,4, Reste, D-Breite (<= 1,92e-9), Zeilensumme und Innenabstand (>= 0,87499 delta) jetzt nach aussen gerundet; Rundungsregel im Tabellenkopf | BEWEIS.md 2, 3.2, 3.3; BEWEIS-PLAN.md 6 |
| K2 K_J nur im Log | Lemma-P/J-Konstanten mit 20 Stellen im JSON; neues Feld K_J_minus_1_obere_schranke = 7,568377185e-17 (A2), 1,711747734e-18 (B2); Satz: K_J <= 1 + 7,57e-17 | pruef-v2.py zert; ZERT-A2/B2; BEWEIS.md 1 |
| K3 Zertifikat nicht selbstbeschreibend | Neulauf A2/B2 mit unveraendertem Kern; JSON enthaelt parameter (N, Nbox, N0, q, Rmax, rfrac, R0, kfak, prec, Kommandozeile) und sha256 von bewkern.py, pruef.py, z0.json | ZERT-A2-L40.json, ZERT-B2-L44.json |
| K4 Hashes verkuerzt | Volle sha256 von Interpreter, pyflint.abi3.so, libflint, libgmp, libmpfr im JSON und in BEWEIS.md 4 | BEWEIS.md 4 |
| K5 Python-max ueber Kugeln | Zeilensummen als Maximum exakter oberer Zeilenschranken (Funktion zeilenschranke); Zahlen unveraendert | pruef-v2.py 330; BEWEIS.md 4 |
| K6 T1 "nur Radien" unbelegt | T1 gibt jetzt Mittelpunktsdifferenz und Radiensumme getrennt aus: Mittelpunkte gleich bis <= 3,5e-77 (M, Mp) bzw. exakt (g', Y', Jets), Radiensummen <= 5,4e-8; Eingangsradien bei r = 3 ausgegeben | LAUF-kontr2.log; BEWEIS.md 3.1 |
| K7 Wortlaut zur Gegenlesung | Ergebnis und Lueckenliste 1 nennen die Code-Lesung; fremdes Haus und zweites Programm fehlen weiterhin | BEWEIS.md Ergebnis, 5 |
| K8 schaerfere Negativkontrolle | Verschiebung delta/4, delta, 4 delta; Erwartung vorab im Code: delta/4 besteht, delta und 4 delta verfehlen; so eingetreten (A2, B2). Benannt als Empfindlichkeitskontrolle, nicht Strenge | pruef-v2.py zert; BEWEIS.md 3.1 |
| Notiert: Huelle je Schritt nicht im Protokoll | Feld einschlusstest: jeder angenommene Schritt hat acb_contains bestanden (sonst Fehler, kleineres R); die Huellen selbst werden nicht gespeichert (Umfang) | ZERT-A2/B2 protokoll |
| Notiert: L_p des Laufs B fehlte | L_p = 7,3560791015625 in 3.2 | BEWEIS.md 3.2 |
| Notiert: consts() hat unbenutzten Parameter | nicht geaendert (ohne Wirkung) | - |

Vergleich alt gegen neu (jq, zwischen 08:14:21 und 08:15:49): delta, Kr, eps, M1, M2, Z, Kanaele, Innenabstaende, D-Breiten, Schrittzahlen,
z0, khat, s1, s3, L, prec gleich; Kasten-Schrittprotokolle bitgleich. Die Neulaeufe aendern also keine Zahl des
Beweises, nur das Protokoll.

### 7.1 Einarbeitung der Lesung der letzten Schicht (LESUNG-LETZTE-SCHICHT.md, 08:21:54 bis 09:56:58)

Urteil der Lesung: letzte Schicht traegt; sechs kleine Befunde, nur Wortlaut und Protokoll. Keine Codeaenderung,
kein Neulauf: Keiner der Befunde betrifft eine Zahl oder eine Pruefbedingung; der Kern bleibt fuer die Hashkette
unveraendert.

| Befund | Aenderung | Stelle |
|---|---|---|
| L1 Schritt 0 zeigt fehlversuche = 0 | Erklaert: nfail wird erst ab r_j > 0 gesetzt; die sieben Verkleinerungen stehen als Nachbildung in protokoll.erster_schritt_*; Summen 184/186 ohne sie | 3.2, Zeile "erster Schritt" |
| L2 "|f| < 0,33208949" mit falschem Grund | Jetzt: |f| < thr <= sqrt(S_-) mit thr >= 0,33208949 (gepruefte Bedingung), tatsaechlich |f| <= 0,093 (A2) bzw. <= 0,085 (B2) laut Schrittprotokoll | 2 Punkt 5; 3.2, Zeile "Positivitaet" |
| L3 "Alle gemeinsamen Felder gleich" zu weit | Praezisiert: gleich bei gleicher Ausgabegenauigkeit; sechs Felder jetzt mit 20 Stellen, als Text verschieden, Rundungen derselben Werte | 3.1; STAND.md Berichtigungszeile |
| L4 Laufzeitunterschied nur teilweise erklaert | Ergaenzt: Empfindlichkeitskontrolle etwa 25 s, Hashen 0,2 s, Rest langsamere Kernlaeufe bei gleichen Ergebnissen (Last), Zahlen je Teillauf | 3.1; BEWEIS-PLAN.md 6 |
| L5 doppelte Befundkuerzel | "Plan-Lesung (B1)", "Plan-Lesung W1", "Plan-Lesung K6", "Code-Lesung W1, K1-K8" | 3.2, 3.3, Ergebnis, 5 Punkt 1 |
| L6 Treibername im JSON gegen Datei | Hinweis: Schluessel 'pruef.py' im Feld sha256 ist fest im Code und meint den laufenden Treiber (lokal pruef-v2.py, 922eb191...); Abgleich per Hash | 4 |

### 7.2 Fremdlesung aus dem Haus OpenAI (ab 2026-09-30 12:43:12 CEST, date)

- Quelle: coordination/resonance-20260930/beweis1-fremdlesung/ (GESAMT-REVIEW.txt), Urteil "TRAEGT MIT AUFLAGEN", kein
  tragender Fehler.
- Dieser Abschnitt ist reiner Text, auf Bitte der Leitung: kein Neulauf, zertifikat/ unveraendert, die Hashkette bleibt.
  Vorher hatte diese Datei sha256 6985f0bb... (Stand 10:00:36).

| Auflage | Einarbeitung |
|---|---|
| 2 Wortlaut "Einfachheit" | Satz Punkt 3 heisst nur: Der Raum der auf [L, oo) quadratintegrierbaren Loesungen im radialen Sektor l = 0 ist bei festen (rho*, omega*) eindimensional (geometrische Vielfachheit 1). Nicht gezeigt: algebraische Einfachheit des dynamischen Generators, fehlende Jordan-Ketten, Eindeutigkeit von (rho, omega), andere l-Sektoren, Stabilitaet. |
| 3 Wortlaut "eingebettet" | Nur im operationalen Sinn von Satz Punkt 4 (offener freier Kanal, k^2 > 0, und eine nichttriviale exponentiell lokalisierte Loesung). Fuer eine operatortheoretische Aussage fehlen Realisierung und Domaene des vollen Bueschels und die Bruecke von dessen wesentlichem Spektrum zum freien Kontinuum; das wird nicht behauptet. Die Laborfrequenzen omega* +- rho* sind gezeigt, ihr Verhaeltnis nicht: "periodisch oder quasiperiodisch". |
| 1 Einfachheitsbedingung im Flag (Hinweis) | 2 kappa0 > kappa_c ist in A2 und B2 erfuellt (>= 0,375236, Tabelle 3.2) und von der Fremdlesung mit eigener exakter Bruchrechnung bestaetigt. Sie stand aber nicht in M3.BESTANDEN. In BEWEIS-2 (RUNDE-10/beweis2/, pruef-l0.py und pruef-l1.py) steht sie im Gesamtflag. |
| 4 Praezisierungen und Export (Hinweis) | Zusatz S: "gewichtete Supremumsnorm" meint sup_{s >= L} von u~_z(s) = s e^{kappa0(z) s} f_z(s), also die parameterweise normierten Funktionen aus Lemma P; der Randstetigkeitsbeweis benutzt nur diese Groessen. Lemma T0: Dt2 ist eine Huelle von {t^2 : |t| <= R} (Kreisscheibe), nicht das Intervallprodukt des Quadrats Dt. Die Untergrenzen von phibar und eta in Tabelle 3.2 stehen nicht im JSON (dort nur .upper()); der Vergleich im Code rechnet mit den vollen Intervallen und bleibt gueltig. Y, DH_0(Z) und Mk fehlen im JSON. In BEWEIS-2 werden Untergrenzen, Y, DH_0(Z), Mk, H_0(z0), eps, delta und Kr exakt exportiert. |
| Hinweis zu Lemma T | 0 < h < R, N >= 1, qfac > 1 kuenftig ausdruecklich pruefen; A2 und B2 erfuellen das (Fremdlesung). In BEWEIS-2 steht die Pruefung fuer T2 im Gesamtflag, fuer T1 aus den Schrittprotokollen. |

Offen bleibt nach der Fremdlesung: ein vollstaendiges zweites Programm (eigene ODE-, H_0- und Krawczyk-Nachrechnung).
Die Fremdlesung hat Kanalgrenzen, Einfachheitsbedingung, Aussenrundung von Tabelle 1 und "B echt in A" unabhaengig
nachgeprueft; das ersetzt kein zweites Programm.

## Einfach gesagt

Ein Q-Ball ist ein Klumpen aus Feld, der sich auf der Stelle dreht und dabei zusammenhaelt. Stoesst man ihn an,
schwingt er, und normalerweise strahlt er dabei Wellen ab und verliert Energie. Wir haben mit einem Computer, der
jede Zahl als garantierten Bereich statt als gerundete Zahl fuehrt, bewiesen: Bei einer ganz bestimmten
Drehgeschwindigkeit gibt es eine Schwingung, die in der vereinfachten (linearen) Rechnung ueberhaupt keine
Welle nach aussen schickt. Ein frischer Leser hat Programm und Rechnung nachgeprueft und nur Fehler in der
Beschreibung gefunden, die jetzt berichtigt sind; eine Pruefung durch ein anderes Haus steht noch aus. Bei grossen
Ausschlaegen strahlt der Ball trotzdem ein wenig ab; das sagt der Satz nicht aus.
