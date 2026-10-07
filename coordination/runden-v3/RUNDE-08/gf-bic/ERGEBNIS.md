# GF-BIC (Runde 8): Ergebnis

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3), keine formale Bestaetigung.
- Zeitkette (alle Zeiten mit date gemessen, CEST; die .69 loggt in UTC = CEST - 2 h):
  - Beginn 05:57:52
  - PLAN.md mit Vorab-Tabelle ab 06:13:15, gespeichert 06:14:34 (Kopie PLAN.md.eingefroren-20260930-0615)
  - Rauchtest lokal 06:22:06 bis 06:22:42
  - Laeufe auf der .69 ab 06:23:39
  - Nachtraege mit Vorab, jeweils vor dem zugehoerigen Lauf bzw. vor dessen Ergebnisdatei:
    - A (gemischter Ball) ab 06:26:18 (Kopie -0627)
    - B (g-Scan P4) ab 06:31:53 (Kopie -0633)
    - C (g-Scan 2 omega) um 06:40:19; der Lauf startete 06:40:08, seine Ergebnisdatei entstand erst danach (Kopie -0640)
  - Entwurf ab 06:37:09, Endfassung ab 06:48:00
- Belegstufen:
  - **[Hand]** Herleitung
  - **[num]** numerisch einfach
  - **[num+K]** numerisch mit Kontrolle (zweites Verfahren, zweite Stufe oder Nullprobe)
  - **[H]** Hypothese
- Modell, Gleichungen und Vorzeichen: PLAN.md, Abschnitt 1.
  - psi_2 = e^{-i omega t}(u e^{-i nu t} + v^* e^{i nu^* t})
  - im ODE-Format dp = U'(S), sp = -g J S; J = 1
  - Im nu > 0 heisst anwachsend, Im nu < 0 abklingend (wie resonanz3d.py)
- Stellen:
  - P1 = 0,797677 (rho* 1,744618)
  - P2 = 0,685129
  - P3 = 0,631449 (rho* 1,652588)
  - P4 = 0,601422 (rho* 1,628113)
  - P5 = 0,582417 (rho* 1,611309)

## 0. Ergebnis in fuenf Punkten

1. **Frage 2, Verlustkanal O(epsilon^2) in die zweite Komponente: nein, nicht gesehen.**
   - Direkt ausgeschlossen [Hand, exakt]: psi_2 -> -psi_2 ist eine Symmetrie. Ein leeres psi_2 bleibt in jeder Ordnung von
     epsilon leer.
   - Parametrisch [num+K]: Floquet mit der stillen Atmungsmode als Pumpe (epsilon <= 0,04, normiert wie Codex) zeigt keine
     neue instabile Mode.
     - geprueft um den einkomponentigen Ball (P1, P3; g = 0 bis 1) und im antisymmetrischen Sektor des gemischten Balls
       (drei stille Stellen der beta_eff-Familie)
     - obere Schranke fuer eine neue Rate: 1e-5 bzw. 1e-6
   - Die Pumpe verschiebt nur vorhandene Raten wie epsilon^2 (hoechstens 0,4 % von lambda).
   - Die Pseudo-Goldstone-Mode des gemischten Balls wird von der Pumpe sogar **gedaempft** (Vorab VG3 "waechst"
     widerlegt).
2. **Frage 1, Spektrum: Der einkomponentige Ball ist instabil, sobald g != 0.**
   - Fuer kleines \|g\| folgt das von Hand aus der Index-Zaehlung (PLAN 1.4) [Hand, L?].
   - Numerisch gilt es bei allen gerechneten g (+-0,2 / 0,5 / 1,0) an allen fuenf Stellen [num+K, zwei Verfahren auf
     1e-7].
   - Die Nullmode wandert auf die imaginaere Achse: nu = +-i lambda.
     - lambda = 0,046 (P1) bis 0,116 (P5) bei g = 0,2
     - lambda = 0,29 bis 0,61 bei g = 1
   - Grosse Baelle haben bis zu drei instabile Paare, immer genau n(L_u).
   - Deutung [Hand]: Paarumwandlung psi_1 psi_1 -> psi_2 psi_2, exakt resonant. Zeitskala 2 bis 6 Atmungsperioden bei
     g = 0,2.
   - Resonanzen:
     - Gegenlaeufer bei 2 omega, Breite ~ g^2: 3e-6 bis 1e-5 bei g = 0,2. Die goldene Regel trifft an P1 auf 0,2 %.
     - omega + sqrt(E_1) an P4 und P5, sehr schmal
   - Echt gebundene psi_2-Zustaende gibt es an P2 bis P5, je nach g.
3. **Gesamtformel** [Hand, exakt; Skalierung numerisch kontrolliert]:
   - Der natuerliche Zustand bei g != 0 ist der gemischte Ball.
   - Sein symmetrischer Unterraum ist nichtlinear invariant und exakt das N = 1-Modell mit
     beta_eff = 1/(2 (1 + g/4)^2). Das Fenster ist KANDIDAT 5.3.
   - Die stillen Stellen bleiben also erhalten, verschoben: zum Beispiel beta_eff = 0,45 bei g = 0,216.
   - Eine rein symmetrische Atmung verliert nach demselben Mechanismus wie bei N = 1. Codex hat dort einen Fluss ~ eps^4
     gemessen, bei beta = 0,5; fuer beta_eff ist das nicht gerechnet.
   - Der antisymmetrische Sektor ist linear stabil.
4. **Frage 3, stille Stellen des psi_2-Problems: ja.**
   - In fuehrender Ordnung hat die Gegenlaeufer-Breite Nullstellen bei omega^2 ~ 0,866 / 0,711 / 0,646 / 0,611 und
     dichter darunter (acht im Raster).
   - Die Abstaende in 1/(omega^2 - 1/2) von 2,0 bis 2,3 gleichen der Atmungsleiter [H].
   - Bei endlichem g gibt es zwei gerechnete Punkte solcher Kurven:
     - (omega^2, g) ~ (0,5512; 0,4985): scharfes quadratisches Minimum -Im nu < 6e-10 [num+K, zwei Stufen]
     - bei g = 0,2 nahe 0,711: Einbruch um mehr als 500 [num]
     - jeweils kein Umlauftest
   - Die omega + sqrt(E_1)-Resonanz hat keine Nullstelle fuer g <= 0,45 (VB1 widerlegt).
5. **Kontrollen, Vorab, Zeiten:**
   - N = 1-Pol 1,7018102865 - 1,468e-3 i reproduziert
   - BIC P1: \|Im\| = 1,5e-10
   - g = 0: Nullmode (D ~ nu^2) und eingebetteter 2 omega-Zustand
   - g <-> -g und Floquet eps <-> -eps bitgleich
   - Vorab: 12 getroffen, 2 teilweise, 2 verfehlt, 2 widerlegt (Tabelle 5)
   - Rechenzeit gemessen: Abschnitt 6

## 1. Frage 1: Spektrum der zweiten Komponente um den einkomponentigen Ball (N = 2, J = 1)

### 1.1 Die Nullmode wird zur Instabilitaet, bei jedem g != 0

- Bei g = 0 hat psi_2 die doppelte Nullmode nu = 0 (u = f oder v = f). Das ist die U(2)-Drehung des Balls in Komponente
  2.
  - Kontrolle [num+K]: \|D(0)\| = 3e-13 bis 2e-12 und \|D(2e-3)\|/\|D(1e-3)\| = 4,000 (doppelte Nullstelle) an allen Stellen
- Bei g != 0 wandert sie **auf die imaginaere Achse**: nu = +-i lambda, rein imaginaer mit \|Re nu\|/Im nu < 1e-16.
  - Das ist eine exponentielle Instabilitaet, keine Schwingung.
  - Die Zahl der instabilen Paare ist genau n(L_u), die Zahl negativer Eigenwerte von
    L_u = -Lap + U'(f^2) - omega^2 - g J f^2 (Hamilton-Krein-Zaehlung, PLAN 1.4) [num+K].
- Zwei Verfahren stimmen auf 1e-7 relativ oder besser ueberein [num+K]: Schiessen mit h = 0,01 gegen den FD-Kasten mit
  Richardson aus Delta = 0,1 und 0,05. Beispiele:
  - P1, g = 0,2: 0,04623841549 gegen 0,04623842001
  - P5, g = 1,0: 0,61442705585 gegen 0,61442705585

| Stelle | omega^2 | kappa = <f^4>/<f^2> | lambda (g = 0,2) | lambda/lambda_2 | lambda (0,5) | lambda/lambda_2 | lambda (1,0) | lambda/lambda_2 | n(L_u) bei 0,2 / 0,5 / 1,0 | weitere Paare |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 0,797677 | 0,404646 | 0,0462384 | 1,0209 | 0,1260051 | 1,1147 | 0,2942843 | 1,3093 | 1 / 1 / 1 | - |
| P2 | 0,685129 | 0,629742 | 0,0782615 | 1,0297 | 0,2169188 | 1,1479 | 0,4809512 | 1,2957 | 1 / 1 / 1 | - |
| P3 | 0,631449 | 0,737102 | 0,0963613 | 1,0406 | 0,2682450 | 1,1687 | 0,5608535 | 1,2561 | 1 / 1 / 2 | 0,2855486 (g = 1) |
| P4 | 0,601422 | 0,797156 | 0,1079895 | 1,0529 | 0,2974012 | 1,1727 | 0,5966011 | 1,2174 | 1 / 2 / 2 | 0,1304327 (0,5); 0,4293061 (1) |
| P5 | 0,582417 | 0,835166 | 0,1163026 | 1,0655 | 0,3139435 | 1,1652 | 0,6144271 | 1,1858 | 1 / 2 / 3 | 0,2087694 (0,5); 0,5045621 und 0,2673510 (1) |

- lambda_2 ist die Zwei-Moden-Formel (PLAN 1.4) mit kappa aus demselben Profil.
  - Bei g = 0,2 trifft sie auf 2 bis 7 %.
  - Bei groesserem g und groesserem Ball unterschaetzt sie lambda um bis zu 31 %. Das passt zu Korrekturen O(g^2) durch
    die uebrigen Moden [Hand].
- g <-> -g: an allen Stellen bitgleich, auch die 2 omega-Pole [num+K]. Das ist die Symmetrie psi_2 -> i psi_2 (PLAN 1.3).
- Zeitskala bei g = 0,2: 1/lambda = 22 (P1) bis 8,6 (P5), also 2 bis 6 Atmungsperioden (T = 2 pi/rho* ~ 3,6 bis 3,9).
- Deutung [Hand, PLAN 1.4]:
  - Paarumwandlung psi_1 psi_1 -> psi_2 psi_2, exakt resonant, weil beide Komponenten dieselbe Frequenz haben.
  - In der Zwei-Moden-Naeherung hat die wachsende Mode die relative Phase 45 Grad. Dort ist der Kanalstrom T_12
    (KANDIDAT 4.2) am groessten. Das ist nur von Hand; der Eigenvektor ist nicht ausgewertet.
  - Der Ball dreht sich in einen gemischten Zustand. Das ist das lokalisierte Gegenstueck zum Ueberlaufband (UEBERLAUF.md).

### 1.2 Echt gebundene Zustaende (0 < nu < 1 - omega), reell [num+K: Schiessen A/B und FD]

| Stelle | 1 - omega | g = 0 | g = 0,2 | g = 0,5 | g = 1,0 |
|---|---|---|---|---|---|
| P1 | 0,106872 | nur Nullmode | keiner | keiner | keiner |
| P2 | 0,172275 | nur Nullmode | keiner | keiner | 0,1313889 |
| P3 | 0,205362 | nur Nullmode | 0,2011852 | 0,1347440 | keiner (wird das 2. instabile Paar) |
| P4 | 0,224486 | 0,1788881 = sqrt(E_1) - omega | 0,1502099 | keiner (2. instabiles Paar) | 0,1474909 |
| P5 | 0,236838 | 0,1370497 = sqrt(E_1) - omega | 0,0875079 | 0,2107787 | keiner (3 instabile Paare) |

- E_1 ist der angeregte l = 0-Zustand von L_0 = -Lap + U'(f^2): E_1 = 0,91080 (P4) und 0,81032 (P5).
- An P1 bis P3 hat L_0 unter 1 nur E_0 = omega^2 (Kontrolle in Abschnitt 4).
- Die gebundenen Zustaende wandern mit wachsendem g zu nu = 0 und werden dort zum naechsten instabilen Paar
  (n(L_u) waechst).

