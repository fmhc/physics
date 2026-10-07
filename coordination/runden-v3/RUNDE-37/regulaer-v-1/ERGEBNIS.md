# REGULAER-V-1: Ergebnis (Runde 49, Code-Agent fuer die Leitung claude-primary)

## Kopf

- **Zeiten (date; CEST, die .69 laeuft in UTC = CEST - 2 h):**
  - Start 2026-10-05 12:41:33 CEST. Schreibtischrechnung im Kopf bis 12:56:23, ab dann Plantext.
  - Rauchtests R1 bis R5: 13:03:17 bis 13:04:55 CEST (11:03:17 bis 11:04:55 UTC).
  - Eingefroren 13:05:34 CEST (PLAN.md und code/rv.py, EINGEFROREN-SHA256.txt; auf der .69 gleiche Pruefsummen).
  - Hauptlaeufe H1 bis H5: 11:06:00 bis 11:07:21 UTC; Auswertung H6: 11:07:33 bis 11:07:34 UTC.
  - Nachtrag N1 (nach Sicht, beschreibend): 11:10:52 bis 11:14:12 UTC.
  - Ergebnistext ab 13:15:19 CEST. Ende: letzte Zeile dieser Datei.
- **Laeufe:** 12 kleintest-Einheiten auf der .69 (p4000a, p4000b), alle rc = 0. 5 Rauchtests (alle unter 60 s),
  6 Hauptlaeufe (laengster 57,6 s), 1 Nachtrag (199 s). Kein Lauf ueber 600 s, kein Rauchtest ueber 120 s.
- **Dateien:** PLAN.md (+ .eingefroren-20261005-130534), code/rv.py (eingefroren, sha256 237a98e5...),
  code/nachtrag_beta.py (nach Sicht, sha256 235d1f43...), lauf-69/ (lp1, lp2, kontrollen, kammer1, kammer2, auswertung,
  nachtrag-beta, Logs, PRUEFSUMMEN-69.txt), rauch-69/. Unveraenderte Kopien: ew.py, tp.py (TT-ISO-1),
  danzer_naeherung.py, licht_netz.py (DANZER-NAEHERUNG-2).
- Synthetische Rechnung an einem gedachten periodischen Netz. Keine Messdaten, keine Messdatenbestaetigung.
- Kennzeichen: [M] Schreibtisch, [E] gerechnet, [P] Projekt, [L] Gedaechtnis-Literatur, [H] Hypothese.
- Einheit: a = kubische Kante; Gewichte und Margen in (a/8)^2; Pyrochlorkante l_P^2 = 8 (a/8)^2; beta in a^2.

## Ergebnis zuerst

1. **V ist regulaer: Es gibt eine Hebehoehe.** Die beste Marge ist t_max = 12/7 (a/8)^2 = 3/14 l_P^2. Die Handrechnung
   stand vor jeder Rechnung im Plan; das LP gibt fuer L = 1, L = 2 und den symmetrischen Schnitt dieselbe Zahl
   (Abweichung < 1e-15). RV1 und RV2 sind eingetroffen.
2. **Bahnweise konstante Gewichte genuegen.** V hat 3 Eckbahnen (Pyrochlor P, Lochmitte C, Sechseckmitte H). Zulaessig ist
   ein Dreieck in (x, y) = (w_C - w_P, w_H - w_P) mit den Ecken (7, 4), (-5, -8) und (-11, -8). w = 0 liegt knapp
   ausserhalb, hinter der Wand der 12 HODGE-L-Zuege. Es reicht schon, die Sechseckmitten leichter zu machen (x = 0,
   y = -2).
3. **Die Kammer ist gross und an allen fuenf Flaechenklassen begrenzt.** Ihre Dimension ist 9 (L = 1) bzw. 79 (L = 2).
   Jede Wandgruppe ist eine echte Facette. An den Waenden liegen drei Arten von 2-3-Zuegen: an Finn-Flaechen, an
   Kegel/Sechseck-Flaechen und an den Sechseck-Sechseck-Flaechen von HODGE-L. Dazu kommen 4-4-Zuege in der
   Sechseckebene und das Verschwinden der Sechseckmitte H; dort wird V zum Netz S.
