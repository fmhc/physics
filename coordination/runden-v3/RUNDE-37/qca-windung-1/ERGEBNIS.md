# QCA-WINDUNG-1: Ergebnis (Runde 41)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (alle per date):**
  - Start 2026-10-04 15:20:53 CEST; Literaturabrufe 15:30 und 15:31; Code ab 15:38; Plantext ab 15:43.
  - Rauchlaeufe 13:43:56 bis 13:59:49 UTC (PLAN.md Abschnitt 5). Plan und Code eingefroren 15:58:48 CEST
    (EINGEFROREN-SHA256.txt).
  - Hauptlaeufe auf der .69 ueber kleintest.sh (UTC = CEST - 2 h): siehe Tabelle "Laeufe" unten.
- **Kennzeichen:** [S] an der Quelle gelesen (Bessho/Sato, arXiv:2006.04204v3, S. 1 bis 5 als Bild); [S Abstract];
  [L] Gedaechtnis; [M] eigene Mathematik, nicht gegengelesen; [E] Rechnung im Modell; [P] Projektdatei; [F] Festlegung
  des Plans; [R] im Rauchlauf gesehen; [H] Hypothese.
- **Art des Ergebnisses:** Rechnung an Modellen (Literaturautomaten, Projekt-Automaten aus QCA-BCC-RUECK-1 und
  QCA-DIRAC-T-1, synthetische Abbildungen). Keine Messdaten, keine Messdatenbestaetigung.

## Ergebnis zuerst

1. **Keiner unserer Automaten traegt eine Takt-Windung [E]: W3 = 0 ueberall.** Gerechnet sind alle 31 gespeicherten
   Repraesentanten aus QCA-BCC-RUECK-1 (2, 4 und 8 Zustaende) und alle 31 Treffer der wiederholten 8-Zustands-Suche.
   Die 9 Repraesentanten mit 8 Zustaenden sind zugleich Treffer; es sind also 53 verschiedene Automaten. Darunter sind
   die 17 Treffer mit Rueckspruengen, alle ohne Inversion. Dazu kommen als Zusatz 26 Repraesentanten aus QCA-DIRAC-T-1.
   Auf allen vier Gittern gilt |W3| <= 4,3e-15 (bei den Doppelten mit gleichem Ergebnis). Die Automaten sind also
   vektorartig: Der Floquet-Weg zu einer Netto-Haendigkeit ist in ihnen nicht verwirklicht.
2. **Wo die Weyl-Punkte vollstaendig gefunden sind, traegt jede Luecke netto W3 [E].** Das gilt in 25 von 26
   auswertbaren Eintraegen: 5 Kontrollen und 20 RUECK-Eintraege. Diese sind 17 verschiedene Automaten, 11 davon mit 8
   Zustaenden und 48 bis 108 Weyl-Punkten.
   Die Grad-1-Kontrollen haben netto -1 bzw. +1 je Luecke (K-S1, K-S1m), alle anderen 0. Die Ausnahme ist die zerlegbare direkte Summe
   (K4_direkte_Summe, Kommutant 2) mit (-2, 0, 2, 0, -2, 0, 2, 0). Dort kreuzen sich die Baender der zwei entkoppelten
   Bloecke auf Flaechen. Meine Suche sieht solche Flaechen nicht, und die Aussage setzt isolierte Weyl-Punkte voraus.
   Nach dem Einfrieren nachgerechnet (Diagnose, kein Urteil):
   - Die Bloecke sind exakt entkoppelt.
   - Der Anteil der Gitterpunkte, an denen sich Phasen beider Bloecke auf eps naehern, waechst linear in eps
     (0,052 / 0,096 / 0,23 / 0,42 bei eps = 0,01 / 0,02 / 0,05 / 0,1). Das zeigt Flaechen.
   - Innerhalb eines Blocks waechst der Anteil wie eps^3. Das zeigt Punkte.
3. **Die Kontrolle mit W3 ungleich 0 bestaetigt die Floquet-Aussage [E, synthetisch].** Die Grad-1-Abbildung der Karte
   hat W3 = -1,000000. Bei Quasienergie 0 ("im Takt") liegen 7 Weyl-Punkte mit netto -1, bei pi ("Gegentakt") ein
   einzelner ungepaarter bei Gamma (-1). Der DP-Automat (W3 = 0) hat dagegen in beiden Takten je ein Links-rechts-Paar:
   A+ im Takt Gamma -1 und P' +1, im Gegentakt P +1 und H -1.
4. **Urteile:**
   - Nach Plan sind alle drei mechanisch "nicht auswertbar". Grund ist meine eigene Vorbedingung, die Nachbaupruefung
     bei Gamma: Sie scheiterte an 6 trivialen Automaten mit Sprunggewicht ~1e-15. Dort ist chiral_det 1e-24 bis 1e-43, also
     Rauschen, und der relative Vergleich auf 1e-6 ist sinnlos. Die Phasen stimmten auf 3e-15 [Selbstanzeige 11].
   - Nach Kartenwortlaut: WI0 eingetroffen, WI1 nicht eingetroffen, WI2 nicht eingetroffen (wegen der direkten Summe).
5. **Reproduktion bitgenau:** Alle 123 gespeicherten D-Werte der zehn wiederholten Faelle sind relativ 0 gleich, und
   die A der Repraesentanten sind identisch (numpy 2.4.4, 1 Thread). Die Zahl "17 Treffer mit Rueckspruengen ohne
   Inversion" aus CHIRAL-L stimmt (12 "rueck+Kegel iso proj" + 5 "rueck+Kegel").

