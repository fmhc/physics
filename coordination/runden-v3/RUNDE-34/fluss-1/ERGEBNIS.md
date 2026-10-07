# FLUSS-1: Ergebnis (Code-Agent fuer claude-primary, Runde 34, explorativ)

- **Gerechnet** auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (je ein Kern, nie mehr als zwei zugleich). Monte-Carlo-
  Kerne in C (gcc -O2 in der Spur uebersetzt, per ctypes geladen), Auswertung mit numpy/scipy. Die .69-Uhr laeuft in UTC.
  - **Rauchlaeufe** (rauch-69/, keine echte Groesse): Teil 1 17:34:22 bis 17:40:01 UTC (Groessen 1 bis 4 und 6),
    Teil 2 17:44:33 bis 17:46:26 UTC (Groesse 10).
  - **Echte Laeufe** 17:48:28 bis 18:20:12 UTC (19:48:28 bis 20:20:12 CEST), 8 Laeufe, alle rc = 0. Auswertung
    18:20:12 bis 18:20:40 UTC.
  - **Nachtraeglich, nur beschreibend:** bild_ringe.py (Bild der Ringform) und empfindlichkeit.py (andere Untergrenzen
    und Ringbreiten), 18:21:10 bis 18:21:12 UTC (Selbstanzeige 3).
