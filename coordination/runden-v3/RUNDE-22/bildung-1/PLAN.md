# BILDUNG-1 (Runde 22): Plan

Bearbeiter: Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 19:02:26 CEST (date).
Plan geschrieben ab 19:13:57 CEST (date), nach dem Rauchlauf (Abschnitt 9) und vor jedem echten Lauf. Explorativ (v3),
Hypothesen [H]. Karte: KARTE.md daneben. Vorhersagen B0 bis B3 und Bedeutung stehen dort und werden hier nur
mechanisch umgesetzt. Was ich selbst festlege, ist mit **[Festlegung BILDUNG-1]** markiert.

## 1. Frage

Laeuft ein einzelner, nicht passender Gauss-Klumpen mit der Ladung des Familienballs bei omega^2 = 0,60 ohne
Verschmelzen auf die Q(omega)-Familie zu? Bewertet mit dem unveraenderten Klassifikator aus Runde 6 zu T = 100, 250,
500, 1000.

## 2. Original geprueft

- sha256, lokal und auf der .69 gleich:
  - kf5_geburt.py (Runde 6) 9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0
  - familie_2d_m0.json f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806
  - kf_eich.py (Runde 21) 332f3293a94448848beeb1c90a58ba9128d14e4f5029983832a8ea7a77eacb59
  - kleintest.sh e380fc4902e7fed4ca2c5a6c9aa30dda89738d9165a367a8bd342e4932b84986
- bildung1.py importiert beide unveraendert (nur gelesen, ohne Bytecode) aus /home/fmh/fmhc-physics-remote/runde6-kf5 und
  /home/fmh/fmhc-physics-remote/runde21-kf-eich.
  - Aus kf5_geburt: Gitter, kraft_fn, dichten, analyse_arm, fenster_start, fenster_probe, fenster_auswerten (darin
    familien_klasse), Familie, Konstanten (STUFEN, BOX0 96, FENSTER 40, DT_FENSTER 1, FAKTOREN 2/3, A_MIN 2, KOMPAKT 2,
    KOMPAKT_FAMILIE 1,3, R_PLUS 6, R_SUCH 2, FAM_TOL 0,10, Q_SCHWANK 0,20).
  - Aus kf_eich: profil (Schiessverfahren), ball_feld, omega_gitter, familien_abstaende, familien_knoten, Hilfen.
- Die Verlet-Schleife steckt in kf5_geburt.lauf() und ist nicht einzeln aufrufbar. Sie ist Zeile fuer Zeile nachgebaut
  wie in Runde 20/21, ergaenzt nur um den Absorber (Abschnitt 4).

## 3. Klumpen (Formeln vorab)

- **Familienball** bei omega^2 = 0,60 aus familie_2d_m0.json: Q_F = 66,616119, E_F = 56,527292, R_F = r_ladung =
  3,074146, omega_F = w0 = sqrt(0,60) = 0,774597.
- **Ladungsradius.** Die Leitung schreibt: "dieselbe Radiusgroesse, die der Klassifikator fuer R_F verwendet; lies sie
  aus dem Code". Befund aus dem Code:
  - kf5_geburt.Familie liest aus der Familiendatei nur omega2, Q und E, nicht r_ladung. Die Definition von r_ladung
    steht in keiner erlaubten Datei (sie stammt aus Runde 4).
  - Der Klassifikator selbst misst nur R_A = sqrt(A/pi), A = Flaeche der Maske S >= 2 S0. Fuer einen Gauss mit Q = Q_F
    gilt R_A^2 = s^2 ln(A^2 / 0,6) mit A^2 = Q_F / (2 w0 pi s^2). Das Maximum ueber s ist Q_F / (2 w0 pi 0,6 e) = 8,39,
    also R_A <= 2,897. Der Familienball hat R_A = 3,19 (Profil, Runde 21). Mit R_A ist (i) also nicht erfuellbar.
  - Daher **[Festlegung BILDUNG-1]**: R_F ist r_ladung aus der Familiendatei (wie die Karte sagt), und der Ladungsradius
    des Klumpens wird mit derselben Definition wie r_ladung gebildet.
  - Regel fuer die Definition (im Code, vor dem Lauf): Am exakten Profil (kf_eich.profil(0,60)) werden drei Kandidaten
    gerechnet: rms = sqrt(Int r^2 rho / Int rho), mittel = Int r rho / Int rho, halb = Radius mit halber Ladung. Gilt
    der Kandidat, der r_ladung am naechsten liegt, auf 1e-3 relativ, wird er genommen, sonst rms.
  - Ergebnis im Rauchlauf: rms 3,074146 (rel -1,9e-7), mittel 2,779950, halb 2,692183. **r_ladung ist der
    rms-Ladungsradius.** Auf dem Gitter misst der K0-Ball r_rms = 3,074145.
  - Fuer den Gauss ist rho ~ exp(-r^2/s^2), also r_rms = s.
