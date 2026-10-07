# Runde 3: Ergebnisse der gerechneten Tests (Auswertung)

Bearbeiter: Anthropic-Agent (Opus 5.5) im Auftrag der Leitung claude-primary. Reine Lese- und Schreibarbeit, nichts
gerechnet. Explorativ; keine Abschaetzung, die Leitung entscheidet.

- **Beginn:** 2026-09-30 02:52:48 CEST (gemessen mit date)
- **Ende:** 2026-09-30 03:15:06 CEST (gemessen mit date)

**Grundlage:**
- README.md (Latten L1 bis L5), RUNDE-03.md (Karten), die zwei PLAN.md (Vorhersagen; tests1d-r3/PLAN.md mit Abschnitt 12
  fuer t2 Version 2)
- Berichte in tests1d-r3/lauf-69/ausgabe/ und tests2d-r3/lauf-69/ausgabe/; fuer t2 auf Weisung der Leitung auch
  t2_ergebnis.json
- LAUF.log, LAUF-T2V2.log und R3-2D.log (Ablauf, Abbruch), KNOTEN-PAPIER.md
- Hintergrund: REVIEW-FABLE.md, RUNDE-02.md; Hinweis der Leitung zur Brechung mit Verweis auf RUNDE-06/weber/PLAN.md

**Lesehilfe:**
- Alle Zahlen stammen aus den Berichten. "nicht im Bericht" heisst, der Bericht nennt die Groesse nicht.
- "getroffen / verfehlt / teilweise" misst am jeweiligen PLAN.md, nicht an der Natur.
- Wo ich eine Spalte erklaere, stuetze ich mich auf den Code; das ist vermerkt. Zahlen aus Code oder JSON habe ich nur
  bei t2 uebernommen (dort als Quelle freigegeben).
- Alle Hauptlaeufe liefen am 30.09. auf der Quadro P4000, jeder unter 10 min (laengste Unit: 2D-Tropfen, 4 min 53 s).

## 1. Je Test

### 1D-Tests (tests1d-r3)

#### Profil (Grundlage aller 1D-Tests, keine Karte)

- **Vorhersage** (PLAN 3): Kontrolle K0, max |f_Schuss - f_Anker| <= 1e-6 auf beiden Gittern.
- **Ergebnis:** K0 bestanden, max 9,84e-11. f0^2 Schuss 0,552786404508 gegen Anker 0,552786404500 (omega^2 = 0,6), die
  anderen drei omega ebenso nah. Schiessen 81,8 s.
- **Treffer:** getroffen.
- **L3:** entfaellt; K0 auf grobem und feinem Gitter gleich.
- **Latten:** entfaellt (keine Karte).
- **Vorschlag:** keine Karte; die Grundlage traegt t1 bis t5.

#### t1, Chemie 1 (Elektronegativitaet)

- **Vorhersage** (PLAN 4): "Ladung pendelt, die Richtung folgt der Anfangsphase; im Phasenmittel fliesst nichts von klein
  nach gross."
  - Periode 2 pi/(omega1 - omega2) = 52,4. Amplitude etwa 0,46 / 0,16 / 0,05 bei d = 8 / 10 / 12, Faktor 2 unsicher.
    Mittelwerte je phi0 etwa -A cos phi0.
  - Urteil erwartet: d = 12 "kein Nettofluss", d = 10 "nahe der Schwelle, eher 'gegen H'", d = 8 "offen". "In keinem Fall
    erwarte ich 'klein -> gross'."
  - Zweite Ordnung (Hypothese): kleiner Gleichanteil gegen H, etwa 25 Prozent von A bei d = 10 und 7 Prozent bei d = 12.
  - Gleiche omega und Spiegel: unter 1e-10.
- **Ergebnis** (fein, T = 400):

  | d | mittleres dQ_klein bei phi0 = 0 / pi/2 / pi / 3pi/2 | Phasenmittel | Amplitude | Periode | Urteil laut Bericht |
  |---|---|---|---|---|---|
  | 8 | -0,5742 / -0,2373 / 0,4223 / 1,937 | 0,3868 | 0,0224 | 351 | Nettofluss gross -> klein (gegen H) |
  | 10 | -0,1616 / -0,04969 / 0,1772 / -0,1893 | -0,05586 | 0,0479 | 43,88 | Nettofluss klein -> gross (H) |
  | 12 | -0,04914 / -0,00509 / 0,05933 / 0,01106 | 0,00404 | 0,05403 | 50,14 | kein Nettofluss: Pendeln (Josephson) |

  - Kontrollen: Spiegel-Differenz hoechstens 2,22e-16, gleiche omega hoechstens 4,408e-16.
  - Q_klein(0) = 2,07821. Laut Code ist das die Ladung links von x = 0 zu Beginn des ersten Laufs (d = 8, phi0 = 0),
    nicht das Anker-Q 1,8859.
  - Kein Vermerk "(verschmolzen)" im Bericht (Code-Kriterium: Endabstand unter d/2).
- **Treffer:** teilweise.
  - d = 12 getroffen: Pendeln, Periode 50,14 gegen 52,43, Amplitude 0,05403 gegen 0,05, Vorzeichenmuster wie -A cos phi0.
    Das Phasenmittel 0,00404 ist positiv, zeigt also in die Richtung der Hypothese zweiter Ordnung.
  - d = 10 verfehlt: "klein -> gross" war ausgeschlossen. Die Amplitude 0,0479 liegt unter dem Band um 0,16. Das Mittel
    bei 3pi/2 (-0,1893) ist nicht nahe null. Das Phasenmittel hat das Gegenvorzeichen der Hypothese zweiter Ordnung.
  - d = 8: Urteil vorab offen. Gemessen "gegen H", aber mit Amplitude 0,0224 statt etwa 0,46 und Periode 351 (Abschnitt 3).
- **L3:** bestanden. Quoten fuer Phasenmittel und Mittel bei phi0 = 0 (laut Code): 3805 und 5563 (d = 8), 597,1 und
  1937 (d = 10), 177,1 und 1294 (d = 12); Schwelle 5.
- **Latten:** L1 ja; L2 bestanden; L3 bestanden; L4 teilweise; L5 mittelbar.
- **Vorschlag:** weiter; d = 10 widerspricht der Vorhersage bei bestandenem L2 und L3, und d = 8 ist im Messfenster nicht
  als Pendeln aufgeloest.

#### t2, Chemie 2/3 (Bindungskurve und Morse), Version 2

- **Stand:** Version 1 brach ab ("RuntimeError: Relaxation instabil", LAUF.log, rc 1). Version 2 mit Punktzwang in der
  Mitte statt Schwerpunktzwang (PLAN 12) lief fehlerfrei (LAUF-T2V2.log, rc 0; 63,3 s). Die Vorhersagen sind unveraendert.
