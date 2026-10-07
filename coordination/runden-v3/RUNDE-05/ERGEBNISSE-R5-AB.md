# Runde 5: Ergebnisse der Pakete R5-A (3D radial) und R5-B (1D Einzelball)

Auswertung: Subagent der Leitung (Anthropic, Opus), reine Lese- und Schreibaufgabe.
Beginn 2026-09-30 02:53:01 CEST, Ende 2026-09-30 03:11:51 CEST (beide mit date gemessen).
Explorativ nach v3, keine formale Bestaetigung. Die Leitung entscheidet die Abschaetzung.

## Grundlage und Kennzeichnung

- **Gelesen:**
  - README.md, RUNDE-05.md, RUNDE-05/AUFTRAG-R5.md
  - Ideentexte Bio 1, 3, 4, 17, 19, 20, 22, 34, 36, 37, 38, 45 und Chemie 10, 11, 18
  - r5a/PLAN.md und r5b/PLAN.md
  - alle zwoelf Berichte in r5a/lauf-69/ausgabe-* und r5b/lauf-69/ausgabe-*
  - r5a/lauf-69/LAUF1.log, LAUF2.log und r5b/lauf-69/LAUF.log
- **Rauchtests** (rauch-cpu/, rauch/) sind nicht ausgewertet.
- **Rechenorte laut Logs:**
  - R5-A: alle sechs auf der CPU der .69 (Spuren cpu und cpu2, 1 Faden, Schiessen 256 x 5), 0 bis 381 s je Aufruf.
  - R5-B: alle sechs auf der Quadro P4000 (p4000a), 21 bis 48 s je Aufruf.
  - Alle Aufrufe endeten mit rc = 0 und "Fehler: keine".
- **Zahlen** stehen so im Bericht, sofern nicht markiert.
  - **KR** heisst Kopfrechnung aus Berichtszahlen (Differenz oder Verhaeltnis). Diese Zahl steht nicht im Bericht.
  - **laut JSON** heisst: aus der Ergebnisdatei neben dem Bericht, weil der Bericht die Einzelheit nicht nennt.
- **Stufen:** "grob" ist h = 0,05 bzw. dx = 0,1 und dt = 0,05; "fein" halbiert sie. Ohne Angabe gilt grob.
- **Latten (ein Wort je Latte):** L1 kann scheitern, L2 Gegenprobe, L3 Numerik, L4 schon bekannt, L5 Messbezug.

## 1. Je Test

### R5-A, 3D radial

#### Bio 1 Membran (`membran`)

- **Vorhersage (PLAN, Abschnitt 4):**
  - V1a: |dP_mech/P_in - 1| < 1e-3.
  - V1b: Gegenprobe d = 1, |P_in| < 1e-8.
  - V1c: sigma/sigma_inf bei omega^2 <= 0,53 zwischen 0,95 und 1,05; die Abweichung waechst etwa linear.
  - V1d: Y_vorh 0,97 bis 1,04 (0,52), 0,93 bis 1,08 (0,55) und 0,95 bis 1,20 (0,60); R_YL = 35,0 / 13,8 / 6,76.
  - V1e: |delta| < 2 und etwa konstant bis 0,60.
  - V1f: Y_grad - 1 < 0,01 bis 0,53, < 0,1 bis 0,60, > 0,1 ab 0,80.
  - Gegenhypothese: Y_vorh bei 0,52 mehr als 5 % neben 1, oder sigma/sigma_inf bei 0,51 bis 0,53 mehr als 10 %.
- **Ergebnis:**
  - V1a: max |ident| 9,4e-05. V1b: max |P_in| 2,1e-09.
  - V1c: 1,0194 / 1,0375 / 1,0545 bei 0,51 / 0,52 / 0,53; Zuwachs je 0,01 etwa 0,018, 0,017, 0,016 (KR).
  - V1d: Y_vorh 1,0185 / 1,0412 / 1,0664; R_YL 35,012 / 13,812 / 6,761.
  - V1e: delta +0,339 (0,51) bis +0,251 (0,60), Fit +0,271.
  - V1f: Y_grad 1,0002 / 1,0008 / 1,0018 (0,51 bis 0,53), 1,0163 (0,60), 1,1652 bis 1,3960 (0,80 bis 0,98).
  - Die Gegenhypothese trat nicht ein.
- **Treffer:** getroffen, bis auf V1c bei 0,53 (1,0545, knapp ueber 1,05). Bei V1e gilt |delta| < 2, "etwa konstant"
  nur grob (0,339 auf 0,251).
- **L3:** 64 von 64 Kenngroessen. Die Aenderungen betragen hoechstens 4,7e-05 bei Effekten ab 5,9e-03.
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 vermutlich, L5 nein.
- **Vorschlag: parken.** Das Tropfenbild gilt fuer duenne Waende auf 1 bis 4 %; das ist vermutlich bekannte
  Duenne-Wand-Physik ohne Messbezug.

#### Bio 4 Tod unter Q_min (`tod`)

- **Vorhersage:**
  - V4a: Der Tod kommt erst, nachdem Q_erw unter Q_min faellt; tau > 0 und gamma tau < 0,3; omega vor dem Tod 0,95 bis
    0,965.
  - V4b: Klasse "schlagartig" (Rate/gamma > 10 und gamma (t10 - t90) < 0,1) mindestens bei gamma = 1e-3 und 5e-4.
  - V4c: Stopp bei 1,1 Q_min ueberlebt (q_rel(T) > 0,9); Stopp bei 0,9 Q_min stirbt (q_rel(T) < 0,1).
  - V4d: tau 10 bis 300; Exponent p 0,1 bis 0,45, erwartet etwa 0,2.
  - Gegenprobe ohne Abfluss: q_rel(T) > 0,99 und S_c(T)/S_c(0) 0,95 bis 1,05.
  - Gegenhypothese "allmaehlich": q_rel bleibt nahe 1 bis weit unter Q_min, oder ein Rest ueberlebt den Stopp bei 0,9 Q_min.
- **Ergebnis** (fein weicht hoechstens 1 % ab):

  | gamma | t(Q_erw = Q_min) | t90 / t50 / t10 | Q_in(t90)/Q_min | omega vor Tod | Rate/gamma | gamma x (t10 - t90) | Klasse |
  |---|---|---|---|---|---|---|---|
  | 2e-3 | 254,6 | 380 / 433 / 569 | 0,695 | 1,0073 | 7,57 | 0,378 | allmaehlich |
  | 1e-3 | 509,2 | 652 / 708 / 852 | 0,775 | 1,0070 | 13,43 | 0,200 | unklar |
  | 5e-4 | 1018,5 | 1180 / 1238 / 1388 | 0,826 | 1,0067 | 24,94 | 0,104 | unklar |

  - tau = t50 - t(Q_erw = Q_min) betraegt 178 / 199 / 220, gamma tau 0,36 / 0,20 / 0,11 (beides KR).
  - Die Dauer t90 bis t10 betraegt 189 / 200 / 208 (KR), also fast unabhaengig von gamma.
  - Exponent p = 0,150 (fein 0,151).
  - Stopp bei 1,1 Q_min: q_rel(T) 0,9999, omega am Ende 0,9373, S_c 1,0437 auf 0,805.
  - Stopp bei 0,9 Q_min: q_rel(T) 0,0030; t90 = 652 liegt nach dem Stopp bei 614,6. Klasse "unklar".
  - Ohne Abfluss: q_rel(T) 1,0000, S_c 1,0437 auf 1,04, omega 0,8944.
