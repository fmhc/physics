# QBALL-PYRO-1: Plan (Code-Agent fuer die Leitung, Runde 37, explorativ nach v3)

- Start des Code-Agenten 2026-10-04 03:39:59 CEST (date). Plantext ab 04:04:43 CEST (date), nach fuenf Rauchlaeufen
  (Abschnitt 8). Zeitbox 120 min, also bis 05:40 CEST.
- Karte: KARTE.md (QP0 bis QP4; Vorhersagen, Wahrscheinlichkeiten und Schwellen unveraendert uebernommen).
- Code: code/pyro.py (Rechnung), code/auswertung.py (Urteile, Bilder), code/laeufe-cpu3.sh und code/laeufe-cpu4.sh
  (Hauptlaeufe). Nur fuer den Rauch: code/rauch-aw.sh.
- Kennzeichen: [M] vorab ableitbar, [S] an der Quelle gelesen, [L] Literatur aus dem Gedaechtnis, [L?] unsicher,
  [H] Hypothese, [F] Festlegung dieses Plans (von der Karte offengelassen), [E] im Rauch gesehen.
- Alles sind synthetische Gitterrechnungen, keine Messdaten.

## 1. Gitter [M, im Rauch geprueft]

- Ganzzahlige Koordinaten in Einheiten a/8 (a = kubische Zellkante). Torus aus L^3 kubischen Zellen, 4 fcc-Punkte je
  Zelle, je fcc-Punkt die Tetraeder-Basis (0,0,0), (0,2,2), (2,0,2), (2,2,0); 16 L^3 Knoten.
- Tetraeder: "oben" = fcc-Punkt + Basis, "unten" = fcc-Punkt - Basis. Nachbarn = Knoten mit gemeinsamem Tetraeder.
- Pruefungen im Code (Rauch r1a, L = 2, 3, 4, 8 [E]): jeder Knoten in genau 2 Tetraedern, 6 verschiedene Nachbarn,
  alle im Abstand |(0,2,2)| = 2 sqrt(2) Einheiten, 48 L^3 Kanten, A symmetrisch, Nachbarn je Knoten paarweise +-d
  (Inversionszentrum).
- Physikalische Laenge: Nachbarabstand = h, also x = Einheiten * h/(2 sqrt 2), Zellkante a = 2 sqrt(2) h.
- **Gitterabstand [F]:** In QP3 und QP4 heisst "Gitterabstand" der Nachbarabstand h.

## 2. Modell und Normierung

- Feldgleichung (Karte): phi_tt = (A - 6) phi/h^2 - U'(|phi|^2) phi, U(S) = S - S^2 + S^3/2, U'(S) = 1 - 2 S + 1,5 S^2.
- **Kontinuumsgrenze [M]:** Fuer die akustische Bande gilt -Delta = h^2 k^2 + O(k^4) (aus der Diamant-Darstellung
  A = 2 + |f(k)| bzw. 2 - |f(k)|, |f|^2 = 16 - a^2 k^2 + ..., a^2 = 8 h^2). Delta/h^2 ist also der Laplace-Operator mit
  Koeffizient 1, h = Nachbarabstand. Das passt zu M1 in REGEL-1 bzw. RUNDE-02 (L = |phi_t|^2 - |grad phi|^2 - U).
- **Volumen je Knoten [M, Berichtigung]:** Eine kubische Zelle (a^3 = 16 sqrt(2) h^3) traegt 16 Knoten, also
  v_s = sqrt(2) h^3.
  - Der Auftrag nannte "... h^3" je Knoten. Das waere fuer das Pyrochlor-Gitter um den Faktor sqrt(2) zu klein; E und Q
    laegen dann systematisch 29,3 % unter dem Kontinuum.
  - Verbindlich ist v_s = sqrt(2) h^3. Fuer QP4 nenne ich zusaetzlich das Urteil mit h^3 ("Kartenwortlaut" bzw.
    Auftragswortlaut).
