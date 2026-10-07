# R5-C: 1D mehrere Baelle und Hintergrund, Laufplan

Bearbeiter: Agent R5-C (Anthropic, Opus), Auftrag ../AUFTRAG-R5.md, dazu zwei Nachrichten der Leitung (01:56 W21/W22;
ca. 02:00 Fable-Review zum Hintergrund). Beginn 2026-09-30 01:43:50 CEST (gemessen), Ende in der letzten Zeile.
Status: **v2** (Abschnitt "Versionen"). v1 lief bei der Leitung; bragg und anderson brachen in der Auswertung ab. v2
behebt das und ist wie v1 ungetestet. Explorativ.

## Versionen

- **v1**, abgegeben 2026-09-30 02:32:25 CEST.
- **v2**, 2026-09-30 02:44 CEST (gemessen), nach der Fehlermeldung der Leitung von 02:42.
  - **Fehler:**
    - `integral()` (Trapezregel ueber die Zeit) kannte nur 1D- und 2D-Felder.
    - `transmission_auswerten()` uebergibt die Flussreihen als (Zeit, Lauf, Ebene). Das Zeitgewicht dt (Laenge 1400)
      wurde deshalb gegen die letzte Achse (Ebene, Laenge 2) gelegt: RuntimeError.
    - Die Lauf- und Seed-Achse lag richtig. Falsch war nur, wo dt eingefuegt wurde.
  - **Behebung:** dt wird zu (Zeit, 1, 1, ...) geformt, passend zu jeder Zahl weiterer Achsen. Sonst aendert sich keine
    Rechnung.
  - **Betroffen sind nur bragg und anderson**, die einzigen Nutzer von `integral`. Beide rechnen beide Stufen voll durch
    und brechen erst danach in der Auswertung ab.
    - anderson nutzt dieselbe Auswertung. Der laufende v1-Lauf endet nach der vollen Rechenzeit mit rc 1, ohne
      Ergebnis und ohne Zeitreihen: v1 speichert bei einem Auswertungsfehler nichts, und die Rechnung steckt nur im
      Speicher des Prozesses. Das Ergebnis ist verloren; der Lauf muss mit v2 neu gerechnet werden.
    - Im GPU-Rauchtest fehlen dieselben zwei Auswertungen. Die Stufenzeiten stehen aber im Log (Zeilen
      "bragg grob/fein ..." und "anderson grob/fein ...") und taugen fuer die Hochrechnung (mal 20).
  - **Nicht betroffen:** osmose, massenwirkung, pendeln, ir, quorum, lawinen, symbiose, hintergrund. Ihr Rechen- und
    Auswertecode ist in v2 unveraendert; die v1-Ergebnisse gelten.
  - **Neu, damit eine Auswertungspanne keine Rechenzeit mehr kostet:**
    - Die Rohdaten jeder Stufe werden sofort in `r5c_roh_zwischen.pt` geschrieben. Am Ende stehen sie in
      `r5c_zeitreihen.pt`, auch wenn die Auswertung scheitert.
    - `--roh DATEI` wertet solche Rohdaten nur neu aus, ohne Zeitentwicklung. Dafuer gleicher Unterbefehl und gleiche
      Optionen wie der Lauf, also auch derselbe Laufzeitfaktor und `--seeds`.
    - `r5c_zeitreihen.pt` hat jetzt ein einheitliches Format: {Unterbefehl: {Stufenname: {grob, fein}}}.
    - Kopfzeile und JSON nennen die Version.
  - **Ungetestet** wie v1. Der Teil der Auswertung nach dem Integral (T, R, Minima, <ln T>, Berichtszeilen) ist noch
    nie gelaufen. Deshalb zuerst der kurze Rauchtest unten.
  - **Bestaetigt von der Leitung (Kette 3):**
    - anderson brach an derselben Stelle ab ("4400" statt "1400" = Zahl der Zeitschritte der Messreihe).
    - rauch-gpu endete ebenfalls mit rc 1; das erklaeren die zwei gleichen Auswertungen.
    - Im Bericht rauch-gpu sollte "Fehler in: ['anderson', 'bragg']" stehen. Steht dort mehr, bitte melden.
  - **Kein lokaler Probelauf.** Die Freigabe kam nur weitergeleitet in einer Nachricht der Leitung. CLAUDE.md verbietet
    lokale Interpreterstarts, und eine weitergeleitete Freigabe ersetzt Finns eigene Zustimmung nicht.
    - Statt eines Laufs sind die v2-Stellen statisch geprueft: Formen im Integral und im ganzen Auswerteweg von bragg und
      anderson, Aufrufe, neue Optionen.
    - Der erste Schritt auf der .69 ist deshalb der Rauchtest von bragg und anderson (Zeile 1 unten, etwa 1 min).
  - **Geaenderte Zeilen (v2):**
    - 33: Aufrufzeile
    - 45: VERSION
    - 281-283: ROH, VORRAT, ZWISCHEN
    - 286-306: stufen, Rohdaten-Sicherung und --roh
    - 309-327: roh_laden (neu)
    - 338-342: integral (die eigentliche Behebung)
    - 1223-1229: Option --roh
    - 1250-1271: Kopfzeile, JSON-Version, Rohdaten je Unterbefehl, Hinweis bei Fehler
    - Physik, Laeufe und Auswertungen der Karten sind unveraendert.

**Nachlauf mit v2** (r5c.py v2 in den Remote-Ordner kopieren, ersetzt v1):

```
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5c-rauch-v2 r5c.py rauch --nur bragg,anderson --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5c/rauch-v2
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5c-bragg-v2 r5c.py bragg --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5c/bragg-v2
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5c-and-v2 r5c.py anderson --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5c/anderson-v2
```

