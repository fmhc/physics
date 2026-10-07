# KAUSAL-WELLE-1: Plan (Code-Agent fuer die Leitung, Runde 37, explorativ nach v3)

- Start des Code-Agenten 05:27:21 CEST (date). Plantext ab 05:50:26 CEST (date).
- Vor dem Plantext liefen nur technische Rauchlaeufe (Abschnitt 8): Codeprobe, Punktquelle, Kontinuum, Zeitmessung.
  Keine Saatmittel, keine Geschwindigkeiten und keine Normen der Kausalmenge angesehen.
- Karte: KARTE.md. Die Vorhersagen KW0 bis KW3 und ihre Schwellen sind unveraendert uebernommen (Abschnitt 6).
- Code:
  - code/kausal_welle.py: Streuung, Johnston-Rekursion, Messsummen, Pruefpunkte, Punktquelle, Codeprobe
  - code/kontinuum.py: Kontinuumsloesung, gleiche Messung, Quadratur-Gegenprobe
  - code/auswertung.py: Urteile, Bilder, auswertung.json
- Kennzeichen:
  - [S] an der Quelle gelesen; [L] Literatur aus dem Gedaechtnis, [L?] unsicher; [H] Hypothese
  - [M] eigene Mathematik; [F] Festlegung dieses Plans (von der Karte offengelassen); [E] im Rauch gesehen

## 1. Quelle und Formeln

- **Gelesen [S]:** S. Johnston, "Particle propagators on discrete spacetime", Class. Quantum Grav. 25 (2008) 202001,
  arXiv:0806.3083v2 (ein Abruf, PDF; Kopfzeile "Imperial/TP/08/SJ/1", 1 Oct 2008).
  - (2.1): (A_C)_ij = 1, wenn v_i vor v_j liegt, sonst 0 (Kausalmatrix; bei natuerlicher Nummerierung oberes Dreieck).
  - (3.1): Phi = a A_C (Summe ueber Ketten). (3.3): K = I + Phi + b Phi^2 + b^2 Phi^3 + ...; (3.5): K = I + Phi (I - b Phi)^-1.
    - a ist die Amplitude je Sprung ("hop"), b je Halt ("stop"); eine Kette der Laenge n traegt a^n b^(n-1) (S. 4).
    - Der Summand I ist "just convention" (S. 5).
  - (3.17), (3.18): (Box + m^2) K = delta, Box = d_0^2 - d_1^2.
  - (3.23): in 1+1 ist K_m(x - y) = (1/2) J0(m tau_xy) im Kegel, sonst 0.
  - (3.31): in 1+1 gilt **a = 1/2, b = -m^2/rho**. Die Masse geht also mit negativem b ein (alternierende Reihe -> J0).
  - (3.8) bis (3.10): Erwartungswert ueber Streuungen; Abschnitt 3.3 (S. 10): fuer 1+1 und m^2 << rho "preliminary results
    suggest the fluctuations decrease as the density increases". (4.13) und Text: K(x, y) haengt nur von Phi im Intervall
    [x, y] ab.
- **Daraus [M]:** K - I = (1/2) A_C (I + (m^2/(2 rho)) A_C)^-1, also die Kartenformel (Faktoren und Vorzeichen stimmen).
  - Feld (ohne den Konventionsterm I): phi(x) = (1/rho) Summe_{y vor x} (K - I)(y, x) J(y) = (1/(2 rho)) (C psi)(x).
  - Dabei (C f)(x) = Summe ueber y mit u_y < u_x und v_y < v_x, und psi = (I + a C)^-1 J mit a = m^2/(2 rho).
  - Vorwaertsrekursion in u-Ordnung: psi(x) = J(x) - a (C psi)(x); dann phi(x) = (C psi)(x)/(2 rho).
  - Erwartung [M, folgt aus (3.8)/(3.10) mit Palm-Lesart]: Fuer einen festen Punkt x (nicht in der Menge, "Zuschauer") ist
    E[phi(x)] = Integral (1/2) J0(m tau) J ueber den Vergangenheitskegel, also genau die Kontinuumsloesung.
