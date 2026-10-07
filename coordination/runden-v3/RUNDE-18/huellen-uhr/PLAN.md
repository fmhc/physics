# PLAN HUELLEN-UHR (Runde 18)

- Code-Agent, Start 2026-10-02 12:45:06 CEST (date). Plan geschrieben ab 12:56 CEST, vor jeder Rechnung und vor dem
  ersten .69-Aufruf. Explorativ (v3), Deutungen sind Hypothesen [H].
- Verbindlich aus der Karte: Modell M2, Stellen S-a und S-b, Arme (i) bis (iv), Messgroessen, H1 bis H5, Bedeutung.
  Hier stehen nur die Ausfuehrung und die Wertungsregeln, die die Karte offen laesst (als "Festlegung" markiert).

## 1 Zeitloeser (eigener Code code/huelle.py, numpy; scipy nur fuer Hintergrund-Newton und Modensuche)

- Variablen u = r psi (komplex), v = r (chi - 1) (reell). Gitter r_i = i h, i = 0..N, R = 120.
- Radialer Laplace: Differenzenstern 4. Ordnung auf u und v, ungerade Spiegelung an r = 0 (u_0 = 0, u_-k = -u_k) und
  an r = R (Dirichlet). Die Matrix D2 ist damit symmetrisch.
- Gleichungen: u_tt = D2 u - U_S u - sig u_t, v_tt = D2 v - r U_chi - sig v_t, mit S = |u|^2/r^2, chi = 1 + v/r,
  U_S = 1 + chi^2 - 2S + 1,5 S^2, U_chi = chi (chi^2 - 1) + 2 chi S.
- Zeitschritt: RK4, dt = h/4 (CFL: omega_max dt ~ 0,58 < 2,8).
- Schwammschicht: sig(r) = 2 ((r - 60)/60)^3 fuer 60 < r <= 120, sonst 0.
- Messkugel r_m = 50 (Index m = 50/h), Hilfskugel r_n = 25 (nur Zusatzangabe).
- Erhaltungsgroessen exakt diskret (Halbdiskretisierung, D2 symmetrisch):
  - E = 4 pi h Sum_i [|u_t|^2 - Re(u* D2u) + r^2 U + (1/2) v_t^2 - (1/2) v D2v], U wie Karte.
  - Q = 4 pi h Sum_i 2 Im(u* u_t).
  - Fluss durch die Kugel zwischen m und m+1: exakter diskreter Fluss aus den Kopplungen D2_ij mit i <= m < j
    (Paare (m, m+1), (m-1, m+1), (m, m+2)); fuer E und Q. Die Flussintegrale und die im Schwamm absorbierte Energie
    und Ladung laufen als Zusatzgleichungen im RK4 mit.
  - Bilanz innerhalb r_m: E_in(t) + E_aus(t) - E_in(0); gesamt: E(t) + E_abs(t) - E(0); ebenso Q.

## 2 Hintergrund

- Saat und Fortsetzung mit stille3.py (RUNDE-17/stille-zweifeld/code, unveraendert kopiert, mit beutel.py):
  saat(M2, Q = 200, hp = 0,05), fortsetzung in Schritten 0,02 bis zur Ziel-omega^2.
- Dann eigener Newton auf meinem Gitter (D2 4. Ordnung, R = 120) fuer F = r f, H = r (g - 1); Abbruch Schritt
  < 1e-12 max|F|. Damit ist der Hintergrund eine exakte stationaere Loesung meiner Halbdiskretisierung.
- Hintergruende: omega^2 = 0,86085981 und 0,87085981 (S-a, (i) und (ii)), 0,84743426 und 0,85743426 (S-b).

## 3 Moden

- Linearisierung (wie STILLE-ZWEIFELD, c' = c/2): L(rho) = -D2 + M - E(rho), Kanaele (A, B, C') = r (a, b, c/2),
  M = [[U_S + S U_SS, S U_SS, 2fg], [S U_SS, U_S + S U_SS, 2fg], [2fg, 2fg, U_chichi]],
  E = diag((w+rho)^2, (w-rho)^2, rho^2). Diskret mit derselben D2, auf dem Kasten r <= R_box = 50 (Dirichlet).
- Prozedur (fuer (i) und (ii) gleich): eigsh, 6 Eigenwerte nahe 0 (Shift 1e-4). Auswahl: (i) die am staerksten
  lokalisierte Eigenrichtung (Gewicht in r < r_half + 10), (ii) die mit dem groessten Ueberlapp zur (i)-Mode.
  Newton in rho auf lambda(rho) = 0 (Ableitung nach Hellmann-Feynman), Start bei rho der Karte, bis |lambda| < 1e-12
  oder 20 Schritte. (ii) startet bei rho(i).
- Lokalisierung (Kontrolle): Betrag der a-Komponente in r in [r_half + 15, 45] relativ zum Maximum der Mode, dazu b, c.
  Erwartung (i): abklingend; (ii): stehende Welle mit Amplitude ungleich null.
