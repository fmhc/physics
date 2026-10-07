# BEWEIS-2-PLAN: zwei weitere stille Stellen rechnergestuetzt (T1 = l 0, n 2; T2 = l 1, n 1)

- Autor: Beweis-Agent der Leitung claude-primary (Haus Anthropic), derselbe wie BEWEIS-1. Auftrag: BRIEF.md.
- Diese Fassung ab 2026-09-30 12:11:22 CEST (date). Zeitverlauf: STAND.md.
- Grundlage: BEWEIS-1 (RUNDE-07/beweis/BEWEIS.md, BEWEIS-PLAN.md, zertifikat/), unveraendert gelassen.

## 1. Ziele und Satzaufbau

| Ziel | l | n | Startwerte (DATENPAKET) | Satzaufbau |
|---|---|---|---|---|
| T1 | 0 | 2 | omega^2 = 0,6851289043286388, rho = 1,6903565771078266 (A02) | wie BEWEIS-1, nur neue Startwerte |
| T2 | 1 | 1 | omega^2 = 0,7544960183525193, rho = 1,826342067337926 (C01) | neuer Sektor: Abschnitt 4 |

Satzform fuer beide Ziele wie BEWEIS-1, Abschnitt 1 (Profil, Mode, Einfachheit, Folgerung), mit Kasten Z in exakten
dyadischen Grenzen aus dem Beweislauf. Korollar Krein (KREIN-1): E_2 = 2 rho [(omega + rho)||a||^2 + (rho - omega)||b||^2]
ist positiv, weil rho - omega > 0 auf ganz Z (geprueft als Kanalzahl rho - omega > 0 in Kugelarithmetik).

## 2. T1 (l = 0, n = 2): was gleich bleibt, was sich aendert

- Kern: bewkern.py **byte-gleich** mit BEWEIS-1 (sha256 a8a7ec6f...). Alle Lemmata (P, J, W, E, T, T0, K, Pos, R,
  Zusatz S, Zusatz J) gelten wortgleich; sie haengen nur ueber die in Kugelarithmetik auf Z geprueften Bedingungen von
  (omega, rho) ab: omega in (1/sqrt 2, 1), k^2 > 0, kappa_c^2 > 0, 2 kappa0 > kappa_c, (i)-(iv) aus Lemma P, Lambda < 1,
  4 - 6 kappa0^2 > 0 (Lemma Pos).
- Treiber: pruef-l0.py = Kopie von pruef-v2.py mit drei Aenderungen (Abschnitt 5).
- n = 2 ist das Leiteretikett aus dem Datenpaket, keine zertifizierte Knotenzahl (berichtigt ab 19:49:12 nach der Lesung der
  letzten Schicht, L1). Kein Lemma benutzt n.
- Parameter vorab (vor dem Newton-Lauf): Weil kappa0 = 0,561 (BEWEIS-1: 0,450) die Vorwaertsverstaerkung
  L e^{2 kappa0 L} bei L = 40 etwa 7000-fach vergroessert, nehme ich L = 32 (e^{kappa0 L} etwa wie BEWEIS-1 bei L = 40).
  - Beweislauf A: L = 32, 256 bit, Punkt N = 64, Kasten N = 48, q = 1/3, Kastenfaktor 8.
  - Wiederholung B: L = 36, 320 bit, Punkt N = 72, Kasten N = 44, q = 1/4, Kastenfaktor 8, gleiches z0.
  - Newton (nicht streng) mit L-Fortsetzung 12, 20, 28, 32, N = 48, q = 1/3, 256 bit.
  - Scheitert A an der Breite, dann Aenderung nur ueber L, N, q oder Bitzahl, jede Aenderung mit date in STAND.md.

### 2.1 Vorab-Zeile T1 (2026-09-30 12:11:22 CEST, vor dem Newton-Lauf und vor dem Startwert-Lauf)

- Erwarteter Bereich: omega*^2 in 0,68512891 +- 1e-7 (Datenpaket: A_out 0,6851289043, W-Fit 0,6851289138,
  Fein-Kurve 0,6851288962; Spanne 1,8e-8, alle mit h = 0,01), rho* in 1,6903566 +- 1e-6 (nur W-Fit vorhanden).
- Empfindlichkeitskontrolle (nicht streng) wie BEWEIS-1: Kastenmitte rho + delta/4 besteht, rho + delta und
  rho + 4 delta verfehlen.