- Zeile 2 und 3 nur nach rc = 0 von Zeile 1 (etwa 1 min).
- Rechnet Zeile 1 anderson auf mehr als 9 min hoch, Zeile 3 mit `--seeds 2` starten.
- p4000b geht ebenso (Spur tauschen), solange WM-1-MB ruht.
- Scheitert eine Auswertung trotzdem, sind die Rohdaten gesichert. Neu auswerten ohne Rechnung, in Sekunden, auf der
  CPU-Spur:
  `cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-bragg-aus r5c.py bragg --geraet cpu --roh /home/fmh/fmhc-physics-remote/runde5-r5c/bragg-v2/r5c_zeitreihen.pt --out /home/fmh/fmhc-physics-remote/runde5-r5c/bragg-v2-auswertung`
  (fuer anderson entsprechend, mit denselben `--seeds` wie im Lauf).

## Kurzfassung

- **Code:** r5c.py (PyTorch, float64/complex128, `--geraet cuda|cpu`). Ein Unterbefehl je Idee, dazu `rauch` und die
  Papierprobe `hintergrund`. Bericht, JSON und Zeitreihen werden nach jedem Unterbefehl geschrieben.
- **Gerechnet werden koennen neun Karten:**
  - osmose (Bio 2) und massenwirkung (Chemie 9), beide nur auf dem dichten, stabilen Kondensat
  - pendeln (Bio 12), ir (Chemie 4), quorum (Bio 39), lawinen (Bio 50), symbiose (Bio 16)
  - bragg (W21) und anderson (W22)
- **Im Ein-Feld-Modell nicht umsetzbar:** Wellen 6 Gleiten, 7 Windschatten, 11 Fahrtwind (Abschnitt 2). Die Papierprobe
  `hintergrund` rechnet die Stabilitaetszahlen dazu nach (Sekunden, keine Zeitentwicklung).
- **Spuren:** Sieben Unterbefehle passen auf eine CPU-Spur (je etwa 1 bis 5 min). bragg und anderson nur auf einer P4000
  (etwa 2 und 4 bis 7 min).
- **Kernvorhersagen:**
  - Der Ball loest sich im dichten Kondensat immer auf, egal ob omega_bg ueber oder unter seinem omega liegt. Die
    Osmose-Regel scheitert.
  - Im gegenphasigen Ring pendeln Ladung und Abstand harmonisch. Beide Frequenzen fallen wie exp(-0,274 D).
  - Symbiose ohne Verschmelzen gibt es nicht.
  - Die Bragg-Luecke liegt bei k = pi/d und wandert mit d.
  - Das Anderson-Gas zeigt nur schwache, zur Laenge proportionale Abschwaechung. Die Lokalisierungslaenge ist
    etwa 100 Baelle, weit laenger als jedes rechenbare Gas.

## 1. Papierprobe: Stabilitaet des Hintergrunds (vor dem Code, Leitung Punkt 1)

Ruhender Hintergrund psi = A exp(-i omega_bg t), S = A^2, omega_bg^2 = U'(S) = 1 - 2 S + 1,5 S^2. Stoerung
(u + i v) exp(i(k x - Om t)). Dann gilt:
- Dispersion: (k^2 - Om^2)(k^2 + M2 - Om^2) = 4 omega_bg^2 Om^2 mit M2 = 2 S U''(S) = 2 S (3 S - 2), also
  Codex' beta.
- **0 < S < 2/3 (M2 < 0): modulationsinstabil.**
  - Das Band ist 0 < k^2 < -M2, die schnellste Rate gamma_max = |M2|/(4 omega_bg), bei duennem Hintergrund etwa S.
  - Keine Schallgeschwindigkeit, keine Landau-Schwelle (v_c = 0), wie im Fable-Review.
  - Dazu die Mechanik-Analogie f'' = -dV/df, V = (omega^2 f^2 - U(f^2))/2. Der Hintergrund ist dort ein Minimum
    von V, also gibt es **keine Einzelloesung "Ball im duennen Hintergrund"**, nur periodische Ketten.
  - Einen Ball im Gleichgewicht mit einem duennen Medium gibt es also schon statisch nicht.
- **S > 2/3 (M2 > 0): linear stabil fuer alle k.**
  - Schall c_s^2 = M2/(M2 + 4 omega_bg^2): 0,555 / 0,707 / 0,733 / 0,747 bei S = 0,8 / 1,0 / 1,1 / 1,2.
  - Hier ist der Hintergrund ein Maximum von V. Stationaer gibt es nur Dellen ("Blasen", S < 1) oder dunkle Solitonen
    (S > 1), **keine Buckel**. Ein Q-Ball kann auf dem stabilen Kondensat also nicht als eigener Koerper bestehen.
  - omega_bg^2 laeuft von 1/3 (S = 2/3) ueber 1/2 (S = 1, Koexistenz mit dem Vakuum, Innenleben der duennen Wand)
    bis 1 (S = 4/3).
- **Kasten-Schlupfloch (nicht gerechnet):**
  - Im Ring der Laenge L liegt keine Ringmode im instabilen Band, wenn S < S_krit(L), etwa (pi/L)^2. Das sind
    9,9e-4 bei L = 100 und 1,1e-4 bei L = 300.
  - Das ist linear stabil, aber ein Kasteneffekt: Das "Medium" ist dann nur eine schwache lineare Welle.
  - Die Bremskraft waere Strahlungsdruck 4 R(k) k^2 S, also aus R(k) von RUNDE-02 Test 2 ableitbar (L4).
  - Nach der Anweisung der Leitung (keine Scheinmessung) nicht gerechnet.
- `hintergrund` prueft das nach: Es scannt die exakte Dispersion auf 30000 k-Werten gegen die Formeln (gamma_max,
  Bandkante, c_s, Landau-v_c) fuer 16 Dichten von 1e-4 bis 1,3 und gibt S_krit(L) fuer L = 100, 200, 300 aus.

## 2. Nicht umsetzbare Karten (Leitung Punkt 3)

- **Wellen 6, Gleiten: im Ein-Feld-Modell nicht umsetzbar.**
  - Bei S < 2/3 ist das Medium instabil und hat v_c = 0. Bei S > 2/3 gibt es keinen Ball, der hindurchfahren koennte.
  - Mit dem Medium als zweitem Feld ginge es, etwa chi mit abstossendem |chi|^4 und Kopplung lambda |psi|^2 |chi|^2.
    Dann ist das Medium ein stabiles Superfluid mit Schallgeschwindigkeit, und F(v) samt Landau-Schwelle ist wohlgestellt.
  - Der Zwei-Feld-Code aus R5-D waere die Grundlage.
