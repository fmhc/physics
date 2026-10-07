# GPU-Z2-1: Ergebnis (Runde 49; GPU-Fassung der Spin-Schwellenrechnung, Barriere gegen R bei festem Kern r0 = 10)

- Code-Agent fuer die Leitung claude-primary. Synthetische Modellrechnung an einem Modellfeld (Einheitsquaternion-Feld,
  Energie 4(1 - c^2) je Bindung, Finns Diamant-Netz); keine Messung, keine Datenbestaetigung.
- **Auftrag geaendert** (Leitung, kurz nach meinem Start): keine Karte (kein Einfrieren, keine Urteile, kein frischer
  Leser); bauen, mit der CPU abgleichen, dann grosse Kugeln R = 40, 48, 64 (80, 96 wenn es geht) bei r0 = 10.
  KARTE.md bleibt liegen und ist nicht bindend; GZ0 bis GZ2 habe ich nicht beurteilt.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):** Start 2026-10-05 15:37:02 CEST. Rauchtest 0 (nur Technik) 13:41 UTC.
  Abgleich 13:50 bis 14:07 UTC. Grosse Kugeln 13:52 bis 15:07:54 UTC (letzte Unit). Text ab 16:45 CEST.
- **Kennzeichen:** [E] Rechnung im Modell; [M] Mathematik; [H] Hypothese, Deutung; [P] Projektdatei (Z2-SCHUTZ-2).

## Ergebnis zuerst

1. **GPU-Fassung steht und stimmt mit der CPU [E]:** torch 2.5.1+cu121 mit CUDA sieht beide P4000 (Rauchtest 0), alles
   in FP64. E_S und Bisektion bei (10, 20) gleich auf 1e-12 (25,028412468783 gegen 25,028412468784), CI-NEB auf 8e-6
   relativ. Gradient bei (10, 32) 12-mal (psi) bzw. 31-mal (Quaternion) schneller als die CPU; die ganze Bisektion
   (10, 32) 71 s statt 441 s; R = 64 (1,15 Mio. Knoten) mit einem ganzen Weg bis T in etwa 16 min.
2. **Barriere gegen R (hoechster Sattel des besten geschlossenen Weges) [E]:** 25,0 (R = 20), 45,6 (24, CPU), 74,6 (32),
   104,0 (40), 83,0 (48), 140,5 (64). R = 80: kein Weg bis T geschlossen (Austritt aus S 81,6 bzw. 129,8 je nach
   Kappe). R = 96: nur der Startzustand (E_S = 2677,18).
3. **Saettigung oder Wachstum: mit dieser Wegsuche nicht entschieden [E, H]:** Bis R = 64 waechst die Barriere
   insgesamt (Faktor 5,6 gegen R = 20), aber nicht monoton (R = 48 tiefer als R = 40), und zwei Kappenfamilien
   unterscheiden sich bei gleichem R um 9 bis 30 %. Die genauen Austrittssattel der 45-Grad-Familie steigen glatt
   (74,6 / 95,3 / 107,8 / 125,2 fuer R = 32 / 40 / 48 / 64) und passen nachtraeglich auf 175 - 3182/R, also auf eine
   Saettigung um 175 [H]; die vorher notierte Probe bei R = 80 (135 +- 5) fiel aus.
4. **Neu [E]:** Ab R = 40 fuehren die Wege ueber viele Zwischenminima (R = 64: 9 Sattel bis T; die offenen
   45-Grad-Wege sind nach 16 Sattel noch nicht bei T). Auf der 30-Grad-Familie
   ist der hoechste Sattel bei R = 40 und 64 nicht der Austritt aus S, sondern ein spaeterer Wachstumssattel (R = 64:
   Austritt 67,9, danach 140,5). Der CI-NEB mit 6 Bildern versagt auf diesen Wegen.
5. **Vorfall:** Meine Zwischenstaende haben die Platte der .69 gefuellt (100 %, belegt von 15:07:41 bis 15:08:10 UTC;
   der Beginn ist nicht genau bekannt, die letzte Pruefung um 14:33 UTC zeigte 17 GB frei). Drei eigene Units brachen
   ab ("No space left on device"); ob fremde Laeufe betroffen waren, weiss ich nicht. Zwischenstaende geloescht,
   danach 18 GB frei.

