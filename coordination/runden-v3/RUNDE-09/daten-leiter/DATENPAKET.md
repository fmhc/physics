# Datenpaket BIC-Leiter: stille Stellen der linearen Abstrahlungsbreite

- **Fuer:** Codex (ag-phy-coordination), Paperentwurf "A ladder of radiative cancellations in the breathing spectrum of
  three-dimensional Q-balls".
- **Ersteller:** Daten-Agent der Leitung claude-primary (Anthropic-Code-Agent).
- **Auftrag:** DATEN-LEITER, Leitung 2026-09-30 10:23:30 CEST.
- **Zeiten:**
  - JSON ab 10:32:36 CEST, Pruefdurchgang und Nachtrag 10:52:11 CEST.
  - Diese Fassung geschrieben ab 10:56:53 CEST (date vor dem Schreiben).
- **Maschinenlesbar:** DATENPAKET.json im selben Ordner.
  - 70 Zeilen, je Stelle eine, mit Pfaden (.69 und lokal), sha256 (16 Zeichen), Laufstart, Code-Fassung und
    Blindstatus.
  - Dazu Blindtest-Chronik, Luecken, Abweichungen und die Liste der nicht aufgenommenen Laeufe.
- **Evidenzregeln:** coordination/resonance-20260930/novelty-audit/PAPER-LEITER-EINARBEITUNG.txt.
  - Breitenminima werden nicht pauschal mit bewiesenen Stellen gleichgesetzt.
  - Jede Zeile traegt ihre eigene Klasse.
- **Nichts neu gerechnet:**
  - Keine neuen Laeufe.
  - Abgeleitet (von Hand mit bc, aus je drei Dateiwerten) sind nur die signierten Wurzeln fuer n = 7, 8, 9. Die
    Protokollwerte n = 11 bis 15 sind mit derselben Methode nachgerechnet.
  - Kopiert (nur IO) sind die .69-Ausgaben, die lokal fehlten, nach quellen-69/ (Abschnitt 7).
- **Modell:** Alles gilt im linearen, radialen Zweikanalmodell mit abgeschnittenem Rand. Das ist numerische Evidenz im
  Modell, keine Messung. Einzige Ausnahme ist n = 1 (Beweis).

## 1. Evidenzklassen und Zaehlung

| Klasse | Bedeutung | Zeilen |
|---|---|---|
| Beweis | rechnergestuetzter Existenzbeweis (BEWEIS-1), nur n = 1, l = 0, beta = 1/2 | 1 |
| Umlauf aufgeloest | Umlaufzahl +-1 auf mindestens einem Rechteck, das die Stelle enthaelt, groesster Phasensprung < 0,4 rad | 42 |
| Vorzeichenwechsel/Kurve | Wechsel von s mit Feinverfahren bis \|Im Pol\| < 1e-8, oder Wechsel des Ueberlappintegrals I (goldene Regel, g -> 0) auf feinem Raster | 14 |
| Breitenminimum | V-Minimum von \|Im rho\| auf drei Punkten, ohne Vorzeichen- oder Umlauftest; Lage aus der signierten Wurzel | 8 |
| interpoliert | Grobraster-Interpolation, Einbruch am Rasterrand oder Feinverfahren ohne \|Im Pol\| < 1e-8 | 5 |

- **Nur diese fuenf Klassen.**
  - Ist eine Umlaufzahl zwar +-1, aber nicht aufgeloest, steht die Stelle in der naechstschwaecheren erfuellten
    Klasse. Der Umlauf steht dann als Bemerkung.
  - Das betrifft zwei Stellen: beta 0,5 n = 5 und beta 0,35 n = 4.
- **Zeiten:** Im JSON stehen .69-Zeiten in UTC (CEST = UTC + 2 h). In dieser Datei steht alles in CEST.

## 2. Hauptleiter: Atmung, l = 0, beta = 1/2, psi_1 (u = 1/(x - 0,5))

