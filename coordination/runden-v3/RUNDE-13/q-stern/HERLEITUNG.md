# Q-STERN: Herleitung (Newton-Grenzfall, statischer Hintergrund, Cowling-Naeherung)

- Code-Agent, Runde 13. Geschrieben nach dem Laufstart; letzter gemessener Zeitpunkt davor 20:40:29 CEST (date in der
  ssh-Ausgabe), keine eigene Zeitmessung beim Schreiben (Selbstanzeige im ERGEBNIS). Markierungen: [ES]
  eigener Schluss, [H] Hypothese, [L?] aus dem Gedaechtnis, nicht an einer Quelle geprueft.
- Signatur (-, +, +, +), Einheiten wie bball2 (Masse des Feldes = 1, U'(0) = 1).

## 1 Wirkung bis erste Ordnung in Phi (Pruefung der Karte)

- Metrik ds^2 = -(1 + 2 Phi) dt^2 + (1 - 2 Phi) dx^2, Phi statisch, |Phi| << 1.
  - sqrt(-g) = (1 + 2 Phi)^(1/2) (1 - 2 Phi)^(3/2) = 1 + Phi - 3 Phi + O(Phi^2) = 1 - 2 Phi
  - g^tt = -1/(1 + 2 Phi) = -(1 - 2 Phi) + O(Phi^2); g^ij = delta_ij/(1 - 2 Phi) = (1 + 2 Phi) delta_ij + O(Phi^2)
- L = sqrt(-g) [-g^{mu nu} d_mu phi* d_nu phi - U(|phi|^2)]
  = (1 - 2 Phi)[(1 - 2 Phi)|d_t phi|^2 - (1 + 2 Phi)|grad phi|^2 - U]
  = (1 - 4 Phi)|d_t phi|^2 - |grad phi|^2 - (1 - 2 Phi) U + O(Phi^2).
- **Stimmt mit der Karte ueberein.** Der Gradiententerm bekommt in erster Ordnung keinen Faktor, weil sich
  (1 - 2 Phi)(1 + 2 Phi) = 1 + O(Phi^2) aufhebt [ES].
- Kontrolle der Kopplung: Die Aenderung der Materie-Wirkung ist delta L = -Phi (4 |d_t phi|^2 - 2 U). Fuer
  phi = f e^{-i omega t} ist das -Phi (4 omega^2 f^2 - 2 U) = -Phi (rho + 3 p) mit rho = omega^2 f^2 + f'^2 + U und
  3 p = 3 omega^2 f^2 - f'^2 - 3 U (isotroper Mittelwert) [ES]. Das ist die bekannte Kopplung -(1/2) h_{mu nu} T^{mu nu}
  mit h_00 = -2 Phi, h_ij = -2 Phi delta_ij [L?].

## 2 Hintergrundgleichungen

- Euler-Lagrange nach phi*: d_t[(1 - 4 Phi) d_t phi] - lap phi + (1 - 2 Phi) U'(|phi|^2) phi = 0. Phi statisch:
  lap phi = (1 - 4 Phi) d_t^2 phi + (1 - 2 Phi) U'(|phi|^2) phi.
- Mit phi = f(r) e^{-i omega t} (d_t^2 -> -omega^2):
  **f'' + (2/r) f' = (1 - 2 Phi) U'(f^2) f - (1 - 4 Phi) omega^2 f** (wie Karte).
- Poisson (Karte, bindend): **Phi'' + (2/r) Phi' = alpha rho_E**, rho_E = omega^2 f^2 + f'^2 + U(f^2) = T_00.
  - Loesung mit Phi'(0) = 0, Phi(inf) = 0: Phi(r) = -alpha [m(r)/r + int_r^inf rho_E r' dr'], m(r) = int_0^r rho_E r'^2 dr'.
    Aussen Phi = -c/r mit c = alpha m(inf); mit alpha = 4 pi G ist c = G M, M = 4 pi m(inf) [ES].
  - **Vermerk zur Quelle (keine Aenderung der Regelfassung):**
    - Linearisierte ART mit zwei Potentialen (-(1 + 2 Phi) dt^2 + (1 - 2 Psi) dx^2): lap Psi = 4 pi G rho,
      lap Phi = 4 pi G (rho + 3 p) [L?, Lehrbuchstand].
    - Die Karte setzt Psi = Phi und nimmt rho als Quelle. Variiert man die Wirkung oben (mit Feldterm) nach diesem
      einen Phi, kaeme rho + 3 p = 4 omega^2 f^2 - 2 U heraus [ES].
    - Fuer nichtrelativistische Materie (p << rho) fallen alle Fassungen zusammen. Beim Q-Ball ist p lokal nicht
      klein. Integriert gilt fuer den flachen Ball int 3 p d^3x = 0 (Virial), also stimmt M aussen ueberein [ES].
      Innen unterscheidet sich Phi; die Lage der Stelle kann davon abhaengen.
    - Das ist eine Modellwahl der Karte ("Newton-Grenzfall"), kein Rechenfehler. Sie bleibt; im Bericht steht sie als
      Grenze. Ein Nebenlauf mit rho + 3 p (qstern.py --quelle rho3p) ist vorbereitet, aber nicht gerechnet.
- Startentwicklung am Ursprung (im Code): f = c + a r^2 + b r^4, Phi = Phi(0) + Phi2 r^2,
  6 a = G(c, Phi(0)), 20 b = G_f a + G_Phi Phi2, G_Phi = (4 omega^2 - 2 U'(c^2)) c.
- Schwanz (f klein, U' -> 1, Phi = -c/r): y = r f, y'' = [kappa^2 - 2 kappa eta / r] y mit kappa^2 = 1 - omega^2,
  eta = c (4 omega^2 - 2)/(2 kappa). Abklingend y ~ e^{-kappa r} r^eta, also f ~ e^{-kappa r} r^(eta - 1) und
  f'/f = -kappa + (eta - 1)/r. Damit klassifiziert das Schiessen im linearen Schwanz und setzt den Profilschwanz an.

## 3 Linearisierung (Cowling: delta Phi = 0)

- phi = e^{-i omega t} (f + psi), |f + psi|^2 = S + f (psi + psi*) + O(psi^2), S = f^2:
  U'(|phi|^2) phi -> e^{-i omega t} [U' f + (U' + S U'') psi + S U'' psi*].
- Linear: lap psi = (1 - 4 Phi)(d_t - i omega)^2 psi + (1 - 2 Phi)[dp psi + sp psi*], dp = U' + S U'', sp = S U''.
- Ansatz psi = a(x) e^{-i rho t} + b*(x) e^{+i rho t}:
  - Faktor e^{-i rho t}: (d_t - i omega)^2 -> -(omega + rho)^2:
    lap a = -(1 - 4 Phi)(omega + rho)^2 a + (1 - 2 Phi)[dp a + sp b]
  - Faktor e^{+i rho t}, danach konjugiert: lap b = -(1 - 4 Phi)(omega - rho)^2 b + (1 - 2 Phi)[dp b + sp a]
- l = 0, y = r w:
  - **offener Kanal (omega + rho):** y_a'' = [(1 - 2 Phi) dp - (1 - 4 Phi)(rho + omega)^2] y_a + (1 - 2 Phi) sp y_b
  - **geschlossener Kanal (omega - rho):** y_b'' = [(1 - 2 Phi) dp - (1 - 4 Phi)(rho - omega)^2] y_b + (1 - 2 Phi) sp y_a
  - Also: **(1 - 4 Phi) an den Frequenztermen, (1 - 2 Phi) an U' und U''** (in dp und sp). Das bestaetigt die Karte.
- Code-Form: A = (1 - 2 Phi) dp - (1 - 4 Phi) omega^2, B = 2 omega (1 - 4 Phi), C = (1 - 2 Phi) sp, D = 1 - 4 Phi;
  y1'' = (A + B rho - D rho^2) y1 + C y2 (geschlossen), y2'' = C y1 + (A - B rho - D rho^2) y2 (offen). Gegenueber
  bball2 neu ist nur D vor rho^2; mit Phi = 0 ist alles wie bisher. Das System bleibt reell-symmetrisch (C in beiden
  Zeilen gleich). Darum gilt der Wronski-Satz unveraendert.
- Schwellen: Phi(inf) = 0, also offen ab rho > 1 - omega und geschlossen bis rho < 1 + omega, wie bisher.

## 4 Langreichweite und Abstrahlamplitude

- Aussen (C ~ f^2 -> 0, dp -> 1) mit Phi = -c/r:
  - offen: y_a'' + [q^2 + c (4 (rho + omega)^2 - 2)/r] y_a = 0, q^2 = (rho + omega)^2 - 1. Das ist eine anziehende
    Coulomb-Gleichung; die Phase laeuft wie q r + eta_a ln(2 q r) mit eta_a = c (4 (rho + omega)^2 - 2)/(2 q) [ES].
  - geschlossen: y_b'' = [kappa_c^2 - c (4 (rho - omega)^2 - 2)/r] y_b, kappa_c^2 = 1 - (rho - omega)^2. Ebenfalls
    anziehend. [H] Unter der geschlossenen Schwelle gibt es darum eine Rydberg-artige Folge gebundener Zustaende im
    -c/r-Schwanz; die Rauchtests zeigen dort ein neues Nullstellenpaar.
- **Wahl: eine Groesse ohne Phase.** W = L(y_a) + i L(y_b), L(y) = Wronski-Summe von y mit z. z startet bei R mit
  z2 = z2' = 0 (offener Kanal exakt null) und z1 abklingend. Ausserhalb des Balls ist C < 1e-12 (Rand-Abweichung im
  Log), und Phi ist diagonal. Damit bleibt z2 fuer r >= R exakt null. W = 0 heisst: z ist am Ursprung regulaer. Das
  ist eine Loesung ganz ohne offenen Anteil, also eine stille Stelle. Es wird keine asymptotische Welle
  angepasst; die Coulomb-Phase eta_a ln(2 q r) kommt in W nicht vor [ES].
- Der einzige Phi-Einfluss am Rand ist der Start von z1: z1'/z1 = -kappa_c + eta_c/R,
  eta_c = c (4 (rho - omega)^2 - 2)/(2 kappa_c) (erste Ordnung in 1/R). Der Restfehler O(1/R^2) mischt eine nach
  aussen wachsende Komponente bei. Nach innen faellt sie mit e^{-2 kappa_c (R - r_m)} ab (an der Stelle kappa_c ~ 0,5,
  R - r_m ~ 25: e^{-25}). Nahe der geschlossenen Schwelle (kappa_c -> 0,063 am Abtastrand) ist das nicht klein. Darum
  K3: R gegen 1,5 R.
- Jenseits des eigenen Randes eines Profils setzt W_multi die Koeffizienten mit Phi = -c/r fort (nicht mit Phi = 0).
- Pole (Breiten) waeren mit der WKB-Wellenzahl q_lok = sqrt(q^2 + c (4 (rho + omega)^2 - 2)/R) vorbereitet; sie sind
  in den Laeufen nicht gerechnet (pole nein).

## 5 Numerik des Hintergrunds

- Schiessen in f(0) bei festem Phi; Klammer und Klassifikation wie bball2. Neu: Startklammer +-3 % um den letzten
  Wert, die nach oben bzw. unten ausweitet, bis beide Enden durch eine klassifizierte Probe bestaetigt sind.
- Phi aus rho_E per kumulativem Trapez mit Euler-Maclaurin-Endkorrektur (O(h^4)). Auf dem Feingitter (h/4) per
  kubischem Spline, jenseits des Profils -c/r.
- Iteration:
  - alpha in 6 Schritten hochfahren. Ohne Rampe ueberschiessen bei alpha = 0,1 alle Amplituden, weil das Phi des
    flachen Profils zu tief ist: Phi(0) < -0,167 macht (1 - 2 Phi) - (1 - 4 Phi) omega^2 innen negativ.
  - Danach Anderson(1)-Mischung, bis max |Phi_neu - Phi_alt| < 1e-9.
  - Einfache Mischung schwingt bei alpha = 0,1 mit Faktor ~ -0,87.
- Warmstart: Zwischenzeilen und Lokalisierung beginnen mit dem linear interpolierten Phi konvergierter Nachbarn.
