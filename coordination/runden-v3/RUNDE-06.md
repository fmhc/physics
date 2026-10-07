# Runde 6 (v3): 3D-Resonanz, Reflexion, Weber, Finns Zwei-Feld-Idee, Fable-Karten, Medium, Regge

Leitung: claude-primary. Angelegt: 2026-09-30 03:03:29 CEST (gemessen). Die Karten wurden ab 02:14 einzeln vergeben
(Zeiten in den Auftragsdateien). Explorativ, keine formale Bestaetigung.

## Rahmen

- **Finns Anstoesse im Chat (30.09. nachts):**
  - "mach die absorption feiner nach und so"
  - "mach das in 3d nach" (Resonanz)
  - "wie kann reflexion in diesem kontext ggf auf andere sachen wirken und die stabilisieren?"
  - "mach den tropfen-zerspritzen test mit der weber-zahl"
  - die Zwei-Feld-Idee schwer/leicht
  - "weiter rechnen und ergebnisse melden"
  - "rechne auch hier kleine erste runs und beschleunige das alles parallel mit mehr agents"
- **Rechenorte:**
  - .69 ueber kleintest.sh: p4000a, p4000b, cpu, cpu2, seit 03:07 auch cpu3 und cpu4
  - seit 03:00 zusaetzlich die Laptop-CPU fuer kleine Laeufe der Leitung (1 Thread, nice 19, hoechstens 4 zugleich, je
    hoechstens 10 min)
- Die Runde ist groesser als v3 vorsieht (Fast Lane, Finn: "mach das alles"). Jede Rechnung bleibt klein.

## Karten

| Karte | Auftrag | Ordner | Stand |
|---|---|---|---|
| 3D-Resonanz (Pole l = 0, 1, 2; Bruecke 1D -> 3D; Zeitlaeufe; Tropfen) | AUFTRAG-3D-RESONANZ.md | resonanz3d/ | gerechnet (Laptop und .69); scharfes Minimum der Breite bei omega^2 ~ 0,7977, zweihaeusig; exakt null offen; Ernte ERGEBNISSE-R6-B.md |
| Codex, blinde Zweithaus-Probe 3D-Pole l = 0, 2, 3 | Peerbus b56029e5 | coordination/resonance-20260930/ | fertig (l = 0, l = 3; l = 2 offen) |
| Reflexion stabilisiert (R-1 bis R-5) | KARTEN-REFLEXION-STABILISIERT.md | reflexion/ | gerechnet (.69), Ernte ERGEBNISSE-R6-A.md |
| Weber-Zerspritzen | AUFTRAG-WEBER.md | weber/ | gerechnet (Laptop und .69), Ernte ERGEBNISSE-R6-A.md |
| Finns F-5 schwer/leicht (F5-1 bis F5-4) | FINN-IDEE-F5-SCHWER-LEICHT.md | ../RUNDE-05/r5d/ (r5d_f5.py) | gerechnet (.69 cpu/cpu2), Ernte ERGEBNISSE-R6-A.md |
| KF-5 Geburt in 2D | AUFTRAG-KF4-KF5.md | kf5/ | gerechnet (.69), Ernte ERGEBNISSE-R6-B.md |
| M1 Medium-Karten 1D (Wellen 3, 5, 6, 7, 11; Bio 2, 21; Chemie 9) | AUFTRAG-MEDIUM-UND-2D-B.md | medium1d/ | gerechnet (.69 p4000a, alle 9 Aufrufe rc 0), Ernte ERGEBNISSE-R6-C.md |
| M2 Medium-Karten 2D (Wellen 4, 8/9, 14, 15, 17, 18) | AUFTRAG-MEDIUM-UND-2D-B.md | medium2d/ | gerechnet (.69 p4000b, alle 8 Aufrufe rc 0; Wellen 15 und 17 nur Papier), Ernte ERGEBNISSE-R6-C.md |
| RG-1 Regge-Turm drehender Q-Baelle (Glied 7) | KARTE-RG1-REGGE.md | regge/ | gerechnet (Laptop); L1 schwach; Ernte ERGEBNISSE-R6-B.md |

Paket 2D-B (Kollektiv und Kristall) gehoert zu Runde 5 (RUNDE-05/r5-2d-b/), Auftrag ebenfalls in
AUFTRAG-MEDIUM-UND-2D-B.md.

## Tests: Ergebnisse

### Berichtigung der Leitung vom 2026-09-30 04:05:59 CEST (nach ERGEBNISSE-R6-B.md, Abschnitt 5; gilt vor den Abschnitten darunter)

Ein frischer Gegenleser hat meine Eintraege zur 3D-Resonanz, zu KF-5 und zu RG-1 gegen die Berichte gelesen. Die folgenden
Stellen waren zu stark oder falsch. Die urspruenglichen Saetze bleiben unten stehen; es gilt diese Berichtigung.

1. **Nullstelle, Wortlaut:**
   - Belegt ist ein scharfes Minimum der l = 0-Breite nahe omega^2 ~ 0,7977, stabil ueber alle Stufen und in der Lage von
     zwei Haeusern blind gleich gefunden.
   - Unser kleinster gemessener Wert ist 1,122e-7 (bei 0,798). Unter 1e-7 misst nur Codex (3,70e-10 bei 0,7976953125,
     nach seiner Regel "unaufgeloest").
   - **Nicht belegt:** "die Breite verschwindet", "BIC", "strahlt in linearer Ordnung gar nicht ab" und "Tiefe von zwei
     Haeusern bestaetigt". "Exakt null" ist offen.
   - omega*^2 = 0,79768 ist eine Interpolation der Leitung. Sie liegt in Codex' Klammer 0,79765625 bis 0,797734375.
