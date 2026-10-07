# GUERTEL-2: Plan (Runde 42; Teil A Staley-Weg, Teil B Guertel im Feld)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 17:13:05 CEST; Plantext ab 17:36:53 CEST (date), vor
  jedem Lauf. Zeitbox 180 min.
- Karte: KARTE.md (GZ0 bis GZ3, Erweiterung Teil B mit GZ4 bis GZ6). Vorhersagen und Wahrscheinlichkeiten der Karte
  bleiben unveraendert.
- Kennzeichen: [M] Mathematik; [E] Messung im Modell (synthetisch); [L] Gedaechtnis; [H] Hypothese; [F] Festlegung
  dieses Plans; [R] im Rauchlauf gesehen. Alles ist eine synthetische Modellrechnung, keine Messdatenbestaetigung.
- Bezugswerte aus GUERTEL-1 (lauf-69/auswertung.json, per jq gelesen):
  - L = 1,8: E_min(0) = 8,409002; dE_360 = 41,242482; Protokollzustand 720 Grad: E = 177,279, W = (1, 0, 1, 0).
  - L = 1,3: E_min(0) = 5,109646; dE_360 = 249,965888.
  - Eingaben: eingaben-g1/protokoll-L1.8.npz und -L1.3.npz (Kopien, sha256 wie in GUERTEL-1/PRUEFSUMMEN.txt).

## 0. Ableitbarkeit (vorab)

1. **Existenz des Wegs [M]:** Schalendrehungen (jede Kugelschale starr gedreht) erhalten Abstaende auf gleichem Radius.
   Fuer unendlich duenne Faeden ist jeder solche Weg durchdringungsfrei. Der Staley-Weg (Abschnitt A2) fuehrt die
   4-pi-Wicklung in den Grundzustand. Das ist Topologie und nur Kontrolle.
2. **Grenze der Diskretisierung [M, vorab]:** 16 (12) Segmente auf 1,8 radialer Strecke. Bei 4 pi Gesamtdrehung dreht
   sich je Segment mit radialer Erstreckung dr die Schale um etwa 7 dr rad. Fuer dr = 0,2 sind das 1,4 rad; die Sehne
   faellt dann auf etwa 0,76 r. Nahe am Koerper (r < 1,3) kann sie den Koerper schneiden. GZ0a ist deshalb nicht
   sicher. Die Gueltigkeit des relaxierten Strings wird unabhaengig davon geprueft (A4).
3. **Feld, Kontinuum [M]:**
   - SO(3)-Feld mit festem Rand: Eine radiale Verdrillung um mehr als 2 pi ist kein lokales Minimum (konjugierter Punkt
     der Geodaete in SO(3)). Der kleinste Vertreter jeder Klasse hat Energie proportional dist(theta, 4 pi Z)^2.
     E_min(theta) ist also 720-periodisch mit Knick bei 360 Grad, und eine Sperre gibt es im Kontinuum nicht.
   - Entlang des Feld-Staley-Wegs ist die Energie in Phase 1 bis auf die Bindungen an der Naht r(h = 1/2) konstant.
   - SO(2)-Feld: Die Windung ist erhalten, E waechst wie theta^2.
   - Nicht ableitbar: was die Relaxation auf dem Gitter findet; Gittersprunge (eine Bindung ueberschreitet den
     Drehwinkel pi), die beide Aussagen aushebeln koennen; die Gitterabhaengigkeit.
4. **Faeden [E aus GUERTEL-1]:** Der Vorwaertsast ist metastabil (Zwischenrasten). Die Hoehe der Sperre S ist deshalb
   nicht ableitbar.

## Teil A: Faeden (GUERTEL-1-Modell unveraendert, zweizaehlige Achse x, Koerper bei 720 Grad = Identitaet)

### A1. Temperaturleiter fuer E_min(0) (GZ3) [F]