- **Rechenweg [M]:** Punkte nach u sortiert; Teilen und Herrschen in u (Beitrag der linken an die rechte Haelfte als
  1D-Praefixsumme in v, mit numpy). Blaetter mit hoechstens 128 Punkten werden dicht geloest (Dreieckssystem).
  - Aufwand O(N log^2 N), statt eines Fenwick-Baums; das Ergebnis ist dasselbe.
  - Alle sechs Quellen laufen als Spalten auf derselben Streuung.

## 2. Gebiet, Quelle, Dichten, Saaten

- **Koordinaten:** u = (t - x)/sqrt2, v = (t + x)/sqrt2, dt dx = du dv, tau^2 = 2 du dv. m = 1.
- **Quelle (Karte):** J = exp(-(t^2 + x^2)/(2 sigma^2)) exp(-i(omega t - p x)), omega = cosh eta, p = sinh eta.
  - sigma in {2; 4; 8}, eta in {0; 1}: sechs Konfigurationen, alle um den Ursprung.
  - [F] Gekappt bei r = sqrt(t^2 + x^2) <= 4,5 sigma.
  - [F] Die Gauss-Huelle ist rund im Laborsystem ("Breite sigma in Raum und Zeit", Kartenwortlaut).
- **Gebiet [F]:** D = J+(Scheibe r0) geschnitten {t <= tb}, r0 = 4,5 * 8 = 36, tb = 3 * 8 + 20 = 44 (fuer alle sechs Quellen
  dasselbe).
  - In (u, v): u, v >= -r0, u + v <= sqrt2 tb, ohne die Ecke u, v < 0 mit u^2 + v^2 > r0^2. Flaeche 8727.
  - [M] D ist kausal konvex: Schnitt einer Zukunftsmenge mit einer Vergangenheitsmenge. Es enthaelt den Traeger jeder
    gekappten Quelle.
  - **Vollstaendige Vergangenheit:** Jeder Punkt von D hat seine ganze Vergangenheit im Quellgebiet (J- geschnitten
    Quelle) samt aller Ketten dazwischen in D. phi ist deshalb an jedem Punkt exakt dasselbe wie in einer unbegrenzten
    Streuung.
  - Es gibt keine Randpunkte mit unvollstaendiger Vergangenheit. Ein Streifen in x haette sie (Hinweis der Leitung) und
    waere kaum kleiner.
  - Fuer sigma = 2 und 4 ist der eigene Kegel J+(Scheibe 4,5 sigma) Teil von D. Ausserhalb davon ist das Feld dieser Quelle
    exakt null (keine Quelle in der Vergangenheit).
- **Dichten:** rho in {50; 200; 800} je Flaecheneinheit (N ~ 0,44 / 1,75 / 7,0 Millionen).
  - Faellt rho = 800 zeitlich aus (Abschnitt 8), nehme ich vor dem Einfrieren die groesste machbare Dichte.
- **Saaten [F]:**
  - Feld: Saaten 1 bis 16 je rho, SeedSequence([20261004, 37, 71, rho, s]).
  - Punktquelle: rho = 200, Saaten 1 bis 16, SeedSequence([20261004, 37, 72, rho, s]).
  - Codeprobe: rho = 5, Saat 1.
  - Rauchsaaten 91 und 92 gehen nicht in Urteile ein.

## 3. Messung

- **Zeitscheiben [F]:** Breite w = 0,5 (sigma/4 bis sigma/16). 40 Scheiben von ta = 3 sigma bis tb = 3 sigma + 20.
  - "Abklingen der Quelle" [F]: t = 3 sigma. Dort ist die Huelle auf e^(-4,5) = 1,1 % gefallen.
  - Die Laufstrecke ist damit genau 20/m, wie die Karte als Mindestmass verlangt.