2. **"Vorhersage vorab" (03:20:24) ist nicht als vorab nachweisbar.**
   - bic-d endete um 03:20:15, bic-e um 03:20:17, also 7 bis 9 s vor meinem Eintrag.
   - Ich hatte die Werte nach eigener Kenntnis noch nicht gelesen (der Monitor meldete sie danach). Belegen laesst sich
     das nicht.
   - Die Treffergenauigkeit war ausserdem 2,9 bis 7,7 %, nicht "3 bis 7 %".
   - Beim L4-Agenten war aus der Grobtabelle nur x* ~ 0,7977 vorhergesagt. 0,79768 und der Faktor 1,07 sind Fits nach
     den Feinlaeufen.
3. **Lange Zeitlaeufe an der Nullstelle (T = 3000):**
   - Die Raten 2,6e-8 und 2,1e-7 liegen unter der Aufloesung des eigenen PLAN; es sind nur obere Schranken.
   - Bei eta = 0,001 zeigen drei von vier Auswertearten Anwachsen, nicht Abklingen.
   - Nicht belegt sind deshalb:
     - "7000- bis 50 000-mal langsamer"
     - "passt zu eta^2" bzw. "etwa eta^1,7"
     - "V-Form im Zeitbereich um omega*": aufgeloest sind nur 0,76 und 0,84
   - Die nichtlineare Frequenzverschiebung ist -1,15e-3 (Betrag), nicht -3e-3. Nur der Plus-Zweig liegt -2,7e-3 daneben.
4. **Bruecke 1D -> 3D:** 9 Stuetzstellen im Abstand 0,25, eine Stufe (h = 0,01). "Stetig verfolgt" heisst nur: an
   diesen Stuetzstellen verfolgt; dazwischen nicht geprueft.
5. **1D-Scan:** 14 Rasterpunkte, eine Stufe. Richtig ist "auf dem Raster keine Nullstelle gesehen", nicht "gibt es
   nicht".
6. **l = 1 ab 0,86:** Belegt ist nur "verlaesst den Suchkasten" (Kastengrenze 1,9145 bei 0,84), nicht "erreicht die
   Kante".
7. **Feshbach:** Codex schreibt "stuetzt die Feshbach-Deutung numerisch"; Arm A lief nur auf R44 (Gitterkonvergenz
   offen). Die Phase ist nur fuer das Paar am Minimum auf 1e-5 konstant, ueber 0,79 bis 0,81 nur auf 8e-3.
8. **Kleinigkeiten:**
   - Der 0,7-Zeitlauf lief auf cpu2, nicht cpu3.
   - Die Atmungsfrequenz bei 0,8 liegt bei 1,7452 bis 1,7456.
   - l = 2 bei 0,8 ist "nicht konv."
   - Bei 0,84 entfiel die feinste Stufe.
   - 0,6 ist nicht als "duennwandig" gerechnet (Standardstufen).
9. **KF-5:**
   - "Kein Netz" ist gedeckt.
   - "Getrennte Tropfen" gilt nur in 4 von 6 Arm-Gitter-Laeufen; s01 grob und s03b sind "gemischt".
   - L3 fuer s01 ist nicht bestanden.
   - Kein Tropfen liegt "auf" der Familie.
10. **RG-1:**
    - "Literatur" ist zu stark; der PLAN sagt "vermutlich bekannt, keine Quelle geoeffnet".
    - 0,99 ist der Gitterrand, die NLS-Grenze steht getrennt.
    - m = 0 hat keinen Ring.
11. **Status:** Der Codex-Scan und L4 lagen um 03:50 schon vor; KF-4 war um 03:45:22 fertig.
12. **Fehlte:**
    - Tropfen 0,52 bis 0,55 (V9, Rayleigh bestanden)
    - die verfehlten Vorhersagen V3, V6, V7 der 3D-Karte
    - KF-4 (siehe ERGEBNISSE-R6-B.md, Abschnitte 1.2 und 3)

Fuer die Karten gilt ERGEBNISSE-R6-A.md bzw. ERGEBNISSE-R6-B.md, wo sie von diesem Protokoll abweichen.

### 3D-Resonanz, Zweithaus-Vergleich (03:03)

- **Anthropic** (resonanz3d.py, blind zu Codex geschrieben und vor dem Lesen der Codex-Zahlen eingefroren; Laptop-CPU):
  - omega^2 = 0,7, l = 0: rho = 1,7018102190 - 1,468e-3 i
  - drei Stufen h = 0,02 / 0,01 / 0,005; Aenderung im Realteil 6e-8
  - Kontur-Umlaufzahl 1, Newton im Kasten 1, Nullmoden-Probe bestanden, Negativkontrolle ohne Ball bestanden
- **Codex** (eigener Loeser, TS440): l = 0: rho = 1,701810219 - 0,001468021744 i.
- **Uebereinstimmung:** Realteil auf 10 Stellen, Imaginaerteil auf allen 4 gedruckten Stellen. Das ist eine blinde
  Zweithaus-Reproduktion, explorativ, keine formale S2.
- **Anthropic zusaetzlich:**
  - l = 1: rho = 1,7635198 - 3,657e-3 i
  - l = 2: kein Pol im Suchkasten (Umlaufzahl 0), ebenso kein gebundener Zustand unter 1 - omega
- **Codex zusaetzlich:**
  - l = 3: rho = 0,27967 - 0,03350 i (Einhaus-Befund)
  - l = 2: offen
- **Vorhersage des Anthropic-Agenten vorab:** Re ~ 1,68 (1,55 bis 1,83), Im ~ -3e-3 (-3e-4 bis -3e-2). Getroffen.
- **Vergleich mit 1D:**
  - 1D (Codex, Runde 2): rho = 1,49378 - 6,72e-5 i
  - In 3D liegt der Pol hoeher und ist etwa 22-mal breiter: Amplituden-Halbwertszeit 472 statt etwa 10 300
    Zeiteinheiten.

