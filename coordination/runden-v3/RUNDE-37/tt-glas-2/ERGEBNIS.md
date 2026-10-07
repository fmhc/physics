# TT-GLAS-2: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 46, Zweig Glas)

> **Berichtigung der Leitung nach GEGENLESEN-R47 (A2; 2026-10-05, gegenlesen-r47/GEGENLESEN.md):** "in der ganzen Brillouin-Zone stabil" (Ergebnis zuerst 1) ist zu stark. Gerechnet und stabil sind die 112 k-Klassen des 6^3-Gitters der Superzelle in allen 24 Netzen. Ausserdem (B3): "sogar etwas steiler" haelt nicht; mit dem Nachtrag liegt -0,47 im Vertrauensbereich. Der Text unten bleibt unveraendert (Sicherung .bak-*).

- Alle Zahlen sind synthetische Gitterrechnungen auf der .69 (Python 3.12.3, numpy 2.4.4, scipy 1.18.0,
  torch 2.5.1+cu121; Quadro P4000 mit complex128 bzw. 1 CPU-Kern), keine Messdaten.
- **Kennzeichen:** [E] hier gerechnet, [M] Mathematik (vorab ableitbar), [P] Projektdatei, [F] Festlegung im Plan,
  [H] Hypothese oder Lesart.
- **Begriffe:** Glas, Modell (R1, J = 1) und Spanne (max/min - 1 von omega^2/k^2 ueber 13 Richtungen x 2 TT-Zweige,
  |k| = 1e-2) wie TT-GLAS-1. Doppelbrechungsanteil = groesste Aufspaltung der zwei Polarisationen / Spanne.
  P = physikalischer Raum (Komplement von Eichung M und Regel c). Varianten (PLAN Abschnitt 3): (a) voll; (b) affin
  eingefroren: Rayleigh-Ritz auf den auf P projizierten affinen TT-Wellen mit der Masse des R1-Modells; (c) isotrope
  Ersatzmasse A3 mit Reduktion R2; (d) Ritz von (c) auf denselben projizierten Wellen; (e) unprojiziert (vorab isotrop).

## 1. Zeiten und Laeufe