- **Treffer: teilweise.**
  - V4c, V4d und die Gegenprobe sind getroffen.
  - V4a ist teilweise getroffen. Die Reihenfolge stimmt, aber gamma tau liegt bei 2e-3 ueber 0,3 (KR), und omega vor
    dem Tod ist 1,007 statt 0,95 bis 0,965.
  - V4b ist verfehlt: Keine Klasse ist "schlagartig". Bei 5e-4 fehlt es knapp (0,104 statt < 0,1).
  - Die Gegenhypothese "allmaehlich" trifft teilweise zu: q_rel bleibt ueber 0,9, bis Q_in 0,70 bis 0,83 Q_min
    erreicht. Einen Rest nach dem Stopp bei 0,9 Q_min gibt es nicht.
- **L3:** 12 von 12 (sterbende Laeufe, grob gegen fein).
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 teilweise, L5 nein.
- **Vorschlag: weiter.** Das Gebilde, das mit omega > 1 bis 0,70 bis 0,83 Q_min haelt und dann in etwa 200
  Zeiteinheiten zerfaellt, ist ungeklaert.

#### Bio 17 Mutanten (`mutanten`)

- **Vorhersage:**
  - V17a: n = 1 und 2 je mindestens 15 von 20 gueltig; Q_n > Q_0 bei gleichem omega; Q_min,2 > Q_min,1 > Q_min,0 = 111,8.
  - V17b: E_n > E_0 bei gleichem Q, und E_2 > E_1.
  - V17c: Alle n = 1- und n = 2-Laeufe zerfallen vor T = 1000, mit lambda > 0,005 und Zerfallszeiten 50 bis 500.
    Kontrollen: n = 0 bei 0,80 lebt (Abweichung am Ende < 1e-3), n = 0 bei 0,95 zerfaellt.
  - V17d: Meist bleibt ein Grundzustandsball (S_c(T) > 0,3, Q_in(T) > Q_min).
- **Ergebnis:**
  - V17a:
    - gueltig 20 von 20 (n = 1) und 20 von 20 (n = 2)
    - Q_min,1 = 1311 bei 0,9654; Q_min,2 = 5351 bei 0,9800 (Rand des Gitters); Q_min,0 = 111,8 bei 0,9269
  - V17b:
    - min(E - E_0) = +210,3 (n = 1) und +1136 (n = 2)
    - E_2 > E_1 steht nicht im Bericht. Stichprobe aus der Tabelle: n = 1 hat bei Q 11822 E/Q 0,889, n = 2 bei
      Q 12481 E/Q 0,969.
  - V17c:
    - Alle sechs Laeufe zerfallen: t_zerfall 141 bis 368 (fein 142 bis 366); lambda 0,0124 bis 0,0443 (fein 0,0125 bis
      0,0411).
    - Kontrolle n = 0 bei 0,80: "lebt bis T". Die Abweichung am Ende steht nicht im Bericht, am Start ist sie 1,4e-06.
    - Kontrolle n = 0 bei 0,95: zerfaellt bei 83 (fein 89), lambda 0,058.
  - V17d:
    - S_c(T) 0,68 bis 1,22 (fein 1,04 bis 1,13)
    - Q_in(T)/Q_0 0,34 bis 1,07 bei Q_0 >= 1776, also weit ueber Q_min
    - omega am Ende 0,74 bis 0,83
- **Treffer: getroffen.** E_2 > E_1 ist nicht direkt geprueft, und Q_min,2 ist nur eine obere Schranke.
- **L3:** 47 von 48. Nicht bestanden hat die Zerfallszeit der Kontrolle n = 0 bei 0,80, die nie zerfaellt (nan,
  laut JSON). lambda und der Endzustand gehoeren nicht zum L3-Satz.
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 vermutlich, L5 nein.
- **Vorschlag: parken.** Existenz und Zerfall kamen wie erwartet. Die Lebensdauern gelten nur fuer l = 0, und der
  Endzustand haengt stark an der Aufloesung.

#### Bio 19/34 Fitness und Energiewaehrung (`fitness`)

- **Vorhersage** (laut PLAN nicht blind, von Hand gegen drei Tabellenzeilen geprueft):
  - F1: E/Q faellt auf beiden Aesten streng (0 Verstoesse).
  - F2: E/Q - omega > 0 in allen Zeilen.
  - F3: Duennwand-Konstante 1,00 bis 1,03 (0,51), 1,02 bis 1,04 (0,52), unter 1,07 (0,55).
  - F4: Fenster [111,8; etwa 142], E = Q zwischen 0,84 und 0,85, Faktor 1,27; auf dem dicken Ast ueberall E > Q.
  - F5: Fusion setzt immer Energie frei, und die Ladung fliesst vom kleinen zum grossen Ball. dE/Q1 fuer (150; 1e6)
    betraegt etwa 0,28, und b reicht von -0,017 bis +0,282.
- **Ergebnis:**
  - F1: Verstoesse duenn 0, dick 0.
  - F2: min(E/Q - omega) 3,584e-03.
  - F3: 1,0129 / 1,0250 / 1,0569.
  - F4: Q_min 111,844 (0,9269) und Q_abs 141,48 (0,8461); kein dicker Ast mit E < Q; Faktor 1,265 (KR).
  - F5: alle dE > 0, Ladungsfluss "True", dE/Q1 (150; 1e6) = 0,2787; b von -0,01725 (0,93) bis +0,28227 (0,51).
- **Treffer: getroffen**, alle fuenf. Die Vorhersage war nicht blind.
- **L3:** nicht anwendbar (nur Tabellenauswertung).
- **Latten:** L1 schwach, L2 Tabellenkontrollen, L3 entfaellt, L4 bekannt, L5 nein.
- **Vorschlag: verwerfen.** Alle Aussagen folgen vorab aus Virialsatz und dE/dQ = omega; es bleibt keine offene Frage.

#### Chemie 11 Keimbildung (`keim`)

- **Vorhersage:**
  - K1: Mit Bad wachsen die Baelle mit Versatz -0,02 und -0,005, die mit +0,005 und +0,02 schrumpfen, bei allen drei
    omega_b. Der Ball mit Versatz 0 aendert Q um weniger als 20 % der Aenderung bei +-0,005.
  - K2: kappa/kappa_vorh 0,75 bis 1,25 fuer alle Versaetze ungleich 0.
  - K3: R_c = R_halb(omega_b) auf 3 %; R_CNT/R_c 0,92 bis 1,08 (0,55) und 0,83 bis 1,05 (0,60); bei 0,70 offen.
  - Gegenprobe ohne Bad: |Q_T/Q_0 - 1| < 1e-3, |kappa| < 1e-6.
