# VERSCHRAENK-DIM-1: Plan des Code-Agenten (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:48:53 CEST (date), Zeitbox 75 min.
  Plan geschrieben ab 19:02:11 CEST (date), vor jeder Rechnung zu S_D oder D*.
- Gelesen: KARTE.md (ganz); Laufform aus RUNDE-37/paar-regge-1/ (PLAN.md, EINGEFROREN-SHA256.txt, lauf-69/*.log).
  Finns voller Wortlaut in RUNDE-37/dim-leiter-qball-1/KARTE.md nicht gelesen (fuer die Rechnung nicht noetig).
- Ordner: lokal RUNDE-37/verschraenk-dim-1/ (code/, lauf-69/); .69: /home/fmh/fmhc-physics-remote/verschraenk-dim-1/
  (code/, lauf/, rauch/).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik von Hand (nicht gegengelesen), [L] Gedaechtnis/Literatur ohne
  Abruf, [S] an der Quelle gelesen, [H] Hypothese, [F] Festlegung dieses Plans (nicht aus der Karte), [D] Diagnose
  (beschreibend, ohne Urteil).
- Vorhersagen und Wahrscheinlichkeiten der Karte (VD0 85 %, VD1 15 %, VD2 50 %) bleiben unveraendert.
- Literatur: kein arXiv-Abruf (0 von 2). quellen/ bleibt leer.

## 1. Schreibtisch der Leitung nachgeprueft (Fehler zuerst)

**F1, Luecke der Karte [M]: Der D-Bereich 1 bis 24 enthaelt das Maximum fuer N = 10^80 nicht.**
- Nach der Karte selbst gilt D* ~ (ln N)/2; fuer N = 10^80 ist (ln N)/2 = 92,1. Mit D <= 24 laege das Maximum am Rand
  D = 24 und waere kein Maximum.
- Abhilfe [F]: Tabelle S_D(m) wie verlangt fuer D = 1 bis 24; die Suche nach D* laeuft ueber D = 1 bis 200 (DMAX).
  Liegt ein D* am Rand (D = 1 oder 200), wird es als "Rand" gemeldet und nicht als Maximum gezaehlt.

**F2, Ungenauigkeit [M]: S_D faellt fuer grosses D wie ln(D)/D^2, nicht wie D^(-2).**
- Grossmassen-Naeherung (zwei gekoppelte Oszillatoren; fuehrende Ordnung): Fuer eine Kette mit Platzterm w = M^2 + 2
  und Kopplung 1 ist die Halbketten-Verschraenkung S_1 ~ (1 + ln(16 w^2)) / (16 w^2).
- Mit w ~ m^2 + 2D folgt S_D ~ (1 + ln(64 D^2)) / (64 D^2). Die Bedingung d ln S_tot / dD = 0 gibt
  D* ~ (ln N)/2 / (1 - 1/ln(64 D*^2)), also 8 bis 17 % ueber (ln N)/2. Die Karte nennt (ln N)/2 "grob"; das stimmt.

**F3, Idealisierung [M]: S_tot(D) = N^((D-1)/D) S_D(m) ist "Dichte im unendlichen Gitter mal Flaeche".**
- Die Kantenlaenge L = N^(1/D) wird bei grossem D klein (N = 10^6: L = 5,6 bei D = 8, L = 2 bei D = 20). In einem
  offenen Wuerfel liegen dann fast alle Randplaetze an Kanten und Ecken. Die Formel gilt sinngemaess fuer periodische
  Querrichtungen (Torus). Sie wird wie in der Karte gerechnet; L wird je D* mit ausgegeben.

**F4, Kleinigkeit [M]:** "m_eff^2 wird scharf um m^2 + 2(D-1)" gilt nur relativ (relative Breite 1/sqrt(2(D-1))).
Die absolute Breite sqrt(2(D-1)) waechst.

**Bestaetigt [M]:**
- Zerlegung in 1D-Ketten je Querimpuls bei verschiebungsgleichem Schnitt, mit m_eff^2 = m^2 + Summe 4 sin^2(k_i/2).
- Querterm t = 2 - 2 cos k, k gleichverteilt: Mittel 2, Varianz 4 E[cos^2 k] = 2.
- Randplaetze L^(D-1) = N^((D-1)/D); Monotonie von S_D ist ableitbar: Fuer jede Stichprobe gilt
  T_(D+1) = T_D + t >= T_D, und S_1 faellt mit der Masse.

## 2. Was ich vorab schon weiss (Offenlegung, Ableitbarkeit) [M]

- **S_1 klein M [M, H-CTM]:** Nach der Eckentransfermatrix-Form (Peschel/Chung, [L] aus dem Gedaechtnis, nicht
  abgerufen) hat die Halbkette die Einteilchen-Niveaus eps_j = (2j + 1) eps mit eps = pi K(k')/K(k). Meine Annahme
  ueber den Modul: k = kleinere Wurzel von k + 1/k = 2 + M^2. Sie gibt fuer kleines M die Steigung -1/6 und fuer grosses M
  die Zwei-Oszillatoren-Grenze aus F2. Von Hand: S_1(0,01) ~ 0,767 und S_1(0,1) ~ 0,383, also S_1 ~ (1/6) ln(1/M) mit
  Konstante nahe 0. Sekante zwischen 0,01 und 0,1: rund -0,167. Teil b von VD0 ist damit vorab fast sicher.
  Die Formel laeuft im Lauf als Gegenprobe mit; sie ist keine Quelle.
- **D* von Hand [M]** (Grossmassen-Naeherung aus F2, m = 0,1; bei kleinem D zu klein, daher eher zu kleines D*):
  N = 10^3: D* = 4 (bis 5); 10^6: 8 (7 bis 9, sehr flaches Maximum, ln S_tot bei D = 7, 8, 9 innerhalb 0,02);
  10^9: rund 12; 10^12: rund 15 bis 16; 10^80: rund 100.
- **Folgen fuer die Urteile:** VD1 (D* = 3 oder 4 bei N = 10^6) erwarte ich als nicht eingetroffen. VD2 (affin in ln N
  auf 10 %) erwarte ich als eingetroffen; das ist nach F2 weitgehend ableitbar (D* ~ (ln N)/2 mal langsam veraenderlicher
  Faktor). Der Lauf liefert die genauen ganzzahligen D*, die Schaerfe und die Massenabhaengigkeit.

## 3. Abweichungen von der Karte und Festlegungen [F]

- D-Bereich fuer D*: 1 bis 200 (F1). Tabelle: D = 1 bis 24.
- Massen m = 0,01, 0,1, 1; N = 10^3, 10^6, 10^9, 10^12, 10^80 (Karte).
- Mittel ueber k: D = 2 und 3 deterministisch (Gauss-Legendre, gestuft), D >= 4 Monte Carlo mit Fehlerangabe (Karte
  erlaubt beides). Monte Carlo laeuft fuer alle D >= 2 mit, damit D = 2, 3 als Kontrolle dienen.

## 4. Verfahren

**S_1(M), Halbkette [Karte Auftrag 1]:**
- Unendliche Kette mit omega_q^2 = M^2 + 4 sin^2(q/2). Korrelationen X_r = <phi_0 phi_r>, P_r = <pi_0 pi_r> per FFT
  auf einem Ring mit nq >= max(2^14, 64 ell) Plaetzen (Fehler ~ exp(-kappa nq), vernachlaessigbar).
- Block aus ell Plaetzen in der unendlichen Kette (zwei Raender): S_1 = S_Block/2.
  ell = max(48, ceil(16/kappa)), kappa = 2 arsinh(M/2) = inverse Korrelationslaenge. Fuer M = 0,01: ell = 1601.
- Entropie (Peschel): X = L L^T (Cholesky), nu^2 = Eigenwerte von L^T P L,
  S = Summe[(nu + 1/2) ln(nu + 1/2) - (nu - 1/2) ln(nu - 1/2)]; nu^2 < 1/4 aus Rundung wird auf 1/4 gesetzt.
- Stuetzstellen: x = ln(M^2) gleichabstaendig von ln(10^-4) bis ln(10^3), 421 Punkte (60 je Dekade in M^2; die
  Kartenmassen liegen auf dem Gitter und werden zusaetzlich genau gerechnet).
- Konvergenzprobe in der Laenge: jede 20. Stuetzstelle (und die letzte) sowie die drei Kartenmassen mit 1,5 ell.
- Interpolation: kubischer Spline von ln S_1 gegen ln(M^2). Splineprobe: 42 Mittelpunkte direkt gerechnet.

**S_D(m) [Auftrag 2]:** S_D(m) = Mittel ueber k_2..k_D von S_1(sqrt(m^2 + T)), T = Summe(2 - 2 cos k_i).
- D = 1: S_1(m) direkt.
- D = 2, 3: Gauss-Legendre auf [0, pi], 40 bzw. 60 Paneele, geometrisch zu k = 0 verfeinert (kleinstes Paneel 10^-4),
  16 bzw. 24 Knoten je Paneel; D = 3 als Tensorprodukt. Fehlerangabe: |fein - grob|. Dazu D = 2 mit scipy quad.
- D >= 4 (und als Kontrolle D = 2, 3): Monte Carlo, k_i gleichverteilt in [0, pi], gemeinsame Zufallszahlen fuer alle D
  (T_D als kumulierte Summe), 32 Bloecke zu 2^17 Stichproben, Saat 20261004. Fehler: Streuung der Blockmittel / sqrt(32).
  S_1 per linearer Interpolation in einer Tabelle des Splines (200001 Punkte).

**Kontrolle der Zerlegung [Auftrag 3]:**
- 2D: L1 = 48 Plaetze in x_1 (Dirichlet-Enden), Lq = 32 periodisch. 3D: L1 = 24, Lq = 10 x 10 periodisch.
- Direkt: volle Gitter-Matrix K = m^2 + Laplace, X = K^(-1/2)/2, P = K^(1/2)/2, Halbraum x_1 < L1/2, Peschel.
- Zerlegung auf demselben Gitter: Summe ueber die diskreten Querimpulse k = 2 pi j/Lq der Halbketten-Entropien der
  Dirichlet-Kette mit L1 Plaetzen und Platzterm m^2 + T(k) + 2.
- Alle drei Massen.

**S_tot und D* [Auftrag 4]:** ln S_tot(D) = (1 - 1/D) ln N + ln S_D, D = 1..200.
- D* = ganzzahliges argmax.
- D*_stetig = Scheitel der Parabel durch D* - 1, D*, D* + 1 (in ln S_tot).
- Schaerfe: S_tot(D* +- 1)/S_tot(D*) und das 90-%-Band {D: S_tot >= 0,9 S_tot(D*)}.
- Stabilitaet: 400 Bootstrap-Ziehungen ueber die 32 Monte-Carlo-Bloecke (D = 1..3 fest); Anteil mit gleichem D*.

## 5. Zusaetzliche Kontrollen (berichtet, nicht Teil der Urteile)

- Laengenprobe S_1: relative Aenderung bei 1,5 ell, Erwartung < 10^-8.
- Splineprobe: relative Abweichung an Mittelpunkten, Erwartung < 10^-6.
- CTM-Gegenprobe (H-CTM aus Abschn. 2): Abweichung zur Peschel-Rechnung. Stimmt sie auf < 10^-8, ist die Formel als
  Kontrolle bestaetigt [E]; stimmt sie nicht, ist nur meine Annahme ueber den Modul falsch, die Rechnung bleibt.
- Monte Carlo gegen Gauss-Legendre fuer D = 2, 3: |z| <= 3.
- quad gegen Gauss-Legendre fuer D = 2: relativ < 10^-6.
- Beschreibend [D]: S_D / Grossmassen-Naeherung (F2); S_D / S_1(sqrt(m^2 + 2(D - 1))) als Mass der Gleichfoermigkeit;
  direkte Rechnung je Randplatz gegen S_D aus dem unendlichen Gitter.

## 6. Urteile

| Nr | Karte | nach Plan [F] | nach Kartenwortlaut [F] |
|---|---|---|---|
| VD0 | Zerlegung < 1 %; Steigung -1/6 auf 5 %; S_D monoton fallend | (a) max. relative Abweichung direkt gegen Zerlegung auf demselben Gitter < 1 % (D = 2, 3, alle drei m); (b) Steigung der Ausgleichsgeraden S_1 gegen ln M ueber die 121 Stuetzstellen M in [0,01; 0,1] innerhalb 5 % von -1/6; (c) S_D streng fallend fuer D = 1..24, alle drei m; eingetroffen, wenn (a), (b) und (c) | wie Plan, aber (b) als Sekante zwischen den Kartenmassen 0,01 und 0,1 |
| VD1 | N = 10^6, m = 0,1: D* = 3 oder 4 | ganzzahliges D* in {3, 4} | dasselbe |
| VD2 | D*(N) linear in ln N, Anpassung ueber die fuenf N auf 10 % | m = 0,1: affine Ausgleichsgerade D*_stetig = a + b ln N; jede relative Abweichung |D* - Fit|/D* <= 10 % | Masse in der Karte nicht genannt: ganzzahliges D*, affine Ausgleichsgerade, je Masse <= 10 %; alle drei ja = eingetroffen, alle nein = nicht eingetroffen, sonst uneindeutig |

- Liegt ein D* am Rand (1 oder 200), gilt VD2 fuer diese Masse als nicht eingetroffen und wird als Rand gemeldet.
- Die Urteile rechnet der eingefrorene Code (Modus auswertung). Ich uebernehme sie und pruefe sie von Hand gegen die Tabelle.

## 7. Laeufe und Ablauf

- Nur .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu und cpu2 (cpu6, cpu7 nicht, da
  ATEM-NETZ-1 laeuft), 1 Thread, je Lauf <= 10 min (RuntimeMaxSec = 600 im Starter).
- Reihenfolge:
  1. Rauchtest (Modus rauch, Kleinstgroessen, gibt nur Laufzeiten aus; seine Dateien werden nicht angesehen).
  2. Einfrieren: dieser Plan und code/vd.py (sha256 in EINGEFROREN-SHA256.txt).
  3. s1 (cpu) und direkt (cpu2) parallel; dann sd (cpu); dann auswertung und bild.
  4. Dateien nach lauf-69/ kopieren, sha256 auf beiden Seiten.
- Keine Aenderung an Plan, Urteilsregeln oder Code nach dem Einfrieren. Noetige Aenderungen nur als datierter Nachtrag
  am Ende dieses Plans mit Begruendung und neuem Hash, und nur vor der ersten Sicht auf S_D bzw. D*; danach nur
  Selbstanzeige.
