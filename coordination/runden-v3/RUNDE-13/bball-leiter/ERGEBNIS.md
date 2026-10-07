# B-BALL-LEITER (Runde 13): Ergebnis

- Code-Agent, Auftrag der Leitung claude-primary. Start 2026-10-01 19:09:03 CEST (date). Diese Datei begonnen
  2026-10-01 19:33:29 CEST (date); Ende: letzte Zeile.
- Grundlagen:
  - KARTE.md (bindend)
  - RUNDE-12/x-baelle/X-BAELLE.md (T3)
  - RUNDE-12/afm-kanal2/ (PLAN, ERGEBNIS, afm_bic.py)
  - RUNDE-12/afm-kanal1/ (HERLEITUNG, ERGEBNIS, afm_kanal.py)
  - RUNDE-10/nls-leiter/ (ERGEBNIS, nls2.py)
- Eigene Dateien:
  - PLAN.md, eingefroren 19:23:22 als PLAN.md.eingefroren-20261001-192322
  - Nachtrag 1 eingefroren 19:28:02 als PLAN.md.nachtrag-eingefroren-20261001-192802
  - bball.py (ein Stand fuer alle Laeufe), start.sh, tabellen.jq
  - quellen/ (Abfrage, PDF, Text, SHA256SUMS.txt)
  - lauf-lokal/ (Rauchtests, ungueltig fuer die Regel), lauf-69/ (alle .69-Ausgaben und Logs)
- Markierungen: [A] an der Quelle gelesen, [L?] aus dem Gedaechtnis, [H] Hypothese/Deutung, [ES] eigener Schluss.
  Modell ist keine Messung. "In den Baendern" heisst: radial l = 0, volle Kopplung, 3 Baender x 11 Zeilen, je zwei
  Zwischenreihen pro Streifen, zwei Gitterstufen.

## 1 Ergebnis zuerst

1. **Ausgang nach der bindenden Regel: "Nicht gesehen".** In keinem der drei Baender der Karte wechselt s das
   Vorzeichen, auf keiner Stufe. Alle 60 Streifen (3 Baender x 10 x 2 Stufen) sind aufgeloest und haben Umlauf 0;
   der groesste Sprung ist 0,366 rad. K1 und K2 sind bestanden (Auswertung bball.py auswertung, .69 17:27:58 UTC).
2. **Kontrollen:**
   - K1 (Sextik, gleicher Code): h = 0,02 ergibt omega*^2 = 0,79767677, rho* = 1,74461754; h = 0,01 ergibt
     0,79767679 / 1,74461754. Die Abweichung vom Ziel ist <= 5e-7. Das Rechteck hat Umlauf -1 und ist aufgeloest
     (0,359 rad).
   - K2: Q und E des Log-Balls stimmen auf beiden Gittern auf <= 6,2e-11 relativ ueberein (33 Zeilen).
3. **Schritt 0 und Bild in den Baendern:**
   - In allen drei Baendern liegt der nackte geschlossene Zustand im Kontinuum; der Test ist also eine offene Frage.
   - Gekoppelt wird aus jedem nackten Zustand eine schmale Resonanz, d. h. eine Nullstelle von L(y_b) dicht am
     nackten Ort.
   - s behaelt auf jedem Ast sein Vorzeichen; die Polbreiten liegen bei 1e-5 bis 2e-3.
   - Der obere Ast (k = 0) wird zum dicken Ende hin stetig schwaecher gekoppelt: s/median von +1,4e-2 (0,70) auf
     +4,0e-3 (0,80).
4. **Nachtrag (nachtraeglich, aendert den Ausgang nicht; ob er gilt, entscheidet die Leitung):**
   - Derselbe Ast, weiter verfolgt bis omega^2 = 0,95, wechselt zwischen 0,9233 und 0,9267 das Vorzeichen.
   - Lokalisiert auf beiden Stufen bei omega*^2 = 0,925610, rho* = 1,837996 (Stufen auf 1,2e-7 gleich).
   - Das kleine Rechteck hat auf beiden Stufen Umlauf -1 und ist aufgeloest (0,398 rad); der Streifen 0,92 .. 0,93
     ebenfalls Umlauf -1.
   - Die Polbreite hat dort ein Minimum (2,9e-10 bei 0,93 gegen 1,0e-5 bei 0,80).
   - Das erfuellt das Kriterium "Gesehen", aber ausserhalb der Baender der Karte.
5. [H] Lesart: Die erste stille Stelle (n = 1) ist nicht an das Sextik-Potential gebunden. Im Log-Potential sitzt
   sie in einem noch dickeren Ball (omega^2 ~ 0,926 statt 0,798) und naeher an 2m (rho ~ 1,84 statt 1,74). Die
   Baender der Karte (bis 0,80) lagen darunter. Eine zweite Stelle (eine Leiter) ist in den Baendern nicht da.

## 2 Potential und Quelle

- arXiv-API-Abfrage (search_query=au:Kasuya AND au:Kawasaki AND ti:Q-ball AND ti:formation), 19:12:25 CEST,
  quellen/arxiv-abfrage-1.xml. Die Nummer hep-ph/9909509 stammt aus dieser Antwort; keine Nummer geraten.
- **[A] Kasuya S., Kawasaki M., "Q-ball Formation through Affleck-Dine Mechanism", arXiv:hep-ph/9909509v3**
  (PRD 61, 041301 [L?, nur Journalangabe]). PDF und Text in quellen/.
  - **Gl. (1), PDF-Seite 2:** V(Phi) = m^4 ln(1 + |Phi|^2/m^2) - c H^2 |Phi|^2 + (lambda^2/M^2) |Phi|^6, "where m is
    the mass of the field".
  - Dazu woertlich: "This form of the potential arises naturally in the gauge-mediated SUSY breaking scenario in
    MSSM [8]". [8] ist Kusenko/Shaposhnikov PLB 418, 46; nicht gelesen.
  - Gl. (8), **PDF-Seite 3** (im eingefrorenen PLAN steht faelschlich Seite 2, Selbstanzeige 8): V1 ~ m^4 log(1 +
    phi^2/(2 m^2)) mit Phi = phi e^{i theta}/sqrt(2). Also ist Phi kanonisch komplex [ES].
- Fuer den Q-Ball: H -> 0, und den Planck-unterdrueckten |Phi|^6-Term lasse ich weg. Dimensionslos mit Phi = m phi,
  x = x'/m, t = t'/m ergibt sich **U(S) = ln(1 + S)**, U'(0) = 1. Das ist genau die Kartenform; eine Umrechnung war
  nicht noetig.
