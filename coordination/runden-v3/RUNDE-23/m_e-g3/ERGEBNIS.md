# ERGEBNIS M_E-G3: IR-endliche Schranke fuer die Graviton-Dreipunktkorrektur in D = 4

- Karte: RUNDE-16/m_e-g3/KARTE.md (mit Nachtrag "Ausfuehrender gewechselt"). Ausfuehrender: Anthropic-Agent (Opus 5.5).
- Plan eingefroren: PLAN.md.eingefroren-20261002-223215 (sha256 94d373a3...dd5a4b). Protokoll: ARBEITSFELD.md.
- Sitzung 2026-10-02 22:10:55 bis Niederschrift ab 22:55:46 CEST (date). Rechnungen nur auf der .69 ueber kleintest.sh.
- Marken: [S] gelesen, [L?] nur Abstract oder Zitat, [ES] eigener Schluss, [E] eigene Rechnung.
- Abkuerzungen: CHLPSD = arXiv:2201.06602 (v1); BBIRRS = arXiv:2512.13780v2; FRS = arXiv:2603.15755v2;
  CPM = Chang/Parra-Martinez arXiv:2501.17949v2. Seiten = gedruckte Seiten.

## 1. Ergebnis (Klasse A, vorlaeufig; Gegenlesung durch Codex steht aus)

1. **Klasse A:** Fuer die festgelegte Skalierung x = |g^3|^2 M^8 = xi log(M/E) (xi fest, G_E = G M^2 log(M/E) fest)
   liegen die g^3-Terme in der fuehrenden Ordnung, die BBIRRS kontrollieren. Daraus folgt ohne neue physikalische
   Annahme **x <= c log(M/E) (1 + O(G_E)) + O(1)**, mit Rest O(G M^2) in BBIRRS' Sinn (Gl. (5.16)-(5.17)). Die dafuer
   benutzten Uebertragungen des BBIRRS-Rahmens auf aeussere Gravitonen sind in Abschnitt 5 einzeln genannt.
2. **c = 895** in CHLPSD-Normierung, aus einem ausdruecklich konstruierten, verschmierten B2^(1)/B3^(1)-Funktional ohne
   Vorwaertslimes (LP; Polynomgrad 10 bis 16 ergibt 895 bis 891, ein Plateau). Positivitaet auf schweren Zustaenden und leichter
   Materie nur numerisch auf Gittern geprueft (Massstab wie CHLPSD Abb. 3), kein Beweis [E].
3. **Ein B4-Anteil wird fuer die Schranke nicht gebraucht.** Mit exakten Vorwaertslimites ist er in M_E nicht
   gleichmaessig kontrolliert, weil die Ein-Schleifen-Glieder wie log(-t/E^2)/t gehen (FRS (F.7)); verschmiert bringt
   er g4 und (4 pi G x + g5) untrennbar mit (CHLPSD (2.32a)) [ES]. Gerade dieser Anteil macht CHLPSDs Koeffizienten
   klein (24,9 in (4.4); in (3.3a) traegt -5 d/dp^2 B4 rund 73 % des x-Koeffizienten [E]). Ueber genaeherte
   Vorwaertslimites koennte c gegen 24,9 gehen, dann aber mit Rest o(log) statt O(1) [ES, nicht gezeigt].
4. **Scheiterregel des Vorlaeufers:** erster Zweig. Die nicht log-verstaerkten Ein-Schleifen-Reste bleiben O(G). Die
   Doppel-Logs aus FRS (F.3) gehoeren unter dieser Skalierung zur fuehrenden, berechenbaren Ordnung und aendern c nur um
   einen relativen Anteil O(G_E). Sie sind kein Unitaritaetsrest.
