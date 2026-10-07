# Q-STERN-2b: Plan (Runde 15, Code-Agent)

- Folgeauftrag der Leitung claude-primary. Start 2026-10-02 01:22:57 CEST (date), Zeitbox 60 min (bis 02:22:57).
- Plan geschrieben ab 01:27:09 CEST (date). Bindend: KARTE.md (Regel, Kontrollen, Vorhersage).
- Zusaetze der Leitung: Spuren cpu, cpu2, cpu3, cpu4; jeder Aufruf hoechstens 10 min; lokal nur die genannten
  Werkzeuge.

## 1 Code

- qstern2.py aus RUNDE-14/q-stern2 unveraendert kopiert (sha256 gleich). Es gibt keine Hilfsmodule; der Code importiert
  nur numpy und scipy.
- **Codeaenderung noetig, darum qstern2b.py mit Diff qstern2b.diff.** Die Physik ist unveraendert.
  - qstern2.py hat das Fenster der Q-STERN-2-Karte (0,74 .. 0,80 / 1,65 .. 1,80) und die K1-Stelle n = 1 mit Umlauf -1
    fest eingebaut. Beides wirkt auf die Reihenfolge der Kandidaten und auf die Auswertung.
  - Neu sind nur Aufrufparameter: --fenster x_lo,x_hi,rho_lo,rho_hi, --k1-ziel x,rho und --k1-umlauf.
  - Ohne sie verhaelt sich qstern2b.py wie qstern2.py.
- Alle Laeufe: --fenster 0.60,0.70,1.60,1.75 (Karte).
- Auswertung: --k1-ziel 0.6851289044582160933,1.690356597328143 --k1-umlauf 1.
  - Umlauf +1 bei alpha = 0 ist berichtet in RUNDE-09/daten-leiter/DATENPAKET.md, Hauptleiter n = 2: "+1, Umlauf
    aufgeloest".

## 2 Rauchtests und Messungen vor dem Einfrieren (lokal, System-python3, 1 Thread, nice 19, timeout <= 115 s)

- rauch-k1-voll (alpha 0, voller Pfad, h 0,04, Zeilen 0,680/0,685/0,690), 9,8 s:
  - s-Wechsel 0,685 .. 0,690, Richtung +1, s von - nach +
  - Stelle 0,68512880 / 1,69035653, Umlauf +1, Sprung 0,398 rad, aufgeloest
  - Bewiesen: 0,6851289 / 1,6903566
- Kompaktheitsmessung (k2, h 0,04, Profilschritte 0,02/0,01, n-rampe 2), 2|Phi(0)|:

  | alpha | 0,665 | 0,671 | 0,675 | 0,680 | 0,685 |
  |---|---|---|---|---|---|
  | 0,0006 | 0,01653 | - | 0,01518 | - | 0,01400 |
  | 0,0018 | 0,04330 | - | 0,04025 | - | 0,03752 |
  | **0,00041** | - | - | 0,01062 | **0,01018** | 0,00977 |
  | **0,00122** | 0,03116 | **0,02972** | 0,02882 | - | - |

  - **Gewaehlt: alpha_1 = 0,00041, alpha_2 = 0,00122.**
  - Erwarteter Ort: alpha_1 ~0,680 (Lage 0,6851 - 0,47 x 0,01). alpha_2 ~0,671 (Rauchtest unten: 0,6727).
  - Dort ist 2|Phi(0)| ~0,0102 bzw. ~0,0297 bis 0,0288.
  - K2 bestand in allen Messungen (<= 9,2e-10).
- rauch-a2-voll (alpha 0,00122, voll, h 0,04, Zeilen 0,660 .. 0,690, n1 3000, n2 1500), 29,0 s:
  - ein s-Wechsel, 0,670 .. 0,675, Richtung +1
  - Stelle 0,67271477 / 1,67621359, Umlauf +1, Sprung 0,400 rad (aufgeloest, knapp unter 0,4)
  - K5 5,9e-7 (h 0,04)
  - Im Profil-Schiessen bei x = 0,66 erscheinen Ueberlauf-Warnungen (RuntimeWarning) von Probeschuessen. Die Zeilen
    sind gueltig.
- Alle Rauchtests sind regelfremd (lauf-lokal/).

## 3 Zeilen, Gitter, Laufliste

- Stufen: h 0,02 (Profilschritt 0,01) und h 0,01 (Profilschritt 0,005). K3: h 0,02 mit --r-fak 1,5.
- Grobsuche o = 0,660 .. 0,690 im Abstand 0,005 (7 Zeilen).
  - Sie deckt Verschiebungen von +0,005 bis -0,025 ab. Das reicht ueber V2 (k bis -0,71 bei 0,03: -0,021) hinaus.
- **Nicht gerechnet:** Fensterteile 0,600 .. 0,660 und 0,690 .. 0,700.
  - Dort liegen nach dem Datenpaket die Stellen n = 3 (0,6314 / 1,6526) und n = 4 (0,6014 / 1,6281), beide im Fenster
    der Karte.
  - "Nicht gesehen" ist darum ohnehin nicht erreichbar.
  - Ohne s-Wechsel in o ist der Ausgang "Unentschieden".
