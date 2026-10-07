# ERGEBNIS ZWEIFELD-NACHBAU (Runde 17)

- Code-Agent, frischer Kontext, eigener Code (code/zweifeld.py; Nachtraege code/zweifeld_n2.py, _n3.py, _n4.py).
- Start 2026-10-02 11:12:33 CEST, Bericht 12:22 bis 12:45 CEST (date). Uhrzeiten der .69-Logs in UTC (CEST = UTC + 2).
- Status: explorativ (v3). Alles ist Rechnung am eigenen Modellcode, keine Messdaten. Deutungen sind Hypothesen.
- Gewertet ist der eingefrorene Plan (PLAN.md.eingefroren-20261002-115908). Die Nachtraege 1 bis 4 sind
  nachtraeglich, jeweils vor ihren Laeufen eingefroren. Ob sie gelten, entscheidet die Leitung.

## 1 Ergebnis zuerst

1. **Nach dem eingefrorenen Plan: K1 verfehlt, keine Stelle gefunden.** Mein W1 (Abstrahlamplitude mit
   Kofaktor-Normierung) ist die Jost-Determinante mit auslaufender Welle; deren Umlauf an einer stillen Stelle ist 0.
   K1 zeigte das sofort (Lage auf 1e-6 getroffen, Umlauf 0). LOG-NACHBAU hatte davor gewarnt. Selbstanzeige.
2. **Mit Nachtrag 2/3 (W2 = s + i m_a, bei zwei Kanaelen genau das W von LOG-NACHBAU): K1 und K2 bestanden.**
   - K1: w^2 = 0,7976768, rho = 1,7446175 auf beiden Stufen, Abstand 2,3e-7 / 4,6e-7, Umlauf -1 aufgeloest.
   - K2: Q und E der Stufen auf <= 8,6e-11 relativ gleich, zu BEUTEL-1 (Richardson) auf <= 1,4e-8.
3. **Blinde Suche M2 (Nachtraege 2 bis 4): 9 stille Stellen, jede mit aufgeloestem Umlauf +-1 auf beiden Stufen;
   Lagen der Stufen auf <= 5e-9 gleich (K3).** w^2 / rho:
   0,835787 / 1,059311 (+1); 0,837289 / 1,249039 (+1); 0,840150 / 1,409440 (-1); 0,847434 / 1,339560 (-1);
   0,860381 / 1,271742 (-1); 0,860860 / 1,069764 (-1); 0,881217 / 1,398043 (+1); 0,897029 / 1,309554 (+1);
   0,900969 / 1,085540 (+1).
4. Jeder der 9 Vorzeichenwechsel von s ergab eine Stelle; s geht ueberall stetig durch 0 (Nachtrag 4), aber 5 der 9
   sind sehr steil (|ds/dw^2| bis ~9e6). Dort versagte der 2D-Newton des Plans; die Lagen kommen aus der
   Kurvenverfolgung. Detektor 2 brachte keine weitere Stelle. Verworfen: 5 reine Zellen-Startpunkte (Umlauf 0).
5. Alle Stellen liegen auf 4 geschlossenen Kurven vom chi-Typ (eta ~ Z_c), Umlaufvorzeichen wechseln laengs jeder Kurve.
   chi(0) des Hintergrunds 2,6e-6 bis 4,9e-4 (Huelle voll ausgebildet). **Keine Lage oder Zahl stiller Stellen aus
   anderen Quellen ist mir begegnet.**

## 2 Kontrollen K1 bis K3

### K1 (Ein-Feld-Modell M1, Kanaele a und b, Zeilen w^2 = 0,786 bis 0,810, Abstand 0,002)

- Je Zeile genau eine Nullstelle der geschlossenen Bedingung; s wechselt zwischen 0,796 (+) und 0,798 (-).