- **Vorhersage** (PLAN 5): "Gleichphasig gibt es kein Molekuel; das einzige Minimum ist der verschmolzene Ball."
  - Lage d0 = 2X = 2,6, Tiefe D = 2 E1(q) - E1(2q) = 4,597 - 4,149 = 0,448, omega^2 etwa 0,516; kein Minimum bei getrennten
    Baellen.
  - Delta phi = pi: E_int > 0 bei allen d, monoton fallend, kein Minimum.
  - Asymptotik: E_int(0) bei d = 8 / 10 / 12 etwa -0,052 / -0,0174 / -0,0058; kappa auf 10 Prozent; E_int(pi)/E_int(0)
    bei d = 10 und 12 zwischen -1,2 und -0,8.
  - Morse: Rest unter 5 Prozent von D, a zwischen 0,4 und 0,9; Schwanzkoeffizient in der Groesse von 4,16 (Faktor 2).
  - Schwingung omega_vib etwa 0,5 (0,4 bis 0,75).
  - Kontrollen: |E(40) - 2 E1| unter 1e-4; Konvergenz unter 1e-3 |E_int| bei d <= 10.
- **Ergebnis** (fein, tau = 600):
  - **Minimum (freier Lauf):** d_ist 2,6370 (Parabel 2,6514), E_int -0,44836, omega 0,71840, Kruemmung 0,7753,
    omega_vib 0,8214. Gesamtenergie E = 4,14884 (t2_ergebnis.json).
  - **Delta phi = 0, gehaltene Laeufe:** d_ist 2,8399 bis 10,5166; E_int steigt monoton von -0,4347 auf -0,006593.
    Links vom Minimum (Zwangwert c = 0,95 / 1,05 / 1,2): d_ist 2,5431 / 2,3601 / 2,1463, E_int -0,4439 / -0,3953 /
    -0,1916. Bericht: "0 alle negativ True (ab Minimum True)".
  - **E_int(0) an den Sollabstaenden:** 2,5: -0,4325; 3: -0,4123; 4: -0,2508; 6: -0,08173; 8: -0,02728; 10: -0,009074;
    12: kein Wert.
  - **Delta phi = pi:** Alle Laeufe enden bei d_ist 13,52 bis 16,10, obwohl d_start von 1,5 bis 13 reicht. E_int von
    3,963e-02 auf 6,789e-04. Bericht: "pi alle positiv True, pi monoton fallend True". An den Sollabstaenden 2,5 bis 12
    kein feiner pi-Wert; grob nur bei 12 (0,0557648). E_int(pi)/E_int(0): alle null.
  - **Morse** (0, fein): D 0,4182, a 0,926, d0 1,549, rms/D 0,0345, omega_vib 0,790, Schwanzkoeffizient 3,509; grob a
    0,939.
  - **Asymptotik:** 0: C 2,236, kappa 0,5542. pi: C 5177, kappa 0,8712. Vorhersage kappa 0,5477, C 4,1569.
  - **Kontrollen:** Referenz d = 40: -5,9e-09 (0) und -3,4e-09 (pi). Konvergenz bei 0 hoechstens 3,4e-08, insgesamt
    hoechstens 1,398e-04 (pi). Keine ungebundenen Laeufe.
- **Treffer:** teilweise.
  - Getroffen: Es gibt kein Minimum bei getrennten Baellen. Das Minimum liegt bei 2,637 mit Tiefe 0,44836 (vorhergesagt
    2,6 und 0,448). pi ist positiv und monoton. kappa(0) = 0,5542 liegt innerhalb 10 Prozent. Der Morse-Rest betraegt
    0,0345 D. Der Schwanzkoeffizient 3,509 liegt im Faktor 2.
  - Verfehlt:
    - Morse a = 0,926 liegt knapp ausserhalb 0,4 bis 0,9. Nach der PLAN-Regel ist das "Scheitern von H (Morse-Bindung)".
    - omega_vib 0,79 bis 0,82 statt 0,4 bis 0,75.
    - Asymptotik-Amplitude C 2,236 statt 4,16; E_int(0) bei 8 und 10 betraegt -0,02728 und -0,009074 statt -0,052 und
      -0,0174.
    - Die pi-Seite ist nur zwischen 13,5 und 16,1 belegt; das Verhaeltnis pi/0 ist nicht bestimmbar.
- **Frage der Leitung: Ist das Minimum ein gebundenes Paar mit Abstand oder der verschmolzene Einzelball?**
  - Der Bericht nennt die Form nicht: weder die Zahl der Maxima noch phi(0) des freien Laufs ("Zwangwert -"). Auch
    t2_ergebnis.json hat dafuer kein Feld.
  - Alle Kennzahlen des freien Laufs stimmen mit den vorab gerechneten Werten des verschmolzenen Einzelballs der Ladung
    2q ueberein:
    - Energie E 4,14884 gegen E1(2q) = 4,149
    - d 2,637 gegen 2X = 2,6
    - omega 0,71840 gegen omega^2 etwa 0,516
  - d ist 2X mit X als Schwerpunkt von phi^2 auf x > 0. Das ist auch fuer einen einzelnen Ball ungleich null.
    d = 2,64 zeigt also nicht, dass zwei Baelle vorliegen.
  - Der freie Lauf liegt zwischen den gehaltenen Laeufen mit c = 0,95 (d_ist 2,5431) und c = 0,8229 (d_ist 2,8399). Der
    Scheitel 0,906 des verschmolzenen Balls (PLAN 12) liegt im selben Intervall.
  - **Einordnung:** Die Zahlen passen zum verschmolzenen Einzelball, die Form ist aber nicht ausgegeben. Deshalb ist das
    eine **offene Frage an die Leitung, kein Befund**. Pruefschritt: phi des freien Laufs ausgeben (ein oder zwei Maxima,
    phi(0) gegen 0,906).
- **L3:** bestanden, min 47,29; nur fuer Delta phi = 0 an den Sollabstaenden 2,5 bis 10. Fuer pi gibt es keinen
  L3-Wert.
- **Latten:** L1 ja; L2 teilweise; L3 bestanden; L4 weitgehend; L5 nein.
- **Vorschlag:** parken ("bekannt") nach Klaerung der Formfrage. Das einzige Minimum traegt die vorab abgeleiteten Werte
  des verschmolzenen Balls, bei getrennten Baellen gibt es keins; offen sind Form und pi-Seite.

#### t3, Chemie 7 (Aktivierungsenergie, Stoesse)

- **Vorhersage** (PLAN 6): "Gleichphasige verschmelzen langsam und laufen schnell durch; gegenphasige verschmelzen bei
  keinem v."
  - Delta phi = 0: verschmolzen bei v <= 0,2, getrennt bei v >= 0,45; keine Barriere, sondern eine obere Grenze.
  - Delta phi = pi: getrennt bei allen sechs v; bei v = 0,05 Abprall bei d etwa 12.
  - Delta phi = +-pi/2: langsam verschmolzen (v <= 0,2), schnell getrennt mit Ladungsasymmetrie ueber 10 Prozent.
  - Gegenprobe: +pi/2 und -pi/2 mit gleichen Klassen und entgegengesetzter Asymmetrie. L3: hoechstens eine Klasse wechselt.
