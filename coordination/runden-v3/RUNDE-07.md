
Leitung: claude-primary. Angelegt: 2026-09-30 03:59:22 CEST (gemessen). Explorativ, keine formale Bestaetigung.
Finn: "weiter rechnen und ergebnisse melden" (03:58), "außerdem mal dem codex agent rein schauen" (03:59).

## Rahmen

- Karten, die in Runde 3 bis 6 "weiter" bekamen, plus Vorschlaege aus der M-Theorie- und der Video-Recherche.
- Fast Lane (Finn, 28.09.): mehr als fuenf Karten, weil sie unabhaengig sind und die Rechner frei werden. Jede Rechnung
  bleibt hoechstens 10 min.
- Rechenorte:
  - .69 ueber kleintest.sh: p4000a, p4000b, cpu, cpu2, cpu3, cpu4
  - Laptop-CPU fuer kleine Laeufe der Leitung
- Abstimmung mit Codex: Codex rechnet auf Finns Anfrage an Hierarchien langlebiger Speicher. Unsere Karten wiederholen
  das nicht; R-2 (dunkler Zustand zweier Baelle) ist an Codex weitergegeben.

## Karten

| Karte | Herkunft | Frage | wer |
|---|---|---|---|
| BIC-2 Exaktheit und Robustheit der Nullstelle | RUNDE-06 (omega*^2 = 0,79768; Codex Feshbach), V-1, MT-3 | (a) Ist die Breite exakt null? Test ueber die Phase bzw. Nullstelle der auslaufenden Amplitude, blind neben Codex. (b) Gibt es die Nullstelle auch fuer U = S - S^2 + beta S^3 mit anderem beta und fuer ein Affleck-Dine-artiges Log-Potential? (c) Nichtlineares Abklingen an omega* gegen eta | Anthropic-Agent, Code aus resonanz3d.py |
| R5F Folgen aus Runde 5 | Bio 4 Tod, Bio 3/36 Fuettern, Kavitation | (a) Ist der Rest unter Q_min ein Oszillon (Spektrum, Lebensdauer)? (b) Warum nimmt der grosse Ball unter der Schwelle Ladung auf? (c) Zerfaellt das dichte Kondensat bei S0 = 0,72 wirklich (Delle, Aufloesung, Box)? | Anthropic-Agent, Codes r5a.py und r5b.py |
| RING Wirbelball aus einem Ring | 2D-B ringe (N6/N8 mitdrehend verschmelzen zu einem Klumpen mit Windung 1; J/Q 1,03 bis 1,04 sind Startwerte, J faellt um 11 bis 12 %, J/Q am Ende nicht im Bericht), 2D-A Vierer-Ring | Entsteht ein stabiler drehender Ball mit Windung 1 (Windungszahl, Profilvergleich mit dem m = 1-Q-Ball)? Haelt der Vierer-Ring mit Windung 2pi/4 laenger? | Anthropic-Agent, Codes r5_2d_b.py und r5_2d_a.py |
| MT-1 Yukawa-Fingerabdruck | M-THEORIE-CALABI-YAU.md, V-2 | Staerke und Vorzeichen einer Sub-mm-Abweichung fuer KK-Turm (Glied 8), Stelle-Geist (Glied 10) und Skalar (Glied 5) auf Papier; Abgleich mit der Eoet-Wash-Schranke (Lee u. a. 2020) | Anthropic-Agent (Papier) |
| CEMZ-Gegenpruefung | VIDEO-6r1au5axOXM.md, Punkt 4 | Gilt die Kopplung der Glieder 7 und 10 ueber CEMZ nur ohne Geister? | Codex (Peerbus 225d6625), Berichtigung von WARUM-SPIN-2.md danach durch die Leitung |

Geparkt fuer spaeter: MT-2 (Zaehlt der Q-Ball-Ringturm wie ein String? Dispersion der Ringschwingungen).

## Tests: Ergebnisse

### MT-1 und V-3 (Papier, Feldforscher, 04:02:52 bis 04:25:28; RUNDE-07/PAPIER-MT1-V3.md)

