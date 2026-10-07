# Berichtigung zur Schreibtischherleitung der KEGEL-XD-Karte (Leitung, 03.10.2026, nach Codex-Lesung daa6a4db)

Die Karte bleibt unveraendert, weil sie vor jeder Rechnung stand. Diese Datei haelt Codex' berechtigte Korrekturen fest
(coordination/resonance-20260930/cone-review-20261003/LESUNG.txt, STRESS-REVIEW.txt).

1. **Huellensatz bei festem Q:** bestaetigt fuer glatte stationaere Aeste mit passenden Raendern.
   - d_a E_Q = d_a F bei festem omega; aus Q^2/(4I) folgt -omega^2 I_a.
   - Komponenten orthonormal nennen: T_thth meint T_(theta-Dach theta-Dach).
   - Der Lage-Multiplikator ist am frei verschiebbaren flachen Ball null.
2. **Strahlunabhaengigkeit:** bedingt.
   - Fuer die erste Ordnung genuegt das glatte flache Ausgangsprofil, an dem die Spitze noch kein singulaerer Punkt ist.
   - Auf dem echten Kegel braucht es zusaetzlich lim r^2 T_rth = 0 an der Spitze, passende Aussenraender und keine
     versteckte Quelle.
3. **Textfehler der Karte, Schritt 2 ("Probe"):** Die Identitaet int_0^inf (f'^2 + V) drho = 0 gilt nur in 2D.
   - In 3D ist int g drho = -2 int f'^2 drho, also nicht null.
   - Richtig ist in 3D: int dz int du g(sqrt(u^2 + z^2)) = pi int rho g drho = 0.
4. **Textfehler der Karte, Schritt 4 ("Kraft"):** -d(Delta E_1)/dd = -delta int_d^inf g drho gilt nur in 2D; in 3D kommt
   das z-Integral dazu.
   - Das anziehende Vorzeichen bei positivem Defizit bleibt (eigener Beweis bei Codex).
   - Die Numerik ist nicht betroffen: Der KEGEL-XD-Agent rechnete die 3D-Kraft mit z-Integral und traf sie auf 0,2 bis
     1,6 %.
5. **Wortwahl:** Statt "keine Fernkraft" besser "exponentieller Schwanz, keine algebraische Langstrecke".
6. **Literatur, von Codex gelesen, von mir noch nicht:**
   - Smolkin und Solodukhin, arXiv:1406.2512v3, Gl. (1.3): K_0 = -2 pi int d^(D-2)y int_0^inf dx_1 x_1 T_22. Das ist
     dieselbe gewichtete Halbraum-Spannungsstruktur, aber fuer Vakuumkorrelatoren bzw. den modularen Hamiltonoperator,
     kein Kraftbeweis fuer einen Q-Ball bei festem Q.
   - Linet 1986 (nur Abstract): abstossende elektrostatische Selbstkraft.
   - Bezerra u. a., gr-qc/9503028; Allen, Kay, Ottewill, gr-qc/9510058.
   - Genau die klassische Formel bei festem Q fand Codex nicht. Kein Neuheitsanspruch.
