# SP-1: Pruefbelege fuer bic2.py Version 3 (l = 0 unveraendert, l = 1 trifft V6)

- Geschrieben ab 2026-09-30 07:13:42 CEST (date). Code: RUNDE-07/bic2/bic2.py Version 3, SHA-256
  ee1ef6d226e8ec2c262e40a6d0e1b571a2a6fe40d334831f8e4ccb0856df12ce (lokal und auf der .69 gleich).
  Version 2 liegt daneben als bic2_v2.py (1f8affbd68b2...). Diff: sp1/bic2-v2-v3.diff.
- Einsetzen auf der .69: hochgeladen als bic2_v3_neu.py, dann `cp -p bic2.py bic2_v2.py` und `mv bic2_v3_neu.py bic2.py`
  (04:49:51 UTC = 06:49:51 CEST). Lokal ebenso per mv (06:49:46 CEST).

## P0: l = 0 bleibt im Rechenweg unveraendert

**P0a, .69 (Pflichtprobe):** kurve mit den Argumenten von RUNDE-07/bic2/lauf-69/aus-kurve-050-dicht (beta 0,5, xmin
0,555, xmax 0,645, dx 0,01, h 0,02; wegen --abstand 0,12 werden daraus 0,62 / 0,63 / 0,64, wie im Auftragsbeispiel
`--xmin 0.62 --xmax 0.64`). Lauf sp1p0, Spur cpu, 04:54:19 bis 04:56:39 UTC, rc = 0. Ausgabe
lauf-69/aus-sp1-p0-kurve-050-dicht/.

- Bericht: `diff` gegen die Referenz zeigt nur Zeile 1 (Startzeit) und Zeile 14 (Endzeit, 140.1 s gegen 140.7 s). Alle
  anderen 12 Zeilen sind zeichengleich, also alle Rechenzahlen: drei Kandidaten, drei Pole, Vorzeichenwechsel
  0.63132 / 1.65245, vier Feinschritte bis s = -7.937701231709915e-10 und Pol 1.65258826 + 3.144e-09 i.
- JSON: nach Entfernen von start, ende, sek und allen Schluesseln "sek...", sowie argumente.out, sind beide Dateien
  **bitgleich** (`cmp`; Zwischendateien lauf-69/p0-referenz-ohne-zeiten.json und p0-v3-ohne-zeiten.json). Das Feld
  argumente.l ist in beiden "0,1,2".

**P0b, lokal (Rauchtest rauch, h = 0,08; rechnet pole, bruecke, zeit, exakt, exakt G5 mit neu gelegtem Rechteck,
exakt ohne Fit, kurve poly und log, nlfit, alles mit l = 0).** CPU, 1 Thread, nice 19, timeout 120. Laeufe (Logs in
lauf-lokal/):

| Lauf | Version | Zeit (CEST) |
|---|---|---|
| rauch-v2 | 2 | 06:45:52 bis 06:47:25 |
| rauch-v3 | 3 | 06:45:55 bis 06:47:29 |
| rauch-v2b | 2 (Wiederholung) | 06:48:20 bis 06:50:04 |
| rauch-v3b | 3 (Wiederholung) | 06:53:08 bis 06:54:36 |

- Berichte: v2, v2b, v3 und v3b stimmen in allen Rechenzahlen ueberein. Verschieden sind nur Zeitangaben
  (Start, Ende, "je bis ... s", "Newton ... s", "Durchlauf ... s") und der Ordnername in der nlfit-Zeile.
- JSON (ohne Zeiten und Pfade, lauf-lokal/rauch-*-ohne-zeiten.json): v2 und v2b sind gleich. v3 und v3b weichen von v2
  und voneinander in je einem Block ab, und zwar nur in den letzten Stellen von Ergebnissen aus `torch.linalg.lstsq`:
  - v2 gegen v3: zweiter Fit des neu gelegten G5-Rechtecks (J, cond J, det J, drho), relativ <= 4e-16.
  - v3 gegen v3b: Polynomfit des Phasentests (c, abl, d_min), relativ <= 6e-13; derselbe Code in beiden Laeufen.
  - Deutung: lstsq ist hier von Lauf zu Lauf nicht bitgenau reproduzierbar. Der zweite Unterschied tritt zwischen zwei
    Laeufen derselben Version auf, ist also Rauschen der Bibliothek und keine Folge der Aenderung. Die Groesse passt zur
    Kondition der Polynommatrix (Spalten 1, 1e-4, 1e-8). Keine gedruckte Zahl aendert sich.
- Folgerung: Fuer l = 0 ist der Rechenweg unveraendert (nu = 0 + 1.0 = 1.0 an denselben Stellen). kurve benutzt kein
  lstsq, deshalb ist P0a bitgleich.

## P1: l = 1 trifft die V6-Pole

Lauf sp1p1 (Spur cpu, 05:12:08 bis 05:13:28 UTC, rc = 0): `kurve --l 1 --omega2-liste 0.72,0.75 --h 0.01`. Ausgabe
lauf-69/aus-sp1-p1-kurve-l1/. Vergleich mit den V6-Laeufen (pole, h = 0,01; runde7-bic2/aus-pole-l1 und
aus-pole-l1-0750 auf der .69), volle Stellen aus JSON:

| omega^2 | Pol kurve --l 1 (Version 3) | Pol V6 (pole, h = 0,01) | Abweichung |
|---|---|---|---|
| 0,72 | 1.7855450098975156 - 1.6980667732557414e-3 i | 1.7855450098975156 - 1.6980667732557429e-3 i | Re 0, Im 1,5e-18 |
| 0,75 | 1.8210850746516325 - 2.0369210732285193e-5 i | 1.8210850746516325 - 2.036921073225409e-5 i | Re 0, Im 3,1e-17 |

- Die Gitter sind verschieden (kurve: R = 35,68, r_m = 3,16, f_rand 1e-8; V6: R = 34,53 / r_m = 3,17 bei 0,72 und
  R = 26,46 / r_m = 2,76 / f_rand 1e-6 bei 0,75). Die Pole stimmen trotzdem auf alle Stellen in Re rho ueberein.
- Weitere Stimmigkeit fuer l = 1 (exakt, Lauf sp1a, h = 0,01):
  - direkter Pol gegen Pluecker-Pol: max 4,4e-9
  - Gamma_Fluss = Gamma_Newton auf 4 bis 5 Stellen (zum Beispiel 3.9107e-07 und 3.9107e-07)
  - sig_min/sig_2 <= 7,3e-15
  - Die Flussbilanz haengt am Fliehkraftterm in direkt_m; sie waere bei falschem l verletzt.
- Rauchtest l = 1 und l = 2 (lokal, h = 0,08, 06:48:26 bis 06:49:25; lauf-lokal/rauch-l1l2-v3.log) lief durch. Die
  falsche Eingabe `exakt --l 0,1` endet mit einer Meldung.