5. **Gegen die Vorhersage der Leitung:** Klasse A hatte 10 %. Die Folgevorhersage (Form + O(1) und c innerhalb Faktor 3
   von 24,9) ist **nicht getroffen**: belegt ist c = 895 = 36 x 24,9; c ~ 24,9 nur ueber einen nicht gezeigten Weg mit
   schwaecherem Rest o(log). Fuer die Massenschranke ist der Unterschied mild: (895/24,9)^(1/8) = 1,57 [E].

## 2. Normierungswoerterbuch g3 (Auflage A2)

| Groesse | CHLPSD [S] | FRS [S] |
|---|---|---|
| Kinematik | mostly plus, s = -(p1+p2)^2, t = -(p2+p3)^2, u = -(p1+p3)^2, Gl. (2.4) | alle einlaufend, s = (p1+p2)^2, t = (p1+p3)^2, u = (p1+p4)^2, nach Gl. (2.3) |
| GR-Austausch MHV | <23>^4 [14]^4 x 8 pi G/(stu), Gl. (2.1), (2.7a) | <23>^4 [14]^4/(M_Pl^2 stu), Gl. (2.6) |
| Dreipunkt (+++) | (g^3/2) sqrt(8 pi G) ([12][13][23])^2, Gl. (2.6); g^3 = alpha3 + i alpha~3, Gl. (2.11) | g3 [12]^2[23]^2[13]^2/M_Pl^3, S. 9 |
| g3-Glied MHV | 2 pi G \|g^3\|^2 su/t, Gl. (2.7a) | M_Pl^-4 (g3^2/M_Pl^2) st/u, Gl. (2.3) |
| Spin-4-Regel | -B4^(1)\|low = 2 g4 + (4 pi G \|g^3\|^2 + g5) p^2, Gl. (2.32a) | M_Pl^4 B_0^4h\|tree = g4 - (g3^2/M_Pl^2 + g5/2) t, Gl. (4.39) |

Abbildung [E, von Hand, zweifach geprueft]:
- s_F = s_C, t_F = u_C, u_F = t_C. M_Pl^-2 = 8 pi G (reduzierte Planckmasse). Zwei unabhaengige Proben: GR-Glied (2.6)
  gegen (2.7a); Weinberg-Exponent FRS (F.1), Vorfaktor 1/(8 pi^2 M_Pl^2), gegen BBIRRS (3.7), G s_ij/(4 pi) je
  geordnetem Paar.
- **|g^3|^2 = 4 |g3_FRS|^2/M_Pl^4 = 4 (8 pi G)^2 |g3_FRS|^2**, also |g^3| = 2 |g3_FRS|/M_Pl^2 (auch aus den
  Dreipunktamplituden). g4_C = (8 pi G)^2 g4_F, g5_C = (8 pi G)^2 g5_F.
- Probe: (2.32a) in FRS-Groessen ist 2 x (4.39)/M_Pl^4, also B_0^4h(FRS) = -B4^(1)(CHLPSD)/2.
- x = |g^3|^2 M^8 = 4 (g3_FRS M^2)^2 (8 pi G M^2)^2. Bei festem g^3 (CHLPSD) haengt x nicht von G ab; bei festem g3_FRS
  (FRS, natuerlich g3 ~ 1/(g* M)^2) geht x wie G^2 gegen null. FRS schreiben g3^2; da das MHV-Glied aus (+++) x (---)
  entsteht, ist |g3|^2 gemeint [ES].
- Die Skalierung unten in FRS-Groessen: g3_FRS/M_Pl^3 fest, also eine endliche R^3-Dreipunktkopplung bei G -> 0.

## 3. Summenregeln und Funktionale