- Linearisierung (PLAN Abschnitt 3): dp = U' + S U'' = 1/(1 + S)^2, sp = S U'' = -S/(1 + S)^2, A = dp - omega^2,
  B = 2 omega, C = sp. Fuer das Sextik-Modell gibt dieselbe Formel ziffergleich den KG-Zweig von afm_bic.

## 3 Schritt 0 (nackter geschlossener Kanal, C = 0)

- -y'' + dp(r) y = E y mit E = (rho - omega)^2 und Dirichlet bei 0 und R_max = max(3 R_w, R_w + 40); Gegenprobe
  mit R_max + 20. Eingebettet heisst 1 - omega < rho < 1 + omega.
- Kontrolle im selben Code (Rauchtest lokal, rauch-s0-kg): Sextik bei omega^2 = 0,7977 ergibt E = 0,706247,
  rho+ = 1,733525 (R10 und AFM-KANAL-1 K2 gleich).
- Ergebnis (.69, 33 Zeilen; h = 0,02 gegen 0,01: |dE| <= 2,4e-6, |drho| <= 1,3e-6, gleiche Zustandszahl):

| Band | Zustand | rho+ (omega^2 unten .. oben) | E | eingebettet |
|---|---|---|---|---|
| b1 0,30 .. 0,40 | k = 0 | 1,0133 .. 1,1676 | 0,2167 .. 0,2864 | ja, alle Zeilen |
| b1 | k = 1 | 1,4178 .. 1,5878 | 0,7570 .. 0,9126 | ja, alle Zeilen |
| b2 0,50 .. 0,60 | k = 0 | 1,3049 .. 1,4312 | 0,3573 .. 0,4311 | ja, alle Zeilen |
| b2 | k = 1 | 1,7044 / 1,7130 / 1,7211 (nur 0,50 / 0,51 / 0,52) | 0,9946 / 0,9977 / 0,99999 | ja; schwellennah, kastenabhaengig (\|dE\| bis 4,8e-4) |
| b3 0,70 .. 0,80 | k = 0 | 1,5511 .. 1,6698 | 0,5104 .. 0,6012 | ja, alle Zeilen |
| b3 | k = 0, unterer Partner rho- | 0,1205 .. 0,1191 (0,78 .. 0,80) | wie oben | ja, nur 0,78 bis 0,80 |

- Die Zustaende sitzen im Ball: r_spitze 2,2 bis 5,5 bei R_w = 2,7 bis 3,7, Beteiligungslaenge P = 3,8 bis 7,2.
  Ausnahme sind die schwellennahen Zustaende k = 1 in b2 (0,50 bis 0,52): r_spitze 5,7 bis 6,2, P = 16,6 bis 24,4.
  Im eingefrorenen PLAN fehlt diese Ausnahme (Selbstanzeige 8).
- **Folge (vor dem Einfrieren festgehalten):** Der Test ist keine Mechanismus-Bestaetigung. "Nicht gesehen" war
  nicht vorhersagbar. Schritt 0 nennt keinen besseren Bereich; die Baender blieben wie in der Karte.
- Gekoppelt (Abschnitt 5) findet sich jeder dieser nackten Zustaende (rho+) als Nullstelle von L(y_b) wieder, um
  +0,0006 bis +0,0065 nach oben verschoben (b1 +0,0024 .. +0,0065, b2 +0,0006 .. +0,0061, b3 +0,0049 .. +0,0054;
  per jq gegen die naechste nackte Lage). Beispiel b3, omega^2 = 0,80: nackt 1,6698, gekoppelt 1,6747.
- Der schwellennahe Zustand k = 1 in b2 erscheint nur bei 0,50 (1,7050) und verlaesst das Fenster vor 0,5033.

## 4 Kontrollen

| Kontrolle | Kriterium (Karte) | h = 0,02 | h = 0,01 | Ergebnis |
|---|---|---|---|---|
| K1 Sextik, gleicher Code | Stelle 0,797677 / 1,744618 auf 1e-4, Umlauf +-1 auf beiden Stufen | 0,79767677 / 1,74461754; Klammer 5,9e-15 (5 Schritte); Rechteck 0,79728 .. 0,79808 x 1,74262 .. 1,74662: Umlauf -1 (Kreuzung -1), 0,359 rad | 0,79767679 / 1,74461754; Klammer 1,7e-15; Umlauf -1 (Kreuzung -1), 0,359 rad | **bestanden** |
| K2 Log-Ball | Q(omega), E(omega) auf zwei Gittern auf 1e-4 gleich | Profilschritt 0,01 | Profilschritt 0,005 | **bestanden**: alle 33 Zeilen, groesstes \|dQ\|/Q = 6,2e-11, \|dE\|/E = 5,5e-11; Virialrest < 1e-12 |

- K1, Familie 0,785 .. 0,815 (7 Zeilen):
  - je eine Nullstelle von L(y_b), s/median +4,1e-3 .. -7,0e-3
  - genau ein s-Wechsel (0,79667 -> 0,79833)
  - Streifen 0,795 .. 0,80 mit Umlauf -1, die anderen 5 mit 0, alle aufgeloest
  - Polbreiten 1,99e-4, 6,96e-5, 7,99e-6, 5,65e-6, 5,23e-5, 1,37e-4, 2,49e-4 (V mit Minimum an der Stelle)
  - Gegen AFM-KANAL-2 (kg-h0.02.json, per jq; dort mit nls2-Profilen): Die lokalisierte Lage ist bitgleich, die
    Nullstellen stimmen auf <= 6,4e-13, s auf <= 3,1e-10 relativ, Gamma auf <= 2,4e-14 relativ. Der neue
    Profilloeser trifft das Sextik-Modell also wie nls2.
- K2, Beispiele (Profilschritt 0,005):
  - omega^2 = 0,30: f0 = 6,7638, R_w = 3,665, Q = 7717,90, E = 5106,75
  - 0,55: f0 = 3,5428, R_w = 2,855, Q = 1452,55, E = 1248,57
  - 0,80: f0 = 1,8647, R_w = 2,698, Q = 464,79, E = 455,99
  - Q faellt mit omega (dQ/domega < 0) [ES].
- Gitter der Bandlaeufe:
  - Nullstellen von L(y_b) zwischen h = 0,02 und 0,01 gleich auf <= 4,2e-10 (b1), 1,4e-10 (b2, b3)
  - s im Betrag gleich auf <= 0,9 %, Vorzeichen ueberall gleich
  - Aussenrand R = 20 bis 27,5 (f < 1e-6 f(0)), Rand-Abweichung von A, B, C <= 2,7e-11
  - Wachstum der regulaeren Loesungen <= 3,7
  - 5999 bis 6001 rho-Punkte je Zeile, groesster Abstand <= 4,5e-4

## 5 Tabellen je Band (Hauptlaeufe, bball.py familie)