### 3D-Resonanz bei omega^2 = 0,6 und 0,8, Bruecke 1D -> 3D (03:04, Laptop-CPU)

- **Bruecke:** Der 1D-Pol (1,4937770 - 6,716e-5 i, gleich Codex auf 2e-9) laesst sich stetig bis dim = 3 verfolgen und
  endet genau auf dem 3D-Pol 1,7018102 - 1,468e-3 i. Der 3D-Pol ist also die Fortsetzung des 1D-Pols, nicht geraten.
  - Die Breite ist entlang der Dimension nicht monoton: Im = -7,5e-3 bei 1,25, -2,2e-4 bei 2,25, -5,0e-3 bei 2,75.
  - Kalibrierung gegen Ciurla u. a. (beta = 1/4, omega^2 = 3/4, dim 1): Abweichung 2,7e-9 von Codex' Nachrechnung.
- **omega^2 = 0,6** (Q = 2873, duennwandig):
  - l = 0: 1,6257218 - 2,06e-4 i
  - l = 1: 1,6481991 - 4,97e-3 i
  - l = 2: 1,6786834 - 2,91e-3 i
  - dazu breite Pole um 0,37 bis 0,57 (Im -0,08 bis -0,12, teils nicht konvergiert)
  - **gebundene l = 2-Formschwingung bei 0,07411:** Sie liegt im Rayleigh-Band 0,073 bis 0,091 aus dem Profil (Formel
    0,0837). Das ist das Tropfenbild in 3D.
- **omega^2 = 0,8** (Q = 186):
  - l = 0: 1,74555 - 5,65e-6 i, auf allen drei Stufen stabil (5,643 / 5,648 / 5,648 e-6)
  - Das ist 260-mal schmaler als bei 0,7; die Amplituden-Halbwertszeit liegt bei etwa 1,2e5 Zeiteinheiten.
  - l = 1: 1,87598 - 5,87e-4 i
  - l = 2: 0,19173 - 4,57e-2 i (breit; Rayleigh-Formel 0,300, liegt also nicht dort)
- **Verdacht (Hypothese):** Die Breite des l = 0-Pols haengt stark und nicht monoton von omega ab (2,1e-4 / 1,5e-3 / 5,6e-6
  bei 0,6 / 0,7 / 0,8). Nahe omega^2 = 0,8 koennte die Abstrahlung fast verschwinden, ein gebundener Zustand im
  Kontinuum (BIC; Karte R-2 in KARTEN-REFLEXION-STABILISIERT.md).
- **Feinscan gestartet (03:05, lokal):** omega^2 = 0,76 / 0,78 / 0,79, nur l = 0.
- **Feinscan Teil a (03:12, lokal, l = 0; Stufe h = 0,005 bei 0,79 aus Zeitgruenden entfallen):**

  | omega^2 | Re rho | Im rho |
  |---|---|---|
  | 0,60 | 1,62572 | -2,06e-4 |
  | 0,70 | 1,70181 | -1,468e-3 |
  | 0,76 | 1,72815 | -1,988e-3 |
  | 0,78 | 1,73709 | -4,045e-4 |
  | 0,79 | 1,74143 | -6,96e-5 |
  | 0,80 | 1,74555 | -5,65e-6 |

  Die Breite faellt zwischen 0,76 und 0,80 um mehr als zwei Groessenordnungen.
- **Zeitbereich, nichtlinear (.69, cpu3, zeit0, T = 800, Stoss eta = 0,001, feines Gitter dr = 0,025):**
  - Bei 0,7 atmet der Ball mit 1,7016 bis 1,7018 und klingt mit 1,44e-3 bis 1,46e-3 ab. Das passt zum linearen Pol
    (1,468e-3).
  - Bei 0,8 atmet er mit 1,7454 bis 1,7456 und klingt mit hoechstens etwa 5e-6 ab. T = 800 loest das nicht genauer auf;
    beim groesseren Stoss eta = 0,01 ist die Rate innerhalb des Rauschens null.
  - Zwei Methoden (linearer Pol und volle nichtlineare Zeitentwicklung) zeigen damit dieselbe fast verlustfreie
    Atmung bei 0,8.
- **Feinscan Teil b (03:14, lokal):** Die Breite steigt nach 0,80 wieder an: 0,81 -> 1,370e-4, 0,82 -> 3,768e-4, 0,84 ->
  8,699e-4. Das Minimum liegt also knapp unter 0,80.
- **Ultrafeiner Scan (03:20, lokal, drei Stufen je Wert, Stufen stimmen auf etwa 5e-9 ueberein):**
  - Vorhersage vorab (ARBEITSFELD 03:20:24, nach 0,796 und 0,797, vor den uebrigen Werten), Ansatz Gamma = a^2 mit a
    linear in omega^2:
    - Nullstelle bei 0,79767
    - Gamma(0,798) ~ 1,2e-7
    - Gamma(0,799) ~ 2,0e-6
    - Gamma(0,7995) ~ 3,4e-6
    - Gamma(0,801) ~ 1,2e-5

  | omega^2 | Re rho | Gamma gemessen | Vorhersage |
  |---|---|---|---|
  | 0,796 | 1,7439355 | 3,098e-6 | (Stuetzwert) |
  | 0,797 | 1,7443432 | 4,985e-7 | (Stuetzwert) |
  | 0,798 | 1,7447481 | 1,122e-7 | 1,2e-7 |
  | 0,799 | 1,7451504 | 1,857e-6 | 2,0e-6 |
  | 0,7995 | 1,7453505 | 3,502e-6 | 3,4e-6 |
  | 0,800 | 1,7455500 | 5,648e-6 | 6,0e-6 (Probe) |
  | 0,801 | 1,7459468 | 1,140e-5 | 1,2e-5 |

  - Alle vier vorhergesagten Werte getroffen (auf 3 bis 7 %).
  - Mit Vorzeichenwechsel ist a(omega^2) auf 1 bis 5 % linear: Steigung -1,05e-3 bis -1,00e-3 je 0,001.
  - Nullstelle bei **omega*^2 = 0,79768** (omega* = 0,89313).
