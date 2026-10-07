# ERGEBNIS SPROSSEN-VORAB (Runde 20)

- Code-Agent. Start 2026-10-02 17:07:55 CEST (date). Plan-Entwurf ab 17:16:21 CEST, vor jedem Lauf. Pflichtpruefung L4
  (Durchgang 1) 15:18:24 bis 15:24:55 UTC, bestanden. Plan eingefroren 17:27:11 CEST
  (PLAN.md.eingefroren-20261002-172711), danach erst die Testlaeufe (15:27:18 bis 15:35:25 UTC), formale Auswertung
  15:35:35 UTC. Kein Nachtrag. Bericht ab 17:36:17 CEST (date), Stand 17:41:58 CEST (date). Uhrzeiten der .69 in UTC
  (CEST = UTC + 2).
- Code: code/sprossen_vorab.py (neu: Annahme ueber Rang und Stetigkeit, Befehle test, ausw, fortfehler; nach dem
  Einfrieren unveraendert, derselbe Code fuer L4 und Test); code/huellen_leiter3.py, huellen_leiter2.py, stille3.py,
  beutel.py unveraendert aus HUELLEN-LEITER-3.
- Verbindlich nach Karte und Kartennachtrag 1 der Leitung (17:09:55, Offenlegung der Stelle bei R = 40,49).
- Explorativ (v3). Alles modellintern (Modell M2, l = 0, linear, klassisch), keine Messdaten. Deutungen sind
  Hypothesen [H].

## 1 Ergebnis zuerst

1. **Alle 12 vorhergesagten Sprossen sind da, wo die Regel sie hinlegt.** Jede wurde vom ersten Newton-Start aus
   gefunden und nach dem vorab eingefrorenen Kriterium angenommen, auf beiden Gitterstufen. k = 0 bis 3 (dritte
   Sprosse): abs(Delta R) <= 0,0045 bei Toleranz 0,06. k = 4 bis 7 (zwei neue Sprossen je Kurve): abs(Delta R) 0,020
   bis 0,095 bei Toleranz 0,12. **V0, V1, V2 (8 von 8) und V3 (12 von 12 Schritten) sind eingetroffen.**
2. **Bedeutung nach Karte (formal):** "Die Sprossenregel sagt neue stille Stellen vorab gewertet voraus [H, im Modell
   gestuetzt]." Der Ausloeser der Gegenaussage ("Abweichung > 0,3 oder nicht gefunden") trat nicht auf; die groesste
   Abweichung ist 0,095 (k = 7, 43,03).
3. **Eine Sprosse ist nicht blind (Kartennachtrag 1):** k = 5 / 40,51 liegt genau auf der schon bekannten Stelle aus
   HUELLEN-LEITER-2 (R = 40,4874, rho = 1,2484145; omega^2 gleich auf 2e-15). Die Stelle liegt also auf k = 5.
   Nebenlesart V2 ohne diese Sprosse: 7 von 7 Treffern, eingetroffen.
4. **Kurvenzuordnung ohne Knotenzahl, vorab geprueft:** Rang k auf beiden Stufen, Fortsetzungsfehler hoechstens 0,018
   des Nachbarabstands (Schwelle 0,1). L4 bestand im ersten Durchgang (12 von 12). Mit der Variante F hat der Umlauf auch
   auf k = 4 bis 7 die Konvention der Runde 18. Die Pruefung fand die schwache Stelle des Kriteriums: Zwei Sprossen weit
   aus den ersten drei Stellen nach der Geburt einer Kurve liegt der Fehler bei bis 0,22 und auf k = 2, 3 und 7 ueber der
   Schwelle. Im Testbereich (reife Kurven) blieb er unter 0,02 (vor dem Einfrieren an den Zeilennullstellen geprueft).
5. **Alle Abweichungen sind negativ und wachsen mit der Reichweite [H].** Der Sprossenabstand schrumpft weiter, die
   lineare Regel mit dem letzten Abstand liegt deshalb zu weit aussen. Beispiel k = 7: 2,379 -> 2,345 -> 2,318, die
   zweite Sprosse brauchte 79 % der Toleranz. Weiter aussen braucht die Regel einen schrumpfenden Abstand.

## 2 Pflichtpruefung L4 (vor dem Einfrieren)

- **Ein Durchgang, bestanden: 12 von 12 bekannten Stellen angenommen** (Entwurf unveraendert, code/sprossen_vorab.py
  b06fbb8a..., 6 Teillaeufe 15:18:24 bis 15:24:45 UTC, Auswertung 15:24:55 UTC, aus/l4-d1/l4-auswertung.json). Kein
  zweiter Durchgang, das Kriterium wurde nicht geaendert.
