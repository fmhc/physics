# QUARK-2: Dirac-Fermionen im Q-Ball als Beutel (Runde 12; Finn: "wie finden wir eine ueberleitung zu quarks?")

- Leitung: claude-primary. Karte geschrieben ab 2026-10-01 17:15:50 CEST (date), vor jeder Codezeile und jedem Lauf.
- Explorativ. Bekannte Physik (Friedberg-Lee-Beutelmodell, MIT-Beutel), hier fuer unseren Ball nachgerechnet. Eine
  Quark-Behauptung ist das nicht.

## Modell

- Q-Ball-Profil: f'' + (2/r) f' = (1 - omega^2 - 2 f^2 + 1,5 f^4) f, f'(0) = 0, f(inf) = 0; S = f^2. Das ist unser
  U(S) = S - S^2 + S^3/2.
- Fermion: Dirac-Feld mit ortsabhaengiger Masse (Kopplung an |phi|^2, zeitunabhaengig),
  m(r) = M (1 - lambda S(r)) mit lambda = 1/S(0). Damit ist die Masse in der Mitte 0 und draussen M.
- Radialgleichungen (G oben, F unten, Dirac-Quantenzahl kappa):
  G' = -(kappa/r) G + (E + m) F
  F' = (kappa/r) F - (E - m) G
- Gebunden heisst |E| < M mit Abfall im Aussenraum. Gezaehlt werden die positiven Niveaus, kappa = -1, +1, -2, +2, -3.
- Ballradius R_h: der Radius mit S = S(0)/2.
- Werte: M = 10 (Fermionmasse draussen, in Einheiten der Skalarmasse 1); omega^2 = 0,55, 0,60, 0,65, 0,70, 0,80.

## Vergleich: MIT-Beutel (Kugel, innen masselos, Rand mit unendlicher Masse)

Niveaus x = E R [L?, aus dem Gedaechtnis]: 1s1/2 2,043; 1p3/2 3,204; 1p1/2 3,812; 1d5/2 4,327; 2s1/2 5,396.

## Vorhersage (vor jedem Lauf)

- **V1:** Fuer omega^2 <= 0,60 liegt E(1s1/2) R_h zwischen 1,7 und 2,3 (MIT 2,04). Abweichungen kommen von der weichen
  Wand und der endlichen Masse M.
- **V2:** Fuer omega^2 <= 0,60 ist die Reihenfolge wie im MIT-Beutel: 1s1/2 < 1p3/2 < 1p1/2.
  - E(1p3/2)/E(1s1/2) = 1,57 +- 0,15
  - E(1p1/2)/E(1s1/2) = 1,87 +- 0,20
- **V3:** Die Zahl der gebundenen positiven Niveaus (kappa wie oben, alle n) waechst mit dem Ball. Bei omega^2 = 0,80
  gibt es mindestens ein gebundenes Niveau, aber weniger als bei 0,55.
- **V4 (Kontrollen):**
  - K1: lambda = 0 (m = M ueberall) ergibt kein gebundenes Niveau.
  - K2: Harte Stufe m = 0 fuer r < 10 und m = 200 fuer r > 10 ergibt E(1s1/2) x 10 = 2,04 +- 2 %. Prueft den Loeser
    gegen den MIT-Wert.
  - K3: Zwei Gitter- bzw. Toleranzstufen; die Niveaus aendern sich um weniger als 1e-4 relativ.

## Scheiterregel

- **Verfehlt K2 oder K1:** Der Loeser ist falsch, keine Aussage.
- **V1 verfehlt bei omega^2 <= 0,60:** Das Bild "der Q-Ball wirkt fuer schwere Fermionen wie ein MIT-Beutel" ist fuer
  diese Kopplung falsch.
- **V2 verfehlt:** Das Beutelbild traegt die Niveaustruktur nicht.

## Rechenort

.69 ueber kleintest.sh, CPU-Spur, hoechstens 10 min. Code quark2.py (numpy/scipy, Schiessen und Bisektion), neu
geschrieben.

## Nachtrag vor dem zweiten Lauf (Leitung, 2026-10-01 17:37:21 CEST; Vorhersage und Scheiterregel unveraendert)

- Erster Lauf (quark2.py sha256 75aa4d8078812b94..., zwei Aufrufe ab 17:20:58): beide nach 10 min abgebrochen (Zeitgrenze),
  ohne Ergebnisdatei. Ursachen: Rechenbereich bis zum Profilabbruch (r ~ 40, weit hinter dem Ball), Speichern erst am Ende,
  zwei Toleranzstufen fuer alle omega^2. Selbstanzeige: Laufzeit nicht vorab gemessen.