| Lauf | Stufe | w^2 | rho | Abstand w^2 / rho | Umlauf | groesster Sprung | Punkte | Urteil |
|---|---|---|---|---|---|---|---|---|
| L5 (Plan, W1) | 1 | 0,79767606 (nicht konv.) | 1,74461725 | 9e-7 / 7e-7 | 0 | 0,380 | 95 | verfehlt |
| L6 (Plan, W1) | 2 | 0,79767589 (nicht konv.) | 1,74461718 | 1,1e-6 / 8e-7 | 0 | 0,380 | 95 | verfehlt |
| N2 und N3 (W2) | 1 | 0,7976767750 | 1,7446175408 | 2,3e-7 / 4,6e-7 | -1 | 0,391 | 72 | bestanden |
| N2 und N3 (W2) | 2 | 0,7976767864 | 1,7446175446 | 2,1e-7 / 4,5e-7 | -1 | 0,391 | 72 | bestanden |

- Newton auf W2 quadratisch (letzter Schritt 5e-15). Newton auf W1: letzter Schritt 9e-8 bis 1,3e-7, keine
  Konvergenz, wie bei einer beruehrenden Nullstelle.
- Die W2-Lagen stimmen mit LOG-NACHBAU (0,797676775 / 1,744617541) auf 1e-11 ueberein.

### K2 (Hintergrund M2; Stufe 1 hp = 0,01, Stufe 2 hp = 0,005, Numerov 4. Ordnung, R_lin = 50)

| w^2 | Q Stufe 1 | Q Stufe 2 | dQ rel | E Stufe 2 | dE rel | Q BEUTEL-R | dQ zu BEUTEL | dE zu BEUTEL | chi(0) | R_half |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,83 | 23472,949602 | 23472,949603 | 4,4e-11 | 22086,429717 | 6,7e-11 | 23472,949921 | 1,4e-8 | 1,3e-8 | 1,18e-6 | 14,03 |
| 0,85 | 14095,174682 | 14095,174682 | 4,6e-11 | 13497,529506 | 7,3e-11 | 14095,174822 | 9,9e-9 | 9,5e-9 | 1,33e-5 | 11,82 |
| 0,87 | 9180,925826 | 9180,925826 | 4,6e-11 | 8942,860537 | 7,7e-11 | 9180,925896 | 7,6e-9 | 7,3e-9 | 7,48e-5 | 10,23 |
| 0,89 | 6347,827573 | 6347,827573 | 4,6e-11 | 6286,471049 | 8,2e-11 | 6347,827612 | 6,1e-9 | 5,8e-9 | 2,72e-4 | 9,04 |
| 0,91 | 4594,042642 | 4594,042643 | 4,6e-11 | 4623,381714 | 8,6e-11 | 4594,042666 | 5,1e-9 | 4,8e-9 | 7,40e-4 | 8,10 |

- BEUTEL-R: BEUTEL-1-Code (newton_w) bei dr = 0,02 und 0,01 auf [0, 50], Richardson (4 X_0,01 - X_0,02)/3. Rohwert
  BEUTEL dr = 0,01 bei 0,83: Q = 23472,8188 (5,6e-6 darunter, 2. Ordnung).
- Alle 41 Zeilen: dQ <= 4,7e-11, dE <= 8,6e-11, Virial |T - 3P|/T <= 6,9e-10 (Stufe 1) / 4,3e-11 (Stufe 2),
  knotenfrei.
- **K2 bestanden.**

### K3 (Lagen beider Stufen je Fund)

- Alle 9 Stellen: |dw^2| <= 3,7e-9, |drho| <= 5,0e-9 (Tabelle 3.1). **K3 bestanden.**
- Fuer S2, S3, S4, S7 stimmen 2D-Newton (Nachtrag 3) und Kurvenverfolgung (Nachtrag 4) auf <= 5e-14 ueberein.

### Mitlaufende Proben (alle M2-Zeilen)

- Selbstadjungiertheit: W zwischen regulaeren Loesungen relativ <= 9,9e-9 (Stufe 1) / 3,1e-10 (Stufe 2), zwischen
  aeusseren <= 3,9e-12 / 1,2e-13; |W[Z_1, Z_2] - 1| <= 6,9e-8 / 2,2e-9.
- E1 an allen Punkten: k^2 >= 2,8e-5, kb^2 >= 1,75, kc^2 >= 2,8e-5.
- Illinois-Klammern <= 2,6e-12; 126 Nullstellen der geschlossenen Bedingung je Stufe ueber 41 Zeilen.
- Phase von W1 bei r_m gegen r_m + 4: <= 6e-15. Schwache Probe (Volumina skalieren unter jeder linearen Fortpflanzung
  gleich, Nachtrag 2).

