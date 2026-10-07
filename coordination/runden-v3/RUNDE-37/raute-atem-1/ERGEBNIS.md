# RAUTE-ATEM-1: Ergebnis (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:21:01 CEST, Plan und Code eingefroren 18:39:07 CEST,
  Nachtrag (Befund A1 des Lesers) eingefroren 18:48:22 CEST, alles per date. Hauptlaeufe .69 16:39:20 bis 16:45:19 UTC,
  Variante 16:48:23 bis 16:53:14 UTC, Auswertung 16:48:23 (Haupt) und 16:53:16 UTC (Variante). Geschrieben ab
  2026-10-04 18:54:36 CEST.
- Unterlagen: PLAN.md (eingefroren), PLAN-NACHTRAG.md (eingefroren, [Zusatz Leitung]), EINGEFROREN-SHA256.txt,
  EINGEFROREN-NACHTRAG-SHA256.txt, code/, rauch-69/, lauf-69/ (Hauptlauf), lauf-69/var/ (Variante),
  lauf-69/PRUEFSUMMEN-69.txt (auch die npz-Zeitreihen, die auf der .69 bleiben).
- Kennzeichen: [E] gerechnet im Modell, [M] Mathematik (nicht gegengelesen), [L] Gedaechtnis, [H] Hypothese.
- Modell (Kartenlesart, PLAN.md Abschn. 2): eps = 0,1, k = 1, mu_x = 2, kappa = 0,01, T = 1e-3 K, delta_f = 0,02 PU,
  B = 0,03 / 0,05 / 0,08, vier Saaten, 500 Takte. Das Medium wirkt nur auf die Lagen (Grenze, Nachtrag N3).

## 1. Ergebnis zuerst

1. **Faltet zum Tetraeder: ja [E].** Mit Medium faltet die Raute in 3D in allen 12 Laeufen, und C-D schliesst nach 31
   bis 92 Takten (RA1 eingetroffen). Ohne Medium bleibt sie flach (Winkelaenderung hoechstens 0,2 Grad). In 2D faltet
   nichts.
2. **Kein Klapptakt [E].** In keinem Lauf oeffnet sich die Raute wieder (0 Oeffnungen nach beiden Lesarten); C und D
   bleiben im anziehenden Bereich (|Phase C - Phase D| hoechstens 65 Grad). RA2 verfehlt, wie nach Befund A1 vorab
   erwartet. Neu: Im geschlossenen Zustand liegt stattdessen das Scharnierpaar A-B um 43 bis 69 Grad auseinander
   (Fenstermittel; offen waren es unter 9 Grad).
3. **Das Phasenmuster ist nicht 120 Grad [M, E].** Der Leser-Befund A1 haelt (selbst nachgerechnet): Gleich starke
   Kopplung gibt A = B und C = D. Gemessen: A ~ B (meist |Delta| < 9 Grad), C = D (< 3 Grad), dazwischen 126 bis 166
   Grad statt 180. RA0 deshalb verfehlt (Phasenteil; vorab ableitbar). Werkzeugprobe (Kraftbilanz je Knoten) 6e-11,
   Statik-Kontrolle 6e-15.
4. **Kraefte im geschlossenen Tetraeder (Zeitmittel) [E]:** groesste Kraft im Schliessstab C-D (Druck 0,67 bis 1,10 B),
   Aussenkanten Zug 0,47 bis 0,88 B, das **Scharnier A-B** (Druck 0,36 bis 0,81 B) **traegt bei B = 0,03 und 0,05 am
   wenigsten**; bei B = 0,08 liegen zwei Aussenkanten knapp darunter. Finns FP verfehlt (0 von 12 Laeufen).
5. **2D getrennt [E]:** In der flachen Raute traegt das Scharnier die groesste mittlere Kraft (Druck 0,67 bis 0,79 B),
   die Aussenkanten die kleinste (Zug 0,42 bis 0,51 B). Dort passt Finns Bild; FP gilt laut Karte aber dem gefalteten
   Zustand. Auch der Wechselanteil (Atemtakt) ist am Scharnier am groessten, in 2D immer, in 3D bei B = 0,03 und 0,05
   (nachtraeglich bemerkt, keine Vorhersage).