- Ziele: die 8 Sprossen aus HUELLEN-LEITER-3 und die letzte Stelle der Runde 18 fuer k = 4 bis 7 (Nr 80, 86, 82, 87),
  R wie in der Karte. Fortsetzung jeweils aus den drei bekannten Stellen davor.

| k | R Karte | R gefunden | Abstand zur bekannten Lage (omega^2 / rho) | F-Umlauf St1/St2 (bekannt) | S-Umlauf | Stufenabstand | Fortsetzungsfehler / d_nb | max abs(W) |
|---|---|---|---|---|---|---|---|---|
| 0 | 39,594 | 39,59426 | 1,2e-14 / 4,0e-15 | +1/+1 (+1) | +1/+1 | 2,9e-10 | 3,1e-9 / 0,1617 = 1,9e-8 | 4,6e-11 |
| 0 | 42,004 | 42,00367 | 8,7e-14 / 3,3e-15 | -1/-1 (-1) | -1/-1 | 2,9e-10 | 1,9e-9 / 0,1613 = 1,2e-8 | 6,8e-11 |
| 1 | 40,506 | 40,50636 | 1,4e-14 / 5,2e-14 | +1/+1 (+1) | +1/+1 | 2,5e-10 | 4,9e-8 / 0,00797 = 6,1e-6 | 2,0e-10 |
| 1 | 42,613 | 42,61313 | 3,6e-13 / 2,7e-13 | -1/-1 (-1) | -1/-1 | 2,4e-10 | 3,7e-8 / 0,00720 = 5,2e-6 | 3,1e-10 |
| 2 | 40,229 | 40,22944 | 3,8e-14 / 2,2e-14 | -1/-1 (-1) | -1/-1 | 3,0e-10 | 4,2e-7 / 0,00809 = 5,2e-5 | 8,4e-11 |
| 2 | 42,351 | 42,35113 | 3,5e-14 / 1,3e-14 | +1/+1 (+1) | +1/+1 | 2,8e-10 | 2,5e-7 / 0,00729 = 3,4e-5 | 1,1e-10 |
| 3 | 39,765 | 39,76541 | 2,2e-15 / 1,0e-14 | +1/+1 (D2: +1) | -1/-1 | 5,5e-10 | 3,4e-6 / 0,01357 = 2,5e-4 | 8,9e-11 |
| 3 | 41,912 | 41,91233 | 6,9e-15 / 4,9e-14 | -1/-1 (D2: -1) | +1/+1 | 4,9e-10 | 2,2e-6 / 0,01223 = 1,8e-4 | 5,3e-11 |
| 4 | 36,92 | 36,91656 | 4,3e-9 / 1,5e-8 (Nr 80) | +1/+1 (+1) | -1/-1 | 1,1e-9 | 2,2e-5 / 0,02137 = 1,0e-3 | 2,0e-11 |
| 5 | 38,26 | 38,25564 | 2,0e-9 / 7,2e-9 (Nr 86) | +1/+1 (+1) | +1/+1 | 1,6e-9 | 4,2e-5 / 0,02484 = 1,7e-3 | 1,1e-10 |
| 6 | 37,19 | 37,19029 | 1,4e-9 / 7,2e-9 (Nr 82) | -1/-1 (-1) | -1/-1 | 2,5e-9 | 1,5e-4 / 0,03063 = 4,8e-3 | 4,1e-11 |
| 7 | 38,27 | 38,27163 | 8,9e-10 / 7,2e-9 (Nr 87) | -1/-1 (-1) | -1/-1 | 3,4e-9 | 3,7e-4 / 0,03285 = 1,1e-2 | 7,8e-11 |

- Bekannte Lage der HL3-Sprossen: S-Wurzel (Abstand ~1e-13). Bekannte Lage der Runde-18-Stellen: Halbierungslage, auf
  ~1e-8 genau. Rang = k an allen 12 auf beiden Stufen, sigma2/sigma1 <= 3,1e-10, F-Rechteck im ersten Versuch
  aufgeloest (groesster Sprung 0,33 bis 0,39 rad, 68 bis 86 Randpunkte). F gegen S an der Wurzel <= 1,2e-13.
