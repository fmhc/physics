# LIFE-FCC-1: Ergebnis (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 07:59:00 CEST, Plantext ab 08:15 CEST.
  - Rauchlaeufe: Kontrolle 06:15:35 bis 06:15:37 UTC, rauch1 (20 Stichprobenregeln) 06:17:30 bis 06:17:31 UTC.
  - Eingefroren 08:18:29 CEST: PLAN.md.eingefroren-20261004-081829 und code/life_fcc.py.eingefroren-20261004-081829.
  - auswertung.py eingefroren 08:30:11 CEST (code/auswertung.py.eingefroren-20261004-083011), vor jeder Sicht auf
    Hauptergebnisse. Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe:
    - Kontrolle 06:18:35 bis 06:18:37 UTC
    - Stufe 1 06:18:41 UTC; alle 7098 Regeln geschrieben bis 06:21:27 UTC. Danach hing das Skript bis zur 600-s-Kappe
      (06:28:41 UTC, rc = 1), Selbstanzeige 1.
    - Stufe 2 06:30:17 bis 06:39:18 (Block a) und 06:39:26 bis 06:48:27 UTC (Block b)
    - Zusatz S leer 06:48:39 bis 06:48:41 UTC; Auswertung 06:48:41 bis 06:48:59 UTC
  - Nachtrag, beschreibend und nicht geurteilt: Rest von Stufe 2, 06:49:07 bis 06:49:48 UTC (Abschnitt 5.3).
  - Dazu zwei Probelaeufe von auswertung.py auf Rauchdaten vor deren Einfrieren (06:29:10 und 06:29:37 bis 06:29:42 UTC,
    Selbstanzeige 4). Alle Laeufe auf Spur cpu7, nacheinander. Text ab 08:51 CEST.
- **Code:** Nach dem Einfrieren ist life_fcc.py nur in einer Zeile geaendert (Selbstanzeige 1). auswertung.py ist
  unveraendert. Lokal, eingefroren bzw. berichtigt und auf der .69 haben beide dieselbe sha256 (Abschnitt 8).
- Alles ist synthetische Gitterrechnung (numpy/scipy, ganzzahlig, exakt). Keine Messdaten, keine
  Messdatenbestaetigung.
- **Kennzeichen:**
  - [E] hier gerechnet; [M] eigene Mathematik; [F] Festlegung im Plan
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher; kein Abruf
  - [H] Hypothese; [S] an der Quelle gelesen (hier keine)

## 1. Ergebnis zuerst

1. **Kein Gleiter [E].** In keiner der 7098 Intervallregeln ist aus Zufallsstarts ein bewegtes Muster entstanden,
   weder als ganzes Muster noch als abgetrenntes Objekt.
   - Stufe 1: alle 7098 Regeln mit je 24 Saaten (Wuerfel 5^3, 63 Knoten), 170 352 Laeufe bis 256 Schritte, dazu 1 086
     Einzellaeufe abgetrennter Haufen.
   - Stufe 2 (geurteilt): 1 455 der 1 788 Kandidatenregeln mit je 96 Saaten, Startbereiche bis 9^3 (365 Knoten):
     139 680 Laeufe, 11 642 Einzellaeufe.
   - Nachtrag, nicht geurteilt (5.3): die uebrigen 333 Kandidaten, 31 968 Laeufe; auch dort kein Gleiter. Stufe 2 ist
     damit vollstaendig, zusammen 342 000 Saatlaeufe in den 7098 Regeln ohne Gleiter (dazu 1 872 im Zusatz S leer,
     3.4, ebenfalls ohne).
   - Keine Zeitkappe wurde erreicht; jeder Lauf endete durch Aussterben, Groesse, Formwiederkehr oder T.
   - Der Gleiterpfad selbst arbeitet. Die eingefrorene Durchgangsprobe (Teil von LF0) fand 12 von 12 eingesetzten
     Kunst-Gleitern. Es waren drei Typen (p = 1 <110>, p = 3 <111>, p = 4 <100>); p, d, Richtung und Tempo stimmten
     jeweils.
2. **Der Regelraum zerfaellt scharf an b1 (kleinste Geburtszahl) [E, M]:**
   - b1 = 1 und b1 = 2 (2 093 Regeln): jede einzelne Saat waechst ueber 600 Knoten (50 232 von 50 232). Fuer b1 = 1 ist
     das ein Satz (M1); dort ist es nach hoechstens 7 Schritten so weit.
   - b1 = 3 (910 Regeln): 853 wachsen; von den uebrigen 57 sterben 30 aus, 26 enden als Oszillatoren, eine erstarrt.
   - b1 >= 4 (4 095 Regeln): In Stufe 1 waechst keine einzige Saat. Die Muster sterben aus, erstarren, blinken
     (Perioden bis 210) oder brodeln in einem begrenzten Gebiet ("offen", 100 Regeln, alle mit b1 = 4 oder 5).
   - Erst aus den groessten Startbereichen (9^3) wachsen in Stufe 2 auch b1 = 4-Regeln (2 628 Saaten). Bei b1 >= 5
     waechst in keiner Stufe etwas.
   - Fuer b1 >= 7 ist "kein Wachstum, kein Gleiter" ein Satz (M4, Huellenargument).
