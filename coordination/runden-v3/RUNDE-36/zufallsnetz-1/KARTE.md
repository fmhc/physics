# ZUFALLSNETZ-1: Ist ein ungeordnetes Tetraedernetz ohne Feinabstimmung richtungsfrei? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 22:51:10 CEST (date), vor jeder Rechnung.
- **Anlass:** Finn ~22:47 "Ideate Mal drumrum ... geometrische Grundformen"; Idee A4 aus IDEEN-EVOLUTION/GEN-03.md
  (Vorschlag 1 der Leitung).
- **Vorlauf:**
  - NETZ-C-1: Geordnete Netze (fcc, Pyrochlor, Diamant, srs) haben richtungsabhaengige Wellen und Doppelbrechung.
  - Gegenleser B1: fcc wird nur bei abgestimmter Winkelfeder (k_theta = 1/18) isotrop.
  - Unvermeidlich ist allein c_laengs ungleich c_quer.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Netz:** Poisson-Punkte in einem periodischen Wuerfel, Delaunay-Tetraeder, Staebe auf allen Delaunay-Kanten,
  Ruhelaenge = Kantenlaenge (spannungsfrei).
  - Mittlerer Grad ~ 15,54 (2 + 48 pi^2/35) [L], weit ueber der Maxwell-Grenze 6, also steif.
- **Affine Naeherung** [M]: Zentralfedern geben C_ijkl = (1/V) sum k l^2 n_i n_j n_k n_l. Fuer eine richtungsfreie
  Kantenverteilung ist das isotrop mit Cauchy-Beziehung lambda = mu, also c_l/c_q = sqrt 3 = 1,732.
- **Nichtaffine Relaxation** [L: ungeordnete Federnetze]: Die Knoten weichen der affinen Verformung aus. Das senkt den
  Schermodul staerker als den Kompressionsmodul, also wird c_l/c_q groesser als sqrt 3.
- **Richtungsfreiheit** [H]: Ein endliches Zufallsnetz ist nur im Mittel isotrop. Seine Restanisotropie (Richtungs-
  schwankung der Querwelle, Doppelbrechung) sollte wie N^(-1/2) fallen. Isotropie ohne Abstimmung, wie bei Kausalmengen
  [L: Bombelli/Henson/Sorkin].

## Test (Code-Agent)

- **Netze:** N = 4000, 16000 und 64000 Punkte, je zwei Saaten. Federn k = 1 (Hauptfall), Variante k = 1/l (gleicher Stab
  pro Querschnitt).
- **Elastizitaetstensor** aus sechs unabhaengigen Verzerrungen des periodischen Wuerfels:
  - affiner Anteil plus nichtaffine Relaxation (lineares Gleichungssystem, duenn besetzt, mit Vorkonditionierer)
  - Konvergenz offenlegen
- **Christoffel-Geschwindigkeiten** auf mindestens 400 Richtungen. Gemessen:
  - Laengs- und Quergeschwindigkeiten
  - Richtungsschwankung je Ast (max/min - 1)
  - groesste relative Aufspaltung der beiden Querwellen (Doppelbrechung)
  - c_l/c_q
  - Verhaeltnis G/G_affin
- **Gegenprobe:** dasselbe Werkzeug auf dem fcc-Netz (NETZ-C-1-Tabelle) muss dessen Werte treffen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Z0 | Kontrolle: fcc-Gegenprobe trifft NETZ-C-1 auf 1e-6; mittlerer Grad des Delaunay-Netzes 15,5 +- 0,1; affiner Tensor erfuellt C12 = C44 auf 1 % | 85 % |
| Z1 | N = 64000, nach Relaxation: Richtungsschwankung der Querwelle < 3 % und groesste Doppelbrechung < 3 % (beide Saaten) | 70 % |
| Z2 | Die Richtungsschwankung faellt mit N wie N^(-p), p zwischen 0,35 und 0,65 (Mittel ueber Saaten, drei Groessen) | 60 % |
| Z3 | c_l/c_q liegt zwischen 1,75 und 2,2 (k = 1, N = 64000) | 65 % |
| Z4 | Nichtaffine Schererweichung G/G_affin zwischen 0,5 und 0,9 (k = 1) | 60 % |

**Bedeutung (vorab):**
- Z1 und Z2 treffen ein: Ein ungeordnetes Tetraedernetz ist ohne Feinabstimmung richtungsfrei. Es gibt eine
  Quergeschwindigkeit fuer beide Polarisationen, in alle Richtungen, bis auf ein Rauschen, das mit der Groesse
  verschwindet.
  - Fuer Finns Bild ist das der natuerliche Weg zu einer einzigen "Lichtgeschwindigkeit" der Querwellen.
  - Uebrig bleiben die Laengswelle (Z3) und das bevorzugte Ruhesystem des Netzes.
- Z1 verfehlt: Zufallsnetze behalten eine merkliche Restanisotropie; dann ihre Groessenabhaengigkeit genau beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (nicht cpu, cpu2, cpu5, cpu6, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
