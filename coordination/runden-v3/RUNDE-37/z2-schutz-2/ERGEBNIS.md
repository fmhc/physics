# Z2-SCHUTZ-2: Ergebnis (Runde 49; Barriere 360 -> 0 Grad: Kerngroesse oder Netzgroesse?)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 14:12:49 CEST. Plantext ab 14:23:51 CEST. Zeitbox bis 16:12:49 CEST.
  - Rauchtests 1 bis 7 von 12:29:17 bis 12:58:43 UTC (14:29:17 bis 14:58:43 CEST), 34 Units, je <= 120 s, nur (6, 12),
    (9, 18), (11, 22) und die Laufzeitprobe (10, 32) im Modus pruef; eine Unit mit rc = 1 (CI-NEB (6, 12) ohne Klammer).
  - Eingefroren 14:59:03 CEST (EINGEFROREN-SHA256.txt, Stempel 20261005-145903), auf der .69 mit sha256sum -c geprueft.
  - Hauptlaeufe 12:59:12 bis 13:26:05 UTC (14:59:12 bis 15:26:05 CEST): 22 Units (7 Groessen je start, bisekt, weg;
    Auswertung) auf cpu und cpu7, alle rc = 0, keiner wiederholt, kein Nachtrag. Laengste Units: bisekt (10, 32) 441 s,
    CI-NEB (10, 28) und (14, 24) je 480 s Wandzeit (nicht konvergiert).
  - Text ab 15:01:04 CEST, waehrend der Hauptlaeufe; letzte Aenderung 15:29:16 CEST (date).
- **Kennzeichen:** [M] Mathematik; [E] Rechnung im Modell (synthetisch, keine Messdaten); [L] Literatur oder
  Gedaechtnis; [H] Hypothese; [P] Projektdatei; [R] im Rauchtest gesehen.
- **Art:** synthetische Modellrechnung an einem Modellfeld (Einheitsquaternion-Feld, Energie 4(1 - c^2) je Bindung, auf
  Finns Diamant-Netz); keine Messdatenbestaetigung.
- **Code:** Kopien aus Z2-SCHUTZ-1 unveraendert (finn.py, guertel2.py, guertel.py, stab.py, z2.py; Hashes wie dort), neu
  code/z2s2.py (korrigierte Bisektion in der ebenen Darstellung psi mit Nachschaerfen, Klasse "M", Stufe 3, Freigabe bis
  zur Ruhe, Hesse S im Startlauf) und code/auswertung_z2s2.py. Gruende im PLAN (Abschnitte 0 bis 3, "Rauchtests").

## Netz und Startzustaende S (360 Grad, FIRE bis Knotenkraft < 1e-7) [E]

| Groesse (r0, R) | Knoten | frei | Kern | E_S | Hesse S: lambda_1, lambda_2, lambda_3 | Ueberlapp Nullmoden | Sonde min c | K-Hesse |
|---|---|---|---|---|---|---|---|---|
| (10, 20) = G1 | 38893 | 29298 | 4235 | 4545,3133 | 1,1e-9; 1,1e-9; 0,0407 | 1,000 / 1,000 | 0,815 | bestanden |
| (10, 24) | 65441 | 53590 | 4235 | 3976,5361 | 6,3e-9; 6,3e-9; 0,0342 | 1,000 / 1,000 | 0,871 | bestanden |
| (10, 28) | 101965 | 87862 | 4235 | 3644,0758 | 1,5e-8; 1,5e-8; 0,0294 | 1,000 / 1,000 | 0,896 | bestanden |
| (10, 32) | 150713 | 133022 | 4235 | 3428,9017 | -3,0e-9; -3,0e-9; 0,0258 | 1,000 / 1,000 | 0,910 | bestanden |
| (8, 24) | 65441 | 55676 | 2149 | 2769,2927 | 3,6e-9; 3,6e-9; 0,0433 | 1,000 / 1,000 | 0,846 | bestanden |
| (12, 24) = G2 | 65441 | 50632 | 7193 | 5516,3793 | -3,1e-9; -3,1e-9; 0,0283 | 1,000 / 1,000 | 0,862 | bestanden |
| (14, 24) | 65441 | 46282 | 11543 | 7719,9003 | -7,0e-10; -7,0e-10; 0,0239 | 1,000 / 1,000 | 0,869 | bestanden |