3. **Lichtkegel des fcc-Netzes [M]:** Jeder Gleiter muesste d/p im Kuboktaeder K erfuellen. Die Hoechstgeschwindigkeit
   in Einheiten c = eine Nachbarkante je Schritt:
   - <110> (Nachbarrichtungen): 1 c
   - <111> (Raumdiagonalen): 0,816 c
   - <100> (Wuerfelachsen): 0,707 c
   - Gerechnet bestaetigt [E]: Die Kugel um einen Knoten nach t Schritten ist genau {K-Norm <= t}
     (13, 55, 147, 309, 561, 923 Knoten).
4. **Urteile:** LF0 eingetroffen, LF1 nicht eingetroffen, LF2 und LF3 nicht auswertbar (bedingt auf Gleiter).
   - Nur auf Stufe 1, also im urspruenglichen Umfang der Karte: dieselben Urteile.
   - Mit dem Nachtrag (Stufe 2 vollstaendig) aendert sich nichts.
5. **Bedeutung, wie auf der Karte vorab festgelegt:** "LF1 verfehlt: Auch 12 Nachbarn reichen in der Intervallklasse
   nicht; klassische Gleiter brauchen dann andere Regelformen oder mehr Zustaende."
   - Zusatz [M]: Anders als auf dem Diamantnetz sind auf fcc die isotropen (unter Oh gleichen) Regeln viel reicher als
     die aussen-totalistischen. Zwei lebende Nachbarn koennen dort im Winkel 60, 90, 120 oder 180 Grad liegen, und Oh
     unterscheidet diese Lagen.
   - Gesucht ist also nur in einem kleinen Teil der richtungsgleichen Regeln (Abschnitt 7).

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 7 und 4.1 durch code/auswertung.py (eingefroren); Werte in lauf-69/auswertung.json.
Keine Sperre: LF0 und Z0 bis Z4 bestanden, Stufe 1 vollstaendig (7098 x 24).

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | nur Stufe 1 | Kennzahlen |
|---|---|---|---|---|---|
| LF0 | Kontrolle: Gitter korrekt (12 Nachbarn); die Durchgangsprobe mit Kunst-Gleitern findet alle | 90 % | **eingetroffen** | (gleich) | 256/256 Knoten mit Grad 12, 0 Schluesselabweichungen, Schalen 12/6/24/12, Graphabstand = K-Norm an 309 Knoten; Kunstfolgen 7/7, Kennung 100/100 verschiebungsfrei, Zerlegung 2 bzw. 1; Durchgangsprobe 12/12 Kunst-Gleiter (3 Typen x 4 Saaten) |
| LF1 | [H] Mindestens eine Intervallregel hat einen Gleiter, der aus Zufallsstarts entsteht | 60 % | **nicht eingetroffen** (Vermerk: Stufe 2 zu 1 455 von 1 788 Kandidaten gerechnet) | nicht eingetroffen | 0 Gleiter in 0 Regeln; 310 032 Saatlaeufe, 12 728 Einzellaeufe |
| LF2 | [H] Falls Gleiter gefunden werden: Alle sind hoechstens halb so schnell wie die Lichtkegelgrenze ihrer Richtung | 60 % | **nicht auswertbar** | nicht auswertbar | keine Gleiter (bedingte Vorhersage) |
| LF3 | [H] Falls Gleiter gefunden werden: Es gibt mehr als eine Gleiterform (nicht nur eine Regel mit einem Gleiter) | 50 % | **nicht auswertbar** | nicht auswertbar | keine Gleiter (bedingte Vorhersage) |

- **Kartenwortlaut:** Die Urteile sind in beiden Lesarten von LF3 (Bahnen bzw. Paare Regel/Bahn, K1) gleich, weil es
  keine Gleiter gibt. Kein Kartenpunkt aendert ein Urteil.
- **Vermerk LF1:** Mit dem Nachtrag 5.3 sind auch die 333 fehlenden Kandidaten gerechnet, ohne Gleiter. Das Urteil
  bleibt das eingefrorene.