- F-Umlauf = bekannter Umlauf an allen 12, auf k = 4 bis 7 erstmals geprueft. S dreht k = 3 (beide) und k = 4 (Nr 80).
- abs(W) < 1e-10 woertlich auf beiden Stufen an 8 von 12; darueber k = 1 (beide, bis 3,1e-10), k = 2 / 42,351
  (1,09e-10) und k = 5 / 38,26 (1,12e-10), alle unter der Kartengrenze 1e-9.
- **Fortsetzungsfehler an allen bekannten Stellen** (Befehl fortfehler, aus/fortfehler.json, im Verhaeltnis zum
  Nachbarabstand gap der Runde 18):
  - Der Fehler ist am groessten kurz nach der Geburt einer Kurve und faellt dann entlang der Kurve schnell.
  - Ein Sprossenschritt, Maximum je Kurve (alle unter 0,1): k = 0: 0,0018; k = 1: 0,029; k = 2: 0,061 (Nr 17);
    k = 3: 0,073 (Nr 24); k = 4: 0,020; k = 5: 0,024; k = 6: 0,030; k = 7: 0,039 (Nr 75). Fuer k = 0 bis 3 ab Nr 60
    (R >= 31,7) hoechstens 8,5e-4 (k = 3, Nr 65); an den letzten Stellen von k = 4 bis 7 0,0010 bis 0,011.
  - Zwei Sprossenschritte, Maximum je Kurve (jeweils aus den ersten drei Stellen nach der Geburt): k = 0: 0,0042;
    k = 1: 0,087; **k = 2: 0,200 (Nr 22); k = 3: 0,221 (Nr 30)**; k = 4: 0,068; k = 5: 0,078; k = 6: 0,093;
    **k = 7: 0,124 (Nr 87, aus Nr 49, 57, 66)**. Drei Werte liegen also ueber der Schwelle 0,1. Danach faellt der Fehler,
    z. B. k = 4: 0,068 (Nr 48) -> 0,028 -> 0,015 -> 0,0089 -> 0,0056 (Nr 80); k = 5: 0,078 -> 0,031 -> 0,016 -> 0,0096;
    k = 6: 0,093 -> 0,034; k = 3 an Nr 83: 0,0020.
- **Zusatzpruefung vor dem Einfrieren (nach dem 0,124-Befund, Kriterium unveraendert):** Die Fortsetzung des Tests (letzte
  drei Stellen der Runde 18) gegen die Zeilennullstellen mit Rang k an den 8 HL3-Wurzeln (R 39,59 bis 42,61, nur Lagen,
  keine Vorzeichen; hilfs/fort-zeilen.jq): Fehler / d_nb hoechstens 0,0044 (k = 4), 0,0040 (k = 5), 0,0141 (k = 6),
  0,0158 (k = 7 bei R = 42,61). Damit blieb die Schwelle im Testbereich mit Faktor >= 5 frei. Im Test selbst kam
  0,018 (k = 7, 42,94) heraus.
- **V0 (erster Durchgang): eingetroffen.**

## 3 Vorhergesagt gegen gefunden

- Je Sprosse und Stufe: Newton (S) ab omega^2(R vorhergesagt) aus der Tabelle der Stufe 1 und rho aus der
  Kurvenfortsetzung; Pruefungen an der S-Wurzel; F-Newton ab der S-Wurzel und F-Rechteck. Alle 24 Faelle im ersten Start
  (Versuch 0), Newton in 2 bis 4 Schritten.
- R gefunden = Rchi an der S-Wurzel, Stufe 1. omega^2, rho: S-Wurzel Stufe 1. Stufenabstand = max(abs(d omega^2),
  abs(d rho)) zwischen den S-Wurzeln beider Stufen. Stetigkeitsmass = abs(rho - rho_fort(R)) / d_nb, Stufe 1 (Stufe 2
  gleich auf 3 Stellen). Rang auf beiden Stufen = k. F-Rechteck: erster Versuch, groesster Sprung 0,32 bis 0,40 rad,
  68 bis 84 Randpunkte, Halbbreite 1,7e-4 bis 2,3e-4.

