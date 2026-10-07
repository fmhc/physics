# R6-Weber: Zerspritzt ein Q-Ball an einer Potentialstufe wie ein Tropfen? Laufplan

Bearbeiter: Agent R6-Weber (Anthropic, Opus), Auftrag ../AUFTRAG-WEBER.md. Beginn 2026-09-30 02:35:12 CEST (gemessen),
Ende in der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ.

## Kurzfassung

- **Code:** weber.py (PyTorch, float64/complex128, `--geraet cuda|cpu`), dazu tests2d_r3.py als unveraenderte Kopie aus
  RUNDE-03 (weber.py importiert daraus Schiessen, Gitter, Ball und Massenformel fuer 2D). Unterbefehle: `papier`,
  `karte1d`, `feinv1d`, `winkel2d`, `l3`, `rauch`.
- **Wichtigster Vorbefund (Hypothese, aus den Runde-3-Dateien gelesen):** Die 92 bis 94 % Ladungsverlust bei 0 und
  20 Grad sind sehr wahrscheinlich ein **Auswertefehler**, kein Zerfall (Abschnitt 1). Der neue Code misst deshalb die
  Ladung links, an und rechts der Stufe ueber die ganze Box und wertet vor dem Erreichen der Randschicht aus.
- **Vorhersage:**
  - Weber-Bild (H), aus der Energie hergeleitet: We_c ist mindestens etwa 1,4 in 1D, fuer alle drei Ballgroessen gleich
    auf 5 %.
  - In 2D ist bei omega^2 = 0,7 und v = 0,2 kein Zerfall moeglich; das verbietet schon die Energie.
  - Meine Erwartung: Kein Weber-Zerfall. Aufspaltung gibt es nur an abstossenden Stufen nahe der Teilchenschwelle v_cl
    (Gegenhypothese). Diese Schwelle liegt bei festem Verhaeltnis Bewegungsenergie zu Stufenhoehe, nicht bei fester
    Weber-Zahl.
- **Rechenzeit (geschaetzt):** alle Aufrufe zusammen etwa 9 min auf p4000a, keiner ueber 5 min.
- **Lokaler Rauchtest: nicht ausgefuehrt.** Die Freigabe (Finn, 02:42) kam bei mir nur als Nachricht der Leitung an.
  CLAUDE.md verbietet lokale Interpreterstarts weiter, und eine Agenten-Nachricht zaehlt fuer mich nicht als Finns
  Zustimmung. Der fertige Befehl steht in Abschnitt 6. Die Leitung kann ihn mit Finns Freigabe starten.

## 1. Was Runde 3 wirklich gemessen hat (Lesung der Dateien, Hypothese)

Quelle: RUNDE-03/tests2d-r3/lauf-69/ausgabe/brechung_ergebnis.json und tests2d_r3.py, test_brechung.

- Der "Q-Verlust Fenster" wird am **letzten gueltigen Messpunkt** ausgewertet: |X|, |Y| <= 28, Fenster R_halb + 8
  um den verfolgten Schwerpunkt.
- **0 Grad:** Der Ball sollte nach der Stufe mit 0,254 laufen. Dann erreicht er x = 28 bei t = 190 und die Randschicht
  (x = 34) bei t = 214. Trotzdem ist der letzte gueltige Punkt t = 280 und die Fit-Geschwindigkeit 0,108.
  - Nachgerechnet: 79 Punkte des echten Durchlaufs (x 8 bis 28, Steigung 0,254) und 10 spaete Punkte bei x = 25 bis 27
    ergeben eine Fit-Steigung von 0,10 bis 0,115. Gemessen wurden n_nachher = 89 Punkte und 0,108.
  - Das Fenster ist also nach dem Verschwinden des Balls in der Randschicht auf einen Rest zurueckgewandert.
- **Der Rest ist Strahlung:** Aus den Verlustanteilen und der Anfangsenergie im Fenster (gamma M = 23,09) folgt fuer das
  Uebrige E/Q = 1,025 (0 Grad) bzw. 1,030 (20 Grad). Das liegt ueber der Massenluecke, ist also Wellenmaterie. Der
  bewegte Ball hat E/Q = 0,962.
- **40 und 60 Grad** zeigen nichts: Bei 40 Grad ist der letzte gueltige Punkt t = 231, vor der Randschicht. Bei 60 Grad
  bleibt der Ball bis t = 280 im Feld.
