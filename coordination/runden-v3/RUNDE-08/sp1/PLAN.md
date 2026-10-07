# Runde 8, Karte SP-1: Stille Stellen fuer l > 0 (Plan und Erwartung vor dem Rechnen)

- Bearbeiter: Anthropic-Code-Agent (Opus), Auftrag der Leitung. Explorativ, v3.
- Beginn 2026-09-30 06:36:11 CEST (date). Diese Datei begonnen 2026-09-30 06:42:28 CEST (date), **vor jeder Code-Aenderung
  und vor jedem Lauf** (auch vor dem Rauchtest).
- **Blindheit:** Nicht geoeffnet: RUNDE-08/VORHERSAGEN-SP1.md, RUNDE-08/VORHERSAGEN-BIC3.md,
  RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md und RUNDE-08.md ab Zeile 91 bis 151 (R5F-b, Chem 14, blinde BIC-3-Vorhersagen).
  Gelesen: RUNDE-07.md (BIC-2), RUNDE-08.md Zeilen 1 bis 90 und 152 bis 181 (l = 0-Ergebnisse), bic2/PLAN.md,
  bic2.py, die V6-Laeufe auf der .69 (aus-pole-l1*). Bekannt ist mir also nur die V6-Vorhersage "0,75 +- 0,02" und
  ihr Ausgang (Minimum nahe 0,7554), beides aus dem Auftrag.
- Neue Deutungen sind Hypothesen **[H]**. Zahlen mit **[Hand]** sind von Hand gerechnet.

## 1. Code (Version 3)

- Die Gleichungen in bic2.py sind schon fuer jedes nu = l + 1 geschrieben (dim = 3):
  - Fliehkraftterm c_nu/r^2 mit c_nu = nu (nu - 1) = l (l + 1) in beiden Kanaelen (rk4_schritt, direkt_m)
  - Reihe am Ursprung U, V ~ r^nu (reg_start, direkt_m)
  - auslaufende und abklingende Loesung mit der abbrechenden Hankel-Reihe (hankel, fuer ganzzahliges nu exakt)
  - pole benutzt das schon (nus = l + 1).
- exakt und kurve uebergeben bisher fest nu = 1.0 (etwa 14 Stellen, auch in umlauf_rechteck und umlauf_neu_gelegt).
- Aenderung: nu = l + 1.0 an allen diesen Stellen, l aus --l.
  - --l bleibt fuer pole, zeitlin und bruecke eine Liste mit Vorgabe 0,1,2 (Argumente-JSON bleibt gleich).
  - exakt und kurve nehmen genau einen Wert; ohne --l gilt l = 0.
  - Fuer l = 0 ist nu = 0 + 1.0 = 1.0 bitgleich, der Rechenweg also unveraendert. Die Kopfzeile des Berichts bekommt
    ", l = ..." nur fuer l > 0; der Bericht fuer l = 0 bleibt zeichengleich (bis auf Zeiten).
  - Die Vorgaben von exakt (--x0, --rho0, --drho, --cgam) gelten fuer l = 0, beta = 0,5. Fuer l > 0 muessen sie
    angegeben werden.
- Nicht geaendert: Profile, Gitter, Newton, W, Umlauf, Fit, neu legen, Sicherheitsnetz.
- Hinweis: Das gemeldete "Kernwachstum" enthaelt den Potenzfaktor (r_m/h)^(l+1) aus dem Start r^(l+1). Fuer l = 1
  und 2 ist es darum um (r_m/h)^l groesser als fuer l = 0, ohne dass die Rechnung schlechter wird [Hand].

## 2. Pruefungen

- **P0 (l = 0 bitgleich):**
  - lokal: rauch mit Version 2 und Version 3, Berichte vergleichen (rauch rechnet pole, exakt, kurve mit l = 0)
  - .69: kurve mit denselben Argumenten wie lauf-69/aus-kurve-050-dicht (beta 0,5, xmin 0,555, xmax 0,645, dx 0,01,
    h 0,02; wegen --abstand 0,12 werden daraus 0,62 / 0,63 / 0,64 wie im Auftragsbeispiel). Alle gedruckten Zahlen
    gleich, nur Zeiten verschieden.