- **Wellen 7, Windschatten: im Ein-Feld-Modell nicht umsetzbar** (gleicher Grund).
  - Mit zweitem Feld ginge es.
  - Papiervorhersage fuer diesen spaeteren Test, fuer schwache Streuer in 1D bis auf O(R):
    - Der hintere Ball spuert dieselbe Bremskraft wie ein Einzelball.
    - Die Kraft auf den vorderen schwankt mit dem Abstand wie F_1 (1 + 2 cos(2 k D + phi0)), also Fabry-Perot.
    - Einen Windschatten im Sinne geringerer Kraft hinten gibt es nicht.
- **Wellen 11, Fahrtwind: im Ein-Feld-Modell nicht umsetzbar** (gleicher Grund).
  - Mit zweitem Feld ginge es.
  - Die Antwort folgt aber schon aus der Lorentz-Invarianz des Modells: Die Kraft laengs der Bewegung ist im Ruhesystem
    des Balls und im Laborsystem gleich.
  - Der Test waere eine reine Numerikprobe (L4).

## 3. Aufbau je Unterbefehl (vor dem Lauf festgelegt)

**Gemeinsam.**
- Integrator, Gitter und Schritt aus tests1d.py unveraendert: Velocity-Verlet, dx = 0,1, dt = 0,05, fein dx/2 und dt/2,
  quadratische Daempfungsschicht 40 breit.
- Standardball omega^2 = 0,70 (FWHM 3,56).
- Messung alle 0,5. Je Zelle:
  - Ort des Maximums (mit Parabel), S_max und Phase dort
  - im Fenster: Ladung, Energie, Impuls und Breite
- Je Ebene: Ladungsfluss und T_xx. Dazu Gesamtladung, -energie und -impuls.
- Abweichungen von der Vorlage, begruendet:
  - (a) Anker statt Schiessen, weil das Schiessen in 1D nur den Anker reproduziert (1,5e-10) und 80 s je Aufruf kostete.
  - (b) Periodischer Ring, weil die Ringtests mechanisch balanciert sein muessen. Die offene Box ist derselbe Ring mit
    Daempfung am Stoss.
  - (c) Hintergrund als exakt diskrete Loesung, damit der Lauf "Kondensat allein" eine saubere Nulllinie ist.

**osmose (Bio 2).**
- Ring L = 200 ohne Daempfung, T = 200, 9 Laeufe.
- Kondensat S = 0,8 / 1,0 / 1,1 / 1,2, also omega_bg = 0,600 / 0,707 / 0,784 / 0,872.
- Ball omega^2 = 0,70 (omega = 0,837) bei 0, Phase pi/2 gegen das Kondensat: Dann gibt es zu Beginn keinen Kreuzterm
  in rho und |psi|^2.
- omega - omega_bg = +0,237 / +0,130 / +0,052 / -0,035. Bei S = 1,2 hat das Kondensat also das hoehere chemische
  Potential; nach der Osmose-Hypothese muesste der Ball dort wachsen.
- Laeufe: Ball + Kondensat (4), Kondensat allein (4), Ball allein (1).
- Messgroesse ist der Ueberschuss im festen Fenster |x| < 15: Q(Ball + Kondensat) - Q(Kondensat). Dazu:
  - Buckelhoehe S(0) - S_Kondensat
  - Anfangsrate (0 bis 30)
  - Verhaeltnis zum Anfang bei T/5 bis 3T/10 und im Endfenster [3T/4, T]
  - Drehfrequenz der Phase bei x = 0 im Endfenster
- Der Schall erreicht die Gegenseite des Rings erst bei t = 135 bis 180 und ist bei T = 200 noch nicht zurueck.

**massenwirkung (Chemie 9).**
- Ring L = 200, T = 800, 7 Laeufe.
- Kondensat S = 1,1 (omega_bg = 0,784).
- Drei Startmischungen: Ball omega^2 = 0,55 / 0,70 / 0,90, also omega - omega_bg = -0,043 / +0,052 / +0,165.
- Laeufe: Ball + Kondensat (3), Kondensat allein (1), Baelle allein (3).
- Gemessen wie osmose, lange Laufzeit. Der Schall laeuft mehrfach um, das Endfenster [600, 800] ist deshalb ein
  Zeitmittel.
- Grundlinie fuer "vollstaendig verteilt": Fensteranteil 2W/L = 0,15.

**pendeln (Bio 12).**
- Ring L = 120 mit K = 16 / 12 / 10 / 8 / 6 / 4 gegenphasigen Baellen (Phasen 0, pi, ...), also D = 7,5 / 10 / 12 / 15
  / 20 / 30.
  - Jeder Ball wird von beiden Nachbarn gleich abgestossen und liegt mechanisch stabil. Beleg ist die gemessene maximale
    Verschiebung.
  - Die Ladungsmode ist um die Gegenphase stabil, weil domega/dQ < 0 ist.
- Anstoss: omega^2 = 0,70 +- 0,004 abwechselnd, also Ladungsungleichgewicht q0 = -0,024.
- Kontrollen: K = 12 ohne Ungleichgewicht; K = 12 gleichphasig mit Ungleichgewicht.
- Dazu freie Paare in der offenen Box [-150, 150]:
  - D = 7 / 8 / 10 mit dphi = pi und Ungleichgewicht
  - D = 8 mit dphi = pi/2 ohne Ungleichgewicht
- T = 600.
- Messgroessen:
  - q(t) = Mittel (-1)^j Q_j; Hauptfrequenz der FFT Omega_p; Steigung von ln Omega_p gegen D (D bis 15)
  - bei freien Paaren: Nulldurchgaenge von q und Abstand D(t)

**ir (Chemie 4).**
- Ring L = 120, K = 16 / 12 / 10 / 8 / 4 gleich grosse gegenphasige Baelle, abwechselnd um +-0,3 verschoben. Das ist
  die Zonenrand-Schwingung, in der jeder Abstand zwischen D + 0,6 und D - 0,6 pendelt.
