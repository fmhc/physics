# ZUS-10 Pruefung: Ergebnis (Runde 9, v3)

- Pruefer: frischer Anthropic-Agent (Fable), nicht der Verfasser der Ideen. Auftrag: Leitung claude-primary.
- Grundlage: IDEEN-10.md (sha256 5d788229…2711, um 08:08:48 CEST gleich mit der eingefrorenen Kopie). Lesarten der
  Scheiterregeln: PRUEFPLAN.md (08:18:57 bis 08:20:52 CEST, vor jedem Lauf).
- Zeiten (date): Beginn 08:08:48 CEST; Laeufe auf der .69 ab 08:22:17 CEST (Logs in UTC = CEST - 2 h); Pause der Leitung
  08:37 bis 09:51; Reparaturlaeufe 09:57 bis 10:04 CEST; Schreibbeginn dieser Datei nach der letzten date-Messung
  10:06:28 CEST. Ende: letzte Zeile.
- Rechenort: .69, /home/fmh/fmhc-physics-remote/runde9-zus10/ (Kopien der Skripte; Originale unveraendert). Ketten
  kette-zus10-{a,a2,a3,b,c,d,d2}.sh; Ausgaben lokal in pruefung/lauf-69/ (ohne Rohfelder).
- Belegstufen: **[Hand]** Nachrechnung von Hand; **[num]** ein Gitter, ein Verfahren; **[num+K]** mit Kontrolle (zweites
  Raster, zweite Stufe, Kontrolllauf); **[L]** Quelle selbst gelesen; **[L?]** nicht an der Quelle geprueft; **[H]**
  Hypothese. **Alles ist Modellaussage; nichts ist Messdatenbestaetigung.**

## Fehlerkasten (technisch, dokumentiert)

1. Kette A wurde um 08:25 von mir selbst beendet: Beim Aufraeumen eines haengenden ssh-Aufrufs habe ich das Kind
   des haengenden Prozesses beendet, das war die Kette selbst. Der laufende Unit z1ua lief als systemd-Unit weiter
   (rc = 0); die uebrigen Aufrufe liefen als Kette A2 (ab 08:25:20 CEST) neu. Kein Datenverlust.
2. **Kette A2, Teil b von Idee 3 (z3bb) ist ungueltig** (Befund Codex, status-audit-20260930/codex-wm1/
   VIER-BEFUNDE-PRAEZISE.txt): `seq -s,` erzeugte unter deutscher Locale Dezimalkommas
   (dims 2,3,2,4,…,3,0); bic2.py trennt an ",". Der Lauf (rc = 1) wird nicht bewertet, keine Zwischenwerte
   werden verwendet. Reparatur: kette-zus10-a3.sh mit expliziter Liste "2.3,…,3.0", LC_ALL=C, Ausgabe der
   Argumentliste vor dem Start (KETTE-A3.log). Neuer Lauf z3bc, rc = 0.
3. **Idee 7, erster Rauchtest (z7rauch) brach mit "No CUDA GPUs are available" ab:** tests1d_r3.uhr() synchronisiert
   CUDA bedingungslos. Reparatur nur in meiner Kopie t5k_zus7.py (eigene Funktion uhr(), CUDA-Sync nur bei
   m.DEV.type == "cuda"); das Fremdmodul blieb unveraendert. Rauchtest z7rauch2 rc = 0, GPU-Lauf z7gpu rc = 0.
4. Zwei ssh-Aufrufe hingen, weil ein `nohup … &` in einer `&&`-Liste stand (Subshell haelt die Pipe); harmlos,
   spaeter freistehend gestartet.
5. Fuer Idee 8 (d) habe ich die R7-Tabelle (x_halb, w) gelesen, bevor ich die Lesart w* = x_halb festlegte; das steht
   so im Plan. Fuer Idee 8 (a) erwies sich meine Lesart (Programmklasse "Kaverne") als grober als der Wortlaut der
   Scheiterregel ("dauerhaft aufreissen"); ich berichte beides, ohne die Lesart nachtraeglich zu aendern.
6. WebSearch war in dieser Sitzung verbraucht; Literatur nur per WebFetch (arXiv-Abstracts, zwei PDFs per Read).

## Uebersicht

| Idee | Ausgang | Zahl | Vorschlag |
|---|---|---|---|
| 1 Zwei Leitern, j1-Regel | **getroffen** | n = 6…9 bei 0,57437 / 0,56388 / 0,55598 / 0,54981 (vorab 0,5742 / 0,5637 / 0,5558 / 0,5496, Abweichung 1,7e-4 bis 2,1e-4); Schritt 2,210 (vorab 2,22 +- 0,02) | weiter |
| 2 Gegenlaeufer als Rotor | nicht entscheidbar | (a), (d) von Hand richtig; (b), (c) brauchen die Codeerweiterung | weiter (Codeerweiterung, 1 bis 2 h) |
| 3 Fuetter-Spitze, Dimensionsbruecke l = 1 | **getroffen** | V-Minimum bei d = 2,6: 2,8e-6 gegen 2,4e-4 / 4,1e-4 (Faktor 84 / 148); Endpunkt Re rho(3) = 1,7635199 (vorab 1,76352 +- 0,001) | weiter |
| 4 Rayleigh-Tropfen l = 2 | **getroffen** | Uebertritt zwischen 0,69 (gebunden) und 0,71 (Resonanz), also 0,70 +- 0,01; Steigung d ln Gamma / d ln q = 4,2 (0,71 bis 0,73) bzw. 3,9 (0,73 bis 0,76); kein V-Einbruch; l = 3 tritt zwischen 0,63 und 0,66 ueber | parken (bestaetigt) |
| 5 Lebensdauerstufen | getroffen (Papier, Literatur); Rechenteil nicht geprueft | k-Tabelle stimmt; SW99: kubisch, 3 Omega > m, R ~ t^(-1/4) (k = 3); MM97: dA/dt = -0,010 A^3, also t^(-1/2) (k = 2) | weiter (kleiner Test 2 nu_0 = Kante) |
| 6 Kein Dunkelzustand in 3D | nicht entscheidbar | KOLL-1: bei 0,76, d = 14, t = 500 klingt das Paar wie der Einzelball ab (0,163 gegen 0,158); Langzeit durch Stoermoden des eingefrorenen Hintergrunds unbrauchbar | parken |
| 7 Vernichtungsrest als Oszillon | **verfehlt** (Chem-14-Paar d = 8) | E15(2000)/E15(0) = 0,0027 < 0,005; Restfrequenz 1,002 (Schwelle). Aber d = 4: 0,48 bei T = 3000, Frequenz 0,80, 127 Ladungswechsel | verwerfen fuer d >= 6; neue Karte: Ladungstausch-Ball bei d = 4 |
| 8 Kavitation und Duennwand | gemischt: (b) verfehlt, (c) getroffen, (a) je nach Lesart, (d) halb | S0 = 1,05 / 1,2: keine Delle reisst dauerhaft auf (t_kav in 48 von 48 undefiniert), aber Klasse "Kaverne" in 14 + 14 von 48; S0 = 0,95: voll w = 1 kavitiert (t_kav 280); F_b 1,5e-4 (0,68) bis 0,619 (0,99), Grenzwert 0,707 | parken; Kriterium "dauerhaft" schaerfen |
| 9 Spinmischung, Verstimmung | **getroffen** | lambda(0) = 0,046238 (R8 0,046238), lambda(0,05) = 0,03806 (vorab 0,036 +- 10 %), lambda(0,08) = 0,01787, delta = 0,10 stabil (reelle Mode 0,02669); Fenster ~0,087 (vorab 0,081 +- 10 %) | weiter |