- **Messsummen:** Je Punkt, Konfiguration und Scheibe werden |phi|^2, x|phi|^2, t|phi|^2 und x^2|phi|^2 gesammelt.
  - Klassen der Breite 1 in d = x - tanh(eta) t, von -140 bis 140. Die Klassen ueberdecken den ganzen Kegel.
- **Fenster ("Scheibe" der Hauptmessung) [F]:** abs(x - tanh(eta) t) < W mit W = ceil(4 * max_k sigma_x,c(t_k)).
  - sigma_x,c ist die |phi|^2-Standardabweichung des Kontinuumspakets in Scheibe k, ueber die ganze Scheibe.
  - W haengt nur vom Kontinuum ab, nicht von Daten der Kausalmenge.
  - Begruendung: Das Feld traegt Rauschen im ganzen Zukunftskegel der Quelle. Die ganze Scheibe (bis 190 breit) wuerde
    <x> ins Rauschen ziehen. Das Fenster entspricht dem "Streifen" der Leitung, ohne dessen Randpunkte.
  - Beschreibend daneben: die ganze Scheibe ohne Fenster.
- **Schwerpunkt:** <x>_k = Summe x|phi|^2 / Summe |phi|^2 und <t>_k ebenso, ueber die Punkte von Scheibe k im Fenster.
  - V = Steigung der gewoehnlichen Ausgleichsgeraden <x>_k gegen <t>_k ueber die 40 Scheiben.
- **Norm:** n_k = Summe |phi|^2 / (rho w), Schaetzer fuer Integral |phi|^2 dx in der Scheibe.
- **Kontinuum:** gleiche Scheiben, gleiche Klassen, gleiches Fenster, gleiche Formeln auf einem feinen Gitter.
  - Gitter dt = 0,05, dx = 0,1, Mittelpunktregel; ergibt V_c und n_c,k.
  - Loesung je Fourier-Mode exakt (Duhamel, Faddeeva-Funktion), fuer die ungekappte Quelle (Kopf von code/kontinuum.py).
  - [M] Schranke der Kappung: abs(Delta phi) <= pi sigma^2 e^(-10,125), bei sigma = 8 hoechstens 0,08 % von abs(phi).
  - Gegenprobe: direkte Gauss-Legendre-Faltung mit (1/2) J0(m tau) ueber die gekappte Quelle an den Pruefpunkten.
- **Pruefpunkte (KW0) [F]:** je Konfiguration t in {ta; ta + 10; tb}, x = tanh(eta) t, als Zuschauer ausgewertet. Dazu
  21 Profilpunkte bei tb (x = tanh(eta) tb + 2j, j = -10 bis 10, nur Bild).
- **Statistik:** Mittel ueber Saaten; SE = Standardabweichung (ddof = 1)/sqrt(n).
  - Komplex [F]: SE_c = sqrt(var Re + var Im)/sqrt(n). Die relative Streuung ist sqrt(var Re + var Im)/abs(phi_c).

## 4. Kontrollen (ohne Urteilskraft)

- **Codeprobe:** Rekursion gegen die dichte Loesung (I + a A) psi = J (N ~ 2000), gegen die abgebrochene Reihe
  K = (1/2) A Summe (-a A)^k und Zuschauer gegen Maskensumme.
- **Normierung an der Punktquelle (Hinweis der Leitung):** J = rho am eingefuegten Ursprung, also phi = K(0 -> x).
  - Erwartung (1/2) J0(m tau) [S: (3.23)] an tau in {0,5; 1; 2; 3; 5; 8; 12; 16}, Rapiditaet zeta in {0; 0,5; 1}.
  - rho = 200, 16 Saaten, Abweichung in SE und relative Streuung.
- **Kontinuum:** k-Raum gegen Quadratur an den 18 Pruefpunkten; Normanteil am Klassenrand; analytische
  Paketgeschwindigkeit <v> = Integral v(k) |A(k)|^2 / Integral |A(k)|^2 mit A = h^(k - p) g^(omega - w_k)/(2 w_k).
