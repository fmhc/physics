# LEITER-1D: Plan (Runde 25, explorativ)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 02:26:08 CEST (date). Plan
  geschrieben ab 02:49:11 CEST (date), nach den Rauchlaeufen (Abschnitt 4), vor jedem echten Lauf. Zeitbox 120 min (bis
  04:26:08 CEST).
- Ordner: lokal coordination/runden-v3/RUNDE-25/leiter-1d/ (code/, lauf-69/, rauch-69/); .69:
  /home/fmh/fmhc-physics-remote/runde25-leiter-1d/ (leiter_1d.py, start*.sh, lauf/, rauch/).
- Markierungen: [K] Wortlaut der KARTE, [L] Vorgabe der Leitung im Auftrag (nicht in der Karte), [A] Festlegung des
  Code-Agenten, [H] Hypothese.

## 1. Karte (bindend, unveraendert) [K]

- Modell M1, beta = 1/2, 1D, beide Paritaeten (gerade: Y'(0) = 0; ungerade: Y(0) = 0). Profil aus der ersten
  Integralform; Aussenschwanz vernachlaessigbar. Linearisierung wie WAND-BETA. W-Abbildung: aussen rein abklingend im
  geschlossenen Kanal, offener Kanal null, nach innen bis x = 0. Je eps die Nullstellenlinie der ersten Komponente in rho
  verfolgen; die Vorzeichenwechsel der zweiten Komponente entlang eps sind die Sprossen; verfeinern, Umlauf pruefen.
  eps logarithmisch von 0,05 bis 1e-7. Kontrolle: Fuer eps -> 0 laeuft die Nullstellenlinie gegen rho_z.

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| L1D-1 | In eps [1e-7; 0,05] gibt es mindestens drei stille Stellen (beide Paritaeten zusammen), mit aufgeloestem Umlauf | 65 % |
| L1D-2 | Die zwei kleinsten-eps-Schritte Delta ln(1/eps) zwischen aufeinanderfolgenden Sprossen liegen innerhalb +-10 % von 2,3100 | 45 % |
| L1D-3 | Die Sprossenfrequenzen laufen mit fallendem eps auf rho_z zu; die Sprosse mit dem kleinsten eps liegt innerhalb 0,005 von 1,52415 | 50 % |

- Bedeutung (vorab, Karte): L1D-1 und L1D-2 treffen ein -> die stille Leiter gibt es auch in 1D; ebene Wand mit stehender
  Innenwelle genuegt, Kruemmung oder "Innenbarriere" nicht noetig; Sprossen geometrisch dicht (Faktor ~0,1 in eps) [H];
  die Projekt-Erklaerung "ohne Innenbarriere keine Leiter" (G2-10) ist dann ueberholt. L1D-1 trifft nicht ein -> die ebene
  Wand allein reicht in 1D nicht, oder die Stellen sind numerisch unzugaenglich; beschreiben, mit Belegen.
- rho_z = 1,5241497621, b = 2,3100 (RUNDE-24/wand-beta/ERGEBNIS.md, Karte).

## 2. Berichtigung zum Auftrag [A]

- Der Auftrag nennt als Umkehrpunkt "S0 = groesste Wurzel von 1 - omega^2 - S + beta S^2 = 0". Fuer beta = 1/2 sind die
  Wurzeln S = 1 -+ sqrt(2 eps); zwischen ihnen ist f'^2 < 0. Das Profil startet bei S = 0 und erreicht zuerst die
  **kleinere** Wurzel. Deshalb gilt hier S0 = 1 - sqrt(2 eps) (-> S_c = 1 fuer eps -> 0). k0 gibt beide Wurzeln aus.

## 3. Verfahren (code/leiter_1d.py, ein Skript, Kommandos k0, scan, sprossen, dop853, regel, selbsttest)

- **Profil [A]:** Die Quadratur x(S) der ersten Integralform ist geschlossen loesbar:
  S(x) = (1 - 2 eps)/(1 + sqrt(2 eps) cosh(sqrt(2 - 4 eps) x)). Kein Schiessen, kein Abschneiden; der Schwanz ist exakt.
  Wandlage x_w: sqrt(2 eps) cosh(b x_w) = 1, also x_w ~ (1/(2 sqrt2)) ln(2/eps).
- **Linearisierung [K]:** A'' = [W - (rho - omega)^2] A + C B, B'' = C A + [W - (rho + omega)^2] B, W = 1 - 4S + 4,5 S^2,
  C = -2S + 3S^2 (wie wand_beta.py, Klasse MB). A geschlossen, B offen.
- **W-Abbildung [A]:** Start bei X = N h, N = ceil((x_w + D)/h), mit A = 1, A' = -q, B = B' = 0; klassisches RK4 mit
  festem Schritt h auf x_j = j h bis x = 0 (vektorisiert ueber rho bzw. Paare (rho, eps)); Normierung exp(-q (X - x_w)) > 0.
  gerade (F1, F2) = (A'(0), B'(0)), ungerade (F1, F2) = (A(0), B(0)). Eine Integration liefert beide Paritaeten.
- **eps-Raster [L/A]:** eps_j = 10^(-7 + j/40), j = 0 .. 252 (40 Punkte je Dekade, 1e-7 bis 0,1995). Der Teil ueber 0,05
  dient dem G2-10-Vergleich.
- **Scan [A]:** je eps 2001 rho-Punkte in [1,30; 1,70] (Leiterfenster, Abstand 2e-4; enthaelt rho_z und den G2-10-Ast
  bei 1,37); jeder Vorzeichenwechsel von F1 je Paritaet wird mit Illinois auf 1e-13 verfeinert, dort F2. Dazu eine
  Uebersicht ueber das ganze Fenster (1 - omega + 0,002; 1 + omega - 0,002) mit 4001 Punkten an jedem vierten eps
  (Nebenaeste dokumentieren).
- **Aeste [A]:** Wurzeln benachbarter eps (j, j + 1) werden verknuepft, wenn sie gegenseitig naechste Nachbarn sind und
  |d rho| < 0,03. Kandidat = Vorzeichenwechsel von F2 zwischen zwei verknuepften Wurzeln im Leiterfenster.
- **Verfeinerung [A]:** geschachteltes Illinois. Aussen l = ln(1/eps) zwischen den zwei Rasterpunkten (bis 1e-10),
  innen je l die F1-Wurzel nahe der linear interpolierten Astlage (41 Punkte in +- max(4 |d rho|, 2e-3), naechster
  Wechsel zur Mitte, Illinois bis 1e-13). Die Vorzeichen an beiden Klammerenden werden neu gerechnet.
- **Umlauf [A]:** Rechteck rho_c +- 0,01, l_c +- 0,5 um die lineare Lage des Kandidaten aus dem feinen Scan (gleiches
  Rechteck fuer beide Stufen), gegen den Uhrzeigersinn in (rho waagrecht, l senkrecht); 60 Punkte je Seite, Halbierung
  jedes Intervalls mit Phasensprung >= 0,4 rad, bis 30 Runden. Aufgeloest: groesster Sprung < 0,4 rad und
  |Summe/2pi - U| < 0,1. Gleichparitaetige Nachbarsprossen liegen nach der Karte ~4,6 in l entfernt.
- **Stufen [A]:** grob h = 0,02, fein h = 0,01 (je D = 30). Lage der Sprossen aus fein.
- **Gegenproben (berichtet, keine Regel) [A]:** (a) Gebiet D = 40 auf h = 0,01 (ganzer sprossen-Lauf); (b) zweites
  Verfahren: Newton in (rho, l) mit scipy DOP853 (adaptiv, rtol 1e-12, D = 40), Start an der feinen Lage.

## 4. Rauchlaeufe vor diesem Plan (ungueltig fuer jede Wertung; offengelegt)

- .69, 00:45:32 bis 00:48:10 UTC (rauch1.sh, rauch2.sh), alle rc = 0. Parameter in keinem echten Lauf: h = 0,025 / 0,0125,
  D = 25, n_rho 501 / 2001, eps nur in [0,063; 0,2] (j = 232 .. 252), G2-10-Teil mit h = 0,025 und 401 Punkten.
- selbsttest (synthetische W-Abbildung, keine Physik): 13 von 13 Nullstellen, Lage auf <= 5e-11 in l, alle Umlaeufe mit
  dem erwarteten Vorzeichen.
- k0 (Rauchparameter): Profilreste <= 2e-15, Quadratur <= 2,7e-10; ebene Wand mit diesem RK4: rho_z = 1,524149762111
  (h = 0,025) und ...133 (h = 0,0125), also 1e-11 bis 3e-11 neben WAND-BETA; k_in = 1,923325, kappa_in = 1,026213.
  RK4 gegen DOP853 (rohe W-Vektoren): <= 1,5e-7 (h = 0,025), <= 1e-8 (h = 0,0125).
- G2-10-Bereich (omega^2 0,55 .. 0,70, h = 0,025): je Paritaet genau eine F1-Wurzel im ganzen Fenster; gerader Ast bei
  1,3751 / 1,3803 / 1,4273 / 1,4944 (G2-10: 1,375130 / 1,380272 / 1,427327 / 1,494353, Abstand <= 4e-6), F2 < 0 ueberall;
  ungerader Ast 1,62 .. 1,78, F2 > 0 ueberall. Kein Vorzeichenwechsel, wie G2-10.
- Rauch-Scan eps 0,063 .. 0,2: gerader Ast 1,370 .. 1,494 (F2 < 0), ungerader Ast 1,640 .. 1,695 und ab eps ~0,115
  ausserhalb [1,30; 1,70] (F2 > 0). Aus dem Vorhersagebereich eps <= 0,05 habe ich nichts gesehen.
- Zeiten (.69): Scan 0,7 s je eps bei h = 0,0125 und 2001 Punkten; nach der Vorab-Tabelle der Koeffizienten (Umbau ohne
  Ergebnisaenderung, Rauch-Scan bitgleich wiederholt) unveraendert.

## 5. Laeufe (start1.sh, start2.sh, start3.sh; je Aufruf eine Kleintest-Einheit, 1 Kern, <= 600 s)

| Phase | Name | Spur | Aufruf (Kurzform) |
|---|---|---|---|
| 1 | k0 | cpu | k0 --h-liste 0.01,0.005 --h-g210 0.01 --n-g210 2001 |
| 1 | scan-h002 | cpu2 | scan --h 0.02 --D 30 --j-von 0 --j-bis 252 --n-rho 2001 |
| 1 | scan-h001-a / -b | cpu3 / cpu4 | scan --h 0.01 --D 30, j 0 .. 126 / 126 .. 252, --n-rho 2001 |
| 1 | survey-h002 | cpu6 | scan --h 0.02 --D 30 --j-schritt 4 --n-rho 4001 --voll |
| 2 | sprossen-h002 | cpu2 | sprossen --h 0.02 --D 30 (Kandidaten aus scan-h002, Rechtecke aus scan-h001) |
| 2 | sprossen-h001 | cpu3 | sprossen --h 0.01 --D 30 |
| 2 | sprossen-h001-D40 | cpu4 | sprossen --h 0.01 --D 40 (Kontrolle) |
| 3 | dop853, dann regel | cpu6, cpu | dop853 --sprossen lauf/sprossen-h001.json --D 40; regel -> lauf/auswertung.json |

- Phase 2 startet erst, wenn alle Phase-1-Aufrufe rc = 0 haben; Phase 3 nach Phase 2. Die Skripte sind unveraendert.

## 6. Regeln (mechanisch, Kommando regel; Ausgabe lauf/auswertung.json) [A]

- **K0 bestanden:** an eps = 1e-7, 1e-5, 1e-3, 0,05, 0,2 Profilreste (erste Integralform und Bewegungsgleichung) <= 1e-10
  und Quadraturabweichung <= 1e-9; ebene Wand |rho_z(h) - 1,5241497621| <= 1e-6 auf h = 0,01 und 0,005, konvergiert.
  Sonst gelten L1D-1 bis L1D-3 als nicht auswertbar (= nicht eingetroffen).
- **Sprosse (gezaehlt):** ein feiner Kandidat (h = 0,01) mit
  (a) Verfeinerung konvergiert, (b) einer groben Entsprechung (gleiche Paritaet, |d l| < 0,3, konvergiert),
  (c) |l_fein - l_grob| <= 1e-4 und |rho_fein - rho_grob| <= 1e-5,
  (d) Umlauf auf beiden Stufen aufgeloest, |U| = 1 und gleiches Vorzeichen.
  Lage aus h = 0,01. Gezaehlt werden nur Sprossen im Leiterfenster [1,30; 1,70] (dort laufen alle Kandidaten).
- **L1D-1:** eingetroffen, wenn mindestens 3 Sprossen eps* in [1e-7; 0,05] haben.
- **L1D-2:** Sprossen in [1e-7; 0,05] nach eps aufsteigend; Schritte l_i - l_(i+1) zwischen Nachbarn (beide Paritaeten);
  "die zwei kleinsten-eps-Schritte" = die zwei Schritte mit den kleinsten eps. Eingetroffen, wenn beide in
  [0,9; 1,1] x 2,3100 = [2,0790; 2,5410] liegen. Weniger als 3 Sprossen: nicht auswertbar = nicht eingetroffen.
- **L1D-3:** (a) |rho_n - rho_z| faellt streng entlang der Sprossen nach fallendem eps, und (b) die Sprosse mit dem
  kleinsten eps hat |rho - 1,52415| <= 0,005. Beides noetig. Weniger als 2 Sprossen: nicht auswertbar = nicht eingetroffen.
- **Bedeutung bei L1D-1 nicht eingetroffen:** mit Astverlauf, F2 entlang der Aeste, Umlauf-Spruengen, Stufen- und
  Gebietsdifferenzen beschreiben, ob die Stellen eher fehlen oder numerisch unzugaenglich sind.

## 7. Kontrollen (berichtet, keine Regel)

- Hauptast je Paritaet (Ast durch die Wurzel bei eps = 1e-7, die rho_z am naechsten liegt): rho bei 1e-7 und die groesste
  Abweichung |rho - rho_z| je Dekade; Erwartung [A]: Abweichung bei 1e-7 < 0,01 und je Dekade fallend.
- Zwei Stufen (h = 0,02 / 0,01), zwei Gebiete (D = 30 / 40), zweites Verfahren (DOP853-Newton), RK4 gegen DOP853 roh (k0),
  ebene Wand mit demselben RK4 (k0).
- G2-10: gerader Ast bei omega^2 = 0,55 / 0,60 / 0,65 / 0,70 gegen 1,375130 / 1,380272 / 1,427327 / 1,494353 (G2-10-Code
  mit h = 0,02; erwartet Abstand <= 1e-4); keine gerade Sprosse mit eps in [0,05; 0,2]; F2-Vorzeichen auf 0,55 .. 0,70.
- Uebersicht ueber das ganze Fenster: Zahl und Lage der F1-Wurzeln je Paritaet, Vorzeichenwechsel von F2 auf Aesten
  ausserhalb [1,30; 1,70] (nicht verfeinert, nicht gezaehlt).
- Sprossen nur auf der groben Stufe (ohne feine Entsprechung) werden aus sprossen-h002.json berichtet, nicht gezaehlt.

## 8. Schreibtisch des Code-Agenten (vor jedem echten Lauf, [H], keine Wertung)

- Innen (S nahe 1) gibt es eine laufende Welle (k_in = 1,9233) und eine abklingende (kappa_in = 1,0262). Gerade
  Sprossen verlangen e2.Y'(0) = 0, ungerade e2.Y(0) = 0. Mit der Wand-Amplitude c_in(rho) ~ c' (rho - rho_z) folgt
  c_in = +- d e^(-kappa_in L), L = 2 x_w ~ (1/sqrt2) ln(2/eps).
- Erwartung daraus: (i) Paritaet wechselt von Sprosse zu Sprosse; (ii) rho_n - rho_z wechselt mit der Paritaet das
  Vorzeichen; (iii) |rho_n - rho_z| ~ eps_n^0,726 (kappa_in/sqrt2); (iv) der Hauptast schwankt um rho_z mit einer
  Huelle ~ eps^0,363; (v) in [1e-7; 0,05] liegen 5 oder 6 Sprossen (13,1/2,31 = 5,7), falls die Leiter bis 0,05 reicht.
- Numerisch erwarte ich keine Huerde: e^(kappa_in x_w) ist bei eps = 1e-7 nur ~450 (in 3D bis 4e7).

## 9. Zeitplan und Grenzen

- Gemessene Zeiten aus den Rauchlaeufen: Abschnitt 4. Keine geschaetzten Endzeiten.
- Faellt ein Aufruf aus (rc != 0) oder erreicht er 600 s: berichten; ein Nachlauf nur als offen benannte Abweichung.
- Nach dem Einfrieren keine Aenderung an Plan, Code und Skripten; Abweichungen offen mit Grund und Zeit im ERGEBNIS.

## 10. Code und Skripte (sha256, vor dem Einfrieren)

- leiter_1d.py f236d3770a02f7ad8adf26f4e3bb9582e39803550e3a7a99e5f490b7baa8205f (lokal = .69)
- start1.sh 023fad7a96d8a2574e410d0b1ef3410ba84e95471c32fecd594de511639ad644
- start2.sh acbefdc9a0a28e8eff84e966030d725f345502a1dc27d8aee439d4e8482236ea
- start3.sh f682fed9675d4e48dfb8a3cb124bcda87d6bd761cd68596498a71fef4a6a23c6
- rauch1.sh ed59906b221f9ed73587fd3634b46a9c0bce49109ece656e0e694523abf4ac0a, rauch2.sh
  7d269189236c5ed53b1a77507c58c0ee26a98d6de813c01819828be3f0f563c3
