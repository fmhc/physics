# RAUTE-ATEM-1: Plan des Code-Agenten (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:21:01 CEST (date). Zeitbox 90 min.
- Gelesen: KARTE.md (ganz), RUNDE-42/SCHALTER-UND-ATMEN.md (ganz, Teil E), Finns Skizze, RUNDE-37/atem-netz-1/KARTE.md
  (ganz) und code/atem.py (Kopf und Konstanten, nur gelesen), RUNDE-37/takt-rand-4d-1/PLAN.md (Laufform), AGENTS.md
  (Dimensionsvergleich).
- Ordner: lokal RUNDE-37/raute-atem-1/ (code/, rauch-69/, lauf-69/); .69: /home/fmh/fmhc-physics-remote/raute-atem-1/
  (code/, rauch/, lauf/). Spuren cpu3 und cpu5, je Lauf <= 10 min, 1 Thread (kleintest.sh).
- Kennzeichen: [M] eigene Mathematik (nicht gegengelesen), [E] Messung im Modell, [L] Gedaechtnis, [H] Hypothese,
  [F] Festlegung dieses Plans, [R] im Rauchlauf gesehen (vor dem Einfrieren).
- Vorhersagen und Wahrscheinlichkeiten der Karte (RA0 85 %, RA1 80 %, RA2 20 %, FP 25 %) bleiben unveraendert. Meine
  eigene Erwartung steht getrennt in Abschn. 1 (D7) und aendert daran nichts. Keine Literaturabrufe.

## 1. Schreibtisch [M] (vor jeder Hauptrechnung)

- **D1 Huellenkopplung laeuft ueber die Stabkraefte.** Mit s_ij = (d_i + d_j)/2 und Stabkraft t_b = k (r_b - s_b)
  (Zug positiv) gilt dU/dphi_i = -(eps/2) cos(phi_i) Summe_(b an i) t_b, also
  phi_i' = omega + mu_phi (eps/2) cos(phi_i) Summe t_b.
  - Feste Lagen: ueber den Takt gemittelt XY-Antiferromagnet mit K = mu_phi k eps^2 / 8 (wie ATEM-NETZ-1).
  - Freie Lagen: Raute (2D) und Tetraeder (3D) sind statisch bestimmt. Folgen die Lagen dem Atmen ganz, verschwinden alle
    Stabkraefte und damit die Kopplung. Je elastischer Mode mit Rate lambda bleibt der Anteil omega^2/(lambda^2 + omega^2).
    Deshalb mu_x k / omega = 0,32 (Lagen langsamer als der Atem, lambda ~ 2 bis 8 je Takt): Kopplung etwa 0,4- bis
    1-fach K.
- **D2 Nur das Paar C-D treibt das Falten.** Alle anderen Paare sind durch Staebe verbunden; ihre Zentralkraefte leisten
  auf der Faltmode (Drehung von C bzw. D um AB, alle Stablaengen fest) in erster Ordnung keine Arbeit. Flach
  (theta = 180 Grad): r_CD = sqrt(3) sin(theta/2) ist dort maximal. Bei Anziehung (|Delta_CD| < 90 Grad) waechst die
  Abweichung alpha = 180 Grad - theta wie exp(0,385 mu_x B cos(Delta_CD) t) (3D, 1/r^2; Reibung 3/(8 mu_x) auf alpha).
  Grobe Schliesszeit von alpha_0 = 6,6 Grad (Z0 = 0,05): t ~ 2,8 / (0,385 mu_x B), also B = 0,03: ~120, 0,05: ~73,
  0,08: ~45 Takte, dazu die Zeit, bis C und D im Gleichtakt sind (~1/K bis 3/K = 16 bis 50 Takte).
