# ERGEBNIS HUELLEN-LEITER-2 (Runde 19)

- Code-Agent. Start 2026-10-02 15:14:36 CEST (date). Plan eingefroren 15:34:04 CEST
  (PLAN.md.eingefroren-20261002-153404), vor dem ersten .69-Lauf (py_compile 15:34:09, erster kleintest-Lauf 13:34:13
  UTC = 15:34:13 CEST). Ein Nachtrag, nach Laufbeginn und als nachtraeglich markiert:
  PLAN-NACHTRAG-1.md.eingefroren-20261002-154320 (Abbruch des Suchbereichs nach dem K0-Befund, Diagnose D1/D2).
  Bericht ab 16:02:31 CEST (date). Uhrzeiten der .69 in UTC (CEST = UTC + 2).
- Code: code/huellen_leiter2.py (Suche der Runde 18 plus stabilisierte Kopplung, Befehl k0newton),
  code/auswertung2.py (K0-Auswertung); Code 1 (code/stille3.py) und code/beutel.py unveraendert. Nach dem Einfrieren
  nicht geaendert.
- Explorativ (v3). Alles modellintern (Modell M2), keine Messdaten. Deutungen sind Hypothesen [H].

## 1 Ergebnis zuerst

1. **K0 nicht bestanden. Nach der Karte ist der stabilisierte Code damit nicht auswertbar; Abbruch vor dem
   Suchbereich.** In den Paaren 0 bis 109 liefert die Kette auf beiden Stufen gleich 97 statt 88 Stellen. Alle 88
   bekannten Stellen sind wiedergefunden, an derselben Lage. Dazu kommen 9 zusaetzliche Vorzeichenwechsel (k = 3 bis 8,
   R = 27,9 bis 37,2), und 15 der 88 Stellen haben den umgekehrten Umlauf (k = 3 bis 9, ab R = 28,45). Der Suchbereich
   R 39 bis 46 ist nicht gerechnet. P1 bis P4 bleiben offen; die Sprossenregel ist nicht getestet.
2. **Die stillen Stellen selbst bleiben, wo sie sind.** Die Newton-Wurzeln von W, alt gegen neu gerechnet, stimmen fuer
   alle 88 Stellen auf beiden Stufen auf <= 1,0e-13 (omega^2) und 1,2e-14 (rho) ueberein (K0c erfuellt, Rangabfall
   sigma2/sigma1 <= 2e-10). Bitweise aendert die Stabilisierung nur die Kopplung M_ac; U_S und U_chichi bleiben gleich
   (0 geaenderte Elemente in 21 Laeufen, wie im Plan begruendet).
3. **Was sich aendert, ist das Vorzeichen von s, bei gleichem Betrag.** An 667 von 4020 Kurvenpunkten je Stufe
   (Zeilen und Unterzeilen der Paare 0 bis 109) hat s das andere Vorzeichen als in Runde 18. |s| ist dabei gleich (bis
   1,4e-3 relativ). Betroffen sind nur die Kurven k = 3 bis 9, zuerst k = 6 und 7 ab Paar 88 (R ~ 28), spaeter die
   unteren. Diagnose (Nachtrag 1): An den 9 Zusatzwechseln hat W keine Nullstelle. Newton laeuft von dort in 8 von 9
   Faellen zu einer echten stillen Stelle (7-mal zu einer der 88 in der Naehe, einmal zu einer bei R = 40,49) und
   konvergiert einmal nicht. Die umgedrehten Stellen haben auch einen umgedrehten Rechteck-Umlauf (3 von 3 aufgeloesten
   Proben je Stufe).
4. **Mechanismus [H]:** s wird von der im Inneren wachsenden a/b-Mode beherrscht, die die Kopplung 2 f chi in die
   c-Loesung saet; das Vorzeichen dieser Saat legt das Vorzeichen von s fest. In Runde 18 kam die Saat aus der Ballmitte
   (chi ~ 1e-13 bis 1e-16), wo die c-Loesung festes Vorzeichen hat. Der Schnitt bei chi < 1e-12 verlegt sie an den
   Schnittradius (r etwa R - 24 bis R - 26), wo die c-Loesung schwingt. Ihre Phase dort wechselt mit R und rho, auf
   den oberen Kurven (kuerzere Wellenlaenge) zuerst. Dasselbe Bild erklaert den Befund der Runde 18 ab R = 40:
   Rundungs-chi in der Mitte mit zufaelligem Vorzeichen kippt alle Kurven zugleich. Die Reparatur muss also das
   Vorzeichen der Saat erhalten, statt die Saat abzuschneiden (Vorschlaege in Abschnitt 6, nicht gerechnet).
5. **Hintergrund bis R = 46,5 sauber:** Q und E auf zwei Gittern in den neuen Zeilen (R 39 bis 46,5) bis 4,4e-11
   gleich, in allen 126 Zeilen bis 6,3e-11; Profile bitgleich mit Runde 18.
   Die Abbildung R <-> omega^2 steht in Abschnitt 4. **Bedeutung nach Karte:** Weil K0 scheitert, ist der stabilisierte
   Code nicht auswertbar. Ueber die Sprossenregel und den Mechanismus "Vorzeichenwechsel der Kopplung je halbe
   Wellenlaenge" sagt diese Runde nichts.

## 2 Vorhersagen P0 bis P4

| Nr | Vorhersage (Wahrsch.) | Ausgang | Zahlen |
|---|---|---|---|
| P0 | K0 bestanden: alle 88 bekannten Stellen unveraendert (90 %) | **nicht eingetroffen** | K0a verletzt: 97 statt 88 gezaehlte Stellen (88 zugeordnet, 9 zusaetzlich). K0b verletzt: Zellen-Umlauf bei 73 von 88 gleich, bei 15 umgekehrt (beide Stufen gleich). K0c erfuellt: Newton-Lagen alt gegen neu fuer 88 von 88 auf beiden Stufen, max 1,0e-13 / 1,2e-14 |
| P1 | k = 0 bis 3: die ersten zwei neuen Sprossen je innerhalb +-0,10 um die Vorhersage (60 %) | **offen** | Suchbereich nach K0 nicht gerechnet (PLAN 3, Nachtrag 1) |
| P2 | Umlauf wechselt weiter von Sprosse zu Sprosse (85 %) | **offen** | wie P1 |
| P3 | Neue Kurve k = 10 beginnt bei R 40,5 bis 42,5 (55 %) | **offen** | wie P1 |
| P4 | Stabilisierung beseitigt den gemeinsamen Vorzeichenwechsel aller Kurven ab R ~ 40 (75 %) | **offen** | wie P1. Nur Diagnose: Im K0-Bereich (R <= 39) gibt es keinen gemeinsamen Wechsel aller Kurven, aber neue Einzelwechsel auf k = 3 bis 9 (Abschnitt 4) |