- E_S(G1) = 4545,313250942401 und E_S(G2) = 5516,3793 stimmen mit Z2-SCHUTZ-1 ueberein [P]. Alle sieben S sind echte
  Minima bis auf genau die zwei Drehungen der Drillachse.

## Ergebnis zuerst

1. **ZT0 eingetroffen [E]:** Auf G1 = (10, 20) geben die korrigierte Bisektion 25,02841 und der CI-NEB 25,02856, je auf
   4e-6 bzw. 2e-6 relativ am Wert 25,02852 aus Z2-SCHUTZ-1. Die zwei Verfahren treffen denselben Sattel (5,8e-6).
2. **Die Barriere haengt an der Kugel, nicht nur am Kern [E]:** Bei festem Kern r0 = 10 waechst sie von 25,0 (R = 20)
   auf 45,6 (R = 24, +82 %) und 76,8 (R = 32, +207 %). **ZT1 nicht eingetroffen** (Plan und Wortlaut).
3. **ZT2 nicht auswertbar:** Bei fester Kugel R = 24 sind nur r0 = 8 (33,9) und r0 = 10 (45,6) gueltig; (12, 24) und
   (14, 24) enden in Zwischenminima. Beschreibend steigt und faellt die Austrittsbarriere mit r0 (8: 34, 10: 46, 12: 42,
   14: 34) statt wie die Kernoberflaeche zu wachsen.
4. **ZT3 nicht eingetroffen [E]:** Auf drei der vier gueltigen Groessen tragen die 10 staerksten Bindungen 58 bis 105 %
   der Barriere, auf (10, 32) nur 36 % (n50 = 15): Mit der Kugel wird der Sattel breiter.
5. **Neu [E]:** Auf vier von sieben Groessen liegen hinter dem ersten Sattel Zwischenminima (Ruhezustaende, weder S noch T;
   Deutung [H]: am Gitter festgehaltene Teilzustaende des wachsenden Rings).
   Auf (10, 32) fuehrt der Weg S -> Sattel 1 (etwa +53) -> Zwischenminimum M (+46,1) -> Sattel 2 (+77,9 Bisektion, +76,8
   CI-NEB) -> T; der zweite Sattel ist hoeher als der erste.

## Urteile ZT0 bis ZT3 (Wortlaut der Karte unveraendert; lauf-69/auswertung.json)

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Wortlaut | tragende Kennzahl |
|---|---|---|---|---|---|
| ZT0 | Kontrolle [P]: Auf G1 = (10, 20) gibt der Code die Barriere 25,03 mit beiden Verfahren (korrigierte Bisektion und CI-NEB) auf 1e-3 relativ wieder | 85 % | **eingetroffen** | **eingetroffen** | B_A = 25,028412, B_B = 25,028557; gegen 25,028516 (Z2-SCHUTZ-1): 4,1e-6 und 1,7e-6; gegen 25,03: 6,3e-5 und 5,8e-5 (Grenze 1e-3); beide gueltig |
| ZT1 | [H] Bei festem Kern (wie G1) aendert sich die Barriere um weniger als 10 %, wenn der Kugelradius von 20 auf mindestens 28 waechst | 60 % | **nicht eingetroffen** | **nicht eingetroffen** | B(10, 20) = 25,03; B(10, 24) = 45,59 (+82 %); (10, 28) ungueltig; B(10, 32) = 76,78 (+207 %, R* = 32) |
| ZT2 | [H] Bei fester Kugel waechst die Barriere mit dem Kernradius etwa wie die Kernoberflaeche (Exponent 1,5 bis 2,5 ueber mindestens drei Kernradien) | 45 % | **nicht auswertbar** | **nicht auswertbar** | gueltig nur r0 = 8 (33,89) und 10 (45,59) bei R = 24; mindestens drei verlangt |
| ZT3 | [H] Am Sattel liegen auf allen gueltigen Groessen mindestens 50 % der Barrierenenergie in hoechstens 10 Bindungen | 50 % | **nicht eingetroffen** | **nicht eingetroffen** | L10: (10, 20) 1,046 / 1,046; (10, 24) 0,583 / 0,597; (8, 24) 0,706 / 0,693; (10, 32) 0,362 (CI-NEB) |

