# PLAN BAD-TAKT (Runde 23), Code-Agent im Auftrag der Leitung claude-primary

- Geschrieben 2026-10-02 ab 22:44:48 CEST (date), nach dem Rauchlauf, vor jedem echten Lauf und jedem Literaturabruf.
- Karte: KARTE.md mit dem Nachtrag der Leitung (22:29:33), unveraendert. BT1 bis BT4, Wahrscheinlichkeiten und
  Bedeutung gelten wie auf der Karte.
- Alles, was nicht woertlich auf der Karte oder im Auftrag steht, ist als **[Zusatz CA]** markiert.

## Code

- Neues Skript code/badtakt1d.py, sha256 4a38fcc0d1236769c68f310eff552d91308250ea2b627fcaaca5009f3bd53f0e.
  Auf der .69 bitgleich unter /home/fmh/fmhc-physics-remote/runde23-bad-takt/badtakt1d.py.
- Grundlage RUNDE-23/schwebungsuhr/code/schwebung1d.py (sha256 bd0fd1b7...c45, unveraendert).
  - Mit gleicher Rechenvorschrift uebernommen: M1 in 1D, U = S - S^2 + S^3/2; Leapfrog dt = 0,4 dx; Startschritt
    f exp(+i w_d dt); diskrete Newton-Profile; Daempfungsschicht (SIGMA0 = 1 quadratisch, Breite 60); Ladungsdichte
    rho = -2 Im(conj(psi) psi_t) mit zentrierter Zeitableitung; parabolische Maximumslage; Phase aus linear
    interpoliertem psi.
  - Neu: drei Baelle, Amplitudenfaktor, Startphasen, Randwahl, Abschnitte mit Zwischenstand (npz, atomar ersetzt),
    Messreihen, Fensterauswertung und Urteile (Modus auswerten, Funktion urteile).
- Die Auswertung steckt im selben Skript; es gibt kein zweites Auswerteskript.

## Rauchlauf (vor dem Einfrieren, nicht gewertet)

- 22:39 bis 22:44 CEST, .69, Spuren cpu bis cpu4. Ausgaben nur auf der .69 unter rauch/.
- Absichtlich Parameter, die in keinem echten Lauf vorkommen:
  - R1: refl, omega^2 = 0,57 / 0,61 / 0,65, D = 17, L = 45, Amplitude x 1,05, Phasen 0, dx 0,1, T = 800
  - R2: wie R1, aber in zwei Abschnitten (400 + 400)
  - R3: wie R1, Rand abs
  - R4: refl, Amplitude x 1,0, D = 30, L = 75, T = 300 (Stationaritaet)
- Befunde:
  - **Abschnitte:** R1 und R2 sind bitgleich (psi, old, alle Messreihen, Bilder, Energie).
  - **Erhaltung (refl):** Ladung auf 1e-14 relativ. Energie auf 4e-6 (angeregt) bzw. 2,6e-11 (unangeregt).
  - **R4 unangeregt:** Die Fenster-omega treffen omega_d auf 1e-7, Q bleibt auf 1e-6 konstant. Messkette und
    Phasenvorzeichen stimmen also.
  - **Anregung x 1,05:** Die Baelle behalten den Grossteil der Zusatzladung (Q_i etwa 1,10 x frei). Die Takte liegen
    im ersten Fenster um 2,0 / 2,6 / 2,8 % unter omega_d.
    - Delta faellt dabei von 0,0512 (omega_d) auf 0,0448 (erstes Fenster).
    - Die langsamste Paarung ist danach (1,2) mit ~0,0213, also Schwebungsperiode ~295.
  - **Abgestrahlte Ladung** (R3, Verlust aus [-45; 45]): 0,0012 im ersten, 0,0027 im letzten Fenster (bis t = 800),
    abflachend. Das sind 2,6e-4 der Gesamtladung.
  - **Bad an der Sonde:** |psi|^2 ~ 1e-5. Spektrum bei omega ~ +1,0 bis +1,1 und ~ +2,15 (positive Ladung), weniger als
    1 % negative Frequenzen.
  - **Laufzeit:** 0,10 ms je Schritt (dx 0,1, N = 900), 0,17 ms bei N = 2100. T = 6000 dauert also etwa 15 bis 30 s;
    dx 0,05 etwa 60 s.
