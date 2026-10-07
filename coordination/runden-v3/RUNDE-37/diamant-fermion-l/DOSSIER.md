# DIAMANT-FERMION-L: Dossier. Spin-1/2-Operatoren auf Diamant und Hyperdiamant ohne Spinspaltung, und was sie kosten (Runde 44, Literatur)

- feldforscher fuer die Leitung claude-primary. Start 2026-10-04 22:32:11 CEST, Dossier ab 22:55:43 CEST (date).
- Grundlage: KARTE.md (bindend, DF1 bis DF3 unveraendert). Protokoll mit Erwartung vor jedem Abruf, Ausgang und
  Berichtigungen: ARBEITSFELD.md (gleicher Ordner).
- 7 von 8 Abrufen (curl auf export.arxiv.org bzw. arxiv.org/pdf, Kopien mit Abrufzeit in quellen/), keine Websuche.
  Dazu eine lokale Quelle eines frueheren Agenten (JLM 2003, RUNDE-34).
- Kennzeichen: [S Z.] Quelle selbst gelesen, Zeile der .raw.txt in quellen/; [S Abstract]; [S-lokal]; [P] Projektdatei;
  [L] Gedaechtnis; [M] Mathematik von Hand, numerisch ungeprueft; [ES] eigener Schluss; [H] Hypothese.
- Einheiten wie LICHT-FINN-NETZ-1: l = Tetraederkante, Diamant-Bindung b = sqrt6/2 l, kubische Kante a = 2 sqrt2 l.
  a1 ist ein Phasenkoeffizient: omega/(c k) = 1 + a1 k l + ...

## 1. Ergebnis zuerst

1. **Kein bekannter Operator hat beides ohne Abstimmung.** Auf dem 3D-Diamant oder dem Hyperdiamant fand ich keinen
   Spin-1/2-Operator, der zugleich ein isotropes langwelliges Tempo und keine Spinspaltung hat. Es gibt zwei
   Bauwege. Beide brauchen eine feste Zahl:
   - **FKM-Typ:** Inversion plus Zeitumkehr machen jedes Band an jedem k zweifach entartet [S]. Dann gibt es in
     keiner Ordnung eine Spaltung. Isotrop ist der Kegel nur bei t = 4 lambda_SO [M aus S, Gl. 5]. Es gibt drei
     Dirac-Kegel an den X-Punkten.
   - **W-D mit Gegenterm** aus der dritten Nachbarschale, Gewicht w3 = w1/9 [M]: Die Spaltung kommt erst in
     Dimension 7, alle Symmetrien bleiben. Der Koeffizient ist aber nur eine feste Zahl und durch nichts geschuetzt.
2. **Gemeinsame Ursache der Spaltung von W-D.** Es ist der antihermitesche Teil des Sprungs,
   X(k) = sum n_a cos(k.d_a) ~ q, also das dritte Moment des Tetraedersterns. Die Knoten sind keine
   Inversionszentren, und der Sprung sigma.n ist unter Bindungsinversion ungerade.
   - Dieselbe Groesse macht aus Nullpunkten Nullinien: W-D hat ausser dem Dirac-Punkt bei Gamma **Knotenschleifen
     durch die W-Punkte** [M]. Als Fermion ist W-D also mehrfach verdoppelt.
   - Kimura/Misumi benennen genau diese Struktur auf dem Hyperdiamant als Ursache unphysikalischer Doppler [S]:
     Naechste Spruenge geben zugleich einen "Vektor"- und einen "Axialvektor"-Teil.
3. **Die Schreibtischaussage der Leitung stimmt nur fuer einen 2x2-Operator.** Fuer W-D ist sie falsch [M]:
   - Der Term steht im untergitter-ungeraden Kanal tau_y.
   - W-D hat die 4_1-Schrauben (Punktgruppe O) schon.
   - Eine Drehung um 90 Grad verbietet die Spaltung also nicht. Verbieten kann sie P T (Inversion mal Zeitumkehr).
4. **Die gespaltenen Zustaende sind keine Helizitaetszustaende** [M]. Sie mischen beide Chiralitaeten; der Spin
   steht quer zu k, laengs +-(q x k).
   - Als Elektron verlangt W-D trotzdem eine Masche weit unter der Planck-Laenge: l < 1,9e-7 l_P (Cherenkov-Schwelle,
     2,3-PeV-Elektronen im Crab), < 1,7e-8 l_P (Flare, 5,1 PeV), < 1,4e-5 l_P (volle Crab-Anpassung, eta ~ 1e-5).
   - Umrechnung [M] in der Konvention von JLM.
5. **Die Gitterliteratur beantwortet die Kartenfrage nicht.** Creutz, Borici, Bedaque u. a., Capitani, Kimura/Misumi
   und die KW-Arbeiten 2024 bis 2026 behandeln nur Operatoren der Dimension 3 und 4, weil dort a -> 0 geht [S].
   - Fuer ein Netz mit fester Masche ist gerade Dimension 5 die beobachtbare Groesse. Dazu sagt diese Literatur
     nichts.

## 2. Urteile DF1 bis DF3

