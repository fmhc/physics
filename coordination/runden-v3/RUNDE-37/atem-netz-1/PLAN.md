# ATEM-NETZ-1: Plan (Code-Agent fuer Leitung claude-primary, Runde 42)

- Agent-Start 2026-10-04 18:01:21 CEST (date). Plan geschrieben ab 2026-10-04 18:23:36 CEST (date), vor jedem
  Hauptlauf. Karte: KARTE.md (Modell, Vorhersagen AN0-AN4 und Wahrscheinlichkeiten dort; hier unveraendert, nicht neu
  bewertet). Zeitbox 150 min ab Start.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [L] Gedaechtnis, [L?] unsicher, [S] an der Quelle gelesen,
  [H] Hypothese, **[Z-A]** eigene Zusatzvorgabe des Code-Agenten (nicht aus der Karte, mit Grund).
- Einheiten wie Karte: Laenge PU (Ruhedurchmesser 1), Zeit Takte (omega = 2 pi je Takt). Die Phase ist ein innerer
  Freiheitsgrad; raeumlich werden 1D, 2D und 3D getrennt ausgewiesen.

## 1. Literatur (Kartenauftrag 0; 2 Abrufe, lokale Kopien in quellen/)

- **Abruf 1** (arXiv-API, 18:10:10 CEST, quellen/arxiv-api-abruf1.xml, 17 Eintraege): Abfrage
  `(au:Moessner AND au:Chalker) OR (ti:pulsating AND ti:active AND ti:matter)`. Ein erster Versuch 18:10:03 ueber http
  lieferte 0 Byte (Weiterleitung, kein Inhalt); siehe Selbstanzeigen.
- **Abruf 2** (Volltext, 18:10:31 CEST, quellen/moessner-chalker-cond-mat-9807384v1.pdf): R. Moessner, J. T. Chalker,
  "Low-temperature properties of classical, geometrically frustrated antiferromagnets", PRB 58, 12049 (1998),
  cond-mat/9807384. Gelesen S. 1-10 [S]:
  - S. 3: XY-Spins auf dem Pyrochlor-Tetraeder: "there is only one continuous degree of freedom ... Ground states are
    therefore the configurations with two pairs of antiparallel spins." Also: Grundzustand = zwei Gegentakt-Paare mit
    freiem Winkel, wie im Schreibtisch.
  - S. 6: Die Nullmoden des XY-Pyrochlors sind geschlossene Linien antiparalleler Spins; jede Linie traegt einen freien
    Winkel ("a zero mode involves changing one such angle").
  - S. 8-9: Ordnung durch Unordnung gibt es nur fuer q = 4, n = 2 (XY-Pyrochlor) und q = 3, n = 3 (Heisenberg-Kagome).
    Fuer XY: "The predicted collinear order for XY spins is confirmed: there is long-range order in P(r)"; bei
    T = 5e-4 J ist P(r -> unendlich) ~ 0,86 (N = 864). Erwartet wird ein Uebergang erster Ordnung (nicht geprueft).
  - Definition [S]: P(r) = (n/(n-1)) (<(S0.Sr)^2> - 1/n), fuer n = 2 also P(r) = <cos 2(theta_0 - theta_r)>.
  - S. 10, Abb. 12: 1 - P(1) ~ sqrt(T/J); abgelesen P(1) ~ 0,91 bei T/J = 5e-4, ~ 0,84 bei 1e-3 (interpoliert),
    ~ 0,81 bei 1,25e-3, ~ 0,73 bei 2,5e-3. Abb. 11: P(1) ~ 0,4 bei T/J = 1e-2.
  - Dynamik [S]: "For XY spins, we are able to equilibrate P(r) ... but not Q(r): collinear order presumably hinders
    relaxation"; MC brauchte bis 1,5e6 Schritte je Spin.
  - **Befund fuer die Karte:** Der [L?]-Satz der Karte stimmt an der Quelle: Bei n = 2 waehlt thermisches Rauschen die
    kollinearen Zustaende, und kollinear plus Zeigersumme 0 heisst zwei plus, zwei minus je Tetraeder (Eisregel mit einer
    gemeinsamen Achse). Das ist eine Gleichgewichtsaussage (Monte Carlo), keine Aussage ueber unsere Phasendynamik.
