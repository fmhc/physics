# FADEN-DIM-2: Ergebnis (Runde 43, Fast Lane)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 21:59:20 CEST (date). Plan und Code eingefroren
  22:13:56 CEST (Stempel 20261004-221356), vor jeder Rechnung mit Treffzahlen. Laeufe 22:14:10 bis 22:22:23 CEST,
  Auswertung und Bild 22:22:36 CEST. ERGEBNIS geschrieben ab 22:24:55 CEST (date).
- Alle Messzahlen [E]: .69, kleintest.sh, Spuren cpu und cpu10, 1 Thread, eingefrorener Code. Vier Laeufe, alle rc = 0,
  keine Zelle abgebrochen. Die Urteile rechnet der eingefrorene Code (fd2.py auswertung); von Hand gegen die Tabelle
  geprueft.
- Kennzeichen: [E] gerechnet, [M] eigene Mathematik von Hand (nicht gegengelesen), [L] Literatur aus dem Gedaechtnis,
  [H] Hypothese, [D] Diagnose nach Sicht (nicht Teil der Urteile).
- **Alles synthetisch:** Gittermodell gerichteter Faeden (RSOS) auf Z_L^D, keine Messdaten.
- Modell wie FADEN-DIM-1 (faden.py bytegleich): Windung +1 und -1 um Richtung 1, Treffen = gemeinsamer Knoten.
  G = starre Faeden mit Zufallsverschiebung. RP = dieselbe Verschiebung plus lokale Metropolis-Zuege (Rauheit).
  T = 4 L^2 Schritte. Neu: Biegesteifigkeit kappa je (D, L) so, dass die Knickdichte der geschlossenen Faeden genau
  0,6 ist (exakt abgezaehlt, Abschnitt 3 im Plan).

## 1. Ergebnis zuerst

1. **Raue Faeden in D = 4 treffen sich bei konstanter Rauheit mit wachsendem L immer seltener [E]:** Treffanteil
   0,840 (L = 16), 0,747, 0,694, 0,604, 0,543 (L = 64), je 3072 Paare. Lokale Steigung von ln P zwischen L = 32 und
   64: -0,352 [-0,407; -0,297], ganz unter der Schwelle -0,25. Nach der Schwellregel von FADEN-DIM-1 heisst das
   **Grenze 3. FD2 ist in beiden Lesarten eingetroffen.**
2. **Rauheit halbiert ungefaehr den Abfall [E]:** Exponent der Rate -ln(1 - P) ueber L = 16 bis 64: rau -0,607
   [-0,651; -0,566], glatt (L = 32 bis 64) -1,10 [-1,23; -0,97]. **FD1 ist in beiden Lesarten eingetroffen**, das
   ganze 95-%-Intervall liegt im Band [-0,75; -0,35].
3. **Kontrolle glatt (FD0) eingetroffen [E]:** P L = 5,13 / 5,12 / 4,98 (L = 32 / 48 / 64), Faktor 1,03. Das war
   vorab ableitbar (Plan 1c: 4,9 / 5,0 / 5,1).
4. **Die "Grenze 4" aus FADEN-DIM-1 haelt nicht [D]:** Dort gab es -0,20 ueber L = 8 bis 32, mit Rauheit, die mit
   L wuchs. Hier, mit konstanter Rauheit, kommt -0,305 [-0,326; -0,285] schon ueber L = 16 bis 64 heraus, und die
   lokalen Steigungen werden mit L steiler (-0,29 / -0,26 / -0,34 / -0,37). Beides traegt bei: kleine L (Saettigung)
   und die mitwachsende Rauheit. Ich kann es nicht auf eine Ursache allein schieben.
5. **Kapazitaets-Skizze der Leitung [M, E]:** Sie stimmt in Richtung und asymptotischen Exponenten. Der gemessene
   Raten-Exponent -0,61 ist aber steiler als ihre -1/2, und die lokalen Werte zeigen keinen gesicherten Gang zu -1/2
   (Abschnitt 6). D = 5 (beschreibend): P faellt mit -1,11, Rate mit -1,30.

## 2. Urteilstabelle