- Scheitern der Erwartung heisst nicht Scheitern des Beweises: Der Beweis steht allein auf Lemmata und Kugelrechnung.
  Eine Nullstelle ausserhalb des Bereichs wuerde aber eine Rueckfrage an das Datenpaket ausloesen.

## 3. T2 (l = 1, n = 1): Aenderungen gegenueber BEWEIS-1 (Auftrag Punkte 1 bis 6)

Wird vor dem ersten T2-Lauf in dieser Datei ausgeschrieben (Lemmata T0-l1, T-l1, J-l1, W-l1, E-l1, Frei-Test l = 1).
Stand der Vorueberlegung:
1. Gleichungen A'' = (V_+ + 2/r^2) A + C B, B'' = (V_- + 2/r^2) B + C A; A, B ~ r^2 am Ursprung; Profil wie l = 0.
2. Start: A = r^2 alpha, B = r^2 beta, alpha'' + (4/r) alpha' = V_+ alpha + C beta (ebenso beta). Integralform
   y(r) = y(0) + (r^2/3) int_0^1 tau (1 - tau^3) F(tau r) dtau, y'(r) = r int_0^1 tau^4 F(tau r) dtau
   (Gewichte 1/10 und 1/5); Reihe (n+2)(n+5) y_{n+2} = F_n.
3. Schwanz exakt mit den Riccati-Funktionen: offen j(x) = sin x/x - cos x, y(x) = -cos x/x - sin x
   (j^2 + y^2 = 1 + 1/x^2), geschlossen d(x) = e^{-x}(1 + 1/x), g(x) = e^{x}(1 - 1/x), W(d, g) = 2 kappa_c.
   Freie Jost-Daten bei L (Normierung e^{kappa_c r} B -> 1):
   J_0 = (0, 1 + 1/(kappa_c L), 0, -(kappa_c + 1/L + 1/(kappa_c L^2))).
4. Einfachheit: Wronski-Komplement wie Lemma E, mit den l = 1-Vergleichsloesungen; Translationsmode liegt bei rho = 0.
5. Kanalzahlen: k^2 = (omega + rho)^2 - 1 > 0, kappa_c^2 = 1 - (omega - rho)^2 > 0 ueber Z.

## 4. T2 (l = 1): Lemmata im Wortlaut (geschrieben ab 2026-09-30 12:22:22 CEST, vor Startwert-, Newton- und Beweislauf T2)

Hinweis zur Reihenfolge: Der Frei-Test l = 1 (Kontrolle, kein Beweislauf) wurde um 12:21:45 in die Warteschlange der
Spur cpu5 gestellt, bevor dieser Abschnitt stand; er lief erst nach Lauf T1-B an.

### 4.1 Gleichungen

delta phi = e^{i omega t} (a(r) e^{i rho t} + b(r) e^{-i rho t}) Y_1m, A = r a, B = r b:
A'' = (V_+ + 2/r^2) A + C B, B'' = (V_- + 2/r^2) B + C A, V_pm, C wie BEWEIS-1 (Profil f unveraendert, l = 0).
Fuer jedes m = -1, 0, 1 dieselbe Radialgleichung; alle Aussagen gelten je (l, m) = (1, m).
Berichtigung nach der Fremdlesung (ab 2026-09-30 13:15, Abschnitt "Einarbeitung der Lesungen" in BEWEIS-2.md):
Y_1m bezeichnet hier eine **reelle** orthonormale Basis der Kugelflaechenfunktionen zu l = 1 (proportional zu x/r,
y/r, z/r). Nur dann traegt der gemeinsame Faktor Y_1m beide Seitenbaender. Bei komplexen Y_lm lautet der Ansatz
delta phi = e^{i omega t} (a(r) Y_lm e^{i rho t} + b(r) Y_lm* e^{-i rho t}). Grund: Mit psi = a Y e^{i rho t}
+ b Z e^{-i rho t} bringt der Term sp * conj(psi) in das Seitenband e^{i rho t} den Winkelfaktor conj(Z); die
Gleichung schliesst nur fuer Z = conj(Y). Die Radialgleichungen bleiben gleich.

### 4.2 Lemma T0-l1 (Start bei r = 0)

