# PLAN HUELLEN-LEITER-2 (Runde 19)

- Code-Agent, Start 2026-10-02 15:14:36 CEST (date). Plan geschrieben ab 15:32:21 CEST (date), vor jedem .69-Lauf.
- Verbindlich aus der Karte: stabilisierte Kopplung, Kontrolle K0, Suchbereich R 39 bis 46, vorhergesagte Sprossen,
  P0 bis P4, Bedeutung. Nichts davon wird nach dem Ergebnis geaendert.
- Gelesen: KARTE; RUNDE-18/huellen-leiter: ERGEBNIS, PLAN.md.eingefroren, PLAN-NACHTRAG-1 bis 4, code/ (huellen_leiter.py,
  auswertung.py, stille3.py), aus/ (zeilen.json, laeufe/stellen.json, prof-st*/profile-info.json, Logs).
- Code: code/huellen_leiter2.py = huellen_leiter.py der Runde 18 (Endfassung 68c0a1fb...) plus stabilisierte Kopplung
  (Klasse PotStab ersetzt S3.Pot), Befehl k0newton, Zwischendatei je Prozess beim Schreiben. code/auswertung2.py = neue
  Auswertung auf Grundlage von auswertung.py (782058b1...), Stellenregel unveraendert. code/stille3.py (Code 1) und
  code/beutel.py unveraendert (1d15a38c..., f831e818...).
- Zeilen: dieselbe Zeilenliste wie Runde 18 (ref/zeilen-r18.json), hier die Zeilen 0 bis 125 (hilfs/zeilen-126.json).

## 1 Stabilisierte Kopplung (verbindlich) und Behandlung der uebrigen g-Terme

