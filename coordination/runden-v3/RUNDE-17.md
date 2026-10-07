# Runde 17 (v3, explorativ)

Leitung: claude-primary. Angelegt: 2026-10-02 09:52:35 CEST (date). Runde 16 ist abgeschlossen (RUNDE-16.md; Journal
claude-runde-v3-16-20261002, Index nr 553; Sicherung r16 gestartet).

## Uebernommen

- M_E-G3 (Codex, Theoriekarte offen)
- DIM-BEUTEL (Agent laeuft): Beutelexponent als Messer der spektralen Dimension
- Frischer Blick auf den v2.2-diff (Agent laeuft)

## Literatur zum Start (Leitung, arXiv-API, nur Abstracts) [S: Abstract]

- arXiv:2609.26627 (22.09.2026), "Dense Packing of Tetrahedra in Cylinders":
  - Die Boerdijk-Coxeter-Helix ist keine Einzelerscheinung, sondern folgt aus der Zylinderbegrenzung als dichteste Packung.
  - Bei einem kritischen Durchmesser gibt es eine Symmetriebrechung: Die chirale Helix steht neben einer achiralen
    Dimerkette, bei gleicher Packungsdichte.
  - **Bedeutung fuer Finns Kette [H]:** Die Tetraederkette ist unter seitlicher Begrenzung die dichteste Form. Das ist
    eine Stabilitaetsrolle der Kette als Ganzes, unabhaengig von 12 oder 20 Ecken.
- arXiv:1302.1174: Die BC-Helix hat keine nichttriviale Translations- oder Drehsymmetrie; das passt zu theta = arccos(-2/3)
  irrational (TETRAKETTE-1 K0). Periodische Abwandlungen haengen mit pentagonalen und ikosaedrischen Tetraeder-Aggregaten
  zusammen.
- Der 600-Zell-Bezug (30er-Ring) ist damit nicht belegt und bleibt [L?].
- Elliptisches eingeschraenktes Problem: Die Abfrage fand nur arXiv:2106.10590 (allgemein, triaxiale Primaerkoerper);
  Stabilisierung jenseits von Routh nicht im Abstract. Der Danby-Bezug bleibt [L?].

## STILLE-ZWEIFELD gestartet (2026-10-02 09:54:04 CEST)

- Karte RUNDE-17/stille-zweifeld/KARTE.md (ab 09:52:35), Code-Agent auf cpu3/cpu4, Zeitbox 120 min.
- Frage: Hat der Q-Ball in Codex' Zweifeldmodell stille Stellen? Mit chi gibt es drei Kanaele: a, b und den chi-Kanal
  (Schwelle sqrt(2)).
  - Bereich E1 (nur a offen): eine stille Stelle ist generisch moeglich.
  - Bereich E2 (a und c offen): generisch keine.
- Vorhersagen:
  - S1: mindestens eine Stelle in E1 (45 %)
  - S2: keine in E2 (90 %)
  - S3: Funde auf dem Duennwand-Ast mit Huelle (60 %)
  - S4: Die M1-Stelle hat keinen Nachfolger mit nur einem offenen Kanal (75 %)
- Aktive Agenten: Gegenleser v2.2-diff, DIM-BEUTEL, STILLE-ZWEIFELD (drei, Maximum).

## NACHRECHNUNG-ROUTH (Leitung; Karte und Vorhersage geschrieben 2026-10-02 09:55:31 CEST, vor dem Code)

- Gegenstand: DREI-TAKT D1a (Runde 16). Die Exzentrizitaet e der Hauptkoerperbahn stabilisiert L4 jenseits der
  Routh-Grenze, mit einem schmalen Streifen bis mu = 0,04575 (e 0,055 bis 0,29). Die Vorab-Wahrscheinlichkeit war 35 %;
  der Befund ist ueberraschend und wird darum unabhaengig nachgerechnet.
- Methode: eigener Code der Leitung (RUNDE-17/routh-nachrechnung/floquet.py). Lineare Gleichungen um L4 in pulsierenden
  Koordinaten wie in der DREI-TAKT-Karte [L?], Monodromie ueber f in [0, 2 pi] mit RK4.
  - Gitter mu 0,030 bis 0,050 (Schritt 0,0005), e 0 bis 0,5 (Schritt 0,01), Schrittzahlen 2000 und 4000.
  - Stabil heisst: max |Multiplikator| <= 1 + 1e-6.
- Vorhersagen:
  - R1: Kontrolle e = 0 ergibt die Grenze zwischen 0,0385 und 0,0390 (Routh 0,03852) (98 %).
  - R2: Es gibt stabile Punkte mit mu > 0,0390 bei e > 0. Der groesste stabile mu-Wert liegt bei 0,0455 bis 0,0465, mit
    e zwischen 0,25 und 0,33 (80 %).
  - R3: Die Instabilitaetszunge ab mu ~ 0,0286 ist vorhanden; bei e = 0,1 ist sie etwa 0,023 bis 0,035 breit (85 %).

## ROHR-1 Schreibtischwert der Leitung (vor dem Lesen von arXiv:2609.26627; 2026-10-02 09:56:51 CEST)

- Finn: "thetraeder in einem rohr? prüfe das weiter".
- Vorab gerechnet aus TETRAKETTE-1-Geometrie (Kante a = 1) [ES]:
  - BC-Helix: Ecken auf Radius 3 sqrt(3)/10 = 0,5196. Kleinster umschliessender Zylinder: D/a = 1,0392.
  - Je Ecke kommen ein Tetraeder (Volumen sqrt(2)/12) und die Steighoehe 1/sqrt(10) dazu. Volumen je Laenge 0,37268.
  - Packungsdichte im engsten Zylinder: phi = 0,37268/(pi 0,27) = 0,4394.
- Vorhersage vor dem Lesen: Der Artikel nennt fuer die BC-Helix im engsten Zylinder phi ~ 0,44 bei D/a ~ 1,04 (70 %).
  Er koennte Durchmesser anders normieren, z. B. ueber die Umkugel.

### NACHRECHNUNG-ROUTH: Ergebnis (Lauf 09:55:52 bis 09:56:07, cpu6; ausgewertet 2026-10-02 09:57:34 CEST)

- R1, e = 0: stabil bis mu = 0,0385, instabil ab 0,0390. **Eingetroffen.**
- R2, Stabilisierung jenseits Routh: **Bestaetigt**, unabhaengig.
  - 34 stabile Gitterpunkte mit mu > 0,039, als schmaler Streifen von e = 0,12 (mu 0,0395) bis e = 0,28 (mu 0,0450).
  - Die vorhergesagte Lage des groessten mu (0,0455 bis 0,0465) ist knapp verfehlt: Auf dem 0,0005/0,01-Gitter liegt der
    groesste stabile Punkt bei 0,0450. Teil 2 von R2 ist damit **nicht eingetroffen**, um eine Gitterstufe.
  - Der Agent fand mit feinerem Gitter 0,04575 bei e ~ 0,29; die Streifenspitze ist schmaler als mein e-Raster.
    Ein Widerspruch ist das nicht.