| k | R vorhergesagt (Tol.) | R gefunden | Delta R | omega^2 | rho | F-Umlauf St1 / St2 (aufgeloest) | S-Umlauf St1 / St2 | Stufenabstand | Fortsetzungsfehler / d_nb = Stetigkeitsmass | max abs(W) | max sigma2/sigma1 | Treffer |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 44,414 (0,06) | 44,4130 | -0,0010 | 0,7591355552 | 1,0240330663 | +1 / +1 (ja / ja) | +1 / +1 | 2,8e-10 | 1,5e-9 / 0,1609 = 9,3e-9 | 3,8e-11 | 3,9e-11 | ja |
| 1 | 44,720 (0,06) | 44,7193 | -0,0007 | 0,7589205641 | 1,1848372985 | +1 / +1 (ja / ja) | +1 / +1 | 2,2e-10 | 3,3e-8 / 0,00653 = 5,0e-6 | 2,9e-10 | 2,9e-10 | ja |
| 2 | 44,473 (0,06) | 44,4707 | -0,0023 | 0,7590948256 | 1,1915620659 | -1 / -1 (ja / ja) | +1 / +1 | 2,5e-10 | 1,4e-7 / 0,00661 = 2,1e-5 | 8,8e-11 | 9,1e-11 | ja |
| 3 | 44,059 (0,06) | 44,0545 | -0,0045 | 0,7593909956 | 1,2029657905 | +1 / +1 (ja / ja) | -1 / -1 | 4,4e-10 | 1,4e-6 / 0,01108 = 1,3e-4 | 3,5e-11 | 3,6e-11 | ja |
| 4 | 39,13 (0,12) | 39,1099 | -0,0201 | 0,7633971064 | 1,2296064473 | -1 / -1 (ja / ja) | +1 / +1 | 9,4e-10 | 1,3e-5 / 0,01915 = 6,9e-4 | 8,2e-11 | 8,3e-11 | ja |
| 4 | 41,33 (0,12) | 41,2931 | -0,0369 | 0,7615088534 | 1,2241040530 | +1 / +1 (ja / ja) | -1 / -1 | 8,3e-10 | 4,4e-5 / 0,01725 = 2,5e-3 | 5,3e-11 | 5,4e-11 | ja |
| 5 | 40,51 (0,12) | 40,4874 | -0,0226 | 0,7621818033 | 1,2484145323 | -1 / -1 (ja / ja) | -1 / -1 | 1,4e-9 | 2,5e-5 / 0,02237 = 1,1e-3 | 3,7e-11 | 3,7e-11 | ja, nicht blind |
| 5 | 42,76 (0,12) | 42,7051 | -0,0549 | 0,7603913824 | 1,2412012975 | +1 / +1 (ja / ja) | +1 / +1 | 1,2e-9 | 8,4e-5 / 0,02025 = 4,1e-3 | 7,3e-11 | 7,4e-11 | ja |
| 6 | 39,51 (0,12) | 39,4855 | -0,0245 | 0,7630572959 | 1,2796376574 | +1 / +1 (ja / ja) | +1 / +1 | 2,2e-9 | 7,7e-5 / 0,02760 = 2,8e-3 | 9,0e-11 | 9,1e-11 | ja |
| 6 | 41,83 (0,12) | 41,7590 | -0,0710 | 0,7611317175 | 1,2691386315 | -1 / -1 (ja / ja) | -1 / -1 | 1,9e-9 | 2,5e-4 / 0,02499 = 1,0e-2 | 4,5e-11 | 4,6e-11 | ja |
| 7 | 40,65 (0,12) | 40,6170 | -0,0330 | 0,7620716687 | 1,3040022719 | +1 / +1 (ja / ja) | -1 / -1 | 2,9e-9 | 1,5e-4 / 0,02978 = 5,2e-3 | 4,0e-11 | 4,1e-11 | ja |
| 7 | 43,03 (0,12) | 42,9354 | -0,0946 | 0,7602161237 | 1,2913762582 | -1 / -1 (ja / ja) | +1 / +1 | 2,5e-9 | 4,9e-4 / 0,02710 = 1,8e-2 | 4,9e-11 | 4,9e-11 | ja |

- **Gemessene Sprossenabstaende** (Fortsetzung der Runde-18-Reihe; letzter Abstand vor dem Test in Klammern):
  k = 0: (2,411) 2,409; k = 1: (2,107) 2,106; k = 2: (2,122) 2,120; k = 3: (2,147) 2,142; k = 4: (2,206) 2,193, 2,183;
  k = 5: (2,248) 2,232, 2,218; k = 6: (2,322) 2,295, 2,274; k = 7: (2,379) 2,345, 2,318.
- F gegen S an allen 12 neuen Wurzeln <= 1,5e-13, auch bei R = 44,7 (jenseits aller bisher mit F gerechneten Stellen).
- S-Umlauf weicht vom F-Umlauf ab an k = 2 (44,47), k = 3 (44,05), k = 4 (beide) und k = 7 (beide); auf k = 2 ist das
  neu (bis 42,35 gleich). Das passt zum Bild aus HUELLEN-LEITER-2, dass die S-Konvention mit wachsendem R von oben nach
  unten durch die Kurven kippt [H]. Gewertet wird nach Plan nur F.
