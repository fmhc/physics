# QBALL-MONOPOL-1: Plan (Runde 38, Code-Agent)

- Code-Agent fuer die Leitung claude-primary. Karte: KARTE.md (geschrieben ab 07:48:13 CEST).
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 07:49:10 CEST. Agenten-Vorhersagen ab 08:04:27 CEST (AGENTEN-VORHERSAGEN.md, vor dem Lesen jedes
    Rauchlaufs).
  - Rauchlaeufe (UTC): rauch1 06:03:55 bis 06:04:07; rauch2 06:09:29 bis 06:09:42; rauch3 06:09:42 bis 06:10:00;
    rauch4 06:12:11 bis 06:12:18; rauch5 (Auswertungstest) 06:12:18 bis 06:12:21.
  - Plantext ab 08:13:11 CEST.
- **Kennzeichen:** [M] eigene Mathematik (Schreibtisch), [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [S] an der
  Quelle gelesen (hier nur ueber Dossier und SPIN1.md), [P] Projektdatei, [R] im Rauchlauf gesehen, [F] Festlegung
  dieses Plans, [H] Hypothese.
- Karte, Vorhersagen QM0 bis QM4, Schwellen und Wahrscheinlichkeiten gelten unveraendert. Was die Karte offenlaesst,
  ist unten mit [F] festgelegt. Kartenfehler stehen in Abschnitt 7.

## 1. Modell, Eichung, Ansatz [M]

- **Feld und Potential (wie qladung2.py, e -> Hintergrundfeld):** U(S) = S - S^2 + S^3/2, S = abs(phi)^2, Masse 1.
  Topf -V0 exp(-r^2/r_c^2) abs(phi)^2 mit r_c = 1, V0 in {0; 0,5; 1; 2}. Coulomb-Selbstenergie vernachlaessigt (Karte).
- **Eichung:** Dirac, A_varphi = (g/(4 pi r)) (1 - cos theta)/sin theta, String auf theta = pi. D = grad - i q A,
  mu = q g/(4 pi) = 1/2.
- **Ansatz:** phi = f(r, theta) e^(i k varphi) e^(-i omega t), f reell.
  - f reell ist keine Einschraenkung: Eine Phase chi(r, theta) fuegt nur int abs(grad chi)^2 f^2 >= 0 hinzu.
  - Damit abs(D phi)^2 = f_r^2 + f_theta^2/r^2 + W(theta) f^2/(r^2 sin^2 theta), W = (k - mu (1 - cos theta))^2.
- **Wahl von k und Randbedingungen in theta:**
  - Bei theta = 0 ist die Klammer k. f(theta = 0) ungleich 0 verlangt k = 0.
  - Bei theta = pi ist sie k - 2 mu = -1. f muss dort wie (pi - theta) verschwinden: Die Nulllinie liegt auf dem
    String. Das ist der Wirbelfaden aus D2; die Karte verlangt "f verschwindet auf dem String".
  - Gewaehlt: **k = 0**. k = 1 ist das Spiegelbild (Nulllinie bei theta = 0).
- **Wu-Yang-Pruefung:**
  - Suedkarte: A^S = A^N - (g/(2 pi)) grad varphi, also phi_S = e^(-i varphi) phi_N und k_S = -1.
  - Dort ist W_S(theta) = (k_S + mu (1 + cos theta))^2 = (mu (1 - cos theta))^2 = W_N(theta).
  - Beide Karten geben dasselbe Funktional. Der singulaere Teil des Dirac-Potentials sitzt genau auf der Nulllinie von
    f und kostet darum nichts. Ein eigener Rechenlauf ist nicht noetig.
- **Tiefste Monopol-Mode (ein Quant, linear):**
  - Y = (1 + cos theta)^(1/2) loest den Winkeloperator -(1/sin) d(sin d) + W/sin^2 mit Eigenwert 1/2. Ausgerechnet mit
    x = cos theta: (1/4)(1 + x)^(-1/2) [(1 + 3x) + (1 - x)] = (1/2) Y.
  - Das ist j(j + 1) - mu^2 = 3/4 - 1/4 fuer j = 1/2 [L Wu/Yang 1976]. Damit abs(Y)^2 = 1 + cos theta und
    abs(Y)^2(0)/abs(Y)^2(pi/2) = 2.
- **Verhalten bei r = 0:** f ~ r^l mit l(l + 1) = 1/2, l = (sqrt3 - 1)/2 = 0,366. Die naechste Mode (j = 3/2,
  Eigenwert 3,5) geht wie r^1,45. Darum ist die Winkelform dicht am Monopol immer die der tiefsten Mode, wenn deren
  Anteil nicht verschwindet.
- **Feste Ladung:**
  - Q = 2 omega N mit N = int f^2 d^3x. Mit omega = Q/(2N) wird omega^2 N = Q^2/(4N), also
    E_Q[f] = Q^2/(4N) + int [abs(D phi)^2 + U(f^2) - V0 e^(-r^2) f^2] d^3x.
  - Stationaer bei fester Ladung heisst: -D^2 f + U'(f^2) f - V0 e^(-r^2) f = omega^2 f. Lokale Minima von E_Q sind die
    stabilen Q-Baelle bei festem Q.
- **Kato auf dem Gitter:** In der Diskretisierung (Abschnitt 2) ist E_mono[f] = E_frei[f] + sum a f^2 mit a >= 0, exakt
  fuer jedes f auf demselben Gitter.
- **Drehimpuls:**
  - Materieanteil: J_m = 2 omega int f^2 (k - mu (1 - cos theta)).
  - Kreuzanteil mit dem Monopolfeld (Thomson, linear in der Ladungsdichte rho = 2 omega f^2):
    J_x = -mu int rho cos theta.
  - Summe J_z = Q (k - mu) = -Q/2 fuer jede axialsymmetrische Konfiguration, unabhaengig von f. Das Vorzeichen haengt an
    der Orientierung.
  - abs(J_z) = Q/2 ist darum vorab ableitbar. Die Rechnung prueft hier nur den Code.

## 2. Diskretisierung [F]

- **Finite Volumen in (r, theta), Zellmitten:**
  - r-Flaechen gleichabstaendig mit Schritt h bis r_s = 20, danach geometrisch gestreckt (Faktor 1,05) bis Rmax = 40.
  - theta-Flaechen gleichabstaendig, N_t Zellen.
  - Zellvolumina exakt: 2 pi (r_+^3 - r_-^3)/3 (cos theta_- - cos theta_+).
- **Energie:**
  - radial: Flaechenfluesse 2 pi r_f^2 (Delta f/Delta r)^2 V_theta
  - polar: 2 pi L_r sin(theta_f) (Delta f/Delta theta)^2/Delta theta
  - azimutal: 2 pi L_r W(theta_c) V_theta/sin^2(theta_c) f^2
  - Potential und Topf mit Zellvolumen, Mittelpunktswerte
- **Randbedingungen:**
  - f = 0 auf r = Rmax (Dirichlet, halbe Zelle).
  - Bei r = 0, theta = 0 und theta = pi ist das Flaechengewicht 0 (natuerliche Randbedingung).
  - f(theta = pi) -> 0 erzwingt der grosse azimutale Term der letzten Zelle.
- **Pruefung des Winkelteils [R, rauch1]:** Der kleinste Eigenwert des diskreten Winkeloperators (mu = 1/2) ist
  0,49900 / 0,49975 / 0,499937 / 0,499984 bei N_t = 16 / 32 / 64 / 128.
  - Das ist zweite Ordnung gegen 1/2. Die naechsten liegen bei 3,4995 und 8,497 (Soll 3,5 und 8,5).
  - mu = 0 gibt 0, 2, 6.
- **Gitter:**

| Name | h | N_t | Unbekannte | Rolle |
|---|---|---|---|---|
| G (grob) | 0,1 | 32 | 7 936 | Gitterverdopplung |
| H (Haupt) | 0,05 | 64 | 29 504 | **Urteile** |
| F (fein) | 0,025 | 128 | 112 000 | Gitterverdopplung, ohne Eigenwerte |

- **Referenzrechnung 1D:** Mit N_t = 1 und mu = 0 ist dasselbe Programm die radiale Gleichung auf demselben r-Gitter.
  Der kugelfoermige Zustand auf dem 2D-Gitter hat exakt diese Energie [M]; rauch2 zeigt Gleichheit auf alle Stellen.

## 3. Relaxation [F]

- **Verfahren:** Minimierung von E_Q[f] mit gedaempftem Newton.
  - Levenberg-Marquardt in der Metrik 2w (w Zellvolumen), Armijo-Liniensuche, also monoton fallende Energie.
  - Hesse-Matrix duenn (5-Punkt) plus Rang-1-Term aus Q^2/(4N); Loesung mit splu und Sherman-Morrison.
  - Die Karte sagt "Gradientenfluss"; der Hinweis der Leitung erlaubt Newton. Das Verfahren ist eine Relaxation, weil
    nur Schritte mit fallender Energie angenommen werden.
- **Konvergenz:** Newton-Dekrement -g.p < 1e-12 abs(E) bei Daempfung 0. Hoechstens 60 Schritte und 120 s je Fall.
- **Abwanderungs-Stopp:** Der Lauf endet mit Status "abgewandert", sobald der Ladungsschwerpunkt z_c > R_halb(Q) + 4
  liegt.
  - R_halb ist der Halbdichteradius des freien Balls.
  - Grund [R, rauch1 und rauch2]: Auf dem Polargitter hat ein verschobener freier Ball eine kuenstlich tiefere
    Energie (Translationsartefakt).
    - rauch1, alter verformter Start ohne Monopol: z_c bis 8,3 und E bis 0,12 unter dem 1D-Wert (Gitter H).
    - rauch2, freier Ball am Stopp: dE = -0,043 (Q = 200) und -0,369 (Q = 2000), Gitter H.
  - Hinter dem Stopp misst die Rechnung nur noch dieses Artefakt, nicht mehr Monopol oder Topf.
  - Festgelegt nach rauch1, vor dem Einfrieren.
- **Starts** (beide mit dem Winkelfaktor sqrt(1 + cos theta) und dem radialen Profil des freien Balls bei gleichem Q):
  - A: Ball am Monopol (d = 0)
  - B: Ball um d = R_halb entlang +z verschoben
- **Ergebnisgroesse:** E_mono(Q, V0) ist das Minimum der Energie ueber die Starts A und B.
- **Minimum-Pruefung (beschreibend):** die 4 Eigenwerte von Hess(E_Q) v = lambda 2w v nahe -0,2 (Shift-Invert, eigsh),
  nur fuer konvergierte Zustaende auf Gitter H.
- **"haftend" [F]** (fuer QM4 und Beschreibung):
  - Status "konvergiert" (auch "konvergiert (Rundung)")
  - kleinster Eigenwert > -1e-6
  - Ladungsanteil in r > Rmax - 10 kleiner als 1e-6

## 4. Referenzen [F]

- **E_frei(Q):** freier Ball (mu = 0, V0 = 0), 1D auf demselben r-Gitter.
  - Kontrolle gegen qladung2 [R, rauch1]: Q = 473,413 gibt 428,6268 / 428,63796 / 428,64075 bei h = 0,1 / 0,05 / 0,025.
  - Richardson ergibt 428,6417 (qladung2: 428,64169).
- **E_topf(Q, V0):** Ball am Topf ohne Monopol, 1D auf demselben r-Gitter. Im kugelfoermigen Topf ist das Minimum
  kugelfoermig [M].
- **E_frei,2D,verschoben(Q):** freier Ball auf dem 2D-Gitter, Start bei d = R_halb + 2, gleicher Abwanderungs-Stopp.
  Er misst das Translationsartefakt am Stopp (Referenz fuer QM1, Abschnitt 6).

## 5. Raster [F]

- **Q:** {150; 200; 300; 500; 1000; 2000}, je V0 in {0; 0,5; 1; 2}, Starts A und B. Dazu QM0 bei Q = 473,413.
- **Begruendung fuer 150 statt 50 und 100** (Hinweis der Leitung "z. B. 50, 100, ..."):
  - Der freie M1-Ball existiert nur fuer Q >= Q_min ~ 112. Laut fam-e0.json [P] liegt das Minimum Q = 112,15 bei
    omega^2 = 0,92.
  - Fuer Q < Q_s ~ 142 gilt E/Q > 1 (E/Q = 1 zwischen omega^2 = 0,84 und 0,86 [P]). Dort ist der zerflossene Zustand
    (E ~ Q) billiger als der Ball.
  - Ein Vergleich E_mono < E_frei koennte dann vom Zerfliessen statt vom Haften kommen. Ab Q = 150 ist das
    ausgeschlossen: Teilzerfliessen kostet E_frei(Q1) + (Q - Q1) > E_frei(Q), weil dE/dQ = omega < 1.
- **Beschreibend (nach den Urteilen):** Q_max je V0 per Bisektion in log Q, 7 Schritte, Gitter H. Nur dort, wo die
  Bindung im Raster endet.

## 6. Urteilsregeln (Gitter H; Werte in lauf-69/auswertung.json, mechanisch durch code/auswertung.py)

- **Bindung [Karte]:** gebunden(Q, V0) heisst E_mono(Q, V0) < (1 - 1e-3) E_frei(Q).
- **QM0 [Karte]:** 2D-Relaxation mit mu = 0 und V0 = 0 bei Q = 473,413.
  - Start [F]: z-symmetrisch verformter Ball f_1(r) (1 + 0,3 P_2(cos theta)). Ein Start ohne z-Symmetrie regt die
    Translationsnullmode an und laeuft ins Artefakt (rauch1).
  - eingetroffen, wenn abs(E/428,641 - 1) <= 1e-3.
  - Beschreibend: z_c und D(0)/D(pi/2) als Kugeltest.
- **QM1 [Karte, mit Gitterreferenz F]:** fuer alle Raster-Q gilt E_mono(Q, V0 = 0) >= E_ref(Q). Dabei ist
  E_ref = min(E_frei(Q), E_frei,2D,verschoben(Q)).
  - Grund: Die Kato-Ungleichung gilt auf demselben Gitter. Der 1D-Wert ist dort wegen des Translationsartefakts nicht das
    Infimum.
  - Festgelegt nach rauch2: Dort lag Q = 2000, V0 = 0 um 0,149 unter E_frei (1D), aber 0,22 ueber dem verschobenen freien
    Ball.
  - **Urteil nach Kartenwortlaut** (gegen E_frei 1D) wird daneben genannt.
- **QM2 [Karte]:** eingetroffen, wenn es V0 in {0,5; 1; 2} und Raster-Q mit gebunden(Q, V0) gibt.
- **QM3 [Karte, F]:** eingetroffen, wenn es V0 in {0,5; 1; 2} gibt, fuer das mindestens ein Raster-Q gebunden ist und
  Q = 2000 nicht.
  - Q_max(V0) ist das groesste gebundene Raster-Q.
  - Ohne jede Bindung: "nicht eingetroffen" mit Vermerk, weil der Wortlaut das Ende einer Bindung verlangt.
- **QM4 [Karte, F]:**
  - Messgroesse D(theta) = int f^2(r, theta) r^2 dr entlang des Strahls (quadratisch auf theta = 0 extrapoliert, bei
    pi/2 gemittelt). Verhaeltnis D(0)/D(pi/2); Band [1,8; 2,2] aus der Karte (2 auf 10 %).
  - Diese Groesse stand vor rauch1 im Code (sha256 71244bf9...).
  - "kleines Q": das kleinste Raster-Q, an dem fuer mindestens ein V0 > 0 der beste Zustand haftend ist.
  - eingetroffen, wenn dort alle haftenden V0 im Band liegen. Kein haftender Zustand im Raster: "nicht auswertbar".
  - Beschreibend: punktweises Verhaeltnis am Radius der groessten Kugelmittel-Dichte, lokaler Exponent an r -> 0
    (Soll 0,366).
- **Drehimpuls (beschreibend):** J_m, J_x, J_z; Erwartung J_z + Q/2 = 0 auf Rundung.
- **Gitterverdopplung (beschreibend):** Bindungen auf G, H, F. Wechselt ein Urteil zwischen H und F, wird das als
  Vermerk "Gitter-Grenzfall" genannt; geurteilt wird auf H.

## 7. Kartenfehler und Berichtigungen (vor dem Einfrieren)

- **K1 (Q-Raster im Hinweis):** Q = 50 und 100 liegen unter Q_min ~ 112. Dort gibt es keinen freien Ball, E_frei ist
  undefiniert. Berichtigung: kleinstes Raster-Q 150 (Abschnitt 5).
  - Kartenwortlaut: Die Karte selbst nennt kein Raster; QM3 nennt "Q bis 2000". Das ist erfuellt.
- **K2 (QM1 vorab ableitbar):**
  - Diskretes Kato ist eine Identitaet (Abschnitt 1). Ohne Topf wandert der Ball ab, ein haftender Zustand existiert
    nicht.
  - QM1 prueft darum den Code und die Referenzwahl, keine Physik (die Karte nennt QM1 "Kontrolle").
  - Die 1D-Referenz ist wegen des Translationsartefakts nicht gitterrein; berichtigt in Abschnitt 6. Das Urteil nach
    Kartenwortlaut wird mitgemeldet.
- **K3 (QM4 Messgroesse unbestimmt):**
  - "abs(phi)^2(theta = 0)/abs(phi)^2(theta = pi/2)" nennt keinen Radius. Fuer einen nichtlinearen Ball haengt das
    Verhaeltnis vom Radius ab.
  - Dicht am Monopol ist es fuer jede Konfiguration 2, weil die j = 1/2-Mode mit r^0,366 dominiert (Abschnitt 1); in
    dieser Lesart waere QM4 vorab ableitbar.
  - Festgelegt: strahlintegriert (Abschnitt 6).
  - "kleines Q" gibt es im M1-Modell nicht unter Q ~ 112. Im linearen Grenzfall Q -> 0 waere die Form exakt die Mode,
    aber nur bei gebundener Einzelmode. Der Gauss-Topf bindet ohne Monopol erst ab V0 ~ 2,68 [L?], mit Monopol noch
    spaeter. Bei V0 <= 2 gibt es also keinen linearen Grenzfall.
- **K4 (Drehimpuls vorab ableitbar):** J_z = Q(k - mu) gilt identisch im Ansatz (Abschnitt 1). "J = Q/2 pruefen" ist
  eine Codeprobe.
  - Die Bedeutungszeile zu QM2 ("J = Q/2 + Z, bei ungeradem Q ein Fermion") ist eine Quantenaussage (Dossier D1). Die
    klassische Rechnung zeigt nur J_z = -Q/2 und prueft keine Statistik.
- **K5 (Relaxationsart):** LM-Newton statt Gradientenfluss (Abschnitt 3); vom Hinweis der Leitung gedeckt.

## 8. Vorwissen aus den Rauchlaeufen (offengelegt)

- **rauch1** (Gitter G und H): Q = 200, V0 = 2, nur Start A.
  - E = 193,259 (G) bzw. 193,287 (H) gegen E_frei = 194,287 bzw. 194,293. Das ist eine Bindung von etwa 1,0, also
    0,5 %. **Damit ist QM2 nach Plan sehr wahrscheinlich eingetroffen.** Mein A1 ("keine Bindung") ist damit
    wahrscheinlich falsch.
  - Der Zustand sitzt nicht zentriert: z_c = 2,82 bei R_halb = 2,38, der Monopol liegt also am unteren Rand des Balls.
    D(0)/D(pi/2) = 22,4.
  - J_z = -100,000; lokale Exponenten an r -> 0 0,375 bis 0,38.
- **rauch1, QM0 mit dem alten Start f_1 sqrt(1 + cos theta):** wanderte ab (z_c = 14,5 bzw. 8,3); E lag 1,59 (G) bzw.
  0,12 (H) unter dem 1D-Wert. Daraus folgen der symmetrische Start (Abschnitt 6) und der Abwanderungs-Stopp
  (Abschnitt 3).
- **rauch2** (Gitter H):
  - QM0 mit symmetrischem Start: E = 428,637955 = 1D-Wert; z_c = 2e-10; D(0)/D(pi/2) = 1,0000000006; Abweichung zur
    Tabelle -7,1e-6. QM0 ist damit absehbar.
  - V0 = 0: Q = 200 abgewandert mit E = 194,3164 (B) > E_frei = 194,2935. Q = 2000 abgewandert mit E = 1652,370 (A) <
    E_frei = 1652,519.
  - Artefaktkontrolle: freier Ball verschoben 1652,150 (Q = 2000), 194,250 (Q = 200).
- **rauch3** (Gitter F, Zeitprobe): Q = 1000, V0 = 0, Start A: abgewandert nach 18 Schritten in 17,3 s, E = 859,671
  > E_frei = 859,579.
- **rauch4:** wie rauch1 (Q = 200, V0 = 2, A, Gitter H) mit Eigenwerten 0,068 / 0,221 / 0,227 / 0,236. Der Zustand ist
  ein lokales Minimum.
- **rauch5:** Auswertungstest an rauch4. Er brach im Profilbild ab (nur ein Q im Testraster); das ist vor dem Einfrieren
  behoben.
- **Nicht gesehen:** V0 = 0,5 und 1, alle anderen Q bei V0 = 2, Start B bei V0 > 0, Gitter F bei V0 > 0.

## 9. Laufplan (nach dem Einfrieren; alles p4000a, nacheinander)

1. haupt: Gitter H, alle V0, Q und Starts, QM0, npz -> lauf/haupt.json, haupt.npz
2. grob: Gitter G, gleiches Raster -> lauf/grob.json
3. fein: Gitter F, je V0 ein Lauf (fein-v2, fein-v1, fein-v05, fein-v0), eig = 0, zeitgrenze 40 s je Fall
4. qmax (beschreibend): Gitter H, nur V0 mit Ende der Bindung im Raster -> lauf/qmax.json
5. auswertung.py -> lauf/auswertung.json und Bilder (bild-bindung.png, bild-winkel.png, bild-profil.png)

- Laufzeit nach Rauchlaeufen: Gitter H 1 bis 3 s je Fall, Gitter F etwa 1 s je Newton-Schritt.
- Bricht ein Lauf an der 600-s-Grenze ab, bleibt das bis dahin gesicherte JSON gueltig. Fehlende Faelle werden als
  "nicht gerechnet" gemeldet.

## 10. Agenten-Vorhersagen

- AGENTEN-VORHERSAGEN.md (ab 08:04:27 CEST, vor dem Lesen von rauch1) gilt unveraendert. Nach rauch1 ist A1
  wahrscheinlich verfehlt (Abschnitt 8).