- **Ablauf (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 06:47:39 CEST. Plantext ab 07:18:41 CEST, vor jeder Hauptrechnung.
  - Rauchtests r1 bis r4 (05:06:44 bis 05:20:54 UTC; nur Schluessel und Laufzeiten, Rauchsaat 901, alle rc = 0):
    r1 cpu6 (bz N = 128; sz N = 256 und 512, duenn besetzt), r2 cpu6 (bz N = 128 und 256, dk N = 128 und 256),
    r3 p4000a und p4000b (bz N = 256, dk N = 256, 512, 1024), r4 cpu6 (bz N = 128 nach einer Speicher-Aenderung).
  - Eingefroren 07:21:04 CEST: PLAN.md.eingefroren-20261005-072104 (sha256 6642835e...), code/bz.py (f3c17fcc...),
    code/dk.py (747f4f03...), code/dz.py (ee6ba6b4...), code/kette-A/B/C.sh; tg.py, ew.py, tp.py unveraendert aus
    TT-GLAS-1 (ec48a258..., fa7b6417..., 419d7da6...). Gleiche Summen auf der .69 (EINGEFROREN-SHA256-69.txt).
  - code/tg2_auswertung.py: nach dem ersten Einfrieren geschrieben, Absturzproben r5 (05:24 bis 05:26 UTC) und r6
    (05:38 bis 05:40 UTC) auf Teildaten mit Lesen nur von Rueckgabewert und Schluesseln; eingefroren 07:40:09 CEST
    (8d2dcd8a...), vor Sicht jedes Ergebniswerts.
  - Laufketten A (p4000a), B (p4000b), C (cpu6) 05:21:17 bis 06:16:44 UTC; Nachholung N = 1024, Saaten 1 und 3,
    auf p4000b bis 06:26:14 UTC (Selbstanzeige 4); Nachtrag N = 512 (p4000a) 05:51:57 (Start mit Wartezeit auf den
    Lock) bis 06:13:21 UTC (Abschnitt 4.4).
  - Endauswertung 06:26:23 bis 06:26:26 UTC (cpu6, rc = 0): auswertung-69/ (auswertung.json, tabellen.md, tg2-bild.png).
    Pruefsummen auf der .69 erzeugt (PRUEFSUMMEN-lauf.txt, 102 Dateien; -auswertung, -nachtrag), lokal alle gleich.
  - Alle Ergebnisdateien tragen die eingefrorenen Summen (bz.py f3c17fcc..., dk.py 747f4f03..., dz.py ee6ba6b4...;
    Auswertung 8d2dcd8a...); Code auf der .69 und lokal nach den Laeufen gleich.
- **Aufrufe:** `bash kleintest.sh <Spur> <Name> code/<Skript> ...` im Ordner /home/fmh/fmhc-physics-remote/tt-glas-2;
  bz = `code/bz.py --N <N> --saat <s> --out lauf/bz-N<N>-s<s>.json` (6^3-Gitter, 112 Klassen);
  dk = `code/dk.py --N <N> --saaten <Liste> --out lauf/dk` (alle Varianten, mit Linearitaet); N = 1024:
  `--ridx 0-6` bzw. `--ridx 7-12`, jeweils `--varianten a --ohne_lin`.
- **Laeufe** (Ende in UTC; Laufzeit = Dienstlaufzeit aus dem kleintest-Log; alle unter 600 s):

| Lauf | Spur | Aufruf | Ende | Laufzeit | rc |
|---|---|---|---|---|---|
| tg2-bz128-s1 bis -s12 | cpu6 | bz N = 128, Saat 1 bis 12 (je ein Lauf) | 05:24:01 bis 05:55:16 | 150 bis 225 s | 0 (12 x) |
| tg2-bz256-s1 bis -s6 | p4000a | bz N = 256, Saat 1 bis 6 | 05:23:51 bis 05:37:59 | 154 bis 191 s | 0 (6 x) |
| tg2-bz256-s7 bis -s12 | p4000b | bz N = 256, Saat 7 bis 12 | 05:23:52 bis 05:37:32 | 154 bis 179 s | 0 (6 x) |
| tg2-dk256-B | p4000b | dk N = 256, Saaten 7 bis 12 | 05:40:26 | 174 s | 0 |
| tg2-dk256-A | p4000a | dk N = 256, Saaten 1 bis 6 | 05:41:15 | 196 s | 0 |
| tg2-dk512-B | p4000b | dk N = 512, Saaten 3, 4 | 05:46:39 | 373 s | 0 |
| tg2-dk512-A | p4000a | dk N = 512, Saaten 1, 2 | 05:48:36 | 441 s | 0 |
| tg2-dk1024-s1-r0 | p4000a | dk N = 1024, Saat 1, ridx 0-6 | 05:50:13 | 97 s | **1** (CUDA-Speicher) |
| tg2-dk1024-s1-r1 | p4000a | dk N = 1024, Saat 1, ridx 7-12 | 05:51:51 | 97 s | **1** (CUDA-Speicher) |
| tg2-dk1024-s2-r0 | p4000b | dk N = 1024, Saat 2, ridx 0-6 | 05:51:55 | 316 s | 0 |
| tg2-dk1024-s3-r0 | p4000a | dk N = 1024, Saat 3, ridx 0-6 | 05:53:24 | 93 s | **1** (CUDA-Speicher) |
| tg2-dk1024-s2-r1 | p4000b | dk N = 1024, Saat 2, ridx 7-12 | 05:56:27 | 272 s | 0 |
| tg2-dk128-a | cpu6 | dk N = 128, Saaten 1 bis 6 | 05:58:45 | 205 s | 0 |
| tg2-dk128-b | cpu6 | dk N = 128, Saaten 7 bis 12 | 06:01:54 | 189 s | 0 |
| tg2-dk1024-s1-r0-p4000b | p4000b | dk N = 1024, Saat 1, ridx 0-6 (Nachholung) | 06:02:25 | 357 s | 0 |
| tg2-dk1024-s3-r1 | p4000a | dk N = 1024, Saat 3, ridx 7-12 | 06:04:06 | 92 s | **1** (CUDA-Speicher) |
| tg2-dk1024-s4-r0 | p4000b | dk N = 1024, Saat 4, ridx 0-6 | 06:07:41 | 317 s | 0 |
| tg2-dk1024-s1-r1-p4000b | p4000b | dk N = 1024, Saat 1, ridx 7-12 (Nachholung) | 06:12:13 | 272 s | 0 |
| tg2-dk1024-s4-r1 | p4000b | dk N = 1024, Saat 4, ridx 7-12 | 06:16:44 | 271 s | 0 |
| tg2-dk1024-s3-r0-p4000b | p4000b | dk N = 1024, Saat 3, ridx 0-6 (Nachholung) | 06:21:52 | 308 s | 0 |
| tg2-dk1024-s3-r1-p4000b | p4000b | dk N = 1024, Saat 3, ridx 7-12 (Nachholung) | 06:26:14 | 262 s | 0 |
| tg2-nt512-a, -b (Nachtrag) | p4000a | dk N = 512, Saaten 5 bis 7 bzw. 8 bis 10 | 06:02:34, 06:13:21 | 550 s, 555 s | 0 |

- Einzelzeilen mit Start, Ende und Dauer einschliesslich Wartezeit auf den Spur-Lock: auswertung-69/tabellen.md.

## 2. Ergebnis zuerst

1. **Das Glas bleibt in der ganzen Brillouin-Zone stabil [E].** Auf allen 24 Netzen (N = 128 und 256, je 12 Saaten)
   ist das volle 6^3-Gitter gerechnet (112 Klassen je Netz, k und -k gleich [M]; 2 688 Klassenpunkte). Es gibt keine
   negative oder wachsende Mode. Nullmoden gibt es nur bei Gamma, dort in jedem Netz genau 6: die homogenen
   Verzerrungen des Torus, wie vorab abgeleitet [M]. Ausserhalb von Gamma ist die reduzierte Bewegungsmatrix ueberall
   positiv definit, und die reduzierte Steifigkeit hat keine negative Richtung. Das kleinste omega^2 liegt jeweils
   beim kleinsten Gitter-k (Schallzweig): 0,18 bis 0,21 (N = 128) bzw. 0,12 bis 0,13 (N = 256). TG2-1 trifft ein.
2. **Die Anisotropie sitzt in der Traegheit der affinen Welle, nicht in einer Relaxation [E].** Die langen TT-Wellen
   sind bis auf 1e-5 genau die auf P projizierten affinen Wellen: Der Rayleigh-Ritz-Wert (b) liegt nur 6,7e-6 bis
   1,0e-5 ueber (a), die Spannen sind gleich. Die Steifigkeit dieser Wellen ist isotrop (1 +- 1,7e-5). Die nichtaffine
   Relaxation traegt bei langen Wellen also nichts; das war mit Stoerungsrechnung erster Ordnung vorab ableitbar, stand
   aber nicht im Plan (Selbstanzeige 1). Mit der isotropen Ersatzmasse A3 faellt die Spanne auf 7,1 % (N = 128) bzw.
   5,7 % (N = 256), etwa die Haelfte von (a). Auch dieser Rest stammt nicht aus Relaxation ((c) = (d)), sondern aus der
   Projektion auf P (Eichvertreter); unprojiziert ist A3 exakt isotrop ((e): 0,00 %). TG2-2 ist verfehlt.
3. **Groessere Netze: Das N-Gesetz haelt, sogar etwas steiler [E].** Mit dichter Rechnung auf der GPU (der duenn
   besetzte Loeser war zu langsam): N = 512: 6,8 +- 1,5 % (4 Netze), N = 1024: 4,66 +- 0,28 % (4 Netze, 4,31 bis
   5,00 %). Erwartet waren nach der Karte etwa 5,9 % [M]. TG2-3 trifft ein. Exponent ueber N = 128 bis 1024: -0,56
   (95 %: -0,65 bis -0,48), mit TT-GLAS-1 N = 32 und 64: -0,52. Der Nachtrag mit 4 weiteren Netzen N = 512 gibt dort
   8,9 +- 1,3 % (zusammen 7,9 %) und einen Exponenten von -0,53; das aendert kein Urteil.
4. **Doppelbrechung bleibt der Hauptteil [E].** Der Doppelbrechungsanteil liegt im Mittel je N zwischen 0,84 und 0,88
   (N = 32 bis 1024; Nachtrag N = 512: 0,90). Aufspaltung der Polarisationen und Richtungsspanne der Zweigmittel fallen beide mit N (13,0 % auf
   4,1 % bzw. 5,6 % auf 1,75 % von N = 128 bis 1024).
5. **Kontrolle TG2-0 trifft ein [E]:** Die TT-GLAS-1-Werte bei kleinem k werden auf 1,9e-9 (624 Werte, dk) bzw.
   6,8e-10 (48 Werte, Kontrollpunkt der Zonenrechnung) reproduziert; N = 512, Saat 1, gegen den TT-GLAS-1-Nachtrag
   auf 1,2e-9.

## 3. Urteile

Mechanisch durch code/tg2_auswertung.py (eingefroren 07:40:09 CEST), auswertung-69/auswertung.json; Regeln PLAN Abschnitt 6.

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| TG2-0 | Kontrolle: TT-GLAS-1-Werte bei kleinem k (N = 128, 256) auf 1e-3 relativ | 90 % | **eingetroffen** | **eingetroffen** | groesste Abweichung 1,9e-9 (dk, 24 Netze x 26 Werte), 6,8e-10 (bz-Kontrollpunkt, 24 x 2) |
| TG2-1 | [H] keine negativen bzw. wachsenden Moden im ganzen k-Gitter (24 Netze) | 55 % | **eingetroffen** | **eingetroffen** | 24 von 24 Netzen vollstaendig (112 Klassen), 0 wachsende Moden; je Netz 6 Nullmoden bei Gamma, 0 sonst |
| TG2-2 | [H] Relaxation traegt mehr als die Haelfte (b kleiner als c) | 50 % | **verfehlt** | **verfehlt** | Spanne (b) / (c): 15,32 / 7,12 % (N = 128), 11,40 / 5,67 % (N = 256); zusammen 13,36 / 6,39 % |
| TG2-3 | [H] N = 1024: Spanne je Netz im Mittel unter 7 % | 60 % | **eingetroffen** | **eingetroffen** | 4,66 % (Saaten 1 bis 4: 4,31; 4,67; 5,00; 4,67 %) |

- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - TG2-1 trifft ein: "Das Glas ist auch bei kurzen Wellen stabil, eine Bedingung fuer den Glas-Zweig."
  - TG2-2: "Traegt die Relaxation die Spanne, liegt die Anisotropie in der Netzverformung (Geometrie); traegt die
    Bewegungsenergie, liegt sie in der Massenverteilung." Ausgeloest ist der zweite Fall: Die Bewegungsenergie traegt die
    Spanne. Einschraenkung: Ihr Wert haengt an der Projektion auf P, und diese Projektion haengt am Netz (Abschnitt 5).
  - TG2-3: Das N-Gesetz haelt (die Karte nannte dafuer keinen eigenen Satz).
- **Wichtige Lesehilfe zu TG2-2 [E, M]:** Die geplante Zerlegung ist entartet. (a) = (b) und (c) = (d) bis auf 1e-5,
  weil die langen TT-Wellen in erster Ordnung in k genau die projizierten affinen Wellen sind. Der Vergleich (b) gegen (c)
  misst deshalb nicht "Masse gegen Relaxation", sondern "Masse A1 gegen Masse A3 auf derselben projizierten Welle". Der
  Relaxationsanteil der Spanne ist nach (a) minus (b) hoechstens 1e-5 relativ, also praktisch null. Am Urteil "verfehlt"
  aendert das nichts: Die Relaxation traegt weniger als die Haelfte.
- **Agenten-Vorhersagen** (PLAN 8, kein Urteil): B1 (keine wachsende Mode, 65 %) eingetroffen. B2 ((b) kleiner als (c) bei
  beiden N, 40 %) verfehlt. B3 (N = 1024 zwischen 4 und 7 %, 60 %) eingetroffen (4,66 %). B4 (Doppelbrechungsanteil bei
  N = 1024 innerhalb +-0,1 des Werts bei N = 256, 55 %) eingetroffen (0,883 gegen 0,836).

## 4. Tabellen

Mechanisch aus auswertung-69/tabellen.md (Punkt als Dezimalzeichen).

### 4.1 Stabilitaet je Netz (Aufgabe 1; 112 k-Klassen je Netz, alle vollstaendig)

min omega^2 = kleinstes omega^2 ohne Nullmoden ausserhalb von Gamma; m = Gitterindex des Orts. A_red pd und
B_red ohne negative Richtung an allen Punkten ausser Gamma in allen 24 Netzen; bei Gamma hat A_red in allen 24 Netzen
genau eine negative Richtung; alle uebrigen omega^2 sind dort reell und positiv, die 6 Nullmoden liegen unter der
Nullschwelle 1e-9 s (|Im omega^2| <= 7,7e-14) [E]. Lesart: Die negative Richtung ist die globale Skalierung, ein
Nullmode von B [H].

| N | Saat | wachsend | Nullmoden bei Gamma / sonst | min omega^2 | bei m | min omega^2 / s | kleinstes omega^2 bei Gamma (ohne Null) | Geraet |
|---|---|---|---|---|---|---|---|---|
| 128 | 1 | 0 | 6 / 0 | 0.2008 | [1,0,0] | 2.8e-4 | 5.10 | CPU |
| 128 | 2 | 0 | 6 / 0 | 0.2004 | [0,1,0] | 1.2e-4 | 5.30 | CPU |
| 128 | 3 | 0 | 6 / 0 | 0.1841 | [1,0,0] | 3.1e-4 | 4.83 | CPU |
| 128 | 4 | 0 | 6 / 0 | 0.2005 | [0,1,0] | 3.4e-4 | 5.02 | CPU |
| 128 | 5 | 0 | 6 / 0 | 0.1991 | [0,1,0] | 9.3e-5 | 4.95 | CPU |
| 128 | 6 | 0 | 6 / 0 | 0.2030 | [0,0,1] | 3.7e-4 | 5.19 | CPU |
| 128 | 7 | 0 | 6 / 0 | 0.2055 | [0,1,0] | 4.6e-4 | 5.09 | CPU |
| 128 | 8 | 0 | 6 / 0 | 0.1920 | [0,1,0] | 5.2e-5 | 5.01 | CPU |
| 128 | 9 | 0 | 6 / 0 | 0.2015 | [0,0,1] | 3.9e-4 | 5.16 | CPU |
| 128 | 10 | 0 | 6 / 0 | 0.2128 | [0,0,1] | 9.3e-5 | 5.32 | CPU |
| 128 | 11 | 0 | 6 / 0 | 0.1978 | [0,0,1] | 5.0e-4 | 5.04 | CPU |
| 128 | 12 | 0 | 6 / 0 | 0.1886 | [0,0,1] | 1.9e-4 | 5.12 | CPU |
| 256 | 1 | 0 | 6 / 0 | 0.1282 | [0,0,1] | 1.8e-4 | 3.60 | GPU |
| 256 | 2 | 0 | 6 / 0 | 0.1305 | [0,0,1] | 1.5e-5 | 3.59 | GPU |
| 256 | 3 | 0 | 6 / 0 | 0.1288 | [1,0,0] | 6.5e-5 | 3.44 | GPU |
| 256 | 4 | 0 | 6 / 0 | 0.1260 | [0,0,1] | 8.9e-5 | 3.65 | GPU |
| 256 | 5 | 0 | 6 / 0 | 0.1231 | [1,0,0] | 7.6e-5 | 3.55 | GPU |
| 256 | 6 | 0 | 6 / 0 | 0.1272 | [0,1,0] | 9.2e-5 | 3.52 | GPU |
| 256 | 7 | 0 | 6 / 0 | 0.1272 | [0,1,0] | 2.8e-5 | 3.58 | GPU |
| 256 | 8 | 0 | 6 / 0 | 0.1239 | [0,1,0] | 6.7e-5 | 3.51 | GPU |
| 256 | 9 | 0 | 6 / 0 | 0.1244 | [0,1,0] | 1.1e-4 | 3.55 | GPU |
| 256 | 10 | 0 | 6 / 0 | 0.1237 | [0,1,0] | 1.8e-4 | 3.57 | GPU |
| 256 | 11 | 0 | 6 / 0 | 0.1258 | [0,0,1] | 1.3e-4 | 3.52 | GPU |
| 256 | 12 | 0 | 6 / 0 | 0.1313 | [0,0,1] | 3.0e-4 | 3.69 | GPU |

- Das kleinste Gitter-|k| ist 2 pi / (6 L): 0,208 (N = 128), 0,165 (N = 256). Mit omega^2/k^2 ~ 4,9 erwartet man dort
  0,21 bzw. 0,13 [Kopfrechnung]; die Minima liegen dort (Bild, Feld 1). s = groesstes |omega^2| (394 bis 8 720,
  Splitter).

### 4.2 Zerlegung (Aufgabe 2; Spannen in Prozent, Mittel +- SD ueber die Netze)

| N | Netze | (a) voll | (b) affin, nur Masse | (c) Ersatzmasse A3 | (d) Kontrolle zu (c) | (e) unprojiziert | Anteil c/(b+c) |
|---|---|---|---|---|---|---|---|
| 128 | 12 | 15.32 +- 3.77 | 15.32 +- 3.77 | 7.12 +- 1.37 | 7.12 +- 1.37 | 0.00 | 0.32 +- 0.06 |
| 256 | 12 | 11.40 +- 1.93 | 11.40 +- 1.93 | 5.67 +- 1.45 | 5.67 +- 1.45 | 0.00 | 0.33 +- 0.08 |
| 512 | 4 | 6.84 +- 1.54 | 6.84 +- 1.54 | 5.41 +- 2.74 | 5.41 +- 2.74 | 0.00 | 0.43 +- 0.12 |

- **Je Netz** (N = 128: (a)/(c) in %): 10.93/8.19, 11.38/7.18, 23.70/8.01, 12.46/8.54, 13.66/6.80, 18.50/6.92,
  12.06/5.41, 14.98/6.80, 18.67/6.78, 15.30/9.05, 18.02/7.63, 14.18/4.07 (Saaten 1 bis 12). N = 256: 12.31/5.23,
  10.67/5.98, 11.91/3.46, 11.89/4.10, 9.57/6.82, 12.31/6.39, 6.91/7.72, 12.84/6.09, 11.54/5.09, 12.29/7.19,
  14.56/6.65, 9.99/3.33. N = 512: 7.20/9.44, 8.86/3.36, 5.84/4.25, 5.45/4.60. In 2 von 28 Netzen (N = 256, Saat 7;
  N = 512, Saat 1) ist (c) groesser als (a). (b) = (a) und (d) = (c) in jedem Netz auf die angegebenen Stellen.
- **Pruefgroessen [E]:** Ritz (b) minus (a) relativ 6,7e-6 bis 1,04e-5, nie negativ (Cauchy [M]); Steifigkeit der
  projizierten affinen Welle z^+ B z / (k^2 V) = 0,999997 bis 1,0000166, unprojiziert 0,999995 bis 1,000013 (Z1 von
  TT-GLAS-1 auf 28 Netzen bestaetigt); Projektionsanteil |a_h - Pi a_h| / |a_h| = 0,40 bis 0,53 je Welle;
  (e) Spanne <= 2,9e-5 (unter 0,003 %) in allen 28 Netzen [M bestaetigt].
- **Ersatzmodell (c) ist auf manchen Netzen instabil [E]:** K3_red ist indefinit (1 bis 2 negative Richtungen) in 2 von
  12 Netzen N = 128, 4 von 12 N = 256 und 4 von 4 N = 512; dort hat (c) 1 bis 2 negative omega^2 (-0,35 bis -15,7,
  weit weg von den TT-Werten ~1e-5). Die zwei TT-Werte findet (c) in allen Netzen (gueltig nach Plan). (c) taugt damit
  als Messgeraet fuer die Spanne, nicht als stabiles Modell.
- Linearitaet von (a) zwischen |k| = 1e-2 und 2e-2: <= 6,3e-5; kleinste Luecke (a): 4,82 (N = 128), 3,42 (256),
  2,39 (512), 1,62 (1024).

### 4.3 Spanne (a) gegen N mit Doppelbrechungsanteil (Mittel +- SD)

| N | Netze | Spanne % | Aufspaltung max % | Richtungsspanne der Zweigmittel % | Doppelbrechungsanteil | Quelle |
|---|---|---|---|---|---|---|
| 32 | 12 | 29.7 +- 4.5 | 25.8 +- 3.9 | 9.2 +- 4.5 | 0.873 +- 0.108 | TT-GLAS-1 [P] |
| 64 | 12 | 22.9 +- 5.7 | 20.1 +- 6.2 | 7.0 +- 1.8 | 0.873 +- 0.100 | TT-GLAS-1 [P] |
| 128 | 12 | 15.32 +- 3.77 | 12.98 +- 3.27 | 5.60 +- 2.00 | 0.850 +- 0.08 | hier |
| 256 | 12 | 11.40 +- 1.93 | 9.63 +- 2.52 | 3.85 +- 0.93 | 0.836 +- 0.12 | hier |
| 512 | 4 | 6.84 +- 1.54 | 6.05 +- 1.76 | 2.27 +- 0.26 | 0.876 +- 0.066 | hier |
| 512 | 4 (Nachtrag) | 8.92 +- 1.27 | 7.98 +- 1.01 | 2.52 +- 0.62 | 0.898 +- 0.077 | Nachtrag, beschreibend |
| 1024 | 4 | 4.66 +- 0.28 | 4.12 +- 0.47 | 1.75 +- 0.55 | 0.883 +- 0.05 | hier |

- N = 1024 je Saat (1 bis 4): Spanne 4.31 / 4.67 / 5.00 / 4.67 %, Doppelbrechungsanteil 0.85 / 0.89 / 0.95 / 0.85.
  Alle vier regulaer (2 masselose Moden an allen 13 Richtungen, nichts waechst, Luecke >= 1,62; ohne Linearitaet).
- **Exponent [E]:** Gerade ln(Spanne) gegen ln N ueber 32 Netze (N = 128 bis 1024): p = -0,564, Bootstrap-95 %:
  -0,648 bis -0,484. Mit TT-GLAS-1 (N = 32, 64; 56 Netze): -0,522. Beschreibend mit Nachtrag (8 Netze N = 512):
  -0,533 (-0,614 bis -0,452). Die Plan-Gerade gibt bei N = 1024 4,80 %.
- **Hochrechnung [Kopfrechnung, keine Messung]:** Gerade dieses Laufs: 1,5 % bei N = 8 000; unter 1 % ab N ~ 1,7e4
  (mit Nachtrag-Gerade ~2,2e4).

### 4.4 Nachtrag (nach Sicht der Zwischenergebnisse, beschreibend, kein Urteil)

- N = 512, Saaten 5 bis 10 auf p4000a (code/nachtrag-A2.sh, eingefrorener dk.py), weil p4000a fuer N = 1024 zu wenig
  Speicher hatte. Vollstaendig: Saaten 5, 6, 8, 9 (Spanne 9.05 / 8.92 / 7.30 / 10.41 %); Saaten 7 und 10 von der Frist
  abgeschnitten (6 bzw. 10 Richtungen) und nicht verwendet. Auch hier (a) = (b), (c) = (d), (e) = 0,00 %.
  Auswertung: nachtrag-69/auswertung/ und nachtrag-69/kombi-aus/ (zusammen mit lauf/).
- Vorbereitet, aber nicht gestartet: code/nachtrag-A.sh und -B.sh (N = 1024, Saaten 5 bis 8); die Zeit reichte nicht.

## 5. Bedeutung fuer Finns Glas-Zweig [H]

- **Stabilitaet:** Das periodische Zufallsnetz hat in diesem Modell (Hamilton-Netz, J = 1, R1) an allen 112
  Gitterklassen der Zone keine wachsende Mode, auch bei kurzen Wellen. Die Bedingung der Karte fuer den Glas-Zweig ist
  damit auf diesen 24 Netzen erfuellt. Geprueft sind nur die mit der Superzelle vertraeglichen k (6^3-Gitter); zwischen den
  Gitterpunkten und fuer das nicht periodische Glas ist das eine Lesart.
- **Woher die Anisotropie kommt:** Nicht aus der Steifigkeit (affin isotrop) und nicht aus nichtaffiner Relaxation
  (traegt bei langen Wellen nichts). Sie sitzt in der Bewegungsenergie, ausgewertet auf der affinen Welle in ihrer
  eichfixierten Form (Projektion auf P). Etwa die Haelfte bleibt sogar mit einer affin isotropen Masse, weil die
  Euklidische Projektion selbst vom Zufallsnetz abhaengt. Die Bewegungsenergie haengt vom Eichvertreter ab
  (Spur-Eichdefekt aus TT-ISO-1 und EINE-WELT-LOCH-1 [P]).
- **Naechster Hebel:** eine Bewegungsenergie, die nicht vom Eichvertreter abhaengt bzw. mit der Eichung vertraeglich ist
  (etwa die Spur-Varianten aus HODGE-L, Christiansen/Lin [P]). Sie wuerde den Projektionsanteil entfernen. Wie viel dann
  von der Spanne bleibt, ist nicht gerechnet.
- **Groesse:** Die Spanne je Probe faellt wie ~N^-0,55 (4,7 % bei N = 1024). Zufallsnetze werden ohne Abstimmung immer
  isotroper; fuer 1 % braeuchte eine Probe ~2e4 Punkte. Die Doppelbrechung bleibt dabei der Hauptteil (~85 %).
- Keine Messdaten, keine Aussage ueber nichtlineare oder Quanten-Effekte.

## 6. Selbstanzeigen

1. **Zerlegung vorab nicht als entartet erkannt:** Dass (a) = (b) und (c) = (d) in erster Ordnung in k gilt, folgt aus
   Stoerungsrechnung (die zwei kleinsten Eigenwerte von B_red sind O(k^2), die projizierten affinen Wellen liegen bis
   O(k^2) in ihrem Eigenraum). Meine Ableitbarkeitsprobe hat das nicht gesehen. Die Plan-Definition von (b) ist damit keine
   "nur Bewegungsenergie"-Grenze, sondern faellt mit (a) zusammen; TG2-2 vergleicht zwei Massen auf derselben Welle.
2. **Abweichung von der Karte: kein duennbesetzter Loeser.** Vor den Hauptlaeufen im Plan begruendet (Rauchtest r1:
   KKT-Faktorisierung fast dicht, 8 s bzw. 50 s je Matrix). Stattdessen dicht auf der GPU. code/sz.py ist Rauchcode.
3. **Ersatzmasse (c) ist eine Festlegung:** A3 mit R2 aendert Masse und Reduktion zugleich und ist auf 10 von 28
   Netzen instabil (negative omega^2). Ihre Spanne ist deshalb nur ein Vergleichswert.
4. **Nachholung N = 1024:** Die geplanten Laeufe fuer Saaten 1 und 3 auf p4000a brachen mit CUDA-Speichermangel ab
   (4 Laeufe, rc = 1; p4000a hatte wegen fremder Dienste ~0,3 GB weniger frei als p4000b). Ich habe sie mit demselben
   eingefrorenen Code und denselben Argumenten auf p4000b nachgeholt (code/nachhol-B.sh). Inhaltlich keine Aenderung.
5. **scp an Ort und Stelle:** Vor Rauchtest r2 habe ich bz.py, dk.py, dz.py und rauch2.sh auf der .69 direkt per scp
   ueberschrieben (kein Lauf aktiv). Ab r3 nur noch neue Datei und mv.
6. **Schreiben ausserhalb des Ordners:** Durch einen falschen relativen Pfad landete EINGEFROREN-SHA256.txt um 07:21 kurz in
   RUNDE-37/ statt in tt-glas-2/; sofort verschoben (Inhalt unveraendert).
7. **Python auf der .69 ausserhalb von kleintest.sh:** einmal `python -c` zum Pruefen, ob torch.geqrf und torch.ormqr
   vorhanden sind (07:12, keine Rechnung). Dazu `flock -n` als Sofortprobe auf die Spur-Locks.
8. **Auswertung nach dem ersten Einfrieren geschrieben:** zweimal auf echten Teildaten angestossen (r5, r6), gelesen nur
   Rueckgabewert und Schluessel; eingefroren vor Sicht jedes Werts. Die Urteilsregeln standen im eingefrorenen Plan.
9. **Nachtrag nach Sicht:** N = 512, Saaten 5 bis 10, angelegt nach Sicht der Zwischenergebnisse (N = 128, 256, 512);
   beschreibend. Er zeigt, dass die 4 Plan-Netze N = 512 eher niedrig lagen (6,8 gegen 8,9 %).
10. **Nicht gerechnet:** TT-Anteil (regulaer heisst hier: Zaehlung, Klassen, Linearitaet); N = 1024 nur Variante (a) und
    ohne Linearitaet; Zonenstabilitaet nur auf dem Superzellen-Gitter, nur N = 128 und 256.
11. **Geraete:** Zonenrechnung N = 128 auf der CPU, N = 256 auf der GPU (beide torch, complex128). Die Kontrollpunkte
    beider Wege stimmen mit TT-GLAS-1 auf <= 6,8e-10.
12. **Bild:** In Feld 2 ueberdeckt die Legende teilweise die Beschriftung "7 % (TG2-3)"; das Skript war eingefroren.
13. **jq auf der .69** zum Auflisten von Einzelwerten benutzt; lokal kein python, awk oder perl. Die Mittelwerte von
    Nachtrag und Plan-Netzen zusammen (7,9 %) und die Hochrechnungen sind Kopfrechnung.
14. **Kein frischer Gegenleser** in der Zeitbox; das bleibt der Leitung.

## 7. Einfach gesagt

Wir haben Finns Zufallsnetz aus Tetraedern, das "Glas", am Computer mit Schwerewellen aller Wellenlaengen geprueft,
die in die Rechenzelle passen, und nirgends schaukelt sich etwas auf. Dass ein einzelnes Netz die Wellen je nach Richtung
verschieden schnell laufen laesst, liegt nicht daran, dass sich das Netz unter der Welle verbiegt, sondern daran, wie
die Bewegungsenergie im Netz verteilt ist. Selbst mit einer gleichmaessig verteilten Ersatz-Bewegungsenergie bleibt etwa
die Haelfte, und die stammt von der Art, wie man die unsichtbaren "Schein-Bewegungen" der Punkte herausrechnet. Mit mehr
Punkten wird das Netz gleichmaessiger: bei 1024 Punkten
unterscheiden sich die Quadrate der Geschwindigkeiten nur noch um knapp 5 %, bei 128 waren es 15 %. Der groesste Teil davon
ist, dass die zwei Schwingungsrichtungen der Welle verschieden schnell sind.

## 8. Dateien

- PLAN.md (+ .eingefroren-20261005-072104), EINGEFROREN-SHA256.txt, EINGEFROREN-SHA256-69.txt, KARTE.md.
- code/: bz.py (Zone), dk.py (kleine k, Varianten a bis e), dz.py (dichte Bausteine), tg2_auswertung.py (Urteile, Tabellen,
  Bild), kette-A/B/C.sh, nachhol-B.sh, nachtrag-A2.sh (gelaufen), nachtrag-A.sh, nachtrag-B.sh (nicht gelaufen),
  rauch1/2/3a/3b.sh, sz.py (Rauchcode); tg.py, ew.py, tp.py, tg_auswertung.py und die Nachtrag-Dateien von TT-GLAS-1
  unveraendert kopiert.
- lauf-69/: bz-N{128,256}-s{1..12}.json, dk-N{128,256}-s{1..12}.json, dk-N512-s{1..4}.json,
  dk-N1024-s{1..4}-r{0,1}.json, kleintest-Logs; PRUEFSUMMEN-lauf.txt.
- auswertung-69/: auswertung.json, tabellen.md, tg2-bild.png (Bild: Feld 1 kleinster Eigenwert ueber |k|, Feld 2 Spanne
  gegen N, Feld 3 Doppelbrechungsanteil gegen N; auf der .69 erzeugt).
- nachtrag-69/: dk-N512-s{5..10}.json, Logs, auswertung/, kombi-aus/. rauch-69/: r1 bis r6.
- kette-*.ausgabe.txt, nachhol-B.ausgabe.txt, nachtrag-A2.ausgabe.txt: Ausgaben der Laufketten.
- Auf der .69: /home/fmh/fmhc-physics-remote/tt-glas-2/ (code/, rauch/, lauf/, zwischen/, auswertung/, nachtrag/).

Abschluss der Datei 2026-10-05 08:32:43 CEST (date). Zeitbox 150 min ab 06:47:39 CEST (bis 09:17:39) eingehalten; kein Lauf mehr aktiv (letzter Lauf
endete 06:26:14 UTC). Journal, Peerbus und Commit uebernimmt die Leitung.
