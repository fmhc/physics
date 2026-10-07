# UEBERGABE-KONFLUENZ-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 48)

- Karte KARTE.md bindend (UK0 bis UK4, Wortlaut, Wahrscheinlichkeiten und Bedeutung unveraendert). Plan PLAN.md,
  eingefroren 2026-10-05 11:43:30 CEST (PLAN.md.eingefroren-20261005-114330).
- Alle Zahlen sind synthetische Gitterrechnungen auf der .69 (Python 3.12.3, numpy 2.4.4, scipy 1.18.0, 1 Thread je
  Lauf), keine Messdaten.
- **Kennzeichen:** [E] hier gerechnet, [M] Mathematik (vorab ableitbar, nicht gegengelesen), [P] Projektdatei,
  [F] Festlegung im Plan, [H] Hypothese oder Lesart, [N] Nachtrag nach Sicht (beschreibend, kein Urteil).
- **Begriffe:**
  - Faelle: Zwei Flaechen X, Y eines Glasnetzes N = 128 werden durch eine kleine Eckverschiebung des Hintergrunds
    gleichzeitig nicht lokal Delaunay (mu = -1e-3).
  - Arten: T = gemeinsames Tetraeder; K = gemeinsame Flaechenkante ohne gemeinsames Tetraeder; D = Traeger ohne
    gemeinsame Ecke (Kontrolle).
  - XY bzw. YX: erst X bzw. erst Y umklappen, danach "umklappen bis Delaunay".
  - Lesart R: Laengen und Raten stetig, orthogonale Projektion auf die neue Zwangsflaeche. Lesart P: Impulse stetig
    (Null-Fortsetzung). Beides td.abbilden unveraendert. Skalar: R = dphi/dt stetig, P = pi stetig.
  - Formen: A1 (J = 1), A2 (Kartenformel, Masse ~ Volumen) = Form A; A2L (Lund-Regge-artig) = Form B.
  - Delta_s = ||u_XY - u_YX|| / max(||u_XY||, ||u_YX||) je Sektor; q = S x, p = S y im Kantenraum.
    "Rundung" heisst hier: Abstaende von 1e-17 bis 1e-13.

## 1. Zeiten und Laeufe