- abs(W) < 1e-10 woertlich an 11 von 12; k = 1 / 44,72: 2,9e-10 / 2,0e-10 (Kartengrenze 1e-9 erfuellt).
- Die Zeilen bei R ~ 44 haben 12 Nullstellen von m_bc (bei R ~ 39 bis 43: 10 bis 11), es ist also eine weitere Kurve
  oben dazugekommen. Nicht weiter untersucht.
- Knotenzahl (S, nur berichtet, nicht gewertet): k = 0 bis 7 an den neuen Sprossen 0, 0, 1, 3, 3/3, 4/4, 6/6, 7/7.

## 4 V0 bis V3

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| V0 | Pflichtpruefung L4 bestanden, alle bekannten Stellen angenommen (85 %) | **eingetroffen** | Erster Durchgang mit dem unveraenderten Entwurf: 12 von 12 angenommen, beide Stufen, alle im ersten Start |
| V1 | k = 0 bis 3: alle 4 Sprossen innerhalb +-0,06 (70 %) | **eingetroffen** | 4 von 4: Delta R = -0,0010 / -0,0007 / -0,0023 / -0,0045 |
| V2 | k = 4 bis 7: mindestens 7 von 8 Sprossen innerhalb +-0,12 (60 %) | **eingetroffen** | 8 von 8: Delta R von -0,020 (k = 4, 39,13) bis -0,095 (k = 7, 43,03) |
| V3 | Der Umlauf wechselt entlang jeder Kurve weiter das Vorzeichen (85 %) | **eingetroffen** | 12 von 12 gewerteten Schritten, beide Stufen gleich (Tabelle unten) |

- **V2-Nebenlesart (Kartennachtrag 1, Zusatzvorgabe der Leitung):** k = 5 / 40,51 ist "nicht blind" (Delta zur bekannten
  Stelle: R 9e-14, omega^2 2e-15, rho 2e-15). Ohne sie: 7 von 7 Treffern, "mindestens 6 von 7" eingetroffen. Das formale V2 bleibt 8 von 8.
- **V3-Folgen** (F-Umlauf, beide Stufen; bekannte Glieder aus L4, gewertet nur Schritte zu einer neuen Sprosse):

| k | Folge (R: Umlauf) | gewertete Schritte |
|---|---|---|
| 0 | 39,59: +1, 42,00: -1, **44,41: +1** | 1 von 1 |
| 1 | 40,51: +1, 42,61: -1, **44,72: +1** | 1 von 1 |
| 2 | 40,23: -1, 42,35: +1, **44,47: -1** | 1 von 1 |
| 3 | 39,77: +1, 41,91: -1, **44,05: +1** | 1 von 1 |
| 4 | Nr 80 36,92: +1, **39,11: -1**, **41,29: +1** | 2 von 2 |
| 5 | Nr 86 38,26: +1, **40,49: -1**, **42,71: +1** | 2 von 2 |
| 6 | Nr 82 37,19: -1, **39,49: +1**, **41,76: -1** | 2 von 2 |
| 7 | Nr 87 38,27: -1, **40,62: +1**, **42,94: -1** | 2 von 2 |

- **Bedeutung (Karte, woertlich):** V1 bis V3 eingetroffen (L4 bestanden) -> "Die Sprossenregel sagt neue stille
  Stellen vorab gewertet voraus [H, im Modell gestuetzt]." Ausloeser der Gegenaussage: keiner (keine Sprosse nicht
  gefunden, keine mit abs(Delta R) > 0,3; Maximum 0,095). Vermerk: eine der 12 Sprossen (k = 5 / 40,51) war nicht blind,
  die Nebenlesart besteht ohne sie.

## 5 Grenzen, Selbstanzeigen, Laufzeiten, sha256

### Grenzen

- **Systematische Abweichung:** Alle 12 Delta R sind negativ. Fuer die zweiten Sprossen von k = 4 bis 7 wachsen sie auf
  -0,037 / -0,055 / -0,071 / -0,095, weil der Abstand weiter schrumpft (Abschnitt 3). Die Toleranz 0,12 wurde auf k = 7
  zu 79 % ausgeschoepft. Eine dritte Sprosse auf k = 6 und 7 laege mit der linearen Regel vermutlich ausserhalb von 0,12
  [H, nicht gerechnet].