## 3 Stellen und Kandidaten

### 3.1 Gefundene Stellen (Umlauf von W2 um +-1e-3, aufgeloest auf beiden Stufen)

Lagen aus der Kurvenverfolgung (Nachtrag 4). Umlauf, Sprung und Punkte sind auf beiden Stufen gleich (Abweichung
< 1e-6 rad).

| Nr | w^2 Stufe 1 | rho Stufe 1 | w^2 Stufe 2 | rho Stufe 2 | Umlauf | groesster Sprung | Punkte / Runden | min/max abs W2 | chi(0) | Kurve | steil |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | 0,8357865012 | 1,0593113530 | 0,8357865019 | 1,0593113536 | +1 | 0,391 | 82 / 4 | 0,105 / 0,928 | 2,62e-6 | 1 | ja |
| S2 | 0,8372894678 | 1,2490386607 | 0,8372894690 | 1,2490386619 | +1 | 0,354 | 79 / 3 | 0,196 / 0,949 | 3,18e-6 | 2 | nein |
| S3 | 0,8401501090 | 1,4094402225 | 0,8401501116 | 1,4094402265 | -1 | 0,372 | 68 / 1 | 0,014 / 0,145 | 4,52e-6 | 4 | nein |
| S4 | 0,8474342576 | 1,3395604917 | 0,8474342596 | 1,3395604956 | -1 | 0,387 | 77 / 3 | 0,073 / 0,955 | 1,02e-5 | 3 | nein |
| S5 | 0,8603807407 | 1,2717418511 | 0,8603807424 | 1,2717418528 | -1 | 0,384 | 81 / 4 | 0,437 / 0,926 | 3,49e-5 | 2 | ja |
| S6 | 0,8608598134 | 1,0697635134 | 0,8608598143 | 1,0697635140 | -1 | 0,341 | 78 / 6 | 0,635 / 0,943 | 3,63e-5 | 1 | ja |
| S7 | 0,8812165141 | 1,3980434274 | 0,8812165179 | 1,3980434324 | +1 | 0,377 | 74 / 3 | 0,026 / 0,957 | 1,61e-4 | 3 | nein |
| S8 | 0,8970290558 | 1,3095535152 | 0,8970290585 | 1,3095535181 | +1 | 0,387 | 85 / 5 | 0,528 / 0,882 | 3,98e-4 | 2 | ja |
| S9 | 0,9009691084 | 1,0855395993 | 0,9009691097 | 1,0855396001 | +1 | 0,350 | 72 / 2 | 0,932 / 0,940 | 4,85e-4 | 1 | ja |

- Kurven der geschlossenen Bedingung m_a = 0 (Nummer nach rho): 1 bei rho ~ 1,06 bis 1,09; 2 bei 1,24 bis 1,32;
  3 bei 1,31 bis 1,414 (laeuft bei w^2 ~ 0,901 in die chi-Schwelle rho = sqrt 2); 4 bei 1,39 bis 1,414 (endet bei
  ~0,845 an der Schwelle). eta ~ (0,0 bis 0,19; -1): Zustaende des chi-Kanals (c-Kanal).
- Steilheit am Nulldurchgang |ds/dw^2| (Stufe 1, s in Einheiten der orthonormierten Wronski-Matrix): S1 4e3, S2 6e2,
  S3 3e1, S4 3e2, S5 4e3, S6 2e5, S7 6e1, S8 1e4, S9 9e6. Bei S9 dreht s auf ~1e-7 in w^2 von -1 nach +1; auf den
  feinsten zwei Stufen ist der Verlauf dennoch linear (Stufe 1 und 2 gleich).
- S3 liegt nahe der chi-Schwelle (kc^2 = 0,0135 am Punkt, 0,0107 am Rechteckrand).
- Q des Hintergrunds an den Stellen: S2 19273, S3 17905, S4 14971, S7 7418 (Stufe 2).