- Kontrolle K = 12 ohne Verschiebung. T = 600.
- Messgroessen: u(t) = Mittel (-1)^j (x_j - x_j0), FFT; Ladungsmode max |q| als Nebenkontrolle.
- Kleinste sinnvolle Form: Ein freies gebundenes Paar gibt es nicht (gleichphasig verschmilzt, gegenphasig stoesst ab).
  Das "Molekuel" ist deshalb ein Ball, der zwischen zwei abstossenden Nachbarn liegt.

**symbiose (Bio 16).**
- Offene Box [-150, 150], freie Paare im Abstand 10: links omega^2 = 0,70, rechts 0,70 / 0,71 / 0,72 / 0,74 / 0,78,
  gleichphasig.
- Dazu 0,70/0,70 gegenphasig und ein Einzelball. T = 800.
- Klassen: verschmolzen (Abstand am Ende < 1,5), getrennt (> 20), sonst "gebunden".
- Energiebilanz:
  - Bindung zu Beginn = E_Box(0) - E1 - E2
  - Gewinn beim Verschmelzen aus dem Anker
  - abgestrahlte Energie E_Box(0) - E_Box(T)
  - Anregung = E_Box(T) - E_Anker(Q_Box(T))

**quorum (Bio 39).**
- Ring L = 120, K = 8 / 12 / 16 gegenphasig (D = 15 / 10 / 7,5, drei Dichten).
- Jeder Ball bekommt einen Atemstoss mit Zufallsphase (Seed 1239): psi mal (1 + 0,02 cos alpha),
  psi_t mal (1 + 0,02 cos alpha) - 0,02 x 0,17 sin alpha psi.
- Kontrollen: K = 12 mit gleicher Phase alpha = 0 (Symmetrie: bleibt synchron); K = 2 (D = 60, entkoppelt).
- T = 600.
- Atemsignal ist die Breite je Ball, demoduliert bei der gemessenen Atemfrequenz. Daraus je Zeitviertel die
  Kuramoto-Ordnung r und die Kohaerenz C.

**lawinen (Bio 50).**
- Ring L = 240, K = 24 gegenphasig (D = 10), T = 500.
- Alle 10 Zeiteinheiten ein Stoss auf einen zufaelligen Ball: Faktor 1 + eta auf psi und psi_t in seiner Zelle,
  eta zwischen 0,01 und 0,03; 49 Stoesse.
- Vier Seeds, dazu zwei Kontrollen: ohne Stoesse; entkoppelter Ring K = 8 (D = 30) mit demselben Stoss-Seed.
- Ereignis: |S_max/S_max(0) - 1| > 1 %. Lawine: zusammenhaengendes Gebiet in (Zeit, Ball), Nachbarn ringfoermig.
  Groesse ist die Zahl der beteiligten Baelle.

**bragg (W21).**
- Ring L = 480 voll mit gegenphasiger Kette, d = 10 (48 Baelle) oder 12 (40 Baelle).
- Die Kette ruht aus Symmetriegruenden (jeder Ball zwischen zwei gleichen Nachbarn). Beleg ist je ein Lauf ohne Paket
  mit maximaler Verschiebung.
- Die Phase (0 oder pi) geht in die lineare Streuung nur als exp(2 i phi) = 1 ein. Fuer die Welle ist die Periode
  also d, nicht 2d.
- Paket: eps = 1e-3, sigma = 25, Start x0 = -120 (Mitte zwischen zwei Baellen), Traeger k0 = 0,22 bis 0,38 (11 Werte).
- Ebenen genau in Mitten zwischen Baellen, dort ist das Kettenfeld null:
  - vorn -210 / -216 und hinten -40 / -36
  - 80 bzw. 84 Laengeneinheiten Kette zwischen Start und hinterer Ebene
- T = 700; die Laufzeit des Pakets um den Ring bis zur vorderen Ebene liegt ueber 880.
- Transmission T = Fluss hinten ueber die Zeit / derselbe Fluss im leeren Ring; R = -Fluss vorn / derselbe Nenner.
  Der Restfluss der Kette ohne Paket wird abgezogen.
- Gegenproben: leerer Ring (11 Laeufe, Nenner) und Einzelball bei -76 (4 k0).

**anderson (W22).**
- Ring L = 1400.
- Baelle ab x = -400, Abstaende gleichverteilt in [30, 40], Zufallsphasen, N = 4 / 8 / 16, vier Seeds (`--seeds`).
- Der Mindestabstand 30 haelt die Kraefte unter 2e-7: Verschiebung bis T hoechstens etwa 0,2, Beleg im Bericht.
- Periodische Gegenprobe: Abstand 35, gegenphasig. k0 d = 4,67 pi liegt mitten im Durchlassband, weit von den Bragg-
  Bedingungen 4 pi und 5 pi.
- Paket k0 = 0,4189 (v_g = 0,386), sigma = 40, bei -500 (2,5 sigma vor dem ersten Ball); Ebenen bei -620 und +230. T = 2200; bis dahin sind 99,8 % des (zerfliessenden) Pakets durch die hintere Ebene.
- Dazu ein leerer Ring (Nenner) und ein Einzelball (R_1).
- Ausgabe:
  - <ln T> ueber die Seeds je N; periodisches ln T
  - Steigung je Ball; Lokalisierungslaenge xi = d_mittel/|Steigung|

## 4. Aufrufe (Leitung, auf der .69, ueber kleintest.sh)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde5-r5c/ mit r5c.py darin. Das Programm braucht nur torch und schreibt nur
in --out.
- `--geraet cpu` auf den Spuren cpu/cpu2: kleintest.sh setzt dort CUDA_VISIBLE_DEVICES leer, das Programm nutzt einen
  Thread.
- `--geraet cuda` auf p4000a/b; der Torch-Speicher ist auf 1,5 GB gedeckelt.

**1. Rauchtests** (Laufzeiten x 0,05; nur Durchlaufprobe und Zeitmessung, Zahlen ungueltig). Der Bericht nennt je
Unterbefehl eine Hochrechnung fuer die volle Laenge.