**Festgelegte Skalierung S** (vor der Rechnung eingefroren): G -> 0, E -> 0, G_E = G M^2 log(M/E) fest (BBIRRS (1.1)) und
xi = x/log(M/E) fest. Gleichwertig y := G M^2 x = xi G_E fest: die R^3-Kopplung bleibt als kurzreichweitige Kopplung
endlich, wie die Pion-Kopplungen bei BBIRRS ("all orders in G_E and any other short-distance coupling, while
perturbatively in G", S. 10 [S]).

**Regeln (M = 1)** [S]: -B2^(1)|low = 16 pi G/p^2 + 2 pi G x p^6, -B3^(1)|low = -2 pi G x p^4 (CHLPSD (2.31a,b)), ohne
Kontaktglieder (Superkonvergenz, (2.30)). Schwere Seite (2.33), (2.35a): B2 ~ (2m^2 - p^2)(|c++|^2 d00~ + |c+-|^2 d44~)/m^6,
B3 ~ (|c++|^2 d00~ - |c+-|^2 d44~)/m^6, d00~ = P_J, d44~ = P^(0,8)_{J-4} (Anh. A), x = 1 - 2p^2/m^2.

**M_E-Form** [ES]: IR-Seite mit Glaettung p in [E, q], UV-Seite mit derselben Funktion ab p = 0 (BBIRRS (5.9): harte
Amplituden tragen keine Gravitonen mit q < E; Luecke (5.10) ist O(G), nicht log-verstaerkt). Positivitaet der UV-Seite
in fuehrender Ordnung (BBIRRS (5.7), (5.13)) heisst dann: das Funktional ist auf allen schweren Zustaenden positiv,
genau CHLPSDs Test mit m_IR = 0. IR-Seite: 16 pi (a1 log(M/E) + c0) - 2 pi K x mit psi2 ~ a1 p,
K = Int (psi3 p^4 - psi2 p^6), also x <= (8 a1/K) log(M/E) + ...

**Was konstruiert wurde** [E] (code/, Laeufe mit sha256 in code/laeufe/SHA256SUMS.txt):
- Nachrechnung CHLPSD: (3.3a) -> 37,839 log - 45,445, also (3.4a), **aber nur ohne g5**; mit g5 kommt -0,0579 g5 M^10/G
  hinzu. Ebenso fehlt g5 in (3.4b). (3.7) -> 1596,7 log - 3208 (Quelle 1598, -3211; gerundete Koeffizienten).
- (3.7) ist in der gedruckten Form an der Schwelle m = M bei grossem J im +- -Kanal nicht positiv (relativ -0,99 bei
  J = 198): Rundungsrest psi3(1) = 0,03 und eine Strukturfrage. Bei Glaettung bis p = M erreicht die Welle mit m = M die
  Rueckwaertsrichtung, wo d44~ wie J^8 waechst [ES, Asymptotik im ARBEITSFELD R3]. F_g3 (3.3a) ist positiv (meine
  Umsetzung bestaetigt CHLPSD Abb. 3), weil -5 d/dp^2 B4 dort +10 J^2 beitraegt.
- **Neues Funktional** (LP, maximiere K bei a1 fest; psi3(0) = 0; Bedingung 2 m^2 psi2_2 +- psi3_2 < 0 fuer den
  Grossb-Schwanz; Glaettung bis q = 0,95 M nach dem Muster von FRS (4.23), (4.27)): psi2 = (1-u)^4 sum a_n u^n, psi3 = (1-u)^4 sum b_n u^n,
  u = p/q, n = 1..10, Koeffizienten im ARBEITSFELD. Ergebnis **x <= 895,0 log(M/E) - 1432** (Konstante in M_E nicht
  kontrolliert). Polynomgrad 8/10/12/14/16: 916,6/895,0/893,2/892,6/891,2.
- Pruefungen: LP-Gitter m in [1, 40], J <= 400, Grenzfall m -> unendlich fuer b <= 400; Nachpruefung m in [1, 60],
  J <= 400; feine Quadratur (6200 Punkte) bei 13 Massen in [1, 5] und 8 Massen in [5, 60] bis J = 3000; leichte
  Materie Spin 0 und 2, m_l in (0, M]. Schlimmster Fall -1,2e-10 relativ (numerische Nullen an aktiven LP-Bedingungen).
  Wirkung auf leichte Materie positiv (Spin 0 >= 0,119; Spin 2 >= 0,0020/m_l^4), also gilt die Schranke auch mit
  leichten Spin-0/2-Zustaenden.
- Nebenbefund: CHLPSD (3.8a,b) haben einen Druckfehler; nur mit (m_l^4 - 6 m_l^2 p^2 + 6 p^4) statt
  (m_l^2 - 6 m_l p^2 + 6 p^4) wird (3.9) exakt reproduziert [E].

**Was nicht konstruiert wurde:**
- kein Funktional mit B4-Anteil in kontrollierter M_E-Form; kein Funktional mit c in der Naehe von 24,9;
- keine Ein-Schleifen-Rechnung der fuehrenden O(G_E)-Korrektur zu c (berechenbar; Muster BBIRRS (7.4)-(7.5));
- kein Positivitaetsbeweis (nur Gitter plus Asymptotik).

**Spin-4-Luecke ohne Mehrgraviton-Kontinuum** [ES]: M ist die EFT-Grenze. Unter M stehen Mehrgraviton-Zustaende in den
EFT-Schleifen (unter S schon fuehrend: Zweigraviton-Zustaende ueber R^3 ~ y^2/16 pi^2); ueber M gehen alle Zwischenzustaende
mit positiver Dichte in die UV-Seite (CHLPSD (2.13), BBIRRS (5.8)). Eine "leichteste Spin-4-Masse" wird nicht gebraucht.
Die Schranke sagt dann: Spektralgewicht jenseits der EFT muss bei m <= M liegen, mit
M^8 <= (895 log(M/E) + O(1))/|g^3|^2.

## 4. Fehlerbudget und Scheiterregel

Ordnung unter S (M = 1, g = G M^2) [ES]; Einzelheiten in ARBEITSFELD W2:

| Term | Quelle | Ordnung | Status |
|---|---|---|---|
| GR-Pol, Log-Teil | CHLPSD (2.31a) | G_E | fuehrend, Baum |
| g^3-Glieder in B2, B3 | (2.31a,b) | y | fuehrend, Baum |
| GR-Ein-Schleife, Doppel-Log | FRS (F.3); BBIRRS (7.4) | G_E^2 | fuehrend, berechenbar, nicht gerechnet |
| gemischt g^3 x weiches Graviton | [ES] | y G_E | fuehrend, berechenbar |
| vier R^3-Vertices, Kontakt-Schleifen | [ES] | y^2/16 pi^2 | fuehrend, berechenbar |
| GR-Pol, Konstante | (2.31a) | g | Rest |
| GR-Ein-Schleife, ein Log oder keiner | FRS (F.2)-(F.3) und nicht-universeller Rest | g G_E, g^2 | Rest |
| Glaettungsluecke q < E | BBIRRS (5.10)-(5.11) | g | Rest |
| delta_sub.soft | BBIRRS (2.5), (4.2) | g | Rest |
| Negativitaet grosser l | BBIRRS S. 17-18, 30 | g | Rest |
| lineare g^3-Glieder (CEMZ-artig) | CHLPSD (2.7b,c) | sqrt(g) | in reinen MHV-Funktionalen abwesend |

Folge: y <= (8 a1/K) G_E [1 + O(G_E) + O(y/16 pi^2)] + O(g), also x <= c_0 log(M/E) (1 + O(G_E)) + O(1), c_0 = 895.
Fuer log(M/E) <~ (G M^2)^(-1/2) ist auch der O(G_E)-Term O(1), dann gilt x <= 895 log(M/E) + O(1) mit dem
Baumkoeffizienten. Realistisch ist G M^2 winzig (fuer M ~ 1/km etwa (l_Pl/1 km)^2 ~ 3e-76 [E]), G_E also vernachlaessigbar.

**Scheiterregel (SPIN2-D4-2, "Weg und fehlende Rechnung"):**
- Nicht log-verstaerkte Ein-Schleifen-Reste des B2-Smearings: G^2 log(M/E) = g G_E und G^2 sind relativ O(G M^2).
  Sie bleiben O(G). -> erster Zweig: Schranke in fuehrender Log-Ordnung ohne neue Annahme.
- Doppel-Logs FRS (F.3) [E, von Hand]: Im Realteil hebt sich log^2(M/E) wegen s + t + u = 0 heraus
  (Re = -2 L (s l_s + t l_t + u l_u) + ..., l_x = log(|x|/M^2)); im B2-Smearing kehrt es ueber l_t = log(p^2/M^2) und den
  1/t-Pol zurueck: G^2 log^2(M/E) = G_E^2. Das ist fuehrende, berechenbare Ordnung (wie BBIRRS (7.5) fuer pi0 pi0 und
  CPM (5.14)-(5.15) mit dem Doppelpol 1/(D-4)^2). c haengt dadurch von G_E ab, aber nicht von unkontrollierten Termen.
- Gegenprobe ohne S (x fest): Dann sind alle g^3-Glieder O(G M^2) und liegen im Rest; die Ungleichung
  x <= 895 log(M/E) + O(1) bleibt wahr, ist dort aber leer. Der Vorlaeufer hatte fuer diesen Fall recht; seine
  Kurzfazit-Aussage "nur mit neuer Annahme" war fuer x ~ log(M/E) zu stark (wie Codex-Auflage A1 vermutete).

## 5. Einordnung gegen die Vorhersage der Leitung

- Klassen: Vorhersage A ~10 %, B ~35 %, C ~45 %, D ~10 %. Ausgang **A** (vorlaeufig), nach meinen vor der Rechnung
  eingefrorenen Kriterien (PLAN Abschnitt 5): (i) x-Terme unter S fuehrend, (ii) ausdrueckliches, zulaessiges
  Funktional mit gepruefter Positivitaet, (iii) Rest gleichmaessig O(G M^2) fuer (G_E, xi) kompakt, (iv) keine Annahme
  ueber CHLPSD und BBIRRS hinaus.
- Folgevorhersage (Form x <= c log(M/E) + O(1) **und** c innerhalb Faktor 3 von 24,9, ~50 %): **nicht getroffen**.
  Belegt ist die Form mit c = 895 (CHLPSD-Normierung), Faktor 36. In FRS-Groessen: 4 |g3_FRS|^2 M^8/M_Pl^4 <=
  895 log(M/E) + O(1).
- Offener Gegenweg [ES, nicht gezeigt]: Im strengen Grenzfall (erst S, dann Vorwaertslimes an der Grenzamplitude M^(0),
  deren Ein-Schleifen-Singularitaet bei festem t mit G verschwindet) waere CHLPSDs Funktional zu (4.4) wieder anwendbar,
  also c -> 24,9 bei G_E -> 0. Der Rest faellt dann aber nur wie o(log(M/E)) (genaeherte Vorwaertslimites, ARBEITSFELD
  W5e), und die Positivitaet an der Schwelle m = M bei J >~ M/E' muesste neu geprueft werden. Dann waere c getroffen, die
  Form "+ O(1)" nicht.
- Warum so gross: Das in M_E kontrollierbare Funktional hat nur die B2/B3-Glieder mit p^6- und p^4-Gewicht. CHLPSDs
  kleine Koeffizienten kommen aus Vorwaertslimites (d/dp^2 B4, verbesserte Regeln), und die sind in M_E der unsichere Teil.
- Benannte Uebertragungen aus BBIRRS (Teil des Rahmens, keine neue Annahme, aber nicht eigens bewiesen):
  - funktionale Unitaritaet (4.10) und Positivitaet (5.7) fuer aeussere Gravitonen mit Helizitaet: bei BBIRRS "An analogous
    statement holds in gravity" (S. 11, 12), harter Hamiltonoperator mit h = +-2 (S. 10); FRS nutzen es (S. 46);
  - Regge-Verhalten (3.12) fuer M_E: hergeleitet ueber die Eikonalform (3.10)-(3.11) (S. 7-8); fuer Helizitaetsamplituden
    nicht eigens gezeigt (Codex-Auflage A5). Die B2^(1)-Regel braucht genau den Fall n = 0 von (3.12) [ES];
  - die R^3-Kopplung des Gravitons selbst als kurzreichweitige Kopplung (meine Uebertragung [ES]; weiche Faktoren bleiben
    universell, R^3-Emission weicher Gravitonen ist impulsunterdrueckt).
- Was A hier nicht heisst: keine Aussage bei festem G und E -> 0 (G_E -> unendlich), keine kontrollierte Konstante,
  kein Beweis der Positivitaet, keine Aussage zu Glied 7 oder 10 ueber die bedingte CEMZ-Kette hinaus.
- Moegliche Folge fuer WARUM-SPIN-2, nur als Vorschlag und erst nach der Gegenlesung: Die IR-Frage des CHLPSD-Arguments
  in D = 4 ist fuer x ~ log(M/E) in fuehrender Log-Ordnung IR-endlich beantwortbar, mit Koeffizient 895 statt 24,9.
  Die uebrigen Bedingungen bleiben: Unitaritaet, Analytizitaet und Kreuzung, verschmierte Regge-Schranke und der M_E-Rahmen.

## 6. Quellen, Lesetiefe, Grenzen, Selbstanzeigen

Quellen (lokale Dateien per sha256sum -c geprueft, alle OK; Manifeste in RUNDE-13/spin2-d4/quellen/ und
spin2-d4-2/quellen/):
- CHLPSD, arXiv:2201.06602 (nur v1 auf arXiv): [S] Abschn. 2.1-2.5, 3.1-3.5, 4.1-4.2, Anh. A-B; PDF-Bild S. 10-12, 16-17,
  19-20, 38-39.
- BBIRRS, arXiv:2512.13780v2: [S] Abschn. 1-5 (S. 1-18), 7-8 (S. 27-32).
- FRS, arXiv:2603.15755v2: [S] Abschn. 2 (S. 4-9), 4 (S. 24-34), Anh. F (PDF-Bild S. 46-47).
- CPM, arXiv:2501.17949v2: [S] Abstract und Abschn. 5 (S. 31-35, Ausschnitte).
- [L?] nur Abstract: Lippstreu 2609.16896; Plestid/Quilez 2606.19432; Peng/Rodina/Tokareva/Xu 2604.15235; Xu 2606.19283;
  de Rham/Jaitly/Tolley 2212.04975; Alberte u. a. 2007.12667; Herrero-Valea u. a. 2011.11652; Caron-Huot/Li 2408.06440.
- Zitationslage (02.10.2026, 22:40-22:53): BBIRRS 23 INSPIRE-Zitate (wie am 01.10.); CHLPSD 195, die neuesten 25 Titel;
  FRS 2 Zitate (Semantic Scholar). In diesen Quellen ist eine IR-sichere g^3-Schranke in D = 4 nicht gerechnet.

Gegensweep (ARBEITSFELD W8), staerkste Gegenposition: Die Grenzwerte G -> 0 und E -> 0 (bzw. D -> 4) vertauschen nicht
(CPM Abschn. 5.2 [S]). Bei festem G und E -> 0 werden die Schranken nach BBIRRS trivial (S. 30 [S]), nach CPM mit
Eikonal-Annahme endlich und ohne IR-Log. Die hier gefundene Schranke gilt deshalb nur fuer G_E klein bis O(1). Zweitens
(Lippstreu [L?]): Bounds mit willkuerlicher IR-Skala koennten ein Artefakt der Technik sein; in M_E ist E aber die
physikalische Detektoraufloesung.

Grenzen:
- Herleitung ist eine Ordnungszaehlung [ES] auf Grundlage der BBIRRS-Aussagen, kein Satz. Positivitaet nur auf Gittern.
- O(G_E)-Korrekturen zu c nicht gerechnet; ihr Vorzeichen offen.
- Genaeherte Vorwaertslimites (Weg zu c ~ 24,9 mit Rest o(log)) nur grob abgeschaetzt [ES].
- Nur MHV-Regeln B^(1); andere Helizitaeten tragen unter S nur lineare g^3-Glieder (O(sqrt(G))) oder brauchen
  Verbesserung mit Vorwaertslimites.
- BBIRRS formulieren die funktionale Unitaritaet (4.10) fuer "s >> q_max^2" (S. 12) [S]; ihre eigenen Anwendungen
  nutzen q_max = M/2 bzw. M/sqrt(3) (Gl. (A.6), (A.25)) [S]. Ich nutze q = 0,95 M. Die Fehlanpassung (4.8) betrifft nur
  das 1/t-Gebiet q -> 0, deshalb halte ich die Bedingung fuer technisch [ES]; mit q = 0,8 M steigt c auf 1406 (R4).

Selbstanzeigen:
- S1: Einmal Interpreterstart auf der .69 ausserhalb von kleintest.sh (Versionsabfrage scipy/numpy, keine Rechnung).
- S2: Vor dem Einfrieren des Plans habe ich zwei Rechnungen von Hand gemacht (Woerterbuch, (3.3a) -> (3.4a) mit
  g5-Befund). Beide stehen im Plan als "schon gerechnet" (PLAN Abschnitt 0), nicht als Vorhersage.
- S3: Im ARBEITSFELD stand zuerst eine geschaetzte Laufzeit "22:50:0x" (R8); ersetzt durch 22:50:59 aus den
  kleintest-Kopfzeilen.
- S4: Die Schwellenpruefung bis J = 2000 in R4 lief mit zu grober Quadratur (700 Punkte, exakt nur bis Grad 1399) und
  zeigte Scheinnegativitaet; erkannt und mit w5c_verify.py (2 J_max + 200 Punkte) wiederholt (R6).
- S5: Mehrere LP-Varianten mit N >= 12 erreichten die Koeffizientenbox; c aendert sich dort kaum (893 -> 891).
- S6: Ein Pruefauftrag (R9) wartete auf der belegten Spur cpu hinter einem fremden Lauf; ich habe nur meine eigenen
  wartenden Prozesse per PID beendet und auf cpu4 neu gestartet. Fremde Laeufe nicht beruehrt.
- Kein git, kein Peerbus, keine Unteragenten; gesperrte Pfade nicht gelesen; geschrieben nur in RUNDE-23/m_e-g3/ und
  auf der .69 in /home/fmh/fmhc-physics-remote/runde23-m_e-g3/.

## 7. Einfach gesagt

Wir wollten wissen, ob man die besondere Dreifach-Kopplung der Gravitonen auch dann begrenzen kann, wenn man die
Unendlichkeiten in vier Dimensionen ehrlich ueber einen Detektor endlicher Groesse behandelt. Ja: Wenn diese Kopplung so
gross ist, dass sie mit dem Logarithmus der Detektorgroesse mitwaechst, steht sie in der Rechnung ganz vorne, und dort
ist die Methode verlaesslich. Die Grenze ist aber rund 36-mal lockerer als die bekannte Zahl 24,9, weil die Bausteine,
die diese Zahl so klein machen, in der sauberen Methode nicht sicher sind. Fuer die Masse der noetigen neuen Teilchen
macht das wenig aus: Sie duerfen hoechstens etwa 1,6-mal schwerer sein als bisher abgeschaetzt. Das ist unsere eigene
Herleitung mit Computerpruefung, noch kein Beweis, und sie muss erst von Codex gegengelesen werden.