## Was gebaut ist (code/)

- **gz1.py:** Netz wie bisher auf der CPU (finn.Netz, unveraendert kopiert), dann alles auf der GPU in FP64 (torch
  2.5.1+cu121, eager, keine eigenen Kernel): Energie und Gradient in Quaternionen und in der ebenen Darstellung psi;
  Nachbarsummen ohne Atomics (je freiem Knoten die vier Bindungsenden als Indexliste, Gradient = Sammeln + Summe);
  FIRE als 1:1-Port von finn.fire_feld bzw. z2s2.fire_psi (ein Abgleich mit dem Wirt je Schritt); Bisektion als 1:1-Port
  von z2s2.modus_bisekt (Stufen 1, 2, 3, 3b, Klassen T, S, M, offen, Freigabe; gleiche Parameter); CI-NEB als Port von
  z2.wegrechnung mit allen Bildern in einem Tensor, hier in psi und ohne Rauschen aus der Ebene.
- **gz2.py:** gz1 plus Zwischenstaende: jede fertige Bahn liegt mit End- und Bestzustand auf der Platte; eine
  unterbrochene Bahn wird bitgleich fortgesetzt (p, v, dt, alpha, npos, Schritt, Bestzustand gesichert); so laeuft eine
  Rechnung in mehreren Units zu je hoechstens 540 s. Neu: **Folgemodus** (Weg ab einem Zwischenminimum bis T: je Stufe
  Bisektion in der Kappenfamilie psi_M (1 - lambda w) mit wachsendem Kappenwinkel, Nachschaerfen, Freigabe).
- **gz3.py:** gz2 mit zwei Korrekturen im Folgemodus (180-Grad-Kappe wird je Stufe mindestens einmal versucht; Folge ab
  Freigabe nur, wenn der Bisektionsweg geschlossen ist) und Fortsetzung eines Folgelaufs ab seinem letzten Ruhezustand.
- **Nicht gebaut:** Lanczos-Sattelpruefung (Hesse-Vektor-Produkte) und Hesse von S; nach der Auftragsaenderung
  zugunsten der grossen Kugeln weggelassen. Fuer R >= 40 ist S daher nur als Ruhezustand (Knotenkraft < 1e-7) geprueft.

## Abgleich mit der CPU (Z2-SCHUTZ-2) [E]

| Groesse | Wert | CPU (Z2-SCHUTZ-2) [P] | GPU | Abweichung |
|---|---|---|---|---|
| (10, 20), (10, 32) | Energie, Kraft an 3 Zufallszustaenden (Quaternion und psi) | numpy | torch FP64 | Energie gleich; Kraft <= 7,1e-15 bei Kraeften bis 15,9 |
| (10, 20) | E_S (FIRE bis 1e-7) | 4545,313250942401 (251 Schritte) | 4545,313250942401 (251) | 0 |
| (10, 32) | E_S | 3428,9017168539285 (347) | 3428,901716853929 (347) | 5e-13 |
| (10, 20) | Bisektion A | 25,028412468784154 | 25,028412468783245 | 9e-13 |
| (10, 20) | CI-NEB B auf dem eigenen Weg | 25,028557 (Quaternion, 74 It.) | 25,028346 (psi, 74 It.) | 8,4e-6 relativ |
| (10, 24) | CI-NEB auf dem CPU-Weg | 45,586078 (266 It.) | 45,585438 (237 It.) | 1,4e-5 relativ |
| (10, 32) | CI-NEB auf dem CPU-Weg | 76,781108 (238 It.) | 76,786348 (235 It.) | 6,8e-5 relativ |
| (8, 24) | CI-NEB auf dem CPU-Weg | 33,892561 (225 It.) | klettert nicht (6000 It.) | nicht abgeglichen |
| (10, 32) | Bisektion, Stufen 1 und 2 (Sattel 1) | 3481,9789904844974 | 3481,978990484497 | gleich |
| (10, 32) | Bisektion, Stufe 3 (Sattel 2) | +77,886 (Kraft 0,026) | +77,550 (Kraft 0,0012) | Bahnen laufen in Stufe 3 auseinander |