- **Ergebnis** (fein, T = 800):

  | Delta phi | v = 0,05 | 0,1 | 0,2 | 0,3 | 0,45 | 0,6 |
  |---|---|---|---|---|---|---|
  | 0 | gebunden/unklar | gebunden/unklar | gebunden/unklar | getrennt | getrennt | getrennt |
  | +pi/2 | abgeprallt | abgeprallt | abgeprallt | abgeprallt | durchgelaufen | durchgelaufen |
  | pi | getrennt | getrennt | getrennt | getrennt | getrennt | getrennt |
  | -pi/2 | abgeprallt | abgeprallt | abgeprallt | abgeprallt | durchgelaufen | durchgelaufen |

  - In keinem Lauf die Klasse "verschmolzen"; die Barriere-Angaben sind in allen vier Zeilen null.
  - Kleinster Abstand sep_min:
    - Delta phi = 0 bei v = 0,05 / 0,1 / 0,2: 2,506 / 2,502 / 2,453
    - Delta phi = pi bei v = 0,05: 11,891
    - +-pi/2 bei v = 0,05 bis 0,3: 10,494 / 8,425 / 6,434 / 5,255
  - Ladungsasymmetrie bei +pi/2, laut Code (q_r - q_l)/(q_r + q_l): 0,0533 / 0,09646 / 0,1651 / 0,1873 / 0,1598 / 0,1082.
    Bei -pi/2 dieselben Betraege mit umgekehrtem Vorzeichen.
- **Treffer:** teilweise.
  - pi getroffen: alle getrennt, sep_min 11,891 bei v = 0,05.
  - 0 teilweise: Langsame bleiben beisammen, schnelle trennen sich, der Umschlag liegt zwischen 0,2 und 0,3. Die langsamen
    heissen aber "gebunden/unklar", nicht "verschmolzen".
  - +-pi/2 teilweise: schnell getroffen (durchgelaufen, Asymmetrie 0,1598 und 0,1082). Langsam verfehlt: abgeprallt statt
    verschmolzen, ohne naeher als 5,255 zu kommen.
- **L3:** bestanden; 0 von 24 Klassen weichen fein gegen grob ab, max |v_aus fein - grob| 0,0007998.
- **Latten:** L1 ja; L2 bestanden; L3 bestanden; L4 teilweise; L5 nein.
- **Vorschlag:** weiter. Die langsamen +-pi/2-Stoesse widersprechen der Vorhersage, und "gebunden/unklar" bei
  Delta phi = 0 entscheidet die feste Klassenregel nicht.

#### t4, Chemie 15 (Redox ueber Bruecke)

- **Vorhersage** (PLAN 7): "Die Anfangssteigung faellt nicht exponentiell mit der Brueckenzahl."
  - Rohsteigung D0: n = 0 etwa 0,016, n >= 1 etwa 0,008 und fast unabhaengig von n; Verhaeltnisse etwa 0,5 / 1 / 1.
  - Spendereffekt: faellt steil, Faktor 0,01 bis 0,05 je Bruecke. Bei n = 3 unter 1e-6, "dass L3 dort wahrscheinlich
    reisst".
  - D90 wie D0, nur bei n = 0 mit linearem Anfang, Steigung etwa 0,02.
- **Ergebnis** (Steigung der Empfaengerladung auf [2, 15], fein, T = 400):

  | n | D0 roh | D0 Spendereffekt | D90 roh | D90 Spendereffekt | ohne Spender |
  |---|---|---|---|---|---|
  | 0 | 2,2700e-02 | 2,2699e-02 | -3,8035e-03 | -3,8045e-03 | 9,8636e-07 |
  | 1 | 9,4386e-03 | -3,4391e-03 | 1,5017e-02 | 2,1393e-03 | 1,2878e-02 |
  | 2 | 1,1825e-02 | -8,1655e-05 | 1,1953e-02 | 4,6278e-05 | 1,1906e-02 |
  | 3 | 1,1900e-02 | -1,7026e-06 | 1,1902e-02 | 9,6465e-07 | 1,1902e-02 |

  - Verhaeltnisse s(n+1)/s(n):
    - D0 roh 0,4158 / 1,2528 / 1,0063
    - D0 Spendereffekt 0,1515 / 0,02374 / 0,02085 (Spreizung 7,27)
    - D90 roh 3,948 / 0,7959 / 0,9958
    - D90 Spendereffekt 0,5623 / 0,02163 / 0,02084 (Spreizung 26,98)
    - Urteil in allen vier Faellen "nicht exponentiell".
  - Spendereffekt bei t = 100 (D0), n = 0 bis 3: 0,1244 / 0,7183 / -0,05458 / -0,05514.
- **Treffer:** teilweise.
  - Rohsteigung getroffen: nicht exponentiell, Muster 0,42 / 1,25 / 1,01 wie vorhergesagt 0,5 / 1 / 1. Die Betraege
    0,0227 und 0,0094 bis 0,0119 liegen ueber den Handwerten 0,016 und 0,008.
  - Spendereffekt teilweise: Die Schritte ab n = 1 (0,02374; 0,02085) liegen im Band 0,01 bis 0,05, der erste (0,1515)
    nicht. Bei n = 3 betraegt er 1,7e-06, knapp ueber "unter 1e-6". L3 riss dort nicht, anders als vorhergesagt.
  - D90 bei n = 0 verfehlt: -3,8e-03 statt etwa +0,02.
- **L3:** bestanden, min 42,79 (Steigung) und 41,39 (Spendereffekt).
- **Latten:** L1 ja; L2 bestanden; L3 bestanden; L4 teilweise; L5 mittelbar.
- **Vorschlag:** parken ("bekannt"). Rohsteigung und Spendereffekt ab n = 1 kamen so, wie PLAN 7 sie aus dem
  Schwanzabfall abgeschaetzt hatte. Offen sind nur der erste Schritt und die nicht ausgewertete Spaetphase (Abschnitt 3).

#### t5, Chemie 14 (Zufallskarte): Q gegen Anti-Q

- **Vorhersage** (PLAN 9): "Q und Anti-Q vernichten sich in T = 1000 nicht zur Haelfte; nah beieinander bleibt ein
  ladungstauschendes Gebilde."
  - d = 3: Q_abs(0)/2q etwa 0,6 bis 0,8; Verlust 10 bis 40 Prozent mit t10 unter 100; t50 (geglaettet) nicht erreicht;
    Endzustand "Restgebilde mit Ladungstausch".
  - d = 5: Verlust unter 10 Prozent. d = 8 und 12: Rest Q_abs ueber 0,95 bzw. 0,99, "Restbaelle".
  - Kontrolle Ball-Ball: Verlust unter 2 Prozent; gleichphasig verschmelzen bei d = 3 und 5, gegenphasig Abstossung.
  - "H scheitert, wenn t50 bei d = 8 oder 12 erreicht wird, oder wenn bei d = 3 nichts Lokalisiertes bleibt."
