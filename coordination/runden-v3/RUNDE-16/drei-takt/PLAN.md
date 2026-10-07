# PLAN drei-takt (Runde 16, Code-Agent)

- Start der Zeitbox: 2026-10-02 08:33:37 CEST (date). Ende spaetestens 10:03:37 CEST.
- Plan geschrieben ab 2026-10-02 08:40:34 CEST (date), vor jedem Lauf auf der .69. Grundlage ist KARTE.md, unveraendert.
- Vor dem Einfrieren nur lokale Rauchtests (System-python3, nice 19, timeout, ein Thread): winzige Gitter, nur Laufzeit
  und die e = 0-Kontrollen, keine Auswertung der Hypothesen.

## Methode je Teil

### D1a (Floquet, elliptisch, linear)

- Gleichungen wie Karte: x'' - 2y' = (Uxx x + Uxy y)/(1 + e cos f), y'' + 2x' = (Uxy x + Uyy y)/(1 + e cos f),
  Uxx = 3/4, Uyy = 9/4, Uxy = (3 sqrt3/4)(1 - 2mu).
- Schreibtischpruefung (vor dem Lauf, Leitung [L?] -> selbst nachgerechnet):
  - Aus Omega = (x^2+y^2)/2 + (1-mu)/r1 + mu/r2 mit m1 = 1-mu bei (-mu,0), m2 = mu bei (1-mu,0), L4 = (1/2-mu, sqrt3/2)
    folgen Omega_xx = 3/4, Omega_yy = 9/4, Omega_xy = (3 sqrt3/4)(1-2mu).
  - Bei e = 0: lambda^4 + (4 - Uxx - Uyy) lambda^2 + (Uxx Uyy - Uxy^2) = lambda^4 + lambda^2 + (27/4) mu(1-mu). Stimmt
    mit der Karte. Routh: 1 - 27 mu(1-mu) = 0, also mu_R = (1 - sqrt(69)/9)/2.
  - Die Form "ganze Hesse-Matrix von Omega geteilt durch (1 + e cos f)" ist die uebliche pulsierende Form
    (Szebehely-Konvention) [L?]. Kein Konventionsunterschied an e = 0 erkennbar; numerische Kontrolle unten.
- Numerik: 4x4-Fundamentalsystem (x, y, x', y') ueber f = 0 bis 2 pi, RK4 mit fester Schrittzahl n = 2000 und n = 4000,
  vektorisiert ueber das Gitter.
- Gitter A: mu = 0 bis 0,06 in Schritten 0,0005 (121), e = 0 bis 0,6 in Schritten 0,005 (121).
- Gitter B: mu in Schritten 0,00025 (241), e in Schritten 0,0025 (241).
- Stabil: max |rho| <= 1 + tol, tol = 1e-6 (Karte). Gegenprobe: tol = 1e-4, und Multiplikatoren aus dem
  charakteristischen Polynom (Broucke-Form sigma = rho + 1/rho) statt eigvals. Kontrolle det M = Produkt der
  Multiplikatoren = 1.
- Grenzlinien: Uebergaenge stabil/instabil je e-Zeile auf A und B; dazu Bisektion (14 Schritte, n = 4000) fuer
  e in {0; 0,005; 0,01; 0,02; 0,04; ...; 0,6}.
- Kontrollen: Bisektion bei e = 0 trifft mu_R = 0,0385209 auf 1e-4; Multiplikatoren bei e = 0 gleich exp(2 pi lambda_k)
  aus der Eigenwertgleichung; bei mu = 0,0285955 und e = 0 zwei Multiplikatoren bei -1; Zungengrenzen laufen fuer
  e -> 0 auf 0,0285955 zu.

### D1d (Takt Omega, e = 0, linear)

- Rechte Seiten = die U-Terme wie in D1a (Coriolis-Terme unveraendert), mal (1 + eps cos(Omega t)). Das ist die
  woertliche Lesart der Karte ("rechte Seiten mal ..."); bei Omega = 1 und kleinem eps entspricht das D1a mit e = eps
  in erster Ordnung (1/(1+e cos f) ~ 1 - e cos f). Diese Uebereinstimmung ist eine zusaetzliche Kontrolle.
