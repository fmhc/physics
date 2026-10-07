# Runde 6: Die Q-Ball-Resonanz in 3D (resonanz3d)

- Bearbeiter: Anthropic-Agent (Opus), Auftrag RUNDE-06/AUFTRAG-3D-RESONANZ.md.
- Beginn 2026-09-30 02:21:26 CEST (gemessen). PLAN.md begonnen 02:56:24 (gemessen). Ende: letzte Zeile.
- Status: Code geschrieben. Lokal liefen nur py_compile, der Rauchtest und zwei Zeitproben, auf Freigabe laut Leitung
  (Nachricht 30.09. 02:42, Finn). Die Messlaeufe sind **ungerechnet**. Explorativ.
- Alle neuen Deutungen sind Hypothesen. Synthetische Kontrollen sind keine Messdatenbestaetigung.

## Kurzfassung

- **Code:** resonanz3d.py, ein Skript mit fuenf Kommandos: rauch, pole, bruecke, zeit0, zeitlin.
  Umschalter --geraet cpu|cuda, alles float64/complex128, Zeitwaechter --budget (Vorgabe 540 s).
- **pole:** lineare Zwei-Kanal-Randwertrechnung radial fuer l = 0, 1, 2. Gesucht werden:
  - gebundene Pole (reell, unter der Kante 1 - omega)
  - Resonanzen (komplex, zwischen 1 - omega und 1 + omega)

  Drei Rand- und Toleranzstufen, Nullmoden, Negativkontrolle ohne Ball, Pol-Zaehlung per Argumentprinzip.
- **bruecke (Zusatz fuer Frage 3):** Der 1D-Pol wird ueber die Raumdimension verfolgt, von dim = 1 bis 3 in Schritten
  von 0,25. Profil und Stoerung werden dabei jeweils in dim Dimensionen gerechnet.
  - Bei dim = 1 muss Codex' Pol 1,49377696 - 6,716e-5 i herauskommen (Kalibrierung).
  - Bei dim = 3 steht dann *derselbe* Pol in 3D. Er wird identifiziert, nicht geraten.
- **zeit0:** nichtlineare kugelsymmetrische Zeitentwicklung mit Stoss (eta = 0,001 und 0,01) und Ballreferenz.
- **zeitlin:** linearisierte Zeitentwicklung fuer l = 2 (Formschwingung) und l = 0. Die Frequenzen und Abklingraten
  liefert ein Matrix-Pencil-Fit.
- **Rayleigh:** Tropfenformel omega_2^2 = 8 sigma / (w R^3). sigma, w und R kommen aus dem Profil, in 12 Varianten
  (Band). Der Vergleich gilt fuer omega^2 = 0,52 bis 0,55.
- **Kernvorhersage (vor dem Rauchtest festgelegt, siehe Abschnitt 3):**
  - Der 1D-Pol wandert in 3D nach oben, auf Re rho_0 ~ 1,68, und wird 10- bis 500-mal breiter.
  - l = 1 liegt etwas hoeher, bei etwa 1,74.
  - l = 2 hat keinen solchen Pol unter 1 + omega.
  - Die l = 2-Formschwingung liegt bei omega^2 = 0,7 nahe der Kante (0,15 +- 0,05).
  - Bei duennen Waenden naehert sie sich Rayleigh: 0,0077 bei omega^2 = 0,52 bis 0,028 bei omega^2 = 0,55.

## 1. Physik und Verfahren

**Modell.**
- U = S - S^2 + S^3/2. Grundzustand phi = f(r) e^{-i omega t}.
- Stoerung [u e^{-i rho t} + v* e^{i rho* t}] e^{-i omega t} Y_lm.
- Reduziert U = r u, V = r v (allgemein r^{(dim-1)/2}):
  - U'' = [dp + l(l+1)/r^2 - (omega+rho)^2] U + sp V
  - V'' = sp U + [dp + l(l+1)/r^2 - (omega-rho)^2] V
  - dp = 1 - 4S + 4,5 S^2, sp = -2S + 3S^2
- Asymptotik:
  - Kanal omega + rho ist offen fuer rho > 1 - omega. Dort gilt die auslaufende Riccati-Hankel-Funktion exp(i q r) P_l.
  - Kanal omega - rho ist geschlossen fuer rho < 1 + omega. Dort gilt die abklingende exp(-kappa r) P_l.