- **Ergebnis:**
  - K1: Alle zwoelf Vorzeichen stimmen, grob und fein.
    - Versatz 0: Q_T/Q_0 1,00096 / 1,00154 / 1,00315 (grob) und 0,99966 / 0,99972 / 0,99991 (fein)
    - Zum Vergleich +-0,005 bei 0,55: 1,08669 und 0,92097
  - K2: kappa/kappa_vorh 1,05 bis 1,11 (0,55), 1,14 bis 1,20 (0,60) und 1,31 bis 1,38 (0,70); fein ebenso
    (1,05 bis 1,12 / 1,13 bis 1,20 / 1,31 bis 1,38).
  - K3: R_halb/R_c 1,0010 / 1,0009 / 1,0009 und R_CNT/R_c 0,9615 / 0,9385 / 0,9276.
  - Gegenprobe: Q_T/Q_0 1,00000 und |kappa| hoechstens 1,3e-10.
- **Treffer: teilweise.** K1, K3 und die Gegenprobe sind getroffen; K2 ist bei omega_b^2 = 0,70 verfehlt.
- **L3:** 12 von 12 (kappa).
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Das Reservoirbild traegt, aber R_c = R_halb(omega_b) folgt fast aus der Formel selbst. Echte
  Keimbildung aus einem duennen Medium ist im Ein-Feld-Modell laut PLAN nicht moeglich (spinodal).

#### Chemie 18 magische Zahlen (`magisch`)

- **Vorhersage:**
  - M1 (n = 0): 0 Monotonie-Verstoesse, keine auffaelligen vierten Differenzen, dE/dQ = omega im Median unter 3e-4,
    min(E/Q - omega) > 0.
  - M2: Q_min = 111,84 +- 0,05 bei 0,927 +- 0,002; Q_abs = 142 +- 3.
  - M3: n = 1 und 2 glatt und monoton je Ast, jeweils mit eigenem Q_min.
  - M4: keine Kreuzung (0 Faelle mit E_n < E_0).
  - Gegenhypothese: ein auffaelliger Punkt oder Monotonie-Verstoss ueber dem Zwanzigfachen des h/2-Rauschens, oder
    eine Kreuzung.
- **Ergebnis:**
  - M1: 97 Profile, Verstoesse 0 und 0.
    - |d4| Median 6,0e-08, max 2,3e-07; auffaellig 0
    - dE/dQ = omega Median 1,4e-04 (max 2,1e-03); min(E/Q - omega) 3,584e-03
  - M2: Q_min 111,8617 bei 0,9271, Q_abs 141,494.
  - M3, n = 1: Q_min 1310,89 (0,9654), Q_abs 1540,57, Verstoesse 0 und 0. Auffaellig sind 2 Stellen:
    - 0,92: d4 -1,49e-04 bei Nachbarn 1,3e-05
    - 0,94: d4 -3,75e-04 bei Nachbarn 1,8e-05
  - M3, n = 2: Q_min 5351,45 (0,9800, Rand des Gitters), Q_abs 6111,13, Verstoesse 0 und 0. Auffaellig sind
    wieder 0,92 (-1,06e-04) und 0,94 (-2,76e-04).
  - M4: 0 von 40 Vergleichen.
- **Treffer: teilweise.** M1, M2 und M4 sind getroffen. Bei M3 ist die Monotonie erfuellt, "glatt" nach dem
  Vorab-Kriterium aber nicht: je zwei auffaellige Stellen. Formal erfuellt das die Gegenhypothese.
- **L3:**
  - Das h/2-Rauschen gibt es nur fuer n = 0: |E/Q(h) - E/Q(h/2)| max 2,9e-08, |Q(h)/Q(h/2) - 1| max 8,2e-07.
  - Fuer n = 1 und 2 gibt es keinen h/2-Lauf. Laut r5a.py (Zeilen 1135 bis 1144) dient das n = 0-Rauschen dort als
    Schwelle.
- **Latten:** L1 schwach, L2 bestanden, L3 teilweise, L4 bekannt, L5 nein.
- **Vorschlag: parken.** n = 0 ist glatt, wie das Papier es festlegt. Die zwei Stellen bei n = 1 und 2 erst auf einem
  feineren omega^2-Gitter mit h/2 beurteilen, sonst verwerfen.

### R5-B, 1D Einzelball

#### Bio 3 Fuettern (`fuettern`)

- **Vorhersage:**
  - C_Q ueber der Schwelle (Born, Faktor 3 unsicher):
    - 0,55: 0,07 (2,6), 0,05 (2,8), 0,04 (3,0)
    - 0,70: 1,3e-3 (2,8), 9e-4 (3,0)
    - 0,90: etwa 1e-8
  - C_Q unter der Schwelle bei eps = 0,01: unter 1e-3 (0,55, und 0,70 ausser nahe 2,3), unter 1e-4 (0,90).
  - V-F1: Sprung mindestens Faktor 5 bei 0,55, bei 0,70 nur falls die Spitze bei 2,2 unter 3e-4 liegt; kein Sprung bei
    0,90.
  - V-F2: C_Q(0,05)/C_Q(0,01) 0,7 bis 1,4 bei 0,55 ueber der Schwelle.
  - V-F3: Wo unter der Schwelle C_Q(0,05) > 1e-4 ist, liegt das Verhaeltnis bei 10 bis 40.
  - V-F4: dE/dQ = omega auf 10 %, wo |C_Q| >= 1e-3; d omega folgt (d omega/dQ) dQ auf 30 %, wo |d omega| > 1e-4.
  - V-F5: Antiteilchen lassen den Ball schrumpfen: 0,55 etwa -0,024 (2,2) und -0,015 (3,0), 0,70 etwa -4e-4 und
    -2e-4.
