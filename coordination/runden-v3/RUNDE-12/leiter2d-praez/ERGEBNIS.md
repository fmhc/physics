# LEITER-2D-PRAEZ: Ergebnis (Runde 12, explorativ)

- Code-Agent im Auftrag der Leitung claude-primary. Geschrieben ab 2026-10-01 17:40:58 CEST (date).
- Beginn 17:12:18 CEST. Plan eingefroren 17:24:46 (PLAN.md.eingefroren-20261001-172446). Nachtrag eingefroren 17:39:25
  (PLAN.md.nachtrag-eingefroren-20261001-173925).
- Hauptlaeufe RM9, RM12, RM15, REC und FEIN: .69, 15:32:20 bis 15:36:16 UTC, alle rc = 0.
- Folgelaeufe F6, F8, REC2 und F7b: .69, 15:39:45 bis 15:46:18 UTC, alle rc = 0 (F7 vor dem Start beendet, rc = 143, siehe Abschnitt 7).

## 1. Ausgang nach der Scheiterregel: **unentschieden**

| Kriterium (Wortlaut der Leitung) | Befund | erfuellt? |
|---|---|---|
| (b) s wechselt bei 0,5285 bis 0,5300 unter geaendertem r_m das Vorzeichen | s fuer r_m = 9, 12 und 15 gleich bis auf ~3e-11 relativ, ueberall negativ | nein |
| (b) ein aufgeloestes Rechteck zeigt Umlauf +-1 | beide Rechtecke Umlauf -1,0000, aber nicht aufgeloest (groesster Sprung 1,82 und 2,60 rad > 0,4) | nein (formal) |
| (a) s bleibt fuer alle r_m negativ und die Rechtecke zeigen Umlauf 0 | s negativ ja; Umlauf ist -1, nicht 0 | nein |

- Damit gilt keiner der beiden Ausgaenge, also "unentschieden".
- Der Grund ist ein anderer als in beiden Lesarten vorgesehen. Der Anschlussradius aendert gar nichts, und die
  Rundung spielt keine Rolle. Das zeigt sich so:
  - Die Fast-Ausloeschung liegt am Kandidaten bei hoechstens 5,8e4.
  - Der Kernzuwachs am Kandidaten liegt bei hoechstens 2,9e4. Die 1,9e6 aus R11 sind das Maximum ueber das ganze
    rho-Fenster.
- Nachtraeglich gefunden: Der Vorzeichentest in kurve tastet rho zu grob ab. Er nimmt 400 Punkte mit Abstand 3,6e-3
  und interpoliert linear. Bei n >= 7 ist s dann vom Interpolationsfehler beherrscht (Abschnitte 2 und 3).

**Nachtraeglich (Abschnitt 3; aendert den vorab festgelegten Ausgang nicht, die Leitung entscheidet ueber die
Wertung):**

- REC2 (dasselbe Rechteck, nur 20 statt 8 Halbierungsrunden) ist aufgeloest und zeigt Umlauf -1 auf beiden Rechtecken.
  Das erfuellt das (b)-Kriterium "aufgeloestes Rechteck mit Umlauf +-1".
- Mit 4000 statt 400 rho-Punkten wechselt s bei n = 8 das Vorzeichen (F8). Die Verfeinerung trifft 0,525780; die
  Breite faellt auf 1,9e-8.
- Bei n = 7 zeigen das Rechteck, der Nulldurchgang der Abstrahlamplitude A_out (0,5292675) und das V der Polbreite
  (Raster bis 1,8e-7, nach Verfeinerung auf Rauschhoehe) dieselbe Stelle.
