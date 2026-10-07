# INDUZIERT-KUGEL-1: Plan (Code-Agent, Runde 39)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 10:40:21 CEST (date). Code ab etwa 10:50, Rauchlaeufe
  08:56:16 bis 09:00:02 UTC (.69), Plantext ab 11:00:55 CEST (date).
- **Grundlage:** KARTE.md (KU0 bis KU4, Wahrscheinlichkeiten und Bedeutungssaetze unveraendert, Abschnitt 6);
  induziert-g-l/DOSSIER.md Abschnitte 6 und 8; INDUZIERT-DICHTE-4D (PLAN, ERGEBNIS, code/).
- **Code:** code/kugel.py und code/auswertung_kugel.py (neu). Unveraendert kopiert und importiert:
  dichte4d.py (sha256 2881048e..., = eingefrorene Fassung INDUZIERT-DICHTE-4D), induziert.py (b3867eac...),
  zufall2d.py (37a0fe8f..., = eingefrorene Fassung INDUZIERT-DICHTE-2D).
- **Kennzeichen:** [M] eigene Mathematik, [L] Literatur aus dem Gedaechtnis, [F] Festlegung dieses Plans, [K]
  Kartenpunkt (vor dem Einfrieren offengelegt), [H] Hypothese, [E] im Rauchlauf gerechnet (blind, nur Streuungen,
  Netz-, Volumen- und Zeitdaten).

## 1. Schreibtisch: Abschnitt 8.3 des Dossiers nachgeprueft (vor jeder Messung)

