# Runde 6, Reflexion: Laufplan fuer die Karten R-1 bis R-5

Karten: ../KARTEN-REFLEXION-STABILISIERT.md (Finn: "wie kann reflexion in diesem kontext ggf auf andere sachen wirken
und die stabilisieren?"). Arbeitsweise v3 (../../README.md), Latten L1 bis L5.

Bearbeiter: Agent (Anthropic, Opus). Beginn 2026-09-30 02:23:00 CEST (gemessen). PLAN.md begonnen 03:01:04 CEST
(gemessen). Ende in der letzten Zeile.

Status: Code geschrieben. Lokal nur py_compile, Rauchtest und kurze Proben (Freigabe Finn 02:42, CPU, 1 Faden, je
hoechstens 120 s). Die Messlaeufe startet die Leitung auf der .69. Explorativ.

## Kurzfassung

- **Code:** reflexion.py. Unterbefehle r1, r2, r2zeit, r3, r4, r5, rauch; `--geraet cpu|cuda`; float64/complex128.
  Nur torch. Schreibt nur in `--out`.
- **Zwei Werkzeuge:**
  - **Linear, fuer R-1, R-2, R-3, R-5 und die Spiegelprobe von R-4.**
    - Einzelball: Zweikanal-Stoerungs-ODE wie Codex (resonance-20260930/linear/run.py), RK4 mit festem Schritt,
      Anschluss bei x = 4. Daraus je Paritaet die S-Matrix S_p(nu).
    - Mehrere Baelle: exakte Vielfachstreuung im offenen Kanal (Foldy-Lax).
    - Pole: Nullstellen von det K(nu), Newton mit tr(K^-1 K'). Abklingrate = -Im nu, in Einheiten
      Gamma0 = 6,716e-5.
  - **Zeit, fuer R-2 in der vollen nichtlinearen Dynamik und fuer R-4.**
    - Aus tests1d.py unveraendert: Velocity-Verlet mit dx = 0,1 und dt = 0,05 (fein beide halbiert), Daempfungsschicht
      (sigma0 = 1, 40 breit), Box [-150, 150].
    - Neu nur: Rand ohne Schwamm, Ring und grosse Box (fuer R-4) sowie die Anregung durch ladungserhaltende Streckung
      (siehe unten).
- **Anker (K0):** Der Einzelpol muss Codex treffen, rho = 1,49377696454877 - 6,71596847535e-5 i, mit |d rho| <= 1e-7.
  - Rauchtest (grobe Probe-Numerik h = 0,02, R = 20, 16 Kreispunkte): |d rho| = 2,6e-11, |d Im|/Gamma0 = 9,4e-8.
  - Direkter ODE-Rest am Pol: 7,7e-17.
- **Ergebnis-Dateien je Aufruf:** reflexion_<unterbefehl>_bericht.txt (auch auf stdout) und
  reflexion_<unterbefehl>_ergebnis.json. Die JSON enthaelt alle Pole, Gewichte, Kraftkurven und Huellen.

## 1. Aufrufe (Leitung, auf der .69 ueber kleintest.sh)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde6-reflexion/ mit reflexion.py darin (nur diese Datei kopieren).

**Rauchtest**, je Geraet einmal (lokal gemessen 34 s auf einem Laptop-Kern):

```
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r6-rauch-cpu reflexion.py rauch --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-reflexion/rauch-cpu
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6-rauch-gpu reflexion.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-reflexion/rauch-cuda
```

**Hauptlaeufe**, nur nach Rauchtest mit rc = 0 auf dem jeweiligen Geraet:

```
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r6-r2 reflexion.py r2 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-reflexion/ausgabe-r2
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r6-r1 reflexion.py r1 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-reflexion/ausgabe-r1
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r6-r3 reflexion.py r3 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-reflexion/ausgabe-r3
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r6-r5 reflexion.py r5 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde6-reflexion/ausgabe-r5
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6-r2zeit reflexion.py r2zeit --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-reflexion/ausgabe-r2zeit
cd /home/fmh/fmhc-physics-remote/runde6-reflexion && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r6-r4 reflexion.py r4 --geraet cuda --out /home/fmh/fmhc-physics-remote/runde6-reflexion/ausgabe-r4
```

- Reihenfolge: r2 zuerst, denn R-1, R-3 und r2zeit benutzen denselben dunklen Abstand. Jeder Aufruf rechnet ihn
  aber selbst neu und ist damit eigenstaendig.
- Auf einer cpu-Spur immer `--geraet cpu`, weil kleintest.sh dort CUDA_VISIBLE_DEVICES leer setzt.
- r2zeit und r4 laufen nacheinander auf p4000a (Lock der Spur). Ist p4000a lange belegt, geht r4 auch auf eine
  cpu-Spur mit `--geraet cpu`; unter Last kann dann die feine Stufe an der Sicherung scheitern (Hinweis im Bericht).
- **Sicherung:**
  - Nach 540 s werden laufende Zeitentwicklungen gekuerzt; fehlt die Zeit fuer die feine Stufe, entfaellt sie.
  - Lineare Anordnungen werden ab 25 s Restzeit uebersprungen.
  - Alles steht dann unter "Hinweise" im Bericht; Bericht und JSON entstehen trotzdem.
- **Ausweg, falls r1 oder r5 die Sicherung ausloesen:** zwei Aufrufe mit `--stufen grob` und `--stufen fein`. L3 dann
  aus den beiden JSON-Dateien vergleichen.
- Lokale Proben benutzen zusaetzlich `--T` (kuerzere Zeitteile) und `--stufen grob`; fuer die Messlaeufe nicht
  setzen.

## 2. Laufzeiten

Gemessen lokal (Laptop, 1 Faden, nice 19; Rauchtest `rauch --geraet cpu`, 03:00):

| Teil | Rauchtest | Inhalt des Rauchtests |
|---|---|---|
| r1 | 1,8 s | Tabelle 16 Punkte, h = 0,02; Ketten M = 1, 2 |
| r2 | 1,7 s | 3 + 2 Abstaende, Goldener Schnitt 12 Schritte |
| r2zeit | 14,5 s | T = 75; grob 1,65 ms je Schritt (11 x 3001), fein 3,68 ms (11 x 6001) |
| r3 | 2,3 s | 3 Abstaende, 3 + 2 Frequenzen |
| r4 | 11,5 s | T = 75; box/ring/gross grob 0,64/0,40/0,66 ms je Schritt, fein 1,19/0,57/0,94 ms |
| r5 | 1,8 s | N = 2, ein Seed |
| gesamt | 33,6 s | zweiter Lauf 03:05 unter Laptop-Last: 67,0 s (r2zeit 33,2 s, r4 22,3 s), rc = 0 |

Dazu zwei lokale Proben mit T = 600, nur grob (03:03 bis 03:04, nach dem Festschreiben der Vorhersagen in Abschnitt 5):

| Teil | Dauer | ms je Schritt |
|---|---|---|
| r4 | 31,3 s | box 0,81; ring 0,51; gross 0,90 |
| r2zeit | 28,7 s | 2,15 (11 x 3001) |

Hochrechnung fuer die vollen Aufrufe (je hoechstens 10 min). Grundlage sind die Probe-Werte je Schritt und das
Verhaeltnis fein/grob aus dem Rauchtest:

- **r2zeit:** T = 1500, grob 30 000 und fein 60 000 Schritte.
  - Laptop-CPU: 30 000 x 2,15 ms + 60 000 x 4,8 ms = 65 s + 288 s, mit Vorlauf etwa 6 min. Auf einer langsameren CPU
    wird es eng; die Sicherung liefert dann grob allein.
  - P4000: etwa 1 ms je Schritt (RUNDE-02, lauf-69), also 30 s + 60 s, mit Vorlauf etwa 2 min. Deshalb steht r2zeit
    auf p4000a.
- **r4:** grob 3 x 30 000, fein 3 x 60 000 Schritte.
  - Laptop-CPU: 24 + 15 + 27 s grob, 90 + 44 + 77 s fein, zusammen etwa 4,7 min; unter Last bis Faktor 2 mehr.
    Deshalb auf p4000a, CPU nur als Ausweg.
  - Auf der P4000 laut Startkosten ~1 ms je Schritt ebenfalls etwa 4,5 min.
- **Lineare Teile:** Die Tabelle braucht grob 2400 RK4-Schritte mit 32 Kreispunkten, fein 6400 (Rauchtest 1000 mit
  16). Das ergibt etwa 3 bis 10 s je Tabelle, mit 11 Balltypen (r5) bis etwa 20 s.
  - Newton-Aufwand: waechst mit der Ballzahl bis N = 41 (Matrix 82 x 82). Nicht lokal gemessen, denn grosse
    Anordnungen waeren schon Messlaeufe. Rauchtest: etwa 0,15 s je Anordnung mit 5 Baellen; linear hochgerechnet mit
    Faktor 2 fuer die groessere Matrix: etwa 3 s je Anordnung mit 41 Baellen, bei entarteten dunklen Polen (langsames
    Newton) bis etwa 10 s.
  - Schaetzung: r2 unter 1 min, r3 unter 1 min, r1 1 bis 4 min, r5 2 bis 6 min.
- Speicher: unter 0,1 GB.

## 3. Warum linear (Begruendung)

- **Die Rate ist klein.** Gamma0 = 6,7e-5 heisst Abklingzeit 1/Gamma0 = 14 900. Eine Zeitrechnung von 10 min kommt bis
  T ~ 1500, dort faellt die Amplitude nur um 10 %.
  - Eine unterdrueckte Rate (etwa 1e-3 Gamma0) ist dort nicht messbar.
  - Ein Pol liefert die Rate direkt, bis auf ~1e-9 Gamma0 genau (Anker oben).
- **Stationaere Zustaende brauchen lange Zeit.**
  - Eine resonant gepumpte Anordnung (R-3) erreicht ihren stationaeren Zustand erst nach t >> 1/Gamma0.
  - Die Bandbreite eines Pakets in einer Box von 300 ist >> Gamma0. Also kann nur die lineare Rechnung R-3 bei
    Resonanz beantworten.
- **Die Vielfachstreuung ist fuer d >= 30 exakt bis auf e^-22.** Vernachlaessigt werden nur:
  - die Kopplung ueber den geschlossenen Kanal, ~ e^{-0,754 d} = 1,5e-10 bei d = 30
  - die Ueberlappung der Auslaeufer, ~ e^{-0,548 d} = 7e-8
  - Beides liegt weit unter Gamma0.
  - Die Einzelball-Funktionen sind exakt (ODE), inklusive des Hintergrunds (gerader Hintergrund und ungerader Kanal).
- **Die Zeitrechnung bleibt als Gegenprobe in der vollen Dynamik (r2zeit).** Dort zeigt sich, ob die Aussage "dunkel
  gegen hell" auch mit nichtlinearer Dynamik, Gitter und Daempfungsschicht gilt (Faktor >= 7 zwischen den Raten in
  T = 1500 messbar).

## 4. Aufbau je Karte (vor dem Lauf festgelegt)

Gemeinsam fuer alle Karten:
- Balltyp 0 ist omega^2 = 0,7.
- Tabelle der Einzelball-Funktionen auf dem Kreis |nu - nu_c| = 0,03 um nu_c = omega + 1,49378; gueltig bis 0,012.
- Numerik grob: h = 0,01, R = 24. Numerik fein: h = 0,005, R = 32 (L3).
- Markov-Modell (Saat und Vergleich), in geraden Streuamplituden E_j:
  - H_jj = nu1_j
  - H_ji = -i g_j e^{2 i delta_e} e^{i k |x_i - x_j|} prod t_bg (Baelle dazwischen)
  - Hintergrundphase e^{2 i delta_e} = -S_e(nu_r); Hintergrund-Durchgang t_bg = (e^{2 i delta_e} + S_o)/2
- Weitere Saaten aus der um nu_r linearisierten Foldy-Lax-Matrix, dann Newton, doppelte Pole (Abstand < 1e-9)
  zusammengefasst.
- Ueberleben einer Anregung des Mittelballs, zwei Wege:
  - exakt als Polsumme der Residuen von [K^-1] am Mittelball, normiert auf den Einzelball
  - Pruefzahl Summenregel: Summe der Residuen / Einzelresiduum, soll 1 sein
  - zum Vergleich im Markov-Modell (Mittelball allein und alle Baelle)

**R-1 (`r1`).**
- Mittelball bei 0, je M = 1, 2, 5, 10, 20 Kettenbaelle links und rechts.
- Vier Arme:
  - `luecke_bragg`: gleiche Baelle, Abstand d_B = exakter dunkler Zwei-Ball-Abstand nahe 36 (Anti-Modus). Im
    Markov-Bild ist das die Bragg-Bedingung k d + 2 delta_e = 2 pi n.
  - `verstimmt_lambda8`: d_B + lambda/8.
  - `ohne_luecke_antibragg`: d_B + lambda/4.
  - `nichtresonant_bragg`: Kettenbaelle omega^2 = 0,6, Abstand d_B. Ihr eigener Pol liegt ausserhalb der Tabelle, bei
    nu0 streuen sie nur schwach. Das ist die echte (nichtresonante) Bragg-Luecke.
- Gemessen: alle Pole, Gamma_min, Gamma des Pols mit groesstem Mittelgewicht, Zahl dunkler Pole (< 0,01), Ueberleben
  bei 1, 5, 20 x 1/Gamma0, |r(nu0)| des 0,6-Balls.

**R-2 (`r2`, linear).**
- Zwei Baelle 0,7 bei -d/2, +d/2.
- Dunkle Abstaende nahe 36 fuer den Anti- und den Sym-Modus: Goldener Schnitt, 40 Schritte, in +-lambda/4 um die
  Markov-Stelle.
- Abtastung einer Periode: 11 Werte d = 34,5 + j lambda/10. Weite Abtastung: d = 20 bis 60 in Schritten von 4.
- Je d: beide Pole, Modus aus den Amplituden (sym/anti), Frequenzverschiebung, Markov-Werte 1 +- cos(k d + phi).
- Gegenprobe: Partner omega^2 = 0,69 (Einzelpol 0,016 = 240 Gamma0 verstimmt) an denselben 11 Abstaenden.

**R-2 in der Zeit (`r2zeit`).**
- Abstaende dS, dA (dunkel sym bzw. anti, linear berechnet, Numerik grob) und dM = (dS + dA)/2.
- Je Abstand drei Laeufe:
  - `sym`: beide Baelle gestreckt, lam = 1 + 1e-3
  - `anti`: links 1 + 1e-3, rechts 1 - 1e-3
  - `ref`: ungestreckt
- Dazu ein einzelner Ball, gestreckt und als Referenz. Zusammen 11 Laeufe, T = 1500.
- Die Streckung haelt die Ladung fest. Ein Stoss (psi mal 1,001) wuerde die Ladung aendern und die beiden Baelle um
  ~5e-4 >> Gamma0 gegeneinander verstimmen; der dunkle Zustand braucht gleiche Baelle.
- Messung: |psi|^2 in beiden Ballmitten alle 0,5.
  - Atemfrequenz: FFT-Spitze des Einzelballs in [1,3; 1,7].
  - Demodulation: Hann-Fenster 100, Schritt 50, Referenz komplex abgezogen.
  - Projektion (A1 +- A2)/2, Gerade durch ln|A| ab t = 200.
- Gleiche Phase beider Baelle: Die Auslaeuferkraft bei d = 36 ist 6e-9. Die Verschiebung bis T = 1500 ist ~ 3e-3,
  gebraucht wird < 0,05.

**R-3 (`r3`).**
- Zwei Baelle 0,7, Abstand d = 30 bis 33 in Schritten von 0,05 (61 Werte, eine Wellenlaenge).
- Pumpe mit reeller Frequenz:
  - Re nu1 + j Gamma0 mit j = -3, -1, 0, 1, 3
  - nicht resonant 2,25 und 2,10
- Zwei Pumpformen: nur von links; von beiden Seiten (stehende Welle).
- Kraft je Ball aus dem Impulsfluss T_xx = 2 k^2 (|A|^2 + |B|^2), links minus rechts, je Pumpamplitude^2.
  - F_rel = F_rechts - F_links (> 0 treibt auseinander)
  - stabile Gleichgewichte: Vorzeichenwechsel + nach -
  - Anpassung an cos/sin(k d) und cos/sin(2 k d)
- Linear gueltige Pumpe eps_lin: Die innere Stoeramplitude (Kernverstaerkung G mal einlaufende Amplitude) bleibt
  <= 1 % von f(0). Dazu F bei eps_lin und der Abstand d_x, ab dem diese Kraft die Auslaeuferkraft uebersteigt.
- Gegenprobe ohne Pumpe: Auslaeuferkraft 16 a0^2/b0 e^{-sqrt(a0) d}, gleichphasig anziehend (Papier: Impulsfluss in
  der Mitte).
- Zusatz "gespeist aus der Resonanz": Kraft aus dem Eigenfeld der beiden Moden am dunklen Abstand und bei dM.

**R-4 (`r4`).**
- Einzelball 0,7, gestreckt und Referenz. Vier Raender:
  - `schwamm`: Standard
  - `spiegel`: fester Rand bei +-150 ohne Schwamm
  - `ring`: periodisch, Laenge 300
  - `gross`: Box +-300, Schwamm ab 260
- T = 1500. Rueckkehrzeit der Abstrahlung 2 L/v_g = 332.
- Fit ab t = 200, dazu getrennt vor (200 bis 332) und nach der Rueckkehr.
- Linear: Ball zwischen zwei festen Spiegeln bei +-150 (Spiegel als Streuer mit r = -1, t = 0). Alle Pole nahe nu0.

**R-5 (`r5`).**
- Mittelball bei 0, je N = 2, 5, 10, 20 Gasbaelle links und rechts, Abstaende gleichverteilt in [30, 45], Seeds 1 bis
  5.
- Zwei Arten:
  - `gleich`: alle 0,7
  - `gemischt`: omega^2 zufaellig aus {0,65 ... 0,75} ohne 0,70
- Gegenprobe: periodisch mit Abstand 37,5 (nicht abgestimmt) und der Einzelball.
- Gemessen je Anordnung wie R-1; Mediane ueber die Seeds.

## 5. Vorhersagen

**Herkunft und Offenlegung.**
- Die Vorhersagen V... stammen aus der Planung vor dem Rauchtest (02:23 bis 02:50, Markov-Bild ohne Hintergrundphase)
  und wurden danach nicht angepasst. Nur die Schwellen sind hier ausgeschrieben.
- Der Rauchtest (02:53 bis 02:58, grobe Probe-Numerik, kleine Anordnungen) war vor dem Festschreiben sichtbar. Seine
  Befunde stehen getrennt in Abschnitt 6.
- Wo er eine Vorhersage schon beruehrt, ist das vermerkt ("[R: ...]"). Offen und entscheidend bleiben die grossen
  Anordnungen, die feine Numerik und die Zeitrechnungen.
- Zeitteile (r2zeit, r4): Vorhersagen festgeschrieben vor jeder Zeitrechnung ueber T = 75.

**R-1.**
- V1a (luecke_bragg): Fuer jedes M haben N - 1 von N Polen Gamma < 0,01, ein Pol hat Gamma = N +- 20 %. Markov: Die
  Kopplungsmatrix hat bei Bragg-Abstand Rang 1. [R: M = 1, 2 erfuellt]
- V1b: Ueberleben der Mittelanregung (Polsumme) bei 5/Gamma0 >= 0,1 fuer alle M; allein e^-10 = 4,5e-5. Markov-Grenze
  (1 - 1/N)^2. [R: M = 1, 2: 0,34 und 0,49]
- V1c (ohne_luecke_antibragg, gleiche Ballzahl): Ueberleben bei 20/Gamma0 mindestens 10-mal kleiner als in der
  Bragg-Kette, fuer M >= 2. Unsicher, weil Anti-Bragg-Ketten subradiante Moden ~ Gamma/N^2 haben.
- V1d (nichtresonant_bragg, 0,6): Gamma_c in [0,9; 1,1] fuer alle M <= 20. Grund: Ein nichtresonanter Ball reflektiert
  bei nu0 nur |r| ~ 1e-2; eine Bragg-Luecke braucht M ~ 1/|r|. [R: |r| = 8,1e-3, M = 1, 2: 1,002 und 1,006]
- V1e: Summenregel 1 +- 0,05, sonst ist die Polsumme nicht verlaesslich (moeglich bei Entartung in langen Ketten). Dann
  zaehlt das Markov-Ueberleben mit Pruefzahl "Markov-exakt".

**R-2 (linear).**
- V2a: Je Periode lambda = 2,985 gibt es einen Abstand mit dunklem Anti-Modus und einen mit dunklem Sym-Modus, lambda/2
  auseinander. [R: erfuellt, dA = 35,350, dS = 36,842]
- V2b: Gamma am dunklen Abstand <= 1e-3, in grob und fein (Markov: exakt 0). [R: 1,8e-8]
- V2c: Der helle Partner hat 2,00 +- 0,05.
- V2d (vor dem Rauchtest): Der dunkle Anti-Abstand liegt bei k d = 2 pi n (Markov ohne Phase), also bei 35,819.
  **[R: gescheitert.]** Er liegt 0,469 tiefer, wegen der Hintergrundphase 2 delta_e = 0,987 des Balls. Das ist eine
  gemessene Eigenschaft von S_e, keine Anpassung. Die Formel Gamma = 1 +- cos(k d + 2 delta_e) wird im Lauf ueber
  d = 20 bis 60 geprueft; Schwelle 0,05.
- V2e (Gegenprobe, Partner 0,69): Mittelball Gamma = 1 +- 0,02 bei allen d, kein dunkler Zustand.
  [R: 0,996 bis 1,002]

**R-2 in der Zeit (festgeschrieben vor jeder Zeitrechnung ueber T = 75).**
- V2z-a: Einzelball Gamma_fit = 1,00 +- 0,10, grob und fein.
  - Abbruchkriterium: Trifft er das nicht, ist die Messmethode (Fenster, Fit) nicht tragfaehig.
  - Dann R-2-Zeit und R-4 nicht werten.
- V2z-b: Dunkle Anregung (dA/anti, dS/sym): Gamma_fit <= 0,15. Hell (dA/sym, dS/anti): 2,0 +- 0,3. Bei dM beide
  1,0 +- 0,3.
- V2z-c (L3): Gamma_fit der dunklen Anregung aendert sich grob -> fein um <= 0,1.
  - Grund: Die Gitterdispersion verschiebt k d bei d = 36 grob um ~0,13 rad; das gibt Gamma_dunkel ~ 0,01.

**R-3.**
- V3a: F_rel(d) hat seinen Hauptanteil bei 2k (Periode lambda/2): Amp_2k > Amp_k fuer alle nu und Pumpen.
- V3b: Stabile Gleichgewichte (wo es sie gibt) liegen lambda/2 +- 5 % auseinander.
- V3c: Bei linear gueltiger Pumpe eps_lin gilt |F_rel| <= 1e-7 fuer alle nu. Der Abstand d_x, ab dem Strahlung die
  gleichphasige Auslaeuferkraft uebersteigt, liegt zwischen 30 und 45. [R: 1e-10 bis 8e-8; d_x 32 bis 45]
  - Bedeutung, falls erfuellt: Strahlungsbindung existiert, ist aber 1e-8 schwach. Die Mulden sind ~ 1e-9 tief. Kein
    Weg zur Paarbindung.
- V3d: Nicht resonant (2,25 und 2,10), Pumpe nur von links: max|F_rel| <= 1e-3 je eps^2 (~ |r|^2).
  [R: 2,8e-5 und 2,7e-6]
- V3e: Eigenfeld des dunklen Modus stoesst ab (F_rel > 0; Licht zwischen zwei Spiegeln drueckt sie auseinander).
  [R: +22,9 je |E|^2]

**R-4 (festgeschrieben vor jeder Zeitrechnung ueber T = 75).**
- V4a (schwamm): Gamma_fit = 1,00 +- 0,10.
- V4b (gross): |Gamma_gross - Gamma_schwamm| <= 0,05.
- V4c (spiegel, ring): |Gamma_fit| <= 0,3 ueber 200 bis 1500. Das heisst: Mit reflektierendem Rand scheint der Ball
  mindestens dreimal laenger zu leben.
  - Vor der Rueckkehr (200 bis 332): Gamma ~ 1 +- 0,5 (nur 3 Fenster).
- V4d (linear): Ball zwischen Spiegeln, alle Pole nahe nu0 mit |Im nu| <= 1e-10. [R: 3e-19]

**R-5.**
- V5a (gleich): Median-Ueberleben (Polsumme) bei 5/Gamma0 >= 1e-2 fuer alle N; Median Gamma_min <= 0,01.
  [R: N = 2: 0,20 und 1,3e-6]
- V5b (gemischt): Median Gamma_c in [0,9; 1,1]; Median-Ueberleben innerhalb Faktor 2 von 4,5e-5.
  [R: N = 2: 1,006 und 4,3e-5]
- V5c (gleich): Median Gamma_min faellt monoton mit N (2, 5, 10, 20). Das waere die Lokalisierung.
- V5d (periodisch 37,5): Ueberleben zwischen gemischt und gleich.

## 6. Rauchtest-Befund (sichtbar vor dem Festschreiben; grobe Probe-Numerik, keine Wertung)

- Anker bestanden (siehe oben).
- **Hintergrundphase.** Der Ball hat bei nu0 die gerade Hintergrundphase 2 delta_e = 0,987. Sie verschiebt alle
  Interferenzbedingungen um 0,469 im Abstand.
  - Das naive Markov-Modell ohne diese Phase lag um ~2 Gamma0 neben den exakten Polen.
  - Mit Phase und Hintergrund-Durchgang: 0,01 bis 0,1 Gamma0.
  - Der Code benutzt seitdem das Modell mit Phase (Saat und Vergleich); die Pole kommen immer aus der exakten
    Rechnung.
- R-1 (M = 1, 2) und R-5 (N = 2): Die exakte Polsumme weicht deutlich vom Markov-Ueberleben ab (0,34 gegen 0,44 bei
  M = 1). Die Summenregel ist 0,99 bis 1,015. Zaehlen soll die Polsumme.
- R-3 bei Resonanz: Ein einzelner Ball reflektiert vollstaendig (|r| = 1,000 bei Re nu1). Das ist die bekannte
  Fano-Totalreflexion eines schmalen Resonators, Breite Gamma0.
- Zeitteile mit T = 75: nur Durchlaufprobe; Gamma_fit ~ 20 ist die Anlaufphase, keine Aussage.

**Lokale Probe T = 600, nur grob.** Sie lief 03:03 bis 03:04, nach dem Festschreiben von Abschnitt 5 um 03:01. Zweck:
Fenster und Fit ueber die Rueckkehrzeit 332 hinaus pruefen. Keine Wertung; die Messlaeufe haben T = 1500 und die feine
Stufe. Werte in Gamma0:
- r2zeit, Probe: einzel 1,012; dunkel 0,0014 (dS/sym) und 0,0052 (dA/anti); hell 2,027 und 2,024; dM 0,919 und 1,098.
  - Die lineare Kontinuumsrechnung sagt 0 / 2,005 / 0,997.
  - Die volle Zeitentwicklung folgt also in der Probe dem linearen Bild.
- r4, Probe:
  - schwamm 1,012 und gross 1,012 (gleich bis 1e-4)
  - spiegel -0,008 ueber 200 bis 600
  - ring 2,02 ueber 200 bis 600: Nach der ersten Rueckkehr verstaerkt die zurueckkehrende Welle hier die Abnahme.
  - V4c (|Gamma| <= 0,3 fuer den Ring ueber 200 bis 1500) kann damit scheitern; das entscheidet der Messlauf.
- Die linearen Pole am dunklen Abstand haben |Gamma| ~ 1e-9 mit beliebigem Vorzeichen. Das ist die Rechengenauigkeit
  der Tabelle (~1e-13 in nu), kein Anwachsen.

**Schwache L1-Stellen (ehrlich).**
- V2d prueft zwei Fernfeld-Rechnungen gegeneinander (Markov mit Phase gegen exakte Vielfachstreuung). Beide kennen kein
  Nahfeld; die Abweichung kann nur aus Laufzeit (Gamma d/v_g ~ 5e-3) und Hintergrundstreuung (|r| ~ 1e-3) kommen. Sie
  kann kaum scheitern; sie ist eine Numerikpruefung.
- V4d (Pole zwischen verlustfreien Spiegeln reell) folgt aus der Energieerhaltung; auch das ist eine Numerikpruefung.
- Echte L1-Stellen: V1a bis V1d, V2b, V2e, alle V2z, V3a bis V3e, V4a bis V4c, alle V5.

## 7. Latten je Karte

| Karte | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| R-1 | V1a bis V1d mit Schwellen | Anti-Bragg, lambda/8, nichtresonante Kette, Einzelball | h und R: grob gegen fein; Summenregel | ja: Subradianz und Bragg-Atomgitter im Wellenleiter (Wellenleiter-QED) | keiner direkt |
| R-2 | V2a bis V2e, V2z | Partner 0,69; Einzelball; dM | grob gegen fein; Zeit: dx, dt halbiert | ja: Friedrich-Wintgen, gebundene Zustaende im Kontinuum | keiner direkt |
| R-3 | V3a bis V3e | ohne Pumpe (Auslaeufer), nicht resonant | grob gegen fein (max F_rel) | ja: optisches Binden | keiner direkt |
| R-4 | V4a bis V4d | Schwamm gegen gross | dx, dt halbiert | ja: Methodenwissen (Randreflexion) | betrifft alle unsere Lebensdauerzahlen |
| R-5 | V5a bis V5d | gemischt, periodisch, Einzelball | grob gegen fein (Median Gamma_c) | ja: Anderson-Lokalisierung von Polaritonen | keiner direkt |

Zu L4: Die Mechanismen sind Standardphysik aus Optik und Quantenoptik. Neu ist nur, dass der Q-Ball genau so ein
schmaler Resonator mit einem offenen Kanal ist. Einordnung nach der Rechnung, als Hypothese.

## 8. Grenzen und Hinweise

- Die linearen Rechnungen halten die Baelle fest.
  - Echte Baelle ziehen sich ueber die Auslaeufer an: bei d = 36 mit 6e-9, bei d = 30 mit 3e-7.
  - Ein dunkler Zustand bleibt nur dunkel, solange der Abstand auf ~0,05 genau bleibt: Gamma_dunkel ~ (k dd)^2/2.
  - Fuer Lebensdauern >> 1e4 braucht es also groessere Abstaende oder Phasen, die die Auslaeuferkraft aufheben
    (Phasendifferenz pi/2; nicht gerechnet).
- Der dunkle Zustand braucht gleiche Baelle. Schon omega^2 0,69 statt 0,70 (240 Gamma0 verstimmt) hebt ihn auf (V2e).
- Die Pumpe in R-3 ist eine Annahme von aussen. Ohne Pumpe bleibt nur das Eigenfeld der zerfallenden Mode.
- Die Polsumme kann bei stark entarteten dunklen Polen (lange Bragg-Ketten) unvollstaendig sein. Pruefzahl ist die
  Summenregel.
- Eine synthetische Kontrolle ist keine Messdatenbestaetigung. Alle Aussagen gelten fuer das 1D-Modell.

## 9. Lokale Ausgaben (nur Durchlauf- und Formproben)

Alles in lauf-lokal/:
- rauch/: erster Rauchtest 02:53. Enthielt den Schluesselfehler in R-5 (Feld N ueberschrieben) und das Markov-Modell
  ohne Hintergrundphase; beides danach behoben.
- rauch-final/ und rauch-final.log: letzter Rauchtest 03:05 bis 03:06, rc = 0, keine Fehler.
- probe-r4-T600/ und probe-r2zeit-T600/: Zeitproben, siehe Abschnitt 6.

Das sind keine Messergebnisse. Die Messlaeufe nach Abschnitt 1 startet die Leitung.

## Einfach gesagt

Ein Q-Ball klingt nach wie eine Glocke und verliert dabei ganz langsam Energie nach aussen. Zwei gleiche Glocken im
richtigen Abstand koennen so zusammen schwingen, dass sich ihre Abstrahlung genau ausloescht; dann klingen sie fast
ewig. Eine Reihe solcher Glocken schuetzt eine Glocke in der Mitte auf dieselbe Weise, eine Reihe anderer Glocken
dagegen kaum. Wir pruefen das mit einer schnellen Rechnung ueber die Eigenschwingungen und einmal mit der vollen
Zeitrechnung. Und wir pruefen, wie stark ein spiegelnder Rand der Rechenbox einen Ball kuenstlich lange leben laesst.

Ende 2026-09-30 03:07:16 CEST (gemessen vor dem Schreiben dieser Zeile).