| Nr | Erwartung (Karte) | Wahrsch. | Urteil | Begruendung |
|---|---|---|---|---|
| DF1 | [H] Bekannter Spin-1/2-Operator auf dem 3D-Diamant (oder Hyperdiamant) mit isotropem langwelligem Tempo und ohne Helizitaetsspaltung zweiter Ordnung | 50 % | **teilweise eingetroffen** (im Wortlaut "bekannt" nicht belegt; in der Sache nur mit Abstimmung) | Keine Quelle nennt einen Operator mit beiden Eigenschaften. FKM hat keine Spaltung (Kramers an jedem k [S Z. 468-469]); isotrop ist er nur bei t = 4 lambda_SO, und das folgt erst aus Gl. (5) [M aus S Z. 474-477]; dazu drei Kegel an X. Creutz/Borici-artige Operatoren haben nur einen Vektor-Teil (spinentartet [M]), brechen aber die Gittersymmetrie und brauchen Abstimmung [S]. Die symmetrische Hyperdiamant-Aktion (Bedaque Gl. 7) hat Doppler [S]. Regel 7: Suche in den letzten 24 Monaten (A4) ohne Treffer, also "nach Recherchestand nicht belegt", nicht "widerlegt". |
| DF2 | [H] Jeder bekannte Diamant- bzw. Hyperdiamant-Operator mit hoechstens minimaler Verdopplung bricht eine Gittersymmetrie und braucht mindestens einen abgestimmten Gegenterm | 65 % | **eingetroffen** (fuer Gegenterme der Dimension 3 und 4) | Bedaque u. a. 0804.1145: "The limit where the actions exhibit minimal doubling does not possess the requisite symmetry" [S Z. 13-15, 493-496]; Kimura/Misumi 0907.1371: "no-go property" [S Z. 513-522]; 0907.3774: Creutz-Fermionen "lose the high discrete symmetry" [S Abstract]; 0801.3361: P und T gebrochen, "fine-tuning of several parameters" [S Abstract]; Capitani 0907.2825, Borsanyi 2502.07354, Vig 2401.07651 (Gegenterme nichtperturbativ abgestimmt) [S Abstract]; Misumi 2512.22609 (Hamilton, 3+1 D): "moderate" Abstimmung [S Abstract]. **Grenze:** Fuer Dimension 5, also die Spaltung, sagt die Literatur nichts (V-f). |
| DF3 | [H] Helizitaetsabhaengige Elektronen-Dispersion der Dimension 5 so stark eingeschraenkt, dass W-D als Elektron l weit unter l_P verlangte | 85 % | **eingetroffen** | l < 1,9e-7 l_P (Cherenkov, 2,3 PeV), < 1,7e-8 l_P (5,1 PeV), < 1,4e-5 l_P (eta ~ 1e-5, 95 %). Abschnitt 6. Vorbehalte: Die Schranken sind fuer Helizitaets-Terme formuliert; die Schwellenrechnung ist kinematisch und gilt je Zweig [ES]. Im D-Branen-Schaum wird Cherenkov umgangen [S Abstract 2505.06121]; fuer ein festes Netz gilt das EFT-Regime [ES]. |

- **Bedeutung nach Karte:**
  - DF1 teilweise: Ein Bauweg ohne lineare Lorentz-Verletzung existiert, aber nur ueber eine Abstimmung (FKM-Typ
    oder Gegenterm). Damit faellt DF1 praktisch mit DF2 zusammen.
  - DF2: Fermionen auf Finns Netz kosten wie das Tempo-Problem (L2) eine Abstimmung. Neu ist, dass das auch fuer
    Dimension 5 gilt [M].
  - DF3: Der naive Weyl-Operator auf Finns Netz ist auch als Elektron ausgeschlossen, und zwar unabhaengig davon,
    ob man die Spaltung als Helizitaet liest.

## 3. Erwartungsverstoesse (wichtigste zuerst)

### 3.1 Gegen Praemissen der Karte (Schreibtisch, [M])

| Nr | Erwartet | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| K-2 gross | Karte und LICHT-FINN-NETZ-1: W-D ist "fuehrend ein isotroper masseloser Dirac" (ein Kegel bei Gamma) | Nullstellen von W-D: det M = (1/4) V.V mit V = sum n_a e^{ik.d_a}. Zwei reelle Bedingungen, also Linien. In der Ebene k_x = 2 pi/a ist Re V senkrecht Im V; Nullbedingung 2 sin^2 alpha + 2 sin^2 beta = (cos alpha + cos beta)^2. Loesungen durch alle W-Punkte und durch (1; 0,392; 0,392) 2 pi/a. Probe mit V.V = (1/3)[4 sum z^2 - (sum z)^2]: -1,77 gegen -1,78 | ARBEITSFELD 1.5 | W-D hat Knotenlinien durch die W-Punkte (abs(k) = 2,48 pro l). Zurueckgefaltet laufen sie auch durchs Zoneninnere: (1; 0,392; 0,392) 2 pi/a entspricht (0; -0,608; -0,608) 2 pi/a mit abs(k) = 1,9 pro l, weil V(k+G) = -i V(k) fuer G = (1,1,1) 2 pi/a [M]. LICHT-FINN-NETZ-1 rechnete nur bis k = 0,6 und konnte sie nicht sehen. Numerisch zu pruefen (Karte, Abschnitt 7.1) |
| K-3 gross | Leitung [M]: sigma.q unter O verboten; 4_1-Schraube koennte die Spaltung verbieten | Fuer W-D falsch, siehe Abschnitt 4 | ARBEITSFELD 1.3 | Der richtige Hebel ist P T, nicht C4 |
| K-1 mittel | Karte: "spaltet die Helizitaeten" | Die Stoerung -eps tau_y sigma.q hat in R und L den Erwartungswert 0 und koppelt R mit L ueber abs(q x k^). Eigenzustaende (R +- e^{i phi} L)/sqrt2, Spin laengs +-(q x k) | ARBEITSFELD 1.2 | Es ist eine Querspin-Spaltung bei gemischter Chiralitaet, in Feldsprache ein Tensor-Term psibar sigma^{0i} psi d_j d_l abs(eps_ijl) [M] |

### 3.2 Gegen meine Erwartungen vor den Abrufen