- **Ergebnis:**
  - Ueber der Schwelle:
    - 0,55: C_Q 0,0601 / 0,0524 / 0,0423 (Born 0,0701 / 0,0539 / 0,0436)
    - 0,70: 7,83e-4 / 6,66e-4 (Born 1,26e-3 / 9,25e-4)
    - 0,90: -2,7e-6
  - Unter der Schwelle bei eps = 0,01:
    - 0,55: 1,9e-5 (1,6), aber **2,36e-2 (2,2)**
    - 0,70: 5,7e-6 (1,6), 5,64e-4 (2,2), 5,50e-4 (2,6)
    - 0,90: |C_Q| hoechstens 1,3e-5
  - V-F1: Faktor 2,5 (0,55), 1,4 (0,70), -0,2 (0,90).
  - V-F2: 0,98 / 0,97 / 0,96.
  - V-F3: 23,1 bei 0,55/1,6 (fein 24,8); dagegen 1,09 bei 0,55/2,2, 0,96 bei 0,70/2,2 und 0,86 bei 0,70/2,6.
  - V-F4, Energie:
    - ueber der Schwelle bei 0,55: dE/dQ 0,742 bis 0,759 (omega 0,7416)
    - bei 0,55/2,2 dagegen 2,15 (eps 0,01) und 2,04 (eps 0,05)
  - V-F4, Frequenz:
    - bei eps = 0,05 ueber der Schwelle: d omega -3,98e-4 / -3,59e-4 / -3,13e-4 gegen Soll -3,94e-4 / -3,63e-4 / -3,14e-4
    - bei 0,55/2,2: -1,73e-4 gegen -1,46e-4
  - V-F5: 0,55: -2,37e-2 / -1,45e-2 (Born -2,43e-2 / -1,45e-2); 0,70: -3,41e-4 / -2,18e-4 (Born -3,84e-4 / -2,21e-4).
  - Ballort am Ende bei 0,55/2,2/eps 0,05: +1,41.
- **Treffer: teilweise.**
  - Getroffen sind V-F2, V-F4 ueber der Schwelle, V-F5 und die Kontrolle 0,90.
  - V-F1 ist fuer 0,55 verfehlt; fuer 0,70 ist seine Bedingung nicht erfuellt (5,64e-4 > 3e-4).
  - V-F3 gilt nur bei 0,55/1,6.
- **L3:** 33 von 34. Nicht bestanden hat 0,70/1,6/eps 0,01: Effekt 5,7e-6 gleich der Aenderung, also Rauschniveau
  (laut JSON).
- **Latten:** L1 ja, L2 gerissen, L3 bestanden, L4 bekannt, L5 nein.
- **Vorschlag: weiter.** Der Einfang unter der Schwelle (0,55 bei 2,2: 2,4 % mit dE/dQ 2,15) widerspricht dem
  Papierbild. Offen ist, wo diese Ladung sitzt: Fenster, Laufzeit, Ort.

#### Bio 36 Photosynthese (`photo`)

- **Vorhersage:**
  - V-P1: Gamma < 1e-3 unter der Schwelle (0,55 bei 2,0 / 2,3 / 2,45; 0,70 bis 2,64).
  - V-P2: Sprung zwischen 2,45 und 2,52 (0,55) bzw. 2,64 und 2,71 (0,70) um mindestens Faktor 5. Die Hoehe folgt Born
    auf Faktor 3:
    - 0,55: bis 0,09 bei 2,52 (nahe der Schwelle eher kleiner), 0,07 (2,6), 0,05 (2,8), 0,04 (3,1)
    - 0,70: 1,6e-3 (2,71), 1,3e-3 (2,8), 8e-4 (3,1)
    - 0,90 bei 3,1: < 1e-5
  - V-P3: gleiches Gamma bei eps 0,025 und 0,05 (auf 30 %).
  - V-P4: G_E/G_Q = omega auf 10 %.
  - V-P5: Antiteilchen-Welle 0,55/2,3 gibt Gamma etwa -0,023.
  - V-P6: 0,55/2,6 gibt G etwa 8e-4 je Zeiteinheit; kein beschleunigtes Wachstum.
  - Gegenprobe Welle allein: Einstrom 2 k eps^2 auf 5 %.
- **Ergebnis:**
  - V-P1:
    - 0,55: -8,6e-4 (2,0), 1,50e-3 (2,3), 1,20e-3 (2,45); eps 0,025 bei 2,3: 2,31e-3
    - 0,70: 5,4e-5 (2,0), 1,45e-3 (2,3), **4,53e-3 (2,6)**, 7,2e-5 (2,64)
  - V-P2, Spruenge: 1,20e-3 auf 2,15e-2 (0,55) und 7,2e-5 auf 9,30e-4 (0,70), etwa Faktor 18 und 13 (KR).
  - V-P2, Hoehen:
    - 0,55: 0,0215 (Born 0,0933), 0,0729, 0,0635, 0,0443
    - 0,70: 9,30e-4, 8,43e-4, 6,13e-4
    - 0,90 bei 3,1: 1,76e-6
  - V-P3: 0,0545 (eps 0,025) gegen 0,0635 (eps 0,05).
  - V-P4, G_E/G_Q ueber der Schwelle:
    - 0,55: 0,290 (2,52), 0,885 (2,6), 0,771 (2,8), 0,758 (3,1), 0,748 (2,8 mit eps 0,025)
    - 0,70: dreimal 0,834
    - 0,90: 1,138
  - V-P5: -0,0200 (Born -0,0226).
  - V-P6:
    - G_Q 8,79e-4 bei 2,6; dQ am Ende +0,188 (Ballladung 3,814 laut rauschen-Bericht)
    - d omega/dt -4,6e-5 gegen Soll -3,2e-5; eine Beschleunigungsgroesse steht nicht im Bericht
  - Einstrom gegen Soll: 0,3 bis 0,7 % daneben (grob), hoechstens 0,15 % (fein) (KR).
- **Treffer: teilweise.**
  - Getroffen sind V-P2 (Spruenge; Hoehen ausser 2,52), V-P3, V-P5, V-P6 (G) und die Gegenproben.
  - V-P1 ist verfehlt: 5 von 8 Werten unter der Schwelle liegen bei 1e-3 oder darueber.
  - V-P4 trifft in 6 von 9 Laeufen ueber der Schwelle.
- **L3:** 18 von 18.
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 bekannt, L5 nein.
- **Vorschlag: weiter, zusammen mit fuettern.** Die Aufnahme unter der Schwelle ist bei 0,70 groesser als ueber der
  Schwelle; ueber der Schwelle ist Born bestaetigt.

#### Bio 38 Winterschlaf (`winterschlaf`)

- **Vorhersage:**
  - V-W1: Die Hauptfrequenz liegt bei allen sechs zwischen 0,9 und 1,15 x (1 - omega) = 0,258 / 0,213 / 0,163 / 0,117 /
    0,078 / 0,051. Der relative Stoss bei 0,70 reproduziert 0,170 +- 0,012.
  - V-W2: Die Antwort je A steigt mit omega^2 (mindestens 4 von 5 Schritten); 0,90/0,55 mindestens 2.
  - V-W3: Der Rest liegt unter 50 % der Stossenergie und steigt mit omega^2.
  - V-W4: Antwort je A bei A = 0,01 und 0,03 gleich auf 20 %.
  - Vorab "bestaetigt": Antwort und Rest sind bei 0,55 am kleinsten und steigen mindestens 4 von 5 Schritte, in
    beiden Stufen.