## Idee 1: Zwei Leitern, zwei Formfaktoren (gfbic.py ueberlapp, g -> 0)

- **Vorhersage (kurz):** zweite Leiter bei X = 2 omega/(omega^2 - 1/2) = x_{1,n} + delta, 0 <= delta <= 0,13:
  n = 6: 0,5742 +- 0,0003; 7: 0,5637 +- 0,0002; 8: 0,5558 +- 0,0002; 9: 0,5496 +- 0,0002; Schritt 2,22 +- 0,02.
- **Laeufe:** z1ua (0,545 bis 0,5625, dx 0,0025, 429 s), z1ub (0,5625 bis 0,580, 448 s), z1uc (0,548 bis 0,577,
  dx 0,001, 511 s), alle hp = 0,02, cpu6/cpu2. Vorzeichenwechsel von I/A, linear interpoliert:

  | n | vorab | gefunden dx 0,001 | dx 0,0025 | Abweichung | 1/(x - 0,5) | Schritt |
  |---|---|---|---|---|---|---|
  | 6 | 0,5742 +- 0,0003 | 0,57437 | 0,57438 | +1,7e-4 | 13,446 | - |
  | 7 | 0,5637 +- 0,0002 | 0,56388 | 0,56392 | +1,8e-4 | 15,654 | 2,208 |
  | 8 | 0,5558 +- 0,0002 | 0,55598 | 0,55606 | +1,8e-4 | 17,864 | 2,209 |
  | 9 | 0,5496 +- 0,0002 | 0,54981 | 0,54977 | +2,1e-4 | 20,076 | 2,213 |

  - Mittlerer Schritt 2,210 (Hand aus den vier Werten). n = 9 liegt 1e-5 ausserhalb des +-0,0002-Fensters, weit
    unter der Scheiterschwelle (+0,0003). Zwischen den Stellen liegt kein weiterer Wechsel (vier Wechsel in 0,548 bis
    0,577). Die R8-Rasterwerte 0,5752 und 0,5656 sind nicht bestaetigt (Abstand 8e-4 bzw. 1,7e-3); 0,55116 war ein
    Interpolationsartefakt zwischen zwei Nullstellen (I(0,55) = +0,086, I(0,56) = -0,656).
  - Polkontrolle bei g = 0,2 (Schiessen h = 0,02, Zugabe): -Im nu = 1,4e-7 (0,549812), 1,2e-7 (0,555980), 7,2e-8
    (0,563922), 6,8e-8 (0,574379) gegen 2,7e-6 bis 7,2e-6 an den Nachbarn +-0,01: Einbrueche um 20 bis 100, wie in R9
    (Kurven verschieben sich mit g).
  - Hinweis ohne Vorab: bei 0,545 ist I/A = -0,085, nahe null; die Regel gaebe n = 10 bei ~0,5448 (nicht geprueft).
- **Scheiterregeln:** keine ausgeloest (Abweichung <= 2,1e-4; R8-Werte nicht bestaetigt; keine Zwischenstelle;
  Schritt 2,21 < 2,26).
- **Gegenprobe [Hand]:** erste Leiter in X: X/pi = 1,910 / 2,846 / 3,849 / 4,868 / 5,895 fuer n = 1 bis 5 (aus
  0,797677 / 0,685129 / 0,631449 / 0,601422 / 0,582417), also n + 0,85…0,91, nicht die j1-Nullstellen (n + 0,43…0,48).
  Z3 (0,551156 bei g = 0,4985) laeuft mit c = (0,551156 - 0,54981)/0,4985^2 = 0,0054 in die n = 9-Stelle; |c| < 0,02.
- **Ausgang: getroffen.** Belegstufe [num+K]: goldene Regel im Grenzfall g -> 0, ein Profilgitter (hp = 0,02), zwei
  Raster (Abweichung <= 8e-5), Polkontrolle bei g = 0,2; kein Umlauftest, keine zweite Stufe hp.
- **Vorschlag:** weiter (Umlauftest an einer der vier Stellen bei g = 0,1 mit gfbic_umlauf.py; n = 10 bei ~0,5448).

## Idee 2: Der Gegenlaeufer ist ein Rotor (Papier)