- **Reines Stichprobenrauschen [M]:** Waere phi exakt das Kontinuum, streute <x>_k nur durch die zufaellige Lage der Punkte.
  - Vorhersage Var(<x>_k) = Integral (x - <x>)^2 |phi_c|^4 / (rho (Integral |phi_c|^2)^2) (Delta-Methode), daraus die SE der
    Steigung.
  - Der Vergleich mit der gemessenen Streuung von V trennt Feldzittern von Messrauschen.
- **Ganze Scheibe** statt Fenster: V, Streuung, Norm.

## 5. Laeufe

- Nur .69 ueber kleintest.sh, Spuren cpu7 (vor allem) und p4000a, hoechstens zwei zugleich, je Lauf < 10 min.
- Das Skript bricht vor einer Saat ab, wenn die Zeitgrenze (540 s) sonst ueberschritten wuerde. Fehlende Saaten folgen in
  einem weiteren Lauf, mit denselben Saatnummern.
- **Reihenfolge nach dem Einfrieren:**
  - kontinuum.py
  - probe
  - punkt 200 (1 bis 16)
  - feld 50 (1 bis 16)
  - feld 200 (1 bis 16)
  - feld 800 in Bloecken
  - auswertung.py lauf kont aus 50,200,800 16

## 6. Vorhersagen (Karte, unveraendert) und Urteilsregeln

| Nr | Vorhersage (Karte) | Wahrsch. |
|---|---|---|
| KW0 | Kontrolle: Das Saatmittel von phi trifft die Kontinuumsloesung an Pruefpunkten innerhalb von 3 Standardfehlern; die relative Streuung faellt mit rho wie rho^(-1/2) (Steigung -0,5 +- 0,1 ueber drei Dichten) | 70 % |
| KW1 | Kein Ruhesystem: Die Schwerpunkt-Geschwindigkeit (Saatmittel) trifft die Gruppengeschwindigkeit des Kontinuums auf 2 % fuer eta = 0 und eta = 1 | 60 % |
| KW2 | [H] Ausgedehnt zittert weniger: Die Streuung der Schwerpunkt-Geschwindigkeit ueber Saaten ist bei sigma = 8 hoechstens halb so gross wie bei sigma = 2 (gleiche Dichte rho = 200) | 55 % |
| KW3 | Stabil: Die Paketnorm (Summe abs(phi)^2 je Zeitscheibe, Saatmittel) waechst ueber die Laufstrecke um hoechstens den Faktor 1,5 gegenueber dem Kontinuum | 70 % |

- Alle Urteile rechnet code/auswertung.py mechanisch (Hauptmessung = Fenster).
- "Nicht auswertbar", wenn fuer eine benutzte Dichte weniger als 16 Saaten vorliegen.
- **KW0 [F]:**
  - (a) Alle 54 Tests (3 Pruefpunkte x 6 Konfigurationen x 3 Dichten): abs(Saatmittel - phi_c) <= 3 SE_c (komplex).
  - (b) Je Dichte das geometrische Mittel der relativen Streuung ueber die 18 Pruefpunkte. Die Steigung der
    Ausgleichsgeraden log(Mittel) gegen log(rho) liegt in [-0,6; -0,4].
  - Eingetroffen, wenn (a) und (b) gelten.
- **KW1 [F]:**
  - Je Dichte, sigma und eta (18 Faelle): abs(Mittel V - V_c) <= Toleranz.
  - Toleranz 0,02 V_c fuer eta = 1. Fuer eta = 0 ist V_c = 0, dort gilt 0,02 absolut (2 % der Lichtgeschwindigkeit;
    Kartenluecke, Abschnitt 7).
  - Eingetroffen, wenn alle 18 Faelle gelten.
- **KW2 [F]:** bei rho = 200, je eta: s8 = Std_Saaten(V) bei sigma = 8, s2 ebenso bei sigma = 2. Eingetroffen, wenn
  s8 <= 0,5 s2 fuer eta = 0 und fuer eta = 1.
