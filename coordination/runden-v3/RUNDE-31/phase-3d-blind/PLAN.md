# PHASE-3D-BLIND: Plan (Runde 31, Messseite des Blindtests)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 11:27:13 CEST (date). Plan
  geschrieben ab 11:39:59 CEST (date), waehrend und nach den Rauchlaeufen (Abschnitt 2), vor jeder echten Rechnung.
  Zeitbox 90 min (bis 12:57:13 CEST).
- Ordner: lokal coordination/runden-v3/RUNDE-31/phase-3d-blind/ (code/, lauf-69/); .69:
  /home/fmh/fmhc-physics-remote/runde31-phase-3d-blind/ (Code-Kopien, rauch/, rauch2/, lauf/).
- Markierungen: [K] Wortlaut der KARTE, [A] Festlegung des Code-Agenten (nicht von der Leitung), [L] Vorgabe der Leitung
  im Auftrag (nicht in der Karte).
- **Blindheit:** Nicht gelesen: Codex' versiegelte Datei, BASELINE-VERSIEGELT.json, nichts unter
  coordination/resonance-20260930/. Vorsorglich ebenfalls nicht gelesen: PROTOKOLL-VORSCHLAG-AN-CODEX.txt im
  Rundenordner. Gelesen: KARTE.md; RUNDE-13/leiter3d-praez (KARTE, PLAN, ERGEBNIS, Code, start.sh); RUNDE-24/leiter-beta
  (KARTE, PLAN, ERGEBNIS, Skripte, ein Lauflog); RUNDE-26/phase-3d/lauf-69/auswertung-b05.json und -b1.json (Lagen, R,
  rho); der R-Teil von RUNDE-26/phase-3d/code/phase_3d.py (Konvention des Halbhoehenradius). KARTE und ERGEBNIS von
  RUNDE-26 habe ich nicht gelesen.

## 1. Karte (bindend, unveraendert) [K]

- beta = 1/2: die Sprossen n = 16, 17, 18 der radialen l = 0-Leiter, anschliessend an n = 15 bei eps = 0,028469
  (omega^2 = 0,528469).
- beta = 1: die drei Sprossen unterhalb der kleinsten bekannten bei eps = 0,030879 (omega^2 = 0,780879), fortlaufend
  nach kleinerem eps.
- Suchfenster nur aus den bekannten Sprossen und dem Abstand in 1/eps, z. B. bekannte letzte Lage plus k * b, Fenster
  +-b/2. Genau eine Sprosse je Fenster erwartet; die Umlaufzahl wechselt.
- Code RUNDE-13/leiter3d-praez/bic2_3d_praez.py bzw. RUNDE-24/leiter-beta/; Sprossen per Nullstellensuche in omega^2.
- Ausgabe je Sprosse: omega_n^2, eps_n, 1/eps_n, Umlaufzahl, Halbhoehenradius R_n, rho_n, Unsicherheit aus zwei
  Gitterweiten und der Bisektionsgenauigkeit.

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| PB0 | Kontrolle: Der Code findet die bekannte Sprosse n = 15 (beta = 1/2) und eps = 0,030879 (beta = 1) mit \|Delta omega^2\| < 1e-6 wieder | 85 % |
| PB1 | In jedem der sechs Fenster gibt es genau eine Sprosse, mit wechselnder Umlaufzahl | 80 % |

## 2. Rauchlaeufe an den bekannten Sprossen (vor dem Einfrieren; ausserhalb der echten Fenster) [L, A]

- Auftrag der Leitung: "Laufzeit vorab im Rauchlauf messen (ausserhalb der echten Fenster, z. B. an der bekannten
  Sprosse als PB0-Kontrolle)" [L]. Fenster u_bekannt +- 0,4 b (5 Startzeilen); sie beruehren die echten Fenster
  (ab u_bekannt + 0,5 b) nicht.