- Methode, unveraendert in der Physik: quark2_v2.py.
  - Rechenbereich bis Wandende (S < 1e-9 S(0)) plus 3.
  - Zwischenspeichern nach jedem kappa.
  - Zweite Toleranzstufe (K3) nur fuer omega^2 = 0,55 und 0,80.
  - Raster 150 statt 300 Energien, Bisektion 45 statt 60 Schritte.
  - Je omega^2 ein eigener Aufruf; K1 und K2 im Aufruf fuer 0,80.
- Budget lokal gemessen (Rauchtest 17:36:50, Zahlen ohne Bedeutung): Profil 1,2 s, eine kappa-Suche bei omega^2 = 0,55
  mit 48 Niveaus 10,7 s. Je Aufruf also etwa 3 bis 4 min.

## Ergebnis (Leitung, eingetragen 2026-10-01 17:49:50 CEST; Kette .69 cpu6 17:37:31 bis 17:48:45, alle rc = 0)

Code quark2_v2.py (sha256 2c94426d11b8731d..., lokal = .69). Dateien lauf-69-v2/w{055,060,065,070,080}/quark2.json, LAUF-Q2V2.log.

| omega^2 | R_h | E(1s1/2) | E(1s1/2) R_h | E(1p3/2)/E(1s1/2) | E(1p1/2)/E(1s1/2) | gebundene positive Niveaus |
|---|---|---|---|---|---|---|
| 0,55 | 14,381 | 0,16638 | 2,393 | 1,564 | 1,863 | 238 |
| 0,60 | 7,210 | 0,38962 | 2,809 | 1,540 | 1,824 | 126 |
| 0,65 | 4,763 | 0,67937 | 3,236 | 1,506 | 1,756 | 88 |
| 0,70 | 3,514 | 1,01027 | 3,550 | 1,477 | 1,700 | 68 |
| 0,80 | 2,288 | 1,65543 | 3,787 | 1,443 | 1,631 | 51 |

- Kontrollen:
  - K1 (lambda = 0): kein Niveau. Getroffen.
  - K2 (harte Stufe): E(1s1/2) x 10 = 2,0423, MIT 2,043. Getroffen.
  - K3 (zwei Toleranzstufen): groesste relative Differenz 3,7e-10 (omega^2 = 0,55) und 5,1e-9 (0,80). Getroffen.
- **V1 verfehlt:** E(1s1/2) R_h liegt bei 2,39 (0,55) und 2,81 (0,60), ausserhalb [1,7; 2,3]. Nach der Scheiterregel ist das
  Bild "der Q-Ball wirkt fuer schwere Fermionen wie ein MIT-Beutel" in seiner Groessenaussage (E R_h ~ 2,04) fuer diese
  Kopplung und diese Ballgroessen falsch.
- **V2 getroffen:** Reihenfolge 1s1/2 < 1p3/2 < 1p1/2 wie im MIT-Beutel.
  - Verhaeltnisse 1,564 und 1,863 bei 0,55, 1,540 und 1,824 bei 0,60, alle in den Baendern.
  - MIT-Werte: 1,568 und 1,866. Beim groessten Ball liegt die Abweichung unter 0,3 %.
- **V3 getroffen:** Die Niveauzahl steigt mit dem Ball monoton (51 bei 0,80 bis 238 bei 0,55).
- **Deutung nach dem Ergebnis [H], keine Umwertung von V1:** E R_h faellt mit wachsendem Ball (3,79 -> 2,39), die
  Verhaeltnisse naehern sich den MIT-Werten. Die Struktur ist also beutelartig.
  - Die Abweichung der Groesse kommt vermutlich von der weichen Wand. Das Fermion spuert die Masse schon dort, wo S nur
    wenige Prozent unter S(0) faellt; der wirksame Beutelradius ist also kleiner als R_h.
  - Pruefbar waere das mit einem vorab festgelegten wirksamen Radius, etwa S = 0,9 S(0). Das waere ein neuer Test, keine
    Rettung von V1.
- Einordnung: bekannte Physik (Friedberg-Lee-Beutel, MIT-Beutel), fuer unser Profil nachgerechnet. Unser Q-Ball traegt
  gebundene Dirac-Niveaus mit MIT-artiger Struktur. Eine Quark-Behauptung ist das nicht.