- **Ergebnis** (fein, T = 1000):

  | d | Art | theta | Q_abs0/2q | t10 | t50 glatt | Rest Q_abs | Rest E | Q ges. Ende | Klumpen | Wechsel | Endzustand laut Bericht |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | 3 | anti | 0 | 0,6444 | 21 | 274,5 | 0,2208 | 0,6407 | 5,6e-17 | 1 | 14 | Restgebilde mit Ladungstausch |
  | 3 | anti | pi | 0,6444 | 75 | 453,5 | 0,3569 | 0,8481 | -1,6e-15 | 2 | 12 | Restgebilde mit Ladungstausch |
  | 5 | anti | 0 | 0,8605 | 21,5 | 201,5 | 0,1864 | 0,5778 | 0 | 1 | 14 | Restgebilde mit Ladungstausch |
  | 5 | anti | pi | 0,8605 | 59,5 | 266,5 | 0,1852 | 0,5491 | -3,9e-16 | 1 | 14 | Restgebilde mit Ladungstausch |
  | 8 | anti | 0 | 0,9709 | 32 | 67 | 0,02171 | 0,05204 | 0 | 0 | 0 | Strahlung, nichts Lokalisiertes |
  | 8 | anti | pi | 0,9709 | 34 | 68 | 0,01945 | 0,04759 | 2,1e-16 | 0 | 0 | Strahlung, nichts Lokalisiertes |
  | 12 | anti | 0 | 0,9967 | 178,5 | 194 | 0,01633 | 0,0463 | 0 | 0 | 0 | Strahlung, nichts Lokalisiertes |
  | 12 | anti | pi | 0,9967 | 180,5 | 195,5 | 0,01094 | 0,0465 | -3,1e-16 | 0 | 2 | Strahlung, nichts Lokalisiertes |
  | 3 | gleich | 0 | 1,6881 | - | - | 0,9945 | 0,9799 | 8,198 | 1 | 0 | Restball/Restbaelle |
  | 3 | gleich | pi | 0,3119 | 168 | 223,5 | 0,002677 | 0,002434 | 0,004049 | 0 | 0 | Strahlung, nichts Lokalisiertes |
  | 5 | gleich | 0 | 1,3847 | - | - | 0,9431 | 0,9102 | 6,373 | 1 | 0 | Restball/Restbaelle |
  | 5 | gleich | pi | 0,6153 | 277 | 288,5 | 0,009074 | 0,008814 | 0,02657 | 0 | 0 | Strahlung, nichts Lokalisiertes |
  | 8 | gleich | 0 | 1,1225 | 472,5 | - | 0,7436 | 0,7143 | 4,076 | 1 | 0 | Restball/Restbaelle |
  | 8 | gleich | pi | 0,8775 | 510,5 | 527 | 0,04856 | 0,05096 | 0,2081 | 0 | 0 | Strahlung, nichts Lokalisiertes |
  | 12 | gleich | 0 | 1,0210 | 796,5 | - | 0,707 | 0,6827 | 3,525 | 1 | 0 | Restball/Restbaelle |
  | 12 | gleich | pi | 0,9790 | - | - | 1 | 1 | 4,781 | 2 | 0 | Restball/Restbaelle |

- **Treffer:** verfehlt, nach der eigenen Regel des PLAN. t50 wird bei d = 8 (67 und 68) und d = 12 (194 und 195,5)
  erreicht, dort bleibt nichts Lokalisiertes.
  - Getroffen nur bei d = 3: Anfangswert 0,6444, t10 21 und 75, Ladungstausch-Gebilde mit 12 bis 14 Wechseln. Aber auch
    dort wird t50 erreicht (274,5 und 453,5).
  - d = 5: Rest 0,1864 und 0,1852 statt Verlust unter 10 Prozent.
  - Kontrolle: Nur d = 3 gleichphasig (0,9945) und d = 12 gegenphasig (1) bleiben ueber 0,98. Die gegenphasigen Paare bei
    d = 3, 5 und 8 enden als "Strahlung, nichts Lokalisiertes".
- **L3:** bestanden. Laut Code auf 1 - Rest Q_abs; kleinste Quote 9,365 (Kontrolle d = 12, pi), Anti-Laeufe 453,3 bis
  5,111e+05.
- **Latten:** L1 ja; L2 gerissen; L3 bestanden; L4 teilweise; L5 nein.
- **Vorschlag:** weiter mit einem Umbau. Die Vorhersage scheitert klar, aber die Ball-Ball-Kontrolle reisst ebenfalls;
  vor jeder Lesart ist die Ladungsbilanz zu klaeren (Abschnitt 3).

#### t6, Wellen 5 (Rumpfgeschwindigkeit), Papierprobe

- **Vorhersage** (PLAN 8): "Wellen 5 (Rumpfgeschwindigkeit) ist im Ein-Feld-Modell nicht umsetzbar. t6 rechnet nur die
  Dispersionstabelle, keine Zeitentwicklung."
  - S < 2/3: modulationsinstabil, groesste Wachstumsrate etwa S, v_c = 0, keine Landau-Schwelle.
  - S >= 2/3: stabil, c_s = 0,31 / 0,55 / 0,71 bei S = 0,7 / 0,8 / 1,0; omega_bg <= 0,707; Gegenpunkt 2 - 2S unter S.
- **Ergebnis** (Papierprobe mit Rechner, keine Messung):
  - S = 0,001 / 0,002 / 0,01 / 0,1 / 0,5: instabil.
    - Wachstumsrate 0,0009995 / 0,001998 / 0,009949 / 0,09415 / 0,2041
    - Verstaerkung in 400 bis 2,884e+35
    - v_c (Raster) 0,0002451 / 0,002024 / 0,0007538 / 0,001248 / 0,008119
  - S = 0,6667: stabil, Rate 0, v_c (Raster) 8,66e-05.
  - S = 0,7 / 0,8 / 1: stabil.
    - c_s = v_c = 0,3076 / 0,5547 / 0,7071
    - omega_bg 0,5788 / 0,6 / 0,7071
    - Gegenpunkt 0,6 / 0,4 / 0
- **Treffer:** getroffen (als Papierprobe). Bei S = 0,5 ist die Rate 0,2041 und nicht "etwa S"; die Vorhersage nannte
  kleines S.
- **L3:** entfaellt (keine Zeitentwicklung).
- **Latten:** L1 nein; L2 entfaellt; L3 entfaellt; L4 ja; L5 mittelbar.
- **Vorschlag:** parken als "im Ein-Feld-Modell nicht umsetzbar". Erst mit einem zweiten Feld als Medium gaebe es eine
  neue Karte (PLAN 8; Fable-Review Z. 40 bis 47: duennes Medium modulationsinstabil fuer S < 2/3).

### 2D-Tests (tests2d-r3)

#### Profilkontrolle m = 0 und m = 1 (Grundlage, Nebenprodukt Idee 19)

- **Vorhersage** (PLAN 1): Virialrest unter 1e-5; dE/dQ / omega = 1 auf etwa 1 Prozent; bei m = 1 S(0) = 0.
  Nebenprodukt Idee 19 [S]: Der innere Halbwertsradius des m = 1-Balls liegt bei etwa 1 (0,7 bis 1,5) und bleibt fuer
  omega^2 <= 0,6 nahezu gleich.
- **Ergebnis:**
  - m = 0, alle fuenf omega^2 gueltig: Virialrest betragsmaessig 8,1e-09 bis 4,2e-07. dE/dQ / omega 0,9941 / 0,9929 /
    0,9873 / 0,9940 bei 0,55 / 0,6 / 0,7 / 0,8.
  - m = 1: nur 0,52 gueltig, mit Virialrest -8,4e-03 und R_kern_halb 2,956. 0,55, 0,6, 0,7 und 0,8: "NEIN (Bahn ungenau,
    Zeile nicht verwenden)".
  - S(0) bei m = 1: nicht im Bericht.
- **Treffer:** teilweise.
  - m = 0 getroffen; 0,9873 bei 0,7 liegt knapp ausserhalb von 1 Prozent.
  - m = 1 verfehlt: Virialrest 8,4e-03 statt unter 1e-5, vier von fuenf Zeilen ungueltig.
  - Idee 19 ist damit nicht pruefbar. Die einzige Zeile (2,956) liegt ausserhalb 0,7 bis 1,5.