- **Rauchlauf 1** (code/rauch.sh, Code Version 1 = code/bic2_3d_suche_v1.py), .69, cpu und cpu2, 09:38:53 bis
  09:48:58 UTC, alle rc = 0. Befunde (nicht blind fuer alles Folgende):
  - beta = 1, k = 1: je Zeile genau eine Nullstelle von L(y_b); Wechsel von s; Wurzel h = 0,04 0,780879830, h = 0,02
    0,780879853 (Differenz 2,3e-8); Rechteck aufgeloest, Umlauf +1 (beide Stufen). Profil 13,7 s (h = 0,04) bzw. 23,5 s
    (h = 0,02), Zeile 9 bis 43 s.
  - beta = 1/2, n = 15: Kernwachstum am Ast 0,9e11 bis 2,7e11. Der Rest L(y_b) an der Illinois-Nullstelle war
    ~5e-8, so gross wie s selbst (1e-8 bis 7e-8): s war so nicht verlaesslich (h = 0,02 fand in der Startklammer keinen
    Wechsel mehr). Das Rechteck (eine Seite fast auf der Wurzel) war nach 30 Runden nicht aufgeloest (Sprung 3,14 rad).
- **Daraus Version 2** (code/bic2_3d_suche_v2.py, Abschnitt 4) und **Rauchlauf 2** (code/rauch2.sh, cpu3 und cpu4,
  Start 09:47 UTC): je bekannte Sprosse h004, u004 (Startzeilen von h004; nur Rauchlauf), h002 wie im Plan. Die ersten
  Zeilen zeigen bei beta = 1/2 korrigiertes s 3,5e-8 und 2,6e-8 gegen unkorrigiert 1,1e-6 und 2,6e-8; bei beta = 1
  sind beide gleich (relativ 1e-4).
- **PB0 wird auf Rauchlauf 2 ausgewertet** (h002-Laeufe; Code Version 2 unveraendert, gleiche sha256). Die Rechtecke an
  den bekannten Sprossen fuer PB1(c) rechnet die eingefrorene Kette neu (pb0-*-u004, Rechteckzeilen x* +- d wie
  unten), weil die u004-Laeufe des Rauchlaufs 2 noch die Startzeilen benutzen.

## 3. Fenster [A]

- u = 1/eps, eps = omega^2 - omega_min^2 mit omega_min^2 = 1 - 1/(4 beta) (0,5 bzw. 0,75).
- Schritt b = b_letzt = der zuletzt gemessene Schritt in u (Auftrag der Leitung [L]; die Karte nennt b_inf als Beispiel).
  - beta = 1/2: b = 1/0,028469 - 1/0,03047 = 2,306760 (u_15 = 35,125926).
  - beta = 1: b = 1/eps_(k=1) - 1/eps_(k=2) = 32,384166 - 29,787745 = 2,596420, mit den genauen Lagen aus
    RUNDE-26/auswertung-b1.json (eps 0,0308792886 und 0,0335708523).
- Fenster k = 1, 2, 3: [u_bekannt + (k - 1/2) b, u_bekannt + (k + 1/2) b]; lueckenlos aneinander.

| Fenster | beta | u-Fenster | omega^2-Bereich | Mitte omega^2 | rho_ref in der Mitte, Steigung | d (Rechteck) |
|---|---|---|---|---|---|---|
| b05-n16 | 1/2 | 36,279306 .. 38,586067 | 0,5259161 .. 0,5275639 | 0,526715 | 1,555432; 1,07 | 6,6e-4 |
| b05-n17 | 1/2 | 38,586067 .. 40,892827 | 0,5244542 .. 0,5259161 | 0,525164 | 1,553773; 1,07 | 5,8e-4 |
| b05-n18 | 1/2 | 40,892827 .. 43,199587 | 0,5231484 .. 0,5244542 | 0,523783 | 1,552296; 1,07 | 5,2e-4 |
| b1-k0 | 1 | 33,682376 .. 36,278796 | 0,7775643 .. 0,7796891 | 0,778587 | 1,800790; 0,86 | 8,5e-4 |
| b1-km1 | 1 | 36,278796 .. 38,875217 | 0,7757233 .. 0,7775643 | 0,776612 | 1,799091; 0,86 | 7,4e-4 |
| b1-km2 | 1 | 38,875217 .. 41,471637 | 0,7741129 .. 0,7757233 | 0,774892 | 1,797612; 0,86 | 6,4e-4 |

