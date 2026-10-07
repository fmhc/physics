# PLAN SCHWEBUNGSUHR-2 (Runde 23), Code-Agent im Auftrag der Leitung claude-primary

- Geschrieben 2026-10-02 ab 22:05:09 CEST (date), nach dem Rauchlauf, vor jedem echten Lauf und jedem Literaturabruf.
- Karte: KARTE.md (unveraendert). Vorhersagen T0 bis T3 und ihre Bedeutung gelten wie auf der Karte.
- Alles, was nicht woertlich auf der Karte steht, ist als **[Zusatz CA]** (Lesart bzw. Festlegung der Code-Agentin)
  markiert.

## Code

- Code der Vorkarte: RUNDE-23/schwebungsuhr/code/schwebung1d.py, sha256
  bd0fd1b7ff5db656f8504d14a695b3a46e84c3a8a9051b3c57b113b368862c45. Per rsync unveraendert nach
  /home/fmh/fmhc-physics-remote/runde23-schwebungsuhr-2/schwebung1d.py (sha256 dort gleich). Keine lokale Kopie im
  Kartenordner.
- Veraendert wird nur der Abstand D, und zwar ueber das Aufrufargument; die Datei bleibt bitgleich.
- Hilfsauswertung hilfs/auswertung2.py (neu, vor dem Einfrieren geschrieben und am Rauchlauf getestet), sha256
  1594ec42f21d36dfffcfaa18f9e486ed47ff6fd0e7efc31366dc14721e6e3c32. Sie importiert idx, steigung und gleitend aus
  schwebung1d.py (Fits genau wie in der Vorkarte) und liest JSON und .roh.npz der Laeufe. Sie bildet V2, Q(0), r(D),
  den T1-Fit und die Urteile T0 bis T3.

## Rauchlauf (vor dem Einfrieren, nicht gewertet)

- 22:04 CEST, .69, Spur cpu, Ausgaben in /home/fmh/fmhc-physics-remote/runde23-schwebungsuhr-2/rauch/.
- `paar 0.70 0.75 10.0 0 0.1 600 900`: absichtlich ein Parametersatz, der in keinem echten Lauf vorkommt (Laufzeit,
  Absturzfreiheit, Test der Hilfsauswertung). 1,13 ms je Schritt, Schleife 14 s, Analyse 4 s; Hilfsauswertung 0,5 s,
  fehlerfrei.
- Hochgerechnet fuer T = 3000: dx 0,1 etwa 90 s, dx 0,05 etwa 260 s je Lauf (Vorkarte: 92 s bzw. 255 bis 276 s).

## Laeufe (alle vor dem ersten Lauf festgelegt)

Gemeinsam: omega_1^2 = 0,60 (Ball a, links bei -D/2), omega_2^2 = 0,65 (Ball b, rechts bei +D/2), Phasenlage 0, ruhend,
T = 3000, L = 900, Aufbau wie Vorkarte (Leapfrog dt = 0,4 dx, Daempfungsschicht, diskrete Newton-Profile).

| Name | D | dx | Spur | wofuer |
|---|---|---|---|---|
| S08 | 8 | 0,1 | cpu | gewertet (T0 nicht, da D < 10; T1, T2, T3) |
| S10 | 10 | 0,1 | cpu2 | gewertet |
| S12 | 12 | 0,1 | cpu3 | gewertet |
| S12f | 12 | 0,05 | cpu6 | zweites Gitter (L3) |
| S18 | 18 | 0,1 | cpu4 | gewertet |
| S22 | 22 | 0,1 | cpu (nach S08) | gewertet |
| S146 | 14,6 | 0,1 | cpu2 (nach S10) | nur berichtet; zugleich Reproduktion von Z2 der Vorkarte (gleiche Argumente) |

Aufruf je Lauf: `kleintest.sh <spur> r23s2-<Name> schwebung1d.py paar 0.60 0.65 <D> 0 <dx> 3000 900 lauf/<Name>.json`,
Log nach lauf/<Name>.log. Danach `kleintest.sh cpu r23s2-aw hilfs/auswertung2.py lauf/auswertung2.json lauf/S*.json`.
Alle D/(2 dx) sind ganzzahlig (40, 50, 60, 120, 90, 110, 73).

## Messgroessen

- **Delta omega_frei** [Zusatz CA]: delta_omega_diskret des jeweiligen Gitters, also omega_d,b - omega_d,a mit
  omega_d = (2/dt) asin(omega dt/2). Werte: dx 0,1: 0,031633058913306; dx 0,05: 0,031630093780574.
  - Grund: Die freien Baelle laufen im Code genau mit omega_d; die Einzelballlaeufe K1 bis K4 der Vorkarte treffen das
    auf 1e-14.
  - Der nominelle Wert 0,031629106 weicht um 1,2e-4 (relativ) ab. Das ist fuer r bei D = 22 nicht vernachlaessigbar.
    r gegen den nominellen Wert wird nur berichtet.