| n | omega*^2 | Re rho* | Umlauf | Klasse | Lage aus | h | Lauf (.69 bzw. Laptop) | blind |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,797676787111865 (+-4,8e-22) | 1,744617544837399 | -1 | **Beweis**; numerisch zusaetzlich Umlauf aufgeloest bei h = 0,02 / 0,01 / 0,005 (Spruenge 0,288 / 0,274) | BEWEIS.md Z. 37, ZERT-B2-L44.json | Beweis; 0,005 | runde7-beweis; Laptop aus-exakt-0005, -001; .69 aus-exakt-002 | nein (Lage aus Runde 6) |
| 2 | 0,6851289 | 1,6903566 | +1 | Umlauf aufgeloest | A_out | 0,01 | Laptop aus-exakt-b050-0685 | nein |
| 3 | 0,6314496 | 1,6525880 | -1 | Umlauf aufgeloest | A_out | 0,01 | Laptop aus-exakt-b050-0631 | nein |
| 4 | 0,6014215 | 1,6281131 | +1 | Umlauf aufgeloest | A_out | 0,01 | .69 aus-exakt-b050-0601 | ja (V1) |
| 5 | 0,5824174 | 1,6113086 | -1, nicht aufgeloest (0,535 / 0,521 rad) | Vorzeichenwechsel/Kurve (\|Im Pol\| 1,3e-9) | kurve Fein | 0,02 (exakt 0,01) | .69 aus-kurve-050-b2dS2; Laptop aus-exakt-b050-0582 | grob (Literatur ~0,58) |
| 6 | 0,5693970 | 1,5991684 (rho_b) | - | interpoliert (Feinverfahren ohne \|Im Pol\| < 1e-8) | kurve Fein, letzter Schritt | 0,02 | Laptop aus-kurve-050-dw67; .69 aus-kurve-050-b2dS1 | nein |
| 7 | 0,5598497 (abgeleitet) | 1,5897567 | - | Breitenminimum (1,81e-6) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n7 | halb |
| 8 | 0,5526199 (abgeleitet) | 1,5826358 | - | Breitenminimum (4,66e-7) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n8 | ja |
| 9 | 0,5469426 (abgeleitet) | 1,5772052 | - | Breitenminimum (6,24e-6) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n9 | ja |
| 10 | 0,5424 (Formel) | 1,5723075 (rho_b bei 0,5425) | - | interpoliert (Einbruch 4,8e-5 am Rasterrand) | Leiterformel | 0,02 | .69 aus-kurve-050-dw89 | nein |
| 11 | 0,5386025 | 1,5688526 | - | Breitenminimum (3,69e-5) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n11 | ja (FORMEL-1) |
| 12 | 0,5354487 | 1,5647849 | - | Breitenminimum (3,90e-7) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n12 | ja (FORMEL-2) |
| 13 | 0,5327716 | 1,5618665 | - | Breitenminimum (9,0e-7) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n13 | ja (FORMEL-2, MOD-2) |
| 14 | 0,5304698 | 1,5594636 | - | Breitenminimum (Im +5,5e-10, Rauschhoehe) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n14a, -n14b | ja (FORMEL-3, MOD-2) |
| 15 | 0,5284695 | 1,5572734 | - | Breitenminimum (2,8e-9) | signierte Wurzel | 0,02 | .69 aus-pole-dw-n15a, -n15b | ja (FORMEL-3, MOD-2) |

- **Laufordner:**
  - .69-Ordner liegen unter runde7-bic2/, Laptop-Ordner unter RUNDE-07/bic2/lauf-lokal/.
  - Die pole-dw-Ausgaben n = 7, 8, 9, 11 bis 15 liegen als Kopie in quellen-69/runde7-bic2/.
- **Re rho* bei den Breitenminima:** Re des Pols am Rasterminimum, nicht an der abgeleiteten Lage.
- **n = 1, weitere Werte:**
  - A_out-Nullstelle: 0,7976767870619597 (h = 0,005), 0,7976767863636814 (0,01), 0,79767677525204 (0,02).
  - Codex, resonance-20260930/bic-tail/RESULT.json, R = 44 / 56 / 68: 0,7976767871112702 / ...109497 / ...108792.
- **Nachbarpunkte der Minima:** Abstand +-6e-4 bei n = 7, 8, 9, 11; +-1,5e-4 bei n = 12, 13; +-5e-5 bei n = 14, 15.
- **Signierte Wurzel:**
  - Das Vorzeichen der Mitte wird so gewaehlt, dass beide Steigungen von sqrt(\|Im\|) am besten gleich sind. Die Lage
    folgt dann aus linearer Interpolation.
  - Steigungen aus den Dateiwerten (bc):

    | n | Steigungen | Mitte |
    |---|---|---|
    | 7 | -27,7 / -27,1 | vor der Stelle |
    | 8 | -35,3 / -34,3 | vor der Stelle |
    | 9 | -43,5 / -42,1 | hinter der Stelle |
    | 11 | -62,3 / -60,0 | hinter der Stelle |
    | 12 | -72,2 / -71,4 | vor der Stelle |
    | 13 | -83,2 / -82,2 | vor der Stelle |
    | 14 | -93,9 / -94,1 | hinter der Stelle |
    | 15 | -105,8 / -106,0 | hinter der Stelle |

- **Schritte in u** (aus der Tabelle, bc):
  - n = 1 bis 5: 2,042 / 2,206 / 2,252 / 2,273.
  - n = 5 bis 9: 2,277 / 2,299 / 2,296 / 2,298.
  - n = 11 bis 15: 2,3047 / 2,3045 / 2,3052 / 2,3059.
  - Der Formelwert n = 10 gibt ungleichmaessige Schritte (2,282 / 2,320). Er ist kein Messpunkt.
  - Grenzschritt gemessen ~2,305, MOD-2 gab 2,298. Endliche Daten belegen keinen Grenzwertsatz.

## 3. Weitere beta (l = 0, psi_1, exakt h = 0,01)