- **MT-1, Yukawa-Fingerabdruck:**

  | Bild | Staerke und Form | heute erlaubt |
  |---|---|---|
  | KK-Turm (Glied 8) | alpha = +8n/3 je erster Stufe; Summe gleich starker Terme bei R, R/2, ... | R* < 30 um (Lee u. a. 2020) |
  | Stelle (Glied 10) | -4/3 (Spin-2-Geist) und +1/3 (Skalar), je eigene Reichweite; bei r -> 0 netto -1 | grob lambda2 < ~36 um, lambda0 < ~50 um; eine gemeinsame Auswertung fehlt |
  | Skalar (Glied 5) | ein Term, alpha > 0 (f(R): 1/3; Dilaton/Moduli groesser), oft materialabhaengig | lambda < 38,6 um bei alpha = 1 |

  - "2n statt 8n/3" ist nur halb richtig. 8n/3 mit vDVZ-Begruendung steht seit Adelberger, Heckel und Nelson 2003;
    2n gilt fuer ein masseloses Radion. Das ist also kein neuer Fund (Berichtigung in M-THEORIE-CALABI-YAU.md).
  - Die nach Vorzeichen getrennten Eoet-Wash-Kurven waren nicht abrufbar (HTTP 401). Heute ist nur die Reichweite
    begrenzt, kein Vorzeichen ausgeschlossen.
  - Der passende Test fuer ein materiegebundenes Medium waere die energieabhaengige Shapiro-Verzoegerung:
    Delta gamma < 2,1e-15 (Bartlett u. a. 2021).
  - Nebenbefund: Die LHAASO-Zahlen im Projekt (14,7e19 bzw. 12,0e11 GeV) stammen aus Yang, Bi und Yin 2024, nicht aus
    der Kollaborations-PRL. Berichtigt in LORENTZ.md und VIDEO-6r1au5axOXM.md (04:26:53). Der Abstract der PRL nennt
    "> 10 E_Pl"; von der Leitung selbst gelesen.

### BIC-2: Nullstellen der Atmungsbreite (Stand 2026-09-30 05:37:56 CEST, date)

Quellen:
- bic2.py v2 (exakt, kurve) auf der .69 (lauf-69/ bzw. runde7-bic2/) und auf dem Laptop (lauf-lokal/, als "Laptop"
  vermerkt)
- Codex bic-tail (TS440)

Belegstufen:
- **"exakt (Umlauf)"** heisst Umlaufzahl +-1 auf einem Rechteck um die Stelle, im radialen linearen Modell mit
  abgeschnittenem Rand. Das ist numerische Evidenz, kein Beweis. Den Beweis soll Karte BEWEIS-1 liefern.
- **"Vorzeichenwechsel"** heisst Wechsel der signierten Amplitude s in `kurve` mit Feinverfahren, Pol bei |Im| < 1e-8.

**beta = 0,5, Folge zur Duennwand-Grenze omega_min^2 = 0,5:**

| n | omega*^2 | rho* | 1/(omega*^2 - 0,5) | Schritt | Beleg |
|---|---|---|---|---|---|
| 1 | 0,797677 | 1,744618 | 3,359 | - | exakt (Umlauf -1), zwei Haeuser; Codex R = 44/56/68: 0,7976767871, Stufendifferenz < 7e-13 |
| 2 | 0,685129 | - | 5,402 | 2,042 | exakt (Umlauf +1) |
| 3 | 0,631449 | 1,652588 | 7,608 | 2,206 | exakt (Umlauf -1); kurve 05:25 bestaetigt 0,6314496 |
| 4 | 0,601422 | 1,628113 | 9,860 | 2,252 | exakt (Umlauf +1 auf beiden Rechtecken, .69, 05:44:22); zuerst Vorzeichenwechsel in zwei Scans (05:34, 05:36) |
| 5 | 0,582417 | 1,611309 | 12,133 | 2,273 | Vorzeichenwechsel (05:36); Umlauf -1 auf beiden Rechtecken, aber nicht aufgeloest (groesster Phasensprung 0,52 bis 0,54 rad, cond J 2,7e3; Laptop 05:47) |
| 6? | 0,5694 | 1,5992 | 14,41 | 2,28 | Kandidat: Feinverfahren lief aus dem Klammerintervall 0,570 bis 0,575 heraus, Pol noch -1,5e-7 i; nicht konvergiert |

- Der Schritt in 1/(omega*^2 - 0,5) waechst von 2,04 auf 2,27 und naehert sich etwa 2,28. Die Nullstellen haeufen sich also
  zur duennen Wand hin. Das passt zum Formfaktor- bzw. Phasenbild. Die Kennzahl ist abgeleitet (von Hand), nicht gemessen.
- Im Raster 0,555 bis 0,58 ist Gamma bei 0,560 klein (1,7e-5). Ein weiterer Kandidat (n = 7?) ist ungeprueft.
- Dort wechselt die Pol-Verfolgung vermutlich zwischen zwei Resonanzen; das Kernwachstum erreicht 9e6.