| Nr | Erwartet (vorab) | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| V-g gross | A6: Kimura/Misumi-Bedingung betrifft nur den Rang-2-Tensor (Isotropie fuehrender Ordnung) | Mit naechsten Spruengen hat der Operator die Form sum i gamma_mu F_mu(p) + sum gamma_mu gamma5 G_mu(p) mit unabhaengigen reellen F, G; "the operator including both ... yields unphysical fermion doublers in general"; Nielsen-Ninomiya zaehlt dann nicht ("Poincare-Hopf theorem for 'either' ... not for both"); nicht-naechste Spruenge noetig, die aber "lower the discrete symmetry" | 0907.1371 [S Z. 485-506, 513-522] | [ES] Strukturgleich mit W-D: Die Untergitter-Chiralitaet tau_z erlaubt zwei Strukturen, tau_x (Vektor) und tau_y (Axial). Naechste Spruenge besetzen beide. Der tau_y-Teil ist die sigma.q-Spaltung und macht die Knotenlinien (K-2) |
| V-h gross | A7: FKM als anisotropes Gegenbeispiel | Gl. (5): H_eff^z = t a sigma^y q_z + 4 lambda_SO a sigma^z (s_x q_x - s_y q_y) + m_z sigma^x; "Due to inversion symmetry, each band is doubly degenerate" | cond-mat/0607699 [S Z. 468-477] | [M] E^2 = t^2 a^2 q_z^2 + 16 lambda^2 a^2 (q_x^2 + q_y^2) + m^2: isotrop fuer t = 4 lambda_SO, spinentartet in jeder Ordnung (P T). Zwei Regime auf dem Diamant (Abschnitt 7.3) |
| V-f gross | A5: Gitterliteratur behandelt die Spaltung zweiter Ordnung mit | Nur "relevant and marginal" Operatoren; die zwei A5-symmetrischen relevanten Operatoren "identically vanish because the five basis vectors sum to zero" | 0804.1145 [S Z. 35-40, 326-334] | Zwei Regime: Gitter als Regulator (a -> 0, Kriterium Dimension 3/4) gegen festes Netz (Dimension 5 beobachtbar) |
| V-b mittel | A1: nur "minimal verdoppelt bricht Symmetrie" | Dazu: Aktionen "with enough symmetries to exclude fine tuning ... produce multiple doublings"; Beispielpol p1 = -p2 = -p3 = p4 = arccos(-2/3) | 0804.1145 [S Z. 13-15, 334-337] | Gegenstueck zu K-2 in 4D |
| V-d mittel | A3: keine Aufweichung der Crab-Schranken in 24 Monaten | Cherenkov-Schranken "naturally evaded in models of space-time foam" (D-Branen); Elektronen strahlen dort "despite moving faster than photons" nicht | 2505.06121 [S Abstract] | Regime EFT gegen Schaum; fuer eine feste Bloch-Dispersion gilt EFT [ES] |
| V-a mittel | A1: Kimura/Misumi nur "Abstimmung noetig" | "non-nearest-site hoppings are essential for the correct excitations" | 0907.1371 [S Abstract] | wie mein Gegenterm aus der dritten Schale (Abschnitt 5) |
| V-e klein | A4: nur Lagrange-Gitter-QCD-Arbeiten | Hamilton-Formulierung in 3+1 D; symmetrie-erhaltende Deformation erzeugt ueber einem kritischen Wert weitere Weyl-Knoten; "moderate" Abstimmung | 2512.22609 [S Abstract] | Zwei Arten Abstimmung: auf ein Gebiet (Phase) oder auf einen Punkt. Der sigma.q-Koeffizient ist ein Punkt [ES] |
| V-c klein | A2: eine Crab-Zahl | JLM: nur "maximum electron speed less than the speed of light"; Maccione: Vollanpassung "of order 10^{-5}" | astro-ph/0212190, 0707.2673 [S Abstract] | Zwei Regime (Zweig, Analyseart) |

## 4. Pruefung der Schreibtischaussage der Leitung [M]

**Aussage:** "Ist sigma ein axialer Vektor (T1) und q eine T2-Form, dann enthaelt T1 x T2 unter O keine Invariante;
sigma.q ist verboten; unter T bzw. T_d erlaubt; ein Operator mit 4_1-Schraube koennte die Spaltung verbieten."

1. **Gruppentheorie fuer einen 2x2-Operator: richtig.**
   - In O gilt T1 x T2 = A2 + E + T1 + T2, also keine Invariante.
   - Explizit fuer C4z: k -> (-k_y, k_x, k_z), q -> (q_y, -q_x, -q_z), sigma -> (-sigma_y, sigma_x, sigma_z). Dann
     geht sigma.q in -sigma.q ueber.
   - "Axial" spielt in O keine Rolle, weil O nur eigentliche Drehungen enthaelt.
2. **Fuer W-D: falsch.**
   - Langwellig gilt H = c [tau_x sigma.k - eps tau_y sigma.q] mit c = -2b/3 und eps = b/sqrt3. Das reproduziert
     a1 = +-0,3536 laengs 110 und das Tempo 0,8165 [P].
   - Die Elemente von O ohne T (4_1-Schrauben, zweizaehlige Achsen laengs 110) tauschen die Untergitter:
     V = tau_x (x) U(R). Dabei geht tau_y in -tau_y ueber, also ist tau_y sigma.q invariant (A2 x A2 = A1).
   - W-D besitzt diese Elemente: T_ij = (i/2) sigma.n_ij haengt nur von der Bindungsrichtung ab. Damit ist jede
     eigentliche Gitterdrehung mit Spin-Drehung eine Symmetrie, auch die mit Untergittertausch (F4_1 3 2,
     Punktgruppe O).
   - In der Lage-Eichung der Bloch-Matrix gibt die Translation nur eine gemeinsame Phase.
3. **Uneigentliche Elemente:**
   - Inversion (Bindungsmitte) und Spiegel bilden H auf -H ab (sigma.n ist ungerade). Symmetrien sind erst
     P Gamma und M Gamma mit Gamma = tau_z. Auch sie lassen tau_y sigma.q stehen.
   - Die Teilaussage "unter T_d erlaubt" gilt nur, wenn sigma wie ein polarer Vektor transformiert oder der Term
     in tau_y steht. Mit axialem sigma und sigma.q im Kanal 1 bzw. tau_x waere er unter T_d verboten (A2).
   - Unter T ist er erlaubt: richtig.
4. **Weitere Symmetrien:** Zeitumkehr (i sigma_y K) und Untergitter-Chiralitaet lassen den Term zu.
   - Keine der vorhandenen Symmetrien verbietet ihn. Er laesst sich nur abstimmen (Abschnitt 5, Zeile W-D+S3).
5. **Was ihn verbietet:** eine antiunitaere Symmetrie, die k festhaelt und mit H vertauscht und deren Quadrat -1
   ist, z. B. P T.
   - Dann ist jedes Band an jedem k Kramers-entartet. So ist es bei FKM [S Z. 468-469].
   - Bei W-D antikommutiert P mit H, also auch P T. Es paart E mit -E, nicht E mit E.
