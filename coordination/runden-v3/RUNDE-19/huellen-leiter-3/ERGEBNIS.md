# ERGEBNIS HUELLEN-LEITER-3 (Runde 19)

- Code-Agent. Start 2026-10-02 16:09:59 CEST (date). Plan eingefroren 16:30:36 CEST
  (PLAN.md.eingefroren-20261002-163036), vor dem ersten .69-Lauf (py_compile 14:31:03 UTC, erster kleintest-Lauf
  14:31:30 UTC). Zwei Nachtraege, beide nach Laufbeginn und als nachtraeglich markiert:
  PLAN-NACHTRAG-1.md.eingefroren-20261002-163837 (Befund Knotenzahl, Diagnose D1) und
  PLAN-NACHTRAG-2.md.eingefroren-20261002-164557 (Diagnose D2, Umlauf an den k = 3-Stellen); beide aendern keine
  Wertung. Bericht ab 16:41 CEST. Uhrzeiten der .69 in UTC (CEST = UTC + 2).
- Code: code/huellen_leiter3.py (neu: Variante F, gedaempfter Newton, Befehle k0, test, ausw-k0, ausw-test; nach dem
  Einfrieren nicht geaendert), code/diag_knoten.py (D1) und code/diag_umlauf.py (D2), beide nach den Nachtraegen;
  code/huellen_leiter2.py, code/stille3.py, code/beutel.py unveraendert aus HUELLEN-LEITER-2.
- Explorativ (v3). Alles modellintern (Modell M2), keine Messdaten. Deutungen sind Hypothesen [H].

## 1 Ergebnis zuerst

1. **Alle 8 vorhergesagten Sprossen liegen dort, wo die Regel sie hinlegt.** Newton auf W ab der Vorhersage findet
   auf k = 0 bis 3 je eine stille Stelle mit |Delta R| <= 0,018 (groesste: k = 3, 41,93 -> 41,912). Beide Gitterstufen
   gleich auf <= 5,5e-10, Rangabfall sigma2/sigma1 <= 4,3e-10, Rechteck-Umlauf von W (F) aufgeloest +-1 (an den zwei
   k = 3-Stellen nur als Diagnose D2 gerechnet). Auch die kontaminierte Sprosse k = 1 / 40,51 liegt bei 40,506 auf
   k = 1 (rho 1,1870). Die in HUELLEN-LEITER-2 gesehene Stelle bei 40,49 (rho 1,2484) ist eine andere, auf einer
   hoeheren Kurve.
2. **Formal nach dem eingefrorenen Plan: P1' nicht eingetroffen, P2' eingetroffen. Bedeutung nach Plan-Lesart: "Die
   Regel gilt nur im bisherigen Bereich."** Dieser formale Ausgang haengt allein an den zwei k = 3-Sprossen. Sie
   scheitern an einer Bedingung, die ich in den Plan geschrieben habe: Die Knotenzahl der c-Komponente muss der der
   Runde 18 gleichen (2), unter der Variante S ist sie 3. Das ist ein Fehler meines Plans, kein Lagebefund. Die
   Knotenzahl haengt wie das Vorzeichen von s an der Saat. Unter S hat k = 3 schon bei R = 33,9 bis 38,95 die
   Knotenzahl 3 (Zeilen von HUELLEN-LEITER-2), mit F an beiden neuen k = 3-Stellen 2 (Diagnose D1, nachtraeglich).
   Ohne diese Bedingung waeren alle 7 unkontaminierten Sprossen Treffer innerhalb +-0,10. Die Wertung habe ich nicht
   geaendert; wie der Ausgang zu lesen ist, entscheidet die Leitung.
3. **K0' bestanden.** 12 bekannte Stellen (k = 0 bis 3, je die drei mit groesstem R), beide Stufen: Lage S gegen
   Kopplung der Runde 18 <= 9,5e-14, F gegen Runde 18 <= 8,9e-16 (17 von 24 bitgleich). Rechteck-Umlauf von W mit F an
   allen 24 aufgeloest und mit dem Vorzeichen der Runde 18. Formal ausgewertet um 16:36, vor der Sicht auf die
   Testlaeufe.
4. **P2' eingetroffen auf allen gewerteten Schritten:** k = 0: -1 (Nr 81) -> +1 -> -1; k = 2: +1 (Nr 85) -> -1 -> +1,
   beide Stufen. k = 3 hat formal keine angenommene Sprosse, also keinen Schritt; als Diagnose D2 (nachtraeglich)
   wechselt auch dort der F-Umlauf: -1 (Nr 83) -> +1 (39,77) -> -1 (41,93). Getrennt (kontaminiert) wechselt k = 1:
   -1 (Nr 88) -> +1 (40,51) -> -1 (42,62). Die gemessenen Abstaende setzen den langsamen Rueckgang der Runde 18
   fort (k = 1: 2,108 -> 2,108 -> 2,107; k = 2: 2,127 -> 2,124 -> 2,122; k = 3: 2,159 -> 2,153 -> 2,147; k = 0: 2,41).