- **L3:** nicht im Bericht (Schiessen nur in einer Aufloesung).
- **Latten:** entfaellt (keine Karte).
- **Vorschlag:** Idee 19 parken, bis das m = 1-Schiessen repariert ist; m = 0 traegt Tropfen und Brechung.

#### Tropfen, Wellen 16

- **Vorhersage** (PLAN 2.2): 2D-Rayleigh Omega_l^2 = (l^3 - l) sigma/(rho R^3) mit rho = w = 2 omega^2 S_c.
  - Bindend ist P1 aus dem Profil: 0,01995 und 0,03991 bei 0,52 (Perioden 314,9 und 157,5), 0,07919 und 0,15838 bei 0,55.
  - Erwartung: Omega/P1 bei 0,52 etwa 0,93 bis 0,99, Omega_3/Omega_2 etwa 1,95; bei 0,55 Abweichung 5 bis 15 Prozent.
  - Kriterium A (0,52, fein): 0,90 <= Omega/P1 <= 1,05 fuer l = 2 und 3 und 1,85 <= Omega_3/Omega_2 <= 2,05.
- **Ergebnis** (fein):

  | omega^2 | l | Omega_mess | Omega/P1 | Omega/P6 | R2 |
  |---|---|---|---|---|---|
  | 0,52 | 2 | 0,01879 | 0,9416 | 0,9704 | 1,000 |
  | 0,52 | 3 | 0,03716 | 0,9312 | 0,9792 | 1,000 |
  | 0,55 | 2 | 0,06986 | 0,8822 | 0,9498 | 1,000 |
  | 0,55 | 3 | 0,13761 | 0,8688 | 0,9826 | 0,999 |

  - Omega_3/Omega_2: 1,978 (0,52) und 1,970 (0,55).
  - Linearitaet (dR 0,5 gegen 0,25): -0,00105 (0,52) und -0,00905 (0,55).
  - Ruhelauf: max |c2|, |c3| zwischen 1,3e-16 und 2,2e-16.
  - E-Verlust Box hoechstens 3,1e-04 (0,55, doppelte Auslenkung); Q-Verlust Box nicht im Bericht.
  - Urteil laut Bericht: "Tropfenbild quantitativ getragen (Kriterium A)".
- **Treffer:** getroffen. Omega/P1 bei 0,52 liegt in 0,93 bis 0,99, das Verhaeltnis bei 1,95, und bei 0,55 liegt die
  Abweichung (0,8822 und 0,8688) im Band 5 bis 15 Prozent.
- **L3:** bestanden; max Aenderung fein gegen grob 5,3e-05 (0,52) und 6,3e-05 (0,55).
- **Latten:** L1 ja; L2 bestanden; L3 bestanden; L4 teilweise; L5 nein.
- **Vorschlag:** parken ("bekannt"). Das Tropfenbild traegt quantitativ, ist aber weitgehend Rayleigh und Coleman und hat
  keinen Messbezug. sigma und rho = w stehen damit als gepruefte Groessen fuer Folgetests bereit.

#### Wellen 8/9, Magnus und Flettner

- **Stand** (PLAN 3): "im Ein-Feld-Modell nicht umsetzbar".
  - Kein stabiler duenner Hintergrund: modulationsinstabil fuer S < 2/3, stabil erst ab S > 2/3 und dort so dicht wie das
    Ballinnere.
  - Die Windung setzt sich nicht in den Hintergrund fort; also keine Zirkulation und keine Kutta-Joukowski-Kraft.
  - Kein Code, keine Laeufe, keine Scheinmessung.
- **Ergebnis:** keins.
- **Treffer:** entfaellt.
- **L3:** entfaellt.
- **Latten:** L1 entfaellt; L2 entfaellt; L3 entfaellt; L4 ja; L5 nein.
- **Vorschlag:** parken als "im Ein-Feld-Modell nicht umsetzbar". Mit einem zweiten Feld waere es eine neue Karte und die
  bekannte Magnuskraft auf einen Wirbel (L4).

#### Brechung, Wellen 14

- **Vorhersage** (PLAN 4.2): "v_y bleibt exakt gleich, sin theta2 = sin theta1 * v1/v2, n_eff = p2/p1 = v2/v1. Das ist
  korpuskulare Brechung."
  - Bindend ist die Code-Vorhersage aus dem Profil:
    - anziehend (V2 = -0,02): 15,64 / 30,44 / 43,05 / 0 Grad bei 20 / 40 / 60 / 0 Grad; v2 0,2537, n_eff 1,2686
    - abstossend (V2 = +0,02): 33,09 Grad bei 20 Grad (v2 0,1253, n_eff 0,6265) und Reflexion bei 45 Grad
    - ohne Stufe: 40 Grad
  - Kriterium: Fuer alle sechs Laeufe mit Stufe gilt gleichzeitig |d theta2| <= 1 Grad, |v2_mess/v2_vorh - 1|
    <= 2 Prozent, und der Ausgang stimmt.
  - Erwartung: Winkel innerhalb 1 Grad mit p = 0,65, Geschwindigkeiten innerhalb 2 Prozent mit p = 0,6, Totalreflexion bei
    45 Grad mit p = 0,9.
- **Ergebnis** (Tabelle je Winkel in Abschnitt 2):
  - Vier Laeufe mit Stufe erfuellen das Kriterium: anz40, anz60, abst20, abst45.
  - Zwei nicht: anz20 (Abweichung 2,73 Grad, v2 0,8513 der Vorhersage) und anz0 (v2 0,4240 der Vorhersage). Beide haben
    Q-Verlust Fenster 0,92 bzw. 0,94, alle anderen hoechstens 1,1e-04. **Diese Verluste sind fraglich, moeglicher
    Auswertefehler (Ball im Randbereich, siehe RUNDE-06/weber/PLAN.md).**
  - Die Totalreflexion bei 45 Grad trat ein (44,99 Grad).
  - Gegenproben: K_interpolation -3,7e-07; ohne Stufe Knick 1,65e-05 Grad und v2/v1 0,9999977; senkrechter Einfall
    (anz0) siehe oben.
  - Urteil laut Bericht: "Brechungsgesetz verfehlt: Winkel, Geschwindigkeit (Befund-Kandidat; zuerst Energieverlust ins
    Innere pruefen)".
- **Treffer:** teilweise. Nach der festen Regel des PLAN verfehlt; die zwei Abweichler sind fraglich (Abschnitt 2).
- **L3:** bestanden (max Aenderung theta2 0,0042 Grad bei kleinstem Knick 1,635 Grad), aber nur fuer anz20, anz40 und
  anz60 gerechnet.
- **Latten:** L1 ja; L2 teilweise; L3 bestanden; L4 ja; L5 nein.
- **Vorschlag:** weiter mit einem Umbau. Vier Laeufe folgen dem vorab ableitbaren Gesetz. Die zwei Abweichler fallen mit
  fast vollstaendigem Fensterverlust zusammen und sind vor jeder Deutung zu klaeren; fuer einen Weber-Zahl-Test fehlen
  ausserdem Groessen (Abschnitt 2).

#### Wellen 20 (Zufallskarte): Knoten-Q-Baelle, nur Papier