6. **Variante [Zusatz Leitung, beschreibend]: C und D mit halber Atemamplitude.** Faltet und schliesst auch (12 von 12),
   kein Klapptakt, kein 120-Grad-Muster. Aber **Finns Kraftbild trifft ein**: Scharnier Zug 0,61 bis 0,70 B
   (groesste), Aussenkanten 0,00 bis 0,28 B (kleinste), C-D Druck 0,34 bis 0,80 B; 9 von 12 Laeufen. Grund [E]: A und B
   laufen gegenphasig (Delta 174 bis 180 Grad); die Aussenpaare haben keine feste Phasenlage, ihr Mittel von cos(Delta)
   und damit ihre mittlere Kraft ist klein (Deutung als Phasenwandern [H]).

## 2. Urteilstabelle

Hauptmodell (Karte, PLAN.md Abschn. 5; Regeln nicht geaendert):

| Nr | Plan | Kartenwortlaut | Kennzahlen |
|---|---|---|---|
| RA0 | nicht eingetroffen | nicht eingetroffen (vorab ableitbar, Nachtrag N2) | Phasen Ende (Kontrollen, 2D und 3D): Delta_AB -39 bis +1 Grad, Aussen 126 bis 166 Grad, Delta_CD 0,1 bis 2,6 Grad (<= 0,045 rad, dieser Teil haelt); 3D max Winkelaenderung in 200 Takten 0,07 bis 0,20 Grad (haelt); Werkzeugprobe: Schleife gegen numerischen Gradienten max 5,6e-11, gegen Bewegungskraft 4,2e-16, Impulssumme 2,3e-17 (3400 Proben, 6 an der Fangkante ausgelassen; haelt); Statik 3D t_b = -f_b auf 5,7e-15, 2D Gleichgewicht auf 4,9e-15 (haelt) |
| RA1 | eingetroffen | eingetroffen | erstes Schliessen B = 0,03: 70 bis 92 Takte; 0,05: 46 bis 68; 0,08: 31 bis 55; kleinster Faltwinkel 53 bis 65 Grad (Tetraeder 70,5) |
| RA2 | nicht eingetroffen | nicht eingetroffen | Oeffnungen Plan/Karte 0/0 in allen 12 Laeufen; Umordnung (|Delta_CD| > 90 Grad im Zu-Zustand) 0 von 12; max |Delta_CD| zu: 8 bis 11 Grad (B = 0,03), 11 bis 22 (0,05), 61 bis 65 (0,08); kein Klappzyklus |
| FP | nicht eingetroffen | nicht eingetroffen | Plan: 0 von 12 auswertbaren Laeufen. Gepoolt (Mittel/B): A-B -0,59, A-C +0,71, B-C +0,84, A-D +0,81, B-D +0,74, C-D -0,97; C-D im Fenster zu 77 % gebunden |

Variante [Zusatz Leitung] (beschreibend, Regeln aus PLAN-NACHTRAG.md N4, vor dem Lauf eingefroren):

| Nr | Ausgang | Kennzahlen |
|---|---|---|
| V-RA0 | nicht eingetroffen | Kontrollen ohne festes Muster: Delta_AB -150 bis +174 Grad je Saat; Delta_CD 2 bis 8 Grad; kein Falten (<= 0,21 Grad); Werkzeugprobe bestanden |
| V-RA1 | eingetroffen | erstes Schliessen 27 bis 165 Takte |
| V-RA2 (Plan / Karte) | nicht eingetroffen / nicht eingetroffen | 0 Oeffnungen in 12 Laeufen; Umordnung in 2 von 12 (B = 0,08, Saat 2 bei 301 Takten, Saat 4 bei 425), danach trotzdem kein Oeffnen |
| V-FP (Plan / gepoolt) | eingetroffen / eingetroffen | 9 von 12 Laeufen (verfehlt: B = 0,03 Saaten 1 und 4, B = 0,05 Saat 4, dort C-D groesser als A-B). Gepoolt (Mittel/B): A-B +0,66, A-C +0,18, B-C +0,12, A-D +0,16, B-D +0,15, C-D -0,56 |

## 3. Stabkraefte je Kante