| beta | n | omega*^2 | Re rho* | Umlauf | Klasse | Lauf | blind |
|---|---|---|---|---|---|---|---|
| 0,35 | 1 | 0,6218730 | 1,5986325 | -1 | Umlauf aufgeloest | .69 aus-exakt-b035-0622 | ja (BIC-3 b) |
| 0,35 | 2 | 0,4764570 | 1,4986943 | +1 | Umlauf aufgeloest (nur grosses Rechteck) | .69 aus-exakt-b035-0476 | ja |
| 0,35 | 3 | 0,4164540 | 1,4433227 | -1 | Umlauf aufgeloest | .69 aus-exakt-b035-0417 | ja |
| 0,35 | 4 | 0,3847511 | 1,4103618 (rho_b) | +1, nicht aufgeloest (1,47 / 1,72 rad) | Vorzeichenwechsel/Kurve (\|Im Pol\| 3,6e-10) | .69 aus-kurve-035-tief, aus-exakt-b035-0385 | ja |
| 0,40 | 1 | 0,6997021 | 1,6630410 | -1 | Umlauf aufgeloest | Laptop aus-exakt-b040-0700 | ja (verfehlt: 0,75 +- 0,03) |
| 0,40 | 2 | 0,5663469 | 1,5837764 | +1 | Umlauf aufgeloest | .69 aus-exakt-b040-0566 | ja (V3) |
| 0,40 | 3 | 0,5081148 | 1,5358759 | -1 | Umlauf aufgeloest | .69 aus-exakt-b040-0508 | ja (V3) |
| 0,45 | 1 | 0,7557378 | 1,7092901 | -1 | Umlauf aufgeloest (grosses Rechteck; kleines einseitig, ohne Stelle) | Laptop aus-exakt-b045-0756 | ja (PLAN B2) |
| 0,45 | 2 | 0,6333798 | 1,6444697 | +1 | Umlauf aufgeloest | Laptop aus-exakt-b045-0633-v2 | nein |
| 0,45 | 3 | 0,5773653 | 1,6021617 | -1 | Umlauf aufgeloest | .69 aus-exakt-b045-0577 | ja (V3) |
| 0,55 | 1 | 0,8299843 | 1,7727330 | -1 | Umlauf aufgeloest | Laptop aus-exakt-b055-0830-v2 | ja (PLAN B2) |
| 0,55 | 2 | 0,7261304 | 1,7263213 | +1 | Umlauf aufgeloest | .69 aus-exakt-b055-0726 | nein |
| 0,55 | 3 | **0,6747657** | 1,6923557 | -1 | Umlauf aufgeloest (neu gelegtes Rechteck) | Laptop aus-exakt-v2-b055-0673 | nein |
| 0,55 | 4 | 0,6456199 | 1,6697985 | +1 | Umlauf aufgeloest | .69 aus-exakt-b055-0646 | ja (BIC-3 b) |
| 0,55 | 5 | 0,6270422 | 1,6541302 | -1 | Umlauf aufgeloest | .69 aus-exakt-b055-0627 | ja (BIC-3 b) |
| 0,60 | 1 | **0,8554449** | 1,7957834 | -1 | Umlauf aufgeloest (nur kleines, neu gelegtes Rechteck) | Laptop aus-exakt-b060-0856-v2 | ja (PLAN B2) |
| 0,60 | 2 | 0,7592940 | 1,7552411 | +1 | Umlauf aufgeloest | Laptop aus-exakt-b060-0759-v2 | nein |
| 0,60 | 3 | 0,7101638 | 1,7245177 | -1 | Umlauf aufgeloest (nur grosses Rechteck) | Laptop aus-exakt-v2-b060-0710 | nein |
| 0,60 | 4 | 0,6819156 | 1,7036265 | +1 | Umlauf aufgeloest | .69 aus-exakt-b060-0682 | ja (BIC-3 b) |
| 0,60 | 5 | 0,6637917 | 1,6889549 | -1 | Umlauf aufgeloest | .69 aus-exakt-b060-0664 | ja (BIC-3 b) |

- Fett: Diese Werte weichen vom Protokoll RUNDE-07.md ab (Abschnitt 8).
- Bei beta 0,5 gibt es oberhalb n = 1 keinen Vorzeichenwechsel auf dem Raster 0,86 bis 0,96 (V4). Fuer die anderen
  beta gilt "nicht gesehen" nur fuer die gerechneten Bereiche.

## 4. l > 0 und andere Kanaele (getrennte Erweiterungen)

**l = 1 und l = 2 (psi_1, beta = 1/2, SP-1; exakt h = 0,01, bic2 v3; Ordner .69 runde7-bic2/, lokal RUNDE-08/sp1/lauf-69/):**

| l | n | omega*^2 | Re rho* | Umlauf | Klasse | Lauf | blind |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 0,7544960 | 1,8263421 | -1 | Umlauf aufgeloest | aus-sp1-a2-exakt-l1-07545 | ja (V6, Minimum-Test) |
| 1 | 2 | 0,6602797 | 1,7173012 | +1 | Umlauf aufgeloest | aus-sp1-d-exakt-l1-0660 | ja (VORHERSAGEN-SP1) |
| 1 | 3 | 0,6171053 | 1,6660504 | -1 | Umlauf aufgeloest | aus-sp1-d-exakt-l1-0617 | ja (VORHERSAGEN-SP1) |
| 1 | 4 | 0,5922424 | 1,6362961 | +1 | Umlauf aufgeloest (--u-n 3000) | aus-sp1-d-exakt-l1-0592-un3000 | eigene Erwartung (sp1/PLAN.md) |
| 1 | 5 | 0,5760743 | 1,6168267 | -1 | Umlauf aufgeloest | aus-sp1-d-exakt-l1-0576 | sequentiell (Nachtrag 07:14:50, gemischt) |
| 1 | 6? | ~0,5648 | ~1,6032 | - | interpoliert (nicht konvergiert) | aus-sp1-b5-kurve-l1-tief | nein |
| 2 | k = 1 | 0,6439055 | 1,7620826 | +1 | Umlauf aufgeloest | aus-sp1-d-exakt-l2-0644 | ja (Lage verfehlt, nach Regel zulaessig) |
| 2 | k = 2 | 0,6069811 | 1,6940364 | -1 | Umlauf aufgeloest (--u-n 3000) | aus-sp1-d-exakt-l2-0607-un3000 | ja |
| 2 | k = 3 | 0,5853911 | 1,6553114 | +1 | Umlauf aufgeloest (--u-n 3000) | aus-sp1-d-exakt-l2-0585-un3000 | ja |