- **Kriterium auf jungen Kurven:** Zwei Sprossen weit aus den ersten drei Stellen nach der Geburt einer Kurve erreicht
  der Fortsetzungsfehler 0,124 bis 0,221 des Nachbarabstands (k = 7, 2, 3); das Kriterium haette dort echte Sprossen
  abgelehnt. Im Test lagen alle Kurven im reifen Bereich (gemessen hoechstens 0,018). Fuer Tests nahe einer
  Kurvengeburt taugt die Schwelle 0,1 mit dieser Fortsetzung nicht.
- **Lueckenlosigkeit nicht geprueft:** Ob zwischen den Gliedern einer Folge weitere Sprossen liegen, ist nicht
  gerechnet. V3 setzt direkte Nachbarschaft voraus. Die gefundenen Abstaende (>= 2,1) sprechen dagegen.
- **Nicht blind:** k = 5 / 40,51 war vorab bekannt (Kartennachtrag 1). Die uebrigen 11 Sprossen hat vor diesem Lauf
  niemand gerechnet. Die Kurvenlagen (Zeilennullstellen) bei R 39,6 bis 42,6 waren aus HUELLEN-LEITER-3 bekannt und
  dienten vor dem Einfrieren nur zur Pruefung des Kriteriums; sie enthalten keine Vorzeichen von s und damit keine
  Sprossenlagen.
- **Varianten:** Lagen aus S, Umlauf aus F (wie HUELLEN-LEITER-3). F gegen S <= 1,5e-13 an allen neuen Stellen. Die
  Knotenzahl ist weggelassen (Fremdstimme L4).
- **Eine Stimme:** keine Fremdpruefung dieses Laufs. Reichweite: l = 0, linear, klassisch, Modell M2, keine Messdaten.

### Selbstanzeigen