- **Lesart [E]:** Energie, Gradient, FIRE und die Bisektion bis Stufe 2 sind bis auf Rundung dieselbe Rechnung (gleiche
  Schrittzahlen, Barrieren auf 1e-12). In Stufe 3 bei (10, 32) laufen die Bahnen auseinander (Rundungsunterschiede in der
  Summenreihenfolge, an der Trennflaeche verstaerkt); die GPU trifft dort einen genaueren Sattel 2 (Kraft 0,0012 statt
  0,026). Die CI-NEB-Fassung in psi gibt auf denselben Anfangswegen die CPU-Werte auf hoechstens 7e-5 relativ wieder.
- **Barriere (10, 32):** GPU-Weg 77,55 (Bisektion und CI-NEB einig), CPU-Wert 76,78 (CI-NEB auf dem CPU-Weg, von der GPU
  auf 76,79 nachgerechnet). Beides sind Sattel auf verschiedenen Wegen; der Unterschied (1 %) ist Wegabhaengigkeit.

## Barriere gegen R bei r0 = 10 [E]

- **Verfahren:** Start S (FIRE bis Knotenkraft 1e-7), Bisektion A wie Z2-SCHUTZ-2 (Kappe um n_P, Kappenwinkel 30 Grad
  wie dort, oder 45 Grad als zweite Familie), danach Folgemodus ab dem Ruhezustand M nach Sattel 1, bis T erreicht ist.
  Barriere eines Weges = hoechster Sattel auf dem Weg minus E_S. "geschlossen" = der Weg erreicht T (E < 1e-3).
  "genau" = beide Klammerbahnen kommen dem Sattel bis Knotenkraft 0,05 nahe (Regel aus Z2-SCHUTZ-2).

| R | Knoten | E_S | 30 Grad: Austritt aus S | 30 Grad: hoechster Sattel des Weges | 45 Grad: Austritt aus S | 45 Grad: hoechster Sattel des Weges | bester geschlossener Weg | GPU-Zeit (s) |
|---|---|---|---|---|---|---|---|---|
| 20 | 38 893 | 4545,3133 | 25,03 | 25,03, geschlossen (CI-NEB 25,03) | - | - | **25,03** | 1 + 13 + 1 |
| 24 | 65 441 | 3976,5361 [P] | - | 45,59 [P] (CPU-Weg, GPU-CI-NEB 45,585) | - | - | **45,59** [P] | 2 (CI-NEB) |
| 32 | 150 713 | 3428,9017 | 53,08 (ungenau) | 77,55, geschlossen (Stufe 3, CI-NEB 77,55); Folge 79,67 | 74,58 (S-Seite Kraft 0,059) | 74,58, geschlossen | **74,6** (CPU-Weg: 76,78) | 2 + 71 + 36; 45 Grad: 55 + 21 |
| 40 | 288 701 | 3164,5170 | 50,91 | 104,03, geschlossen; Folge 104,27 | 95,33 | 95,33, offen (16 Sattel, Ende bei -9,1) | **104,0** | 3 + 84 + 43; 45 Grad: 74 + 37 + 75 |
| 48 | 492 621 | 3008,8423 | 83,01 | 83,01, geschlossen | 107,76 | 107,76 (dazu +128,2 ungenau), offen (Ende bei -21,0) | **83,0** | 6 + 104 + 49; 45 Grad: 169 + 52 + 88 |
| 64 | 1 149 801 | 2833,6474 | 67,94 | 140,51, geschlossen (9 Sattel) | 125,16 | 125,16 (dazu +190,6 ungenau, 180-Grad-Kappe), offen (Ende bei +84,4) | **140,5** | 18 + 365 + 350 + 211; 45 Grad: 382 + 116 + 326 |
| 80 | 2 226 313 | 2737,7720 | 81,61 (widerspruechlich) | Weg fuehrte zurueck nach S; ab S mit 90-Grad-Kappe 129,80 (genau), offen (Ende bei +124,1) | - | - | **keiner** | 13 + 784 + 502 + 1080 (Fortsetzung abgebrochen) |
| 96 | 3 822 269 | 2677,1828 | - | - | - | - | **keiner** | 42 (Start) + 1080 (Bisektion, 14 von etwa 59 Bahnen) |