- **Pulsating active matter** [S, nur Zusammenfassungen aus Abruf 1]:
  - Zhang, Fodor, PRL 131, 238302 (2023), arXiv:2208.06831: dichte abstossende Teilchen mit periodischer
    Groessenaenderung; "the competition between repulsion and synchronisation triggers an instability ... from spiral
    waves to defect turbulence". Die Abstossung wirkt also gegen den Gleichtakt; Gleichtakt kommt dort aus einer
    zusaetzlichen Synchronisationskopplung. Das stuetzt den Schreibtisch (Gleichtakt braucht etwas Zusaetzliches).
    Modellgleichungen nicht an der Quelle gelesen [L?].
  - Casagrande, Manacorda, Fodor, arXiv:2605.25996 (2026): Defekte in pulsierender Materie sind beweglich durch einen
    Ratscheneffekt aus Oszillation und Abstossung. Naechster Literaturbezug zu Kartenfrage (c) Pumpen; dort wandern
    Defekte, nicht Dreiecke.
  - Pineros, Fodor, PRL 134, 038301 (2025), arXiv:2403.16961: verzerrte Ensembles; geometrisch frustrierte Packungen.
  - [L] Tjhung, Berthier 2017 (aktiv verformbare Teilchen, Verfluessigung durch Atmen) und Shapere/Wilczek 1989
    (geometrische Phase): nur Gedaechtnis, nicht abgerufen.

## 2. Pruefung des Schreibtischs (vor jeder Rechnung) [M]

**Ergebnis: Mittelung und Vorzeichen stimmen. Die Gueltigkeitsbedingung der Karte ist unvollstaendig; daraus folgen
vier Ergaenzungen, die die Auswertung betreffen (K1-K4). Keine Rechnung wurde wegen eines Fehlers zurueckgestellt.**

- **Mittelung:** Paar im Abstand 1 - delta: h = delta + (eps/2)(s1 + s2), s_i = sin phi_i. U = (k/2) h^2. Mit <s> = 0,
  <s^2> = 1/2, <s1 s2> = (1/2) cos(phi_1 - phi_2): <U> = const + (k eps^2/8) cos(phi_1 - phi_2). Stimmt.
- **Vorzeichen:** Volle Gleichung phi_i' = omega - mu k (eps/2) cos(phi_i) sum_j h_ij. Der Kreuzterm
  -(mu k eps^2/4) cos(phi_i) sin(phi_j) mittelt sich zu +(mu k eps^2/8) sin(theta_i - theta_j). Mit K = mu k eps^2/8:
  theta_i' = K sum_j sin(theta_i - theta_j); fuer das Paar Delta' = 2K sin Delta. Delta = 0 instabil, Delta = pi stabil,
  Rate 2K. Stimmt: gemittelt ein XY-Antiferromagnet mit Kopplung K auf dem Beruehrungsgraphen; Gleichgewichtsverteilung
  exp(-(K/T) sum cos), also T/K entspricht T/J bei Moessner/Chalker.
- **K1 (Gueltigkeit, Einfrieren):** In erster Ordnung in eps steht ein Einzelpunkt-Term
  -a_i cos(phi_i) mit a_i = mu k (eps/2) z_i delta (z_i = Zahl der Beruehrungen). Er mittelt sich weg, ist aber um den
  Faktor 4 z delta/eps groesser als K (hier 4,8 z). Die Mittelung braucht also a_i << omega, nicht nur K << omega.
  Fuer a_i >= omega bleibt die Phase stehen (Adler-Gleichung): **Takt-Stillstand** bei
  kappa_c = eps/(4 z delta) mit kappa = K/omega [M]. Hier (eps = 0,1, delta = 0,12): z = 1: 0,208; z = 2: 0,104;
  z = 4: 0,052; z = 6: 0,035. Schwache Kopplung kappa_w = 0,005 hat a/omega = 0,024 z (Pyrochlor 0,144).
