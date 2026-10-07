# LESUNG-PLAN: Frische mathematische Gegenlesung von BEWEIS-PLAN.md (M0)

- Leser: frischer Gegenleser (Claude, Haus Anthropic), kein Autor, keine Rechnung, keine Aenderung fremder Dateien.
- Beginn 2026-09-30 06:39:41 CEST (date). Ende: siehe letzte Zeile (date).
- Gelesen (ganz): BRIEF.md, BEWEIS-PLAN.md (Fassung 06:20), STAND.md (Fassung 06:39),
  bic-proof/analytic/CERTIFICATION.txt, OBSTRUCTION.txt, UMLAUF-CODEX.md; zusaetzlich zum Abgleich
  bic-proof/analytic/CONTINUUM-MEMBERSHIP.txt, REVIEW-CERTIFICATE.txt, REVIEW-ROBUST-INPUT.txt.
- Methode: jede Formel der Lemmata P, J, W, T, T0, K, Pos, R von Hand nachgerechnet (Kerne, Konstanten,
  Vorzeichen, Randwertformeln, Wronski-Identitaet, Restglied, Konditionierung). Literatur nur als [L?], nichts
  an der Quelle geprueft.

## Gesamturteil: TRAGFAEHIG MIT AUFLAGEN

Kein Fehler gefunden, der aus einem bestandenen Zertifikat einen falschen Beweis machen wuerde. Die Kette
"H(z*) = 0 => globales positives Profil + abklingende Loesung mit A(0) = B(0) = 0" ist richtig, die
Schwanzkonstanten stimmen, Lemma K (Brouwer mit Stoerterm) ist korrekt. Ein Befund ist blockierend (der Satz
hat noch Platzhalter, Abschnitt 6 ist leer; das ist an M0 erwartbar, verhindert aber "bewiesen", solange es
offen bleibt). Sieben Befunde sind wesentlich, die uebrigen klein.

## Nachgerechnet und in Ordnung (damit der Autor es nicht noch einmal tun muss)

- Linearisierung, V_pm, C, dV = -4S + 4.5 S^2, C = -2S + 3S^2, N(f): stimmen mit BRIEF, bic2.py-Angaben und
  Codex (D, S0, Rueckwaertsstart (0,1,0,-kappa)). Alle Kopplungs- und Potentialterme sind O(S) = O(f^2);
  es gibt keinen O(f)-Term, weil U''(S) S = -2S + 3S^2 selbst O(S) ist. Vorzeichen spielen in P und J keine
  Rolle, weil nur Betraege eingehen.
- Fenster: omega* = sqrt(0,79767679) = 0,89313; 1 - omega* = 0,10687 < rho* = 1,74462 < 1 + omega* = 1,89313.
  Abstand zum oberen Rand 0,1485, zum unteren 1,64. k^2 = 5,958, kappa_c^2 = 0,2750 (kappa_c = 0,5244).
  Auf einem Kasten der Breite 1e-10 oder kleiner ist das trivial strikt.
- Lemma P: G(r,s) = (1 - e^{-2 kappa0 (s-r)})/(2 kappa0) ist der richtige Kern fuer u~ = r e^{kappa0 r} f;
  0 <= G <= 1/(2 kappa0); Selbstabbildung K m^3, Kontraktion Lambda, Randwertformel
  e^{kappa0 r} u' + kappa0 c = -int (1 + e^{-2 kappa0 (s-r)})/2 q u~ und die Schranke 2 kappa0 K m^3 stimmen.
  Folgerung fuer E_1, E_2 stimmt (f' = (u' - f)/r eingesetzt).
- Lemma J: K_A = sin(k(s-r)) e^{-kappa_c (s-r)}/k loest A'' + k^2 A = g mit Nullanteil im offenen Kanal
  (nachdifferenziert), K_B richtig, Gronwall-Schluss int q_J e^{mu Q} = (e^{mu Q} - 1)/mu richtig,
  |d_r K_A| <= sqrt(1 + kappa_c^2/k^2) richtig, Ableitungsschranken richtig, E_J-Komponenten passen zu J_0.
