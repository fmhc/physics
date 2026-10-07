# GF-BIC (Runde 8): zweite Komponente um einen einkomponentigen Ball, Plan

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) im Auftrag der Leitung claude-primary.
- Beginn der Karte: 2026-09-30 05:57:52 CEST (date). Plan geschrieben ab 2026-09-30 06:13:15 CEST (date), **vor jeder
  Rechnung dieser Karte**.
- Explorativ (v3). Alle Aussagen dieses Plans sind Herleitung von Hand; neue Deutungen sind mit [H] markiert.
- Quellen: gesamtformel-20260921/KANDIDAT.md (0 bis 7 gelesen), RUNDE-07/beweis/BRIEF.md (1), RUNDE-07.md,
  RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md (3, 4.4, 4.6), resonance-20260930/BIC-TESTPAKET-ERGEBNIS.txt,
  RUNDE-06/resonanz3d/resonanz3d.py, RUNDE-07/bic2/bic2.py (nur gelesen).

## 1. Herleitung der linearisierten psi_2-Gleichungen

### 1.1 Ausgangspunkt

- Formel (KANDIDAT.md 0, 2.2), N = 2, J_12 = J:
  - L = sum_a (|d_t psi_a|^2 - |grad psi_a|^2) - U(S) + g J Re[(psi_1^* psi_2)^2], S = |psi_1|^2 + |psi_2|^2
  - Bewegungsgleichung fuer psi_2: d_t^2 psi_2 - Lap psi_2 + U'(S) psi_2 - g J psi_2^* psi_1^2 = 0
  - U' = 1 - 2S + (3/2) S^2, U'' = -2 + 3S (beta = 1/2)
- Grundzustand (Konvention von resonanz3d.py und KANDIDAT.md): psi_1 = f(r) e^{-i omega t}, psi_2 = 0.
  - Die Leitung schreibt e^{+i omega t}. Das ist die komplex konjugierte Loesung; die Konjugation C ist eine Symmetrie
    (KANDIDAT 3.2). Das Spektrum ist dasselbe.

### 1.2 Linearisierung

- S = f^2 + |psi_2|^2 haengt von psi_2 erst in zweiter Ordnung ab. Also steht in linearer Ordnung U'(f^2) ohne U''-Term.
- Der Paarterm ist linear in psi_2: g J psi_2^* psi_1^2 = g J f^2 e^{-2 i omega t} psi_2^*.
- Die Gleichung fuer psi_1 enthaelt g J psi_1^* psi_2^2, also zweite Ordnung. Die Atmungsgleichungen fuer delta psi_1
  bleiben deshalb exakt die von N = 1 (THEORIE 4.6 stimmt in diesem Punkt).
