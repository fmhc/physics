# G2-10 Stille Leiter in zwei Dimensionen: gleiche Wandphase, doppelter Sprossenabstand, eine Viertelphase versetzt

- Hypothese: Die stillen Atmungsstellen (eingebettete Eigenwerte, Breite null) des radialen Q-Balls mit
  U = S - S^2 + S^3/2 gibt es auch in zwei Raumdimensionen; weil der Duennwandradius wie (d - 1) skaliert und die innere
  stehende Welle als Bessel-Funktion eine Viertelphase frueher an der Wand ankommt, liegen sie bei
  1/(omega*^2 - 1/2) = 2 b (n + theta - 1/4) mit denselben Wandgroessen b und theta wie in 3D [H].

- Papier vorab [S] (Duennwandbild, von Hand; beta = 0,5, eps = omega^2 - 1/2):
  - Duennwandradius aus Wandspannung gegen Druck: R_d = (d - 1)/(4 sqrt(beta) eps). In 3D 1/(sqrt(2) eps), in 2D
    1/(2 sqrt(2) eps), also halb so gross bei gleichem eps. Die mittlere Kruemmung (d - 1)/R = 4 sqrt(beta) eps ist in
    beiden Dimensionen gleich.
  - Das Wandproblem ist in fuehrender Ordnung eben und haengt nicht von d ab: derselbe eine gebundene Zustand des
    geschlossenen Kanals im Rosen-Morse-Topf der Wand, dieselbe Wandphase und Niveauverschiebung. Aus der 3D-Leiter
    bekannt (Anpassung an n = 2, 3, 4): theta(eps) = 0,664 + 0,209 eps + 0,576 eps^2; c = Re rho* - omega* = 0,826 + 0,24 eps.
  - Innenwelle: k_c^2 = omega^2 + rho^2 - 1,5 + sqrt(4 omega^2 rho^2 + 1). Die bei r = 0 regulaere Loesung geht in d
    Dimensionen wie sin(k r + (3 - d) pi/4) (3D: sin k r; 2D: sqrt(r) J_0(k r) ~ cos(k r - pi/4)). Stille Bedingung:
    k_c R_d = pi (n + theta - (3 - d)/4).
  - Probe in 3D (n = 3, gemessen omega*^2 = 0,631449): Die Formel gibt Psi/pi = 3,7007 gegen 3,7014 aus den Messwerten.
  - 2D, geloest mit rho = omega + c(eps):

    | n | eps | omega*^2 in 2D (Vorhersage) | Spanne | 3D zum Vergleich (gemessen) |
    |---|---|---|---|---|
    | 1 | ~0,171 | ~0,671 | +- 0,02 (dicke Wand, nur qualitativ) | 0,797677 |
    | 2 | 0,0971 | 0,5971 | +- 0,003 | 0,685129 |
    | 3 | 0,0674 | 0,5674 | +- 0,0015 | 0,631449 |
    | 4 | 0,0515 | 0,5515 | +- 0,001 | 0,601422 |
    | 5 | 0,0417 | 0,5417 | +- 0,001 | 0,582417 |

  - Schritte in 1/eps (2D, Vorhersage): 4,54 / 4,57 / 4,59 fuer n = 2 -> 3 -> 4 -> 5; 3D gemessen 2,21 / 2,25 / 2,27.
    Das Verhaeltnis 2,0 folgt allein aus R ~ (d - 1).
  - Innenbarriere: Eine Stelle braucht B = dp(S0) - (omega - Re rho)^2 > 0 in der Ballmitte, dp(S) = 1 - 4S + 4,5 S^2; bei
    (omega - rho)^2 ~ 0,72 heisst das S0 > 0,81. In 2D ist S0 bei gleichem omega kleiner als in 3D (weniger "Reibung" im
    Profil); die Leiter endet oben an einer 2D-Barrierengrenze x_B(2D) unterhalb der 3D-Grenze 0,878. Die dicke Stelle
    n = 1 kann deshalb fehlen.