- **K2 (eingefroren ist nicht Gleichtakt):** Eingefrorene Punkte stehen nahe sin(phi) = -1 (kleinster Durchmesser) oder,
  nahe der Schwelle, bei einem gemeinsamen Winkel. Ihre Phasendifferenzen sind dann ~ 0. Ein Phasenmass wuerde das als
  Gleichtakt zaehlen. **Festlegung:** Gleich- und Gegentakt werden zusaetzlich nur unter laufenden Punkten gezaehlt;
  ein eingefrorener gleichphasiger Zustand heisst "Stillstand", nicht Gleichtakt.
- **K3 (Verstimmung):** Die Adler-Verschiebung der mittleren Frequenz ist ~ a_i^2/(2 omega), haengt also an z_i.
  Ungleiche Beruehrungszahlen verstimmen die Takte (Rand fester Gitter, freie Packungen). Teil A und B nutzen daher
  periodische Gitter mit gleichem z (Ausnahme: offene Kette, Verstimmung der Enden ~ 0,17 K, vernachlaessigbar).
- **K4 (AN2 fast ableitbar):** Alle gleichfoermigen Zustaende (Zufallslast, alle eingefroren gleichphasig) skalieren mit
  z, also kappa_c(Diamant)/kappa_c(Pyrochlor) = 6/4 = **1,5 genau**. Nur der geordnete laufende Pyrochlor-Zustand
  (Nachbarsumme der Sinus = -2 s_i statt -4 s_i auf dem Diamant) gibt eine Last cos(phi)(6 delta + 2 eps sin phi), also
  kappa_c = eps/(4 * 0,7456) = 0,0335 gegen 0,0521 auf dem Diamant: Verhaeltnis 1,55. **Die Schwelle der Karte (1,5)
  liegt genau auf dem Koordinationswert.** Ein Treffer bei ~ 1,5-1,55 waere die Koordinationszahl, kein
  Frustrationsbefund. Hysterese [M]: der gleichphasige Stillstand existiert schon ab kappa ~ 0,0283 (Pyrochlor) bzw.
  0,0424 (Diamant).
- **K5 (AN1 teilweise ableitbar):** Auf der Grundzustandsmenge (Zeigersumme 0) ist jedes Tetraeder automatisch "2 + 2"
  bezueglich seiner eigenen Achse (Phasen {0, pi, a, a + pi}) [M]. Zeigersumme und Anteil 2 + 2 messen also nur das
  Erreichen der Grundzustandsmenge (schnell, ~ 1/K). Nicht ableitbar bleibt allein die **Kollinearitaet**. Im
  Gleichgewicht waere sie bei T/K = 1e-3 erfuellt (P(1) ~ 0,84 [S]); offen ist, ob die Dynamik dorthin kommt.
  **Vorab-Erwartung des Code-Agenten [H]** (aendert die Kartenwahrscheinlichkeit nicht): Die Auswahl durch Rauschen ist
  eine Drift der Ordnung T entlang der Linienwinkel; bei T = 1e-3 K reichen 10 000 Takte (~ 315/K, Abschn. 10) dafuer
  voraussichtlich nicht; Kollinearitaet unter 0,8 erwartet.
- **K6 (AN3-Kontrolle ableitbar):** Ohne Atmen (eps = 0) gibt es nach der Entspannung keine Kraft mehr, die Lagen
  bewegen sich nicht (kein Lagerauschen im Modell) [M]. "MSD >= 2 x Kontrolle" ist dann durch jede Bewegung erfuellt,
  auch durch blosses Mitschwingen. Deshalb nach Plan zusaetzlich eine absolute Schwelle (Abschn. 7).
  Auf dreiecksreichen Beruehrungsnetzen ist das Ideal cos(120 Grad) = -0,5; -0,5 oder tiefer braucht viele
  zweifaerbbare Beruehrungen [M].
