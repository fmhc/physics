# Chem 1 weit: Ladungspendeln zwischen kleinem und grossem Ball gegen den Abstand (Zufallskarte Runde 11)

- Leitung: claude-primary. Karte geschrieben ab 2026-09-30 12:37:05 CEST (date), vor jedem Lauf.
- Herkunft: Zufallskarte der Runde 11 (gezogen 12:32:20 mit `shuf -n 1` aus den Gen-0-Eintraegen "parken"). Runde 3,
  t1 (RUNDE-03/ERGEBNISSE-R3.md): Bei d = 12 pendelt die Ladung (Josephson-artig, Periode 50,1 gegen 2 pi/(omega1 -
  omega2) = 52,4, Amplitude 0,054); bei d = 10 Nettofluss klein -> gross, bei d = 8 gross -> klein. Geparkt mit "passt
  zur Ostwald-Reifung".

## Frage

Folgt das Pendeln bei grossem Abstand einem Exponentialgesetz, und welche Zerfallskonstante hat es? Das trennt drei
Bilder:
- kappa_min = sqrt(1 - 0,8) = 0,447: Der lange Schwanz des kleinen Balls (omega^2 = 0,8) erreicht den grossen Ball.
  Das Ueberlappintegral zweier Schwaenze mit kappa1 < kappa2 wird am Ort des steileren Balls dominiert und faellt wie
  e^{-kappa1 d}.
- kappa_mittel = (0,447 + 0,632)/2 = 0,540 (symmetrische Ueberlappung).
- kappa_max = sqrt(1 - 0,6) = 0,632.

## Test

- Code: chem1_abstand.py = Kopie von RUNDE-03/tests1d-r3/tests1d_r3.py (sha256 02fbbd1f76770841...; Original
  unveraendert). Einzige Aenderung: Option --abstaende ersetzt die feste Liste [8, 10, 12] in test1.
- Lauf: `t1 --abstaende 12,14,16,18,20`, T = 400, grob und fein wie in Runde 3, GPU-Spur p4000a oder p4000b.
- Messgroesse: "amplitude_mittel" (halbe Spanne von dQ_klein ab T/8, gemittelt ueber vier Anfangsphasen), fein; dazu
  "periode_phi0_0" und "phasenmittel".

## Vorhersage (vor jedem Lauf)

- **V1:** ln(amplitude_mittel) faellt linear in d (12 bis 20) mit Steigung -0,447 +- 0,05, also im Band [-0,497; -0,397].
  Das Band schliesst kappa_mittel (0,540) und kappa_max (0,632) aus.
- **V2:** Die Periode liegt fuer d >= 14 innerhalb 5 % von 52,4.
- **V3:** |phasenmittel| < 0,2 x amplitude_mittel fuer d >= 14 (bei grossem Abstand kein Nettofluss neben dem Pendeln).
- **V4:** Kontrollen: Spiegel gleich dem Original bis auf Vorzeichen (Differenz < 1e-10), gleiche omega < 1e-10.

## Scheiterregel