4. **RV3 ist verfehlt: Die l = 4-Anisotropie aendert sich in der Kammer stark.** Bezogen auf beta_mid = 1,244e-3 a^2 ist
   Delta_max = 3,17. Im symmetrischen Schnitt reicht beta von 0,10 bis 4,2 beta_mid. Schon auf halbem Weg zur Wand sind es
   bis 183 % (symmetrisch), 38 % (zufaellige L = 1-Richtungen) und 8 % (zufaellige L = 2-Richtungen). Die
   Grundgeschwindigkeit bleibt dabei fuer jedes w exakt c = 1; die Gewichte wirken erst in Ordnung (k a)^2.
5. **Nachtrag nach Sicht [E, beschreibend]:** Im F-43m-Schnitt (zwei verschieden schwere Lochmitten) wechselt beta in der
   Kammer das Vorzeichen; dort ist die skalare Dispersion bis k^3 isotrop. Im Fd-3m-Schnitt bleibt beta > 0
   (325 Gitterpunkte, Minimum 0,10 beta_mid). RV0 (Kontrollen) ist eingetroffen.

## 1. Schreibtisch-Ergebnis (vor jeder Rechnung im Plan, Abschn. 1) [M]

- **Bahnen:** Fd-3m hat auf den 10 Ecken je Zelle 3 Bahnen, P (4), C (2) und H (4). Die Wyckoff-Namen sind [L].
- **Fuenf Flaechenklassen** mit dem Sehnenabstand g (linear in w). Ich setze x = w_C - w_P und y = w_H - w_P.

| Klasse | Flaeche / Nachbarn | je Zelle | g(x, y) von Hand | LP bei w = 0 [E] | LP am Handpunkt [E] |
|---|---|---|---|---|---|
| 1 | P P P, Finn / Kegel | 8 | 4 - 4x/9 | 4 | 344/63 = 5,4603 |
| 2 | C P P (Dreieck-Sechseck), Kegel / Sechsecktet. | 24 | 1/2 + x/2 - 5y/8 | 0,5 | 12/7 |
| 3 | C P P (Sechseck-Sechseck), Sechsecktet. / Sechsecktet. | 12 | -2/3 + 2x/3 - y | **-2/3** | 12/7 |
| 4 | H P P (Sechseckebene), Loch C / Loch C' | 24 | 3 - x + y | 3 | 12/7 |
| 5 | C H P, Raute im Sechseck | 48 | 4 + y/2 | 4 | 12/7 |

- Handloesung: Das Zulassungsgebiet ist das offene Dreieck (7, 4), (-5, -8), (-11, -8) mit der Flaeche 36 (a/8)^4.
  - Seine Kanten liegen auf g3 = 0, g4 = 0 und g5 = 0; g2 = 0 beruehrt nur die Ecke (-11, -8).
  - Groesste Marge: t_max = 12/7 bei (x, y) = (-23/7, -32/7); aktiv sind g2 bis g5.
  - Das Mittelungsargument (Kammer konvex und gruppeninvariant) gibt t_max(L = 1) = t_max(L = 2) = t_sym.
- **Kontrolle K5 [E]:** Alle 17 Vergleiche Hand gegen LP stimmen (Klassenwerte bis 1e-9, t bis 1e-7, Ecken des Schnitts
  bis 1e-6). Die LP-Extreme des symmetrischen Schnitts liegen bei x in [-11, 7] und y in [-8, 4]. HODGE-L-Zahl: Die
  duale Laenge an Klasse 3 bei w = 0 ist -0,058926 a = -(sqrt2/3)(a/8), wie im HODGE-L-Arbeitsfeld.

## 2. Urteile RV0 bis RV3

