# GUERTEL-FELD-STAB-2: Plan (Runde 43, Fast Lane, Robustheit)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 19:24:34 CEST (date). Plantext ab 19:33:14 CEST
  (date), vor Code, Rauchlauf und jedem Hauptlauf. Zeitbox 90 min, also bis 20:54:34 CEST.
- Karte: KARTE.md (Teile A bis C, GT0 bis GT2, Bedeutung). Daran aendert dieser Plan nichts. Festlegungen [F] machen
  die Karte rechenbar; Zusaetze sind als **Zusatz** markiert und nicht urteilsbildend. Eine Lesart, die vom
  naheliegenden Wortlaut abweichen koennte (Teil B, "Schritte von 30 Grad"), ist als **Lesart** markiert und begruendet.
- Kennzeichen: [M] Mathematik; [E] Rechnung im Modell; [L] Literatur oder Gedaechtnis; [H] Hypothese; [F] Festlegung
  dieses Plans; [R] im Rauchlauf gesehen. Alles ist eine synthetische Modellrechnung, keine Messdatenbestaetigung.
- Vorarbeit (nur gelesen, Code kopiert): GUERTEL-FELD-STAB-1 (GFS-1) und GUERTEL-2 (mit Nachtrag N1).

## 0. Ableitbarkeit, Schreibtischrechnung und Dimensionen (vorab)

1. **Kontinuum [M]** (aus GFS-1 uebernommen): Der Vorwaertsast ist fuer theta > 360 Grad ein Sattel (konjugierter
   Punkt; kleinster Jacobi-Eigenwert (180/(theta/2))^2 - 1, bei 450 Grad -0,36). Endpunkt ohne Sprung:
   E(720 - theta), auf dem Gitter exakt wegen der Symmetrie q -> q quer. Gilt radial fuer d = 1, 2, 3.
2. **Schreibtischrechnung Bindungswinkel [M, grob]:**
   - Harmonisches Profil in 3D mit R = 2 r0: h(r) = 2 r0/r - 1. Die radiale Kernbindung (r0 -> r0 + 1) dreht um
     theta * 2/(r0 + 1): (8, 16) 0,222 theta; (12, 24) 0,154 theta; (16, 32) 0,118 theta. Zum Vergleich (6, 24):
     0,190 theta.
   - Gemessen auf (12, 24) bei 450 Grad (GFS-1, Sonde 0,489): 2,12 rad gegen ideal 1,21 rad, Faktor 1,75 (Ecken der
     Wuerfelkugel und Nichtlinearitaet).
   - Grobe Folgerung [H]: Die Sprunggrenze skaliert etwa mit r0 + 1. Aus 540 Grad auf (12, 24) folgen etwa 375 Grad
     auf (8, 16) und etwa 705 Grad auf (16, 32). Auf (6, 24) sprang der Ast bei 450 Grad; (8, 16) hat einen um 17 %
     steileren Kern.
   - **Folge fuer die Vertraege:** GT1 kann schon am Startzustand scheitern, wenn der Vorwaertsast auf (8, 16) vor oder
     bei 450 Grad springt; das ist nach dieser Abschaetzung wahrscheinlich, aber nicht sicher (Eckenfaktor und
     Rauschen sind gitterabhaengig). GT1 kann auch bestehen. GT2 ist grob ableitbar (Monotonie in r0 + 1); nicht
     ableitbar sind die Werte, die Ecken-Effekte und ob auf (16, 32) der Zerfall (glattes Umlegen) vor dem Sprung kommt.
     theta_max(12, 24) = 540 Grad ist aus N1 bekannt (gleicher Code, gleiche Saat); neu sind (8, 16) und (16, 32).
3. **Nicht ableitbar [E, Gegenstand der Rechnung]:** ob die Stoesse auf (8, 16) und (16, 32) ohne Sprung in die
   umgekehrte Verdrillung fuehren; die Sprunggrenzen auf (8, 16) und (16, 32).
4. **Dimensionen (AGENTS.md):**
   - **Innere Symmetrie:** SO(3) (Teile A und B) und SO(2) (Teil C) werden getrennt gerechnet und getrennt
     ausgewiesen. Fuer SO(2) gibt es keine Kipprichtung und keine Entdrillung: pi_1(SO(2)) = Z [M]. Teil C ist deshalb
     nur Werkzeugprobe (Karte).
   - **Raum:** SO(3) nur auf dem Z^3-Kugelgitter; SO(2) auf dem Z^2-Scheibengitter (wie GUERTEL-2, "Ebene"). Die
     Kontinuumsaussage in Punkt 1 gilt radial fuer d = 1, 2, 3 [M]; die Gitterwinkel skalieren je Dimension anders
     (3D etwa theta/(r0 (1 - r0/R)), 2D theta/(r0 ln(R/r0))). Gitterergebnisse werden nicht zwischen Dimensionen
     uebertragen. Ein radialer 3D-Lauf ist kein 1D-Modell und kein voller 3D-Stabilitaetsnachweis; der Stoss prueft
     eine Richtung.