- Spalten: Nullstellen von L(y_b) je Zeile mit rho, s/median|W| (s = L(y_a) an der Nullstelle), Richtung (Vorzeichen
  von dL(y_b)/drho) und Polbreite Gamma = -Im rho_Pol (nur h = 0,02). Rechts s/median bei h = 0,01.
- Alle 45 Pole der Baender konvergiert (3 bis 4 Newton-Schritte), alle mit Gamma > 0. Kein Budget entfallen.
- s-Vorzeichen: Auf allen 125 Nullstellen der Hauptlaeufe (Zeilen und Zwischenreihen, je Stufe) gilt
  sgn s = +Richtung. Es gibt keinen Wechsel und keinen Kandidaten.

### b1 (omega^2 0,30 .. 0,40)

| omega^2 | R_w | Nullst. | rho (s/median, Richtung, Gamma) bei h = 0,02 | s/median bei h = 0,01 |
|---|---|---|---|---|
| 0.3 | 3.665 | 2 | 1.019732 (5.08e-2, +1, 1.9e-3); 1.421797 (-6.38e-2, -1, 1.46e-3) | 5.11e-2; -6.39e-2 |
| 0.31 | 3.611 | 2 | 1.036176 (5.8e-2, +1, 1.85e-3); 1.441107 (-7.25e-2, -1, 1.36e-3) | 5.77e-2; -7.25e-2 |
| 0.32 | 3.56 | 2 | 1.052361 (6.56e-2, +1, 1.79e-3); 1.459843 (-8.27e-2, -1, 1.26e-3) | 6.56e-2; -8.27e-2 |
| 0.33 | 3.511 | 2 | 1.0683 (7.04e-2, +1, 1.73e-3); 1.478018 (-8.87e-2, -1, 1.16e-3) | 7.03e-2; -8.89e-2 |
| 0.34 | 3.465 | 2 | 1.084005 (7.06e-2, +1, 1.67e-3); 1.495643 (-8.98e-2, -1, 1.07e-3) | 7.08e-2; -8.97e-2 |
| 0.35 | 3.421 | 2 | 1.099488 (7.17e-2, +1, 1.61e-3); 1.512724 (-9.14e-2, -1, 9.77e-4) | 7.17e-2; -9.14e-2 |
| 0.36 | 3.379 | 2 | 1.114759 (7.26e-2, +1, 1.54e-3); 1.529271 (-9.28e-2, -1, 8.91e-4) | 7.26e-2; -9.28e-2 |
| 0.37 | 3.339 | 2 | 1.129828 (7.33e-2, +1, 1.48e-3); 1.545287 (-9.42e-2, -1, 8.09e-4) | 7.33e-2; -9.42e-2 |
| 0.38 | 3.301 | 2 | 1.144705 (7.35e-2, +1, 1.41e-3); 1.560777 (-9.5e-2, -1, 7.31e-4) | 7.35e-2; -9.5e-2 |
| 0.39 | 3.265 | 2 | 1.159397 (7.32e-2, +1, 1.35e-3); 1.575743 (-9.54e-2, -1, 6.57e-4) | 7.32e-2; -9.54e-2 |
| 0.4 | 3.23 | 2 | 1.173913 (7.11e-2, +1, 1.28e-3); 1.590185 (-9.34e-2, -1, 5.87e-4) | 7.13e-2; -9.32e-2 |

| Streifen | omega^2 | Umlauf h = 0,02 / 0,01 | groesster Sprung (rad) h = 0,02 / 0,01 | aufgeloest | neue Profile |
|---|---|---|---|---|---|
| 0 | 0.3 .. 0.31 | 0 / 0 | 0.034 / 0.034 | ja / ja | 0 / 0 |
| 1 | 0.31 .. 0.32 | 0 / 0 | 0.036 / 0.036 | ja / ja | 0 / 0 |
| 2 | 0.32 .. 0.33 | 0 / 0 | 0.039 / 0.039 | ja / ja | 0 / 0 |
| 3 | 0.33 .. 0.34 | 0 / 0 | 0.041 / 0.041 | ja / ja | 0 / 0 |
| 4 | 0.34 .. 0.35 | 0 / 0 | 0.041 / 0.041 | ja / ja | 0 / 0 |
| 5 | 0.35 .. 0.36 | 0 / 0 | 0.035 / 0.035 | ja / ja | 0 / 0 |
| 6 | 0.36 .. 0.37 | 0 / 0 | 0.037 / 0.037 | ja / ja | 0 / 0 |
| 7 | 0.37 .. 0.38 | 0 / 0 | 0.038 / 0.038 | ja / ja | 0 / 0 |
| 8 | 0.38 .. 0.39 | 0 / 0 | 0.039 / 0.039 | ja / ja | 0 / 0 |
| 9 | 0.39 .. 0.4 | 0 / 0 | 0.04 / 0.04 | ja / ja | 0 / 0 |

- 0 s-Wechsel (31 Reihen je Stufe), 0 ungepaarte Nullstellen, 0 Kandidaten.

### b2 (omega^2 0,50 .. 0,60)

| omega^2 | R_w | Nullst. | rho (s/median, Richtung, Gamma) bei h = 0,02 | s/median bei h = 0,01 |
|---|---|---|---|---|
| 0.5 | 2.954 | 2 | 1.310917 (4.01e-2, +1, 6.99e-4); 1.704986 (-5.73e-2, -1, 8.42e-5) | 3.99e-2; -5.76e-2 |
| 0.51 | 2.932 | 1 | 1.323932 (3.85e-2, +1, 6.5e-4) | 3.84e-2 |
| 0.52 | 2.911 | 1 | 1.336844 (3.69e-2, +1, 6.03e-4) | 3.68e-2 |
| 0.53 | 2.892 | 1 | 1.349656 (3.53e-2, +1, 5.57e-4) | 3.52e-2 |
| 0.54 | 2.873 | 1 | 1.362374 (3.38e-2, +1, 5.14e-4) | 3.37e-2 |
| 0.55 | 2.855 | 1 | 1.375002 (3.23e-2, +1, 4.72e-4) | 3.23e-2 |
| 0.56 | 2.838 | 1 | 1.387544 (3.08e-2, +1, 4.33e-4) | 3.08e-2 |
| 0.57 | 2.822 | 1 | 1.400005 (2.93e-2, +1, 3.95e-4) | 2.93e-2 |
| 0.58 | 2.806 | 1 | 1.412389 (2.79e-2, +1, 3.6e-4) | 2.8e-2 |
| 0.59 | 2.792 | 1 | 1.4247 (2.67e-2, +1, 3.27e-4) | 2.66e-2 |
| 0.6 | 2.778 | 1 | 1.436942 (2.53e-2, +1, 2.96e-4) | 2.53e-2 |

