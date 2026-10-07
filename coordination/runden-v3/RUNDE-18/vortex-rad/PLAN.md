# PLAN VORTEX-RAD (Runde 18, Code-Agent fuer claude-primary)

- Zeitbox ab 14:13:24 CEST (date), Ende spaetestens 15:43. Plan geschrieben ab 14:25:30 CEST (date), vor jeder Rechnung.
- Verbindlich aus der Karte: Modell, Wirbel mit Ladung m, Scan, W1 bis W5, Bedeutung. Hier steht nur, wie gerechnet und
  wie W1 bis W5 ausgezaehlt werden. Explorativ (v3), Hypothesen [H].

## 1. Rechnung

**Gleichung (wie V5):** L phi + (V'(|phi|^2) - omega^2) phi = 0, L = J (D - A) auf dem Rad (Ring 0..N-1, Nabe N),
V'(S) = 1 - 2S + 1,5 S^2. Stationaer Psi = phi e^{i omega t}, phi komplex.

**Newton:** 2(N+1) reelle Unbekannte (Re, Im). Phase fixiert durch Im phi_g = 0 am Knoten g (Wirbel: Ringknoten 0):
Unbekannte Im phi_g und Gleichung Im F_g entfallen (Noether-Identitaet Sum Im(phi_i^* F_i) = 0). Konvergenz: max |F| < 1e-12
auf ALLEN 2(N+1) Gleichungen. Jacobi-Matrix = K der Linearisierung (selbst hergeleitet, siehe 2.).

**Familie U, gleichfoermiger Wirbel (Hauptscan, Karte):**
- N = 4..24, m = 1..floor(N/2), J in {0,02; 0,05; 0,1}, Ast klein/gross.
- Raster je Fall: c_k = 1/3 + (2/3)(k - 1/2)/30, k = 1..30, omega^2 = c_k + J g_m mit g_m = 3 - 2 cos(2 pi m/N).
  c = V'(S) ist die Einzelplatzgroesse. Begruendung: Der gleichfoermige Wirbel existiert auf dem kleinen Ast genau fuer
  c in (1/3; 1), also omega^2 in (1/3 + J g_m; 1 + J g_m) [ES]. Das ist das Existenzfenster der Karte. Der grosse Ast
  existiert fuer alle c > 1/3; gerechnet wird nur das Bild des Einzelplatzfensters, S in (2/3; 4/3). Darueber: nicht gescannt.
- Fortsetzung in J von J = 0 in 20 Schritten. Start: Ring auf dem Ast mit Phasen 2 pi m j/N, Nabe 0.
  - Pfad A (festes omega^2, wie V5): wenn der Ast bei J = 0 fuer dieses omega^2 existiert (grosser Ast immer, kleiner Ast fuer omega^2 < 1).
  - Pfad B (festes c, omega^2(J') = c + J' g_m): nur kleiner Ast mit omega^2 >= 1, weil dort bei J = 0 keine Einzelplatzloesung existiert.
    Abweichung vom Hinweis "Fortsetzung in J", begruendet; Pfad B startet exakt auf der Formel und prueft W1 deshalb nicht.
  - Schrittkriterien wie V5: Newton konvergiert, max |phi| >= 1e-3, Sprung je Schritt <= 0,3.
- Danach gestoerter Neustart am Zielpunkt: Stoerung 1e-3 (komplex, Seed fest) auf allen N+1 Knoten einschliesslich Nabe.
- m = N/2 (gerades N) ist reell (Phasen 0, pi), wird mitgerechnet.

**Lokalisierte Wirbel (Karte: "sofern sie existieren"), Fortsetzung bei festem omega^2 aus dem Antikontinuumslimes:**
- omega^2-Raster: 30 Mittelpunkte in (1/3; 1), Ast klein/gross, J wie oben, 40 Schritte.
- L-a, Teilring-Wirbel: K Ringknoten im Abstand d = N/K, also K | N, 3 <= K < N. Phasen 2 pi m' k/K (k = 0..K-1),
  Ladung m' = 1..floor((K-1)/2) (echte Wirbel; m' = K/2 waere reell). Nabe 0 aus Symmetrie.
  - Geloest im symmetrischen Teilraum (d Knoten, verdrehte Randbedingung phi_{j+d} = e^{2 pi i m'/K} phi_j).
    Grund: Im vollen Raum sind die relativen Phasen bei kleinem J nur mit J^2 bzw. J^d steif, Newton waere numerisch singulaer.
  - Danach volles Residuum auf allen Gleichungen < 1e-10 als Pflicht. Stabilitaet im vollen 2(N+1)-System.
  - Existiert, wenn Fortsetzung, volles Residuum und Lokalisierung gelingen (>= 50 % von |phi|^2 je Bereich auf dem Startknoten).
- L-b, Dreierwirbel ohne exakte Symmetrie: N = 7..24 mit 3 teilt N nicht, Orte {0, round(N/3), round(2N/3)},
  Phasen 0, 2pi/3, 4pi/3. Volles Newton. Existiert, wenn Fortsetzung gelingt, Windung um die drei Orte = 1 und
  >= 50 % von |phi|^2 auf den drei Orten. Zweck: Gibt es nabengetragene Wirbel auch fuer Primzahlen?
- L-c, zusammenhaengender Bogen (Negativkontrolle): N in {11, 12, 19, 20}, K = 3 und 4 benachbarte Knoten, m = 1,
  omega^2 in {0,6; 0,8}. Existiert, wenn Fortsetzung gelingt, Phasenschritte innerhalb 0,3 rad von 2 pi/N bleiben und
  >= 50 % von |phi|^2 auf dem Bogen liegen.

## 2. Stabilitaet

- Psi = e^{i omega t}(phi + w), w = u + i v: [u; v]'' + G [u; v]' + K [u; v] = 0.
  - G = [[0, -2 omega I], [2 omega I, 0]].
  - K = [[L + D(V' - omega^2 + 2V'' a^2), D(2V'' a b)], [D(2V'' a b), L + D(V' - omega^2 + 2V'' b^2)]], phi = a + i b.
  - Herleitung geprueft: Phasenmode (-b, a) liegt im Kern von K. Fuer reelles phi folgt exakt V5 (K_u, K_v).
- Begleitmatrix [[0, I], [-K, -G]], numpy eig. Die zwei Eigenwerte kleinsten Betrags (Jordan-Paar der Phasenmode) werden
  abgezogen; ihr Betrag wird mitgeschrieben (Soll < 1e-5).
- Spektral stabil: max Re < 1e-8. Zur Robustheit auch bei 1e-6 und 1e-10 eingestuft.
- Art: reell (alle instabilen Eigenwerte |Im| <= 1e-6), oszillatorisch (alle |Im| > 1e-6), gemischt. Dazu die
  dominante Art (Eigenwert mit groesstem Re).
- Krein-Signatur jedes Eigenwerts i sigma auf der Achse: Vorzeichen von E = x^* K x + sigma^2 |x|^2 (Energie im
  mitrotierenden Bild). n_K^- = Zahl der Paare mit E < 0.
- Kontrolle Indexzaehlung (Kapitula-Kevrekidis-Sandstede): N_r + 2 N_c + 2 n_K^- = n(K) - n(D),
  n(D) = 1 falls dQ/domega < 0 (wie die V5-Regel), Q = 2 omega Sum |phi|^2. Abweichungen werden gezaehlt.

## 3. Kontrolle gegen V5 (m = 0, reelle Moden, neuer Code)

- Ring- und Nabenmode, N = 8..21, J in {0,05; 0,1}, Ast klein/gross, omega^2 = 0,300..0,995 (Schritt 0,005), 12 Schritte,
  V5-Lokalisierung (argmax am Ort, PR < 3, Amplitude > 1e-3).
- Vergleich mit V5-ERGEBNIS: Fenstergrenzen (z. B. J = 0,05 Ring klein [0,475; 0,945 bis 0,960], stabil bis 0,93 bis 0,95)
  und V5-Regel (stabil, wenn n(K) = 0 oder n(K) = 1 mit dQ/domega < 0) an allen Punkten.
- Nabenmoden-Schwelle: groesstes N mit Nabenmode fuer J in {0,03; 0,04; 0,05; 0,06; 0,08}, N = 4..26. Soll 20, 15, 11, 9, 7.
- Bestanden, wenn N_max gleich, Fenstergrenzen innerhalb eines Rasterschritts und die V5-Regel an >= 99,9 % der Punkte trifft.

## 4. Zeitentwicklung (Kontrolle der Linearisierung)

- N = 12, J = 0,05, c = 0,6: (gross, m = 1), (gross, m = 5), (klein, m = 1), (klein, m = 5). Zusaetzlich der oszillatorisch
  instabile U-Punkt mit dem groessten max Re bei N in {11, 12} (falls vorhanden, sonst bei beliebigem N).
- Stoerung 1e-6, T = 400, DOP853 rtol 1e-10. Abstand zur mitrotierenden Loesung nach Abzug der globalen Phase;
  Wachstumsrate aus log(Abstand) zwischen 1e-5 und 1e-2 gegen max Re. Energie- und Ladungsfehler.

## 5. Auszaehlung W1 bis W5 (vor dem Lauf festgelegt, nur Familie U)

- f(N, m) = Anteil spektral stabiler Rasterpunkte unter den konvergierten Punkten je (N, m, J, Ast).
- **W1:** eingetroffen, wenn alle U-Punkte konvergieren, max_j | |phi_j|^2 - S(c) | <= 1e-10 und |phi_Nabe| <= 1e-10.
  Neustart-Ergebnis nur berichtet.
- **W2:** J = 0,02, grosser Ast, m = 1. Ein N gilt als stabil bei f >= 0,5. Eingetroffen, wenn >= 14 der 21 N stabil sind.
  J = 0,05 und 0,1 nur berichtet.
- **W3:** Je (J, Ast): Etikett f >= 0,5. Bester Einzelschwellen-Klassifikator auf x = m/N (beide Richtungen).
  - (a) In jeder Kombination mit beiden Etiketten erklaert er >= 90 % der (N, m), und mindestens 3 der 6 Kombinationen haben beide Etiketten.
  - (b) Fehlerquote bei primem N hoechstens 10 Prozentpunkte ueber der bei zusammengesetztem N (gepoolt).
  - Eingetroffen, wenn (a) und (b). "Instabil nahe m = N/2" wird je Ast nur berichtet.
  - m/N = 1/4 (nur 4 | N) zaehlt als m/N-Wert.
- **W4:** Fuer N* in {11, 19} und jede (J, Ast): Delta = Mittel ueber m von f_{N*}(m) minus Mittel der Nachbarn N* +- 1,
  deren f linear in m'/N' auf x = m/N* interpoliert (Randwerte festgehalten). Eingetroffen, wenn alle 12 Delta <= 0,10.
- **W5:** Unter allen instabilen U-Punkten der Anteil mit oszillatorischer dominanter Instabilitaet.
  - Eingetroffen bei > 50 %, sonst nicht.
  - Zusaetzlich: Anteil oszillatorischer Punkte, deren stabiler Nachbarpunkt im Raster n_K^- >= 1 hat (passt zu einer Krein-Kollision).
- Lokalisierte Wirbel (L-a, L-b, L-c) werden getrennt berichtet und gehen nicht in W1 bis W5 ein.

## 6. Schreibtisch vor dem Lauf (Code-Agent, [ES]/[H], keine Kartenvorhersage, aendert W1 bis W5 nicht)

- Phasendynamik bei kleinem J: delta theta'' = -omega'(Q) 2 J A^2 cos(2 pi m/N) L_Ring delta theta.
  - Kleiner Ast: dQ/domega < 0. Grosser Ast: dQ/domega > 0.
- Erwartung:
  - Grosser Ast stabil fuer m/N < 1/4, reell instabil fuer m/N > 1/4.
  - Kleiner Ast reell instabil fuer m/N < 1/4, fuer m/N > 1/4 stabil mit N - 1 Paaren negativer Krein-Signatur
    (oszillatorische Instabilitaet durch Kollision moeglich).
  - m/N = 1/4 entartet in erster Ordnung.
- Das legt W5 eher "nicht eingetroffen" nahe und W3 als m/N-Schwelle bei 1/4.
- L-a existiert bei kleinem J aus Symmetrie, gibt es aber nur fuer N mit Teiler 3 <= K < N, also nicht fuer Primzahlen.
- L-c sollte nicht existieren: Die Bedingung erster Ordnung am Bogenende erzwingt Phasenschritte 0 oder pi.

## 7. Laeufe (.69, Spur cpu6, je <= 600 s)

1. `vortex_rad.py schnell` (Rauchtest, kleine Teilmenge)
2. `vortex_rad.py kontrolle`
3. `vortex_rad.py nmax`
4. bis 6. `vortex_rad.py scan <J>` fuer J = 0,02 / 0,05 / 0,1
7. `vortex_rad.py lokal`
8. `vortex_rad.py zeit`
9. `auswertung.py` (W1 bis W5, Abbildungen)

- JSON wird je N zwischengespeichert.
- Laeuft ein Aufruf in die Grenze, wird er ohne Code-Aenderung in Teilen wiederholt (Argument N-Bereich).
  Die Abweichung wird nachtraeglich vermerkt.
