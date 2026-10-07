# HAGEDORN-2: Ergebnis (Runde 38)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 06:35:45 CEST, Plan eingefroren 06:52:33 CEST
  (PLAN.md.eingefroren-20261004-065233), Ende siehe Abschnitt 4 (date).
- Explorativ (v3). Alles ist synthetische Rechnung im Modell M1 (2D, U(S) = S - S^2 + S^3/2), keine
  Messdatenbestaetigung.
- Urteile mechanisch aus lauf-69/auswertung.json (code/auswertung2.py nach PLAN.md Abschnitt 3).
- Kennzeichen: [M] Mathematik/eigene Rechnung, [S] an der Quelle gelesen (hier keine), [L] Literatur aus dem
  Gedaechtnis, [L?] unsicher, [H] Hypothese.

## 1. Ergebnis

1. **Auch kurz vor der Duennwand-Grenze zerfallen die langen Ringe.**
   - Stabil sind nur m = 3 bei omega^2 = 0,51 bis 0,54 und m = 5 bei 0,51. Dort sind alle gezaehlten Eigenwerte
     fuer l = 0 bis 3m exakt reell.
   - m = 8 und m = 12 sind bei jedem omega^2 instabil, auch bei 0,51: Im Omega = 4,3e-4 (m = 8) und 4,8e-4 (m = 12).
   - **HZ1 nicht eingetroffen:** Bei 0,52 sind m = 5 (Im 8,6e-4) und m = 8 (Im 1,4e-3) instabil, nur m = 3 haelt.
2. **Es ist immer dieselbe Instabilitaet: der Ring beult sich langsam zur Ellipse aus.**
   - Instabil ist l = 2, bei m >= 8 manchmal auch l = 3, bei m = 12 und 0,55 auch l = 4. Alle hoeheren l bis 3m sind
     stabil.
   - Die Moden sind oszillierend (Re Omega 1,6e-3 bis 2,6e-2) und am Ring lokalisiert (Ringanteil 0,98 bis 0,99).
   - Die Rate faellt mit sinkendem omega^2 stetig, fuer m = 8 von 4,0e-3 (0,55) auf 4,3e-4 (0,51).
   - **HZ2 eingetroffen.**
3. **Muster [H, nach der Rechnung, nicht vorhergesagt]:** Ob ein Ring haelt, entscheidet offenbar sein
   Seitenverhaeltnis A = mittlerer Radius / Dicke (Halbwertsradien).
   - Stabil sind alle Ringe mit A <= 1,79, instabil alle mit A >= 1,99. Das gilt fuer alle 20 Profile hier und fuer
     m = 1, 2, 3 bei 0,55 aus HAGEDORN-1 (A = 0,88; 1,40; 1,99).
   - Bei 0,70 gilt es nicht mehr: Dort ist m = 1 mit A = 1,14 stark instabil (HAGEDORN-1). Das Muster beschreibt also
     nur den Duennwand-Bereich.
   - Duennwand-Naeherung [M]: Die Dicke ist sigma/eps, unabhaengig von m; der mittlere Radius ist ~ m/sqrt(eps).
     Mit A_c ~ 1,8 bis 2,0 folgt m_max ~ (0,61 bis 0,68)/sqrt(eps) [H].
   - Folge: Fuer jedes m gibt es nahe genug an der Grenze einen stabilen Ring. Er ist dann aber immer dick: Der Umfang
     ist hoechstens etwa 12 Dicken lang.
4. **HZ0 eingetroffen:** Der Anschluss an HAGEDORN-1 stimmt auf 1,4e-10 (m = 3) und 1,9e-11 (m = 5), trotz groeberem
   Gitter (h = 0,2 statt 0,1).
5. **HZ3 nicht auswertbar.** An keinem omega^2 sind drei m stabil (0,51: m = 3 und 5; 0,52 bis 0,54: nur m = 3).
   - Beschreibend gilt E ~ R ueber alle m mit Steigung 1,02 bis 1,19. Das war aus den Profilen vorab ableitbar
     (PLAN.md 0.3).

