# R33 Messseite: Plan (Code-Agent, Blindtest weit draussen, beta = 1)

- Code-Agent (Claude, Anthropic) im Auftrag der Leitung claude-primary. Beginn 2026-10-03 14:01:28 CEST (date). Plan
  geschrieben ab 14:26:34 CEST (date), nach dem Rauchlauf (Abschnitt 2), vor jeder echten Rechnung. Zeitbox 150 min
  (bis 16:31 CEST).
- Ordner: lokal coordination/runden-v3/RUNDE-33/r33-messung/ (code/, lauf-69/); .69:
  /home/fmh/fmhc-physics-remote/runde33-messung/ (Code-Kopien, rauch/, lauf/). Die .69-Uhr laeuft in UTC.
- Markierungen: [L] Vorgabe der Leitung (Auftrag, RUNDE-33.md), [A] Festlegung des Code-Agenten.
- **Blindheit:** Nicht gelesen: BASELINE-R33-VERSIEGELT.json, BASELINE-HASH-AN-CODEX.txt, Codex' versiegelte Datei
  und alle Codex-Nachrichten, nichts unter coordination/resonance-20260930/. Vorsorglich ebenfalls nicht gelesen:
  RUNDE-31.md, RUNDE-32.md, in RUNDE-31/phase-3d-blind/ die Dateien BASELINE-VERSIEGELT.json,
  NACHTRAG-VERSIEGELT.json, VERGLEICH-LEITUNG.json, AUSGANG-AN-CODEX.txt, PROTOKOLL-VORSCHLAG-AN-CODEX.txt.
  Gelesen: runden-v3/README.md, RUNDE-33.md (enthaelt die Form der Primaervorhersage ohne Konstanten),
  RUNDE-31/phase-3d-blind/ KARTE.md, PLAN.md, ERGEBNIS.md, code/bic2_3d_suche_v2.py, code/start.sh,
  code/rauch2.sh, lauf-69/sprossen.json, runden-v3/kleintest.sh.

## 1. Ziel und Protokoll [L]

- beta = 1, Fortsetzungen k = -3, -4, ..., -25 der R31-Zaehlung nach kleinerem eps (eps = omega^2 - 3/4,
  z = 1/eps). Ziele des Tors: k = -10, -18, -25. Alle 23 Fortsetzungen werden der Reihe nach bestimmt, damit die
  Indizes eindeutig sind.
- Start: k = -2 aus RUNDE-31/phase-3d-blind/lauf-69/sprossen.json (sha256 4267791b7d2dfaae4bc8da28ab80ce30d0f0bf26e0e24c97f1c998fb911a1005),
  z = 40.18844229618716 (h = 0,02), Umlauf -1.
- **Fenster fuer k:** [z_(k+1) + b/2, z_(k+1) + 3b/2] mit b = b_inf = 2,6186, z_(k+1) = zuletzt gemessene Lage
  (woertlich; kein anderer Schrittwert, keine Formel).
- Fehlende oder mehrdeutige Fortsetzung: dieses k und alle folgenden sind UNRESOLVED; nichts nachtraeglich auffuellen.
- Alle Fortsetzungen bleiben versiegelt, bis beide Seiten ihren Ergebnis-Hash gemeldet haben. Abschlussbericht und
  ERGEBNIS-OHNE-ZAHLEN.md nennen keine Ziel- oder Zwischenwerte (nur Status, Anzahl, Unsicherheitsklassen, Hash).

## 2. Rauchlauf (vor dem Einfrieren; nur bekannte Sprossen und z >= 112) [A]

- code/rauch.sh, .69, Spuren cpu, cpu2, cpu3, cpu4, 12:20:43 bis 12:23:22 UTC, 13 Aufrufe, alle rc = 0; dazu vorher
  eine Syntaxprobe (py_compile) und nachher ein zweiter kette-Aufruf auf den Rauchdaten (Code-Endfassung, Abschnitt 9).
  Kein Lauf im Bereich 41,1 <= z <= 106 (dort liegen alle moeglichen Zielfenster).