- Damit gilt eine **Lesart (b) in praezisierter Form [H, numerisch, explorativ]:** Nicht die Rechengenauigkeit, sondern
  die grobe rho-Abtastung des Vorzeichentests verliert die Sprossen ab n = 7.
  - n = 7 bei 0,5292654 (F7b; A_out-Nulldurchgang 0,5292675) und n = 8 bei 0,525780 sind stille Stellen mit den
    Leiterschritten 4,624 bzw. 4,620 in 1/eps.
  - Lesart (a), Abbruch nach n = 6, ist fuer dieses Modell und diesen Code nicht haltbar: n = 7 und n = 8 sind gefunden.
  - Belegstufe: Umlauf -1 (aufgeloest) nur fuer n = 7; n = 8 nur Vorzeichenwechsel plus Breitenminimum.
- **Folgerungen [H, nicht geprueft]:**
  - Die R11-Aussage "Die Leiter endet auf diesem Raster bei n = 6" geht auf die grobe Abtastung zurueck.
  - Das 3D-Versagen von kurve ab n = 7 ("Zweigmischung", RUNDE-08/09) hat vermutlich dieselbe Ursache.
  - Empfehlung fuer kurve: rho um jeden Kandidaten lokal fein nachtasten, oder n_rho >= 4000. Den Umlauf mit mehr als
    8 Halbierungsrunden rechnen (v2: --u-runden).

## 2. Hauptlaeufe (vorab festgelegt)

### 2a. s gegen r_m (kurve, h = 0,02, Rand R = 31,76; Kernzuwachs am Kandidaten / Maximum ueber das rho-Fenster)

| r_m | omega^2 | rho_b | s = L(y_a) | Pol (Pluecker) | Kernzuwachs | Ausloeschung |
|---|---|---|---|---|---|---|
| 9 | 0,5285 | 1,555671 | -6,98673e-5 | 1,5524035 - 1,972e-3 i | 2,2e3 / 6,4e4 | 1,8e3 |
| 9 | 0,5290 | 1,556165 | -8,77470e-5 | 1,5548957 - 2,346e-4 i | 2,2e3 / 6,4e4 | 1,7e3 |
| 9 | 0,5295 | 1,556657 | -1,12740e-4 | 1,5578110 - 1,743e-4 i | 2,2e3 / 6,4e4 | 1,6e3 |
| 9 | 0,5300 | 1,557149 | -1,40865e-4 | 1,5602363 - 1,610e-3 i | 2,2e3 / 6,4e4 | 1,5e3 |
| 12 | 0,5285 | 1,555671 | -6,98673e-5 | 1,5524035 - 1,972e-3 i | 2,9e4 / 1,9e6 | 5,8e4 |
| 12 | 0,5290 | 1,556165 | -8,77470e-5 | 1,5548957 - 2,346e-4 i | 2,4e4 / 1,7e6 | 3,1e4 |
| 12 | 0,5295 | 1,556657 | -1,12740e-4 | 1,5578110 - 1,743e-4 i | 2,0e4 / 1,4e6 | 1,2e4 |
| 12 | 0,5300 | 1,557149 | -1,40865e-4 | 1,5602363 - 1,610e-3 i | 1,7e4 / 1,2e6 | 1,2e3 |
| 15 | 0,5285 | 1,555671 | -6,98673e-5 | 1,5524035 - 1,972e-3 i | 1,4e4 / 1,4e6 | 1,9e4 |
| 15 | 0,5290 | 1,556165 | -8,77470e-5 | 1,5548957 - 2,346e-4 i | 1,0e4 / 1,2e6 | 1,1e4 |
| 15 | 0,5295 | 1,556657 | -1,12740e-4 | 1,5578110 - 1,743e-4 i | 7,4e3 / 1,1e6 | 6,5e3 |
| 15 | 0,5300 | 1,557149 | -1,40865e-4 | 1,5602363 - 1,610e-3 i | 5,5e3 / 1,0e6 | 3,9e3 |

- Die drei r_m geben dieselben s-Werte. Sie unterscheiden sich um hoechstens 2e-15 absolut, etwa 3e-11 relativ.
  Beispiel 0,5285: -6,98673210199896e-5 / -6,986732101885162e-5 / -6,986732102091942e-5.