6. **Ursache [ES, Feldregel 6]:** das dritte Moment sum w v (x) v (x) v des Sprungsterns (der Knoten ist kein
   Inversionszentrum) zusammen mit einem Sprung, der unter Bindungsinversion ungerade ist (sigma.n). Nicht die
   90-Grad-Drehung. FKM hat dieselben Knoten, aber einen geraden Sprung und deshalb P T.

**Urteil:** Die Aussage stimmt als Gruppentheorie fuer 2x2-Operatoren und ist fuer Finns Diamant-Operator falsch.
Eine Quelle dafuer habe ich nicht; es ist eigene Rechnung von Hand.

## 5. Operatoren

| Operator | Gitter | Nullstellen / Doppler | Symmetrie | Tempo langwellig | Spinspaltung | Gegenterme / Abstimmung | Quelle |
|---|---|---|---|---|---|---|---|
| **W-D** (i/2) sigma.n_ij, naechste Nachbarn | Diamant (Finns Netz, Tetraedermitten) | Dirac-Punkt bei Gamma (zwei Weyl, entgegengesetzt), dazu **Knotenschleifen durch W** | O mit Spin (inkl. 4_1), T, Untergitter-Chiralitaet, P Gamma, M Gamma | isotrop, 2b/3 = 0,8165 | linear: a1 = +-(b/sqrt3) abs(q^ x n), bis 0,354 (110), 0 laengs 100/111; Querspin | sigma.q symmetrie-erlaubt; nur durch Gegenterm entfernbar | [P] LICHT-FINN-NETZ-1; [M] |
| **W-D + S3** (dritte Schale, 12 Vektoren (+-1,+-1,+-3) a/4, w3 = w1/9 bei unnormiertem Sprung (i/2) w sigma.v; in normierten Richtungen wie W-D: Gewicht sqrt(11/3)/9 = 0,213 des Grundsprungs) | Diamant | nicht geprueft (Linien vermutet, weil X(k) nicht identisch null sein kann) | wie W-D | isotrop | erste Spaltung erst in Dimension 7 (relativ ~ k^3) | fester Koeffizient 1/9 (Baumniveau, Naik-artig); nicht geschuetzt, in Wechselwirkung abzustimmen [ES] | [M] |
| Vektor-only-Diamant (Zellen-Eichung, Spruenge d_b und 2 d_1 - d_b) | Diamant | nicht geprueft | Tetraedersymmetrie gebrochen (d_1 ausgezeichnet, Creutz-Mechanismus) | anisotrop, abzustimmen | keine, in jeder Ordnung (H^2 = F^2) | Isotropie-Gegenterm (Dimension 4) | [M]; Mechanismus wie [S] 0804.1145 Z. 380-404 |
| **FKM** t + i (8 lambda_SO/a^2) s.(d1 x d2) | Diamant | drei Dirac-Punkte an X (sechs Weyl); nur mit t: Entartung laengs Linien [L] | Inversion [S], T; volle Raumgruppe Fd-3m [L] | anisotrop: t a laengs X, 4 lambda_SO a quer; isotrop bei t = 4 lambda_SO | keine (P T, jedes Band zweifach) | ein Verhaeltnis t/lambda; Massen durch Bindungsmodulation delta t_p | [S] cond-mat/0607699 Z. 450-482; [M] fuer Isotropie |
| Young u. a. (Raumgruppen-Dirac) | Fd-3m (beta-Cristobalit BiO2) | Dirac an den drei X, durch Kristallsymmetrie geschuetzt | nichtsymmorph | [nicht gelesen] | [nicht gelesen] | - | [S Abstract] 1111.6483 |
| Bedaque Gl. (7): sigma.e_alpha, naechste Nachbarn | Hyperdiamant (4D) | Pol bei p = 0 und "several others", z. B. p1 = -p2 = -p3 = p4 = arccos(-2/3) | A5 (Z5 genuegt gegen Dimension 3/4) | Dirac-Form bei p = 0 | nicht behandelt; drittes Moment des Simplex ungleich null [ES] | keine fuer Dimension 3/4 noetig | [S] 0804.1145 Z. 156-190, 326-337 |
| Creutz / Borici | Hyperdiamant bzw. orthogonal (4D) | zwei Spezies (minimal) | exakte Chiralitaet; hyperkubische Symmetrie, P, T, Z5 gebrochen | nur bei abgestimmten Parametern kovariant | Vektor-only [M aus Struktur] | Dimension 3 (linear divergent) und 4 | [S Abstract] 0712.1201, 0712.4401, 0801.3361, 0907.2825; [S] 0804.1145 Z. 380-404 |
| BBTW in hoeheren geraden Dimensionen | Hyperdiamant (d > 4) | "inevitably yield unphysical degrees of freedom" | hoch | - | - | - | [S Abstract] 0907.3774 |
| Creutz verformt, nicht-naechste Spruenge | verformter Hyperdiamant | minimal | Symmetrie erniedrigt | "Lorentz-covariant excitations" | Vektor-only | ja | [S] 0907.1371 Z. 503-522, 1102-1110 |
| Karsten-Wilczek (Vergleich) | hyperkubisch (4D) | zwei | hyperkubisch gebrochen | abzustimmen | - | nichtperturbativ abgestimmt; raeumliche Naik-Verbesserung | [S Abstract] 2502.07354, 2401.07651, 2508.09690 |
| Minimal verdoppelt, Hamilton (3+1 D) | hyperkubisch | Dirac und Weyl; Einzel-Weyl mit Speziesmasse; weitere Knoten oberhalb kritischer Deformation | "all the symmetries" der Familie | - | - | "moderate" Abstimmung | [S Abstract] 2512.22609 |
| Dirac-QCA (Vergleich) | BCC | - | diskrete Isotropie | fuer kleine k Dirac; "Lorentz covariance is distorted in the ultra-relativistic limit" | - | - | [S Abstract] 1306.1934 |
| Q-W (Projekt) | Diamant | zwei Kegel | nur L_2 | Spannweite 56 % | a1 bis +-1,13 | - | [P] LICHT-FINN-NETZ-1 |

## 6. Elektronen-Schranke mit Umrechnung [M]

