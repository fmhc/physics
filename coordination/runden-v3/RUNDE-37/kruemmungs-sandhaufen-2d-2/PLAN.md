# KRUEMMUNGS-SANDHAUFEN-2D-2: Plan (Code-Agent fuer die Leitung claude-primary, Runde 49)

- **Zeiten (date, CEST):** Start 12:04:14. Vorlage gelesen bis ~12:10. Codekopie 12:10:55, Erweiterung ksh2.py bis 12:13:51.
  Plantext ab 12:14:31. Rauchtests erst nach Abschluss dieses Texts (Startzeit in Abschnitt 11). Einfrierzeit steht in
  EINGEFROREN-SHA256.txt.
- Grundlage: KARTE.md (Vorhersagen KS0 bis KS4 unveraendert). Vorlage: RUNDE-37/kruemmungs-sandhaufen-2d-1/
  (KARTE.md, PLAN.md.eingefroren-20261005-113347, ERGEBNIS.md, code/ksh.py eingefroren f2c3627a..., aus-69/urteile.json,
  nachtrag-69/alter.json mit code/nachtrag_alter.py). Dort wird nichts geaendert.
- Alles ist eine synthetische, kombinatorische Modellrechnung, keine Messdatenbestaetigung. Kennzeichen: [M] Mathematik
  vorab, [F] Festlegung dieses Plans, [V] woertlich aus dem eingefrorenen Plan der Vorlage, [P] Projektdatei,
  [L] Literatur aus dem Gedaechtnis, [H] Hypothese, [ES] eigener Schluss, [N] Nachtrag nach Sicht.

## 1. Code [F]

- code/ksh-vorlage-2d-1.py: unveraenderte Kopie der eingefrorenen Vorlage (sha256 f2c3627a..., gleich
  ksh.py.eingefroren-20261005-113347).
- code/ksh2.py: dieselbe Datei mit genau drei Aenderungen (diff gegen die Kopie liegt bei):
  1. zustand() zaehlt zusaetzlich das Gradhistogramm der inneren Ecken (Grad 3 bis 15, letzte Klasse 16+) und haengt es
     an jede Zeitreihenzeile (alle 1000 Schritte, Einschwingen und Messung). Kein Zugriff auf den Zufallsstrom.
  2. Kartenname im Kopf der Ausgabe.
  3. Neuer Befehl `aus2` (Abschnitte 6 bis 9). Die Auswertefunktionen der Vorlage (analyse_fall, Fits M1/M2/M3,
     Stuetze, bin_pruefung, d_fit, Block-Bootstrap) sind unveraendert und werden aufgerufen.
- Modell, Kippregel, Wellen, Zulaessigkeit, Antrieb, Zusatzantrieb r, Anfangsrelaxation, Einschwingen, Pruefungen
  (KH0-Pruefung je Schritt, volle Strukturpruefung alle 2000 Schritte) und alle Konstanten (SMIN 2, CAPF 50, RELAXF 100,
  EINF 10, EIN_ANTEIL 0,4, MMAX 300 000, VOLLPRUEF 2000, REIHE 1000) sind die der Vorlage [V]. Nur der zufaellige Arm Z,
  nur die Kugel (konvexe Huelle von N gleichverteilten Punkten, Netzsaat 1000 + N) [V, Karte "Nur der zufaellige Arm"].
- **Antriebsrate r [V, Vorlage PLAN 8]:** Waehrend der Lawine folgt mit Wahrscheinlichkeit r nach jedem Kipp-Flip ein
  zusaetzlicher Antriebsflip (zaehlt nicht in s). r = 0 ist volle Zeitskalentrennung.
- **Identitaetskontrolle K-ID [F]:** Ein kurzer Lauf mit Saat 11, N = 2000, r = 0 (wie 2D-1, Lauf L1) muss die
  Lawinenfolge (s, T, A, Status), die Anfangsrelaxation und die Zeitreihen (ohne die neue Spalte) der Vorlage im
  ueberlappenden Teil bitgleich wiedergeben. Das prueft, dass ksh2.py dieselbe Dynamik und dasselbe Netz hat
  (Kennzahlen-Abgleich der Karte). K-ID ist eine Code-Kontrolle, keine Vorhersage. Bei "nicht identisch" werden alle
  Urteile mit dem Vorbehalt "Code nicht identisch" versehen.

## 2. Faelle, N, Raten, Saaten, Budgets [F]