- **Profil:** skalare Bisektion gegen bic2.profil bei z = 40,188 (k = -2) und z = 112: s gleich auf 9e-14 bzw. 0,
  f bis zum Schnitt und mit Schwanz gleich auf 7,5e-13 bzw. 0, gleiches j_cut und r_halb; 0,3 bis 0,5 s statt 15 bis
  24 s.
- **Gleichwertigkeit mit RUNDE-31** (z = 36,28 und 38,88, zwischen bekannten Sprossen): Nullstelle von L1 = Nullstelle
  von L(y_b) des direkten Verfahrens auf 2e-15; Vorzeichen von s gleich; s mit n_orth = 0, 2, 8, 32 gleich auf ~1e-15
  relativ.
- **Wachstum und erreichbare Genauigkeit:** Die geschlossene Kanalloesung waechst bis zum Anschluss um
  10^5,46 / 10^5,86 / 10^6,25 (k = 0, -1, -2; R_wand 17,9 bis 20,5) und um 10^17,0 bis 10^17,3 bei z = 112 bis 115
  (R_wand 56,5 bis 58,0), also etwa 10^(0,30 R). Fuer die Ziele (R ~ 31, 41, 51) folgt 10^9,4, 10^12,5, 10^15,2.
  - Das direkte Verfahren (RUNDE-31) ist bei z = 112 bis 115 unbrauchbar: s_direkt = -1,9e-10 / -1,9e-10 / -1,7e-10
    gegen stabilisiert -7,3e-13 / -6,4e-13 / +3,0e-13 (bei z = 115 falsches Vorzeichen); ebenso n_orth = 0 (nur
    Schluss-Orthonormierung): -3,6e-11 / -2,5e-11 / +1,3e-12.
  - Stabilisiert: n_orth = 2 und 32 gleich auf 4e-15 relativ, gegen n_orth = 8 (andere Interpolationspunkte) auf
    1,2e-12 relativ. Groesster Einzelterm von L(q2) ~ |s| (keine Ausloeschung), Rundungsrauschen von s ~1e-15 relativ.
- **Kontrollen (Auftrag: k = 0, -1, -2 auf < 1e-6 in omega^2):**

  | Sprosse | h = 0,04 gegen R31 h004 | h = 0,02 gegen R31 h002 | Umlauf Kreuzung / Phase (groesster Sprung) |
  |---|---|---|---|
  | k = 0 | 0,7785854193053 (+7,6e-13) | 0,7785854399004 (+5,5e-13) | -1 / -1,0000 (0,234 rad) |
  | k = -1 | 0,7766066086376 (-1,5e-12) | 0,7766066277135 (-2,3e-12) | +1 / +1,0000 (0,287 rad) |
  | k = -2 | 0,7748827580576 (+4,7e-12) | 0,7748827758194 (+4,6e-12) | -1 / -1,0000 (0,283 rad) |

  - k = -1 lief als ganze Kette (zeilen mit dz = b_inf/8 -> wurzel -> h002 -> Randprobe -> kette mit Start k = 0): das
    Fenster [z(k=0) + b/2, z(k=0) + 3b/2] ergab genau eine Wurzel, z = 37,584620297 (R31: 37,58462029395), Klasse A
    (Unsicherheit 2,7e-5 in z), alle harten Kriterien erfuellt; Randprobe -6e-16.
  - Rauschmass am Kandidaten 1,7e-18 bis 2,3e-18 in omega^2 (R31 direkt: 4e-13 bis 2e-12).
- **Laufzeiten:** Zeile (600 + 401 rho-Punkte, zwei Zoomrunden) 3,9 s bei R ~ 19, 15 s bei R ~ 57 mit Vergleichen
  (ohne ~10 s); wurzel-Aufruf mit einer Klammer 26 bis 41 s bei R ~ 18 bis 20 (h = 0,04 mit Rechteck, h = 0,02,
  Randprobe).

## 3. Verfahren (code/r33_stab.py) [A]