- Die Pluecker-Pole sind auf etwa 1e-15 gleich.
- **r_m = 12 reproduziert R11-d bitgleich**, etwa s(0,5285) = -6,986732101885162e-5 und |Im Pol(0,5295)| =
  1,7431781435970172e-4.
- **Ausloeschungsmass:** der groesste Einzelterm von Omega(y_a, z2)*|nz|, geteilt durch |s|. Es liegt ueberall bei
  <= 5,8e4.
  - Rundung allein gaebe einen relativen Fehler von etwa 1e-16 * 6e4, also ~1e-11. Das ist genau die gemessene
    r_m-Streuung.
  - Rundung als Ursache ist damit ausgeschlossen.

### 2b. Positivkontrolle n = 6 (in denselben Laeufen)

| r_m | s(0,533) | s(0,535) | Wechsel | Verfeinerung omega*^2 | Pol am Ende |
|---|---|---|---|---|---|
| 9 | -1,02591e-4 | +1,44041e-4 | ja | 0,53384528386 | 1,56089233 - 5,0e-9 i |
| 12 | -1,02591e-4 | +1,44041e-4 | ja | 0,53384528386 | 1,56089233 - 5,0e-9 i |
| 15 | -1,02591e-4 | +1,44041e-4 | ja | 0,53384528386 | 1,56089233 - 5,0e-9 i |

- Der Wechsel bleibt bei jedem r_m. Die verfeinerte Lage ist auf 6e-14 gleich und trifft 0,5338453 aus R11-a.
  P3 getroffen.

### 2c. Rechteck um (0,5292; 1,557) (exakt mit --dim 2, r_m = 12, 9 Profile 0,5289 bis 0,5295 im Abstand 7,5e-5)

- **Pole:** Pluecker-Newton konvergiert 9/9. Die Breite faellt V-foermig:
  - 4,5e-4 / 2,8e-4 / 1,5e-4 / 6,5e-5 / 1,4e-5
  - **2,6e-7 bei 0,529275**
  - 2,3e-5 / 8,1e-5 / 1,7e-4
- **Gamma aus der Flussbilanz** (direkter Eigenvektor, Krein-Norm) stimmt mit Gamma Newton auf 4 bis 5 Stellen ueberein,
  z. B. 4,5019e-4 / 4,5019e-4.
  - Die direkten Pole liegen hoechstens 7,7e-6 neben den Pluecker-Polen.
  - Nur 2/9 erfuellten die Toleranz 1e-14 in 10 Schritten.
- **Abstrahlamplitude A_out:**
  - Sie geht bei omega^2 = 0,5292675 auf d_min = 1,26e-6 an den Nullpunkt heran. |A'| = 55,7, also
    d_min/|A'| = 2,3e-8 in Einheiten von omega^2.
  - Die Phase springt um pi + 0,12. Das ist die Signatur einer stillen Stelle wie bei den 3D-Sprossen.
- **s(x) auf dem feinen W-Gitter** (rho-Abstand 3e-5 bis 7e-4 um 1,557):
  - +2,20e-5 / +1,65e-5 / +1,12e-5 / +6,03e-6 / **+1,02e-6 (0,5292) / -3,84e-6 (0,529275)** / -8,54e-6 / -1,31e-5 /
    -1,75e-5
  - Hier wechselt s das Vorzeichen, linear bei 0,52922. Die Unsicherheit betraegt etwa +-8e-5, wegen der Interpolation
    ueber bis zu 7e-4 in rho.
- **Linearer Fit von W:** cond J = 3,3e4, Fitrest 1,3e-3, Mitte ausserhalb (0,53009). Er ist unbrauchbar, weil die
  Gradienten von L(y_a) und L(y_b) fast parallel liegen.