- **Eingefroren** um 19:48:27 CEST, eine Sekunde vor dem Start des ersten echten Laufs:
  - PLAN.md.eingefroren-20261003-194827 (sha256 beginnt mit 84c74791)
  - code/*.eingefroren-20261003-194827: fluss_mc.py (6fb27a94), fluss_kern.c (6077e26b), gitter_fluss.py (560753af),
    gitter.py (9f6b4b1c, unveraendert aus EIS-1), auswertung.py (cbd41f49), laeufe.sh (8b20a677). Alle acht Laeufe und
    die Auswertung melden genau diese Pruefsummen.
- **Rohdaten:** lauf-69/
  - je Lauf JSON, NPZ und Log; auswertung.json mit den mechanischen Urteilen; empfindlichkeit.json (nachtraeglich)
  - Bilder: auswertung-F.png (Paarpotential), auswertung-korr.png (Schalen), ringe.png (Ringform, nachtraeglich),
    auswertung-pinch.png (Strukturfaktor)
  - Rauchlaeufe in rauch-69/ (auswertung.json mit L = 6, auswertung2.json mit L = 10)
- Geschrieben ab 20:01:22 CEST (date); Zahlen nach der Auswertung eingesetzt.
- **Einheiten:** kubische Zellkante = 1. Kantenlaenge beider Netze a = sqrt(2)/4 = 0,354. F in Einheiten von T
  (alle erlaubten Zustaende gleich gewichtet).

## Ergebnis zuerst

1. **Netz A (Pyrochlor-Kanten, Regel 3 rein / 3 raus) ist eine Coulomb-Phase, und zwar quantitativ.**
   - **Paarpotential** zweier Regelverletzungen q = +2 / -2 (L = 12, zwei Seeds, 9,1e9 Stichproben):
     F(r) = a - C r^-p mit p = 0,963 +- 0,070 (Jackknife) und C = 0,105 +- 0,005, also anziehend.
     - Schreibtisch (Gauss-Naeherung, K = 2/3): C = 1/(3 pi) = 0,106.
     - Gauss-Referenz auf demselben Gitter durch dieselbe Routine: p = 0,938, C = 0,108.
   - **Pfeil-Korrelationen:** Der P2-Anteil D(r) faellt wie r^-3,01 (Ringform, 8 von 8 Ringen). RSS 0,005 (Potenz)
     gegen 0,142 (exponentiell).
     - Amplitude 0,0153 (Schalenform) gegen 0,0149 vom Schreibtisch.
     - Monte Carlo und Gauss-Referenz stimmen je Ring auf 1 bis 2 % ueberein.
   - **Strukturfaktor:** S_xx(h,0,l) zeigt die Pinch-Fliege. Entlang h ist S_xx exakt 0 (Flusserhaltung), entlang l
     bei kleinstem k 0,49.
2. **Netz B (K4-Kristall, q = +-1 an jeder Ecke): Die Korrelationen sind sehr kurzreichweitig. F3 ist nach der
   eingefrorenen Regel trotzdem nicht eingetroffen.**
   - Der Schalen-RMS von C faellt von 0,022 (r = 0,92) auf 8e-5 (r = 2,21), also um den Faktor 270 auf 1,3 Zellkanten
     (3,7 Kantenlaengen); ab r ~ 2,4 bleibt Rauschen. Netz A hat bei r = 2,1 noch 7e-4, mit r^-3.
   - **Ringform von R2 auf [0,8; 3,0], 5 signifikante Ringe:**
     - Die beste Potenz (p = 6,3, RSS 0,58) passt besser als die exponentielle Form (RSS 0,94).
     - Die exponentielle Form hat xi = 0,234 Zellkanten = 0,66 Kantenlaengen, also weit unter 3.
     - Verfehlt ist allein die Formbedingung "exponentiell besser als jede Potenz".
   - **Nachtraeglich, nur beschreibend:** Ohne die innerste Schale (0,866) kehrt sich der Formvergleich um.
     - Untergrenze 0,9, 1,0 oder 1,2: exponentiell besser, xi = 0,25 bis 0,27 Zellkanten; beste Potenz p = 5,8 bis 6,7.
     - Das Urteil haengt also an einer Schale. Auf dem kurzen Signalfenster (Faktor ~2,4 in r) trennt die Messung
       Potenz und exponentiell nicht robust.
   - **Kein Pinch-Punkt:** Kennzahl 1,02 bis 1,06 (Netz A: ~1e32).
   - **Ladungen ungeordnet:** gestaffelte Ladung (Summe auf A minus Summe auf B, je Ecke) 2e-5 bzw. -6e-7.
3. **Kontrollen (F0 eingetroffen):**
   - 0 Regelfehler in allen Laeufen, nach jedem angenommenen Zug geprueft: 3,4e10 angenommene Paar-Zuege (ohne
     Einlauf), 8,0e9 Wurm-Umklappungen, 3,3e9 srs-Zuege. Alle Vollpruefungen fehlerfrei.
   - Gitterzahlen und Kennzeichen stimmen; srs: Taillenweite 10, 15 Zehnerringe je Ecke, Quotient K4.
   - Beide Anfaenge in Netz B geben dieselben Mittelwerte. Bei L = 1 ist der Zug-Graph der 450 erlaubten Zustaende
     zusammenhaengend.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang (mechanisch nach PLAN.md, auch in lauf-69/auswertung.json) |
|---|---|---|
| F0 | Kontrolle: Eisregel (Netz A) bzw. q = +-1 (Netz B) nach jedem Zug exakt erhalten; Gitterzahlen (Grad, Kanten) stimmen (95 %) | **eingetroffen**: 8 von 8 Laeufen in Ordnung. Lokale Regelfehler 0, Vollpruefungen (je Block bzw. je Messung) fehlerfrei. Netz A, L = 12: 27 648 Ecken, 82 944 Kanten, Grad 6, 1728 Ketten zu 48 Kanten. Netz B, L = 12: 13 824 Ecken, 20 736 Kanten, Grad 3, zweiteilig, eben mit 120 Grad, Taillenweite 10, K4-Quotient. L = 8 ebenso |
| F1 | Netz A, Paarpotential: anziehend, bester Exponent p in [0,8; 1,2] (Coulomb) (75 %) | **eingetroffen**: L = 12, p = 0,963 (Jackknife +- 0,070), C = 0,105 > 0; 26 Schalen in [1,0; 2,28], chi^2 = 41 bei 23 Freiheitsgraden. Seeds einzeln p = 1,03 und 0,90 |
| F2 | Netz A, Korrelationen: Potenzgesetz mit Exponent in [2,5; 3,5] (dipolar) (65 %) | **eingetroffen**: L = 12, Ringform von D(r) auf [1,0; 3,0], 8 von 8 Ringen signifikant, p = 3,014; RSS 0,0052 (Potenz) gegen 0,142 (exponentiell) |
| F3 | Netz B (K4-Kristall), Korrelationen: abgeschirmt, ein exponentieller Ausgleich ist besser als jeder Potenzansatz, Korrelationslaenge <= 3 Kantenlaengen (60 %) | **nicht eingetroffen**: L = 12, beide Anfaenge, Ringform von R2(r) auf [0,8; 3,0]. 5 von 9 Ringen signifikant (8 belegt). RSS 0,94 (exponentiell, xi = 0,234 Zellkanten = 0,66 a) > 0,58 (Potenz, p = 6,30). Die Bedingung an xi waere erfuellt, die Formbedingung nicht |

- **Ableitbarkeit:**
  - F1 und F2 sind Literatur-Erwartung; die Zahl auf diesem Gitter war neu.
    - Die Gauss-Referenz (eine Rechnung ohne Monte Carlo) sagt C und D auf 1 bis 3 % voraus.
    - Nach dem Rauchlauf Teil 2 (L = 10: p = 3,07 in der Ringform) waren F1 und F2 praktisch ableitbar.
  - F3 war offen. Den Ausgang liess der Rauchlauf Teil 2 schon ahnen (Handrechnung im Plan, Abschnitt 6). Die Regel
    blieb unveraendert.

**Bedeutung (nach Karte):**
- **F1 und F2 treffen ein.** Karte: "Aus Finns Bild entsteht eine Fernkraft genau dann, wenn die Fluss-Regel an jeder
  Ecke exakt aufgeht (gerader Grad, eckverknuepfte Tetraeder)."
  - Der erste Teil ist bestaetigt: Pfeile entlang der Kanten mit "so viel rein wie raus" geben genau das Gitter-Coulomb
    der Gauss-Theorie, dieselbe Physik wie Spin-Eis "durch die Tetraeder" (EIS-1).
  - "Genau dann" ist mit einem Gegenbeispiel (Netz B) nur gestuetzt, nicht bewiesen [H].
- **F3 trifft nicht ein.** Karte, Fall "F3 trifft nicht ein (auch Netz B weitreichend): Frustration allein verhindert
  die Fernwirkung nicht. Beschreiben."
  - **Diese Lesart passt nicht zum Befund.** Netz B ist nach keinem Mass weitreichend:
    - kein Pinch-Punkt (Kennzahl 1,02 bis 1,06)
    - Abfall um den Faktor 270 auf 3,7 Kantenlaengen; bei r = 2,2 Zellkanten 8,5-mal kleiner als Netz A
    - beste Potenz p = 6,3 statt 3
    - Ladungen ungeordnet
  - Gescheitert ist nur die Formbedingung "exponentiell besser als jede Potenz", auf einem Fenster von Faktor ~2,4
    in r. Dieses Fenster bestimmt die Gitterstruktur (Schalen gleichen Abstands haben verschiedene Graphenabstaende,
    z. B. ist die Schale 1,732 staerker korreliert als 1,658). Ohne die innerste Schale kehrt sich der Vergleich um.
  - [H] Das frustrierte Einzeltetraeder, als K4-Kristall fortgesetzt, hat keine Fernwirkung; ob der Abfall streng
    exponentiell ist, bleibt auf diesen Abstaenden offen.
  - [H] Die Kartenaussage "Frustration allein verhindert die Fernwirkung nicht" wird von diesem Lauf **nicht** gestuetzt.
- **[H] Einordnung:** Netz B ist das dreidimensionale Gegenstueck zum Kagome-Eis I.
  - Dort sind die Ladungen +-1 an Ecken vom Grad 3 ungeordnet, und die Korrelationen kurz [S: Chern, Mellado,
    Tchernyshyov, arXiv:0906.4781, Zusammenfassung].
  - Lagen die Ladungen fest im A/B-Muster (+1 auf A, -1 auf B), wuerde die Regel zur Dimerbedeckung des zweiteiligen
    srs-Netzes. Dimere auf zweiteiligen 3D-Gittern bilden eine Coulomb-Phase [S: Huse, Krauth, Moessner, Sondhi,
    cond-mat/0305318].
  - Moeglicher naechster Test [H]: Netz B mit Gewicht fuer gestaffelte Ladung (oder mit festgelegtem A/B-Muster);
    erwartet ein Uebergang von kurzreichweitig zu dipolar.

## Tabellen

**Paarpotential, Netz A** (Ausgleich a - C r^-p, gewichtet):

| L | Bereich | Schalen | p | C | Gauss-Referenz p / C | Berichtet |
|---|---|---|---|---|---|---|
| 12 (gewertet) | [1,0; 2,28] | 26 | 0,963 +- 0,070 | 0,105 +- 0,005 | 0,938 / 0,108 | Seeds 1,03 / 0,90; ab 0,8: p = 1,14 |
| 8 | [1,0; 1,52] | 8 | 0,82 +- 0,22 | 0,118 | 0,58 / 0,158 | enger Bereich, p dort unbestimmt; ab 0,8: p = 1,83 |

**Korrelationen, Ringform** (Ringe 0,25 Zellkanten breit; ln y gegen ln r bzw. gegen r, ungewichtet; xi in Zellkanten,
in Klammern in Kantenlaengen):

| Netz | L | Mass | Ringe signifikant | Potenz p | RSS Potenz | exponentiell xi | RSS exp | besser |
|---|---|---|---|---|---|---|---|---|
| A | 12 | D (Urteil F2) | 8 von 8 | 3,014 | 0,0052 | 0,638 (1,80) | 0,142 | Potenz |
| A | 12 | D, Gauss-Referenz | 8 | 3,045 | 0,0042 | 0,631 (1,78) | 0,129 | Potenz |
| A | 8 | D | 4 von 4 | 3,117 | 0,0018 | 0,479 (1,35) | 0,0114 | Potenz |
| A | 12 | R2 (Mass von F3) | 8 | 3,10 | 0,18 | 0,623 (1,76) | 0,92 | Potenz |
| A | 12 | Cax (Verschiebung auf der Achse) | 6 | 3,31 | 0,0070 | 0,550 (1,56) | 0,102 | Potenz |
| A | 12 | Cbar (reines Schalenmittel, Wortlaut) | 4 | 0,73 | 1,78 | 1,98 (5,6) | 1,59 | exp (Dipolanteil geloescht) |
| B | 12 | R2 (Urteil F3) | 5 von 9 (8 belegt) | 6,30 | 0,58 | 0,234 (0,66) | 0,94 | Potenz |
| B | 8 | R2 | 4 von 5 (4 belegt) | 6,15 | 0,48 | 0,224 (0,63) | 0,79 | Potenz |
| B | 12 | D | 7 | 6,39 | 0,34 | 0,256 (0,72) | 0,68 | Potenz |
| B | 12 | Cbar | 6 | 5,96 | 0,25 | 0,262 (0,74) | 0,062 | exponentiell |

**Ringwerte**, Schalen-RMS sqrt(R2) (L = 12):

| r (Netz B) | 0,92 | 1,41 | 1,68 | 2,00 | 2,21 | 2,45 |
|---|---|---|---|---|---|---|
| Netz B | 0,0221 | 0,00144 | 0,00075 | 0,00018 | 8,1e-5 | 4e-5 (1,3 sigma) |

| r (Netz A) | 1,16 | 1,37 | 1,61 | 1,87 | 2,14 | 2,39 | 2,63 | 2,89 |
|---|---|---|---|---|---|---|---|---|
| Netz A | 0,0052 | 0,0024 | 0,0016 | 0,0011 | 6,9e-4 | 4,6e-4 | 3,7e-4 | 2,9e-4 |

**Empfindlichkeit der Ringform** (nachtraeglich, empfindlichkeit.py, nur beschreibend, L = 12):

| Untergrenze | Breite | B: Ringe sign. | B: p | B: xi | B: besser | A: p | A: besser |
|---|---|---|---|---|---|---|---|
| 0,8 (eingefroren) | 0,25 | 5 | 6,30 | 0,234 | Potenz | 2,83 | Potenz |
| 0,9 | 0,25 | 5 | 6,00 | 0,253 | exponentiell | 2,97 | Potenz |
| 1,0 | 0,25 | 4 | 5,85 | 0,259 | exponentiell | 3,01 (eingefroren) | Potenz |
| 1,2 | 0,25 | 5 | 6,75 | 0,272 | exponentiell | 2,95 | Potenz |
| 0,8 bis 1,2 | 0,5 | 3 | nicht auswertbar | | | 3,01 bis 3,05 | Potenz |

**Laeufe:**

| Lauf | Messungen / Bloecke | tau_int (Messabstaende) | Mittel |
|---|---|---|---|
| korr A L = 12 (20 Wuermer je Messung) | 11 200 / 40 | 0,50 (Fluss), 0,54 (Kettennachbar) | Kettennachbar 0,1624, Fluss 1,48 |
| korr A L = 8 | 36 000 / 40 | 0,50 / 0,52 | 0,1624 / 1,47 |
| korr B L = 12, Anfang kette (2 Durchgaenge je Messung) | 74 000 / 37 | 0,71 / 0,50 / 0,51 | Fluss 1,998, gestaffelte Ladung 2,0e-5, umklappbar 0,44452 |
| korr B L = 12, Anfang reparatur | 74 000 / 37 | 0,73 / 0,50 / 0,53 | 1,997, -5,8e-7, 0,44451 |
| korr B L = 8, kette | 105 000 / 35 | 0,73 / 0,50 / 0,52 | 1,994, 7,7e-5, 0,44452 |
| paar L = 12, Seeds 1 und 2 | 36 + 37 Bloecke zu 5e8 Zuegen | | 3,8e7 Zuege/s, Annahme 2/3 |
| paar L = 8 | 29 Bloecke | | 4,0e7 Zuege/s |

## Kontrollen

- **Regeln exakt (F0):**
  - Netz A, Paar-Sektor: nach jedem angenommenen Zug alte Ecke q = 0 und neue q = +-2 geprueft (2,4e10 angenommene
    Zuege bei L = 12, 9,7e9 bei L = 8), Vollpruefung nach Einlauf und jedem Block: alles fehlerfrei.
  - Netz A, Eis-Sektor: nach jeder Umklappung beide Enden geprueft (8,0e9 Umklappungen), Vollpruefung je Messung
    (47 200): fehlerfrei.
  - Netz B: nach jedem angenommenen Zug beide Enden aus den Pfeilen neu berechnet (3,3e9 Zuege), Vollpruefung je
    Messung (253 000) gegen die mitgefuehrten Ladungen: fehlerfrei.
- **Geometrie srs:**
  - Koordinationsfolge 3, 6, 12, 24, 35, 48, 69, 86, 108, 138 und 15 Zehnerringe je Ecke. Das passt zu den
    RCSR-Kennzahlen des srs-Netzes [L?, aus dem Gedaechtnis, nicht nachgelesen].
  - Quotient nach dem bcc-Gitter ist K4 (je Eckenpaar genau eine Kantenklasse): das "aufgerollte Tetraeder"
    [L?: Sunada 2008].
  - Torus L = 2 hat Taillenweite 8 (Kreise um den Torus), ab L = 3 ist sie 10.
- **Ergodizitaet Netz B:**
  - **L = 1** (Wuerfelgraph, Rauchlauf): 450 von 4096 Belegungen erlaubt; der Zug-Graph ist zusammenhaengend; 4 bis 8
    Zuege je Zustand, alle symmetrisch. MC-Besuche gegen Gleichverteilung: chi^2 = 523 bei 449 Freiheitsgraden
    (Stichproben korreliert).
  - **L = 12, zwei Anfaenge:** Die Mittel stimmen (siehe Tabelle Laeufe).
    - Schalenform je Anfang: R2-Potenz p = 5,64 / 5,61, xi = 0,218 / 0,221; D-Amplitude 0,02593 / 0,02592.
    - Der Anfang "reparatur" musste 3461 verletzte Ecken in 4695 Umklappungen reparieren.
  - **L = 8 gegen 12:** Die Ringwerte von R2 stimmen in den ersten drei Ringen auf 0,3 bis 1,3 % (4,877e-4 gegen
    4,879e-4; 2,071e-6 gegen 2,065e-6; 5,71e-7 gegen 5,64e-7).
- **Autokorrelation:**
  - Netz A: tau_int 0,50 bis 0,54 Messabstaende; je Messung 20 Wuermer, also etwa 4 E Umklappungen.
  - Wuermer bei L = 12: im Mittel 25 800 Versuche (0,93 N) und 17 200 Umklappungen (0,21 E); der laengste hatte 797 095
    Versuche.
  - Netz B: tau_int 0,50 bis 0,73 Messabstaende (2 Durchgaenge).
- **Paar-Sektor:** Annahme 2/3 wie erwartet (4 von 6 Kanten passen). Der +2-Defekt sitzt auf allen vier Untergittern
  gleich oft (Abweichung der Anteile <= 2e-5). Vernichtungsablehnungen 1,4e6 bei L = 12.
- **Gauss-Referenzen:**
  - Die Projektor-Diagonale K = 0,666679 entspricht genau (E - V + 1)/E.
  - Paarpotential bei L = 6 (Rauchlauf): F - F_G ist ab r = 0,61 konstant auf 0,001.
  - D(r) bei L = 12 je Ring: Monte Carlo / Gauss = 0,98 bis 1,02. Kettennachbar 0,1624 (MC) gegen 0,1645 (Gauss).
- **Endlichkeit Netz A:** Kettennachbar-Korrelation 0,1624 bei L = 6, 8, 10 und 12. D-Ringe: p = 3,12 (L = 8) gegen
  3,01 (L = 12).
- **Schalenform** (gewichtete Ausgleiche je Schale, nur berichtet):
  - A, L = 12: p = 3,05, Potenz besser (chi^2 36 007 gegen 44 609).
  - A, L = 8: p = 2,86, aber exponentiell "besser" (39 580 gegen 40 952), ebenso die Gauss-Referenz. Das ist der
    Grund fuer die Ringform.
  - B, L = 12: p = 5,63, Potenz besser (1773 gegen 2425).
- **Strukturfaktor:**
  - Netz A: S_xx bei kleinstem k entlang l 0,494, entlang h 7e-33. Im Eiszustand ist der Fluss durch jede Ebene
    gleich, darum ist S_xx(h,0,0) exakt 0.
  - Netz B: 0,668 gegen 0,642 (kette) bzw. 0,666 gegen 0,652 (reparatur), glatt ohne Fliege (auswertung-pinch.png).

## Latten (v3)

- **L1: ja.** F1, F2 und F3 konnten scheitern; F3 ist gescheitert.
  - F2 wurde vor dem Einfrieren an der Gauss-Referenz geprueft: Die Ringform erkennt ein Coulomb-Feld als Potenz.
  - Die alte Schalenform haette auch ein exaktes Coulomb-Feld verworfen.
- **L2: ja.**
  - Gauss-Referenz als unabhaengige Rechnung ohne Monte Carlo (F1 und F2)
  - zwei Groessen je Netz; zwei Anfaenge in Netz B; Vollaufzaehlung bei L = 1; Pinch-Kennzahl
  - nachtraeglich: Empfindlichkeit der Ringform
- **L3: ja.** Regeln exakt erhalten; tau_int ~ 0,5; Block- und Jackknife-Fehler; L = 8 gegen 12; Seeds gegeneinander.
  - F1: die Seeds liegen 0,12 auseinander (1,03 / 0,90), etwa 1,7 sigma_JK.
- **L4: ja, fuer Netz A; teilweise fuer Netz B.**
  - Coulomb-Phase von Eisregel-Modellen [S: Henley, arXiv:0912.4531, Zusammenfassung].
  - Dipolare Korrelationen [S: Isakov, Gregor, Moessner, Sondhi, cond-mat/0407004, Zusammenfassung].
  - 3D-Dimere auf zweiteiligen Gittern: Coulomb [S: Huse u. a., cond-mat/0305318].
  - Kagome-Eis, Ladungsordnung in zwei Stufen [S: arXiv:0906.4781 und 1109.0275, Zusammenfassungen].
  - K4-Kristall [L?: Sunada, Notices AMS 2008, nicht nachgelesen].
  - Das 3-rein-3-raus-Modell auf Pyrochlor-Kanten und das q = +-1-Modell auf dem srs-Netz habe ich nicht gezielt
    gesucht (5 arXiv-Anfragen).
- **L5: nein.** Analogien [H]: Spin-Eis-Materialien mit Pinch-Punkten in der Neutronenstreuung [L?]; kuenstliches
  Kagome-Eis als 2D-Gegenstueck von Netz B. Kein Messbezug fuer Finns Bild.

## Selbstanzeigen

1. **Rauchlauf vor dem Plantext gelesen, Urteilsform danach geaendert.**
   - Die Ausgaben von Teil 1 (L = 6) habe ich vor dem Schreiben des Plans gelesen.
   - Danach habe ich die Urteilsform fuer F2 und F3 von der Schalenform zur Ringform geaendert und die Untergrenze fuer
     Netz B auf 0,8 gesetzt.
   - Offen gelegt im Plan, Abschnitt 6, vor dem Einfrieren; Grund war die Gitterstreuung, die auch die exakte
     Gauss-Referenz zeigte.
2. **Der F3-Ausgang war absehbar; die Regel blieb.**
   - Rauchlauf Teil 2 (L = 10) und meine Handrechnung im Plan zeigten, dass die Potenzform gewinnen duerfte.
   - Ich habe die Regel danach nicht geaendert.
   - Die nachtraegliche Empfindlichkeitsrechnung zeigt: Schon das Weglassen der innersten Schale kehrt das Urteil um.
     Sie aendert das Urteil nicht.
3. **Nach den Laeufen geschrieben, nicht eingefroren:** bild_ringe.py (Bild) und empfindlichkeit.py (andere
   Untergrenzen und Breiten). Beide nur beschreibend, auf cpu3 nach der Auswertung gelaufen.
4. **Abweichung vom Wortlaut des Auftrags:** Das Hauptmass ist nicht das reine Schalenmittel <s_e s_e'>(r).
   - Gewertet sind D(r) (P2-Anteil, Netz A) und R2(r) (Schalen-RMS, Netz B).
   - Grund: Das Schalenmittel loescht den Dipolanteil (Schreibtisch, Plan Abschnitt 3).
   - Berichtet ist es trotzdem: Netz A p = 0,73, exponentiell "besser", also unbrauchbar. Netz B: exponentiell besser
     (xi = 0,26 Zellkanten).
5. **Untergrenzen verschieden** (A 1,0, B 0,8), aus der Zahl signifikanter Schalen im Rauchlauf Teil 1. Die Untergrenze
   0,8 bezieht die innerste Schale von Netz B ein, an der das F3-Urteil haengt.
6. **Vollaufzaehlung und Kleingeometrie nur im Rauchlauf.** Die Vollaufzaehlung L = 1 und die Geometrie fuer L = 1 bis 6
   liefen im Rauchlauf (pruef), nicht in den echten Laeufen. Die echten Laeufe pruefen ihre eigene Geometrie
   (L = 8 und 12).
7. **Pinch-Kennzahl von Netz A ist kein unabhaengiger Beleg.** ~1e32 folgt aus der Regel selbst (Fluss durch jede
   Ebene gleich). Belegend sind die Fliegenform bei l != 0 und das r^-3.
8. **F1 bei L = 8 ist unbestimmt** (8 Schalen in [1,0; 1,52]: p = 0,82 +- 0,22, Gauss-Referenz 0,58). Gewertet ist
   nur L = 12.
9. **Literatur und Koordinaten:**
   - Nur arXiv-Zusammenfassungen (5 Anfragen, je >= 3 s Abstand) [S] bzw. Gedaechtnis [L?], z. B. Sunada 2008 und
     die RCSR-Kennzahlen.
   - Die srs-Koordinaten habe ich durch Pruefung bestaetigt (Grad, Abstand, Taillenweite, K4-Quotient,
     Koordinationsfolge), nicht an einer Quelle nachgelesen.
10. **Uhrzeiten:** Die Laufzeiten stammen aus den .69-Logs (UTC); die Zeiten in CEST sind umgerechnet.

## Einfach gesagt

Wir haben Finns Bild nachgerechnet: Auf jeder Kante eines grossen Netzes liegt ein Pfeil, und an jeder Ecke soll so
viel hinein- wie hinausfliessen. Geht das an jeder Ecke genau auf (eckverknuepfte Tetraeder, sechs Kanten je Ecke),
entstehen echte Fernkraefte: Zwei Fehlstellen ziehen sich wie elektrische Ladungen mit etwa 1/r an, und die Pfeile
spueren einander noch weit weg wie kleine Magnete (1/r^3). Setzt man dagegen das einzelne Tetraeder selbst als Kristall
fort, geht die Regel an keiner Ecke auf: Jede Ecke ist ein kleiner Plus- oder Minuspol, und die Pfeile vergessen
einander schon nach zwei bis drei Kantenlaengen. Ob dieses Vergessen genau "exponentiell" verlaeuft, liess sich auf
dem kurzen messbaren Stueck nicht sauber entscheiden. Darum gilt die dritte Vorhersage formal als nicht eingetroffen,
obwohl es dort keine Fernwirkung gibt.