- **Regeln:** PLAN Abschnitt 7, mechanisch in code/auswertung_z2s2.py (eingefroren). B(G) = kleinste gueltige Barriere je
  Groesse; gueltig nur mit bestandener Hesse-Kontrolle von S und einer Freigabe, die T erreicht.
- **Beschreibend [M, Kopfrechnung]:** Zwischen B(10, 24) und B(8, 24) laege der Exponent bei ln(45,59/33,89)/ln(10/8)
  = 1,33; zwei Punkte sind aber kein Urteil.

## Barriere je Groesse und Verfahren [E]

| Groesse | A: Bisektion (Stufen; kleinste Kraft unten / oben) | B_A | A gueltig | B: CI-NEB (Iterationen; Kraft Kletterbild) | B_B | B gueltig | K-Weg | B(G) |
|---|---|---|---|---|---|---|---|---|
| (10, 20) | 14 + 12 Halbierungen; 3,6e-5 / 9,7e-5 | 25,0284 | ja | 74; 3,3e-3 | 25,0286 | ja | 5,8e-6 bestanden | **25,028** (A) |
| (10, 24) | 14 + 12; 1,1e-5 / 3,4e-6 | 48,4118 | ja | 266; 4,5e-3 | 45,5861 | ja | 0,062 verfehlt | **45,586** (B) |
| (10, 28) | 14 + 12, Stufe 3 (14 + 12); Sattel 1: 0,0043 / Ruhe; Sattel 2: 0,0082 / 0,0060 | (60,76) | nein: Freigabe endet in Zwischenminimum | 846, Wandzeit; 0,093 | (60,42) | nein | - | ungueltig |
| (10, 32) | 14 + 12, Stufe 3 (12 + 2); Sattel 1: 0,157 / Ruhe; Sattel 2: Ruhe / 0,026 | (77,89) | nein: Sattel 1 ungenau (0,157 > 0,05) | 238; 4,7e-3 | 76,7811 | ja | - | **76,781** (B) |
| (8, 24) | 14 + 12; 0,0080 / 0,0216 | 34,8003 | ja | 225; 4,9e-3 | 33,8926 | ja | 0,027 bestanden | **33,893** (B) |
| (12, 24) | 14 + 12; 0,0063 / 0,0056 | (41,990) | nein: Freigabe endet in Zwischenminimum | 149; 4,0e-3 | (41,992) | nein (Freigabe) | - | ungueltig |
| (14, 24) | 14 + 12, Stufe 3 (14 + 12); Sattel 1: 0,0117 / Ruhe; Sattel 2: Ruhe / 0,036 | (33,85 bzw. 36,70) | nein: Weg nicht geschlossen (unten anderes Gleichgewicht) | 1292, Wandzeit; 1,74 | (35,62) | nein | - | ungueltig |

- Werte in Klammern sind beschreibend (ungueltige Groessen). "Ruhe" heisst: die Bahn dieser Seite endete in einem
  Zwischenminimum, ihr Zustand kleinster Kraft ist keine Sattelnaeherung; die Sattelenergie kommt dann von der Gegenseite.
- **Zwei Sattel auf (10, 24) und (8, 24):** Die Bisektion findet einen Sattel 6,2 % bzw. 2,7 % ueber dem des CI-NEB. Beide
  sind genau (kleinste Kraefte 1e-5 bzw. 2e-2; CI-NEB 5e-3); der CI-NEB ist vom Bisektionsweg zu einem tieferen
  Nachbarsattel gerutscht (staerkste Bindung bei 20 statt 27 Grad zu n_P auf (10, 24)). Die Barriere haengt damit auch am
  Keimort auf dem Gitter [E].