**Bedeutung (nach der Karte, vorab formuliert):** Es gilt der Fall "HZ1 verfehlt": "Grosse Ringe zerfallen auch dicht
an der Grenze. Der Ringturm ist kein String; Glied 7 bleibt bei Strings oder anderen Auswegen."
- Genauer [H]: Grosse Ringe gibt es stabil, aber nur dicke. Ein stabiler Ring ist nie ein langes, duennes Gebilde,
  laengs dessen viele Wellen Platz haben.
- Damit fehlt die Voraussetzung des Schreibtischs der Leitung (ein 1D-Objekt der Laenge L, viel laenger als dick, mit
  L ~ E). Eine Hagedorn-Dichte aus Ringschwingungen ist in diesem Modell nicht zu erwarten [H].
- Die Karte rechnet 2D; fuer dreidimensionale Tori sagt das nichts.

## 2. Urteile

Mechanisch aus lauf-69/auswertung.json (erstellt 2026-10-04T05:02:53Z).
- Kein Profil in der Grauzone, keine Zeile "nicht konvergiert", keine Randmode, kein ungepruefter Kandidat.
- Keine fehlende Zeile; alle 20 Profile mit allen l = 0 bis 3m.

| Nr | Vorhersage (Karte, kurz) | Wahrsch. | gemessen | Urteil | Bemerkung |
|---|---|---|---|---|---|
| HZ0 | Anschluss an HAGEDORN-1 bei 0,55, m = 3 und 5: max Im auf 1e-4 gleich | 85 % | Differenz 1,4e-10 (m = 3), 1,9e-11 (m = 5) | eingetroffen | nach Kartenwortlaut (l = 0 bis 3m) ebenso eingetroffen |
| HZ1 | [H] Bei 0,52 sind m = 3, 5, 8 stabil | 40 % | m = 3 stabil; m = 5: 8,61e-4 (l = 2); m = 8: 1,37e-3 (l = 2) | nicht eingetroffen | Dichteprobe (volles Spektrum auf h/2) bestaetigt alle drei Klassen |
| HZ2 | m = 3, 5, 8: max Im faellt von 0,55 bis 0,51 monoton (oder wird null) | 65 % | Folgen in Tabelle 3.1; kein Anstieg | eingetroffen | m = 3 wird bei 0,54 null, m = 5 bei 0,51, m = 8 faellt um Faktor 9 |
| HZ3 | [H] E ~ R auf stabilen Profilen, Steigung 1 +- 0,15 aus >= 3 stabilen m | 45 % | hoechstens 2 stabile m je omega^2 | nicht auswertbar | Steigung bei jeder Auswahl vorab ableitbar (PLAN.md 0.3) |

## 3. Tabellen

### 3.1 Groesstes Im Omega je Profil (l des Maximums), l = 0 bis 3m, Basisgitter h = 0,2

| omega^2 | m = 3 | m = 5 | m = 8 | m = 12 |
|---|---|---|---|---|
| 0,51 | stabil | stabil | 4,32e-4 (2) | 4,81e-4 (2) |
| 0,52 | stabil | 8,61e-4 (2) | 1,369e-3 (2) | 1,086e-3 (2) |
| 0,53 | stabil | 2,495e-3 (2) | 2,247e-3 (2) | 1,663e-3 (2) |
| 0,54 | stabil | 3,932e-3 (2) | 3,091e-3 (2) | 2,450e-3 (3) |
| 0,55 | 4,290e-3 (2) | 5,402e-3 (2) | 3,958e-3 (2) | 3,381e-3 (3) |

- "stabil": alle gezaehlten Eigenwerte exakt reell (max Im = 0).
- Instabile l je Zeile: nur l = 2; dazu l = 3 bei m = 8 (0,54 und 0,55) und m = 12 (0,52 bis 0,55); l = 4 bei m = 12
  und 0,55.
- Bilder: lauf-69/bild_max_im.png (max Im gegen omega^2 je m) und lauf-69/bild_im_l.png (Im je l gegen l/m).

### 3.2 Staerkste Instabilitaet je instabiler Zeile (Eigenwert, Ringanteil)