- Zeit tau = Omega t, Periode 2 pi in tau; Schrittzahl je Omega n = max(400, ceil(2 pi/(Omega h))) mit h = 0,01 in t,
  Wiederholung mit doppelter Schrittzahl.
- Gitter: Omega 0,2 bis 10 in Schritten 0,01 (981), eps 0 bis 0,3 in Schritten 0,005 (61), mu in
  {0,01; 0,02; 0,035; 0,0390; 0,0400; 0,0420}.
- Auswertung: Instabilitaetsintervalle in Omega bei eps = 0,1; 0,2; 0,3 mit naechster Resonanz 2 s_k/n (n = 1..4),
  |s1 - s2|/n und (s1 + s2)/n (n = 1..3); s1, s2 aus der Eigenwertgleichung. Fuer mu > mu_R: alle stabilen Punkte
  mit eps > 0 und ihr Omega-Bereich.
- Erwartung aus der Krein-Theorie (Hypothese des Agenten, vor dem Lauf): die zwei L4-Moden haben entgegengesetzte
  Krein-Signatur, daher Zungen bei 2 s_k/n und |s1 - s2|/n, nicht bei (s1 + s2)/n.

### D1b (Lebensdauer, kreisfoermig, nichtlinear)

- Volle Gleichungen im mitrotierenden System, m1 = 1-mu bei (-mu,0), m2 = mu bei (1-mu,0).
- mu in {0,0386; 0,0387; 0,0388; 0,0390; 0,0393; 0,0396; 0,0400; 0,0405; 0,0410; 0,0420; 0,0430; 0,0440; 0,0450;
  0,0475; 0,0500}, Auslenkung 0,005 und 0,02 in 64 Richtungen, Startgeschwindigkeit null im mitrotierenden System
  (Karte legt sie nicht fest; Festlegung hier).
- RK4, dt = 2 pi/400, bis 1000 Umlaeufe. Ende: Abstand zu L4 > 0,5 oder r2 < 0,05 (jeder Schritt geprueft).
- Gemessen: Lebensdauer (Umlaeufe), Anteil gefangen nach 1000 Umlaeufen, groesste Auslenkung (fuer Gefangene).
- Lineare Referenz: Re lambda = Wachstumsrate aus der Eigenwertgleichung, T_lin = ln(0,5/delta)/Re lambda.
  Fit log(Median-Lebensdauer) gegen log(mu - mu_R) nur ueber mu, bei denen alle Teilchen entkommen.
- Kontrollen: Jacobi-Konstante (relativ) fuer Gefangene < 1e-9; Stichprobe mu in {0,0386; 0,039; 0,042}, 16 Richtungen
  je Auslenkung, mit dt/2.

### D1c (Chaos nahe L4, elliptisch, nichtlinear; nur wenn Zeit bleibt)

- Volle Gleichungen in pulsierenden Koordinaten mit f als Zeit, Tangentengleichung mit analytischer Hesse-Matrix,
  Benettin mit Renormierung je Umlauf, 1000 Umlaeufe, 400 Schritte je Umlauf.
- mu in {0,001; 0,01; 0,02; 0,03}, e in {0; 0,05; 0,1; 0,2}; 8 Anfangswerte je Paar (Auslenkung 0,005 und 0,02,
  4 Richtungen, Geschwindigkeit null). Entkommen wird gemeldet, nicht gemittelt. Einheit: je Bogenmass f.

### D2 (Phasenmodell)

- A, B: theta = t. Mit phi = theta_C - t: phi' = Delta - 2K sin phi + F sin((Omega - 1) t + psi - phi).
- D2a: F = 0, K in {0,5; 1}, |Delta| - 2K = 10^(-4 ... 0), 21 Werte je K; RK4 dt = 0,01 bis t = 20000 bzw. bis
  mindestens 20 Phasenspruenge; Rastdauer = Zeit zwischen Spruengen (Mittel), Vergleich mit 2 pi/sqrt(Delta^2 - 4K^2)
  (Kontrolle 1 %), Steigung im log-log nahe der Grenze.
