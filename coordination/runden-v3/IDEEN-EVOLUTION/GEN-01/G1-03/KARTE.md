# G1-03 Teilung eines drehenden Q-Balls (Windung m = 2): Gibt es eine kritische Groesse?

- **Hypothese [H]:** Ein drehender 2D-Q-Ball mit Windung m = 2 teilt sich in Tochterbaelle; die Teilung haengt an einer
  kritischen Groesse, wie bei Zellen.

- **Vorbefund (2D-Rechnung, r5_2d_a.py "teilung", T = 600, dx 0,3 und 0,2):**
  - m = 2 bei omega^2 = 0,65 (Q = 171) und 0,80 (Q = 111) teilt sich in 3 bzw. 4 Toechter, alle mit Windung 0,
    gamma = 0,091 bzw. 0,133.
  - m = 2 bei omega^2 = 0,55 (Q = 628) teilt sich bis T = 600 nicht.
  - Offen ist, ob es zwischen 0,55 und 0,65 eine echte Schwelle gibt oder der grosse Ball nur langsamer ist.

- **Papier vorab [S]:**
  - Die Gerade gamma^2 gegen omega^2 durch 0,65 und 0,80 hat ihren Nullpunkt bei 0,515.
  - Dann muesste der Ball bei 0,55 mit gamma etwa 0,046 in unter 100 Zeiteinheiten zerfallen; das tat er nicht.
  - Entweder faellt gamma zwischen 0,55 und 0,65 steil und stetig auf null (lineare Schwelle), oder gamma springt an einer
    Grenze (endliche Rate bis zur Grenze). Der Test unterscheidet beides.

- **Kleiner Test:**
  - Code: Kopie von r5_2d_a.py, Unterbefehl "teilung". Geaendert sind nur die Laufliste und T = 1200 (doppelt so lang wie
    zuvor), dazu die Kennzahlen dieser Karte und die Plausibilitaetsschranke. Stoerung wie zuvor: Moden l = 1 bis 6,
    Amplitude 0,01.
  - Hauptlauf: m = 2 bei omega^2 = 0,55 / 0,57 / 0,59 / 0,61 / 0,63 / 0,65 / 0,70.
  - Gegenprobe (eigener Lauf): m = 0 bei omega^2 = 0,59, gleich gestoert.
  - Grob/fein: dx 0,3, dt 0,05 fuer alle; fein dx 0,2, dt 0,025 (halber Zeitschritt) fuer 0,57 / 0,59 / 0,61 / 0,63.
  - Messung je Lauf: Teilung ja/nein, t_teilung, Zahl und Windung der Toechter, dominante Mode l_dom, Wachstumsrate
    gamma (Fit wie zuvor), Ladung Q des Profils (Groesse).
  - Rechenort: .69, GPU-Spur p4000a oder p4000b, drei Aufrufe (Hauptlauf grob, Gegenprobe, fein), je unter 10 min.

- **Vorhersage vorab:**
  - V1 Schwelle: Es gibt genau eine Grenze omega_c^2 zwischen 0,55 und 0,65. Alle m = 2-Laeufe oberhalb teilen sich bis
    T = 1200, alle darunter nicht; auch 0,55 teilt sich bis 1200 nicht.
  - V2 stetig: gamma steigt ueber die teilenden Laeufe monoton mit omega^2. Die Gerade gamma^2 gegen omega^2 durch die
    zwei tiefsten teilenden Laeufe hat ihren Nullpunkt hoechstens 0,03 unter der hoechsten nicht teilenden Stelle.
  - V3 (Wiederholung): Alle Toechter tragen Windung 0.
  - **Scheitert, wenn** eines davon eintritt:
    - 0,55 teilt sich bis T = 1200 (dann keine Schwelle im Intervall, nur ein langsamerer Zerfall)
    - die Teilung ist nicht monoton in omega^2 (ein Lauf teilt sich, ein hoeherer nicht)
    - der gamma^2-Nullpunkt liegt mehr als 0,03 unter der hoechsten nicht teilenden Stelle (Sprung statt stetiger
      Schwelle), oder gamma ist nicht monoton
    - eine Tochter traegt Windung ungleich 0

- **Gegenprobe (Effekt muss verschwinden):** m = 0 bei omega^2 = 0,59 teilt sich bis T = 1200 nicht, und keine
  azimutale Mode waechst messbar (kein gamma-Fit, oder gamma unter 0,005).

- **Plausibilitaetsschranke:**
  - Die Ladung der Box waechst nie: Q_box(t) <= Q_box(0) (1 + 1e-4), weil der Rand nur schluckt
  - Ladung der Box erhalten auf 2e-3 relativ: ohne Teilung bis T, mit Teilung bis 0,5 t_teilung (vor dem Aufbrechen)
  - J/Q am Start auf 1e-3 gleich m
  - Summe der Tochterladungen hoechstens 1,002 Q
  - Tochtergeschwindigkeiten unter 1
  - 0 <= gamma <= 1

- **Latten erwartet:**
  - L1 ja: Schwelle, Stetigkeit und Toechter koennen je scheitern.
  - L2: m = 0.
  - L3: grob gegen fein. Gleicher Ausgang und gleiche Toechterzahl; gamma-Aenderung hoechstens ein Fuenftel von gamma.
  - L4 teilweise: Die Instabilitaet drehender Q-Baelle ist Literatur [L, aus dem Gedaechtnis]; die Lage der Schwelle in
    diesem Potential kenne ich nicht.
  - L5 nein: Modellaussage.

- **Einfach gesagt:** Ein kreiselnder Q-Ball kann in Stuecke zerfallen. Frueher zerfielen die kleinen, der grosse nicht.
  Jetzt suchen wir die Groesse, an der das umschlaegt, und pruefen, ob der Zerfall zur Grenze hin sanft langsamer wird
  oder ploetzlich aufhoert. Zerfaellt auch der grosse Ball, wenn man nur laenger wartet, gibt es keine kritische Groesse,
  und die Idee faellt.

- Vorhersage geschrieben: 2026-09-30 07:58:24 CEST