Zeitmittel in Einheiten von B (Zug +, Druck -), Spanne ueber 4 Saaten; Wechsel = sqrt(2) x Standardabweichung, ebenfalls
in B. 3D: Fenster "zu" (C-D gebunden im Sinne der Plan-Ereignisse); 2D: zweite Haelfte (t = 250 bis 500).

**Hauptmodell, 3D geschlossen [E]:**

| Kante | B = 0,03 Mittel | B = 0,05 Mittel | B = 0,08 Mittel | Wechsel (0,03 / 0,05 / 0,08) |
|---|---|---|---|---|
| A-B (Scharnier) | -0,36 bis -0,40 | -0,74 bis -0,78 | -0,48 bis -0,81 | 2,46-2,49 / 1,61-1,63 / 0,92-1,09 |
| A-C | +0,65 bis +0,88 | +0,79 bis +0,85 | +0,50 bis +0,71 | 0,59-1,02 / 0,25-0,43 / 0,05-0,50 |
| B-C | +0,66 bis +0,88 | +0,85 bis +0,88 | +0,83 bis +0,86 | (Aussenkanten zusammen) |
| A-D | +0,65 bis +0,88 | +0,81 bis +0,88 | +0,85 bis +0,87 | |
| B-D | +0,66 bis +0,88 | +0,81 bis +0,87 | +0,47 bis +0,67 | |
| C-D (Schluss) | -1,01 | -1,08 bis -1,10 | -0,67 bis -1,01 | 1,75 / 1,50-1,51 / 0,90-1,10 |

- Der Wechselanteil am Scharnier ist in absoluten Einheiten fast unabhaengig von B (~0,07 bis 0,09 k PU): Er kommt vom
  Gleichtakt-Atmen von A und B (Ruhelaenge A-B schwingt mit +-eps), nicht vom Medium [E, M].

**Hauptmodell, 2D flach [E]:** A-B -0,67 bis -0,79 (Druck, groesste); Aussenkanten +0,42 bis +0,51 (Zug); C-D kein Stab,
Abstand 1,775 bis 1,851 PU (> sqrt 3: die Raute wird laengs C-D gestreckt). Wechsel A-B 1,15 bis 3,04 B, Aussen 0,16 bis
0,64 B. Phasen: Delta_AB -9 bis +9 Grad, Aussen 139 bis 148 Grad, Delta_CD < 2 Grad.

**Kontrolle, Statik bei festen Phasen der Kartenannahme (0, 120, 240, 240 Grad), ableitbar [E als Kontrolle]:**
3D C-D Druck 1,07 bis 1,23 B, alle uebrigen Zug 0,46 bis 0,49 B (t_b = -f_b auf 6e-15); mit Atmen bei festen
Relativphasen (B = 0,05) aendern sich die Zeitmittel in 3D um hoechstens 1,2 %. 2D: A-B Zug 0,83 B, Aussen 0,15 bis
0,16 B (Schreibtisch 5/6 und 1/6); mit Atmen A-B 0,2 %, Aussenkanten bis 11 % anders.

**Variante, 3D geschlossen [E]:** A-B +0,61 bis +0,70 (Zug, groesste), Aussenkanten +0,00 bis +0,28, C-D -0,34 bis
-0,80. Wechsel: A-B 0,37 bis 1,18 B, Aussen 1,1 bis 1,8 B (hier ist der Wechselanteil aussen am groessten), C-D 0,50 bis
1,25 B. Phasen im Zu-Fenster: Delta_AB 174 bis 180 Grad, Delta_CD 39 bis 71 Grad. **Variante 2D (B = 0,05):** A-B
+0,73 bis +0,81 (Zug), Aussen -0,23 bis +0,13, Delta_AB 154 bis 176 Grad.

## 4. Bilder (lauf-69/)

- `raute-kraefte.png`: Tetraeder (3D, B = 0,05, Saat 1, Zu-Fenster) und flache Raute (2D, B = 0,05, Saat 1) mit
  Zeitmittel je Stab (rot Zug, blau Druck, Dicke nach Betrag); rechts Saatenmittel je Stab und B mit den Statikwerten der
  Kartenannahme (Strich) und nach A1 (Kreuz).