- **Stand** (KNOTEN-PAPIER.md): "Ein-Feld-Modell: keine geknoteten Q-Baelle (keine Knotenzahl). C x S^2: isorotierende
  Hopfionen sind Literatur. Ein gebundener Knoten-Q-Ball ist offen und braucht das Fenster
  1/2 < omega^2 < min(1, v^2/(2 kappa))."
- **Ergebnis:** Papier und Literatur, nichts gerechnet.
  - Ein-Feld: Die Abbildung S^3 -> C ist zusammenziehbar. Knoten der Nullinien koennen sich umverbinden (Hypothese [S];
    GP-Literatur Kleckner u. a. 2016 [T]).
  - C x S^2: Bei kappa = 1/4 (CX-1, Punkt P*) ist das Fenster 1/2 < omega^2 < 1 offen. Der gemischte Ast (Tor T4) ist
    weder definiert noch gerechnet.
- **Treffer:** entfaellt (Papierkarte, keine Zahlvorhersage).
- **L3:** entfaellt.
- **Latten:** L1 ja; L2 teilweise; L3 entfaellt; L4 ja; L5 nein.
- **Vorschlag:** Ein-Feld-Fassung verwerfen (keine Knotenzahl, bekannt); C x S^2 beim CX-1-Strang parken, wie in
  KNOTEN-PAPIER.md vorgeschlagen.

## 2. Brechung je Winkel (Grundlage fuer den Weber-Zahl-Test)

Quelle: brechung_bericht.txt. "Snellius" ist die Vorhersage des Berichts, also das korpuskulare Gesetz aus PLAN 4.2
(sin theta2 = sin theta1 * v1/v2, v_y erhalten), vor der Entwicklung aus dem Profil gerechnet. Feinlaeufe gibt es nur fuer
anz20, anz40 und anz60.

| Lauf (V2) | theta1 [Grad] | Normal-geschwindigkeit | Ausgang vorh. / gemessen | Ladung durchgelassen / reflektiert | Ladung verloren (Q-Verlust Fenster), grob / fein | theta2 gemessen, grob / fein [Grad] | theta2 Snellius [Grad] | v2 mess/vorh, grob / fein; vy2/vy1 | Zerfall oder Aufspaltung |
|---|---|---|---|---|---|---|---|---|---|
| anz0 (-0,02) | 0 (gemessen -0,00) | nicht im Bericht | durchgelaufen / durchgelaufen | nicht im Bericht | 9,4e-01 / kein Feinlauf; **fraglich, moeglicher Auswertefehler (Ball im Randbereich, siehe RUNDE-06/weber/PLAN.md)** | 0,00 (Abw. 0,00) | 0,00 | 0,4240; vy2/vy1 nan | nicht im Bericht |
| anz20 (-0,02) | 20,00 | nicht im Bericht | durchgelaufen / durchgelaufen | nicht im Bericht | 9,2e-01 / 9,2e-01; **fraglich, moeglicher Auswertefehler (Ball im Randbereich, siehe RUNDE-06/weber/PLAN.md)** | 18,37 / 18,37 (Abw. 2,73 / 2,72) | 15,64 | 0,8513 / 0,8514; 0,9950 | nicht im Bericht |
| anz40 (-0,02) | 40,00 | nicht im Bericht | durchgelaufen / durchgelaufen | nicht im Bericht | 1,1e-04 / 1,1e-04 | 30,45 / 30,45 (Abw. 0,00 / 0,01) | 30,44 | 0,9999 / 0,9998; 1,0000 | nicht im Bericht |
| anz60 (-0,02) | 60,00 | nicht im Bericht | durchgelaufen / durchgelaufen | nicht im Bericht | 5,1e-06 / 5,6e-06 | 43,05 / 43,05 (Abw. -0,00) | 43,05 | 1,0001 / 1,0000; 1,0000 | nicht im Bericht |
| abst20 (+0,02) | 20,00 | nicht im Bericht | durchgelaufen / durchgelaufen | nicht im Bericht | 3,4e-05 / kein Feinlauf | 33,10 (Abw. 0,03) | 33,09 | 0,9993; 1,0000 | nicht im Bericht |
| abst45 (+0,02) | 45,00 | nicht im Bericht | reflektiert / reflektiert | nicht im Bericht | 1,6e-05 / kein Feinlauf | 44,99 als Reflexionswinkel (Abw. -0,01) | 45,00 (Reflexion) | 1,0003; 1,0001 | nicht im Bericht |
| ohne40 (0) | 40,00 | nicht im Bericht | durchgelaufen / durchgelaufen | nicht im Bericht | 2,9e-05 / kein Feinlauf | 40,00 (Abw. 0,00) | 40,00 | 1,0000; 1,0000 | nicht im Bericht |

- **Normalgeschwindigkeit:** Der Bericht nennt weder v1 noch dessen Normalkomponente. Laut PLAN 4.1 startet der Ball mit
  v1 = 0,2 unter theta1 zur Stufennormalen; alle Laeufe haben dieselbe Einfallsgeschwindigkeit.
- **Ladung:** Der Bericht nennt nur den Ausgang des ganzen Balls und den Q-Verlust im Fenster am letzten gueltigen
  Messpunkt (PLAN 4.3). Eine Aufteilung in durchgelassene und reflektierte Ladung gibt es nicht.
- **Zerfall oder Aufspaltung:** Dazu sagt der Bericht nichts, er gibt auch keine Klumpenzahl. Das Urteil verweist nur auf
  "zuerst Energieverlust ins Innere pruefen".
- **Ergebnis-JSON:** brechung_ergebnis.json fuehrt je Lauf zusaetzlich v1_mess, v2_mess, vy1, vy2, E_fenster_verlust und
  t_letzter_gueltiger. Felder fuer Normalgeschwindigkeit, Klumpenzahl, Aufspaltung oder getrennte Ladungsanteile gibt es
  auch dort nicht. Zahlen daraus sind hier nicht uebernommen.
- **Fuer einen Weber-Zahl-Test fehlen damit:** die Normalgeschwindigkeit als Messgroesse, die Aufteilung der Ladung und
  jede Diagnose von Zerfall oder Aufspaltung.
- **Pruefung des Hinweises "Ball im Randbereich" am Bericht** (Weber-Agent, RUNDE-06/weber/PLAN.md, Hypothese, nicht
  nachgerechnet):
  - Der Bericht enthaelt keine Zeitpunkte und keine Positionen: weder Ballort noch Boxrand noch Randschicht, auch nicht den
    letzten gueltigen Messpunkt. Aus den Berichtszahlen laesst sich der Hinweis weder bestaetigen noch widerlegen.
  - Was der Bericht hergibt und dem Hinweis nicht widerspricht:
    - Betroffen sind nur die zwei anziehenden Laeufe mit dem steilsten Einfall (0 und 20 Grad); bei 40 und 60 Grad
      bleibt der Verlust bei 1,1e-04 und 5,1e-06.
    - Der Verlust bei 20 Grad ist grob und fein gleich (9,2e-01), haengt also nicht an der Aufloesung.
    - Nur in diesen zwei Laeufen weichen auch v2 (0,8513 und 0,4240 der Vorhersage) und bei 20 Grad vy2/vy1 (0,9950) ab.
  - Eine Weg-Zeit-Rechnung mit den PLAN-Groessen (Start x0 = -16, Box halbe Laenge 42, T = 280, Randschicht Breite 8)
    habe ich nicht gemacht. Sie steht mit eigenen Zahlen im Weber-Plan.