- **Energie und Ladung [F, Gitterfassung]:**
  - E = v_s [ sum_i |phi_t,i|^2 + sum_i U(|phi_i|^2) + (1/h^2) sum_Kanten |phi_i - phi_j|^2 ] (jede Kante einmal).
    Daraus folgt genau die Feldgleichung oben.
  - Q = v_s sum_i 2 Im(conj(phi_i) phi_t,i). Ein Zustand phi ~ exp(+i omega t) hat Q > 0.
  - Stationaer, phi = f exp(i omega t) mit reellem f: Q = 2 omega v_s sum f^2,
    E = v_s [omega^2 sum f^2 + sum U(f^2) + (1/h^2) sum_Kanten (f_i - f_j)^2]. Das ist die Normierung von RUNDE-02
    (Q = 2 omega int f^2, E = int (omega^2 f^2 + f'^2 + U)).
- **Kontinuumswerte fuer QP4 [S]:** omega^2 = 0,70: Q = 473,413, E = 428,641, f0^2 = 1,135060 (RUNDE-02/tests1d,
  lauf-69/ausgabe/tests1d_bericht.txt, Test 4; von REGEL-1, K1, auf 4,8e-6 bestaetigt). Gegenprobe im Code: eigener
  3D-Radialloeser (Schiessen, DOP853, Schwanz C exp(-kappa r)/r), nur Kontrolle.

## 3. Schreibtisch vorab [M]

- **Spektrum:** A(k) = B(k)^+ B(k) - 2 (Liniengraph des Diamantgitters, B = 2x4-Inzidenz). Zwei Eigenwerte sind exakt -2,
  die beiden anderen 2 +- |f(k)| in [-2, 6]; die untere Bande beruehrt die flachen bei Gamma.
  - Auf dem Torus L^3: genau 8 L^3 + 1 Eigenwerte bei -2 (zwei je k-Punkt plus Gamma).
- **Sechserringe:** Jeder einfache Sechserzyklus des Pyrochlor-Gitters ist ein Hexagon (Liniengraph eines
  Diamant-Sechserrings, Taillenweite 6): sechs verschiedene Tetraeder, oben und unten im Wechsel, keine Sehnen.
  - Jeder Nachbar ausserhalb liegt in genau einem Ring-Tetraeder und sieht genau zwei Ringknoten mit +1 und -1.
    Darum gilt A v = -2 v.
  - "Nicht jeder geschlossene Sechserweg ist geeignet" betrifft geschlossene Wege mit Wiederholung, etwa ein Dreieck
    zweimal: Der Wechsel +-1 hebt sich dort auf.
  - Der Code zaehlt alle geschlossenen Sechserwege ab einem Knoten und prueft jeden einfachen (Rauch r1a [E]: 1512
    Wege, 12 gerichtete einfache = 6 Hexagone je Knoten, alle mit 6 verschiedenen Tetraedern und Residuum 0).
- **Ring nichtlinear:** Fuer f = a v gilt |f|^2 = a^2 auf allen 6 Ringknoten und 0 sonst, also U'(|f|^2) f = U'(a^2) f
  (ausserhalb ist f = 0). Mit (A - 6) f = -8 f folgt omega^2 = 8/h^2 + U'(a^2) exakt. Die Karte stimmt.
  - U'(S) >= 1/3 > 0, also omega^2 > 0 fuer jedes a. U'(S) > 1 genau fuer S > 4/3 (Karte richtig).
  - h = 1: omega^2 = 8,375 / 8,5 / 9,375 / 11 / 16,5 fuer a^2 = 0,5 / 1 / 1,5 / 2 / 3; Band omega^2 in [1, 9].
- **QP1 ist vorab ableitbar [M]:** Die Zeitschritte bilden den Raum der Ringmuster c(t) v exakt auf sich ab, auch in
  IEEE-Arithmetik. Ringknoten tragen exakt +c und -c (Rundung ist vorzeichensymmetrisch), jeder Aussennachbar summiert
  c + (-c) = 0 exakt. Ohne Rauschen bleibt der Leck also exakt 0.
  - QP1 prueft damit den Code (Gitter, Ring, Residuum), nicht die Stabilitaet. Diese misst erst QP2.
- **Bogoliubov im rotierenden Rahmen:** phi = (f + x + i y) exp(i omega t), f reell.
  - x_tt - 2 omega y_t + L+ x = 0 und y_tt + 2 omega x_t + L0 y = 0.
  - L0 = -Delta/h^2 + U'(f^2) - omega^2, L+ = L0 + 2 U''(f^2) f^2.
  - Erstordnungssystem (x, y, x_t, y_t) mit 4N Zeilen; instabil, wenn ein Eigenwert Re lambda > 0 hat.
  - **Sektor m = 3** (Stoerung entlang v, bleibt auf dem Ring): Kreisbahn im Zentralpotential; stabil genau fuer
    4 omega^2 + 2 a^2 U''(a^2) > 0, fuer alle fuenf Amplituden erfuellt.
- **Erwartung aus einer Ringnaeherung [M, Naeherung; nach Rauch r2a/r4a aufgestellt, Abschnitt 8]:**
  - Andere Ringmuster mit Ringimpuls m sehen nur -Delta_m = 6 - 2 cos(2 pi m/6), also 4 / 5 / 7 fuer m = 0 / +-1 / +-2,
    statt 8. Die Kopplung nach aussen wird dabei vernachlaessigt.
  - Die Frequenz bleibt aber an 8/h^2 geheftet. Also ist L0 = -Delta_m - 8 < 0 (h = 1), waehrend
    L+ = L0 + 2 a^2 U''(a^2) fuer grosses a positiv wird.
  - Je Muster gilt lambda^4 + (L+ + L0 + 4 omega^2) lambda^2 + L+ L0 = 0. Bei L+ L0 < 0 gibt es eine reelle
    Instabilitaet (wie Vakhitov-Kolokolov).
  - Werte (m = 0 / +-1 / +-2):
    - a^2 = 3: lambda = 1,22 / 1,07 / 0,62
    - a^2 = 2: m = 0 ergibt 0,95
    - a^2 = 1,5: m = 0 ergibt 0,61
    - a^2 = 1: nur m = +-2, lambda ~ 0,17
    - a^2 = 0,5: keine reelle Instabilitaet in dieser Naeherung, da U'' < 0
  - Schwelle fuer m = +-2: a^2 > 0,86.
- **Folgerung (Erwartung, keine Urteilsaenderung):** Die Ringe ueber dem Band sollten stark instabil sein; QP2 Teil A
  verfehlte dann. Unklar bleiben a^2 = 0,5 (im Band, Kopplung nach aussen) und die genaue Rate bei a^2 = 1.
- **Vergleichsball:** Gitterkorrekturen O(h^2 k^2) am Wandprofil, h = 0,5, Breite ~ 1/kappa = 1,8, R_halb ~ 3,6:
  wenige Prozent oder weniger.

## 4. Numerik [F]

- **Ringgitter:** h = 1, periodisch, L = 8 (8192 Knoten, Kante 22,6) als Hauptgitter. Proben: L = 10, dt/2, Saat 2;
  dazu L = 4 als Abgleich mit Bogoliubov. Der Ring ist das erste Hexagon durch den Knoten nahe der Torusmitte.
- **Integrator:** Stoermer-Verlet (Stoss-Drift-Stoss), symplektisch.
  - Jeder Teilschritt erhaelt Q exakt: sum conj(phi) (A - 6) phi ist reell, und die Drift aendert Im(conj(phi) p) nicht.
  - E schwankt beschraenkt mit O(dt^2).
- **Zeitschritt:** dt = 0,005 (Ringe, omega dt <= 0,02); Probe 0,0025. Ball dt = 0,01 (max. Gitterfrequenz ~ 5,8,
  omega_max dt ~ 0,06).
- **Rauschen (QP2, QP3) [F]:** auf allen Knoten
  - delta phi = 1e-6 a (xi1 + i xi2)/sqrt(2)
  - delta phi_t = 1e-6 a omega (xi3 + i xi4)/sqrt(2)
  - xi unabhaengig standardnormal, Saat 1 (Haupt), Saat 2 (Probe).
- **Stoss (QP3) [F]:**
  - phi(0) = a v exp(-i kappa omega e.x), phi_t(0) = i omega phi(0); e = [100] (kubische Gitterachse), x relativ zur
    Ringmitte (minimales Bild).
  - kappa = 0,02, 0,05, 0,1 ("bis 10 % von omega"). Mit demselben Rauschen wie QP2.
  - Bei exp(+i omega t) laeuft ein Ball mit exp(-i k x) nach +x (wie die Lorentz-Startphase in ZUFALLS-REIBUNG-1).
- **Vergleichsball (QP4) [F]:**
  - h = 0,5, L = 17 (78 608 Knoten, Kante 24,04, halbe Kante 12,0, dort f ~ 3e-3 f0).
  - Zentrum auf dem Knoten nahe der Torusmitte (Inversionszentrum, kein Dipol).
  - Startwert: Kontinuumsprofil am Knotenabstand (eigener Radialloeser), dann Newton auf dem Gitter.
    - Residuum R = -(A - 6) f/h^2 + (U'(f^2) - omega^2) f
    - lineare Schritte mit MINRES (rtol 1e-13)
    - Ziel max |R| <= 1e-10
  - Stoss wie beim Ring: phi = f exp(-i kappa omega x), kappa = 0,1 (Urteil) und 0,02 (beschreibend), T = 200.
  - Kontrolle: ruhender Ball T = 50.
  - Bekannte Kleinigkeit: Die Phase springt an der Torusflaeche, wo f <= 3e-3 ist (Energieanteil < 1e-4).

## 5. Messvorschriften [F, soweit die Karte offen ist]

- **Leckanteil (Hauptmass):** Leck_N(t) = sum_{i nicht Ring} |phi_i|^2 / sum_i |phi_i|^2. Kontrolle:
  Ladungsanteil Leck_Q = Q_aussen/Q.
- **Residuum (QP1):** max_i |R_i| / (omega^2 a), R = -omega^2 f - (A - 6) f/h^2 + U'(|f|^2) f; dazu absolut.
- **Ladungsschwerpunkt:** iteriertes glattes Fenster wie QBALL-GITTER-1.
  - X = X + sum w q d / sum w q mit Ladungsdichte q_i = 2 Im(conj(phi_i) phi_t,i) v_s, d = minimales Bild von x_i - X.
  - Gewicht w = cos^2(pi r/(2 R_w)) fuer r < R_w; iteriert bis |dX| < 1e-12.
  - X wird stetig mitgefuehrt (entfaltet).
  - R_w = 2,5 h (Ring, h = 1) bzw. 8,0 (Ball). Q_fenster = sum w q.
- **Verschiebung:** D(t) = |X(t) - X(0)|, X(0) aus dem Startzustand (mit Stoss). Massgeblich D_ende = D(200).
  Beschreibend max_t D(t).
- **Messabstand 0,5**, Reihen vollstaendig in den JSON-Dateien.
- **Numerische Gueltigkeit [F]** (jeder Lauf, sonst "nicht auswertbar"):
  - max |Q(t)/Q(0) - 1| <= 1e-10 und max |E(t)/E(0) - 1| <= 1e-3
  - Lauf erreicht T

## 6. Urteilsregeln (mechanisch, code/auswertung.py)

- **QP0** (Karte: Flachbandabweichung <= 1e-12 ueber das k-Gitter; Hexagon-Residuum <= 1e-12):
  - k-Gitter: 48^3 Punkte der primitiven fcc-Zelle plus 100 000 Zufallspunkte, je 4x4 Bloch-Matrix
    A_st = 2 cos(k.(b_t - b_s)).
  - Abweichung = max |lambda_1,2(k) + 2|. Residuum = max |A v + 2 v| auf dem L = 8-Torus (Hauptring).
  - Vorbedingung: Gitter- und Ringpruefungen bestanden (6 Nachbarn, 2 Tetraeder je Knoten, Ring ohne Sehnen, jeder
    Aussennachbar mit genau zwei Ringknoten entgegengesetzten Vorzeichens, Tetraeder im Wechsel). Sonst nicht auswertbar.
  - **Eingetroffen**, wenn beide <= 1e-12.
  - Beschreibend: Realraum (L = 4) gegen k-Raum; Zahl der Eigenwerte bei -2 gegen 8 L^3 + 1.
- **QP1** (Karte: Residuum <= 1e-12 fuer alle fuenf Amplituden; ohne Rauschen Leck ueber T = 100 <= 1e-10):
  - Lauf ring-qp1 (L = 8, h = 1, dt = 0,005, kein Rauschen, kein Stoss).
  - **Eingetroffen**, wenn fuer alle fuenf a^2 Residuum_rel <= 1e-12 und max_{t <= 100} Leck_N <= 1e-10, Lauf bis
    T = 100.
- **QP2** (Karte: mit Rauschen 1e-6 bleibt der Ring fuer mindestens eine der Amplituden 1,5; 2; 3 ueber T = 200 kompakt
  (Leck <= 1e-3); fuer 0,5 und 1 zerlaeuft er (Leck >= 1e-2)):
  - Hauptlauf ring-qp2-s1 (L = 8, Saat 1, dt = 0,005).
  - kompakt(a) [F]: max_{t <= 200} Leck_N <= 1e-3; zerlaufen(a) [F]: Leck_N(t = 200) >= 1e-2.
  - Teil A: kompakt fuer mindestens ein a^2 in {1,5; 2; 3}. Teil B: zerlaufen fuer a^2 = 0,5 und 1.
  - **Eingetroffen** genau dann, wenn A und B gelten; sonst nicht eingetroffen. Numerik ungueltig oder Lauf fehlt:
    nicht auswertbar.
  - Proben: dieselbe Regel auf ring-qp2-s2, ring-qp2-L10 und ring-qp2-dt2. Weicht ein Probenurteil ab, steht "nicht
    robust" im Vermerk; massgeblich bleibt der Hauptlauf.
- **QP3** (Karte: ein Stoss bis 10 % von omega verschiebt den Ladungsschwerpunkt eines stabilen Rings ueber T = 200 um
  weniger als einen halben Gitterabstand):
  - Stabile Ringe [F] = Amplituden mit kompakt(a) im QP2-Hauptlauf (alle fuenf a^2 zulaessig).
  - Gibt es keinen stabilen Ring, ist QP3 **nicht auswertbar** (Vermerk); die Stossdaten werden beschreibend berichtet.
  - Je stabile Amplitude und kappa in {0,02; 0,05; 0,1}:
    - D_ende < 0,5 h gilt als "ja"
    - D_ende >= 0,5 h gilt als "nein"
    - nicht messbar, wenn Q_fenster(200) < 0,1 Q_fenster(0) oder die Numerik ungueltig ist
  - **Eingetroffen**, wenn alle "ja"; **nicht eingetroffen**, wenn mindestens ein "nein"; sonst nicht auswertbar.
- **QP4** (Karte: Vergleichsball h = 0,5, omega^2 = 0,7; E und Q hoechstens 5 % vom 3D-Kontinuum; Schwerpunkt > 2
  Gitterabstaende in T = 200 nach einem Stoss):
  - E, Q aus der Newton-Loesung (v_s = sqrt(2) h^3) gegen Q = 473,413, E = 428,641.
  - Stoss kappa = 0,1 [F: derselbe groesste Stoss wie beim Ring]: D_ende > 2 h = 1,0 und Q_fenster(200) >= 0,5
    Q_fenster(0) (Ball heil).
  - **Eingetroffen**, wenn |E/E_k - 1| <= 0,05, |Q/Q_k - 1| <= 0,05 und die Bewegungsbedingung gelten.
  - Newton-Residuum > 1e-10, Numerik ungueltig oder Lauf unvollstaendig: nicht auswertbar.
  - Zusaetzlich berichtet: Urteil mit h^3 je Knoten (Auftragswortlaut), eigener Radialwert gegen die Tabelle, kappa = 0,02.
- **Beschreibend, ohne Urteil:**
  - Bogoliubov-Eigenwerte auf L = 3 und L = 4 (Ring, h = 1). Instabil heisst Re lambda > 1e-5; der Rest wegen der
    Jordanbloecke der Nullmoden ist ~1e-7.
  - Wachstumsrate aus der Zeitentwicklung: Ausgleich ln Leck_N = c + 2 gamma t im Bereich 1e-8 <= Leck_N <= 1e-4,
    L = 8 und L = 4, gegen max Re lambda.
- **Bedeutung:** wie in der Karte vorab. Ein Bedeutungssatz wird nur ausgeloest, wenn die Urteile so ausfallen.

## 7. Laeufe (alle auf der .69 ueber kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde37-pyro)

| Spur | Lauf (Ausgabe lauf/...) | Inhalt | erwartet |
|---|---|---|---|
| cpu3 | linear.json | QP0: k-Gitter 48^3 + 1e5, Realraum L = 4, Ringpruefung L = 2, 3, 4, 8 | ~ 15 s |
| cpu3 | ring-qp1.json | QP1: L = 8, T = 100, kein Rauschen | ~ 40 s |
| cpu3 | ring-qp2-s1.json | QP2 Haupt: L = 8, T = 200, Rauschen 1e-6, Saat 1 | ~ 80 s |
| cpu3 | ring-qp2-s2 / -L10 / -dt2 / -L4 .json | Proben Saat 2, L = 10, dt = 0,0025; L = 4 Abgleich | ~ 6 min |
| cpu4 | bogo-L3.json, bogo-L4.json | Bogoliubov, fuenf Amplituden | ~ 20 s, ~ 4,5 min |
| cpu4 | ring-kick-{0.1, 0.05, 0.02}.json | QP3: L = 8, T = 200, Stoss [100], Rauschen 1e-6 | je ~ 80 s |
| cpu4 | ball-kick-0.1.json | QP4: Newton, E, Q; Stoss 0,1, T = 200 | ~ 3,5 min |
| cpu4 | ball-ruhe.json, ball-kick-0.02.json | Kontrolle ruhend (T = 50), kleiner Stoss | ~ 1,5 und 3,5 min |
| cpu3 | auswertung.json + Bilder | code/auswertung.py lauf | ~ 10 s |

- Aufrufe woertlich in code/laeufe-cpu3.sh und code/laeufe-cpu4.sh. Hoechstens zwei Laeufe zugleich (je Spur einer).
- Jeder Lauf bricht vor 540 s Wandzeit selbst ab (Status "wandzeit"), der Starter nach 600 s.

## 8. Rauchlaeufe vor dem Einfrieren (offengelegt, was ich gesehen habe; Zeiten UTC)

| Lauf | Zeit | Inhalt | gesehen |
|---|---|---|---|
| r1a | 01:57:12 | linear, k 8^3 + 1000, Realraum L = 2 | Flachband 2,2e-15; Realraum gegen k 5,3e-15; 65 = 8 L^3 + 1 Eigenwerte bei -2; Sechserwege wie Abschnitt 3; Ringpruefung L = 2, 3, 4, 8 bestanden |
| r1b | 01:57:13 | Ring L = 3, T = 2, Rauschen, a^2 = 0,5 und 3 | Residuum <= 1,9e-16; Leck ~ 1e-10 (Rauschsockel); dE ~ 1e-9, dQ ~ 1e-15 |
| r2a | 01:57:20 | Bogoliubov L = 2, a^2 = 3 | **reelle Instabilitaet**: Re lambda = 1,124 / 0,975 (2x) / 0,562 (2x) |
| r2b, r3 | 01:57:21, 01:59:26 | Ball omega^2 = 0,8 (nicht 0,7), h = 0,5, L = 12, T = 2 | r2b Klammerfehler im Radialloeser (behoben, Abschnitt 9); r3: Newton in 3 Schritten auf 6e-14; Gitter gegen eigenes Radialprofil E -1,06 %, Q -0,97 %; Stoss 0,1: D(2) = 0,17 |
| r4a | 01:59:26 | Bogoliubov L = 3, a^2 = 2,5 (keine Kartenamplitude) | Re lambda = 0,992 / 0,864 (2x) / 0,499 (2x); 3,9 s |
| r4b | 01:59:31 | Ring L = 8, a^2 = 2,5, Rauschen, T = 10 | Leck waechst bis 3,0e-6 bei t = 10; 0,35 ms je Schritt |
| r5 | 02:03:08 | Auswertepfad mit Kurzlaeufen (L = 3, T = 2, alle fuenf a^2; Ball wie r3) unter den Hauptnamen | ohne Rauschen Leck exakt 0; mit Rauschen Leck 1,0e-10 bis 1,9e-10 bei t = 2; Stoss 0,1: Leck 8e-3 bis 1,2e-2 und D(2) = 0,13 bis 0,15 bei t = 2; Bogoliubov L = 2, a^2 = 2,5: 0,9919; Urteile ohne Bedeutung (Laeufe zu kurz) |

- **Bewertung:**
  - Die reellen Bogoliubov-Eigenwerte aus r2a und r4a liegen bei L = 2 und L = 3 fast gleich (0,99191 und 0,99188 fuer
    a^2 = 2,5). Die Mode ist also oertlich.
  - Muster und Vielfachheiten (1 + 2 + 2) passen zur Ringnaeherung in Abschnitt 3 (m = 0, +-1, +-2). Diese habe ich
    erst nach r2a aufgeschrieben. Sie ist eine Erklaerung, keine unabhaengige Vorhersage.
  - Damit habe ich vor dem Einfrieren gesehen: Die Amplituden 2,5 und 3 sind in der linearen Naeherung instabil. Fuer
    a^2 = 3 (Kartenamplitude) gilt das bei L = 2.
  - Die QP2-Schwellen bleiben unveraendert.
- Keine Schwelle der Karte und keine Regel dieses Plans wurde nach einem Rauchlauf geaendert. Festgelegt wurden nach
  dem Rauch nur:
  - R_w = 2,5 h, die Stossrichtung [100] und die Ballgroesse L = 17. Sie stammen aus der Geometrie, nicht aus
    Rauchergebnissen.
  - die Groessen der Bogoliubov-Laeufe (Laufzeit).

## 9. Code-Aenderungen waehrend des Rauchs

- radial3: Die Klammer des Schiessverfahrens war fuer omega^2 = 0,8 falsch (beide Enden ueberschossen).
  - Neu: unten f0^2 = (S_min + 1 - sqrt(2 omega^2 - 1))/2. Dort ist V_eff(f0) < V_eff(0), also sicher zu kurz.
  - Oben f0^2 = S_max (1 - 1e-4), knapp unter dem Maximum von V_eff.
- auswertung.py: JSON-Ausgabe von numpy-Wahrheitswerten (default-Umwandlung). Sonst unveraendert seit Rauch r5.

## 10. Agenten-Erwartung [H] (vor den Hauptlaeufen, geht in kein Urteil ein)

| Nr | Erwartung |
|---|---|
| A0 | QP0 und QP1 eingetroffen (vorab ableitbar), Abweichungen <= 1e-14 |
| A1 | QP2 nicht eingetroffen: a^2 = 1,5 / 2 / 3 instabil mit Re lambda ~ 0,5 / 0,9 / 1,1; Leck > 1e-3 vor t = 40 |
| A2 | a^2 = 1 instabil mit Re lambda ~ 0,1 bis 0,2, zerlaeuft (Leck >= 1e-2 bei t = 200); a^2 = 0,5 offen (eher stabil) |
| A3 | QP3: falls a^2 = 0,5 stabil ist, bleibt er nach dem Stoss am Ort (D_ende < 0,5 h), nach einem Ladungsverlust von einigen Prozent |
| A4 | QP4: E und Q innerhalb 2 % (Gitter etwas tiefer), Ball laeuft mit v ~ 0,1 (D_ende ~ 20 = 40 h) |

## 11. Nach dem Einfrieren

- Plan und Urteilsregeln bleiben unveraendert. Code nur bei echten Fehlern aendern, mit Offenlegung in ERGEBNIS.md.
- Pruefsummen von Plan und Code in code/pruefsummen-einfrieren.txt.
