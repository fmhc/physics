# Q-STERN-2: Plan (Runde 14, Code-Agent)

- Auftrag der Leitung claude-primary. Start 2026-10-01 23:30:47 CEST (date), Zeitbox 90 min (bis 01:00:47).
- Plan geschrieben ab 23:55:29 CEST (date). Bindend: KARTE.md (Modell, Kompaktheitsziel, Vorhersage, K1 bis K5, Regel,
  Plan-Vorgabe).
- Zusaetze der Leitung (Auftrag): Spuren cpu, cpu2, cpu3, cpu4; Zeitbox 90 min.
- Code: qstern2.py = Kopie von RUNDE-13/q-stern/qstern.py, erweitert um psi. Diff qstern2.diff. Starter start-cpu.sh,
  start-cpu2.sh, start-cpu3.sh, start-cpu4.sh.

## 1 Herleitung (Einzelheiten HERLEITUNG.md)

- delta rho_E = sigma cos(rho t), sigma = 2 [omega f ((omega + rho) a + (omega - rho) b) + f' (a' + b') + U' f (a + b)];
  Zeit-, Gradienten- und Potentialterm sind alle enthalten.
- u = r psi: u'' = 2 alpha [(Pa - Pb rho) y1 + (Pa + Pb rho) y2 + f' (y1' + y2')], Pa = (omega^2 + U') f - f'/r,
  Pb = omega f.