| Nr | Karte | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| FD0 | Kontrolle: G, D = 4, P L zwischen L = 32 und 64 konstant bis Faktor 1,5 (85 %) | **eingetroffen**: Faktor aus Wilson-Grenzen 1,180 <= 1,5 (Punktfaktor 1,030) | **eingetroffen**: P L = 5,125 / 5,121 / 4,977, Faktor 1,030 <= 1,5 |
| FD1 | [H, M] RP, Rauheit 0,6, D = 4: Exponent der Rate ueber L = 16 bis 64 in [-0,75; -0,35] (60 %) | **eingetroffen**: -0,607, Bootstrap-95-% [-0,651; -0,566] ganz im Band; alle fuenf L im Rauheitsband | **eingetroffen**: Punktwert -0,607 im Band |
| FD2 | [H] RP, Rauheit 0,6, D = 4: lokale Steigung von P zwischen L = 32 und 64 unter -0,25, also Grenze 3 (75 %) | **eingetroffen (Grenze 3)**: Fit ueber L = 32, 48, 64: -0,352 [-0,407; -0,297]; < -0,25 und obere Grenze < 0; ganzes Intervall unter -0,25 | **eingetroffen**: Zwei-Punkt-Steigung L = 32 auf 64: -0,354 [-0,414; -0,294] < -0,25 |

- **Bedeutung nach der Karte (vorab):** FD1 und FD2 eingetroffen. Raue Faeden treffen sich in 4 Raumdimensionen
  leichter, aber mit wachsender Groesse immer seltener. Die Grenze 3 fuer Faeden (Brandenberger/Vafa) ist in diesem
  Modell robust gegen Rauheit. "Rauheit halbiert ungefaehr den Abfallsexponenten" [H]: gemessen 0,607/1,102 = 0,55.
- Zu "Grenze 3": Die Regel braucht auch einen Abfall bei D >= 5. D = 5 faellt hier deutlich (-1,11, beschreibend);
  D = 6 fiel in FADEN-DIM-1 (-1,84 bei p = 0,6).
- Die Lesart entscheidet hier nichts: Plan und Kartenwortlaut geben fuer FD0 bis FD2 dasselbe Urteil.

## 3. Tabellen [E]

**D = 4: Treffanteil bis T = 4 L^2 (Wilson-95-%), Rate, Knickdichte, kappa**

| L | G: P (Treffer/Paare) | G: P L | RP: P (Treffer/Paare) | RP: Rate -ln(1-P) | RP: Knickdichte Start / Ende | kappa |
|---|---|---|---|---|---|---|
| 16 | - | - | 0,840 (2581/3072) [0,827; 0,853] | 1,833 | 0,599 / 0,591 | 0,6145 |
| 24 | - | - | 0,747 (2295/3072) [0,731; 0,762] | 1,374 | 0,601 / 0,603 | 0,6409 |
| 32 | 0,160 (1312/8192) [0,152; 0,168] | 5,13 | 0,694 (2132/3072) [0,678; 0,710] | 1,184 | 0,602 / 0,598 | 0,6540 |
| 48 | 0,107 (874/8192) [0,100; 0,114] | 5,12 | 0,604 (1854/3072) [0,586; 0,621] | 0,925 | 0,599 / 0,598 | 0,6671 |
| 64 | 0,078 (637/8192) [0,072; 0,084] | 4,98 | 0,543 (1668/3072) [0,525; 0,561] | 0,783 | 0,600 / 0,601 | 0,6736 |

**D = 5 (beschreibend), RP, Rauheit 0,6, je 4096 Paare**

| L | P (Treffer) [Wilson] | Rate | Knickdichte Start / Ende | kappa |
|---|---|---|---|---|
| 8 | 0,408 (1672) [0,393; 0,423] | 0,525 | 0,601 / 0,599 | 0,6287 |
| 12 | 0,272 (1114) [0,259; 0,286] | 0,318 | 0,602 / 0,599 | 0,6952 |
| 16 | 0,192 (786) [0,180; 0,204] | 0,213 | 0,599 / 0,600 | 0,7311 |
| 24 | 0,118 (484) [0,109; 0,128] | 0,126 | 0,599 / 0,599 | 0,7671 |

**Steigungen von ln P und Exponenten der Rate** (gewichtete Gerade, Bootstrap-95-%)