| Streifen | omega^2 | Umlauf h = 0,02 / 0,01 | groesster Sprung (rad) h = 0,02 / 0,01 | aufgeloest | neue Profile |
|---|---|---|---|---|---|
| 0 | 0.5 .. 0.51 | 0 / 0 | 0.364 / 0.364 | ja / ja | 6 / 6 |
| 1 | 0.51 .. 0.52 | 0 / 0 | 0.366 / 0.366 | ja / ja | 0 / 0 |
| 2 | 0.52 .. 0.53 | 0 / 0 | 0.143 / 0.143 | ja / ja | 0 / 0 |
| 3 | 0.53 .. 0.54 | 0 / 0 | 0.074 / 0.074 | ja / ja | 0 / 0 |
| 4 | 0.54 .. 0.55 | 0 / 0 | 0.075 / 0.075 | ja / ja | 0 / 0 |
| 5 | 0.55 .. 0.56 | 0 / 0 | 0.079 / 0.079 | ja / ja | 0 / 0 |
| 6 | 0.56 .. 0.57 | 0 / 0 | 0.084 / 0.084 | ja / ja | 0 / 0 |
| 7 | 0.57 .. 0.58 | 0 / 0 | 0.088 / 0.088 | ja / ja | 0 / 0 |
| 8 | 0.58 .. 0.59 | 0 / 0 | 0.093 / 0.093 | ja / ja | 0 / 0 |
| 9 | 0.59 .. 0.6 | 0 / 0 | 0.099 / 0.099 | ja / ja | 0 / 0 |

- 0 s-Wechsel, 0 Kandidaten. 1 ungepaarte Nullstelle auf beiden Stufen: rho = 1,704986 bei 0,50, Ast k = 1. Er
  verlaesst das Fenster an der geschlossenen Schwelle vor der ersten Zwischenreihe 0,5033 (Randereignis wie in
  AFM-KANAL-2).

### b3 (omega^2 0,70 .. 0,80)

| omega^2 | R_w | Nullst. | rho (s/median, Richtung, Gamma) bei h = 0,02 | s/median bei h = 0,01 |
|---|---|---|---|---|
| 0.7 | 2.686 | 1 | 1.556545 (1.35e-2, +1, 8.35e-5) | 1.36e-2 |
| 0.71 | 2.682 | 1 | 1.568325 (1.25e-2, +1, 7.11e-5) | 1.25e-2 |
| 0.72 | 2.678 | 1 | 1.580094 (1.16e-2, +1, 6.01e-5) | 1.16e-2 |
| 0.73 | 2.676 | 1 | 1.591857 (1.06e-2, +1, 5.03e-5) | 1.06e-2 |
| 0.74 | 2.675 | 1 | 1.603622 (9.74e-3, +1, 4.16e-5) | 9.74e-3 |
| 0.75 | 2.675 | 1 | 1.615394 (8.87e-3, +1, 3.41e-5) | 8.87e-3 |
| 0.76 | 2.677 | 1 | 1.627182 (8.02e-3, +1, 2.76e-5) | 8.02e-3 |
| 0.77 | 2.679 | 1 | 1.638994 (7.15e-3, +1, 2.2e-5) | 7.15e-3 |
| 0.78 | 2.684 | 1 | 1.650839 (5.95e-3, +1, 1.73e-5) | 5.95e-3 |
| 0.79 | 2.69 | 1 | 1.662727 (4.92e-3, +1, 1.34e-5) | 4.92e-3 |
| 0.8 | 2.698 | 1 | 1.674669 (4.02e-3, +1, 1.01e-5) | 4.02e-3 |

| Streifen | omega^2 | Umlauf h = 0,02 / 0,01 | groesster Sprung (rad) h = 0,02 / 0,01 | aufgeloest | neue Profile |
|---|---|---|---|---|---|
| 0 | 0.7 .. 0.71 | 0 / 0 | 0.09 / 0.09 | ja / ja | 0 / 0 |
| 1 | 0.71 .. 0.72 | 0 / 0 | 0.099 / 0.099 | ja / ja | 0 / 0 |
| 2 | 0.72 .. 0.73 | 0 / 0 | 0.11 / 0.11 | ja / ja | 0 / 0 |
| 3 | 0.73 .. 0.74 | 0 / 0 | 0.123 / 0.123 | ja / ja | 0 / 0 |
| 4 | 0.74 .. 0.75 | 0 / 0 | 0.139 / 0.139 | ja / ja | 0 / 0 |
| 5 | 0.75 .. 0.76 | 0 / 0 | 0.158 / 0.158 | ja / ja | 0 / 0 |
| 6 | 0.76 .. 0.77 | 0 / 0 | 0.179 / 0.179 | ja / ja | 0 / 0 |
| 7 | 0.77 .. 0.78 | 0 / 0 | 0.206 / 0.206 | ja / ja | 0 / 0 |
| 8 | 0.78 .. 0.79 | 0 / 0 | 0.237 / 0.237 | ja / ja | 0 / 0 |
| 9 | 0.79 .. 0.8 | 0 / 0 | 0.272 / 0.272 | ja / ja | 0 / 0 |

- 0 s-Wechsel, 0 ungepaarte Nullstellen, 0 Kandidaten.
- Der Partner rho- aus Schritt 0 (0,12 bei 0,78 bis 0,80) erscheint gekoppelt nicht als Nullstelle von L(y_b) im
  Fenster [1 - omega + 0,002, ...]. Grund nicht untersucht; er liegt nur 0,014 bis 0,017 ueber der offenen Schwelle.

### Polbreiten (h = 0,02)

- b1: oberer Ast 1,46e-3 -> 5,87e-4, unterer Ast 1,90e-3 -> 1,28e-3, beide monoton fallend
- b2: Ast k = 0 6,99e-4 -> 2,96e-4; Ast k = 1 8,42e-5 (nur 0,50)
- b3: 8,35e-5 -> 1,01e-5, monoton fallend
- Kein inneres Minimum in den Baendern.
- Gamma ~ s^2 gilt nur grob [ES]. Beispiel b3 von 0,70 auf 0,80: Gamma faellt um den Faktor 8,3, s (roh) um 2,5
  (s^2: 6,3), s/median um 3,4 (s^2: 11,3).

## 6 Nachtrag 1 (NACHTRAEGLICH; aendert den Ausgang in Abschnitt 1, Punkt 1 nicht)

- Festgelegt nach Kenntnis der Hauptlaeufe (PLAN Abschnitt 12, geschrieben ab 19:27:49, eingefroren 19:28:02 als
  PLAN.md.nachtrag-eingefroren-20261001-192802). Gestartet 17:28:16 UTC (19:28:16 CEST), nach dem Einfrieren.