- Lemma W: W(Psi, R_i)(0) = Psi_i(0); H_3 = H_4 = 0 => Psi(0) = 0, Psi != 0 (B~ -> 1) => BIC. Richtig.
- Lemma T0: Greensche Darstellung f = a + r^2 int tau(1-tau) N, f' = r int tau^2 N, Rekursion
  (n+2)(n+3) f_{n+2} = [N(f)]_n, Iteriertenschranke (Lambda R^2)^m/(2m+1)!: alle richtig.
- Lemma T: Picard auf der komplexen Scheibe, Konvexitaetsschritt, Cauchy-Ungleichung, Rest beta q^N/(1-q):
  richtig.
- Lemma K: Mittelwertsatz zeilenweise, Kr-Einschliessung, Brouwer, Invertierbarkeit aus ||I - Y D|| < 1:
  richtig (Krawczyk-Operator mit beschraenktem Stoerterm).
- Lemma Pos: S_- = (2 - sqrt(4 - 6 kappa0^2))/3 = 0,110 (f < 0,332); Minimumsargument richtig.
- Lemma R: Paritaetsargument (f gerade, Psi ungerade, A/r gerade analytisch) richtig.
- Groessenordnungen bei L = 40: e^{-2 kappa0 L} = 2,4e-16, K = 4e-19, eta = 3e-16, Lambda = 6e-17,
  Q = 6e-17, eps = 5e-17. Die Schwanzlemmata sind bei L = 40 also um Groessenordnungen schaerfer als noetig.
  Bei L = 30 waeren die Schwanzfehler etwa 2e-12 (immer noch ausreichend).

## Befundliste

Schweregrade: blockierend (verhindert "bewiesen", falls offen), wesentlich (muss vor M4 behoben oder
ausdruecklich als Luecke gefuehrt werden), klein (Wortlaut, Vollstaendigkeit, Protokoll).

### B1 (blockierend, faellig M4): Satz mit Platzhaltern, Abschnitt 6 leer

Der Satz sagt "Kasten Z (Abschnitt 6, explizite dyadische Grenzen)", "nahe 0,79767679", "nahe 1,74461754",
"K e^{-kappa_c r}". Abschnitt 6 ist leer. Ohne explizite Zahlen gibt es keinen Satz, nur ein Geruest.

Anforderung: "Im Satz stehen die dyadischen Grenzen von Z fuer a, c, rho und omega (oder omega^2; eine der
beiden Groessen festlegen und durchgaengig verwenden), die Konstante K = 1 + eps/(mu k) + eps/(2 mu kappa_c)
mit Zahlenwert, sowie L. In Abschnitt 6 stehen: L, khat, q = h/R, N, Praezision, Schrittzahl, die Werte
eps_1..eps_4 ueber Z, die geprueften Bedingungen (i)-(iv) von Lemma P ueber Z, die Untergrenzen von k^2 und
kappa_c^2 ueber Z, ||I - Y D||_inf, der Innenabstand von Kr zu Z je Koordinate, und die gemessene
Laufzeit (date, nicht geschaetzt). Fehlt eine dieser Zahlen, heisst das Ergebnis 'Beweisgeruest'."

### W1 (wesentlich): Konditionierung des Vorwaertsschusses bis L = 40 nicht ausgewiesen

