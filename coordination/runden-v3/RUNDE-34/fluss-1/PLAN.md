# FLUSS-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 34)

- Geschrieben ab 2026-10-03 19:45:01 CEST (date). Karte: KARTE.md (unveraendert); Vorhersagen F0 bis F3 und ihre
  Bedeutung stehen dort fest und sind in Abschnitt 5 woertlich uebernommen.
- **Reihenfolge offen gelegt:** Code geschrieben ab 19:20 CEST. Rauchlaeufe Teil 1 (Gittergroessen 1, 2, 3, 4, 6; keine
  echte) gestartet 17:34:22 UTC, Ausgaben gelesen ab 19:36 CEST, also **vor** diesem Text. Daraufhin habe ich die
  Urteilsform fuer F2 und F3 geaendert (Ringform, Abschnitt 6). Rauchlauf Teil 2 (Groesse 10, keine echte) laeuft
  seit 17:44:33 UTC; Abschnitt 6 ergaenze ich nach seinem Lesen, vor dem Einfrieren.
- Code (code/): gitter.py (aus EIS-1, unveraendert, sha256 9f6b4b1c...), gitter_fluss.py (Netze A und B),
  fluss_kern.c (Monte-Carlo-Kerne, C, in der Spur mit gcc -O2 uebersetzt), fluss_mc.py (Laeufe), auswertung.py
  (Urteile), rauch.sh, rauch2.sh, laeufe.sh.
- Einheiten: kubische Zellkante = 1, Koordinaten intern in 1/8. Kantenlaenge beider Netze a = sqrt(2)/4 = 0,3536.

## 1. Modell

- Jede Kante e traegt einen Pfeil. Je Richtungsklasse c (sechs Klassen <110>: [110], [1-10], [101], [10-1], [011],
  [01-1]) gilt eine feste Bezugsrichtung +n_c; s_e = +1, wenn der Pfeil entlang +n_c zeigt, sonst -1.
  Ladung q_v = (rein - raus).
- **Netz A, Pyrochlor-Kanten:** 16 L^3 Ecken, 48 L^3 Kanten (Tetraederkanten), Grad 6, Kanten der Laenge a.
  - [M] Jede Kante liegt auf einer geraden Kette entlang ihrer Klasse; eine Kette schliesst sich auf dem Torus nach
    4 L Kanten, es gibt 12 L^2 Ketten. Eine je Kette einheitliche Pfeilrichtung ist ein Eiszustand (q = 0 ueberall).
  - Eisregel: q = 0 (3 rein, 3 raus). Defekte: q = +2 (4 rein, 2 raus) und q = -2.
- **Netz B, srs-Netz (K4-Kristall):** 8 L^3 Ecken (Lagen (1/8,1/8,1/8), (5/8,3/8,7/8), (3/8,7/8,5/8), (7/8,5/8,3/8)
  und um (1/2,1/2,1/2) verschoben), Nachbarn im Abstand a, 12 L^3 Kanten, Grad 3.
  - Regel: q in {+1, -1} an jeder Ecke (2 rein 1 raus oder umgekehrt); verboten sind 3 rein bzw. 3 raus.
  - Gepruefte Kennzeichen (gitter_fluss.py, in jedem Lauf): Grad 3; zweiteilig (A-B); je Ecke drei Kantenvektoren
    in einer Ebene mit 120 Grad; Quotient nach dem bcc-Gitter ist K4 (4 Ecken, je Paar genau eine Kantenklasse);
    Taillenweite 10 (BFS von allen 8 Basisecken, Tiefe 10); Koordinationsfolge und Zahl der 10-Ringe je Ecke
    berichtet.
- **Geometriepruefung (F0):** Ecken, Kanten, Grad, Kantenlaenge, Kanten je Klasse, Ketten (A), Kennzeichen (B).

## 2. Abtastung

- **Netz A, Paar-Sektor (F1):** wie EIS-1, Teil 1, auf Ecken statt Tetraedern.
  - Anfang: Eiszustand mit zufaelliger Kettenrichtung; eine zufaellige Kante umklappen ergibt +2 und -2.
  - Zug: Defekt mit W. 1/2, Platz (eine der 6 Kanten) mit W. 1/6. Der +2-Defekt springt nur ueber einen
    hineinzeigenden Pfeil, der -2-Defekt nur ueber einen hinauszeigenden; Umklappen; der Defekt sitzt danach an der
    anderen Ecke. Waere dort der Gegendefekt (Vernichtung), Ablehnung.
  - Vorschlag symmetrisch, Ablehnung = Bleiben: Gleichverteilung ueber alle Zustaende mit genau diesen zwei Defekten.
  - Lokale Pruefung nach jedem angenommenen Zug (alte Ecke q = 0, neue q = +-2), Vollpruefung nach jedem Block.