- Folgen fuer diesen Plan:
  - Fensterlaenge (unten).
  - BT3/BT4 gegen omega_d wird nur berichtet (unten).
  - Ein Spektrumsvorzeichen im Code wurde vor dem Einfrieren berichtigt: positive Frequenz heisst jetzt positive Ladung.
  - Die Badkorrektur wurde vor dem Einfrieren auf den Kontrollverlust umgestellt.

## Aufbau (fest)

- **Baelle:** omega^2 = 0,58 (Ball 1, x = -18), 0,62 (Ball 2, x = 0), 0,66 (Ball 3, x = +18).
  - Amplitude x 1,05, Startschritt wie freie Baelle, ruhend.
  - Startphasen theta_i pi: Satz A (0, 0, 0), Satz B (0, 2/3, 4/3).
- **Abstand D = 18** [Zusatz CA]. Die Karte verlangt mindestens ~15.
  - Bei D = 14,6 (SCHWEBUNGSUHR-2) floss anfangs ~1 % Ladung, danach drifteten die Baelle auseinander (dX 15,3 -> 36,5
    bis T = 3000).
  - Bei D = 18 blieb der Abstand fast (17,96 -> 19,46), und die Ladung pendelte nur (halbe Spanne ~0,0016).
  - D = 18 ist also schwach gekoppelt, und die aeusseren Baelle wandern nicht an den Rand.
- **Box im Bad-Arm: L = 45**, also Rechengebiet [-45; 45] mit Dirichlet psi = 0 und ohne Daempfung [Zusatz CA].
  Begruendung:
  - Der Randabstand der aeusseren Baelle ist 27 = 1,5 D.
    - Schwanzdichte am Rand ~ 2,4 e^(-2 k 27) ~ 5e-14 (k = 0,583 fuer 0,66).
    - Spiegelkopplung ~ e^(-k 54) ~ 2e-14, gegen die Nachbarkopplung e^(-k 18) ~ 3e-5.
    - Auch nach einer Drift von einigen Einheiten bleibt der Rand wirkungslos.
  - Kleiner waehle ich die Box nicht. Die Baddichte steigt nur wie 1/L (L = 36: Faktor 1,25), der Rand kaeme aber naeher.
  - **Erwartete Baddichte:**
    - Abgestrahlte Ladung bis T etwa 0,003 bis 0,004 (Rauchlauf: 0,0027 bei t = 800, abflachend).
    - Verteilt auf 90 Laengeneinheiten: n ~ 3e-5 bis 4e-5 Ladung je Laenge.
    - Je Ballbereich (Laenge 16) also ~5e-4 bis 7e-4.
    - Feld an der Sonde: |psi|^2 ~ 1e-5, gegen Zentrumsdichten 0,5 bis 0,7.
  - Die Baddichte ist durch die schwache Abstrahlung der Anregung x 1,05 begrenzt, nicht durch die Box. Ein dichteres Bad
    braeuchte eine staerkere Anregung; die steht nicht auf der Karte.
- **Kontrolle (abs):** Rechengebiet [-105; 105], Daempfungsschicht wie in der Vorlage (Breite 60) fuer |x| > 45. Der
  Innenbereich [-45; 45] ist gleich wie im Bad-Arm, die Startlage auch.
- dt = 0,4 dx. Messabstand 0,2. Sonde bei x = 31,5 (zwischen Ball 3 und Rand). Dichtebild |psi|^2 alle 100, Energie
  alle 10.

## Laeufe (alle vor dem ersten Lauf festgelegt)

| Name | Rand | Phasen / pi | dx | T | Spur | wofuer |
|---|---|---|---|---|---|---|
| B1 | refl | 0, 0, 0 | 0,1 | 6000 | cpu | BT1, BT2, BT4 (Satz A) |
| B1f | refl | 0, 0, 0 | 0,05 | 6000 | cpu2 | zweites Gitter: BT2 "auf beiden Gittern", Gittercheck BT1/BT4, L3 |
| B2 | refl | 0, 2/3, 4/3 | 0,1 | 6000 | cpu3 | BT1, BT2, BT4 (Satz B) |
| K1 | abs | 0, 0, 0 | 0,1 | 6000 | cpu4 | Kontrolle: BT3, L2, Badkorrektur |
| B1s | refl | 0, 0, 0 | 0,1 | 6000 in drei Aufrufen (2000, 4000, 6000) | cpu6 | Abschnittsprobe [Zusatz CA]: muss bitgleich zu B1 sein |