- **Umlauf:**
  - dx = 3e-4: -1,0000, 159 Punkte, groesster Sprung 1,819 rad
  - dx = 1,5e-4: -1,0000, 146 Punkte, groesster Sprung 2,596 rad
  - Beide gelten nach dem Code als nicht aufgeloest.
- **Wo die Spruenge liegen** (nachtraeglich mit jq aus exakt.json gelesen):
  - Sie liegen genau dort, wo die Linie L(y_b) = 0 die rho-Seiten kreuzt, nach 8 Halbierungsrunden auf
    1,95e-7 breiten Stuecken.
  - Beispiel x = 0,5295: W = (-2,19e-5, -2,01e-5) -> (-1,20e-5, +2,23e-5). Re W behaelt das Vorzeichen, die Phase
    laeuft also eindeutig ueber die negative reelle Achse.
  - Links (x = 0,5289) ist Re W = +2,96e-5 -> +1,85e-5, die Phase laeuft durch 0.
  - Der Umlaufsinn ist so ablesbar. Formal aufgeloest ist das Rechteck aber nicht: Das ist meine Lesung nach dem
    Lauf, kein Vorab-Kriterium.

### 2d. FEIN (Zusatz, vorab festgelegt, nicht Teil der Scheiterregel; kurve r_m = 12, R = 31,48)

| omega^2 | s (kurve, grob) | Pol (Pluecker) | Wurzel aus der Breite, signiert |
|---|---|---|---|
| 0,52920 | -9,71e-5 | 1,5560674 - 1,426e-5 i | +3,776e-3 |
| 0,52925 | -9,96e-5 | 1,5563629 - 8,363e-7 i | +9,145e-4 |
| 0,52930 | -1,02e-4 | 1,5566575 - 3,739e-6 i | -1,934e-3 |
| 0,52935 | -1,05e-4 | 1,5569505 - 2,277e-5 i | -4,772e-3 |

- Die Steigungen sind -57,2 / -57,0 / -56,8 je Einheit omega^2. Die Nullstelle liegt bei **0,529266**, ein Sockel ist
  nicht zu sehen.
- Vorab erwartet: min |Im Pol| <= 3e-6 und eine Lage bei 0,52927 +- 1,5e-5. **Getroffen** mit 8,4e-7 und 0,529266.
- Das grobe s bleibt glatt negativ, wie erwartet.

## 3. Folgelaeufe (nachtraeglich festgelegt, Abschnitt 7 des Plans; aendern den Ausgang in Abschnitt 1 nicht)

Alle mit Code v1 (kurve) bzw. v2 (REC2), r_m = 12 und rho-Abtastung mit 4000 statt 400 Punkten (Abstand 3,6e-4).

### F8: n = 8 (0,5255 und 0,5260), .69 cpu2, 15:39:45 bis 15:42:38 UTC, rc = 0

| omega^2 | s grob (R11-f, 400 Punkte) | s fein (4000 Punkte) | Pol (Pluecker) |
|---|---|---|---|
| 0,5255 | -3,13e-5 | **-1,063e-5** | 1,5509714 - 4,173e-4 i |
| 0,5260 | -5,86e-5 | **+7,342e-6** | 1,5545425 - 2,484e-4 i |

- Mit der feinen Abtastung wechselt s das Vorzeichen. Die Verfeinerung (4 Stufen) laeuft auf diese Punkte:
  - 0,52579569: s = +5,4e-7, |Im Pol| 1,4e-6
  - 0,52578145: s = -1,9e-7, |Im Pol| **1,9e-8**
  - 0,52578654: s = +1,3e-7, |Im Pol| 2,6e-7
  - 0,52578445: s = +1,0e-7, |Im Pol| 1,3e-7
- s liegt dort an der Aufloesungsgrenze des Feinfensters (~1e-7). Aus der signierten Wurzel der Breite folgt
  **omega*^2_8 = 0,525780 +- 3e-6**, rho* = 1,55299.