## 3 Vorhergesagte Sprossen k = 0 bis 3

- Nicht gerechnet. omega^2 der vorhergesagten R aus der Abbildung in Abschnitt 4 (linear zwischen den Zeilen, Stufe 1),
  zur Weiterverwendung.

| k | letzte bekannte Stelle R | vorhergesagt R (omega^2) | gefunden | Abweichung in R |
|---|---|---|---|---|
| 0 | 37,18 | 39,59 (0,762965) / 42,00 (0,760940) / 44,41 (0,759138) | nicht gerechnet | - |
| 1 | 38,40 | 40,51 (0,762163) / 42,62 (0,760458) / 44,72 (0,758921) | nicht gerechnet | - |
| 2 | 38,11 | 40,24 (0,762395) / 42,36 (0,760658) / 44,49 (0,759081) | nicht gerechnet | - |
| 3 | 37,61 | 39,77 (0,762806) / 41,93 (0,760996) / 44,09 (0,759366) | nicht gerechnet | - |

- P3-Fenster R = 40,5 bis 42,5 entspricht omega^2 = 0,762171 bis 0,760549.

## 4 Stellen

### Neue Stellen im Suchbereich

- Keine. Der Suchbereich (Paare 110 bis 123) ist nach dem K0-Befund nicht gerechnet: Die Bloecke Stufe 1 110-124 und
  Stufe 2 110-117, 117-124 (und die zweite Welle auf cpu) haben ueber die Stoppdateien sofort beendet (< 0,5 s, keine
  Zeile, kein Paar). Rechteck-Stichproben an neuen Stellen gibt es deshalb nicht.
- Nebenbefund der Diagnose, nicht gewertet: Newton ab dem Zusatzwechsel bei R = 37,23 (k = 5) lief zu einer stillen
  Stelle bei omega^2 = 0,76218180, rho = 1,24841453 (R = 40,49, Stufe 1, sigma2/sigma1 = 2,9e-12, Rechteck-Umlauf -1
  aufgeloest). Sie liegt im Suchbereich, ist keiner Kurve zugeordnet und geht in keine Wertung ein.

### Hintergrund und Abbildung R <-> omega^2

- Profile wie Runde 18 aus der Saat bei Q = 200, Zeilen 0 bis 125 auf beiden Stufen (hp = 0,01 und 0,005). Fuer alle 126
  Zeilen: |dQ/Q| <= 6,2e-11, |dE/E| <= 6,3e-11 zwischen den Stufen, R auf 3,5e-6 gleich, Rand |f|/f0 <= 6,8e-17.
  Newton konvergiert in jeder Zeile. w2, Q, E, R, chi(0) und N sind in allen 126 Zeilen beider Stufen bitgleich mit
  profile-info der Runde 18. Die Zeilenliste ist bitgleich mit der der Runde 18 (sha256 der w2-Liste).
- R = Radius der chi = 1/2-Kreuzung (r_chi der Runde 18). Die Zeilenformel R ~ 1,3736/(omega^2 - 0,7281) + 0,55 (nur
  fuer die Zeilenwahl) liegt hier um 0,35 bis 0,41 ueber dem gemessenen R.

| Zeile | omega^2 | R Stufe 1 | R Stufe 2 | R Formel | dQ/Q | dE/E | Gitterpunkte St1 / St2 |
|---|---|---|---|---|---|---|---|
| 110 | 0.763542360431 | 38.952 | 38.952 | 39.306 | 4.2e-11 | 4.2e-11 | 8624 / 17248 |
| 111 | 0.76308510908 | 39.454 | 39.454 | 39.812 | 4.3e-11 | 4.3e-11 | 8698 / 17396 |
| 112 | 0.762639579866 | 39.957 | 39.957 | 40.319 | 4.3e-11 | 4.3e-11 | 8772 / 17544 |
| 113 | 0.76220532587 | 40.46 | 40.46 | 40.825 | 4.3e-11 | 4.3e-11 | 8848 / 17696 |
| 114 | 0.761781922677 | 40.962 | 40.962 | 41.332 | 4.3e-11 | 4.3e-11 | 8922 / 17844 |
| 115 | 0.761368966971 | 41.465 | 41.465 | 41.838 | 4.4e-11 | 4.4e-11 | 8998 / 17996 |
| 116 | 0.76096607524 | 41.967 | 41.967 | 42.344 | 4.4e-11 | 4.4e-11 | 9072 / 18144 |
| 117 | 0.76057288257 | 42.469 | 42.469 | 42.85 | 4.2e-11 | 4.2e-11 | 9148 / 18296 |
| 118 | 0.760189041531 | 42.971 | 42.971 | 43.356 | 4.2e-11 | 4.2e-11 | 9222 / 18444 |
| 119 | 0.759814221137 | 43.473 | 43.473 | 43.862 | 4.3e-11 | 4.3e-11 | 9298 / 18596 |
| 120 | 0.759448105884 | 43.975 | 43.975 | 44.368 | 4.4e-11 | 4.4e-11 | 9372 / 18744 |
| 121 | 0.759090394854 | 44.477 | 44.477 | 44.873 | 4.4e-11 | 4.4e-11 | 9448 / 18896 |
| 122 | 0.758740800877 | 44.979 | 44.979 | 45.379 | 4.3e-11 | 4.3e-11 | 9522 / 19044 |
| 123 | 0.758399049757 | 45.48 | 45.48 | 45.885 | 4.3e-11 | 4.3e-11 | 9598 / 19196 |
| 124 | 0.758064879541 | 45.982 | 45.982 | 46.39 | 4.2e-11 | 4.2e-11 | 9672 / 19344 |
| 125 | 0.757738039848 | 46.483 | 46.483 | 46.896 | 4.3e-11 | 4.3e-11 | 9748 / 19496 |

### Abweichungen im K0-Bereich (Diagnose, Nachtrag 1)

- **9 zusaetzliche Vorzeichenwechsel** (auf beiden Stufen, gezaehlt nach der Stellenregel; Lage Stufe 1).
  Bei 8 der 9 stimmt die Lage beider Stufen wie bei den echten Stellen auf <= 7,2e-9 (omega^2) und 6,0e-9 (rho);
  nur Paar 100 (k = 6) weicht ab: R = 34,049 gegen 34,064 (d omega^2 = 1,9e-5, d rho = 1,1e-4).

