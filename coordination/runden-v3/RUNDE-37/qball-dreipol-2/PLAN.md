# QBALL-DREIPOL-2: Plan (Code-Agent, Runde 42, Fast Lane)

- Code-Agent fuer claude-primary. Start 2026-10-04 18:03:51 CEST (date). Plantext begonnen 18:26:06 CEST (date).
- Zeitbox 150 min, also bis 20:33:51 CEST.
- **Reihenfolge offen gelegt:** Code zuerst. Vor diesem Text liefen vier Laeufe auf der .69; Abschnitt 9 nennt, was
  ich davon gesehen habe:
  - r1, r2: Rauchlaeufe
  - r3: Schwellenrechnung fuer die Ableitbarkeitsprobe von DP3
  - Leitungstest mit fremden Werten
  Hauptwerte (Dreieck-Nachbau, Stoerungsfluesse, 3D-Dreiecksfluss, Zeitentwicklung des schiefen Dreiers) habe ich
  nicht gesehen.
- **Grundlagen [P]:**
  - KARTE.md: Vorhersagen DP0 bis DP3, Wahrscheinlichkeiten und Bedeutung unveraendert.
  - QBALL-DREIPOL-1: ERGEBNIS.md, PLAN.md, code/dreipol.py (eingefroren 20261004-174224), lauf-69/c_m01.json und
    a.json.
  - AGENTS.md, Abschnitt "Dimensionsvergleich" (Finn 04.10.).
- **Kennzeichen:** [M] Mathematik, [E] gerechnet im Modell, [P] Projektdatei, [L] Gedaechtnis/Literatur, [S] Quelle,
  [H] Hypothese.
- Alles ist eine synthetische Rechnung im Modell, **keine Messdatenbestaetigung**.

## 1. Modell (unveraendert aus QBALL-DREIPOL-1)

- Drei komplexe Komponenten, V = U(S) + g4 sum_a |phi_a|^4, U(S) = S - S^2 + S^3/2, S = sum_a |phi_a|^2.
  - Die Ladungen Q_a sind einzeln erhalten (U(1)^3).
- **Fluss bei festen Ladungen:** E_Q[psi] = W[psi] + sum_a Q_a^2/(2 Lam_a), halbimplizit mit tau = 0,5, c = 1. Der
  Fixpunkt ist ein stationaerer Zustand psi_a e^{i om_a t}.
- **Zeitentwicklung:** Stoermer-Verlet, spektraler Laplace.
- **Portierung:** code/dreipol2.py uebernimmt Formeln und Ablauf von dreipol.py (Kopie: code/dreipol-vorlage-qd1.py).
  Gitterrechnung in torch auf CUDA (float64/complex128), fuer d = 2 und d = 3.
  - Ohne CUDA bricht das Skript ab (kein CPU-Fallback).
  - Der radiale 1D-Bezug (tridiagonal, scipy) und die Zufallszahlen (numpy) laufen wie in DREIPOL-1 auf der CPU.
  - DREIPOL-1 rechnete das 2D-Gitter mit numpy auf der CPU. Die Portierung folgt CLAUDE.md ("dort auf CUDA").
- **Probe der Portierung (r1) [E]:** 2D-Einpolball bei g4 = -0,1, Q1 = 60.
  - E = 48,512942932687494 gegen 48,51294293268749 in DREIPOL-1 (relativ 2,2e-16); R_halb gleich bis 9e-16.
- **Radialer Bezug in 3D:** Flaechenfaktor 4 pi r^2 statt 2 pi r; sonst dasselbe Verfahren wie in 2D (dr = 0,01,
  Dirichlet bei rmax = 60).

## 2. Ableitbarkeitsprobe (vor den Hauptlaeufen)

1. **Bindung gegen drei getrennte Baelle:** Bei konkavem E(Q) ist sie trivial (QD2-Lehre). Ich fuehre sie nicht als
   Befund.