- **KW3 [F]:**
  - R_k = Saatmittel(n_k)/n_c,k; G = Mittel(R der letzten 4 Scheiben)/Mittel(R der ersten 4 Scheiben).
  - Eingetroffen, wenn G <= 1,5 in allen 18 Faellen.
  - Beschreibend daneben max_k R_k (Lesart "nie mehr als 1,5-mal das Kontinuum").

### 6.1 Eigene Erwartung (Schreibtisch des Code-Agenten [M/H], keine Urteilsregel)

- **Rauschen [M, grobe Abschaetzung]:** phi(x) = (1/(2 rho)) Summe_{y vor x} f(y) mit f = J - m^2 phi ist eine
  Monte-Carlo-Summe ueber eine stark schwingende Funktion. Ihr Fehler pflanzt sich mit G_R fort.
  - Var(delta phi) ~ (1/(4 rho)) Integral J0(m tau)^2 |f|^2 ueber die Vergangenheit.
  - Das Paket hat |phi| ~ 1,25 sigma, also |f| ~ m^2 |phi|. Daraus folgt relativ Var/|phi|^2 ~ sigma (1 + ln(T/sigma))/(6 rho).
  - Das Rauschen je Punkt waechst also mit sigma, statt zu fallen. Es reicht ueber den ganzen Zukunftskegel, nicht nur ueber
    das Paket.
- **Erwartung:**
  - KW0 eingetroffen (75 %); unverzerrt nach Konstruktion, Steigung -0,5 plausibel.
  - KW1 eingetroffen (55 %); Gefahr: die |phi|^2-Gewichtung verzerrt durch Rauschen, am staerksten bei rho = 50.
  - KW2 **nicht** eingetroffen (60 %); Rauschen je Punkt waechst mit sigma, das Mitteln ueber mehr Punkte gleicht das
    hoechstens aus.
  - KW3 eingetroffen (65 %); R > 1 durch die Rauschvarianz, mit der Zeit wachsend, bei rho = 50 und sigma = 8 am
    groessten.

## 7. Hinweise zur Karte (vor dem Einfrieren offengelegt)

1. **Kartenfehler KW1, Bezugsgeschwindigkeit.**
   - Die Kartengroesse "Gruppengeschwindigkeit" heisst woertlich v_g = d omega/dp = tanh(eta) = 0,7616 bei eta = 1.
   - Das Kontinuumspaket selbst laeuft bei runder Laborhuelle langsamer. Die Gewichtung |A(k)|^2 ~ exp(-sigma^2 ((k - p)^2 +
     (omega - w_k)^2))/w_k^2 verschiebt zu kleinerem k.
   - [E, nur Kontinuum, analytisch] <v> = 0,7118 / 0,7507 / 0,7590 fuer sigma = 2 / 4 / 8, also -6,5 / -1,4 / -0,3 %
     gegen tanh(1).
   - Nach Kartenwortlaut wuerde schon die exakte Kontinuumsloesung bei sigma = 2 an 2 % scheitern.
   - **Berichtigung [F]:** Bezug ist V_c, die Schwerpunktgeschwindigkeit des Kontinuumspakets mit identischer Messung.
     tanh(eta) und das analytische <v> werden daneben genannt.
   - **Urteil nach Wortlaut** (Bezug tanh(eta)) wird zusaetzlich berichtet. Erwartung: nicht eingetroffen, wegen sigma = 2.
2. **Kartenluecke KW1 bei eta = 0:** 2 % von V_c = 0 ist null. Festlegung 0,02 absolut (Abschnitt 6). Woertlich (relativ)
   ist der Fall unerfuellbar; das Urteil nach Wortlaut nennt ihn "nicht eingetroffen", sofern V nicht exakt 0 ist.
3. **Offen gelassen und festgelegt:** Pruefpunkte, komplexe SE, Pooling der Streuung (KW0); Dichten und sigma fuer KW1;
   eta fuer KW2; Lesart des Wachstumsfaktors (KW3); Abklingzeit, Scheiben, Fenster (Abschnitt 3). Alles [F] in den
   Abschnitten 2, 3 und 6.
