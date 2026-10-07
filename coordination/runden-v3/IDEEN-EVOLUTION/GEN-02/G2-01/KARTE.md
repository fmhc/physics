# G2-01 Teilungsschwelle drehender Q-Baelle aus der NLS-Wirbelgrenze: m = 3 blind vorhergesagt

- **Hypothese [H]:** Die Teilungsschwelle eines drehenden 2D-Q-Balls mit Windung m (Klein-Gordon,
  U(S) = S - S^2 + S^3/2) liegt bei der umgerechneten Stabilitaetsgrenze der Wirbelsolitonen des kubisch-quintischen
  NLS, omega_c^2 = 1 - (8/3) Omega_st(m), hoechstens 0,006 darunter. Die Profilfamilie beider Modelle ist nach
  Umskalierung exakt dieselbe. Fuer m = 3 folgt omega_c^2 in [0,540; 0,548].

- **Papier vorab [S]:**
  - Unsere Profilgleichung f'' + f'/r - m^2 f/r^2 - (1 - omega^2) f + 2 f^3 - (3/2) f^5 = 0 geht mit f = sqrt(4/3) g
    und r = sqrt(3/8) rho in g'' + g'/rho - (Omega + m^2/rho^2) g + g^3 - g^5 = 0 ueber. Das ist die Profilgleichung
    des NLS i Psi_t + Laplace Psi + |Psi|^2 Psi - |Psi|^4 Psi = 0 mit Omega = (3/8)(1 - omega^2).
  - Proben: Die Kuppe S = 1 entspricht g^2 = 3/4. Omega_max = 3/16 entspricht omega^2 = 1/2. Die Ladung ist
    Q = omega N (N = NLS-Norm).
  - Veroeffentlichte Grenzen (NLS stabil fuer Omega > Omega_st), umgerechnet (bei uns stabil fuer omega^2 < omega_c^2):

    | m | Evans-Funktion | 2D-Simulation (instabil / stabil) | omega_c^2 umgerechnet | bei uns gerechnet |
    |---|---|---|---|---|
    | 1 | 0,1487 | 0,146 / 0,147 | 0,6035 (Evans), 0,608 bis 0,611 (Simulation) | zwischen 0,59 und 0,60 |
    | 2 | 0,1619 | 0,161 / 0,162 | 0,5683 (Evans), 0,568 bis 0,571 (Simulation) | zwischen 0,55 und 0,57, gamma^2-Nullpunkt 0,567 |
    | 3 | 0,1700 | 0,170 / 0,171 | 0,5467 (Evans), 0,544 bis 0,547 (Simulation) | nicht gerechnet |

  - Die Spalte "bei uns" stammt aus vorhandenen Rechnungen mit demselben Stoerverfahren (m = 1: RUNDE-07 RING-T,
    0,59 ruhig bis T = 3000, 0,60 geteilt bei t = 1045 mit gamma 0,0041; m = 2: 0,57 geteilt mit gamma 0,0098). Sie
    eichen die Verschiebung gegen den Evans-Wert: etwa -0,004 (m = 1) und hoechstens -0,0015 (m = 2; bei nach oben
    gekruemmtem gamma^2 liegt der wahre Nullpunkt unter der Sehnen-Verlaengerung 0,567). Daraus das Band fuer m = 3:
    0,5467 minus 0 bis 0,006, mit 0,001 Rand: [0,540; 0,548]. m = 1 und m = 2 sind damit kein Test mehr.
  - Warum das nicht selbstverstaendlich ist [S]: Die linearisierten Gleichungen von Klein-Gordon und NLS stimmen nur
    beim Eigenwert null ueberein. Bei lambda = i nu mit nu ungleich 0 stehen bei Klein-Gordon lambda^2 -+ 2 i omega
    lambda, beim NLS nur ein Term linear in lambda. Kippt die Stabilitaet ueber einen Zusammenstoss bei nu ungleich 0,
    koennen die Schwellen weit auseinanderliegen. Die kleine Verschiebung bei m = 1 und 2 kann Zufall sein.