- Lauf: bball.py unveraendert, Band "b3plus" mit omega^2 = 0,80 .. 0,95 (16 Zeilen, Abstand 0,01), sonst alles wie
  in den Hauptlaeufen.
  - h = 0,02 mit Polen: cpu3, 130,2 s, rc = 0
  - h = 0,01: cpu4, 226,7 s, rc = 0
  - Ausgabe lauf-69/aus-nachtrag/

| omega^2 | R_w | R | Nullst. | rho (s/median, Richtung, Gamma) bei h = 0,02 | s/median bei h = 0,01 |
|---|---|---|---|---|---|
| 0.8 | 2.698 | 27.54 | 1 | 1.674669 (4.02e-3, +1, 1.01e-5) | 4.02e-3 |
| 0.81 | 2.708 | 28.14 | 1 | 1.686679 (3.26e-3, +1, 7.49e-6) | 3.26e-3 |
| 0.82 | 2.72 | 28.8 | 1 | 1.69877 (2.6e-3, +1, 5.4e-6) | 2.6e-3 |
| 0.83 | 2.735 | 29.5 | 1 | 1.710959 (2.05e-3, +1, 3.77e-6) | 2.05e-3 |
| 0.84 | 2.753 | 30.28 | 1 | 1.723263 (1.58e-3, +1, 2.53e-6) | 1.58e-3 |
| 0.85 | 2.774 | 31.14 | 1 | 1.735706 (1.19e-3, +1, 1.63e-6) | 1.19e-3 |
| 0.86 | 2.799 | 32.1 | 1 | 1.748311 (8.67e-4, +1, 9.87e-7) | 8.67e-4 |
| 0.87 | 2.829 | 33.16 | 1 | 1.76111 (6.1e-4, +1, 5.57e-7) | 6.09e-4 |
| 0.88 | 2.865 | 34.36 | 1 | 1.774138 (4.06e-4, +1, 2.85e-7) | 4.06e-4 |
| 0.89 | 2.907 | 35.7 | 2 | 0.061438 (1.95e-1, -1, -); 1.787439 (2.52e-4, +1, 1.28e-7) | 1.94e-1; 2.51e-4 |
| 0.9 | 2.958 | 37.26 | 2 | 0.058837 (1.79e-1, -1, -); 1.801068 (1.39e-4, +1, 4.61e-8) | 1.79e-1; 1.39e-4 |
| 0.91 | 3.021 | 39.08 | 2 | 0.055929 (1.63e-1, -1, -); 1.815093 (6.27e-5, +1, 1.13e-8) | 1.63e-1; 6.27e-5 |
| 0.92 | 3.098 | 41.24 | 2 | 0.052667 (1.46e-1, -1, -); 1.829603 (1.58e-5, +1, 8.83e-10) | 1.46e-1; 1.58e-5 |
| 0.93 | 3.194 | 43.84 | 2 | 0.048994 (1.27e-1, -1, -); 1.844712 (-8.06e-6, +1, 2.94e-10) | 1.28e-1; -8.08e-6 |
| 0.94 | 3.319 | 47.06 | 2 | 0.044833 (1.09e-1, -1, -); 1.860579 (-1.56e-5, +1, 1.47e-9) | 1.09e-1; -1.56e-5 |
| 0.95 | 3.485 | 51.24 | 2 | 0.040088 (8.93e-2, -1, -); 1.877425 (-1.34e-5, +1, 1.56e-9) | 8.93e-2; -1.34e-5 |

| Streifen | omega^2 | Umlauf h = 0,02 / 0,01 | groesster Sprung (rad) h = 0,02 / 0,01 | aufgeloest | min/median \|W\| (h = 0,02) |
|---|---|---|---|---|---|
| 0 | 0.8 .. 0.81 | 0 / 0 | 0.333 / 0.333 | ja / ja | 3.36e-3 |
| 1 | 0.81 .. 0.82 | 0 / 0 | 0.385 / 0.385 | ja / ja | 2.7e-3 |
| 2 | 0.82 .. 0.83 | 0 / 0 | 0.385 / 0.385 | ja / ja | 2.11e-3 |
| 3 | 0.83 .. 0.84 | 0 / 0 | 0.396 / 0.396 | ja / ja | 1.64e-3 |
| 4 | 0.84 .. 0.85 | 0 / 0 | 0.396 / 0.396 | ja / ja | 1.23e-3 |
| 5 | 0.85 .. 0.86 | 0 / 0 | 0.377 / 0.377 | ja / ja | 8.97e-4 |
| 6 | 0.86 .. 0.87 | 0 / 0 | 0.371 / 0.371 | ja / ja | 6.32e-4 |
| 7 | 0.87 .. 0.88 | 0 / 0 | 0.371 / 0.371 | ja / ja | 4.26e-4 |
| 8 | 0.88 .. 0.89 | 0 / 0 | 0.362 / 0.362 | ja / ja | 2.63e-4 |
| 9 | 0.89 .. 0.9 | 0 / 0 | 0.394 / 0.394 | ja / ja | 1.48e-4 |
| 10 | 0.9 .. 0.91 | 0 / 0 | 0.394 / 0.394 | ja / ja | 6.63e-5 |
| 11 | 0.91 .. 0.92 | 0 / 0 | 0.389 / 0.389 | ja / ja | 1.71e-5 |
| **12** | **0.92 .. 0.93** | **-1 / -1** | 0.389 / 0.389 | ja / ja | 8.77e-6 |
| 13 | 0.93 .. 0.94 | 0 / 0 | 0.367 / 0.367 | ja / ja | 7.43e-6 |
| 14 | 0.94 .. 0.95 | 0 / 0 | 0.388 / 0.388 | ja / ja | 1.41e-5 |

- **Ein s-Wechsel auf beiden Stufen:** Ast Richtung +1, zwischen den Zwischenreihen 0,923333 (rho 1,834566,
  s = +1,16e-5) und 0,926667 (rho 1,839600, s = -4,95e-6).
- **Lokalisiert (Illinois, 5 Schritte):**
  - h = 0,02: omega*^2 = 0,92560981, rho* = 1,83799594, Klammer 3,4e-10
  - h = 0,01: omega*^2 = 0,92560989, rho* = 1,83799607, Klammer 4,0e-10
  - Stufen gleich auf 8e-8 in omega^2 und 1,2e-7 in rho; drho/domega^2 = 1,514
- **Kleines Rechteck** omega*^2 +- 4e-4, rho* +- 2e-3:
  - h = 0,02: Umlauf -1,0000 (Kreuzung -1), groesster Sprung 0,398 rad (links 0,393, rechts 0,398, unten 1,2e-4,
    oben 1,5e-4), aufgeloest
  - h = 0,01: Umlauf -1,0000 (Kreuzung -1), groesster Sprung 0,398 rad, aufgeloest
  - min|W|/median im Rechteck 4,5e-4
  - Die rho-Seiten werden halbiert, bis jeder Sprung unter 0,4 rad liegt; Werte knapp unter 0,4 sind deshalb zu
    erwarten (K1: 0,359, AFM-KANAL-2: 0,399).