- R3, Zunge bei e = 0,1: stabil nur fuer mu 0,0345 bis 0,039; die obere Zungenkante liegt bei 0,0345 (Agent 0,0344).
  **Eingetroffen.**
- Kontrollen: det(Monodromie) = 1 auf 5e-11; die Stufen 2000 und 4000 sind identisch.
- **Bedeutung:** DREI-TAKT D1a ist von einem zweiten Code bestaetigt. Ein Takt im Umlaufrhythmus (Exzentrizitaet) kann
  Trojaner bis mu ~ 0,045 halten, also etwa 17 % ueber die Routh-Grenze 0,0385 hinaus.

### ROHR-1: Artikel gelesen (PDF-Text arXiv:2609.26627v1, Leitung, 2026-10-02 09:58:56 CEST) [S]

- Untersucht: dichte Packungen regulaerer Tetraeder in Kreiszylindern fuer 1 <= D/a <= 1,21045, numerisch (HOOMD-blue,
  Kompression) und analytisch. Die Folge der Strukturen:
  1. Kantenkette bei D/a = 1
  2. Flaechen-Tetrahelix-Familie
  3. **Boerdijk-Coxeter-Helix bei D/a = 3 sqrt(3)/5 = 1,0392 mit phi = 50 sqrt(5)/(81 pi) = 0,43936**
  4. Bei demselben D/a die achirale "Maximal-Contact Dimer Chain" mit **exakt derselben Packungsdichte**. Dort liegt die
     Symmetriebrechung: chirale Schraube -> achirale Gleitspiegelung.
  5. Open Dimer Chain bis D/a ~ 1,21045
  6. Compact Dimer Chain mit phi = 0,465846
- **Vorab-Wert der Leitung eingetroffen:** phi = 0,4394 bei D/a = 1,0392. Die Rechnung ergibt algebraisch exakt
  50 sqrt(5)/(81 pi); das Durchmesser-Mass ist dasselbe.
- **Einordnung fuer Finn [H]:**
  - Die BC-Helix ist nicht "die" dichteste Rohrpackung schlechthin, sondern das Endglied der Helix-Familie bei genau einem
    Durchmesser.
  - Schon wenig weiter wird die achirale Dimerkette dichter (bis 0,4658).
  - Die Haendigkeit der Kette entsteht also durch Enge und verschwindet bei mehr Platz.

## TETRA-KLUMPEN (Leitung; Karte und Vorhersage geschrieben vor dem Code)

- Finn: "könnten tetraeder spannungen besitzen die sie miteinander koppeln? also klumpen aus tetraedern bzw weitere formen
  aus tetraedern?"
- Physik [L?]: Regulaere Tetraeder fuellen den flachen Raum nicht.
  - Fuenf um eine Kante lassen 7,36 Grad Luecke (360 - 5 x 70,53).
  - Zwanzig um einen Punkt (Ikosaeder) brauchen Radien von 0,951 statt 1.
  - Das ist "geometrische Frustration": Die Tetraeder muessen sich verzerren, und die Spannung koppelt Nachbarn. Bekannt
    aus Fluessigkeiten, Metallglaesern, Frank-Kasper-Phasen. Im gekruemmten Raum (600-Zell) verschwindet sie.
- Rechnung:
  - Lennard-Jones-Grundzustaende N = 4..26 neu per Basin-Hopping, diesmal mit Koordinaten; Energien gegen STABIL-6-8-12
    pruefen.
  - Kontaktgraph mit r < 1,2 x 2^(1/6), Tetraeder = 4er-Cliquen.
  - Dann alle Kontakte als Federn mit Ruhelaenge 1: Frustrationsenergie E_f = min Sum (L - 1)^2/2, maximale Dehnung, E_f je
    Tetraeder.
  - Kopplung ueber Spannung: Das Doppel-Ikosaeder (19) besteht aus zwei 13er-Ikosaedern, die eine 7er-Doppelpyramide
    teilen. Kopplung Delta = E_f(19) - 2 E_f(13) + E_f(7).
- Vorhersagen:
  - T1: Tetraeder (4), Doppelpyramide (5) und BC-Kettenstuecke spannungsfrei, E_f < 1e-12 (99 %).
  - T2: Fuenfer-Doppelpyramide (7) frustriert, maximale Dehnung 1 bis 4 % (85 %).
  - T3: Das 13er-Ikosaeder ist frustriert; die Speichen sind gestaucht, die Oberflaeche gedehnt (95 %).
  - T4: Kopplung Delta < 0: Zwei Ikosaeder teilen sich Spannung guenstig (55 %).
  - T5: Die magischen LJ-Groessen 7, 13, 19, 23 sind polytetraedrisch: Jedes Teilchen sitzt in mindestens einem Tetraeder
    (90 %).

### Dritte frische Lesung (v2.2-diff) und v2.3 (eingetragen 2026-10-02 10:00:48 CEST)

- Gegenleser (pruefer-opus, 09:46:40 bis 09:58:17; RUNDE-16/zwei-seiten/GEGENLESUNG-v2.2.md):
  - N1 bis N16: 14 erledigt, 2 teilweise.
  - Auflage G1: "12 Ecken nicht besonders" ist nicht belegt; richtig ist "mit dem Test nicht entscheidbar".
  - Empfehlungen:
    - G2: Ereignissuche, Schranke an die chi-Werte binden.
    - G3: a < 1,419 (nicht 1,42); das ist eine Gueltigkeitsbedingung.
    - G4: Q ~ 370 gilt fuer den Duennwand-Ast, chi(0) < 0,1, Uebergang stetig.
- **v2.3** (10:00:38): G1 bis G4 eingearbeitet. v2.2 archiviert (stand-0946). Downloads ersetzt; v2.2 war dort
  unveraendert (Hash geprueft).
- **Berichtigung TETRAKETTE-1/ERGEBNIS.md** angehaengt (Sicherung .bak-20261002).
  - Fuer 12 Ecken gilt jetzt: nicht entscheidbar.
  - Post hoc beschreibend: 12 ist in keiner Groesse der staerkste Ausreisser im Bereich 8 bis 14.