Die Profilzeile H_0,1 = s1 (f_a(L) - c e^{-kappa0 L}/L) hat Empfindlichkeit d H_0,1/d a = s1 d_a f(L) ~
e^{2 kappa0 L} = 4e15 (L = 40; 5e11 bei L = 30), weil jede Stoerung des Profils wie e^{kappa0 r} waechst und
s1 = L e^{kappa0 L} noch einmal denselben Faktor bringt. Folgen: (a) der Kasten in a ist um e^{-2 kappa0 L}
duenner als in c (Groessenordnung 1e-33 bei 1e-18 in c); z0 muss deshalb in a auf mindestens 120 Bit
exakt dyadisch gespeichert und die Newton-Iteration entsprechend weit konvergiert sein. (b) Jeder
Schrittrest beta_j q^N/(1-q) im Kern (r < 2) wird in H_0,1 mit etwa L e^{2 kappa0 L} e^{-2 kappa0 r_j}
verstaerkt; grob gerechnet ist die Breite von H_0,1(z0) etwa 1e18 q^N. Mit q = 1/2, N = 64 (5e-20) waere
das 1e-2: Kr passt dann nicht in Z. Mit q = 1/4, N = 64 (1e-39) etwa 1e-21: ausreichend. Die Zeilen
H_0,3, H_0,4 sind nach der Skalierung s3 gut konditioniert (Verstaerkung s3 e^{kappa_c (L - r)} <= 1).
Codex nennt dieselbe Gefahr in CONTINUUM-MEMBERSHIP.txt ("Vorwaertsintegration bis R kann wachsende
Profil-/geschlossene Modenanteile stark aufblasen") und schlaegt Anschluss bei r_m = 6 mit Rueckwaerts-
integration des Schwanzes vor.

Anforderung: "Abschnitt 6 enthaelt eine Budgetrechnung: Summe ueber alle Schritte von (Schrittrest +
Rundung) mal Verstaerkung bis L mal s1 bzw. s3, verglichen mit dem Kastenradius je Koordinate; daraus
folgen q, N und die Praezision, nicht umgekehrt. Alternativ (Entwurfsentscheidung des Autors, mit Zeit in
STAND.md): Anschluss an einem Zwischenpunkt L_m (etwa 8 bis 15) mit Rueckwaertsintegration des Schwanz-
profils und der Jost-Loesung von L nach L_m aus den strengen Cauchy-Daten der Lemmata P und J; das senkt die
Verstaerkung von e^{2 kappa0 L} auf e^{2 kappa0 L_m}. Auch dann bleiben die Lemmata unveraendert gueltig."

### W2 (wesentlich): Lemma T braucht R < r_j fuer alle Schritte mit r_j > 0

Fuer das Profil steht 2/r in F. Lemma T verlangt F analytisch auf Dt x B; also muss die Scheibe (und das
umschliessende Quadrat Dt) den Punkt 0 ausschliessen: R < r_j strikt. Ebenso konvergiert die Taylor-
Rekursion von 2/(r_j + t) nur fuer |t| < r_j. Das steht nirgends. Folge fuer das Gitter: nach dem
T0-Schritt bis r_1 = h_0 muss der naechste Radius kleiner als h_0 sein, die Schritte wachsen also
zunaechst geometrisch. In arb liefert 2/Dt mit 0 in Dt zwar keine endliche Kugel (der Einschluss-Test
scheitert dann laut), ein stiller Fehlbeweis ist deshalb unwahrscheinlich; die Voraussetzung gehoert
trotzdem in den Wortlaut und in den Pruefcode (Test 0 nicht in Dt vor jedem Schritt).

Anforderung: "In Lemma T den Zusatz aufnehmen: 'F analytisch auf Dt x B; fuer das Profil heisst das
R < r_j, geprueft in Kugelarithmetik vor jedem Schritt.' Das Schrittprotokoll fuehrt r_j, R, h je Schritt."

### W3 (wesentlich): "Eingebettet" ist nicht definiert

