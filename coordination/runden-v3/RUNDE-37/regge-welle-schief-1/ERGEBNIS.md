# REGGE-WELLE-SCHIEF-1: Ergebnis (Runde 37, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 05:08:26 CEST. Plantext ab 05:23:53 CEST.
  - Rauchlaeufe 03:22:29 bis 03:31:25 UTC (drei Fassungen, Protokoll in PLAN.md Abschnitt 9).
  - Eingefroren 05:32:52 CEST: PLAN.md.eingefroren-20261004-053252 und Code-Kopien *.eingefroren-20261004-053252;
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe:
    - s = 0: 03:33:03 bis 03:35:35 UTC, cpu5.
    - s = 0,1: 03:33:00 bis 03:35:48 UTC, p4000b (nur CPU).
    - s = 0,2: 03:35:35 bis 03:38:22 UTC, cpu5.
    - Auswertung: 03:38:22 bis 03:38:35 UTC, cpu5.
    - Nachtrag Weg K (beschreibend): 03:47:07 bis 03:47:28 UTC, cpu5.
    - Alle rc = 0.
  - Text ab 05:42:09 CEST.
- Nach dem Einfrieren ist der Code unveraendert. Die Pruefsummen auf der .69 (lauf-69/PRUEFSUMMEN.txt), lokal und
  eingefroren stimmen ueberein.
- Alle Zahlen stammen aus einer linearisierten Gitterrechnung auf der .69 (numpy/scipy, complex128). Gerechnet ist die
  formale Fortsetzung k_tau -> i omega einer euklidischen Form wie in REGGE-WELLE-1. Keine Messdaten.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier nur ueber die Vorgaengerkarten)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik
  - [E] hier gerechnet
  - [H] Hypothese
  - [F] Festlegung im Plan
- Netz: X -> A X mit A = diag(1, 1 + s B), B und Saat wie REGGE-4D-SCHIEF-1. Die Zeitachse ist Gitterachse 0, senkrecht
  zum Raum, Zeitkante Laenge 1. 24 physikalische Richtungen, abs(k_phys) = 0,05; 0,1; 0,2; 0,4; 0,8;
  k_lat = A^T k_phys. v = Re omega / abs(k_phys).

## 1. Ergebnis zuerst

1. **Lange Schwerewellen laufen auch im schiefen Netz mit Lichtgeschwindigkeit, in jeder Richtung, mit genau zwei
   Polarisationen [E].**
   - Windung 2,000 an allen 360 Punkten. In R liegt nur das Paar, reell (abs(Im omega) <= 6,7e-10), TT-Anteil
     >= 0,9999996 bei 0,05.
   - Bei abs(k) = 0,05 gilt abs(v - 1) <= 3,0e-4 (s = 0,1) bzw. <= 5,1e-4 (s = 0,2).
2. **Kurze Wellen verraten die Schiefe: Die zwei Polarisationen laufen verschieden schnell (Doppelbrechung) [E].**
   - Die Aufspaltung waechst etwa wie k^2: bei s = 0,2 von <= 3,4e-4 (0,05) bis 1,5e-3 bis 6,2e-2 (0,8, je nach
     Richtung); bei s = 0,1 bis 2,4e-2.
   - Die exakte Entartung und die Wuerfelgitter-Formel des Kuhn-Netzes (REGGE-WELLE-1) gelten nicht mehr.
3. **Bei s = 0,2 ist in einigen Richtungen eine Polarisation schneller als das Licht [E].**
   - fib10: v = 1,0000615 (0,05), 1,000245 (0,1), 1,00096 (0,2), 1,00355 (0,4), **1,01002 (0,8)**.
   - Dazu fib01 (1,00021 bei 0,4), 123 und -1-2-3 (knapp ueber 1 bei 0,05 bis 0,2).
   - Der Ueberschuss waechst wie +k^2: Die Grenzgeschwindigkeit langer Wellen bleibt 1, aber die Gitterkorrektur hat in
     diesen Richtungen das "falsche" Vorzeichen. Bei s = 0,1 bleibt v ueberall unter 1 (hoechstens 0,99991).
   - Unabhaengig vom Ableitungsweg: Weg T und Weg K stimmen bei fib10, 0,8 auf 1e-11 ueberein (Nachtrag).
4. **Die Diagonalmode wird eine zusaetzliche Gitterwelle, nicht am Lichtkegel, sondern am Zeit-Zonenrand [E].**
   - Im Zensus aller Wurzeln (Re omega <= 2,4, abs(Im omega) <= pi) liegt bei s != 0 an 229 von 240 Punkten eine
     weitere intrinsische Wurzel. An den uebrigen 11 ist sie auch da, liegt aber knapp unter den Pruefgrenzen
     (rho < 0,05 oder Physikalitaet < 0,1).
   - Sie ist **gestaffelt**: Im omega = +-pi, also ein Vorzeichenwechsel je Zeitschritt. Der Diagonalanteil ist hoch
     (0,75 bis 0,99 bei s = 0,1).
   - **s = 0,1:** schwer, Re omega = 2,28 bis 2,38.
   - **s = 0,2:** leicht, Re omega = 0,25 bis 0,82. An 11 Punkten (x+, x-, xy+, xy-, 312, fib04, fib08 bei 0,4
     bzw. 0,8) wechselt auf der euklidischen Linie die Signatur von 2 auf 3 negative Eigenwerte. Dort ist die Welle auf
     die imaginaere Achse gekippt.
   - An 10 dieser Punkte steht sie als intrinsische Wurzel bei abs(Im omega) = 2,57 bis 3,10 (an fib04, 0,8 unter den
     Pruefgrenzen). Formal ist das eine rein anwachsende Welle mit Rate 2,6 bis 3,1 je Zeiteinheit.
   - In R (Hauptlesart der Karte) taucht davon nichts auf.