Die regulaeren Loesungen sind A = r^2 alpha, B = r^2 beta mit alpha, beta analytisch und
alpha'' + (4/r) alpha' = V_+ alpha + C beta, beta'' + (4/r) beta' = V_- beta + C alpha
(die Terme l(l+1)/r^2 heben sich exakt weg). R_1: alpha(0) = 1, beta(0) = 0; R_2: alpha(0) = 0, beta(0) = 1; Ableitungen 0.
Integralform fuer y'' + (4/r) y' = F, y regulaer: y(r) = y(0) + (r^2/3) int_0^1 tau (1 - tau^3) F(tau r) dtau,
y'(r) = r int_0^1 tau^4 F(tau r) dtau (Gewichtsmassen 3/10 * 1/3 = 1/10 und 1/5).
Huellenbedingung: y(0) + (Dt^2/10) F(B) in B_y und B_y' := (Dt/5) F(B), dabei Dt2 als Huelle von {r^2 : |r| <= R}
(Kreisscheibe, wie in T0 von BEWEIS-1; Praezisierung aus der Fremdlesung). Reihe: (n+2)(n+5) y_{n+2} = F_n, y_1 = 0.
Jets (Ableitungen nach a, rho, omega): dieselbe Form mit Quellen d_p V_pm y + d_p C (Gegenkomponente).
Bei r = h0 exakte Umrechnung: A = h0^2 alpha, A' = 2 h0 alpha + h0^2 alpha', ebenso B, dann VOC
(al = A cos(khat h0) - A'/khat sin, be = A sin + A'/khat cos). Beweis wie T0: Volterra-Operator, Iterierte
<= (Lambda R^2)^m / m!; Picard auf der Kreisscheibe; Cauchy-Rest wie Lemma T.

### 4.3 Lemma T-l1 (r > 0)

Wie Lemma T. Der Koeffizient 2/r^2 ist auf r_j + Dt analytisch, weil R < r_j vor jedem Schritt in Kugelarithmetik
geprueft wird (dieselbe Pruefung wie fuer 2/r im Profil). Reihe 2 (w * w)_n mit w_n = (-1)^n / r_j^{n+1}; Huelle 2 WD^2.

### 4.4 Lemma J-l1 (Jost-Loesung mit Riccati-Funktionen)

Freie Loesungen: offen j(x) = sin x/x - cos x, y(x) = -cos x/x - sin x (x = k r), W_x(j, y) = 1,
j^2 + y^2 = 1 + 1/x^2, j'^2 + y'^2 = 1 - 1/x^2 + 1/x^4 <= 1 fuer x >= 1; geschlossen d(u) = e^{-u}(1 + 1/u),
g(u) = e^{u}(1 - 1/u) (u = kappa_c r), W_r(d, g) = 2 kappa_c.
Greensche Funktionen (s >= r): G_A = [j(kr) y(ks) - y(kr) j(ks)]/k, G_B = [d(kc r) g(kc s) - g(kc r) d(kc s)]/(2 kc).
Normiert (A~ = e^{kc r} A, B~ = e^{kc r} B):
- A~ = int_r^oo K_A (dV A~ + C B~), K_A = e^{-kc (s-r)} G_A, |K_A| <= a1 := (1 + 1/(k L)^2)/k.
- B~ = (1 + 1/(kc r)) + int_r^oo K_B (dV B~ + C A~),
  K_B = [(1 + 1/(kc r))(1 - 1/(kc s)) - e^{-2 kc (s-r)} (1 - 1/(kc r))(1 + 1/(kc s))]/(2 kc), |K_B| <= b1 := b0/(2 kc),
  b0 := 1 + 1/(kc L).
- e^{kc r} A' = int e^{-kc (s-r)} d_r G_A (...), |d_r G_A| <= a2 := sqrt(1 + 1/(k L)^2).
- B~' - kc B~ = -(kc + 1/r + 1/(kc r^2)) + int K_B' (...), |K_B'| <= b2 := (2 + 2/(kc L) + 1/(kc L)^2)/2.
  Dabei ist K_B' := (d_r - kc) K_B = e^{kc r} (d_r G_B)(r, s) e^{-kc s} der normierte Ableitungskern, nicht d_r K_B
  (Praezisierung nach der Fremdlesung ab 13:15; Schranke b2 und Code unveraendert, der Codekommentar in
  pruef-l1.py benutzt dieselbe Kurzschreibweise).
