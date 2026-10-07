# ARBEITSFELD M_E-G3 (Protokoll; Zeiten per date)

Plan: PLAN.md, eingefroren als PLAN.md.eingefroren-20261002-223215 (sha256 94d373a3...dd5a4b), chmod a-w.

## Abrufe und Rechnungen

- 22:10:55 Start. Gelesen (vor Plan, siehe PLAN Abschnitt 0): KARTE, SPIN2-D4-2, LESUNG (Codex), WARUM-SPIN-2 (Glieder 7,
  10, Nachtraege ab 01.10.), CHLPSD, BBIRRS S. 1-18, FRS Abschn. 2, 4, Anh. F. Quellen-Hashes in RUNDE-13/spin2-d4/quellen/
  und spin2-d4-2/quellen/ per sha256sum -c geprueft: alle OK.
- 22:32:15 Plan eingefroren.
- 22:33 Selbstanzeige S1: Vor dem ersten kleintest-Lauf habe ich auf der .69 einmal den Interpreter direkt gestartet
  (`python -c "import scipy, numpy; print(versions)"`, scipy 1.18.0, numpy 2.4.4), also ausserhalb von kleintest.sh.
  Keine Rechnung, nur Versionsabfrage; danach nur noch kleintest.sh und py_compile.
- 22:35:07-22:35:11 R1 [E] kleintest cpu, `w5_funktionale.py check` (Ausgabe: .69 runde23-m_e-g3/check.out, Kopie
  code/check.out):
  - Jacobi-Rekursion (0,8) gegen scipy.eval_jacobi: max. relativer Fehler 4,7e-13.
  - **W5a, CHLPSD (3.3a) -> (3.4a):** Steigung 37,839, Konstante -45,445, also (3.4a) mit 37,8 und -45,4 genau
    reproduziert, aber nur ohne g5. Mit g5: x <= 37,84 L - 45,45 - 0,0579 g5 M^10/G (Einheiten M = G = 1 auf der
    IR-Seite). H1 bestaetigt. Gleiches bei (3.3b) -> (3.4b): 14,143 L - 15,507 - 0,0419 x stimmt mit (3.4b), g5 fehlt
    dort ebenso.
  - **W5b, CHLPSD (3.7):** 1596,7 L - 3208,0 (Quelle: 1598, -3211; Abweichung 0,1 %, gerundete Koeffizienten).
    psi3(1) = 0,0307 statt 0 (Rundung der gedruckten Koeffizienten).
  - **W5c, Positivitaet auf schweren Zustaenden** (m in [1, 40], J <= 200, Grenzfall b <= 400, Glaettung ab p = 0):
    - F_g3 (3.3a): ueberall positiv (relative Minima ++ 1,0e-3, +- 4,3e-4, Grenzfall b: 6,2e-7 > 0). Das prueft meine
      Umsetzung der schweren Dichten gegen CHLPSD Abb. 3.
    - (3.7): ++ und Grenzfall positiv (++ Minimum -1e-9 relativ, Rundung), aber **+- bei m = M, J = 198 stark negativ**
      (relativ -0,99). Ursache [ES]: d44~ = P^(0,8)_{J-4}(x) waechst bei x -> -1 (Rueckwaertsrichtung, nur bei m = M
      erreicht) wie J^8; der Rundungsrest psi3(1) = 0,03 wird dort riesig. Auch ohne Rundung braucht ein reines
      B2/B3-Funktional an der Schwelle eine hohe Nullstellenordnung der +- -Kombination bei p = M; F_g3 umgeht das
      ueber -5 d/dp^2 B4 (Beitrag +10 J^2/m^10).
- 22:37:50 R2 gestartet [E]: LP-Varianten (N = 8, 10, 12 mit drei Schwellenbedingungen B(1) = B'(1) = B''(1) = 0 fuer
  B(p) = psi2^(p)(2 - p^2) - psi3^(p) bei m = M; N = 10 ohne Schwellenbedingung als Vergleich), Spuren cpu, cpu2, cpu4,
  cpu6.