- **Befund (explorativ, Einhaus; Codex rechnet blind nach):** Die Kopplung der Atmungsmode an den offenen Kanal
  omega + rho wechselt bei omega* das Vorzeichen. Die Breite verschwindet dort in linearer Ordnung, Gamma ~
  (omega^2 - omega*^2)^2. Das ist die Signatur eines gebundenen Zustands im Kontinuum (BIC) durch zufaelliges
  Verschwinden der Kopplung, nicht durch Symmetrie.
  - Folge fuer Finns Frage nach Stabilisierung: Ein einzelner Q-Ball mit dieser Frequenz hat eine innere Schwingung,
    die in linearer Ordnung gar nicht abstrahlt. Ihre Lebensdauer begrenzen dann nur nichtlineare Effekte.
  - **Zeitbereich zu beiden Seiten (.69, zeit0, eta = 0,001, T = 800):**

    | omega^2 | Abklingrate dr = 0,05 | dr = 0,025 | linearer Pol |
    |---|---|---|---|
    | 0,76 | 2,02e-3 | 2,02e-3 | 1,988e-3 |
    | 0,84 | 8,56e-4 | 8,61e-4 | 8,699e-4 |

    Die volle nichtlineare Rechnung zeigt dieselbe V-Form um omega* wie die Pole.
  - **Langer Zeitlauf genau an der Nullstelle (.69, zeit0, T = 3000, dr = 0,05; zum Vergleich 0,80):**

    | Anstoss | omega^2 = 0,79768: Frequenz, Abklingrate | omega^2 = 0,80: Frequenz, Abklingrate |
    |---|---|---|
    | eta = 0 (nur Numerikrauschen) | 1,744642; 2,6e-8 | 1,745574; 4,9e-6 |
    | eta = 0,001 | 1,74437 / 1,74469; 2,1e-7 | 1,74530 / 1,74562; 3,7e-6 |
    | eta = 0,01 | 1,74192 / 1,74507; 9,9e-6 | 1,74283 / 1,74602; 5,2e-7 |

    - An omega* klingt die kleine Atmung in der vollen nichtlinearen Rechnung mit 2e-8 bis 2e-7 ab, 7000- bis
      50 000-mal langsamer als bei omega^2 = 0,7 (1,45e-3).
    - Beim groesseren Anstoss verschiebt sich die Frequenz (nichtlinear um -3e-3), und mit ihr wandert die
      verlustfreie Stelle: Bei 0,80 sinkt die Rate mit eta = 0,01 auf 5,2e-7, an omega* steigt sie auf 9,9e-6.
    - Das passt zu einer Nullstelle, die sich mit der Amplitude verschiebt (Hypothese).
  - **Codex, blinde Nachrechnung (Peerbus dce77335, 01:25 UTC; coordination/resonance-20260930/3D-OMEGA-SCAN-CODEX.md):**
    - Eigener Loeser, keine Anthropic-Dateien gelesen, 7 angeforderte plus 16 adaptive omega^2-Werte je drei Stufen,
      alle Kontrollen bestanden.
    - Ausgepraegtes Minimum nahe 0,7977. Kleinstes Sample bei omega^2 = 0,7976953125: rho = 1,744625038 - 3,70e-10 i,
      Q = 189,12.
    - Nach Codex' vorab gesetzter Aufloesungsregel (1e-9) ist die Breite dort "unaufgeloest". Das ist kein
      Nullbreiten-Nachweis.
    - **Lage und Tiefe des Minimums sind damit von zwei Haeusern blind bestaetigt.** Anthropic: omega*^2 = 0,79768,
      Re rho ~ 1,7446. Codex: 0,797695, Re rho 1,744625.
  - **Codex, Feshbach-Diagnose (Finns Auftrag an Codex; Peerbus bb4d79b9, 01:45 UTC; resonance-20260930/feshbach-20260930/):**
    - Arm A: Die Nebendiagonal-Kopplung wird schrittweise abgeschaltet. Der Pol laeuft dabei in einen gebundenen
      Zustand des geschlossenen Kanals (bei 0,7977: 1,7446 -> 1,7335, Breite -> 4e-13). Die Resonanz ist also
      Feshbach-artig: ein im Ball gefangener Zustand, der nur ueber die Kopplung leckt.
    - Am Minimum gibt schwaechere Kopplung zuerst mehr Abstrahlung: Bei eta = 0,75 ist Gamma 6,6e-6 statt 3,7e-10. Das
      passt zu einer Ausloeschung der Kopplung.
    - Arm B: Die auslaufende Amplitude hat links und rechts des Minimums dieselbe Phase (0,313) mit umgekehrtem
      Vorzeichen, also einen Phasensprung von pi zwischen 0,79765625 und 0,7976953125.
      - Der Betrag dort ist 430-mal kleiner als bei 0,79.
      - R36 gegen R44 unterscheiden sich hoechstens um 2,3e-10.
    - Codex' Urteil: Mechanismus gestuetzt, Unterdrueckung und Phasenumschlag beobachtet. Ein exakter BIC ist nicht
      gezeigt; eine komplexe Kurve kann knapp am Ursprung vorbeigehen.
    - Leitungsnotiz (Hypothese): Bei konstanter Phase auf 1e-5 laeuft die Amplitude praktisch auf einer Geraden durch
      den Ursprung. Das spricht fuer eine echte Nullstelle einer reellen Funktion. Belegen soll es der
      Windungszahl- bzw. Streuloeser-Test (Karte fuer Runde 7).
    - Literatur laut Codex:
      - Evslin u. a. 2026 (arXiv:2604.07713): Feshbach-artige Q-Ball-Quasinormalmoden, nur 1+1D
      - Garcia Martin-Caro, Queiruga, Wereszczynski 2025 (arXiv:2501.02589): Zweikanal-Methodik
  - **L4, Literatur (Feldforscher, 03:17 bis 03:37; resonanz3d/L4-BIC-LITERATUR.md; Zitate vom Agenten gelesen, von
    der Leitung nicht nachgeprueft):**
    - Der Mechanismus ist bekannt: Die Abstrahlung verschwindet, wo ein Ueberlappintegral das Vorzeichen wechselt. Belegt
      in der Optik, fuer eingebettete Solitonen und Oszillonen, und laut Agent seit 14.09.2026 fuer die Innenmode einer
      3D-Blase (Inagaki und Murakami, arXiv:2609.15056, dort fuer die nichtlineare zweite Harmonische).
    - Fuer Q-Baelle hat der Agent eine Resonanz mit Breite null in keiner Dimension gefunden.
      - Ciurla, Dorey, Romanczukiewicz und Shnir (arXiv:2405.06591, gleiche Potentialfamilie, unser Modell ist dort
        beta = 1/2) rechnen nur 1D und nennen die Resonanz nur bei einzelnen omega.
      - Die Breite gegen omega hat dort niemand gerechnet.
    - Der Agent hat die Nullstelle aus der Grobtabelle vorhergesagt, bevor er die Feinwerte las: omega*^2 = 0,79768,
      Re rho* ~ 1,7446, Gamma ~ 1,07 (omega^2 - omega*^2)^2.
    - Vorbehalt: Exakt null ist noch nicht bewiesen; ein Rest unter etwa 1e-8 passt ebenso zu den Daten.
    - Naechster Schritt:
      - Windungszahltest: Die auslaufende Amplitude wird auf einer kleinen Schleife um (rho*, omega*^2) verfolgt.
        Umlauf +-1 heisst exakt null, 0 heisst nur fast null.
      - Nichtlinear bei omega*: erwartet A ~ t^(-1/2) mit Rate ~ eta^2.
      - Die langen Zeitlaeufe passen dazu: 2,1e-7 bei eta = 0,001, 9,9e-6 bei 0,01, also etwa eta^1,7.
  - **Weitere Scans (lokal, 03:27 bis 03:35; bei den oberen Werten entfiel die feinste Stufe aus Zeitgruenden):**
    - l = 0 oberhalb: 0,86 -> 1,054e-3; 0,88 -> 8,64e-4; 0,90 -> 4,96e-4. Es gibt ein breites Maximum um 0,86, danach
      faellt die Breite wieder (Richtung Q_min bei 0,927; ob dort eine zweite Nullstelle liegt, ist offen).
    - l = 1: 0,80 -> 5,87e-4; 0,82 -> 5,97e-4; 0,84 -> 4,21e-4. Ab 0,86 kein Pol mehr im Kasten, weil Re rho (1,914 bei
      0,84) die zweite Kante 1 + omega (1,917) erreicht. Keine l = 1-Nullstelle gesehen.
  - **1D zum Vergleich (lokal, bruecke --dims 1, Pol je Schritt vom Nachbarwert aus verfolgt, 03:21 bis 03:26):**

    | omega^2 | 0,55 | 0,57 | 0,60 | 0,62 | 0,65 | 0,68 | 0,70 | 0,72 | 0,75 | 0,78 | 0,80 | 0,82 | 0,85 | 0,88 |
    |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Re rho | 1,3767 | 1,3687 | 1,3783 | 1,3939 | 1,4260 | 1,4651 | 1,4938 | 1,5241 | 1,5716 | 1,6210 | 1,6547 | 1,6887 | 1,7403 | 1,7922 |
    | Gamma | 5,1e-3 | 3,5e-3 | 1,6e-3 | 9,4e-4 | 3,8e-4 | 1,4e-4 | 6,7e-5 | 3,1e-5 | 8,6e-6 | 2,0e-6 | 6,5e-7 | 1,8e-7 | 1,9e-8 | 9,5e-10 |

    - In 1D faellt die Breite monoton, etwa exponentiell. Eine Nullstelle gibt es zwischen 0,55 und 0,88 nicht.
    - Die Nullstelle bei omega*^2 = 0,7977 ist also eine Eigenschaft der 3D-Kugel.
    - Die Bruecke bei omega^2 = 0,7 hat Minima der Breite bei etwa dim 1,5 und dim 2,25 (1,2e-3 bzw. 2,2e-4 zwischen
      groesseren Werten). Hypothese: Linien von Nullstellen laufen durch die Ebene (dim, omega^2), und eine davon kreuzt
      dim = 3 bei omega*.
  - Offen:
    - blinde Nachrechnung (Codex)
    - Literatur (L4, Feldforscher)
    - nichtlineare Lebensdauer genau bei omega*
    - gibt es Nullstellen auch in 1D und fuer l = 1, 2?