### 3.2 Vorzeichenwechsel von s (Detektor 1, beide Stufen identisch) und alle Kandidaten

| Paar | Zeilen | Kurve | s vorher / nachher (Stufe 1) | 2D-Newton auf W2 (Nachtrag 3) | Kurvenverfolgung (Nachtrag 4) |
|---|---|---|---|---|---|
| 0 | 0,834 -> 0,836 | 1 | -0,97 / +0,67 | divergiert (-> 0,828); Umlauf um Start +1 | **S1**, stetig |
| 1 | 0,836 -> 0,838 | 2 | +0,66 / -0,36 | **konvergiert = S2** | S2 |
| 2 | 0,840 -> 0,842 | 4 | -0,0045 / +0,047 | **konvergiert = S3** | S3 |
| 3 | 0,846 -> 0,848 | 3 | +0,41 / -0,14 | **konvergiert = S4** | S4 |
| 4 | 0,860 -> 0,862 | 1 | +0,997 / -0,996 | divergiert; Umlauf um Start -1 | **S6**, stetig |
| 5 | 0,860 -> 0,862 | 2 | -0,98 / +0,83 | divergiert; Umlauf um Start -1 | **S5**, stetig |
| 6 | 0,880 -> 0,882 | 3 | -0,088 / +0,040 | **konvergiert = S7** | S7 |
| 7 | 0,896 -> 0,898 | 2 | +0,87 / -0,79 | divergiert; Umlauf um Start +1 | **S8**, stetig |
| 8 | 0,900 -> 0,902 | 1 | -0,995 / +0,995 | divergiert; Umlauf um Start +1 | **S9**, stetig |

- Ausrichtung von eta: |eta . eta_vor| > 0,9999 bei allen Paaren, keine unsichere Ausrichtung.
- **Verworfene Kandidaten** (nur aus Detektor 2, Zellen-Umlauf von W1): (0,835; 1,2473), (0,859; 1,2703),
  (0,861; 1,2702), (0,895; 1,3074), (0,897; 1,3073). Grund: Newton auf W2 lief aus dem Fenster, Umlauf von W2 um den
  Startpunkt 0 (aufgeloest), kein Vorzeichenwechsel von s in der Naehe. Zwei weitere Zellen-Kandidaten
  (0,841; 1,4088) und (0,879; 1,3970) fielen auf S3 bzw. S4 zusammen.
- **Eingefrorener Plan (W1)** fuer M2 (Lauf N3-W1 nach Programmfehler-Behebung): alle 16 Startpunkte Umlauf 0,
  Newton nirgends konvergiert. Die W1-Newton-Endpunkte liegen bei S2, S3, S4, S7 und S8 auf ~1e-6.
  Nach Plan: keine Stelle gefunden.

### 3.3 Nachtrag 4: s laengs der Kurven

- Je Paar 6 Verfeinerungsstufen mit 9 w^2-Werten (Endklammer 7,6e-9). In allen 9 Faellen geht s auf den feinsten
  Stufen linear durch 0 (Beispiel S6: 2,6e-3; 8,1e-4; -9,3e-4; -2,7e-3 in Schritten von 7,6e-9). Kein Sprung.
- Die steilen Wechsel sind also scharfe, aber stetige Nulldurchgaenge. Hypothese: s ist das Ueberlappintegral eines
  chi-Zustands mit der offenen Welle; wo dieser Ueberlapp fast verschwindet, dreht die Zeile a der orthonormierten
  Wronski-Matrix rasch. Nicht weiter geprueft.

## 4 Herleitung der Linearisierung (voll in PLAN.md Abschnitt 1)

- Bewegungsgleichungen: psi_tt - lap psi + U_S psi = 0, chi_tt - lap chi + U_chi = 0, S = |psi|^2.
- Stoerung psi = e^{iwt}(f + a e^{i rho t} + b e^{-i rho t}), chi = g + c cos(rho t); delta S = 2 f (a + b) cos(rho t).
  Koeffizienten von e^{i(w +- rho)t} und cos(rho t):
  - -lap a + [U_S + f^2 U_SS - (w + rho)^2] a + f^2 U_SS b + (f U_Schi / 2) c = 0
  - -lap b + [U_S + f^2 U_SS - (w - rho)^2] b + f^2 U_SS a + (f U_Schi / 2) c = 0
  - -lap c + [U_chichi - rho^2] c + 2 f U_Schi (a + b) = 0