- Konvention wie Codex: Im rho < 0 heisst abklingend (Ciurla u. a. konjugiert).
- Kanten:

  | omega^2 | 1 - omega | 1 + omega |
  |---|---|---|
  | 0,6 | 0,2254 | 1,7746 |
  | 0,7 | 0,1633 | 1,8367 |
  | 0,8 | 0,1056 | 1,8944 |

**Warum 3D anders ist als 1D (Profil aus RUNDE-02, Test 4, und im Rauchtest reproduziert):**
- Bei omega^2 = 0,7 hat der 3D-Ball S(0) = 1,135, Q = 473,41 und R_Q = 3,90.
- Der 1D-Ball hat nur S(0) = 0,3675. Der 3D-Ball ist also halb duennwandig: fast flacher Kern, Wand bei r ~ 3,5 bis 4.
- Folgen fuer die Stoerpotentiale:
  - Im Kern ist dp = 2,26 > 1. Fuer den Antiteilchen-Kanal wirkt der Kern allein als Wall.
  - Der Topf (dp_min = 0,111 bei S = 4/9) liegt als Kugelschale in der Wand.
  - Im Kern ist die Kopplung sp = 1,6 gross. u und v mischen dort zu Bogoliubov-Moden:
    - Schall mit c_s^2 = sp/(sp + 2 omega^2) = 0,53
    - massiver Zweig ab rho = sqrt(2 sp + 4 omega^2) ~ 2,5
- Der 1D-Pol ist dagegen ein im Zentrum gebundenes "Antiteilchen" (v-Kanal, E = (omega - rho)^2 = 0,43). Es ist nur
  schwach an den offenen Kanal gekoppelt; die Welle dort schwingt schnell mit k = 2,1. Daher ist es so schmal
  (Gamma = 6,7e-5).

**Verfahren pole (je omega^2):**
1. Profil durch Schiessen in u = f_top - f, wie tests1d Test 4:
   - Grob 2 Runden (h = 0,05), dann fein 4 Runden x 1024 Kandidaten im Fenster +-0,02.
   - Rueckfall: volles Fenster.
   - Schwanz f_c (r_c/r) e^{-kappa (r - r_c)} ab f < 1e-5 f(0).
2. **Verbundmatrix:** Integriert wird nicht die Loesung, sondern die Pluecker-Koordinaten der 2-Ebene der regulaeren
   Loesungen (von r = h nach aussen) und der Jost-Ebene (von R nach innen).
   - Grund: In duennwandigen Baellen waechst eine Kernloesung wie e^{1,4 r}. Bei R = 36 waeren die zwei regulaeren
     Loesungen sonst numerisch parallel.
   - D(rho) = <p, q> / (|p| |q|) mal einem reinen Phasenfaktor. Nullstellen von D sind die Pole.
   - Positive Normierungen und der Phasenfaktor aendern weder Nullstellen noch Umlaufzahl.
3. Drei Stufen (Rand- und Toleranzstufen):

   | Stufe | ODE-Schritt h | Profilschritt | Rand R bei f(R) = | Rolle |
   |---|---|---|---|---|
   | A | 0,02 | 0,01 | 1e-6 f(0) | Nachpolieren |
   | B | 0,01 | 0,005 | 1e-8 f(0) | volle Suche |
   | C | 0,005 | 0,0025 | 1e-10 f(0) | Nachpolieren |

   Duennwandig: h = 0,04 / 0,02 / 0,01.
4. Stufe B, volle Suche:
   - Nullmoden-Probe bei rho = 0, 1e-3, 2e-3.
   - Gebundene Zustaende: 300 Punkte in (0, 1 - omega), Vorzeichenwechsel von Re D, dann Illinois-Verfahren.
   - Resonanzen:
     - Keime aus Minima von |D| auf der reellen Achse (700 Punkte) und auf 4 Zeilen Im rho = -0,003 ... -0,07
       (160 Punkte je Zeile)
     - dann 2D-Newton
   - Zaehlung per Argumentprinzip im Kasten [1 - omega + 0,002, 1 + omega - 0,002] x [-0,1, +0,001]:
     adaptiv, bis jeder Phasensprung < 0,4 ist.