```
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5c-rauch-gpu r5c.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5c/rauch-gpu
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-rauch-cpu r5c.py rauch --geraet cpu --nur osmose,massenwirkung,pendeln,ir,quorum,lawinen,symbiose --out /home/fmh/fmhc-physics-remote/runde5-r5c/rauch-cpu
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-hg r5c.py hintergrund --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/hintergrund
```

**2. Hauptlaeufe**, nur wenn der passende Rauchtest rc = 0 hatte und die Hochrechnung unter 9 min liegt. Jede Zeile ist
unabhaengig und kann auf der genannten Spur parallel zu den anderen Spuren laufen.

```
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-osm r5c.py osmose --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/osmose
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5c-mw r5c.py massenwirkung --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/massenwirkung
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-pend r5c.py pendeln --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/pendeln
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5c-ir r5c.py ir --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/ir
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-quor r5c.py quorum --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/quorum
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5c-law r5c.py lawinen --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/lawinen
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5c-sym r5c.py symbiose --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5c/symbiose
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5c-bragg r5c.py bragg --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5c/bragg
cd /home/fmh/fmhc-physics-remote/runde5-r5c && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5c-and r5c.py anderson --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5c/anderson
```

- **Anderson:** Rechnet der GPU-Rauchtest mehr als 9 min hoch, dann mit `--seeds 2` starten (halbe Laufzahl bei den
  Zufallsgasen, der Rest bleibt gleich).
- Die CPU-Unterbefehle laufen auch auf p4000a/b: `--geraet cuda`, Spur tauschen, sonst gleich.
- Ein Abbruch durch RuntimeMaxSec trifft nur den laufenden Unterbefehl. Seit v2 steht jede fertige Stufe sofort in
  `r5c_roh_zwischen.pt`. Sind beide Stufen fertig, laesst sich mit `--roh` ohne Rechnung auswerten. Bricht schon die
  feine Stufe ab, fehlt L3; die Hochrechnung aus dem Rauchtest bleibt deshalb verbindlich.

## 5. Laufzeit je Unterbefehl (Schaetzung, nicht gemessen)

Grundlage sind die RUNDE-02-Messungen auf der P4000: etwa 1 ms je Verlet-Schritt bis rund 2e5 Feldpunkte je Schritt
(Kernelstarts); darueber waechst die Zeit mit dem Speicherverkehr. Fuer die CPU (ein Kern) setze ich 50 bis 100 ns je
Feldpunkt und Schritt an, plus 0,3 ms Python je Schritt. Das ist geschaetzt; der CPU-Rauchtest misst es.

| Unterbefehl | Laeufe x Punkte (grob) | Schritte grob + fein | P4000 | CPU, 1 Kern | Spur |
|---|---|---|---|---|---|
| hintergrund | keine Zeitentwicklung | - | - | unter 10 s | cpu |
| osmose | 9 x 2000 | 4000 + 8000 | etwa 0,5 min | 0,5 bis 1 min | cpu |
| massenwirkung | 7 x 2000 | 16000 + 32000 | etwa 1 min | 1,5 bis 3 min | cpu2 |
| pendeln | 8 x 1200 und 4 x 3000 | je 12000 + 24000 | etwa 1,5 min | 2 bis 4 min | cpu |
| ir | 6 x 1200 | 12000 + 24000 | etwa 0,7 min | etwa 1 min | cpu2 |
| quorum | 5 x 1200 | 12000 + 24000 | etwa 0,7 min | etwa 1 min | cpu |
| lawinen | 6 x 2400, 24 Zellen | 10000 + 20000 | etwa 0,7 min | 1,5 bis 3 min | cpu2 |
| symbiose | 7 x 3000 | 16000 + 32000 | etwa 1 min | 2,5 bis 5 min | cpu |
| bragg | 39 x 4800 | 14000 + 28000 | etwa 2 min (1,5 bis 3) | 15 min oder mehr, nicht auf CPU | p4000a |
| anderson | 17 x 14000 | 44000 + 88000 | 4 bis 7 min | Stunden, nicht auf CPU | p4000a |
| rauch (GPU, alle) | | x 0,05 | 2 bis 4 min mit Start | | p4000a |
| rauch (CPU, sieben) | | x 0,05 | | 1 bis 2 min | cpu |

- **Speicher:** Das groesste Feld ist anderson fein, 17 x 28000 complex128 = 7,6 MB; mit Zwischenwerten und
  Zellenmasken (17 x 4 x 28000) unter 0,2 GB. Die Zeitreihen sind hoechstens 25 MB.
- **Zusammen:** etwa 12 min GPU und 12 bis 20 min CPU, verteilt auf zwei GPU- und sieben CPU-Aufrufe.

## 6. Vorhersagen (vor dem Rechnen, von Hand)

Zahlen fuer omega^2 = 0,70 aus dem Anker:
- kappa = 0,5477, Tail-Amplitude A^2 = 4 a0/b0 = 1,897
- Kopplung J(D) = 4 kappa A^2 exp(-kappa D) = 4,157 exp(-0,5477 D)
- |domega/dQ| = 0,1013, E = 2,2986, Q = 2,4415

**osmose (Bio 2).**
- Papierbild: Auf dem stabilen Kondensat gibt es keinen Buckel als Loesung (Abschnitt 1). Der Ball ist dort nur ein
  Druckberg und laeuft als Schall auseinander.
- **V-O1:** In allen vier Dichten faellt der Ueberschuss im Fenster bis T/4 unter 0,3 und liegt im Endfenster unter
  0,3 des Anfangs. Die Aufloesungszeit liegt bei etwa 15/c_s + Ballbreite/c_s, also 25 bis 40.
  - Moeglich ist, dass eine Delle (Blase, S < 1) oder ein dunkles Soliton (S > 1) zurueckbleibt; dann wird der
    Ueberschuss negativ.
  - Das zaehlt nicht als Wachstum, wohl aber als "nicht aufgeloest" im Bericht (|rel.| >= 0,3); es waere ein
    Nebenbefund.
- **V-O2 (die L1-Probe):** Kein Wachstum bei S = 1,2, obwohl dort omega_bg > omega ist. Die Richtung haengt nicht vom
  Vorzeichen von omega_bg - omega ab.
  - Die Osmose-Hypothese sagt Wachstum bei 1,2 und Schrumpfen bei 0,8 bis 1,1 voraus.
  - Traete dieses Vorzeichenmuster auf (rel. Ende > 1 nur bei S = 1,2), waere meine Vorhersage widerlegt.