- Gemeinsam: omega^2 = 0,58 / 0,62 / 0,66, D = 18, Amplitude 1,05, L = 45.
- Aufrufe aus /home/fmh/fmhc-physics-remote/runde23-bad-takt/:
  - `kleintest.sh <spur> r23bt-<name>-neu badtakt1d.py neu lauf/<name>.npz <rand> 0.58 0.62 0.66 18 <th1> <th2> <th3> 1.05 <dx> 45`
  - dann `kleintest.sh <spur> r23bt-<name> badtakt1d.py weiter lauf/<name>.npz 6000 500`
  - Meldet ein Aufruf FORTSETZEN (Wandzeit 500 s erreicht), wird er wiederholt.
  - Logs: /home/fmh/fmhc-physics-remote/runde23-bad-takt/lauf/<name>.log
- Auswertung: `kleintest.sh cpu r23bt-aw badtakt1d.py auswerten lauf/auswertung.json B1=lauf/B1.npz B1f=lauf/B1f.npz
  B2=lauf/B2.npz K1=lauf/K1.npz`. Danach der Bitvergleich B1 gegen B1s per `python -c`, wie im Rauchlauf.

## Messgroessen (je Messung, alle 0,2)

- Lage p_i: Dichtemaximum im Suchbereich +-3 um die letzte Lage, parabolisch verfeinert.
- Zentrumsdichte S_i = |psi|^2 am Gittermaximum. Zentrumsphase = arg psi(p_i).
- Q_i = Integral von rho ueber |x - p_i| <= 8 [Zusatz CA: Ballbereich R = 8]. Zwischen den Ballbereichen bleiben 2
  Einheiten. Die Schwanzladung jenseits 8 ist kleiner als 1e-3 je Ball.
- Q_box = Ladung in [-45; 45]; Q_gitter = Ladung im ganzen Rechengebiet (bei refl dasselbe).
- **Badladung** Q_bad = Q_box - Q_1 - Q_2 - Q_3. Sie enthaelt auch die nahezu konstanten Ballschwaenze jenseits 8 (~1e-3).
  - Weil das Bad durch die Baelle laeuft, liegt ein Teil davon in den Ballbereichen.
  - Berichtet wird deshalb zusaetzlich der Kontrollverlust Q_gitter(0) - Q_box in K1. Das ist die Ladung, die im
    Bad-Arm in der Box bleibt.
- Energie (Erhaltungskontrolle im Bad-Arm), Sonde psi(31,5) mit Spektrum im ersten und letzten Fenster.

## Fenster und Fenstermittel (Nachtrag der Karte)

- 8 gleich lange Fenster in [100; 6000], Laenge W = 737,5. Fenster k = [100 + (k - 1) W; 100 + k W].
- Begruendung der Laenge [Zusatz CA]:
  - Nominell (omega_d) ist die langsamste Paarung (2,3), mit Delta 0,0250 und Periode 251.
  - Nach der Anregung (Rauchlauf) ist es eher (1,2), mit ~0,021 und Periode ~295.
  - W = 737,5 ist 2,5 x 295 bzw. 2,9 x 251. Die Regel W >= 2 P_langsam haelt, solange die kleinste Paardifferenz
    mindestens 0,0170 betraegt.
  - Die Auswertung prueft das je Fenster mit den gemessenen omega (fensterregel_ok). Ein Verstoss aendert kein Urteil,
    wird aber als Abweichung genannt.
- omega_i im Fenster = -Steigung eines linearen Fits der abgewickelten Zentrumsphase (wie Vorkarten).
- Q_i, S_i, p_i, Q_bad: arithmetische Fenstermittel.
- Atmungsamplitude = halbe Spanne von S_i im Fenster. Im Bad-Arm enthaelt sie auch die Interferenz mit dem Bad.
- Delta_k = max_i omega_i - min_i omega_i im Fenster k, ueber die vorhandenen Baelle.
- Ball vorhanden [Zusatz CA]: Fenstermittel S_i >= 0,1 (entspricht omega^2 ~ 0,9, Q ~ 1,3). Bei weniger als zwei
  vorhandenen Baellen ist Delta undefiniert.

## Urteilsregeln (mechanisch, Funktion urteile; die Urteile im Ergebnis stammen aus ihrer Ausgabe)

- **BT1** (Nachtrag: "waechst" = letztes Fenster ueber dem ersten):
  - Eingetroffen, wenn Delta_8 > Delta_1 in B1 und in B2 gilt; sonst nicht eingetroffen.
  - Gittercheck [Zusatz CA]: dieselbe Rechnung mit B1f statt B1. Weicht die Kategorie ab: "offen (Gitter uneinig)".
  - Delta undefiniert: offen.