- **Konvention der Quelle:** E^2 = p^2 + m_a^2 + eta_a p^n/M^(n-2) mit M ~ M_P = 1,22e19 GeV [S-lokal JLM PRD,
  Z. 103, 167]. Die Cherenkov-Linie ist eta = m^2/(2 p_max^3) [S-lokal Z. 655]. Probe [M]: fuer 100 TeV gibt das
  1,6e-3, die Quelle sagt ~1,5e-3.
- **W-D als Elektron:**
  - E = hbar c k (1 + a1 k l) gibt E^2 = p^2 + 2 a1 l p^3 (hbar = c = 1). Also eta = 2 a1 l M und
    l = eta l_P/(2 a1) mit l_P = hbar c/M = 1,616e-35 m.
  - a1 = 0,3536 (110), also 2 a1 = 0,7071. Laengs 100 und 111 ist a1 = 0. Kreisende Elektronen durchlaufen alle
    Richtungen einer Ebene [ES].
- **Superluminaler Zweig, Cherenkov:**
  - Keine Abstrahlung bis p verlangt eta < m^2 M/(2 p^3), also l < hbar c m^2/(4 a1 p^3).

| Grundlage | p | eta-Grenze [M] | l-Grenze [M] |
|---|---|---|---|
| LHAASO: 1,12-PeV-Photon des Crab entspricht einem 2,3-PeV-Elektron (SSC) [S Abstract 2210.14817] | 2,3 PeV | 1,31e-7 | 3,0e-42 m = 1,9e-7 l_P |
| Crab-Flare 2010: Elektronen "up to ~5.1 PeV", superluminal delta_e <= ~5e-21 [S Abstract 1306.6095] | 5,1 PeV | 1,20e-8 | 2,7e-43 m = 1,7e-8 l_P |
| Probe ueber delta_e: delta = 2 a1 k l, l <= 5e-21 x 1,973e-16 GeV m / (0,7071 x 5,1e6 GeV) | 5,1 PeV | - | 2,7e-43 m (gleich) |

- **Subluminaler Zweig** (gleich gross, entgegengesetzt):
  - Maccione u. a.: "constraints of order 10^{-5} at 95% confidence level on the lepton Lorentz Violation
    parameters" [S Abstract 0707.2673]. Daraus l < 1e-5 x 1,616e-35/0,7071 = 2,3e-40 m = 1,4e-5 l_P.
  - JLM Nature: 7e-8 [L, nicht im Abstract]; daraus l < 1,6e-42 m = 1e-7 l_P.
- **Vorbehalte:**
  - (i) Die Literaturschranken sind fuer helizitaetsabhaengige Terme formuliert. Bei CPT-ungeraden Termen gilt fuer
    Positronen ein anderes eta ("LV parameters for positrons and electrons are different", astro-ph/0309681
    [S Abstract]). W-D gibt Teilchen und Loechern dieselben zwei Zweige (Zeitumkehr und Untergitter-Chiralitaet
    [M]), wirkt also CPT-gerade; dazu kommt der Querspin (K-1).
  - (ii) Die Schwelle ist Kinematik und gilt je Zweig. Die Raten fuer Querspin-Zustaende habe ich nicht geprueft.
    2505.06121 nennt die Raten in phaenomenologischen Ansaetzen "substantial" [S Abstract].
  - (iii) Im D-Branen-Schaum wird die Schwelle umgangen (V-d). Fuer ein festes Netz gilt das nicht [ES].
  - (iv) Die 2,3 PeV und die 5,1 PeV sind modellabhaengige Rueckschluesse aus Photonen.
- **Ergebnis:** In jeder Lesart l << l_P; der lockerste Wert ist 1,4e-5 l_P. Zum Vergleich als Licht verlangte W-D
  l < 0,17 l_P [P]. Fuer Elektronen ist die Schranke also 1e4- bis 1e7-mal strenger.

## 7. Kartenvorschlag, Regime, Unterscheidungspunkte, Gegensweep, Kalibrierung, offene Fragen

### 7.1 Kartenvorschlag (einer)

**DIAMANT-NULLSTELLEN-1 (Rechenkarte, Kleintest .69, <= 10 min, exakte Bloch-Matrizen 4x4)**

- **Frage:** Wo liegen die Nullstellen von W-D im ganzen BZ? Was aendern (i) der Gegenterm W-D+S3 (w3 = w1/9) und
  (ii) FKM bei t = 4 lambda_SO an a1, a2, a3, Tempo-Isotropie und Nullstellen?
- **Messgroessen:**
  - min abs(E) auf einem BZ-Gitter; Dimension der Nullmenge (Punkte oder Linien)
  - a1 bis a3 je Richtung (26 Richtungen)
  - FKM: groesste Spinspaltung und Kegeltempo an X je Richtung
- **Vorab abgeleitet [M]:** Das ist eine Pruefung meiner Mathematik, keine Messung.
  - W-D-Schleife durch W und durch (1; 0,392; 0,392) 2 pi/a
  - W-D+S3: a1 = 0
  - FKM bei t = 4 lambda: isotroper Kegel, Spaltung 0
- **Offen (nicht abgeleitet):** Nullstellen von W-D+S3, a3 von W-D+S3, a2-Anisotropie von FKM.
- **Vorhersagen [H]:**
  - (1) W-D+S3 hat weiter Knotenlinien (70 %).
  - (2) W-D+S3 hat a3 ungleich null laengs 110 (80 %).
  - (3) FKM bei t = 4 lambda: a2-Spannweite > 10 % (60 %).
- **Bedeutung:**
  - (1) ja: Die W-D-Familie ist ohne Wilson-artigen Term (tau_z, bricht 4_1 bzw. Untergittertausch) als Elektron
    mehrfach verdoppelt; die FKM-Familie wird der Kandidat.
  - (1) nein: W-D+S3 ist ein symmetrischer Einzel-Dirac-Operator mit einem Rest der Dimension 7.
- **Ableitbarkeitsprobe:** Teile oben sind ableitbar; offen sind (1) bis (3). Vorher Projekt-grep nach "Knotenlinie",
  "Nullstellen", "FKM", "Fu-Kane" mit den Ausschluessen.

### 7.2 Regime und Moderatoren