| Paar | k | omega^2 | rho | R | Zellen-Umlauf | D1 Stufe 1: Newton landet bei | sigma2/sigma1 | Rechteck-Umlauf dort | D1 Stufe 2 |
|---|---|---|---|---|---|---|---|---|---|
| 88 | 7 | 0.77788592 | 1.41307337 | 27.859 | -1 | Nr 49 (k 7, R 28,45), 1. Schritt 5,5e-3 | 9,2e-12 | +1 aufgeloest | gleich (Nr 49) |
| 88 | 6 | 0.77709225 | 1.36372722 | 28.303 | +1 | Nr 46 (k 6, R 27,66), 1. Schritt 1,0e-2 | 9,3e-12 | -1 aufgeloest | gleich (Nr 46) |
| 90 | 5 | 0.77573874 | 1.31032776 | 29.095 | +1 | Nr 51 (k 5, R 29,12), 1. Schritt 1,9e-4 | 4,1e-11 | -1 nicht aufgeloest (Sprung 1,70 rad) | gleich (1,59 rad) |
| 93 | 4 | 0.77346624 | 1.26222546 | 30.531 | +1 | Nr 56 (k 4, R 30,25), 1. Schritt 1,7e-3 | 4,4e-12 | -1 aufgeloest | gleich (Nr 56) |
| 96 | 7 | 0.77101228 | 1.36836288 | 32.251 | +1 | Nr 66 (k 7, R 33,47), 1. Schritt 1,5e-2 | 3,4e-12 | -1 aufgeloest | gleich (Nr 66) |
| 99 | 3 | 0.76921885 | 1.22237725 | 33.639 | +1 | Nr 65 (k 3, R 33,29), 1. Schritt 1,1e-3 | 5,3e-13 | -1 aufgeloest | gleich (Nr 65) |
| 100 | 6 | 0.76871665 | 1.31234106 | 34.049 | -1 | nicht konvergiert (Schritte pendeln 0,011/0,019) | - | - | gleich (nicht konvergiert) |
| 105 | 8 | 0.76594807 | 1.36942274 | 36.506 | +1 | Nr 79 (k 8, R 36,82), 1. Schritt 3,1e-3 | 3,0e-11 | -1 aufgeloest | gleich (Nr 79) |
| 106 | 5 | 0.76520407 | 1.26116915 | 37.228 | -1 | keine der 88: R = 40,49 (Nebenbefund oben), 1. Schritt 0,12 | 2,9e-12 | -1 aufgeloest | nicht gerechnet (600-s-Grenze) |

- Lesart: Ein Zusatzwechsel ist kein Nullpunkt von W. Der erste Newton-Schritt ist gross (1,9e-4 bis 0,12, groesste
  Komponente), und Newton endet an einer echten stillen Stelle (Rangabfall). Ab einer echten Stelle ist der erste
  Schritt <= 8,9e-7 (K0c, Start an der interpolierten Lage der Runde 18) bzw. <= 1,7e-8 (D2).
- Beispiel Paar 93, k = 4 (Stufe 1), s ueber Zeile und Unterzeilen: neu 0,2111 0,1983 0,1835 0,1668 0,1481 0,1276
  -0,1054 -0,0818 -0,0460; Runde 18 -0,2111 -0,1983 -0,1835 -0,1668 -0,1481 -0,1276 -0,1054 -0,0818 -0,0460. Der Betrag
  ist gleich, das Vorzeichen springt zwischen |s| = 0,13 und 0,11, ohne Nulldurchgang.

- **15 bekannte Stellen mit umgekehrtem Zellen-Umlauf** (beide Stufen gleich umgedreht; Lage unveraendert):

| Nr (Runde 18) | k | Paar | R | Umlauf Runde 18 | Umlauf neu St1 / St2 | D2 (Rechteck neu, St1 / St2) |
|---|---|---|---|---|---|---|
| 49 | 7 | 89 | 28.45 | -1 | 1 / 1 | +1 / +1 aufgeloest |
| 51 | 5 | 90 | 29.12 | 1 | -1 / -1 | -1 / -1 nicht aufgeloest (der Zusatzwechsel bei R = 29,10, d omega^2 = 3,8e-5, liegt im Rechteck der Halbbreite 4,2e-4) |
| 55 | 6 | 92 | 30.12 | 1 | -1 / -1 | -1 / -1 aufgeloest |
| 57 | 7 | 94 | 31.00 | 1 | -1 / -1 | -1 / -1 aufgeloest |
| 59 | 5 | 95 | 31.44 | -1 | 1 / 1 | - |
| 63 | 4 | 97 | 32.49 | 1 | -1 / -1 | - |
| 64 | 6 | 97 | 32.51 | -1 | 1 / 1 | - |
| 67 | 5 | 99 | 33.74 | 1 | -1 / -1 | - |
| 71 | 4 | 101 | 34.71 | -1 | 1 / 1 | - |
| 74 | 3 | 103 | 35.45 | 1 | -1 / -1 | - |
| 77 | 5 | 104 | 36.01 | -1 | 1 / 1 | - |
| 79 | 8 | 105 | 36.82 | 1 | -1 / -1 | (D1-Lauf: -1 / -1 aufgeloest) |
| 80 | 4 | 105 | 36.92 | 1 | -1 / -1 | - |
| 83 | 3 | 107 | 37.61 | -1 | 1 / 1 | - |
| 84 | 9 | 107 | 37.65 | 1 | -1 / -1 | - |

- In Runde 18 war der Rechteck-Umlauf an Nr 79 und Nr 83 +1 bzw. -1 (Stichprobe dort). Neu ist der Zellen-Umlauf
  beider umgedreht; an Nr 79 zeigt auch der neue Rechteck-Umlauf -1 (Nr 83 neu nicht im Rechteck gerechnet). Der Umlauf
  ist also eine Konvention der Messgroesse, die die Stabilisierung auf einigen Kurven umdreht; die Stelle selbst
  (Rangabfall) bleibt.

## 5 K0 im Detail

- **Lauf:** Kette der Runde 18 (Zeilen 0 bis 110, Paare 0 bis 109, beide Stufen, Illinois von Anfang an), stabilisierte
  Kopplung; dazu k0newton fuer alle 88 Stellen und beide Stufen (je zweimal: alte und stabilisierte Kopplung, Start an
  der Lage der Runde 18, gleiches Ankerprofil). Auswertung: code/auswertung2.py k0 -> aus/k0-auswertung.json.
- **K0a (Zaehlung): verletzt.** 97 gezaehlte Stellen (Runde 18: 88), keine Stelle nur auf einer Stufe, keine gepaarte
  Stelle mit Merker, kein fehlendes Paar. Alle 88 bekannten sind eins zu eins zugeordnet; 9 sind zusaetzlich
  (Abschnitt 4). In den Paaren 90 (k = 5) und 105 (k = 8) wechselt s innerhalb des Paares zweimal (echte Stelle plus
  Zusatzwechsel); einen gemeinsamen Wechsel aller Kurven gibt es in keinem Paar.