- **D3 Statik bei festen Phasen (ableitbar, nur Kontrolle).** Phasen 0, 120, 240, 240 Grad.
  - 3D, geschlossen: Der Tetraeder ist statisch bestimmt, und alle Lasten sind Paarkraefte entlang der Staebe. Also traegt
    jeder Stab genau seine Paarkraft: C-D Druck B/r^2, die fuenf 120-Grad-Staebe Zug B/(2 r^2). Das Scharnier ist nicht
    der staerkste Stab (Karte).
  - 2D, flach (nicht in der Karte): C-D-Anziehung B/sqrt(3) wird ueber die Raute abgetragen. Aussenstaebe Druck B/3,
    Scharnier Zug B/3, dazu je 120-Grad-Paar Zug B/2. Ergebnis: A-B Zug 5B/6, Aussenstaebe Zug B/6. **In 2D passt Finns
    Kraftbild schon bei festen Phasen** (grosse Kraft durchs Scharnier, kleine aussen). FP gilt aber laut Karte dem
    gefalteten bzw. geschlossenen Zustand (3D); 2D nur als Vermerk.
- **D4 Kollaps-Schranke.** Ein Gleichtakt-Paar in Beruehrung haelt nur, wenn k (s - r) = B/r^2 eine Loesung hat:
  B <= 4 k s^3 / 27, also 0,148 k (s = 1) bzw. 0,108 k mit Atmen im Gleichtakt (s_min = 1 - eps). [R] Der erste
  Statik-Rauchlauf mit B = 0,2 (k = 1) bestaetigte das: C und D gingen durcheinander (r_CD = 1,59 statt < 1). Deshalb
  B <= 0,08 (Abschn. 3). In 2D (1/r) waere die Schranke B <= k s^2 / 4; C-D beruehren sich dort nicht.
- **D5 Phasen nach dem Schliessen.** Auf dem Tetraeder (K4) sind die Grundzustaende des XY-Antiferromagneten alle
  Lagen mit Zeigersumme 0, also zwei Gegentakt-Paare mit freiem Winkel. Ab (0, 120, 240, 240) waechst die C-D-Spaltung
  linear mit Rate K; die naechsten Grundzustaende haben Delta_CD = 120 Grad (Paare A-D und B-C oder A-C und B-D).
  Der freie Winkel ist entartet; Delta_CD kann dort zwischen 0 und 180 Grad liegen (nicht ableitbar).
  - Statik in diesen Lagen: |t_b| = B |cos Delta_b| / r^2. Im naechsten Grundzustand tragen die Aussenstaebe A-D und
    B-C mit B die groesste Kraft, A-B und C-D je B/2 -> FP verfehlt. Fuer das Paar (A,B)(C,D) tragen A-B und C-D
    gleich viel (B). **Bei festen Phasen kann FP auf dem Tetraeder nie streng gelten**; nur Zeitmittel ueber wechselnde
    Phasen, Atmen und Loesen der Fangbindung koennen es aendern.
- **D6 Oeffnen.** Die C-D-Bindung haelt hoechstens k delta_f Zug. Im Tetraeder ist die Zugkraft in C-D gleich der
  C-D-Paarkraft, also reisst sie bei B |cos Delta_CD| / r^2 > k delta_f, d. h. beta |cos Delta_CD| > 1 mit
  beta = B/(k delta_f). Bei Delta_CD = 120 Grad: beta > 2. Nach dem Loesen zieht die Rauten-Kopplung Delta_CD mit
  Rate K zurueck auf 0; von 120 auf 90 Grad dauert das ~0,33/K ~ 5 Takte. In dieser Zeit oeffnet die Abstossung nur
  wenig (grob 0,1 bis 0,3 PU Luecke bei B = 0,08). Atmen bricht die Bindung zusaetzlich je Takt kurz auf.
- **D7 Meine Erwartung [H], getrennt von der Karte:** RA0 ja; RA1 ja, bei B = 0,03 knapp; RA2 hoechstens bei
  B = 0,08, eher nein (Oeffnung bleibt klein, D6); FP nein (D3, D5).

## 2. Modell (Lesart der Karte) [F]

- Punkte A = 0, B = 1 (Scharnier), C = 2, D = 3. d_i = 1 + eps sin(phi_i).
- Staebe A-B, A-C, B-C, A-D, B-D: U_b = (k/2)(r_b - s_b)^2 (Zug und Druck).
- C-D: Fangbindung. U_CD = (k/2)(r - s)^2, solange die Luecke g = r_CD - s_CD < delta_f ist (Beruehrung samt
  Fangabstand; Druck bei g < 0 ist die Huellenabstossung); sonst kraftfrei. Binden und Loesen an derselben Schwelle,
  ohne Hysterese. Die Zugkraft ist so auf k delta_f begrenzt.