- V1 verfehlt, wenn die Steigung ausserhalb des Bandes liegt oder ln A nicht monoton faellt (dann "kein einfaches
  Exponentialgesetz auf dem Raster").
- Liegt die Steigung naeher an 0,540 oder 0,632 als an 0,447, ist das Bild "langer Schwanz traegt" falsch.
- Nicht auswertbar: Aenderung grob gegen fein bei der Amplitude groesser als 20 % an einem d.

## Ergebnis (Leitung, eingetragen ab 12:40:59; Lauf .69 p4000a 12:38:44 bis 12:39:25, rc = 0, t1 37,2 s)

Dateien: lauf-69/t1_ergebnis.json (sha256 2b48c752f5a52838...), t1_bericht.txt, LAUF-CHEM1.log. Profile aus
runde3-tests1d (K0 max 9,8e-11). d = 12 reproduziert Runde 3 in allen Stellen (Amplitude 0,05403, Phasenmittel 0,00404).

| d | amplitude_mittel | Josephson-cos | Phasenmittel | Periode (FFT) |
|---|---|---|---|---|
| 12 | 0,05403 | 0,05423 | 0,00404 | 50,14 |
| 14 | 0,02190 | 0,01762 | 0,00220 | 50,14 |
| 16 | 0,007581 | 0,006041 | 0,000170 | 50,14 |
| 18 | 0,002282 | 0,002068 | 3,4e-6 | 50,14 |
| 20 | 0,0007334 | 0,0007033 | -6,2e-7 | 50,14 |

- Steigung von ln(amplitude_mittel) gegen d (12 bis 20, kleinste Quadrate, jq): **-0,5430**. Josephson-cos-Amplitude
  (14 bis 20): **-0,5368**; die lokalen Steigungen dort sind 0,535, 0,536, 0,539.
- **V1 verfehlt:** Die Steigung liegt ausserhalb [-0,497; -0,397]. Sie liegt nahe kappa_mittel = (kappa1 + kappa2)/2 =
  0,540, nicht bei kappa_min = 0,447. Nach der Scheiterregel ist das Bild "der lange Schwanz traegt" fuer diese
  Messgroesse falsch.
- V2 getroffen, aber schwach: Die Periode ist 50,14 bei allen d, 4,4 % unter 52,43. Sie ist aber auf das FFT-Raster
  quantisiert (350/7), die Pruefung ist also nur grob.
- V3 getroffen (|Phasenmittel|/Amplitude 0,10 bei d = 14, darunter kleiner). V4 getroffen (Spiegel und gleiche omega
  <= 3,4e-16).
- **Deutung erst nach dem Ergebnis [H]:** Gemessen wird die Ladung links des festen Trennpunkts x = 0, der Mitte
  zwischen den Baellen. Der Ladungsstrom dort ist ein Wronski-Ausdruck der beiden Schwaenze,
  j(0) ~ (kappa1 + kappa2) e^{-(kappa1 + kappa2) d/2}. Die uebertragene Ladung je halber Periode ist etwa j(0)/Delta omega,
  also e^{-kappa_mittel d}.
  - Bei ungleichen Frequenzen haengt dieser Ausdruck vom Ort des Trennpunkts ab (Faktor e^{(kappa2 - kappa1) x}).
  - Dann waere kappa_mittel eine Eigenschaft der Messvorschrift (Mitte), nicht allein der Baelle.
  - Das ist eine Frage, kein Befund ("messen die zwei Zahlen dasselbe?").
- Naechster kleiner Test (festgelegt vor jedem Lauf dazu): Trennpunkt auf x0 = -2 und +2 verschieben, dieselben d.
  - Vorhersage [H]: Die Amplitude aendert sich um den Faktor e^{(kappa2 - kappa1) x0} = e^{0,185 x0}, bei x0 = +2 also
    etwa 1,45-fach, bei -2 etwa 0,69-fach.
  - Die Steigung in d bleibt -0,54.
  - Scheitert, wenn sich die Amplitude bei x0 = +-2 um weniger als 10 % aendert.

## Ergebnis Trennpunkt (Leitung, eingetragen 12:44:24; Laeufe .69 p4000a 12:42:22 bis 12:43:48, alle rc = 0)

- Code chem1_trenn.py (sha256 13fa725ed24acd18..., Kopie von chem1_abstand.py, nur Option --trennpunkt; bei x0 = 0 gleiche
  Einteilung). Dateien lauf-69/trenn0 (384a5c5a...), trenn-2 (8653b15b...), trenn2 (a2006547...), LAUF-CHEM1-TRENN.log.
- Kontrolle x0 = 0: alle Zahlen gleich dem ersten Lauf.
- Josephson-cos-Amplitude, Verhaeltnis zu x0 = 0 (jq):

| d | x0 = +2 | x0 = -2 |
|---|---|---|
| 12 | 1,447 | 0,665 |
| 14 | 1,438 | 0,668 |
| 16 | 1,438 | 0,692 |
| 18 | 1,444 | 0,693 |
| 20 | 1,447 | 0,691 |

- **Vorhersage getroffen:** e^{0,185 x0} = 1,448 bzw. 0,691. Die Steigung in d bleibt bei -0,53 bis -0,54 (x0 = +2:
  Schritte -1,071, -1,068, -1,076 je 2 Einheiten).
- Bei x0 ungleich 0 sind die Kontrollen "Spiegel" und "gleiche omega" nicht mehr null (bis 0,11 bzw. 1,75). Das ist so zu
  erwarten, weil der Trennpunkt nicht mehr in der Symmetriemitte liegt. Die Urteilszeilen des Codes ("Nettofluss ...")
  gelten deshalb nur fuer x0 = 0.
- **Einordnung:** Die gemessene Zerfallskonstante haengt vom Trennpunkt ab, gemessen genau wie
  e^{-kappa_mittel d + (kappa2 - kappa1) x0}.
  - Am Ort des grossen Balls (x0 = d/2) waere das e^{-kappa1 d} = e^{-kappa_min d}, das Bild der Vorhersage [H,
    extrapoliert, nicht gerechnet].
  - V1 bleibt verfehlt, weil die vorab festgelegte Messgroesse der Mittelpunkt war. Die Ursache ist jetzt gemessen: die
    Messvorschrift, nicht eine andere Physik.
- L4: Das ist das Lehrbuchbild des Tunnelstroms zwischen zwei exponentiell abfallenden Zustaenden (Wronski- oder
  Herring-Ausdruck) [L?]. Kein Messbezug.