5. **Urteile:**
   - WS0 bis WS5 sind nach der Hauptlesart eingetroffen.
   - WS3 und WS4 sind in der vorab festgelegten Zensuslesart (Kartenluecke K1) **nicht eingetroffen**.
   - Bedeutung: Lange Wellen bleiben einsteinsch. Kurze Wellen zeigen Doppelbrechung und Ueberlichtgeschwindigkeit. Die
     negative Diagonalmode ist keine reine Zwangsmode: Bei s = 0,2 ist sie stellenweise formal eine anwachsende
     Gitterwelle.

## 2. Urteile

Die Urteile entstehen mechanisch nach PLAN.md Abschnitt 6 durch code/regge_welle_schief_auswertung.py; die Werte stehen
in lauf-69/auswertung.json. Die Felder "vermerk" sind per jq nachgetragen; Urteile und Werte sind gegen
lauf-69/auswertung.maschine.json identisch (jq -S, cmp). Kein Punkt ist gesperrt (Abschnitt 5 des Plans).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil (Hauptlesart) | Zusatzlesart | Kennzahlen |
|---|---|---|---|---|---|
| WS0 | s = 0 reproduziert REGGE-WELLE-1 (v auf <= 1e-9) | 85 % | **eingetroffen** | - | 120 von 120 Punkten bitgleich: max abs(dv) = 0 (auch komplex), gleiche Windung und Zahl |
| WS1 | s = 0,1/0,2, abs(k) = 0,05: genau zwei laufende Moden mit abs(v - 1) <= 1e-3 | 75 % | **eingetroffen** | komplex: eingetroffen | Windung 2 an 48 von 48 Punkten; max abs(v - 1) = 5,1e-4 (s = 0,2, fib06) |
| WS2 | [H] s = 0,2, abs(k) = 0,8: Moden unterscheiden sich in mindestens einer Richtung um > 1e-4 in v | 65 % | **eingetroffen** | - | Aufspaltung 1,5e-3 (312) bis 6,2e-2 (fib06), in allen 24 Richtungen > 1e-4 |
| WS3 | [H] Keine Zusatzmode: Zahl der laufenden Moden bleibt 2 (s = 0,1/0,2, alle Punkte) | 50 % | **eingetroffen** | Zensus: **nicht eingetroffen** | Windung in R 2 an 240 von 240 Punkten. Zensus: 3 oder 4 intrinsische Wurzeln an 229 von 240 Punkten; Kontrolle s = 0 erfuellt (2 an 120 von 120) |
| WS4 | [H] Kein Anwachsen: keine Wurzel nahe der reellen Achse mit abs(Im omega) > 1e-6 | 45 % | **eingetroffen** | Zensus: **nicht eingetroffen** | in R max abs(Im omega) = 6,7e-10; Zensus: abs(Im omega) = pi (gestaffelt) bzw. 2,57 bis 3,10 (imaginaere Achse) |
| WS5 | [H] s = 0,2, abs(k) >= 0,4: eine Richtung mit v > 1 + 1e-6 | 30 % | **eingetroffen** | nur Polarisationen: eingetroffen | fib10: 1,00355 (0,4), 1,01002 (0,8); fib01: 1,00021 (0,4) |

- **Ohne die 11 Kreuzungspunkte** [F7] sind alle Urteile in beiden Lesarten gleich. Die Ueberlicht-Richtungen fib10 und
  fib01 sind keine Kreuzungspunkte.
- **Kartenwortlaut:** Die Hauptlesarten sind der Kartenwortlaut (K1, K2, K4 im Plan). Die Zusatzlesarten sind vorab
  festgelegt und werden mitberichtet.
- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "WS1 trifft ein, WS2 bis WS5 zeigen Abweichungen" ist ausgeloest: Lange Wellen bleiben im ungeordneten Netz
    einsteinsch. Bei kurzen Wellen zeigt das Netz seine Unordnung durch Doppelbrechung (WS2) und durch eine
    richtungsabhaengige Grenzgeschwindigkeit (WS5).
  - "WS3 und WS4 treffen ein: Die negative Mode bleibt eine reine Eich- oder Zwangsmode ohne eigene Ausbreitung" gilt
    nur in der Hauptlesart, also nahe dem Lichtkegel.
  - Der Zensus zeigt: Die Diagonalmode ist eine eigene, gestaffelte Gitterwelle. Bei s = 0,2 wird sie an 11 Punkten
    formal anwachsend. Fuer diesen Teil gilt die Kartenbedeutung "WS3 und WS4 verfehlt": Das schiefe Netz ist bei
    s = 0,2 auch in der Fortsetzung krank, nicht nur in der euklidischen Rechnung (Grenzen in Abschnitt 7).