| Zeile | l | Omega | Ringanteil |
|---|---|---|---|
| m = 8, 0,51 | 2 | 0,002179 + 0,000432 i | 0,985 |
| m = 12, 0,51 | 2 | 0,001559 + 0,000481 i | 0,989 |
| m = 5, 0,52 | 2 | 0,006641 + 0,000861 i | 0,981 |
| m = 8, 0,52 | 2 | 0,004582 + 0,001369 i | 0,988 |
| m = 12, 0,52 | 2 | 0,003179 + 0,001086 i | 0,990 |
| m = 5, 0,53 | 2 | 0,010346 + 0,002495 i | 0,983 |
| m = 5, 0,54 | 2 | 0,014016 + 0,003932 i | 0,987 |
| m = 12, 0,54 | 3 | 0,011084 + 0,002450 i | 0,987 |
| m = 3, 0,55 | 2 | 0,025966 + 0,004290 i | 0,978 |
| m = 12, 0,55 | 3 | 0,013789 + 0,003381 i | 0,987 |

Alle Instabilitaeten sind oszillierend (komplexe Vierergruppen), Re Omega etwa 3- bis 9-mal so gross wie Im Omega.
Keine ist rein imaginaer.

### 3.3 Profile: E, R und Seitenverhaeltnis

R_max = Ort des Maximums von f (Urteilsgroesse wie HAGEDORN-1); R_i, R_a = Halbwertsradien von S = f^2;
A = (R_i + R_a)/2 / (R_a - R_i). Quelle: Schiessen (S) oder Duennwand-Newton (N, Versuch 2).

| omega^2 | m | Quelle | E | R_max | R_i | R_a | A | Klasse |
|---|---|---|---|---|---|---|---|---|
| 0,51 | 3 | N | 8017,9 | 46,10 | 17,17 | 52,42 | 0,99 | stabil |
| 0,51 | 5 | N | 12234,7 | 64,36 | 35,35 | 70,66 | 1,50 | stabil |
| 0,51 | 8 | N | 18916,9 | 93,15 | 64,24 | 99,58 | 2,32 | instabil |
| 0,51 | 12 | N | 28015,2 | 132,35 | 103,61 | 138,95 | 3,43 | instabil |
| 0,52 | 3 | S | 2743,95 | 26,62 | 14,20 | 31,77 | 1,31 | stabil |
| 0,52 | 5 | S | 4363,66 | 39,96 | 27,62 | 45,26 | 2,07 | instabil |
| 0,52 | 8 | S | 6863,08 | 60,56 | 48,42 | 66,08 | 3,24 | instabil |
| 0,52 | 12 | S | 10230,41 | 88,39 | 76,47 | 94,14 | 4,83 | instabil |
| 0,53 | 3 | S | 1508,79 | 19,66 | 12,48 | 24,17 | 1,57 | stabil |
| 0,53 | 5 | S | 2438,20 | 30,63 | 23,60 | 35,35 | 2,51 | instabil |
| 0,53 | 8 | S | 3858,28 | 47,49 | 40,68 | 52,45 | 3,96 | instabil |
| 0,53 | 12 | S | 5764,36 | 70,26 | 63,65 | 75,43 | 5,90 | instabil |
| 0,54 | 3 | S | 1001,21 | 16,14 | 11,31 | 20,06 | 1,79 | stabil |
| 0,54 | 5 | S | 1631,87 | 25,75 | 21,00 | 29,82 | 2,88 | instabil |
| 0,54 | 8 | S | 2590,52 | 40,49 | 35,84 | 44,68 | 4,56 | instabil |
| 0,54 | 12 | S | 3874,77 | 60,33 | 55,75 | 64,60 | 6,80 | instabil |
| 0,55 | 3 | S | 735,97 | 14,12 | 10,43 | 17,46 | 1,99 | instabil |
| 0,55 | 5 | S | 1205,82 | 22,82 | 19,15 | 26,23 | 3,20 | instabil |
| 0,55 | 8 | S | 1917,82 | 36,09 | 32,45 | 39,55 | 5,07 | instabil |
| 0,55 | 12 | S | 2870,57 | 53,90 | 50,29 | 57,40 | 7,57 | instabil |