- **Energie (harte Schranke):**
  - Gesamtenergie 23,09, Ball-Masse 22,63.
  - Bewegungsenergie 0,47 plus Stufengewinn 0,29 sind zusammen 0,76.
  - Ladung als Welle abzugeben kostet im Medium mindestens sqrt(0,98) = 0,99 je Einheit. Der Ball im Medium spart nur
    omega_med = 0,82 je Einheit. Damit koennen hoechstens etwa 4,5 Einheiten (19 %) abgegeben werden.
  - Spaltung in zwei Baelle scheitert an Q_min: 2D-Baelle brauchen etwa Q >= 11,7 (Townes-Grenze fuer omega -> 1). Zwei
    Baelle mit je 12 kosten etwa 23,5 bis 23,8, mehr als die vorhandenen 23,09.
  - "Hauptfragment < 50 %" ist bei diesen Parametern in Durchlassrichtung also unmoeglich.
- **Vorhersage V-2D-1:** Bei 0 bis 60 Grad laeuft der Ball intakt durch.
  - q_rechts(t_eval) >= 0,95 bei allen Winkeln, wenn er bei x = +12 steht.
  - Q_box faellt bei 0 und 20 Grad erst ab t ≈ 215 bis 230 (Randschicht), vorher nicht.
  - Scheitert, wenn ein Winkel bei richtiger Auswertung q_haupt < 0,85 zeigt. Dann zuerst Energieerhaltung (E_drift) und
    L3 pruefen.

## 2. Groessen aus dem Profil (vor dem Rechnen, von Hand; `papier` rechnet sie nach)

Wie im Tropfentest:
- rho_W = 2 omega^2 S_c (Enthalpiedichte)
- 1D: D = N/S_c (aequimolarer Durchmesser), sigma = G. Die Wandspannung folgt aus E - omega Q = 2 sigma, weil der
  Kerndruck in 1D exakt null ist. Im Duennwand-Grenzfall gilt G -> sqrt(2)/4 = ebene Wand.
- 2D: D = 2 R_Q, sigma = G/(pi R_Q).
- Daraus: We_1D = omega Q v^2/G und We_2D = 2 omega Q v^2/G.

| omega^2 (1D) | N | G = sigma | Q | E | S_c | D | rho_W | We-Faktor |
|---|---|---|---|---|---|---|---|---|
| 0,6 | 2,0416 | 0,2141 | 3,1628 | 2,8782 | 0,5528 | 3,693 | 0,6634 | 11,44 |
| 0,7 | 1,4591 | 0,1280 | 2,4414 | 2,2986 | 0,3675 | 3,970 | 0,5146 | 15,96 |
| 0,8 | 1,0543 | 0,0655 | 1,8860 | 1,8178 | 0,2254 | 4,677 | 0,3606 | 25,77 |

- Die 1D-Karte reicht bis We = 1,8 (0,6), 2,6 (0,7) und 4,1 (0,8) bei v = 0,4.
- **2D, omega^2 = 0,7:** Q = 23,996, E = 22,626, G = 2,549, R_Q = 2,317, sigma = 0,350. Der We-Faktor ist 15,75.
  - We_n = 0,630 (0 Grad), 0,556 (20), 0,518 (25), 0,472 (30), 0,423 (35), 0,370 (40) und 0,158 (60).

## 3. Vorhersagen (vor dem Rechnen)

**H, Weber-Bild, aus dem Tropfen hergeleitet.** Zerfall braucht mindestens die Energie fuer neue Oberflaeche. Die
senkrechte Bewegungsenergie ist die einzige Quelle ("Wucht").
- Duennwand-Tropfen:
  - 1D: (1/2) M v^2 >= 2 sigma (zwei neue Waende), also We >= 4.
  - 2D: Teilung in zwei gleiche Tropfen verlaengert den Rand um (2 sqrt(2) - 2) pi R, also We >= 3,3. Die
    anziehende Stufe schenkt 4 |V2| N/G = 0,45, dann We >= 2,9.
- Exakt mit den 1D-Ankerformeln (Spaltung in zwei gleiche ruhende Baelle, relativistische Bewegungsenergie):

| omega^2 | Spaltkosten dE | v_E | We_E |
|---|---|---|---|
| 0,6 | 0,203 | 0,357 | 1,46 |
| 0,7 | 0,105 | 0,293 | 1,37 |
| 0,8 | 0,051 | 0,232 | 1,38 |