Der Satz nennt "gebundener Zustand im Kontinuum" und "Kanal offen", definiert aber nicht, worin rho*
eingebettet ist. Fuer das reelle Bueschel P(rho) = [[-Laplace + U' + U''S - (omega + rho)^2, U''S],
[U''S, -Laplace + U' + U''S - (omega - rho)^2]] ist das freie Kontinuum (S = 0) elementar:
{rho: (omega + rho)^2 >= 1 oder (omega - rho)^2 >= 1}, fuer rho > 0 also [1 - omega, oo). Dass das
wesentliche Spektrum des vollen Bueschels dasselbe ist, folgt aus relativer Kompaktheit der S-Terme
(Weyl-Satz) [L?], wird aber im Plan nirgends behauptet oder belegt.

Anforderung: "Im Satz 'eingebettet' operational definieren: 'rho* liegt im Kontinuum des freien Bueschels
[1 - omega*, oo), da (omega* + rho*)^2 > 1; es gibt eine nichttriviale L^2-Loesung.' Der Zusatz
'wesentliches Spektrum des vollen Bueschels' nur mit Quellenbeleg (Weyl-Satz fuer relativ kompakte
Stoerungen, z. B. Kato, Perturbation Theory, IV.5.35, oder Reed-Simon IV, XIII.4) [L?], sonst weglassen.
Zusatz 'im mitrotierenden Rahmen 2 pi/rho*-periodisch' statt 'zeitperiodisch' (delta phi selbst ist mit
den Frequenzen omega* +- rho* nur quasiperiodisch)."

### W4 (wesentlich fuer die Schnittstelle zu Codex, klein fuer den Satz selbst): Umkehrung von Lemma W fehlt

Der Plan beweist nur H = 0 => BIC. Fuer den Satz reicht das. Codex' Hindernissatz (OBSTRUCTION.txt, H1
"exakte lokalisierte einfache radiale BIC-Mode", H4 "kein zweiter unabhaengiger Modenanteil bei rho")
braucht aber die Einfachheit: Jede L^2-Loesung bei (rho*, omega*) ist ein Vielfaches von Psi. Das ist ein
kurzes Lemma: der Raum der auf [L, oo) abklingenden Loesungen ist eindimensional, weil das
Fundamentalsystem aus Psi und drei Loesungen mit Asymptotik cos(kr), sin(kr), e^{kappa_c r}(0,1) besteht
(Levinson-Asymptotik fuer x' = (Lambda + R(t)) x mit R in L^1 [L?: Coddington-Levinson, Kap. 3, Satz 8.1;
Eastham 1989, Satz 1.3.1], oder direkt per Volterra: die Kerne sinh(kappa_c (s-r)) konvergieren, weil
2 kappa0 = 0,900 > kappa_c = 0,524). Ohne dieses Lemma darf der Satz weder "die" Mode noch "einfach" sagen,
und die Leitung darf Satz und Hindernissatz nicht aneinanderhaengen.

Anforderung: "Entweder Lemma W um die Umkehrung ergaenzen (Beweis im Text oder Quelle an der Quelle geprueft),
oder in der Lueckenliste eintragen: 'Einfachheit der Mode nicht bewiesen; Codex' H1/H4 damit nicht
abgedeckt.'"

### W5 (wesentlich): Stetigkeit von E auf Z ist nur skizziert

Lemma K braucht H stetig auf ganz Z, also E_1..E_4 stetig in (a, c, rho, omega). Lemma P sagt "T haengt
stetig ab, gleichmaessig kontrahierend"; der Ball X haengt aber selbst von (c, omega) ab (Mitte c,
Radius eta(c, omega)). Lemma J sagt "gleichmaessige Konvergenz mit stetigen Kernen". Beides ist richtig,
aber nicht ausgefuehrt; und die Bedingungen (i)-(iv) sowie k, kappa_c > 0 muessen fuer jedes z in Z
gelten, sonst ist E dort gar nicht definiert.

Anforderung: "Beweis der Stetigkeit ausschreiben: fester Umgebungsball X' um c0 mit Radius eta' > eta,
auf dem dieselben Schranken (ii), (iii) gelten; dann ||u~_z - u~_z'|| <= (1 - Lambda)^{-1}
||T_z u~_z' - T_z' u~_z'||, und der letzte Term geht gegen 0. Fuer J: Picard-Iterierte stetig in
(rho, omega, c), gleichmaessig konvergent. Im Zertifikat: (i)-(iv), k^2 > 0, kappa_c^2 > 0 ueber ganz Z
in Kugelarithmetik protokollieren (kappa0 monoton: Randwerte genuegen, das ist zu begruenden)."