2. **Phasenversatz (P1, P2) ist vorab ableitbar [M]:**
   - Fuer psi_a = f_a e^{i theta_a} gilt exakt E_Q[psi] = E_Q[f] + sum_a int f_a^2 |grad theta_a|^2. Lam_a haengt nur
     von f_a ab, V nur von |psi_a|^2.
   - Ein gleichfoermiger Phasenversatz einer Komponente ist daher eine exakte Symmetrie (U(1)^3). Der Fluss ist
     aequivariant, der versetzte Zustand ist selbst stationaer.
   - Folgen: Energie gleich bis auf Rundung, Abstand 0.
   - Ein ortsabhaengiger Phasenversatz kann E nur erhoehen. Eine Phasenstoerung allein kann also keinen Sattel
     verraten.
   - Ich rechne P1 und P2 trotzdem, weil die Karte sie verlangt (Kartenwortlaut: Phasenversatz zwischen den Klumpen).
     Sie gelten als vorab ableitbar; der Gehalt von DP1 liegt in V1, V2, L1 und L2.
3. **Nullmoden [M]:** Verschiebung und Drehung des ganzen Dreiecks kosten keine Energie. Der Fluss stellt die Lage
   deshalb nicht wieder her.
   - "Endabstand" misst nur die Form (Abschnitt 5): Paarabstaende sowie RMS nach bester Verschiebung und Drehung.
4. **L1 und L2 sind im Kontinuum gleichwertig [M]:**
   - Das Dreieck hat die Symmetrie D3 x S3: Ecken und Farben vertauschen gemeinsam.
   - S3 wirkt transitiv auf geordnete Paare (Farbe a, fremder Klumpen b). Jede Uebertragung "5 % der Farbe a in
     Klumpen b" ist also gleichwertig.
   - Auf dem quadratischen Gitter unterscheiden sich L1 und L2 nur durch die Gitteranisotropie. Es bleibt eine Klasse
     von Ladungsstoerungen.
   - Der Sektorwechsel L3 (Q = 63/57/60) ist eine andere Klasse. Er laeuft beschreibend mit (Abschnitt 9a.2).
5. **DP1 sonst nicht ableitbar:** Das Hesse-Spektrum des Dreiecks ausserhalb des symmetrischen Unterraums ist
   unbekannt.
6. **DP2:**
   - Vorab ableitbar ist nur der Vergleich Einpolball gegen Mischball in 3D. Er folgt aus den radialen Loesungen; er
     ist Kontrolle in DP0.
   - Ob ein festes 3D-Dreieck existiert und ob es unter dem Mischball liegt, ist nicht ableitbar.
   - Der Startwert erzwingt nichts. Das Dreieck liegt in 2D nur 0,146 (1e-3 relativ) unter dem Mischball.
7. **DP3: Energiebilanz des schiefen Starts** (r3, Fluesse bei festen Ladungen, ohne Rauschen) [E, M].

   | g4 | E_start | drei getrennt | Paar 60+60 + Pol 57 frei | Paar 60+57 + Pol 60 frei | Abstand zur kleinsten Schwelle |
   |---|---|---|---|---|---|
   | +0,1 | 153,737 | 158,588 | 100,227 + 51,200 = 151,427 | 97,872 + 53,694 = 151,566 | **+2,31** (erlaubt) |
   | -0,1 | 139,745 | 143,390 | 94,047 + 46,364 = 140,411 | 91,887 + 48,513 = 140,400 | **-0,656** (verboten) |

   - Das Paarminimum ist der kleinere Wert aus zwei Startformen: beruehrendes Paar (2R) und gemischter Start.
     - Bei g4 = -0,1 ist es ein getrenntes Zweifarbenpaar mit Abstand 0,79 R bzw. 0,66 R. Es liegt 0,03 unter dem
       Mischpaar. Das ist beschreibend und neu [E].
   - Strahlung hilft nicht [M]: Ladung in Strahlung kostet mindestens 1 je Einheit, gebundene Ladung nur om < 1 je
     Einheit. E(Q) - Q faellt mit Q (Argument aus DREIPOL-1, Selbstanzeige 5).
   - Ein Pol mehr als 4 R von der Mitte kostet bis auf die Schwanzwechselwirkung (~e^{-2 kappa 2R} ~ 1e-4) mindestens
     die Schwelle.
   - **Folgen:**
     - Bei g4 = -0,1 ist "kein Ausstoss" vorab ableitbar. Offen bleibt dort nur das 90-%-Kriterium (Strahlung).
     - Der Energieueberschuss ueber dem Dreiersektor erlaubt rund 10 Ladungseinheiten Strahlung [M, Schaetzung]. Ein
       Pol koennte also 10 % verlieren.
     - Bei g4 = +0,1 ist der Ausstoss energetisch erlaubt (um 2,2 bis 2,3); dort ist DP3 nicht ableitbar.
     - In drei getrennte Baelle zerfallen ist bei beiden g4 verboten.
   - **Darum:** Das Planurteil zu DP3 faellt bei g4 = +0,1 (Hauptwert). Das ist auch das g4 von QD3 und der Fall, auf
     den sich "Die Energie erlaubt das" in der Karte bezieht (DREIPOL-1, Selbstanzeige 5).
     - g4 = -0,1 wird mit derselben Regel als Nebenurteil gefuehrt, mit dem Vermerk "kein Ausstoss vorab ableitbar".
     - Die Auswertung schreibt diesen Vermerk mechanisch aus S.json.