- Vorab (Nachtrag): Lage 0,52578 +- 5e-5. **Getroffen.**
- Die V1-Vorhersage der R11-Karte (0,52578 +- 0,0003) und meine Schreibtischlesung (0,525782) treffen ebenfalls.
- Schritt in 1/eps von n = 7 (F7b, 0,5292654) nach n = 8: 38,790 - 34,170 = 4,620.

### F6: Kontrolle n = 6 (0,533 und 0,535) mit feiner Abtastung, .69 cpu3, bis 15:42:23 UTC, rc = 0

- s(0,533) = -9,657e-5 (grob -1,026e-4), s(0,535) = +1,701e-4 (grob +1,440e-4). Der Wechsel bleibt.
- Die Verfeinerung landet bei 0,5338457, |Im Pol| 8,0e-9. Mit dem groben Gitter waren es 0,5338453; das ist innerhalb
  der Aufloesung der Verfeinerung (s ~ 4e-8).
- Vorab: 0,5338453 +- 1e-5. **Getroffen.**
- Auch bei n = 6 verschiebt das grobe Gitter s um 6e-6 bis 3e-5. Dort ist s aber gross genug, dass der Wechsel bleibt.

### REC2: dasselbe Rechteck mit 20 statt 8 Halbierungsrunden (Code v2), .69 cpu4, 15:39:45 bis 15:43:50 UTC, rc = 0

| Rechteck | Punkte | Umlauf | groesster Sprung | aufgeloest | min \|W\| |
|---|---|---|---|---|---|
| dx = 3e-4, drho = 1,5e-3 | 178 | **-1,0000** | 0,292 rad | **ja** | 1,7e-5 |
| dx = 1,5e-4, drho = 1,5e-3 | 170 | **-1,0000** | 0,289 rad | **ja** | 5,8e-6 |

- Pole, A_out und s(x) sind identisch mit REC (gleiche Profile, gleiche Rechnung; nur die Halbierungsrunden sind mehr).
- Vorab (Nachtrag): beide aufgeloest, Umlauf -1. **Getroffen.**
- Damit ist das (b)-Kriterium "aufgeloestes Rechteck mit Umlauf +-1" erfuellt, aber nur in einem nachtraeglich
  festgelegten Lauf.
- Die Nullstelle von W liegt im kleineren Rechteck: 0,52905 bis 0,52935, rho 1,5555 bis 1,5585.

### F7b: n = 7 (0,5285 bis 0,5300) mit 4000 rho-Punkten, .69 cpu2, 15:42:41 bis 15:46:18 UTC, rc = 0

| omega^2 | s grob (RM9/12/15, 400 Punkte) | s fein (4000 Punkte) | rho_b fein | Pol (Pluecker, unveraendert) |
|---|---|---|---|---|
| 0,5285 | -6,99e-5 | **+4,303e-5** | 1,555701 | 1,5524035 - 1,972e-3 i |
| 0,5290 | -8,77e-5 | **+1,711e-5** | 1,556195 | 1,5548957 - 2,346e-4 i |
| 0,5295 | -1,127e-4 | **-1,813e-5** | 1,556687 | 1,5578110 - 1,743e-4 i |
| 0,5300 | -1,409e-4 | **-5,700e-5** | 1,557178 | 1,5602363 - 1,610e-3 i |