- **Ergebnis:**
  - V-W1, Hauptfrequenz bei A = 0,01 (Verhaeltnis zur Kante):
    - 0,55: 0,2608 (1,010); 0,62: **1,3907 (6,541)**; 0,70: **1,4875 (9,106)**
    - 0,78: 0,1198 (1,025); 0,85: 0,0809 (1,037); 0,90: 0,0526 (1,026)
  - V-W1 bei A = 0,03: Verhaeltnisse 1,015 / 6,521 / 9,042 / 1,056 / 1,071 / 1,092.
  - Bei 0,62 und 0,70 ist die Kantenlinie nur Nebenspitze (0,2176 und 0,1672).
  - Eine zweite Linie steht bei allen sechs Baellen zwischen 1,38 und 1,82 (1,3775 / 1,3907 / 1,4875 / 1,6144 /
    1,7347 / 1,8230), als Haupt- oder Nebenspitze.
  - Der relative Stoss bei 0,70 gibt 0,1689.
  - V-W2: Antwort Breite/A 0,0573 / 0,0722 / 0,2129 / 0,4792 / 0,7514 / 0,9060; steigend in 5 von 5 Schritten,
    Verhaeltnis 15,8.
  - V-W3: Rest -0,000 bis +0,005 (A = 0,01) bzw. bis +0,015 (A = 0,03); steigend in 5 von 5 Schritten.
  - V-W4: Die Antwort je A weicht zwischen A = 0,01 und 0,03 hoechstens 7 % ab (KR, z. B. 0,7514 gegen 0,7012).
  - Das Vorab-Kriterium "bestaetigt" ist grob und fein erfuellt.
- **Treffer: teilweise.** V-W2, V-W3, V-W4 und das Vorab-Kriterium sind getroffen; V-W1 ist bei 0,62 und 0,70
  verfehlt.
- **L3:** 37 von 39. Nicht bestanden hat der Rest bei 0,55 fuer beide A. Der Effekt 6e-6 bzw. 1e-5 liegt unter bzw.
  gleich der Aenderung 1,2e-5 bzw. 1,1e-5 (laut JSON).
- **Latten:** L1 ja, L2 bestanden, L3 teilweise, L4 teilweise, L5 nein.
- **Vorschlag: parken.** Das Vorab-Kriterium ist erfuellt, gilt aber nur in 1D. Die Linie bei 1,38 bis 1,82 an den
  Resonanz-Strang geben (siehe Anker).

#### Bio 20/37 Rauschen und Schmelzen (`rauschen`)

- **Vorhersage:**
  - V-R1: Alle drei ueberleben eps <= 0,1 (R_Q >= 0,9).
  - V-R2: eps_c(0,55) > eps_c(0,70) > eps_c(0,90); eps_c(0,90) in [0,07; 0,25], eps_c(0,70) in [0,15; 0,4],
    eps_c(0,55) >= 0,25.
  - V-R3: eps_c(0,70)/eps_c(0,90) liegt naeher bei 1,9 als bei 2,5.
  - V-R4 (unsicher): Bei eps <= 0,1 ist dQ/Q fuer 0,55 negativ und waechst wie eps^2; fuer 0,90 kein systematischer
    Abzug.
  - Gegenprobe: Rauschen allein R_Q < 0,5 bei eps <= 0,2; Ball allein R_Q = 1.
- **Ergebnis:**
  - V-R1: kleinstes R_Q bei eps <= 0,1: 0,9327 / 0,9011 / 0,9425.
  - V-R2: eps_c 0,286 / 0,273 / 0,223 (fein 0,280 / 0,276 / 0,223).
  - V-R3: 0,273/0,223 = 1,22 (KR; fein 1,24).
  - V-R4, dQ/Q bei eps 0,025 / 0,05 / 0,1 (je zwei Saaten):
    - 0,55: -1,84e-2 und -1,04e-2 / -3,60e-2 und -2,09e-2 / -6,73e-2 und -5,62e-2
    - 0,90: -1,07e-2 und -2,68e-3 / -2,23e-2 und -6,18e-3 / -5,79e-2 und -2,03e-2
    - Alle Werte sind negativ; das Mittel fuer 0,55 verdoppelt sich je Verdopplung von eps (KR).
  - Gegenprobe: Rauschen allein gibt R_Q hoechstens 0,067 bei eps <= 0,2, hoechstens 0,446 bei eps 0,4. "Ball allein"
    steht nicht als Zeile im Bericht, nur als Bezug fuer dQ/Q.
- **Treffer: teilweise.**
  - V-R1 und V-R2 sind getroffen.
  - V-R3 ist formal getroffen, aber 1,22 passt zu keinem der beiden Werte.
  - V-R4 ist verfehlt.
- **L3:** R_Q 36 von 36, eps_c 3 von 3.
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 teilweise, L5 nein.
- **Vorschlag: weiter, nur mit mehr Saaten.** Die Reihenfolge der Schwellen haengt an 0,004 bis 0,013 Abstand bei
  zwei Saaten, und der Laufteil kostet 21 s.

#### Bio 45 angetriebener Ball (`pumpe`)

- **Vorhersage:**
  - V-PU1: Bei h = 0 gilt d ln Q/dt = -0,0100 auf 2 % (Codeprobe).
  - V-PU2: stabil dissipativ bei h/h_min = 1,25 / 2 / 4, nicht bei 0 / 0,5 / 0,8.
  - V-PU3: Bei 2 h_min enden die Startbaelle 0,55 / 0,60 / 0,70 / 0,80 bei gleichem Q_Ende (2 %, nahe Q* = 2,44) und
    omega = Omega_d; 0,90 zerfaellt (geringe Sicherheit).
  - V-PU4: Bei 0,5 h_min zerfallen 0,60 und 0,80.
  - V-PU5: Der Treiber allein bildet keine Struktur (S_max < 10 S_bg).
  - V-PU6: Ohne Daempfung (2 h_min) bleibt der Ball, rastet aber nicht ein.
- **Ergebnis:**
  - Konstanten: h_min 3,2971e-3, F 3,7025, Q* 2,4415.
  - V-PU1: -0,01027 (fein -0,01026).
  - V-PU2: "stabil" ist in allen 14 Laeufen False.
    - Ball 0,70 bei 1,25 und 2 h_min: Q_Ende/Q* 0,0025 und 0,0038, omega am Ende 0,834
    - bei 4 h_min: Q_Ende/Q* 1,272, omega 0,8359, dQ/dt +6,1e-3 (Q waechst noch)
    - Rate d ln Q/dt in [0,1 T; 0,4 T]: -0,01027 (h = 0), -0,01045 (0,5), -0,01062 (0,8), -0,01109 (1,25),
      -0,01149 (2), +0,00149 (4)
  - V-PU3, Startbaelle bei 2 h_min:
    - 0,55: 0,0041 Q*; 0,70: 0,0038 Q*
    - 0,60: 1,0352 Q* bei omega 0,8352 und dQ/dt -5,3e-4
    - 0,80: -0,0004 Q* (Rate -0,20); 0,90: 0,0014 Q* (Rate -0,62)
  - V-PU4: 0,60 endet bei 0,0035 Q*, 0,80 bei 0,0008 Q*.
  - V-PU5: S_max liegt beim 1,00- bis 1,03-fachen des Soll-Hintergrunds (KR); Struktur False.
  - V-PU6: Q 2,7138 auf 3,1622 (1,295 Q*), omega 0,772, dQ/dt +2,6e-3.
  - Freier Ball ohne Daempfung: Q 2,4415 bleibt 2,4415.