5. Stufen A und C polieren die Pole aus B nach. Die Negativkontrolle (Ball entfernt, dp = 1, sp = 0) laeuft auf dem
   Gitter von B:
   - |D_frei| an den Polen
   - Vorzeichenwechsel unter der Kante
   - Umlaufzahl

**Zeitentwicklung.**
- Radial in Psi = r phi, Leapfrog.
  - dt = 0,4 dr, stabil fuer l = 2 bis dt < 0,63 dr.
  - Daempfungsschicht ab r_sd, Dirichlet bei 0 und r_max.
- zeit0: nichtlinear.
  - Stoss psi, psi_t mal (1 + eta), wie Codex und tests1d.
  - Die Ballreferenz eta = 0 laeuft im selben Stapel mit. Das Differenzsignal entfernt den Gitterfehler des ruhenden
    Balls.
- zeitlin: im Laborsystem, Phi_tt = Phi_rr - (l(l+1)/r^2 + dp) Phi - sp e^{-2 i omega t} Phi*. Anfangsstoerung ist
  die Wandverschiebung r f'(r) r^2/(r^2+1), mitrotierend.
- Auswertung im spaeten Fenster [T/2, T]: Matrix-Pencil (Summe gedaempfter Exponentiale; Re = Frequenz,
  Im = Abklingrate) und Nulldurchgaenge der Projektion auf die Anfangsform.

**Rayleigh (nur dim = 3).** omega_2^2 = 8 sigma / (w R^3).
- w = eps + p = 2 omega^2 S(0), die Enthalpiedichte als Traegheit der relativistischen Supraflüssigkeit; Variante eps(0).
- sigma: 2 int |grad f|^2 / (4 pi R_Q^2), Laplace p_in R_Q/2 oder Kink-Wert 1/(2 sqrt 2) = 0,3536.
- R: R_Q (aequimolare Flaeche aus Q) oder R_halb.
- Hauptvariante: grad / R_Q / w; das Band spannen alle 12 Varianten auf.

## 2. Literatur (gelesen, soweit noetig)

- Kovtun, Nugaev, Shkerin 1805.03518 (papers/): Unser Modell ist genau ihr Potential (37) mit delta = 1/2, v = 1,
  omega_min = 1/sqrt 2.
  - Duennwand: R = sqrt(delta) v^2 / (2 omega_min eps), eps = omega - omega_min, also R = 0,5/eps.
  - Das stimmt mit R_Q aus unserer Q-Tabelle ueberein: 14,5 bei 0,55; 35,7 bei 0,52.
  - Ihre Stufen-Naeherung gibt Kavitaetsmoden gamma = sqrt 2 mu_{n,l+1/2} eps (Schall mit Druck null am Rand), aber
    keine Wand-Kapillarmode. Die liefert erst Rayleigh.
  - Nahe omega_c gibt es in l = 0 eine weiche Mode, keine in l = 1, 2 (Abschn. 3).
- Ciurla u. a. 2405.06591: nur 1+1 D. 3+1 D nennen sie ausdruecklich als offene Erweiterung (Abschn. 5).
  - Klassen: gebunden, halb-propagierend, QNM.
  - QNM-Kalibrierung beta = 1/4, omega = sqrt 3/2: rho = 1,538789 + 1,18e-5 i.
- Azatov u. a. 2412.13885: 3+1 D, Streuung von S-Wellen und Partialwellen am Q-Ball, Gl. (7) bis (13) = unsere
  Laborsystem-Gleichung. Keine Polliste.
- Saffin u. a. 2212.03269: 3+1 D nur kurz, Superradianz.

## 3. Vorhersagen vorab

Gedankengang 02:25 bis 02:44, vor dem Code und vor dem Rauchtest, hier unveraendert. Die Nebenbefunde des Rauchtests
stehen getrennt in 3b.

**V1 Nullmoden (omega^2 = 0,7).**
- l = 0 (Phase + Ladung) und l = 1 (Translation + Boost) haben je eine Jordan-Kette. Also D ~ rho^2:
  - |D(2e-3)|/|D(1e-3)| = 4 +- 0,4
  - |D(0)| << |D(1e-3)|
- l = 2: Verhaeltnis ~1, keine Nullmode.