- Mit der feinen Abtastung wechselt s zwischen 0,5290 und 0,5295 das Vorzeichen, linear bei 0,52924 (rho* 1,55643).
- Die grobe Abtastung verschiebt s um -8e-5 bis -1,1e-4. Das ist mehr als s selbst; darum gab es dort keinen Wechsel.
- Vorab (Nachtrag): s(0,5290) +1e-5 bis +2e-5 und s(0,5295) -1e-5 bis -2e-5. **Getroffen** (+1,71e-5 / -1,81e-5).
- Verfeinerung:
  - 0,52924279: s = +1,7e-6, Pol 1,55632031 - 1,8e-6 i
  - 0,52926541: s = -1,7e-9, Pol 1,55645379 + 8,0e-10 i
  - 0,52926539: s = +1,5e-7, Pol 1,55645366 + 7,1e-10 i
  - Der Imaginaerteil liegt auf Rauschhoehe, mit Vorzeichen +.
  - **omega*^2_7 = 0,5292654 +- 2e-6, rho* = 1,556457.** Die Unsicherheit kommt aus dem s-Rauschen des
    Feinfensters, ~1,5e-7.
  - Unabhaengig davon: der A_out-Nulldurchgang in REC liegt bei 0,5292675, die FEIN-Wurzel bei 0,529266.
- Vorab (Nachtrag): Lage 0,52927 +- 3e-5, Breite < 1e-6. **Getroffen.**
- Schritte in 1/eps: n = 6 -> 7 4,624, n = 7 -> 8 4,620. Gegen R11-V2 [4,59; 4,65]: beide innerhalb.

## 4. Schreibtisch (PLAN.md Abschnitt 1, kurz)

- **Die 3D-Sprossen n = 11 bis 15 kamen aus `pole`** (Pluecker-Breitenminima, signierte Wurzel), nicht aus dem
  Vorzeichentest.
  - In den zehn pole_bericht.txt (RUNDE-09/daten-leiter/quellen-69/runde7-bic2/) steht kein Kernwachstum.
  - Die Schaetzung ueber r_m = 25 ergibt etwa 1e13; das ist nicht gemessen.
- **Der Vorzeichentest versagte in 3D ab n = 7:** Kernwachstum 1,1e7, "Zweigmischung"; bei n = 8 und 9 1,0e9, nicht
  entscheidbar (RUNDE-08.md Z. 275 bis 282; RUNDE-09.md Z. 139, 154).
  - Derselbe Code fand also bei vergleichbarem oder groesserem Kernzuwachs **keine** sauberen Vorzeichenwechsel. Das
    spricht nicht gegen (b).
- **Nachtraegliche Lesung der R11-Polbreiten mit der 3D-Methode** (vor allen Laeufen dieser Karte):
  - n = 7 bei 0,529269, Schritt 4,6202
  - n = 8 bei 0,525782 aus zwei Punkten, Schritt 4,6200
  - Beide liegen auf den V1-Vorhersagen der R11-Karte (0,52927 und 0,52578).

## 5. Vorab gegen Ausgang

| Vorab (PLAN.md, eingefroren 17:24:46) | Ausgang |
|---|---|
| Lesarten: (a) 0,35, (b) 0,65, davon "Genauigkeit, mit r_m beweglich" 0,15 | r_m bewegt nichts; die Ursache liegt im Verfahren (rho-Abtastung), nicht in der Rundung |
| P1 s r_m-invariant (>= 2 Stellen), negativ: 0,8 | getroffen (~3e-11 relativ) |
| P2 r_m = 12 reproduziert R11-d: 0,95 | getroffen (bitgleich) |
| P3 Kontrolle bleibt, Lage +-2e-5: 0,85 | getroffen (0,53384528386 bei allen r_m) |
| P4 Rechteck: Umlauf 0 aufgeloest 0,45 / +-1 aufgeloest 0,25 / nicht aufgeloest 0,30 | nicht aufgeloest, Umlauf -1 |
| P5 Ausloeschung < 1e8, erwartet 1e3 bis 1e6 | getroffen (1,2e3 bis 5,8e4) |
| Ausgang: (a) 0,45 / (b) 0,30 / unentschieden 0,25 | unentschieden |
| FEIN: min Breite <= 3e-6, Lage 0,52927 +- 1,5e-5 | getroffen (8,4e-7; 0,529266) |
| Nachtrag (17:39:25), F8: Wechsel, Lage 0,52578 +- 5e-5 (0,6) | getroffen (0,525780) |
| Nachtrag, F6: Wechsel bleibt, 0,5338453 +- 1e-5 | getroffen (0,5338457) |
| Nachtrag, REC2: beide aufgeloest, Umlauf -1 | getroffen (0,292 und 0,289 rad; -1, -1) |
| Nachtrag, F7: Wechsel 0,5290 bis 0,5295, Lage 0,52927 +- 3e-5, Breite < 1e-6 | getroffen (F7b: 0,5292654, Breite auf Rauschhoehe < 1e-9) |

