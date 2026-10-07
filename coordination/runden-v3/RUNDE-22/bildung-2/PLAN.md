# BILDUNG-2 (Runde 22): Plan

Bearbeiter: Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 19:30:35 CEST (date).
Plan geschrieben ab 19:44:49 CEST (date), nach dem Rauchlauf (Abschnitt 11) und vor jedem echten Lauf. Explorativ (v3),
Hypothesen [H]. Karte: KARTE.md daneben. Vorhersagen C0 bis C4 und Bedeutung stehen dort und werden hier nur
mechanisch umgesetzt. Was ich selbst festlege, ist mit **[Festlegung BILDUNG-2]** markiert.

## 1. Frage

Woran lag das "nie auf" der KF-5-Tropfen: an der Groesse (duennwandig, grosses Q), am Wellenbad oder am Verschmelzen?
Drei Arme mit dem unveraenderten Aufbau, Integrator, Klassifikator und der Box von BILDUNG-1, Urteile zu T = 100, 250,
500, 1000.

## 2. Original geprueft

- sha256, lokal und auf der .69 gleich:
  - bildung1.py (R22) 0ef60ef1f8f1dd209808c5b1dbce044d8238f1f9ceedbe64405c2879f6a0ff64
  - kf5_geburt.py (R6) 9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0
  - familie_2d_m0.json f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806
  - kf_eich.py (R21) 332f3293a94448848beeb1c90a58ba9128d14e4f5029983832a8ea7a77eacb59
  - kleintest.sh e380fc4902e7fed4ca2c5a6c9aa30dda89738d9165a367a8bd342e4932b84986
- bildung2.py importiert bildung1.py unveraendert (nur gelesen, ohne Bytecode) aus
  /home/fmh/fmhc-physics-remote/runde22-bildung-1, darueber wie in BILDUNG-1 kf5_geburt (R6) und kf_eich (R21).
  - Aus bildung1: radius_definitionen, klumpen_feld, absorber, diag_zeile; Konstanten W2_F, BOX, ABS_BREITE, ABS_SIGMA,
    T_FEN, T_DIAG, S0_HAUPT/ZUSATZ, BALL_SUCH, K_TOL, R_TOL_DEF, RINGE, MASKE_ABSTAND, GAUSS_FAKTOR, ZEITGRENZE_S,
    RAUCH_*.
  - Aus kf5_geburt: Gitter, kraft_fn, dichten, komponenten, eigenschaften, analyse_arm, fenster_start, fenster_probe,
    fenster_auswerten, Familie, Konstanten. Aus kf_eich: profil, ball_feld, omega_gitter, familien_abstaende,
    familien_knoten, Hilfen.
- **Integrator:** Die Schleife steckt in bildung1.befehl_lauf und ist nicht einzeln aufrufbar. Sie ist Zeile fuer Zeile
  nachgebaut: vel += F dt/2; psi += vel dt; psi *= m; F = kraft(psi); vel += F dt/2; vel *= m.
- **Absorber:** absorber_box hat die Form von bildung1.absorber (Breite 16, sigma_max 1, sigma = xi^2), nur
  innen = Box/2 - 16 aus der eigenen Box. Fuer Box 96 prueft der Lauf, dass m und Rahmen **bitgleich** mit
  bildung1.absorber sind, sonst Abbruch (im Rauchlauf bestanden).
- Gitter wie Runde 6: grob dx 0,25 / dt 0,04, fein dx 0,125 / dt 0,02.

## 3. Arme und Startzustaende (Werte aus dem Rauchlauf, K-Pruefung bei t = 0)

- **Klumpen (i)** wie BILDUNG-1: psi = A exp(-r^2/(2 s^2)), psi_t = -i w0 psi, s = R_F (r_ladung = rms-Ladungsradius,
  Regel aus BILDUNG-1), A = sqrt(Q_F / (2 w0 pi s^2)), w0 = omega_F.
  - omega^2 0,60: Q_F 66,616119, R_F 3,074146, s 3,074146, A 1,203476, S_max 1,44835, E/Q 0,85932 (Familie 0,84855).
  - omega^2 0,52: Q_F 1421,452286, E_F 1045,954016, R_F 12,532245; Profil-rms 12,532263 (rel +1,4e-6), Wahl rms.
    s 12,532245, A 1,413339, S_max 1,99753, E/Q 0,82694 (Familie 0,73583, also 12,4 % darueber).