**V2 rho_2 = l = 2-Formschwingung bei omega^2 = 0,7: Re rho_2 = 0,15 (0,10 bis 0,20), nahe der Kante 0,163.**
- Grund: Rayleigh mit sigma = 0,354, w = 1,59, R_Q = 3,90 ergibt 0,173. Die diffuse Wand senkt eher.
- 55 %: gebunden (reell). Sonst eine schmale Resonanz knapp ueber der Kante mit |Im rho_2| < 1e-3 (l = 2-Schwelle,
  k R ~ 1).

**V3 l = 0-Atmungsmode (Kompression):**
- Re ~ 0,45 (0,30 bis 0,65), aus c_s pi/R mit c_s = 0,73, R ~ 4 bis 4,5.
- Liegt ueber der Kante und ist damit breit: Im rho zwischen -0,1 und -0,005.

**V4 rho_0 = Fortsetzung des 1D-Pols in 3D (l = 0): Re rho_0 = 1,68 (1,55 bis 1,83), Im rho_0 ~ -3e-3
(-3e-4 bis -3e-2).**
- Grund: Der Antiteilchen-Topf wird in 3D zur Schale in der Wand. Die Bindung ist dort schwaecher (E ~ 0,8 statt 0,43),
  also gilt rho = omega + sqrt(E) ~ 1,73.
- Die Wand ist schaerfer als der 1D-Ball, also ist die Fourier-Unterdrueckung der Kopplung schwaecher. Dazu kommt die
  Mischung mit Kernschall.
- Ergebnis: 10- bis 500-mal breiter als in 1D.

**V5 rho_1: Re rho_1 ~ Re rho_0 + 0,05 bis 0,06, also ~1,74 (1,60 bis 1,835).**
- Grund: Zentrifugalterm auf der Schale, Delta E = 2/R_w^2 ~ 0,11.
- Breite aehnlich oder groesser als bei rho_0.

**V6 l = 2:** kein v-dominierter Pol unter 1 + omega. Delta E = 6/R_w^2 ~ 0,32 hebt ihn in den Bereich, in dem beide
Kanaele offen sind. Ueber der Kante liegen fuer l = 2 nur breite Kompressionspole mit |Im| > 1e-2.

**V7 Mehr Pole in 3D:** je l mindestens 2 Nullstellen im Kasten |Im| < 0,1 (Kavitaetsmoden des Kerns). In 1D gab es im
selben Streifen nur den einen schmalen geraden Pol.

**V8 Trend in omega:**
- omega^2 = 0,6 (R = 7,4): Die Formschwingung ist klar gebunden, rho_2 = 0,065 +- 0,015 (Rayleigh 0,073).
- omega^2 = 0,8 (R = 2,9): Die Formschwingung ist aufgeloest oder eine Resonanz knapp ueber 0,106.
- rho_0 verschiebt sich mit omega grob wie omega + sqrt(E).

**V9 Tropfenfrequenz (Rayleigh, Duennwand-Formeln R = 0,5/eps, sigma = 0,3536, w = 2 omega^2 S_top):**

| omega^2 | R | omega_2 Rayleigh | Periode |
|---|---|---|---|
| 0,52 | 35,7 | 0,00765 | ~820 |
| 0,53 | 23,9 | 0,0138 | ~456 |
| 0,54 | 18,0 | 0,0208 | ~303 |
| 0,55 | 14,5 | 0,0284 | ~221 |

- rho_2/omega_R -> 1 fuer omega^2 -> 0,5.
- Das Verhaeltnis liegt bei 0,55 in [0,80, 1,10] und bei 0,52 in [0,90, 1,05].
- Die Abweichung schrumpft monoton mit R (Wanddicke/R ~ 20 % bzw. 8 %).

**V10 Bruecke:**
- dim = 1 gibt Codex' Pol auf < 1e-7 (Re) und < 1 % (Im).
- Entlang dim steigt Re, und der Pol wird breiter. Bei S(0) ~ 2/3, wo sp(0) = 0, wird er vielleicht zwischendurch
  schmaler.
- Am Ende steht der Wert aus V4. 60 %: die Spur bleibt bis dim = 3 verfolgbar. Sonst endet sie an der oberen Kante
  1 + omega.

**V11 zeit0:**
- Schwacher Stoss (eta = 1e-3): spaete Frequenz innerhalb 2e-3 von Re des langlebigsten l = 0-Pols.
- Starker Stoss (1e-2): etwa 10-mal weiter weg; der Stoss aendert Q, wie in Codex' 1D-Befund.

