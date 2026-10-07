# DIM-BEUTEL-2 Plan (Code-Agent, Runde 17)

- Geschrieben ab 2026-10-02 11:03:28 CEST (date), vor jedem .69-Aufruf, jeder Syntaxpruefung und jedem Rauchtest.
- Zeitbox: Start 10:50:22 CEST, Ende spaetestens 12:20 CEST. Laeufe enden spaetestens 12:02.
- Verbindlich und unveraendert: KARTE.md (F1, F2, Verfahren, Kontrollen, E1 bis E4, Bedeutung).
- Gelesen: RUNDE-16/dim-beutel/ KARTE, PLAN, Nachtraege 1 bis 4, ERGEBNIS, code/dimbeutel2.py, aus/frisch (Z3, Z4).
- Code: code/dimbeutel3.py (aus dimbeutel2.py uebernommen und erweitert), Auswertung code/auswertung2.py.

## 1. Schreibtisch des Code-Agenten

- Funktional, Gradient, Identitaet E = omega Q + E_chi und p_loc = omega Q/E unveraendert aus DIM-BEUTEL.
- **Vicsek-Graph (Standardfassung: Plus-/Kreuzfassung):**
  - Zelle (x, y) in [0, 3^g)^2 bleibt, wenn an jeder Ternaerstelle x_d = 1 oder y_d = 1 gilt (Mitte und vier
    Kreuzarme). Knoten = Zellen, Kanten = Naechstnachbarn (4er-Nachbarschaft).
  - Begruendung: Nur die Plusfassung ist mit Naechstnachbarkanten des Quadratgitters zusammenhaengend; die
    X-Fassung (Ecken) braeuchte Diagonalkanten. Beide sind als Graph derselbe Baum (Mittelkopie an vier
    Aussenkopien ueber je eine Spitze gebunden).
  - Pruefungen im Code: 5^g Knoten, 5^g - 1 Kanten (Baum), zusammenhaengend.
  - Mittelpunkt c = ((3^g - 1)/2, (3^g - 1)/2), die Mitte hoechster Generation. Bis Graphabstand (3^g - 1)/2 sieht
    seine Umgebung exakt wie das unendliche Fraktal aus; das ist R_self.
  - Die Hauptarme sind gerade Gitterlinien. Der Graphabstand ist daher der Abstand entlang der Arme (d_min = 1).
- **Periode in Q fuer Vicsek:**
  - Laenge x 3 gibt Knoten x 5. Der Widerstand waechst auf dem Baum wie die Laenge (x 3), also kleine
    Laplace-Eigenwerte x 1/15 und omega x 1/sqrt(15). Daraus folgt d_w = ln15/ln3 und d_s = 2 d_H/d_w = 2 ln5/ln15
    = 1,18863 [L?, hier hergeleitet].
  - Ist ein Beutel bei Q optimal, ist der dreimal so grosse bei Q' = 5 sqrt(15) Q = 19,365 Q optimal, mit E' = 5 E
    (Wand und Gitter vernachlaessigt). Daraus folgt p = ln5/ln(5 sqrt15) = 0,54310 = d_s/(d_s + 1).
  - Periode P_V = 5 sqrt(15) = 19,3649; Sierpinski wie DIM-BEUTEL P_S = 3 sqrt(5) = 6,7082.
  - Sollwerte: Vicsek p_s = 0,54310, p_H = 0,59432, Mitte 0,56871. Sierpinski p_s = 0,57720, p_H = 0,61315,
    Mitte 0,59518.
- **Startradius Vicsek (Schreibtisch):**
  - Die Gen-1-Kopie (5 Knoten) mit Dirichlet-Rand hat lambda_1 = 3 - sqrt5 = 0,764. Angenommen wird
    lambda_1(m) ~ 0,764 x 15^-(m-1).
  - Das Optimum Q omega = d_s B V mit B = 1/4 gibt Q(m) ~ 0,0878 x 19,365^m. Der Radius der Gen-m-Kopie
    (3^m - 1)/2 ist dann etwa 1,2 Q^0,3707.
  - Startradius A fuer Vicsek: R0 = 1,2 Q^(ln3/ln P_V) = 1,2 Q^0,3707.
  - Erwarteter Beutelradius: etwa 8 bei k = 21 und etwa 290 bei k = 60 (k siehe 2).