- **P1 (l = 1 trifft V6):** kurve --l 1 --h 0,01 bei 0,72 / 0,75 / 0,755 / 0,76. Pole bei 0,72 und 0,75 gegen
  V6 (pole, h = 0,01): 1,7855450099 - 1,698e-3 i und 1,8210850747 - 2,037e-5 i.

## 3. Laeufe (.69, kleintest.sh, Spuren cpu und cpu2, je hoechstens 10 min)

- (a) exakt --l 1 --h 0,01 um die Stelle; Keim rho0 = Re rho(0,755) + 1,17 (x0 - 0,755); Rechteck um den Fit (exakt
  legt es selbst neu, wenn der Fit-Mittelpunkt ausserhalb liegt).
- (b) kurve --l 1 --h 0,02 ueber 0,58 bis 0,75, dx 0,005 unter 0,68, darueber 0,01, in Teilen; --abstand 0,05.
- (c) kurve --l 2 --h 0,02 ueber 0,55 bis 0,95, dx 0,01, in vier Teilen; --abstand 0,05.
- (d) exakt an jeder gefundenen Stelle (h = 0,01, 9 Profile).

## 4. Erwartung vor dem Rechnen (eigene Schaetzung, vor jedem Lauf)

Grundlage [Hand]: Die l = 0-Folge bei beta = 0,5 hat in 1/(x - 0,5) die Schritte 2,04 / 2,21 / 2,25 / 2,27. Die
erste l = 1-Stelle liegt bei 1/(x - 0,5) = 3,91, also 0,55 ueber der ersten l = 0-Stelle (3,36). Bild [H]: Die
auslaufende Welle schwingt ueber den Ball, und die Kopplung verschwindet, wenn das Ueberlappintegral null wird
(Formfaktor). Der Ballradius waechst etwa wie 1/(x - 0,5). Dann hat jedes l eine eigene Folge mit aehnlichem Schritt.

- **E1 (a), l = 1 nahe 0,7556:**
  - Umlaufzahl +-1 auf beiden Rechtecken, aufgeloest: 85 %.
  - Lage omega*^2 = 0,7557 +- 0,0003, rho* = 1,8277 +- 0,0006 [Hand: 1,82693 + 1,17 x 0,0007].
  - Vorzeichen -1 wie die oberste l = 0-Stelle bei allen fuenf beta: 55 % (fast Muenzwurf).
- **E2 (b), l = 1 unterhalb 0,7554:** Vorzeichenwechsel von s nach der l = 0-Schrittregel (Schritt 2,0 bis 2,3):
  - n = 2 bei 1/(x - 0,5) = 6,0 +- 0,4, also x = 0,667 (0,661 bis 0,672)
  - n = 3 bei 8,2 +- 0,6, also x = 0,622 (0,615 bis 0,630)
  - n = 4 bei 10,5 +- 0,8, also x = 0,595 (0,589 bis 0,603)
  - n = 5 bei 12,8 +- 1,0, also x = 0,578, am Rand oder knapp unter dem Scan
  - Umlaufzahlen wechseln von Stelle zu Stelle das Vorzeichen.
  - Mindestens zwei Vorzeichenwechsel in 0,58 bis 0,75: 70 %. Keiner: 10 %.
- **E3 (c), l = 2:**
  - Der Ast nahe 1 + omega liegt nur unterhalb einer Schwelle x_c im Fenster (1 - omega, 1 + omega) [H]: Mit
    wachsendem l liegt der Zustand des geschlossenen Kanals naeher an 1 + omega (l = 0: 0,15 darunter bei 0,798;
    l = 1: 0,04 darunter bei 0,756). Fuer l = 2 braucht er einen groesseren Ball. x_c grob 0,70 (0,62 bis 0,80).
  - Falls der Ast existiert: erste (oberste) Stelle bei 1/(x - 0,5) = 4,5 bis 5,0 (x = 0,70 bis 0,72), sofern
    unter x_c. Danach im Schritt etwa 2,2: bei 0,645, 0,610 und 0,590, je +- 0,01.
  - Mindestens ein Vorzeichenwechsel in 0,55 bis 0,95: 60 %. Oberhalb 0,80 keiner: 80 %.