- **Arm A [Festlegung BILDUNG-2: Box 128]:** ein Klumpen (i) bei omega^2 = 0,52 in der Mitte.
  - Der Punkt 0,52 ist ein Knoten der Familiendatei (geprueft; kein Ersatzpunkt noetig).
  - Box 128 (grob n 512, fein n 1024), Absorber innen 48, Rahmen 16. Grund: Der Familienball hat bei S ~ 1,02 einen
    Kern bis etwa r = 17,5 (Flaeche aus Q). Mit Box 96 laege die Box-Grenze bei 24, zu knapp. Mit 128 liegt sie bei 40.
  - **Zusatz-K-Arm KA [Festlegung BILDUNG-2]:** exakter Familienball 0,52 im selben Aufbau (Box 128, Absorber). Er
    entscheidet nichts, er zeigt nur, ob der Klassifikator in diesem Aufbau bei 0,52 "auf" sagt (L2). K bei t = 0:
    Q rel +2,9e-6, E rel +2,9e-6, omega der Gittergleichung rel -3e-11 / -6e-11 (wie KF-EICH).
- **Arm B (Wellenbad) [Festlegung BILDUNG-2: Erzeugung]:** Klumpen (i) bei 0,60 in der Mitte plus Bad.
  - Bad = Summe ebener Gittermoden k = 2 pi n / 96 mit 0,25 <= |k| <= 1,0 (696 Moden), gleiche Amplitude 9,173e-4,
    Phase gleichverteilt (Seed 2202, CPU-Generator), positive Frequenz nach der freien Dispersion omega_k =
    sqrt(1 + k^2) (Linearisierung um psi = 0, U'(0) = 1); psi_t = sum (-i omega_k) c e^{ikx}. Statistisch raeumlich
    gleichmaessig.
  - Normierung: Ladung des Bads in der ganzen Box 96 x 96 (Q_box wie in BILDUNG-1) = 0,20 Q_F = 13,323224. Auf dem
    Gitter exakt (rel -1e-16). E/Q des Bads 1,2439, mittleres S 5,9e-4, S_max 0,00483.
  - Grob und fein: dieselbe kontinuierliche Funktion.
  - Kreuzterm Ball/Bad bei t = 0: Q_box(B) = 80,4933 statt 79,9393 (rel +6,9e-3, also +0,55 Ladung).
  - **K-Arm B0 (Karte):** exakter Familienball 0,60 (Profil aus kf_eich) plus dasselbe Bad. K-Pruefung des Balls wie
    BILDUNG-1 (bestanden).
  - **Zusatz BAD [Festlegung BILDUNG-2]:** das Bad allein, beschreibend: Wie viel Bad ist zu welcher Zeit noch im
    ungedaempften Inneren?
- **Arm C (Verschmelzen):** zwei Klumpen (i) bei 0,60 bei (-4,611220, 0) und (+4,611220, 0), Mittenabstand 3 R_F =
  9,222439, gleichphasig, ruhend. **[Festlegung BILDUNG-2]:** einfache Ueberlagerung psi = psi_1 + psi_2.
  - Wegen der Interferenz im Ueberlapp ist Q = 2 Q_F (1 + e^{-9/4}) = 147,274813 = 2,2108 Q_F (Gitter = analytisch,
    rel 0). E 122,9067, E/Q 0,8345.
  - **Vorab-Befund:** In der Mitte ist S = (2 A e^{-9/8})^2 = 0,61062 > 0,6. Die Hauptmaske ist bei t = 0 durch eine
    duenne Bruecke verbunden (Gebietszahl(0) = 1). Deshalb die Verschmelzungsregel in Abschnitt 5.
- **K-Pruefung (Gate je Lauf bei t = 0, sonst keine Zeitentwicklung):** Klumpen: Q auf 1e-3 gegen Q_F und r_rms gegen s
  (je Klumpen einzeln). Ball: Q, E, omega_gitter auf 1e-3 gegen die Familie. Bad: Q auf 1e-3 gegen 0,2 Q_F. C: Q der
  Summe auf 1e-3 gegen die analytische Formel. Im Rauchlauf alle bestanden (beide Gitter, beide Boxen).

## 4. Klassifikator, Hintergrund, Box

- **Wie der Klassifikator den Hintergrund behandelt (vorab, Pflicht):**
  - Maske S >= 2 S0. Das Bad hat S_max 0,00483, erzeugt also bei beiden Schwellen (0,6 und 0,2) keine Komponente.
  - Q und E je Tropfen: Scheibe R_A + 6 um den Schwerpunkt (Pixel zum naechsten Zentrum). Hintergrund = Median von rho
    bzw. e ausserhalb aller Scheiben mal Scheibenflaeche, abgezogen (Q_net, E_net). Im Bad schaetzt der Median die
    mittlere Baddichte; ein Bad, das an der Scheibe anders ist als aussen, verfaelscht Q_net.
  - omega aus der Phasendrehung von arg(sum S psi) im Kern (Gewicht S). Badwellen mit omega_k 1,03 bis 1,41 im Kern
    stoeren die Phase (Amplitudenverhaeltnis etwa 0,025). Das kann u vergroessern ("unentschieden").
  - Q-Schwankung > 20 % im Fenster, Sprung > 2 ("verloren") oder Naehe zu einem anderen Tropfen ("Stoss") geben
    "gestoert".
  - Der Klassifikator ist im Bad nicht geeicht. Dafuer ist B0 da (C0).
- **Bad und Absorber (Grenze, vorab, aus dem Rauchlauf):** Der Absorber von BILDUNG-1 (bindend) nimmt auch das Bad.
  - BAD, grob: Q_box 1 / 0,49 / 0,44 / 0,39 / 0,34 / 0,30 / 0,26 bei t = 0 / 10 / 20 / 30 / 40 / 50 / 60.
  - Im Kreis r <= 32: 0,32 / 0,33 / 0,31 / 0,28 / 0,25 / 0,22 / 0,18.
  - Das Bad wirkt also vor allem in der Bildungsphase (bis etwa t = 100). Bei T = 500 ist es fast weg. Arm B prueft
    damit "Bad waehrend der Bildung", nicht "dauerndes Bad" wie in KF-5. Die Badparameter wurden vor dem Rauchlauf im
    Code festgelegt und danach nicht geaendert.
- **Box-Pruefung (Regel wie BILDUNG-1):** Je Lauf (Gitter, Fall) liegt die Maske S >= 0,6 zu allen Diagnosezeiten (alle
  10, 0 bis 1000) innerhalb max(|x|, |y|) <= innen - 8: 24 (Box 96), 40 (Box 128). Fehlt die Reihe bis 1000 oder ist
  das verletzt, ist die betroffene Vorhersage "offen (Box)". Berichtet: Q_box/Q0, Rahmenladung, Ringe (Box 96: r <= 6,
  12, 20, 32; Box 128: r <= 12, 24, 32, 48), Ausdehnung der Masken 0,6 / 0,2 / 1e-4 / 1e-6.

## 5. Zeitentwicklung, Urteile, Gebietszahl [Festlegung BILDUNG-2, wo nicht Karte]

- **Fenster [T - 40, T]** wie BILDUNG-1: T = 50, 100, 200, 250, 500, 1000. Die Karte entscheidet an 100, 250, 500,
  1000; 50 und 200 sind beschreibend, ausser fuer C0 ("bleibt bis 1000") und C3 ("bevor einer auf ist").
- Je Fenster wie BILDUNG-1: analyse_arm am Fensterbeginn, fenster_probe alle 1, fenster_auswerten.
  - Ball = der Fenstertropfen, der am naechsten an (0, 0) startet, hoechstens 5 entfernt; sonst "kein Tropfen".
  - Fuer C wird zusaetzlich jeder Fenstertropfen gespeichert (Ort, Klasse, rund, Q, omega, u, E/Q, Q-Schwankung,
    Stoss, verloren).
- **S0:** Hauptauswertung S0 = 0,3 (Maske 0,6) entscheidet. Zusatz S0 = 0,1 (Maske 0,2), getrennt berichtet,
  entscheidet nichts.
- **Rohgroessen je Fall, Gitter, Zeit:** Urteil; rund (rmax/R_A); Q-Anteil = Q_net / Q_F (Klumpen und Ball) und
  Q_net / Q0 (Q0 = Q_box bei t = 0, mit Bad bzw. beiden Klumpen); Q(r <= 12 bzw. 24)/Q_F am Fensterbeginn; omega_ruhe
  +- u; E/Q und (E/Q)_fam(Q); Abstandsmasse dQ*, E/Q-Abstand, omega-Abstand (wie Runde 20/21); Q-Schwankung; v.
- **Gebietszahl:** alle 1 von t = 0 bis 100, danach alle 10 bis 1000 (umfasst die Auswertezeiten), in jedem Lauf.
  - Maske = die Klassifikator-Maske S >= 0,6 (Haupt) bzw. 0,2 (Zusatz), periodische 4-Nachbar-Komponenten
    (kf5_geburt.komponenten), gezaehlt mit Flaeche >= 2 (A_MIN). Die Runde-5-Maske (geglaettet) ist nicht verwendet:
    Ihr Code liegt nicht in den erlaubten Dateien; die Karte erlaubt die Klassifikator-Maske.
  - Je Gebiet: Flaeche, R_A, Schwerpunkt, rmax/R_A, Q in der Maske, S_max.
  - **verschmolzen** (Probe) = Gebietszahl 1 (Hauptmaske) UND dieses Gebiet rund (rmax/R_A <= 1,3, das Rund-Kriterium
    des Klassifikators) UND Schwerpunkt hoechstens 2 von der Mitte (0, 0). Grund: Bei t = 0 ist die Gebietszahl schon 1
    (Bruecke, Abschnitt 3); zwei verbundene Lappen haben rmax/R_A um 1,8.
  - **t_m** = erste Probe, ab der "verschmolzen" bei allen spaeteren Proben bis 1000 gilt (dauerhaftes Verschmelzen).

## 6. Vorhersagen (Karte) und Regeln (S0 = 0,3)

| Nr | Karte | Wahrsch. | Regel |
|---|---|---|---|
| C0 | K-Arm B0: exakter Ball im Bad bleibt bis T = 1000 "auf" | 60 % | B0 zu allen sechs Fensterenden (50, 100, 200, 250, 500, 1000), beide Gitter: 12 Urteile. Eingetroffen, wenn alle "auf" ("auf" schliesst rund ein); nicht eingetroffen, wenn eines fehlt; offen, wenn Laeufe fehlen oder Box-Pruefung scheitert |
| C1 | A: "auf" und rund bei T = 500, beide Gitter | 55 % | 2 Urteile (A, T = 500), beide "auf" und rund; sonst nicht eingetroffen |
| C2 | B: "auf" und rund bei T = 500, beide Gitter (nur wertbar bei C0) | 50 % | 2 Urteile (B, T = 500), beide "auf" und rund. Ist C0 nicht eingetroffen oder offen: "offen", der Rohausgang wird mitgeteilt |
| C3 | C: verschmelzen (Gebietszahl 1), bevor einer "auf" ist | 55 % | Je Gitter erfuellt, wenn t_m existiert und kein Fenster mit >= 2 Fenstertropfen, darunter einer "auf" und rund, vor t_m beginnt (T - 40 < t_m). Beide Gitter erfuellt: eingetroffen; beide nicht: nicht eingetroffen; uneinig: offen (L3) |
| C4 | C: das verschmolzene Gebilde ist bei T = 1000 "auf" und rund | 35 % | Je Gitter: t_m existiert und der Ball (Tropfen naechst (0, 0), <= 5) bei T = 1000 ist "auf". Beide ja: eingetroffen; beide nein: nicht eingetroffen; uneinig: offen. Ohne t_m auf einem Gitter: "offen (kein Verschmelzen)" |

- Box-Pruefung: C0 braucht B0, C1 A, C2 B, C3/C4 C auf beiden Gittern, sonst "offen (Box)".
- **Bedeutung (Karte, mechanisch; alle zutreffenden Zeilen werden genannt):**
  - C1 und C2 eingetroffen, C4 nicht eingetroffen: Groesse und Bad hindern die Bildung nicht; das "nie auf" in KF-5
    lag am Verschmelzen [H].
  - C1 nicht eingetroffen: Grosse, duennwandige Klumpen erreichen die Familie langsamer oder gar nicht.
  - C2 nicht eingetroffen (bei C0): Das Wellenbad hindert die Bildung.
  - C0 nicht eingetroffen: Der Klassifikator taugt im Bad nicht; Arm B bleibt offen.
  - Sonst: Die Karte nennt keine Bedeutung. Ich berichte beschreibend und deute nicht.
- **Schreibtischrechnung (koennen C0 bis C4 scheitern und bestehen?):**
  - C0: Der exakte Ball ist im Vakuum "auf" (BILDUNG-1, KF-EICH). Im Bad koennen Phasenrauschen (u) oder ein falscher
    Hintergrund (Median) bei T = 50 bis 100 stoeren. Spaeter ist das Bad fast weg (Abschnitt 4). Beide Ausgaenge
    moeglich, bei 50/100 am ehesten Scheitern.
  - C1: Bei 0,52 ist die Familie sehr steil: 10 % in Q entsprechen nur etwa 6e-4 in omega (KF-EICH: "engste Stelle").
    Der Klumpen startet mit S_max 2,0 statt 1,02 und E/Q 12,4 % ueber der Familie; er muss stark umbauen und
    abstrahlen. Ein Atmen mit u > 6e-4 gibt "unentschieden". Beide Ausgaenge moeglich.
  - C2: Das Bad ist schwach (Amplitude etwa 2,5 % des Kerns) und fluechtig. BILDUNG-1 (i) war schon ab T = 50 "auf".
    Scheitern nur, wenn das Bad den Klumpen in der Bildungsphase dauerhaft stoert (Drift, Atmen) oder der Klassifikator
    stolpert. Eher Eintreffen; der Test ist schwach (Grenze).
  - C3: Gleichphasige Klumpen ziehen sich an; die Bruecke (S 0,611 knapp ueber 0,6) kann sofort zum Verschmelzen fuehren
    oder abreissen, wenn sich die Klumpen zusammenziehen. Ein Einzelklumpen war in BILDUNG-1 schon in [10, 50] "auf".
    Beide Ausgaenge moeglich.
  - C4: Das Gebilde hat Q 2,21 Q_F (Familienpunkt etwa omega^2 0,565) und E/Q etwa 4 % ueber der Familie; Verschmelzen
    regt Schwingungen an. Beide Ausgaenge moeglich. Ohne Verschmelzen ist C4 offen.
  - Keine Regel steht vorab fest.

## 7. Aufrufe (kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde22-bildung-2)

```
Spur p4000a:
bash .../kleintest.sh p4000a b2-grob-bc  bildung2.py lauf --stufe grob --gruppe bc --von 0 --bis 1000
bash .../kleintest.sh p4000a b2-grob-a   bildung2.py lauf --stufe grob --gruppe a  --von 0 --bis 1000
bash .../kleintest.sh p4000a b2-fein-a1  bildung2.py lauf --stufe fein --gruppe a  --von 0 --bis 500
bash .../kleintest.sh p4000a b2-fein-a2  bildung2.py lauf --stufe fein --gruppe a  --von 500 --bis 1000
Spur p4000b (Lock regelt die Belegung):
bash .../kleintest.sh p4000b b2-fein-bc1 bildung2.py lauf --stufe fein --gruppe bc --von 0 --bis 500
bash .../kleintest.sh p4000b b2-fein-bc2 bildung2.py lauf --stufe fein --gruppe bc --von 500 --bis 1000
Danach:
bash .../kleintest.sh p4000a b2-zusammen bildung2.py zusammen --geraet cpu
```

- Gruppen: a = A, KA (Box 128); bc = B0, B, BAD, C (Box 96).
- Zwischenspeicher (nur .69): lauf-69/zwischen/fein_<gruppe>_t500.pt. Keine Abschnittsgrenze schneidet ein Fenster
  (Pruefung im Code; im Rauchlauf 0 -> 30 -> 60 geprueft).
- Laufzeit (Rauchlauf, ms je Schritt): grob bc 3,2 (B 4), grob a 2,8 (B 2), fein bc 12,8 (B 4), fein a 11,0 (B 2).
  Geschaetzt: grob je etwa 100 s, fein je Abschnitt etwa 300 bis 370 s. Zeitgrenze im Code 560 s (Prognose nach 400
  Schritten); bei Ueberschreitung wird der Abschnitt geteilt (0 -> 250 -> 500 usw.) und das vermerkt.
- Faellt p4000b aus oder ist lange belegt, laufen die fein-bc-Abschnitte nach den a-Laeufen auf p4000a.

## 8. Latten (v3) und Grenzen (vorab)

- **L1 kann scheitern:** ja, C0 bis C4 haben beide Ausgaenge (Abschnitt 6).
- **L2 Gegenprobe:** B0 (Karte), KA (exakter Ball 0,52 in Box 128), BAD (Bad allein), K-Pruefungen, Absorber bitgleich
  mit BILDUNG-1, zwei Schwellen, zweites Ladungsmass Q(r <= R) am Fensterbeginn.
- **L3 Numerik:** grob gegen fein mit identischer kontinuierlicher Anfangsfunktion (auch das Bad).
- **L4 schon bekannt:** Q-Ball-Relaxation, Verschmelzen gleichphasiger Q-Baelle und Q-Baelle in thermischen Baedern
  sind allgemein in der Literatur bekannt [L, nicht nachgeprueft, keine Literaturabfrage]. Neu ist nur der Befund fuer
  M1 in 2D mit diesem Klassifikator.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter).