## W1 Woerterbuch, Pruefung (22:38:00)

- FRS schreiben g3^2 in (2.3) und (4.39); die Dreipunktamplitude S. 9 nennt g3 ohne Aussage zu reell/komplex [S]. Da
  der MHV-Term aus (+++) x (---) entsteht, ist |g3|^2 gemeint; bei reellem g3 gleich [ES].
- Unabhaengige Probe der Planckmasse [E, von Hand]: FRS (F.1) hat im Weinberg-Exponenten 1/(8 pi^2 M_Pl^2 eps) mal
  (s log(-s) + t log(-t) + u log(-u)). BBIRRS (3.7) hat je geordnetem Paar G s_ij/(4 pi), also G s/pi fuer s (Paare 12
  und 34, je zweimal geordnet). Gleich, wenn 1/(8 pi^2 M_Pl^2) = G/pi, also M_Pl^-2 = 8 pi G. Stimmt mit dem
  GR-Abgleich (2.6)/(2.7a) ueberein: M_Pl ist die reduzierte Planckmasse.
- Ergebnis W1: |g^3|^2 = 4 |g3_FRS|^2/M_Pl^4 = 4 (8 pi G)^2 |g3_FRS|^2; g4_C = (8 pi G)^2 g4_F; g5_C = (8 pi G)^2 g5_F;
  B_0^4h(FRS) = -B4^(1)(CHLPSD)/2.

## LP-Runden (Eintrag 22:48:44; Laufzeiten aus den kleintest-Kopfzeilen, .69-Uhr in UTC)

- R2 (22:37:48-22:37:58, lp mit Glaettung bis p = M, psi3(0) frei): c_0 = 8 a1/K = 1017 (N = 8), 943 (N = 10),
  875 (N = 12, Koeffizientenbox aktiv); ohne Schwellenbedingung 941. Nachpruefung: ++ leicht negativ zwischen
  Gitterpunkten (m ~ 1,2, J = 4, relativ -9e-4), +- an der Schwelle m = M fuer J > 160 stark negativ.
  Ursache 1 [E/ES]: psi3(0) = b_0 ~ 2e-5 > 0 gibt im +- -Kanal einen Schwanz -b_0/(2J), der den positiven
  B2-Schwanz ~ J^-3 bei grossem J uebertrifft. Folge: psi3(0) = 0 und Grossb-Bedingungen 2 m^2 psi2_2 +- psi3_2 < 0
  (schlimmster Fall m = M) noetig.
- R3 (22:40:01-22:40:20, psi3(0) = 0, Grossb-Bedingungen, J <= 320 an der Schwelle): c_0 = 1024 (N = 8), 946 (N = 10),
  874 (N = 12), 943 (N = 10 ohne Schwellenbedingung). Schwelle m = M: weiter negativ bei J ~ 500-600.
  Ursache 2 [ES]: Bei Glaettung bis p = M erreicht die schwere Welle mit m = M die Rueckwaertsrichtung x = -1; dort
  d44~ ~ (-1)^n 16 eps^-4 J_8(n sqrt(2 eps)) (eps = 1 + x). Ein Endpunktverhalten g ~ (1-p)^k liefert Beitraege
  ~ (-1)^n n^(8-2k-2) Gamma(k+1)/Gamma(8-k); das ueberholt den positiven Vorwaertsschwanz ~ J^-3 erst ab k >= 5
  und auch dann erst bei sehr grossem J. F_g3 (3.3a) rettet das ueber -5 d/dp^2 B4 (+10 J^2), das reine B2/B3-Funktional
  (3.7) nicht.
- R4 (22:43:27-22:43:47, Glaettung nur bis q < M wie FRS (4.27)): c_0 = 878 (q = 0,95), 959 (0,9), 964 (0,9, N = 8),
  1406 (0,8). Schwellenpruefung bis J = 2000 zeigte -0,3 bei J > 1200: **Quadraturartefakt** (700 Gauss-Punkte sind
  nur bis Polynomgrad 1399 exakt, der Integrand hat Grad ~2J); siehe R6.