- Physik unveraendert aus bic2_3d_suche_v2.py (RUNDE-31, importiert): Profil-Regeln (Einteilung, RK4, Startreihe,
  Schnitt, Schwanz), lin_multi (Profil mit Schritt h/2, Aussenrand f(R) = f_rand f0 mit f_rand 1e-8 bei h = 0,04 und
  1e-6 bei h = 0,02, Anschluss r_m), RK4-Schema und Startreihe von direkt_m, abklingende Jost-Loesung z2 und
  L(y) = Omega(y, z2) exp(-kappa R).
- **Stabilisiert (Godunov/Conte):** y_a, y_b alle 8 RK4-Schritte und am Anschluss per Gram-Schmidt (zweifach)
  orthonormiert, q1 = y_b/|y_b|, q2 = Anteil von y_a senkrecht zu q1. Wegen y_b = T11 q1, y_a = T12 q1 + T22 q2
  (T11, T22 > 0): L1 = L(q1) hat dieselben Nullstellen in rho wie L(y_b); s = L(q2) an der Nullstelle von L1 hat
  dasselbe Vorzeichen wie s in RUNDE-31; W = L(q2) + i L(q1) hat dieselben Nullstellen und Umlaufzahlen wie
  L(y_a) + i L(y_b).
- **Zeile omega^2 = x:** Profil skalar (Schritt h/2); R und r_m fest je Lauf (R = groesster Einzelrand der Startzeilen
  plus r_zusatz, r_m = Median der R_halb). rho-Abtastung 600 Punkte im ganzen Fenster [1 - omega + 0,002;
  1 + omega - 0,002] plus 401 Punkte in rho_ref +- 0,04; je Vorzeichenwechsel von L1 zwei Zoomrunden mit 201 Punkten;
  rho_f und s durch lineare Interpolation von L1 und L2 auf der Endklammer. Zielast = Nullstelle naechst rho_ref
  innerhalb 0,04. rho_ref = 1,79751388 + 0,881 (eps - 0,02488278) (lineare Fortsetzung aus den R31-Werten k = 0 .. -2;
  nur Astwahl, keine Lagevorhersage).
- **Abtastung (Phase 1):** feste Zeilen z_j = z0 + j dz, dz = b_inf/8 = 0,327325, z0 = z(k = -2) + b_inf/2 - dz =
  41,17041729618716, j = 0 .. 208 (bis z = 109,25). 13 Abschnitte zu 17 Zeilen (j = 16c .. 16c + 16; benachbarte
  Abschnitte rechnen ihre Randzeile beide).
- **Wurzeln (Phase 2):** jeder Vorzeichenwechsel von s zwischen benachbarten Zeilen (erste Zeile je z massgeblich)
  wird verfeinert: beide Zeilen neu (eigenes R, r_m), Wechsel muss sich bestaetigen; Illinois in omega^2 (neues Profil
  je Schritt; rho-Abtastung 100 Punkte plus 201 Punkte in +-2e-4 um das interpolierte rho) bis Klammer <= 1e-10 oder
  30 Schritte oder Zeit. Lage = lineare Interpolation von s auf der Endklammer.
- **Umlauf (Phase 2):** Rechteck auf den zwei Startzeilen (x_lo < x_hi), rho_c = rho*, halbe Hoehe
  drho = min(0,03; max(0,01; 2 |Aststeigung| halbe Klammer)), Umlauf gegen den Uhrzeigersinn wie praez_rechteck;
  je rho-Seite 61 gleichabstaendige Punkte plus geometrische Haeufung (+-10^m, m = -14 .. 2) um die Nullstelle von L1
  der Zeile, dann bis 30 Halbierungsrunden fuer Phasenspruenge > 0,3 rad. Massgeblich die Kreuzungszaehlung
  (1/2 Summe sgn L2 sgn Delta L1 an den Wechseln von L1, wie R31); Phase aufgeloest, wenn groesster Sprung < 0,4 rad.
- **Gitter (Phase 3):** jede konvergierte h = 0,04-Wurzel neu auf h = 0,02 aus der engen Klammer x* +- 1e-5
  (Wechsel muss sich auf h = 0,02 zeigen), Illinois wie oben.