- **V-H1:** Wenn das Weber-Bild stimmt, liegt die Zerfallsschwelle bei allen drei Ballgroessen bei derselben We_c >= 1,4.
  Oberhalb davon zerfaellt der Ball immer (monoton in v). Bei 0,8 waere das ab v ≈ 0,25, bei 0,7 ab v ≈ 0,3, bei 0,6
  ab v ≈ 0,36. Das gilt fuer beide Vorzeichen von V2.
- Eine zweite Zahl ist moeglich, Phi = |V2| N/G (Stufe gegen Wand). Mit dem Stufengewinn sinkt die Energieschranke fuer
  "beide Haelften durch" deutlich, bei 0,8 und V2 = -0,04 bis We ≈ 0,3; `papier` gibt die Tabelle.
- **2D:** We_n <= 0,63 liegt weit unter 2,9. H sagt dort also **keinen** Zerfall; die Energie verbietet ihn ohnehin
  (Abschnitt 1).

**G, Gegenhypothese Solitonspaltung an der Stufe** [L, aus dem Gedaechtnis: NLS-Solitonen an Barrieren und Stufen,
Holmer/Marzuola/Zworski 2007; Lee/Brand 2006; Experimente Marchant u. a. 2013 mit 85Rb].
- Die Ausgangsgroesse ist die Teilchenschwelle der abstossenden Stufe: gamma M1 = M2(Q). Erster Ordnung gilt
  v_cl ≈ sqrt(V2)/omega.

| omega^2 | v_cl (V2 = +0,01) | We_cl | v_cl (V2 = +0,02) | We_cl |
|---|---|---|---|---|
| 0,6 | 0,118 | 0,161 | 0,167 | 0,318 |
| 0,7 | 0,112 | 0,201 | 0,158 | 0,398 |
| 0,8 | 0,107 | 0,296 | 0,151 | 0,588 |

- **V-G1 (feinv1d):**
  - Der Uebergang zurueck -> durch (q_durch = 0,5) liegt bei allen sechs (omega^2, V2) innerhalb von 5 % um v_cl.
  - Das Spaltfenster (0,1 < q_durch < 0,9) ist hoechstens +-5 % breit. Genau an v_cl kann der Ball auch "haengen"
    bleiben (instabiles Gleichgewicht auf der Stufe).
  - Gespalten heisst hier: genau zwei Fragmente, eines auf jeder Seite.
  - We am Uebergang ist nicht konstant: We50(0,8)/We50(0,6) ≈ 1,85. Beim Weber-Bild waere es 1.
- **V-G2 (karte1d, grob):**
  - V2 = +0,01: zurueck bei v = 0,05 und 0,10, durch ab 0,15.
  - V2 = +0,02: zurueck bis 0,15, durch ab 0,20. Einzige wahrscheinliche Ausnahme ist (0,8; +0,02; 0,15), nur 0,7 %
    unter v_cl: gespalten oder haengt.
  - Anziehende Stufen: durch fuer alle v >= 0,10. Bei v = 0,05 ist teilweise Rueckstreuung moeglich
    (Quantenreflexion, q_zurueck <= 0,3).
  - Kein Zerfall bei v >= 0,25 an irgendeiner Stufe.
- **Meine Erwartung:** G gilt, H scheitert an L1 (kein monotoner Zerfall oberhalb einer festen We_c). Unsicher bin ich
  bei v = 0,05 an anziehenden Stufen und bei der Breite des Spaltfensters.

**Woran man H und G unterscheidet (vorab festgelegt):**

| Merkmal | H (Weber) | G (Solitonspaltung) |
|---|---|---|
| Wo | oberhalb fester We_c, monoton in v | nur um v_cl der abstossenden Stufe, Fenster in v |
| Skalierung ueber omega^2 | We_c gleich | E_kin/(M2 - M1) ≈ 1 gleich; We-Verhaeltnis 0,8 zu 0,6 ≈ 1,85 |
| Fragmente | mehrere oder Strahlung, auch auf derselben Seite | genau zwei, je eines links und rechts |
| Vorzeichen von V2 | beide | nur abstossend (anziehend hoechstens Reflexion bei kleinem v) |
| V2 = 0 | kein Zerfall (keine Stufe, kein Stoss) | kein Zerfall |

## 4. Tests und Auswertung (Regeln vor dem Rechnen fest)

**Gemeinsam:**
- Stufe V(x) = V2 (1 + tanh x)/2 (Breite 1 wie Runde 3), Ball Lorentz-geboostet.
- Fragmente:
  - 1D: zusammenhaengende Gebiete mit S > 0,01 S_c.
  - 2D: gierige Spitzensuche, Kreis R_halb + 5, solange S_max > 0,05 S_c.
  - Ladung relativ zur Anfangsladung. Es zaehlen Fragmente >= 5 %.