- **Netz A, Eis-Sektor (F2):** geschlossene Wuermer.
  - Je Wurm: eine Kante gleichverteilt umklappen; der +2-Defekt waehlt je Schritt einen seiner 6 Plaetze
    gleichverteilt und springt nur ueber hineinzeigende Pfeile, bis er den -2-Defekt erreicht.
  - Erweiterter Zustandsraum: Eiszustaende Gewicht 1, Zwei-Defekt-Zustaende Gewicht 6/E (detailliertes
    Gleichgewicht: Erzeugung 1/E, Vernichtung 1/6; Wanderung symmetrisch). Jeder Besuch eines Eiszustands dauert
    genau einen Schritt; die Folge der Eiszustaende nach jedem Wurm ist darum gleichverteilt (induzierte Kette).
  - Messung nach jeweils fest 20 Wuermern (fester Abstand, kein vom Verlauf abhaengiger Haltepunkt).
  - Wuermer koennen sich um den Torus winden und wechseln so den Flusssektor; alle Sektoren werden abgetastet.
- **Netz B (F3):** Einzelkanten-Zuege.
  - Vorschlag: Kante gleichverteilt. Pfeil a -> b darf umklappen, wenn danach beide Enden in {+1, -1} liegen, also
    genau dann, wenn q_a = -1 und q_b = +1 (danach vertauscht). Gleichverteilung ueber alle erlaubten Zustaende.
  - Lokale Pruefung nach jedem angenommenen Zug (beide Enden aus den Pfeilen neu berechnet), Vollpruefung je Messung.
  - Anfaenge: "kette" (Klassen [011] und [01-1] bilden eine perfekte Paarung; der Rest zerfaellt in Kreise, die je
    einheitlich durchlaufen werden; Paarungskanten zufaellig) und "reparatur" (zufaellige Pfeile, Ecken mit
    |q| = 3 durch Umklappen repariert).
  - Ergodizitaet: (i) L = 1: alle 2^12 Belegungen aufgezaehlt, Zug-Graph der erlaubten Zustaende zusammenhaengend?
    Besuchshaeufigkeiten eines MC-Laufs gegen Gleichverteilung (chi^2). (ii) L = 12: zwei Laeufe mit verschiedenen
    Anfaengen, Mittelwerte (Fluss, gestaffelte Ladung, Anteil umklappbarer Kanten) und Korrelationen gleich?
    (iii) integrierte Autokorrelationszeiten je Lauf.
- Zufall xoshiro256** im C-Kern; Seeds je Lauf verschieden.

## 3. Messgroessen

- **F1, Paarpotential (Netz A):** P(r) = Anteil der Stichproben mit Defektabstand r (Minimalbild, exakte Schalen
  r^2 in 1/64). g(r) = Zahl der geordneten Eckenpaare im Abstand r. F(r) = -ln[P(r)/g(r)], Fehler aus der Streuung
  der Blockwerte.
  - Ausgleich F = a - C r^(-p), Gewichte 1/sigma^2, p auf festem Gitter [0,05; 6] (Schritt 0,001), a und C linear.
  - **Bereich: 1,0 <= r <= 0,19 L** (L = 12: [1,0; 2,28]; L = 8: [1,0; 1,52]). Obergrenze wie EIS-1 (Torus-Korrektur
    r^2/(6 L^3): oertlicher Exponent bei 0,19 L etwa 1,09). Untergrenze 1,0 = knapp 3 Kantenlaengen.
  - Jackknife ueber 10 Blockgruppen (nur berichtet). Gauss-Referenz (nur berichtet): F_G = 4 K [G(0) - G(r)] mit
    K = (E - V + 1)/E ~ 2/3 und G = Pseudo-Inverse des Ecken-Laplace auf demselben Torus, durch dieselbe Routine.