| Serie | L-Fenster | Steigung ln P | Exponent Rate |
|---|---|---|---|
| RP D = 4 | 16 bis 64 | -0,305 [-0,326; -0,285] | **-0,607 [-0,651; -0,566]** (FD1) |
| RP D = 4 | 32, 48, 64 | **-0,352 [-0,407; -0,297]** (FD2 Plan) | - |
| RP D = 4 | 32 auf 64 (zwei Punkte) | **-0,354 [-0,414; -0,294]** (FD2 Karte) | - |
| RP D = 4 | 16-24 / 24-32 / 32-48 / 48-64 | -0,29 / -0,26 / -0,34 / -0,37 | -0,71 / -0,52 / -0,61 / -0,58 |
| G D = 4 | 32 bis 64 | -1,033 [-1,153; -0,909] | -1,102 [-1,230; -0,971] |
| G D = 4 | 32-48 / 48-64 | -1,00 / -1,10 | -1,08 / -1,15 |
| RP D = 5 | 8 bis 24 | -1,107 [-1,174; -1,035] | -1,298 [-1,381; -1,218] |
| RP D = 5 | 8-12 / 12-16 / 16-24 | -1,00 / -1,21 / -1,19 | -1,24 / -1,39 / -1,30 |

- Intervalle der lokalen Werte RP D = 4 (ln P): [-0,35; -0,23], [-0,36; -0,15], [-0,44; -0,25], [-0,53; -0,22];
  Rate: [-0,87; -0,56], [-0,74; -0,30], [-0,77; -0,45], [-0,81; -0,33]. Alle Fits in lauf-69/auswertung.txt.
- Median der Treffzeit / L^2: RP D = 4: 1,20 / 1,28 / 1,38 / 1,54 / 1,61 (waechst mit L); G D = 4: 1,85 / 2,00 / 1,91;
  RP D = 5: 1,72 / 1,87 / 1,90 / 1,92. Annahmerate der lokalen Zuege: D = 4 0,108 bis 0,102; D = 5 0,086 bis 0,075.

## 4. Bild

BILD-faden-dim-2.png (gleich lauf-69/faden-dim-2.png). Links: D = 4, P (gefuellt, Wilson-Balken) und Rate (offen)
gegen L, doppelt logarithmisch, rau und glatt. Mitte: lokale Steigungen von ln P je Nachbarpaar von L, dazu der
FD2-Fit (Balken) und die Schwelle -0,25. Rechts: D = 5, P und Rate.

## 5. Kontrollen

- **FD0 gegen die Ableitung (K0) [E gegen M]:** gemessen 0,160 / 0,107 / 0,078, vorab 1 - exp(-5,28/L) = 0,152 /
  0,104 / 0,079. FADEN-DIM-1 hatte bei L = 32 mit 16384 Paaren 0,153 (Abstand ~ 1,5 Fehlerbreiten) [M nach Sicht].
- **Rauheit konstant [E]:** Start-Knickdichte aller RP-Zellen 0,5986 bis 0,6021, also im Band 0,59 bis 0,61.
  Am Ende (nur ueberlebende Paare) 0,5906 bis 0,6031. Den tiefsten Wert 0,591 hat L = 16: Dort ueberleben nur 16 %,
  und es bleiben eher die glatteren Paare uebrig [D, H].
- **Kalibrierung [E]:** Die exakte Formel trifft die Start-Knickdichten von FADEN-DIM-1 (Abweichung hoechstens
  0,0075). Die Dynamikprobe D = 5, L = 12 lag vor dem Einfrieren bei 0,615. Im Lauf mit 4096 Paaren: 0,602 am Start,
  0,599 am Ende. Die Abweichung war also Zufall.
- **Bloecke [E, M nach Sicht]:** L = 48: 617 / 612 / 625 Treffer, L = 64: 573 / 550 / 545, je 1024 Paare.
  Binomialbreite ~ 16, die Bloecke sind also vertraeglich.
- **Eingefrorenes:** sha256sum -c EINGEFROREN-SHA256.txt lokal und auf der .69: 8 von 8 OK (22:23 und 22:24).
  PRUEFSUMMEN.txt der 15 Laufdateien ist auf beiden Seiten gleich.
- **Laufzeit:** fd2a 241 s, fd2b 205 s, fd2c 249 s, fd2d 243 s. Plan: hoechstens ~ 11 min je Spur, erwartet 7 bis
  9 min; tatsaechlich 7,4 und 8,2 min.
