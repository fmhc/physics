# LEITER-BETA: Plan (Runde 24, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 01:24:10 CEST (date). Plan
  geschrieben ab 01:37:36 CEST (date), nach den Rauchlaeufen (Abschnitt 2), vor jedem echten Lauf. Zeitbox 120 min (bis
  03:24:10 CEST).
- Ordner: lokal coordination/runden-v3/RUNDE-24/leiter-beta/; .69: /home/fmh/fmhc-physics-remote/runde24-leiter-beta/
  (Code-Kopie, lauf/, rauch/).
- Markierungen: [K] Wortlaut der KARTE, [A] Festlegung des Code-Agenten (nicht von der Leitung), [L] Vorgabe der Leitung
  im Auftrag (nicht in der Karte).

## 1. Karte (bindend, unveraendert) [K]

- Test: 3D radial, l = 0, U = S - S^2 + beta S^3 mit beta = 1; Code RUNDE-13/leiter3d-praez/bic2_3d_praez.py (--beta);
  Verfahren wie RUNDE-12/13. Suchbereich eps in [0,03; 0,08] mit eps = omega^2 - 3/4; rho entlang 1,7735 + c eps,
  c in [0,5; 2]; mindestens so fein wie RUNDE-12 fuer n >= 7 (4000 rho-Punkte), lokal um Kandidaten feiner; Rechtecke
  so klein, dass sie nur eine Sprosse enthalten.
- K0: Derselbe Code reproduziert bei beta = 1/2 die 3D-Sprosse n = 10 aus RUNDE-13 (omega^2 = 0,5423644, rho = 1,57218)
  auf 1e-5 in omega^2 und 1e-4 in rho.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LB0 | K0 bestanden | 85 % |
| LB1 | Bei beta = 1 mindestens vier aufeinanderfolgende Sprossen mit aufgeloestem Umlauf +-1 (abwechselnd) in eps [0,03; 0,08] | 55 % |
| LB2 | Alle Schritte 1/eps_(n+1) - 1/eps_n der gefundenen Folge liegen in [2,45; 2,80], die letzten zwei innerhalb +-3 % von 2,6186 | 50 % |
| LB3 | Alle gefundenen rho_n liegen in (rho_z(1), rho_z(1) + 1,5 eps_n) | 60 % |

- Bedeutung (vorab, Karte): LB1 und LB2 treffen ein -> die ebene Wandnullstelle sagt die radiale Leiter bei beta = 1 ohne
  Eichung voraus; RUNDE-10s offene Frage beantwortet [H, 3D, l = 0]. LB1 trifft nicht ein -> keine aufgeloeste
  Sprossenfolge im Bereich; entweder fehlt sie radial, oder das schmale Fano-Fenster macht sie numerisch unzugaenglich;
  beschreiben, mit dem besten Hinweis.
- rho_z(1) = 1,7734530718, b_inf(1) = 2,6186 (RUNDE-24/wand-beta/ERGEBNIS.md).

## 2. Rauchlaeufe vor diesem Plan (ungueltig fuer jede Wertung; offengelegt)

- rauch.sh, .69 (Spuren cpu3, cpu4), 23:28:45 bis 23:30:40 UTC, beide rc = 0. Parameter in keinem echten Lauf: 3 Zeilen,
  Abstand 3,3e-4 bzw. 7e-4 um x0 = 0,78513 bzw. 0,82017, n_rho 1000, n_dicht 1001 (+-0,06), h = 0,04, keine Pole.