5. **Kontrolle der Stabilisierung bestanden:** Die zweite Variante F (chi im Inneren durch die analytische Fortsetzung
   sinh(m0 r)/r ersetzt) bestaetigt die Lagen der S-Wurzeln an allen angenommenen Sprossen auf <= 2,6e-13 (gewertet:
   39,59 und 40,24). Mit F stimmen auch Umlaufzeichen und Knotenzahl mit Runde 18 ueberein; S dreht beide auf k = 3.
   **Inhaltlich [H, nicht gewertet]:** Lagen und Umlaeufe aller 8 Sprossen sehen so aus, wie die Karte es fuer "P1' und
   P2' eingetroffen" vorsieht (Leiter setzt sich ueber R = 39 hinaus regelmaessig fort). Formal gilt wegen der
   Knotenzahl-Bedingung meines Plans die zweite Aussage der Karte.

## 2 K0' im Detail

- **Lauf:** Befehl k0, je Stelle und Stufe drei gedaempfte Newton-Laeufe auf W vom selben Start (Lage der Runde 18
  dieser Stufe) und demselben Anker (naechste Zeile mit omega^2 <= Start): Kopplung der Runde 18 (alt), S, F. Danach
  Rechteck-Umlauf von W mit F um die F-Wurzel (Code 1, 16 Punkte je Kante, Verfeinerung bis Sprung < 0,4 rad,
  Halbbreite wie Runde 18: 2,4e-4 bis 3,4e-4). Formale Auswertung ausw-k0 auf der .69 um 14:35:53 UTC (16:35:53
  CEST); die Testlaeufe habe ich erst danach angesehen (16:36).
- **Profile:** Zeilen 0 bis 125 beider Stufen neu gerechnet; w2, Q, E, Rchi, chi0 und N in allen 126 Zeilen beider
  Stufen bitgleich mit profile-info der Runde 18 (Vergleichsdateien hilfs/prof-vergleich-*.json).
- **K0'a (Lage S gegen alt):** alt und S konvergiert in 2 Schritten an allen 24; max |d| = 9,5e-14.
- **F gegen alt (Kriterium, da F die Vorzeichen liefert):** konvergiert in 2 Schritten; max |d| = 8,9e-16, 17 von 24
  bitgleich.
- **K0'b (Umlauf):** F-Rechteck an allen 24 im ersten Versuch aufgeloest (groesster Sprung 0,347 bis 0,399 rad, 66
  bis 84 Randpunkte), Vorzeichen gleich Runde 18 an allen 24.
- **Berichtet (kein Kriterium):**
  - Abstand der Newton-Wurzel (alt) zur tabellierten Halbierungslage der Runde 18: bis 2,6e-8 (Nr 74, rho). Darum war
    die Newton-Wurzel der Bezug, nicht die Tabelle.
  - |W| an den Wurzeln bis 1,7e-10 (alt, F) bzw. 1,9e-10 (S); |W| > 1e-10 an 4 (alt), 1 (S), 4 (F) von 24 bekannten
    Stellen. sigma2/sigma1 (F) <= 1,8e-10.
  - S-Umlauf (Rechteck um die S-Wurzel, Information): an allen 24 aufgeloest; an Nr 74 und 83 (k = 3) auf beiden
    Stufen umgekehrt, sonst gleich Runde 18. Das war die Erwartung vorab (Plan 7) und der Grund, die Vorzeichen aus F
    zu nehmen.

| Nr | k | R | max abs(S - alt) St1 / St2 | max abs(F - alt) St1 / St2 | Umlauf R18 St1 / St2 | Umlauf F St1 / St2 | aufgeloest | groesster Sprung (rad) | Randpunkte | Umlauf S St1 / St2 | abs(W) St1 S / F | sigma2/sigma1 F St1 / St2 | K0' |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 62 | 0 | 32.37 | 8.7e-14 / 1.9e-14 | 6.7e-16 / 2.2e-16 | -1 / -1 | -1 / -1 | true / true | 0.362 / 0.362 | 84 / 84 | -1 / -1 | 5.5e-12 / 2.8e-11 | 2.8e-11 / 4.9e-12 | true |
| 72 | 0 | 34.77 | 3.3e-14 / 3.3e-14 | 8.9e-16 / 5.6e-16 | 1 / 1 | 1 / 1 | true / true | 0.399 / 0.399 | 82 / 82 | 1 / 1 | 6.6e-12 / 3.1e-11 | 3.1e-11 / 2.2e-11 | true |
| 81 | 0 | 37.18 | 6.1e-14 / 7e-14 | 3.3e-16 / 5.6e-16 | -1 / -1 | -1 / -1 | true / true | 0.386 / 0.386 | 84 / 84 | -1 / -1 | 6.5e-12 / 7.1e-12 | 7.1e-12 / 2.4e-11 | true |
| 69 | 1 | 34.18 | 1.2e-14 / 1.2e-14 | 0 / 0 | -1 / -1 | -1 / -1 | true / true | 0.385 / 0.385 | 71 / 71 | -1 / -1 | 5.4e-12 / 1.7e-10 | 1.8e-10 / 6.7e-11 | true |
| 78 | 1 | 36.29 | 9.5e-14 / 1.1e-14 | 1.1e-16 / 0 | 1 / 1 | 1 / 1 | true / true | 0.392 / 0.392 | 72 / 72 | 1 / 1 | 1.9e-10 / 4e-11 | 4.1e-11 / 1e-10 | true |
| 88 | 1 | 38.4 | 9.8e-15 / 9.8e-15 | 0 / 0 | -1 / -1 | -1 / -1 | true / true | 0.39 / 0.39 | 74 / 74 | -1 / -1 | 5e-11 / 6e-11 | 6.1e-11 / 1.1e-10 | true |
| 68 | 2 | 33.85 | 8.8e-15 / 8.8e-15 | 0 / 0 | 1 / 1 | 1 / 1 | true / true | 0.367 / 0.367 | 68 / 68 | 1 / 1 | 5.9e-12 / 1.8e-12 | 1.9e-12 / 1.3e-11 | true |
| 76 | 2 | 35.98 | 7.4e-14 / 7.1e-15 | 0 / 0 | -1 / -1 | -1 / -1 | true / true | 0.347 / 0.347 | 68 / 68 | -1 / -1 | 2.2e-11 / 1e-10 | 1.1e-10 / 8.6e-11 | true |
| 85 | 2 | 38.11 | 5e-15 / 5.1e-15 | 0 / 0 | 1 / 1 | 1 / 1 | true / true | 0.396 / 0.396 | 66 / 66 | 1 / 1 | 4.9e-11 / 5.3e-11 | 5.3e-11 / 4.2e-11 | true |
| 65 | 3 | 33.29 | 2.3e-15 / 2.2e-15 | 0 / 0 | -1 / -1 | -1 / -1 | true / true | 0.39 / 0.39 | 70 / 70 | -1 / -1 | 6.5e-12 / 5.6e-12 | 5.7e-12 / 4.1e-12 | true |
| 74 | 3 | 35.45 | 3.3e-16 / 3.3e-16 | 0 / 0 | 1 / 1 | 1 / 1 | true / true | 0.394 / 0.394 | 68 / 68 | -1 / -1 | 3.5e-12 / 3.4e-12 | 3.4e-12 / 6.6e-12 | true |
| 83 | 3 | 37.61 | 1.8e-15 / 1.6e-15 | 0 / 0 | -1 / -1 | -1 / -1 | true / true | 0.363 / 0.363 | 68 / 68 | 1 / 1 | 3.4e-11 / 3.3e-11 | 3.3e-11 / 2.2e-11 | true |