| Lauf | Spur | Fall | Zweck | Saat | Budget (s) |
|---|---|---|---|---|---|
| L1 | cpu | Kugel, Z, N = N_max (= 16000 nach Abschnitt 11), r = 0,01 | KS1, KS3, KS4 | 21 | 520 |
| L2 | cpu7 | Kugel, Z, N = 8000, r = 0,01 | KS1, KS2, KS3 | 22 | 300 |
| L3 | cpu7 | Kugel, Z, N = 8000, r = 0,003 | KS2, KS3 | 23 | 300 |
| L4 | cpu | Kugel, Z, N = 8000, r = 0,03 | Rate (beschreibend), KS3 | 24 | 300 |
| L5 | cpu7 | Kugel, Z, N = 2000, r = 0,01 | KS1, KS3 | 25 | 90 |
| L6 | cpu7 | Kugel, Z, N = 2000, r = 0 | KS0, KS3 | 26 | 90 |
| L7 | cpu | Kugel, Z, N = 2000, r = 0 | K-ID (Code-Kontrolle) | 11 | 60 |
| AUS | cpu | aus2 ueber L1 bis L7 und die Vorlage | Urteile, Tabellen, Bilder | - | - |

- **KS0 mit neuer Saat [F]:** "Dieselben Einstellungen" heisst hier: Kugel, Arm Z, N = 2000, r = 0, Budget 90 s, gleiche
  Konstanten und gleiches Netz (Netzsaat 3000) wie 2D-1. Die Dynamik-Saat ist neu (26). Mit Saat 11 waere die
  Lawinenfolge bitgleich mit 2D-1 (K-ID), der Ausgang also vorab festgelegt; das waere kein Test.
- Budgets 90 und 300 s wie in 2D-1 fuer N = 2000 und 8000. Fuer N_max 520 s, damit der Lauf mit Netzbau, Relaxation,
  Speichern und hoechstens einer ueberlaufenden Lawine unter RuntimeMaxSec 600 bleibt.
- **N_max [F]:** das groesste N aus {16000, 24000, 32000}, das nach den Rauchtests R1 bis R3 "machbar" ist:
  - Durchsatz v = 0,8 * min(Einschwing-Durchsatz, Mess-Durchsatz) im Rauchtest (Schritte je s, Faktor 0,8 als Reserve
    fuer wachsende Lawinen), t_vor = Fallzeit - Einschwingzeit - Messzeit (Netzbau, Relaxation, Pruefungen).
  - machbar, wenn t_vor + 10 N / v <= 0,4 * 520 s = 208 s (Einschwingen 10 N voll, nicht zeitbegrenzt) UND
    t_vor + 20 N / v <= 0,95 * 520 s (mindestens 10 N Messschritte).
  - Ist keines machbar, gilt N_max = 16000 (Kartenminimum) mit Budget 520 s; ein zeitbegrenztes Einschwingen wird dann
    als Vorbehalt gemeldet.
  - Erwartung vorab [ES aus den Laufzeiten der Vorlage, N = 8000: 1358 Schritte/s]: N_max = 16000.
- **Zahl der Lawinen [F]:** ergibt sich aus Budget und MMAX (300 000 Schritte). Erwartet etwa 82 % der Schritte mit
  s >= 1 (Vorlage): N = 2000 ~150 000 Lawinen, N = 8000 bis ~245 000, N_max bis ~245 000. Berichtet wird die echte Zahl.
- **Einschwingzeit [V]:** Anfangsrelaxation ohne Antrieb (bis 100 N Flips, nicht gemessen), dann 10 N Schritte
  Einschwingen (hoechstens 40 % des Fallbudgets, nicht gemessen), dann Messung bis 300 000 Schritte oder Budgetende. Die
  Drift-Probe (Abschnitt 7) prueft, ob 10 N reicht; sie ersetzt eine laengere Einschwingzeit, die bei N_max nicht in
  10 min passt.
- Gleiche r-Werte und gleiches Einschwingen fuer alle N; Alter = (Einschwingschritte + Messschritt) / N.

## 3. Messgroessen je Fall [V, plus Gradhistogramm]

- je Schritt: s (Kipp-Flips), T (Wellen), A (verschiedene gekippte Ecken), Status 0 bis 3 (Rohdaten npz).
- Zeitreihe alle 1000 Schritte: mittleres s, Defektanteil, mittleres q^2, instabile Ecken, kleinster/groesster Grad,
  **neu: Gradhistogramm** (Grad 3 bis 15, 16+).