- `faltwinkel.png`: Faltwinkel ueber der Zeit (12 Laeufe, je B eine Zeile) und |Phase C - Phase D|.
- Variante: `var/var-raute-kraefte.png`, `var/var-faltwinkel.png`.
- Anzeige-Skripte code/bilder.py, code/bilder_var.py, code/tabellen.jq, code/tabellen_var.jq: nach dem Einfrieren
  geschrieben, nicht Teil der Auswertung.

## 5. Selbstanzeigen

1. **Schreibtischfehler uebernommen:** Mein Plan (D1, D5, D7) hat den falschen 120-Grad-Grundzustand der Karte nicht
   geprueft (ich habe nur gegen "A, B gegenphasig" verglichen, nicht gegen A = B). Gefunden hat es der Leser (A1), nicht
   ich. Plan und Regeln blieben unveraendert; Nachtrag N1/N2 vor Sicht auf die Ergebnisse.
2. **Bibliotheksprobe ausserhalb kleintest.sh:** 16:21 UTC ein direkter python-Aufruf auf der .69 (nur Import und
   Versionsnummern, keine Rechnung).
3. **Rauchlaeufe vor dem Plan:** Die ersten zwei Rauchlaeufe (alte Parameter) liefen, bevor PLAN.md geschrieben war. Die
   Statik zeigte den Kollaps bei B = 0,2; danach habe ich B, delta_f, mu_x und kappa vor dem Einfrieren geaendert
   (PLAN.md Abschn. 3). Gesehen waren nur ableitbare Statikwerte, keine Hauptergebnisse.
4. **Werkzeugprobe teils doppelt:** Die "Bilanz mit Reibung" ist rechnerisch dieselbe Groesse wie "vektorisiert gegen
   Schleife"; unabhaengig ist nur der Vergleich mit dem numerischen Gradienten.
5. **FP-Regel ohne Gleichstandstoleranz** eingefroren; nach A1 waere ein Gleichstand moeglich gewesen. Tatsaechlich lag
   das Scharnier in jedem Lauf um 0,17 bis 0,65 B hinter C-D; das Urteil haengt daran nicht.
6. **Variante ohne eigenen Rauchlauf:** raute_var.py lief direkt als Variantenlauf (Zeitbox); die Werkzeugprobe lief
   darin mit und bestand. Variante beschreibend; ihre Regeln standen vor dem Lauf im eingefrorenen Nachtrag.
7. **Anzeige nachgebessert:** bilder.py nach der ersten Darstellung geaendert (Beschriftung, zweite Statikmarke) und neu
   gerechnet; keine Zahl der Auswertung betroffen.
8. **Wechselanteil am Scharnier** (Punkt 1.5) ist eine nachtraegliche Beobachtung, keine vorab festgelegte Pruefung.
9. Kein Journaleintrag: Mein Schreibrecht endet im Kartenordner; der Eintrag ueber research_journal.py bleibt bei der
   Leitung.
10. Keine lokale Rechnung (lokal nur jq zur Anzeige, sed, grep, ssh/scp, sha256sum); kein pkill/pgrep; keine Hooks oder
    Dienste. Warteschleifen (until/sleep) liefen per ssh auf der .69 als einfache Befehle.

## 6. Einfach gesagt

Finns Raute aus zwei Dreiecken klappt im Modell tatsaechlich zu einem Tetraeder zusammen, wenn die beiden Aussenpunkte im
gleichen Takt atmen: Sie ziehen sich an und schliessen die Luecke nach 30 bis 90 Takten. Danach bleibt das Tetraeder
zu; es oeffnet sich nicht wieder, einen eigenen langsamen Klapptakt gibt es nicht. Wenn alle Ecken gleich stark atmen,
traegt im geschlossenen Tetraeder die Schliesskante zwischen den Aussenpunkten die groesste Kraft und das Scharnier meist
die kleinste, also anders als Finn vermutet hat. Atmen die Aussenpunkte nur halb so stark (wie die kleinen Kreise in
Finns Skizze), dreht sich das um: Dann geht die grosse Kraft durchs Scharnier und aussen bleibt wenig, wie Finn es
gezeichnet hat, allerdings weil die zwei Scharnierpunkte dann gegeneinander atmen. Auch in der flachen Raute (2D) traegt
das Scharnier am meisten.