## 1. Gitter und Drehprotokoll (Teile A und B) [F]

- Gitter (dim 3, SO(3)): (r0, R) = (8, 16), (12, 24), (16, 32). Platzliste, Energie, Sonde, FIRE wie g2.Feld und
  g2.fire_feld (guertel2.py, Kopie, unveraendert).
- **Protokoll** je Gitter: wortgleich wie GFS-1 (= g2.feld_protokoll): 10-Grad-Schritte (Praediktor, setze, Rauschen
  1e-3, FIRE 30), Gitterwinkel alle 90 Grad mit FIRE 150, ftol 1e-5, dtmax 0,1; Saat
  default_rng([42, 3, round(10 r0), round(R)]) wie g2.modus_feld. tmax = 720 Grad.
- (16, 32) laeuft wegen der 10-min-Grenze in zwei Abschnitten: 0 -> 450 Grad und 450 -> 720 Grad. Am Ende des ersten
  Abschnitts werden Feld und Zustand des Zufallsgenerators gespeichert; der zweite setzt bei 460 Grad fort. Die
  Arithmetik ist dieselbe wie in einem durchgehenden Lauf (FIRE startet je Winkel neu). Rauchlauf-Probe dazu: Abschnitte
  0 -> 10 und 10 -> 20 gegen 0 -> 20 auf (8, 16), bitgleich verlangt.
- Gespeicherte Zustaende (nach allen Relaxationen des Winkels): 270, 300, 420, 450.
- **Je Winkel aufgezeichnet (Zusatz zur Kopie, aendert nichts an x):** E und Sonde wie GFS-1 (Schritt und Gitter),
  dazu die Sonde im Lauf (Minimum ueber alle FIRE-Schritte des Winkels), das mittlere q_z der aeusseren Haelfte
  (h < 1/2) und die Kipp-Amplitude P.

## 2. Teil A: Stoss [F]

- Wie GFS-1 (Funktion kipp, Kopie): innere Haelfte h >= 1/2, f_i = clip(2h - 1, 0, 1), Kippprofil
  delta = eps sin(pi f_i), Achse um delta von z nach x gekippt (q -> q_s q_y(delta) q_s^-1 q q_y(-delta),
  q_s = q_z(theta/2)), Kern, Rand und aeussere Haelfte bleiben. Danach FIRE hoechstens 3000 Schritte, ftol 1e-5,
  dtmax 0,1, mit Aufzeichnung je Schritt (E, Sonde, fmax, P).
- **Laeufe bei 450 Grad, eps = 0,01, 0,1, 0,3:** auf (8, 16) und (16, 32) (GT1) und auf (12, 24) (GT0, Reproduktion).
- **Referenzlaeufe (urteilsbildend):** FIRE 3000 ab dem Protokollzustand bei 270 Grad, je Gitter, ohne Stoss. Ihr
  Endwert ist E_ref = E(270) = E(720 - 450) in GT1 und GT0. Gueltig nur, wenn Sonde im Lauf > 0, mittleres q_z aussen
  am Ende > 0 (Vorwaertsdrehsinn) und fmax am Ende <= 1e-5 (konvergiert).
- **Zusatz (beschreibend, nur wenn die Zeit reicht):** auf (16, 32) bei 420 Grad eps = 0,01, 0,1, 0,3 mit Referenz
  ab dem Zustand bei 300 Grad.
- Ist der Protokollzustand bei 450 Grad schon gesprungen (Sonde <= 0 vor dem Stoss), werden die Stoesse trotzdem
  gerechnet; sie sind dann "sprung", weil die Sonde im Lauf den Startzustand einschliesst.

## 3. Teil B: Sprunggrenze theta_max [F, Lesart]