### W6 (wesentlich): Jets vollstaendig auflisten, Einwickeleffekt messen

Die Krawczyk-Matrix D muss DH_0(z) fuer alle z in Z einschliessen. Dazu gehoeren d_a R_i und d_omega R_i
ueber die Koeffizientenabhaengigkeit von f (Kettenregel mit d_a f, d_omega f; d S = 2 f d f), d_rho R_i
mit d_rho V_pm = -+ 2 (omega +- rho), d_rho kappa_c und d_omega kappa_c in H_0,3/4, sowie die expliziten
c- und omega-Ableitungen in H_0,1/2. Der Plan sagt nur "Jets in a, rho, omega". Der Einwickeleffekt wird
fuer den offenen Kanal per (al, be)-Variablen entschaerft; fuer den geschlossenen Kanal ist Wachstum
e^{kappa_c r} echt und harmlos, wenn die Huellen im Verhaeltnis zum Wert schmal bleiben. Ob sie das tun,
entscheidet ||I - Y D|| < 1.

Anforderung: "Die Zustandsliste des gekoppelten Jet-Systems (Profil 2, Profilvariationen 4, R_1, R_2 je 4,
deren Variationen nach a, rho, omega je 8; erwartet 38 Komponenten) und die Kettenregel-Terme im Plan
ausschreiben. Im Protokoll je Schritt die relative Breite der Huellen von f, R_i und der Jets ausgeben;
am Ende ||I - Y D||_inf und die Breite jedes Eintrags von D relativ zu |mid D|."

### W7 (wesentlich): Codex' Parallelplan CONTINUUM-MEMBERSHIP.txt ist nicht abgeglichen

STAND.md (06:05) nennt nur CERTIFICATION.txt. bic-proof/analytic/CONTINUUM-MEMBERSHIP.txt (05:55) enthaelt
Codex' eigenen Plan fuer dasselbe Zertifikat: Lemma P (Profil-Tailmap, Dirichlet-Kern, explizite
Konstanten), Lemma B (eindimensionaler BIC-Tail, dieselben Volterra-Gleichungen wie Lemma J),
sechsdimensionales Anschlussproblem bei r_m = 6 mit Unbekannten (a, p, rho, b, A, B), Krawczyk-Test.
Vergleich: (1) Gleichungen identisch; (2) Codex normiert am Ursprung (v'(0) = 1, u'(0) = b), der Plan im
Unendlichen (B~ -> 1) mit Wronski-Formen: der Plan kommt so mit vier Unbekannten aus, das ist die
elegantere Wahl; (3) Codex' Schwanzkonstanten sind um Faktor 2 (kubisch) bzw. 6 (quintisch) schaerfer, die
des Plans sind als Schranken ebenfalls richtig (nachgerechnet), bei L = 40 spielt das keine Rolle;
(4) Codex' Hinweis zum Aufblasen wachsender Anteile deckt sich mit W1; (5) Codex verlangt
Parameterableitungen der Tailmap; der Plan umgeht sie durch Brouwer mit Stoerterm und verzichtet dafuer
auf Eindeutigkeit (Luecke 5), das ist konsistent. Keine Widersprueche. Gefahr: doppelte Implementierung
desselben Zertifikats, ohne dass die beiden Haeuser es wissen. Chance: eine unabhaengige Codex-
Implementierung waere das "zweite unabhaengige Programm" aus Luecke 2.

Anforderung (an Autor und Leitung): "Modellabgleich um CONTINUUM-MEMBERSHIP.txt ergaenzen (Punkte 1-5).
Leitung entscheidet, ob Codex dasselbe Zertifikat unabhaengig baut (dann als Gegenprobe zu Luecke 2 fuehren)
oder nicht. Ausgabeformat so waehlen, dass Codex' Glieder 3-6 aus CERTIFICATION.txt es nutzen koennen:
Huellen von f, A, B auf einem Gitter in [0, L] plus die Schwanzkonstanten (m, kappa0, K, eps, kappa_c)."