- **Treffer: verfehlt.**
  - Die Kernvorhersagen V-PU2 und V-PU3 sind verfehlt.
  - V-PU1 ist knapp verfehlt: 2,7 % statt hoechstens 2 % (KR).
  - Getroffen sind die Kontrollen V-PU4, V-PU5, V-PU6 und "0,90 zerfaellt".
- **L3:** 14 von 14 (Q_Ende/Q*).
- **Latten:** L1 ja, L2 bestanden, L3 bestanden, L4 bekannt, L5 Analogie.
- **Vorschlag: weiter.** Die Kernvorhersage ist verfehlt, obwohl die Numerik stabil ist. Mit Treiber stirbt der
  passende Ball schneller als ohne. Offene Stellgroessen sind Startphase und Laufzeit.

#### Bio 22 und Chemie 10 Modulationsinstabilitaet und Uebersaettigung (`mi`)

- **Vorhersage:**
  - V-M1: Verklumpung genau fuer S0 < 2/3: ja bei 0,15 / 0,35 / 0,55 / 0,63, nein bei 0,72 / 0,85 (Kontrast < 1e-3).
  - V-M2: k_dom liegt innerhalb 0,063 von k_max.
  - V-M3: Die gemessene Rate trifft g_max auf 15 %, die Raten je Mode auf 0,02.
  - V-M4: Rauschen 1e-3 verklumpt 29 (0,35) bzw. 115 (0,63) Zeiteinheiten frueher.
  - V-M5: Am Ende gibt es weniger Klumpen als L/lambda_max (Plan: 17 / 15 / 13 / 8).
  - V-M6 (Kavitation, geringe Sicherheit): Eine Delle der Breite 8 waechst (Leerlaenge am Ende mindestens Anfang + 5),
    eine der Breite 2 heilt (Ende < 0,5 x Anfang).
  - Zeiten aus der Theorie: t_lin 76 / 43 / 64 / 172 und t_klumpen 105 / 59 / 88 / 237.
  - Gegenprobe: 0,72 und 0,85 ohne Effekt; Q-Drift < 1e-10.
- **Ergebnis:**
  - V-M1:
    - t_klumpen 99 und 97 (0,15), 57 und 55 (0,35), 83 und 82 (0,55), 221 und 224 (0,63)
    - 0,72 und 0,85: keine Klumpen, Leerlaenge 0, E-Drift 4e-10 bis 8e-10; den Kontrastwert nennt der Bericht nicht
  - t_lin: 76 und 74, 44 und 42, 63 und 63, 176 und 185.
  - V-M2: Abstand k_dom zu k_max (KR):
    - 0,026 und 0,025 (0,15); **0,085** und 0,030 (0,35); 0,019 und 0,015 (0,55); 0,024 und 0,063 (0,63)
    - mit delta 1e-3: **0,087** (0,35), 0,025 (0,63)
  - V-M3:
    - g gemessen 0,049 und 0,050 (g_max 0,136), 0,104 und 0,108 (0,239), 0,080 und 0,082 (0,162), 0,029 und 0,028
      (0,060)
    - max |g_k - Theorie| 0,004 bis 0,032; bei delta 1e-3 bis 0,070
  - V-M4: t_klumpen 57 auf 27 (0,35) und 221 auf 100 (0,63), also 30 und 121 frueher (KR).
  - V-M5, Klumpen am Ende:
    - grob: 6 und 7 (0,15), 9 und 16 (0,35), 22 und 22 (0,55), 19 und 16 (0,63)
    - fein: 7 und 6, 11 und 16, 20 und 20, 15 und 17
    - L/lambda_max aus den Berichtswerten: 14,7 / 16,7 / 13,0 / 8,2 (KR)
  - V-M6, Leerlaenge Anfang / Mitte / Ende:
    - 0,72: 6,3 / 118,7 / 39,9 (Breite 2) und 25,1 / 120,9 / 113,8 (Breite 8)
    - 0,85: 6,3 / 83,3 / 19,7 (Breite 2) und 25,1 / 97,1 / 36,9 (Breite 8)
    - Klumpen am Ende: 20 bei 0,72 (fein 24), 0 bei 0,85
  - Q-Drift hoechstens 1,2e-15.
- **Treffer: teilweise.**
  - Getroffen sind V-M1, V-M4, die Zeiten t_lin und t_klumpen und die Gegenprobe.
  - V-M2 trifft in 8 von 10 Laeufen.
  - V-M3 ist fuer die Gesamtrate verfehlt.
  - V-M5 ist bei 0,55 und 0,63 verfehlt.
  - V-M6 trifft fuer Breite 8; die Delle der Breite 2 heilt nicht.
- **L3:** 32 von 54; nicht definierte Werte zaehlen als nicht bestanden.
  - Von 34 definierten Werten bestehen 32.
  - Nicht bestanden hat g gemessen bei S0 = 0,15 in beiden Saaten: Aenderung 0,018 bei Effekt 0,049 (laut JSON).
- **Latten:** L1 ja, L2 bestanden, L3 teilweise, L4 bekannt, L5 Analogie.
- **Vorschlag: parken fuer den MI-Teil, weiter fuer die Kavitation.** Einsatz und Zeiten folgen der bekannten Theorie.
  Offen und neu ist nur, dass bei 0,72 auch die schmale Delle nicht heilt und das Kondensat in 20 Klumpen zerfaellt.

## 2. Auffaelligkeiten

### Klare Widersprueche zur Vorhersage

1. **pumpe: Kein eingerasteter Ball (V-PU2, V-PU3).**
   - Bei 1,25 und 2 h_min stirbt ausgerechnet der passende Ball (omega = Omega_d, Q = Q*).
   - Mit Treiber faellt Q schneller als ohne: -0,0111 und -0,0115 gegen -0,0103.
   - Nur der Startball 0,60 endet bei 2 h_min nahe Q* (1,035 Q*), ist aber nicht stationaer.
   - Bei 4 h_min waechst Q noch am Ende.
   - L3 besteht in allen Laeufen; das ist kein Numerikproblem.
2. **fuettern und photo: Einfang unter der Schwelle, die Gegenprobe reisst.**
   - 0,55 bei nu = 2,2: C_Q = 2,4 % statt unter 1e-3, linear in eps (1,09).
   - Dort ist dE/dQ = 2,15 statt 0,742, und der Ball wandert um 1,41.
   - Dadurch ist der Sprung nur Faktor 2,5 statt mindestens 5.
   - In photo liegt 0,70 bei 2,6 (unter der Schwelle) mit Gamma 4,5e-3 ueber allen 0,70-Werten ueber der Schwelle
     (6,1e-4 bis 9,3e-4).
   - G_E/G_Q unter der Schwelle schwankt von -0,65 bis 2,55 (fein bis -0,92); eine einheitliche Energie je Ladung gibt
     es dort nicht.