- **Randprobe (Phase 3):** jede konvergierte Wurzel auf h = 0,04 mit Aussenrand R + 20, Klammer x* +- 1e-5.

## 4. Kriterien je Fenster (kette, mechanisch) [A]

Erweitertes Fenster = [lo - dz, hi + dz]. Ein Fenster ist **OK**, wenn alle harten Kriterien gelten; sonst ist k
UNRESOLVED und alle folgenden ebenfalls.

- **Hart, Abtastung und Ast:**
  - (a1) Die Abtastung deckt das erweiterte Fenster; groesste Luecke <= dz.
  - (a2) Jede Zeile im erweiterten Fenster: genau eine Nullstelle von L1 im ganzen rho-Fenster, Zielast vorhanden,
    gleiche Richtung von L1 in allen Zeilen, |Delta rho| <= 0,03 zwischen Nachbarzeilen. Damit liegen alle Kandidaten
    (gemeinsame Nullstellen von L1 und L2) auf diesem einen Ast.
  - (a3) Doppelt gerechnete Randzeilen haben dasselbe Vorzeichen von s.
  - (a4) Rauschreserve: |s| > 1e-12 * groesster Einzelterm von L(q2) in jeder Zeile (1000-fach ueber 1e-15).
  - (a5) Keine Beinahe-Nullstelle: an jeder Zeile, die nicht an einen Wechsel grenzt, |s| >= 0,05 * groesstes |s|
    desselben Abschnitts.
- **Hart, genau eine Sprosse:**
  - (b1) Jeder Vorzeichenwechsel im erweiterten Fenster ist verfeinert; genau eine verfeinerte Wurzel liegt in [lo, hi].
  - (b2) Wurzel h = 0,04 konvergiert (Klammer <= 1e-10), Wechsel im Wurzellauf bestaetigt, Ast dort konsistent.
  - (b3) Umlauf (Kreuzung) +-1 und Vorzeichen entgegengesetzt zur vorigen Sprosse (k = -3: +1, da k = -2: -1).
  - (b4) h = 0,02 konvergiert mit bestaetigtem Wechsel; |omega^2(h002) - omega^2(h004)| <= 1e-6.
  - (b5) Unsicherheit in z < 0,05 und Abstand der Lage zu beiden Fensterraendern > Unsicherheit in z.
- **Berichtet, nicht entscheidend:** Phasenumlauf (aufgeloest und gleich der Kreuzung), Randprobe, Kernwachstum,
  R_wand, R_halb_S0, rho, Rauschmass.
- Uebersehene Zwischenkandidaten: Ein zusaetzliches Paar muesste innerhalb eines Zeilenabstands dz = b_inf/8 zweimal das
  Vorzeichen von s wechseln, ohne dass eine Nachbarzeile unter 5 % des Abschnittsmaximums faellt (a5); das schliesst
  die Abtastung nicht beweisartig aus, ist aber gebunden. Eine Netto-Umlaufzahl allein wird nicht verwendet.

## 5. Lage und Unsicherheit [A]

- Berichtete Lage: h = 0,02 (h002), eps = omega^2 - 3/4, z = 1/eps; das naechste Fenster setzt an dieser Lage an.
- unsicherheit_omega2 = |h002 - h004| + groessere Endklammer + groesseres Rauschmass
  (1e-15 * groesster Einzelterm / |ds/domega^2| der Startklammer) + |Randprobe - h004|; unsicherheit_z =
  unsicherheit_omega2 / eps^2.
- Klassen: A < 1e-3, B < 1e-2, C < 5e-2 (alle in z); D >= 5e-2 gilt als gescheitert (b5).

## 6. Abbruch und Budget [L, A]

- Nur .69 ueber kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4 (hoechstens vier zugleich; nicht cpu5, keine GPU), je
  Aufruf <= 600 s, 1 Kern, 4 GB; intern Budget 540 s, Reserve 30 s.