- **F2, F3, Pfeil-Korrelationen:** je Klasse c ein Gitter der Kantenmitten (Netz A Abstand 1/4, Netz B 1/2 Zellkante);
  je Messung FFT, Summe von |F|^2 je Block; am Blockende C_c(Delta) = <s_e s_e'> fuer alle Verschiebungen Delta
  (Minimalbild), geteilt durch die Paarzahl m_c(Delta). Schalen nach |Delta|^2.
  - **Schreibtisch [M]:** Eine dipolare Korrelation <s_e s_e'> ~ (3 cos^2 theta - 1)/r^3 (theta = Winkel zwischen
    Klassenrichtung und Verbindung) mittelt sich ueber eine Kugelschale zu null. Der reine Schalenmittelwert
    Cbar(r) (Wortlaut des Auftrags) loescht also gerade das gesuchte Signal; er wird nur berichtet.
  - **D(r)**, Hauptmass fuer F2: Amplitude des P2-Anteils, D = Summe(m C P2)/Summe(m P2^2) ueber die Schale (alle
    Klassen), P2 = (3 cos^2 theta - 1)/2. Fuer eine reine Dipolform ist D(r) der Wert auf der Achse; ein konstanter
    Torus-Versatz (Nullmode) faellt weitgehend heraus. Fehler aus den Bloecken.
  - **R2(r)**, Hauptmass fuer F3: unverzerrter Schalenmittelwert von C(Delta)^2 (Kreuzprodukte verschiedener Bloecke,
    paargewichtet, alle Klassen), Jackknife ueber Bloecke. Vorzeichen- und winkelunabhaengig; fuer eine Dipolform
    ~ r^-6, fuer Abschirmung ~ exp(-2 r/xi). Die Korrelationslaenge xi ist die von C selbst.
  - Nur berichtet: Cbar(r), Cax(r) (Verschiebung entlang der Klassenachse), Csenk(r), R2 ohne Schalenmittel (l >= 1),
    die Schalenform (gewichtete Ausgleiche je Schale, Abschnitt 6) und dieselben Masse fuer das jeweils andere Netz.
  - **Gauss-Referenz fuer D(r) in Netz A** (nur berichtet): <b_e b_e'> = -(x[kopf'] - x[schwanz'])/K mit
    x = Lap^+ (e_kopf - e_schwanz), K = Diagonale des Projektors auf divergenzfreie Felder; je Klasse zwei
    Bezugskanten (beide Tetraederarten); gleiche Schalen und Ringe.
- **Ringform (Urteilsform fuer F2 und F3, nach dem Rauchlauf, Abschnitt 6):**
  - Ringe der Breite 0,25 Zellkanten, Netz A von 1,0 bis L/4, Netz B von 0,8 bis L/4 (L = 12: A 8 Ringe [1,0; 3,0],
    B 9 Ringe [0,8; 3,0]; L = 8: A 4 Ringe, B 5 Ringe).
  - Je Ring: D = Summe der Zaehler / Summe der Nenner aller Schalen im Ring (je Block, dann Mittel und Fehler);
    R2 = paargewichtetes Mittel der Schalen (Jackknife-Fehler gleich gebildet). Ringradius = gewichtetes Mittel.
    Mehrere Laeufe gleicher Groesse: Mittel der Laeufe, Fehler quadratisch.
  - Verwendet werden Ringe mit Wert > 2 sigma. Mindestens 4, sonst "nicht auswertbar".
  - Ausgleich ungewichtet in Logarithmen: Potenz = Gerade ln y gegen ln r, exponentiell = Gerade ln y gegen r.
    Vergleich der Restquadratsummen (RSS); beide Ansaetze haben zwei freie Groessen. Fuer R2 gilt p = -Steigung/2 und
    xi = 2/(-Steigung).
- **Strukturfaktor-Schnitt** (nur berichtet): S_aa(k) = <|B_a(k)|^2>/E fuer B = sum_e s_e n_e e^{-i k r_e}, Ebene
  k_y = 0. Pinch-Kennzahl: S_xx bei kleinstem k entlang z geteilt durch S_xx bei kleinstem k entlang x (Coulomb:
  sehr gross, Abschirmung: nahe 1).

## 4. Laeufe (echt)

| Lauf | Netz | L | Zweck | Spur |
|---|---|---|---|---|
| paar_L12_s1, paar_L12_s2 | A | 12 | F1 (gewertet, beide Seeds zusammen) | cpu3 |
| paar_L8_s1 | A | 8 | Endlichkeit F1 (berichtet) | cpu3 |
| korr_A_L12_s1 | A | 12 | F2 (gewertet) | cpu4 |
| korr_A_L8_s1 | A | 8 | Endlichkeit F2 (berichtet) | cpu4 |
| korr_B_L12_s1 (Anfang kette), korr_B_L12_s2 (Anfang reparatur) | B | 12 | F3 (gewertet, beide zusammen); Ergodizitaet | cpu4 bzw. cpu3 |
| korr_B_L8_s1 (kette) | B | 8 | Endlichkeit F3 (berichtet) | cpu4 |
| pruef | B, A | 1 bis 6 | Geometrie, L = 1 Vollaufzaehlung (aus dem Rauchlauf, keine echte Groesse) | - |
| auswertung | alle | | Urteile, lauf-69/auswertung.json, Bilder | cpu3 |

- Laufparameter (nach den Geschwindigkeiten im Rauchlauf, Abschnitt 6):
  - paar: Einlauf 2e9 Schritte, Bloecke zu 5e8 Schritten, Stichprobe alle 4 Schritte, interne Zeitgrenze 540 s
    (L = 12) bzw. 420 s (L = 8).
  - korr A: Einlauf 20 000 Wuermer, Messung alle 20 Wuermer; L = 12: 280 Messungen je Block, Zeitgrenze 540 s;
    L = 8: 900 je Block, 480 s. Hoechstens 40 Bloecke.
  - korr B: Einlauf 2000 Durchgaenge, Messung alle 2 Durchgaenge (je E Vorschlaege); L = 12: 2000 Messungen je Block,
    480 s; L = 8: 3000 je Block, 300 s. Hoechstens 40 Bloecke.
- Spuren cpu3 und cpu4, je Spur nacheinander, nie mehr als zwei zugleich. Startskript code/laeufe.sh.
- Bricht die Spur einen Lauf ab (rc != 0), wird er offen gelegt und nicht gewertet. Fehlt ein gewerteter Lauf, ist das
  Urteil "nicht auswertbar".

## 5. Urteile (mechanisch, auswertung.py)

Woertlich aus der Karte:

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| F0 | Kontrolle: Eisregel (Netz A) bzw. q = +-1 (Netz B) nach jedem Zug exakt erhalten; Gitterzahlen (Grad, Kanten) stimmen | 95 % |
| F1 | Netz A, Paarpotential: anziehend, bester Exponent p in [0,8; 1,2] (Coulomb) | 75 % |
| F2 | Netz A, Korrelationen: Potenzgesetz mit Exponent in [2,5; 3,5] (dipolar) | 65 % |
| F3 | Netz B (K4-Kristall), Korrelationen: abgeschirmt, ein exponentieller Ausgleich ist besser als jeder Potenzansatz, Korrelationslaenge <= 3 Kantenlaengen | 60 % |

**Bedeutung (vorab, aus der Karte):**
- F1 bis F3 treffen ein: Aus Finns Bild entsteht eine Fernkraft genau dann, wenn die Fluss-Regel an jeder Ecke exakt
  aufgeht (gerader Grad, eckverknuepfte Tetraeder). Das frustrierte Einzeltetraeder, fortgesetzt als K4-Kristall,
  schirmt ab [H].
- F3 trifft nicht ein (auch Netz B weitreichend): Frustration allein verhindert die Fernwirkung nicht. Beschreiben.
- F1 trifft nicht ein: Werkzeug pruefen (gegen EIS-1, Teil 1), dann deuten.

Regeln:
- **F0:** eingetroffen genau dann, wenn in allen echten Laeufen gilt: Gitterpruefung "alles_ok" (Netz A: Ecken,
  Kanten, Grad 6, Kantenlaenge, Klassen, Ketten; Netz B: dazu zweiteilig, eben 120 Grad, K4-Quotient,
  Taillenweite 10), lokale Regel-Fehler = 0, alle Vollpruefungen in Ordnung, Anfangszustand regelgerecht.
- **F1:** eingetroffen genau dann, wenn bei L = 12 (beide Seeds zusammen) C > 0 und das beste p in [0,8; 1,2] liegt.
- **F2:** eingetroffen genau dann, wenn bei L = 12 in der Ringform von D(r) auf [1,0; 3,0] mindestens 4 Ringe
  signifikant sind, RSS(Potenz) <= RSS(exponentiell) und p in [2,5; 3,5] liegt.
- **F3:** eingetroffen genau dann, wenn bei L = 12 (beide Anfaenge zusammen) in der Ringform von R2(r) auf [0,8; 3,0]
  mindestens 4 Ringe signifikant sind, RSS(exponentiell) < RSS(Potenz) (beste Potenz, p frei) und
  0 < xi <= 3 a = 1,0607 Zellkanten.
- Weniger als 4 signifikante Ringe: "nicht auswertbar". L = 8, die Schalenform und alle Gegenproben werden berichtet
  und aendern kein Urteil. Deutungen in ERGEBNIS.md als [H].

## 6. Schreibtisch und Rauchlaeufe

- **Schreibtisch (vor jeder Rechnung, [M] bzw. [H]):**
  - Gauss-Naeherung Netz A: Fluss +-1 je Kante, divergenzfreier Anteil (E - V)/E = 2/3 der Freiheitsgrade, also
    Steifigkeit K = 2/3. Leitfaehigkeit des Ecken-Laplace im Kontinuum sigma = 2 (affines Potential ist exakt
    stromfrei, da die Nachbarn in +-Paaren liegen). Damit F(r) ~ a - 4K/(4 pi sigma r) = a - 0,106/r und
    D(r) ~ 2 a^2/(4 pi sigma K r^3) = 0,0149/r^3 [H fuer die Vorfaktoren].
  - Netz B [H]: Bethe-Naeherung je Ecke <in/out-Paar> = -1/3, Faktor ~1/3 je Kantenschritt; erwartet xi ~ 0,5 a.
  - Netz B [H, L?]: Liegen die Ladungen fest im A/B-Muster (+1 auf A, -1 auf B), wird die Regel zur Dimerbedeckung des
    zweiteiligen srs-Netzes, also selbst eine Coulomb-Phase (vgl. Kagome-Eis II gegen I, Huse u. a. 2003 fuer
    3D-Dimere). Abschirmung erwartet nur, solange die Ladungen ungeordnet sind; die gestaffelte Ladung wird
    mitgemessen.
- **Rauchlauf Teil 1** (rauch-69/, gestartet 17:34:22 UTC, Groessen 1 bis 4 und 6, keine echte):
  - pruef: Netz A L = 1, 2, 3, 4, 6 alles_ok. Netz B alles_ok; Taillenweite 10 ab L = 3 (L = 2: 8, Kreise um den
    Torus), 15 Zehnerringe je Ecke, Koordinationsfolge bei L = 6: 3, 6, 12, 24, 35, 48, 69, 86, 108, 138.
  - Netz B, L = 1 (Wuerfelgraph): 450 von 4096 Belegungen erlaubt, Zug-Graph zusammenhaengend (eine Komponente mit 450),
    Zuege symmetrisch, 4 bis 8 Zuege je Zustand; MC 200 000 Stichproben: chi^2 = 523 bei 449 Freiheitsgraden
    (Stichproben korreliert), lokale Fehler 0.
  - paar L = 6: 4,2e7 Schritte/s, Annahme 2/3, Untergitter des +2-Defekts gleich verteilt, Fehler 0.
  - korr A L = 6: 82 000 Wuermer, im Mittel 3280 Versuche (0,95 N) und 0,21 E Umklappungen je Wurm; FFT 2,7 ms je
    Messung; tau_int (Fluss, Kettennachbar) 0,5 Messabstaende; Fehler 0. Pinch-Kennzahl ~1e32 (S_xx entlang x
    exakt 0).
  - korr B L = 6, beide Anfaenge: Annahme 0,445; tau_int 0,5 bis 0,7 Messabstaende (2 Durchgaenge); Mittel von Fluss
    (1,98 gegen 2,01), gestaffelter Ladung (2,6e-4 gegen 2,5e-4) und Umklappanteil (0,4445 gegen 0,4445) gleich;
    Fehler 0. Pinch-Kennzahl 1,10 bzw. 1,13.
- **Gesehen und daraufhin geaendert (vor dem Einfrieren):**
  1. **Schalenform taugt nicht als Urteilsform.** Bei L = 6 streut D(r) von Schale zu Schale um bis zu einen Faktor 2
     (r = 1,0: 0,0086; r = 1,061: 0,0163), und die exakte Gauss-Referenz zeigt dieselbe Streuung (0,0087; 0,0164).
     Das ist Gitterstruktur, kein Rauschen. Die gewichteten Ausgleiche je Schale werden davon beherrscht: Die
     Gauss-Referenz selbst (reines Coulomb) ergab p = 2,94, aber chi^2(exponentiell) < chi^2(Potenz). Die alte Regel
     haette F2 also auch fuer ein exaktes Coulomb-Feld verworfen. Neu: Ringform (Abschnitt 3), ungewichtet in
     Logarithmen. Die Schalenform bleibt nur berichtet.
  2. **Untergrenze Netz B 0,8 statt 1,0.** In Netz B liegen die gleichklassigen Kanten auf einem bcc-Gitter; die
     naechste Schale ist 0,866 (2,45 a), darunter gibt es keine. Bei L = 6 fiel C von 0,028 (0,866) auf 0,0015
     (1,414); ab r ~ 2 war nur Rauschen. Mit Untergrenze 1,0 blieben bei L = 12 voraussichtlich nur 3 bis 4
     signifikante Ringe. Netz A bleibt bei 1,0 (Gitterkern, vgl. EIS-1).
  3. Die Mindestzahl signifikanter Stuetzstellen gilt jetzt je Ring (> 2 sigma, mindestens 4).
- **Rauchlauf Teil 2** (Groesse 10, keine echte; gestartet 17:44:33 UTC mit der Ringform, gelesen ab 19:46 CEST,
  Auswertung rauch-69/auswertung2.json mit L_haupt = 10):
  - Netz A, Ringform von D(r) auf [1,0; 2,5]: 6 von 6 Ringen signifikant, p = 3,07, RSS 0,0033 (Potenz) gegen 0,051
    (exponentiell). Die Gauss-Referenz in derselben Ringform: p = 3,08, RSS 0,0035 gegen 0,047. Monte Carlo und
    Gauss-Referenz stimmen je Ring auf 1 bis 2 % ueberein. Die Ringform erkennt also ein Coulomb-Feld als Potenzgesetz.
  - Netz B, Ringform von R2(r) auf [0,8; 2,5], 19 500 Messungen: nur 3 Ringe signifikant (0,92: 4,9e-4; 1,41: 2,2e-6;
    1,68: 6,0e-7), der Ring bei 2,21 liegt bei 1,8 sigma (1,1e-8). Bei L = 6 also "nicht auswertbar".
  - **Offen gelegt (von Hand aus diesen Rauchzahlen, nicht gerechnet):** Naehme man den Ring bei 2,21 hinzu, gaebe die
    Ringform RSS 0,35 (Potenz, p ~ 6) gegen 1,19 (exponentiell); F3 waere dann nicht eingetroffen. Die oertliche
    Abfallrate von ln C schwankt von Ring zu Ring (5,5 / 2,5 / 3,8 je Zellkante), Gitterstruktur auch hier.
  - **Keine weitere Regelaenderung danach.** Untergrenze 0,8 fuer Netz B war vor dem Lesen von Teil 2 festgelegt (aus
    Teil 1, wegen der Zahl signifikanter Ringe). Die Regel bleibt, wie sie ist; ich aendere sie nicht nach diesem
    Ausgang. Bei L = 12 erwarte ich (Statistik etwa 2,5- bis 3,5-mal besser, zwei Laeufe) 4 bis 5 signifikante Ringe.
  - Netz A, Paarpotential L = 6: F(r) - F_G(r) ist ab r = 0,61 konstant auf 0,001 (nur die naechste Schale weicht um
    0,004 ab). Untergrenze 1,0 bleibt.
  - Geschwindigkeiten fuer die Laufparameter: korr A L = 10: MC 37 s, FFT 48 s fuer 5850 Messungen; korr B L = 10:
    MC 14 s, FFT und Beobachtung 38 s fuer 19 500 Messungen.

## 7. Einfrieren

- PLAN.md.eingefroren-<Zeit> und code/*.eingefroren-<Zeit> (schreibgeschuetzt), vor dem ersten echten Lauf. Die
  Laeufe schreiben die sha256 von Kern und Skripten in jede Ausgabe.