## Urteile (lauf-69/auswertung.json; Kennzahlen aus den Laufdateien)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil nach Plan (mechanisch) | Urteil nach Kartenwortlaut | Kennzahlen |
|---|---|---|---|---|---|
| WI0 | Kontrollen: DP A+, A- und alle Automaten mit Inversion W3 = 0; Grad-1-Abbildung abs(W3) = 1; je innerhalb 0,05 | 90 % | nicht auswertbar (Vorbedingung Nachbau, Selbstanzeige 11) | eingetroffen | K-S1 -0,99999999999997; DP A+ 2,7e-17, A- 1,9e-17; 9 Automaten mit Inversion (K-S1inv, 6 Konstruktionen und 2 Form-P-Repraesentanten aus DIRAC-T-1), max abs(W3) 3,3e-18 |
| WI1 | [H] Mindestens ein Projekt-Automat ohne Inversion (Repraesentant oder wiederholter Treffer) hat abs(W3) >= 1 | 20 % | nicht auswertbar (dieselbe Vorbedingung) | nicht eingetroffen | 62 von 62 RUECK-Eintraegen (53 verschiedene Automaten) ohne Inversion haben round(W3) = 0, alle konvergiert; Vermerke "nur Repraesentanten", "nur Treffer" und "mit DIRAC-Zusatz": je nicht eingetroffen |
| WI2 | Kontrolle der Floquet-Aussage [M]: Wo die Weyl-Punkte vollstaendig gefunden sind, ist die Netto-Chiralitaet in jeder Quasienergie-Luecke gleich W3 | 85 % | nicht auswertbar (dieselbe Vorbedingung) | nicht eingetroffen | 26 von 95 Eintraegen auswertbar; 25 erfuellen es, abweichend nur K4_direkte_Summe_0 (-2, 0, 2, 0, -2, 0, 2, 0) bei W3 = 0 |

- **Diagnose ohne Bindung (nachtraeglich, keine Urteilsaenderung):**
  - Beschraenkt man die Nachbau-Vorbedingung auf nichttriviale Automaten, wo sie sinnvoll ist (dort bestanden), ergeben
    die gespeicherten Regeln dieselben Ausgaenge wie nach Kartenwortlaut: WI0 eingetroffen, WI1 nicht eingetroffen,
    WI2 nicht eingetroffen.
  - Fuer WI2 haengt der Ausgang an einem einzigen Automaten, und dessen Voraussetzung (isolierte Weyl-Punkte) ist
    verletzt. Die uebrigen 20 RUECK-Eintraege (17 Automaten) mit vollstaendiger Suche haben laut RUECK-1-Daten Kommutant 1, sind also
    unzerlegbar [P]; die 5 Kontrollen habe ich darauf nicht geprueft. Diese 25 erfuellen die Aussage alle. Die
    Karte sagt fuer diesen Fall: "Erst die Numerik bzw. die Formel pruefen, keine Physik-Aussage". Das tue ich hier:
    In allen 25 Faellen mit vollstaendiger Suche, in denen die Voraussetzung gilt, stimmt die Formel. Mein
    Vollstaendigkeitskriterium erkennt zerlegbare Automaten aber nicht.
  - Im Sinn des Kartenwortlauts ("wo die Weyl-Punkte vollstaendig gefunden sind") ist die direkte Summe streng genommen
    nicht vollstaendig erfasst. Ihre Entartungsflaechen fehlen; das zeigt die Diagnose nach dem Einfrieren. Ich lasse das
    Urteil trotzdem bei "nicht eingetroffen", weil die Zuordnung zu "vollstaendig" vor der Rechnung mechanisch
    festgelegt war.
- **Woran die Urteile haengen:**
  - WI1: an der Ganzzahligkeit. Alle Werte liegen 13 Groessenordnungen unter der Schwelle 0,05.
  - WI2: an meinem Vollstaendigkeitskriterium; zwei unabhaengige Suchen muessen gleich sein. Es versagt bei zerlegbaren
    Automaten. In 25 der 46 nichttrivialen RUECK-Eintraege war die Suche unvollstaendig, dort fehlen Weyl-Punkte. In 19
    davon ist die Summe der Chiralitaeten nicht 0, entgegen der Summenregel N W3 = 0.

## Tabelle je Automat (Projekt-Automaten aus QCA-BCC-RUECK-1)

