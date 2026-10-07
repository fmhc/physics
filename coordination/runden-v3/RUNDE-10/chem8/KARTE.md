# Chem 8 dicht: Katalyse durch einen dritten Ball, dichtes v-Raster (Zufallskarte Runde 10)

- Leitung: claude-primary. Karte geschrieben ab 2026-09-30 12:13:56 CEST (date), vor jedem Lauf.
- Herkunft: Zufallskarte der Runde 10 (gezogen 10:26:26 mit `shuf -n 1` aus den Gen-0-Eintraegen "parken"). Runde 4 hatte
  Chemie 8 geparkt: "nur je ein v-Punkt knapp ueber der Schwelle, kein Klumpen nahe 2 Q0; kein tragender Katalyseeffekt"
  (RUNDE-04.md, Zeile 71). Naechster Schritt aus dem Parkgrund: dichteres v-Raster um die Schwelle.

## Bestand aus Runde 4 (RUNDE-04/ERGEBNISSE-R4.md 1.6, chemie-bio/lauf-69)

- 1D, omega^2 = 0,7, Q0 = 2,4415. A bei -12 (Phase 0, +v) gegen B bei +12 (Phase dphi, -v). C ruht bei 0 mit Phase
  dphi/2 ("bruecke") oder dphi/2 + pi ("sperre"); "nur_AC" ohne B; "ohne" ohne C. T = 300.
- "verschmolzen" = groesster Klumpen >= 1,5 Q0 im Mittel der letzten 50 Zeiteinheiten.
- Raster v = 0,05, 0,1, 0,15, 0,2, 0,3, ..., 0,6. Ergebnis fein:
  - dphi = pi: bruecke nur bei v = 0,15 (1,52 Q0); sperre gleich bruecke (Codeprobe); ohne und nur_AC nirgends.
  - dphi = 3pi/4: bruecke nur bei v = 0,1 (1,53 Q0); sperre und ohne und nur_AC nirgends.

## Frage

Ist die Verschmelzung mit Bruecke ein Fenster ueber mehrere v, das es ohne dritten Ball und mit C allein nicht gibt,
oder ein Einzelpunkt am Rand der Schwelle?

## Test

- Code: chem8_dicht.py = Kopie von RUNDE-04/chemie-bio/chemie_bio.py (sha256 6f6560be47e4d430...; Original bleibt
  unveraendert). Einzige Aenderung: Optionen --kat-v (Liste) und --kat-t, die KAT_V und KAT_T ersetzen.
- Lauf 1: v = 0,05 bis 0,25 in Schritten 0,01 (21 Werte), T = 300, grob (dx 0,1) und fein (dx 0,05) wie in Runde 4.
- Lauf 2 (Zeitprobe): dasselbe Raster mit T = 600. Zeigt, ob die Klumpen bis zum Ende halten.
- Spur p4000b (GPU), je Lauf unter 10 min (Runde 4: 64 Laeufe fein in 19,6 s).

## Vorhersage (Leitung, vor jedem Lauf; Zeit siehe Kopf)

- V1: Bruecke verschmilzt je dphi an 1 bis 3 benachbarten v-Punkten (ein schmales Fenster), bei dphi = pi um
  v = 0,13 bis 0,17, bei 3pi/4 um v = 0,08 bis 0,12.
- V2: Der groesste Klumpen bleibt unter 1,7 Q0 (keine echte Paarbildung nahe 2 Q0).
- V3: ohne und nur_AC verschmelzen bei keinem v des Rasters.
- V4: Mit T = 600 bleiben hoechstens die Haelfte der Fensterpunkte aus Lauf 1 "verschmolzen" (die Klumpen zerfallen
  langsam).

## Entscheidung (vorab festgelegt)

- **weiter**, wenn fuer ein dphi gilt:
  (a) bruecke verschmilzt an mindestens 3 benachbarten v-Punkten, grob und fein gleich,
  (b) ohne und nur_AC verschmelzen an keinem dieser Punkte,
  (c) mit T = 600 bleiben mindestens 2 dieser Punkte verschmolzen.
- **verwerfen**, wenn bruecke an hoechstens einem Punkt je dphi verschmilzt oder nur_AC dort ebenfalls verschmilzt.
- sonst **parken** mit Grund.
- Nebenlatte, nur berichtet: groesster Klumpen >= 1,8 Q0 (Paarbildung nahe 2 Q0) an irgendeinem Punkt.

## Ergebnis (Leitung, eingetragen ab 2026-09-30 12:18:46 CEST; Laeufe .69 p4000b 12:14:43 bis 12:17:55, rc = 0)

Dateien: lauf-69/t300/ (katalyse.json sha256 301354ca170738ba..., katalyse_bericht.txt), lauf-69/t600/ (katalyse.json
2524110d80941812...), LAUF-CHEM8.log, kette.sh. Code chem8_dicht.py sha256 b49075c729dc1d0f... (lokal = .69).