- Die Dicke R_a - R_i ist bei festem omega^2 fast gleich fuer alle m (35,3; 17,6; 11,8; 8,8; 7,1), wie die
  Duennwand-Formel sigma/eps sagt (35,4; 17,7; 11,8; 8,8; 7,1) [M].
- A wurde nach der Rechnung mit jq aus lauf-69/profile/zeilen.json gebildet; es ist keine Urteilsgroesse.
- Bild: lauf-69/bild_E_R.png (E gegen R_max je omega^2, gefuellt = stabil).

### 3.4 E gegen R (HZ3, beschreibend)

| omega^2 | stabile m | Steigung ln E / ln R_max, alle m | dito mit r_mittel |
|---|---|---|---|
| 0,51 | 3, 5 | 1,185 | 1,066 |
| 0,52 | 3 | 1,096 | 1,040 |
| 0,53 | 3 | 1,052 | 1,032 |
| 0,54 | 3 | 1,026 | 1,029 |
| 0,55 | - | 1,016 | 1,028 |

- Mit R_max steigt die Steigung zur Grenze hin, weil R_max nahe am Aussenrand liegt und einen m-unabhaengigen Versatz
  traegt (PLAN.md 0.3). Mit dem ladungsgewichteten Radius bleibt sie bei 1,03 bis 1,07 [M].
- E ~ R gilt also fast genau. Das folgt aber aus der Ringform und nicht aus Stabilitaet.

### 3.5 Tiefste reelle Ringmoden der stabilen Profile (Ringast nach Kartenregel, beschreibend)

Re Omega je l, Basisgitter. Die Regel nimmt je l die kleinste positive Ringmode und springt bei kleinem l zwischen
Aesten, wie in HAGEDORN-1.

| Zeile | l = 0 bis 3 | l = 4 bis 9 |
|---|---|---|
| m = 3, 0,51 | 0,0106 / 0,0015 / 0,0009 / 0,0114 | 0,0172 / 0,0234 / 0,0301 / 0,0371 / 0,0445 / 0,0522 |
| m = 3, 0,52 | 0,0182 / 0,0038 / 0,0050 / 0,0002 | 0,0381 / 0,0517 / 0,0660 / 0,0811 / 0,0969 / 0,1133 |
| m = 3, 0,54 | 0,0326 / 0,0090 / 0,0179 / 0,0118 | 0,0006 / 0,1050 / 0,1335 / 0,1632 / 0,1940 / 0,2258 |
| m = 5, 0,51 | 0,0054 / 0,0012 / 0,0020 / 0,0010 | 0,0124 / 0,0169 / 0,0216 / 0,0265 / 0,0317 / 0,0371 |

- m = 5 bei 0,51 weiter bis l = 15: 0,0427 / 0,0485 / 0,0545 / 0,0606 / 0,0669 / 0,0734. Die Abstaende wachsen langsam
  (0,0045 bis 0,0065), wie bei Kapillarwellen in HAGEDORN-1, nicht konstant wie bei einer Saite [H].
- Bei einzelnen l nahe l = m liegt eine fast verschwindende Mode (0,0002 bei m = 3, 0,52, l = 3; 0,0006 bei 0,54,
  l = 4; 0,0009 bei 0,51, l = 2). Sie bleibt reell.
- Feines Gitter (h/2) fuer l = 2 bis 6: relative Abweichung <= 4,4e-7 (lauf-69/haupt/, Feld fein.sektoren); nicht geurteilt.

## 4. Kontrollen

- **Profile (zwei Wege, Abschnitt R des Plans):**
  - Schiessen scheitert bei 0,51 fuer alle m (erwartet, PLAN.md 0.2).
  - Duennwand-Newton ist fuer alle 20 gueltig, Rest <= 9,3e-13.
  - Wo beide Wege gueltig sind (16 Zeilen), sind die Gitterprofile gleich auf <= 1,7e-12 relativ.
  - E auf dem BdG-Gitter gegen die Quelle: <= 3,7e-7 relativ.