- R5 (22:45:32-22:46:17, Endpunktordnung (1 - p/q)^4, feineres m-Gitter): c_0 = 895 (q = 0,95), 1031 (q = 0,9),
  1066 (q = 0,9, Schwanzabstand 5), 877 (q = 1). Nachpruefung J <= 400: nur numerische Nullstellen an aktiven
  LP-Bedingungen (relativ -3e-12 bis -1e-8), ausser q = 1 (Schwelle, -0,99).
- R6 (22:47:30-22:47:40, w5c_verify.py, Quadratur mit 2 J_max + 200 Punkten, J <= 3000, 13 Werte von m in [1, 5],
  ++ und +-): q = 0,95/k = 4: schlimmster Fall -2,2e-12 relativ (m = 1, ++, J = 12, aktive Bedingung);
  q = 0,9/k = 4: -1,2e-8; q = 0,95/k = 2: -1,6e-11; q = 1/k = 4: -0,997 bei m = 1, J = 2525 (Schwellenproblem bestaetigt).
- Zwischenergebnis [E]: Ein vorwaertslimesfreies MHV-B2/B3-Funktional mit Glaettung ab p = 0 bis q = 0,95 M ist auf dem
  Gitter (m in [1, 60], J <= 400; Schwelle und m bis 5 fuer J <= 3000; Grenzfall m -> unendlich fuer b <= 600) bis auf
  numerische Nullstellen positiv, mit c_0 = 895. Kein Beweis; Massstab wie CHLPSD Abb. 3 (Gitter plus Asymptotik).

## Weitere Rechnungen (Eintrag 22:53:32)

- R7 (22:48:39-22:49:41) Polynomgrad bei q = 0,95, (1 - p/q)^4: c_0 = 916,6 (N = 8), 895,0 (10), 893,2 (12), 892,6 (14),
  891,2 (16; Box ab N = 12 aktiv). **Plateau bei ~890** [E]. Nachpruefung J <= 400: nur numerische Nullstellen
  (bis -5e-7 relativ bei N = 16, m = 7,06, J = 82).
- R8 (22:50:59, alle drei Laeufe laut kleintest-Kopfzeilen 20:50:59 UTC) w5d_materie.py: Selbsttest reproduziert CHLPSD (3.9) fuer F_g3 exakt (12,338; -13,278; -41,931; 82,455
  und 12,338; 0,0556), **aber nur mit dem Faktor (m_l^4 - 6 m_l^2 p^2 + 6 p^4)**; gedruckt ist in (3.8a,b)
  (m_l^2 - 6 m_l p^2 + 6 p^4), ein Druckfehler [E]. Bestes Funktional (q = 0,95, N = 10): Wirkung auf leichte Materie
  Spin 0 >= 0,119, Spin 2 (mal m_l^4) >= 0,0020 bei m_l = 0,825. Also F_matter >= 0: die Schranke gilt auch mit
  leichten Spin-0/2-Zustaenden unter M (Gitter m_l in [1e-3, 1]).
- Bestes Funktional (Datei code/laeufe/lpq4_N10_q095_d1.out, sha256 in code/laeufe/SHA256SUMS.txt), u = p/q, q = 0,95 M:
  psi2 = (1-u)^4 sum_{n=1..10} a_n u^n, psi3 = (1-u)^4 sum_{n=1..10} b_n u^n,
  a = (1; 3,5; -6,3633; -103,657; 864,201; -3276,49; 7323,45; -9175,15; 5979,66; -1301,18),
  b = (-0,088454; -0,353816; 44,3669; -67,3933; 137,491; -867,667; 4637,25; -10726,5; 11513,6; -4343,77).
  IR-Seite: x <= 894,97 log(M/E) - 1432,1 (die Konstante ist in M_E nicht kontrolliert).