- **Vorhersage (kurz):** (a) alpha -> 0 ergibt die R8-Gegenlaeuferbreite; (b) stille Stellen werden fuer alpha > 0 zu
  Minima, Rest ~ tan^2(alpha); (c) exakte Stille nur in isolierten Punkten; (d) langsame Rotoren mit
  Omega < (2/3)(1 - omega) strahlen linear nicht.
- **Papier [Hand]:** Bei g = 0 ist die Lagrangedichte in den vier reellen Feldkomponenten O(4)-symmetrisch (Kinetik
  und S = |psi_1|^2 + |psi_2|^2), also ist psi_1 = cos(alpha) f e^{-i omega t}, psi_2 = sin(alpha) f e^{+i omega t}
  exakt stationaer (S = f^2, beide Gleichungen sind die Profilgleichung). Der Paarterm g J Re[(psi_1^* psi_2)^2]
  liefert die Quellen (psi_1^* psi_2) psi_2 ~ cos(alpha) sin^2(alpha) f^3 e^{+3 i omega t} fuer psi_1 und
  (psi_1 psi_2^*) psi_1 ~ cos^2(alpha) sin(alpha) f^3 e^{-3 i omega t} fuer psi_2. Fuer alpha -> 0 bleibt die
  psi_2-Quelle ~ alpha g f^3 bei 3 omega: genau das lineare Gegenlaeufer-Problem von R8 (sp = -g J S auf v = f). (a)
  stimmt damit per Konstruktion. (d): symmetrische Aufteilung mit Relativfrequenz Omega gibt Quellfrequenzen
  omega +- 3 Omega/2; unter der Masse fuer Omega < (2/3)(1 - omega). Stimmt.
- **(b), (c):** brauchen den erweiterten Zweikanal-Loeser (Idee: 1 bis 2 h). Nicht gerechnet. Die Scheiterregel
  "0,7107 bleibt bei alpha = 0,1 und 0,2 exakt still" ist damit ungeprueft.
- **Literatur [L]:** Copeland, Saffin, Zhou, PRL 113, 231603 (2014), Abstract (arXiv 1409.3232): zusammengesetzte
  Q-Baelle, in denen positive und negative Ladung koexistieren und mit einer Frequenz unter der Einzelballfrequenz
  tauschen; gebaut aus eng ueberlappenden Q- und Anti-Q-Baellen. Das ist ein Einfeld-Gegenstueck; fuer zwei Felder mit
  O(4) habe ich keine Quelle gesucht (WebSearch gesperrt).
- **Ausgang: nicht entscheidbar** (Kern (b)/(c) ungeprueft; (a), (d) von Hand bestaetigt). Belegstufe [Hand].
- **Vorschlag:** weiter, wenn die Codeerweiterung gebaut wird; die O(4)-Beobachtung ist exakt und kostet nichts.

## Idee 3: Zweite Fuetter-Spitze und Dimensionsbruecke l = 1 (bic2.py bruecke)

- **Vorhersage (kurz):** V-Minimum von |Im rho(d)| bei d = 2,5 +- 0,2, mindestens 100-mal tiefer als die Nachbarn
  (Raster 0,1); Endpunkt Re rho(3) = 1,76352 +- 0,001; schwaecher: zweites Minimum bei 1,9 +- 0,25.
- **Laeufe:** z3ba (dims 1 bis 2,3; 159 s) und z3bc (2,3 bis 3,0, Start = Spurpunkt 2,3; 175 s), l = 1,
  omega^2 = 0,7, h = 0,02, Start 1,7777169 - 1,328e-5 i. z3bb ungueltig (Fehlerkasten 2).

  | d | 1 | 1,25 | 1,5 | 1,75 | 2 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | **2,6** | 2,7 | 2,8 | 2,9 | 3 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Re rho | 1,77772 | 1,78179 | 1,78426 | 1,78396 | 1,78067 | 1,77890 | 1,77709 | 1,77522 | 1,77317 | 1,77083 | 1,76831 | 1,76592 | 1,76412 | 1,76331 | 1,76352 |
  | -Im rho | 1,33e-5 | 5,37e-5 | 1,98e-4 | 6,35e-4 | 1,48e-3 | 1,75e-3 | 1,77e-3 | 1,44e-3 | 8,38e-4 | 2,36e-4 | **2,79e-6** | 4,13e-4 | 1,46e-3 | 2,77e-3 | 3,66e-3 |

  - Newton ueberall konvergiert (|D| <= 1e-15); der Spurpunkt 2,3 wurde in beiden Teilen identisch gerechnet.
  - V-Minimum bei d = 2,6: Verhaeltnis zu den Nachbarn 84 (2,5) und 148 (2,7). Meine Schwelle (10) ist erfuellt; die
    Zahlenvorhersage "100-mal" gilt gegen einen Nachbarn, gegen den anderen knapp nicht (84). Die Nullstelle liegt
    damit innerhalb weniger 0,01 von 2,6, im Fenster 2,5 +- 0,2 (Faecherregel: 2,57).
  - Endpunkt d = 3: 1,7635199 - 3,657e-3 i = der 3D-l = 1-Pol aus R6 (1,7635198 - 3,657e-3 i); Abweichung 1e-7.
  - Zweites Minimum bei 1,9 +- 0,25: nicht gesehen; |Im| waechst von d = 1 bis 2,2 monoton (Raster 0,25 bzw. 0,1).
  - Gegenprobe l = 0 mit feiner d-Liste (Ergaenzungslaeufe z3ca / z3cb auf cpu2, nach dem Hauptergebnis; Start
    1,4937770 - 6,716e-5 i, dim 1 gegen Codex auf 3,6e-8): -Im rho = 6,7e-5 (1) / 2,78e-3 (1,25) / 1,49e-3 (1,4) /
    1,15e-3 (1,5) / 1,42e-3 (1,6) / 2,40e-3 (1,75) / 2,68e-3 (2,0) / 1,74e-3 (2,1) / 6,3e-4 (2,2) / 2,2e-4 (2,25) /
    1,4e-5 (2,3). Das R6-Minimum bei d ~ 1,5 ist ein **flaches** Minimum (Verhaeltnis zu den Nachbarn 1,3 und 1,2),
    keine V-Form, also nach THEORIE 4.2 keine Nullstellenlinie; das R6-Minimum bei ~2,25 ist eine echte V-Form bei
    d = 2,3: 1,4e-5 gegen 2,2e-4 (2,25) und 3,8e-4 (2,4), Faktor 16 bzw. 27; weiter 1,75e-3 (2,5), 3,56e-3 (2,6),
    4,83e-3 (2,7), 4,74e-3 (2,8), 3,32e-3 (2,9), 1,468e-3 (3,0) mit Re rho(3) = 1,7018102865, dem 3D-l = 0-Pol aus R6
    (1,7018102865 - 1,468e-3 i, bitgleich in den gedruckten Stellen). Die Gegenprobe "beide R6-Minima sind echte
    Nullstellen" ist damit halb verfehlt (1,5 nein, 2,3 ja); die Faecherregel der Theorie (Wechsel bei 1,68 und 2,43)
    trifft nur den zweiten, um 0,13 verschoben. Abwechslung l = 0 (2,3) / l = 1 (2,6): ja, fuer dieses eine Paar.