- **Kriterium des Nachtrags = "Gesehen"-Kriterium der Karte: erfuellt auf beiden Stufen**, aber im Band b3plus, das
  die Karte nicht hat.
- Polbreite auf dem Ast (h = 0,02): 1,01e-5 (0,80), 2,85e-7 (0,88), 8,8e-10 (0,92), **2,9e-10 (0,93)**, 1,47e-9
  (0,94), 1,56e-9 (0,95). Das V hat sein Minimum an der Stelle, wie beim Sextik-K1.
- Bei 0,94 -> 0,95 nimmt |s| wieder ab (s/median -1,56e-5 -> -1,34e-5). Ob s oberhalb von 0,95 ein zweites Mal das
  Vorzeichen wechselt, ist nicht gerechnet (offene Frage).
- Ab 0,8833 erscheint ein Schwellenzustand an der offenen Schwelle (rho 0,063 -> 0,040, Richtung -1, s/median
  +0,19 -> +0,09). Sein Auftauchen ist der einzige ungepaarte Eintrag; danach ist er gepaart, ohne s-Wechsel.
- Lage im Vergleich [ES]:
  - nackter Zustand bei 0,90: rho+ = 1,7974 (Schritt-0-Rauchtest); gekoppelt 1,8011
  - die Stelle sitzt also wie beim Sextik-Modell (nackt 1,7335, Stelle 1,7446) auf dem Ast k = 0 dicht am nackten
    Zustand

## 7 Vorab gegen Ausgang

| Vorab (Quelle) | Ausgang |
|---|---|
| Leitung: K1 besteht ~85 % | eingetreten (beide Stufen, Abweichung <= 5e-7) |
| Leitung: Schritt 0 findet einen nackten Zustand im Kontinuum ~60 % | eingetreten, in allen drei Baendern (b1 zwei, b2 ein bis zwei, b3 einer) |
| Leitung: Gesehen in den drei Baendern ~45 % | **nicht eingetreten** ("Nicht gesehen") |
| Leitung, dafuer: n = 1 sitzt beim Sextik im dicken Ball, nicht an der Duennwand | [H] gestuetzt durch den Nachtrag: Die Log-Stelle sitzt in einem noch dickeren Ball (0,926) |
| Leitung, dagegen: keine Duennwandgrenze, anderer Kanal-Topf | [H] passt zu den Baendern: Die Kopplung faellt bis 0,80 nur langsam (s/median 1,4e-2 -> 4,0e-3) und wechselt erst bei 0,926 |
| Leitung: falls gesehen, rho 1,5 .. 1,95 | entfaellt nach der Regel; die Nachtragsstelle liegt mit rho* = 1,838 in diesem Bereich |
| E-1 K1 besteht auf beiden Stufen ~92 % | eingetreten |
| E-2 Gesehen 15 / Nicht gesehen 55 / Unentschieden 30 % | "Nicht gesehen" eingetreten |
| E-2, Begruendung [H]: s in b3 linear erst bei ~0,86 null | falsch in der Zahl: s faellt immer langsamer und wechselt erst bei 0,9256 |
| E-3 falls gesehen: b2 oder b3, rho 1,5 .. 1,75 ~60 % | entfaellt |
| E-4 Polbreiten 1e-5 bis 1e-2, kein Ast schmaler als 1e-7 (Baender) ~75 % | eingetreten: 1,01e-5 bis 1,90e-3 |
| E-5 Streifen-Umlauf und s-Wechsel stimmen je Streifen ueberein ~90 % | eingetreten (Baender ueberall 0/0; K1 -1/1; Nachtrag -1/1) |
| Nachtrag: s-Wechsel zwischen 0,80 und 0,95 ~70 % | eingetreten (0,9233 .. 0,9267) |
| Nachtrag: falls ja, Kriterium auf beiden Stufen ~90 % | eingetreten |
| Nachtrag: Lage omega*^2 in [0,84; 0,92] und rho* in [1,70; 1,80] ~65 % | nicht eingetreten (0,9256 / 1,838) |
| Nachtrag: Umlauf -1 wie K1 ~80 % | eingetreten |
| Nachtrag: V-foermiges Gamma-Minimum ~80 % | eingetreten (2,9e-10 bei 0,93) |
| Nachtrag: alle Streifen aufgeloest ~85 % | eingetreten (15 von 15, beide Stufen) |

## 8 Laufzeiten, Spuren, Hashes

- .69, alle ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, nur Spuren cpu3 und cpu4. Alle rc = 0, alle
  unter 10 min Wanduhr, kein Budget entfallen. Zeiten UTC (CEST = UTC + 2 h).

| Lauf | Spur | Start | Ende | Laufzeit |
|---|---|---|---|---|
| s0-log-h0.02 (Schritt 0) | cpu3 | 17:19:16 | 17:19:24 | 7,3 s |
| s0-log-h0.01 (Schritt 0) | cpu4 | 17:19:16 | 17:19:32 | 16,2 s |
| k2-log (K2) | cpu3 | 17:20:25 | 17:20:44 | 18,7 s |
| PLAN eingefroren | - | 17:23:22 | - | - |
| kg-h0.02 (K1) | cpu3 | 17:23:25 | 17:24:16 | 50,4 s |
| kg-h0.01 (K1) | cpu4 | 17:23:25 | 17:24:53 | 87,5 s |
| auswertung-k1 | cpu3 | 17:24:53 | 17:24:54 | 0,0 s |
| log-b1-h0.02 | cpu3 | 17:24:54 | 17:25:29 | 34,7 s |
| log-b1-h0.01 | cpu4 | 17:24:54 | 17:25:48 | 53,5 s |
| log-b2-h0.02 | cpu3 | 17:25:29 | 17:26:10 | 40,3 s |
| log-b2-h0.01 | cpu4 | 17:25:48 | 17:26:52 | 63,6 s |
| log-b3-h0.02 | cpu3 | 17:26:10 | 17:26:51 | 40,5 s |
| log-b3-h0.01 | cpu4 | 17:26:52 | 17:27:57 | 65,1 s |
| auswertung | cpu3 | 17:27:57 | 17:27:58 | 0,1 s |
| Nachtrag eingefroren | - | 17:28:02 | - | - |
| nachtrag-b3plus-h0.02 | cpu3 | 17:28:16 | 17:30:27 | 130,2 s |
| nachtrag-b3plus-h0.01 | cpu4 | 17:28:16 | 17:32:03 | 226,7 s |