## 3 Sprossen: vorhergesagt gegen gefunden

- Je Sprosse und Stufe: Newton (S) ab omega^2 aus der Tabelle (Rchi, omega^2) der Stufe 1 beim vorhergesagten R und
  rho aus dem quadratischen Polynom in 1/R durch die letzten drei Stellen der Kurve aus Runde 18. Dann Konvergenz,
  Rangabfall, Kurvenrang und Knotenzahl in einer Zeilenrechnung bei omega^2 der Wurzel (zeile_k), Fenster +-0,5;
  bei Erfolg F-Newton ab der S-Wurzel (Kontrolle) und Rechteck-Umlauf von W mit F und S. Nachstarts (R +-0,25) nur
  bei Misserfolg.
- R gefunden = Rchi des Profils an der S-Wurzel, Stufe 1. Delta R = R gefunden - R vorhergesagt. omega^2 und rho: S-Wurzel
  Stufe 1. Stufenabstand = max(abs(d omega^2), abs(d rho)) zwischen den S-Wurzeln beider Stufen.

### Unkontaminierte Sprossen (P1')

| k | R vorhergesagt | R gefunden | Delta R | omega^2 | rho | Umlauf F St1 / St2 (aufgeloest) | Umlauf S St1 / St2 | Stufenabstand | Rang St1 / St2 | Knotenzahl S St1 / St2 | abs(W) St1 / St2 | sigma2/sigma1 St1 / St2 | Versuch | angenommen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 39.59 | 39.594 | 0.004 | 0.762960052 | 1.02592639 | 1 / 1 (true / true) | 1 / 1 | 2.9e-10 | 0 / 0 | 0 / 0 | 2.7e-12 / 2.8e-11 | 2.7e-12 / 2.8e-11 | 0 / 0 | true |
| 0 | 42.0 | 42.004 | 0.004 | 0.760937006 | 1.02492679 | -1 / -1 (true / true) | -1 / -1 | 2.9e-10 | 0 / 0 | 0 / 0 | 4.8e-12 / 1.6e-11 | 4.9e-12 / 1.6e-11 | 0 / 0 | true |
| 1 | 42.62 | 42.613 | -0.007 | 0.760461874 | 1.18587758 | -1 / -1 (true / true) | -1 / -1 | 2.4e-10 | 1 / 1 | 0 / 0 | 2.7e-10 / 4.2e-10 | 2.8e-10 / 4.2e-10 | 0 / 0 | true |
| 2 | 40.24 | 40.229 | -0.011 | 0.762402975 | 1.19528644 | -1 / -1 (true / true) | -1 / -1 | 3e-10 | 2 / 2 | 2 / 2 | 1.5e-11 / 6.3e-11 | 1.5e-11 / 6.4e-11 | 0 / 0 | true |
| 2 | 42.36 | 42.351 | -0.009 | 0.760664436 | 1.19330579 | 1 / 1 (true / true) | 1 / 1 | 2.8e-10 | 2 / 2 | 2 / 2 | 2.4e-11 / 9.2e-11 | 2.5e-11 / 9.5e-11 | 0 / 0 | true |
| 3 | 39.77 | 39.765 | - | 0.762808178 | 1.20932238 | - / - (- / -) | - / - | - | 3 / 3 | 3 / 3 | 8e-11 / 3.5e-11 | 8.1e-11 / 3.6e-11 | - / - | false |
| 3 | 41.93 | 41.912 | - | 0.761009416 | 1.20592276 | - / - (- / -) | - / - | - | 3 / 3 | 3 / 3 | 4.4e-11 / 2.4e-11 | 4.5e-11 / 2.4e-11 | - / - | false |