**Gemischter Ball, Gleichtakt (g = 0,2, beta_eff = 0,4535147):**

- n = 1 bei 0,7590814, rho 1,7120741, Umlauf -1, Klasse Umlauf aufgeloest (h = 0,02 und 0,01).
- Blind: VD4 sagte 0,7587 +- 0,001 voraus (Abstand +3,8e-4).
- Natives Profil (gfbic_umlauf) und Ein-Feld-bic2 bei beta_eff stimmen auf 1e-8 ueberein.
- Laeufe: runde9-gfbic2/aus-BG, aus-BG-h001, aus-beff, aus-beff-h001.

**Zweite Leiter psi_2 (Gegenlaeufer um den einkomponentigen Ball):**

| n | g -> 0 (Wechsel von I/A) | Raster | Klasse | endliches g | blind |
|---|---|---|---|---|---|
| 1 | 0,8653612 (dx 0,005; dx 0,01: 0,8657506) | hp 0,02 | Vorzeichenwechsel/Kurve | bei g = 0,2 nicht aufloesbar | g -> 0: Klasse (V6) |
| 2 | 0,7107303 (dx 0,005) | hp 0,02 | Vorzeichenwechsel/Kurve | Z1, g = 0,2: 0,7113723 / 1,6888290 / -1 (h 0,02 und 0,01); g = 0,1: 0,7108615 / 1,6867493 / -1 (nur h 0,02) | g -> 0: Klasse (V6); Z1 g = 0,2: Fenster aus R8; Z1 g = 0,1: ja (VE2) |
| 3 | 0,6456753 (dx 0,01) | hp 0,02 | Vorzeichenwechsel/Kurve | Z2, g = 0,2: 0,6458619 / 1,6103661 / +1 (h 0,02 und 0,01) | g -> 0: Klasse (V6); Z2: Fenster aus R8 |
| 4 | 0,6106080 (dx 0,01) | hp 0,02 | Vorzeichenwechsel/Kurve | - | Klasse (V6) |
| 5 | 0,5885198 (dx 0,01, knapp) | hp 0,02 | interpoliert | - | nein |
| 6 | 0,5743700 (dx 0,001) | hp 0,02 | Vorzeichenwechsel/Kurve | Pol-Einbruch bei g = 0,2: 6,8e-8 | ja (ZUS-10 Idee 1) |
| 7 | 0,5638841 (dx 0,001) | hp 0,02 | Vorzeichenwechsel/Kurve | Einbruch 7,2e-8 | ja |
| 8 | 0,5559798 (dx 0,001) | hp 0,02 | Vorzeichenwechsel/Kurve | Einbruch 1,2e-7 | ja |
| 9 | 0,5498118 (dx 0,001) | hp 0,02 | Vorzeichenwechsel/Kurve | Einbruch 1,4e-7; Z3, g = 0,4985: 0,5511558 / 1,5152569 / +1 (nur h 0,02, Duennwand) | g -> 0: ja (ZUS-10); Z3: ja (VC1) |

- Die Zeilen mit endlichem g (Z1, Z2, Z3) sind im JSON eigene Zeilen (G01 bis G04) mit Klasse Umlauf aufgeloest.
- SD-1 reproduziert Z1 und Z2 bei g = 0,2 mit dem bic2-Kanal (Probe Q2, kurve Fein: 0,7113723 und 0,6458620); gleiches Haus.
- Die R8-Rasterwerte 0,57524 und 0,56556 sind durch ZUS-10 nicht bestaetigt. 0,55116 war ein Interpolationsartefakt.

**Gegentakt des gemischten Balls (anti, gegenlaeufig, g = 0,2, SD-1; h = 0,02, sd1 e4b52881):**