## 3. Numerik

**2D (Teil A und C):**
- Wie DREIPOL-1: L = 64, N = 256 (h = 0,25), periodisch, spektral.
- Gitterprobe dort: N = 320 aendert E des Einpolballs um 2,2e-16 [P].

**3D (Teil B):**
- **Ladung, begruendet nach der Dimensionsregel:** Q1_3D = 2500.
  - Die Zahl Q1 = 60 aus 2D hat in 3D keine Bedeutung. Abgeglichen wird stattdessen die Frequenz des Einpolballs bei
    g4 = -0,1: 3D om = 0,7144 (Q = 2500, r2) gegen 2D om = 0,7151.
  - Gleiches om heisst gleicher Schwanzabfall kappa = sqrt(1 - om^2) = 0,70. Es heisst auch gleicher Abstand zur
    Duennwandschwelle om_c(g4 = -0,1) = sqrt(0,395) = 0,628 [M].
  - Aus der radialen Abtastung (r1: Q = 100 bis 3200) ergibt die Interpolation in ln Q den Wert 2493; gerundet 2500.
  - R_halb = 6,87 (2D: 3,18).
  - Bei g4 = +0,1 ist om(2500) = 0,83 (r1, Ball existiert).
- **Gitter:** L = 48, N = 80 (h = 0,6) im Hauptlauf.
- **Gitterprobe r2** (Einpolball Q = 2500, g4 = -0,1, L = 48):

  | N | h | E | gegen N = 128 | gegen radial (dr = 0,01) |
  |---|---|---|---|---|
  | 80 | 0,6 | 1902,26427532 | 2,3e-9 | 2,28e-7 |
  | 96 | 0,5 | 1902,26427961 | 2,5e-12 | 2,30e-7 |
  | 128 | 0,375 | 1902,26427961 | 0 | 2,30e-7 |

  - Der Rest gegen radial ist der Diskretisierungsfehler zweiter Ordnung des radialen Bezugs. In 2D war er 3,6e-7.
  - Zusatzlauf B_m01_fein mit N = 96 fuer den Dreiecksfluss bei g4 = -0,1: nur beschreibend.
- **Kasten:** Das beruehrende Dreieck reicht bis 2 (rho + R) = 4,31 R = 29,6 < 48.
  - Abstand einer Farbe zu ihrem eigenen periodischen Bild: 48 - 2R = 34. Mit kappa = 0,70 ergibt das e^{-24}.
  - Der Mischball (Q = 7500, R ~ 9,9) hat zu seinem Bild 28 Abstand, also e^{-20} [Schaetzung, M].
- **Zeit je Flussschritt** (drei Komponenten, P4000, r2): 6,8 ms (N = 80), 11,7 ms (N = 96), 26,8 ms (N = 128).
- **Toleranz:** max abs(Residuum) < 1e-6 fuer Ball, Mischball und Dreiecksfluss; hoechstens 60000 Schritte bzw.
  420 s (Fein: 400 s).