- **BT2:**
  - Groesster Ball = kleinstes omega im ersten Fenster (erwartet Ball 1). Kleinster = groesstes omega (erwartet Ball 3).
  - Eingetroffen, wenn in B1, B1f und B2 jeweils Q_gross,8 > Q_gross,1 und Q_klein,8 < Q_klein,1 gilt.
- **BT3:** K1, max_i |omega_i,8 - omega_i,1| / omega_i,1 < 0,01.
- **BT4:** min_k Delta_k >= 0,5 Delta_1 in B1 und in B2. Gittercheck mit B1f wie bei BT1.
- **Lesarten** [Zusatz CA]:
  - "Anfangswert" (BT4) und "aendert sich bis T" (BT3) beziehen sich nach dem Nachtrag auf das erste Fenster (ab t = 100).
  - Die Lesart gegen den Startwert omega_d wird nur berichtet. Aus dem Rauchlauf ist bekannt, dass die Anregung die Takte
    in den ersten 100 Einheiten um 2 bis 3 % senkt; gegen omega_d wuerde BT3 schon daran scheitern.
  - Wie auf der Karte entscheidet das Vorzeichen, ohne Mindestgroesse. Zu jedem Unterschied werden berichtet:
    - die Streuung der Folgefenster, std(diff)/sqrt 2
    - die Gitterabweichung (B1 gegen B1f)
    - der Wert der Kontrolle K1
  - Ist ein Unterschied kleiner als die Streuung, steht im Ergebnis "innerhalb der Streuung"; das Urteil bleibt
    mechanisch.
  - Nur berichtet: BT2 mit Badkorrektur, Q_korr_i = Q_i - 2 R Q_verlust(K1) / (2 L). Das ist der Badanteil im
    Ballbereich bei gleichmaessig verteiltem Bad.
- **Bedeutung:** wie auf der Karte. Passt der Ausgang in keine Bedeutungszeile, wird er beschrieben, nicht umgedeutet.

## Latten (v3, coordination/evolution-review-20260929/V3-ENTWURF.md, Abschnitt 2)

- **L1, kann scheitern:** BT1 bis BT4 haben je zwei moegliche Ausgaenge; die Karte nennt, was man bei Synchronisation
  saehe.
- **L2, Gegenprobe:** B1 gegen K1 (Bad an/aus) bei gleicher Startlage.
  - Effekt = letztes minus erstes Fenster, fuer Delta, Q_gross und Q_klein.
  - Berichtet wird die Differenz Bad minus Kontrolle.
- **L3, Numerik:** B1 gegen B1f (halbe Gitterweite und halber Zeitschritt). Bestanden, wenn
  5 |e(B1) - e(B1f)| <= |e(B1)| gilt.
- **L4:** Literatur erst nach den Laeufen.
- **L5:** kein Messbezug (1D-Modell).

## Vorab-Abschaetzung der Code-Agentin (Schreibtisch, Hypothese [H], aendert keine Vorhersage)

- **Badspektrum gegen Austauschkanal:**
  - Ein Ladungsaustausch Bad <-> Ball in erster Ordnung braucht einen offenen Konversionskanal 2 omega - omega_r < -1,
    also omega_r > 2 omega + 1 ~ 2,5.
  - Das Badspektrum liegt im Rauchlauf bei 1,0 bis 2,2.
  - Bad-getriebene Fluesse kommen also erst in hoeherer Ordnung, und das Bad ist duenn (n ~ 3e-5).
- **Erwartung [H]:**
  - Die Q-Fenstermittel zeigen vor allem den Restanteil des Josephson-Pendelns (2,5 Perioden je Fenster) und den
    langsamen Strahlungsverlust.
  - Aenderungen erste gegen letzte Fenster sind klein und nicht monoton. BT1 und BT2 entscheidet dann ein Vorzeichen
    innerhalb der Streuung.
- Ob das stimmt, zeigt nur der Lauf; diese Abschaetzung wird im Ergebnis gegen den Ausgang gestellt.

## Ablauf

- Plan einfrieren (Kopie PLAN.md.eingefroren-<datum-uhrzeit>, chmod a-w). Danach Laeufe wie oben, parallel auf den
  Spuren.
- Ergebnisse per rsync nach lauf-69/. Literatur (L4) erst danach.