- **Energieprofile CI-NEB:** (10, 20) 4545,31 / 4547,68 / 4557,75 / 4567,79 / **4570,34** / 4567,45 / 4556,87 / 4543,73;
  (10, 24) 3976,54 / 3979,44 / 3997,17 / 4016,20 / **4022,12** / 4020,46 / 4000,37 / 3975,53;
  (8, 24) 2769,29 / 2771,92 / 2792,30 / **2803,19** / 2797,97 / 2786,41 / 2769,06 / 2768,15;
  (10, 32) 3428,90 / 3432,99 / 3481,08 / 3496,12 / **3505,68** / 3494,60 / 3458,17 / 3427,57 (Weg ueber M).
- **Freigabe (Weg weiter nach T):** (10, 20) 1696 Schritte, (10, 24) 2183, (8, 24) 1565, (10, 32) 3434, (14, 24) 3592; je
  bis E < 1e-3 und unter E_S. (10, 28) und (12, 24) enden in Ruhe (siehe unten).

## Zwischenminima [E]

| Groesse | wo gefunden | Energie relativ zu E_S | Bemerkung |
|---|---|---|---|
| (10, 28) | Klasse "M" in der Bisektion; Freigabe | +40,916 (M); -115,92 (Freigabe-Ende, 136 Bindungen c <= 0) | M liegt nur 0,003 unter Sattel 1 (+40,919); Sattel 2 (+60,76, unten S) fuehrt in ein tiefes Zwischenminimum, nicht nach T |
| (10, 32) | Klasse "M" | +46,068 | Weg S -> Sattel 1 (~+53, ungenau) -> M -> Sattel 2 (+77,89) -> T geschlossen (unten dasselbe M, D = 8e-17) |
| (12, 24) | Freigabe | -180,07 (134 Bindungen c <= 0) | wie G3 in Z2-SCHUTZ-1 (dort -219,6 auf (14, 28)) |
| (14, 24) | Klasse "M" | drei verschiedene: +33,26; +33,35; +33,39 | Sattel 1 bei +33,85, Sattel 2 bei +36,70; untere Bahn in Stufe 3 endet in einem anderen M als oben |

- Energien relativ zu E_S sind Differenzen aus den JSON-Werten (Kopfrechnung). Die M sind Ruhezustaende von FIRE
  (Knotenkraft <= 1e-9), Hesse nicht gerechnet.

## Sattelform und Lokalisierung (ZT3) [E]

| Groesse, Sattel | L10 | n50 | groesstes Delta_b | Ort der staerksten Bindung (r; Winkel zu n_P) | Bindungen c <= 0 | Anteil Kernbindungen an B |
|---|---|---|---|---|---|---|
| (10, 20) A / B | 1,046 / 1,046 | 5 / 5 | 2,99 / 2,99 | 9,81; 27,4 Grad (beide) | 12 / 12 | 2,45 / 2,45 |
| (10, 24) A / B | 0,583 / 0,597 | 9 / 9 | 3,22 / 3,13 | 10,26; 27,3 Grad / 9,91; 20,2 Grad | 23 / 22 | 1,41 / 1,09 |
| (8, 24) A / B | 0,706 / 0,693 | 7 / 7 | 3,07 / 3,24 | 8,67; 37,6 Grad / 7,89; 35,2 Grad | 15 / 14 | 1,24 / 1,09 |
| (10, 32) B | 0,362 | 15 | 3,37 | 9,81; 27,4 Grad | 44 | 0,79 |
| (10, 32) A, Sattel 2 (ungueltig) | 0,393 | 14 | 3,60 | 9,71; 35,7 Grad | 63 | 0,84 |
| (10, 28) A, Sattel 2 (ungueltig) | 0,479 | 11 | 3,56 | 10,59; 24,4 Grad | 35 | 0,91 |
| (12, 24) A (ungueltig) | 0,633 | 8 | 3,23 | 12,09; 35,9 Grad | 24 | 1,07 |
| (14, 24) A, Sattel 1 (ungueltig) | 0,680 | 7 | 3,50 | 14,74; 19,6 Grad | 17 | 0,48 |

- **Lesart [E, H]:** Der erste Sattel ist auf allen Groessen ein Fleck gesprungener Bindungen an der Kernoberflaeche
  (12 bis 24 Bindungen mit c <= 0; Anteil der Kernbindungen an B 0,48 bis 2,45); sein Rand ist ein Z_2-Wirbelring [H,
  Deutung]. Der hoehere zweite Sattel auf (10, 32)
  ist breiter (44 bis 63 gesprungene Bindungen, n50 = 14 bis 15): ein gewachsener Ring, der eine Gitterstufe ueberwinden
  muss [H].