- **Scheiterregeln:** keine ausgeloest.
- **Ausgang: getroffen.** Belegstufe [num]: ein Code, eine Stufe (h = 0,02), stetige Polverfolgung; Endpunkt gegen
  R6 [num+K].
- **Vorschlag:** weiter (exakt/Umlauf fuer l = 1 bei d = 2,6 waere die naechste Stufe; l = 0-Gegenprobe nachholen).

## Idee 4: Rayleigh-Tropfen l = 2 (bic2.py pole, eine Stufe h = 0,02)

- **Vorhersage (kurz):** Kantenuebertritt bei omega^2 = 0,70 +- 0,04; knapp darueber d ln Gamma / d ln q = 5 +- 1,5;
  bis 0,90 kein V-Einbruch unter 1e-6, Phi/pi < 0,5; l = 3 tritt bei 0,62 bis 0,66 ueber.
- **Laeufe:** z4pa (0,64 / 0,67 / 0,70, alles, 202 s), z4pb (0,73 / 0,76, alles, 129 s), z4pc (0,80 / 0,84 / 0,88,
  resonanz, 208 s), z4pd (l = 3: 0,60 / 0,63 / 0,66, alles, 212 s). Abweichung vom Vorschlag der Idee: eine Stufe
  statt zwei (Budget). Tiefster l = 2-Pol (Re rho < 0,3):

  | omega^2 | Kante 1 - omega | Pol | q | Gamma |
  |---|---|---|---|---|
  | 0,64 | 0,2000 | 0,11327 gebunden | - | 0 |
  | 0,67 | 0,1815 | 0,14101 gebunden | - | 0 |
  | 0,69 (Ergaenzung z4pe) | 0,1693 | 0,15710 gebunden | - | 0 |
  | 0,70 | 0,1633 | nicht gefunden (Kontur 0, kein gebundener) | - | - |
  | 0,71 (Ergaenzung z4pe) | 0,1574 | 0,16887 - 7,009e-4 i | 0,1520 | 7,01e-4 |
  | 0,73 | 0,1456 | 0,17698 - 5,774e-3 i | 0,2525 | 5,77e-3 |
  | 0,76 | 0,1282 | 0,18617 - 1,966e-2 i | 0,3453 | 1,97e-2 |
  | 0,80 | 0,1056 | 0,19173 - 4,568e-2 i (R6: 0,19173 - 4,57e-2 i) | 0,4240 | 4,57e-2 |
  | 0,84 | 0,0835 | 0,18612 - 7,561e-2 i | 0,4646 | 7,56e-2 |
  | 0,88 | 0,0619 | nicht gefunden (Kontur 0) | - | - |

  - Uebertritt nach Lesart (Hauptraster): letzter gebundener 0,67, erste Resonanz 0,73, also 0,70 +- 0,03 (der
    Punkt 0,70 fehlt: der Pol liegt dort im unabgetasteten Streifen +-0,002 um die Kante). Ergaenzungslauf z4pe
    (0,69 / 0,71, 140 s, nach dem Hauptergebnis): bei 0,69 gebunden 0,012 unter der Kante, bei 0,71 Resonanz 0,0115
    ueber der Kante, also Uebertritt 0,70 +- 0,01 (linear: ~0,700).
  - Steigung aus 0,73 und 0,76 (Hand): ln(1,966e-2/5,774e-3)/ln(0,3453/0,2525) = 1,2253/0,3132 = 3,9; weiter
    4,1 (0,76 bis 0,80) und 5,5 (0,80 bis 0,84). Mit dem Ergaenzungspunkt 0,71 (q = 0,1520, Gamma = 7,01e-4) ist die
    schwellennaechste Steigung 0,71 -> 0,73: ln(8,238)/ln(1,661) = 4,2 (Hand).
  - Gamma waechst von 0,73 bis 0,84 monoton; kein Einbruch. Phi/pi = q R_tw/pi = 0,30 (0,76), 0,32 (0,80), 0,31 (0,84).
  - l = 3: 0,60 gebunden 0,14058 (Kante 0,2254); 0,63 gebunden 0,19289 (Kante 0,2063); 0,66 Resonanz 0,23449 - 4,49e-3 i
    (Kante 0,1876). Uebertritt zwischen 0,63 und 0,66, vor l = 2. Rayleigh-Verhaeltnis bei 0,60: 0,14058/0,07411 = 1,90
    (vorab sqrt(30/8) = 1,94).
  - Konturzaehlung an jedem gefundenen Punkt 1, Negativkontrolle ohne Ball |D_frei| >= 0,05.
  - Nebenbefund [Hand]: Die R6-Tropfenwerte 0,52 bis 0,60 skalieren wie epsilon^1,4, nicht epsilon^0,86 wie im Ideentext;
    die Uebertrittsschaetzung bleibt 0,68 bis 0,70.
