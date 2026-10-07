# SD-1: Pruefbelege fuer sd1.py (l = 0 wie GF-BIC, l-Verdrahtung wie SP-1, Kanal "anti" wie ROT-2)

- Geschrieben ab 2026-09-30 09:59:36 CEST (date).
- Code: RUNDE-09/sd1/sd1.py, Kopie von RUNDE-08/gf-bic/gfbic_umlauf.py (Fassung 2) mit --l, kurve, exakt, gebunden und
  Kanal "anti". Diff: sd1-gegen-gfbic_umlauf.diff.
- Auf der .69 liegt sie in /home/fmh/fmhc-physics-remote/runde9-sd1/, mit unveraenderten Kopien von bic2.py (Version 3,
  ee1ef6d2...), gfbic.py (cb62cdfd...) und resonanz3d.py (99c54b9c...).
- Die Originale von GF-BIC und ROT-2 sind nicht beruehrt.
- Fassungen von sd1.py (sha256, erste 16 Zeichen):
  - 0045cce6 (08:25): erste Fassung
  - ee06078d (08:26): Vorparser ohne "--h"-Hilfe-Abfang
  - 08f0d1aa: gebunden
  - b5000e3f (08:33): gebunden ohne Newton
  - e4b52881 (09:58): gebunden mit gemeinsamer Bisektion
  - Der Rechenweg von punkt ist in allen Fassungen derselbe.

## Q0: punkt bei l = 0 gibt R9-Z1 wieder (.69, cpu2, 06:31:23 bis 06:36:53 UTC; lauf-69/aus-q0-Z1)

- Argumente wie R9 (g = 0,2, h = 0,02, f_rand 1e-6, Offsets 0/+-5e-4/+-2e-3, Rechtecke 5e-4 und 1e-4, u_n 60).
- Bericht gegen RUNDE-08/gf-bic/lauf-69-r9/aus-Z1: Alle Rechenzeilen sind zeichengleich. Verschieden sind nur die
  Kopfzeile, die Profilzeit und die Endzeit.
  - zweiter Fit 0,711372079 / 1,6888288890 und 0,711372264 / 1,6888290010
  - Umlauf -1 / -1, Spruenge 0,294 / 0,290 rad
- JSON (ohne Zeiten, Pfade und neue Argumente): Die Umlauf-Eintraege und die Fit-Mittelpunkte sind gleich. 7 Zeilen
  weichen in den letzten Stellen ab: J, cond J, det J, fit_rest und drho aus lstsq. Das ist das Bibliotheksrauschen,
  das schon in SP-1 (PRUEFBELEGE P0b) zwischen zwei Laeufen derselben Fassung auftrat.
- Lokal (Rauchtest h = 0,08, 08:25): sd1.py rauch gegen gfbic_umlauf.py rauch, alle Rechenzeilen gleich.

## Q1 und Q2: die neuen Wege exakt und kurve bei l = 0 im psi_2-Kanal (.69, cpu)

| Groesse | R9 (gfbic_umlauf) | SD-1 | Abweichung |
|---|---|---|---|
| Z2 (g = 0,2), Nullstelle von W | 0,645861922 (Fit dx 1e-4) | exakt: 0,6458619287; A_out-Nullstelle 0,6458619647 | 7e-9 / 4e-8 |
| Z2 Umlauf | +1 / +1 | exakt: +1 / +1, Spruenge 0,135 / 0,134 rad (--u-n 3000) | gleich |
| Z2 aus kurve (Feinverfahren) | 0,645861922 | 0,6458619596 (s = -7e-11) | 4e-8 |
| Z1 aus kurve (Feinverfahren) | 0,711372264 | 0,7113722624 (s = -6e-12) | 2e-9 |

- Q1: exakt --kanal psi2 --g 0.2, h = 0,02, 06:46:59 bis 06:49:21 UTC (lauf-69/aus-q1-exakt-psi2-Z2).
- Q2: kurve --kanal psi2 --g 0.2, 0,63 bis 0,73, h = 0,02, 06:36:55 bis 06:42:58 UTC (lauf-69/aus-q2-kurve-psi2-l0).
- R8: Der Pol war zwischen 0,711 und 0,712 am schmalsten. Q2 zeigt dort 0,7100 mit Gamma 1,8e-8.

## Q3: l-Verdrahtung im psi_1-Kanal gegen SP-1 (.69, cpu2, 06:51 UTC; lauf-69/aus-q3-kurve-psi1-l1)

- kurve --kanal psi1 --l 1 bei 0,72 und 0,75, h = 0,01. Die Koeffizienten stammen hier aus sd1.k_psi1, in SP-1 aus
  bic2.pot_werte; algebraisch gleich, andere Rechenreihenfolge.

| omega^2 | SD-1 (psi1, l = 1) | SP-1 P1 (bic2 Version 3) |
|---|---|---|
| 0,72 | 1.7855450098975156 - 1.6980667732557795e-3 i | 1.7855450098975156 - 1.6980667732557414e-3 i |
| 0,75 | 1.8210850746516325 - 2.0369210732311268e-5 i | 1.8210850746516325 - 2.0369210732285193e-5 i |

- Re gleich auf alle Stellen, Im auf 4e-17. rho_b ist gleich; s weicht erst in der 16. Stelle ab.
- Rauchtest lokal (h = 0,08): kurve psi1 l = 1 ueber sd1 und ueber bic2 geben dieselben gedruckten Zahlen.

## Q5: Kanal "anti" gegen ROT-2 (gfbic_anti.py), l = 0, g = 0,05 (.69, cpu, 06:50 UTC; lauf-69/aus-q5-kurve-anti-g005-l0)

| omega^2 | SD-1 kurve --kanal anti --l 0 | ROT-2 anti_scan (runde9-rot2/aus-antiscan) |
|---|---|---|
| 0,70 | 1.6987914845278467 + 1.6658085455e-9 i | 1.6987914845278467 + 1.6658085558e-9 i |
| 0,72 | 1.720523181790384 - 3.6219883331e-8 i | 1.720523181790384 - 3.6219883339e-8 i |

- Re gleich auf alle Stellen, Im auf 1e-17. Das prueft natives Profil, Koeffizienten des Gegentakts und die Umleitung
  von bic2.lin_multi bzw. bic2.profil_pot.
- Nebenbei: Die l = 0-Gegenlaeufer-Nullstelle des Gegentakts bei g = 0,05 liegt laut kurve-Feinverfahren bei
  0,70225154 (s -> -7e-12). ROT-2 rechnet dort selbst; den Vergleich macht ROT-2 oder die Leitung.

## Rauchtests lokal (CPU, 1 Thread, nice 19, timeout 120; lauf-lokal/)

- 08:25:25 bis 08:25:59: rauch mit gfbic_umlauf.py und sd1.py, Berichte gleich (Q0 lokal)
- 08:26:43 bis 08:27:32: kurve psi1 l = 1, kurve psi2 l = 0, exakt psi2 l = 0
  - Der erste Versuch 08:26:09 endete ohne Ausgabe: Der Vorparser nahm "--h" als "--help".
  - Behoben mit add_help=False und allow_abbrev=False.
- nach der Freigabe:
  - 08:31:32 bis 08:32:15: gebunden und kurve anti l = 1
  - 08:33:27: gebunden ohne Newton
  - 09:58:25: gebunden mit gemeinsamer Bisektion, gleiche Nullstellen wie vorher