### K1 (klein): Auswahl des Profils im Satz benennen

f ist durch (a*, omega*) als Loesung des Anfangswertproblems eindeutig bestimmt (Lemma T0). Ob es die
einzige positive abklingende radiale Loesung bei omega* ist, bleibt [L?]. Hinweis zur Literaturpruefung:
Mit f(x) = lambda g(mu x), lambda^2 = 4/3, mu^2 = 8/3 wird die Profilgleichung zu
Laplace g - w g + g^3 - g^5 = 0 mit w = 3 kappa0^2/8 = 0,0759; das Fenster omega^2 in (1/2, 1) entspricht
w in (0, 3/16). Das ist genau die Form der kubisch-quintischen NLS, fuer die Killip, Oh, Pocovnicu, Visan
(ARMA 2017) Eindeutigkeit des Grundzustands fuer 0 < w < 3/16 angeben sollen [L?], gestuetzt auf
Serrin-Tang 2000 [L?]. An der Quelle pruefen, ob "positiv radial" oder nur "Grundzustand" gemeint ist.

Anforderung: "Satz: 'f ist die Loesung des Anfangswertproblems zu (a*, omega*); es ist ein positiver
radialer Q-Ball. Ob es der einzige ist, wird nicht behauptet [L?].' Lueckenliste 4 um die Skalierung und
die zu pruefende Aussage ergaenzen."

### K2 (klein): Die Richtung "BIC => H = 0" nicht behauptet, aber Folge nennen

Lemma W sagt richtig, dass die Umkehrung nicht gebraucht wird. Folge, die in den Satz gehoert: Der Satz
erlaubt keine Aussage "kein weiterer BIC in Z" und keine Aussage ueber Eindeutigkeit von (rho*, omega*).
Anforderung: "Unter 'Nicht behauptet' ergaenzen: 'Nichtexistenz weiterer Nullstellen in Z'."

### K3 (klein): Skalierungskonstanten s1, s3 als feste dyadische Zahlen

s1 "= L e^{kappa0 L}" ist nicht dyadisch; als feste dyadische Naeherung ist es zulaessig, weil es nur
skaliert und in den E-Schranken als Faktor mitlaeuft. Anforderung: "Schreiben: 's1, s3 feste dyadische
Zahlen nahe L e^{kappa0 L} bzw. e^{-kappa_c L}; ihr genauer Wert ist unerheblich.'"

### K4 (klein): Lemma T, Restglied auch fuer Ableitungskomponenten

Im T0-Schritt ist f' keine Zustandskomponente; der Rest fuer f'(h) braucht die Cauchy-Schranke von g = f'
aus B_g = (Dt/3) N(B_f). Der Plan hat B_g; im Text steht der Rest nur fuer y. Anforderung: "Satz in
Lemma T0 ergaenzen: 'Rest fuer f'(h) mit beta_g aus B_g, Koeffizienten g_n = (n+1) f_{n+1}.'"

### K5 (klein): A-priori-Huelle: Suche und Pruefung trennen

STAND (06:39) beschreibt die Suche der Huelle per epsilon-Inflation (Faktor 9/8). Zulaessig, solange die
Pruefung Y0 + Dt F(Dt, B) in B ein getrennter, protokollierter Kugel-Einschlusstest ist. Anforderung:
"Im Protokoll je Schritt: Huelle B, Ergebnis des Einschlusstests (acb_contains), Anzahl Inflationsrunden."

### K6 (klein): z0 exakt dyadisch mit genuegend Bits

Wegen W1 muss a0 mit mindestens 120 Bit Mantisse gespeichert werden (z0.json als Bruch m/2^e, nicht als
float). Anforderung: "z0.json enthaelt Zaehler und Exponent je Koordinate; sha256 im Protokoll."

### K7 (klein): Softwarevertrauen praezisieren