- **Scheiterregeln:** keine ausgeloest.
- **Ausgang: getroffen.** Belegstufe [num]: eine Stufe, ein Code; der Punkt 0,80 stimmt mit R6 [num+K].
- **Vorschlag:** parken (bestaetigt); der fehlende Punkt 0,70 (Streifen an der Kante) und die zweite Stufe waeren die
  Nacharbeit.

## Idee 5: Ordnung der ersten strahlenden Oberwelle (Papier, Literatur)

- **Vorhersage (kurz):** k = kleinste ganze Zahl mit omega + k rho > 1; Fluss ~ eps^(2k), A ~ t^(-1/(2k-2)); Tabelle
  (P1: 2; Tropfen 0,60: 4; 0,55: 9 bis 10; 0,52: 37; M1: 2 knapp; M3: 2).
- **Hand:** (1 - omega)/rho = 0,2254/0,0741 = 3,04 -> k = 4 (0,60); 0,2584/0,0287 = 9,00 -> 9 bis 10 (0,55);
  0,2789/0,0077 = 36,2 -> 37 (0,52); M1: 0,13067/0,0687 = 1,90 -> 2, 2 nu_0 - Kante = 0,0067; M3: 0,2474/0,2182 = 1,13 -> 2.
  Alle Tabellenwerte stimmen. Gesetz: dE/dt ~ -A^(2k) mit E ~ A^2 gibt A^2 ~ t^(-1/(k-1)), also A ~ t^(-1/(2k-2)).
- **Literatur [L]:** Soffer und Weinstein, Invent. Math. 136 (1999), arXiv chao-dyn/9807003, Theorem 1.1 (PDF gelesen):
  kubische Nichtlinearitaet f(u) = u^3, Resonanzbedingung ueber die dritte Harmonische (Gl. 1.8: |F_c phi^3 (3 Omega)|^2 > 0),
  Amplitude R(t) = O(|t|^(-1/4)) (Gl. 1.10). Das ist k = 3 im Gesetz der Idee. Manton und Merabet, Nonlinearity 10
  (1997), arXiv hep-th/9605038, Anhang (PDF gelesen): dA_0/dt = -0,010 A_0^3 (Gl. A.32) fuer die Formmode des
  phi^4-Kinks, also A ~ t^(-1/2), k = 2. Bambusi und Cuccagna 2011 nicht gefunden (arXiv-Suche ohne Treffer) [L?].
- **Nicht geprueft:** die nichtlineare Rechnung (koll1.py mit l = 2, ueber 10 min, Codeaenderung); damit die zweite
  Scheiterregel (Fluss ~ eps^4 oder eps^6 bei 0,60). Der kleine Test "2 nu_0 = Kante" (gfbic_gem.py) ebenfalls nicht.
- **Ausgang: getroffen (Papier, Literatur); Rechenteil nicht geprueft.** Belegstufe [Hand], [L] fuer k = 2 und 3.
- **Vorschlag:** weiter (kleiner Test 2 nu_0 = Kante an M1 mit g = 0,15 / 0,10).

## Idee 6: Kein Dunkelzustand zweier Baelle in 3D (nur Lesen, KOLL-1)

- **Vorhersage (kurz):** |Gamma_+ - Gamma_-|/(Gamma_+ + Gamma_-) = |sin(qd)/(qd)| = 0,038 / 0,017 / 0,024 bei
  d = 10 / 12 / 14 (0,76); keine kollektive Mode unter 0,9 Gamma_0; scheitert bei Gamma < 0,5 Gamma_0.
- **Hand:** q = 2,3999: qd - 7 pi = 2,008, sin = 0,906, /24,0 = 0,038; qd - 9 pi = 0,525, sin = 0,501, /28,8 = 0,017;
  qd - 10 pi = 2,183, sin = 0,821, /33,6 = 0,024. Stimmt. 1D-Periode: q = sqrt((0,8367 + 1,4938)^2 - 1) = 2,105,
  2 pi/q = 2,985 = R-2-Periode. Stimmt.
- **KOLL-1 (RUNDE-09/koll1/ERGEBNIS.md, fertig):** (a) J_rad = Gamma/(qd) = 8,6e-5 / 7,2e-5 / 6,2e-5 bei 0,76, d = 10 /
  12 / 14: dieselbe Dicke-Form, keine unabhaengige Messung. Zeitlaeufe (gehalten, linear): bei 0,76, d = 14, t = 500
  klingt das Paar wie der Einzelball ab (Summe a^2 0,163 gegen 0,158); der ungerade Sektor bei 0,76 ebenso (0,41 gegen
  0,40). Danach wachsen in allen eingefrorenen Paaren Stoermoden (Raten 0,002 bis 0,08 laut KOLL-1); die langen Laeufe (T = 2500 /
  3500) sind dadurch unbrauchbar. Freie Baelle fliegen auseinander.
- **Scheiterregel:** nicht ausgeloest (keine kollektive Mode mit Gamma < 0,5 Gamma_0 gesehen, soweit messbar).
  Das Verhaeltnis 0,038 / 0,017 / 0,024 ist nicht messbar (Stoermoden). 1D-Gegenprobe bei 0,6 nicht gerechnet.
- **Ausgang: nicht entscheidbar.** Belegstufe: Lesen fremder Ergebnisse, [Hand].
- **Vorschlag:** parken (KOLL-1 selbst schlaegt parken vor).

## Idee 7: Der Rest der Q/Anti-Q-Vernichtung ist ein Oszillon (t5k_zus7.py, p4000a)

- **Vorhersage (kurz):** (a) E in |x| < 15 bei T = 1000 >= 3 % und von 1000 bis 3000 um weniger als Faktor 2 fallend;
  (b) Hauptfrequenz 0,75 bis 1,0; (c) >= 10 Vorzeichenwechsel von Q_links mit Q_links ~ -Q_rechts, sonst neutral;
  (d) d = 4, 6 lassen mehr Rest als 8, 12. Scheitert bei E15(2000) < 0,5 % oder Restfrequenz ueber 1.
