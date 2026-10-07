# REGGE-SCHAUM-1: Traegt ein zufaelliges Tetraedernetz in Regges Laengen-Bild Newtons Gesetz, und mit welchem G? (Runde 36)

- Leitung claude-primary, rechnet selbst. Karte und Vorhersagen geschrieben ab 2026-10-04 02:09:50 CEST (date), vor jeder
  Rechnung.
- **Anlass:**
  - Finn ~02:00: "Rechne weiter". Alle drei Agentenplaetze waren belegt (REGEL-1, DREIECK-LINSE-1, Gegenleser der
    Anschauungsseite).
  - REGGE-RAND-1 und NEWTON-NACHRECHNUNG: Auf dem regelmaessigen Kuhn-Gitter ist der lineare Eckenoperator genau -8 mal
    7-Punkt-Laplace, also G ohne Umnormierung.
  - ZUFALLSNETZ-1: Ein Poisson-Delaunay-Netz ist fast richtungsfrei. Offen ist, ob Regges Regel auf so einem Schaum dasselbe
    G gibt.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Ansatz** wie REGGE-RAND-1: l_e = l0_e psi_mitte^2 mit psi_mitte = (psi_a + psi_b)/2. Linear: delta l_e = l0_e (delta
  psi_a + delta psi_b).
- **Operator:** A_v = sum_{e an v} l_e eps_e. Linear ist L = B^T J B mit B_{e,a} = l0_e (a Ende von e) und
  J_{ef} = d eps_e/d l_f = -sum_t d theta_{e,t}/d l_f.
  - J ist die Hesse-Matrix der Regge-Wirkung in den Laengen, also symmetrisch; damit ist auch L symmetrisch [M].
- **Exakt vorab [M]:**
  - L 1 = 0 (gleichmaessige Streckung).
  - L x_i = 0 auf inneren Zeilen: Ein linearer konformer Faktor ist in erster Ordnung eine reine Verschiebung der Ecken im
    flachen Raum; die Fehlwinkel bleiben 0.
  - Schlaefli je Tetraeder: sum_e l_e d theta_e = 0.
- **Folge [M]:** Wegen L x = 0 braucht die Homogenisierung keinen Korrektor. Der wirksame Koeffizient ist
  K = (1/Vol) sum_{v<w} (-L_vw) (x_w - x_v)(x_w - x_v)^T.
  - Fuer q = x^2 gilt (L q)_v = sum_w L_vw (x_w - x_v)^2. Der volumengewichtete Mittelwert von (L x^2)_v/(-16 V_v) ist
    also K_xx/8.
  - Newton auf dem Gitter gibt dann delta psi = G M/(2 kappa r) mit kappa = K/8. Die Vorhersagen RS1 und RS2 messen damit
    dieselbe Zahl; RS2 prueft die Homogenisierung im endlichen Netz.
- **Offen** (der eigentliche Test): Ist kappa = 1 fuer jedes flache Netz (eine Summenregel), oder haengt G von der
  Netzgeometrie ab?
  - Fuer Kuhn ist kappa = 1 bekannt.
  - Argument fuer 1 [H]: Der linearisierte Regge-Fluss ist eine Randgroesse (Schlaefli); ein statistisch gleichfoermiges
    Netz sollte im Mittel den Kontinuumsrand treffen.
  - Argument dagegen: Der Ansatz psi_mitte = Mittel der Enden weicht auf schiefen Kanten von der wahren Laenge ab
    (-l0 (e.H.e)/6), und zwar in derselben Ordnung wie das Kruemmungssignal.

## Test (Leitung selbst, .69, Spur cpu5)

- **Drei Netze in einer Kugel mit Radius R0 = 20, Dichte 1:**
  - **K:** Kuhn-Gitter (Tetraeder ganz in der Kugel), Kontrolle.
  - **J:** Delaunay eines verwackelten Wuerfelgitters (Wackelbreite 0,25), Gegensweep.
  - **P:** Delaunay von Poisson-Punkten, Saat 1 und 2.
- **Ableitungen** d theta/d l je Tetraeder per komplexem Schritt (h = 1e-20) ueber die Einbettung aus den sechs Laengen.
- **Messungen:**
  - Kontrollen RS0.
  - **Quadrattest:** (L x_i^2)_v/(-16 V_v), V_v = Summe der anliegenden Tetraedervolumen/4; Mittel, Streuung, Quantile
    ueber innere Ecken.
  - Der Tensor K direkt aus L, ueber innere Paare mit r < 0,7 R0.
  - **Newton:** Punktmasse an der Ecke naechst dem Ursprung (L delta psi = 16 pi an dieser Ecke, G M = 1). Rand-Ecken
    Dirichlet 1/(2 r_v). f_v = 2 r_v delta psi_v; Schalen der Breite 1; Ausgleich f = a + b r ueber 4 <= r <= 14
    (a = 1/kappa).
  - Kleinste Eigenwerte des inneren Blocks L_II (Verschiebung -0,5).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RS0 | Kontrollen. (a) Schlaefli je Tetraeder <= 1e-10 relativ. (b) L symmetrisch <= 1e-10 relativ. (c) L 1 und L x_i auf inneren Zeilen <= 1e-9 relativ. (d) Netz K: innere Schablone = -8 mal 7-Punkt-Laplace (<= 1e-9) und Newton-Ausgleich a = 1 +- 0,01 | 85 % |
| RS1 | Netz P (beide Saaten): volumengewichtetes Mittel von (L x_i^2)/(-16 V) = 1 +- 0,03 fuer x, y, z; Einzelwerte streuen stark (Standardabweichung > 0,10) | 55 % |
| RS2 | Netz P: Newton-Ausgleich a = 1 +- 0,05, und a stimmt mit 1/(RS1-Mittel) auf 0,03 ueberein | 55 % |
| RS3 | Netz P: Die relative Standardabweichung von f in der Schale um r = 12 liegt unter 0,03 und ist kleiner als bei r = 5 | 55 % |
| RS4 | Netz P: L_II positiv definit (kleinster Eigenwert > 0) | 60 % |

**Bedeutung (vorab):**
- **RS1 und RS2 treffen ein:** Auch ein zufaelliger Schaum aus Tetraedern traegt in Regges Laengen-Bild Newtons Gesetz,
  mit demselben G wie das Wuerfelgitter. Die Netzunordnung erscheint nur als Rauschen nahe der Masse. Das stuetzt
  Weg A der Regel (REGEL.md) fuer Finns Schaumbild [H].
- **RS1 oder RS2 verfehlt (kappa ungleich 1):** G haengt von der Netzgeometrie ab. Das waere keine Widerlegung (G ist
  ein Parameter). Der einfache Mittelwert-Ansatz waere dann aber nicht netzunabhaengig, und eine Laengenvorschrift aus
  Kanten statt Ecken waere zu pruefen.
- **RS4 verfehlt:** Der konforme Modus wird auf dem Schaum instabil (Splitter-Tetraeder). Das waere ein ernstes Problem
  fuer das Laengen-Bild auf ungeordneten Netzen.

## Rahmen

- Leitung rechnet selbst. Nur auf der .69 ueber kleintest.sh, Spur cpu5; je Lauf <= 10 min.
- Die Karte steht vor dem Code; Schwellen und Urteilsregeln aendern sich danach nicht.
- Rauchlauf mit R0 = 8 erlaubt und offengelegt.