| Nr | Vorhersage (Karte, woertlich) | Wahrsch. | Urteil nach Plan | Urteil nach Wortlaut | Kennzahl |
|---|---|---|---|---|---|
| RV0 | Kontrolle: Bei w = 0 meldet das LP genau die 12 verletzten Flaechen je Zelle aus HODGE-L. Eine Delaunay-Zerlegung zufaelliger Punkte ist bei w = 0 zulaessig. Ein bekannt nicht-regulaeres Beispiel (2D "mother of all examples" [L], als Prisma in 3D) ist unzulaessig | 85 % | **eingetroffen** | **eingetroffen** | (a) 12 (L = 1) bzw. 96 (L = 2) verletzte Flaechen, alle Klasse 3, uebrige g >= 0,5. (b) 3 von 3 Saaten zulaessig, min g = 1,4e-4 / 4,5e-5 / 1,6e-5 (Einheitswuerfel^2). (c) t_max = -3,3e-8 <= 1e-9. Positivkontrolle (c'): t_max = 3,5e-3 |
| RV1 | [H] V ist regulaer (t_max > 0) | 55 % | **eingetroffen** (vorab von Hand entschieden) | **eingetroffen** | t_max = 1,7142857142857135 (L = 1), 1,7142857142857137 (L = 2), Hand 12/7 |
| RV2 | [H] Falls regulaer: bahnweise konstante (Fd-3m-symmetrische) Gewichte genuegen | 60 % | **eingetroffen** (vorab von Hand entschieden) | **eingetroffen** | t_sym = 1,7142857142857133 = t_max. Die LP-Loesung des vollen Raums ist selbst symmetrisch (Abweichung 7e-16 bzw. 2e-13) |
| RV3 | [H] Innerhalb der Kammer aendert sich die langwellige l = 4-Anisotropie des gewichteten Laplace um weniger als 10 % ihres Werts in der Kammermitte | 50 % | **nicht eingetroffen** | **nicht eingetroffen** | Delta_max(beta_S4) = 3,169; Delta_max(rms_l4) = 3,169 (206 Stichproben, alle in der Kammer) |

- **Kartenkontrolle L-Unabhaengigkeit:** t_max(1) = t_max(2) (Differenz 2e-16), RV1/RV2-Urteil gleich: bestanden.
- **Bedeutung nach Karte, angewandt:** RV1 trifft ein. Finns "vierte Richtung beim Zusammensetzen" gibt es fuer V als
  Hebehoehe mit messbarem Spielraum. Dynamische Gewichte koppeln dann nur an die Materie (VIERTE-KOORDINATE-L M2). Die
  Pruefung als universelles Feld wird sinnvoll, mit der Einschraenkung aus RV3 und Abschnitt 4 (Wirkung erst in Ordnung
  (k a)^2).

## 3. Tabellen

**3.1 Groesste Marge [E]**

| Rechnung | t_max (a/8)^2 | in l_P^2 | Kasten aktiv | Bahnmittel (w_P, w_C, w_H) in sum w = 0 |
|---|---|---|---|---|
| Hand | 12/7 = 1,714286 | 3/14 = 0,2143 | - | x = -23/7, y = -32/7 |
| LP L = 1 | 1,7142857142857135 | 0,2142857 | nein | (2,4857, -0,8000, -2,0857); x = -3,285714, y = -4,571429 |
| LP L = 2 | 1,7142857142857137 | 0,2142857 | nein | gleich (bis 1e-14) |
| LP symmetrisch | 1,7142857142857133 | 0,2142857 | nein | x = -3,2857142857, y = -4,5714285714 |

**3.2 Kammer (abgeschlossen, Eichung sum w = 0) [E]**

| Groesse | L = 1 | L = 2 |
|---|---|---|
| Dimension modulo Konstante | 9 | 79 |
| Bereich w_P (min, max; Breite) | -8,07 bis 7,59 (15,65) | -19,25 bis 29,40 (48,65) |
| Bereich w_C | -6,80 bis 5,20 (12,00) | -17,76 bis 21,54 (39,30) |
| Bereich w_H | -5,72 bis 3,10 (8,82) | -17,51 bis 17,35 (34,86) |
| Symmetrischer Schnitt | Dreieck (7, 4), (-5, -8), (-11, -8) | gleich (gleiche Zeilen) |

- Die Bereiche je Koordinate haengen an L und an der Eichung. Bei L = 2 bewegt eine Ecke nur 1/8 ihrer Bilder, und das
  Mittel verteilt sich auf 80 statt 10 Ecken. Das ist keine Verletzung der Kartenkontrolle; diese gilt fuer t_max und die
  Regularitaet. In Einheiten l_P^2 (/8) ist die Bahnbreite bei L = 1: P 1,96, C 1,50, H 1,10.

**3.3 Wandzuege [E] (Facette: LP mit Gruppe = 0 und allen anderen >= tau, tau > 1e-6)**

| Klasse | Zugart (aus mu) | neue Kante bzw. Wirkung [M] | L = 1: Gruppen / Facetten (Zeilen je Gruppe) | L = 2 | im symm. Schnitt |
|---|---|---|---|---|---|
| 1 Finn / Kegel | 2-3 | Lochmitte C zur fernen Finn-Ecke | 8 / 8 (1) | 64 / 64 (1) | nicht erreicht |
| 2 Kegel / Sechsecktet. | 2-3 | Dreiecksecke P zu H | 24 / 24 (1) | 192 / 192 (1) | nur Ecke (-11, -8) |
| 3 Sechseck / Sechseck | 2-3 | H_a-H_b (die HODGE-L-Zuege) | 12 / 12 (1) | 96 / 96 (1) | obere Kante |
| 4 Sechseckebene | Ecke (q = H) | H verschwindet; Doppelpyramide um die Achse C-C' (Netz S) | 4 / 4 (6) | 32 / 32 (6) | rechte Kante |
| 5 Raute im Sechseck | 4-4 (q auf Kante) | Speiche H-v_i gegen v_(i-1)-v_(i+1) | 12 / 12 (4) | 192 / 192 (2) | untere Kante |

- Gruppen: 60 (L = 1) bzw. 576 (L = 2), alle sind Facetten. Bei L = 1 fallen in Klasse 5 die Zeilen gegenueberliegender
  Sechseckecken zusammen (gleiches Untergitter; im Plan 10a vor dem Einfrieren erklaert).
- An den Waenden 4 und 5 geht die Potenzzelle von H gegen Volumen 0 [E]: min *0 = 2,5e-9 a^3 bei s = 0,99 zur Ecke
  (-5, -8), gegen 2,5e-3 in der Mitte.

**3.4 l = 4-Anisotropie des gewichteten Skalar-Laplace [E] (DANZER-NAEHERUNG-2-Messung, 40 Richtungen, Fenster
[0,03; 0,12] pi/a)**

| Ort | beta = beta_S4 (a^2) | beta / beta_mid | rms_l4 | a2-Mittel | Bemerkung |
|---|---|---|---|---|---|
| Kammermitte (L = 1) | 1,24396e-3 | 1 | 2,1716e-4 | -4,0803e-3 | c = 1 - 7e-14; l = 2, nichtkub. l = 4 und l = 6 <= 4e-11 |
| Kammermitte, Probefenster | 1,24396e-3 | 1 - 6e-7 | | | Fit robust |
| Kammermitte (L = 2, gekachelt) | 1,24396e-3 | 1 + 4,4e-8 | | | K4, siehe Selbstanzeige 1 |
| w = 0 (umkreisbasiert, ausserhalb) | 1,28152e-3 | 1,030 | 2,2372e-4 | -2,6461e-3 | 12 negative *2, alle *1, *0 > 0 |
| S1: zur Ecke (-11, -8), s = 0,5 / 0,9 / 0,99 | 3,52e-3 / 4,96e-3 / 5,19e-3 | 2,83 / 3,99 / 4,17 | | | groesstes Delta |
| S1: zur Ecke (7, 4) | 5,26e-4 / 2,36e-3 / 3,00e-3 | 0,42 / 1,90 / 2,41 | | | |
| S1: zur Ecke (-5, -8) | 1,63e-3 / 2,13e-3 / 2,26e-3 | 1,31 / 1,71 / 1,82 | | | |
| S1: zur Mitte der g4-Kante (1, -2) | 3,60e-4 / 1,53e-4 / 1,86e-4 | 0,29 / 0,12 / 0,15 | | | |
| S1: zur Mitte der g5-Kante (-8, -8) | 2,70e-3 / 4,09e-3 / 4,40e-3 | 2,17 / 3,29 / 3,54 | | | |
| S1: zur Mitte der g3-Kante (-2, -2) | 1,137e-3 / 1,181e-3 / 1,209e-3 | 0,91 / 0,95 / 0,97 | | | Richtung der HODGE-L-Wand: klein |
| S3: Extreme von w_C (s = 0,99) | 2,48e-5 | 0,020 | 4,3e-6 | | l = 2 <= 6e-11 (Td-symmetrisch) |
| S3: Extreme von w_H, w_P | 1,55e-3 bis 3,92e-3 | 1,25 bis 3,15 | | | l = 2 bis 1,5e-3 (kubisch gebrochen) |

- Delta je Gruppe (Auswertung): S1 1,83 / 2,99 / 3,17 (s = 0,5 / 0,9 / 0,99); S2 0,38 / 0,71 / 0,78; S3 2,15;
  S4 (L = 2) 0,084 / 0,153 / 0,169.
- Alle 206 Stichproben liegen in der Kammer: alle *1, *2, *0 > 0, Vorzeichen von *2 und g an jeder Flaeche gleich,
  |g - delta H| und die Identitaeten (Volumen, sum A* l n n^T = Vol I) <= 1e-12 (Filter ueber alle Stichproben; in der
  Mitte und an den K2-Zufallsgewichten <= 2e-16 bzw. <= 4e-16). Grundtempo c = 1 mit Spanne <= 1e-8; Fit-Rest <= 1e-9;
  kein beta < 0.
- **Nachtrag nach Sicht (N1, N2; beschreibend, nach den Hauptlaeufen geschrieben):**
  - N1: Fd-3m-Schnitt, 325 Gitterpunkte. beta von 1,247e-4 (0,10 beta_mid, nahe der g4-Wand bei (x, y) = (-0,03, -3,02))
    bis 5,186e-3 (4,17 beta_mid, Ecke (-11, -8)); kein Vorzeichenwechsel.
  - N2: F-43m-Schnitt (w_P, w_C1, w_C2, w_H), 1000 Punkte. beta von -2,84e-4 bis 4,58e-3; 10 Punkte mit beta < 0, alle
    mit stark verschiedenen Lochmitten, z. B. (0; 2,10; -6,09; -4,97) oder (0; -3,55; 2,03; -3,20) bei s = 0,9 bis 0,99.
    Laengs Richtung 1 wechselt beta zwischen s = 0,9 (+3,3e-6) und s = 0,99 (-1,8e-5), also im Inneren der Kammer.
    Die l = 2- und nichtkubischen Anteile bleiben <= 8e-10 (kubisch erhalten).
  - Lesart [M/E]: Mit kubischer Symmetrie hat a2(n) nur l = 0 und den kubischen l = 4-Anteil. Wo beta = 0 ist, ist der
    gewichtete Skalar auf V bis zur Ordnung k^3 isotrop. Das gelingt nur, wenn T1- und T2-Loecher verschieden schwer
    sind.

## 4. Bedeutung [H]

- **Fuer Finns "vierte Richtung":**
  - V laesst sich als Unterseite einer gehobenen Flaeche im vierdimensionalen Raum lesen, mit Spielraum. Die Hoehe
    selbst ist eine Gitterfreiheit: Sie aendert keine Kombinatorik, solange sie in der Kammer bleibt, und laesst die
    Grundgeschwindigkeit exakt bei c = 1 (Divergenzsatz [M], gerechnet bis 1e-8).
  - Sie veraendert aber die Ausbreitung von Materiewellen in Ordnung (k a)^2 deutlich, bis zum Faktor 4 oder bis zur
    Isotropie.
  - Waere die Hoehe ein dynamisches Feld, waere ihr Kennzeichen also eine gitterskalige, richtungsabhaengige Dispersion
    (quadratisch in E/E_QG), keine Fuenfte Kraft in fuehrender Ordnung. Das passt zu "im Kontinuum konstant" (de Goes, ueber
    VIERTE-KOORDINATE-L [S dort]).
  - Die Lesart "dritte masselose Mode" (VIERTE-KOORDINATE-L 4.1 A4) wird damit nicht gestuetzt. Geprueft habe ich das
    nicht.
- **Fuer die Delaunay-Dynamik auf V (UMKLAPP-1, TAKT-DYNAMIK-1):**
  - V ist kein Ruhezustand der ungewichteten Auswahlregel: w = 0 liegt hinter der g3-Wand, und die 12 HODGE-L-Zuege je
    Zelle wuerden laufen.
  - V ist aber Ruhezustand jeder gewichteten Regel mit w in der Kammer. Am einfachsten macht man die Sechseckmitten um
    1/32 a^2 leichter (x = 0, y = -2).
  - Die Marge 3/14 l_P^2 sagt, wie weit Gewichte schwanken duerfen, ohne dass ein Zug faellt.
  - Die Waende benennen die ersten Zuege bei einer Drift der Gewichte: die HODGE-L-2-3-Zuege, das Verschwinden von H
    (V -> S) und 4-4-Zuege im Sechseck. Erst ausserhalb des symmetrischen Schnitts kommen die Finn- und Kegel-2-3-Zuege
    hinzu.
  - Fuer eine Dynamik mit Gewichten als Freiheitsgrad hiesse das: V und S liegen in benachbarten Kammern derselben
    Hebung [H].

## 5. Selbstanzeigen

1. **K4 nach Plan nicht bestanden:** beta(L = 2, Mitte) gegen beta(L = 1) relativ 4,4e-8; die Schwelle war 1e-8.
   - Absolut sind das 5,4e-11 a^2. Die symmetrieverbotenen Anteile (l = 2, l = 6, nichtkubisch l = 4) liegen in denselben
     Laeufen bei 1e-11 bis 6e-10 a^2.
   - Die Differenz liegt also am numerischen Boden. Ich hatte die Schwelle gesetzt, ohne den Boden vorher zu messen.
   - Fuer RV3 (Delta = 3,17) und fuer die L-Kontrolle (t_max) aendert das nichts.
2. **Gerundete Lagen in den LP-Zeilen der Kontrollnetze:** zeilen() nimmt die Flaecheneckenlagen aus den kanonischen
   Schluesseln, gerundet auf 6 Stellen.
   - Fuer V ist das exakt (ganzzahlige Lagen in a/8).
   - Fuer die Zufalls-Delaunay-Netze (b) und das Mutter-Prisma (c, c') entsteht ein Fehler um 1e-6. (b) liegt mit
     min g >= 1,6e-5 deutlich darueber. Bei (c) ist g0_min = -9,3e-7 an kugelgleichen Punkten Rundungsrauschen.
   - Das Urteil (c) (t_max = -3,3e-8, Theorie 0) bleibt richtig, ist aber nur auf etwa 1e-6 von einer winzigen positiven
     Marge getrennt. Erst nach Sicht bemerkt.
3. **Hodge-Stern-Formel aus dem Gedaechtnis [L]:** A*_(ij,T) = 1/2 (h h + h h) mit Orthozentren nach Glickenstein.
   - An keiner Quelle gelesen.
   - Geprueft nur ueber Identitaeten: Volumen, Divergenzsatz, sign(*2) = sign(g) mit g = delta 2 h_d h_e/(h_d + h_e) bis
     2e-16, die HODGE-L-Zahl.
4. **CPU statt CUDA:** LP (HiGHS) und dichte Eigenwerte (10 x 10 bzw. 80 x 80) liefen auf der CPU, in den kleintest-
   Einheiten der GPU-Spuren p4000a/p4000b. Der Auftrag nennt HiGHS ausdruecklich; die Projektregel "auf CUDA" ist damit
   nicht woertlich erfuellt.
5. **jq-Grenzfall:** Lokal habe ich mit jq gefiltert (select mit Vergleichen) und mit length Treffer gezaehlt (z. B.
   "0 Stichproben mit nichtpositivem Stern"). Neue Messzahlen habe ich mit jq nicht berechnet; alle Kennzahlen stammen
   aus den Laeufen auf der .69. Dazu kommen Umrechnungen im Kopf (Einheiten, Verhaeltnisse in 3.4).
6. **Nachtrag nach Sicht:** code/nachtrag_beta.py ist nach den Hauptlaeufen entstanden und nicht eingefroren (Pruefsumme
   in lauf-69/PRUEFSUMMEN-69.txt). N1 und N2 sind beschreibend und gehen in kein Urteil ein.
7. **ssh-Wartezeit:** Der ssh-Aufruf, der die Laufketten startete, wartete auf deren Ende (etwa 80 s). Ohne Folgen.
8. **Zeitstempel:** Die Schreibtischrechnung hat keinen eigenen date-Stempel. Belegt ist nur, dass bis 13:03:17 CEST kein
   Lauf stattfand (erster kleintest R1). Der Plantext mit der Handloesung entstand ab 12:56:23.

## 6. Negativliste (nicht behaupten)

- Nicht: "V ist physikalisch gewichtet Delaunay" oder "die vierte Dimension existiert". Gezeigt ist nur, dass eine Hebung
  existiert und wie gross ihr Spielraum ist. Eine Dynamik der Gewichte ist nicht gerechnet.
- Nicht: "Die Hoehe ist eine Fuenfte Kraft". c bleibt exakt 1; die Wirkung liegt in Ordnung (k a)^2.
- Nicht: "Mit Fd-3m-Gewichten wird V isotrop". Im Fd-3m-Schnitt bleibt beta > 0. Der Vorzeichenwechsel steht nur im
  F-43m-Schnitt, und nur im Nachtrag nach Sicht.
- Nicht: "Die Kammerbreite ist L-unabhaengig". L-unabhaengig sind t_max und die Regularitaet, nicht die Bereiche je
  Koordinate.
- Nicht: "K4 zeigt eine L-Abhaengigkeit". Das ist numerischer Boden (Selbstanzeige 1).
- Nicht: "RV3 scheitert nur an den Waenden". Schon bei s = 0,5 liegen S1 (183 %) und S2 (38 %) ueber 10 %; nur S4
  (L = 2, zufaellig) liegt dort bei 8 %. S3 hat nur Punkte bei s = 0,99.
- Nicht: Messdatenbestaetigung irgendeiner Art.

## 7. Einfach gesagt

Finns Netz V kann man sich als Schatten einer gebogenen Flaeche im vierdimensionalen Raum vorstellen, wenn man jedem
Eckpunkt ein passendes "Gewicht" gibt. Von Hand und am Rechner kam dasselbe heraus: Das geht, und es genuegt schon, die
Mittelpunkte der Sechsecke etwas leichter zu machen. Die Gewichte haben viel Spielraum, ohne dass sich das Netz umbaut.
Sie aendern aber, wie stark Wellen im Netz je nach Richtung verschieden schnell laufen, und zwar deutlich, bis zum
Vierfachen. Die Grundgeschwindigkeit bleibt dabei immer exakt gleich.

---
Ende Ergebnistext: siehe naechste Zeile (date).
Abgabe ERGEBNIS.md: 2026-10-05 13:18:04 CEST (date).