## 3. Auffaelligkeiten

### Klare Widersprueche zur Vorhersage

1. **t5, Q gegen Anti-Q:**
   - Bei d = 8 und 12 bleibt nichts Lokalisiertes (Rest Q_abs 0,01094 bis 0,02171, t50 zwischen 67 und 195,5).
     Vorhergesagt waren Restbaelle ueber 0,95 bzw. 0,99.
   - Die Vernichtung ist bei d = 8 (t50 67 und 68) schneller als bei d = 3 (274,5 und 453,5) und d = 12 (194 und 195,5).
   - Eine Kontrolle "einzelner Anti-Ball allein" enthaelt der Aufbau nicht (PLAN 9).
2. **t1, d = 10:** Das Urteil lautet "Nettofluss klein -> gross (H)" (Phasenmittel -0,05586 bei Amplitude 0,0479).
   Vorhergesagt war "in keinem Fall 'klein -> gross'". L2 und L3 sind bestanden (597,1 und 1937).
3. **t3, +-pi/2 langsam:** abgeprallt bei v = 0,05 bis 0,3 statt verschmolzen; der kleinste Abstand bleibt 10,494 bis
   5,255.
4. **t4, D90 bei n = 0:** Steigung -3,8035e-03 statt etwa +0,02.
5. **t2 (Version 2):**
   - Morse a = 0,926 knapp ausserhalb 0,4 bis 0,9.
   - omega_vib 0,79 bis 0,82 statt 0,4 bis 0,75.
   - Asymptotik C 2,236 statt 4,1569 (kappa passt).
6. **Brechung, anz20 und anz0:**
   - anz20: Winkel 18,37 statt 15,64 Grad, vy2/vy1 0,9950 statt "exakt gleich".
   - v2 0,8513 bzw. 0,4240 der Vorhersage.
   - Fraglich wegen des Fensterverlusts (Abschnitt 2).
7. **2D-Profil, Idee 19:** innerer Halbwertsradius 2,956 bei 0,52 statt etwa 1 (0,7 bis 1,5), allerdings bei gerissener
   Virialkontrolle.

### Kontrollen, die reissen

1. **t5, Ball-Ball-Kontrolle:** Erwartet war ein Verlust unter 2 Prozent; sechs von acht Laeufen verfehlen das.
   - Gegenphasig d = 3 / 5 / 8: Rest Q_abs 0,002677 / 0,009074 / 0,04856.
   - Gleichphasig d = 5 / 8 / 12: 0,9431 / 0,7436 / 0,707.
   - Damit ist L2 fuer t5 nicht erfuellt.
2. **Brechung, senkrechter Einfall (Gegenprobe anz0):** v2 mess/vorh 0,4240 bei Q-Verlust Fenster 0,94 (fraglich, s. o.).
3. **2D-Profil m = 1:**
   - Virialrest -8,4e-03 in der einzigen gueltigen Zeile (Erwartung unter 1e-5); vier von fuenf Zeilen
     "NEIN (Bahn ungenau)".
   - m = 0: dE/dQ / omega 0,9873 bei 0,7, knapp ausserhalb "auf etwa 1 Prozent".
4. **t2, pi-Seite:** Die antisymmetrischen Laeufe halten den Abstand nicht (d_ist 13,52 bis 16,10 fuer d_start 1,5 bis 13).
   Die Gegenprobe pi deckt deshalb nur 13,5 bis 16,1 ab; das Verhaeltnis pi/0 ist nicht bestimmbar.

### L3

- In keinem gerechneten Test gerissen (t1, t2 Version 2, t3, t4, t5, Tropfen, Brechung).
- Einschraenkungen:
  - Brechung: fein nur anz20, anz40 und anz60 (PLAN 4.1); anz0 und die abstossenden Laeufe haben keinen L3-Vergleich.
  - Tropfen: Omega_2 bei 0,52 ist grob und fein ziffergleich (0,018787531856019536). Die Aenderung fuer l = 2 bei 0,52 ist
    damit null; wie fein die Frequenzverfeinerung aufloest, steht nicht im Bericht. Am Bestehen aendert das nichts, die
    gemeldete Aenderung 5,3e-05 liegt weit unter der Schwelle max(0,2 * 0,0688; 0,005) aus PLAN 2.3.
  - t1: L3 nur fuer Phasenmittel und das Mittel bei phi0 = 0 (laut Code), nicht fuer Amplitude und Periode.
  - t2: L3 nur fuer Delta phi = 0.
  - t4: Vorhergesagt war, dass L3 beim Spendereffekt n = 3 reisst; es bestand (41,39).

### Unplausible oder unvollstaendige Bilanzen

1. **Brechung:** Der Q-Verlust im Fenster betraegt 0,92 (anz20) und 0,94 (anz0), bei allen anderen Laeufen 5,1e-06 bis
   1,1e-04. Der Ausgang heisst trotzdem "durchgelaufen".
   - Fraglich, moeglicher Auswertefehler (Ball im Randbereich, siehe RUNDE-06/weber/PLAN.md).
   - Laut Weber-Agent (Hypothese, nicht nachgerechnet) war der Ball bei t = 280 schon in der Randschicht verschwunden, und
     das Fenster wanderte auf einen strahlungsartigen Rest zurueck.
   - Der Bericht kann das nicht pruefen, er nennt weder Positionen noch Zeiten (Abschnitt 2).
2. **t5:** Die Gesamtladung im Messbereich am Ende ("Q ges. Ende") faellt bei den gegenphasigen Kontrollen auf 0,004049
   (d = 3), 0,02657 (d = 5) und 0,2081 (d = 8), gegen 4,781 bei d = 12.
   - Die Feldgleichung erhaelt die Ladung; sie hat also den Messbereich |x| < 75 verlassen (Daempfungsschicht ab
     |x| = 80, PLAN 3).
   - Ob als Strahlung oder mit Baellen, die hinauslaufen, steht nicht im Bericht.
   - Bei d = 8 geht der Verlust spaet und rasch (t10 510,5, t50 527).
   - Die Randfrage der Brechung stellt sich hier ebenso; Pruefschritt: Schwerpunktbahnen gegen |x| = 75.
3. **t4, Spaetphase:**
   - dQ_A max reicht bis 3,2741, "dQ_A Mittel spaet" bis -2,9449 (n = 3 ohne Spender). Das ist die Groesse der ganzen
     Empfaengerladung (Q = 3,1628 bei omega^2 = 0,6, PLAN 3).
   - Der Spendereffekt bei t = 100 faellt nicht wie die Anfangssteigung: n = 1 (0,7183) liegt ueber n = 0 (0,1244), n = 2
     und 3 sind fast gleich (-0,05458 und -0,05514).
   - Die feste Messgroesse (Steigung auf [2, 15]) ist davon nicht beruehrt; die Spaetphase ist nicht ausgewertet.
4. **t1, d = 8:** Das mittlere dQ_klein bei phi0 = 3pi/2 (1,937) liegt nahe an der Anfangsladung links (Q_klein(0) =
   2,07821).
   - Nach t = T/8 aendert sich die Ladung kaum noch: Amplitude 0,0224, laut Code auf [T/8, T] gemessen.
   - Das Urteil "gegen H" stammt aus der festen Regel, die das Phasenmittel mit dieser kleinen Amplitude vergleicht.