- **K7 (Pumpen, Einzeldreieck) [M]:** Drei Punkte, die sich dauernd beruehren, mit Seiten l_ij = (d_i + d_j)/2 und
  ueberdaempften Lagen mit gleicher Beweglichkeit: Zentralkraefte geben sum_i (x_i - X) x x_i' = 0, die Bedingung der
  "fallenden Katze". Rechnung in Jacobi-Koordinaten: Kruemmung am gleichseitigen Dreieck (Seite s) = sqrt(2)/s^2 je
  Flaeche in den massegewichteten Formkoordinaten; die Seitenschleife bei 120-Grad-Phasen hat in Seitenlaengen die
  Flaeche (3 pi/8) eps^2, in Formkoordinaten (pi/(2 sqrt 2)) eps^2. **Drehung je Takt = (pi/2) eps^2 / s^2 = 0,0157 rad
  (s = 1)**, Vorzeichen = Drehsinn der Phasen; Gleichtakt dreht nicht. Ein freies Dreieck pumpt also im Prinzip;
  Teil C0 prueft die Zahl, die Packung (AN4) ist nicht ableitbar.
- **Gleichtakt:** entsteht durch die Huelle allein nicht (gemittelt antiferromagnetisch); Ausnahme nur der Stillstand
  aus K2.

## 3. Parameter (fuer alle Teile gleich)

- eps = 0,10 PU; feste Gitter: Beruehrungsabstand 1 - delta mit delta = 0,12 > eps, also h >= 0,02 > 0 immer (dauernd
  beruehrend). Uebernaechste Nachbarn liegen in allen Gittern bei >= 1,24 PU > 1 + eps (beruehren nie) [M].
- k = 1, mu_x = mu_phi = mu (Karte legt das Verhaeltnis nicht fest; [Z-A], gleiche Beweglichkeit wie bei K7).
  kappa = mu eps^2/(8 omega). **Schwach kappa_w = 0,005** (mu = 25,1 je Takt, K = 0,0314 je Takt, 1/K = 31,8 Takte).
  **Stark:** Teil B Abtastung kappa = 0,01 bis 0,3 (26 Werte, logarithmisch); Teil C kappa_s = 0,05.
- Alle omega_i = omega (Finn: "im gleichen Takt").
- **Kleines Rauschen:** T = 1e-3 K(kappa_w) = 3,14e-5 je Takt, in Teil B und C absolut gleich (Teil A: T = 0).
  Grund: Bei T/J = 1e-3 liegt die Gleichgewichts-Kollinearitaet ueber 0,8 [S], Zeigersummen-Rauschen ~ sqrt(4T/K)/4
  ~ 0,016 << 0,1 [M].
- Integrator: stochastischer Heun, volle Dynamik dt = 0,01 Takt (feste Gitter), gemittelt dt = 0,1 Takt (Teil A) bzw.
  0,05/K (B3). Teil C: dt = 0,004 (schwach, Kontrolle), 0,0004 (stark).
- Takt-Mittel: Phasen relativ zu omega t ueber jeden Takt gemittelt (theta_quer = arg Mittel exp(i(phi - omega t))),
  Lagen ueber jeden Takt gemittelt (entfaltet). Alle "langsamen" Masse benutzen Takt-Mittel.
- **Eingefroren:** mittlere Phasengeschwindigkeit ueber W Takte < 0,1 omega (W = 10 in B1, 50 in B2 und C).

## 4. Teil A: Kontrollen (feste Lagen, T = 0, Zufallsphasen, volle und gemittelte Dynamik)

- Paar (8 Saaten, 400 Takte); Kette offen N = 32 (1D); Quadrat 16 x 16 periodisch (2D); Dreieck 18 x 18 periodisch (2D);
  Diamant 5 x 5 x 5 kubische Zellen periodisch, N = 1000 (3D). Je 6 Saaten, 3000 Takte (~ 94/K). Gleiche Anfangsphasen
  fuer volle und gemittelte Dynamik.
- Masse am Ende (Takt-Mittel des letzten Takts): Gegentakt-Ordnung = Mittel ueber Beruehrungen von -cos(Delta);
  Dreieck: Drehsinn chi = (2/(3 sqrt 3)) (sin(b-a) + sin(c-b) + sin(a-c)) je Elementardreieck (a, b, c gegen den
  Uhrzeigersinn), Mittel und Minimum von |chi|. Paar: Abstand pi - |Delta|.