**Agenten-Vorhersagen** (PLAN Abschnitt 7, vor jeder Rechnung mit s != 0)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (80 %) | WS0 bitgleich | **eingetroffen** (max abs(dv) = 0 an 120 Punkten) |
| A2 (80 %) | G: (a) <= 1e-15, (b) <= 1e-11; e_top-Residuum bei s = 0,2 >= 1e-3 | **eingetroffen**: 6,9e-16; 1,6e-12; 4,9e-2 |
| A3 (70 %) | WS1 eingetroffen; max abs(v - 1) bei 0,05 <= 5e-4 | **nicht eingetroffen** (knapp): WS1 ja, aber 5,1e-4 |
| A4 (55 %) | WS2 eingetroffen (Gegenhypothese: skalare Laplace-Struktur, keine Doppelbrechung) | **eingetroffen**; die Gegenhypothese ist widerlegt |
| A5 (60 %) | WS3 Hauptlesart eingetroffen | **eingetroffen** |
| A6 (55 %) | WS4 Hauptlesart eingetroffen | **eingetroffen** |
| A7 (55 %) | Kontrolle der Zensuslesart haelt; die Wurzeln bei +-1,02 abs(k) i sind Scheinwurzeln | **eingetroffen**: s = 0 an 120 von 120 Punkten genau 2; alle uebrigen mit rho = 0 und Physikalitaet 0 |
| A8 (45 %) | Kreuzungspunkte bei s = 0,2 | **eingetroffen**: 11 |
| A9 (60 %) | WS5 Hauptlesart nicht eingetroffen | **nicht eingetroffen**: WS5 ist eingetroffen |
| A10 (85 %) | Wuerfelgitter-Formel mit Gitter-k gilt bei s != 0 nicht (>= 1e-2 bei 0,05) | **eingetroffen**: Abweichung 1,1e-2 bis 0,25 (s = 0,2) |

## 3. Tabellen

### 3.1 Geschwindigkeit des Paars je s und Betrag [E]

v = Re omega/abs(k_phys); Spanne ueber 24 Richtungen und beide Polarisationen.

| abs(k) | s = 0: v | s = 0: Aufspaltung | s = 0,1: v | s = 0,1: Aufspaltung | s = 0,2: v | s = 0,2: Aufspaltung |
|---|---|---|---|---|---|---|
| 0,05 | 0,99979 bis 0,99986 | <= 5,9e-9 | 0,99970 bis 0,99991 | 3,1e-6 bis 1,1e-4 | 0,99949 bis **1,000062** | 4,8e-6 bis 3,4e-4 |
| 0,1 | 0,99917 bis 0,99945 | <= 1,5e-9 | 0,99881 bis 0,99965 | 1,2e-5 bis 4,6e-4 | 0,99796 bis **1,000245** | 1,9e-5 bis 1,4e-3 |
| 0,2 | 0,99668 bis 0,99779 | <= 3,7e-10 | 0,99526 bis 0,99858 | 4,9e-5 bis 1,8e-3 | 0,99197 bis **1,00096** | 7,8e-5 bis 5,4e-3 |
| 0,4 | 0,98693 bis 0,99127 | <= 9,4e-11 | 0,98151 bis 0,99436 | 1,9e-4 bis 6,9e-3 | 0,96954 bis **1,00355** | 3,2e-4 bis 2,0e-2 |
| 0,8 | 0,95048 bis 0,96685 | <= 2,5e-11 | 0,93257 bis 0,97790 | 6,8e-4 bis 2,4e-2 | 0,89776 bis **1,01002** | 1,5e-3 bis 6,2e-2 |

- max abs(Im omega) in R: 2,5e-10 (s = 0), 2,3e-10 (s = 0,1), 6,7e-10 (s = 0,2). Das ist Rauschen; es faellt mit
  abs(k) wie in REGGE-WELLE-1.
- Die Spalte s = 0 ist REGGE-WELLE-1 (bitgleich).
- Bilder:
  - lauf-69/bild-geschwindigkeit.png: v ueber abs(k) je s und Richtung.
  - lauf-69/bild-aufspaltung-im.png: Aufspaltung und Im omega.
  - lauf-69/bild-modenzahl.png: Windungszahl und Zensuszahl je Punkt.

### 3.2 Ausgewaehlte Richtungen, s = 0,2 (beide Polarisationen) [E]

| Richtung | 0,05 | 0,1 | 0,2 | 0,4 | 0,8 |
|---|---|---|---|---|---|
| x+ | 0,99981 / 0,99983 | 0,99926 / 0,99930 | 0,99704 / 0,99721 | 0,98833 / 0,98901 | 0,95592 / 0,95830 |
| xyz+ | 0,99986 / 0,99994 | 0,99943 / 0,99977 | 0,99774 / 0,99907 | 0,99107 / 0,99632 | 0,96599 / 0,98562 |
| 123 | 0,99981 / 1,0000008 | 0,99924 / 1,0000027 | 0,99699 / 1,0000006 | 0,98816 / 0,99985 | 0,95558 / 0,99716 |
| fib06 | 0,99949 / 0,99983 | 0,99796 / 0,99933 | 0,99197 / 0,99733 | 0,96954 / 0,98947 | 0,89776 / 0,96006 |
| fib10 | 0,99982 / **1,000062** | 0,99928 / **1,000245** | 0,99713 / **1,000961** | 0,98871 / **1,003549** | 0,95742 / **1,010024** |