- Kleiner Test:
  - Code-Basis: Kopie von RUNDE-07/bic2/bic2_v2.py (Profil und Stoerung in dim Dimensionen, nu = l + (dim - 1)/2, Parameter
    beta; Polsuche und Breitenraster der 3D-Leiter). Aufruf mit dim = 2, l = 0, beta = 0,5, Potential unveraendert. Neu
    nur eine Rasterschleife ueber omega^2 bei festem dim (unter 30 min), sonst wie die 3D-Leiterlaeufe: |Im rho| auf dem
    Raster, Minima mit der signierten Wurzel verfeinern.
  - Laeufe:
    - Zuerst, vor der Polsuche und in die Ausgabe geschrieben: x_B(2D) aus den 2D-Profilen allein = groesstes omega^2
      auf dem Raster mit dp(S0) > c(eps)^2, c(eps) = 0,826 + 0,24 eps (Niveau aus 3D), S0 = S(r = 0) des 2D-Profils.
      Kein Pol geht in x_B ein.
    - d = 2: Raster omega^2 = 0,535 bis 0,70, Schritt 0,002; um jedes Rasterminimum +- 0,002 mit Schritt 0,0002.
    - Gegenproben: d = 3 an n = 2 und 3; d = 1 auf 0,55 bis 0,70, Schritt 0,005.
  - Rechenort: .69 ueber kleintest.sh, Spur cpu oder cpu2 (radialer linearer Loeser, CPU-faehig); geschaetzt 5 bis 10 min,
    sonst Raster 0,004.
  - Messgroessen: Lagen der Breitenminima (Nulldurchgang der signierten Wurzel), |Im rho| am Minimum, Umlaufzahl falls der
    Code sie gibt, x_B(2D).

- Vorhersage vorab:
  - V1 (Kern): Die 2D-Leiter existiert: mindestens drei der vier Stellen n = 2 bis 5 liegen in den Spannen der Tabelle, jede
    mit Nulldurchgang der signierten Wurzel (dasselbe Kriterium wie bei der 3D-Leiter).
  - V2: Die Schritte in 1/eps zwischen benachbarten gefundenen Stellen mit n >= 3 liegen zwischen 3,9 und 5,2
    (doppelter 3D-Schritt +- 15 %).
  - V3: theta_2D := k_c R_2D/pi - n + 1/4 an den Stellen n = 3 bis 5 liegt bei 0,68 +- 0,05, also wie in 3D.
  - V4: Keine Stelle oberhalb x_B(2D). Liegt x_B(2D) unter 0,67, fehlt n = 1.
  - Wenn der Code Umlaufzahlen gibt: Sie wechseln von Stelle zu Stelle das Vorzeichen.
  - **Scheitert, wenn** eines davon eintritt:
    - auf 0,535 bis 0,70 keine Stelle mit Nulldurchgang
    - zwei oder mehr der vier Lagen n = 2 bis 5 ausserhalb der Spannen
    - ein Schritt nach V2 ausserhalb 3,9 bis 5,2
    - eine Stelle oberhalb x_B(2D)

- Gegenprobe:
  - d = 1: keine Stelle auf 0,55 bis 0,70 (ohne Innenbarriere keine Leiter; bekannt: keine Stelle auf 0,55 bis 0,88).
  - d = 3: n = 2 und 3 an den bekannten Lagen 0,685129 und 0,631449 auf 2e-4 (Code und Raster richtig).

- Plausibilitaetsschranke:
  - Im rho <= 0 an allen Polen (keine anwachsende Mode); Re rho im offenen Fenster 1 - omega < Re rho < 1 + omega
  - Hintergrund: 2D-Virial omega^2 Int f^2 = Int U(f^2) (in d = 2 faellt der Gradiententerm heraus) auf 1e-6 relativ
  - Q(omega) im gerechneten Bereich stetig und monoton (sonst ist ein Profil falsch geschossen)

- Latten erwartet:
  - L1 ja: Existenz, Schritt, Versatz und Barrierengrenze koennen je einzeln scheitern.
  - L2: d = 1 (keine Stelle), d = 3 (Reproduktion).
  - L3: halber Radialschritt und groesserer Aussenrand; Lagen auf 1e-4.
  - L4 teilweise: Duennwandradius R ~ (d - 1)/eps [A fuer d = 3: Kovtun, Nugaev, Shkerin 2018, arXiv:1805.03518, Gl. (46),
    laut RUNDE-09/MODELL-DUENNWAND.md; d = 2 eigene Umrechnung]. Eingebettete Atmungseigenwerte zweidimensionaler Q-Baelle
    kenne ich nicht [L?].
  - L5: nein (Modellrechnung); ein Bezug zu duennen Schichten und Monolagen waere nur Hypothese.

- Einfach gesagt: Ein grosser Q-Ball ist wie ein Tropfen mit duenner Haut, in der eine Schwingung gefangen sitzt. Bei
  bestimmten Groessen kann sie nicht nach aussen entweichen; in drei Dimensionen gibt es davon eine ganze Leiter, die
  unsere Formel gut beschreibt. Fuer eine flache, zweidimensionale Welt sagt dieselbe Formel eine eigene Leiter voraus:
  gleiche Haut, aber doppelte Sprossenabstaende und etwas verschoben, weil sich Wellen in einer Scheibe anders ausbreiten
  als in einer Kugel. Findet der Rechner in 2D keine stillen Stellen oder liegen sie woanders, stimmt unser Bild der Haut
  nicht.

- Karte geschrieben: 2026-09-30 10:58:14 CEST

- Vorhersage geschrieben: 2026-09-30 11:06:31 CEST