- D2b: K = 0,5, Delta = 1,1 (0,1 ausserhalb der Rastung). Karte (psi, F): psi 0 bis 2 pi (72), F 0 bis 0,5 (51),
  Omega = 1. Gerastet = kein Phasensprung in der Messzeit (Einschwingen 500, Messung 2000). Vergleich mit der
  Zeigerformel |2K + F e^{i psi}| > |Delta| (Anteil uebereinstimmender Punkte ausserhalb eines Randstreifens).
  Karte (Omega, F): Omega 0 bis 2 (101), F 0 bis 0,5 (51), psi = 0; Klassen: rastet an A/B (mittlere Frequenz von C
  = 1), rastet am Takt (= Omega), sonst.
- D2c (explorativ): omega_A = 0,8, omega_B = 1,2, omega_C = 1,1, K = 0,15; Karte Omega 0,5 bis 1,5 (101), F 0 bis 0,5
  (51); gemessen mittlere Frequenz von C und Lyapunov-Exponent der C-Phase (negativ = C ist eingefangen).

### D3 (Kuramoto-Sakaguchi mit Takt)

- Mitlaufendes Bild phi_i = theta_i - Omega t: phi_i' = omega_i - Omega + (K/N) sum_j sin(phi_j - phi_i - alpha)
  - F sin phi_i. Die Summe enthaelt j = i (konstante Verschiebung -K sin(alpha)/N), wie in der Karte geschrieben.
- Faelle: N = 2 mit Takt, N = 3 ohne, N = 3 mit, N = 4 ohne. Je 2000 Zufallspunkte (feste Seeds):
  K ~ U[0;4], alpha ~ U[0;1,5], F ~ U[0;2] (ohne Takt F = 0), Streuung s ~ U[0;2] mit omega_i = s u_i, u_i ~ U[-1/2;1/2];
  Omega = mittlere Frequenz + d, d ~ U[-2;2].
- RK4 dt = 0,02, Einschwingen 500, Messung 2000; Tangente v' = J v (Mittelfeldform, O(N)), Renormierung jede
  Zeiteinheit; Anfangsphasen gleichverteilt, Tangente zufaellig.
- Nachrechnen aller Punkte mit lambda_max > 0,01 (bei mehr als 300 Treffern die 300 groessten; Anzahl wird gemeldet):
  dt/2, doppelte Messzeit, andere Anfangsbedingung. Robust = alle drei > 0,01.
- Kontrolle des Codes: N = 2 mit Takt und N = 3 ohne Takt nirgends lambda_max > 0,005 (Theorie: 2-Torus).

## Laufliste (Spuren cpu3 und cpu4, je Aufruf <= 10 min, Schaetzung)

| Nr | Spur | Skript | Inhalt | Schaetzung |
|---|---|---|---|---|
| 1 | cpu3 | d1a_floquet.py A | Gitter A n = 2000/4000, Bisektion, Kontrollen | 1 min |
| 2 | cpu4 | d1a_floquet.py B | Gitter B n = 2000/4000 | 3 min |
| 3 | cpu3 | d3_kuramoto.py stichprobe N=4 ohne, N=2 mit | 2000 Punkte je Fall | 5 min |
| 4 | cpu4 | d3_kuramoto.py stichprobe N=3 ohne, N=3 mit | 2000 Punkte je Fall | 5 min |
| 5 | cpu3/4 | d3_kuramoto.py nachrechnen | Treffer, drei Varianten | je 2 min |
| 6 | cpu3 | d1d_takt.py | Gitter, zwei Schrittzahlen (bei Bedarf je mu aufgeteilt) | 3 min |
| 7 | cpu4 | d2_phasen.py | D2a, D2b, D2c | 3 min |
| 8 | cpu3 | d1b_lebensdauer.py haupt | 1920 Teilchen | 4 min |
| 9 | cpu4 | d1b_lebensdauer.py halb | 96 Teilchen dt/2 | 4 min |
| 10 | cpu3/4 | d1c_lyap.py | 128 Bahnen (nur wenn Zeit) | 4 min |
| 11 | cpu3 | plots.py | Abbildungen PNG | 1 min |

Laufzeiten, die die Schaetzung um mehr als das Doppelte ueberschreiten wuerden, werden auf mehrere Aufrufe verteilt
(Nachtrag vor dem Lauf).

