# KF-EICH (Runde 21): Plan

Bearbeiter: Code-Agent (Claude, Anthropic), Auftrag der Leitung claude-primary. Beginn 2026-10-02 18:20:58 CEST (date).
Plan geschrieben ab 18:41:21 CEST (date), nach dem Rauchlauf (Abschnitt 9) und vor jedem echten Lauf. Explorativ (v3),
Hypothesen [H]. Karte: KARTE.md daneben; die Vorhersagen E0 bis E3 und die Bedeutung stehen dort und werden hier nur
mechanisch umgesetzt. Was ich selbst festlege (nicht in der Karte), ist mit **[Festlegung KF-EICH]** markiert.

## 1. Frage

Kann der unveraenderte Klassifikator aus Runde 6 "auf" sagen, wenn ein Objekt sicher auf der Q(omega)-Familie liegt? Dazu
werden einzelne exakte Familien-Q-Baelle (m = 0) auf das Runde-6-Gitter gesetzt und bis T = 200 entwickelt.

## 2. Original geprueft

- kf5_geburt.py sha256 9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0 und familie_2d_m0.json sha256
  f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806, lokal (RUNDE-06/kf5) und auf der .69
  (/home/fmh/fmhc-physics-remote/runde6-kf5) gleich.
- kf_eich.py importiert kf5_geburt.py von dort (nur gelesen, ohne Bytecode) und ruft unveraendert auf: Gitter, kraft_fn,
  dichten, analyse_arm, fenster_start, fenster_probe, fenster_auswerten (darin familien_klasse), Familie, Konstanten
  (STUFEN, BOX0 = 96, FENSTER = 40, DT_FENSTER = 1, FAKTOREN 2/3, A_MIN 2, KOMPAKT 2, KOMPAKT_FAMILIE 1,3, R_PLUS 6,
  R_SUCH 2, FAM_TOL 0,10, Q_SCHWANK 0,20).
- Die Verlet-Schleife steckt in kf5_geburt.lauf() und ist nicht einzeln aufrufbar. Sie ist Zeile fuer Zeile nachgebaut,
  wie in Runde 20.
- Die Familiendatei enthaelt keine Profile (nur omega^2, Q, E, virial, r_ladung, f_max). kf5_geburt.py hat keinen
  Profilloeser. Daher das Schiessverfahren in Abschnitt 4.

## 3. Baelle, Gitter, Platzierung [Festlegung KF-EICH, wo nicht Karte]

- Gitter wie Runde 6: Box 96 (periodisch, [-48, 48)^2), grob dx 0,25 / dt 0,04 (n 384), fein dx 0,125 / dt 0,02 (n 768).
- **Satz E (exakt), drei Knoten der Familiendatei:**

  | Ball | omega^2 | omega | Q_fam | E_fam | Rolle | Radius S = 0,6 / S = 0,2 (Profil) |
  |---|---|---|---|---|---|---|
  | E52 | 0,52 | 0,72111 | 1421,45 | 1045,95 | im Bereich der R6/R20-Tropfen (omega 0,72 bis 0,73, Q dort 1300 bis 2100) | 17,25 / 18,48 |
  | E60 | 0,60 | 0,77460 | 66,616 | 56,527 | Karte "z. B. 0,60" | 3,19 / 4,36 |
  | E70 | 0,70 | 0,83666 | 23,996 | 22,626 | Karte "z. B. 0,70" | 1,40 / 2,72 |

  - Je ein Lauf ruhend ("r") und einer bewegt ("b", v = 0,05 in +x).
  - E52 statt 0,53 (omega 0,7280, Q 641): 0,52 trifft omega und Q der R6/R20-Tropfen zugleich.
- **Satz A (angeregt):** dieselben drei Profile, nur ruhend, Amplitude x 1,05 auf psi und psi_t (Karte nennt fuer A keine
  Bewegung). Damit Q = 1,1025 Q_fam(omega_set) bei T = 0.