- fib10 = (0,280; -0,599; -0,750) physikalisch, abs(k_lat)/abs(k_phys) = 1,198.
  - Wurzeln bei 0,8: s(omega) = 2e-17, rho 0,71 bis 0,73, Physikalitaet 0,89 bis 0,97, TT 0,9953 / 0,9995.
  - Das Minimum von s(omega) auf der reellen Achse liegt unabhaengig bei omega = 0,80802, also v = 1,01002.
- Ueberschuss v - 1 bei fib10: 6,2e-5 / 2,4e-4 / 9,6e-4 / 3,5e-3 / 1,0e-2. Je Verdopplung von k etwa der Faktor 4,
  also wie k^2.
- 123 liegt bei 0,05 bis 0,2 knapp ueber 1 (+8e-7, +2,7e-6, +6e-7; ueber 1e-6 nur bei 0,1) und faellt bei 0,4 unter 1.
  Dort uebernehmen hoehere Ordnungen. Fuer WS5 zaehlen nur 0,4 und 0,8.

### 3.3 Zusatzwellen im Zensus (intrinsisch, ausserhalb des Paars; Kopien omega, omega - 2 pi i gepaart) [E]

| s | Punkte mit 2 / 3 / 4 intrinsischen Wurzeln | Art | Re omega | abs(Im omega) | Diagonalanteil | Lapse/Shift | TT |
|---|---|---|---|---|---|---|---|
| 0 | 120 / 0 / 0 | keine (nur Scheinwurzeln: rho = 0, Physikalitaet 0, auf der imaginaeren Achse) | - | - | - | - | - |
| 0,1 | 4 / 116 / 0 | gestaffelt | 2,28 bis 2,38 | pi | 0,75 bis 0,99 | 0,24 bis 0,74 | 0,08 bis 0,80 |
| 0,2 | 7 / 105 / 8 | gestaffelt | 0,25 bis 0,82 | pi | 0,30 bis 0,53 | 0,06 bis 0,92 | 0,04 bis 0,95 |
| 0,2 | (an 10 Punkten) | imaginaere Achse (18 Wurzeln) | <= 2e-9 | 2,57 bis 3,10 | 0,17 bis 0,46 | 0,47 bis 0,93 | 0,24 bis 0,90 |

- An den Punkten mit nur 2 intrinsischen Wurzeln (4 bzw. 7) liegt die gestaffelte Welle auch vor. Sie faellt dort
  aber unter rho < 0,05 oder Physikalitaet < 0,1 (Klasse "Schein", [F6]). Unklare Wurzeln: keine.
- **Verlauf** (Re omega der gestaffelten Welle; bei Kreuzung kappa*):
  - s = 0,1: in allen Richtungen ~2,32, schwach abhaengig von k (x+: 2,320 bei 0,05 bis 2,279 bei 0,8).
  - s = 0,2, x+: 0,300 (0,05), 0,292 (0,1), 0,257 (0,2), dann Kreuzung bei kappa* = 3,03 (0,4) und 2,56 (0,8).
  - s = 0,2, xyz+: 0,304 bis 0,483; fib10: 0,306 bis 0,718. Die Welle wird mit k schwerer und kreuzt nicht.
- Lesart [M]: omega = a +- i pi heisst z^2 = exp(-omega) = -exp(-a). Euklidisch ist das (-1)^tau exp(-a tau), also
  Vorzeichenwechsel je Zeitschritt und Abklingen mit a. Bei a -> 0 trifft die Welle die imaginaere Achse bei
  k_tau = pi. Danach wandert sie dort als euklidischer Nulldurchgang nach innen (kappa* < pi).
- Bild: lauf-69/bild-zensus.png.

### 3.4 Kreuzungspunkte (s = 0,2; Signaturwechsel auf der euklidischen Linie) [E]

| Punkt | kappa* | Punkt | kappa* |
|---|---|---|---|
| x+, 0,4 | +-3,031 | x+, 0,8 | +-2,565 |
| x-, 0,4 | +-3,031 | x-, 0,8 | +-2,565 |
| xy+, 0,8 | +-3,056 | xy-, 0,8 | +-3,056 |
| 312, 0,8 | +-3,031 | fib04, 0,4 | +-2,982 |
| fib04, 0,8 | +-2,540 | fib08, 0,4 | +-3,105 |
| fib08, 0,8 | +-2,614 | | |

- kappa* ist auf das Raster 2 pi/256 genau. Die Zensuswurzeln auf der imaginaeren Achse liegen innerhalb dieser
  Genauigkeit bei denselben Werten, zum Beispiel x+, 0,8: 2,572 gegen 2,565 +- 0,012.