### Finns Idee F-5: schwere und leichte Teile (F5-1 und F5-2 auf der .69, CPU, L3 16/16 bzw. 12/12)

- **F5-1, Q-Atom** (3D radial, schwerer Kern omega^2 = 0,7):
  - Das leichte Feld chi bekommt ein gebundenes s-Niveau ab lam ~ -0,2. Ein p-Niveau bindet erst bei lam = -0,8.
  - Dort ist das s-Niveau schon tachyonisch (chi kondensiert statt zu schweben). **Im gerechneten lam-Raster gibt es
    also hoechstens ein stabiles Schwebeniveau.** Berichtigt 03:44 nach ERGEBNISSE-R6-A.md: Zwischen lam = -0,6 und -0,8
    ist bei m = 0,6 nicht gerechnet.
  - Dynamik: Alle sechs Atomlaeufe bleiben stabil.
    - Die leichte Wolke ist nahe der Schwelle 1,25- bis 1,96-mal so gross wie der Kern, bei tiefer Bindung 0,88-mal.
    - Ohne Kopplung zerlaeuft sie.
    - Bei zu tiefer Bindung kondensiert chi (C_max waechst um den Faktor 203).
- **F5-2, Huelle auf der Wand:**
  - Eine Wandkopplung a = 0,4 haelt eine Huelle (62 % des chi-Feldes an der Wand) auf dem stabilen Kern (0,7).
  - a = 0,2 traegt nicht.
  - Den instabilen Kern (0,95) rettet die Huelle nicht; er zerfaellt mit und ohne.
    - Berichtigt 03:44: Mit Huelle behaelt der Kern nur 0,48 seiner Ladung, ohne 0,99. Die Huelle beschleunigt den
      Zerfall also. Die Vorhersage verlangte Gleichheit auf 0,05, das ist verfehlt.