4. **Laborhuelle und "kein Ruhesystem":** Bei runder Laborhuelle ist das eta-1-Paket nicht der Boost des eta-0-Pakets. Der
   Vergleich der Rapiditaetsstreuung zwischen eta = 0 und 1 (Hinweis der Leitung) ist deshalb nur beschreibend, und
   Unterschiede koennen von der Quelle kommen, nicht vom Netz.
5. **Benincasa-Dowker-Vergleich (beschreibend, Karte):** nur, falls am Ende Zeit bleibt; sonst als "nicht gerechnet"
   gemeldet.

## 8. Rauch (vor dem Einfrieren)

- **Gesehen [E]** (03:48:03 bis 03:48:14 UTC, Ordner rauch-69/), alle rc = 0:
  - **Codeprobe** (rho = 5, N = 2142): Rekursion gegen dichte Loesung, relative Abweichung 9,3e-16 (psi) und 1,4e-15
    (C psi). Abgebrochene Reihe 7,6e-12, Zuschauer 2,4e-15.
  - **Punktquelle** (rho = 200, Saaten 91 und 92, je 0,5 s): Werte liegen bei (1/2) J0(tau), etwa 0,469 / 0,466 / 0,473
    gegen 0,469 bei tau = 0,5. Normierung und Vorzeichen der Masse stimmen also (falsches Vorzeichen gaebe
    anwachsendes I0).
  - **Kontinuum** (9,2 s):
    - Quadratur gegen k-Raum an den 18 Pruefpunkten <= 3,7e-5 relativ.
    - Normanteil am Klassenrand <= 5e-31.
    - Analytisches <v> wie in Abschnitt 7.1.
  - **Feld rho = 50, Saat 91:** N = 436 512, Loesen 2,8 s, Messen 0,6 s; max abs(psi) = 16,4; alles endlich.
### 8.1 Zeitmessung und Pfadprobe (03:48:14 bis 03:52:09 UTC)

- **Feld:**
  - rho = 50, Saat 92: 3,4 s.
  - rho = 200, Saaten 91 und 92: je 15,1 s (Loesen 12,2 s), N = 1,75 Mio.
  - rho = 800, Saat 91: 68,3 s (Loesen 54,6 s, Messen 11,6 s), N = 6 985 491. rc = 0 unter MemoryMax 4G, alles endlich.
- **rho = 800 passt also:** 16 Saaten brauchen ~18 min, verteilt auf drei Laeufe zu hoechstens 7 Saaten (je < 540 s).
  Es bleibt bei rho in {50; 200; 800}.
- **Pfadprobe auswertung.py** auf dem Rauchordner (rho = 50 und 200, je 2 Saaten): rc = 0, alle vier Bilder und
  auswertung.json geschrieben, kein NaN.
  - Angesehen habe ich nur die Schluessel und die Kontinuumswerte, nicht die Urteile, Bilder oder Werte der Kausalmenge.
  - Kontinuum: Fenster W = 30 / 14 / 24 / 16 / 28 / 29 (sigma, eta = 2,0 / 2,1 / 4,0 / 4,1 / 8,0 / 8,1).
  - V_c (Fenster) = 0 / 0,7139 / 0 / 0,7506 / 0 / 0,7587; ganze Scheibe 0,7117 / 0,7507 / 0,7587 fuer eta = 1. Die
    eta-0-Werte liegen bei 1e-17.
- **Folge fuer den Plan:** keine. Keine Schwelle und keine Regel geaendert.

## 9. Einfrieren

- Kopie PLAN.md.eingefroren-JJJJMMTT-HHMMSS (Zeit per date), Code-Kopien mit derselben Endung, sha256 in
  code/pruefsummen-einfrieren.txt.
- Danach aendern sich Plan und Urteilsregeln nicht. Code nur bei echten Fehlern, offengelegt im ERGEBNIS.
