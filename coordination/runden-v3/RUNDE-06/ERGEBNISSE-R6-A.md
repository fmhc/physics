# Runde 6, Paket A: Reflexion (R-1 bis R-5), Weber-Zerspritzen, Finns F-5 (explorativ, v3)

Auswertung: Anthropic-Agent (Opus) im Auftrag von claude-primary. Nur gelesen, nur diese Datei geschrieben.
Beginn 2026-09-30 03:22:39 CEST, Ende 2026-09-30 03:43:17 CEST (beide gemessen mit date).

## Grundlage und Lesehilfe

- **Quellen:**
  - Reflexion: KARTEN-REFLEXION-STABILISIERT.md, reflexion/PLAN.md, Berichte
    reflexion/lauf-69/ausgabe-{r1, r2, r2zeit, r3, r4, r5}/reflexion_*_bericht.txt, Logs lauf-69/LAUF1.log bis LAUF3.log.
    An zwei Stellen zusaetzlich die Ergebnis-JSON desselben Aufrufs; das ist jeweils markiert.
  - Weber: AUFTRAG-WEBER.md, weber/PLAN.md.
    - grob (Laptop-CPU): weber/lauf-lokal/{karte1d, feinv1d}/*_grob_bericht.txt
    - fein (.69, P4000): weber/lauf-69/{karte1d, feinv1d}/*_fein_bericht.txt
    - 2D (.69, P4000): weber/lauf-69/winkel2d/winkel2d_bericht.txt; Logs lauf-69/LAUF1.log bis LAUF3.log
  - F-5: FINN-IDEE-F5-SCHWER-LEICHT.md, RUNDE-05/r5d/PLAN-F5.md, Berichte
    RUNDE-05/r5d/lauf-69/{f51, f52, f53, f54-m03, f54-m06}/r5d_f5_*_bericht.txt, Logs LAUF-F5A.log und LAUF-F5B.log.
- **Vollstaendigkeit:**
  - reflexion/lauf-69/ausgabe-r4 ist vollstaendig: Bericht mit Endzeile (01:21:28 UTC = 03:21:28 CEST), JSON
    geschlossen, LAUF1.log mit "ende ... rc=0" und KETTE-RF1-ENDE. Alle sechs Reflexionsaufrufe: rc = 0, "Fehler in:
    keine".
  - weber/lauf-69/winkel2d ist vorhanden und vollstaendig (Ende 01:20:19 UTC = 03:20:19 CEST; LAUF3.log rc = 0).
  - Weber: Das PLAN-Werkzeug `l3` ist auf der .69 nicht gelaufen (kein l3-Ordner). L3 fuer 1D steht hier von Hand
    (W-1, W-2).
  - Syntaxfehler kleintest.sh Zeile 31 statt "ende ... rc=": Weber LAUF1.log (nach dem Rauchtest), LAUF-F5A.log (nach
    f53), LAUF-F5B.log (nach f54-m06). Dort steht jeweils "code=exited/status=0", im Bericht "Fehler in: keine". Die
    drei Reflexions-Logs haben alle rc-Zeilen.
  - Nicht gewertet: reflexion/lauf-lokal/ (Rauch und T = 600-Proben), reflexion/lauf-69/rauch-cuda, weber/lauf-69/rauch,
    weber/lauf-lokal/rauch-*. Rauchtests erscheinen nur als "Hinweis".
- **Zahlen:**
  - "grob / fein", wo beide stehen.
  - Eigene Ueberschlaege sind mit "(von Hand)" markiert.
  - "nicht im Bericht" heisst: Die Groesse steht nicht im Bericht.
  - Reflexion: Abklingraten Gamma in Einheiten Gamma0 = 6,716e-5 (Einzelball = 1).
- **Urteil** gegen die Vorhersage im jeweiligen PLAN: getroffen, teilweise oder verfehlt. Die Abschaetzung entscheidet
  die Leitung.
- **Latten, je ein Wort:**
  - L1 kann scheitern: ja / teilweise
  - L2 Gegenprobe: haelt / teilweise / gerissen
  - L3 Aufloesungsvergleich: bestanden / teilweise / fraglich
  - L4 schon bekannt: bekannt / teilweise / nein (Einstufung aus dem PLAN; Literatur dort aus dem Gedaechtnis)
  - L5 Messbezug: nein / Methode / teilweise
- **Regelabweichung (offen gelegt):** Beim Lesen der R-5-JSON habe ich einmal awk als reinen Zeilenfilter benutzt
  (`NR<=45`, entspricht head). Es wurde damit nichts gerechnet. Sonst nur grep, cut, diff, cmp, tail und date.

## 1. Je Test

### Reflexion (1D, Messlaeufe auf der .69)

Gemeinsam: Der Anker (Einzelpol gegen Codex) ist in allen fuenf linearen Aufrufen und beiden Stufen bestanden, mit
|rho - Codex| = 1,3e-12 / 6,9e-13 und |dIm|/Gamma0 = 1,2e-8 / 7,0e-9.

**R-1 Bandlueckenschutz (`r1`, cpu3, 115 s)**
- Vorhersage (PLAN Abschnitt 5):
  - V1a: "Fuer jedes M haben N - 1 von N Polen Gamma < 0,01, ein Pol hat Gamma = N +- 20 %."
  - V1b: "Ueberleben der Mittelanregung (Polsumme) bei 5/Gamma0 >= 0,1 fuer alle M"
  - V1c (Anti-Bragg): "Ueberleben bei 20/Gamma0 mindestens 10-mal kleiner als in der Bragg-Kette, fuer M >= 2"
  - V1d (nichtresonant, 0,6): "Gamma_c in [0,9; 1,1] fuer alle M <= 20"
  - V1e: "Summenregel 1 +- 0,05, sonst ist die Polsumme nicht verlaesslich ... Dann zaehlt das Markov-Ueberleben mit
    Pruefzahl 'Markov-exakt'."
- Ergebnis (grob und fein gleich auf allen gedruckten Stellen, ausser bei Zahlen unter 1e-10):
  - **luecke_bragg**, M = 1 / 2 / 5 / 10 / 20 (N = 3 / 5 / 11 / 21 / 41):
    - gefundene Pole: 2/3, 2/5, 2/11, 5/21, 22/41
    - heller Pol Gamma_c: 3,021 / 5,108 / 12,42; bei M = 10 und 20 kein heller Pol gefunden (Gamma_c 6,9e-6 und 1,6e-5,
      Mittelgewicht w_c 0,000)
    - dunkle Pole (< 0,01): 1 / 1 / 1 / 5 / 22
    - Summenregel: 0,562 / 0,521 / 0,581 / 0,000 / 0,000
    - Polsumme bei 5/Gamma0: 2,4e-14 / 3,0e-23 / 1,8e-29 / 2,1e-29 / 8,2e-28
    - Markov Mitte bei 5/Gamma0: 0,444 / 0,640 / 0,826 / 0,907 / 0,952; Pruefzahl Markov-exakt 0,021 / 0,11 / 1,4 / 21 /
      41 Gamma0
    - Gamma_min negativ: -2,7e-13 / -3,0e-13 / -1,3e-7 / -6,9e-6 / -3,3e-5
  - **verstimmt_lambda8:** Gamma_min 6,0e-2 bis 1,4e-5; Polsumme bei 20/Gamma0 0,049 / 0,130 / 0,067 / 0,075 / 0,048;
    Summenregel 0,925 bis 0,996.
  - **ohne_luecke_antibragg:** Gamma_min 0,495 bis 1,4e-4; Polsumme bei 20/Gamma0 1,1e-9 / 3,9e-3 / 2,9e-2 / 2,8e-2 /
    2,5e-3; Summenregel 0,858 (M = 20) bis 1,026.
  - **nichtresonant_bragg** (Kettenball 0,6, |r(nu0)| = 8,1e-3): Gamma_c 1,002 / 1,006 / 1,036 / 1,124 / 1,145; Pole
    1/1, 1/1, 2/1, 2/1, 6/1; Summenregel 1,007 / 1,015 / 0,882 / 0,910 / 0,800.
  - **allein:** Ueberleben 1,35e-1 / 4,54e-5 / 4,25e-18 bei 1 / 5 / 20 x 1/Gamma0.
- Treffer:
  - V1a teilweise: Der helle Pol liegt bei M = 1, 2, 5 in N +- 20 %. Die N - 1 dunklen Pole sind nicht gefunden.
  - V1b nicht entscheidbar: Die Polsumme liegt weit unter 0,1, ist aber nach V1e unverlaesslich. Der Markov-Ersatz liegt
    fuer alle M ueber 0,1; eine kleine Pruefzahl hat er nur bei M = 1 und 2.
  - V1c nicht entscheidbar, weil die Bragg-Polsumme unverlaesslich ist. Markov (Mitte, 20/Gamma0) bei M = 2: Bragg 0,640
    gegen Anti-Bragg 2,3e-3.
  - V1d verfehlt bei M = 10 und 20 (1,124 und 1,145).
  - V1e verfehlt fuer die ganze Bragg-Kette und fuer vier weitere Zeilen (0,800 bis 0,925).
  - Hinweis (Rauchtest .69, h = 0,02, keine Wertung): Dort fand die Suche bei luecke_bragg M = 1 und 2 noch 3/3 und 5/5
    Pole, Summenregel 1,002 / 1,008, Polsumme bei 5/Gamma0 0,343 / 0,494.
- Urteil: teilweise. Die Kernfrage (Schutz durch die Bragg-Luecke) ist in diesem Lauf nicht messbar, weil die Polsuche
  in der Bragg-Kette Pole verliert.
- L3 laut Bericht: Gamma_c 20 von 21, Gamma_min 20 von 21. Die fehlende Zeile ist die Einzelball-Nullzeile (JSON:
  Effekt 1,2e-8). L3 prueft nur h und R, nicht die Vollstaendigkeit der Pole; beide Stufen verlieren dieselben Pole.
- Latten: L1 ja, L2 teilweise, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken. Erst muss die Polsuche fuer entartete dunkle Pole repariert sein (PLAN Abschnitt 8 nennt genau
  diese Grenze), sonst ist der Bragg-Arm nicht auswertbar.

**R-2 Dunkler Zustand zweier Baelle, linear (`r2`, cpu3, 41 s)**
- Vorhersage:
  - V2a: "Je Periode lambda = 2,985 gibt es einen Abstand mit dunklem Anti-Modus und einen mit dunklem Sym-Modus,
    lambda/2 auseinander."
  - V2b: "Gamma am dunklen Abstand <= 1e-3, in grob und fein"
  - V2c: "Der helle Partner hat 2,00 +- 0,05."
  - V2d: dunkler Anti-Abstand bei 35,819 (Markov ohne Phase; laut PLAN schon im Rauchtest gescheitert). Die Formel
    1 +- cos(k d + 2 delta_e) wird ueber d = 20 bis 60 geprueft, Schwelle 0,05.
  - V2e: "Partner 0,69: Mittelball Gamma = 1 +- 0,02 bei allen d, kein dunkler Zustand."
- Ergebnis:
  - dA = 35,35007 (anti), dS = 36,84253 (sym); Abstand 1,49246 = lambda/2 (von Hand: 2,98492 / 2).
  - Gamma dunkel: 8,1e-15 und 7,9e-15 (grob), 3,2e-14 und 3,2e-14 (fein).
  - Heller Partner an denselben Abstaenden: 2,0052 (dA, sym) und 2,0054 (dS, anti), aus dem r2zeit-Bericht (Zeilen
    "linear (Kontinuum)"). Naechste Abtastpunkte im r2-Bericht: 2,00056 und 2,00079.
  - Hintergrundphase 2 delta_e = 0,98725, Verschiebung -0,4690; Markov mit Phase 35,34998.
  - Formel mit Phase gegen exakt: groesste Abweichung 0,0058 bei d = 56, sym (1,87640 gegen 1,87056; von Hand
    abgelesen).
  - Partner 0,69: Gamma/Gamma_einzel 0,9960 bis 1,0046 an allen 11 Abstaenden.
- Treffer: V2a, V2b, V2c und V2e getroffen. V2d in der Ursprungsform verfehlt (vorab bekannt), in der Form mit Phase
  getroffen; der PLAN (Abschnitt 6) nennt V2d eine schwache L1-Stelle.
- Urteil: getroffen.
- L3 laut Bericht: Gamma_anti_min und Gamma_sym_min bestanden; d_anti grob = fein = 35,350074.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: weiter. Linear und in der vollen Zeitrechnung (R-2z) gilt dieselbe Aussage; offen ist der Fall freier
  Baelle (PLAN Abschnitt 8: Auslaeuferkraft 6e-9 bei d = 36, Abstand muss auf ~0,05 halten).

**R-2z Dunkler Zustand in der Zeitentwicklung (`r2zeit`, P4000, T = 1500, 120 s)**
- Vorhersage:
  - V2z-a: "Einzelball Gamma_fit = 1,00 +- 0,10, grob und fein." (Abbruchkriterium fuer R-2z und R-4)
  - V2z-b: "Dunkle Anregung (dA/anti, dS/sym): Gamma_fit <= 0,15. Hell (dA/sym, dS/anti): 2,0 +- 0,3. Bei dM beide
    1,0 +- 0,3."
  - V2z-c: "Gamma_fit der dunklen Anregung aendert sich grob -> fein um <= 0,1."
- Ergebnis (grob / fein, linear in Klammern):
  - einzel 1,0124 / 1,0031 (1,0000)
  - dunkel: dS/sym 0,0031 / -0,0004; dA/anti 0,0032 / 0,0001 (beide -0,0000)
  - hell: dS/anti 2,0268 / 2,0117 (2,0054); dA/sym 2,0281 / 2,0125 (2,0052)
  - dM: sym 0,9244 / 0,9823 (0,9971); anti 1,0930 / 1,0186 (0,9975)
  - Atemfrequenz 1,49363 / 1,49374 (Kontinuum 1,49378); rms ln 1,2e-5 bis 6,3e-5; Fremdmodus hoechstens 1,7e-3.
- Treffer: V2z-a, V2z-b und V2z-c getroffen (Aenderung dunkel 0,0035 und 0,0031, von Hand).
- Urteil: getroffen.
- L3 laut Bericht: "True" bei dS/sym, dS/anti, dA/sym, dA/anti; "False" bei einzel, dM/sym, dM/anti.
  - Das Code-Kriterium lautet "Effekt |Gamma - 1| >= 5 x Aenderung grob -> fein" (reflexion.py, l3). Bei Zeilen mit
    erwartetem Gamma = 1 ist es nicht anwendbar.
  - Nach V2z-c bestanden.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: weiter, zusammen mit R-2 (zwei Methoden, gleiche Aussage).

**R-3 Bindung durch Strahlung (`r3`, cpu4, 56 s)**
- Vorhersage:
  - V3a: "F_rel(d) hat seinen Hauptanteil bei 2k (Periode lambda/2): Amp_2k > Amp_k fuer alle nu und Pumpen."
  - V3b: "Stabile Gleichgewichte (wo es sie gibt) liegen lambda/2 +- 5 % auseinander."
  - V3c: "Bei linear gueltiger Pumpe eps_lin gilt |F_rel| <= 1e-7 fuer alle nu. Der Abstand d_x ... liegt zwischen 30
    und 45."
  - V3d (nicht resonant, Pumpe von links): "max|F_rel| <= 1e-3 je eps^2"
  - V3e: "Eigenfeld des dunklen Modus stoesst ab (F_rel > 0)"
- Ergebnis (grob = fein auf allen gedruckten Stellen, ausser Amp_k unter 1e-11):
  - Pumpe links: Amp_2k > Amp_k in 7 von 7 (Beispiel -1 Gamma: 0,349 gegen 17,6).
  - Pumpe beide: Amp_k > Amp_2k in 7 von 7 (Beispiele -1 Gamma: 50,2 gegen 35,4; 2,25: 6,0e-2 gegen 5,6e-5).
  - Bei Resonanz (0): Amp_k und Amp_2k 1,2e-6 bis 9,2e-6, dagegen max|F_rel| 17,7 (links) und 35,5 (beide); kein
    Gleichgewicht.
  - Gleichgewichtsabstaende bei Pumpe links: 1,500 (lambda/2 1,4926), 1,450 und 1,500, 1,500, 1,500, 1,550 (1,5587),
    1,700 (1,7013). Bei Pumpe beide je 1 Gleichgewicht im Fenster d = 30 bis 33, also kein Abstand.
  - F bei eps_lin: 1,0e-10 bis 5,77e-7; ueber 1e-7 in 6 von 14 Faellen (alle "beide" ausser bei Resonanz). d_x 29,0 bis
    44,8 (29,0 bei 2,25 beide).
  - Nicht resonant, links: 2,80e-5 (2,25) und 2,74e-6 (2,10).
  - Eigenfeld: dunkel (dA anti) F_rel/|E|^2 = +22,85; hell (dA sym) -10,61.
  - Ohne Pumpe (Auslaeufer): 3,33e-7 (d = 30) bis 9,0e-11 (d = 45).
- Treffer: V3a fuer beidseitige Pumpe verfehlt, fuer einseitige getroffen; V3b getroffen, wo Abstaende messbar sind;
  V3c teilweise; V3d und V3e getroffen.
- Urteil: teilweise.
- L3 laut Bericht: 14 von 14.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken. Die Kraft bei linear gueltiger Pumpe (hoechstens 5,8e-7) liegt in der Groesse der Auslaeuferkraft
  und braucht eine Pumpe von aussen (PLAN Abschnitt 8).

**R-4 Randreflexion (`r4`, P4000, T = 1500, 286 s)**
- Vorhersage:
  - V4a (schwamm): "Gamma_fit = 1,00 +- 0,10."
  - V4b (gross): "|Gamma_gross - Gamma_schwamm| <= 0,05."
  - V4c (spiegel, ring): "|Gamma_fit| <= 0,3 ueber 200 bis 1500." Vor der Rueckkehr (200 bis 332): "Gamma ~ 1 +- 0,5".
  - V4d (linear): "Ball zwischen Spiegeln, alle Pole nahe nu0 mit |Im nu| <= 1e-10."
- Ergebnis (grob / fein):
  - schwamm 1,0124 / 1,0031; gross 1,0124 / 1,0031 (gleich auf 4 Stellen); |A| 2,866e-5 -> 2,632e-5.
  - spiegel -0,1130 / 0,0090; vor der Rueckkehr 1,0500 / 1,2190, danach -0,1449 / -0,1659.
  - ring -0,3918 / -0,1539; vor der Rueckkehr 0,9807 / 0,7908, danach -0,8858 / -0,2886.
  - rms ln: schwamm 1,2e-5; spiegel 4,0e-3 / 9,3e-3; ring 1,9e-2 / 1,2e-2.
  - Linear: 1 Pol nahe nu0, max |Im nu| = 4,28e-18.
  - Hinweis im Bericht: "linearisierte Saat entfallen (K' singulaer)".
- Treffer: V4a, V4b und V4d getroffen. V4c teilweise: Ring grob |-0,3918| > 0,3, fein getroffen; vor der Rueckkehr
  liegen alle vier Werte im Band.
- Urteil: teilweise.
- L3 laut Bericht: spiegel und ring "True", schwamm und gross "False". Die "False" sind Nullzeilen (Effekt
  |1,0124 - 1| = 0,0124 unter 5 x 0,0093, von Hand). Das V4c-Urteil fuer den Ring kippt zwischen grob und fein.
- Latten: L1 teilweise, L2 haelt, L3 teilweise, L4 bekannt, L5 Methode.
- Vorschlag: weiter, als Methodenkontrolle. Schwamm und grosse Box stimmen auf 4 Stellen ueberein, Spiegel und Ring
  zeigen eine scheinbar fast verlustfreie Resonanz.

**R-5 Lokalisierung im Q-Ball-Gas (`r5`, cpu4, 123 s)**
- Vorhersage:
  - V5a (gleich): "Median-Ueberleben (Polsumme) bei 5/Gamma0 >= 1e-2 fuer alle N; Median Gamma_min <= 0,01."
  - V5b (gemischt): "Median Gamma_c in [0,9; 1,1]; Median-Ueberleben innerhalb Faktor 2 von 4,5e-5."
  - V5c (gleich): "Median Gamma_min faellt monoton mit N (2, 5, 10, 20). Das waere die Lokalisierung."
  - V5d (periodisch 37,5): "Ueberleben zwischen gemischt und gleich."
- Ergebnis (N = 2 / 5 / 10 / 20; grob = fein ausser Gamma_min bei N = 10 und 20):
  - gleich: Median Polsumme bei 5/Gamma0 0,167 / 0,160 / 0,339 / 0,249; CMT 0,253 / 0,252 / 0,341 / 0,0799; Median
    Gamma_min 4,75e-5 / 5,92e-7 / 6,5e-15 (fein 3,2e-14) / 3,7e-15 (fein 1,6e-14); dunkle Pole 1 / 4 / 10 / 23.
  - gemischt: Median Gamma_c 0,9991 / 0,9981 / 0,9980 / 0,9978; Polsumme 4,59e-5 / 4,61e-5 / 4,61e-5 / 4,68e-5.
  - periodisch: Polsumme 0,175 / 0,106 / 0,0892 / 0,0841; Gamma_c 0,0573 / 0,0045 / 0,0006 / 0,0001.
  - Einzelball: 4,54e-5.
  - Summenregel: nicht im Bericht. Aus der Ergebnis-JSON (grob):
    - "gleich" N = 10: in 0 von 5 Seeds in 1 +- 0,05; N = 20: in 1 von 5.
    - Werte 0,785 bis 1,084; es fehlen je 1 bis 3 Pole.
    - Ebenso periodisch N = 20: 0,881 (37/41 Pole).
- Treffer:
  - V5a und V5b getroffen.
  - V5c formal getroffen. Die Stufen N = 10 -> 20 liegen aber bei 1e-14, unter der im PLAN genannten
    Rechengenauigkeit von ~1e-9.
  - V5d teilweise: bei N = 2 liegt periodisch (0,175) ueber gleich (0,167).
- Urteil: teilweise.
- L3 laut Bericht: 12 von 12.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken. "Gleich" (Zufallsabstaende) und periodisch schuetzen, gemischt nicht; das Lokalisierungszeichen
  V5c ist nur auf 1e-14-Niveau monoton, und die Polsummen bei N >= 10 stehen auf unvollstaendigen Polmengen.

### Weber-Zerspritzen

Vorab aus `papier` (Formeln, Rauchtest-Log LAUF1.log): We-Faktor 11,44 / 15,96 / 25,77 fuer omega^2 = 0,6 / 0,7 / 0,8;
v_cl (V2 = +0,01 / +0,02) 0,1182 / 0,1658 (0,6), 0,1119 / 0,1571 (0,7), 0,1070 / 0,1504 (0,8); We_cl 0,160 / 0,315,
0,200 / 0,394, 0,295 / 0,583.

**W-1 1D-Karte (`karte1d`): Weber-Bild H und Gegenhypothese G im groben v-Raster**
- Vorhersage:
  - V-H1: "Wenn das Weber-Bild stimmt, liegt die Zerfallsschwelle bei allen drei Ballgroessen bei derselben We_c >= 1,4.
    Oberhalb davon zerfaellt der Ball immer (monoton in v)."
  - V-G2: "V2 = +0,01: zurueck bei v = 0,05 und 0,10, durch ab 0,15. V2 = +0,02: zurueck bis 0,15, durch ab 0,20.
    Einzige wahrscheinliche Ausnahme ist (0,8; +0,02; 0,15) ... gespalten oder haengt. Anziehende Stufen: durch fuer
    alle v >= 0,10. ... Kein Zerfall bei v >= 0,25 an irgendeiner Stufe."
  - Erwartung des Autors: "G gilt, H scheitert an L1".
- Ergebnis (grob Laptop-CPU / fein .69):
  - 144 Laeufe, We bis 4,123. Zerfall: in keinem Lauf, in beiden Stufen.
  - Alle Laeufe haben ein Fragment; q_haupt 0,986 bis 0,996 (fein 0,987 bis 0,996); frei 0,004 bis 0,014.
  - Klassenwechsel: V2 = +0,01 bei v 0,10 -> 0,15 (alle drei omega^2); V2 = +0,02 bei 0,15 -> 0,20 (0,6 und 0,7);
    (0,8; +0,02): 0,10 reflektiert, 0,15 haengt, 0,20 durch.
  - Anziehende Stufen und V2 = 0: alle "durch", auch bei v = 0,05 (zurueck 0,000).
  - Gegenprobe V2 = 0: 24 von 24 durch, q_haupt 0,995 bis 0,996.
  - Teilchenbild: stimmt in allen Laeufen ausser (0,8; +0,02; 0,15) "haengt"; dieser Lauf liegt im ausgenommenen Band
    +-10 % um v_cl = 0,1504.
  - E-Drift hoechstens 4,6e-4 / 4,4e-4 (0,8; -0,04; v = 0,05), sonst hoechstens 1,4e-4.
- Treffer: V-H1: H scheitert an L1 (Bericht: "kein Zerfall ... bis We = 4.12 -> H scheitert (L1)"). Damit ist die
  Erwartung des Autors getroffen. V-G2 getroffen, einschliesslich der vorhergesagten Ausnahme.
- Urteil: getroffen.
- L3 (von Hand, Bericht grob gegen Bericht fein):
  - 144 von 144 Klassen gleich, Zerfall nirgends.
  - Alle 18 Schwellenzeilen und die drei Urteilszeilen gleich.
  - q-Spalten in 14 Zeilen um 0,001 verschieden, sonst gleich.
  - Verlangt waren hoechstens ein Klassenwechsel, kein Zerfallswechsel und |dq| <= 0,05: bestanden.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: verwerfen (Weber-Bild H in 1D). Bis We = 4,12 zerfaellt in beiden Aufloesungen nichts; die Klassenwechsel
  liegen an der Teilchenschwelle, also bei Energieerhaltung (L4).

**W-2 Feinscan um die Teilchenschwelle (`feinv1d`, abstossende Stufen)**
- Vorhersage (V-G1): "Der Uebergang zurueck -> durch (q_durch = 0,5) liegt bei allen sechs (omega^2, V2) innerhalb von
  5 % um v_cl. Das Spaltfenster (0,1 < q_durch < 0,9) ist hoechstens +-5 % breit. Genau an v_cl kann der Ball auch
  'haengen' bleiben ... We am Uebergang ist nicht konstant: We50(0,8)/We50(0,6) ≈ 1,85."
  - L1 fuer G (PLAN Abschnitt 8): "G scheitert, wenn v50/v_cl ausserhalb [0,9; 1,1] liegt, oder an anziehenden Stufen
    bei v >= 0,25 gespalten oder zerspritzt wird."
- Ergebnis (grob Laptop / fein .69; 54 Laeufe, v/v_cl = 0,80 bis 1,20):
  - Bis v/v_cl = 0,98 "reflektiert" (zurueck 0,994 bis 0,996).
  - Bei 1,00 in allen sechs Faellen "haengt" (ein Fragment bei x = 6,1 bis 7,7).
  - Ab 1,02 "durch" (0,994 bis 0,996).
  - v50/v_cl = 1,0100 in allen sechs Faellen und beiden Stufen; Spaltfenster leer; kein Zerfall; ein Fragment in jedem
    Lauf.
  - We50: 0,163 / 0,321 (0,6), 0,204 / 0,402 (0,7), 0,301 / 0,595 (0,8) fuer V2 = +0,01 / +0,02.
  - We50(0,8)/We50(0,6) = 1,848 (V2 = +0,01) und 1,854 (+0,02).
  - E-Drift hoechstens 3,8e-5 / 4,8e-5.
- Treffer: V-G1 in allen vier Teilen getroffen; G scheitert nach PLAN-L1 nicht. Bericht: "Gegenhypothese/Teilchenschwelle
  getragen".
- Urteil: getroffen.
- L3 (von Hand): 54 von 54 Klassen gleich; v50 auf etwa 1e-6 gleich; Spaltfenster in beiden leer; We50-Verhaeltnisse
  gleich; q in 4 Zeilen um 0,001 verschieden. Bestanden.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: parken. Der Ball verhaelt sich an der Stufe wie ein Punktteilchen an der Energieschwelle (L4); ein
  Spaltfenster schmaler als das 2-%-Raster ist nicht ausgeschlossen.

**W-3 2D-Winkelprobe (`winkel2d`, P4000, grob und fein, 270 s)**
- Vorhersage (V-2D-1): "Bei 0 bis 60 Grad laeuft der Ball intakt durch. q_rechts(t_eval) >= 0,95 bei allen Winkeln ...
  Q_box faellt bei 0 und 20 Grad erst ab t ≈ 215 bis 230 (Randschicht), vorher nicht. Scheitert, wenn ein Winkel bei
  richtiger Auswertung q_haupt < 0,85 zeigt."
  - Gegenprobe V2 = 0: "durch, q_haupt >= 0,97".
  - H selbst sagt in 2D keinen Zerfall voraus (We_n <= 0,63).
- Ergebnis (omega^2 = 0,7, V2 = -0,02, v = 0,2; Winkel 0, 20, 25, 30, 35, 40 und 60 Grad, We_n 0,630 bis 0,157; dazu
  V2 = 0 bei 0 und 20 Grad):
  - Alle 9 Laeufe in beiden Stufen "durch", ein Fragment, q_haupt 0,997.
  - q_rechts(t_eval) 0,9987 bis 0,9996; q_box(t_eval) 1,0000.
  - t_randschicht: 208 (0 Grad), 217 (20), 223 (25), 230 / 231 (30), 240 (35), 251 (40); bei 60 Grad keine.
  - q_box(Ende): 0,102 (0 Grad), 0,113 (20), 0,121, 0,137, 0,179, 0,342 (40), 1,000 (60); V2 = 0: 0,249 und 0,596.
  - E-Drift hoechstens 2,1e-6.
  - 1D-Vergleich (0,7; -0,02): alle v "durch", We_c None.
- Treffer: V-2D-1 getroffen. t_randschicht liegt bei 0 Grad (208) knapp vor dem Band "≈ 215 bis 230", bei 20 Grad (217)
  darin.
- Urteil: getroffen.
- L3 laut Bericht: "L3 grob/fein: bestanden (verlangt: gleiche Klasse, |dq| <= 0,02)".
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: verwerfen (Zerfallsdeutung der Runde-3-Verluste). Bei 0 bis 60 Grad zerfaellt nichts; die Box-Ladung
  faellt erst, wenn der Ball die Randschicht erreicht.

### Finns F-5 schwer/leicht (RUNDE-05/r5d, .69, CPU)

**F5-1 Q-Atom (3D radial, `f51`, cpu, 147 s)**
- Vorhersage:
  - Befund-Kandidat aus dem linearen Rauchtest: "Ein stabiles Q-Atom hat genau ein Schwebeniveau. Bevor ein zweites (p)
    gebunden ist, kondensiert das erste."
  - V1a: "Die vier Laeufe im stabilen Fenster sind 'Atom stabil'. omega_chi liegt fuer Q = 1 auf 0,01 bei
    sqrt(m^2 + e0). Bei Q = 20 liegt omega_chi durch g4 hoeher, um weniger als 0,03."
  - V1b: "R_chi/R_psi > 1,2 bei m = 0,3, lam = -0,25 ... R_chi/R_psi <= 1 bei m = 0,6, lam = -0,6"
  - V1c (lam = 0): "zerlaeuft, Q_chi gehalten < 0,5."
  - V1d (tief): "Kondensation. C_max waechst mehr als dreifach und saettigt bei C ~ |lam| S/(2 g4) ~ 0,45; Q_chi bleibt
    erhalten (eps = 0)."
- Ergebnis (grob / fein):
  - s-Niveau e0: -0,0033 (lam -0,2), -0,0363, -0,0892, -0,1532, -0,2245, -0,3811, -0,5498 (lam -1,0); Radius 13,2 bis
    2,68; bei lam = -0,1 kein Niveau.
  - p-Niveau: ungebunden bis lam = -0,6, gebunden bei -0,8 (e = -0,0330, Radius 5,14) und -1,0 (-0,1362). d-Niveau:
    keines bis -1,0.
  - Stabilitaet des s-Niveaus:
    - m = 0,3: stabil bis -0,4 (omega0^2 = +0,0008 / +0,0009), tachyonisch ab -0,5
    - m = 0,6: stabil bis -0,6 (+0,1355), tachyonisch bei -0,8 (-0,0211) und -1,0
  - Zwischen lam = -0,6 und -0,8 liegt kein Rechenpunkt.
  - Dynamik: sechs Laeufe "Atom stabil", Q_chi und Q_psi gehalten 0,9965 bis 1,0000.
    - omega_chi 0,2716 / 0,1722 / 0,5691 / 0,3679 (Q = 1) bei omega^2 linear 0,0736 / 0,0291 / 0,3237 / 0,1356
    - Q = 20: 0,1998 (m = 0,3, lam -0,35) und 0,3675 (m = 0,6, lam -0,6)
  - R_chi/R_psi: 1,95 / 1,96 (m = 0,3, lam -0,25), 1,25 (lam -0,35), 1,33 (Q = 20), 1,47 (m = 0,6, lam -0,3), 0,88 / 0,89
    (m = 0,6, lam -0,6).
  - Gegenprobe lam = 0: Q_chi gehalten 0,0097, Radienverhaeltnis 8,25, "zerlaeuft".
  - tief: C_max-Wachstum 203,09 / 202,87, "Kondensation"; Q_chi im Fenster r < 40 0,8006 / 0,8019; Q_psi 0,9967.
- Treffer:
  - Befund-Kandidat im Raster bestaetigt: Bei keinem gerechneten lam sind s- und p-Niveau zugleich stabil gebunden. Fuer
    m = 0,6 ist das Intervall -0,6 bis -0,8 ungeprueft.
  - V1a getroffen (von Hand: sqrt(0,0736) = 0,271, sqrt(0,0291) = 0,171, sqrt(0,3237) = 0,569, sqrt(0,1356) = 0,368;
    Abweichungen hoechstens 0,002). Bei Q = 20 liegt omega_chi fuer m = 0,3 um 0,028 hoeher, fuer m = 0,6 um 0,0004
    tiefer statt hoeher.
  - V1b und V1c getroffen.
  - V1d teilweise: Kondensation ja; der Saettigungswert von C ist nicht im Bericht; Q_chi im Fenster 0,80, die
    Gesamtladung ist nicht im Bericht.
- Urteil: getroffen, V1d teilweise.
- L3 laut Bericht: Dynamik 16 von 16, linear (e0) 9 von 9.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: weiter. Das lam-Raster zwischen -0,6 und -0,8 fuer m = 0,6 verdichten; erst dann traegt "hoechstens ein
  Schwebeniveau".

**F5-2 Huelle auf der Wand (3D radial, `f52`, cpu2, 140 s)**
- Vorhersage:
  - V2a: "Die Huelle traegt bei a = 0,4 auf dem Kern 0,7: Wandanteil >= 0,5 auf [T/2, T], Q_chi gehalten >= 0,5. a = 0,2
    ist knapp gebunden, Wandanteil 0,3 bis 0,6. a = 0 zerlaeuft (Wandanteil < 0,2)."
  - V2b: "Der Kern 0,7 bleibt in allen Laeufen stabil (Q_psi >= 0,98, S-Aenderung < 0,3)."
  - V2c: "Der Kern 0,95 nackt zerfaellt oder wandelt sich innerhalb T = 400 (Q_psi < 0,9 oder S-Aenderung > 0,5)."
  - V2d: "Die Huelle rettet ihn nicht: '0,95 a = 0,4' hat dieselbe Klasse wie '0,95 nackt' und ein Q_psi auf 0,05
    gleich."
- Ergebnis (grob / fein):
  - Kern 0,7:
    - a = 0,4, A = 0,2: Wandanteil 0,626 / 0,619, Q_chi 0,720, "traegt"
    - a = 0,4, A = 0,05: 0,624 / 0,617, Q_chi 0,709, "traegt"
    - a = 0,2: 0,345 / 0,340, Q_chi 0,408, "traegt nicht"
    - a = 0: 0,002, Q_chi 0,002, C_max-Wachstum 9,05
    - in allen fuenf Laeufen Q_psi 0,9993 bis 0,9999, S-Aenderung hoechstens 0,126
  - Kern 0,95:
    - nackt: Q_psi 0,9936 / 0,9938, S-Aenderung 0,941 / 0,938, "zerfaellt"; a = 0 gleich
    - a = 0,4: Q_psi 0,4783 / 0,4715, S-Aenderung 0,999, omega_psi 1,00205 / 1,00193, Wandanteil 0,004, Q_chi 0,212,
      "zerfaellt"
  - Lineares Huellen-Niveau in allen vier Faellen gebunden und stabil (omega^2 0,2615 bis 0,3472).
- Treffer: V2a, V2b und V2c getroffen. V2d teilweise: Die Klasse ist gleich, Q_psi aber 0,478 gegen 0,994 (verlangt:
  gleich auf 0,05).
- Urteil: teilweise.
- L3 laut Bericht: 12 von 12.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 teilweise, L5 nein.
- Vorschlag: weiter. Der grosse Unterschied im Q_psi des instabilen Kerns mit und ohne Huelle war nicht vorhergesagt und
  ist ungeklaert.

**F5-3 Mischung und Oszillation (1D, `f53`, cpu, 320 s)**
- Vorhersage:
  - V3a: "P_max auf 10 % bei sin^2 2theta, Periode auf 5 % bei der Formel."
  - V3b: "eps = 0: P = 0."
  - V3c (schwerer Ball, chi m = 0,6 < omega): "Es gibt keinen stabilen gemischten Ball; er verdampft in das leichte Feld.
    ... Gemessen/Formel zwischen 0,5 und 2; Gamma(0,05)/Gamma(0,02) zwischen 4 und 9 (Formel 6,1)."
  - V3d (m = 1,2): "stabil, |Gamma| < 1e-5; p (schwerer Anteil) ~0,996 bleibt auf 0,002."
  - V3e (chi-Ball, Kopie mit m = 0,6): "stabil; p ~0,004 ... bleibt auf 0,002."
  - V3f: "eps = 0: Gamma = 0, p = 1."
- Ergebnis (grob; fein gleich auf 3 bis 4 Stellen):
  - Pakete, P_max gegen sin^2 2theta:
    - m = 0,6: 4,14e-3 gegen 3,89e-3; 2,54e-2 gegen 2,38e-2
    - m = 0,9: 4,254e-2 gegen 4,244e-2; 0,2173 gegen 0,2169
    - m = 0,97: 0,31421 gegen 0,31417; 0,74155 gegen 0,74114
    - Abweichung (von Hand) 0,01 bis 6,5 %; 6,4 und 6,5 % bei m = 0,6.
  - Perioden gemessen / Formel: 15,73 / 15,68; 15,52 / 15,51; 61,64 / 61,48; 56,04 / 55,58; 179,56 / 173,44;
    105,30 / 106,52. Abweichung (von Hand) 0,06 bis 3,5 %.
  - eps = 0: P_max = 0.
  - Ball ueber chi m = 0,6:
    - eps = 0,02: Gamma 7,135e-4 (Formel 1,059e-3), Lebensdauer 3359, Q_Ball 2,4415 -> 2,1797, p 1 -> 0,983
    - eps = 0,05: Gamma 1,462e-3 (Formel 6,481e-3), Lebensdauer 1546, Q_Ball 2,4415 -> 1,7811, p 1 -> 0,967
  - Ball ueber chi m = 1,2: Gamma 5,6e-8, Lebensdauer 4,4e7, p 0,99584 -> 0,99636.
  - chi-Ball m = 0,6: Gamma 5,9e-9 / 5,4e-9, p 0,00416 -> 0,00416.
  - eps = 0: Gamma 2,9e-10 / 1,8e-11, p = 1.
- Treffer: V3a, V3b, V3d, V3e und V3f getroffen. V3c teilweise: Der Ball verdampft; Gamma/Formel (von Hand) 0,674 bei
  eps = 0,02 (im Band) und 0,226 bei eps = 0,05 (verfehlt); Gamma(0,05)/Gamma(0,02) = 2,05 statt 4 bis 9.
- Urteil: teilweise.
- L3 laut Bericht: 20 von 20.
- Latten: L1 ja, L2 haelt, L3 bestanden, L4 bekannt, L5 teilweise.
- Vorschlag: parken. Das Pendeln folgt der Lehrbuchformel (L4); offen ist nur die zu kleine Verdampfungsrate bei
  eps = 0,05.

**F5-4 Unsichtbarer Kern (1D, `f54`; m = 0,3 auf cpu 387 s, m = 0,6 auf cpu2 418 s)**
- Vorhersage:
  - V4a: "Fuer k >= 0,6: R_mess/R_Born zwischen 0,7 und 1,3, und R(+lam) = R(-lam) auf 20 % (Vorzeichen unsichtbar)."
  - V4b: "Bei k = 0,25 unterscheiden sich R(-lam) und R(+lam) um mehr als 30 %; Born ist dort ungueltig ... Anziehung und
    Abstossung sind nur bei kleinem k unterscheidbar."
  - V4c: "Einfang < 1e-4 des Einstroms und |A| < 1e-3."
  - V4d (vorab ableitbar, Codeprobe): "R(m = 0,3, k) = R(m = 0,6, k) ... Ebenso lam = 0: R = 0."
- Ergebnis (grob; fein gleich auf 2 bis 3 Stellen), k = 0,25 / 0,4 / 0,6 / 0,9 / 1,3:
  - m = 0,3, lam = -0,3: R = 0,149 / 2,51e-2 / 1,95e-3 / 3,10e-5 / 3,85e-8
  - m = 0,3, lam = +0,3: R = 0,448 / 0,123 / 1,20e-2 / 2,42e-4 / 7,81e-7
  - m = 0,6, lam = -0,3: R = 0,134 / 2,60e-2 / 2,00e-3 / 3,14e-5 / 3,88e-8
  - m = 0,6, lam = +0,3: R = 0,412 / 0,126 / 1,22e-2 / 2,45e-4 / 7,85e-7
  - Born (beide Vorzeichen, beide m): 0,374 / 5,39e-2 / 4,15e-3 / 7,09e-5 / 1,43e-7
  - A = 1 - T - R bei k = 0,25: m = 0,3: +9,2e-4 (-lam), +1,40e-3 (+lam), ohne Kopplung +1,16e-3; m = 0,6: +4,6e-2,
    +6,0e-2, ohne Kopplung +5,36e-2. Bei k = 0,4: 1,4e-6 bis 2,9e-5. Bei k >= 0,6 in allen Laeufen etwa -1,2e-6 (ohne
    Kopplung T = 1,000001).
  - Einfang (|x| < 10, minus Bezug) bei k = 0,25: -2,5e-4 / -2,0e-4 (m = 0,3), -6,19e-3 / +5,6e-4 (m = 0,6); ab k = 0,4
    hoechstens 7e-7.
  - lam = 0: R = 0 in allen Laeufen.
- Treffer:
  - V4a verfehlt (von Hand, k >= 0,6): R/Born 0,27 bis 0,48 bei Anziehung und 2,9 bis 5,5 bei Abstossung;
    R(+lam)/R(-lam) = 6,1 / 7,8 / 20 bei k = 0,6 / 0,9 / 1,3, bei beiden Massen.
  - V4b getroffen (Faktor 3 bei k = 0,25). Der Zusatz "nur bei kleinem k unterscheidbar" ist durch das V4a-Ergebnis
    verfehlt.
  - V4c verfehlt bei k = 0,25 (Einfang und |A| ueber den Schwellen), getroffen ab k = 0,4.
  - V4d: lam = 0 gibt R = 0 (getroffen). R(m = 0,3) und R(m = 0,6) unterscheiden sich (von Hand) um 0,6 % (k = 1,3)
    bis 11 % (k = 0,25); der PLAN nennt dafuer keine Schwelle.
- Urteil: teilweise; die Kernvorhersage V4a ist verfehlt.
- L3 laut Bericht: 10 von 10 (m = 0,3) und 10 von 10 (m = 0,6).
- Latten: L1 ja, L2 teilweise, L3 bestanden, L4 bekannt, L5 nein.
- Vorschlag: weiter. V4a ist deutlich verfehlt (Vorzeichen bei grossem k sichtbar); vorher die Flussbilanz bei k = 0,25
  klaeren.

## 2. Auffaelligkeiten

### Messmittel und Kontrollen, die reissen

- **R-1, Polsuche in der Bragg-Kette:**
  - Im Messlauf fehlen Pole: 2/3, 2/5, 2/11, 5/21, 22/41 (JSON: newton_fehl 0 bei M = 1 und 2, also keine gescheiterten
    Newton-Laeufe).
  - Summenregel 0,562 / 0,521 / 0,581 / 0,000 / 0,000; damit ist die Polsumme nach V1e unverlaesslich.
  - Der .69-Rauchtest (h = 0,02) fand bei M = 1 und 2 noch alle Pole (Summenregel 1,002 / 1,008) und ein Ueberleben
    0,343 / 0,494 statt 2,4e-14 / 3,0e-23. Das ist nur ein Hinweis.
  - L3 kann das nicht aufdecken, weil grob und fein dieselben Pole verlieren.
  - Der PLAN nennt diese Grenze selbst (Abschnitt 8: "Die Polsumme kann bei stark entarteten dunklen Polen (lange
    Bragg-Ketten) unvollstaendig sein").
- **R-5, Summenregel nicht im Bericht:** In der JSON liegt sie fuer "gleich" N = 10 in keinem und fuer N = 20 in einem
  von fuenf Seeds in 1 +- 0,05 (0,785 bis 1,084), ebenso periodisch N = 20 (0,881). Die Medianwerte der Polsumme bei
  N >= 10 beruhen damit auf unvollstaendigen Polmengen. V5a haelt trotzdem, weil auch das CMT-Ueberleben weit ueber 1e-2
  liegt (0,341 und 0,0799).
- **F5-4, Flussbilanz ohne Kopplung (Gegenprobe lam = 0):**
  - A = 1 - T - R ist ohne Kopplung nicht null: +5,36e-2 (m = 0,6, k = 0,25), +1,16e-3 (m = 0,3, k = 0,25), 1,9e-5
    bzw. 1,4e-6 (k = 0,4).
  - Bei k >= 0,6 ist T = 1,000001, also A etwa -1,2e-6.
  - Bei k = 1,3 liegt R (3,8e-8 bis 7,8e-7) unter diesem Bilanzrest. Der Born-Vergleich ist dort nicht belastbar.
  - Bei k = 0,6 und 0,9 liegt R dagegen weit darueber; das V4a-Ergebnis steht dort.
- **R-1, nichtresonante Kette (V1d):** Gamma_c 1,124 und 1,145 bei M = 10 und 20, ausserhalb [0,9; 1,1]. Die Suche
  findet dort mehr Pole als resonante Baelle (2/1, 6/1), Summenregel 0,800 bis 0,910.

### Widersprueche zur Vorhersage

- **F5-4 V4a:** Das Vorzeichen der Kopplung ist bei grossem k nicht unsichtbar, sondern am deutlichsten:
  R(+lam)/R(-lam) = 6,1 / 7,8 / 20 bei k = 0,6 / 0,9 / 1,3 (von Hand). Born liegt um Faktor 2 bis 5,5 daneben, fuer
  Anziehung zu hoch und fuer Abstossung zu tief.
- **F5-2 V2d:** Mit Huelle verliert der instabile Kern 0,95 in T = 400 etwa die Haelfte seiner Ladung (Q_psi 0,478 /
  0,472), ohne Huelle 0,6 % (0,994). omega_psi steigt mit Huelle auf 1,002, also ueber die Masse 1.
- **F5-3 V3c:** Die Verdampfungsrate bei eps = 0,05 ist 0,23-mal die Formel. Das Verhaeltnis der Raten ist 2,05 statt
  4 bis 9 (Formel 6,1).
- **R-3:**
  - V3a gilt nur fuer einseitige Pumpe. Bei beidseitiger Pumpe dominiert die Periode lambda (Amp_k > Amp_2k in 7 von 7).
  - Bei Resonanz ist die Kraft fast unabhaengig von d (Amp_k, Amp_2k ~1e-6 bei max|F_rel| 17,7 und 35,5).
  - V3c: F bei eps_lin bis 5,77e-7 statt <= 1e-7; d_x einmal 29,0 statt >= 30.
- **R-4 V4c:**
  - Der Ring verfehlt grob (-0,3918) und trifft fein (-0,1539).
  - Nach der Rueckkehr sind die Raten negativ, die Amplitude waechst also (Ring grob -0,8858).
  - Die Fitguete ist bei Spiegel und Ring 300- bis 1600-mal schlechter als beim Schwamm (rms ln 4,0e-3 bis 1,9e-2 gegen
    1,2e-5). Der exponentielle Fit beschreibt dort keinen exponentiellen Verlauf.
  - Hinweis: Die lokale T = 600-Probe zeigte fuer den Ring +2,02, das andere Vorzeichen (keine Wertung).

### Unphysikalische oder ungenaue Zahlen

- **R-1, negative Abklingraten:** Gamma_min -6,9e-6 (M = 10) und -3,3e-5 (M = 20), grob = fein. Der PLAN nennt ~1e-9
  als Rechengenauigkeit und deutet |Gamma| ~ 1e-9 mit beliebigem Vorzeichen als Rauschen. Diese Werte liegen vier
  Groessenordnungen darueber. Bei festgehaltenen Baellen ohne Pumpe hiesse ein negatives Gamma Anwachsen.
- **R-5 V5c:** Die Monotonie N = 10 -> 20 steht bei Gamma_min 6,5e-15 -> 3,7e-15 (fein 3,2e-14 -> 1,6e-14), unter der
  Rechengenauigkeit. Grob und fein unterscheiden sich dort um Faktor 5.
- **F5-1 V1d:** Q_chi im Fenster r < 40 faellt auf 0,80, vorhergesagt war "bleibt erhalten". Die Gesamtladung steht
  nicht im Bericht.
- **Weber:** Schon ohne Stufe (V2 = 0) ist q_haupt 0,995 bis 0,996; "frei" 0,004 bis 0,005 steht damit auch ohne jede
  Wirkung der Stufe.

### Aufloesung, Raster, vorab Ableitbares

- **Weber-Schwelle ist eine Rasterangabe:**
  - v50/v_cl = 1,0100 in allen sechs Faellen und in beiden Stufen, auf 5 Stellen gleich.
  - Das ist die lineare Interpolation zwischen den Rasterpunkten 1,00 ("haengt", q_durch 0) und 1,02 ("durch", q_durch
    0,995).
  - Die Schwelle ist damit nur auf das Intervall 0,98 bis 1,02 v_cl bestimmt.
- **Weber, We50-Verhaeltnis vorab ableitbar:** 1,848 und 1,854 folgen damit aus v_cl und dem We-Faktor, die vor dem Lauf
  feststanden. `papier` gibt We_cl 0,160 / 0,295 und 0,315 / 0,583, also dasselbe Verhaeltnis (von Hand: etwa 1,84 und
  1,85). Die eigentliche Messung ist nur "Uebergang im Intervall 0,98 bis 1,02 v_cl".
- **Weber "haengt":** Die Klasse gilt am Laufende (T = 726 bzw. 45/v + 60). Ob der Ball danach nach einer Seite faellt,
  steht nicht im Bericht.
- **F5-1, Rasterluecke:** Fuer m = 0,6 ist das s-Niveau bei lam = -0,8 nur knapp tachyonisch (omega0^2 = -0,0211), das
  p-Niveau nur knapp gebunden (e = -0,0330). Zwischen -0,6 und -0,8 ist nicht gerechnet. Ein schmales Fenster mit zwei
  stabilen Niveaus ist nicht ausgeschlossen.
- **R-2z und R-4, Code-L3 "False":** Diese Eintraege sind Nullzeilen des Kriteriums, keine Aufloesungsfehler.
  Auffaellig ist trotzdem die Aenderung bei dM grob -> fein um 0,058 und 0,074 (0,9244 -> 0,9823, 1,0930 -> 1,0186).

### Dateien und Logs

- Die Syntaxfehler-Zeilen (kleintest.sh Zeile 31) stehen in drei Logs, siehe Grundlage. Die Rechnungen selbst enden mit
  status=0.
- weber/lauf-69/karte1d/karte1d_grob_bericht.txt ist bytegleich mit der lokalen Laptop-Datei (Kopf "cpu", CEST-Zeiten).
  Es ist kein eigener .69-Lauf.
- Die Reflexionslaeufe liefen auf p4000b, cpu3 und cpu4 (PLAN: p4000a, cpu, cpu2).

## 3. Abgleich mit RUNDE-06.md

- RUNDE-06.md ist zweimal gelesen: um 03:23 und erneut nach der Aenderung von 03:39:38 (Dateizeit).
- Die Abschnitte F-5 und Weber sowie die Karten-Tabelle sind in beiden Staenden gleich.
- Neu hinzugekommen sind Ergaenzungen zur 3D-Resonanz, RG-1 und KF-5. Sie gehoeren nicht zu Paket A und sind nicht
  geprueft.
- Fuer die Reflexion enthaelt RUNDE-06.md noch keine Zahlen; dort ist nur der Stand zu pruefen.

| Stelle in RUNDE-06.md | eingetragen | laut Bericht | Bewertung |
|---|---|---|---|
| Karten-Tabelle, Reflexion | "Code in Arbeit" | alle sechs Aufrufe gerechnet, rc = 0, letzter Ende 03:21:29 CEST | veraltet |
| Karten-Tabelle, Weber | "Code in Arbeit" | Karte grob und fein, Feinscan grob und fein, 2D gerechnet | veraltet |
| Karten-Tabelle, F-5 | "laeuft auf .69 cpu/cpu2" | fertig (KETTE-F5B-ENDE 03:13:35, KETTE-F5A-ENDE 03:18:14 CEST) | veraltet |
| Rechenorte | p4000a, p4000b, cpu, cpu2 | Reflexion zusaetzlich auf cpu3 und cpu4 | unvollstaendig |
| F5-1 | s-Niveau ab lam ~ -0,2; p erst bei -0,8; s dort tachyonisch | gleich (Raster) | stimmt |
| F5-1 | "Es gibt also hoechstens ein stabiles Schwebeniveau." | nur im lam-Raster; -0,6 bis -0,8 fuer m = 0,6 nicht gerechnet, bei -0,8 beide Niveaus knapp an der Grenze | zu stark formuliert |
| F5-1 | sechs Atomlaeufe stabil; 1,25 bis 1,96; 0,88; C_max Faktor 203; L3 16/16 | 1,25 bis 1,95 / 1,96; 0,88 / 0,89; 203,09 / 202,87; 16/16 (dazu linear 9/9) | stimmt |
| F5-2 | a = 0,4: 62 % an der Wand; a = 0,2 traegt nicht; L3 12/12 | 0,626 / 0,619 und 0,624 / 0,617; "traegt nicht"; 12/12 | stimmt |
| F5-2 | "Den instabilen Kern (0,95) rettet die Huelle nicht; er zerfaellt mit und ohne." | Klasse stimmt; Q_psi aber 0,478 mit gegen 0,994 ohne Huelle, V2d (gleich auf 0,05) verfehlt | unvollstaendig |
| F5-3 | "genau nach der Neutrino-Formel", P_max 0,31421 gegen 0,31417 | P_max-Zahl stimmt; bei m = 0,6 liegt P_max 6,4 bis 6,5 % daneben (im 10-%-Band) | "genau" zu stark |
| F5-3 | "Perioden auf 1 bis 4 %" | 0,06 bis 3,5 % (von Hand) | ungenau |
| F5-3 | "Lebensdauer 1500 bis 3400" | 1546 / 1547 und 3359 / 3363 | stimmt |
| F5-3 | "die Formel sagt 2- bis 4-mal schneller" | Gamma_Formel / Gamma_mess = 1,48 und 4,43 (von Hand); V3c-Baender verfehlt, nicht erwaehnt | Abweichung |
| F5-3 | p = 0,996, Lebensdauer ueber 4e7; eps = 0 keine Mischung | 0,99584 -> 0,99636; 4,36e7 / 4,41e7; P_max 0 | stimmt |
| F5-4 | k = 0,25: 15 % (Anziehung), 45 % (Abstossung), Born 37 % | stimmt fuer m = 0,3 (0,149 / 0,448 / 0,374); m = 0,6: 0,134 / 0,412 | m fehlt |
| F5-4 | "Das Vorzeichen der Kopplung ist bei kleinem k also sichtbar." | sichtbar bei allen k, am staerksten bei grossem k: R(+)/R(-) = 6,1 / 7,8 / 20 bei k = 0,6 / 0,9 / 1,3; V4a verfehlt | wesentliche Abweichung |
| F5-4 | "Einfang im Kernbereich hoechstens 0,6 %" | Betrag stimmt (6,19e-3), der Wert ist aber negativ (weniger chi-Ladung als im Bezugslauf); V4c-Schwelle 1e-4 bei k = 0,25 ueberschritten | Vorzeichen fehlt |
| F5-4 | m = 0,6 ohne Kopplung A = 0,054 | 5,36e-2 / 5,37e-2; zusaetzlich m = 0,3 ohne Kopplung A = 1,16e-3 | stimmt, unvollstaendig |
| Weber, Karte 1D | 144 Laeufe; kein Zerfall bis We = 4,12; H scheitert (L1); V2 = 0 bestanden | gleich, grob und fein | stimmt |
| Weber, Feinscan | "0,996 der Ladung zurueck, bis v/v_cl = 0,98" | 0,994 bis 0,996 (0,996 nur bei 0,6 und einem Teil von 0,7) | kleine Abweichung |
| Weber, Feinscan | "haengt" genau bei v_cl; ab 1,02 durch; Punktteilchen auf 2 % | gleich | stimmt |
| Weber, Feinscan | "Auch die Gegenhypothese 'Solitonspaltung wie bei NLS' scheitert." | Bericht grob und fein: "Gegenhypothese/Teilchenschwelle getragen"; PLAN-L1 fuer G nicht ausgeloest. Richtig ist nur: keine Spaltung beobachtet (Spaltfenster leer im 2-%-Raster); G liess hoechstens +-5 % zu | Abweichung im Urteil |
| Weber | "2D-Winkel laeuft", "Offen: 2D-Winkelprobe (p4000a eingereiht)" | gerechnet, Ende 03:20:19 CEST, rc = 0: kein Zerfall bei 0 bis 60 Grad, L3 bestanden | veraltet |

## 4. Zusammenfassung

| Paket | Test (Karte) | Ergebnis kurz | Urteil | L3 laut Bericht | L1 | L2 | L3 | L4 | L5 | Vorschlag |
|---|---|---|---|---|---|---|---|---|---|---|
| Reflexion | R-1 Bragg-Kette | heller Pol N +- 20 % (M <= 5); Polsuche verliert Pole, Summenregel 0,52 bis 0,58 bzw. 0; nichtresonant 1,12 / 1,15 bei M = 10 / 20 | teilweise | 20/21 (Nullzeile) | ja | teilweise | bestanden | bekannt | nein | parken |
| Reflexion | R-2 zwei Baelle, linear | dunkel 1e-14, hell 2,005, Abstaende lambda/2; Partner 0,69 bei 1,00 | getroffen | 2/2 | ja | haelt | bestanden | bekannt | nein | weiter |
| Reflexion | R-2z zwei Baelle, Zeit | dunkel 0,0031 / 0,0032 (grob), -0,0004 / 0,0001 (fein); hell 2,01 bis 2,03; einzel 1,01 | getroffen | 4/7 (3 Nullzeilen) | ja | haelt | bestanden | bekannt | nein | weiter |
| Reflexion | R-3 Strahlungsbindung | F bei linearer Pumpe 1e-10 bis 5,8e-7; beidseitig Periode lambda statt lambda/2 | teilweise | 14/14 | ja | haelt | bestanden | bekannt | nein | parken |
| Reflexion | R-4 Randreflexion | Schwamm = gross 1,0124 / 1,0031; Spiegel -0,11 / 0,01; Ring -0,39 / -0,15 | teilweise | 2/4 (2 Nullzeilen) | teilweise | haelt | teilweise | bekannt | Methode | weiter |
| Reflexion | R-5 Q-Ball-Gas | gleich 0,16 bis 0,34, periodisch 0,08 bis 0,18, gemischt 4,6e-5 (bei 5/Gamma0) | teilweise | 12/12 | ja | haelt | bestanden | bekannt | nein | parken |
| Weber | W-1 Karte 1D (H, V-G2) | 144 Laeufe, kein Zerfall bis We 4,12; Wechsel nur an der Teilchenschwelle | getroffen | von Hand 144/144 | ja | haelt | bestanden | bekannt | nein | verwerfen (H) |
| Weber | W-2 Feinscan v_cl (G) | zurueck bis 0,98, haengt bei 1,00, durch ab 1,02; keine Spaltung; We50-Verhaeltnis 1,85 | getroffen | von Hand 54/54 | ja | haelt | bestanden | bekannt | nein | parken |
| Weber | W-3 2D-Winkel | 0 bis 60 Grad intakt durch (q 0,997); Box-Ladung faellt erst an der Randschicht | getroffen | bestanden | ja | haelt | bestanden | teilweise | nein | verwerfen (Zerfallsdeutung R3) |
| F-5 | F5-1 Q-Atom | ein s-Niveau, p erst wenn s tachyonisch (im Raster); 6 Atome stabil; Wolke 0,88 bis 1,96 x Kern | getroffen | 16/16, 9/9 | ja | haelt | bestanden | teilweise | nein | weiter |
| F-5 | F5-2 Huelle | a = 0,4 traegt (62 %); Kern 0,95 zerfaellt mit und ohne, Q_psi 0,48 gegen 0,99 | teilweise | 12/12 | ja | haelt | bestanden | teilweise | nein | weiter |
| F-5 | F5-3 Mischung | P_max und Perioden nach Formel; Verdampfen 1,5- bis 4,4-mal langsamer als Formel | teilweise | 20/20 | ja | haelt | bestanden | bekannt | teilweise | parken |
| F-5 | F5-4 unsichtbarer Kern | k = 0,25: 15 % / 45 % gegen Born 37 %; grosses k: R(+)/R(-) 6 bis 20; Flussleck ohne Kopplung | teilweise | 10/10, 10/10 | ja | teilweise | bestanden | bekannt | nein | weiter |

## 5. Zwei Antworten fuer Finn

**"Kann Reflexion Q-Baelle oder ihre Schwingungen stabilisieren?"**
In der 1D-Rechnung ja, aber nur die Schwingung (Resonanz) und nur mit genau gleichen Nachbarn: Zwei gleiche Baelle im
richtigen Abstand klingen linear mit etwa 1e-14 statt 1 ab und in der vollen Zeitrechnung mit hoechstens 0,003 statt
1,0, und in einem Gas gleicher Baelle sind nach fuenf Abklingzeiten noch 16 bis 34 % der Anregung da statt 0,005 %.
Schon leicht verschiedene Nachbarn (omega^2 = 0,69 oder 0,65 bis 0,75) schuetzen nicht (Rate 0,996 bis 1,005), und
Strahlung bindet zwei Baelle nur mit einer Pumpe von aussen und sehr schwach (Kraft hoechstens etwa 6e-7). Ein
spiegelnder Rechenrand taeuscht Stabilitaet nur vor (Rate -0,39 bis +0,01 statt 1,0); alle diese Rechnungen halten die
Baelle fest.

**"Zerspritzt ein Q-Ball wie ein Tropfen?"**
Nein, in keinem gerechneten Fall. In 1D gab es in 144 Laeufen bis zur Weber-Zahl 4,12 und in 54 Laeufen nahe der Schwelle
weder Zerfall noch Spaltung: Der Ball behaelt mindestens 98,6 % seiner Ladung, wird unter der Teilchenschwelle ganz
zurueckgeworfen, bleibt genau an ihr auf der Stufe liegen und laeuft darueber ganz durch. In 2D laeuft er bei 0 bis 60
Grad intakt durch (99,7 %); die Ladung in der Box faellt erst, wenn er die Randschicht erreicht (ab t = 208 bis 251).

## Einfach gesagt

Ein Q-Ball klingt nach wie eine Glocke. Steht eine genau gleiche Glocke im richtigen Abstand daneben, loeschen sich
ihre abgestrahlten Wellen aus, und beide klingen fast ewig; eine etwas andere Glocke hilft nicht. An einer Stufe
zerplatzt ein Q-Ball nicht wie ein Wassertropfen, sondern verhaelt sich wie eine Kugel an einer Rampe: zu langsam rollt
er zurueck, genau an der Grenze bleibt er oben liegen, schneller rollt er drueber. Leichte Teilchen koennen auf einem
schweren Ball schweben wie Elektronen um einen Kern, in unserem Raster aber nur auf einer Stufe. Zwei Rechenwerkzeuge
haben Schwaechen gezeigt (verlorene Loesungen bei langen Ketten, ein Leck in der Flussbilanz), die vor weiteren Schluessen
behoben werden muessen.