3. **tod: Kein schlagartiger Tod, und omega > 1 kurz vor dem Tod.**
   - q_rel bleibt ueber 0,9, bis Q_in nur noch 0,70 bis 0,83 Q_min betraegt.
   - omega im Messfenster bis t90 - 10 (r5a.py, Zeile 757) ist 1,0067 bis 1,0073, vorhergesagt waren 0,95 bis 0,965.
     Ein ruhender Q-Ball mit omega > 1
     existiert nicht; der Rest ist also kein stationaerer Ball mehr. Ob die Phasenmessung am Zentrum dort noch
     zuverlaessig ist, ist nicht geprueft.
   - Die Aufloesung dauert 189 bis 208 Zeiteinheiten fast unabhaengig von gamma (KR). Die mit gamma skalierte
     Klassengrenze gamma (t10 - t90) < 0,1 verlangt bei gamma = 1e-3 aber weniger als 100.
4. **winterschlaf: Die Hauptlinie liegt bei 0,62 und 0,70 nicht an der Kante.** Sie liegt bei 1,39 und 1,49, also beim
   6,5- und 9,1-Fachen der Kante (V-W1).
5. **rauschen: Ladungsverlust schon bei kleinem Rauschen, auch beim kleinen Ball (V-R4).** Er waechst etwa wie eps,
   nicht wie eps^2. Die drei Schwellen liegen eng beieinander (0,22 bis 0,29), das Verhaeltnis 1,22 passt zu keiner
   der beiden Skalierungen (V-R3).
6. **mi:**
   - Mehr Klumpen als L/lambda_max bei 0,55 und 0,63 (22 gegen 13; 16 bis 19 gegen 8).
   - k_dom bei 0,35 (Saat 21) 0,085 bis 0,087 neben k_max.
   - Die Delle der Breite 2 heilt nicht: 6,3 auf 39,9 bei 0,72 und 6,3 auf 19,7 bei 0,85.
7. **keim:** kappa/kappa_vorh liegt bei omega_b^2 = 0,70 mit 1,31 bis 1,38 ueber dem Band 0,75 bis 1,25. Ueberall ist
   der Wert groesser als 1 (1,05 bis 1,20 bei 0,55 und 0,60).
8. **magisch:** je zwei auffaellige vierte Differenzen bei n = 1 und n = 2, an denselben Stellen 0,92 und 0,94. Formal
   ist das die Gegenhypothese.
9. **membran:** V1c bei 0,53 knapp verfehlt (1,0545 statt hoechstens 1,05).

### Numerisch fragwuerdig oder unplausibel

10. **mi, Messgroesse "g gemessen":** Sie liegt bei 36 bis 68 % von g_max (KR). Dagegen treffen t_lin, t_klumpen und
    die Verschiebung mit staerkerem Rauschen die aus g_max abgeleiteten Werte (t_lin 76 / 44 / 63 / 176 gegen
    76 / 43 / 64 / 172; Verschiebung 30 und 121 gegen 29 und 115). Die Groesse ist in sich nicht stimmig, Messfenster
    oder Definition pruefen. Zugleich reisst L3 fuer g bei S0 = 0,15 (0,0488 grob gegen 0,0673 fein).
11. **mutanten: Anwachsrate und Endzustand haengen stark an der Aufloesung und liegen ausserhalb von L3.**
    - lambda bei n = 1/0,70: 0,0242 gegen 0,0339.
    - S_c(T): 0,680 gegen 1,118.
    - Q_in(T)/Q_0: 0,761 gegen 0,675.
12. **mutanten und magisch: Q_min,2 = 5351 liegt am Gitterrand (0,98)** und ist deshalb nur eine obere Schranke.
    Fuer n = 1 und 2 gibt es keinen h/2-Lauf. Die auffaelligen Stellen (Punkt 8) liegen am oberen Ende des groben
    0,02-Gitters.
13. **pumpe, V-PU1:** d ln Q/dt = -0,01027 statt -0,0100 auf 2 %. dQ/dt = -gamma Q gilt fuer die Gesamtladung exakt;
    gemessen wird laut PLAN im Fenster |x| < 20.
14. **keim:** Der Ball mit Versatz 0 heisst bei 0,60 und 0,70 grob "waechst" (+0,15 % und +0,32 %), fein "bleibt".
    Die Klasse kippt also mit der Aufloesung. R_c = R_halb(omega_b) auf 0,1 % folgt fast aus kappa_vorh = 0 bei
    omega = omega_b; die Aussage ist darum schwach pruefend.
15. **rauschen:** Ab eps = 0,3 verliert die Verfolgung den Ball: x am Ende bis -129, R_Q teils negativ. Rauschen allein
    erzeugt dort Spitzen bis R_S 3,1 (fein 3,4). eps_c ist zwischen 0,2 und 0,3 interpoliert und beruht auf zwei
    Saaten.
16. **Bedeutungslose Verhaeltnisse (Division durch Werte nahe 0):**
    - winterschlaf: "Rest 0,90/0,55" = -796 / 1467 / 900 / 722, weil der Rest bei 0,55 auf Rauschniveau liegt; L3
      reisst genau dort.
    - fuettern bei 0,70/1,6: C_Q-Verhaeltnis -8,6 bzw. 8822 und fein dE/dQ = -279.
    - photo: G_E/G_Q unter der Schwelle.
17. **membran:** Die "Membranbreite" (p_t < 0) von 10 bis 32 misst den Schwanz bis zum Schnitt, nicht die Wand. Bei
    0,55 ist sie 10,38 gegen r_cut - R_halb = 24,0 - 14,4 (KR, r_cut aus dem mutanten-Bericht). An die Groesse ist
    keine Vorhersage gebunden.

### Abgleich mit den Ankern

- **3D Q_min = 111,84 bei omega^2 = 0,927: vereinbar.**
  - fitness: 111,844 bei 0,9269
  - mutanten: 111,8 bei 0,9269
  - magisch (Schritt 0,005): 111,8617 bei 0,9271
- **Duenner Ast VK-stabil, dicker instabil: vereinbar.** n = 0 bei 0,80 lebt bis T = 1000; n = 0 bei 0,95 zerfaellt bei
  83 (fein 89).
- **E/Q > 1 ab omega^2 etwa 0,85, metastabiles Fenster bis Q etwa 140: vereinbar.**
  - Q_abs 141,48 bei 0,8461 (fitness), 141,494 (magisch)
  - E/Q bei 0,85: 1,00159
- **Ein Q-Ball unter Q_min (tod):** kein Widerspruch zum Anker, weil bei omega > 1 kein ruhender Ball vorliegt. Die
  Ladung bleibt aber noch 125 bis 162 Zeiteinheiten nach Q_erw = Q_min im Ballgebiet (bis t90, KR; Punkt 3).