- Klassen in dieser Reihenfolge:
  1. haengt: Ladung an der Stufe (|x| <= 8 in 1D, <= 6 in 2D) >= 20 %
  2. zerspritzt: mindestens 3 Fragmente, oder Ladung ausserhalb von Fragmenten >= 30 %
  3. gespalten: durch >= 10 % und zurueck >= 10 %
  4. durch bzw. reflektiert: Hauptfragment >= 90 %, Seite nach seinem Schwerpunkt
  5. sonst angeschlagen
- **Zerfall (H)** heisst: Hauptfragment < 50 %.

**1. karte1d:**
- 3 omega^2 x 6 V2 (-0,04, -0,02, -0,01, 0, +0,01, +0,02) x 8 v (0,05 bis 0,40), zusammen 144 Laeufe.
- Das sind 8 Stapel zu 18 Laeufen, je v ein Stapel mit eigener Laufzeit T = 45/v + 60.
- Box [-200, 200], dx 0,1, dt 0,05, Daempfung |x| > 160. Start 20 vor der Stufe, Auswertung am Ende.
- Die schnellsten Fragmente erreichen bis T hoechstens x ≈ 140 (0,6; -0,04; v = 0,05).
- Ausgabe:
  - je Lauf: Klasse, Zerfall, q_haupt, q_durch, q_zurueck, q_frei, Fragmentliste, Geschwindigkeiten, E-Drift und
    Teilchenbild-Vorhersage
  - je (omega^2, V2): Klassenwechsel, Zerfall-v, v_c und We_c-Intervall
  - Urteil nach Latten

**2. feinv1d:**
- V2 = +0,01 und +0,02, je omega^2 9 Geschwindigkeiten v_cl (1 + {-0,2, -0,1, -0,05, -0,02, 0, 0,02, 0,05, 0,1, 0,2}).
- 54 Laeufe in einem Stapel, T = 45/v_min + 200 ≈ 720.
- Ausgabe: v50, v50/v_cl, We50, Spaltfenster.

**3. winkel2d:**
- Aufbau wie Runde 3: L = 42, x0 = -16, T = 280, y0 = -0,5 v sin(theta) T; omega^2 = 0,7, V2 = -0,02, v = 0,2.
- Winkel 0, 20, 25, 30, 35, 40 und 60 Grad. Dazu V2 = 0 bei 0 und 20 Grad, zusammen 9 Laeufe.
- Auswertung je Lauf bei t_eval: Dann steht der vorhergesagt durchgelassene Ball bei x = +12, vor jeder Randschicht.
- Dazu Zeitreihen Q_links, Q_mitte, Q_rechts, Q_box und E_box bis t = 280, fuer die Runde-3-Deutung (t_randschicht).
- Aufloesungen grob (dx 0,3, dt 0,05) und fein (dx 0,15, dt 0,025).
- Kritischer Winkel und v_n,c, falls es Zerfall gibt; Vergleich mit der 1D-Schwelle (0,7; -0,02) ueber `--karte`.

**4. L3:**
- karte1d und feinv1d zusaetzlich mit `--fein` (dx und dt halbiert).
- Vergleich mit `l3` (verlangt: hoechstens ein Klassenwechsel, kein Zerfallswechsel, |dq| <= 0,05).
- 2D grob gegen fein im selben Aufruf (gleiche Klasse, |dq| <= 0,02).
- Der Auftrag verlangt L3 nur an den Schwellenlaeufen. Die ganze Karte fein kostet auf der GPU nur etwa 1 min, deshalb
  vergleicht `l3` alle Laeufe; die Schwellenlaeufe sind darin enthalten.

## 5. Gegenproben

- **V2 = 0 (1D):** 24 Laeufe (3 omega^2 x 8 v). Verlangt: alle "durch", q_haupt >= 0,99. Das ist L2 im Bericht.
- **V2 = 0 (2D):** 0 und 20 Grad. Verlangt: durch, q_haupt >= 0,97.
- **Teilchenbild:** Ausserhalb von +-10 % um v_cl muss die Klasse durch/reflektiert der Vorhersage aus gamma M1 gegen M2
  folgen (Spalte "Teilchenbild").
- **Energie:** E_drift bis zur Auswertung unter 1e-3 (2D) bzw. solange keine Strahlung die Daempfung erreicht (1D).