- **V-O3:** Die Phase bei x = 0 dreht im Endfenster mit omega_bg +- 0,03, nicht mit dem omega des Balls.

**massenwirkung (Chemie 9).**
- **V-M1:** Keine Mischung behaelt einen Ball. Der Ueberschuss im Endfenster liegt bei hoechstens 0,3; die Grundlinie
  fuer volle Verteilung ist 0,15.
- **V-M2:** "omega = omega_bg" wird erreicht (Drehfrequenz in der Mitte = 0,784 +- 0,03), aber durch Aufloesung. Es ist
  kein Gleichgewicht zwischen gebundener und freier Ladung. Der Ball mit omega < omega_bg (0,55) waechst nicht.
- Scheitert, wenn in einer Mischung ein Buckel mit eigener Frequenz bis T = 800 ueberlebt.

**pendeln (Bio 12).**
- Papierbild: Josephson-Kontakt mit negativer Ladeenergie (domega/dQ < 0). Deshalb ist die Gegenphase stabil und die
  Gleichphase instabil.
- Im Ring hat jeder Ball zwei Kontakte, also Omega_p^2 = 4 |domega/dQ| J(D), Omega_p = 1,298 exp(-0,2739 D).

| D | 7,5 | 10 | 12 | 15 | 20 | 30 |
|---|---|---|---|---|---|---|
| Omega_p | 0,166 | 0,084 | 0,049 | 0,021 | 0,0054 | 0,0004 |
| Periode | 38 | 75 | 130 | 294 | 1160 | 18000 |

- **V-P1:** q(t) schwingt harmonisch um 0. Das Verhaeltnis gemessen/vorhergesagt liegt bei D = 10 und 12 in
  [0,5; 2], bei D = 7,5 in [0,3; 3], weil die Tail-Formel dort grob ist.
- **V-P2:** Die Steigung von ln Omega_p gegen D liegt in [-0,33; -0,22] (Vorhersage -0,274 = -kappa/2).
- **V-P3:** D = 20 zeigt hoechstens eine halbe Schwingung. D = 30 bleibt eingefroren (Spanne q < 5 % von |q0|).
- **V-P4:** Kontrollen:
  - Ohne Ungleichgewicht bleibt |q| < 1e-3.
  - Gleichphasig waechst |q| um mindestens den Faktor 3, oder die Baelle verschmelzen (min. Abstand < 1,5).
- **V-P5 (freie Paare):**
  - dphi = pi: Die Baelle trennen sich (D_Ende > 2 D0), mit hoechstens zwei Nulldurchgaengen von q. Mechanische
    Abstossung und Ladungspendeln haben die gleiche Zeitskala (Verhaeltnis 0,88, unabhaengig von D).
  - dphi = pi/2: Ein grosser Ladungsschub, danach Trennung oder Verschmelzen; kein Dauerpendeln.

**ir (Chemie 4).**
- Omega_vib^2 = 4 kappa^2 J(D)/E, Omega_vib = 1,473 exp(-0,2739 D):

| D | 7,5 | 10 | 12 | 15 | 30 |
|---|---|---|---|---|---|
| Omega_vib | 0,189 | 0,095 | 0,055 | 0,024 | 0,0004 |
| Periode | 33 | 66 | 114 | 260 | eingefroren |

- **V-I1:** Das Verhaeltnis gemessen/vorhergesagt liegt in [0,5; 2] fuer D = 10, 12 und 15. Die Steigung von
  ln Omega_vib ist -0,274 +- 25 %.
- **V-I2:** Omega_vib/Omega_p = 1,135, fuer alle D gleich (Vergleich mit pendeln).
- **V-I3:** Die Ladungsmode bleibt ruhig (max |q| < 1e-3), denn die Verschiebung stoert die Gegenphase nicht in erster
  Ordnung. D = 30 bleibt bei u = s0 (Spanne < 5 %). Die Kontrolle s0 = 0 bleibt bei u ~ 0.
- **V-I4:** Die Schwingung ist kaum gedaempft (Spanne im letzten Viertel mindestens 0,7 x erstes Viertel). Bei D = 7,5
  ist sie etwas anharmonisch.

**symbiose (Bio 16).**
- Anker-Bilanz: Verschmelzen zweier 0,70-Baelle ergibt Q = 4,883, omega^2 = 0,516, E = 4,149 gegen 2 x 2,2986 = 4,597.
  Das ist ein Gewinn von -0,448.
- Bindung des getrennten Paars bei D = 10: nur -J(10) = -0,017.
- Die Schwebungsperiode 2 pi/(omega_2 - omega_1) betraegt 1056 / 529 / 267 / 135 fuer rechts 0,71 / 0,72 / 0,74 /
  0,78. Die Anziehung wirkt nur etwa ein Viertel davon; der Kontakt braucht bei D = 10 etwa 60.
- **V-S1:**
  - 0,70/0,70, 0,71 und 0,72 verschmelzen.
  - 0,74 liegt auf der Kippe.
  - 0,78 verschmilzt nicht und trennt sich nicht (Abstand bleibt 7 bis 14). Die Kraft mittelt sich weg; das ist kein
    Energiegewinn.
  - Gegenphasig: getrennt.
- **V-S2:** Nach dem Verschmelzen ist die abgestrahlte Energie 0,05 bis 0,45; der Rest steckt als Anregung im Ball.
- **V-S3 (L1):** Es gibt keinen Lauf mit "gebunden" UND einer Energie deutlich unter E1 + E2. Symbiose ohne
  Verschmelzen gibt es nicht.

**quorum (Bio 39).**
- Papierbild (siehe Fable-Review):
  - Q-Baelle sind keine freien Phasenoszillatoren. Die Atemfrequenz (etwa 0,17) liegt an der Kontinuumskante
    1 - omega = 0,163 und strahlt langsam ab.
  - Die Kopplung zwischen Nachbarn laeuft ueber J (0,0006 bis 0,055) und langsame Strahlung.
