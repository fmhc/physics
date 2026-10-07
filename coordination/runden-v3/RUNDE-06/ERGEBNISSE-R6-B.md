# Runde 6, Ernte B: 3D-Resonanz, KF-4, KF-5, RG-1 (Gegenlesen der Leitungseintraege)

- Beginn: 2026-09-30 03:46:34 CEST (date). Ende: siehe naechste Zeile (nach dem Schreiben mit date gemessen).
- Ende: 2026-09-30 04:04:59 CEST (date, nach dem Schreiben gemessen). Dauer rund 18,5 Minuten, Budget 45 Minuten.
- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung. Nur gelesen, nur diese Datei geschrieben. Explorativ (v3).
- Gegengelesen: RUNDE-06.md in der Fassung vom 2026-09-30 03:50:02 (Zeilennummern in Abschnitt 5 beziehen sich darauf).
- Gelesen: README.md; AUFTRAG-3D-RESONANZ.md, resonanz3d/PLAN.md, lauf-lokal/aus-*/ (pole, bruecke, bic-a bis -e,
  scan-l0-hoch, scan-l1-a/b), lauf-lokal/*.log, scan1d/ (w*.log, w*/bruecke_bericht.txt), lauf-69/LAUF1-8.log (inhaltsgleich
  mit aus-*/..._bericht.txt, fuer nlbic per diff geprueft), L4-BIC-LITERATUR.md; resonance-20260930/3D-POLE-CODEX.md,
  3D-OMEGA-SCAN-CODEX.md, OMEGA-SCAN-ACK-CODEX.txt, OMEGA-PEERBUS-RESULT.txt, HIGHERL-ERGEBNIS-CODEX.txt (Zeile l = 3),
  FESHBACH-ERGEBNIS-CODEX.txt (weil RUNDE-06.md ab Z. 164 daraus zitiert); AUFTRAG-KF4-KF5.md, kf4/PLAN.md,
  kf4/lauf-69/{statik, scan-langsam, scan-schnell, resonanz, kante}/ und LAUF1.log; kf5/PLAN.md, kf5/lauf-69/ausgabe/*.txt
  und LAUF1.log; KARTE-RG1-REGGE.md, regge/PLAN.md, regge/lauf-lokal/bahn/bericht.txt, h001/ und h0005/ (Kopf);
  ARBEITSFELD-claude-primary.md (nur die Zeile 03:20:24, per grep).
- Gesperrte Pfade nicht geoeffnet.
- Zeichen: "(abgel.)" = Quotient oder Differenz aus Berichtswerten, von mir im Kopf gebildet, keine Berichtszahl.
  "nicht im Bericht" = die Groesse steht in keinem gelesenen Bericht.
- Zu den .69-Logs: Die Syntaxfehler des Startskripts (Zeile 31) stehen in resonanz3d/lauf-69/LAUF1.log und LAUF2.log
  nach lin07b und nl07b. Alle Laeufe melden "code=exited/status=0"; das ist wie im Auftrag beschrieben und kein Befund.

## 1. Je Test

### 1.1 3D-Resonanz (Karte 3D-Resonanz, Vorhersagen V1 bis V12 in resonanz3d/PLAN.md, Abschnitt 3)

| Kennung | Vorhersage (PLAN, knapp) | Ergebnis (Bericht) | Urteil |
|---|---|---|---|
| V1 Nullmoden | l = 0, 1: \|D(2e)\|/\|D(e)\| = 4 +- 0,4 und \|D(0)\| << \|D(1e-3)\|; l = 2 etwa 1 | 0,7: 3,9998 / 4,0000 / 0,9999; l = 0: \|D(0)\| 3,964e-10 gegen \|D(0,001)\| 1,656e-5. Alle anderen omega^2: 3,9983 bis 4,0013 | getroffen |
| V2 rho_2 bei 0,7 | Re 0,15 (0,10 bis 0,20); 55 % gebunden, sonst schmale Resonanz knapp ueber der Kante, \|Im\| < 1e-3 | Polrechner: gebunden 0, l = 2 Umlauf 0 (Kante +-0,002 wird nicht durchsucht). zeitlin (.69): 0,163781 (dr 0,05), 0,163780 (dr 0,025), \|Im\| hoechstens 1,1e-6; Kante 0,163340 | getroffen (zweiter Zweig); nur zwei dr |
| V3 l = 0-Kompressionsmode | Re etwa 0,45 (0,30 bis 0,65), Im -0,1 bis -0,005 | 0,7: kein solcher Pol (l = 0: Umlauf 1, das ist der Pol bei 1,70). 0,6: 0,5710604 - 0,1137 i "(nicht konv.)" | verfehlt |
| V4 rho_0 | Re 1,68 (1,55 bis 1,83), Im etwa -3e-3 (-3e-4 bis -3e-2), 10- bis 500-mal breiter als 1D | 1,7018102190 - 1,468e-3 i (Stufe C); 21,9-mal breiter als 6,716e-5 (abgel.) | getroffen |
| V5 rho_1 | etwa 1,74 (1,60 bis 1,835), Re rho_0 + 0,05 bis 0,06, Breite aehnlich oder groesser | 1,7635198 - 3,657e-3 i; Abstand 0,0617 (abgel.) | getroffen (Abstand knapp ueber 0,06) |
| V6 l = 2 | kein v-dominierter Pol unter 1 + omega; darueber nur breite Pole mit \|Im\| > 1e-2 | 0,7: Umlauf 0. 0,8: nur 0,1917286 - 0,0457 i "(nicht konv.)". **0,6: schmaler Pol 1,6786834 - 2,911e-3 i unter 1 + omega = 1,7746** | teilweise |
| V7 mehr Pole in 3D | je l mindestens 2 Nullstellen im Kasten \|Im\| < 0,1 | Umlauf l = 0/1/2: 0,7: 1/1/0; 0,6: 1/2/1; 0,8: 1/1/1 | verfehlt |
| V8 Trend in omega | 0,6: rho_2 = 0,065 +- 0,015, gebunden; 0,8: aufgeloest oder Resonanz knapp ueber 0,106; rho_0 etwa omega + sqrt(E) | 0,6: 0,0741107 gebunden (Rayleigh-Band 0,0730 bis 0,0909). 0,8: 0,1917 - 0,0457 i (nicht konv.), 0,086 ueber der Kante (abgel.). omega + sqrt(E): nicht im Bericht | teilweise |
| V9 Tropfen 0,52 bis 0,55 | rho_2/omega_R bei 0,55 in [0,80; 1,10], bei 0,52 in [0,90; 1,05], Abweichung schrumpft mit R | rho_2 (drei Stufen, h 0,04/0,02/0,01): 0,0076881 / 0,0138556 / 0,0209348 / 0,0287211 bei 0,52 / 0,53 / 0,54 / 0,55. Rayleigh aus dem Profil 0,007943 / 0,014520 / 0,022225 / 0,030859, jeweils im Band. Verhaeltnis 0,968 / 0,954 / 0,942 / 0,931 (abgel.); gegen die Duennwand-Tabelle des PLAN 1,005 (0,52) und 1,011 (0,55) (abgel.) | getroffen |
| V10 Bruecke | dim 1 = Codex (< 1e-7 Re, < 1 % Im); Re steigt, Pol wird breiter; 60 %: bis dim 3 verfolgbar | dim 1: Abweichung 2,27e-9; Ciurla-Kalibrierung 2,72e-9. Re 1,4937770 -> 1,4921629 (dim 1,25) -> ... -> 1,7018102 (dim 3). Im: 6,7e-5 / 7,5e-3 / 1,2e-3 / 2,3e-3 / 2,7e-3 / 2,2e-4 / 1,8e-3 / 5,0e-3 / 1,5e-3 | teilweise (Kalibrierung und Durchgang ja; Re im ersten Schritt fallend, Breite nicht monoton) |
| V11 zeit0 | eta 1e-3: spaete Frequenz innerhalb 2e-3 von Re rho_0; eta 1e-2 etwa 10-mal weiter weg | 0,7, dr 0,025: eta 1e-3: 1,701610 bis 1,701803; eta 1e-2: 1,699766 bis 1,701686 (Pol 1,7018102) | getroffen |
| V12 zeitlin l = 2 | trifft das reelle rho_2 auf 1e-3 relativ, stabil ueber drei dr | 0,7: kein reelles rho_2 zum Vergleich. 0,55: 0,028579 / 0,028686 / 0,028712 (dr 0,1/0,05/0,025) gegen 0,0287211, 3e-4 relativ (abgel.). 0,52: 0,007466 / 0,007633 (dr 0,025 entfallen) gegen 0,0076881, 7e-3 relativ (abgel.) | teilweise |

Weitere Ergebnisse ohne Vorab-Vorhersage im PLAN:
- l = 0 linear (zeitlin) bei 0,7: 1,701807 - 1,46e-3 i (dr 0,025) gegen den Pol 1,7018102 - 1,468e-3 i.
- zeit0 bei 0,6 (nl06a, eta 1e-3, dr 0,025): 1,625551 bis 1,625647, Rate 2,31e-4 bis 2,32e-4 gegen den Pol 2,064e-4
  (12 % hoeher, abgel.). eta = 0: 1,625721 - 2,09e-4 i.
- Breiten-Scan l = 0 (Feinscan, ultrafein, oben) und 1D-Scan: siehe Abschnitt 2 und 5.
- Zweithaus: Codex' l = 0 bei 0,7 (1,701810218748 - 0,001468021744 i, R44) weicht im Re um 2,5e-10 (abgel.) von Stufe C ab.

**L3-Status:**
- Pole: drei Stufen; bei 0,7 aendert sich Re von A nach C um 6,8e-8 (abgel.), Im nicht in den gedruckten 4 Stellen.
- Stufe C fehlt (Zeitwaechter) bei l = 0: 0,79, 0,84, 0,88, 0,90 und l = 1: 0,84. Nach PLAN-L2 ("jeder berichtete Pol
  erscheint in A, B und C") gelten diese Pole als unsicher. Fuer 0,79 und 0,84 deckt Codex sie ab (Re-Abweichung von
  Stufe B 5,2e-9 bzw. 6,2e-9, abgel.).
- Bruecke und 1D-Scan: nur h = 0,01, obwohl `--h 0.02,0.01,0.005` uebergeben wurde (bruecke.json). Eine Stufe.
- Zeitlaeufe: 0,7 nur dr 0,05 und 0,025 (0,0125 fuer zeitlin und zeit0 entfallen); 0,52 nur dr 0,1 und 0,05; 0,55 drei dr
  (Aenderungen 1,07e-4 und 2,6e-5, abgel., konvergent); lange Laeufe (T = 3000) nur dr 0,05.
- Ergebnis: teilweise.

**Latten:** L1 ja | L2 bestanden | L3 teilweise | L4 teilweise | L5 nein.

**Vorschlag:** weiter. Die l = 0-Resonanz und das Breitenminimum sind von zwei Haeusern reproduziert; offen sind nur
kleine, rechenbare Punkte (dritte Stufe bei Bruecke und Zeitlaeufen, Exaktheit der Nullstelle).


| Kennung | Vorhersage (PLAN, knapp) | Ergebnis (Bericht, fein) | Urteil |
|---|---|---|---|
| P0 Anker | R_starr(0, 0) = 0,2227 (A), 1,0000 (C) | 0,2227 / 1,0000 in allen Berichtskoepfen | getroffen |
| P1 gleichfoermig | A: dS/S = +3,564e-3, domega/omega = -5,92e-4 (je +-3 %); C: dS/S betragsmaessig < 1e-4, domega/omega = -1,000e-3 | A: +3,5765e-3 / -5,9330e-4 (2g: +7,1753e-3 / -1,1894e-3); C: +3,96e-6 / -9,9913e-4 (2g: +1,4988e-5 / -1,9964e-3); Bericht: "erfuellt" (4 von 4) | getroffen |
| P2 ruhend periodisch | C: D(8)/D(16) zwischen 2,8 und 5,2; A-Gezeitenteil ebenso; A(16) innerhalb 10 % des Monopols | C: D(4) +1,7535e-3, D(8) +4,1643e-3, D(16) +2,2546e-3, D(8)/D(16) 1,847; A-Gezeitenteil D(8)/D(16) 7,435; beide "NICHT erfuellt". A(16)/Monopol 0,9333 | ueberwiegend verfehlt |
| P2b bewegt gegen ruhend (C) | D1_C bei (8; 0,1) und (16; 0,2) innerhalb Faktor 1,5 von \|D_C statik\| | 4,738e-3 gegen 4,1643e-3; 2,674e-3 gegen 2,2546e-3 (Faktor 1,14 und 1,19, abgel.) | getroffen |
| P3a Vorzeichen R | Vorzeichen R_mess = R_starr, wo \|R_starr\| > 0,1 | 3/3, 11/11, 32/32, 12/12 | getroffen |
| P3b Betrag R | \|R_mess/R_starr - 1\| <= 0,2 fuer Omega < 0,5 | 2/3 (langsam), 2/3 (schnell), 9/12 (Kante) | teilweise |
| P4 Kernfrage 1 | Gamma_A/Gamma_C > 3 an allen Punkten unter der Kante; (8; 0,1) -> (16; 0,2) waechst um Faktor 2,5 bis 10; D1_A(16; 0,2) 2,1e-3 bis 5,0e-3; Gamma_A divergiert nahe v = 0,32 | > 3 an 2 von 6 Punkten unter der Kante (3,520 und 16,780; sonst 0,587, 0,171, 1,113, 0,481). Faktor 4,77 (abgel.). D1_A(16; 0,2) 3,463e-3. Divergenz auf dem Raster nicht gesehen (A bei v 0,3: Gamma 11,64 bzw. 24,42) | teilweise |
| P5 (D1_A/D1_C)^2 | >= 0,15 bei lambda 8 und 16 unter der Kante (Karte: 0,05) | lambda 16: 1,6767; lambda 8: 0,1218 / 0,0014 / 0,0327 / 0,0087 (Omega 0,079 / 0,160 / 0,140 / 0,155) | teilweise |
| P6 Kernfrage 2, Resonanz | Maximum ring_res bei Omega 1,485 bis 1,503 (A, C, beide Gitter); Frequenz 1,4937 +- 0,01; Spitze >= Faktor 5; Halbwertsbreite etwa 0,011; ring(2g)/ring(g) 1,8 bis 2,2; dQ_kern ohne starke Spitze | Maximum fein 1,4940, grob 1,4980 (A und C); Nachschwingen 1,4937; Faktor 13,12 / 13,79 (A), 13,52 / 14,71 (C); ring(2g)/ring(g) 1,952 (A), 1,988 (C) (abgel.); dQ_kern-Maximum am Rand 1,30, Faktor 1,07 bis 1,08. Halbwertsbreite: nicht im Bericht (Verlauf A: halber Spitzenwert zwischen 1,485 und 1,490 sowie zwischen 1,498 und 1,503) | getroffen |
| P7 Kante | unter der Kante (0,14; 0,155) dQ hoechstens 3-mal Kontrolle; Maximum bei 0,165 bis 0,23 und mindestens 3-mal so gross wie bei 0,35 | Kontrolle 8,361e-9. A: 1,403e-7 / 9,095e-7, C: 1,757e-5 / 1,213e-4 unter der Kante. Maximum bei 0,170 (A 2,549e-5, C 2,973e-3); gegen 0,35: A 2,43-fach, C 4,14-fach (abgel.) | verfehlt (Scheiterregel "Abstrahlung unter der Kante" greift) |

**L3-Status:** In allen Paaren "L3 D1" und "L3 R" ok (Effekt mindestens 5-mal groesser als fein gegen grob), ausser
D1_A bei Omega 1,48 / 1,485 / 1,49 ("NEIN"; fein 8,352e-4 gegen grob 1,086e-3, 1,560e-3 gegen 7,924e-4, 4,672e-3 gegen
3,670e-3). Die Resonanzspitze liegt fein bei 1,494, grob bei 1,498. Kontrollen D1 (g = 0) 1,3e-7 bis 1,84e-5. Ergebnis:
bestanden, mit drei Ausnahmen an der Resonanzflanke.

**Latten:** L1 ja | L2 teilweise (P1, g = 0 und 2g bestanden; C-Gegenprobe P2 verfehlt) | L3 bestanden | L4 teilweise |
L5 mittelbar.

**Vorschlag:** weiter. Die Kernfrage ist mit aufgeloesten Zahlen beantwortet, aber die C-Gegenprobe P2 (Kruemmung ~ k^2)

### 1.3 KF-5 Geburt in 2D (Vorhersagen V1 bis V11 in kf5/PLAN.md)

| Kennung | Vorhersage (PLAN, knapp) | Ergebnis (Bericht) | Urteil |
|---|---|---|---|
| V1 lineares Wachstum | gamma_mess/gamma_max 0,85 bis 1,02 | s03 0,9035 (fein) / 0,9036 (grob); s01 0,9655 / 0,9658; s03b 0,9062; s01b 0,9574 | getroffen |
| V2 T_sat | s03: 22 +- 6; s01: 55 +- 12 | 20,47 / 20,47; 51,14 / 51,13 | getroffen |
| V3 Kontrollen | s08, frei: Kontrast max 0,02 bis 0,035, keine Komponente | Kontrast max 0,02000273 (= Startwert), keine Komponente, beide Gitter | getroffen |
| V4 Netzphase | umspannend hoechstens kurz um T_sat | in keinem Arm je umspannend ("zuerst -, zuletzt -") | getroffen |
| V5 Urteil T = 800 | "getrennte Tropfen" fuer s03 und s01 auf beiden Gittern | s03 grob/fein: getrennte Tropfen; s01 fein getrennt, **grob "gemischt"** (N_Netz 1); s03b (Seed 73, grob) **"gemischt"**; s01b getrennt | teilweise |
| V6 erste Generation | s03: N_max 40 bis 70, Median-Q 40 bis 90; s01: N_max 20 bis 40, Median-Q 30 bis 70 (Karte: Q etwa 62 / 44) | s03: N_max 40 (fein) / 41, Median-Q 34,03 / 34,82; s01: N_max 49 / 49, Median-Q 22,59 / 22,60 | verfehlt (nur N_max s03 im Band) |
| V7 Vergroeberung | N(800)/N_max: s03 0,15 bis 0,7; s01 0,3 bis 0,9; Median-Q(800) >= 1,3 x erste Generation (s03) | s03 3/40 = 0,075; s01 12/49 = 0,245 (abgel.); Median-Q(800) s03 1301 | teilweise |
| V8 Familie | "auf" etwa 55 %, "neben" etwa 15 %; E/Q unter 1 und 0 bis 3 % ueber (E/Q)_fam | "auf" 0 in allen Armen, "neben" 1 (s01b), Rest "unentschieden" oder "nicht rund" (fein: 12 von 16 Tropfen "nicht rund"); Urteil "nicht entscheidbar"; E/Q alle unter 1 (hoechstens 0,9899), Abstand zu (E/Q)_fam -4,8 % bis +7,3 % (abgel., fein) | verfehlt |
| V9 Anteile bei 800 | Ladung in Tropfen s03 0,8 bis 0,97, s01 0,7 bis 0,95; Energieanteil kleiner | s03 0,8339 / 0,8858; s01 0,7721 (fein) / 0,6141 (grob); Energieanteil ueberall kleiner | teilweise |
| V10 Erhaltung | Q-Drift < 1e-12; E-Drift < 1e-4 grob, < 3e-5 fein | Q hoechstens 1,1e-15; E grob hoechstens 8,9e-5, fein 2,2e-5 und 5,2e-6 | getroffen |
| V11 Geschwindigkeiten | v meist 0,01 bis 0,1; omega_geo und omega_ruhe gleich auf 1e-3 | v 0,022 bis 0,093 (ein Tropfen 0,299); omega_geo - omega_ruhe 5,0e-3 bis 2,8e-2 (abgel., z. B. 0,72624 gegen 0,73202) | teilweise (Gegenprobe der Geschwindigkeitskorrektur verfehlt) |

**L3-Status (vergleich_bericht.txt):** s03 bestanden (T_sat 20,471 / 20,474, gamma 0,20383 / 0,20381, N 3 / 3). s01
**nicht bestanden: urteil_netz_gleich** (grob "gemischt", fein "getrennte Tropfen"; T_sat 51,125 / 51,139, N 12 / 12).
Ergebnis: teilweise.

**Latten:** L1 ja | L2 teilweise (s08 und frei bestanden, V11-Gegenprobe verfehlt) | L3 teilweise | L4 teilweise |
L5 nein.

**Vorschlag:** parken. Die Netzfrage ist beantwortet (keine umspannende Komponente in 6 von 6 Arm-Gitter-Laeufen), die
Kernfrage der Karte (Familie, Stufe 5) blieb in allen Armen "nicht entscheidbar".

### 1.4 RG-1 Regge-Turm (Vorhersagen in regge/PLAN.md, Abschnitt 3, Urteilsregeln Abschnitt 5)

| Kennung | Vorhersage (PLAN, knapp) | Ergebnis (bahn/bericht.txt) | Urteil |
|---|---|---|---|
| H alpha (Ecken, m = 3..8) | 2,01 (1,97 bis 2,05); Regel "H getragen" bei \|alpha - 2\| <= 0,1 | 2,01199 (Standardfehler 1,7e-3); lokal 2,0214 -> 2,0046 | getroffen, "H getragen" |
| beta (m = 3..8) | 0,99 (0,95 bis 1,02) | 0,98814 (1,6e-3); lokal 0,9790 -> 0,9955 | getroffen, "Ring-Mechanismus getragen" |
| Lage Q_min | am oberen Rand 0,99 fuer alle m | "Rand oben" fuer m = 0 bis 8, Q faellt monoton | getroffen |
| Q_lim(0) | 11,70 +- 0,01 | 11,70090 | getroffen |
| Ringbild bei 0,99 | R_max sqrt(a)/m = sqrt 2 +- 10 % fuer m >= 3 | 1,447 bis 1,423 | getroffen |
| Ringexponent gamma | 0,85 bis 1,0 (nach dem Rauchtest geaendert) | 0,9573 bis 0,9829 | getroffen |
| Huelle E_min(J) | Saegezahn 4 bis 5 Spruenge, alpha_Huelle 1,9 bis 2,5 | 5 Spruenge, 2,0911 | getroffen |
| Chew-Frautschi | alpha_CF 1,95 bis 2,3 | 2,0552 | getroffen |
| R3-Anschluss | p bis 1e-12, Q und E bis 1e-6 | p bis 1,55e-15; dQ/Q bis 2,98e-6, dE/E bis 3,96e-6 (L2-Grenze 1e-4 bestanden) | teilweise (knapp verfehlt, im PLAN selbst vermerkt) |
| L3 | d alpha, d beta < 1e-4 | -1,22e-12 / +1,20e-12 | getroffen |

Nebenproben ohne Vorhersage: Rotorprobe bei festem Q, Exponent 0,899 (Q = 300) und 0,924 (Q = 1000), starrer Rotor
waere 2. dE = omega dQ (Trapez): Rest 5,1e-3 bis 6,0e-3 je m. J = mQ auf 6,7e-16.

**L3-Status:** bestanden (h0 0,01 gegen 0,005; max \|dQ/Q\|, \|dE/E\| in den Fitzeilen 4,5e-9).

**Latten:** L1 schwach | L2 bestanden | L3 bestanden | L4 teilweise | L5 nein.

**Vorschlag:** parken. alpha = 1 + 1/beta mit beta -> 1 war vorab aus der Duennring-Rechnung ableitbar (PLAN 1.5 bis
1.6, "schwache L1"); fuer Glied 7 fehlt der 3D-Fall (Tori, PLAN Abschnitt 10).

## 2. Die Nullstelle der Breite (omega*^2 ~ 0,7977)

**Stufenstabilitaet, Anthropic (bic-c, -d, -e, pole-08; Im rho, Betrag):**

| omega^2 | Stufe A (h 0,02) | B (0,01) | C (0,005) | A - C (abgel.) |
|---|---|---|---|---|
| 0,796 | 3,094e-6 | 3,098e-6 | 3,098e-6 | 4e-9 |
| 0,797 | 4,937e-7 | 4,983e-7 | 4,985e-7 | 4,8e-9 |
| 0,798 | 1,074e-7 | 1,121e-7 | 1,122e-7 | 4,8e-9 |
| 0,799 | 1,852e-6 | 1,857e-6 | 1,857e-6 | 5e-9 |
| 0,7995 | 3,497e-6 | 3,502e-6 | 3,502e-6 | 5e-9 |
| 0,800 | 5,643e-6 | 5,648e-6 | 5,648e-6 | 5e-9 |
| 0,801 | 1,140e-5 | 1,140e-5 | 1,140e-5 | unter der Druckstelle |

- Das Minimum ist auf allen drei Stufen an derselben Stelle; die Reihenfolge der Werte aendert sich nicht.
- **Kleinster gemessener Wert (Anthropic): 1,122e-7 bei omega^2 = 0,798** (Stufe C). Stufenstreuung dort: A - C 4,8e-9
  (4 %), B - C 1e-10 (abgel.). Re: 1,7447482334 / 1,7447481545 / 1,7447481496, also A - C 8,4e-8, B - C 4,9e-9 (abgel.).
- Das PLAN-Kriterium L2 (\|rho_B - rho_C\| < 5 % von \|Im\|) haelt bei 0,798 nur knapp: 4,9e-9 gegen 5,6e-9 (abgel.).
- Den Wert omega*^2 = 0,79768 hat kein Anthropic-Lauf gerechnet. Er ist eine Interpolation von +-sqrt(Gamma) zwischen
  0,797 und 0,798 (Leitung; L4-Fit). Der naechste gerechnete Punkt liegt 3,2e-4 daneben.

**Codex (3D-OMEGA-SCAN-CODEX.md, eigener Loeser, 23 Punkte je drei Stufen R28/R36/R44):**

| omega^2 | Im rho (R44) | Einordnung (Codex) |
|---|---|---|
| 0,7975 | -3,3797e-8 | |
| 0,797578125 | -1,0516e-8 | |
| 0,7976171875 | -3,8355e-9 | |
| 0,79765625 | -4,552e-10 | unter deklarierter Aufloesung |
| 0,7976953125 | -3,702e-10 | unter deklarierter Aufloesung (kleinstes Sample) |
| 0,797734375 | -3,5755e-9 | gedaempft |
| 0,7978125 | -1,9837e-8 | |
| 0,79796875 | -9,163e-8 | |

- Stufenaenderung am kleinsten Sample: R28 -> R44 4,3e-12 (abgel.), R36 -> R44 1,92e-14; Re 5,14e-10.
- Codex' Vorabregel: \|Im\| <= max(1e-9; 3 x letzte Stufenaenderung) heisst "unaufgeloest". Beide Punkte der Klammer
  liegen darunter. Codex: "Es ist kein exakt ungedaempfter Zustand nachgewiesen"; die Klammer ist "kein zertifiziertes
  Einschlussintervall"; die Kontrastschranke 1e-9 wurde nicht erreicht.
- **Zeilenvergleich mit unseren Werten an den sieben gemeinsamen Punkten** (Codex R44 gegen Anthropic Stufe C, bei 0,79
  und 0,84 Stufe B):

  | omega^2 | Re Codex | Re Anthropic | Differenz (abgel.) | Im Codex | Im Anthropic |
  |---|---|---|---|---|---|
  | 0,76 | 1,728146929750 | 1,7281469301 | 3,5e-10 | -1,988323749e-3 | -1,988e-3 |
  | 0,78 | 1,737088345765 | 1,7370883461 | 3,4e-10 | -4,044660398e-4 | -4,045e-4 |
  | 0,79 | 1,741434730334 | 1,7414347355 (B) | 5,2e-9 | -6,959222769e-5 | -6,959e-5 |
  | 0,80 | 1,745549972342 | 1,7455499727 | 3,6e-10 | -5,648125732e-6 | -5,648e-6 |
  | 0,81 | 1,749395533296 | 1,7493955337 | 4,0e-10 | -1,369867434e-4 | -1,370e-4 |
  | 0,82 | 1,752993121777 | 1,7529931222 | 4,2e-10 | -3,768176054e-4 | -3,768e-4 |
  | 0,84 | 1,759804382033 | 1,7598043882 (B) | 6,2e-9 | -8,699021886e-4 | -8,699e-4 |

  Im stimmt an allen sieben Punkten in allen vier gedruckten Stellen; Re auf hoechstens 4,2e-10 (Stufe C) bzw. 6,2e-9
  (nur Stufe B). Unsere Feinpunkte 0,796 / 0,797 / 0,798 / 0,799 / 0,7995 / 0,801 liegen nicht auf Codex' Gitter; jeder
  unserer Werte liegt zwischen Codex' Nachbarwerten (z. B. 0,798: 1,122e-7 zwischen 9,163e-8 bei 0,79796875 und
  2,155e-7 bei 0,798125).
- Codex, Feshbach-Arm B: Phase der auslaufenden Amplitude 0,31303 bei 0,79765625 und -2,82857 bei 0,7976953125, Betrag
  1,8e-5 bzw. 1,6e-5 gegen 7,0e-3 bei 0,79. Codex: "Der beobachtete Phasenwechsel erzwingt deshalb keine exakte Null."

**Zeitbereich (zeit0, .69):**
- Aufgeloest (PLAN-L3: \|Im\| x Fenster > 0,05) sind nur die Punkte abseits: 0,7 (1,44e-3 bis 1,46e-3 gegen 1,468e-3),
  0,76 (2,02e-3 gegen 1,988e-3), 0,84 (8,61e-4 gegen 8,699e-4), 0,6 (2,31e-4 gegen 2,064e-4).
- Bei 0,80 (T = 800, Fenster 400) und bei 0,79768 und 0,80 (T = 3000, Fenster 1500) liegen alle Raten unter der
  Aufloesungsgrenze des PLAN: 2,6e-8 x 1500 = 3,9e-5, 2,1e-7 x 1500 = 3,2e-4, 9,9e-6 x 1500 = 1,5e-2 (abgel.). Nach
  dem PLAN sind sie nur obere Schranken.
- Bei 0,79768, eta = 0,001, widersprechen sich die Auswertearten desselben Laufs im Vorzeichen: roh_zentrum -2,13e-7
  (Abklingen), differenz_zentrum +2,73e-7 und +3,23e-6, differenz_wand +3,50e-7 und +3,18e-6, betrag_zentrum +6,20e-6
  (Anwachsen); Im-Werte aller Atmungskomponenten zwischen -1,7e-5 und +6,2e-6. Bei eta = 0,01 sind die
  Hauptkomponenten einig (-9,5e-6 bis -1,0e-5).
- Nur eine Aufloesung (dr 0,05). Diese verschiebt die Frequenz gegen den Pol: bei 0,80 1,745574 gegen 1,7455500. Wie weit
  sich damit die Lage der Nullstelle im Zeitlauf verschiebt, steht in keinem Bericht.
- Passt der Zeitbereich? Er ist mit einer sehr kleinen Breite vertraeglich und zeigt die V-Form an den aufgeloesten
  Punkten. Eine Nullstelle kann er weder bestaetigen noch ausschliessen.

**Belegt:**
- Auf dem fortgesetzten l = 0-Polzweig gibt es ein scharfes Minimum der Breite nahe omega^2 = 0,7977. Zwei Haeuser mit
  verschiedenen Loesern finden es blind zu den Werten (die Gitterpunkte gab die Leitung vor). Es ist auf allen Stufen stabil.
- sqrt(Gamma) mit Vorzeichenwechsel verlaeuft zwischen 0,796 und 0,801 glatt; die Steigung aendert sich um etwa 5 %
  (L4: -1,054 bis -1,003, abgel. aus den Berichtswerten).
- Kleinster gemessener Wert: 1,122e-7 (Anthropic, 0,798) und 3,70e-10 (Codex, 0,7976953125).
- Auslaufende Amplitude mit Phasensprung nahe pi zwischen zwei Nachbarpunkten (Codex).
- In 1D kein solches Minimum auf dem Raster 0,55 bis 0,88 (14 Punkte, eine Stufe).

**Nicht belegt:**
- "Exakt null": Kein Lauf misst Gamma = 0. Codex nennt den kleinsten Wert "unaufgeloest"; L4 nennt einen Boden unter etwa
  1e-8 ebenso vertraeglich; Windungszahltest und L2-Eigenfunktion sind nicht gerechnet.
- BIC im strengen Sinn (gebundener Zustand im Kontinuum): nicht gezeigt.
- Die nichtlineare Lebensdauer an omega* und das Gesetz A ~ t^(-1/2) mit Rate ~ eta^2: Die Raten liegen unter der
  Aufloesung, und ein Exponentialfit kann t^(-1/2) nicht pruefen.

## 3. KF-4, Kernfrage: A gegen C bei gleicher Schwerpunktbeschleunigung

Umsetzung laut PLAN (Abweichung 1): nicht gleich gemachte Beschleunigung, sondern Gamma = D1/a_com je Lauf (Dehnung je
Schwerpunktbeschleunigung). Die Linearitaet in g ist geprueft: lin D1 1,897 bis 2,010; Gamma(2g)/Gamma(g) nahe 1 (z. B.
A lambda 4 v 0,1: 48,66 gegen 49,72).

| lambda | v | Omega | Gamma_A/Gamma_C | D1_A | D1_C | a_com A | a_com C | L3 D1 A, C |
|---|---|---|---|---|---|---|---|---|
| 8 | 0,1 | 0,079 | 3,520 | 1,653e-3 | 4,738e-3 | 2,795e-5 | 2,820e-4 | ok, ok |
| 16 | 0,2 | 0,080 | 16,780 | 3,463e-3 | 2,674e-3 | 2,019e-5 | 2,617e-4 | ok, ok |
| 8 | 0,1755 | 0,140 | 1,113 | 1,371e-3 | 7,582e-3 | 4,038e-5 | 2,484e-4 | ok, ok |
| 8 | 0,1936 | 0,155 | 0,481 | 1,035e-3 | 1,112e-2 | 4,316e-5 | 2,231e-4 | ok, ok |
| 4 | 0,1 | 0,158 | 0,587 | 4,815e-3 | 3,139e-3 | 9,684e-5 | 3,706e-5 | ok, ok |
| 8 | 0,2 | 0,160 | 0,171 | 6,020e-4 | 1,618e-2 | 4,245e-5 | 1,956e-4 | ok, ok |

- Ueber der Kante (0,165 bis 1,78): Gamma_A/Gamma_C zwischen 0,158 und 1,489 (scan-schnell, kante), an der Resonanz
  0,329 bis 1,346.
- **Antwort:** Ja, die Gezeitenverformung je Schwerpunktbeschleunigung unterscheidet sich zwischen A und C, aber nicht
  in einer festen Richtung. Bei Omega 0,08 verformt sich A je Beschleunigung 3,5- bzw. 16,8-mal staerker als C.
  Zwischen Omega 0,15 und 1,5 liegt das Verhaeltnis meist unter 1 (0,158 bis 0,97, C verformt sich staerker); Ausnahmen
  sind 0,2 bis 0,28 (1,05 bis 1,2) und 0,89 (1,49). Bei 0,14 (1,11) und ab 1,51 (1,02 bis 1,43) liegt es nahe 1 oder
  leicht darueber.
- Bei (16; 0,2) kommt der grosse Faktor ueberwiegend aus der Beschleunigung: D1 aehnlich (A 1,3-mal C, abgel.), a_com in
  A 13-mal kleiner (abgel.; R_mess A +0,0514, C +0,6663).
- **Aufgeloest (L3):** ja, an allen Punkten der Tabelle; der Effekt ist mindestens 5-mal groesser als fein gegen grob,
  die Kontrollen (g = 0) liegen mindestens 100-mal unter D1 (abgel.; knappster Fall lambda 8, v 0,2: 5,916e-6 gegen
  6,020e-4). Ausnahme ausserhalb dieser Tabelle: D1_A an der
  Resonanzflanke 1,48 bis 1,49.
- Vorbehalt aus demselben Lauf: Die C-Gegenprobe P2 ist verfehlt. Ruhend im periodischen Feld verformt sich C bei
  lambda 8 mit +4,16e-3 staerker als A im gleichfoermigen Feld (+3,58e-3), und D_C folgt nicht k^2.

## 4. Auffaelligkeiten

Die drei wichtigsten zuerst.

1. **Zeitbereich an der Nullstelle ist unaufgeloest und im Vorzeichen uneinheitlich.** Alle Raten der langen Laeufe
   (T = 3000, nur dr 0,05) liegen unter der PLAN-eigenen Aufloesungsgrenze; bei eta = 0,001 zeigen drei von vier
   Auswertearten Anwachsen statt Abklingen. RUNDE-06.md liest daraus "klingt mit 2e-8 bis 2e-7 ab", "7000- bis
   50 000-mal langsamer" und "etwa eta^1,7".
2. **Vorab-Status zweier Vorhersagen ist schwaecher als eingetragen.**
   - Leitung: ARBEITSFELD 03:20:24 sagt "bic-d, bic-e laufen noch". Die Logs zeigen Ende 03:20:15 (bic-d, rc-Zeile
     03:20:16) und 03:20:17 (bic-e, rc-Zeile 03:20:18). Die Berichte werden nach jeder Stufe gesichert. "Vorab" traegt
     also nur als "vor dem Lesen" (Selbstauskunft).
   - L4-Agent: Aus der Grobtabelle vorhergesagt war x* etwa 0,7977 mit Treffern bis 12 %. Die Werte 0,79768, 1,7446 und
     1,07 sind das Fit-Ergebnis nach den Feinlaeufen (L4 Abschn. 5 iii; G1: "bevor ich die Feinwerte vollstaendig las").
3. **KF-4: Die C-Gegenprobe P2 und die Kantenregel P7 sind verfehlt.**
   - P2: C folgt ruhend nicht k^2 (D(8)/D(16) = 1,847 statt 2,8 bis 5,2).
   - P7: Unter der Kante verliert C 1,757e-5 bzw. 1,213e-4 Ladung, das 2100- bzw. 14 500-fache der Kontrolle 8,361e-9
     (abgel.); A das 17- bzw. 109-fache.
   - Die Richtung des A/C-Unterschieds wechselt mit Omega (Abschnitt 3).

Weitere:
4. KF-5: Die Gegenprobe der Geschwindigkeitskorrektur (V11) verfehlt um Faktor 5 bis 28. 12 von 16 Tropfen (fein) sind
   "nicht rund". Der zweite Seed s03b endet "gemischt" mit nur 0,398 der Ladung in Tropfen. L3 fuer s01 ist "nicht
   bestanden". Die erste Generation liegt bei Median-Q 34 (s03) und 23 (s01) statt 62 und 44 (Karte).
5. 3D, fehlende Stufen: dr 0,0125 bei 0,7 (zeitlin und zeit0) entfallen; dr 0,025 bei 0,52 entfallen; Stufe C bei 0,79,
   0,84, 0,88, 0,90 (l = 0) und 0,84 (l = 1) entfallen. Bruecke und 1D-Scan laufen trotz `--h 0.02,0.01,0.005` nur mit
   h = 0,01.
6. 3D, V3 und V7 verfehlt: Die erwarteten Kompressions- und Kavitaetsmoden fehlen im Kasten (Umlaufzahlen 0 bis 2 je l).
7. 3D, V6 bei 0,6: schmaler l = 2-Pol 1,6786834 - 2,911e-3 i unter 1 + omega. Bei 0,8 ist der l = 2-Pol "(nicht konv.)".
8. 3D, Bruecke: Im springt zwischen den Stuetzstellen (7,5e-3 bei dim 1,25, 1,2e-3 bei 1,5, 2,2e-4 bei 2,25). Ob die Spur
   zwischen Stuetzstellen im Abstand 0,25 auf einen anderen Pol wechselt, prueft der Bericht nicht (keine
   Schritthalbierung noetig, Newton konvergierte immer).
9. 3D, l = 1 ab 0,86: Der Pol bei 0,84 (1,9138667) liegt 0,0007 unter der Kastengrenze 1 + omega - 0,002 = 1,9145 (abgel.).
   Belegt ist "verlaesst den Suchkasten", nicht "erreicht die Kante".
10. RG-1: Die Rechnung ist sauber, das Ergebnis war aber vorab ableitbar. Die Nebenprobe dE = omega dQ hat einen Rest von
    5e-3 (Trapez, grob). Bei festem Q gilt ein Exponent 0,9 statt 2 (kein starrer Rotor).
11. KF-4 scan-schnell: R_mess weicht in C ueber der Kante stark von R_starr ab (lambda 8, v 0,45: +0,1607 gegen +0,0130;
    lambda 8, v 0,6: -0,0678 gegen -0,3558). Der PLAN nennt R_starr dort nur einen Richtwert.

## 5. Abgleich mit RUNDE-06.md (Fassung 03:50:02)

Richtung Text -> Bericht (nicht gedeckt oder abweichend):

| Zeile | Textstelle | Berichtswert |
|---|---|---|
| 26 | "Codex-Scan offen" | 3D-OMEGA-SCAN-CODEX.md liegt vor (03:25), in Z. 155 bis 163 eingetragen |
| 32 | KF-4 "laeuft (.69 p4000b), letzter Aufruf kante" | kante Ende 01:45:22 UTC = 03:45:22 CEST, rc = 0, "KETTE-KF4-ENDE" |
| 65 bis 66 | "laesst sich stetig bis dim = 3 verfolgen ... nicht geraten" | 9 Stuetzstellen im Abstand 0,25, eine Stufe h = 0,01; Re faellt im ersten Schritt (1,4937770 -> 1,4921629); Stetigkeit zwischen den Stuetzstellen nicht geprueft |
| 69 | "duennwandig" (0,6) | nicht im Bericht; R_Q 7,41, gerechnet mit den Standardstufen h 0,02/0,01/0,005, nicht mit den Duennwand-Stufen |
| 80 | l = 2 bei 0,8 ohne Vermerk | Bericht: "(nicht konv.)" |
| 97 | ".69, cpu3" fuer 0,7 und 0,8 | 0,7 (nl07a) auf cpu2, 0,8 (nl08a) auf cpu3 |
| 100 | "atmet er mit 1,7454 bis 1,7456" | dr 0,025, eta 1e-3: 1,745244 / 1,745245 / 1,745279 (Plus-Zweig), 1,745426 (Betrag), 1,745602 / 1,745608 -> 1,7452 bis 1,7456 |
| 104 bis 105 | 0,84 ohne Vermerk | Stufe C bei 0,84 entfallen ("-") |
| 107 | "Vorhersage vorab (ARBEITSFELD 03:20:24, ... vor den uebrigen Werten)" | bic-d Ende 03:20:15, bic-e Ende 03:20:17; Vorhersage 7 bis 9 s nach Laufende |
| 125 | "auf 3 bis 7 %" | 0,799: 2,0e-6 gegen 1,857e-6 = 7,7 % vom Messwert (abgel.); 0,798: 7 %; 0,7995: 2,9 %; 0,801: 5,3 % |
| 127 | "omega*^2 = 0,79768 (omega* = 0,89313)" | in keinem Rechenbericht; Interpolation; liegt in Codex' Klammer 0,79765625 bis 0,797734375 |
| 129 bis 131 | "Die Breite verschwindet dort ... Signatur eines ... BIC" | kleinster Wert 1,122e-7 (Anthropic) bzw. 3,70e-10 "unaufgeloest" (Codex); Codex: "kein exakt ungedaempfter Zustand nachgewiesen" |
| 132 bis 133 | "Schwingung, die in linearer Ordnung gar nicht abstrahlt" | dito, nicht gezeigt |
| 141 | "dieselbe V-Form um omega*" | aufgeloest nur 0,76 und 0,84; 0,80 nur obere Schranke (PLAN-L3) |
| 146 bis 151 | Raten 2,6e-8 / 2,1e-7 als Abklingen; "7000- bis 50 000-mal langsamer" | Fenster 1500: nur obere Schranken; eta 1e-3: differenz_zentrum +2,73e-7 / +3,23e-6, differenz_wand +3,50e-7 / +3,18e-6, betrag_zentrum +6,20e-6 (Anwachsen), nur roh_zentrum -2,13e-7; 1,45e-3/2,6e-8 = 5,6e4 (abgel.) |
| 152 | "verschiebt sich die Frequenz (nichtlinear um -3e-3)" | betrag_zentrum 1,743494 gegen 1,744642 (eta 0): -1,15e-3 (abgel.); nur der Plus-Zweig 1,741918 liegt -2,7e-3 daneben |
| 162 | "Lage und Tiefe des Minimums ... von zwei Haeusern blind bestaetigt" | Lage ja. Tiefe: Anthropic hat am Minimum nicht gerechnet (kleinster Wert 1,122e-7 bei 0,798); unter 1e-7 misst nur Codex. Gitterpunkte gab die Leitung vor (OMEGA-SCAN-ACK) |
| 166 bis 167 | "Die Resonanz ist also Feshbach-artig" | Codex: "stuetzt die Feshbach-Deutung numerisch"; "Arm A wurde nur auf R44 gerechnet; seine Gitterkonvergenz ist offen" fehlt |
| 176 | "Bei konstanter Phase auf 1e-5" | Phasen (+pi wo noetig): 0,31950 (0,79), 0,31303, 0,31302, 0,31307 (0,80), 0,32139 (0,81) (abgel.): 1e-5 nur fuer das Paar am Minimum, ueber 0,79 bis 0,81 bis 8e-3 |
| 191 bis 192 | "aus der Grobtabelle vorhergesagt, bevor er die Feinwerte las: omega*^2 = 0,79768, ..., 1,07" | L4: Grobvorhersage x* etwa 0,7977, Gamma 3,3e-6 / 5,6e-7 / 1,0e-7 / 1,9e-6 / 3,7e-6 / 1,25e-5; 0,79768 und 1,07 sind das Ergebnis mit den Feinlaeufen; "bevor ich die Feinwerte vollstaendig las" |
| 198 | "Die langen Zeitlaeufe passen dazu: ... etwa eta^1,7" | Raten unter der Aufloesung (s. o.); t^(-1/2) mit Exponentialfit nicht pruefbar; eine Aufloesung |
| 202 bis 203 | "weil Re rho ... die zweite Kante 1 + omega (1,917) erreicht" | Bericht: Umlauf 0, Newton 0 ab 0,86; Kastengrenze 1,9145 bei 0,84; belegt ist "verlaesst den Kasten" |
| 211 | "Eine Nullstelle gibt es zwischen 0,55 und 0,88 nicht." | 14 Rasterpunkte, eine Stufe h = 0,01: "auf dem Raster nicht gesehen" |
| 216 bis 218 | "Offen: blinde Nachrechnung (Codex); Literatur (L4)" | beide liegen vor (Z. 155, Z. 182) |
| 268 | "am oberen Gitterrand (omega^2 = 0,99, NLS-Grenze), wo der Ball ein duenner Ring ist" | 0,99 ist der Gitterrand, die NLS-Grenze (omega -> 1) steht getrennt als Q_lim; m = 0 hat keinen Ring, m = 1 Dicke/R 0,854 |
| 274 | "Die Skalierung duenner Wirbelringe in der NLS-Grenze ist Literatur (L4, [S])" | PLAN: "Die Duennring-Asymptotik der NLS-Wirbel ist vermutlich bekannt; eine Quelle habe ich nicht geoeffnet." |
| 288 | "In 2D entstehen also getrennte Tropfen, kein Netz." | "kein Netz" gedeckt (nie umspannend); "getrennte Tropfen" nur in 4 von 6 Arm-Gitter-Laeufen: s01 grob und s03b grob "gemischt" |

Gedeckt, ohne Befund: Z. 45 bis 61 (Pol 0,7, Codex-Abgleich, l = 1, l = 3, 1D-Vergleich 22-mal, 472 und 10 300),
Z. 67 bis 68, Z. 70 bis 79, Z. 81 bis 96, Z. 98 bis 99, Z. 115 bis 124 (alle Tabellenwerte),
Z. 126, Z. 136 bis 139, Z. 144 bis 148 (Tabellenwerte selbst), Z. 155 bis 161, Z. 165 bis 175 (Zahlen), Z. 184 bis 190,
Z. 193 bis 197, Z. 200 bis 201, Z. 206 bis 209 (alle 28 Tabellenwerte), Z. 263 bis 267, Z. 269 bis 273, Z. 275 bis 276,
Z. 280 bis 287, Z. 289 bis 290.

Richtung Bericht -> Text (fehlt in RUNDE-06.md):
- 3D: die Tropfen-Ergebnisse 0,52 bis 0,55 (V9, PLAN-L5 bestanden, Tabelle in 1.1); die l = 2-Frequenz bei 0,7 knapp ueber
  der Kante (0,16378); zeit0 bei 0,6 (Rate 12 % ueber dem Pol); die verfehlten Vorhersagen V3, V6 (bei 0,6) und V7; die
  fehlende dritte Aufloesung bei 0,7.
- KF-4: noch keine Eintraege (Ernte offen); alle Zahlen in 1.2 und 3.
- KF-5: V6 bis V8 und V11 verfehlt oder teilweise; L3 s01 "nicht bestanden"; zweiter Seed s03b "gemischt"; kein Tropfen
  "auf" der Familie, 12 von 16 (fein) "nicht rund".
- RG-1: Huelle und Chew-Frautschi (2,0911 / 2,0552), Ringexponent 0,957 bis 0,983, Rotorprobe (0,899 / 0,924), R3-Anschluss
  knapp ueber der eigenen 1e-6-Vorgabe.

## 6. Zusammenfassung

| Test | Kernvorhersage | Ergebnis | Urteil | L3 | L1 / L2 / L3 / L4 / L5 | Vorschlag |
|---|---|---|---|---|---|---|
| 3D-Resonanz | rho_0 Re 1,68 (1,55 bis 1,83), Im etwa -3e-3 | 1,7018102190 - 1,468e-3 i; Codex gleich auf 2,5e-10 | getroffen (V1, V2, V4, V5, V9, V11), teilweise (V6, V8, V10, V12), verfehlt (V3, V7) | teilweise | ja / bestanden / teilweise / teilweise / nein | weiter |
| 3D-Nullstelle (ohne PLAN-Vorhersage) | Leitung 03:20:24: Nullstelle 0,79767, Gamma(0,798) etwa 1,2e-7 | Minimum 1,122e-7 (0,798), Codex 3,70e-10 unaufgeloest; stabil ueber alle Stufen | Minimum belegt, "exakt null" nicht | Pole ja, Zeitbereich nein | ja / bestanden / teilweise / teilweise / nein | weiter |
| KF-4 | Gamma_A/Gamma_C > 3 unter der Kante; Resonanz bei 1,494 | 2 von 6 Punkten > 3 (3,52; 16,78), sonst 0,17 bis 1,1; Resonanzspitze 1,494, Faktor 13 | P0, P1, P2b, P3a, P6 getroffen; P3b, P4, P5 teilweise; P2, P7 verfehlt | bestanden (Ausnahme Flanke) | ja / teilweise / bestanden / teilweise / mittelbar | weiter |
| KF-5 | getrennte Tropfen; Familie "auf" etwa 55 % | nie umspannend; 4 von 6 "getrennt"; Familie 0 "auf", "nicht entscheidbar" | V1 bis V4, V10 getroffen; V5, V7, V9, V11 teilweise; V6, V8 verfehlt | teilweise (s01 nicht bestanden) | ja / teilweise / teilweise / teilweise / nein | parken |
| RG-1 | alpha 2,01 (1,97 bis 2,05) | 2,01199 +- 0,0017; beta 0,98814 | getroffen, "H getragen" | bestanden | schwach / bestanden / bestanden / teilweise / nein | parken |

## 7. Einfach gesagt

Der dreidimensionale Q-Ball hat eine innere Atmung, die langsam Energie nach aussen verliert, und bei einer bestimmten
Frequenz wird dieses Lecken fast null. Zwei voneinander unabhaengige Programme finden diese Stelle gleich; ob das Lecken
dort ganz aufhoert oder nur winzig wird, ist noch nicht gezeigt, und die langen Zeitsimulationen sind zu grob, um das zu
die eine, mal die andere staerker. In 2D zerfaellt eine duenne Feldschicht in Tropfen statt in ein Netz; ob die Tropfen
ruhige, echte Q-Baelle sind, blieb offen. Drehende Baelle folgen der String-Regel J ~ E^2, das liess sich aber schon
vorher auf dem Papier ausrechnen.