## 6. Hashes (sha256)

- bic2_2d.py (Original, unveraendert, lokal G2-10 und .69 runde11-leiter2d): e5f035c994922d357f0307b1acfea3edae5305396eb94c5e303760f9d7dcd2e1
- bic2_2d_praez.py (v1, lokal = .69): 55f27ec8ae014f8f4db90346ef84355c668e0ca6a2b016385686f2f2908f3cfe
- bic2_2d_praez_v2.py (nachtraeglich, nur --u-runden): 042ba893129ac3971dc53bf2c42b313f95f35e0f420149b274b7fd6a5be4ef00
- bic2_2d_praez.diff: 4e7d1c58bb14f2c40e462adc919471f4738fbb71e3a8c04be0273b3b37feca0a; bic2_2d_praez_v2.diff: a040dfca97f493b675d3939e543dfed45022e19b1d947db01cdb4f210c9bdbb7
- PLAN.md.eingefroren-20261001-172446: 46b99f6b186a76efbe6298336a99bf571281c74f968a88f3a6ea93aadabb0a0c
- PLAN.md.nachtrag-eingefroren-20261001-173925: ab56a22aef6c83711054202bd9c317cf47787f371ba171f97fcc2e74e1d1f05a
- start.sh 354d5f9380e0065a242055ead4e3ffadb24a617869d75f85b7ffcd9d9b9771bc; start2.sh 2f460753f30d597e8bc3d80fe92229b53cc91ca6453f21fbf496312a66184d18
- Ausgaben (lokal in lauf-69/):
  - rm9/kurve.json 0f18277964c69e22332a2578da17b9fa290c8f2039fd1ef1552049f0f86e9eb7
  - rm12/kurve.json 4ab226754049d180bdc0865493068d731a083c18c11325216ae3ac6e02892a1e
  - rm15/kurve.json fe71887711721e586641bce15a57a4720470113370b67a1ecc456dbd1be7ecc5
  - rec/exakt.json 9896e0b9d073a8ee8ac0656df462de998cdcf7e6aa6eeb1033d791980fbddef8
  - fein/kurve.json 36cc881f1fd39ec3614772626f261c3613bf020e25af8ecc5cba40723e2b0427
  - Folgelaeufe:
    - f6/kurve.json e76a8e1a4790f69aa0c6d79aa9be696467683d905299a7c00d52034c19a5c59d
    - f8/kurve.json e16eb5066ccf97eb3bc51e8f7ec23b98ef2e64de48752fd4223c84f2e03efbaf
    - rec2/exakt.json 68f0d5b8980aceb5ac974190ef7ee5decdc7eddb176e81d721b7f3d89013009f
    - f7b/kurve.json f52e718a7eea44edc8a77c167db20072872a1f60bbdd63180613c1abe155eb9d
- Vergleich: R11-d kurve.json 2c99a0e123fe914ede2af6d0613b712bda3ae3d1706703d499cc6806d1177ab8 (unveraendert).

## 7. Ablauf, Fehler, Regelverstoesse (selbst angezeigt)

- **Lokal kein python/python3/awk.**
  - Lokal steht keine Physik-Umgebung bereit, deshalb lief auch der Rauchtest auf der .69, ueber kleintest.sh, mit
    --budget 100 bis 110.
  - Zur Auswertung habe ich lokal jq (Tabellen aus den JSON-Dateien) und bc (Nachrechnen der signierten Wurzeln)
    benutzt. Beide sind weder python noch awk; ich nenne sie, damit es offen liegt.
