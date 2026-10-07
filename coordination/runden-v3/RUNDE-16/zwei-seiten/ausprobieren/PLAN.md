# PLAN: Ausprobieren V1 bis V5 (Runde 16, Code-Agent)

- Geschrieben ab 2026-10-02 08:22:05 CEST (date), Start der Zeitbox 08:16:11 CEST, Ende spaetestens 09:46 CEST.
- Grundlage: KARTE.md (Vorhersagen dort bindend), ZWEI-SEITEN-DES-FELDES-v2.md Abschnitte 1, 2, 4, 5, 6, 7, 17.
- Code: ausprobieren/code/ (numpy, scipy, eigener Code). Ausgaben: ausprobieren/aus/ (JSON, TXT, PNG).
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu2, je Aufruf <= 10 min. Lokal nur Rauchtests (<= 120 s, nice 19, ein Thread, timeout).
- Literatur vorab (arXiv-API, 08:20): Vanderbei/Kolemen, arXiv:astro-ph/0606510 (Abstract): "always unstable for 2<=n<=6 and for n > 6 they are stable provided that the central mass is massive enough". arXiv:1903.10270 (Abstract): (1+n)-Gon fuer n >= 8 bei jeder Exzentrizitaet stabil, wenn die Zentralmasse gross genug ist. Maxwells Faktor 0,4352 N^3 nur aus dem Gedaechtnis [L?].

## Einheiten und gemeinsame Regeln

- Dimensionslos: G = 1, M = 1, R = 1 (V2); m = k = 1, L0 = 1 (V1, V3); m_Feld = 1 (V5).
- Spektrale Stabilitaet: alle Eigenwerte s der Begleitmatrix [[0, I], [-M^-1 K_eff, -M^-1 G]] mit Re s <= tol. tol = 1e-6 (Haupt), Robustheit mit 1e-5 und 1e-7. Triviale Eigenwerte (Symmetrien) werden benannt und gezaehlt; sie liegen exakt auf der imaginaeren Achse, ihr numerischer Realteil (Jordan-Bloecke) gilt als Rauschboden und wird berichtet.
- Zwei Aufloesungen je Ergebnis: analytische Hesse-Matrix gegen finite Differenzen (bzw. zwei Zeitschritte oder Toleranzen).

## V1 Federtetraeder

- Methode: E = (k/2) sum (L - L0)^2, regulaeres Tetraeder mit L0 = 1. Hesse-Matrix analytisch (Summe k u u^T, ohne Vorspannung) und per zentralen finiten Differenzen (h = 1e-4 und 1e-5). Eigenwerte.
- Zusatzkontrolle: nichtlineare Zeitentwicklung (Velocity-Verlet), Zufallsauslenkung 1e-4, dt = 0.01 und 0.005, T = 400; Energiefehler; FFT-Spitzen gegen sqrt(1), sqrt(2), 2.
- Treffer, wenn alle Eigenwerte innerhalb 1e-8 (analytisch) bzw. 1e-5 (FD) bei {0 x6, 1, 1, 2, 2, 2, 4} liegen.

## V2 Maxwell-Ring mit Gravitation

- N + 1 Koerper, Zentralmasse M = 1 im Schwerpunkt, N Massen m = eps auf R = 1. Omega^2 = 1 + (eps/4) sum_{j=1}^{N-1} 1/sin(pi j/N). Kontrolle: Gradient des effektiven Potentials im Gleichgewicht < 1e-12.
- Methode A: volles (N+1)-Koerper-System, Hesse-Matrix analytisch, K_eff = H - Omega^2 M P_ebene, G = 2 Omega M J; in 2D und 3D.
- Methode B: heliozentrische Koordinaten (Schwerpunkt exakt abgetrennt), Jacobi-Matrix der Bewegungsgleichungen im mitrotierenden System per finiter Differenzen (h = 1e-6), 2D.
- Erwartete triviale Eigenwerte (2D, Methode A): 0 (2-fach, Drehung und Radius/Omega-Familie), +-i Omega (Schwerpunkt, je 2-fach, Jordan) und die Kepler-Familie bei +-i Omega. Benannt, nicht als Instabilitaet gezaehlt; Realteile zeigen den Rauschboden.
- Laufliste: N = 3..16 bei eps = 1e-6 und 1e-4 (2D A und B, 3D A). eps-Raster 1e-9..1e-1 (81 Punkte, 0,1 Dekaden) fuer N = 3..40, dazu 48 und 64 (nur A, 2D); fuer N >= 7 Bisektion der Grenze eps_c(N) (groesstes stabiles eps unterhalb des ersten Umschlags), Nicht-Monotonie wird gemeldet.
- Skalierung: Fit log eps_c gegen log N fuer N = 20..64; Steigung p (Vorhersage -3) und Vorfaktor eps_c N^3 (Gedaechtnis: 1/0,4352 = 2,298).
- Zeitentwicklung (Kontrolle): N = 6 und N = 8, eps = 1e-4, Inertialsystem, DOP853, rtol = 1e-10 und 1e-12, T = 3000, Stoerung 1e-7. Energie- und Drehimpulsfehler; Wachstumsrate der Formabweichung gegen max Re s aus Methode A.
- Positivkontrolle bestanden, wenn: N <= 6 instabil fuer alle eps im Raster, N >= 7 stabil fuer kleine eps; A und B stimmen in der Einstufung ueberein.