- **Lauf:** z7gpu, omega^2 = 0,7, T = 3000, Messung alle 0,5, Stapel: Paare d = 4 / 6 / 8 (theta 0), Paar d = 8 mit
  theta = pi/2, Einzelball; Stufen grob (dx 0,1) und fein (dx 0,05), 72,6 + 135,4 s. Zahlen der feinen Stufe (grob in
  Klammern, wo abweichend):

  | Lauf | E15/E15(0) bei 500 / 1000 / 2000 / 3000 | Hauptfrequenz (Fenster t >= 1000) | Q_links Wechsel | max abs Q_links | korr(Q_l, -Q_r) |
  |---|---|---|---|---|---|
  | d = 4 | 0,697 / 0,590 / 0,514 / 0,483 | 0,8009 | 127 | 0,361 | 1,00 |
  | d = 6 | 0,0027 / 0,0004 / 0,0094 (grob 0,0117) / 0,0048 (0,0018) | 1,0051 | 1 | 0,121 | 1,00 |
  | d = 8 (Chem 14) | 0,0117 / 0,0086 / 0,0027 / 0,0021 | 1,0019 | 0 | 0,046 | 1,00 |
  | d = 8, theta = pi/2 | 0,0124 / 0,0069 / 0,0015 / 0,0006 | 1,0019 | 1 | 0,044 | 1,00 |
  | Einzelball (Kontrolle) | 1,0000 / 1,0000 / 1,0000 / 1,0000 | 0,8355 (omega = 0,8367), P+/P- = 3e-18 | 0 | 2,405 (Ladung links) | - |

  - Chem-14-Bezugslauf d = 8: E15(2000)/E15(0) = 0,0027 < 0,005 und Restfrequenz 1,002 (Fensteraufloesung 0,003, also
    an der Massenschwelle; Spektrum symmetrisch +-1,002, neutral): **beide Scheiterbedingungen ausgeloest.** (a) verfehlt
    (0,86 % bei 1000). Der Rest ist verzoegerte Abstrahlung nahe der Schwelle, kein gebundenes Oszillon.
  - d = 6: ebenso (0,04 % bei 1000, Frequenz 1,005). (d) fuer d = 6 verfehlt.
  - **d = 4 [num+K]:** 48 % der Anfangsenergie bei T = 3000 in |x| < 15, Abfall 1000 -> 3000 um Faktor 1,22, Frequenz
    0,80 (unter der Masse, unter omega = 0,837), 127 Vorzeichenwechsel der linken Ladung mit Q_links = -Q_rechts,
    max |Q_links| = 0,36 (Anfangsladung je Ball 2,44); grob und fein gleich auf 1 %. Das ist ein Ladungstausch-Ball
    im Sinn von Copeland, Saffin und Zhou 2014 [L, Abstract]: eng zusammengesetzte Q/Anti-Q-Kerne, Ladungstausch
    mit einer Frequenz unter der Einzelballfrequenz. (a) bis (d) treffen fuer d = 4.
  - Gegenprobe theta = pi/2 bei d = 8: Rest 0,0006 statt 0,0021, aendert nichts am Bild. Einzelball: Messung sauber.
- **Ausgang: verfehlt** fuer den Chem-14-Rest (d = 8, und d = 6); die Hypothese "Oszillon" trifft nur fuer das eng
  gestartete Paar d = 4 (Ladungstausch-Ball). Belegstufe [num+K] (zwei Gitterstufen, Kontrolle).
- **Vorschlag:** verwerfen fuer d >= 6; neue Karte "Ladungstausch-Ball bei d <= 4" (Lebensdauer, Abhaengigkeit von d
  und theta, Vergleich mit CSZ 2014).

## Idee 8: Kavitation und Duennwand-Grenze (r5f.py kavitation, CPU)

- **Vorhersage (kurz):** (a) S0 >= 1: keine Delle kavitiert; (b) 0,95: nur deutlich breitere Dellen; (c) F_b -> 0,707
  monoton; (d) Fehltreffer schmaler als w*, richtig kavitierende breiter; (e) 3D ohne Kavitation.
- **Laeufe:** z8kv (Keimtabelle, --nur-vorhersage, 4,7 s), z8ka (Raster S0 = 0,95 / 1,05 / 1,2, je 24 Dellen + Kontrolle,
  L = 200, T = 600, nur grob, 223 s; die feine Stufe entfiel durch die Restzeitregel des Skripts).
- **(a)** S0 = 1,05 und 1,2: Kontrollen ohne Delle heilen (rms/S0 1,6e-4 / 1,9e-4). Programmklasse "Kaverne" in je 14
  von 24 Dellen (mittel w = 4, 8; tief, sehr tief, voll alle w); aber t_kav (Leerlaenge >= 10) ist in 48 von 48 Dellen
  undefiniert, die Leerlaenge zur Laufmitte ist 0,0 in 45 von 48 (sonst 1,2 bis 2,4) und am Ende <= 0,4: die Dellen
  schliessen sich und lassen nur eine Schwingung unter S0/2 zurueck. Zum Vergleich S0 = 0,95: acht Dellen mit t_kav 35
  bis 280 und Leerlaenge am Ende 14 bis 42 (wachsend). Nach meiner vorab festgelegten Lesart (Klasse) ist (a)
  **verfehlt**; nach dem Wortlaut der Scheiterregel ("dauerhaft aufreissen") reisst bei S0 >= 1,05 nichts dauerhaft auf.
  Ich lasse beides stehen.
- **(b) verfehlt:** bei 0,95 kavitiert die volle Delle mit w = 1 dauerhaft (t_kav 280, Leerlaenge Ende 26,4), ebenso
  voll w = 2 (41), tief w = 4 (52) und w = 8 (46), sehr tief w = 4 / 8 (39 / 38), voll w = 4 / 8 (36 / 35). Schmale tiefe
  Dellen (tief w = 1, 2) heilen bei 0,95 (bei 0,70 bis 0,75 kavitierten sie); die Verschiebung zu breiteren Dellen gibt
  es also fuer "tief", nicht fuer "voll".