**Fluesse in Teil A:**
- Nachbau wie DREIPOL-1: vom eingespannten Dreieck (d0 = 2R) bis Residuum < 1e-7, hoechstens 12000 Schritte.
- Danach weiter bis 1e-9 (hoechstens 8000 Schritte): Das ist die Referenz fuer die Stoerungen.
- Stoerungsfluesse bis Residuum < 1e-8, hoechstens 30000 Schritte bzw. 45 s je Stoerung.
- Zeit je Schritt in 2D: 1,28 ms (r1).

**Zeitentwicklung in Teil C:**
- dt = 0,025 (Stabilitaetsgrenze ~0,11), Messung alle 0,5, T = 300. Zeit je Schritt 1,39 ms (r1).
- Rauschen wie DREIPOL-1: glattes komplexes Gaussfeld, k_c = 2, eps = 1e-3, nur auf den Baellen.
  - In DREIPOL-1 kamen die Zufallszahlen aus numpy default_rng(saat), die Glaettung aus scipy. Hier: dieselben
    Zufallszahlen, Glaettung mit torch.

## 4. Parameter (vorab gebunden)

**Teil A** (2D, g4 = -0,1, Q1 = 60):
- **Stoerungen** des Referenzdreiecks (R = R_halb des Einpolballs):
  - V1: Komponente 1 (Pol oben auf der Spiegelachse) spektral um 0,15 R in +x verschoben (tangential, bricht die
    Spiegelung).
  - V2: Komponente 2 um 0,15 R radial nach aussen verschoben (Richtung Mitte -> Schwerpunkt 2).
  - L1: 5 % der Farbe 2 aus Klumpen 2 nach Klumpen 1, gleichphasig: psi_2 -> sqrt(0,95) psi_2 + sqrt(0,05)
    psi_2(verschoben auf Platz 1). Klumpen 1 hat dann +5 %, Klumpen 2 -5 %; alle Q_a bleiben 60.
  - L2: 5 % der Farbe 1 aus Klumpen 1 nach Klumpen 2 (Klumpen 1 -5 %, Klumpen 2 +5 %).
  - P1: Phase von Komponente 2 um pi/2 versetzt.
  - P2: Phasen von Komponente 2 und 3 um 2 pi/3 und 4 pi/3 versetzt.
  - L3 (beschreibend, ohne Urteil): Sektorwechsel Q = (63, 57, 60), Amplituden mit sqrt(1,05) bzw. sqrt(0,95)
    skaliert.
- **Groesse:** 0,15 R ist das 7,5-fache der Schwelle 0,02 R und 12 % des Paarabstands. 5 % ist der Kartenwert.

**Teil B** (3D):
- g4 in {-0,1; +0,1}, Q1 = 2500 je Pol, N = 80, L = 48.
- Einpolball (Q1) und Mischball (3 Q1, Richtung (1,1,1)/sqrt 3, Start: radialer Ball mit g_eff = g4/3), je radial und
  auf dem Gitter.
- Dreiecksfluss vom beruehrenden Dreieck: d0 = 2R, Ecken bei 90/210/330 Grad in der Ebene z = 0.

**Teil C** (2D, echte Zeit, Q1 = 60):
- g4 = +0,1 (Hauptwert) und g4 = -0,1 (Nebenurteil).
- **Schiefer Start:**
  - Grunddreieck mit d0 = 2R wie c1 in DREIPOL-1, Baelle in Ruhe (pi_a = i om_a psi_a).
  - Pol 1 liegt so weit aussen, dass seine Abstaende zu Pol 2 und 3 gleich 1,1 d0 sind ("10 % weiter weg").
  - Pol 2 hat die Ladung 0,95 Q1 = 57 (eigener Einpolball).
  - Damit ist keine Spiegelung mehr uebrig.
- Saaten 1, 2, 3, 4; eps = 1e-3; T = 300.
- Klumpengebiet: Kreis R_K = rho + 3R um den momentanen Gesamtladungsschwerpunkt (rho = d0/sqrt 3, wie DREIPOL-1).
- Ausstoss: Ladungsschwerpunkt eines Pols mehr als 4 R vom Gesamtladungsschwerpunkt.

## 5. Messgroessen

**Teil A:**
- **Nachbau** (DP0): Paarabstaende/R, E, Status. Mischball Q = 180 (E_mix) auf demselben Gitter; Luecke
  E_mix - E_Dreieck.