- Spalten: Name (A = gespeicherter Repraesentant, B = wiederholter Treffer #i im Fall), Zustaende, Inversion, W3 bei
  N = 16 / 24 / 32 / 48 (gerundet auf 1e-6, "-0" = kleiner negativer Rest; alle |W3| <= 4,3e-15), Weyl-Punkte Suche 1 /
  Suche 2 und vollstaendig ja/nein, Chiralitaeten +1 / -1 der Suche 1, Netto je Luecke (Luecke 1 bis N, globale
  Beschriftung; nur bei vollstaendiger Suche aussagekraeftig).
- **Quasienergie:** Alle 3029 Weyl-Punkt-Eintraege der Projekt-Automaten (Suche 1, mit Doppelten) liegen "dazwischen", keiner bei 0 oder pi.
  Das ist eichabhaengig: Diese Automaten haben keine natuerliche Nullphase (die Suche liefert sie mit beliebiger
  globaler Phase; W(0) ist nicht auf I normiert). Eichfrei sind nur die Netto-Werte je Luecke.
- Orte: In jedem nichttrivialen 8-Zustands-Automaten liegen an Gamma, H, P und P' je vier Weyl-Punkte. Bei den K4- und
  K5-Automaten ist das netto 0 je Ort, bei den einseitigen K2- und K3-Treffern (Form O) netto +2 oder -2 je Ort; deren
  Suche ist unvollstaendig. Der Rest liegt an allgemeinen Punkten in T-Bahnen. Die Gamma-Kegel des ersten K4-Treffers (Phasen 0,551; -0,234; 1,613; -3,117)
  haben die Chiralitaeten +, +, -, -, wie CHIRAL-L gelesen hatte; sie liegen in vier verschiedenen Luecken (7, 5, 1, 3)
  und werden dort von Kegeln an H, P, P' und an allgemeinen Punkten ausgeglichen.

| Automat | Zust. | Inv. | W3 (16 / 24 / 32 / 48) | Weyl-Punkte | Chiralitaet | Netto je Luecke |
|---|---|---|---|---|---|---|
| A: L2:Pauli N frei | 2 | nein | 0 / 0 / 0 / 0 | 4/4 voll. | +2 / -2 (netto 0) | 0,0 |
| A: L2:Pauli N r50 | 2 | nein | -0 / 0 / -0 / 0 | 4/4 voll. | +2 / -2 (netto 0) | 0,0 |
| A: K4_gemischt_0 | 8 | nein | 0 / -0 / -0 / 0 | 104/100 unvoll. | +52 / -52 (netto 0) | 0,0,0,0,0,0,0,0 |
| A: K4_gemischt_1 | 8 | nein | -0 / -0 / -0 / -0 | 100/100 unvoll. | +52 / -48 (netto 4) | 0,4,0,0,0,0,0,0 |
| A: K4_gemischt_2 | 8 | nein | -0 / -0 / -0 / -0 | 88/84 unvoll. | +44 / -44 (netto 0) | 0,0,0,0,0,0,0,0 |
| A: K4_direkte_Summe_0 | 8 | nein | -0 / 0 / -0 / 0 | 16/16 voll. | +8 / -8 (netto 0) | -2,0,2,0,-2,0,2,0 |
| A: K5_gemischt_0 | 8 | nein | -0 / -0 / 0 / -0 | 120/112 unvoll. | +52 / -68 (netto -16) | 0,-8,0,0,0,-8,0,0 |
| A: K5_gemischt_1 | 8 | nein | -0 / -0 / -0 / -0 | 142/139 unvoll. | +66 / -76 (netto -10) | 0,-4,0,0,0,-6,0,0 |
| A: 4N T:1+3 N frei | 4 | nein | 0 / -0 / 0 / 0 | 4/4 unvoll. | +1 / -3 (netto -1) | -1,0,-1,1 |
| A: 4N T:1'+3 N frei | 4 | nein | 0 / 0 / 0 / 0 | 4/4 unvoll. | +0 / -4 (netto -3) | -1,-1,-1,0 |
| A: 4N T:2+2' N frei | 4 | nein | 0 / -0 / -0 / -0 | 8/8 voll. | +4 / -4 (netto 0) | 0,0,0,0 |
| A: 4N T:2+2'' N frei | 4 | nein | -0 / 0 / -0 / -0 | 8/8 voll. | +4 / -4 (netto 0) | 0,0,0,0 |
| A: 4O T:1+3 O frei | 4 | nein | 0 / -0 / 0 / -0 | 4/4 unvoll. | +1 / -3 (netto -2) | 1,-1,-1,-1 |
| A: 4O T:1'+3 O frei | 4 | nein | -0 / -0 / -0 / -0 | 4/4 unvoll. | +2 / -2 (netto 1) | 1,0,1,-1 |
| A: 4O T:2+2' O frei | 4 | nein | -0 / 0 / 0 / -0 | 8/8 voll. | +4 / -4 (netto 0) | 0,0,0,0 |
| A: 4O T:2+2'' O frei | 4 | nein | -0 / 0 / -0 / 0 | 8/8 voll. | +4 / -4 (netto 0) | 0,0,0,0 |
| A: 8 K4 N frei | 8 | nein | 0 / 0 / 0 / 0 | 64/64 voll. | +32 / -32 (netto 0) | 0,0,0,0,0,0,0,0 |
| A: 8 K5 N frei (einseitig) | 8 | nein | -0 / -0 / -0 / -0 | 80/80 voll. | +40 / -40 (netto 0) | 0,0,0,0,0,0,0,0 |
| A: 8 K4 N r50 | 8 | nein | 0 / 0 / 0 / 0 | 116/120 unvoll. | +64 / -52 (netto 12) | 4,0,0,0,4,0,4,0 |
| A: 8 K2 O frei (einseitig) | 8 | nein | -0 / -0 / -0 / -0 | 59/59 unvoll. | +31 / -28 (netto 3) | 0,0,0,-1,4,0,0,0 |
| A: 8 K3 O frei (einseitig) | 8 | nein | -0 / -0 / 0 / -0 | 55/55 unvoll. | +27 / -28 (netto -1) | 0,0,-5,0,0,4,0,0 |
| A: 8 K4 O frei | 8 | nein | 0 / 0 / 0 / 0 | 64/64 voll. | +32 / -32 (netto 0) | 0,0,0,0,0,0,0,0 |
| A: 8 K4 O r50 | 8 | nein | -0 / -0 / -0 / -0 | 104/92 unvoll. | +52 / -52 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 N frei#0 | 8 | nein | 0 / 0 / 0 / 0 | 64/64 voll. | +32 / -32 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 N frei#1 | 8 | nein | 0 / 0 / 0 / 0 | 120/120 unvoll. | +56 / -64 (netto -8) | -4,0,0,0,-4,0,0,0 |
| B: K4 N frei#2 | 8 | nein | -0 / 0 / 0 / 0 | 48/48 voll. | +24 / -24 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 N frei#3 | 8 | nein | -0 / -0 / -0 / -0 | 112/120 unvoll. | +56 / -56 (netto 0) | 4,0,-4,0,4,0,-4,0 |
| B: K4 N frei#4 | 8 | nein | -0 / -0 / -0 / -0 | 64/64 voll. | +32 / -32 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 N frei#5 | 8 | nein | -0 / -0 / -0 / -0 | 136/144 unvoll. | +72 / -64 (netto 8) | 0,0,4,0,0,0,4,0 |
| B: K4 N frei#6 | 8 | nein | -0 / -0 / -0 / -0 | 88/88 voll. | +44 / -44 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K5 N frei#0 (einseitig) | 8 | nein | -0 / -0 / -0 / -0 | 80/80 voll. | +40 / -40 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K5 N frei#1 (einseitig) | 8 | nein | -0 / 0 / 0 / 0 | 80/80 voll. | +40 / -40 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 N r50#0 | 8 | nein | 0 / 0 / 0 / 0 | 116/120 unvoll. | +64 / -52 (netto 12) | 4,0,0,0,4,0,4,0 |
| B: K4 N r50#1 | 8 | nein | -0 / -0 / -0 / -0 | 48/48 voll. | +24 / -24 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K2 O frei#0 (einseitig) | 8 | nein | -0 / -0 / -0 / -0 | 59/59 unvoll. | +31 / -28 (netto 3) | 0,0,0,-1,4,0,0,0 |
| B: K2 O frei#3 (einseitig) | 8 | nein | -0 / -0 / -0 / -0 | 51/51 unvoll. | +26 / -25 (netto 1) | 0,4,-4,0,0,3,-2,0 |
| B: K3 O frei#1 (einseitig) | 8 | nein | -0 / -0 / 0 / -0 | 55/55 unvoll. | +27 / -28 (netto -1) | 0,0,-5,0,0,4,0,0 |
| B: K3 O frei#2 (einseitig) | 8 | nein | -0 / -0 / -0 / -0 | 48/48 unvoll. | +27 / -21 (netto 6) | 0,0,-4,4,0,0,-1,7 |
| B: K4 O frei#0 | 8 | nein | 0 / 0 / 0 / 0 | 64/64 voll. | +32 / -32 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 O frei#1 | 8 | nein | -0 / -0 / -0 / -0 | 96/100 unvoll. | +48 / -48 (netto 0) | 0,0,4,0,4,0,-8,0 |
| B: K4 O frei#2 | 8 | nein | 0 / 0 / 0 / 0 | 48/48 voll. | +24 / -24 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 O r50#0 | 8 | nein | -0 / -0 / -0 / -0 | 108/108 voll. | +54 / -54 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 O r50#1 | 8 | nein | -0 / -0 / -0 / -0 | 104/92 unvoll. | +52 / -52 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 O r50#2 | 8 | nein | 0 / 0 / 0 / 0 | 76/80 unvoll. | +42 / -34 (netto 8) | 0,0,4,0,4,4,-4,0 |
| B: K4 O r50#3 | 8 | nein | 0 / 0 / 0 / 0 | 100/100 voll. | +50 / -50 (netto 0) | 0,0,0,0,0,0,0,0 |
| B: K4 O r50#4 | 8 | nein | 0 / 0 / -0 / -0 | 96/116 unvoll. | +46 / -50 (netto -4) | 0,0,0,0,0,0,-4,0 |

- **Trivial (16, keine Weyl-Suche, W3 <= 1e-36):** A: 4O T:1+1+1+1, 1+1+1+1', 1+1+1+1'', 1+1+1'+1', 1+1+1'+1'',
  2+2; A: 8 K1 O frei, K5 O frei; B: K1 O frei #0 bis #2, K2 O frei #1, #2, K3 O frei #0, K5 O frei #0, #1. Sprunggewicht
  ~1e-15, nicht exakt 0, deshalb erkennt mein Test keine exakte Inversion; W3 = 0 ist dort erzwungen [M].
- **Zusatz QCA-DIRAC-T-1 (26 Repraesentanten, ohne Weyl-Suche):** alle W3 <= 8,6e-15. Inversion erkannt bei den
  Konstruktionen a_spiegel und b_muenze_verschiebung (je m = 0,1; 0,3; 0,6) und bei den Form-P-Repraesentanten K4 und K5
  (8 Automaten). Nicht erkannt bei den Quell-Dirac-Automaten E+- (Grund nicht untersucht).

## Reproduktionsprobe (Stufe B)

| Fall | Treffer neu / gespeichert | D-Werte verglichen | groesste relative Abweichung | A des Repraesentanten |
|---|---|---|---|---|
| 8 K4 N frei | 7 / 7 | 24 | 0 | gleich (0) |
| 8 K5 N frei | 2 / 2 | 9 | 0 | gleich (0) |
| 8 K4 N r50 | 2 / 2 | 9 | 0 | gleich (0) |
| 8 K5 N r50 | 0 / 0 | 3 | 0 | - |
| 8 K1 O frei | 3 / 3 | 12 | 0 | gleich (0) |
| 8 K2 O frei | 4 / 4 | 15 | 0 | gleich (0) |
| 8 K3 O frei | 3 / 3 | 12 | 0 | gleich (0) |
| 8 K4 O frei | 3 / 3 | 12 | 0 | gleich (0) |
| 8 K5 O frei | 2 / 2 | 9 | 0 | gleich (0) |
| 8 K4 O r50 | 5 / 5 | 18 | 0 | gleich (0) |

- log10D-Listen gleich; numpy 2.4.4 alt und neu. Strikte Probe (1e-10 relativ) bestanden, auch der Vermerk "nur Werte
  >= 1e-20". Die alte Zaehlung gilt; neue Saaten waren nicht noetig.
- Kategorien der 31 wiederholten Treffer: 12 "rueck+Kegel iso proj", 5 "rueck+Kegel", 6 "einseitig", 8 "trivial"; mein
  Inversionstest findet bei keinem eine Inversion. Die 17 Rueck-Treffer sind die Zahl aus CHIRAL-L.

## Laeufe (UTC)

| Lauf | Spur | Inhalt | Start bis Ende | Rechenzeit |
|---|---|---|---|---|
| H-K | p4000b | Kontrollen | 13:59:38 bis 14:01:58 | 127,8 s |
| H-A1 | p4000b | Stufe A: RUECK Teil 0 (2 L2:Pauli, 6 Konstruktionen) | 14:01:59 bis 14:06:22 | 258,4 s |
| H-A2 | p4000b | Stufe A: 4 Zustaende (14) | 14:06:23 bis 14:08:59 | 126,2 s |
| H-A3 | p4000b | Stufe A: 8 Zustaende (9) | 14:09:10 bis 14:15:04 | 338,8 s |
| H-BN1, BN2, BN3 | p4000a | Wiederholung Form N (K4 frei; K5 frei; r50) | 13:59:45 bis 14:01:38 | 27,9 / 34,7 / 47,2 s |
| H-BOa, BOb | p4000a | Wiederholung Form O (frei; r50 K4) | 14:01:45 bis 14:05:40 | 175,0 / 20,5 s |
| H-WN1, WN23 | p4000a | W3 der N-Treffer | 14:05:42 bis 14:15:25 | 265,6 / 309,9 s |
| H-WOb | p4000a | W3 der O-r50-Treffer | 14:15:26 bis 14:19:09 | 204,1 s |
| H-WOa | p4000b | W3 der O-frei-Treffer | 14:15:06 bis 14:19:35 | 268,3 s |
| H-D | p4000a | Zusatz DIRAC-T-1 (--weyl 0) | 14:19:10 bis 14:20:10 | 59,4 s |
| Auswertung | p4000b | auswertung.py | 14:20:24 bis 14:20:25 | 0,7 s |

- Alle rc = 0, 1 Thread (OMP/OPENBLAS/MKL = 1 im Starter), 4 GB Grenze, hoechstens zwei meiner Laeufe zugleich.

## Literatur (2 von 3 Abrufen, keine Websuche)

- **Bessho/Sato, "Nielsen-Ninomiya Theorem with Bulk Topology: Duality in Floquet and Non-Hermitian Systems",
  arXiv:2006.04204v3, PRL 127, 196404 (2021)** [S, S. 1 bis 5 als Bild; quellen/bessho-sato-2006.04204v3.pdf,
  sha256 6a20e340...5d630d369]:
  - W3-Formel (Eq. 9): "w3 = -(1/24pi^2) Int_BZ tr[H^-1 dH]^3" mit "H(k) = iU_F(k)" (Eq. 3, 12). Damit ist
    w3 = -W3 in der Normierung der Karte; Betrag und Ganzzahligkeit sind gleich.
  - Floquet-Satz (Theorem 3', Eq. 15, S. 4): "n = Sum_{eps_a = mu} nu^mu_a, in case (i')"; Fall (i') sind Klassen A,
    AI, AII, "band crossing points with arbitrary energies in the quasi-energy spectra"; "alpha labels the Fermi
    surfaces defined by eps = mu, and nu^mu_a is the topological charge of gapless fermions inside the alpha-th Fermi
    surface". In Worten: Fuer **jede** Quasienergie mu ist die Gesamtladung der Weyl-Punkte innerhalb der Fermi-Flaechen
    gleich der Volumenzahl. Statisch ist die Zahl 0; das ist NN. Theorem 2 (Eq. 8, 10) ist dieselbe Aussage bei den
    Quasienergien 0 und pi, mit Orientierung laengs Re dE/dk.
  - Was die Quelle **nicht** woertlich sagt: "Netto-Chiralitaet je Luecke zwischen Band n und n+1 = W3". Die Bruecke
    (globale Bandbeschriftung, Ladungserhaltung je Band) ist meine (PLAN.md Abschn. 3) [M, nicht gegengelesen]. Das
    Vorzeichen "+W3 mit chi = lokaler Grad" habe ich vorab am Grad-1-Beispiel festgelegt und gerechnet bestaetigt.
- **Higashikawa/Nakagawa/Ueda, "Floquet chiral magnetic effect", arXiv:1806.06868v2, PRL 123, 066403 (2019)**
  [S Abstract]: "A single Weyl fermion, which is prohibited in static lattice systems by the Nielsen-Ninomiya theorem, is
  shown to be realized in a periodically driven three-dimensional lattice system with a topologically nontrivial
  Floquet unitary operator". Das ist das Literaturbeispiel mit W3 ungleich 0.
- 1D-Index (Gross/Nesme/Vogts/Werner 2012) [L], nur genannt.

## Methode (kurz; Einzelheiten PLAN.md)

- U(u) = Sum_f A_f exp(i u.f), u = k/sqrt3, Ableitungen analytisch. W3 = (1/8 pi^2) Int tr(X1 [X2, X3]) d^3u,
  X_j = U^dag d_j U, Rechteckregel ueber die primitive Zelle (Jacobi-Faktor 2 pi^3), N = 16, 24, 32, 48. Probe: Wuerfel
  [0, 2pi)^3 durch 4.
- Fuer die Fourier-Automaten ist der Integrand ein trigonometrisches Polynom (Frequenzen <= 6); die Rechteckregel ist
  ab N = 7 exakt [M]. Die N-Reihe ist dort eine Code- und Aliasingprobe. Echte Konvergenz zeigt nur die synthetische
  Abbildung (-0,999859 bei N = 16, -1,000000 ab N = 32).
- Inversion: invertierbarer V mit V U(u) = U(-u) V aus 32 Zufallspunkten (Nullraum, Kondition, Rest an 16 neuen Punkten).
- Weyl-Punkte: Gamma, H, P, P' direkt; dazu zwei unabhaengige Gittersuchen (40^3 ohne Versatz, 35^3 mit halbem Versatz,
  verschiedene Schnitte), Newton auf den sigma-Teil des Paares, Bahnergaenzung unter T. Chiralitaet chi = Vorzeichen von
  det M (lokaler Grad). "Vollstaendig" heisst: beide Suchen gleich, alle Punkte einfach.
