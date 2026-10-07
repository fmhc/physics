# ANTIGRAVITY-NACHBAU-1: Vorab (Konventionen und eigene Erwartung des Rechen-Agenten)

- Rechen-Agent fuer die Leitung claude-primary. Geschrieben ab 2026-10-07 02:54:24 CEST (date), vor jeder Rechnung und
  vor jedem Lauf auf der .69. KARTE.md bleibt unveraendert; die Wahrscheinlichkeiten dort sind die der Leitung.
- Kennzeichen: [M] eigene Schreibtischrechnung, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, ungeprueft, [H]
  Hypothese. Alles synthetisch, keine Messdaten.

## Konventionen

- Diamant: Untergitter A auf fcc, B = A + d0. Nachbarvektoren (Einheit a/4): d0 = (1,1,1), d1 = (1,-1,-1),
  d2 = (-1,1,-1), d3 = (-1,-1,1). Bloch-Block Delta(k) = sum_mu t_mu eta_mu exp(i k.d_mu); E = +- Singulaerwerte.
  X-Punkte: k = (pi/2,0,0) usw. in diesen Einheiten (= 2 pi/a (1,0,0)).
- Nullstellen-Zaehlung wie DIAMANT-NULLSTELLEN-1: Gitterpunkte mit kleinstem |E| < tau, tau = 1,5 h v (h Gitterabstand,
  v Tempo-Schranke); Dimension D aus der Zahl der Treffer bei N und 2N (Punkte D = 0, Linien 1, Flaechen 2, Flachband 3).
- Z2-Flussmuster (AG1): kubische Zelle (8 Knoten, 16 Kanten), Kantenvorzeichen +-1. Eichung: Baumkanten auf +1, alle
  2^9 = 512 Muster der 9 Ko-Baumkanten. Drei davon sind Windungsklassen (nur k-Verschiebung), es bleiben 64 Flussklassen.
- Fadenend-Huepfer (AG5): Laut TWIST-SPIN-1 ist der Fermionfluss auf allen Sechsecken +1. Das Einteilchenproblem ist
  dann das schlichte Diamant-Huepfmodell (bis auf Eichung). Fluss +1 heisst hier: alle Vorzeichen +1.
- AG2: M_eff aus NETZ-NICHTLINEAR-1 (nn.py, unveraendert importiert), Lesart G1, Netz s2 Arm P beim ersten Zug.
  Unimodulare Bedingung als lineare Zwangsbedingung an die Geschwindigkeiten a' = dl/l0 / dt:
  - global: d(Summe der Tetraedervolumen)/dt = 0, eine Bedingung;
  - lokal: d(V_v)/dt = 0 je Ecke, V_v = Summe der anliegenden Tetraedervolumen / 4 (baryzentrisch), 128 Bedingungen.
  Gezaehlt wird die Zahl negativer Eigenwerte von M_eff eingeschraenkt auf den Kern der Bedingungen.
  Das ist meine Lesart von "4-Volumen festhalten (Lagrange)"; das 4-Volumen der Lage zwischen zwei Zeitschnitten ist bei
  festem Takt das Zeitintegral des 3-Volumens. Eine andere Lesart (4-Simplex-Volumen am Zug) ist im Projektcode nicht
  frei, weil die neue Kante aus der flachen Doppelpyramide folgt.
- AG3: PPN-Faktor P = (2 + 2 gamma - beta)/3 mit gamma aus LICHT-ABLENKUNG-V und beta aus BETA-NETZ-V [P].
- AG4: Lense-Thirring-Laufzeit Delta t = 4 G J/(c^4 b) je Seite [L], Phase Delta phi = E Delta t / hbar.
- Teil C: lokale Eichinvarianz und Kontinuitaet numerisch auf einem Zufallsgraphen pruefen, mit den Formeln woertlich aus
  THEORIE-ABC.md und mit meiner Herleitung.

## Schreibtisch vorab [M]

1. **AG2, Interlacing:** Schraenkt man eine quadratische Form auf eine Hyperebene ein, sinkt die Zahl negativer
   Eigenwerte um hoechstens 1. Mit einer globalen Bedingung kann M_eff von 130 also nur auf 130 oder 129 fallen, nie auf
   128. Das Kartenkriterium "faellt auf 128" kann mit der globalen Lesart nicht eintreten. Offen ist nur die lokale
   Lesart (128 Bedingungen, Abnahme um bis zu 128 moeglich).
2. **AG2, Skript:** unimodular_pachner.py hat eine Variable und eine Gleichungs-Bedingung, also keinen Freiheitsgrad; die
   "Minimierung" ist leer. Das Ziel sqrt(5/96) = 0,228 ist nicht das Volumen des regulaeren 4-Simplex (sqrt(5)/96 =
   0,0233). Erwartung: Der Optimierer meldet Misserfolg oder eine verletzte Bedingung.
3. **AG1 und AG5:** Gleichfoermige Richtungsphasen eta_mu (wie in dirac_gitter_gpu.py, eta = 1, -1, i, -i) sind eine
   reine Eichung: Es gibt k0 und phi mit eta_mu = exp(i (k0.d_mu + phi)), weil die Matrix (d_mu, 1) invertierbar ist.
   Hier k0 = (pi/4, 0, -pi/2), phi = pi/4. Auf dem Torus mit geradem L ist das Spektrum exakt das des schlichten
   Diamanten. dirac_gitter_gpu.py ruft ausserdem parser.parse_argument() auf und bricht deshalb ab.