Luecke 2 ist richtig gefuehrt. Anforderung: "Versionen von python-flint, FLINT und Arb, sha256 des Wheels
und des Interpreters ins Protokoll; sowie die Aussage, dass keine float64-Operation in der strengen Kette
liegt (Startwerte und Y ausgenommen)."

### K8 (klein): Lemma R, letzte Zeile

"1 - omega* < rho* < 1 + omega* ... geprueft auf ganz Z" gehoert als Zahl ins Zertifikat (Untergrenzen von
k^2 und kappa_c^2 ueber Z). Anforderung: siehe B1.

### K9 (klein): Umlaufzahl-Vorzeichen

bic2 meldet Umlaufzahl -1, Codex +1. Das ist eine Orientierungskonvention (Achsenreihenfolge, Vorzeichen
von F), fuer diesen Plan ohne Belang, weil keine Umlaufzahl benutzt wird. Kein Handlungsbedarf; nur nicht
als Widerspruch zitieren.

## Antworten auf die sieben Prueffragen (Kurzform)

1. Satz: Existenzaussage; Profil durch (a*, omega*) als AWP-Loesung eindeutig ausgewaehlt, Eindeutigkeit
   unter allen positiven Loesungen [L?] nicht tragend; Stetigkeit in omega nicht noetig (Entwurf loest
   alles gleichzeitig, das ist die richtige Entscheidung). "Eingebettet" undefiniert (W3). rho* strikt im
   offenen Fenster, Abstand 0,1485 nach oben.
2. Aequivalenz: H = 0 => BIC richtig und ausreichend fuer den Satz; Umkehrung fehlt (W4, K2).
   Kanalstruktur auf Z trivial, aber als Zahl zu protokollieren (B1).
3. Lemmata P, J: Konstanten richtig; alle Terme erfasst, keine langsamer als f^2 abfallenden Terme;
   L = 40 gilt fuer ganz Z, wenn (i)-(iv) mit Randwerten von kappa0 und c geprueft werden (W5).
4. Lemmata T, T0: Rest streng (komplexe Huelle, Cauchy); Singularitaet bei 0 durch T0 richtig behandelt;
   fuer r_j > 0 fehlt R < r_j (W2); Ableitungsrest im T0-Schritt benennen (K4).
5. Lemma K: Argument richtig; Stetigkeit auf ganz Z gegeben, sobald die Huellen ueber Z existieren und E
   stetig ist (W5); Einwickeleffekt fuer den offenen Kanal entschaerft, Konditionierung der Profilzeile
   nicht ausgewiesen (W1); Parameterabhaengigkeit des Profils ueber Jets richtig, Liste fehlt (W6).
6. Luecken: fehlen W1, W2, W3, W4, W5 und die Zahlen aus B1. "Bewiesen" verhindern bei Offenbleiben:
   B1 (keine Zahlen), W2 (Voraussetzung von Lemma T nicht geprueft). Literaturbeleg noetig nur fuer:
   Weyl-Satz, falls "wesentliches Spektrum" behauptet wird (W3); Levinson, falls Einfachheit ueber
   Literatur statt Volterra (W4); KOPV/Serrin-Tang nur fuer "der" Q-Ball (K1).
7. Codex: keine Ergebnisdoppelung (Codex hat kein strenges BIC-Zertifikat gerechnet); Plandoppelung mit
   CONTINUUM-MEMBERSHIP.txt (W7); Formeln kompatibel, keine Widersprueche; Codex' Hindernissatz braucht
   Einfachheit der Mode (W4).

## Was ich nicht getan habe

Keine Rechnung, keine Aenderung an BEWEIS-PLAN.md, STAND.md oder Codex-Dateien, kein Code gelesen
(bewkern.py, pruef.py liegen auf der .69 und waren nicht Teil des Auftrags; die Code-Gegenlesung ist
Luecke 3 des Plans und bleibt offen).

- Ende 2026-09-30 06:58:03 CEST (date). Dauer 18 min 22 s.