- Zaehler: Zusatzantriebe (extra_antrieb), blockierte Versuche, Antriebs-Fehlversuche; KH0-Pruefungen (beschreibend).

## 4. Auswerteregeln der Vorlage, woertlich [V, Vorlage PLAN 6]

- **Fitstichprobe:** Lawinen mit s >= s_min = 2 und Status 0 oder 1. Traeger 2 bis 50 N.
- **Modelle:** M1 p(s) ~ s^(-tau) exp(-s/s_c); M2 exp(-s/s_0); M3 exp(-(s/s_0)^beta); diskrete Maximum-Likelihood,
  Normierung exakt bis 3000, darueber log-Gitter (4001 Punkte); AIC = 2k + 2 NLL.
- **P2D** ("Potenzgesetz ueber mindestens 2 Dekaden") = alle fuenf Bedingungen:
  - (a) AIC(M2) - AIC(M1) >= 10 und AIC(M3) - AIC(M1) >= 10;
  - (b) s_c(M1) >= 100 s_min = 200;
  - (c) Fitguete: Log-Bins (10 je Dekade ab s = 2); in jedem Bin mit mindestens 100 Lawinen und Obergrenze <= s_c/2
    weicht die Zahl hoechstens um den Faktor 10^0,15 vom M1-Erwartungswert ab; mindestens ein solcher Bin;
  - (d) mindestens 50 Lawinen mit s >= 200;
  - (e) Abbruchanteil (Status 2 oder 3) unter den Lawinen s >= 1 hoechstens 0,1 %.
  - Entscheidbarkeit: "ja" nur mit mindestens 5000 Lawinen in der Fitstichprobe; "nein", wenn (e) verletzt ist oder bei
    mindestens 1000 Lawinen eine von (a) bis (d) verletzt ist; sonst "nicht bestimmbar".
- **tau:** M1-Schaetzwert, 95-%-Intervall aus Block-Bootstrap (20 Bloecke, 100 Ziehungen).
- **s_c2 (Hauptschaetzer):** Momentverhaeltnis <s^2>/<s> ueber alle Lawinen s >= 1 der Messung (auch Abbrueche mit ihrem
  s). Fehler aus Block-Bootstrap (20 zeitlich zusammenhaengende Bloecke, 200 Ziehungen).
- **D:** Steigung der Ausgleichsgeraden log s_c2 gegen log N; Fehler aus 200 Bootstrap-Tripeln (je N unabhaengig),
  95-%-Intervall aus den 2,5- und 97,5-%-Quantilen.
- **Stationaritaet:** Mittelwert von s in erster gegen zweite Messhaelfte (je 10 Bloecke), z > 3 = "Drift"
  (Vorbehalt, aendert das Urteil nicht).
- **Eichung:** Die BTW-Eichung derselben Auswertefunktionen ist in 2D-1 bestanden (P2D BTW N = 8000 "ja") [P]. Die
  Funktionen sind unveraendert; die Eichung gilt hier weiter und wird nicht neu gerechnet.

## 5. Gradverteilung im stationaeren Zustand [F]

- rho_k = Anteil der Ecken vom Grad k (Kugel: alle Ecken innen), gemittelt ueber alle Zeitreihenzeilen der Messung
  ("ganz") und getrennt ueber die Zeilen der ersten und der zweiten Messhaelfte (Schritt <= m/2 bzw. > m/2).
- Berichtet fuer jeden Fall: rho4 bis rho8, Rest, das volle Histogramm (Mittel ueber die Messung) und die groben
  Verzweigungszahlen 2 rho5 + rho7 und rho5 + 2 rho7 (Mittelfeld-Kopfrechnung aus 2D-1, nur beschreibend).
- Zeitreihe rho5/rho6/rho7 gegen das Alter als Bild (Einschwingen und Messung).

## 6. Drift-Probe (Pflicht) [F, nach Vorlage-Nachtrag NA1]

- **Je Fall:** s_c2 und mittleres s je Messviertel (wie nachtrag_alter.py); Alter am Ende jedes Viertels.
- **Je Gruppe G** (KS1: die drei N bei r = 0,01; KS2: r = 0,003 und 0,01 bei N = 8000):
  - A_start = groesstes Einschwing-Ende (Einschwingschritte / N) in G, A_ende = kleinstes Alter am Messende in G.
  - **W1** = Alter (A_start, A_ende]: alle Faelle gleich alt (wie NA1 "Alter 10 bis 47,5").
  - **W2** = spaetere Haelfte von W1: Alter ((A_start + A_ende)/2, A_ende] (wie NA1 "Alter 30 bis 47,5").
  - In jedem Fenster s_c2 ueber die Lawinen s >= 1, Block-Bootstrap (20 Bloecke, 200 Ziehungen, je Fall und Fenster
    eigener Zufallsstrom), daraus D (KS1) bzw. der Quotient (KS2) mit 95-%-Intervall.