- rho_ref nur zur Wahl des Zielasts (dichtes Band +-0,04): lineare Fortsetzung in eps aus den bekannten rho (beta = 1/2:
  n = 7 bis 10 aus RUNDE-13, Steigung 1,00 bis 1,04, fortgesetzt 1,07; beta = 1: k = 1 bis 3, Steigung 0,84 bis 0,85,
  fortgesetzt 0,86). Keine Lagevorhersage.
- d = 0,4 * b * eps_Mitte^2 (0,4 des erwarteten Sprossenabstands in omega^2 an der Fenstermitte): halbe Breite des
  Umlauf-Rechtecks um die gefundene Wurzel. Bekannte Sprossen: d = 7,5e-4 (n = 15), 9,9e-4 (k = 1).
- Namen: n16, n17, n18 (beta = 1/2); k0, km1, km2 (beta = 1, Fortsetzung der R24-Zaehlung k = 1 .. 8 nach kleinerem eps:
  k = 0, -1, -2). Die Leiternummer bei beta = 1 ist laut R24 nur vorlaeufig (dort k = 1 ~ n = 12) und wird nur berichtet.

## 4. Verfahren (Kommando suche in code/bic2_3d_suche_v2.py) [A]

- Code: Kopie von RUNDE-13/leiter3d-praez/bic2_3d_praez.py (sha256 ba86ae6a..., = RUNDE-24-Kopie). Physik unveraendert
  (Profile, Gleichungen, direkt_m, praez_W, praez_illinois, praez_rechteck). Aenderungen mit "SUCHE31" markiert, Diff in
  code/bic2_3d_suche_v2.diff: lin_multi mit optional festem r_m; Kommando suche; Hilfen hermite_wurzel, r_wand.
- **Startzeilen:** Fenster-Modus 5 Zeilen gleichabstaendig in u (Abstand b/4, Raender eingeschlossen); Klammer-Modus
  "eng" 2 Zeilen x* +- klammer_halb um die Wurzel einer frueheren Datei. Je Lauf fester Aussenrand R (groesster
  Einzelrand der Startzeilen: f(R) = f_rand f0, f_rand 1e-8 bei h = 0,04 und 1e-6 bei h = 0,02 wie bic2 FRAND; plus
  r_zusatz) und fester Anschluss r_m (Median R_halb der Startzeilen).
- **Je Zeile:** Profil (Schritt h/2); rho-Abtastung 1000 Punkte im ganzen Fenster [1 - omega + 0,002; 1 + omega - 0,002]
  plus 801 Punkte in rho_ref +- 0,04; je Vorzeichenklammer von L(y_b) ein Zoom (199 innere Punkte, ein Stapel), dann
  Illinois bis Endklammer 1e-11 (relativ); Zielast = konvergierte Nullstelle naechst rho_ref im Band.
- **s an der Nullstelle (Version 2):** Zweipunkt-Interpolation: W = L(y_a) + i L(y_b) an rho_f -+ 1e-8, s = Re W dort,
  wo die Gerade durch die zwei Punkte Im W = 0 hat. Grund (Rauchlauf 1): L(y_a) und L(y_b) haengen nahe der Nullstelle
  beide affin von derselben schnell veraenderlichen Groesse ab; der Rest L(y_b)(rho_f) verfaelscht das unkorrigierte s um
  dL(y_a)/drho * delta rho. Der unkorrigierte Wert wird als s_roh mitgeschrieben.
- **Wechsel:** jedes Paar benachbarter Startzeilen mit s_i * s_(i+1) < 0 auf dem Zielast; Ast konsistent, wenn beide
  Nullstellen dieselbe Richtung von L(y_b) haben und |Delta rho| <= 0,03.