- **Anschluss an HAGEDORN-1 (HZ0):**
  - Groeberes Gitter (h = 0,2) und neue Kastenregel geben die alten Eigenwerte auf 1,4e-10 wieder:
    m = 3: 0,0259659911 + 0,0042896584 i gegen 0,0259659911 + 0,0042896585 i.
  - m = 8 bei 0,55: 3,9581659573e-3 gegen 3,9581659534e-3 (HAGEDORN-1), l = 2. HAGEDORN-1 fand dort nur l = 2 und 3
    instabil, wie hier.
- **Feinprobe (h/2 = 0,1, Shift-Invert):** alle 22 verfolgten Instabilitaeten, relative Abweichung <= 7,0e-9. Keine
  Klasse aendert sich.
- **Dichteprobe** (volles Spektrum auf h/2, alle l, HZ1-Zeilen m = 3, 5, 8 bei 0,52):
  - Gleiche Klassen. m = 3 hat auch auf h/2 nur reelle gezaehlte Eigenwerte.
  - m = 5: l = 2, Im 8,6143634e-4 gegen 8,6143640e-4 auf der Basis. m = 8: 1,36916339e-3 gegen 1,36916338e-3.
  - Keine Randmoden.
  - Der Kasten der Dichteprobe ist nach derselben Regel neu gerundet: L = 49,1 statt 49,2 bei m = 3.
- **Kastenprobe (18/kappa innen und aussen):** die drei groessten Instabilitaeten je Zeile, relative Aenderung
  <= 3,0e-7 (m = 8, 0,51).
  - Bei Zeilen mit innerem Schnitt verschiebt die Probe auch r_a. Der Schnitt im Loch aendert also nichts Messbares.
- **Nullmoden:**
  - Phasenresiduum <= 2,8e-14.
  - Verschiebungsresiduum im Fenster 4,6e-6 bis 4,9e-6 (h = 0,2) und 2,2e-8 bis 2,3e-8 (h/2). Der Faktor ~210 je
    Halbierung passt zur 8. Ordnung.
  - Nullpaar-Eigenwerte: l = 0 <= 1,9e-8; l = 1 1,4e-6 bis 2,4e-6 (wie in HAGEDORN-1 ueber 1e-6, Kasteneffekt).
  - Ausgenommene Nullpaare haben |Im| <= 1,9e-8. Auch gezaehlt waeren sie unter 1e-6; die Nullpaar-Regel entscheidet
    hier keine Zeile.
  - Ueberlappung mit der bekannten Mode >= 0,9999998.
- **Verallgemeinerte Nullmode (nur beschreibend):** nahe der Grenze unbrauchbar (Rest 0,7 bis 209 bei 0,51 und 0,52).
  dQ/domega liegt zwischen -4e4 und -8e6, die Newton-Differenzen sind fast singulaer. Ohne Einfluss auf ein Urteil.
- **VK-Seite (l = 0):** dQ/domega < 0 ueberall; l = 0 ist in allen 20 Zeilen stabil.
- **Hashes (sha256):**
  - PLAN.md = PLAN.md.eingefroren-20261004-065233: 093d30f40008dee67769b883f5625408fd48cba58f206c21968e69a94a549b77
  - code/hagedorn2.py: 81cd74bb19a14e563175bd1b9159debef1a9b6f5ed8549d5f89358d1d36ee654 (gleich vor dem ersten Lauf)
  - code/auswertung2.py: 65f335f349ff50841a91b45b3843765bc8c482995ea8c1d623f9d470bca2e5b8
  - code/hagedorn.py (= HAGEDORN-1): 40782567712f4e7b885b73873225e242248a86beeb25108cecc3be77852514b3
  - code/regge2d.py (= RUNDE-06): 7e7f666793b956fe8a1b495ba254ee872d97f8780306f42a671dca0ebd892608
  - lauf-69/auswertung.json: 77539768e4fa269855e94539fed403a1224564107d8477ce7f6b9b9c0480cf47
  - Dieselben Code-Hashes auf der .69 nach allen Laeufen geprueft (05:04:13 UTC); EINGEFROREN-SHA256.txt.