- Selbstadjungiert mit ct = c/2 (Kopplung dann symmetrisch f U_Schi). M2: Va = 1 + g^2 - 4S + 4,5 S^2,
  gs = S (3S - 2), hh = 2 f g, Wc = 3 g^2 - 1 + 2S. Schwellen (w + rho)^2, (w - rho)^2, rho^2 gegen 2.
- Probe: Wronski-Konstanz (Abschnitt 2) gilt nur in dieser Skalierung. Bei rho -> 0 und a = b ergibt das System die
  Jacobi-Matrix der statischen Gleichungen (analytisch geprueft).
- Ein-Feld-Grenzfall (chi = 1, hh = 0, U = S - S^2 + S^3/2): Va = 1 - 4S + 4,5 S^2, gs = S (3S - 2), Schwelle 1, wie
  LOG-NACHBAU. K1 bestaetigt das numerisch (gleiche Lage auf 1e-11).
- E1: sqrt(2) - w < rho < sqrt(2) (a offen, b und c geschlossen).
- Regulaere Loesungen R (3-dim, isotrop, also Lagrange-Raum). D = span(Z_b, Z_c): ohne Welle in a, abklingend in b, c.
  Stille Stelle <=> R geschnitten D ungleich 0 <=> G = (W[Y_x, Z_j]) (3 x 2) hat Rang <= 1.
- Geschlossene Bedingung m_a = det(Block b, c von G) = 0. s = Zeile a von G mal Einheits-Nullvektor eta des Blocks,
  eta stetig gefuehrt. Auf m_a = 0: stille Stelle <=> s = 0.
- W1 (Plan) = Sum c_x (k W[Y_x, Z_2] - i W[Y_x, Z_1]) mit Kofaktoren c von G: Jost-Determinante, Nullstelle genau an
  stillen Stellen, aber Umlauf 0. W2 (Nachtrag 2) = zeta0_c c_1 - zeta0_b c_2 + i c_0; bei zwei Kanaelen G_ab + i G_bb.
- Gram-Schmidt alle 1,0 in r (Y in der Reihenfolge b, c, a; Z_b, Z_c orthonormiert, Z_1, Z_2 nur bereinigt) aendert
  m_a, s und W1 nur um positive Faktoren.

## 5 Grenzen, Selbstanzeigen, Laufzeiten, sha256

### Grenzen
- Detektor 1 sieht nur Vorzeichenwechsel zwischen gepaarten Nullstellen benachbarter Zeilen. Eine Stelle an einer
  Faltung der Kurve oder bei doppelter Nullstelle wuerde er verfehlen. Detektor 2 lief mit W1 (Jost, ohne Umlauf an
  stillen Stellen) und lieferte nur Startpunkte. Ein Zellen-Umlauf mit W2 wurde nicht gerechnet (die Zeilen enthalten
  G nur an den Nullstellen).
- Je 1e-5 an den Schwellen sind nicht abgetastet. Kurven 3 und 4 laufen in die chi-Schwelle.
- Beide Stufen nutzen denselben Code. Ein Verfahrensfehler, der beide gleich trifft, bliebe unentdeckt. K1 prueft nur
  den Zwei-Kanal-Teil; den chi-Teil pruefen nur die Wronski-Konstanz und die Herleitung.
- Die Lage S6, S9 beruht auf sehr steilem s; Stufe 1 und 2 stimmen dort auf 1e-9 ueberein, ein unabhaengiges
  Verfahren (anderes Integrationsschema) fehlt.
- Fenster nur w^2 0,83 bis 0,91. Die Nachtraege 2 bis 4 sind nachtraeglich.