**V12 zeitlin:** Die l = 2-Frequenz trifft das reelle rho_2 auf 1e-3 relativ (gebundener Fall), stabil ueber drei dr.

### 3b. Nebenbefunde des Rauchtests (grob, h = 0,08/0,04; keine Messung, gesehen vor Abschluss dieser Datei)

- Nullmoden bei omega^2 = 0,7, h = 0,04:
  - l = 0: Verhaeltnis 3,983, |D(0)| = 9e-8
  - l = 1: Verhaeltnis 4,004, |D(0)| = 3e-8
  - l = 2: Verhaeltnis 1,000
- Profil: S(0) = 1,135061, Q = 473,413, E = 428,642. Gleich der RUNDE-02-Tabelle (473,413 / 428,641).
- Bruecke (h = 0,04):
  - dim = 1: rho = 1,4937775 - 6,710e-5 i. Codex: 1,4937770 - 6,716e-5 i.
  - dim = 1,25: rho = 1,49802 - 1,18e-3 i. Der Pol wird frueh deutlich breiter.
- Kontur (unaufgeloest, 90 Punkte): Umlaufzahl 1 / 1 / 0 fuer l = 0 / 1 / 2. Ohne Ball 0 / 0 / 0.
  - Das spraeche gegen V7 und fuer V6. Es ist aber nicht aufgeloest; zaehlt erst im echten Lauf.
- Die Vorhersagen V1 bis V12 bleiben trotzdem unveraendert stehen.

## 4. Gegenproben

- G1 **Kalibrierung 1D:** Bruecke bei dim = 1 gegen Codex' Pol (resonance-20260930/linear/RESULT.txt). Anderer Code,
  anderes Verfahren (Verbundmatrix statt Spaltendeterminante).
- G2 **Ciurla-Pol** (--ciurla): beta = 1/4, omega^2 = 3/4, dim = 1; Soll 1,53878955 - 1,1788e-5 i.
- G3 **Nullmoden** l = 0 und l = 1 (V1).
- G4 **Negativkontrolle ohne Ball:**
  - |D_frei| an jedem Pol
  - keine Vorzeichenwechsel unter der Kante
  - Umlaufzahl 0
- G5 **Argumentprinzip** gegen die Newton-Liste: Vollstaendigkeit der Resonanzen im Kasten.
- G6 **Zeit gegen Pol:**
  - zeit0 (l = 0, nichtlinear) gegen rho_0
  - zeitlin l = 0 und l = 2 gegen die linearen Pole
- G7 **Profil** gegen die RUNDE-02-Tabelle; im Rauchtest schon gleich.
- G8 **Zweithaus:** Codex rechnet l = 0 und l = 2 unabhaengig. Abgleich erst nach beiden Laeufen, kein Austausch vorher.

## 5. Latten

Jede Latte kann bestehen und scheitern.