- **Wand:** Beide Fraktale sind endlich verzweigt. Ein Beutel aus ganzen Teilkopien hat O(1) Wandstellen
  (Sierpinski 2 bis 4, Vicsek 4). Die Wandenergie ist dann ein fester Versatz c, der die Sekante um etwa
  -c/(E ln P) verschiebt; das wird mit wachsendem E kleiner.

## 2. Graphen, Ladungsstufen, Startformen

- Q-Gitter: Q_k = P^(k/12), also 12 Indexschritte je Periode, fuer beide Fraktale. Bei Sierpinski sind das dieselben
  Q_k wie in DIM-BEUTEL.

| Lauf | Graph | Stufen k | je Periode | Formen | Gebiet | +-Fortsetzung |
|---|---|---|---|---|---|---|
| F1 Haupt | Sierpinski g = 10, Mitte s1 = (256, 256) | 34, 36, ..., 78 (23) | 6 | A, Bm, Bp | Teilgebiet | ja |
| F1 Kontrolle | Sierpinski g = 9, s1 = (128, 128) | 34, 38, ..., 78 (12) | 3 | A | voller Graph | nein |
| F2 Haupt | Vicsek g = 8 (390625 Knoten), Mitte c | 15, 18, ..., 63 (17) | 4 | A, Bm, Bp | Teilgebiet | ja |
| F2 Kontrolle | Vicsek g = 7 (78125 Knoten), Mitte c | 15, 21, ..., 63 (9) | 2 | A | voller Graph | nein |

- Warum g = 8 fuer Vicsek: Der Beutel braucht drei Perioden (Laenge x 27) von Radius etwa 8 an, also bis etwa 220
  bis 300. Bei g = 8 ist R_self = 3280, bei der Kontrolle g = 7 ist R_self = 1093. Laengere Rechnungen begrenzt der
  Loeser (kleine Eigenwerte grosser Beutel), nicht die Graphgroesse.
- **Startform A:** Kugel im Graphabstand R0 um den Mittelpunkt; innen chi = 0 und phi ~ 1 - (r/R0)^2, aussen
  chi = 1 und phi = 0.
  - Die Amplitude kommt aus dem Rayleigh-Quotienten (Minimum entlang der Amplitude), sonst wie DIM-BEUTEL.
  - R0: Sierpinski Q^0,4 (genau Z3 aus DIM-BEUTEL), Vicsek 1,2 Q^0,3707.
- **Startform B: andere Anfangsradien.** Bm mit R0/f, Bp mit R0 x f. Dabei ist f = sqrt2 (Sierpinski) bzw. sqrt3
  (Vicsek), also eine halbe Periode in der Laenge nach unten und oben.
  - Begruendung gegen einen zweiten Mittelpunkt: Alle Mittelpunkte hoher Generation haben bis zu ihrem
    Selbstaehnlichkeitsradius dieselbe Umgebung (Sierpinski: zwei an einer Ecke verklebte Dreiecke; Vicsek: eine
    volle Kopie). Sie liefern daher dieselben Energien und pruefen nichts.
  - Unterschiedliche Radien treffen dagegen verschiedene Nebentaeler. In DIM-BEUTEL lag der Beutelradius nach der
    Minimierung nahe am Startradius.
- **Je Stufe gilt die tiefste Energie unter den konvergierten Formen A, Bm, Bp.** Ist keine konvergiert, ist die Stufe
  ungueltig.
- **Teilgebiet (numerisch, kein Modellwechsel):**
  - Minimiert wird ueber die Knoten mit Graphabstand <= Rcut vom Mittelpunkt; alle Knoten ausserhalb bleiben fest im
    Vakuum (phi = 0, chi = 1). Rcut = 1,4 x R0(Bp) + 25.
  - Das ist dasselbe Funktional wie auf dem ganzen Graphen mit festgehaltenem Vakuum aussen. Die Felder fallen
    ausserhalb des Beutels je Knoten um etwa 2 - sqrt3 = 0,27 ab.
  - Pruefung je Loesung: Auf der Randlage (Abstand >= Rcut - 4) muessen phi/max <= 1e-10 und |1 - chi| <= 1e-10
    sein. Sonst wird Rcut = 1,5 Rcut + 10 gesetzt und von der Loesung aus weitergerechnet (hoechstens 3-mal).
  - Unabhaengige Pruefung: Die Kontrollen der kleineren Generation laufen auf dem vollen Graphen.