- **Setzen:** Mitte (0, 0), ein Ball je Box (Stapel von unabhaengigen Boxen, B = Zahl der Baelle im Aufruf).
  - ruhend: psi = A f(r), psi_t = -i omega A f(r) (Phase e^{-i omega t} wie kf5_geburt: psi_t = -i omega psi).
  - bewegt: Lorentz-Boost (die Gleichung ist Lorentz-invariant), bei t = 0:
    psi = f(r') e^{i omega gamma v x}, r' = sqrt((gamma x)^2 + y^2),
    psi_t = (-gamma^2 v x f'(r')/r' - i omega gamma f(r')) e^{i omega gamma v x}.
  - Abstand zu den Raendern: E52 reicht bis r etwa 18,5 (S = 0,2), Abstand zum Boxrand also etwa 29. Der bewegte Ball
    laeuft von x = -2 (t = -40) bis x = +10 (t = 200). Profil am Boxrand (r 48) bei E70 unter 1e-14, Bildladungen
    periodisch vernachlaessigbar.

## 4. Profil und K-Pruefung

- **Schiessverfahren:** f'' + f'/r = (1 - omega^2 - 2 f^2 + 1,5 f^4) f, f'(0) = 0, f -> 0.
  - RK4, Schritt 0,005; Reihenstart bei r = 0,005 (bis r^4).
  - Bisektion auf f(0) zwischen W(S) = 0 (S = 1 - sqrt(2 omega^2 - 1), Unterschwinger) und dem Maximum von W
    (Ueberschwinger), bis ein Lauf monoton f < 1e-7 erreicht.
  - Sonst weitere Stufen mit Bisektion auf f' an der letzten Stelle, an der beide Klammerlaeufe auf 1e-9 uebereinstimmen.
    Im Rauchlauf reichte ueberall eine Stufe.
  - Jenseits von f < 1e-7 die asymptotische K0-Form.
  - Auf das Gitter kubisch nach Hermite (f, f').
  - Rechenort: skalar in Python auf der .69, 0,5 s je Aufruf, Vorbereitung. Alle 2D-Rechnungen auf CUDA.
- **K-Pruefung** (je Aufruf bei t = 0 auf dem Gitter, Summen wie dichten). Q, E (bewegt: E/gamma) und omega gegen die
  Familiendatei.
  - omega = Wurzel des Rayleigh-Quotienten <f, -Lap f + U'(f^2) f> / <f, f> der Gittergleichung fuer das Ruheprofil.
  - Satz E muss in allen drei Groessen auf 1e-3 stimmen. Sonst bricht der Aufruf vor der Zeitentwicklung ab (Gate), und
    es gibt kein Urteil.
  - Satz A wird nur berichtet (erwartet Q/Q_fam = 1,1025).
- **Ergebnis der K-Pruefung im Rauchlauf** (Setup, kein Klassifikatorurteil):

  | Ball | dQ rel | dE rel | domega rel | Residuum (Zusatz) |
  |---|---|---|---|---|
  | E52 | +2,9e-6 | +2,9e-6 | -6e-11 (grob) / -3e-11 (fein) | 2,5e-4 / 3,7e-4 |
  | E60 | +7e-8 | +7e-8 | -5e-11 / -2e-11 | 2,0e-4 / 3,0e-4 |
  | E70 | -3,6e-6 | -3,0e-6 | -3e-9 / -2e-9 | 1,9e-3 / 2,7e-3 |

  - Bewegte Baelle: gleiche dQ und dE/gamma auf 1e-7.
  - Das Residuum |(-Lap + U') f - omega^2 f| / |omega^2 f| ist ein Zusatz, kein K-Kriterium. Es waechst von grob zu fein
    um etwa den Faktor sqrt(2) und steht fast senkrecht auf f (omega aus dem Rayleigh-Quotienten auf 1e-9). Die Ursache
    ist nicht gefunden; Grenze in Abschnitt 8.

## 5. Zeitentwicklung und Urteile [Festlegung KF-EICH]

- **Verlet** wie kf5_geburt.lauf(): F = kraft(psi); vel += F dt/2; psi += vel dt; F = kraft(psi); vel += F dt/2.
- **"Urteil zu T" = Messfenster [T - 40, T]**, wie in Runde 6 ("bei T = 800" = [760, 800]) und Runde 20.
  - Fenster: [-40, 0], [10, 50], [60, 100], [160, 200].
  - Fuer T = 0 rechnet derselbe Verlet mit -dt von 0 nach -40 zurueck. Dann laeuft er vorwaerts durchgehend von -40 bis
    200. Die Entwicklung nach vorn endet bei T = 200 (Karte).
  - Fuer ruhende Baelle ist [-40, 0] wegen psi(-t) = conj(psi(t)) das Spiegelbild von [0, 40]. Fuer bewegte gilt das mit
    -v.
- **Je Fenster und Ball** genau wie in Runde 6:
  - analyse_arm am Fensterbeginn (alt = None; Verschmelzungsdiagnose ohne Bedeutung).
  - fenster_start mit dessen Tropfen; fenster_probe alle 1 (41 Proben); fenster_auswerten(fzs, T - 40, 1, fam, box).
- **Ball-Tropfen:** der Fenstertropfen, dessen Startort (x0, y0) dem Sollort (v (T - 40), 0) am naechsten liegt, hoechstens
  5 entfernt. Gibt es keinen: Klasse "kein Tropfen".
- **Urteil je Ball** = die Klasse aus fenster_auswerten ("auf", "neben", "unentschieden", "ausserhalb", "gestoert",
  "nicht rund"). "rund" = rmax/R_A <= 1,3 am Fensterbeginn.
  - Das Armurteil (familien_urteil) braucht mindestens 5 entscheidbare Tropfen. Mit einem Ball je Box ist es immer "nicht
    entscheidbar". Es wird berichtet, geht aber nicht in E0 bis E3 ein.
- **S0:** Der Klassifikator setzt Schwellen relativ zu S0 des Arms.
  - Hauptauswertung S0 = 0,3 (Arm s03, Schwelle S >= 0,6). Daher kamen die Tropfen mit omega 0,72 bis 0,73. Sie
    entscheidet E0 bis E3 und die Bedeutung.
  - Zusatz S0 = 0,1 (Arm s01, Schwelle 0,2), dieselben Laeufe und Regeln, getrennt berichtet. Er entscheidet nichts.
- **Rohgroessen je Ball, Lauf und Zeit:** Q_net, Q_roh, E_ruhe_net, E/Q und (E/Q)_fam(Q), omega_rot, omega_ruhe +- u,
  omega_geo, v_mess, Rundheit rmax/R_A, Maskenflaeche, S_max, Q-Schwankung, verloren/stoss.
- **Abstandsmasse wie Runde 20:**
  - dQ* = Q_net / Q_fam(omega_ruhe) - 1
  - E/Q-Abstand = (E/Q) / (E/Q)_fam(Q) - 1
  - omega-Abstand = omega_ruhe - omega_fam(Q)
- **Abstandsmasse, Zusatz:**
  - d_set = Q_net / Q_fam(omega_set) - 1
  - domega_set = omega_ruhe - omega_set

## 6. Vorhersagen (Karte) und Regeln

| Nr | Karte | Wahrsch. | Regel (S0 = 0,3) |
|---|---|---|---|
| E0 | Satz E ruhend: alle Baelle zu allen Zeiten "rund" und "auf", beide Gitter | 55 % | 3 Baelle x 4 Zeiten x 2 Gitter = 24 Urteile; eingetroffen, wenn alle 24 "auf" und rund; nicht eingetroffen, wenn eines fehlt; offen, wenn Laeufe fehlen |
| E1 | Satz E bewegt: ebenfalls "auf" | 45 % | dasselbe fuer die drei bewegten Baelle (24 Urteile) |
| E2 | Satz A: zu T = 0 "neben" oder "unentschieden", nicht "auf" | 60 % | 3 Baelle x T = 0 x 2 Gitter = 6 Urteile; eingetroffen, wenn alle 6 "neben" oder "unentschieden"; nicht eingetroffen, wenn eines "auf"; sonst offen |
| E3 | Scheitert E0: Schwelle oder omega-Messung, nicht die Familiendatei | 70 % | nur wenn E0 nicht eingetroffen (sonst offen, Bedingung nicht erfuellt); Diagnose je fehlgeschlagenem E0-Urteil (unten); eingetroffen, wenn alle Diagnosen "Schwelle" oder "omega-Messung"; sonst nicht eingetroffen |

**Diagnose je E0-Urteil, das nicht "auf" ist [Festlegung KF-EICH], in dieser Reihenfolge:**
1. "kein Tropfen", "nicht rund", "gestoert" -> **Schwelle** (Erkennung, Rundheit 1,3, Q-Schwankung, Sprung, Stoss).
2. "ausserhalb" (omega_ruhe ausserhalb der Tabelle, omega_set liegt drin) -> **omega-Messung**.
3. "neben" oder "unentschieden":
   - |d_set| > 0,10 -> **Q-Messung** (Q_net trifft schon beim Sollwert omega nicht; Scheibe oder Hintergrund).
   - sonst |dQ*| > 0,10 -> **omega-Messung**.
   - sonst (beide innerhalb, das Band aus u reicht ueber 10 %) -> **omega-Messung (Unsicherheit u)**.
- Die Familiendatei selbst ist durch die K-Pruefung gedeckt (Q und E auf 1e-3; an den Knoten interpoliert Familie exakt).
- "Q-Messung" zaehlt nicht als Schwelle oder omega-Messung; dann ist E3 nicht eingetroffen.

**Bedeutung (Karte, mechanisch aus E0 bei S0 = 0,3):**
- E0 eingetroffen: Der Klassifikator kann "auf" sagen. Das "nie auf" der Tropfen in Runde 6 und 20 ist ein Befund.
- E0 nicht eingetroffen: Alle bisherigen "nie auf"-Urteile sind ohne Aussage. Vor jedem weiteren Bildungsversuch wird der
  Klassifikator repariert, KF-5 bleibt geparkt.
- Zusatz S0 = 0,1: wird mit denselben Regeln berichtet. Weicht er ab, sage ich das fuer die s01-Urteile aus Runde 20
  dazu, ohne die Bedeutung zu aendern.

**Schreibtischrechnung (kann E0 scheitern und bestehen?):**
- **Erkennung:** S_max 1,019 / 1,061 / 0,850, alle ueber 0,6. Flaeche der 0,6-Maske bei E70: pi 1,40^2 = 6,2, ueber
  A_MIN = 2. Scheibe R_A + 6 deckt bei E70 bis r etwa 7,4.
- **omega-Band:** bei E52 ist d ln Q_fam / d omega etwa 115. 10 % in Q entsprechen also 0,0009 in omega. "auf" verlangt
  dort |omega_ruhe - 0,72111| und u unter etwa 0,0008.
  - Verlet-Frequenzfehler (omega dt)^2 / 24: grob 3e-5 relativ.
  - Bewegt: Fehlt die gamma-Korrektur, verschiebt sich omega um omega v^2 / 2 = 0,0009, genau an der Grenze (E1).
- **Satz A:** Q = 1,1025 Q_fam(omega_set). Liegt das gemessene omega bei omega_set, ist d = +0,10 und das Urteil haengt
  am Band. Verschiebt die Anregung omega, kann der Ball auch "auf" einem anderen Familienpunkt erscheinen.
- Beide Ausgaenge sind also fuer E0, E1 und E2 moeglich. Keine Regel steht vorab fest.

## 7. Aufrufe (kleintest.sh, Ordner /home/fmh/fmhc-physics-remote/runde21-kf-eich)

```
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kfeich-grob      kf_eich.py lauf --stufe grob --gruppe alle
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b kfeich-fein-er   kf_eich.py lauf --stufe fein --gruppe E-ruhend
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kfeich-fein-eb   kf_eich.py lauf --stufe fein --gruppe E-bewegt
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b kfeich-fein-a    kf_eich.py lauf --stufe fein --gruppe A
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a kfeich-zusammen  kf_eich.py zusammen --geraet cpu
```

- Ausgabe: lauf-69/ausgabe/<stufe>_<gruppe>_ergebnis.json und _bericht.txt; zusammen.json und zusammen.txt; Logs
  lauf-69/LAUF-*.log.
- Laufzeit (Hochrechnung aus dem Rauchlauf): grob alle 91 s; fein je Gruppe (B = 3) etwa 150 s. Jeder Aufruf hat eine
  eigene Zeitgrenze 560 s (Prognose nach 400 Schritten) unter der Systemgrenze 600 s.

## 8. Latten (v3) und Grenzen (vorab)

- **L1 kann scheitern:** ja. E0 bis E2 haben beide Ausgaenge (Abschnitt 6).
- **L2 Gegenprobe:** K-Pruefung gegen die Familiendatei (unabhaengiger Profilcode gegen R4/R3), Rueckkehrfehler, zwei
  Gitter, zwei Schwellen-Arme, Satz A als Negativprobe.
- **L3 Numerik:** grob gegen fein mit identischer kontinuierlicher Anfangsfunktion.
- **L4 schon bekannt:** Q-Ball-Profile und Boosts sind Lehrbuch [L]. Neu ist nur die Eichung dieses Klassifikators.
- **L5 Messbezug:** nein, modellintern (Stufe 5 der Stabilitaetsleiter, Werkzeugpruefung).
- **Grenzen:**
  - Ein Ball je Box im Vakuum. Die Tropfen der Geburt sitzen in einem Wellenbad mit Hintergrund. Die Eichung prueft den
    Klassifikator ohne Bad (Hintergrundabzug nahe null).
  - Das Gittergleichungs-Residuum (Abschnitt 4) zeigt, dass die gesetzten Baelle nicht ganz auf Maschinengenauigkeit
    stationaer sind. Q, E und omega stimmen auf 4e-6.
  - f_max der Familiendatei ist nicht f(0): E70 weicht 1,3e-4 ab, passend zu f bei r = 0,04, dem ersten Gitterpunkt von R4.
    f_max geht nicht in die K-Pruefung ein.
  - Satz A nur ruhend.

## 9. Rauchlauf (vor dem Einfrieren; nur Dauern und K-Pruefung, keine Klassifikatorausgabe)

- 2026-10-02 18:38:17 bis 18:38:30 CEST (Uhr der .69 in UTC: 16:38:17 bis 16:38:30). p4000a: grob alle neun Baelle.
  p4000b: fein E-ruhend. Beide mit Fenster 4 und Zeiten 0 und 8, rc = 0.
- Gemessen:
  - grob: 6,57 ms je Schritt (B = 9), GPU max 226 MB.
  - fein: 8,95 ms je Schritt (B = 3), 330 MB.
  - Profile 0,5 s; Rueckkehrfehler 2e-15 bzw. 2,8e-15.
- Die Rauch-JSON enthalten keine Urteile (lauf-69/rauch/).

## 10. Stand beim Einfrieren

Siehe die letzte Zeile (sha256 von kf_eich.py, lokal = .69, py_compile auf der .69 ok).

Eingefroren 2026-10-02 18:42:39 CEST (date), vor jedem echten Lauf. kf_eich.py sha256 332f3293a94448848beeb1c90a58ba9128d14e4f5029983832a8ea7a77eacb59 (lokal = .69, py_compile auf der .69 ok).