- **Delta omega Anfang/Ende**: lineare Fits der abgewickelten Phase am jeweiligen Dichtemaximum wie in der Vorkarte
  (w["anfang"], w["ende"] im JSON).
  - Anfang [50; 50 + 2P], Ende [T - 2P; T] = [2602,7; 3000], P = 2 pi/Delta_nom = 198,65.
  - [Zusatz CA, Lesart] "Ende ist das letzte Fenster vor T = 3000" lese ich als das Ende-Fenster der Vorkarte; es
    endet bei T = 3000 und mittelt ueber zwei Schwebungsperioden.
  - Zweitlesart (berichtet, Urteile T1 und T2 zusaetzlich damit gerechnet, nicht gewertet): letztes gleitendes Fenster
    [2950; 3000].
  - Bei verschiedenen Ausgaengen werden beide Lesarten deutlich genannt.
- **Delta omega(t)**: gleitender Fit wie in der Vorkarte (Fenster 50, Schritt 5, Funktion gleitend). Berichtet werden
  die Reihe alle 100 Einheiten, min/max sowie je Drittel ([50; 1000], [1000; 2000], [2000; 3000]) der Fit der Vorkarte.
- **r(D)** = (Delta omega_Ende - Delta omega_frei)/Delta omega_frei.
- **Q_1, Q_2** (Integral der Ladungsdichte links bzw. rechts des beweglichen Mittelpunkts, Messformel der Vorkarte):
  - [Zusatz CA] Anfang = Q(t = 0), erste Messung. Ende = Mittel ueber das Ende-Fenster [T - 2P; T]; das Fenster
    mittelt das Pendeln im Schwebungstakt.
  - Grund: Laut Vorkarte floss die Ladung in den ersten ~90 Einheiten, also vor bzw. in ihrem Anfangsfenster.
  - Berichtet werden zusaetzlich das Anfangsfenster der Vorkarte und die freien Werte aus K1 bis K4:
    - dx 0,1: Q_1,frei = 3,161949367, Q_2,frei = 2,758189341
    - dx 0,05: Q_1,frei = 3,162622507, Q_2,frei = 2,758854813
  - Dazu die halbe Spanne von Q_1 im Ende-Fenster.
- **Schwebungsfrequenz am Mittelpunkt**: dominante Pencil-Frequenz |Re| der Dichte am beweglichen Mittelpunkt (Code der
  Vorkarte), je Drittel und ueber [50; T].
- **Abstand**: Mittel ueber Anfangs- und Ende-Fenster, und zwar fuer zwei Masse:
  - Schwerpunktabstand dX, gemessen am ladungsgewichteten Ort je Seite
  - Abstand d der Dichtemaxima
  - Dazu d(0) sowie die Geschwindigkeiten v1, v2 der Maxima im Ende-Fenster (lineare Fits).
  - Daraus die Zeitdehnung in Delta omega, -(omega_2 v2^2 - omega_1 v1^2)/2, relativ zu Delta omega_frei. Sie wird
    berichtet, nicht korrigiert (wie Vorkarte).
- **Verschmelzen**:
  - **V1** (Vorkarte, unveraendert): Median des Maximaabstands d ueber [T - 100; T] < 1,5. Berichtet wird auch
    erstmals d < 1,5.
  - **V2** (Dichtebild-Pruefpunkt) [Zusatz CA, vorab festgelegt]:
    - Grundlage ist das gespeicherte Bild |psi|^2 bei t = 3000 (Bilder alle 100 Einheiten, Abstand 0,5).
    - Gezaehlt werden lokale Maxima mit |psi|^2 > 0,1, dazu der Abstand der zwei groessten.
    - V2 = verschmolzen, wenn hoechstens ein solches Maximum da ist oder die zwei groessten weniger als 1,5
      auseinander liegen.
    - Begruendung der Schwelle:
      - Die Zentraldichten der freien Baelle sind 0,553 und 0,452.
      - Ein M1-Ball mit Zentraldichte 0,1 hat omega^2 ~ 0,9 und Q ~ 1,3.
      - Die Splitter der Vorkarte (Q ~ 0,74, Zentraldichte ~ 0,04) zaehlen damit nicht.
    - Berichtet werden je Bild (alle 100): Zahl der Maxima > 0,1 und > 0,01, Orte, Hoehen und Integral |psi|^2 je
      Klumpen, sowie das erste Bild mit V2 = verschmolzen.
  - **Verschmolzen** (fuer T0 bis T3) [Zusatz CA] = V1 oder V2. "Ohne Verschmelzen" heisst also: beide Kriterien
    sagen nein. Abweichungen zwischen V1 und V2 werden gemeldet.
  - **Verfolgungspruefung** [Zusatz CA]: Bei T muessen p1(T) und p2(T) (Maxima je Halbraum, aus denen omega und
    Q stammen) je hoechstens 1,0 von einem Bildmaximum > 0,1 liegen. Sonst gilt "Verfolgung gestoert".

## Urteilsregeln (vor dem ersten Lauf festgelegt)

Gewertet werden nur die Laeufe mit dx 0,1 und D = 8, 10, 12, 18, 22. D = 14,6 wird nur berichtet.