- Befund (nicht blind fuer alles Folgende):
  - Je Zeile genau eine Nullstelle von L(y_b) im ganzen rho-Fenster, bei c = (rho_b - rho_z)/eps ~ 0,94 (eps 0,035)
    bzw. ~ 0,85 (eps 0,07); Steigung des Astes d rho_b/d omega^2 ~ 0,84 bzw. 0,68.
  - rauch-b: Vorzeichenwechsel von s bei omega*^2 = 0,819642, rho* = 1,832532, Rechteck (Zeilen 0,81947 bis 0,82087,
    rho* +- 0,01) aufgeloest (0,279 rad), Umlauf -1. Kernwachstum am Kandidaten 1,5e2.
  - rauch-a: kein Wechsel in drei Zeilen (s ~ -1,5e-5 bis -1,7e-5, flach); Kernwachstum ~3e4; Rechteck um die Mitte
    aufgeloest, Umlauf 0.
  - Zeiten (.69, h = 0,04): Profil bis 13,8 s, W-Punkt ~2 ms (R = 52), Nullstellensuche 18 bis 21 s, Rechteck 20 bis 26 s.
- Folge fuer den Plan: Die Sprosse bei ~0,8196 ist schon gesehen; Phase 1 und 2 rechnen sie mit eigenen Zeilen neu.

## 3. K0 (LB0) [K, Auslegung A]

- Laeufe k0-h004 und k0-h002: woertlich die Argumente von RUNDE-13 start.sh (G und N10), --h 0.04 bzw. 0.02.
- Bestanden [A], je Stufe: ein Vorzeichenwechsel von s auf dem Zielast mit |omega*^2 - 0,5423644| <= 1e-5 und
  |rho* - 1,57218| <= 1e-4, dessen Rechteck aufgeloest ist (groesster Sprung < 0,4 rad) mit Umlauf +-1 (|abs U - 1| < 0,1).
  K0 bestanden = beide Stufen bestanden. Die Bedingung "Umlauf +-1" ist ein Zusatz [A] (eine Sprosse im Sinne von RUNDE-13).
- Umsetzung k0.jq. Berichtet (nicht Regel): Abweichung der Zahlen gegen RUNDE-13 lauf-69/n10-h00x.
- Verfehlt K0: Die beta = 1-Ergebnisse werden berichtet, LB1 bis LB3 gelten dann als nicht auswertbar [A].

## 4. Phase 1: Grobsuche bei beta = 1, Stufe h = 0,04 (start1.sh)

- Fuenf Fenster in omega^2, je ein Aufruf praez; benachbarte Fenster teilen ihre Randzeile, damit jedes Paar
  benachbarter Zeilen in einem Aufruf liegt.

| Fenster | Zeilen | Abstand d | erste .. letzte Zeile | eps-Bereich | d / (b_inf eps_erst^2) | dichtes Band +- | rho0 bei x0 |
|---|---|---|---|---|---|---|---|
| g1 | 10 | 5,5e-4 | 0,78000 .. 0,78495 | 0,0300 .. 0,0350 | 0,233 | 0,027 | 1,814044 |
| g2 | 10 | 7,5e-4 | 0,78495 .. 0,79170 | 0,0350 .. 0,0417 | 0,234 | 0,032 | 1,821356 |
| g3 | 10 | 1,1e-3 | 0,79170 .. 0,80160 | 0,0417 .. 0,0516 | 0,241 | 0,039 | 1,831763 |
| g4 | 10 | 1,7e-3 | 0,80160 .. 0,81690 | 0,0516 .. 0,0669 | 0,244 | 0,051 | 1,847513 |
| g5 | 7 | 2,9e-3 | 0,81690 .. 0,83430 | 0,0669 .. 0,0843 | 0,248 | 0,064 | 1,867950 |

- Begruendung [A]: Der Zeilenabstand ist hoechstens ein Viertel des erwarteten Sprossenabstands b_inf eps^2 am
  kleinsten eps des Fensters. Zwischen zwei Sprossen liegen damit mindestens drei Zeilen; zwei Wechsel koennen nicht in
  dasselbe Zeilenintervall fallen, solange der wahre Abstand nicht unter ~0,3 b_inf eps^2 liegt.