## W2 Ordnungszaehlung unter S (Eintrag 22:53:32) [ES, gestuetzt auf die genannten Gleichungen]

Bezeichnungen (M = 1): g = G M^2 -> 0, L = log(M/E) -> unendlich, G_E = g L fest, y = g x = xi G_E fest.
IR-Seite des Funktionals F = Int_E^q dp [psi2 B2^(1) + psi3 B3^(1)], psi2 ~ a1 p:

| Nr. | Term (Quelle) | nach Glaettung | Ordnung unter S |
|---|---|---|---|
| 1 | GR-Pol 16 pi G/p^2 (CHLPSD 2.31a) | 16 pi G (a1 L + c0) | 16 pi a1 G_E fuehrend; 16 pi c0 g Rest |
| 2 | g^3 in B2: 2 pi G x p^6 (2.31a) | 2 pi G x Int psi2 p^6 | y, fuehrend |
| 3 | g^3 in B3: -2 pi G x p^4 (2.31b) | -2 pi G x Int psi3 p^4 | y, fuehrend |
| 4 | Kontakte g4, g5, ... in B2/B3 | keine (Superkonvergenz, (2.30)-(2.31)) | - |
| 5 | GR-Ein-Schleife, universeller IR-Teil (FRS F.3; Analogon BBIRRS 7.4) | G^2 L^2 + G^2 L + G^2 | G_E^2 fuehrend (berechenbar); g G_E, g^2 Rest |
| 6 | dasselbe in B3 | vollsymmetrisch in s,t,u, faellt in der s<->t-antisymmetrischen B3-Regel heraus | - |
| 7 | gemischt: g^3-Austausch mal weiches Graviton (Pol-Residuum ~ p^6, kein 1/p^2) | G^2 x L + G^2 x | y G_E fuehrend; g y Rest |
| 8 | vier R^3-Vertices (Zweigraviton-Zustaende) | (G x)^2/(16 pi^2) | y^2/(16 pi^2) fuehrend, ohne IR-Log |
| 9 | Kontakt-Schleifen (g4 ~ y) | y^2/(16 pi^2) | fuehrend, berechenbar bei gegebenen Kontakten |
| 10 | linear in g^3 (g- und h-Amplitude, (2.7b,c), CEMZ-artig) | G g^3 = sqrt(g y) | kommt in reinen MHV-B^(1)-Funktionalen nicht vor; sonst O(sqrt(g)) |
| 11 | Glaettungsluecke q < E (BBIRRS 5.10, 5.11) | O(G) ohne Log | Rest |
| 12 | delta_sub.soft (BBIRRS 2.5, 4.2) | relativ O(G) | Rest |
| 13 | Negativitaet grosser l (BBIRRS S. 17-18, 30) | O(G) | Rest |
| 14 | leichte Materie (CHLPSD 3.8) | F_matter >= 0 (R8) | verschaerft die Schranke |

UV-Seite: fuehrende Ordnung nach BBIRRS (5.7)-(5.9), (5.13): positiv, wenn das bis p = 0 fortgesetzte Funktional auf allen
schweren Zustaenden (m >= M, alle J, ++ und +-) positiv ist; das ist CHLPSD's Test mit m_IR = 0 (R6, R7).
Ergebnis fuehrende Ordnung: 16 pi a1 G_E - 2 pi K y + O(G_E^2, y G_E, y^2) >= 0, Rest O(g).
Also y <= (8 a1/K) G_E [1 + O(G_E) + O(y/16 pi^2)] + O(g), d. h. **x <= c_0 log(M/E) [1 + O(G_E)] + O(1)**,
c_0 = 8 a1/K. Mit dem Funktional aus R5/R6: c_0 = 895.

## W3 Scheiterregel (Eintrag 22:53:32)