## Auswertung gegen Vorhersagen (Kartentabelle, unveraendert)

- K: D1-Kontrollen bei e = 0 auf 1e-4 (mu_R, Zungenspitze, Eigenwerte), Jacobi < 1e-9; D2a Adler auf 1 %.
- D1a-1: Gibt es Punkte mit mu < mu_R, die bei e = 0 stabil und bei e > 0 instabil sind (Zunge ab 0,0286)?
- D1a-2: Gibt es stabile Punkte mit mu > mu_R bei e > 0 (auf beiden Gittern und beiden Schrittzahlen)?
- D1d-1: Liegen die Zungen bei 2 s_k/n und Kombinationen? Ist Omega nahe s_k bzw. 2 s_k instabil?
- D1d-2: Falls Stabilisierung oberhalb mu_R: bei welchem Omega (schnell, Omega > 3, oder nahe den Eigenfrequenzen)?
- D1b-1/D1b-2: Lebensdauer endlich und Exponent nahe -1/2, oder Teilchen knapp oberhalb mu_R 1000 Umlaeufe gefangen.
- D1c: Mittlere endliche Lyapunov-Zahl bei e > 0 groesser als bei e = 0 (je mu).
- D2a: Steigung nahe -1/2 und Adler auf 1 %. D2b: psi = 0 rastet ein, psi = pi rastet aus.
- D3-1/2/3: wie in der Karte, mit der Robust-Definition oben.

## Antwortklassen (Karte) und Zuordnung

- H1: gestuetzt, wenn in mindestens einem Modell eine endliche, zur Grenze hin wachsende Lebensdauer mit bestandenen
  Kontrollen gemessen ist (D2a, D1b).
- H2: gestuetzt, wenn ein Takt bei der Eigenfrequenz instabile Zustaende stabil macht, besser als andere Takte;
  teilweise, wenn nur in Phase, nur gedaempft oder nur bei schnellem Takt.
- H3: gestuetzt, wenn im Dreiersystem mit Takt robuste lambda_max > 0,01 auftreten und ohne Takt nicht; der Zusatz
  ("drei besonders?") wird mit N = 2 mit Takt und N = 4 ohne Takt beantwortet.
- offen: Kontrolle verfehlt, Numerik nicht aufgeloest oder Zeit aus.

## Ablage

- Code: code/, Ausgaben: aus/, Abbildungen: abb/, Hilfsdateien: hilfs/. Remote: /home/fmh/fmhc-physics-remote/runde16-drei-takt/.

## Ergaenzungen vor dem Einfrieren (nach den lokalen Rauchtests, nur Methodik)

- Rauchtests lokal 08:45 bis 08:47 (date): D1a winzig (Bisektion e = 0: 0,0385217 bei Intervall 2,4e-6, mu_R 0,0385209;
  Multiplikatoren bei e = 0 auf 3e-9), D3 mit P = 200 und kurzer Zeit, D1d/D2/D1b/D1c in Kleinstform. Keine
  Auswertung der Hypothesen daraus.
- D1c: Abbruch nicht bei Abstand 0,5 zu L4 (bei kleinem mu verlassen grosse Kaulquappen- und Hufeisenbahnen diese
  Kugel, ohne zu entkommen), sondern bei r1 < 0,05, r2 < 0,05 oder Abstand zum Ursprung > 3. Groesste Auslenkung wird
  gemeldet.
- D3-Kontrollfaelle (N = 2 mit Takt, N = 3 ohne Takt): Nachrechnen aller Punkte mit lambda_max > 0,005 (Schwelle der
  Vorhersage D3-1), robust = alle drei Varianten > 0,005. Faelle N = 3 mit Takt und N = 4 ohne: Schwelle 0,01.
- Hinweis zur Endlichkeit: regulaere (quasiperiodische) Bahnen mit Scherung geben endliche Werte bis etwa
  ln(T)/T ~ 0,004 bei T = 2000; deshalb das Nachrechnen mit doppelter Zeit.
- Uhr der .69 zeigt UTC; Zeiten in diesem Ordner sind CEST (Laptop, date).