| Streitpunkt | Regime A | Regime B | Moderator | Beleg |
|---|---|---|---|---|
| Welche Operatoren zaehlen? | Gitter als Regulator: Dimension 3/4 muss weg | festes Netz: Dimension 5 ist beobachtbar | a -> 0 oder l fest | 0804.1145 [S]; [ES] |
| Symmetrie gegen Verdopplung | symmetrisch, mehrfach verdoppelt (Bedaque Gl. 7, BBTW, W-D [M]) | minimal verdoppelt, Symmetrie gebrochen, abgestimmt (Creutz/Borici, KW) | Symmetriegruppe; nicht-naechste Spruenge | 0804.1145, 0907.1371 [S] |
| Spinspaltung auf dem Diamant | Sprung ungerade unter Bindungsinversion (sigma.n): Dirac bei Gamma, Spaltung ~ abs(X x Y), Knotenlinien | gerade (FKM): P T, Kramers an jedem k, Dirac an drei X | Paritaet des Naechste-Nachbarn-Sprungs | FKM [S]; [M] |
| Art der Abstimmung | auf ein Gebiet (Phase, "moderate") | auf einen Punkt (Isotropie; sigma.q-Koeffizient = 0) | Kodimension des Ziels | 2512.22609 [S Abstract]; [ES] |
| Crab-Schranken | subluminal: maximale Geschwindigkeit (JLM), Vollanpassung ~1e-5 (Maccione) | superluminal: Cherenkov bei PeV | Zweig, Analyseart | [S Abstract] |
| Gilt die Cherenkov-Schwelle? | EFT-Dispersion mit ueblichen Matrixelementen | D-Branen-Schaum: Prozess unterdrueckt | lokale Dispersion gegen Medium | 2505.06121 [S Abstract] |

- **Feldregel 6 [ES]:** Drei Wege zur linearen Spaltung bzw. zu falschen Polen fuehren auf dieselbe Groesse,
  naemlich die Komplexitaet einseitiger Spruenge:
  - W-D: dritter Moment, Kanal tau_y
  - Hyperdiamant: G-Funktion bei Kimura/Misumi
  - Projekt-QCA Q-W: a1 bis 1,13 [P]; ob das dieselbe Ursache hat, ist nicht geprueft
  - Die gemeinsame Groesse ist der antihermitesche Teil des A -> B-Blocks bzw. X x Y, nicht das einzelne Bauteil.

### 7.3 Unterscheidungspunkte (Feldregel 2)

| Paar | Wo sie auseinanderlaufen | Zugaenglich? |
|---|---|---|
| W-D gegen W-D+S3 | a1 laengs 110: 0,354 gegen 0; bei k l = 0,01 relativ 3,5e-3 | modellintern sofort; physikalisch nur ueber die Cherenkov-Schwelle, die W-D schon ausschliesst |
| Helizitaetsspaltung (CPT-ungerade, Myers-Pospelov) gegen Querspin-Spaltung (CPT-gerade, W-D) | Positronen-Dispersion (andere eta gegen gleiche); Spinstruktur der Eigenzustaende; Winkel (isotrop gegen abs(q^ x n) mit Nullen bei 100/111) | nein: keine Signale, beide Klassen bei 1e-7 bis 1e-5 begrenzt |
| FKM-Typ gegen W-D-Typ | Zahl und Lage der Kegel (drei an X gegen einen bei Gamma plus Linien); Spinentartung | modellintern ja; physikalisch nur ueber die Zahl der Elektronenarten (es gibt eine) [ES] |
| symmetrisch-verdoppelt gegen minimal-abgestimmt | Zustandsdichte nahe E = 0 (Linien ~ E gegen Punkte ~ E^2) | modellintern ja; bei l ~ l_P nicht |
| EFT gegen Schaum | Cherenkov-Rate superluminaler PeV-Elektronen | nur modellabhaengig (Elektronen werden erschlossen, nicht gesehen) |

### 7.4 Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlich | geprueft? | Ergebnis |
|---|---|---|---|
| G1 | "spaltet die Helizitaeten" (Karte) | ja [M] | Querspin, Chiralitaet gemischt (K-1) |
| G2 | W-D hat nur den Kegel bei Gamma | ja [M]; Gattung durch Quellen gestuetzt (0804.1145 Z. 334-337, 0907.1371 Z. 500-501) | Knotenschleifen durch W (K-2) |
| G3 | Die Gitterliteratur meint dieselbe Ordnung wie die Karte | ja [S] | nur Dimension 3/4 (V-f) |
| G4 | FKM ist das anisotrope Gegenbeispiel | ja [S + M] | isotrop bei t = 4 lambda_SO, spinentartet (V-h) |
| G5 | Elektronen-Schranken fuer Helizitaet gelten fuer W-D | teilweise [ES] | Schwelle kinematisch je Zweig; Matrixelemente mit Querspin nicht geprueft |
| G6 | Finns Knoten sind die Diamant-Knoten (Tetraedermitten) | nein, nur Skizze [M] | Auf den Pyrochlor-Knoten (Tetraederecken, Inversionszentren) ist sigma.n unter Inversion ungerade. Dann verschwinden alle in k geraden Terme, und H(0) = 0 fuer alle 8 Baender: eine achtfache lineare Kreuzung statt eines Dirac-Kegels. Nicht gerechnet. |
| G7 | Elektron und Licht haben im Netz dieselbe Grenzgeschwindigkeit | nein | W-D 0,8165 gegen Maxwell 2,8284 (Code-Einheiten [P]); das ist L2 bzw. LICHT-GLEICH-L (Abstimmung [P]) |
| G8 | 4D-Euklid-Befunde (Bedaque, Kimura/Misumi) gelten fuer 3D-Hamilton | teilweise | Misumi 2512.22609 bestaetigt die Gattung in 3+1 D [S Abstract]; die Uebertragung auf den Diamant ist [ES] |

### 7.5 Kalibrierung

- **(a) Gemessen:**
  - Crab-Spektren; LHAASO-Photonen bis 1,1 bzw. 1,42 PeV.
  - Daraus modellabhaengig: 2,3-PeV-Elektronen (SSC) und 5,1 PeV (Flare).
  - Kein Signal einer Elektronen-Lorentz-Verletzung. Fuer das Netz selbst gibt es keine Messung.