## V3 Federring N + 1

- Massen 1 (Ring und Zentrum), k_Speiche = k_Ring = 1.
  - Variante F0: Ruhelaengen L_s = 1, L_r = 2 sin(pi/N), spannungsfrei bei Omega = 0.
  - Variante F1: L_s = L_r = 1, fuer N != 6 vorgespannt.
- R(Omega) aus der Kraeftebilanz: Omega^2 R = k_s (R - L_s) + 2 k_r (2 R sin(pi/N) - L_r) sin(pi/N), also linear in R; existiert fuer Omega^2 < K_N = k_s + 4 k_r sin^2(pi/N).
- Methode A: analytische Hesse-Matrix (k u u^T + (T/L)(I - u u^T)), K_eff, G wie V2, 2D und 3D. Methode B: Hesse per finiter Differenzen (h = 1e-5), 2D.
- Triviale Eigenwerte: Drehung 0 (2-fach), Schwerpunkt in der Ebene +-i Omega (je 2-fach); in 3D zusaetzlich z-Translation 0 (2-fach) und Kippungen +-i Omega.
- Laufliste: N = 4..32, Omega = 0.3, 0.6, 0.9 (alle unter sqrt(K_N), da K_N >= 1), dazu feines Omega-Raster 0..0,999 sqrt(K_N) (120 Punkte) fuer Omega_c(N) = kleinstes Omega mit Instabilitaet.
- Kennzahlen: S(N) = groesster nicht-trivialer Realteil; omega_soft(N) = kleinste nicht-triviale |Im s| bei Omega = 0.6; Omega_c(N).
- **Auffaelligkeit (vorab festgelegt):** fuer jede Kennzahl X(N), 8 <= N <= 28: quadratischer Fit an die Nachbarn N-4..N-1 und N+1..N+4 (ohne N); sigma = Standardabweichung der Nachbar-Residuen (ddof 3); z(N) = (X(N) - Fit(N))/sigma. Auffaellig nur, wenn |z| > 3 UND die relative Abweichung |X - Fit|/|X| > 1 %. Berichtet: z(11), z(19), Zahl aller auffaelligen N.

## V4 Ticks ereignisgenau

- Zwei regulaere Tetraeder (Kantenlaenge 1). A: Mittelpunkt 0, Drehung um z mit omega_A = 1. B: Mittelpunkt c_B(t) = (0.25, 0.1, 0.05) + 0.3 sin(0.618 t) e_x, Drehung um n_B = (1, 2, 2)/3 mit omega_B = sqrt(2), feste Anfangsdrehung (Seed 1). Bahn analytisch.
- Paare: Ecke-Flaeche (4 x 4 x 2 = 32), Kante-Kante (6 x 6 = 36). chi = det[x_b - x_a, x_c - x_a, x_d - x_a].
- Ereignisgenau: chi auf dem Raster t_k = k dt; bei Vorzeichenwechsel brentq (xtol 1e-14) auf der analytischen Bahn, dann Innen-Test (baryzentrisch bzw. Kreuzung innerhalb beider Kanten). Zaehlt N_EF, N_KK; Rate nu = N/T.
- Naiv: Zustand B(t_k) = Menge der (Kante, Flaeche)-Paare zwischen den Koerpern, die sich schneiden (48 Paare). Naive Zahl = sum_k |B(t_k) Delta B(t_k+1)|; Sollwert ohne Verluste 3 N_EF + 4 N_KK. Dazu Zahl der Schritte mit Zustandswechsel.
- Laufliste: dt in {0.2, 0.1, 0.05} und {0.02, 0.01, 0.005}, Referenz dt = 0.001; T = 200 und 400. Ereigniszeiten gegen die Referenz abgeglichen (max |Delta t|). Robustheit: 5 Stoerungen von c_B um 1e-3.

