# SCHACHBRETT-KAUSAL-1: Plan (Code-Agent fuer die Leitung, Runde 38, explorativ nach v3)

- Start des Code-Agenten 06:19:19 CEST (date). Plantext ab 06:47:17 CEST (date).
- Vor dem Plantext (Abschnitt 8, offengelegt):
  - ein Literaturabruf (Johnstons Doktorarbeit, PDF lokal gelesen)
  - Code geschrieben
  - Rauch nur fuer Schachbrett, Kontinuum, Codeprobe und Laufzeiten; dazu eine Pfadprobe der Auswertung mit umgeleiteter
    Ausgabe
  - **Das SK0-Ergebnis habe ich im Rauch gesehen** (erlaubt, Abschnitt 8). Pruefpunkte und Fehlermass von SK0 standen
    vorher im Code fest und sind unveraendert.
  - Werte der Bauweise auf der Kausalmenge habe ich nicht angesehen.
- Karte: KARTE.md. Vorhersagen SK0 bis SK3 und ihre Schwellen sind unveraendert uebernommen (Abschnitt 5).
- Code (code/):
  - schachbrett.py: regelmaessiges Schachbrett, SK0
  - kausal_dirac.py: Hauptbauweise, Pakete, Punktquelle, Codeprobe
  - kontinuum_dirac.py: Kontinuum der Pakete, Gegenprobe per direkter Faltung
  - auswertung.py: Urteile, Bilder, auswertung.json
  - kausal_welle.py: unveraendert aus KAUSAL-WELLE-1 (sha256 2f897e12..., eingefrorene Fassung dort)