**Vorab gebundene Vorhersagen:**
- **Literatur-Agent** (L4-BIC-FAMILIE-LITERATUR.md, Ende 05:18:20, vor jedem Scan): Nullstellen bei ~0,634 (+-0,01),
  ~0,60 und ~0,58.
  - Die 0,634 war nachtraeglich: Der Kandidat 0,631 war bekannt, ging aber nicht in die Rechnung ein.
  - ~0,60 und ~0,58 trafen: 0,6014 und 0,5824.
- **Theorie-Agent** (THEORIE-ATMUNGS-NULLSTELLEN.md, V1, Abschnitt 5 ab 05:25:34; Datei zuletzt 05:32 geaendert; Kopie
  eingefroren 05:33, siehe unten): vierte Nullstelle bei 0,6018 +- 0,0006, Re rho* ~ 1,627, Umlauf +1.
  - Gefunden: 0,601421 und rho* = 1,628113.
  - Die Lage liegt im Fenster; die Widerlegungsgrenze war 0,6005 bis 0,6035. Die Umlaufzahl ist noch offen.
  - Zeitkette: Die ersten Scan-Berichte entstanden 05:33:03 und enthielten da nur Profile. Die Vorzeichenwechsel standen
    erst um 05:34:31 im Bericht.
  - Die eingefrorene Kopie ist RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md.eingefroren-20260930-053328 (cp -p, Dateizeit
    05:32 erhalten).
- V3, V4, V7 und V8 der Theorie laufen seit 05:36 auf der .69 (Kette M bzw. L). V6 (l = 1) ist noch nicht gestartet.
- **Ausgang der gebundenen Theorie-Tests** (Stand 05:43:41, date):

  | Test | vorab (eingefroren 05:32) | gefunden (.69, kurve h = 0,02) | Lage | Umlauf |
  |---|---|---|---|---|
  | V1, beta 0,5, n = 4 | 0,6018 +- 0,0006, Re rho ~ 1,627, Umlauf +1 | 0,601421, rho 1,628113 | getroffen | +1, getroffen (.69, 05:44:22) |
  | V3, beta 0,40, n = 2 | 0,5657 +- 0,002, Umlauf +1 | 0,566347, rho 1,583776 | getroffen | +1, getroffen (.69, 05:49:34) |
  | V3, beta 0,40, n = 3 | 0,5080 +- 0,001, Umlauf -1 | 0,508115, rho 1,535876 | getroffen | -1, getroffen (.69, 05:50:47) |
  | V3, beta 0,45, n = 3 | 0,5774 +- 0,0012, Umlauf -1 | 0,577365, rho 1,602162 (.69, 05:47:02) | getroffen | -1, getroffen (.69, 05:57:47, nach Rundenschluss, siehe RUNDE-08) |
  | V4, beta 0,5 | keine Nullstelle ueber 0,878; s bleibt 0,86 bis 0,96 negativ | s negativ an allen 11 Rasterpunkten 0,86 bis 0,96 (-7,2e-3 bis -4,0e-4) | bestanden auf dem Raster | - |
  | V8, ln(1 + S) | keine Nullstelle bei 0,10 bis 0,40 | kein Vorzeichenwechsel auf der verfolgten Spur (.69, 05:48:47). Bei 0,10 und 0,15 gibt es 2 bzw. 3 Kandidaten. Nach Zuordnung der Leitung (von Hand, nach Naehe zu 1 + omega) bleibt s auf der oberen Spur negativ (-9,1e-3 bis -3,0e-5) und auf der unteren positiv | bestanden auf dem Raster; Spurzuordnung bei 0,10 bis 0,15 von Hand | - |

  - V4 kann ein enges Nullstellenpaar zwischen zwei Rasterpunkten (Abstand 0,01) nicht ausschliessen. Oberhalb von
    0,96 ist nichts geprueft.
  - Die |s|-Werte, die die Theorie bei 0,86, 0,88 und 0,90 nannte, stammen aus frueheren Laeufen. Sie sind keine
    Vorhersage.
  - Laeufe nach der Vorhersage, alle ab 05:36:16.

**Andere beta (obere Familie und weitere):**