| l | Zaehlung m | omega*^2 | Re nu* | Umlauf | Klasse | blind |
|---|---|---|---|---|---|---|
| 1 | 9 | 0,5050963 | 1,5878766 | -1 | Umlauf aufgeloest | nein |
| 1 | 8 | 0,5127061 | 1,5980313 | +1 | Umlauf aufgeloest | ja (0,515 +- 0,004) |
| 1 | 7 | 0,5227046 | 1,6116852 | -1 | Umlauf aufgeloest | ja (0,525 +- 0,004) |
| 1 | 6 | 0,5364362 | 1,6309642 | +1 | Umlauf aufgeloest | ja (0,539 +- 0,004) |
| 1 | 5 | 0,5565041 | 1,6599702 | -1 | Umlauf aufgeloest | nein (ueber der vorhergesagten Schwelle) |
| 1 | 4 | 0,5887158 | 1,7074843 | +1 | Umlauf aufgeloest | nein |
| 1 | 3 | 0,6493098 | 1,7925671 | -1 | Umlauf aufgeloest | nein |
| 0 | - | 0,5016474 / 0,5082423 / 0,6043769 | 1,5762892 / 1,5830030 / 1,6749390 | - | Vorzeichenwechsel/Kurve | nein |
| 0 | - | 0,51647 / 0,52757 / 0,54332 / 0,56664 | - | - | interpoliert | nein |

- **Zaehlung m:** stammt aus VORHERSAGEN-SD1 (k_a R ~ m pi). Sie ist eine Modellzaehlung, keine Messgroesse.
- **Existenzschwelle des l = 1-Asts:** abgeleitet [Hand] aus den gebunden-Laeufen w1 und w2 (RUNDE-09/sd1/ERGEBNIS.md).
  - g = 0,2: 0,6743 +- 0,0005.
  - g = 0,02: 0,742 +- 0,002.
- **Anti l = 0 bei g = 0,05:** 0,7022515 (kurve Fein, Probe Q5).
  - ROT-2 rechnet dort eigene Umlauftests. Sie sind nicht Teil dieses Pakets.

## 5. Blindtest-Chronik

Die Vorhersagezeit stammt aus der Einfrierkopie oder, wo keine existiert, aus der Datei selbst. Laufstart und Ergebnis
stammen aus dem JSON bzw. dem Kettenlog. Alle Zeiten CEST.