- **Vergleich mit FADEN-DIM-1 bei gleichem L [D]:** Dort betrug die Knickdichte 0,56 / 0,57 / 0,58 und P war 0,810 /
  0,760 / 0,672 (L = 16 / 24 / 32). Hier, bei 0,60: 0,840 / 0,747 / 0,694.

## 6. Ableitbarkeit und Urteil zur Kapazitaets-Skizze

- **Skizze (Pruefung im Plan, Abschnitt 1a) [M, L]:**
  - Sie **stimmt** in Richtung und asymptotischen Exponenten. Raten-Exponent bei D = 4 -1/2, bei D = 5 -1 mit
    log-Korrektur, bei D = 6 -2; glatt L^(3-D). Die Grenze 3 bleibt asymptotisch.
  - Voraussetzung: Die Form der Faeden ist auf grossen Skalen waehrend eines Vorbeigangs eingefroren.
    Rouse-Skalenargument: Relaxation auf Skala r dauert ~ r^4/rho^2, die Durchquerung ~ r^2.
  - Zwei Ungenauigkeiten: "P ~ T cap/L^d" gilt fuer die Rate -ln(1 - P), fuer P nur ohne Saettigung. Die Ordnungen der
    Spurkapazitaet stimmen, die Zuschreibung allein an Lawler ist ungenau (d = 3 und 4: Asselah/Schapira/Sousi;
    d >= 5: Jain/Orey [L]).
- **Gegen die Rechnung [D]:**
  - Die Richtung stimmt: rau -0,61 gegen glatt -1,10 bei D = 4, und D = 4 faellt weiter.
  - Den Zahlenwert bei L <= 64 trifft die Skizze nicht genau: -0,61 [-0,65; -0,57] statt -0,5.
  - Die Abweichung geht in die steilere Richtung. Die Spurkapazitaet kurzer Wege allein sagt die flachere voraus
    (effektiv zwischen n^(1/2) und n, also Exponent zwischen -1/2 und 0) [M]. Bei kleinem L wirkt also etwas, das
    die Skizze nicht enthaelt [H]. Kandidaten: T = 4 L^2 ist nur wenige Mischzeiten lang, und Treffen durch lokale Zuege.
  - Die lokalen Exponenten (-0,71 / -0,52 / -0,61 / -0,58) haben Fehlerbalken von ~ 0,15 bis 0,24. Ob sie gegen -1/2
    laufen, ist mit L <= 64 nicht entschieden.
  - D = 5: -1,30 [-1,38; -1,22]. Das passt zur log-korrigierten Form der Skizze: Mit n = 1,2 L = 10 bis 29 gibt
    n/ln n effektiv etwa -1,3 bis -1,4 [M nach Sicht].
- **Kopplung FD1/FD2 (Plan 1a) [M nach Sicht]:** Mit dem gemessenen P(32) = 0,694 verlangt FD2 einen lokalen
  Raten-Exponenten zwischen L = 32 und 64 unter etwa -0,43. Gemessen ist er -0,597 (Rate 1,184 auf 0,783). Die
  Umrechnung ist eine Identitaet, kein zweiter Befund: FD2 folgt hier aus dem Raten-Abfall und der Saettigung bei
  L = 32. FD2 ist also nicht unabhaengig von FD1.
- **Rohdaten FADEN-DIM-1 (Plan 1b):** Sie beantworteten die Frage nicht. Es gab kein L > 32 bei D = 4, keine Zelle
  im Rauheitsband 0,59 bis 0,61 und keine Knickzahl je Paar.
- **FD0** war vorab ableitbar (Plan 1c) und ist nur Codekontrolle, keine Messung.
- **Meine Erwartung vor der Rechnung (Plan 1a) [H]:** Raten-Exponent -0,5 bis -0,65, Steigung 32 bis 64 etwa -0,3.
  Gemessen: -0,61 und -0,35.

## 7. Selbstanzeigen

1. **Startbefehl:** Beim ersten ssh-Start galt das "&" fuer die ganze &&-Kette. Der Kalibrierlauf lief wie gewollt.
   Der Rauchtest startete nicht (cd in einen noch nicht angelegten Ordner) und lief 25 s spaeter. Ohne Wirkung auf
   die Ergebnisse.
