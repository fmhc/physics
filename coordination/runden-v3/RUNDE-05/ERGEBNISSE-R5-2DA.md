# Runde 5, Paket 2D-A (Zelle): Ergebnisse der Laeufe auf der .69

Auswertung: Anthropic-Agent (Opus 5.5) im Auftrag der Leitung claude-primary. Explorativ (v3), keine formale
Bestaetigung. Die Leitung entscheidet die Abschaetzung; alle Urteile, Latten und Vorschlaege unten sind Vorschlaege.

- **Beginn:** 2026-09-30 03:14:18 CEST (gemessen mit date)
- **Ende:** 2026-09-30 03:29:56 CEST (gemessen mit date)
- **Quellen:**
  - r5-2d-a/lauf-69/ausgabe/*_bericht.txt: profile, teilung, schale, polaritaet, vielzeller, groesse, replikation, phasen
  - r5-2d-a/lauf-69/LAUF1.log, LAUF2.log, LAUF3.log
  - Vorhersagen aus r5-2d-a/PLAN.md, Ideen aus RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md (5, 7, 23, 24, 28, 29, 49) und
    RUNDE-03/IDEEN-20-QBALL-CHEMIE.md (12)
- **Nicht gewertet:** lauf-69/rauchtest/ und der Rauchtest-Block am Anfang von LAUF1.log (Zeilen 1 bis 161).
- **Zahlen:** nur aus den Berichten. "Von Hand" markiert einfache Vergleiche von Berichtszahlen; sie stehen so nicht im
  Bericht.
- **Latten:** L4 und L5 aus der Lattentabelle in PLAN.md, L2 und L3 nach Bericht. L1 "ja" heisst: Vorhersage vorab
  festgelegt, sie konnte scheitern.

## Hinweise zum Lauf

- **Fehlende rc-Zeilen:**
  - In LAUF1.log fehlt die Zeile "ende ... rc=" fuer polaritaet, in LAUF2.log fuer phasen fein.
  - Grund laut Leitung: Das Startskript wurde waehrend des Laufs ueberschrieben; danach folgt ein Syntaxfehler von
    kleintest.sh (Zeile 31).
  - Beide Rechnungen melden "Finished with result: success" und "Main processes terminated with: code=exited/status=0".
    Ihre Berichte werden normal gewertet.
- **phasen_bericht.txt enthaelt nur die feine Stufe:**
  - drei Diagonalzellen, "Kennzahlen: {}"; Dateizeit 03:10, das ist das Ende des feinen Aufrufs
  - Die grobe Stufe (neun Zellen) steht nur noch in LAUF2.log (Zeilen 63 bis 73) und wird von dort gelesen.
  - PLAN 9 hatte fuer den zweiten Aufruf "--out ausgabe-fein" vorgesehen.
- **replikation:** eigener Aufruf nach der Teilung, LAUF3.log, rc=0.
- **Laufzeiten:** laut Log je Aufruf zwischen 1 min 25 s (profile) und 3 min 15 s (phasen fein), alle unter der
  10-min-Grenze.

## 1. Karten

### Karte 0: Profile (Vorpruefung, PLAN 1.2 und 0.2)

- **Vorhersage:**
  - "Virialrest unter 1e-5 in allen gueltigen Zeilen, alle 13 gueltig (p = 0,8)"
  - Loch bei m = 1 "etwa 2 (1 bis 3)", bei m = 2 "etwa 6 (4 bis 8), der Ball ist dort ein Ring"
- **Ergebnis:**
  - 13 von 13 Zeilen gueltig.
  - Virialrest (Betrag): m = 0 zwischen 1,5e-8 und 4,5e-7; m = 1 und m = 2 zwischen 1,3e-11 und 1,4e-10.
  - Klammer hoechstens 1,1e-14 (Betrag).
  - R_kern_halb: m = 1 zwischen 2,012 und 2,544; m = 2: 6,259 (omega^2 0,55), 4,816 (0,65), 5,469 (0,80).
  - m = 2 bei 0,55: R_kern_halb 6,259, R_max 9,930, R_halb 13,185, Q 627,878.
  - p bei m = 2: 0,00686 / 0,01632 / 0,00984. PLAN 0.2 nannte "etwa 1e-3".
- **Urteil:** getroffen.
- **L3 laut Bericht:** nicht im Bericht (nur Schiessen, keine zweite Aufloesung).
- **Latten:** L1 ja · L2 keine · L3 Virialrest · L4 entfaellt · L5 nein
- **Vorschlag:** weiter als Grundlage: Die berichtigte Schiessregel liefert alle m = 1- und m = 2-Profile mit kleinem
  Virialrest. Ob die alte Regel in tests2d_r3.py scheiterte (Vorhersage 0.2 fuer den R3-Rauchtest), steht nicht in
  diesen Berichten.

### Karte 1: Teilung und Vererbung (Bio 5/29)

Ideen: Bio 5 "Die Teilung kommt ab einer kritischen Groesse, wie bei Zellen." Bio 29 "Teilt sich m = 2, erben die
Toechter je m = 1."

- **Vorhersage (PLAN 2.3):**
  - Kern: "Kleine (dickwandige) Baelle teilen sich, grosse (flache) nicht." Toechter: "Windungen alle 0 mit p = 0,7,
    1 + 1 mit p = 0,2".
  - m2_080 "ja, p = 0,75, t_teilung 80 bis 450", Toechter "2 bis 4 (3 mit p = 0,4)"; m2_065 "ja, p = 0,55"; m2_055
    "nein, p = 0,6".
  - Gegenproben: m2_080_rein "spaeter als m2_080 oder gar nicht, p = 0,85"; m0_080 "nein, p = 0,97".
  - m = 1: m1_080 "ja, p = 0,45, 2 Toechter (l_dom = 2)", Windungen 0; m1_065 / m1_055 "ja, p = 0,25 / 0,1".
  - Eigendrehungen "unter 0,2 (p = 0,65)"; gamma (m2_080) "zwischen 0,01 und 0,1".
- **Ergebnis (grob; fein gleiche Ausgaenge):**

| Lauf | Q | Teilung t | Toechter: Q (alle Windung 0) | Jspin/Q | l_dom | gamma | Q/E-Verlust |
|---|---|---|---|---|---|---|---|
| m2_055 | 627,9 | keine | keine (Windung Ende 2) | - | 2 | - | 2,2e-4 / 4,6e-4 |
| m2_065 | 171,2 | 50 | 50,0 / 40,5 / 40,4 | 0,03 / 0,04 / 0,22 | 3 | 0,0913 | 0,99 / 0,99 |
| m2_080 | 111,1 | 30 | 25,1 / 23,9 / 20,9 / 12,4 | 0,02 / 0,05 / 0,01 / 0,01 | 3 | 0,1326 | 0,98 / 0,98 |
| m2_080_rein | 111,1 | 155 | 4 x 20,3 | je 0,03 | 4 | 0,1501 | 0,98 / 0,98 |
| m1_055 | 370,2 | keine | keine (Windung Ende 1) | - | 2 | - | 2,0e-4 / 4,8e-4 |
| m1_065 | 93,9 | 50 | 35,9 / 34,8 | 0,03 / 0,03 | 2 | 0,0926 | 1,0 / 1,0 |
| m1_080 | 60,1 | 35 | 24,4 / 19,2 | 0,02 / 0,02 | 2 | 0,1368 | 0,99 / 0,99 |
| m0_080 | 16,2 | keine | keine (Windung Ende 0) | - | 3 | - | 7,9e-5 / 5,5e-4 |

  - Fein: m2_055 ohne Teilung; m2_065 und m2_080 mit denselben Teilungszeiten, Toechterzahlen und Windungen, gamma
    0,0913 bzw. 0,1325.
  - Die Toechter haben Geschwindigkeitskomponenten bis 0,321. m2_080_rein: vier gleiche Toechter, Geschwindigkeiten
    jeweils um 90 Grad gedreht.
  - Kennzahlen: "Windung nicht vererbt: alle Toechter m = 0"; "klein teilt, gross nicht: umgekehrt zu Bio 5";
    gegenprobe_m0_ohne_teilung true; gegenprobe_rein_spaeter true.
  - Anteil des Drehimpulses in den Eigendrehungen: nicht im Bericht (nur Jspin/Q je Tochter, 0,00 bis 0,22).
- **Urteil:** teilweise, der Kern ist getroffen.
  - Getroffen: klein teilt, gross nicht; alle Toechter mit Windung 0; m2_080 mit 4 Toechtern (Fenster 2 bis 4); m1_080
    mit 2 Toechtern und l_dom 2; beide Gegenproben des PLAN.
  - Verfehlt: t_teilung 30 bzw. 50 statt 80 bis 450; gamma m2_080 0,1326 ueber 0,1; m1_065 teilt sich (vorab p = 0,25).
- **L3 laut Bericht:** bestanden (gleicher Ausgang und gleiche Windungen; gamma-Aenderung 1,3e-4 und 1,7e-4).
- **Latten:** L1 ja · L2 teilweise · L3 bestanden · L4 weitgehend · L5 mittelbar
  - L2 teilweise: Die Gegenproben des PLAN halten. Die Gegenprobe des Auftrags "m = 1 ohne Teilung" haelt nur bei
    omega^2 = 0,55.
- **Vorschlag:** verwerfen: Beide Ideen-Hypothesen stehen gegen das Ergebnis (der grosse Ball teilt sich nicht, die
  Toechter tragen keine Windung); neu waeren laut PLAN 10 nur die Schwelle in omega^2 (hier zwischen 0,55 und 0,65) und
  die Wachstumsraten, als eigene Frage.

### Karte 2: Q-Schale (Bio 7)

Idee: "Die Schalenform ist in unserem Potential ohne Eichfeld instabil. Mit Drehung koennte sie ueberleben."

- **Vorhersage (PLAN 3.3):**
  - m0 "fuellt sich: S(0) >= 0,5 bei t = 20 bis 80 (Mitte 40), p = 0,8; danach atmender Ball, 1 Gebiet"
  - m1 "Loch schrumpft auf etwa 2 bis 4 (Wirbelkern), fuellt sich nicht; p = 0,6"
  - m3 "Ring haelt, R_innen in der 2. Haelfte zwischen 6 und 12; p = 0,5"
  - m6 "Ring weitet sich auf R etwa 19 und zerfaellt in 3 bis 8 Tropfen mit Windung 0; p = 0,5"
  - scheibe "ruhig: 1 Gebiet, kein Bruch, p = 0,95"
  - Windungsschwelle zwischen 1 und 3, Papierzahl 2,6
- **Ergebnis (grob; fein gleich bis auf die Raender von R_innen):**

| Lauf | t_gefuellt | R_innen 2. Haelfte min / mittel / max | R_aussen Start / Ende | n_max | t_bruch | Windung Ende | Q-Verlust |
|---|---|---|---|---|---|---|---|
| m0 | 26,0 | 0 / 0 / 0 | 14,00 / 10,00 | 1 | None | 0 | 4,6e-2 |
| m1 | None | 1,00 / 3,69 / 6,50 (fein 1,25 / 3,69 / 6,50) | 14,00 / 11,75 | 1 | None | 1 | 1,2e-2 |
| m3 | None | 8,25 / 9,26 / 10,50 (fein 8,25 / 9,25 / 10,25) | 14,00 / 14,25 | 1 | None | 3 | 3,5e-3 |
| m6 | None | "-" | 14,00 / -1,00 | 4 | None | keine | 0,98 |
| scheibe | 0,0 | 0 / 0 / 0 | 11,50 / 11,25 | 1 | None | 0 | 2,1e-4 |

  - J/Q wie gebaut: 0 / 1 / 3 / 6 / 0.
  - Kennzahlen: "Schale fuellt sich nach t = 26.0"; m1 "Loch schrumpft unter 4 (Wirbelkern)"; m3 "Ring haelt bis T";
    gegenprobe_scheibe_ruhig true.
  - Fuer m6 steht in den Kennzahlen "Loch schrumpft unter 4 (Wirbelkern)". Das widerspricht der Tabellenzeile
    (Abschnitt 2.4).
  - m6: Weitung auf R etwa 19 und Windung der Tropfen nicht im Bericht (R_aussen Ende -1,00, am Ende kein Gebiet).
- **Urteil:** getroffen fuer m0, m1, m3 und die Scheibe; m6 teilweise (n_max 4 im Fenster 3 bis 8, der Rest nicht im
  Bericht). Bei m1 schrumpft das Loch auf einen Wirbelkern, m3 haelt den Ring: Die Schwelle liegt wie vorhergesagt
  zwischen 1 und 3.
- **L3 laut Bericht:** bestanden (alle fuenf).
- **Latten:** L1 ja · L2 gehalten · L3 bestanden · L4 ja · L5 nein
- **Vorschlag:** parken: Die Vorhersagen sind getroffen, laut PLAN weitgehend bekannt (Kapillarschluss, drehender Ring
  als Wirbelsoliton) und ohne Messbezug; vor jeder Weiterverwendung die m6-Zeile klaeren.

### Karte 3: Polaritaet im Gradienten (Bio 23)

Idee: "Im Gradienten wird der Q-Ball einseitig, wie eine polarisierte Zelle."

- **Vorhersage (PLAN 4.3):**
  - Fall: "a_mess/a_vorh = 1,00 +- 0,03 (p = 0,85)"
  - "d_QE = X_Q - X_E < 0 fuer g > 0 (p = 0,6)"; Betrag bei g = 1e-3 "zwischen 1e-5 und 1e-2", Schaetzung etwa 5e-4
  - Linearitaet "2,0 +- 0,2 (p = 0,8)"; Antisymmetrie "-1,0 +- 0,1 (p = 0,85)"
  - g = 0: "|d_QE| < 1e-8 und Schiefe < 1e-8 (p = 0,95)"
  - "Der kleine Ball (0,70) ist schwaecher polarisiert als der grosse (p = 0,6)"
  - Langstreckung "zweiter Ordnung in g, unter 1e-5 (p = 0,7)"
- **Ergebnis (grob; fein nahezu gleich, siehe L3):**

| Groesse | w55 (omega^2 0,55) | w70 (omega^2 0,70) |
|---|---|---|
| a_mess/a_vorh bei g = 5e-4 / +-1e-3 | 0,9958 / 0,9936 | 0,9994 / 0,9984 |
| d_QE bei g = +5e-4 (Streuung) | +2,703e-4 (6,6e-5) | +1,008e-4 (6,1e-5) |
| d_QE bei g = +1e-3 (Streuung) | +4,691e-4 (1,3e-4) | +1,926e-4 (1,2e-4) |
| d_QE bei g = -1e-3 | -4,691e-4 | -1,926e-4 |
| Linearitaet d(1e-3)/d(5e-4) | 1,735 | 1,911 |
| Antisymmetrie | -1,0000002 | -1,0000000 |
| g = 0: d_QE / Schiefe | -3,4e-17 / 3,9e-18 | 1,3e-16 / -2,2e-17 |
| d_SE bei g = +1e-3 | -1,142e-2 | -1,671e-3 |
| Schiefe bei g = +1e-3 | +6,98e-5 | -2,12e-4 |
| Langstreckung bei g = 5e-4 / +-1e-3 | -9,947e-4 / -3,984e-3 | -5,449e-4 / -2,181e-3 |
| y-Kontrolle (Betrag, grob) | hoechstens 2,3e-16 | hoechstens 1,0e-15 |

- **Urteil:** teilweise.
  - Getroffen: Fall (0,9934 bis 0,9994, fein eingeschlossen), Betragsfenster, Antisymmetrie, g = 0, der kleine Ball ist
    schwaecher polarisiert.
  - Verfehlt: Vorzeichen (d_QE > 0 bei g > 0); Linearitaet bei w55 (1,735, ausserhalb 1,8 bis 2,2); Langstreckung
    (Betrag 5,4e-4 bis 4,0e-3 statt unter 1e-5; fuer +g und -g gleich).
- **L3 laut Bericht:** bestanden (Aenderung von d_QE fein gegen grob 1,2e-7 bis 7,3e-7).
- **Latten:** L1 ja · L2 gehalten · L3 bestanden · L4 teilweise · L5 mittelbar
- **Vorschlag:** parken: Der Fall bestaetigt nur die bekannte QG-1-Linie; die innere Polarisation (d_QE hoechstens
  4,7e-4) hat das umgekehrte Vorzeichen der Papierrechnung und keinen Messbezug.

### Karte 4: Vielzeller (Bio 24)

Idee: "Drei oder vier Q-Baelle mit passenden Phasen bilden einen stabilen Verbund."

- **Vorhersage (PLAN 5.3):**
  - n3_gleich, n4_gleich "verschmolzen, p = 0,85; erste Verschmelzung bei t = 20 bis 200"
  - n3_wechsel "teilweise (die zwei gleichphasigen verschmelzen, der dritte wird abgestossen), p = 0,6"
  - n4_wechsel "auseinander, p = 0,75"
  - n3_windung "auseinander (cos 120 Grad < 0), p = 0,5; schwebend p = 0,3"
  - n4_windung "auseinander (Diagonalen gegenphasig), p = 0,5; schwebend (Klasse zusammen) p = 0,35"
  - n1_kontrolle "ruhig, p = 0,97"
  - Bio 24: "Kein Lauf endet als stabiler Verbund (p = 0,85)."
- **Ergebnis** (Ball omega^2 0,70: Q 23,996, R_halb 1,916, Seitenlaenge 7,832; fein gleiche Klassen und Zeiten):

| Lauf | Klasse | erste Verschmelzung t | n Ende | Abstand Start / max | Windungen Ende | Q-Verlust |
|---|---|---|---|---|---|---|
| n3_gleich | verschmolzen | 5 | 1 | 7,32 / 7,32 | 0 | 0,18 |
| n3_wechsel | verschmolzen | 10 | 1 | 7,91 / 7,92 | 0 | 0,63 |
| n3_windung | auseinander | None | 0 | 7,99 / 55,38 | keine | 0,87 |
| n4_gleich | verschmolzen | 5 | 1 | 8,52 / 8,52 | 0 | 0,21 |
| n4_wechsel | auseinander | None | 0 | 9,14 / 68,61 | keine | 0,97 |
| n4_windung | zusammen | None | 4 | 8,90 / 9,98 | 0, 0, 0, 0 | 5,1e-4 |
| n1_kontrolle | ruhig | None | 1 | 7,83 / - | 0 | 1,4e-8 |

  - Kennzahl: stabiler_verbund_gefunden true.
  - startzerlegung_ok (PLAN 1.3): nicht im Bericht.
  - Pruefung "echte Bindung oder nur Schweben" und Abstand am Ende (PLAN 5.3): nicht im Bericht.
- **Urteil:** teilweise; die Kernaussage ist verfehlt.
  - Getroffen: n3_gleich, n4_gleich, n3_windung, n4_wechsel, n1_kontrolle.
  - Verfehlt: n3_wechsel (verschmolzen statt teilweise); n4_windung (zusammen; vorab auseinander p = 0,5, schwebend
    p = 0,35); erste Verschmelzung von n3_gleich und n4_gleich schon bei t = 5 (erste Analyse) statt 20 bis 200; die
    Kernaussage "kein stabiler Verbund".
- **L3 laut Bericht:** bestanden (alle sechs Verbuende).
- **Latten:** L1 ja · L2 gehalten · L3 bestanden · L4 weitgehend · L5 nein
- **Vorschlag:** weiter, nur mit n4_windung: Er ist der einzige Verbund der Klasse "zusammen", und PLAN 5.3 und 10
  verlangen vor jeder Deutung die Frage Bindung oder Schweben, laengeres T und ein zweites Haus.

### Karte 5: Groessengrenze (Bio 28)

Idee: "Waechst ein drehender Q-Ball durch Einfang, wird er ab einer Groesse instabil und teilt sich." Umbau laut PLAN 6:
Futter durch gleichphasige Nachbarbaelle statt Zufluss aus einem Bad.

- **Vorhersage (PLAN 6):**
  - "Gefuetterte Laeufe verschmelzen bis T (p = 0,8)."
  - "Die Windung 1 bleibt im gewachsenen Ball (p = 0,6); Ausstoss des Wirbels p = 0,4."
  - "Keine Teilung nach dem Wachstum (p = 0,7 bei einem, p = 0,6 bei zwei Nachbarn): Bio 28 scheitert."
  - Kontrollen: "0,60 bleibt ganz (p = 0,85); 0,75 teilt sich (p = 0,35)"
- **Ergebnis (grob; fein gleiche Ausgaenge):**

| Lauf | Q_m1 + k Q_0 | J/Q | verschmolzen t | Windung groesstes: Ende; je gesehen | Teilung danach t | n Ende | Q-Verlust |
|---|---|---|---|---|---|---|---|
| w60_nachbarn0 | 138,8 | 1,000 | None | 1; 1 | None | 1 | 4,1e-9 |
| w60_nachbarn1 | 138,8 + 66,6 | 0,687 | 5 | None; 0 und 1 | 15 | 0 | 0,94 |
| w60_nachbarn2 | 138,8 + 2 x 66,6 | 0,536 | 5 | None; 0 und 1 | 10 | 0 | 0,81 |
| w75_nachbarn0 | 66,2 | 1,000 | None | None; 0 und 1 | 255 | 0 | 0,97 |
| w75_nachbarn1 | 66,2 + 19,0 | 0,792 | 5 | None; 0 und 1 | 15 | 0 | 0,99 |
| w75_nachbarn2 | 66,2 + 2 x 19,0 | 0,675 | 5 | None; 0 und 1 | 10 | 0 | 0,97 |

  - Kennzahlen: bio28 "Groessengrenze gesehen: gewachsener Ball teilt sich"; windung_behalten false in allen vier
    gefuetterten Laeufen; kontrollen_ohne_nachbarn: w60 null, w75 255.0.
  - Verlauf der Gebietszahl zwischen t = 0 und 20, also die Pruefung aus PLAN 10: nicht im Bericht.
- **Urteil:** verfehlt.
  - Getroffen: Verschmelzen (alle vier bei t = 5); Kontrolle 0,60 bleibt ganz.
  - Verfehlt: Teilung nach dem Wachstum in allen vier gefuetterten Laeufen; Windung nicht behalten.
  - Die Kontrolle 0,75 teilt sich ohne Futter bei t = 255 (vorab p = 0,35).
- **L3 laut Bericht:** bestanden (vier gefuetterte Laeufe, gleicher Ausgang).
- **Latten:** L1 ja · L2 teilweise · L3 bestanden · L4 teilweise · L5 nein
- **Vorschlag:** weiter, aber nur mit der Pruefung aus PLAN 10: Ob die "Teilung" bei t = 10 bis 15 ein gewachsener Ball
  ist, der zerfaellt, oder noch nicht verschmolzene Nachbarn, steht nicht im Bericht; bis dahin den Satz
  "Groessengrenze gesehen" nicht verwenden.

### Karte 6: Selbstreplikation (Bio 49)

Idee: "Im geladenen Bad waechst ein m = 2-Ball durch Einfang, teilt sich in zwei m = 1, die wieder wachsen und sich
teilen." Umbau laut PLAN 7: ohne Bad, bedingt auf eine Teilung in Karte 1.

- **Bedingung:** erfuellt. Karte 1 teilte m2_065 und m2_080, alle Toechter mit Windung 0. Aufruf mit
  --tochter-m 0 --omega2 0.80 (LAUF3.log).
- **Vorhersage (PLAN 7):**
  - "Toechter mit m = 0: Verschmelzen bei v etwa 0,4 unsicher (p = 0,4). Windung 2 entsteht nur mit p = 0,3 davon, also
    etwa 0,12. Zyklus p = 0,1."
  - "Bio 49 scheitert in beiden Faellen wahrscheinlich."
  - Gegenprobe: Einzeltochter bleibt ganz.
- **Ergebnis (grob; fein gleich):**

| Lauf | v | J/Q (Soll laut PLAN 7) | verschmolzen t | Windungen als ein Gebiet | m = 2 erreicht | neue Teilung t | n Ende |
|---|---|---|---|---|---|---|---|
| rueck_J2 | 0,4988 | 1,881 (2) | None | keine | nein | None | 0 |
| rueck_J1 | 0,2765 | 0,802 (1) | None | 0 | nein | None | 1 |
| einzel | 0 | 0 | None | 0 | nein | None | 1 |

  - Kennzahlen: zyklus false fuer beide; m2_erreicht false fuer beide; gegenprobe_einzel_ruhig true.
  - Q-Verlust: nicht im Bericht.
- **Urteil:** getroffen: kein Verschmelzen erkannt, kein m = 2, kein Zyklus; die Einzeltochter bleibt ruhig.
- **L3 laut Bericht:** bestanden (rueck_J2 und rueck_J1).
- **Latten:** L1 ja · L2 gehalten · L3 bestanden · L4 teilweise · L5 nein
- **Vorschlag:** verwerfen: Die Voraussetzung der Idee (Teilung in zwei m = 1) scheiterte schon in Karte 1, der Rueckweg
  zu m = 2 kam nicht zustande, und das Bad ist laut PLAN im Ein-Feld-Modell nicht umsetzbar.

### Karte 7: Endzustand nach Rauschstart (Chemie 12)

Idee: "Je nach mittlerer Dichte und Rauschenergie ('Temperatur') endet eine Box als Gas aus Wellen, als Tropfen
(Q-Materie) oder als Kondensat. Gibt es einen Tripelpunkt?" Umbau laut PLAN 8: 2D statt 3D, geschlossene Box ohne
Thermostat; einen Tripelpunkt "darf man daraus nicht ablesen".

- **Vorhersage (PLAN 8.4):**
  - Klassen je Zelle (Tabelle unten)
  - "Mindestens drei Klassen im Raster (p = 0,7)"
  - "Schranke in allen 9 Zellen erfuellt (p = 0,9)"
  - Startwerte E/Q etwa 0,98 / 1,25 / 1,83 (S0 = 0,1), 0,87 / 1,14 / 1,72 (0,4), 0,74 / 1,01 / 1,59 (0,9)
- **Ergebnis grob (aus LAUF2.log):** Klasse am Ende, in Klammern f_geb, danach die Vorhersage.

| S0 \ eps | 0,1 | 1 | 3 |
|---|---|---|---|
| 0,1 | T (0,669); vorh. T | T (0,700); vorh. G oder M | T (0,723); vorh. G |
| 0,4 | N (0,945); vorh. T oder N | T (0,962); vorh. T oder M | T (0,958; bei T/2 N); vorh. G |
| 0,9 | K (1,000); vorh. K | K (0,996); vorh. K oder N | K (0,959); vorh. G oder M |

  - E/Q Start gemessen: 0,9791 / 1,2186 / 1,7525 (S0 = 0,1); 0,8666 / 1,0737 / 1,5850 (0,4); 0,7442 / 1,0562 /
    2,0623 (0,9).
  - f_geb_min (Schranke): 0,071 / 0,455 / 0,874 in der Spalte eps = 0,1, sonst 0,000. Schranke "ja" in allen neun
    Zellen. Die Vorgaben "f_geb >= 0,43" bei (0,4; 0,1) und "f_geb >= 0,88" bei (0,9; 0,1) sind erfuellt (0,945 und
    1,000).
  - Stationaer (Klasse bei T/2 gleich der bei T): alle Zellen ausser (0,4; 3), dort N -> T. Kennzahl stationaer_alle
    false.
  - Q-Drift hoechstens 1,9e-15; E-Drift 2,6e-5 bis 4,7e-3 (groesster Wert bei (0,9; 3)).
  - Fein (phasen_bericht.txt): (0,1; 0,1) T -> T, f_geb 0,689; (0,4; 1) N -> T, f_geb 0,965; (0,9; 3) K -> K, f_geb
    0,965. E-Drift 1,1e-5 bis 1,3e-3.
- **Urteil:** teilweise.
  - Getroffen: 5 von 9 Zellen; drei Klassen (T, N, K); Schranke in allen Zellen.
  - Verfehlt: die Zellen (0,1; 1), (0,1; 3), (0,4; 3) und (0,9; 3). In keiner Zelle entsteht G (Gas) oder M.
- **L3 laut Bericht:** nicht im Bericht (Kennzahlen leer, weil grob und fein getrennt liefen).
  - Von Hand nach PLAN 9: Die Klasse am Ende ist in allen drei Diagonalzellen gleich (T, T, K). Die f_geb-Paare
    0,669/0,689, 0,962/0,965 und 0,959/0,965 liegen enger als 0,05 beieinander. Das Kriterium ist damit erfuellt.
  - Die Klasse bei T/2 weicht in (0,4; 1) ab: grob T, fein N.
- **Latten:** L1 ja · L2 schwach · L3 Handvergleich · L4 teilweise · L5 nein
  - L2 schwach: Die Schranke kann nur in den drei Zellen mit eps = 0,1 scheitern; in den anderen sechs ist f_geb_min
    0,000.
- **Vorschlag:** parken: Die Klassen beschreiben Endzustaende nach einem Rauschstart ohne Temperatur, einen Tripelpunkt
  kann man laut PLAN daraus nicht ablesen, und es gibt keinen Messbezug.

## 2. Auffaelligkeiten

### 2.1 Widersprueche zur Vorhersage

- **Karte 5, Groessengrenze:**
  - Der Bericht meldet "Groessengrenze gesehen"; vorhergesagt war "keine Teilung nach dem Wachstum".
  - Die Teilungen folgen 5 bis 10 Zeiteinheiten auf das Verschmelzen (verschmolzen t = 5, Teilung t = 10 bzw. 15).
    Danach ist kein Gebiet mehr in der Box (n Ende 0, Q-Verlust 0,81 bis 0,99).
  - Genau diesen Fall nennt PLAN 10 als erste Pruefung ("ob die 'Teilung' nur zwei noch nicht verschmolzene Nachbarn
    sind"). Ihr Ergebnis steht nicht im Bericht.
- **Karte 4, Vielzeller:**
  - n4_windung bleibt "zusammen": 4 Gebiete, Abstand 8,90 bis hoechstens 9,98, Q-Verlust 5,1e-4.
  - Der Bericht setzt stabiler_verbund_gefunden true, gegen die Kernvorhersage "kein stabiler Verbund (p = 0,85)".
  - Bindung oder Schweben, Abstand am Ende und Laenge von T stehen nicht im Bericht.
- **Karte 3, Polaritaet:**
  - d_QE hat das umgekehrte Vorzeichen: positiv bei g > 0.
  - Die Langstreckung ist 5,4e-4 bis 4,0e-3 statt unter 1e-5 und fuer +g und -g gleich.
  - Die Linearitaet bei w55 ist 1,735.
  - Die Streuung von d_QE ist gross: 1,2e-4 bei einem Mittel von 1,926e-4 (w70, g = 1e-3).
  - Frage, kein Befund: Haengt die Langstreckung mit der Fallbewegung des Balls zusammen? Der Bericht sagt dazu nichts.
- **Karte 1, Teilung:**
  - Die Teilung kommt frueher als vorhergesagt: t = 30 und 50 statt 80 bis 450.
  - gamma von m2_080 (0,1326) liegt ueber dem Fenster 0,01 bis 0,1.
  - m1_065 teilt sich (vorab p = 0,25).
- **Karte 4, weitere Abweichungen:**
  - Gleichphasige Baelle verschmelzen schon bei der ersten Analyse (t = 5).
  - n3_wechsel endet "verschmolzen" statt "teilweise".
- **Karte 7, Phasen:**
  - In keiner Zelle entsteht Gas.
  - Bei (0,9; 3) liegt E/Q bei 2,0623, der Papierwert war etwa 1,59. Klasse dort K mit f_geb 0,959.
- **Karte 6, Replikation:**
  - Der Aufbau trifft das Soll-J/Q nicht: 1,881 statt 2 (rueck_J2), 0,802 statt 1 (rueck_J1).
  - PLAN 7 nimmt an, die wahren Toechter seien leichter als die gebauten ("ihre wahre Ladung ist kleiner").
  - Der gebaute m = 0-Ball bei omega^2 = 0,80 hat Q = 16,231 (profile). Die Toechter von m2_080 hatten 25,1 / 23,9 /
    20,9 / 12,4; drei von vier waren also schwerer.

### 2.2 Gerissene oder schwache Kontrollen

- **Auftrags-Gegenprobe "m = 1 ohne Teilung" (Karte 1):**
  - Sie haelt nur bei omega^2 = 0,55; m1_065 (t = 50) und m1_080 (t = 35) teilen sich.
  - Der PLAN hatte das mit p = 0,25 bzw. 0,45 offen gelassen.
- **Kontrolle w75_nachbarn0 (Karte 5):**
  - Sie teilt sich ohne Futter (t = 255, n Ende 0, Q-Verlust 0,97).
  - Bei omega^2 = 0,75 unterscheiden sich gefuetterte und ungefuetterte Laeufe damit nicht im Ausgang, nur in der Zeit
    (10 bis 15 gegen 255).
- **Schranke (Karte 7):** In sechs von neun Zellen ist sie ohne Wirkung (f_geb_min 0,000 bei E/Q ueber 1).
- **Symmetrieproben (Karte 3):**
  - Antisymmetrie (-1,0000002), y-Kontrolle (hoechstens 1,0e-15) und g = 0 (d_QE hoechstens 1,3e-16) liegen auf
    Rundungsniveau.
  - Frage an die Leitung: Koennen diese Proben bei einem spiegelsymmetrischen Aufbau ueberhaupt scheitern?
- **Gehalten:** Scheibe (Karte 2), n1_kontrolle (Karte 4), Einzeltochter (Karte 6), m0_080 und m2_080_rein (Karte 1),
  w60_nachbarn0 (Karte 5).

### 2.3 L3

- **Laut Bericht bestanden:** teilung, schale, polaritaet, vielzeller, groesse, replikation. Kein Bericht meldet "nicht
  bestanden".
- **phasen:** kein L3 im Bericht. Der Handvergleich besteht fuer die Klasse am Ende und fuer f_geb; die Klasse bei T/2
  weicht in (0,4; 1) ab.
- **profile:** kein L3 (nur Schiessen).
- **Nur grob gerechnet:** Die Gitter-Gegenprobe m2_080_rein lief nur grob (PLAN 2.1); ihre Teilungszeit 155 ist also
  nicht gegen fein geprueft.

### 2.4 Bilanzen (Ladung, Energie, Drehimpuls)

- **Karte 1, Ladung und Energie:**
  - In allen geteilten Laeufen ist der Q/E-Verlust 0,98 bis 1,0 (Randschicht); bis T hat die Box ihre Ladung fast ganz
    verloren.
  - Die Toechter wurden laut PLAN 2.2 30 Zeiteinheiten nach der Teilung vermessen. Ihre Ladungen ergeben zusammen rund
    drei Viertel der Anfangsladung (von Hand: 0,73 bis 0,76).
  - Wohin der Rest ging (Strahlung, Gebietsraender), steht nicht im Bericht.
- **Karte 1, Drehimpuls:**
  - Die Mutter hat J/Q = m; die Toechter tragen Jspin/Q 0,00 bis 0,22.
  - Der Anteil der Eigendrehungen und J_Box ueber die Zeit stehen nicht im Bericht.
  - Der Zusatz "Drehimpuls in der Bahnbewegung" in der Kennzahl ist ein Text, keine gemessene Zahl.
- **Karte 2, m6:**
  - n_max ist 4, aber t_bruch None. Q-Verlust 0,98, am Ende kein Gebiet (R_aussen -1,00, keine Windungen).
  - Die Kennzahl sagt dazu "Loch schrumpft unter 4 (Wirbelkern)". Tabelle und Kennzahltext widersprechen sich.
- **Karte 4:**
  - n3_wechsel ist "verschmolzen" bei einem Q-Verlust von 0,63. Ob der dritte Ball ueber die Randschicht verloren ging
    und so ein Gebiet uebrig blieb, steht nicht im Bericht.
  - Die verschmolzenen gleichphasigen Verbuende verlieren 0,18 bzw. 0,21 der Ladung.
- **Karte 5:**
  - In allen gefuetterten Laeufen und in w75_nachbarn0 ist am Ende kein Gebiet mehr da (n Ende 0, Q-Verlust 0,81 bis
    0,99).
  - "windung_behalten false" kann daher auch heissen, dass kein Gebiet zum Messen mehr da war. Der Bericht trennt das
    nicht.
- **Karte 6:** rueck_J1 endet mit einem Gebiet, ohne dass ein Verschmelzen erkannt wurde (t verschmolzen None). Der
  Q-Verlust steht nicht im Bericht.
- **Karte 7:** Q bleibt erhalten (Drift hoechstens 3,7e-15). Die E-Drift erreicht 4,7e-3 grob und 1,3e-3 fein in
  (0,9; 3); der PLAN nennt dafuer kein Kriterium.
- **Karte 3:** a_mess/a_vorh 0,9934 bis 0,9994 zeigt die Kraft -g N im Rahmen der Vorhersage; die y-Kontrolle liegt
  auf Rundungsniveau.

### 2.5 Buchfuehrung

- phasen_bericht.txt ohne grobe Stufe (siehe "Hinweise zum Lauf").
- Im PLAN genannte Ausgaben, die in den Berichten fehlen:
  - startzerlegung_ok (Karte 4, PLAN 1.3)
  - Anteil der Eigendrehungen (Karte 1, PLAN 2.2)
  - Pruefung aus PLAN 10 fuer Karte 5
  - Die *_ergebnis.json-Dateien wurden nicht gelesen; dort koennten diese Werte stehen.
- Der Kennzahltext zu Schale m6 widerspricht der Tabelle (2.4).

## 3. Zusammenfassung

| Karte | Idee | Ergebnis | Urteil | L3 (Bericht) | L1 / L2 / L3 / L4 / L5 | Vorschlag |
|---|---|---|---|---|---|---|
| 0 profile | Vorpruefung | 13 von 13 Profilen gueltig, Virialrest hoechstens 4,5e-7, Loch m = 1 bei 2,0 bis 2,5, m = 2 bei 4,8 bis 6,3 | getroffen | nicht im Bericht | ja / keine / Virialrest / entfaellt / nein | weiter (Grundlage) |
| 1 teilung | Bio 5/29 | m = 2 teilt sich bei 0,65 und 0,80, nicht bei 0,55; alle Toechter Windung 0; Teilung bei t = 30 bis 50 | teilweise (Kern getroffen) | bestanden | ja / teilweise / bestanden / weitgehend / mittelbar | verwerfen |
| 2 schale | Bio 7 | m0 gefuellt bei t = 26; m1 Wirbelloch im Mittel 3,69; m3 Ring haelt; m6 in 4 Stuecke, Q-Verlust 0,98 | getroffen (m6 teilweise) | bestanden | ja / gehalten / bestanden / ja / nein | parken |
| 3 polaritaet | Bio 23 | Fall 0,993 bis 0,999 wie vorhergesagt; d_QE +4,7e-4 bzw. +1,9e-4 bei g = 1e-3 mit umgekehrtem Vorzeichen; Langstreckung bis -4,0e-3 | teilweise | bestanden | ja / gehalten / bestanden / teilweise / mittelbar | parken |
| 4 vielzeller | Bio 24 | gleichphasige verschmelzen bei t = 5; n4_windung bleibt "zusammen"; stabiler_verbund_gefunden true | teilweise (Kern verfehlt) | bestanden | ja / gehalten / bestanden / weitgehend / nein | weiter (nur n4_windung) |
| 5 groesse | Bio 28 | alle gefuetterten Baelle verschmelzen bei t = 5 und "teilen" sich bei t = 10 bis 15; Windung weg; am Ende kein Gebiet | verfehlt | bestanden | ja / teilweise / bestanden / teilweise / nein | weiter (nur Pruefung aus PLAN 10) |
| 6 replikation | Bio 49 | kein Verschmelzen erkannt, kein m = 2, kein Zyklus; J/Q 1,881 statt 2 und 0,802 statt 1 | getroffen | bestanden | ja / gehalten / bestanden / teilweise / nein | verwerfen |
| 7 phasen | Chemie 12 | Klassen T, N, K, kein Gas; 5 von 9 Zellen wie vorhergesagt; nicht alle stationaer | teilweise | nicht im Bericht (von Hand erfuellt) | ja / schwach / Handvergleich / teilweise / nein | parken |

## 4. Einfach gesagt

Wir haben am Rechner getestet, ob sich Q-Baelle wie Zellen verhalten. Drehende Baelle teilen sich wirklich, aber nur
die kleinen, und die Stuecke drehen sich danach nicht mehr selbst, sondern fliegen auseinander: Die Drehung wird nicht
wie ein Gen vererbt. Ein hohler Ball laeuft ohne Drehung nach etwa 26 Zeiteinheiten zu, mit dreifacher Drehung bleibt
er ein Ring. Zwei Ergebnisse muessen noch genauer angeschaut werden, bevor sie zaehlen: Vier Baelle, deren innere Uhren
um je eine Vierteldrehung versetzt laufen, blieben beisammen, und gefuetterte Baelle zerfielen kurz nach dem Wachsen.
Einen Vermehrungskreislauf und ein echtes Phasendiagramm gab es nicht.