- Gesamtrahmen: Wanduhr <= 2 h ab Start von code/start.sh. Geplant: Abschnitt 8.
- Abbruch: Laeuft die Kette bis 16:05 CEST nicht durch, rechne ich kette auf dem vorhandenen Stand; was fehlt, ist
  UNRESOLVED (Kriterien oben). Ein ausgefallener Aufruf wird nicht von Hand ersetzt; die eingebaute Wiederholung
  (--fortsetzen) ist die einzige Nachholung. Faellt eine Genauigkeitsgrenze (b5) ab einem k, wird das Scheitern so
  eingefroren.
- Reicht die Abtastung fuer das Fenster k = -25 nicht (z > 109,25 noetig), gilt (a1) als verletzt; keine Zusatzzeilen.

## 7. Ausgabe und Versiegelung

- kette schreibt lauf/MESSUNG-R33-VERSIEGELT.json auf der .69: je k Status, Fenster, omega2, eps, z, Umlauf
  (Kreuzung, Phase), Unsicherheit (omega^2, z), Klasse, alle Kriterien, Gitter- und Randwerte; Gesamtstatus
  (vollstaendig / teilweise UNRESOLVED ab k = ... / gescheitert).
- Kopie nach lauf-69/MESSUNG-R33-VERSIEGELT.json, chmod a-w, sha256 in MESSUNG-HASH.txt. Rohdaten bleiben auf der .69.
- ERGEBNIS-OHNE-ZAHLEN.md: Ablauf, Kriterien, Status, Kontrollen k = 0, -1, -2, Selbstanzeigen, Einfach gesagt; keine
  Ziel- oder Zwischenwerte.

## 8. Laufliste (code/start.sh, einmal per nohup)

| Phase | Aufrufe | Spuren | geschaetzt (Rechenzeit) |
|---|---|---|---|
| 1 zeilen | 13 Abschnitte z-c0 .. z-c12 | cpu: c0, c4, c8, c12; cpu2: c1, c5, c9; cpu3: c2, c6, c10; cpu4: c3, c7, c11 | 221 Zeilen x 4 bis 11 s, ~30 min |
| 2 wurzel h = 0,04 | 8 Teile w-p0 .. w-p7 (+ 8 Wiederholungen --fortsetzen) | je Spur zwei Teile | ~26 Wurzeln x 40 bis 80 s, ~25 min |
| 3 gitter h = 0,02 | 8 Teile g-p0 .. g-p7 (+ 8) | je Spur zwei Teile | ~26 x 60 bis 120 s, ~35 min |
| 3 Randprobe R + 20 | 8 Teile r-p0 .. r-p7 (+ 8) | je Spur zwei Teile | ~26 x 40 bis 80 s, ~25 min |
| 4 kette | 1 | cpu | < 1 min |

- Zusammen 38 Aufrufe plus 24 Wiederholungen (leer, wenn nichts fehlt: je ~5 s). Rechenzeit geschaetzt ~2 h CPU,
  Wanduhr ~30 bis 45 min (obere Grenze 2 h).
- Nach dem Einfrieren keine Aenderung an Plan, Code und Skripten; Abweichungen offen mit Grund und Zeit im Ergebnis.

## 9. Code und Skripte (sha256 vor dem Einfrieren)

- code/r33_stab.py fa7a06ec5f3e7c00b9e0b16abddda9f9e3bcbf1d68fa7ad453690ea457644182 (lokal = .69). Die Rauchlaeufe
  zeilen/wurzel liefen mit der Vorfassung e1a04938...; die Endfassung aendert nur kette (Begruendungstext bei fehlender
  Abdeckung, Kriterium a4) und wurde auf den Rauchdaten erneut gerechnet (gleiches Ergebnis, a4 erfuellt).
- code/bic2_3d_suche_v2.py 6beabc3f0d499df31a20c21fc9a35a2dc028117be5df05badf7863c22eb53c71 (= RUNDE-31, unveraendert)
- code/start.sh 24624192755645198959c16e1bdc930b5c26984ef13371cbc8ff1380dbf4ff4c
- code/rauch.sh 8d2e63419f456a0239478e3303d4c5f27757671767b1c6d158f64f125ffec772