- **Je Stoerung**, alle 50 Flussschritte und am Ende:
  - E - E_ref, Residuum
  - Schwerpunkte |psi_a|^2 und Paarabstaende
  - **d_form** = max_ab abs(D_ab - D_ab,ref)/R
  - **d_rms** = RMS-Abstand der drei Schwerpunkte zum Referenzdreieck nach bester Verschiebung und Drehung (Kabsch,
    ohne Spiegelung), durch R
  - **Reinheit:** Anteil von |psi_a|^2 in der eigenen Voronoi-Zelle der drei Schwerpunkte

**Teil B:**
- Einpol- und Mischball: E Gitter, E radial, om, R_halb, Status.
- Dreiecksfluss: E(Schritt), Residuum, Paarabstaende, Reinheit. Am Ende Gestalt und E gegen Mischball und 3 E_1.
- **Gestalt** (wie DREIPOL-1, R = R_halb des 3D-Einpolballs): verschmolzen bei max D < 0,25 R, Dreieck bei
  min D > R, sonst Zwischenform.
- Bilder: Ebene z = 0.

**Teil C:**
- Alle 0,5: E, Q_a, Q_a,in (im Klumpengebiet), Ladungsschwerpunkte, Abstand jedes Pols zur Mitte.
- Bilder bei t = 0, 100, 200, 300.
- Pulsationsdauer (beschreibend): mittlerer Abstand der lokalen Minima des mittleren Paarabstands (Fenster +-5,
  unter dem Mittelwert).

## 6. Urteilsregeln (vorab, in Zahlen; Code: code/auswertung2.py)

| Nr | Plan (Hauptregel) | Kartenwortlaut |
|---|---|---|
| DP0 | **eingetroffen**, wenn alle Teile halten. 2D: Nachbau und Mischball konvergiert, max_ab abs(D_ab/R / 1,245 - 1) <= 0,02 und abs(Luecke/0,146 - 1) <= 0,10. 3D: bei beiden g4 Einpol- und Mischball konvergiert (Gitter und radial) mit abs(E_Gitter/E_radial - 1) <= 1e-4. **Nicht eingetroffen**, wenn ein Teil konvergiert ist und verfehlt; sonst nicht auswertbar | gleich (Kartenwortlaut ist schon in Zahlen) |
| DP1 | Je Stoerung V1, V2, L1, L2, P1, P2 drei Faelle. **"zurueck":** Fluss konvergiert (Residuum < 1e-8), d_form < 0,02, d_rms < 0,02 und abs(E_Ende - E_ref) < 1e-3. **"nicht zurueck":** konvergiert, aber nicht zurueck; oder E_Ende < E_ref - 1e-3; oder nicht konvergiert mit d_rms am Ende > d_rms am Start. **Sonst "offen".** Eingetroffen, wenn alle sechs "zurueck"; nicht eingetroffen, wenn eine "nicht zurueck"; sonst nicht auswertbar | je Stoerung am Flussende (gleich welcher Status): d_rms < 0,02 R und abs(E_Ende - E_ref)/E_ref < 1e-3. Eingetroffen, wenn alle sechs; sonst nicht eingetroffen |
| DP2 | g4 = -0,1, Lauf B_m01. **Eingetroffen**, wenn alles gilt: Fluss konvergiert (< 1e-6), Gestalt "Dreieck", Reinheit jeder Farbe >= 0,5 und E_Ende < E_Misch,Gitter (1 - 1e-6). **Nicht eingetroffen**, wenn konvergiert, aber eine Bedingung verfehlt, oder wenn nicht konvergiert und die Gestalt "verschmolzen" ist. Sonst nicht auswertbar | wie Plan, aber E_Ende unter dem Gitter- **und** dem radialen 3D-Mischball (ohne Rand 1e-6) |
| DP3 | g4 = +0,1, vier Saaten. Gueltig: T = 300 erreicht, abs(dE/E) <= 1e-3, abs(dQ_a/Q_a) <= 1e-8. "Beisammen": kein Ausstoss bis t = 300 (kein Polschwerpunkt > 4 R von der Mitte) und min ueber t <= 300 und a von Q_a,in/Q_a(0) >= 0,9. **Eingetroffen** bei >= 3 gueltigen Saaten "beisammen"; **nicht eingetroffen** bei >= 2 gueltigen Saaten "nicht beisammen"; sonst nicht auswertbar. g4 = -0,1 mit derselben Regel als Nebenurteil | bei **beiden** g4 (die Karte nennt keines): >= 3 von 4 Saaten ohne Ausstoss und Q_a,in/Q_a(0) >= 0,9 bei t = 300 (Ende); eingetroffen nur, wenn beide g4 eintreffen |