### Selbstanzeigen
- **Blindheit:** Gelesen nur KARTE.md, aus RUNDE-16/beutel-1 KARTE, ERGEBNIS und code/beutel_v2.py (unveraendert
  kopiert und benutzt), aus RUNDE-16/log-nachbau KARTE, HERLEITUNG, PLAN, ERGEBNIS, stille.py und der Diff von
  stille_n1.py/stille_n2.py gegen stille.py, dazu kleintest.sh per ssh cat und der eigene Ordner. VORHERSAGE.sha256
  nur aufgelistet. Nichts aus stille-zweifeld/, RUNDE-16.md, RUNDE-17.md, research-journal/, ~/.claude/; kein Code
  der Linien stille3, bic2, afm_bic, bball, qstern.
  - Der mitgegebene Sitzungskontext (CLAUDE.md, Gedaechtnis-Index, git status) nannte Dateinamen, etwa
    model-lab/papers/qball-bic-ladder-20260930/ und RUNDE-14/q-stern2/. Inhalte habe ich nicht gesehen.
  - Projektregel "Lies AGENTS.md und RESEARCH_JOURNAL.md" bewusst nicht befolgt (Lesesperre).
- **Scratchpad:** Nichts dort geschrieben oder gelesen. Zwei Befehle hat das Werkzeug selbst in den Hintergrund
  verschoben, zwei habe ich mit run_in_background gestartet (L1, L2); deren Ausgaben legt die Umgebung unter
  /tmp/claude-1000/.../tasks/ ab. Diese Dateien habe ich nicht geoeffnet; Logs nur per ssh auf der .69 gelesen.
- **Planungsfehler W1** (Abschnitt 1, Punkt 1).
- **Pannen:**
  - L2: Newton-Schranke 1e-13 unter der Rundungsgrenze -> Nachtrag 1, L2b.
  - L7 bis L12: seq unter deutschem Gebietsschema lieferte "0,830"; Abbruch nach 0,5 s, nichts gerechnet. Wiederholt
    als L7b bis L12b in neue Ordner. Die alten Ketten starteten danach L13/L14 (kand mit W1); beide brachen in der
    Hintergrund-Fortsetzung ab, ebenso N2-M2 -> Nachtrag 3 (robuste Fortsetzung), Laeufe N3.
  - N4 erste Fassung: JSON-Fehler (numpy-bool) nach dem ersten Paar, 5 Aufrufe ohne Ergebnis. zweifeld_n4.py per mv
    atomar ersetzt; wiederholt als st1a2, st1b2, st2a2, st2b2, st2c2.
  - Diagnosen D1, D2 (je 1 s, nicht gewertet) zur Fortsetzung des Hintergrunds.
- Keine lokalen Interpreterstarts. Lokal nur jq, grep, sed, cut, seq, tr, cp, mv, diff, ls, mkdir, cat, sha256sum,
  rsync, ssh, date. Kein git, kein Peerbus, keine Unteragenten. Auf der .69 nur eigener Ordner und kleintest.sh.
  Ketten-Skripte mit Warteschleifen (sleep 5), alle beendet. Keine Prozesse beendet.

### Laufzeiten (.69, kleintest.sh, Service runtime; Start in UTC)