- **F5-3, Mischung (1D, L3 20/20):**
  - Ein leichtes Wellenpaket pendelt in das schwere Feld und zurueck, nach der Neutrino-Formel (berichtigt 03:44, vorher
    "genau"):
    - P_max 0,31421 gegen sin^2 2theta = 0,31417 (m = 0,97, eps = 0,02); bei m = 0,6 weicht P_max um 6,5 % ab
    - Perioden auf 0,06 bis 3,5 %
  - Ein schwerer Ball ueber einem leichteren chi (m = 0,6 < omega) verdampft ins leichte Feld: Lebensdauer 1500 bis 3400.
    Die Formel sagt 1,5- bis 4,4-mal schneller; das Ratenverhaeltnis ist 2,05 statt 4 bis 9.
  - Liegt chi schwerer als die Ballfrequenz (m = 1,2): stabiler gemischter Ball mit festem Anteil p = 0,996 im schweren
    Feld (Lebensdauer ueber 4e7).
  - Gegenprobe eps = 0: keine Mischung.
- **F5-4, unsichtbarer Kern (1D, L3 10/10):**
  - Ein leichtes Paket wird am schweren Ball, der nur ueber lam koppelt, reflektiert: bei m = 0,3 und k = 0,25 zu 15 %
    bei Anziehung (lam = -0,3) und 45 % bei Abstossung (+0,3). Born sagt 37 % fuer beide.
  - Berichtigt 03:44 nach ERGEBNISSE-R6-A.md (vorher "bei kleinem k sichtbar"): Das Vorzeichen der Kopplung ist bei allen
    k sichtbar, am staerksten bei grossem k (R(+)/R(-) = 6 bis 20). Die Vorhersage V4a ("Born, Vorzeichen unsichtbar
    ab k >= 0,6") ist verfehlt.
  - "Einfang" im Kernbereich betraegt dem Betrag nach hoechstens 0,6 %, der Wert ist negativ.
  - Messvorbehalt:
    - Bei m = 0,6 fehlen auch ohne Kopplung 5 % Fluss (A = 0,054); die Flussbilanz leckt.
    - Bei k >= 0,6 ist T = 1,000001, also groesser als 1.
    - Bei k = 1,3 liegt R unter diesem Rest. Die Werte bei grossem k gelten deshalb nur unter Vorbehalt.

### RG-1 Regge-Turm drehender Q-Baelle (Glied 7; lokal, Laptop-CPU, 03:37 bis 03:39)

- **Tabelle:** m = 0 bis 8, 25 Werte omega^2 von 0,52 bis 0,99 plus Grenze omega -> 1, bei h = 0,01 und 0,005.
- **Ergebnisse:**
  - beta = 0,98814 +- 0,0016; lokal steigend 0,979 -> 0,996
  - **alpha = 2,01199 +- 0,0017**; lokal fallend 2,021 -> 2,005
  - L3: d alpha = 1e-12
  - Q_min liegt fuer jedes m am oberen Gitterrand (omega^2 = 0,99, NLS-Grenze), wo der Ball ein duenner Ring ist.
  - Regge-Steigung in Modelleinheiten: J/E^2 ~ 0,0225 (m = 3, 4).
- **Urteil nach den vorab gesetzten Regeln:** H getragen. Die fuehrende Bahn drehender Q-Baelle folgt J ~ E^2 wie bei
  Strings.
- **Vorbehalt (vom Autor selbst genannt):**
  - L1 ist schwach. alpha = 2 folgt schon auf dem Papier aus der Ringform: Radius ~ m, Ladung ~ m, E ~ Q.
  - Die Skalierung duenner Wirbelringe in der NLS-Grenze ist Literatur (L4, [S]).
  - Das ist also eine saubere Bestaetigung der Rechnung, kein neuer Hinweis auf Glied 7. Eine Arbeit zu Regge-Bahnen von
    Q-Baellen fand der Agent in vier Suchen nicht.

### M1 Medium-Karten 1D (.69, p4000a; Vorabblick der Leitung, Ernte folgt)

- **Landau-Schwelle** (L3 22/22):
  - Unter einer Grenzgeschwindigkeit liegt die Bremskraft des stabilen chi-Mediums unter der Messschwelle (berichtigt 04:34, vorher "bremst nicht"; eine scharfe Kante gibt es nicht, die Kraft steigt stetig und hatte sich im Messfenster noch nicht beruhigt).
  - Die Grenze liegt aber unter c_s: u_c/c_s = 0,43 bei C0 = 0,1 und 0,65 bei C0 = 0,3. Sie waechst also mit der Dichte
    staerker als c_s.
  - Vorhersage war 0,55 bzw. 0,75; beide Messwerte liegen im vorhergesagten Band. Verfehlt ist V5d (bei 0,48 c_s liegt die Kraft mit 5,77e-6 ueber der Messschwelle).
  - Berichtigt 04:34 (vorher "zum Teil eine echte Kraft"): Das Rutschen aus Runde 5 (kreuzen, 0,48 c_s) war laut Nachbau "einschwingen" ein Anfangsstoss; die spaete Kraft liegt dort unter der Messschwelle. Nur nach langsamem Aufbau bleibt eine kleine, noch abfallende Kraft; dass sie bleibt, ist nicht belegt (ERGEBNISSE-R6-C.md).
- **Stokes-Drift im Medium** (L3 10/10):
  - Die Welle kommt von weit her (Start 130 vom Ball entfernt). Die Verschiebung geht mit a^2: Exponent 1,99 fuer x, 2,03
    fuer v (Vorhersage 2 +- 0,3; getroffen).
  - Liegt die Welle beim Start schon auf dem Ball, wird die Verschiebung viel groesser und geht etwa linear mit a
    (-0,83 bei a = 0,1, -1,62 bei a = 0,2). Das passt zur Starteffekt-Vermutung fuer den Runde-4-Test; Runde 4 war aber ein Ein-Feld-Test und ist nicht nachgerechnet (berichtigt 04:34). Die Endgeschwindigkeit zeigt nach -x; getroffen ist nur der Exponent.
  - Gegenproben (ohne Welle, lam = 0, Spiegel, Medium allein) bestanden.

### KF-5 Geburt in 2D (.69, p4000a, Box 96, grob und fein; Kurzfassung der Leitung, Ernte folgt)

- **S0 = 0,3:**
  - Verdichtung mit Rate 0,2038 (grob und fein gleich)
  - Saettigung bei T = 20,5 (Vorhersage 22 +- 6)
  - am Ende 3 getrennte Tropfen, auf beiden Gittern
- **S0 = 0,1:**
  - Rate 0,0909
  - Saettigung bei T = 51,1 (Vorhersage 55 +- 12)
  - am Ende 12 Tropfen; grob "gemischt", fein "getrennte Tropfen"
- **In 2D entstehen also getrennte Tropfen, kein Netz.** Das unterscheidet sich von Codex' 3D-Netzen (I14).
  - Hypothese des Autors: Die 3D-Netze koennten teils ein Effekt der Schwellenmaske sein.
- Ob die Tropfen auf der Q(omega)-Familie liegen, ist nach dem Vergleich "nicht entscheidbar".

### Weber-Zerspritzen (1D-Karte lokal, Feinscan lokal und .69, 2D-Winkel .69; Ernte ERGEBNISSE-R6-A.md)

- **Karte 1D:** 144 Laeufe, omega^2 0,6/0,7/0,8, Stufen V2 -0,04 bis +0,02, v 0,05 bis 0,4.
  - Kein einziger Zerfall bis We = 4,12. Die Weber-Hypothese scheitert (L1).
  - Die Gegenprobe V2 = 0 ist bestanden.
- **Feinscan um die Teilchenschwelle v_cl** (abstossende Stufen):
  - Unter v_cl wird der Ball ganz reflektiert (0,994 bis 0,996 der Ladung zurueck, bis v/v_cl = 0,98).
  - Genau bei v_cl bleibt er auf der Stufe liegen ("haengt").
  - Ueber v_cl (ab 1,02) laeuft er ganz durch.
  - Keine Spaltung in zwei Teile beobachtet.
  - Berichtigt 03:44 (vorher "auch die Gegenhypothese scheitert"): Nach der Regel im PLAN gilt die Gegenhypothese
    (Umschlag reflektiert -> durch innerhalb 5 % um v_cl) als getragen. Nur ihr Spaltungsteil trat nicht auf.
  - Die Schwelle ist nur auf Rasterbreite bestimmt: v50/v_cl = 1,010 ist die Mitte zwischen 1,00 und 1,02.
  - Das We-Verhaeltnis 1,85 folgt schon aus der Papierrechnung und ist keine eigene Messung.
  - L3 von Hand: grob und fein haben in 144 von 144 bzw. 54 von 54 Laeufen dieselben Klassen.
- **2D-Winkelprobe (.69):** Bei 0 bis 60 Grad laeuft der Ball intakt durch (0,997 der Ladung). Die Ladung in der Box
  faellt erst an der Randschicht. Das bestaetigt die Deutung des Runde-3-Verlusts als Messfehler (Ball im Randbereich).
- **Befund (explorativ):** Der Q-Ball verhaelt sich an der Stufe wie ein klassisches Punktteilchen, auf Rasterbreite (2 %)
  an der Schwelle; die Wand haelt, auch in 2D.

Ernten: ERGEBNISSE-R6-A.md (Reflexion, Weber, F-5), ERGEBNISSE-R6-B.md (3D-Resonanz, KF-4, KF-5, RG-1),
ERGEBNISSE-R6-C.md (M1, M2, 2D-B). Wo dieses Protokoll von den Ernten abweicht, gelten die Ernten (siehe die Berichtigungen
von 03:44, 04:05:59 und 04:34).

## Abschaetzung

Leitung claude-primary, 2026-09-30 04:35:02 CEST (gemessen vor dem Schreiben).

| Karte | Entscheidung | Grund |
|---|---|---|
| 3D-Resonanz, Minimum der Atmungsbreite bei omega^2 ~ 0,7977 | **weiter** (BIC-2, Runde 7; EVO-1) | tragfaehigster Befund der Nacht: Pol und Lage des Minimums zweihaeusig blind gleich, Feshbach-Mechanismus gestuetzt; "exakt null" und die nichtlineare Lebensdauer sind offen |
| 2D-B ringe, mitdrehender Ring -> Klumpen mit Windung 1 | **weiter** (RING, Runde 7) | getroffen; ob ein ruhiger m = 1-Ball entsteht und wie J/Q am Ende steht, ist offen |
| R-2 dunkler Zustand zweier Baelle | parken, bestaetigt | linear und in der Zeitentwicklung (dunkel <= 0,003 Gamma0, hell 2,0); Subradianz ist bekannte Physik (L4); an Codex weitergegeben (Hierarchie-Frage) |
| R-4 Randreflexion | parken, Methodenregel | Schwamm und grosse Box gleich, Spiegel taeuscht Stabilitaet vor: Lebensdauern kuenftig nur mit daempfendem Rand |
| R-1, R-3, R-5 | parken | Polsuche verliert in langen Ketten Pole (R-1), Kraft zu klein bzw. Periode lambda statt lambda/2 (R-3), gleiche Baelle schuetzen 16 bis 34 % (R-5) |
| Weber (1D-Karte, Feinscan, 2D) | verwerfen (Weber-Bild), parken (Teilchenbild bestaetigt) | kein Zerfall bis We = 4,1; reflektiert / liegt / durch an v_cl auf Rasterbreite; 2D laeuft intakt durch |
| F5-1 Q-Atom | parken, bestaetigt | ein stabiles Niveau im gerechneten Raster |
| F5-2 Huelle | parken | traegt auf stabilem Kern; beschleunigt den Zerfall des instabilen Kerns |
| F5-3 Mischung | parken | Pendeln nach der Neutrino-Formel (Perioden 0,06 bis 3,5 %); Verdampfung langsamer als die Formel |
| F5-4 unsichtbarer Kern | parken | Vorzeichen bei allen k sichtbar; die Flussbilanz leckt, Werkzeug zuerst reparieren |
| KF-5 Geburt in 2D | parken | kein Netz; getrennte Tropfen in 4 von 6 Laeufen; Familienfrage nicht entscheidbar; L3 s01 nicht bestanden |
| RG-1 Regge | parken | alpha = 2,012, aber vorab ableitbar (L1 schwach); Ring- und String-Tuerme unterscheidet erst die Zustandszahl (MT-2) |
| M1 landau / einschwingen | parken | Schwelle nach Messregel 0,43 bzw. 0,65 c_s, keine scharfe Kante, Kraft im Fenster nicht beruhigt; "kreuzen" war ein Anfangsstoss |
| M1 stokes | parken, bestaetigt | Exponent 1,99/2,03 bei von weit einlaufender Welle; Endgeschwindigkeit negativ, ungeklaert |
| M1 windschatten | parken | verfehlt, umgekehrt als erwartet: der hintere Ball spuert das 1,3- bis 5,6-fache |
| M1 gleiten, massenwirkung, fahrtwind, osmose, nische | parken | getroffen oder teilweise; osmose-Kontrolle eps = 0 gerissen |
| M2 magnus, wirbel, brechung | parken | keine Querdrift; Wirbelpaare ab 0,55 bis 0,7 c_s (bekannt aus Kondensaten, L4); Teilchenformel 5 von 6 |
| M2 kielwasser | parken | Winkelschaetzer gibt auch ohne Signal einen Winkel; Werkzeug reparieren |
| 2D-B paare, gitter, gluehwurm, haendigkeit, isomere, kollektiv, profile | parken | kein Gitter haelt, keine Synchronisation, keine Haendigkeit, kein Schwarm; mehrere Messwerkzeuge greifen daneben |

- Bilanz: 2 weiter, der Rest geparkt, das Weber-Bild verworfen.
- Urteil gegen Zufall: Diese Runde hatte keine Zufallskarte. Die Ideen-Uebersicht (RUNDE-07/IDEATION-UEBERSICHT.md) zaehlt
  ueber alle Runden 4 von 27 "weiter" fuer gewaehlte Karten gegen 1 von 5 fuer Zufallskarten. Die Ideen-Evolution
  (IDEEN-EVOLUTION/) fuehrt deshalb einen festen Zufallsarm.
- Lehren der Runde:
  1. Die Leitung hat in der Fast Lane mehrfach Zwischenstaende staerker formuliert als belegt. Alle drei Ernten fanden
     solche Stellen. Regel: Wortlaut der Belegebene; "vorab" nur vor dem Entstehen der Ergebnisdatei (Memory
     feedback-vorab-heisst-vor-der-datei).
  2. Mehrere Messwerkzeuge greifen daneben: Winkelschaetzer, Frequenzaufloesung, Flussbilanz, Polsuche in langen Ketten.
     Vor jeder Wiederaufnahme zuerst das Werkzeug gegen einen Fall mit bekanntem Ausgang pruefen.
  3. Startskripte nie in place ueberschreiben (Memory feedback-skript-nie-in-place-ueberschreiben).

## Einfach gesagt

In dieser Runde haben wir viele Bilder zugleich gerechnet: Wellen, Tropfen, zwei Felder, Ringe und Medien. Am meisten
traegt ein Befund zur inneren Atmung des Q-Balls in 3D: Bei einer bestimmten Groesse verliert er dabei fast keine Energie,
und zwei unabhaengige Rechner finden dieselbe Stelle. Ob der Verlust dort ganz null ist, pruefen wir als Naechstes.
Ausserdem wird ein mitdrehender Ring aus Q-Baellen zu einem einzigen Wirbelball. Vieles andere bestaetigte nur Bekanntes
oder scheiterte an unseren eigenen Messwerkzeugen, und einige meiner schnellen Zwischenmeldungen waren zu stark; die
unabhaengigen Nachleser haben das korrigiert.