- **V-Q1:** Kein Quorum-Schalter: r_Ende < 0,6 bei allen drei Dichten, und r_Ende - r_Anfang < 0,3.
- **V-Q2:** Die Kohaerenz C bleibt unter 0,5.
- **V-Q3:** Kontrollen:
  - Gleiche Phase bleibt aus Symmetrie bei r nahe 1.
  - Der entkoppelte Ring (K = 2) bleibt beim Anfangswert.

**lawinen (Bio 50).**
- Papierbild:
  - Ein Stoss aendert die Ladung des Balls um 2 eta Q, also 0,05 bis 0,15. Damit dreht seine Phase gegen die Nachbarn
    mit |domega/dQ| x Delta Q, etwa 0,01 je Zeiteinheit.
  - Das treibt Josephson-Stroeme; die Stoerung laeuft als Ladungswelle die Kette entlang, mit hoechstens
    sqrt(|domega/dQ| J) = 0,042 Baellen je Zeiteinheit.
  - Ohne Daempfung im Ring bleibt jede Anregung erhalten.
- **V-L1:**
  - Lawinen sind groesser als ein Ball (mittlere Groesse > 1,5), weil die Ladungswelle die Nachbarn ueber die 1-%-
    Schwelle hebt.
  - Die Verteilung ist aber kein Potenzgesetz: Mit der Zeit waechst der aktive Anteil, und am Ende gibt es eine
    Riesenlawine (aktiver Anteil am Ende > 0,5). Das ist Aufsummieren ungedaempfter Anregung, keine Kritikalitaet.
- **V-L2:** Kontrollen:
  - Ohne Stoesse: keine Ereignisse.
  - Entkoppelter Ring (D = 30, J = 3e-7): nur Groesse 1, abgesehen von Zufallstreffern benachbarter Baelle.
- Mit 49 Stoessen ist ein Potenzgesetz ohnehin nicht belegbar. Die Frage ist nur, ob die Groessen ueber die
  Zufallstreffer hinausgehen.

**bragg (W21).**
- Einzelball-Reflexion aus RUNDE-02 Test 2: R = 4,2e-3 bei k = 0,515, faellt etwa wie exp(-7,2 k). Hochgerechnet ist
  R(0,31) etwa 0,018 und R(0,26) etwa 0,026, also |r| = 0,13 bis 0,16.
- Luecke bei k = pi/d mit Breite etwa 2|r|/d = 0,027 und Daempfungslaenge d/|r|, etwa 75.
- **V-B1:** Das Transmissionsminimum liegt bei k0 = 0,31 +- 0,015 (d = 10) und 0,26 +- 0,015 (d = 12). Die Luecke
  wandert mit pi/d.
- **V-B2:** Die Tiefe betraegt T_min 0,4 bis 0,85. Monochromatisch waere 1/cosh^2(8 |r|) = 0,4; das Paket
  (sigma_k = 0,04) ist breiter als die Luecke und verschmiert sie. Ausserhalb der Luecke gilt T >= 0,95.
- **V-B3:** Einzelball: T >= 0,95 ohne Minimum, R_1(k0) faellt mit k0. Die Kette ohne Paket ruht (max Verschiebung
  < 0,05).
- **V-B4 (L1):** Laege das Minimum bei pi/(2d), also bei Periode 2d, waere die Phasenaussage falsch. Diese Werte (0,157
  und 0,131) liegen allerdings ausserhalb des Scans, weil sie zu langsam sind; das bleibt offen.

**anderson (W22).**
- R_1(0,4189) etwa 8e-3 (hochgerechnet), also -ln T_1 etwa 0,008.
- **V-A1:** <-ln T> waechst linear mit N: etwa 0,03 / 0,07 / 0,13 fuer N = 4 / 8 / 16. Das Verhaeltnis zu
  N x (-ln T_1) liegt in [0,7; 1,4].
- **V-A2:** Die Lokalisierungslaenge ist xi = d_mittel/R_1, etwa 4000 Laengeneinheiten oder rund 120 Baelle. Echte
  Lokalisierung (T << 1) ist im Rahmen von 10 min nicht zu sehen.
  - Linear in N und "Ohm" (1/(1 + N R)) unterscheiden sich hier nur um weniger als 1 %.
  - Der Test prueft nur die zufallsphasige Addition, nicht Lokalisierung gegen Diffusion.
- **V-A3 (Gegenprobe):** Die periodische Kette im Durchlassband waechst nicht mit N: |ln T_per(16)| < 0,5 x
  <-ln T_zufall(16)>.
- **V-A4:** Die Kugeln ruhen (max Verschiebung < 0,5).

## 7. Gegenproben

| Unterbefehl | Gegenprobe (Effekt muss verschwinden) | im Code |
|---|---|---|
| osmose, massenwirkung | Kondensat allein (steht exakt), Ball allein (Vakuum); Vorzeichen von omega - omega_bg in beiden Richtungen | Laeufe "hg", "ball" |
| pendeln | kein Ungleichgewicht (q bleibt 0); D = 30 (eingefroren); gleichphasig (Pendeln wird Weglaufen) | K = 12 delta = 0, K = 4, "gleich" |
| ir | keine Verschiebung; D = 30 | K = 12 s0 = 0, K = 4 |
| symbiose | gegenphasig; Einzelball (Energiedrift) | letzte zwei Laeufe |
| quorum | gleiche Phase (Symmetrie); entkoppelt K = 2 | "gleich", "entkoppelt" |
| lawinen | ohne Stoesse; entkoppelter Ring D = 30 | letzte zwei Laeufe |
| bragg | leerer Ring; Einzelball; zwei Abstaende; Kette ohne Paket | "leer", "einzel", d = 10/12 |
| anderson | periodisch (Durchlassband); leer; Einzelball | "periodisch", "leer", "einzel" |

## 8. Aufloesungsvergleich (L3)

- Jeder Unterbefehl rechnet grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025).
- L3 ist bestanden, wenn der Effekt (Abstand vom Nullwert) mindestens fuenfmal so gross ist wie die Aenderung grob ->
  fein. Die Hilfe l3 stammt aus tests1d.py.