- **Klumpen:** psi = A exp(-r^2/(2 s^2)), psi_t = -i w0 psi, Mitte (0, 0), ein Klumpen je Box.
  - (i) s = R_F; (ii) s = 1,3 R_F; (iii) s = 0,7 R_F.
  - A aus Q = 2 w0 Int |psi|^2 dA = 2 w0 A^2 pi s^2 = Q_F, also A = sqrt(Q_F / (2 w0 pi s^2)).
  - **Vorzeichen [Festlegung BILDUNG-1]:** Die Karte schreibt psi_t = i w0 psi. Mit der Ladungsdichte von kf5_geburt
    (rho = 2 Im(psi conj psi_t)) gaebe das Q = -Q_F. Der Klassifikator verlangt Q > 0 ("ungestoert") und misst omega
    ueber exp(-i omega t). Daher psi_t = -i w0 psi wie in kf5_geburt und kf_eich. Wegen der Ladungskonjugation ist
    das physikalisch gleichwertig.

  | Fall | s | A | S_max = A^2 | Q (Gitter, rel zu Q_F) | E (Gitter) | E/Q (Familie E_F/Q_F = 0,84855) |
  |---|---|---|---|---|---|---|
  | (i) | 3,074146 | 1,203476 | 1,44835 | 0 | 57,2449 | 0,85932 |
  | (ii) | 3,996390 | 0,925751 | 0,85701 | -2e-16 | 58,3310 | 0,87563 |
  | (iii) | 2,151903 | 1,719251 | 2,95582 | 0 | 77,1510 | 1,15814 |
  | K0 (Familienball) | - | f(0) | 1,06119 | +7,1e-8 | 56,5273 | 0,84855 |

  - Diese Startwerte sind Setup (Rauchlauf, Abschnitt 9). Auffaellig: (iii) hat E/Q > 1, also mehr Energie als Q
    ruhende freie Quanten.
- **K-Pruefung** je Lauf bei t = 0 (Gate, sonst keine Zeitentwicklung):
  - K0: Q, E und omega der Gittergleichung auf 1e-3 gegen die Familiendatei (wie Runde 21).
  - Klumpen: Q auf 1e-3 gegen Q_F und r_rms auf dem Gitter auf 1e-3 gegen s.

## 4. Box und Absorber [Festlegung BILDUNG-1]

- **Gitter wie Runde 6:** Box 96, periodisch, [-48, 48)^2. grob dx 0,25 / dt 0,04 (n 384), fein dx 0,125 / dt 0,02
  (n 768).
- **Absorberrahmen:** Breite 16, ungedaempft fuer max(|x|, |y|) <= 32.
  - sigma = 1 * xi^2 mit xi = clamp((max(|x|, |y|) - 32) / 16, 0, 1); m = exp(-sigma dt).
  - Schritt: vel += F dt/2; psi += vel dt; psi *= m; F = kraft(psi); vel += F dt/2; vel *= m.
  - Innen ist m exakt 1. Dort ist der Schritt bitgleich mit dem Runde-6-Verlet.
  - Was durch den Rand laeuft, kommt periodisch im gegenueberliegenden Rahmen an und wird dort weiter gedaempft.