- **Nullstellensuche in omega^2:** Illinois auf s(omega^2) in der Startklammer, jeder Schritt mit neuem Profil; je
  Schritt rho-Abtastung 100 Punkte grob plus 201 Punkte in +-2e-4 um das zwischen den Klammerenden interpolierte rho.
  Ende bei Klammer <= 1e-9 oder 14 Schritten oder Zeitnot (Budget 560 s, Reserve 40 s). Lage omega*^2 = lineare
  Interpolation von s zwischen den Endpunkten der Endklammer; rho*, R* ebenso. Bisektionsgenauigkeit = Endklammerbreite.
- **Umlauf (Lauf u004):** praez_rechteck (unveraendert) auf den Zeilen x* +- d (Klammer-Modus eng aus h004, ohne
  Illinois), rho-Mitte rho*, halbe Hoehe drho = min(0,03; max(0,01; 2 |Aststeigung| d)), 60 Punkte je rho-Seite, bis 50
  Halbierungsrunden. Berichtet: Umlauf aus der Phase (aufgeloest: groesster Sprung < 0,4 rad) und aus der
  Kreuzungszaehlung (praez_rechteck "umlauf_kreuzung", 1/2 Summe sgn L(y_a) sgn Delta L(y_b) an den Wechseln von L(y_b)).
  - Festlegung: **Massgeblich ist die Kreuzungszaehlung**; die Phase wird berichtet. Grund (Rauchlauf 1): Bei beta = 1/2
    laeuft W auf den rho-Seiten so nah an 0 vorbei (Breite ~|s|/|dL(y_b)/drho|, bei n = 15 ~1e-13 bis 1e-14), dass die
    Halbierung an die Rechengenauigkeit von rho stossen kann.
- **Halbhoehenradius:** R_n in der Konvention von RUNDE-26 (S(R) = S_c/2, S_c = 1/(2 beta); Hermite auf dem Profil wie
  RUNDE-26 R_bic2), dazu R_halb nach bic2 (S(R) = S(0)/2); beide an omega*^2 linear interpoliert. rho_n = rho*.

## 5. Laeufe je Sprosse [A]

- **h004:** h = 0,04, Fenster-Modus, Illinois, ohne Rechteck.
- **h002:** h = 0,02, Klammer-Modus eng: x*(h004) +- 1e-5, neu gerechnet auf h = 0,02; die Klammer muss auf h = 0,02
  selbst einen Wechsel zeigen; Illinois wie oben. Begruendung: Laufzeit (ein Fenster-Lauf auf h = 0,02 kaeme an 600 s).
- **u004:** h = 0,04, Klammer-Modus eng: x*(h004) +- d, kein Illinois, Rechteck.
- **rand:** Randprobe h = 0,04, Klammer-Modus eng x*(h004) +- 1e-5, Aussenrand R + 20, fuer b05-n18 und b1-km2 (groesste
  Baelle). Berichtet: Lageaenderung gegen h004.
- Eine Stufe h = 0,01 fehlt (wie RUNDE-13 und RUNDE-24).

## 6. Regeln (mechanisch, vor jeder echten Rechnung festgelegt) [A]

- **PB0 je bekannte Sprosse:** eingetroffen, wenn der Lauf h002 aus Rauchlauf 2 eine Wurzel mit Endklammer <= 1e-9 hat
  und |omega*^2 - x_ref| < 1e-6, x_ref = 0,528469 (beta = 1/2) bzw. 0,780879 (beta = 1), die Kartenwerte. PB0
  eingetroffen = beide. Berichtet, nicht entscheidend: h004, Abstand zum R24-Wert 0,7808792886, R und rho gegen RUNDE-26
  (R 25,160632 bei 0,528469; R 16,598747 bei 0,7808792886; rho 1,8027610 bei k = 1; bei n = 15 kein rho bekannt).