- **T3**: eingetroffen, wenn S08 bei T verschmolzen ist (V1 oder V2).
- **T0** [Zusatz CA, Lesart von "Q_1 steigt bis T = 3000"]: Fuer jedes D aus {10, 12, 18, 22} ohne Verschmelzen gilt
  Q_1,Ende - Q_1(0) > 0. Gibt es kein solches D: offen.
  - Q_2,Ende - Q_2(0) und der Vergleich mit den freien Werten werden berichtet, aendern das Urteil aber nicht.
- **T2** [Zusatz CA, Lesart]: Fuer jedes gewertete D ohne Verschmelzen gilt r(D) > -0,10. Gibt es kein solches D:
  offen.
  - Verschmolzene D zaehlen nicht. Begruendung aus der Kartenbedeutung: "Eine gemeinsame Zeit entsteht nur durch
    Verschmelzen" setzt voraus, dass T2 beim Verschmelzen nicht automatisch scheitert. Sonst stuende T2 (80 %) gegen
    T3 (55 %).
  - Die woertliche Lesart mit verschmolzenen D wird im Ergebnis zusaetzlich genannt.
- **T1**: Punkte sind die gewerteten D ohne Verschmelzen.
  - Weniger als zwei Punkte: offen.
  - Ist ein r(D) <= 0: nicht eingetroffen. Ein Fit ueber die positiven Punkte wird nur berichtet.
  - Sonst eingetroffen, wenn beides gilt:
    - (a) r faellt streng mit D [Zusatz CA: "faellt mit D"];
    - (b) die Kleinste-Quadrate-Steigung von ln r gegen D liegt in [-1,22; -0,61].
  - Residuen werden berichtet.
- **Gitter (L3)** [Zusatz CA]: Alle Urteile werden ein zweites Mal gerechnet, mit S12f statt S12. Weicht die Kategorie
  (eingetroffen / nicht eingetroffen / offen) ab, gilt "offen (Gitter uneinig bei D = 12)". Berichtet werden auch
  r(12), Q und V1/V2 beider Gitter.
- **Verfolgung gestoert** bei einem gewerteten D ohne Verschmelzen: T0 (falls D >= 10), T1 und T2 sind dann offen.
- Die Hilfsauswertung rechnet diese Regeln mechanisch (Funktion urteile). Die Urteile im Ergebnis stammen aus ihrer
  Ausgabe.

## Vorab-Abschaetzung der Code-Agentin (Schreibtisch, Hypothese [H], aendert keine Vorhersage)

- Kontinuums-Steigungen dQ/domega der freien Baelle (aus Q(omega) = 4 sqrt2 omega atanh(sqrt((1 - s)/(1 + s))),
  s = sqrt(2 omega^2 - 1)): -14,9 fuer 0,60 und -11,3 fuer 0,65.
  - Ladungsgewinn senkt omega. Q_1 hoch und Q_2 runter heisst, Delta waechst (r > 0).
  - Die Vorkarte bei 14,6 (Q_1 +0,040, Q_2 -0,023 gegen frei) gibt so r ~ +0,149, wie gemessen.
- Bei D = 14,6 war das Ladungspendeln am Ende fast erloschen: halbe Spanne von Q1 im letzten Drittel 2e-6 gegen 3e-2
  im ersten. Die Baelle waren auseinandergedriftet, der Ladungsstand "eingefroren".
  - Ohne Drift waere der Nettofluss ueber eine Schwebung in erster Ordnung null.
  - Erwartung [H]: Ob r(18), r(22) in erster Ordnung (~ e^(-kappa D)) oder zweiter (~ e^(-2 kappa D)) laufen, haengt
    davon ab, ob die Baelle dort ebenfalls auseinanderdriften.
- Hochgerechnet von r(14,6) = 0,149:
  - mit Steigung -kappa: r(18) ~ 0,019, r(22) ~ 0,0016
  - mit -2 kappa: r(18) ~ 0,0023, r(22) ~ 2e-5
- Messgrenze fuer r [H]:
  - Schwanzmodulation der Phase am Zentrum ueber zwei Schwebungen ~ 0,08 eps, mit eps = f_Nachbar(D)/f_eigen(0):
    bei D = 22 ~ 4e-7, bei 18 ~ 4e-6.
  - Die Zeitdehnung driftender Baelle kann bei kleinen r vergleichbar werden. Sie wird je D berichtet.
- Die Interferenzladung des Starts (Phasenlage 0) ist positiv und erhaltene Gesamtladung. Ihre Aufteilung geht in Q(0)
  und Q_Ende ein. Sie wird je Lauf berichtet (Q_innen(0) - Q_1,frei - Q_2,frei).

## Ablauf

- Code und Hilfsauswertung per rsync nach /home/fmh/fmhc-physics-remote/runde23-schwebungsuhr-2/. Laeufe ueber
  kleintest.sh auf den Spuren cpu, cpu2, cpu3, cpu4, cpu6, je Aufruf ein Lauf (< 600 s).
- Ergebnisse per rsync zurueck nach lauf-69/. Literatur (L4, arXiv-Volltexte per WebFetch) erst nach allen Laeufen.