| beta | Stellen omega*^2 (Umlauf) | offen |
|---|---|---|
| 0,40 | 0,699702 (-1) | V3: 0,5657 und 0,5080 vorhergesagt |
| 0,45 | 0,755738 (-1, grosses Rechteck); 0,633380 (+1 auf beiden Rechtecken, neu zentriert, Laptop 05:43) | Erklaert (05:44): Das erste grosse Rechteck lag um x0 = 0,63267, die Stelle aber bei 0,63338, 7,1e-4 daneben bei halber Breite 5e-4. Die Stelle lag also ausserhalb; ein zweiter Nullpunkt ist nicht noetig |
| 0,55 | 0,674782 (-1, Laptop); 0,726130 (+1); 0,829984 (-1 auf beiden Rechtecken, neu zentriert, Laptop 05:39) | Erklaert: Das erste Rechteck um 0,8300 lag beim alten Keim 0,83052, 5,4e-4 daneben |
| 0,60 | 0,710164 (-1, Laptop); 0,759294 (+1 auf beiden Rechtecken, neu zentriert, Laptop 05:43); 0,855443 (-1, kleines Rechteck, Laptop) | Erklaert: Das erste Rechteck um 0,7593 lag bei x0 = 0,75873, 5,6e-4 neben der Stelle bei halber Breite 5e-4 |
| log | keine gesehen | V8 laeuft |

- Codex (TS440, BIC-TESTPAKET-ERGEBNIS.txt, 05:16):
  - Die nackte lineare Mode strahlt als endliche Anregung in der zweiten Harmonischen ab. Der Restfluss waechst wie
    epsilon^4.
  - Die Nullstelle ist also eine lineare Eigenschaft; eine nichtlineare periodische Fortsetzung ist weder gezeigt noch
    ausgeschlossen.

### BEWEIS-1 (seit 05:34)

- Auftrag: RUNDE-07/beweis/BRIEF.md.
- Ziel: rechnergestuetzter Beweis der Nullstelle n = 1 (beta = 0,5) mit Kugelarithmetik (python-flint auf der .69, seit
  05:32) und analytischen Schwanzlemmata.
- Bearbeiter: Anthropic-Agent; Plan zuerst, danach Code und Laeufe. Ein frischer Gegenleser liest den Plan.

### RING und R5F (Ernte ERGEBNISSE-R7-A.md, 04:59:51 bis 05:19:09)

- **RING-W:** Der Klumpen hat eine Zeit lang J/Q 0,96 bis 0,99 und ein m = 1-aehnliches Profil. Er zerfaellt in allen
  10 Laeufen. Die Zerfallszeit waechst mit ln(1/Saat). Die Windung waehrend der Klumpenphase steht nicht im Bericht.
- **RING-T:** Die Teilungsschwelle liegt bei omega^2 0,59 bis 0,60, nicht bei 0,60 bis 0,625.
- **RING-V:** Der Vierer-Ring haelt nur im erzwungenen C4-Sektor.
- **RING-K:** Die Ladungsbilanz reisst bei grossem Randverlust. Das ist laut PLAN ein Quadraturfehler der Verlustrate.
- **R5F-a:** Kein Oszillon unter Q_min gesehen (nur radiales Modell).
- **R5F-b:** Die Aufnahme unter der Schwelle ist linear und trifft den vorher bekannten Pol. Eine zweite, nicht
  vorhergesagte Spitze liegt bei nu 2,375 (omega^2 0,55).
- **R5F-c:** Die Energieregel trifft heilt/heilt nicht in 86 von 91 Laeufen. Die Box-Probe L = 400 lief um 04:59 noch.

### EVO-1 Generation 0 (zusammenfassen 03:36:17 UTC)

- Der Anker besteht: omega*^2 = 0,79755, Gamma(0,798) = 1,12e-7, F2 ja.
- Die Kontrolle dim = 1 ist "nicht entscheidbar". Das einzige grobe Minimum ist ein Rauschknick bei 0,8927, alle Breiten
  liegen unter etwa 2e-9.
- **A1 ist damit nicht bestanden.** Generation 1 startet nicht. Die Reparatur nach PLAN Zeile 62 (Aufloesungsboden,
  Abschnitt 11) wird vorbereitet und frisch gelesen, bevor sie wirkt.

### R5F-c Box-Probe (nachgetragen; Lauf endete 05:00:25, nach der Ernte um 04:59)

- Box L = 200 gegen L = 400: Die Klasse ist in 9 von 10 Laeufen gleich, in grob und fein.
- Die eine Abweichung betrifft die Unterklasse "zerfaellt"/"Kaverne" bei S0 = 0,72, tief. Das ist dieselbe
  Messzeit-Abhaengigkeit, die die Ernte schon nannte.
- Aufloesung: L3 grob gegen fein und fein gegen sehr fein ist in 10 von 10 Laeufen gleich.
- Heilt/heilt nicht ist in diesem Teil 7 von 7 getroffen (ohne "unklar").