- Starter start.sh: einmalig per nohup, 17:23:25 bis 17:27:58 UTC. Die Nachtragslaeufe sind direkt per kleintest.sh
  gestartet (setsid/nohup), je einer pro Spur.
- Vorab erwartet: 1 bis 5 min je Bandaufruf; gemessen 35 bis 65 s. K1 wie erwartet: 50 und 88 s.
- Rauchtests lokal: System-python3, 1 Thread, nice 19, timeout 115 bis 120 s; Ausgaben in lauf-lokal/.
  - rauch-s0-kg 2,9 s; rauch-s0-log 2,1 s; rauch-k2 4,3 s
  - rauch-kg 9,5 s; rauch-log-b3 3,6 s; rauch-log-b1 2,5 s
  - Summe 24,9 s
- sha256:
  - bball.py 2edf52b6344aa4dc88cdca095c022a3d06b27e5c2215e1a9b0e97accbe2f349b (lokal = .69, alle Laeufe)
  - start.sh d8548ceb8c37829bf8d5d95b798f68640f92242eecf3d128fe8bca5210aac6fa (lokal = .69)
  - KARTE.md 2794de28cf18ce6395a00b2bed67836d15c61d6b0d1f16ff36a65b71e25ab811
  - PLAN.md.eingefroren-20261001-192322 7a73053cd0843fff1dbe38976808d060862e44dd4d00b1980665c0ba29f34a44
  - PLAN.md.nachtrag-eingefroren-20261001-192802 ec7c7f21bd1385db2a16993b930a2b0f5bad389041c20c39c92e02428d1226da
    (= PLAN.md am Ende)
  - Quellen:
    - hep-ph-9909509v3.pdf dc7f1a96b484a6def22f3c24bfd00ebbe27e7f75c64218de9504e87d1a9fdf04
    - hep-ph-9909509v3.txt 6958a3578686089b04a40b70167498555b42333b79592a5b6d1ba3aa0b23f58a
    - arxiv-abfrage-1.xml c87ea12931cb2a0ee79e83aab7cfef3ad32b9196a15ae96dd7f1c90938bdcd51
  - Ausgaben lauf-69/aus/:
    - auswertung.json 2819b2e5bcc13a13fc3e2702909c9e2f1aa34cd3f016952fa4dc284f15fdf06b
    - auswertung-k1.json dace27751f208a6febe3c62cdedbaca0e77a2c198fcd72ff7a129678ee2aae4e
    - k2-log.json e1e416997b0211a806db061ecc70e26e3e431a5d5bafae10158357961d9dc1b6
    - kg-h0.02.json 90e59e92ab318422ce8eb0e697b15ffe950f17c440f7c14c730ce93321c3ad55
    - kg-h0.01.json 023346d129882afb84187d1f1a132297eb02c8305abf22c65ea97bcb7538af7d
    - log-b1-h0.02.json f884de09e66dbf0ad1d259ff48cc47f56f120e2a053d12cb65114cc1ea535974
    - log-b1-h0.01.json fdeecab671529885e8588105526302097fd04ef38f8b24a2fd28d414fa07928f
    - log-b2-h0.02.json 7c8f2363341145efd019020dbddad3ebe8aa928c2ec989a20e778067a719ce56
    - log-b2-h0.01.json e7c67de360f4787dd19fae944dc0476700618146039a857f4af7416adf1d6719
    - log-b3-h0.02.json 08cc8eded058e382469e080aa7e2dd2d9188eaee62721a35b1cb3d0ce52ffd92
    - log-b3-h0.01.json 4ca283a79a7a9d214afdce743cb5422e83201bfc7ca3bdf74bfff1048e3ce20b
    - s0-log-h0.02.json 4d34402e7c1453de416900a5a5059ecbb2615c1e18ec4d61e6c46ec865e7612a
    - s0-log-h0.01.json f74fe5533f2860e0268df5723e2b8944716ae78563f8f121ac7041c0fb50ce65
  - Ausgaben lauf-69/aus-nachtrag/:
    - nachtrag-b3plus-h0.02.json 2fb712b11946a5e86d5a00e79f15e6356efcf2c6ca5a7738a004f333c52d12c8
    - nachtrag-b3plus-h0.01.json aa86818add341f669aacc46c1839a6e55e2191f222f4453088da9d513513f45c

## 9 Selbstanzeigen

1. Der erste arXiv-Abruf (19:12:18, http) kam leer zurueck, weil curl der Umleitung nicht folgte. Die leere Datei
   lag kurz im Ordner und wurde geloescht. Danach kam der Abruf per https (19:12:25, 7 s Abstand) und das PDF
   (19:12:41).
2. s0-log-h0.02 enthaelt als 34. Zeile versehentlich das Log-Modell bei omega^2 = 0,7977. Gemeint war eine
   Sextik-Kontrolle, die aber schon im Rauchtest lief. Die Zeile ist ohne Bedeutung und wird nirgends verwendet.
3. Der ssh-Aufruf, der start.sh per nohup startete, kehrte erst nach dem Ende des Starters zurueck (19:27:58); das
   Werkzeug legte ihn nach 120 s in den Hintergrund. Die Laeufe betraf das nicht. Ausgaben der Hintergrund-Aufrufe
   und Warteschleifen (nur ssh, grep, sleep) legte das Werkzeug unter /tmp/claude-1000/.../tasks/ ab.
4. Lokal benutzte Werkzeuge ausserhalb der Liste "jq, grep, sed, cut, sha256sum, rsync, ssh, date":
   - curl (arXiv-API, vom Auftrag verlangt), pdftotext und pdfinfo (Quelle als Text)
   - seq und paste (Zeilenlisten), sowie ls, cat, head, tail, wc, mkdir, cp, chmod, rm, sleep
   - python3 nur in den 6 Rauchtests (Abschnitt 8); kein leerer Aufruf.
   - **Ein lokaler awk-Aufruf, kurz vor 19:37:45 CEST (date direkt danach):** Er stand in einer Pipe zur Pruefung
     der Tabellenzeilen von ERGEBNIS.md (Spalten zaehlen) und wurde mit head -0 verworfen, ohne Ausgabe und ohne
     Rechnung. Das verstoesst gegen "lokal kein awk". Sonst kein awk.
5. Der Nachtrag ist nach Kenntnis der Hauptlaeufe beschlossen; der Anlass war der Trend von s in b3. Geschrieben ab
   19:27:49, als b3 (h = 0,01) und die Schlussauswertung noch liefen (Ende 19:27:58). Eingefroren 19:28:02, vor dem
   Start (19:28:16). Er ist darum kein blinder Test.