- Start B0 = GUERTEL-1-Protokollzustand bei 0 Grad (System zweizaehlig).
- T0 in {0,5; 1; 2; 4}, je 5 Saaten, ueberdaempftes Langevin, T linear auf 0 in nL = 12000 Schritten. Das ist
  doppelt so lang wie in GUERTEL-1, mit bis zu achtfacher Starttemperatur. dt0 = 2e-4, capl = 0,01, danach FIRE
  nF = 3000, ftol 1e-3.
- Sonde wie GUERTEL-1 (4.2). Fadenlaengen 1,8 und 1,3. Saat numpy default_rng([42, 10 L, 0]).
- E_min(0)_neu := kleinste Endenergie der gueltigen Saaten ueber alle Stufen. Weniger als 80 % gueltige Saaten
  insgesamt: nicht auswertbar.
- Zusatz, beschreibend (nur L = 1,8): dieselbe Leiter bei 720 Grad ab X_W (GUERTEL-1-Protokollzustand, W = (1, 0, 1,
  0)), T0 in {1; 2; 4} je 5 Saaten. Frage: Findet staerkeres Abkuehlen die Entwirrung?

### A2. Staley-Weg (Bau) [F]

- Radiale Koordinate t(r) = clip((2,9 - r)/1,8, 0, 1); t = 0 am Anker, t = 1 am Ansatz.
- Rampen: f_a(t) = clip((t - 0,05)/0,45, 0, 1); f_i(t) = clip((t - 0,5)/0,45, 0, 1). Zonen von 0,09 Radius an Anker und
  Ansatz bleiben starr.
- Phase 1, s von 0 bis 1 (360 Schritte): g_s = Rot(x, 2 pi f_a) Rot(n(s), 2 pi f_i), mit n(s) = (cos pi s, sin pi s, 0),
  also von x ueber y nach -x.
- Phase 2, lambda von 1 bis 0 (360 Schritte): g = Rot(x, 2 pi lambda (f_a - f_i)).
- Jede freie Perle x geht nach g(t(|x|)) x; feste Perlen bleiben. Am Ansatz ist g = I fuer alle s, der Koerper steht
  also fest.
- G4pi[X] := Phase 1 bei s = 0 = Rot(x, 4 pi k(t)) mit k = (f_a + f_i)/2: die ideale 4-pi-Wicklung von X.

### A3. Anfangsstrings [F]

- **S1 (Haupt, L = 1,8 und 1,3):**
  - FIRE ab G4pi[B0] (hoechstens 10000 Schritte, ftol 1e-3, Sonde). Ein Rahmen wird gespeichert, sobald sich eine
    Perle um >= 0,02 bewegt hat.
  - Weg = Rahmen rueckwaerts (relaxierter Start -> G4pi[B0]), dann Staley(B0) Phase 1 und 2 (-> B0).