- **E4 (P1):** kurve-Pole bei 0,72 und 0,75 treffen V6 auf 1e-7 in Re rho und 1 % in Gamma: 95 %.
- **E5 (P0):** Fuer l = 0 sind alle gedruckten Zahlen gleich: 99 %.
- Gefahr: Unter etwa 0,6 wird der Ball duennwandig. Dort waechst das Kernwachstum, und die Astverfolgung kann
  zwischen zwei Resonanzen springen (bekannt von l = 0 bei 0,555 bis 0,58).

## 5. Belegstufen (wie RUNDE-07, BIC-2)

- **exakt (Umlauf):** Umlaufzahl +-1 auf einem Rechteck, das den Fit-Mittelpunkt enthaelt, groesster Phasensprung
  < 0,4 rad. Numerische Evidenz im radialen linearen Modell mit abgeschnittenem Rand, kein Beweis.
- **Umlauf, nicht aufgeloest:** +-1, aber Phasensprung >= 0,4 rad.
- **Vorzeichenwechsel:** Wechsel von s in kurve, Feinverfahren mit |Im Pol| < 1e-8.
- **Minimum:** nur kleine Breite ohne Vorzeichenwechsel oder Umlaufzahl. Dann schreibe ich "Minimum", nicht "null".
- Nicht gesehene Stellen heissen "nicht gesehen", nicht "gibt es nicht".

## Nachtrag 2026-09-30 07:14:50 CEST (date), vor Lauf F (kurve l = 1 unter 0,58)

- Stand: l = 1 hat Vorzeichenwechsel bzw. Umlauf bei 0,754504 / 0,660280 / 0,617105 / 0,592243. In 1/(x - 0,5) sind
  das 3,9292 / 6,2391 / 8,5393 / 10,8409, Schritte 2,310 / 2,300 / 2,302 [Hand, bc].
- Vorhersage fuer n = 5 aus konstantem Schritt 2,30 +- 0,05: 1/(x - 0,5) = 13,14 +- 0,05, also
  omega*^2 = 0,57609 +- 0,0003. Umlauf -1 (Wechsel der Vorzeichenfolge).
- Kann scheitern: kein Vorzeichenwechsel zwischen 0,565 und 0,585, oder einer ausserhalb 0,5758 bis 0,5764.
- Ausserdem gilt ab hier: Die Lage in E1 (0,7557 +- 0,0003) ist verfehlt; die Stelle liegt bei 0,754504 (Lauf sp1a).

## Nachtrag 2026-09-30 07:26:25 CEST (date), vor den Laeufen G und H (l = 2)

- Stand: kurve l = 2 (Lauf c1, h = 0,02) hat Vorzeichenwechsel bei 0,585395 und 0,606980; 1/(x - 0,5) = 11,710 und
  9,348, Schritt 2,363. s ist bei 0,57 fast null (-2,5e-5), bei 0,56 und 0,58 aber negativ (-2,0e-3, -5,9e-3).
- Erwartung:
  - Umlauf an beiden Stellen +-1 mit entgegengesetztem Vorzeichen: 0,585395 +1 (s steigt von - nach +),
    0,606980 -1 (s faellt).
  - Naechste Stelle darueber bei 1/(x - 0,5) = 7,01 +- 0,1, also 0,6427 +- 0,002, also zwischen den Laeufen c1 (bis
    0,64) und c2 (ab 0,65). Danach 4,67 +- 0,2, also 0,714 +- 0,01 (Lauf c2).
  - Bei 0,571 (Schritt nach unten) liegt nach der Regel eine Stelle. Weil s bei 0,56 und 0,58 dasselbe Vorzeichen hat,
    sehe ich dort im Feinscan 0,562 bis 0,580 entweder zwei Wechsel (Paar) oder keinen (Beruehrung). Eine einzelne
    Stelle waere mit den Vorzeichen nicht vertraeglich, solange der Ast derselbe ist. Unsicher: Duennwand-Bereich.