- Phasen: phi_i' = omega - mu_phi dU/dphi_i + sqrt(2T) xi_i. **U enthaelt nur Stab- und Huellenenergie** (Karte:
  "Huellen-Kopplung ueber die Bindungen"); das Medium wirkt nur auf die Lagen.
- Medium: Paarkraft f_ij = B cos(phi_i - phi_j) / r^(D-1) entlang der Verbindung, positiv anziehend, alle 6 Paare.
- Lagen: x_i' = mu_x F_i, ohne Rauschen. Integration: Heun (Lagen und Phasen), Rauschen additiv (wie ATEM-NETZ-1).
- Start: Raute aus zwei gleichseitigen Dreiecken (Seite 1): A = (0,-1/2), B = (0,1/2), C = (-sqrt(3)/2, 0),
  D = (sqrt(3)/2, 0). 3D: C und D um Z0 = 0,05 PU angehoben (Faltwinkel ~173,4 Grad). Dazu Lagerauschen
  N(0, 0,002^2) je Koordinate. Phasen gleichverteilt. Saat s bestimmt Phasen, Lagerauschen und Rauschfolge (gleich fuer
  2D/3D und alle B).
- Faltwinkel theta: Winkel zwischen den Lotvektoren von C und D auf die Achse AB (flach 180 Grad, Tetraeder 70,5 Grad).

## 3. Parameter [F]

| Groesse | Wert | Begruendung |
|---|---|---|
| eps | 0,10 | wie ATEM-NETZ-1 |
| k | 1 | wie ATEM-NETZ-1 |
| mu_x | 2 | mu_x k/omega = 0,32: Lagen langsamer als der Atem (D1), schneller als Falten und Phasenordnung |
| mu_phi | 50,27 | kappa = mu_phi k eps^2/(8 omega) = 0,01 (schwach; ATEM-NETZ-1 0,005 bzw. 0,05), K = 0,063 je Takt; Ordnung in ~50 Takten, damit RA1 (200 Takte) nicht an der Phasenordnung haengt |
| T | 6,28e-5 | T = 1e-3 K (wie ATEM-NETZ-1), nur auf den Phasen |
| B | 0,03; 0,05; 0,08 | unter der Kollaps-Schranke 0,108 (D4); mu_x B = 0,06 bis 0,16, Schliessen nach D2 in 45 bis 120 Takten |
| delta_f | 0,02 PU | beta = B/(k delta_f) = 1,5; 2,5; 4 ueberdeckt die Reissschwellen beta = 1 (Gegentakt) und 2 (120 Grad), D6 |
| G_AUF | 0,20 PU | "offen" (Plan) = C-D-Luecke >= 2 eps, doppelter Atemhub der Radiensumme (Faltwinkel ~88 Grad) |
| Saaten | 1, 2, 3, 4 | Karte: mindestens vier |
| dt | 0,005 Takt | Heun; [R] dt gegen dt/2 ueber 20 Takte: Lagen 7e-6 PU, Phasen 2e-4 rad |
| Dauer | 500 Takte | RA2-Fenster; Kontrollen gleich lang |

- Vor dem Einfrieren geaendert (ohne Hauptergebnis gesehen): B von 0,05/0,1/0,2 auf 0,03/0,05/0,08 und delta_f von
  0,05 auf 0,02 wegen D4 ([R] Statik-Kollaps bei B = 0,2); mu_x von 1 auf 2 und kappa von 0,005 auf 0,01 aus D2 (sonst
  laege die Schliesszeit fuer kleine B schon am Schreibtisch ueber 200 Takten).

## 4. Messgroessen [F]

- Ablage alle 0,05 Takt: Zeit, theta, Luecken g_b = r_b - s_b, Abstaende, Stabkraefte t_b (C-D = 0, wenn geloest),
  Mediumkraefte f_b, Phasen, Lagen, Bindung C-D.
