# QBALL-GITTER-1: Plan (Code-Agent fuer die Leitung, Runde 35, explorativ nach v3)

- Start des Code-Agenten 21:56:48 CEST (date). Plan geschrieben ab 22:18:09 CEST (date), nach drei Rauchlaeufen (Abschnitt 8).
- Karte: KARTE.md (Vorhersagen G0 bis G4, Schwellen unveraendert uebernommen).
- Code: code/qgitter.py (Rechnung), code/auswertung.py (Urteile, Bilder), code/laeufe.sh (Hauptlaeufe).
  Nur fuer den Rauch: code/rauch1.sh, rauch2.sh, rauch3.sh, rauchcheck.py, vergleich.py.
- Kennzeichen: [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [L?] unsicher erinnert, [H] Hypothese,
  [F] Festlegung dieses Plans (von der Karte offengelassen), [E] im Rauch gesehen.

## 1. Modell [M]

- Gitter x_n = n h, komplexes psi_n, p_n = d psi_n/dt, U(S) = S - S^2 + S^3/2, omega^2 = 0,7.
- Lagrange-Funktion in zeitlicher Eichung (Peierls-Phase wie in der Karte):
  L = h sum |p_n|^2 - h sum U(|psi_n|^2) - (1/h) sum |exp(-i th) psi_{n+1} - psi_n|^2, th(t) = h a(t), a(t) = E t.
- Bewegungsgleichung:
  p_n' = (exp(-i th) psi_{n+1} + exp(i th) psi_{n-1} - 2 psi_n)/h^2 - U'(|psi_n|^2) psi_n (im Schwamm zusaetzlich - eta_n p_n).
- Ladung Q = 2 h sum Im(conj(psi_n) p_n). Ein Ball psi ~ exp(+i omega t) hat Q > 0.
  - Ladung je Verbindung: Strom j = -(2/h) Im(conj(psi_n) exp(-i th) psi_{n+1}). Die Kontinuitaetsgleichung gilt exakt.
  - Jeder Teilschritt des Integrators erhaelt Q exakt (bis auf Rundung).
- Energie H = h sum |p_n|^2 + h sum U + (1/h) sum |exp(-i th) psi_{n+1} - psi_n|^2. Es gilt dH/dt = E J mit dem
  Gesamtstrom J = -2 sum Im(conj(psi_n) exp(-i th) psi_{n+1}).
- Kraft, Vorzeichen und Formel [M]:
  - Kinetischer Impuls P = -2 h sum Re(conj(p_n) D psi_n) mit D psi_n = (exp(-i th) psi_{n+1} - exp(i th) psi_{n-1})/(2h).
  - Im Kontinuum ist P = P_kan + a Q, und P_kan ist erhalten. Aus der Ruhe folgt also gamma M v = P = Q E t.
  - Fuer Q > 0 und E > 0 zeigt die Beschleunigung nach +x. Der Rauch bestaetigt das (Abschnitt 8).
- Bloch-Periode [M]: Die Gitterdynamik haengt nur ueber exp(i th) von a ab, also T_B = 2 pi/(h E). Massgeblich ist das
  tatsaechlich verwendete E.
- Kontinuumswerte des Balls [M, geschlossene Form]:
  - Profil: phi^2 = 2 k^2/(1 + sqrt(1 - 2 k^2) cosh(2 k x)) mit k^2 = 1 - omega^2 = 0,3.
  - Werte: phi(0) = 0,6062, Q = 2,4416, M = 2,2986, M/Q = 0,9415.

## 2. Startzustand

- Stationaere Gitterloesung bei omega^2 = 0,7, platzzentriert.
  - Newton auf der halben Kette (Laenge 60) mit Spiegelrand phi_{-1} = phi_1 und phi = 0 am fernen Ende.
  - Startwert ist das Kontinuumsprofil, das Ergebnis wird gespiegelt.
  - Start: psi_n = phi_n, p_n = i omega phi_n bei th = 0.
- M0 = H(0) ist die Ruheenergie des Gitterballs, Q0 seine Ladung. Beide werden je h aus der Gitterloesung berechnet.
- **Feld [F]:** E1 = 0,005 M0/Q0 je h, also Q0 E1/M0 = 0,005 exakt (Karte: "~ 0,005"). Vergleich E2 = 2 E1.
  - Damit ist die Kontinuumskurve gamma = sqrt(1 + (0,005 t)^2) fuer alle h dieselbe.

## 3. Numerik [F]

- **Integrator:** Yoshida 4. Ordnung, symplektisch im erweiterten Phasenraum.
  - Die Drift schiebt psi und t, der Stoss rechnet mit th zur aktuellen Zeit.
  - Die Feldarbeit W wird schema-treu an den Stoessen summiert: W += d_i dt E J_i.
  - Damit ist R(t) = H(t) + E_abs + E_ab - H(0) - W(t) ein Fehler der Ordnung dt^4 ohne Drift (im Rauch: Faktor 16 je
    Halbierung).
- **Zeitschritt:** dt1 = 0,02 fuer alle h (Hauptlaeufe), Probe dt2 = 0,01.
  - Stabil: dt Omega_max <= 0,02 * 16,03 = 0,32 (Yoshida-Grenze ~1,57 [L?]).
- **Fenster:** mitlaufend, Laenge L_w = 400 (N = 800 / 1600 / 3200 Plaetze); Probe bei h = 0,125: L_w = 800 (6400
  Plaetze).
  - Sollort des Balls bei 0,4 L_w. Ab 10 Laengeneinheiten Abstand wird das Fenster um 10 Laengeneinheiten (ganze
    Plaetze) verschoben, in beide Richtungen. Das ist eine exakte Gittertranslation.
  - Was herausfaellt, wird mit Energie und Ladung exakt gebucht (E_ab, Q_ab). Die Werte sind H und Q vor minus nach
    der Verschiebung.
  - Abstand des Balls zu den Schwaemmen >= 90 (L_w = 400) bzw. >= 250 (L_w = 800).
- **Rand:** Geisterplaetze psi = 0 an beiden Enden. Schwamm je 60 Laengeneinheiten an beiden Enden:
  eta = 1,0 (1 - d/60)^2, d = Abstand zum Ende.
  - Ausgefuehrt exakt als p -> p exp(-eta dt/2) vor und nach jedem Schritt (Strang).
  - Energie- und Ladungsabfluss werden exakt gebucht (E_abs, Q_abs).
- **Modellgrenze:** Abstrahlung, die den Schwamm oder das Fensterende erreicht, ist weg. Ein Ball, der nach einer Umkehr
  zurueckkommt, trifft also nicht mehr auf seine alte Schleppstrahlung, soweit sie weiter als 90 bis 100 hinter ihm lag.
  Die lange Probe (Abstand 250 hinten, 470 vorn) prueft das.
- **Messung und Checkpoints:**
  - Messabstand 0,5, Momentaufnahmen der Ladungsdichte alle 25.
  - Jeder Abschnitt laeuft hoechstens 500 s Wandzeit, dann Checkpoint. Fortsetzung mit denselben Argumenten (im Rauch
    bitgleich).
- **Laufende:** t_end = T_B + 25 (G0: t = 500). Abbruch "zerfallen", wenn Q_win < 0,05 Q0.

## 4. Messvorschriften [F, soweit die Karte sie offenlaesst]

- **Ladungsdichte:** rho_n = 2 h Im(conj(psi_n) p_n) (Ladung je Platz). Q_dom = sum rho_n im Fenster.
- **Ladungsschwerpunkt X (Hauptmass):**
  - Schwerpunkt von rho mit glattem Gewicht w = cos^2(pi xi/(2 R)), |xi| < R, R = 10, xi = x - X.
  - Iteriert bis |dX| < 1e-12 max(1, |X|), Start am vorigen X.
  - Grund: Ein hartes Fenster verschob im Rauch 1 den ruhenden Ball um 5e-4 bis t = 50, weil Randplaetze
    hinzukamen bzw. herausfielen.
- **Zweites Mass (nur Kontrolle):** Energieschwerpunkt XE, gleiches Gewicht, ebenfalls iteriert.
  - Energiedichte = Platzenergie plus je die halbe Energie der beiden anliegenden Verbindungen.
- **Im Ball:**
  - Q_win = sum rho_n ueber |x_n - X| <= 10 (hartes Fenster). Beim ruhenden Ball liegen 3,1e-5 Q0 (h = 0,5) bzw. 3,9e-5 Q0
    (h = 0,125) ausserhalb (Rauch 2).
  - E_win ist die Energie im selben Fenster.
- **Abstrahlung:**
  - Q_aussen = Q0 - Q_win. Darin stecken die Ladung im Fenster ausserhalb des Balls, Q_abs und Q_ab.
  - E_aussen = (H + E_abs + E_ab) - E_win.
- **Schnelle:**
  - v(t) ist die Steigung der Ausgleichsgerade an X ueber [t - 10, t + 10] (41 Punkte). Definiert fuer
    10 <= t <= t_end - 10.
  - Kontrolle 1: Fenster [t - 20, t + 20]. Kontrolle 2: dasselbe aus XE.
- **gamma:** gamma(t) = 1/sqrt(1 - v(t)^2). Bei |v| >= 1 wird gamma = unendlich gesetzt und gemeldet.
- **gamma_max, t_max:** Maximum von gamma(t) ueber den ganzen Lauf. Nebenwert: Maximum, solange Q_win >= 0,5 Q0.
- **Energiebilanz mit der Feldarbeit:** R(t) wie in Abschnitt 3. Numerische Kontrolle max |R|/M0 <= 1e-4, keine
  Vorhersage.
- **Ladungsbilanz:** Q_dom + Q_abs + Q_ab - Q0. Kontrolle <= 1e-10 relativ.
- **Bloch-Periode:** T_B = 2 pi/(h E) aus dem Kopf jedes Laufs.
- **Umkehr:** t_u ist der erste Zeitpunkt nach t_max mit v < 0, linear zwischen den Messpunkten interpoliert.
  Q_win(t_u) wird interpoliert.
- **M und Q fuer G1:** M0 = H(0), Q0 = Q(0) des Gitterballs. Kontrolle: P_win/(Q0 E t) - 1 mit dem kinetischen Impuls im
  Fenster.

## 5. Laeufe (alle auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4)

| Name | h | Q0 E/M0 | t_end | dt | L_w | Zweck |
|---|---|---|---|---|---|---|
| g0_h{0,5; 0,25; 0,125} | je | 0 | 500 | 0,02 | 400 | G0 |
| f1_h{...}_dt1 | je | 0,005 | T_B + 25 | 0,02 | 400 | G1 bis G4 (Hauptlaeufe) |
| f2_h{...}_dt1 | je | 0,01 | T_B(E2) + 25 | 0,02 | 400 | Vergleich doppeltes Feld |
| f1_h{...}_dt2 | je | 0,005 | T_B + 25 | 0,01 | 400 | Probe halber Zeitschritt |
| f1_h0.125_lang | 0,125 | 0,005 | T_B + 25 | 0,02 | 800 | Probe laengere Kette |

- Erwartete Bloch-Perioden (E1): 2669 / 5339 / 10678 fuer h = 0,5 / 0,25 / 0,125. Fuer E2 die Haelfte.
- Die Karte verlangt bei h = 0,5 mindestens T_B/2; gerechnet wird bei allen h bis T_B + 25.
- Zeitbedarf (Rauch: 0,28 ms je Schritt bei N = 800, 0,5 ms bei N = 3200): etwa 15 min je Spur.

## 6. Urteilsregeln (mechanisch, code/auswertung.py)

- **G0** (Karte: Drift < 1e-4 bis t = 500, Ladung auf 1e-10, Energie auf 1e-7):
  - Laeufe g0_h0.5, g0_h0.25, g0_h0.125 mit dt1.
  - Je h: max |X(t) - X(0)| < 1e-4, max |Q_dom(t) - Q_dom(0)|/Q_dom(0) <= 1e-10 und max |H(t) - H(0)|/H(0) <= 1e-7,
    jeweils fuer t <= 500. Der Lauf muss t = 500 erreichen.
  - **Eingetroffen**, wenn alle drei h bestehen [F: alle drei h]. Fehlt ein Lauf: nicht auswertbar.
- **G1** (h = 0,125: gamma M v = Q E t innerhalb 2 % bis gamma = 1,5):
  - Lauf f1_h0.125_dt1, M = M0, Q = Q0, E = E1.
  - t_1,5 ist der erste Zeitpunkt mit gamma(t) >= 1,5.
  - Abweichung A(t) = gamma M0 v/(Q0 E t) - 1 fuer alle Messpunkte t in [20, t_1,5] [F: Beginn t = 20, dort ist
    Q E t/M = 0,1].
  - **Eingetroffen**, wenn max |A| <= 0,02.
  - **Nicht eingetroffen**, wenn max |A| > 0,02 oder gamma 1,5 nie erreicht.
- **G2** (gamma_max(h) existiert, waechst mit kleinerem h, gamma_max(0,125) >= 1,5 gamma_max(0,5)):
  - Hauptlaeufe f1_h*_dt1.
  - Je h gilt "Maximum erreicht", wenn eine der drei Bedingungen zutrifft:
    1. gamma am Ende der v-Reihe <= gamma_max - 0,05 (gamma_max - 1) (gefallen)
    2. die Steigung einer Ausgleichsgerade an gamma(t) im letzten Viertel der v-Reihe ist <= 0,05 * 0,005 = 2,5e-4
       je Zeiteinheit (gesaettigt)
    3. der Ball ist zerfallen (Lauf mit Status "zerfallen")
  - **Eingetroffen**, wenn alle drei folgenden Punkte gelten:
    - alle drei h haben ein Maximum
    - gamma_max(0,5) < gamma_max(0,25) < gamma_max(0,125)
    - gamma_max(0,125)/gamma_max(0,5) >= 1,5
  - Wird irgendwo |v| >= 1 gemessen: nicht auswertbar.
- **G3** (Umkehr nach dem Maximum vor T_B mit >= 50 % Ladung):
  - Hauptlaeufe f1_h*_dt1. Je h gilt:
    - **ja:** t_u existiert, t_u < T_B und Q_win(t_u) >= 0,5 Q0
    - **nein:** t_u existiert, aber t_u >= T_B oder Q_win(t_u) < 0,5 Q0; oder es gibt kein t_u und die v-Reihe reicht bis
      T_B; oder der Ball ist vor einer Umkehr zerfallen
    - **offen:** sonst
  - **Eingetroffen**, wenn alle drei h "ja" haben [F: Die Karte formuliert allgemein, also alle drei h].
  - **Nicht eingetroffen**, wenn mindestens ein h "nein" hat. Sonst nicht auswertbar.
- **G4** (gamma_max des Q-Balls mindestens so gross wie beim Kink, 1,78 / 2,61 / 3,86):
  - gamma_max aus G2 (E1). **Eingetroffen**, wenn alle drei h die Schwelle erreichen [F: alle drei h, Feld E1].
  - Hinweis: Der Kink-Wert in NETZ-C-1 stammt aus der Energie, hier aus der Schnelle des Ladungsschwerpunkts.
- **Konvergenzproben:**
  - Dieselben Regeln werden mit f1_h*_dt2 an Stelle der Hauptlaeufe angewandt (G1 bis G4), ebenso mit f1_h0.125_lang an
    Stelle von h = 0,125.
  - Massgeblich bleibt das Urteil des Hauptlaufs. Gibt eine Probe ein anderes Urteil, wird das Urteil in ERGEBNIS.md als
    "nicht robust" vermerkt.
- **Zweites Feld E2:** dieselben Regeln, nur beschreibend (Vergleich der Karte, kein eigenes Urteil).
- **Bedeutung:** wie in der Karte vorab festgelegt. Ein Satz der Karte wird nur ausgeloest, wenn seine Urteile so
  ausfallen.

## 7. Schreibtisch-Erwartungen (vor den Hauptlaeufen)

- Kontinuumsfahrplan fuer Q E/M = 0,005: gamma = 1,5 bei t = 224. Die Kink-Werte 1,78 / 2,61 / 3,86 waeren bei
  t = 294 / 482 / 746 erreicht.
- Lineare Gitterwellen [M]: v_g,max = 0,781 / 0,883 / 0,940, also gamma 1,60 / 2,13 / 2,92 (Karte).
- Diskretheit [H, L?]:
  - Die Gitterkorrektur eines glatten Profils der Breite 1/(gamma k) faellt etwa wie exp(-pi^2/(h k gamma)). Das waere
    fuer h = 0,5 und gamma = 1,6 noch ~1e-10.
  - Der fruehe Einfluss des Gitters liegt deshalb eher in der Traegerwelle als im Profil.
    - Traegerwelle: Phase je Verbindung h omega gamma v (kinetisch).
    - Bei gamma v ~ 1 ist das 0,4 (h = 0,5), die Gitterdispersion weicht um (k h)^2/24 ~ 1 % ab.
- Bloch-Bild [H]:
  - Bliebe der Ball relativistisch (k_kin = omega gamma v = (omega Q/M) E t), erreichte seine Traegerphase je
    Verbindung den Zonenrand pi bei t = 0,563 T_B.
  - Dort muesste ein heiler Ball aus Symmetriegruenden stehen bleiben.
- Erwartung ohne Rechnung [H]:
  - G1 duerfte halten, weil das Gitter bei h = 0,125 erst bei gamma v ~ 3 bis 4 merklich wird.
  - Ob der Ball danach saettigt (wie der Kink) oder Bloch-artig umkehrt, ist offen. Ein Ball kann im Unterschied zum
    Kink Ladung abgeben.

## 8. Rauchlaeufe vor dem Einfrieren (offengelegt, was ich gesehen habe)

- **Rauch 1** (20:10:23 bis 20:10:30 UTC, code/rauch1.sh):
  - Newton:
    - h = 0,5: 4 Schritte, Rest 4,7e-16, phi_0 = 0,60778, M0 = 2,28763, Q0 = 2,42946
    - h = 0,125: 3 Schritte, Rest 1,3e-14, phi_0 = 0,60635, M0 = 2,29793, Q0 = 2,44075
  - Fehler 1: Ein Checkpoint-Schluessel war doppelt (n0). Behoben.
  - Fehler 2: Der Schwerpunkt mit hartem Fenster (R = 8, drei Iterationen) driftete beim ruhenden Ball um 5e-4 (h = 0,5)
    bzw. 1,8e-4 (h = 0,125) bis t = 50.
    - Behoben durch das glatte Gewicht und Iteration bis zur Konvergenz, R von 8 auf 10 (Abschnitt 4).
    - Das ist eine Messkorrektur vor dem Einfrieren; die G0-Schwelle bleibt.
  - h = 0,125, Q E/M = 0,005, dt = 0,0125, t = 100: Der Ball laeuft nach +x, X(100) - X(0) = 23,58 (Kontinuum 23,61).
- **Rauch 2** (20:15:08 bis 20:15:17 UTC, code/rauch2.sh, nach der Messkorrektur):
  - **Ruhender Ball** (h = 0,5 und 0,125, dt = 0,02, t = 50): Drift 0, Ladung 2e-15, Energie 1,7e-15.
  - **Vorzeichen und Formel bei kleinem h** (h = 0,125, Q E/M = 0,005, t = 100):
    - Abweichung A = gamma M0 v/(Q0 E t) - 1 = -0,09 % / -0,15 % / -0,16 % / -0,18 % / -0,21 % bei t = 20 / 30 / 50 / 70
      / 90, also gamma bis 1,096.
    - Aus dem kinetischen Impuls: -0,08 % bis -0,13 %. dt = 0,02 und 0,01 stimmen auf 1e-7 ueberein.
    - **Damit habe ich G1-relevante Werte bis gamma = 1,1 gesehen; die Schwelle 2 % bleibt unveraendert.**
  - h = 0,5, Q E/M = 0,01 (Fortsetzungstest): A = -1,6 % / -2,0 % / -3,0 % bei t = 20 / 30 / 50 (gamma bis 1,11).
  - **Energiebilanz R/M0:** 5,8e-9 (dt = 0,02), 3,7e-10 (dt = 0,01); Faktor 16 je Halbierung. Ladungsbilanz <= 7e-15.
  - **Fortsetzung:** ueber 4 Abschnitte mit einer Fensterverschiebung bitgleich zum ununterbrochenen Lauf.
  - **Zeit:** 0,28 ms je Schritt (N = 800), 0,5 ms (N = 3200).
  - **Festlegung danach:** dt1 = 0,02 statt der zuerst benutzten 0,0125, wegen der Laufzeit. Die Probe dt2 = 0,01 bleibt.
- **Rauch 3** (bis 20:17:35 UTC, code/rauch3.sh):
  - Auswertepfad mit Kurzlaeufen (t <= 40) unter den Namen der Hauptlaeufe. Er prueft die Code-Pfade und die Bilder; die
    Urteile dort sind ohne Bedeutung.
  - Ladung im Ball in Ruhe (Rauch 2, R = 10): 3,1e-5 Q0 (h = 0,5) bzw. 3,9e-5 Q0 (h = 0,125) ausserhalb von +-10.
- Keine Schwelle der Karte wurde nach einem Rauchlauf geaendert.

## 9. Nach dem Einfrieren

- Plan und Urteilsregeln bleiben unveraendert. Code nur bei echten Fehlern aendern, mit Offenlegung in ERGEBNIS.md.
- Pruefsummen von Plan und Code in code/pruefsummen-einfrieren.txt.