- Alle Barrieren relativ zu E_S; Werte aus bisekt-, folge- und weg-*.json (lauf-69/). E_S fuer R <= 64 aus
  Quaternion-FIRE, fuer R = 80, 96 aus psi-FIRE. "offen" = Folgemodus erreichte T nicht (10 Stufen je Lauf).
- **Einordnung [E]:** Die genauen Sattel (beide Klammerbahnen <= 0,05) bestimmen jede Zeile; die spaeten Stufen sind
  meist ungenau, liegen aber ausser den gekennzeichneten Werten weit unter dem hoechsten genauen Sattel.

## Geschwindigkeit und Speicher [E]

| Groesse | Knoten | Gradient GPU: Quaternion / psi / psi 6 Bilder (ms) | Gradient CPU: Quaternion / psi (ms) | Faktor Quaternion / psi |
|---|---|---|---|---|
| (10, 20) | 38 893 | 0,70 / 0,86 / 2,37 | 16,9 / 2,73 | 24 / 3,2 |
| (10, 32) | 150 713 | 1,60 / 0,92 / 4,04 | 50,3 / 11,0 | 31 / 12 |

- Median ueber 50 (GPU, je mit Synchronisation) bzw. 5 Aufrufe (CPU, 1 Thread) in derselben Unit auf der .69
  (pruef-*.json). Bis etwa 300 000 Knoten bestimmen Startkosten der Kernel und Python die GPU-Zeit, nicht der Speicher.

| Lauf | CPU (Z2-SCHUTZ-2) [P] | GPU |
|---|---|---|
| Start S (10, 20), nur FIRE | 6,5 s | 1,0 s |
| Bisektion (10, 20) | 28,4 s | 13,1 s |
| CI-NEB (10, 20) | 17,1 s | 0,8 s |
| Start S (10, 32), nur FIRE | 36,9 s | 2,0 s |
| Bisektion (10, 32) | 441 s | 71 s |
| CI-NEB (10, 32), CPU-Weg | 220 s | 2,4 s |

| R | Knoten | Bindungen | FIRE-Schritt psi (ms, Bisektion mit allen Nebenkosten) | GPU-Speicher Spitze (MiB) |
|---|---|---|---|---|
| 20 | 38 893 | 75 360 | 2,1 | 12 |
| 32 | 150 713 | 295 504 | 2,1 | 55 |
| 40 | 288 701 | 568 268 | 2,4 | 106 |
| 48 | 492 621 | 972 196 | 3,4 | 182 |
| 64 | 1 149 801 | 2 276 428 | 8,5 | 424 |
| 80 | 2 226 313 | 4 416 848 | 14,1 | 814 |
| 96 | 3 822 269 | 7 593 260 | 57,6 (Startlauf) | 1191 (Startlauf) |

- **Hochrechnung [E, Kopfrechnung]:** ab 1 Mio. Knoten etwa 6 bis 7,5 ns je Knoten und FIRE-Schritt und etwa 380 Byte
  GPU-Speicher je Knoten. R = 96 lief mit 58 ms je Schritt mehr als doppelt so langsam wie hochgerechnet (24 bis 28 ms);
  auf der Karte waren dabei nur noch etwa 0,4 GB frei (nvidia-smi), vermutlich Speicherdruck [H]. Frei waren vor den
  Laeufen 2,35 GB (p4000a) bzw. 2,64 GB (p4000b), belegt von ruhenden Fremddiensten (nicht angefasst; die Belegung
  schwankte waehrend der Laeufe). Damit passen auf eine P4000 Kugeln bis etwa R = 100 (psi), auf die P5000 (heute etwa
  5 GB frei) bis etwa R = 130. Eine ganze Barrierenrechnung (Start, Bisektion, Folgestufen bis T) dauerte bei R = 64
  etwa 16 min GPU-Zeit, bei R = 80 mehr als 30 min.

## Was nicht geklappt hat