- Kanaele: y1'' += (Ea - Eb rho) u (geschlossen), y2'' += (Ea + Eb rho) u (offen), Ea = f (2 omega^2 - U'),
  Eb = 2 omega f.
- psi kommt nur mit f multipliziert vor; die Kanalasymptotik bleibt (Karte bestaetigt).
- Randbedingungen: u(0) = 0; aussen u' = 0, also psi = c0/r.
- Abweichung von der Karte in der Auslesung (Regel unveraendert):
  - Das System ist mit psi nicht mehr symmetrisch, der Wronski-Satz faellt weg.
  - W stammt darum aus der exakten Abhaengigkeitsbedingung (3 regulaere, 2 stille Loesungen, u eliminiert):
    W = Omega(Ya^, Z_perp) + i Omega(Yb^, Z_perp).
  - Bei alpha = 0 ist es das alte W.
  - Den Vertreter Z2 - gamma Z1 nach dem Rauchtest gewaehlt: Er beseitigt Pole von W (dazu Abschnitt 2).
  - --psi null rechnet den unveraenderten Q-STERN-Pfad (Cowling).

## 2 Rauchtests und Messungen vor dem Einfrieren (lokal, System-python3, 1 Thread, nice 19, timeout <= 118 s)

- rauch-k1-voll (alpha 0, voller Pfad, h 0,04, Zeilen 0,795/0,800), 9,8 s:
  - Stelle 0,79767660 / 1,74461748, Umlauf -1, Sprung 0,359 rad, aufgeloest
  - s bei 0,80 = -2,445e-3 (Q-STERN-Rauchtest: -2,4e-3)
- Kompaktheitsmessung (Kommando k2, h 0,04, Profilschritte 0,02/0,01, n-rampe 2), 2|Phi(0)|:

  | alpha | x 0,775 | x 0,784/0,785 | x 0,793 | x 0,7977 |
  |---|---|---|---|---|
  | 0,001 | - | 0,01209 (0,784) | 0,01154 | 0,01127 |
  | 0,003 | - | 0,03341 (0,784) | 0,03203 | 0,03135 |
  | **0,00087** | 0,01110 | 0,01053 (0,785) | **0,01010** | 0,00986 |
  | **0,0027** | 0,03177 | **0,03027 (0,785)** | 0,02914 | 0,02851 |

  - **Gewaehlt: alpha_1 = 0,00087, alpha_2 = 0,0027.**
  - Begruendung: Am erwarteten Ort, alpha_1 ~0,793, alpha_2 ~0,784 (Rauchtests unten), ist 2|Phi(0)| ~0,0101 bzw.
    ~0,0303.
  - K2 bestand in allen vier Messungen, relativ <= 1,5e-9.
- rauch-a2-voll (alpha 0,0027, h 0,04, Zeilen 0,775 .. 0,800), erste Codefassung, 63 s:
  - Stelle 0,78364321 / 1,72975971, Umlauf -1
  - Zusaetzlich Nullstellen von Im W mit |s|/median 1e4 .. 4e5 bei rho ~0,36 und 1,57 .. 1,61 (Pole von W)
  - Ursache: Der u-Block (Yu, Z2) wurde singulaer, weil Z2 nach innen einen grossen geschlossenen Anteil aufnimmt.
  - Behebung: Z2 durch Z2 - gamma Z1 ersetzt (Spaltenoperation im stillen Raum, Lage exakt unveraendert).
- rauch-a2-voll-b (dieselben Zeilen, Fassung mit Behebung), 31,8 s:
  - Pole weg, nur noch der Ast der Stelle
  - Stelle 0,78364321 / 1,72975971, ziffergleich zur ersten Fassung
  - Umlauf -1, Sprung 0,370 rad, aufgeloest
  - K5-Rest 5,4e-7 (h 0,04), sigma_min/sigma_max 5,5e-11
- rauch-a2-cow (alpha 0,0027, Cowling, h 0,04): 0,78331043 / 1,73013699, Umlauf -1, aufgeloest, ~26 s.
- rauch-a1-voll-h0.02 (alpha 0,00087, voll, h 0,02, Zeilen 0,785 .. 0,800), 46,4 s:
  - s-Wechsel 0,790 .. 0,795
  - Stelle 0,79290507 / 1,73952747, Umlauf -1, Sprung 0,380 rad, aufgeloest
  - K5-Rest 2,45e-8, sigma_min/sigma_max 5,3e-12
  - Zeiten: Profile 11 s (4 Zeilen), je Zeile 2,4 s, Lokalisierung bis 37 s, Rechteck bis 45 s
- Alle Rauchtests sind regelfremd (lauf-lokal/).

## 3 Zeilen, Gitter, Laufliste

- Stufen: h = 0,02 (Profilschritt 0,01) und h = 0,01 (Profilschritt 0,005), wie Q-STERN. K3: h = 0,02 mit --r-fak 1,5.
- Grobsuche (Zeilen im Abstand 0,005):
  - o = 0,770 .. 0,800 (7 Zeilen)
  - u = 0,740 .. 0,770 (7 Zeilen)
  - Zusammen decken sie das Fenster 0,74 .. 0,80 ab.
- K3-Zeilen (Klammer aus den Rauchtests, je 4 Zeilen): alpha_1 0,785 .. 0,800; alpha_2 0,775 .. 0,790.
- **Lokalisierung zuerst** (Code, cmd_familie):
  - Reihenfolge: Zeilen -> s-Wechsel aus den Zeilen -> Lokalisierung und kleines Rechteck (Kandidaten im Fenster zuerst,
    hoechstens 3) -> K5 -> erst danach Zwischenreihen (n-mid 1) und Streifen.
  - Budget je Aufruf 420 s. Die Lokalisierung startet nach Messung bei ~40 s (h 0,02) bzw. geschaetzt ~150 s (h 0,01).
  - Reserve 90 s vor jeder Lokalisierung, 40 s je Schritt, 60 s vor dem Rechteck (Code wie Q-STERN).
  - Streifen und Zwischenreihen bekommen nur den Rest. Sie sind nur fuer "Nicht gesehen" noetig.
- Gemeinsame Argumente: --modell kg --n-mid 1 --max-kand 3 --budget 420 --pole nein --n-rampe 2; n1 4000, n2 2000
  (dicht 1,5 .. 1,95), n_zw 1500, rdx 4e-4, rdrho 2e-3, r_nx 5 (Vorgaben).
  - n-rampe 2 nur fuer die kleinen alpha; das konvergierte Phi haengt nicht von der Rampe ab (Toleranz 1e-9).
- Laufliste (.69, kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde14-q-stern2, aus/, logs/); vier Starter, je
  einmal per nohup:
  - cpu: k1-h0.02; a1-voll-o-h0.02; a1-voll-k3; a2-voll-o-h0.02; a2-voll-k3; a1-voll-u-h0.02; a2-voll-u-h0.02
  - cpu2: k1-h0.01; a1-voll-o-h0.01; a2-voll-o-h0.01; a1-voll-u-h0.01; a2-voll-u-h0.01
  - cpu3: k2-a1; k2-a2; k4-h0.02; a1-null-o-h0.02; a1-null-k3; a2-null-o-h0.02; a2-null-k3; a1-null-u-h0.02;
    a2-null-u-h0.02
  - cpu4: k4-h0.01; a1-null-o-h0.01; a2-null-o-h0.01; a1-null-u-h0.01; a2-null-u-h0.01
- Gemessene bzw. geschaetzte Dauer:
  - h 0,02 mit 7 Zeilen: 1,5 bis 2 min bis zum Rechteck, danach Streifen bis zum Budget
  - h 0,01: etwa das Vierfache vor dem Rechteck (Profile), 4 bis 6 min
  - Jeder Aufruf hoechstens 10 min (systemd), Programmbudget 420 s
  - Was bis zum Ende der Zeitbox nicht gelaufen ist, gilt als "nicht gerechnet". Laufende Hauptlaeufe beschreibe ich im
    Bericht.
- Kontrollen:
  - K1: alpha 0, voller Pfad, Zeilen 0,795/0,800, beide Stufen; Lokalisierung und Rechteck
  - K2: k2 je alpha, x = 0,775/0,785/0,793/0,7977, h 0,02 (Profilschritte 0,01/0,005)
  - K3: siehe oben
  - K4: Cowling (--psi null), alpha 0,01, Zeilen 0,75/0,76 plus Zwischenreihe 0,755 (wie Q-STERN a0.01-*-pa,
    n_zw 1500), --max-kand 0, n-rampe 6 wie Q-STERN, beide Stufen.
    - Vergleich an denselben Zeilen: rho und s des Asts (Richtung +1) bei 0,750 und 0,755.
    - Lineare Interpolation x* = x1 + (x2 - x1) s1/(s1 - s2) gegen Q-STERN.
    - Q-STERN-Werte (aus der JSON per jq): h 0,02 s 2,2400878e-3 / -1,7224180e-3, also x* = 0,7528266; h 0,01
      s 2,2276828e-3 / -1,7320748e-3, also x* = 0,7528129.
    - Bestanden, wenn |dx*| <= 1e-6 auf beiden Stufen.
  - K5: an jeder lokalisierten Stelle des vollen Pfads (Code k5_voll), Rest relativ < 1e-8.
- Auswertung: qstern2.py auswertung --aus aus --alphas 0.00087,0.0027 (auf der .69, nach den Laeufen; bei Zeitmangel
  auf dem Stand der fertigen Laeufe). K4 und K5 werden per jq aus den JSON gelesen.

## 4 Auswertung (wortgleich zur Regel der Karte; Umsetzung qstern2.py cmd_auswertung)

Regel (bindend, je alpha und je Rechnung voll/Cowling):
- **Gesehen:**
  - lokalisiertes, aufgeloestes Rechteck (groesster Phasensprung < 0,4 rad) mit Umlauf +-1 auf beiden Stufen, dazu ein
    Vorzeichenwechsel von s
  - Lage im Fenster 0,74 <= omega^2 <= 0,80, 1,65 <= rho <= 1,80
  - Stufen auf 1e-4 gleich, K3 bestanden
- **Nicht gesehen:** im Fenster kein Vorzeichenwechsel von s auf beiden Stufen, alle Rechtecke aufgeloest mit Umlauf 0.
- **Unentschieden:** alles andere.
- Kontrollen: K1 alpha = 0 gibt die bewiesene Stelle auf 1e-4, Umlauf -1 auf beiden Stufen. K2 Hintergrund auf zwei
  Gittern, omega, Q, E und Phi(0) auf 1e-6 relativ. K3 Aussenrand R und 1,5 R, Lage auf 1e-4. K4 der neue Code mit
  psi = 0 reproduziert die Lage aus Q-STERN bei alpha = 0,01 auf 1e-6. K5 Restpruefung der psi-Gleichung an der
  gefundenen Stelle, relativ < 1e-8. Verfehlt K1, K2 oder K4: nicht auswertbar.

Umsetzung (Lesart, vor den Laeufen festgelegt, wie Q-STERN):
- "Rechteck" = kleines Rechteck um die lokalisierte Stelle (omega*^2 +- 4e-4, rho* +- drho).
- "Auf beiden Stufen, Stufen gleich": Kandidat auf h 0,02 und h 0,01 mit |d omega^2| < 1e-4 und |d rho| < 1e-4, beide
  aufgeloest, |Umlauf| = 1, beide im Fenster.
- K3 bestanden: Der K3-Lauf hat einen Kandidaten auf 1e-4 zur h-0,02-Lage. Fehlt der K3-Lauf, ist hoechstens
  "Unentschieden" moeglich. Ein K3-Lauf ohne passenden Kandidaten macht das betroffene alpha nicht auswertbar.
- "Nicht gesehen": Beide Stufen decken 0,74 .. 0,80 ab (o und u), alle Zeilen gueltig, kein s-Wechsel mit Mittelpunkt
  im Fenster, alle Streifen aufgeloest mit Umlauf 0.
- K2 je alpha, K1 fuer alle; K4 fuer alle (per jq, Kriterium oben).
- Verschiebung gegen alpha = 0: omega*^2 - 0,797677 (bewiesene Stelle).
- Verhaeltnis voll zu Cowling: (omega*^2_voll - 0,797677)/(omega*^2_Cowling - 0,797677) je Stufe.
- Kompaktheit am Ort: 2|Phi(0)| des Mittelprofils im Rechteck (kompaktheit_ort).

## 5 Vorab (Agent, nach den Rauchtests, vor den Hauptlaeufen)

- Die Rauchtests (h 0,04 bzw. h 0,02) kennen den Ausgang schon fast:
  - alpha_2 voll 0,78364, Cowling 0,78331
  - alpha_1 voll 0,79291
  - Diese Vorab-Saetze sind darum keine echten Vorhersagen, nur Erwartungen fuer die Hauptlaeufe.
- E-1 K1, K2, K4 bestehen: ~90 %.
- E-2 Gesehen fuer alle vier Kombinationen (alpha_1/alpha_2, voll/Cowling): ~80 %.
- E-3 Verhaeltnis voll zu Cowling zwischen 0,9 und 1,05 bei beiden alpha: ~70 % (Rauchtest alpha_2: ~0,977).
- E-4 K5 auf h 0,02 verfehlt (Rauchtest 2,45e-8, RK4-Fehler O(h^4)), auf h 0,01 bestanden: ~60 %.
- E-5 V1 der Leitung (Cowling auf +-20 % der vorhergesagten Verschiebung): Die Vorhersagen nennen Lagen fuer alpha ~0,001
  und ~0,003; meine alpha sind 0,00087 und 0,0027. Bei alpha_2 erwarte ich nach dem Rauchtest eine Cowling-Verschiebung
  von ~-0,0144. Die Steigung -4,5 alpha gaebe -0,0122, also 18 % mehr, knapp an der Grenze.
  - Vergleich je alpha: mit der Steigung -4,5 alpha bei meinem alpha und mit der Lage der Leitung.