- **L1 Kontrollen:**
  - Nullmoden: |D(0)|/|D(1e-3)| < 0,05 und Verhaeltnis in [3,6, 4,4] fuer l = 0, 1; fuer l = 2 in [0,8, 1,25].
  - Ohne Ball: |D_frei| > 1e-3 an jedem Pol, Umlauf 0, keine Vorzeichenwechsel.
  - G1: |Delta Re| < 1e-7 und |Delta Im|/|Im| < 1 % bei h = 0,01.
  - G2: |Delta Re| < 2e-5 und |Delta Im|/|Im| < 20 % (Codex' Vorab-Toleranzen).
- **L2 drei Toleranzstufen:**
  - Jeder berichtete Pol erscheint in A, B und C.
  - |rho_B - rho_C| < 1e-6 und < 5 % von |Im rho|.
  - |rho_A - rho_B| > |rho_B - rho_C| (monotone Konvergenz). Sonst wird der Pol als unsicher markiert.
- **L3 drei Aufloesungen der Zeitentwicklung:**
  - Die spaete Hauptfrequenz konvergiert: |f(dr/2) - f(dr/4)| < |f(dr) - f(dr/2)|.
  - Feinstes dr: zeitlin innerhalb 1e-3 relativ vom linearen Pol, zeit0 (eta = 1e-3) innerhalb 2e-3.
  - Abklingrate innerhalb 30 %, wenn |Im rho| x Fensterlaenge > 0,05; sonst nur als obere Schranke.
- **L4 Vollstaendigkeit:** Die aufgeloeste Umlaufzahl ist gleich der Zahl der Newton-Pole im Kasten, je l. Bei
  Abweichung gilt die Polliste als unvollstaendig.
- **L5 Rayleigh:**
  - Bei omega^2 = 0,52 bis 0,55 stimmen Polrechner (reell) und zeitlin fuer die l = 2-Formschwingung auf 2 % ueberein.
  - rho_2 liegt bei 0,52 im Rayleigh-Band.
  - |rho_2/omega_R,haupt - 1| faellt von 0,55 nach 0,52.

## 6. Aufrufe (Leitung, auf der .69)

- Vorbereitung: resonanz3d.py nach /home/fmh/fmhc-physics-remote/runde6-3d-resonanz/ kopieren.
- Jeder Aufruf hat die Form

      cd /home/fmh/fmhc-physics-remote/runde6-3d-resonanz && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> resonanz3d.py <kommando> --geraet cpu ...

- Ausgabe je Aufruf: <out>/<kommando>.json und <out>/<kommando>_bericht.txt. Die Dateien werden nach jeder Stufe
  gesichert; ein Abbruch verliert nichts Fertiges.
- Hochrechnung: gemessene Laptop-Zeiten (ein Kern) mal Zahl der Durchlaeufe. Die .69-CPU kann langsamer sein, daher
  bleibt der Waechter (--budget 540).

| Nr | Spur | Kurzname | Argumente nach resonanz3d.py | Hochrechnung |
|---|---|---|---|---|
| 1 | cpu | r6rauch | `rauch --geraet cpu --out aus-rauch` | 25 bis 40 s |
| 2 | cpu | r6pol07 | `pole --geraet cpu --omega2 0.7 --out aus-pole-07` | 5 bis 7 min |
| 3 | cpu2 | r6bruecke | `bruecke --geraet cpu --omega2 0.7 --l 0 --h 0.02,0.01,0.005 --ciurla --out aus-bruecke` | 4 bis 6 min |
| 4 | cpu | r6lin07a | `zeitlin --geraet cpu --omega2 0.7 --l 2,0 --T 1000 --dr 0.05,0.025 --out aus-lin07a` | ~1,5 min |
| 5 | cpu2 | r6nl07a | `zeit0 --geraet cpu --omega2 0.7 --eta 0,0.001,0.01 --T 800 --dr 0.05,0.025 --out aus-nl07a` | ~1,5 min |
| 6 | cpu | r6lin07b | `zeitlin --geraet cpu --omega2 0.7 --l 2,0 --T 1000 --dr 0.0125 --out aus-lin07b` | ~4 min |
| 7 | cpu2 | r6nl07b | `zeit0 --geraet cpu --omega2 0.7 --eta 0,0.001,0.01 --T 800 --dr 0.0125 --out aus-nl07b` | ~4,5 min |
| 8 | cpu | r6pol06 | `pole --geraet cpu --omega2 0.6 --out aus-pole-06` | 5 bis 7 min |
| 9 | cpu2 | r6pol08 | `pole --geraet cpu --omega2 0.8 --out aus-pole-08` | 6 bis 8 min |
| 10 | cpu | r6dw1 | `pole --geraet cpu --omega2 0.52,0.53 --l 2 --bereich gebunden --h 0.04,0.02,0.01 --out aus-duenn-a` | ~4 min |
| 11 | cpu2 | r6dw2 | `pole --geraet cpu --omega2 0.54,0.55 --l 2 --bereich gebunden --h 0.04,0.02,0.01 --out aus-duenn-b` | ~4 min |
| 12 | cpu | r6tr55 | `zeitlin --geraet cpu --omega2 0.55 --l 2 --T 2000 --dr 0.1,0.05,0.025 --rmax 160 --rsd 100 --mess 0.5 --out aus-tropfen-055` | ~1,5 min |
| 13 | cpu2 | r6tr52 | `zeitlin --geraet cpu --omega2 0.52 --l 2 --T 4000 --dr 0.1,0.05,0.025 --rmax 190 --rsd 120 --mess 0.5 --out aus-tropfen-052` | ~3,5 min |

- Reihenfolge nach Vorrang: 1, dann 2 und 3 parallel (cpu/cpu2). Danach 4/5, 6/7, 8/9, 10/11, 12/13.
- Zusammen etwa 50 min Rechenzeit, auf zwei Spuren etwa 25 min Wandzeit.
- Optional: zeitlin fuer 0,53 und 0,54 wie Nr. 12 mit --T 3000.
- --geraet cuda auf p4000a geht auch; es lohnt nur bei grossen Stapeln (Kontur, feine Zeitgitter).

**Gemessene lokale Zeiten** (Laptop, ein Thread, nice 19, 30.09.):
- Rauchtest: 23,1 s (rc = 0, Ende 02:55:51); nach der letzten Code-Aenderung erneut 23,7 s (rc = 0, 02:58:16 bis 02:58:42). Ausgaben in lauf-lokal/.
- Profil omega^2 = 0,7 mit h/2 = 0,005: 13,5 s.
- Profil 0,52 mit h/2 = 0,01: 12,7 s; S(0) = 1,019434 = RUNDE-02.
- Determinanten-Durchlauf bei K = 3399 Schritten: 1,56 s (9 Werte), 1,77 s (300), 3,12 s (2100).
- Zeitschritt zeit0 bei N = 4000 x 3 Reihen: 0,47 ms; zeitlin bei N = 4000 x 2: 0,34 ms.

**Hochrechnung pole 0,7:**
- Profile: 7 + 13,5 + 27 s.
- Stufe B: etwa 60 Durchlaeufe zu 1,6 bis 3,1 s, also ~130 s.
- Stufen A und C: ~20 + 80 s.
- Zusammen ~4,7 min.

## 7. Grenzen und Risiken

- **Schwellennaehe:** Pole innerhalb 0,002 ueber 1 - omega oder 0,0005 unter der Kante werden nicht gesucht. Liegt die
  l = 2-Formschwingung bei 0,7 genau dort (V2), meldet der Lauf "gebunden: 0". Dann zeigt zeitlin die Frequenz.
- **Gebundene Zustaende:** Nur Vorzeichenwechsel auf 300 Punkten. Zwei sehr nahe Nullstellen koennen fehlen. Die
  Doppelnullstelle bei rho = 0 ist ausgenommen (eigene Probe V1).
- **Breite Pole mit Im < -0,1** liegen ausserhalb des Kastens. Newton kann sie melden, die Zaehlung nicht.
- **Bruecke:** Fuer nicht ganzzahliges nu ist die Jost-Randbedingung die asymptotische Hankel-Reihe (bei R ~ 35 sehr
  genau). Scheitert Newton, wird der dim-Schritt bis zu 6-mal halbiert; sonst endet die Spur (Vermerk im Bericht).
- **zeit0:** Der Stoss aendert Q, also den Hintergrund. Die spaete Frequenz ist deshalb nicht exakt der lineare Pol;
  darum laufen zwei Staerken mit. Die "Ladungsdrift" ist nur fuer zeit0 aussagekraeftig.
- **Zeitfenster:** Bei Gamma ~ 1e-4 und Fenster 400 aendert sich die Amplitude um 4 %. Die Abklingrate ist dann nur
  grob (L3 regelt das).
- Codex rechnet parallel. Kein Austausch vor dem Abgleich (G8).

## 8. Einfach gesagt

In einer Linie gerechnet hatte der Q-Ball eine Art eingesperrte Schwingung, die nur sehr langsam nach aussen leckt.
Jetzt pruefen wir, ob es sie auch in einer echten Kugel gibt. Wir rechnen getrennt, ob die Kugel gleichmaessig atmet
(l = 0), hin und her wackelt (l = 1) oder sich wie ein Wassertropfen zur Zigarre verformt (l = 2). Meine Vorhersage:
Die eingesperrte Schwingung gibt es auch in 3D, aber sie liegt etwas hoeher und leckt deutlich schneller aus. Die
Tropfen-Schwingung grosser Baelle sollte der alten Formel fuer Wassertropfen folgen, die Rayleigh vor fast 150 Jahren
aufgeschrieben hat.

## Abgabe

- resonanz3d.py SHA-256 99c54b9ccdb517c1a033669cd664586e642f59fc58f82fd6df8f0d83b7b5bcb0 (Stand des letzten Rauchtests).
- Ende 2026-09-30 02:58:47 CEST (gemessen).