- Luecke eines Weyl-Punkts: globale Bandbeschriftung ueber die Phase von det U (Windung 0 entlang b1, b2, b3), zwei Wege.

## Kontrollen (lauf-69/kontrollen.json, Lauf H-K)

| Kontrolle | Erwartung [M] | W3 bei N = 16 / 24 / 32 / 48 | Inversion | Weyl-Punkte (zwei Suchen) | Netto je Luecke |
|---|---|---|---|---|---|
| K-S1 Grad-1, m = 2 (Karte) | -1 (Abschn. 3 PLAN) | -0,999859 / -0,999999 / -1,000000 / -1,000000 | nein | 8 / 8, vollstaendig: 7 bei 0 (netto -1), Gamma bei pi (-1) | (-1, -1) |
| K-S1m = K-S1(-u) | +1 | +0,999859 / ... / +1,000000 | nein | 8 / 8, vollstaendig | (+1, +1) |
| K-S1q = K-S1^2 | -2 | -1,998450 / -1,999991 / -2,000000 / -2,000000 | nein | Knotenflaeche bei -I, nicht einfach (erwartet) | - |
| K-S1inv = K-S1(u) + K-S1(-u) | 0 | 2,5e-18 bis 5e-19 | **ja** (Rest 1,3e-15) | entkoppelte Bloecke, Flaechen, nicht einfach | - |
| K-MS8 = X1 S X2 S, 8 Zustaende | 0 | -4,3e-16 / ... / -4,0e-16; Wuerfel/4: -4,6e-16 | nein | 116 / 116, vollstaendig, 58 mit +1, 58 mit -1 | (0, 0, 0, 0, 0, 0, 0, 0) |
| DP A+ (Eq. 24, Quelle 2014) | 0 | ~1e-17 auf allen Gittern; Wuerfel/4: 1,5e-16 | nein | 4 / 4: Gamma -1, P' +1 (bei 0); P +1, H -1 (bei pi) | (0, 0) |
| DP A- | 0 | ~2e-17; Wuerfel/4: -1,0e-16 | nein | 4 / 4: Gamma +1, P -1 (bei 0); H +1, P' -1 (bei pi) | (0, 0) |