- **Wirkung auf die Urteile:** Jede Regel aus Abschnitt 8, die s_c2 benutzt, wird auf drei Schaetzer angewandt:
  Hauptschaetzer (ganze Messung), W1 und W2. Stimmen alle drei Urteile ueberein, ist das das Urteil nach Plan. Sonst
  lautet es "nicht entscheidbar (Drift)".
- Fuer KS3 entspricht das: ganze Messung und zweite Messhaelfte; fuer KS4: P2D auf der ganzen Messung und auf der
  zweiten Messhaelfte (Schritte m/2 bis m) des groessten N.
- KS0 vergleicht ganze Messung mit ganzer Messung bei gleichen Einstellungen (gleiche Alter); dort keine Drift-Probe,
  die Viertel werden berichtet.

## 7. Urteilsregeln nach Plan [F; mechanisch in ksh2.py aus2]

- **KS0:** Q = s_c2(L6) / 830,0857502893972 (s_c2 kugel-Z-N2000 aus 2D-1, aus/urteile.json). Eingetroffen, wenn
  abs(Q - 1) <= 0,15; sonst nicht eingetroffen. Plan = Wortlaut. Berichtet: s_c2 mit 95-%-Intervall, Viertel.
  Zusatz: aus2 rechnet die Vorlage aus deren Rohdaten neu; gleich 830,0857... ist eine Kontrolle der Auswertung.
- **KS1 (je Schaetzer):** D und s_c2 aus L5 (N = 2000), L2 (N = 8000), L1 (N_max), r = 0,01.
  - eingetroffen, wenn die untere 95-%-Grenze von D >= 0,3 ist und s_c2 mit N streng waechst;
  - nicht eingetroffen, wenn die obere 95-%-Grenze < 0,3 ist;
  - sonst nicht entscheidbar. (Vorlage KH3 [V] mit der Grenze der Karte "D >= 0,3".)
  - Urteil nach Plan: Kombination Hauptschaetzer, W1, W2 (Abschnitt 6).
- **KS2 (je Schaetzer):** Q = s_c2(r = 0,01) / s_c2(r = 0,003) bei N = 8000 (L2 / L3); 95-%-Intervall aus den paarweisen
  Quotienten unabhaengiger Bootstrap-Ziehungen (je 200).
  - eingetroffen, wenn das Intervall ganz in (1/1,5; 1,5) liegt;
  - nicht eingetroffen, wenn das Intervall ganz ausserhalb liegt (untere Grenze >= 1,5 oder obere Grenze <= 1/1,5);
  - sonst nicht entscheidbar. Urteil nach Plan: Kombination Hauptschaetzer, W1, W2.
- **KS3:** alle Kugelfaelle dieser Karte, L1 bis L6 (alle N und alle r; K-ID zaehlt nicht). Je Fall: "drin", wenn
  0,25 <= rho5, rho6, rho7 <= 0,40.
  - Je Fall: drin in ganzer Messung und zweiter Haelfte = eingetroffen; in beiden draussen = nicht eingetroffen;
    gemischt = nicht entscheidbar (Drift).
  - Gesamt: nicht eingetroffen, wenn ein Fall nicht eingetroffen ist; eingetroffen, wenn alle Faelle eingetroffen sind;
    sonst nicht entscheidbar (Drift).
- **KS4:** groesstes N (L1, r = 0,01). P2D (Abschnitt 4) auf der ganzen Messung und auf der zweiten Haelfte:
  "ja" = eingetroffen, "nein" = nicht eingetroffen, "nicht bestimmbar" = nicht entscheidbar; Kombination beider wie
  Abschnitt 6. Die Eichung aus 2D-1 gilt (Abschnitt 4); ohne sie waere ein "nein" "nicht entscheidbar (Eichung)".
- Fehlt ein Fall (Lauf zweimal gescheitert), ist das betroffene Urteil "nicht entscheidbar (fehlt)".
- Vorbehalte (aendern das Urteil nicht): Planflag Drift (z > 3), zeitbegrenztes Einschwingen, Abbruchanteil > 0,1 %,
  K-ID nicht identisch.