- **(c) getroffen:** F_b = 1,5e-4 (0,68), 1,49e-3 (0,70), 4,9e-3 (0,72), 1,52e-2 (0,75), 5,1e-2 (0,80), 0,118 (0,85),
  0,228 (0,90), 0,401 (0,95), 0,553 (0,98), 0,619 (0,99); monoton, Grenzwert der bounce-Formel bei S_t -> 0 ist
  sqrt(2)/2 = 0,707 [Hand]. Kleinste Barriere bei 0,68 (Gegenprobe). Konvention geprueft: F_b = sqrt 2 Int (S0 - S)
  sqrt((S - S_t)/S) dS folgt aus E = Int(|f'|^2 + U - omega^2 S) mit f'^2 = (S - S0)^2 (S - S_t)/2 [Hand].
- **(d) halb:** Fehltreffer (R7): 1,177 w = 1,18 / 1,18 / 1,18 / 2,35 / 1,18 gegen x_halb = 5,01 / 4,05 / 3,37 / 3,37 / 2,87:
  alle schmaler als der Keim, Scheiterregel nicht ausgeloest. Die zweite Haelfte ("alle richtig kavitierenden
  w >= w*") ist verfehlt: 0,70 tief w = 1 (1,18 < 5,01) kavitiert (t_kav 27), ebenso 0,72 tief w = 1 (36).
- **(e)** nicht geprueft. Gegenprobe P = S0^2 (S0 - 1) [Hand, aus P = S U' - U]: -0,147 (0,70) bis -0,128 (0,80) < 0.
- **Ausgang: gemischt** ((b) verfehlt, (c) getroffen, (a) nach Lesart verfehlt / nach Wortlaut nicht, (d) halb).
  Belegstufe [num] (eine Gitterstufe), [Hand].
- **Vorschlag:** parken; wenn weiter, das Kriterium "dauerhaft" (t_kav, Leerlaenge am Ende) vorab binden und die
  feine Stufe nachholen.

## Idee 9: Spinmischung mit Verstimmung (gfbic_delta.py spektrum, P1, g = 0,2)

- **Vorhersage (kurz):** Fenster |delta| < 0,081 (+-10 %); lambda(0,05) = 0,036 (+-10 %); delta = 0,10 stabil.
- **Codeaenderung (Kopie gfbic_delta.py, Diff gfbic_delta.diff):** DELTA_M2 aus --delta-m2 auf die Diagonale des
  psi_2-Operators in koeff (FD), lin_g (Schiessen, dv und d0) und lu_zaehlung (L_u, L_v, L_0).
- **Laeufe:** z9d0 / z9d005 / z9d010 / z9d008 (265 / 225 / 237 / 212 s, cpu6):

  | delta | lambda Schiessen B | FD Richardson | Zwei-Moden-Formel der Idee | n(L_u) | reelle gebundene Mode |
  |---|---|---|---|---|---|
  | 0 (Kontrolle) | 0,046238 (R8: 0,0462384) | 0,046238 | 0,04531 | 1 | - |
  | 0,05 | 0,038063 | 0,038063 | 0,03563 | 1 | - |
  | 0,08 | 0,017870 | 0,017870 | 0,00684 | 1 | - |
  | 0,10 | keine (Newton auf der imaginaeren Achse findet die reelle Mode 0,026689) | keine instabile | stabil | 0 | 0,026689 |

  - lambda(0,05) = 0,0381 liegt im Vorab-Fenster 0,0324 bis 0,0396 und in der Scheiterschwelle 0,030 bis 0,042.
  - Bei delta = 0,10 keine instabile Mode (FD und Schiessen, n(L_u) = 0); die Nullmode ist zur reellen gebundenen Mode
    0,0267 geworden. Fensterrand aus L_u,min = -6,8e-3 (0,08) und +1,3e-2 (0,10): delta_c ~ 0,087 [Hand, linear],
    im Vorab-Fenster 0,073 bis 0,089. Die Kreisform der Idee unterschaetzt lambda nahe dem Rand (0,08: 0,0179 gegen
    0,0068).
  - Gegenprobe delta -> -delta (Ergaenzungslauf z9dm005, delta = -0,05, 245 s, nach dem Hauptergebnis): lambda =
    0,034218 (Schiessen B; FD 0,034196) gegen 0,038063 bei +0,05, also nur naeherungsweise symmetrisch (11 %
    Unterschied); beide Werte liegen im Band 0,030 bis 0,042. Die Zwei-Moden-Formel ist gerade in delta [Hand], das
    volle Problem nicht (bei -0,05 erscheinen zudem zwei reelle gebundene psi_2-Moden 0,0848 und 0,0942 unter der
    Kante).
- **Scheiterregeln:** keine ausgeloest.
- **Ausgang: getroffen.** Belegstufe [num+K] (Schiessen zwei Stufen und FD mit Richardson stimmen auf 1e-6; Kontrolle
  delta = 0 reproduziert R8).
- **Vorschlag:** weiter (Fensterrand delta_c(g) an zwei weiteren g; -delta).


- **Vorhersage (kurz):** (a) starre Mitdrehung gaebe Praezession ~1/r, GP-B/LAGEOS-Faktor 1,75 statt 5,3,
  ausgeschlossen; Gordon mit kappa = 1 gibt g_0i mit Faktor 4; (b) Kerr ist nicht exakt als Gordon-Metrik eines
  isotropen bewegten Mediums schreibbar.
- **Hand:** Gordon g = eta + (1 - 1/n^2) u u (Vorzeichen: ruhendes Medium g_00 = -1/n^2, Lichtgeschwindigkeit 1/n).
  Mit n^2 - 1 = 4|Phi|/c^2 und u = (1, v/c): g_0i = -(1 - 1/n^2) v_i/c = -4 G M v_i/(r c^3), Einsteins
  gravitomagnetisches Potential, Faktor 4. Verhaeltnis der Radien 12270/7030 = 1,745, hoch drei 5,31. Starre
  Mitdrehung v = Omega x r gibt g_0i unabhaengig von r und eine Drehrate ~ Omega/r. Stimmt.
- **Literatur [L]:** Garat und Price, PRD 61, 124011 (2000), arXiv gr-qc/0002013, Abstract: keine konform flachen,
  achsensymmetrischen Schnitte der Kerr-Raumzeit, die im Schwarzschild-Grenzfall in Schnitte konstanter Zeit
  uebergehen. Visser und Weinfurtner, CQG 22, 2493 (2005), arXiv gr-qc/0409014, Abstract: Aequatorschnitt von Kerr
  als Wirbelgeometrie; "it is not possible to put the entire Kerr spacetime into perfect-fluid acoustic form". Beide
  Zitate der Idee stimmen. Fuer die relativistische Gordon-Form mit schnellem Medium ist der raeumliche Teil
  delta_ij + alpha u_i u_j nicht konform flach; Garat/Price greift dafuer nicht unmittelbar [Hand]. Zwei arXiv-Suchen
  ("Gordon metric Kerr moving medium", "Kerr Gordon metric") ergaben keine Arbeit zu einer exakten Gordon-Darstellung
  von Kerr. Anmerkung [H]: Die Kerr-Schild-Form eta + 2 H k k mit lichtartigem k ist der entartete Grenzfall n -> 1,
  u -> lichtartig, kein isotropes Medium mit endlichem n.
- **Scheiterregeln:** (a) nicht ausgeloest (Faktor 4). (b) nicht ausgeloest, aber nur mangels gefundener Quelle.
- **Ausgang: (a) getroffen [Hand]; (b) nicht entscheidbar** (Literatur unvollstaendig; keine eigene Rechnung).
- **Vorschlag:** parken (die Frage "Kerr in Gordon-Form" waere eine eigene Papierkarte mit Literaturlauf).

## Laeufe (.69, Zeiten UTC aus den Logs; alle rc = 0 ausser z3bb, z7rauch)

| Lauf | Spur | Inhalt | Start | Dauer |
|---|---|---|---|---|
| z1ua / z1ub / z1uc | cpu6 / cpu6 / cpu2 | ueberlapp fein a / b / c | 06:22:19 / 06:29:49 / 06:56:46 | 430 / 448 / 511 s |
| z3ba / z3bb (ungueltig) / z3bc | cpu6 | bruecke l = 1, Teil a / b (Locale-Fehler) / b repariert | 06:41:54 / 06:48:25 / 07:57:39 | 159 / rc 1 / 175 s |
| z4pa / z4pb / z4pc / z4pd | cpu6 / cpu6 / cpu2 / cpu2 | pole l = 2 a / b / c, l = 3 | 06:58:56 / 07:06:06 / 06:36:57 / 06:51:50 | 202 / 129 / 208 / 212 s |
| z8kv / z8ka | cpu2 | Keimtabelle / Raster 0,95, 1,05, 1,2 | 06:26:18 / 06:27:12 | 4,7 / 223 s |
| z9d0 / z9d005 / z9d010 / z9d008 | cpu6 | spektrum delta 0 / 0,05 / 0,10 / 0,08 | 06:37:21 / 06:44:38 / 06:54:56 / 07:02:32 | 265 / 225 / 237 / 212 s |
| z7rauch (rc 1) / z7rauch2 / z7gpu | cpu6 / cpu6 / p4000a | Idee 7 Rauch / Rauch repariert / Hauptlauf | 06:41 (Unit ab 06:32:52) / 08:00:37 / 08:00:43 | - / 3 / 209 s |
| z4pe / z9dm005 (Kette E) | cpu6 | Ergaenzung Idee 4 (0,69 / 0,71) / Idee 9 (delta = -0,05) | 08:11:54 / 08:14:17 | 140 / 245 s |
| z3ca / z3cb (Kette F) | cpu2 | Ergaenzung Idee 3, Gegenprobe l = 0, Teil a / b | 08:13:54 / 08:17:40 | 222 / 164 s |

- Lokal kein python, python3, awk; jq auf der .69. Keine Originaldatei geaendert; Codeaenderungen nur in
  gfbic_delta.py (Diff beiliegend) und t5k_zus7.py (neu, aus t5k.py).

## Einfach gesagt

Von zehn Ideen haben vier den Rechentest bestanden: Die zweite Leiter stiller Stellen folgt tatsaechlich dem
Zaehlgesetz der Kugelform (vier neue Stellen auf zwei Zehntausendstel genau), die seitliche Schwappmode wird auf
dem Weg von einer zu drei Dimensionen bei 2,6 Dimensionen einmal ganz still, die Tropfenschwingung tritt bei etwa 0,70
ueber die Kante und bleibt danach ohne stille Stelle, und ein kleiner Massenunterschied zwischen den Feldsorten
schliesst die Umwandlungs-Instabilitaet genau im vorhergesagten Fenster. Die Oszillon-Idee fuer den Rest der
Teilchen-Antiteilchen-Vernichtung ist gescheitert, fuer das eng gestartete Paar entsteht aber ein langlebiger
Klumpen, der seine Ladung hin und her tauscht. Die Kavitationsidee ist halb richtig (die Barriere waechst wie
vorhergesagt, aber volle Loecher reissen auch bei fast dichtem Kondensat noch auf). Drei Ideen (Rotor, Dunkelzustand,
Kerr) konnten mit den Mitteln der Runde nicht entschieden werden. Alles bleibt Modellrechnung.

**Ende: 2026-09-30 10:21:03 CEST (date, nach dem Schreiben gemessen).** Ergaenzungslaeufe (Ketten E, F) eingearbeitet; Ausgaben in pruefung/lauf-69/ (ohne Rohfelder .pt).