### Kontaminierte Sprosse (getrennt gewertet)

| k | R vorhergesagt | R gefunden | Delta R | omega^2 | rho | Umlauf F St1 / St2 (aufgeloest) | Umlauf S St1 / St2 | Stufenabstand | Rang St1 / St2 | Knotenzahl S St1 / St2 | abs(W) St1 / St2 | sigma2/sigma1 St1 / St2 | Versuch | angenommen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 40.51 | 40.506 | -0.004 | 0.762165623 | 1.18703811 | 1 / 1 (true / true) | 1 / 1 | 2.5e-10 | 1 / 1 | 0 / 0 | 3.2e-10 / 4.1e-11 | 3.3e-10 / 4.1e-11 | 0 / 0 | true |

- **Nicht angenommen: k = 3 / 39,77 und k = 3 / 41,93**, auf beiden Stufen nur wegen der Knotenzahl (S: 3, Plan
  verlangt 2). Alle uebrigen Bedingungen sind erfuellt (Konvergenz in 3 bis 4 Schritten, abs(W) <= 8,0e-11,
  sigma2/sigma1 <= 8,1e-11, Rang 3 mit Abstand <= 1,2e-13 zur Nullstelle der Zeile, Fenster). Die Nachstarts bei
  R +-0,25 enden an derselben Wurzel (auf <= 1e-10). Rechtecke und F-Kontrolle wurden fuer nicht angenommene Stellen
  nach Plan nicht gerechnet (als Diagnose D2 nachgeholt, Abschnitt 5). Formal gelten die beiden Sprossen als nicht
  gefunden. In der Tabelle stehen fuer sie die Werte des letzten Starts.
- Spalte "Versuch": 0 = Start bei R vorhergesagt. Alle 6 angenommenen Sprossen wurden vom ersten Start gefunden (Newton
  in 3 Schritten).
- Zeilenrechnung bei R ~ 42 (S): Knotenzahlen nach Rang 0, 0, 2, 3, 3, 4, 6, 7, 7, 8, 8 (11 Nullstellen); Runde 18
  bei R = 38,95: 0, 0, 2, 2, 4, 4, 4, 6, 6, 6.
- abs(W) > 1e-10 (woertliches Kriterium der Karte) nur bei k = 1: 40,51 Stufe 1 (3,2e-10) und 42,62 beide Stufen
  (2,7e-10, 4,2e-10); angenommen nach Plan 4 (<= 1e-9). Woertlich waere k = 1 / 42,62 nicht angenommen; P1' waere
  dann ebenso nicht eingetroffen.

## 4 P1' und P2'

| Nr | Vorhersage (Wahrsch.) | Ausgang (formal, Plan 6) | Zahlen |
|---|---|---|---|
| P1' | Die 7 unkontaminierten Sprossen liegen je innerhalb +-0,10 um den vorhergesagten R-Wert (60 %) | **nicht eingetroffen** | 5 von 7 angenommen, alle 5 mit abs(Delta R) <= 0,011. k = 3 / 39,77 und 41,93 formal nicht gefunden (Knotenzahl, Abschnitt 3); ihre Stellen auf Rang 3 liegen bei Delta R = -0,005 und -0,018. max abs(Delta R) aller 7 Lagen: 0,018 |
| P2' | Der Rechteck-Umlauf von W wechselt entlang jeder Kurve das Vorzeichen (85 %) | **eingetroffen** | 4 von 4 gewerteten Schritten, beide Stufen gleich: k = 0: Nr 81 (-1) -> 39,59 (+1) -> 42,00 (-1); k = 2: Nr 85 (+1) -> 40,24 (-1) -> 42,36 (+1). k = 3 ohne Schritt (keine angenommene Sprosse). Getrennt, kontaminiert: k = 1: Nr 88 (-1) -> 40,51 (+1) -> 42,62 (-1), beide Schritte erfuellt |

- **Bedeutung nach Karte und Plan-Lesart:** P1' nicht eingetroffen; nach der Plan-Lesart zaehlt eine nicht gefundene
  Sprosse als "Abweichung > 0,3", also formal "Die Regel gilt nur im bisherigen Bereich." Der Ausgang entsteht nur
  durch die Knotenzahl-Bedingung. Bei allen 8 Sprossen liegt die gefundene Lage innerhalb 0,018 der Vorhersage.
- Kontaminierte Sprosse k = 1 / 40,51: angenommen, Delta R = -0,004, Umlauf +1 (beide Stufen), wechselt gegen Nr 88
  und gegen 42,62.

## 5 Kontrolle der zweiten Stabilisierung

- Variante F: chi wird an allen Punkten bis zum letzten mit chi < 1e-12 durch chi(r_a) sinh(m0 r)/r /
  (sinh(m0 r_a)/r_a) ersetzt (r_a = erster aufgeloester Punkt, m0^2 = 2 S(0) - 1). Bitweise geaendert ist nur M_ac
  (Zaehler in den Ausgaben).
- **Gewertet (Plan 5): 39,59 (k = 0) und 40,24 (k = 2)**, die zwei angenommenen unkontaminierten Sprossen mit kleinstem
  R vorhergesagt: F-Newton ab der S-Wurzel konvergiert, abs(d omega^2), abs(d rho) <= 4,6e-14 (39,59) und <= 3,0e-14
  (40,24), beide Stufen. **Bestanden.**