- **Grenzen:**
  - Je Arm ein Startzustand, ein Familienpunkt, eine Saat. Symmetrische Starts (A, C) brechen die Symmetrie nur durch
    Rundungsfehler (B durch das Bad).
  - Bad: schwach (0,2 Q_F in der ganzen Box) und durch den Absorber fluechtig (Abschnitt 4). Ein dauerndes, dichtes Bad
    wie in KF-5 ist nicht geprueft.
  - C: Mittenabstand 3 R_F mit Gauss-Breite s = R_F ist eng; die Klumpen ueberlappen (Interferenzladung +10,5 %).
  - "auf" heisst nur "Q passt zu omega" (Runde 21); E/Q wird mitberichtet.

## 9. Was nicht geaendert wird

- Vorhersagen, Wahrscheinlichkeiten und Bedeutung: Karte, unveraendert.
- Nach dem Einfrieren keine Aenderung an bildung2.py, Regeln oder Parametern. Nachtraege nur in einer neuen eingefrorenen
  Fassung, als nachtraeglich markiert.

## 10. Hilfsdateien

- hilfs/ (nur Darstellung, nach den Laeufen): jq-Filter fuer die Tabellen.

## 11. Rauchlauf (vor dem Einfrieren)

- 2026-10-02 19:42:44 bis 19:44:00 CEST, Spur p4000a, rc = 0 ueberall:
  - grob bc 0 -> 30 und 30 -> 60 mit Zwischenspeicher (prueft das Abschnittsverfahren), Fenster 4 bei T = 8, 16, 40.
  - fein a 0 -> 10, fein bc 0 -> 10, grob a 0 -> 10.
