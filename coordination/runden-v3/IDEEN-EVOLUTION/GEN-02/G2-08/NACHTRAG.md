# G2-08 Nachtrag (nach dem Stempel 11:16:14, vor jedem echten Lauf)

- 2026-09-30 11:28:42 CEST, T-1:
  - Code: prisma.py, umgebaute Kopie von RUNDE-01/qg1/qg1.py (Modell, Gitter, Schwamm, Verlet und Ladungs-/
    Killing-Dichte wie qg1). Neu: Stufe Phi(x) statt Gradient, Start bei x0 = -20 mit Lorentz-Boost, Anteile
    links/Stufe/rechts, --geraet cpu, --faktor nur fuer die Formprobe. Neuer Code etwa 20 min.
  - Abweichungen vom Kartentext, vor jedem Lauf festgelegt:
    - Profil und Schwellen aus dem geschlossenen 1D-Anker statt aus dem Schiessen. qg1 lauf-69 zeigte
      Schuss gegen Anker 1,2e-10; die Familie ist dieselbe. Die Schwellen rechnet der Code vor der Entwicklung
      (M2 = sqrt(B2) E(Q/sqrt(A2 B2)), ohne erste Ordnung) und schreibt sie oben in den Bericht; sie sind vorab
      ableitbar und keine Messung (so auch die Karte).
    - Laufzeit je Lauf T_run = min(2000, 80/v) statt "T bis 2000 bei v = 0,035, sonst 600": Kurz ueber der Schwelle
      bleibt nach Energiesatz nur v2 ~ 0,3 v (1,05 v_cl), dann reichen 600 bei omega^2 = 0,55 in A nicht; 80/v
      haelt zurueckgeworfene Baelle vor dem Schwamm bei |x| = 80 und laesst durchlaufende die Zone verlassen.
      Gemessen wird je Lauf bei T_run; der Stapel laeuft bis zum groessten T_run.
    - Ausgang nach der Mehrheit der Ladung links (x < -6), in der Stufe, rechts (x > +6). "reflektiert" verlangt
      zusaetzlich v2 < 0; sonst heisst der Ausgang "vor der Stufe" (Stufe nicht erreicht, zaehlt als falsch).
      Spalten: mehr als 10 % links und rechts. v2 = Steigung des Ladungsschwerpunkts der Ausgangsseite auf
      [0,75 T_run, T_run]; S_max-Schwankung im selben Fenster.
    - q_frei = 1 - (links + Stufe + rechts) = geschluckte Ladung. Die Plausibilitaet "Summe = 1 +- 1e-3" gilt damit
      per Bau; unabhaengig sind Ladung (1e-6) und Killing-Energie (1e-5) bis zum Schwammkontakt (Ladung in |x| > 80
      ueber 1e-6 Q0) und 0 <= Anteil <= 1.
    - Gegenprobe ohne Stufe: "v2 = v auf 1e-3" relativ gelesen.
    - L3: fein nur fuer die vier Schwellenlaeufe bei 0,70 (wie Karte): gleicher Ausgang, v2 der durchlaufenden mit
      Effekt >= 5 x Aenderung. "Codeschwellen auf 1 %" entfaellt: die Schwellen sind geschlossen und gitterfrei.
  - Codeschwellen (vom Code vor der Entwicklung gerechnet, in der Formprobe ausgegeben; keine Messung):
    A 0,55 / 0,70 / 0,90: v_cl = 0,07924 / 0,06553 / 0,03652; C: 0,14120 / 0,14127 / 0,14137 (Spanne 0,12 %);
    v_P1 = 0,051023, v_P2 = 0,072387. Die Handwerte der Karte (0,0796 / 0,0663 / 0,0371) liegen 0,5 bis 1,6 % daneben,
    wie die Karte fuer die zweite Ordnung erwartet.
  - Formprobe (lokal, CPU, 1 Faden, nice 19, Zeitfaktor 0,01; 11:25:08 bis 11:25:15, nach der Berichtigung
    "vor der Stufe" erneut bis 11:25:52): haupt und gegen rc 0. Keine Aussage daraus (die Baelle erreichen die Stufe
    in der verkuerzten Zeit nicht).
  - Die Karte kann scheitern (Schwellenausgaenge, Sortierung, Universalitaet in C); kein "L1 schwach".

- 2026-09-30 11:30:37 CEST, Leitung (Entscheidung vor jedem echten Lauf, ohne Ergebnis): Die drei Abweichungen des Test-Agenten sind
  angenommen.
  - Laufzeit T_run = min(2000, 80/v), damit auch langsame Baelle knapp ueber der Schwelle ankommen.
  - Schwellen aus der geschlossenen Formel statt aus dem Schiessen; beides stimmte in qg1 auf 1,2e-10 ueberein.
  - Die Pruefung "Summe der Anteile = 1" ist bauartbedingt immer erfuellt und zaehlt nicht als Kontrolle.
  - Kein Zusatz der Leitung zu den Messregeln.