## Kontrollen [E]

- **K-Hesse S:** auf allen sieben Groessen bestanden (Tabelle oben): zwei Nullmoden auf |lambda| <= 1,5e-8, Ueberlapp mit
  den analytischen Drehungen der Drillachse 1,000, lambda_3 zwischen 0,024 und 0,043. T ist globales Minimum (E = 0) [M].
- **Ebene Darstellung:** Die Kletterbilder des CI-NEB (mit Rauschen aus der Ebene gestartet) liegen am Ende in der Ebene
  (groesste Komponente ausserhalb 2,5e-5 auf (10, 20), sonst <= 5e-6). Die psi-Rechnung der Bisektion verliert also
  keinen tieferen Sattel ausserhalb der Ebene. Die Barrieren von A und B stimmen auf (10, 20) und (12, 24) auf 6e-6 bzw.
  4e-5 ueberein.
- **K-Weg (beschreibend, 5 %):** bestanden auf (10, 20) und (8, 24), verfehlt auf (10, 24) (6,2 %, zwei verschiedene
  Sattel, beide genau); auf den uebrigen Groessen nicht auswertbar.

## Bedeutung [H] fuer Spin 1/2 auf Finns Netz

- **Gemessen [E]:** Die Barriere des Spin-Vorzeichens (360 -> 0 Grad) haengt stark an der Kugel: bei festem Kern r0 = 10
  von 25 (R = 20) ueber 46 (R = 24) auf 77 (R = 32). Nach der Karte (vorab): "ZT1 verfehlt (Barriere waechst mit der
  Kugel): Der Schutz ist kollektiv; das waere ein Hinweis auf einen echten topologischen Sektor."
- **Lesart [H]:** Die Barriere bleibt endlich (SO(3)^N zusammenhaengend [M]); "kollektiv" heisst hier: Die Kugel bestimmt,
  wie stark die Verdrillung am Kernrand ist (g = 2 pi R/(r0 (R - r0)) faellt mit R), und je schwaecher die Verdrillung je
  Bindung, desto groesser der kritische Keim und desto hoeher die Barriere. Bei R -> unendlich und festem r0 bleibt g
  endlich (2 pi/r0); ich erwarte dort eine Saettigung, nicht ein Unendlich [H, nicht gerechnet]. Ein echter topologischer
  Sektor entstuende erst, wenn die Verdrillung je Bindung gegen null geht (Kontinuumsgrenze), wie in Z2-SCHUTZ-1 vermutet.
- **Nicht wie die Kernoberflaeche [E, beschreibend]:** Bei R = 24 steigt die Austrittsbarriere von r0 = 8 auf 10 und faellt
  zu 12 und 14 wieder; formal ist ZT2 nicht auswertbar.
- **Neu [E, H]:** Hinter dem Keimsattel liegen oft Zwischenminima; der wachsende Ring bleibt am Gitter haengen und muss
  weitere Sattel nehmen, die auf (10, 32) hoeher sind als der Keimsattel. Fuer das Spin-Vorzeichen zaehlt dann der hoechste
  Sattel des Weges, und der waechst mit dem Netz. Das Bild "eine Schwelle an der Kernoberflaeche" (Bedeutung bei ZT1 trifft
  ein) passt nur fuer die kleinen Netze.
- **Fuer exakten halben Spin [H]:** Auf einem endlichen Netz bleibt der Schutz energetisch; eine Zulaessigkeitsregel, die
  Gittersprung verbietet (Luescher-Typ [L]), bleibt die Kandidatin fuer exakten Schutz. Die Messung hier sagt nur, dass der
  energetische Schutz mit der Netzgroesse bei festem Kern deutlich waechst.
- **Grenzen:** ein Keimort (n_P) und eine Kappenfamilie; quasistatisch; der CI-NEB fand zweimal einen tieferen Nachbarsattel
  (Keimort-Abhaengigkeit einige Prozent); nur drei bzw. vier gueltige Groessen; (10, 28) ungueltig.