- **Zeiten (date; .69 in UTC):**
  - Profillauf 04:47:31 bis 04:48:16 UTC; Rauchlaeufe r1/r2 04:48:32 bis 04:48:42 UTC.
  - Plan ab 06:50:55 CEST geschrieben, eingefroren 06:52:33 CEST.
  - Hauptlaeufe 04:52:43 bis 04:58:18 UTC (cpu 333,7 s, cpu6 288,4 s).
  - Dichteprobe 04:58:18 bis 05:02:29 UTC (cpu 220,8 s; cpu6 119,5 s + 108,8 s).
  - Zusammenfuehrung m = 8 lokal 07:02:53 CEST; Auswertung 05:02:53 bis 05:02:56 UTC.
  - ERGEBNIS.md ab 07:04:27 CEST (date direkt davor); letzte inhaltliche Aenderung nach 07:07:32 CEST (date direkt davor).

## 5. Latten (v3)

- **L1 (kann scheitern):**
  - HZ1 konnte scheitern und ist gescheitert. Ob m = 5 und 8 bei 0,52 halten, war offen; die Raten liegen weit ueber
    der Grauzone.
  - HZ2 konnte an jedem Anstieg scheitern. Der Trend aus HAGEDORN-1 sprach aber schon dafuer.
  - HZ0 war eine reine Codeprobe. HZ3 war bei gegebener Auswahl vorab ableitbar und ist nicht auswertbar.
  - Das A-Muster (Ergebnis 3) ist nachtraeglich gefunden, also noch ungeprueft.
- **L2 (Gegenprobe):**
  - zwei unabhaengige Profilwege (Schiessen und Duennwand-Newton)
  - feines Gitter, volles Spektrum auf h/2, groesserer Kasten mit anderem innerem Schnitt
  - Anschluss an HAGEDORN-1
  - Rand- und Ringanteil der Eigenvektoren
- **L3 (Numerik):** Instabilitaeten auf h/2 <= 7e-9, Kasten <= 3e-7, Dichteprobe gleich; Newton <= 1e-12; Residuen
  8. Ordnung.
- **L4 (schon bekannt):**
  - Wirbelringe in Medien mit konkurrierender Nichtlinearitaet zerfallen azimutal; flache, dicke Wirbel mit kleiner
    Ladung sind stabil [L: Firth/Skryabin 1997; L?: Quiroga-Teixeiro/Michinel 1997; Towers u. a. 2001].
  - Ich erinnere unsicher, dass Pego/Warchall 2002 in der kubisch-quintischen NLS stabile "eingekapselte" Wirbel auch
    mit hoeherer Ladung fanden, im Flachprofil-Bereich [L?]. Das passt zu "m_max waechst zur Grenze hin".
  - Ob es fuer genau dieses Klein-Gordon-Potential ein Seitenverhaeltnis-Kriterium gibt, weiss ich nicht.
  - Kein Abruf.
- **L5 (Messbezug):** keiner. Glied 7 (CEMZ) ist eine theoretische Bedingung; das Ergebnis ist eine Modellaussage in
  2D.

## 6. Selbstanzeigen

1. **Reihenfolge:**
   - Profillauf (04:47:31 UTC) und Rauchlaeufe r1/r2 (04:48:32 UTC) liefen, bevor PLAN.md geschrieben war (ab
     06:50:55 CEST = 04:50:55 UTC), wie in HAGEDORN-1.
   - Gitter- und Kastenregel, Profilregel und die Zusatzregeln 3.0 standen vorher im Code (Hash vor dem ersten Lauf).
2. **Nach r1/r2 festgelegt (vor dem Einfrieren, offengelegt in PLAN.md R):**
   - die Lesarten fuer HZ0 (gemeinsamer l-Bereich) und HZ2 (nicht steigend, stabil = 0)
   - die Dichteprobe
   - r2 zeigte schon m = 12 bei 0,51 instabil (l = 2, Im 4,8e-4). Keine Schwelle ist geaendert.