Voraussetzungen: k L >= 1, kc L >= 1 (ueber Z geprueft), S wie Lemma P. Mit q_J = |dV| + |C|, Q wie in BEWEIS-1,
mu := max(a1, b1): psi := max(|A~|, |B~|) <= b0 + mu int q_J psi, Gronwall psi <= b0 e^{mu Q}, also mit
eps := b0 (e^{mu Q} - 1)/mu: |A~(L)| <= a1 eps, |B~(L) - (1 + 1/(kc L))| <= b1 eps, |e^{kc L} A'(L)| <= a2 eps,
|e^{kc L} B'(L) + (kc + 1/L + 1/(kc L^2))| <= b2 eps. Also Psi_n = J_0 + E_J mit
J_0 = (0, 1 + 1/(kc L), 0, -(kc + 1/L + 1/(kc L^2))), und e^{kc r}(|A| + |B|) <= K_J := b0 + (a1 + b1) eps auf [L, oo).
Fuer l = 0 (j -> -cos, y -> -sin, d -> e^{-u}) ergeben sich die Kerne von BEWEIS-1. Stetigkeit wie Zusatz S.

### 4.5 Lemma W-l1

Bei r = 0 hat das System die Exponenten 2 (regulaer, R_1, R_2) und -1 (singulaer, S_1, S_2 ~ r^{-1} e_i/3).
W(r^{-1}, r^2) = 3, also W(S_i, R_j) = delta_ij und W(R_i, R_j) = 0 (Grenzwert r -> 0; Logarithmen treten erst in
relativer Ordnung r^3 auf und tragen nicht bei). Fuer Psi = c_i R_i + d_i S_i gilt W(Psi, R_j) = d_j.
H(z*) = 0 heisst W(Psi_n, R_j) = 0, also Psi = c_1 R_1 + c_2 R_2 regulaer am Ursprung (Nullstelle von H =
Regularitaet bei 0; "BIC" nur im operationalen Sinn des Satzes, Wortlaut nach der Lesung ab 13:15).

### 4.6 Lemma E-l1 (geometrische Einfachheit) und Lemma R-l1

- Wie Lemma E, mit Psi_c, Psi_s ~ (j(kr), 0), (y(kr), 0) und W(Psi_c, Psi_s) = k W_x = k != 0; die Konstruktion
  braucht 2 kappa0 > kappa_c (im Gesamtflag, Auflage 1 der Fremdlesung).
- Aussage im Wortlaut der Fremdlesung (Auflage 2): Der Raum der auf [L, oo) quadratintegrierbaren Loesungen im
  Radialsektor (l, m) = (1, m) bei festen (rho*, omega*) ist eindimensional (geometrische Vielfachheit 1). Keine Aussage
  ueber algebraische Einfachheit, Jordan-Ketten oder Stabilitaet.
- Translationsmode: Sie loest die Linearisierung bei rho = 0 (l = 1). Lemma E-l1 ist eine Aussage bei festem
  rho* = 1,826..., dort ist die Translationsmode keine Loesung; sie stoert also nicht.
- Lemma R-l1: alpha, beta sind gerade analytisch (gerade Koeffizienten, der Operator alpha'' + (4/r) alpha' erhaelt die
  Paritaet), also a Y_1m = alpha(|x|) (r Y_1m) mit r Y_1m linear in x: glatt.

### 4.7 Kanalzahlen und Bedingungen (alle ueber Z, im Gesamtflag M3.BESTANDEN)

k^2 > 0, kappa_c^2 > 0, omega in (1/sqrt 2, 1), 2 kappa0 > kappa_c, rho > omega (Korollar Krein), 4 - 6 kappa0^2 > 0,
k L >= 1, kappa_c L >= 1, Lemma P (i)-(iv).

### 4.8 Parameter T2 und Vorab-Zeile T2 (2026-09-30 12:22:22 CEST, vor dem Newton-Lauf T2)

- kappa0 = 0,4955: L e^{2 kappa0 L} bei L = 36 etwa wie BEWEIS-1 bei L = 40. Beweislauf A: L = 36, 256 bit,
  N = 64/48, q = 1/3, Kastenfaktor 8. Wiederholung B: L = 40, 320 bit, N = 72/44, q = 1/4. Newton: Ls 12, 20, 28, 36.
- Erwarteter Bereich: omega*^2 in 0,7544961 +- 3e-7 (A_out 0,7544960184, W-Fit 0,7544962018, Abstand 1,8e-7, h = 0,01),
  rho* in 1,826342 +- 1e-5.