- s = 0 und s = 0,1: kein Wechsel. Die Zahl negativer Eigenwerte ist konstant 1 bzw. 2.
- x+ und x- stimmen ueberein (Inversion).

### 3.5 Polarisationsanteile des Paars [E]

| s | TT (min, alle k) | TT bei 0,05 | Diagonalanteil (max) | Lapse/Shift (max) | Gitterrest C4 (max) |
|---|---|---|---|---|---|
| 0 | 0,9987 | 0,99999998 | 0,016 | 0,048 | 0,048 |
| 0,1 | 0,9955 | 0,9999999 | 0,054 | 0,063 | 0,076 |
| 0,2 | 0,978 | 0,9999996 | 0,054 | 0,084 | 0,120 |

- Beide Kernvektoren eines Paars sind raeumlich-TT (zweiter Kernvektor TT >= 0,979). Die Doppelbrechung trennt also
  zwei TT-Polarisationen; die Diagonalmode mischt bei 0,8 bis 5 % bei.
- **Zwangsbedingungen:**
  - Die Kinetik-Matrix hat an allen 360 Punkten drei grosse Werte (0,18 bis 0,27) und drei kleine (s4/s3 <= 0,0195).
  - Die kleinen drei sind Lapse und Shift (Anteil >= 0,992), wie im Kuhn-Netz.
  - Die grossen Werte bei 0,05: 0,2499 bis 0,2501 (s = 0), 0,2274 bis 0,2277 (s = 0,1), 0,2004 bis 0,2007 (s = 0,2),
    also 1/4 det A (0,2276 bzw. 0,2006). Die Form gilt je Gitterzelle.

### 3.6 Wuerfelgitter-Formel (beschreibend, Karte) [E]

sinh^2(omega/2) = sum_i sin^2(k_i/2); verglichen wird das Paarmittel mit v_hk.

| s | mit Gitter-k: abs(v - v_hk) bei 0,05 | mit physikalischem k: bei 0,05 | mit physikalischem k: bei 0,8 |
|---|---|---|---|
| 0 | <= 2e-9 | (gleich) | 7,9e-12 |
| 0,1 | 9,4e-4 bis 0,126 | <= 4,7e-5 | <= 9,5e-3 |
| 0,2 | 1,1e-2 bis 0,25 | <= 1,5e-4 | <= 2,5e-2 |

- Mit Gitter-k scheitert die Formel schon im Langwellenlimit: Sie gaebe v = abs(A^T n) (bis 1,2 bei s = 0,2). Das
  Netz aber laeuft physikalisch mit 1. So war es vorhergesagt (A10).
- Mit physikalischem k trifft sie das Langwellenlimit, nicht aber die k^2-Korrekturen; die Aufspaltung allein ist schon
  groesser.
- Die exakte Wuerfelgitter-Dispersion aus REGGE-WELLE-1 ist eine Eigenschaft des Kuhn-Kristalls.
- Bild: lauf-69/bild-wuerfelgitter.png.

## 4. Kartenluecken und Lesarten (vor dem Einfrieren offengelegt) und was daraus wurde

- **K1 (WS3/WS4 "nahe der reellen Achse"):**
  - Vorab hergeleitet [M]: Eine anwachsende Gittermode zeigt sich als Wurzel auf der imaginaeren Achse oder weit weg
    vom Lichtkegel, also ausserhalb von R.
  - Genau so kam es [E]: In R ist alles sauber. Die Diagonalmode steht bei Im omega = pi und bei s = 0,2 auf der
    imaginaeren Achse.
  - Hauptlesart (Kartenwortlaut) und Zensuslesart gehen deshalb auseinander. Beide sind vorab festgelegt.
- **K2 (WS5, v aller laufenden Moden):** Beide Lesarten ergeben dasselbe; die ueberlichtschnelle Mode ist eine
  TT-Polarisation.
- **K3 (WS0):** bitgleich. Das prueft die Einbindung (Netz, Form, Komplement), keine unabhaengige Physik.
- **K4 (WS1, Re gegen komplex):** gleich, weil die Wurzeln reell sind.
- **K5 (Kreuzung):** Die Kreuzung liegt nicht im Raum, sondern in der Zeitrichtung bei kappa* = 2,5 bis 3,1, nahe am
  Zeit-Zonenrand. Unsere kleinen Raum-k reichen, um sie zu treffen.
- **Hinweis der Leitung** "x_phys = B x_gitter, k_gitter = B^T k_phys": Die Regel stimmt. Im Code heisst die Abbildung
  A (B ist die Zufallsmatrix). Belegt ist sie durch:
  - WS0;
  - das Langwellenlimit v -> 1 in allen physikalischen Richtungen (mit falscher Umrechnung waere v -> abs(A^T n), bis
    1,2).

## 5. Kontrollen