- Vergleich voll gegen gemittelt: Paar: Rate aus Anpassung von ln(pi - |Delta|) gegen t (Bereich 0,003 bis 0,3) gegen
  die Vorhersage 2K; Gitter: t_halb = erster Takt, an dem e(t) = Mittel cos(Delta) die Mitte zwischen Anfangs- und
  Endwert erreicht; Verhaeltnis voll/gemittelt.
- Grund fuer periodische 2D/3D-Gitter: K3. Grund fuer die Groessen: Eine einzelne globale Verdrillung (Windung um den
  Torus, bei T = 0 metastabil) senkt die Gegentakt-Ordnung im Quadrat 16 auf 0,962, im Diamant 5 auf 0,951 und
  laesst den Drehsinn im Dreieck 18 ueber 0,9 [M]; je kleiner das Gitter, desto eher faellt eine Kontrolle nur an
  einer Verdrillung.

## 5. Teil B: Finns Netz (Pyrochlor) und Diamant, feste Lagen, volle Dynamik

- Pyrochlor 4 x 4 x 4 kubische Zellen periodisch: N = 1024, 3072 Beruehrungen, 512 Tetraeder (z = 6). Diamant
  5 x 5 x 5: N = 1000 (z = 4). Konstruktion ueber ganzzahlige Koordinaten (Pyrochlor = Mitten der Diamant-Bindungen,
  Tetraeder = Diamant-Plaetze).
- **B1 (schwach):** kappa_w, T = 1e-3 K, Zufallsphasen, **10 000 Takte** (Rauchlauf: 31 ms je Takt, 20 000 Takte
  waeren ueber 10 min; Abschn. 10). Pyrochlor Saaten 1 und 2, Diamant Saat 1 (die Diagnose T = 0 entfaellt, B3 hat sie).
  (Saat 1). Alle 100 Takte:
  - Anteil Tetraeder mit |Zeigersumme|/4 < 0,1; Mittel |Summe|/4;
  - **Kollinearitaet P(1)** = Mittel ueber Beruehrungen von cos 2(Delta) [S-Definition]; **nematische Ordnung S** =
    |Mittel exp(2 i theta)| (global); Mittel der Tetraeder-Kollinearitaet |sum exp(2 i theta)|/4;
  - 2 + 2 / 3 + 1 / 4 + 0: Vorzeichen von cos(theta - Achse) mit Achse = arg(sum exp(2 i theta))/2 je Tetraeder;
  - Anteil eingefrorener Takte (W = 10). Diamant: Gegentakt-Ordnung, Untergitter-Ordnung, S, P(1), eingefroren.
