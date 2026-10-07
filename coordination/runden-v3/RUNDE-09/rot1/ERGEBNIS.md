# ROT-1 (Runde 9): Wirbel mit gefuelltem Kern, Waende der relativen Phase, Paar mit Waenden

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5) fuer die Leitung claude-primary. Explorativ (v3), keine formale Bestaetigung.
- Zeitkette (date, CEST; die .69 loggt in UTC = CEST - 2 h):
  - Beginn 07:45:40; PLAN.md mit Vorab-Tabelle V1 bis V20 07:57:31 bis 07:58:49 (Kopie PLAN.md.eingefroren-20260930-0758)
  - lokale Rauchtests 08:07:50 bis 08:21:37 (CPU, 1 Thread, nice 19, timeout 120, Ausgaben lauf-lokal/)
  - Nachtrag mit Codeaenderungen und Vorab V21 bis V25 um 08:22:33 (Kopie -0822), vor jedem Messlauf ausser dem
    GPU-Rauchtest
  - .69: GPU-Rauchtest 08:16:36 bis 08:19:19; Messlaeufe LAUF1 bis LAUF9 von 08:18:53 bis 08:42:02, alle rc = 0
  - Pause (Nutzungslimit der Leitung) etwa 08:37 bis 09:51; Auswertung ab 09:55:43, dieser Text ab 09:59:19
- Belegstufen: **[Hand]** Herleitung, **[num]** numerisch, eine Gitterstufe, **[num+K]** numerisch mit Kontrolle (zweite
  Gitterstufe im Feinfenster, zweites Verfahren oder exakte Symmetrieprobe), **[Bild]** aus den PNG gelesen, **[H]**
  Hypothese, **[nachtr.]** Abschaetzung erst nach dem Ergebnis.