| Nr | Behauptung (Dossier/Karte) | Pruefung | Befund |
|---|---|---|---|
| S1 | Int sqrt(g) R auf S^4 = 32 pi^2 a^2 = 61,6 sqrt(N) bei Dichte 1 | R = 12/a^2, Vol = (8 pi^2/3) a^4 = N, a^2 = (3/(8 pi^2))^(1/2) sqrt(N) = 0,19492 sqrt(N); 32 pi^2 a^2 = 16 pi (3/2)^(1/2) sqrt(N) | **richtig**: 61,562 sqrt(N) [M] |
| S2 | c = 6 B (konforme Mode) | 4D, g = e^(2 sigma) delta: sqrt(g) R = -6 e^(2 sigma)(Box sigma + (grad sigma)^2), partiell integriert Int sqrt(g) R = 6 Int e^(2 sigma)(grad sigma)^2 exakt; fuer kleine sigma 6 Int (grad sigma)^2 | **richtig im Grenzfall S -> 0** [M] |
| S2' | beta = 61,6 B = 10,26 c_Torus, also +1,14 +- 0,46 | c_Torus wurde mit dem Schema y = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/(S^2 V), S = 0,25, bei fester Punktzahl gemessen. Fuer eine reine Einstein-Wirkung gilt dort exakt y = 6 B_1 k^2 (I1(2S)/S) I0(4S)^(-1/2): Faktor I1(2S)/S aus Int e^(2 sigma)(grad sigma)^2 = s^2 k^2 V I1(2s)/(2s), Faktor I0(4S)^(-1/2) aus B(rho) = rho^(1/2) B_1 (Homogenitaet, Grad 2) bei der Dichte 1/I0(4S). Bei S = 0,25: 1,0316 mal 0,8887 = 0,9168 (steht schon in PLAN-4D [K5]) | **Fehler 1:** Unter H-kov ist c_Torus = 6 B_1 mal 0,9168, also beta = 61,562/(6 mal 0,9168) c_Torus = **11,19 c_Torus = +1,24 +- 0,50** statt 1,14 +- 0,46 [M]. Karte (KU2) bleibt; die Planlesart nutzt 1,24 +- 0,50, beide werden berichtet |
| S3 | Volumenglied (N - 1)/4 ln(V_Kugel/V_Polytop) fuer Gamma | K_T = V P^T G^-1 P ist vom Grad n - 2 in den Laengen; Gamma(lambda l) = Gamma(l) + (N - 1)(n - 2)/2 ln lambda exakt; Polytop auf V_K skalieren: lambda^n = V_K/V_R | **richtig fuer Gamma** [M]; Kontrolle KE bestaetigt die Skalierung auf 1e-10 [E] |
| S3' | (implizit) gilt so fuer beide Regeln und fuer Gamma_M | M ist vom Grad n, M^-1 K vom Grad -2: Gamma_M(lambda l) = Gamma_M(l) - (N - 1) ln lambda. Regel S hat ein eigenes Volumen V_S = sum_T J_T V_T^C, das nicht V_K ist (Mittelpunktsregel fuer das Integral von J) | **Ergaenzung 2 [K2]:** Korrektur je Regel mit deren eigenem Volumen V_R; fuer Gamma_M mit umgekehrtem Vorzeichen: Gamma_M,korr = Gamma_M - (N - 1)/4 ln(V_K/V_R). Groesse vorab (Rauch, keine Messgroesse): Gamma, Regel C +1,70 sqrt(N) (V_C/V_K = 0,80 bei N = 1000 bis 0,927 bei 8000), Regel S -0,48 sqrt(N) (V_S/V_K = 1,064 bis 1,021). Beides ist so gross wie die erwarteten beta; ohne Korrektur waere KU1 bis KU3 von der Volumenkonvention beherrscht |
| S4 | 2D: K skaleninvariant, kein Volumenglied, beta_2D = 0 | Grad n - 2 = 0; Int sqrt(g) R = 8 pi topologisch; Kruemmungsanteile von Masse und Laengen O(h^2 R) N = O(1) | **richtig** [M]. Zusatz: In 2D ist Regel S fuer Gamma exakt gleich Regel C (Simplizes nur aehnlich skaliert; Kontrolle KH: Abweichung 0,0). Gamma_M haengt in 2D vom Volumen ab (-(N - 1)/2 ln(V_K/V_R)), das Glied ist aber O(1) (V_C/V_K = 0,9985 bei N = 4000) |
| S5 | gamma ln N universell, Groessenordnung 1, stoert nicht | ln N-Glied aus zeta(0) [M]: Gamma ⊃ -(zeta(0)/n) ln N; Torus zeta(0) = -1 (Nullmode), S^4 minimal gekoppelt zeta(0) = 29/90 - 1 (a_2 = 29/(15 a^4)) [L Waermeleitungskoeffizienten, M]; S^2: 1/3 - 1 | gamma_4D = -29/360 = -0,081, gamma_2D = -1/6 (wie Dossier). **Begruendung fuer gamma = 0 im Fit:** Ein nicht mitgefuehrtes gamma ln N verschiebt beta um gamma b0 mit b0 = 0,0388 (4D-Design) bzw. 0,0164 (2D-Design), also um 0,003 bzw. 0,003 bei den Kontinuumswerten und um hoechstens 0,04 bei abs(gamma) <= 1. Frei mitgefuehrt waere gamma bei unserem Rauschen unbestimmt (ln N ist ueber Faktor 8 in N fast linear in sqrt(N)) und wuerde SE(beta) etwa verzehnfachen. Der Dreiparameterfit wird beschreibend mitberichtet |
| S6 | H-Kont: beta ~ -0,58 | B = -Lambda^2/(192 pi^2), Lambda^4 = 32 pi^2 (Modenzahl) -> Lambda^2 = 17,8, beta = 61,56 B = -0,578 | nachgerechnet wie Dossier; nur das Vorzeichen wird benutzt |
| S7 | Rauschen ~0,15 sqrt(N) je Netz, SE(beta) 0,05 bis 0,1 mit 4 bis 6 Saaten | Rauchlauf (blind, Abschnitt 10) | **zu optimistisch**: Std von y = Delta Gamma/sqrt(N) je Saat 0,38 (N = 1000) und 0,11 (2000) aus je 4 Saaten, in 2D 0,28/0,12/0,14 (4000/16 000/64 000). Mit dem Zweiparameterfit Std(beta_j) etwa 0,3 bis 0,45 (4D) und 0,21 (2D). Daher 40 Saaten in 4D und 80 in 2D (Karte: "mehr Saaten statt neuer Groessen") |