- **Lesart "Schritte von 30 Grad":** theta_max wird auf dem 30-Grad-Raster abgelesen; die Drehung selbst laeuft mit
  dem 10-Grad-Protokoll aus Abschnitt 1. Begruendung: (1) Teil A und die GT0-Reproduktion brauchen genau dieses
  Protokoll, ein Lauf je Gitter traegt also A, B und GT0; (2) die Vergleichswerte der Karte (270, 450, 540 Grad aus
  GUERTEL-2 und N1) stammen aus demselben 10-Grad-Protokoll; ein 30-Grad-Protokoll wuerde den Ast anders fuehren
  (groessere Praediktorschritte, weniger FIRE je Grad) und waere mit ihnen nicht vergleichbar. Der 10-Grad-Wert wird
  beschreibend mit angegeben.
- **Definitionen** je Gitter (Protokoll 0 bis 720 Grad, ungestossen):
  - theta_J (Plan): erster Protokollwinkel, an dem die Sonde im Lauf (Minimum ueber alle FIRE-Schritte dieses Winkels,
    einschliesslich des Startzustands nach Praediktor und Rauschen) <= 0 ist.
  - theta_J (Wortlaut): erster Protokollwinkel, an dem die Sonde eines Protokollzustands (nach FIRE 30 bzw. nach
    FIRE 150 am Gitterwinkel) <= 0 ist; so sind die GUERTEL-2-Werte bestimmt.
  - theta_U: erster Protokollwinkel vor theta_J, an dem das mittlere q_z aussen < 0 ist (glatt umgelegt, ohne Sprung).
  - **theta_max** = theta_J auf das 30-Grad-Raster aufgerundet (erstes Vielfaches von 30 Grad, bei dem der Sprung
    erfolgt ist), wenn kein theta_U davor liegt.
  - Liegt theta_U vor theta_J (oder gibt es nur theta_U): Der Ast legt sich glatt um, statt zu springen;
    theta_max = "kein Sprung" (zaehlt als groesser als jeder endliche Wert).
  - Weder theta_J noch theta_U bis 720 Grad: theta_max = "> 720" (untere Schranke).

## 4. Teil C: SO(2)-Kontrolle [F]

- SO(2)-Feld auf dem Z^2-Scheibengitter (r0, R) = (12, 24) (g2.Feld dim 2: Winkelfeld phi, Energie
  Summe 2(1 - cos(phi_a - phi_b)), h = ln(R/r)/ln(R/r0)). Protokoll wie Abschnitt 1 (10 Grad, FIRE 30/150, Rauschen
  1e-3, Saat default_rng([42, 2, 120, 24])) bis 450 Grad.
- **Stoss:** Eine Kipprichtung gibt es in SO(2) nicht [M]. Gestossen wird deshalb mit demselben Sinusprofil in der
  einzigen Richtung: phi -> phi + eps sin(pi f_i) auf der inneren Haelfte, eps = 0,01, 0,1, 0,3. Danach FIRE 3000.
- **Sonde:** max |phi_a - phi_b| im Lauf; >= pi heisst Gittersprung (Phasensprung), wie GUERTEL-2.
- **SO(2)-Referenz (nach dem Rauchlauf ergaenzt, vor dem Einfrieren; urteilsbildend fuer GT0 nach Plan):** FIRE 3000
  ab dem SO(2)-Protokollzustand bei 450 Grad ohne Stoss (eps = 0). Ihr Endwert ist E_Ast,ref, der auskonvergierte Ast.
  Gueltig nur mit Sonde im Lauf < pi und fmax am Ende <= 1e-5.

## 5. Urteilsregeln [F] (mechanisch in code/auswertung.py)

**Referenzwerte, die in die Urteile eingehen (ausdruecklich Teil des Urteils):**
- E_ref(270) je Gitter aus den Referenzlaeufen (Abschnitt 2), mit ihren Gueltigkeitsbedingungen.
- GFS-1-Werte fuer GT0, mechanisch aus Kopien der GFS-1-Laufdateien gelesen (eingaben-gfs1/, sha256 in
  EINGEFROREN-SHA256.txt): prot.json (E_schritt(450), E_gitter(450)), stoss-T450-e{0.01, 0.1, 0.3}.json (E_end),
  stoss-T270-e0.json (E_end, Referenz).
- E_Ast := E des Protokollzustands bei theta vor dem Stoss (je Lauf).

**Klassen je SO(3)-Stoss** (rho := (E_end - E_ref)/(E_Ast - E_ref); P_0, P_end: Kipp-Amplitude nach dem Stoss und am
Ende; Sonde im Lauf schliesst Start- und Stosszustand ein):