- Quellen: lauf-69/ausgabe/*.json (Feldpfade in eckigen Klammern), Berichte *_bericht.txt, Logs lauf-69/LAUF*.log.
  Code rot1.py (Stand auf der .69 = lokal, sha256 c29e7794...); fruehere Laeufe nutzten Vorstaende mit gleicher Physik
  (Abschnitt 9).
- **Feinfenster:** dyn0 fein bis T = 600 (grob 1500), dyng fein bis T = 400 (grob 1000), paar und paardyn nur grob.
  Aussagen jenseits t = 600 bzw. 400 und alle Paarzahlen sind eine Gitterstufe.

## 0. Ergebnis in fuenf Punkten

1. **g = 0: Der Wirbel mit gefuelltem Kern existiert, ist gebunden und stabiler als der einkomponentige Wirbel.**
   - Existenz: 12 von 12 (Q, q_2), Residuum <= 8,7e-13 [num+K: K1, K5, Virial].
   - Bindung: 2,5 bis 11,0 Energieeinheiten unter "Wirbel mit Q_1 plus getrennter Ball mit Q_2" (gleiches Q, gleiches J).
   - Dynamik: Bei Q = 139 teilt sich der einkomponentige Wirbel bei t = 1085, der gefuellte (q_2 = 0,25) bis 1500 nicht
     [num]. Bei Q = 94 und 110 teilen sich beide mit l = 2; die Rate faellt mit der Fuellung monoton (0,063 / 0,049 /
     0,035 / 0,027 bei q_2 = 0 / 0,1 / 0,25 / 0,4) [num; L3 fuer q_2 = 0 und 0,25 bis t = 600].
   - Der Kern hat die kleinere Frequenz (omega_2 < omega_1 in 12 von 12). Das Muster dreht mit
     Omega = omega_1 - omega_2 = 0,0785 (Q = 199) [num].
2. **g != 0: Es entstehen genau die zwei vorhergesagten pi-Waende, Ising-artig; der Wirbel ueberlebt sie aber nicht.**
   - Waende bilden sich zwischen t = 15 (g = 0,5) bzw. 25 (g = 0,2) und 55 (Rampe bis 50). An der Wand verschwindet
     die schwaechere Komponente
     (Rest 0,02 bis 0,03 bei g = 0,5).
   - Steilheit: sqrt(|g| S) bei g = 0,5; sqrt(2 |g| S) bei g = 0,2 [num+K fuer 0,5].
   - Die Musterdrehung rastet ein: Omega faellt von 0,078 auf 0 bis t = 35 (g = 0,5) bzw. 60 (g = 0,2). Q_1/Q faellt
     dabei von 0,75 auf 0,22 bis 0,26.
   - Danach: bei g = 0,5 schneiden die Waende den Ball in zwei Haelften (psi_1 = +psi_2 und psi_1 = -psi_2), Teilung bei
     t = 75 [num+K]. Bei g = 0,2 wird der Wirbel bei t = 65 ausgestossen, J/Q faellt bis t = 1000 von 0,75 auf 0,11 [num].
3. **Zwei Wirbel (psi_1 bei A, psi_2 bei B) sind durch einen Strang verbunden; die Kraft haengt nicht vom Abstand ab.**
   - Statisch, geklammert: E(d) steigt linear. Steigung 0,97 (g = 0,5) bzw. 0,61 (g = 0,2), Fitrest 0,04 bzw. 0,08
     [num, K4 exakt].
   - Frei, zeitlich entwickelt: Das Paar kreist mit Omega d = 0,65 bis 0,77 bei mittleren Abstaenden 2,6 bis 7,4.
     Daraus folgt die Kraft F = pi rho_a Omega d = 1,48 bis 1,77, Wandformel 2 sigma_Pol = 1,75 [num].
   - Zwei Strangformen: frei eine Linse aus zwei Ising-Waenden, geklammert (g = 0,5) ein leerer Schlitz [Bild]. Das ist
     ein lineares Potential im Sinn der Vortex-Molekuele [H, Analogie], kein QCD-Einschluss.
4. **Frage 3 (oszillierende Selbststabilisierung, stille Stellen): nicht gerechnet.**
   - Bei g = 0 dreht der stabile gefuellte Wirbel mit zwei Frequenzen. Der Anteil der Drehung an der Stabilitaet ist vom
     Kerneffekt nicht getrennt.
   - Bei g != 0 bremst die Kopplung die Drehung ab, statt sie zu halten.
5. **Vorab gegen Ausgang:** 14 getroffen, 3 teilweise, 8 verfehlt (Abschnitt 5).
   - Verfehlt u. a.: Kernaustritt als Zerfallsart; Wandschaerfe-Schwellen F90 >= 0,6 und r k_eff >= 2; stetiges
     Mitdrehen bei g != 0; Omega-Verhaeltnis zwischen g = 0,2 und 0,5.
   - Kontrollen: K1 (RING-T zweimal reproduziert), K4 (<= 1e-11) und L3 (Feinfenster) bestanden. Ladung und Energie
     bilanzieren bis 1 % geschluckter Ladung unter 1e-3 (J 2,6e-3), ueber den ganzen Lauf nicht (Quadraturfehler).

## 1. Frage 1: g = 0, gefuellter Wirbel

### 1.1 Existenz und Form [num+K]

- Radialer Gradientenfluss bei festen Q_1 (m = 1) und Q_2 (m = 0), h = 0,05 bis R = 40, 18 000 Iterationen
  [radial_ergebnis.json: loesungen[].residuum].
  - Residuum <= 8,7e-13 fuer alle gefuellten Wirbel.
  - Hoechstens 4,9e-11 unter allen 49 Loesungen; das ist der zerstreute Einzelball Q_2 = 11,0.
- Form (radial_profile.png, [Bild]):
  - q_2 = 0,25 und 0,4: |psi_2|^2 ist bei r = 0 maximal (S_0 = 0,42 bis 0,85) und reicht in den Ring von |psi_1|^2 hinein
    [loesungen[fc_*].S_0, R_kern_h].
  - q_2 = 0,1: |psi_2|^2 ist ein duenner Ring auf der Innenflanke von |psi_1|^2 (Maximum bei r ~ 2 bis 2,5, S_0 = 0,07 bis
    0,13), also kein gefuellter Kern. Das trifft V1 nur teilweise.
- Frequenzen: omega_2^2 = 0,474 bis 0,515 (auch unter 1/2, der Kern ist im Ring tiefer gebunden als ein freier Ball),
  omega_1^2 = 0,581 bis 0,688. Omega = omega_1 - omega_2 = 0,065 bis 0,125 [loesungen[fc_*].omega1, omega2].
- Kontrollen:
  - K1: einkomponentig gegen die RING-Schiesstabelle; omega^2 gleich, E auf <= 6,2e-6 relativ (Q = 93,86 / 110,17 /
    138,76 / 199,35) [K1].
  - Virial V = sum omega_a^2 N_a: Rest <= 1,1e-5 fuer gebundene Loesungen [loesungen[].virialrest]. Die zwei zerstreuten
    Einzelbaelle mit Q_2 = 9,4 und 11,0 haben 2,8e-4 bzw. 6,2e-4 (Zerlaufen bis zum Rand).
  - K5: dE/dQ_1 = 0,805210 gegen omega_1 = 0,805209; dE/dQ_2 = 0,690079 gegen omega_2 = 0,690073 [K5].

### 1.2 Energie bei gleichem Q und gleichem J = Q_1 [num+K]

- E_sep = E_v1(Q_1) + E_b(Q_2); ein Einzelball unter seiner Existenzgrenze zaehlt als zerstreut mit E = Q_2
  [vergleich[].E_sep, bindung, reihenfolge].

| Q (einkomp. omega^2) | q_2 | E_fc | E_sep | Bindung | E_v1(Q), J = Q | E_b(Q), J = 0 |
|---|---|---|---|---|---|---|
| 93,86 (0,65) | 0,10 / 0,25 / 0,40 | 86,94 / 85,42 / 83,64 | 89,47 / 90,53 / 89,64 | 2,53 / 5,11 / 6,00 | 87,71 | 77,46 |
| 110,17 (0,625) | 0,10 / 0,25 / 0,40 | 99,86 / 98,17 / 96,27 | 102,98 / 104,14 / 103,54 | 3,12 / 5,97 / 7,27 | 100,73 | 89,87 |
| 138,76 (0,60) | 0,10 / 0,25 / 0,40 | 122,10 / 120,17 / 118,13 | 126,08 / 127,27 / 126,97 | 3,98 / 7,11 / 8,83 | 123,07 | 111,46 |
| 199,35 (0,575) | 0,10 / 0,25 / 0,40 | 168,30 / 166,00 / 163,79 | 173,48 / 174,82 / 174,81 | 5,18 / 8,82 / 11,01 | 169,45 | 156,82 |

- Die Reihenfolge E_b(Q) < E_fc < E_v1(Q) gilt in 12 von 12 Faellen [vergleich[].reihenfolge].
- Die Bindung waechst mit Q und mit q_2 [Tabelle].
- Deutung [H]: Der Kern ersetzt eine zweite Oberflaeche. Die getrennte Anordnung hat zwei Raender, der gefuellte Wirbel
  einen.

### 1.3 Zeitentwicklung mit Saat 0,01 (Stoerfaktor wie RING-T), T = 1500

| Lauf | Q | J/Q | Teilung t | l_dom | gamma(l = 2) | Quelle |
|---|---|---|---|---|---|---|
| einkomponentig | 93,86 | 1 | 50 | 2 | 0,0926 (RING-T: 50 / 0,0925) | dyn0_grob_v1_Q94+...json |
| gefuellt q_2 = 0,25 | 93,86 | 0,75 | 105 | 2 | 0,0574 | ebenda |
| einkomponentig | 110,17 | 1 | 75 | 2 | 0,0631 (RING-T: 75 / 0,0641) | dyn0_grob_teil_ergebnis.json |
| gefuellt q_2 = 0,10 | 110,17 | 0,90 | 100 | 2 | 0,0488 | ebenda |
| gefuellt q_2 = 0,25 | 110,17 | 0,75 | 160 | 2 | 0,0350 | ebenda |
| gefuellt q_2 = 0,40 | 110,17 | 0,60 | 230 | 2 | 0,0274 | ebenda |
| einkomponentig, gleiches J wie q_2 = 0,25 | 82,63 | 1 | 40 | 2 | 0,1138 | ebenda |
| einkomponentig | 138,76 | 1 | 1085 | 2 | 0,0019 (RING-T 0,60: 1045 / 0,0041) | dyn0_grob_v1_Q94+...json |
| gefuellt q_2 = 0,25 | 138,76 | 0,75 | keine bis 1500 | - | A_l <= 0,006 (Saatniveau) | ebenda |
| gefuellt q_2 = 0,25 | 199,35 | 0,75 | keine bis 1000 | - | Wirbel zentral 100 % | dyng_grob_ergebnis.json, Q199_g0 |

- Feldpfade: laeufe[].t_teilung, l_dom, raten["2"].gamma.
- L3 im Feinfenster (T = 600) [num+K]:
  - einkomponentig Q = 110,17: Teilung 75 / 75, gamma 0,0631 / 0,0631
  - gefuellt q_2 = 0,25: 160 / 160, gamma 0,0350 / 0,0346 [dyn0_fein_ergebnis.json]
- Stabilitaet bei Q = 139 und 199 bis t = 1500 bzw. 1000 ist nur grob gerechnet [num].
- **Zerfallsart:** In allen zerfallenden gefuellten Laeufen teilt sich der Ring mit l = 2.
  - Die Schwerpunkte von S_1 und S_2 trennen sich erst danach um mehr als 1 (t = 146 / 202 / 314 gegen Teilung
    100 / 160 / 230) [t_d12_gt1].
  - Der Kern rutscht also nicht zuerst heraus (V9 verfehlt).
- Musterdrehung bei g = 0 (Q = 199): d arg P/dt = 0,07845 gegen omega_1 - omega_2 = 0,07835 (t = 60 bis 1000, drei
  Fenster gleich) [dyng_grob_ergebnis.json: laeufe[Q199_g0].drehung[].Omega_P].
  - Das ist die kinematische Identitaet fuer ein starr drehendes Muster; ROT-3 G1 ist damit bestaetigt (Abschnitt 4).

## 2. Frage 2: g != 0

Aufbau: gefuellter Wirbel Q = 199,35, q_2 = 0,25 (bei g = 0 stabil, 1.3), g linear eingeschaltet von t = 0 bis 50.
Kreise um den S^2-Schwerpunkt, r = 2,5 / 3,5 / 4,5, alle 5 Zeiteinheiten [nach_waende_ergebnis.json,
"dyng_grob_roh.pt:<Lauf>"[t]."r3.5"]. Masse: F90 (Anteil des Kreises mit \|n_e\| >= 0,9 max; gleichmaessig 0,287),
r k_eff (Steilheit an den Vorzeichenwechseln; gleichmaessig 1), Minderheit an der Wand relativ zu ihrem Kreismittel.

### 2.1 Wandbildung [num+K fuer g = 0,5; num fuer g = 0,2]

| g | gleichmaessig bis | staerkste Schaerfung | k_eff gegen sqrt(\|g\|S) / sqrt(2\|g\|S) | Minderheit an der Wand |
|---|---|---|---|---|
| +0,2 | t ~ 20 (F90 0,27 bis 0,33, r k 0,98 bis 1,16) | t = 50/55: r k 2,09 (r 4,5), 1,95 (r 3,5); F90 0,59 (r 4,5) | r 3,5, t = 50/55: 0,509/0,557 gegen 0,372/0,366 (Pol) und 0,526/0,517 (Aequator), also 0,97 bis 1,08 x Aequator | r 3,5: 0,85 (t = 50), 0,61 (55), 0,28 (60), 0,00 (65) |
| +0,5 | t ~ 10 | t = 35: r k 1,66 (r 3,5); F90 0,52 (r 4,5) | r 3,5, t = 30/35: 0,436/0,473 gegen 0,565/0,506 (Pol), also 0,77 bis 0,93 x Pol; r 2,5, t = 35: 0,583 gegen 0,590 (Pol) | r 2,5: 0,45 (t = 30), 0,24 (35), 0,02 (40); r 3,5: 0,70, 0,37, 0,03 |

- Zahl der Waende: zwei, radial gegenueber, als zwei Domaenen der relativen Phase (Delta ~ 0 und Delta ~ pi).
  - Belegt durch Bilder bei t = 50: dyng_grob_Q199_g+0.2.png, dyng_grob_Q199_g+0.5.png [Bild]. n_z/S ist in den
    Wandflecken +-1.
  - Die Zahl der Vorzeichenwechsel von n_e (immer 2) unterscheidet nicht zwischen Waenden und gleichmaessiger Windung;
    das war in V10 schlecht gewaehlt.
- **Wandtyp: Ising-artig** (die schwaechere Komponente verschwindet an der Wand), wie ROT-3 W1.1 und V1 vorhersagen.
  - Bei g = 0,5 zuerst mit Minderheit 0,24, dann 0,02; bei g = 0,2 spaeter (0,28 bei t = 60).
- Breite: Bei g = 0,5 passt die Pol-Formel sqrt(\|g\| S) auf 1 bis 23 %, bei g = 0,2 die Aequator-Formel sqrt(2\|g\| S)
  auf 3 bis 8 %.
  - k_eff ist eine grobe Steilheit (unnormiertes n_e, Mittel ueber zwei Wechsel). Der Unterschied zwischen 0,2 und 0,5
    ist nicht weiter geprueft [num].
- L3 [num+K]: g = +0,5 fein gegen grob bis t = 80 auf drei Stellen gleich. Beispiele: t = 35, r 3,5: r k 1,66 / 1,66,
  Minderheit 0,37 / 0,37; t = 50: Q_1/Q 0,518 / 0,518 [nach_waende: "dyng_fein_roh.pt:Q199_g+0.5"].
- K4 [num+K]: g = +0,5 und -0,5 ohne Saat. Die Dichten stimmen nach 90-Grad-Drehung auf 9,7e-12 (+90) bzw. 6,5e-12
  (-90) ueberein, die Reihen Q_1 und E auf 3e-13 [dyng_grob_ergebnis.json: K4]. Beide Drehsinne passen wegen der
  C2-Symmetrie des ungestoerten Starts.

### 2.2 Drehung: Einrasten statt Mitdrehen [num+K fuer 0,5]

- d arg P/dt (Musterdrehung) und Q_1/Q [nach_waende: Omega_P, Q1_Q]:
  - g = +0,2: 0,0784 (t = 0), 0,0405 (50), 0,0007 (60), danach -0,006 bis +0,05; Q_1/Q von 0,75 auf 0,22 (t = 60)
  - g = +0,5: 0,0784 (0), 0,0552 (30), -0,004 (35), -0,034 (40), danach Pendeln um 0 mit bis zu +-0,06; Q_1/Q von 0,75
    auf 0,25 (t = 40), dann 0,36 bis 0,57
- Die Kopplung setzt Ladung von psi_1 in psi_2 um, bis die Frequenzen gleich sind; dann steht das Muster.
  - Fenstermittel t = 200 bis 400: omega_1 - omega_2 = -0,0005 (g = 0,2) bzw. +0,0004 (g = 0,5)
    [dyng_grob_ergebnis.json: laeufe[].drehung[].omega1_minus_omega2].
  - Ein stetig mitdrehendes Wandmuster (ROT-3 G1-Fortsetzung, V14) gab es bei diesem Ball und dieser Rampe nicht.

### 2.3 Schicksal bis T = 1000 [num; bis t = 400 num+K fuer g = 0,5]

| Lauf | Teilung t | Wirbel verlaesst Zentrum t | J/Q (Fenster) t = 1000 | Q geschluckt | Quelle laeufe[] |
|---|---|---|---|---|---|
| Q199, g = 0 | keine | nie | 0,750 | 1,3e-4 | Q199_g0 |
| Q199, g = +-0,2 | keine | 65 | 0,107 / 0,137 | 0,117 / 0,112 | Q199_g+-0.2 |
| Q199, g = +-0,5 (mit und ohne Saat) | 75 | 80 | ~0 | 0,77 | Q199_g+-0.5(_ohne) |
| Q110, g = +0,2 | keine | 110 | 0,025 | 0,185 | Q110_g+0.2 |
| Q110, g = +0,5 | 95 | 70 | 0,021 | 0,229 | Q110_g+0.5 |

- Feldpfade: t_teilung, t_wirbel_weg, t1000.J_Q, bilanz.Q_geschluckt_rel.
- g = 0,5: Die Teilung kommt mit und ohne Saat zur selben Zeit (75). Die Rampe selbst treibt die l = 2-Verformung;
  die cos(2 phi)-Kraft ist eine l = 2-Stoerung [Hand].
- g = 0,2 (Q = 199): Es bleibt ein gemischter Ball ohne zentralen Wirbel. Der Drehimpuls geht mit der geschluckten
  Ladung (12 %) und der Randstrahlung hinaus. Bei Q = 110 werden am Ende 92 bis 98 % der Fensterladung zu psi_2
  (Q_1/Q 0,02 bis 0,08 ab t = 250) [dyng_grob_bericht.txt].
- Mit V15: Die Hauptoption "zerfaellt frueher als bei g = 0" trat ein.

### 2.4 Zwei Wirbel: psi_1-Wirbel bei A = (-d/2, 0), psi_2-Wirbel bei B = (+d/2, 0), grosser gemischter Ball Q = 700

**Statisch** (Gradientenfluss, Q_1 = Q_2 = Q/2 fest, Phasenklammer auf 0,5 < r < 2 um A und B; paar_ergebnis.json) [num, K4]:

| g | E_g(d) - E_g(5) bei d = 5 / 6,5 / 8 / 9,5 | Steigung, Fitrest | Steigung mit Abzug E_0(d) | 2 sigma_Pol / 2 sigma_Aequator |
|---|---|---|---|---|
| 0,5 | 0 / 1,521 / 2,991 / 4,374 | 0,973, 0,040 | 1,872 (Fitrest 0,31) | 1,749 / 2,474 |
| 0,2 | 0 / 0,759 / 1,693 / 2,751 | 0,613, 0,083 | 1,512 (Fitrest 0,20) | 1,000 / 1,415 |

- Feldpfade: auswertung["g"].steigung_direkt, fitrest_direkt, steigung_minus_E0, 2sigma_pol, 2sigma_aequator.
- Kein Vorzeichenwechsel von n_e auf dem Kreis um beide Wirbel, bei allen g > 0 und d [konf[].kreis_um_beide.wechsel].
  Der Strang laeuft also von A nach B, nicht zum Rand.
- Strangform [Bild, paar_felder.png]:
  - bei g = 0,5 (alle d) und g = 0,2, d = 5 ein **leerer Schlitz** zwischen A und B: beide Komponenten verschwinden
  - bei g = 0,2, d >= 6,5 eine Linse Delta ~ pi zwischen zwei Waenden; die Waende kreuzen die Mittelsenkrechte bei
    y = +-2,1 bis +-2,7 [konf[].ne_Mittelsenkrechte_Wechsel_y]
- [nachtr., Duennwandnaeherung, Hand] Ein Schlitz kostet zwei Ballraender, 2 sigma_Rand ~ 0,9 je Laenge bei g = 0,5.
  Das liegt nahe an der Steigung 0,97 und unter zwei Ising-Waenden (1,75). Das erklaert die kleinere statische Steigung,
  ist aber eine Deutung nach dem Ergebnis.
- E_0(d) bei g = 0 ist keine saubere Lagereferenz:
  - Ohne Kopplung raeumt psi_1 den Bereich um A (S_1 im Klammerring 0,025 bis 0,064), und die Windungsprobe um A ist
    dort nicht auswertbar.
  - E_0 faellt von 533,66 (d = 5) auf 529,58 (d = 9,5).
- K4: E(g = -0,5, psi_2 -> i psi_2) = E(g = +0,5) auf 1,1e-13.
- Konvergenz: max \|Delta E\| ueber die letzten 1000 Iterationen 1,2e-5.
- Windungsprobe um A (Kreis r = 2,4) bei g = 0,5, d = 9,5: 0. Ob ein Phasenschlupf vorliegt oder die Probe die Wand mit
  psi_1 = 0 schneidet, ist nicht geklaert. Der Punkt liegt auf der Geraden.

**Frei zeitlich entwickelt** (keine Klammer, g von Anfang an, T = 250; paardyn_grob_ergebnis.json) [num]:
- Eine Kraft F wird zu einer Kreisbewegung des Paars [Hand, Magnus-Kraft 2 pi rho_a v je Wirbel]:
  Omega = F/(pi rho_a d) mit rho_a = omega S_0.

| g | d_0 | mittleres d (t >= 30) | Omega | Omega d | Omega d^2 | F = pi rho_a Omega d | F / 2 sigma_Pol |
|---|---|---|---|---|---|---|---|
| 0,5 | 3 / 5 / 7 / 9 | 2,58 / 5,15 / 6,29 / 7,39 | -0,256 / -0,125 / -0,115 / -0,104 | 0,660 / 0,645 / 0,722 / 0,772 (Betrag) | 1,70 / 3,33 / 4,54 / 5,71 | 1,51 / 1,48 / 1,65 / 1,77 | 0,86 / 0,84 / 0,94 / 1,01 |
| 0,2 | 3 / 5 / 7 | 2,29 / 5,22 / 7,14 | -0,105 / -0,028 / -0,026 | 0,240 / 0,144 / 0,183 | 0,55 / 0,75 / 1,30 | 0,56 / 0,34 / 0,43 | 0,56 / 0,34 / 0,43 |
| 0 | 3 / 5 / 7 / 9 | 1,68 / 4,10 / 5,52 / 6,27 | +0,027 / +0,046 / +0,040 / +0,033 | - | - | - | - |

- Feldpfade: laeufe[].d_mittel, Omega, F_magnus, 2sigma_pol, fehlt_anteil.
- g = 0,5: Omega d bleibt ueber d = 2,6 bis 7,4 auf +-10 % gleich; Omega d^2 waechst um den Faktor 3,4. Die Kraft haengt
  nicht vom Abstand ab, das Potential waechst also linear.
- Die Groesse passt zu zwei Ising-Waenden (0,84 bis 1,01 x 2 sigma_Pol).
- Strangform frei [Bild, paardyn_grob_g0.5_d7.png]: eine drehende Linse Delta ~ pi, begrenzt von zwei Waenden. An der
  einen verschwindet psi_1, an der anderen psi_2. Kein leerer Schlitz.
- Vorbehalte:
  - Die Paare naehern sich langsam (d-Drift -0,6 bis -1,5 je 100); einzelne Lagen sind Fehlzuordnungen (Sprung auf d = 12
    bei t = 25).
  - Bei g = 0 kreist das Paar entgegengesetzt mit +0,03 bis +0,05 (Lage im Ball). Zieht man das ab, wird
    F/2 sigma_Pol = 0,95 bis 1,33 (g = 0,5) bzw. 0,71 bis 1,10 (g = 0,2).
  - g = 0,2, d_0 = 9: 53 % der Analysen ohne Wirbelpaar, nicht gewertet.
  - Die Rechnung hat nur eine Gitterstufe und keine g <-> -g-Probe.

## 3. Frage 3: oszillierende Selbststabilisierung

- Nicht gerechnet (PLAN 3: nur wenn Zeit bleibt). Die stillen Stellen der beta_eff-Leiter sind 3D-Werte; eine 2D-Leiter
  gibt es nicht.
- Was die Laeufe dazu sagen [num]:
  - Bei g = 0 ist der stabile gefuellte Wirbel (Q = 139, 199) ein drehendes Zwei-Frequenz-Muster. Ob die Drehung oder die
    Fuellung stabilisiert, trennen die Laeufe nicht.
  - Bei g != 0 bremst die Kopplung die Drehung (2.2). Eine selbsterhaltende Drehung des Wandmusters wurde nicht gesehen.
- ROT-3 V5 (Pendeln zwischen Ring- und Zwillingsform) wurde nicht gesucht. Bei g = 0,5 pendelt Q_1/Q nach dem Einrasten
  zwischen 0,36 und 0,57 (t = 45 bis 100), vermutlich im zerfallenden Ball [num, H].

## 4. Bezug zu ROT-3 (PAPIER-ROT3.md, Test T1)

| T1-Messgroesse | ROT-3-Vorab [H] | ROT-1-Ausgang |
|---|---|---|
| Musterdrehzahl Omega_pat, G1 | bei g = 0 zwei Frequenzen, Muster dreht mit omega_1 - omega_2 | bestaetigt: 0,07845 gegen 0,07835 (0,13 %); omega_2 < omega_1 in 12 von 12 radialen Loesungen [num] |
| stetige Fortsetzung bei g != 0 | mitdrehendes Muster, Omega_pat = omega_1 - omega_2 +- 10 % (Texturregime) | bei g = 0,2 und 0,5 nicht: Einrasten auf 0 bis t = 35 bzw. 60 durch Ladungsumsatz. Kleine g (0,02; 0,05) nicht gerechnet, der Texturast bleibt offen |
| Wandkontrast P2 | P2 > 0,5 mit Plateaus bei R/delta >= 3, g = 0,5 | P2 normiert nicht aufgezeichnet. Zaehler Cw steigt von ~0 auf +24 (g = 0,5, t = 50). Plateaus nur teilweise (F90 hoechstens 0,52 bzw. 0,59, gleichmaessig 0,287) |
| n_z/S in der Stufenmitte | Ising: \|n_z\|/S > 0,8; Phasenwand: < 0,3 | Ising: Minderheit an der Wand 0,02 bis 0,03 ihres Mittels (g = 0,5), 0,00 bis 0,28 (g = 0,2, t >= 60); n_z/S = +-1 in den Wandflecken [Bild]; n_z/S selbst nicht aufgezeichnet |
| J/Q, Q_1/Q | J/Q erhalten, Q_1/Q nicht | J/Q (Fenster) 0,75 +- 0,005 bis t = 50 bei Q = 199, danach faellt es mit dem Zerfall; Q_1/Q 0,75 -> 0,22 bis 0,26 |
| Abstrahlung bei 2 omega_1 - omega_2 > 1 | erst oberhalb | hier 0,85 (Q = 199) und 0,92 (Q = 110), also darunter; Fluss nicht gemessen |

- Kurz: G1 und der Ising-Wandtyp sind bestaetigt [num+K]. Die "Familie" (a) bis (c) mit stetigem Mitdrehen ist bei
  g >= 0,2 nicht gesehen: der gefuellte Wirbel rastet ein und zerfaellt. Der Texturast bei kleinem g ist offen.

## 5. Vorab gegen Ausgang (Vorab: PLAN.md 4 und 8)

| Nr. | Vorab (kurz) | Ausgang | Bewertung |
|---|---|---|---|
| V1 | Existenz, h maximal bei r = 0, Residuum < 1e-8, alle 12 | existiert 12/12, Residuum <= 8,7e-13; bei q_2 = 0,1 ist h ein Ring (4/12) | teilweise |
| V2 | omega_2 < omega_1; Omega 0,01 bis 0,08 (Q = 110, q_2 = 0,25) | 12/12; Omega = 0,115 | teilweise |
| V3 | Bindung > 0 alle; E_fc = 96 +- 3, Bindung 8 +- 4 | 12/12; 98,17 und 5,97 | getroffen |
| V4 | E_b < E_fc < E_v1 | 12/12 | getroffen |
| V5 | K1 auf 1e-3, Virial < 1e-4 | <= 6,2e-6 und <= 1,1e-5 | getroffen |
| V6 | einkomp. Q = 110: l = 2, gamma 0,055 bis 0,075 | l = 2, 0,0631, t = 75 | getroffen |
| V7 | gefuellt lebt laenger als einkomp. gleichen Q | gamma 0,0350 gegen 0,0631; 160 gegen 75 | getroffen |
| V8 | laenger als einkomp. gleichen J | 160 gegen 40 | getroffen |
| V9 | Kern rutscht zuerst heraus (l = 1) | l = 2 zuerst, Schwerpunkte trennen sich danach | verfehlt |
| V10 | g = 0,5: zwei Waende mit F90 >= 0,6, r k >= 2 | zwei Ising-Waende sichtbar, aber F90 max 0,52, r k max 1,66, Zerfall bei 75 | verfehlt (Schwellen) |
| V11 | g = 0,2 ebenso, F90 kleiner als bei 0,5 | F90 max 0,59 (groesser als bei 0,5), r k 2,09 | verfehlt |
| V12 | k zwischen 0,7 sqrt(\|g\|S) und 1,3 sqrt(2\|g\|S) | 0,77 bis 0,99 x Pol (0,5); 0,97 bis 1,08 x Aequator (0,2) | getroffen |
| V13 | Ising: Minderheit an der Wand < 1/2 | 0,02 bis 0,24 (0,5); 0,28 und weniger ab t = 60 (0,2) | getroffen |
| V14 | Muster dreht mit omega_1 - omega_2 +- 30 %, kein Einrasten bis T | Einrasten bei t = 35 bzw. 60 | verfehlt |
| V15 | Schicksal: frueher Zerfall 0,45 / gebunden drehend 0,4 / Einrasten 0,15 | frueher Zerfall (nach Einrasten) | Hauptoption getroffen |
| V16 | K4 <= 1e-9 | 9,7e-12 | getroffen |
| V17 | Paar g = 0,5: Waende verbinden A und B | 0 Wechsel auf dem Kreis um beide, alle d | getroffen |
| V18 | E_g - E_0 linear, Steigung 1,22 bis 3,22 (g = 0,5) | 1,87 mit Abzug (direkt 0,97; E_0 unsauber) | getroffen nach Wortlaut, Vorbehalt |
| V19 | E_0 aendert sich um < 1/3 der Wandarbeit | Delta E_0 = 3,14 (d = 5 bis 8) gegen 1/3 x 6,13 = 2,04 | verfehlt |
| V20 | Bilanz <= 1e-3; L3 gleicher Ausgang, Raten auf 20 % | bis 1 % geschluckt: Q <= 9,6e-5, E <= 1,0e-3, J <= 2,6e-3; ganzer Lauf Q bis 5,3e-3; L3 bestanden | teilweise |
| V21 | g = 0,5: Omega d konstant +- 30 %, Omega d^2 nicht | +-10 %; Faktor 3,4 | getroffen |
| V22 | F zwischen 0,5 und 1,5 x 2 sigma_Pol | 0,84 bis 1,01 | getroffen |
| V23 | g = 0: \|Omega\| < 0,3 \|Omega(0,5)\| | 0,32 bis 0,37 (d_0 5 bis 9), 0,10 (d_0 3) | verfehlt (knapp) |
| V24 | g = 0,5, d = 3: Wirbel laufen zusammen | d bleibt ~2,4 bis 2,6 | verfehlt |
| V25 | \|Omega(0,2)\|/\|Omega(0,5)\| = 0,6 +- 0,2 | 0,22 (d_0 = 5 und 7), 0,41 (d_0 = 3); mit Abzug von g = 0 0,43 | verfehlt (2 von 3 ausserhalb) |

- Summe: 14 getroffen, 3 teilweise, 8 verfehlt.
- Offengelegt:
  - Die Radialzahlen bei Q = 110 kannte ich aus dem lokalen Rauchtest (08:07) vor den .69-Laeufen. Die Vorab-Tabelle war
    da schon eingefroren (07:58).
  - V21 bis V25 standen vor paardyn fest (08:22:33), paardyn lief ab 08:30:12.

## 6. Kontrollen

- **K1** (bekannte einkomponentige Grenze) bestanden:
  - radial auf <= 6,2e-6
  - Teilung Q = 110,17: 75 / gamma 0,0631 gegen RING-T 75 / 0,0641
  - Q = 93,86: 50 / 0,0926 gegen 50 / 0,0925
  - Q = 138,76 teilt spaet (1085 gegen RING-T 1045 bei 0,60)
- **K2** (Bilanz, nach_bilanz_ergebnis.json):
  - Bis 1 % geschluckter Ladung: Q <= 9,6e-5, E <= 1,0e-3 (mit Rampenarbeit), J <= 2,6e-3 relativ.
  - Ueber den ganzen Lauf Q bis 5,3e-3. Das ist der von RING-K bekannte Quadraturfehler grosser Verlustraten
    (T_MEAS = 1); fein halbiert ihn (4,8e-3 -> 2,4e-3).
  - Laeufe ohne Randverlust (Q199_g0, fc_Q139): Q ~ 1e-6, E ~ 6e-6.
- **K3 / L3** bestanden im Feinfenster (dyn0 bis 600, dyng bis 400); paar und paardyn nur grob.
- **K4** bestanden: dyng 9,7e-12; paar 1,1e-13.
- **K5** bestanden: dE/dQ_a = omega_a auf 1e-5 relativ.

## 7. Latten und Vorschlag

- L1 ja (8 von 25 Vorab verfehlt). L2 ja (einkomponentige Kontrollen, g = 0, g <-> -g).
- L3 ja im Feinfenster; nein fuer paar und paardyn.
- L4 teilweise: Gefuellte Wirbel und Vortex-Molekuele mit linearem Potential sind fuer Rabi-Kopplung bekannt (ROT-3:
  Son und Stephanov, Tylutki u. a., Kasamatsu u. a.). Neu nach ROT-3-Stand sind die Ising-Waende bei Kopplung zweiter
  Ordnung im Q-Ball und das Einrasten durch Ladungsumsatz.
- L5 nein (kein Messbezug; modellintern).
- Vorschlag:
  - (a) gefuellter Kern: **parken** (bei g = 0 stabiler, bei g != 0 zerstoert).
  - (c) Strang zwischen zwei Wirbeln: **weiter**, mit L3 fuer paardyn, g <-> -g, groesserem Ball fuer "Strangbruch" bei
    grossem d und der Frage Schlitz gegen Linse.
  - T1-Texturast bei kleinem g (0,02 / 0,05, langsame Rampe) als kleiner Test, wenn die Leitung ihn will.

## 8. Grenzen

- 2D-Querschnitt (Wirbellinien, keine Wirbelringe); ein Ball fuer g != 0 (Q = 199, q_2 = 0,25) plus Q = 110; eine Rampe
  (50); Saat 0,01 mit festen Phasen.
- Wandmasse auf Kreisen um den S^2-Schwerpunkt. Nach dem Wirbelaustritt schneiden die Kreise Waende mit psi_1 = 0; die
  Windungen W, W1 sind dann nicht auswertbar (Vorzeichensprung t = 65 bis 90 bei g = 0,2).
- P2 und n_z/S in der Wandmitte (ROT-3 T1) wurden nicht direkt aufgezeichnet; die Minderheitsdichte an der Wand ist der
  Ersatz.
- Paar: Die Magnus-Beziehung ist von Hand hergeleitet und nicht nachgelesen [Hand]. Die Wirbelzuordnung ist
  blockbasiert (Lagefehler <= dx).

## 9. Abweichungen vom Plan und Verstoesse

- **Verstoss (Selbstanzeige):** Um etwa 08:11 (vor 08:11:19 laut date) begann ein Bearbeitungsbefehl versehentlich mit
  einem leeren `python3 -` (leerer, gequoteter Heredoc). Das ist ein lokaler Interpreterstart ohne Zweck; gerechnet wurde
  nichts. Bitte ins Arbeitsfeld uebernehmen.
- Lokal gelaufen ausser den Rauchtests: ein Diagnoseskript (Scratchpad dbg_paar.py, 08:10, CPU, 1 Thread, nice 19,
  timeout 120). Es rechnete nur die Wirbelsuche auf dem Anfangsfeld.
- Aenderungen vor den Messlaeufen (PLAN 8, 08:22:33):
  - Wirbelsuche per Achter-Umlauf
  - paar mit Phasenklammer statt Fleck, d = 5 / 6,5 / 8 / 9,5 statt 2 / 4 / 6 / 8, Q_1 und Q_2 einzeln fest
  - neu paardyn
- Nach den ersten Laeufen (08:26 bis 08:33) nur die Nachauswertung ergaenzt (Bilanz bis 1 %, Wand-Zeitreihe; nach liest
  die gespeicherten Reihen). Die Physikrechnung blieb unveraendert.
- Codestaende je Lauf (sha256-Anfang):
  - LAUF0 (GPU-Rauchtest) 66c63780, noch mit engerer Klammer (0,4 bis 1,0) und ohne paardyn
  - LAUF1 bis LAUF4 (radial, dyn0a, dyng, dyn0b) cb0635d9
  - LAUF5 und 6 (paar, paardyn) 9137766a
  - LAUF7 bis 9 c29e7794; LAUF7 startete in der Minute des Tauschs, also 9137766a oder c29e7794
  - Ab cb0635d9 aendern sich nur Auswertungsteile (bilanz, nach); radial, dyn0, dyng, paar und paardyn rechnen gleich.
- Das Skript auf der .69 wurde jeweils per neue Datei + mv ersetzt, nie in place.
- Kein git, keine Journaleintraege, keine Hooks oder Dienste; fremde Dateien nur gelesen.

## 10. Dateien und Rechenzeit

- Code: rot1.py (dieser Ordner; auf der .69 /home/fmh/fmhc-physics-remote/runde9-rot1/rot1.py).
- Plan: PLAN.md mit Kopien -0758 und -0822.
- Ausgaben: lauf-69/ausgabe/ (Berichte, JSON, PNG; die *_roh.pt bleiben auf der .69); Logs lauf-69/LAUF0 bis LAUF9.
- Bilder:
  - radial_profile.png
  - dyn0_grob_* und dyn0_fein_* (Schnappschuesse; die groben Zeitpunkte 500 bis 1500 zeigen nur Reststrahlung)
  - dyng_grob_Q199_g+0.2.png und dyng_grob_Q199_g+0.5.png (Waende bei t = 50)
  - dyng_grob_Q199_g0.png (stabil drehend)
  - paar_felder.png, paardyn_grob_*.png
- GPU-Zeit (Entwicklung, P4000, gemessen im Bericht):
  - radial 36 s; dyn0a 186 s; dyn0b 158 s; dyng 237 s; paar 74 s; paardyn 76 s; dyn0 fein 106 s; dyng fein 40 s
  - zusammen etwa 15 min
  - Wartezeit hinter EVO-1 auf beiden Spuren 3 bis 6 min je Aufruf

## Einfach gesagt

Ein drehender Feldklumpen hat in der Mitte ein Loch. Wenn man dieses Loch mit dem zweiten Feld fuellt, haelt der Klumpen
besser zusammen und braucht weniger Energie, solange die beiden Felder nichts voneinander wissen (g = 0). Schaltet man die
Kopplung ein, bilden sich wie vorhergesagt zwei scharfe Grenzlinien im Feld; die Drehung bremst ab, und der Klumpen
zerbricht oder verliert seinen Wirbel. Zwei Wirbel in verschiedenen Feldern sind dann durch ein Band verbunden, dessen
Zugkraft nicht vom Abstand abhaengt, aehnlich wie ein Gummiband mit fester Spannung. Das ist ein huebsches Bild fuer
"Einschluss", aber kein Beweis fuer Quarks.