- **Rauchlauf-Schaetzung** (grob, alle vier Faelle, t = 0 bis 60, Abschnitt 9):
  - K0: Q_box konstant auf < 1e-6, Ladung im Rahmen hoechstens 8e-10 Q0. Der Absorber stoert den exakten Ball nicht.
  - Strahlung: Die Front S >= 1e-4 laeuft mit etwa 0,75 je Zeiteinheit (Fall i: 12,25 / 19 / 26,75 / 34,5 bei t = 10 /
    20 / 30 / 40) und erreicht den Rahmen ab t etwa 35 bis 40.
  - Ladung im Rahmen: hoechstens 3,4 % von Q0 (Fall iii, t = 50 bis 60); Q_box bei t = 60: 0,9957 / 0,9988 / 0,9439
    (i / ii / iii). Das ist abgestrahlte Ladung, die der Absorber nimmt.
  - Der dichte Kern (Maske S >= 0,6) bleibt bei allen vier Faellen bis t = 60 innerhalb max(|x|, |y|) <= 3.
- **Hochrechnung auf T = 1000:**
  - Strahlung erreicht den Absorber bis T = 1000 sicher, auch langsame Anteile (Gruppengeschwindigkeit 0,03 erreicht den
    Rahmen ab Abstand 30 bis T = 1000). Das ist erlaubt.
  - Die Ballladung erreicht ihn nur, wenn der Ball um etwa 20 wandert oder auf mehr als etwa 24 anschwillt. Der Start
    ist zentriert und ruhend; ein Grund fuer eine Drift ist nicht vorhanden. **Keine Boxvergroesserung.**
- **Box-Pruefung (Regel):** Je Lauf (Gitter, Fall) liegt die Maske S >= 0,6 zu allen Diagnosezeiten (alle 10, 0 bis
  1000) innerhalb max(|x|, |y|) <= 24, also mindestens 8 vor dem Rahmen.
  - Ist das verletzt oder fehlt die Reihe bis 1000, sind B1 bis B3 fuer diesen Fall "offen (Box)".
  - Berichtet werden dazu: Q_box(t)/Q0 (der Rest ist absorbierte Strahlung), Ladung im Rahmen, Q(r <= 12) und die
    Ausdehnung der Maske S >= 0,2.

## 5. Zeitentwicklung und Urteile [Festlegung BILDUNG-1, wo nicht Karte]

- **Fenster [T - 40, T]** wie Runde 6/20/21, T = 50, 100, 200, 250, 500, 1000.
  - Die Karte entscheidet an T = 100, 250, 500, 1000.
  - K0 entscheidet an T = 50, 100, 200 ("bleibt bis T = 200").
  - Klumpen zu 50 und 200 sind beschreibend.
- **Je Fenster und Fall** genau wie Runde 21:
  - analyse_arm am Fensterbeginn (alt = None), fenster_start, fenster_probe alle 1 (41 Proben), fenster_auswerten(fzs,
    T - 40, 1, fam, 96).
  - Ball = der Fenstertropfen, dessen Startort (x0, y0) (0, 0) am naechsten liegt, hoechstens 5 entfernt. Sonst
    "kein Tropfen".
  - Urteil = Klasse aus fenster_auswerten ("auf", "neben", "unentschieden", "ausserhalb", "gestoert", "nicht rund").
    "rund" = rmax/R_A <= 1,3 am Fensterbeginn.
- **S0:** Hauptauswertung S0 = 0,3 (Schwelle S >= 0,6, wie Runde 21). Sie entscheidet B0 bis B3. Zusatz S0 = 0,1
  (Schwelle 0,2) auf denselben Laeufen, getrennt berichtet, entscheidet nichts (Ausnahme B3-Ersatz, Abschnitt 6).
