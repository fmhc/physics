# PEITSCHE-1, Plan des Code-Agenten (Runde 35)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-03 20:48:23 CEST (date). Plan geschrieben ab 21:08 CEST,
  nach den Rauchlaeufen (Abschnitt R). Karte: KARTE.md daneben; ihre Vorhersagen und Schwellen gelten unveraendert.
- Explorativ (v3). Alle Rechnungen synthetisch; keine Messdatenbestaetigung.
- Rechenort: .69, Ordner /home/fmh/fmhc-physics-remote/runde35-peitsche/, nur ueber kleintest.sh (Spuren p4000a fuer Teil A,
  cpu fuer Teil B und die Auswertung). Python /home/fmh/fmhc-physics-gpu-venv (torch 2.5.1+cu121, numpy 2.4.4), float64.
- Code: code/peitsche_a.py (Teil A), code/peitsche_b.py (Teil B), code/regge2d.py (RG-1, unveraendert,
  sha256 7e7f6667...892608 wie RUNDE-06/regge/regge2d.py), code/auswertung.py (Urteile). Hashes beim Einfrieren unten.
- Kennzeichnung: Festlegungen, die die Karte offenlaesst, sind mit **[P]** markiert (Plan-Festlegung des Code-Agenten).

## A. Teil A: radiale phi^4-Wand

### A.1 Loeser

- Gleichung phi_tt = phi_rr + (d-1)/r phi_r - (phi^3 - phi), V = (phi^2 - 1)^2/4. Anfang phi = tanh((r - R0)/sqrt 2),
  phi_t = 0.
- **[P] Ort:** Finite-Volumen auf versetztem Gitter, Zellmitten r_i = (i + 1/2) dr, Flaechen r_f = (i+1) dr, Zellmass
  W_i = (r_{i+1/2}^d - r_{i-1/2}^d)/d (exakt, damit der Laplace bei r = 0 konsistent ist). Bei r = 0 kein Fluss
  (regulaer, keine Division durch r). Das halbdiskrete System ist hamiltonsch mit
  E = Omega_d [sum W_i (p_i^2/2 + V(phi_i)) + sum_f r_f^(d-1) (phi_{i+1} - phi_i)^2/(2 dr)], Omega_2 = 2 pi,
  Omega_3 = 4 pi.
- **[P] Zeit:** Yoshida/Forest-Ruth, 4. Ordnung, symplektisch, dt = 0,4 dr. Auf der GPU je Ausgabeblock ein CUDA-Graph
  (gleiche Rechnung; Rauchlauf: bitgleiche Zusammenfassung mit und ohne Graph).
- **[P] Rand:** reflektierend (kein Fluss) bei r_max = max(R0 + t_end/2, (t_end + R0 + 10)/2) + 20. Damit kommt vor
  t_end nichts vom Rand in r < R0 (kurze Laeufe) bzw. in r < 10 (lange Laeufe) zurueck; die Energie bleibt eine
  Erhaltungsgroesse des Gitters. Kein Absorber.
- **[P] Laufende:** t_end = t_c(duenn) + 10 (kurz) bzw. t_c(duenn) + 505 (lang, damit das Fenster bis t_c + 500 auch bei
  etwas spaeterem t_c ganz drin liegt).
- **[P] Ausgaben:** alle n_aus = round(0,02/dt) Schritte (Abstand 0,0196 bei d = 2, 0,02016 bei d = 3).

### A.2 Messvorschriften (alle in peitsche_a.py, Funktion zusammenfassen)

- **phi_c(t)** = (9 phi_0 - phi_1)/8 (Ursprungswert, gerade Extrapolation aus den zwei innersten Zellen).
- **t_c:** erste Ausgabe mit phi_c >= 0 nach phi_c < 0, linear zwischen den beiden Ausgaben interpoliert.
- **R(t):** wenn phi_0 < 0: innerste Nullstelle (erster Wechsel von phi < 0 nach phi >= 0 von innen), linear zwischen
  den Zellmitten interpoliert. Wenn phi_0 >= 0: R = 0 (zusammengefallen bzw. Ursprung aussen).
- **Wandschnelle v_k** (einwaerts positiv) = -(R_{k+1} - R_{k-1})/(t_{k+1} - t_{k-1}), nur fuer t_{k+1} < t_c und
  R_{k-1}, R_k, R_{k+1} > 0.
- **v bei R = R0/2, R0/4, R0/10:** erstes Unterschreiten vor t_c, v linear in R zwischen den Nachbarausgaben
  interpoliert. Sollwert v_duenn = sqrt(1 - (R/R0)^2) (d = 2) bzw. sqrt(1 - (R/R0)^4) (d = 3).