- rho-Abtastung je Zeile: 5000 Punkte im ganzen Fenster [1 - omega + 0,002; 1 + omega - 0,002] (Abstand ~3,5e-4, so
  fein wie RUNDE-12 mit 3,6e-4) plus 2001 Punkte im dichten Band rho_ref +- dicht_halb, rho_ref = 1,77345 + 1,25 eps
  (Steigung 1,25); dicht_halb = 0,75 eps am Fensterende deckt c in [0,5; 2] (Abstand 2,7e-5 bis 6,4e-5).
- Gemeinsam: --pr-u-halb 0 (Rechteck nur zwischen den zwei Zeilen um den Wechsel, also hoechstens ein Viertel
  Sprossenabstand breit), --pole nein, sonst wie RUNDE-13 (u-n 60, u-runden 30, pr-drho 0,01, iter-wurzel 80,
  tol-wurzel 1e-13, budget 500, reserve 150).
- Spuren: cpu: k0-h004, dann g1; cpu6: k0-h002, dann g5; cpu2: g2; cpu3: g3; cpu4: g4. Ein Starter start1.sh per nohup.

## 5. Kandidaten (phase1.jq) [A]

- Kandidat = jeder Vorzeichenwechsel von s auf dem Zielast eines Phase-1-Fensters (ziel_wechsel), dazu jeder Wechsel auf
  einem anderen gepaarten Ast (neben_wechsel), dessen rho* im dichten Band liegt. Nummer k nach omega*^2 aufsteigend.
- Ausgabe lauf-69/kandidaten.json; die grobe Lage (omega*^2, rho*, Steigung) bestimmt die Phase-2-Zeilen.

## 6. Phase 2: je Kandidat zwei Stufen h = 0,04 und h = 0,02 (gen2.sh -> start2.sh)

- 7 Zeilen, Abstand 3e-4 um X = omega*^2 (grob, 6 Stellen), also X +- 9e-4. Der kleinste erwartete Sprossenabstand
  (eps = 0,03) ist 2,4e-3; das Fenster (1,8e-3) enthaelt hoechstens eine Sprosse.
- rho je Zeile: 5000 Punkte im ganzen Fenster plus 2001 Punkte in rho_ref +- 0,002 (Abstand 2e-6, weit unter 1e-5),
  rho_ref = R + S (x - X) mit S = Steigung des Zielasts aus Phase 1 (4 Stellen), R = rho* + S (X - omega*^2) (7 Stellen).
- Danach wie RUNDE-13: Illinois bis Klammer < 1e-13, s exakt an der Nullstelle, Rechteck um jeden Wechsel mit
  --pr-u-halb 3 (Zeilen i - 3 bis i + 4), rho* +- 0,01, 60 Punkte je rho-Seite, bis 30 Halbierungsrunden; Pole am
  Zielast als Zusatz (--pole ja), --budget 480, --reserve 150.
- Reihenfolge: Kandidaten mit omega*^2 in [0,78; 0,83] nach omega*^2 aufsteigend, dann die uebrigen; je Kandidat erst
  h = 0,02, dann 0,04; reihum auf cpu, cpu2, cpu3, cpu4, cpu6, je Spur nacheinander. start2.sh wird nach Phase 1 von
  gen2.sh mechanisch erzeugt und unveraendert gestartet.

## 7. Regeln (auswertung.jq, auswertung.sh) [A]

- **Stufe in Ordnung** (je Lauf): alle 7 Profile da; genau ein Wechsel von s auf dem Zielast; sein Rechteck aufgeloest
  (groesster Sprung < 0,4 rad) mit Umlauf +-1 (|abs U - 1| < 0,1); Kernwachstum am Kandidaten <= 1e8 (strenge Lesart
  wie RUNDE-13).
- **Sprosse** (aufgeloest): beide Stufen in Ordnung; omega*^2 und rho* stimmen zwischen den Stufen auf 1e-4; gleiches
  Vorzeichen des Umlaufs. Lage eps_n, rho_n und Umlauf aus h = 0,02. Sonst "unentschieden" bzw. "nicht gerechnet".