## 3. Messung je Stufe

- Je Form gespeichert: E, omega, p_loc, h, Identitaetsrest, skalierter und unskalierter Gradient, Iterationen,
  chi_min, V_bag = #(chi < 1/2), R_bag = groesster Graphabstand eines Beutelknotens, Wandkanten, Randwerte, Rcut,
  Knotenzahl des Teilgebiets und Laufzeit.
- Je Stufe: die beste Form. Von ihr aus folgt die Fortsetzung nach Q e^(+-0,01), warm gestartet auf demselben
  Teilgebiet.
  - Daraus p_fd = ln(E+/E-)/0,02 und (dE/dQ)/omega - 1.
  - Profil der besten Form: phi, chi, Graphabstand und Lage aller Knoten mit Abstand <= 1,5 R_bag + 15.
- **d_s des Vicsek-Graphen direkt** (Lauf ds, vor den Hauptlaeufen):
  - (a) Zaehlfunktion N(lambda) der Eigenwerte von L = D - A unter lambda, exakt per Traegheitssatz. Auf dem Baum
    laeuft die Gauss-Elimination von den Blaettern zur Wurzel ohne Auffuellung; N ist die Zahl negativer Pivots.
    - Gerechnet fuer g = 5, 7, 8 auf lambda = 8 x 15^(-i/8), i = 0 bis 64.
    - Kontrolle bei g = 5 gegen dichte Eigenwerte.
    - Sekante je Spektralperiode: d_s/2 = ln(N(lambda)/N(lambda/15))/ln15.
  - (b) Rueckkehrwahrscheinlichkeit der traegen Irrfahrt vom Mittelpunkt, g = 7, bis t = 15^4 = 50625.
    - Daraus Sekanten -ln(P(15 t)/P(t))/ln15 und ein Fit der Steigung ueber t = 225 bis 50625.
  - **Gewerteter Direktwert d_s,V:** 2 x Mittel der Sekanten aus (a) bei g = 8 im Skalenbereich, also
    N(lambda/15) >= 5 und N(lambda) <= n/25. (b) und g = 7 sind Kontrollen.
  - Weicht d_s,V um mehr als 0,03 von 1,18863 ab, gilt laut Karte p_s,V = d_s,V/(d_s,V + 1) als Soll fuer E3 und E4.
- Sierpinski: d_s = 1,3652 aus DIM-BEUTEL (direkt gemessen), nicht neu gerechnet.

## 4. Wertung (vor dem Lauf festgelegt)

- **Gueltige Stufe (Hauptlauf):**
  - die beste Form konvergiert, d. h. skalierter projizierter Gradient <= 100 x gtol und Identitaetsrest <= 1e-6
    (wie DIM-BEUTEL Nachtrag 1, N2);
  - chi_min < 0,1;
  - Randwerte phi/max <= 1e-6 und |1 - chi| <= 1e-6;
  - **Beutelbereich:** 8 <= R_bag <= R_self/2 (Zellgroesse 1; F1: R_self = H = 256, F2: R_self = 3280).
- **Beutelbereich eines Laufs:** die laengste zusammenhaengende Folge gueltiger Stufen der Stufenliste.
- **p_per(k)** = ln(E(Q_k+12)/E(Q_k))/ln P fuer jedes k, bei dem k und k + 12 im Beutelbereich liegen.
  - **Gewertet:** Mittel p_per ueber alle diese k (alle Phasen der Periode gleich gewichtet).
  - **Fehlerband:** +- Standardabweichung dieser p_per(k). Berichtet werden zusaetzlich Min/Max und die
    nicht ueberlappenden Perioden ab dem ersten k.
  - Volle Perioden = (k_letzt - k_erst)/12 des Beutelbereichs. **Unter 3 vollen Perioden ist die betreffende
    Vorhersage "offen"**; die Zahlen werden trotzdem berichtet.