### 1.3 Resonanzen im offenen Fenster 1 - omega < nu < 1 + omega [num+K: Schiessen A/B]

**Gegenlaeufer nu ~ 2 omega** (bei g = 0: v = f, psi_2 = f e^{+i omega t}, eingebettet, Breite 0):

| Stelle | g = 0 (in Klammern 2 omega) | g = 0,2 | g = 0,5 | g = 1,0 | Im(0,5)/Im(0,2) |
|---|---|---|---|---|---|
| P1 | 1,7862553061 + 1,5e-10 i (1,7862553) | 1,7872051 - 3,329e-6 i | 1,7920569 - 2,114e-5 i | 1,8077033 - 8,269e-5 i | 6,35 |
| P2 | 1,6554503947 + 7e-11 i (1,6554504) | 1,6578144 - 7,866e-6 i | 1,6696278 - 5,325e-5 i | 1,7050005 - 2,052e-4 i | 6,77 |
| P3 | 1,5892753083 + 4e-11 i (1,5892753) | 1,5926081 - 9,818e-6 i | 1,6090445 - 6,775e-5 i | 1,6562009 - 1,985e-4 i | 6,90 |
| P4 | 1,5510280474 + 3e-11 i (1,5510281) | 1,5550101 - 1,0487e-5 i | 1,5744819 - 7,044e-5 i | 1,6287699 - 1,115e-4 i | 6,72 |
| P5 | 1,5263249991 + 2e-11 i (1,5263250) | 1,5307647 - 1,0478e-5 i | 1,5523448 - 6,525e-5 i | 1,6112185 - 2,544e-5 i | 6,23 |

- Alle abklingend. Bei kleinem g waechst die Breite wie g^2 (goldene Regel, 3.1).
- An P5 ist die Breite bei g = 1,0 kleiner als bei 0,5. [H] Dort laeuft eine Kurve stiller Stellen vorbei (3.3).
- Physik [Hand]: Ein gegenlaeufiger psi_2-Anteil am Ball strahlt ueber den Paarterm bei der Frequenz 3 omega ab.

**Angeregter Zustand nu ~ omega + sqrt(E_1)** (P4, P5; bei g = 0 eingebettet mit \|Im\| ~ 1e-10):

| Stelle | g = 0 | g = 0,2 | g = 0,5 | Im(0,5)/Im(0,2) |
|---|---|---|---|---|
| P4 | 1,7299162 | 1,7327072 - 7,86e-8 i (Stufe A: -7,52e-8) | 1,7466841 - 4,190e-6 i | 53 |
| P5 | 1,6633747 | 1,6670393 - 3,35e-8 i (Stufe A: -3,09e-8) | 1,6856261 - 2,210e-6 i | 66 |

- Das Verhaeltnis passt nicht zu g^2 (6,25). Der g-Scan dazu steht in 3.3.
- Breite Pole nahe der Kante, bei g = 0 und 0,2 [num]:
  - P4: 0,389 - 0,130 i
  - P5: 0,287 - 0,055 i und 0,551 - 0,159 i
  - Das sind Formresonanzen des Topfes U'(f^2) knapp ueber der Kante. Sie sind breit (Lebensdauer < 20) und spielen fuer die
    Fragen keine Rolle.

### 1.4 Abgleich mit KANDIDAT 5.2 und 5.3 [Hand, Nachtrag A numerisch]

- Der einkomponentige Ball existiert fuer jedes g im Fenster 1/2 < omega^2 < 1, weil der Paarterm auf ihm identisch
  verschwindet. Die Vakuumschranke 5.2 (\|g\| J <= 1,657) begrenzt ihn nicht.
- Er ist aber fuer jedes g != 0 ein Sattel (1.1). Der natuerliche Zustand ist der gemischte Ball:
  - psi_1 = psi_2 bei g > 0, psi_2 = +-i psi_1 bei g < 0
  - U_eff = S - (1 + \|g\| J/4) S^2 + S^3/2; sein Fenster ist genau 5.3
- Der symmetrische Unterraum psi_1 = psi_2 ist **nichtlinear invariant** und exakt das N = 1-Modell der beta-Familie mit
  beta_eff = 1/(2 (1 + g J/4)^2) [Hand]. Werte: g = 0,2 -> 0,4535; g = 0,5 -> 0,3951; g = 1,0 -> 0,32.
  - Kontrolle [num]: L_eff = -Lap + U' - g J S/2 - omega^2 hat auf dem skalierten Profil den tiefsten Eigenwert -1e-4 bis
    -3e-5 (FD-Fehler von 0), an allen drei Punkten.
  - **Folge:** Der gemischte Ball hat stille Atmungsstellen an den Stellen der beta-Familie bei beta_eff. Die symmetrische
    Atmung ist dort exakt die N = 1-Atmung des beta_eff-Modells, auch nichtlinear. Codex' eps^4-Fluss ist bei beta = 0,5
    gemessen, nicht bei beta_eff.
- Antisymmetrischer Sektor (psi_1 - psi_2):
  - L_p = L_eff + g J S und L_q = L_eff + 2 g J S, beide positiv definit [Hand]
  - FD an drei Stellen: keine Instabilitaet [num]
  - Die Drehung in der Komponentenebene wird zur Pseudo-Goldstone-Mode nu_0 = 0,0687 / 0,1306 / 0,2182 (M1 / M2 / M3,
    Tabelle in 2.4).

## 2. Frage 2: Parametrische Kopplung durch die Atmung

### 2.1 Kein direkter Kanal [Hand, exakt]

- psi_2 -> -psi_2 ist eine Symmetrie, also ist psi_2 = 0 invariant ("in einen exakt leeren Kanal geht nichts",
  KANDIDAT 4.2).
- Eine Atmung in psi_1 treibt deshalb **in keiner Ordnung von epsilon** einen Fluss in ein leeres psi_2. psi_1 allein
  folgt exakt der N = 1-Dynamik.
- Neues kann nur aus Keimen wachsen (Instabilitaet oder parametrische Verstaerkung).
- Dasselbe gilt fuer den gemischten Ball: Sein symmetrischer Unterraum ist invariant (1.4).

### 2.2 Paare nu_a + nu_b ~ rho*

- Zwei gebundene Moden reichen nie [Hand]: Beide liegen unter 1 - omega. An den vier Stellen mit bekanntem rho* ist
  2 (1 - omega) = 0,21 / 0,41 / 0,45 / 0,47, rho* aber 1,61 bis 1,74.
- Jede Summenresonanz braucht also einen Kontinuumspartner oder einen Resonanzpol.
  - Einen Kontinuumspartner gibt es fuer jede gebundene Mode (rho* - nu_k > 1 - omega).
  - Moeglich ist damit nur eine goldene-Regel-Rate O(epsilon^2), keine Zunge erster Ordnung.
- Bei g = 0 im Laborsystem [Hand]:
  - Summenresonanz mit Kontinuum braucht Omega_a <= rho* - 1 < omega. Das ist an den vier Stellen mit bekanntem rho*
    unmoeglich.
  - Gebunden plus gebunden braucht rho* >= 2 omega; an P1 unmoeglich.
- Auffaelligste Naehe: Gegenlaeufer minus Pumpe.
  - 2 omega - rho* = +0,042 (P1); rho* - 2 omega = 0,063 / 0,077 / 0,085 (P3 / P4 / P5)
  - Dort liegt keine psi_2-Mode; die Nullmode ist bei g != 0 imaginaer.

### 2.3 Floquet, einkomponentiger Ball (P1, P3) [num+K]

- Pumpe = BIC-Mode, normiert max\|a + b\| = 1 wie Codex.
- Verfahren:
  - Monodromie ueber eine Periode 2 pi/rho_FD fuer (P, Q, P_t, Q_t) im FD-Kasten (Delta 0,1, R 40, Schwamm 12)
  - Pumpe aus dem N = 1-FD-Kasten: rho_FD = 1,744508 (P1) und 1,652390 (P3), Lokalisierung 0,99999 bzw. 0,99997
- Kontrollen:
  - epsilon = 0 gibt lambda aus dem Eigenwertproblem auf 1e-9 wieder.
  - epsilon und -epsilon sind bitgleich (erwartet: Zeitverschiebung um T/2).
  - Die 2 omega-Resonanz erscheint mit der Rate -3,40e-6 (Pol: -3,33e-6).
- **g = 0:** groesste Rate <= 1,9e-8 bei epsilon = 0,04 (P1 und P3). Keine parametrische Verstaerkung, wie von Hand
  erwartet.
- **g != 0:** Die einzige wachsende Mode bleibt das lambda-Paar (bzw. die n(L_u) Paare). **Keine neue instabile Mode**
  (Schwelle 1e-5) bis epsilon = 0,04.
- Die Pumpe verschiebt lambda um c epsilon^2. Exponent aus 0,01 -> 0,02 -> 0,04: 1,97 bis 2,00.

| Stelle | g | lambda (eps = 0) | Delta bei eps = 0,02 | Delta bei eps = 0,04 | c = Delta/eps^2 | relativ bei 0,04 |
|---|---|---|---|---|---|---|
| P1 | 0,2 | 0,046253869 | +9,89e-6 | +3,883e-5 | +0,024 | +0,08 % |
| P1 | 0,5 | 0,126057547 | -1,272e-4 | -5,106e-4 | -0,32 | -0,41 % |
| P1 | 1,0 | 0,294430927 | -2,991e-4 | -1,2013e-3 | -0,75 | -0,41 % |
| P3 | 0,2 | 0,096363385 | +2,323e-5 | +9,288e-5 | +0,058 | +0,10 % |
| P3 | 0,5 | 0,268261257 | -3,684e-5 | -1,473e-4 | -0,092 | -0,05 % |
| P3 | 1,0 | 0,56088 / 0,285831 | -4,89e-5 / -1,66e-4 | -1,956e-4 / -6,68e-4 | -0,12 / -0,42 | -0,03 / -0,23 % |

- lambda stammt hier aus dem FD-Kasten mit Delta 0,1; die Abweichung zum Schiessen ist < 1e-4 relativ.
- Konvergenz (P1, g = 0,2), Delta bei eps = 0,04 [num+K]:
  - +3,883e-5 (Delta 0,1, R 40)
  - +3,823e-5 (R 60, Schwamm 20 statt 12, sigma0 1,0 statt 1,5)
  - +3,866e-5 (Delta 0,075)
  - bei g = 0,5: -5,106e-4 gegen -5,003e-4 (R 60)
  - c ist also auf etwa 2 % bestimmt.
  - Die 2 omega-Rate geht mit feinerem Gitter von -3,40e-6 auf -3,35e-6, gegen den Pol -3,33e-6.
- Gebundene psi_2-Moden unter der Pumpe (P3):
  - g = 0,5 (nu = 0,1347): Daempfung -8,5e-7 / -3,40e-6 / -1,35e-5 bei epsilon = 0,01 / 0,02 / 0,04, also -8,5e-3 epsilon^2.
    Die Hochmischung ins Kontinuum ueberwiegt.
  - g = 0,2 (nu = 0,2012, knapp unter der Kante, reicht in den Schwamm): Basisrate -1,0e-5 (Schwamm), Aenderung durch die
    Pumpe +1,4e-7 bei 0,04, also +8,5e-5 epsilon^2
  - Beide Effekte sind um den Faktor 2e4 bis 7e5 kleiner als lambda an derselben Stelle.
  - Die Schwamm-Empfindlichkeit dieser kleinen Raten ist nur am gemischten Ball geprueft (2.4, Faktor 2 bis 3).

### 2.4 Floquet, gemischter Ball [num+K]

- Antisymmetrischer Sektor, Pumpe ist die symmetrische Atmung.
- Stellen mit bekannter stiller Stelle der beta-Familie (Nachtrag A):
  - M1, M2 bei beta_eff = 0,45 (g = 0,216370)
  - M3 bei beta_eff = 0,40 (g = 0,472136)

