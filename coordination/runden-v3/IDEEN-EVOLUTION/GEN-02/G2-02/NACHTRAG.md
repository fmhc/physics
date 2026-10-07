# G2-02 Nachtrag (nach dem Stempel 11:16:14, vor jedem echten Lauf)

- 2026-09-30 11:28:26 CEST, T-1:
  - Code: r5d_bilanz.py, Kopie von RUNDE-05/r5d/r5d.py; neu nur der Abschnitt "G2-02" (Unterbefehle bilanz = 8
    masselose Laeufe, bilanz_gegen = 3 Gegenproben), zwei TESTS-Eintraege und die Option --faktor. Dynamik und
    Anfangsfelder wie altern (gleiche Laeufe, gleiche Reihenfolge). Neuer Code etwa 15 min.
  - Vor jedem Lauf festgelegt, wo die Karte offen ist:
    - Geschluckt = Gesamtwert(0) - Gesamtwert(t) im ganzen Gitter. Die Buchfuehrungspruefung (Fenster + Schale +
      Schwammbereich = gesamt) prueft damit nur, dass die Masken das Gitter lueckenlos teilen; sie ist keine
      unabhaengige Bilanz. Unabhaengig sind die Erhaltung bis t = 90 und "der Schwamm schluckt nur".
    - R_EQ als Verhaeltnis zweier Geradensteigungen (E_Fenster, Q_Fenster) auf [100, 400] (V1) bzw. [100, 200] (V3);
      omega(t) = Im(psi conj(psi_t))/|psi|^2 am Maximum von |psi|^2, gemittelt im selben Zeitfenster.
    - V2 und V3 "Maximum bei |x| <= 0,5" und |Q_neg| <= 1e-3 Q(0) gelten fuer alle Messzeiten bis T bzw. bis 200.
    - V4 vergleicht mit den Q_ball_T-Werten aus RUNDE-05/r5d/lauf-69/altern/r5d_altern_ergebnis.json (grob und fein),
      gebunden nur im Hauptlauf auf einer P4000 (R5-D lief dort).
    - Diagnose (nicht bindend): t_Ereignis = erste Zeit mit |x_max| > 0,5 oder Q_neg < -1e-3 Q(0); dazu S_max,
      mittleres |x|, Q_psi und Q_chi im Fenster, Schale und geschluckt bei T.
  - Hinweise vor dem Lauf, Karte unveraendert:
    - "E_ges steigt nie um mehr als 1e-6 E(0)" kann an den O(dt^2)-Schwankungen des Verlet-Verfahrens reissen
      (eigene Schaetzung: bis etwa 3e-5 relativ, wenn eine innere Mode angeregt ist). Reisst sie, sagt die Karte
      "nicht entscheidbar". Der Code gibt zusaetzlich den Anstieg ueber einem gleitenden Mittel (20 Messpunkte) aus,
      nur als Diagnose.
    - V2-Schale bei 0,6: Strahlung, die in den letzten etwa 70 Zeiteinheiten ausgesandt wurde, ist bei T noch in der
      Schale; mit der R5-D-Rate 1,85e-3 sind das etwa 4 % von Q(0), knapp unter der 5-%-Grenze.
  - Formprobe (lokal, CPU, 1 Faden, nice 19, Zeitfaktor 0,05; 11:22:12 bis 11:22:23, nach einer Berichtigung erneut
    11:25:15 bis 11:25:24): beide Unterbefehle rc 0. Berichtigt wurde nur, dass die Pruefung V1 bis V4 auch in der
    Formprobe durchlaeuft (vorher bei Zeitfaktor != 1 uebersprungen). Keine Aussage aus der Formprobe.
  - Die Karte kann scheitern (E/Q, Ort, negative Ladung, Fruehphase bei 0,51 und 0,55); kein "L1 schwach". V3s
    Zeitpunkt ist schwach, weil er aus dem R5-D-Lesebefund folgt (steht so in der Karte).

- 2026-09-30 11:30:37 CEST, Leitung (vor jedem echten Lauf, ohne Ergebnis): Die Karte bleibt unveraendert, auch die Energieschranke 1e-6.
  - Reisst sie, lautet der Ausgang "nicht entscheidbar", ohne Lockerung.
  - V3 ist schwach, weil sie aus den R5-D-Daten ableitbar ist; das steht in der Karte und zaehlt nicht als eigener Treffer.