- Nur dt allein: in `stufen` DX * FEIN durch DX ersetzen (eine Stelle).

| Unterbefehl | L3-Groesse (Nullwert) |
|---|---|
| osmose | rel. Ueberschuss am Ende (1 = kein Effekt) |
| massenwirkung | Drehfrequenz in der Mitte am Ende (omega des Balls) |
| pendeln | Omega_p (0) |
| ir | Omega_vib (0) |
| symbiose | Abstand am Ende (D0) |
| quorum | r am Ende (r am Anfang) |
| lawinen | mittlere Lawinengroesse (1) |
| bragg | T je k0 (1) |
| anderson | <ln T> je N (0) |

## 9. Latten (Vorschlag, die Leitung entscheidet)

| Latte | osmose / massenwirkung | pendeln / ir | symbiose | quorum / lawinen | bragg | anderson |
|---|---|---|---|---|---|---|
| L1 kann scheitern | ja: Wachstum nur bei omega_bg > omega (V-O2), oder ein ueberlebender Buckel (V-M1) | ja: Steigung ausserhalb [-0,33; -0,22], Verhaeltnis ausserhalb [0,5; 2] | ja: "gebunden" mit Energiegewinn | ja: r_Ende > 0,6 bzw. nur Groesse 1 im gekoppelten Ring | ja: Minimum nicht bei pi/d oder wandert nicht | ja: <-ln T> nicht proportional zu N, oder periodisch gleich stark |
| L2 Gegenprobe | ja | ja | ja | ja | ja | ja |
| L3 Numerik | im Code | im Code | im Code | im Code | im Code | im Code |
| L4 schon bekannt | weitgehend: Blasen und dunkle Solitonen auf stabilem Hintergrund (kubisch-quintische NLS); Codex' Dispersion [A] | weitgehend: Bosonischer Josephson-Kontakt (Smerzi u. a. 1997), Soliton-Schwanzkraefte (Manton); die Zahlen sind ableitbar | teilweise: 1D-Q-Ball-Stoesse (Battye, Sutcliffe 2000) | nein; Fable-Review: "keine Phasenoszillatoren" | ja: Bragg-Reflexion; neu nur R(k) des Q-Balls | ja: 1D-Lokalisierung; neu nur xi fuer das Q-Ball-Gas |
| L5 Messbezug | nein | nein | nein | nein | nein | nein |

Literatur aus dem Gedaechtnis, nicht nachgelesen.

## 10. Ausgabedateien (im --out-Ordner)

- `r5c_bericht.txt`: Tabellen je Unterbefehl und Stufe, Kontrollen, L3-Zaehlung, Laufzeiten; bei `rauch` die
  Hochrechnung je Unterbefehl
- `r5c_ergebnis.json`: alle Kenngroessen, Laeufe, Fehlertexte
- `r5c_zeitreihen.pt`: Rohmessungen, seit v2 als {Unterbefehl: {Stufenname: {grob, fein}}}, je Stufe t und Daten der
  Form Zeit x Lauf x Spalte. Spaltenplan in `spalten(K, P)`: 7 K Zellspalten, 2 P Ebenenspalten, 3 Summen.
  - Seit v2 auch bei Auswertungsfehlern geschrieben.
  - v1 schrieb {Unterbefehl: Stufen} bzw. bei pendeln {ring, frei}.
- `r5c_roh_zwischen.pt` (v2): Rohdaten des laufenden Unterbefehls, nach jeder Stufe neu geschrieben. Beide Dateien
  taugen fuer `--roh`.

## 11. Grenzen

- **Ungetestet:** Wahrscheinlichste Fehlerstellen sind die Zellenmasken (Formen B x K x N), der Cluster-Code in
  lawinen und die Ebenenlage in bragg. Deshalb zuerst die Rauchtests.
- **Anfangsfelder sind Summen:** Ueberlappende Auslaeufer (D = 7,5) starten leicht angeregt. Der Ball auf dem
  Kondensat ist keine Loesung; genau das wird gemessen.
- **Tracker:** folgen dem Maximum in +-1. Bei Verschmelzen fallen sie zusammen; das wird gezaehlt, nicht gedeutet.
- **bragg:** Das Paket ist spektral breiter als die Luecke; die Tiefe ist deshalb verschmiert. Die Bragg-Lage bleibt
  scharf.
- **anderson:** Die Streuung ist so schwach, dass Lokalisierung und Diffusion nicht zu trennen sind (V-A2); das Ergebnis
  ist eine Zahl fuer xi.
- **Hintergrund:** Der duenne Hintergrund ist bewusst nicht gerechnet (Abschnitt 1). Die dichten Laeufe zeigen
  Aufloesung, nicht Osmose im Sinne der Biologie.
- **Laufzeiten:** nur geschaetzt; die Rauchtests messen sie.

## Einfach gesagt

Wir wollten pruefen, ob sich Q-Baelle in einem "Meer" aus Feld wie Zellen oder Boote verhalten. Auf dem Papier kam
heraus, dass so ein Meer in unserem Modell entweder von selbst zerfaellt (wenn es duenn ist) oder so dicht ist, dass der
Ball darin einfach zerlaeuft wie ein Tropfen Wasser in Wasser; Segel- und Windschatten-Ideen gehen darum erst mit einem
zweiten Feld. Gerechnet wird, was ohne duennes Meer auskommt: Ringe aus Baellen, die Ladung hin- und herschaukeln und im
Abstand schwingen (wir sagen die Takte vorher), Paare, die verschmelzen oder nicht, Stossketten und zwei Wellenversuche
an Ball-Ketten, bei denen eine regelmaessige Kette bestimmte Wellen spiegelt und eine zufaellige nur wenig schwaecht.
Gerechnet ist noch nichts; die Rechnungen dauern je 1 bis 7 Minuten.

Beginn 2026-09-30 01:43:50 CEST, Ende der Fassung 2026-09-30 02:32:25 CEST (beide gemessen mit date).
v2 (Behebung bragg/anderson): Beginn 2026-09-30 02:43:08 CEST, Ende 2026-09-30 02:46:57 CEST (gemessen mit date).
