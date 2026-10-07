# ICO-STAB: Ergebnis (Code-Agent fuer die Leitung, Runde 29, explorativ)

- Gerechnet auf der .69 (kleintest.sh, CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6):
  - Rauchlaeufe 05:27:08 bis 05:34:30 UTC (07:27 bis 07:34 CEST); Parameter anders als echt (Speichen-Ruhelaenge 0,98
    oder N = 8)
  - 20 echte Laeufe 05:35:26 bis 05:42:17 UTC (07:35 bis 07:42 CEST), alle rc = 0, je 16 bis 176 s
  - Auswertung (code/auswertung.py) 05:42:17 UTC
  - Nachprobe (nicht im Plan, nicht gewertet) 05:43:42 bis 05:49:54 UTC: drei Wiederholungen der Kontrolle bei N = 12
    mit anderen Starts
- Plan und Code eingefroren 07:35:22 CEST (PLAN.md.eingefroren-20261003-073522, code/*.eingefroren-20261003-073522),
  vor dem ersten echten Lauf (07:35:26 CEST). Aenderungen nach dem Rauchlauf stehen offen in PLAN.md Abschnitt 6.
- Daten: lauf-69/ (Laeufe, auswertung.json mit den Urteilen), rauch-69/, nachprobe-69/.
- Code: code/ico_stab.py (sha256 3746c7da...), code/auswertung.py (cb331390...), code/laeufe.sh (8e39015f...),
  code/nachprobe.sh (nach dem Einfrieren geschrieben).
- Geschrieben ab 07:51:15 CEST (date).
- **Einheiten:**
  - Im Modell B = 1 und Stablaenge L = 1; Kraefte in B/L^2, Momente und Energie in B/L. Euler-Last mit Gelenken
    P_E = pi^2 B/L^2 = 9,87.
  - Echte Groessen wie FRUST-3D: Knicklicht 20 cm, voller LDPE-Stab angenommen, B ~ 7,7e-3 N m^2. Dann ist
    B/L^2 = 0,19 N, B/L = 38,5 mJ bzw. 38,5 N mm (Biegespannung 3,1 MPa je B/L), P_E = 1,9 N, 0,01 L = 2 mm.

## Ergebnis zuerst

1. **Das Zentrum wandert zur Seite.**
   - Mit Gelenken liegt das freie Minimum 2,0 % unter dem symmetrischen Zustand: 5,708 gegen 5,825 B/L bei N = 20,
     also 220 gegen 224 mJ.
   - Das Zentrum sitzt 0,0602 L (1,2 cm) neben der Huellenmitte, genau in Richtung einer Flaechenmitte (Winkel
     0,00 Grad).
2. **Drei Speichen bleiben gerade, neun knicken.**
   - Gerade sind die drei Speichen zur Gegenflaeche. Sie stehen unter Druck 8,26 B/L^2 (1,6 N), das ist das 0,84-fache
     der Euler-Last.
   - Die neun anderen knicken in drei Stufen zu je drei: Stich 0,191, 0,151 und 0,118 L (3,8, 3,0 und 2,4 cm).
3. **Der symmetrische Zustand ist ein Sattel.**
   - Haelt man das Zentrum in der Huellenmitte fest, knicken alle zwoelf Speichen gleich (Stich 0,138 L, Druck 10,09,
     Huelle Zug 3,84).
   - Laesst man es los, hat die Hesse-Matrix drei negative Eigenwerte, je einen fuer jede Richtung des Zentrums.
   - Alle 14 freien Laeufe (7 Starts, 2 Gitter) enden im selben Zustand, bis auf die Wahl einer der 20 gleichwertigen
     Flaechen. Dort ist die Hesse-Matrix ohne die neun Drehmoden der geknickten Speichen positiv.
4. **Vorab:** IS1 bis IS4 eingetroffen, gleich bei N = 12 und 20.
   - IS0 ist nach der eingefrorenen Regel **nicht eingetroffen**. ctrl_20 ist spannungsfrei (|F| <= 3,5e-11).
     ctrl_12 blieb aber nach 300 Newton-Schritten mit |F| bis 1,7e-6 stehen, ueber der Grenze 1e-8 (vermutlich
     Liniensuche am Rundungsboden der Energie [H]).
   - Nachprobe (nicht gewertet): Drei andere Starts bei N = 12 bleiben unter 1e-8 (<= 4,2e-9). Das spricht fuer eine
     Loeserschwaeche, nicht fuer Physik [H].
5. **Mit Einspannung (nur berichtet, N = 12) bleibt das Zentrum in der Mitte.**
   - Die Sattelprobe zeigt dort keinen negativen Eigenwert.
   - Alle zwoelf Speichen knicken, in zwei Gruppen zu sechs (Druck 24,3 und 14,7).
   - Energie 11,24 B/L (433 mJ), doppelt so viel wie mit Gelenken.

## Vorab gegen Ausgang

Mechanisch nach PLAN.md. Die Messschwelle s = 100 x groesster Gleichgewichtsrest liegt in den gewerteten Zustaenden
(sym_12, sym_20, frei_flaeche_12, frei_flaeche_20) bei 3,6e-9 bis 1,02e-8. Die Urteile stehen in lauf-69/auswertung.json.

| Nr | Vorhersage | Wahrsch. | Ausgang |
|---|---|---|---|
| IS0 | Kontrolle: Speichen-Ruhelaenge R_c ist spannungsfrei, \|F\| L, \|tau\| < 1e-8 | 90 % | **nicht eingetroffen** (Regel: beide Laeufe). ctrl_20: \|F\| <= 3,5e-11, Stich 6e-15. ctrl_12: \|F\| bis 1,66e-6. Der Loeser endete dort bei 300 Schritten (maxit) mit \|grad\| 2,7e-6; Energie -2,5e-14, Stich 8e-10, u 7e-12. tau = 0 (Gelenke) |
| IS1 | Ruhelaenge 1, (G): Speichen auf Druck, alle 30 Huellenstaebe auf Zug (Kontrolle, ableitbar) | 95 % | **eingetroffen**, bei N = 12 und 20 und in beiden Zustaenden. Symmetrisch: Speichen -10,04 / -10,09, Huelle +3,82 / +3,84 (N = 12 / 20). Frei: Speichen -8,21 bis -10,28 / -8,26 bis -10,34, Huelle +2,91 bis +4,22 / +2,93 bis +4,23 |
| IS2 | (G): Das freie Minimum liegt mindestens 0,5 % unter dem symmetrischen Zustand, und das Zentrum ist um u in [0,035; 0,075] L verschoben | 60 % | **eingetroffen**. N = 12: E_frei 5,68251 gegen E_sym 5,80052, also 2,03 % darunter. N = 20: 5,70787 gegen 5,82477, also 2,01 %. u = 0,06022 bei beiden N |
| IS3 | (G): Im freien Minimum ist mindestens eine Speiche gerade (Stich < 1 % L) und mindestens sechs sind geknickt (Stich > 5 % L) | 60 % | **eingetroffen**: 3 gerade (Stich <= 3e-12), 9 geknickt (Stich 0,118 bis 0,191), bei beiden N |
| IS4 | (G): E_min liegt zwischen 5,2 und 6,2 B/L | 70 % | **eingetroffen**: 5,683 (N = 12), 5,708 (N = 20) |

**Bedeutung (vorab festgelegt) und was davon ausgeloest ist:**
- **Fall "IS2 und IS3 treffen ein": ausgeloest.**
  - Nach der Karte: Der Konvexitaetsmechanismus aus FRUST-3D gilt allgemein fuer frustrierte Stabcluster mit
    gemeinsamem Knoten [H]. Ein Frank-Ikosaeder aus Knicklichtern waere sichtbar schief.
  - Meine Einschraenkung: "Allgemein" stuetzt sich auf zwei Faelle (Bipyramide, Ikosaeder), beide mit Gelenken. Mit
    Einspannung bleibt das Zentrum in der Mitte (nur berichtet, unten). Der Mechanismus braucht also Staebe, die geknickt
    laengs weich sind und an den Enden nur Kraefte uebertragen [H].
- **Fall "IS2 trifft nicht ein": nicht ausgeloest.**
- **IS0:** Fuer das Scheitern nennt die Karte keine Bedeutung. Die Kontrolle sollte zeigen, dass der Code den
  spannungsfreien Fall richtig rechnet.
  - Das zeigen ctrl_20, rauch_ctrl_8 und die Nachprobe.
  - ctrl_12 scheitert vermutlich an der Abbruchregel des Loesers [H] (unten, Selbstanzeigen). Das Urteil bleibt
    trotzdem "nicht eingetroffen".

## Lesart [H] (nachtraeglich; der Schreibtisch stand vor den Laeufen in KARTE.md und PLAN.md Abschnitt 5)

- **Warum das Zentrum wandert:**
  - Die Summe der zwoelf Abstaende Zentrum-Ecke ist in der Mitte am kleinsten. Die Mitte ist der Fermat-Weber-Punkt der
    Ecken, und die Abstandssumme ist konvex [M, elementar].
  - Eine geknickte Speiche speichert etwa P_E mal ihre Verkuerzung, also fast linear.
  - Rueckt das Zentrum um u, sinkt die Summe der Verkuerzungen um ~4,2 u^2 und die Energie um ~3,3 P_E u^2. Die
    Nachknick-Versteifung P_E/(2L) holt davon nur ~0,9 P_E u^2 zurueck.
  - Die Sattelprobe bestaetigt das Vorzeichen: drei negative Eigenwerte im symmetrischen Zustand.
- **Wo es haltmacht:**
  - Das Zentrum wandert, bis die fernsten Speichen die Sehne 1 erreichen. Gerade sind sie laengs steif (Ks) und wirken
    als Anschlag.
  - Die erlaubte Zone ist der Schnitt der zwoelf Einheitskugeln um die Ecken. Ihre Spitzen zeigen in die 20
    Flaechenrichtungen, und dort ist die Summe der Verkuerzungen am kleinsten.
  - Schreibtisch E/P_E: Flaeche 0,5823, Kante 0,5837, Ecke 0,5866, symmetrisch 0,5945.
  - Gemessen: u = 0,0602. Das ist etwa die Spitze der Zone (0,0607) minus die Stauchung der geraden Speichen
    (8,26/Ks = 3e-4, also ~0,0004 in u).
- **Die geraden Speichen sind gedrueckt, nicht gezogen.**
  - Das folgt aus dem Gleichgewicht am Zentrum. Ohne sie wuerden die drei Speichen zur nahen Flaeche das Zentrum zurueck
    in die Mitte druecken; die geraden halten mit 0,84 P_E dagegen.
  - Unter P_E bleiben sie gerade. Das ist dasselbe Bild wie FRUST-3D, wo die fuenf geraden Speichen 0,94 P_E trugen.
- **Welche Flaeche:** Die Endflaeche liegt 86 bis 164 Grad von der Startrichtung entfernt; acht verschiedene Flaechen
  kamen vor.
  - Vermutlich draengen in den ersten Newton-Schritten die staerker gestauchten Speichen auf der Versatzseite das
    Zentrum durch die Mitte zurueck: Alle Speichen sind dann noch gerade und tragen das 127-fache der Euler-Last. Die
    Flaeche waehlt also der Rechenweg [H].

## Tabellen (N = 20; in Klammern N = 12)

**Freies Minimum (G), Lauf frei_flaeche_20.** Alle sieben Starts liefern denselben Zustand, Energie gleich auf
4e-14 relativ; Startrichtung und gewaehlte Flaeche unterscheiden sich.

| Speichen (je 3) | cos(theta) gegen u | Sehne | Verkuerzung | Stich (L) | Stich echt | Axialkraft (B/L^2) | echt | Euler-Verh. | Moment im Stab max (B/L) |
|---|---|---|---|---|---|---|---|---|---|
| zur nahen Flaeche | +0,795 | 0,90407 | 0,0959 | 0,1910 (0,1914) | 3,8 cm | -10,338 (-10,278) | -2,0 N | 1,047 | 1,975 (1,967) = 76 N mm, 6,1 MPa |
| naher Guertel | +0,188 | 0,94177 | 0,0582 | 0,1505 (0,1508) | 3,0 cm | -10,140 (-10,090) | -1,95 N | 1,027 | 1,526 |
| ferner Guertel | -0,188 | 0,96433 | 0,0357 | 0,1184 (0,1186) | 2,4 cm | -10,026 (-9,982) | -1,93 N | 1,016 | 1,187 |
| zur Gegenflaeche (gerade) | -0,795 | 0,99968 | 0,0003 | 1,4e-12 (1,7e-15) | 0 | -8,264 (-8,213) | -1,59 N | 0,837 | 0 |

- Biegeenergie je Speiche: 0,964, 0,578, 0,351 und 0.
- Energie 5,70787 (5,68251) B/L = 220 mJ:
  - Biegung 5,6798 (99,5 %)
  - Dehnung: Speichen 0,0200, Huelle 0,0081
- Huelle: Eckradien 0,95116 bis 0,95122 (regulaer 0,95106).
- Endmomente null (Gelenk); Querkraft an den Stabenden <= 1,4e-11, die Endkraft liegt also auf der Sehne.

| Huelle: Kantenklasse (cos Kantenmitte gegen u) | Anzahl | Axialkraft (B/L^2) | echt | Laenge |
|---|---|---|---|---|
| +0,934 (Kanten der nahen Flaeche) | 3 | +4,073 (+4,049) | 0,78 N | 1,000159 |
| +0,577 | 6 | +3,911 (+3,889) | 0,75 N | 1,000153 |
| +0,357 | 3 | +3,681 (+3,659) | 0,71 N | 1,000144 |
| 0 (Guertel) | 6 | +4,232 (+4,218) | 0,81 N | 1,000165 |
| -0,357 | 3 | +2,964 (+2,940) | 0,57 N | 1,000116 |
| -0,577 | 6 | +3,445 (+3,427) | 0,66 N | 1,000135 |
| -0,934 (Kanten der Gegenflaeche) | 3 | +2,928 (+2,908) | 0,56 N | 1,000114 |

**Symmetrischer Zustand (G, Zentrum in der Huellenmitte gehalten), Lauf sym_20:**

| Stabart | Axialkraft (B/L^2) | echt | Stich (L) | Sehne | Euler-Verh. | Moment im Stab max (B/L) |
|---|---|---|---|---|---|---|
| Speichen (alle 12, gleich auf 1,6e-11) | -10,092 (-10,044) | -1,94 N | 0,1381 (0,1384) = 2,8 cm | 0,95120 | 1,023 | 1,394 = 54 N mm |
| Huelle (alle 30) | +3,839 (+3,821) | +0,74 N | < 2e-15 | 1,00015 | Zug | 0 |

- Energie 5,82477 (5,80052) B/L = 224 mJ:
  - Biegung 5,7945 (99,5 %)
  - Dehnung: Speichen 0,0216, Huelle 0,0086
- Haltekraft (Summe der Speichenkraefte am Zentrum): 3,0e-11 (2,9e-11), also null bis auf Rundung.
- Mit gehaltenem Zentrum ist der Zustand stabil: kleinster Eigenwert ohne Drehmoden +6,10 (+10,11).
- **Sattelprobe** (Zentrum losgelassen):
  - Eigenwerte -0,545, -0,513, -0,427 (N = 12: -0,931, -0,870, -0,745), dann +6,11 (+10,13).
  - Restkraft am Zentrum 6,8e-10 (3,2e-10).
  - Die drei Eigenvektoren tragen nur 0,7 bis 0,8 % ihres Gewichts am Zentrum; der Rest sind die Speichenformen, die
    mitgehen.

## Vergleich mit dem Schreibtisch der Karte

| Karte (vor der Rechnung) | Rechnung (N = 20) |
|---|---|
| Ungeknickt ~1250 B/L^2 je Speiche, weit ueber pi^2 | Startenergie 368 = 12 x Ks/2 x 0,049^2; alle zwoelf knicken (symmetrisch) bzw. neun (frei) |
| Huelle symmetrisch T = P/(5 x 0,5257) ~ 3,75 | 3,839; die Formel mit dem gemessenen P = 10,09 gibt genau 3,839 |
| E_sym ~ 5,86 B/L | 5,825 (-0,6 %) |
| E/P_E ~ 0,594 - 3,2 u^2, symmetrisch instabil | Sattelprobe: drei negative Eigenwerte |
| Richtung Flaeche: u = 0,062, drei Speichen gerade | Flaeche, u = 0,0602, drei gerade |
| Richtung Ecke: u = 0,049, eine Speiche gerade | kein Lauf endet dort (nicht direkt geprueft) |
| E_min ~ 5,7 B/L, 1 bis 2 % unter E_sym | 5,708, 2,0 % darunter |
| geknickteste Delta ~ 0,098, Stich ~ 20 % L | 0,0959, Stich 19,1 % L |
| echt: Speichen ~1,9 N, Huelle ~0,7 N, E ~ 0,22 J, Zentrum ~1 cm | Speichen 1,6 bis 2,0 N, Huelle 0,56 bis 0,81 N, 0,220 J, 1,2 cm |
| IS1 ableitbar | ja; eingetroffen wie erwartet |

- **Mein Schreibtisch (PLAN.md Abschnitt 5) gegen Rechnung:**
  - u ~ 0,060 gegen 0,0602
  - gerade Speichen ~0,84 P_E gegen 0,837
  - Verkuerzungen 0,096, 0,058, 0,036 gegen 0,0959, 0,0582, 0,0357; Stiche 0,20, 0,15, 0,12 gegen 0,191, 0,151, 0,118
  - drei negative Eigenwerte im symmetrischen Zustand, neun Nullrichtungen im freien Minimum: wie erwartet
  - Huelle "3 bis 4,5" gegen 2,93 bis 4,23
  - **Daneben:** E_sym ~5,90 und E_frei ~5,78 lagen je 1,3 % zu hoch. Die Verkuerzung durch Huellendehnung und
    Speichenstauchung hatte ich nicht abgezogen.

## Kontrollen

- **IS0** (Speichen-Ruhelaenge R_c):
  - ctrl_20: 9 Newton-Schritte bis zum Rundungsboden; \|F\| <= 3,5e-11, Stich 6e-15, u 2e-17.
  - ctrl_12: Der Loeser lief bis maxit (300 Schritte, 55 s). Ab Schritt 8 nahm die Liniensuche nur noch Schritte der
    Laenge 3e-8 bis 7e-9 an, die Energie stand bei -1e-14 und \|grad\| bei 2,7e-6. Rest: \|F\| <= 1,7e-6, Lagerreaktion
    9e-8, Querkraft 8e-8.
  - Rauchlauf rauch_ctrl_8 (N = 8): <= 1,1e-11.
- **Nachprobe** (nicht gewertet; gleicher eingefrorener Code, ctrl_12 mit anderen Starts):
  - zufall2: 13 Schritte, \|F\| <= 4,2e-9
  - zufall3: 12 Schritte, <= 6,3e-10
  - null (ohne Versatz): wieder maxit, 369 s, \|grad\| 1,0e-8, aber \|F\| <= 9,3e-10
- **Gleichgewicht** (alle Hauptlaeufe, G und E):
  - Rest der freien Komponenten <= 1,0e-10, Gradient am Ende <= 7,2e-10.
  - Lagerreaktionen <= 3,9e-11 (G) bzw. 7,1e-10 (E frei): Das Gebilde ist in sich ausgeglichen.
  - In keinem Lauf war ein Stoss aus einem Sattel noetig; alle endeten am Rundungsboden.
- **Gelenk-Probe (G):** Querkraft an den Stabenden <= 2,1e-11 in allen Hauptlaeufen.
- **Gitter N = 12 gegen 20:** E_frei 0,44 %, E_sym 0,42 %, u 0,006 %, Speichenkraft symmetrisch 0,47 %. Alle Urteile
  IS1 bis IS4 gleich.
- **Starts:**
  - Je N enden alle sieben Starts (null, ecke, kante, flaeche, zufall1 bis 3) mit gleicher Energie (Streuung <= 4e-14
    relativ) und gleichem u (auf 1e-6), stets in Flaechenrichtung (Winkel <= 1e-6 Grad).
  - Gewaehlt wurden acht verschiedene Flaechen.
- **Hesse-Matrix im freien Minimum** (die Frage der Karte):
  - Neun Nullrichtungen, genau die neun geknickten Speichen (Drehung um die Sehne, \|H Q\| <= 1,3e-10).
  - Ohne sie ist der kleinste Eigenwert +0,780 (N = 20) bzw. +1,307 (N = 12): **positiv**, das freie Minimum ist stabil.
  - Die Starrkoerpermoden nehmen die Lager heraus. Die Eigenwerte haengen von N ab (Koordinaten nicht massegewichtet);
    aussagekraeftig ist das Vorzeichen.
- **Symmetrischer Zustand:** Alle zwoelf Speichen gleich (Axialkraft auf 1,6e-11, Stich auf 1e-16), alle 30 Kanten
  gleich.

## Einspannung (E), nur berichtet, ohne Urteil (N = 12, zwei Laeufe)

- Verbinder als starre Koerper, jedes Stabende in seiner Richtung im regulaeren Ikosaeder eingespannt (meine
  Festlegung). Ecke 1 fest in Lage und Drehung.
- e_frei_flaeche_12 (Start mit Versatz 0,01 zur Flaeche) endet mit dem Zentrum in der Mitte (u = 1e-13). Die Energie
  ist gleich der von e_sym_12: 11,2396 B/L = 433 mJ, das 1,98-fache von G.
- Sattelprobe in e_sym_12: kein negativer Eigenwert (kleinster +0,018). Mit Einspannung ist der symmetrische Zustand
  stabil.
- **Speichen:** alle zwoelf geknickt, in zwei Gruppen zu sechs:
  - Druck 24,31 (Stich 0,1397) und 14,72 (Stich 0,1362). Das ist das 2,5- bzw. 1,5-fache der Euler-Last mit Gelenken.
  - Die stark gedrueckten sind in beiden Laeufen die Speichen zu den Ecken zweier gegenueberliegender Flaechen (jeweils
    ein anderes Flaechenpaar). Die Symmetrie sinkt also auf eine dreizaehlige Achse durch Flaechenmitten; warum, habe ich
    nicht untersucht.
- **Huelle:** Zug +0,45 bis +11,79, die Kantenstaebe leicht gebogen (Stich 0,009 bis 0,012 L).
- **Momente:** Endmomente bis 1,88 B/L (72 N mm) an den Ecken und 1,06 am Zentrum, im Stab bis 2,00 B/L.
- **Energie:** Biegung innen 9,904, Einspannterme 1,209, Dehnung 0,127. Biegeanteil 98,9 %.

## Latten (v3)

- **L1: ja.**
  - IS2 und IS3 haetten an einem symmetrischen Minimum scheitern koennen; die Einspannung zeigt, dass es das gibt.
  - Die Sattelprobe haette positiv ausfallen koennen.
  - IS0 ist tatsaechlich gescheitert (am Loeser).
- **L2: ja.**
  - Kontrolle (R_c spannungsfrei) und Konkurrenzzustand laufen durch denselben Code. Die Sattelprobe prueft die
    Instabilitaet unabhaengig von der Suche nach dem Minimum.
  - Die Schreibtischwerte der Karte und aus PLAN.md stimmen auf 0,6 bis 1,3 % (Energie) und 1 % (u).
- **L3: ja.** N = 12 und 20 (Abweichung 0,44 %, Urteile gleich), sieben Starts je N, Gleichgewicht <= 1e-10, Hesse-Matrix
  ohne Drehmoden positiv. Ausnahme: ctrl_12 (Loeserabbruch, siehe IS0).
- **L4: teilweise.**
  - Bekannt sind:
    - Franks Fehlpass von 12 Kugeln um eine [S, RUNDE-17]
    - das Nachknicken der Elastica (P/P_E ~ 1 + Delta/(2L)) [L]
    - die Konvexitaet der Abstandssumme (Fermat-Weber-Punkt) [L, elementar]
    - die Lokalisierung des Knickens bei mehreren gleichen Staeben, die eine Last teilen [L, aus dem Gedaechtnis]
  - Fuer genau diesen Symmetriebruch in einem Ikosaeder aus Staeben habe ich nicht gesucht (keine Websuche in diesem
    Auftrag).
- **L5: nein, aber machbar** mit 42 Knicklichtern und 13 Verbindern. Vorhersage [H]:
  - Mit losen Verbindern sitzt das Zentrum ~1,2 cm neben der Mitte, Richtung einer Dreiecksflaeche. Die drei Speichen
    zur Gegenflaeche sind gerade, die anderen neun sichtbar gebogen (2,4, 3,0 und 3,8 cm Stich).
  - Mit festen Verbindern sitzt das Zentrum mittig, alle zwoelf Speichen sind gebogen (~2,7 cm).
  - Stoerungen: Eigengewicht, Reibung in den Verbindern, hohle Staebe.

## Literatur [L, aus dem Gedaechtnis, Angaben nicht nachgeprueft]

- F. C. Frank, Proc. R. Soc. A 215 (1952) 43: Ikosaedrische Ordnung in unterkuehlten Fluessigkeiten (siehe RUNDE-17).
- S. P. Timoshenko, J. M. Gere, Theory of Elastic Stability (1961): Elastica, Nachknicken.
- J. M. T. Thompson, G. W. Hunt, A General Theory of Elastic Stability (1973): Verzweigung, Symmetriebruch, Lokalisierung.
- J.-F. Sadoc, R. Mosseri, Geometrical Frustration (1999).

## Selbstanzeigen

- **IS0 nicht eingetroffen, Regel nicht gelockert.**
  - Die Regel (beide Gitter unter 1e-8) stand vor den Laeufen fest. ctrl_12 verfehlt sie um den Faktor 170.
  - Die Nachprobe mit anderen Starts kam erst nach dem Ergebnis, steht nicht im Plan und ersetzt den Lauf nicht.
  - Vermutete Ursache [H]: Die Energie ist bei N = 12 nur auf ~1e-12 genau (Rundung in 462 Biegetermen je
    (B/l0)(1 - t.t)). Der restliche Abstieg eines Newton-Schritts bei \|grad\| ~ 3e-6 liegt darunter, die Armijo-Suche
    findet keinen echten Abstieg mehr.
  - Die Abbruchregel "Rundungsboden" greift erst bei \|grad\| < 1e-8. Dieselbe Schwaeche traf in FRUST-3D k1_E_12.
    Ich habe sie vor den Laeufen nicht behoben.
- **Konkurrenzzustand nach dem Rauchlauf neu festgelegt** (PLAN.md Abschnitt 6, vor dem Einfrieren): Zentrum = Mittel
  der Ecken statt fest im Ursprung. Im Ursprung festgehalten sass das Zentrum 1,5e-4 neben der Huellenmitte; das
  aenderte die Energie nur um ~7e-7.
- **Vor den echten Laeufen bekannt:** Der Rauchlauf (Fehlpass 0,029) zeigte das qualitative Ergebnis: Flaechenrichtung,
  drei gerade Speichen, 1,2 % Abstand. Die Regeln blieben unveraendert.
- **IS1-Lesart:** Ich habe vor den Laeufen die strengere Lesart gewaehlt (symmetrischer Zustand und freies Minimum).
  Beide Lesarten geben hier dasselbe.
- **Reihenfolge:** PLAN.md Abschnitte 1 bis 5 sind ab 07:28:22 geschrieben. Die Rauchlaeufe waren um 07:28:14 fertig;
  gelesen habe ich sie erst danach (wie FRUST-3D). Die Fassung davor liegt als PLAN.md.bak-vor-rauch daneben.
- **Ecke und Kante als Sattel:** Kein Lauf endete in Ecken- oder Kantenrichtung, auch nicht von dort gestartet. Dass
  diese Lagen Sattel sind, ist nur mit dem Schreibtisch begruendet [H], nicht gerechnet.
- **Einspannung:** nur N = 12, zwei Laeufe, kein Gitter; die Wunschrichtungen sind meine Festlegung.
- **Code:** Das optionale zehnte Argument (Zeitgrenze) von ico_stab.py habe ich nur in den Rauchlaeufen benutzt.
  code/nachprobe.sh ist nach dem Einfrieren geschrieben.
- **Grenzen:**
  - keine Torsion, ideale Gelenke bzw. Einspannungen, kein Eigengewicht
  - Beruehrung zwischen Staeben nicht geprueft. Bei G ist die Knickebene jeder Speiche frei und im Modell vom Anstoss
    bestimmt; echte Speichen koennten sich am Zentrum beruehren.
  - Knicklicht-Zahlen fuer einen vollen Stab; echte sind hohl.
  - Ein tieferer Zustand ausserhalb der sieben Starts ist nicht ausgeschlossen.

## Einfach gesagt

Zwoelf gleiche Kugeln passen nicht ganz eng um eine dreizehnte. Baut man daraus ein Ikosaeder aus gleich langen,
biegsamen Staeben, sind die zwoelf Speichen zur Mitte etwa 5 Prozent zu lang und muessen sich durchbiegen. Die Rechnung
zeigt: Wenn die Staebe in den Ecken locker sitzen, bleibt der Mittelpunkt nicht in der Mitte. Er rutscht gut einen
Zentimeter zur Seite, auf eine Dreiecksflaeche zu. Dann werden drei Speichen wieder gerade, die anderen neun biegen sich
verschieden stark, und das spart 2 Prozent Spannenergie; sitzen die Staebe fest eingespannt, bleibt der Mittelpunkt
dagegen in der Mitte.