| Test | Vorhersage (Datei, Zeit) | Ziel | Laufstart | Ergebnisdatei | Ausgang |
|---|---|---|---|---|---|
| bic2 PLAN A2 | RUNDE-07/bic2/PLAN.md, 04:31:04 bis 04:42:32 (laut Datei, keine Kopie) | n = 1: 0,797690 +- 2e-5, rho 1,744623 +- 1,5e-5 | 04:43:54 (Laptop), 04:43:56 (.69) | 04:47:46 / 04:48:08 / 04:49:51 | getroffen (-1,3e-5); Lage aus Runde 6 bekannt, nicht blind |
| bic2 PLAN B2 | wie A2 | n = 1 bei beta 0,40 / 0,45 / 0,55 / 0,60: 0,75 / 0,775 / 0,816 / 0,83 +- 0,03 | 04:43:54 bis 04:51:39 (kurve) | kurve 04:47:24 bis 04:59:15; exakt bis 05:39:44 | 3 von 4 (beta 0,40 verfehlt: 0,6997) |
| Theorie V1 | THEORIE-ATMUNGS-NULLSTELLEN.md, Ende 05:32:16, Kopie 05:33:28 | n = 4: 0,6018 +- 0,0006, +1 | 05:31:06 / 05:31:07 (1 min vor Schreibende) | kurve 05:34:31, 05:36:21; exakt 05:44:22 | getroffen (-3,8e-4, +1) |
| Theorie V3 | wie V1 | beta 0,40: 0,5657 +- 0,002 (+1), 0,5080 +- 0,001 (-1); beta 0,45: 0,5774 +- 0,0012 (-1) | 05:36:51 / 05:42:36 | 05:42:31 bis 05:57:47 | 3 von 3 Lagen, 3 von 3 Umlaeufe |
| Theorie V4 | wie V1 | keine Nullstelle ueber 0,878 | 05:36:19 | 05:41:48 | bestanden (Raster 0,86 bis 0,96) |
| Theorie V6 | wie V1 | l = 1 nahe 0,75 +- 0,02; Einbruch unter 1e-5 | 05:50:34 | 05:58:35 (0,74: 2,5e-4), 06:01:23 (0,75: 2,0e-5), 06:04:03 (0,755: 2,3e-7); exakt 07:14:34 | bestanden; exakt 0,754496, -1 |
| Literatur-Agent | L4-BIC-FAMILIE-LITERATUR.md, Ende 05:18:20 (laut Datei, keine Kopie) | ~0,634 +- 0,01 (Kandidat 0,631 lag vor), ~0,60, ~0,58 | 05:31:06 / 05:31:07 | 05:34:31 / 05:36:21 | ~0,60 und ~0,58 getroffen (ohne Balken); n = 3 nicht blind |
| BIC-3 (b) | VORHERSAGEN-BIC3.md, festgehalten 06:09:41, Kopie 06:10:07 | 8 Stellen bei beta 0,55 / 0,60 / 0,35 | 06:10:21 bis 06:10:24 | 06:13:37 bis 06:48:23 | 8 von 8 Lagen; 7 von 8 Umlaeufe aufgeloest und getroffen, die achte richtig, aber nicht aufgeloest |
| SP-1, Vorhersage | VORHERSAGEN-SP1.md, Kopie 06:43:17 | l = 1 n = 2, 3; l = 2 m = 2, 3, 4 | 06:52:22 | 06:56:27 bis 08:03:35 | 4 von 5 Lagen, 5 von 5 Umlaeufe; die verfehlte Lage (l = 2, m = 2) war nach Regel zulaessig |
| SP-1, eigene Erwartung | RUNDE-08/sp1/PLAN.md 06:42:28, Nachtraege 07:14:50 und 07:26:25 (keine Kopie) | E1 bis E5 | 06:52:22 | wie oben | E1-Lage verfehlt (0,754496 statt 0,7557); Nachtrag 07:14:50 gemischt; "danach 0,714" verfehlt; sonst getroffen |
| BIC-3 (c) | RUNDE-08.md, Eintrag 06:52:42 (keine Kopie) | n = 6 (nicht blind), 7 (halb), 8, 9 (blind), Schritt 2,29 +- 0,03 | 06:52:59 (Laptop), 06:56:42 (.69) | 06:54:48 / 06:59:15 | n = 6 vereinbar; n = 7 kein Vorzeichenwechsel; n = 8, 9 nicht entscheidbar (Kernwachstum 1,0e9 > 1e8) |
| BIC-4 | Lagen aus BIC-3 (c); Methode (pole) erst danach gewaehlt | Breitenminimum n = 7, 8, 9 | 07:02:23 (n8), 07:14:37 (n7), 07:28:47 (n9) | 07:06:35 / 07:18:32 / 07:32:41 | Minima im Balken: +1,0e-5 / -1,0e-5 / -2,7e-5; ohne Umlauf |
| GF-BIC V6 | gf-bic/PLAN.md, Kopie 06:14:34 | mindestens zwei Wechsel von I in (0,52; 0,98) | 06:30:07 | 06:39:14 | acht Wechsel (vier gut aufgeloest), getroffen, wo pruefbar |
| GF-BIC VC1 | Nachtrag C, Kopie 06:40:19 | Minimum < 1e-9 bei g* = 0,50 +- 0,03 | eingereiht 06:40:08, Python 06:44:10 | 06:46:56 | getroffen (g* ~ 0,4985) |
| GF-BIC-2 VD/VE | Nachtraege D 07:07:08 und E 07:24:37 (Kopien) | Umlauf Z1 bis Z3, BG; Z1 bei g = 0,1: 0,71089 +- 0,0002 | 07:14:00 bis 07:34:38 | bis 07:37:29 | 6 von 6; Fenster aus R8 eng, eigentliche Pruefung Umlauf und Codevergleich |
| FORMEL-1 | RUNDE-09.md, 07:57:22 (keine Kopie) | n = 11: 0,53867 +- 0,0003 | 08:07:36 (cpu2; 08:07:33 neu gestartet) | 08:11:47 | getroffen (-6,7e-5) |
| ZUS-10 Idee 1 | IDEEN-10.md, Kopie 08:06:53 | psi_2 n = 6 bis 9; Schritt 2,22 +- 0,02 | 08:22:19 / 08:29:49 / 08:56:46 | 08:29:29 / 08:37:17 / 09:05:18 | getroffen (+1,7e-4 bis +2,1e-4) |
| FORMEL-2 | RUNDE-09.md, 08:26:04 (keine Kopie) | n = 12: 0,53544; n = 13: 0,53276, je +- 0,00012 | 08:26:29 / 08:32:10 | 08:32:06 / 08:38:25 | getroffen (+8,7e-6 / +1,2e-5) |
| SD-1 | VORHERSAGEN-SD1.md, Kopie 08:28:19 | m = 6, 7, 8; Re nu*; Schwelle; g = 0,02 | 08:43:01 | 08:45:34 bis 10:10:26 | Lagen im Balken, Umlauf abwechselnd; Re nu*, Schwelle und g = 0,02 verfehlt; Regel 1a ausgeloest, 2b nach Wortlaut (Leitung entscheidet) |
| MOD-2 | VORHERSAGEN-MOD2.md, fertig 08:33:26, Kopie 08:33:57 | n = 10 bis 15 (Regel +-3 Balken) | n11 08:07:36, n12 08:26:29 (der Leitung bekannt, dem Agenten nicht); n13 08:32:10 (vor der Kopie); n14, n15 ab 08:38:30 | 08:11:47 bis 08:50:54 | n = 11 bis 15 getroffen (-1,6e-5 / -1,9e-5 / -2,0e-5 / -2,0e-5 / -1,9e-5); n = 10 nicht getestet |
| FORMEL-3 | RUNDE-09.md, 08:34:29 (keine Kopie) | n = 14: 0,530460 +- 4e-5; n = 15: 0,528458 +- 5e-5 | 08:38:30 / 08:45:08 | 08:45:04 / 08:50:54 | getroffen (+1,0e-5 / +1,2e-5) |

- **Fortschreibung:** FORMEL-1/2/3 wurden schrittweise fortgeschrieben (Anker n = 9, dann n = 11, dann n = 12). Das
  ist kein einzelner, unveraendert eingefrorener Fuenf-Punkte-Test.
- **Keine unabhaengigen Replikationen:** Formel und MOD-2 pruefen dieselben Zielrechnungen.
- **"Stets ~1e-5 zu tief":** gilt nur fuer n = 12 bis 15. FORMEL-1 lag bei n = 11 7e-5 zu hoch.
- **Methodenwahl BIC-4:** Die Polsuche wurde nach dem gescheiterten Vorzeichentest gewaehlt; die Lagen standen vorher
  fest.