- Normierung (Festlegung): eps = max_r |delta S(r, 0)| / S(0), delta S = 2 f (a + b), S(0) = f(0)^2.
  eps in {0,002; 0,005}. Vorzeichen so, dass delta S(0, 0) > 0.
- Anfangsdaten (i), (ii): u = F + eps (A + B), u_t = i w F + i eps ((w + rho) A + (w - rho) B), v = H + eps 2 C',
  v_t = 0.

## 4 Arme (eine Rechnung je Stelle und Gitter, 8 Zeilen gebuendelt)

- Zeile 0: Nullarm (iv) auf Hintergrund (i). Zeilen 1, 2: (i) mit eps 0,002 / 0,005.
- Zeile 3: Nullarm auf Hintergrund (ii) (Referenz fuer (ii)). Zeilen 4, 5: (ii) mit eps 0,002 / 0,005.
- Zeilen 6, 7: (iii) auf Hintergrund (i): Stoss in chi, v_t(r, 0) = r A_k exp(-r^2 / sigma_k^2), sigma_k = 2
  (Festlegung), A_k so, dass die diskrete Anregungsenergie gleich |E_exc(i)| beim selben eps und Gitter ist.
- E_exc = E_in(0) - E_in(0) des zugehoerigen Nullarms.
- Gitter h = 0,05 (grob) und h/2 = 0,025 (fein). T = 50 Perioden 2 pi/rho der Karte (S-a 293,7; S-b 234,5).
- Aufzeichnung: Zentrumsdichte |psi(0)|^2 (Extrapolation 4. Ordnung aus psi_1..3) alle 2 Schritte; E_in, Q_in, E, Q,
  Flussintegrale, Absorption alle 8 Schritte. Zwischenstand alle 10 % der Laufzeit gespeichert (atomar).

## 5 Messgroessen und Auswertung (Festlegungen)

- Signal x(t) = |psi(0,t)|^2 - |psi(0,t)|^2 des zugehoerigen Nullarms.
- Ticks: A_ref = max |x| in den ersten 2 Perioden. Hysterese: scharf, wenn x < -0,5 A_ref; Tick, wenn danach
  x > +0,5 A_ref; Tickzeit = letzter Aufwaerts-Nulldurchgang (linear interpoliert) davor. Periode = Steigung der
  Tickzeiten gegen den Index (kleinste Quadrate), dazu Mittel und Streuung der Abstaende.
  Nullarm: x = Dichte minus Anfangswert, Schwellen von (i) bzw. (ii) bei eps 0,002 desselben Laufs.
- Abklingrate: Amplitude je Fenster einer Modenperiode ((max - min)/2 von x), Fit ln A = a - gamma t ab t >= 5 Perioden.
- Abgestrahlter Anteil bis T: f_rad = E_aus(r_m, T) / E_exc. Fuer (iii) mit E_exc = |E_exc(i)|.
- Bilanzfehler: max_t |E_in + E_aus - E_in(0)| relativ zu |E_exc| (angeregte Arme) bzw. zu E_in(0) (Nullarme);
  ebenso Q (relativ zu Q_in(0)). Gesamtbilanz mit Absorption zusaetzlich.
- Exponent fuer H4: p = ln(E_aus(eps 0,005) / E_aus(eps 0,002)) / ln 2,5.

## 6 Wertung H1 bis H5 (Festlegung der Operationalisierung)

- Gewertet wird das feine Gitter. Weicht der Ausgang auf dem groben Gitter ab, heisst der Ausgang "offen (Gitter)".
- H1: beide Nullarme, beide Stellen: 0 Ticks und relative E- und Q-Bilanz < 1e-6.
- H2: (i), beide eps, beide Stellen: |P_tick - 2 pi/rho| / (2 pi/rho) < 1e-3 (rho der Karte), mindestens 30 Ticks.
- H3: f_rad(ii) / f_rad(i) >= 30 bei beiden eps und beiden Stellen.
- H4: (i) 3,5 <= p <= 4,5 und (ii) 1,5 <= p <= 2,5, an beiden Stellen.
- H5: (iii) f_rad > 0,5 bei beiden eps und beiden Stellen.

## 7 Vorab-Kontrollen

- Absorber-Reflexion: Vakuum (f = 0, chi = 1), Pakete r0 = 30, Breite 6, Amplitude 1e-3, nach aussen laufend:
  psi k0 = 1,41 und 0,7; chi k0 = 1,6 und 0,7. T_end = 500, grobes Gitter. Reflexion = E(r < 55, T_end) / E(0).
  Annahme des Schwamms bei < 1e-6. Sonst Nachtrag (Schwamm laenger/staerker) vor den Hauptlaeufen.
- Rauchtest: kurzer Lauf (T = 5) je Stelle auf dem groben Gitter fuer Laufzeit und Bilanz; nicht gewertet.

## 8 Rechnen

- Code per rsync nach /home/fmh/fmhc-physics-remote/runde18-huellen-uhr/, Aufrufe ueber kleintest.sh, Spuren cpu und
  cpu2, je <= 600 s. Threads = 1. Neue Ausgabedateien je Lauf, kein Ueberschreiben laufender Dateien.
- Abbildungen mit matplotlib auf der .69.