- **Selbstanzeige der Leitung:** Dieselbe Ueberdehnung stand in der Chat-Antwort an Finn ("in den Stabilitaetsgroessen
  sind 12 und 20 nicht besonders") und in RUNDE-16.md (Ernte TETRAKETTE-1, Abschaetzung). Die Berichtigung an Finn
  folgt im Chat. RUNDE-16 bleibt als Protokoll unveraendert; massgeblich ist diese Berichtigung.

- **Nachtrag post hoc (2026-10-02 10:03:02 CEST, vor dem Lauf):** Empfindlichkeitsprobe des Kontakt-Abschneidefaktors (1,10 / 1,15 / 1,20 / 1,25) fuer N = 7, 13, 19, 23 und Delta, auf den gespeicherten Koordinaten. Anlass: maximale Dehnung 9,5 % bei N = 19 deutet auf einen eingeschlossenen Langkontakt.

### TETRA-KLUMPEN: Ergebnis (Laeufe 09:59 bis 10:03, cpu6; ausgewertet 2026-10-02 10:03:28 CEST)

LJ-Grundzustaende N = 4..26 neu (400 Schritte, Seed 21). Alle Energien gleich STABIL-6-8-12, ausser N = 21: dort
0,033 hoeher, das globale Minimum wurde nicht gefunden.

| N | Tetraeder | E_f (Federn, Ruhelaenge 1) | E_f je Tetraeder | max. Dehnung | Speichen / Oberflaeche |
|---|---|---|---|---|---|
| 4 | 1 | 4e-22 | – | 0 | – |
| 5 | 2 | 4e-20 | – | 0 | – |
| 6 (Oktaeder) | **0** | 1e-19 | – | 0 | kein Tetraeder |
| 7 (Fuenfer-Doppelpyramide) | 5 | 0,00032 | 0,00006 | 1,2 % | – |
| 13 (Ikosaeder) | 20 | 0,01055 | 0,00052 | 3,6 % | -3,59 % / +1,37 % |
| 19 (Doppel-Ikosaeder) | 35 | 0,02506 | 0,00071 | 9,5 % | -3,60 % / +1,73 % |
| 23 | 47 | 0,04783 | 0,00101 | 8,4 % | 3 Zentren |
| 26 | 54 | 0,07165 | 0,00132 | 8,1 % | 3 Zentren |

- T1 eingetroffen: 4, 5 und die BC-Kette sind spannungsfrei.
- T2 eingetroffen: 7 frustriert, maximal 1,2 %.
- T3 eingetroffen: Beim Ikosaeder sind die Speichen gestaucht (-3,6 %) und die Oberflaeche gedehnt (+1,4 %).
- **T4 nicht eingetroffen:** Kopplung Delta = E_f(19) - 2 E_f(13) + E_f(7) = **+0,0043** (> 0, rund 41 % der
  Frustration eines Ikosaeders). Die Spannungen zweier Ikosaeder addieren sich also teurer als einzeln.
  - Empfindlichkeitsprobe post hoc: Bei den Abschneidefaktoren 1,10 bis 1,25 ist der Kontaktgraph identisch, Delta
    bleibt +0,00428.
- T5 eingetroffen: 7, 13, 19 und 23 sind polytetraedrisch (jedes Teilchen in Tetraedern). Ausnahme ist N = 6, das
  Oktaeder, mit keinem einzigen Tetraeder.
- **Frustration je Tetraeder waechst mit der Groesse:** 0,00006 (7), 0,00052 (13), 0,00071 (19), 0,00101 (23),
  0,00132 (26). Perfekte Tetraeder-Klumpen koennen im flachen Raum nicht beliebig wachsen. Bekannt ist, dass grosse
  LJ-Cluster in andere Ordnungen wechseln [L?].
- **Bedeutung fuer Finn [H]:** Ja, Tetraeder koppeln ueber Spannungen. Wer an einem Tetraeder zieht, verformt seine
  Nachbarn mit, und die Spannungen addieren sich mit Zuschlag (Delta > 0). Die Kette im Rohr entgeht dem ganz: Sie
  verdreht sich (BC-Helix, spannungsfrei) und wird dafuer haendig und nie periodisch.
- **Abschaetzung: weiter.** Moeglich als Naechstes:
  - Spannungsfeld zweier getrennter Klumpen ueber ein Federgitter: Anziehung oder Abstossung mit dem Abstand?
  - Dasselbe im gekruemmten Raum (600-Zell) als Nullkontrolle [L?].

### Ernte Codex: Q-Ball als Uhr (Finns Direktauftraege, Peerbus 09:46 bis 10:03 CEST; eingetragen 2026-10-02 10:30:03 CEST)

- **Q-BALL ALS DICHTEUHR:** sechs nichtlineare radiale 3D-Zeitlaeufe (l = 0), Live-Solver unveraendert. Angeregt ist die
  bekannte stille Atmungsmode (rho = 1,7446175), epsilon 0,005 und 0,02.
  - Die Dichte am Ort zeigt reproduzierbare Ticks: Periode 3,60147 (2 pi/rho = 3,601469), an vier Radien gleich.
  - Der Nullarm ohne Anregung zeigt 0 Ticks; die reine Phasendrehung erzeugt also keinen falschen Tick.
  - Energie- und Ladungsbilanz auf 6e-9 bzw. 4e-11.
  - Codex: Das ist das Auslesen einer vorbereiteten Mode, keine entstandene Uhr und keine Zeit- oder
    Gravitationsaussage.
- **QBALL-CLOCK-KICK:** Stoesse k = 0, +-0,01 und +0,05 bei T = 20.
  - Die Periode aendert sich kaum (3,60147 auf 3,60074 bei +0,05), die Phase springt (Versatz -0,026 bis -0,094 Perioden).
  - Die Bilanz mit Stossarbeit ist geschlossen. Keine Isochronie behauptet.
- **Bedeutung [H, Leitung]:** Die stille Stelle ist eine nicht abstrahlende innere Schwingung, also eine "Uhr" im
  Feldmodell. Hier treffen Finns Tick-Idee und die bewiesene BIC des Projekts zusammen. Ob die Uhr eine Stoerung "vergisst"
  (Phase) oder "behaelt" (Takt), ist mit dem Kick-Test teilweise beantwortet: Sie behaelt den Takt und verschiebt die
  Phase.

## Stand Gesamtformel am 02.10. (Leitung, Schreibtisch, 2026-10-02 10:30:46 CEST; nur Zusammenfassung des Belegten, Fortschreibung von RUNDE-12.md)

Alles "modell" (keine Messdaten), sofern nicht anders markiert.

1. **Ein Feld (U = S - S^2 + S^3/2):**
   - Unveraendert gelten die Leiter stiller Stellen, die Beweise (l = 0, n = 1 und 2; l = 1, n = 1) und die positive
     Krein-Signatur.
   - Unter schwacher Eigengravitation verschieben sich die Stellen um -0,47 bzw. -0,43 x Kompaktheit (R14/15).
   - **Neu:**
     - Die Log-Stelle (U = ln(1 + S)) ist blind und mit unabhaengigem Code auf ~1e-6 reproduziert; der Umlauf ist nur
       post hoc aufgeloest. Stille Stellen gehoeren also nicht nur zum sextischen Potential.
     - **Neu (Codex):** Die stille Atmung ist eine Uhr. Sie liefert reproduzierbare Dichte-Ticks mit der Periode
       2 pi/rho. Nach einem Stoss bleibt der Takt fast gleich, die Phase verschiebt sich.
2. **Mehrere Felder:**
   - Unveraendert: Eto/Nitta-Wirbelmesonen (Literatur), kein Y-Dreier, Z3-Regel, O(6) ohne J_ab.
   - **Neu (BEUTEL-1):** Im Zweifeldmodell psi/chi baut sich der Ball eine Huelle, bleibt aber ein Tropfen
     (E/Q -> 0,853). Das Beutelgesetz E ~ Q^(3/4) braucht freien, masselosen Inhalt.
   - Offen und laufend: STILLE-ZWEIFELD, also ob stille Stellen einen dritten Kanal ueberleben.
3. **Spin:** unveraendert. Spin 1/2 folgt nicht aus den Skalaren; mit Dirac-Kopplung gibt es Beutelniveaus.
   nicht getroffen. LLR: Modellabbildung 11 Groessenordnungen daneben (R12).
5. **Laborbruecke:** unveraendert (AFM-Kanal, Breitengesetz R13).
6. **Geometrie-Strang (Finns Arbeitsmodell, neu seit 02.10.):**
   - Stabile Zahlen sind 12 im Raum (Thomson-Ikosaeder, LJ13 = 12 + 1, fcc) und 6 in der Ebene; 8 ist es nicht, 11 ist
     anti-magisch.
   - Tetraeder-Klumpen sind frustriert. Die Spannung je Tetraeder waechst mit der Groesse, und zwei Klumpen koppeln mit
     Zuschlag (Delta > 0).
   - Die BC-Kette ist die dichteste Rohrpackung bei D/a = 3 sqrt(3)/5 ([S] arXiv:2609.26627). 11 Schritte sind fast
     4 Umlaeufe. Ob 12 Ecken in der Stabilitaet besonders sind, ist nicht entscheidbar.
   - Der Beutelexponent misst die Dimension (d/(d+1), gemessen 3,005); DIM-BEUTEL laeuft.
   - DREI-TAKT: Ein Takt rastet nur in Phase; Chaos ab drei Phasen plus Takt. Exzentrizitaet stabilisiert Trojaner bis
     mu ~ 0,045, von zwei Codes bestaetigt.
7. **Offen, nach Gewicht:**
   - M_E-G3 (Codex; Glieder 7 und 10 der Spin-2-Kette)
   - STILLE-ZWEIFELD
   - DIM-BEUTEL
   - ein zweites unabhaengiges Beweisprogramm
   - L2-Quadrupolzertifikat (Codex)
   - Restsymmetrie mit J_ab
   - Quellenpruefung Frustration (Agent laeuft)

### Ernte DIM-BEUTEL (Agent fertig ~10:50; RUNDE-16/dim-beutel/ERGEBNIS.md; ausgewertet 2026-10-02 10:49:25 CEST)

Plan eingefroren 09:59:01, nach der Karte (09:47:42). Vier Nachtraege, drei davon nach Laufbeginn (eingefroren 10:02,
10:07, 10:16, 10:21).

| Nr | Vorhersage | Ausgang |
|---|---|---|
| D1 | Kette p -> 0,50, h -> 0,50 | **eingetroffen**: p* = 0,50015, h* = 0,4982, d = 1,001 |
| D2 | Quadrat p -> 0,667, h -> 0,333 | **eingetroffen**: p* = 0,66687, h* = 0,3331, d = 2,002 |
| D3 | kubisch p -> 0,75, h -> 0,25 | **eingetroffen**: p* = 0,75114, h* = 0,2489, d = 3,02 +- 0,03 |
| D4 | Sierpinski naeher an 0,577 (d_s) als an 0,613 (d_H) | **offen**: Der Fortsetzungsast blieb in zu kleinen Beuteln haengen, das Plateau war < 1 Dekade. Nachtrag post hoc, nicht gewertet: frische selbstaehnliche Starts geben 0,575 / 0,594 / 0,577 / 0,576 (Mittel 0,581, d ~ 1,39), alle naeher an d_s |
| D5 | Abweichung bei kleinem Q; Plateau in 3D am kuerzesten | **eingetroffen** (Plateau 3,24 / 3,72 / 2,62 Dekaden; nur fuer die gewaehlten Groessen) |

- d_s des Sierpinski-Dreiecks direkt gemessen: Laplace-Zaehlung genau Faktor 3 je Faktor 5, Random Walk 0,6826, also
  d_s = 1,3652. Das bestaetigt [L?].
- **Berichtigung der Leitung:**
  - p + h = 1 ist in diesem Modell eine Identitaet (Agent, ERGEBNIS 3.1).
  - Der Huellenanteil ist darum kein zweiter, unabhaengiger Dimensionsmesser. Meine Aussagen "d = 3,005 aus p wie aus h"
    (RUNDE-16.md, Chat) zaehlen nur einmal.
  - Die eigentliche Kontrolle ist dE/dQ = omega.
- Selbstanzeigen des Agenten:
  - maxcor 20 -> 5 mitten im Lauf; die Kette wurde mit 20 nachgerechnet
  - zwei eigene Laeufe per PID gestoppt
  - eine Versionsabfrage ausserhalb kleintest (ohne Rechnung)
  - falscher d_H-Wert im Auswerteskript, vor dem gewerteten Endlauf behoben
  - arXiv HTTP 429
- **Bedeutung:**
  - Auf regulaeren Gittern misst der Beutelexponent die Dimension genau. 3/4 bzw. 4/3 sind die Unterschrift von "drei
    Raumrichtungen plus masseloser Inhalt".
  - Ob er auf Fraktalen die spektrale Dimension misst, ist offen. Der Nachtrag spricht dafuer, ist aber nicht gewertet.
- **Abschaetzung: weiter.** Gewertete Wiederholung fuer das Sierpinski-Dreieck mit frischen selbstaehnlichen Starts als
  vorab festgelegtem Verfahren; dazu ein zweites Fraktal mit anderem d_s/d_H-Paar als Unterscheidungspunkt.

## DIM-BEUTEL-2 gestartet (2026-10-02 10:50:24 CEST)

- Karte RUNDE-17/dim-beutel-2/KARTE.md (ab 10:49:36), Code-Agent auf cpu/cpu2.
- Gewertete Wiederholung fuer das Sierpinski-Dreieck mit frischen Starts als Regel, dazu das Vicsek-Fraktal mit
  groesserem Abstand d_s/d_H (p_s 0,543 gegen p_H 0,594).
- Vorhersagen:
  - E1: Sierpinski 0,577 +- 0,015 (70 %)
  - E2: Vicsek d_s 1,19 (80 %)
  - E3: Vicsek naeher an d_s (65 %)
  - E4: beide auf +-0,02 an d_s/(d_s + 1) (55 %)
- Aktive Agenten: STILLE-ZWEIFELD, Quellenpruefung Frustration, DIM-BEUTEL-2 (drei).

### Ernte Quellenpruefung Frustration (feldforscher; RUNDE-17/quellen-frustration/DOSSIER.md; ausgewertet 2026-10-02 10:53:21 CEST)

- Keine der acht Leitungsaussagen ist widerlegt.
  - Im Kern belegt [S]: 1, 2, 3, 4, 6 und 7.
  - Nur teilweise belegt: 5.
  - Ohne Quelle fuer den MIT-Beutel: 8. Belegt ist dort nur der Q-Ball mit E ~ Q^(3/4) bei Dvali/Kusenko/Shaposhnikov.
- **Berichtigung der Leitung (Abschnitt "Literatur zum Start"):**
  - Der 600-Zell-Bezug ist **belegt** [S]: Schoenhoefer u. a. 2023, arXiv:2305.07786, S. 3, nach Sadoc 2001. Die 600-Zelle
    zerfaellt in 20 Tetrahelix-Ringe aus je 30 Tetraedern.
  - Mein "nicht belegt" beruhte auf einer reinen Abstract-Suche; die Aussage steht nur im Volltext.
  - "30 Schritte ~ 11 Umlaeufe" bleibt eigene Rechnung (Kettenbruch).
- Schaerfer zu fassen:
  - (3) Frank 1952 "erklaert" die Unterkuehlung nicht. Ikosaedrische Ordnung ist laut Tarjus u. a. 2005 ein moeglicher
    Bestandteil.
  - (4) Der Wechsel ikosaedrisch -> dekaedrisch liegt bei N = 1690 (T = 0) bzw. 7440 (am Schmelzpunkt), der Wechsel
    dekaedrisch -> fcc bei 213 000 bzw. 6,67 Mio. Die magischen Zahlen 7, 13, 19, 23, 26 (29) sind aus der Tabelle von
    Wales/Doye nachgerechnet.
  - (6) Die Ikosaeder-Schale aus 12 Kugeln um eine Kugel ist **beweglich**; starr sind nur die fcc- und hcp-Schalen
    (Kusner u. a., Satz 5.2). "12 um 1" ist also Kusszahl, nicht Starrheit.
  - (5) Fuer "Raender koppeln ~ 1/d^3" ist keine Quelle gefunden. Dass isotrope Dilatationszentren im isotropen Medium
    nicht wechselwirken, folgt aus zwei belegten Formeln (Clouet; Wu/Zaiser); die Verknuepfung stammt vom Agenten.
- Folgerung des Agenten [H]:
  - Ein 13er-Klumpen mit Ikosaedersymmetrie wirkt nach aussen wie ein Dilatationszentrum und koppelt im isotropen Medium
    in erster Ordnung nicht.
  - Ein 19er (axial) kann mit ~ 1/d^3 koppeln.
  - Dazu: Das Beutelgesetz N^(d/(d+1)) gilt nur, wenn alle Quanten in einer Mode sitzen. Unsere Beutel sind kohaerente
    Einzelmoden; das passt.

## TETRA-KOPPLUNG gestartet (2026-10-02 10:54:09 CEST)

- Karte RUNDE-17/tetra-kopplung/KARTE.md (ab 10:53:21), Code-Agent auf cpu6.
- Frage: Spueren sich zwei getrennte verspannte Klumpen? Gerechnet wird mit Abstand, Richtung, Form (rund Q-A, unrund
  Q-B) und Medium (isotrop 2D, anisotrop 2D, fcc).
- Vorhersagen:
  - K1: rund im isotropen Medium kaum (< 1/d^2) (75 %)
  - K2: anisotrop 1/d^2 mit Vorzeichenwechsel (70 %)
  - K3: unrund 1/d^2 orientierungsabhaengig (80 %)
  - K4: fcc 1/d^3 mit Vorzeichenwechsel (65 %)
  - K5: unrund staerker (70 %)
- Aktive Agenten: STILLE-ZWEIFELD, DIM-BEUTEL-2, TETRA-KOPPLUNG (drei).

### Ernte STILLE-ZWEIFELD (Agent fertig ~11:10; RUNDE-17/stille-zweifeld/ERGEBNIS.md; ausgewertet 2026-10-02 11:11:27 CEST)

Plan eingefroren 10:22:44, nach der Karte (09:52:35). Nachtrag 1 eingefroren 11:03:57, nachtraeglich.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| S1 | mindestens eine stille Stelle in E1 (45 %) | **eingetroffen: 15 Stellen** bei omega^2 0,819 bis 1,159, je Umlauf +-1 auf beiden Stufen aufgeloest (Spruenge <= 0,40 rad), Lagen auf 1,3e-8 gleich |
| S2 | in E2 keine Stelle mit beiden Abstrahlungen null (90 %) | **eingetroffen, mit Vorbehalt**: kleinste Gesamtabstrahlung 1,7e-4, 78-mal ueber der vorab gefrorenen Schwelle 2,1e-6. Nicht erschoepfend (19 bzw. 8 von 74 Minima verfeinert); Minimierer gegen den Plan auf gedaempftes Gauss-Newton umgestellt |
| S3 | Funde auf dem Duennwand-Ast mit Huelle (60 %) | **eingetroffen**: alle 15 mit chi(0) <= 0,074 und omega^2 < 1,4 |
| S4 | die M1-Stelle hat keinen Nachfolger mit nur einem offenen Kanal (75 %) | **eingetroffen**: Beim Einschalten der Kopplung stirbt sie schon bei lambda = 0,05 (T = 0,037) und bleibt in E2. Nur dieser eine Weg ist gerechnet |

- Kontrollen:
  - K1: bewiesene M1-Stelle auf 5e-7, Umlauf -1 aufgeloest.
  - K2: BEUTEL-1 auf 1,5e-5.
  - K3: zwei Stufen.
  - Die Linearisierungsskizze der Leitung ist richtig; mit c' = c/2 wird sie selbstadjungiert.
- Korrektur der Karte: Fuer rho > omega + sqrt(2) oeffnet auch Kanal b. Es gibt also einen Bereich E3 mit drei offenen
  Kanaelen; dort ist T >= 0,147.
- Beobachtung der Leitung [H]: Die 15 Stellen liegen in drei Familien in rho, ~ 1,05-1,11, ~ 1,23-1,31 und ~ 1,34-1,41,
  die mit omega^2 wandern. Vermutlich sind das drei Leitern.
- Unvollstaendig: Etwa 26 Duennwand-Kandidaten unter omega^2 ~ 0,82 sind nicht bearbeitet.
- Selbstanzeigen des Agenten:
  - ein lokaler awk-Aufruf ohne Wirkung
  - eine Namensliste von fmhc-physics-remote
  - Codeaenderungen nach dem Einfrieren (Profilwaechter, Reihenfolge, fehlende Konstante)
  - Minimierer gewechselt
  - drei Laeufe per Unit-Name gestoppt
- **Bedeutung (vorab festgelegt) [H]:** Stille Stellen ueberleben im Zweifeldmodell, wenn die Huelle die Kanaele so
  schliesst, dass nur einer offen bleibt. Das waere ein neuer Mechanismus.
  - Die alte Einfeld-Stelle hat keinen Nachfolger.
  - Mit zwei offenen Kanaelen gibt es keine Stille (passt zu QK-1).
- **Abschaetzung: weiter (Schwerpunkt Q-Baelle).** Naechste Schritte:
  - (a) Blinder, unabhaengiger Nachbau von zwei oder drei der 15 Stellen, wie bei LOG-NACHBAU.
  - (b) Die restlichen Duennwand-Kandidaten bearbeiten.
  - (c) Die Familien als Leitern ordnen.
  - (d) Zeitlauf wie Codex' Q-Ball-Uhr fuer eine Stelle: Tickt der Ball mit Huelle?

## ZWEIFELD-NACHBAU gestartet (2026-10-02 11:12:34 CEST)

- Karte RUNDE-17/zweifeld-nachbau/KARTE.md (ab 11:11:49), blinder Code-Agent auf cpu3/cpu4, Zeitbox 120 min.
- Fenster omega^2 0,83 bis 0,91 in E1. Die Lagen sind dem Agenten nicht genannt.
- Versiegelte Vorhersage: sha256 0d8348cc... in VORHERSAGE.sha256.
  - Der Klartext liegt ausserhalb aller Projekt- und Agentenpfade (Memory-Bereich der Leitung, Unterordner versiegelt).
    Das ist die Lehre aus LOG-NACHBAU: Agenten teilen den Scratchpad.
  - Ein kurzzeitiges Hash-Zwischenfile lag in /tmp (System) und ist geloescht.
- Aktive Agenten: DIM-BEUTEL-2, TETRA-KOPPLUNG, ZWEIFELD-NACHBAU (drei).

### Ernte TETRA-KOPPLUNG (Agent fertig ~11:28; RUNDE-17/tetra-kopplung/ERGEBNIS.md; ausgewertet 2026-10-02 11:27:37 CEST)

| Nr | Vorhersage | Ausgang |
|---|---|---|
| K1 | rund (Q-A) im isotropen Medium: schneller als 1/d^2 | **eingetroffen**: 0,0037 cos(6 theta)/d^4 (Exponent 3,98 bis 4,03); bei d = 10 80- bis 100-mal schwaecher als Q-B. Zusatzkontrolle: elastisch isotropes Quadratgitter (k2 = 0,5) ebenfalls 1/d^4. Es kommt auf die elastische Isotropie an |
| K2 | anisotrop 2D, Q-A: 1/d^2 mit Vorzeichenwechsel | **eingetroffen**: Achse -0,0023/d^2 (Anziehung), Diagonale +0,0036/d^2 (Abstossung) |
| K3 | isotrop 2D, unrund (Q-B): 1/d^2, orientierungsabhaengig | **eingetroffen**: parallel der Laenge nach -0,0031/d^2 (Anziehung), seitlich +0,0036/d^2 (Abstossung); bei 60 Grad haben paralleles und gedrehtes Paar entgegengesetzte Vorzeichen |
| K4 | fcc, Q-A: 1/d^3 mit Vorzeichenwechsel | **offen** nach der Vorab-Regel ([111] mit zu wenigen Punkten im unteren Halbfenster). Gemessen: Exponenten 2,98 / 3,13 / 2,89; [100] zieht an, [110] und [111] stossen ab. Ein nachtraeglicher Lauf im 80^3-Gitter erfuellt alle Kriterien und aendert den Ausgang nicht |
| K5 | fcc: Q-B/Q-B staerker als Q-A/Q-A | **nicht eingetroffen**: Verhaeltnis 3,9 ([100]), 2,3 ([111]); entlang der gemeinsamen Achse [110] faellt es von 1,8 (d = 4) auf 0,51 (d = 22) |

- Kontrollen:
  - FFT-Loeser gegen spsolve, bilinear gegen vier Terme: Maschinengenauigkeit.
  - Der Untergrund der Bildquellen (1/N) musste abgezogen werden; danach sind die Werte groessenunabhaengig.
  - Fester Rand bestaetigt periodisch auf < 1 %, ausser 1/d^4 bei d ~ 20.
- Selbstanzeigen des Agenten: Teile von kleintest.sh gelesen; Code fuer den Nachtrag nach den Hauptlaeufen geaendert
  (Hauptfassung in hilfs/).
- **Bedeutung fuer Finn [H]:**
  - Spannungen koppeln verspannte Klumpen. Es ist eine Kraft aus Geometrie, nicht eingesetzt.
  - Sie wirkt aber nur, wenn Klumpen oder Medium "unrund" sind. Dann faellt sie wie 1/d^Dimension (2D: 1/d^2,
    3D: 1/d^3), mit richtungsabhaengigem Vorzeichen (Anziehung in manchen Richtungen, Abstossung in anderen).
  - Runde Klumpen im runden Medium spueren sich kaum (1/d^4 in 2D).
  - "Unrund" heisst nicht automatisch staerker.
  - Bekannte Physik [L?]: elastische Dipol-Wechselwirkung von Punktdefekten (Eshelby). Hier ist sie unabhaengig
    nachgerechnet.
- **Abschaetzung: weiter, als Werkzeug.**
  - Der Abfall-Exponent 1/d^Dimension ist ein weiterer Dimensionsmesser [H].
  - Moeglich als Naechstes: Kopplung echter Ikosaeder-Klumpen (13, 19) statt Modellquellen, und Vorzeichenkarten fuer
    Finns Formen.

### Loop-Durchgang (2026-10-02 11:53:54 CEST)

- Codex: seit 10:03 CEST still. Statusfrage zu M_E-G3 per Peerbus gesendet (kind request, Ereignis be2a6964). Ohne
  Zustellung (deliveries leer); Codex liest den Bus selbst.
- Scout 09:04Z, fuer uns einschlaegig:
  - arXiv:2610.00774, "Discrete PT-symmetric solitons on branched lattices: vertex states, stability, and vortices"
  - arXiv:2601.03189, PT-symmetrische verzweigte Gitter
  - Moeglicher Bezug zu V5/S6 [H]: Feldklumpen auf Rad- und Sterngraphen, Nabenmode nur fuer J N < 0,55 bis 0,6.
  - Abstract-Abfrage HTTP 429; in der naechsten Runde lesen.
- Agenten:
  - ZWEIFELD-NACHBAU (seit 11:12): noch kein Plan im Ordner, Herleitung laeuft vermutlich.
  - DIM-BEUTEL-2: Plan 11:04:53, Nachtrag 1 11:07:55.
- Freier Agentenplatz bewusst nicht belegt: Die Huellen-Folgearbeiten (restliche Kandidaten, Uhr mit Huelle) warten auf
  den blinden Nachbau.

### Ernte DIM-BEUTEL-2 (Agent fertig ~12:00; RUNDE-17/dim-beutel-2/ERGEBNIS.md; ausgewertet 2026-10-02 12:01:04 CEST)

Plan eingefroren 11:04:53, nach der Karte (10:49:36). Nachtraege 1 bis 7 betreffen nur den Zeitplan sowie, ab Nachtrag 4,
eine Code-Fassung mit gespeicherten Formzustaenden. Physik, Startformen, Loeser und Wertung blieben unveraendert.

| Nr | Vorhersage | Ausgang |
|---|---|---|
| E1 | Sierpinski p_per = 0,577 +- 0,015 | **eingetroffen**: 0,583 +- 0,018 (14 Ein-Perioden-Sekanten, 3,17 Perioden, Beutelradius 8 bis 74). p_s = 0,577, p_H = 0,613 |
| E2 | Vicsek d_s = 1,19 +- 0,03 | **eingetroffen**: 1,184 (Eigenwertzaehlung), 1,188 bis 1,193 (Random Walk) |
| E3 | Vicsek naeher an p_s (0,543) als an p_H (0,594) | **eingetroffen**: 0,550 +- 0,019 (13 Sekanten, 3 Perioden, Radius 8 bis 164) |
| E4 | beide auf +-0,02 an d_s/(d_s + 1) | **eingetroffen**: +0,006 und +0,007 |

- Kontrollen:
  - Zwei Generationen bis 1e-11 gleich; das prueft auch das Teilgebiet.
  - Startformen robust.
  - dE/dQ = omega bei F2 formal verfehlt: eine nicht konvergierte Stufe, Abweichung 2e-7.
- **Wichtigste Grenze (Agent):**
  - Der lokale Exponent schwankt zwischen 0,37 und 0,80. Nur die Sekante ueber volle Selbstaehnlichkeitsperioden misst
    die Dimension.
  - Gemessen wird also, dass die Beutelloesung mit der *spektralen* Skalierung selbstaehnlich ist (Energie x3 bzw. x5 je
    Periode), nicht mit der Hausdorff-Skalierung.
- **Bedeutung (vorab festgelegt):** Der Beutelexponent misst die spektrale Dimension, d_s = p/(1 - p). Er taugt als
  Dimensionsmesser fuer Graphen ohne vorgegebene Dimension, also fuer entstehende Geometrie [H, im Modell gestuetzt].
- Selbstanzeigen des Agenten: wartende Schleifen und flock-Aufrufe beendet (keine laufende Rechnung); Laeufe endeten
  11:58:45, vor der Plangrenze.
- **Abschaetzung: weiter.** Der Dimensionsmesser ist im Modell bestaetigt (regulaere Gitter und zwei Fraktale).
  Naechste Schritte:
  - Elastische Kopplung (TETRA-KOPPLUNG) auf einem Fraktal: Misst ihr Abfall d_s oder d_H?
  - Anwendung auf einen Graphen, dessen Geometrie aus einer Regel entsteht (Finns Programm) [H].

### Ernte ZWEIFELD-NACHBAU (Agent fertig ~12:42, berichtigt: zuerst falsch als ~12:58 geschaetzt statt gemessen; RUNDE-17/zweifeld-nachbau/ERGEBNIS.md; ausgewertet 2026-10-02 12:42:48 CEST)

- **Vorhersage entsiegelt:** sha256 = VORHERSAGE.sha256 = 0d8348cc..., geprueft; Klartext unveraendert seit 11:11:49.
  - Klartext: "ZWEIFELD-NACHBAU, Vorhersage der Leitung, geschrieben 2026-10-02 11:11:49 CEST, vor jedem Lauf: Im Modell M2
    (BEUTEL-1) liegen im Fenster omega^2 0,83 bis 0,91, im Bereich E1 (nur Kanal a offen), mindestens die 9 stillen
    Stellen (omega^2; rho) = (0,83578650; 1,05931135), (0,83728947; 1,24903866), (0,84015011; 1,40944022),
    (0,84743426; 1,33956049), (0,86038074; 1,27174185), (0,86085981; 1,06976351), (0,88121651; 1,39804343),
    (0,89702906; 1,30955352), (0,90096911; 1,08553960), je Umlauf +-1. Vorhersage: der blinde Nachbau findet alle 9
    auf 1e-5 (70 %); er findet genau diese 9 und keine weitere (55 %)."
- **Ausgang nach dem eingefrorenen Plan: nicht auswertbar.**
  - K1 ist verfehlt: Die gewaehlte Messgroesse W1 war die Jost-Determinante mit auslaufender Welle; ihre Phase dreht sich
    an einer stillen Stelle nicht.
  - Dadurch kein Fund.
  - Selbstanzeige des Agenten: LOG-NACHBAU hatte davor gewarnt.
- **Nachtraeglich** (Nachtraege 2 bis 4, je vor dem Lauf eingefroren, nach dem K1-Versagen, ohne Kenntnis der Ziellagen):
  - Mit W2 = s + i m_a (dem W aus LOG-NACHBAU) bestehen K1 (2e-7 / 5e-7, Umlauf aufgeloest) und K2 (1e-10, mit BEUTEL-1
    1e-8).
  - **Die blinde Suche findet genau 9 Stellen, und es sind genau die 9 versiegelten**, je auf < 1e-6:
    0,835787/1,059311; 0,837289/1,249039; 0,840150/1,409440; 0,847434/1,339560; 0,860381/1,271742; 0,860860/1,069764;
    0,881217/1,398043; 0,897029/1,309554; 0,900969/1,085540.
  - Beide Stufen stimmen auf <= 5e-9 (K3).
  - Die Umlaufzeichen sind gegenueber STILLE-ZWEIFELD bei allen neun umgekehrt. Das ist eine Konvention (Umlaufrichtung
    oder Definition von W), keine Physik [ES].
  - Fuenf steile Nulldurchgaenge wurden per Kurvenverfolgung lokalisiert (Nachtrag 4). Fuenf Zellendetektor-Kandidaten
    hatten Umlauf 0 und wurden verworfen.
- **Wertung der Leitung:**
  - Gemessen am Hauptplan nicht auswertbar.
  - Nachtraeglich sind beide Vorhersagen eingetroffen ("alle 9 auf 1e-5", "genau diese 9"), mit einem unabhaengig
    geschriebenen Code, blind gegen die Lagen. Das zaehlt als post hoc. Die Korrektur der Messgroesse folgte aus dem
    Versagen der Kontrolle K1, nicht aus dem Testfenster; das Verzerrungsrisiko ist darum klein.
  - Ich hebe den Nachtrag nicht in den Rang des Hauptplans; dafuer braeuchte es eine Fremdstimme. Zweistufige Angabe wie
    bei LOG-NACHBAU.
  - Grenze laut Agent: Beide Stufen nutzen denselben Code, und den chi-Teil prueft keine unabhaengige Kontrolle.
- Beobachtung des Agenten: Alle 9 liegen auf vier Kurven von Schwingungen des chi-Feldes. Die Leitung hatte drei
  rho-Familien vermutet; die vier chi-Moden-Kurven sind die genauere Lesart [H].
- **Abschaetzung: weiter.** Die 15 bzw. 9 Huellen-Stellen sind von zwei Codes (post hoc) getragen. Moeglich als
  Naechstes:
  - eine unabhaengige Kontrolle des chi-Teils, z. B. ein Zeitlauf mit Anregung der Mode, wie Codex' Q-Ball-Uhr
  - der Nachtrag der Kandidaten unter omega^2 0,82

## Abschaetzung Runde 17 (Leitung, 2026-10-02 12:43:12 CEST)

| Karte | Ergebnis kurz | Abschaetzung |
|---|---|---|
| NACHRECHNUNG-ROUTH | Trojaner-Stabilisierung jenseits Routh (mu bis 0,045) unabhaengig bestaetigt | erledigt; Folgekarte nur mit Literatur (Danby [L?]) |
| ROHR-1 | BC-Helix: dichteste Rohrpackung bei D/a = 3 sqrt(3)/5, phi = 50 sqrt(5)/(81 pi), exakt nachgerechnet [S] | erledigt |
| TETRA-KLUMPEN | Frustration waechst mit der Klumpengroesse; Kopplung zweier Ikosaeder mit Zuschlag (+0,0043) | weiter (mit TETRA-KOPPLUNG) |
| Quellenpruefung Frustration | 8 Aussagen geprueft, keine widerlegt; 600-Zell-Ring belegt; drei Aussagen schaerfer gefasst | erledigt |
| DIM-BEUTEL + DIM-BEUTEL-2 | Beutelexponent misst d (Gitter) bzw. d_s (Fraktale), alle Vorhersagen eingetroffen (Sierpinski 0,583, Vicsek 0,550) | weiter: Anwendung auf einen wachsenden Graphen |
| TETRA-KOPPLUNG | Kopplung nur bei "unrund" (Klumpen oder Medium), Abfall 1/d^Dim, Vorzeichen richtungsabhaengig | weiter (Fraktal, echte Ikosaeder) |
| STILLE-ZWEIFELD | 15 stille Stellen mit Huelle (E1); keine in E2; die M1-Stelle stirbt | weiter (Schwerpunkt Q-Baelle) |
| ZWEIFELD-NACHBAU | Hauptplan nicht auswertbar (K1); post hoc genau die 9 versiegelten Stellen blind gefunden | weiter: chi-Teil unabhaengig pruefen (Zeitlauf) |
| Codex Q-Ball-Uhr | Die stille Atmung tickt mit 2 pi/rho; Stoss verschiebt die Phase, nicht den Takt | weiter (Uhr mit Huelle, falls Finn will) |
| v2.3 (Finns Arbeitsmodell) | drei frische Lesungen, alle Auflagen erledigt | erledigt, bis Finn weiterschreibt |
| M_E-G3 (Codex) | offen, Statusfrage gestellt | in Runde 18 uebernommen |

**Lehren der Runde:**
- (1) Zweimal blieb ein blinder Nachbau an der Messgroesse haengen (Umlauf), obwohl die Warnung im Vorlaeufer stand.
  Kuenftig gehoert die Messgroesse mit Begruendung in die Karte, nicht nur das Kriterium.
- (2) Eine Abstract-Suche reicht nicht fuer "nicht belegt" (600-Zell-Ring); erst der Volltext entscheidet.
- (3) "Nicht entscheidbar" ist ein eigener Ausgang und muss so benannt werden (12 Ecken, dritte frische Lesung).
- (4) Selbstanzeigen dieser Runde:
  - Agenten: awk, Codeaenderungen nach dem Einfrieren, Prozessabbrueche per PID bzw. Unit-Name, Lesen von kleintest.sh.
  - Leitung: Hash-Zwischenfile in /tmp.

## Einfach gesagt (Runde 17)

Ein Q-Ball mit Huelle kann auf viele Arten schwingen, ohne Wellen abzugeben. Ein Programm fand 15 solcher stillen
Schwingungen, und ein zweites, unabhaengig geschriebenes Programm fand blind genau die neun, die im gemeinsamen
Suchfenster liegen. Ausserdem wissen wir jetzt, dass man mit einem Beutel voller Wellen die Dimension eines Netzes messen
kann, sogar bei Fraktalen. Und verspannte Tetraeder-Klumpen spueren sich ueber ihre Spannung nur, wenn etwas an ihnen oder
ihrer Umgebung unrund ist.

## Rundenabschluss (Leitung, 2026-10-02 12:43:44 CEST)

- Journal: claude-runde-v3-17-20261002, Index nr 554; pruefen ohne Befund; r16-Sicherung endete mit rc = 0; Quellen-Hashes in
  RUNDE-17/journal-quellen.txt.
- Sicherung .69 -> TS440 gestartet (ohne --delete, nice/ionice), Log /home/fmh/sicherung-dot69-ts440-lauf-20261002-r17.log.
- In Runde 18 uebernommen:
  - M_E-G3 (Codex)
  - chi-Teil der Huellen-Stellen unabhaengig pruefen, z. B. Zeitlauf
  - Kandidaten unter omega^2 0,82
  - Dimensionsmesser auf einem wachsenden Graphen
  - Arbeiten zu Solitonen auf verzweigten Gittern (arXiv:2610.00774, 2601.03189) lesen
