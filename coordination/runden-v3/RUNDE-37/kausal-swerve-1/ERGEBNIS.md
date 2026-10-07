# KAUSAL-SWERVE-1: Ergebnis (Code-Agent fuer die Leitung, Runde 37, explorativ)

- Gerechnet auf der .69 ueber kleintest.sh, nur Spuren cpu3 und cpu4, hoechstens zwei Laeufe zugleich.
- **Ablauf** (Zeiten per date; .69 in UTC, CEST = UTC + 2):
  - Start 04:35:13 CEST. Plan ab 04:52:02 CEST.
  - Rauch 1: 02:54:00 bis 02:54:06 UTC. Spiegelprobe und Rauch 2: 02:56:43 bis 02:56:59 UTC.
  - Eingefroren 04:58:21 CEST:
    - PLAN.md.eingefroren-20261004-045821
    - code/*.eingefroren-20261004-045821
    - sha256 in code/pruefsummen-einfrieren.txt
  - Hauptlaeufe 02:58:35 bis 03:03:58 UTC: 16 Laeufe, alle rc = 0, Status "fertig".
  - Auswertung 03:04:04 bis 03:04:09 UTC. Text ab 05:05:50 CEST.
- **Hashes:**
  - Alle Laeufe tragen die sha256 des eingefrorenen swerve.py (f13f6334...), die Auswertung die von auswertung.py
    (ba4a5a28...).
  - Plan und Code nach dem Einfrieren unveraendert (sha256 um 05:05:50 CEST erneut geprueft).
- **Daten:**
  - lauf-69/: je Lauf .json (Kopf) und .npz (Laeuferdaten), dazu Logs
  - lauf-69/auswertung.json: Urteile, Gegenproben, Beschreibung
  - Bilder lauf-69/: drift_n.png, var_n.png, cosh_n.png, kontrollen.png
  - rauch-69/: Rauchlaeufe
- Kennzeichen:
  - [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese
  - [E] hier gerechnet (synthetisch, keine Messdatenbestaetigung), [S] Schreibtisch des Code-Agenten vor jeder Rechnung

## 1. Ergebnis

1. **Im Inneren bremst das Netz nicht [E].**
   - Schritte, die bulk-exakt sind (also auch ohne Rand dieselben waeren), N = 64 000, 469 605 Schritte:
     - mittlere Aenderung der Rapiditaet +0,0004 +- 0,0007
     - Steigung gegen die Rapiditaet vor dem Schritt -0,0005 +- 0,0005 (Reibung hiesse deutlich negativ)
     - In allen 16 Klassen von eta = -4 bis 4 liegt die mittlere Aenderung innerhalb 2,4 SE bei 0.
   - Die eingefrorenen Laeufer (alle 4000 je eta_0, ohne Auslese) haben bei n = 50: <eta_50 - eta_0> = +0,03 / +0,03 /
     0,00 (+- 0,04) fuer eta_0 = -1 / 0 / 1.
2. **Die Rapiditaet zittert, gleich stark in jedem Bezugssystem [E, M].**
   - Streuung je Schritt sigma^2 = 0,246 bis 0,252 in jeder Klasse mit abs(eta) < 1,5. Vorab berechnet [S, M]: genau 1/4.
   - Ohne Rand (Kontrolle mit unbegrenzter Streuung):
     - sigma^2 = 0,2491 (300 000 Schritte)
     - Var(eta_n - eta_0) = 12,5 bis 13,3 bei n = 50 und 25,0 bis 25,2 bei n = 100 (n/4: 12,5 und 25)
3. **Nur der Rand des Diamanten bremst scheinbar [E].**
   - Nach dem Randkontakt ziehen die Schritte zur Rapiditaet 0 des Diamanten. Steigung -0,071 +- 0,001, bis +-0,30 je
     Schritt bei abs(eta) ~ 3,75.
   - Unter der Hauptregel (nur Laeufer, die n Schritte sicher im Inneren bleiben) sind bei n = 50 noch 27 bis 31 % uebrig,
     und zwar die mit kleiner Rapiditaet.
   - Fuer sie gilt <eta_50 - eta_0> = +1,04 / -0,02 / -1,07: Die Startrapiditaet ist "vergessen". Die Varianz saettigt
     bei ~2,4 statt n/4 zu wachsen.
4. **Das Netz heizt [M, E].**
   - Ohne Rand waechst <cosh eta_n> wie 1,1378^n [M]. Die Stichprobe gibt bei n = 50 895 +- 416 (Schreibtisch 636); der
     Median steigt von 1,28 (n = 5) auf 5,9.
   - Unter der Hauptregel steigt <cosh eta_n> nur von 1,89 auf 2,92, weil der Rand die schnellen Laeufer abschneidet.
5. **Urteile:**
   - KS0 eingetroffen (berichtigt; nach Kartenwortlaut nicht eingetroffen)
   - KS1 nicht eingetroffen
   - KS2 nicht eingetroffen
   - KS3 eingetroffen
   - KS1 und KS2 scheitern am Rand, nicht am Netz:
     - Ohne Auslese (eingefroren) trifft KS1 ein.
     - Ohne Rand (unbegrenzte Streuung) treffen KS1 und KS2 ein.

## 2. Urteile

Mechanisch nach PLAN.md (eingefroren 04:58:21 CEST) durch code/auswertung.py; Werte in lauf-69/auswertung.json.
Hauptregel: N = 64 000, Laeufer zaehlen bis zu ihrem ersten nicht bulk-exakten Schritt (PLAN Abschnitt 4).

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Werte |
|---|---|---|---|---|
| KS0 | Zukunftslinks je Punkt = ln N - 1,42 +- 0,15 bei N = 64 000 | 85 % | **eingetroffen** (berichtigt: alle Punkte) | alle Punkte 9,6465 (Saaten 9,647 / 9,630 / 9,663) gegen 9,6466; Abweichung -0,0001. **Kartenwortlaut** (Zentrum, 7530 Punkte): 10,267 +- 0,034, Abweichung +0,620: **nicht eingetroffen** |
| KS1 | abs(<eta_50 - eta_0>) <= 3 SE fuer eta_0 = -1, 0, 1 | 75 % | **nicht eingetroffen** | +1,038 +- 0,046 (22,7 SE) / -0,024 +- 0,044 (-0,6 SE) / -1,067 +- 0,045 (-23,5 SE); im Inneren bei n = 50: 1129 / 1235 / 1096 von je 4000 |
| KS2 | Var linear in n (R^2 > 0,98, n = 5 bis 50), Steigungen gleich innerhalb 15 % | 55 % | **nicht eingetroffen** | Steigung 0,0124 / 0,0103 / 0,0131; R^2 0,26 / 0,20 / 0,29; max/min 1,27; Var bei n = 5: 1,17 / 1,25 / 1,22, bei n = 50: 2,36 / 2,36 / 2,26 |
| KS3 | eta_0 = 0: <cosh eta_50> > <cosh eta_5> ueber 3 SE | 65 % | **eingetroffen** | 1,889 +- 0,030 -> 2,917 +- 0,087; Differenz 1,03 +- 0,09 (11,1 SE) |

- **Kartenfehler KS0** (PLAN Abschnitt 1.1, vor jeder Rechnung offengelegt):
  - ln N - 1,42 ist das Mittel ueber alle Punkte (L/N). Ein Punkt bei (u, v) hat im Mittel H_(N-1) + ln((1-u)(1-v))
    Zukunftslinks [M].
  - Fuer das Zentrum gibt das 10,245; gemessen 10,267 +- 0,034. Die Ortsformel stimmt also, nur der Kartenwert gehoert
    zum Mittel ueber den ganzen Diamanten.
- **Bedeutung nach der Karte (vorab):**
  - "KS1 bis KS3 treffen ein" ist nicht ausgeloest.
  - Ausgeloest ist der Zweig "KS2 verfehlt: Die Laeuferregel selbst zeichnet etwas aus (z. B. der Rand des Diamanten)".
  - Genau das ist hier der Fall. Die Schritte selbst haengen nicht von eta ab (Abschnitt 3.3); der Rand zeichnet das
    Ruhesystem des Diamanten aus.
- **Meine Vorab-Erwartung** (PLAN Abschnitt 3, vor jeder Rechnung): KS0 berichtigt ein, KS1 nicht, KS2 nicht, KS3 ein. So
  ist es gekommen (Selbstanzeige 2).

## 3. Tabellen

### 3.1 Hauptregel, N = 64 000 (4000 Laeufer je eta_0)

| eta_0 | n | im Inneren | <eta_n - eta_0> | Var | <cosh eta_n> | Median cosh |
|---|---|---|---|---|---|---|
| -1 | 5 | 3972 | -0,001 +- 0,017 | 1,17 | 2,75 | 1,66 |
| -1 | 20 | 2903 | +0,635 +- 0,029 | 2,61 | 3,34 | 1,89 |
| -1 | 50 | 1129 | +1,038 +- 0,045 | 2,36 | 2,87 | 1,77 |
| -1 | 100 | 151 | +1,103 +- 0,105 | 1,67 | 2,20 | 1,46 |
| 0 | 5 | 3996 | +0,037 +- 0,017 | 1,25 | 1,89 | 1,28 |
| 0 | 20 | 3196 | -0,032 +- 0,029 | 2,69 | 3,28 | 1,85 |
| 0 | 50 | 1235 | -0,024 +- 0,043 | 2,36 | 2,92 | 1,69 |
| 0 | 100 | 190 | +0,121 +- 0,100 | 1,93 | 2,42 | 1,59 |
| +1 | 5 | 3975 | -0,022 +- 0,017 | 1,22 | 2,73 | 1,66 |
| +1 | 20 | 2873 | -0,608 +- 0,029 | 2,56 | 3,29 | 1,87 |
| +1 | 50 | 1096 | -1,066 +- 0,045 | 2,26 | 2,82 | 1,64 |
| +1 | 100 | 155 | -1,090 +- 0,112 | 1,96 | 2,46 | 1,61 |

- Bei n = 5 sind noch > 99 % im Inneren; Var = 1,17 bis 1,25 entspricht n/4 = 1,25.
- Die Drift fuer eta_0 = +-1 beginnt um n = 10 (+0,19 / -0,16), wenn die ersten Laeufer ausscheiden.

### 3.2 Gegenproben bei n = 50 (gleiche Regeln, ohne Urteilskraft)

| Population | <eta_50 - eta_0> (eta_0 = -1 / 0 / 1) | KS1 | Var bei 50 | KS2 (Steigungen; R^2; max/min) | KS3 |
|---|---|---|---|---|---|
| Hauptregel N = 64 000 (Urteil) | +1,04 / -0,02 / -1,07 (+- 0,045) | nein | 2,36 / 2,36 / 2,26 | nein (0,012 / 0,010 / 0,013; <= 0,29; 1,27) | ja |
| eingefroren N = 64 000 | +0,028 / +0,031 / +0,001 (+- 0,045) | ja | 7,53 / 8,32 / 7,46 | nein (0,137 / 0,156 / 0,138; 0,96 bis 0,97; 1,14) | ja |
| bis zum Rand N = 64 000 | +1,14 / +0,02 / -1,17 (+- 0,04) | nein | 3,99 / 4,13 / 3,87 | nein (0,05; ~0,7; 1,10) | ja |
| Hauptregel N = 16 000 | +1,02 / -0,01 / -1,08 (+- 0,058) | nein | 1,42 / 1,54 / 1,34 | nein (Steigungen -0,002 / -0,007 / +0,0001) | ja (3,4 SE) |
| eingefroren N = 16 000 | -0,067 / +0,043 / +0,007 (+- 0,037) | ja | 5,2 / 6,1 / 5,3 | nein (R^2 0,91 bis 0,93) | ja |
| unbegrenzte Streuung | -0,17 / +0,14 / +0,21 (+- 0,11) | ja | 13,3 / 12,5 / 13,0 | **ja** (0,268 / 0,250 / 0,267; >= 0,998; 1,07) | **nein** (2,1 SE) |

- **KS1 mit SE ueber die 4 Bloecke** (Hauptregel N = 64 000): +1,038 +- 0,010 / -0,022 +- 0,049 / -1,067 +- 0,065; Urteil
  gleich.
- **Unbegrenzte Streuung, KS3:** <cosh eta_50> = 895 +- 416 gegen 1,92 bei n = 5. Das scheitert an 3 SE, weil der
  Mittelwert von seltenen schnellen Laeufern lebt (Varianz ~ (16/9)^n/2, PLAN Abschnitt 3).
  - Bei eta_0 = +-1: 1499 +- 838 und 982 +- 368 (Schreibtisch cosh(1) 636 = 981).
  - Median von n = 5 nach n = 50: 1,28 -> 5,9; bis n = 100: 14,8.

### 3.3 Schritte nach Rapiditaet vor dem Schritt (N = 64 000, alle eta_0 zusammen)

| eta-Klasse | Schritte im Inneren | <Delta eta> | <Delta eta^2> | Schritte nach Randkontakt | <Delta eta> |
|---|---|---|---|---|---|
| [-4,0; -3,5) | 730 | +0,014 +- 0,008 | 0,044 | 8960 | +0,290 +- 0,011 |
| [-3,0; -2,5) | 13 387 | +0,009 +- 0,004 | 0,185 | 13 887 | +0,117 +- 0,009 |
| [-2,0; -1,5) | 34 054 | -0,003 +- 0,003 | 0,242 | 15 320 | +0,039 +- 0,008 |
| [-1,0; -0,5) | 56 741 | -0,003 +- 0,002 | 0,251 | 16 321 | +0,020 +- 0,008 |
| [0,0; 0,5) | 59 336 | -0,001 +- 0,002 | 0,250 | 15 919 | -0,015 +- 0,008 |
| [1,0; 1,5) | 48 028 | +0,003 +- 0,002 | 0,250 | 15 434 | -0,031 +- 0,008 |
| [2,0; 2,5) | 23 600 | -0,004 +- 0,003 | 0,223 | 15 049 | -0,070 +- 0,008 |
| [3,0; 3,5) | 5213 | -0,004 +- 0,005 | 0,110 | 12 844 | -0,170 +- 0,009 |
| [3,5; 4,0] | 747 | -0,005 +- 0,008 | 0,042 | 9276 | -0,295 +- 0,011 |

- Jede zweite Klasse gezeigt, alle 16 in auswertung.json. Bild: kontrollen.png, rechts.
- Im Inneren:
  - <Delta eta^2> = 0,246 bis 0,252 fuer abs(eta) < 1,5.
  - Weiter aussen ist es kleiner, weil dort nur kleine Schritte bulk-exakt bleiben (symmetrische Kappung, kein Drift).
- Nach dem Randkontakt: <Delta eta^2> ~ 1,0. Nahe dem Rand hat ein Punkt wenige Links und springt weit.

### 3.4 Anteil im Inneren (Hauptregel)

| N | eta_0 | n = 10 | n = 20 | n = 30 | n = 50 | n = 100 |
|---|---|---|---|---|---|---|
| 64 000 | -1 / 0 / 1 | 0,93 / 0,97 / 0,93 | 0,73 / 0,80 / 0,72 | 0,53 / 0,59 / 0,53 | 0,28 / 0,31 / 0,27 | 0,04 / 0,05 / 0,04 |
| 16 000 | -1 / 0 / 1 | 0,81 / 0,91 / 0,81 | 0,51 / 0,60 / 0,52 | 0,31 / 0,38 / 0,33 | 0,11 / 0,13 / 0,10 | 0,001 |

- Erster nicht bulk-exakter Schritt im Median: 34 (N = 64 000), 22 (N = 16 000).
- Ohne Randregel enden 10 516 von 12 000 Laeufern (N = 64 000) vor Schritt 100 ohne zulaessigen Link.

## 4. Kontrollen

- **Spiegelprobe** (N = 64 000, 20 Streuungen):
  - u <-> v und eta_0 -> -eta_0 geben eta -> -eta auf 8,9e-16.
  - Alle Kennzeichen und Schrittzahlen sind gleich (Rauch, N = 4000: 4,4e-16).
- **tau-Schnitt:**
  - 646 von 7 061 790 Links an besuchten Punkten (9,1e-5) entfallen; an 517 von 722 997 Punkten mindestens einer.
  - KS0-Laeufe: 6e-5 bis 1,2e-4 aller Links. Schreibtisch [M]: e^(-9) = 1,2e-4.
  - Der Schnitt wirkt also praktisch nicht (PLAN 1.2).
- **Linkzahl an besuchten Punkten** gegen die Ortsformel H_(N-1) + ln((1-u)(1-v)) (c N > 100):
  - -0,0047 +- 0,0037 (657 448 Punkte, N = 64 000)
  - +0,0023 +- 0,0040 (N = 16 000)
- **KS0 gegen den exakten Wert** (KAUSAL-1-Integral 9,6440): +0,0025.
  - Die leichte Unterschaetzung aus KAUSAL-1 (-0,016 bis -0,052) zeigt sich bei N = 64 000 nicht.
  - Im Rauch bei N = 4000 und 16 000 lag sie bei -0,065 bzw. -0,033 (je eine Saat).
- **Schreibtisch gegen unbegrenzte Streuung** (300 000 Schritte):

  | Groesse | Schreibtisch [M] | Kontrolle |
  |---|---|---|
  | sigma^2 | 0,25 | 0,2491 +- 0,0009 |
  | E abs(Delta eta) | 0,375 | 0,3746 |
  | E cosh Delta eta | 1,1378 | 1,1371 |

  - Links je Rapiditaetseinheit: Rauch 1,005.
  - Mittleres tau sqrt(N) des gewaehlten Links: 0,738 (Kontrolle) und 0,741 (Diamant, innen), kuerzer als ein
    zufaelliger Link (sqrt(pi)/2 = 0,886 [M]).
- **Latten (v3):**
  - **L1 kann scheitern:** ja.
    - KS1 und KS2 sind gescheitert, KS0 nach Wortlaut ebenfalls.
    - KS3 scheitert ohne Rand an den schweren Schwaenzen.
    - Die Drift im Inneren haette von 0 abweichen koennen (Rauch 1 zeigte zufaellig +0,04 +- 0,016).
  - **L2 Gegenprobe:**
    - eingefroren, bis zum Rand, N = 16 000
    - unbegrenzte Streuung, SE ueber Bloecke, Spiegelprobe
  - **L3 Numerik:**
    - Spiegelung auf 1e-15
    - Linkzahl gegen Ortsformel auf 0,005
    - Schritt-Statistik gegen Schreibtisch auf 1 SE
  - **L4 schon bekannt:**
    - Teilchen auf Kausalmengen diffundieren im Impuls, Lorentz-invariant ("swerves", Dowker/Henson/Sorkin 2004) [L].
    - Lorentz-invariante Diffusion auf der Massenschale heizt [L?, Philpott/Dowker/Sorkin um 2009].
    - Beobachtungen begrenzen die Diffusionskonstante stark [L?, Kaloper/Mattingly 2006].
    - Neu sind hier nur:
      - die exakte 1+1-Zahl sigma^2 = 1/4 je Linkschritt fuer die Regel "naechste Rapiditaet"
      - die Groesse der Scheinreibung durch den Rand
  - **L5 Messbezug:** keiner (synthetisch, 1+1, eine Laeuferregel).

## 5. Selbstanzeigen

1. **Die Hauptregel ist meine Festlegung** (Karte: "Laeufer nahe dem Rand ausschliessen").
   - Sie liest die Laeufer mit kleiner Rapiditaet aus. Daher kommen die Scheinreibung in KS1 und die Saettigung in KS2.
   - Die Urteile KS1 und KS2 beschreiben also den endlichen Diamanten mit dieser Regel, nicht das Netz im Inneren.
   - Die Kartenvariante "bis zum oberen Rand" (ohne Regel) scheitert ebenso, mit etwas staerkerer Drift (+-1,14 bis
     1,17).
2. **Die Ausgaenge waren zum grossen Teil vorab ableitbar.**
   - Ohne Rand sind KS1 und KS2 Folgen von Boost- und Spiegelsymmetrie [M]. sigma^2 = 1/4 habe ich vor jeder Rechnung
     hergeleitet.
   - Im Diamanten folgt das Scheitern aus dem Verhaeltnis von Streubreite (3,5 bei n = 50) zu Rapiditaetsraum (~4,4).
     Das stand vor der Rechnung im Plan (1.3, 3).
   - Der Test prueft damit vor allem Code, Herleitung und die Groesse des Randeffekts.
3. **Rauch vor dem Einfrieren** (PLAN 8.1):
   - Nach Rauch 1 habe ich B von 300 auf 1000 erhoeht (Stichprobengroesse). Grund: bei N = 4000 waren bei n = 50 nur
     0,3 bis 0,7 % der Laeufer im Inneren.
   - Die zufaellige Drift +0,040 +- 0,016 in Rauch 1 fuehrte zur Spiegelprobe und zu Rauch 2 (dort -0,001 +- 0,004).
   - Schwellen und Regeln blieben.
4. **KS0 berichtigt.**
   - Das Urteil steht auf allen Punkten (Kartenwert = L/N). Nach Kartenwortlaut ist KS0 nicht eingetroffen (+0,62 gegen
     +-0,15).
   - Die Berichtigung stand vor jeder Rechnung im Plan, mit der Erwartung "Wortlaut scheitert".
5. **KS3 "eingetroffen" ist kein Beleg fuer das Heizen ohne Rand.**
   - Unter der Hauptregel steigt <cosh> bis n ~ 15 (Ausbreitung vor dem Randkontakt), dann saettigt es und faellt leicht
     (2,92 bei n = 50, 2,42 bei n = 100).
   - Das Heizen ohne Rand zeigen der Schreibtisch (1,1378^n) und der Median der Kontrolle. Das 3-SE-Kriterium auf den
     Mittelwert scheitert dort an den schweren Schwaenzen.
6. **Die Randregel "bulk-exakt" beruht auf meiner Herleitung [M]** (PLAN Abschnitt 4); niemand hat sie gegengelesen.
   - Dafuer sprechen:
     - Drift 0 in allen 16 Klassen
     - <Delta eta^2> = 0,250 fuer abs(eta) < 1,5, gleich der Kontrolle ohne Rand
     - eingefrorene Mittel 0 (Martingal)
     - exakte Spiegelprobe
   - Fuer festes N statt Poisson gilt das Martingal nur bis auf O(1/N); das ist hier nicht aufloesbar.
7. **Statistik:** Die Populationen der Hauptregel bei verschiedenen n sind ineinander geschachtelt. SE und Var behandeln sie
   je n getrennt; das SE in KS3 ist deshalb konservativ.
8. **Kosmetik:** In lauf-69/auswertung.json steht einmal das Literal Infinity, bei Gegenprobe N16000_hauptregel, KS2,
   max_durch_min_steigung (kleinste Steigung <= 0). jq liest es, strenge JSON-Leser nicht. Kein Urteil betroffen.
9. **Kein frischer Gegenleser** fuer Code, Herleitungen und Text.
10. **Zeitbox:** Start 04:35:13 CEST, Text ab 05:05:50 CEST, Abschluss 05:08:48 CEST (date), innerhalb von 90 min.

## 6. Bedeutung

- **Fuer Finns Weiche:**
  - Ein zufaelliges Raumzeit-Netz ohne Ruhesystem bremst ein Teilchen nicht. Im Inneren gibt es keine Reibung zu
    irgendeinem Bezugssystem [E].
  - Es laesst die Geschwindigkeit zittern, gleich stark in jedem Bezugssystem, und heizt dadurch [M, E].
  - Das ist das Gegenstueck zu ZUFALLS-REIBUNG-1: Ein raeumliches Zufallsnetz bremst zu seinem Ruhesystem.
  - Beide Wege sind unterscheidbar:
    - Reibung zeigt ein Ruhesystem an.
    - Zittern mit Heizen zeigt keines an.
- **Der Rand verhaelt sich wie ein Ruhesystem [E].**
  - Ein endliches Netzstueck zeichnet sein eigenes Ruhesystem aus.
  - Wer nur die Teilchen zaehlt, die drin bleiben, sieht Scheinreibung.
  - Messungen an endlichen Ausschnitten muessen das trennen.
- **Die Staerke des Zitterns [M, H]:**
  - In 1+1 gibt es genau 1 Link je Rapiditaetseinheit (KAUSAL-1). Wer pro Schritt dem naechsten Link folgt, aendert seine
    Rapiditaet deshalb um etwa 0,5 je Schritt, unabhaengig von N.
  - Ein Teilchen, das einzelnen Links folgt, haette seine Geschwindigkeit nach wenigen Dutzend Schritten vergessen.
  - Reale Teilchen tun das ueber unvorstellbar viele Planck-Schritte nicht. Also folgen sie nicht einzelnen Links,
    sondern mitteln ueber sehr viele, oder das Zittern je Schritt ist winzig. Das ist der Inhalt der Swerve-Schranken [L?].
  - [H, nicht gerechnet]: In 3+1 ist die Zahl der Links je Volumen im Raum der Geschwindigkeiten ebenfalls eine feste
    Zahl. Das Zittern je Linkschritt waere dort von derselben Groessenordnung.

## 7. Einfach gesagt

Wir haben Teilchen ueber ein zufaelliges Netz aus Raumzeit-Punkten laufen lassen, das keine Ruhelage hat; bei jedem
Schritt nimmt ein Teilchen die Verbindung, deren Richtung seiner eigenen Geschwindigkeit am naechsten kommt. Gebremst wird
es im Inneren des Netzes nicht: Im Mittel behaelt es seine Geschwindigkeit, egal wie schnell es anfangs war. Das Netz laesst
die Geschwindigkeit aber bei jedem Schritt deutlich zittern, und dadurch steigt die mittlere Energie immer weiter an; es
heizt also, statt zu bremsen. Nur am Rand unseres endlichen Netzstuecks sieht es nach Bremsen aus, weil die schnellen
Teilchen dort zuerst hinausfallen; das liegt am Rand, nicht am Netz.