- **(b) Nuetzlich verdichtet [M/ES]:**
  - Die X(k)-Diagnose (Spaltung und Knotenlinien aus einer Groesse)
  - Die Regime FKM-Typ gegen W-D-Typ
  - Der Gegenterm w3 = w1/9
  - Die Umrechnungen in Abschnitt 6
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Keine Symmetrie verbietet sigma.q in W-D-artigen Operatoren" ist nur fuer die aufgezaehlten Symmetrien
    geprueft (O, P Gamma, M Gamma, T, Untergitter-Chiralitaet). Mehrbandige Erweiterungen oder andere
    Spin-Darstellungen sind nicht geprueft.
  - Die Knotenlinien beruhen auf drei Punkten von Hand und einem Strukturargument, ohne Numerik.
- **Warnzeichen:**
  - Meine Sicherheit, dass W-D als Fermion unbrauchbar ist, stieg mit jeder Quelle (Bedaque, Kimura/Misumi).
    Beide rechnen aber in 4D-Euklid an anderen Operatoren.
  - Die Frage zerfiel zugleich in drei Teile: Spaltung, Doppler, Symmetrie. Das ist das Muster aus der
    Kalibrierregel.

### 7.6 Offene Fragen

1. Knotenlinien von W-D numerisch (Karte 7.1).
2. Nullstellen von W-D+S3; ob ein Wilson-artiger tau_z-Term (bricht den Untergittertausch) sie hebt, ohne Gamma zu
   stoeren.
3. sigma.n-Operator auf den Pyrochlor-Knoten (G6): Spektrum bei Gamma, Tempi.
4. SME-Zuordnung des Terms psibar sigma^{0i} psi d_j d_l abs(eps_ijl) (Kostelecky/Mewes 1308.4973 klassifizieren
   alle Dimensionen [S Abstract]) und eigene Schranken fuer CPT-gerade spinabhaengige Terme der Dimension 5. Nicht
   gelesen.
5. Enthaelt die Symanzik-Wirkung der KW-Fermionen bis Dimension 5 (2508.09690) spinabhaengige Terme?
6. FKM auf Finns Netz: Laesst sich t = 4 lambda_SO aus einer Symmetrie gewinnen? Lassen sich zwei der drei X-Kegel
   ueber delta t_p massiv machen (Gl. 5, m_z), ohne die Isotropie zu verlieren?

## 8. Quellen (Abrufstand 2026-10-04; Kopien in quellen/, Zeiten im ARBEITSFELD)

| Quelle | URL | Abruf | gelesen |
|---|---|---|---|
| Creutz, M. (2008): Four-dimensional graphene and chiral fermions, JHEP 0804:017 | https://arxiv.org/abs/0712.1201 | A1 22:44:08 | [S Abstract] |
| Borici, A. (2008): Creutz Fermions on an Orthogonal Lattice, PRD 78, 074504 | https://arxiv.org/abs/0712.4401 | A1 | [S Abstract] |
| Bedaque, P. F.; Buchoff, M. I.; Tiburzi, B. C.; Walker-Loud, A. (2008): Broken Symmetries from Minimally Doubled Fermions, PLB 662, 449 | https://arxiv.org/abs/0801.3361 | A1 | [S Abstract] |
| Bedaque, P. F.; Buchoff, M. I.; Tiburzi, B. C.; Walker-Loud, A. (2008): Search for Fermion Actions on Hyperdiamond Lattices, PRD 78, 017502 | https://arxiv.org/abs/0804.1145 | A1; A5 22:47:59 (PDF) | [S] Volltext, Z. 1-60, 156-190, 321-404, 433-502 |
| Kimura, T.; Misumi, T. (2010): Characters of Lattice Fermions Based on the Hyperdiamond Lattice, Prog. Theor. Phys. 124, 415 | https://arxiv.org/abs/0907.1371 | A1; A6 22:49:54 (PDF) | [S] Z. 440-530, 1095-1120 |
| Kimura, T.; Misumi, T. (2010): Lattice Fermions Based on Higher-Dimensional Hyperdiamond Lattices, Prog. Theor. Phys. 123, 63 | https://arxiv.org/abs/0907.3774 | A1 | [S Abstract] |
| Capitani, S.; Weber, J.; Wittig, H. (2009): Minimally doubled fermions at one loop | https://arxiv.org/abs/0907.2825 | A1 | [S Abstract] |
| Fu, L.; Kane, C. L.; Mele, E. J. (2007): Topological Insulators in Three Dimensions, PRL 98, 106803 | https://arxiv.org/abs/cond-mat/0607699 | A1; A7 22:53:26 (PDF) | [S] Z. 448-500 |
| Young, S. M.; Zaheer, S.; Teo, J. C. Y.; Kane, C. L.; Mele, E. J.; Rappe, A. M. (2012): Dirac semimetal in three dimensions, PRL 108, 140405 | https://arxiv.org/abs/1111.6483 | A1 | [S Abstract] |
| D'Ariano, G. M.; Perinotti, P. (2014): Derivation of the Dirac Equation from Principles of Information Processing, PRA 90, 062106 | https://arxiv.org/abs/1306.1934 | A1 | [S Abstract] |
| Jacobson, T.; Liberati, S.; Mattingly, D. (2003): Lorentz violation and Crab synchrotron emission: a new constraint far beyond the Planck scale, Nature 424, 1019 | https://arxiv.org/abs/astro-ph/0212190 | A2 22:45:12 | [S Abstract] |
| Maccione, L.; Liberati, S.; Celotti, A.; Kirk, J. G. (2007): New constraints on Planck-scale Lorentz Violation in QED from the Crab Nebula, JCAP 0710:013 | https://arxiv.org/abs/0707.2673 | A2 | [S Abstract] |
| Liberati, S.; Maccione, L. (2009): Lorentz Violation: Motivation and new constraints, Ann. Rev. Nucl. Part. Sci. 59, 245 | https://arxiv.org/abs/0906.0681 | A2 | [S Abstract], ohne Zahl |
| Liberati, S. (2013): Tests of Lorentz invariance: a 2013 update | https://arxiv.org/abs/1304.5795 | A2 | [S Abstract], ohne Zahl |
| Kostelecky, V. A.; Mewes, M. (2013): Fermions with Lorentz-violating operators of arbitrary dimension, PRD 88, 096006 | https://arxiv.org/abs/1308.4973 | A2 | [S Abstract] |
| arXiv-API-Suche Elektronen-LV (39 Eintraege), daraus: Li, C.; Ma, B.-Q. 2204.02956 (PLB 829 (2022) 137034, laut Zitat in 2505.06121); 2210.14817 (2.3-PeV-Elektron); 2308.02021; Stecker, F. W. 1306.6095 (Astropart. Phys. 56 (2014) 16); Jacobson, T. u. a. astro-ph/0309681 (PRL); 2505.06121 (D-Schaum, 2025) | https://export.arxiv.org/api/query (A3) | A3 22:45:49 | [S Abstract] |
| arXiv-API-Suche Hyperdiamant / minimal verdoppelt (40 Eintraege), daraus: Misumi, T. u. a. 2512.22609 (PRD 113, 074521 (2026)); Shukre, K. u. a. 2508.09690 (PRD 112, 114501); Borsanyi, S.; Capitani, S. u. a. 2502.07354; Vig, R. A.; Borsanyi, S. u. a. 2401.07651; Kishore, A. u. a. 2602.19767, 2501.10336 | https://export.arxiv.org/api/query (A4) | A4 22:47:10 | [S Abstract] |
| Jacobson, T.; Liberati, S.; Mattingly, D. (2003): Threshold effects and Planck scale Lorentz violation: combined constraints from high energy astrophysics, PRD 67, 124011 | https://arxiv.org/abs/hep-ph/0209264 | lokal RUNDE-34/grb-221009a/quellen/ | [S-lokal] Z. 103, 167, 655 |
| Projektdateien: RUNDE-37/licht-finn-netz-1 (ERGEBNIS, PLAN, code/licht_netz.py Z. 1-58, 153-166), weyl-linear-1/ERGEBNIS, strang-anker-l/DOSSIER | lokal | - | [P] |