2. **Scratchpad-Pfad:** Die Werkzeugumgebung legte die Ausgabe meines Hintergrund-Wartebefehls und des Monitors unter
   /tmp/claude-1000/.../tasks/ ab. Ich habe dort nichts selbst geschrieben. Der Inhalt sind nur Start-, Ende- und
   rc-Zeilen der Kette, keine Treffzahlen. Der Pfad liegt aber im ausgeschlossenen Bereich.
3. **Kalibrier-Toleranz:** Die Dynamikprobe D = 5, L = 12 lag ausserhalb +-0,01 (0,615). Ich habe sie vor dem
   Einfrieren als Zufall gewertet (2,4 Fehlerbreiten), ohne Nachlauf. Der Lauf bestaetigt das (Abschnitt 5).
4. **"kopieren, dort nichts aendern":** Ich habe "dort" als faden.py gelesen. faden.py ist bytegleich kopiert, alles
   Neue steht in fd2.py, das nur Funktionen aus faden.py aufruft.
5. **Lesarten:** Die Urteilsregeln sind meine Festlegungen vor der Rechnung. Das sind die dreiwertige FD1-Regel mit
   Bootstrap-Intervall, die Zwei-Punkt-Steigung als Kartenwortlaut fuer FD2 und Wilson-Grenzen fuer FD0. Hier
   entscheiden sie nichts.
6. **Vorwissen:** FADEN-DIM-1 (auch P(32) ~ 0,67) kannte ich vor dem Plan. Im Plan diente es nur der Abschaetzung
   der Kopplung. Bei der Rohdatenprobe habe ich ueber jq 'keys' hinaus auch p_start, kappa und laufzeit_s der
   D = 4/5-Zellen gelesen (nur lesen, keine Treffzahlen neu gerechnet).
7. **Tempo:** Den Plan habe ich in knapp 2 min geschrieben und ohne Gegenleser eingefroren. Die Pruefung der Skizze
   [M] ist nicht gegengelesen. Die Literatur [L] stammt aus dem Gedaechtnis, ohne Abruf; Jahreszahlen und
   Zuschreibungen koennen falsch sein.
8. **Nach Sicht:** Die Abschnitte 1.4, 5 (Vergleiche, Bloecke) und 6 (Gegen die Rechnung, D = 5, Kopplung) sind
   Diagnose [D] bzw. Handrechnung [M nach Sicht] und nicht Teil der Urteile.
9. Ein foreground-"sleep 45" wurde von der Werkzeugumgebung blockiert. Ohne Wirkung.

## 8. Einfach gesagt

Wir haben wieder zwei geschlossene Faeden in einem Kasten mit vier Raumrichtungen herumwandern lassen, diesmal in
jedem Kasten gleich wackelig, und gezaehlt, wie oft sie sich treffen. Wackelige Faeden treffen sich viel
oefter als glatte, aber je groesser der Kasten, desto seltener: von 84 von 100 Paaren bei Kantenlaenge 16 auf 54
von 100 bei Kantenlaenge 64. Die Trefferrate faellt dabei etwa halb so schnell wie bei glatten Faeden. Auch raue
Faeden finden sich also nur bis drei Raumrichtungen zuverlaessig; die "Grenze 4" aus dem ersten Versuch lag nach
unserer Deutung an den kleinen Kaesten und der dort mitwachsenden Rauheit. Alles ist Computersimulation, keine Messung.

## 9. Dateien

- KARTE.md (Leitung), PLAN.md, PLAN.md.eingefroren-20261004-221356, EINGEFROREN-SHA256.txt.
- code/faden.py (bytegleich FADEN-DIM-1), code/fd2.py, code/kette.sh und je .eingefroren-20261004-221356.
- kalib-69/: kalib.log (nur Knickdichte und kappa), rauch.log (nur Laufzeiten).
- lauf-69/: fd2a bis fd2d (.jsonl Rohdaten mit allen Treffzeiten, .log), kette-cpu(10).log, auswertung.json/.txt/
  .log, bild.log, faden-dim-2.png, PRUEFSUMMEN.txt. .69: /home/fmh/fmhc-physics-remote/faden-dim-2/.
- BILD-faden-dim-2.png.