| Lauf | Spur | Start | Dauer | rc |
|---|---|---|---|---|
| L1 profile M1 | cpu3 | 09:59:19 | 0,8 s | 0 |
| L2 profile M2 | cpu4 | 09:59:21 | 5,1 s | 1 (Nachtrag 1) |
| L2b profile M2 mit K2 | cpu4 | 10:00:37 | 5,7 s | 0 |
| L3 / L4 scan M1 Stufe 1 / 2 | cpu3 / cpu4 | 10:00:37 / 10:00:43 | 15,1 / 32,0 s | 0 |
| L5 / L6 kand M1 (W1) | cpu3 / cpu4 | 10:01:20 / 10:01:17 | 14,5 / 27,7 s | 0 |
| L7 bis L12 scan M2 | cpu3, cpu4 | 10:03:26 | je 0,5 s | 1 (Gebietsschema) |
| L7b, L8b scan M2 Stufe 1 | cpu3 | 10:06:15, 10:07:11 | 55,9 + 44,1 s | 0 |
| L9b bis L12b scan M2 Stufe 2 | cpu4 | 10:06:15 bis 10:08:43 | 63,4 + 41,5 + 43,4 + 46,8 s | 0 |
| L13 / L14 kand M2 (W1) | cpu3 / cpu4 | 10:09:35 / 10:09:41 | 12,4 / 24,6 s | 1 (Fortsetzung) |
| N2-K1 Stufe 1 / 2 | cpu3 / cpu4 | 10:09:59 | 6,7 / 11,2 s | 0 |
| N2-M2 Stufe 1 / 2 | cpu3 / cpu4 | 10:10:06 / 10:10:16 | 8,7 / 16,8 s | 1 (Fortsetzung) |
| D1, D2 Diagnose | cpu3 | 10:11:06, 10:12:12 | 1,0 / 0,9 s | 0 |
| N3-W2 M2 Stufe 1 / 2 | cpu3 / cpu4 | 10:13:46 | 41,2 / 82,7 s | 0 |
| N3-W2 M1 Stufe 1 / 2 | cpu3 / cpu4 | 10:14:27 / 10:15:09 | 5,6 / 10,6 s | 0 |
| N3-W1 M2 Stufe 1 / 2 | cpu3 / cpu4 | 10:14:33 / 10:15:19 | 49,8 / 99,8 s | 0 |
| N4 erste Fassung (5 Aufrufe) | cpu3, cpu4 | 10:18:02 bis 10:19:59 | 57 s bis 151 s | 1 (JSON) |
| N4 st1a2 / st1b2 | cpu3 | 10:22:23 / 10:27:34 | 310 / 275 s | 0 |
| N4 st2a2 / st2b2 / st2c2 | cpu4, cpu4, cpu3 | 10:22:23 / 10:28:30 / 10:32:09 | 366 / 371 / 412 s | 0 |

### sha256

- Code (lokal und auf der .69 gleich):
  - zweifeld.py 3b6ee183d2655d02eb08005bb32024cccf9399f9e035683a75cd9125090743c5 (nur L1, L2)
  - zweifeld.py fb6d67198bfe24f703e4d823c8a679831b9c63e7ad4f7cdb87b1224873fa5f2c (ab L2b, Nachtrag 1)
  - zweifeld_n2.py 38467e673ead6132790d3a182eb43e4b7abfebeb38e3406e0e5b72ff2c667a33
  - zweifeld_n3.py 20e7aa7aade8d2866708e1e343aed170b5b608b3b1c810632194f61fc9bcf10c
  - zweifeld_n4.py 497e1d0663719be916947d240687855a77b7d8aacee4a9c56ec1fdcfc1289953 (erste Fassung),
    6e220e917b103ba01ebbf603d757922097017e758b0d7b18c9dbeb9d4d7def95 (gewertete N4-Laeufe)
  - beutel_v2.py 6875e6e511283afb3812e23a28722826fe0c1e338f70c09b0474dab16a6a80ad (= RUNDE-16/beutel-1/code)
  - diag_profil.py 9ecf3f872aaf832ee618b1220cc05a2e876e16ce28eaa9a1f64560e06bafa65d,
    diag_profil2.py 09e56513a5969c6b93bbb8558e9c23cb2a69c39acd43ad1a7b11a1e80e0da9b4
- Plaene:
  - PLAN.md.eingefroren-20261002-115908 f50ba95f0d81e81b931164ec8c5f013b8b2e19cfd5944c886f2400afbb7a7fca
  - PLAN-NACHTRAG-1.md.eingefroren-20261002-120020 b8b4503f999ce2eac44b776cb2542f267deeab7f92746440c11bbf504c7f89c8
  - PLAN-NACHTRAG-2.md.eingefroren-20261002-120959 4713358d672177aab762846777ef7bdcb5bd6750b8dcc7e845b179c314d8e408
  - PLAN-NACHTRAG-3.md.eingefroren-20261002-121346 bfa3936df6dfde34e7318feb8a3cd3fcfc7dcbf1706de0f3319dbd11962c9adb
  - PLAN-NACHTRAG-4.md.eingefroren-20261002-121801 4e15d21c60995cc0858e075a99af7c200c73c65625349e4510fac7a832f5e120