### Numerisch fragwuerdig

1. **t1, Perioden:** Die Periode ist laut Code der staerkste FFT-Kanal des Fensters [T/8, T] im Lauf phi0 = 0.
   - 351 bei d = 8 ist der unterste Kanal, also die Fensterlaenge selbst; ein Pendeln ist dort nicht aufgeloest.
   - 50,14 (d = 12) und 43,88 (d = 10) sind benachbarte Kanaele; der Vergleich mit 52,43 ist grob gerastert.
2. **t2, Morse:** d0 = 1,549 liegt ausserhalb der belegten Abstaende (kleinster d_ist 2,1463) und nicht beim gemessenen
   Minimum 2,637. Dazu kommt E_unendlich -0,0244 statt 0. Der Fit beschreibt die Punkte (rms/D 0,0345), seine Parameter
   sind aber nur bedingt deutbar.
3. **t2, pi-Asymptotik:** C = 5177, kappa = 0,8712 (Vorhersage 4,1569 und 0,5477).
   - Die pi-Werte stammen aus d_ist 13,5 bis 16,1; E_int faellt dort von 3,963e-02 auf 6,789e-04.
   - Die Konvergenz dE der pi-Laeufe reicht bis 1,4e-04; das PLAN-Kriterium galt nur fuer d <= 10.
   - Grob gibt es bei d_soll = 12 einen pi-Wert (0,0557648), fein keinen.
4. **t3, Klasse "gebunden/unklar":** Die langsamen gleichphasigen Paare kommen bis 2,453 bis 2,506 zusammen, erfuellen am
   Ende aber die Regel "verschmolzen" nicht.
   - Hinweis aus dem Rauchtest (T = 80, gilt nicht als Ergebnis): Dort hiessen v = 0,05 und 0,1 noch "verschmolzen".
   - Die Klasse wechselte also zwischen T = 80 und T = 800.
5. **Tropfen:** Omega_2 bei 0,52 ist grob und fein ziffergleich (siehe L3).
6. **t6:** Die v_c-Rasterwerte bei S < 2/3 liegen zwischen 8,66e-05 und 8,119e-03 und steigen nicht monoton mit S. Laut
   Spaltenkopf sind es Rasterwerte, erwartet war 0.

### Geschwindigkeiten ueber c = 1

- Keine. Die groessten gemeldeten Geschwindigkeiten sind v_aus 0,5993 (t3), c_s 0,7071 (t6) und die v2-Vorhersage 0,2537
  (Brechung).

### Bezug zu Runde 2

- Die Resonanz rho = 1,4938 (1D, Runde 2) laesst sich mit keiner Zahl dieser Runde vergleichen; kein Bericht gibt eine
  innere Frequenz des Einzelballs aus.

## 4. Zusammenfassung

| Test | Karte | Ergebnis in einem Satz | Treffer | L3 | L1 | L2 | L4 | L5 | Vorschlag |
|---|---|---|---|---|---|---|---|---|---|
| 1D profil | Grundlage | K0 max 9,84e-11 | getroffen | entfaellt | - | - | - | - | Grundlage haelt |
| t1 | Chemie 1 | Pendeln bei d = 12; "klein -> gross" bei d = 10; bei d = 8 "gegen H" ohne aufgeloestes Pendeln | teilweise | bestanden | ja | bestanden | teilweise | mittelbar | weiter |
| t2 (V2) | Chemie 2/3 | einziges Minimum bei d 2,637, Tiefe 0,448 mit den Werten des verschmolzenen Balls; kein Minimum bei getrennten Baellen; Form offen | teilweise | bestanden (nur 0) | ja | teilweise | weitgehend | nein | parken ("bekannt") nach Klaerung der Formfrage |
| t3 | Chemie 7 | pi nie verschmolzen; 0 langsam "gebunden/unklar"; +-pi/2 langsam abgeprallt | teilweise | bestanden | ja | bestanden | teilweise | nein | weiter |
| t4 | Chemie 15 | Rohsteigung nicht exponentiell (0,42 / 1,25 / 1,01); Spendereffekt 0,15 / 0,024 / 0,021 je Bruecke | teilweise | bestanden | ja | bestanden | teilweise | mittelbar | parken ("bekannt") |
| t5 | Chemie 14 (Zufall) | Q und Anti-Q enden bei d = 8 und 12 als Strahlung (t50 67 bis 195,5); Ball-Ball-Kontrolle reisst | verfehlt | bestanden | ja | gerissen | teilweise | nein | weiter mit Umbau |
| t6 | Wellen 5 | Papier: v_c = 0 fuer S < 2/3, c_s 0,31 bis 0,71 fuer S >= 2/3 | getroffen (Papier) | entfaellt | nein | entfaellt | ja | mittelbar | parken |
| 2D profile | Grundlage, Idee 19 | m = 0 sauber; m = 1 vier von fuenf ungueltig, Virialrest 8,4e-03 | teilweise | nicht im Bericht | - | - | - | - | Idee 19 parken |
| tropfen | Wellen 16 | Kriterium A: Omega/P1 0,9416 und 0,9312, Omega_3/Omega_2 1,978 | getroffen | bestanden | ja | bestanden | teilweise | nein | parken ("bekannt") |
| - | Wellen 8/9 | im Ein-Feld-Modell nicht umsetzbar | entfaellt | entfaellt | entfaellt | entfaellt | ja | nein | parken |
| brechung | Wellen 14 | 4 von 6 Laeufen wie vorhergesagt; anz20 und anz0 daneben bei fraglichem Fensterverlust 0,92 / 0,94 | teilweise (Regel: verfehlt) | bestanden (3 Laeufe) | ja | teilweise | ja | nein | weiter mit Umbau |
| Papier | Wellen 20 (Zufall) | Ein-Feld ohne Knotenzahl; C x S^2 offen im Frequenzfenster | entfaellt | entfaellt | ja | teilweise | ja | nein | Ein-Feld verwerfen, C x S^2 bei CX-1 parken |

## Einfach gesagt

Ein grosser Q-Ball wackelt wie ein Wassertropfen, und Lord Rayleighs alte Tropfenformel sagt sein Tempo auf wenige
Prozent genau voraus; das ist der klarste Treffer der Runde. Zwei gleiche Baelle bilden kein Molekuel mit festem Abstand:
Die Energie hat nur ein Tal, und dessen Zahlen passen zu den vorab berechneten Werten des verschmolzenen Einzelballs; ob
es wirklich ein einziger Ball ist, muss man sich noch als Bild ansehen. Rollt ein Q-Ball schraeg ueber eine Stufe, knickt er in vier von sechs
Faellen genau wie berechnet ab; in den zwei anderen verschwindet er vermutlich nur aus dem Messfenster am Rand, das wird
gerade nachgeprueft. Ein Q-Ball und sein Anti-Ball zerstrahlen anders als erwartet auch mit Abstand, aber die
Vergleichsrechnung mit zwei normalen Baellen verliert ebenfalls Ladung, deshalb ist das noch kein Befund. Zwischen einem
kleinen und einem grossen Ball schwappt Ladung bei grossem Abstand hin und her wie vorhergesagt, bei mittlerem Abstand
fliesst sie im Mittel vom kleinen zum grossen.