| Klasse | nach Plan | nach Kartenwortlaut |
|---|---|---|
| sprung | Sonde im Lauf <= 0 | gleich |
| umgekehrt | kein Sprung, abs(E_end - E_ref) <= 1e-6 E_ref, q_z aussen vor dem Stoss > 0 und am Ende < 0, Referenz gueltig | kein Sprung und abs(E_end - E_ref) <= 1e-6 E_ref ("E auf E(270) auf 1e-6 relativ") |
| ast | kein Sprung, rho >= 0,90 und P_end <= P_0 | nicht umgekehrt (sonst) |
| dazwischen | sonst | - |

**Klassen je SO(2)-Stoss** (Bezug nach Plan: E_Ast,ref aus der SO(2)-Referenz, Abschnitt 4; ist sie ungueltig oder
fehlt sie, ist die Plan-Klasse offen und GT0 nach Plan nicht auswertbar. Bezug nach Wortlaut: E_Ast = Protokollzustand
vor dem Stoss):

| Klasse | nach Plan | nach Kartenwortlaut |
|---|---|---|
| sprung | max abs(phi_a - phi_b) im Lauf >= pi | gleich |
| ast | kein Sprung und abs(E_end - E_Ast,ref) <= 1e-3 E_Ast,ref | kein Sprung und abs(E_end - E_Ast) <= 0,10 E_Ast ("E bleibt auf dem Ast") |
| entdrillt | kein Sprung und E_end < E_Ast,ref - 1e-3 E_Ast,ref | kein Sprung und E_end < 0,90 E_Ast |
| dazwischen | sonst | sonst |

**Urteile:**

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| GT0 | eingetroffen, wenn (a) alle drei SO(2)-Stoesse "ast" oder "sprung" sind und (b) auf (12, 24): E_schritt(450) und E_gitter(450) auf 1e-6 relativ gleich GFS-1, Sonde des 450-Zustands > 0, die drei E_end(450, eps) auf 1e-6 relativ gleich GFS-1 und alle drei "umgekehrt" (Plan-Klasse), E_ref(270) auf 1e-6 gleich der GFS-1-Referenz | eingetroffen, wenn (a) wie links mit Wortlaut-Band und (b) E_gitter(450) (der gestossene Zustand) und die drei E_end(450, eps) auf 1e-6 relativ gleich GFS-1 |
| GT1 | eingetroffen: alle sechs Laeufe ((8, 16) und (16, 32), je eps 0,01, 0,1, 0,3 bei 450 Grad) "umgekehrt"; nicht eingetroffen: mindestens ein Lauf in einer anderen Klasse; nicht auswertbar: sonst (Datei fehlt oder Referenz ungueltig) | dasselbe mit den Wortlaut-Klassen |
| GT2 | eingetroffen: theta_max(8, 16) < theta_max(12, 24) < theta_max(16, 32) streng (theta_J nach Plan); nicht eingetroffen: Ordnung verletzt (gleich oder umgekehrt); nicht entschieden: Vergleich nur zwischen zwei unteren Schranken; nicht auswertbar: Protokoll fehlt oder bricht ab | dasselbe mit theta_J nach Wortlaut |

- GT0 ist eine Kontrolle; ein "nicht eingetroffen" dort heisst Werkzeugfehler oder Umgebungsunterschied, und GT1/GT2
  werden dann nur unter Vorbehalt gelesen.
- **Beschreibend (nicht urteilsbildend):** theta_J auf 10 Grad; Sonde und E je Winkel; erster Sprungschritt, P_max,
  "halb" (erster Schritt mit E < (E_Ast + E_ref)/2) je Stoss; Zusatzlaeufe bei 420 Grad (mit Referenz 300, gleiche
  Klassen); Bilder energie-verlauf.png (E, Sonde, P ueber die FIRE-Schritte je Gitter bei 450 Grad und SO(2)) und
  sprunggrenze.png (Sonde und E ueber theta je Gitter).

## 6. Laufplan [F]

- Nur .69, ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu3 und cpu5. Je Lauf <= 10 min
  (RuntimeMaxSec 600), 1 Thread, Logs mit absolutem Pfad. Ordner /home/fmh/fmhc-physics-remote/guertel-feld-stab-2/
  (code/, rauch/, lauf/, eingaben-gfs1/).
- **Rauchlauf** (Spur cpu3): Laufzeit je Gitter mit Protokoll bis 20 Grad (8, 12 und 16 sowie SO(2)); Abschnittsprobe
  auf (8, 16) (0 -> 10 -> 20 gegen 0 -> 20); Stoss bei 20 Grad auf (16, 32) (eps 0,3, 100 Schritte) und SO(2)
  (eps 0,3, 100 Schritte); Auswertung im Rauchmodus. Kein Wert bei 270 bis 720 Grad wird dabei erzeugt oder angesehen.