- **Regge-Kruemmung des Sehnenpolytops [E, beschreibend]:** sum_h A_h delta_h/(1/2 Int sqrt(g) R) = 0,921 (N = 1000),
  0,943 (2000), 0,960 (4000), 0,972 (8000). Die Abweichung faellt wie 1/sqrt(N) und geht damit in delta, nicht in
  beta. In 2D ist die Summe exakt 4 pi (Gauss-Bonnet, Abweichung <= 1e-13).

## 2. Konstruktion (code/kugel.py)

- **Kugel S^n [Karte]:** N Punkte normalverteilt in R^(n+1), normiert, mal a; omega_n a^n = N (omega_4 = 8 pi^2/3,
  omega_2 = 4 pi). Saat numpy default_rng([20261004, 39, n, N, saat]).
- **Netz:** scipy ConvexHull (Qhull; Optionen scipy-Vorgabe, in R^5 "Qx Qt", in R^3 "Qt"). Facetten = Simplizes
  des sphaerischen Delaunay. Normale aus dem verallgemeinerten Kreuzprodukt der Kantenvektoren; **Orientierung:**
  zwei Ecken getauscht, wo die Normale nach innen zeigt (Normale . Schwerpunkt < 0).
- **Pruefung je Kugelnetz (Tor):** Ecken je Simplex verschieden; alle N Punkte benutzt; jede Facette ((n-1)-Seite) in
  genau zwei Simplizes mit entgegengesetzter induzierter Orientierung; Euler-Charakteristik sum (-1)^d f_d = 2;
  d0 > 0 (Ursprung innen); kleinstes Simplexvolumen > 0; eigene Normale gegen Qhull-Normale cos >= 1 - 1e-9;
  **leere Kappen:** kein Punkt im Inneren der Kugelkappe ueber einer Facette (kd-Baum, Kugel um a n mit Sehnenradius
  mal (1 - 1e-9)); in 2D zusaetzlich Gauss-Bonnet abs(sum_v (2 pi - Winkelsumme) - 4 pi) <= 1e-8.
- **Regel C:** Kantenlaengen = Sehnen. **Regel S:** je Simplex alle Laengen mal J_T^(1/n), J_T = a^n d0/abs(c_T)^(n+1)
  (Jacobi-Faktor der Radialprojektion x -> a x/abs(x) am Schwerpunkt c_T, d0 = n . c_T). Kontrolle: Quadratur zweiten
  Grades von J auf jedem Simplex summiert sich auf V_K (Projektionen pflastern die Kugel): V_Q/V_K = 0,9980 bis
  0,99977 (4D), 1 - 1e-6 (2D), waehrend V_S/V_K = 1,064 bis 1,021 [E].
- **Torus [Karte]:** 4D dichte4d.periodisches_netz (isotrop L = N^(1/4), Saum 2,5, s = 0, Pruefung dichte4d.gueltig);
  2D zufall2d.zufallsnetz (L = N^(1/2); Tor: Euler 0, Kanten in genau zwei Dreiecken, Ecken verschieden, Orientierung
  > 0, Flaeche exakt, keine Delaunay-Verletzung > 1e-9). Torus-Saat = 39000 + saat (frische Saaten).
- **P1 [Karte]:** K_T = V P^T G^-1 P aus den Kantenlaengenquadraten (Gram-Formel), m^2 = 0, fuer n = 2 und 4 mit
  derselben Funktion; K global per COO-Summe.
- **log det' [Karte]:** Gamma = 1/2 (log det K_(0) + log N), Knoten 0 geerdet, scipy splu (MMD_AT_PLUS_A,
  SymmetricMode, diag_pivot_thresh 0, Equil aus), math.fsum der log U_ii; LU ok: alle U_ii > 0, perm_r = perm_c,
  alle Simplizes einbettbar.
- **Gamma_M [Karte]:** 1/2 log det'(M^-1 K) = Gamma - 1/2 sum_i log m_i + 1/2 log(sum_i m_i/N) [M, exakt aus
  adj(D K D) mit D = M^(-1/2)], m_i = sum_(T an i) V_T/(n+1) mit den Volumina der jeweiligen Regel; Kontrolle KC
  gegen verallgemeinerte Eigenwerte.