## 8. Urteilsregeln nach Kartenwortlaut [F]

Die Karte nennt keine Intervalle und kein Altersfenster. Die Wortlaut-Spalte liest die Saetze woertlich mit den
Punktschaetzern der ganzen Messung:
- **KS0:** wie Plan.
- **KS1:** eingetroffen, wenn D (Punktschaetzer, Hauptschaetzer) >= 0,3 und s_c2 mit N streng waechst; sonst nicht
  eingetroffen.
- **KS2:** eingetroffen, wenn 1/1,5 < Q < 1,5 (Punktschaetzer, ganze Messung); sonst nicht eingetroffen.
- **KS3:** eingetroffen, wenn in allen Kugelfaellen L1 bis L6 die Mittel der ganzen Messung rho5, rho6, rho7 in
  [0,25; 0,40] liegen; sonst nicht eingetroffen.
- **KS4:** "ueber mindestens 2 Dekaden" = (b) s_c >= 200; "Fitguete <= 0,15" = (c); "Potenzgesetz vor gestreckter
  Exponentialfunktion um dAIC > 10" = AIC(M3) - AIC(M1) > 10 (Karte: echt groesser). Eingetroffen, wenn alle drei gelten
  und mindestens 5000 Lawinen in der Fitstichprobe sind; nicht eingetroffen, wenn eine verletzt ist und mindestens 1000
  Lawinen da sind; sonst nicht entscheidbar. (a) gegen M2, (d) und (e) werden berichtet, entscheiden hier aber nicht.

## 9. Beschreibende Kontrollen [F]

- Antriebsrate bei N = 8000: s_c2, tau, P2D, <s>, Zusatzantriebe fuer r = 0,003 / 0,01 / 0,03, dazu r = 0 aus 2D-1 [P]
  (s_c2 = 988,9 [863,3; 1 120,8]) als Bezug. Kein eigenes Urteil.
- Quotient der Raten 0,01 / 0,03 und D-Fit aus s_c2 gegen r nur beschreibend.
- KH0-Pruefungen (Summe q = 12, Grad >= 3, Kantenzahl, volle Pruefungen) je Fall, beschreibend.
- Bilder: P(s) fuer r = 0,01 je N (mit M1-Fit), P(s) je r bei N = 8000, KS0 (2D-1 gegen 2D-2), rho5/rho6/rho7 gegen
  das Alter, s_c2 gegen N je Schaetzer.

## 10. Laufliste und Ablauf (.69, kleintest.sh; Arbeitsordner /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-2/)

- Aufruf je Lauf: `bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <name> code/ksh2.py lauf --geo kugel
  --arm Z --N <N> --budget <B> --r <r> --seed <saat> --out lauf/<Lx>` (1 Thread, RuntimeMaxSec 600).
- AUS: `code/ksh2.py aus2 --ks0 lauf/L6.json --kid lauf/L7.json
  --ref /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1/lauf/kugel-Z.json --r001 lauf/L5.json lauf/L2.json
  lauf/L1.json --r0003 lauf/L3.json --r003 lauf/L4.json --out aus/urteile.json --bild aus` (Spur cpu, nach beiden Ketten).
- Ketten: code/kette-cpu.sh (L1, L4, L7, dann AUS nach der Marke der Kette cpu7, Warten hoechstens 20 min) und
  code/kette-cpu7.sh (L2, L3, L5, L6, dann Marke). Erwartete Dauer ~15 min (cpu) bzw. ~13 min (cpu7), AUS ~2 min.
- Ein Lauf mit rc != 0 wird einmal mit demselben Aufruf wiederholt (gekennzeichnet).
- Schlusszeit: Nach 11:35 UTC (13:35 CEST) startet kein neuer Lauf; AUS startet spaetestens 11:50 UTC.
- Eingefrorener Code per scp in einen neuen Ordner, dann mv nach code/ (nie in place).

## 11. Rauchtests (nach diesem Text, vor dem Einfrieren; je <= 120 s)

- R1 (cpu): N = 16000, r = 0,01, Budget 100 s, Saat 91. R2 (cpu7): N = 24000, Saat 92. R3 (cpu): N = 32000, Saat 93.
- R4 bis R9 (cpu7, kleine Budgets 10 bis 20 s, Saaten 94 bis 99 bzw. 11): je ein Fall wie L6, L7, L5, L2, L3, L4.
- R10 (cpu): aus2 ueber R1 und R4 bis R9 (Rolle N_max = R1).
- Gelesen werden nur rc, Laufzeiten, Dateinamen, JSON-Schluessel und fuer N_max die Schrittzahlen und Zeiten von
  Einschwingen und Messung in R1 bis R3 (Durchsatz). Keine Werte zu s_c2, P(s), Fits, Gradanteilen oder Urteilen.