## Abweichungen vom ersten Plantext (alle vor dem Einfrieren, im PLAN unter "Rauchtests" begruendet)

- Erster Plantext 14:23:51 CEST: Bisektion mit neuer S-Regel, psi-FIRE, Freigabe bis zur Ruhe. Bis zum Einfrieren
  (14:59:03) kamen nach den Rauchtests dazu: Sattelbereich D >= 0,5 (Rauchtest 1), Stufe 2 Nachschaerfen (Rauchtest 2),
  Klasse "M" (Rauchtest 3), Ruhegrenze 1e-6 im Sattelbereich und Stufe 3 (Rauchtest 4 und 5; Familie nach Rauchtest 5
  geaendert), Genauigkeitsgrenze 0,05, Zeitanteile, Laufplan ((14, 24) auf cpu7), vorlaeufige Start-JSON. Die Regel "erster
  Durchgang" habe ich in Rauchtest 6 probiert und verworfen (Parameter anstieg = inf im Code).
- Rauchgroesse (11, 22) kam nach Rauchtest 2 dazu (Plan: nur (6, 12), (9, 18) und die Laufzeitprobe).

## Selbstanzeigen

1. **Plan nach Rauchtests stark umgebaut**, alle Aenderungen vor dem Einfrieren und im PLAN begruendet; der erste Wortlaut
   ist durch die Bearbeitung ueberschrieben (keine Kopie ausser der Beschreibung oben).
2. **Sieben Rauchtestrunden, 34 Units**, auf (6, 12), (9, 18), (11, 22) und als Laufzeitprobe (10, 32). (11, 22) liegt
   zwischen G1 und G2, also nahe am Raster; dort habe ich Klassen, Kraefte, Abstaende D und Schrittzahlen angesehen, keine
   Energien oder Barrieren.
3. **L10 und n50 von (9, 18) gesehen:** In Rauchtest 1 gab mein jq-Befehl auch L10 und n50 der Rauchgroesse (9, 18) aus,
   gegen meine eigene Plan-Aussage ("keine Energie- oder Barrierenwerte", Lokalisierung nicht ausgenommen). (9, 18) ist
   nicht im Raster.
4. **Haengender ssh-Start (Rauchtest 3):** "&&" vor dem Hintergrundzeichen hielt den ssh-Kanal bis zum Kettenende offen;
   ohne Wirkung auf die Laeufe. Dieselbe Panne steht schon in Z2-SCHUTZ-1 (Selbstanzeige 6); ab Rauchtest 4 und fuer die
   Hauptketten habe ich ohne "&&" gestartet.
5. **Genauigkeitsregel macht (10, 32) fuer A ungueltig, obwohl B_A dort vom genauen Sattel 2 bestimmt ist:** Nach Plan muessen
   beide Sattel genau sein; Sattel 1 hatte 0,157. Nicht nachtraeglich geaendert; (10, 32) zaehlt ueber B (CI-NEB).
6. **Kopfrechnung lokal:** g-Werte und D >= 0,66 im PLAN, Laufzeitschaetzungen, im Bericht die Energien relativ zu E_S der
   Zwischenminima, Prozentangaben, der beschreibende Exponent 1,33. Kein lokaler Interpreter.
7. **Werkzeuge:** lokal date, ls, mkdir, cp, mv, cat, sed, grep, head, tail, wc, du, sha256sum, scp, rsync, ssh, printf,
   test, sleep (nur in Warteschleifen). Auf der .69 ausserhalb von kleintest.sh: mkdir, mv, cp, cat, ls, test, sha256sum,
   jq (nur Feldauswahl, keine Rechnung, keine Rundung), date, uptime, nproc, systemctl --user list-units (lesend), setsid nohup
   bash fuer die Ketten. Kein python ausserhalb von kleintest.sh, kein awk, kein perl, kein pgrep, kein rm.
8. **Hintergrundausgaben:** Das Werkzeug legt die Ausgaben meiner Warteschleifen in seinem Sitzungsordner
   (/tmp/claude-1000/.../tasks/) ab; selbst habe ich dort nichts geschrieben.