- **Folge:** Sprossen mit eps_n in [0,03; 0,08], deren Kandidatennummern k lueckenlos aufeinander folgen (kein anderer
  Phase-1-Kandidat dazwischen) und deren Umlaeufe abwechseln. Gewertet wird die laengste Folge (bei Gleichstand die mit
  dem kleineren eps).
- **LB1:** eingetroffen, wenn die gewertete Folge mindestens 4 Sprossen hat.
- **LB2:** Schritte 1/eps_n - 1/eps_(n+1) benachbarter Folgenglieder (n waechst mit fallendem eps). "Die letzten zwei" =
  die zwei Schritte mit den kleinsten eps (groesste n). Eingetroffen, wenn alle Schritte in [2,45; 2,80] liegen und die
  letzten zwei in [0,97; 1,03] x 2,6186. Bei weniger als 3 Folgengliedern nicht auswertbar = nicht eingetroffen.
- **LB3:** alle Sprossen mit eps_n in [0,03; 0,08] (nicht nur die Folge) erfuellen rho_z(1) < rho_n < rho_z(1) + 1,5 eps_n.
  Ohne Sprosse nicht auswertbar = nicht eingetroffen.
- **Bedeutung bei LB1 nicht eingetroffen:** belegt mit Kernwachstum, Halbierungsrunden, groesstem Sprung, s-Groesse,
  Stufendifferenz und (Zusatz) Polbreiten je Kandidat, ob die Leiter eher fehlt oder numerisch unzugaenglich ist.

## 8. Zeitplan und Grenzen

- Zeiten aus den Rauchlaeufen: Phase 1 je Fenster ~400 s (g5 ~260 s), K0 ~170 s und ~290 s wie RUNDE-13. Phase 2 je
  Kandidat ~250 s (h = 0,04) und ~450 s (h = 0,02); geschaetzt, nicht gemessen.
- Phase 2 laeuft hoechstens bis 03:05 CEST. Was dann nicht gerechnet ist, bleibt "nicht gerechnet" (bricht Folgen),
  und wird als offen berichtet. Kein Nachlauf ohne offen benannte Abweichung.
- Faellt ein Aufruf aus (rc != 0): gewertet wird, was die praez.json enthaelt (Zwischenspeicher nach jedem Schritt).
- Nach dem Einfrieren keine Aenderung an Plan, Code und Skripten; Abweichungen offen mit Grund und Zeit im ERGEBNIS.

## 9. Code und Skripte (sha256, vor dem Einfrieren)

- bic2_3d_praez.py ba86ae6a61eb31b3afbbefcd630771ae627dfcaaa33b9bd7903b768d44838e9b (= RUNDE-13, unveraendert; .69-Kopie
  gleich)
- start1.sh f0b6f6263ffaf8af54eff24c57312c5874239775d652c0dc8b447ecfe396c5e5
- gen2.sh 38b5a3699a29299eda045ec2f2f963d8136fad74f047b5d30632f68a303ae6a3
- phase1.jq c6fffe78f725a0364345f756ab7ad78154fea41a8de6d5457a39ad197c921c0d
- k0.jq 2b91cce60582d8310bde6e10f6cf73a2416a8dda38463c6b9a5f8f95003d3b60
- auswertung.jq 1a820dbc1106cfc973809ec2236609aa6ee7e2f136f12d27b3c7fef879b4bef6
- auswertung.sh d01de02896c8ccdae6da1e8efee0082e771177161af383945bd139470bf432d5
- rauch.sh ade1a6a9550a72af2340df3ef3096053848a2260e8ac09f19b43b202d2e5a637
- Die jq-Skripte sind lokal an synthetischen Daten und an RUNDE-13 n10 geprueft (Scratchpad, nicht abgelegt).