- **PB1 je Fenster** (alle Bedingungen):
  - (a) h004: genau ein Wechsel von s zwischen den 5 Startzeilen, Ast konsistent;
  - (b) h004 und h002: Wurzel mit Endklammer <= 1e-9; beide Lagen auf 1e-6 gleich;
  - (c) u004: Wechsel von s zwischen x* - d und x* + d und Umlauf (Kreuzung) +-1;
  - (d) je beta wechseln die Umlaeufe (u004, Kreuzung) in der Folge bekannte Sprosse (pb0-*-u004), Fenster 1, 2, 3 ab.
  - PB1 eingetroffen = (a) bis (c) in allen sechs Fenstern und (d) fuer beide beta. Faellt ein Lauf aus (rc != 0,
    Zeit): gewertet wird, was die suche.json enthaelt; was fehlt, zaehlt als nicht erfuellt.
- **Unsicherheit je Sprosse:** unsicherheit_omega2 = |omega*^2(h002) - omega*^2(h004)| + groessere Endklammerbreite der
  beiden Stufen; in 1/eps: unsicherheit_omega2 / eps^2. Daneben berichtet: Randprobe und Rauschmass
  1e-15 * groesster Einzelterm von L(y_a) / |ds/domega^2|.
- **Berichtete Lage:** h002.

## 7. Ausgabe

- lauf-69/sprossen.json (per jq aus den suche.json): je Sprosse beta, Index (n = 16, 17, 18 bzw. k = 0, -1, -2), omega2,
  eps, inv_eps, Umlauf, R_halb (RUNDE-26-Konvention), R_halb_S0, rho, unsicherheit_omega2, unsicherheit_inv_eps,
  gitter_vergleich (beide Stufen, Differenz, Endklammern, Randprobe), Kernwachstum am Kandidaten.
- ERGEBNIS.md wie RUNDE-24/leiter-beta/ERGEBNIS.md; keine Deutung gegen eine Vorhersage (Vergleich macht die Leitung).

## 8. Laufliste (.69, kleintest.sh; Einheiten r31pb-*; code/start.sh, einmal per nohup)

| Spur | Kette |
|---|---|
| cpu6 | b05-n18-h004, -h002, -u004, -rand |
| cpu2 | b1-km2-h004, b1-km1-h004, b1-km2-h002, b1-km1-h002, b1-km2-u004, b1-km2-rand |
| cpu | b05-n16-h004, -h002, -u004, pb0-b05-u004 |
| cpu3 | b05-n17-h004, -h002, -u004 (nach Rauchlauf 2 auf cpu3) |
| cpu4 | b1-k0-h004, -h002, -u004, pb0-b1-u004, dann b1-km1-u004 (wartet auf das Ende von b1-km1-h004) |

- Zeiten (Rauchlauf 1, h = 0,04): Profil ~14 s, Zeile 9 bis 35 s, Illinois-Schritt ~22 s; h = 0,02 etwa doppelt.
  Geschaetzt: h004 5 bis 7 min, h002 4 bis 6 min, u004 2 bis 3 min.
- Nach dem Einfrieren keine Aenderung an Plan, Code und Skripten; Abweichungen offen mit Grund und Zeit im ERGEBNIS.

## 9. Code und Skripte (sha256, vor dem Einfrieren)

- bic2_3d_suche_v2.py 6beabc3f0d499df31a20c21fc9a35a2dc028117be5df05badf7863c22eb53c71 (lokal = .69)
- bic2_3d_suche_v1.py 3eb8fd8d02c0e526a34520e95f94439fcb0143390de60db07ab0d22c47fb4303 (nur Rauchlauf 1)
- rauch.sh fff753864bc9f323bf03a75937dd1769b6f9e8bd4276a0bf32138eb0c48dcf65
- rauch2.sh f2e09062a5b60ca2c047b56e2b58127357e53ec760f21b1964ceaebc9d4330e8
- bic2_3d_suche_v2.diff 48186dc3c2fbc873cfeb50dab760681d7fc1af0464007710922e07d5eabe436f
- start.sh af6a07a54d012c021e99e3581974a51317efc6094c0a1e5e593a6f975be2534e
- Rauchlauf 2 lief beim Einfrieren noch (cpu3, cpu4); erste Wurzelschritte bei n = 15 (h004): s ~ 1e-11 um
  0,5284692, Rauschen von s dort ~5e-12 (nicht blind fuer die Unsicherheitsangaben).