- **Kennzeichen:**
  - [S] an der Quelle gelesen; [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [F] Festlegung dieses Plans (von der Karte offengelassen); [E] im Rauch gesehen

## 1. Quellen und Formeln

### 1.1 Literatur

- **Gelesen [S]:** S. P. Johnston, "Quantum Fields on Causal Sets", Doktorarbeit, Imperial College London, Sept. 2010,
  arXiv:1010.5514v1 (Kopf: 26 Oct 2010).
  - Die Nummer stimmt. Ein Abruf (PDF); gelesen: Inhaltsverzeichnis, Kapitel 6 (S. 142 bis 152).
- **Kap. 6.3.1 "The checkerboard on a causal set":**
  - Wortlaut: "the most naïve choice for the straight parts of the causal set trajectories would be links" (S. 145).
  - Das Problem dort: Aus Links allein ist die Zahl der Ecken nicht ablesbar.
  - Johnston nimmt "chain intervals" als gerade Stuecke, das sind total geordnete Intervalle. Ecken R = kleinste Zahl
    solcher Intervalle minus 1.
  - Johnston: "we should not think of the corners as being assigned to a particular element" (S. 147).
- **Kap. 6.3.2:**
  - Amplitude a^(n+1) b^n fuer n Ecken; a = A sqrt(rho), b = B m/rho (6.7) mit offenen Konstanten A, B
  - K_++ = K_-- = Summe ueber gerade n (6.11), K_+- = K_-+ = Summe ueber ungerade n (6.12)
  - Wortlaut: "Calculating these matrices explicitly is difficult"; "it is possible that we could choose the A and B
    constants to give a good model for the Dirac propagator" (S. 149).
- **Kap. 6.4 "Square root of the propagator":**
  - R_m R_(-m) = -rho K_R (x) I (6.19); Massenreihe R_m = R_0 (I - b R_0)^(-1) mit b = +-m/rho (6.22) bis (6.24)
  - Wortlaut: "This remains a task for future work." (S. 151)
- **Folgerung:**
  - Es gibt einen veroeffentlichten Ansatz fuer ein Schachbrett auf Kausalmengen (Johnston 2010), aber keine fertige
    Bauweise: A und B sind offen, und die Matrizen T^(n) sind nicht berechnet.
  - Dazu [M]: (6.11) setzt K_++ = K_-- fuer jedes Elementpaar. Im Kontinuum gilt fuer die glatten Teile
    S_RR/S_LL = e^(2 zeta) (Abschnitt 1.2). Der Ansatz kann R und L abseits der Ruhe-Achse also nicht trennen.
  - Ich uebernehme ihn deshalb nicht als Hauptbauweise.
  - Spaetere Arbeiten kann ich ohne Suche nicht ausschliessen [L?].
- **Weitere Quellen:**
  - Johnston, arXiv:0806.3083 [S, in KAUSAL-WELLE-1 an der Quelle gelesen]: (3.5) K = I + Phi (I - b Phi)^-1; (3.23) K_m =
    (1/2) J0(m tau); (3.31) a = 1/2, b = -m^2/rho in 1+1.
  - Feynman/Hibbs 1965, S. 35 bis 36, Amplitude (i m eps)^R; Jacobson/Schulman 1984 als ausgerechnete Loesung.
    [S nur als Zitat in Johnstons Arbeit, S. 144 bis 145; die Originale nicht gelesen.]

### 1.2 Kontinuum [M]

- **Gleichungen:**
  - U = t - x, V = t + x (ohne sqrt2), tau = sqrt(U V), zeta = Rapiditaet des Pruefpunkts; Komponenten (R, L).
  - (d_t + d_x) psi_R = -i m psi_L + j_R und (d_t - d_x) psi_L = -i m psi_R + j_L, also 2 d_V psi_R = ..., 2 d_U psi_L = ...
  - Das ist i d_t psi = (alpha p + beta m) psi mit alpha = diag(1, -1), beta = [[0, 1], [1, 0]].
  - Erhaltene Norm: d_t (|psi_R|^2 + |psi_L|^2) + d_x (|psi_R|^2 - |psi_L|^2) = 0. Die Massenterme heben sich weg.
- **Faktorisierung:** D = d_t + alpha d_x + i m beta und D'' = d_t - alpha d_x - i m beta erfuellen D D'' = Box + m^2.
  - Also ist S = D'' G mit G = (1/2) J0(m tau) theta [S: Johnston (3.23)] der retardierte Dirac-Propagator.
  - S_RR = 2 d_U G, S_LL = 2 d_V G, S_RL = S_LR = -i m G.
- **Komponentenweise (R-Quelle am Ursprung, im Kegel):**
  - S_RR = delta(t - x) theta(t) - (m/2) sqrt(V/U) J1(m tau)
  - S_LR = -(i m/2) J0(m tau)
  - S_LL und S_RL entsprechend mit U <-> V, also x -> -x.
- **Gegenprobe als Pfadsumme:**
  - Erste Ordnung: S_LR = -(i m/2) theta theta. Zweite: S_RR = -(m^2/4) V. Dritte: S_LR = +(i m^3/8) U V. Alle stimmen mit
    den Reihen von J0 und J1.
  - Masselos bleibt nur delta(t - x): Normierung und Vorzeichen sind also festgelegt.
- **Daraus fuer die Glieder:** sqrt(V/U) = e^zeta, also S_RR glatt = -(m/2) e^zeta J1(m tau).

### 1.3 Regelmaessiges Schachbrett [M]

- **Gitter:** U = 2 eps i, V = 2 eps j (Zeit- und Ortsschritt eps).
  - Rekursion: psi_R(i, j+1) = psi_R(i, j) - i m eps psi_L(i, j) und psi_L(i+1, j) = psi_L(i, j) - i m eps psi_R(i, j).
  - Je Richtungswechsel also -i m eps, wie Feynman (i m eps), Vorzeichen nach unserer Konvention.
  - Start psi_R(0, 0) = 1. Die Kontinuumsdichte ist psi/(2 eps).
- **Geschlossen (Pfadzaehlung):**
  - psi_L(i, j) = -i m eps Summe_k C(j, k) C(i-1, k) (-m^2 eps^2)^k
  - psi_R(i, j) = Summe_(k>=1) C(j, k) C(i-1, k-1) (-m^2 eps^2)^k
  - Fuer eps -> 0 folgen die Reihen von J0 und J1 aus 1.2.
- **Fehler (Schreibtisch):**
  - Der Schrittoperator hat Determinante 1 + m^2 eps^2. Seine Eigenwerte haben den Betrag sqrt(1 + m^2 eps^2).
  - Die Amplitude waechst deshalb wie e^(m^2 eps t/2). Fuehrender Fehler von S_LR: (m^2 eps/2) [t J0 + 2 x J1/(m tau)] mal
    (m/2), also erste Ordnung in eps und mit t wachsend.
- **Rechnung:** Zeilen in i, Kumulativsumme in j (numpy). Pruefpunkte bilinear in (i, j) interpoliert (Fehler O(eps^2)).

### 1.4 Hauptbauweise "Eckpaar-Kette" (Umgruppierung des Schachbretts) [M]

- **Identitaet:**
  - Eine Zickzack-Bahn, die als L-Laeufer ankommt, ist eindeutig durch die Folge ihrer L->R-Ecken c_1, ..., c_k gegeben.
  - Diese bilden eine Kette c_1 < ... < c_k in der Kausalordnung.
  - Die R->L-Ecken liegen an den Rechteckecken (U_(c_(i-1)), V_(c_i)), am Schnitt des R-Strahls des einen mit dem L-Strahl
    des naechsten Glieds.
  - Jedes Eckpaar traegt (-i m/2)^2 dU dV = -(m^2/2) dt dx.
  - Fuer R-Ankunft gilt dasselbe mit den R->L-Ecken.
- **Auf der Kausalmenge** sind die Eckpaare die Elemente, mit Gewicht 1/rho:
  - psi_L(x) = s_L(x) - (m^2/(2 rho)) Summe_(y < x) psi_L(y)   (Elemente = L->R-Ecken)
  - psi_R(x) = s_R(x) - (m^2/(2 rho)) Summe_(y < x) psi_R(y)   (Elemente = R->L-Ecken)
  - s_a sind die Bahnen ohne Element-Ecke, analytisch aus der glatten Quelle:
    - s_R(x) = (1/2) Integral_(V' < V_x) j_R(U_x, V') dV' - (i m/2) Integral ueber J-(x) von j_L dt dx
    - s_L(x) = (1/2) Integral_(U' < U_x) j_L(U', V_x) dU' - (i m/2) Integral ueber J-(x) von j_R dt dx
  - Der erste Teil ist der gerade Lauf laengs des eigenen Lichtstrahls, der zweite eine Ecke an einer Rechteckecke.
- **Das ist Johnstons Rekursion:**
  - Stop-Amplitude -m^2/(2 rho) je Element wie (3.31), mit Quelle s_a.
  - Rechnung mit der CDQ-Rekursion aus KAUSAL-WELLE-1 (unveraendert): O(N log^2 N) statt Fenwick, Ergebnis gleich.
- **Zuschauer** (Punkt x ausserhalb der Menge, Palm): psi_a(x) = s_a(x) - (m^2/(2 rho)) Summe_(y < x) psi_a(y).
- **Punktquelle j_R = delta am Ursprung:**
  - s_L = -i m/2 im ganzen Zukunftskegel, also psi_L = S_LR = -i m K_Johnston.
  - S_RR braucht einen Lichtstrahl am Ende. Diesen Lauf rechne ich analytisch: S_RR glatt = (-i m/2) Integral_0^(V_x)
    psi_L(U_x, V') dV' = -(m^2/4) V_x + (i m^3/(4 rho)) Summe_(y < x) psi_L(y) (V_x - V_y).
  - Der delta-Teil auf dem Lichtstrahl selbst ist auf der Kausalmenge nicht darstellbar (dort liegen keine Elemente). Die
    Pruefpunkte liegen deshalb strikt im Kegel.
- **Was intrinsisch ist:**
  - Intrinsisch: die Rekursion (nur die Kausalordnung).
  - **Halb-intrinsisch:** die Lichtrichtungen. Sie kommen aus der Einbettung, ueber U, V an der Quelle (s_a) und am
    Zuschauer (Gewicht V_x - V_y).
  - Links werden nicht benutzt.
- **Erwartungswert [M]:**
  - Die Kettenentwicklung psi_a = Summe_k (-m^2/(2 rho))^k Summe ueber k-Ketten von s_a hat bei Poisson-Streuung den
    Erwartungswert Summe_k (-m^2/2)^k Integral ueber k-Ketten = Kontinuum.
  - Das ist dasselbe Argument wie Johnston (3.8) bis (3.10), mit Palm-Lesart fuer Elemente.
  - **Vorab ableitbar:** E[psi] = Kontinuum folgt also aus der Konstruktion.
  - SK1 prueft hier Umgruppierung, Herleitung und Code, keine offene Physikfrage. Neu und nicht ableitbar sind die
    Streuung (SK2), die Stabilitaet (SK3) und das Verhalten der Komponenten bei endlicher Dichte.
- **Verwandtschaft:** Johnston 6.4 (Dirac aus dem Klein-Gordon-Propagator). Hier geschieht das ohne Matrixwurzel, ueber
  S = D'' G und die Ecken-Umgruppierung.

### 1.5 Warum nicht Links (Schreibtisch, zweite Bauweise nicht gerechnet) [M/H]

- **Linkdichte:**
  - Laengs eines Lichtstrahls liegen je Einheit Delta v im Mittel 1/Delta v Links.
  - Die Schrittlaengen eines Link-Zickzacks sind also logarithmisch gleichverteilt, ohne Skala, die mit rho schrumpft.
- **Folgen [H]:**
  - Eine Riemann-Summe ueber solche Schritte, (-i m/2) Delta v psi_L(y) je Link, hat eine Verzerrung durch die grossen
    Schritte. Sie faellt nicht mit rho.
  - Das Rauschen je Strahlintegral ist O(1), da es nur ~ ln 2 Links je Oktave gibt.
  - Erwartung fuer ein reines Link-Schachbrett: im Mittel verzerrt, Streuung ohne Fall mit rho.
- **Beschreibende zweite Bauweise: nicht gerechnet.** Gruende:
  - Zeitbox
  - Die Linksuche je Element und die Gewichtswahl sind offen (Johnston 6.3.2 laesst A, B offen).

## 2. Gebiet, Quellen, Dichten, Saaten

- **Pakete [F]:** j_a = c_a exp(-(t^2 + x^2)/(2 sigma^2)) exp(-i(omega t - p x)), m = 1.
  - **"zitter":** sigma = 1, omega = 0, p = 0, (c_R, c_L) = (1, 0).
    - Kurze Quelle mit reiner R-Chiralitaet. Ihr Spektrum reicht an +-m, also mischen positive und negative Energie.
    - Es soll Zitterbewegung (Kreisfrequenz ~2m) im Anteil |psi_R|^2 geben.
  - **"bewegt":** sigma = 4, eta = 1 (omega = cosh 1, p = sinh 1), positiver Spinor (c_R, c_L) ~ (e^(1/2), e^(-1/2)),
    normiert.
- **Analytik:** Die Gauss-Huelle trennt in U und V. Strahl- und Flaechenintegrale in s_a sind damit Produkte von
  I(Y; W) = Integral_(-inf)^Y exp(-y^2/(4 sigma^2) - i W y) dy (Faddeeva, Formel aus KAUSAL-WELLE-1).
- **Gebiet Pakete [F]:** D = J+(Scheibe r0 = 18) geschnitten {t <= 32}, wie KAUSAL-WELLE-1.
  - N ~ 0,65 Mio. (rho = 200) bzw. 2,6 Mio. (rho = 800).
  - Elemente ausserhalb von J+(Scheibe) fehlen. Ihr Beitrag kommt nur aus den Gauss-Auslaeufern jenseits 4,5 sigma
    (~e^(-10)) [M].
- **Gebiet Punktquelle:** Zukunftskegel des Ursprungs mit t <= 25. N ~ 0,13 Mio. bzw. 0,5 Mio. Jeder Pruefpunkt hat dort
  seine volle Vergangenheit.
- **Dichten (Karte):** rho in {200; 800} je Flaecheneinheit.
- **Saaten [F]:** 1 bis 16 je rho.
  - Pakete: SeedSequence([20261004, 38, 81, rho, s]); Punktquelle: [20261004, 38, 82, rho, s]; Codeprobe: [.., 83, ..].
  - Rauchsaaten 91 und 92 gehen nicht in Urteile ein.

## 3. Messung

- **Pruefpunkte [F]:**
  - **Propagator:** tau in {0,5; 1; 2; 3; 5; 8; 12; 16} (wie KAUSAL-WELLE-1), zeta in {-1; -0,5; 0; 0,5; 1}.
    Komponenten S_RR (glatt) und S_LR; 80 Tests.
    - Die L-Quelle ist das Spiegelbild x -> -x und durch zeta < 0 mit abgedeckt.
  - **Pakete:** t in {ta; ta + 10; ta + 20}, ta = 3 sigma, x = tanh(eta) t; Komponenten R und L. 12 Tests.
  - Zusammen 92 Tests je Dichte. Dazu je Paket 21 Profilpunkte bei ta + 20 (nur Bild).
- **Scheiben [F]:**
  - Breite w = 0,5; 40 Scheiben von ta bis ta + 20 (Laufstrecke 20/m).
  - Klassen der Breite 1 in d = x - tanh(eta) t.
- **Fenster [F]:** abs(d) < W, W = ceil(4 max_k sigma_x,c), nur aus dem Kontinuum (wie KAUSAL-WELLE-1).
- **Norm:**
  - n_k = Summe (|psi_R|^2 + |psi_L|^2)/(rho w) ueber die Elemente der Scheibe im Fenster.
  - Kontinuum: gleiche Scheiben und gleiches Fenster auf feinem Gitter (dt = 0,05, dx = 0,1).
- **Komponentenanteil (beschreibend):** f_k = Summe |psi_R|^2 / Summe (|psi_R|^2 + |psi_L|^2) im Fenster.
- **Statistik:** Saatmittel; komplexe SE = sqrt(var Re + var Im)/sqrt(n), ddof = 1.
  - Relative Streuung r = sqrt(var Re + var Im)/abs(Kontinuum).

## 4. Kontrollen (ohne Urteilskraft)

- **Codeprobe** (rho = 5, N ~ 2000):
  - CDQ-Rekursion gegen dichte Loesung (I + a A) psi = s
  - Zuschauersummen (auch die V-gewichtete) gegen Maskensumme
  - analytische s_a gegen direkte Gauss-Legendre-Quadratur an 5 Punkten
- **Schachbrett:** Rekursion gegen die geschlossene Binomialsumme (eps = 0,05, 6 Knoten).
- **Kontinuum Pakete:**
  - k-Raum (exakt je Mode) gegen direkte Faltung mit dem analytischen Dirac-Propagator aus 1.2 (delta-Teil als
    Strahlintegral, glatte Teile 2D-Gauss-Legendre) an den 6 Pruefpunkten
  - Normanteil am Klassenrand
- **Beschreibend:** normiertes Schachbrett (Faktor (1 + m^2 eps^2)^(-t/(2 eps))), trennt den Normzuwachs vom Rest des Fehlers.

## 5. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| SK0 | Kontrolle: Das regelmaessige Schachbrett trifft den Kontinuums-Dirac-Propagator an den Pruefpunkten auf <= 1e-2 bei Schritt 0,01, Fehler etwa proportional zum Schritt (Steigung 1 +- 0,2) | 85 % |
| SK1 | [H] Kausalmenge: Das Saatmittel der Zwei-Komponenten-Pfadsumme trifft die Kontinuumsloesung an mindestens 90 % der Pruefpunkte innerhalb 3 Standardfehlern (rho = 800) | 35 % |
| SK2 | [H] Die relative Streuung faellt mit rho (Steigung -0,5 +- 0,15 zwischen 200 und 800) | 45 % |
| SK3 | Stabil: Die Norm waechst ueber die Laufstrecke um hoechstens den Faktor 1,5 gegenueber dem Kontinuum | 50 % |

- Alle Urteile rechnet code/auswertung.py mechanisch.
- "Nicht auswertbar", wenn fuer eine Dichte weniger als 16 Saaten (Pakete oder Punktquelle) vorliegen.
- **SK0 [F]:**
  - E(eps) = max ueber die 80 Pruefwerte (40 Punkte x {S_RR glatt, S_LR}) von abs(S_eps - S), absolut. Der Propagator ist
    von der Groesse m/2; "auf <= 1e-2" lese ich als absolute Abweichung.
  - Schritte eps in {0,02; 0,01; 0,005; 0,0025}; Steigung = Ausgleichsgerade log E gegen log eps.
  - Eingetroffen, wenn E(0,01) <= 1e-2 und die Steigung in [0,8; 1,2] liegt.
- **SK1 [F]:** bei rho = 800 alle 92 Tests: abs(Saatmittel - Kontinuum) <= 3 SE (komplex). Eingetroffen, wenn der Anteil
  >= 90 % ist (mindestens 83 von 92).
- **SK2 [F]:**
  - Steigung = Mittel ueber die 92 Pruefgroessen von [ln r(800) - ln r(200)] / ln 4. Das ist gleich der Steigung der
    geometrischen Mittel.
  - Eingetroffen, wenn sie in [-0,65; -0,35] liegt.
- **SK3 [F]:**
  - R_k = Saatmittel(n_k)/n_c,k; G = Mittel(R der letzten 4 Scheiben)/Mittel(R der ersten 4 Scheiben).
  - Eingetroffen, wenn G <= 1,5 fuer beide Pakete und beide Dichten (4 Faelle).
  - Beschreibend daneben max_k R_k.

### 5.1 Eigene Erwartung (Schreibtisch, keine Urteilsregel)

- **SK0:** nicht eingetroffen, durch den Rauch bereits bekannt (Abschnitt 8): E(0,01) = 0,0295, Steigung ~1,04.
  - Ursache nach 1.3 [M]: Der Fehler waechst mit t; die Pruefpunkte reichen bis t = 24,7.
- **SK1 eingetroffen (90 %):** unverzerrt nach Konstruktion (1.4). Risiko: schwere Raender der Verteilung bei 16 Saaten.
- **SK2 eingetroffen (75 %):** Monte-Carlo-Rauschen ~ rho^(-1/2) wie in KAUSAL-WELLE-1 (dort -0,52).
  - Risiko: Der V-gewichtete Zuschauer (S_RR) mittelt ueber lange Strahlen. Dort koennte ein anderer Exponent auftreten.
- **SK3 eingetroffen (90 %):** R - 1 ist Rauschleistung (KAUSAL-WELLE-1: G <= 1,11 bei rho = 50).
- **Komponentenwechsel:** Das Saatmittel folgt der Kontinuumskurve. Das "zitter"-Paket schwingt mit Kreisfrequenz nahe 2m
  und gedaempft, weil das Paket zerfliesst.

## 6. Hinweise zur Karte (vor dem Einfrieren offengelegt)

1. **SK0, Schwelle gegen Pruefbereich (Kartenluecke, keine Berichtigung):**
   - Die Karte legt 1e-2 bei eps = 0,01 fest, aber keinen Pruefbereich.
   - Feynmans ungenormtes Schachbrett waechst je Zeiteinheit um den Faktor e^(m^2 eps/2) (1.3). Der Fehler ist deshalb
     etwa (m^2 eps/2) t abs(S).
   - Bei eps = 0,01 haelt die Schwelle nur bis t ~ 1 bis 2/m.
   - Mit den von KAUSAL-WELLE-1 geerbten Pruefpunkten (tau bis 16) verfehlt das Schachbrett sie, und das ist schon aus dem
     Rauch bekannt.
   - Schwelle und Pruefpunkte bleiben, wie sie vor dem Rauch im Code standen. **Urteil nach Kartenwortlaut** = Urteil
     nach Plan (Abschnitt 5).
   - Beschreibend: Fehler je tau und das normierte Schachbrett.
2. **SK1, Wahrscheinlichkeit der Karte:** Die Karte (35 %) dachte an eine naheliegende Link-Bauweise. Fuer die
   Eckpaar-Kette ist SK1 im Mittel vorab ableitbar (1.4). Das steht so im Ergebnis.
3. **Offen gelassen und festgelegt [F]:**
   - Bauweise (1.4), Pakete, Gebiet, Pruefpunkte, Fehlermass SK0
   - komplexe SE, Buendelung der Streuung (SK2), Lesart des Wachstumsfaktors (SK3), Fenster
4. **Strategie Weg 3** fragt "ueber die Links einer Kausalmenge". Die Hauptbauweise benutzt keine Links, sondern alle
   Relationen (Ketten). Warum Links allein schwierig sind, steht als Schreibtisch in 1.5 (nicht gerechnet).
5. **Hinweis "Fenwick-Rekursion O(N log N)":** Benutzt ist die CDQ-Rekursion O(N log^2 N) aus KAUSAL-WELLE-1. Sie liefert
   dieselbe Summe und ist dort gegen die dichte Loesung geprueft.

## 7. Laeufe

- Nur .69 ueber kleintest.sh, Spuren cpu7 und p4000a, hoechstens zwei zugleich, je Lauf < 10 min.
- Zeitgrenze im Skript 540 s: Abbruch vor einer Saat, Rest mit denselben Saatnummern nachholen.
- **Reihenfolge nach dem Einfrieren** (Ordner lauf/):
  - cpu7: schachbrett.py, kontinuum_dirac.py, probe, punkt 200 (1 bis 16), punkt 800 (1 bis 16), paket 200 (1 bis 16),
    paket 800 (1 bis 8)
  - p4000a: paket 800 (9 bis 16)
  - danach auswertung.py lauf kont sb aw 200,800 16

## 8. Rauch (vor dem Einfrieren, Ordner rauch-69/)

- **Gesehen [E]** (04:43:56 bis 04:45:13 UTC), alle rc = 0:
  - **Schachbrett:** E_max = 0,0620 / 0,0295 / 0,0144 / 0,0071 bei eps = 0,02 / 0,01 / 0,005 / 0,0025, also Steigung ~1,04.
    - Binomialprobe 1,3e-15.
    - **SK0 nach den Regeln aus Abschnitt 5 damit: nicht eingetroffen.** Pruefpunkte und Fehlermass standen vorher im Code
      (schachbrett.py, 06:41 CEST geschrieben, Rauch 06:43:56 CEST) und sind unveraendert.
  - **Codeprobe** (rho = 5, N = 1982): Rekursion gegen dichte Loesung 2,5e-15, Zuschauer 3,0e-15, analytische Quellen gegen
    Quadratur <= 3,6e-13.
  - **Kontinuum:** k-Raum gegen direkte Faltung mit dem analytischen Dirac-Propagator <= 4e-15 ("zitter") bzw. <= 2,9e-13
    ("bewegt") an allen 6 Pruefpunkten.
    - Damit sind S = D'' G, die delta-Teile, die J1-Normierung und die Fourier-Konventionen zweifach bestaetigt.
    - Normanteil am Klassenrand <= 4e-31.
  - **Laufzeit:** Pakete rho = 200: N = 646 298, Loesen 5,1 s. Punktquelle rho = 800: N = 499 946, 2,1 s.
- **Pfadprobe** (04:46:18 bis ~04:47:30 UTC):
  - Laeufe punkt 200/800 und paket 200/800, Saaten 91 und 92, alle endlich, rc = 0
  - paket 800: N = 2 584 352, 28,5 s je Saat
  - Angesehen habe ich nur die Infozeilen (N, endlich, Zeit), keine Feldwerte.
  - Die Pfadprobe von auswertung.py lief mit umgeleiteter Ausgabe (04:49 UTC, 2 Saaten je Dichte).
    - Geprueft habe ich nur: rc = 0, alle fuenf Bilder, Schluessel von auswertung.json (SK0 bis SK3), 0 Treffer fuer
      NaN/Infinity.
    - Keine Urteile, Werte oder Bilder der Kausalmenge angesehen.
- **Folge fuer den Plan:** keine. Keine Schwelle und keine Regel geaendert.

## 9. Einfrieren

- Kopie PLAN.md.eingefroren-JJJJMMTT-HHMMSS (Zeit per date), Code-Kopien mit derselben Endung, sha256 in
  code/pruefsummen-einfrieren.txt.
- Danach aendern sich Plan und Urteilsregeln nicht. Code nur bei echten Fehlern, offengelegt im ERGEBNIS.