- Ausgaben (aus/, Spiegel von /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau/aus/; Logs in aus/logs/):
  - prof-M1.json 0f9f2a3b4e1455cdd974ae944e19f90515ae2e8ccac49620b15b8165a96a81d7
  - prof-M2.json 6a4b1db500426a8ab99c2834cff0c26e2332a966c1beb97e63ea085afec78262
  - prof-M1.npz 24691531fff7f9d37e770c32faa1f7842d6ec0947b182aae7b52fc955eb1dac0
  - prof-M2.npz 86dc4e388e8cee6bcf76feaf0583678acdcc314d9c9d4013c2c9902555ef681b
  - kand-M1-st1.json d16fd4fcb24ff740cc07351b128cdca1c4a84d9811b63e8e22e44e07e624e383
  - kand-M1-st2.json 8b8bc9e4a9dfda6b31bf41e50f5b08efd6574a83e38b49889eac2e041f98daf8
  - n2-kand-M1-st1.json 34dc85c29dc2410f030d3f6d54ae483a85215503c27a06bf9409722c9810e5b8
  - n2-kand-M1-st2.json 965278d01b05ee963b205e1f37ea22f7a048a74fd59cf14c7af1cee63a777333
  - n3w2-kand-M1-st1.json 516a0a9f2ca46ae2037f2eca8347bddd2c5e1336fefca6748dcb13c978f62a0f
  - n3w2-kand-M1-st2.json 374adf03bc7fba3d670c85457ee9d2be03a6d8f3be8aa08b41073a0b2233f8d4
  - n3w2-kand-M2-st1.json cd6f9c22be15d59066cc77b4b94cf306aa65c64db8ade0fc9b9988b53cfa2bb3
  - n3w2-kand-M2-st2.json 8f0f86612ae7ebd8bcaa6807220093b4a8d724b490c83e5e02284b761ba5c8e1
  - n3w1-kand-M2-st1.json f0114969747d49ab5f3bf64e85e732e63c68122a1cdeeb1882c92ffb33def723
  - n3w1-kand-M2-st2.json fa7caf45c94698c01c16f0aef125fdb2b5accc27613f8866bf75b8e62606c2d0
  - n4-kurve-M2-st1a2.json e8f4087e249890529816271b2e2840c1d7637ddcbc62f1043107ebf22c62a423
  - n4-kurve-M2-st1b2.json 6e40a2b583abc6ccbf1aa845c0864230668a13c7fa5fe9d06e43c91a40a30d45
  - n4-kurve-M2-st2a2.json d0744a777c82c3395c780792982c240a71cccd6fbeaf13273b3e672a9fd5c56a
  - n4-kurve-M2-st2b2.json f345234effe5d62ce305b508ec0c6d43677be50eee31db0100ac4cde1216c579
  - n4-kurve-M2-st2c2.json fcfc0d6470c5519da0bcad7a1b699e68090638a16b70a45605abaf51a796803c
  - Zeilendateien je Ordner in Namensfolge verkettet: zeilen-M1-st1 e4b732bc...f278f6,
    zeilen-M1-st2 3d3d399a...9553ab, zeilen-M2-st1-b a6228e32...853d9b, zeilen-M2-st2-b 136bdae0...8b8d6c
    (aus/zeilen-M2-st1 und -st2 sind Kopien von -b fuer die alten Ketten).

## 6 Einfach gesagt

Ein Q-Ball mit Huelle kann schwingen. Meist strahlt er dabei Wellen ab. An "stillen Stellen" bleibt die Schwingung
eingesperrt. Mein eigenes Programm sollte solche Stellen im Zweifeldmodell blind finden. Zuerst habe ich einen
Messfehler eingebaut: Meine Kenngroesse dreht sich an einer stillen Stelle nicht einmal herum, deshalb fiel selbst die
bekannte Teststelle durch. Mit der richtigen Kenngroesse (der von LOG-NACHBAU) trifft das Programm die Teststelle
genau. Im Zweifeldmodell findet es dann 9 stille Stellen, alle bei Schwingungen des chi-Feldes und auf beiden
Rechengenauigkeiten an derselben Stelle. Ob diese nachtraegliche Korrektur zaehlt, entscheidet die Leitung.