- **Rauchtest, drei Anlaeufe, alle auf der .69:**
  1. Beim ersten exakt-Start stand die Variable K wegen meines Shell-Fehlers nur in der Hintergrund-Subshell
     ("cpu2: command not found"). Es entstand kein Lauf. Die Meldung wurde vom zweiten Anlauf in RAUCH-exakt.log
     ueberschrieben.
  2. Im zweiten Anlauf liess die Vorgabe --reserve 90 bei --budget 100 nur ein Profil zu, es wurde also nichts geprueft.
  3. Erst der dritte Anlauf (RAUCH-exakt2.log, --reserve 10) lief durch. Der kurve-Rauchtest (RAUCH-kurve.log) wartete
     6 min auf die Spur cpu, die ein anderer Agent (quark2) belegte, und lief dann 18 s.
- **F7 aus dem Nachtrag:** Die Spur cpu war von einem anderen Agenten belegt (k3diag). Ich habe meinen eigenen
  wartenden flock-Aufruf beendet, bevor eine Unit startete (LAUF-F7.log, rc = 143, keine Rechnung). Dann habe ich ihn
  als F7b auf cpu2 hinter F8 neu eingereiht.
- **Nachtraeglich festgelegt:** Die Folgelaeufe (Abschnitt 3) und Code v2 habe ich erst nach Kenntnis von REC und FEIN
  beschlossen. Plan-Nachtrag und Vorhersagen standen vor diesen Laeufen und sind eingefroren. Der Ausgang nach der
  Scheiterregel (Abschnitt 1) bleibt davon unberuehrt.
- **Schaetzung:** Die 3D-Kernwachstumszahl 1e13 ist geschaetzt, nicht gemessen.
- **Ablage:** Die Hintergrund-Wartebefehle des Werkzeugs haben ihre Ausgabe automatisch unter
  /tmp/claude-1000/.../tasks/ abgelegt. Das sind keine von mir angelegten Hilfsdateien. Alle meine Dateien liegen in
  RUNDE-12/leiter2d-praez/ (lokal) und in runde12-leiter2d-praez/ (.69).
- **Sonst:** kein git, kein Peerbus, keine Unteragenten, keine Dienste.
  - Die Starts liefen ueber kleintest.sh als einmalige Units. start.sh und start2.sh habe ich je einmal von Hand mit
    nohup gestartet.
  - Auf der .69 wurde nichts in place ueberschrieben; v2 und start2.sh liegen unter neuen Namen.
  - Nur die Spuren cpu, cpu2, cpu3, cpu4 und cpu6, jeder Aufruf unter 10 min Laufzeit.

## 8. Einfach gesagt

Wir wollten wissen, ob die Reihe der "stillen Stellen" in 2D nach Stufe 6 wirklich aufhoert oder ob das Programm sie
nur nicht mehr sieht. Das Verschieben des Anschlusspunkts aenderte die Ergebnisse nicht einmal in der zehnten Stelle;
an der Rechengenauigkeit liegt es also nicht. Der Fehler steckt in der Suchmethode: Sie tastet die Frequenz zu grob ab
und verbindet die Punkte mit geraden Linien, und bei den hoeheren Stufen ist dieser Linienfehler groesser als das
gesuchte Signal. Mit feinerer Abtastung und einem sauber aufgeloesten Rechteck tauchen Stufe 7 und 8 genau dort auf, wo
sie vorhergesagt waren. Nach der vorher festgelegten Regel heisst der Test trotzdem "unentschieden", weil das
entscheidende Rechteck erst in einem nachtraeglich beschlossenen Lauf aufgeloest war.

---
Letzte Aenderung dieser Datei: 2026-10-01 17:47:09 CEST (date). Zeitbox 60 min ab 17:12:18 eingehalten.