- **Geometrie und Form** (s = 0 / 0,1 / 0,2):
  - flach 1,8e-15 / 2,7e-15 / 4,4e-15; Weg T 7,5e-12 / 1,5e-11 / 5,8e-11.
  - Formkontrolle G: (a) 6,2e-16 / 5,7e-16 / 6,9e-16 (96 Punkte); (b) 1,2e-12 / 1,4e-12 / 1,6e-12 (64 komplexe
    Punkte).
  - e_top-Residuum: 5e-13 bei s = 0 (Nullmode), 2,8e-2 bis 9,1e-2 bei s != 0 (keine Nullmode). Das bestaetigt den
    Wechsel 5 -> 4 Nullvektoren.
  - k = 0: 11. Eigenwert -0,381 / -0,934 (s = 0,1 / 0,2), Anteil e_top 0,60 / 0,58, wie REGGE-4D-SCHIEF-1.
  - Laurent-Bereich m = -2 bis 2 fuer alle s; weggelassen wurde nichts.
- **Nullstellen, drei Wege:**
  - PEP plus Aberth gegen Windungszahl: 2 gegen 2,000 an allen 360 Punkten.
  - Reelle Achse: Minima von s(omega) bei Re omega (Beispiel fib10, oben).
  - Pruefwerte: s(omega_j) <= 6,4e-17; rho >= 0,41; Physikalitaet >= 0,757.
  - Randregularitaet min rho 0,150; Nullvektor-Residuum <= 8,7e-13.
  - Aberth erreichte an einigen Punkten 80 Iterationen; der letzte Schritt war <= 1,3e-13 (absolut).
- **Symmetrien:** Inversion (Nullstellen bei -n gegen konjugierte bei n) <= 3,1e-12 abs(k); Zeitumkehr-Relation
  F(-omega) = conj F(omega) <= 3,0e-12.
- **Gegenprobe Weg K** (komplexer Schritt mit schiefen Laengen; x+, xyz+, 123, fib05): <= 5,7e-9 abs(k) bei 0,05,
  <= 2,6e-11 abs(k) bei 0,8, fuer alle s.
- **Nachtrag Weg K an den Ueberlicht-Richtungen** (nach dem Einfrieren, beschreibend, nicht geurteilt;
  code/nachtrag_wegk.py, .69 03:47:07 bis 03:47:28 UTC, cpu5, rc = 0):
  - fib10 und fib01 bei s = 0,2, abs(k) = 0,05; 0,4; 0,8.
  - Weg T gegen Weg K: max abs(dv) = 2,4e-9 (0,05) bzw. <= 3,7e-11 (0,4 und 0,8).
  - Beispiel fib10 bei 0,8: v = 1,0100241058 (T) gegen 1,0100241058 (K).
  - Die Ueberlichtgeschwindigkeit haengt also nicht am Ableitungsweg.
- **Zensuskontrolle:** s = 0 hat an 120 von 120 Punkten genau 2 intrinsische Wurzeln. Alle anderen sind Scheinwurzeln
  mit rho = 0 und Physikalitaet 0.
- **Euklidische Linie gegen Zensus:** Signaturwechsel und Wurzeln auf der imaginaeren Achse fallen an denselben Punkten
  und kappa-Werten zusammen (3.4).
- **Latten (v3):**
  - **L1 (kann scheitern):** ja.
    - WS2, WS5 und die Zensuslesarten haetten anders ausgehen koennen.
    - Meine Vorhersagen A3 (knapp) und A9 sind gescheitert. Die Gegenhypothese in A4 (keine Doppelbrechung) ist
      widerlegt.
  - **L2 (Gegenprobe):**
    - WS0 bitgleich; Formkontrolle G; Weg K, auch an den Ueberlicht-Richtungen (Nachtrag).
    - PEP gegen Windung gegen reelle Achse.
    - Inversion und Zeitumkehr.
    - Zensus gegen euklidische Linie; Zensuskontrolle s = 0.
  - **L3 (Numerik):** 1e-9 bis 1e-17.
  - **L4 (schon bekannt):**
    - Regge konvergiert fuer dicke Simplizes gegen Einstein [L, Cheeger/Mueller/Schrader]; das Langwellenlimit war
      also erwartet.
    - Anisotrope, polarisationsabhaengige O(a^2 k^2)-Dispersion auf schiefen Gittern ist fuer Gitterwellengleichungen
      allgemein bekannt [L?].
    - Gestaffelte Moden bei k_tau = pi ("Verdoppler" in der Zeitrichtung) sind ein bekannter Diskretisierungstyp [L?].
    - Ob die Ueberlichtgeschwindigkeit und die negative Diagonalmode fuer schiefe Kuhn-Regge-Gitter in der Literatur
      stehen, habe ich nicht geprueft.
  - **L5 (Messbezug):** GW170817 [L], siehe Abschnitt 7. Das ergibt nur eine schwache Schranke an die Maschenweite,
    keine Bestaetigung.

## 6. Selbstanzeigen

1. **Fehlstart durch Shell-Klammerung** (Rauchlauf, Fassung 1): Mit `cd ... && (A) & (B) &` galt das cd nur fuer A.
   Der Rauchlauf s = 0,2 brach vor dem Programmstart ab, gerechnet wurde nichts. Danach jeder Start mit eigenem cd.