- **K0b (Umlauf): verletzt.** 73 von 88 gleich, 15 umgekehrt, auf beiden Stufen dieselben 15.
- **K0c (Lage): erfuellt.** Newton alt und neu konvergiert an 88 von 88 Stellen auf beiden Stufen (je 2 Schritte).
  |d omega^2| <= 9,5e-14 (St1) bzw. 1,0e-13 (St2), |d rho| <= 1,2e-14 (beide). Bitgleich an den 41 Stellen ohne
  maskierten Punkt (Nr 1 bis 41, R < 26,3); an den 47 uebrigen <= 1e-13. sigma2/sigma1 an der Wurzel <= 2e-10. Newton
  verschiebt die interpolierte Lage um hoechstens 8,9e-7 (omega^2).
- **Zusaetzlich berichtet (kein Kriterium):**
  - Interpolierte Lage neu gegen Runde 18: alle 88 auf beiden Stufen <= 1,5e-10 (omega^2) und 7,4e-11 (rho), 41
    bitgleich. Meine Plan-Erwartung (bis ~5e-8 Verschiebung) war falsch: Der Betrag von s aendert sich nicht, nur das
    Vorzeichen.
  - Zeilenvergleich der neuen Kette: in allen 111 Zeilen auf beiden Stufen gleiche Zahl, Lage (<= 4,3e-10) und
    Vorzeichenfolge der Nullstellen von m_bc. Gegen Runde 18: 22 Zeilen (89 bis 110) mit anderer Vorzeichenfolge, auf
    beiden Stufen dieselben.
  - Matrixelemente (Summe ueber 21 Laeufe, 4131 Pot-Aufbauten, 3,5e7 Gitterpunkte): geaendert M_aa 0, M_ab 0, M_cc 0,
    M_ac 1 837 303. Maskiert 2 123 514 Punkte (die uebrigen hatten g = 0 exakt, dort ist M_ac ohnehin 0), davon 82 mit
    g < 0. Erster maskierter Punkt ab Zeile 85 (R = 26,33, 24 Punkte bis r = 0,23); Zeile 110: 1513 Punkte bis r = 15,1
    (Stufe 1).
- Tabelle aller 88 Stellen: Anhang B.

## 6 Grenzen, Vorschlaege, Selbstanzeigen, Laufzeiten, sha256

### Grenzen

- K0 ist nicht bestanden; der Suchbereich ist nicht gerechnet. Ueber P1 bis P4, die Sprossenregel und R > 39 sagt die
  Runde nichts (ausser dem Hintergrund und dem Nebenbefund bei R = 40,49).
- Der Mechanismus in Abschnitt 1, Punkt 4 ist eine Hypothese. Gestuetzt durch: gleicher Betrag von s bei anderem
  Vorzeichen, Beginn auf den oberen Kurven, kein Nullpunkt von W an den Zusatzwechseln, das Rundungsbild der Runde 18.
  Nicht gerechnet: die Phase der c-Loesung am Schnittradius selbst.
- Die Diagnose D1/D2 ist nachtraeglich (Nachtrag 1) und keine Wertung. Stufe 2: 12 von 13 Punkten (der Lauf 0-13 endete
  an der 600-s-Grenze, der Punkt bei R = 37,23 fehlt).
- Plan-Erwartungen (b) "Umlauf gleich" und (c) "Lage bis 5e-8 verschoben" waren falsch. Meine Schreibtisch-Annahme, die
  Saat aus g >= 1e-12 sei positiv, hat die schwingende c-Loesung am Schnittradius uebersehen.

### Vorschlaege fuer eine Folgerunde [H], nicht gerechnet