## Abschaetzung

Leitung claude-primary, 2026-09-30 05:51:39 CEST (date, vor dem Schreiben). Noch laufende Tests gehen in Runde 8 ueber:
Umlauf bei beta = 0,45 (0,5774), V6 (l = 1) und V7 (1D).

| Karte | Entscheidung | Grund |
|---|---|---|
| BIC-2 Exaktheit und Robustheit | **weiter** (als BEWEIS-1 und BIC-3) | 16 Stellen mit Umlaufzahl +-1 bei 5 beta-Werten, 15 davon aufgeloest (0,5824 knapp nicht); alle frueheren "Umlauf 0" erklaert (Rechteck lag neben der Stelle). Folge zur Duennwand; vorab gebundene Theorie-Tests V1, V3 (drei Stellen), V4 und V8 bestanden. Nichtlinear strahlt die Mode in der zweiten Harmonischen (Codex) |
| R5F-a Tod unter Q_min | parken | kein Oszillon gesehen (nur radial); die v_g-Dauerformel verfehlt um mehr als Faktor 2 |
| R5F-b Fuettern unter der Schwelle | **weiter** | Aufnahme linear am vorher bekannten Pol; eine zweite, nicht vorhergesagte Spitze (nu 2,375 bei 0,55) ist ungeklaert |
| R5F-c Kavitation | parken, bestaetigt | Energieregel 86 von 91; Box und Aufloesung aendern die Klasse nicht (9-10 von 10); offen sind 5 Fehltreffer schmaler Dellen und die messzeitabhaengige Unterklasse |
| RING-W Wirbelball | parken | Klumpen mit J/Q 0,96 bis 0,99 zerfaellt in allen 10 Laeufen; Windung waehrend der Klumpenphase nicht gemessen |
| RING-T Teilungsschwelle | parken | Schwelle 0,59 bis 0,60 statt 0,60 bis 0,625 |
| RING-V Vierer-Ring | verwerfen (als gebundener Verband) | haelt nur im erzwungenen C4-Sektor |
| MT-1 Yukawa-Fingerabdruck | weiter als ST-1 | "8n/3" ist Literatur; offen ist eine gemeinsame Schranke fuer die zwei Stelle-Terme (Glied 10) |
| CEMZ-Gegenpruefung | erledigt | WARUM-SPIN-2.md berichtigt (Fassung 2, frisch gelesen); Journal #542 |

- Bilanz: 3 weiter (BIC-2, R5F-b, MT-1 als ST-1), 5 parken, 1 verwerfen, 1 erledigt.
- **Abweichung von v3:** Runde 7 hatte keine Zufallskarte. Runde 8 zieht wieder eine.
- **EVO-1:** A1 nicht bestanden; Reparatur (Abschnitt 12 des Plans) wird frisch gelesen.
- **Neue Idee aus arXiv** (Scout 03:07 UTC): Romanczukiewicz u. a., "Radiation damping of the soliton internal mode in 1D
  quadratic Klein-Gordon equation", Phys. Rev. E 114, 024213 (2026). Sie kommt als Literaturkarte in Runde 8.
- **Gesamtformel:** Der Kandidat (gesamtformel-20260921/KANDIDAT.md) benutzt genau U = S - S^2 + S^3/2. Die Nullstellen
  gelten damit fuer seinen einkomponentigen Ball.
  - Der Kopplungsterm g J_ab Re[(psi_a^* psi_b)^2] koppelt eine zweite Komponente bereits linear an sich selbst (Paarterm
    psi_1^2 psi_2^*).
  - Ob das neue Kanaele oeffnet, ist Karte GF-BIC in Runde 8.

## Einfach gesagt

Diese Runde hat vor allem eines gezeigt: Die stillen Stellen, an denen ein atmender Q-Ball keine Energie abstrahlt, sind
keine Zufallstreffer. Wir hatten vorher aufgeschrieben, wo die naechsten liegen muessen und in welche Richtung sie sich
drehen. Alle bisher geprueften Vorhersagen stimmten: Vier Stellen lagen im vorhergesagten Fenster, drei davon drehten sich
wie vorhergesagt, und wo keine Stelle sein sollte, war im Raster auch keine. Die Stellen werden zur duennen Wand hin immer
dichter, wie Sprossen einer Leiter. Andere Ideen dieser Runde, etwa der drehende Ringball, haben sich nicht gehalten. Als
Naechstes bauen wir einen strengen Beweis und pruefen, ob dasselbe auch in der Gesamtformel mit mehreren Feldern gilt.