- **Lauf 1 (T = 300):** Muster grob = fein (168 von 168 Klassen gleich, L3 bestanden: Effekt 0,60 Q0 gegen Aenderung
  0,0028 Q0).
  - dphi = pi: bruecke (und sperre, Codeprobe gleich) verschmilzt bei v = 0,12 bis 0,17 (6 benachbarte Punkte), groesster
    Klumpen hoechstens 1,52 Q0.
  - dphi = 3pi/4: bruecke verschmilzt bei v = 0,06 bis 0,12 (7 Punkte), hoechstens 1,56 Q0 (v = 0,07 und 0,08).
  - ohne, nur_AC und sperre (3pi/4) verschmelzen bei keinem v; ohne bleibt bei 0,93 bis 1,02 Q0, nur_AC bei hoechstens
    1,33 Q0.
  - Die Groesse ist glatt in v: bruecke bei pi steigt von 1,18 (v = 0,05) auf 1,52 (v = 0,13 bis 0,15) und faellt auf 1,43
    (v = 0,25). Das "Fenster" ist der Teil einer glatten Kuppe ueber der Schwelle 1,5 Q0.
  - Die drei groessten Klumpen, z. B. pi bruecke v = 0,14: 1,52 / 0,71 / 0,44 Q0 (Summe 2,67 von 3 Q0). Es bilden sich
    also drei Klumpen mit umverteilter Ladung, keiner nahe 2 Q0.
- **Lauf 2 (T = 600):**
  - dphi = pi: kein Punkt mehr verschmolzen.
  - dphi = 3pi/4: bruecke bei v = 0,11 und 0,12 weiter verschmolzen (1,51 und 1,50 Q0).
  - Fuer v >= 0,11 bleibt ein Klumpen von 1,26 bis 1,51 Q0 im Messbereich, mit fast denselben Werten wie bei T = 300.
    Die kleineren Klumpen haben den Messbereich verlassen (v = 0,2: nur noch ein Klumpen, 1,37 Q0).
  - Grob = fein (168 von 168).
- **Fehlerkasten:** Der Messbereich ist |x| < 75 (Box 120 minus Schwamm 40 minus 5). Bis T = 600 verlassen schnelle
  Klumpen den Bereich. Der Wert 0,00 heisst dort "verlaesst den Messbereich", nicht "zerfallen". Beispiel: 3pi/4
  bruecke, v = 0,08: bei T = 300 drei Klumpen (1,56 / 0,68 / 0,43), bei T = 600 keiner mehr im Bereich. Die Zeitprobe ist
  damit nur fuer Klumpen aussagekraeftig, die in der Mitte ruhen. Der Fehler wirkt gegen Kriterium (c), nicht dafuer.

## Vorhersage gegen Ausgang

| Vorab | Ausgang |
|---|---|
| V1 schmales Fenster, 1 bis 3 Punkte je dphi | verfehlt: 6 (pi) und 7 (3pi/4) Punkte; Lage pi 0,12 bis 0,17 (vorhergesagt 0,13 bis 0,17), 3pi/4 0,06 bis 0,12 (vorhergesagt 0,08 bis 0,12) |
| V2 groesster Klumpen unter 1,7 Q0 | getroffen (hoechstens 1,56) |
| V3 ohne und nur_AC nirgends | getroffen |
| V4 bei T = 600 hoechstens die Haelfte der Fensterpunkte | getroffen (pi 0 von 6, 3pi/4 2 von 7), aber mit dem Fehlerkasten oben |

## Entscheidung nach der vorab festgelegten Regel

- dphi = 3pi/4: (a) 7 benachbarte Punkte, grob = fein; (b) ohne und nur_AC dort nicht verschmolzen; (c) bei T = 600
  zwei Punkte weiter verschmolzen. **Regel erfuellt: weiter.**
- Nebenlatte (>= 1,8 Q0): an keinem Punkt erreicht.
- **Einordnung der Leitung:**
  - Gemessen ist eine Umverteilung der Ladung auf drei Klumpen, keine Verschmelzung zu etwa 2 Q0.
  - Ein Klumpen von etwa 1,5 Q0 bleibt bei 3pi/4 und v >= 0,11 bis T = 600 im Messbereich [H: der ruhende Ball C hat
    Ladung von A und B aufgenommen; die Lage der Klumpen wurde nicht gemessen].
  - "Katalyse" im Sinn "C hilft A und B zu verschmelzen und bleibt selbst gleich" ist damit nicht gezeigt.
- Naechster Schritt (weiter), klein:
  1. Klumpen mit Ort und Ladung ueber die Zeit verfolgen (drei v-Punkte je dphi): Ist der grosse Klumpen C?
  2. L4: Ladungsuebertrag bei Q-Ball-Stoessen in Abhaengigkeit von der Phase ist aus der Literatur bekannt [L?:
     Axenides u. a. 2000; Battye/Sutcliffe 2000]. An der Quelle lesen, ob der Dreierfall mit ruhendem Ball dort vorkommt.

## L4, erster Blick an der Quelle (Leitung, 12:19:45; nur die Abstracts gelesen)

- Battye, Sutcliffe, "Q-ball Dynamics", Nucl. Phys. B590 (2000) 329 (arXiv:hep-th/0003252): Simulationen in 1D, 2D und
  3D; Ladungsuebertrag und Spaltung ("charge transfer and Q-ball fission"); die Zweierwechselwirkung wird ueber die
  zeitabhaengigen Phasen erklaert. Ein Dreierstoss wird im Abstract nicht genannt.
- Axenides, Komineas, Perivolaropoulos, Floratos, Phys. Rev. D61 (2000) 085006 (arXiv:hep-ph/9910388): 1D und 2D;
  bei relativistischen Stoessen teilt sich die Ladung in eine Vorwaerts- und eine Rechtwinkel-Komponente.
- Stand L4: Der paarweise, phasenabhaengige Ladungsuebertrag ist bekannt. Ob der Dreierfall mit ruhendem Ball
  behandelt ist, ist nur am Abstract geprueft, also offen.