- **Vorzeitige Starts:** Bei V1, VC1 und MOD-2 n = 13 lag der Laufstart vor dem Einfrieren. Die Ergebnisdatei kam
  jeweils danach.

## 6. Luecken

- **l = 0, beta = 1/2:**
  - n = 5: Umlauf nicht aufgeloest.
  - n = 6: Feinverfahren ohne \|Im Pol\| < 1e-8; zwei Laeufe liegen 1,8e-5 auseinander; kein Umlauf.
  - n = 7 bis 9: nur Breitenminimum auf drei Punkten, kein Umlauf.
    - kurve versagte bei n = 7 (Zweigmischung).
    - bei n = 8 und 9 war kurve nicht entscheidbar (Kernwachstum 1e9).
  - n = 10: nur ein Einbruch am Rasterrand (0,5425), nicht verfeinert.
    - Die Lage stammt aus der Formel.
    - Der MOD-2-Wert 0,542382 ist ungeprueft.
  - n = 11 bis 15: nur Breitenminima, Lage von Hand, ohne Umlauftest. n = 11 hat das flachste Minimum (3,7e-5).
  - n > 15: nicht gerechnet.
  - Ab n = 6 nur h = 0,02.
- **Weitere beta:**
  - beta 0,35, n = 4: Umlauf nicht aufgeloest.
  - beta 0,55, n = 6: nur s ~ 0 am Scanrand 0,6155, nicht gerechnet.
  - Nur ein Rechteck mit Umlauf: beta 0,35 n = 2, beta 0,45 n = 1, beta 0,60 n = 1 und n = 3.
- **l = 1:**
  - n = 6 (~0,5648) ist nur Kandidat.
  - Grobraster-Wechsel bei 0,5666 (b5) sowie 0,5742 und 0,5753 (b6) sind ungeklaert. Sie wurden erst nach dem Ausgang
    als Interpolationsfehler bzw. Kandidat n = 6 gedeutet.
- **l = 2:**
  - Bei 0,571 (Schrittregel) nicht gesehen (c0: 0,562 bis 0,58 ohne Wechsel); die Astverfolgung ist dort unsicher.
  - l >= 3 nicht gerechnet.
- **psi_2:**
  - n = 1 und n = 3 bis 9 nur in fuehrender Ordnung g -> 0 (hp 0,02, eine Stufe).
  - Umlauf nur fuer n = 2 (Z1), n = 3 (Z2) und n = 9 (Z3 bei g = 0,4985, nur h 0,02).
  - n = 5 nur grob.
  - n = 10 bei ~0,5448 (I/A = -0,085) nicht geprueft.
- **Gegentakt (SD-1):**
  - nur h = 0,02
  - zweiter l = 1-Ast unter 0,51 nicht untersucht
  - l = 0-Stellen ohne Umlauf, teils nur grob
  - bei g = 0,02 nur Grobraster (dx 0,02) ohne Wechsel, keine Stelle aufgeloest
  - Spin-Dipol nur als reelle Nullstelle von D belegt, ohne Konturzaehlung
- **Allgemein:**
  - Alles linear. Die nichtlineare Leckage ist nur fuer n = 1 gerechnet.
  - Zwei Haeuser rechneten nur bei n = 1.
  - Der Beweis wartet auf Fremdhauspruefung und ein zweites Programm.
  - Die bic2-Ausgaben tragen keinen Code-Hash; die Version ist aus Zeiten erschlossen.

## 7. Pruefvermerk: jede Zahl gegen die Ausgabedatei, in beide Richtungen

- **Protokoll -> Datei:**
  - Geprueft sind alle Lagen, Re rho, Breiten und Umlaufzahlen aus RUNDE-07/08/09.md (BIC-2/3/4, FORMEL-1/2/3,
    MOD-2-Vergleich, SP-1, GF-BIC-2, SD-1, ZUS-10 Idee 1).
  - Werkzeug: jq-Auszug aus allen exakt-, kurve-, pole-, umlauf-, ueberlapp- und gebunden-Dateien.
  - Ausnahmen stehen in Abschnitt 8.
- **Datei -> Protokoll:**
  - Alle Laufordner der fuenf Bereiche sind gegen die Zeilen abgeglichen (runde7-bic2, runde8-gfbic, runde9-gfbic2,
    runde9-zus10, runde9-sd1).
  - Scans mit Wechseln fuehren auf die Zeilen oben oder stehen in den Luecken: kurve-045-tief, q2, r2, s1 und die
    SP-1-Scans.
  - Ohne Stelle bzw. als Duplikat nicht aufgenommen:
    - Rauchtests
    - aus-exakt-g5 (Gegenprobe, Umlauf 0)
    - aus-exakt-b050-0629 (Vorlauf n = 3)
    - .69 aus-exakt-b055-0831 und -b060-0710 (v1-Duplikate)
    - kurve-log und -log-tief (Log-Potential, kein Wechsel)
    - kurve-050-barriere (V4, kein Wechsel)
    - nl-*, bruecke-*, fq-*, sp-P*, gem-*, kontrolle1, gscan-P4 (andere Fragen)
    - SD-1-Schwellenlaeufe und Scans ohne Wechsel (q3, r3, s3, u3, v3)