0. **Platte voll (Vorfall):** Die Zwischenstaende (je Bahn End- und Bestzustand, bei R = 80 etwa 36 MB je Bahn) der
   Laeufe R = 80 (Fortsetzung, zweiter Folgelauf) und der 45-Grad-Familie fuellten die Platte der .69 auf 100 %.
   Drei eigene Units brachen mit "No space left on device" ab (gz3f1080w3 bis 15:07:46, gz3f1080k1 15:07:41,
   gz3vb10801 15:07:54 UTC). Um 15:08:10 UTC habe ich alle eigenen Zwischenstandsordner geloescht (danach 18 GB frei).
   Wann die Platte voll wurde, weiss ich nicht genau (zuletzt geprueft 14:33 UTC mit 17 GB frei). Fremde Units, die
   heute fehlschlugen, endeten schon um 11:31 und 13:47 UTC, also vorher; ob laufende fremde Prozesse in dem Fenster
   nicht schreiben konnten, habe ich nicht geprueft.
1. **CI-NEB mit 6 Bildern ab R = 40:** Das Band rutscht in tiefere Zustaende (R = 40: alle Bilder unter E_S,
   "konvergiert ohne Klettern" nach 13 227 Iterationen; R = 48 und 64: Wandzeit, Kletterbild bei +29 000 bzw. +26 000).
   Grund [H]: Weg mit mehreren Zwischenminima, Endpunkt (Ende einer T-Bahn) ist kein Minimum, 6 Bilder zu wenig. Nicht
   verwendet; ab R = 40 zaehlen nur die Sattelnaeherungen der Bisektion und des Folgemodus.