- **Rohgroessen je Fall, Gitter, Zeit:**
  - Q-Anteil = Q_net / Q0 (Q0 = Q_box bei t = 0 = Q_F); dazu Q(r <= 12)/Q0 und Q_box/Q0 am Fensterbeginn.
  - omega_ruhe +- u, omega_geo; E/Q (E_ruhe_net / Q_net) und (E/Q)_fam(Q); Rundheit rmax/R_A; S_max; Q-Schwankung; v.
  - Abstandsmasse wie Runde 20/21: dQ* = Q_net / Q_fam(omega_ruhe) - 1; E/Q-Abstand = (E/Q) / (E/Q)_fam(Q) - 1;
    omega-Abstand = omega_ruhe - omega_fam(Q). Zusatz: d_F = Q_net / Q_F - 1, domega_F = omega_ruhe - w0.

## 6. Vorhersagen (Karte) und Regeln (S0 = 0,3)

| Nr | Karte | Wahrsch. | Regel |
|---|---|---|---|
| B0 | K0 bestanden | 90 % | K0 zu T = 50, 100, 200 auf beiden Gittern: 6 Urteile; eingetroffen, wenn alle "auf" und rund; nicht eingetroffen, wenn eines fehlt; offen, wenn Laeufe fehlen |
| B1 | (i) bei T = 500 "auf" und "rund", beide Gitter | 65 % | 2 Urteile, beide "auf" und rund |
| B2 | (ii) und (iii) bei T = 1000 beide "auf" und "rund", beide Gitter | 50 % | 4 Urteile, alle "auf" und rund |
| B3 | alle drei behalten bei T = 1000 >= 80 % der Anfangsladung | 60 % | 6 Werte (3 Faelle x 2 Gitter) Q-Anteil = Q_net / Q0 im Fenster [960, 1000] >= 0,80; gibt es bei S0 = 0,3 keinen Ball, gilt der Ball des Zusatzes S0 = 0,1, gibt es keinen, zaehlt 0 |

- B1 bis B3 sind "offen (Box)", wenn die Box-Pruefung eines beteiligten Laufs scheitert.
- **Bedeutung (Karte, mechanisch):**
  - B0 nicht eingetroffen oder offen: B1 bis B3 ohne Aussage.
  - B1 und B2 eingetroffen: Einzelne Klumpen laufen auf die Familie zu. M1 ist in 2D fuer isolierte Klumpen
    bildungsfaehig (Stufe 5, im Modell) [H]. Das "nie auf" in KF-5 lag dann am Verschmelzen bzw. an der Zeit.
  - B1 nicht eingetroffen: Auch ein einzelner, gut passender Klumpen erreicht die Familie bis T = 500 nicht. Stufe 5
    ist fraglich; Grund beschreiben.
  - Sonst (B1 eingetroffen, B2 nicht): Die Karte nennt keine Bedeutung. Ich berichte beschreibend und deute nicht.
- **Schreibtischrechnung (koennen B1 bis B3 scheitern und bestehen?):**
  - (i) liegt nahe der Familie: E/Q 1,3 % ueber dem Familienwert, S_max 1,45 statt 1,06. Abstrahlen von etwa 0,7
    Energie fuehrt zum Familienball; ein langlebiges Atmen kann omega verschmieren (u gross -> "unentschieden") oder
    rmax/R_A > 1,3. Beide Ausgaenge moeglich.
  - (iii) hat E/Q 1,158 > 1. Er kann ganz zerfliessen ("kein Tropfen", Q-Anteil klein) oder einen kleineren Ball
    zuruecklassen. Ein kleinerer Ball kann "auf" sein (anderer Familienpunkt); B3 kann daran scheitern.
  - (ii) hat S_max 0,857 nahe der Schwelle 0,6 und E/Q 3,2 % ueber der Familie.
  - Keine Regel steht vorab fest.

## 7. Aufrufe (kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde22-bildung-1)

```
bash .../kleintest.sh p4000a b1-grob     bildung1.py lauf --stufe grob --gruppe alle --von 0 --bis 1000
bash .../kleintest.sh p4000x b1-fa1      bildung1.py lauf --stufe fein --gruppe a --von 0 --bis 500
bash .../kleintest.sh p4000x b1-fa2      bildung1.py lauf --stufe fein --gruppe a --von 500 --bis 1000
bash .../kleintest.sh p4000y b1-fb1      bildung1.py lauf --stufe fein --gruppe b --von 0 --bis 500
bash .../kleintest.sh p4000y b1-fb2      bildung1.py lauf --stufe fein --gruppe b --von 500 --bis 1000
bash .../kleintest.sh p4000a b1-zusammen bildung1.py zusammen --geraet cpu
```