- **Pfade und Hashes:**
  - Alle 111 Dateiverweise im JSON zeigen auf vorhandene Dateien.
  - Die sha256 stimmen mit dem Paket ueberein (Nachpruefung 10:59:03).
- **Nur im Protokoll, in keiner Ausgabedatei:**
  - n = 10: Lage 0,5424 (Formel).
  - n = 7 bis 9 und n = 11 bis 15: Lagen aus der signierten Wurzel. Hier aus den Dateiwerten nachgerechnet und
    bestaetigt.
  - Die Schritte in u.
  - Die SD-1-Schwellen 0,6743 und 0,742 (Hand aus gebunden-Laeufen).
  - Die Z1-Kurve 0,710691 + 0,017 g^2.
  - Alle Vorhersagewerte.
- **Kopien:**
  - Die .69-Ausgaben aus-pole-dw-n7, n8, n9 und n11 bis n15 lagen lokal nicht vor. Der lokale Ordner zu n = 8 ist
    leer.
  - Sie liegen jetzt in RUNDE-09/daten-leiter/quellen-69/runde7-bic2/.
  - Ihre sha256 sind mit der .69 verglichen (quellen-69/SHA256-69.txt).

## 8. Abweichungen zwischen Protokoll und Datei

1. **beta 0,55, n = 3:**
   - RUNDE-07.md nennt 0,674782. Das ist der erste W-Fit, dessen Rechteck die Stelle nicht enthielt.
   - Die neu gelegten Fits (0,6747614 / 0,6747657) und kurve (0,6747658) geben 0,674766, also 1,6e-5 tiefer.
2. **beta 0,60, n = 1:** RUNDE-07.md nennt 0,855443 (erster W-Fit). A_out und der zweite Fit geben 0,855445 (1,9e-6).
3. **n = 11, Steigungen:** RUNDE-09.md nennt "-61 und -60". Aus den Dateiwerten folgen -62,3 und -60,0; die Lage
   stimmt.
4. **l = 1, n = 1:** RUNDE-08.md nannte "Minimum nahe 0,7554" (Handschaetzung). Die Datei gibt 0,754496; SP-1 hat das
   berichtigt.
5. **Z3:**
   - Der Protokollwert 0,5511558 ist der Fit mit dx 1e-4.
   - A_out (0,5511583) und der Fit mit dx 5e-4 (0,5511385) streuen bis 2e-5.
   - Grund: Duennwand, Fitrest so gross wie min \|W\|.
6. **MOD-2, n = 11:** RUNDE-09.md nennt -2,0e-5 (mit der gerundeten Lage ~0,53860). Mit der Lage aus den Dateiwerten
   (0,5386025) sind es -1,6e-5.
7. **Schritte in u, n = 12 bis 15:** RUNDE-09.md nennt 2,3043 / 2,3054 / 2,3055, gerechnet aus sechsstellig gerundeten
   Lagen. Aus den Dateiwerten folgen 2,3045 / 2,3052 / 2,3059. Die Rundung auf 1e-6 verschiebt u um bis zu 6e-4.
8. **ZUS-10 Polkontrolle:**
   - Die Einbrueche bei g = 0,2 stehen in den ueberlapp.json (Feld pole).
   - "2,7e-6 bis 7,2e-6 an den Nachbarn +-0,01" gilt nur fuer die aeusseren Nachbarn.
   - Zwei Nachbarn liegen nahe der naechsten Stelle: 0,564379 (4,9e-8) und 0,573922 (4,1e-7).
9. **n = 13, Startzeit:** Das Protokoll nennt 08:32:06; das ist der Kettenschritt. Der Python-Start in der Datei ist
   08:32:10.
10. **V6:** Der entscheidende Wert unter 1e-5 kam erst mit pole-l1-0755 (06:04:03, 2,3e-7). pole-l1 selbst rechnete
    nur 0,72 und 0,74.
11. **Bestaetigt, keine Abweichung:** Die Protokollangabe "Codex R = 44/56/68: 0,7976767871" steht in
    resonance-20260930/bic-tail/RESULT.json. Die groesste Differenz der drei R ist 3,9e-13.

## 9. Hinweise fuer das Paper

- **Figur 1:**
  - Evidenzklasse je Punkt als Symbol.
  - Breitenminima n = 7 bis 15 nicht als Nullstellen zeichnen.
  - n = 6 und n = 10 als "interpoliert" markieren.
- **Figur 2:** Fitpunkte und Vorhersagepunkte getrennt zeigen. FORMEL nutzte n <= 9 bzw. spaetere Anker, MOD-2 nutzte
  n = 5, 7, 8, 9.
- **Getrennte Erweiterungen:** l > 0, psi_2 und Gegentakt stehen getrennt; keine gemeinsame Zaehlung n ueber die
  Leitern.
- **Vorzeichen:** Umlaufzahl-Vorzeichen sind Orientierungen; +1 und -1 bedeuten beide "exakt" im Sinn der Klasse.