2. **Stufe 3 der Bisektion ab R = 48:** Die untere Bahn endet in einem anderen Minimum als M ("Weg nicht
   geschlossen", wie (10, 28) in Z2-SCHUTZ-2). Deshalb der Folgemodus ab M (Ruhezustand nach Sattel 1).
3. **Folgemodus (gz2):** (a) Er kann rueckwaerts laufen: Bei R = 80 fuehrte die erste Folgestufe von M1 (+81,6) zurueck
   nach S, weil "T" dort nur "1 unter E(M_k)" heisst; die naechste Stufe startete dann von S mit 90-Grad-Kappe.
   (b) Er brach bei 180 Grad ab, ohne es zu versuchen (R = 64 und 80, 45-Grad-Familie): mit gz3 fortgesetzt.
   (c) "Folge ab Freigabe" pruefte nicht, ob der Bisektionsweg geschlossen ist (R = 64, R = 80 und 45-Grad-Familie bei
   R = 40, 48, 64 dadurch trivial "geschlossen"): ungueltig, nicht verwendet; in gz3 behoben.
   (d) Sattelnaeherungen spaeter Stufen sind oft ungenau (Kraft der oberen Bahn bis 0,9); sie liegen ausser einer
   Stufe (45 Grad, R = 48, 180-Grad-Kappe: +128,2 bei Kraeften 0,16 und 0,22, nicht verlaesslich) weit unter dem
   hoechsten genauen Sattel.
4. **Austritt R = 80 widerspruechlich:** Das Minimum M1 (+81,61) liegt hoeher als die Sattelnaeherung der S-Seite
   (+80,18, Kraft 0,0038); die Regel max(E oben, E unten) liefert damit E(M1). Die S-seitige Naeherung gehoert also zu
   einem anderen Sattel als dem vor M1.
5. **R = 96:** Startzustand fertig (E_S); die Bisektion lief 2 Units (14 von etwa 59 Bahnen, 58 ms je Schritt), dann
   habe ich die Kette wegen der Zeitbox beendet; ihr Zwischenstand ist mit dem Vorfall geloescht. Keine Barriere.
5b. **R = 80:** Die Fortsetzung des offenen Weges lief 2 Units und brach in der dritten ab (Platte voll); der zweite
   Folgelauf ab M1 mit 90-Grad-Kappe (Kette 11) und die 45-Grad-Bisektion (Kette 12) brachen ebenso ab. Kein
   geschlossener Weg fuer R = 80.
6. **CI-NEB auf dem CPU-Weg (8, 24)** klettert in psi nicht (Band rutscht ab); auf (10, 20), (10, 24), (10, 32) gelingt es.
7. **Keine Sattelpruefung (Lanczos) und keine Hesse von S fuer R >= 40;** alle Wege nur in der Ebene (psi). Bei R <= 32
   lagen die CPU-Sattel trotz Rauschen aus der Ebene in der Ebene [P]; fuer groessere R ungeprueft.

## Agenten-Vorhersage vor Kette 12 (notiert 2026-10-05 17:00:24 CEST per date, vor dem Lauf; kein Urteil)

- Die genauen Austrittssattel der 45-Grad-Familie (R = 32, 40, 48, 64: 74,58 / 95,33 / 107,76 / 125,16) liegen
  [Kopfrechnung, nachtraeglich angepasst] auf B(R) = 174,9 - 3182/R (aus R = 40 und 64; R = 32 und 48 je 0,9 darunter).
- **Vorhersage:** Kette 12 (Bisektion der 45-Grad-Familie bei R = 80) gibt einen Austrittssattel von 135 +- 5.
  Trifft das, stuetzt es eine Annaeherung an etwa 175 fuer R -> unendlich (fuer diesen einen Sattel, nicht fuer die
  kleinste Barriere) [H].

- **Ausgang:** nicht geprueft. Kette 12 brach nach 7 s ab, weil die Platte voll war (siehe Vorfall); danach keine
  Rechnung mehr in der Zeitbox.

## Bedeutung [H]

- **Zu Finns Frage (grosse Rechnung performant auf der GPU):** Die Rechnung ist durch den Speicher begrenzt; eine
  schlichte torch-Fassung (FP64, Indexlisten statt Atomics, Bilder in einem Tensor, ein Abgleich mit dem Wirt je
  Schritt) reicht fuer das 7- bis 30-Fache der CPU-Spur. R = 64 rechnet ein ganzer Weg in etwa 16 min; R = 80 bis 100
  passen in den Speicher einer P4000, brauchen aber mehrere Units (Zwischenstaende, gz2/gz3). Die Zwischenstaende
  muessen klein bleiben (nur die gerade noch gebrauchten Zustaende halten), sonst laeuft die Platte voll.
- **Zur Physik:** Bei festem Kern waechst die Barriere des Spin-Vorzeichens (360 -> 0 Grad) mit der Kugel mindestens
  bis R = 64 (auf 125 bis 141 je nach Weg); sie bleibt endlich [M: SO(3)^N zusammenhaengend]. Eine Saettigung ist zu
  erwarten, weil die Verdrillung am Kernrand fuer R -> unendlich endlich bleibt (g -> 2 pi / r0); die glatte Reihe der
  45-Grad-Austrittssattel passt dazu (Grenze um 175). Belegt ist sie nicht: Die Unsicherheit durch die Wegwahl (9 bis
  30 %) ist so gross wie der Schritt zwischen benachbarten R, und R = 80 und 96 fehlen.
- **Was fuer Z2-SCHUTZ-3 fehlt:** eine Wegsuche, die nicht an einer Kappenfamilie haengt (mehrere Keimorte und
  Kappenwinkel je R, oder ein String mit vielen Bildern, die auf der GPU jetzt billig sind), eine Sattelpruefung
  (Lanczos, auch aus der Ebene heraus) und sparsame Zwischenstaende. Dann R = 64 bis 96, am besten auf der P5000.

## Negativliste (darf aus diesem Befund nicht gesagt werden)

- "Die Barriere bei R = 64 ist 140,5" oder "die kleinste Barriere ist ...": Alle Werte sind hoechste Sattel einzelner
  gefundener Wege (ein Keimort n_P, zwei Kappenfamilien), also obere Schranken fuer diese Wege; ein anderer Weg kann
  tiefer liegen (bei R = 40, 48 und 64 unterscheiden sich die zwei Familien um 9 bis 30 %).
- "Die Barriere saettigt" oder "waechst wie R^p": Die Folge ist nicht monoton (R = 48 tiefer als R = 40 auf dem
  30-Grad-Weg), R = 80 ist offen, R = 96 fehlt. Kein Gesetz, keine Saettigung belegt.
- "Die GPU-Fassung gibt die CPU-Barrieren exakt wieder": exakt (1e-12) nur bis Stufe 2 der Bisektion; ab Stufe 3 und im
  CI-NEB auf 1e-5 bis 7e-5 relativ bzw. auf anderen Wegen andere Sattel.
- "S ist fuer R >= 40 ein echtes Minimum": nur Ruhezustand geprueft, keine Hesse.
- "Spin 1/2 ist im Modell geschuetzt" oder irgendeine Aussage ueber Messdaten. Synthetisch, keine Messung.

## Selbstanzeigen

0. **Platte der .69 gefuellt** (siehe "Was nicht geklappt hat", Punkt 0): Ich habe den Platzbedarf der Zwischenstaende
   (zwei volle Zustaende je Bahn, bei grossen R mehrere GB je Lauf, mehrere Laeufe zugleich) nicht begrenzt und die
   Platte nach 14:33 UTC nicht mehr geprueft. Die Leitung sollte pruefen, ob fremde Laeufe um 15:00 bis 15:08 UTC
   Schreibfehler hatten.
1. **Auftrag geaendert** (Leitung): kein PLAN.md, kein Einfrieren, keine Vorhersageurteile, kein frischer Leser. Der
   Rauchtest 0 (Technik) lief vor der Aenderung; danach sind alle Laeufe ausprobierend, keiner ist vorab festgelegt.
2. **Parameter abweichend von Z2-SCHUTZ-2:** Bisektion mit --nbis 4000 statt 1500 fuer R >= 40, alle Folgelaeufe und
   die 45-Grad-Familie (groessere Netze relaxieren langsamer); (10, 20) und (10, 32) mit 1500 wie die CPU.
   CI-NEB in psi ohne Rauschen aus der Ebene (CPU: Quaternionen, Rauschen 1e-3). Start S fuer R = 80, 96 in psi
   (S ist eben), fuer R <= 64 in Quaternionen wie die CPU.
3. **Zusaetze ohne Auftrag:** Folgemodus, zweite Kappenfamilie (45 Grad) und die Fortsetzungslaeufe, um die Wege bis T
   zu schliessen und die Wegabhaengigkeit zu sehen.
4. **Fehlstarts:** Kette 3 (p4000b) mit falscher Argumentform (--tag_zusatz -cpuweg) gab 36 Fehlstarts (rc = 2, je etwa
   3 s); ihre Logs teilen Namen mit den gueltigen Laeufen der Kette 4 (angehaengt). CI-NEB-Laeufe R = 40, 48, 64 mit
   nmax 20 000 (Voreinstellung) statt 6000: etwa 20 min GPU-Zeit fuer unbrauchbare Ergebnisse.
5. **Eingriffe auf der .69:** eigene Kettenskripte k5 (R = 96) und k9 (R = 80) per kill beendet (die laufende Unit lief
   jeweils bis zur Einheitsgrenze weiter); eigene Zwischenstandsordner mit rm -r geloescht (zuerst fertige Laeufe bei
   92 bis 94 % Belegung, um 15:08 UTC alle wegen voller Platte), Ergebnisdateien (json, npz) bleiben. Keine fremden
   Dienste angefasst, nichts installiert.
6. **Erster Kettenstart:** eine "&&"-Liste mit "&" in den Hintergrund gelegt; die zweite Kette startete erst beim
   zweiten Versuch (ohne Wirkung auf Ergebnisse).
7. **Lokal:** versehentlich eine leere Datei code/.leer angelegt und sofort geloescht. Eine Warteschleife lief laenger
   als 10 min; das Werkzeug legte sie in den Hintergrund und schrieb ihre Ausgabe in seinen Sitzungsordner unter
   /tmp/claude-1000/... (nicht von mir geschrieben).
8. **Kopfrechnung lokal:** Faktoren, Zeiten je Schritt, Byte je Knoten, relative Abweichungen, Hochrechnung; kein
   lokaler Interpreter. Energien relativ zu E_S stehen so in den JSON-Dateien (E_rel, E_M_rel, barriere).
9. **Werkzeuge:** lokal date, ls, mkdir, cp, mv, cat, sed, grep, head, tail, diff, chmod, sha256sum, scp, ssh, jq (nur
   Lesen), until-Schleifen mit sleep. Auf der .69 ausserhalb von kleintest.sh: mkdir, cat, ls, grep, jq (Lesen; jq -e
   als Bedingung in Kette 10), nvidia-smi, sha256sum, du, df, ps, kill (eigener Prozess), rm -r (eigene
   Zwischenstaende), setsid nohup bash fuer die Ketten. Python nur ueber kleintest.sh, nur Spuren p4000a und p4000b.
10. Kein Journaleintrag, kein Peerbus, kein Commit; das liegt bei der Leitung.

## Einfach gesagt

Wir haben das Rechenprogramm fuer die Spin-Schwelle auf die Grafikkarte gebracht; es rechnet dieselben Zahlen wie vorher
auf dem normalen Prozessor, nur 7- bis 30-mal schneller. Damit konnten wir die Kugel um den festen Kern bis Radius 64
(mehr als eine Million Netzpunkte) vergroessern. Die Huerde, die das Feld nehmen muss, um seine Verdrehung loszuwerden,
waechst von 25 bei Radius 20 auf etwa 125 bis 140 bei Radius 64, aber nicht gleichmaessig, und je nach gefundenem Weg
springt sie um bis zu ein Drittel. Ob sie irgendwann aufhoert zu wachsen, koennen wir deshalb noch nicht sagen; dafuer
braucht es eine bessere Wegsuche. Unterwegs habe ich mit Zwischendateien kurz die Festplatte des Rechners gefuellt; das
ist behoben, und alles hier ist eine Modellrechnung, keine Messung in der Natur.

## Dateien

- **Code (code/):** gz1.py, gz2.py, gz3.py (neu), rauch0.py (Rauchtest 0); finn.py, guertel2.py, guertel.py, stab.py,
  z2.py, z2s2.py unveraendert aus Z2-SCHUTZ-2 (Pruefsummen wie dort eingefroren). PRUEFSUMMEN-code.txt (lokal) und
  lauf-69/PRUEFSUMMEN-code-69.txt (.69) sind gleich; jede Ergebnis-JSON traegt code_sha256 im Kopf.
- **Ketten (ketten/):** k1 (Abgleich), k2 (R = 40, 48, 64 mit gz1), k3 (Fehlstarts), k4 (CI-NEB auf CPU-Wegen, Folge
  R = 32, 40, 48), k5 (Folge R = 64, R = 96; beendet), k6 (R = 80), k7 (45-Grad-Familie), k8 (Fortsetzung R = 64),
  k9 (R = 80 Fortsetzung; beendet), k10 (Fortsetzung 45-Grad-Familie), k11 (R = 80 zweiter Folgelauf; abgebrochen),
  k12 (45-Grad-Bisektion R = 80; abgebrochen).
- **Ergebnisse (lauf-69/):** abgleich/ (pruef-, start-, bisekt-, weg-*.json, weg-*-cpuweg.json, folge-r10-R32-M1.json,
  Logs), gross/ (start-, bisekt-, weg-, folge-*.json, *.stand.json, Logs, kette*.out), var45/ (45-Grad-Familie).
  rauch-69/: Rauchtest 0 (torch, Karte, Speicher) auf p4000a und p4000b. Die *-fr-Folgedateien mit offenem
  Bisektionsweg (R = 64, 80 und 45 Grad) sind ungueltig (Punkt 3c oben) und nur der Vollstaendigkeit halber da.
- **Nur auf der .69** (/home/fmh/fmhc-physics-remote/gpu-z2-1/lauf/, etwa 0,8 GB): die npz-Zustaende (S, Bisektionswege,
  Freigaben, Kletterbilder, Folge-Endzustaende); Pruefsummen in lauf-69/PRUEFSUMMEN-npz-69.txt.

## Gegenlesen und Zeitbox

- Kein frischer Leser (Leitung: nicht noetig nach der Auftragsaenderung); Zahlen aus den JSON-Dateien abgelesen.
- Zeitbox 150 min ab 15:37:02 CEST, also bis 18:07:02 CEST. Abgabe: 2026-10-05 17:12:50 CEST (date).