- **B2 (stark):** je kappa (26 Werte 0,01 bis 0,3) und Saat (1, 2): Zufallsphasen, 200 Takte (Abschn. 10), T wie B1, Anteil
  eingefrorener Takte ueber die letzten 50 Takte. kappa_50 = erstes kappa, bei dem das Saatenmittel >= 0,5 ist,
  logarithmisch linear interpoliert mit dem vorigen Gitterpunkt (liegt schon der erste Punkt >= 0,5: "unterhalb des
  Bereichs"; nie >= 0,5: "nicht bestimmbar"). R = kappa_50(Diamant)/kappa_50(Pyrochlor). Dazu Muster: Anteil
  eingefroren je Untergitter (Diamant), Verteilung eingefrorener Ecken je Tetraeder (Pyrochlor), mittleres sin(phi) der
  eingefrorenen Punkte, cos(Delta) unter laufenden Paaren.
- **B3 (Diagnose, [Z-A]):** gemittelte XY-Dynamik auf demselben Pyrochlor bis t = 5e4/K, dt = 0,1/K (T/K = 0 und 1e-3; Abschn. 10), um zu sehen,
  wohin die Phasen nach sehr langer Zeit laufen. Kein Urteil daraus.

## 6. Teil C: freie Punkte (2D N = 500, 3D N = 1000, periodische Kaesten)

- Fuellgrad (Ruhedurchmesser): 2D 0,80 / 0,84 / 0,88; 3D 0,60 / 0,64 / 0,68. Zufallslagen, Entspannung ohne Atmen
  (eps = 0, mu wie schwach) 50 Takte, dann Zufallsphasen (gleiche Saat fuer alle Bedingungen), Bedingungen:
  schwach (kappa_w; 2D 300, 3D 200 Takte), stark (kappa_s = 0,05; 2D 50, 3D 15 Takte, Kostengrund, Abschn. 10),
  Kontrolle eps = 0 (2D 300, 3D 200 Takte). Messfenster: ab Takt 50 bzw. bei kurzen Laeufen ab einem Drittel.
- **Gegentakt-Korrelation an Beruehrungen:** Mittel von cos(phi_i - phi_j) ueber alle Paare mit h_ij > 0 (momentane
  Beruehrungen), abgetastet 4-mal je Takt in den letzten 50 Takten.
  Diagnose: dieselbe Groesse ueber geometrische Nachbarn (Takt-gemittelter Abstand < 1 + eps) am Ende, auch nur ueber
  laufende Punkte.
- **Verschiebung:** MSD zwischen Takt-gemittelten Lagen der Takte 0 und 100 (Karte) sowie 100 und 200 (Plan).
- **Beruehrungsdreiecke:** Dreiercliquen der geometrischen Nachbarn (Takt-gemittelter Abstand < 1 + eps). Drehsinn chi
  aus Takt-gemittelten Phasen (2D: Ecken gegen den Uhrzeigersinn; 3D: Reihenfolge a, b, c mit Normale (b-a) x (c-a)),
  Windung w = Summe der gefalteten Phasenschritte / 2 pi (Wirbel; in 3D Durchstosspunkte von Wirbellinien),
  Drehsinn-Gebiete (2D: Dreiecke mit |chi| >= 0,5, verbunden ueber gemeinsame Kanten bei gleichem Vorzeichen).
- **Pumpen:** Drehung dpsi je Takt jedes Beruehrungsdreiecks zwischen Takt n und n + 1 (Procrustes-Winkel der
  schwerpunktbezogenen Ecken; 3D: Drehung um die Normale), gepaart mit chi im Takt n, gesammelt ueber Takte 50 bis Ende.
  Pearson-Korrelation r und Steigung dpsi gegen chi.
- **Eingefroren:** wie oben (W = 50).
- **C0 ([Z-A], Pruefung von K7):** einzelnes Dreieck mit Federn U = (1/2) sum (r - l_ij)^2, Phasen vorgegeben
  (Drehsinn +1, -1, 0), mu = mu(kappa_w) und 4-fach; Drehung je Takt (Schnappschuesse bei ganzen Takten, Takte 10-40)
  gegen (pi/2) eps^2 = 0,0157.

## 7. Urteilsregeln in Zahlen (vor jedem Hauptlauf festgelegt)

| AN | nach Plan | nach Kartenwortlaut |
|---|---|---|
| AN0 | (i) Paar: alle 8 Saaten (voll) mit pi - abs(Delta) <= 0,05 am Ende; (ii) Kette, Quadrat, Diamant: Median ueber Saaten der Gegentakt-Ordnung (voll) >= 0,95; (iii) Dreieck: Median ueber Saaten von Mittel abs(chi) (voll) >= 0,9; (iv) Paar: Median Rate_voll/(2K) in [0,9; 1,1]; jedes Gitter: Median t_halb(voll)/t_halb(gemittelt) in [0,9; 1,1]. Alle vier -> eingetroffen | wie Plan, aber (ii) in **jeder** Saat >= 0,95 und (iii) **jedes** Dreieck abs(chi) >= 0,9 in jeder Saat ("je Dreieck") |
| AN1 | Pyrochlor B1 am Ende (Takt 10 000), je Saat: Anteil abs(Summe)/4 < 0,1 >= 0,90 **und** P(1) >= 0,8 **und** Anteil 2+2 >= 0,80. Beide Saaten -> eingetroffen; keine -> verfehlt; eine -> unentschieden | dasselbe mit nematischer Ordnung S (global) statt P(1) |
| AN2 | R = kappa_50(Diamant)/kappa_50(Pyrochlor) aus dem Saatenmittel >= 1,5 -> eingetroffen; < 1,5 -> verfehlt; kappa_50 nicht bestimmbar -> nicht entscheidbar | dieselbe Regel |
| AN3 | Fuellgrad 0,84, schwach: momentane Kontakt-Korrelation <= -0,5 **und** MSD(100-200) >= max(2 x Kontrolle MSD(100-200); 0,01 PU^2) | Kontakt-Korrelation <= -0,5 **und** MSD(0-100) >= 2 x Kontrolle MSD(0-100) |
| AN4 | 2D, schwach: r >= 0,3 in mindestens 2 von 3 Fuellgraden oder r <= -0,3 in mindestens 2 von 3 -> eingetroffen | dieselbe Regel |

- Gruende fuer Plan-Abweichungen: AN0 Median statt jede Saat (eine Saat mit metastabiler Verdrillung ist Topologie,
  kein Fehler der Mittelung; Kartenwortlaut prueft streng). AN1 P(1) ist die Kollinearitaet der Quelle [S]; S ist die
  "nematische Ordnung" der Karte. AN3 Fenster 100-200 ohne Einschaltvorgang und Mindestbewegung 0,1 PU rms (K6).
- Ableitbarkeit: AN0 ist Kontrolle; in AN1 sind Zeigersumme und 2 + 2 Kontrollen (K5); AN2 liegt auf dem
  Koordinationswert (K4); in AN3 ist das Verhaeltnis zur Kontrolle Kontrolle (K6). Diese Teile werden im Ergebnis als
  Kontrolle gefuehrt, nicht als Befund.
- Keine Schwelle wird nach Befund geaendert. Abweichungen werden als Selbstanzeige gemeldet.

## 8. Was bildet sich von selbst (Zaehlung je Dimension, kein Urteil)

- 1D: Kette (Teil A). 2D: Quadrat, Dreieck (A), freie Packungen (C). 3D: Diamant (A, B), Pyrochlor (B), freie
  Packungen (C).
- Gezaehlt wie eine Life-Asche: Anteil Gegentakt-Paare (cos < -0,9) und Gleichtakt-Paare (cos > 0,9, auch nur
  laufende), Drehsinn-Dreiecke (abs(chi) >= 0,5 bzw. 0,9), Wirbel (Windung != 0), Drehsinn-Gebiete (Zahl, groesstes),
  eingefrorene Takte, Verschiebung gegen Kontrolle, Pumpkorrelation; Pyrochlor: 2 + 2, 3 + 1, 4 + 0, Kollinearitaet.

## 9. Laeufe (nur .69, kleintest.sh, Spuren cpu6 und cpu7, je Lauf <= 10 min, 1 Thread, 4 GB)

- Ordner .69: /home/fmh/fmhc-physics-remote/atem-netz-1/{rauch,lauf}. Logs mit absolutem Pfad.
- **Rauchlauf** (rauch/): teilA --rauch, teilC0, teilB2 --rauch (Pyrochlor, Diamant), teilB1 (300 Takte), teilB3 --rauch,
  teilC --rauch (2D 0,84; 3D 0,64). Nur Zeit, Speicher und Programmproben ansehen.
- **Einfrieren:** Kopien PLAN.md.eingefroren-<zeit>, code/*.py.eingefroren-<zeit>, Hashes in EINGEFROREN-SHA256.txt.
- **Hauptlaeufe** (lauf/), Reihenfolge nach Abschn. 10.
- auswertung.py liest lauf/*.json, schreibt auswertung.json und Bilder (PNG) nach lauf/; Kopie nach lauf-69/,
  Pruefsummen in lauf-69/PRUEFSUMMEN.txt.

## 10. Aenderungen nach den Rauchlaeufen (vor dem Einfrieren)

- **Rauchlauf 1** (rauch-69/, Code-Fassung atem.py vom 18:21, .69-Zeiten 16:21-16:29 UTC): alle zehn Laeufe rc = 0,
  <= 73 MB. Zeiten: B1 Pyrochlor 31 ms je Takt; B2 2,8 s je (kappa, Saat, 100 Takte); B3 270 us je Schritt;
  Teil C 2D 0,22 s je Takt (schwach), 2,05 s (stark); 3D 0,72 s (schwach), 6,9 s (stark); Teil A Diamant 8,9 s je
  Saat und 300 Takte. Programmproben: Paar-Rate voll 0,0628 = 2K (gemittelt 0,0628); C0 (K7): Drehung je Takt
  -0,01528 (mu x 1), -0,01568 (mu x 4) bei Drehsinn +1, Vorzeichen umgekehrt bei -1, 0 bei Gleichtakt; Vorhersage
  (pi/2) eps^2 = 0,01571 [E bestaetigt M, adiabatischer Grenzfall].
- **Selbstanzeige vorab:** Beim Rauchlauf habe ich die groben B2-Werte (6 kappa-Werte, 100 Takte, 1 Saat) angesehen:
  Pyrochlor eingefroren ab kappa = 0,039, Diamant ab 0,077 (bei 0,039 noch laufend). Das ist eine grobe Sicht auf die
  AN2-Groesse vor dem Einfrieren. Keine Schwelle und keine AN2-Regel wurde danach geaendert; die Regel stand vorher
  (Abschn. 5, 7). Die Rauch-Werte von AN1, AN3, AN4 habe ich nicht angesehen.
- **Aenderungen (nur Laufzeit und Messauflösung):**
  - B1: 10 000 statt 20 000 Takte (10-min-Grenze); Pyrochlor T = 0 entfaellt (B3 enthaelt T = 0).
  - B2: 200 statt 300 Takte, Saaten 1 und 2 in einem Lauf je Gitter, W = 50 unveraendert.
  - B3: bis 5e4/K mit dt = 0,1/K (statt 1e5/K, 0,05/K).
  - Teil C: 3D schwach und Kontrolle 200 Takte (Plan-MSD-Fenster in 3D dann 100-199, nur Diagnose); stark 2D 50,
    3D 15 Takte; Fenster fuer Pumpen und Einfrieren bei kurzen Laeufen ab einem Drittel (W = takte/3). AN3 und AN4
    (2D, schwach, 300 Takte) unberuehrt.
  - Teil A: Diamant in zwei Laeufe (Saaten 1-3, 4-6); gemittelte Dynamik 10 Abtastungen je Takt (wie die volle,
    damit beide Takt-Mittel dieselbe Lage im Takt haben); t_halb linear zwischen Takten interpoliert (vorher ganze
    Takte, bei t_halb ~ 10-20 Takten eine Stufung von 5-10 %, zu grob fuer die 10-%-Regel).
- **Rauchlauf 2** (rauch2/ auf der .69): dieselben Aenderungen, kurze Laeufe aller Hauptlauf-Arten und auswertung.py
  einmal durchlaufen lassen (nur Programmprobe: laeuft, schreibt Dateien).
- **Reihenfolge Hauptlaeufe:** cpu6: A1 (Paar, Kette, Quadrat), A2 (Dreieck), A3 (Diamant 1-3), A4 (Diamant 4-6),
  B2 Diamant, C 2D 0,84, C 2D 0,80, C 2D 0,88, C0, B3. cpu7: B1 Pyrochlor 1, B2 Pyrochlor, B1 Pyrochlor 2,
  B1 Diamant, C 3D 0,64, C 3D 0,60, C 3D 0,68. Danach auswertung.py (cpu6).
- Rauchlauf 2 (16:33-16:35 UTC): alle Laeufe rc = 0. auswertung.py brach an den kurzen Rauch-Dateien ab (fehlendes
  MSD-Fenster); geaendert: fehlende Werte geben "nicht entscheidbar" statt eines Abbruchs. Danach rc = 0. Ausgaben der
  Programmprobe nicht als Ergebnis gelesen. Eingefroren werden atem.py und auswertung.py in dieser Fassung
  (atem_rauch1.py = Fassung des Rauchlaufs 1, nur zur Nachvollziehbarkeit).