- Alle angenommenen Sprossen: <= 2,6e-13 (k = 1 / 42,62). Umlauf F = Umlauf S an allen 6 angenommenen Sprossen
  (k = 0, 1, 2).
- K0' zeigt dasselbe an den bekannten Stellen: F gegen alt <= 8,9e-16, S gegen alt <= 9,5e-14.
- **Diagnose D1 (nachtraeglich, Nachtrag 1, keine Wertung):** Rang und Knotenzahl an den S-Wurzeln der Stufe 1 mit
  F und mit der Kopplung der Runde 18:

| k | R vorhergesagt | S: Rang / Knoten | F: Rang / Knoten | alt: Rang / Knoten | Knoten je Rang, S | Knoten je Rang, F | Knoten je Rang, alt |
|---|---|---|---|---|---|---|---|
| 0 | 39,59 | 0 / 0 | 0 / 0 | 0 / 0 | 0,0,2,3,3,4,6,7,7,7,8 | 0,0,2,2,4,4,4,6,6,6,8 | 0,0,2,2,4,4,4,6,6,6,8 |
| 3 | 39,77 | 3 / 3 | 3 / 2 | 3 / 3 | 0,0,2,3,3,4,6,7,7,7,8 | 0,0,2,2,4,4,4,6,6,6,8 | 1,1,1,3,3,3,5,5,7,7,7 |
| 2 | 40,24 | 2 / 2 | 2 / 2 | 2 / 1 | 0,0,2,3,3,4,6,7,7,7,8 | 0,0,2,2,4,4,4,6,6,6,8 | 1,1,1,3,3,3,5,5,5,7,7 |
| 1 | 40,51 | 1 / 0 | 1 / 0 | 1 / 0 | 0,0,2,3,3,4,6,7,7,7,8 | 0,0,2,2,4,4,4,6,6,6,8 | 0,0,2,2,4,4,4,6,6,8,8 |
| 3 | 41,93 | 3 / 3 | 3 / 2 | 3 / 2 | 0,0,2,3,3,4,6,7,7,8,8 | 0,0,2,2,4,4,4,6,6,6,8 | 0,0,2,2,4,4,5,5,7,7,9 |
| 0 | 42,00 | 0 / 0 | 0 / 0 | 0 / 1 | 0,0,2,3,3,4,6,7,7,8,8 | 0,0,2,2,4,4,4,6,6,6,8 | 1,1,1,3,3,3,5,5,5,7,7 |
| 2 | 42,36 | 2 / 2 | 2 / 2 | 2 / 2 | 0,0,2,3,3,4,6,7,7,8,8 | 0,0,2,2,4,4,4,6,6,6,8 | 0,0,2,2,4,4,4,5,7,7,7 |
| 1 | 42,62 | 1 / 0 | 1 / 0 | 1 / 1 | 0,0,2,3,3,4,6,7,7,8,8 | 0,0,2,2,4,4,4,6,6,6,8 | 1,1,1,3,3,3,5,5,5,7,7 |

- Mit F ist das Knotenmuster an allen 8 Stellen das der Runde 18 (0,0,2,2,4,4,4,6,6,6, dazu 8 fuer die elfte Kurve),
  fest von R = 39,6 bis 42,6. Der Rang (die Kurve) ist in allen drei Varianten gleich.

- Stufe 2 (nur F): an allen 8 Stellen derselbe Rang und dieselbe F-Knotenzahl wie auf Stufe 1 (k = 3: 2).
- **Diagnose D2 (nachtraeglich, PLAN-NACHTRAG-2, keine Wertung):** An den zwei k = 3-Stellen F-Newton ab der S-Wurzel
  (Abstand <= 8,2e-14) und Rechteck-Umlauf von W mit F: 39,77 -> +1 (beide Stufen, aufgeloest, Sprung 0,394 rad,
  68 Randpunkte), 41,93 -> -1 (beide Stufen, 0,352 rad, 70 Randpunkte). Mit Nr 83 (-1) wechselt der Umlauf also auch
  auf k = 3 von Sprosse zu Sprosse.
- Lesart [H]: Mit F hat k = 3 die Knotenzahl 2 wie in Runde 18 (bis R = 39), mit S 3. Die Kopplung der Runde 18 selbst
  ist ab R ~ 40 rundungsbestimmt (Runde 18, Nachtrag 4) und liefert dort wechselnde Knotenzahlen. Die Knotenzahl ist
  also so konventionsabhaengig wie das Vorzeichen von s; als Kurvenmerkmal taugt sie nur innerhalb einer festen
  Variante.

## 6 Grenzen, Selbstanzeigen, Laufzeiten, sha256

### Grenzen

- **Formaler Ausgang und Planfehler:** P1' scheitert nur an der Knotenzahl-Bedingung, die ich in Plan 4 als Pflicht
  geschrieben habe ("Kurve k wie im Vorlaeufer"). Sie vergleicht eine Knotenzahl unter S mit einer der Kopplung der
  Runde 18. Die Zeilen von HUELLEN-LEITER-2 (erlaubt, vorab nicht geprueft) zeigen, dass S auf k = 3 schon im
  K0-Bereich 3 statt 2 Knoten gibt. Die Wertung ist trotzdem unveraendert nach dem eingefrorenen Plan.