- Empfindlichkeitskontrolle: rho + delta/4 besteht, rho + delta und rho + 4 delta verfehlen.
- Frei-Test l = 1 muss bestehen (A_1, A_1', B_2, B_2' ueberlappen die geschlossenen Werte, B_1 und A_2 enthalten 0).

## 5. Codeaenderungen (Zeile fuer Zeile; Enddateien in zertifikat/)

| Datei | Aenderung gegenueber BEWEIS-1 | Grund |
|---|---|---|
| bewkern.py | keine (byte-gleich, sha256 a8a7ec6f...) | T1 braucht nur neue Startwerte |
| pruef-l0.py Kopf | Kommentar BEWEIS-2 | - |
| pruef-l0.py argparse | neue Optionen --w2, --rho (Vorgabe = BEWEIS-1-Werte) | Startwerte nicht mehr fest im Code |
| pruef-l0.py Modus start | w2 = float(args.w2), rho = float(args.rho); Quellenvermerk nennt DATENPAKET und die Werte | Startwerte T1 |
| pruef-l0.py zert, sha256 | Schluessel = wirkliche Dateinamen (os.path.basename) statt fest 'bewkern.py'/'pruef.py' | Auflage L6 aus BEWEIS-1 |

### 5.1 Nachtrag ab 2026-09-30 12:40:27 CEST (nach den Beweislaeufen): vollstaendige Zeilenliste

**Vermerk zur Pflicht "Liste der geaenderten Codezeilen vor jedem Beweislauf":**
- Vor den Beweislaeufen standen im Plan die T1-Treiberaenderungen (Tabelle oben) und die T2-Aenderungen auf Ebene der
  Lemmata und Funktionen (Abschnitt 4, 12:22:22).
- Nicht vorab im Plan standen:
  - die Treiberaenderungen aus der Fremdlesung (Auflagen 1 und 4, eingebaut 12:16 bis 12:20, vor Lauf T1-A)
  - die Zeilennummern der T2-Aenderungen
  - die Pruefung 0 < h < R (12:28, vor T2-A)
  - die Option --dcexp (12:36, vor B2, vorab in STAND.md)
- Welche Fassung lief, belegt je Zertifikat die sha256 im JSON: T1: pruef-l0.py 7713f636...; T2-A, T2-B:
  pruef-l1.py c1f85f81...; T2-B2: pruef-l1.py eecfb3cd...; Kern bewkern_l1.py 24b3dc8d....
- Die vollstaendige Zeilenliste steht in BEWEIS-2.md, Abschnitt 5 (aus diff der Enddateien). Das ist eine Abweichung vom
  Auftrag; ich melde sie so.

Kurzfassung der Zeilenliste (Enddateien):
- pruef-l0.py gegen pruef-v2.py: 1-3 Kopf; 134 Untergrenzen phibar, eta; 226-227, 257, 261 --w2, --rho; 268-269
  Quellenvermerk; 413-414 sha256-Schluessel; 490-494 Gesamtflag (2 kappa0 > kappa_c, rho > omega, 4 - 6 kappa0^2 > 0);
  570-571 Untergrenzen im Protokoll; 601-618 Export Y, DH_0(Z), Mk, H_0(z0), eps, delta, Kr.
- bewkern_l1.py gegen bewkern.py: 1-7 Kopf; 63, 65-66 Par(l); 177, 185-192 Zentrifugalreihe; 283-356 lin_series0_l1 und
  voc_aus_alpha; 380, 385-391 Zentrifugalhuelle; 498-528 A-priori-Integralform l = 1; 597-599, 617-622, 625-628,
  633-634 step; 651-657 Anfangszustand l = 1.
- pruef-l1.py gegen pruef-l0.py: 1-6 Kopf; 19, 21 Import, ELL; 68 Par(l = 1); 74-76, 79-80 J_0-l1 in H_0; 87-90, 96-99
  DH_0-Zeilen 3, 4; 125-126, 130-141 Lemma J-l1; 156-158 Protokoll K_J und Konstanten; 250 --dcexp; 256-261, 270-290 Frei-Test
  l = 1; 448-449 dcexp im Parameterblock; 489-493 c-Radius mal 2^dcexp; 537-540 Gesamtflag (k L, kc L >= 1; 0 < h < R;
  N, qfac); 623-625 Protokoll Lemma J; 690, 698, 705 Kontrollmodus.