- **Kleiner Test:**
  - Code: Kopie von IDEEN-EVOLUTION/GEN-01/G1-03/teilung_schwelle.py, Unterbefehl "teilung". Stoerung wie dort
    (Moden l = 1 bis 6, Amplitude 0,01), T = 2400.
  - Neu: halbe Boxlaenge L = 48,0 fuer m = 3 (n = 320 grob, 480 fein; Randschicht wie bisher 8 breit). Geschaetzt
    [S] ist ein m = 3-Ball nahe omega^2 = 0,53 etwa anderthalbmal so gross wie der m = 2-Ball bei 0,55 (R_halb 13,2,
    Schwanz bis 22,9). Die Startreihe f = p r^m (...) ist fuer jedes m geschrieben; ob das Schiessen fuer m = 3 ohne
    Eingriff laeuft, zeigt die Formprobe. Neuer Code: Laufliste, L als Argument, Kennzahlen V1 bis V3; unter 1 h.
  - Hauptlauf grob (dx 0,3, dt 0,05):
    - m = 3 bei omega^2 = 0,530 / 0,535 / 0,540 / 0,545 / 0,550 / 0,560 (L = 48,0)
    - m = 2 bei 0,560 / 0,565 (L = 38,4 wie bisher)
  - Fein (dx 0,2, dt 0,025): m = 3 bei 0,535 und 0,550.
  - Gegenprobe: m = 0 bei 0,55 und 0,56 (L = 48,0), gleich gestoert.
  - Messung je Lauf wie bisher: Teilung ja/nein, t_teilung, Zahl und Windung der Toechter, l_dom, gamma, Ladung Q.
  - Rechenort: .69, Spur p4000a oder p4000b, drei Aufrufe (haupt grob, haupt fein, gegen), je unter 10 min.
    Schaetzung aus dem Vorlaeuferlauf (0,0078 s je Lauf und Zeiteinheit grob bei n = 256, 0,037 s fein bei n = 384,
    mal Flaechenfaktor 1,56): grob etwa 4 min, fein etwa 5 min, jeweils mit Schiessen. Liegt die Formprobe darueber,
    wird T fuer die aeussersten Punkte (0,530 und 0,560) auf 1200 gekuerzt und das im NACHTRAG.md vermerkt.

- **Vorhersage vorab:**
  - V1 (m = 3, Schwelle): Die Teilung ist monoton in omega^2. 0,530 und 0,535 teilen sich bis T = 2400 nicht, 0,550
    und 0,560 teilen sich.
  - V2 (m = 3, Nullpunkt): Die Gerade gamma^2 gegen omega^2 durch die zwei tiefsten teilenden m = 3-Laeufe hat ihren
    Nullpunkt in [0,540; 0,548]. gamma faellt mit omega^2 nicht.
  - V3: m = 2 bei 0,560 und 0,565 teilt sich bis T = 2400 nicht. Alle Toechter tragen Windung 0.
  - **Scheitert, wenn** eines davon eintritt:
    - 0,530 oder 0,535 teilt sich, oder 0,550 oder 0,560 teilt sich nicht
    - die Teilung ist nicht monoton
    - der gamma^2-Nullpunkt liegt ausserhalb [0,540; 0,548]
    - V3 verfehlt (dann stimmt schon die m = 2-Einordnung nicht, die das Band mitbestimmt)
  - Nur V1 und V2 pruefen die Hypothese. V3 prueft die Eichung.

- **Gegenprobe (Effekt muss verschwinden):** m = 0 bei 0,55 und 0,56 teilt sich bis T = 2400 nicht, und keine
  azimutale Mode waechst messbar (kein gamma-Fit oder gamma < 0,005).

- **Plausibilitaetsschranke:**
  - Q_box(t) <= Q_box(0) (1 + 1e-4)
  - Ladung der Box auf 2e-3 relativ erhalten bis T (ohne Teilung) bzw. bis 0,5 t_teilung
  - J/Q am Start auf 1e-3 gleich m
  - Summe der Tochterladungen hoechstens 1,002 Q
  - Tochtergeschwindigkeiten unter 1; 0 <= gamma <= 1
  - Profilprobe: S_max < 1 fuer alle geschossenen Profile; Schwanz (f < 1e-3 f_max) endet vor der Randschicht

- **Latten erwartet:**
  - L1 ja: m = 3 ist in unserem Modell nicht gerechnet. Das Band [0,540; 0,548] kann verfehlt werden, auch in beide
    Richtungen.
  - L2: m = 0 bei gleichem omega^2 und gleicher Box.
  - L3: grob gegen fein bei 0,535 und 0,550: gleicher Ausgang und gleiche Toechterzahl, gamma-Aenderung hoechstens ein
    Fuenftel.
  - L4 teilweise: Stabilitaetsgrenzen der Wirbelsolitonen im kubisch-quintischen NLS sind bekannt (Simulation und
    Evans-Funktion). Fuer die relativistische Klein-Gordon-Fassung in 2+1 D keine Arbeit gefunden.
  - L5 nein: Die Vergleichszahl ist eine veroeffentlichte Theoriezahl, keine Messung.

- **Einfach gesagt:** Ein kreiselnder Q-Ball zerfaellt, wenn er zu klein ist. Seine Form stimmt nach einem einfachen
  Umrechnen genau mit einem Lichtwirbel ueberein, den Optiker schon lange untersuchen, und fuer diesen Lichtwirbel sind
  die kritischen Groessen veroeffentlicht. Fuer Baelle mit einer und zwei Phasenumdrehungen liegt unsere gerechnete
  Grenze knapp unter der umgerechneten Zahl. Jetzt sagen wir damit die Grenze fuer drei Umdrehungen vorher, bevor sie
  jemand rechnet. Liegt sie ausserhalb des Bandes, war die Naehe bei eins und zwei Zufall.

- Karte geschrieben: 2026-09-30 10:48:29 CEST

- Vorhersage geschrieben: 2026-09-30 11:06:31 CEST