- Gemessen: Radiuswahl, K-Pruefungen (Abschnitt 3), Dauern, GPU 104 bis 137 MB (grob) / 520 bis 531 MB (fein), die
  Diagnosereihe (nur Q_box und Rahmen je Fall, fuer BAD dazu r <= 32 und die Front).
- Die Fenstereintraege und Gebietsproben wurden gerechnet, aber nicht ausgegeben (nur gezaehlt).
- **Selbstanzeige:** Die Diagnosereihe zeigte vor dem Einfrieren Q_box(t) fuer B0, B und C bis t = 60 (z. B. C:
  0,9956 bei t = 60; B0/B: 0,878 / 0,875 bei t = 60, vor allem Badverlust). Vorhersagen stammen aus der Karte und
  bleiben unveraendert. Aus dem Rauchlauf folgen nur die Laufzeiten und der Vermerk zum Badverlust (Abschnitt 4).
- Dateien: lauf-69/RAUCH-*.log, Rauch-JSON in lauf-69/rauch/.

## 12. Stand beim Einfrieren

Siehe die letzte Zeile (sha256 von bildung2.py, lokal = .69, py_compile auf der .69 ok).

Eingefroren 2026-10-02 19:46:44 CEST (date), vor jedem echten Lauf. bildung2.py sha256 f1bc80b4d86743e4190a5d719089a180ada8bc4de1a51a52465ae0d97bfb8f90 (lokal = .69, py_compile auf der .69 ok).
