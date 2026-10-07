# SPIEGEL-HAELFTE-1: Ergebnis (Runde 42)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 17:35:36 CEST; Plantext ab 17:57:24; Text dieser Datei ab 18:18:57 CEST.
  - Rauchlaeufe 16:00:07 bis 16:06:48 UTC (PLAN.md Abschnitt 7). Plan und Code eingefroren 18:07:54 CEST
    (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe auf der .69 ueber kleintest.sh, Spur cpu11, je ein ssh-Aufruf, alle rc = 0 (UTC = CEST − 2 h).
    Die "start"-Zeilen der Logs sind Aufrufzeiten; H2 und H3 warteten am Lock der Spur.

    | Lauf | Inhalt | Aufruf (UTC) | Ende (UTC) | Laufzeit |
    |---|---|---|---|---|
    | H0 | Teil A (Zahlenpruefung, Kegel) | 16:08:02 | 16:08:03 | 0,2 s |
    | H1 | W = 0 (Bloch, C²-Regel), π/8, π/4 (je 3 Saaten), Saatbasis 42000 | 16:08:08 | 16:11:18 | 189 s |
    | H2 | W = π/2, π, 3π/2 (je 3 Saaten), Saatbasis 43000 | 16:08:10 | 16:14:21 | 182 s |
    | H3 | W = 2π (6 Saaten), Saatbasis 44000 | 16:08:12 | 16:16:28 | 127 s |
    | Auswertung | auswertung.py | 16:16:34 | 16:16:34 | < 1 s |

- **Kennzeichen:** [M] eigene Mathematik (nicht gegengelesen); [E] Messung im Modell; [P] Projektdatei; [S] Quelle
  (Foster/Jacobson = FJ, arXiv:1610.01142, Zeilen der lokalen Kopie dunkel-flip-l/quellen/F11-...txt); [H] Hypothese;
  [R] im Rauchlauf gesehen.
- **Art:** Synthetische Rechnung an einem selbst gebauten Modell. Keine Messdaten, keine Aussage ueber die Natur.

## Ergebnis zuerst

1. **Teil A haelt in der Sache, mit zwei Berichtigungen [M, Zahlen bestaetigt].**
   - Die Kompression der unitaeren Einbahn-Regel W = C S_+ auf eine Haelfte ist ein FJ-Schachbrett. Dort wirkt die
     andere Haelfte als vollkommene Senke.
   - Berichtigung 1: In der Projekt-Loesung T:2+2' traegt die Haelfte 2 Spinoren **antiparallel** zur Sprungrichtung.
     Die Kompression auf 2 ist also FJ mit P-quer, also die andere Haendigkeit (auf 1,7e−15). FJ mit P sitzt in 2'.
     Bei T:2+2'' ist es umgekehrt. Die Betraege der Matrixelemente, auf die sich das Dossier stuetzt, legen das nicht
     fest; das tut erst die Bargmann-Invariante.
   - Berichtigung 2: Die Verdoppler an H, P, P' sind die vier entkoppelten FCC-Familien des BCC-Gitters. FJ hat sie
     ebenso und identifiziert sie mit k = 0. Der echte Unterschied zu FJ ist der Partner in 2' und die Unitaritaet.
2. **Neu und exakt [M, im Lauf bestaetigt]: Bei W = 2π ist der Unordnungsmittelwert der Amplitude genau FJ.**
   - Gemessen: Ueberlapp mit dem FJ-Zustand 0,4947 ± 0,0005 gegen N_FJ = 0,4956 bei t = 100 (Abstand 2 Standardfehler).
     Bei t = 10 und 25 liegt er auf 2e−4 an N_FJ.
3. **SH1 nicht eingetroffen [E]: Die verborgene Haelfte ist keine Senke, sie verwuerfelt.**
   - Bei W = 2π liegt das 2-Gewicht bei t = 100 bei 0,717. Die FJ-Kurve liegt bei 0,496. Die groesste relative
     Abweichung ist 0,448 im Saatmittel und 0,444 bis 0,450 in jeder Saat.
   - Etwa 44 % des abgeflossenen Gewichts kommen nach 2 zurueck (Rueckgabequote 0,41 bei t = 10, 0,44 ab t = 50). Die
     Schreibtisch-Erwartung vor dem Lauf war ~1/2 (PLAN A9).
4. **SH2 eingetroffen, knapp [E].** v_eff = 0,3048 bei W = 2π, die Bandgrenze liegt bei 0,300. Die Ausbreitung faellt
   mit W stetig: 0,3237 bei W = 0, 0,3195 bei π, 0,3128 bei 3π/2.
5. **Doppler-Anteile verschwinden nicht, sie wachsen [E].**
   - Bei W = 2π liegen bei t = 100 31 % des 2-Gewichts bei grossen Wellenvektoren (|k| > 0,5 Hop^−1). Bei W = 0 sind
     es 0,11 %. Bei FJ faellt der Anteil von 0,11 % auf 0,013 %.
   - Das zurueckgekehrte Gewicht ist ueber die ganze Brillouin-Zone verteilt ("weiss").

## Teil-A-Urteil

| Schritt (DOSSIER 6.2, ARBEITSFELD 9) | Urteil | Zahl (H0 = R1) |
|---|---|---|
| A1 V V^† = 1 | haelt | 1,8e−15 (Projekt-Loesung), 2,2e−16 (saubere Fassung) |
| A2 V^†V Rang-2-Projektor, 1/2 und 1/12 | haelt | Diagonale auf 6e−16, Nebenbetrag² 1/12 auf 4e−16 |
| A3 "Betraege gleich, also V^†V = P_2" | **Luecke, berichtigt**: P_2' = 1 − P_2 hat dieselben Betraege; erst die Bargmann-Invariante entscheidet | T:2+2': passt zu Spinoren laengs −h_a auf 1,2e−16, zu +h_a nicht (4,8e−2); Spin der Haelfte 2 mal h_a = −1 bei allen a |
| A4 V S_+ V^† = (1/2) Σ e^{ik·h_a} P_a, unabhaengig von der Phasenwahl | haelt, mit P-quer statt P fuer die Haelfte 2 von T:2+2' | Kompression gegen FJ mit P-quer 1,7e−15, mit P 1,56; T:2+2'': mit P 7,8e−16; zweite Phasenwahl 1,1e−16 |
| A5 P_2 W P_2 = e^{iα} V^† A V, 2' als Senke | haelt | iteriert bis t = 10: 2,4e−14; C²-Regel FJ Gl. (11) gegen Kompression im Gitter: 2,6e−17 |
| A6 vier FCC-Familien = BCC, Schritte T+ | haelt | Kopfrechnung; Zyklusoperator = W(k)^4 exakt (Versatz-Summe null) |
| A7 (neu) H/P/P'-Verdoppler = die vier Familien | Berichtigung der Lesart "FJ doppler-frei gegen Einbahn-Regel mit Verdopplern" | e^{ik·t_a} an H, P, P' fuer alle a gleich (−1, −i, +i) |
| A8 (neu) Mittelwert bei W = 2π = FJ | exakt [M] | Ueberlapp: 0,90743 gegen 0,90748 (t = 10); 0,4947 ± 0,0005 gegen 0,4956 (t = 100) |

- T-Kovarianz: Projekt-Loesung ≤ 2,1e−15; saubere Fassung ≤ 5,3e−16. Saubere Fassung gegen Projekt-Loesung nach
  diagonaler Eichung: 1,0e−15.
- Die gespeicherte Projekt-Loesung ist genau (C unitaer auf 7,6e−13, Restgewicht in S_− 3,1e−12).
- **Folge fuer Teil B:** gerechnet, nicht nur beschrieben. Die sichtbare Haelfte ist im Rechenmodell die P-quer-Haelfte
  von T:2+2'. Fuer das entsprechend konjugierte Startpaket sind die Gewichte bei beiden Haendigkeiten gleich: Komplexe
  Konjugation mit diagonaler Eichung tauscht die Haelften, und die Phasenverteilung um β = π ist symmetrisch [M].

## Urteile (lauf-69/auswertung.json, Vorbedingungen erfuellt)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil Plan | Urteil Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| SH0 | Kontrollen: Teil-A-Herleitung haelt; W = 0 reproduziert die Bloch-Vorhersage (Kegel auf 2, Partner auf 2', kohaerente Rueckkehr) auf 1e−8 | 75 % | eingetroffen | eingetroffen (Herleitung mit Berichtigungen A3, A7) | w_2 gegen Bloch 1,0e−13; Endzustand 2,7e−14; Eigenphasen W(0) = {0, 0, π, π} auf 1,1e−16; Steigungen 1/3 auf 6e−11; Kegelgewicht ≥ 1 − 1,1e−11; det M = −1/27 (2) und +1/27 (2') |
| SH1 | [H] Bei W = 2π folgt das 2-Gewicht ueber 100 Schritte der FJ-Kurve auf 10 % | 45 % | nicht eingetroffen | nicht eingetroffen | D_rel = 0,448 (bei t = 100); je Saat 0,444 bis 0,450; ⟨w_2⟩(100) = 0,717 gegen N_FJ(100) = 0,496 |
| SH2 | [H] Die Ausbreitung des 2-Anteils bleibt bei 1/3 ± 10 % | 60 % | eingetroffen | eingetroffen (alle W, alle Saaten im Band) | v_eff = 0,3048 bei W = 2π (Saaten 0,3044 bis 0,3051); Band 0,300 bis 0,367; v_eff(W = 0) = 0,3237 |

- **Vorbedingungen:** SH1: SH0 (b) erfuellt, N_FJ(100) = 0,496 im Fenster 0,3 bis 0,7. SH2: v_eff(W = 0) = 0,3237 im
  Band.
- **Kartenwortlaut:** SH1 je Saat geprueft, keine unter 0,44. SH2 fuer jedes W > 0 im Saatmittel und je Saat im Band.
- **Woran SH1 haengt:** an der Paketbreite. Die Regel PLAN 2.6 waehlte vor jeder Unordnungsrechnung σ = 4, also das
  Paket mit N_FJ(100) am naechsten bei 0,5. Ein schmaleres k-Paket verliert bei FJ weniger, dann ist das Band von 10 %
  leichter zu halten. Das von σ weniger abhaengige Mass ist die Rueckgabequote r ≈ 0,44.
- **Woran SH2 haengt:** an der Bandbreite. Gegen die eigene W = 0-Kontrolle ist die Ausbreitung bei W = 2π um 5,8 %
  langsamer; die Steigung zwischen t = 50 und 100 faellt von 0,284 auf 0,238 (−16 %).

## Tabellen (Saatmittel; Paket σ = 4 Hop, N = 96, 100 Schritte, α = 0, β = π)

| W | Saaten | w_2(25) | w_2(50) | w_2(100) | D_rel | r(100) | v_eff | v_steig | f_gross(100) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0,9921 | 0,9979 | 0,9979 | 1,014 | 0,996 | 0,3237 | 0,284 | 0,0011 |
| π/8 | 3 | 0,9921 | 0,9978 | 0,9976 | 1,013 | 0,995 | 0,3236 | 0,284 | 0,0012 |
| π/4 | 3 | 0,9921 | 0,9971 | 0,9962 | 1,010 | 0,993 | 0,3234 | 0,283 | 0,0014 |
| π/2 | 3 | 0,9921 | 0,9928 | 0,9899 | 0,997 | 0,980 | 0,3229 | 0,283 | 0,0025 |
| π | 3 | 0,9767 | 0,9617 | 0,9340 | 0,885 | 0,869 | 0,3195 | 0,277 | 0,029 |
| 3π/2 | 3 | 0,9317 | 0,8803 | 0,8037 | 0,622 | 0,611 | 0,3128 | 0,260 | 0,154 |
| 2π | 6 | 0,8841 | 0,8101 | 0,7174 | 0,448 | 0,440 | 0,3048 | 0,238 | 0,306 |
| FJ | | 0,7961 | 0,6614 | 0,4956 | 0 | 0 | 0,3360 | | 0,00013 |

- D_rel = groesste relative Abweichung von der FJ-Kurve ueber t = 1..100; r = (w_2 − N_FJ)/(1 − N_FJ). Fuer W < 2π
  ist r nur ein normierter Ueberschuss, weil der Mittelwert dort nicht FJ ist.
- **Aufteilung bei W = 2π, t = 100:** kohaerenter Teil in 2 (Projektion auf den FJ-Zustand) 0,4937, inkohaerenter
  Teil 0,2237. Bei t = 10, 25, 50: inkohaerent 0,038, 0,088, 0,150.
- **Schwache Unordnung (vorab ableitbar, nur Kontrolle):** Zusatzverlust gegen W = 0, gemittelt ueber t = 51..100:
  1,26e−4 (π/8) und 5,78e−4 (π/4), Verhaeltnis 4,58. Das passt zur W²-Skalierung (Erwartung 4) der Groessenordnung nach.
- **Kohaerente Rueckkehr bei W = 0:** w_2 ≥ 0,9897, w_2(100) = 0,9979, Mittel ueber t = 51..100 minus Mittel ueber
  t = 1..50 = +2,0e−5 (kein Abfluss).
- **Radialprofil des 2-Anteils bei t = 100:** schon bei W = 0 zwei Schalen, bei 26 bis 28 und bei 38 bis 40 Hop. Mein
  Verdacht [H, nicht geprueft]: ein T-erlaubter chiraler Term zweiter Ordnung (Q(k)·σ) macht die beiden Helizitaeten
  bei |k| ≈ 0,2 verschieden schnell. Die Gipfel-Angabe in auswertung.json ist deshalb nicht aussagekraeftig. Bei
  W = 2π fuellt sich das Innere auf (Gewicht schon ab 2 Hop).

## Kontrollen

- **Bloch (W = 0):** w_2-Kurve 1,0e−13; Endzustand aus dem Zyklusoperator U(q)^25 2,7e−14 relativ; schrittweise gegen
  Zyklus 6e−15; zwei Realraum-Fassungen 3,6e−17.
- **Normerhalt:** ≤ 4,3e−14 in allen Laeufen.
- **Randgewicht:** 2-Anteil jenseits 0,75 R_in hoechstens 4,5e−5 (W = 2π), jenseits 0,9 R_in hoechstens 3,3e−9
  (R_in = 78 Hop). FJ 5,0e−5 bzw. 2,1e−9.
- **FJ-Referenz:** in allen drei Laeufen bitgleich (Abweichung 0).
- **Gleichheit H0 = R1:** bis auf Laufzeit und Speicher bitgleich.

## Bedeutung fuer Finns Bild

- **Belegt im Modell [M, E]:** Ein eigener, zufaelliger Takt je Knoten in der verborgenen Haelfte macht die sichtbare
  Haelfte **im Mittel** genau zum doppler-freien FJ-Schachbrett. In jeder einzelnen Welt aber kommt gut 40 % des
  Abgeflossenen zurueck. Es kommt verwuerfelt zurueck: ohne feste Phase und ueber alle Wellenlaengen verteilt.
- **Lesart [H]:** Die "Negativseite" wirkt hier nicht als Ausguss, sondern als Rauschquelle fuer die sichtbare Welt.
  Was FJ als Normverlust verbucht, ist im unitaeren Bild Dekohaerenz: Die Information bleibt erhalten, ihre Phase nicht.
- **Was fehlt:** Wechselwirkung, Masse, ein zweites Pfeil-Eis fuer eine dunkle Spiegelhaelfte (DOSSIER 6.2 Grenze),
  Messbezug. Unbekannt ist auch, ob Takt-Unordnung, die sich mit der Zeit aendert, die Rueckgabe unterdrueckt (dann
  waere die Senke vollkommener) [H].

## Selbstanzeigen

1. **SH1 war naeher an "vorab ableitbar", als die Karte annahm.** Das habe ich vor dem Lauf im Plan offengelegt
   (A8 exakt, A9 heuristisch: r ≈ 1/2). Gemessen ist r = 0,44. Die Messung prueft die Rueckgabequote; das Urteil haengt an
   der Paketwahl (Regel 2.6, vor den Unordnungslaeufen festgelegt).
2. **Teil A habe ich selbst geprueft, kein frischer Leser.** A7, A8 und A9 sind meine Mathematik und nicht
   gegengelesen; die Zahlen bestaetigen A1 bis A8.
3. **Saubere statt gespeicherte Muenze:** Teil B rechnet mit dem exakten Gram-Projektor der FJ-Spinoren, nicht mit
   den gespeicherten Koeffizienten. Beide sind nach diagonaler Eichung auf 1,0e−15 gleich.
4. **Rauchlauf:**
   - R3 zeigte die W = 0-Werte, darunter v_eff(W = 0) als Vorbedingung von SH2 (Kontrollgroesse).
   - R4 lief blind. R5 (N = 24) habe ich nur nach rc und Schluesseln angesehen.
   - Die erste R5-Auswertung brach ab (rc = 1, JSON-Ausgabe von numpy-Wahrheitswerten); behoben vor dem Einfrieren.
   - Die FJ-Kurven fuer fuenf σ (R2) habe ich angesehen; sie sind vorab ableitbar.
5. **Zeilennummern:** Die erste Planfassung nannte fuenf falsche FJ-Zeilen; per grep geprueft und vor dem Einfrieren
   berichtigt.
6. **Hintergrund-ssh:** Die drei Hauptlaeufe habe ich lokal als Hintergrundbefehle gestartet. Das Werkzeug legte ihre
   kurze Ausgabe in seinem Aufgabenordner unter /tmp/claude-1000/ ab. Selbst geschrieben habe ich dort nichts.
7. **Werkzeuge:**
   - Lokal: jq, sed, grep, sha256sum, date, ssh, scp, cp, mv, mkdir. Ausserhalb der Liste: ls, cat, head, cmp, diff.
     Kein python, awk oder perl.
   - Auf der .69 ausserhalb des Starters: cat (Starter lesen), ls, mkdir, mv, sha256sum, grep, uptime, nproc, free,
     date und Warteschleifen "until grep ...; do sleep 5; done" im Vordergrund einer ssh-Sitzung. Kein Python ausserhalb
     des Starters.
8. **Laufbuchhaltung:** Nach dem Einfrieren keine Aenderung an Plan, Code oder Regeln. Jeder Hauptlauf einmal, je ein
   ssh-Aufruf; drei Aufrufe warteten zugleich am Lock von cpu11 (Grenze vier).
9. **Radialprofil:** Die Gipfel-Kennzahl der Auswertung ist bei zwei Schalen irrefuehrend (siehe Tabellen); sie geht
   in kein Urteil ein.
10. **Zahl im eingefrorenen Plan zu klein:** PLAN Abschnitt 7 nennt fuer die Kegelsteigungen "1/3 auf 3e−11". Beim
    Gegenlesen gegen die JSON-Datei stimmt das nur fuer den Zweig auf 2. Auf 2' weicht die Steigung bis 6,0e−11 ab
    (0,33333333339279). Das Urteil aendert sich nicht (Schwelle 1e−4).
11. **Gegenlesen dieser Datei:** Beim Abgleich mit auswertung.json habe ich drei Stellen berichtigt: die
    Nebenbetrag-Genauigkeit (4e−16 statt 3e−16), die Steigungsgenauigkeit (6e−11 statt 5e−11) und die
    Haendigkeits-Aussage (gilt fuer das konjugierte Startpaket). Kein Urteil betroffen.

## Dateien

- **Plan:** PLAN.md, PLAN.md.eingefroren-20261004-180754; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Code:** code/spiegel_haelfte.py, code/auswertung.py (je mit .eingefroren-20261004-180754);
  code/qcad4_repr_2p2s.json und code/qcad4_repr_2p2ss.json (per jq kopiert aus qca-diamant-4/lauf-69/haupt_Bb.json und
  haupt_Bc.json); Gruppenaufbau aus qca-diamant-4/code/qca_diamant.py kopiert.
- **Rauchlaeufe:** rauch-69/rauch1_teilA.json, rauch2_fj.json, rauch3_w0.json, rauch4_w2pi_blind.json,
  rauch5_mini*.
- **Hauptlaeufe:** lauf-69/haupt_0A.json, haupt_1.json, haupt_2.json, haupt_3.json (je mit .log), auswertung.json,
  auswertung.log, PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde42-spiegel-haelfte/ (code/, rauch/, lauf/).

## Einfach gesagt

Wir haben geprueft, ob eine verborgene Haelfte mit eigenem, zufaelligem Takt an jedem Knoten die sichtbare Haelfte
unseres Netzes in das bekannte Schachbrett von Foster und Jacobson verwandelt, das keine Doppelgaenger hat. Im
Durchschnitt ueber viele zufaellige Takte klappt das genau: Die gemittelte Welle ist exakt dieses Schachbrett. In jeder
einzelnen Welt fliesst das Gewicht aber nicht einfach ab. Gut 40 Prozent dessen, was in die verborgene Haelfte geht,
kommen zurueck, nur verwuerfelt und ueber alle Wellenlaengen verteilt. Das Tempo bleibt mit 0,30 knapp im Band um ein
Drittel, wird mit staerkerer Unordnung aber langsamer. Das ist eine Rechnung im Modell, keine Messung.