- Ansatz: psi_2 = e^{-i omega t} chi, chi = u(x) e^{-i nu t} + v^*(x) e^{+i nu^* t}.
  - Zuerst: chi_tt - 2 i omega chi_t - omega^2 chi - Lap chi + U'(f^2) chi - g J f^2 chi^* = 0.
  - Koeffizient von e^{-i nu t}: [-Lap + U'(f^2) - (omega + nu)^2] u - g J f^2 v = 0
  - Koeffizient von e^{+i nu^* t}, konjugiert: [-Lap + U'(f^2) - (omega - nu)^2] v - g J f^2 u = 0
- Sektor l = 0, A = r u, B = r v, in der Form von resonanz3d.py:
  - A'' = [dp - (omega + nu)^2] A + sp B, B'' = sp A + [dp - (omega - nu)^2] B
  - **psi_2:** dp = U'(S) = 1 - 2S + 3 beta S^2, sp = -g J S
  - **psi_1 (N = 1, Kontrolle):** dp = U' + S U'' = 1 - 4S + 9 beta S^2, sp = S U'' = -2S + 6 beta S^2
- Das bestaetigt die Anmerkung der Leitung: Diagonale U'(f^2) - (omega +- nu)^2 ohne U''S, Nebendiagonale -g J f^2
  (im Operator; im ODE-Format sp = -g J S).

### 1.3 Reelle Form und Symmetrien

- s = u + v, d = u - v, L_- = -Lap + U'(f^2) - omega^2:
  - (L_u - nu^2) s = 2 omega nu d mit L_u = L_- - g J f^2
  - (L_v - nu^2) d = 2 omega nu s mit L_v = L_- + g J f^2
- Symmetrien des Spektrums:
  - nu -> -nu mit u <-> v, und nu -> nu^* (reelle Koeffizienten). Eigenwerte kommen als {nu, -nu, nu^*, -nu^*}.
  - g -> -g mit s <-> d. Das ist psi_2 -> i psi_2, das den Paarterm umkehrt. **Das Spektrum haengt nur von |g| ab.**
- Kontrollen bei g = 0 (U(2)-Symmetrie; Kanaele entkoppelt):
  - L_- f = 0 (Profilgleichung). Also nu = 0 doppelt: u = f oder v = f, das heisst psi_2 = c f e^{-i omega t} (Drehung
    des Balls in Komponente 2).
  - nu = 2 omega mit v = f, u = 0: psi_2 = f e^{+i omega t}, der Gegenlaeufer. Er liegt im offenen Kanal
    omega + nu = 3 omega > 1, ist also bei g = 0 ein **eingebetteter Eigenwert der Breite 0**.
  - Angeregte l = 0-Zustaende E_k von L_0 = -Lap + U'(f^2) in (omega^2, 1): nu = sqrt(E_k) - omega (gebunden,
    unter 1 - omega) und nu = omega + sqrt(E_k) (eingebettet).
  - Kontinuum: Kanal a offen fuer nu > 1 - omega, Kanal b fuer nu > 1 + omega. Alle interessanten Stellen
    (2 omega, omega + sqrt(E_k)) liegen im Fenster 1 - omega < nu < 1 + omega mit genau einem offenen Kanal.

### 1.4 Die Nullmode bei g != 0 (Hand)

- Energie der psi_2-Stoerung im mitdrehenden System: K_2 = <s, L_u s> + <d, L_v d> + kinetischer Teil.
  - Fuer g > 0 ist L_v >= L_- >= 0, und L_u hat mindestens einen negativen Eigenwert: <f, L_u f> = -g J int f^4 < 0.
  - Fuer g < 0 tauschen L_u und L_v die Rollen (1.3).
- Das System ist gyroskopisch: s'' + 2 omega d' + L_u s = 0, d'' - 2 omega s' + L_v d = 0 (s, d reell in t).
  - Kelvin-Tait-Chetaev bzw. Hamilton-Krein-Index [L?]: k_r + 2 k_c + 2 k_i^- = n(L_u) + n(L_v) - (Korrektur aus einem
    verallgemeinerten Kern).
  - Jordan-Kette bei nu = 0 im psi_2-Sektor: G (f, 0) = (0, -2 omega f) liegt im Kern, also ist L x1 = -G x0 nicht
    loesbar (<f, 2 omega f> != 0). **Kein verallgemeinerter Kern**, keine Korrektur.
  - Bei kleinem |g| ist n(L_u) = 1, also k_r = 1: **genau ein reelles Paar nu = +-i lambda, eine Instabilitaet fuer
    jedes g != 0.**
- Zwei-Moden-Formel (Projektion auf span{(f, 0), (0, f)}; G bildet diesen Raum in sich ab, die Korrektur beginnt deshalb
  erst in O(g^2) relativ):
  - lambda^4 + 4 omega^2 lambda^2 - g^2 kappa^2 = 0 mit kappa = J <f^4>/<f^2> (Integrale mit r^2 dr)
  - lambda_2 = sqrt(-2 omega^2 + sqrt(4 omega^4 + g^2 kappa^2)) ~ |g| kappa / (2 omega)
  - Eigenvektor: d ~ sign(g) s, also relative Phase 45 Grad. Dort ist der Kanalstrom T_12 ~ sin(2 Delta chi) am groessten
    (KANDIDAT 4.2).
- Bild [H]: Paarumwandlung psi_1 psi_1 -> psi_2 psi_2. Sie ist exakt resonant, weil beide Komponenten dieselbe Frequenz
  omega haben (U haengt nur von S ab). Das ist das lokalisierte Gegenstueck zum homogenen Ueberlaufband von UEBERLAUF.md
  (dort s(0)^2 = -2 omega^2 + sqrt(4 omega^4 + kappa^2), KANDIDAT 6, Zeile 3).
- Abgleich mit KANDIDAT 5.2 und 5.3 (Hand):
  - Der einkomponentige Ball existiert fuer alle g im Fenster 1/2 < omega^2 < 1, weil der Paarterm auf ihm identisch
    verschwindet. 5.2 (Vakuum bis |g| J <= 1,657) begrenzt ihn nicht.
  - Er ist aber ein Sattel: Der gemischte Ball hat tiefere Energie.
    - g > 0: psi_1 = psi_2 = h e^{-i omega t}; g < 0: psi_2 = +-i psi_1.
    - Im invarianten Unterraum psi_1 = psi_2 ist das exakt das N = 1-Modell mit U_eff(S) = S - (1 + |g| J/4) S^2 + S^3/2.
      Das ist genau das Fenster 5.3.
    - Mit S = S'/b, b = 1 + |g| J/4 wird daraus U' = 1 - 2 S' + 3 beta_eff S'^2 mit **beta_eff = 1/(2 b^2)**.
    - Folgerung [Hand, exakt]: Der symmetrische Sektor des gemischten Balls hat die stillen Stellen der beta-Familie bei
      beta_eff. Werte: g = 0,2 -> 0,4535; g = 0,5 -> 0,3951; g = 1,0 -> 0,32.
    - Antisymmetrischer Sektor (psi_1 - psi_2): L_p = L_-^eff + 2 g J h^2 und L_q = L_-^eff + 4 g J h^2, beide positiv
      definit (Hand). Also dort keine lineare Instabilitaet.

## 2. Frage 2 von Hand: Gibt es einen Verlustkanal der Ordnung epsilon^2?

- psi_2 -> -psi_2 ist eine Symmetrie, psi_2 = 0 also ein invarianter Unterraum ("in einen exakt leeren Kanal geht
  nichts", KANDIDAT 4.2). Deshalb gibt es klassisch **keinen direkten Fluss in ein leeres psi_2**, in keiner Ordnung von
  epsilon. psi_1 allein folgt exakt der N = 1-Dynamik, einschliesslich Codex' epsilon^4-Fluss.
- Neue Kanaele koennen nur Keime verstaerken (Instabilitaet oder parametrische Verstaerkung).
- Pumpe: Atmung an der stillen Stelle, delta psi_1 = epsilon e^{-i omega t}(a e^{-i rho t} + b e^{i rho t}) mit reellen
  a, b (BIC). In der chi-Gleichung erscheinen dann zwei Terme erster Ordnung:
  - epsilon U''(f^2) 2 f (a + b) cos(rho t) chi
  - -g J epsilon 2 f (a e^{-i rho t} + b e^{i rho t}) chi^*
- g = 0 im Laborsystem [Hand]:
  - psi_2 erfuellt eine KG-Gleichung mit reellem, zeitperiodischem Potential U'(|psi_1|^2). Ihre Energie ist positiv
    definit (L_0 >= omega^2 > 0).
  - Parametrische Instabilitaet gibt es dann nur bei Summenresonanz Omega_a + Omega_b = n rho* (Omega >= omega:
    gebunden in [omega, 1), Kontinuum >= 1).
  - n = 1, gebunden plus Kontinuum: noetig waere Omega_a <= rho* - 1. An allen fuenf Stellen ist rho* - 1 < omega
    (0,745 < 0,893; 0,653 < 0,795; 0,628 < 0,776; 0,611 < 0,763). **Unmoeglich.**
  - n = 1, gebunden plus gebunden: noetig rho* >= 2 omega. Stelle 1 scheitert (2 omega = 1,786 > 1,745). Die Stellen 2
    bis 5 erlauben es nur bei zufaelliger Gleichheit (Zungen der Breite O(epsilon)).
  - Der f-Sektor ist zusaetzlich geschuetzt: psi_2 = c psi_1(t) und c psi_1(t)^* sind bei g = 0 exakte beschraenkte
    Loesungen.
  - n = 2 (Pumpe epsilon^2 bei 2 rho*): gebunden plus Kontinuum moeglich, Rate O(epsilon^4).
- g != 0: Der Paarterm koppelt Omega an 2 omega - Omega. Im mitdrehenden System heisst die Bedingung dann
  nu_a + nu_b = rho* (beide positive Energie).
  - gebunden (nu_k < 1 - omega) plus Kontinuum (rho* - nu_k > 1 - omega) ist immer erfuellt.
  - [H] Jeder echt gebundene psi_2-Zustand mit 0 < nu_k < 1 - omega waechst dann mit einer Rate O(epsilon^2 g^2)
    (goldene Regel, Paarerzeugung).
  - Die Nullmoden-Instabilitaet lambda = O(g) aus 1.4 besteht aber schon bei epsilon = 0 und ueberwiegt bei kleinem
    epsilon.
  - gebunden plus gebunden: 2 (1 - omega) < rho*, also nie.
- [H] Fuer den gemischten Ball (den natuerlichen Zustand bei g != 0):
  - Der antisymmetrische Sektor hat eine Pseudo-Goldstone-Mode nu_0 = O(g) (innere Drehung).
  - nu_0 + (rho*_eff - nu_0) mit einem Partner im Kontinuum ist eine Summenresonanz, also moeglicherweise ein
    parametrischer Kanal O(epsilon^2).
  - Dieser Plan rechnet das nicht; es waere eine Folgekarte.

## 3. Vorab-Erwartungen (geschrieben ab 2026-09-30 06:13:15 CEST, Datei zuerst gespeichert 06:14:34 laut mtime, vor jeder Rechnung dieser Karte)

Stellen: P1 = 0,797677 (rho* 1,744618), P2 = 0,685129, P3 = 0,631449 (rho* 1,652588), P4 = 0,601422
(rho* 1,628113), P5 = 0,582417 (rho* 1,611309, RUNDE-07.md). g in {0; 0,2; 0,5; 1,0}, J = 1.

| Nr. | Erwartung | widerlegt, wenn |
|---|---|---|
| V1 | Fuer jedes g != 0 an allen fuenf Stellen genau ein instabiles Paar nu = +-i lambda (rein imaginaer), solange n(L_u) = 1 | kein instabiler Eigenwert bei g = 0,2, oder \|Re nu\|/lambda > 1e-6 am instabilen Paar |
| V1a | lambda/lambda_2 in [0,95; 1,05] bei g = 0,2, in [0,85; 1,15] bei 0,5 und in [0,7; 1,3] bei 1,0 (lambda_2 aus 1.4, kappa aus demselben Profil) | ausserhalb dieser Fenster |
| V1b | Grobe Zahlen an P1 (Annahme kappa ~ 0,73 aus S0 = 1,045): lambda ~ 0,08 / 0,2 / 0,4 bei g = 0,2 / 0,5 / 1,0, je +-30 % | ausserhalb +-30 % (dann ist die kappa-Annahme falsch, nicht V1a) |
| V1c | Spektrum bei g und -g gleich (relativ 1e-10) | Abweichung > 1e-8 |
| V2 | n(L_u) = 1 fuer g <= 0,5 an allen Stellen; bei g = 1,0 an P4/P5 moeglich 2 [H, schwach] | n(L_u) >= 2 schon bei g = 0,2 |
| V3 | g = 0: D(0) = 0 und D(2 omega) = 0 (Nullmode und eingebetteter Gegenlaeufer); Newton findet 2 omega mit \|Im\| < 1e-9 | \|nu - 2 omega\| > 1e-6 bei g = 0 |
| V3a | g != 0: Pol nahe 2 omega mit Im nu < 0 (abklingend). \|Im nu(0,5)\|/\|Im nu(0,2)\| in [5; 7,5] (g^2 gaebe 6,25), ausser nahe einer Nullstelle aus V6 | Im nu > 0, oder Verhaeltnis ausserhalb |
| V4 | Echt gebundene psi_2-Zustaende 0 < nu < 1 - omega: an P1 keine (ausser der Nullmode bei g = 0); an P3 bis P5 mindestens einer [H] | umgekehrt |
| V5 | Floquet (Pumpe epsilon an P1 und P3), g = 0: keine Wachstumsrate ueber 1e-4 fuer epsilon <= 0,04 | Wachstumsrate > 1e-4 bei g = 0 |
| V5a | g != 0: groesste Floquet-Rate = lambda(g) + O(epsilon^2), \|Aenderung\| < 5 % von lambda bei epsilon = 0,02 | Aenderung > 5 % |
| V5b | Keine zusaetzliche instabile Floquet-Mode (neben dem lambda-Paar) fuer epsilon <= 0,04, bei g = 0,2 [H] | eine weitere Mode mit Rate > 1e-4 |
| V6 | Frage 3: Das Ueberlappintegral I(omega) = int Phi_reg f^3 r dr des Gegenlaeufers (Kanal a bei 3 omega) wechselt in 0,52 < omega^2 < 0,98 mindestens zweimal das Vorzeichen [H]. Dort faellt die Breite des 2 omega-Pols bei g = 0,2 um mehr als das 100-fache gegen die Nachbarn | kein Vorzeichenwechsel, oder kein Einbruch |

## 4. Kontrollen

- **N = 1-Grenze** (dp, sp von psi_1, derselbe Code): Pol bei omega^2 = 0,7 = 1,7018102 - 1,468e-3 i; an P1 ist \|Im rho\|
  < 1e-7 nahe 1,744618.
- **g = 0:** Nullmode und 2 omega (V3), dazu die Kastenrechnung (doppelter Eigenwert nahe 0).
- **g <-> -g** (V1c).
- **Zwei Verfahren fuer lambda und die gebundenen Zustaende:**
  - Schiessen mit Verbundmatrix (det aus resonanz3d.py, RK4, h = 0,02 und 0,01)
  - Finite Differenzen im Kasten (quadratisches Eigenwertproblem, Delta = 0,1 und 0,05, Richardson)
- **Negativkontrolle ohne Ball:** keine Instabilitaet, kein gebundener Zustand.
- **Floquet:**
  - epsilon = 0 muss lambda aus dem Eigenwertproblem wiedergeben.
  - g = 0: f-Sektor mit \|mu\| = 1 bis auf O(epsilon^2) (Abschneiden der Pumpe auf O(epsilon))
  - Gitter Delta 0,1 gegen 0,075 und Zeitschritt T/N gegen T/(2N)
- Belegstufen je Aussage: Hand, numerisch einfach, numerisch mit Kontrolle.

## 5. Umsetzung und Kostenplan

- gfbic.py (dieser Ordner):
  - importiert resonanz3d.py unveraendert (lokal aus RUNDE-06/resonanz3d/, auf der .69 als Kopie im Laufordner, sha256
    im Bericht) fuer Profil, det, newton und illinois
  - eigener Teil:
    - lin-Struktur fuer psi_2
    - FD-Kasten
    - Zwei-Moden-Formel
    - Floquet-Monodromie
    - Ueberlappintegral
- Unterbefehle:
  - rauch
  - spektrum (je Stelle: Profil, kappa, lambda_2, FD-Kasten, Newton fuer i lambda, 2 omega, omega + sqrt(E_k),
    gebundene Zustaende, g <-> -g, Kontrollen)
  - floquet (Monodromie ueber eine Periode 2 pi/rho*, g- und epsilon-Liste)
  - ueberlapp (I(omega) auf einem omega^2-Gitter, dazu die Breite des 2 omega-Pols bei g = 0,2 an den Wechseln)
- Rechenorte:
  - Rauchtest lokal: CPU, CUDA_VISIBLE_DEVICES leer, 1 Thread, nice 19, timeout 120
  - alles andere auf der .69 ueber kleintest.sh (cpu, cpu2, cpu4; floquet auf p4000a oder cpu), je Aufruf <= 10 min
    mit eigenem Zeitwaechter (Budget 540 s)
- Geschaetzte Kosten (werden gemessen und im Ergebnis ersetzt):
  - spektrum: etwa 1 bis 2 min je Stelle
  - floquet: etwa 5 bis 30 s je Paar (g, epsilon)
  - ueberlapp: etwa 2 min
  - Zusammen weniger als 40 min Rechenzeit.

## Einfach gesagt

Wir pruefen, was eine zweite Feldsorte mit einem Q-Ball macht, der nur aus der ersten Sorte besteht. Nach der
Rechnung von Hand ist so ein Ball bei jeder Kopplung g instabil: Er "kippt" langsam in eine Mischung aus beiden Sorten,
weil zwei Teilchen der ersten Sorte ohne Energieaufwand in zwei der zweiten umwandeln koennen. Die stillen Stellen der
Atmung bleiben fuer den einkomponentigen Ball erhalten und tauchen im gemischten Ball verschoben wieder auf. Ob die
Atmung selbst die zweite Sorte zusaetzlich aufschaukelt, rechnen wir mit einer Floquet-Analyse nach.

## Nachtrag A: gemischter Ball (geschrieben ab 2026-09-30 06:26:18 CEST, date; vor jeder Rechnung dazu)

- Anlass: 1.4 zeigt von Hand, dass der einkomponentige Ball bei g != 0 ein Sattel ist. Die Frage "Verlustkanal O(eps^2)"
  ist deshalb am gemischten Ball zu stellen (psi_1 = psi_2 = h e^{-i omega t}, g > 0). Der Rauchtest (06:22, grob)
  hat nur Code-Durchlauf gezeigt; Zahlen daraus gehen nicht in diese Vorab-Tabelle ein, ausser der Existenz von lambda.
- Herleitung (Hand), S = 2 h^2, psi_{1,2} = (H +- eta) e^{-i omega t}, H = h + eps xi:
  - symmetrischer Sektor = N = 1 mit U_eff = U - g J S^2/4; im ODE-Format dp = U' + S U'' - g J S, sp = S U'' - g J S/2.
    Nach S' = b S ist das exakt die beta-Familie mit beta_eff = 1/(2 b^2), b = 1 + g J/4.
  - antisymmetrischer Sektor: eta_tt - 2 i omega eta_t + [-Lap + U'(2|H|^2) + 2 g J |H|^2 - omega^2] eta
    - g J H^2 eta^* = 0. Bei eps = 0 also dp = U'(S) + g J S, sp = -g J S/2. Positiv definit (1.4).
  - Pseudo-Goldstone-Mode (Zwei-Moden, Hand): nu_0 ~ alpha/(sqrt(2) omega), alpha = 2 g J <h^4>/<h^2>.
- Punkte mit bekannter stiller Stelle der beta-Familie (RUNDE-07.md, RUNDE-08.md):
  - beta_eff = 0,45 heisst g = 4 (1/sqrt(0,9) - 1) = 0,216370: omega*^2 = 0,755738 (rho* aus dem FD-Kasten nahe 1,72)
    und 0,577365 (rho* 1,602162)
  - beta_eff = 0,40 heisst g = 4 (1/sqrt(0,8) - 1) = 0,472136: omega*^2 = 0,566347 (rho* 1,583776)
- **Vorab:**

| Nr. | Erwartung | widerlegt, wenn |
|---|---|---|
| VG1 | Antisymmetrischer Sektor: keine Instabilitaet (FD) an allen drei Punkten; tiefste Mode nu_0 reell, nu_0 / nu_0,2 in [0,8; 1,2] | instabiler Eigenwert, oder Verhaeltnis ausserhalb |
| VG2 | Floquet antisymmetrisch, eps = 0: groesste Rate <= 1e-6 | Rate > 1e-6 bei eps = 0 |
| VG3 [H] | Mit Pumpe waechst die Pseudo-Goldstone-Mode (Summenresonanz nu_0 + Kontinuum = rho*): Rate > 1e-6 bei eps = 0,04 an mindestens einem Punkt, Skalierung ~ eps^2 (Exponent 1,8 bis 2,2 zwischen 0,02 und 0,04) | keine Rate > 1e-6 bei eps = 0,04 (dann: Kanal nicht gesehen, obere Schranke) |
| VG4 | Floquet-Spektrum gerade in eps (eps und -eps gleich, relativ 1e-6) | Abweichung > 1e-4 |

## Nachtrag B: Frage 3 gezielt (geschrieben ab 2026-09-30 06:31:53 CEST, date; nach dem Lauf sp-P4, vor jedem g-Scan)

- Anlass (Ausgang sp-P4, .69, Ende 04:30:52 UTC): Der eingebettete g = 0-Zustand nu = omega + sqrt(E_1) (E_1 = 0,9108,
  angeregter l = 0-Zustand von L_0) wird bei g != 0 zur Resonanz. Ihre Breite ist bei g = 0,2 nur 7,86e-8, bei g = 0,5
  aber 4,19e-6. Das Verhaeltnis 53 passt nicht zu g^2 (6,25).
- Modell (Hand): Amplitude A(g) = g (a + b g^2), Breite ~ A^2. Aus den zwei Werten folgen zwei Faelle:
  - gleiches Vorzeichen: keine Nullstelle, Breite(0,3) ~ 3,7e-7
  - verschiedenes Vorzeichen: Nullstelle bei g* = 0,31
- **Vorab VB1 [H]:** Im g-Scan bei omega^2 = 0,601422 (g = 0,05 bis 0,45) hat -Im nu dieser Resonanz ein tiefes Minimum
  (< 1e-9) bei g* = 0,31 +- 0,05. Das waere eine stille Stelle des psi_2-Problems, also ein Punkt einer Kurve in der
  (omega^2, g)-Ebene.
  - widerlegt, wenn -Im nu monoton waechst (dann gilt der Fall ohne Nullstelle; Pruefwert Breite(0,3) ~ 3,7e-7)
  - widerlegt auch, wenn das Minimum ausserhalb von 0,26 bis 0,36 liegt

## Nachtrag C: 2 omega-Pol entlang g bei omega^2 = 0,551158 (geschrieben ab 2026-09-30 06:40 CEST, date 06:40:08 beim Start; vor dem Ergebnis)

- Anlass (Lauf ueberlapp, Ende 04:39:14 UTC): 2 omega-Pol bei omega^2 = 0,551158 hat bei g = 0,5 die Breite 1,5e-10, die
  goldene Regel erwartet 2,4e-5; bei g = 0,2 ist er 2,8e-6 breit.
- **Vorab VC1 [H]:** -Im nu hat im g-Scan (0,3 bis 0,7) ein Minimum bei g* = 0,50 +- 0,03, nahe g* quadratisch
  (sqrt(-Im nu) linear in g - g*), Tiefe < 1e-9; bei g = 0,3 und 0,7 ueber 1e-7. Das waere ein Punkt einer Kurve stiller
  Stellen des psi_2-Problems in der (omega^2, g)-Ebene.
- widerlegt, wenn kein Minimum < 1e-8 zwischen 0,44 und 0,56 liegt

## Nachtrag D: Runde 9, Karte GF-BIC-2 (geschrieben ab 2026-09-30 07:07:08 CEST, date; vor jeder Rechnung dazu)

Auftrag der Leitung (RUNDE-09.md): Umlauftest fuer die zweite Leiter (Gegenlaeufer), Probe der Abbildung auf beta_eff an
einer Stelle.

### D.1 Verfahren

- W-Abbildung wie bic2.py exakt (Version 3, l = 0), unveraendert importiert:
  - direkt_m: W = L(y_a) + i L(y_b) bei reellem nu
  - lin_fit_nullstelle
  - umlauf_rechteck mit adaptiver Verfeinerung der nu-Seiten und Aufloesungspruefung (groesster Phasensprung < 0,4 rad)
- Neu nur die Koeffizienten je Profil (lin_multi mit eigener Koeffizientenfunktion):
  - psi_2: dp = U'(S), sp = -g J S; dp' = U''(S), sp' = -g J
  - gemischter Ball, symmetrischer Sektor, direkt aus der Zwei-Komponenten-Bewegungsgleichung (PLAN Nachtrag A), in der
    Gesamtdichte S = 2 h^2: dp = U' + S U'' - g J S, sp = S U'' - g J S/2
- Rechteck immer um den Fit-Mittelpunkt:
  - Stufe 1: grobes Gitter um den Keim, Pole, W-Gitter, linearer Fit, Ergebnis (nu*, x*)
  - Stufe 2: je Rechteckbreite dx (5e-4 und 1e-4) fuenf neue Profile bei x* + dx (-1, -1/2, 0, 1/2, 1), zweiter Fit,
    Rechteck um (x*, nu**)
  - Liegt der zweite Fit-Mittelpunkt ausserhalb von 0,8 dx, wird noch einmal um ihn gelegt.
- Profil des gemischten Balls **nativ, nicht aus beta_eff skaliert**: eigenes Schiessen fuer
  h'' + (2/r) h' = [U'(2 h^2) - g J h^2 - omega^2] h. Damit ist der Vergleich mit bic2 bei beta_eff nicht zirkulaer.
  - Geprueft wird die Herleitung der Reduktion (Faktoren von g) und die Skalierung.
  - Der lineare Loeser (RK4, Verbundmatrix) ist in beiden Rechnungen derselbe.
- Ein-Feld-Stelle bei beta_eff = 1/(2 * 1,05^2) = 0,4535147392: bic2.py exakt --beta 0.4535147392 (fremder Code, unveraendert).

### D.2 Vorab

| Nr. | Erwartung | widerlegt, wenn |
|---|---|---|
| VD1 | An jeder der drei psi_2-Stellen hat W eine Nullstelle mit Umlaufzahl +-1 auf beiden Rechtecken um den Fit-Mittelpunkt, aufgeloest (Sprung < 0,4 rad): Z1 (g = 0,2, nahe 0,711), Z2 (g = 0,2, nahe 0,646), Z3 (g = 0,4985, nahe 0,551158) | Umlauf 0 auf einem sauber gelegten, aufgeloesten Rechteck |
| VD2 [H] | Z1 und Z2 sind Nachbarn auf der Leiter und haben entgegengesetzte Umlaufzahlen (I(omega) wechselt dort mit entgegengesetzter Steigung das Vorzeichen) | gleiche Umlaufzahl |
| VD3 | Fit-Mittelpunkte: Z1 omega*^2 in [0,7105; 0,7125], nu* in [1,6880; 1,6900]; Z2 omega*^2 in [0,6455; 0,6475], nu* in [1,607; 1,614]; Z3 omega*^2 in 0,551158 +- 5e-4, nu* in 1,5153 +- 5e-4 | ausserhalb |
| VD4 | beta_eff-Probe, g = 0,2, n = 1: gemischte Stelle (nativ, eigener Code) und Ein-Feld-Stelle (bic2, beta_eff) stimmen in omega*^2 und rho* auf 1e-6 ueberein; beide liegen bei 0,7587 +- 0,001 (lineare Interpolation zwischen beta = 0,45 -> 0,755738 und 0,50 -> 0,797677), rho* bei 1,7117 +- 0,002 | \|Delta omega*^2\| > 1e-5, oder Stelle ausserhalb des Fensters |

- Keime (von Hand aus den Runde-8-Laeufen):
  - Z1: x0 0,7113, nu0 1,68874, d nu/d x 1,17
  - Z2: x0 0,6462, nu0 1,6109, 1,25
  - Z3: x0 0,551158, nu0 1,51526, 1,35
  - beta_eff: x0 0,75869, rho0 1,71173, 0,40
- Spuren: cpu, cpu2, p4000a/b (Leitung, RUNDE-09). Je Aufruf hoechstens 10 min, Stufe h = 0,02 (Profilzeit); wenn Zeit
  bleibt, h = 0,01 als zweite Stufe.

## Nachtrag E: Zusatzlaeufe Runde 9 (geschrieben ab 2026-09-30 07:24:37 CEST, date; nach Z1, Z2, Z3, BG und bic2-beta_eff bei h = 0,02, vor diesen Laeufen)

- Anlass: VD1 bis VD4 sind bei h = 0,02 ausgewertet. Es bleibt Zeit fuer eine zweite Stufe und einen Punkt der Kurve bei
  kleinerem g. K1 (Pipeline-Kontrolle) ist ueberfluessig, weil BG gegen bic2 schon Pol fuer Pol uebereinstimmt; der Lauf
  wurde in der Warteschlange abgebrochen.
- **VE1:** Bei h = 0,01 (drei Profile in Stufe 1, Rechteck dx = 1e-4) bleiben Umlaufzahlen und Fit-Mittelpunkte von Z1 und
  Z2 gleich: omega*^2 auf 2e-6, nu* auf 1e-6 wie bei h = 0,02. Widerlegt bei anderer Umlaufzahl oder groesserer
  Verschiebung.
- **VE2 [H]:** Z1 bei g = 0,1 liegt auf der Kurve zwischen der Nullstelle fuehrender Ordnung (0,71073) und g = 0,2
  (0,711372); bei einer Verschiebung ~ g^2 bei omega*^2 = 0,71089 +- 0,0002, nu* ~ 1,68678 +- 0,0005, Umlauf -1.
  Widerlegt ausserhalb des Fensters oder bei anderer Umlaufzahl.

## Nachtrag F: Karte ROT-2, innerer Rotor des gemischten Balls (geschrieben ab 2026-09-30 07:51:47 CEST, date; vor jedem Lauf dazu)

Auftrag: RUNDE-09.md (Nachtrag ROT-1 bis ROT-3, Freigabe Finn 07:47). Gelesen: RUNDE-09/PAPIER-ROT3.md, W1.1 bis W1.5
(Pseudospin, zweiachsige Anisotropie, kein stationaerer Zwei-Frequenz-Rotor).

### F.1 Reduzierte Dynamik (Hand)

- Relative Phase phi = Delta theta, Ungleichgewicht z = (Q_1 - Q_2)/Q; starre Profile, fuehrende Ordnung in g.
  - Bei g = 0 kostet eine Umverteilung der Ladung nichts (U(2)): Es gibt keine Ladeenergie E_C.
  - Die einzige phi- und z-Abhaengigkeit kommt aus dem Paarterm, -g J int |psi_1|^2 |psi_2|^2 cos 2 phi:

        H(z, phi) = -K (1 - z^2) cos 2 phi,   K ~ g J int h^4

  - Das ist ein reiner Paartunnel-Josephson-Kontakt.
- Folgen [Hand, im reduzierten Modell]:
  - Kleine Schwingung um (0, 0) mit nu_0 (Pseudo-Goldstone, R8 2.4). Die Niveaulinien H = E < 0 sind geschlossen um
    phi = 0.
  - **Laufende Bahnen (phi rotiert ueber die Mulden) gibt es nicht.** Eine Niveaulinie, die alle phi ueberstreicht,
    muesste cos 2 phi mit wechselndem Vorzeichen bei festem Vorzeichen von E erfuellen. Auf der Pseudospin-Kugel ist das
    die Drehung um die mittlere Achse (z, ROT-3 W1.1), also der Tennisschlaeger-Fall: keine Bahnfamilie.
  - Start aus dem Grundzustand mit Kick: z0 = Omega_0/(2 omega) aus Q_a = 2 omega_a N.
    - Die langsame Phase schwingt mit phi_max = (1/2) arccos(1 - z0^2) < pi/4.
    - Frequenz nu(z0) = nu_0 (pi/2) sqrt((2 - z0^2)/2) / K_ell(m), m = z0^2/(2 - z0^2); sie faellt mit der Amplitude.
  - Der Kick (gleiche Profile, verschiedene Geschwindigkeiten) regt zusaetzlich den Gegenlaeufer an (bei g = 0 exakt:
    psi_- = (delta/2 omega) f (e^{-i omega t} - e^{i omega t})). Das ergibt eine **schnelle Schwingung von Delta theta bei
    ~2 omega** mit Amplitude ~Omega_0/(2 omega), die bei 3 omega strahlt (Gegentakt-Gegenlaeufer, Breite ~1,7e-6 an M1,
    R8-Floquet).
  - O(g^2)-Terme (echte Ladeenergie aus der Profilanpassung) koennen laufende Bahnen nahe z -> +-1 erlauben; das liegt
    ausserhalb von Omega_0 < 2 omega.

### F.2 Kanalkinematik der Abstrahlung (Hand)

- Libration mit Frequenz nu:
  - 2. Harmonische im symmetrischen Kanal a, offen fuer omega + 2 nu > 1, also nu > (1 - omega)/2
  - 3. Harmonische im antisymmetrischen Kanal a, offen fuer nu > (1 - omega)/3
- An M1 (omega = 0,869332, 1 - omega = 0,130668; nu_0 = 0,0687 FD) liegen die Grenzen bei 0,06533 bzw. 0,04356.
  - Kleine Libration: 2 nu_0 ist offen, knapp (k ~ 0,12).
  - Wird nu(z0) < 0,06533 (bei z0 > ~0,31, also Omega_0 > ~0,55), schliesst sich der Kanal der 2. Harmonischen.
    [H] Das ist eine amplitudenabhaengige Selbststabilisierung durch die nichtlineare Frequenzverschiebung.
- Schneller Anteil: Kanal 3 omega (Gegentakt-Gegenlaeufer). Stille Stellen dieses Kanals = stille Stellen des
  Gegentakt-Gegenlaeufers (Teil c); an M1 nicht still.
- Die vom Auftrag erwarteten Rotor-Kanaele omega +- 2 Omega mit laufender Phase entfallen, falls F.1 stimmt.

### F.3 Vorab (vor jedem Lauf)

| Nr. | Erwartung (M1: g = 0,216370, omega^2 = 0,755738, gemischter Ball) | widerlegt, wenn |
|---|---|---|
| VF1 [H] | Kein laufender Rotor fuer Omega_0 = 0,05 bis 1,3: der langsame Anteil von Delta theta bleibt beschraenkt, keine Schwelle | Delta theta (tiefpassgefiltert) laeuft um mehr als pi weiter |
| VF2 [H] | Langsame Schwingung: phi_max und nu gemaess F.1 auf +-30 % bzw. +-20 %: Omega_0 = 0,1 / 0,3 / 0,6 / 0,9 / 1,3 -> phi_max = 0,041 / 0,122 / 0,246 / 0,375 / 0,557 rad; nu = 0,0686 / 0,0679 / 0,0655 / 0,0613 / 0,0518 | ausserhalb |
| VF3 | Schneller Anteil: Linie bei ~2 omega = 1,739 in Delta theta, Amplitude ~Omega_0/(2 omega) (+-30 %, kleine Kicks) | fehlt oder Amplitude ausserhalb |
| VF4 | g = 0: Q_1 und Q_2 einzeln erhalten (bis auf den Randfluss), kein langsamer Anteil, nur die 2 omega-Schwingung | Drift von Q_1 - Q_2 oder langsame Schwingung |
| VF5 [H] | Energiefluss durch r = 20: bei kleinen Kicks Linien bei 3 omega (~2,61) und omega + 2 nu (~1,007); bei Omega_0 >= 0,6 faellt die Linie omega + 2 nu weg (Kanal zu) | Linie omega + 2 nu auch bei Omega_0 >= 0,6 deutlich, oder bei kleinen Kicks keine der Linien |
| VF6 | Zwei Gitter (Delta 0,1 gegen 0,05) aendern nu und phi_max um weniger als 2 % | mehr |
| VF7 [H], Teil c | Der Gegentakt-Gegenlaeufer (nu ~ 2 omega) hat stille Stellen; bei kleinem g nahe der psi_2-Leiter (0,711, 0,646, ...), mit Umlauf +-1 | kein Minimum der Breite in +-0,01 um die Leiter |

### F.4 Nachtrag zu Teil (c), vor dessen Laeufen (2026-09-30 07:56:50 CEST, date)

- Gegentakt-Gegenlaeufer: Seine Frequenz ist gegen 2 omega verschoben. Zwei-Moden-Naeherung: nu_G ~ sqrt(4 omega^2 +
  3 alpha), alpha = 2 g J <h^4>/<h^2>. An M1 (g = 0,216) sind das ~1,825 statt 2 omega = 1,739.
  - Bei g = 0,216 liegen die stillen Stellen deshalb nicht bei der psi_2-Leiter, weil sich der Kanal a mitverschiebt.
    VF7 wird bei kleinem g geprueft: g = 0,05, Raster 0,700 bis 0,722 und 0,636 bis 0,656 (Schritt 0,002).
  - Danach Umlauftest am Minimum nahe 0,711.
- **VF7 konkret:** Die Breite hat bei g = 0,05 in beiden Fenstern je ein Minimum, das mindestens zehnmal tiefer ist als
  die Randpunkte (oder unter der Gitter-Untergrenze ~5e-9 liegt); am Minimum Umlauf +-1.

### F.5 Vorab fuer den Vergleichslauf M3 (Lauf D, noch in der Warteschlange; 2026-09-30 07:57:35 CEST, date)

- M3: g = 0,472136, omega^2 = 0,566347, omega = 0,752560, 1 - omega = 0,24744, nu_0 = 0,2182 (FD, R8).
- Kanaele:
  - 2 nu offen fuer nu > 0,1237
  - 3 nu offen fuer nu > 0,0825
  - beide fuer alle Kicks offen, anders als an M1
- **VF8 [H]:** kein laufender Rotor. Reduziertes Modell bei Omega_0 = 0,1 / 0,3 / 0,6 / 1,0:
  - phi_max = 0,047 / 0,141 / 0,286 / 0,489 rad
  - nu = 0,218 / 0,215 / 0,205 / 0,178
  - Toleranzen +-30 % bzw. +-25 % (grosser Ball, die Zwei-Moden-Naeherung lag dort bei nu_0 24 % daneben)

### F.6 Reine Libration ohne schnellen Anteil (2026-09-30 08:05:30 CEST, date; nach Lauf A, vor diesem Lauf)

- Anlass (Lauf A, M1, Ende 06:04:30 UTC):
  - Die Kicks regen den schnellen Gegenlaeufer (Linie 1,811) mit ~Omega_0/(2 omega) an. Er strahlt bei omega + nu_G und
    in Kombinationslinien und ueberdeckt im Gesamtfluss die 2. Harmonische der Libration.
  - Die Linie omega + 2 nu (1,0069 bis 1,0043) ist bei Kick 0,05 bis 0,3 im Spektrum sichtbar und fehlt ab 0,6.
- Neuer Start "ungleich": psi_1 = sqrt(1 + z0) h, psi_2 = sqrt(1 - z0) h, beide mit omega.
  - Bei g = 0 ist das eine U(2)-Drehung des Balls, also exakt stationaer.
  - Bei g != 0 liegt der Start auf der langsamen Mannigfaltigkeit: Libration mit Amplitude z0, praktisch ohne schnellen
    Anteil (O(g z0)).
- **VF9 [H]:** An M1 (nu_0 = 0,06877 gemessen) schliesst der Kanal omega + 2 nu bei nu(z0) < 0,065334, nach F.1 bei
  z0 ~ 0,36.
  - Erwartung fuer z0 = 0,05 / 0,1 / 0,2 / 0,3 / 0,35 / 0,4 / 0,5 / 0,6:
    - nu = 0,0687 / 0,0685 / 0,0677 / 0,0664 / 0,0655 / 0,0645 / 0,0619 / 0,0586
    - Energiefluss steigt bis z0 ~ 0,3 etwa wie z0^4 und faellt ab z0 = 0,4 um mindestens den Faktor 10 gegen z0 = 0,3
      (nur noch der Kanal 3 nu, Amplitude ~ z0^3).
  - Das waere die Selbststabilisierung durch die nichtlineare Frequenzverschiebung.
  - Widerlegt, wenn der Fluss bei z0 = 0,4 bis 0,6 nicht mindestens zehnmal unter dem Wert bei 0,3 liegt.

### F.7 Nach dem Gegentakt-Scan, vor den Umlauftests (2026-09-30 08:09 CEST, date beim Schreiben)

- Scan g = 0,05 (Ende 06:08:00 UTC): In beiden Fenstern faellt die Breite zum unteren Rand hin unter die
  Gitter-Untergrenze (~5e-9 bei h = 0,02) und steigt nach oben (4,3e-8 bei 0,722; 1,7e-7 bei 0,656).
  - Die Minima liegen also unten am Fenster: nahe 0,703 bis 0,706 und bei <= 0,637. Die psi_2-Leiter liegt bei 0,7107
    und 0,6457.
  - Die Breite allein trennt das nicht auf. Deshalb Umlauftests.
- **VF7a [H]:** Umlauf +-1 bei x* = 0,705 +- 0,003 (Keim nu 1,70425) und bei x* = 0,633 +- 0,006 (Keim nu 1,6250), mit
  entgegengesetzten Vorzeichen (Nachbarn auf der Leiter).

### F.8 Direkter Test "Hauptkanal auf stiller Stelle" (2026-09-30 08:17:30 CEST, date; nach AG1/AG2 und E, vor diesem Lauf)

- Die Umlauftests ergaben bei g = 0,05 eine Gegentakt-Leiter mit stillen Stellen:
  - 0,702252, Umlauf -1
  - 0,635507, Umlauf +1
- Ein Kick (Omega_0 = 0,3) regt dort den schnellen Gegenlaeufer an. Sein direkter Strahlungskanal ist psi_- bei
  omega + nu_G.
- **VF10:** Bei omega^2 = 0,702252 (still) ist die Linie von psi_- bei omega + nu_G (~0,838 + 1,701 = 2,539) im Spektrum bei
  R_m mindestens zehnmal schwaecher als bei omega^2 = 0,690 und 0,715 (nicht still), bei gleichem Kick. Die
  Kombinationslinien omega + nu_G +- nu im symmetrischen Kanal duerfen bleiben.

### F.9 Nach VF10, vor dem Nachlauf mit kleinem Kick (gespeichert 2026-09-30 08:20:00 CEST laut date direkt danach; die zuerst eingetragene Zeit 08:20:40 war geschaetzt und falsch; berichtigt um 08:20:11 laut date)

- Ausgang VF10 (Kick 0,3, Delta 0,1): Die Linie omega + nu_G in psi_- ist an der stillen Stelle nicht zehnmal schwaecher.
  Gemessen 5,4e-6 gegen 1,02e-5 (0,690) und 3,2e-6 (0,715). **VF10 widerlegt.**
- Moegliche Gruende (von Hand):
  - Nahe der Stelle ist Gamma ~ C (x - x*)^2 mit kleinem C (bei g = 0,05 etwa 1,6e-4). Die Amplitude faellt also nur
    linear in |x - x*|; die Referenzen liegen nur 0,012 weg.
  - Die Nullstelle des FD-Gitters (Delta 0,1) ist gegen x* = 0,702252 (Schiessen) verschoben.
  - Bei Kick 0,3 fallen nichtlineare Kombinationen (schnell x langsam x langsam) auf dieselbe Frequenz.
- **VF11:** Kick 0,05, Delta 0,05: An 0,702252 ist die Linie omega + nu_G in psi_- mindestens fuenfmal schwaecher als
  an 0,690 und an 0,715. Widerlegt, wenn nicht.

### F.10 Nach der Pause: T2 aus ROT-3 und Separatrix (gespeichert 2026-09-30 09:57:10 CEST laut date direkt danach; zuerst stand hier eine geschaetzte Zeit)

- Leitung 09:51: ROT-3 erwartet oberhalb der Separatrix Rotoren mit beliebiger Drehrate und ein ruhiges Fenster
  0 < Omega_r < (2/3)(1 - omega) (0,087 an M1). T2 prueft den Sprung der Verlustrate an dieser Schwelle.
- Stand hier:
  - Lauf A ist der T2-Aufbau (Frequenzversatz omega +- delta ueber die Anfangsgeschwindigkeit). Bis Omega_0 = 1,3 kein
    Rotor, bei 1,7 ein Uebergangsrotor mit Omega_r ~ 0,15, also ueber der Schwelle.
  - Nach F.1 gibt es ohne echte Ladeenergie ueberhaupt keine Rotorbahnen.
- Zusatzlauf H: Start "ungleich" nahe der Separatrix, z0 = 0,8 / 0,9 / 0,95 / 0,99 (ohne schnellen Anteil).
- **VF12 [H]** (reduziertes Modell F.1):
  - kein Laufen
  - phi_max = 0,601 / 0,690 / 0,737 / 0,775 rad (-> pi/4)
  - nu = 0,0406 / 0,0346 / 0,0255 (0,8 nicht vorab)
  - Toleranz phi_max +-15 %, nu +-30 %
  - Widerlegt, wenn die langsame Phase um mehr als pi weiterlaeuft.