2. **Zwei Codefehler im neuen Zensusteil, beide vor dem Einfrieren behoben und offengelegt** (PLAN Abschnitt 9):
   - (1) Die gemeinsame Aberth-Iteration lief aus dem Ruder (rc = 1). Ersetzt durch die Aberth-Werte aus R' plus
     gedaempftes Newton je Wurzel.
   - (2) Wurzeln auf Im = +-pi wurden doppelt gezaehlt. Berichtigt durch die Paarung omega, omega - 2 pi i (Vertreter
     mit dem groessten rho), vor dem Einfrieren und nach Sicht der Rauchdaten.
   - Die Paarung aendert kein Urteil: Ohne sie waeren die Zensuszahlen hoeher, beide Zensuslesarten aber ebenso "nicht
     eingetroffen", und die Kontrolle s = 0 bliebe unberuehrt (dort keine Wurzeln bei +-pi).
   - Sie aendert die Zahlen in 3.3. Die Regel "Vertreter = groesstes rho" ist meine Festlegung; die Klassengrenze
     (rho 0,05, Physikalitaet 0,1) bestimmt, ob 4 bzw. 7 Punkte "2" statt "3" zaehlen.
3. **Vorwissen aus Rauchlaeufen** (0,3/0,6; 3 Richtungen):
   - Gesehen waren die Aufspaltung (WS2), die gestaffelte Zusatzwelle (Zensuslesarten) und ein Kreuzungspunkt.
   - WS1 und WS5 bei den Kartenbetraegen waren nicht gesehen. Die Ueberlichtgeschwindigkeit war in den Rauchdaten
     nicht sichtbar (v <= 0,9979).
4. **Vor dem Plantext gestartet:** der Rauchlauf s = 0 (Kuhn, aus REGGE-WELLE-1 bekannt), angesehen erst nach den
   Vorhersagen.
5. **Eigene Vorhersagen verfehlt:**
   - A3: Schwelle 5e-4 knapp verfehlt (5,1e-4).
   - A9: Ich hatte v <= 1 erwartet wie im Kuhn-Netz.
6. **auswertung.json:**
   - Die Liste "zusatzwurzeln_intrinsisch" ist im Code auf 200 Eintraege gekuerzt (Gesamtzahl 237 steht dabei). Die
     vollstaendigen Spannen in 3.3 sind per jq direkt aus haupt-s*.json gelesen.
   - Die Vermerke sind per jq eingetragen; die Maschinenfassung ist auswertung.maschine.json.
7. **Bilder:** In bild-geschwindigkeit.png ueberlappen die Tafeltitel (kosmetisch). Nicht berichtigt, weil der Code
   eingefroren ist.
8. **Lokal:** kein python, awk oder perl.
   - Benutzt habe ich jq, ssh, scp, sha256sum, date, grep und sed (sed nur zum Einruecken einer Ausgabe).
   - Dazu Dateibefehle: cp, mv, mkdir, ls, cat (Anhaengen per gequotetem Heredoc), cmp (Bitvergleich), cut, head.
9. **Auf der .69:** Python nur ueber kleintest.sh.
   - Ausserhalb des Starters nur Dateibefehle in meinem Ordner: mkdir, cp, mv, ls, tail, grep, sha256sum und rm der
     eigenen *.teil-Dateien der Rauchlaeufe.
   - Keine Versionsproben, keine fremden Prozesse.
10. **Spuren:** cpu5 und p4000b, nie mehr als zwei Laeufe zugleich.
    - 16 Starts: Rauchlaeufe 3 + 4 + 4 (Fassung 1: einer nicht gestartet, einer rc = 1), Hauptlaeufe 3,
      Auswertung 1, Nachtrag 1.
    - code/nachtrag_wegk.py ist nach dem Einfrieren neu geschrieben. Es importiert den eingefrorenen Code unveraendert,
      ist beschreibend und nicht geurteilt (PRUEFSUMMEN-NACHTRAG.txt).
    - Der laengste Lauf dauerte 167 s.
11. **Reichweite:**
    - Gerechnet ist die formale Fortsetzung einer euklidischen, linearisierten Form um ein flaches, periodisch schiefes
      Netz, mit einer festen Matrix B (Saat 20261004) und zwei Werten von s.
    - Ein zufaelliges Netz ist nicht gerechnet. Ebenso wenig -B: Dort kehrt sich in erster Ordnung das Vorzeichen der
      Diagonalmode um (REGGE-4D-SCHIEF-1).
    - "Anwachsend" fuer Wurzeln mit Im omega != 0 gilt im Rahmen dieser Fortsetzung. Eine echte Lorentz-Regge-Zeit-
      entwicklung ist nicht gerechnet.
12. **Zeitbox:** Start 05:08:26, Text ab 05:42:09 CEST, Abgabe innerhalb von 100 min.

## 7. Bedeutung

- **Zu Finns Frage "Lichtgeschwindigkeit im Netz":**
  - Auch im schief verzogenen Netz laufen lange Schwerewellen genau mit Lichtgeschwindigkeit, in jeder Richtung, mit
    zwei TT-Polarisationen und Lapse/Shift als Zwangsbedingungen. Das Langwellenlimit ist also keine
    Kristalleigenschaft [E].
  - Kristalleigenschaft ist dagegen die Sauberkeit bei kurzen Wellen: exakte Entartung, Wuerfelgitter-Dispersion,
    nie ueberlichtschnell.
  - Im schiefen Netz spalten die Polarisationen auf, wie in einem doppelbrechenden Kristall. In einigen Richtungen
    laeuft eine bei s = 0,2 schneller als das Licht, bei 8 Maschen je Wellenlaenge um 1 %.