- Linearisierung (Code 1, Klasse Pot, Kanaele a, b, c' = c/2), Modell M2 (lam = 1, cpot = 1/4), S = f^2, g = chi:
  - M_aa = U_S + S U_SS mit U_S = 1 + g^2 - 2 S + 1,5 S^2; M_ab = S U_SS (ohne g);
  - M_ac = f U_Sg = 2 f g: die Kopplung (g f c in den a/b-Gleichungen, 4 g f (a + b) in der c-Gleichung; nach c' = c/2
    symmetrisch 2 f g in beiden);
  - M_cc = U_chichi = 3 g^2 - 1 + 2 S.
  - Energien (w +- rho)^2, rho^2 und die Massen draussen haengen nicht von g ab.
- **Stabilisierung:** g_s = 0 an allen Gitterpunkten mit g < 1e-12 (auch negative Rundungswerte; exakt ist chi > 0),
  sonst g_s = g. Alle vier Matrixelemente werden mit g_s gebildet (Linearisierung um einen Hintergrund, der dort chi = 0
  hat). Der Hintergrund selbst (Profil f, g, Q, E, R) bleibt unveraendert.
- **Pruefung der uebrigen Terme:** g geht in M_aa und M_cc nur als g^2 ein. Fuer g < 1e-12 ist g^2 < 1e-24, weit unter
  einem halben ulp der O(1)-Summanden (1 in U_S, -1 in 3 g^2 - 1; ulp/2 = 1,1e-16). In double gilt dort 1 + g^2 = 1 und
  3 g^2 - 1 = -1 exakt; diese Terme tragen ausserdem kein Vorzeichen von g. Also aendert die Stabilisierung bitweise
  nur M_ac. Der Code zaehlt je Lauf die bitweise geaenderten Elemente je Matrix gegen die alte Fassung (erwartet:
  aa = ab = cc = 0; ac = Zahl der maskierten Punkte mit g != 0). Ein Wert != 0 bei aa, ab oder cc wird berichtet und als
  Programmfehler behandelt.
- **Wo die Stabilisierung wirkt:** chi(0) faellt wie e^(-1,15 R); chi(0) < 1e-12 ab Zeile 85 (omega^2 = 0,780818,
  R = 26,33). Davor gibt es keinen maskierten Punkt, die Rechnung ist bitgleich mit Runde 18. Betroffen sind die
  bekannten Stellen ab Nr. 42 (Paar 85, R = 26,71), 47 von 88.

## 2 Erwartung vorab (Schreibtisch, [H], nicht gerechnet)

- s = m_ac auf m_bc = 0 haengt von der Basis der regulaeren Loesungen ab. Ueber M_ac nimmt Y_c (Start e_c) einen Anteil
  der im Inneren wachsenden a/b-Mode (~e^(1,8 r)) auf. Das wirkt wie Y_c -> Y_c + delta Y_b: m_bc bleibt, s wird auf der
  Kurve mit (1 + delta lambda) multipliziert (lambda = Verhaeltnis der Zeilen b und c von G auf der Kurve). Nullstellen
  von s laengs der Kurve (die stillen Stellen, Rang G <= 1) bleiben; das Vorzeichen des Faktors legt das Vorzeichen von s
  und damit den Umlauf fest.
- Alter Code: delta = exakter Anteil (positiv) plus ab R ~ 32 bis 40 Rundungsanteile mit zufaelligem Vorzeichen ->
  gemeinsame Vorzeichenwechsel aller Kurven. Neuer Code: delta nur aus g >= 1e-12, positiv -> Vorzeichen wieder
  bestimmt.
- Erwartet: (a) Newton-Lagen der stillen Stellen alt gegen neu gleich (<= 1e-10); (b) Umlauf gleich; (c) die
  interpolierte Lage (Unterzeilen und zwei Halbierungen) ist fuer R < 26,3 bitgleich, fuer R > 26,3 kann sie sich
  bis ~5e-8 in omega^2 und rho verschieben, weil der Faktor ueber eine Klammer (1/32 Zeilenabstand, ~0,016 in R) um ~1 %
  variiert. Das verschiebt den interpolierten Nullpunkt in der Klammer, nicht die stille Stelle.

## 3 K0 (verbindlich, vor allem anderen)

- **Lauf:** dieselbe Kette wie Runde 18 (Zeilen 0 bis 110, Paare 0 bis 109, beide Stufen, Illinois nach Nachtrag 1 der
  Runde 18 von Anfang an, Endfassung des Verfahrens), mit stabilisierter Kopplung.
- **Bestanden, wenn alle drei gelten:**
  - K0a: Stellenregel der Runde 18 liefert in den Paaren 0 bis 109 genau 88 gezaehlte Stellen, eins zu eins den 88 der
    Runde 18 zugeordnet ueber (Paar i, Kurve k); keine zusaetzliche, keine fehlende, kein fehlendes Paar.
  - K0b: Zellen-Umlauf auf beiden Stufen gleich wie in Runde 18 (88 von 88).
  - K0c, Lage: Newton-Wurzel von W = m_ac + i m_bc (Code 1, newton_E1; das ist die stille Stelle selbst, Rang G <= 1),
    je Stelle und Stufe zweimal gerechnet, mit alter und mit stabilisierter Kopplung, gleicher Start (Lage der Runde 18
    auf dieser Stufe), gleiches Ankerprofil (naechste Zeile mit omega^2 <= Start). Beide Newton-Laeufe konvergiert und
    |d omega^2| <= 1e-8 und |d rho| <= 1e-8, alle 88 Stellen, beide Stufen. Konvergiert der Newton mit alter Kopplung
    an einer Stelle nicht, ist die Lage dort nicht geprueft und K0 nicht bestanden.
- **Begruendung der Lagegroesse (Abweichung von "Lage aus Halbierung", vor dem Lauf):** Die interpolierte Lage ist der
  Nullpunkt einer linearen Interpolation von s zwischen den Klammerenden. Die Stabilisierung multipliziert s mit einem
  glatten positiven Faktor (Abschnitt 2) und kann diesen Punkt in der Klammer verschieben, ohne die stille Stelle zu
  bewegen. Der Interpolationsfehler der Runde 18 gegen Newton war bis 8,9e-7 (L1) und 2,1e-8 (Stichprobe bei R ~ 37),
  also nicht kleiner als die Toleranz. Die Newton-Wurzel prueft die Lage der stillen Stelle selbst auf 1e-8.
- **Zusaetzlich berichtet (kein Kriterium):** interpolierte Lage neu gegen Runde 18 je Stelle (max |d|, Zahl bitgleich,
  Zahl <= 1e-8), Zeilenvergleich (Zahl, Lage, Vorzeichen der Nullstellen von m_bc je Zeile auf beiden Stufen),
  Zaehler der geaenderten Matrixelemente.
- **K0 nicht bestanden:** Abbruch. Der Suchbereich wird nicht ausgewertet (P1 bis P4 offen), Bericht.
- **Reihenfolge:** Die K0-Auftraege stehen auf jeder Spur vorn; Auftraege fuer den Suchbereich stehen dahinter. Ihre
  Ausgaben sehe ich erst nach der K0-Auswertung an.

## 4 Hintergrund und Abbildung R <-> omega^2

- Profile wie Runde 18 (Saat BEUTEL-1 bei Q = 200, Fortsetzung, Stufe 1 hp = 0,01, Stufe 2 hp = 0,005), Zeilen 0 bis 125.
- Pruefung: |dQ/Q| und |dE/E| <= 1e-6 zwischen den Stufen und Newton konvergiert, berichtet fuer alle Zeilen und
  getrennt fuer die neuen (R >= 38,9). Vergleich mit profile-info der Runde 18 (bitgleich erwartet).
- R = Radius der chi = 1/2-Kreuzung (r_chi der Runde 18, lineare Interpolation auf dem Profilgitter). Berichtet: Tabelle
  omega^2, R (beide Stufen) der Zeilen 108 bis 125, Abweichung von der Zeilenformel R ~ 1,3736/(omega^2 - 0,7281) + 0,55,
  und die vorhergesagten R als omega^2 (lineare Interpolation in der Zeilentabelle).

## 5 Suche im Suchbereich

- Paare 110 bis 123 (Zeilen 110 bis 124), R = 38,95 bis 45,98, beide Stufen, dieselbe Kette (Zeilen, Rang, Unterzeilen,
  zwei Halbierungen), stabilisierte Kopplung.
- Stellenregel unveraendert (Runde 18 PLAN 4): Vorzeichenwechsel von s auf Kurve k, auf beiden Stufen im selben Paar und
  auf derselben Kurve, Lage in omega^2 auf 1/16 des Zeilenabstands gleich, Zellen-Umlauf +-1 auf beiden Stufen gleich,
  ohne Merker (weg, steig, rangsprung, umlauf0). Stellen nur einer Stufe oder mit Merker werden getrennt gelistet.
- Kurvenindex k = Rang der Nullstelle von m_bc von unten. Geburt der Kurve k = erste Zeile mit k + 1 Nullstellen.
- **Stichprobe Rechteck-Umlauf** (Code 1: newton_E1, umlauf_mit_rueckfall, Halbbreite wie Runde 18; stabilisierte
  Kopplung; beide Stufen), Reihenfolge: die ersten zwei neuen Stellen auf k = 0 bis 3 (die P1-Stellen, bis zu 8), dann
  die erste Stelle jeder Kurve k >= 10, dann je Kurve k = 4 bis 9 die neue Stelle mit groesstem R. Mindestens 8 Stellen
  (wenn es 8 gibt). Prueft Rechteck-Umlauf = Zellen-Umlauf; bei Abweichung Bericht, Zaehlung dann vorlaeufig.

## 6 Wertung P0 bis P4 (vorab operationalisiert)

- **P0:** eingetroffen, wenn K0 bestanden (Abschnitt 3).
- **P1:** Fuer k = 0 bis 3 die ersten zwei neuen gezaehlten Stellen (Paare 110 bis 123, nach R steigend) gegen die
  ersten zwei vorhergesagten R der Karte. Treffer: |R_gefunden - R_vorhergesagt| <= 0,10 (R der Stufe 1). Eingetroffen
  bei 8 von 8 Treffern; eine fehlende Stelle ist kein Treffer. Berichtet: alle Abweichungen, max |Abweichung| (Karte:
  > 0,3 = deutlich verfehlt), dazu die dritte vorhergesagte Sprosse (kein Kriterium).
- **P2:** Je Kurve mit neuen Stellen die Folge: letzte gezaehlte Stelle der Runde 18 auf dieser Kurve (falls vorhanden),
  dann die neuen Stellen nach R steigend. Eingetroffen, wenn der Umlauf in jeder Folge bei jedem Schritt das Vorzeichen
  wechselt. Offen, wenn es keine neue Stelle gibt.
- **P3:** Lesart: "beginnt" = erste stille Stelle auf k = 10. Grund: Der Bezugspunkt der Karte, "k = 9 bei 37,65", ist
  die erste Stelle von k = 9 (ihre Geburt lag bei 35,93). Eingetroffen, wenn die erste gezaehlte Stelle auf k = 10 bei
  R in [40,5; 42,5] liegt; sonst (auch ohne Stelle auf k = 10 im Bereich) nicht eingetroffen. Berichtet zusaetzlich:
  Geburt von k = 10 (erste Zeile mit 11 Nullstellen).
- **P4:** Eingetroffen, wenn in allen Paaren 110 bis 123 auf beiden Stufen gilt: (a) kein Unterzeilen-Intervall, in dem
  alle Kurven (mindestens 2) zugleich das Vorzeichen von s wechseln, und (b) je Kurve Zahl der Wechsel ueber die
  Unterzeilen = Zahl der Wechsel zwischen den beiden Zeilen (so wie in Runde 18 bis Paar 109). Sonst nicht eingetroffen.
  Berichtet: Wechsel fein/zeile je Paar, Stellen nur einer Stufe.
- **Bedeutung:** woertlich nach Karte (P1 und P2 eingetroffen: Leiter setzt sich regelmaessig fort, stuetzt den
  Mechanismus [H]; P1 deutlich verfehlt (> 0,3): Regel gilt nur im bisherigen Bereich, Grund suchen).

## 7 Laeufe (.69, kleintest.sh, Spuren cpu, cpu2, cpu3, cpu4; je <= 600 s)

- Ordner /home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2/ (code/, hilfs/, aus/, logs/), alle Pfade absolut.
- V0: py_compile; Zeilenliste (liste) gegen ref/zeilen-r18.json (sha256 der w2-Liste). V1: Profile Stufe 1 und 2.
- V2 (K0): Bloecke der Kette fuer Zeilen 0 bis 110 (Stufen getrennt, auf die Spuren verteilt) und k0newton (88 Stellen,
  beide Stufen, in Teilen). V3: Bloecke Zeilen 110 bis 124 (hinter V2 auf denselben Spuren).
- V4: K0-Auswertung (auswertung2.py k0). Nur wenn bestanden: Auswertung des Suchbereichs (neu), Rechteck-Stichprobe
  (umlauf), Abgleich (umlaufabgleich).
- Zeitnot: Vorrang K0, dann Suchbereich auf beiden Stufen, dann 8 Stichproben, dann weitere.
- Programmfehler werden behoben und mit sha256 dokumentiert; das Verfahren bleibt. Nachtraege nur eingefroren
  (PLAN-NACHTRAG-n.md.eingefroren-*), als nachtraeglich markiert.