- **Ablauf (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 11:21:14 CEST. Code kopiert 11:33:19. Plantext ab 11:40:32.
  - Rauchtests r1 bis r7: 09:37:25 bis 09:43:15 UTC (p4000a), alle rc = 0 (PLAN 11).
  - Eingefroren 11:43:30 CEST: PLAN (sha256 827a13b3...), code/konfluenz.py (56f9a6f0...), code/kette.sh
    (53876c6d...). Die Vorlagemodule sind unveraendert (td.py fbc02c48..., hm_td.py c62c15ab..., tg.py, uk.py, tu.py,
    tp.py, ew.py, mn.py, tg_auswertung.py). Liste in EINGEFROREN-SHA256.txt. Auf der .69 dieselben Summen
    (EINGEFROREN-SHA256-69.txt, 09:43:36 UTC).
  - Hauptlaeufe 09:43:40 bis 09:47:35 UTC, Abschluss (haeufigkeit, auswertung, tabellen, Pruefsummen) 09:47:41 bis
    09:47:45 UTC. lauf-69/PRUEFSUMMEN.txt lokal: 0 Abweichungen.
  - Nachtraege [N] 09:50:19 bis 09:53:04 UTC; nachtrag-69/PRUEFSUMMEN-2.txt lokal: 17 von 17 gleich.
  - Text ab 11:54:15 CEST. Abschluss siehe Dateiende.
- **Laeufe** (`bash kleintest.sh <Spur> <Name> code/konfluenz.py ...` im Ordner
  /home/fmh/fmhc-physics-remote/uebergabe-konfluenz-1; Laufzeit = Service runtime):

| Lauf | Spur | Aufruf | Start / Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| uk1-s1 | p4000a | lauf --saat 1 | 09:43:40 / 09:45:31 | 110,6 s | 0 |
| uk1-s2 | p4000b | lauf --saat 2 | 09:43:41 / 09:45:11 | 90,3 s | 0 |
| uk1-s3 | p4000a | lauf --saat 3 | 09:45:31 / 09:47:35 | 124,5 s | 0 |
| uk1-s4 | p4000b | lauf --saat 4 | 09:45:11 / 09:46:48 | 96,9 s | 0 |
| uk1-hf, uk1-aw, uk1-tab | p4000a | haeufigkeit (TAKT-DYNAMIK-1-Laeufe, nur lesen), auswertung, tabellen | 09:47:41 / 09:47:45 | je 1,3 bis 1,5 s | 0 |
| uk1-nt-s1 bis s4 [N] | p4000a (s1, s3), p4000b (s2, s4) | code/nachtrag_t.py <saat> 600 (nur Art T, 600 statt 80 Kandidaten) | 09:50:19 / 09:52:17 | 73,2 / 34,0 / 45,2 / 42,4 s | 0 |
| uk1-nt-aw, uk1-nt-tab, uk1-nt-zahlen [N] | p4000a | auswertung und tabellen auf nachtrag/, nachtrag_zahlen.py | 09:52:23 / 09:53:04 | <= 0,9 s | 0 |
| r1 bis r7 (Rauch) | p4000a | PLAN 11 | 09:37:25 / 09:43:15 | 0,8 bis 38,9 s | 0 |

- Zusammen 21 Aufrufe von kleintest.sh (17 auf p4000a, 4 auf p4000b), alle rc = 0. Kein Lauf ueber 600 s;
  Schlusszeit 11:00 UTC nicht erreicht.

## 2. Ergebnis zuerst

1. **Die Kombinatorik ist konfluent [E].** In allen 42 Faellen (32 nach Plan, dazu 10 weitere T-Faelle im Nachtrag [N])
   endeten XY und YX in derselben Delaunay-Zerlegung. Nur die 11 T-Faelle pruefen verschiedene Wege:
   - In 6 Faellen braucht eine Reihenfolge 4 Zuege, die andere 2; der laengere Weg entfernt seine erste neue Kante am
     Ende mit einem 3-2-Zug wieder.
   - In 5 Faellen legen beide Wege dieselben drei Kanten in umgekehrter Reihenfolge an.
   - In D und K sind es dieselben zwei Zuege in anderer Reihenfolge.
2. **Lesart R ist reihenfolgefest [E].** In allen Faellen und in beiden Formen A1 und A2 sind Delta_q hoechstens
   3,0e-14 und Delta_p hoechstens 1,6e-13, auch bei verschiedenen Wegen; das ist Rundung. Die statische Zeitumkehr
   kehrt ebenfalls exakt zurueck (<= 1,3e-14).
   - Erklaerung nach Sicht [H, nicht nachgerechnet]: Umschliessen die beteiligten urspruenglichen Tetraeder keine
     urspruengliche Kante, lassen sich ihre Kantenwerte flach einbetten. Dann sind alle flachen Fortsetzungen
     wegunabhaengig.
   - Nach 2-3-Zuegen entfernt die Projektion nur Eich- und Streckanteile [M, PLAN 8].
   - Die 3-2-Zuege in den Wegen entfernten jeweils eine im selben Weg flach angelegte Kante (nichtflacher Anteil
     <= 3e-17).
3. **Lesart P hinterlaesst eine Reihenfolgespur im Impuls der Geometrie, auch bei disjunkten Zuegen [E].**
   - Delta_p (A1): Median 4,5e-9 (D), 2,7e-7 (K), 3,6e-7 (T, Nachtrag); Maximum 1,3e-5. Delta_H der Geometrie bis
     1,5e-7. Delta_q bleibt bei Rundung, die Zeitumkehr ist auch in P exakt (<= 4,7e-15).
   - UK0 ist allein deshalb verfehlt: D-Maximum 2,8e-7 statt < 1e-12.
   - Ursache [H, nicht getrennt gerechnet]: Der null-fortgesetzte Impuls verletzt die Regeln leicht (im T-Fall der
     Saat 1 entfernte die Projektion 2,7e-7 bis 1,4e-5 des Impulses je Zug). Die Projektion wirkt global, also auch
     zwischen weit getrennten Zuegen.
4. **Der Skalar auf den Ecken ist reihenfolgefest, wie vorab abgeleitet [M, E].** Delta_Feld <= 7e-17. Bei 2-3- und
   3-2-Zuegen bleiben alle Ecken; die Uebergabe ist diagonal (PLAN 8).
   - UK1 ist verfehlt. UK2 ist nach Plan nicht entscheidbar und nach Wortlaut nur an Rundungsrauschen eingetroffen (so
     im Plan vorab vermerkt). UK3 ist nicht entscheidbar.
   - Licht ist nicht gerechnet: Der Vorlagencode hat keinen Lichtsektor.
5. **Form B ist nicht startbar, und doppelte Ereignisse sind selten [E].**
   - A2L hat im Kasten 28 bis 33 negative Richtungen; UK4 ist damit nicht entscheidbar.
   - In TAKT-DYNAMIK-1 (A = 1e-3) hatte hoechstens ein Zeitschritt je Lauf zwei Delaunay-Ereignisse, ohne erkennbaren
     Unterschied zwischen h = 0,5 und 0,25.
   - Nach 29 von 31, 56 von 113 und 49 von 65 Zuegen war aber sofort eine weitere Flaeche verletzt. Dort hat die
     Sperre in td.py ueber die Reihenfolge entschieden.

## 3. Urteile

Mechanisch durch code/konfluenz.py auswertung (eingefroren 11:43:30 CEST), lauf-69/auswertung.json; Regeln PLAN 7.

| Nr | Vorhersage (woertlich) | Wahrsch. | nach Plan | nach Kartenwortlaut | Kennzahl [E] |
|---|---|---|---|---|---|
| UK0 | Kontrolle [M]: disjunkte Zuege Delta < 1e-12; ohne Felder kombinatorisch gleiche Endzerlegung | 90 % | **verfehlt** | **verfehlt** | Endzerlegung gleich in 32 von 32 Faellen. D (11 Faelle): Lesart R alle Sektoren <= 6,6e-15, Skalar 0; Lesart P Delta_p 4,7e-10 bis 2,8e-7 (Maximum 2,76e-7, A2) |
| UK1 | [H] Lesart R, Feldamplitude 1e-3: Delta_Feld > 1e-6 relativ fuer mindestens eine Ueberlappungsart | 60 % | **verfehlt** | **verfehlt** | Median T 1,5e-17 (n = 1), K 0 (n = 20); Maximum T 1,5e-17, K 4,1e-17. Nachtrag [N]: T (n = 11) Median 2,3e-17, Maximum 6,8e-17 |
| UK2 | Kontrolle [M, Zusatz Leitung]: Delta_Feld waechst linear mit der Feldamplitude (Steigung 0,9 bis 1,1 zwischen 1e-3 und 1e-2) | 85 % | **nicht entscheidbar** | **eingetroffen** (nur Rundung) | Plan: kein Paar mit Delta_Feld > 1e-12. Wortlaut: 4 Paare (Fall, Lesart R) mit Rundungswerten (absolut 5,4e-20 bis 3,5e-18), Verhaeltnisse 8 = 2^3 (dreimal) und 9,6, Median der Steigung 0,90 |
| UK3 | [H] Lesart R hat eine mindestens 10-mal groessere Reihenfolgespur (Delta_Feld) als P | 35 % | **nicht entscheidbar** | **nicht entscheidbar** | Median Delta_Feld R = 0, P = 0 (T und K, A = 1e-3) |
| UK4 | [H] Form A und Form B unterscheiden sich in Delta_p um mehr als Faktor 2. Ist Form B im Kasten nicht startbar, lautet das Urteil "nicht entscheidbar" | 40 % | **nicht entscheidbar** | **nicht entscheidbar** | A2L mit R1 in keinem der 32 Faelle positiv definit: 28 (Saat 1, 4), 31 (Saat 2), 32 bis 33 (Saat 3) negative Richtungen |

- **Vorab ableitbar bzw. erwartet (PLAN 8), keine Messungen:**
  - UK1, UK2 (Plan) und UK3 fuer den Eckenskalar: Diagonale Uebergabe, also Delta_Feld = 0 bis auf Rundung [M].
    Bestaetigt (<= 7e-17). Der Kartenwortlaut von UK2 "trifft" an Rundung ein; das stand vorab im Plan.
  - UK4: nach HODGE-MASSE-1 nicht startbar erwartet [P]. Bestaetigt; die Zahl der negativen Richtungen gleicht der dort
    gemeldeten (28 / 31 / 33 / 28).
  - Lesart R mit reinen 2-3-Folgen: D exakt [M]. Bestaetigt (<= 6,6e-15).
  - Lesart P und Faelle mit 3-2: vorab offen; dass D in P > 1e-12 ergeben kann, stand im Plan als Moeglichkeit.
- **Agenten-Erwartungen (PLAN 10, kein Urteil):** E1 (Endzerlegung gleich, 90 %) eingetroffen (32 von 32).
  E2 (Skalar <= 1e-13, 90 %) eingetroffen. E3 (D in R < 1e-12, 80 %) eingetroffen. E4 (T und K in R Median
  Delta_q > 1e-6, 60 %) verfehlt (2,5e-15). E5 (A2L nicht startbar, 85 %) eingetroffen.
- **Bedeutung nach Karte (vorab festgelegt):**
  - "UK1 trifft ein ..." nicht ausgeloest.
  - "UK1 verfehlt: Die Uebergabe ist bei kleinen Feldern reihenfolgefest. Dann bleibt als einzige bekannte
    Reihenfolgespur die Kruemmung (PACHNER-TAKT-1)." **Ausgeloest.** Zwei Einschraenkungen:
    - Satz 1 gilt fuer einen Eckenskalar ohne Rueckwirkung vorab [M]; die Rechnung bestaetigt nur die Umsetzung.
    - Satz 2 trifft so nicht zu. Lesart P hinterlaesst eine zweite Reihenfolgespur im Impuls der Geometrie. Sie tritt
      auch bei disjunkten Traegern auf, haengt also nicht an gemeinsamen Kanten im Traeger (Ursache [H], Abschnitt 2,
      Punkt 3).
      Lesart R zeigt dagegen trotz gekruemmter Welle keine Spur.
  - "UK3 trifft ein ..." nicht ausgeloest (nicht entscheidbar). Beschreibend [E] gilt in der Geometrie das Gegenteil:
    Die Spur liegt in P, nicht in R.
  - Zusatz der Leitung (Spin): Die Rechnung sagt dazu nichts.

## 4. Tabellen

- Quellen: lauf-69/tabellen.md und lauf-69/auswertung.json (eingefroren erzeugt); Nachtrag [N]:
  nachtrag-69/tabellen-nt.md und nachtrag-69/zahlen.json (Median und Maximum von Delta_H gesamt, Skalar-Kontrollen;
  auf der .69 gerechnet). Punkt als Dezimalzeichen in den Tabellen.

### 4.1 Faelle und Kombinatorik

| Art | Faelle (Saat 1 / 2 / 3 / 4) | Kandidaten versucht | gleiche Endzerlegung | Zuege XY / YX | Typ X / Y | Verschiebung / l (Median) |
|---|---|---|---|---|---|---|
| D | 11 (2 / 2 / 4 / 3) | 45 / 50 / 38 / 39 | 11 | 2 / 2 (11) | 2-3 / 2-3 | 0.0017 |
| T | 1 (1 / 0 / 0 / 0) | 80 je Saat | 1 | 4 / 2 (1) | 2-3 / 2-3 | 0.0040 |
| K | 20 (5 / 5 / 5 / 5) | 19 / 60 / 35 / 72 | 20 | 2 / 2 (20) | 2-3 / 2-3 | 0.011 |
| T [N] | 11 (3 / 2 / 3 / 3), darunter der Plan-Fall | 596 / 597 / 597 / 595 | 11 | 4 / 2 (5), 3 / 3 (5), 2 / 4 (1) | 2-3 / 2-3 | 0.022 (Maximum 0.078) |

- Alle Status ok / ok. X und Y waren in allen Faellen 2-3-Zuege. 3-2 kam nur als letzter Zug des laengeren Wegs vor
  (6 der 11 T-Faelle) und entfernte jedes Mal die vom ersten Zug desselben Wegs angelegte Kante.
- In den 5 T-Faellen mit 3 / 3 Zuegen legen beide Wege dieselben drei Kanten in umgekehrter Reihenfolge an.
- In D und K sind beide Wege dieselben zwei Zuege in anderer Reihenfolge. Nur T prueft verschiedene Wege.

### 4.2 Geometrie: Delta je Sektor (relativ), Median [Min, Max] ueber die Faelle

| Art | Form | Lesart | n | Delta_q | Delta_p | Delta_H geo | Zeitumkehr q | Zeitumkehr p | Zwangsrest (Summe ueber XY) |
|---|---|---|---|---|---|---|---|---|---|
| D | A1 | R | 11 | 2.4e-15 [2.3e-15, 2.6e-15] | 5.1e-15 [4.5e-15, 5.5e-15] | 5.9e-16 [0, 1.2e-15] | 3.0e-15 | 6.3e-15 | 0.026 [0.0055, 0.052] |
| D | A1 | P | 11 | 2.4e-15 | 4.5e-09 [8.4e-10, 2.5e-07] | 6.0e-11 [4.1e-12, 4.7e-10] | 3.0e-15 | 3.1e-15 | 0.026 |
| D | A2 | R | 11 | 2.4e-15 [2.3e-15, 2.6e-15] | 5.7e-15 [4.6e-15, 6.5e-15] | 3.9e-16 [0, 7.8e-16] | 3.1e-15 | 7.6e-15 | 0.023 [0.0084, 0.050] |
| D | A2 | P | 11 | 2.4e-15 | 5.9e-09 [4.7e-10, 2.8e-07] | 9.4e-11 [9.2e-14, 6.3e-09] | 3.1e-15 | 3.1e-15 | 0.023 |
| T | A1 | R | 1 | 3.1e-15 | 7.4e-15 | 9.1e-16 | 4.3e-15 | 9.6e-15 | 0.060 |
| T | A1 | P | 1 | 3.1e-15 | 1.3e-08 | 3.1e-10 | 4.3e-15 | 4.2e-15 | 0.060 |
| T | A2 | R | 1 | 3.1e-15 | 5.7e-15 | 1.2e-15 | 4.1e-15 | 9.1e-15 | 0.087 |
| T | A2 | P | 1 | 3.1e-15 | 5.7e-08 | 4.4e-10 | 4.1e-15 | 4.0e-15 | 0.087 |
| K | A1 | R | 20 | 2.5e-15 [2.2e-15, 4.4e-15] | 5.1e-15 [4.6e-15, 1.0e-14] | 6.4e-16 [0, 2.0e-15] | 3.0e-15 | 6.1e-15 | 0.026 [0.010, 0.063] |
| K | A1 | P | 20 | 2.5e-15 | 2.7e-07 [1.0e-08, 1.3e-05] | 9.3e-10 [3.0e-12, 6.1e-08] | 3.0e-15 | 3.0e-15 | 0.026 |
| K | A2 | R | 20 | 2.5e-15 [2.3e-15, 3.0e-15] | 5.9e-15 [4.2e-15, 7.3e-15] | 3.0e-16 [0, 1.3e-15] | 3.0e-15 | 6.8e-15 | 0.032 [0.0020, 0.069] |
| K | A2 | P | 20 | 2.5e-15 | 2.3e-07 [7.8e-09, 2.2e-06] | 1.1e-09 [3.8e-12, 3.2e-08] | 3.0e-15 | 3.1e-15 | 0.032 |
| T [N] | A1 | R | 11 | 3.4e-15 [2.9e-15, 2.3e-14] | 7.3e-15 [6.1e-15, 1.6e-13] | 7.9e-16 [1.1e-16, 3.2e-15] | 3.8e-15 [3.3e-15, 4.5e-15] | 8.5e-15 [6.4e-15, 9.7e-15] | 0.043 [0.017, 0.081] |
| T [N] | A1 | P | 11 | 3.4e-15 | 3.6e-07 [1.3e-08, 3.7e-06] | 3.3e-09 [3.1e-10, 5.9e-08] | 3.8e-15 | 4.0e-15 [3.3e-15, 4.5e-15] | 0.043 |
| T [N] | A2 | R | 11 | 3.3e-15 [3.0e-15, 3.0e-14] | 8.4e-15 [5.7e-15, 1.5e-13] | 8.2e-16 [1.2e-16, 4.0e-15] | 3.8e-15 | 9.1e-15 [7.0e-15, 1.3e-14] | 0.062 [0.042, 0.093] |
| T [N] | A2 | P | 11 | 3.3e-15 | 5.3e-07 [1.3e-08, 1.7e-06] | 6.6e-09 [1.6e-10, 1.5e-07] | 3.8e-15 | 4.0e-15 [3.2e-15, 4.7e-15] | 0.062 |

- Zeitumkehr ohne Spanne: Median; die Maxima liegen in allen Zeilen bei hoechstens 1,3e-14.
- "Zwangsrest" ersetzt den Gauss-Rest (PLAN 6): Anteil von a, den die Projektion je Zug entfernt (Eichung und
  Streckung), summiert ueber die Zugfolge XY. In P gilt fuer die Laengen dieselbe Abbildung wie in R.
- Delta_q ist in R und P gleich, weil beide Lesarten die Laengen gleich uebergeben.

### 4.3 Skalar (phi, pi auf den Ecken)

| Art | Lesart | A | n | Delta_phi | Delta_pi (Median [Min, Max]) | Delta_pi absolut (Max) | Zeitumkehr phi / pi (Max) | Delta_H_phi (Max) |
|---|---|---|---|---|---|---|---|---|
| D | R | 1e-3 / 1e-2 | 11 | 0 | 0 | 0 | 0 / 6.3e-17 | 0 |
| T | R | 1e-3 / 1e-2 | 1 | 0 | 1.5e-17 / 1.4e-17 | 1.6e-19 / 1.6e-18 | 0 / 4.6e-17 | 0 |
| K | R | 1e-3 | 20 | 0 | 0 [0, 4.1e-17] | 4.3e-19 | 0 / 5.8e-17 | 0 |
| K | R | 1e-2 | 20 | 0 | 0 [0, 3.3e-17] | 3.5e-18 | 0 / 6.0e-17 | 0 |
| D, T, K | P | 1e-3 / 1e-2 | 32 | 0 | 0 | 0 | 0 / 0 | 0 |
| T [N] | R | 1e-3 | 11 | 0 | 2.3e-17 [5.2e-18, 6.8e-17] | 7.5e-19 | 0 / 6.4e-17 | 0 |
| T [N] | P | 1e-3 / 1e-2 | 11 | 0 | 0 | 0 | 0 / 0 | 0 |

- Kontrollen [E, N]: Summe *0 = V auf 3,3e-16; kleinstes *0 = 0,21 x Mittel; kein *0 negativ, auch nicht in den
  Zwischenzerlegungen.

### 4.4 Delta_H gesamt (Geometrie + Skalar), Median / Maximum ueber die 32 Faelle [N, nachtrag-69/zahlen.json]

| Form | Lesart | Skalar A = 0 | A = 1e-3 | A = 1e-2 |
|---|---|---|---|---|
| A1 | R | 6.4e-16 / 2.0e-15 | 2.0e-16 / 4.1e-16 | 0 / 0 |
| A1 | P | 3.9e-10 / 6.1e-08 | 8.4e-11 / 1.4e-08 | 1.0e-12 / 1.8e-10 |
| A2 | R | 3.6e-16 / 1.3e-15 | 0 / 4.2e-16 | 0 / 0 |
| A2 | P | 5.6e-10 / 3.2e-08 | 1.4e-10 / 8.6e-09 | 1.8e-12 / 1.3e-10 |

- Mit wachsender Skalar-Amplitude wird Delta_H gesamt kleiner, weil der Skalar (reihenfolgefest) einen wachsenden Teil
  von H traegt. Nachtrag T: A1 P bei A = 0 Median 3,3e-9, Maximum 5,9e-8; A2 P 6,6e-9 / 1,5e-7.

### 4.5 Haeufigkeit doppelter Ereignisse in TAKT-DYNAMIK-1 (A = 1e-3, Arm b, Lesart R; beschreibend)

| Saat | h | Schritte | Ereignisse / Zuege | Schritte mit Ereignis | Schritte mit >= 2 Ereignissen (Anteil an allen / an Schritten mit Ereignis) | Zuege, nach denen sofort eine Flaeche verletzt war |
|---|---|---|---|---|---|---|
| 1 | 0,5 | 1360 | 31 / 31 | 31 | 0 | 29 |
| 1 | 0,25 | 2720 | 31 / 31 | 31 | 0 | 29 |
| 2 | 0,5 | 1920 | 113 / 113 | 113 | 0 | 56 |
| 2 | 0,25 | 3840 | 113 / 113 | 112 | 1 (2,6e-4 / 0,0089) | 56 |
| 3 | 0,5 | 1330 | 67 / 65 | 66 | 1 (7,5e-4 / 0,015) | 49 |
| 3 | 0,25 | 2650 | 70 / 67 | 69 | 1 (3,8e-4 / 0,015) | 51 |
| 4 | 0,5 und 0,25 | 1360 / 2720 | 0 | 0 | 0 | 0 |

- Die Zaehlungen (0 oder 1 je Lauf) tragen keinen Vergleich zwischen h = 0,5 und 0,25.
- Die rechte Spalte zaehlt Zuege, nach denen eine weitere Flaeche sofort mu < 0 hatte (Linearisierungsrest der neuen
  Kante, TAKT-DYNAMIK-1 PLAN 3). td.py sperrt sie, bis mu wieder > 0 ist. Gleichzeitig faellig im Sinn der Karte
  waeren diese Flaechen auch; die Sperre entscheidet dort die Reihenfolge, ohne dass sie getestet ist.

### 4.6 Weitere Kontrollen [E]

- Ausgangsnetze: Delaunay (0 verletzte Flaechen), kleinster Randabstand mu0 6,1e-4 / 9,2e-5 / 1,9e-4 / 2,0e-3.
  Nach der Verschiebung genau X und Y verletzt, kein Tetraeder mit umgekehrtem Vorzeichen (Auswahlregel).
- A_red von A1 und A2 ist in allen Netzen aller Ketten positiv definit (alle 42 Faelle).
- Mode (Saat 1, verschobenes Netz): omega = 2,4926, TT-Anteil 0,289 (TAKT-DYNAMIK-1: 2,493 / 0,289).
- Nichtflacher Anteil der 3-2-Zuege in den Wegen: |delta| <= 2,7e-17. Die entfernte Kante war jeweils eine flache
  Fortsetzung aus demselben Weg.

## 5. Bedeutung [H] fuer die Uebergaberegel der Grundgleichung (GRUNDGLEICHUNG-SKIZZE-v2, Abschnitt 6)

- **Was die Rechnung traegt [E]:**
  - Fuer 2-3-Zuege an festen Ecken ist "umklappen bis Delaunay" kombinatorisch konfluent, auch wenn die Wege
    verschieden sind (11 T-Faelle).
  - Die Projektions-Uebergabe (R) ist dort reihenfolgefest und statisch umkehrbar.
  - Die Impuls-Uebergabe (P) ist statisch umkehrbar, aber nicht reihenfolgefest (bis 1,3e-5 relativ im Impuls).
  - Eckfelder (phi, pi) sind unter diesen Zuegen trivial reihenfolgefest [M].
- **Folgerungen fuer Abschnitt 6 [H]:**
  1. **Skalar:** phi und pi brauchen beim Umklappen an festen Ecken keine Reihenfolgeregel.
     - Fuer einen geladenen Skalar [M, nicht gerechnet]: Lesart R skaliert pi_v mit *0'_v / *0_v und aendert damit
       die Ladungsdichte Im(phi* pi) an den Ecken, deren *0 sich aendert. Das erzeugt Ladung und verletzt Gauss nach
       dem Zug.
     - Lesart P laesst pi und damit die Ladung unveraendert. Fuer die Forderung "Gauss nach dem Zug ohne Ladung" ist P
       beim Skalar die passende Wahl.
  2. **Geometrie:** Die beiden Lesarten verteilen die drei Bedingungen aus Abschnitt 6 verschieden.
     - R: hier reihenfolgefest und umkehrbar, verliert aber Energie (TAKT-DYNAMIK-1: -2,4 bis -12,7 % ueber 10
       Perioden, A = 1e-3).
     - P: umkehrbar, gewinnt Energie (TAKT-DYNAMIK-1: +15 bis +20 %) und hinterlaesst eine kleine Reihenfolgespur.
     - Die dritte Bedingung (symplektische Struktur) ist fuer keine der beiden geprueft. Der reduzierte Phasenraum
       waechst bzw. schrumpft je Zug um 2 Dimensionen.
     - Waehlt die Grundgleichung P, braucht sie entweder eine Reihenfolgeregel fuer gleichzeitige Zuege oder eine
       Impulsfortsetzung, die die Regeln oertlich erfuellt (dann entfiele die globale Projektion). Das zweite ist eine
       Vermutung, nicht gerechnet.
  3. **Licht (A_e, E^e auf Kanten):** Es hat dasselbe Problem wie die Geometrie: neue Kanten bei 2-3, wegfallende bei
     3-2. Ob eine Uebergabe, die d respektiert und Gauss erhaelt, reihenfolgefest ist, ist offen. Die Rechnung hier
     sagt nichts darueber.
  4. **Gleichzeitigkeit in der Praxis:** In der Dynamik von TAKT-DYNAMIK-1 entscheidet weniger der Zeitschritt als die
     Sperre nach einem Zug ueber die Reihenfolge. Eine Grundgleichung mit Umklappen braucht deshalb eine ausdrueckliche
     Regel fuer Flaechen, die durch einen Zug selbst verletzt werden.
- **Grenzen:**
  - Alle Startzuege X, Y waren 2-3-Zuege. Ein 3-2-Zug, der eine urspruengliche, gekruemmte Kante entfernt, kam nicht vor.
    Gerade dort verliert R den nichtflachen Anteil (PLAN 8) und koennte nichtoertlich werden. Das ist ungetestet.
  - Statische Paarprobe auf festem, verschobenem Hintergrund; keine dynamische Bahn (die Zuege loest hier die
    Verschiebung aus, nicht die Welle).
  - N = 128, eine TT-Mode (Wellenlaenge = Kastenlaenge), lineares Modell um den flachen Hintergrund, Testfeld ohne
    Rueckwirkung.

## 6. Selbstanzeigen und Negativliste

### 6.1 Selbstanzeigen

1. **Scratchpad:** Der Startbefehl der Laufketten hielt die ssh-Verbindung offen, weil die Liste `cd ... && nohup ...`
   als Ganzes im Hintergrund lief. Das Werkzeug verschob den Befehl nach 120 s in den Hintergrund und legte seine
   Ausgabe unter /tmp/claude-1000/.../tasks/ ab. Das verletzt "nie nach /tmp/claude-1000/...". Die Ketten liefen
   dabei normal und einmal; spaeter mit `setsid nohup` gestartet und nur auf der .69 gewartet.
2. **jq lokal zum Rechnen:** Nach dem Abschluss habe ich lokal mit jq Maxima, Minima und eine Eindeutigkeitsliste
   ueber die Faelle gebildet (Delta_H gesamt, Skalar-Kontrollen, A_pd). Das ist mehr als Lesen. Die zitierten Zahlen
   stammen aus nachtrag-69/zahlen.json, auf der .69 gerechnet (code/nachtrag_zahlen.py), und stimmen mit der lokalen
   Sichtung ueberein.
3. **sed -i lokal:** drei Ersetzungen in code/konfluenz.py vor dem Einfrieren (N_FAELLE, Option --faelle). Der Auftrag
   verbietet es nicht; die Vorlage HODGE-MASSE-1 zeigte es an, darum hier auch.
4. **Vorab ableitbar:** UK1, UK2 (Plan) und UK3 waren fuer den Eckenskalar vor jeder Rechnung entschieden (PLAN 8). Die
   Karte nannte "Groesse von Delta_Feld je Ueberlappungsart" nicht ableitbar. Diese Urteile sind Kontrollen, keine
   Messungen.
5. **UK2 nach Wortlaut "eingetroffen"** beruht auf vier Paaren mit Rundungswerten (5,4e-20 bis 3,5e-18 absolut;
   Verhaeltnisse 8 = 2^3, also Stufen der Gleitkommarundung). Der Plan hatte das vorab als moegliches
   Rundungs-Eintreffen vermerkt. Inhaltlich ist es kein Befund.
6. **Zu enge Auswahl fuer T:** Der eingefrorene Plan fand nur 1 T-Fall (1 von 320 versuchten Kandidaten). Bemerkt erst
   nach dem Lauf. Der Nachtrag mit 600 Kandidaten je Saat (code/nachtrag_t.py, konfluenz.py unveraendert importiert)
   ist nach Sicht und beschreibend; die Urteile bleiben die des eingefrorenen Laufs.
7. **Nicht gerechnet:** Licht (kein Vorlagencode), Gauss-Rest (ersetzt durch den Zwangsrest), dynamische Zeitumkehr,
   Startzuege vom Typ 3-2, Rueckwirkung des Felds.
8. **Rauchtests:** r2 (Rauchsaat 901) schrieb volle Werte nach rauch/; nicht gelesen. Gelesen habe ich in r1 und r7 die
   Zahl angenommener Faelle je Art (1 / 1 / 1) und Laufzeiten, in r3 bis r6 nur rc, Schluessel und Zeilenzahlen.
9. **Zwischenstaende:** Waehrend der Hauptlaeufe habe ich nur Status und rc gelesen, keine Werte. Die Werte habe ich
   erst nach der eingefrorenen Auswertung gelesen.
10. **Kein frischer Gegenleser** in der Zeitbox. Zahlen rueckwaerts gegen lauf-69/tabellen.md,
    nachtrag-69/tabellen-nt.md und nachtrag-69/zahlen.json geprueft. Kein Journal, kein Peerbus, kein Commit.

### 6.2 Negativliste (nach diesen Befunden NICHT sagen)

- "Die Uebergabe beim Umklappen ist Church-Rosser." Belegt ist das nur fuer Lesart R, Startzuege 2-3, die hier gebauten
  Paare (D, K, T), statisch, linear, N = 128.
- "Felder hinterlassen keine Reihenfolgespur." Gezeigt (und vorab abgeleitet) ist das nur fuer einen Eckenskalar ohne
  Rueckwirkung bei Zuegen an festen Ecken. Licht und 1-4/4-1-Zuege sind ungetestet.
- "UK2 bestaetigt die Linearitaet." Das Eintreffen nach Wortlaut ist Rundung.
- "Lesart P ist falsch" oder "R ist richtig": P ist umkehrbar und hat nur eine kleine Spur; R ist konfluent, verliert
  aber Energie.
- "Die einzige Reihenfolgespur ist die Kruemmung": In P gibt es eine zweite.
- "Gleichzeitige Zuege sind selten, also unwichtig": Die Sperre nach Zuegen verdeckt die Gleichzeitigkeit.
- "Spin steckt in der Reihenfolge": Die Karte prueft keinen Spin.
- Keine Aussage ueber Messdaten.

## 7. Einfach gesagt

Wir haben im Netz zwei Zellen gleichzeitig zum Umklappen gebracht und einmal die eine, einmal die andere zuerst
umgeklappt. Am Ende kam in allen 42 Faellen dasselbe Netz heraus, auch wenn der Weg dorthin verschieden lang war. Ein
Feld, das auf den Ecken sitzt, merkt von der Reihenfolge nichts, weil die Ecken beim Umklappen bleiben; das war vorher
klar. Bei der Schwerewelle haengt es an der Rechenvorschrift: Schneidet man nach jedem Umklappen den unerlaubten Teil
weg (Lesart R), ist die Reihenfolge egal. Uebernimmt man die Impulse (Lesart P), bleibt eine winzige Spur der
Reihenfolge, hoechstens gut ein Hunderttausendstel; alles sind Rechnungen an kleinen Modellnetzen, keine Messungen.

## 8. Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-114330, EINGEFROREN-SHA256.txt,
  EINGEFROREN-SHA256-69.txt.
- code/: konfluenz.py und kette.sh (je mit .eingefroren-20261005-114330); unveraendert kopiert: td.py, hm_td.py, tg.py,
  uk.py, tu.py, tp.py, ew.py, mn.py, tg_auswertung.py; Nachtraege [N]: nachtrag_t.py, nachtrag_kette.sh,
  nachtrag_zahlen.py.
- lauf-69/: konfluenz-s1..s4.json, haeufigkeit.json, auswertung.json, tabellen.md, Logs, kette-*.out, PRUEFSUMMEN.txt.
- nachtrag-69/: konfluenz-s1..s4.json (nur T), auswertung-nt.json, tabellen-nt.md, zahlen.json, zahlen-ausgabe.txt,
  Logs, PRUEFSUMMEN.txt, PRUEFSUMMEN-2.txt.
- rauch-69/: r1 bis r7 (Logs, Schluessel), Testdateien aus r2 bis r6.
- Auf der .69: /home/fmh/fmhc-physics-remote/uebergabe-konfluenz-1/ (code/, lauf/, nachtrag/, rauch/).

Abschlusszeile geschrieben nach date 2026-10-05 12:00:03 CEST. Zeitbox 120 min ab 11:21:14 CEST (bis 13:21:14)
eingehalten. Kein Lauf mehr aktiv (letzter Aufruf uk1-nt-zahlen endete 09:53:04 UTC). KARTE.md unveraendert (sha256
bce98aa9...), code/konfluenz.py seit dem Einfrieren unveraendert. Journal, Peerbus und Commit uebernimmt die Leitung.