- **Groesste Wandschnelle fuer R >= 2:** max v_k ueber k mit R_{k-1}, R_k, R_{k+1} >= 2 (vor t_c).
- **Musterschnelle (A4):** max |R_{k+1} - R_k|/(t_{k+1} - t_k) ueber alle Paare aufeinanderfolgender Ausgaben mit
  t_c - 1 <= t_k und t_{k+1} <= t_c + 1 (R = 0 bei phi_0 >= 0, siehe oben). **[P]** Fenster +-1 (stand schon in der
  ersten, vor allen Rauchlaeufen hochgeladenen Fassung von peitsche_a.py, sha256 6a139e9a...).
  Beschreibend dazu die Momentanschnelle -phi_t/phi_r an der Nullstelle.
- **A0-Groessen:** max |E(t)/E(0) - 1| ueber alle Ausgaben mit t <= t_c; max |T^0r|/T^00 ueber alle Zellen und alle
  Ausgabezeiten, mit T^0r = -phi_t phi_r und T^00 = phi_t^2/2 + phi_r^2/2 + V an den Zellmitten, phi_r zentral.
  **[P]** "jederzeit" heisst an allen Ausgabezeiten (alle ~0,02), nicht nach jedem Zeitschritt.
- **Nachlauf (lange Laeufe):** E(r < 10) gemittelt ueber t_c + 490 bis t_c + 500, geteilt durch E(0). Frequenz am Ursprung:
  phi_c(t) auf t_c + 400 bis t_c + 500, Mittel abgezogen, Hann-Fenster, FFT mit 8-facher Nullauffuellung, Kreisfrequenz
  des hoechsten Gipfels (parabolisch verfeinert; Aufloesung 2 pi/100 = 0,063). Beschreibend: dieselbe Frequenz in
  frueheren Fenstern, Mittelwert und Amplitude von phi_c, erstes Wiedereintauchen phi_c < 0 nach t_c (Rueckprall).
- **Beschreibend (kein Urteil):** Verhaeltnis |T^0r|/T^00 nur im energietragenden Bereich (T^00 >= 1e-3 max T^00,
  "Wand") und energiegewichtetes Mittel sum W |T^0r| / sum W T^00, je Ausgabezeit.

### A.3 Laeufe und Gitter

| Lauf | d | R0 | dr fein (urteilt) | dr grob (Konvergenz) | Laufende | Spur |
|---|---|---|---|---|---|---|
| a_d2_R80 | 2 | 80 | 0,0035 | 0,007 | t_c + 10 | p4000a |
| a_d2_R40 | 2 | 40 | 0,0035 | 0,007 | t_c + 10 | p4000a |
| a_d2_R20 | 2 | 20 | 0,0035 | 0,007 | t_c + 505 | p4000a |
| a_d3_R40 | 3 | 40 | 0,0014 | 0,0028 | t_c + 10 | p4000a |
| a_d3_R20 | 3 | 20 | 0,0014 | 0,0028 | t_c + 505 | p4000a |

- **Aufloesung (Karte: dr <= sqrt(2) R/(5 R0) fuer die gemessenen R):**
  - d = 2: R0/10 verlangt dr <= 0,0283; A3 (R0 = 80, R >= 2) verlangt dr <= 0,00707. Fein 0,0035 und grob 0,007
    erfuellen beides.
  - d = 3: Die verkuerzte Dicke ist dort sqrt(2) (R/R0)^2 (gamma = (R0/R)^2), nicht sqrt(2) R/R0. **[P]** Ich wende
    die d = 3-Fassung an: R0/10 verlangt dr <= sqrt(2)/500 = 0,00283. Fein 0,0014 und grob 0,0028 erfuellen sie
    (die Kartenformel fuer d = 2 waere 0,0283, also schwaecher).
  - Unterhalb von R ~ 1 (d = 2, R0 = 80: Dicke 0,018) bzw. R ~ 4 (d = 3, R0 = 40) ist die Wand auf dem feinen Gitter
    nur noch mit weniger als 5 Punkten aufgeloest; das betrifft nur die Musterschnelle (A4) und den Nachlauf.
- **[P] Nachlauf** bis t_c + 500 nur fuer R0 = 20 (d = 2: A5; d = 3: beschreibend). Fuer R0 = 40 und 80 nicht gerechnet
  (Kosten; die Karte bindet A5 nur an d = 2, R0 = 20).