## 9. Selbstanzeigen

1. **Abrufweg:** curl statt WebFetch, wie STRANG-ANKER-L, damit Kopien mit Abrufzeit in quellen/ liegen.
   - 7 von 8 Abrufen verbraucht, einer bleibt.
   - PDFs mit pdftotext gewandelt; A5 zusaetzlich mit -layout.
2. **A1-Erwartung:** Sie nennt "11 IDs", abgerufen wurden 10. Alle zehn waren richtig, nur die Titel der beiden
   Kimura/Misumi-Arbeiten hatte ich vertauscht im Kopf.
3. **Zeilenangaben A6, A7 und A5:** Im ARBEITSFELD standen zuerst ungenaue Zeilen. Sie sind dort gekennzeichnet
   berichtigt (22:53:58 und 22:58:37). Im Dossier habe ich nach einer Nachkontrolle per grep (22:58) vier
   Zeilenangaben ersetzt: FKM Z. 466-467 durch 468-469 bzw. 468-477, Bedaque-Abstract Z. 11-13 durch 13-15.
4. **Alles [M] ist von Hand und numerisch ungeprueft:** Entwicklung von W-D, Symmetriepruefung, Knotenschleifen
   (drei Punkte plus Strukturargument), Gegenterm w3 = w1/9, Isotropie von FKM bei t = 4 lambda_SO, alle
   Umrechnungen. Lokal kein python, awk oder perl.
5. **[L] statt Quelle:**
   - JLM-Nature-Zahl 7e-8
   - Entartung des skalaren Diamanten laengs X-W
   - Kristallographie von F4_1 3 2
   - Myers-Pospelov-Form und das CPT-Verhalten der Positronen (die Aussage "different" ist [S Abstract])
   - SME-Familie des Terms
6. **Konvention Maccione:** Dass "lepton Lorentz Violation parameters" dieselben eta wie bei JLM sind, nehme ich an
   [L]. Das Abstract sagt nur "O(E/M) Lorentz Violation in QED in an effective field theory framework".
7. **Analogie 4D-Euklid zu 3D-Hamilton** (gamma5 entspricht der Untergitter-Chiralitaet tau_z, i gamma F
   entspricht tau_x, gamma gamma5 G entspricht tau_y): eigener Schluss [ES], nicht aus einer Quelle.
8. **Werkzeuge lokal:** date, mkdir, ls, cat, sed, grep (nur auf Einzeldateien, kein Verzeichnis-grep), head, cut,
   tr, paste, wc, file, curl, pdftotext. jq nicht benutzt.
   - Kein versiegelter Pfad, keine KS-1-Datei geoeffnet.
   - Kein Journal, kein Peerbus, kein Commit.
   - Geschrieben nur in diamant-fermion-l/.
9. **ARBEITSFELD-Gliederung:** Die Abschnitte stehen in der Folge 0, 1, 2, 5 (Gegensweep), 4 (Umrechnung),
   3 (offene Rueckfragen), 6. Das ist umstaendlich, aber vollstaendig.
10. **Zeitbox:** Start 22:32:11, letzte Aenderung am Dossier gegen 23:02 CEST (date-Werte im ARBEITSFELD), also
    innerhalb der 60 Minuten.

## 10. Einfach gesagt

Wir haben gefragt, ob es auf Finns Tetraeder-Netz eine Regel fuer Elektronen gibt, bei der beide Spin-Sorten bei
hoher Energie gleich schnell bleiben. Die naive Regel trennt sie leicht, und weil Elektronen im Krebsnebel bis zu
Millionen Milliarden Elektronenvolt erreichen, muesste die Masche dann viel kleiner als die Planck-Laenge sein. Der
Grund ist, dass die Regel die Richtung jeder Bindung in den Spin schreibt und die Knoten keine Spiegelmitte haben.
Dieselbe Ursache erzeugt bei grossen Impulsen ganze Linien falscher Zusatzteilchen. Es gibt Auswege, zum Beispiel ein
Modell von Fu, Kane und Mele, dessen Regel beim Punktspiegeln gleich bleibt, oder einen Zusatzsprung zu weiter
entfernten Nachbarn mit genau einem Neuntel Gewicht. Jeder Ausweg braucht aber eine fest eingestellte Zahl, die
nichts von selbst festhaelt.