- Saat mit festem Vorzeichen erhalten: chi im Inneren nicht abschneiden, sondern unterhalb einer Schwelle (z. B. 1e-10)
  glatt und positiv fortsetzen (Loesung von chi'' + 2 chi'/r = m0^2 chi, an den aufgeloesten Teil angeschlossen). Dann
  kommt die Saat wie in Runde 18 aus der Mitte, ohne Rundungsvorzeichen. K0 wie hier waere dann sinnvoll.
- Oder s saatfrei machen: Y_c in jedem Gram-Schmidt-Schritt gegen Y_b orthogonalisieren (Reihenfolge b vor c). m_bc
  bleibt gleich; s haengt dann nicht mehr von der Saat ab. Das ist eine andere Vorzeichenkonvention, also braucht diese
  Fassung eine eigene K0 (Lage und Zaehlung, Umlauf je Kurve bis auf ein festes Vorzeichen).
- In beiden Faellen Zusatzwechsel mit sigma2/sigma1 pruefen: Ein Vorzeichenwechsel ohne Rangabfall ist keine Stelle.

### Selbstanzeigen

- **Lokale Werkzeuge ausserhalb der Liste:** wc und sort (Zaehlen, Sortieren von Listen), comm (im Monitor-Skript),
  timeout (zwei ssh-Aufrufe), chmod (Einfrieren, von den Regeln verlangt), Shell-Schleifen mit sleep in
  Warte-Befehlen. Kein lokales python oder bc. **Regel verletzt:** Um 16:08 habe ich in einer Pruefzeile versehentlich
  einmal `awk` ohne Programm aufgerufen (wirkungslos, Ausgabe verworfen, nach dem Ende aller Rechnungen). Ein Befehl mit
  vorangestelltem `sleep 45` wurde vom Werkzeug abgelehnt und lief nicht.
- **Auf der .69:** mkdir meines Ordners, rm -rf code/__pycache__ (von py_compile in meinem Ordner angelegt), touch der
  Stoppdateien, nohup/setsid fuer meine Ketten, einmal ps meiner eigenen Prozesse (gefiltert auf mein Warte-Skript).
  Zwei lokale ssh-Sitzungen blieben nach dem Start mit nohup minutenlang offen (ohne Folge fuer die Rechnung). Keine
  Prozesse beendet, keine Dateien ausserhalb meines Ordners angelegt, keine fremden Ordner gelistet.
- **Lesen:** wie freigegeben (Karte, Runde 18 ERGEBNIS, PLAN*, code/, aus/ einschliesslich aus/logs); kleintest.sh und
  hilfs/ der Runde 18 nicht gelesen. Nichts aus Sperrbereichen.
- **Vor der formalen K0-Auswertung gesehen** (15:40 bis 15:55): Newton-K0 Stufe 1, Vorzeichenfolgen und Stellen der
  Paare 80 bis 94 (Stufe 2), dann die vollstaendigen Ketten. Daraus Nachtrag 1 und die Stoppdateien (15:42), vor der
  formalen K0-Auswertung (15:57:25). Das Ergebnis der Diagnose D1 bei R = 40,49 (im Suchbereich) habe ich um 15:55
  gesehen, ebenfalls vor der formalen K0-Auswertung, aber nach dem feststehenden K0-Befund.
- **Ablauf:** Um 15:38 habe ich auf cpu eine zweite Welle (Stufe 2, 110-117) angehaengt, um die Spuren auszulasten;
  sie endete ueber die Stoppdatei sofort. Die Diagnose-Liste (hilfs/diag-liste.sh) hatte zuerst eine nicht eins-zu-eins
  Zuordnung (8 statt 9 Zusatzwechsel); vor den Diagnose-Laeufen berichtigt. Ein fehlerhafter sed-Zwischenstand des
  Skripts lief nie.
- Nichts in den Scratchpad geschrieben (die Ausgaben der Hintergrund-Befehle legt das Werkzeug selbst unter
  /tmp/claude-1000/.../tasks ab). Kein git, kein Peerbus, keine Unteragenten, keine Literatur.

### Laufzeiten (.69, kleintest.sh, Service runtime; UTC)

| Lauf | Spur | Start | Ende | Dauer | rc | Teil |
|---|---|---|---|---|---|---|
| r19hl2-liste | cpu | 13:34:13 | 13:34:14 | 0,5 s | 0 | V0 |
| r19hl2-prof1 / prof2 | cpu / cpu2 | 13:34:19 | 13:34:23 / 13:34:27 | 4,5 s / 8,2 s | 0 | V1 |
| r19hl2-b1-0-50 | cpu | 13:34:51 | 13:37:33 | 162 s | 0 | K0 |
| r19hl2-b1-50-85 | cpu | 13:37:33 | 13:41:42 | 250 s | 0 | K0 |
| r19hl2-b1-85-110 | cpu | 13:41:42 | 13:48:00 | 378 s | 0 | K0 |
| r19hl2-b2-0-50 | cpu2 | 13:34:51 | 13:40:05 | 315 s | 0 | K0 |
| r19hl2-b2-50-80 | cpu2 | 13:40:05 | 13:46:24 | 378 s | 0 | K0 |
| r19hl2-b2-80-92 | cpu3 | 13:34:51 | 13:39:43 | 292 s | 0 | K0 |
| r19hl2-b2-92-101 | cpu3 | 13:39:43 | 13:44:11 | 268 s | 0 | K0 |
| r19hl2-b2-101-110 | cpu3 | 13:44:11 | 13:49:07 | 296 s | 0 | K0 |
| r19hl2-n1-0-44 / n1-44-88 | cpu4 | 13:34:51 / 13:39:05 | 13:39:05 / 13:45:14 | 254 s / 369 s | 0 | K0 |
| r19hl2-n2-0-30 / n2-30-60 | cpu4 | 13:45:14 / 13:50:19 | 13:50:19 / 13:57:24 | 305 s / 425 s | 0 | K0 |
| r19hl2-n2-60-88 | cpu2 | 13:46:24 | 13:54:09 | 465 s | 0 | K0 |
| r19hl2-ausw-k0 | cpu2 | 13:57:25 | 13:57:25 | 0,6 s | 0 | K0 |
| r19hl2-b1-110-124, b2-110-117, b2-117-124, b2-110-117x | cpu, cpu4, cpu3, cpu | 13:48:00 bis 13:57:24 | sofort | je < 0,5 s | 0 | Stoppdatei |
| r19hl2-diag-st1-0-13 | cpu | 13:48:53 | 13:55:38 | 405 s | 0 | Diagnose |
| r19hl2-diag-st2-0-13 | cpu3 | 13:51:08 | 14:01:08 | 600 s (Grenze) | 1 | Diagnose, 8 von 13 Punkten |
| r19hl2-diag-st2-9-13 | cpu | 13:57:04 | 14:00:35 | 211 s | 0 | Diagnose |

- Zusammen ~90 min Spurzeit, 27 min Wandzeit auf vier Spuren.

### sha256

Code (lokal = .69, verglichen; nach dem Einfrieren unveraendert):

```
2755359c497aca04eeeca48f851e83a62a6671aa121713cc709ca5c77076c57e  code/huellen_leiter2.py
46deb0651b9305df5f6bc820e05301753a519d0bfbcdc154b614e6b4ff234374  code/auswertung2.py
1d15a38c17d06c71919cf86b425af43a574a04cba9cc2578cc4e29619d4d9b83  code/stille3.py
f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb  code/beutel.py
```

Plaene:

```
5732232937a79a211f59ebab3bb0da00176f5b48e1cc45d3f45d8738bb3d9f74  PLAN.md.eingefroren-20261002-153404
afa5127fd029056c0388ccfc9a67d30dd8edd617514b80b08ffb1283225073d1  PLAN-NACHTRAG-1.md.eingefroren-20261002-154320
```

Ausgaben (lokal = Spiegel von /home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2/aus/ ohne *.npz):

```
20f104cca0fbc85e69f69ca43875d810e415f6a469e797b71f1db8bbd5065f4d  aus/laeufe/z-st1-*.json (verkettet, Namensfolge, 111 Dateien)
04002f00c7532522c15dc2b73ff5b897565d126296360262bc52d53f62088ed7  aus/laeufe/paar-st1-*.json (verkettet, 110 Dateien)
96b76669782b47b48b4a6e87468acaade4c4b418a40b2dd5e8398a89d83ad4e8  aus/laeufe/z-st2-*.json (verkettet, 111 Dateien)
aac50de27fbf9363d46272056cb77a90962ac9a087d95c310dfb2e43c5b7d2f9  aus/laeufe/paar-st2-*.json (verkettet, 110 Dateien)
eee8662ec1992da375adba32001734fd68c74a9bfa30f819f093dbe90ca6689e  aus/k0-auswertung.json
750f2890429f9146eee9919a525441ebae0e0100994c71d98105d8fcb5e44b0b  aus/k0/k0newton-st1-0-44.json
372fefc3a37a7121228d8292571549a505123b3646a730ee457a37cc526e593e  aus/k0/k0newton-st1-44-88.json
da3162f07b1347c652cb437e3aeec9ee729fb838e62fb711a247611d7e827bc4  aus/k0/k0newton-st2-0-30.json
0e99b1ab776684086ee1c0815ae9c22e3116130bb9b0faddbbf700c18ae2b4cf  aus/k0/k0newton-st2-30-60.json
c6d6405bcd39e0d5d3b6a906fe6a0b6b1e3b95cd7927b491175e79dc2557a069  aus/k0/k0newton-st2-60-88.json
dc79521af21dd7986fc22be396294d15a53eecd881a566be55dd458b6f01717a  aus/diag/umlauf-st1-0-13.json
cc41886a3f4b96d66b75c836dfe27625ad77189b777843775fa31f9acc548e94  aus/diag/umlauf-st2-0-13.json
ade0520103374d786696fe0a75ab8e656d312981a0060ac10f99af7a8967ae44  aus/diag/umlauf-st2-9-13.json
586c36891558f3ac36d20fbab1c672719f3707cd4dcd954df8bf63d0e5fbc748  aus/zeilen.json (= Runde 18 zeilen.json)
72def7e5ba59ebd5cffb034d119d0bbef479a533776db1eec11a2e25f0183458  aus/prof-st1/profile-info.json
5442e9d3bd10fd24e8a79bdd367f921a9de9af5ff0f54a395660ed525fb5e5cc  aus/prof-st2/profile-info.json
```

Referenzen (Kopien aus Runde 18) und Hilfsdateien:

```
5ce185ec655577131d6eca73cb4e8006aab6294ca4ad91840360caaf0a6ab202  ref/stellen-r18.json
586c36891558f3ac36d20fbab1c672719f3707cd4dcd954df8bf63d0e5fbc748  ref/zeilen-r18.json
228b3beccbe82f50bb6e7547f60ba8ca9f154bea9a782a5030254f766f50a9a2  ref/profile-info-r18-st1.json
97c59bf85bdedf69a03332964ee615139792aee82e025d5471ae5611f5c2fdee  ref/profile-info-r18-st2.json
e01b1379ea26a3e309be63f1a6588e349c94f86938c1bfc667216f9e327b74ec  hilfs/zeilen-126.json
e642267d1696e879ac3806ce3283049ae84cd48c46963146852f092d7761d7eb  hilfs/kette.sh
b05d3e2205d95d400d841cb879522d78e3d94eba75569bc518680012c4071796  hilfs/auf-cpu.txt
715a8af760a42d14a611c9924afada9eaa9a747ad0c36dc17acbd1ca374c8bc2  hilfs/auf-cpu2.txt
ec9f68d9482f791d0f88e965509068729e5733e7885a16c580d48f5158d20fbb  hilfs/auf-cpu3.txt
04f78fb235db1b4f613f4fd21956b4b15808c870dc2c3997572f849258b6e796  hilfs/auf-cpu4.txt
a19f3425307da813c58df358549113fb1ca34d8fa2bdc494656b2fa2edebaf0f  hilfs/auf-cpu-b.txt
7d9ad97015d6c2a9d89c97f6de45fba0e6109f94efede7e93de87838d8a0b36b  hilfs/warte-cpu-b.sh
2a51cdc38e6d8db4dec188bcb5f920229cacbde308f06423a52bd13ed4566d23  hilfs/v4-k0.sh
08daad47b38053a7005f227e0a5a7c09e3bde78258f6cc2ea1f416db72789b77  hilfs/diag-liste.sh
9d6ce763b6f2719cfe3cdec38213fd8b2fccdce5bc155e7a2cdff8db58bf7520  hilfs/diag-vergleich.jq
69448dbe021df7947b829415f6275158e3883f932e4ffb7ead5267781e61db05  hilfs/diag-lauf.sh
53fd77558af831a18abf752809757b5e89832a82766d667cb441caa25e75878d  hilfs/diag-punkte-st1.json
5fdbdf7cb2cd38dc049e1946ac8ff1c71322a91fc0062e577fc3a39a2a17c0b8  hilfs/diag-punkte-st2.json
3f2739c6d99fa3b39e94859385d773626e66a5a2a4cfd8c4f5b9347bd64c4ecb  hilfs/diag-vergleich-st1.json
1947756e51ebabd7f38022d22aa08aef89b86f607146c9cdf5e914d745d1735b  hilfs/diag-vergleich-st2.json
83476e6888f4b1e69481005b3c1aa6c4d17ad3bb88667eecdda6d6a1f6e32189  hilfs/anhang-k0.jq
9d9fda02278c682f90c9a306d55e51c83af20577010f6cc09f67e44a74e62866  hilfs/laufzeiten.sh
```

- Nicht benutzt: hilfs/v4-neu.sh (Auswertung des Suchbereichs, nach Abbruch nicht gestartet).

## 7 Einfach gesagt

Wir wollten pruefen, ob sich die stillen Stellen eines grossen Q-Balls vorhersagen lassen wie die Sprossen einer
Leiter. Vorher musste ein Rundungsproblem der alten Rechnung behoben werden: Tief im Ball ist das zweite Feld so
winzig, dass der Computer dort nur Rauschen sieht, und ab Radius 40 verdarb das das Vorzeichen der Messgroesse. Die
Reparatur war, dieses winzige Feld dort auf null zu setzen. Bevor die Vorhersage zaehlen durfte, musste die reparierte
Rechnung die 88 schon bekannten Stellen unveraendert wiederfinden. Die Stellen liegen tatsaechlich genau dort, wo sie
waren. Aber die Reparatur dreht auf einigen Kurven das Vorzeichen der Messgroesse um und erzeugt neun Scheinwechsel,
die keine echten Stellen sind; die Zaehlung stimmt nicht mehr. Nach den vorab festgelegten Regeln ist die reparierte
Rechnung damit nicht auswertbar, und die Vorhersage bleibt ungeprueft. Gelernt haben wir, dass das winzige Feld im
Inneren das Vorzeichen der Messgroesse festlegt; eine bessere Reparatur muss diese Festlegung erhalten.

## Anhang B: K0 je bekannter Stelle (88)

- Nr, k, Paar und R aus Runde 18. Umlauf: Zellen-Umlauf Runde 18 / neu, je Stufe. Interp.: max |d omega^2|, |d rho| der
  interpolierten Lage neu gegen Runde 18 ueber beide Stufen (0 = bitgleich). Newton: max |d omega^2|, |d rho| der
  Newton-Wurzel neu gegen alt ueber beide Stufen. sigma2/sigma1: neu, Maximum beider Stufen. Maske: maskierte Punkte des
  Ankerprofils (Stufe 1).

| Nr | k | Paar | R | Umlauf St1 alt / neu | Umlauf St2 alt / neu | Interp. max | Newton max | sigma2/sigma1 | Maske |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 24 | 3.21 | -1 / -1 | -1 / -1 | 0 | 0 | 2.5e-13 | 0 |
| 2 | 0 | 42 | 5.76 | 1 / 1 | 1 / 1 | 0 | 0 | 4.5e-13 | 0 |
| 3 | 1 | 43 | 5.92 | 1 / 1 | 1 / 1 | 0 | 0 | 1.1e-12 | 0 |
| 4 | 0 | 49 | 8.21 | -1 / -1 | -1 / -1 | 0 | 0 | 5.4e-13 | 0 |
| 5 | 1 | 50 | 8.4 | -1 / -1 | -1 / -1 | 0 | 0 | 2.2e-12 | 0 |
| 6 | 2 | 51 | 9.25 | -1 / -1 | -1 / -1 | 0 | 0 | 2.9e-12 | 0 |
| 7 | 0 | 54 | 10.64 | 1 / 1 | 1 / 1 | 0 | 0 | 1.9e-12 | 0 |
| 8 | 1 | 54 | 10.68 | 1 / 1 | 1 / 1 | 0 | 0 | 4.2e-12 | 0 |
| 9 | 2 | 56 | 11.81 | 1 / 1 | 1 / 1 | 0 | 0 | 8.2e-12 | 0 |
| 10 | 3 | 58 | 12.56 | 1 / 1 | 1 / 1 | 0 | 0 | 4.9e-12 | 0 |
| 11 | 1 | 58 | 12.89 | -1 / -1 | -1 / -1 | 0 | 0 | 6e-12 | 0 |
| 12 | 0 | 59 | 13.06 | -1 / -1 | -1 / -1 | 0 | 0 | 3.6e-12 | 0 |
| 13 | 2 | 61 | 14.19 | -1 / -1 | -1 / -1 | 0 | 0 | 1e-11 | 0 |
| 14 | 1 | 62 | 15.06 | 1 / 1 | 1 / 1 | 0 | 0 | 2.7e-12 | 0 |
| 15 | 3 | 63 | 15.16 | -1 / -1 | -1 / -1 | 0 | 0 | 4.5e-12 | 0 |
| 16 | 0 | 63 | 15.48 | 1 / 1 | 1 / 1 | 0 | 0 | 6.4e-12 | 0 |
| 17 | 2 | 65 | 16.47 | 1 / 1 | 1 / 1 | 0 | 0 | 1.1e-11 | 0 |
| 18 | 1 | 67 | 17.21 | -1 / -1 | -1 / -1 | 0 | 0 | 1.1e-11 | 0 |
| 19 | 3 | 67 | 17.6 | 1 / 1 | 1 / 1 | 0 | 0 | 1.7e-11 | 0 |
| 20 | 0 | 68 | 17.9 | -1 / -1 | -1 / -1 | 0 | 0 | 4.1e-12 | 0 |
| 21 | 4 | 69 | 18.49 | 1 / 1 | 1 / 1 | 0 | 0 | 1.1e-12 | 0 |
| 22 | 2 | 70 | 18.71 | -1 / -1 | -1 / -1 | 0 | 0 | 1.1e-11 | 0 |
| 23 | 1 | 71 | 19.35 | 1 / 1 | 1 / 1 | 0 | 0 | 1.1e-11 | 0 |
| 24 | 3 | 72 | 19.94 | -1 / -1 | -1 / -1 | 0 | 0 | 4.2e-12 | 0 |
| 25 | 0 | 73 | 20.31 | 1 / 1 | 1 / 1 | 0 | 0 | 1.8e-12 | 0 |
| 26 | 2 | 74 | 20.91 | 1 / 1 | 1 / 1 | 0 | 0 | 2.8e-11 | 0 |
| 27 | 4 | 74 | 20.97 | -1 / -1 | -1 / -1 | 0 | 0 | 1.4e-11 | 0 |
| 28 | 1 | 75 | 21.48 | -1 / -1 | -1 / -1 | 0 | 0 | 2.3e-11 | 0 |
| 29 | 5 | 76 | 21.82 | -1 / -1 | -1 / -1 | 0 | 0 | 3.3e-12 | 0 |
| 30 | 3 | 76 | 22.23 | 1 / 1 | 1 / 1 | 0 | 0 | 6.3e-12 | 0 |
| 31 | 0 | 77 | 22.72 | -1 / -1 | -1 / -1 | 0 | 0 | 1.4e-12 | 0 |
| 32 | 2 | 78 | 23.1 | -1 / -1 | -1 / -1 | 0 | 0 | 2.3e-11 | 0 |
| 33 | 4 | 79 | 23.36 | 1 / 1 | 1 / 1 | 0 | 0 | 7.4e-12 | 0 |
| 34 | 1 | 79 | 23.61 | 1 / 1 | 1 / 1 | 0 | 0 | 6.3e-11 | 0 |
| 35 | 5 | 81 | 24.32 | 1 / 1 | 1 / 1 | 0 | 0 | 2.6e-11 | 0 |
| 36 | 3 | 81 | 24.49 | -1 / -1 | -1 / -1 | 0 | 0 | 2.6e-11 | 0 |
| 37 | 0 | 82 | 25.13 | 1 / 1 | 1 / 1 | 0 | 0 | 1.8e-11 | 0 |
| 38 | 6 | 82 | 25.13 | 1 / 1 | 1 / 1 | 0 | 0 | 1e-11 | 0 |
| 39 | 2 | 82 | 25.27 | 1 / 1 | 1 / 1 | 0 | 0 | 2.9e-11 | 0 |
| 40 | 4 | 83 | 25.7 | -1 / -1 | -1 / -1 | 0 | 0 | 4e-11 | 0 |
| 41 | 1 | 83 | 25.73 | -1 / -1 | -1 / -1 | 0 | 0 | 2.8e-11 | 0 |
| 42 | 3 | 85 | 26.71 | 1 / 1 | 1 / 1 | 3.8e-15 | 4.2e-15 | 2.7e-11 | 167 |
| 43 | 5 | 85 | 26.75 | -1 / -1 | -1 / -1 | 8.9e-15 | 10e-15 | 1.8e-11 | 167 |
| 44 | 2 | 87 | 27.42 | -1 / -1 | -1 / -1 | 2.2e-16 | 6.7e-16 | 8.6e-12 | 315 |
| 45 | 0 | 87 | 27.54 | -1 / -1 | -1 / -1 | 6e-11 | 3.9e-14 | 1.3e-11 | 315 |
| 46 | 6 | 87 | 27.66 | -1 / -1 | -1 / -1 | 1.4e-14 | 8.9e-15 | 1.3e-11 | 315 |
| 47 | 1 | 87 | 27.84 | 1 / 1 | 1 / 1 | 2.7e-15 | 5.1e-15 | 5.4e-11 | 315 |
| 48 | 4 | 88 | 27.99 | 1 / 1 | 1 / 1 | 8e-15 | 9.1e-15 | 5.5e-11 | 378 |
| 49 | 7 | 89 | 28.45 | -1 / 1 | -1 / 1 | 1.6e-14 | 4.2e-15 | 3.6e-12 | 439 |
| 50 | 3 | 90 | 28.92 | -1 / -1 | -1 / -1 | 1.1e-15 | 2e-15 | 3.7e-11 | 498 |
| 51 | 5 | 90 | 29.12 | 1 / -1 | 1 / -1 | 9.1e-13 | 1.8e-15 | 2.9e-11 | 498 |
| 52 | 2 | 91 | 29.57 | 1 / 1 | 1 / 1 | 4e-15 | 1e-13 | 3.5e-11 | 555 |
| 53 | 0 | 92 | 29.95 | 1 / 1 | 1 / 1 | 6.2e-12 | 1.4e-15 | 1.1e-11 | 611 |
| 54 | 1 | 92 | 29.96 | -1 / -1 | -1 / -1 | 5.6e-15 | 1.1e-14 | 6.1e-11 | 611 |
| 55 | 6 | 92 | 30.12 | 1 / -1 | 1 / -1 | 2.4e-15 | 8.9e-16 | 1.2e-11 | 611 |
| 56 | 4 | 92 | 30.25 | -1 / -1 | -1 / -1 | 1.2e-14 | 4.7e-15 | 2.6e-11 | 611 |
| 57 | 7 | 94 | 31 | 1 / -1 | 1 / -1 | 8.9e-16 | 1.2e-14 | 2e-11 | 722 |
| 58 | 3 | 94 | 31.11 | 1 / 1 | 1 / 1 | 2.9e-15 | 2.3e-15 | 4.3e-11 | 722 |
| 59 | 5 | 95 | 31.44 | -1 / 1 | -1 / 1 | 6.7e-16 | 3.6e-15 | 4.7e-11 | 777 |
| 60 | 2 | 95 | 31.71 | -1 / -1 | -1 / -1 | 5.1e-15 | 9.3e-15 | 6e-11 | 777 |
| 61 | 1 | 96 | 32.07 | 1 / 1 | 1 / 1 | 6.4e-15 | 9.3e-14 | 5.6e-11 | 831 |
| 62 | 0 | 96 | 32.37 | -1 / -1 | -1 / -1 | 1.4e-10 | 8.7e-14 | 5.6e-12 | 831 |
| 63 | 4 | 97 | 32.49 | 1 / -1 | 1 / -1 | 4.4e-15 | 1.1e-15 | 5.6e-11 | 884 |
| 64 | 6 | 97 | 32.51 | -1 / 1 | -1 / 1 | 6.2e-15 | 6e-15 | 3.4e-11 | 884 |
| 65 | 3 | 98 | 33.29 | -1 / -1 | -1 / -1 | 1.3e-14 | 2.3e-15 | 6.6e-12 | 938 |
| 66 | 7 | 99 | 33.47 | -1 / -1 | -1 / -1 | 4e-15 | 3.8e-15 | 3.6e-11 | 991 |
| 67 | 5 | 99 | 33.74 | 1 / -1 | 1 / -1 | 2e-15 | 5.3e-15 | 2.9e-11 | 991 |
| 68 | 2 | 99 | 33.85 | 1 / 1 | 1 / 1 | 4.8e-15 | 8.8e-15 | 8.4e-12 | 991 |
| 69 | 1 | 100 | 34.18 | -1 / -1 | -1 / -1 | 6.2e-15 | 1.2e-14 | 5.5e-11 | 1044 |
| 70 | 8 | 100 | 34.33 | -1 / -1 | -1 / -1 | 1.6e-14 | 8.2e-15 | 4.5e-11 | 1044 |
| 71 | 4 | 101 | 34.71 | -1 / 1 | -1 / 1 | 4.9e-15 | 2e-15 | 4.3e-11 | 1096 |
| 72 | 0 | 101 | 34.77 | 1 / 1 | 1 / 1 | 1.5e-10 | 3.3e-14 | 2.2e-11 | 1096 |
| 73 | 6 | 101 | 34.87 | 1 / 1 | 1 / 1 | 3e-14 | 4e-15 | 6.4e-11 | 1096 |
| 74 | 3 | 103 | 35.45 | 1 / -1 | 1 / -1 | 2e-15 | 3.3e-16 | 6.8e-12 | 1201 |
| 75 | 7 | 103 | 35.89 | 1 / 1 | 1 / 1 | 6e-15 | 4.9e-15 | 5e-11 | 1201 |
| 76 | 2 | 104 | 35.98 | -1 / -1 | -1 / -1 | 3.6e-15 | 7.4e-14 | 3.1e-11 | 1253 |
| 77 | 5 | 104 | 36.01 | -1 / 1 | -1 / 1 | 4.7e-15 | 2.2e-15 | 4.5e-11 | 1253 |
| 78 | 1 | 104 | 36.29 | 1 / 1 | 1 / 1 | 5.9e-15 | 9.5e-14 | 2e-10 | 1253 |
| 79 | 8 | 105 | 36.82 | 1 / -1 | 1 / -1 | 8.8e-13 | 5.1e-15 | 4.9e-11 | 1306 |
| 80 | 4 | 105 | 36.92 | 1 / -1 | 1 / -1 | 6.2e-15 | 3.6e-15 | 7.3e-11 | 1306 |
| 81 | 0 | 106 | 37.18 | -1 / -1 | -1 / -1 | 1.1e-10 | 7e-14 | 2.2e-11 | 1357 |
| 82 | 6 | 106 | 37.19 | -1 / -1 | -1 / -1 | 1.1e-15 | 1.8e-15 | 4.9e-11 | 1357 |
| 83 | 3 | 107 | 37.61 | -1 / 1 | -1 / 1 | 1.6e-15 | 1.8e-15 | 3.4e-11 | 1409 |
| 84 | 9 | 107 | 37.65 | 1 / -1 | 1 / -1 | 5.5e-14 | 4.7e-15 | 3.2e-11 | 1409 |
| 85 | 2 | 108 | 38.11 | 1 / 1 | 1 / 1 | 3.1e-15 | 5.1e-15 | 5e-11 | 1461 |
| 86 | 5 | 108 | 38.26 | 1 / 1 | 1 / 1 | 1.1e-14 | 6.7e-16 | 3.1e-11 | 1461 |
| 87 | 7 | 108 | 38.27 | -1 / -1 | -1 / -1 | 9.5e-15 | 7.3e-15 | 2.9e-11 | 1461 |
| 88 | 1 | 108 | 38.4 | -1 / -1 | -1 / -1 | 5.1e-15 | 9.8e-15 | 1e-10 | 1461 |