4. **AG1, Kodimension:** Ohne Spin-Bahn ist Delta(k) bei reellen Vorzeichen ein komplexer Block; det Delta = 0 sind zwei
   reelle Bedingungen im 3D-k-Raum, generisch also Linien. Isolierte Punkte brauchen Feinabstimmung oder Zusatzsymmetrie.
   Erwartung: kein Flussmuster gibt genau 3 isolierte Knoten; die meisten geben Linien oder sind gelueckt, einige
   Flachbaender.
5. **E-Teil (1D, 2D, 3D):** 1D-Kette mit gleichen Spruengen: ein Knoten bei k = pi, aber nur am kritischen Punkt (SSH).
   2D-Wabe: K und K'. 3D-Diamant ohne Spin-Bahn: Linien X-W. Mit Spin-Bahn (Fu/Kane/Mele [L], DIAMANT-NULLSTELLEN-1 [P]):
   genau die drei X-Punkte, aber nur am isotropen Punkt (alle vier Bindungen gleich). Erwartung: Die Folge 1, 2, 3 stimmt
   nur, wenn man in 3D Spin-Bahn hinzunimmt und in 1D und 3D am kritischen Punkt sitzt.
6. **Higgs-Skript:** M_i an den X-Punkten sind |t0 + t1 - t2 - t3|, |t0 - t1 + t2 - t3|, |t0 - t1 - t2 + t3|. Drei
   lineare Kombinationen von vier freien Spruengen: jede Massenfolge ist einstellbar, also keine Vorhersage. Ohne
   Spin-Bahn bleiben ausserdem Knotenlinien, das kleinste |E| ueber die Zone ist dann 0 statt M_1.
7. **AG3:** gamma = 1,000 (Fernfeld, Laengen/Takt 0,999 bis 1,001), beta = 1,00 bis 1,02 (Variante A) bzw. 0,95 +- 0,05
   (Variante B). P = 0,993 bis 1,000 (A), 1,017 +- 0,017 (B). Erwartung: innerhalb 0,02 von 1 fuer A, Grenzfall fuer B.
8. **gravity_nearfield_collapse.py:** Ein zusaetzliches Kraftglied alpha Rs^2/r^3 gibt die Drehung
   Delta phi = 2 pi alpha Rs/p in erster Ordnung, ART 3 pi Rs/p. alpha = 1,5 ist also genau der ART-Wert, eingesetzt.
   Der "Horizont" c^2 = 0 liegt bei Rs/r = (sqrt 7 - 1)/3 = 0,549, also r = 1,82 Rs, nicht bei Rs.
9. **AG4:** Fuer ein Elektron (J = hbar/2): Delta phi = 2 G E/(c^4 b) = 2 (E/E_P)(l_P/b). Mit E = 1 MeV und b = 1 fm etwa
   3e-42 rad. Beste Phasenempfindlichkeit grob 1e-10 rad oder schlechter: Abstand etwa 32 Groessenordnungen. Die Formel
   im Skript (c^5 b^2) hat die Einheit s/m^2, ist also nicht dimensionslos.
10. **Teil C:** Die eichinvariante Kombination ist phi_j^* exp(i q A_ij) phi_i. Der Strom in THEORIE-ABC.md,
    Im(phi_i^* exp(+i q A_ij) phi_j), ist damit nicht eichinvariant (Vorzeichen der Phase). Erwartung: numerisch
    nicht eichinvariant; mit e^{-i q A_ij} korrekt; die Kontinuitaet gilt dann bis auf ein Vorzeichen-Konventionsthema.
11. **ribbon_frustration.py:** Literaturskalierung [L]: Biegung ~ t^3 w k^2, Dehnung ~ t w^5 k^4, Verhaeltnis
    (w^2 k / t)^2. Das Skript nimmt w^2/t ohne k als Kriterium, alle Zahlen sind gesetzt, kein Netzbezug.

## Eigene Erwartungen (Wahrscheinlichkeit, vor der Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| V1 | AG1: keines der 64 Flussmuster hat genau 3 isolierte Knoten | 85 % |
| V2 | AG2 global: s2 nach dem Ausnahmezug 129 oder 130 (Interlacing), Abstand zum Start bleibt | 90 % |
| V3 | AG2 lokal: die Differenz "nach Ausnahmezug minus Start" bleibt > 0 | 65 % |
| V4 | AG3: P innerhalb 0,02 von 1 (Variante A) | 90 % |
| V5 | AG4: Abstand > 30 Groessenordnungen | 95 % |
| V6 | AG5: Fadenend-Spektrum hat Linien, keine isolierten Kegel; eta-Phasen = Eichung (Spektren gleich auf 1e-12) | 95 % |
| V7 | AG6: Platzhalter | 95 % |
| V8 | Teil C: woertliche Stromformel nicht eichinvariant, korrigierte erfuellt die Kontinuitaet auf 1e-10 | 80 % |