- **Planangabe "Gelesen" ungenau:** Der Kopf des eingefrorenen Plans nennt fuer HUELLEN-LEITER-3 "aus/test/*.json nur
  Laufzeiten und Lagen, diag/ nur Dateinamen". Vor dem Einfrieren habe ich zusaetzlich die F-Umlaeufe aus
  diag/umlauf-k3-st*.json (D2, 17:19) und die Zeilennullstellen rho_null aus aus/test/*.json gelesen (Zusatzpruefung,
  in Plan 4a beschrieben). Beides ist erlaubter Lesebereich und aendert nichts am Kriterium. Ausserdem gelesen:
  diag/-Struktur per jq, die Ordnerlisten von RUNDE-18/huellen-leiter/, aus/laeufe/, RUNDE-19/huellen-leiter-2/ (aus/,
  code/ nur Dateinamen) und huellen-leiter-3/.
- **Zusatzpruefung nach L4:** Die Pruefung der Fortsetzung an den HL3-Zeilen habe ich erst nach dem Befund 0,124
  geplant und gerechnet (lokal mit jq, hilfs/fort-zeilen.jq, gequoteter Heredoc). Sie lag vor dem Einfrieren und vor
  jedem Testlauf und hat am Kriterium nichts geaendert.
- **Fortsetzungsfehler vor dem Einfrieren unvollstaendig angesehen:** Mein Filter zeigte fuer k = 0 bis 3 nur die
  Stellen ab Nr 60 und die HL3-Sprossen. Die fruehen Werte k = 2 (Nr 22: 0,200) und k = 3 (Nr 30: 0,221) habe ich erst
  beim Gegenlesen des Berichts gesehen. Plan 4a nennt deshalb nur k = 7 (0,124) als Ueberschreitung. Fuer den Test
  aendert das nichts (k = 0 bis 3 nur ein Schritt im reifen Bereich, gemessen <= 1,3e-4), die Grenze des Kriteriums ist
  aber groesser als im Plan beschrieben.
- **Zaehlfehler im eingefrorenen Plan 4a:** Dort steht "|W| <= 1e-10 an 9 von 12 (k = 1 und 2 / 42,351)". Richtig sind
  8 von 12; k = 5 / 38,26 hat auf Stufe 2 1,12e-10. Kein Kriterium (Kartengrenze 1e-9), Annahme unberuehrt.
- **Lokale Werkzeuge ausserhalb der Liste:** sleep in until-Warteschleifen (Hintergrund und Monitor), [ -s ] und
  grep -q als Bedingungen, bash fuer meine Hilfsskripte (hilfs/l4.sh, test.sh, laufzeiten.sh). Ein Befehl mit
  vorangestelltem sleep 45 wurde vom Werkzeug abgelehnt und lief nicht. Eine Warteschleife enthielt versehentlich ein
  lokales ls auf einen nur auf der .69 vorhandenen Pfad (wirkungslos). Kein lokales python, awk oder bc.
- **Auf der .69:** mkdir meines Ordners, py_compile mit rm -rf code/__pycache__ in meinem Ordner, sha256sum und ls
  in meinem Ordner. Keine Prozesse beendet, keine fremden Ordner gelistet, nichts ausserhalb meines Ordners angelegt.
  kleintest.sh nicht gelesen (Aufrufform aus dem Auftrag).
- Nichts in den Scratchpad geschrieben (die Ausgaben der Hintergrund-Befehle legt das Werkzeug selbst unter
  /tmp/claude-1000/.../tasks ab). Kein git, kein Peerbus, keine Unteragenten, keine Literatur. Nichts aus Sperrbereichen.

### Laufzeiten (.69, kleintest.sh, Service runtime; UTC)

| Lauf | Spur | Start | Ende | Dauer | rc | Teil |
|---|---|---|---|---|---|---|
| prof-st1 / prof-st2 | cpu / cpu2 | 15:17:28 | 15:17:33 / 15:17:36 | 4,5 s / 8,0 s | 0 | Profile |
| l4d1-st1-a / st2-c | cpu | 15:18:24 / 15:21:39 | 15:21:39 / 15:23:55 | 195 s / 135 s | 0 | L4 |
| l4d1-st1-b / st2-d | cpu2 | 15:18:24 / 15:22:12 | 15:22:12 / 15:24:45 | 228 s / 153 s | 0 | L4 |
| l4d1-st2-a | cpu3 | 15:18:24 | 15:22:48 | 264 s | 0 | L4 |
| l4d1-st2-b | cpu4 | 15:18:24 | 15:23:10 | 286 s | 0 | L4 |
| ausw-l4d1 / fortfehler | cpu / cpu2 | 15:24:54 | 15:24:55 | 0,6 s / 0,5 s | 0 | L4 formal, Bericht |
| test-st2-a / st1-a | cpu | 15:27:18 / 15:32:11 | 15:32:11 / 15:35:25 | 293 s / 194 s | 0 | Test |
| test-st2-b / st1-b | cpu2 | 15:27:18 / 15:30:43 | 15:30:43 / 15:33:04 | 205 s / 141 s | 0 | Test |
| test-st2-c / st1-c | cpu3 | 15:27:18 / 15:30:55 | 15:30:55 / 15:33:42 | 217 s / 166 s | 0 | Test |
| test-st2-d | cpu4 | 15:27:18 | 15:31:21 | 243 s | 0 | Test |
| ausw-test | cpu | 15:35:35 | 15:35:36 | 0,5 s | 0 | Test formal |

- Zusammen ~46 min Spurzeit (2735 s: L4 1261 s, Test 1459 s, Profile 12 s, Auswertungen 2 s), 18 min Wandzeit
  (15:17:28 bis 15:35:36) auf vier Spuren. Kein Lauf an der 600-s-Grenze (laengster 293 s).

### sha256

Code (lokal = .69, verglichen):

```
b06fbb8a3a4fb8e0a6ac717bc5c8b72a470e7ba03194d889d793989c37791b1e  code/sprossen_vorab.py
f67e137580aab1fe48a56b965c7d432d186039e2c9bd8b301e7ff870af572738  code/huellen_leiter3.py
2755359c497aca04eeeca48f851e83a62a6671aa121713cc709ca5c77076c57e  code/huellen_leiter2.py
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py
f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py
```

Plan:

```
482814025ba4d7f4ce6d41b6f80227bfdc4ec996425f3d1ce963c281f03e23af  PLAN.md.eingefroren-20261002-172711
```

Ausgaben (lokal = Spiegel von /home/fmh/fmhc-physics-remote/runde20-sprossen-vorab/aus/ ohne *.npz):

```
27d56c57e04b526f23e493c885127d68e8d7e5ddf599cbee3fc32372148c0858  aus/l4-d1/l4-auswertung.json (formal, = .69)
bd870c21ddf2221268fe2d4141cd20c50e35a047c551335a968c190bf5593eb9  aus/test/test-auswertung.json (formal, = .69)
75f6a037cceca1432bc6ae4f788a0f9488fd7c8a4f95887f369b85fdae258068  aus/fortfehler.json
0d51089ea6d8261b486ff809cb0c2082cfc1011be7323e2ee4e3fc621570dedc  aus/l4-d1/l4/l4-st1-a.json
607e0d60122c55747832e6b927239cf1b19fb88266224b018187d1b3fde77275  aus/l4-d1/l4/l4-st1-b.json
b663efabc66b37bcf22f43f4b4993ecaf9f7e4245d8e3331510877c7b59d83c8  aus/l4-d1/l4/l4-st2-a.json
77770eca9e4e5305d30a88626dbb1b7d5068e4ac82601da1010f1ab31e3db8f7  aus/l4-d1/l4/l4-st2-b.json
981389878a23374987ac3f0211bcd46f0436394d31c7f9f529470103de29f75c  aus/l4-d1/l4/l4-st2-c.json
8a2896cc73dc9dad8f3ddc889201d768d965ec2ae35725b2bda960a45e0806c8  aus/l4-d1/l4/l4-st2-d.json
d282fe1dcb9e667b82eb21867e5115a12bf2ce16fb698484c6e03637a48fc4f2  aus/test/test/test-st1-a.json
e2ca6487fce7e24ffc3ac2ed6f5b2ee42724267ea82f270ada599bc901bc7c16  aus/test/test/test-st1-b.json
74733c5e17f73561ddb87d3800d38f2a1dc0cb43c74c524a6dc854d6b218b808  aus/test/test/test-st1-c.json
37aa01bc0f7338a911078d93aa1fa12466d47de0db123e78ec19a4434f0033b7  aus/test/test/test-st2-a.json
3706bc95ba96583e36904a73a515ec55ecee254e3ddbcd85cbce97f7c661d279  aus/test/test/test-st2-b.json
7d793f3870be6a18594e14914e51aadd69c6dbf95dcf60b097e7316e53cbaf42  aus/test/test/test-st2-c.json
1a76d09eac60f326f19f65d3b9ebedb6e506d2c2b80ab12f3527041f2916bf0b  aus/test/test/test-st2-d.json
1c408236e1223da48276225a0c3fabc82913bcc5f09c54bf5bafb5859c400fab  aus/prof-st1/profile-info.json
82da3c2b2dac0fb2d21d3641a3c137989b684fd77db8257c179ce27daa00cde8  aus/prof-st2/profile-info.json
```

- Profile: w2, Q, E, Rchi, chi0, N in allen 126 Zeilen beider Stufen bitgleich mit HUELLEN-LEITER-3 (sha256 der
  jq-Auszuege gleich). Profile (*.npz) nur auf der .69. Logs lokal unter logs/.

Hilfsdateien:

```
fbaa7906ffc7ad3843f036a788087bc026165778fce714e24bd07eb3c304385b  hilfs/bekannte.json
8effaedf8b3fe6bf7d47254767133af0cd46bf4c04fec2b1f52e27a414518a86  hilfs/zeilen-126.json
457e36882fce45a21526fba727d5a1cd3a3a6ce36b17b5e48bca57701fafb364  hilfs/fort-zeilen.jq
3de57dde5e368f3e0d0c1074fc86f46fcfb53218735c9528546a2307728fbbd8  hilfs/fort-zeilen-ausgabe.tsv
2cd60498ed072427f38520b57dde4f0ae79d65c0867f38dce5aa1dde01af7ab2  hilfs/l4.sh
2b34006389bda899d22da4f16d65f25c136a328d4d6f34f3c133877d95f9da00  hilfs/test.sh
0cbf66bbd1c3f542d33d685d8c90768ce7945b22e3a310b2944dcf15e0508a23  hilfs/tab.jq
df57f25775b360ca552d705f0059c7873e7fc11b6ca5d1d24c9ec6427c07e0a1  hilfs/laufzeiten.sh
```

## 6 Einfach gesagt

Ein grosser Q-Ball hat stille Stellen, an denen er schwingen kann, ohne Wellen abzustrahlen. Auf jeder Schwingungsart
folgen sie wie Sprossen einer Leiter in fast festem Abstand. Mit dieser Regel haben wir zwoelf neue Stellen
vorhergesagt und die Pruefregeln vorher festgelegt und an schon bekannten Stellen getestet. Danach haben wir genau an den
vorhergesagten Orten gesucht. Alle zwoelf sind da, jede hoechstens 0,1 Laengeneinheiten neben der Vorhersage, auf zwei
Rechengittern gleich, und der Drehsinn wechselt weiter von Sprosse zu Sprosse. Eine der zwoelf war schon vorher
zufaellig gefunden worden; auch ohne sie besteht der Test. Die kleine Abweichung zeigt immer in dieselbe Richtung, weil
die Sprossen nach aussen langsam enger werden.
