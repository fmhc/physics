# Runde 2: Laufplan fuer die 1D-Tests (Ideen 9/10, 32, 33) und das 3D-Radialprofil (Idee 31)

Bearbeiter: Anthropic-Agent (Opus), Auftrag ../AUFTRAG-1D-TESTS.md. Beginn 2026-09-30 00:54:07 CEST (gemessen), Ende in
der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ.

**Rechenort geaendert** (Nachricht der Leitung 30.09. 01:31; Finn: "mach die kleinen tests auf anderen karten oder auf
cpu"):
- Gerechnet wird auf einer Quadro P4000 mit eigener Sperre ueber kleintests/kleintest.sh, nicht mehr in VS-1-Pausen auf
  der P5000.
- Abschnitt 2 (Aufruf) und 3 (Laufzeit) sind darauf umgestellt, dazu Speichergrenze und Zwischenstand im Code.
- Physik, Vorhersagen und Latten sind unveraendert.

## Kurzfassung

- **Code:** tests1d.py (PyTorch, float64 bzw. complex128, nur CUDA). Ein Aufruf rechnet die gewaehlten Tests
  nacheinander; ein Fehler in einem Test bricht die anderen nicht ab (Bericht nennt ihn, Rueckgabewert 1).
  - Bericht, JSON und Zeitreihen werden nach jedem Test neu geschrieben.
  - Der Torch-Speicher ist auf 2,5 GB gedeckelt; erwartet sind unter 0,1 GB, dazu der CUDA-Kontext (einige 100 MB).
- **Aus qg1.py unveraendert:** Schiessen (rhs, rk4, schiessen, profil_bahn), Anker (profil_anker, anker_wgv), Gitter
  (gitter, profil_gitter), Velocity-Verlet mit dx = 0,1 und dt = 0,05, fein dx/2 und dt/2, Daempfungsschicht
  (quadratisch, sigma0 = 1, 40 breit). Geaendert: Box [-150, 150] statt [-120, 120], kein Brechungsfeld.
- **Neu:** Profil an beliebigen Orten (lineare Interpolation der Schiessbahn, h = 0,01) fuer bewegte Baelle mit
  Lorentz-Boost; Messungen je Test; fuer Test 4 radiales Schiessen in d = 3.
- **Laufzeit P4000** (P5000-Schaetzung mal 1,7, also obere Lage):
  - Rauchtest etwa 3,5 min
  - Hauptlauf in vier Einzelaufrufen je 1 bis 3 min, zusammen etwa 5,5 min (4 bis 9,5 min)
  - Jeder Test liegt deutlich unter 10 min.
- **Kernvorhersagen:** keine gleichphasige Synchronisation ohne Verschmelzen (Test 1); keine Absorption im
  laufenden Band (Test 2); gleichphasig verschmilzt, gegenphasig trennt sich, danach die Moden eines gewoehnlichen Balls
  gleicher Ladung (Test 3); dicke Wand VK-instabil, also kein Gedaechtnis (Test 4).

## 1. Aufbau je Test (vor dem Lauf festgelegt)

Modell wie im Auftrag: L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2. Ladungsdichte rho = 2 Im(psi conj psi_t),
Ladungsfluss j = -2 Im(psi conj psi_x), Energiefluss -2 Re(psi_t conj psi_x). Halbwertsbreite = volle Breite von
|psi|^2 auf halber Hoehe, aus dem Anker: FWHM = arcosh((1 + 2 b0)/b0)/sqrt(a0) = 3,466 / 3,558 / 4,160 / 5,704 bei
omega^2 = 0,55 / 0,70 / 0,80 / 0,90.

**1D-Profile:** ein Schiessen (qg1-Konstanten, 4 Runden x 4096 Kandidaten, h = 0,01, bis x = 80) fuer alle
omega^2 = 0,55; 0,69; 0,695; 0,70; 0,705; 0,71; 0,80; 0,90 und den Ersatzball 0,5128 (Q = Q(0,55) + Q(0,90) = 5,105).
K0 wie in QG-1: max |f - f_Anker| <= 1e-6. Der Rauchtest speichert die Bahnen (profil_1d.pt); der Hauptlauf laedt sie.

**Test 1, Uhren (Idee 9/10).** T = 400, Messung alle 0,5. 20 Laeufe.
- (a) Kette aus fuenf Baellen, omega^2 = 0,695 / 0,710 / 0,700 / 0,690 / 0,705 (feste Reihenfolge), Mitten (j - 2) D.
  - D = 8,0 (1,12 x 2 FWHM(0,70) = 7,12), dazu 11 und 14.
  - Anfangsphasen: gleich (alle 0), wechselnd (0, pi, 0, pi, 0), zufall (j x 2,39996 mod 2 pi).
- (b) gross (0,55) bei -4,3 und klein (0,80) bei +4,3: D = 8,6 = 1,13 x (FWHM(0,55) + FWHM(0,80)).
  Anfangsphase des Kleinen 0, pi/2, pi, 3pi/2.
- Gegenprobe ohne Kopplung: dieselben Laeufe mit D = 30 (Auslaeufer dort ~ 1e-7).
- Messung: Jeder Ball wird ueber das Maximum von |psi|^2 in +-1 um seinen letzten Ort verfolgt. Dort gilt:
  - Phase theta = -arg psi
  - Ort
  - Eigenfrequenz = gamma x (Phasenzuwachs / Zeit), aus dem Ortszuwachs, weil bewegte Uhren langsamer gehen
  - Kuramoto r(t) = |Mittel exp(i theta_j)|
  - Nachbar-Phasendifferenz |dphi|
  - Fenster: Anfang [0, T/10], Ende [3T/4, T]
- **Was "Synchronisation" heisst (vorab):**
  - phasensynchron: r_Ende >= 0,9, kein Ball verschmolzen (Nachbarn > 1,5 auseinander) und r_Ende - r_Ende(Kontrolle) >= 0,3
  - frequenzsynchron: Streuung der Eigenfrequenzen im Endfenster <= 0,2 x Anfangsstreuung der Kontrolle (0,0042),
    ohne Verschmelzen
  - gegenphasig eingerastet: mittleres |dphi|_Ende >= 2,5 und mindestens 0,5 ueber der Kontrolle
  - Mitnahme (b): P = (omega_klein - omega_gross)_Ende / (dieselbe Differenz am Anfang der Kontrolle) <= 0,5, ohne
    Verschmelzen
  - Verschmelzen zaehlt nicht als Synchronisation; es wird getrennt gemeldet.

**Test 2, Absorptionsspektrum (Idee 32).** Ball omega^2 = 0,70 ruhend bei 0. T = 500, Messung alle 0,1. 26 Laeufe.
- Wellenpaket eps exp(-(x - x0)^2 / (2 sigma^2)) exp(i k (x - x0)) mit eps = 1e-3, sigma = 8, x0 = -65, nu^2 = k^2 + 1,
  nach rechts laufend (psi_t mit Huellenbewegung).
- **nu = 1,125 bis 2,5 in Schritten von 0,125 (12 Werte).** Abweichung vom Auftrag: nu = 1,0 laeuft nicht
  (Gruppengeschwindigkeit 0), deshalb beginnt die Reihe bei 1,125.
- Laeufe: Ball + Paket (12), Paket allein (12, Gegenprobe), Ball allein, Ball mit Stoss.
  Der Stoss multipliziert psi und psi_t mit 1,01.
- Messung: Ladungs- und Energiefluss durch die Ebenen x = -30 und +30, ueber die Zeit integriert; Ball-allein-Lauf
  abgezogen.
  - T = Fluss rechts / Einstrom; Einstrom = Fluss links im Lauf ohne Ball
  - R = 1 - Fluss links / Einstrom
  - A = 1 - T - R
  - A0: dasselbe ohne Ball (Rest, der bei T noch unterwegs ist); dA = A - A0
  - Bilanzrest: Ladungsaenderung in |x| < 30 gegen die Fluesse
- Innere Moden: FFT der Breite (Standardabweichung von |psi|^2 in |x| < 30) des gestossenen Balls ab T/8, die drei
  groessten Spitzen.

**Test 3, Virus (Idee 33, Zufallskarte).** T = 600, Messung alle 0,5. 12 Laeufe.
- Gross 0,55 ruhend bei 0; klein 0,90 bei -24 mit v = 0,1 nach rechts (Lorentz-Boost).
- "Gleichphasig" gilt nur im Kontaktmoment, weil die relative Phase mit 0,202 umlaeuft (Periode 31).
  - Deshalb acht Laeufe mit Soll-Phasendifferenz 0, pi/4, ..., 7pi/4 beim freien Kontakt: Abstand 5,50 bei t = 185.
  - Gemessen wird die tatsaechliche Differenz beim ersten Abstand unter 5,50.
  - gleichphasig = Soll 0, gegenphasig = Soll pi; die Zwischenwerte zeigen den Uebergang.
- Referenzen: gross allein; gross mit Stoss (Moden vorher); Ersatzball 0,5128 mit Stoss (Soll-Moden nachher);
  klein allein (Kontrolle des Boosts).
- Messung:
  - Klumpen = Fenster +-10 um das Maximum von |psi|^2: Ladung, Energie, Breite, Phase
  - kleiner Ball = Maximum links davon
  - Ladung und Energie der Box
- Kenngroessen:
  - M = (Q_Klumpen(T) - Q_Klumpen(0)) / Q_klein; verschmolzen ab 0,7, getrennt bis 0,3
  - omega^2 des Klumpens im Endfenster gegen omega^2 des Ankers mit derselben Ladung; Anregung = E_Klumpen - E_Anker(Q)
  - Breite-FFT nach dem Stoss, ab T/2

**Test 4, Gedaechtnis (Idee 31), 3D radial, nur Schiessen.** omega^2 = 0,51 bis 0,99 in 0,01 (49 Werte).
- Zustand u = f_top - f; f_top ist der Buckel des Teilchenpotentials, S+ = (2 + sqrt(4 - 6 a0))/3.
  - Die rechte Seite ist das exakte Taylor-Polynom um f_top. Damit bleiben duenne Waende mit
    f(0) = f_top - e^-100 rechenbar; in f(0) selbst waeren sie in float64 nicht darstellbar.
  - Geschossen wird in s = -ln(f_top - f(0)) in [s_min, 150]: 4 Runden x 1024 Kandidaten, RK4 mit h = 0,05 bis r = 150.
  - Start ueber die Reihe u0 + a r^2 + b r^4.
- Q = 2 omega 4 pi Int f^2 r^2 dr, E = 4 pi Int (omega^2 f^2 + f'^2 + U) r^2 dr, Trapez bis f < 1e-3 f(0) plus
  exponentieller Schwanz.
- Kontrollen:
  - dasselbe Verfahren in d = 1 bei 0,55 / 0,70 / 0,90 gegen den Anker
  - Pohozaev-Rest (G + 3 (V - W))/E
  - dE/dQ = omega
- Auswertung:
  - dQ/domega (zentrale Differenzen) und dessen Vorzeichenwechsel
  - Q_min (Parabel durch das Gitterminimum)
  - E auf beiden Aesten bei gleichem Q (1,2 bis 5 x Q_min)
  - omega-Bereich mit E < Q

## 2. Aufruf (Leitung, auf der .69, Quadro P4000 ueber kleintest.sh)

Vorschlag: Remote-Ordner /home/fmh/fmhc-physics-remote/tests1d-20260930/ mit tests1d.py darin.
- kleintest.sh setzt Sperre, Unit, CUDA_VISIBLE_DEVICES, RuntimeMaxSec 600 und das Arbeitsverzeichnis selbst.
- Das Programm braucht nur torch und schreibt nur in --out. Die Pfade fuer --out und --profil stehen absolut, damit sie
  nicht vom Arbeitsverzeichnis abhaengen.

**Rauchtest** (alle vier Tests, Laufzeiten x 0,05, Test 4 mit einer Schiessrunde; schiesst und speichert die 1D-Profile):

```
cd /home/fmh/fmhc-physics-remote/tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a t1d-rauch tests1d.py --rauch --out /home/fmh/fmhc-physics-remote/tests1d-20260930/rauchtest
```

**Hauptlauf**, ein Aufruf je Test, nur wenn der Rauchtest rc = 0 hatte (Tests 1 bis 3 laden die Profile des Rauchtests):

```
cd /home/fmh/fmhc-physics-remote/tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a t1d-t4 tests1d.py --tests 4 --out /home/fmh/fmhc-physics-remote/tests1d-20260930/ausgabe-t4
cd /home/fmh/fmhc-physics-remote/tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a t1d-t1 tests1d.py --tests 1 --profil /home/fmh/fmhc-physics-remote/tests1d-20260930/rauchtest/profil_1d.pt --out /home/fmh/fmhc-physics-remote/tests1d-20260930/ausgabe-t1
cd /home/fmh/fmhc-physics-remote/tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a t1d-t2 tests1d.py --tests 2 --profil /home/fmh/fmhc-physics-remote/tests1d-20260930/rauchtest/profil_1d.pt --out /home/fmh/fmhc-physics-remote/tests1d-20260930/ausgabe-t2
cd /home/fmh/fmhc-physics-remote/tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a t1d-t3 tests1d.py --tests 3 --profil /home/fmh/fmhc-physics-remote/tests1d-20260930/rauchtest/profil_1d.pt --out /home/fmh/fmhc-physics-remote/tests1d-20260930/ausgabe-t3
```

- **Warum einzeln:**
  - RuntimeMaxSec 600 gilt je Aufruf. Einzeln bleibt jeder Test auch in der oberen Schaetzung unter 3 min, und ein
    Abbruch trifft nur diesen Test.
  - `--tests 123` in einem Aufruf passt ebenfalls (obere Schaetzung etwa 7 min), aber mit weniger Reserve.
  - Die fertigen Tests eines Aufrufs bleiben ohnehin erhalten, weil das Programm nach jedem Test schreibt.
- Der Rauchtest zeigt nur, ob alles durchlaeuft; seine Zahlen gelten nicht (zu kurz, Test 4 zu grob).
- **Hochrechnung** aus den gedruckten Teilzeiten des Rauchtests:
  - Test 4 mal 2,5 (4 + 1 statt 1 + 1 Durchgaenge)
  - jede Entwicklungszeit der Tests 1 bis 3 mal 20
  - je Aufruf etwa 10 s Start dazu
  - Ergibt ein Test mehr als 9 min, diesen nicht starten; die Leitung entscheidet.

## 3. Erwartete Laufzeit (Schaetzung fuer die P4000, nicht gemessen)

Grundlage sind die QG-1-Messungen auf der P5000:
- 1,2 ms je Verlet-Schritt, gleich fuer 27 x 2401 und 27 x 4801 Punkte
- 2,1 ms je RK4-Schiessschritt
- 84 s fuer das 1D-Schiessen

Diese Werte sind mit dem float64-Faktor 1,7 der Leitung auf die P4000 hochgerechnet. Die Laeufe sind durch
Kernelstarts begrenzt, nicht durch die Arithmetik; 1,7 ist daher eher eine obere Schranke (erwartet 1,0 bis 1,7).

| Teil | Arbeit | P5000 | P4000 (x 1,7) |
|---|---|---|---|
| Start je Aufruf | Python, CUDA | 5 bis 15 s | 5 bis 15 s |
| Rauchtest | 1D-Schiessen (9 omega), Test 4 mit 1 + 1 Durchgaengen, Tests 1 bis 3 mal 0,05 | 1,5 bis 2,5 min | 2,5 bis 4,5 min |
| Test 4 | 52 omega x 1024 Kandidaten; 4 x 2999 + 2999 RK4-Schritte | 30 bis 70 s | 50 bis 120 s |
| Test 1 | 20 Laeufe; grob 8000, fein 16000 Schritte | 25 bis 60 s | 45 bis 100 s |
| Test 2 | 26 Laeufe; grob 10000, fein 20000 Schritte, Messung alle 0,1 | 40 bis 90 s | 70 bis 155 s |
| Test 3 | 12 Laeufe; grob 12000, fein 24000 Schritte | 35 bis 80 s | 60 bis 135 s |
| **Hauptlauf, vier Aufrufe zusammen** | | 2,5 bis 5,5 min | **4 bis 9,5 min, erwartet etwa 5,5 min** |

- Jeder einzelne Test braucht auf der P4000 hoechstens etwa 2,5 min plus Start, also weit unter 10 min.
- Rauchtest und Hauptlauf zusammen etwa 9 min, verteilt auf fuenf Aufrufe (6,5 bis 14 min).
- **Speicher:**
  - Groesstes Feld: 26 x 6001 complex128 = 2,5 MB.
  - Alle Tensoren zusammen unter 0,1 GB, mit CUDA-Kontext geschaetzt unter 0,6 GB (Vorgabe hoechstens 2,5 GB).
  - Der Code deckelt den Torch-Speicher mit torch.cuda.set_per_process_memory_fraction auf 2,5 GB und meldet den
    Hoechststand am Ende des Berichts.

## 4. Vorhersagen (vor dem Rechnen, von Hand)

**Test 1.** Papierbild: Zwei Baelle tauschen ueber die Auslaeufer Ladung aus wie ein Josephson-Kontakt.
- Strom J sin(dphi) mit J = 4 kappa A^2 e^(-kappa D); kappa = sqrt(1 - omega^2) = 0,548, A^2 = 4 a0/b0 = 1,90.
  J = 0,052 / 0,010 / 0,0020 / 3e-7 bei D = 8 / 11 / 14 / 30.
- Weil in 1D domega/dQ = -0,101 < 0 ist (VK-stabil), gilt dphi'' = 2 |domega/dQ| J sin(dphi).
  - Stabil ist also **gegenphasig** (dphi = pi); gleichphasig ist instabil.
  - Rastfrequenz 0,10 / 0,045 / 0,020. Nachbarn rasten ein, solange ihr Frequenzabstand (0,006 bis 0,009) unter
    2 sqrt(2 |domega/dQ| J) liegt; das gilt bis D ~ 19.
- Mechanisch ziehen sich gleichphasige Baelle an (Kontakt nach etwa 30 / 80 / 200 Zeiteinheiten); gegenphasige stossen
  sich ab (Endgeschwindigkeit etwa 0,3 / 0,13 / 0,06).
- **V1a:** In keinem gekoppelten Lauf gibt es gleichphasige Synchronisation ohne Verschmelzen
  (phasensynchron 0 von 9 in (a)).
- **V1b:** Die gleichphasig gestarteten Ketten verschmelzen bei D = 8 und 11 (verschmolzen >= 1), bei 14 wahrscheinlich.
- **V1c:** Die wechselnd gestarteten Ketten verschmelzen nicht, sie laufen auseinander.
  - Gegenphasige Rastung sieht man nur, solange Nachbarn naeher als ~19 sind.
  - Im Endfenster erwarte ich sie hoechstens in einem Lauf (unsicher).
- **V1d:** Frequenzsynchron in keinem Lauf ohne Verschmelzen (Streuverhaeltnis > 0,2).
- **V1e (b):**
  - Frequenzabstand 0,153, Kopplungskonstante ~0,006: Rastung nur bei Start nahe gegenphasig (|dphi_0 - pi| < 0,4).
  - Mitnahme P <= 0,5 hoechstens im Lauf mit Phase pi; sonst P = 1 +- 0,2.
  - Die Frequenz des Kleinen schwingt mit etwa 0,03 (Periode ~41).
  - Ein Herzschrittmacher-Effekt ohne Verschmelzen waere ein Befund-Kandidat.
- **Kontrolle D = 30:** r_Ende ~ 0,2 beim gleichen Start (Auseinanderlaufen der Phasen), keine Frequenzaenderung, P = 1.

**Test 2.**
- Papierbild: Der Ball hat innere Moden nur in der Luecke Omega < 1 - omega = 0,163; im Labor liegen sie unter der
  Massenschwelle 1.
- Das Band nu = 1,125 bis 2,5 liegt ganz im Kontinuum (Omega = nu - omega = 0,29 bis 1,66). Der Partnerkanal
  2 omega - nu = -0,83 bis 0,55 ist geschlossen.
- Deshalb gilt in linearer Ordnung T + R = 1 genau, und A ist hoechstens von der Ordnung eps^2 ~ 1e-6.
- **V2a:** |dA_Q| und |dA_E| < 1e-4 fuer alle 12 nu. Keine Absorptionslinie; Schwelle fuer einen Befund 1e-3 mit
  bestandenem L3.
- **V2b:** R faellt mit nu. R(1,125) zwischen 1e-3 und 0,3, R(2,5) < 1e-3 (Schaetzung, nicht gerechnet).
- **V2c (Gegenprobe):** Ohne Ball T0 = 1 auf 2e-4. Der Rest ist Ladung, die bei nu = 1,125 noch unterwegs ist.
- **V2d:** Der gestossene Ball schwingt in der Breite hauptsaechlich mit Omega <= 0,163, also mit einer inneren Mode oder
  an der Kontinuumskante. Ueber 0,2 kommen nur Oberschwingungen vor.
- **Bilanzrest:** unter 1e-3.

**Test 3.**
- Papierbild: In 1D ist E(Q) unteradditiv. Der Ersatzball (Q = 5,105) hat E = 4,31 gegen 4,65 vorher (einschliesslich
  Bewegung); Verschmelzen setzt also 0,34 frei, als Strahlung oder Anregung.
- Gleichphasige Baelle ziehen sich an, gegenphasige stossen sich ab. Die Barriere liegt bei ~0,05, weit ueber der
  Bewegungsenergie 0,006.
- **V3a:** Verschmelzen (M >= 0,7), wenn die gemessene Kontaktphase nahe 0 liegt (|dphi| < pi/2); Trennung (M <= 0,3)
  nahe pi. Mindestens 2 der 8 Phasen verschmelzen und mindestens 2 trennen sich.
- **V3b:** Bei Verschmelzen liegt M zwischen 0,7 und 1; die Box verliert 1 bis 10 % der Ladung; die Anregung ist > 0.
- **V3c:** omega^2 des Klumpens am Ende liegt auf 0,01 bei omega^2_Anker(Q_Klumpen), also nahe 0,513.
- **V3d:** Die Hauptfrequenz der Breite nach dem Verschmelzen liegt innerhalb 0,042 (zwei FFT-Stufen) bei der des
  gestossenen Ersatzballs.
  - Der "Virus" aendert die Moden nur ueber die Ladung.
  - Eine eigene, bleibende neue Mode (Abweichung > 0,042 bei bestandenem L3) waere ein Befund-Kandidat.
  - Schwellen 1 - omega: 0,258 (0,55), 0,284 (0,513).

**Test 4 (die L1-Probe aus dem Auftrag).**
- **V4a:** dQ/domega wechselt genau einmal das Vorzeichen (ein Minimum).
  - Die duenne Wand (omega < omega_c) ist VK-stabil, die dicke Wand (omega > omega_c) VK-instabil.
  - Zwei Loesungen bei gleichem Q gibt es fuer Q > Q_min, stabil ist aber nur eine: **kein Gedaechtnis**.
- **V4b:** omega^2_c zwischen 0,75 und 0,95, Q_min zwischen 30 und 150 (grob aus den Grenzfaellen).
- **V4c:** Grenzfaelle:
  - Q(0,51) ~ 2e6 bis auf Faktor 1,5 (duenne Wand R = 0,707/(omega^2 - 1/2) = 71, Q ~ (8 pi/3) omega R^3)
  - Q(0,99) = 190 bis 210 (NLS-Grenze 18,9 omega / sqrt(1 - omega^2) = 188)
  - s(0,51) ~ 100
- **V4d:** Bei gleichem Q liegt die dicke Wand energetisch hoeher (Spitze in E(Q)).
  - Nahe omega^2 = 1 gilt E > Q (NLS-Grenze E/Q ~ 1 + (1 - omega^2)/2).
  - Dort ist die dicke Wand auch gegen Zerfall in freie Quanten instabil.
- **Kontrollen:** d = 1 gegen den Anker < 1e-5 relativ; Pohozaev-Rest < 1e-4; Median |dE/dQ / omega - 1| < 1e-2
  (grobes omega-Gitter).
- **Gegenhypothese:** Ein zweites Minimum, also ein Abschnitt mit dQ/domega < 0 auf der dicken Seite, gaebe zwei stabile
  Aeste bei gleichem Q, also ein Bit.

## 5. Gegenproben

| Test | Gegenprobe | im Code |
|---|---|---|
| 1 | grosser Abstand D = 30 (keine Kopplung); feine Stufe dx/2, dt/2 | Kontroll-Laeufe, Stufe "fein" |
| 2 | Paket ohne Ball (volle Transmission); Ball ohne Paket (abgezogen); feine Stufe | Laeufe 13 bis 24 (Paket allein), 25 (Ball allein) |
| 3 | gegenphasig (Soll pi) und alle Zwischenphasen; gross allein; kleiner allein; feine Stufe | Laeufe 1 bis 8 (Phasen), 9 bis 12 (Referenzen) |
| 4 | d = 1 gegen den Anker; Pohozaev; dE/dQ = omega | kontrolle_1d, virial |

"Halber Zeitschritt": Die feine Stufe halbiert wie in QG-1 dx und dt zugleich. Sie enthaelt also den halben Zeitschritt
und ist strenger. Nur dt: FEIN im Code bleibt 0,5, und in stufen_rechnen DX * FEIN durch DX ersetzen (eine Stelle).

## 6. Latten (Vorschlag, die Leitung entscheidet)

| Latte | Test 1 Uhren | Test 2 Absorption | Test 3 Virus | Test 4 Gedaechtnis |
|---|---|---|---|---|
| L1 kann scheitern | ja: r_Ende >= 0,9 ohne Verschmelzen oder P <= 0,5 widerspraeche V1a/V1e | ja: dA > 1e-3 widerspraeche V2a | ja: Verschmelzen unabhaengig von der Phase, oder eine neue Mode nach dem Verschmelzen | ja: dQ/domega < 0 auf der dicken Seite |
| L2 Gegenprobe | ja: D = 30, drei Phasensaetze | ja: ohne Ball, ohne Paket | ja: acht Phasen, Referenzbaelle | nur Kontrollen (d = 1, Pohozaev) |
| L3 Numerik | im Code: Effekt >= 5 x Aenderung grob -> fein fuer r, Frequenzstreuung, P | im Code fuer R und dA | im Code fuer M | Klammerbreite, d = 1 gegen Anker; kein zweites Gitter |
| L4 schon bekannt | teilweise: phasenabhaengige Kraefte (Battye/Sutcliffe 2000, Axenides u. a. 2000), Ladungsaustausch (Copeland/Saffin/Zhou 2014); das Pendelbild folgt vorab aus dQ/domega | weitgehend: Spektrum des linearisierten Operators, Moden in der Luecke | weitgehend: Q-Ball-Stoesse in 1D sind Literatur | ja: VK-Kriterium, duenne/dicke Wand (Coleman; Lee/Pang; Tsumagari/Copeland/Saffin 2008) |
| L5 Messbezug | nein (Analogie) | nein | nein | nein |

Literatur aus dem Gedaechtnis, nicht nachgelesen.

## 7. Ausgabedateien (im --out-Ordner)

- `tests1d_bericht.txt`: Tabellen je Test und Stufe, Kontrollen, L3-Zaehlung; auch auf stdout
- `tests1d_ergebnis.json`: alle Kenngroessen; Laufliste je Test; Fehlertexte, falls ein Test scheiterte
- `tests1d_zeitreihen.pt`: Rohmessungen je Test und Stufe, Spalten laut Code:
  - Test 1: 5 Orte, 5 Phasen, 5 |psi|^2
  - Test 2: jL, SL, jR, SR, Q_Mitte, Breite, S_max
  - Test 3: 11 Spalten
- `profil_1d.pt`: 1D-Schiessbahnen (nur bei eigenem Schiessen)

## 8. Grenzen

- **Ungetestet:** Das Programm ist nie gelaufen, daher zuerst der Rauchtest. Wahrscheinlichste Fehlerstellen:
  Tensorformen in den Messfunktionen, torch.linalg.lstsq in der FFT-Hilfe.
- **Anfangsfelder:** Mehrere Baelle sind als Summe gesetzt. Bei ueberlappenden Auslaeufern (D = 8) ist das keine exakte
  Loesung; die Baelle starten leicht angeregt.
- **Verfolgung:** ueber Maxima von |psi|^2. Bei Verschmelzen oder Durchdringen koennen Tracker springen oder
  zusammenfallen; das wird als "verschmolzen" gezaehlt, nicht gedeutet.
- **Test 2:**
  - Endliche Pakete haben eine Frequenzbreite (Delta nu ~ v_g / 11, bei nu = 2,5 etwa 0,08).
  - Die langsamsten Anteile bei nu = 1,125 sind bei T = 500 noch zu ~1e-4 unterwegs (A0).
- **Test 3:** Die Kontaktphase haengt vom tatsaechlichen Anlauf ab. Die acht Soll-Phasen tasten sie ab; gedeutet wird
  die gemessene.
- **Test 4:**
  - Nur Profile und VK-Vorzeichen, keine Zeitentwicklung.
  - omega-Gitter 0,01, an der duennen Wand grob, weil Q sich dort pro Schritt um Faktoren aendert.
  - dE/dQ ist nur ein Plausibilitaetstest.
- **Allgemein:** 1D, ein Kanal, explorativ. Die Tests 1 bis 3 sagen nichts ueber 3D, Test 4 nichts ueber 1D.
- **Laufzeit P4000:** nur hochgerechnet (P5000-Messung mal 1,7). Der Rauchtest liefert die ersten echten Teilzeiten auf
  der Karte.

## Einfach gesagt

Wir pruefen am Rechner vier Ideen, bei denen Q-Baelle sich wie Lebewesen verhalten sollen: ob benachbarte Baelle wie
Uhren in den Gleichtakt kommen, ob ein Ball nur Wellen "schluckt", die zu ihm passen, was ein kleiner Ball in einem
grossen anrichtet, und ob ein Ball zwei stabile Zustaende als Gedaechtnis haben kann. Nach der Papierrechnung klappt fast
nichts davon so, wie die Biologie-Analogie es nahelegt: Nachbarn rasten eher im Gegentakt ein oder verschmelzen, Wellen
im laufenden Bereich laufen einfach vorbei, der verschmolzene Ball schwingt wie jeder gewoehnliche Ball derselben
Groesse, und der zweite Zustand fuer das Gedaechtnis ist instabil. Der Rechenlauf soll das auf einer zweiten
Grafikkarte (P4000) in zusammen knapp zehn Minuten nachpruefen, jeder Test in hoechstens drei Minuten; spannend wird es,
wo er der Vorhersage widerspricht. Gerechnet ist noch nichts.

Ende der ersten Fassung: 2026-09-30 01:31:01 CEST. Umstellung auf die P4000: 2026-09-30 01:35:11 CEST (beide gemessen mit date).