- **Rollen der Varianten (Plan-Abweichung, vorab begruendet):** Lagen aus S, Umlaufzeichen aus F. An allen 6
  angenommenen Sprossen ist der Umlauf in S und F gleich; an den K0'-Stellen siehe Spalte "Umlauf S".
- **Konvergenz (Plan-Abweichung, vorab begruendet):** Newton-Schritt < 1e-10 und abs(W) <= 1e-9. Der Rauschboden von
  abs(W) an bekannten Stellen liegt bei bis 1,9e-10 (K0'). Woertlich (abs(W) < 1e-10) waere k = 1 / 42,62 nicht
  angenommen (2,7e-10 / 4,2e-10) und die kontaminierte Sprosse 40,51 auf Stufe 1 nicht (3,2e-10).
- **Kurvenindex:** Rang der Nullstelle von m_bc in der Zeile bei omega^2 der Wurzel; in allen Varianten gleich (D1).
  Die Zeilen bei R ~ 42 haben 11 Nullstellen, k = 1 und 2 liegen 0,0072 auseinander (Gitter plus q-Punkte loesen das
  auf, Abstand Wurzel zu Zeilennullstelle <= 1,2e-13).
- **Nicht geprueft:** die dritte Sprosse je Kurve (44,09 bis 44,72), neue Kurven (P3 der Vorgaengerkarte), und ob
  zwischen der letzten Stelle der Runde 18 und der ersten Vorhersage weitere Stellen liegen. P2' setzt voraus, dass die
  gefundenen Stellen direkt aufeinander folgen.
- **Variante F:** Das befuerchtete Genauigkeitsproblem (Saat aus der Mitte waechst bei R ~ 42 auf ~1e12) zeigt sich
  nicht: F und S stimmen an den neuen Stellen auf <= 2,6e-13 ueberein, F und Runde 18 an den K0'-Stellen auf 8,9e-16.
- Reichweite: l = 0, linear, klassisch, Modell M2, keine Messdaten.

### Selbstanzeigen

- **Plan:** Die Knotenzahl-Bedingung (Abschnitt 3) war ein Fehler, den ich mit den erlaubten Daten von
  HUELLEN-LEITER-2 vorab haette sehen koennen. Nachtrag 1 und 2 (nach dem Befund bzw. nach der formalen
  Testauswertung, eingefroren) aendern keine Wertung und fuegen nur die Diagnosen D1 und D2 hinzu (neuer Code
  code/diag_knoten.py, code/diag_umlauf.py; huellen_leiter3.py unveraendert).
- **Plan-Abweichungen vorab (begruendet im Plan):** Rollen der Varianten (Lagen S, Umlaufzeichen F), Konvergenz
  abs(W) <= 1e-9 statt 1e-10, Zusatz sigma2/sigma1 <= 1e-6, Nachstarts. Keine davon hat den formalen Ausgang
  entschieden; woertlich 1e-10 haette P1' ebenfalls scheitern lassen (k = 1 / 42,62).
- **Reihenfolge der Sicht:** Die K0'-Logzeilen habe ich waehrend der Laeufe gesehen (Monitor), die formale
  K0'-Auswertung lief um 16:35:53, ich habe sie um 16:36 gelesen. Die Testlaeufe habe ich erst danach angesehen. Die
  Testauswertung (ausw-test) lief nach Nachtrag 1 mit unveraendertem Code. Die Laeufe fuer K0', Test und Auswertung
  liefen parallel; die Testlaeufe begannen also vor der K0'-Auswertung (so im Plan vorgesehen).
- **Zeitstempel:** In PLAN-NACHTRAG-2 steht "Geschrieben ab 16:46 CEST"; das war geschaetzt, nicht gemessen, und liegt
  nach dem gemessenen Einfrieren (16:45:57). Richtig ist: geschrieben kurz vor 16:45:57, Beginn nicht gemessen. Der
  "Bericht ab 16:41" im Kopf ist ebenfalls aus dem Gedaechtnis (ERGEBNIS.md angelegt nach date 16:41:32).
- **Prozessliste:** einmal ps meiner Prozesse auf der .69, gefiltert auf meinen Ordnernamen (Zaehlung).
- **Lokale Werkzeuge ausserhalb der Liste:** chmod (Einfrieren, von den Regeln verlangt), comm und eine
  while-/sleep-Schleife im Monitor-Befehl, until-/sleep-Schleifen in zwei Hintergrund-Warte-Befehlen, basename in
  hilfs/laufzeiten.sh. Ein Befehl mit vorangestelltem sleep 50 wurde vom Werkzeug abgelehnt und lief nicht. Kein
  lokales python, awk oder bc.
- **Auf der .69:** mkdir meines Ordners, dreimal py_compile mit rm -rf code/__pycache__ in meinem Ordner, nohup/setsid
  fuer die Ketten, drei Warte-Skripte (until-/sleep-Schleifen) und drei Diagnose-Aufrufe, einmal cat von kleintest.sh
  (Aufrufform; nicht in der Leseliste). Keine Prozesse beendet, keine fremden Ordner gelistet, nichts ausserhalb
  meines Ordners angelegt.
- **Lesen:** Karte; HUELLEN-LEITER-2: KARTE, ERGEBNIS, PLAN, PLAN-NACHTRAG-1, code/, aus/k0, aus/laeufe
  z-st1-0095/0100/0105/0108/0110 und z-st2-0110 (Knotenzahlen, nach dem Befund); Runde 18: ERGEBNIS,
  aus/laeufe/stellen.json, umlauf-P-st*.json, umlauf-punkte-P-st1.json, z-st1-0100/0105/0110, z-st2-0110,
  aus/logs/prof-st1.log, aus/prof-st*/profile-info.json (Hintergrund bis Zeile 125, fuer den Bitvergleich). Keine
  Zeilen oder Paare der Runde 18 jenseits Zeile 110, kein hilfs/ und logs/ von HUELLEN-LEITER-2, nichts aus
  Sperrbereichen.
- Nichts in den Scratchpad geschrieben (die Ausgaben der Hintergrund-Befehle legt das Werkzeug selbst unter
  /tmp/claude-1000/.../tasks ab). Kein git, kein Peerbus, keine Unteragenten, keine Literatur.

### Laufzeiten (.69, kleintest.sh, Service runtime; UTC)

| Lauf | Spur | Start | Ende | Dauer | rc | Teil |
|---|---|---|---|---|---|---|
| prof-st1 / prof-st2 | cpu / cpu2 | 14:31:30 | 14:31:35 / 14:31:38 | 4,6 s / 8,2 s | 0 | Profile |
| k0-st1-a | cpu | 14:31:47 | 14:35:40 | 233 s | 0 | K0' |
| k0-st2-a / k0-st2-b | cpu2 / cpu3 | 14:31:47 | 14:35:51 / 14:35:18 | 244 s / 211 s | 0 | K0' |
| ausw-k0 | cpu4 | 14:35:53 | 14:35:54 | 0,6 s | 0 | K0' formal |
| test-st1-b | cpu4 | 14:31:47 | 14:34:55 | 188 s | 0 | Test |
| test-st1-a | cpu | 14:35:40 | 14:38:24 | 164 s | 0 | Test |
| test-st2-b / test-st2-d | cpu3 | 14:35:18 / 14:37:15 | 14:37:15 / 14:39:34 | 116 s / 140 s | 0 | Test |
| test-st2-a / test-st2-c | cpu2 | 14:35:51 / 14:39:25 | 14:39:25 / 14:43:25 | 213 s / 240 s | 0 | Test |
| ausw-test | cpu4 | 14:43:30 | 14:43:30 | 0,5 s | 0 | Test formal |
| k0s-st1-a / k0s-st2-b / k0s-st2-a | cpu / cpu3 / cpu2 | 14:38:24 / 14:39:34 / 14:43:25 | 14:41:16 / 14:42:36 / 14:45:58 | 172 s / 182 s / 152 s | 0 | S-Rechtecke K0' (Information) |
| ausw-k0-mitS | cpu2 | 14:46:09 | 14:46:09 | 0,6 s | 0 | K0'-Tabelle mit S-Umlauf (Information) |
| diag-st1 / diag-st2 | cpu4 / cpu3 | 14:38:47 / 14:43:29 | 14:42:12 / 14:46:55 | 205 s / 207 s | 0 | Diagnose D1 |
| diag2-st1 / diag2-st2 | cpu / cpu4 | 14:45:57 | 14:46:14 / 14:46:30 | 17 s / 32 s | 0 | Diagnose D2 |

- Zusammen ~46 min Spurzeit (2730 s), 15,5 min Wandzeit (14:31:30 bis 14:46:55) auf vier Spuren. Kein Lauf an der
  600-s-Grenze.

### sha256

Code (lokal = .69, verglichen):

```
f67e137580aab1fe48a56b965c7d432d186039e2c9bd8b301e7ff870af572738  code/huellen_leiter3.py
2755359c497aca04eeeca48f851e83a62a6671aa121713cc709ca5c77076c57e  code/huellen_leiter2.py
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py
f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py
07dc5110b61f7a4bfc906beb9f74314c3a503642ba80f8ceb844959b0607acc6  code/diag_knoten.py (Nachtrag 1)
35c512d6b3ecca6fc67effd45dbd4f644c76e5630d68a4235655cb52835fc931  code/diag_umlauf.py (Nachtrag 2)
```

Plaene:

```
66665693e51eb190d50fa6eb4bd6c0ef9fec5a5875f5c0dbc1bf54184fe2c98a  PLAN.md.eingefroren-20261002-163036
f265f0aa2b5304ca029387b48a3fe4132436a331e8ba8ba77cb7adcbbefa0ab1  PLAN-NACHTRAG-1.md.eingefroren-20261002-163837
82a28de4705093da685b5801441569103a7af2a85dd39cba20fa0722cdc347c4  PLAN-NACHTRAG-2.md.eingefroren-20261002-164557
```

Ausgaben (lokal = Spiegel von /home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3/aus/ ohne *.npz):

```
5464722345076283b025726ba7c8f4c0031ec3591a34fff1dca88838c6b2c091  aus/k0-auswertung.json (formal, = .69)
c1ece3ee720c8d02c9b3c2b4a7caf89eb1bbfeec8c0b52ff58d84ce45665b55e  aus/test-auswertung.json (formal, = .69)
2f9bae69edd0f2e280c6f9b7284148125dcb927683af9799bc7f67357082fd2d  aus/k0-auswertung-mit-S.json
200fd2a9d50e3371e3f1599ba298408313bbd4df812bff9d2f62f4e301319d05  aus/k0/k0-st1-a.json
7cd558e0a1cef0298ddabe20369e9d4e470c82c6321fe6434b112c308692f25e  aus/k0/k0-st2-a.json
91c14d38547416d225cbfb9bf09838cb26522804d4aafca710ae377777c0747c  aus/k0/k0-st2-b.json
957efd2daf6295fda1d7c3fdc28bb0a05ee95b6f8d2f7e0b63a1c30c760955a9  aus/k0/k0s-st1-a.json
889ae06bbcdafa064a1abf22628d96644d14314d69b9c25d808bf556d5622e05  aus/k0/k0s-st2-a.json
7527e50357ef64020bd729af3589e9f5899568e81eca816f7d0aed9fa6d6c6fb  aus/k0/k0s-st2-b.json
28cbd15941385001b96a751fdd9c2be39817826a1fddc59ce12c1307a2286291  aus/test/test-st1-a.json
994cfa70fcdd1f880fd616b8f59edbfcace371da232e88bf74b2dd93591f4e1e  aus/test/test-st1-b.json
51f97312f909afdba18b56defbb30ad581e2716368b87e16a591a243a7ea3a4d  aus/test/test-st2-a.json
458568909e4305ce5aca2051bfd91729bda1a6f435781959b7b4650058036b7b  aus/test/test-st2-b.json
3d44100ce67d4bc08e4d95011731a25f42c138a89377aa978958dbc7b5c6141e  aus/test/test-st2-c.json
56e99d7c88765f274f7b90892dba45e92af9ea208525c00fb3371e959b5915b1  aus/test/test-st2-d.json
9a4f107ee36e452b67db309e81e466d4794d61fe1f8e9dbf0496d46851d1657c  aus/diag/knoten-st1.json
1880f88730360bb227fb09a2e9216465109bd3bbac0775b74afbed6035000f70  aus/diag/knoten-st2.json
084caebbb6ea2502b628cd7b8a30c74b6be6ee7b697c3e87cfd533f6dcc4014a  aus/diag/umlauf-k3-st1.json
01c4d71eeb93c2e2d847dadc4d0fd7b06401fa652a6464be9578e66b1d84a67b  aus/diag/umlauf-k3-st2.json
22100f29efc6b5e20a6f6d04dd3a04825695fd857d370433e89235b90f1fcd46  aus/prof-st1/profile-info.json
c70be1e757421d8220f8f738e8831dce3ae62c19b4b9bf8aa3b10e9d81cc5413  aus/prof-st2/profile-info.json
```

Referenzen (Kopien aus Runde 18) und Hilfsdateien:

```
5ce185ec655577131d6eca73cb4e8006aab6294ca4ad91840360caaf0a6ab202  ref/stellen-r18.json
586c36891558f3ac36d20fbab1c672719f3707cd4dcd954df8bf63d0e5fbc748  ref/zeilen-r18.json
e89b3895ee64e3d527c6c8751a0d5e948d6398dcabaf001e1a524157a730e3a1  hilfs/zeilen-126.json
5161008c6aee4eac0b744dddb0de3a5949afb4256ae02a1a2c84f69d60006410  hilfs/v1-profile.sh
fc400344476f92d78a47853bdd967dd42013c8a6363784c50eb9224db1014e20  hilfs/ketten.sh
dc6ccf1537a69f6b987e2ac6ace9b557eebef7550cd9f3f362c688898d70ecd2  hilfs/v4-k0.sh
044476526a2067c770933999c76f7df5cce43c72a5555882a07a5dc6155ebf9e  hilfs/v4-test.sh
0648d5c114f3fbe90ec392dc45ceb3f076549237a41b845d65f72857cb0d9396  hilfs/diag-st2.sh
45580017440845ec6ed25b0273eaca9662a8418dac35e92e54f7542ca2353d26  hilfs/laufzeiten.sh
17b747c5adef584b54307c1328d8f325bd38d8028be57c0c0a6084129526b863  hilfs/k0tab.jq
4837172d1abb48062ca81589f2bb973e8eccb55bf6311e0d831e1d3cf9b1a899  hilfs/testtab.jq
```

- Profile (*.npz) nur auf der .69. Logs lokal unter logs/ (Spiegel).

## 7 Einfach gesagt

Aus 88 bekannten stillen Stellen eines grossen Q-Balls hatten wir eine Regel abgelesen: Auf jeder Kurve folgen die
Stellen in fast festem Abstand aufeinander, wie Sprossen einer Leiter. Damit haben wir vorab acht neue Stellen jenseits
des bisher gerechneten Bereichs vorhergesagt und dann gezielt an genau diesen Orten gesucht. Alle acht sind da, jede
weniger als 0,02 Laengeneinheiten neben der Vorhersage, auf zwei Rechengittern gleich, und der Drehsinn wechselt
weiter von Sprosse zu Sprosse. Nach den vorher festgelegten Regeln zaehlen zwei davon trotzdem nicht, weil ein
Zusatzmerkmal nicht passte, die Zahl der Nulldurchgaenge einer Feldkomponente. Dieses Merkmal haengt, wie sich zeigte,
von einer Rechenkonvention ab, und es als Pflicht in den Plan zu schreiben war mein Fehler. Formal ist die Vorhersage
deshalb nicht bestanden; in der Sache liegen alle neuen Stellen dort, wo die Regel sie erwartet.