- **S2 (Zwischenrast, L = 1,8):**
  - Das GUERTEL-1-Drehprotokoll (drei Systeme, gleiche Saat und Parameter) wird bis 720 Grad wiederholt. System 0
    wird nach jedem 1-Grad-Schritt und innerhalb von FIRE bei Bewegung >= 0,02 aufgezeichnet.
  - **Reproduktionskontrolle:** Der 720-Grad-Zustand muss mit X_W aus GUERTEL-1 uebereinstimmen (max. Abweichung
    berichtet).
  - Kompensation Q_j = Rot(x, (4 pi - theta_j) k(t)) je Perle. Sie haelt den Koerper fest; Q(720) = X_W,
    Q(0) = G4pi[B0'].
  - Weg = Q rueckwaerts (X_W -> G4pi[B0']), dann Staley(B0') (-> B0').
- **S0 (trivial, GZ0b, L = 1,8 und 1,3):** g_s = Rot(x, pi sin(pi s) sin(pi t)), s von 0 bis 1 (360 Schritte), von B0
  nach B0.
- Jeder Weg wird auf M = 201 Bilder gleicher Bogenlaenge umverteilt (GUERTEL-1 reparam).

### A4. Stringrelaxation [F]

- Vereinfachte Stringmethode wie GUERTEL-1: Endpunkte fest, dx = -grad E dts, dts = 1e-4, je Perle hoechstens 0,005.
  Alle 5 Iterationen Umverteilung. niter = 2000.
- **Laufende Durchdringungsprobe** je Bild ueber alle Iterationen:
  - min Faden-Faden >= 0,1; min rho >= 1; max r <= 3;
  - Rand je Bewegung (Schritt plus Umverteilung, delta = groesste Perlenverschiebung): d_min - 2 delta > 0 und
    rho_min - delta - 1 > 0.
- **Endpruefung** wie GUERTEL-1: jedes Bild in den Grenzen; zwischen Nachbarbildern d_min - 2 delta > 0 und
  rho_min - delta - 1 > 0.
- Gueltig := laufende Probe und Endpruefung bestanden.
- Konvergenz: S alle 100 Iterationen. Konvergiert, wenn |S(2000) - S(1500)| <= 0,02 dE_360(L). Wenn nicht
  konvergiert: Kennzeichen am Urteil, kein Wechsel der Regel.

### A5. Messgroessen [F]

- **S_plan := max_k E_k - E_0** (E_0 = relaxierter gewickelter Start). Das ist die Sperre aus dem gewickelten Zustand,
  wie GUERTEL-1 3.4. Sie passt zur Karte "S = 0 in fuehrender Ordnung".
- **S_wort := max_k E_k - E_(M-1)** (E am Ende des relaxierten Wegs, B0). Das ist die woertliche Lesung von "minus
  E(Ende)".
- Beide werden berechnet, berichtet und je GZ beurteilt.
- **Entwirrt** (Koerper bei 720 Grad = I): gerundete Windungen jedes Fadens um x, y und z alle 0, und
  E <= 1,10 E(B0). Bei 720 Grad sind die Windungen um jede Achse ganzzahlig, weil Ansatz und Anker gleiche Richtung
  haben. Das zusaetzliche y/z-Mass schliesst die Achsenwanderung aus GUERTEL-1 aus.
- **Start entwirrt:** Endet die FIRE-Relaxation der idealen Wicklung (S1) schon entwirrt, gibt es dort keinen
  metastabilen gewickelten Zustand. Dann gilt S_plan := 0 (Kennzeichen "Entwirrung ohne Sperre").
- **dE_360:** GUERTEL-1-Werte (Karte: "wie in GUERTEL-1").

## Teil B: Orientierungsfeld [F]

### B1. Modell

- **3D:** Gitterplaetze x in Z^3 mit |x| <= R + 1.
  - Kern |x| <= r0 mit q = (cos theta/2, 0, 0, sin theta/2), also Drehung um z, stetig in theta.
  - Rand |x| > R mit q = 1; frei r0 < |x| <= R.
  - Energie E = Summe ueber Nachbarbindungen (3 - tr R_a^T R_b) = Summe 4 (1 - (q_a . q_b)^2).
  - Die Einheitsquaternionen sind die dynamischen Groessen, also die stetige Hebung nach SU(2).
- **2D:** Z^2, Winkel phi (reell, stetig); Kern phi = theta, Rand 0; E = Summe (2 - tr R_a^T R_b) =
  Summe 2 (1 - cos(phi_a - phi_b)).
- Die Kopplung ist im Werteraum isotrop. Die Wahl der Drehachse z ist deshalb ohne Einfluss.
- **Gittergroessen (r0, R):**
  - 3D: (3, 12) "grob" und (6, 24) "fein". Urteil auf fein.
  - 2D: (3, 12), (6, 24), (16, 64). Urteil GZ4 auf (16, 64).
  - Vorab [M]: Groesster Bindungswinkel der harmonischen Verdrillung etwa theta/(r0 (1 - r0/R)) in 3D bzw.
    theta/(r0 ln(R/r0)) in 2D.
    - 3D fein bei 360 Grad: 1,40 rad. 2D (16, 64) bei 1440 Grad: 1,13 rad.
    - (6, 24) in 2D erreicht pi/2 bei etwa 750 Grad.
- **Sonde (Gittersprung):**
  - 3D gueltig, wenn min ueber Bindungen q_a . q_b > 0 (Hebung raeumlich stetig, kein Gittersprung).
  - 2D gueltig, wenn max |phi_a - phi_b| < pi.
  - Das ist das Gegenstueck zur Durchdringungsprobe: Ein Gittersprung aendert die Klasse, die im Kontinuum erhalten
    waere.

### B2. Drehprotokoll

- Schritte von 5 Grad bis 1440 Grad.
- Je Schritt:
  - Praediktor (freie Plaetze um 5 Grad mal h(r) um z weitergedreht, h harmonisch: 3D (1/r - 1/R)/(1/r0 - 1/R), 2D
    ln(R/r)/ln(R/r0));
  - Kern setzen; Rauschen 1e-3 rad je Platz (Symmetriebruch);
  - FIRE auf S^3 bzw. R, hoechstens 40 Schritte, ftol 1e-5, Schritt je Platz <= 0,05.
- Gitterwinkel alle 45 Grad: FIRE bis 300 Schritte; E, Sonde, Zustand (Zustand alle 180 Grad) speichern.

### B3. E_min

- Je Winkel 0, 360, 720, 1080, 1440: Protokollzustand plus 4 Saaten. Saat = Protokollzustand mit Stoss (zufaellige
  Drehung je Platz, rms 0,1 rad), danach FIRE bis 600 Schritte.
- E_min := kleinste Energie der gueltigen Zustaende; E_quer und SE ueber die gueltigen.
- Ein Winkel ist ausgewertet, wenn >= 80 % (also >= 4 von 5) gueltig sind.

### B4. Feld-Sperre (nur 3D, bei 720 Grad)

- **Weg:** Feld-Staley-Weg q = q_z(2 pi f_a(h)) q_n(s)(2 pi f_i(h)), mit f_a = clip(2h, 0, 1) und
  f_i = clip(2h - 1, 0, 1); dann Phase 2 q_z(2 pi lambda (f_a - f_i)). Je 40 Schritte.
- **Start:** FIRE ab der harmonischen 4-pi-Verdrillung plus Rauschen 1e-3, hoechstens 3000 Schritte, Rahmen alle 25
  Schritte. Weg = Rahmen rueckwaerts plus Staley-Weg, umverteilt auf M = 25 Bilder.
- **Relaxation:** Gradientenschritt auf S^3, dts = 0,02, je Platz <= 0,05, Endpunkte fest, Umverteilung alle 5
  Iterationen, 400 Iterationen.
- **Gueltig,** wenn jedes Bild am Ende und waehrend des Laufs min q_a . q_b > 0 hat und benachbarte Bilder je Platz
  q_k . q_k+1 > 0.
- S_Feld,plan := max E - E_0; S_Feld,wort := max E - E_(M-1).
- Endet der Start entdrillt (E_0 <= 0,10 dE_360,Feld), gilt S_Feld := 0 (Kennzeichen).
- dE_360,Feld := E_quer(360) - E_quer(0) auf demselben Gitter.

## Urteilsregeln [F] (mechanisch in code/auswertung2.py)

| Nr | nach Plan | nach Kartenwortlaut |
|---|---|---|
| GZ0 | (a) Staley-Weg A2 (Phase 1 und 2, 721 Bilder) fuer L = 1,8 und 1,3: an jedem Bild min Faden-Faden >= 0,1, min rho >= 1, max r <= 3; (b) S0 fuer L = 1,8 und 1,3 gueltig und S_plan(S0) <= 0,01 dE_360(L) | (a) wie Plan; (b) S0 gueltig und S_plan(S0) <= 0,01 E(B0) |
| GZ1 | L = 1,8, S1: gueltig, letztes Bild entwirrt, S_plan < dE_360 = 41,2425 | dasselbe mit S_wort |
| GZ2 | S1 bei 1,8 und 1,3 gueltig und Ende entwirrt; S_plan(1,8) < S_plan(1,3). Sonst nicht auswertbar | dasselbe mit S_wort |
| GZ3 | L = 1,8: E_min(0)_neu <= 0,90 x 8,409002 = 7,568101 | gleich |
| GZ4 | 2D (16, 64): 0, 360, 720, 1080, 1440 ausgewertet; dE_k = E_min(k 360) - E_min((k-1) 360) > 0,5 dE_1 > 0 fuer k = 2, 3, 4 (jede Umdrehung kostet mindestens halb so viel wie die erste) | 2D (16, 64): E_min streng steigend ueber 0, 360, 720, 1080, 1440 (alle ausgewertet) |
| GZ5 | 3D fein: alle fuenf Winkel ausgewertet; (a) E_min(720) - E_min(0) <= 0,10 (E_min(360) - E_min(0)); (b) E_min(360) - E_min(0) >= 3 SE_komb(360, 0) und > 0; (c) E_min(1440) - E_min(0) <= 0,10 (E_min(360) - E_min(0)) und E_min(1080) <= 1,10 E_min(360) | (a') abs(E_min(720) - E_min(0)) <= 0,10 E_min(0) + eps, eps = 1e-6 (E_min(360) - E_min(0)) (E_min(0) = 0, das Band ist sonst leer); (b) und (c) wie Plan |
| GZ6 | S_Feld,plan / dE_360,Feld < S_plan(S1, 1,8) / 41,2425; beide Strings gueltig | dasselbe mit S_wort beider Strings |

- Eingangsbedingung: Fehlt ein benoetigter Wert oder ist er nicht gueltig, lautet das Urteil "nicht auswertbar".
  Ausnahme GZ1: Ist S1 bei L = 1,8 ungueltig (Durchdringung), lautet es "nicht eingetroffen", weil die Karte "ohne
  Durchdringung" vorhersagt.
- SE_komb = sqrt(SE_a^2 + SE_b^2); SE = sd/sqrt(n) ueber die gueltigen Zustaende eines Winkels.
- **Beschreibend:**
  - Teil A: S2 (S_plan, S_wort, Profil); Leiter bei 720 Grad (entwirrt?); Energieprofile; lokale Minima der Profile;
    W je Bild; grobe Gitter in B; Spruenge im Protokoll.
  - Teil B: Lesart "ohne Sonde" (Gittersprung-Zustaende mitgezaehlt) als Gitterbefund.

## Laufplan [F]

- Nur .69, Spur cpu10, ueber kleintest.sh; je Lauf <= 10 min, 1 Thread, 4 GB.
- Ordner: /home/fmh/fmhc-physics-remote/runde42-guertel-2/ (code/, rauch/, lauf/, eingaben-g1/).
- **Rauchlauf:**
  - Zeit und Speicher je Modus mit verkleinerten Parametern.
  - Kontrollen GZ0 (pfad L = 1,8 und 1,3 voll; S0-Strings voll) und GZ4 (2D voll).
  - Von den Pfad-Laeufen sehe ich nur die GZ0a-Felder und die Laufzeit an.
- **Hauptlaeufe** (eingefrorener Code, je genau einmal):
  - leiter L1,8 (mit 720), leiter L1,3;
  - pfad L1,8 (mit S2), pfad L1,3;
  - string S1 L1,8, S1 L1,3, S2 L1,8, S0 L1,8, S0 L1,3;
  - feld 3D grob (prot, saat, string), 3D fein prot, 3D fein saat, 3D fein string, feld 2D (drei Gitter, prot und saat);
  - auswertung2.
- Muss ein Lauf wegen Zeitueberschreitung oder Absturz wiederholt werden, steht das als Nachtrag mit Grund; die Werte
  des abgebrochenen Laufs werden nicht angesehen.

## Rauchlauf und Festlegungen vor dem Einfrieren [R] (Text ab 17:47:11 CEST)

### Gesehen

Angesehen habe ich nur Laufzeit, Speicher und die Kontrollfelder GZ0 und GZ4. Nicht angesehen: Startzustaende S1/S2,
Energieprofile, Leiter- und 3D-Feldwerte.

1. **Zeiten** (Laeufe 15:38:39 bis 15:45:56 UTC, alle rc = 0):
   - 3D fein (6, 24): 65.267 Plaetze, 189.918 Bindungen; etwa 64 ms je FIRE-Schritt (B = 1), etwa 180 ms bei B = 2;
     Feld-String mit M = 25 etwa 1,3 s je Iteration; Speicher 1,2 GB.
   - 3D grob (3, 12): 9.171 Plaetze, etwa 8 ms je Schritt.
   - Leiter: 7,5 ms je Langevin-Schritt bei B = 35.
   - pfad L1,8 mit S2: 200 s; pfad L1,3: 5 s.
   - Faden-String M = 201: 32 ms je Iteration.
   - 2D (16, 64): Protokoll 16 s, Saaten 30 s.
2. **Reproduktion:** Das wiederholte GUERTEL-1-Protokoll trifft X_W bei 720 Grad und B0 bei 0 Grad bitgleich
   (Abweichung 0,0). Die Naht Q(0) = G4pi[B0] stimmt auf 1,3e-15.
3. **GZ0a (Kontrolle):** Der Staley-Bau verletzt an einzelnen Bildern die Ausschlussgrenze.
   - L = 1,8: 576 von 721 Bildern gueltig, kleinster Faden-Faden-Abstand 0,00045.
   - L = 1,3: 653 von 721, kleinster Abstand 0,00094.
   - Die verletzten Bilder liegen nur in Phase 1, um n(s) nahe (+-1, 1, 0)/sqrt(2). Dort liegen zwei Faeden fast in
     der Drehebene. Ihre Spiralarme stehen dicht, und die Sehnen der Segmente schneiden sich (Diskretisierung, vgl.
     Abschnitt 0 Punkt 2).
   - Die Bilder bei s = 0 und s = 0,5 sowie Phase 2 sind sauber. Der Koerper wird nie geschnitten (min rho 1,078).
   - Der Bau wird **nicht** geaendert; GZ0a wird nach Plan beurteilt.
4. **GZ0b (Kontrolle), erster Rauchlauf** mit niter 2000 und dts 1e-4: nicht konvergiert.
   - S0 L1,8: S = 8646, 532, 115, 37, 16,1 bei 0, 500, ..., 2000.
   - S0 L1,3: 9464, 406, 45, 11,6, 4,3.
   - Die Stringmethode ist bei diesen Zahlen zu langsam; der Abfall haelt an.
5. **GZ4 (Kontrolle),** 2D (16, 64): E_min bei 0, 360, 720, 1080, 1440 Grad = 0 (Rest 5e-6), 174,69, 695,19,
   1550,22, 2718,11. Alle Zustaende gueltig (groesster Bindungssprung 2,15 rad < pi).
   - Gleiches Gitter wie 3D fein, (6, 24): Sprung nach 630 Grad.
   - (3, 12): Sprung nach 360 Grad.
   - Das entspricht der Abschaetzung in B1.

### Aenderungen vor dem Einfrieren (wegen Laufzeit und Konvergenz; Regeln unveraendert)

- **Faden-String (A4):** dts 1e-4 -> 3e-4 (stabil fuer die Dehnung: groesster Eigenwert etwa 4 k_s = 2000,
  2000 x 3e-4 = 0,6 < 2; tiefe Kontakte bleiben wie in GUERTEL-1 durch die Schrittkappe 0,005 begrenzt); niter
  2000 -> 8000; S-Protokoll alle 250 Iterationen.
  - Konvergenz neu: |S(8000) - S(6000)| <= 0,02 dE_360(L), also bei 75 % von niter statt fest bei 1500.
  - Gilt fuer S1, S2 und S0 gleich.
  - **Zweiter Rauchlauf S0 L1,8** (dts 3e-4, niter 5000; 15:46:52 bis 15:49:39 UTC):
    - S = 8646, 6,36, 2,69, 1,49, 0,854 bei 0, 1250, 2500, 3750, 5000; gueltig.
    - Der Abfall haelt an (Halbierung etwa alle 1500 Iterationen), daher niter 8000; erwartet etwa 0,2 bis 0,3.
  - Der Hauptlauf S0 ist der beurteilte. Selbstanzeige: Die Iterationszahl ist nach zwei Blicken auf die
    GZ0b-Kontrolle gewaehlt; die Regel (1 % von dE_360) bleibt.
- **Feld (B2 bis B4),** alle Gitter:
  - Protokollschritt 10 Grad (statt 5), FIRE 30 je Schritt (statt 40). Gitterwinkel alle 90 Grad (statt 45) mit FIRE
    150 (statt 300). Saaten FIRE 400 (statt 600).
  - Feld-String: M = 17 (statt 25), 250 Iterationen (statt 400), Start-FIRE hoechstens 2000 (statt 3000), dts 0,015
    (statt 0,02; Stabilitaet: groesster Eigenwert etwa 96, 96 x 0,015 = 1,44 < 2).
- **3D fein, Saaten:** zwei Laeufe, Winkel 0, 360, 720 bzw. 1080, 1440. Die beiden JSON-Dateien fuehre ich mit jq
  mechanisch zu lauf/feld-3d-r6-R24-saat.json zusammen (saaten und saaten_protokollzustand vereinigt, beide Koepfe
  behalten).
- **Hauptlaeufe:** alle Teile neu mit eingefrorenem Code, auch die Kontrollen (pfad, S0, 2D). Die Rauchlaufwerte
  zaehlen nicht.
- **Code:** guertel2.py nach dem Rauchlauf unveraendert, alle Aenderungen per Befehlszeile. In auswertung2.py
  Konvergenzbezug von Iteration 1500 auf 75 % von niter.

## Nachtraege nach dem Einfrieren

### Nachtrag N1 (2026-10-04 18:13:32 CEST): glatteres 3D-Gitter, beschreibend, nicht urteilsbildend

- **Anlass:** Im Hauptlauf 3D fein (6, 24) wuchs die Verdrillung bis 360 Grad (E = 3608,5; groesster Bindungswinkel
  etwa 1,9 rad, also ueber pi/2). Zwischen 360 und 450 Grad sprang das Feld auf dem Gitter (Sonde -0,994). Danach
  war E 360-periodisch. Frage: Ist das ein Gitterbefund, der bei glatterem Feld verschwindet?
- **Lauf:** feld --dim 3 --r0 12 --R 24 --teil prot,saat --ftmax 720 --fsaatwinkel 720, sonst Hauptlaufzahlen (10 Grad,
  FIRE 30 bzw. 150, Saaten 4 x 400). Code unveraendert (eingefrorener Hash). Vorab [M]: groesster Bindungswinkel bei
  360 Grad etwa 2 pi/(12 x 0,5) = 1,05 rad, mit dem Eckenfaktor 1,36 aus (6, 24) etwa 1,42 rad < pi/2.
- **Vorhersage (vor dem Lauf):**
  - [M] Im Kontinuum ist die Vorwaertsverdrillung jenseits von 360 Grad instabil (konjugierter Punkt), E_min(720) = 0.
  - [H] Auf (12, 24): Das Feld entdrillt stetig, ohne Gittersprung (Sonde > 0 an allen Gitterwinkeln bis 720 Grad),
    und E(720) <= 0,10 E(360). Wahrscheinlichkeit 45 %.
  - Gegenausgang: Gittersprung wie auf (6, 24), dann ist die Guertelwirkung auf diesem Gitter nicht erreichbar.
  - Haelt der Vorwaertsast ohne Sprung bis 720 Grad, ist das ein dritter Ausgang (metastabil).
- Dieser Lauf aendert kein GZ-Urteil; er steht im Ergebnis getrennt als Nachtrag.