3. **Dichteprobe m = 8 geteilt:**
   - Der erste Block (dicht-b) startete die Zeile nicht: Die Budgetschaetzung im Skript ergab 552 s > 540 s.
   - Ich habe sie in zwei l-Bloecke geteilt (l = 0 bis 12 und 13 bis 24, je ein eigener Start) und die beiden JSON
     lokal mit jq zusammengefuegt (nur die Sektorlisten aneinandergehaengt, Vermerk "zusammengefuegt" in der Datei).
   - Beide Teile liegen in lauf-69/dicht-m8-teil1 und -teil2. Im Plan stand ein Block je Lauf; die Teilung ist eine
     Abweichung im Ablauf, nicht in den Regeln.
4. **Wartende Starts:** Die Dichteprobe habe ich hinter die Hauptlaeufe gereiht; sie wartete am Lock der Spur. Es
   rechneten nie mehr als zwei Laeufe zugleich.
5. **Textfehler im eingefrorenen Code:** Der HZ0-Vermerk in auswertung2.py verweist auf "PLAN.md 3.2", richtig ist 3.1.
   Nicht geaendert.
6. **A-Muster nachtraeglich:** Seitenverhaeltnis, Schwelle 1,8 bis 2,0 und m_max-Formel habe ich nach dem Hauptlauf
   mit jq gebildet. Sie sind Hypothese [H], kein Kartenurteil. Die Schwelle stuetzt sich auf je einen Punkt auf beiden
   Seiten (1,79 und 1,99).
7. **Befehle:**
   - Auf der .69 lief kein Interpreter ausserhalb von kleintest.sh, auch keine Versionsprobe.
   - Ausserhalb des Starters auf der .69: mkdir, mv, ls, cat, grep, cut, tail, sha256sum, date, which jq,
     systemctl --user list-units (nur lesen).
   - Lokal: jq, ssh, scp, sha256sum, date, grep, sed, dazu mkdir, cp, ls, cat, sort, wc und eine sleep-Warteschleife
     (until). Kein Interpreter.
   - Ein Aufruf "sleep 60; ssh ..." wurde vom Werkzeug abgelehnt und lief nicht.
8. **Zeitbox:** 90 min ab 06:35:45 CEST eingehalten. Letzte inhaltliche Aenderung nach 07:07:32 CEST (date), also
   nach knapp 32 min.
9. **Literatur:** kein Abruf; alle Angaben aus dem Gedaechtnis ([L], [L?]).

## 7. Naechster Schritt (Vorschlag)

- **Das A-Muster vorab pruefen [H]:**
  - omega^2 = 0,505 (eps = 0,005) rechnen. Vorhersage: m <= 8 stabil, m = 12 instabil (m_max ~ 8,6 bis 9,7).
  - Bei 0,51: m = 6 stabil (A = 1,77), m = 7 instabil (A = 2,04), beides nach der Duennwand-Formel.
  - Die Profile liefert der Duennwand-Newton; ein Lauf dauert unter 10 min.
- **Schreibtisch:** Kreisring mit Oberflaechenspannung an zwei Raendern und Wirbelstroemung v = m/r. Gibt das
  Kapillarmodell eine l = 2-Schwelle bei A ~ 1,9 [H]? Gelingt das, waere die Aussage "stabile Ringe sind dick"
  verstanden und nicht nur gemessen.
- **Fuer Glied 7:** Der 2D-Ringturm ist als String-Kandidat erledigt; weiter nur, falls 3D-Tori anders laufen (teuer).

## 8. Einfach gesagt

Wir haben am Computer geprueft, ob grosse, sich drehende Feldringe stabil bleiben, wenn man sie leicht anstoesst. Kurz
vor der Grenze werden die Ringe sehr gross und dick, und einige halten tatsaechlich, aber nur die dicken: Ihr Radius
ist hoechstens etwa doppelt so gross wie ihre Dicke. Laengere, im Verhaeltnis duennere Ringe beulen sich langsam zu
einer Ellipse aus und zerfallen, auch dicht an der Grenze, nur immer langsamer. Eine schwingende Saite mit
Zugspannung muesste aber gerade ein langer, duenner Ring sein; deshalb liefern diese Feldringe in unserem Modell
keinen saitenartigen Turm. Das ist eine Modellrechnung in zwei Dimensionen, keine Messung.