- K3-Zeilen (Klammer nach den Rauchtests, je 4 Zeilen): alpha_1 0,675 .. 0,690; alpha_2 0,665 .. 0,680.
- **Lokalisierung zuerst** (Code wie Q-STERN-2):
  - Zeilen, dann s-Wechsel, dann Lokalisierung, kleines Rechteck und K5
  - Erst danach Zwischenreihen (n-mid 1) und Streifen
  - Kandidaten im Fenster zuerst, hoechstens 3
- Gemeinsame Argumente: --modell kg --n-mid 1 --max-kand 3 --budget 420 --pole nein --n-rampe 2
  --fenster 0.60,0.70,1.60,1.75.
- Laufliste (.69, kleintest.sh, /home/fmh/fmhc-physics-remote/runde15-q-stern2b, aus/, logs/); vier Starter, je einmal
  per nohup:
  - cpu: k1-h0.02; a1-voll-o-h0.02; a1-voll-k3; a2-voll-o-h0.02; a2-voll-k3
  - cpu2: k1-h0.01; a1-voll-o-h0.01; a2-voll-o-h0.01
  - cpu3: k2-a1 (x 0,675/0,680/0,685); k2-a2 (x 0,665/0,671/0,675); a1-null-o-h0.02; a1-null-k3; a2-null-o-h0.02;
    a2-null-k3
  - cpu4: a1-null-o-h0.01; a2-null-o-h0.01
- Gemessene Dauer:
  - Q-STERN-2 mit gleichem Code und 7 Zeilen: h 0,02 100 bis 174 s, h 0,01 209 bis 347 s, K3 82 bis 140 s,
    k2 73 bis 113 s, K1 43 s bzw. 88 s
  - Rauchtest hier (h 0,04, 7 Zeilen): 29 s
  - Erwartetes Ende aller Starter ~20 min nach dem Start
- Auswertung: qstern2b.py auswertung --aus aus --alphas 0.00041,0.00122 --fenster 0.60,0.70,1.60,1.75
  --k1-ziel 0.6851289044582160933,1.690356597328143 --k1-umlauf 1 (Spur cpu, nach den Laeufen).

## 4 Auswertung (Regel der Karte, wortgleich; Umsetzung wie Q-STERN-2)

- **Gesehen:**
  - lokalisiertes, aufgeloestes Rechteck (< 0,4 rad) mit Umlauf +-1 auf beiden Stufen, dazu ein Vorzeichenwechsel von s
  - Lage im Fenster 0,60 <= omega^2 <= 0,70, 1,60 <= rho <= 1,75
  - Stufen auf 1e-4 gleich, K3 bestanden
- **Nicht gesehen:** im Fenster kein Vorzeichenwechsel auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.
- Kontrollen:
  - K1: alpha = 0 gibt die n = 2-Stelle auf 1e-4, Umlauf auf beiden Stufen wie bei alpha = 0 berichtet (+1)
  - K2: Hintergrund auf zwei Gittern auf 1e-6 relativ
  - K3: R gegen 1,5 R, Lage auf 1e-4
  - K5: nur berichten, Vergleich Q-STERN-2 (1,2e-8 bis 3,0e-8 bei h 0,02/0,01, 8,6e-9 einmal)
  - Verfehlt K1 oder K2: nicht auswertbar
- Lesart (wie Q-STERN-2): Kandidat auf h 0,02 und h 0,01 mit |d omega^2|, |d rho| < 1e-4, beide aufgeloest, |Umlauf| = 1,
  beide im Fenster; K3-Kandidat auf 1e-4 zur h-0,02-Lage.
- Zuordnung zur n = 2-Stelle: Die Stelle muss auf dem Ast liegen, der stetig aus der K1-Stelle hervorgeht (Richtung +1,
  rho 1,66 .. 1,70 in den Zeilen o). Eine andere Stelle im Fenster wuerde getrennt berichtet.
- Groessen:
  - Verschiebung = omega*^2 - K1-Lage derselben Stufe
  - Koeffizient k = Verschiebung / Kompaktheit am Ort, 2|Phi(0)| des Mittelprofils im Rechteck, h 0,01
  - voll : Cowling = Verhaeltnis der omega^2-Verschiebungen

## 5 Vorab (Agent, nach den Rauchtests; keine echten Vorhersagen, der Rauchtest zeigt die alpha_2-Lage schon)

- E-1 K1 und K2 bestehen ~90 %. Der Sprung 0,398 rad im K1-Rauchtest liegt knapp unter 0,4; die Rechteckverfeinerung
  greift erst ab 0,4.
- E-2 Gesehen in allen vier Faellen ~80 %.
- E-3 k (voll) bei alpha_2 um -0,42 (Rauchtest: -0,0124/0,0297); bei alpha_1 aehnlich; beide in [-0,71; -0,24]: ~80 %.
- E-4 voll : Cowling in [0,9; 1,1] ~75 %.
