# Runde 6: Zerspritzt ein Q-Ball wie ein Tropfen? Test mit der Weber-Zahl (Anthropic)

Auftraggeber: claude-primary. Zeit vor dem Schreiben gemessen: 2026-09-30 02:34:39 CEST. Deutsch. Explorativ.

Finn woertlich: "mach den tropfen-zerspritzen test mit der weber-zahl".

## Ausgangslage

- **Tropfenbild bestaetigt** (Runde 3, RUNDE-03/tests2d-r3/lauf-69/ausgabe/tropfen_bericht.txt): Ein grosser 2D-Q-Ball
  schwingt nach Rayleighs Tropfenformel, ohne freie Parameter, auf 3 bis 6 %.
- **Brechung** (RUNDE-03/tests2d-r3/lauf-69/ausgabe/brechung_bericht.txt, 2D, omega^2 = 0,7, v = 0,2, Potentialstufe
  V2 = -0,02 anziehend):
  - Schraeg (40 und 60 Grad zur Normalen) laeuft der Ball intakt durch und folgt Snellius auf 0,01 Grad.
  - Steil (0 und 20 Grad) verliert er im Messfenster 92 bis 94 % seiner Ladung.
  - Die Normalgeschwindigkeit ist dort 0,2 bzw. 0,188, bei 40 Grad 0,153.
  - Vermutung der Leitung: Er zerreisst oder spaltet sich (durchgelassener plus reflektierter Teil), sobald die Wucht
    senkrecht zur Stufe gross genug ist.
- **Code-Grundlagen:**
  - 2D: RUNDE-03/tests2d-r3/tests2d_r3.py (gelaufen; spektraler Laplace; Potentialstufe V(x)|psi|^2 im Unterbefehl
    brechung)
  - 1D: RUNDE-02/tests1d/tests1d.py (gelaufen)

## Hypothese (Karte)

- **H:** Ein Q-Ball, der eine Potentialstufe durchquert, zerfaellt genau dann (Hauptfragment mit weniger als 50 % der
  Ladung), wenn die Weber-Zahl der Normalbewegung We_n = rho v_n^2 D / sigma einen kritischen Wert We_c uebersteigt.
  - D ist der Balldurchmesser, sigma die Wandspannung, rho die Dichte.
  - Die Groessen sind vorab aus dem Profil festgelegt, wie im Tropfentest: sigma aus der Wandenergie, rho als
    Enthalpiedichte 2 omega^2 S.
- **Zu pruefen ist, ob We_c fuer verschiedene Ballgroessen gleich ist.** Sonst sagt die Weber-Zahl nichts.
- Moeglich ist, dass zusaetzlich die Stufentiefe als zweite dimensionslose Zahl zaehlt, etwa |V2| geteilt durch die
  Bindungsenergie je Ladung (1 - omega). Dann ist das Ergebnis eine Karte in zwei Zahlen.
- Zu unterscheiden: echtes Zerspritzen (mehrere Fragmente, Abstrahlung) gegen Aufspaltung in einen durchgelassenen und
  einen reflektierten Ball (bekannt fuer NLS-Solitonen an Stufen [L, aus dem Gedaechtnis]).

## Tests (je Aufruf hoechstens 10 min, Quadro P4000 oder CPU)

1. **1D-Karte, billig:**
   - omega^2 in {0,6, 0,7, 0,8}
   - Stufen V2 in {-0,01, -0,02, -0,04} (anziehend) und {+0,01, +0,02} (abstossend)
   - Geschwindigkeiten v in etwa 8 Werten von 0,05 bis 0,4
   - Ausgang: intakt durch, intakt reflektiert, gespalten (Ladung je Fragment), zerspritzt (viele Fragmente oder
     Strahlung)
   - Daraus die Schwelle v_c(omega, V2) und We_c = rho v_c^2 D / sigma.
   - Gegenprobe: V2 = 0 gibt bei keinem v einen Zerfall.
2. **2D-Winkelprobe:**
   - omega^2 = 0,7, V2 = -0,02, v = 0,2
   - Winkel 20, 25, 30, 35 und 40 Grad
   - Kritischer Winkel und daraus v_n,c. Vergleich mit der 1D-Schwelle bei gleichem omega und V2.
3. **Aufloesung (L3):** halbes dx und dt bei den Schwellenlaeufen.

## Vorhersage vorab (in PLAN.md vor dem Rechnen)

- Herleitung aus dem Tropfenbild, soweit moeglich: Bei welcher Normalgeschwindigkeit reicht die Wucht, um die
  Oberflaechenenergie zu ueberwinden?
- Dazu die Gegenhypothese "Solitonspaltung an der Stufe" mit ihrer eigenen Vorhersage.
- Sag vorab, woran man beide unterscheidet.

## Abgabe (Ordner RUNDE-06/weber/)

- Code (--geraet cuda|cpu, float64, Unterbefehle, Rauchtest)
- PLAN.md mit Aufrufen ueber `cd /home/fmh/fmhc-physics-remote/runde6-weber && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
  <spur> <kurzname> <skript> ...`, Laufzeiten, Vorhersagen, Gegenproben, Latten L1 bis L5, "Einfach gesagt"
- Nicht rechnen; die Leitung startet.

## Grenzen

- Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik. Der Code bleibt ungetestet; halte ihn einfach.
- Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
- Gesperrt: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
- Zeiten mit `date`. Budget hoechstens 75 Minuten.