- Nicht log-verstaerkte Ein-Schleifen-Reste des B2-Smearings: G^2 L = g G_E und G^2 = g^2 -> relativ O(g), also O(G)
  im Sinn der Regel. Erster Zweig der Regel: Schranke in fuehrender Log-Ordnung ohne neue Annahme.
- Doppel-Logs aus FRS (F.3) [E, von Hand]: Mit L_x = log(|x|/E^2) = 2L + l_x und s + t + u = 0 hebt sich im Realteil
  (physikalische Kinematik) das L^2 heraus: Re[...] = -2L (s l_s + t l_t + u l_u) + O(l^2); Imaginaerteil
  2 pi L s - pi (t l_u + u l_t) (Coulomb-Phase). Im B2-Smearing laeuft aber l_t = log(p^2/M^2) bis -2L, und der
  1/t-Pol macht daraus nach Glaettung G^2 L^2 = G_E^2 (Tabelle Nr. 5). Diese Terme tragen also ein log(M/E) in den
  fuehrenden Koeffizienten, aber nur relativ O(G_E), und sie sind EFT-berechenbar (universelle IR-Struktur). Sie liegen
  in der fuehrenden Ordnung, wo BBIRRS die Positivitaet sichern, nicht im unkontrollierten Rest. Der Scheiterfall der
  Regel ("haengt an Termen, die M_E nicht kontrolliert") tritt deshalb nicht ein; c haengt aber von G_E ab:
  c(G_E) = c_0 (1 + O(G_E)). Literaturabgleich: BBIRRS (7.5) rechnen genau diesen Typ fuer pi0 pi0 aus
  (8 pi G_E - (8 pi G_E)^2/(2 pi^2)) [S]; Chang/Parra-Martinez (5.14)-(5.15): Doppelpol 1/(D-4)^2 bei einer Schleife,
  "the G -> 0 limit and the D -> 4 limit do not commute" [S].

## W4 Spin-4-Luecke ohne Mehrgraviton-Kontinuum (Eintrag 22:53:32) [ES]

- M := EFT-Grenze. Unter M rechnet die EFT (GR + R^3 + Kontakte + leichte Materie) mit Schleifen; darin liegen die
  Mehrgraviton-Zustaende (unter S schon auf fuehrender Ordnung: Nr. 8). Ueber M gehen alle Zwischenzustaende X,
  Ein- und Mehrteilchen, mit positiver Dichte in die UV-Seite (CHLPSD (2.13) "X runs over intermediate states",
  BBIRRS (5.8)). Eine eigene "leichteste Spin-4-Masse" wird nicht gebraucht.
- Inhalt der Schranke damit: Bei |g^3|^2 M^8 > c log(M/E) + O(1) kann die EFT nicht bis M gelten; Spektralgewicht
  jenseits der EFT (schwere J >= 4 oder Mehrteilchenzustaende nicht-EFT-Felder, CHLPSD S. 25, 34) muss bei m <= M liegen.
- Achtel-Potenz: c = 895 statt 24,9 schwaecht die Massenschranke nur um (895/24,9)^(1/8) = 1,57 [E].

## W5e Vorwaertslimites in M_E (Eintrag 22:53:32) [ES, grob, nicht nachgerechnet]

- Exakte Vorwaertslimites (d/dp^2 B4 bei p = 0, verbesserte Regeln (3.11)-(3.13)) sind nicht gleichmaessig kontrolliert:
  die Ein-Schleifen-GR-Glieder gehen wie log(-t/E^2)/t (FRS (F.7)), die UV-Eikonalseite oszilliert bei t -> 0.
