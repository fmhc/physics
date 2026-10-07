# NLS-LEITER (Runde 10): Ergebnis

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung claude-primary (Finn: "bekommen wir damit eine ueberleitung auf
  echte physik / experimente hin?"). Explorativ (v3).
- Beginn 2026-09-30 11:25:37 CEST (date). PLAN.md ab 11:27:48 vor jedem Lauf; Nachtrag PLAN Abschnitt 5 um 11:37:09 vor
  jedem Lauf des Zusatzmodells. Diese Datei begonnen 2026-09-30 11:41:05 CEST (date); Ende: letzte Zeile.
- Code:
  - nls1.py: kubisch-quintisch, Kopie von RUNDE-09/mess1/mess1.py mit Dimension d = 2/3 und exakten 2D-Randfunktionen
    (scipy hankel1e/kve).
  - nls2.py: Kopie von nls1.py mit Modellschalter cq/qs und dem Befehl "kanal" (nackter geschlossener Kanal).
  - Staende (SHA-256, erste 16 Zeichen): nls1.py 9d9788fd334a0b28 (alle nls1-Laeufe); nls2.py 074f2e6588bb3838 (.69-Laeufe
    und Rauchtests bis 11:50), danach lokal 3981995b0a43e701 (nur Zusatz --beta und Kopfzeile, fuer kanal-qb-beta*).
- Laeufe: .69 ueber kleintest.sh (Spuren cpu6, p4000a, p4000b), Ausgaben lauf-69/; Rauchtests lokal (CPU, 1 Thread, nice
  19, timeout 120) in lauf-lokal/. Bei jeder Zahl steht, woher sie kommt.
- Markierungen: **[H]** Hypothese; **[A]** an der Quelle gelesen; **[L?]** aus dem Gedaechtnis. Modell ist keine Messung.

## 0. Ergebnis zuerst

1. **Stille Stellen im kubisch-quintischen NLS: nein**, weder in 3D noch in 2D.
   - 3D: W-Gitter auf der .69 in zwei Gitterstufen (57 Omega von 0,03 bis 0,17 mal 197 nu bis 1,0): keine Zelle, in der
     beide Komponenten das Vorzeichen wechseln. Die Nullkonturen liegen in getrennten Bereichen; Umlauf 0 (Rauchtest) auf einem grossen
     Rechteck dort, wo sie sich am naechsten kommen.
   - 2D: gleiches Bild auf der .69 in zwei Gitterstufen (w2a h = 0,02 und w2b h = 0,01, je 61 Omega bis 0,18 mal 197 nu;
     bei h = 0,01 ist nur die Zeile 0,18 ungueltig), gleiche Konturen, keine Kandidatenzelle.
   - Bis nu = 3 (Rauchtest): Re W wechselt nirgends das Vorzeichen.
   - Zaehlmaschine geprueft: bekannte Q-Ball-Stelle Umlauf +1, Nachbarkasten 0 (.69, h = 0,01).
2. **Grund, direkt gemessen:** Die Wand der Flachkuppe bindet einen Zustand des geschlossenen Kanals, aber bei
   E_0 ~ +0,02, rund 0,1 ueber der Einbettungsgrenze -Omega/2. Er liegt also unter der Emissionsschwelle und kann keine
   Feshbach-Resonanz im Kontinuum bilden. Beim Q-Ball liegt dieser Zustand (E = 0,706) im Kontinuum. Dieselbe Pruefung
   bestaetigt die MESS-1-Begruendung beim Petrov-Troepfchen (E_0 ~ +0,1 statt < mu ~ -0,45).
   - Eingebettete nackte Zustaende gibt es nur bei dicken Solitonen (Omega <= 0,05 in 3D, <= 0,06 in 2D); das sind
     Volumenzustaende ohne Leiter.
   - Die Atmung ist fuer Flachkuppen gebunden und im mittleren Bereich breit (Guete 1,1 bis 2,2), wie beim Troepfchen
     (MESS-1).
3. **Auch das quintisch-septische NLS (vorab als bester nichtrelativistischer Kandidat benannt) hat keine Leiter:** Die
   Energiebilanz liesse einen Wandtopf zu, die Nullpunktsenergie hebt den Zustand aber ueber die Grenze.
4. **Die Leiter braucht den relativistischen Zweig [H]:** Im Klein-Gordon-Modell bleibt der Wandzustand auch fuer fast
   nichtrelativistische
   Q-Baelle (beta = 1 bis 4) gebunden (nur der nackte Zustand gerechnet), bei rho ~ 2 m, also im Bereich der
   Teilchen-Antiteilchen-Mischung (ob die Leiter selbst dort existiert, ist offen, Abschnitt 7). Das NLS schneidet diesen
   Bereich ab.
   Fuer Optik (fluessiges Licht, CS2) und kalte Atome (Troepfchen) folgt: keine stille Leiter, nichts
   zum Messen. Eine Ueberleitung braucht ein Medium mit zwei Frequenzzweigen und Luecke, z. B. Gap-Solitonen in Gittern
   oder praezedierende Solitonen in Antiferromagneten [H].
5. Vorab gegen Ausgang: Kern-Erwartung "nein" (~85 %) getroffen; Profile gegen Pego/Warchall getroffen (2D-Kinkradius
   +0,98 zur Formel); Zusatzhypothese quintisch-septisch (~35 %) nicht eingetreten.
   - Belegstufe: "nicht gesehen" im abgeschnittenen radialen linearen Modell (l = 0), W-Gitter in zwei Gitterstufen,
     Positivkontrolle der Zaehlmaschine bestanden (3D). Kein Beweis der Abwesenheit; Omega naeher an 3/16 als 0,17 (3D)
     bzw. 0,18 (2D) ist nicht gerechnet.

## 1. Kontrollen

| Kontrolle | Ergebnis | Quelle |
|---|---|---|
| Zaehlmaschine am Q-Ball (bekannte Stelle omega*^2 = 0,797677, rho* = 1,7446) | Umlauf +1 in der Zelle omega^2 0,7976..0,7980, rho 1,744..1,745; Nachbarkasten 0,7996..0,8008: 0 | Rauchtest qb-rauch (h = 0,02) und .69-Lauf qb01 (h = 0,01), gleich |
| Nackter Kanal am Q-Ball (Kontrolle fuer "kanal") | genau ein Wandzustand unter dem Kontinuum: E = 0,706247 bei omega^2 = 0,7977 (Codex Arm A: (omega - rho_c)^2 = 0,7063), ebenso 0,698 bis 0,719 fuer omega^2 = 0,60 bis 0,90 | Rauchtest kanal-qb-rauch und .69-Lauf kqb, gleich |
| Flachkuppe gegen PW [A] | w(0) -> a_* = 0,8660 fuer Omega -> 3/16 (2D: 0,8744 bei 0,18 = Gipfelwert sqrt((1 + sqrt(1 - 4 Omega))/2)) | Rauchtest prof2-rauch |
| Kinkradius 2D gegen PW (A.22, m = 0) [A] | R_kink - sqrt(3)/(8 (3/16 - Omega)) = +0,99 / +0,98 / +0,98 bei Omega = 0,17 / 0,175 / 0,18 (12,4 / 17,3 / 28,9 nach PW); Vorab-Band +-1,5 getroffen | Rauchtest prof2-rauch |
| Kinkradius 3D (Hand: doppelte PW-Formel) | +1,55 / +1,65 / +1,69 bei Omega = 0,15 / 0,165 / 0,17 | Rauchtest prof3-rauch |
| Norm N(Omega) | monoton steigend fuer Omega >= 0,05 (2D) bzw. >= 0,03 (3D): stabiler Ast (PW: stabil fuer dN/dOmega > 0 [A]) | Rauchtests |
| Klein-Gordon gegen NLS im Ueberlapp (3D) | Nichtrelativistische Grenze (Hand): rho_KG = (4/3) nu_PW bei omega^2 = 1 - (8/3) Omega. Gebundene Atmung bei Omega = 0,035: KG-Q-Ball rho = 0,04529, NLS (4/3) x 0,03441 = 0,04588 (1,3 % Abstand, relativistische Korrektur); bei 0,03 nahe dem Vakhitov-Kolokolov-Punkt 16 % | Rauchtest kg-nls-rauch (Skript im Scratchpad) |
| Profilgrenze | Schiessen in doppelter Genauigkeit traegt 2D bis Omega = 0,18 (R_kink 29,8), 3D bis 0,17 (26,4); 3D bei 0,175 ungueltig (Klammer auf dem Plateau auseinander) | Rauchtests |

## 2. Kubisch-quintisches NLS: Atmung, Breite, W-Gitter

### 2.1 3D

- **W-Gitter (.69, w3a h = 0,02 und w3b h = 0,01; 57 Omega von 0,03 bis 0,17 mal 197 nu von 0,02 bis 1,0): keine
  Kandidatenzelle** (beide Komponenten wechseln das Vorzeichen, nu > Omega). Imaginaere Reste 0,0.
- Lage der Nullkonturen (nu der Vorzeichenwechsel, nur nu > Omega), auf beiden Gitterstufen gleich (einzige Abweichung
  0,79 -> 0,785 bei Omega = 0,09):
  - Re W = 0 nur fuer Omega = 0,040 bis 0,0725: von nu = 0,715 (Omega 0,04) hinunter zur Schwelle (nu = 0,075 bei 0,0725).
  - Im W = 0 fuer Omega <= 0,045 knapp ueber der Schwelle (nu = 0,05 bis 0,065) und fuer Omega >= 0,09 in 1 bis 5 Aesten
    (Hohlraumaeste der Obertoene, z. B. 0,195 / 0,325 / 0,48 / 0,65 / 0,85 bei Omega = 0,17).
  - Wo beide in derselben Zeile auftreten (Omega 0,040 bis 0,045), liegen sie bei nu ~ 0,05 und 0,36 bis 0,72, weit
    auseinander. Die Konturen treffen sich nirgends.
  - Feines Gitter im Duennwandbereich (Rauchtest w3-duenn-rauch: 41 Omega von 0,15 bis 0,17 mal 171 nu bis 1,0): Re W
    wechselt dort kein einziges Mal das Vorzeichen. Eine Stelle ist in diesem Bereich also ausgeschlossen (auf dem Gitter).
  - Umlauf auf einem grossen Rechteck genau dort (Rauchtest u3-rauch: Omega 0,035 bis 0,05, nu 0,07 bis 0,73): 0,
    groesster Phasensprung 0,16 rad, min |W| 0,20. Gleiches in 2D (u2-rauch: Omega 0,075 bis 0,105, nu 0,11 bis 0,61): 0.
- Atmung (.69 g3; Rauchtests geb3-rauch, p3-rauch, p3-rauch-b; .69 p3 s. u.):
  - .69 g3: N faellt bis mindestens Omega = 0,025 (N = 189,5; dort kein gebundener Zustand ueber nu = 0,002, die Atmung
    wird nahe dem Vakhitov-Kolokolov-Punkt weich [H]); gebunden bei 0,03 (nu = 0,0247)
    und 0,035 (0,0344, knapp unter der Schwelle), nicht gebunden von 0,04 bis 0,16, wieder gebunden ab 0,165 (0,1425) und
    0,17 (0,1133). Fenster ueber der Schwelle also etwa Omega = 0,036 bis 0,163 (N ~ 200 bis ~20000).
  - gebunden (nu < Omega) bei Omega = 0,03 (nu = 0,0247) und 0,17 (nu = 0,1133; Hand: Schallmode c k mit c = 0,866 und
    k R = pi gibt 2,72/R_kink = 0,103, also 10 % darunter);
  - dazwischen (0,06 bis 0,14) kein gebundener l = 0-Zustand: Fenster der Selbstverdampfung wie beim Troepfchen;
  - Pole dort breit oder keine (.69 p3, Gitter Re nu von Omega - 0,05 bis Omega + 1,0, Gamma bis 0,6): Omega = 0,04 / 0,06 /
    0,08 / 0,10 / 0,12 kein Pol; 0,14: nu = 0,2630 - 0,1195 i (Gamma/Re nu = 0,45); 0,16: 0,3697 - 0,0854 i (0,23),
    0,6205 - 0,1664 i (0,27) und
    0,9161 - 0,2724 i (0,30). Guete also 1,1 bis 2,2, kein schmaler Pol.

### 2.2 2D

- W-Gitter, Rauchtest w2-rauch-gross (lokal, h = 0,02, 31 Omega von 0,03 bis 0,18 mal 99 nu von 0,02 bis 1,0): **keine
  Kandidatenzelle**. Re W = 0 nur fuer Omega = 0,095 bis 0,11 (nu 0,6 -> 0,14), Im W = 0 fuer Omega <= 0,075 (nu 0,09
  bis 0,1) und fuer Omega >= 0,14 (Hohlraumaeste). Getrennt wie in 3D.
- **.69-Lauf w2a (h = 0,02, 61 Omega von 0,03 bis 0,18 mal 197 nu bis 1,0): keine Kandidatenzelle.** Alle Profile gueltig
  (Anschluss hoechstens 1,5e-2 bei 0,18). Konturen wie im Rauchtest: Re W = 0 nur fuer Omega = 0,0975 bis 0,1125 (nu 0,42
  -> 0,115 an der Schwelle), Im W = 0 fuer Omega <= 0,075 (nu 0,09 bis 0,1) und ab 0,1425 (Hohlraumaeste, bei 0,18: 0,245 /
  0,365 / 0,5 / 0,65 / 0,82). Zweite Gitterstufe: Rauchtest w2-rauch-h01 (h = 0,01, 21 x 99) ohne Kandidatenzelle, gleiche
  Konturen (die Zeile 0,18 ist dort ungueltig, Profilanschluss 0,4). **.69-Lauf w2b (h = 0,01, 61 x 197): keine
  Kandidatenzelle**, Konturen an denselben Gitterpunkten wie w2a; nur die Zeile 0,18 ist bei h = 0,01 ungueltig
  (Profilanschluss 0,38), die uebrigen 60 Zeilen gueltig.
- Atmung (.69 g2; Rauchtests geb2-rauch, p2-rauch; .69 p2 s. u.):
  - .69 g2: gebunden bei Omega = 0,17 (nu = 0,1615, knapp unter der Schwelle), 0,175 (0,1236) und 0,18 (0,0747 und
    0,1678); von 0,08 bis 0,16 ausser der sehr tiefen Mode (s. u.) kein gebundener l = 0-Zustand; bei 0,06 liegt noch
    eine Mode knapp unter der Schwelle (0,0597, Rauchtest). Fenster ueber der Schwelle also etwa
    Omega = 0,07 bis 0,168 (N ~ 17 bis ~350).
  - Bei Omega = 0,03 bis 0,10 eine sehr tiefe gebundene Mode, nu = 0,0022 bis 0,0028, gitterstabil (h = 0,02 und 0,01:
    0,00277771 / 0,00277786 bei 0,06; Rauchtests geb2-tief-*); sie faellt mit Omega (0,0028 / 0,0026 / 0,0022 / 0,0017 bei
    0,06 / 0,08 / 0,10 / 0,12). Deutung offen (Rest der
    Skalen-Entartung des kritischen 2D-NLS [H]), und bei 0,03 und 0,06 eine zweite knapp unter der Schwelle.
  - Feines Gitter im Duennwandbereich (Rauchtest w2-duenn-rauch: 41 Omega von 0,16 bis 0,18 mal 169 nu bis 1,0, Profile
    gueltig): Re W wechselt kein einziges Mal das Vorzeichen, wie in 3D.
  - Pole im Fenster (.69 p2 und Rauchtests p2-rauch, p2-rauch-b): Omega = 0,16: nu = 0,1930 - 0,0843 i (Gamma/Re nu =
    0,44, Guete ~1); bei 0,10 / 0,12 / 0,14 / 0,15 / 0,17 kein Pol mit Gamma < 0,6 (bei 0,12 nur die sehr tiefe gebundene Mode,
    nu = 0,00168);
    die Guete liegt also bei ~1.
  - Omega = 0,18 (Flachkuppe, R_kink = 29,8): gebunden bei nu = 0,0747 und 0,1678 (Hand: c j_0-Nullstellen,
    0,866 x 2,405/R = 0,070 und 0,866 x 5,52/R = 0,160).

## 3. Warum nicht: der nackte geschlossene Kanal

- Test "kanal" (nls2.py): tiefste Eigenwerte E des nackten geschlossenen Kanals (Kopplung C = 0), -1/2 U'' + D U
  (NLS-intern). Ein Zustand dieses Kanals liegt im Kontinuum des offenen Kanals (und kann wie beim Q-Ball eine schmale
  Feshbach-Resonanz tragen), wenn E < -Omega/2; dann nu_c = -2 E > Omega.
- Q-Ball-Kontrolle: genau ein Wandzustand bei E = (omega - rho)^2 = 0,706 (omega^2 = 0,7977), wie Codex' Arm A.
- Kubisch-quintisch (.69-Laeufe kcq3 und kcq2, ziffergleich mit den Rauchtests):

  | Omega | 3D: E_0 (noetig < -Omega/2) | 2D: E_0 |
  |---|---|---|
  | 0,03 | -0,0385 (eingebettet, nu_c = 0,077) | -0,0233 (eingebettet, nu_c = 0,047) |
  | 0,04 | -0,0371 (eingebettet, nu_c = 0,074) | -0,0285 (eingebettet, nu_c = 0,057) |
  | 0,05 | -0,0328 (eingebettet, nu_c = 0,066) | -0,0324 (eingebettet, nu_c = 0,065) |
  | 0,06 | -0,0271 (nein, knapp) | -0,0349 (eingebettet, nu_c = 0,070) |
  | 0,08 | -0,0146 (nein) | -0,0349 (nein, knapp) |
  | 0,10 | -0,0029 (nein) | -0,0278 (nein) |
  | 0,14 | +0,0151 (nein) | +0,0040 (nein) |
  | 0,16 | +0,0213 (nein) | +0,0179 (nein) |
  | 0,17 | +0,0236 (nein) | +0,0222 (nein, Rauchtest) |
  | 0,18 | (Profil ungueltig) | +0,0250 (nein) |

- Lesart:
  - Im Flachkuppenbereich bindet die Wand zwar einen Zustand des Kanals v, aber bei E_0 ~ +0,02, also rund 0,1 ueber der
    Einbettungsgrenze -Omega/2 ~ -0,085. Er liegt damit unter der Emissionsschwelle und gehoert zu den diskreten
    Bogoliubov-Moden. Eine Feshbach-Resonanz im Kontinuum kann er nicht tragen. Genau das fehlt gegenueber dem Q-Ball.
  - Eingebettete nackte Zustaende gibt es nur bei kleinem Omega (dicke, buckelfoermige Solitonen). Dort sind sie
    Volumenzustaende, nicht an eine Wand gebunden, wie beim Log-Potential der Runde 7. Auch dort zeigt W keine Stelle,
    und es gibt dort keinen schmalen Pol: Rauchtests p2-dick-rauch und p3-dick-rauch (Omega = 0,04 bis 0,06 in 2D, 0,03
    bis 0,05 in 3D, Re nu von Omega - 0,01 bis Omega + 0,12) finden keinen Pol mit Gamma < 0,1.
- Physikalischer Grund (Hand, PLAN.md):
  - Nichtrelativistisch liegt der geschlossene Kanal bei mu - eps, also mindestens 2 |mu'| = Omega unter seiner
    Kontinuumskante; der Wandtopf von D ist nur 1/6 tief und zu schmal fuer die Nullpunktsenergie.
  - Beim Klein-Gordon-Q-Ball ist der geschlossene Kanal der Zweig bei omega - rho ~ -omega (rho ~ 2 omega), knapp unter
    der Massenluecke. Die Leiter lebt also bei Frequenzen der Groesse 2 m ueber der Solitonfrequenz, im Bereich der
    Teilchen-Antiteilchen-Mischung. Diesen Zweig hat das NLS nicht; es beschreibt nur Stoerungen mit rho << omega.
- Dieselbe Pruefung am Petrov-Troepfchen aus MESS-1 (Rauchtest egpe-kanal-rauch, mess1.py unveraendert importiert):
  eingebettet nur bei mu = -0,10 (N~ = 20, dicht an N~_c); ab N~ = 34 nicht, im Flachkuppenbereich E_0 = +0,08 bis +0,11
  gegen noetig < mu = -0,40 bis -0,46. Damit ist die MESS-1-Begruendung (fehlender Wandtopf) auch numerisch belegt.
- Literaturbezug: Das passt zur NLS-Mathematik, die fuer Grundzustaende keine eingebetteten Eigenwerte erwartet
  (Cuccagna, Maeda; zitiert nach RUNDE-07/L4-BIC-FAMILIE-LITERATUR.md und MODELL-DUENNWAND.md Punkt 6, dort [A], von mir
  nicht an der Quelle gelesen).
- **Gegenprobe im Klein-Gordon-Modell selbst** (Rauchtests kanal-qb-beta*): Auch wenn der Q-Ball nichtrelativistisch wird
  (grosses beta, omega_c^2 = 1 - 1/(4 beta) -> 1), bleibt der nackte Wandzustand des Antiteilchen-Kanals gebunden:
  E = 0,84 bis 0,86 (beta = 1), 0,92 bis 0,93 (beta = 2), 0,96 (beta = 4), Kontinuum ab 1, Bindung ~0,16/beta. Er liegt bei
  rho_c = omega + sqrt(E) ~ 2 m. Der Baustein der Leiter haengt also nicht daran, dass der Soliton relativistisch ist, sondern daran,
  dass die Stoerungen bei 2 m den Antiteilchen-Zweig erreichen. Die NLS-Naeherung schneidet genau diesen Bereich ab. Ob die
  Leiter selbst bei beta = 1 bis 4 existiert, ist nicht gerechnet (nur der nackte Zustand) [H,
  Schluss aus diesen Zahlen].

## 4. Zusatzmodell quintisch-septisch [H]

- Vorab (PLAN Abschnitt 5, 11:37:09, vor jedem Lauf): Das Energie-Kriterium ((p+1)/(q+1))^(2p/(q-p)) > 2/(p+1)^2 fuer
  F(n) = (-n^p + n^q)/2 laesst beim quintisch-septischen NLS (p = 2, q = 3) einen Wandtopf zu (0,316 > 0,222), beim
  kubisch-quintischen nicht (0,444 < 0,5). Erwartung: Stellen moeglich (~35 %), dann knapp ueber der Schwelle.
- Ausgang:
  - Nackter Kanal (.69 kqs3 und kqs2, gleich den Rauchtests): 3D kein eingebetteter Zustand bei Omega = 0,02 bis
    0,07 (E_0 = -0,0056 bei 0,02, noetig < -0,01; ab 0,03 positiv); 2D nur bei 0,02 und 0,03 (nu_c = 0,059 und 0,045). Im
    Flachkuppenbereich (Omega_* = 64/729 = 0,0878) liegt E_0 bei +0,011 bis +0,020. **Die Nullpunktsenergie zehrt den
    Topf auf**; das Energie-Kriterium ist notwendig, nicht hinreichend.
  - W-Gitter: Rauchtests qs-w3-rauch (11 Omega x 59 nu, h = 0,02), qs-w3-rauch-h01 (11 x 60, h = 0,01) und
    qs-w2-rauch-gross (25 x 80): keine Kandidatenzelle. .69-Lauf wqs3 (51 Omega von 0,02 bis 0,07 mal 159 nu bis 0,8,
    Profile gueltig): keine Kandidatenzelle, Re W wechselt nur fuer Omega = 0,020 bis 0,027 das Vorzeichen;
    .69-Lauf wqs2 (2D, 61 Omega von 0,02 bis 0,08 mal 159 nu bis 0,8, Profile gueltig): keine Kandidatenzelle.
  - Zusatzhypothese damit **nicht bestaetigt**: auch das quintisch-septische NLS hat keine stille Leiter.

## 5. Laborbezug

- Stille Stellen gibt es in beiden NLS-Modellen nicht; eine Umrechnung von Stellen entfaellt.
- Zur Einordnung die optische Standardnormierung (Hand, paraxial): 2 i k A_z + Lap_perp A + 2 k^2 (n2 I - |n4| I^2)/n0 A = 0
  geht mit A = sqrt(I0) u, x = x0 xi, z = 2 k x0^2 zeta ueber in PW Gl. (1.1), wenn
  I0 = n2/|n4|,  x0^2 = n0 |n4| / (2 k^2 n2^2),  Leistung P = N lambda^2 / (8 pi^2 n0 n2).
  - Probe: Die Townes-Norm 11,70 gibt P = 0,148 lambda^2/(n0 n2), die bekannte kritische Leistung des Kerr-Mediums
    (1,86 lambda^2/(4 pi n0 n2) = 0,148 lambda^2/(n0 n2)) [L?].
  - Mit Werten fuer fluessiges CS2 bei 920 nm [L?, Falcao-Filho u. a. 2013, nicht an der Quelle]: n0 = 1,6,
    n2 = 3,1e-19 m^2/W, |n4| = 5,2e-33 m^4/W^2: I0 ~ 6 GW/cm^2, x0 ~ 19 um, Leistungseinheit ~22 kW. Ein 2D-Flachkuppen-
    Strahl bei Omega = 0,17 (N = 368) entspraeche ~8 MW Spitzenleistung und ~0,25 mm Radius.
- Was im Modell pruefbar waere, ohne Stellen: Die l = 0-Atmung ist fuer grosse Flachkuppen gebunden (ungedaempft im
  linearen Modell) und im mittleren Bereich stark gedaempft (Guete hoechstens ~2). Das ist das Troepfchen-Bild aus MESS-1,
  keine Leiter.
  - Groessenordnung in CS2 (Hand, mit den [L?]-Werten): Laengeneinheit der Ausbreitung z0 = 2 k x0^2 ~ 8 mm. Die breite
    2D-Atmung bei Omega = 0,16 (nu = 0,193 - 0,084 i) haette eine Periode von ~26 cm und eine Abklinglaenge von ~9 cm,
    das Fenster Omega = 0,07 bis 0,168 laege bei ~0,4 bis ~8 MW. Uebliche CS2-Zellen sind nur Millimeter bis Zentimeter
    lang [L?]; selbst die gewoehnliche Atmung waere dort kaum zu verfolgen.
- **Ueberleitung auf echte Physik [H]:** Die Leiter lebt bei Stoerfrequenzen der Groesse 2 m, wo Teilchen- und
  Antiteilchenzweig mischen. Ein Laboranalogon braucht deshalb ein Spektrum mit zwei Zweigen und einer Luecke dazwischen
  (Klein-Gordon- oder Dirac-artig) plus einen nichtlinearen lokalisierten Zustand. Kandidaten, nicht gerechnet:
  - Gap-Solitonen in Bragg-Gittern und binaeren Wellenleiterarrays (nichtlineare Dirac-Gleichung, Optik)
  - Gap-Solitonen von Kondensaten in optischen Gittern
  - Rabi-gekoppelte Zweikomponenten-Kondensate (Spinzweig mit einstellbarer Luecke; Blasen aus dem falschen Vakuum sind
    dort beobachtet [L?])
  - Antiferromagnete mit leichter Achse: Ihre Magnonen gehorchen einer Lorentz-artigen Gleichung mit Luecke (zwei
    Zweige), und praezedierende Solitonen tragen eine erhaltene Magnonenzahl, sind also Q-Ball-artig [L?]. Das waere das
    naechste echte Klein-Gordon-System mit U(1)-Ladung.
  - Troepfchen, kubisch-quintisches oder quintisch-septisches Licht sind nach diesem Ergebnis nicht der richtige Pruefstand.

## 6. Vorab gegen Ausgang

| Vorab (PLAN.md) | Ausgang |
|---|---|
| Kern: keine stillen Stellen der l = 0-Atmung, 3D und 2D (~85 %), Grund: kein Wandtopf fuer den geschlossenen Kanal | getroffen (3D und 2D je zwei Gitterstufen auf der .69); der Grund ist mit "kanal" direkt bestaetigt (Abschnitt 3) |
| Scheiterregel (Zelle mit Umlauf +-1 auf zwei Gitterstufen und eigenem Rechteck) | nicht eingetreten; keine einzige Kandidatenzelle |
| V1 Profile gegen PW: w(0) -> 0,866; 2D-Kinkradius innerhalb +-1,5 der PW-Formel | getroffen (+0,98 bis +0,99) |
| V2 Atmung fuer Flachkuppen gebunden, in 3D ein Fenster ueber der Schwelle (~70 %), in 2D offen (~50 %) | getroffen: Fenster in 3D etwa Omega = 0,036 bis 0,163, in 2D etwa 0,07 bis 0,168; Flachkuppen gebunden |
| V3 ueber der Schwelle breit (Guete <= 5), glatt | getroffen: Gamma/Re nu = 0,23 bis 0,45 (Guete 1,1 bis 2,2; 3D .69 p3, 2D Rauchtest), sonst kein Pol mit Gamma < 0,5 bis 0,6 |
| V4 W-Gitter ohne Kandidatenzelle, zwei Gitterstufen | getroffen in 3D und 2D (je zwei Gitterstufen auf der .69) |
| Zusatz (PLAN 5): quintisch-septisch hat Stellen (~35 %) | nicht eingetreten: der nackte Wandzustand bleibt wegen der Nullpunktsenergie unter der Schwelle |

## 7. Grenzen und Fehlerkasten

- Nur radial, l = 0, lineare Stoerungen; Profile im Flachkuppenbereich bis R_kink ~ 26 (3D, Omega = 0,17) bzw. ~ 30 (2D,
  0,18). Duennere Waende sind nicht gerechnet; nach Abschnitt 3 entfernt sich der Wandzustand dort weiter von der
  Einbettung (E_0 steigt auf +0,024 bis +0,025) [H].
- W-Gitter bis nu = 1,0 (.69); nu von 1 bis 3 nur als Rauchtest (w3-hochnu-rauch, w2-hochnu-rauch): dort wechselt Re W
  nirgends das Vorzeichen, also keine Stelle.
- Schwellennaehe: Die Zellenpruefung beginnt erst am ersten Gitterpunkt ueber der Schwelle (Streifen bis 0,005 breit).
  Dort ueberdeckt die Konturlage: Re W erreicht die Schwelle nur bei Omega ~ 0,074 (3D) bzw. ~ 0,113 (2D), Im W laeuft
  nahe der Schwelle nur fuer Omega <= 0,045 (3D) bzw. <= 0,075 (2D). Eine Stelle im Streifen muesste beide Konturen dort
  kreuzen lassen; das tun sie nicht.
- Aussenrand: Mit f_rand = 1e-13 statt 1e-9 (R_aus 83 bis 141 statt 59 bis 97) liegen die Vorzeichenwechsel beider
  Komponenten bei Omega = 0,045 / 0,10 / 0,15 in 2D und 3D auf denselben Gitterpunkten (Rauchtest rand-rauch, Skript im
  Sitzungs-Scratchpad, Ausgabe lauf-lokal/rand-rauch.txt).
- Optische Umrechnung paraxial, ohne Verluste und Nichtlokalitaet; CS2-Werte [L?].
- **Offen: Gibt es die Leiter im Klein-Gordon-Modell auch bei beta = 1 und 2?** Ein schneller Rauchtest-Scan
  (qb-beta-leiter-rauch, Skript im Scratchpad) findet bei beta = 0,5 genau die drei bekannten Stellen (0,63/1,65,
  0,68/1,68, 0,79/1,74; nach Ausschluss der Zellen an der zweiten Schwelle 1 + omega). Bei beta = 1 und 2 zeigt er Zellen
  mit Eck-Umlauf +-1 entlang rho ~ omega + sqrt(E_Wand) (1,80 bis 1,94). Ein aufgeloestes Rechteck um eine davon
  (beta = 1, omega^2 0,808 bis 0,822, rho 1,805 bis 1,845) gibt auf zwei Gitterstufen aber Umlauf 0. Die Eck-Umlaeufe sind
  also unzuverlaessig; die Frage ist nicht entschieden und gehoert in eine eigene Karte.
- Die Positivkontrolle der Zaehlmaschine ist dreidimensional (Q-Ball). Fuer den 2D-Rechenweg (nu_l = 1/2, exakte K- und
  H-Funktionen) gibt es keine eigene Positivkontrolle mit bekannter Stelle; geprueft sind dort nur die Profile gegen PW
  und die gebundenen Moden gegen die Schallformel (7 % Abstand wie in 3D).
- Fehlerkasten:
  - Die auf p4000a und p4000b eingereihten Laeufe (w2a, w2b, qb01, g3, g2, p3, p2) warteten ~11 min auf die Spuren und
    wurden vor dem Start abgebrochen und auf cpu6 neu eingereiht; die Logs dieser Namen wurden dabei ueberschrieben.
  - Der Rauchtest qs-w3-rauch traegt im Kopf noch den Namen "nls1.py" (Kopfzeile vor der Korrektur); gerechnet hat nls2.py
    mit Modell qs.
  - Grosse Rauchtests lokal (w2-rauch-gross 31 x 99, qs-w2-rauch-gross 25 x 80, je ~29 s) blieben unter 120 s.

## 8. Einfach gesagt

Wir haben geprueft, ob die "stillen Schwingungen" unserer Q-Baelle auch in der Gleichung vorkommen, mit der Optiker
"fluessiges Licht" und Physiker Atomtroepfchen beschreiben. Die Antwort ist nein, in drei und in zwei Dimensionen: Wenn
die Atmung eines solchen Lichttropfens ueber der Schwelle liegt, verliert sie in allen gerechneten Faellen Energie, meist in ein bis zwei
Schwingungen. Der Grund ist, dass die stillen Stellen einen am Rand gefangenen Zustand eines zweiten, eigentlich
verbotenen Kanals brauchen; beim relativistischen Q-Ball ist das der Antiteilchen-Zweig, und den gibt es in diesen
Gleichungen nicht. Dass unser Zaehlwerkzeug solche Stellen findet, wenn es sie gibt, haben wir am Q-Ball nachgeprueft.
Eine Bruecke ins Labor muesste deshalb ueber Systeme mit zwei Frequenzzweigen und einer Luecke dazwischen gehen, etwa
Gap-Solitonen in optischen Gittern.

---
Ende: 2026-09-30 12:16:46 CEST (date, nach dem Schreiben gemessen). Alle .69-Laeufe beendet (rc = 0): w3a, w3b, w2a, w2b, qb01, kcq3, kcq2, kqs3,
kqs2, kqb, g3, g2, p3, p2, wqs3, wqs2.