6. Die Tabellen in Abschnitt 5 und 6 sind per jq aus den JSON-Ausgaben erzeugt. Die Hilfsdateien dafuer lagen
   nur im eigenen Ordner und sind nach dem Einfuegen geloescht.
7. Kein git, kein Peerbus, keine Unteragenten, keine Dienste, Timer oder Hooks. Auf der .69 nichts in place
   ueberschrieben. Gesperrte Pfade nicht gelesen. Nur Spuren cpu3 und cpu4.
8. Drei Fehler im eingefrorenen PLAN, beim Gegenlesen gefunden. Der PLAN bleibt unveraendert; richtig steht es hier.
   Keiner betrifft Regel, Raster oder Ausgang.
   - (a) Gl. (8) der Quelle steht auf PDF-Seite 3, nicht 2. Gl. (1) steht wirklich auf Seite 2.
   - (b) Abschnitt 4 nennt fuer alle nackten Zustaende "r_spitze 2,2 bis 5,5; P = 3,8 bis 7,2". Die schwellennahen
     Zustaende in b2 (0,50 bis 0,52) haben r_spitze 5,7 bis 6,2 und P = 16,6 bis 24,4 (Abschnitt 3).
   - (c) Abschnitt 10 (E-2) nennt fuer das Sextik-Modell "~1e-2 je 0,005". Richtig ist ~5e-3 je 0,005 (s roh,
     AFM-KANAL-2: +2,9e-3 bei 0,795, -2,4e-3 bei 0,80).

## 10 Grenzen

- Radial l = 0, ein Potential der Klasse (U = ln(1 + S)), ohne Hubble- und |Phi|^6-Term. Andere flache Formen
  (etwa die gravitationsvermittelte Variante mit K < 0 [L?]) sind nicht gerechnet.
- "Nicht gesehen" gilt nur auf diesem Raster:
  - Zwischen zwei Reihen (Abstand 0,0033) koennte ein Paar entgegengesetzter Nullstellen von W liegen. Der
    Streifen-Umlauf 0 schliesst das nicht aus.
  - Die schmalen Keile zwischen benachbarten Fenstern decken die Streifen nicht ab.
  - Fensterrand 0,002 an beiden Schwellen; der Partner rho- in b3 liegt nahe daran und erscheint nicht als
    Nullstelle.
- Die Luecken zwischen den Baendern (0,40 .. 0,50, 0,60 .. 0,70), omega^2 < 0,30 und > 0,95 sind nicht gerechnet.
- Der Nachtrag ist nachtraeglich und nicht blind. Er hat dieselbe Maschine, dieselben Schwellen und zwei Stufen; ob
  er zaehlt, entscheidet die Leitung.
- An der Nachtragsstelle sind die Breiten sehr klein (Gamma ~ 3e-10 bei 0,93). Die Newton-Toleranz (1e-11) loest
  sie noch auf.
- Labor: nichts gemessen. Die Datennaehe der B-Baelle (Dunkle Materie, Super-K) beruehrt dieser Test nicht.

## 11 Einfach gesagt

Ein Q-Ball ist ein Klumpen aus einem Feld, der sich durch eine erhaltene Ladung selbst zusammenhaelt. Wir haben
nachgesehen, ob ein solcher Ball im "flachen" Potential, wie es in Supersymmetrie-Modellen vorkommt, an bestimmten
Stellen schwingen kann, ohne Energie nach aussen abzugeben. In den drei Bereichen, die die Karte vorgab, gibt es
keine solche stille Stelle: Die Abstrahlung wird zwar zum dicken Ball hin schwaecher, aber nie null. Erst ein
nachtraeglicher Lauf etwas weiter draussen (bei einem noch dickeren Ball) findet eine stille Stelle, auf zwei
Rechengittern gleich und mit dem gleichen Drehsinn wie beim bekannten Modell. Die stille Stelle ist also wohl nicht an
das alte Potential gebunden, sie wandert nur an eine andere Stelle; ob das zaehlt, entscheidet die Leitung, weil der
Bereich nicht vorab festgelegt war.

---
Ende: 2026-10-01 19:38:42 CEST (date, nach dem Schreiben gemessen). Alle .69-Aufrufe beendet (rc = 0): 3 Vorlaeufe (Schritt 0, K2), 8 Rechenlaeufe, 2 Auswertungen, 2 Nachtragslaeufe.

## Karte 2: B-BALL-2 Interpolation (Folgeauftrag; Abschnitt geschrieben ab 2026-10-01 20:02 CEST)

- Entscheidung der Leitung zu Nachtrag 1: Der Ausgang der ersten Karte bleibt "Nicht gesehen". Der Fund bei
  omega^2 = 0,925610 zaehlt nicht fuer die erste Karte. Karte 2 (KARTE-2-INTERPOLATION.md) prueft ihn mit
  vorab gebundener Vorhersage ueber das Mischpotential U_t = (1 - t)(S - S^2 + S^3/2) + t ln(1 + S).
- Volltext: ERGEBNIS-KARTE2.md; Plan: PLAN.md Abschnitt 13, eingefroren als
  PLAN.md.karte2-eingefroren-20261001-194516.
- **Gesamt nach der Regel der Karte 2: "Kontinuitaet traegt".** K1 (t = 0) und K2 (t = 1) bestanden, beide Stufen.

| t | Ausgang | omega*^2 (h = 0,02) | rho* (h = 0,02) | Abstand zur linearen Vorhersage (omega^2; rho) | Umlauf (beide Stufen) |
|---|---|---|---|---|---|
| 0 (K1) | bestanden | 0,79767677 | 1,74461754 | Ziel: -2,3e-7; -4,6e-7 | -1 |
| 0,25 | Gefunden | 0,83076540 | 1,77194114 | +0,0011; +0,0039 | -1 |
| 0,5 | Gefunden | 0,85882391 | 1,79581481 | -0,0029; +0,0045 | -1 |
| 0,75 | Gefunden | 0,87651902 | 1,81004334 | -0,0171; -0,0047 | -1 |
| 1 (K2) | bestanden | 0,92560981 | 1,83799594 | Ziel: -1,9e-7; -5,9e-8 | -1 |

- Die Stufen stimmen je t auf <= 1,3e-8 (t-Laeufe) bzw. 1,2e-7 (K2) ueberein. Alle 16 Streifen je Lauf sind
  aufgeloest; genau einer hat Umlauf -1, und zwar der mit der Stelle.
- [H] Die erste stille Stelle des Log-Balls ist ueber das Mischpotential dieselbe wie die bewiesene Sextik-Stelle,
  stetig verschoben. Offen bleibt der grosse Schritt zwischen t = 0,75 und 1 (omega^2 +0,049).
- Abschnitt Karte 2 beendet: 2026-10-01 20:02:04 CEST (date).