- **Volumenkorrektur [K2]:** Gamma_korr = Gamma + (n-2)/(2n) (N-1) ln(V_K/V_R); Gamma_M,korr = Gamma_M - (N-1)/n
  ln(V_K/V_R); V_R = Summe der Simplexvolumina der Regel; Torus: V_R = V = N (Korrektur 0 bis auf Rundung).

## 3. Messgroesse und Fit [Karte; F wo vermerkt]

- Je Saat j, Dimension n, Regel r, Groesse q (Gamma, Gamma_M), Fassung v (korr = Urteil, roh = berichtet):
  y_j(N) = (G_Kugel,j(N) - G_Torus,j(N))/sqrt(N).
- **Fit [F]:** je Saat y_j(N) = beta_j + delta_j/sqrt(N) (gleichbedeutend mit Delta Gamma = beta sqrt(N) + delta,
  gewichtet mit 1/N), OLS ueber alle N der Dimension; gamma = 0 (Begruendung S5). **beta = Mittel der beta_j,
  SE = Std(beta_j, ddof 1)/sqrt(M)**. Kugel- und Torusnetz einer Saat und verschiedene N sind unabhaengig; die
  Gruppierung nach Saat dient nur der SE.
- **Mitberichtet (beschreibend, kein Urteil):** Dreiparameterfit (beta, gamma, delta) je Saat; beta mit gamma auf dem
  Kontinuumswert (beta - gamma b0); WLS-Fit auf die Mittelwerte je N mit chi^2 (Modellprobe); Teilbereiche ohne
  kleinstes bzw. groesstes N; Mittelwerte von y je N; Volumen-, Regge- und Netzstatistik.
- **KU4-Groesse:** d_j = beta_j(Gamma) - beta_j(Gamma_M), gepaart auf denselben Netzen; Mittel und SE wie oben.

## 4. Saaten, N, Laeufe [Karte; F]

- 4D: N = 1000, 2000, 4000, 8000 [Karte], Saaten 0 bis 39 (40 je N) [F, S7]. 2D: N = 4000, 16 000, 64 000 [Karte],
  Saaten 0 bis 79 (80 je N) [F, S7].
- Laufzeit je Saat (Rauch, beide Regeln, Kugel und Torus, alle Pruefungen): 4D 7 / 12,5 / 27 / 85 s, RSS bis 1,13 GB;
  2D 0,5 / 2,4 / 11,4 s.
- .69, /home/fmh/fmhc-physics-remote/runde39-induziert-kugel/, nur ueber kleintest.sh, Spuren cpu3, cpu4, cpu5, je Spur
  eine Kette nacheinander (ein ssh je Spur, Starter je Lauf). Jeder Lauf schreibt nach jeder (Saat, N).
  - cpu3: kontrolle; N = 8000 Saaten 0-3, 4-7, 8-11, 12-15; N = 4000 Saaten 0-14; 2D Saaten 0-19.
  - cpu4: N = 8000 Saaten 16-19, 20-23, 24-27, 28-31; N = 4000 Saaten 15-29; 2D Saaten 20-39.
  - cpu5: N = 8000 Saaten 32-35, 36-39; N = 4000 Saaten 30-39; N = 2000 Saaten 0-19, 20-39; N = 1000 Saaten 0-39;
    2D Saaten 40-59, 60-79.
  - Ausgabe lauf/messung-n<n>-N<N>-s<saat0>.json (2D: N-Liste in einer Datei), lauf/kontrolle.json, Logs je Lauf.
- **Abbruch [F]:** Nicht fertige (Saat, N) fehlen; Saaten ohne alle N heissen "unvollstaendig" und fallen aus dem Fit
  (offengelegt). Mindestens 8 vollstaendige Saaten je Dimension, sonst "nicht auswertbar". Letzter Start spaetestens
  12:35 CEST.
- Danach: auswertung_kugel.py lauf lauf/auswertung.json (ueber den Starter).

## 5. Tor [F]