- **Mechanische Vermerke:** "P1/P2 vorab ableitbar" (2.2) und "kein Ausstoss bei g4 = -0,1 vorab ableitbar", falls
  S.json das zeigt (2.7).
- **Nur beschreibend:** L3, der Feinlauf B_m01_fein, Teil B bei g4 = +0,1, Pulsationsdauer und Reinheiten.
  - Weicht B_m01_fein in der Gestalt von B_m01 ab, steht das als Vermerk in ERGEBNIS.md; das Urteil bleibt beim
    Hauptlauf.
- **Leseregel fuer Teil A:** E_ref ist die Referenz aus diesem Lauf, nicht die Datei aus DREIPOL-1.

## 7. Laeufe (.69, kleintest.sh, Spuren p4000a und p4000b, GPU)

| Spur | Lauf | Inhalt | Obergrenze |
|---|---|---|---|
| p4000a | A | Teil A: Nachbau, Referenz, Mischball, 7 Stoerungen | ~6 min |
| p4000a | B_m01 | Teil B, g4 = -0,1, N = 80 | 8,5 min |
| p4000a | C_p01 | Teil C, g4 = +0,1, 4 Saaten | ~2 min |
| p4000b | B_p01 | Teil B, g4 = +0,1, N = 80 | 8,5 min |
| p4000b | C_m01 | Teil C, g4 = -0,1, 4 Saaten | ~2 min |
| p4000b | S | Schwellen fuer DP3 mit dem eingefrorenen Code | < 1 min |
| p4000b | B_m01_fein | Teil B, g4 = -0,1, N = 96, beschreibend | 8 min |

- Danach die Auswertung: kleintest.sh p4000a dp2-aw code/auswertung2.py lauf (< 1 min).
- Laufskripte code/laeufe-p4000a.sh und code/laeufe-p4000b.sh. Ausgaben auf der .69 unter
  /home/fmh/fmhc-physics-remote/qball-dreipol-2/lauf/, danach per scp in lauf-69/.
- Jede Einheit: CPUQuota 100 %, MemoryMax 4G, RuntimeMaxSec 600 (kleintest.sh).

## 8. Erwartungen des Agenten (vorab, ohne Urteil)

- E0: DP0 trifft ein. 2D-Nachbau bitnah wie DREIPOL-1; 3D-Abweichung ~2e-7.
- E1: Unsicher. Ein Dreieck aus sich ueberlappenden Klumpen (Paarabstand 1,245 R) koennte gegen Ladungsuebertragung
  weich sein. Ich erwarte eher Rueckkehr (55 %).
- E2: Bei Q1 = 2500 (dickere Klumpen, mehr Volumen gegen Oberflaeche) ist die Entmischung in 3D eher guenstiger als in
  2D. Ich erwarte ein Dreieck unter dem Mischball (50 %).
- E3: Bei g4 = +0,1 pulsiert der schiefe Dreier und verliert Strahlung. Ein Ausstoss in 300 Zeiteinheiten ist
  moeglich, aber nicht wahrscheinlich (60 % beisammen).

## 9. Rauchlaeufe, Schwellen und Leitungstest (vor dem Einfrieren; Werte gesehen)

- **r1** (rauch-69/r1.json, 16:18:59 bis 16:19:25 UTC):
  - Geraet: Quadro P4000, torch 2.5.1+cu121.
  - 2D-Einpolball gegen DREIPOL-1 (Abschnitt 1); Zeiten 2D.
  - Radiale 3D-Einpolbaelle bei Q = 100 bis 3200, g4 = +-0,1. Bei g4 = +0,1 und Q = 100 gibt es keinen Ball: om > 1,
    die Norm zerfliesst.