- Der Durchsatz haengt ueber <s> mittelbar an der Lawinenstatistik; das wird als moegliche indirekte Sicht vermerkt.
- **Ergebnis (Nachtrag vor dem Einfrieren):** Rauchketten 10:16:57 bis 10:22:50 UTC, Code code-r1/ksh2.py
  (sha256 1a1b4e26...). R1 bis R10 alle rc = 0; Dienstlaufzeiten R1 bis R3 je 1 min 41 s, R4 bis R9 10 bis 20 s,
  R10 (aus2) 21,7 s. Keine Warnung und kein Traceback in den Logs. aus2 schrieb urteile.json mit allen Schluesseln
  (urteile KS0 bis KS4, drift, k_id, faelle) und fuenf Bilder. Gelesen: rc, Laufzeiten, Schluessel und die
  Durchsatzzahlen unten; keine Werte zu Lawinen, Fits, Gradanteilen, K-ID oder Urteilen.
- Die cpu7-Rauchkette startete wegen eines Startfehlers (Wettlauf mkdir/Umleitung im ssh-Aufruf) erst 10:19:18 UTC.
- **N_max nach Abschnitt 2** (Kopfrechnung aus Schrittzahl / Zeit; Fallbudget 100 s, Einschwingen zeitbegrenzt):

| N | Einschwingen (Schritte / s) | Messung (Schritte / s) | v = 0,8 min | t_vor (s) | t_vor + 10 N / v (s) | Grenze | machbar |
|---|---|---|---|---|---|---|---|
| 16000 | 42 245 / 38,51 = 1097,0 | 56 000 / 59,93 = 934,4 | 747,5 | 1,94 | 216,0 | 208 | nein (knapp) |
| 24000 | 32 320 / 37,87 = 853,4 | 44 000 / 59,90 = 734,6 | 587,7 | 2,80 | 411,2 | 208 | nein |
| 32000 | 27 505 / 37,29 = 737,6 | 37 986 / 59,50 = 638,4 | 510,7 | 3,69 | 630,3 | 208 | nein |

  - Keines ist nach der Regel machbar. Also gilt N_max = 16000 (Kartenminimum), Budget 520 s (Abschnitt 2). Ohne den
    Reservefaktor 0,8 braeuchte das Einschwingen bei N = 16000 etwa 160000 / 934 = 171 s < 208 s; ein zeitbegrenztes
    Einschwingen wird in L1 trotzdem geprueft und gemeldet.
- **Aenderung nach dem Rauchtest (vor dem Einfrieren):** bild_sc2_N klemmt negative Fehlerbalken auf 0 (Robustheit,
  matplotlib lehnt negative yerr ab). Sonst keine Codeaenderung gegenueber code-r1.

## 12. Erwartung des Code-Agenten (vorab, nicht bindend, nur zur Kalibrierung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| E0 | KS0 eingetroffen | 80 % |
| E1 | KS1 nach Plan eingetroffen (Vorlage r = 0: s_c2 2000 -> 8000 nur x 1,19) | 15 % |
| E2 | KS2 nach Plan eingetroffen | 35 % |
| E3 | KS3 nach Plan eingetroffen | 75 % |
| E4 | KS4 nach Plan eingetroffen | 20 % |
| E5 | K-ID identisch | 95 % |
| E6 | N_max = 16000 | 85 % |

## 13. Vorab-Negativliste

- Kein Ergebnis dieses 2D-Modells sagt etwas ueber Lambda, Schwerewellen oder Finns 3D-Netz direkt.
- "SOC gezeigt" nur, wenn KS1, KS2 und KS4 nach Plan eingetroffen sind (Bedeutung der Karte); sonst hoechstens
  "Potenzgesetz unter diesen Regeln" oder "breite Lawinen".
- Ein Exponent tau wird nur mit dem Hinweis zitiert, dass die Methode das BTW-tau in 2D-1 zu klein schaetzte (1,07).
- Ein D aus nur drei N und unter einer Dekade (2000 bis N_max) ist kein Nachweis einer Potenzgesetz-Skalierung in N.