- Je (Saat, N): Kugelnetz gueltig (Abschnitt 2), Torusnetz gueltig, drei LU ok (Kugel C, Kugel S, Torus).
- Eine Saat mit einem Fehler bei irgendeinem N wird ausgeschlossen und gezaehlt. Sind mehr als 10 % der Saaten einer
  Dimension ausgeschlossen oder bleiben weniger als 8, sind die Urteile dieser Dimension "nicht auswertbar (Tor)".
- Kontrollen (Abschnitt 7) KA bis KE und KG muessen ihre Schwellen erfuellen, sonst kein Urteil.

## 6. Vorhersagen der Karte (unveraendert) und Urteilsregeln (mechanisch in auswertung_kugel.py)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KU0 | 2D-Kontrolle: abs(beta_2D) <= 2 SE und <= 0,05 | 75 % |
| KU1 | [H] 4D, Regel S: beta > 0 mit >= 3 SE (negatives Gitter-G, wie auf dem Torus) | 50 % |
| KU2 | [H] 4D: beta(Regel S) liegt innerhalb 2 SE von 10,26 c_Torus = +1,14 +- 0,46 | 35 % |
| KU3 | [H] 4D: beta(Regel C) und beta(Regel S) haben verschiedenes Vorzeichen | 30 % |
| KU4 | [H] Mass: beta aus Gamma und aus Gamma_M unterscheidet sich um mehr als 2 SE | 50 % |

Alle Urteile mit der Fassung korr, Groesse Gamma, sofern nicht anders gesagt; die Fassung roh mit denselben Regeln
nur berichtet.
- **KU0** (n = 2, Gamma; Regel C = S):
  - Karte: eingetroffen, wenn abs(beta) <= 2 SE und abs(beta) <= 0,05; sonst nicht eingetroffen.
  - Plan [F]: eingetroffen wie Karte; nicht eingetroffen, wenn abs(beta) > 2 SE (sqrt(N)-Glied nachgewiesen);
    sonst (abs(beta) <= 2 SE, aber > 0,05) nicht auswertbar (Rauschen).
  - Ist KU0 (Plan) nicht "eingetroffen", stehen die 4D-Urteile mechanisch da, tragen aber den Vermerk "keine
    4D-Lesart" (Karte: "Karte stoppen, Ursache suchen").
  - Mitberichtet: Gamma_M (beide Regeln), roh.
- **KU1** (n = 4, Regel S):
  - Karte: eingetroffen, wenn beta >= 3 SE; sonst nicht eingetroffen.
  - Plan [F]: eingetroffen wie Karte; nicht eingetroffen, wenn beta + 2 SE < 0; sonst nicht auswertbar.
  - Zweig der Karte "KU1 verfehlt durch beta < 0 mit >= 3 SE": eigenes Merkmal (beta <= -3 SE).
  - Mitberichtet: Regel C mit denselben Regeln; Abstand zu H-Kont (-0,58) in SE.