- **[P] Urteilsgitter:** das feine. Das grobe Gitter wird gleich ausgewertet; gibt es ein anderes Urteil, steht beim
  Urteil der Vermerk "nicht konvergiert" (das Urteil bleibt das des feinen Gitters).

### A.4 Urteilsregeln (mechanisch, feines Gitter)

- **A0** eingetroffen, wenn in allen fuenf Laeufen max |E/E0 - 1| (t <= t_c) < 1e-4 und max |T^0r|/T^00 <= 1 + 1e-6.
- **A1** eingetroffen, wenn |t_c/t_c(duenn) - 1| <= 0,02 fuer d = 2, R0 = 40 und 80, und d = 3, R0 = 40 (alle drei).
  t_c(duenn) = (pi/2) R0 bzw. 1,3110288 R0.
- **A2** eingetroffen, wenn fuer d = 2, R0 = 80 bei allen drei R (R0/2, R0/4, R0/10) |v/v_duenn - 1| <= 0,02.
- **A3** eingetroffen, wenn fuer d = 2, R0 = 80 die groesste Wandschnelle mit R >= 2 groesser als 0,99 ist.
- **A4** **[P]** eingetroffen, wenn in allen fuenf Laeufen die Musterschnelle im Fenster > 1 ist und A0 im selben Lauf
  gilt; sonst nicht eingetroffen (Vermerk nennt die Laeufe).
- **A5** eingetroffen, wenn fuer d = 2, R0 = 20: E(r < 10)/E0 (Mittel t_c + 490 bis t_c + 500) >= 0,05 und die
  Gipfel-Kreisfrequenz von phi_c auf t_c + 400 bis t_c + 500 kleiner als sqrt 2 ist.
- Fehlt ein benoetigter Lauf oder eine Groesse: "nicht auswertbar".

## B. Teil B: drehende Q-Baelle in M1

### B.1 Rechnung