## 6. Aufrufe (Leitung, auf der .69, ueber kleintest.sh)

- Remote-Ordner /home/fmh/fmhc-physics-remote/runde6-weber/ mit **weber.py und tests2d_r3.py** (beide aus diesem Ordner).
- Das Programm braucht nur torch und schreibt nur in --out. Mit `--geraet cpu` nutzt es einen Thread. Auf der GPU ist
  der Speicher auf 1,5 GB gedeckelt.

**0. Lokaler Rauchtest (von mir nicht ausgefuehrt, siehe Kurzfassung).** Nur mit Finns Freigabe, CPU, 1 Thread.
Geschaetzt: die erste Zeile etwa 15 s; die zweite etwa 60 s 2D-Schiessen auf der CPU plus 20 s Entwicklung. Die
Hochrechnung aus einem CPU-Rauchtest gilt nicht fuer die P4000.

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/weber && python3 -m py_compile weber.py tests2d_r3.py
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/weber && mkdir -p lauf-lokal && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 weber.py rauch --geraet cpu --nur karte1d,feinv1d --out lauf-lokal/1d
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-06/weber && mkdir -p lauf-lokal && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 19 timeout 120 python3 weber.py rauch --geraet cpu --nur winkel2d --stufe grob --out lauf-lokal/2d
```

**1. Rauchtest auf der .69** (Laufzeiten x 0,05; Zahlen ungueltig, nur Durchlauf und Hochrechnung je Unterbefehl):

```
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6w-rauch weber.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-weber/rauch
```

**2. Hauptlaeufe**, nur nach Rauchtest mit rc = 0 und Hochrechnung unter 9 min. Die Reihenfolge zaehlt nur bei l3 und
bei `--karte`.

```
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r6w-papier weber.py papier --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-weber/papier
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6w-karte weber.py karte1d --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-weber/karte1d
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6w-karte-fein weber.py karte1d --fein --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-weber/karte1d
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6w-feinv weber.py feinv1d --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-weber/feinv1d
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6w-feinv-fein weber.py feinv1d --fein --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-weber/feinv1d
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6w-2d weber.py winkel2d --geraet cuda --stufe beide --karte /home/fmh/fmhc-physics-remote/runde6-weber/karte1d/karte1d_grob_ergebnis.json --out /home/fmh/fmhc-physics-remote/runde6-weber/winkel2d
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r6w-l3-karte weber.py l3 --geraet cpu --a /home/fmh/fmhc-physics-remote/runde6-weber/karte1d/karte1d_grob_ergebnis.json --b /home/fmh/fmhc-physics-remote/runde6-weber/karte1d/karte1d_fein_ergebnis.json --out /home/fmh/fmhc-physics-remote/runde6-weber/l3-karte
cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r6w-l3-feinv weber.py l3 --geraet cpu --a /home/fmh/fmhc-physics-remote/runde6-weber/feinv1d/feinv1d_grob_ergebnis.json --b /home/fmh/fmhc-physics-remote/runde6-weber/feinv1d/feinv1d_fein_ergebnis.json --out /home/fmh/fmhc-physics-remote/runde6-weber/l3-feinv
```

- **Ausweichen:**
  - karte1d und feinv1d grob laufen auch auf cpu/cpu2 (`--geraet cpu`). Die feinen Laeufe und winkel2d nur auf einer
    P4000.
  - Rechnet der Rauchtest winkel2d ueber 9 min hoch, dann zwei Aufrufe mit `--stufe grob` und `--stufe fein` in
    verschiedene --out-Ordner. Der L3-Vergleich 2D faellt dann weg; von Hand aus beiden JSON vergleichen.
- Geschrieben wird erst am Ende eines Unterbefehls. Ein Abbruch durch RuntimeMaxSec verliert nur diesen Unterbefehl.

## 7. Laufzeit je Aufruf (Schaetzung, nicht gemessen)

Grundlage:
- RUNDE-03 auf der P4000: 2D etwa 5,6 ns je Punkt und Schritt, 2D-Schiessen etwa 60 s.
- RUNDE-02: 1D etwa 0,2 bis 0,3 ms je Verlet-Schritt, solange die Kernelstarts dominieren.
- CPU (ein Kern): 1D 40 bis 60 ns je Feldpunkt und Schritt.

| Aufruf | Laeufe x Punkte | Schritte | P4000 | CPU, 1 Kern | Spur |
|---|---|---|---|---|---|
| papier | Formeln | - | - | unter 5 s | cpu |
| karte1d grob | 8 x (18 x 4001) | 58500 | 0,5 bis 1 min | 3 bis 5 min | p4000a (oder cpu) |
| karte1d --fein | 8 x (18 x 8001) | 117000 | 1 bis 2 min | nicht auf CPU | p4000a |
| feinv1d grob | 54 x 4001 | 14500 | etwa 0,3 min | 2 bis 3 min | p4000a (oder cpu) |
| feinv1d --fein | 54 x 8001 | 29000 | etwa 0,5 bis 1 min | nicht auf CPU | p4000a |
| winkel2d beide | 9 x 280^2, 9 x 560^2 | 5600 und 11200 | etwa 4,5 min (60 s Schiessen, 25 s grob, 3 min fein) | nicht auf CPU | p4000a |
| l3 (je) | keine Rechnung | - | - | Sekunden | cpu |
| rauch (GPU, alle, x 0,05) | | | etwa 1,5 min (Schiessen dominiert) | | p4000a |

- **Zusammen** etwa 9 min auf p4000a, dazu Sekunden auf cpu.
- **Speicher:** Das groesste Feld ist winkel2d fein, 9 x 560^2 complex128 = 45 MB je Feld. Mit FFT- und
  Messzwischenwerten unter 1 GB. Die Schnappschuesse liegen auf der CPU (unter 50 MB).

## 8. Latten

- **L1 (kann scheitern):**
  - H scheitert, wenn
    - bis We = 4,1 kein Zerfall auftritt, oder
    - die We_c-Intervalle der drei Ballgroessen keinen gemeinsamen Bereich haben, oder
    - Zerfall nur als Fenster um v_cl auftritt, also als Spaltung.
  - G scheitert, wenn
    - v50/v_cl ausserhalb [0,9; 1,1] liegt, oder
    - an anziehenden Stufen bei v >= 0,25 gespalten oder zerspritzt wird.
  - V-2D-1 scheitert bei q_haupt < 0,85 bei richtiger Auswertung.
  - Der Bericht nennt das Urteil nach diesen Regeln.
- **L2 (Gegenprobe):**
  - V2 = 0 in 1D (24 Laeufe) und in 2D (2 Laeufe) ohne jeden Zerfall
  - Teilchenbild abseits von v_cl
  - Energiedrift
- **L3 (Numerik):**
  - dx und dt halbiert (1D ganze Karte und feinv1d; 2D alle 9 Laeufe)
  - Regeln in Abschnitt 4
  - Ein Zerfall, der sich bei feiner Aufloesung aendert, zaehlt nicht.
- **L4 (schon bekannt):**
  - Die Teilchenschwelle ist Energieerhaltung.
  - Solitonspaltung und Quantenreflexion an Stufen und Barrieren sind fuer NLS-Solitonen bekannt [L, aus dem
    Gedaechtnis].
  - Traegt G, ist das Ergebnis also bekannte Physik in unserem Modell und kein neuer Befund.
  - Neu waere nur ein Weber-Zerfall mit fester We_c.
- **L5 (Messbezug):**
  - Keiner direkt; das Ergebnis bleibt modellintern.
  - Analogien mit Messungen: Tropfenzerfall (We_c ≈ 12 im Luftstrom), BEC-Solitonen an Barrieren (85Rb, 7Li).
  - Ein Bezug waere erst gegeben, wenn das Modell eine messbare Groesse vorhersagt, die dort nicht schon folgt.

## Einfach gesagt

Wir pruefen, ob ein Q-Ball an einer Stufe zerplatzt wie ein Wassertropfen, der zu schnell aufprallt. Beim Tropfen
entscheidet die Weber-Zahl: Wucht gegen Oberflaechenspannung. Die Energie-Rechnung zeigt aber, dass der Ball aus
Runde 3 gar nicht genug Energie hatte, um zu zerfallen. Der gemessene Verlust war sehr wahrscheinlich ein Messfehler:
Der Ball war schon im Rand der Rechenbox verschwunden, und das Messfenster schaute danach auf Reste. Die neuen Rechnungen
werten richtig aus. Sie pruefen, ob es echten Zerfall gibt und ob er zur Weber-Zahl passt oder eher dazu, dass der Ball
knapp an der Stufenkante in zwei Teile geteilt wird, wie man es von Solitonen kennt.

Ende: 2026-09-30 03:03:03 CEST (gemessen). Beginn 02:35:12, also 28 min.