**Eigene Vorhersagen** (PLAN Abschnitt 9, vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. | Ergebnis |
|---|---|---|---|
| A1 | Z1 haelt (B1-Regeln wachsen) | 99 % | **eingetroffen**: 1 092 Regeln, 26 208/26 208 Saaten gross, nach hoechstens 7 Schritten (Mittel 4,7) |
| A2 | Z2 haelt (S = [0..12]: kein Oszillator, kein Gleiter) | 99 % | **eingetroffen**: 45 Regeln Stilleben, 33 Wachstum, kein Oszillator oder Gleiter, auch nicht unter den Objekten |
| A3 | Z4 haelt (b1 >= 7: kein Wachstum, kein Gleiter) | 99 % | **eingetroffen**: 1 911 Regeln in Stufe 1 und 245 in Stufe 2 ohne gross-Saat und ohne Gleiter |
| A4 | LF1 eingetroffen | 60 % | **nicht eingetroffen** |
| A5 | Gleiter nur bei b1 in {3, 4} | 50 % | nicht auswertbar |
| A6 | LF2 eingetroffen | 65 % | nicht auswertbar |
| A7 | LF3 eingetroffen | 55 % | nicht auswertbar |
| A8 | Schnellste laengs <110> | 40 % | nicht auswertbar |

## 3. Tabellen [E]

### 3.1 Regelklassen nach b1 (Stufe 1, 24 Saaten je Regel; Bild lauf-69/klassenkarte.png)

| b1 | Regeln | Wachstum | offen | Oszillator | Stilleben | ausgestorben | Gleiter |
|---|---|---|---|---|---|---|---|
| 1 | 1 092 | 1 092 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 001 | 1 001 | 0 | 0 | 0 | 0 | 0 |
| 3 | 910 | 853 | 0 | 26 | 1 | 30 | 0 |
| 4 | 819 | 0 | 93 | 366 | 159 | 201 | 0 |
| 5 | 728 | 0 | 7 | 232 | 202 | 287 | 0 |
| 6 | 637 | 0 | 0 | 181 | 197 | 259 | 0 |
| 7 | 546 | 0 | 0 | 149 | 166 | 231 | 0 |
| 8 | 455 | 0 | 0 | 109 | 151 | 195 | 0 |
| 9 | 364 | 0 | 0 | 81 | 123 | 160 | 0 |
| 10 | 273 | 0 | 0 | 30 | 114 | 129 | 0 |
| 11 | 182 | 0 | 0 | 0 | 98 | 84 | 0 |
| 12 | 91 | 0 | 0 | 0 | 49 | 42 | 0 |
| **Summe** | **7 098** | **2 946** | **100** | **1 174** | **1 260** | **1 618** | **0** |

- Regelklasse nach Vorrang (PLAN Abschnitt 5): Gleiter > Wachstum > offen > Oszillator > Stilleben > ausgestorben.
- **b1 = 3, nicht wachsend (57):**
  - Ausgestorben (30): B3/S3, S4, S4-5, S5, S5-6, S5-7, S6, S6-7, S6-8, S6-9 und alle B3/S[s1..s2] mit s1 >= 7 ausser
    S7.
  - Stilleben (1): B3/S0.
  - Oszillator (26): B3/S1, S2, S4-6, S5-8 bis S5-12, S6-10 bis S6-12, S7; dazu 14 Regeln B3-4 mit s1 >= 7 (S7, S7-8,
    S8 bis S8-12, S9 bis S9-12, S11, S11-12, S12).
  - In den Oszillator-Regeln ueberleben nur 1 bis 9 von 24 Saaten; der Rest stirbt aus.
- **"offen" (100):** B4-b2 mit S0-3 bis S0-8, S1-4 bis S1-8 und S2-6 bis S2-8 (93 Regeln); dazu B5-b2/S0-5 und
  B5-9/S0-6 (7 Regeln). Dort brodelt ein begrenztes Gebiet ohne Wiederkehr in 256 + 128 Schritten.
  - Die abgetrennten Haufen dieser Regeln (1 042 Verweise aus Pruefpunkten und Enden) enden im Einzellauf zu 904
    wieder offen, sonst als Oszillator (74), Stilleben (59) oder tot (5).
- **Saatklassen Stufe 1 (170 352):** tot 58 480, Stilleben 34 500, Oszillator 11 119, gross 65 168 (nur b1 <= 3), offen
  1 085, Gleiter 0.
  - Groesstes Endmuster ausserhalb von b1 = 1: 562 Knoten.
  - Kein Lauf erreichte eine Kappe: groesste Arbeit 366 297 von 1 500 000 Knotenschritten (Stapel) bzw. 175 563 von
    600 000 (Objekte).

### 3.2 Oszillatorperioden (Stufe 1, ganze Muster, 11 119 Saaten)

| p | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | uebrige bis 30 | 31 bis 99 | ab 100 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Saaten | 7 959 | 356 | 1 860 | 109 | 262 | 148 | 91 | 68 | 220 | 40 | 6 |

- Laengste Perioden: 210 (B4-12/S1-8), 186 (B3-8/S7-10), 143 (B4-12/S1-7), 132 (B4-11/S0-8), 121 (B4-8/S2-7) und
  107 (B4-9/S1-7).
- p = 2 allein macht 72 % aus. In Stufe 2 reicht die laengste Periode bis 230.

### 3.3 Stufe 2 (Kandidaten nach der eingefrorenen Auswahlregel, je 96 Saaten)

- **Auswahl:** 1 788 Kandidaten, also Regeln mit mindestens einer klein-langlebigen Saat, ohne b1 = 1 und ohne
  S = [0..12].
  - In Rangfolge gerechnet: 1 455 in zwei Bloecken, darunter alle mit mindestens 2 klein-langlebigen Saaten.
  - Nicht erreicht: 333, alle mit genau einer solchen Saat (b1 = 3: 30, 4: 72, 5: 40, 6: 49, 7 bis 12: 142).
- **Gerechnet nach b1:** 3: 285, 4: 489, 5: 268, 6: 168, 7: 103, 8: 63, 9: 25, 10: 24, 11: 20, 12: 10.
- **Regelklassen Stufe 2:** Wachstum 606, offen 342, Oszillator 415, Stilleben 92, Gleiter 0.
  - "Wachstum" heisst hier oft Fuellen grosser Startbereiche. Deshalb stammt die Klassenkarte aus Stufe 1 (Plan).
- **Saatklassen (139 680):** tot 22 945, Stilleben 47 788, Oszillator 36 057, gross 18 804, offen 14 086, Gleiter 0.
  - 11 642 Einzellaeufe abgetrennter Haufen. Ein Haufen ueber 300 Knoten wird nicht allein gerechnet; solche
    Verweise gab es 2 525.
  - Keine Kappe erreicht: groesste Arbeit 3 567 790 von 6 000 000 (Stapel) bzw. 1 198 858 von 1 500 000 (Objekte).
- **Wachstum nach Startbereich bei b1 >= 4 [E]:**
  - Bereiche 5^3 und 7^3: keine Saat gross.
  - Bereich 9^3: 2 628 gross-Saaten, alle bei b1 = 4. Sie wachsen ueber die Startbereichsgroesse (365 Knoten) hinaus;
    das ist echtes Wachstum, kein Fuellen.
  - Bei b1 >= 5 waechst in keiner Stufe etwas.
  - b1 = 4 braucht also einen grossen Keim zum Wachsen [E]. Ob es eine scharfe kritische Keimgroesse gibt, ist offen
    [H].
- Laufzeit Stufe 2: 1 079 s fuer 1 455 Regeln; die teuersten waren die offen-Regeln B4-x/S0-x mit 3,4 bis 4,1 s.

### 3.4 Zusatz S leer (Kartenpunkt K2; beschreibend, nicht geurteilt)

- Die 78 Regeln B = [b1..b2] mit S leer ("Seeds"-Typ), je dieselben 24 Saaten wie Stufe 1, 1 872 Laeufe.
- b1 <= 2: alle 23 Regeln Wachstum. b1 = 3: 8 Wachstum, B3-4/S Oszillator, B3/S ausgestorben. b1 >= 4: alle 45
  ausgestorben.
- Kein Gleiter. Saatklassen: tot 1 158, gross 601, Oszillator 113.

### 3.5 Gleiterliste und Drehverhalten

- lauf-69/gleiter.json ist leer ([]), lauf-69/gleiter-uebersicht.tsv hat nur die Kopfzeile. Es gibt keine
  Geschwindigkeiten, Richtungen, Groessen oder Drehbilder.
  - lauf-69/geschwindigkeiten.png zeigt nur die drei Lichtkegelwerte und die Linie f = 0,5.
  - lauf-69/gleiter-3d.png zeigt ersatzweise eine kubische Zelle des fcc-Gitters (14 Knoten, Nachbarkanten). Eine
    Bildfolge ueber eine Periode gibt es mangels Gleiter nicht.
- **Zur Drehungsfrage der Karte bleibt nur der Schreibtisch [M, PLAN M6]:**
  - Bildet eine Drehung der Ordnung m Phase 0 auf Phase k ab und laesst sie d fest, so gilt m k = 0 mod p.
  - "Drehung um die Laufachse = halbe Periode" geht in O nur mit C2, C2' oder C4, in T nur mit den C2 um die
    Wuerfelachsen.
- **Die Drehpruefung selbst lief durch, in der Durchgangsprobe:**
  - Der Kunst-Gleiter p = 3 <111> (Schraube mit C3) hat 3 Selbstbilder in O, der Kunst-Gleiter p = 4 <100> (Schraube
    mit C4) 4 Selbstbilder, der reine Verschiebungs-Gleiter p = 1 eines.
  - Das ist genau die eingebaute Symmetrie, die Pruefung erkennt also Phasenversatz und Drehachse.

## 4. Kartenpunkte (vor dem Einfrieren offengelegt) und was daraus wurde

- **K1 (LF3 mehrdeutig):** "mehr als eine Gleiterform (nicht nur eine Regel mit einem Gleiter)". Festgelegt: Form =
  Bahn unter Oh, Verschiebung und Phase, ueber alle Regeln; die Klammerlesart (Paare Regel/Bahn) als Nebenlesart.
  Ohne Gleiter folgenlos.
  - Nachtraegliche Beobachtung (Probelauf 4, nicht geurteilt): Die Bahnkennung haengt nur von der Gestalt ab. Zwei
    Kunst-Gleiter mit gleicher Gestalt, aber p = 1 bzw. p = 3, fielen in eine Bahn.
  - Fuer eine Folgekarte sollte die Form p und die Richtungsklasse mitfuehren.
- **K2 (Luecke der Regelklasse):** Die Intervallklasse hat S nie leer. Damit fehlen die "Seeds"-artigen Regeln, die in 2D
  besonders viele Raumschiffe tragen [L]. Als Zusatz gerechnet (3.4): kein Gleiter.
- **K3 (Bedeutung LF1):** "bewegte Teilchen mit Hoechstgeschwindigkeit" gelesen als "mit einer Hoechstgeschwindigkeit
  (Lichtkegel)"; LF1 nur nach Existenz geurteilt.
- **K4 (Drehungen):** Die Punktgruppe des fcc-Netzes ist Oh (48); die Karte nennt O (24) und T (12). Gebaut ist die
  Pruefung fuer alle 48, gemeldet getrennt fuer O, T und alle 48 (gleiter.json-Felder dreh24, dreh12_T, alle48).
- **K5:** Kein Kartenfehler gefunden. 2^26 und 78 x 91 = 7098 stimmen. Die richtungsabhaengige Lichtkegelgrenze der
  Karte ist richtig (M3); laengs <110> liegt sie genau bei einer Nachbarkante je Schritt.

## 5. Kontrollen, Nachtrag, Latten

### 5.1 Kontrollen (lauf-69/kontrolle.json, Hauptlauf; per jq/diff gleich dem Rauchlauf bis auf Laufzeit und PARAM N2_max)

- **LF0 (a) Gitter:**
  - Periodischer Kasten 8^3: 256 Knoten (Soll 4 L^3, L = 4), Grad 12 ueberall (Abstandsnachbarn mit Minimalbild).
  - An allen 256 Knoten: Schluessel-Nachbarn = Abstandsnachbarn = die 12 Vektoren (+-1, +-1, 0) und Vertauschungen.
  - Schalen 12, 6, 24, 12 bei Abstand^2 = 2, 4, 6, 8; Breitensuche bis 4 Schritte: 309 Knoten, Graphabstand = K-Norm
    ueberall.
- **LF0 (b) Kunstfolgen:** 7 von 7 mit richtiger Klasse, p und d erkannt.
  - Gleiter p = 3, d = (3,-1,2); Oszillator p = 4; Stilleben; Gleiter p = 1, d = (1,1,0)
  - Gleiter p = 5, d = (0,-2,2) nach 10 Zufalls-Vorlaufschritten
  - Gleiter p = 2, d = (-1,-1,0) nach 3; Gleiter p = 7, d = (2,2,-2) nach 5
  - Dazu Kennung verschiebungsfrei 100/100, Zerlegung 2 (getrennt) bzw. 1 (nah).
- **LF0 (c) Durchgangsprobe** (eingefroren, Teil des Urteils; Aufbau PLAN Abschnitt 7):
  - Typ p1_110: 4 von 4 Saaten mit Gleiter, alle p = 1, d = (1,1,0), v = 1 c, f = 1.
  - Typ p3_111: 4 von 4, alle p = 3, d = (2,2,2), v = 0,816 c, f = 1.
  - Typ p4_100: 4 von 4, alle p = 4, d = (0,0,4), v = 0,707 c, f = 1.
  - Je Typ: reine Laufsaat als "ganz", die drei gemischten Saaten (Laufsaat plus entfernter Block) als "objekt";
    alle geprueft.
  - Damit lief die ganze Kette (Stapel, Pruefpunkt-Zerlegung, Objektlaeufe, Gleiterpruefung, Drehverhalten, JSON)
    vor der Suche.
- **Z0:**
  - 1 568 Gleichverhaltensproben ohne Fehler: 8 Regeln x 4 Muster x (48 Elemente von Oh + 1 fcc-Verschiebung). Die
    Gruppe hat 48 Elemente, 24 in O, 12 in T.
  - Stapel = Einzeln: 120 von 120 (5 Regeln x 24 Saaten; Klasse, t, p, d und Endmuster gleich).
  - Lichtkegel B1-12/S0-12 aus einem Knoten: 13, 55, 147, 309, 561, 923 Knoten = Kugel {K-Norm <= t}, t = 1..6.
- **Z1:** 1 092 B1-Regeln, 26 208/26 208 Saaten gross, kein Gleiter.
- **Z2:** 78 Regeln mit S = [0..12]: nur Stilleben und Wachstum, kein Oszillator und kein Gleiter, auch nicht unter den
  Objekten.
- **Z3:** leer erfuellt (kein Gleiter).
- **Z4:** b1 >= 7: keine gross-Saat und kein Gleiter, 1 911 Regeln in Stufe 1 und 245 in Stufe 2.
- **Erkennung auf echten Daten:** Ueber dieselbe Formwiederkehr, die Gleiter erkennen wuerde (d != 0), wurden erkannt:
  - 11 119 + 36 057 Oszillatoren (Stufe 1 + 2) mit Perioden bis 210 bzw. 230
  - 34 500 + 47 788 Stilleben (Stufe 1 + 2)

### 5.2 Probelaeufe der Auswertung (vor ihrem Einfrieren, nur Rauchdaten)

- auswertung.py lief zweimal auf Rauchdaten:
  - rauch/test-ausw: 20 Stichprobenregeln, Gleiterpfad leer.
  - rauch/test-ausw2: dieselben, Regeln 0 und 355 durch Kunst-Laeufe ersetzt, per code/test_auswertung_gleiter.py.
- Beide liefen fehlerfrei. In test-ausw2 entstanden 4 Gleiter in 2 Bahnen, dazu Uebersicht, Geschwindigkeitsbild und
  3D-Bild. Die Sperre griff dort erwartungsgemaess, weil Stufe 1 unvollstaendig war.
- Dateien: rauch-69/test-ausw2/ (auswertung.json, gleiter-uebersicht.tsv, Bilder).

### 5.3 Nachtrag: Rest von Stufe 2 (nicht geurteilt)

- **Anlass:** Die zwei geplanten Bloecke erreichten 1 455 von 1 788 Kandidaten.
- **Aufbau:** Derselbe berichtigte Code im Modus stufe2. Die Ausgabedatei lauf/nachtrag-stufe2.jsonl begann als Kopie
  von stufe2.jsonl; das Skript ueberspringt dort schon gerechnete Regeln. Die ersten 1 455 Zeilen sind also die
  geurteilten (Indexfolge per sha256 gleich).
- **Ergebnis [E]:** 333 von 333 Regeln, 31 968 Saaten, 194 Einzellaeufe in 40 s: **0 Gleiter.**
  - Regelklassen: Oszillator 159, Stilleben 100, Wachstum 43, offen 30, ausgestorben 1.
- **Folge:** Stufe 2 ist im geplanten Umfang vollstaendig: 1 788 Regeln, 171 648 Saaten. Das Haupturteil bleibt das
  eingefrorene.

### 5.4 Latten (v3)

- **L1 (kann scheitern):** ja.
  - LF1 hatte einen offenen Ausgang; die Leitung schaetzte 60 %, ich auch. Ein einziger gepruefter Gleiter in 310 032
    Laeufen haette LF1 eingetroffen gemacht.
  - Gescheitert ist meine eigene Vorhersage A4.
  - Z1, Z2 und Z4 sind Saetze. Sie konnten nur durch Programmfehler scheitern.
- **L2 (Gegenprobe):**
  - Gitter gegen unabhaengige Abstandskonstruktion; Schalen und Graphabstand
  - Gleichverhalten unter 48 Symmetrien und Verschiebungen
  - Stapel gegen Einzellaeufe
  - Lichtkegel exakt nach M3
  - Z1, Z2 und Z4 als Saetze gegen die Rechnung
  - Durchgangsprobe mit drei Kunst-Gleitertypen vor der Suche
  - Stufe 2 als zweite, groessere Stichprobe mit anderen Saaten und groesseren Startbereichen
- **L3 (Numerik):** ganzzahlig und exakt; keine Rundung. Die Grenzen liegen im Suchumfang:
  - T = 256; Einzellaeufe 128
  - Groessen bis 600 bzw. 300 Knoten
  - 24 bzw. 96 Saaten je Regel, Startbereiche bis 9^3
  - Knotenschritt-Kappen, nirgends erreicht
  - Zerlegung bei R = 4,5; gross-Enden nicht zerlegt
- **L4 (schon bekannt):**
  - Leben in 3D auf dem kubischen Gitter mit 26 Nachbarn hat Gleiter (Bays ab 1987, z. B. Regeln 4555 und 5766) [L?].
  - Ob Bays oder andere fcc mit 12 Nachbarn (Rhombendodekaeder-Zellen) untersucht haben, weiss ich nicht [L?].
  - Fuer Conways Leben gelten c/2 orthogonal und c/4 diagonal als Hoechsttempo endlicher Raumschiffe [L].
  - M1 (B1 waechst) ist vermutlich Folklore; das Huellenargument M4 kenne ich nicht als Zitat [L?].
- **L5 (Messbezug):** keiner. Reine Modellfrage ueber entstehende Teilchen; kein Datenpfad.

## 6. Selbstanzeigen

1. **Programmfehler nach der letzten Regel (Stufe 1):**
   - In main stand fertige(aus) in der Listenbedingung von "rest = ...". Das las die 6-MB-Ausgabe je Regel neu ein.
   - Alle 7098 Zeilen waren um 06:21:27 UTC geschrieben (geprueft: 7098 Zeilen, 7098 verschiedene Indizes 0..7097,
     n_saaten = 24 ueberall).
   - Danach hing das Skript bis zur 600-s-Kappe des Starters (rc = 1). Die Spur cpu7 war dadurch gut 7 min belegt.
   - Berichtigt nach dem Einfrieren in genau dieser Zeile (diff in EINGEFROREN-SHA256.txt beschrieben). Rechenkern,
     Saaten und Urteile sind unberuehrt. Stufe 2, Zusatz und Nachtrag liefen mit dem berichtigten Code.
2. **Revision N2 nach dem Rauchlauf (vor dem Einfrieren, PLAN 4.1):**
   - Die Obergrenze von 400 Stufe-2-Regeln fiel weg, weil Stufe 1 nur Minuten kostet.
   - Ich kannte dabei das Rauchergebnis: kein Gleiter in 20 Stichprobenregeln.
   - Auswahlregel, Rangfolge und Urteilsregeln blieben unveraendert.
3. **Abweichung von LIFE-DIAMANT-1 (im Plan festgelegt):** gross-Enden werden nicht zerlegt (Laufzeit).
   - Ein Gleiter, der sich aus einer Explosion loest, bevor das Muster 600 Knoten erreicht, und an keinem Pruefpunkt
     abgetrennt war, wird so nicht gefunden.
   - Bei b1 <= 2 explodiert jede Saat in hoechstens wenigen Schritten. Dort ist das die Luecke der Suche [H].
4. **auswertung.py nach dem Plan-Einfrieren geschrieben** (im Plan angekuendigt):
   - Eingefroren 08:30:11 CEST, nach zwei Probelaeufen auf Rauchdaten (5.2).
   - Fuer den Gleiterpfad schrieb ich dazu code/test_auswertung_gleiter.py; nicht eingefroren, nur Rauchdaten.
   - Vom Hauptlauf hatte ich bis dahin gesehen:
     - Zeilenzahlen (3735, 4418, 7098)
     - die Pruefung "7098 Indizes, n_saaten = 24"
     - die Endzeile des Stufe-1-Logs (rc = 1)
   - Klassen oder Gleiterzahlen hatte ich nicht gesehen.
5. **Stufe 2 im Urteil unvollstaendig** (1 455 von 1 788). Die zwei Bloecke standen so im Plan. Die fehlenden 333 hat
   der Nachtrag 5.3 gerechnet, ohne Gleiter; geurteilt ist ohne ihn.
6. **Bahnkennung nur nach Gestalt** (K1, Beobachtung in 5.2). Ohne Gleiter folgenlos; fuer Folgekarten aendern.
   - auswertung.json traegt per jq einen beschreibenden Block nachtrag_stufe2; die Urteile sind die der
     Maschinenfassung (auswertung.maschine.json).
7. **Lokal:** kein python, awk oder perl.
   - Benutzt: jq, sed, grep, sha256sum, date, ssh, scp; Dateibefehle cp, mv, mkdir, ls, cat, rm.
   - rm nur fuer meine eigene Zwischenkopie lauf-69/stufe2-zwischen.jsonl.
   - Ausserhalb der Liste als Filter: cut, diff, seq, tr, fold, head, tail, wc.
   - sort einmal mit LC_ALL=C.
   - Gewartet habe ich mit until-Schleifen (sleep 5 bis 10 s); ein einzelnes "sleep 45" lehnte das Werkzeug ab.
8. **Ablage:** Die Konsolenausgaben meiner Hintergrund-ssh-Aufrufe legt das Werkzeug selbst unter
   /tmp/claude-1000/.../tasks/ ab. Ich habe dort nichts geschrieben; alle Ergebnisse liegen im Kartenordner und auf der
   .69.
9. **Auf der .69 ausserhalb des Starters:** mkdir, cp, mv, ls (auch site-packages des venv, kein Interpreterstart),
   stat, wc, grep, head, tail, sha256sum, date.
   - Python lief nur ueber kleintest.sh, Spur cpu7, nie zwei Laeufe zugleich.
10. **Starts:** 12 insgesamt.
    - Rauch: Kontrolle, rauch1
    - Haupt: Kontrolle, Stufe 1, Stufe 2a, Stufe 2b, Zusatz S leer, Auswertung
    - Probe: zwei Laeufe auswertung.py, ein Lauf test_auswertung_gleiter.py
    - Nachtrag Stufe 2
    - Der laengste war Stufe 1 mit 600 s (Kappe, Selbstanzeige 1); Stufe 2a und 2b je 541 s.
11. **Reichweite:** Gesucht ist nur aus kleinen Zufallsstarts.
    - Nicht ausgeschlossen sind Gleiter,
      - die seltener als etwa 1 zu 100 Saaten je Regel entstehen,
      - die nur aus gebauten oder groesseren Startmustern entstehen,
      - die laenger als 256 Schritte zum Abloesen brauchen,
      - mit Perioden ueber 128 (Objekte) oder mit mehr als 300 Knoten.
    - Die Suche findet Gleiter; ihre Abwesenheit beweist sie nicht.
12. **Zeitbox:** Start 07:59:00, Abgabe vor 09:29 CEST.

## 7. Bedeutung

- **Zu Finns Frage (Game of Life auf der Tetraeder-Oktaeder-Packung):**
  - Gerechnet ist die einfachste Spielart: zwei Zustaende, die 12 naechsten Nachbarn, Regel nur nach der Nachbarzahl,
    Geburts- und Ueberlebenszahlen je ein zusammenhaengender Bereich.
  - Dann entstehen aus Zufallsstarts keine bewegten Teilchen. Es gibt drei Welten:
    - Explosion: alle Regeln mit b1 <= 2 und fast alle mit b1 = 3
    - Gebundenes: ab b1 = 4 kleine, gebundene Muster; sie erstarren, blinken (bis Periode 210) oder brodeln
      eingesperrt
    - Aussterben
  - Den Uebergang zwischen Explosion und Bindung macht die Regelklasse in einem Sprung von b1 = 3 auf b1 = 4 [E]. Ein
    "Rand des Chaos", auf dem in 2D die Gleiter leben, ist hier kaum besetzt [H].
  - Bei b1 = 3 ueberleben ausserhalb der Explosion nur 1 bis 9 von 24 Saaten, als Oszillatoren oder Stilleben; bei
    b1 = 4 waechst ein Muster nur aus grossen Keimen [E].
- **Warum vermutlich [H]:**
  - Ein Knoten ausserhalb der Huelle sieht hoechstens 6 lebende Nachbarn (M4). Ein Gleiter muss vorne gebaeren und
    hinten sterben.
  - Bei b1 <= 3 gebaert die ganze Front, das Muster explodiert. Bei b1 >= 4 braucht jede Frontgeburt eine dichte
    Vorderkante, die zufaellige Muster selten haben.
  - Zusammenhaengende Intervalle koennen "gebaere bei 3 und bei 5, aber nicht bei 4" nicht ausdruecken. Gerade solche
    Luecken tragen in 2D viele Raumschiffe [L?].
- **Was die Suche abdeckt [M]:**
  - Anders als auf dem Diamantnetz ist eine richtungsgleiche (Oh-invariante) Regel auf fcc nicht automatisch
    aussen-totalistisch.
  - Oh wirkt auf die 12 Nachbarn nicht transitiv auf die k-Teilmengen: Zwei Nachbarn liegen im Winkel 60, 90, 120 oder
    180 Grad.
  - Gerechnet ist also nur ein kleiner Teil, die Intervallklasse der totalistischen Regeln, dazu im Zusatz S leer.
- **Naechste Schritte [H], je eine Karte mit offenem Ausgang:**
  - (a) Nicht-Intervall-Regeln: B und S als beliebige Teilmengen, etwa die Nachbarschaft der Uebergangszone b1 = 3/4 mit
    Luecken in B.
  - (b) Isotrope, nicht totalistische Regeln auf fcc, die die Winkellage der Nachbarn unterscheiden.
  - (c) Mehr Zustaende ("Generations" mit Erholungszustaenden), in 2D leichte Gleitertraeger [L].
  - (d) Gezielte Kleinmuster-Suche in den Grenzregeln (alle zusammenhaengenden Muster bis etwa 8 Knoten) statt
    Zufallsstarts.
- **Zum Spin:** Klassisch ohne Vorzeichen -1, wie die Karte sagt. Das Gegenstueck mit Spin bleibt der
  Quanten-Zellautomat (QCA-TETRA-1).

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-081829, EINGEFROREN-SHA256.txt
- code/:
  - life_fcc.py: Gitter, Schritt, Stapellaeufe, Kennung, Zerlegung, Gleiter, Drehverhalten, Kontrolle, Bloecke
  - life_fcc.py.eingefroren-20261004-081829 (Einfrierstand) und life_fcc.py.berichtigt-20261004-083011 (= life_fcc.py)
  - auswertung.py und auswertung.py.eingefroren-20261004-083011: Urteile, Tabellen, Bilder
  - test_auswertung_gleiter.py: Probe des Gleiterpfads der Auswertung, nicht eingefroren
- lauf-69/:
  - auswertung.json (Format urteile/LF0..LF3/urteil, vermerk, werte; dazu Kontrollen, Zusammenfassung, Zusatz). Per jq
    ist nur der Block nachtrag_stufe2 ergaenzt; die unveraenderte Maschinenfassung liegt als auswertung.maschine.json
    bei (per diff bis auf diesen Block gleich).
  - regeln.tsv: alle 7098 Regeln mit Klassen beider Stufen
  - gleiter.json (leer) und gleiter-uebersicht.tsv (nur Kopf)
  - kontrolle.json, kontrolle.log
  - stufe1.jsonl (alle Regeln, Saaten kompakt [Klasse, t, Knoten, p, Gleiter]) und stufe1-a.log
  - stufe2.jsonl, stufe2-a.log, stufe2-b.log
  - zusatz-s-leer.jsonl und .log
  - nachtrag-stufe2.jsonl und .log
  - auswertung.log
  - Bilder: klassenkarte.png, geschwindigkeiten.png, gleiter-3d.png
- rauch-69/: kontrolle.json, rauch1.jsonl, test-ausw2/ (Probe der Auswertung)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde38-life-fcc/ (code/, rauch/, lauf/)
- **sha256** (lokal = .69, geprueft 08:50 CEST):
  - life_fcc.py (berichtigt) 30edb65192913d5dad7aa4bf1a2ecfe58000f5261dd04ad0aa0ea58cd5ba775a
  - life_fcc.py (eingefroren) 725dbe0b5961ec9752ec5496c29d17a583923173b3c9b9a603ee81151cd69a5e
  - auswertung.py aa1eb7a1e8e99b66e28a3ddfe1e7a833d48709fbd28203e85b99aa9160dc9753
  - PLAN.md 033d0f70473716af5c2e87a77773c11a3bc3b7d60d897d921508eee60a96f5e2
  - test_auswertung_gleiter.py dca5e9729db2f9cf3b8b42603bc17faa782e0e55a9125306be94bfc63af930eb

## 9. Einfach gesagt

Wir haben alle 7098 einfachen Ja/Nein-Spielregeln einer ueblichen Bauart auf dem Netz ausprobiert, in dem jeder Knoten
12 Nachbarn hat (das Knotennetz der Tetraeder-Oktaeder-Packung), und jede Regel mit 24 bis 96 zufaelligen Startmustern
laufen lassen. In keinem einzigen Fall ist ein Muster entstanden, das wie der Gleiter im Game of Life als Ganzes durchs
Netz wandert. Die Regeln teilen sich scharf: Genuegen fuer eine Geburt schon 1 bis 3 lebende Nachbarn, wuchert fast
alles; verlangt die Regel 4 oder mehr, bleiben die Muster klein, erstarren, blinken auf der Stelle oder brodeln
eingesperrt weiter. Bewegte "Teilchen" braeuchten gerade den schmalen Uebergang dazwischen, und den trifft diese
einfache Regelklasse offenbar nicht. Das ist ein Suchergebnis und kein Beweis; feinere Regeln, die auch auf die Lage der
Nachbarn achten, oder mehr Zustaende koennen es noch aendern.