| Punkt | omega^2 | nu_0 (FD) | nu_0 Zwei-Moden | Verh. | Pumpe rho_FD (bekannt) | Lokal. | Rate nu_0 bei eps = 0 / 0,01 / 0,02 / 0,04 | groesste Rate insgesamt |
|---|---|---|---|---|---|---|---|---|
| M1 | 0,755738 | 0,0687385 | 0,0778573 | 0,883 | 1,709131 (-) | 0,99999 | -2e-10 / -2,3e-8 / -8,9e-8 / -3,17e-7 | <= -2e-10 |
| M2 | 0,577365 | 0,1305624 | 0,1464161 | 0,892 | 1,601872 (1,602162) | 0,99992 | 0 / -1,39e-7 / -5,54e-7 / -2,19e-6 | <= 0 |
| M3 | 0,566347 | 0,2182124 | 0,2858922 | 0,763 | 1,583414 (1,583776) | 0,99946 | -1,1e-7 / -3,53e-6 / -1,378e-5 / -5,44e-5 | <= -1,1e-7 |

- Die Summenresonanz nu_0 + (rho - nu_0) mit einem Partner im offenen Kanal ist an allen drei Punkten erfuellt:
  rho - nu_0 = 1,640 / 1,471 / 1,365, Kante 0,131 / 0,240 / 0,247.
- Trotzdem **waechst nichts**: Die Pumpe **daempft** die Pseudo-Goldstone-Mode mit -2e-4 / -1,4e-3 / -0,034 epsilon^2.
  Die Hochmischung nu_0 + rho ins Kontinuum ueberwiegt die Paarerzeugung.
- epsilon und -epsilon gleich; keine Mode mit Rate > 1e-6.
- Konvergenz der Daempfung (nu_0-Rate bei eps = 0,02 / 0,04) [num+K]:
  - M3: -1,378e-5 / -5,44e-5 (Delta 0,1, R 40); -1,483e-5 / -5,86e-5 (Delta 0,075); -3,32e-5 / -1,334e-4 (R 60,
    Schwamm 20)
  - M2: -5,54e-7 / -2,19e-6 (R 40); -3,57e-7 / -1,40e-6 (R 60)
  - Das Vorzeichen (Daempfung) und die Skalierung eps^2 (Faktor 3,9 bis 4,0 je Verdopplung) halten in allen Varianten.
  - Die Groesse haengt am Kasten bzw. Schwamm (Faktor 0,6 bis 2,4).
    - Die goldene-Regel-Rate braucht die Kontinuumsdichte, und die gibt der Kasten mit Schwamm nur ungefaehr wieder.
    - Die Koeffizienten sind deshalb nur auf einen Faktor 2 bis 3 bestimmt.

### 2.5 Antwort auf Frage 2

**Nein, nicht gesehen.**
- Einen direkten Verlustkanal O(epsilon^2) in die zweite Komponente gibt es nicht (2.1, exakt).
- Parametrisch ist bis epsilon = 0,04 keine neue Instabilitaet zu sehen: einkomponentig an P1 und P3, gemischt an drei
  stillen Stellen der beta_eff-Familie.
- Obere Schranke fuer eine neue Wachstumsrate: 1e-5 (einkomponentig) bzw. 1e-6 (gemischt).
- Die Wirkungen O(epsilon^2) sind Ratenverschiebungen (hoechstens 0,4 % von lambda) und Daempfung vorhandener Anregungen.
  Das ist ein Verlust nur fuer eine schon angeregte Mode, kein selbsttragender Kanal.
- Schwellenamplitude: Innerhalb epsilon <= 0,04 kreuzt keine Rate die Null. Die einzige positive eps^2-Rate einer
  gebundenen Mode (+8,5e-5 eps^2, P3, g = 0,2) liegt um mehr als 1e5 unter lambda.
- Entscheidend fuer die Gesamtformel ist etwas anderes:
  - Der einkomponentige Ball ist bei jedem g != 0 in O(g) instabil (1.1), unabhaengig von der Atmung.
  - Der natuerliche gemischte Ball traegt die stillen Stellen exakt (verschoben nach beta_eff). Symmetrisch verliert er
    nach demselben Mechanismus wie N = 1 (eps^4 bei Codex, dort fuer beta = 0,5 gemessen).

## 3. Frage 3: stille Stellen des psi_2-Zwei-Kanal-Problems

### 3.1 Goldene Regel fuer den Gegenlaeufer (Hand, dann gegen den Pol geprueft)

- Bei g = 0 ist x0 = (0, f) Eigenvektor bei nu0 = 2 omega. Die Kopplung sp = -g J S speist Kanal a bei
  (omega + nu0)^2 = 9 omega^2, k = sqrt(9 omega^2 - 1).