- **Dynamisch [E, Deutung H]:**
  - Die negative Diagonalmode bleibt nicht stumm. Sie ist eine gestaffelte Gitterwelle am Zeit-Zonenrand.
  - Bei s = 0,1 ist sie schwer (Abklingrate ~2,3 je Zeitschritt in euklidischer Zeit).
  - Bei s = 0,2 ist sie fast weich, und fuer einige Richtungen schon bei abs(k) >= 0,4 kippt sie in einen euklidischen
    Nulldurchgang. Das bedeutet formal anwachsende Wellen mit Rate ~3 je Zeitschritt.
  - [H] Es gibt eine kritische Schiefe zwischen 0,1 und 0,2. Darueber wird das Netz an der Gitterskala instabil.
- **Gitterschranke [H, Zahlen L]:**
  - GW170817 gibt -3e-15 < v/c - 1 < 7e-16 [L]. Mit v - 1 ~ +0,025 (2 pi a/lambda)^2 (fib10, s = 0,2) folgt
    2 pi a/lambda <~ 1,7e-7, also a <~ 3e-8 lambda. Bei lambda ~ 1000 bis 3000 km sind das a <~ 3 bis 8 cm.
  - Das ist dieselbe Groessenordnung wie die Schranke aus REGGE-WELLE-1, weit ueber der Planck-Laenge, also kein
    Konflikt und kein Test.
  - Eine Polarisationsabhaengigkeit der Ankunftszeit waere ein eigenes Signal. Wie gut sie gemessen ist, weiss ich nicht
    [L?].
- **Hineingesteckt** sind die Regge-Wirkung, die schiefe Abbildung A und die formale Fortsetzung (Regime A). Aus Punkten
  und Strichen allein folgt auch hier nichts.
- **Naechste Schritte [H]:**
  1. Dasselbe mit -B: Wird die Diagonalmode positiv? Verschwinden dann Zusatzwelle, Kreuzung und Ueberlichtrichtung?
  2. s fein zwischen 0,1 und 0,2: Wo trifft die gestaffelte Welle zuerst die imaginaere Achse (kritische Schiefe)?
  3. Ein Zufallsnetz: Mittelt sich die Doppelbrechung heraus? Bleiben stellenweise Minus-Moden?
  4. Analytisch: warum genau Im omega = pi, und ob sich die Aufspaltung als Anisotropie einer Gitter-Metrik schreiben
     laesst.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-053252, EINGEFROREN-SHA256.txt
- code/:
  - regge_welle_schief.py: Rechnung (Netz, Form, Komplement, PEP, Aberth, Windung, Kern, Zensus, euklidische Linie)
  - regge_welle_schief_auswertung.py: Urteile und Bilder
  - unveraendert: regge4d.py, regge_zeit.py, regge_schief.py, regge_welle.py
  - je mit Kopie *.eingefroren-20261004-053252
  - nachtrag_wegk.py: Nachtrag, nicht eingefroren
- lauf-69/:
  - haupt-s0.json, haupt-s0.1.json, haupt-s0.2.json mit Logs
  - auswertung.json (mit Vermerken), auswertung.maschine.json, auswertung.log
  - Bilder: bild-geschwindigkeit.png, bild-aufspaltung-im.png, bild-modenzahl.png, bild-zensus.png,
    bild-wuerfelgitter.png
  - nachtrag-wegk.json, nachtrag-wegk.log
  - PRUEFSUMMEN.txt (.69), PRUEFSUMMEN-lokal.txt, PRUEFSUMMEN-NACHTRAG.txt
- rauch-69/:
  - v1/ (Fassung 1): rauch-s0-alt.json/.log, rauch-s0.1-abbruch1.log
  - v2/ (Fassung 2 mit Probe)
  - v3/ (Endfassung mit Probe)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde37-welle-schief/ (code/, rauch/, lauf/, ref/)

## 9. Einfach gesagt

Wir haben Finns Strich-Netz schief gezogen und wieder gemessen, wie schnell kleine Schwerewellen hindurchlaufen. Lange
Wellen laufen weiterhin genau mit Lichtgeschwindigkeit, in jeder Richtung und mit genau zwei Schwingungsarten, wie es
Einstein verlangt. Kurze Wellen, die nur wenige Maschen lang sind, merken die Schiefe: Die zwei Schwingungsarten werden
verschieden schnell, und in einigen Richtungen ist eine davon sogar etwas schneller als das Licht, bei acht Maschen pro
Welle um ein Prozent. Ausserdem schwingt der fruehere "tote" Strich jetzt als eigene Gitterwelle mit, die bei jedem
Zeitschritt das Vorzeichen wechselt, und bei der staerkeren Schiefe kippt sie an manchen Stellen ins Anwachsen, dort
wird das Netz instabil. Ein schiefes Netz ist also fuer lange Wellen so gut wie der Kristall, fuer kurze Wellen aber
unsauberer und zum Teil krank.