- Profile mit regge2d.py (RG-1-Code, unveraendert): schiessen, profile_bauen; peitsche_b.py uebergibt alle Zeilen als
  Gitterschluessel und bekommt so jedes Profil (f, f', h) zurueck.
- **[P] Raster:** m = 1, 2, 3, 5, 8; omega^2 = die 25 RG-1-Werte 0,52 bis 0,99 (W2_STANDARD). Damit sind alle Punkte
  gemeinsame Punkte mit RG-1.
- **[P] Gitter:** h0 = 0,005 (urteilt) und h0 = 0,01 (Konvergenz), wie RG-1 (h001 und h0005). Gibt h0 = 0,01 ein
  anderes Urteil: Vermerk "nicht konvergiert".
- v_E(r) = 2 omega m f^2/r / (omega^2 f^2 + f'^2 + m^2 f^2/r^2 + U(f^2)) auf dem ganzen Profil (Reihe, Schuss,
  Schwanz), v_E(0) = 0. Maximum ueber r und seine Lage; Schranke omega/sqrt(omega^2 + 1/2).
- Ungueltige Zeilen (regge2d: Klammer nicht geschlossen, nicht monoton, Schwanz nicht erreicht) werden gefuehrt und im
  Vermerk genannt, gehen aber nicht in B1 bis B3 ein.
- **Beschreibend (kein Urteil):** v_E an der Ringmitte R_max; Maximum von v_E im energietragenden Bereich
  (T^00 >= 1e-2 max T^00); energiegewichtetes Mittel int |T^0theta| dA / int T^00 dA; Kartenschaetzung m/(R_max omega).

### B.2 Kontrollen

- J = m Q: im radialen Code ist J = m Q per Definition. Die echte Probe ist regge2d.gitterprobe: Feld auf kartesischem
  Gitter, spektrale Ableitungen, J = int (x p_y - y p_x) direkt. **[P]** Zeilen m = 1, 2, 3, 5, 8 bei
  omega^2 = 0,55; 0,70; 0,80; 0,95 (20 Zeilen, h0 = 0,005).
- Q, E gegen RG-1 bei gleichem h0 (h0 = 0,005 gegen lauf-lokal/h0005, h0 = 0,01 gegen lauf-lokal/h001).
- Zusatz (beschreibend): v_E auf demselben kartesischen Gitter aus T^0i = -2 Re(psi_t^* d_i psi), verglichen mit dem
  radialen Maximum (beide nur wo |psi|^2 >= 1e-6 max).

### B.3 Urteilsregeln (mechanisch, h0 = 0,005)

- **B0** eingetroffen, wenn max |J/(mQ) - 1| ueber die 20 Gitterzeilen <= 1e-8 und max |Q/Q_RG1 - 1|, |E/E_RG1 - 1|
  ueber alle gemeinsamen gueltigen Zeilen <= 1e-5.
- **B1** eingetroffen, wenn fuer alle gueltigen Zeilen max_r (v_E - Schranke) <= 1e-12 (Rundung).
- **B2** eingetroffen, wenn das groesste v_E-Maximum ueber alle gueltigen Zeilen in [0,35; 0,65] liegt.
- **B3** **[P]** eingetroffen, wenn fuer jedes m in {3, 5, 8} das Maximum von vE_max ueber omega^2 strikt im Innern des
  Rasters liegt (weder bei 0,52 noch bei 0,99). Sind die Randzeilen 0,52 oder 0,99 eines m ungueltig: "nicht
  auswertbar".

## R. Rauchlaeufe vor dem Einfrieren (offengelegt)

Alle in rauch/ auf der .69, Zeiten UTC.

- **Teil A, d = 2, R0 = 10, dr = 0,01** (18:59, ohne und mit CUDA-Graph, Ergebnis bitgleich; 21,7 s gegen 1,2 s):
  t_c = 15,06 (duenn 15,71, -4,1 %); v(R0/2) = 0,873 (+0,8 %), v(R0/4) = 1,010 (+4,4 %), v(R0/10) = 1,193 (+20 %);
  groesste Wandschnelle mit R >= 2: 1,04; Musterschnelle im Fenster 7,3; Energiefehler bis t_c 5,7e-9;
  max |T^0r|/T^00 = 1 - 2e-11 (in der aeusseren Strahlungsfront, T^00 ~ 1e-27); im energietragenden Bereich hoechstens
  0,989. Rueckprall: phi_c wird 1,0 nach t_c wieder negativ, phi_c steigt nach t_c bis 3,97.
- **Teil A, d = 3, R0 = 10, dr = 0,005** (19:05): t_c = 12,24 (duenn 13,11, -6,7 %); v(R0/4) = 1,09; Musterschnelle 146
  (vermutlich der Sprung beim Wiederauftauchen der Nullstelle: phi_c < 0 wieder ab t = 13,04); Energiefehler 1,3e-9.
- **Gesehen und wichtig:** Bei R0 = 10 laeuft die Nullstelle schon bei R = R0/4 schneller als 1, waehrend
  |T^0r|/T^00 in der Wand unter 0,99 bleibt. Die Nullstelle ist dort also schon vor dem Zusammenschlag ein Muster,
  das der Energie davonlaeuft. Wie das mit R0 skaliert, weiss ich vor den Hauptlaeufen nicht. Keine Schwelle wurde
  deshalb geaendert; R0 = 10 ist kein Lauf der Karte.
- **Zeitprobe** d = 2, R0 = 20, dr = 0,0035 (N = 88 060): 75 600 Schritte in 20 s (0,26 ms je Schritt mit Graph);
  Zwischenstand-Mechanik (checkpoint.npz) dabei einmal ausgeloest.
- **Teil B, h0 = 0,01** (m = 1, 3, 8; omega^2 = 0,55; 0,80; 0,99) und **h0 = 0,005** (m = 3, 8; 0,52; 0,70; 0,99):
  Q und E gleich RG-1 bis 4e-16; J/(mQ) - 1 bis 2e-16; v_E Gitter gegen radial bis 9e-5.
  vE_max 0,37 bis 0,50, steigend mit omega^2, **Lage bei r ~ m im fast leeren Kern** (nicht am Ring R_max):
  dort ist das Feld klein und linear (f ~ I_m), und v_E -> omega/sqrt(2(1 + omega^2)) (0,499 bei omega^2 = 0,99) [M,
  nachgerechnet aus der Formel]. Im energietragenden Bereich (T^00 >= 1 % des Maximums) liegt das Maximum dagegen innen
  (0,40 bei omega^2 = 0,70; 0,14 und 0,09 bei 0,99). Die Kartenregeln B2 und B3 verwenden das unbeschraenkte Maximum
  ueber r; daran halte ich mich. Das Maximum im tragenden Bereich und das energiegewichtete Mittel werden nur
  beschreibend berichtet.
- **Hinweis zur Karte:** Die Schranke bei omega^2 = 0,99 ist omega/sqrt(omega^2 + 1/2) = 0,8151, nicht 0,814 (Karte,
  Schreibtisch). B1 verwendet die Formel.

## E. Einfrieren

Siehe Kopie PLAN.md.eingefroren-* und die Hashes in ERGEBNIS.md (Abschnitt Kontrollen). Nach dem Einfrieren werden
Plan und Urteilsregeln nicht mehr geaendert; Code nur bei echten Fehlern, offengelegt.