- **Hauptlaeufe** (eingefrorener Code, je genau einmal):
  - cpu3: Protokoll (16, 32) 0 -> 450; Stoesse (16, 32) bei 450 Grad (eps 0,01, 0,1, 0,3); Referenz (16, 32) 270;
    danach Zusatz (16, 32): Referenz 300, Stoesse bei 420 Grad.
  - cpu5: Protokoll (8, 16) 0 -> 720; Protokoll (12, 24) 0 -> 720; SO(2)-Protokoll bis 450, SO(2)-Referenz (eps 0)
    und drei SO(2)-Stoesse; Stoesse und Referenz (8, 16); Stoesse und Referenz (12, 24); wartet auf den ersten
    (16, 32)-Abschnitt, dann Protokoll (16, 32) 450 -> 720.
  - Skripte: skripte/kette-K3.sh und skripte/kette-K5.sh (eingefroren mit dem Code).
  - Danach die Auswertung (cpu5), wenn beide Ketten fertig sind.
- Bricht ein Lauf ab (Zeit, Absturz), wird er mit Grund als Nachtrag wiederholt; die Werte des abgebrochenen Laufs sehe
  ich nicht an. Reicht die Zeit nicht, entfaellt zuerst der Zusatz bei 420 Grad.

## 7. Rauchlauf und Festlegungen vor dem Einfrieren [R]

- Code geschrieben nach dem Plantext (ab 19:33:14) zwischen den date-Messungen 19:35:49 und 19:39:48 CEST. Text
  dieses Abschnitts ab 19:43:14 CEST (date).
- **Rauchlauf 1:** 17:39:51 bis 17:40:37 UTC, Spur cpu3, zehn Units (skripte/kette-rauch.sh), alle rc = 0.
- **Rauchlauf 2:** 17:42:27 bis 17:42:31 UTC, zwei Units (skripte/kette-rauch2.sh: SO(2)-Referenz bei 20 Grad und die
  geaenderte Auswertung), beide rc = 0.
- **Laufzeit je FIRE-Schritt** (Protokoll bis 20 Grad, 60 Schritte): (8, 16) 1,2 s, also etwa 20 ms; (12, 24) 3,6 s,
  60 ms; (16, 32) 8,4 s, 140 ms. Stoss (16, 32) mit Aufzeichnung: 100 Schritte 13,3 s, 133 ms. SO(2): unter 0,1 s.
  - Erwartet: Protokoll (16, 32) 0 -> 450 (etwa 2100 Schritte) etwa 5 min, 450 -> 720 (1260) etwa 3 min;
    Protokoll (12, 24) 0 -> 720 (3360) etwa 3,4 min; (8, 16) etwa 1,1 min; Stoss (16, 32) schlimmstenfalls 3000
    Schritte, also 6,7 min. Alles unter 10 min; der Zusatz bei 420 Grad passt in die Zeitbox.
- **Proben bestanden:** Abschnittsprobe (8, 16): 0 -> 10 -> 20 gleich 0 -> 20, E(20) = 22,1084104648263 in beiden,
  Sonde gleich (bitgleich). (12, 24) bei 20 Grad: E_schritt bitgleich mit GFS-1 (Abweichung 0,0).
- **Gesehen:** nur Laufzeiten, Codepfade und Werte bei 10 und 20 Grad; die Bilder haben den erwarteten Aufbau.
- **Aenderung nach dem Rauchlauf (vor dem Einfrieren):** Bei 20 Grad lag die SO(2)-Relaxation ohne Sprung 0,67 % unter
  dem Protokollzustand (E 1,0284 gegen 1,0354): Der Protokollzustand ist nicht auskonvergiert (die SO(2)-Referenz
  eps = 0 endet nach 137 Schritten bei 1,02784). Mit dem Protokollzustand als Bezug haette die Plan-Klasse
  faelschlich "entdrillt" ergeben. Deshalb bezieht sich die SO(2)-Klasse nach Plan jetzt auf die SO(2)-Referenz
  (Abschnitt 4, neue Zeile; Abschnitt 5, Tabelle; Abschnitt 6, ein Lauf mehr). Die Wortlaut-Klasse behaelt den
  Protokollzustand mit dem 10-%-Band. Das ist eine Korrektur des Kontrollbezugs, keine Aenderung an GT1 oder GT2.
- Sonst keine Aenderung an Code oder Plan nach dem Rauchlauf; die Beschriftung der Bilder nennt jetzt die
  eingestellten Winkel statt fester Zahlen.