- **Ereignisse (Plan):** Startzustand "auf". Schliessen: g_CD < delta_f. Oeffnen: g_CD >= G_AUF.
  **Ereignisse (Karte):** Schliessen wie Plan; Oeffnen: Bindung >= 1 Takt am Stueck geloest (g_CD >= delta_f).
- Klappzyklus: mittlerer Abstand aufeinanderfolgender Schliessereignisse (Plan).
- **Umordnung:** im Zu-Zustand (Plan) nach dem ersten Schliessen einmal |Delta_CD| > 90 Grad (die C-D-Kraft wird
  abstossend).
- Phasendifferenzen: Kreismittel von exp(i Delta_ij) ueber das jeweilige Fenster (Ende: letzte 10 Takte).
- **Stabkraefte:** Mittel t_b (vorzeichenbehaftet, Zug +), Betrag des Mittels, Mittel des Betrags, Wechselamplitude
  sqrt(2) x Standardabweichung. FP-Fenster: alle Proben im Zu-Zustand (Plan), wenn >= 10 Takte; sonst theta <= 125 Grad
  (gefaltet), wenn >= 10 Takte; sonst nicht auswertbar.
- **Werkzeugprobe (Kraftbilanz je Knoten), alle 5 Takte in jedem Lauf:** Summe Stab- plus Mediumkraefte je Knoten aus
  einer Schleife je Paar gegen (a) die Kraft, die die Bewegung treibt (Bilanz mit Reibung -x'/mu_x), und (b) -grad(U+V)
  als zentrale Differenz (h = 1e-5; V = -B cos/r in 3D, B cos ln r in 2D); dazu Summe ueber alle Knoten (Impuls). Proben
  mit |g_CD - delta_f| < 1e-3 (Unstetigkeit der Fangbindung) werden ausgelassen und gezaehlt.

## 5. Urteilsregeln (mechanisch in code/auswertung.py)

- **Vorbedingung:** alle 24 Hauptlaeufe (2D, 3D je 3 B x 4 Saaten), 8 Kontrolllaeufe (B = 0, 2D und 3D) und die
  Statik-Kontrolle liegen vor; sonst "nicht auswertbar".
- **RA0 (Plan):** eingetroffen genau dann, wenn
  - in allen 8 Kontrolllaeufen (2D und 3D) die fuenf Stabpaare | |Delta| - 120 Grad | < 0,1 rad und |Delta_CD| < 0,1 rad
    haben (Kreismittel der letzten 10 Takte),
  - in allen 4 3D-Kontrollen max |theta(t) - theta(0)| < 5 Grad fuer t <= 200 Takte,
  - die Werkzeugprobe in allen Laeufen (Haupt, Kontrolle, Statik) unter 1e-6 bleibt,
  - und die Statik-Kontrolle stimmt: 3D |t_b + f_b| < 1e-6, 2D Stabkraefte gleich der Gleichgewichtsloesung der
    verformten Raute auf 1e-6, Restkraft < 1e-6.
  **Kartenwortlaut:** dieselben Bedingungen ohne die 2D-Phasen und ohne die Statik.
- **RA1 (Plan):** alle 12 3D-Hauptlaeufe schliessen (erstes g_CD < delta_f) bei t <= 200 Takten.
  **Kartenwortlaut:** je B mindestens 3 von 4 Saaten.
- **RA2 (Plan):** Ein Lauf erfuellt RA2, wenn Umordnung und >= 2 Oeffnungen (Plan, G_AUF) bis t = 500. Eingetroffen,
  wenn bei mindestens einem B mindestens 3 von 4 Saaten RA2 erfuellen.
  **Kartenwortlaut:** gleich, Oeffnen nach Karten-Ereignis (Bindung >= 1 Takt geloest).
- **FP (Plan):** Ein Lauf erfuellt FP, wenn im FP-Fenster |Mittel t_AB| groesser ist als |Mittel| jedes anderen
  vorhandenen Stabs, und - falls C-D in >= 50 % des Fensters gebunden ist - max der vier Aussenstaebe < |Mittel t_CD|.
  Eingetroffen, wenn >= 8 3D-Laeufe auswertbar sind und >= 3/4 davon FP erfuellen; weniger als 8 auswertbar: nicht
  auswertbar.
  **Kartenwortlaut:** dieselbe Regel auf das ueber alle auswertbaren 3D-Laeufe gepoolte Mittel (je Lauf durch B
  geteilt, nach Fensterdauer gewichtet).
- **Vermerke (zaehlen nicht):** 2D getrennt (C-D-Abstand, Stabkraefte, Phasen, je B, zweite Haelfte t >= 250);
  Stabkraefte der zweiten Haelfte auch in 3D; Zyklusdauer; Umordnungszeit; Statik mit Atmen (B = 0,05, feste
  Relativphasen, Mittel der zweiten Haelfte) gegen Statik ohne Atmen.

## 6. Laufplan [F]

- Hauptlaeufe: `raute.py haupt --dim D --B b --saaten 1,2,3,4 --takte 500` fuer D = 3, 2 und b = 0,03, 0,05, 0,08;
  Kontrollen `raute.py kontrolle --dim D`; Statik `raute.py statik --takte 100`; danach `auswertung.py`. Abwechselnd
  cpu3 und cpu5, hoechstens zwei zugleich.
- Ein Lauf, der ausserhalb des Codes scheitert (Starter, Netz), darf einmal wiederholt werden. Fehler im eingefrorenen
  Code machen die betroffenen Urteile "nicht auswertbar". Kein Code-Wechsel nach dem Einfrieren; Bilder und Tabellen
  nur aus eigenen, nach dem Einfrieren geschriebenen Anzeige-Skripten (als solche gekennzeichnet).

## 7. Rauchlaeufe [R] (vor dem Einfrieren)

- rauch 3D B = 0,1 (alte Werte), 10 Takte, cpu3, 16:33:21 bis 16:33:22 UTC, rc = 0: 0,42 s; Werkzeugprobe
  int/Schleife 2e-16, Schleife/FD 4e-11, Impuls 1e-17.
- Statik (alte Werte), cpu5, 16:33:21 bis 16:33:52 UTC, rc = 0: 3D B = 0,05 und 0,1: Restkraft 1e-14, t_b = -f_b auf
  1e-14 (C-D Druck 0,056 bzw. 0,133; uebrige Zug 0,024 bzw. 0,046, wie D3). **3D B = 0,2: Kollaps** (D4). 2D: A-B Zug
  0,083, Aussen 0,015 bei B = 0,1 (D3: 5B/6 = 0,083, B/6 = 0,017 fuer die unverformte Raute); Abweichung zur
  Gleichgewichtsloesung 1e-14.
- dtprobe (neue Werte), cpu5, 16:36:27 bis 16:36:34 UTC: 3D B = 0 und B = 0,08, 20 Takte, dt gegen dt/2: Lagen
  1,7e-6 bzw. 7,2e-6 PU, Phasen 1,8e-4 rad.
- Nach den Rauchlaeufen nur die Parameter in Abschn. 3 geaendert; keine Urteilsregel nach Sicht auf Hauptergebnisse.
- Statik (neue Werte), cpu5, 16:36:34 bis 16:37:08 UTC, rc = 0: 3D und 2D fuer B = 0,03, 0,05, 0,08 Restkraft
  < 6e-15; Statik mit Atmen (B = 0,05) Werkzeugprobe int/Schleife 4e-16, Schleife/FD 4e-11.
- Rauch-Testlaeufe aller Haupt- und Kontrollaufrufe mit 10 Takten (cpu3, 16:36:27 bis 16:36:53 UTC, alle rc = 0;
  0,7 bis 0,8 s je Saat und 10 Takte, hochgerechnet ~40 s je Saat und 500 Takte). Gesehen nur Laufzeiten und
  Werkzeugprobe (max Schleife/FD 5e-11, 264 Proben, keine ausgelassen). auswertung.py darauf ohne Laufzeitfehler
  (Urteile auf 10 Takten bedeutungslos, nicht verwendet).
- test_auswertung.py an einer Schein-Zeitreihe (keine Rechenwerte, 16:38:51 UTC): Ereignislogik wie erwartet
  (Schliessen bei 24,4 + 100 n, Oeffnen Plan 81,55 + 100 n, Karte 75,65 + 100 n, Zyklus 100, Umordnung erkannt).