- **r2** (rauch-69/r2.json, 16:20:25 bis 16:20:36 UTC): 3D-Gitterprobe des Einpolballs bei Q = 2500 und Zeiten
  (Abschnitt 3).
- **r3** (rauch-69/r3_schwellen.json, 16:20:41 bis 16:20:51 UTC): Schwellen und Startenergie fuer DP3 (Abschnitt
  2.7). Der Hauptlauf S wiederholt das mit dem eingefrorenen Code.
- **Leitungstest** (rauch-69/pipe/, 16:23:53 bis 16:24:27 UTC):
  - Alle Modi mit fremden Werten und die Auswertung, ohne Fehler.
  - Fremde Werte: A mit Q1 = 25 und 30 Flussschritten, B mit N = 32 und Q1 = 300, C mit Q1 = 25 und T = 2.
  - Gelesen habe ich nur Rueckgabecodes, Tracebacks und die Bildvermerke, keine Zahlen.
  - Die Urteilsfelder der Testauswertung (Fremdwerte) standen in derselben Ausgabe. Sie sind ohne Bedeutung.

## 9a. Lesarten und Abweichungen von der Karte (vor dem Einfrieren begruendet)

1. **Phasenversatz:** gleichfoermiger Versatz je Komponente (Kartenwortlaut "zwischen den Klumpen"). Er ist vorab
   ableitbar (2.2); ich behalte ihn und kennzeichne ihn.
2. **Ladungsverschiebung:** Uebertragung im Sektor, alle Q_a bleiben 60.
   - Nur so kann der Fluss bei festen Ladungen zum selben Dreieck "zurueckkehren".
   - Die andere Lesart, Komponentenladungen 63/57, ist ein anderer Sektor mit eigenem Gleichgewicht. Sie laeuft als L3
     ohne Urteil.
3. **Endabstand:** Formabstand, weil Verschiebung und Drehung Nullmoden sind (2.3). Energie im Plan absolut 1e-3, im
   Kartenwortlaut relativ 1e-3.
   - Relativ 1e-3 entspricht 0,139. Das ist fast die ganze Luecke zum Mischball (0,146); deshalb ist absolut die
     Hauptregel.
4. **Teil C:**
   - "10 % weiter weg": Die Abstaende von Pol 1 zu den beiden anderen sind 1,1 d0.
   - Die kleinere Ladung sitzt auf Pol 2, damit keine Spiegelung bleibt.
   - g4 nennt die Karte nicht. Hauptwert ist +0,1 (2.7), Nebenurteil -0,1.
5. **Teil B:** Q1_3D nach Frequenzabgleich (Abschnitt 3); Hauptgitter N = 80 nach der Gitterprobe. Die Karte erlaubt
   ein groberes Gitter, wenn die Gitterprobe es traegt.
6. **Mischball in Teil A:** auf demselben Gitter neu gerechnet. Start ist der radiale Ball mit g_eff, nicht wie in
   DREIPOL-1 der Ball mit g = 0. Der Fixpunkt ist derselbe.

## 10. Grenzen

- 2+1 bzw. 3+1 ohne Eichfeld; Anisotropie nur g4 sum |phi_a|^4 (wie DREIPOL-1).
- Teil A prueft sechs Stoerungsrichtungen, kein volles Hesse-Spektrum. Ein Sattel mit einer Richtung, die keine der
  Stoerungen enthaelt, bliebe unentdeckt.
  - V1 und V2 enthalten beide E-Anteile (Formmoden des Dreiecks). L1/L2 sind eine Klasse; P1/P2 sind trivial.
- Teil B: ein Q1, ein Gitter (plus Feinlauf), nur der Fluss, keine Zeitentwicklung in 3D. Ein 3D-Fixpunkt ist kein
  voller 3D-Stabilitaetsnachweis: Der Fluss erhaelt die Spiegelung z -> -z und die Lage in der Ebene.
- Teil C: periodischer Kasten (L = 64). Strahlung kommt zurueck; das ist wie in DREIPOL-1.