- **KU2** (n = 4, Regel S):
  - Karte: eingetroffen, wenn abs(beta - 1,14) <= 2 sqrt(SE^2 + 0,46^2); sonst nicht eingetroffen. ("2 SE" lese ich
    als kombinierte SE von beta und Zielwert, weil die Karte den Zielwert mit +- 0,46 angibt [F].)
  - Plan (Fehler 1, S2'): dieselbe Regel mit 1,242 +- 0,504.
  - Mitberichtet: enge Lesart nur mit SE(beta).
- **KU3** (n = 4):
  - Karte: eingetroffen, wenn die Punktschaetzer beta_C und beta_S verschiedenes Vorzeichen haben; sonst nicht
    eingetroffen.
  - Plan [F]: eingetroffen, wenn beide mehr als 2 SE von 0 liegen und verschiedenes Vorzeichen haben; nicht
    eingetroffen, wenn beide mehr als 2 SE von 0 liegen und gleiches Vorzeichen haben; sonst nicht auswertbar.
  - Mitberichtet: gepaarte Differenz beta_S - beta_C.
- **KU4** (n = 4, Regel S; Regel C mitberichtet):
  - Karte und Plan: eingetroffen, wenn abs(mittel(d_j)) > 2 SE(d), d_j = beta_j(Gamma) - beta_j(Gamma_M) (gepaart);
    sonst nicht eingetroffen.
  - Mitberichtet: beta(Gamma_M) und ob sein Vorzeichen von beta(Gamma) abweicht.

## 7. Kontrollen (code/kugel.py kontrolle; Schwellen vor dem Lauf)

- **KA:** P1 gegen dichte4d.p1_lokal und induziert.lokal_K_batch (n = 4) <= 1e-9 relativ; n = 2 gegen Kotangens-Formel
  <= 1e-9 relativ.
- **KB:** LU gegen dichte Eigenwerte und slogdet(K + 1 1^T/N) <= 1e-8 absolut (Kugel S^4 N = 400 und S^2 N = 400 je
  Regel; Torus 4D N = 600, 2D N = 400).
- **KC:** Gamma_M gegen verallgemeinerte Eigenwerte von (K, M) <= 1e-8.
- **KD:** eigene Gamma gegen dichte4d.gamma (4D-Torus) und zufall2d.Netz.gamma (2D-Torus) <= 1e-9.
- **KE:** Skalierung: Gamma(lambda l) - Gamma(l) = (n-2)/2 (N-1) ln lambda und Gamma_M: -(N-1) ln lambda <= 1e-8;
  korrigierte Groessen skalenfrei <= 1e-8.
- **KF (beschreibend):** V_C/V_K, V_S/V_K, V_Q/V_K und Regge-Verhaeltnis gegen N.
- **KG (Negativproben):** Huelle ohne Punkt 0 gegen alle Punkte: Kappentest muss anschlagen (> 0); ein Simplex
  entfernt: Facettenpaarung muss scheitern, Euler ungleich 2.
- **KH:** 2D Gamma Regel S gegen C <= 1e-9.
- Laufend in jedem Netz: Tor-Pruefungen (Abschnitt 2), LU-Pruefungen, Zeilensumme von K, kleinstes U_ii.

## 8. Kartenpunkte (vor dem Einfrieren offengelegt)

- **[K1] Fehler 1 (S2'):** Der Zielwert von KU2 vergisst den Faktor 0,9168 des Torus-Schemas. Karte unveraendert
  geurteilt, Planlesart mit 1,24 +- 0,50 daneben.
- **[K2] Volumenkorrektur je Regel und fuer Gamma_M (S3'):** Die Karte nennt nur Gamma und V_Polytop. Geurteilt wird
  mit der korrigierten Fassung (Dichte genau 1 bezogen auf das eigene Volumen der Regel, also "Zahl = Volumen"); roh
  wird berichtet. Das Glied ist vorab je Netz exakt berechenbar und keine Messung.
- **[K3] gamma = 0 im Fit (S5):** begruendet ueber b0; Dreiparameterfit beschreibend.
- **[K4] KU4 ist eine Netzgroesse:** d_j ist bis auf 1/2 ln(V/N) und die Volumenkorrektur das sqrt(N)-Glied von
  1/2 sum_i ln m_i (Kugel minus Torus). Es haengt nur von der Netzgeometrie und der Massenkonvention ab, nicht von der
  LU; vorab nicht abgeleitet, aber ohne Materie berechenbar. KU4 sagt also, ob die Massenkonvention ein
  sqrt(N)-Glied traegt, nicht ob die Materie etwas anderes tut.
- **[K5] Regel S ist keine Regge-Geometrie:** Gemeinsame Kanten bekommen in verschiedenen Simplizes verschiedene
  Laengen (wie sp auf dem Torus); K = sum_T J_T^((n-2)/n) K_T^C ist FEM mit stueckweise konstantem Koeffizienten.
  Regge-Summe nur fuer Regel C.
- **[K6] Kugel klein bei N = 1000:** h/a ~ 0,4, R h^2 ~ 2. Hoehere Ordnungen gehen in delta bzw. O(N^(-1/2)); der
  Teilbereich ohne N = 1000 wird beschreibend berichtet.
- **[K7] Saatzahl:** 40 (4D) und 80 (2D) nach der blinden Streuung (S7); die Karte nannte 4 bis 6.
- **[K8] Abhaengigkeit von der Torus-Form:** isotroper Torus (L^n = N), damit dessen Konstante nicht von N abhaengt;
  dichte4d nutzte 24 x 6,5^3.
- Kartenfehler, die ein Urteil nach Kartenwortlaut aendern koennen: [K1] (KU2-Zielwert). [K2] aendert die Lesart von
  KU1 bis KU4 (korr gegen roh); beide Fassungen werden berichtet.

## 9. Agenten-Vorhersagen (nach den Rauchlaeufen, vor den Hauptlaeufen; ohne Kenntnis der Messwerte)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| A1 | Tor besteht in beiden Dimensionen (hoechstens 10 % Saaten ausgeschlossen) | 90 % |
| A2 | KU0 (Plan) eingetroffen | 70 % |
| A3 | Punktschaetzer beta_S (korr) > 0 | 55 % |
| A4 | abs(beta_S - beta_C) > 2 SE (gepaart) | 60 % |
| A5 | KU4 eingetroffen | 65 % |
| A6 | Modellprobe (WLS, Regel S, Gamma, korr) p >= 0,05 | 70 % |

## 10. Rauchlaeufe (Protokoll, vor dem Einfrieren; .69-Zeiten in UTC; Rauchsaaten 900 bis 903, Probesaaten 950 bis 952)

- **kontrolle** (08:56:16 bis 08:56:32, cpu5, rc 0): KA 1,6e-16 / 1,4e-15 / 1,8e-10 (2D gegen Kotangens); KB, KC
  <= 1,0e-12; KD 2,3e-12 (4D) und 0 (2D); KE <= 1,8e-10; KH 0,0; KG: Kappentest schlaegt an (141 bzw. 3 Kappen),
  Paarung scheitert, Euler 1. KF siehe S3', Regge siehe Abschnitt 1. Alle Schwellen erfuellt.
- **rauch-a** (08:56:18 bis 08:57:35, cpu3, rc 0), 4D N = 1000 und 2000, 4 Saaten, blind: alle Netze und LU gueltig;
  F/N Kugel 27,2 bis 27,6 bzw. 28,5 bis 28,7 (flach 31,8; positive Kruemmung); 7,0 und 12,5 s je Saat.
- **rauch-b** (08:56:19 bis 09:00:02, cpu4, rc 0), 4D N = 4000 und 8000, 2 Saaten, blind: gueltig; 27 und 85 s je
  Saat; LU 13/13/21 s bei N = 8000; RSS 1,13 GB.
- **rauch-c** (08:58:19 bis 08:59:17, cpu5, rc 0), 2D N = 4000, 16 000, 64 000, 4 Saaten, blind: gueltig, Gauss-Bonnet
  exakt; 0,5 / 2,4 / 11,4 s je Saat.
- **Blinde Streuung (Std von y = Delta Gamma/sqrt(N), korr, Regel S):** 4D 0,38 (1000, 4 Saaten), 0,11 (2000, 4),
  0,02 und 0,04 (4000, 8000, je 2 Saaten, kaum belastbar); Gamma_M 0,52 / 0,32 / 0,08 / 0,01. 2D 0,28 / 0,12 / 0,14.
  Einzelnetze: Kugel 0,20 / 0,13, Torus 0,21 / 0,22 (4D, N = 1000 / 2000).
- **Codeprobe** (08:58:22 bis 08:59:23, cpu3): nicht blind auf kleinen N (4D 600, 1200; 2D 500, 1000, 2000; Saaten
  950 bis 952), dann Auswertung; rc 0 fuer alle drei. Nur Struktur geprueft (jq keys: dim 2 und 4, je 8 Fits, KU0 bis
  KU4 vorhanden); Werte und Urteile der Probe nicht gelesen.
- **Zeitfolge der Festlegungen:** Konstruktion, Regeln, Fit und Urteilsregeln standen vor den Rauchlaeufen im Code
  (auswertung_kugel.py vor der Probe geschrieben). Nach den Rauchlaeufen festgelegt: Saatzahlen (S7), Laufaufteilung.
  Vor dem Einfrieren keine Mittelwerte oder Vorzeichen der Messgroesse gesehen.