- Zweite Ordnung: delta nu = -g^2 J^2 <f^3, G_a f^3> / (2 omega N2), mit G_a = (L_0 - 9 omega^2 - i0)^{-1} auslaufend und
  N2 = int f^2 r^2 dr. Daraus [Hand]:

      -Im nu = g^2 J^2 I^2 / (2 omega k A^2 N2),   I = int Phi f^3 r dr,

  Phi'' = (U'(f^2) - 9 omega^2) Phi, Phi(0) = 0, Phi'(0) = 1, Phi -> A sin(k r + delta).
- Pruefung an P1 [num+K]:
  - Pol: -Im nu/g^2 = 8,323e-5 bei g = 0,2 (8,454e-5 bei g = 0,5)
  - goldene Regel, linear zwischen den Rasterpunkten 0,79 und 0,80 interpoliert: 8,31e-5
  - Das sind 0,2 % bei g = 0,2. Die 1,8 % bei 0,5 sind die erwartete Korrektur O(g^2).
- An P2 und P3 stimmt es auf 4 % (Interpolation ueber steilere Stellen). An P4 und P5 liegt eine Nullstelle zwischen den
  Rasterpunkten; dort taugt die Interpolation nicht.

### 3.2 Nullstellen in fuehrender Ordnung: Startpunkte von Kurven stiller Stellen (g -> 0)

- I(omega) wechselt im Raster 0,55 bis 0,98 (Schritt 0,01, Profil hp = 0,02) **achtmal das Vorzeichen**, linear
  interpoliert bei:

  | omega^2 | 1/(omega^2 - 1/2) | Schritt | Aufloesung |
  |---|---|---|---|
  | 0,86575 | 2,734 | - | gut |
  | 0,71079 | 4,744 | 2,01 | gut |
  | 0,64568 | 6,864 | 2,12 | gut |
  | 0,61061 | 9,041 | 2,18 | gut |
  | 0,58852 | 11,30 | 2,26 | knapp |
  | 0,57524 | 13,29 | 1,99 | Raster an der Grenze |
  | 0,56556 | 15,25 | 1,96 | Raster an der Grenze |
  | 0,55116 | 19,55 | 4,29 (wohl eine Stelle uebersprungen) | Raster zu grob |

  - Oberhalb 0,87 kein Wechsel mehr; I/A faellt dort gegen 0 (S0 -> 0).
  - Beleg [num]: ein Gitter, ein Verfahren. Bei den letzten vier ist der Rasterabstand so gross wie der Nullstellenabstand.
- Das beantwortet Frage 3 in fuehrender Ordnung mit **ja**:
  - Die Breite des Gegenlaeufer-Pols hat Nullstellen an diskreten omega^2.
  - [H] Von dort gehen bei endlichem g Kurven stiller Stellen in die (omega^2, g)-Ebene aus (Kodimension-Argument wie
    THEORIE 3.4: reelles Problem mit einem offenen Kanal). Gerechnet sind zwei Punkte solcher Kurven (3.3, 3.4).
- Auffaellig [H]:
  - Die Schritte 2,01 / 2,12 / 2,18 / 2,26 in 1/(omega^2 - 1/2) gleichen der Atmungs-Leiter von psi_1
    (2,04 / 2,21 / 2,25 / 2,27, RUNDE-07.md).
  - Jede psi_2-Stelle liegt dort 0,6 bis 0,8 unter der naechsten psi_1-Stelle.
  - Das passt zum selben Duennwand-Formfaktor.

### 3.3 Bei endlichem g

**Gegenlaeufer, g-Scan bei omega^2 = 0,551158** (Nachtrag C, Vorab VC1):
- Anlass: Im Lauf ueberlapp hatte der Pol hier bei g = 0,5 die Breite 1,5e-10, die goldene Regel erwartet 2,4e-5; bei
  g = 0,2 war er 2,84e-6 breit (goldene Regel 3,86e-6).

| g | 0,30 | 0,35 | 0,40 | 0,44 | 0,47 | 0,49 | 0,50 | 0,51 | 0,53 | 0,56 | 0,60 | 0,65 | 0,70 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| -Im nu (h = 0,02) | 3,84e-6 | 3,36e-6 | 2,19e-6 | 1,02e-6 | 2,97e-7 | 3,09e-8 | **1,47e-10** | 5,62e-8 | 4,88e-7 | 2,18e-6 | 7,10e-6 | 1,90e-5 | 3,90e-5 |
| -Im nu (h = 0,01) | 3,84e-6 | 3,36e-6 | 2,19e-6 | 1,03e-6 | 2,98e-7 | 3,13e-8 | **5,9e-10** | 5,66e-8 | 4,89e-7 | 2,18e-6 | 7,10e-6 | 1,90e-5 | 3,90e-5 |

- Scharfes, quadratisches Minimum: sqrt(-Im nu) faellt linear auf beiden Seiten.
- Aus 0,49 und 0,51 folgt in beiden Stufen g* ~ 0,4985 (von Hand, lineare Naeherung). Daraus erwartet bei g = 0,50:
  9e-10, gemessen 5,9e-10.
- Re nu laeuft glatt durch (1,51432 / 1,51543 / 1,51655).
- Beide Stufen stimmen ausser am Minimum auf 1e-9 ueberein [num+K].
- **VC1 getroffen:** Minimum < 1e-9 bei g* = 0,50 +- 0,03; bei 0,3 und 0,7 ueber 1e-7.
- Das ist eine **stille Stelle des psi_2-Problems bei endlichem g**, (omega^2, g) ~ (0,5512; 0,4985), also ein Punkt einer
  Kurve in der (omega^2, g)-Ebene.
- Beleg: Pol-Verfolgung auf einem g-Raster, kein Umlauftest. "Exakt null" ist damit nicht gezeigt, nur ein Minimum unter
  6e-10 auf dem Raster.

**P5:** Die Gegenlaeufer-Breite faellt von 6,53e-5 (g = 0,5) auf 2,54e-5 (g = 1,0). [H] Eine Kurve stiller Stellen laeuft
dort zwischen g = 0,5 und 1,0 in der Naehe vorbei. Ihr Startpunkt bei g -> 0 ist vermutlich die Nullstelle 0,5885.

**Zustand omega + sqrt(E_1) an P4** (Nachtrag B, Vorab VB1), g-Scan 0,05 bis 0,45 in Stufe h = 0,01:
- Die Stufe h = 0,02 ist bis g = 0,075 vom Gitterfehler ~3e-9 ueberdeckt.
- -Im nu = 1,65e-9 / 8,99e-9 / 7,86e-8 / 4,03e-7 / 1,48e-6 / 2,56e-6 bei g = 0,05 / 0,1 / 0,2 / 0,3 / 0,4 / 0,45
- **monoton, keine Nullstelle** [num+K: zwei Stufen]
- -Im nu/g^2 steigt von 6,6e-7 auf 1,3e-5. Die fuehrende Kopplung dieses Zustands ist also klein, aber nicht null.
- Die Nullstelle bei g* = 0,31 aus VB1 ist widerlegt. Der Fall ohne Nullstelle hatte Breite(0,3) ~ 3,7e-7 vorhergesagt,
  gemessen 4,03e-7.

### 3.4 Breitentest nahe den gut aufgeloesten Nullstellen bei g = 0,2 (zweiter Teil von V6) [num]

Schiessen h = 0,02, Pol 2 omega bei g = 0,2. Die Untergrenze durch den Gitterfehler liegt bei etwa +-5e-9 in Im nu
(bei g = 0 zeigt diese Stufe Im ~ +1e-9 statt 0).

| omega^2 | 0,70073 | 0,705 | 0,708 | 0,710 | 0,71073 | 0,711 | 0,712 | 0,715 | 0,72073 |
|---|---|---|---|---|---|---|---|---|---|
| -Im nu (Pol) | 1,39e-6 | 4,82e-7 | 1,29e-7 | 1,84e-8 | 1,8e-9 | -1,3e-9 (Boden) | 1,5e-9 | 1,35e-7 | 8,16e-7 |
| goldene Regel | 1,24e-6 | 3,92e-7 | 8,48e-8 | 5,4e-9 | 1,8e-11 | 1,1e-9 | 1,9e-8 | 1,96e-7 | 9,49e-7 |

- **An der Stelle 0,7107 getroffen:** Die Breite faellt gegen die Nachbarn bei +-0,01 um mehr als das 500-fache, bis auf
  die Untergrenze. Das Minimum des Pols liegt zwischen 0,711 und 0,712, das der goldenen Regel bei 0,7107.
  - Bei g = 0,2 ist die stille Stelle also um etwa +0,001 in omega^2 verschoben.
  - Das ist ein zweiter Punkt einer Kurve, nahe ihrem Startpunkt.
- **An der Stelle 0,8654 nicht aufloesbar:** Die Breiten dort (goldene Regel 1e-8 bis 1e-13, Pol 2,6e-8 bis 8e-9) liegen
  schon an den Nachbarpunkten nahe der Untergrenze. Dafuer braucht es die Stufe h = 0,01 oder feiner.

## 4. Kontrollen

| Kontrolle | Soll | Ausgang | Beleg |
|---|---|---|---|
| N = 1-Grenze, Pol bei omega^2 = 0,7 (psi_1-Koeffizienten, derselbe Code) | 1,7018102 - 1,468e-3 i (R6 pol07, h = 0,02: 1,7018102865) | 1,7018102865 - 1,4680e-3 i (h = 0,02), 1,7018102230 - 1,4680e-3 i (h = 0,01) | getroffen, bis auf die letzte Stelle |
| N = 1-BIC an P1 (0,797677) | \|Im rho\| < 1e-7 nahe 1,744618 | 1,7446176362 + 1,5e-10 i (h = 0,01); 1,7446177150 + 4,8e-9 i (h = 0,02) | getroffen |
| g = 0: doppelte Nullmode | D(0) = 0, D ~ nu^2 | \|D(0)\| 3e-13 bis 2e-12, \|D(2e-3)\|/\|D(1e-3)\| = 4,000 an allen fuenf Stellen | getroffen |
| g = 0: Gegenlaeufer eingebettet | nu = 2 omega, Im = 0 | Abstand <= 1e-8, \|Im\| <= 1,5e-10 (fuenf Stellen) | getroffen |
| g = 0: omega + sqrt(E_1) eingebettet (P4, P5) | Im = 0 | \|Im\| 1,1e-10 bzw. 8,4e-11 | getroffen |
| g <-> -g | gleiches Spektrum | bitgleich (instabil und 2 omega, alle Stellen) | getroffen |
| lambda: Schiessen gegen FD-Kasten | gleich | relativ <= 1e-7 (Richardson aus Delta 0,1 und 0,05) | getroffen |
| Stufen h = 0,02 gegen 0,01 | klein | lambda: <= 1e-9; Resonanzen: Re <= 8e-8, Im <= 4e-9 | getroffen |
| Negativkontrolle ohne Ball | \|D_frei\| gross an allen Polen | Minimum 0,023 (P5) bis 0,35 (P2), gegen \|D\| ~ 1e-15 an den Polen | getroffen |
| Profil: E_0(L_0) = omega^2 | gleich | FD (Delta 0,1): 0,797594 / 0,685081 / 0,631419 / 0,601400 / 0,582400 | FD-Fehler O(Delta^2) |
| Floquet eps = 0 gegen Eigenwertproblem | gleich | lambda auf 1e-9 (P1, P3, alle g); 2 omega-Rate -3,40e-6 gegen Pol -3,33e-6 | getroffen |
| Floquet eps <-> -eps | gleich | bitgleich (alle Laeufe) | getroffen |
| gemischter Ball: L_eff hat Nullmode h | 0 | -1e-4 bis -3e-5 (FD-Fehler) | getroffen |
| gemischter Ball: Pumpe an bekannter stiller Stelle | rho_FD nahe rho* | 1,601872 gegen 1,602162 (M2); 1,583414 gegen 1,583776 (M3); Lokalisierung >= 0,9995 | getroffen (FD-Fehler 2e-4) |

## 5. Vorab gegen Ausgang

| Nr. | Vorab (PLAN.md) | Ausgang | Urteil |
|---|---|---|---|
| V1 | je g != 0 ein rein imaginaeres instabiles Paar, solange n(L_u) = 1 | ueberall k_r = n(L_u) >= 1, \|Re\|/Im < 1e-16; wo n(L_u) = 1, genau ein Paar | getroffen |
| V1a | lambda/lambda_2 in [0,95; 1,05] / [0,85; 1,15] / [0,7; 1,3] bei g = 0,2 / 0,5 / 1,0 | g = 0,2: 1,021 / 1,030 / 1,041 / 1,053 / 1,066 (P1 bis P5); 0,5: 1,115 / 1,148 / 1,169 / 1,173 / 1,165; 1,0: 1,309 / 1,296 / 1,256 / 1,217 / 1,186 | teilweise: P4, P5 bei 0,2; P3 bis P5 bei 0,5; P1 bei 1,0 knapp ausserhalb. Die Zwei-Moden-Formel unterschaetzt systematisch |
| V1b | an P1 lambda ~ 0,08 / 0,2 / 0,4, je +-30 % (Annahme kappa ~ 0,73) | 0,046 / 0,126 / 0,294; kappa ist 0,405 | verfehlt (die kappa-Annahme war falsch; so war es im Vorab als Deutung festgelegt) |
| V1c | g und -g gleich (1e-10) | bitgleich | getroffen |
| V2 | n(L_u) = 1 fuer g <= 0,5 ueberall; bei 1,0 an P4/P5 moeglich 2 | n(L_u) = 2 schon bei g = 0,5 an P4 und P5; bei 1,0: 1 / 1 / 2 / 2 / 3 | verfehlt fuer g = 0,5 (P4, P5) |
| V3 | g = 0: D(0) = 0 doppelt, 2 omega mit \|Im\| < 1e-9, Abstand < 1e-6 | Abstand <= 1e-8, \|Im\| <= 1,5e-10 | getroffen |
| V3a | Im nu(2 omega) < 0, Verhaeltnis 0,5/0,2 in [5; 7,5] | alle abklingend; 6,35 / 6,77 / 6,90 / 6,72 / 6,23 | getroffen |
| V4 | gebundene Zustaende: P1 keiner; P3 bis P5 mindestens einer [H] | P1 keiner; P3 bei g = 0,2 und 0,5; P4 bei 0, 0,2, 1,0; P5 bei 0, 0,2, 0,5; P2 nur bei 1,0 | getroffen (die Begruendung ueber E_1 von L_0 trifft nur an P4 und P5; an P3 entstehen sie erst durch g) |
| V5 | Floquet g = 0: keine Rate > 1e-4 bis eps = 0,04 | <= 1,9e-8 | getroffen |
| V5a | g != 0: Aenderung von lambda < 5 % bei eps = 0,02 | <= 0,1 % | getroffen |
| V5b [H] | keine weitere instabile Floquet-Mode bei g = 0,2, eps <= 0,04 | keine, auch nicht bei 0,5 und 1,0 | getroffen |
| V6 [H] | I(omega) mindestens zwei Vorzeichenwechsel in (0,52; 0,98); dort Breite bei g = 0,2 mehr als 100-fach tiefer | acht Wechsel (vier gut aufgeloest); bei 0,7107 Einbruch um mehr als 500 bis zur Gitter-Untergrenze; bei 0,8654 nicht aufloesbar (Breiten nahe der Untergrenze) | getroffen, wo pruefbar |
| VG1 | antisymmetrisch keine Instabilitaet; nu_0/nu_0,2 in [0,8; 1,2] | keine Instabilitaet; 0,883 / 0,892 / 0,763 | teilweise (M3 ausserhalb) |
| VG2 | eps = 0: Rate <= 1e-6 | <= 0 bis -1,1e-7 | getroffen |
| VG3 [H] | Pseudo-Goldstone-Mode waechst mit der Pumpe (Rate > 1e-6 bei eps = 0,04) | sie wird **gedaempft** (-3,2e-7 / -2,2e-6 / -5,4e-5 bei eps = 0,04) | widerlegt |
| VG4 | eps und -eps gleich | bitgleich | getroffen |
| VB1 [H] | Nullstelle der omega + sqrt(E_1)-Breite bei g* = 0,31 +- 0,05 (P4) | monoton, keine Nullstelle; der Gegenfall Breite(0,3) ~ 3,7e-7 trifft (4,03e-7) | widerlegt |
| VC1 [H] | 2 omega-Breite bei omega^2 = 0,551158: Minimum < 1e-9 bei g* = 0,50 +- 0,03 | Minimum 5,9e-10 (h = 0,01) bzw. 1,5e-10 (h = 0,02) bei g = 0,50, g* ~ 0,4985, quadratisch | getroffen |

- Bilanz: 12 getroffen (V1, V1c, V3, V3a, V4, V5, V5a, V5b, V6 wo pruefbar, VG2, VG4, VC1), 2 teilweise (V1a, VG1),
  2 verfehlt (V1b, V2), 2 widerlegt (VG3, VB1).

## 6. Rechenzeiten (gemessen; Python-Zeit laut Bericht, Unit-Laufzeit laut systemd)

| Lauf | Ort | Python | Unit | Inhalt |
|---|---|---|---|---|
| rauch1 (gfbic.py, Fassung c719b4e0 ohne Thread-Block) | Laptop, CPU, 1 Thread, nice 19 | 34,1 s | - | 06:22:06 bis 06:22:42 |
| gem-rauch1 | Laptop, dito | 8,0 s | - | 06:28:09 bis 06:28:19 |
| gscan-rauch1 | Laptop, dito | 8,2 s | - | 06:32:42 bis 06:32:52 |
| fq-P1 | .69 p4000a | 160,9 s | 2:55 | Floquet P1, 4 g x 5 eps |
| fq-P3 | .69 p4000a | 150,8 s | 2:34 | Floquet P3 |
| sp-P1 / P2 / P3 / P4 / P5 | .69 cpu, cpu4, cpu2, cpu4, cpu2 | 248,6 / 261,6 / 260,1 / 259,5 / 262,7 s | 4:12 / 4:25 / 4:23 / 4:23 / 4:32 | Spektrum je Stelle |
| kontrolle1 | .69 cpu4 | 113,2 s | 1:56 | N = 1-Grenze |
| ueberlapp | .69 cpu | 547,0 s | 9:17 | I(omega) 0,55 bis 0,98; Polpruefung nach zwei Punkten durch das Zeitbudget abgebrochen |
| gemischt | .69 p4000a | 222,4 s | 4:42 | M1 bis M3 |
| gem-R60 / gem-d0075 | .69 p4000a | 216,6 / 118,5 s | 3:46 / 2:01 | Konvergenz gemischter Ball |
| gscan-P4 | .69 cpu4 | 149,7 s | 2:36 | Nachtrag B |
| fq-P1-R60 / fq-P1-d0075 | .69 p4000a | 135,0 / 115,6 s | 2:22 / 1:59 | Konvergenz einkomponentig |
| gscan-2w0551 | .69 cpu2 | 166,0 s | 2:52 | Nachtrag C |
| ueberlapp-071 / ueberlapp-087 | .69 cpu4 / cpu | 300,4 / 349,1 s | 5:04 / 5:53 | V6, zweiter Teil |
| sp-P1-kleing (g = 0,02 / 0,05 / 0,1) | .69 cpu | - | - | in der Warteschlange um 04:44:04 UTC per PID abgebrochen (Lanes belegt), nicht gerechnet |

- Summe Python auf der .69: 4038 s = 67,3 min in 18 Laeufen (je hoechstens 9:17 min Unit-Zeit). Letzter Lauf zu Ende
  04:54:16 UTC.
- Dazu 50 s Rauchtests lokal.
- Der Kostenplan (PLAN 5: < 40 min) ist ueberschritten, weil die Nachtraege A bis C und die Konvergenzlaeufe dazukamen.

## 7. Dateien

- coordination/runden-v3/RUNDE-08/gf-bic/:
  - PLAN.md: Herleitung, Vorab, Nachtraege A bis C
    - eingefrorene Kopien PLAN.md.eingefroren-20260930-0615, -0627, -0633, -0640
  - ERGEBNIS.md (diese Datei)
  - gfbic.py (sha256 cb62cdfd0a62c3c1e748b4e1b6b036532bc1823a2e9f6f84a556aaf78ccb0bd5)
  - gfbic_gem.py (4d5032c0b64abcf95fd3fba23e50efd97627c00de088b0b2ede0d5f92418a6a6)
  - gfbic_q3.py (e394f0c58f0c96512b0c73a6c6fe0c2f09bfb41ba05e369429e743158729e782)
  - resonanz3d.py (RUNDE-06, 99c54b9ccdb517c1a033669cd664586e642f59fc58f82fd6df8f0d83b7b5bcb0): unveraendert importiert,
    auf der .69 als Kopie im Laufordner
  - lauf-lokal/: Rauchtests
  - lauf-69/: Kopien aller Ausgaben (aus-*/ mit *_bericht.txt und *.json) und LAUF-*.log
- .69: /home/fmh/fmhc-physics-remote/runde8-gfbic/
- Fremde Dateien (bic2.py, resonanz3d.py, KANDIDAT.md, THEORIE, Codex-Ordner) nur gelesen.

## Einfach gesagt

Wir haben geprueft, was eine zweite Feldsorte mit einem Q-Ball macht, der nur aus der ersten Sorte besteht. So ein Ball
ist nicht stabil, sobald die beiden Sorten ueber den Paarterm gekoppelt sind: Zwei Teilchen der ersten Sorte koennen ohne
Energieaufwand in zwei der zweiten umwandeln, und der Ball kippt innerhalb weniger Schwingungen in eine Mischung. Diese
Mischung verhaelt sich im Gleichtakt genau wie ein einfacher Q-Ball mit leicht veraendertem Potential. Deshalb hat auch
sie die stillen Atmungsstellen, nur an etwas verschobenen Orten. Einen neuen Energieverlust der Atmung ueber die zweite
Sorte haben wir nicht gefunden: Die Atmung schaukelt die zweite Sorte nicht auf, sie bremst deren Schwingung sogar leicht.
Dafuer hat die zweite Sorte eigene stille Stellen, die wie eine zweite Leiter neben der ersten liegen.

---

## Nachtrag Runde 9: Karte GF-BIC-2 (geschrieben ab 2026-09-30 07:26:12 CEST, date)

- Auftrag: RUNDE-09.md (Leitung). Vorab: PLAN.md, Nachtrag D (07:07:08, Kopie -0708) und E (07:24:37, Kopie -0725),
  jeweils vor den zugehoerigen Laeufen.
- Code:
  - gfbic_umlauf.py (Fassung 1 sha256 e5f68ae3..., Fassung 2 mit Keim-Optionen 322772c0...)
  - bic2.py Version 3 (ee1ef6d2...) unveraendert importiert bzw. aufgerufen: direkt_m, newton_m, newton_direkt, eigen,
    lin_fit_nullstelle, umlauf_rechteck
- Neu sind nur die Koeffizienten je Profil (lin_multi_k) und ein natives Profil des gemischten Balls (eigenes Schiessen,
  nicht aus beta_eff skaliert).
- Belegstufe "Umlauf" heisst wie in Runde 7: Umlaufzahl +-1 auf Rechtecken um den Fit-Mittelpunkt, im radialen linearen
  Modell mit abgeschnittenem Rand. Das ist numerische Evidenz, kein Beweis.

### R9.1 Umlauftest der zweiten Leiter (Gegenlaeufer, h = 0,02) [num+K: zwei Rechtecke, Aufloesungspruefung]

| Stelle | g | omega*^2 (Fit 1 / Fit dx 5e-4 / Fit dx 1e-4) | nu* (Fit dx 1e-4) | Umlauf dx 5e-4 / 1e-4 | groesster Sprung (rad) | min \|W\| | det J |
|---|---|---|---|---|---|---|---|
| Z1 | 0,2 | 0,711372026 / 0,711372079 / 0,711372264 | 1,6888290 | **-1 / -1** | 0,294 / 0,290 | 8,7e-6 / 1,7e-6 | +2,43e-2 |
| Z2 | 0,2 | 0,645861314 / 0,645861021 / 0,645861922 | 1,6103661 | **+1 / +1** | 0,297 / 0,298 | 7,4e-6 / 1,5e-6 | -1,22e-2 |
| Z3 | 0,4985 | 0,551132890 / 0,551138531 / 0,551155815 | 1,5152569 | **+1 / +1** | 0,297 / 0,292 | 4,2e-7 / 6,9e-8 | -1,43e-5 |

- Jedes Rechteck liegt um den Fit-Mittelpunkt aus Stufe 1, auf fuenf neuen Profilen bei x* + dx (-1 ... 1).
- Der zweite Fit auf diesen Profilen lag in allen sechs Faellen innerhalb von 0,8 dx; ein Neulegen war nicht noetig.
- Die Aufloesungspruefung besteht ueberall (Sprung < 0,4 rad nach adaptiver Verfeinerung der nu-Seiten, 134 bis 154
  Punkte je Rechteck).
- Z1 und Z2 sind Nachbarn auf der Leiter und haben entgegengesetzte Umlaufzahlen, wie bei der Atmungs-Leiter von psi_1.
- Bei Z3 sind W und det J klein (die Stelle liegt tief im Duennwand-Bereich, R_halb ~ 12). Der Fitrest (4,5e-8) ist dort
  so gross wie min \|W\| auf dem kleinen Rechteck. Die Umlaufzahl beruht aber auf den gerechneten W-Werten des Pfades, nicht
  auf dem Fit, und der Fit-Mittelpunkt liegt 0,23 dx neben der Rechteckmitte.
- Pole an den Gitterpunkten (Newton, zur Einordnung):
  - Z1 bei 0,7113: Gamma = 5,8e-11
  - Z2 bei 0,6457: 1,5e-9
  - Z3 bei 0,551158: 4,0e-11
- Einordnung: Die Nullstellen der goldenen Regel (R8, 3.2) lagen bei 0,71073 und 0,64568. Bei g = 0,2 sind die Stellen um
  +6,4e-4 bzw. +1,8e-4 verschoben, also Kurven, die bei g -> 0 in diese Punkte laufen [H, siehe R9.3].

### R9.2 Probe der Abbildung auf beta_eff (g = 0,2, n = 1) [num+K: zwei Codes, zwei Rechtecke]

| Rechnung | Code, Profil | omega*^2 (Fit) | rho* | Umlauf dx 5e-4 / 1e-4 (Sprung rad) |
|---|---|---|---|---|
| Ein-Feld, beta_eff = 0,4535147392 | bic2.py exakt (fremd), Profil aus bic2 | 0,759081556 (Fit 1); 0,759081395 (neu gelegt, dx 1e-4) | 1,7120739833 / 1,7120741014 | -1 / -1 (0,268 / 0,262) |
| gemischter Ball, symmetrischer Sektor | gfbic_umlauf.py, natives Schiessen fuer h(r), Koeffizienten aus der Zwei-Komponenten-Gleichung | 0,759081249 (Fit 1); 0,759082145 (dx 5e-4); 0,759081384 (dx 1e-4) | 1,7120741066 (dx 1e-4) | -1 / -1 (0,260 / 0,260) |

- Die Pole an den gemeinsamen Gitterpunkten stimmen auf zehn Stellen ueberein, zum Beispiel bei 0,75819 in beiden
  Rechnungen 1,7116471594 - 1,3827e-6 i.
- Differenz der feinsten Fits: Delta omega*^2 = 1,1e-8, Delta rho* = 5,2e-9.
- Das native Profil trifft das skalierte beta_eff-Profil: S0 stimmt auf 4e-14 (Rauchtest, hp = 0,04).
- Aussage [num+K]: Die n = 1-Atmungsnullstelle des gemischten Balls bei g = 0,2 liegt dort, wo das Ein-Feld-Modell mit
  beta_eff sie hat: omega*^2 = 0,759081, rho* = 1,712074.
  - Gegenueber dem einkomponentigen Ball (0,797677) ist sie um -0,0386 verschoben.
  - Das bestaetigt numerisch die Reduktion (1.4) samt ihren g-Faktoren, an einer Stelle.
- Zweite Stufe h = 0,01 (Nachtrag E):
  - nativ, Rechteck dx 1e-4 um den Fit-Mittelpunkt: omega*^2 = 0,759081396, rho* = 1,7120741107, Umlauf -1 (Sprung
    0,269 rad)
  - bic2 bei beta_eff:
    - Der Pol bei 0,759081 hat Gamma = 2,3e-13.
    - Die Vorzeichenfunktion s(x) wechselt bei 0,7590814, der Phasentest ergibt d_min bei 0,75908137.
    - Der lineare W-Fit ueber +-5e-4 liefert 0,759082099. Er ist groeber, weil die Profile weiter auseinanderliegen.
    - Das Rechteck dx 1e-4 fiel aus ("zu wenige Profile"): Mein Profilraster (+-2e-4, +-5e-4) hatte nur ein Profil
      innerhalb +-1e-4, und bic2 legt nicht neu, wenn der Fit-Mittelpunkt schon mittig liegt. Das ist ein Fehler meiner
      Aufrufparameter, nicht von bic2.
- **Zusammen:** omega*^2 = 0,7590814 +- 3e-8 und rho* = 1,7120741 +- 4e-8, aus zwei Codes und zwei Stufen [num+K].

### R9.3 Zweite Stufe und ein zweiter Punkt der Kurve (Nachtrag E)

| Lauf | omega*^2 (Fit dx 1e-4) | nu* | Umlauf (Sprung rad) | Vergleich |
|---|---|---|---|---|
| Z1, g = 0,2, h = 0,01 | 0,711372274 | 1,6888290132 | -1 (0,290) | h = 0,02: 0,711372264 / 1,6888290010, Differenz 1e-8 |
| Z2, g = 0,2, h = 0,01 | 0,645861928 | 1,6103661402 | +1 (0,300) | h = 0,02: 0,645861922 / 1,6103661332, Differenz 7e-9 |
| Z1, g = 0,1, h = 0,02 | 0,710861469 | 1,6867493317 | -1 / -1 auf beiden Rechtecken (0,290 / 0,299) | Vorab 0,71089 +- 0,0002 |

- Die Stufen h = 0,02 und 0,01 stimmen fuer Z1 und Z2 auf 1e-8 ueberein, bei gleicher Umlaufzahl [num+K].
- **Kurve durch Z1** [num]:
  - omega*^2 = 0,7108615 bei g = 0,1 und 0,7113723 bei g = 0,2
  - Mit omega*^2 = omega0^2 + c g^2 folgt c = 0,01703 und omega0^2 = 0,710691 fuer g -> 0.
  - Die Nullstelle der goldenen Regel lag bei 0,71073, linear interpoliert auf dem Raster 0,710 / 0,715, also auf etwa 5e-5
    genau. Die Kurve laeuft also in die Nullstelle fuehrender Ordnung, im Rahmen der Rastergenauigkeit.
  - Die Umlaufzahl bleibt entlang der Kurve -1.

### R9.4 Vorab gegen Ausgang (Nachtraege D und E)

| Nr. | Vorab | Ausgang | Urteil |
|---|---|---|---|
| VD1 | Umlauf +-1 auf beiden Rechtecken, aufgeloest, an Z1, Z2, Z3 | Z1 -1/-1, Z2 +1/+1, Z3 +1/+1; Spruenge 0,290 bis 0,298 rad | getroffen |
| VD2 [H] | Z1 und Z2 mit entgegengesetzter Umlaufzahl | -1 gegen +1 | getroffen |
| VD3 | Fit-Mittelpunkte in den Fenstern | Z1 0,711372 / 1,688829; Z2 0,645862 / 1,610366; Z3 0,551156 / 1,515257 | getroffen |
| VD4 | gemischt nativ und Ein-Feld bei beta_eff auf 1e-6 gleich, bei 0,7587 +- 0,001, rho* 1,7117 +- 0,002 | Differenz 1,1e-8 (omega^2) und 5e-9 (rho); 0,759081 und 1,712074 | getroffen |
| VE1 | h = 0,01 aendert Umlauf und Fit-Mittelpunkte von Z1, Z2 nicht (2e-6 bzw. 1e-6) | gleiche Umlaufzahl, Verschiebung 1e-8 | getroffen |
| VE2 [H] | Z1 bei g = 0,1: 0,71089 +- 0,0002, nu* 1,68678 +- 0,0005, Umlauf -1 | 0,710861, 1,686749, -1 | getroffen |

- Bilanz Runde 9: 6 von 6 getroffen.
- Einschraenkung: Die Vorab-Fenster von VD3 und VE2 stammen aus den Pol-Scans von Runde 8 und waren deshalb eng
  vorgegeben. Die eigentliche Pruefung sind die Umlaufzahlen (VD1, VD2) und die Zwei-Code-Uebereinstimmung (VD4).

### R9.5 Rechenzeiten (gemessen) und Dateien

| Lauf | Spur | Python | Unit |
|---|---|---|---|
| Z1 / Z2 / Z3 (h = 0,02) | p4000a / cpu / p4000b | 253,8 / 253,4 / 318,5 s | 4:17 / 4:16 / 5:22 |
| BG / bic2-beta_eff (h = 0,02) | p4000b / p4000a | 78,5 / 264,9 s | 1:21 / 4:28 |
| Z1 / Z2 (h = 0,01) | p4000a / p4000b | 278,8 / 281,2 s | 4:42 / 4:44 |
| Z1 g = 0,1 | p4000a | 259,4 s | 4:22 |
| BG / bic2-beta_eff (h = 0,01) | p4000b / p4000a | 107,3 / 171,0 s | 1:50 / 2:54 |

- Summe 2267 s = 37,8 min Python in 10 Laeufen, je unter 6 min Unit-Zeit. Dazu Rauchtests lokal 30,9 s und 7,9 s.
- In der Warteschlange abgebrochen (per PID, nicht gerechnet):
  - Z1 auf cpu und BG auf cpu2, weil beide Spuren je drei fremde Laeufe vor sich hatten. Beide wurden auf p4000a/b neu
    eingereiht.
  - K1 (Pipeline-Kontrolle gegen bic2), ueberfluessig, weil BG gegen bic2 schon Pol fuer Pol gleich war.
- Arbeitszeit Runde 9: 07:05:02 bis 07:38:19 CEST (date); letzter Lauf zu Ende 05:37:29 UTC.
- Dateien:
  - RUNDE-08/gf-bic/gfbic_umlauf.py (Fassung 2, sha256 322772c0809b714f...)
  - PLAN.md mit den Nachtraegen D und E
  - PLAN.md.eingefroren-20260930-0708 und -0725
  - lauf-69-r9/ (aus-*/umlauf_bericht.txt bzw. exakt_bericht.txt, JSON, LAUF-*.log)
  - lauf-lokal/aus-umlauf-rauch1 und -rauch2
  - .69: /home/fmh/fmhc-physics-remote/runde9-gfbic2/

### Einfach gesagt (Runde 9)

Die zweite Leiter aus stillen Stellen, die wir in Runde 8 fuer die zweite Feldsorte gefunden hatten, haelt dem strengeren
Test stand. Um jede der drei geprueften Stellen dreht sich die Rechengroesse W genau einmal herum, einmal links- und
einmal rechtsherum, wie bei echten Nullstellen und wie bei der ersten Leiter. Ausserdem haben wir nachgerechnet, ob der
gemischte Ball aus beiden Feldsorten wirklich wie ein einfacher Q-Ball mit veraendertem Potential atmet. Zwei voellig
getrennt aufgebaute Rechnungen landen auf derselben stillen Stelle, auf acht Stellen hinter dem Komma genau. Die Abbildung
auf das einfachere Modell stimmt also, zumindest an dieser Stelle.

---

## Nachtrag Runde 9: Karte ROT-2, innere Drehung im gemischten Ball (geschrieben ab 2026-09-30 08:20:21 CEST, date)

- Auftrag: RUNDE-09.md (ROT-1 bis ROT-3, Freigabe Finn 07:47). Beginn 07:47:58 (date).
- Vorab: PLAN.md Nachtrag F. Die Abschnitte stehen je vor ihrem Lauf; die Kopien liegen in PLAN.md.eingefroren-*:
  - F.1 bis F.3 um 07:52:14
  - F.4 um 07:56:54
  - F.5 um 07:57:36
  - F.6 um 08:06:01
  - F.7 um 08:08:46
  - F.8 um 08:17:33
  - F.9 um 08:20:00
  - F.10 um 09:57:10 (nach der Pause)
- Code:
  - gfbic_rot.py: volle nichtlineare Zwei-Komponenten-Zeitentwicklung, radial 3D, Leapfrog mit Schwamm; Fassung 1
    63a46c9b..., Fassung 2 c96e516d... mit Start "ungleich"
  - gfbic_anti.py (1e9a23dd...) fuer den Gegentakt
  - gfbic_rot_zeit.py (eefd144d..., Zeitverlauf-Auslese)
  - Profil: nativ geschossen, auf dem FD-Gitter per Newton nachrelaxiert (Rest < 1e-13), also ein diskret stationaerer
    Anfang.
- Ball M1: g = 0,216370, omega^2 = 0,755738 (stille Atmungsstelle von beta_eff = 0,45), omega = 0,869332,
  Massenluecke 1 - omega = 0,130668.
- Messort: Ladung und Fluesse bei R_m = 20, Kasten R = 80 mit Schwamm ab 60. T = 6000 (Tiefpass fuer die langsame Phase
  ueber eine schnelle Periode). Die Ladungsbilanz schliesst in allen Laeufen auf <= 2e-4.

### ROT.0 Ergebnis in Kuerze (Stand 10:02, date)

1. **Kein innerer Rotor, keine Schwelle.**
   - Die relative Phase pendelt (Libration) statt zu laufen: bei allen Kicks bis Omega_0 = 1,3 und bei allen
     Ungleichgewichten bis z0 = 0,99 [num+K].
   - Ursache [Hand]: Ohne Kopplung kostet die Ladungsverteilung nichts. Es bleibt ein reiner Paartunnel-Josephson,
     H = -K (1 - z^2) cos 2 phi, ohne Rotorbahnen.
   - Das Modell trifft phi_max auf 0 bis 7 % und nu auf 0 bis 11 % (bis 33 % an der Separatrix).
   - Nur an der Separatrix (Omega_0 = 1,7) dreht die Phase etwa vier Mal, verliert 4 % Ladung und pendelt dann.
2. **T2 aus ROT-3 scheitert an M1:**
   - Die Kinematik (Schwelle (2/3)(1 - omega)) ist richtig, aber es gibt keinen Rotor unterhalb der Schwelle.
   - Die Verlustrate waechst glatt wie Omega_0^3, ohne Sprung.
   - Eine Ladeenergie, die ein ruhiges Rotorfenster tragen koennte, ist nicht gesehen (\|E_C\| <~ 0,3 K).
3. **Selbststabilisierung, teilweise:**
   - Die Libration strahlt ueber ihre Harmonischen n nu (gerade n im Gleichtakt, ungerade im Gegentakt). Jede
     Harmonische schliesst, wenn n nu unter 1 - omega faellt, und nu sinkt mit der Amplitude.
   - Beim Schliessen von n = 3 faellt der Fluss um den Faktor 7 [num, nicht vorab gebunden].
   - Beim Schliessen von n = 2 faellt er nicht, weil n = 3 den Fluss schon traegt (VF9 widerlegt).
4. **Stille Kanaele:**
   - Der Gegentakt hat eine eigene Leiter stiller Stellen: g = 0,05 bei 0,702252 (Umlauf -1) und 0,635507 (+1)
     [num+K].
   - Ein kleiner Kick genau dort schaltet den direkten Kanal des schnellen Anteils ab (15- bis 23-mal schwaecher).
   - Der Gesamtfluss bleibt, weil Kombinationskanaele offen sind.
5. **Kontrollen:**
   - g = 0: Q_1, Q_2 erhalten, die schnelle Linie genau bei 2 omega, keine freie Rotation
   - zwei Gitter: <= 0,3 % (phi_max), < 1 % (Fluss)
   - Ladungsbilanz <= 2e-4
   - Vorab: 7 getroffen, 4 teilweise, 2 widerlegt (ROT.5)

### ROT.1 Von Hand: reiner Paartunnel-Josephson, keine laufende Phase (PLAN F.1)

- Bei g = 0 kostet die Umverteilung der Ladung zwischen den Komponenten nichts (U(2)). Die ganze Abhaengigkeit von relativer
  Phase phi und Ungleichgewicht z kommt aus dem Paarterm:

      H(z, phi) = -K (1 - z^2) cos 2 phi

- Folgen:
  - Es gibt keine Bahn, auf der phi ueber die Mulden laeuft. Auf der Pseudospin-Kugel (ROT-3, W1.1) waere das die Drehung
    um die mittlere Achse (Tennisschlaeger-Fall).
  - Ein Kick der Phasengeschwindigkeit Omega_0 ergibt z0 = Omega_0/(2 omega) und eine Libration mit
    phi_max = (1/2) arccos(1 - z0^2) < pi/4 und einer Frequenz nu(z0), die mit der Amplitude faellt.
  - Dazu kommt eine schnelle Schwingung von Delta theta: der Gegentakt-Gegenlaeufer bei nu_G ~ sqrt(4 omega^2 + 3 alpha).
  - Eine laufende Phase ist erst an der Separatrix z0 -> 1 (Omega_0 -> 2 omega) moeglich, getragen von Termen O(g^2).

### ROT.2 (a) Rotor gegen Libration, Zeitentwicklung an M1 [num+K: zwei Gitter, g = 0-Kontrolle, Ladungsbilanz]

| Omega_0 | z0 | phi_max gemessen (Modell F.1) | nu gemessen (Modell F.1) | schnelle Linie, Amplitude (Modell Omega_0/2 omega) | E-Fluss bei R_m | laeuft? |
|---|---|---|---|---|---|---|
| 0,05 | 0,029 | 0,0194 (0,0203) | 0,0688 (0,0687) | 1,8117; 0,026 (0,029) | 3,7e-7 | nein |
| 0,1 | 0,058 | 0,0388 (0,041) | 0,0688 (0,0686) | 1,8113; 0,052 (0,058) | 2,2e-6 | nein |
| 0,2 | 0,115 | 0,0775 (0,081) | 0,0684 (0,0683) | 1,8106; 0,103 (0,115) | 1,6e-5 | nein |
| 0,3 | 0,173 | 0,1167 (0,122) | 0,0677 (0,0679) | 1,8099; 0,151 (0,173) | 5,9e-5 | nein |
| 0,45 | 0,259 | 0,1746 (0,184) | 0,0670 (0,0670) | 1,8082; 0,211 (0,259) | 1,9e-4 | nein |
| 0,6 | 0,345 | 0,2350 (0,246) | 0,0656 (0,0655) | 1,8061; 0,271 (0,345) | 4,9e-4 | nein |
| 0,9 | 0,518 | 0,3567 (0,375) | 0,0621 (0,0613) | 1,8029; 0,329 (0,518) | 1,5e-3 | nein |
| 1,3 | 0,748 | 0,5164 (0,557) | 0,0576 (0,0518) | 1,8019; 0,326 (0,748) | 2,6e-3 | nein |
| 1,7 | 0,978 | laeuft anfangs | 0,0538 | 1,8008; 0,363 | 3,2e-3 | **anfangs ja** |

- Die Modellwerte bei 0,1 / 0,3 / 0,6 / 0,9 / 1,3 standen vorab in PLAN F.3. Die Werte bei 0,05 / 0,2 / 0,45 sind nach
  derselben Formel nachgetragen.
- **Keine Schwelle zur Rotation bis Omega_0 = 1,3.** Die langsame Phase bleibt in der Mulde (Spanne <= 1,0 rad je
  500-Zeitfenster). phi_max trifft das reduzierte Modell auf 4 bis 7 %, nu auf 0 bis 11 %.
- **Omega_0 = 1,7 (z0 = 0,978, an der Separatrix): ein kurzlebiger Rotor.**
  - Delta theta laeuft in den ersten ~500 Zeiteinheiten netto -24,7 rad, also etwa vier Umlaeufe.
  - Dabei wandert die Ladung fast ganz von Komponente 1 in Komponente 2 (z von +0,97 auf -0,88 bei t = 253).
  - In dieser Phase strahlt der Ball 4 % seiner Ladung ab (190,4 -> 182,7).
  - Danach ist es eine Libration grosser Amplitude (|z| bis 0,74, Spanne ~1 rad je Fenster). Bis T = 6000 gehen insgesamt
    11 % der Ladung verloren.
  - **Ein Rotor haelt also nur etwa 250 bis 500 Zeiteinheiten** [num].
- Kontrollen:
  - **g = 0** (Lauf C, 0,1 / 0,3 / 0,9):
    - kein langsamer Anteil (phi_max <= 0,014)
    - Q_1 - Q_2 erhalten (Drift 1e-5 relativ bei kleinen Kicks)
    - schnelle Linie genau bei 2 omega = 1,7387, Amplitude 0,0569 gegen 0,0575 vorhergesagt
    - Die Erwartung "freie Rotation bei g = 0" trifft also nicht zu: Ohne Kopplung dreht die relative Phase nicht, der Kick
      verteilt nur die Ladung um und regt den Gegenlaeufer an (PLAN F.1).
  - **Gitter** (Lauf B, Delta 0,05 gegen 0,1, Kicks 0,1 / 0,3 / 0,6 / 0,9): phi_max auf <= 0,3 %, nu gleich (FFT-Raster
    3,5e-4), Fluesse auf < 1 %.
- **M3** zum Vergleich (Lauf D: g = 0,472, omega^2 = 0,566, grosser Ball, nu_0 = 0,218):
  - Auch dort laeuft nichts [num].
  - Das reduzierte Modell trifft dort die Amplituden nicht: phi_max 30 bis 40 % kleiner, nu fast unabhaengig von der
    Amplitude (0,2175 bis 0,2182).
  - Die Ladung in r < 20 steigt bei grossen Kicks (+4,6 % bei Kick 1,0), bei geschlossener Bilanz. Das ist ungeklaert
    (Einfang schwellennaher Wellen oder Randeffekt).
- Abstrahlung (Spektrum von psi_+- = (psi_1 +- psi_2)/sqrt 2 bei R_m, Kick 0,05):
  - psi_-: omega + nu_G = 2,681 (schneller Anteil, direkt)
  - psi_+: omega + nu_G +- nu = 2,749 und 2,612 (Kombination)
  - psi_+: omega + 2 nu = 1,0069 (2. Harmonische der Libration)
  - e^{+iEt}-Ast: \|omega - nu_G - nu\| = 1,011
  - Bei Kick 0,9 zusaetzlich omega + 3 nu = 1,0556 in psi_-.
  - Die Rotor-Kanaele omega +- 2 Omega aus dem Auftrag gibt es nicht, weil es keinen Rotor gibt.
  - Der Energiefluss waechst etwa wie Omega_0^3. Relativ zur Kick-Energie (27,4 Omega_0^2) ist die Lebensdauer ~2e5 bei
    Kick 0,05 und ~4e4 bei 0,3 [num].

### ROT.2b Abgleich mit ROT-3 (PAPIER-ROT3.md W5.2, Test T2) (nach der Pause, ab 09:58:11 CEST, date)

- **Einig:**
  - Einen stationaeren reinen Rotor gibt es nicht (ROT-3 W1.4/W5.2, hier F.1).
  - Die Kinematik stimmt: Ein Rotor mit omega_1,2 = omega +- Omega_r/2 speist psi_2 bei omega + (3/2) Omega_r und
    strahlt in erster Ordnung erst oberhalb Omega_r = (2/3)(1 - omega) = 0,087 / 0,160 / 0,165 an M1 / M2 / M3. Dieselbe
    Grenze steht in meiner Kanal-Buchhaltung vom Anfang dieser Karte.
- **Nicht einig: Gibt es oberhalb der Separatrix Rotoren mit kleiner Drehrate (das "ruhige Fenster" von ROT-3)?**
  - ROT-3 nimmt einen Josephson-Kontakt mit Ladeenergie an: H = E_C z^2/2 - K cos 2 phi.
  - Hier fehlt die Ladeenergie in fuehrender Ordnung (U(2) bei g = 0), und es bleibt H = -K (1 - z^2) cos 2 phi. Dann
    gibt es gar keine Rotorbahnen (F.1).
  - Lauf A entscheidet das numerisch fuer M1: Frequenz und Amplitude der Libration folgen dem reinen Paartunnel-Modell auf
    1 bis 7 % bis Kick 0,9, ohne Ladeenergie.
  - Mit Ladeenergie gilt am Umkehrpunkt cos 2 phi_max = 1 - (1 + E_C/(2K)) z0^2 [Hand].
    - Bei E_C = K waere phi_max bei kleinen Kicks um sqrt(1,5) = 1,22 groesser.
    - Gemessen ist es 2 bis 7 % kleiner (A und E). Das entspricht E_C zwischen etwa -0,3 K und 0, oder kleinen
      Profileffekten. Eine positive Ladeenergie von der Groesse K, die ein ruhiges Rotorfenster tragen koennte, ist nicht
      gesehen [Hand + num, M1]. Laufende Bahnen bleiben damit auf z -> +-1 beschraenkt, passend zum Uebergangsrotor bei
      Omega_0 = 1,7.
- **T2 selbst:**
  - Lauf A ist genau der T2-Aufbau (gemischter Ball, Frequenzversatz omega +- delta ueber die Anfangsgeschwindigkeit,
    Omega_0 = 2 delta).
  - Ergebnis: Unterhalb von Omega_0 = 1,7 entsteht kein Rotor. Die Verlustrate waechst glatt wie Omega_0^3 und springt bei
    0,087 nicht.
  - Der einzige Rotor (Omega_0 = 1,7) dreht mit Omega_r ~ 0,15, also ueber der Schwelle. Er strahlt stark (4 % der Ladung
    in ~500) und faellt nach etwa vier Umlaeufen in Libration.
  - Nach seinen eigenen Kriterien **scheitert T2**: kein Sprung an der Schwelle, und kein Rotor unterhalb der Schwelle, der
    zehn Umlaeufe haelt.
  - Beleg: [num+K] fuer M1 (zwei Gitter, g = 0-Kontrolle); M2 nicht gerechnet, M3 nur als Vergleich (D).
- Zusatzlauf H (Start "ungleich" nahe der Separatrix, z0 bis 0,99): siehe ROT.2c.

### ROT.2c Nahe der Separatrix, ohne schnellen Anteil (Lauf H, Vorab F.10/VF12; geschrieben ab 10:01:25 CEST, date) [num]

| z0 | phi_max gemessen (Modell) | nu gemessen, 1. Haelfte (Modell) | laeuft? | E-Fluss | staerkste Linien bei R_m (2. Haelfte) | Harmonische n mit n nu > 1 - omega |
|---|---|---|---|---|---|---|
| 0,8 | 0,6025 (0,601) | 0,0538 (0,0486, nachgetragen) | nein | 2,2e-4 | psi_- 1,0388 (n = 3), psi_+ 1,0928 (n = 4) | ab 3 |
| 0,9 | 0,7050 (0,690) | 0,0499 (0,0406) | nein | 5,2e-4 | psi_- 1,0294 (n = 3, 1,0e-3), psi_+ 1,0802 (n = 4) | ab 3 |
| 0,95 | 0,7610 (0,737) | 0,0377 (0,0346) | nein | **7,4e-5** | psi_+ 1,0336 (n = 4), psi_- 1,0713 (n = 5); n = 3 fehlt | ab 4 |
| 0,99 | 0,8034 (0,775) | 0,0339 (0,0255) | nein | 1,5e-4 | psi_+ 1,0205 (n = 4), psi_- 1,0556 (n = 5) | ab 4 |

- **Auch nahe der Separatrix laeuft nichts.** Die Spanne der langsamen Phase ist hoechstens 1,60 rad, phi_max liegt
  3 bis 4 % ueber dem Modell (bei z0 = 0,99 knapp ueber pi/4).
- nu faellt zur Separatrix hin wie vorhergesagt: +9 % bei 0,95, +23 % bei 0,9, +33 % bei 0,99. Letzteres liegt knapp
  ausserhalb der Toleranz.
- Die Linien in der 2. Haelfte liegen bei hoeherem nu als in der ersten, weil die Amplitude durch Abstrahlung sinkt.
- **Treppe der Kanaele [num]:** Die n-te Harmonische liegt im symmetrischen (n gerade) bzw. antisymmetrischen (n ungerade)
  Kanal. Sie ist offen, solange n nu > 1 - omega = 0,1307.
  - Zwischen z0 = 0,9 und 0,95 schliesst n = 3. Der Energiefluss faellt dort um den Faktor 7 (5,2e-4 -> 7,4e-5), und die
    Linie n = 3 verschwindet aus dem Spektrum.
  - **Das ist ein Fall der Selbststabilisierung durch die nichtlineare Frequenzverschiebung** (nicht vorab gebunden, als
    Befund markiert).
  - Beim Schliessen von n = 2 (z0 ~ 0,4, VF9) gab es keinen solchen Abfall, weil n = 3 dort schon den Fluss trug.
  - Bei z0 = 0,99 steigt der Fluss wieder (n = 4 knapp an der Kante, Amplitude hoeher).

### ROT.3 (b) Oszillierende Selbststabilisierung und stille Kanaele

**Reine Libration** (Lauf E, Start "ungleich": psi_1 = sqrt(1 + z0) h, psi_2 = sqrt(1 - z0) h, beide mit omega; schneller
Anteil <= 0,01):

| z0 | phi_max (Modell) | nu (Vorab) | E-Fluss | Linie omega + 2 nu in psi_+ | Linie omega + 3 nu in psi_- |
|---|---|---|---|---|---|
| 0,05 | 0,0339 (0,0354) | 0,0688 (0,0687) | 6,5e-9 | 1,0069: 4,6e-6 | - |
| 0,1 | 0,0680 (0,0708) | 0,0688 (0,0685) | 7,4e-8 | 1,0069: 1,9e-5 | - |
| 0,2 | 0,1359 (0,1419) | 0,0681 (0,0677) | 3,2e-6 | 1,0053: 2,1e-4 | 1,0734: 7e-6 |
| 0,3 | 0,2052 (0,2135) | 0,0670 (0,0664) | 3,8e-6 | 1,0037: 2,0e-4 | 1,0708: 2,4e-5 |
| 0,35 | 0,2409 (0,2501) | 0,0663 (0,0655) | 4,4e-6 | 1,0022: 1,4e-4 | 1,0692: 4,1e-5 |
| 0,4 | 0,2781 (0,2898) | 0,0653 (0,0645) | 3,8e-5 | 1,0016: 6,5e-4 (an der Kante) | 1,0671: 6,2e-5 |
| 0,5 | 0,3521 (0,3614) | 0,0632 (0,0619) | 2,1e-5 | weg | 1,0613: 1,4e-4 |
| 0,6 | 0,4306 (0,4382) | 0,0604 (0,0586) | 5,0e-5 | weg | 1,0545: 2,1e-4 |

- Das reduzierte Modell trifft Amplitude und Frequenz der reinen Libration auf 1 bis 7 % [num+K].
- Der Kanal der 2. Harmonischen schliesst tatsaechlich, sobald omega + 2 nu(z0) unter 1 faellt: Bei z0 = 0,4 liegt die
  Linie an der Kante, ab 0,5 ist sie weg [num].
- **Selbststabilisierung im Gesamtfluss: nicht gesehen, VF9 widerlegt.**
  - Der Fluss faellt ab z0 = 0,4 nicht, er steigt.
  - Die 3. Harmonische im Gegentakt (omega + 3 nu, offen bis nu > 0,0436) waechst etwa wie z0^3 und uebernimmt.
  - Bei z0 = 0,4 gibt es eine Spitze (3,8e-5), genau wenn die 2. Harmonische an der Kante liegt; ungeklaert
    (schwellennahes Nahfeld am Messradius?).
- Kinematik [Hand, H]:
  - Harmonische n schliessen, wenn n nu < 1 - omega. Weil nu_0 ~ g, sind bei kleinem g viele Harmonische zu. Dann strahlt
    die Libration erst in hoher Ordnung (Amplitude^(2 n)).
  - Das ist die eigentliche Form der Selbststabilisierung: eine kleine Kopplung macht die innere Schwingung langsam
    gegen die Massenluecke. An M1 (g = 0,216) ist nur die 2. Harmonische knapp offen.
- Schneller Anteil: Sein direkter Kanal omega + nu_G ist still an den stillen Stellen des Gegentakt-Gegenlaeufers (ROT.4).
  Direkter Test: ROT.3a.

**ROT.3a Kick auf einer stillen Gegentakt-Stelle** (g = 0,05, Kick 0,3, Delta 0,1; Linie omega + nu_G in psi_-):

| omega^2 | omega + nu_G | Amplitude der Linie | Anmerkung |
|---|---|---|---|
| 0,690 | 2,5174 | 1,02e-5 | nicht still, 0,012 unter der Stelle |
| 0,702252 | 2,5380 | 5,4e-6 | stille Stelle (Schiessen, Umlauf -1) |
| 0,715 | 2,5595 | 3,2e-6 | nicht still, 0,013 ueber der Stelle |

- **VF10 widerlegt:** Bei Kick 0,3 ist die Linie an der Stelle nicht zehnmal schwaecher. Moegliche Gruende stehen in
  PLAN F.9. Ein Nachlauf mit Kick 0,05 und Delta 0,05 (VF11) steht in ROT.3b.

**ROT.3b Dasselbe mit kleinem Kick** (g = 0,05, Kick 0,05, Delta 0,05, T = 3000; Laeufe G) [num]:

| omega^2 | omega + nu_G | Amplitude der direkten Linie in psi_- | Gesamt-E-Fluss |
|---|---|---|---|
| 0,690 | 2,5188 | 1,07e-6 | 5,6e-7 |
| **0,702252** (still) | 2,5393 | **4,7e-8** | 7,4e-7 |
| 0,715 | 2,5609 | 7,1e-7 | 6,3e-7 |

- **VF11 getroffen:** An der stillen Gegentakt-Stelle ist der direkte Kanal des schnellen Anteils 15- bis 23-mal
  schwaecher als 0,012 daneben.
- Bei Kick 0,3 war das nicht so: Von 0,05 auf 0,3 waechst die Linie an der Stelle wie Kick^2,65 statt linear, ist dort
  also nichtlinear bestimmt. Die beiden Laeufe hatten verschiedene Gitter (Delta 0,05 gegen 0,1); ein Rest-Einfluss des
  Gitters ist nicht getrennt.
- Der Gesamtfluss sinkt nicht mit, er ist an allen drei Punkten gleich gross (5,6e-7 bis 7,4e-7). Er kommt ueberwiegend
  aus den Kombinationslinien im symmetrischen Kanal (psi_+ bei omega + nu_G +- nu, ~6e-6) und aus dem Bereich knapp ueber
  der Kante (~1,4e-6).
- **Also:** Die stille Stelle schaltet genau den einen Kanal ab, auf den sie faellt, nicht die ganze Abstrahlung. Das ist
  die Antwort auf (b) in ihrer schaerfsten Form: Ein Hauptkanal kann auf eine stille Stelle fallen, die Nebenkanaele
  bleiben offen.

### ROT.4 (c) Stille Stellen im Gegentakt [num+K: Umlauf auf zwei Rechtecken]

- Gegentakt (psi_1 - psi_2) des gemischten Balls, Pol des Gegenlaeufers bei nu ~ sqrt(4 omega^2 + 3 alpha).
  Koeffizienten dp = U' + g J S, sp = -g J S/2, natives Profil.
- Scan bei g = 0,05 (Lauf antiscan): Die Breite faellt in beiden Fenstern zum unteren Rand hin unter die Gitter-Untergrenze.
  Die Umlauftests um den Fit-Mittelpunkt ergeben:

| Stelle | omega*^2 (Fit 1 / dx 5e-4 / dx 1e-4) | nu* | Umlauf dx 5e-4 / 1e-4 (Sprung rad) | Abstand zur psi_2-Leiter (g -> 0) |
|---|---|---|---|---|
| AG1 | 0,702249 / 0,702251 / 0,702252 | 1,7012519 | **-1 / -1** (0,285 / 0,296) | -0,0085 gegen 0,71073 |
| AG2 | 0,635481 / 0,635506 / 0,635507 | 1,6267216 | **+1 / +1** (0,295 / 0,281) | -0,0102 gegen 0,64568 |

- **Antwort auf Finns Frage** ("bei einem Ball mit zwei Sorten gibt's Nullstellen, right?"): Ja. Auch der Gegentakt hat
  eine eigene Leiter stiller Stellen, mit abwechselnder Umlaufzahl.
- Sie laeuft bei g -> 0 in die psi_2-Leiter (U(2)-Grenze). Schon bei g = 0,05 ist sie aber um etwa -0,009 bis -0,010 in
  omega^2 verschoben, weil sich die Frequenz des Gegenlaeufers mit alpha ~ g verschiebt [num].
- Pole an den Gitterpunkten: Gamma = 9,9e-11 bei 0,703 und 2,3e-10 bei 0,636.

### ROT.5 Vorab gegen Ausgang (PLAN F)

| Nr. | Vorab | Ausgang | Urteil |
|---|---|---|---|
| VF1 [H] | kein laufender Rotor fuer Omega_0 = 0,05 bis 1,3 | keiner (Spanne <= 1,0 rad); bei 1,7 ein Rotor fuer ~500 Zeiteinheiten, dann Libration | getroffen (1,7 lag ausserhalb, passt zu F.1) |
| VF2 [H] | phi_max +-30 %, nu +-20 % nach F.1 | phi_max -4 bis -7 %; nu -0,1 bis +11 % | getroffen |
| VF3 | schnelle Linie bei ~2 omega = 1,739, Amplitude ~Omega_0/(2 omega) | Linie bei 1,811 (die vor dem Lauf eingetragene Korrektur F.4, nu_G ~ 1,825, trifft auf 0,8 %); Amplitude -9 bis -19 % bis Kick 0,45, darueber Saettigung | Frequenz nach F.3 verfehlt, nach F.4 getroffen; Amplitude getroffen fuer kleine Kicks |
| VF4 | g = 0: Q_1, Q_2 erhalten, kein langsamer Anteil, nur 2 omega | Drift 1e-5, phi_max <= 0,014, Linie 1,7387 | getroffen |
| VF5 [H] | Linien bei 3 omega und omega + 2 nu; omega + 2 nu fehlt ab 0,6 | omega + 2 nu wie erwartet (bis 0,3 da, ab 0,6 weg); die schnelle Linie liegt bei omega + nu_G = 2,681, nicht bei 3 omega | teilweise |
| VF6 | Gitter aendert nu und phi_max um < 2 % | <= 0,3 %, nu gleich | getroffen |
| VF7 [H] | Gegentakt-Stellen bei kleinem g innerhalb +-0,01 der psi_2-Leiter, Umlauf +-1 | Umlauf -1/+1; Abstand -0,0085 und -0,0102 | teilweise (zweite Stelle 0,0002 ausserhalb) |
| VF7a [H] | 0,705 +- 0,003 und 0,633 +- 0,006, entgegengesetzte Umlaufzahl | 0,702252 und 0,635507, -1 und +1 | getroffen |
| VF8 [H] | M3: kein Rotor; phi_max, nu nach F.1 (+-30 %, +-25 %) | kein Rotor; phi_max 30 bis 40 % kleiner; nu praktisch konstant | teilweise |
| VF9 [H] | reine Libration: Fluss faellt ab z0 = 0,4 um >= 10x | Fluss steigt (3. Harmonische uebernimmt); die 2. Harmonische schliesst wie erwartet | widerlegt |
| VF10 | Kick 0,3 auf stiller Gegentakt-Stelle: Linie >= 10x schwaecher | 5,4e-6 gegen 1,0e-5 und 3,2e-6 | widerlegt |
| VF11 | Kick 0,05, Delta 0,05: Linie >= 5x schwaecher | 4,7e-8 gegen 1,07e-6 und 7,1e-7 (Faktor 23 und 15) | getroffen |
| VF12 [H] | nahe der Separatrix (z0 = 0,8 bis 0,99) kein Laufen; phi_max +-15 %, nu +-30 % | kein Laufen (Spanne <= 1,60 rad); phi_max +0 bis +4 %; nu +9 / +23 / +33 % | getroffen bis auf nu bei z0 = 0,99 (+33 %) |

- Bilanz ROT-2: 7 getroffen (VF1, VF2, VF4, VF6, VF7a, VF11, VF12 mit einer Ausnahme), 4 teilweise (VF3, VF5, VF7, VF8),
  2 widerlegt (VF9, VF10).
- Zusaetzlich, nicht vorab gebunden: Abfall des Flusses um den Faktor 7 beim Schliessen der 3. Harmonischen (ROT.2c).

### ROT.6 Rechenzeiten, Dateien, Regelverstoesse

- Laeufe auf der .69 (Python-Zeit laut Bericht):

  | Lauf | Spur | Python |
  |---|---|---|
  | A | p4000a | 427,4 s |
  | B | p4000b | 458,2 s |
  | C | p4000a | 130,9 s |
  | D | p4000b | 172,3 s |
  | E | cpu | 425,2 s |
  | F (3 Laeufe) | cpu | 3 x 27 s |
  | antiscan | cpu | 261,1 s |
  | AG1 | p4000b | 153,1 s |
  | AG2 | cpu2 | 98,8 s |
  | Zeitauslese | p4000b | < 1 s |
  | G (3 Laeufe, Delta 0,05) | cpu | 67,6 / 67,0 / 68,3 s |
  | H (4 Laeufe, nach der Pause) | cpu | 188,3 s |

  - Alles unter 10 min je Aufruf. Die .69 war stark belastet (Last 10,6 um 06:32 UTC).
  - Summe ROT-2: 2600 s = 43 min Python-Zeit.
  - Unterbrechung: etwa 08:37 bis 09:51 angehalten (Nutzungslimit der Leitung, Angabe der Leitung). Die Laeufe G endeten
    in der Pause (06:46:47 UTC). Nach der Pause kamen Lauf H und die Abschnitte ROT.2b, ROT.2c und ROT.3b dazu.
- Rauchtests lokal: rot-rauch1 4,9 s, rot-rauch2 4,7 s, anti-rauch1 4,3 s.
- Abgebrochen in der Warteschlange: Lauf E auf p4000a, weil fuenf fremde Laeufe davor standen; neu auf cpu.
- **Regelverstoesse (selbst gemeldet):**
  - Lokal habe ich einmal `python3 -` mit leerem Heredoc aufgerufen (Tippfehler beim Zusammensetzen eines Befehls).
    Das war ein Interpreterstart ohne Rechnung, aber gegen die Regel. Zeit nicht eigens gemessen: zwischen 07:54:19 und
    07:55:31 (date-Ausgaben davor und danach).
  - In PLAN F.9 stand zuerst eine geschaetzte Zeit (08:20:40 statt 08:20:00). Ich habe sie um 08:20:11 auf den gemessenen
    Wert berichtigt, die eingefrorene Kopie ersetzt (-0820b) und den Vorgang im Kopf von F.9 vermerkt.
  - Derselbe Fehler noch einmal in F.10 (09:58 geschaetzt, 09:57:10 gemessen). Berichtigt vor dem Lauf H, Kopie -0957, im
    Kopf von F.10 vermerkt.
- Dateien:
  - RUNDE-08/gf-bic/gfbic_rot.py, gfbic_anti.py, gfbic_rot_zeit.py
  - PLAN.md (Nachtrag F)
  - lauf-69-rot2/ (Berichte, JSON, npz-Zeitreihen, 67 MB)
  - .69: /home/fmh/fmhc-physics-remote/runde9-rot2/

### Einfach gesagt (ROT-2)

Wir wollten wissen, ob sich im gemischten Ball die beiden Feldsorten gegeneinander drehen koennen wie ein kleiner Kreisel.
Das tun sie kaum: Gibt man einer Sorte einen Schubs, pendelt der Phasenunterschied nur hin und her, statt herumzulaufen.
Der Grund ist, dass die Kopplung selbst davon abhaengt, wie die Ladung auf die beiden Sorten verteilt ist. Nur ein sehr
starker Schubs bringt ein paar Umdrehungen; dabei geht Ladung verloren, und danach pendelt der Ball wieder. Das Pendeln
selbst lebt sehr lange. Je weiter es ausschlaegt, desto langsamer wird es, und dabei schalten sich seine Abstrahlkanaele
der Reihe nach ab; einmal sank die Abstrahlung dadurch auf ein Siebtel. Und ja: Auch das Gegeneinander-Schwingen der
beiden Sorten hat stille Stellen, an denen sein Hauptkanal nicht abstrahlt.