- Gruppen: alle = K0, i, ii, iii; a = K0, i; b = ii, iii. Spur p4000a, die zweite fein-Gruppe auf p4000b, wenn frei.
- Zwischenspeicher (nur .69): lauf-69/zwischen/fein_<gruppe>_t500.pt (complex128 psi und vel, Q0, E0). Keine
  Abschnittsgrenze schneidet ein Fenster (Pruefung im Code).
- Laufzeit (Rauchlauf): grob 3,15 ms je Schritt (B 4), 25000 Schritte etwa 80 s plus Fenster; fein 6,47 ms je Schritt
  (B 2), je Abschnitt 25000 Schritte etwa 165 s plus Fenster. Zeitgrenze im Code 560 s (Prognose nach 400 Schritten).

## 8. Latten (v3) und Grenzen (vorab)

- **L1 kann scheitern:** ja, B0 bis B3 haben beide Ausgaenge (Abschnitt 6).
- **L2 Gegenprobe:** K0 im selben Aufbau; K-Pruefung; r_rms des K0-Balls auf dem Gitter gegen r_ladung; zwei Schwellen;
  Q(r <= 12) als zweites Ladungsmass neben der Scheibe des Klassifikators.
- **L3 Numerik:** grob gegen fein mit identischer kontinuierlicher Anfangsfunktion.
- **L4 schon bekannt:** Relaxation angeregter Q-Baelle und Zerfall zu grosser Klumpen sind in der Literatur bekannt [L,
  nicht nachgeprueft]. Neu ist nur der Befund fuer M1 mit diesem Klassifikator.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter).
- **Grenzen:**
  - Nur radialsymmetrische Starts mit Q = Q_F; keine Stoerung der Symmetrie ausser Rundungsfehlern.
  - Absorber: Reflexion am Rahmen nicht gemessen (nur die Rahmenladung).
  - "auf" heisst nur "Q passt zu omega" (Runde 21).

## 9. Rauchlauf (vor dem Einfrieren)

- 2026-10-02 19:12:49 bis 19:13:27 CEST (Uhr der .69 in UTC), Spur p4000a, rc = 0:
  - grob alle 0 -> 30 und 30 -> 60 mit Zwischenspeicher (prueft das Abschnittsverfahren), Fenster 4 bei T = 8, 16, 40.
  - fein a 0 -> 10.
- Gemessen: Radiuswahl rms, K-Pruefung (Abschnitt 3), Dauern, GPU 103 MB (grob, B 4) / 234 MB (fein, B 2), die
  Diagnosereihe bis t = 60 (Abschnitt 4).
- Die Fenstereintraege wurden gerechnet, aber nicht ausgegeben (nur gezaehlt: 16, 8, 4).
- **Selbstanzeige:** Die Diagnosereihe zeigte vor dem Einfrieren fruehe Ladungsverluste (z. B. (iii): Q(r <= 12) 0,65
  von Q0 bei t = 60). Die Vorhersagen stammen aus der Karte und bleiben unveraendert. Aus dem Rauchlauf folgt hier nur
  die Box-Entscheidung (Box 96 bleibt).
- Dateien: lauf-69/RAUCH-grob.log, lauf-69/RAUCH-fein.log, Rauch-JSON in lauf-69/rauch/.

## 10. Stand beim Einfrieren

Siehe die letzte Zeile (sha256 von bildung1.py, lokal = .69, py_compile auf der .69 ok).

Eingefroren 2026-10-02 19:15:21 CEST (date), vor jedem echten Lauf. bildung1.py sha256 0ef60ef1f8f1dd209808c5b1dbce044d8238f1f9ceedbe64405c2879f6a0ff64 (lokal = .69, py_compile auf der .69 ok).