- QT3-Tabelle von QCA-TETRA-1 getroffen: A+ Gamma +I, P -I, H -I, P' +I; A- Gamma +I, P +I, H -I, P' -I (Abweichung
  <= 2,2e-16). Unitaritaet aller Kontrollen <= 1,1e-15; Imaginaerteile <= 2e-17; det-Windungen 0.
- Die Grad-1-Abbildung zeigt die Floquet-Aussage in kleinster Form: Bei Quasienergie 0 liegen sieben Weyl-Punkte mit
  netto -1, bei pi ein einzelner ungepaarter (Gamma, -1). Jede der beiden Luecken traegt netto W3 = -1.
- Die Chiralitaeten der DP-Kegel bestaetigen CHIRAL-L [M] (Gamma -1, P' +1 bei A+, Abbildungsgrad 0) numerisch.

## Selbstanzeigen

1. **Vor dem Einfrieren gesehen:** alle Kontrollwerte (K-S1, K-S1m, K-S1q, K-S1inv, K-MS8, DP A+-; erlaubt). Fuer
   Projekt-Automaten nur: Nachbaupruefung bei Gamma, Inversionsmerker, Trivialmerker, Laufzeit, Zahl der Weyl-Funde der
   zwei Suchen, ob sie gleich sind, ob alle einfach sind, fehlende T-Bildpunkte. Keine W3-Werte, keine Phasen, keine
   Chiralitaeten, keine Netto-Werte (Rauchmodus schrieb sie nicht).
2. **Code nach den Rauchlaeufen geaendert (vor dem Einfrieren, PLAN.md Abschn. 5):** Trivialkriterium um das
   Sprunggewicht ergaenzt (die "trivialen" RUECK-Treffer haben Sprunggewicht ~1e-14, nicht 0); Weyl-Suche in vier
   Schritten verstaerkt (32/27 -> 36/31 -> 40/35; 32 -> 64 -> bis 400 Kandidaten, Schwelle 0,5 -> 0,3; Bahnergaenzung
   unter T; Gamma, H, P, P' direkt; ein Schnitt je Suche); Zusammenfassen vektorisiert, Obergrenze 400 Punkte;
   Schalter --weyl; auswertung.py liest Teildateien per Muster. Anlass war allein die Vollstaendigkeit der Suche (Zahl
   und Gleichheit der Funde), keine W3- oder Chiralitaetswerte. Keine Urteilsregel geaendert.
3. **Die letzte Aenderung hat die Vollstaendigkeit teils verschlechtert:** Mit zwei Schnitten je Suche war
   K4_gemischt_0 im Rauchlauf 2d vollstaendig (104/104); mit einem Schnitt je Suche (eingefroren, halbe Laufzeit) ist es
   im Hauptlauf 104/100. Ich habe die Einschnitt-Fassung nur an 8Na K4|N|frei geprueft (64/64), nicht an den
   Konstruktionen. Nachtrag zu PLAN Abschn. 5: Rauch 1d (eingefrorene Fassung, Kontrollen) gab dieselben Werte wie
   Rauch 1, K-MS8 jetzt 116/116 vollstaendig; Rauch 2f (8Na K4|N|frei) 64/64 gleich, keine fehlenden Bildpunkte, 54 s.
4. **Skript auf der .69 ueberschrieben, waehrend ein Lauf es benutzte:** 15:47:47 CEST scp von code/windung.py und
   code/auswertung.py direkt ueber die Dateien, waehrend Rauchlauf 2 lief (Regel: neue Datei, dann mv). Python hatte die
   Datei beim Start gelesen; der Lauf endete mit rc = 0 und nutzte die alte Fassung. Danach immer .neu + mv.
5. **Eigene Rauch-Unit gestoppt:** r41rK3 (Kontrollen, alte quadratische Zusammenfassung) nach 2 min 38 s mit
   systemctl --user stop beendet. Nur meine Unit; keine fremden Prozesse angefasst.
6. **Aufteilung der Wiederholung abweichend von PLAN Abschn. 4:** Statt eines Aufrufs B-N drei (N1: K4|frei; N2:
   K5|frei; N3: r50, K4 und K5), damit die W3-Laeufe unter 10 min bleiben. Saaten haengen nur am Fall, nicht am Aufruf.
   Die drei Dateien habe ich auf der .69 mit jq zu lauf/wiederholung_N.json zusammengefuehrt (nur die Faelle-Tabelle),
   weil auswertung.py diesen Namen erwartet.
7. **Nach dem Einfrieren geschrieben:** code/tabellen.jq, code/zeilen.jq und lauf-69/tabelle_*.md (nur Anzeige per jq) sowie code/diag_summe.py (Diagnose der direkten Summe, ein Lauf ueber den Starter); nichts davon ist Teil der Auswertung.
8. **Werkzeuge:** Lokal ausser jq, sed, grep, sha256sum, date, ssh, scp, cp, mv, mkdir auch ls, cat, cut, tail, tr, wc und
   Warteschleifen (until ...; sleep) im Hintergrund bzw. als Monitor; kein python, awk oder perl lokal. Auf der .69
   ausserhalb des Starters nur mkdir, cp, mv, ls, cat, grep, tail, cut, sed, test, basename, sha256sum, jq, which, uptime, top (lesend),
   systemctl --user list-units (lesend) und einmal systemctl --user stop (eigene Unit); in einer Warteschleife paste und
   bc. Kein Python ausserhalb des Starters.
9. **Literatur:** 2 von 3 Abrufen. Die PDF lieferte das Abrufwerkzeug nur als Datei; gelesen habe ich S. 1 bis 5 als
   Bild (Theorem 2, 3', Eq. 8 bis 10, 15). Higashikawa u. a. nur als Abstract. Die Bruecke "netto je Luecke = W3" ist
   meine Herleitung [M], nicht gegengelesen.
10. **Saatformel:** Die Karte nennt seedbase*10000 + 10*vi (Teil-0-Formel); fuer Teil 8 gilt laut Code zusaetzlich
    + 2000 + 100*Form + Fall. Ich habe die Code-Formel benutzt (PLAN Abschn. 4).
11. **Fehler in meiner Vorbedingung, Ursache von "nicht auswertbar":**
    - Die Nachbaupruefung verlangt chiral_det relativ <= 1e-6. Bei den trivialen Automaten ist chiral_det 1e-24 bis
      1e-43 (Spruenge ~1e-7 und kleiner), also reines Rundungsrauschen.
    - Sechs von ihnen (8Oa K1 O frei; B: K1 #0, #2, K2 #2, K3 #0, K5 #1) verfehlten die Schwelle (1e-6 bis 0,37
      relativ), obwohl die Phasen auf <= 3,3e-15 stimmten. Bei allen nichttrivialen Automaten ist die Pruefung
      bestanden.
    - Den Fall habe ich beim Planen nicht bedacht. Ich habe die Regel nach dem Ergebnis nicht geaendert, und die
      offiziellen Urteile bleiben "nicht auswertbar". Die Urteile nach Kartenwortlaut stuetzen sich nicht auf diese
      Vorbedingung, weil die Karte sie nicht kennt (sie verlangt die Probe "an einem Repraesentanten").
12. **Schwaeche des Vollstaendigkeitskriteriums:** Zwei gleiche Suchen erkennen keine Entartungsflaechen zwischen
    entkoppelten Bloecken. Dort ist Newton singulaer, und die Kandidaten fallen still heraus. Das betrifft
    K4_direkte_Summe_0 (Kommutant 2 laut RUECK-1-Daten [P]) und entscheidet WI2. Die Begruendung ist eine
    Dimensionszaehlung [M]: Eine Phase aus Block 1 gleich einer aus Block 2 ist eine reelle Bedingung in drei Dimensionen.
    Nach dem Einfrieren habe ich das mit einem neuen Diagnoseskript nachgerechnet (code/diag_summe.py, Lauf r41dSumme,
    14:29:14 bis 14:29:22 UTC, lauf-69/diag_summe.json). Es aendert kein Urteil.
13. **"Diagnose ohne Bindung"** (Abschnitt Urteile) ist nachtraeglich und als solche gekennzeichnet; sie aendert kein
    Urteil.
14. **Weyl-Punkte nur teilweise vollstaendig:** In 25 von 46 nichttrivialen RUECK-Eintraegen sind die zwei Suchen
    ungleich. Deren Netto-Werte und Summen in der Tabelle sind unvollstaendig und nicht zu deuten.
15. **Zeitbox:** 120 min ab 15:20:53 CEST; Text abgeschlossen um 16:30:27 CEST (date).

## Bedeutung fuer Finns Frage

- **Belegt im Modell [E]:**
  - In keinem unserer Automaten traegt der Takt eine Windung. Das gilt fuer die Repraesentanten und Treffer aus
    QCA-BCC-RUECK-1 (auch die 17 mit Rueckspruengen) und fuer die Repraesentanten aus QCA-DIRAC-T-1.
  - Wo die Weyl-Punkte vollstaendig gefunden sind, hat jede Quasienergie-Luecke gleich viele links- wie rechtshaendige
    Punkte. Ausgenommen ist die zerlegbare direkte Summe, bei der die Voraussetzung isolierter Weyl-Punkte fehlt.
  - Beim DP-Automaten, der eine natuerliche Nullphase hat (W(0) = I), sitzen im Gegentakt (U = -I) P und H mit +1 und
    -1, im Takt Gamma und P' mit -1 und +1. Die Teilchen mit "falsch herum laufendem Takt" sind dort also selbst ein
    Links-rechts-Paar.
- **Synthetisch gezeigt [E, kein Projekt-Automat]:** Ein Takt mit Windung W3 = -1 erzeugt genau das Bild aus Finns
  Frage. Im Gegentakt sitzt ein einzelnes ungepaartes Teilchen, im Takt netto eines derselben Haendigkeit. Bessho/Sato,
  Theorem 3' [S]: Die Ladung bei jeder Quasienergie ist gleich der Volumenzahl. Meine Deutung [M]: Den Ausgleich traegt
  die Windung des Takts, nicht ein Partner bei derselben Quasienergie.
- **Vorab notierte Bedeutung (Karte), WI1 verfehlt:** Die gefundenen Automaten sind vektorartig. Der Floquet-Weg braucht
  eine gezielte Konstruktion. Folgekarte nach Karte: QCA-WINDUNG-2, ein BCC- bzw. Pyrochlor-Automat mit W3 = 1, dann
  Kegel und Isotropie pruefen. Hinweis [M]: W3 ungleich 0 verlangt, dass jede Quasienergie irgendwo in der Zone
  angenommen wird. Hat das Spektrum eine echte Luecke, ist U = exp(iH) stetig und damit W3 = 0.
- **Grenzen:**
  - Ein-Teilchen-Bild; keine Eichung, keine Wechselwirkung, kein Messbezug.
  - Die Tetraedergruppe T verbietet W3 ungleich 0 nicht [M, CHIRAL-L]. Dass alle Treffer W3 = 0 haben, ist ein Befund
    der Suche, kein Satz.
  - Eine echte Zeitumkehr allein tauscht nie links und rechts [L]; die Windung des Takts ist etwas anderes als eine
    Zeitumkehr.
- **Nicht gezeigt:** ob es T-kovariante BCC-Automaten mit W3 ungleich 0 gibt, wie viele Zustaende sie braeuchten und ob
  ihre Kegel isotrop waeren.

## Dateien

- **Plan:** PLAN.md und PLAN.md.eingefroren-20261004-155848; Pruefsummen in EINGEFROREN-SHA256.txt.
- **Quelle:** quellen/bessho-sato-2006.04204v3.pdf.
- **Code:** code/windung.py, code/wiederholung.py (Huelle, Zusatz A je Treffer), code/qca_rueck.py (unveraenderte
  Kopie, sha256 a42239a2...), code/auswertung.py, je mit .eingefroren-20261004-155848; code/tabellen.jq und
  code/zeilen.jq (Anzeige) und code/diag_summe.py (Diagnose), alle nach dem Einfrieren.
- **Rauchlaeufe:** rauch-69/ (Kontrollen 1 bis 4, Stufe A rauch bis rauch6, Wiederholung rauch und rauch2, Test der
  Auswertung in rauch-69/test/; rauch-69/windung.py.rauchfassung1 = erste Codefassung).
- **Hauptlaeufe:** lauf-69/kontrollen.json, stufeA_rueck_{1,2,3}.json, stufeA_dirac.json, wiederholung_{N1,N2,N3,N,Oa,
  Ob}.json, stufeB_{N1,N23,Oa,Ob}.json, auswertung.json, diag_summe.json, Logs r41h*.log und r41dSumme.log,
  tabelle_zeilen.md, tabelle_nichttrivial.md,
  PRUEFSUMMEN.txt.
- **Auf der .69:** /home/fmh/fmhc-physics-remote/runde41-qca-windung/ (code/, rauch/, lauf/, ref_rueck/, ref_dirac/).

## Einfach gesagt

Finn hat gefragt, ob links- und rechtsdrehende Teilchen vielleicht deshalb verschieden sind, weil ihr Takt falsch herum
laeuft. Bei einer Spielregel mit festem Takt ist so etwas moeglich: Ist der Takt selbst "verdreht" (Windungszahl), dann
bleibt in jedem Energiebereich ein Teilchen ohne Spiegelpartner uebrig. Eines davon sitzt im Gegentakt, also in dem
Zustand, der bei jedem Schritt sein Vorzeichen wechselt; das haben wir an einem kuenstlichen Rechenbeispiel genau so
gesehen. In allen Netz-Spielregeln, die wir bisher gefunden haben, ist diese Verdrehung aber null: Links- und
rechtsdrehende Teilchen kommen dort in jedem Energiebereich paarweise vor. Bei der einfachsten Spielregel gilt das auch
fuer die Teilchen im Gegentakt. Wer Finns Idee im Modell sehen will, muss eine Spielregel mit verdrehtem Takt gezielt
bauen; das ist eine Rechnung an Modellen, keine Messung.