- Naeherung ueber schmale Glaettung bei E << E' << M: Taylorfehler O(E'^2) gegen Schleifenfehler O(g G_E/E'^4) bei
  einer Ableitung -> bester Fehler O((g G_E)^(1/3)) in y, also O(L^(2/3)) in x; bei zweiten Ableitungen
  (verbesserte Regeln) etwa O(L^(3/4)). Damit koennte c -> 24,9 (CHLPSD (4.4)) erreichbar sein, aber mit Rest o(L)
  statt O(1). Nicht gezeigt.
- CHLPSD (3.4a) ist als Beispiel ungeeignet: g5 fehlt (R1). (4.4) nutzt verbesserte Regeln und ist davon nicht betroffen.

## W8 Gegensweep (Abrufe 22:40-22:53, Eintrag 22:54:56)

Abrufe (WebFetch): arXiv-Versionen 2201.06602 (nur v1, 17.01.2022, kein Kommentar); Semantic Scholar Zitate von
2512.13780 (leer) und 2603.15755 (2: 2604.15235, 2606.19283); INSPIRE refersto:recid:3093263 (BBIRRS, 23 Treffer wie
am 01.10.) und refersto:recid:2012035 (CHLPSD, 195; die neuesten 25 Titel); arXiv-API Volltextsuche
abs:graviton AND positivity AND infrared (16 Treffer); Abstracts 2604.15235, 2606.19283, 2606.19432, 2609.09282,
2607.16179, 2212.04975, 2007.12667, 2011.11652, 2408.06440, 2609.16896, 2604.22916, 2607.05503 [L?].
Lokal gelesen [S]: Chang/Parra-Martinez 2501.17949v2 Abschn. 5 (txt Z. 2004-2240); BBIRRS Abschn. 7-8 (S. 27-32).

- G1 (staerkste Gegenposition, Grenzwerte vertauschen nicht): Chang/Parra-Martinez Abschn. 5.2 [S]: bei einer Schleife
  Doppelpol 1/(D-4)^2 statt 1/(D-4); "the G -> 0 limit and the D -> 4 limit do not commute"; mit der Annahme, dass die
  Eikonalformel das Vorwaertsverhalten in allen Ordnungen in G traegt, endliche D = 4-Schranken ohne IR-Log (Abstract).
  BBIRRS S. 30-31 [S] deuten solche Schranken bei festem G als triviale Aussagen ("g2 M^4 x 0 + 259 >= 0") und
  sagen, bei G_E -> unendlich trivialisierten die Schranken (S. 30). Folge fuer uns: x <= c log(M/E) ist nur fuer
  G_E klein bis O(1) eine Aussage; c haengt von G_E ab; bei festem G und E -> 0 gilt sie nicht weiter.
- G2 (IR-Skala ueberhaupt): Lippstreu 2609.16896 [L?]: Standardverfahren liefern Schranken mit willkuerlicher IR-Skala; in
  einem nichtrelativistischen Modell hat die exakte Schranke keine; DWPT. Gegen M_E nur bedingt: dort ist E die
  physikalische Detektoraufloesung, gewollt.
- G3 (Vorwaertslimes mit Graviton): Alberte/de Rham/Jaitly/Tolley 2007.12667 [L?]: Standardschranken mit Gravitation
  "inapplicable" (t-Pol-subtrahiert); Herrero-Valea u. a. 2011.11652 [L?]: Vorwaertsschranken brauchen Aufhebung von
  1/t und log t, moeglich nur mit Regge-Annahme unter der Planckskala. Stuetzt E2: exakte Vorwaertslimites sind der
  schwache Teil, nicht die verschmierten B2/B3-Regeln.
- G4 (Regge): de Rham/Jaitly/Tolley 2212.04975 [L?]: Regge-Verhalten wird durch IR-Physik eingeschraenkt; Haering/
  Zhiboedov (d > 4) nur ueber BBIRRS S. 7-8 [S]. Die M_E-Regge-Aussage (3.12) ist fuer "neutral massless particles"
  hergeleitet; fuer Helizitaetsamplituden nicht eigens.
- G5 (Literaturstand g^3 in D = 4 IR-sicher): In den geprueften Quellen (Titel/Abstracts der 23 BBIRRS-Zitate, 25
  neueste CHLPSD-Zitate, 2 FRS-Zitate, 16 Suchtreffer; Volltexte FRS, BBIRRS, CPM, CHLPSD) nicht gerechnet.
  2609.16896 (DWPT) und 2606.19432 (Partialwellen mit Langreichweite) sind naechste Nachbarn, nur Abstracts gelesen.

## Erwartungen gegen Ausgang (Eintrag 22:54:56)

| Erwartung (22:31:10) | Ausgang |
|---|---|
| E1 x-Terme unter S fuehrend, BBIRRS-Positivitaet greift (~60 %) | bestaetigt [ES] (W2) |
| E2 exakte Vorwaertslimites nicht gleichmaessig kontrolliert (~70 %) | bestaetigt [ES]; neu: genaeherte Vorwaertslimites mit Rest o(L) (W5e) |
| E3 (3.7) gibt 1598 und ist positiv (~60 %) | teilweise verletzt: 1596,7 reproduziert; +- an der Schwelle m = M stark negativ (Rundungsrest psi3(1) = 0,03 und Schwellenstruktur) |
| E4 LP: c_0 zwischen 100 und 1000, nicht unter 75 (~50 %) | bestaetigt: 891-1031, Plateau ~890 |
| E5 Doppel-Logs fuehrend, berechenbar, relativ O(G_E); Rest O(G) (~65 %) | bestaetigt [ES/E]; zusaetzlich: L^2 hebt sich im Realteil heraus, kehrt im B2-Smearing ueber l_t zurueck |
| E6 Gesamt: A mit c >> 75 (40 %) | eingetreten (vorlaeufig, Gegenlesung aussteht) |

Nicht vorhergesagt: (i) CHLPSD (3.4a,b) lassen g5 aus; (ii) Druckfehler in CHLPSD (3.8a,b); (iii) die Schwellenecke
m = M, J gross bei Glaettung bis p = M; (iv) FRS (F.10) dimensional unstimmig (von Hand: rechte Seite ~ M^-6, g4_F ~ M^-4
nach (2.3); erwartet waere log^2(q/E)/(q^2 s), vgl. (4.41)) - Nebenbefund, nicht tragend.

## Einordnung und Abschluss (Eintrag 23:03:40)

- ERGEBNIS.md geschrieben ab 22:55:46, danach berichtigt (Sicherung ERGEBNIS.md.bak-*): Punkt 2 Plateau-Angabe, Punkt 3
  B4-Aussage genauer (exakte Vorwaertslimites gegen verschmiertes B4), Tabellen-Pipes, Regge-Zitat (Eikonalform
  (3.10)-(3.11) statt "neutral massless particles", das steht bei (4.12)), CPM-Seiten, Zahl G M^2 (3e-76 statt 1e-77),
  schlimmster Fall der Nachpruefung (-1,2e-10 statt -2e-12), q_max-Grenze ergaenzt.
- Klasse A (vorlaeufig) nach den eingefrorenen Kriterien PLAN Abschnitt 5, c = 895 in CHLPSD-Normierung.
- Pruefung auf absolute Aussagen (nie/immer/nur) im ERGEBNIS: "B4 nicht gebraucht" (wahr fuer das Funktional),
  "exakte Vorwaertslimites nicht gleichmaessig kontrolliert" ([ES], FRS (F.7)), "in diesen Quellen nicht gerechnet"
  (auf die genannten Quellen begrenzt), "nur auf Gittern" (wahr).
- R9: w5c_verify bei grossen Massen m = 5, 7, 10, 15, 20, 30, 40, 60, J <= 3000, feine Quadratur. Erster Start 23:01:29
  auf Spur cpu wartete hinter einem fremden Lauf (r23sg-A015) im Lock; ich habe nur meine eigenen wartenden Prozesse
  (PID 2008294, 2008296, 2008299, per ps -p geprueft) beendet und auf cpu4 neu gestartet: 23:05:53-23:06:00.
  Ergebnis: ueberall positiv, schlimmster Fall +1,5e-7 relativ (m = 5, ++, J = 3000).