9. **Entwurfsdateien** (Textblock und Vorfassung von z2s2.py) nach code/entwurf/ verschoben, nicht geloescht; die
   Rauchtest-Ketten liegen in ketten/.
10. **Literatur aus dem Gedaechtnis [L]:** Skufca, Yorke, Eckhardt 2006; Schneider, Eckhardt, Yorke 2007; Henkelman,
    Uberuaga, Jonsson 2000; Luescher (Zulaessigkeit): nicht an der Quelle geprueft.
11. Kein Journaleintrag, kein Peerbus, kein Commit; das liegt bei der Leitung.

## Negativliste (darf aus diesem Befund NICHT gesagt werden)

- "Finns Netz hat einen topologisch geschuetzten Spin-1/2-Sektor." Alle Barrieren sind endlich.
- "Die Barriere waechst wie R^p" oder "wie die Kernoberflaeche": Bei festem Kern drei gueltige Punkte, bei fester Kugel zwei;
  kein Gesetz, ZT2 nicht auswertbar.
- "Die kleinste Barriere auf (10, 24) ist 45,6": ein Keimort, eine Familie; der CI-NEB fand zweimal einen tieferen
  Nachbarsattel, weitere koennten tiefer liegen.
- "Auf (10, 28), (12, 24) oder (14, 24) liegt die Barriere bei ...": ungueltig (Zwischenminima, Weg nicht geschlossen).
- "Die Barriere ist rein oertlich an der Kernoberflaeche": Sie haengt bei festem Kern stark an der Kugel (ZT1 nicht
  eingetroffen), und auf (10, 32) ist der hoechste Sattel ein breiter, gewachsener Ring (L10 = 0,36).
- "Spin 1/2 ist im Modell nachgewiesen" oder irgendeine Aussage ueber Messdaten. Synthetisch, keine Messung.

## Dateien

- **Plan:** PLAN.md, PLAN.md.eingefroren-20261005-145903, EINGEFROREN-SHA256.txt.
- **Code:** code/z2s2.py, code/auswertung_z2s2.py (neu, je mit .eingefroren-20261005-145903); code/finn.py, guertel2.py,
  guertel.py, stab.py, z2.py (unveraenderte Kopien aus Z2-SCHUTZ-1); code/entwurf/ (Entwuerfe).
- **Ketten:** ketten/lauf-cpu.sh, lauf-cpu7.sh (eingefroren); ketten/rauch1 bis rauch7 (Rauchtests); ketten/tabelle-lesen.sh
  (jq-Auswahl zum Lesen, nach den Hauptlaeufen).
- **Hauptlaeufe:** lauf-69/ (start-, bisekt-, weg-haupt-*.json, auswertung.json, Logs, kette-*.out,
  PRUEFSUMMEN-69-roh.txt fuer die npz, die nur auf der .69 liegen).
- **Rauchtests:** rauch-69/rauch1 bis rauch7 (JSON und Logs, ohne npz).
- **Auf der .69:** /home/fmh/fmhc-physics-remote/z2-schutz-2/ (code/, ketten/, rauch1 bis rauch7/, lauf/).

## Einfach gesagt

Wir haben in Finns Netz die Mitte um eine volle Umdrehung verdreht festgehalten und gemessen, wie viel Energie das Feld
mindestens braucht, um diese Verdrehung loszuwerden, einmal mit fester Mitte und wachsender Kugel und einmal mit fester
Kugel und wachsender Mitte. Die Kontrolle hat geklappt: Der verbesserte Rechner trifft den alten Wert 25,03 auf fuenf Stellen,
mit zwei verschiedenen Verfahren. Bei fester Mitte wird die Schwelle mit der Kugel viel hoeher (25, dann 46, dann 77), weil
die Verdrehung sich auf mehr Platz verteilt und jede Verbindung weniger verdreht ist; die Vorhersage "fast gleich" stimmt
also nicht. Unterwegs bleibt das Feld oft in Zwischenzustaenden haengen, und bei der groessten Kugel ist die zweite Huerde
sogar hoeher als die erste und auf viele Verbindungen verteilt. Es ist eine Modellrechnung und kein Nachweis in der Natur.
