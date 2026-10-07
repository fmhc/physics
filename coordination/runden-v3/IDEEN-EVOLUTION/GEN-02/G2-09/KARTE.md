# G2-09 Ist der drehende Hintergrund selbst stabil? (Stoerquelle fuer WM-1)

- Quelle: coordination/ideation-arxiv-20260929/KARTEN.md, K-4, nur ins Kartenformat gebracht (keine neue Idee).
  Bisher ungetestet.

- **Hypothese [H] (K-4):** Ein drehender Q-Ball mit m = 1 ist in unserem U (U = S - S^2 + S^3/2) nur oberhalb einer
  Mindestladung gegen Aufspaltung stabil. Darunter koennte ein Wachstum im Nachbarkanal (WM-1) aus der Instabilitaet
  des Hintergrunds stammen statt aus Mischung.

- **Papier vorab [S]:**
  - Die Ladung faellt mit omega^2 (m = 1: Q 157,1 bei 0,59 und 138,8 bei 0,60, RUNDE-07 RING-T). "Oberhalb einer
    Mindestladung stabil" heisst bei uns "stabil unterhalb einer Schwelle omega_c^2".
  - Vorhandene 2D-Rechnungen mit demselben Verfahren (Stoerung l = 1 bis 6, Amplitude 0,01):
    - m = 1 (RUNDE-07 RING-T, T = 3000): 0,55 / 0,575 / 0,59 ruhig; 0,60 teilt bei t = 1045 (gamma 0,0041);
      0,625 bei 75 (0,0641); 0,65 bei 50 (0,0925); l_dom 2, Toechter mit Windung 0.
    - m = 2 (GEN-01 G1-03, T = 1200): 0,55 ruhig; 0,57 teilt bei 440 (0,0098); 0,65 bei 50 (0,0913); 0,70 bei 35
      (0,1179); l_dom 3 ab 0,63.
  - Die Kernfrage von K-4 fuer m = 1 ist in 2D damit schon beantwortet: Es gibt eine Mindestladung, die Schwelle
    liegt bei omega^2 0,59 bis 0,60. Vorhersagen an diesen Stellen sind vorab ableitbar und keine Messung.
  - WM-1 (farben-20260927/wm-1-mb-lauf/inputs/WM-1-VERTRAG-F3.md, A1.1, A1.5, Parameter): Hintergrund m = 1 in 3D
    (achsensymmetrisch, FM-2-Profil), omega = 0,87 (omega^2 = 0,7569), Q = 751, eingefroren, T = 300. Die Stabilitaet
    des Hintergrunds ist dort ausdruecklich nicht Gegenstand.
  - Nicht ableitbar ist nur:
    - was m = 1 und m = 2 in 2D bei omega^2 = 0,7569 (WM-1-Frequenz) innerhalb T = 300 tun
    - die Raten der Dichtemoden l = 2 und l = 3 getrennt (bisher nur die dominante Mode gefittet)
  - Schaetzung [S]: gamma(m = 1) steigt von 0,0641 (0,625) auf 0,0925 (0,65). Linear weiter waeren es bei 0,7569 etwa
    0,21, mit Abflachung 0,10 bis 0,20. Bei 0,65 gilt t_teilung * gamma = 4,6; mit gamma 0,1 bis 0,2 folgt
    t_teilung 23 bis 46, weit vor T = 300.

- **Kleiner Test:**
  - Code: Kopie von IDEEN-EVOLUTION/GEN-01/G1-03/teilung_schwelle.py, Unterbefehl "teilung" (Schiessen, Gitter
    L = 38,4, Stoerung, Gebietsanalyse und gamma-Fit wie dort). Neu nur: Laufliste, T = 300 (wie WM-1), getrennter
    Ratenfit fuer l = 2 und l = 3 (gleiches Fenster wie der l_dom-Fit: 3 A_l(0) <= A_l <= 0,2, bis zur Teilung),
    fein mit halber Gitterweite und halbem Zeitschritt (dx 0,15, dt 0,025).
  - Drei Ladungen je Windung: omega^2 = 0,55 / 0,65 / 0,7569 (0,55 und 0,65 sind Wiederholungsstellen, 0,7569 ist
    die WM-1-Frequenz).
  - Hauptlauf grob (dx 0,3, dt 0,05, T = 300): m = 1 und m = 2 an allen drei Stellen.
  - Fein (dx 0,15, dt 0,025): m = 1 bei 0,65 und 0,7569, m = 2 bei 0,7569.
  - Gegenprobe (getrennter Aufruf): m = 0 bei 0,55 und 0,7569, gleich gestoert, T = 300, grob.
  - Messung je Lauf: Teilung ja/nein, t_teilung, Zahl und Windung der Toechter, l_dom, gamma (l_dom), gamma_2 und
    gamma_3, Ladung Q.
  - Rechenort: .69, Spur p4000a oder p4000b, drei Aufrufe, je unter 10 min.

