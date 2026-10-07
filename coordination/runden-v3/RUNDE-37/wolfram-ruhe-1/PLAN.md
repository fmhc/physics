# WOLFRAM-RUHE-1: Plan (Code-Agent fuer Leitung claude-primary)

- Plan geschrieben ab 2026-10-04 17:35:31 CEST (date), vor jedem Lauf. Karte: KARTE.md (Vorhersagen und
  Wahrscheinlichkeiten dort, hier unveraendert uebernommen, nicht neu bewertet).
- Kennzeichen wie in der Karte: [M] Mathematik, [E] Messung im Modell, [L] Literatur (Gedaechtnis), [S] Quelle selbst
  gelesen, [H] Hypothese. Zusaetzlich **[Z-K1]** = Vorgabe aus Kartenvorschlag K1 (wolfram-scan-l/DOSSIER.md Z. 136-167),
  nicht aus der Karte; **[Z-A]** = eigene Zusatzvorgabe des Code-Agenten (mit Grund).

## 1. Regel, Anfangszustand, Aktualisierung, Kausalgraph (Quelle)

- **Regel R2** [S]: `{{x, y, y}, {x, z, u}} -> {{u, v, v}, {v, z, y}, {x, y, v}}`
  - Technical Introduction (Wolfram 2020, lokale Kopie quellen/A4-Wolfram-ModelsForPhysics.pdf), Abschnitt 6.8: Regeltext
    am Ende von Druckseite 283 (Textdatei A4-...txt Z. 12384), Bilder "after 500 steps", Kegel "after 10,000 steps" und der
    Satz "the causal graph having dimension 2" auf Druckseite 284 (Z. 12388-12411). Dieselbe Regel TI S. 80 (Z. 2666)
    und Gorard A34 Fig. 45/46 (Z. 2604-2632: "causal networks are known to limit to two-dimensional Lorentzian
    manifold-like structures").
  - Muster: Relation 1 = (a, b, b) ("Marke"), Relation 2 = beliebige andere Relation mit erstem Element a. Musterplaetze
    duerfen dasselbe Element treffen (sonst passt der Selbstschleifen-Anfang nicht). v ist ein neues Element.
- **Anfangszustand:** zwei ternaere Selbstschleifen `{{0,0,0},{0,0,0}}`. Grund [S]: TI Z. 1025-1026 ("we will usually use
  such self-loop initial conditions Table[0,n,k]") und Z. 2218-2220; Abschnitt 6.8 nennt fuer R2 keinen anderen.
  Diagnose (ohne Urteil): zweiter Anfang = Kopie der linken Seite `{{1,2,2},{1,3,4}}` (TI Z. 1022-1023).
- **Standard-Aktualisierung** [S], TI Druckseite 243 (Z. 11312-11317): "in each overall step, relations are scanned from
  oldest to newest, in each case using them in an update event so long as this can be done without using any relation
  that has already been updated in this overall step". Umsetzung: In Generation g sind nur Relationen verfuegbar, die zu
  Beginn von g existieren; Durchlauf nach Erzeugungsnummer aufsteigend; fuer die gerade gelesene Relation wird unter den
  passenden Ereignissen das mit dem aeltesten Partner genommen, bei Gleichstand die Rolle "Marke" zuerst. Die
  Partnerwahl ist in der Quelle nicht festgelegt [S]; sie ist eine Festlegung dieses Plans.
- **Zufallsreihenfolge** (Kausalinvarianz-Probe): Schritt fuer Schritt ein gleichverteilt gezogenes Ereignis aus allen
  aktuell passenden.
- **Kausalgraph** [S], TI Druckseite 361 (Z. 15340-15341): "an edge between events A and B if the input to B involves
  output from A". Umsetzung: Kante A -> B, wenn B eine von A erzeugte Relation verbraucht. Die Halbordnung ist die
  transitive Huelle; laengste Ketten gleich laengste Pfade (jeder Link ist eine Kante [M]).
- **Generation T(e)** eines Ereignisses = Schrittnummer der Standard-Aktualisierung (Blaetterung "Generationsschritte
  als Zeit", Karte Z. 14-15).

## 2. Schreibtischrechnung und Ableitbarkeitsprobe (vor jedem Lauf) [M]

- Marken sind Relationen (a, b, b). Je Ereignis: -1 (Relation 1), -[z = u] (Relation 2 ist selbst Marke), +1 ((u,v,v),
  v neu), +[z = y] ((v,z,y) ist Marke), (x,y,v) nie Marke (v neu).
- Behauptung: Nach dem ersten Ereignis gilt z = y nie mehr. Grund: z = y verlangt eine zweite Relation der Form
  (x, y, .) neben der lebenden Marke (x, y, y). Neue Relationen haben die Formen (u, v, v) und (v, z, y) mit frischem v
  (passen nicht) oder (x', y', v), wobei (x', y', y') die im selben Ereignis verbrauchte Marke ist. Eine Relation
  (x, y, .) neben der Marke kann also nur aus dem Anfang stammen. Nach Ereignis 1 (Relationen (0,1,1), (1,0,0), (0,0,1))
  gibt es fuer keine der beiden Marken eine solche Relation, danach entsteht keine mehr (Induktion).
- Folgerung: Die Markenzahl steigt nie (nach Ereignis 1: 2 Marken). Jedes Ereignis verbraucht eine Marke als Relation
  1, also hoechstens so viele Ereignisse je Generation wie Marken; sobald nur eine Marke uebrig ist, hoechstens eines
  (genau eines, solange ein Partner existiert), und jedes Ereignis verbraucht die Marke des vorigen. **Dann ist die
  Kausalordnung eine Kette (totale Ordnung)**: jedes Intervall [p, q] ist eine Kette, L = N, r = sqrt(N)/2 (N = 50: 3,5;
  N = 2000: 22,4), und der Generationskegel waechst wie T + 1.
- **Vorab-Erwartung des Code-Agenten [M]** (aendert die Kartenwahrscheinlichkeiten nicht): WR1 nach Plan scheitert an
  (b) und (c) (Abschn. 4) mit Sicherheit, wenn die Rechnung oben stimmt; WR1(a) (geodaetischer Kegel) ist **nicht**
  ableitbar (haengt an den Fernkanten; TI S. 284 meldet Dimension 2). Die Kartenzeile "Fuer den Wolfram-Graphen ist
  r(eta) nicht ableitbar" waere dann zu berichtigen: Fuer R2 aus dem Standardanfang ist r ableitbar.
- Der Rauchlauf prueft die Rechnung (Ereignisse je Generation, Markenzahl, Kettenprobe). Faellt sie, gilt der Rest des
  Plans unveraendert.

## 3. Kausalinvarianz-Probe (KI, Kartenauftrag 1; kein Abbruchgrund laut Karte)

- Tiefe d(e) = Laenge der laengsten Kette von einem minimalen Ereignis bis e (intrinsisch). Je Reihenfolge so lange
  aktualisieren, bis alle passenden Ereignisse Tiefe > D haetten; dann ist der Teilgraph "Tiefe <= D" endgueltig [M].
- Vergleich: Standard plus 8 Zufallsreihenfolgen (Saaten 1-8), D = 25, 50, 100; Isomorphie der gerichteten Teilgraphen
  (networkx, Knotenmerkmal Tiefe).
- Urteil: "KI verletzt", wenn fuer irgendein D zwei Reihenfolgen nicht-isomorphe Teilgraphen liefern; "KI ohne
  Gegenbeispiel" sonst (kein Beweis).

## 4. WR1: Waechst das Netz wie 1+1? (Standardreihenfolge, Standardanfang)

- Lauf: E Ereignisse (Rauch 2e4, Haupt 5e4). Startereignisse: 40 Ereignisse gleichverteilt aus den Generationen
  [0,1 G; 0,3 G] (G = letzte Generation), Saat fest.
- **(a) Kartenwortlaut, geodaetischer Kegel** (TI S. 366-367: "follow the connections in the causal graph"):
  C_t = Zahl der Ereignisse, die von e ueber hoechstens t gerichtete Kanten erreichbar sind (e mitgezaehlt), gemittelt
  ueber die Startereignisse, t = 1 bis 100. Gueltig nur bis t_g = groesstes t, bei dem kein Kegel die letzten 2 % der
  Generationen erreicht; t_g < 40 -> (a) "nicht bestimmbar". D_geo = Steigung (kleinste Quadrate) von log C_t gegen
  log t fuer t in [t_g/4, t_g]. **(a) erfuellt, wenn 1,8 <= D_geo <= 2,2.**
- **(b) [Z-K1] Ereignisse je Generation wachsen mit der Knotenzahl** (K1 "Vorpruefung (i)", gegen Front-Wachstum):
  Steigung s_b von log(Ereignisse je Generation, in 20 gleich langen Generationsfenstern gemittelt) gegen log(Zahl
  lebender Relationen am Fensterende) ueber die zweite Laufhaelfte. **(b) erfuellt, wenn s_b >= 0,25 und im letzten
  Zehntel der Generationen im Mittel >= 10 Ereignisse je Generation.**
- **(c) [Z-A] Generationskegel** (Kegelvolumen gegen die Aktualisierungs-Blaetterung, die WR2 benutzt; Grund: r haengt
  an der Ordnung, nicht an Graphabstaenden): C^gen_T = Zahl der f mit e <= f (Ordnung) und T(f) - T(e) <= T, gemittelt
  ueber dieselben Starts, T = 1 bis 100; D_gen = Steigung von log C^gen_T gegen log T fuer T in [25, 100].
  **(c) erfuellt, wenn 1,8 <= D_gen <= 2,2.**
- **WR1 nach Plan = (a) und (b) und (c). WR1 nach Kartenwortlaut = (a).**
- Diagnosen ohne Urteil: Markenzahl je Generation, Kettenprobe (Anteil der Ereignisse, deren Vorgaenger in der
  Standardreihenfolge ein Elter ist), dieselben Groessen fuer den zweiten Anfang und fuer Zufallsreihenfolge Saat 1.
- **Abbruch (Karte Z. 31, Auftrag):** Ist WR1 nach Plan verfehlt, wird WR2 nicht geprueft ("abbrechen und melden").

## 5. Intervalle, Schraegstellung eta, Fehler (fuer WR0 und WR2)

- **Intervall** [p, q], p < q: N = |{e : p <= e <= q}| (mit Endpunkten), L = Zahl der Elemente der laengsten Kette von p
  nach q (mit Endpunkten), r = L/(2 sqrt N). Endpunkte mitgezaehlt, damit die Gitterformel des Dossiers
  r = (a+b+1)/(2 sqrt((a+1)(b+1))) (Z. 108, 149) genau gilt; Karte: "Ereignisse dazwischen" (Abweichung benannt).
- **Zeit** T: Gitter T = i + j; Poisson T = u + v (Lichtkegelkoordinaten, Dichte 1 je Einheitsflaeche du dv); R2 T =
  Generation.
- **Eichung c** (Dichte in Zeiteinheiten): quadratische Anpassung C^gen_T = A + B T + (c^2/2) T^2 an den
  Generationskegel des jeweiligen Graphen, T in [10, 100] (Gitter: genau c = 1; Poisson: c = 1 im Mittel [M]).
  c^2 <= 0 -> eta nicht bestimmbar.
- **Schraegstellung** [M]: x = c (Delta T + 1)/(2 sqrt N), cosh eta = x (eta = arcosh x fuer x >= 1, sonst 0). Grund:
  in 1+1 mit Lichtkegel-Ausdehnungen U, V gilt Delta T = U + V, N ~ UV, cosh eta = (U+V)/(2 sqrt(UV)), also das
  "Verhaeltnis der Nullrichtungen" eta = (1/2) ln(U/V) aus Endpunkten und N. Benutzt nicht die innere Anordnung des
  Intervalls, daher fuer Poisson bei festem N von L unabhaengig [M]. Folge fuer das Gitter: L = Delta T + 1, also r = x
  genau; die Gitterkontrolle ist mit dieser Definition eine Programmprobe (Zaehlen von L, N, Delta T) und die
  Ruhesystem-Referenz (Steigung 1), keine unabhaengige eta-Pruefung [M]. Zusaetzlich fuer die Kontrollen: eta_wahr aus
  Koordinaten.
- **Kontrolle P (Poisson 1+1):** je Intervall Ziel eta_w ~ U[0, 2], ln N_ziel ~ U[ln 50, ln 2000]; U = sqrt(N_ziel) e^eta,
  V = sqrt(N_ziel) e^-eta; Innenpunkte ~ Poisson(UV) gleichverteilt im Rechteck [0,U] x [0,V] (exakt nach Slivnyak-Mecke
  [L]); L = 2 + laengste steigende Teilfolge (O(n log n)). Rauchlauf: Gleichheit mit der allgemeinen Ketten-Routine
  (Elternlisten) an 40 kleinen Intervallen. Eichung c aus einem gestreuten Kegel (Dreieck u + v <= 100).
- **Kontrolle G (Nullgitter):** Gitter 420 x 420 als gerichteter Graph (Kanten (i,j)->(i+1,j), (i,j)->(i,j+1)); Intervalle
  mit a + 1 = round(sqrt(N_ziel) e^eta), b + 1 = round(sqrt(N_ziel) e^-eta), a, b >= 1, Lage zufaellig; N, L ueber
  **dieselbe** Graph-Routine wie bei R2 (Vorwaerts- und Rueckwaerts-Suche, laengste Kette per Elternlisten).
- **R2-Intervalle** (nur fuer WR2): p gleichverteilt aus Generationen [0,1 G; 0,6 G]; Ziel-Delta T ~ log-gleichverteilt
  in [5, 3000]; q gleichverteilt aus den Ereignissen der Zielgeneration; Abweisung, wenn q nicht in der Zukunft von p
  oder N nicht in [50, 2000].
- **Stichprobe:** je Graph 6000 Intervalle (Rauch: 1500 fuer P und G, keine R2-Intervalle). N-Bins [50,100), [100,200),
  [200,500), [500,1000), [1000,2000].
- **Fehler:** Steigung b von r gegen x (kleinste Quadrate, Intervalle mit 1 <= x <= 4) mit Standardfehler; Mediane mit
  16-/84-%-Bootstrap (200 Ziehungen, Saat fest). Bild: Median r gegen eta-Bin ([0;0,25), ... , [1,5;2,0)) je N-Bin,
  dazu cosh eta.

## 6. Urteilsregeln in Zahlen (vor jedem Lauf festgelegt)

| WR | nach Plan | nach Kartenwortlaut |
|---|---|---|
| WR0 | P(i): in jedem N-Bin mit >= 200 Intervallen abs(b_P) <= 0,05; P(ii): Median r im Bin [1000,2000] in [0,92; 1,05]; G(i): max abs(r - x) <= 1e-9 (Programmprobe); G(ii): abs(Median(r/cosh eta_wahr) - 1) <= 0,02 im Bin [1000,2000]; G(iii): b_G in [0,9; 1,1] in jedem N-Bin mit >= 200 Intervallen. Alle fuenf -> eingetroffen | Poisson: Median r in [0,95; 1,05] in **jedem** N-Bin und abs(b_P) <= 0,05; Gitter: abs(Median(r/cosh eta) - 1) <= 0,02 in jedem N-Bin, eta = Programm-eta (zusaetzlich berichtet mit eta_wahr) |
| WR1 | (a) und (b) und (c) aus Abschn. 4 | (a) |
| WR2 | nur wenn WR1 nach Plan: s = b_R2/b_G in den zwei groessten N-Bins; s >= 0,5 in beiden -> eingetroffen; s < 0,5 im groessten -> verfehlt; sonst unentschieden; weniger als 30 Intervalle mit x <= 1,2 oder mit x >= 1,8 im Bin, oder c^2 <= 0 -> nicht entscheidbar | dieselbe Regel, wenn WR1 nach Kartenwortlaut gilt ("auch bei den groessten N" = groesster Bin); sonst entfaellt |

- Vorab bekannte Grenzen [M, L]: Fuer Poisson liegt r bei endlichem N unter 1 (Baik-Deift-Johansson,
  E[LIS] ~ 2 sqrt n - 1,77 n^(1/6) [L]): erwartet r ~ 0,90 bei N ~ 70, ~ 0,95 bei N ~ 1400. **WR0 nach Kartenwortlaut wird
  daher in kleinen N-Bins voraussichtlich verfehlt** (Endlichkeitseffekt, nicht Programmfehler); deshalb die
  Plan-Fassung P(ii) nur im groessten Bin mit Untergrenze 0,92. Gitter mit eta_wahr: r/cosh eta_wahr ~ 1 - 1/(a+b+2)
  -> Kartenwortlaut mit eta_wahr in kleinen Bins verfehlt; mit Programm-eta trivial erfuellt.
- Keine Schwelle wird nach Befund geaendert. Abweichungen vom Plan werden als Selbstanzeige gemeldet.

## 7. Laeufe (nur .69, kleintest.sh, Spuren cpu6 und cpu7, je Lauf <= 10 min, 1 Thread, 4 GB)

- **Rauchlauf** (rauch/): `rauch.py`: Zeit- und Speichermessung; WR0 mit 1500 Intervallen je Kontrolle; Programmprobe
  LIS gegen Ketten-Routine; WR1 mit E = 2e4; KI mit D = 25, 50; Markenzahl, Kettenprobe. Keine R2-Intervalle (WR2-Werte
  nicht ansehen).
- **Einfrieren:** Kopien `PLAN.md.eingefroren-<zeit>` und `code/*.py.eingefroren-<zeit>`, Hashes in
  EINGEFROREN-SHA256.txt.
- **Hauptlaeufe** (lauf/): `haupt_kontrollen.py` (WR0, 6000 Intervalle je Kontrolle, cpu6); `haupt_r2.py` (WR1 mit
  E = 5e4, KI mit D = 25, 50, 100, Diagnosen, R2-Intervalle nur als Daten; cpu7). `auswertung.py` -> auswertung.json und
  Bild r(eta). Aufteilung, falls ein Lauf laenger als 10 min dauerte: E halbieren und das als Selbstanzeige melden.
- Ergebnisse per scp nach rauch-69/ bzw. lauf-69/, Pruefsummen in lauf-69/PRUEFSUMMEN.txt.