- **1D-Resonanz rho = 1,4938 - 6,7e-5 i bei omega^2 = 0,70: kein Widerspruch.**
  - Die winterschlaf-Hauptlinie bei 0,70 liegt bei 1,4875 (A = 0,01) und 1,4770 (A = 0,03), der relative Stoss hat
    eine Nebenlinie bei 1,4821. Die FFT-Aufloesung ist 0,012; ob das dieselbe Resonanz ist, pruefen die Berichte
    nicht.
  - In fuettern und photo liegt die Aufnahme unter der Schwelle bei 0,70 bei nu = 2,2 bis 2,6. Einen direkten Bezug zu
    rho stellt kein Bericht her.
- **Modulationsinstabil fuer S < 2/3: vereinbar.** mi verklumpt bei 0,15 bis 0,63, nicht bei 0,72 und 0,85.

## 3. Zusammenfassung

| Paket | Karte | Kern des Ergebnisses | Treffer | L3 laut Bericht | L1 / L2 / L3 / L4 / L5 | Vorschlag |
|---|---|---|---|---|---|---|
| R5-A | Bio 1 Membran | Y_vorh 1,02 / 1,04 / 1,07 bei 0,52 / 0,55 / 0,60; sigma/sigma_inf 1,02 bis 1,05 bei 0,51 bis 0,53 | getroffen (V1c knapp nicht) | 64/64 | ja / bestanden / bestanden / vermutlich / nein | parken |
| R5-A | Bio 4 Tod | stirbt bei 0,70 bis 0,83 Q_min, omega 1,007; Klasse allmaehlich oder unklar; p 0,15 | teilweise | 12/12 | ja / bestanden / bestanden / teilweise / nein | weiter |
| R5-A | Bio 17 Mutanten | n = 1, 2 existieren (20/20), zerfallen bei 141 bis 368, Rest ist Grundzustandsball | getroffen | 47/48 | ja / bestanden / bestanden / vermutlich / nein | parken |
| R5-A | Bio 19/34 Fitness | E/Q streng fallend, Fenster 111,84 bis 141,48, Fusion immer exotherm | getroffen (nicht blind) | entfaellt | schwach / Tabellenkontrollen / entfaellt / bekannt / nein | verwerfen |
| R5-A | Chemie 11 Keim | Vorzeichen 12/12, R_c = R_halb(omega_b) auf 0,1 %, kappa/vorh bis 1,38 | teilweise | 12/12 | ja / bestanden / bestanden / teilweise / nein | parken |
| R5-A | Chemie 18 magisch | n = 0 glatt, Q_min 111,86; n = 1, 2 je 2 auffaellige Stellen ohne h/2 | teilweise | nur n = 0 | schwach / bestanden / teilweise / bekannt / nein | parken |
| R5-B | Bio 3 Fuettern | ueber der Schwelle C_Q 4 bis 6 % (Born), dE/dQ = omega; unter der Schwelle 2,4 % bei 0,55/2,2 | teilweise | 33/34 | ja / gerissen / bestanden / bekannt / nein | weiter |
| R5-B | Bio 36 Photo | Sprung Faktor 18 und 13; Gamma bei 0,55 ueber der Schwelle 0,022 bis 0,073; unter der Schwelle bis 4,5e-3 | teilweise | 18/18 | ja / bestanden / bestanden / bekannt / nein | weiter |
| R5-B | Bio 38 Winterschlaf | Antwort steigt 15,8-fach von 0,55 bis 0,90; Hauptlinie bei 0,62/0,70 bei 1,39/1,49 | teilweise | 37/39 | ja / bestanden / teilweise / teilweise / nein | parken |
| R5-B | Bio 20/37 Rauschen | eps_c 0,286 / 0,273 / 0,223 geordnet; Verlust ~eps schon bei 0,025 | teilweise | 36/36, 3/3 | ja / bestanden / bestanden / teilweise / nein | weiter (Saaten) |
| R5-B | Bio 45 Pumpe | kein stabiler dissipativer Ball; mit Treiber schnellerer Zerfall | verfehlt | 14/14 | ja / bestanden / bestanden / bekannt / Analogie | weiter |
| R5-B | Bio 22 / Chemie 10 MI | Verklumpung genau fuer S0 < 2/3, Zeiten wie Theorie; g-Messgroesse unstimmig | teilweise | 32/54 (32/34 definiert) | ja / bestanden / teilweise / bekannt / Analogie | parken (MI), weiter (Kavitation) |

## 4. Finns Frage: Was passiert, wenn man einen Q-Ball fuettert?

Wirft man einem grossen Q-Ball (omega^2 = 0,55) Wellen oberhalb der Schwelle nu > 2 omega + 1 zu, behaelt er 4 bis
6 % der ankommenden Ladung (C_Q 0,041 bis 0,060, Born 0,044 bis 0,070). Dabei nimmt er genau omega an Energie je Ladung
auf (dE/dQ 0,742 bis 0,759 gegen 0,742), und seine Frequenz sinkt wie vorhergesagt; ein mittlerer Ball (0,70) behaelt
nur 0,05 bis 0,08 %, ein kleiner (0,90) nichts, und Antiteilchen-Wellen lassen den Ball schrumpfen (-2,4 % und -1,4 %
bei 0,55). Unterhalb der Schwelle, wo nach der Papierrechnung nichts haengen bleiben duerfte, behaelt der grosse Ball bei
nu = 2,2 trotzdem 2,4 % der Ladung, aber mit etwa 2,1 statt 0,74 Energie je Ladung und mit Rueckstoss. Unter
Dauerbestrahlung (photo) waechst er bei nu = 2,6 bis 3,1 mit 4 bis 7 % Fangquote (8,8e-4 Ladung je Zeiteinheit bei
nu = 2,6, zusammen +0,19 bei einer Ballladung von 3,81).

## Einfach gesagt

Wir haben zwoelf kleine Computerversuche ausgewertet, in denen sich ein Q-Ball wie eine Zelle verhalten sollte. Vieles
kam wie vorhergesagt: Die Haut des Balls wirkt wie die Haut eines Wassertropfens, ein grosser Ball frisst schnelle
Wellen und nimmt dabei genau die erwartete Energie auf, und ein duenner Nebel zerfaellt von selbst in Klumpen. Drei Dinge
liefen anders: Ein Ball, dem man langsam Ladung abzieht, stirbt nicht sofort bei seiner Mindestgroesse, sondern haelt
sich noch eine Weile als unruhiger Rest. Ein grosser Ball behaelt auch langsamere Wellen, obwohl er das nach der Rechnung
nicht sollte, und eine Pumpe mit Bremse haelt den Ball nicht am Leben, sondern laesst ihn sogar schneller verloeschen.
Das sind Rechenergebnisse in einem vereinfachten Modell, keine Messungen in der Natur; welche Karten weiterlaufen,
entscheidet die Leitung.