- **Vorhersage vorab:**
  - V1 (m = 1, Mindestladung): 0,55 teilt sich bis T = 300 nicht; 0,65 und 0,7569 teilen sich; 0,7569 teilt sich
    frueher als 0,65 und mit groesserem gamma. (0,55 und 0,65 sind aus RING-T ableitbar, neu ist nur 0,7569.)
  - V2 (WM-1-Fenster): m = 1 bei 0,7569 teilt sich vor t = 150 (halbes WM-1-Fenster), gamma (l_dom) in [0,09; 0,30].
  - V3 (Moden): An jeder teilenden m = 1-Stelle ist gamma_2 > gamma_3; alle Toechter tragen Windung 0.
  - V4 (m = 2, K-4-Kontrolle "m = 2 muss spalten"): teilt sich bei 0,65 und 0,7569; bei 0,55 nicht bis T = 300 (0,55
    und 0,65 aus G1-03 ableitbar).
  - **Scheitert, wenn** eines davon eintritt:
    - m = 1 teilt sich bei 0,55, oder teilt sich bei 0,7569 nicht
    - Teilung von m = 1 nicht monoton in omega^2, oder 0,7569 teilt nicht frueher als 0,65
    - m = 1 bei 0,7569: t_teilung >= 150 oder gamma ausserhalb [0,09; 0,30]
    - an einer teilenden m = 1-Stelle gamma_3 >= gamma_2, oder eine Tochter mit Windung ungleich 0
    - m = 2 teilt sich bei 0,65 oder 0,7569 nicht (dann scheitert die K-4-Kontrolle)
  - V1 an 0,55 und 0,65 sowie V4 an 0,55 und 0,65 pruefen nur Code und Reproduktion.

- **Gegenprobe (Effekt muss verschwinden):** m = 0 bei 0,55 und 0,7569, gleich gestoert: keine Teilung bis T = 300,
  kein gamma-Fit oder gamma < 0,005.

- **Plausibilitaetsschranke:**
  - Q_box(t) <= Q_box(0) (1 + 1e-4)
  - Ladung der Box auf 2e-3 relativ erhalten bis T (ohne Teilung) bzw. bis 0,5 t_teilung
  - J/Q am Start auf 1e-3 gleich m
  - Summe der Tochterladungen hoechstens 1,002 Q; Tochtergeschwindigkeiten unter 1; 0 <= gamma, gamma_2, gamma_3 <= 1
  - Profilprobe: S_max < 1 fuer alle geschossenen Profile; Schwanz (f < 1e-3 f_max) endet vor der Randschicht

- **Latten erwartet:**
  - L1 teilweise: 0,55 und 0,65 sind ableitbar (Reproduktion); scheitern koennen die Stellen bei 0,7569 und der
    Modenvergleich l = 2 gegen l = 3.
  - L2: m = 0 bei gleichem omega^2 und gleicher Box.
  - L3: halbe Gitterweite und halber Zeitschritt: gleicher Ausgang und gleiche Toechterzahl, gamma-Aenderung hoechstens
    ein Fuenftel.
  - L4 teilweise: Stabilitaetsschwellen der Wirbelsolitonen im kubisch-quintischen NLS [L, nicht nachgelesen];
    Wirbeltroepfchen (2609.32342) und drehende Bosonensterne (2609.06954) laut K-4. Unser U ist relativistisch, die
    NLS-Schwelle uebertraegt sich nicht zahlengleich.
  - L5 nein: Modellrechnung. Der Schluss auf WM-1 bleibt Hypothese: WM-1 ist 3D und eingefroren; ein 2D-Zerfall zeigt
    nicht, dass der 3D-Hintergrund bei omega = 0,87 zerfaellt.

- **Einfach gesagt:** Ein kreiselnder Q-Ball kann in Stuecke zerfallen, wenn er zu klein ist. In einem anderen Versuch
  (WM-1) sitzt so ein kreiselnder Ball neben einem leeren zweiten Feld, und man fragt, ob dort etwas waechst. Waechst
  etwas, koennte das auch daher kommen, dass der Ball selbst wackelt und zerfaellt. Wir pruefen deshalb in einer flachen
  Welt, ob ein kreiselnder Ball mit der WM-1-Frequenz in der WM-1-Laufzeit zerfaellt. Fuer groessere Baelle kennen wir
  die Antwort schon; neu ist nur der kleine Ball.

- Karte geschrieben: 2026-09-30 11:09:32 CEST

- Vorhersage geschrieben: 2026-09-30 11:10:06 CEST