## V5 Diskretes sextisches Feld auf dem Rad-Graphen

- Graph: Ring aus N Knoten plus Zentrum, mit allen Ringknoten verbunden; J gleich auf allen Kanten. Gleichung psi_i'' + sum_j J (psi_i - psi_j) + V'(|psi_i|^2) psi_i = 0, V'(s) = 1 - 2 s + 1,5 s^2.
- Band (linear): omega^2 in {1} u {1 + J (3 - 2 cos(2 pi k/N))} u {1 + J (N+1)}. Lokalisierte Moden unterhalb 1 gesucht.
- Stationaer, reell, Newton mit analytischer Jacobi-Matrix (Toleranz 1e-12), Start auf einem Ringknoten bzw. dem Zentrum, Fortsetzung in omega^2 von 0,995 abwaerts (Zweig s < 2/3) und vom Umkehrpunkt weiter (Zweig s > 2/3, Pseudo-Bogenlaenge ueber die Amplitude).
- Stabilitaet: (u, v) = Real- und Imaginaerteil im mitrotierenden Phasenbild; K = diag(L + V' + 2 phi^2 V'' - omega^2, L + V' - omega^2), G = 2 omega [[0, -I], [I, 0]]. Trivial: Phasenmode 0 (2-fach). Stabil bei fester Ladung, wenn alle nicht-trivialen Re s <= tol.
- Q = 2 omega sum phi_i^2; dQ/domega zweifach: finite Differenzen entlang des Zweigs und aus dem linearen Gleichungssystem (dphi/domega).
- Laufliste: N = 8..21, J = 0.05, 0.1, 0.2; Ring- und Zentrumsmode; omega^2-Raster 0,30..0,995. Kontrolle J = 1e-4 (Anti-Kontinuum: Fenster [1/3, 1)).
- Zeitentwicklung (Kontrolle): N = 11 und 12, J = 0.1, je eine Mode auf jedem Zweig, DOP853 rtol 1e-10 und 1e-12, T = 500, Stoerung 1e-6. E- und Q-Fehler, PR(t).
- Auffaelligkeit wie V3 auf omega^2_min(N) (unteres Ende des Existenzfensters) und auf dem stabilen Anteil.

## Auswertung

- Je Versuch: Vorhersage der Karte gegen Ausgang, Kontrollen, Abbildung.
- Gemessene Laufdauern: werden nach den Laeufen unten ergaenzt (nicht im eingefrorenen Stand).

## Nachtrag nach dem Einfrieren (ab 08:40 CEST, nicht Teil des eingefrorenen Stands)

Abweichungen vom eingefrorenen Plan, jeweils mit Grund:

1. V1: dt-Liste um 0.0025, 0.00125, 0.000625 erweitert (Energiefehler von Verlet faellt wie dt^2, die Kartenschwelle 1e-6 wird erst bei dt = 0.000625 erreicht). FFT-Spitzensuche nach dem Rauchtest auf lokale Maxima umgestellt (vorher fing sie eine Nebenkeule).
2. V2: Methode B (finite Differenzen) hat am Jordan-Block der Drehmode einen Rauschboden um 1e-5; Einstufung fuer B deshalb ohne die zwei betragskleinsten Eigenwerte (Drehpaar). Der erste .69-Lauf (v2_maxwell.py) wurde nach 600 s vom Zeitlimit beendet, bevor er JSON schrieb (Selbstanzeige: Laufzeit unterschaetzt, BLAS-Threads gegen CPUQuota 100 %). Wiederholung als v2b_maxwell.py in drei Teilen (teil1: Tabelle und N = 3..24; teil2: N = 25..40, 48, 64; zeit), mit OMP/OPENBLAS-Threads = 1, sonst gleicher Code.
3. V3: gleiche Ursache; Wiederholung als v3b_federring.py je Variante. Nachtraeglich (nicht vorab festgelegt) die Kennzahl Omega_stab (Rotation stabilisiert die vorgespannte Variante F1) und ein 3D-Omega-Raster.
4. V5: Newton vom Anti-Kontinuum-Startwert fiel bei J > 0 oft auf die Nullloesung; ersetzt durch Fortsetzung in J von 0 (MacKay-Aubry, 12 Schritte) und Pflicht-Amplitude > 1e-3. VK-Pruefung korrigiert: Vorhersage stabil, wenn K_u keine negative Richtung hat oder genau eine und dQ/domega < 0.

## Laufliste und gemessene Dauer (.69, kleintest.sh)

- wird in ERGEBNIS.md Abschnitt 4 gefuehrt.