- **E1:** eingetroffen, wenn |p_per(F1) - 0,577| <= 0,015.
- **E2:** eingetroffen, wenn |d_s,V - 1,19| <= 0,03.
- **E3:** eingetroffen, wenn p_per(F2) < (p_s,V + 0,59432)/2, also naeher an p_s,V als an p_H.
- **E4:** eingetroffen, wenn |p_per(F1) - 0,57720| <= 0,02 UND |p_per(F2) - p_s,V| <= 0,02.
- **Kontrollen:**
  - **dE/dQ = omega:** |p_fd - p_loc| je gueltiger Stufe, dazu Median und Hoechstwert. Bestanden, wenn an jeder
    gueltigen Stufe |p_fd - p_loc| <= 2e-3 gilt und beide +-Loesungen konvergiert sind. Aendert eine
    +-Loesung V_bag, wird das gemeldet.
  - **Zwei Generationen:** |E_Kontrolle(k)/E_Haupt,A(k) - 1| an den gemeinsamen Stufen, beide gueltig.
    Bestanden, wenn <= 1e-6. Der Vergleich prueft Graphgroesse und Teilgebiet zugleich.
  - **Zwei Startformen:** E_A, E_Bm, E_Bp je Stufe; wie oft welche Form gewinnt; groesste relative Differenz.
    - p_per nur aus A (wo A gueltig ist) gegen p_per aus dem Minimum.
    - Robust, wenn |p_per(A) - p_per(min)| <= 0,01.
  - **Beutelradius gegen Zelle und Graph:** R_bag, R_bag/1 und R_bag/R_self je Stufe.
- Zusatz ohne Wertung: p_loc schwankt log-periodisch; berichtet wird die Spanne von p_loc im Beutelbereich.

## 5. Rechnen

- Code per rsync nach /home/fmh/fmhc-physics-remote/runde17-dim-beutel-2/. Aufrufe nur ueber kleintest.sh, Spuren
  cpu und cpu2, je Aufruf <= 600 s.
  - Das Skript beendet sich vor 540 s, schreibt jede Form und jede Stufe sofort (stufen-<tag>.jsonl).
  - Ein weiterer Aufruf ueberspringt fertige Stufen und rechnet unvollstaendige neu.
- Threads = 1 vor dem numpy-Import. Lokal kein python/awk/bc; Syntax per py_compile auf der .69.
- **Rauchtest** (Zahlen nicht gewertet), danach Nachtrag 1 (eingefroren) mit den Loeser-Einstellungen:
  - (R1) Vicsek g = 4 und g = 5 Graphbau;
  - (R2) Sierpinski g = 10, k = 46, A auf Teilgebiet gegen Z3 (E = 178,26321514805);
  - (R3) Vicsek g = 8, k = 36, A, maxcor 20 gegen 10 (Laufzeit).
- **Loeser:** L-BFGS-B mit Jacobi-Skalierung, gtol 1e-7, ftol 1e-15, maxiter 30000; maxcor 20 oder 10 nach
  Rauchtest (R3). Danach fest fuer alle gewerteten Folgen.
- **Regel fuer F2 vorab:** Braucht die volle Stufe k = 36 im Rauchtest-Mass (3 Formen + Fortsetzung, geschaetzt
  aus R3) unter 40 s, bekommt F2 6 Stufen je Periode (k = 14, 16, ..., 64). Sonst bleibt es bei 4 je Periode wie in
  der Tabelle. Die Festlegung steht in Nachtrag 1, vor dem Hauptlauf. Die F2-Kontrolle nimmt dann 2 Stufen je
  Periode aus der Hauptliste (k = 14, 20, ..., 62).
- Reihenfolge: cpu: ds, dann F1 Haupt, F1 Kontrolle; cpu2: F2 Haupt (mehrere Aufrufe), dann F2 Kontrolle.
  - Reicht die Zeit nicht, entfallen zuerst die oberen Stufen der Kontrollen, dann die obersten Stufen von F2.
- Abbildungen mit matplotlib auf der .69 (auswertung2.py):
  - abb1: p_loc und p_per gegen Q mit p_s und p_H;
  - abb2: Profile gegen Graphabstand und Lagebilder des Beutels;
  - abb3: d_s-Messung Vicsek;
  - abb4: E/Q^p_s gegen Q (log-periodisch), alle Formen.
